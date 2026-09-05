# Instructions for Claude Code

* read the instructions in the file doc/HowToWriteSyllabus.txt
* read the sample syllabus from the file syllabi/courses/languages/python/python_programming.md

# Instructions

To run all tests run "rsconstruct build"

# Terms

The technical-terms registry lives in the `shared/shared-terms/` submodule
(github.com/veltzer/shared-terms). It is not owned by this repo: edit terms
in the `shared-terms` repo first, then bump the submodule here.

# Git

* Never commit changes. Only commit when the user explicitly asks.

# Coding style

* Be strict. Never pass errors silently. Never forgive validation failures. All checks must fail loudly on any error.
* Never propose ugly workarounds. Prefer clean, proper solutions even if they require more effort.
