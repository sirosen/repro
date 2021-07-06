#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

mypy --warn-unreachable platform_check.py
