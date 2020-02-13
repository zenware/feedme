"""feedme restaurant_chooser module.

This module is responsible for the logic that decides what restaurant you're
going to eat at.
"""
import random
from typing import List


def read_restaurant_text_file(my_file: str) -> List[str]:
    """Read a text file containing 1 restaurant name per line.

    Args:
        my_file: OS File Path.

    Returns:
        A List[str] of restaurants.
    """
    with open(my_file) as f:
        restaurants = f.readlines()  # Missing coverage
    return restaurants  # Missing coverage


def choose_random_restaurant(restaurants: List[str]) -> str:
    """Choose a random restaurant from a List[str] of restaurants.

    It's done the way it is because it's more testable than using
    random.choice, the noqa comment in the code disables the flake8 check for
    builtin psuedo-random number generators being used for crypto.

    Args:
        restaurants: List[str] of restaurants to choose from.

    Returns:
        The randomly chosen restaurant.

    Example:
        >>> from feedme import restaurant_chooser
        >>> rlist = ["Restaurant 1", "Restaurant 2", "Restaurant 3"]
        >>> restaurant_chooser.choose_random_restaurant(restaurants) in rlist
        True
    """
    return restaurants[random.randint(0, (len(restaurants) - 1))]  # noqa: S311
