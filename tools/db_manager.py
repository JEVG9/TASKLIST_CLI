import json
from pathlib import Path

current_path = Path(__file__).parent
users_db_folder = current_path.parent / "lists_db"
db_file = users_db_folder / "db.json"

def filechecker() -> None:
    if not users_db_folder.exists():
        users_db_folder.mkdir()
    if not db_file.exists():
        db_file.touch()
        db_file.write_text(json.dumps([], indent=4))

def check_list(listname: str) -> bool:
    with open(db_file, 'r') as jsonfile:
        db = jsonfile.read()
    if listname in db:
        return True
    return False

def add_list(newlist: dict) -> None:
    with open(db_file, 'r') as jsonfile:
        try:
            data = json.load(jsonfile)
        except json.JSONDecodeError:
            data = []
    data.append(newlist)
    with open(db_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def listname_chg(listname: str, newlistname: str) -> None:
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    for lists in db:
        if lists["listname"] == listname:
            lists["listname"] = newlistname
            break
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

def del_list(listname:str)->None:
    with open(db_file, 'r') as jsonfile:
        db=json.load(jsonfile)
    for lists in db:
        if lists["listname"] == listname:
            db.remove(lists)
            break
    with open(db_file, 'w') as jsonfile:
        json.dump(db,jsonfile,indent=4)

def lists_on_db():
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    return [entry["listname"] for entry in db if "listname" in entry]

def add_task(listname:str,task:str):
    with open(db_file, 'r') as jsonfile:
        db=json.load(jsonfile)
    for lists in db:
        if lists["listname"]==listname:
            lists["tasks"]...