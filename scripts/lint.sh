#!/usr/bin/env bash

set -e
set -x

flake8 pydoppler pydoppler-stubs tests
black pydoppler pydoppler-stubs tests --check
isort pydoppler pydoppler-stubs tests --check-only