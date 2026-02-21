# gui/scan_manager.py

import os
import webbrowser
import re
from datetime import datetime
import customtkinter as ctk
from core.nmap_launcher import run_nmap_scan, is_nmap_available
from core.config_manager import load_config

# ✅ Fonction utilitaire pour nettoyer les noms de fichiers
def sanitize_filename(name: str) -> str:
    # Remplace les caractères interdits par "_"
    return re.sub(r'[<>:"/\\|?*]', '_', name)

class ScanManagerFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.profile_option: ctk.CTkOptionMenu

        # Titre
        ctk.CTkLabel(
            self,
            text="🔍 Scan Manager",
            font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0, 20))

        # Champ IP cible
        self.target_entry = ctk.CTkEntry(self, placeholder_text="IP address or domain")
        self.target_entry.pack(pady=10, fill="x")

        # ✅ Chargement de la configuration
        self.scan_config = load_config()

        # ✅ Récupération des profils conviviaux
        profile_config = self.scan_config.get("scan_profiles", {})
        profile_labels = [f"{info['icon']} {info['label']}" for info in profile_config.values()]
        self.profile_map = {
            f"{info['icon']} {info['label']}": key for key,
            info in profile_config.items()}

        # Choix du profil de scan
        self.profile_option = ctk.CTkOptionMenu(self, values=profile_labels)
        self.profile_option.set(profile_labels[0])
        self.profile_option.pack(pady=10)

        # Bouton de scan
        ctk.CTkButton(
            self,
            text="Start the scan",
            command=self.launch_scan
        ).pack(pady=10)

        # Zone de sortie
        self.output_box = ctk.CTkTextbox(self, height=300)
        self.output_box.pack(pady=10, fill="both", expand=True)

        # Vérification Nmap
        self.check_nmap()

    def check_nmap(self) -> None:
        if not is_nmap_available():
            self.output_box.insert("end", "⚠️ Nmap is not installed or cannot be found.\n")
            ctk.CTkButton(
                self,
                text="Install Nmap",
                command=self.open_nmap_site,
                fg_color="red").pack(pady=5)

    def launch_scan(self) -> None:
        target = self.target_entry.get().strip()

        selected_label = self.profile_option.get()
        profile_key = self.profile_map.get(selected_label)

        # ✅ Vérifie que le menu existe
        if not profile_key:
            self.output_box.insert("end", "⚠️ No profiles selected.\n")
            return

        self.output_box.delete("1.0", "end")

        if not is_nmap_available():
            self.output_box.insert("end", "⚠️ Nmap is required to start a scan.\n")
            return

        if target:
            self.output_box.insert(
                "end",
                f"🔎 Scan in progress on {target} with the profile '{profile_key}'...\n\n")
            result = run_nmap_scan(target, profile_key)
            self.output_box.insert("end", result)
            self.save_scan_history(target, profile_key, result)
        else:
            self.output_box.insert("end", "⚠️ Please enter a valid target.\n")

    def save_scan_history(self, target: str, profile: str, result: str) -> None:
        os.makedirs("scan_history", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_target = sanitize_filename(target)
        file_path = os.path.join("scan_history", f"{safe_target}_{profile}_{timestamp}.log")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Target: {target}\nProfile: {profile}\nTimestamp: {timestamp}\n\n{result}")

        self.output_box.insert("end", f"\n🗂️ Result saved in {file_path}\n")

    def open_nmap_site(self) -> None:
        webbrowser.open("https://nmap.org/download.html")
