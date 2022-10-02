# Overview

A simple Flask app based on the standard Flask tutorial at https://flask.palletsprojects.com/en/2.2.x/

# Install the Project

`pip install -e .`

# Dev Setup

Install python

Setup a venv

`pip install -r requirements.txt`

`flask --app flaskr init-db`

## Run (local debug)

`flask --app flaskr --debug run`

# Tests

`pytest`

`coverage run -m pytest`

`coverage report`

# Deploy

`python setup.py bdist_wheel`

Then copy `dist/flaskr-1.0.0-py3-none-any.whl` to another machine

On other machine:

`pip install flaskr-1.0.0-py3-none-any.whl`

`flask --app flaskr init-db`

In instance folder (`venv/var/flaskr-instance`), create config.py with 

`SECRET_KEY = 'some_random_string'`

`pip install waitress`

`waitress-serve --call 'flaskr:create_app'`
