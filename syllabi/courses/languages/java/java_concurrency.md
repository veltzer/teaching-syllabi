---
tags:
  - languages:java
  - concepts:concurrency
  - concepts:multithreading
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: java_concurrency -->
# `Java` Concurrency

## Description
This course provides comprehensive coverage of concurrency and multithreading in `Java`, from foundational `threading` concepts through modern features like virtual threads and structured concurrency. Students will learn to write correct, performant, and scalable concurrent `Java` applications using threads, executors, CompletableFuture, concurrent collections, and the Fork/Join framework. The course also covers the `Java` memory model, synchronization mechanisms, and techniques for detecting and preventing deadlocks and other concurrency hazards.

## Duration
24 hours / 3 days

## Intended Audience
* `Java` developers building high-performance, multi-threaded applications
* Backend developers working on concurrent server-side systems
* Developers who need a deep understanding of `Java` concurrency for system design and debugging

## Prerequisites
* `Solid` understanding of object-oriented programming principles
* Familiarity with basic data structures and algorithms

## Required Knowledge
* `Java` Programming

## Objectives
* Create and manage threads using Thread, Runnable, and executor services
* Write non-blocking asynchronous code with CompletableFuture
* Apply synchronization mechanisms to ensure thread safety
* Use concurrent collections and atomic variables for lock-free programming
* Leverage the Fork/Join framework and virtual threads for scalable parallelism
* Understand the `Java` memory model and diagnose concurrency issues

## Outline
<!-- chapter: threads-and-runnable, duration: 2h -->
* Threads and Runnable
    * Creating threads with Thread and Runnable
    * Thread lifecycle and states
    * Thread methods: join, sleep, interrupt
    * Daemon threads
    * ThreadLocal variables
    * Thread safety fundamentals
<!-- chapter: executors-and-thread-pools, duration: 2h -->
* Executors and Thread Pools
    * Executor, ExecutorService, and ScheduledExecutorService
    * Thread pool types: fixed, cached, single, scheduled
    * Callable and Future
    * Submitting and managing tasks
    * Graceful shutdown patterns
    * Custom ThreadFactory and rejection policies
<!-- chapter: completablefuture, duration: 2h -->
* CompletableFuture
    * Creating and completing futures
    * Chaining with thenApply, thenCompose, thenCombine
    * Exception handling with exceptionally and handle
    * Combining multiple futures with allOf and anyOf
    * `Async` variants and custom executors
    * Real-world composition patterns
<!-- chapter: synchronized-and-locks, duration: 2h -->
* synchronized and Locks
    * Intrinsic locks and synchronized blocks
    * ReentrantLock and ReadWriteLock
    * StampedLock for optimistic reads
    * Condition variables and signaling
    * Lock fairness and performance implications
    * Best practices for lock usage
<!-- chapter: concurrent-collections, duration: 2h -->
* Concurrent Collections
    * ConcurrentHashMap and its operations
    * CopyOnWriteArrayList and CopyOnWriteArraySet
    * ConcurrentLinkedQueue and ConcurrentLinkedDeque
    * BlockingQueue implementations
    * ConcurrentSkipListMap and ConcurrentSkipListSet
    * Choosing the right concurrent collection
<!-- chapter: atomic-variables, duration: 2h -->
* Atomic Variables
    * AtomicInteger, AtomicLong, AtomicReference
    * Compare-and-swap operations
    * AtomicStampedReference and the ABA problem
    * LongAdder and LongAccumulator
    * VarHandle for advanced atomic access
<!-- chapter: fork-join-framework, duration: 2h -->
* Fork/Join Framework
    * ForkJoinPool architecture and work stealing
    * RecursiveTask and RecursiveAction
    * Splitting strategies and granularity
    * Parallel streams and the common ForkJoinPool
    * Monitoring and tuning the pool
<!-- chapter: virtual-threads-project-loom, duration: 2h -->
* Virtual Threads (Project Loom)
    * Platform threads vs virtual threads
    * Creating and running virtual threads
    * Virtual thread scheduling and carrier threads
    * Scalability benefits for `I/O`-bound workloads
    * Pinning and its implications
    * Migration strategies from platform threads
<!-- chapter: structured-concurrency, duration: 2h -->
* Structured Concurrency
    * StructuredTaskScope and its subtypes
    * ShutdownOnFailure and ShutdownOnSuccess
    * Scoped values
    * Error handling in structured concurrency
    * Comparison with CompletableFuture and executors
<!-- chapter: memory-model-and-happens-before, duration: 3h -->
* Memory Model and Happens-Before
    * `Java` Memory Model overview
    * Visibility, ordering, and atomicity
    * Happens-before relationships
    * volatile keyword and its guarantees
    * `final-fields` and safe publication
    * Data races and their consequences
<!-- chapter: deadlock-detection, duration: 3h -->
* Deadlock Detection
    * Causes of deadlocks: lock ordering, nested locks
    * Livelock and starvation
    * Detecting deadlocks with thread dumps
    * `JMX` and programmatic deadlock detection
    * Prevention strategies and lock hierarchy
    * Diagnosing concurrency bugs with tools

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
