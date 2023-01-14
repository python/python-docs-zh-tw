#!/bin/sh

WORK_DIR=.scripts
cd $WORK_DIR

source utils/install_poetry.sh

TEMP=tmp.po
TARGET=../$1

poetry install -q
poetry run bash -c "
    python google_translate/main.py $TARGET > $TEMP
    pomerge -t $TARGET -i $TEMP -o $TARGET
"
rm $TEMP
