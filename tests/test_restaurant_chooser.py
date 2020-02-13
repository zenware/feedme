"""Test cases for restaurant_chooser module."""
import pytest
from pytest_mock import MockFixture

from feedme import restaurant_chooser


@pytest.fixture
def random_mock(mocker: MockFixture):
    """Mock randint."""
    return mocker.patch("random.randint")


def test_read_existing_restaurant_text_file() -> None:
    """Test reading a text file into a list."""
    # How do I make this think that file exists?
    restaurants = restaurant_chooser.read_restaurant_text_file(
        "tests/test-restaurants.txt"
    )
    assert "The Bread Co.\n" in restaurants


def test_fails_on_nonexistent_file() -> None:
    """Program should fail with FileNotFound when a file doesn't exist."""
    BOGUS_FILENAME = "Bogus File"

    with pytest.raises(FileNotFoundError) as exc_info:
        restaurant_chooser.read_restaurant_text_file(BOGUS_FILENAME)

    assert "No such file" in exc_info.value.args[1]


def test_choose_random_restaurant(random_mock: MockFixture) -> None:
    """Test randomly choosing a restaurant has expected output."""
    random_mock.return_value = 2
    SAMPLE_RESTAURANT_LIST = ["The Bread Co.", "Brunch Street", "Supper Club"]
    assert (
        restaurant_chooser.choose_random_restaurant(SAMPLE_RESTAURANT_LIST)
        == "Supper Club"
    )


def test_random_gets_used(random_mock: MockFixture) -> None:
    """Test randomly choosing a restaurant has expected output."""
    SAMPLE_RESTAURANT_LIST = ["The Bread Co.", "Brunch Street", "Supper Club"]
    restaurant_chooser.choose_random_restaurant(SAMPLE_RESTAURANT_LIST)
    assert random_mock.called
