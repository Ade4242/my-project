# 📅 Routine Tracker - Python CLI App

Eine einfache Python-Konsolen-App zur Verwaltung von täglichen Routinen mit Kalender-Funktion. Perfekt für Anfänger geeignet!

## 🎯 Features

✅ **CRUD-Operationen** (Create, Read, Update, Delete)
- ➕ Neue Routinen hinzufügen
- 📋 Alle Routinen anzeigen
- ✏️ Routinen bearbeiten
- ❌ Routinen löschen

✅ **Zwei View-Modi**
- 📅 **Wochenkalender**: Routinen nach Wochentag sortiert
- 📊 **Tabelle**: Alle Routinen mit allen Details

✅ **Routine-Eigenschaften**
- 📝 Name
- 📅 Wochentag (Montag bis Sonntag)
- 🕐 Uhrzeit (HH:MM Format)
- ⏱️ Dauer in Minuten
- 🏷️ Kategorie (Sport, Lernen, Wellness, etc.)
- 📈 Wöchentliche Steigerung (in Minuten)

✅ **Persistierung**
- 💾 Routinen werden in `routines.json` gespeichert
- 🔄 Automatisches Laden beim Programmstart
- 🛡️ Fehlerbehandlung bei ungültigen Daten

## 🚀 Schnellstart

### Installation
```bash
# Keine externen Abhängigkeiten nötig!
# Nur Python 3.6+ erforderlich
```

### Programm starten
```bash
python routine_tracker.py
```

## 📖 Benutzerhandbuch

### Hauptmenü
```
📅 ROUTINE TRACKER - Kalender App
========================================
1. 📅 Kalender anzeigen
2. ➕ Routine hinzufügen
3. 📋 Alle Routinen anzeigen
4. ✏️  Routine bearbeiten
5. ❌ Routine löschen
6. 🚪 Beenden
========================================
```

### 1️⃣ Kalender anzeigen
Zeigt die Woche mit allen Routinen sortiert nach Wochentag und Uhrzeit an.

```
MONTAG
  06:30 - Joggen                    | 60min | Sport

DIENSTAG
  09:00 - Coding Practice           | 90min | Lernen
```

### 2️⃣ Routine hinzufügen
Interaktiver Assistent zur Erstellung einer neuen Routine:
- Name eingeben (min. 3 Zeichen)
- Wochentag wählen (1-7 oder Name)
- Uhrzeit eingeben (HH:MM Format)
- Dauer angeben (1-480 Minuten)
- Kategorie eingeben
- Wöchentliche Steigerung angeben

```
➕ NEUE ROUTINE HINZUFÜGEN
========================================
Routine Name (min. 3 Zeichen): Laufen
Wochentag (1-7 oder Name): 1
Uhrzeit (HH:MM, z.B. 09:30): 06:30
Dauer in Minuten (1-480): 45
Kategorie: Sport
Steigerung pro Woche (Minuten, z.B. 5): 5
```

### 3️⃣ Alle Routinen anzeigen
Zeigt alle Routinen in einer sortierten Tabelle:

```
📋 ALLE ROUTINEN
ID  | Name                | Wochentag    | Uhrzeit  | Dauer    | Kategorie
001 | Joggen              | Montag       | 06:30    | 60min    | Sport
002 | Coding Practice     | Dienstag     | 09:00    | 90min    | Lernen
```

### 4️⃣ Routine bearbeiten
Wähle eine Routine nach ID und ändere einzelne Felder oder alle gleichzeitig:

```
✏️  ROUTINE BEARBEITEN
1. Name
2. Wochentag
3. Uhrzeit
4. Dauer
5. Kategorie
6. Steigerung
7. Alle ändern
0. Zurück
```

### 5️⃣ Routine löschen
Wähle eine Routine nach ID zum Löschen (mit Bestätigung):

```
❌ ROUTINE LÖSCHEN
⚠️  Du möchtest diese Routine LÖSCHEN:
   Coding Practice (Dienstag 09:00)
Bist du sicher? (ja/nein): ja
```

## 📁 Dateistruktur

```
my-project/
├── routine_tracker.py          # Hauptprogramm
├── routines.json               # Speicherdatei (auto-erstellt)
├── routines_calendar.json      # Test-Daten
└── README.md                   # Diese Datei
```

## 💾 Dateiformat (routines.json)

