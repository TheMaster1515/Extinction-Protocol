import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "chapter8game"))

import pygame
import EasterEgg


class DesktopArcadeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((EasterEgg.WIDTH, EasterEgg.HEIGHT))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.game = EasterEgg.Game(self.screen)
        self.game.begin()
        self.random = patch.object(EasterEgg.random, "random", return_value=1)
        self.random.start()
        self.addCleanup(self.random.stop)
        self.addCleanup(pygame.mixer.music.stop)
        self.keys = {key: False for key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_x)}

    def key(self, key, character=""):
        return self.game.handle_event(pygame.event.Event(pygame.KEYDOWN, key=key, unicode=character))

    def hit(self):
        self.game.objects.append(EasterEgg.Object("enemy", self.game.player.x, self.game.player.y, 100, 100))
        self.game.update(0, self.keys)

    def test_lives_pause_and_game_over(self):
        self.game.draw()
        self.hit()
        self.assertEqual(self.game.lives, 2)
        self.hit()
        self.assertEqual(self.game.lives, 2)
        self.key(pygame.K_p)
        self.assertEqual(self.game.state, "paused")
        self.game.draw()
        self.game.update(10000, self.keys)
        self.assertEqual(self.game.time, 0)
        self.key(pygame.K_p)
        self.game.update(1999, self.keys)
        self.hit()
        self.assertEqual(self.game.lives, 2)
        self.game.update(1, self.keys)
        self.hit()
        self.assertEqual(self.game.lives, 1)
        self.game.update(2000, self.keys)
        self.hit()
        self.assertEqual(self.game.lives, 0)
        self.assertEqual(self.game.state, "flash")
        self.game.draw()
        self.game.update(1799, self.keys)
        self.assertEqual(self.game.state, "flash")
        self.game.update(1, self.keys)
        self.assertEqual(self.game.state, "initials")
        self.game.draw()

    def test_scoring_and_held_fire(self):
        self.game.objects.append(EasterEgg.Object("prize", 437, 400, 50, 50))
        self.game.shots.append(EasterEgg.Object("blaster", 100, 100, 19, 78))
        self.game.objects.append(EasterEgg.Object("enemy", 100, 100, 100, 100))
        self.game.update(0, self.keys)
        self.assertEqual(self.game.score, 85)
        self.keys[pygame.K_x] = True
        self.game.update(0, self.keys)
        self.assertEqual(len(self.game.shots), 1)
        self.game.update(499, self.keys)
        self.assertEqual(len(self.game.shots), 1)
        self.game.update(1, self.keys)
        self.assertEqual(len(self.game.shots), 2)

    def test_initials_shared_scores_and_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "HighScores.txt"
            path.write_text("OLD 100\n", encoding="utf-8")
            with patch.object(EasterEgg.web_server, "HIGH_SCORES_FILE", path):
                self.game.score = 125
                self.game.state = "initials"
                for letter in "ab1c":
                    self.key(ord(letter), letter)
                self.assertEqual(self.game.initials, "ABC")
                self.key(pygame.K_RETURN)
                self.assertEqual(self.game.state, "high_scores")
                self.assertEqual(path.read_text(encoding="utf-8"), "ABC 125\nOLD 100\n")
                self.game.draw()
                self.key(pygame.K_p)
                self.assertEqual((self.game.state, self.game.lives, self.game.score), ("playing", 3, 0))

    def test_save_failure_stays_on_initials_for_retry(self):
        self.game.state = "initials"
        self.game.initials = "ABC"
        with patch.object(EasterEgg.web_server, "write_high_scores", side_effect=OSError("disk error")):
            with patch.object(EasterEgg.web_server, "read_high_scores", return_value=[]):
                with self.assertLogs(level="ERROR"):
                    self.key(pygame.K_RETURN)
        self.assertEqual(self.game.state, "initials")
        self.assertTrue(self.game.score_error)


if __name__ == "__main__":
    unittest.main()
