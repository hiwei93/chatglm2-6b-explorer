#!/usr/bin/env bash

set -x

mypy src/
black --check src/
isort --check-only src/
flake8 --max-line-length=88 --exclude=__init__.py