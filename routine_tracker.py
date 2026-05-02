import json
import os
from datetime import datetime

# Datei-Konstante
ROUTINES_FILE = "routines.json"

# Wochentage als Konstanten
WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# ==================== DATENMODELL ====================

def load_routines():
    """Lädt Routinen aus routines.json"""
    if os.path.exists(ROUTINES_FILE):
        try:
            with open(ROUTINES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Fehler beim Laden von routines.json")
            return []
    else:
        return []


def save_routines(routines):
    """Speichert Routinen in routines.json"""
    with open(ROUTINES_FILE, "w", encoding="utf-8") as f:
        json.dump(routines, f, ensure_ascii=False, indent=2)


def generate_routine_id(routines):
    """Generiert eindeutige ID für neue Routine"""
    if not routines:
        return "001"
    max_id = max(int(r.get("id", "0")) for r in routines if r.get("id", "0").isdigit())
    return str(max_id + 1).zfill(3)


# ==================== MENÜ ====================

def display_menu():
    """Zeigt Hauptmenü an"""
    print("\n" + "=" * 40)
    print("📅 ROUTINE TRACKER - Kalender App")
    print("=" * 40)
    print("1. 📅 Kalender anzeigen")
    print("2. ➕ Routine hinzufügen")
    print("3. 📋 Alle Routinen anzeigen")
    print("4. ✏️  Routine bearbeiten")
    print("5. ❌ Routine löschen")
    print("6. 🚪 Beenden")
    print("=" * 40)


def get_user_choice():
    """Holt Benutzer-Input mit Validierung"""
    try:
        choice = input("Auswahl (1-6): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("❌ Ungültige Eingabe. Bitte 1-6 eingeben.")
            return None
    except KeyboardInterrupt:
        print("\n👋 Programm beendet.")
        return "6"


# ==================== HAUPTPROGRAMM ====================

def main():
    """Hauptprogramm-Schleife"""
    routines = load_routines()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            continue
        
        if choice == "1":
            print("(📅 Kalender-View - wird noch implementiert)")
        elif choice == "2":
            print("(➕ Routine hinzufügen - wird noch implementiert)")
        elif choice == "3":
            print("(📋 Alle Routinen anzeigen - wird noch implementiert)")
        elif choice == "4":
            print("(✏️  Routine bearbeiten - wird noch implementiert)")
        elif choice == "5":
            print("(❌ Routine löschen - wird noch implementiert)")
        elif choice == "6":
            print("\n👋 Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
