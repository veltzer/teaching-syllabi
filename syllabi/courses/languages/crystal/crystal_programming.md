---
tags:
  - languages:crystal
  - concepts:compiled
  - concepts:oop
  - concepts:type-system
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: crystal_programming -->
# `Crystal` Programming

## Description
`Crystal` is a statically typed, compiled systems programming language with a syntax inspired by `Ruby`, offering the elegance of a dynamic language with the safety and performance of a compiled one.
Its type inference engine eliminates most explicit annotations, while macros enable powerful compile-time metaprogramming.
`Crystal` compiles to native code via `LLVM` and features built-in fibers and channels for lightweight concurrency.
This course covers `Crystal` from first programs through its type system, concurrency model, macros, and web development with the `Kemal` framework.

## Duration
24 hours / 3 days

## Intended Audience
* `Ruby` developers looking for a compiled, type-safe alternative
* Developers wanting native performance without `C`/`C++` complexity
* Backend engineers exploring modern compiled language options

## Prerequisites
* Experience in at least one object-oriented language
* Basic understanding of compiled languages is helpful

## Objectives
* Write idiomatic `Crystal` programs using its type system and inference
* Model domains with classes, modules, and structs
* Implement concurrent programs using fibers and channels
* Use macros for compile-time code generation
* Manage dependencies with `shards`
* Build `web services` with `Kemal`

## Outline
<!-- chapter: introduction-to-crystal, duration: 2h -->
* Introduction to `Crystal`
    * History and design philosophy
    * Comparison with `Ruby` and other compiled languages
    * Setting up the toolchain
    * Your first `Crystal` program
    * The `crystal` compiler and `shards` package manager

<!-- chapter: types-and-variables, duration: 2h -->
* Types and Variables
    * Type inference
    * Primitive types and literals
    * Strings and string interpolation
    * Symbols and enums
    * Nil and union types (`T | Nil`)

<!-- chapter: control-flow-and-blocks, duration: 2h -->
* Control Flow and Blocks
    * Conditionals and ternary expressions
    * Loops — `while`, `loop`, `each`
    * Blocks, procs, and lambdas
    * `yield` and block arguments
    * Iterators and the `Enumerable` mixin

<!-- chapter: classes-and-modules, duration: 3h -->
* Classes and Modules
    * Defining classes and instance variables
    * Constructors and `initialize`
    * Inheritance and method overriding
    * Abstract classes and methods
    * Modules as mixins
    * Structs vs classes

<!-- chapter: generics-and-type-system, duration: 2h -->
* Generics and the Type System
    * Generic classes and methods
    * Type restrictions and unions
    * Type aliases
    * Casting and `as?`
    * Compile-time type checking

<!-- chapter: concurrency-with-fibers-and-channels, duration: 3h -->
* Concurrency with Fibers and Channels
    * Fibers — lightweight cooperative threads
    * Spawning fibers with `spawn`
    * Channels for inter-fiber communication
    * Select statements
    * `Mutex` and synchronisation primitives

<!-- chapter: macros, duration: 2h -->
* Macros
    * Macro fundamentals
    * Compile-time reflection
    * `define_method` and code generation patterns
    * Hooks — `included`, `extended`, `inherited`
    * Annotations

<!-- chapter: standard-library-and-shards, duration: 2h -->
* Standard Library and Shards
    * Collections — `Array`, `Hash`, `Set`, `Tuple`
    * `File` and `I/O`
    * `HTTP` client
    * `JSON` and `YAML` serialisation
    * Managing dependencies with `shards`

<!-- chapter: c-bindings, duration: 2h -->
* `C` Bindings
    * `lib` declarations
    * Calling `C` functions from `Crystal`
    * Structs and unions in bindings
    * Managing memory at the boundary

<!-- chapter: testing-and-spec, duration: 2h -->
* Testing and Spec
    * `Crystal` Spec framework
    * Writing unit tests
    * Mocking and stubbing
    * Code coverage

<!-- chapter: building-web-applications-with-kemal, duration: 2h -->
* Building Web Applications with `Kemal`
    * `Kemal` routing
    * Request and response handling
    * Middleware
    * Rendering `JSON` APIs
    * Deploying `Crystal` applications

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
