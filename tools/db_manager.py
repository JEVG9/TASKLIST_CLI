import json
from pathlib import Path

current_path = Path(__file__).parent
users_db_folder = current_path.parent / "users_db"
list_db_folder = current_path.parent / "list_db"
db_file = users_db_folder / "db.json"


def filechecker()->None:
    if not users_db_folder.exists():
        users_db_folder.mkdir()
    if not db_file.exists():
        db_file.touch()
        db_file.write_text(json.dumps([],indent=4))
    if not list_db_folder.exists():
        list_db_folder.mkdir()

def check_user(username:str):
    with open(db_file,'r') as jsonfile:
        db=jsonfile.read()
    if username in db:
        return True
    return False

def add_user(newacc:dict):
    with open(db_file, 'r') as jsonfile:
        try:
            data = json.load(jsonfile)
        except json.JSONDecodeError:
            data = []
    data.append(newacc)
    with open(db_file, 'w') as jsonfile:
        json.dump(data,jsonfile,indent=4)
        

"""def change_passw(username:str,password:str,new_password):
    account = {"username":username,
               "password":password}
    account_mod = {"username":username,
                   "password":new_password}
    with open(db_file, 'r') as jsonfile:
        try:
            data = json.load(jsonfile)
        except json.JSONDecodeError:
            return False
    if account in data:
        data[data.index(account)]=account_mod
        with open(db_file,'w') as jsonfile:
            json.dump(data,jsonfile,indent=4)
    else:
        return False
    return True

def get_file_names_in_folder():
    return [f.name for f in list_db_folder.iterdir() if f.is_file()]
"""