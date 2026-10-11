# Plan: courses from Markdown to YAML

Status: planned (2026-10-11), not started. Decisions A-D in the last section
are open.

## Goal

Each course becomes a YAML data file. Chapter ids and durations become real
fields instead of `<!-- chapter: id, duration: Nh -->` comments, the build
generates the Markdown that is rendered, and courses and tracks share one
pipeline. The Lua filter, the chapter comments and the regular expressions
that parse them all go away.

Why: chapter durations are part of the content, not something to hide in
comments, and chapter ids must stay explicit and stable because tracks select
chapters by id (`chapters: [what-is-devops, continuous-integration]`). No
standard Markdown feature carries both; YAML does, and the tracks are already
YAML with the same kinds of fields.

## What the research found

- The structure is uniform: all 666 course files have the same seven required
  sections (Description, Duration, Intended Audience, Prerequisites,
  Objectives, Outline, Copyright) in the same order. The optional ones follow
  the order in `check_syllabus_md.py`'s `REQUIRED` list. There are 23 distinct
  section sequences in total, bullets nest at most four deep, and there are
  no code blocks or tables.
- Some of it is redundant: the course id always equals the file name,
  Copyright is the same text in all 666 files, and the Duration section
  restates `duration_hours` in 642 of them.
- The content is Markdown text: 31,128 code spans, 773 links, and markup in
  438 of the titles. YAML values are therefore Markdown strings, as they
  already are in the track YAML.
- Irregular cases the schema must hold:
    - 15 Duration sections say more than a number (short/long variants, notes
      such as "assumes `Java` experience");
    - about 60 list sections mix prose with bullets;
    - 116 plain-text lines sit inside 17 outlines, including "Day 1/2/3"
      sub-headings in two files.
- What reads the course `.md` files today:
    - six build steps: pandoc, zspell, terms, tags, rumdl and
      `check_syllabus_md.py`;
    - three scripts: `build_tracks.py` (chapters by id), `build_site.py`
      (front matter, the title from `<h1>`, stale-file cleanup) and
      `print/pandoc_filter.lua`;
    - outside the repository: teaching-slides' authoring guide
      (`doc/slides_from_syllabi_progress.md`), which points authors at the
      `.md` paths.

## Course schema

One file per course, `syllabi/courses/<domain>/<course>.yaml`; the course id
is the file name.

```yaml
title: Advanced `C++`                 # Markdown inline text
tags: [...]                           # unchanged: tags, level, category, audience
level: advanced
category: languages
audience: [...]
duration_note: ...                    # optional Markdown, for the 15 special Duration texts
description: |                        # Markdown, any number of paragraphs
  This course covers ...
intended_audience: [...]              # list sections, see "Items" below
prerequisites: [...]
required_knowledge: [...]             # optional
objectives: [...]
chapters:
  - id: move-semantics-and-perfect-forwarding
    title: Move Semantics and Perfect Forwarding
    hours: 2
    text: ...                         # optional Markdown before the topics
    topics:
      - Rvalue references and value categories
      - text: Move constructors
        topics: [...]                 # nested, up to the existing depth of 4
exercises: ...                        # optional sections, in today's order:
                                      # exercises, references, installations,
                                      # not_covered, notes, resources, links
```

- Items: a list section is either a list of items or a Markdown block (for
  the sections that mix prose and bullets). An item is a Markdown string or
  `{text, topics}`.
- Computed, no longer written by hand:
    - `duration_hours` is the sum of the chapters' `hours`, so the
      "durations must add up" check can no longer fail;
    - Copyright and the course id.
- The 13 short/long courses keep `duration_hours_short` and
  `duration_hours_long` as explicit fields.
- The two outlines grouped by day use an optional
  `parts: [{title, chapters}]` instead of `chapters`.

## Validation

- A JSON Schema, checked by a new `scripts/check_syllabus_yaml.py`
  (`jsonschema`), for exact structural errors.
- The same script checks what a schema cannot express: chapter ids unique and
  well-formed, `hours` a positive integer.
