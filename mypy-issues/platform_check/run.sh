#!/bin/bash
set -e
cd "$(dirname "$0")"

echo "do ok file"
mypy --warn-unreachable ok.py
echo "done"
echo "do failing file"
mypy --warn-unreachable fail.py
echo "done"
