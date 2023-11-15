#!/bin/sh

WORK_DIR=.scripts
cd $WORK_DIR

source utils/install_poetry.sh

poetry lock
poetry install
poetry run bash -c "
    python mark_file/main.py

"
