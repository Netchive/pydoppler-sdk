#!/usr/bin/env bash

set -e
set -x

flake8 pydoppler tests
black pydoppler tests --check
isort pydoppler tests --check-only