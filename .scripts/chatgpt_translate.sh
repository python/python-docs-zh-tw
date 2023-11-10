#!/bin/sh

WORK_DIR=.scripts
cd $WORK_DIR

source utils/install_poetry.sh

TEMP=tmp.po
TARGET=../$2

poetry lock
poetry install
poetry run bash -c "
    python google_translate/main.py $2 $TARGET $3 > $TEMP
    pomerge -t $TARGET -i $TEMP -o $TARGET
"
rm $TEMP
