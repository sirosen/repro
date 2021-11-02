#!/bin/bash

if [ ! -d .venv ]; then
  virtualenv .venv
  . .venv/bin/activate
  pip install 'mypy==0.910' 'flask==2.0.2' 'werkzeug==2.0.2'
else
  . .venv/bin/activate
fi

mypy ua_parser.py
mypy minimal.py
