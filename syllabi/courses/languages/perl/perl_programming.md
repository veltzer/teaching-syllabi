---
tags:
  - languages:perl
  - concepts:programming
  - concepts:scripting
level: beginner
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: perl_programming -->
# `Perl` Programming

## Description
`Perl` is a highly capable, feature-rich programming language with a long history of use in text processing, system administration, web development, and bioinformatics. Known for its powerful regular expression support and the motto "There's more than one way to do it," `Perl` remains a practical choice for many scripting and automation tasks.

This course covers `Perl` from the basics through advanced topics including object-oriented programming with Moose/Moo, CPAN module usage, text processing, and modern `Perl` best practices. Students will gain hands-on experience writing real-world `Perl` scripts and applications.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who need to write scripts for text processing and automation
* System administrators looking for a powerful scripting language
* Programmers maintaining or extending existing `Perl` codebases
* Anyone who wants to learn a versatile scripting language

## Prerequisites
* Prior programming experience in another language such as `Python`, `Bash`, or `C`
* Basic familiarity with the command line
* Understanding of fundamental programming concepts

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Bash` Scripting (or equivalent experience)

## Objectives
* Write `Perl` programs using scalars, arrays, and hashes
* Master `Perl` regular expressions for text processing
* Use subroutines, references, and data structures effectively
* Leverage CPAN for modules and libraries
* Apply object-oriented programming with Moose and Moo
* Write tests with Test::More

## Outline
<!-- chapter: getting-started-with-perl, duration: 1h -->
* Getting Started with `Perl`
    * What is `Perl` and its history
    * Installing `Perl` and setting up the environment
    * Running `Perl` scripts
    * The perldoc documentation system
    * Hello, World!
    * Strict and warnings pragmas
<!-- chapter: scalars, duration: 1h -->
* Scalars
    * Numbers and strings
    * Scalar variables
    * Operators (arithmetic, string, comparison)
    * String interpolation
    * Undefined values and undef
    * Context (scalar vs list)
<!-- chapter: arrays-and-lists, duration: 1h -->
* Arrays and Lists
    * Creating and accessing arrays
    * `Array` functions (push, pop, shift, unshift, splice)
    * `Array` slices
    * Sorting arrays
    * qw shortcut
    * Looping over arrays
<!-- chapter: hashes, duration: 1h -->
* Hashes
    * Creating and accessing hashes
    * Hash functions (keys, values, each, exists, delete)
    * Hash slices
    * Iterating over hashes
    * Using hashes for counting and lookups
<!-- chapter: regular-expressions, duration: 2h -->
* Regular Expressions
    * Pattern matching with m//
    * Substitution with s///
    * Character classes and quantifiers
    * Anchors and boundaries
    * Grouping and capturing
    * Non-greedy matching
    * Lookahead and lookbehind
    * Named captures
    * Transliteration with tr///
<!-- chapter: control-structures, duration: 1h -->
* Control Structures
    * if, elsif, else, unless
    * `while-loop`, `until-loop`, `for-loop`, foreach
    * Loop control (next, last, redo)
    * Statement modifiers
    * given/`when` (switch)
    * Ternary operator
<!-- chapter: subroutines-and-references, duration: 2h -->
* Subroutines and References
    * Defining and calling subroutines
    * Arguments and `return-values`
    * The @_ `array`
    * References (scalar, `array`, hash)
    * Anonymous references
    * Dereferencing
    * Nested data structures
    * The `ref` function
<!-- chapter: file-i-o, duration: 2h -->
* `File` `I/O`
    * Opening and closing files
    * Reading from files (line by line, slurping)
    * Writing and appending to files
    * Filehandle operations
    * Directory operations
    * `File` tests (-e, -f, -d, -`r`, -w)
    * Working with STDIN, STDOUT, STDERR
<!-- chapter: modules-and-cpan, duration: 2h -->
* Modules and CPAN
    * Using modules with use and `require`
    * The @INC path
    * Creating your own modules
    * Introduction to CPAN
    * Installing modules with cpanm
    * Popular CPAN modules
    * local::lib for local installations
<!-- chapter: object-oriented-perl, duration: 2h -->
* Object-Oriented `Perl`
    * Traditional `Perl` `OOP` (bless, constructors, methods)
    * Introduction to Moose
    * Attributes and types in Moose
    * Roles and composition
    * Moo as a lightweight alternative
    * Method modifiers (before, after, around)
    * Type constraints and coercions
<!-- chapter: text-processing, duration: 2h -->
* Text Processing
    * Line-by-line processing
    * Field splitting and joining
    * Parsing structured text (`CSV`, `TSV`)
    * Working with `JSON` and `YAML`
    * `Unicode` and encoding
    * Report generation with format
<!-- chapter: perl-one-liners, duration: 1h -->
* `Perl` One-Liners
    * Command-line switches (-e, -n, -p, -i, -a, -F)
    * In-place editing
    * Field processing
    * Common one-liner patterns
    * Replacing `sed`, `awk`, and `grep` with `Perl`
<!-- chapter: system-administration-scripting, duration: 2h -->
* System Administration Scripting
    * Running external commands (system, backticks, open)
    * Process management
    * `File` and directory manipulation
    * Log `file` analysis
    * Automating system tasks
    * Working with environment variables
<!-- chapter: testing-with-test-more, duration: 2h -->
* Testing with Test::More
    * Writing test files
    * Test functions (ok, is, isnt, like, is_deeply)
    * Test plans and subtests
    * Running tests with prove
    * Test-driven development workflow
    * Mocking and test fixtures
<!-- chapter: modern-perl-best-practices, duration: 2h -->
* Modern `Perl` Best Practices
    * Use of strict and warnings
    * Proper error handling with Try::Tiny
    * `Perl`::Critic for code quality
    * `Perl`::Tidy for code formatting
    * Modern `Perl` idioms
    * Version-specific features

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
