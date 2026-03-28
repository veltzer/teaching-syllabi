---
tags:
  - infrastructure:linux
  - practices:debugging
  - tools:gdb
  - tools:valgrind
  - practices:sanitizers
  - practices:performance
  - concepts:multithreading
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - practices:devops
  - audiences:performance-engineers
---
# `Linux` Debugging

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Linux` Debugging and Troubleshooting is a comprehensive course focused on mastering the art and science of debugging complex `C`/`C++` applications on `Linux` systems. From basic debugging techniques to hunting elusive Heisenbugs, this course covers the full spectrum of debugging methodologies, tools, and strategies used by professional developers to diagnose and fix the most challenging software defects.
Participants will learn to use industry-standard debugging tools, analyze complex runtime issues, debug multi-threaded and distributed applications, and tackle non-deterministic bugs that appear only in production environments.
This course emphasizes practical, real-world debugging scenarios including memory corruption, race conditions, performance bottlenecks, and system-level issues that affect application behavior.

This course covers `GDB` 12+, modern `Valgrind`, LLDB, and current `Linux` debugging tools. Legacy debugging techniques and deprecated tools are not discussed.

## Duration
40 hours / 5 days

## Intended Audience
* `C`/`C++` developers debugging complex applications
* System programmers dealing with low-level bugs
* `DevOps` engineers troubleshooting production issues
* QA engineers performing deep technical analysis
* Performance engineers identifying bottlenecks
* Technical leads responsible for code quality and reliability

## Prerequisites
* Strong `C`/`C++` programming experience
* Understanding of `Linux` system programming
* Familiarity with multi-threaded programming
* Basic knowledge of computer architecture
* Command line proficiency in `Linux`

## Objectives
* Master `GDB` and advanced debugging techniques
* Identify and fix memory-related bugs efficiently
* Debug multi-threaded and concurrent applications
* Diagnose and resolve Heisenbugs and race conditions
* Use dynamic analysis tools for runtime debugging
* Implement production debugging strategies
* Analyze core dumps and post-mortem debugging
* Apply systematic debugging methodologies

## Outline

* Introduction to Debugging Methodology
    * Scientific method in debugging
    * Hypothesis-driven debugging
    * Binary search debugging
    * Minimal reproducible examples
    * Bug classification and triage
    * Documentation and bug tracking
    * Debugging psychology and cognitive biases

* `GDB` Fundamentals
    * `GDB` architecture and concepts
    * Compilation for debugging (-g, -O0, -ggdb3)
    * Starting and attaching to processes
    * Breakpoints and watchpoints
    * Conditional breakpoints
    * Stepping through code
    * Examining variables and memory
    * Call stack navigation
    * Source code navigation

* Advanced `GDB` Features
    * `GDB` scripting and automation
    * `Python` extensions in `GDB`
    * Pretty printers
    * Reverse debugging (record and replay)
    * Remote debugging
    * Multi-process debugging
    * Catchpoints and syscall tracing
    * `GDB` MI (Machine Interface)
    * Custom commands and hooks

* LLDB and Alternative Debuggers
    * LLDB basics and comparison with `GDB`
    * LLDB command syntax
    * Data formatters in LLDB
    * `IDE` integration (VS Code, CLion)
    * TUI mode debugging
    * DDD (Data Display Debugger)
    * Console vs GUI debugging

* Static Analysis Tools
    * Compiler warnings and sanitizers
    * Clang Static Analyzer
    * Cppcheck
    * PVS-Studio basics
    * Coverity concepts
    * PC-lint/PC-lint Plus
    * Integration with build systems
    * False positive management

* Memory Bug Categories
    * Buffer overflows and underflows
    * Use-after-free bugs
    * Double-free errors
    * Memory leaks
    * Uninitialized memory usage
    * Stack corruption
    * Heap corruption
    * Invalid pointer dereference

* `Valgrind` Memory Debugging
    * Memcheck tool in depth
    * Leak detection and analysis
    * Cachegrind for cache profiling
    * Helgrind for thread errors
    * Massif heap profiler
    * DHAT dynamic heap analysis
    * `Valgrind` suppression files
    * Custom memory allocators with `Valgrind`

* AddressSanitizer (ASan)
    * ASan architecture and overhead
    * Compilation and runtime options
    * Understanding ASan reports
    * Memory poisoning concepts
    * Stack buffer overflow detection
    * Global buffer overflow detection
    * Use-after-return detection
    * ASan with production code

* Memory Debugging Techniques
    * Custom memory allocators for debugging
    * Guard pages and electric fence
    * Memory pattern filling
    * Heap consistency checking
    * Memory usage tracking
    * Smart pointers and `RAII`
    * Memory pool debugging
    * Debugging memory-mapped files

* Core Dump Analysis
    * Core dump generation and configuration
    * Analyzing core files with `GDB`
    * Extracting information from stripped binaries
    * Matching core dumps to source code
    * Automated core dump analysis
    * Core dump management in production
    * Debugging info packages
    * Mini-dumps and custom crash handlers

* Multi-threading Bugs
    * Race conditions
    * Deadlocks and livelocks
    * Priority inversion
    * Thread starvation
    * ABA problems
    * Memory ordering issues
    * False sharing
    * Thread-safety violations

* Thread Debugging with `GDB`
    * Thread-specific breakpoints
    * Switching between threads
    * All-stop vs non-stop mode
    * Thread apply commands
    * Scheduler locking
    * Thread-local storage debugging
    * Debugging thread creation/destruction

* ThreadSanitizer (TSan)
    * TSan principles and implementation
    * Data race detection
    * Deadlock detection
    * Understanding TSan reports
    * TSan suppressions
    * Performance impact
    * TSan with real applications
    * Limitations and false positives

* Helgrind and DRD
    * Helgrind race detection
    * Lock order violation detection
    * Comparing Helgrind and DRD
    * `POSIX` thread `API` checking
    * Custom synchronization primitives
    * Performance considerations

* Advanced Synchronization Debugging
    * Lock-free algorithm debugging
    * Atomic operation debugging
    * Memory barrier issues
    * Debugging condition variables
    * Semaphore debugging
    * Read-write lock issues
    * Futex debugging
    * Event ordering analysis

* Understanding Heisenbugs
    * Definition and characteristics
    * Why Heisenbugs occur
    * Observer effect in debugging
    * Timing-dependent bugs
    * Environment-sensitive bugs
    * Optimization-related bugs
    * Undefined behavior manifestation

* Reproducing Non-Deterministic Bugs
    * Stress testing techniques
    * Fuzzing and property-based testing
    * Record and replay systems
    * rr (record and replay) debugger
    * Deterministic scheduling
    * Environment control
    * Statistical debugging
    * Chaos engineering for debugging

* Race Condition Hunting
    * Systematic concurrency testing
    * Schedule exploration
    * Delay injection
    * CPU affinity manipulation
    * Priority manipulation
    * Intel Inspector
    * Dynamic race detection
    * Lock-free debugging strategies

* Timing and Performance Bugs
    * Performance regression debugging
    * Latency spike investigation
    * CPU profiling with perf
    * Cache miss analysis
    * Lock contention analysis
    * I/O bottleneck debugging
    * Context switch debugging
    * Interrupt and preemption issues

* Production Debugging Techniques
    * Non-intrusive debugging methods
    * eBPF for production tracing
    * Dynamic instrumentation
    * Logging strategies
    * Distributed tracing
    * Debugging without symbols
    * Customer site debugging
    * Debugging containerized applications

* Dynamic Binary Instrumentation
    * Intel Pin framework
    * DynamoRIO basics
    * Frida for runtime manipulation
    * Custom instrumentation tools
    * Binary analysis and patching
    * Runtime code modification
    * `API` hooking and interception

* System-Level Debugging
    * strace advanced usage
    * ltrace for library calls
    * SystemTap scripting
    * ftrace for kernel tracing
    * perf events and counters
    * /proc filesystem debugging
    * netstat and network debugging
    * inotify for file system debugging

* Specialized Debugging Tools
    * UndefinedBehaviorSanitizer (UBSan)
    * LeakSanitizer standalone usage
    * MemorySanitizer for uninitialized memory
    * Intel VTune Profiler
    * AMD uProf
    * Heap profilers comparison
    * GPU debugging basics
    * JTAG debugging concepts

* Debugging Best Practices
    * Defensive programming techniques
    * Assertion strategies
    * Logging best practices
    * Error handling patterns
    * Unit testing for debugging
    * Continuous debugging
    * Debugging documentation
    * Team debugging practices

* Post-Mortem and Failure Analysis
    * Crash dump analysis automation
    * Symbol servers and debugging symbols
    * Minidump analysis
    * Black box analysis
    * Statistical crash analysis
    * Bug pattern recognition
    * Root cause analysis methodology
    * Debugging metrics and KPIs

<!-- Topics from the old `linux_debugging_old.md` not covered above:
- `MMU` internals: how it works, what programs can/can't do, memory page limitations
- Legacy memory debugging tools: `efence`, `dmalloc`, `MPatrol`
- "Earliest point principle": sparse allocator, `ulimit`, changing r/w attributes of memory pages, injecting errors
- Stack structure: stacks & interrupts, infinite recursion
- Linker debugging: `ld`, `LD_PRELOAD`, overriding symbols
- Misc: dynamic loading/unloading code, `C++` name mangling, basic assembly for debugging, system logger, listing open files/ports
- Programming for better debugging: managing `changesets`, writing naive object versions, modular code for debugging
-->

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
