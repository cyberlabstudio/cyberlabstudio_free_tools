# core/notes_handler.py

def create_note(path: str, template: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(template)

def load_note(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_note(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
