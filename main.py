routines = []
chat_log = ""

def log_input(user_input):
    with open("user_inputs.log", "a") as log_file:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {user_input}\n"
        log_file.write(entry)
        global chat_log
        chat_log += entry


def show_chat_log():
    print("\n=== Eingaben-Log ===")
    print(chat_log if chat_log else "Noch keine Eingaben vorhanden.")


def show_menu():
    print("\n=== Dev Routine Tracker ===")
    print("1. Routine hinzufügen")
    print("2. Routinen anzeigen")
    print("3. Routine als erledigt markieren")
    print("4. Fortschritt anzeigen")
    print("5. Beenden")


def add_routine():
    name = input("Name der Routine: ")
    log_input(name)
    routine = {
        "name": name,
        "done": False
    }
    routines.append(routine)
    print("Routine wurde hinzugefügt.")


def show_routines():
    if len(routines) == 0:
        print("Noch keine Routinen vorhanden.")
        return

    print("\nDeine Routinen:")
    for index, routine in enumerate(routines, start=1):
        status = "✅" if routine["done"] else "⬜"
        print(f"{index}. {status} {routine['name']}")


def mark_done():
    show_routines()

    if len(routines) == 0:
        return

    choice = int(input("Welche Routine wurde erledigt? Nummer eingeben: "))

    if 1 <= choice <= len(routines):
        routines[choice - 1]["done"] = True
        print("Routine wurde als erledigt markiert.")
    else:
        print("Ungültige Nummer.")


def delete_routine():
    show_routines()

    if len(routines) == 0:
        return

    choice_str = input("Welche Routine soll gelöscht werden? Nummer eingeben: ")
    log_input(choice_str)
    choice = int(choice_str)

    if 1 <= choice <= len(routines):
        deleted_routine = routines.pop(choice - 1)
        print(f"Routine '{deleted_routine['name']}' wurde gelöscht.")
    else:
        print("Ungültige Nummer.")


def show_progress():
    if len(routines) == 0:
        print("Noch keine Routinen vorhanden.")
        return

    done_count = 0

    for routine in routines:
        if routine["done"]:
            done_count += 1

    total = len(routines)
    percent = done_count / total * 100

    print(f"Erledigt: {done_count} von {total}")
    print(f"Fortschritt: {percent:.0f}%")


while True:
    show_menu()
    choice = input("Auswahl: ")
    log_input(choice)

    if choice == "1":
        add_routine()
    elif choice == "2":
        show_routines()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        show_progress()
    elif choice == "6":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe.")