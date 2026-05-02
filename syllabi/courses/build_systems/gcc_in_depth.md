---
tags:
  - tools:gcc
  - languages:c
  - languages:c++
  - hardware-and-embedded:compiler
  - hardware-and-embedded:toolchain
level: advanced
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:firmware-developers
  - audiences:performance-engineers
---
<!-- course: gcc_in_depth -->
# `GCC` in Depth

## Description
This advanced course provides an in-depth exploration of the GNU Compiler Collection (`GCC`),
covering the full compilation pipeline from preprocessing through linking. Participants will
learn how to leverage `GCC`'s powerful optimization capabilities, sanitizers, and diagnostic
tools to produce high-quality, performant binaries. The course also covers cross-compilation,
link-time optimization, profile-guided optimization, and static analysis, equipping developers
with the knowledge to get the most out of their toolchain.

## Duration
16 hours / 2 days

## Intended Audience
* C and `C++` developers who want to master the `GCC` toolchain for better code quality and performance.
* Embedded engineers who need to cross-compile and fine-tune binaries for target hardware.
* Firmware developers working with `GCC`-based toolchains for embedded platforms.
* Performance engineers seeking to optimize application performance through compiler techniques.

## Prerequisites
* `Solid` experience programming in C or `C++`.
* Familiarity with the `Linux` command line and build tools such as `make`.
* Basic understanding of how compilers and linkers work.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the full `GCC` compilation pipeline from source to binary.
* Apply optimization flags effectively and understand their trade-offs.
* Use sanitizers to detect memory errors, undefined behavior, and data races.
* Configure and perform cross-compilation for different target architectures.
* Implement link-time optimization and profile-guided optimization workflows.
* Leverage `GCC` static analysis and diagnostic features for code quality.

## Outline
<!-- chapter: the-gcc-compiler-pipeline, duration: 1h -->
* The `GCC` Compiler Pipeline
    * Overview of compilation stages
    * Preprocessing, compilation, `assembly`, and linking
    * Intermediate representations
    * Inspecting compiler output at each stage
    * Compiler driver vs individual tools
<!-- chapter: the-preprocessor, duration: 1h -->
* The Preprocessor
    * Macro definitions and expansion
    * Conditional compilation
    * Include paths and header search order
    * Predefined macros
    * Common preprocessor pitfalls
<!-- chapter: optimization-levels, duration: 2h -->
* Optimization Levels
    * -O0: no optimization and debugging
    * -O1: basic optimizations
    * -O2: standard production optimizations
    * -O3: aggressive optimizations
    * -Os: optimizing for size
    * -Ofast: beyond standard-compliant optimizations
    * Individual optimization flags and fine-tuning
    * Understanding optimization trade-offs
<!-- chapter: warning-flags, duration: 1h -->
* Warning Flags
    * -Wall, -Wextra, and -Wpedantic
    * Treating warnings as errors with -Werror
    * Selective warning suppression
    * Custom warning policies for projects
    * Warning flags for C vs `C++`
<!-- chapter: sanitizers, duration: 1h -->
* Sanitizers
    * AddressSanitizer (ASan): memory error detection
    * UndefinedBehaviorSanitizer (UBSan): detecting undefined behavior
    * ThreadSanitizer (TSan): data race detection
    * Combining sanitizers and runtime options
    * Sanitizer performance overhead and deployment strategies
<!-- chapter: cross-compilation, duration: 1h -->
* Cross-Compilation
    * Cross-compilation concepts and target triples
    * Setting up cross-compilation toolchains
    * Sysroot configuration
    * Building for `ARM`, `RISC-V`, and other architectures
    * Testing cross-compiled binaries with emulators
<!-- chapter: linker-scripts, duration: 1h -->
* Linker Scripts
    * Linker script syntax and structure
    * Memory layout and section placement
    * Symbol definitions and assignments
    * Custom linker scripts for embedded targets
    * Debugging linker issues
<!-- chapter: link-time-optimization-lto, duration: 2h -->
* Link-Time Optimization (LTO)
    * How LTO works in `GCC`
    * Enabling and configuring LTO
    * Fat LTO objects
    * LTO impact on build times and binary quality
    * Troubleshooting LTO issues
<!-- chapter: profile-guided-optimization-pgo, duration: 2h -->
* Profile-Guided Optimization (PGO)
    * PGO workflow: instrumentation, profiling, and optimization
    * Generating and collecting profile data
    * Applying profile data for optimization
    * Choosing representative workloads
    * Measuring PGO impact
<!-- chapter: static-analysis, duration: 2h -->
* Static Analysis
    * `GCC` built-in static analyzer (-fanalyzer)
    * Detecting common bug patterns
    * Analyzer warnings and diagnostics
    * Integrating static analysis into build workflows
    * Limitations and complementary tools
<!-- chapter: debugging-symbols-and-abi-compatibility, duration: 2h -->
* Debugging Symbols and ABI Compatibility
    * Debugging symbol formats (DWARF)
    * Debug information levels (-g, -g3, -ggdb)
    * Separate debug info files
    * ABI compatibility between `GCC` versions
    * Symbol versioning and library compatibility
    * Managing ABI stability in shared libraries

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
