from pathlib import Path

ART_LOCATION = Path("tools/rti/assets/")

def load_ascii(screen_name):
    """
    Loads ascii art file based on the screen name stored in state_manager.
    
    Example:
        screen_name = "mainMenu"
        -> tools/rti/assets/mainMenu.txt
    """

    filename = f"{screen_name}.txt"
    filepath = ART_LOCATION / filename

    if not filepath.exists():
        return f"[Missing ASCII file: {filename}]"

    with open(filepath, "r", encoding="utf-8") as f:
        ascii_art = f.read()

    return ascii_art
