#!/bin/sh -e

set -x

isort pydoppler pydoppler-stubs tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pydoppler pydoppler-stubs tests --exclude=__init__.py
black pydoppler pydoppler-stubs tests
isort pydoppler pydoppler-stubs tests
