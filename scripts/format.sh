#!/usr/bin/env bash

set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src/ --exclude=__init__.py
black src/
isort src/
