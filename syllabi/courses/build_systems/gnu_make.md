---
tags:
  - tools:make
  - languages:c
  - practices:build-systems
  - infrastructure:linux
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: gnu_make -->
# GNU `Make`

## Description
`GNU make` is the most widely used build system in the open source world but also has the most arcane syntax
while being the most flexible and misunderstood. This course will get you started using `GNU make` correctly.

## Duration
16 hours / 2 days

## Intended Audience
* `C` programmers who would like to write their build system in `GNU make`.
* Anyone wanting to use `GNU make` to create build systems for any other language.

## Prerequisites
* Basic command line experience
* Understanding of compilation process
* Text editor familiarity
* `Git` basics (optional)

## Objectives
* Create and maintain Makefiles
* Understand `Make`'s execution model
* Implement efficient build systems
* Debug `Make`-related issues
* Apply best practices in build automation

## Outline
<!-- chapter: introduction-to-make, duration: 2h -->
* Introduction to `Make`
    * What is `Make` and why use it?
    * Build automation concepts
    * `Make` vs other build tools
    * First `Makefile` example
<!-- chapter: basic-makefile-structure, duration: 2h -->
* Basic `Makefile` Structure
    * Targets and prerequisites
    * Rules and recipes
    * Basic syntax
    * Running `make` commands
    * Implicit rules
    * Exercise: Creating your first `Makefile`
<!-- chapter: variables-and-functions, duration: 2h -->
* Variables and Functions
    * Variable types and assignment
    * Built-in variables
    * Function syntax
    * Common functions
    * Pattern substitution
    * Exercise: Using variables and functions
<!-- chapter: practical-applications, duration: 2h -->
* Practical Applications
    * Building `C`/`C++` projects
    * Managing multiple source files
    * Object files and dependencies
    * Exercise: Building a multi-`file` project
<!-- chapter: advanced-make-features, duration: 2h -->
* Advanced `Make` Features
    * Pattern rules
    * Static pattern rules
    * Double-colon rules
    * Order-only prerequisites
    * Exercise: Implementing pattern rules
<!-- chapter: dependencies-and-conditionals, duration: 2h -->
* Dependencies and Conditionals
    * Automatic dependency generation
    * Conditional directives
    * Include statements
    * Exercise: Managing complex dependencies
<!-- chapter: makefile-best-practices, duration: 2h -->
* `Makefile` Best Practices
    * Organizing large projects
    * Phony targets
    * Error handling
    * Debugging techniques
    * Parallel execution
    * Exercise: Optimizing Makefiles
<!-- chapter: real-world-applications, duration: 2h -->
* Real-World Applications
    * Project structure examples
    * Common patterns and idioms
    * Integration with other tools
    * Exercise: Creating a complete build system
    * Review of key concepts
    * Additional resources

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
