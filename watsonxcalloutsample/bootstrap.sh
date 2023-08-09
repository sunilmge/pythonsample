#!/bin/sh

export FLASK_APP=./application.py
pipenv run flask run -h 0.0.0.0

