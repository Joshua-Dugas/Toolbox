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

SPLASH_ART = Path("tools/rti/assets/introSplash.txt") 

@rti.route("/")
def ui():
   return render_template("rti.html") 

#TODO: This is temporary, eventually will have game engine pass in the scene name and art 
@rti.route("/loadScreen", methods=["GET"])
def drawScene():
    scene = {}
    art = load_ascii(SPLASH_ART)
    scene["name"] = "landing splash" 
    scene["art"] = art
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
