import json
import hashlib
from datetime import datetime
from pathlib import Path

# Paths definition
current_path = Path(__file__).parent
users_db_folder = current_path.parent / "list_db"
db_file = users_db_folder / "db.json"


def filechecker() -> None:
    """
    Checks if the database folder and the database file exist. If they don't,
    it creates them. If the database file doesn't exist, it initializes it with
    an empty list.

    This function ensures that the necessary directory and file for storing
    task data are present. If the file is missing, it creates and writes an empty
    JSON array to the file.
    """
    if not users_db_folder.exists():
        users_db_folder.mkdir()
    if not db_file.exists():
        db_file.touch()
        db_file.write_text(json.dumps([], indent=4))

def id_gen(data: str) -> str:
    """
    Generates a unique 4-character alphanumeric ID based on a SHA-1 hash of the provided data.
    If the ID already exists in the database, a counter is added to the data to ensure uniqueness.

    Args:
        data (str): The input data used to generate the ID.

    Returns:
        str: The unique 4-character ID.
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    all_ids = [task["id"] for task in db] if db else []
    counter = 0
    while True:
        unique_data = f"{data}_{counter}" if counter > 0 else data
        unique_id = hashlib.sha1(unique_data.encode()).hexdigest()[:4]
        if unique_id not in all_ids:
            return unique_id
        counter += 1

def add_task(task: str) -> None:
    """
    Adds a new task to the database with a status of "to-do", the current time as the 'createdAt'
    and 'updatedAt' fields, and a unique generated ID.

    Args:
        task (str): The description of the task to add.
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    timenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.append({"id": id_gen(task),
               "description": task,
               "status": "to-do",
               "createdAt": timenow,
               "updatedAt": timenow})
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

def upd_task(task_id: str, newdescrp: str) -> None:
    """
    Updates the description of an existing task and sets the 'updatedAt' field to the current time.

    Args:
        task_id (str): The ID of the task to update.
        newdescrp (str): The new description for the task.
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    for tasks in db:
        if tasks["id"] == task_id:
            tasks["description"] = newdescrp
            tasks["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

def del_task(task_id: str) -> None:
    """
    Deletes a task from the database using its ID.

    Args:
        task_id (str): The ID of the task to delete.
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    db = [task for task in db if task["id"] != task_id]
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

def task_sts(task_id: str, status: bool) -> None:
    """
    Updates the status of a task (either "in-progress" or "done") and sets the 'updatedAt' field to the current time.

    Args:
        task_id (str): The ID of the task to update.
        status (bool): The new status for the task, where False means "in-progress" and True means "done".
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    statuses = {False: "in-progress", True: "done"}
    for tasks in db:
        if tasks["id"] == task_id:
            tasks["status"] = statuses[status]
            tasks["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

def task_lst(list_type: str = "all") -> list:
    """
    Returns a list of tasks filtered by their status. The status can be "all", "done", "to-do", or "in-progress".

    Args:
        list_type (str): The type of task list to return ("all", "done", "to-do", "in-progress"). Default is "all".

    Returns:
        list: A list of tasks formatted as strings, or None if the list type is invalid.
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    if list_type == "all":
        tasks_to_print = db
    elif list_type in ["done", "todo", "in-progress"]:
        tasks_to_print = [task for task in db if task["status"] == list_type]
    else:
        return None
    return [f"|{task['id']} | {task['description']} | {task['createdAt']} | {task['updatedAt']}|" for task in
            tasks_to_print]
