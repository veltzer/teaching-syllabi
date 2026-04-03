#!/usr/bin/env python

"""
Build track markdown files from YAML track definitions.

Usage (batch mode):
    build_tracks.py source1.yaml target1.md source2.yaml target2.md ...

Each source/target pair: reads the YAML track definition, assembles
the markdown by pulling content from referenced courses/chapters,
and writes the result to the target path.
"""

import re
import sys
from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = PROJECT_ROOT / "syllabi" / "courses"
TERMS_DIR = PROJECT_ROOT / "terms"


def _load_terms() -> list[str]:
    """Load all terms from the terms directory, sorted longest-first."""
    terms: set[str] = set()
    for tf in TERMS_DIR.glob("*.txt"):
        for line in tf.read_text(encoding="utf-8").splitlines():
            t = line.strip()
            if t:
                terms.add(t)
    return sorted(terms, key=len, reverse=True)


def _wrap_terms(text: str, terms: list[str]) -> str:
    """Wrap known terms in backticks, skipping already-wrapped occurrences."""
    for term in terms:
        pattern = r"(?<!`)(?<!\w)" + re.escape(term) + r"(?!\w)(?!`)"
        text = re.sub(pattern, f"`{term}`", text)
    return text


CHAPTER_COMMENT_RE = re.compile(
    r"\s*<!--\s*chapter:\s*([\w+-]+)\s*(?:,\s*duration:\s*(\d+)h\s*)?-->"
)


def parse_course_md(md_path: Path) -> dict[str, Any]:
    """Parse a course markdown file, extracting frontmatter and outline chapters."""
    text = md_path.read_text(encoding="utf-8")

    # Strip frontmatter
    fm_match = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    body = text[fm_match.end():] if fm_match else text

    # Extract title
    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else md_path.stem

    # Extract the Outline section
    outline_match = re.search(
        r"^## Outline\n(.*?)(?=\n## |\Z)", body, re.DOTALL | re.MULTILINE
    )
    if not outline_match:
        return {"title": title, "chapters": {}, "outline": ""}

    outline_text = outline_match.group(1)

    # Parse chapters: split by <!-- chapter: id --> markers
    # Store both the comment line and content lines for each chapter
    chapters: dict[str, dict[str, Any]] = {}
    current_id: str | None = None
    current_duration: int | None = None
    current_lines: list[str] = []

    for line in outline_text.splitlines():
        ch_match = CHAPTER_COMMENT_RE.match(line)
        if ch_match:
            if current_id is not None:
                chapters[current_id] = {
                    "content": "\n".join(current_lines).rstrip(),
                    "duration": current_duration,
                }
            current_id = ch_match.group(1)
            current_duration = int(ch_match.group(2)) if ch_match.group(2) else None
            current_lines = []
        else:
            current_lines.append(line)

    if current_id is not None:
        chapters[current_id] = {
            "content": "\n".join(current_lines).rstrip(),
            "duration": current_duration,
        }

    return {"title": title, "chapters": chapters, "outline": outline_text.strip()}


def build_frontmatter(track: dict[str, Any], track_id: str) -> list[str]:
    """Build the YAML frontmatter block."""
    lines: list[str] = ["---"]
    fm: dict[str, Any] = {}
    for key in ("tags", "level", "category", "audience"):
        if key in track:
            fm[key] = track[key]
    if "_computed_duration_hours" in track:
        fm["duration_hours"] = track["_computed_duration_hours"]
    elif "duration_hours" in track:
        fm["duration_hours"] = track["duration_hours"]
    lines.append(yaml.dump(fm, default_flow_style=False).rstrip())
    lines.append("---")
    lines.append(f"<!-- course: {track_id} -->")
    return lines


def build_metadata(track: dict[str, Any], terms: list[str]) -> list[str]:
    """Build the metadata sections of a track markdown."""
    lines: list[str] = []

    lines.append(f"# {_wrap_terms(track['title'], terms)}")
    lines.append("")

    if "description" in track:
        lines.append("## Description")
        lines.append(_wrap_terms(track["description"].strip(), terms))
        lines.append("")

    hours = track.get("_computed_duration_hours", track.get("duration_hours"))
    if hours is not None:
        days = hours // 8
        lines.append("## Duration")
        lines.append(f"{hours} hours / {days} days")
        lines.append("")

    for key, heading in [
        ("intended_audience", "Intended Audience"),
        ("prerequisites", "Prerequisites"),
        ("required_knowledge", "Required Knowledge"),
        ("objectives", "Objectives"),
    ]:
        if key in track:
            lines.append(f"## {heading}")
            for item in track[key]:
                lines.append(f"* {_wrap_terms(item.strip(), terms)}")
            lines.append("")

    if "exercises" in track:
        lines.append("## Exercises")
        for ex in track["exercises"]:
            url = re.sub(r"^https://", "`https`://", ex["url"])
            url = re.sub(r"^http://", "`http`://", url)
            lines.append(f"* [{ex['description']}]({url})")
        lines.append("")

    return lines


