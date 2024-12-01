import click
from tools.db_manager import check_list,add_list,listname_chg,del_list,lists_on_db

@click.command(short_help="Show help for a specific command or list all commands.")
@click.argument('command', required=False)
@click.pass_context
def help_tl(ctx, command):
    """
    Displays help for a specific command or lists all available commands.

    If a command name is passed, it provides detailed help for that command.
    Otherwise, it lists all available commands with their short descriptions.

    Parameters:
        ctx (click.Context): The context object to find the root CLI group.
        command (str, optional): The name of the command to show help for.

    Example Usage:
        - To list all commands:
          `python cli.py help_tl`
        - To get detailed help for a specific command:
          `python cli.py help_tl <command_name>`
    """
    cli = ctx.find_root().command
    if not command:
        click.echo("TL --> Available commands:")
        for cmd_name, cmd in cli.commands.items():
            click.echo(f" - {cmd_name}: {cmd.short_help}")
    elif command in cli.commands:
        cmd = cli.commands[command]
        click.echo(f"Help for '{command}':")
        click.echo(cmd.get_help(ctx))
    else:
        click.echo(f"TL --> Error: Command '{command}' does not exist.")

@click.command(short_help="Creates a new list.")
@click.argument('listname', required=True)
def newlist(listname):
    if not listname.strip():
        click.echo(
            "TL --> The list cannot be created. The list name cannot be empty."
        )
        return
    new_list = {"listname":listname,
                   "tasks":{}}
    if check_list(new_list["listname"]):
        click.echo(f"TL --> List {listname} already exist, try with another name")
    else:
        add_list(new_list)
        click.echo(f"TL --> List created and added to file")

@click.command(short_help = "shows all list on db.")
def alllist():
    lists = lists_on_db()
    if lists:
        click.echo("TL --> All lists on file:")
        for listn in lists:
            click.echo(f"> {listn}")
    else:
        click.echo("TL --> No lists on file")

@click.command(short_help = "Changes the name of the list.")
@click.argument('listname',required = True)
@click.argument('newlistname',required = True)
def chgusr(listname,newlistname):
    if not newlistname.split() or not listname.split():
        click.echo("TL --> The new username cannot be empty, ")
    if check_list(listname):
        click.echo(f"TL --> Username changed from {listname} to {newlistname}")
        listname_chg(listname,newlistname)
    
@click.command(short_help = "Deletes the list and all the tasks on it.")
@click.argument('listname',required = True)
def delusr(listname):
    if click.confirm("TL <-- Confirm choice"):
        if check_list(listname):
            del_list(listname)
            click.echo(f"TL --> Deleting account with all lists included.")
        else:
            click.echo(f"TL --> Account does not exist, nothing got deleted.")

@click.command(short_help = "Adds a task on a list")
@click.argument('listname',required=True)
@click.argument('taskname',required = True)
def addtask(listname:str,taskname:str):
    ...

@click.command(short_help = "Returns all task on a list")
@click.argument('listname',required = True)
def alltasks(listname:str):
    ...

@click.command(short_help = "change the name of a task on a list")
@click.argument('listname',required = True)
@click.argument('taskname',required = True)
@click.argument('newtaskname',required = True)
def modtaskname(listname:str,taskname:str,newtaskname:str):
    ...

@click.command(short_help = "Deletes a task on a list")
@click.argument('listname',required = True)
@click.argument('taskname',required = True)
def deltask(listname:str,taskname:str):
    ...

