#!/bin/bash
set -e
cd "$(dirname "$0")"

echo "do ok file"
mypy --warn-unreachable platform_check_ok.py
echo "done"
echo "do failing file"
mypy --warn-unreachable platform_check.py
echo "done"
