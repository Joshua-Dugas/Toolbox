from flask import Blueprint, render_template, request, jsonify
import json
from pathlib import Path
from tools.rti.utils.ascii_loader import load_ascii

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



