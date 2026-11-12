"""Small single-process web server for isolated, temporary game sessions."""

from collections import deque
from http import HTTPStatus
from http.cookies import CookieError, SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
import mimetypes
import os
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import threading
import time
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "code"))
import character_data

SESSION_LIMIT = 20
SESSION_TIMEOUT = 30 * 60
MAX_EVENTS = 10000
MAX_HIGH_SCORES = 5
HIGH_SCORES_FILE = ROOT / "files" / "HighScores.txt"
sessions = {}
sessions_lock = threading.Lock()
high_scores_lock = threading.Lock()


def valid_character(data):
    if not isinstance(data, dict) or set(data) - set(character_data.FIELDS):
        return False
    for field, value in data.items():
        if not isinstance(value, str) or not value.strip() or len(value) > 1024:
            return False
        if any(
            char in "\r\n\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029" or 0xD800 <= ord(char) <= 0xDFFF
            for char in value
        ):
            return False
        if field == "Age" and (not value.isascii() or not value.isdigit() or int(value) > 150):
            return False
    return True


def read_high_scores():
    try:
        lines = HIGH_SCORES_FILE.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []

    scores = []
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            logging.warning("Ignoring malformed high-score entry")
            continue
        name, raw_score = parts
        try:
            score = int(raw_score)
        except ValueError:
            logging.warning("Ignoring high-score entry with invalid score")
            continue
        if len(name) != 3 or not name.isascii() or not name.isalpha() or score < 0:
            logging.warning("Ignoring invalid high-score entry")
            continue
        scores.append({"name": name.upper(), "score": score})
    scores.sort(key=lambda entry: entry["score"], reverse=True)
    return scores[:MAX_HIGH_SCORES]


def write_high_scores(scores):
    HIGH_SCORES_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=HIGH_SCORES_FILE.parent,
            prefix=".HighScores.", suffix=".tmp", delete=False,
        ) as output:
            temporary_path = Path(output.name)
            for entry in scores:
                output.write(f'{entry["name"]} {entry["score"]}\n')
        os.replace(temporary_path, HIGH_SCORES_FILE)
    except OSError:
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass
        raise


class Session:
    def __init__(self, character, chapter8_unlocked):
        self.directory = tempfile.TemporaryDirectory(prefix="extinction-")
        try:
            if character:
                character_data.update_character(
                    Path(self.directory.name) / "files" / "character.txt",
                    **character_data.prepare_character(character),
                )
            if chapter8_unlocked:
                marker = Path(self.directory.name) / "files" / "chapter8_complete.txt"
                marker.parent.mkdir(parents=True, exist_ok=True)
                marker.write_text("Made By Alex Haworth", encoding="utf-8")
            self.process = subprocess.Popen(
                [sys.executable, "-B", "-u", str(ROOT / "web_game.py")],
                cwd=self.directory.name,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                text=True, encoding="utf-8", bufsize=1,
            )
        except OSError:
            self.directory.cleanup()
            raise
        self.events = deque()
        self.lock = threading.Lock()
        self.last_seen = time.monotonic()
        self.waiting = None
        self.closed = False
        threading.Thread(target=self.read_events, daemon=True).start()

    def read_events(self):
        try:
            for line in self.process.stdout:
                event = json.loads(line)
                with self.lock:
                    if len(self.events) >= MAX_EVENTS:
                        self.events.clear()
                        self.events.append({"type": "error", "message": "Game output limit exceeded. Start a new game."})
                        self.process.terminate()
                        break
                    if event["type"] in ("input", "arcade"):
                        self.waiting = event["type"]
                    self.events.append(event)
        except (ValueError, KeyError):
            logging.exception("Invalid game event")
            with self.lock:
                self.events.append({"type": "error", "message": "The game sent an invalid response."})
                if self.process.poll() is None:
                    self.process.terminate()
        finally:
            self.process.wait()
            with self.lock:
                if self.process.returncode and not self.closed:
                    self.events.append({"type": "error", "message": "The game stopped unexpectedly. Start a new game."})
                    self.events.append({"type": "finished"})

    def stop(self):
        with self.lock:
            if self.closed:
                return
            self.closed = True
            if self.process.poll() is None:
                self.process.terminate()
        try:
            self.process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()
        self.process.stdin.close()
        self.process.stdout.close()
        self.directory.cleanup()


