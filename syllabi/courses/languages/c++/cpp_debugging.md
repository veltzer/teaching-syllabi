---
tags:
  - languages:c++
  - practices:debugging
  - tools:gdb
  - tools:valgrind
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:performance-engineers
---
<!-- course: cpp_debugging -->
# `C++` Debugging

## Description
This course provides comprehensive training in debugging `C++` applications using industry-standard tools. Participants will master `GDB`, `Valgrind`, sanitizers, and reverse debugging techniques. The course covers debugging multi-threaded code, template-heavy codebases, and production systems, equipping developers with the skills to diagnose and resolve the most challenging `C++` bugs efficiently.

## Duration
16 hours / 2 days

## Intended Audience
* `C++` developers who need to diagnose complex bugs efficiently
* Embedded engineers debugging on target and host systems
* Performance engineers investigating memory and concurrency issues

## Prerequisites
* Working experience with `C++` programming
* Familiarity with `Linux` command-line tools
* Basic understanding of multi-threaded programming concepts

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Master `GDB` for interactive and scripted debugging sessions
* Use `Valgrind` tools to detect memory errors, data races, and cache inefficiencies
* Apply address, thread, and undefined behavior sanitizers during development
* Analyze core dumps to diagnose crashes in deployed applications
* Use reverse debugging with rr to trace bugs backwards from failure
* Debug multi-threaded and template-heavy `C++` code effectively

## Outline
<!-- chapter: gdb-mastery, duration: 3h -->
* `GDB` Mastery
    * Compiling for debugging: -g, -Og, and debug info levels
    * Navigating source code and stack frames
    * Conditional breakpoints and commands
    * Watchpoints for data changes
    * Catchpoints for exceptions and system calls
    * Pretty printers for `STL` containers
    * Scripting `GDB` with `Python`
    * `GDB` TUI mode and dashboard
    * Remote debugging with `gdbserver`
<!-- chapter: valgrind-suite, duration: 2h -->
* `Valgrind` Suite
    * Memcheck for memory errors and leaks
    * Suppression files for known issues
    * Helgrind for data race detection
    * DRD as an alternative thread checker
    * Cachegrind and Callgrind for cache and call profiling
    * Massif for heap profiling
    * Interpreting `Valgrind` output and common false positives
<!-- chapter: sanitizers, duration: 2h -->
* Sanitizers
    * AddressSanitizer (ASan): buffer overflows and use-after-free
    * ThreadSanitizer (TSan): data races and deadlocks
    * UndefinedBehaviorSanitizer (UBSan): integer overflow, null dereference, alignment
    * MemorySanitizer (MSan): uninitialized memory reads
    * LeakSanitizer (LSan): memory leak detection
    * Combining sanitizers and their limitations
    * Integrating sanitizers into build systems and CI
<!-- chapter: core-dump-analysis, duration: 1h -->
* Core Dump Analysis
    * Configuring core dump generation
    * Loading core dumps in `GDB`
    * Extracting stack traces and variable state
    * Analyzing core dumps from stripped binaries
    * Automated core dump collection and analysis
<!-- chapter: reverse-debugging-with-rr, duration: 1h -->
* Reverse Debugging with rr
    * Recording program execution
    * Replaying and stepping backwards
    * Reverse continue and reverse stepping
    * `When` rr shines: non-deterministic bugs
    * Limitations and performance considerations
<!-- chapter: debugging-multi-threaded-code, duration: 1h -->
* Debugging Multi-Threaded Code
    * Thread-aware debugging in `GDB`
    * Switching between threads and inspecting state
    * Reproducing race conditions
    * Debugging deadlocks and lock ordering issues
    * Using TSan and Helgrind together
<!-- chapter: debugging-templates, duration: 2h -->
* Debugging Templates
    * Reading template error messages
    * Strategies for simplifying template diagnostics
    * Using static_assert for early error detection
    * Debugging template instantiation with compiler flags
    * Concept-based constraints for better diagnostics
<!-- chapter: production-debugging, duration: 2h -->
* Production Debugging
    * Debugging optimized code (-O2, -O3)
    * Split debug info and debuginfod
    * Attaching to running processes
    * Using `perf` and `strace` for initial triage
    * Logging and tracing strategies for production systems
    * Post-mortem analysis workflow
<!-- chapter: ide-debugging, duration: 2h -->
* IDE Debugging
    * Debugging with `Visual Studio Code` and `CLion`
    * Configuring launch and attach configurations
    * Integrating `GDB` and LLDB backends
    * Visual breakpoints, watch expressions, and memory views
    * Remote debugging from an IDE

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
