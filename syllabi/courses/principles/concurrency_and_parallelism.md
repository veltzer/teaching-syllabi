---
tags:
  - concepts:concurrency
  - concepts:parallel-computing
  - concepts:multithreading
  - concepts:async-programming
  - concepts:locking
  - concepts:synchronization
  - concepts:performance
level: advanced
category: language
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:systems-programmers
  - audiences:performance-engineers
---
<!-- course: concurrency_and_parallelism -->
# Concurrency and Parallelism

## Description
Concurrency and parallelism are two of the hardest topics in software engineering and two of the most poorly taught.
Most developers learn them piecemeal through a single language's `threading` library, then re-learn the same ideas
incompletely when they switch languages. This five day course is a unified, language-agnostic treatment of the
underlying concepts.

The course covers the distinction between concurrency and parallelism, modern hardware memory models, the spectrum
of concurrency primitives (locks, atomics, channels, actors, futures, async/await, structured concurrency),
lock-free data structures, common bug classes and how to find them, and the parallel programming techniques that
actually scale. Examples are drawn from `C++`, `Java`, Go, Rust, `Python` and `JavaScript`. Participants leave
able to reason about concurrent code regardless of language and to choose the right abstraction for the problem
in front of them.

## Duration
40 hours / 5 days

## Intended Audience
* senior developers who write concurrent code in any language
* systems programmers building libraries, runtimes or kernels
* performance engineers tuning concurrent workloads
* developers preparing for systems-level technical interviews

## Prerequisites
* several years of software development experience
* working knowledge of at least one language with native `threading` or async support
* basic familiarity with operating system concepts (processes, threads, memory)
* basic computer architecture (caches, memory hierarchy)

## Objectives
* clearly distinguish concurrency, parallelism and asynchrony
* reason about hardware and language memory models
* choose between locks, atomics, channels, actors and async/await for a given problem
* implement and reason about basic lock-free algorithms
* recognize, reproduce and fix the major bug classes (races, deadlocks, livelocks, ABA)
* analyze concurrent code for correctness and performance
* design data-parallel and task-parallel programs that scale

## Outline
<!-- chapter: concurrency-vs-parallelism-vs-asynchrony, duration: 2h -->
* Concurrency vs parallelism vs asynchrony
    * the textbook distinction
    * hardware perspective: cores, hyperthreads, vector units
    * runtime perspective: green threads, fibers, coroutines
    * `IO`-bound vs `CPU`-bound workloads
    * Amdahl's law and Gustafson's law
    * when parallelism is worth the cost
<!-- chapter: hardware-and-memory-models, duration: 4h -->
* Hardware and memory models
    * cache hierarchy and cache coherence
    * `MESI` and friends
    * the store buffer and memory barriers
    * sequential consistency, total store order, weak memory
    * acquire/release semantics
    * the `C++`, `Java` and Go memory models compared
    * data race vs race condition
<!-- chapter: threads-and-processes, duration: 2h -->
* Threads and processes
    * the OS thread abstraction
    * process vs thread vs fiber
    * thread-local storage
    * thread pools and their sizing
    * thread creation and destruction costs
    * `pthread`, `std::thread`, virtual threads, goroutines
<!-- chapter: locks-and-mutual-exclusion, duration: 3h -->
* Locks and mutual exclusion
    * `mutex` implementations and the `futex`
    * spin locks vs blocking locks
    * reader/writer locks
    * recursive locks and their pitfalls
    * fairness and starvation
    * the cost of contention
    * lock granularity and the lock-coupling pattern
<!-- chapter: atomics-and-lock-free-fundamentals, duration: 3h -->
* Atomics and lock-free fundamentals
    * atomic loads, stores, exchanges and compare-and-swap
    * memory orders in `C++`/`C11`/Rust
    * the ABA problem
    * hazard pointers and epoch-based reclamation
    * `RCU` (read-copy-update)
    * lock-free queues and stacks
    * wait-free vs lock-free vs obstruction-free
<!-- chapter: condition-variables-and-signaling, duration: 2h -->
* Condition variables and signaling
    * the wait/notify pattern
    * spurious wake-ups
    * predicate-based waiting
    * the lost wake-up problem
    * `pthread`, `std::condition_variable`, `Java` `Object.wait`
    * counting semaphores and barriers
<!-- chapter: channels-and-message-passing, duration: 3h -->
* Channels and message passing
    * `CSP` (Communicating Sequential Processes)
    * unbuffered, buffered and rendezvous channels
    * `select` over multiple channels
    * pipeline patterns
    * fan-in and fan-out
    * Go, Rust (`crossbeam`), `Kotlin` (Channel), `Erlang`
<!-- chapter: actors, duration: 2h -->
* Actors
    * the actor model and its history
    * mailbox semantics
    * supervision hierarchies
    * `Erlang`/`OTP`, Akka, `Orleans`, Elixir
    * actors vs `CSP` channels
    * common actor anti-patterns
<!-- chapter: futures-promises-and-async-await, duration: 3h -->
* Futures, promises and async/await
    * futures and promises across languages
    * cooperative scheduling
    * the `Python`, `JavaScript`, Rust, `C++` and `C#` async models
    * cancellation and timeouts
    * error propagation
    * the colored-function problem
    * structured concurrency: scopes, nurseries, `JEP 453`
<!-- chapter: data-parallelism, duration: 2h -->
* Data parallelism
    * map/filter/reduce on parallel collections
    * `OpenMP` for C/`C++`
    * `Java` parallel streams
    * `Rayon` for Rust
    * SIMD and vectorization
    * `GPU` data parallelism overview
<!-- chapter: task-parallelism-and-work-stealing, duration: 2h -->
* Task parallelism and work stealing
    * fork/join algorithms
    * work-stealing schedulers
    * `Cilk`, TBB, `Java` ForkJoinPool, `.NET` TPL
    * task granularity tuning
    * load balancing in practice
<!-- chapter: concurrency-bugs-and-how-to-find-them, duration: 4h -->
* Concurrency bugs and how to find them
    * data races
    * deadlocks and lock ordering
    * livelocks and starvation
    * priority inversion
    * the `ABA` problem revisited
    * memory ordering bugs
    * tools: `ThreadSanitizer`, Helgrind, DRD, `Java FlightRecorder`, Go race detector
<!-- chapter: testing-concurrent-code, duration: 2h -->
* Testing concurrent code
    * deterministic vs stochastic approaches
    * stress testing
    * model checking with `TLA+`, Stateright, `Jepsen`
    * randomized scheduling
    * property-based testing of concurrent code
<!-- chapter: performance-of-concurrent-code, duration: 2h -->
* Performance of concurrent code
    * false sharing and cache-line padding
    * NUMA effects on shared data
    * lock contention vs cache contention
    * scalability bottlenecks at high core counts
    * measuring concurrent code with `perf` and tracing
<!-- chapter: distributed-concurrency-preview, duration: 2h -->
* Distributed concurrency preview
    * how distributed systems differ from shared-memory concurrency
    * partial failure and timeouts
    * leader election and consensus at a glance
    * idempotency as a substitute for transactions
    * what carries over from local concurrency and what does not
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * hands-on debugging of representative concurrency bugs
    * group code review of concurrent code
    * recommended reading: `Goetz`, Herlihy, Williams, `Drepper`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
