# core/lab_manager.py

import os
import json
from datetime import datetime
import shutil

TEMPLATE_DIR = "labs/templates"

def create_lab_folder(
    lab_id: int,
    name: str,
    platform: str,
    os_type: str,
    template_type: str = "default") -> str:
    """
    Initialise un dossier de lab avec les fichiers types.
    :param lab_id: Numéro du lab (ex: 002)
    :param name: Nom du lab (ex: Blue)
    :param platform: Plateforme (TryHackMe ou HackTheBox)
    :param os_type: OS détecté (Windows, Linux, etc.)
    :param template_type: Type de template (default, linux, windows, web)
    :return: Chemin du dossier créé
    """
    # Normalisation
    platform = platform.lower()
    template_type = template_type.lower()
    folder_name = f"lab_{lab_id:03d}_{name.lower().replace(' ', '_')}_{platform}"
    folder_path = os.path.join("labs", folder_name)

    # Création du dossier
    os.makedirs(folder_path, exist_ok=True)

    # Création du fichier metadata.json
    metadata = {
        "lab_name": name,
        "platform": platform.capitalize(),
        "ip": "",
        "os": os_type,
        "status": "in_progress",
        "created": datetime.now().isoformat(timespec="seconds")
    }
    with open(os.path.join(folder_path, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    # Copie du template de notes
    template_file = os.path.join(TEMPLATE_DIR, f"{template_type}.md")
    notes_path = os.path.join(folder_path, "notes.md")
    if os.path.exists(template_file):
        shutil.copy(template_file, notes_path)
    else:
        with open(notes_path, "w", encoding="utf-8") as f:
            f.write(f"# Notes – {name}\n\n## À compléter...\n")

    # Création des fichiers vides
    open(os.path.join(folder_path, "report.md"), "w", encoding="utf-8").close()
    open(os.path.join(folder_path, "scan.xml"), "w", encoding="utf-8").close()

    print(f"✅ Lab créé : {folder_path}")
    return folder_path
