#!/usr/bin/env python3

"""
Build the GitHub Pages site from generated pandoc HTML files.
Copies all HTML syllabi to docs/ and generates an index.html
with JavaScript-based filtering by tags, level, category, and audience.
"""

import json
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SYLLABI_DIR = ROOT / "syllabi"
PANDOC_DIR = ROOT / "out" / "pandoc"
DOCS_DIR = ROOT / "docs"


def parse_frontmatter(md_path: Path) -> dict[str, object]:
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


def build_site() -> None:
    if not PANDOC_DIR.exists():
        print(f"Error: {PANDOC_DIR} does not exist. Run 'rsconstruct build' first.")
        raise SystemExit(1)

    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

    entries: list[dict[str, object]] = []
    all_tags: set[str] = set()
    all_levels: set[str] = set()
    all_categories: set[str] = set()
    all_audiences: set[str] = set()

    for html_file in sorted(PANDOC_DIR.rglob("*.html")):
        rel = html_file.relative_to(PANDOC_DIR)
        dest = DOCS_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(html_file, dest)

        md_file = SYLLABI_DIR / rel.with_suffix(".md")
        meta = parse_frontmatter(md_file) if md_file.exists() else {}

        title = extract_title(html_file)
        tags = [str(t) for t in meta.get("tags", []) if t is not None]
        level = str(meta.get("level", ""))
        category = str(meta.get("category", ""))
        audience = [str(a) for a in meta.get("audience", []) if a is not None]
        duration_days = meta.get("duration_days", 0)
        folder = folder_label(rel)

        if isinstance(tags, list):
            all_tags.update(tags)
        if isinstance(level, str) and level:
            all_levels.add(level)
        if isinstance(category, str) and category:
            all_categories.add(category)
        if isinstance(audience, list):
            all_audiences.update(audience)

        entries.append({
            "title": title,
            "path": str(rel),
            "folder": folder,
            "tags": tags if isinstance(tags, list) else [],
            "level": level if isinstance(level, str) else "",
            "category": category if isinstance(category, str) else "",
            "audience": audience if isinstance(audience, list) else [],
            "duration_days": duration_days if isinstance(duration_days, int) else 0,
        })

    index_html = generate_index(
        entries,
        sorted(all_tags),
        sorted(all_levels),
        sorted(all_categories),
        sorted(all_audiences),
    )
    index_path = DOCS_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"Site built: {len(entries)} syllabi copied to {DOCS_DIR}")
    print(f"Index: {index_path}")


