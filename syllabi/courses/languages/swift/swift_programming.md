---
tags:
  - languages:swift
  - concepts:programming
  - practices:mobile
level: beginner
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: swift_programming -->
# Swift Programming

## Description
Swift is a powerful and intuitive programming language developed by Apple for building apps across `iOS`, `macOS`, watchOS, and tvOS. It combines modern language features with safety-first design, making it accessible to beginners while remaining powerful enough for experienced developers. Swift emphasizes clarity, performance, and safety through features like optionals, type inference, and automatic memory management via ARC.

This course covers the Swift language from the ground up, including its type system, object-oriented and protocol-oriented programming paradigms, modern concurrency model, and an introduction to building user interfaces with SwiftUI.

## Duration
32 hours / 4 days

## Intended Audience
* Developers who want to build `iOS` and `macOS` applications
* Programmers transitioning from other languages to the Apple ecosystem
* Mobile developers looking to learn native Apple platform development

## Prerequisites
* Prior programming experience in another language such as `Java`, `Python`, `C#`, or `JavaScript`
* Basic understanding of object-oriented programming concepts
* Access to a Mac with `Xcode` installed

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand Swift syntax, type system, and core language features
* Write safe and expressive code using optionals and error handling
* Apply object-oriented and protocol-oriented programming techniques
* Use modern concurrency with async/await and actors
* Build basic user interfaces with SwiftUI
* Write unit tests with XCTest

## Outline
<!-- chapter: getting-started-with-swift, duration: 2h -->
* Getting Started with Swift
    * What is Swift and why use it?
    * Setting up the development environment with `Xcode`
    * Playgrounds and the REPL
    * Hello, World!
    * Basic program structure
<!-- chapter: swift-basics, duration: 2h -->
* Swift Basics
    * Variables and constants (var and let)
    * Basic data types (`Int`, Double, String, `Bool`)
    * Type inference and `type-annotations`
    * String interpolation
    * Tuples
    * Type aliases
<!-- chapter: optionals, duration: 2h -->
* Optionals
    * Understanding optionals
    * Optional binding (`if let`, `guard let`)
    * Nil coalescing operator
    * Optional chaining
    * Implicitly unwrapped optionals
    * Force unwrapping and when to avoid it
<!-- chapter: control-flow, duration: 2h -->
* Control Flow
    * Conditional statements (if, else, switch)
    * Loops (`for-in-loop`, `while-loop`, `repeat-while-loop`)
    * Pattern matching in `switch-statements`
    * Value bindings and where clauses
    * Control transfer statements (break, continue, fallthrough)
<!-- chapter: functions-and-closures, duration: 2h -->
* Functions and Closures
    * Defining and calling functions
    * Parameter labels and default values
    * Variadic parameters and inout parameters
    * `Return-values` and multiple `return-values`
    * Closure syntax and trailing closures
    * Capturing values
    * Escaping and autoclosures
<!-- chapter: collections, duration: 2h -->
* Collections
    * Arrays
    * Dictionaries
    * Sets
    * Iterating over collections
    * Higher-order functions (map, filter, reduce, compactMap)
    * Collection protocols
<!-- chapter: object-oriented-programming, duration: 2h -->
* Object-Oriented Programming
    * Classes and structures
    * Properties (stored, computed, lazy)
    * Property observers
    * Methods and mutating methods
    * Initializers and deinitializers
    * Inheritance and overriding
    * Access control
<!-- chapter: enumerations, duration: 2h -->
* Enumerations
    * Basic enumerations
    * Associated values
    * Raw values
    * Recursive enumerations
    * Pattern matching with enums
<!-- chapter: protocols-and-extensions, duration: 2h -->
* Protocols and Extensions
    * Defining and adopting protocols
    * Protocol requirements
    * Protocol extensions and default implementations
    * Protocol-oriented programming
    * Extensions on existing types
    * Conditional conformance
<!-- chapter: error-handling, duration: 2h -->
* Error Handling
    * Defining errors with Error protocol
    * Throwing and catching errors
    * do-try-`catch-blocks`
    * try? and try!
    * Propagating errors
    * Cleanup with defer
<!-- chapter: generics, duration: 2h -->
* Generics
    * Generic functions
    * Generic types
    * Type constraints
    * Associated types
    * Generic where clauses
    * Opaque types
<!-- chapter: concurrency, duration: 2h -->
* Concurrency
    * Introduction to Swift concurrency model
    * async/await basics
    * Structured concurrency with Task and TaskGroup
    * Actors and data isolation
    * Sendable protocol
    * MainActor and global actors
<!-- chapter: memory-management, duration: 2h -->
* Memory Management
    * Automatic Reference Counting (ARC)
    * Strong, weak, and unowned references
    * Retain cycles and how to avoid them
    * Closures and capture lists
    * Value types vs reference types
<!-- chapter: introduction-to-swiftui, duration: 2h -->
* Introduction to SwiftUI
    * Declarative UI basics
    * Views and modifiers
    * State management (@State, @Binding, @ObservedObject)
    * Layout system (HStack, VStack, ZStack)
    * Lists and navigation
<!-- chapter: ios-app-basics, duration: 2h -->
* `iOS` App Basics
    * App lifecycle
    * Project structure in `Xcode`
    * Building and running on simulators
    * Basic app architecture patterns
    * Debugging with `Xcode`
<!-- chapter: testing-with-xctest, duration: 2h -->
* Testing with XCTest
    * Writing unit tests
    * Test assertions
    * Testing asynchronous code
    * UI testing basics
    * Test-driven development workflow

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
