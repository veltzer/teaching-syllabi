---
tags:
  - languages:bash
  - practices:scripting
  - infrastructure:linux
  - practices:automation
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: bash_scripting -->
# `Bash` scripting

## Description
`Bash` is the de-facto standard for scripting in the `Linux` world and is used by many and understood by few.
This course intends to change this by explaining how `bash` works in detail and how to overcome many of the
flaws in `bash` design to create well written, easy to maintain, reliable and deterministic scripts.

## Duration
24 hours / 3 days

## Intended Audience
* system administrators and `DevOps` engineers
* developers who want to automate tasks using shell scripts

## Prerequisites
* familiarity with the `Linux` command line

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of `Bash`` scripting
* gain practical knowledge of Theory
* gain practical knowledge of How does the shell run things?
* gain practical knowledge of Basic shell features

## Outline
<!-- chapter: theory, duration: 1h -->
* Theory
    * What is a shell ?
    * Why do we need a shell?
    * How is a shell better than a GUI?
    * The shell as a game.
    * Shell families.
    * The history of `ksh` and `bash`.
<!-- chapter: how-does-the-shell-run-things, duration: 1h -->
* How does the shell run things?
    * Command line parsing
    * The PATH environment variable.
    * Built in commands
<!-- chapter: basic-shell-features, duration: 1h -->
* Basic shell features
    * Several commands in one line with semi colons
    * Variable substitution
    * Escaping the shell
<!-- chapter: the-return-code, duration: 1h -->
* The return code
    * return code on the command line
    * return code if a script
<!-- chapter: environment-and-shell-variables, duration: 1h -->
* Environment and shell variables
    * Defining
    * Deleting
    * Demoting and promoting
    * Checking if they exist
<!-- chapter: redirection, duration: 1h -->
* Redirection
    * Redirecting standard output
    * Redirecting standard error
    * Redirecting standard input
    * Doing other tricks with redirection
<!-- chapter: handling-errors, duration: 1h -->
* Handling errors
    * Errors from a single line
    * &&
    * -e flag and `set -e`
<!-- chapter: globbing, duration: 1h -->
* Globbing
    * asterisk
    * question mark
    * characters classes
    * negation
    * several options
<!-- chapter: expansion, duration: 1h -->
* Expansion
    * curly braces and comma
    * several options
<!-- chapter: writing-you-first-script, duration: 1h -->
* Writing you first script
    * editors
    * shbang line
    * chmodding and why
    * extensions for scripts
    * failure in a script
    * prohibiting failure in a script
    * return code of an entire script
    * exiting early with code
    * using wrong variable names
    * using strict variable names
    * debugging your script
<!-- chapter: syntax, duration: 1h -->
* Syntax
    * Conditionals.
        * no brace
        * left straight brace
        * two left straight braces
    * `while-loops`
    * `for-loops`
<!-- chapter: pipes, duration: 1h -->
* Pipes
    * How to use them
    * How do they work
    * Handling pools
<!-- chapter: io, duration: 1h -->
* IO
    * reading from a `file`
    * writing to a `file`
    * writing data to process
    * reading data from process
<!-- chapter: redirection-in-scripts, duration: 1h -->
* Redirection in scripts
    * Redirecting for entire scripts
    * Restoring from redirection
<!-- chapter: multi-processing, duration: 1h -->
* Multi processing
    * launching sub processes
    * getting their return code
    * launching more than one sub process and collecting their codes
<!-- chapter: writing-bash-functions, duration: 1h -->
* Writing `bash` functions
    * return code of functions
    * passing parameters to functions
    * passing parameters by reference
<!-- chapter: using-variable-types, duration: 1h -->
* Using variable types
    * strings
    * arrays
    * associative arrays
<!-- chapter: doing-arithmetic, duration: 1h -->
* Doing arithmetic
    * integer arithmetic
    * floating point arithmetic
<!-- chapter: using-arrays, duration: 1h -->
* Using Arrays
    * Creating arrays
    * Adding elements
    * Iterating arrays
    * Removing elements
    * Checking if an element is in the `array`
<!-- chapter: using-associative-arrays, duration: 1h -->
* Using Associative Arrays
    * Creating associative arrays
    * Adding key, value pairs
    * Iterating associative arrays
<!-- chapter: timing, duration: 1h -->
* Timing
    * The basic tools
    * The precision
<!-- chapter: object-oriented-programming, duration: 1h -->
* Object oriented programming
    * Using associative arrays to create objects
<!-- chapter: test-harnesses, duration: 1h -->
* Test harnesses
<!-- chapter: aliases, duration: 1h -->
* Aliases

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
