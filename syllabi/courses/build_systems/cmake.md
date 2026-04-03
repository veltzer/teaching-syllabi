---
tags:
  - tools:cmake
  - languages:c
  - languages:c++
  - practices:build-systems
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: cmake -->
# `CMake`

## Description
`CMake` is one of the leading tools for building `C` based software.

## Duration
16 hours / 2 days

## Intended Audience
* software developers managing build processes
* `DevOps` engineers working with `CI/CD` pipelines

## Prerequisites
* software development experience

## Objectives
* understand the core concepts and principles of `CMake`
* gain practical knowledge of Introduction to ```CMake``
* gain practical knowledge of "Hello, World!"
* gain practical knowledge of In-Depth Syntax

## Outline
<!-- chapter: introduction-to-cmake, duration: 4h -->
* Introduction to `CMake`
    * `CMake` History
    * `CMake` Major features
    * `CMake` Pipeline configuration
    * `CMake` and Platform independence
    * `CMake` Developer
    * CPack
    * CTest
    * CDash
<!-- chapter: hello-world, duration: 3h -->
* "Hello, World!"
    * Create an executable
    * Add a library
    * Set global compiler flags
    * User-configured options
    * Build types (Release/Debug)
    * Inheriting properties from dependencies
<!-- chapter: in-depth-syntax, duration: 3h -->
* In-Depth Syntax
    * Variables
    * if & foreach
    * Generator Expressions
    * Macros
    * Functions
<!-- chapter: importing-dependencies, duration: 2h -->
* Importing Dependencies
    * General usage
    * Making use of exported targets
    * Making use of find_* functions
<!-- chapter: installing-software, duration: 1h -->
* Installing Software
    * `install()` Function
    * Exported targets
<!-- chapter: packaging-software, duration: 1h -->
* Packaging Software
    * Archive
    * NSIS - `Windows` .exe format
<!-- chapter: miscellaneous-optional, duration: 2h -->
* Miscellaneous (optional)
    * Generating files during `CMake` execution
    * Custom targets
    * Executing processes during `CMake` execution

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
