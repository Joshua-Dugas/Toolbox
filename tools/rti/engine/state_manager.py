from pathlib import Path
import json

SAVE_DATA_LOCATION = Path("data/rti_saves/")
SAVE_DATA_LOCATION.mkdir(exist_ok=True)  # ensure folder exists
ART_LOCATION = Path("tools/rti/assets/") 


#Temporary way to know if the game has init'd yet 
game_initialized = False 

class StateManager:
    def __init__(self):
        self._screen_name = None
        self._actions = None

    def initialize(self, screen_name, actions):
        self._screen_name = screen_name
        self._actions = actions

    def update(self, screen_name=None, actions=None):
        if screen_name is not None:
            self._screen_name = screen_name
        if actions is not None:
            self._actions = actions

    def get_screen_name(self):
        return self._screen_name

    def get_actions(self):
        return self._actions


state_manager = StateManager()

#TODO: hook up init and get game running
def initialize():
    state_manager.initialize("mainMenu", ["1. New game", "2. load game"])
    game_initialized = True

def is_game_initialized():
    return game_initialized

def get_available_actions():
    return state_manager.get_actions()

def get_current_screen():
    return state_manager.get_screen_name()



#Game Save Logic
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

