#!/bin/sh -e

set -x

isort pydoppler tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pydoppler tests --exclude=__init__.py
black pydoppler tests
isort pydoppler tests
