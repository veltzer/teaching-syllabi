---
tags:
  - languages:perl
  - concepts:programming
  - practices:scripting
level: advanced
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
---
<!-- course: advanced_perl -->
# Advanced `Perl`

## Description
`Perl` remains a powerful language for text processing, system administration, and rapid prototyping. This advanced course dives deep into `Perl`'s sophisticated features including references, complex data structures, object-oriented programming with Moose/Moo, and the rich CPAN ecosystem. Students will master regular expressions, learn effective testing practices, and optimize `Perl` code for production use.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who need advanced `Perl` skills for complex applications
* System administrators automating infrastructure with `Perl`
* Developers maintaining or extending existing `Perl` codebases

## Prerequisites
* Working knowledge of `Perl` basics (variables, control flow, subroutines)
* Experience writing `Perl` scripts

## Objectives
* Use references and build complex data structures
* Master `Perl` regular expressions for advanced text processing
* Write object-oriented `Perl` using Moose and Moo
* Leverage CPAN modules effectively
* Test `Perl` code with Test::More and related frameworks
* Optimize `Perl` code for performance

## Outline
<!-- chapter: references-and-complex-data-structures, duration: 2h -->
* References and Complex Data Structures
    * Scalar, `array`, and hash references
    * Anonymous references
    * Nested data structures
    * References to subroutines
    * Dereferencing techniques
    * Data::Dumper for debugging
    * Weak references
<!-- chapter: regular-expressions-mastery, duration: 2h -->
* Regular Expressions Mastery
    * Advanced quantifiers and grouping
    * Lookahead and lookbehind assertions
    * Named captures
    * Non-greedy matching
    * Regex modifiers (/x, /s, /m, /e)
    * Regex debugging
    * `Unicode` and regex
    * Common patterns and recipes
<!-- chapter: object-oriented-perl, duration: 3h -->
* Object-Oriented `Perl`
    * Traditional `Perl` `OOP` (bless, constructors, methods)
    * Moose framework
        * Attributes (has, is, `isa`)
        * Type constraints
        * Roles and composition
        * Method modifiers (before, after, around)
        * Inheritance and overriding
    * Moo (lightweight alternative)
    * Moo vs Moose tradeoffs
<!-- chapter: cpan-ecosystem, duration: 1h -->
* CPAN Ecosystem
    * Finding and evaluating modules
    * Installing modules (cpanm, carton)
    * Managing dependencies
    * Key modules for common tasks
    * Local::Lib for user installations
    * Pinning module versions
<!-- chapter: file-i-o-and-process-management, duration: 1h -->
* `File` `I/O` and Process Management
    * Advanced `file` handling (open modes, binmode)
    * Directory traversal (`File`::`Find`, Path::Tiny)
    * Temporary files and locking
    * Process creation (system, exec, backticks)
    * `IPC` (pipes, signals)
    * Forking and parallel processing
<!-- chapter: networking-and-database-access, duration: 1h -->
* Networking and Database Access
    * Socket programming basics
    * LWP and `HTTP`::Tiny for web requests
    * DBI for database access
    * Prepared statements and placeholders
    * DBD drivers (`MySQL`, `PostgreSQL`, `SQLite`)
    * Connection management
<!-- chapter: testing-with-test-more, duration: 2h -->
* Testing with Test::More
    * Test structure and organization
    * ok, is, is_deeply, like, throws_ok
    * Test plans and subtests
    * Mock objects (Test::MockObject)
    * Test::Class for `xUnit`-style tests
    * prove and TAP protocol
    * Code coverage with Devel::Cover
<!-- chapter: packaging-and-distribution, duration: 1h -->
* Packaging and Distribution
    * Module structure and naming
    * `Makefile`.PL and Build.PL
    * Writing documentation with POD
    * Dist::Zilla for distribution management
    * Publishing to CPAN
<!-- chapter: perl-one-liners, duration: 1h -->
* `Perl` One-Liners
    * Command-line switches (-e, -n, -p, -i, -a, -F)
    * Field processing
    * In-place editing
    * Common one-liner patterns
<!-- chapter: performance-optimization, duration: 2h -->
* Performance Optimization
    * Benchmarking with Benchmark module
    * Profiling with Devel::NYTProf
    * Memoization
    * XS and Inline::`C` for critical paths
    * Memory optimization
    * Identifying and resolving bottlenecks

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
