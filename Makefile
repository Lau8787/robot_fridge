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
	$(VENV) flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	$(VENV) flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

.PHONY: black
black:
	$(VENV) black --check $(PY_FILES)

.PHONY: format
format:
	$(VENV) black $(PY_FILES)
