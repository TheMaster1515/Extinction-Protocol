import http.client
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock

import web_game
import web_server


class WebTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = web_server.ThreadingHTTPServer(("127.0.0.1", 0), web_server.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_port

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def tearDown(self):
        with web_server.sessions_lock:
            sessions = list(web_server.sessions.values())
            web_server.sessions.clear()
        for session in sessions:
            session.stop()

    def request(self, method, path, data=None, cookie=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        headers = {}
        body = None
        if data is not None:
            headers["Content-Type"] = "application/json"
            body = json.dumps(data)
        if cookie:
            headers["Cookie"] = cookie
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        contents = response.read()
        headers = dict(response.getheaders())
        status = response.status
        connection.close()
        return status, headers, contents

    def start(self):
        status, headers, _ = self.request("POST", "/api/start", {})
        self.assertEqual(status, 200)
        return headers["Set-Cookie"].split(";", 1)[0]

    def wait_for(self, cookie, event_type, timeout=4):
        events = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            status, _, body = self.request("GET", "/api/events", cookie=cookie)
            self.assertEqual(status, 200)
            events.extend(json.loads(body)["events"])
            if any(event["type"] == event_type for event in events):
                return events
            time.sleep(0.02)
        self.fail(f"Timed out waiting for {event_type}: {events}")

    def answer(self, cookie, value):
        status, _, body = self.request("POST", "/api/input", {"value": value}, cookie)
        self.assertEqual(status, 200, body)

    def test_story_and_isolated_player_data(self):
        first = self.start()
        second = self.start()
        for cookie, name in ((first, "Alice"), (second, "Bob")):
            self.wait_for(cookie, "input")
            self.answer(cookie, name)
            self.wait_for(cookie, "input")
            self.answer(cookie, "25")
            self.wait_for(cookie, "input")
            self.answer(cookie, "America")
            self.wait_for(cookie, "input")
            self.answer(cookie, "")
            events = self.wait_for(cookie, "input")
            self.assertIn("Choose which chapter", "".join(event.get("text", "") for event in events))

        with web_server.sessions_lock:
            players = list(web_server.sessions.values())
        self.assertEqual(len(players), 2)
        first_data = (web_server.Path(players[0].directory.name) / "files/data.txt").read_text()
        second_data = (web_server.Path(players[1].directory.name) / "files/data.txt").read_text()
        self.assertIn("Alice", first_data)
        self.assertNotIn("Bob", first_data)
        self.assertIn("Bob", second_data)
        self.assertNotIn("Alice", second_data)

        self.answer(second, "2.1")
        events = self.wait_for(second, "input")
        self.assertIn("basic training", "".join(event.get("text", "") for event in events))

        self.answer(first, "1")
        events = self.wait_for(first, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("Alice", output)
        self.answer(first, "")
        events = self.wait_for(first, "image")
        self.assertEqual(next(event["path"] for event in events if event["type"] == "image"), "images/background.jpg")
        self.assertEqual(self.request("GET", "/images/background.jpg")[0], 200)
        self.assertEqual(self.request("GET", "/arcade/images/player.png")[0], 200)

    def test_moon_chapter_can_be_selected(self):
        cookie = self.start()
        for value in ("Moon player", "25", "America", ""):
            self.wait_for(cookie, "input")
            self.answer(cookie, value)
        self.wait_for(cookie, "input")
        self.answer(cookie, "2.2")
        events = self.wait_for(cookie, "input")
        self.assertFalse(any(event["type"] == "error" for event in events))
        self.assertNotIn("Invalid option", "".join(event.get("text", "") for event in events))

    def test_validation_stop_and_restart(self):
        cookie = self.start()
        self.wait_for(cookie, "input")
        self.assertEqual(self.request("POST", "/api/input", {"value": "a\nb"}, cookie)[0], 400)
        self.assertEqual(self.request("GET", "/arcade/../web_game.py")[0], 404)
        self.assertEqual(self.request("POST", "/api/stop", {}, cookie)[0], 200)
        self.assertEqual(self.request("GET", "/api/events", cookie=cookie)[0], 404)
        new_cookie = self.start()
        self.wait_for(new_cookie, "input")
        status, _, _ = self.request("POST", "/api/start", {}, new_cookie)
        self.assertEqual(status, 200)

    def test_arcade_bridge(self):
        with mock.patch.object(web_game, "emit") as emit, mock.patch.object(web_game, "protocol_in") as stream:
            stream.readline.return_value = "\n"
            result = web_game.run_arcade(["python3", "chapter8game/EasterEgg.py"])
            self.assertEqual(result.returncode, 0)
            emit.assert_called_once_with("arcade")
            with self.assertRaises(RuntimeError):
                web_game.run_arcade(["other"])

    def test_chapter_eight_hands_off_and_returns_to_story(self):
        root = str(Path(web_game.__file__).resolve().parent)
        code = """
import builtins, io, os, subprocess, sys
sys.path.insert(0, sys.argv[1])
import web_game
sys.path.insert(0, os.path.join(sys.argv[1], "code"))
sys.modules["cv2"] = web_game.make_cv2()
import chapter8
chapter8.time.sleep = lambda seconds: None
chapter8.chapterX.chapterx = lambda: None
builtins.input = lambda prompt="": ""
web_game.protocol_in = io.StringIO("\\n")
subprocess.run = web_game.run_arcade
os.mkdir("files")
chapter8.Game().chapter8()
assert os.path.exists("files/chapter8_complete.txt")
"""
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-B", "-c", code, root],
                cwd=directory, text=True, capture_output=True, timeout=10,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"type": "arcade"', result.stdout)
        self.assertIn("There is something hidden in each chapter", result.stdout)


if __name__ == "__main__":
    unittest.main()