- `iyamllint` extends to `syllabi/`.
- `check_syllabus_md.py` is retired; its section-order and required-section
  rules are now the schema.

## One generator for courses and tracks

`scripts/build_tracks.py` becomes `scripts/build_markdown.py`, which turns a
course or a track YAML into the Markdown that is rendered:

- front matter with `title`, tags, level, category, audience and the computed
  `duration_hours`, so the tags processor and `build_site.py` keep working
  unchanged on the output;
- sections in today's order, Copyright generated;
- chapters as bullets, with the duration shown or hidden (decision A);
- no chapter comments, and no category line (decision B).

Tracks read chapters straight from the course YAML by `id`. The comment
regular expressions and the `else 1` duration fallbacks (listed in
`TOFIX.md`) disappear.

In `rsconstruct.toml`, a `processor.generator.generic` instance for
`syllabi/**/*.yaml` writes the generated Markdown, and the pandoc instances
read it with no `--lua-filter`. To verify in phase 1: the generated path must
still map to `_site/courses/<path>.html`, which the site depends on.

## Other consumers

- zspell, terms and rumdl run on the generated Markdown. The cost is that
  their errors name the generated file rather than the YAML; the terms
  checker names the term, so finding it in the YAML is easy.
- The tags processor works unchanged on the generated front matter.
- `build_site.py` reads metadata from the course YAML, takes the title from
  YAML instead of scraping `<h1>`, and its stale-file cleanup keys on
  `.yaml`.
- The site's syllabus view draws the folder breadcrumbs itself, reusing
  `renderBreadcrumb`, built from DOM nodes (which also fixes the XSS in that
  function listed in `TOFIX.md`).
- `print/pandoc_filter.lua` is deleted, with its luacheck entry.

## Migration and verification

- A one-shot `scripts/migrate_md_to_yaml.py` converts every `.md` to `.yaml`,
  stopping with an explicit error on anything it cannot classify, so nothing
  is guessed silently.
- Verification is mechanical. Every course and track is built both ways: the
  current Markdown through pandoc with the Lua filter, and the YAML through
  the generator with durations hidden and the category line reproduced. The
  HTML must be byte-identical for all 666 courses and 11 tracks, and the DOCX
  must read back as the same document. Only then are the intended changes
  switched on (visible durations, the category line per decision B).

## Phases

Each phase ends with a green `rsconstruct build`. Following `CLAUDE.md`,
nothing is committed without an explicit request, so each phase stops for
review.

1. Build alongside: schema, checker, converter and generator, next to the
   existing Markdown. Proof: the comparison above matches. Nothing switches
   over.
2. Switch: commit the YAML, delete the `.md` sources, repoint the
   processors, remove the filter and `check_syllabus_md.py`.
3. Site: breadcrumbs in the site's JavaScript, `build_site.py` reading YAML.
4. Docs: `HowToWriteSyllabus.txt` rewritten for YAML (also resolving the
   contradiction on its line 3), the sample path in `CLAUDE.md`,
   `STRUCTURE.md`, the README, and teaching-slides' authoring guide.

## Open decisions

- **A. Durations.** Show them as `Chapter title (2h)` by default? When must
  they be hidden: a per-build option, a per-course flag, or never?
- **B. Category line.** Keep it in DOCX and PDF (from the folder path or from
  the front-matter `category`), or drop it? On the website it moves into the
  page's breadcrumbs either way.
- **C. YAML quoting.** About 17% of list items need quotes in hand-written
  YAML (7,714 start with a code span, 2,875 contain `: `). Proposal: the
  converter writes every Markdown value double-quoted, so editing never runs
  into it, and yamllint enforces the style.
- **D. Irregular content.** Keep it as Markdown blocks in the schema (as
  above), or normalize it during the migration (the ~60 mixed sections into
  pure lists, the 15 special Duration texts into `duration_note`)?

## Not affected

- rspandoc needs no new feature: the plan removes the only Lua filter, so
  the gap with Lua filters and tables no longer matters.
- business-syllabi is unaffected; it is a separate repository with its own
  syllabi.
