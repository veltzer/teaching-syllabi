---
tags:
  - languages:bash
  - practices:scripting
  - infrastructure:linux
  - practices:automation
level: intermediate
category: language
duration_days: 3
audience:
  - audiences:developers
  - practices:devops
  - audiences:sysadmins
---
# `Bash` scripting

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Bash` is the de-facto standard for scripting in the `Linux` world and is used by many and understood by few.
This course intends to change this by explaining how bash works in detail and how to overcome many of the
flaws in bash design to create well written, easy to maintain, reliable and deterministic scripts.

## Duration
24 hours / 3 days

## Intended Audience
* system administrators and DevOps engineers
* developers who want to automate tasks using shell scripts

## Prerequisites
* familiarity with the Linux command line

## Objectives
* understand the core concepts and principles of Bash` scripting
* gain practical knowledge of Theory
* gain practical knowledge of How does the shell run things?
* gain practical knowledge of Basic shell features

## Outline
* Theory
    * What is a shell ?
    * Why do we need a shell?
    * How is a shell better than a GUI?
    * The shell as a game.
    * Shell families.
    * The history of ksh and bash.
* How does the shell run things?
    * Command line parsing
    * The `PATH` environment variable.
    * Built in commands
* Basic shell features
    * Several commands in one line with semi colons
    * Variable substitution
    * Escaping the shell
* The return code
    * return code on the command line
    * return code if a script
* Environment and shell variables
    * Defining
    * Deleting
    * Demoting and promoting
    * Checking if they exist
* Redirection
    * Redirecting standard output
    * Redirecting standard error
    * Redirecting standard input
    * Doing other tricks with redirection
* Handling errors
    * Errors from a single line
    * `&&`
    * `-e` flag and `set -e`
* Globbing
    * asterisk
    * question mark
    * characters classes
    * negation
    * several options
* Expansion
    * curly braces and comma
    * several options
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
* Syntax
    * Conditionals.
        * no brace
        * left straight brace
        * two left straight braces
    * `while` loops
    * `for` loops
* Pipes
    * How to use them
    * How do they work
    * Handling pools
* IO
    * reading from a file
    * writing to a file
    * writing data to process
    * reading data from process
* Redirection in scripts
    * Redirecting for entire scripts
    * Restoring from redirection
* Multi processing
    * launching sub processes
    * getting their return code
    * launching more than one sub process and collecting their codes
* Writing bash functions
    * return code of functions
    * passing parameters to functions
    * passing parameters by reference
* Using variable types
    * strings
    * arrays
    * associative arrays
* Doing arithmetic
    * integer arithmetic
    * floating point arithmetic
* Using Arrays
    * Creating arrays
    * Adding elements
    * Iterating arrays
    * Removing elements
    * Checking if an element is in the array
* Using Associative Arrays
    * Creating associative arrays
    * Adding key, value pairs
    * Iterating associative arrays
* Timing
    * The basic tools
    * The precision
* Object oriented programming
    * Using associative arrays to create objects
* Test harnesses
* Aliases

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
