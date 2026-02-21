# gui/history_viewer.py

import os
import shutil
import customtkinter as ctk

class HistoryViewerFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="📁 Logs",
            font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0, 20))

        # Choix du type
        self.type_option = ctk.CTkOptionMenu(
            self,
            values=["Scans", "Notes"],
            command=self.load_file_list)
        self.type_option.set("Scans")
        self.type_option.pack(pady=10)

        # Liste des fichiers
        self.file_list = ctk.CTkOptionMenu(self, values=["No file"])
        self.file_list.pack(pady=10)

        # Boutons d'action
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="View logs",
            command=self.display_file_content).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="🗑️ Delete",
            fg_color="red",
            command=self.delete_file).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="📤 Export",
            command=self.export_file).pack(side="left", padx=5)

        # Zone de lecture
        self.viewer_box = ctk.CTkTextbox(self, height=300)
        self.viewer_box.pack(padx=20, pady=10, fill="both", expand=True)

        # Chargement initial
        self.load_file_list("Scans")

    def load_file_list(self, file_type: str) -> None:
        folder = "scan_history" if file_type == "Scans" else "notes"
        files = []

        if os.path.exists(folder):
            for root, _, filenames in os.walk(folder):
                for f in filenames:
                    if f.endswith(".log") or f.endswith(".txt"):
                        files.append(os.path.join(root, f))

        self.file_list.configure(values=files if files else ["No file"])
        self.file_list.set(files[0] if files else "No file")

    def display_file_content(self) -> None:
        path = self.file_list.get()
        self.viewer_box.delete("1.0", "end")

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.viewer_box.insert("end", content)
        else:
            self.viewer_box.insert("end", "⚠️ File not found.")

    def delete_file(self) -> None:
        path = self.file_list.get()
        self.viewer_box.delete("1.0", "end")

        if os.path.exists(path):
            os.remove(path)
            self.viewer_box.insert("end", f"🗑️ File deleted : {path}\n")
            self.load_file_list(self.type_option.get())
        else:
            self.viewer_box.insert("end", "⚠️ File not found.")

    def export_file(self) -> None:
        path = self.file_list.get()
        self.viewer_box.delete("1.0", "end")

        if os.path.exists(path):
            os.makedirs("exported", exist_ok=True)
            filename = os.path.basename(path)
            dest = os.path.join("exported", filename)
            shutil.copy2(path, dest)
            self.viewer_box.insert("end", f"📤 File exported to : {dest}\n")
        else:
            self.viewer_box.insert("end", "⚠️ File not found.")
