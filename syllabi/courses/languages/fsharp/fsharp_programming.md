---
tags:
  - languages:fsharp
  - concepts:functional-programming
  - concepts:dotnet
  - concepts:type-system
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
  - audiences:dotnet-developers
---
<!-- course: fsharp_programming -->
# `F#` Programming

## Description
`F#` is a strongly typed, functional-first language on the `.NET` platform that blends functional, object-oriented, and imperative styles within a single, concise syntax.
Its expressive type system, discriminated unions, pattern matching, and computation expressions `make` it ideal for domain modelling, data transformation, and building reliable backend services.
`F#` runs everywhere `.NET` runs—`Windows`, `Linux`, and `macOS`—and interoperates seamlessly with the entire `C#` and `.NET` ecosystem.
This course equips `.NET` developers with the skills to write idiomatic `F#` code, model complex domains with algebraic types, write asynchronous workflows, and integrate `F#` into existing `.NET` projects.

## Duration
32 hours / 4 days

## Intended Audience
* `C#` and `.NET` developers who want to adopt functional programming within the `.NET` ecosystem
* Developers interested in strong type-system-driven design and domain modelling
* Backend engineers building data pipelines, APIs, or concurrent services on `.NET`

## Prerequisites
* Experience with `C#` or another `.NET` language is strongly recommended
* Basic familiarity with object-oriented programming concepts
* No prior functional programming experience is required

## Objectives
* Write `clean`, idiomatic `F#` code using functions, pipelines, and algebraic types
* Model complex domains using discriminated unions, records, and option types
* Handle errors explicitly using the `Result` type without exceptions
* Write asynchronous workflows using `async` and `task` computation expressions
* Interoperate with existing `C#` libraries and `.NET` APIs
* Test `F#` code with `xUnit` or `NUnit`

## Outline
<!-- chapter: introduction-to-fsharp, duration: 3h -->
* Introduction to `F#`
    * History and motivation: functional programming on `.NET`
    * Installing `F#` with the `.NET SDK` and `Visual Studio Code`
    * The `F#` interactive (`dotnet fsi`) REPL
    * First expressions and the `let` binding
    * Type inference and the compiler
    * Tooling: `Ionide`, `Rider`, `Visual Studio`
<!-- chapter: basic-types-and-expressions, duration: 3h -->
* Basic Types and Expressions
    * Primitive types: `int`, `float`, `bool`, `string`, `char`
    * Immutable bindings with `let`
    * Mutable values with `mutable`
    * Tuples
    * `unit` type
    * Arithmetic and comparison operators
    * String interpolation
<!-- chapter: functions-and-pattern-matching, duration: 3h -->
* Functions and Pattern Matching
    * Defining functions
    * Currying and partial application
    * The pipe operator `|>` and function composition `>>`
    * Pattern matching with `match`
    * Matching on tuples, lists, and records
    * Active patterns
    * Recursive functions and `rec`
<!-- chapter: collections-and-pipelines, duration: 3h -->
* Collections and Pipelines
    * Lists, arrays, and sequences
    * The `List`, `Array`, and `Seq` modules
    * `map`, `filter`, `fold`, `collect`, `choose`
    * Lazy evaluation with `Seq`
    * Building data transformation pipelines with `|>`
    * Set and Map collections
<!-- chapter: discriminated-unions-and-records, duration: 2h -->
* Discriminated Unions and Records
    * Defining records and their immutable update syntax
    * Discriminated unions as algebraic data types
    * Single-case discriminated unions for type safety
    * Exhaustive matching on union cases
    * Modelling domains with types
<!-- chapter: options-and-result-types, duration: 3h -->
* Options and Result Types
    * The `option` type: `Some` and `None`
    * Avoiding null with `option`
    * Mapping and chaining option values
    * The `Result` type for error handling
    * Railway-oriented programming
    * The `FsToolkit.ErrorHandling` library overview
<!-- chapter: modules-and-namespaces, duration: 2h -->
* Modules and Namespaces
    * Defining and opening modules
    * Nested modules
    * Namespaces vs modules
    * `File` order and the `F#` compiler's `top`-down rule
    * Organizing a multi-`file` `F#` project
<!-- chapter: asynchronous-programming, duration: 3h -->
* Asynchronous Programming
    * `async` computation expressions
    * `Async.Start`, `Async.RunSynchronously`, `Async.Parallel`
    * The `task {}` computation expression for `.NET` Task interop
    * Cancellation tokens
    * Combining `async` workflows
    * Comparison of `async` vs `task`
<!-- chapter: computation-expressions, duration: 2h -->
* Computation Expressions
    * What computation expressions are
    * The `builder` pattern
    * Understanding `async`, `seq`, and `result` as computation expressions
    * Writing a custom computation expression
    * Using `CE` libraries from the ecosystem
<!-- chapter: interoperability-with-csharp-and-dotnet, duration: 2h -->
* Interoperability with `C#` and `.NET`
    * Consuming `C#` libraries from `F#`
    * Handling `null` from `C#` APIs
    * Exposing `F#` code to `C#` consumers
    * Using `LINQ` from `F#`
    * Attributes and reflection
<!-- chapter: testing-fsharp-code, duration: 2h -->
* Testing `F#` Code
    * Testing with `xUnit` and `NUnit`
    * Writing property-based tests with `FsCheck`
    * Using `Expecto` as an `F#`-native test framework
    * Organising test projects with `dotnet test`
    * Snapshot testing overview
<!-- chapter: building-real-world-applications, duration: 2h -->
* Building Real-World Applications
    * Building a web `API` with `Giraffe` or `Falco`
    * Domain modelling with discriminated unions
    * Parsing and validating input with the `Result` type
    * Structuring an `F#` solution with multiple projects
<!-- chapter: type-providers, duration: 2h -->
* Type Providers
    * What type providers are and why they matter
    * `FSharp.Data`: consuming `JSON`, `CSV`, and `XML` with types
    * `SQLProvider` for typed database access
    * Writing a simple custom type provider

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
