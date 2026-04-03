from flask import Blueprint, render_template, request, jsonify
import json
from pathlib import Path
from tools.rti.utils.ascii_loader import load_ascii
from tools.rti.engine import state_manager

rti = Blueprint(
    "rti",
    __name__,
    template_folder="."
)


@rti.route("/")
def ui():
   return render_template("rti.html") 

"""
screen_name = the visual render of ascii art 
Actions = menu options that print to the screen
Scene = The complete render of screen and actions 
"""
@rti.route("/loadScreen", methods=["GET"])
def drawScene():
    if(state_manager.is_game_initialized() == False):
        state_manager.initialize()

    screen_name = state_manager.get_current_screen()
    ascii_art = load_ascii(screen_name)
    actions = state_manager.get_available_actions()
    
    scene = {
        "screen": ascii_art,
        "actions": actions
    }

    print(f"{scene}")
    return jsonify(scene) 

@rti.route("/createGame", methods=["POST"])
def create_game():
    """
    Expects JSON:
    {
        "save_name": "save_1",
        "game_data": {...}
    }
    """
    data = request.get_json()
    save_name = data.get("save_name", "save_1")
    game_data = data.get("game_data", {})

    # delegate to state manager
    path = state_manager.create_game(save_name, game_data)

    return jsonify({"status": "success", "path": path}) 

@rti.route("/saveGame", methods=["POST"])
def save_game_route():
    """
    Expects JSON:
    {
        "save_name": "save_1",
        "game_data": {...}
    }
    """
    data = request.get_json()
    save_name = data.get("save_name")
    game_data = data.get("game_data", {})

    if not save_name:
        return jsonify({"status": "error", "message": "No save name provided"}), 400

    path = state_manager.save_game(save_name, game_data)
    return jsonify({"status": "success", "path": path})

@rti.route("/loadGame/<save_name>", methods=["GET"])
def load_game_route(save_name):
    game_data = state_manager.load_game(save_name)
    if game_data is None:
        return jsonify({"status": "error", "message": "Save not found"}), 404
    return jsonify({"status": "success", "game_data": game_data})