def _make_unique_id(ch_id: str, course_slug: str, seen_ids: set[str]) -> str:
    """Return a unique chapter ID, prefixing with course slug if needed."""
    if ch_id not in seen_ids:
        seen_ids.add(ch_id)
        return ch_id
    unique_id = f"{course_slug}-{ch_id}"
    seen_ids.add(unique_id)
    return unique_id


def _rewrite_chapter_ids(
    outline_text: str, course_slug: str, seen_ids: set[str],
) -> str:
    """Rewrite chapter IDs in an outline block to be globally unique."""
    result_lines: list[str] = []
    for line in outline_text.splitlines():
        ch_match = CHAPTER_COMMENT_RE.match(line)
        if ch_match:
            old_id = ch_match.group(1)
            new_id = _make_unique_id(old_id, course_slug, seen_ids)
            duration_part = f", duration: {ch_match.group(2)}h " if ch_match.group(2) else " "
            result_lines.append(f"<!-- chapter: {new_id}{duration_part}-->")
        else:
            result_lines.append(line)
    return "\n".join(result_lines)


def build_outline(track: dict[str, Any]) -> tuple[list[str], int]:
    """Build the outline section by assembling content from courses.

    Returns the outline lines and the total chapter duration in hours.
    """
    lines: list[str] = ["## Outline", ""]
    seen_ids: set[str] = set()
    total_hours = 0

    for entry in track.get("chapters", []):
        course_path = COURSES_DIR / f"{entry['course']}.md"
        if not course_path.exists():
            raise FileNotFoundError(
                f"course not found: {entry['course']} "
                f"(expected {course_path})"
            )

        course = parse_course_md(course_path)
        course_slug = Path(entry["course"]).stem
        selected_chapters = entry.get("chapters")

        if selected_chapters:
            for ch_id in selected_chapters:
                if ch_id not in course["chapters"]:
                    raise ValueError(
                        f"chapter '{ch_id}' not found in {entry['course']}. "
                        f"Available chapters: {list(course['chapters'].keys())}"
                    )
                ch = course["chapters"][ch_id]
                unique_id = _make_unique_id(ch_id, course_slug, seen_ids)
                dur = ch["duration"] if ch["duration"] is not None else 1
                total_hours += dur
                lines.append(f"<!-- chapter: {unique_id}, duration: {dur}h -->")
                lines.append(ch["content"])
                lines.append("")
        elif course["outline"]:
            rewritten = _rewrite_chapter_ids(course["outline"], course_slug, seen_ids)
            lines.append(rewritten)
            lines.append("")
            # Sum durations from the original chapters
            for ch in course["chapters"].values():
                dur = ch["duration"] if ch["duration"] is not None else 1
                total_hours += dur

    return lines, total_hours


def build_footer(track: dict[str, Any], terms: list[str]) -> list[str]:
    """Build the notes and copyright sections."""
    lines: list[str] = []

    if "notes" in track:
        lines.append("## Notes")
        for item in track["notes"]:
            lines.append(f"* {_wrap_terms(item.strip(), terms)}")
        lines.append("")

    lines.append("## Copyright")
    lines.append(
        "Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), "
        "\u00a9 2026"
    )
    lines.append("")

    return lines


def build_track(yaml_path: Path, terms: list[str]) -> str:
    """Build a track markdown from a YAML definition."""
    track = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    track_id = yaml_path.stem
    outline_lines, total_hours = build_outline(track)
    # Use the actual sum of chapter durations so frontmatter matches
    track["_computed_duration_hours"] = total_hours
    lines = (
        build_frontmatter(track, track_id)
        + build_metadata(track, terms)
        + outline_lines
        + build_footer(track, terms)
    )
    return "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 0:
        raise SystemExit(
            "usage: build_tracks.py source1.yaml target1.md [source2.yaml target2.md ...]"
        )
    if len(args) % 2 != 0:
        raise SystemExit(
            f"expected even number of arguments (source/target pairs), got {len(args)}"
        )

    terms = _load_terms()
    for i in range(0, len(args), 2):
        source = Path(args[i])
        target = Path(args[i + 1])
        md_content = build_track(source, terms)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(md_content, encoding="utf-8")


if __name__ == "__main__":
    main()