def generate_index(
    entries: list[dict[str, object]],
    all_tags: list[str],
    all_levels: list[str],
    all_categories: list[str],
    all_audiences: list[str],
) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teaching Syllabi - Mark Veltzer</title>
<style>
body {{ font-family: sans-serif; max-width: 1100px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
.filters {{ background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
.filter-row {{ margin-bottom: 10px; display: flex; align-items: center; flex-wrap: wrap; gap: 8px; }}
.filter-row label {{ font-weight: bold; min-width: 90px; }}
select {{ padding: 4px 8px; border-radius: 4px; border: 1px solid #ccc; }}
input[type="text"] {{ padding: 4px 8px; border-radius: 4px; border: 1px solid #ccc; width: 300px; }}
.count {{ color: #888; font-size: 0.9em; }}
h2 {{ color: #555; margin-top: 30px; }}
ul {{ list-style: none; padding-left: 0; }}
li {{ margin: 5px 0; }}
li.hidden {{ display: none; }}
a {{ color: #0366d6; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.tag {{ display: inline-block; background: #e1ecf4; color: #39739d; padding: 1px 6px; border-radius: 3px; font-size: 0.8em; margin-left: 4px; }}
.level {{ display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 0.8em; margin-left: 4px; }}
.level-beginner {{ background: #dff0d8; color: #3c763d; }}
.level-intermediate {{ background: #fcf8e3; color: #8a6d3b; }}
.level-advanced {{ background: #f2dede; color: #a94442; }}
.duration {{ color: #888; font-size: 0.85em; margin-left: 6px; }}
.no-results {{ color: #888; font-style: italic; padding: 20px 0; }}
</style>
</head>
<body>
<h1>Teaching Syllabi</h1>
<p id="total-count">{len(entries)} courses</p>

<div class="filters">
<div class="filter-row">
<label for="search">Search:</label>
<input type="text" id="search" placeholder="Type to filter by title...">
</div>
<div class="filter-row">
<label for="filter-level">Level:</label>
<select id="filter-level">
<option value="">All levels</option>
{"".join(f'<option value="{v}">{v.title()}</option>' for v in all_levels)}
</select>
</div>
<div class="filter-row">
<label for="filter-category">Category:</label>
<select id="filter-category">
<option value="">All categories</option>
{"".join(f'<option value="{v}">{v.replace("-", " ").title()}</option>' for v in all_categories)}
</select>
</div>
<div class="filter-row">
<label for="filter-tag">Tag:</label>
<select id="filter-tag">
<option value="">All tags</option>
{"".join(f'<option value="{v}">{v}</option>' for v in all_tags)}
</select>
</div>
<div class="filter-row">
<label for="filter-audience">Audience:</label>
<select id="filter-audience">
<option value="">All audiences</option>
{"".join(f'<option value="{v}">{v.replace("-", " ").title()}</option>' for v in all_audiences)}
</select>
</div>
</div>

<div id="results"></div>

<hr>
<p>Mark Veltzer <a href="mailto:mark.veltzer@gmail.com">mark.veltzer@gmail.com</a>, &copy; 2026</p>

<script>
const DATA = {json.dumps(entries, ensure_ascii=False)};

const searchEl = document.getElementById("search");
const levelEl = document.getElementById("filter-level");
const categoryEl = document.getElementById("filter-category");
const tagEl = document.getElementById("filter-tag");
const audienceEl = document.getElementById("filter-audience");
const resultsEl = document.getElementById("results");
const totalEl = document.getElementById("total-count");

function render() {{
    const search = searchEl.value.toLowerCase();
    const level = levelEl.value;
    const category = categoryEl.value;
    const tag = tagEl.value;
    const audience = audienceEl.value;

    const filtered = DATA.filter(e => {{
        if (search && !e.title.toLowerCase().includes(search)) return false;
        if (level && e.level !== level) return false;
        if (category && e.category.replace(/-/g, " ").toLowerCase() !== category.replace(/-/g, " ").toLowerCase()) return false;
        if (tag && !e.tags.includes(tag)) return false;
        if (audience && !e.audience.some(a => a.replace(/-/g, " ").toLowerCase() === audience.replace(/-/g, " ").toLowerCase())) return false;
        return true;
    }});

    totalEl.textContent = filtered.length + " of " + DATA.length + " courses";

    const grouped = {{}};
    for (const e of filtered) {{
        if (!grouped[e.folder]) grouped[e.folder] = [];
        grouped[e.folder].push(e);
    }}

    const folders = Object.keys(grouped).sort();
    let html = "";
    if (folders.length === 0) {{
        html = '<p class="no-results">No courses match the current filters.</p>';
    }}
    for (const folder of folders) {{
        const items = grouped[folder].sort((a, b) => a.title.localeCompare(b.title));
        html += "<h2>" + folder + ' <span class="count">(' + items.length + ")</span></h2><ul>";
        for (const item of items) {{
            const levelClass = item.level ? " level-" + item.level : "";
            const levelBadge = item.level ? '<span class="level' + levelClass + '">' + item.level + "</span>" : "";
            const durationBadge = item.duration_days ? '<span class="duration">' + item.duration_days + "d</span>" : "";
            html += '<li><a href="' + item.path + '">' + item.title + "</a>" + levelBadge + durationBadge + "</li>";
        }}
        html += "</ul>";
    }}
    resultsEl.innerHTML = html;
}}

searchEl.addEventListener("input", render);
levelEl.addEventListener("change", render);
categoryEl.addEventListener("change", render);
tagEl.addEventListener("change", render);
audienceEl.addEventListener("change", render);
render();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    build_site()