```json
[
  {
    "id": "001",
    "name": "Joggen",
    "weekday": "Montag",
    "time": "06:30",
    "duration": 60,
    "category": "Sport",
    "increment": 5
  },
  {
    "id": "002",
    "name": "Meditation",
    "weekday": "Mittwoch",
    "time": "20:00",
    "duration": 20,
    "category": "Wellness",
    "increment": 2
  }
]
```

## 🛡️ Validierungsregeln

| Feld | Format | Beispiel | Bereich |
|---|---|---|---|
| Name | Text | "Joggen" | Min. 3 Zeichen |
| Wochentag | Text oder Zahl | "Montag" oder "1" | Mo-So / 1-7 |
| Uhrzeit | HH:MM | "06:30" | 00:00 - 23:59 |
| Dauer | Zahl | "60" | 1-480 Minuten |
| Kategorie | Text | "Sport" | Beliebig |
| Steigerung | Zahl | "5" | 0 oder positiv |

## 🔧 Technische Details

### Funktionen im Code

**Datenmodell:**
- `load_routines()` - Lädt Routinen aus JSON
- `save_routines()` - Speichert Routinen in JSON
- `generate_routine_id()` - Generiert eindeutige ID

**Validierung:**
- `validate_time()` - Prüft Uhrzeit-Format
- `validate_weekday()` - Prüft Wochentag
- `validate_duration()` - Prüft Dauer-Wert
- `validate_increment()` - Prüft Steigerungs-Wert

**Operationen:**
- `add_routine()` - Neue Routine hinzufügen
- `show_all()` - Alle Routinen in Tabelle
- `show_calendar()` - Wochenkalender-View
- `edit_routine()` - Routine bearbeiten
- `delete_routine()` - Routine löschen
- `find_routine_by_id()` - Sucht Routine nach ID

**Menü:**
- `display_menu()` - Zeigt Hauptmenü
- `get_user_choice()` - Holt validierte Eingabe
- `main()` - Programmschleife

### Dependencies
```
Python 3.6+
json (Standard Library)
os (Standard Library)
datetime (Standard Library)
```

## 📝 Beispiel-Workflow

### Szenario: Neue Trainingsroutine hinzufügen

1. **Programm starten**
   ```bash
   python routine_tracker.py
   ```

2. **Option 2 wählen** (Routine hinzufügen)
   ```
   Auswahl (1-6): 2
   ```

3. **Details eingeben**
   ```
   Routine Name: Laufen
   Wochentag: Montag (oder 1)
   Uhrzeit: 06:30
   Dauer: 45
   Kategorie: Sport
   Steigerung: 5
   ```

4. **Bestätigung**
   ```
   ✅ Routine 'Laufen' hinzugefügt!
   ID: 005 | Montag 06:30 | 45min | Sport
   ```

5. **Kalender anschauen**
   ```
   Auswahl (1-6): 1
   (Zeigt Kalender mit neuer Routine)
   ```

## 🐛 Fehlerbehandlung

- ❌ **Ungültige Eingabe**: Benutzer wird aufgefordert, erneut einzugeben
- ❌ **Routine nicht gefunden**: ID wird überprüft, Fehlermeldung angezeigt
- ❌ **Fehlerhafte JSON**: Fallback auf leere Liste beim Laden
- ❌ **Bestätigung erforderlich**: Vor dem Löschen wird abgefragt

## 💡 Anfänger-Tipps

### Code verstehen
1. **main.py-Aufbau**: Import → Konstanten → Funktionen → main()
2. **JSON-Struktur**: Jede Routine ist ein Dictionary mit 7 Schlüsseln
3. **Validierung**: Benutzer-Input wird vor dem Speichern geprüft
4. **Schleife**: `while True` läuft bis der Benutzer "Beenden" wählt

### Weitere Entwicklungen möglich
- 🔔 Erinnerungen/Benachrichtigungen
- 📊 Statistiken (wie viel Zeit insgesamt?)
- 🎯 Fortschritts-Tracking
- 🌐 Export in CSV/Excel
- 🎨 Farbige Terminal-Ausgabe
- 📱 Web-Interface mit Flask

## 📄 Lizenz
Frei verwendbar für Lernzwecke.

## 👨‍💻 Autor
Erstellt als MVP für einen Python-Anfänger mit GitHub Copilot CLI.

---

**Viel Erfolg beim Verwenden und Erweitern der App! 🚀**
