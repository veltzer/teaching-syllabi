---
tags:
  - languages:go
  - concepts:programming
  - concepts:concurrency
level: beginner
category: language
duration_hours: 32
audience:
  - audiences:developers
---
# `Go` Programming

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Go` is a statically typed, compiled language designed at Google for simplicity, reliability, and efficiency. It excels at building networked services, command-line tools, and concurrent systems. This course covers the `Go` language from fundamentals through advanced topics like concurrency, interfaces, and production patterns.

## Duration
32 hours / 4 days

## Intended Audience
* Developers learning `Go` for backend services or systems programming
* Developers coming from `Python`, `Java`, `C`, or other languages
* Teams adopting `Go` for microservices or cloud-native development

## Prerequisites
* Programming experience in any language

## Objectives
* Write idiomatic `Go` code
* Understand `Go`'s concurrency model with `goroutines` and channels
* Build and test `Go` applications
* Use `Go`'s standard library for networking and I/O
* Manage dependencies with `Go` modules

## Outline
* Introduction to `Go`
    * History and design philosophy
    * The `Go` toolchain (go build, go run, go test, go fmt)
    * Workspace and project layout
    * `Go` modules and dependency management
    * First program: Hello World
* Basic Syntax and Types
    * Variables, constants, and declarations
    * Basic types (int, float64, string, bool)
    * Zero values
    * Type conversions
    * Pointers
    * Operators
* Control Flow
    * if, else, switch
    * for loops (the only loop)
    * Range
    * Defer, panic, and recover
    * Labeled statements and goto
* Functions
    * Function declarations
    * Multiple return values
    * Named return values
    * Variadic functions
    * First-class functions and closures
    * Init functions
* Composite Types
    * Arrays and slices
    * Slice internals and capacity
    * Maps
    * Structs
    * Struct embedding
    * Struct tags
* Methods and Interfaces
    * Methods on types
    * Value receivers vs pointer receivers
    * Interfaces and implicit satisfaction
    * The empty interface
    * Type assertions and type switches
    * Common interfaces (io.Reader, io.Writer, error, fmt.Stringer)
* Error Handling
    * The error interface
    * Creating custom errors
    * Error wrapping and unwrapping (errors.Is, errors.As)
    * Sentinel errors
    * Error handling patterns and best practices
* Concurrency
    * `Goroutines`
    * Channels (buffered and `unbuffered`)
    * Select statement
    * `WaitGroups`
    * Mutexes and sync package
    * Context package for cancellation and timeouts
    * Common concurrency patterns (fan-in, fan-out, pipeline, worker pool)
* Packages and Modules
    * Package organization and naming
    * Exported vs `unexported` identifiers
    * `Go` modules in depth
    * Versioning and semantic import versioning
    * Vendoring
    * Internal packages
* The Standard Library
    * `fmt` and strings
    * io and `bufio`
    * os and `filepath`
    * net/http (client and server)
    * encoding/json
    * time
    * log and `slog`
* Testing
    * Writing tests with the testing package
    * Table-driven tests
    * Benchmarks
    * Fuzzing
    * Test coverage
    * Testable code patterns
* `Go` in Production
    * Building static binaries
    * Cross-compilation
    * Profiling with `pprof`
    * Race detector
    * `Go` and `Docker`
    * Linting and static analysis (go vet, `staticcheck`, `golangci-lint`)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
