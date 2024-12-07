
# CLIST

**CLIST** is a command-line interface (CLI) tool for managing task lists, developed in Python using the `Click` library. This application allows users to interact with their task lists efficiently using simple and intuitive commands.

## Features
- Create and manage task lists.
- Rename existing lists.
- Delete lists and tasks.
- Add, modify, and remove tasks in the lists.
- View all available lists and tasks.
- Interactive interface for handling commands directly.

## Prerequisites
- Python 3.7 or higher.
- The following Python libraries (detailed in `requirements.txt`):
  - `click`

## Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd CLIST
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To initialize the application, run:
```bash
python cli.py init
```

This will start an interactive session where you can manage your task lists. Once initialized, you can enter the commands directly, without needing to type `python cli.py` before each command.

### Main Commands
1. **Command help:**
   ```bash
   htl [command]
   ```
   Lists all commands or shows detailed help for a specific command.

### List Commands
1. **Create a new list:**
   ```bash
   newlist <list_name>
   ```

2. **View all lists:**
   ```bash
   alllist
   ```

3. **Rename a list:**
   ```bash
   chgusr <current_name> <new_name>
   ```

4. **Delete a list:**
   ```bash
   delusr <list_name>
   ```

### Task Management Commands
1. **Add a task to a list:**
   ```bash
   addtask <task_name>
   ```
   Adds a task to the specified list. You need to specify the list name during the session.

2. **View all tasks in a list:**
   ```bash
   alltasks <list_name>
   ```
   Displays all tasks in the specified list.

3. **Rename a task in a list:**
   ```bash
   modtaskname <list_name> <task_name> <new_task_name>
   ```
   Renames a task in the specified list.

4. **Delete a task from a list:**
   ```bash
   deltask <task_name>
   ```
   Removes a task from the specified list.

## Project Structure
```
CLIST/
├── cli.py               # Main script; initializes and defines the app's commands.
├── tools/
│   ├── commands.py      # Defines the available commands for the CLI.
│   ├── db_manager.py    # Manages the JSON database for lists.
├── lists_db/
│   └── db.json          # Database file storing the lists.
├── requirements.txt     # Project dependencies.
```

## Author
Jesús Vega

## Link
https://github.com/JEVG9/TASKLIST_CLI

## Project
https://roadmap.sh/projects/task-tracker
