# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `site-resources/index_material_css.js:170` - DOM XSS: `currentFolder` comes straight from `location.hash` (`#folder=...`, lines 115 and 377) and its last segment is concatenated into `breadcrumbEl.innerHTML`, so `#folder=<img src=x onerror=...>` runs script on the shared `veltzer.github.io` origin; the same code is in `site-resources/index_material_web.js:165`. Build the breadcrumb with `textContent`/DOM nodes (and stop splicing `path` into inline `onclick` strings at line 172). The `#syllabus=` value is likewise put unescaped into `href` attributes at lines 70-73.
- `scripts/build_tracks.py:167` - exercise URLs are rewritten to `` `https`:// ``, which lands inside the link target: `out/processor.generator.generic/aws_for_experienced_developers.md:33` renders `[...](`https`://amazon.qwiklabs.com)`, a broken link in the published HTML/PDF/DOCX. Leave the URL untouched (only wrap terms in the link text).

## Medium

- `scripts/build_site.py:21` - `TAG_LISTS_DIR` points at `tag_lists/`, which no longer exists (the vocabulary moved to `shared/shared-tags`, see `rsconstruct.toml:129-132`); `read_tag_order` silently returns `[]` (line 39), so the level/category/audience filters fall back to alphabetical order. Point it at `shared/shared-tags` and raise if the file is missing, per the repo's fail-loudly rule (`CLAUDE.md:22`).
- `scripts/build_tracks.py:81` - a course without an `## Outline` section returns no chapters, and `build_outline` (line 237) then silently adds nothing for that track entry; raise instead. Likewise the `else 1` duration fallbacks at lines 232 and 243 invent durations that `doc/HowToWriteSyllabus.txt:4` says must always be explicit.
- `pyproject.toml:224` - `demjson3` is a declared dependency but nothing in the repo imports it; remove it (and refresh `uv.lock`).
- `doc/HowToWriteSyllabus.txt:3` - "do not state how long each topics/subtopic takes" contradicts line 4 ("ALL chapters MUST have a duration specified"), which `scripts/check_md.py:176` enforces; delete or reword line 3. Line 8 has typos ("syllsbus my have").

## Low

- `scripts/build_site.py:144` - missing or non-int `duration_hours*` values silently become `0` (lines 169-174), and missing `level`/`category` become `""`; fail on them instead, as `CLAUDE.md:22` requires.
- `scripts/build_tracks.py:262` - the track copyright year is hard-coded `© 2026`; derive it (or read it from config) so generated tracks do not go stale.
- `doc/course_division_rules.md:53` - says tags must exist in `tag_lists/*.txt`; update to `shared/shared-tags/*.txt`.
- `doc/superpowers/plans/2026-04-04-folder-browser.md:15` - completed implementation plan still lists unchecked steps against `resources/index.{html,css,js}`, files that are now `site-resources/index_material_*`; delete the plan or mark it done.
- `tera.snippets/main.md.tera:1` - no leading blank line, so `README.md:43-44` glues the build badge to the `## Number of syllabi` heading; start the snippet with an empty line.
- `doc/TODO.txt:1` - empty file; delete it.
