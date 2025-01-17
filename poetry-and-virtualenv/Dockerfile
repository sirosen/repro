FROM python:3.10-slim-bookworm AS setup

WORKDIR /myapp/
RUN \
    python -m venv --upgrade-deps .venv \
    && .venv/bin/python -m pip install 'poetry==2.0.1' \
    && .venv/bin/python -m pip install 'virtualenv==20.29.1'

COPY pyproject.toml poetry.lock poetry.toml ./
COPY src src
RUN .venv/bin/poetry install -vv
