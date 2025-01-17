FROM python:3.10-slim-bookworm AS setup
RUN apt-get update -y && apt-get install git -y

WORKDIR /myapp/
RUN \
    python -m venv --upgrade-deps .venv \
    && .venv/bin/python -m pip install 'poetry==2.0.1' \
    && .venv/bin/python -m pip install 'git+https://github.com/robsdedude/virtualenv.git@fix/py-info-cache-versioning'

COPY pyproject.toml poetry.lock poetry.toml ./
COPY src src
RUN .venv/bin/poetry install -vv
