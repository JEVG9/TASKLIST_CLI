import click
import json



@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo("--------------TASK LIST CLI--------------")
    click.echo("This CLI helps you to make a tasklist")
    click.echo("To close this CLI type 'close'")

    while True:
        try:
            command = input("TL <-- ").strip()

            if command.lower() in ('close'):
                click.echo("Closing")
                break
            try:
                cli.main(args=command.split(), standalone_mode=False)
            except click.exceptions.UsageError as e:
                click.echo(f"invalid command: {e}")
        except KeyboardInterrupt:
            click.echo("\nClosing")
            break

@cli.command()
@click.option('-h','--help','help_command',type=str,required=False, help="Shows a list of the commands or a full description of a command")
def commands(help_command):
    
    ctx = click.get_current_context()
    if not help_command:
        click.echo("TL --> Commands list: ")
        for cmd_name , cmd in cli.commands.items():
            click.echo(f" - {cmd_name} : {cmd.short_help}")
    
    else:
        if help_command in cli.commands:
            cmd = cli.commands[help_command]
            click.echo(f"TL --> Command - '{help_command}':")
            click.echo(cmd.help)
        else:
            click.echo(f"TL --> Command '{help_command}'does not exist")
