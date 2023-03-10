#!/bin/sh -eu

VENV_PATH=./.venv

pip3 install virtualenv
virtualenv -p python3 $VENV_PATH
source $VENV_PATH/bin/activate
pip3 install -r requirements.txt
