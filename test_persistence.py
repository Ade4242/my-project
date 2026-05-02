import json
import os

# Test, ob die routines.json Datei erstellt und geladen werden kann
ROUTINES_FILE = "routines.json"

test_routines = [
    {"name": "Debugging", "done": False},
    {"name": "Code Review", "done": True},
    {"name": "Dokumentation", "done": False}
]

# Speichern
with open(ROUTINES_FILE, "w", encoding="utf-8") as f:
    json.dump(test_routines, f, ensure_ascii=False, indent=2)
print("✅ Routinen gespeichert in routines.json")

# Laden
if os.path.exists(ROUTINES_FILE):
    with open(ROUTINES_FILE, "r", encoding="utf-8") as f:
        loaded_routines = json.load(f)
    print("✅ Routinen geladen:")
    for i, routine in enumerate(loaded_routines, 1):
        status = "✅" if routine["done"] else "⬜"
        print(f"  {i}. {status} {routine['name']}")
else:
    print("❌ Datei nicht gefunden")
