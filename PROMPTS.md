# 📋 Prompts – DevRoutineCalendar

Eine Sammlung aller Prompts, die beim Entwickeln dieses Projekts verwendet wurden.  
Nützlich als Referenz, Lerndokumentation und für zukünftige Erweiterungen.

---

## 1. Projekt planen

> Ich möchte eine kleine Python-Konsolen-App in VS Code bauen.  
> Die App soll Routinen verwalten, ähnlich wie ein Kalender.  
> Eine Routine soll Name, Wochentag, Uhrzeit, Dauer, Kategorie und Steigerung in Minuten haben.  
> Bitte hilf mir, einen einfachen MVP zu planen, der für Anfänger umsetzbar ist.

---

## 2. Grundstruktur erstellen

> Erstelle eine einfache Python-Konsolen-App für eine Routine-Kalender-App.  
> Die App soll ein Menü haben mit:
> 1. Routine hinzufügen
> 2. Wochenplan anzeigen
> 3. Feedback eintragen
> 4. Empfehlung anzeigen
> 5. Beenden
>
> Nutze zunächst eine Liste mit Dictionaries und noch keine Datenbank.

---

## 3. Routine hinzufügen

> Schreibe eine Funktion `add_routine()`, mit der ich eine neue Routine hinzufügen kann.  
> Die Routine soll folgende Werte speichern:
> - Name
> - Wochentag
> - Uhrzeit
> - Dauer in Minuten
> - Kategorie
> - Steigerung in Minuten
>
> Speichere die Routine als Dictionary in einer Liste.

---

## 4. Wochenplan anzeigen

> Schreibe eine Funktion `show_week_plan()`, die alle Routinen nach Wochentagen gruppiert ausgibt.  
> Die Wochentage sollen Montag bis Sonntag angezeigt werden.  
> Wenn an einem Tag keine Routine geplant ist, soll "keine Routinen" ausgegeben werden.

---

## 5. Tagesübersicht anzeigen

> Schreibe eine Funktion `show_today_routines()`, die automatisch erkennt, welcher Wochentag heute ist,  
> und nur die Routinen für diesen Tag anzeigt.  
> Nutze dafür das Python-Modul `datetime`.

---

## 6. Feedback eintragen

> Schreibe eine Funktion `add_feedback()`, mit der ich zu einer Routine Feedback eintragen kann.  
> Das Feedback soll folgende Optionen haben:
> 1. gut
> 2. okay
> 3. schwer
> 4. nicht geschafft
>
> Das Feedback soll mit Datum gespeichert werden.

---

## 7. Empfehlung berechnen

> Schreibe eine Funktion `calculate_recommendation(routine)`, die eine empfohlene Dauer für die nächste Woche berechnet.
>
> Regeln:
> - Wenn die letzten zwei Feedback-Einträge "gut" waren, erhöhe die Dauer um `increase_minutes`.
> - Wenn das letzte Feedback "okay" war, bleibt die Dauer gleich.
> - Wenn das letzte Feedback "schwer" war, bleibt die Dauer gleich.
> - Wenn das letzte Feedback "nicht geschafft" war, bleibt die Dauer gleich.
> - Wenn noch nicht genug Feedback vorhanden ist, bleibt die Dauer gleich.

---

## 8. JSON speichern

> Erweitere das Programm so, dass alle Routinen in einer Datei `routines.json` gespeichert werden.  
> Schreibe dafür zwei Funktionen:
> - `save_routines()`
> - `load_routines()`
>
> Beim Programmstart sollen die Routinen geladen werden.  
> Nach jeder Änderung sollen sie gespeichert werden.

---

## 9. Erinnerungsfunktion

> Schreibe eine Funktion `check_reminders()`, die prüft, ob heute eine Routine in den nächsten 10 Minuten beginnt.  
> Wenn ja, soll eine Erinnerung in der Konsole ausgegeben werden.
>
> Beispiel:  
> `"Erinnerung: In 10 Minuten beginnt deine Routine Sport um 18:00."`  
> Nutze `datetime` für die Berechnung.

---

## 10. Routine bearbeiten

> Schreibe eine Funktion `edit_routine()`, mit der ich eine bestehende Routine bearbeiten kann.  
> Ich möchte Name, Wochentag, Uhrzeit, Dauer, Kategorie und Steigerung ändern können.  
> Wenn ich bei einem Feld nichts eingebe, soll der alte Wert behalten werden.

---

## 11. Routine löschen

> Schreibe eine Funktion `delete_routine()`, mit der ich eine Routine anhand ihrer Nummer löschen kann.  
> Zeige vorher alle Routinen nummeriert an.  
> Wenn die Eingabe ungültig ist, soll eine Fehlermeldung erscheinen.

---

## 12. Fehlerbehandlung

> Verbessere die Fehlerbehandlung im gesamten Programm.  
> Das Programm soll nicht abstürzen, wenn der Nutzer:
> - Text statt Zahl eingibt
> - eine ungültige Menüoption wählt
> - eine falsche Uhrzeit eingibt
> - einen unbekannten Wochentag eingibt

---

## 13. Monatsauswertung

> Schreibe eine Funktion `show_month_summary()`, die für jede Routine eine Monatsauswertung erstellt.
>
> Anzeigen soll sie:
> - Name der Routine
> - Anzahl der Feedback-Einträge in diesem Monat
> - Anzahl "gut"
> - Anzahl "okay"
> - Anzahl "schwer"
> - Anzahl "nicht geschafft"
> - Empfehlung für die nächste Woche

---

## 14. Streak-System

> Erstelle eine Funktion `calculate_streak(routine)`, die berechnet, wie oft eine Routine hintereinander erfolgreich war.  
> Als erfolgreich zählen Feedback-Einträge mit "gut" oder "okay".  
> Wenn "schwer" oder "nicht geschafft" vorkommt, wird der Streak unterbrochen.

---

## 15. Kommentare hinzufügen

> Füge verständliche Kommentare zu meinem Python-Code hinzu.  
> Erkläre besonders:
> - was jede Funktion macht
> - warum `datetime` verwendet wird
> - wie die JSON-Speicherung funktioniert
> - wie die Empfehlungslogik funktioniert

---

## 16. Code erklären lassen

> Erkläre mir diesen Python-Code Schritt für Schritt in einfachen Worten.  
> Ich möchte verstehen, was jede Funktion macht und wie die Daten gespeichert werden.

---

## 17. Fehler erklären lassen

> Ich bekomme folgenden Fehler in meinem Python-Projekt.  
> Bitte erkläre mir in einfachen Worten, was der Fehler bedeutet und wie ich ihn beheben kann:
>
> `[Fehlermeldung hier einfügen]`

---

## 18. README erstellen

> Schreibe mir eine `README.md` für mein Python-Projekt "DevRoutineCalendar".  
> Die README soll enthalten:
> - Projektbeschreibung
> - Funktionen
> - Installation
> - Starten des Programms
> - Projektstruktur
> - mögliche Erweiterungen

---

## 19. Lesson Learned schreiben

> Schreibe ein Lesson Learned für mein Projekt "DevRoutineCalendar".  
> Es soll erklären:
> - was die Projektidee war
> - welche Funktionen geplant waren
> - was ich beim Programmieren gelernt habe
> - welche Probleme auftreten können
> - welche Erweiterungen später möglich sind

---

## 20. Refactoring

> Verbessere die Struktur meines Codes.  
> Teile den Code sinnvoll in Funktionen auf, vermeide Wiederholungen und mache ihn lesbarer.  
> Bitte erkläre danach, was verbessert wurde.
