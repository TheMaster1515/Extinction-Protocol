"""Run one isolated story session and exchange events with the web server."""

import builtins
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback
import types


ROOT = Path(__file__).resolve().parent
protocol_out = sys.stdout
protocol_in = sys.stdin


def emit(kind, **values):
    protocol_out.write(json.dumps({"type": kind, **values}) + "\n")
    protocol_out.flush()


class Output:
    def write(self, text):
        if text:
            emit("output", text=text)
        return len(text)

    def flush(self):
        pass


def read_input(prompt=""):
    emit("input", prompt=str(prompt))
    line = protocol_in.readline()
    if not line:
        raise EOFError("Player disconnected")
    return line.rstrip("\n")


def run_arcade(command, *args, **kwargs):
    if command != ["python3", "chapter8game/EasterEgg.py"]:
        raise RuntimeError(f"Unexpected game subprocess: {command!r}")
    emit("arcade")
    if not protocol_in.readline():
        raise EOFError("Player disconnected")
    return subprocess.CompletedProcess(command, 0)


def make_cv2():
    cv2 = types.ModuleType("cv2")
    cv2.WINDOW_NORMAL = cv2.WND_PROP_FULLSCREEN = 0
    cv2.WINDOW_FULLSCREEN = cv2.WND_PROP_TOPMOST = cv2.WND_PROP_VISIBLE = 0
    cv2.imread = lambda path: path if (ROOT / path).is_file() else None
    cv2.namedWindow = lambda *args: None
    cv2.imshow = lambda name, image: emit("image", path=image)
    cv2.setWindowProperty = lambda *args: None
    cv2.waitKey = lambda *args: 0
    cv2.getWindowProperty = lambda *args: 1
    cv2.destroyAllWindows = lambda: None
    return cv2


def main():
    os.makedirs("files", exist_ok=True)
    sys.path.insert(0, str(ROOT / "code"))
    sys.modules["cv2"] = make_cv2()
    builtins.input = read_input
    subprocess.run = run_arcade
    sys.stdout = Output()
    try:
        import chapterZ
        import chapter2
        import chapter8
        import character_data

        class WebCharacterManager(chapterZ.CharacterManager):
            def save_character_data(self, name, age, colony, filepath):
                super().save_character_data(name, age, colony, filepath)
                emit("character_update", changes={"Name": name, "Age": str(age), "Colony": colony})

        save_job = chapter2.save_job

        def save_web_job(job):
            save_job(job)
            emit("character_update", changes={"Job": job})

        save_character_work = character_data.save_character_work

        def save_web_character_work(person, ship=None):
            save_character_work(person, ship)
            changes = {"Person": person}
            if ship is not None:
                changes["Ship"] = ship
            emit("character_update", changes=changes)

        unlock_chapter8 = chapter8.unlock_chapter8

        def unlock_web_chapter8():
            unlock_chapter8()
            emit("chapter8_unlocked")

        chapterZ.CharacterManager = WebCharacterManager
        chapter2.save_job = save_web_job
        character_data.save_character_work = save_web_character_work
        chapter8.unlock_chapter8 = unlock_web_chapter8
        chapterZ.chapterz()
    except EOFError:
        pass
    except Exception:
        traceback.print_exc(file=sys.stderr)
        emit("error", message="The game stopped unexpectedly. Please start a new game.")
    finally:
        emit("finished")


if __name__ == "__main__":
    main()
