---
tags:
  - concepts:programming
  - concepts:scripting
  - practices:automation
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:testers
---
<!-- course: tcl_programming -->
# Tcl/Tk Programming

## Description
Tcl (Tool Command Language) is a dynamic scripting language widely used in embedded systems, test automation, and rapid prototyping. Paired with Tk, it provides a cross-platform GUI toolkit. This course covers the Tcl language from fundamentals through advanced topics including namespaces, packages, GUI development with Tk, automation with Expect, and embedding Tcl in C applications.

## Duration
16 hours / 2 days

## Intended Audience
* Developers working with Tcl-based tools and environments
* Embedded engineers using Tcl for testing and automation
* Testers building automated test frameworks with Tcl and Expect

## Prerequisites
* Basic programming experience in any language
* Familiarity with command-line interfaces

## Objectives
* Write Tcl scripts using core language features
* Manipulate strings, lists, and dictionaries
* Build graphical user interfaces with Tk
* Automate interactive applications using Expect
* Organize code with namespaces and packages
* Embed Tcl as a scripting engine in C programs

## Outline
<!-- chapter: introduction-to-tcl, duration: 1h -->
* Introduction to Tcl
    * History and design philosophy
    * Everything is a string
    * The Tcl interpreter (tclsh, wish)
    * Command structure and substitution rules
    * Comments and script organization
<!-- chapter: variables-expressions-and-data-types, duration: 1h -->
* Variables, Expressions, and Data Types
    * Variable assignment (set, unset)
    * String representation of data
    * Numeric expressions (expr)
    * Boolean values
    * Arrays (associative)
    * Variable scope and upvar/uplevel
<!-- chapter: control-flow, duration: 1h -->
* Control Flow
    * if, elseif, else
    * switch
    * `while-loop`, `for-loop`, foreach
    * break and continue
    * catch and error handling
    * try/finally
<!-- chapter: procedures, duration: 1h -->
* Procedures
    * Defining procedures (proc)
    * Arguments and default values
    * Variable-length argument lists (args)
    * `Return-values`
    * Recursion
    * Renaming and wrapping commands
<!-- chapter: string-manipulation, duration: 1h -->
* String Manipulation
    * String commands (string length, index, range, map, trim)
    * String matching and comparison
    * Format and scan
    * Append and string building
    * `Unicode` handling
<!-- chapter: lists-and-dictionaries, duration: 1h -->
* Lists and Dictionaries
    * List creation and manipulation (list, lappend, linsert, lreplace)
    * List searching (lsearch) and sorting (lsort)
    * List iteration
    * Dictionaries (dict create, set, get, for, filter)
    * Nested data structures
<!-- chapter: file-i-o, duration: 1h -->
* `File` `I/O`
    * Opening and closing files (open, close)
    * Reading and writing (gets, puts, read)
    * `File` positioning (seek, tell)
    * `File` system commands (file exists, mkdir, delete, copy)
    * Glob for file matching
<!-- chapter: regular-expressions, duration: 1h -->
* Regular Expressions
    * regexp command
    * regsub command
    * Capture groups
    * Advanced regex features
    * Performance considerations
<!-- chapter: namespaces-and-packages, duration: 2h -->
* Namespaces and Packages
    * Namespace creation and management
    * Exporting and importing commands
    * Namespace variables
    * Package creation (package provide, package require)
    * pkgIndex.tcl
    * Package distribution
<!-- chapter: tk-gui-programming, duration: 2h -->
* Tk GUI Programming
    * Tk widget overview
    * Geometry managers (pack, grid, place)
    * Buttons, labels, and entry widgets
    * Text and canvas widgets
    * Menus and dialogs
    * Listbox and treeview (ttk)
    * Themed widgets (ttk)
    * Binding events to widgets
<!-- chapter: event-driven-programming, duration: 1h -->
* Event-Driven Programming
    * The event loop
    * After command for timers
    * Fileevent for `I/O` events
    * Vwait and tkwait
    * Interprocess communication with sockets
<!-- chapter: expect-for-automation, duration: 1h -->
* Expect for Automation
    * Spawning processes
    * Expect, send, and interact
    * Pattern matching and timeouts
    * Automating `SSH`, `FTP`, and telnet sessions
    * Building test harnesses
<!-- chapter: embedding-tcl-in-c, duration: 2h -->
* Embedding Tcl in C
    * The Tcl C `API`
    * Creating an interpreter (Tcl_CreateInterp)
    * Evaluating scripts from C
    * Registering custom commands
    * Passing data between C and Tcl
    * Building loadable extensions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
