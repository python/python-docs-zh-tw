#!/bin/sh
# Translation memory lookup over this repo's .po files (see translation_memory/main.py).
exec python3 "$(dirname "$0")/translation_memory/main.py" "$@"
