#!/bin/sh -eu

isort ./webapp
black ./webapp
terraform fmt -recursive ./infrastructure
