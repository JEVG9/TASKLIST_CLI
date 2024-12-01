
import click
from tools.db_manager import *

@click.command(short_help="Show help for a specific command or list all commands.")
@click.argument('command', required=False)
@click.pass_context
def htl(ctx, command):
    """
    Displays help for a specific command or lists all available commands.

    If a command name is passed, it provides detailed help for that command.
    Otherwise, it lists all available commands with their short descriptions.

    Parameters:
        ctx (click.Context): The context object to find the root CLI group.
        command (str, optional): The name of the command to show help for.

    Example Usage:
        - To list all commands:
          `python cli.py htl`
        - To get detailed help for a specific command:
          `python cli.py htl <command_name>`
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

@click.command(short_help="Creates a new task.")
@click.argument('task', required=True)
def addt(task:str):
    """
    Creates a new task and adds it to the database.

    Args:
        task (str): The description of the task to create.

    Returns:
        None. Outputs a success or error message to the console.
    """
    if not task.strip():
        click.echo("TL --> The Task cannot be created, The Task name cannot be empty.")
        return
    if not task_names(task):
        add_task(task)
        click.echo(f"TL --> Task created and added to file")
    else:
        click.echo(f"{task_names(task)}")
        click.echo(f"TL --> Task {task} already exist, try with another ID")

@click.command(short_help = "Modifies an exiting task")
@click.argument('tid',required = True)
@click.argument('newdescrp', required = True)
def modt(tid:str,newdescrp:str):
    """
    Modifies the description of an existing task.

    Args:
        tid (str): The ID of the task to modify.
        newdescrp (str): The new description for the task.

    Returns:
        None. Outputs a success or error message to the console.
    """
    if not tid.strip() or not newdescrp.strip():
        click.echo("TL --> The inputs cannot be empty")
        return
    if not lst_empty():
        if not task_exs(tid):
            click.echo(f"TL --> Task does not exist.")
            return
        upd_task(tid,newdescrp)
        click.echo(f"TL --> Task modified successfully.")
    else:
        click.echo(f"TL --> Task list is empty")

@click.command(short_help = "Deletes an exiting task")
@click.argument('tid',required = True)
def delt(tid):
    """
    Deletes a task from the database.

    Args:
        tid (str): The ID of the task to delete.

    Returns:
        None. Outputs a success or error message to the console.
    """
    if not tid.strip():
        click.echo("TL --> The inputs cannot be empty")
        return
    if not lst_empty():
        del_task(tid)
        click.echo(f"TL --> Task deleted successfully.")
    else:
        click.echo(f"TL --> Task list is empty")

@click.command(short_help = "Changes the status of an exiting task")
@click.argument('tid',required = True)
@click.argument('status',required = True)
def stst(tid,status):
    """
    Changes the status of an existing task.

    Args:
        tid (str): The ID of the task to modify.
        status (str): The new status for the task. Must be "done" or "in-progress".

    Returns:
        None. Outputs a success or error message to the console.
    """
    if not tid.strip() or not status.strip():
        click.echo("TL --> The inputs cannot be empty")
        return
    if not lst_empty():
        if status.lower() not in ["done", "in-progress"]:
            click.echo("TL --> Invalid status. Use 'done' or 'in-progress'.")
            return
        if not task_exs(tid):
            click.echo(f"TL --> Task does not exist.")
            return
        task_sts(tid,status)
        click.echo(f"TL --> Task status changed successfully.")
    else:
        click.echo(f"TL --> Task list is empty")
    
@click.command(short_help = "Changes the status of an exiting task")
@click.option('--listt', default='all', help='The type of task list to return ("all", "done", "to-do", "in-progress").')
def lstt(listt):
    """
    Lists tasks based on their status.

    Args:
        listt (str, optional): The type of tasks to list ("all", "done", "to-do", "in-progress").
                                Defaults to "all".

    Returns:
        None. Outputs the list of tasks to the console.
    """
    toprint = task_lst(listt)
    if toprint is None:
        click.echo("TL --> Invalid list type. Use one of: 'all', 'done', 'to-do', 'in-progress'.")
        return
    click.echo("TL --> LIST OF TASKS")
    for element in toprint:
        click.echo(element)