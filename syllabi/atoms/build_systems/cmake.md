---
tags:
  - cmake
  - c
  - c++
  - build-systems
level: intermediate
category: build-system
duration_days: 2
audience:
  - developers
---
# `CMake`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`CMake` is one of the leading tools for building `C` based software.

## Duration
16 hours / 2 days

## Outline
* Introduction to `CMake`
    * `CMake` History
    * `CMake` Major features
    * `CMake` Pipeline configuration
    * `CMake` and Platform independence
    * `CMake` Developer
    * `CPack`
    * `CTest`
    * `CDash`
* "Hello, World!"
    * Create an executable
    * Add a library
    * Set global compiler flags
    * User-configured options
    * Build types (Release/Debug)
    * Inheriting properties from dependencies
* In-Depth Syntax
    * Variables
    * `if` & `foreach`
    * Generator Expressions
    * `Macros`
    * `Functions`
* Importing Dependencies
    * General usage
    * Making use of exported targets
    * Making use of `find_*` functions
* Installing Software
    * `install()` Function
    * Exported targets
* Packaging Software
    * Archive
    * `NSIS` - `Windows` `.exe` format
* Miscellaneous (optional)
    * Generating files during `CMake` execution
    * Custom targets
    * Executing processes during `CMake` execution
