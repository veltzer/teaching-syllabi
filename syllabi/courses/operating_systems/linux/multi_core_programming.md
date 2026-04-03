---
tags:
  - infrastructure:linux
  - hardware-and-embedded:multi-core
  - practices:performance
  - concepts:concurrency
  - hardware-and-embedded:cache
  - concepts:synchronization
level: advanced
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: multi_core_programming -->
# Multi Core Programming

## Description
`C`/`C++` projects are hard to develop and maintain but provide performance gains relative to other
programming languages. But they also offer the ability to tune your application to the hardware architecture
that you are running on `top` of. Failure to do this tuning will result is application under performance.
This course is about the multi-core architecture, it's advantages and disadvantages and mostly, about how to
program efficiently `when` running on this platform.

## Duration
* 2 days for all topics.
* 1 day for some of the topics (you can pick).
* first four topics are a must.

## Intended Audience
* Seasoned `C`/`C++` developers who are not familiar with this information and the techniques presented.
* `Java` and other programming language programmers are also welcome and will benefit from the course but not as much as `C`/`C++` developers.

## Prerequisites
* experience with `C` programming
* familiarity with `Linux` command line

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of Multi Core Programming
* gain practical knowledge of Basics of scaling hardware
* gain practical knowledge of Basics of `CPU` design (how did we get here)
* gain practical knowledge of multi-core vs multi-`cpu`

## Outline
<!-- chapter: basics-of-scaling-hardware, duration: 1h -->
* Basics of scaling hardware
    * Why is Moore's law outdated
    * Why adding more CPUs is not a silver bullet
    * NUMA architectures.
<!-- chapter: basics-of-cpu-design-how-did-we-get-here, duration: 1h -->
* Basics of `CPU` design (how did we get here)
    * CICS
    * RISC
    * Pipeline CPUs
<!-- chapter: multi-core-vs-multi-cpu, duration: 1h -->
* multi-core vs multi-`cpu`
    * Definitions.
    * Exceptions.
<!-- chapter: caches, duration: 4h -->
* Caches
    * Types of caches
    * What are the 4 layers of cache?
    * `Linux`: finding out sizes of caches and cache lines
    * Which caches are shared among cores and which are not
    * Techniques to improve performance that have to do with cache
        * Cache thrashing
        * Making do with the size of cache you have
        * Allocating memory on boundaries
        * Decreasing information to fit in fewer cache lines
        * Inflating structures to take cache lines
        * Coupling data to increase performance
        * Removing rarely used data to increase performance
<!-- chapter: coherency, duration: 1h -->
* Coherency
    * Coherent vs non coherent platforms
    * How does this affect programming?
    * Solving coherency problems
<!-- chapter: memory-reordering, duration: 1h -->
* Memory reordering
    * What is it?
    * How does it affect programming?
    * Solving reordering problems (memory barriers)
    * Why volatile is evil
<!-- chapter: pipeline-architecture-and-its-effect-on-programming, duration: 1h -->
* Pipeline architecture and its effect on programming
    * Trying to be predictable
    * What to do `when` you are not predictable?
    * Telling the `CPU` where I'm going to branch to
<!-- chapter: sharing-and-solutions, duration: 2h -->
* Sharing and solutions
    * Sharing caches (and solutions)
    * Sharing mathematical processing units (and solutions)
    * Sharing crypto units (and solutions)
    * Sharing vector processing units (and solutions)
    * Sharing pipeline segments (and solutions)
<!-- chapter: cpu-topology, duration: 2h -->
* `CPU` topology
    * What is topology?
    * `Linux`: finding out your `CPU` topology.
    * `Linux`: forcing affinity on your own threads.
    * `Linux`: forcing affinity of other programs.
    * `Linux`: forcing affinity of OS threads.
    * `Linux` RT: forcing affinity of interrupt handlers
    * Changing number of cores at runtime?
<!-- chapter: synchronization-between-threads-or-processes, duration: 2h -->
* Synchronization between threads or processes
    * Share nothing
    * atomic operations
    * Lockless algorithms/lockless data structures
    * RCU/`COW`
    * Readers/Writer lock
    * Spinlock
    * `Futex`
    * `Mutex`
    * Semaphore

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
