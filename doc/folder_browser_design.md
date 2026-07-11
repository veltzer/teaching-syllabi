# Folder Browser Design

## Problem

The index page provides flat filtering by metadata (category, level, tags, audience,
duration) and text search. This works well for finding specific courses but does not
expose the folder hierarchy that organizes courses by domain (e.g., `languages/c++`,
`devops/kubernetes`, `operating_systems/linux/kernel`). Users who want to explore
what is available in a domain must already know what to search for.

## Decision: Integrated breadcrumb browser (not a separate mode)

Three approaches were considered:

1. **Separate toggle** - A "Browse by folder" / "Filter" toggle at the top, with the
   folder view as an entirely separate UI.
2. **Integrated breadcrumb** - A clickable folder path bar above the existing results,
   narrowing the course list to the selected subtree while keeping all existing filters.
3. **Replace** - The folder browser replaces the current filter UI entirely.

**Chosen: option 2 (integrated breadcrumb).** Rationale:
- Least disruptive to the existing UI that already works.
- Filters become more useful when scoped to a folder (e.g., browse to `languages`,
  then filter by level).
- No mode switching needed - folder browsing and metadata filtering coexist naturally.
- Avoids duplicating or discarding the existing filter logic.

## Decision: Subfolders and courses shown together

When a folder contains both subfolders and courses (e.g., `big_data` has subfolders
like `spark`, `splunk` and may have courses directly in it), subfolders are shown
first as clickable cards, followed by the course list below. This mirrors standard
file-browser behavior and handles the real structure of the course tree where courses
exist at multiple depth levels.

The alternative (only showing subfolders until reaching a leaf folder) was rejected
because it would hide courses that sit alongside subfolders.

## Components

### Breadcrumb bar

Shows the current path as clickable segments: `All > languages > c++`. Clicking
any segment navigates to that level. Always visible. Starts at "All" which
represents the root of the course tree.

### Subfolder cards

When the current folder has immediate subfolders, they are displayed as clickable
cards in a grid above the course list. Each card shows the folder name and the
total number of courses it contains (including all nested subfolders). This gives
users a quick sense of how much content each subfolder holds.

### Course list

The existing course list, filtered to the current folder subtree. All metadata
filters (level, category, tag, duration, audience) and text search continue to
work within the selected folder scope. Sort controls are unaffected.

## Data model

No new data is introduced. The folder tree is derived client-side from the `path`
field already present in each course entry (e.g., `courses/languages/c++/advanced_cpp.html`).
A `currentFolder` state variable tracks where the user is in the tree.

## URL scheme

Deep-linking uses `#folder=courses/languages` in the URL hash. This coexists with
the existing `#syllabus=...` and `#search=...` hash schemes.

## Files affected

The index page ships as two parallel UI variants (`material_web`, the default, using
real `<md-*>` components; and `material_css`, using native controls). The folder
browser is implemented in both, so the markup and logic exist in each variant:

- `site-resources/index_material_web.html`, `site-resources/index_material_css.html` -
  Breadcrumb and subfolder container divs above results.
- `site-resources/index_material_web.js`, `site-resources/index_material_css.js` -
  Folder state, breadcrumb rendering, subfolder card rendering, folder-scoped
  filtering in `render()`.

Styling is shared rather than duplicated:

- `shared/shared-themes/components.css` - Canonical styles for the breadcrumb bar
  (`.breadcrumb-current`, `.breadcrumb-sep`) and subfolder cards (`.subfolder-card`,
  `.subfolder-count`). Both variants rely on these.
- `site-resources/index_material_css.css` - Overrides a subset of the above for the
  native-controls variant. The `material_web` variant needs no folder-browser CSS of
  its own.

## What does not change

- The syllabus view (`#syllabus=...`) is unaffected.
- All existing filters, sort controls, and autocomplete work as before.
- The data format produced by `build_site.py` is unchanged.
- PDF and DOCX outputs are unaffected.
