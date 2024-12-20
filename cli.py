import click
import shlex
from tools.commands import *
from tools.db_manager import  filechecker

@click.group()
def cli():
    """Task List CLI - Manage your tasks interactively."""
    pass

cli.add_command(htl)
cli.add_command(addt)
cli.add_command(modt)
cli.add_command(delt)
cli.add_command(stst)
cli.add_command(lstt)


@cli.command(short_help="Start the interactive CLI session.")
def init():
    """Initialize the interactive task list CLI.

    This command starts an interactive session for managing tasks.
    Type 'close' to exit the session.
    """
    click.echo("--------------TASK LIST CLI--------------")
    click.echo("This CLI helps you to manage your tasks")
    click.echo("To close this CLI, type 'close'")
    filechecker()
    while True:
        try:
            command = input("TL <-- ").strip()
            if command.lower() in ('close', 'exit'):
                click.echo("Closing")
                break
            try:
                cli.main(args=shlex.split(command), standalone_mode=False)
            except click.exceptions.UsageError as e:
                click.echo(f"Invalid command: {e}")
        except KeyboardInterrupt:
            click.echo("\nClosing")
            break

if __name__ == "__main__":
    cli()
