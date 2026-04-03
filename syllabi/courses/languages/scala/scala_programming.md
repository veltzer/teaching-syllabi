---
tags:
  - languages:scala
  - languages:java
  - concepts:programming
  - concepts:functional-programming
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: scala_programming -->
# `Scala` Programming

## Description
`Scala` is a modern, multi-paradigm programming language that runs on the `JVM` and seamlessly integrates object-oriented and functional programming. Designed to be concise, elegant, and type-safe, `Scala` is used extensively in data engineering, distributed systems, and backend development. Its powerful type system, pattern matching, and functional programming features `make` it a compelling choice for building robust and scalable applications.

This course covers the `Scala` language comprehensively, from basic syntax through advanced type system features, functional programming patterns, concurrency with Futures and Akka, and interoperability with `Java`.

## Duration
32 hours / 4 days

## Intended Audience
* `Java` developers looking to adopt a more expressive language on the `JVM`
* Developers interested in functional programming concepts
* Backend and data engineers working with `Spark`, Akka, or Play
* Programmers who want to leverage `Scala`'s powerful type system

## Prerequisites
* `Solid` programming experience, preferably in `Java` or another `JVM` language
* Understanding of object-oriented programming concepts
* Familiarity with basic functional programming ideas is helpful but not required

## Objectives
* Write idiomatic `Scala` code combining `OOP` and functional programming
* Use pattern matching, case classes, and algebraic data types effectively
* Leverage `Scala`'s type system including generics, variance, and type bounds
* Build concurrent applications with Futures and Akka
* Manage projects with `SBT`
* Interoperate seamlessly with existing `Java` code

## Outline
<!-- chapter: getting-started-with-scala, duration: 2h -->
* Getting Started with `Scala`
    * What is `Scala` and why use it?
    * Installing `Scala` and `SBT`
    * The `Scala` REPL
    * Hello, World!
    * IDE setup with `IntelliJ IDEA`
    * Basic project structure
<!-- chapter: scala-basics, duration: 2h -->
* `Scala` Basics
    * Values (val) and variables (var)
    * Basic types (`Int`, Double, String, Boolean, Char)
    * Type inference
    * String interpolation
    * Expressions vs statements
    * Blocks and scope
    * Lazy values
<!-- chapter: control-structures, duration: 2h -->
* Control Structures
    * `if/else-expressions`
    * `while-loops` and `do-while-loops`
    * `for-loops` and ranges
    * for-comprehensions with yield
    * Guards in for-comprehensions
    * match expressions
<!-- chapter: functions, duration: 2h -->
* Functions
    * Defining functions
    * Default and named parameters
    * Higher-order functions
    * Anonymous functions (lambdas)
    * Currying
    * Partially applied functions
    * By-name parameters
    * Tail recursion with @tailrec
<!-- chapter: object-oriented-programming, duration: 3h -->
* Object-Oriented Programming
    * Classes and constructors
    * Auxiliary constructors
    * Access modifiers
    * Traits and trait composition
    * Abstract classes
    * Objects and companion objects
    * Case classes and case objects
    * Sealed traits and `sealed-classes`
    * Inheritance and linearization
<!-- chapter: pattern-matching, duration: 2h -->
* Pattern Matching
    * Basic pattern matching
    * Matching on types
    * Matching on case classes
    * Guards in patterns
    * Extractors and unapply
    * Pattern matching in variable assignments
    * Nested patterns
    * Partial functions
<!-- chapter: collections, duration: 2h -->
* Collections
    * Immutable vs mutable collections
    * Lists, Vectors, and Arrays
    * Sets and Maps
    * Tuples
    * Sequences and ranges
    * Common operations (map, filter, flatMap, fold, reduce)
    * Collection transformations
    * Views for lazy evaluation
<!-- chapter: for-comprehensions, duration: 2h -->
* For-Comprehensions
    * Desugaring for-comprehensions
    * Working with Option
    * Working with Either
    * Working with Try
    * Chaining monadic operations
    * Combining multiple generators
<!-- chapter: implicits-and-givens, duration: 2h -->
* Implicits and Givens
    * Implicit parameters
    * Implicit conversions
    * Implicit classes (extension methods)
    * Type classes pattern
    * `Scala` 3 given/using syntax
    * Context bounds
    * Implicit resolution rules
<!-- chapter: type-system, duration: 3h -->
* Type System
    * Generics and type parameters
    * Covariance and contravariance
    * Upper and lower type bounds
    * `Abstract-type` members
    * Self types
    * Structural types
    * Path-dependent types
    * Type aliases
<!-- chapter: futures-and-concurrency, duration: 2h -->
* Futures and Concurrency
    * Creating and composing Futures
    * ExecutionContext
    * map, flatMap, and recover on Futures
    * Future.sequence and Future.traverse
    * Promises
    * Blocking vs non-blocking
    * Error handling in Futures
<!-- chapter: introduction-to-akka, duration: 2h -->
* Introduction to Akka
    * The Actor model
    * Creating actors
    * Sending and receiving messages
    * Actor lifecycle
    * Supervision strategies
    * Actor hierarchies
    * Basic Akka patterns
<!-- chapter: sbt-build-tool, duration: 2h -->
* `SBT` Build Tool
    * Project structure and build.`sbt`
    * Dependencies and resolvers
    * Multi-project builds
    * Common `SBT` commands
    * Plugins
    * Publishing artifacts
<!-- chapter: testing-with-scalatest, duration: 2h -->
* Testing with ScalaTest
    * Testing styles (FunSuite, FlatSpec, WordSpec)
    * Matchers and assertions
    * Test fixtures
    * Mocking with ScalaMock
    * Property-based testing with ScalaCheck
    * Integration testing
<!-- chapter: java-interoperability, duration: 2h -->
* `Java` Interoperability
    * Calling `Java` from `Scala`
    * Calling `Scala` from `Java`
    * `Java` collections conversions
    * Annotations for `Java` compatibility
    * Working with `Java` libraries

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
