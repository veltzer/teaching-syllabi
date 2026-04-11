---
tags:
  - languages:haskell
  - concepts:programming
  - concepts:functional-programming
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: haskell_programming -->
# `Haskell` Programming

## Description
`Haskell` is a purely functional, statically typed programming language known for its strong type system, lazy evaluation, and mathematical foundations. Named after the logician `Haskell` Curry, the language emphasizes correctness, conciseness, and abstraction. `Haskell` has profoundly influenced modern programming language design, and its concepts such as monads, type classes, and algebraic data types have been adopted by many other languages.

This course teaches `Haskell` from foundational functional programming concepts through advanced topics such as monads, functors, and applicatives. Students will learn to think functionally, leverage `Haskell`'s powerful type system, and build real-world applications using the `Haskell` ecosystem. The course includes hands on exercises.

## Duration
32 hours / 4 days

## Intended Audience
* Software developers who want to learn functional programming through `Haskell`.
* Programmers experienced in imperative or object-oriented languages who want to expand their paradigm knowledge.
* Developers interested in building correct, reliable software using strong type systems.

## Prerequisites
* Prior programming experience in another language such as `Python`, `Java`, `C`, or `JavaScript`.
* Basic understanding of mathematical concepts (functions, sets, logic).
* Familiarity with command-line interfaces.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand functional programming principles and how they apply in `Haskell`
* Write `Haskell` programs using algebraic data types, pattern matching, and type classes
* Use higher-order functions and recursion effectively
* Understand and apply monads, functors, and applicatives
* Build and manage `Haskell` projects with Cabal and Stack
* Write property-based tests with QuickCheck

## Outline
<!-- chapter: introduction-to-functional-programming, duration: 3h -->
* Introduction to Functional Programming
    * What is functional programming?
    * Pure functions and referential transparency
    * Immutability and side effects
    * Why `Haskell`?
    * Installing GHC and development tools
    * GHCi interactive environment
<!-- chapter: haskell-basics, duration: 3h -->
* `Haskell` Basics
    * Basic types: `Int`, Integer, Float, Double, Char, `Bool`
    * Variables and bindings
    * Arithmetic and boolean operators
    * `Function-definitions` and application
    * `let` and where clauses
    * Type annotations and type inference
<!-- chapter: functions-and-pattern-matching, duration: 3h -->
* Functions and Pattern Matching
    * Defining functions
    * Pattern matching on values and constructors
    * Guards and conditional expressions
    * Recursion and recursive patterns
    * Tail recursion and accumulator patterns
    * `Lambda` expressions
<!-- chapter: the-type-system, duration: 3h -->
* The Type System
    * Algebraic data types (data, type, newtype)
    * Sum types and product types
    * Record syntax
    * Parameterized types
    * Type classes (Eq, Ord, Show, Read, Num)
    * Defining custom type classes and instances
    * Polymorphism and type constraints
<!-- chapter: lists-and-list-comprehensions, duration: 2h -->
* Lists and List Comprehensions
    * List construction and operations
    * List comprehensions
    * Infinite lists and lazy evaluation
    * Common list functions (map, filter, fold, `zip`)
    * Working with strings as lists
<!-- chapter: higher-order-functions, duration: 2h -->
* Higher-Order Functions
    * Functions as first-class values
    * map, filter, foldl, foldr
    * Function composition and the . operator
    * Partial application and currying
    * The $ operator
<!-- chapter: modules-and-project-structure, duration: 2h -->
* Modules and Project Structure
    * Defining and importing modules
    * Qualified imports and hiding
    * Cabal build tool
    * Stack build tool
    * Project organization and best practices
<!-- chapter: functors-and-applicatives, duration: 2h -->
* Functors and Applicatives
    * The Functor type class and fmap
    * The Applicative type class
    * pure and `<*>`
    * Applicative laws
    * Practical applications of applicatives
<!-- chapter: monads, duration: 4h -->
* Monads
    * What is a monad?
    * The Monad type class and `>>=`
    * do notation
    * The Maybe monad
    * The Either monad
    * The IO monad
    * The State monad
    * The Reader monad
    * The Writer monad
    * Monad laws
<!-- chapter: lazy-evaluation, duration: 2h -->
* Lazy Evaluation
    * Evaluation strategies: strict vs. lazy
    * Thunks and evaluation order
    * Benefits and pitfalls of laziness
    * Strict evaluation with `seq` and BangPatterns
    * Space leaks and how to avoid them
<!-- chapter: error-handling, duration: 2h -->
* Error Handling
    * Maybe and Either for error handling
    * Exceptions in `Haskell`
    * MonadFail and safe patterns
    * Validating input
<!-- chapter: testing-with-quickcheck, duration: 2h -->
* Testing with QuickCheck
    * Introduction to property-based testing
    * Writing properties
    * Generators and Arbitrary instances
    * Shrinking and test case minimization
    * Integrating QuickCheck into projects
<!-- chapter: real-world-haskell-patterns, duration: 2h -->
* Real-World `Haskell` Patterns
    * Working with IO and files
    * Parsing with Parsec
    * `JSON` handling with Aeson
    * Command-line argument parsing
    * Common `design patterns` in `Haskell`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
