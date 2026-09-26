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

tasks = None
backup_tasks = {}

"""Fügt einen neuen Task hinzu und erstellt eine ID, wenn nicht vorhanden"""
def add_task(name, due_date, priority=3, task_id=None):
    global tasks, backup_tasks
    if tasks is None:
        tasks = {}

    if task_id == None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id

"""Entfernt einen Task aus der Liste Tasks. True wenn der Task gefunden wurde, sonst false"""
def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

"""Markiert einen Task als 'done'"""
def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"

"""Zeige alle Tasks an"""
def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")

"""Schaltet den Status einer zufälligen Aufgabe um: 'offen/fertig'"""
def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3] # Schaltet den Status 'offen/fertig' um
    return False
    # TODO

"""Gibt einen Durchschnittswert auf Basis der ID zurück"""
def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg

"""Gibt eine sortierte Liste von Tasks aus, welche in der Zukunft liegen"""
def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming

"""entfernt abgeschlossene oder inaktive Tasks"""
def cleanup():
    global tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


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
