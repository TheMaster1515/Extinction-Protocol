import builtins
import os
import queue
import sys
import threading
import traceback
from io import BytesIO

os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import cv2
import pygame


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_DIR, "code"))
os.chdir(PROJECT_DIR)

WINDOW_SIZE = (1600, 900)
BACKGROUND = (16, 20, 29)
TEXT_COLOR = (224, 231, 240)
ACCENT = (112, 220, 180)
MUTED = (140, 153, 170)


class GameWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Text-Based Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 17)
        self.title_font = pygame.font.SysFont("monospace", 21, bold=True)

        self.messages = queue.Queue()
        self.input_ready = threading.Event()
        self.input_response = None
        self.input_pending = False
        self.input_buffer = ""
        self.input_prompt = ""
        self.lines = []
        self.current_line = ""
        self.scroll_offset = 0
        self.image_surface = None
        self.opencv_image_window_open = False
        self.closed = False
        self.finished = False

    def write(self, text):
        self.messages.put(("output", text))
        return len(text)

    def flush(self):
        pass

    def read_input(self, prompt=""):
        self.input_ready.clear()
        self.input_response = queue.Queue(maxsize=1)
        self.messages.put(("input", str(prompt)))
        self.input_ready.wait()
        if self.closed:
            raise EOFError
        return self.input_response.get()

    def _append_output(self, text):
        parts = (self.current_line + text).split("\n")
        for line in parts[:-1]:
            self.lines.extend(self._wrap_line(line))
        self.current_line = parts[-1]
        self.scroll_offset = 0

    def _wrap_line(self, line):
        line = line.expandtabs(4)
        char_width = max(1, self.font.size("M")[0])
        available = max(1, self._output_rect().width - 32)
        max_chars = max(1, available // char_width)
        if not line:
            return [""]
        return [line[index:index + max_chars] for index in range(0, len(line), max_chars)]

    def _output_rect(self):
        width, height = self.screen.get_size()
        return pygame.Rect(32, 68, width - 64, height - 146)

    def _handle_messages(self):
        while True:
            try:
                kind, value = self.messages.get_nowait()
            except queue.Empty:
                return

            if kind == "output":
                self._append_output(value)
            elif kind == "input":
                self.input_prompt = value
                self.input_buffer = ""
                self.input_pending = True
            elif kind == "image":
                self.image_surface = pygame.image.load(BytesIO(value)).convert()
            elif kind == "error":
                self._append_output(value)
            elif kind == "finished":
                self.finished = True

    def _submit_input(self):
        if not self.input_pending or self.input_response is None:
            return
        self._append_output(self.input_prompt + self.input_buffer + "\n")
        self.input_response.put(self.input_buffer)
        self.input_pending = False
        self.input_ready.set()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closed = True
                self.input_ready.set()
            elif event.type == pygame.MOUSEWHEEL:
                self.scroll_offset = max(0, self.scroll_offset + event.y * 3)
            elif event.type == pygame.KEYDOWN:
                if self.input_pending:
                    if event.key == pygame.K_RETURN:
                        self._submit_input()
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_buffer = self.input_buffer[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        self._submit_input()
                    elif event.unicode and event.unicode.isprintable():
                        self.input_buffer += event.unicode
                elif event.key == pygame.K_PAGEUP:
                    self.scroll_offset += 20
                elif event.key == pygame.K_PAGEDOWN:
                    self.scroll_offset = max(0, self.scroll_offset - 20)

    def _draw(self):
        width, height = self.screen.get_size()
        if self.image_surface is None:
            self.screen.fill(BACKGROUND)
        else:
            image_width, image_height = self.image_surface.get_size()
            scale = max(width / image_width, height / image_height)
            scaled_size = (max(1, int(image_width * scale)), max(1, int(image_height * scale)))
            image = pygame.transform.smoothscale(self.image_surface, scaled_size)
            crop = pygame.Rect(
                (image.get_width() - width) // 2,
                (image.get_height() - height) // 2,
                width,
                height,
            )
            self.screen.blit(image, (0, 0), crop)

        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((8, 13, 22, 165))
        self.screen.blit(overlay, (0, 0))

        output_rect = self._output_rect()
        title = self.title_font.render("TEXT BASED ADVENTURE", True, ACCENT)
        self.screen.blit(title, (32, 27))

        visible_lines = self.lines + self._wrap_line(self.current_line)
        line_height = self.font.get_linesize()
        visible_count = max(1, output_rect.height // line_height)
        end = max(0, len(visible_lines) - self.scroll_offset)
        start = max(0, end - visible_count)
        self.screen.set_clip(output_rect)
        for index, line in enumerate(visible_lines[start:end]):
            rendered = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(rendered, (output_rect.x + 14, output_rect.y + index * line_height))
        self.screen.set_clip(None)

        input_rect = pygame.Rect(24, height - 66, width - 48, 38)
        input_background = pygame.Surface(input_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(input_background, (8, 13, 22, 210), input_background.get_rect(), border_radius=5)
        self.screen.blit(input_background, input_rect)
        if self.input_pending:
            prompt = self.input_prompt.strip() or "Enter your response"
            input_text = f"{prompt}  {self.input_buffer}"
            input_color = ACCENT
        else:
            input_text = "Game finished" if self.finished else "Waiting for the game..."
            input_color = MUTED
        rendered_input = self.font.render(input_text, True, input_color)
        self.screen.blit(rendered_input, (input_rect.x + 10, input_rect.y + 9))

        pygame.display.flip()

    def _start_game(self):
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        original_input = builtins.input

        def run():
            sys.stdout = self
            sys.stderr = self
            builtins.input = self.read_input
            try:
                import chapterZ

                chapterZ.chapterz()
            except EOFError:
                if not self.closed:
                    self.messages.put(("error", traceback.format_exc()))
            except Exception:
                self.messages.put(("error", traceback.format_exc()))
            finally:
                sys.stdout = original_stdout
                sys.stderr = original_stderr
                builtins.input = original_input
                self.messages.put(("finished", None))

        threading.Thread(target=run, daemon=True).start()

    def _use_game_image_window(self):
        def show_image(_window_name, image):
            success, encoded = cv2.imencode(".png", image)
            if not success:
                raise RuntimeError("Could not encode a chapter image for display.")
            self.messages.put(("image", encoded.tobytes()))
            self.opencv_image_window_open = True

        def wait_key(delay=0):
            return 0 if self.opencv_image_window_open else -1

        def destroy_windows():
            self.opencv_image_window_open = False

        cv2.namedWindow = lambda *_args, **_kwargs: None
        cv2.imshow = show_image
        cv2.setWindowProperty = lambda *_args, **_kwargs: None
        cv2.waitKey = wait_key
        cv2.getWindowProperty = lambda *_args, **_kwargs: 0 if self.closed else 1
        cv2.destroyAllWindows = destroy_windows

    def run(self):
        self._use_game_image_window()
        self._start_game()
        while not self.closed:
            self._handle_events()
            self._handle_messages()
            self._draw()
            self.clock.tick(60)
        pygame.quit()


def main():
    GameWindow().run()


if __name__ == "__main__":
    main()
