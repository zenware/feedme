"""CLI Assistant for finding some food to eat."""
import click

from . import __version__, restaurant_chooser


@click.command()
@click.version_option(version=__version__)
@click.argument(
    "restaurant_file",
    type=click.Path(exists=True, readable=True),
    nargs=1,
    default="~/restaurants.txt",
    metavar="RESTAURANTS_FILE",
)
def main(restaurant_file: str) -> None:
    """Entrypoint to the logic that helps decide where you're eating.

    Args:
        restaurant_file: A textfile containing newline separated restaurants.
    """
    restaurants = restaurant_chooser.read_restaurant_text_file(my_file=restaurant_file)
    click.secho(restaurant_chooser.choose_random_restaurant(restaurants), fg="green")
