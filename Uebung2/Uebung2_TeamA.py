# TNKR
# JSOS

"""
- Erstellung der TaskID ist zufällig und kann doppelt sein (add_task)
- Globale Nutzung von Variablen in der Funktion add_task: tasks und backup_tasks 
- Task-Identifizierung über den Namen (und teilweise nur über die ID) -> ID nutzen (mark_done)
- Das Task-Objekt ist ein Array -> eigene Typen/Objekt mit sinnvollen Benennungen
- mark_done liefert einen string anstelle eines booleans zurück
"""

"""
1. Task-Objekt als Objekt und nicht als Array
2. Einheitliche Verwendung der Task-ID (kein Name)
3. Die TaskID muss eindeutig sein und darf nicht verändert werden
4. Überflüssige Verwendung von global entfernen
5. process_tasks() kann einen fertigen Task zu einem unfertigen Task machen
"""

import datetime
import random

tasks = {}
backup_tasks = {}

"""Fügt einen neuen Task hinzu und erstellt eine ID, wenn nicht vorhanden"""
def add_task(name, due_date, priority=3, task_id=None):
    if task_id is None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task.copy()
    return task_id

"""Entfernt einen Task aus der Liste Tasks. True wenn der Task gefunden wurde, sonst false"""
def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

"""Markiert einen Task als 'done'"""
def mark_done(task_name):
    found = False

    for task in tasks.values():
        if task[0] == task_name:
            task[3] = True
            found = True

    return found

"""Zeige alle Tasks an"""
def show_tasks():
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")

"""Schaltet den Status einer zufälligen Aufgabe um: 'offen/fertig'"""
def process_tasks():
    if not tasks:
        return False  # Kein Task vorhanden

    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]

    return True  # Status wurde erfolgreich geändert


"""Gibt einen Durchschnittswert auf Basis der ID zurück"""
def calculate_task_average():
    # Nur numerische Task-IDs berücksichtigen
    numeric_ids = [
        task_id for task_id in tasks
        if isinstance(task_id, int)
    ]

    if not numeric_ids:
        return 0

    return sum(numeric_ids) / len(numeric_ids)

"""Gibt eine sortierte Liste von Tasks aus, welche in der Zukunft liegen"""
def upcoming_tasks():
    today = datetime.date.today()
    upcoming = []

    for task in tasks.values():
        # Datum nur einmal umwandeln
        due_date = datetime.datetime.strptime(
            task[1], "%d-%m-%Y"
        ).date()

        if due_date >= today and not task[3]:
            upcoming.append((due_date, task))

    # Nach dem bereits umgewandelten Datum sortieren
    upcoming.sort(key=lambda item: item[0])

    # Nur die ursprünglichen Tasks zurückgeben
    return [task for due_date, task in upcoming]

"""entfernt abgeschlossene oder inaktive Tasks"""
def cleanup():
    # IDs aller erledigten Tasks ermitteln
    completed_ids = [
        task_id for task_id, task in tasks.items()
        if task[3]
    ]

    # Erledigte Tasks entfernen
    for task_id in completed_ids:
        del tasks[task_id]

    return len(completed_ids)  # Anzahl entfernter Tasks


def get_task_count():
    return len(tasks)


add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())
