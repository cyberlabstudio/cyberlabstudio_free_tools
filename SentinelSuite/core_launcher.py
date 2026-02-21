# core_launcher.py

import customtkinter as ctk
from core.config_manager import load_config
from gui.preferences import PreferencesFrame
from gui.scan_manager import ScanManagerFrame
from gui.notes_manager import NotesManagerFrame
from gui.history_viewer import HistoryViewerFrame

class SentinelSuiteApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        # Fenêtre principale
        self.title("SentinelSuite Lite")
        self.geometry("900x600")
        self.minsize(800, 500)

        # Configuration du thème
        self.config = load_config()
        ctk.set_appearance_mode(self.config.get("theme", "light"))
        ctk.set_default_color_theme(self.config.get("default_color_theme", "blue"))

        # Menu latéral
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        # Logo de l'app
        self.logo = ctk.CTkLabel(self.sidebar, text="🛡️ SentinelSuite", font=("Arial", 18, "bold"))
        self.logo.pack(pady=(20, 10))

        # Zone principale
        self.main_area = ctk.CTkFrame(self)
        self.main_area.pack(side="right", expand=True, fill="both")

        # Boutons de navigation
        self.buttons = {}
        self._create_sidebar_buttons()

        # Chargement initial du module ScanManager
        self.load_module(ScanManagerFrame, "scan")

    def _create_sidebar_buttons(self) -> None:
        modules = self.config.get("modules", {})
        sidebar_config = self.config.get("sidebar", {})

        # Dictionnaire des modules disponibles
        module_map = {
            "scan_manager": ScanManagerFrame,
            "notes_manager": NotesManagerFrame,
            "history_viewer": HistoryViewerFrame,
            "preferences": PreferencesFrame
        }

        for key, frame_class in module_map.items():
            if not modules.get(key, True):
                continue

            # Lecture des styles personnalisés
            style = sidebar_config.get(key, {})
            label = f"{style.get('icon', '')} {style.get('label', key.capitalize())}"
            color = style.get("color")

            btn = ctk.CTkButton(
                self.sidebar,
                text=label,
                fg_color=color,
                text_color="white",
                hover_color="#5a9bd5",
                corner_radius=6,
                command=lambda cls=frame_class, k=key: self.load_module(cls, k)
            )
            btn.pack(pady=10, padx=20, fill="x")

            self.buttons[key] = btn

    def load_module(self, frame_class, key: str) -> None:
        self._clear_main_area()
        self._highlight_button(key)
        frame = frame_class(self.main_area)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

    def _highlight_button(self, active_key: str) -> None:
        for key, btn in self.buttons.items():
            if key == active_key:
                btn.configure(border_width=2, border_color="white")
            else:
                btn.configure(border_width=0)

    def _clear_main_area(self) -> None:
        for widget in self.main_area.winfo_children():
            widget.destroy()

# Lancement de l'interface
if __name__ == "__main__":
    app = SentinelSuiteApp()
    app.mainloop()
