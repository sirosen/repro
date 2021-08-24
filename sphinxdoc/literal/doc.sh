#!/bin/bash
set -e

cd "$(dirname "$0")/docs"
sphinx-build . _build -n -W
