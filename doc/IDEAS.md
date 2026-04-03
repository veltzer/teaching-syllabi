# Ideas for future development

## Build & CI

* Wire `build_tracks.py` into rsconstruct as a `script` processor so tracks are built automatically, not manually.

## Site / index.html

* Render assembled track markdowns through pandoc and show them in the SPA alongside courses.
* Show course metadata (tags, level, duration, audience) in the syllabus SPA view, not just in the index listing.

## Structure & Quality

* Validate track YAML files at build time — check that all course references and chapter IDs are valid (could be a rsconstruct `script` processor).

## Older Ideas

* Course dependency graph — use Prerequisites fields to generate a visual graph (mermaid or graphviz).
* Duration summary — auto-generate a report showing total teaching hours per category and overall.
* Diff/changelog — track syllabus changes over time so clients can see what was updated between versions.
