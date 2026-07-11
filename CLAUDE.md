# Instructions for Claude Code

* read the instructions in the file doc/HowToWriteSyllabus.txt
* read the sample syllabus from the file syllabi/courses/languages/python/python_programming.md

# Instructions

To run all tests run "rsconstruct build"

# Terms

The `terms.ambiguous/` and `terms.single_meaning/` directories are vendored
from github.com/veltzer/terms — committed to this repo, but not the source
of truth. To pull in upstream changes run `scripts/sync_terms.py` and
commit the resulting diff. Edits to these terms must be made in the `terms`
repo first, then synced here.

# Git

* Never commit changes. Only commit when the user explicitly asks.

# Coding style

* Be strict. Never pass errors silently. Never forgive validation failures. All checks must fail loudly on any error.
* Never propose ugly workarounds. Prefer clean, proper solutions even if they require more effort.
