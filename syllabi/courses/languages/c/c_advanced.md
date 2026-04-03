---
tags:
  - languages:c
  - concepts:programming
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: c_advanced -->
# `C` Advanced

## Description
This course covers advanced `C` programming topics for experienced developers working on `Linux`. Topics include advanced debugging with `gdb`, memory allocation strategies and leak detection, dynamic shared objects, performance measurement and optimization, multi-`threading` with pthreads, and managing large `C` projects. The course also covers `C99` features and the `C` pre-processor in depth.

## Duration
24 hours / 3 days

## Intended Audience
* `C` programmers
* embedded and systems software developers

## Prerequisites
* working experience with `c`
* `solid` experience with `C` programming

## Objectives
* understand the core concepts and principles of `C` Advanced
* gain practical knowledge of Debugging using `gdb` and friends
* gain practical knowledge of Various ways of allocation memory
* gain practical knowledge of Memory leaks and memory corruption

## Outline
<!-- chapter: debugging-using-gdb-and-friends, duration: 2h -->
* Debugging using `gdb` and friends
    * configuring source code locations.
    * calling functions.
    * changing variables on the fly.
    * reverse debugging.
    * pretty printing of structures.
    * Hardware breakpoints as opposed to software ones.
<!-- chapter: various-ways-of-allocation-memory, duration: 3h -->
* Various ways of allocation memory
    * `malloc(3)`.
    * `malloc(3)` replacements for debugging and performance.
    * how `malloc` works and what are its problems.
    * obstacks.
    * pool per thread.
    * calling `sbrk(2)` or `mmap(2)` directly.
    * allocating on the stack: `c99` style dynamic arrays.
    * allocating on the stack: `alloca(3)`.
    * data segment: bss allocations.
    * date segment: initialized allocations.
    * data segment: const allocations.
<!-- chapter: memory-leaks-and-memory-corruption, duration: 1h -->
* Memory leaks and memory corruption
    * mprotect and friends.
    * shaking things up to `find` bugs.
    * padding to detect memory corruption.
    * `malloc` debugging in the standard library (`mcheck(3)`)
    * `dmalloc`
<!-- chapter: c-pre-processor, duration: 1h -->
* `C`-Pre processor
    * var args macros
    * quoting in macros
    * writing type independent functions using the pre-processor.
    * list of out of the box defines
<!-- chapter: dynamic-shared-objects, duration: 3h -->
* Dynamic Shared Objects
    * How to prepare a DSO.
    * ldd, ld.so
    * Versions and dependencies of DSOs.
    * DSO and rpath.
    * GOT, PLT and DSO performance vs static library performance.
    * Weak symbols in `C`.
    * Resolver functions.
    * LD_LIBRARY_PATH, LD_PRELOAD, LD_RUN_PATH, ldconfig
    * `dlopen(3)`, `dlsym(3)` and their performance.
<!-- chapter: c-technical-issues, duration: 1h -->
* `C` technical issues
    * 32<->64 bit issues and `C` programming.
<!-- chapter: performance-in-c, duration: 2h -->
* Performance in `C`
    * inline.
    * compiler attributes for functions.
    * restricted pointers.
    * why you should use the standard libraries as much as possible.
    * using `CPU` specific libraries.
    * `CPU` cache lines and performance.
<!-- chapter: advanced-topics-in-make, duration: 1h -->
* Advanced topics in `Make`
    * Non recursive `make` approach.
    * Handling dependencies automatically for source files.
    * Managing a large project.
<!-- chapter: issues-with-large-c-projects, duration: 2h -->
* Issues with large `C` projects
    * h `file` organization in large projects.
    * private vs public h files.
    * helping the debugger `find` all your source code for debugging.
    * versioning object files, libraries and executables.
    * building large projects.
<!-- chapter: measuring-performance-in-c, duration: 1h -->
* Measuring performance in `C`
    * tools: callgrind, `perf`, oprofile, gperf
    * measuring it yourself: `gettimeofday()`, RDTSC
<!-- chapter: c99-issues, duration: 5h -->
* `C99` issues
    * `inline-functions`
    * intermingled declarations and code
    * new data types
    * variable-length arrays
    * flexible `array` members
    * one line comments
    * new library functions
    * new headers
    * type-generic math
    * improved floating point support
    * designated initializers
    * compound literals
    * variadic macros
    * restrict keyword
    * universal character names
    * static in `array` indices
<!-- chapter: multi-threading-and-synchronization-in-c-on-linux, duration: 2h -->
* Multi-`threading` and Synchronization in `C` on `Linux`
    * pthreads
    * compiler barriers and machine barriers
    * review of all synchronization mechanisms
    * transactional memory (new in core i7)

## References
* [`C99`](`https`://en.wikipedia.org/wiki/`C99`)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
