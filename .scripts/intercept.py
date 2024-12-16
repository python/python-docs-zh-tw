# /// script
# dependencies = [
#     "polib",
# ]
# ///
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        help="the path of a PO file",
    )
    parser.add_argument("-n", '--occurrence_number', type=int, default=1)
    args = parser.parse_args()
    path = Path(args.path).resolve()
    pofile = get_pofile_from_path(path)
    occurrence_number = args.occurrence_number

    for entry in pofile:
        if not any(path.stem in p and int(n) == occurrence_number for p, n in entry.occurrences):
            continue
        print(entry.msgid)
        break
