#!/bin/sh

set -e

rm -rf dist
python -m build
python -m twine upload --repository testpypi dist/*