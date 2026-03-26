#!/usr/bin/env python

"""
Check that no term appears in more than one word-list file.
Exit code 0 if no duplicates, 1 if duplicates found.
"""

import os
import sys
from collections import defaultdict

WORD_LISTS_DIR = os.path.join(os.path.dirname(__file__), "..", "word-lists")


def main():
    term_to_files = defaultdict(list)
    for filename in sorted(os.listdir(WORD_LISTS_DIR)):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(WORD_LISTS_DIR, filename)
        with open(filepath, encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                term = line.rstrip("\n")
                if term:
                    term_to_files[term].append(f"{filename}:{line_num}")

    duplicates = {
        term: files for term, files in term_to_files.items() if len(files) > 1
    }

    if duplicates:
        print(f"FAIL: {len(duplicates)} duplicate(s) found across word-list files:")
        for term, files in sorted(duplicates.items()):
            print(f"  '{term}' appears in: {', '.join(files)}")
        return 1

    total = len(term_to_files)
    file_count = len(
        [f for f in os.listdir(WORD_LISTS_DIR) if f.endswith(".txt")]
    )
    print(f"OK: {total} terms across {file_count} files, no duplicates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
