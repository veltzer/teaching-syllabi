---
tags:
  - languages:csharp
  - concepts:async-programming
  - concepts:concurrency
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: advanced_csharp -->
# Advanced `C#`

## Description
This advanced course dives deep into the most powerful features of modern `C#`, equipping experienced developers with the skills to write high-performance, maintainable, and scalable code. Topics include advanced `LINQ` techniques, mastering `async`/`await` patterns, memory-efficient programming with `Span<T>` and `Memory<T>`, code generation with source generators, and sophisticated dependency injection patterns. The course also covers records, advanced pattern matching, and strategies for building high-performance `C#` applications. The course includes hands on exercises.

## Duration
24 hours / 3 days

## Intended Audience
* Experienced `C#` developers who want to deepen their understanding of advanced language features.
* Software engineers building high-performance `.NET` applications.
* Developers who want to leverage modern `C#` patterns for production systems.

## Prerequisites
* `Solid` experience with `C#` and the `.NET` ecosystem.
* Understanding of object-oriented programming, generics, and basic `LINQ`.
* Familiarity with `async`/`await` fundamentals.

## Objectives
* Master advanced `LINQ` techniques including custom providers and expression trees
* Write correct and efficient asynchronous code with advanced `async`/`await` patterns
* Use `Span<T>` and `Memory<T>` for high-performance memory management
* Build and use source generators for compile-time code generation
* Apply advanced dependency injection patterns in `.NET` applications
* Leverage records, pattern matching, and modern `C#` features effectively

## Outline
<!-- chapter: advanced-linq, duration: 3h -->
* Advanced `LINQ`
    * Expression trees and `IQueryable<T>`
    * Custom `LINQ` providers
    * Performance considerations and deferred execution pitfalls
    * `LINQ` over `Span<T>` and custom iterators
    * Query optimization strategies
    * Combining `LINQ` with `async` streams
<!-- chapter: mastering-async-await, duration: 3h -->
* Mastering `async`/`await`
    * The `async` state machine under the hood
    * ValueTask and `ValueTask<T>`
    * ConfigureAwait and synchronization contexts
    * `Async` streams with `IAsyncEnumerable<T>`
    * Cancellation patterns and CancellationToken propagation
    * Parallel asynchronous operations
    * Common pitfalls: deadlocks, fire-and-forget, and exception handling
<!-- chapter: span-t-and-memory-t, duration: 3h -->
* `Span<T>` and `Memory<T>`
    * Stack vs heap allocation
    * `Span<T>` fundamentals and constraints
    * `Memory<T>` and `IMemoryOwner<T>`
    * Slicing and working with contiguous memory
    * `ArrayPool<T>` and memory pooling
    * Reducing allocations in hot paths
    * `ref` structs and `ref` returns
<!-- chapter: source-generators, duration: 3h -->
* Source Generators
    * Introduction to the Roslyn compiler platform
    * Incremental source generators
    * Syntax and semantic analysis
    * Generating code at compile time
    * Debugging and testing source generators
    * Practical use cases: serialization, logging, and boilerplate elimination
<!-- chapter: dependency-injection-patterns, duration: 3h -->
* Dependency Injection Patterns
    * Advanced service lifetimes and scoping
    * Keyed services and factory patterns
    * Decorator and composite patterns with `DI`
    * `IOptions<T>`, `IOptionsSnapshot<T>`, and `IOptionsMonitor<T>`
    * Custom service providers
    * Integration testing with dependency injection
<!-- chapter: records-and-value-semantics, duration: 3h -->
* Records and Value Semantics
    * Record classes and record structs
    * Positional records and deconstruction
    * with expressions and non-destructive mutation
    * Value equality and immutability
    * Records in `domain-driven design`
    * `When` to use records vs classes vs structs
<!-- chapter: advanced-pattern-matching, duration: 3h -->
* Advanced Pattern Matching
    * Relational and logical patterns
    * Property patterns and nested patterns
    * List patterns and slice patterns
    * Pattern matching with `switch-expressions`
    * Recursive patterns
    * Designing APIs with pattern matching in mind
<!-- chapter: high-performance-c, duration: 3h -->
* High-Performance `C#`
    * Benchmarking with BenchmarkDotNet
    * Reducing allocations and GC pressure
    * Unsafe code and pointer manipulation
    * SIMD and hardware intrinsics
    * System.IO.Pipelines for high-throughput `I/O`
    * Profiling and identifying bottlenecks
    * NativeAOT compilation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
