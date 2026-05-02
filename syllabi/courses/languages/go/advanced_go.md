---
tags:
  - languages:go
  - concepts:concurrency
  - concepts:programming
  - concepts:testing
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: advanced_go -->
# Advanced Go

## Description
This course covers advanced Go topics for experienced developers who want to deepen their expertise. It explores concurrency patterns, generics, testing strategies, performance profiling, reflection, the unsafe package, and advanced build tooling including code generation and build tags.

## Duration
24 hours / 3 days

## Intended Audience
* Experienced Go developers looking to master advanced language features
* Backend engineers building high-performance Go services
* Developers who want to write more idiomatic and efficient Go code

## Prerequisites
* `Solid` experience with Go programming
* Familiarity with goroutines, channels, and interfaces
* Understanding of Go modules and the standard library

## Objectives
* Apply advanced concurrency patterns for real-world systems
* Use Go generics effectively for type-safe reusable code
* Write comprehensive tests including fuzzing and benchmarking
* Profile and optimize Go applications using pprof
* Leverage reflection, unsafe, and code generation for advanced use cases

## Outline
<!-- chapter: advanced-concurrency-patterns, duration: 3h -->
* Advanced Concurrency Patterns
    * Review of goroutines and channels
    * Fan-in, fan-out, and pipeline patterns
    * Worker pools and rate limiting
    * errgroup and structured concurrency
    * Context propagation and cancellation
    * Lock-free programming with sync/atomic
    * The sync.Pool and memory reuse
    * Detecting and avoiding deadlocks and race conditions
<!-- chapter: generics, duration: 3h -->
* Generics
    * Type parameters and constraints
    * The comparable and any constraints
    * Defining custom constraints
    * Generic data structures
    * Generic functions and methods
    * Limitations and best practices
    * `When` to use generics vs interfaces
<!-- chapter: testing-strategies, duration: 3h -->
* Testing Strategies
    * Table-driven tests and subtests
    * Test fixtures and helpers
    * Mocking and dependency injection for tests
    * Integration testing patterns
    * Fuzzing with `go test -fuzz`
    * Property-based testing
    * Test coverage analysis and best practices
    * Testing concurrent code
<!-- chapter: profiling-and-benchmarking, duration: 3h -->
* Profiling and Benchmarking
    * Writing benchmarks with testing.B
    * `CPU` and memory profiling with pprof
    * Trace analysis with `go tool trace`
    * Identifying allocations and escape analysis
    * Compiler optimizations and inlining
    * The race detector in depth
    * Performance optimization techniques
<!-- chapter: reflection, duration: 3h -->
* Reflection
    * The reflect package
    * reflect.Type and reflect.Value
    * Inspecting struct tags
    * Dynamic method invocation
    * Building generic utilities with reflection
    * Performance implications of reflection
<!-- chapter: the-unsafe-package, duration: 2h -->
* The unsafe Package
    * Understanding unsafe.Pointer
    * Pointer arithmetic and type conversions
    * unsafe.Sizeof, unsafe.Alignof, unsafe.Offsetof
    * Interfacing with C code via cgo
    * Safety considerations and when to use unsafe
<!-- chapter: internal-packages-and-project-structure, duration: 2h -->
* Internal Packages and Project Structure
    * The internal package convention
    * Large project layout patterns
    * `API` design and exported surface management
    * Dependency management strategies
    * Multi-module repositories
<!-- chapter: build-tags-and-conditional-compilation, duration: 2h -->
* Build Tags and Conditional Compilation
    * Build constraint syntax
    * Platform-specific code
    * Feature flags with build tags
    * Custom build tags for testing and debugging
    * The `go`:build directive
<!-- chapter: code-generation, duration: 3h -->
* Code Generation
    * The `go generate` command
    * Writing custom code generators
    * Using `go`/ast and `go`/parser
    * Popular code generation tools (stringer, mockgen, protoc-gen-`go`)
    * Template-based code generation with text/template
    * Best practices for generated code

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
