---
tags:
  - languages:cobol
  - concepts:programming
level: beginner
category: language
duration_hours: 40
audience:
  - audiences:developers
---
<!-- course: cobol_programming -->
# `COBOL` Programming

## Description
`COBOL` (Common Business-Oriented Language) remains one of the most widely deployed programming
languages in the world, powering critical systems in banking, insurance, and government.
Despite being over six decades old, billions of lines of `COBOL` code continue to process
trillions of dollars in transactions daily. This course provides a comprehensive introduction
to `COBOL` programming, from fundamental syntax and program structure through `file` handling,
data manipulation, and modular programming. Students will also learn how `COBOL` operates
on mainframe environments and explore strategies for modernizing legacy `COBOL` systems.
The course includes hands on exercises.

## Duration
40 hours / 5 days

## Intended Audience
* Developers entering the mainframe or enterprise computing space.
* Programmers tasked with maintaining or modernizing legacy `COBOL` systems.
* IT professionals working in banking, finance, insurance, or government sectors.

## Prerequisites
* Basic understanding of programming concepts (variables, control flow, data types).
* Familiarity with a command-line interface.

## Objectives
* Understand `COBOL` program structure and its four divisions
* Write `COBOL` programs that process business data
* Work with sequential, indexed, and relative files
* Use tables, string manipulation, and subprograms
* Navigate mainframe environments and JCL basics
* Evaluate strategies for modernizing `COBOL` applications

## Outline
<!-- chapter: introduction-to-cobol, duration: 3h -->
* Introduction to `COBOL`
    * History and evolution of `COBOL`
    * Relevance of `COBOL` in banking and finance
    * The `COBOL` ecosystem today
    * Setting up a `COBOL` development environment
    * Compiling and running a `COBOL` program
<!-- chapter: program-structure, duration: 3h -->
* Program Structure
    * The four divisions: Identification, Environment, Data, Procedure
    * Sections and paragraphs
    * `COBOL` coding format and conventions
    * Comments and documentation
    * Hello World in `COBOL`
<!-- chapter: data-types-and-the-picture-clause, duration: 3h -->
* Data Types and the PICTURE Clause
    * Numeric, alphabetic, and alphanumeric data items
    * The PICTURE clause and data formatting
    * Level numbers and data hierarchy
    * USAGE clause (DISPLAY, COMP, COMP-3)
    * Figurative constants and literals
    * Working-Storage Section vs Local-Storage Section
<!-- chapter: arithmetic-and-data-movement, duration: 3h -->
* Arithmetic and Data Movement
    * MOVE statement and data conversion
    * ADD, SUBTRACT, MULTIPLY, DIVIDE
    * COMPUTE statement
    * Arithmetic precision and rounding
    * The `ON SIZE ERROR` clause
<!-- chapter: control-flow, duration: 3h -->
* Control Flow
    * IF / ELSE / END-IF
    * EVALUATE (case/switch equivalent)
    * PERFORM and `PERFORM VARYING`
    * `PERFORM UNTIL` and `PERFORM THRU`
    * `GO TO` and structured programming considerations
    * Paragraphs and sections as control units
<!-- chapter: file-handling, duration: 3h -->
* `File` Handling
    * `File` organization: sequential, indexed, relative
    * SELECT, FD, and `file` description entries
    * OPEN, READ, WRITE, REWRITE, CLOSE
    * Sequential `file` processing
    * Indexed `file` processing with READ / START / DELETE
    * Relative `file` processing
    * `File` status codes and error handling
<!-- chapter: input-output, duration: 2h -->
* Input/Output
    * ACCEPT and DISPLAY statements
    * Screen Section for formatted `I/O`
    * Working with dates and times
    * `ACCEPT FROM` system variables
<!-- chapter: tables-and-the-occurs-clause, duration: 3h -->
* Tables and the OCCURS Clause
    * Defining tables with OCCURS
    * Single and multi-dimensional tables
    * `OCCURS DEPENDING ON` for variable-length tables
    * Table indexing vs subscripting
    * SEARCH and `SEARCH ALL`
    * Sorting table data
<!-- chapter: string-handling, duration: 2h -->
* String Handling
    * STRING statement
    * UNSTRING statement
    * INSPECT (TALLYING, REPLACING, CONVERTING)
    * Reference modification
<!-- chapter: copybooks-and-modular-programming, duration: 2h -->
* Copybooks and Modular Programming
    * The COPY statement
    * Copybook libraries and management
    * REPLACING option in COPY
    * Code reuse and standardization
<!-- chapter: subprograms, duration: 3h -->
* Subprograms
    * CALL statement
    * Passing parameters (BY REFERENCE, BY CONTENT, BY VALUE)
    * CANCEL statement
    * Nested programs
    * Static vs dynamic calls
<!-- chapter: cobol-on-mainframes, duration: 3h -->
* `COBOL` on Mainframes
    * Introduction to JCL (Job Control Language)
    * TSO/ISPF environment overview
    * Submitting and monitoring batch jobs
    * Working with datasets and VSAM files
    * Debugging with tools like Xpediter and CEDF
<!-- chapter: cobol-on-modern-platforms, duration: 2h -->
* `COBOL` on Modern Platforms
    * GnuCOBOL (open-source `COBOL` compiler)
    * `COBOL` on `Linux` and cloud environments
    * `COBOL` in containers
    * IDE support and modern tooling
<!-- chapter: debugging-and-testing, duration: 2h -->
* Debugging and Testing
    * Common `COBOL` errors and diagnostics
    * Debugging techniques and tools
    * Unit testing `COBOL` programs
    * Test data management
<!-- chapter: modernization-strategies, duration: 3h -->
* Modernization Strategies
    * Wrapping `COBOL` programs with APIs
    * Screen scraping and integration middleware
    * Incremental rewriting approaches
    * `COBOL` to `Java`/`C#` conversion tools
    * `Microservices` integration with legacy systems
    * Planning a modernization roadmap

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
