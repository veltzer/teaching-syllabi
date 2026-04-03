---
tags:
  - languages:mojo
  - concepts:ai
  - concepts:performance
  - concepts:python-superset
  - concepts:systems-programming
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:ml-engineers
---
<!-- course: mojo_programming -->
# `Mojo` Programming

## Description
`Mojo` is a new programming language designed by Modular to bridge the gap between `Python`'s productivity and the performance of systems languages like `C++` and `Rust`.
It is a strict superset of `Python`, meaning all valid `Python` code is valid `Mojo`, while adding `def`/`fn` distinctions, ownership semantics, SIMD intrinsics, and zero-cost abstractions for hardware acceleration.
`Mojo` is purpose-built for `AI` and high-performance computing workloads, enabling developers to write kernels, neural network layers, and numerical algorithms that run at full hardware speed without leaving the `Python` ecosystem.
This course takes `Python` developers through `Mojo`'s type system, memory ownership model, SIMD programming, and practical patterns for accelerating `ML` workloads.

## Duration
24 hours / 3 days

## Intended Audience
* `Python` developers who need native performance for numerical and `AI` workloads
* `ML` engineers optimising model inference and training kernels
* Systems programmers exploring modern alternatives for `AI` infrastructure

## Prerequisites
* Strong `Python` programming skills
* Familiarity with `NumPy` and basic `machine learning` concepts
* Basic understanding of `CPU` architecture and memory hierarchy is helpful

## Objectives
* Understand how `Mojo` extends `Python` for performance-critical code
* Use `fn` functions, `struct` types, and the type system for zero-overhead abstractions
* Apply `Mojo`'s ownership and borrow checker to manage memory safely
* Write SIMD-accelerated code using `Mojo`'s hardware intrinsics
* Implement parallel algorithms using `Mojo`'s parallelism primitives
* Interoperate seamlessly between `Python` and `Mojo` in the same codebase
* Benchmark and optimise `Mojo` code for `ML` inference tasks

## Outline
<!-- chapter: introduction-to-mojo, duration: 2h -->
* Introduction to `Mojo`
    * Design goals — why `Python` is not enough for `AI` infrastructure
    * `Mojo` vs `Python` vs `C++` vs `Rust` positioning
    * The Modular ecosystem and `MAX` platform
    * Installing `Mojo` and the toolchain
    * Running `Mojo` programs and notebooks

<!-- chapter: mojo-basics-and-python-compatibility, duration: 2h -->
* `Mojo` Basics and `Python` Compatibility
    * `def` functions — full `Python` compatibility mode
    * `fn` functions — strict mode with `type-annotations`
    * Running existing `Python` code in `Mojo`
    * Importing `Python` modules from `Mojo`
    * `let` and `var` declarations

<!-- chapter: types-and-variables, duration: 2h -->
* Types and Variables
    * Scalar types — `Int`, `Float64`, `Bool`, `StringLiteral`
    * `SIMD` vector type introduction
    * `DType` and type parameters
    * `Optional` and `Variant` types
    * Type aliases

<!-- chapter: functions-and-parameters, duration: 2h -->
* Functions and Parameters
    * Argument conventions — `borrowed`, `inout`, `owned`
    * `Return-types` and multiple returns
    * Default parameter values
    * Keyword arguments
    * `@parameter` decorator for compile-time constants
    * Overloaded functions

<!-- chapter: structs-and-traits, duration: 3h -->
* Structs and Traits
    * Defining structs
    * Methods and lifecycle — `__init__`, `__del__`, `__copyinit__`, `__moveinit__`
    * Traits — compile-time interfaces
    * Implementing traits
    * Generic structs and functions
    * Operator overloading via special methods

<!-- chapter: memory-management-and-ownership, duration: 3h -->
* Memory Management and Ownership
    * Stack vs heap allocation
    * Value semantics by default
    * The borrow checker — borrowed and mutable references
    * Owned values and move semantics
    * `Pointer` and `UnsafePointer`
    * Manual memory allocation patterns

<!-- chapter: simd-and-hardware-intrinsics, duration: 3h -->
* SIMD and Hardware Intrinsics
    * SIMD fundamentals — why vector operations matter
    * The `SIMD[DType, size]` type
    * SIMD arithmetic and comparison operations
    * Vectorising loops with `vectorize`
    * Hardware-specific intrinsics
    * Benchmarking SIMD vs scalar code

<!-- chapter: parallelism-and-concurrency, duration: 2h -->
* Parallelism and Concurrency
    * `parallelize` for parallel loops
    * Thread pool management
    * Atomic operations
    * Avoiding data races
    * Performance scaling across cores

<!-- chapter: python-interoperability, duration: 2h -->
* `Python` Interoperability
    * Calling `Python` libraries from `Mojo`
    * Passing data between `Python` and `Mojo`
    * Wrapping `Python` objects
    * Performance implications of the boundary
    * Gradual migration strategies

<!-- chapter: building-high-performance-ml-code, duration: 3h -->
* Building High-Performance `ML` Code
    * Writing a matrix multiplication kernel from scratch
    * Tiling and cache-friendly algorithms
    * Optimising transformer attention layers
    * Profiling `Mojo` programs
    * Integrating `Mojo` kernels into `PyTorch` workflows

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
