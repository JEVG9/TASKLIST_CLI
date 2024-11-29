import click
from tools.db_manager import check_user,add_user,username_chg


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
        click.echo("Available commands:")
        for cmd_name, cmd in cli.commands.items():
            click.echo(f" - {cmd_name}: {cmd.short_help}")
    elif command in cli.commands:
        cmd = cli.commands[command]
        click.echo(f"Help for '{command}':")
        click.echo(cmd.get_help(ctx))
    else:
        click.echo(f"Error: Command '{command}' does not exist.")

@click.command(short_help="Creates a new account.")
@click.argument('username', required=True)
def newacc(username):
    """
    Creates a new user account and adds it to the database.

    This command allows the creation of a new user account by taking only a username as an argument.
    The function performs the following checks:
    
    1. Ensures that the username is not empty.
    2. Checks if the username already exists in the database.

    If all the conditions are satisfied, the new account is added to the database file 
    as a JSON object containing:
      - "username": the unique username for the account.
      - "TLS": an empty dictionary reserved for future use.

    If any condition is not met, the function displays an appropriate error message 
    and exits without creating the account.

    Parameters:
        username (str): The desired username for the account.

    Returns:
        None: This function does not return any value, but prints messages to the console
              indicating the result of the operation.

    Error Messages:
        - If the username is empty:
          "The account cannot be created. The username cannot be empty."
        - If the username already exists in the database:
          "User '<username>' already exists. Try with another name."

    Success Message:
        - If the account is successfully created:
          "Account '<username>' created and added to the file."

    Example Usage:
        To create a new account:
        `python cli.py newacc <username>`
    """
    if not username.strip():
        click.echo(
            "The account cannot be created. The username cannot be empty."
        )
        return
    new_account = {"username":username,
                   "TLS":{}}
    if check_user(new_account["username"]):
        click.echo(f"User {username} already exist, try with another name")
    else:
        add_user(new_account)
        click.echo(f"Account created and added to file")

@click.command(short_help = "Changes the passw of the user.")
@click.argument('username',required = True)
@click.argument('newusername',required = True)
def chgusr(username,newusername):
    if not newusername.split() or not username.split():
        click.echo("The new username cannot be empty, ")
    if check_user(username):
        click.echo(f"Username changed from {username} to {newusername}")
        username_chg(username,newusername)
    


