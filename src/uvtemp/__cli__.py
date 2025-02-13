"""Command line interface for uvtemp"""

# Importing the libraries

import click

from uvtemp._version import __version__


@click.command()
@click.version_option(__version__)
@click.option("--count", "-c", default=1, help="Number of greetings.")
@click.option("--name", "-n", prompt="Your name", help="The person to greet.")
def main(count: int, name: str) -> None:
    """
    This is the cli function of the package.
    You can use this function to print a message to the user.

    Args:
        count: The number of items to print
        name: The name of the package that will be printed
    """
    # Print a message to the user.
    for _ in range(count):
        click.echo(f"Hello, {name}!")
        click.echo(f"This is uvtemp version {__version__}.")


# main function for the main module
if __name__ == "__main__":
    main()
