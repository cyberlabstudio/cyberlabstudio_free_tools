# core/config_manager.py

import os
import json

CONFIG_FILE = "config.json"

# Configuration par défaut
DEFAULT_CONFIG = {
    "theme": "light",
    "default_color_theme": "blue",
    "language": "fr",
    "ui_mode": "compact",
    "paths": {
        "notes": "C:/SentinelSuite/notes",
        "scan_history": "C:/SentinelSuite/scans",
        "labs": "C:/SentinelSuite/labs"
    },
    "modules": {
        "scan_manager": True,
        "notes_manager": True,
        "history_viewer": True
    }
}

def load_config() -> dict:
    """Charge la configuration depuis config.json ou crée le fichier avec les valeurs par défaut."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️ Erreur de lecture du fichier config.json. Rechargement des valeurs par défaut.")
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def save_config(config: dict) -> None:
    """Sauvegarde la configuration dans config.json."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
