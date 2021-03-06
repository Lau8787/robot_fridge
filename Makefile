SHELL = /bin/bash
VENV = source .venv/bin/activate;

PY_FILES = $(wildcard *.py)

.PHONY: install
install: .venv
	python3 -m pip install -r requirements.txt

.venv:
	python3 -m venv .venv

.PHONY: check
check: pytest mypy black

.PHONY: pytest
pytest:
	$(VENV) $(PYTEST_FLAGS) pytest

.PHONY: mypy
mypy:
	$(VENV) mypy $(PY_FILES)

.PHONY: black
black:
	$(VENV) black --check $(PY_FILES)

.PHONY: format
format:
	$(VENV) black $(PY_FILES)
