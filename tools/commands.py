import click


@click.command(short_help="List all available commands.")
@click.pass_context
def commands(ctx):
    """List all available commands in the CLI."""
    cli = ctx.find_root().command  # Obtén el grupo principal
    click.echo("Commands available:")
    for cmd_name, cmd in cli.commands.items():
        click.echo(f" - {cmd_name}: {cmd.short_help}")

@click.command(short_help="Show help for a specific command or list all commands.")
@click.argument('command', required=False)
@click.pass_context
def help_tl(ctx, command):
    """Show detailed help for a specific command or list all commands."""
    cli = ctx.find_root().command  # Accede al grupo principal
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
    """
    ...


