#!/bin/bash

echo Creating virtual environment using requirements.txt...

source ./requirements/modules.sh
python -m venv .env
source .env/bin/activate
pip install -r ./requirements/pip.txt
deactivate
module purge

echo Script finished.

