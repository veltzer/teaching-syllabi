---
tags:
  - tools:git
  - concepts:version-control
level: beginner
category: version-control
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
  - audiences:managers
---
<!-- course: introduction_to_git -->
<!-- Track gaps: core `Git` internals (SHA1, object store), renaming/moving/removing files, stashing, rewriting history -->
# Introduction to `Git`

## Description
`Git` is the de-facto standard source control system for the tech industry and is one of the most flexible software tools to be found. Any developer or `DevOps` person probably needs at least a basic understanding of `Git` to get going and this course is intended for that purpose.

This course covers all of the fundamental operations an experienced coder would use on a daily basis. The course begins with an introduction to `Git` and a comparison of `Git` to other version control systems. It then transitions into the nuts-and-bolts of working with `Git`, including everything from setting up a repository to advanced topics like branching and merging.

Because the industry sometimes misuses `git` this course is also focuses on clearing up muddled understanding of `git`: the staging area, merge vs rebase, history management, branching and more

## Duration
24 hours/3 days

## Intended Audience
* Any software developer or `DevOps` who needs to work with `Git` or understand `Git` better.
* Any software developer who has worked with `Git` but wants a deeper understanding of it.
* System administrators who are moving to `DevOps` in general or `Git` specifically.
* Any manager who needs to understand what is possible and how to manage `git` using projects.

## Prerequisites
* Tech affinity.

## Objectives
* Setup and use `git`
* Understand and use `Git`'s branching features correctly and effectively
* Decide on which workflows to use `when` using `Git`

## Outline
<!-- chapter: introduction-to-git, duration: 1h -->
* Introduction to `Git`
    * History of `Git`
    * Who is using `Git`
    * Adopting `Git`
<!-- chapter: core-git-concepts, duration: 2h -->
* Core `Git` Concepts
    * Always on a branch
    * Everything is SHA1 (files, changes, tags, branches)
    * Everything has a parent except first change.
    * Never store anything twice
    * `SHA` includes all history
    * `SHA` is unique in the world
<!-- chapter: git-basics, duration: 3h -->
* `Git` basics
    * Setting up a local repository
    * Setting up a client to a repository
        * local
        * remote
    * The staging area
    * Making your first change
    * Committing
    * Seeing history
    * Renaming, moving and removing files
<!-- chapter: configuring-git, duration: 1h -->
* Configuring `Git`
    * local and global config files
    * configuring `Git` commands
    * configuring signing
    * adding aliases
    * ignoring files
<!-- chapter: undoing-things, duration: 1h -->
* Undoing things
    * Staging area undoings
    * Undoing latest commit
    * Undoing last n commits
    * Cherry picking from latest commits
<!-- chapter: remote-repositories, duration: 1h -->
* Remote repositories
    * Working with a remote repository
    * Setting up / publishing a repository
    * Understanding the repository structure
    * Working with Multiple remotes
    * Working with `GitHub`
<!-- chapter: branches, duration: 1h -->
* Branches
    * Creating local branches
    * Working on local branches
    * Committing on local branches
    * Moving between local branches
    * Pruning branches
<!-- chapter: merging-changes, duration: 2h -->
* Merging changes
    * Fetch
    * Pull
    * Rebase
    * what is fast forwarding?
    * cherry picking
    * handling conflicts
        * basics
        * using merge tools
<!-- chapter: merge-vs-rebase, duration: 1h -->
* Merge vs Rebase
    * Which should you choose? (Rebase)
    * Why?
<!-- chapter: workflows, duration: 2h -->
* Workflows
    * `Git` does not force a workflow
    * feature branches
    * dev vs production
    * back porting changes
    * Examples of workflows
        * working on your own workflow
        * `Jenkins`
        * pull requests
<!-- chapter: getting-git-data, duration: 1h -->
* Getting `Git` data
    * `Git` log and it's many options
    * Visual tools
    * Using programming (example is `Python`)
<!-- chapter: under-the-hood, duration: 2h -->
* Under the hood
    * The `Git` object store and how it works
    * What happens `when` you add
    * What happens `when` you commit?
    * What happens `when` you create an annotated tag?
    * What happens `when` you branch?
<!-- chapter: worktrees, duration: 1h -->
* Worktrees
    * Why are they needed?
    * Creating a worktree
    * Working with worktrees
    * Pruning worktrees
<!-- chapter: tagging, duration: 1h -->
* Tagging
    * Why tag?
    * difference between annotates and non annotated tags
    * pushing and pulling tags
    * Using tags in other `Git` commands
<!-- chapter: rewriting-history, duration: 1h -->
* Rewriting History
    * Why you should never do it
    * How to do it anyway
<!-- chapter: stashing, duration: 1h -->
* Stashing
    * Why would you want stashing?
    * Creating and naming stashes
    * Apply a specific stash
    * Delete stashes
<!-- chapter: git-hooks, duration: 1h -->
* `Git` hooks
    * How to set up hooks?
    * What guarantees do you get?
<!-- chapter: external-git-tools, duration: 1h -->
* External `Git` tools
    * `GitHub` and `BitBucket`
    * `Gitlab`
    * `Git` and `IDEs`
    * `Git` and `Jenkins`, `Bamboo` etc

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
