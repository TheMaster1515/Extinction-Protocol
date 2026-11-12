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

    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.character_file = Path(directory.name) / "files" / "character.txt"
        self.job_file = self.character_file.parent / "job.txt"
        self.characters = {}

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

    def start(self, design=True, character=None, chapter8_unlocked=False):
        status, headers, _ = self.request(
            "POST", "/api/start", {"character": character or {}, "chapter8Unlocked": chapter8_unlocked}
        )
        self.assertEqual(status, 200)
        cookie = headers["Set-Cookie"].split(";", 1)[0]
        self.characters[cookie] = dict(character or {})
        if design:
            self.wait_for(cookie, "input")
            self.answer(cookie, "2")
        return cookie

    def wait_for(self, cookie, event_type, timeout=4):
        events = []
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            status, _, body = self.request("GET", "/api/events", cookie=cookie)
            self.assertEqual(status, 200)
            received = json.loads(body)["events"]
            for event in received:
                if event["type"] == "character_update":
                    self.characters[cookie].update(event["changes"])
            events.extend(received)
            if any(event["type"] == event_type for event in events):
                return events
            time.sleep(0.02)
        self.fail(f"Timed out waiting for {event_type}: {events}")

    def answer(self, cookie, value):
        status, _, body = self.request("POST", "/api/input", {"value": value}, cookie)
        self.assertEqual(status, 200, body)

    def test_start_menu_validates_choice_and_designs_character(self):
        cookie = self.start(design=False)
        events = self.wait_for(cookie, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("1. Start at a level", output)
        self.assertIn("2. Design your character", output)
        self.answer(cookie, "9")
        events = self.wait_for(cookie, "input")
        self.assertIn("Invalid option", "".join(event.get("text", "") for event in events))
        self.answer(cookie, "2")
        events = self.wait_for(cookie, "input")
        self.assertTrue(any("character's name" in event.get("prompt", "") for event in events))

    def test_start_at_level_loads_latest_saved_character(self):
        character = {"Name": "Latest", "Age": "30", "Colony": "Russia", "Person": "Friend", "Ship": "Star", "Job": "Pilot"}
        cookie = self.start(design=False, character=character)
        self.wait_for(cookie, "input")
        self.answer(cookie, "1")
        events = self.wait_for(cookie, "input")
        self.assertIn("Choose which chapter", "".join(event.get("text", "") for event in events))
        self.answer(cookie, "3")
        events = self.wait_for(cookie, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("Name: Latest", output)
        self.assertIn("Job: Pilot", output)
        self.assertIn("Friend: Friend", output)
        self.assertIn("Ship: Star", output)

    def test_start_at_level_without_saved_character(self):
        cookie = self.start(design=False)
        self.wait_for(cookie, "input")
        self.answer(cookie, "1")
        events = self.wait_for(cookie, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("No saved character found", output)
        self.assertIn("Choose which chapter", output)
        self.assertFalse(self.character_file.exists())
        self.answer(cookie, "1")
        events = self.wait_for(cookie, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("Name: Unknown", output)
        self.assertFalse(any(event["type"] == "error" for event in events))

    def test_start_at_level_saves_subsequent_job_choice(self):
        character = {"Name": "Saved", "Age": "25", "Colony": "America", "Person": "Friend", "Ship": "Star", "Job": "Engineer"}
        cookie = self.start(design=False, character=character)
        for value in ("1", "2", ""):
            self.wait_for(cookie, "input")
            self.answer(cookie, value)
        self.wait_for(cookie, "input", timeout=10)
        self.answer(cookie, "")
        self.wait_for(cookie, "input")
        self.answer(cookie, "1")
        self.wait_for(cookie, "input")
        self.assertEqual(self.characters[cookie], {**character, "Job": "Pilot"})

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
        first_data = (web_server.Path(players[0].directory.name) / "files/character.txt").read_text()
        second_data = (web_server.Path(players[1].directory.name) / "files/character.txt").read_text()
        self.assertIn("Alice", first_data)
        self.assertNotIn("Bob", first_data)
        self.assertIn("Bob", second_data)
        self.assertNotIn("Alice", second_data)
        self.assertEqual(self.characters[first]["Name"], "Alice")
        self.assertEqual(self.characters[second]["Name"], "Bob")
        self.assertFalse(self.character_file.exists())

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
        self.assertEqual(self.request("GET", "/arcade/font/RetroFont.ttf")[0], 200)

    def test_character_data_is_saved_and_overwritten_by_new_game(self):
        cookie = self.start()
        for value in ("First player", "25", "America", ""):
            self.wait_for(cookie, "input")
            self.answer(cookie, value)
        self.wait_for(cookie, "input")
        saved = self.characters[cookie].copy()
        self.assertEqual(saved, {"Name": "First player", "Age": "25", "Colony": "America"})
        self.assertEqual(self.request("POST", "/api/stop", {}, cookie)[0], 200)

        cookie = self.start(character=saved)
        for value in ("New player", "31", "China", ""):
            self.wait_for(cookie, "input")
            self.answer(cookie, value)
        self.wait_for(cookie, "input")
        self.assertEqual(self.characters[cookie], {"Name": "New player", "Age": "31", "Colony": "China"})

    def test_invalid_saved_character_is_rejected(self):
        for character in ({"Age": "bad"}, {"Name": "Alice\nJob: Pilot"}, {"Extra": "value"}, []):
            with self.subTest(character=character):
                status, _, _ = self.request("POST", "/api/start", {"character": character})
                self.assertEqual(status, 400)

    def test_chapter_eight_unlock_is_restored_per_session(self):
        for unlocked in (True, False, True):
            with self.subTest(unlocked=unlocked):
                cookie = self.start(design=False, chapter8_unlocked=unlocked)
                self.wait_for(cookie, "input")
                self.answer(cookie, "1")
                events = self.wait_for(cookie, "input")
                output = "".join(event.get("text", "") for event in events)
                self.assertEqual("8.Chapter 8" in output, unlocked)
                prompt = next(event["prompt"] for event in events if event["type"] == "input")
                self.assertIn("1 through 8" if unlocked else "1 through 7", prompt)
                self.answer(cookie, "8")
                if unlocked:
                    events = self.wait_for(cookie, "arcade")
                    self.assertNotIn("Welcome to Chapter 8", "".join(event.get("text", "") for event in events))
                    self.answer(cookie, "")
                    events = self.wait_for(cookie, "input")
                    self.assertIn("8.Chapter 8", "".join(event.get("text", "") for event in events))
                else:
                    events = self.wait_for(cookie, "input", timeout=5)
                    self.assertIn("Chapter 8 is locked", "".join(event.get("text", "") for event in events))
        for invalid in ("true", 1, None, {}):
            with self.subTest(invalid=invalid):
                self.assertEqual(self.request("POST", "/api/start", {"chapter8Unlocked": invalid})[0], 400)

    def test_friend_and_ship_are_combined_with_character_in_both_paths(self):
        for chapter, choices in (
            ("2.1", ("1", "1", "1", "1", "1")),
            ("2.2", ("2", "2", "1", "1", "1")),
        ):
            with self.subTest(chapter=chapter):
                old = {"Name": "Old", "Age": "20", "Colony": "China", "Person": "Old Friend", "Ship": "Old Ship", "Job": "Engineer"}
                cookie = self.start(character=old)
                for value in ("Player", "25", "America", "", chapter):
                    self.wait_for(cookie, "input")
                    self.answer(cookie, value)
                for choice in choices:
                    self.wait_for(cookie, "input")
                    self.answer(cookie, choice)
                    self.wait_for(cookie, "input")
                    self.answer(cookie, "")
                self.wait_for(cookie, "input")
                self.answer(cookie, "Friend")
                self.wait_for(cookie, "input")
                self.assertEqual(self.characters[cookie], {
                    "Name": "Player", "Age": "25", "Colony": "America",
                    "Person": "Friend", "Ship": "Old Ship", "Job": "Engineer",
                })
                self.answer(cookie, "")
                self.wait_for(cookie, "input")
                self.answer(cookie, "Stargazer")
                self.wait_for(cookie, "input")
                self.assertEqual(self.characters[cookie]["Ship"], "Stargazer")
                self.answer(cookie, "")
                events = self.wait_for(cookie, "input")
                output = "".join(event.get("text", "") for event in events)
                self.assertIn("Name: Player", output)
                self.assertIn("Friend: Friend", output)
                self.assertIn("Ship: Stargazer", output)
                self.assertEqual(self.request("POST", "/api/stop", {}, cookie)[0], 200)
                saved = self.characters[cookie].copy()
                cookie = self.start(character=saved)
                for value in ("Next", "30", "Russia", "", "3"):
                    self.wait_for(cookie, "input")
                    self.answer(cookie, value)
                events = self.wait_for(cookie, "input")
                output = "".join(event.get("text", "") for event in events)
                self.assertIn("Friend: Friend", output)
                self.assertIn("Ship: Stargazer", output)
                self.assertIn("Job: Engineer", output)
                self.assertEqual(self.request("POST", "/api/stop", {}, cookie)[0], 200)

    def test_job_is_carried_into_new_game_and_overwritten_by_new_choice(self):
        first = self.start()
        second = self.start()
        for cookie, name in ((first, "First"), (second, "Second")):
            for value in (name, "25", "America", ""):
                self.wait_for(cookie, "input")
                self.answer(cookie, value)
            self.wait_for(cookie, "input")
            self.answer(cookie, "2")
            self.wait_for(cookie, "input")
            self.answer(cookie, "")

        for cookie, choice in ((second, "4"), (first, "1")):
            self.wait_for(cookie, "input", timeout=10)
            self.answer(cookie, "")
            self.wait_for(cookie, "input")
            self.answer(cookie, choice)
            self.wait_for(cookie, "input")
        self.assertEqual(self.characters[second]["Job"], "Engineer")
        self.assertEqual(self.characters[first]["Job"], "Pilot")
        self.assertFalse(self.job_file.exists())
        self.assertEqual(self.characters[second]["Name"], "Second")

        third = self.start(character=self.characters[second])
        for value in ("Third", "30", "China", ""):
            self.wait_for(third, "input")
            self.answer(third, value)
        self.wait_for(third, "input")
        self.assertEqual(self.characters[third]["Job"], "Engineer")
        self.answer(third, "3")
        events = self.wait_for(third, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("Job: Engineer", output)

        fourth = self.start(character=self.characters[third])
        for value in ("Fourth", "28", "Russia", "", "2", ""):
            self.wait_for(fourth, "input")
            self.answer(fourth, value)
        self.wait_for(fourth, "input", timeout=10)
        self.answer(fourth, "")
        self.wait_for(fourth, "input")
        self.answer(fourth, "1")
        self.wait_for(fourth, "input")
        self.assertEqual(self.characters[fourth]["Job"], "Pilot")

    def test_new_game_without_previous_job_uses_unknown(self):
        cookie = self.start()
        for value in ("Player", "25", "America", "", "3"):
            self.wait_for(cookie, "input")
            self.answer(cookie, value)
        events = self.wait_for(cookie, "input")
        output = "".join(event.get("text", "") for event in events)
        self.assertIn("Job: Unknown", output)
        self.assertFalse(self.job_file.exists())

    def test_separate_browser_saves_remain_independent(self):
        computer = {"Name": "Computer", "Age": "25", "Colony": "America", "Job": "Pilot"}
        phone = {"Name": "Phone", "Age": "30", "Colony": "China", "Job": "Engineer"}
        for character in (computer, phone, computer):
            cookie = self.start(design=False, character=character)
            for value in ("1", "3"):
                self.wait_for(cookie, "input")
                self.answer(cookie, value)
            events = self.wait_for(cookie, "input")
            output = "".join(event.get("text", "") for event in events)
            self.assertIn(f"Name: {character['Name']}", output)
            self.assertIn(f"Job: {character['Job']}", output)

    def test_local_character_updates_preserve_other_fields_and_migrate_job(self):
        self.character_file.parent.mkdir(parents=True)
        self.character_file.write_text(
            "Name: Old\nAge: 20\nColony: China\nPerson: Friend\nShip: Star\n",
            encoding="utf-8",
        )
        self.job_file.write_text("Job: Engineer\n", encoding="utf-8")
        web_server.character_data.update_character(
            self.character_file, Name="New", Age=30, Colony="Russia"
        )
        web_server.character_data.update_character(self.character_file, Person="New Friend")
        self.assertEqual(
            self.character_file.read_text(encoding="utf-8"),
            "Name: New\nAge: 30\nColony: Russia\nPerson: New Friend\nShip: Star\nJob: Engineer\n",
        )

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

    def test_high_scores_are_saved_and_limited_to_top_five(self):
        with tempfile.TemporaryDirectory() as directory:
            score_file = Path(directory) / "files" / "HighScores.txt"
            with mock.patch.object(web_server, "HIGH_SCORES_FILE", score_file):
                status, _, body = self.request("GET", "/api/high-scores")
                self.assertEqual(status, 200)
                self.assertEqual(json.loads(body)["scores"], [])

                submitted = []
                for score in (10, 70, 30, 50, 20, 90, 40):
                    submitted.append(score)
                    status, _, body = self.request(
                        "POST", "/api/high-scores", {"name": "you", "score": score}
                    )
                    self.assertEqual(status, 200)
                    self.assertEqual(
                        [entry["score"] for entry in json.loads(body)["scores"]],
                        sorted(submitted, reverse=True)[:5],
                    )

                saved = score_file.read_text(encoding="utf-8").splitlines()
                self.assertEqual(saved, ["YOU 90", "YOU 70", "YOU 50", "YOU 40", "YOU 30"])
                self.assertEqual(self.request("GET", "/api/high-scores")[0], 200)
                status, _, _ = self.request(
                    "POST", "/api/high-scores", {"name": "AB", "score": 100}
                )
                self.assertEqual(status, 400)

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
import io, os, sys
sys.path.insert(0, sys.argv[1])
import web_game
sys.path.insert(0, os.path.join(sys.argv[1], "code"))
sys.modules["cv2"] = web_game.make_cv2()
import chapter8, chapterZ
chapter8.time.sleep = lambda seconds: None
chapter8.chapterX.chapterx = lambda: None
chapterZ.chapterz = lambda: chapter8.Game().chapter8()
web_game.protocol_in = io.StringIO("\\n\\n")
web_game.main()
assert os.path.exists("files/chapter8_complete.txt")
"""
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-B", "-c", code, root],
                cwd=directory, text=True, capture_output=True, timeout=10,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"type": "arcade"', result.stdout)
        self.assertIn('"type": "chapter8_unlocked"', result.stdout)
        self.assertIn("Welcome to Chapter 8", result.stdout)
        self.assertIn("There is something hidden in each chapter", result.stdout)


if __name__ == "__main__":
    unittest.main()
