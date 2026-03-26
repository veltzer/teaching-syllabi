#!/usr/bin/env python

"""
Script to check the correctness of a course syllabus written in .md format
"""

import sys
from typing import List

REQUIRED = [
    "Credits",
    "Description",
    "Tags",
    "Duration",
    "Intended Audience",
    "Prerequisites",
    "Objectives",
    "Exercises",
    "Outline",
    "References",
    "We will not cover",
    "Installations",
    "Notes",
    "Links",
    "Textbooks and Resources",
]
MUST = [
    "Description",
    "Duration",
    # "Prerequisites",
    # "Objectives",
    "Outline",
]

def is_sublist(list1: List[str], list2: List[str]) -> bool:
    """
    Check that one list is a sublist of the other
    """
    pos2 = 0
    pos1 = 0
    while pos2<len(list2) and pos1<len(list1):
        if list2[pos2] == list1[pos1]:
            pos1+=1
        pos2+=1
    return pos1 == len(list1)

def check_file(filename: str) -> List[str]:
    """Check a single file and return a list of error messages (empty if OK)."""
    errors = []
    headers = []
    title = None
    with open(filename, "r", encoding="utf-8") as stream:
        for line in stream:
            line = line.rstrip()
            if line.startswith("## "):
                headers.append(line[3:])
            if line.startswith("# "):
                if title is None:
                    title = line[2:]
                else:
                    errors.append(f"{filename}: two titles in one file")
                    return errors
    if title is None:
        errors.append(f"{filename}: have no title")
        return errors
    if not is_sublist(headers, REQUIRED):
        errors.append(f"{filename}: headers not a sublist of required")
        errors.append(f"  found:    {headers}")
        errors.append(f"  required: {REQUIRED}")
    missing = [h for h in MUST if h not in headers]
    if missing:
        errors.append(f"{filename}: missing required headers: {missing}")
    return errors


def main():
    """ main entry point """
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} [filename ...]", file=sys.stderr)
        sys.exit(1)
    failed = False
    for filename in sys.argv[1:]:
        errors = check_file(filename)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            failed = True
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
