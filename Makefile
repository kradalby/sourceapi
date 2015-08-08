ENV=./env/bin
SHELL := /bin/bash
PYTHON=$(ENV)/python
PIP=$(ENV)/pip
SETUP=$(PYTHON) setup.py

dev: 
	$(PIP) install -r requirements/development.txt --upgrade

prod:
	$(PIP) install -r requirements/production.txt --upgrade

env:
	virtualenv -p `which python3` env

clean:
	pyclean .
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info

test:
	$(SETUP) test

run:
	$(PYTHON) app.py

freeze:
	mkdir -p requirements
	$(PIP) freeze > requirements/base.txt
