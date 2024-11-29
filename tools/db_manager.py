import json
from pathlib import Path

current_path = Path(__file__).parent
users_db_folder = current_path.parent / "users_db"
db_file = users_db_folder / "db.json"

def filechecker() -> None:
    """
    Ensures the existence of the necessary database directory and file.

    This function checks if the directory for storing the user database (`users_db_folder`) 
    and the database file (`db_file`) exist. If either does not exist, the function creates them.
    The database file is initialized as an empty JSON array.

    Parameters:
        None

    Returns:
        None: This function does not return any value but ensures the directory and file are ready.

    Example Usage:
        filechecker()
    """
    if not users_db_folder.exists():
        users_db_folder.mkdir()
    if not db_file.exists():
        db_file.touch()
        db_file.write_text(json.dumps([], indent=4))

def check_user(username: str) -> bool:
    """
    Checks if a username exists in the database.

    This function reads the user database and verifies whether a given username exists.

    Parameters:
        username (str): The username to check for in the database.

    Returns:
        bool: 
            - True if the username exists in the database.
            - False otherwise.

    Example Usage:
        exists = check_user("test_user")
        if exists:
            print("User exists.")
        else:
            print("User does not exist.")
    """
    with open(db_file, 'r') as jsonfile:
        db = jsonfile.read()
    if username in db:
        return True
    return False

def add_user(newacc: dict) -> None:
    """
    Adds a new user to the database.

    This function appends a new user record (as a dictionary) to the existing user database.
    If the database file is empty or invalid, it initializes it as an empty list.

    Parameters:
        newacc (dict): A dictionary representing the new user, typically containing:
                       - "username": The user's unique username.
                       - "TLS": Additional reserved data.

    Returns:
        None: This function does not return any value but updates the database file.

    Example Usage:
        new_user = {"username": "test_user", "TLS": {}}
        add_user(new_user)
    """
    with open(db_file, 'r') as jsonfile:
        try:
            data = json.load(jsonfile)
        except json.JSONDecodeError:
            data = []
    data.append(newacc)
    with open(db_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def username_chg(username: str, newusername: str) -> None:
    """
    Changes the username of an existing user in the database.

    This function locates a user record in the database by their current username
    and updates it to a new username. If the user is not found, no changes are made.

    Parameters:
        username (str): The current username of the user.
        newusername (str): The new username to assign to the user.

    Returns:
        None: This function does not return any value but modifies the database file.

    Example Usage:
        username_chg("old_user", "new_user")
    """
    with open(db_file, 'r') as jsonfile:
        db = json.load(jsonfile)
    for user in db:
        if user["username"] == username:
            user["username"] = newusername
            break
    with open(db_file, 'w') as jsonfile:
        json.dump(db, jsonfile, indent=4)

