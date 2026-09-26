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
'''

'''
Aufgabe 2
1. Typehints hinzufügen
2. Datenstruktur von Task ändern => Klasse oder Dictionary 
3. Task_id vergabe ändern in add_task + prüfen ob ID schon vergeben
4. globale Variabelen entfernen
5. calculate_task_average entfernen? Division durch Zero entfernen! Summe mit Strings?
6. Ordentliche Funktionsbeschreibung
'''

import datetime
import random

tasks = None
backup_tasks = {}


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


def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


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
