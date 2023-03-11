#!/bin/sh -eu

cd webapp
isort . --settings-path=./pyproject.toml
black .

cd ../infrastructure
terraform fmt -recursive
