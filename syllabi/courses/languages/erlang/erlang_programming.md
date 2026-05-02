---
tags:
  - languages:erlang
  - concepts:concurrency
  - concepts:distributed-systems
  - concepts:functional-programming
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: erlang_programming -->
# `Erlang` Programming

## Description
`Erlang` is a functional, concurrent programming language originally developed by `Ericsson` for building highly available, fault-tolerant telecom systems.
Its actor-based concurrency model, lightweight processes, and share-nothing message passing `make` it exceptionally well-suited for distributed systems that must handle millions of concurrent connections.
The `OTP` (Open Telecom Platform) framework builds on `Erlang` to provide battle-tested patterns for building robust supervisors, workers, and stateful servers.
This course gives developers a thorough grounding in `Erlang` syntax, the actor model, `OTP` behaviours, fault tolerance strategies, and distributed deployment techniques.

## Duration
32 hours / 4 days

## Intended Audience
* Developers building distributed or highly concurrent backend systems
* Software architects evaluating `Erlang` or Elixir for fault-tolerant infrastructure
* Engineers coming from imperative backgrounds who want to understand the actor model

## Prerequisites
* `Solid` programming experience in at least one other language such as `Java`, `Python`, `C++`, or Go
* Basic understanding of concurrency concepts (threads, locks) is helpful but not required
* Familiarity with functional programming concepts is an advantage

## Objectives
* Understand `Erlang`'s philosophy of building for failure and letting processes crash
* Write idiomatic `Erlang` code using pattern matching, guards, and recursion
* Model concurrent systems using lightweight `Erlang` processes and message passing
* Build supervision trees with `OTP` to achieve self-healing applications
* Design and deploy distributed `Erlang` clusters
* Write and run tests using `EUnit` and `Common Test`

## Outline
<!-- chapter: introduction-to-erlang, duration: 2h -->
* Introduction to `Erlang`
    * History and origin at `Ericsson`
    * The design philosophy: let it crash
    * Where `Erlang` is used today (`WhatsApp`, `RabbitMQ`, telecom)
    * Installing `Erlang`/`OTP` and the `rebar3` build tool
    * The `erl` REPL and first expressions
<!-- chapter: erlang-syntax-and-data-types, duration: 3h -->
* `Erlang` Syntax and Data Types
    * Atoms, numbers, booleans
    * Tuples and lists
    * Binaries and bit strings
    * Strings and `iodata`
    * Variables and immutability
    * Maps
    * Records
    * Comprehensions
<!-- chapter: pattern-matching-and-guards, duration: 2h -->
* Pattern Matching and Guards
    * The match operator `=`
    * Matching on tuples and lists
    * Function clause selection via pattern matching
    * Guards: when expressions and allowed functions
    * Case and `if-expressions`
    * Destructuring nested structures
<!-- chapter: processes-and-concurrency, duration: 4h -->
* Processes and Concurrency
    * The `Erlang` process model
    * Spawning processes with `spawn` and `spawn_link`
    * Process identifiers (`PIDs`)
    * Monitoring processes
    * Registered processes and the process registry
    * Process mailboxes
    * Selective receive
    * Timeout handling in `receive`
<!-- chapter: message-passing-and-the-actor-model, duration: 3h -->
* Message Passing and the Actor Model
    * The actor model explained
    * Sending and receiving messages
    * Synchronous request-reply patterns
    * Designing message protocols
    * Avoiding common message-passing pitfalls
    * Back-pressure and flow control
<!-- chapter: otp-framework, duration: 4h -->
* `OTP` Framework
    * What `OTP` provides and why it matters
    * `gen_server`: state machines over message passing
    * `gen_statem`: explicit state machine behaviour
    * `gen_event`: event handling
    * The `application` behaviour
    * Structuring an `OTP` application
<!-- chapter: fault-tolerance-and-supervision-trees, duration: 3h -->
* Fault Tolerance and Supervision Trees
    * Supervision trees explained
    * The `supervisor` behaviour
    * Restart strategies: one-for-one, one-for-all, `rest`-for-one
    * Child specifications
    * Dynamic supervisors
    * Designing for reliability
<!-- chapter: distributed-erlang, duration: 3h -->
* Distributed `Erlang`
    * Node naming and cookies
    * Connecting nodes and the hidden node model
    * Remote process spawning
    * Global process registration with `global`
    * `net_kernel` and node monitoring
    * Distributed traps and partitions
<!-- chapter: ets-and-dets, duration: 2h -->
* `ETS` and `DETS`
    * In-memory tables with `ETS`
    * Table types: set, ordered_set, bag, duplicate_bag
    * Concurrent access patterns
    * Disk-backed storage with `DETS`
    * `mnesia` overview
<!-- chapter: testing-with-eunit-and-common-test, duration: 2h -->
* Testing with `EUnit` and `Common Test`
    * Unit testing with `EUnit`
    * Writing test generators
    * Integration testing with `Common Test`
    * Test suites, groups, and configuration
    * Code coverage with `cover`
<!-- chapter: building-and-deployment, duration: 2h -->
* Building and Deployment
    * The `rebar3` build tool: dependencies, compilation, releases
    * `OTP` releases and `relx`
    * Hot code upgrades and `appup` files
    * Logging with `logger`
    * Observing running systems with `observer` and `recon`
<!-- chapter: building-a-real-world-application, duration: 2h -->
* Building a Real-World Application
    * Designing a concurrent, fault-tolerant service end to end
    * Structuring supervision trees for the problem domain
    * Integrating external dependencies via `rebar3`
    * Deploying and operating the application

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
