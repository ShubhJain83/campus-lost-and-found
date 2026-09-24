import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "records.json"


def ensure_data_file():
    DATA_FILE.parent.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_records():
    ensure_data_file()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        return []


def save_records(records):
    ensure_data_file()

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def add_record(record):
    records = load_records()
    records.append(record)
    save_records(records)


def update_record_status(item_id, status):
    records = load_records()

    for item in records:
        if item["id"] == item_id:
            item["status"] = status
            save_records(records)
            return True

    return False