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


# ==================== VALIDIERUNGSFUNKTIONEN ====================

def validate_time(time_str):
    """Validiert Uhrzeit im Format HH:MM"""
    try:
        parts = time_str.split(":")
        if len(parts) != 2:
            return False
        hour = int(parts[0])
        minute = int(parts[1])
        return 0 <= hour <= 23 and 0 <= minute <= 59
    except:
        return False


def validate_weekday(weekday):
    """Validiert Wochentag"""
    return weekday.capitalize() in WEEKDAYS


def validate_duration(duration_str):
    """Validiert Dauer (positive Zahl)"""
    try:
        duration = int(duration_str)
        return duration > 0 and duration <= 480  # Max 8 Stunden
    except:
        return False


def validate_increment(increment_str):
    """Validiert Steigerung (0 oder positiv)"""
    try:
        increment = int(increment_str)
        return increment >= 0
    except:
        return False


# ==================== ROUTINE-FUNKTIONEN ====================

def add_routine(routines):
    """Fügt neue Routine interaktiv hinzu"""
    print("\n" + "=" * 40)
    print("➕ NEUE ROUTINE HINZUFÜGEN")
    print("=" * 40)
    
    # Name
    while True:
        name = input("Routine Name (min. 3 Zeichen): ").strip()
        if len(name) >= 3:
            break
        print("❌ Name muss mindestens 3 Zeichen lang sein.")
    
    # Wochentag
    print("\nVerfügbare Wochentage:")
    for i, day in enumerate(WEEKDAYS, 1):
        print(f"  {i}. {day}")
    while True:
        weekday_input = input("Wochentag (1-7 oder Name): ").strip()
        try:
            # Wenn Nummer eingegeben
            if weekday_input.isdigit():
                weekday_idx = int(weekday_input) - 1
                if 0 <= weekday_idx < len(WEEKDAYS):
                    weekday = WEEKDAYS[weekday_idx]
                    break
            # Wenn Name eingegeben
            elif validate_weekday(weekday_input):
                weekday = weekday_input.capitalize()
                break
        except:
            pass
        print("❌ Ungültige Eingabe. Bitte 1-7 oder Wochentag eingeben.")
    
    # Uhrzeit
    while True:
        time_input = input("Uhrzeit (HH:MM, z.B. 09:30): ").strip()
        if validate_time(time_input):
            break
        print("❌ Ungültige Uhrzeit. Format: HH:MM (00:00 - 23:59)")
    
    # Dauer
    while True:
        duration_input = input("Dauer in Minuten (1-480): ").strip()
        if validate_duration(duration_input):
            duration = int(duration_input)
            break
        print("❌ Dauer muss zwischen 1 und 480 Minuten liegen.")
    
    # Kategorie
    print("\nEmpfohlene Kategorien: Sport, Lernen, Wellness, Bildung, Arbeit, Sonstiges")
    category = input("Kategorie: ").strip()
    if not category:
        category = "Sonstiges"
    
    # Steigerung
    while True:
        increment_input = input("Steigerung pro Woche (Minuten, z.B. 5): ").strip()
        if validate_increment(increment_input):
            increment = int(increment_input)
            break
        print("❌ Steigerung muss 0 oder positive Zahl sein.")
    
    # Neue Routine erstellen
    new_routine = {
        "id": generate_routine_id(routines),
        "name": name,
        "weekday": weekday,
        "time": time_input,
        "duration": duration,
        "category": category,
        "increment": increment
    }
    
    routines.append(new_routine)
    save_routines(routines)
    
    print(f"\n✅ Routine '{name}' hinzugefügt!")
    print(f"   ID: {new_routine['id']} | {weekday} {time_input} | {duration}min | {category}")


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
            add_routine(routines)
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
