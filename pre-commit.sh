#!/usr/bin/env bash

STAGEDFILES=($(git diff --cached --name-only -- '*.po' --diff-filter=ACM))
echo "po files: ${STAGEDFILES[@]}"

NEED_FORMAT_FILES=0

# set the error msg color
RED='\033[0;31m'
NC='\033[0m' # No Color

if [ ${#STAGEDFILES[@]} -gt 0 ]; then
    for FILE in "${STAGEDFILES[@]}"; do
        powrap --check --quiet "$FILE"
        RETURN_CODE=$?
        if [ $RETURN_CODE -eq 1 ]; then
            powrap "$FILE"
            NEED_FORMAT_FILES=1
        fi
    done

    if [ $NEED_FORMAT_FILES -eq 1 ]; then
        echo -e "${RED}Failed to commit, please add the formatted po file(s) and commit again.${NC}"
        exit 1
    fi
else
    echo "There's no staged po files to format."
fi

exit 0
