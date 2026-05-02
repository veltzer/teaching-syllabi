---
tags:
  - languages:elixir
  - concepts:programming
  - concepts:functional-programming
  - concepts:concurrency
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: elixir_programming -->
# Elixir Programming

## Description
Elixir is a dynamic, functional programming language built on the `Erlang` VM (BEAM), designed for building scalable and maintainable applications. Created by Jose Valim, Elixir leverages the battle-tested `Erlang` ecosystem while providing a modern, approachable syntax and powerful metaprogramming capabilities. Elixir excels at building distributed, fault-tolerant systems and real-time applications.

This course covers Elixir from the fundamentals through advanced topics including `OTP`, concurrency patterns, and the Phoenix web framework. Students will learn functional programming with Elixir, build concurrent applications using lightweight processes, and understand the fault tolerance patterns that `make` BEAM-based systems highly reliable. The course includes hands on exercises.

## Duration
32 hours / 4 days

## Intended Audience
* Software developers who want to learn Elixir for building concurrent and distributed systems.
* Programmers interested in functional programming with practical, real-world applications.
* Developers who need to build fault-tolerant, scalable web applications and services.

## Prerequisites
* Prior programming experience in another language such as `Python`, Ruby, `Java`, or `JavaScript`.
* Understanding of basic computer science concepts.
* Familiarity with command-line interfaces.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand Elixir syntax, pattern matching, and functional programming concepts
* Build concurrent applications using Elixir processes and message passing
* Design fault-tolerant systems using `OTP` patterns
* Work with Mix, ExUnit, and the Elixir toolchain
* Use Ecto for database interactions
* Understand the basics of the Phoenix framework and LiveView

## Outline
<!-- chapter: getting-started-with-elixir, duration: 2h -->
* Getting Started with Elixir
    * What is Elixir and the BEAM VM?
    * Installing Elixir and development tools
    * IEx interactive shell
    * First program: Hello, World!
    * Basic syntax and conventions
<!-- chapter: elixir-fundamentals, duration: 2h -->
* Elixir Fundamentals
    * Basic types: integers, floats, atoms, strings, booleans
    * Tuples, lists, and keyword lists
    * Maps and structs
    * Pattern matching and the match operator
    * Pin operator
    * String handling and interpolation
<!-- chapter: control-flow, duration: 2h -->
* Control Flow
    * `case-expressions`
    * cond expressions
    * if, unless, and with
    * Guards and guard clauses
    * Pipe operator (`|>`)
<!-- chapter: functions-and-modules, duration: 2h -->
* Functions and Modules
    * Anonymous functions
    * Named functions and arity
    * Default arguments and function clauses
    * Pattern matching in function heads
    * Modules and module attributes
    * import, alias, and use
<!-- chapter: collections-and-enumeration, duration: 2h -->
* Collections and Enumeration
    * Working with lists and tuples
    * The Enum module
    * The Stream module and lazy evaluation
    * Comprehensions
    * Keyword lists and maps in depth
<!-- chapter: processes-and-message-passing, duration: 2h -->
* Processes and Message Passing
    * Spawning processes
    * Sending and receiving messages
    * Process linking and monitoring
    * Process state with recursive loops
    * Process registration
<!-- chapter: otp-fundamentals, duration: 2h -->
* `OTP` Fundamentals
    * Introduction to `OTP`
    * GenServer: generic server processes
    * Supervisor: supervision trees and strategies
    * Application: packaging and starting applications
    * Agent and Task abstractions
    * Supervision strategies (one_for_one, one_for_all, rest_for_one)
<!-- chapter: concurrency-model, duration: 2h -->
* Concurrency Model
    * The BEAM VM and schedulers
    * Lightweight processes and scalability
    * Preemptive scheduling and fairness
    * Process isolation and garbage collection
    * ETS and in-memory storage
<!-- chapter: error-handling-and-fault-tolerance, duration: 2h -->
* Error Handling and Fault Tolerance
    * The "let it crash" philosophy
    * try/rescue/after
    * throw and catch
    * Supervisor restart strategies
    * Designing for failure recovery
<!-- chapter: the-mix-build-tool, duration: 2h -->
* The Mix Build Tool
    * Creating projects with Mix
    * Dependencies and Hex package manager
    * Configuration and environments
    * Tasks and custom tasks
    * Releases with `mix release`
<!-- chapter: testing-with-exunit, duration: 3h -->
* Testing with ExUnit
    * Introduction to ExUnit
    * Writing and organizing tests
    * Assertions and pattern matching in tests
    * Setup and fixtures with setup and setup_all
    * Doctests
    * Mocking and test isolation
<!-- chapter: ecto-and-database-access, duration: 3h -->
* Ecto and Database Access
    * Introduction to Ecto
    * Repositories and schemas
    * Migrations
    * Changesets and validations
    * Querying with the Ecto query DSL
    * Associations and preloading
<!-- chapter: phoenix-framework-introduction, duration: 2h -->
* Phoenix Framework Introduction
    * Overview of the Phoenix framework
    * Request lifecycle and plugs
    * Routing, controllers, and views
    * Templates and layouts
    * `JSON` APIs with Phoenix
<!-- chapter: liveview-basics, duration: 2h -->
* LiveView Basics
    * What is `Phoenix LiveView`?
    * Real-time server-rendered UI
    * Events and state management
    * Live navigation
    * Form handling with LiveView
<!-- chapter: distributed-elixir, duration: 2h -->
* Distributed Elixir
    * Connecting BEAM nodes
    * Distributed processes and message passing
    * Global process registration
    * Distributed `OTP` patterns
    * Considerations for distributed systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
