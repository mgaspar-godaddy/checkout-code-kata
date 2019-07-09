# Checkout Code Kata

## Setup & Run Tests

* Install pipenv if you haven't already
* Clone the repo
* `export PIPENV_VENV_IN_PROJECT=true` to setup a virtual environment in the directory where you've cloned the repo
* `pipenv install --dev --python 3`
* `source .venv/bin/activate`
* `pytest -v --cov=checkout`