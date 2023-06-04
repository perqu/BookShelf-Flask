# Zmienne
PYTHON = python
PIP = pip
PROJECT_NAME = Bookshelf - Flask

# Cele
.PHONY: install run test lint format

install:
	$(PIP) install --upgrade $(PIP) &&\
		$(PIP) install -r requirements.txt

migrate:
	flask db migrate -m "Initial migration."
	flask db upgrade

run:
	$(PYTHON) app.py

test:
	pytest

lint:
	pylint *.py --exit-zero

format:
	black *.py

all: lint format install test
