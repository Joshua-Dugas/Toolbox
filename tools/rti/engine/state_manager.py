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
        self._text = None 

    def initialize(self, screen_name, actions, text):
        self._screen_name = screen_name
        self._actions = actions
        self._text = text 

    def update(self, screen_name=None, actions=None, text=None):
        if screen_name is not None:
            self._screen_name = screen_name
        if actions is not None:
            self._actions = actions
        if text is not None:
            self._text = text 

    def get_screen_name(self):
        return self._screen_name

    def get_actions(self):
        return self._actions

    def get_text(self):
        return self._text


state_manager = StateManager()

#We always want the game to init on the main menu so the hard coding is fine 
def initialize():
    state_manager.initialize("mainMenu", ["1. New game", "2. load game"], "Welcome to Roads to Izalyth. Please select an option")
    game_initialized = True

def is_game_initialized():
    return game_initialized

def get_available_actions():
    return state_manager.get_actions()

def get_current_screen():
    return state_manager.get_screen_name()

def get_current_text():
    return state_manager.get_text()

#----------Game Save Logic----------
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

