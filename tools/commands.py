import click
from tools.db_manager import check_user,add_user


@click.command(short_help="List all available commands.")
@click.pass_context
def commands(ctx):
    """List all available commands in the CLI."""
    cli = ctx.find_root().command
    click.echo("Commands available:")
    for cmd_name, cmd in cli.commands.items():
        click.echo(f" - {cmd_name}: {cmd.short_help}")

@click.command(short_help="Show help for a specific command or list all commands.")
@click.argument('command', required=False)
@click.pass_context
def help_tl(ctx, command):
    """Show detailed help for a specific command or list all commands."""
    cli = ctx.find_root().command
    if not command:
        click.echo("TL --> Commands list:")
        for cmd_name, cmd in cli.commands.items():
            click.echo(f" - {cmd_name}: {cmd.short_help}")
    elif command in cli.commands:
        cmd = cli.commands[command]
        click.echo(f"TL --> Help for command '{command}':")
        click.echo(cmd.help)
    else:
        click.echo(f"TL --> Command '{command}' does not exist.")

@click.command(short_help="Creates a new account.")
@click.argument('username', required=True)  # Define el primer argumento
@click.argument('passw', required=True)    # Define el segundo argumento
def newacc(username, passw):
    """
    This command is for the creation of a new account.

    The command newacc requires both params, so it can check
    if the username exist.
    :param username:str
    :param passw:str

    Once checked the user gets added to the db file.
    """
    if not username.strip() or not passw.strip() or len(passw) < 4:
        click.echo(
            "The account cannot be created. The username and/or password "
            "cannot be empty. Also, the password must be at least 4 characters long."
        )
        return

    new_account = {"username":username,
                   "passw":passw,
                   "TLS":{}}
    
    if check_user(new_account["username"]):
        click.echo(f"User {username} already exist, try with another name")
    else:
        add_user(new_account)
        click.echo(f"Account created and added to file")


    


