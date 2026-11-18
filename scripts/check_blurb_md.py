#!/usr/bin/env python

"""
Check the correctness of a short-lecture blurb written in .md format.

A blurb is not a syllabus: it is a one-page marketing description of a short
talk. Its agenda states each topic's length visibly, in minutes, and those
lengths must add up to duration_minutes in the frontmatter. The format is
described in doc/HowToWriteBlurb.txt.
"""

import re
import sys
from pathlib import Path

MUST = [
    "The Challenge",
    "What This Session Covers",
    "Agenda",
    "Takeaways",
    "Who Should Attend",
    "Speaker",
]
OPTIONAL = {
    # optional header -> the header it must directly follow
    "Continue the Journey": "Who Should Attend",
}

BLURB_ID_RE = re.compile(r"^<!--\s*blurb:\s*([\w+]+)\s*-->$")
DURATION_RE = re.compile(r"^duration_minutes:\s*(\d+)\s*$")
AGENDA_ITEM_RE = re.compile(r"^\* \*\*(.+?)\*\* \((\d+) min\): (\S.*)$")


def split_frontmatter(filename: str, lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    """Return (frontmatter lines, body lines, errors)."""
    if not lines or lines[0] != "---":
        return [], lines, [f"{filename}: missing YAML frontmatter"]
    for i in range(1, len(lines)):
        if lines[i] == "---":
            return lines[1:i], lines[i + 1:], []
    return [], lines, [f"{filename}: unterminated YAML frontmatter"]


def extract_duration(filename: str, frontmatter: list[str]) -> tuple[int | None, list[str]]:
    """Return duration_minutes from the frontmatter."""
    found = [m for m in (DURATION_RE.match(line) for line in frontmatter) if m]
    if len(found) != 1:
        return None, [f"{filename}: frontmatter must have exactly one integer duration_minutes"]
    minutes = int(found[0].group(1))
    if minutes <= 0:
        return None, [f"{filename}: duration_minutes must be positive"]
    return minutes, []


def check_headers(filename: str, headers: list[str]) -> list[str]:
    """Check the second-level headers: all required, in order, nothing else."""
    expected: list[str] = []
    for header in MUST:
        expected.append(header)
        for optional, after in OPTIONAL.items():
            if after == header and optional in headers:
                expected.append(optional)
    if headers != expected:
        return [
            f"{filename}: headers do not match the blurb format",
            f"  found:    {headers}",
            f"  expected: {expected}",
        ]
    return []


def check_agenda(filename: str, body: list[str], duration: int | None) -> list[str]:
    """Every agenda line is a timed topic; topic times sum to duration_minutes."""
    errors = []
    start = body.index("## Agenda") + 1
    total = 0
    count = 0
    for line in body[start:]:
        if line.startswith("## "):
            break
        if line == "":
            continue
        match = AGENDA_ITEM_RE.match(line)
        if match is None:
            errors.append(
                f"{filename}: agenda line is not '* **Topic** (N min): Focus': {line}"
            )
            continue
        minutes = int(match.group(2))
        if minutes <= 0:
            errors.append(f"{filename}: agenda topic with non-positive length: {line}")
        total += minutes
        count += 1
    if count == 0:
        errors.append(f"{filename}: agenda has no topics")
    elif duration is not None and total != duration:
        errors.append(
            f"{filename}: agenda topics sum to {total} min "
            f"but duration_minutes is {duration}"
        )
    return errors


def check_file(filename: str) -> list[str]:
    """Check a single blurb and return a list of error messages (empty if OK)."""
    with open(filename, encoding="utf-8") as stream:
        lines = [line.rstrip("\n") for line in stream]
    frontmatter, body, errors = split_frontmatter(filename, lines)
    if errors:
        return errors
    duration, errors = extract_duration(filename, frontmatter)

    titles = [line for line in body if line.startswith("# ")]
    if len(titles) != 1:
        errors.append(f"{filename}: must have exactly one title, found {len(titles)}")

    ids = [m.group(1) for m in (BLURB_ID_RE.match(line) for line in body) if m]
    stem = Path(filename).stem
    if len(ids) != 1:
        errors.append(f"{filename}: must have exactly one <!-- blurb: id --> comment")
    elif ids[0] != stem:
        errors.append(f"{filename}: blurb id '{ids[0]}' does not match file name '{stem}'")

    for line in body:
        if re.match(r"^\s*<!--\s*(course|chapter):", line):
            errors.append(f"{filename}: syllabus marker in a blurb: {line}")
        if line.startswith("### "):
            errors.append(f"{filename}: blurbs have no third-level headers: {line}")
        if re.match(r"^\s+\*", line):
            errors.append(f"{filename}: blurbs have no nested bullets: {line}")

    headers = [line[3:] for line in body if line.startswith("## ")]
    header_errors = check_headers(filename, headers)
    errors.extend(header_errors)
    if not header_errors:
        errors.extend(check_agenda(filename, body, duration))
    return errors


def main():
    """ main entry point """
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} [filename ...]", file=sys.stderr)
        sys.exit(1)
    errors = []
    for filename in sys.argv[1:]:
        errors.extend(check_file(filename))
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
