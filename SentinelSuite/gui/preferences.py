# gui/preferences.py

import customtkinter as ctk
from core.config_manager import load_config, save_config

class PreferencesFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.config: dict = load_config()

        ctk.CTkLabel(
            self,
            text="⚙️ Preferences",
            font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0, 20))

        # Thème
        ctk.CTkLabel(self, text="Theme").pack(anchor="w")
        self.theme_option = ctk.CTkOptionMenu(self, values=["light", "dark"])
        self.theme_option.set(self.config.get("theme", "light"))
        self.theme_option.pack(pady=5, fill="x")

        # Chemins
        self.notes_entry = ctk.CTkEntry(self, placeholder_text="Notes path")
        self.notes_entry.insert(0, self.config["paths"]["notes"])
        self.notes_entry.pack(pady=5, fill="x")

        self.scan_entry = ctk.CTkEntry(self, placeholder_text="Scan path")
        self.scan_entry.insert(0, self.config["paths"]["scan_history"])
        self.scan_entry.pack(pady=5, fill="x")

        self.labs_entry = ctk.CTkEntry(self, placeholder_text="Labs path")
        self.labs_entry.insert(0, self.config["paths"]["labs"])
        self.labs_entry.pack(pady=5, fill="x")

        # Bouton de sauvegarde
        ctk.CTkButton(self, text="save", command=self.save_preferences).pack(pady=10)

        # Zone de confirmation
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=(10, 0))

    def save_preferences(self) -> None:
        self.config["theme"] = self.theme_option.get()
        self.config["paths"]["notes"] = self.notes_entry.get().strip()
        self.config["paths"]["scan_history"] = self.scan_entry.get().strip()
        self.config["paths"]["labs"] = self.labs_entry.get().strip()

        save_config(self.config)
        self.status_label.configure(text="✅ Preferences saved.")
