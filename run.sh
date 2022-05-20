#!/bin/sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt

export FLASK_APP=main.py
flask run -h 0.0.0.0