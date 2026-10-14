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


"""Markiert alle Aufgaben mit diesem Namen als erledigt. True sobald ein Ergebnis gefunden"""
def mark_done(tasks: dict, task_name: str) -> bool:
    found = False
    for task in tasks.values():
        if task["name"] == task_name:
            task["done"] = True
            found = True
    return found


"""Gibt alle Aufgaben auf der Konsole aus."""
def show_tasks(tasks: dict) -> None:
    for task_id, task in tasks.items():
        status = "Erledigt" if task["done"] else "Offen"
        print(f"{task_id}: {task['name']} ({task['priority']}) "
              f"- bis {task['due_date']:%d-%m-%Y} - {status}")


"""Schaltet den Status einer zufälligen Aufgabe um."""
def process_tasks(tasks: dict) -> bool:
    if not tasks:
        return False
    task = tasks[random.choice(list(tasks))]
    task["done"] = not task["done"]
    return True


"""Durchschnitt der Task-IDs."""
def calculate_task_average(tasks: dict) -> float:
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


"""Aufgaben mit Fälligkeitsdatum ab heute."""
def upcoming_tasks(tasks: dict) -> list:
    today = datetime.date.today()
    open_tasks = [t for t in tasks.values()
                  if not t["done"] and t["due_date"] >= today]
    return sorted(open_tasks, key=lambda t: t["due_date"])


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
    today: datetime.date = datetime.date.today()
    in_days = lambda n: today + datetime.timedelta(days=n)

    add_task(my_tasks, "Projekt abschließen", in_days(4), 1, task_id="hello")
    add_task(my_tasks, "Projekt abschließen", in_days(4), 1)
    add_task(my_tasks, "Einkaufen gehen", in_days(1), 3)
    add_task(my_tasks, "Dokumentation schreiben", in_days(9), 2)

    mark_done(my_tasks, "Einkaufen gehen")

    process_tasks(my_tasks)
    show_tasks(my_tasks)

    print("Offene Aufgaben nach Datum sortiert:")
    for t in upcoming_tasks(my_tasks):
        print(f"  {t['due_date']:%d-%m-%Y} {t['name']}")

    """
    
    cleanup()
    print("Gesamtzahl der Aufgaben:", get_task_count())
    """
