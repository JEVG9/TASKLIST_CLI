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
@click.option('command',type=str, help="")
def help():
    ...