---
tags:
  - languages:clojure
  - concepts:functional-programming
  - concepts:jvm
  - concepts:lisp
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: clojure_programming -->
# `Clojure` Programming

## Description
`Clojure` is a modern, dynamic Lisp dialect that runs on the `JVM`, bringing immutable persistent data structures, first-class functions, and powerful macros to `Java` platform developers.
Its emphasis on functional programming, immutability, and simple concurrency primitives makes it an excellent choice for data transformation pipelines, concurrent applications, and systems that must evolve safely over time.
`ClojureScript` extends the same language to the browser and `Node.js`, enabling full-stack development from a single language.
This course provides a comprehensive introduction to `Clojure` programming, covering the language itself, its concurrency model, the macro system, `Java` interoperability, and practical project tooling with `Leiningen`.

## Duration
32 hours / 4 days

## Intended Audience
* `JVM` developers (`Java`, `Kotlin`, `Scala`) looking to explore functional programming
* Developers interested in Lisp family languages and metaprogramming
* Engineers building data-intensive or concurrent backend services

## Prerequisites
* `Solid` experience programming in at least one language, preferably `Java` or another `JVM` language
* Basic understanding of functional concepts such as higher-order functions is helpful
* No prior Lisp experience is required

## Objectives
* Read and write idiomatic `Clojure` code using its core data structures and functions
* Understand and leverage immutability and persistent data structures
* Use `Clojure`'s concurrency primitives (atoms, refs, agents) safely
* Write macros to extend the language for domain-specific use cases
* Interoperate seamlessly with existing `Java` libraries
* Build, test, and package `Clojure` projects with `Leiningen`

## Outline
<!-- chapter: introduction-to-clojure, duration: 2h -->
* Introduction to `Clojure`
    * History and motivation: Lisp on the `JVM`
    * The `Clojure` philosophy: simplicity, data, and functions
    * Installing `Clojure` and `Leiningen`
    * The `REPL` and interactive development
    * Evaluating expressions and the `s-expression` syntax
<!-- chapter: clojure-syntax-and-basic-data-types, duration: 3h -->
* `Clojure` Syntax and Basic Data Types
    * Symbols, keywords, and vars
    * Numbers, strings, and characters
    * Booleans and `nil`
    * The reader and reader macros
    * Defining vars with def and `defn`
    * Namespaced keywords
<!-- chapter: collections-and-sequences, duration: 3h -->
* Collections and Sequences
    * Lists, vectors, maps, and sets
    * Persistent data structures and structural sharing
    * The sequence abstraction
    * Lazy sequences and `lazy-seq`
    * Core sequence functions: `map`, `filter`, `reduce`, `take`, `drop`
    * Transducers for efficient data transformation
    * Destructuring
<!-- chapter: functions-and-functional-programming, duration: 4h -->
* Functions and Functional Programming
    * Defining functions with `defn` and fn
    * Variadic arguments and `rest` parameters
    * Higher-order functions
    * Partial application with `partial`
    * Function composition with `comp`
    * `apply` and `juxt`
    * `Threading` macros: `->` and `->>`
    * Recursion and `recur` for tail-call optimisation
<!-- chapter: namespaces-and-code-organization, duration: 2h -->
* Namespaces and Code Organization
    * Creating and switching namespaces with `ns`
    * require, `use`, and `import`
    * Managing dependencies between namespaces
    * Public and private vars
    * Project directory structure conventions
<!-- chapter: macros-and-metaprogramming, duration: 3h -->
* Macros and Metaprogramming
    * What macros are and why they are powerful
    * `defmacro` and quote/unquote (`'`, `` ` ``, `~`, `~@`)
    * Writing simple macros: `unless`, `when-let`
    * Macro expansion with `macroexpand`
    * Hygiene and avoiding variable capture
    * `When` to reach for a macro vs a function
<!-- chapter: concurrency-with-atoms-refs-and-agents, duration: 3h -->
* Concurrency with Atoms, Refs and Agents
    * The concurrency problem in mutable languages
    * Atoms and `swap!` / `reset!`
    * Software transactional memory with refs and `dosync`
    * Agents for asynchronous state changes
    * Promises and futures
    * `core.async` channels overview
<!-- chapter: java-interoperability, duration: 3h -->
* `Java` Interoperability
    * Calling `Java` methods and constructors
    * Accessing fields
    * Implementing `Java` interfaces with `proxy` and `reify`
    * Defining `Java`-compatible classes with `gen-class`
    * Handling `Java` exceptions
    * Using `Java` collections from `Clojure`
<!-- chapter: testing-with-clojure-test, duration: 2h -->
* Testing with `clojure.test`
    * Writing tests with `deftest` and `is`
    * Grouping tests and running subsets
    * Fixtures for setup and teardown
    * Property-based testing with `test.check`
    * Running tests from the `REPL` and with `Leiningen`
<!-- chapter: leiningen-and-build-tools, duration: 2h -->
* `Leiningen` and Build Tools
    * The `project.clj` file
    * Managing dependencies with `Clojars` and `Maven Central`
    * Running and building `uberjar` artifacts
    * Profiles for environment-specific configuration
    * `deps.edn` and the `Clojure CLI` tools alternative
<!-- chapter: clojurescript-overview, duration: 3h -->
* `ClojureScript` Overview
    * `ClojureScript` vs `Clojure`: differences and shared philosophy
    * Compiling to `JavaScript` with the `ClojureScript` compiler
    * Using `shadow-cljs` for build tooling
    * Interoperating with `JavaScript` libraries
    * Reagent and `Re-frame` for React-based UIs overview
<!-- chapter: building-a-practical-application, duration: 2h -->
* Building a Practical Application
    * Designing a `Clojure` service with immutable domain model
    * Composing transformation pipelines with core sequence functions
    * Adding concurrency with atoms and `core.async`
    * Packaging and deploying the application

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
