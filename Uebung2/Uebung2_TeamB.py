# BNFT, TMMH

'''
Aufgabe 1
1. Wenige bis gar keine Kommentare. Die vorhandenen sind nicht aussagekräftig!
2. Zeile 22 => Warum nicht verändern?
3. Zeile 61 => Was ist das TODO?
4. Funktion get_task_count() ist unnötig komlpiziert
5. Funktion cleanup() ist nicht klar, was passiert (beispielsweise Variable temp)
6. Datenstruktur task nicht schön, Liste wo der Inhalt immer an der selben Stelle sein muss,
    man auch wissen muss => unübersichtlich, lieber Klasse oder dict
7. Einsatz von globalen Variablen!! Nicht gut, trägt zur Unübersichtlichkeit bei
8. Funktion calculate_task_average wird nicht genutzt
9. Zeile 54 division bei Zero
10. Zeile 87/89 upcoming_tasks: Datum wird als String formatiert und ein Stringvergleich wird gemacht
'''

'''
Aufgabe 2
1. Typehints hinzufügen
2. Datenstruktur von Task ändern => Klasse oder Dictionary 
3. Task_id vergabe ändern in add_task + prüfen ob ID schon vergeben
4. globale Variabelen entfernen
5. calculate_task_average entfernen? Division durch Zero entfernen! Summe mit Strings?
6. Ordentliche Funktionsbeschreibung
7. Stringvergleich raus nehmen
'''

import datetime
import random

# tasks = None
# backup_tasks = {}


"""Legt eine Aufgabe an und gibt deren ID zurück."""
def add_task(tasks: dict, name: str, due_date: datetime.date, priority: int = 3,
             task_id: int | str | None = None) -> int | str:
    
    if task_id is None:
        task_id = len(tasks) + random.randint(2, 7)
        # Kollisionen vermeiden, ohne die obige Zeile anzufassen
        while task_id in tasks:
            task_id += 1
    elif task_id in tasks:
        """
        Ohne task_id wird eine freie ID erzeugt. Eine bereits vergebene,
        explizit übergebene ID führt zu einem ValueError.
        """
        raise ValueError(f"ID {task_id} ist bereits vergeben")
 
    tasks[task_id] = {
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "done": False,
        "owner": "user1",
        "created": datetime.datetime.now(),
    }
    return task_id


"""Löscht die Aufgabe. True, wenn sie existierte, sonst False."""
def remove_task(tasks: dict, task_id: int | str) -> bool:
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


"""Markiert alle Aufgaben mit diesem Namen als erledigt."""
def mark_done(tasks: dict, task_name: str) -> str:
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


"""Gibt alle Aufgaben auf der Konsole aus."""
def show_tasks(tasks: dict) -> None:
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


"""Schaltet den Status einer zufälligen Aufgabe um."""
def process_tasks(tasks: dict) -> bool:
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


"""Durchschnitt der Task-IDs."""
def calculate_task_average(tasks: dict) -> float:
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


"""Aufgaben mit Fälligkeitsdatum ab heute."""
def upcoming_tasks(tasks: dict) -> list:
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


"""Entfernt alle erledigten Aufgaben."""
def cleanup(tasks: dict) -> None:
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


"""Anzahl aller gespeicherten Aufgaben."""
def get_task_count(tasks: dict) -> int:
    return sum(1 for _ in tasks) if tasks else 0



if __name__ == "__main__":
    my_tasks: dict = {}
    today = datetime.date.today()
    in_days = lambda n: today + datetime.timedelta(days=n)

    add_task(my_tasks, "Projekt abschließen", in_days(4), 1, task_id="hello")
    add_task(my_tasks, "Projekt abschließen", in_days(4), 1)
    add_task(my_tasks, "Einkaufen gehen", in_days(1), 3)
    add_task(my_tasks, "Dokumentation schreiben", in_days(9), 2)

    print(my_tasks)

    """
    mark_done("Einkaufen gehen")
    process_tasks()
    show_tasks()
    print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
    cleanup()
    print("Gesamtzahl der Aufgaben:", get_task_count())
    """
