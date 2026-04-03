---
tags:
  - tools:git
  - concepts:version-control
  - practices:devops
level: advanced
category: version-control
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:team-leads
---
<!-- course: advanced_git -->
# Advanced `Git`

## Description
This course dives deep into advanced `Git` workflows and techniques for experienced developers. Topics include rebasing strategies, interactive rebase, cherry-pick, bisect, hooks, subtrees, submodules, monorepo strategies, reflog, worktrees, and advanced merge conflict resolution. Students will gain the expertise needed to manage complex version control scenarios and optimize team workflows.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers who use `Git` daily and want to deepen their expertise
* Team leads responsible for branching strategies and code integration
* `DevOps` engineers managing complex repository structures

## Prerequisites
* `Solid` working knowledge of `Git` fundamentals (commit, branch, merge, push, pull).
* Experience working with remote repositories.
* Familiarity with command-line interfaces.

## Objectives
* Master rebasing strategies including interactive rebase for `clean` commit history.
* Use cherry-pick to selectively apply commits across branches.
* Debug regressions efficiently using `git bisect`.
* Implement and manage `Git` hooks for automation.
* Work with subtrees and submodules for multi-repository projects.
* Apply monorepo strategies and tooling.
* Recover lost work using reflog.
* Leverage worktrees for parallel development.
* Resolve complex merge conflicts with advanced techniques.

## Outline
<!-- chapter: rebasing-strategies, duration: 2h -->
* Rebasing Strategies:
    * Rebase vs. merge workflows.
    * Interactive rebase: squashing, reordering, editing, and splitting commits.
    * Rebase onto and upstream rebasing.
    * Risks and best practices for rebasing shared branches.
<!-- chapter: cherry-pick, duration: 2h -->
* Cherry-Pick:
    * Selecting and applying individual commits.
    * Cherry-picking ranges of commits.
    * Handling conflicts during cherry-pick.
    * Use cases and best practices.
<!-- chapter: bisect, duration: 1h -->
* Bisect:
    * Binary search for regressions with `git bisect`.
    * Manual and automated bisect runs.
    * Writing bisect scripts for automation.
<!-- chapter: hooks, duration: 2h -->
* Hooks:
    * Client-side hooks: pre-commit, commit-msg, pre-push.
    * Server-side hooks: pre-receive, post-receive, update.
    * Managing hooks across teams.
    * Integration with `CI/CD` pipelines.
<!-- chapter: subtrees-and-submodules, duration: 2h -->
* Subtrees and Submodules:
    * `Git` submodules: adding, updating, and removing.
    * `Git` subtrees: merging and splitting.
    * Comparing subtrees vs. submodules.
    * Managing dependencies with nested repositories.
<!-- chapter: monorepo-strategies, duration: 2h -->
* Monorepo Strategies:
    * Monorepo vs. multi-repo trade-offs.
    * Sparse checkout and partial clone.
    * Tooling for monorepo management.
    * Scaling `Git` for large repositories.
<!-- chapter: reflog, duration: 1h -->
* Reflog:
    * Understanding the reflog and reference history.
    * Recovering lost commits and branches.
    * Reflog expiration and maintenance.
<!-- chapter: worktrees, duration: 2h -->
* Worktrees:
    * Creating and managing multiple worktrees.
    * Parallel development workflows.
    * Worktrees with branches and detached HEAD.
<!-- chapter: advanced-merge-conflict-resolution, duration: 2h -->
* Advanced Merge Conflict Resolution:
    * Three-way merge internals.
    * Merge strategies and strategy options.
    * Using merge tools and diff3 conflict style.
    * Resolving complex conflicts in rebases and cherry-picks.
    * Rerere: reuse recorded resolution.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
