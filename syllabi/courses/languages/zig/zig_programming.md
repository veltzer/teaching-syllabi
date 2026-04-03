---
tags:
  - languages:zig
  - concepts:programming
  - concepts:systems-programming
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: zig_programming -->
# Zig Programming

## Description
Zig is a modern systems programming language designed to be a practical alternative to `C` and `C++`. It emphasizes simplicity, explicit control over memory and behavior, and compile-time evaluation through its powerful comptime feature. Zig provides manual memory management without hidden control flow, no hidden allocations, and seamless interoperability with `C` code and ABI.

This course covers Zig from its design philosophy through practical systems programming, including its unique compile-time features, error handling model, memory management with allocators, `C` interoperability, and the built-in build system and test framework.

## Duration
24 hours / 3 days

## Intended Audience
* Systems programmers looking for a modern alternative to `C`/`C++`
* Developers interested in low-level programming with better safety guarantees
* `C`/`C++` programmers who want more explicit and predictable behavior
* `Rust` developers curious about a different approach to systems programming

## Prerequisites
* Prior programming experience in `C`, `C++`, `Rust`, or a similar systems language
* Understanding of pointers, memory layout, and manual memory management
* Familiarity with command-line build tools

## Required Knowledge
* `Rust` Programming (or equivalent experience)

## Objectives
* Understand Zig's design philosophy and goals
* Write Zig programs using its type system, error handling, and comptime features
* Manage memory explicitly using Zig's allocator model
* Interoperate with `C` libraries and ABI
* Use the Zig build system and test framework
* Compare Zig's approach to those of `C`, `C++`, and `Rust`

## Outline
<!-- chapter: zig-philosophy-and-design-goals, duration: 1h -->
* Zig Philosophy and Design Goals
    * Why Zig exists
    * Design principles: simplicity, explicitness, performance
    * No hidden control flow, no hidden allocations
    * Comparison with `C`, `C++`, and `Rust` at a high level
    * The Zig ecosystem and community
    * Installing Zig and editor setup
<!-- chapter: basic-syntax-and-types, duration: 2h -->
* Basic Syntax and Types
    * Hello, World!
    * Variables and constants (var and const)
    * Primitive types (integers, floats, booleans)
    * Arrays and multi-dimensional arrays
    * Characters and strings
    * Pointers and pointer arithmetic
    * Type coercions and @as
    * Undefined and undefined values
<!-- chapter: comptime-compile-time-execution, duration: 2h -->
* Comptime (Compile-Time Execution)
    * What is comptime?
    * comptime variables and parameters
    * Compile-time function execution
    * comptime blocks
    * Type reflection and @typeInfo
    * Generating code at compile time
    * Compile-time vs runtime evaluation
<!-- chapter: error-handling, duration: 2h -->
* Error Handling
    * Error unions
    * The `try-keyword`
    * catch and default values
    * Error sets and merging
    * errdefer for cleanup
    * Returning errors from functions
    * Error traces
    * Comparison with exceptions and Result types
<!-- chapter: slices-and-arrays, duration: 1h -->
* Slices and Arrays
    * `Array` types and initialization
    * Slices and slice syntax
    * Sentinel-terminated arrays
    * Slice operations and bounds checking
    * Multi-dimensional arrays
    * Strings as slices of bytes
<!-- chapter: structs-and-enums, duration: 2h -->
* Structs and Enums
    * Defining structs
    * Default field values
    * Methods and namespace functions
    * Packed and extern structs
    * Enums and tagged unions
    * Union types
    * Anonymous structs and tuples
<!-- chapter: allocators-and-memory-management, duration: 2h -->
* Allocators and Memory Management
    * Zig's allocator interface
    * General purpose allocators
    * Arena allocators
    * Fixed buffer allocators
    * Page allocators
    * Custom allocator implementation
    * Memory safety patterns
    * Detecting memory leaks in tests
<!-- chapter: optionals, duration: 2h -->
* Optionals
    * Optional types
    * Null and the null literal
    * Unwrapping optionals
    * orelse and default values
    * Optional pointers
    * if with optionals
    * while with optionals
<!-- chapter: generics-via-comptime, duration: 1h -->
* Generics via Comptime
    * Generic functions using comptime parameters
    * Generic data structures
    * anytype parameters
    * comptime interfaces
    * Compile-time duck typing
    * Standard library generic patterns
<!-- chapter: c-interop-and-abi-compatibility, duration: 2h -->
* `C` Interop and ABI Compatibility
    * Importing `C` headers with @cImport
    * Calling `C` functions from Zig
    * Exporting Zig functions to `C`
    * `C`-compatible types and extern structs
    * Linking with `C` libraries
    * Translating `C` code to Zig
    * Working with `C` strings
<!-- chapter: build-system-build-zig, duration: 2h -->
* Build System (build.zig)
    * The build.zig `file`
    * Build steps and dependencies
    * Compiling executables and libraries
    * Adding `C` sources and dependencies
    * Cross-compilation
    * Build options and configuration
    * Package management
<!-- chapter: async-i-o, duration: 1h -->
* `Async` `I/O`
    * Zig's `async` model
    * `Async` functions and frames
    * Suspend and resume
    * `Async` `I/O` operations
    * Event loops
    * Integrating with OS `I/O` facilities
<!-- chapter: testing, duration: 2h -->
* Testing
    * Built-in test framework
    * Writing test blocks
    * Test assertions and expect
    * Testing allocators for leak detection
    * Running tests with `zig test`
    * Test organization and filtering
    * Testing patterns for Zig code
<!-- chapter: comparison-with-c-c-rust, duration: 2h -->
* Comparison with `C`/`C++`/`Rust`
    * Memory safety approaches
    * Error handling comparison
    * Build system and tooling comparison
    * Performance characteristics
    * Interoperability differences
    * `When` to choose Zig

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
