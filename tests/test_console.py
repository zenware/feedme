"""Test cases for console module."""
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture

from feedme import console


TEST_RESTAURANT_FILENAME = "tests/test-restaurants.txt"


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for providing click.testing.CliRunner."""
    return CliRunner()


def test_main_succeeds_with_help(runner: CliRunner) -> None:
    """It returns exit code when Called with --help."""
    result = runner.invoke(console.main, ["--help"])
    assert result.exit_code == 0


def test_main_prints_usage_when_called_with_no_arguments(runner: CliRunner) -> None:
    """Test that the CLI prints usage information when called with no args."""
    result = runner.invoke(console.main)
    assert "Usage" in result.output


def test_main_uses_specified_file(runner: CliRunner, mocker: MockFixture) -> None:
    """Test that the specified file gets handed off to the read_file function."""
    mock_read_file = mocker.patch(
        "feedme.console.restaurant_chooser.read_restaurant_text_file"
    )

    runner.invoke(console.main, [TEST_RESTAURANT_FILENAME])
    mock_read_file.assert_called_with(my_file=TEST_RESTAURANT_FILENAME)


def test_main_prints_restaurant_on_success(
    runner: CliRunner, mocker: MockFixture
) -> None:
    """Test that a restaurant actually gets spit out on a successful run."""
    TEST_RESTAURANT = "My Favorite Restaurant"

    mock_random_restaurant = mocker.patch(
        "feedme.console.restaurant_chooser.choose_random_restaurant"
    )
    mock_random_restaurant.side_effect = [TEST_RESTAURANT]

    result = runner.invoke(console.main, [TEST_RESTAURANT_FILENAME])
    assert TEST_RESTAURANT in result.output


def test_main_prints_error_on_file_not_found(runner: CliRunner) -> None:
    """Test main prints error when the file doesn't exist."""
    result = runner.invoke(console.main, ["/file_does_not_exist/ajlkjsdf"])
    assert "Error" in result.output
