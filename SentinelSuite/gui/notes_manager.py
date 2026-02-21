# gui/notes_manager.py

import os
from datetime import datetime
import customtkinter as ctk
from core.lab_manager import create_lab_folder
from core.notes_handler import load_note, save_note

class NotesManagerFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        # Titre
        ctk.CTkLabel(
            self,
            text="📝 Notes Manager",
            font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0, 20))

        # Champs d'entrée
        self.lab_name_entry = ctk.CTkEntry(
            self,
            placeholder_text="Lab name (ex: Blue)")
        self.lab_name_entry.pack(pady=5, fill="x")

        self.platform_entry = ctk.CTkEntry(
            self,
            placeholder_text="Plateform (TryHackMe, HackTheBox...)")
        self.platform_entry.pack(pady=5, fill="x")

        self.os_entry = ctk.CTkEntry(
            self,
            placeholder_text="System (Windows, Linux...)")
        self.os_entry.pack(pady=5, fill="x")

        self.lab_id_entry = ctk.CTkEntry(
            self,
            placeholder_text="Lab ID (ex: 002)")
        self.lab_id_entry.pack(pady=5, fill="x")

        # Zone de texte pour les notes
        self.notes_box = ctk.CTkTextbox(self, height=300)
        self.notes_box.pack(padx=20, pady=10, fill="both", expand=True)

        # Bouton de sauvegarde
        ctk.CTkButton(self, text="Save notes", command=self.save_notes).pack(pady=10)

        # sauvegarde markdown
        self.textbox = ctk.CTkTextbox(self)
        self.textbox.pack(fill="both", expand=True)

    def save_notes(self) -> None:
        name = self.lab_name_entry.get().strip()
        platform = self.platform_entry.get().strip()
        os_type = self.os_entry.get().strip()
        lab_id_str = self.lab_id_entry.get().strip()
        notes = self.notes_box.get("1.0", "end").strip()

        self.notes_box.insert("end", "\n")

        # Validation
        if not (name and platform and os_type and lab_id_str and notes):
            self.notes_box.insert("end", "⚠️ Please fill in all lines.\n")
            return

        try:
            lab_id = int(lab_id_str)
        except ValueError:
            self.notes_box.insert("end", "⚠️ The lab ID must be a number.\n")
            return

        # Création du dossier via lab_manager
        folder_path = create_lab_folder(
            lab_id=lab_id,
            name=name,
            platform=platform,
            os_type=os_type,
            template_type="default"
        )

        # Sauvegarde des notes personnalisées
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(folder_path, f"notes_custom_{timestamp}.txt")

        with open(notes_file, "w", encoding="utf-8") as f:
            f.write(notes)

        self.notes_box.insert("end", f"✅ Notes saved in {notes_file}\n")

    def load_lab_note(self, lab_path: str) -> None:
        note_path = os.path.join(lab_path, "notes.md")
        content = load_note(note_path)
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", content)

    def save_lab_note(self, lab_path: str) -> None:
        note_path = os.path.join(lab_path, "notes.md")
        content = self.textbox.get("1.0", "end").strip()
        save_note(note_path, content)
