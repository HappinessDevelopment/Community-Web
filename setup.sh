#!/bin/bash

alias python='python3'

echo "Pip installing virtual env..."
pip install virtualenv
# create clean virtual environment
python -m venv .venv

# activate the environment
echo "Created a virtual env and now activating."
source .venv/bin/activate

# install pip
echo "Installing pip for venv..."
easy_install pip

# install from requirements.txt (currently only django and djangorestframework)
echo "Installing requirements..."
pip install -r requirements.txt
 

