#!/usr/bin/env python

"""
Check that the union of all word-list files equals exactly the set of
backticked terms found in the syllabi markdown files.
Exit code 0 if in sync, 1 if mismatches found.
"""

import os
import re
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
WORD_LISTS_DIR = os.path.join(PROJECT_ROOT, "word-lists")
SYLLABI_DIR = os.path.join(PROJECT_ROOT, "syllabi")

BACKTICK_RE = re.compile(r"`([^`]+)`")


def collect_word_list_terms():
    terms = set()
    for filename in os.listdir(WORD_LISTS_DIR):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(WORD_LISTS_DIR, filename)
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                term = line.rstrip("\n")
                if term:
                    terms.add(term)
    return terms


def collect_syllabi_terms():
    terms = set()
    for dirpath, _, filenames in os.walk(SYLLABI_DIR):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            for match in BACKTICK_RE.finditer(content):
                terms.add(match.group(1))
    return terms


def main():
    word_list_terms = collect_word_list_terms()
    syllabi_terms = collect_syllabi_terms()

    only_in_lists = word_list_terms - syllabi_terms
    only_in_syllabi = syllabi_terms - word_list_terms

    if not only_in_lists and not only_in_syllabi:
        print(
            f"OK: {len(syllabi_terms)} terms in sync between "
            f"word-lists and syllabi."
        )
        return 0

    print("FAIL: word-lists and syllabi backticked terms are out of sync.")
    if only_in_lists:
        print(f"\n  {len(only_in_lists)} term(s) in word-lists but NOT backticked in any syllabus:")
        for term in sorted(only_in_lists):
            print(f"    {term}")
    if only_in_syllabi:
        print(f"\n  {len(only_in_syllabi)} term(s) backticked in syllabi but NOT in any word-list:")
        for term in sorted(only_in_syllabi):
            print(f"    {term}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
