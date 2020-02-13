# [feedme](https://github.com/zenware/feedme)

This is a weekend project to make a CLI tool that can help you figure out where to get lunch.
Currently it's a command line tool that prints a random restaurant from a text-file list of restaurants.
I made it because sometimes I can be indecisive.

This project is currently under development with no stable releases.

## Usage

Ask where to eat
```
$ feedme ~/restaurants.txt
Your Favorite Restaurant
$
```
## Prerequisites

* Git
* Python 3

## Installing feedme

Currently you can install the project like this:
```
$ git clone https://github.com/zenware/feedme.git && cd feedme
$ poetry install
```

When versioned releases exist the above will be removed and you can pip install:
```
$ pip install feedme
```

## Development / Contributing to feedme

To contribute to feedme, follow these steps:
1. Fork this repository
1. Create a branch: `git checkout -b <branch_name>`
1. Make your changes and commit them: `git commit -m <commit_message>`
1. Push to the original branch: `git push origin <project_name>/<location>
1. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request.](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-requesth)

Working on this project will be easier if you have the following tools.

Before copying and pasting the following commands into your terminal I
recommend taking a moment to read more about them and in fact read the scripts
before they execute on your computer.

### Prerequisites
* [pyenv](https://github.com/pyenv/pyenv) can be installed by `curl https://pyenv.run | bash`
* [poetry](https://python-poetry.org/) can be installed by `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

### Useful
* [pre-commit](https://pre-commit.com/) can be installed by `pip install --user --upgrade pre-commit`

The best way to get the project set up is:
```
$ git clone https://github.com/zenware/feedme.git && cd feedme
$ precommit
```

### Testing
Testing is performed with a combination of Pytest and nox.

To run the test suite use the command `poetry run pytest --cov`.

### Steps to take pre-commit
If you haven't installed and setup [pre-commit](https://pre-commit.com/) on this
repo and perhaps even if you have, it's a good idea to run some more comprehensive
testing before committing your code.

The CI/CD will run the full-gamut of configured nox sessions with the command `nox`.
You can replicate that yourself either with `nox` or `poetry run nox`

## License
This project uses the following license: [MIT](LICENSE)

That means that anyone is free to do anything they want with it, including sell it. 
If anyone *succeeds* in selling this software please contact me I almost certainly have a job opportunity for you if you're interested.