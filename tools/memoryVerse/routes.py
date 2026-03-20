from flask import Blueprint, render_template, request, jsonify
import json
from pathlib import Path

memoryVerse = Blueprint(
    "memoryVerse",
    __name__,
    template_folder="."
)
#TODO: I should see if I can just make a save helper class to save repetition

#----------save functions --------- 
V_DATA_FILE = Path("data/memoryVerses.json")

def load_verses():
    if not V_DATA_FILE.exists():
        V_DATA_FILE.parent.mkdir(exist_ok=True)
        with open(V_DATA_FILE, "w") as f:
            json.dump({}, f)
        return {}

    try:
        with open(V_DATA_FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_verse(data):
    with open(V_DATA_FILE, "w") as e:
        json.dump(data, e, indent=2)

#----------Routes----------
@memoryVerse.route("/")
def ui():
    verse_dict = load_verses()
    return render_template("memoryVerse.html", verse_dict=verse_dict)

@memoryVerse.route("verse/getData", methods=["GET"])
def getData():
    verse_dict = load_verses()
    return jsonify(verse_dict)

@memoryVerse.route("/verse/add", methods=["POST"])
def addVerse():
    verse_dict = load_verses()
    data = request.json
    verseHeader = data["header"]
    verseBody = data["body"]
    
    verse_dict[verseHeader] = {
        "body": verseBody
    }

    save_verse(verse_dict)
    print(verse_dict)

    return jsonify({
        "header": verseHeader,
        "body": verseBody 
    })

@memoryVerse.route("verse/delete", methods=["DELETE"])
def deleteVerse():
    #placeholder
    verse = "verse"
    return verse 

