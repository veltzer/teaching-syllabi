#!/usr/bin/env python

"""
Script to check the correctness of a course syllabus written in .md format
"""

import re
import sys
from typing import List, Optional, Tuple

REQUIRED = [
    "Description",
    "Tags",
    "Duration",
    "Intended Audience",
    "Prerequisites",
    "Required Knowledge",
    "Objectives",
    "Exercises",
    "Outline",
    "References",
    "We will not cover",
    "Installations",
    "Notes",
    "Links",
    "Textbooks and Resources",
    "Copyright",
]
MUST = [
    "Description",
    "Duration",
    "Intended Audience",
    "Prerequisites",
    # "Required Knowledge",
    "Objectives",
    "Outline",
    "Copyright",
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
    lines: List[str] = []
    with open(filename, "r", encoding="utf-8") as stream:
        for line in stream:
            lines.append(line.rstrip())
            if line.rstrip().startswith("## "):
                headers.append(line.rstrip()[3:])
            if line.rstrip().startswith("# "):
                if title is None:
                    title = line.rstrip()[2:]
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
    errors.extend(check_course_id(filename, lines))
    errors.extend(check_chapter_ids(filename, lines))
    return errors


def check_course_id(filename: str, lines: List[str]) -> List[str]:
    """Check that the file has exactly one <!-- course: id --> comment."""
    errors = []
    course_ids = [
        line for line in lines
        if re.match(r"^\s*<!--\s*course:\s*[\w_+]+\s*-->", line)
    ]
    if len(course_ids) == 0:
        errors.append(f"{filename}: missing course id (<!-- course: id -->)")
    elif len(course_ids) > 1:
        errors.append(f"{filename}: multiple course ids found")
    return errors


CHAPTER_WITH_DURATION_RE = re.compile(
    r"^\s*<!--\s*chapter:\s*([\w+-]+)\s*,\s*duration:\s*(\d+)h\s*-->"
)
CHAPTER_WITHOUT_DURATION_RE = re.compile(
    r"^\s*<!--\s*chapter:\s*([\w+-]+)\s*-->"
)


def extract_duration_hours(lines: List[str]) -> Optional[int]:
    """Extract duration_hours from YAML frontmatter."""
    in_frontmatter = False
    for line in lines:
        if line == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            break
        if in_frontmatter:
            match = re.match(r"^duration_hours:\s*(\d+)", line)
            if match:
                return int(match.group(1))
    return None


def parse_chapter_comment(line: str) -> Optional[Tuple[str, Optional[int]]]:
    """Parse a chapter comment, returning (id, duration_or_None)."""
    match = CHAPTER_WITH_DURATION_RE.match(line)
    if match:
        return (match.group(1), int(match.group(2)))
    match = CHAPTER_WITHOUT_DURATION_RE.match(line)
    if match:
        return (match.group(1), None)
    return None


def check_chapter_ids(filename: str, lines: List[str]) -> List[str]:
    """Check chapter ids, durations, and that durations sum to total."""
    errors = []
    in_outline = False
    past_outline = False
    prev_was_chapter = False
    seen_ids: List[str] = []
    chapter_durations: List[Tuple[str, Optional[int]]] = []

    for line in lines:
        if line == "## Outline":
            in_outline = True
            continue
        if in_outline and line.startswith("## "):
            past_outline = True
            in_outline = False
            continue
        if not in_outline or past_outline:
            prev_was_chapter = False
            continue

        parsed = parse_chapter_comment(line)
        if parsed is not None:
            ch_id, duration = parsed
            if ch_id in seen_ids:
                errors.append(f"{filename}: duplicate chapter id: {ch_id}")
            seen_ids.append(ch_id)
            chapter_durations.append((ch_id, duration))
            prev_was_chapter = True
            continue

        if re.match(r"^\*\s+", line):
            if not prev_was_chapter:
                errors.append(
                    f"{filename}: top-level outline bullet without chapter id: {line.strip()}"
                )
            prev_was_chapter = False
            continue

        # Sub-bullets, empty lines, etc.
        prev_was_chapter = False

    # Check duration consistency
    if chapter_durations:
        missing_duration = [ch_id for ch_id, d in chapter_durations if d is None]

        if missing_duration:
            errors.append(
                f"{filename}: chapters missing duration: {missing_duration}"
            )
        else:
            total_chapter_hours = sum(
                d for _, d in chapter_durations if d is not None
            )
            course_hours = extract_duration_hours(lines)
            if course_hours is not None and total_chapter_hours != course_hours:
                errors.append(
                    f"{filename}: chapter durations sum to {total_chapter_hours}h "
                    f"but course duration_hours is {course_hours}h"
                )

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
