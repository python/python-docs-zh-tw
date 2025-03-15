"""
A utility script to extract message IDs from PO files.

This script extracts a specific message ID from a PO file based on the file name
and occurrence number. It's useful for retrieving translation strings for
specific occurrences in the Python documentation.

Usage:
    python intercept.py path/to/file.po [-n OCCURRENCE_NUMBER]

Arguments:
    path: Path to a PO file
    -n, --occurrence_number: The occurrence number to match (default: 1)
"""
import argparse
from pathlib import Path

import polib


def get_pofile_from_path(path: Path) -> polib.POFile:
    if not path.exists():
        raise ValueError(f"The path '{path.absolute()}' does not exist!")

    if not (path.is_file() and path.suffix == ".po"):
        raise ValueError(f"{path} doesn't seem to be a .po file")

    try:
        pofile = polib.pofile(path)
    except OSError:
        raise ValueError(f"{path} doesn't seem to be a .po file")
    return pofile


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Extract message IDs from PO files"
    )
    parser.add_argument("path", type=Path,
                        help="the path of a PO file")
    parser.add_argument("-n", '--occurrence_number',
                        type=int, default=1, help="the occurrence number to match")
    args = parser.parse_args()
    path = args.path.resolve()
    pofile = get_pofile_from_path(path)
    occurrence_number = args.occurrence_number

    for entry in pofile:
        if not any(path.stem in p and int(n) == occurrence_number for p, n in entry.occurrences):
            continue
        print(entry.msgid)
        break
