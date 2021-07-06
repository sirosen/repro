#!/bin/bash

rm -rf ~/.cache/jsonschema_validate/
if [ ! -d venv ]; then
  python -m venv venv
fi
. venv/bin/activate
pip install -e ~/projects/check-jsonschema
# pip install check-jsonschema
for x in {1..10}; do
  check-jsonschema \
    --schemafile "https://json.schemastore.org/github-workflow" \
    "wf$x.yaml" &
done
