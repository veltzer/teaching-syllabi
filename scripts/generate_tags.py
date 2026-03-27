#!/usr/bin/env python

"""Generate .tags from tag_lists/*.txt files."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAG_LISTS_DIR = ROOT / "tag_lists"
OUTPUT = ROOT / ".tags"


def main():
    tags = []
    for f in sorted(TAG_LISTS_DIR.glob("*.txt")):
        group = f.stem
        for line in f.read_text().splitlines():
            tag = line.strip()
            if tag:
                tags.append(f"{group}:{tag}")
    tags.sort()
    OUTPUT.write_text("\n".join(tags) + "\n")
    print(f"Generated {OUTPUT} with {len(tags)} tags from {len(list(TAG_LISTS_DIR.glob('*.txt')))} group files")


if __name__ == "__main__":
    main()
