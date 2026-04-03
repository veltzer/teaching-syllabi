---
tags:
  - languages:nim
  - concepts:compiled
  - concepts:systems-programming
  - concepts:meta-programming
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:systems-programmers
---
<!-- course: nim_programming -->
# `Nim` Programming

## Description
`Nim` is a statically typed, compiled systems programming language that combines the readability of `Python`, the performance of `C`, and a uniquely powerful macro system for compile-time metaprogramming.
`Nim` transpiles to `C`, `C++`, or `JavaScript`, enabling deployment targets ranging from microcontrollers to web browsers.
Its hygienic macros and template system allow developers to extend the language itself and build zero-overhead abstractions.
This course covers `Nim` from first programs through its type system, memory management options, `async`/`await` concurrency, `C` interoperability, and practical tooling.

## Duration
24 hours / 3 days

## Intended Audience
* Systems programmers looking for a more ergonomic alternative to `C`/`C++`
* Developers interested in metaprogramming and compile-time code generation
* Engineers exploring modern compiled language alternatives to `Rust` or `Go`

## Prerequisites
* `Solid` experience in at least one compiled or systems programming language
* Basic understanding of memory management concepts

## Objectives
* Write idiomatic `Nim` code using its type system and procedural style
* Apply object-oriented features using `Nim`'s type hierarchy
* Use generics and templates for reusable, type-safe abstractions
* Write macros to extend the language at compile time
* Understand `Nim`'s memory management — `GC` options and manual allocation
* Interoperate with `C` and `C++` libraries
* Write concurrent programs using `async`/`await`

## Outline
<!-- chapter: introduction-to-nim, duration: 2h -->
* Introduction to `Nim`
    * History and design goals
    * `Nim` vs `C`, `Rust`, `Go` — `when` to choose `Nim`
    * Installation and toolchain (`nim`, `nimble`)
    * Your first `Nim` program
    * Compiling and running

<!-- chapter: types-and-variables, duration: 2h -->
* Types and Variables
    * Primitive types and type aliases
    * Variables — `var`, `let`, `const`
    * Strings and `char`
    * Arrays, sequences, and tuples
    * Type inference

<!-- chapter: control-flow-and-procedures, duration: 3h -->
* Control Flow and Procedures
    * `if`, `elif`, `else`, `case`
    * `for` and `while` loops
    * Procedure definitions and `return-values`
    * Named parameters and default values
    * Iterators
    * `result` variable

<!-- chapter: object-oriented-features, duration: 2h -->
* Object-Oriented Features
    * Objects and inheritance
    * Method dispatch
    * Interfaces via concepts (experimental)
    * `ref` objects vs value objects
    * Operator overloading

<!-- chapter: generics-and-templates, duration: 3h -->
* Generics and Templates
    * Generic procedures and types
    * Constraints with concepts
    * Templates — hygienic substitution
    * `When` to use templates vs generics

<!-- chapter: macros-and-meta-programming, duration: 3h -->
* Macros and Meta-programming
    * `Nim`'s AST and compile-time representation
    * Writing simple macros
    * `quote do:` blocks
    * Compile-time execution with `static`
    * Practical macro examples — DSLs and code generation

<!-- chapter: memory-management-and-garbage-collection, duration: 2h -->
* Memory Management and Garbage Collection
    * `Nim`'s default ORC garbage collector
    * Manual memory management with `alloc`/`dealloc`
    * `ptr` vs `ref`
    * Destructors and `=destroy`
    * Compile-time memory analysis

<!-- chapter: concurrency-with-async-await, duration: 2h -->
* Concurrency with `Async`/`Await`
    * `asyncdispatch` event loop
    * `async` procedures and `await`
    * Futures
    * `Async` `file` and network `I/O`
    * Threads with `threadpool`

<!-- chapter: c-and-cpp-interoperability, duration: 2h -->
* `C` and `C++` Interoperability
    * Importing `C` headers with `importc`
    * Wrapping `C++` classes
    * Emitting raw `C` code
    * Practical binding patterns

<!-- chapter: testing-and-tooling, duration: 2h -->
* Testing and Tooling
    * `unittest` module
    * `testament` test runner
    * `nimble` package manager
    * Debugging with `GDB`
    * Profiling `Nim` programs

<!-- chapter: nim-for-systems-programming, duration: 1h -->
* `Nim` for Systems Programming
    * Cross-compilation targets
    * Embedded and bare-metal `Nim`
    * `Nim` to `JavaScript` for web targets
    * Real-world use cases

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
