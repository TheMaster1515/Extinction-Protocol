import os
from pathlib import Path
import tempfile


FIELDS = ("Name", "Age", "Colony", "Person", "Ship", "Job")


def parse_character(content):
    data = {}
    for line in content.splitlines():
        if not line:
            continue
        key, separator, value = line.partition(": ")
        if not separator or key in data:
            raise ValueError("Invalid character data")
        data[key] = value
    return data


def read_character(path):
    path = Path(path)
    try:
        data = parse_character(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = {}
    if not data.get("Job", "").strip():
        data.pop("Job", None)
        try:
            legacy = (path.parent / "job.txt").read_text(encoding="utf-8")
        except FileNotFoundError:
            legacy = ""
        if legacy.strip():
            job = parse_character(legacy)
            if set(job) != {"Job"} or not job["Job"]:
                raise ValueError("Invalid legacy job data")
            data["Job"] = job["Job"]
    return data


def format_character(data):
    values = {**{field: "Unknown" for field in FIELDS}, **data}
    for field in ("Person", "Ship", "Job"):
        if not values[field].strip():
            values[field] = "Unknown"
    ordered = list(FIELDS) + [field for field in values if field not in FIELDS]
    return "".join(f"{field}: {values[field]}\n" for field in ordered)


def prepare_character(data):
    data = {"Name": "Unknown", "Age": "0", "Colony": "Unknown", **data}
    if not data["Name"].strip() or not data["Colony"].strip() or not data["Age"].isdigit():
        raise ValueError("Invalid character identity")
    return data


def update_character(path, **updates):
    path = Path(path)
    data = read_character(path)
    data.update(updates)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=".character.", suffix=".tmp", delete=False,
        ) as output:
            temporary_path = Path(output.name)
            output.write(format_character(data))
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def save_character_work(person, ship=None):
    updates = {"Person": person}
    if ship is not None:
        updates["Ship"] = ship
    update_character("files/character.txt", **updates)
