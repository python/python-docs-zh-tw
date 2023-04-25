#!/bin/sh
cd .scripts
source utils/install_poetry.sh

# check if OpenCC is installed
if [[ ! -x "`which opencc 2>/dev/null`" ]]
then
    echo "You do not have OpenCC installed. Please install it first."
    echo "Instruction: https://github.com/BYVoid/OpenCC/wiki/Download"
    exit 1
fi

# clone pydoc zh_CN repo and pull from remote
CN_REPO=.python-docs-zh-cn
if [[ ! -d $CN_REPO ]]
then
    read -p "You do not have a clone of zh_CN repo. Clone now? (y/N)" choice
    case "$choice" in 
        y|Y ) git clone --depth 1 --no-single-branch https://github.com/python/python-docs-zh-cn $CN_REPO ;;
        n|N|* ) echo "Aborted"; exit 1 ;;
    esac
fi
git -C $CN_REPO checkout 3.10  # the current latest version of CN repo
git -C $CN_REPO pull


# convert zh_CN po content and merge into zh_TW po
TARGET=$1
CN_PATH=$CN_REPO/$TARGET
TW_PATH=../$TARGET

poetry lock
poetry install
poetry run bash -c "
    opencc -i $CN_PATH -c s2twp.json -o /tmp/tmp.po
    pofilter --nonotes --excludefilter unchanged --excludefilter untranslated /tmp/tmp.po | msgattrib --set-fuzzy -o /tmp/tmp.po
    pomerge -t $CN_PATH -i /tmp/tmp.po -o /tmp/tmp.po

    pofilter --nonotes --excludefilter untranslated $TW_PATH /tmp/tmp2.po
    pomerge -t /tmp/tmp.po -i /tmp/tmp2.po -o /tmp/tmp3.po
    msgcat --lang zh_TW /tmp/tmp3.po -o $TW_PATH
"

rm /tmp/tmp.po /tmp/tmp2.po /tmp/tmp3.po
