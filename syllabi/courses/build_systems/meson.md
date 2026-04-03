---
tags:
  - tools:meson
  - build:c
  - build:cpp
  - build:cross-compilation
  - practices:build-automation
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:embedded-developers
  - audiences:systems-programmers
---
<!-- course: meson -->
# `Meson`

## Description
`Meson` is a modern, fast, and user-friendly build system designed for `C`, `C++`, and a growing number of other
languages, with a focus on speed and developer experience. This course teaches participants to configure and
maintain `Meson`-based projects from small libraries to large multi-target codebases, covering dependency
management through `pkg-config` and `WrapDB`, and advanced cross-compilation scenarios common in embedded
development. Participants will compare `Meson` with `CMake` and leave with the practical skills to migrate
existing projects or start new ones confidently.

## Duration
16 hours / 2 days

## Intended Audience
* `C` and `C++` developers who want a faster, more readable alternative to `CMake` or `Autotools`.
* Embedded and systems engineers who need reliable cross-compilation support.
* Build engineers responsible for configuring and optimising native code build pipelines.

## Prerequisites
* Working knowledge of `C` or `C++` programming.
* Familiarity with the command line on `Linux` or `macOS`.
* Basic understanding of compilers and linkers is assumed.

## Objectives
* Understand `Meson`'s design philosophy and advantages over traditional build systems.
* Write and maintain `meson.build` files using `Meson`'s `Python`-like syntax.
* Configure build options and handle multiple build types.
* Build static and shared libraries as well as executables.
* Manage external dependencies with `pkg-config` and the `WrapDB` package manager.
* Set up and perform cross-compilation for embedded targets.
* Write and run unit tests within the `Meson` framework.
* Integrate `Meson` projects with popular `IDE`s and `CI/CD` pipelines.
* Evaluate `Meson` vs `CMake` for new and existing projects.

## Outline
<!-- chapter: introduction-to-meson, duration: 1h -->
* Introduction to `Meson`:
    * Why `Meson`? Problems with `Autotools`, `Make`, and `CMake`.
    * `Meson` design goals: speed, readability, correctness.
    * Installing `Meson` and `Ninja`.
    * First build: hello world project.
<!-- chapter: meson-syntax-and-build-files, duration: 2h -->
* `Meson` Syntax and Build Files:
    * The `meson.build` `file` structure.
    * Variables, strings, arrays, and dictionaries.
    * Control flow: conditionals and loops.
    * Functions and keyword arguments.
    * Project declaration and versioning.
<!-- chapter: configuring-projects, duration: 2h -->
* Configuring Projects:
    * Build directories and the `meson setup` command.
    * Built-in and user-defined build options.
    * The `meson configure` command and `meson_options.txt`.
    * Build types: debug, release, minsize.
    * Feature options and optional components.
<!-- chapter: building-libraries-and-executables, duration: 2h -->
* Building Libraries and Executables:
    * Declaring executables and linking.
    * Static, shared, and module libraries.
    * Include directories and compile flags.
    * Install targets and `RPATH` handling.
    * Subprojects and code reuse.
<!-- chapter: dependency-management, duration: 2h -->
* Dependency Management with `pkg-config` and `WrapDB`:
    * Finding system dependencies with `dependency()`.
    * Using `pkg-config` for third-party libraries.
    * The `WrapDB` package manager and `.wrap` files.
    * Fallback dependencies and bundled subprojects.
    * Version constraints and optional dependencies.
<!-- chapter: cross-compilation, duration: 2h -->
* Cross-Compilation:
    * Cross-compilation concepts and toolchain files.
    * Writing a `Meson` cross-`file`.
    * Host vs. build vs. target machine.
    * Handling platform-specific code and feature detection.
    * Practical example: `ARM` embedded target.
<!-- chapter: testing-with-meson, duration: 2h -->
* Testing with `Meson`:
    * Declaring and running tests with `test()`.
    * Test timeouts, dependencies, and environment variables.
    * Test suites and filtering.
    * Integration with `Valgrind` and sanitizers.
<!-- chapter: ide-and-cicd-integration, duration: 1h -->
* Integration with `IDEs` and `CI/CD`:
    * `VSCode`, `CLion`, and `Qt Creator` integration.
    * Running `Meson` builds in `GitHub Actions` and `GitLab CI`.
    * Caching build artifacts for faster pipelines.
<!-- chapter: meson-vs-cmake, duration: 2h -->
* `Meson` vs `CMake` Comparison:
    * Syntax and readability comparison.
    * Feature parity and ecosystem differences.
    * Migration strategies from `CMake` to `Meson`.
    * Community and long-term support considerations.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
