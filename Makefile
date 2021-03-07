SHELL = /bin/bash
VENV = source .venv/bin/activate;

PY_FILES = $(wildcard *.py)

.PHONY: install
install: .venv
	$(VENV) python3 -m pip install -r requirements.txt

.venv:
	python3 -m venv .venv

.PHONY: check
check: pytest mypy black

.PHONY: pytest
pytest:
	$(VENV) $(PYTEST_FLAGS) pytest

.PHONY: mypy
mypy:
	$(VENV) mypy --follow-imports silent $(PY_FILES)

.PHONY: flake8
flake8:
	# stop the build if there are Python syntax errors or undefined names
	$(VENV) flake8 . --count --show-source --statistics

.PHONY: black
black:
	$(VENV) black --check $(PY_FILES)

.PHONY: format
format:
	$(VENV) black $(PY_FILES)
