
# CLIST

**CLIST** is a command-line interface (CLI) tool for managing task lists, developed in Python using the `Click` library. This application allows users to interact with their task lists efficiently using simple and intuitive commands.

## Features
- Create and manage task lists.
- Rename existing lists.
- Delete lists and tasks.
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

This will start an interactive session where you can manage your task lists. Type help_tl to see the available commands.

### Main Commands
1. **Command help:**
   ```bash
   python cli.py help_tl [command]
   ```
   Lists all commands or shows detailed help for a specific command.

2. **Create a new list:**
   ```bash
   python cli.py newlist <nombre_lista>
   ```

3. **View all lists:**
   ```bash
   python cli.py alllist
   ```

4. **Rename a list:**
   ```bash
   python cli.py chgusr <current_name> <new_name>
   ```

5. **Delete a list:**
   ```bash
   python cli.py delusr <list_name>
   ```

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

## Autor
Jesús Vega
