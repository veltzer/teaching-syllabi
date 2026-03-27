---
tags:
  - git
  - version-control
level: beginner
category: version-control
duration_days: 3
audience:
  - developers
  - devops
---
# Introduction to `Git`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Git` is the de-facto standard source control system for the tech industry and is one of the most flexible software tools to be found. Any developer or `DevOps` person probably needs at least a basic understanding of `Git` to get going and this course is intended for that purpose.

This course covers all of the fundamental operations an experienced coder would use on a daily basis. The course begins with an introduction to `Git` and a comparison of `Git` to other version control systems. It then transitions into the nuts-and-bolts of working with `Git`, including everything from setting up a repository to advanced topics like branching and merging.

Because the industry sometimes misuses git this course is also focuses on clearing up muddled understanding of git: the staging area, merge vs rebase, history management, branching and more

## Duration
24 hours/3 days

## Intended Audience
* Any software developer or `DevOps` who needs to work with `Git` or understand `Git` better.
* Any software developer who has worked with `Git` but wants a deeper understanding of it.
* System administrators who are moving to `DevOps` in general or `Git` specifically.
* Any manager who needs to understand what is possible and how to manage git using projects.

## Prerequisites
* Tech affinity.

## Objectives
* Setup and use git
* Understand and use `Git`'s branching features correctly and effectively
* Decide on which workflows to use when using `Git`

## Outline
* Introduction to `Git`
    * History of `Git`
    * Who is using `Git`
    * Adopting `Git`
* Core `Git` Concepts
    * Always on a branch
    * Everything is SHA1 (files, changes, tags, branches)
    * Everything has a parent except first change.
    * Never store anything twice
    * SHA includes all history
    * SHA is unique in the world
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
* Configuring `Git`
    * local and global config files
    * configuring `Git` commands
    * configuring signing
    * adding aliases
    * ignoring files
* Undoing things
    * Staging area undoings
    * Undoing latest commit
    * Undoing last n commits
    * Cherry picking from latest commits
* Remote repositories
    * Working with a remote repository
    * Setting up / publishing a repository
    * Understanding the repository structure
    * Working with Multiple remotes
    * Working with GitHub
* Branches
    * Creating local branches
    * Working on local branches
    * Committing on local branches
    * Moving between local branches
    * Pruning branches
* Merging changes
    * Fetch
    * Pull
    * Rebase
    * what is fast forwarding?
    * cherry picking
    * handling conflicts
        * basics
        * using merge tools
* Merge vs Rebase
    * Which should you choose? (Rebase)
    * Why?
* Workflows
    * `Git` does not force a workflow
    * feature branches
    * dev vs production
    * back porting changes
    * Examples of workflows
        * working on your own workflow
        * `Jenkins`
        * pull requests
* Getting `Git` data
    * `Git` log and it's many options
    * Visual tools
    * Using programming (example is `Python`)
* Under the hood
    * The `Git` object store and how it works
    * What happens when you add
    * What happens when you commit?
    * What happens when you create an annotated tag?
    * What happens when you branch?
* Worktrees
    * Why are they needed?
    * Creating a worktree
    * Working with worktrees
    * Pruning worktrees
* Tagging
    * Why tag?
    * difference between annotates and non annotated tags
    * pushing and pulling tags
    * Using tags in other `Git` commands
* Rewriting History
    * Why you should never do it
    * How to do it anyway
* Stashing
    * Why would you want stashing?
    * Creating and naming stashes
    * Apply a specific stash
    * Delete stashes
* `Git` hooks
    * How to set up hooks?
    * What guarantees do you get?
* External `Git` tools
    * GitHub and BitBucket
    * Gitlab
    * `Git` and `IDEs`
    * `Git` and `Jenkins`, Bamboo etc

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
