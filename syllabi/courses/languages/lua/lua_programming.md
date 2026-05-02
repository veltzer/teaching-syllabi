---
tags:
  - languages:lua
  - concepts:programming
  - concepts:scripting
level: beginner
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: lua_programming -->
# `Lua` Programming

## Description
`Lua` is a lightweight, high-performance, embeddable scripting language. It is widely used in game development, embedded systems, and as a configuration and extension language in many applications. `Lua` combines simple procedural syntax with powerful data description constructs based on associative arrays and extensible semantics via metatables.

This course teaches `Lua` from the fundamentals through advanced topics including metatables, coroutines, the C `API`, and embedding `Lua` in applications. Students will also learn about LuaJIT and using `Lua` as a scripting language in game engines.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who want to embed a scripting language in their applications
* Game developers looking to use `Lua` for game scripting
* Systems programmers who need a lightweight extension language
* Anyone who wants to learn a fast and flexible scripting language

## Prerequisites
* Prior programming experience in another language such as C, `Python`, or `JavaScript`
* Basic understanding of programming concepts (variables, loops, functions)
* Familiarity with C is helpful for the C `API` sections

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Write `Lua` programs using tables, functions, and closures
* Implement object-oriented patterns with metatables
* Use coroutines for cooperative multitasking
* Integrate `Lua` with C applications using the C `API`
* Understand LuaJIT and its performance characteristics
* Script game engines and applications with `Lua`

## Outline
<!-- chapter: getting-started-with-lua, duration: 1h -->
* Getting Started with `Lua`
    * What is `Lua` and why use it?
    * Installing `Lua` and setting up the environment
    * Running `Lua` scripts and the interactive interpreter
    * Hello, World!
    * `Lua` ecosystem overview
<!-- chapter: lua-basics, duration: 1h -->
* `Lua` Basics
    * Data types (nil, boolean, number, string, function, table, userdata, thread)
    * Variables and scope (local vs global)
    * Operators (arithmetic, relational, logical, concatenation)
    * Type coercion and conversion
    * Comments and coding style
<!-- chapter: control-structures, duration: 1h -->
* Control Structures
    * if, elseif, else
    * `while-loops`
    * repeat-until loops
    * Numeric `for-loops`
    * Generic `for-loops` and iterators
    * break and return
<!-- chapter: functions-and-closures, duration: 1h -->
* Functions and Closures
    * Defining and calling functions
    * Multiple `return-values`
    * Variadic functions
    * First-class functions
    * Closures and upvalues
    * Tail calls
<!-- chapter: tables, duration: 1h -->
* Tables
    * Tables as arrays
    * Tables as dictionaries
    * Table constructors
    * Table manipulation functions
    * Sequences and the length operator
    * Nested tables and data structures
<!-- chapter: metatables-and-metamethods, duration: 2h -->
* Metatables and Metamethods
    * Understanding metatables
    * Arithmetic metamethods
    * Comparison metamethods
    * The __index and __newindex metamethods
    * The __tostring metamethod
    * Object-oriented programming with metatables
    * Inheritance via metatables
<!-- chapter: string-manipulation, duration: 1h -->
* String Manipulation
    * String library functions
    * Pattern matching
    * string.find, string.match, string.gmatch
    * String formatting with string.format
    * Captures and replacements
<!-- chapter: modules-and-packages, duration: 1h -->
* Modules and Packages
    * Creating modules
    * The require function
    * Module search paths
    * Package management with LuaRocks
    * Organizing larger projects
<!-- chapter: coroutines, duration: 1h -->
* Coroutines
    * What are coroutines?
    * Creating and resuming coroutines
    * Yielding values
    * Coroutine states
    * Producer-consumer patterns
    * Cooperative multitasking
<!-- chapter: file-i-o-and-error-handling, duration: 1h -->
* `File` `I/O` and Error Handling
    * Reading and writing files
    * The io library
    * The os library
    * Error handling with pcall and xpcall
    * Error messages and stack traces
    * Custom error objects
<!-- chapter: c-api-integration, duration: 2h -->
* C `API` Integration
    * Overview of the `Lua` C `API`
    * The `Lua` stack
    * Calling `Lua` from C
    * Calling C from `Lua`
    * Creating C modules for `Lua`
    * Userdata and metatables in C
<!-- chapter: embedding-lua, duration: 1h -->
* Embedding `Lua`
    * Embedding `Lua` in C/`C++` applications
    * Configuration files with `Lua`
    * Sandboxing and security considerations
    * Custom allocators
<!-- chapter: scripting-in-game-engines, duration: 1h -->
* Scripting in Game Engines
    * `Lua` in game development
    * Common game engine integrations
    * Scripting game logic
    * Event systems and callbacks
    * Performance considerations for games
<!-- chapter: luajit, duration: 1h -->
* LuaJIT
    * Introduction to LuaJIT
    * Performance characteristics and benchmarks
    * FFI (Foreign Function Interface)
    * LuaJIT extensions and limitations
    * `When` to use LuaJIT vs standard `Lua`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
