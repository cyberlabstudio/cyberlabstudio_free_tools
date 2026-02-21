# core/nmap_launcher.py

import subprocess
import shutil
import json
import os

def is_nmap_available() -> bool:
    """Vérifie si Nmap est disponible dans le PATH."""
    return shutil.which("nmap") is not None

def load_profiles() -> dict:
    """Charge les profils de scan depuis config.json."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("scan_profiles", {})
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def run_nmap_scan(target: str, profile_key: str = "basic") -> str:
    """
    Lance un scan Nmap sur la cible donnée avec le profil choisi.
    profile_key correspond à la clé du profil dans config.json (ex: "basic", "full", "stealth", "udp").
    """
    if not is_nmap_available():
        return "⚠️ Nmap n'est pas installé ou n'est pas dans le PATH."

    profiles = load_profiles()

    if profile_key not in profiles:
        return f"⚠️ Profil '{profile_key}' introuvable dans config.json."

    options = profiles[profile_key].get("options", [])
    args = ["nmap"] + options + [target]

    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=60, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"⚠️ Erreur pendant le scan : {str(e)}"
    except subprocess.TimeoutExpired as e:
        return f"⚠️ Le scan a dépassé la limite de temps : {str(e)}"
    except FileNotFoundError as e:
        return f"⚠️ Fichier ou répertoire introuvable : {str(e)}"
    except PermissionError as e:
        return f"⚠️ Permission refusée : {str(e)}"
    except RuntimeError as e:
        return f"⚠️ Erreur inattendue pendant le scan : {str(e)}"
