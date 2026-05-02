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


def show_all(routines):
    """Zeigt alle Routinen in einer Tabelle an"""
    if not routines:
        print("\n⚠️  Keine Routinen vorhanden.")
        return
    
    # Routinen sortieren nach Wochentag und Uhrzeit
    def sort_key(routine):
        weekday_index = WEEKDAYS.index(routine.get("weekday", "Montag"))
        time_parts = routine.get("time", "00:00").split(":")
        time_minutes = int(time_parts[0]) * 60 + int(time_parts[1])
        return (weekday_index, time_minutes)
    
    sorted_routines = sorted(routines, key=sort_key)
    
    # Tabelle erstellen
    print("\n" + "=" * 120)
    print("📋 ALLE ROUTINEN")
    print("=" * 120)
    print(f"{'ID':<4} | {'Name':<20} | {'Wochentag':<12} | {'Uhrzeit':<8} | {'Dauer':<8} | {'Kategorie':<15} | {'Steigerung':<10}")
    print("-" * 120)
    
    for routine in sorted_routines:
        routine_id = routine.get("id", "?")
        name = routine.get("name", "?")[:19]  # Max 19 Zeichen
        weekday = routine.get("weekday", "?")[:11]
        time_str = routine.get("time", "?")
        duration = f"{routine.get('duration', '?')}min"
        category = routine.get("category", "?")[:14]
        increment = f"+{routine.get('increment', 0)}min/Wo"
        
        print(f"{routine_id:<4} | {name:<20} | {weekday:<12} | {time_str:<8} | {duration:<8} | {category:<15} | {increment:<10}")
    
    print("=" * 120)
    print(f"Gesamt: {len(sorted_routines)} Routine(n)")
    print()


def show_calendar(routines):
    """Zeigt Routinen als Wochenkalender an (nach Wochentag sortiert)"""
    if not routines:
        print("\n⚠️  Keine Routinen vorhanden.")
        return
    
    # Routinen nach Wochentag gruppieren
    calendar = {day: [] for day in WEEKDAYS}
    
    for routine in routines:
        weekday = routine.get("weekday", "Montag")
        if weekday in calendar:
            calendar[weekday].append(routine)
    
    # Jeden Wochentag sortieren nach Uhrzeit
    for day in WEEKDAYS:
        calendar[day].sort(key=lambda r: r.get("time", "00:00"))
    
    # Kalender anzeigen
    print("\n" + "=" * 100)
    print("📅 WOCHENKALENDER")
    print("=" * 100)
    
    for day in WEEKDAYS:
        routines_on_day = calendar[day]
        print(f"\n{day.upper()}")
        print("-" * 100)
        
        if not routines_on_day:
            print("  (Keine Routinen)")
        else:
            for routine in routines_on_day:
                name = routine.get("name", "?")
                time_str = routine.get("time", "?")
                duration = routine.get("duration", "?")
                category = routine.get("category", "?")
                
                print(f"  {time_str} - {name:<25} | {duration}min | {category}")
    
    print("\n" + "=" * 100)


def find_routine_by_id(routines, routine_id):
    """Sucht Routine nach ID"""
    for i, routine in enumerate(routines):
        if routine.get("id") == routine_id:
            return (i, routine)
    return (None, None)


