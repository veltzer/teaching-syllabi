---
tags:
  - languages:python
  - concepts:concurrency
  - concepts:async-programming
level: advanced
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: python_async_programming -->
# `Python` `Async` Programming

## Description
This course provides a deep dive into asynchronous programming in `Python` using `asyncio` and related tools. Students will learn how the event loop works, how to write coroutines, manage tasks and futures, and build high-performance async applications. The course covers advanced topics including structured concurrency with TaskGroup, async generators, synchronization primitives, and integration with concurrent.futures for mixed async/threaded workloads. Emphasis is placed on debugging techniques and performance patterns for real-world async systems.

## Duration
16 hours / 2 days

## Intended Audience
* `Python` developers building `I/O`-bound or network-heavy applications
* Backend developers seeking to improve throughput with asynchronous patterns
* Developers working with async web frameworks such as `FastAPI` or aiohttp

## Prerequisites
* `Solid` understanding of functions, generators, and decorators
* Familiarity with networking and `I/O` concepts

## Required Knowledge
* `Python` Programming

## Objectives
* Understand the `asyncio` event loop and its execution model
* Write correct and efficient coroutines using async/await syntax
* Manage concurrent work with tasks, futures, and TaskGroup
* Use async generators and async context managers effectively
* Apply synchronization primitives to coordinate concurrent coroutines
* Debug and profile async code to identify bottlenecks and common pitfalls

## Outline
<!-- chapter: the-asyncio-event-loop, duration: 1h -->
* The `asyncio` Event Loop
    * How the event loop works
    * Running and managing the loop
    * Event loop internals and selectors
    * Custom event loop policies
    * Integrating with synchronous code
<!-- chapter: coroutines-tasks-and-futures, duration: 2h -->
* Coroutines, Tasks, and Futures
    * Defining coroutines with `async def`
    * await expressions and suspension points
    * Creating and scheduling tasks
    * Future objects and callbacks
    * Gathering and waiting for multiple coroutines
    * `asyncio`.wait vs `asyncio`.gather
<!-- chapter: async-await-syntax-in-depth, duration: 1h -->
* async/await Syntax In Depth
    * Awaitable protocol
    * Chaining coroutines
    * `Return-values` and exception propagation
    * Cancellation and CancelledError
    * Timeouts with `asyncio`.timeout and `asyncio`.wait_for
<!-- chapter: aiohttp-and-async-http, duration: 1h -->
* aiohttp and `Async` `HTTP`
    * Client sessions and connection pooling
    * Making concurrent `HTTP` requests
    * Server-side async handlers
    * Streaming responses
    * Middleware and signal handling
<!-- chapter: async-generators-and-async-context-managers, duration: 1h -->
* `Async` Generators and `Async` Context Managers
    * `async for` and `async with` syntax
    * Writing async generators with yield
    * `Async` iterator protocol
    * @asynccontextmanager decorator
    * Resource management patterns
<!-- chapter: structured-concurrency-with-taskgroup, duration: 2h -->
* Structured Concurrency with TaskGroup
    * TaskGroup fundamentals and motivation
    * Creating and managing task groups
    * Error handling and cancellation in task groups
    * Nested task groups
    * Comparison with gather and wait
<!-- chapter: concurrent-futures-integration, duration: 2h -->
* concurrent.futures Integration
    * ThreadPoolExecutor and ProcessPoolExecutor
    * Running blocking code in executors
    * loop.run_in_executor patterns
    * Mixing threads, processes, and coroutines
    * `When` to use threads vs async
<!-- chapter: synchronization-primitives, duration: 2h -->
* Synchronization Primitives
    * Lock, Event, Condition, Semaphore
    * BoundedSemaphore for resource limiting
    * Barrier for coordinating coroutines
    * Queue for producer-consumer patterns
    * Avoiding deadlocks in async code
<!-- chapter: debugging-async-code, duration: 2h -->
* Debugging `Async` Code
    * Debug mode in `asyncio`
    * Detecting slow callbacks and blocked coroutines
    * Logging and tracing async execution
    * Common pitfalls: forgotten await, unawaited coroutines
    * Using `asyncio` debug tools and third-party profilers
<!-- chapter: performance-patterns, duration: 2h -->
* Performance Patterns
    * Batching and throttling concurrent requests
    * Connection pooling and resource reuse
    * Backpressure and flow control
    * Memory considerations with large task sets
    * Benchmarking async vs synchronous approaches

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
