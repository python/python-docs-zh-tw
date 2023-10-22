import argparse
import logging
from pathlib import Path
from typing import List

import polib
from googletrans import Translator

from utils import refine_translations


def _get_po_paths(path: Path) -> List[Path]:
    """Find all .po files in given path"""
    if not path.exists():
        logging.error(f"The path '{path.absolute()}' does not exist!")

    # return 1-element list if it's a file
    if path.is_file():
        return [path.resolve()]

    # find all .po files
    po_paths = [p.resolve() for p in path.glob("**/*.po")]
    return po_paths


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        help="the path of a PO file or a directory containing PO files"
    )
    args = parser.parse_args()

    translator = Translator()
    po_files = _get_po_paths(Path(args.path).resolve())
    errors = []
    for path in po_files:
        try:
            pofile = polib.pofile(path)
        except OSError:
            errors.append(f"{path} doesn't seem to be a .po file")
            continue

        for entry in pofile.untranslated_entries()[::-1]:
            translation = translator.translate(entry.msgid, src='en', dest='zh-TW')

            print(
                '#, fuzzy\n'
                f'msgid "{repr(entry.msgid)[1:-1]}"\n'
                f'msgstr "{repr(refine_translations(translation.text))[1:-1]}"\n'
            )
