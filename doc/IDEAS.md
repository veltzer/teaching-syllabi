# Ideas for future development

## PDF/HTML generation
Add a step to produce polished PDFs with a consistent template, header, and logo for each syllabus using pandoc.

## Index page
Auto-generate an index page that lists all courses by category with links, durations, and short descriptions. Could be implemented as a tera template.

## Course dependency graph
Use the Prerequisites fields to generate a visual graph (mermaid or graphviz) showing which courses lead into which.

## Duration summary
Auto-generate a report showing total teaching hours per category and overall.

## Diff/changelog
Track syllabus changes over time so clients can see what was updated between versions.

## Validation CI step
Check all syllabi for required YAML fields, non-empty sections, valid durations, and consistent formatting.

## Website/GitHub Pages
Publish the generated HTML syllabi as a browsable site with search and navigation.
