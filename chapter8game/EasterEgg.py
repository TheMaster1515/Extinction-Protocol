import logging
import random
import sys
from dataclasses import dataclass
from pathlib import Path

import pygame

ROOT = Path(__file__).resolve().parent.parent
ASSETS = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import web_server

WIDTH, HEIGHT = 1000, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GAME_OVER_FLASH_MS = 1800


@dataclass
class Object:
    kind: str
    x: float
    y: float
    w: int
    h: int
    speed: float = 0
    shot: float = 0
    dead: bool = False


def overlap(a, b):
    return a.x < b.x + b.w and a.x + a.w > b.x and a.y < b.y + b.h and a.y + a.h > b.y


class Game:
    def __init__(self, screen):
        self.screen = screen
        sizes = {
            "background": (1000, 1200), "player": (125, 125),
            "enemy": (100, 100), "prize": (50, 50), "blaster": (19, 78),
            "friend": (100, 100), "asteroid": (100, 100),
            "enemy_blaster": (19, 78),
        }
        self.images = {}
        for name, size in sizes.items():
            extension = "jpg" if name == "background" else "png"
            image = pygame.image.load(str(ASSETS / "images" / f"{name}.{extension}")).convert_alpha()
            self.images[name] = pygame.transform.scale(image, size)
        self.sounds = {
            name: pygame.mixer.Sound(str(ASSETS / "sounds" / f"{name}.mp3"))
            for name in ("blaster", "prize", "destruction")
        }
        self.font_path = str(ASSETS / "font" / "RetroFont.ttf")
        self.fonts = {size: pygame.font.Font(self.font_path, size) for size in (22, 28, 36, 48, 56, 64)}
        self.state = "menu"
        self.score = 0
        self.initials = ""
        self.score_error = False
        self.high_scores = []

    def begin(self):
        self.player = Object("player", 437, 400, 125, 125)
        self.objects = []
        self.shots = []
        self.enemy_shots = []
        self.score = 0
        self.lives = 3
        self.time = 0
        self.last_shot = -500
        self.invulnerable_until = 0
        self.initials = ""
        self.score_error = False
        self.state = "playing"
        pygame.mixer.music.load(str(ASSETS / "sounds" / "arcade.mp3"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def spawn(self, kind, width, height, speed, y):
        self.objects.append(Object(kind, random.random() * (WIDTH - width), y, width, height, speed, self.time))

    def lose_life(self):
        if self.state != "playing" or self.time < self.invulnerable_until:
            return
        self.lives -= 1
        self.invulnerable_until = self.time + 2000
        self.player.x, self.player.y = 437, 400
        self.sounds["destruction"].play()
        if self.lives <= 0:
            self.state = "flash"
            self.game_over_started = self.time
            pygame.mixer.music.stop()

    def update(self, milliseconds, keys):
        if self.state == "flash":
            self.time += milliseconds
            if self.time - self.game_over_started >= GAME_OVER_FLASH_MS:
                self.state = "initials"
            return
        if self.state != "playing":
            return

        self.time += milliseconds
        step = min(milliseconds / (1000 / 60), 3)
        self.player.x = max(0, min(875, self.player.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 6 * step))
        self.player.y = max(0, min(475, self.player.y + (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 6 * step))
        if keys[pygame.K_x] and self.time - self.last_shot >= 500:
            self.last_shot = self.time
            self.shots.append(Object("blaster", self.player.x + 53, self.player.y, 19, 78))
            self.sounds["blaster"].play()

        for shot in self.shots:
            shot.y -= 18 * step
        for shot in self.enemy_shots:
            shot.y += 9 * step
        for obj in self.objects:
            obj.y += obj.speed * step
            if obj.kind == "enemy" and self.time - obj.shot > 3000:
                obj.shot = self.time
                self.enemy_shots.append(Object("enemy_blaster", obj.x + 40, obj.y + 100, 19, 78))

        collision = Object("collision", self.player.x + 32, self.player.y + 22, 60, 80)
        for obj in self.objects:
            if obj.dead:
                continue
            if obj.kind in ("enemy", "asteroid") and overlap(collision, obj):
                obj.dead = True
                self.lose_life()
                if self.state != "playing":
                    return
                continue
            if obj.kind == "prize" and overlap(self.player, obj):
                obj.dead = True
                self.score += 10
                self.sounds["prize"].play()
            if obj.kind in ("enemy", "asteroid"):
                for shot in self.shots:
                    if not shot.dead and overlap(shot, obj):
                        shot.dead = obj.dead = True
                        self.score += 75 if obj.kind == "enemy" else 20
                        self.sounds["destruction"].play()
                        break

        for shot in self.enemy_shots:
            if not shot.dead and overlap(self.player, shot):
                shot.dead = True
                self.lose_life()
                if self.state != "playing":
                    return
                break

        self.objects = [obj for obj in self.objects if not obj.dead and obj.y < 700]
        self.shots = [shot for shot in self.shots if not shot.dead and shot.y + shot.h > 0]
        self.enemy_shots = [shot for shot in self.enemy_shots if not shot.dead and shot.y < 700]
        for kind, width, height, speed, y, probability in (
            ("enemy", 100, 100, 1, -200, 0.001),
            ("asteroid", 100, 100, 3, -1000, 0.005),
            ("prize", 50, 50, 2, -2000, 0.02),
            ("friend", 100, 100, 5, -1000, 0.01),
        ):
            if random.random() < 1 - (1 - probability) ** step:
                self.spawn(kind, width, height, speed, y)

    def save_score(self):
        with web_server.high_scores_lock:
            scores = web_server.read_high_scores()
            scores.append({"name": self.initials, "score": self.score})
            scores.sort(key=lambda entry: entry["score"], reverse=True)
            self.high_scores = scores[:web_server.MAX_HIGH_SCORES]
            web_server.write_high_scores(self.high_scores)
        self.state = "high_scores"

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False
        if event.type != pygame.KEYDOWN:
            return True
        if event.key == pygame.K_ESCAPE:
            return False
        if self.state == "menu":
            if event.key == pygame.K_p:
                self.begin()
            elif event.key == pygame.K_q:
                return False
        elif self.state in ("playing", "paused") and event.key == pygame.K_p:
            if self.state == "playing":
                self.state = "paused"
                pygame.mixer.music.pause()
            else:
                self.state = "playing"
                pygame.mixer.music.unpause()
        elif self.state == "initials":
            if event.key == pygame.K_BACKSPACE:
                self.initials = self.initials[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and len(self.initials) == 3:
                try:
                    self.save_score()
                    self.score_error = False
                except (OSError, UnicodeError):
                    logging.exception("Unable to save high scores")
                    self.score_error = True
            elif len(self.initials) < 3 and event.unicode.isascii() and event.unicode.isalpha():
                self.initials += event.unicode.upper()
        elif self.state == "high_scores":
            if event.key in (pygame.K_p, pygame.K_y, pygame.K_RETURN):
                self.begin()
            elif event.key in (pygame.K_q, pygame.K_n):
                return False
        return True

    def text(self, value, size, x, y, align="center"):
        surface = self.fonts[size].render(value, True, WHITE)
        rect = surface.get_rect()
        if align == "left":
            rect.midleft = (x, y)
        elif align == "right":
            rect.midright = (x, y)
        else:
            rect.center = (x, y)
        self.screen.blit(surface, rect)

    def draw(self):
        self.screen.fill(BLACK)
        if self.state == "menu":
            self.text("Press P to Play", 48, 500, 250)
            self.text("Press Q to Quit", 48, 500, 350)
        elif self.state in ("playing", "paused"):
            self.screen.blit(self.images["background"], (0, 0))
            for obj in self.objects + self.shots + self.enemy_shots:
                self.screen.blit(self.images[obj.kind], (obj.x, obj.y))
            if self.time >= self.invulnerable_until or int(self.time / 100) % 2 == 0:
                self.screen.blit(self.images["player"], (self.player.x, self.player.y))
            self.text(f"Score: {self.score}", 28, 10, 25, "left")
            self.text(f"Lives: {self.lives}", 28, 990, 25, "right")
            if self.state == "paused":
                overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 187))
                self.screen.blit(overlay, (0, 0))
                self.text("PAUSED", 48, 500, 300)
        elif self.state == "flash":
            if int((self.time - self.game_over_started) / 250) % 2 == 0:
                self.text("GAME OVER", 64, 500, 300)
        elif self.state == "initials":
            self.text("GAME OVER", 48, 500, 115)
            self.text(f"Final score: {self.score}", 28, 500, 175)
            self.text("Enter three initials for the high score", 22, 500, 270)
            self.text(" ".join(self.initials.ljust(3, "_")), 56, 500, 365)
            self.text("Type letters, then press Enter", 22, 500, 435)
            if self.score_error:
                self.text("Could not save score. Press Enter to retry.", 22, 500, 490)
        elif self.state == "high_scores":
            self.text("GAME OVER", 48, 500, 100)
            self.text(f"Final score: {self.score}", 28, 500, 155)
            self.text("HIGH SCORES", 36, 500, 230)
            for index, entry in enumerate(self.high_scores):
                self.text(f'{index + 1}. {entry["name"]} {entry["score"]}', 28, 500, 290 + index * 48)
            self.text("P: Play again    Q: Quit", 22, 500, 565)
        pygame.display.flip()


def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chapter 8: The Hunt For The Egg")
        pygame.display.set_icon(pygame.image.load(str(ASSETS / "icon" / "icon.ico")))
        game = Game(screen)
        clock = pygame.time.Clock()
        running = True
        while running:
            elapsed = clock.tick(FPS)
            for event in pygame.event.get():
                if not game.handle_event(event):
                    running = False
                    break
            if running:
                game.update(elapsed, pygame.key.get_pressed())
                game.draw()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
