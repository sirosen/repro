#!/bin/bash
set -e
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  python -m venv .venv
  .venv/bin/pip install mypy typing-extensions
fi
. .venv/bin/activate

mypy no_op.py
