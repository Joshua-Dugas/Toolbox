from pathlib import Path
import json

SAVE_DATA_LOCATION = Path("data/rti_saves/")
SAVE_DATA_LOCATION.mkdir(exist_ok=True)  # ensure folder exists

def create_game(save_name: str, save_data: dict):
    save_path = SAVE_DATA_LOCATION / f"{save_name}.json"
    with open(save_path, "w") as f:
        json.dump(save_data, f, indent=2)
    return str(save_path)

def save_game(save_name: str, save_data: dict):
    save_path = SAVE_DATA_LOCATION / f"{save_name}.json"
    with open(save_path, "w") as f:
        json.dump(save_data, f, indent=2)
    return str(save_path)

def load_game(save_name: str):
    save_path = SAVE_DATA_LOCATION / f"{save_name}.json"
    if not save_path.exists():
        return None
    with open(save_path, "r") as f:
        return json.load(f)