def clean_sessions():
    while True:
        time.sleep(30)
        now = time.monotonic()
        with sessions_lock:
            expired = [key for key, session in sessions.items() if now - session.last_seen > SESSION_TIMEOUT]
            old = [sessions.pop(key) for key in expired]
        for session in old:
            session.stop()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        if self.path != "/api/events":
            super().log_message(format, *args)

    def reply(self, status, body, content_type="application/json; charset=utf-8", headers=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def session(self):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
        except CookieError:
            return None
        token = cookie.get("game_session")
        with sessions_lock:
            session = sessions.get(token.value) if token else None
            if session:
                session.last_seen = time.monotonic()
            return session

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/api/high-scores":
            try:
                with high_scores_lock:
                    scores = read_high_scores()
            except (OSError, UnicodeError):
                logging.exception("Unable to read high scores")
                return self.reply(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "Unable to load high scores."})
            return self.reply(HTTPStatus.OK, {"scores": scores})
        if path == "/api/events":
            session = self.session()
            if not session:
                return self.reply(HTTPStatus.NOT_FOUND, {"error": "Your session has expired. Start a new game."})
            with session.lock:
                events = list(session.events)
                session.events.clear()
            return self.reply(HTTPStatus.OK, {"events": events})
        if path == "/":
            path = "/static/index.html"
        parts = unquote(path).split("/")
        if len(parts) < 3 or parts[1] not in ("static", "images", "arcade"):
            return self.reply(HTTPStatus.NOT_FOUND, {"error": "Not found"})
        base = {"static": ROOT / "web", "images": ROOT / "images", "arcade": ROOT / "chapter8game"}[parts[1]]
        if parts[1] == "arcade" and (len(parts) < 4 or parts[2] not in ("images", "sounds", "font")):
            return self.reply(HTTPStatus.NOT_FOUND, {"error": "Not found"})
        target = (base / "/".join(parts[2:])).resolve()
        if not target.is_relative_to(base.resolve()) or not target.is_file():
            return self.reply(HTTPStatus.NOT_FOUND, {"error": "Not found"})
        self.reply(HTTPStatus.OK, target.read_bytes(), mimetypes.guess_type(target.name)[0] or "application/octet-stream")

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ("/api/start", "/api/input", "/api/stop", "/api/high-scores"):
            return self.reply(HTTPStatus.NOT_FOUND, {"error": "Not found"})
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            return self.reply(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, {"error": "Expected JSON"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 0 or length > 65536:
                raise ValueError("Invalid content length")
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError("Expected object")
        except (ValueError, json.JSONDecodeError):
            return self.reply(HTTPStatus.BAD_REQUEST, {"error": "Invalid request"})
        if path == "/api/high-scores":
            name = data.get("name")
            score = data.get("score")
            if (
                not isinstance(name, str) or len(name) != 3
                or not name.isascii() or not name.isalpha()
                or type(score) is not int or score < 0 or score > 2_147_483_647
            ):
                return self.reply(HTTPStatus.BAD_REQUEST, {"error": "Invalid high score"})
            entry = {"name": name.upper(), "score": score}
            try:
                with high_scores_lock:
                    scores = read_high_scores()
                    scores.append(entry)
                    scores.sort(key=lambda item: item["score"], reverse=True)
                    scores = scores[:MAX_HIGH_SCORES]
                    write_high_scores(scores)
            except (OSError, UnicodeError):
                logging.exception("Unable to save high scores")
                return self.reply(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "Unable to save high scores."})
            return self.reply(HTTPStatus.OK, {"scores": scores})
        if path == "/api/start":
            character = data.get("character", {})
            if not valid_character(character):
                return self.reply(HTTPStatus.BAD_REQUEST, {"error": "Invalid saved character data."})
            chapter8_unlocked = data.get("chapter8Unlocked", False)
            if type(chapter8_unlocked) is not bool:
                return self.reply(HTTPStatus.BAD_REQUEST, {"error": "Invalid chapter unlock data."})
            old = self.session()
            if old:
                with sessions_lock:
                    for key, value in list(sessions.items()):
                        if value is old:
                            del sessions[key]
                            break
                old.stop()
            with sessions_lock:
                if len(sessions) >= SESSION_LIMIT:
                    return self.reply(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "The server is full. Please try again later."})
                try:
                    session = Session(character, chapter8_unlocked)
                except OSError:
                    logging.exception("Unable to start game")
                    return self.reply(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "Unable to start the game."})
                token = secrets.token_urlsafe(32)
                sessions[token] = session
            return self.reply(HTTPStatus.OK, {"ok": True}, headers={"Set-Cookie": f"game_session={token}; Path=/; HttpOnly; SameSite=Strict"})
        session = self.session()
        if not session:
            return self.reply(HTTPStatus.NOT_FOUND, {"error": "Your session has expired. Start a new game."})
        if path == "/api/stop":
            with sessions_lock:
                for key, value in list(sessions.items()):
                    if value is session:
                        del sessions[key]
                        break
            session.stop()
            return self.reply(HTTPStatus.OK, {"ok": True}, headers={"Set-Cookie": "game_session=; Path=/; Max-Age=0; HttpOnly; SameSite=Strict"})
        value = data.get("value")
        if (
            not isinstance(value, str) or len(value) > 1024
            or any(
                char in "\r\n\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029" or 0xD800 <= ord(char) <= 0xDFFF
                for char in value
            )
        ):
            return self.reply(HTTPStatus.BAD_REQUEST, {"error": "Invalid input"})
        with session.lock:
            if not session.waiting or session.closed or session.process.poll() is not None:
                return self.reply(HTTPStatus.CONFLICT, {"error": "The game is not waiting for input."})
            try:
                session.process.stdin.write(value + "\n")
                session.process.stdin.flush()
            except (BrokenPipeError, OSError):
                logging.exception("Could not send game input")
                return self.reply(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": "The game stopped unexpectedly."})
            session.waiting = None
        return self.reply(HTTPStatus.OK, {"ok": True})


def main():
    logging.basicConfig(level=logging.INFO)
    threading.Thread(target=clean_sessions, daemon=True).start()
    port = int(os.environ.get("PORT", "10000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        with sessions_lock:
            active = list(sessions.values())
            sessions.clear()
        for session in active:
            session.stop()


if __name__ == "__main__":
    main()
