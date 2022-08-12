# Checkout Code Kata

This comes from the content from the following udemy course: https://www.udemy.com/course/unit-testing-and-tdd-in-python/

## Setup & Run Tests

* Install pipenv if you haven't already
* Clone the repo
* `export PIPENV_VENV_IN_PROJECT=true` to setup a virtual environment in the directory where you've cloned the repo
* `pipenv install --dev`
* `source .venv/bin/activate`
* `pytest -v --cov=checkout`
