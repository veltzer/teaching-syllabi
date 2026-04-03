---
tags:
  - languages:java
  - tools:jvm
  - practices:performance
  - practices:profiling
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:performance-engineers
---
<!-- course: java_performance_tuning -->
# `Java` Performance Tuning

## Description
This course provides an in-depth exploration of `Java` performance tuning techniques.
Participants will learn how the `JVM` executes code, how garbage collection algorithms
work, and how to use modern profiling and diagnostic tools to identify and resolve
performance bottlenecks. The course covers heap analysis, thread dump analysis,
JIT compilation internals, and rigorous benchmarking methodologies.

## Duration
24 hours / 3 days

## Intended Audience
* Experienced `Java` developers who want to optimize application performance.
* Performance engineers responsible for tuning `Java` applications in production.

## Prerequisites
* `Solid` experience programming in `Java`.
* Familiarity with `JVM` basics and command-line tools.

## Objectives
* Participants will gain a deep understanding of
    * `JVM` architecture and how it affects performance.
    * Garbage collection algorithms and how to tune them.
    * How to use profiling tools to identify bottlenecks.
    * Memory leak detection and prevention strategies.
    * JIT compilation and its impact on runtime performance.
    * Rigorous benchmarking with JMH.

## Outline
<!-- chapter: jvm-architecture, duration: 2h -->
* `JVM` Architecture
    * Class loading subsystem
    * Runtime data areas
    * Execution engine
    * Memory model overview
    * Stack vs heap allocation
<!-- chapter: garbage-collection-fundamentals, duration: 2h -->
* Garbage Collection Fundamentals
    * Object lifecycle and reachability
    * Generational garbage collection
    * GC roots and reference types
    * GC pauses and safe points
<!-- chapter: garbage-collection-algorithms, duration: 2h -->
* Garbage Collection Algorithms
    * G1 garbage collector
    * ZGC — low-latency garbage collection
    * Shenandoah garbage collector
    * Parallel and CMS collectors
    * Choosing the right collector
<!-- chapter: gc-tuning, duration: 2h -->
* GC Tuning
    * Heap sizing strategies
    * GC logging and log analysis
    * Tuning collector-specific parameters
    * Metaspace configuration
    * String deduplication
<!-- chapter: heap-analysis, duration: 2h -->
* Heap Analysis
    * Heap dump generation
    * Analyzing heap dumps with MAT
    * Identifying memory leaks
    * Retained size vs shallow size
    * Dominator trees
<!-- chapter: profiling-tools, duration: 2h -->
* Profiling Tools
    * `Java` Flight Recorder (JFR)
    * `async`-profiler
    * VisualVM
    * JDK Mission Control
    * Sampling vs instrumentation profiling
<!-- chapter: memory-leaks, duration: 3h -->
* Memory Leaks
    * Common causes of memory leaks in `Java`
    * ClassLoader leaks
    * Collection-related leaks
    * Listener and callback leaks
    * Native memory leaks
<!-- chapter: thread-dumps-and-cpu-profiling, duration: 3h -->
* Thread Dumps and `CPU` Profiling
    * Capturing thread dumps
    * Analyzing thread states
    * Detecting deadlocks and contention
    * `CPU` flame graphs
    * Hot method identification
<!-- chapter: jit-compilation, duration: 3h -->
* JIT Compilation
    * Tiered compilation
    * C1 and `C2` compilers
    * Inlining and escape analysis
    * Deoptimization
    * Inspecting JIT output
<!-- chapter: benchmarking-with-jmh, duration: 3h -->
* Benchmarking with JMH
    * JMH fundamentals
    * Writing correct microbenchmarks
    * Benchmark modes and parameters
    * Avoiding common benchmarking pitfalls
    * Interpreting results

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