def edit_routine(routines):
    """Bearbeitet eine Routine"""
    if not routines:
        print("\n⚠️  Keine Routinen vorhanden.")
        return
    
    print("\n" + "=" * 40)
    print("✏️  ROUTINE BEARBEITEN")
    print("=" * 40)
    
    # Routine nach ID suchen
    show_all(routines)
    routine_id = input("Routine ID eingeben: ").strip()
    
    index, routine = find_routine_by_id(routines, routine_id)
    if index is None:
        print(f"❌ Routine mit ID '{routine_id}' nicht gefunden.")
        return
    
    print(f"\n✏️  Bearbeite: {routine.get('name')}")
    print("\nWas möchtest du ändern?")
    print("1. Name")
    print("2. Wochentag")
    print("3. Uhrzeit")
    print("4. Dauer")
    print("5. Kategorie")
    print("6. Steigerung")
    print("7. Alle ändern")
    print("0. Zurück")
    
    choice = input("\nAuswahl (0-7): ").strip()
    
    if choice == "0":
        return
    
    # Hilfsfunktion zum Ändern einzelner Felder
    def update_field(field_name, field_key, validator, input_prompt):
        if choice in ["7", str(field_key)] or choice == str(field_key):
            while True:
                new_value = input(f"{input_prompt} (aktuell: {routine.get(field_key)}): ").strip()
                if validator(new_value):
                    routine[field_key] = new_value
                    break
                else:
                    print(f"❌ Ungültige Eingabe für {field_name}.")
    
    if choice == "1" or choice == "7":
        while True:
            new_name = input(f"Neuer Name (aktuell: {routine.get('name')}): ").strip()
            if len(new_name) >= 3:
                routine["name"] = new_name
                break
            print("❌ Name muss mindestens 3 Zeichen lang sein.")
    
    if choice == "2" or choice == "7":
        print("\nVerfügbare Wochentage:")
        for i, day in enumerate(WEEKDAYS, 1):
            print(f"  {i}. {day}")
        while True:
            weekday_input = input(f"Neuer Wochentag (aktuell: {routine.get('weekday')}): ").strip()
            try:
                if weekday_input.isdigit():
                    weekday_idx = int(weekday_input) - 1
                    if 0 <= weekday_idx < len(WEEKDAYS):
                        routine["weekday"] = WEEKDAYS[weekday_idx]
                        break
                elif validate_weekday(weekday_input):
                    routine["weekday"] = weekday_input.capitalize()
                    break
            except:
                pass
            print("❌ Ungültige Eingabe.")
    
    if choice == "3" or choice == "7":
        while True:
            new_time = input(f"Neue Uhrzeit (aktuell: {routine.get('time')}): ").strip()
            if validate_time(new_time):
                routine["time"] = new_time
                break
            print("❌ Ungültige Uhrzeit. Format: HH:MM")
    
    if choice == "4" or choice == "7":
        while True:
            new_duration = input(f"Neue Dauer in Min (aktuell: {routine.get('duration')}): ").strip()
            if validate_duration(new_duration):
                routine["duration"] = int(new_duration)
                break
            print("❌ Ungültige Dauer (1-480).")
    
    if choice == "5" or choice == "7":
        new_category = input(f"Neue Kategorie (aktuell: {routine.get('category')}): ").strip()
        if new_category:
            routine["category"] = new_category
    
    if choice == "6" or choice == "7":
        while True:
            new_increment = input(f"Neue Steigerung (aktuell: {routine.get('increment')}): ").strip()
            if validate_increment(new_increment):
                routine["increment"] = int(new_increment)
                break
            print("❌ Ungültige Steigerung.")
    
    routines[index] = routine
    save_routines(routines)
    print(f"\n✅ Routine '{routine.get('name')}' aktualisiert!")


def delete_routine(routines):
    """Löscht eine Routine"""
    if not routines:
        print("\n⚠️  Keine Routinen vorhanden.")
        return
    
    print("\n" + "=" * 40)
    print("❌ ROUTINE LÖSCHEN")
    print("=" * 40)
    
    # Routine nach ID suchen
    show_all(routines)
    routine_id = input("Routine ID zum Löschen eingeben: ").strip()
    
    index, routine = find_routine_by_id(routines, routine_id)
    if index is None:
        print(f"❌ Routine mit ID '{routine_id}' nicht gefunden.")
        return
    
    # Bestätigung abfragen
    print(f"\n⚠️  Du möchtest diese Routine LÖSCHEN:")
    print(f"   {routine.get('name')} ({routine.get('weekday')} {routine.get('time')})")
    
    confirm = input("\nBist du sicher? (ja/nein): ").strip().lower()
    if confirm in ["ja", "j", "yes", "y"]:
        deleted = routines.pop(index)
        save_routines(routines)
        print(f"\n✅ Routine '{deleted.get('name')}' gelöscht!")
    else:
        print("❌ Löschen abgebrochen.")
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
            show_calendar(routines)
        elif choice == "2":
            add_routine(routines)
        elif choice == "3":
            show_all(routines)
        elif choice == "4":
            edit_routine(routines)
        elif choice == "5":
            delete_routine(routines)
        elif choice == "6":
            print("\n👋 Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
