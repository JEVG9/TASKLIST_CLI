from importlib.metadata import requires

import click
from tools.db_manager import *

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

@click.command(short_help="Creates a new task.")
@click.argument('task', required=True)
def addt(task):
    if not task.strip():
        click.echo(
            "TL --> The Task cannot be created, The Task name cannot be empty."
        )
        return
    if not task_names(task):
       click.echo(f"TL --> Task {task} already exist, try with another ID")
    else:
        add_task(task)
        click.echo(f"TL --> Task created and added to file")

@click.command(short_help = "Modifies an exiting task")
@click.argument('id',required = True)
@click.argument('newdescrp', required = True)
def modt(id,newdescrp):
    upd_task(id,newdescrp)
    click.echo(f"Task modified successfully.")

@click.command(short_help = "Deletes an exiting task")
@click.argument('id',required = True)
def delt(id):
    del_task(id)
    click.echo(f"Task deleted successfully.")

@click.command(short_help = "Changes the status of an exiting task")
@click.argument('id',required = True)
@click.argument('status',required = True)
def stst(id,status):
    task_sts(id,status)
    click.echo(f"Task status changed successfully.")
    
@click.command(short_help = "Changes the status of an exiting task")
@click.argument('list_type')
def lstt(list_type):
    toprint = task_lst(list_type)
    click.echo(f"TL --> LIST OF TASKS")
    for element in toprint:
        click.echo(element)