#!/usr/bin/env python3

"""
Build the GitHub Pages site from generated pandoc HTML files.
Copies all HTML syllabi to docs/ and generates an index.html.
"""

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PANDOC_DIR = ROOT / "out" / "pandoc"
DOCS_DIR = ROOT / "docs"


def extract_title(html_path):
    """Extract the course title from the first <h1> tag."""
    text = html_path.read_text(encoding="utf-8")
    match = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.DOTALL)
    if match:
        title = re.sub(r"<[^>]+>", "", match.group(1))
        return title.strip()
    return html_path.stem.replace("_", " ").title()


def category_label(rel_path):
    """Derive a human-readable category from the relative path."""
    parts = rel_path.parts[:-1]  # drop filename
    return " / ".join(p.replace("_", " ").title() for p in parts)


def build_site():
    if not PANDOC_DIR.exists():
        print(f"Error: {PANDOC_DIR} does not exist. Run 'rsconstruct build' first.")
        raise SystemExit(1)

    # clean and recreate docs/
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

    # collect all HTML files
    entries = []
    for html_file in sorted(PANDOC_DIR.rglob("*.html")):
        rel = html_file.relative_to(PANDOC_DIR)
        dest = DOCS_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(html_file, dest)
        title = extract_title(html_file)
        category = category_label(rel)
        entries.append((category, title, str(rel)))

    # group by category
    categories = {}
    for category, title, path in entries:
        categories.setdefault(category, []).append((title, path))

    # generate index.html
    index_path = DOCS_DIR / "index.html"
    lines = [
        "<!DOCTYPE html>",
        "<html lang=\"en\">",
        "<head>",
        "<meta charset=\"utf-8\">",
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
        "<title>Teaching Syllabi - Mark Veltzer</title>",
        "<style>",
        "body { font-family: sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }",
        "h1 { border-bottom: 2px solid #333; padding-bottom: 10px; }",
        "h2 { color: #555; margin-top: 30px; }",
        "ul { list-style: none; padding-left: 0; }",
        "li { margin: 5px 0; }",
        "a { color: #0366d6; text-decoration: none; }",
        "a:hover { text-decoration: underline; }",
        ".count { color: #888; font-size: 0.9em; }",
        "</style>",
        "</head>",
        "<body>",
        "<h1>Teaching Syllabi</h1>",
        f"<p>Mark Veltzer — {len(entries)} courses</p>",
    ]

    for category in sorted(categories.keys()):
        items = sorted(categories[category], key=lambda x: x[0])
        lines.append(f"<h2>{category} <span class=\"count\">({len(items)})</span></h2>")
        lines.append("<ul>")
        for title, path in items:
            lines.append(f"<li><a href=\"{path}\">{title}</a></li>")
        lines.append("</ul>")

    lines.extend([
        "<hr>",
        "<p>Mark Veltzer <a href=\"mailto:mark.veltzer@gmail.com\">mark.veltzer@gmail.com</a>, &copy; 2026</p>",
        "</body>",
        "</html>",
    ])

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Site built: {len(entries)} syllabi copied to {DOCS_DIR}")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    build_site()
