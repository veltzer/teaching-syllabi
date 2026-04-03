---
tags:
  - concepts:parallel-computing
  - concepts:multithreading
  - concepts:concurrency
  - hardware-and-embedded:multi-core
  - infrastructure:linux
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:performance-engineers
---
<!-- course: parallel_programming -->
# Parallel Programming

## Description
This advanced course covers the theory and practice of parallel programming on modern multi-core systems. Participants will learn to exploit hardware parallelism using multiple programming models including `POSIX` threads, `OpenMP`, SIMD intrinsics, and `Intel TBB`. The course addresses the critical challenges of parallel software development, including memory models, cache coherency, synchronization, and common pitfalls such as race conditions, deadlocks, and false sharing.

Emphasis is placed on writing correct, scalable, and performant parallel code, with thorough coverage of profiling and debugging techniques for parallel applications.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers building high-performance applications
* Embedded engineers working with multi-core processors
* Performance engineers optimizing compute-intensive workloads
* Systems programmers targeting `Linux` platforms

## Prerequisites
* Strong proficiency in `C` or `C++`
* Basic understanding of `POSIX` threads
* Familiarity with `Linux` development environment
* Understanding of computer architecture basics (`CPU`, cache, memory)

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand modern multi-core architecture and its impact on software
* Write parallel programs using `POSIX` threads, `OpenMP`, and `Intel TBB`
* Apply SIMD/vectorization techniques for data-level parallelism
* Reason about memory models and cache coherency
* Implement lock-free data structures
* Design and implement parallel algorithms
* Profile and debug parallel applications
* Identify and fix race conditions, deadlocks, and false sharing

## Outline
<!-- chapter: multi-core-architectures, duration: 2h -->
* Multi-Core Architectures
    * Evolution of processor architectures
    * Multi-core and many-core designs
    * Cache hierarchy (L1, L2, L3)
    * NUMA architecture
    * Memory buses and bandwidth
    * Hardware threads and hyper-`threading`
    * Implications for software design

<!-- chapter: threading-models, duration: 2h -->
* `Threading` Models
    * Process vs thread parallelism
    * User-space vs kernel threads
    * Thread pools
    * Task-based parallelism
    * Fork-join model
    * Work stealing
    * Choosing the right model

<!-- chapter: posix-threads-review, duration: 2h -->
* `POSIX` Threads Review
    * Thread creation and lifecycle
    * Mutexes and condition variables
    * Read-write locks
    * Barriers and semaphores
    * Thread-local storage
    * Thread safety patterns
    * `POSIX` threads limitations

<!-- chapter: openmp, duration: 2h -->
* `OpenMP`
    * `OpenMP` programming model
    * Parallel regions and work sharing
    * Loop parallelism
    * Sections and tasks
    * Data sharing clauses
    * Reduction operations
    * Nested parallelism
    * `OpenMP` 5.x features

<!-- chapter: simd-and-vectorization, duration: 2h -->
* SIMD and Vectorization
    * SIMD instruction sets (`SSE`, AVX, AVX-512)
    * Auto-vectorization by compilers
    * Intrinsics programming
    * Data alignment requirements
    * Vectorization-friendly data structures
    * Compiler hints and pragmas
    * Performance gains and limitations

<!-- chapter: intel-tbb, duration: 2h -->
* `Intel TBB`
    * TBB architecture overview
    * Parallel algorithms (parallel_for, parallel_reduce, parallel_pipeline)
    * Task scheduler
    * Concurrent containers
    * Flow graph
    * Scalable memory allocation
    * Integration with other frameworks

<!-- chapter: memory-models, duration: 2h -->
* Memory Models
    * Sequential consistency
    * Relaxed memory models
    * `C++11` memory model
    * Memory ordering (acquire, release, relaxed)
    * Memory barriers and fences
    * Compiler reordering
    * Hardware memory ordering

<!-- chapter: cache-coherency, duration: 2h -->
* Cache Coherency
    * MESI protocol
    * Cache line ownership
    * Cache line bouncing
    * False sharing detection and prevention
    * Cache-friendly data structures
    * Padding and alignment strategies
    * NUMA-aware programming

<!-- chapter: lock-free-data-structures, duration: 2h -->
* Lock-Free Data Structures
    * Compare-and-swap operations
    * Atomic operations
    * Lock-free stacks and queues
    * ABA problem and solutions
    * Hazard pointers
    * Read-copy-update (RCU)
    * `When` to use lock-free designs

<!-- chapter: parallel-algorithms, duration: 2h -->
* Parallel Algorithms
    * Parallel sorting algorithms
    * Parallel reduction and scan
    * Divide and conquer parallelism
    * Pipeline parallelism
    * Map-reduce patterns
    * Load balancing strategies
    * Scalability analysis (Amdahl's law, Gustafson's law)

<!-- chapter: profiling-parallel-code, duration: 2h -->
* Profiling Parallel Code
    * Performance metrics for parallel programs
    * Profiling tools (`perf`, VTune, `Valgrind`/Helgrind)
    * Identifying scalability bottlenecks
    * Thread contention analysis
    * Cache performance analysis
    * Roofline model
    * Benchmarking methodology

<!-- chapter: common-pitfalls, duration: 2h -->
* Common Pitfalls
    * Race conditions and data races
    * Deadlocks and livelocks
    * Priority inversion
    * False sharing
    * Over-synchronization
    * Non-deterministic bugs
    * Debugging strategies and tools
    * Best practices for correct parallel code

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
