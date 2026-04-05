#!/usr/bin/env python3

"""
Generate index.html for the GitHub Pages site.
Pandoc outputs directly to _site/ via rsconstruct; this script
scans the HTML files there and builds a filterable index page.
"""

import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
SYLLABI_DIR = ROOT / "syllabi"
TRACKS_DIR = ROOT / "tracks"
DOCS_DIR = ROOT / "_site"
TAG_LISTS_DIR = ROOT / "tag_lists"
RESOURCES_DIR = ROOT / "resources"
DOCS_EXTENSIONS = {".html", ".docx", ".pdf"}


def read_tag_order(filename: str) -> list[str]:
    """Read tag values from a tag_lists file, preserving file order."""
    path = TAG_LISTS_DIR / filename
    if not path.exists():
        return []
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def order_by_tag_list(values: set[str], filename: str) -> list[str]:
    """Order values according to tag_lists file order, with any extras sorted at the end."""
    file_order = read_tag_order(filename)
    ordered = [v for v in file_order if v in values]
    remaining = sorted(values - set(ordered))
    return ordered + remaining


def parse_frontmatter(md_path: Path) -> dict[str, Any]:
    """Parse YAML frontmatter from a markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if match:
        result = yaml.safe_load(match.group(1))
        if isinstance(result, dict):
            return result
    return {}


def extract_title(html_path: Path) -> str:
    """Extract the course title from the first <h1> tag."""
    text = html_path.read_text(encoding="utf-8")
    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.DOTALL)
    if match:
        title = re.sub(r"<[^>]+>", "", match.group(1))
        return title.strip()
    return html_path.stem.replace("_", " ").title()


def folder_label(rel_path: Path) -> str:
    """Derive a human-readable folder path from the relative path."""
    parts = rel_path.parts[:-1]
    return " / ".join(p.replace("_", " ").title() for p in parts)


def clean_stale__site() -> None:
    """Remove files from _site/ that no longer have a corresponding source."""
    expected_stems: set[Path] = set()
    for md_file in SYLLABI_DIR.rglob("*.md"):
        rel = md_file.relative_to(SYLLABI_DIR).with_suffix("")
        expected_stems.add(DOCS_DIR / rel)
    for yaml_file in TRACKS_DIR.glob("*.yaml"):
        rel = Path("tracks") / yaml_file.stem
        expected_stems.add(DOCS_DIR / rel)
    removed = 0
    for doc_file in DOCS_DIR.rglob("*"):
        if not doc_file.is_file():
            continue
        if doc_file.suffix not in DOCS_EXTENSIONS:
            continue
        stem_path = doc_file.with_suffix("")
        if stem_path not in expected_stems:
            doc_file.unlink()
            print(f"Removed stale: {doc_file.relative_to(ROOT)}")
            removed += 1
    if removed:
        # Remove empty directories left behind
        for dirpath in sorted(DOCS_DIR.rglob("*"), reverse=True):
            if dirpath.is_dir() and not any(dirpath.iterdir()):
                dirpath.rmdir()
        print(f"Cleaned {removed} stale file(s) from _site/")


def load_metadata(rel: Path) -> dict[str, Any]:
    """Load metadata for a syllabus entry from its markdown frontmatter or track YAML."""
    md_file = SYLLABI_DIR / rel.with_suffix(".md")
    if md_file.exists():
        return parse_frontmatter(md_file)
    if rel.parts[0] == "tracks":
        yaml_file = TRACKS_DIR / (rel.stem + ".yaml")
        if yaml_file.exists():
            return yaml.safe_load(yaml_file.read_text(encoding="utf-8")) or {}
    return {}


def build_site() -> None:
    if not DOCS_DIR.exists():
        print(f"Error: {DOCS_DIR} does not exist. Run 'rsconstruct build' first.")
        raise SystemExit(1)

    clean_stale__site()

    entries: list[dict[str, Any]] = []
    all_tags: set[str] = set()
    all_levels: set[str] = set()
    all_categories: set[str] = set()
    all_audiences: set[str] = set()

    for html_file in sorted(DOCS_DIR.rglob("*.html")):
        if html_file.name == "index.html":
            continue
        rel = html_file.relative_to(DOCS_DIR)

        meta = load_metadata(rel)

        title = extract_title(html_file)
        tags = [str(t) for t in meta.get("tags", []) if t is not None]
        level = str(meta.get("level", ""))
        category = str(meta.get("category", ""))
        audience = [str(a) for a in meta.get("audience", []) if a is not None]
        duration_hours = meta.get("duration_hours", 0)
        duration_hours_short = meta.get("duration_hours_short", 0)
        duration_hours_long = meta.get("duration_hours_long", 0)
        folder = folder_label(rel)

        if isinstance(tags, list):
            all_tags.update(tags)
        if isinstance(level, str) and level:
            all_levels.add(level)
        if isinstance(category, str) and category:
            all_categories.add(category)
        if isinstance(audience, list):
            all_audiences.update(audience)

        entry: dict[str, Any] = {
            "title": title,
            "path": str(rel),
            "folder": folder,
            "tags": tags if isinstance(tags, list) else [],
            "level": level if isinstance(level, str) else "",
            "category": category if isinstance(category, str) else "",
            "audience": audience if isinstance(audience, list) else [],
        }
        if duration_hours_short or duration_hours_long:
            dhs = duration_hours_short
            entry["duration_hours_short"] = dhs if isinstance(dhs, int) else 0
            dhl = duration_hours_long
            entry["duration_hours_long"] = dhl if isinstance(dhl, int) else 0
        else:
            dh = duration_hours
            entry["duration_hours"] = dh if isinstance(dh, int) else 0
        entries.append(entry)

    index_html = generate_index(
        entries,
        sorted(all_tags),
        order_by_tag_list(all_levels, "level.txt"),
        order_by_tag_list(all_categories, "category.txt"),
        order_by_tag_list(all_audiences, "audiences.txt"),
    )
    index_path = DOCS_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"Site index built: {len(entries)} syllabi found in {DOCS_DIR}")
    print(f"Index: {index_path}")


def generate_index(
    entries: list[dict[str, Any]],
    all_tags: list[str],
    all_levels: list[str],
    all_categories: list[str],
    all_audiences: list[str],
) -> str:
    css = (RESOURCES_DIR / "index.css").read_text(encoding="utf-8")
    js = (RESOURCES_DIR / "index.js").read_text(encoding="utf-8")
    template = (RESOURCES_DIR / "index.html").read_text(encoding="utf-8")

    level_options = "".join(
        f'<option value="{v}">{v.title()}</option>' for v in all_levels
    )
    category_options = "".join(
        f'<option value="{v}">{v.replace("-", " ").title()}</option>'
        for v in all_categories
    )
    tag_options = "".join(
        f'<option value="{v}">{v}</option>' for v in all_tags
    )
    audience_options = "".join(
        f'<option value="{v}">{v.replace("-", " ").title()}</option>'
        for v in all_audiences
    )

    return (
        template
        .replace("{{CSS}}", css)
        .replace("{{JS}}", js)
        .replace("{{DATA_JSON}}", json.dumps(entries, ensure_ascii=False))
        .replace("{{TOTAL_COUNT}}", str(len(entries)))
        .replace("{{LEVEL_OPTIONS}}", level_options)
        .replace("{{CATEGORY_OPTIONS}}", category_options)
        .replace("{{TAG_OPTIONS}}", tag_options)
        .replace("{{AUDIENCE_OPTIONS}}", audience_options)
    )


if __name__ == "__main__":
    build_site()
