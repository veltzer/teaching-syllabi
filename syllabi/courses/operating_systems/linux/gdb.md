---
tags:
  - infrastructure:linux
  - tools:gdb
  - practices:debugging
  - languages:c
  - languages:c++
  - hardware-and-embedded:toolchain
level: intermediate
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: gdb -->
# `Gdb`

## Description
This course is intended for C/`C++` developers who wish to learn how to better
use the `Linux` `gdb` debugger and get better at debugging in general.

## Duration
16 hours / 2 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* basic familiarity with operating system concepts

## Objectives
* understand the core concepts and principles of `Gdb`
* gain practical knowledge of definitions
* gain practical knowledge of `gdb`` intro
* gain practical knowledge of the toolchain and its tools

## Outline
<!-- chapter: definitions, duration: 1h -->
* definitions
<!-- chapter: gdb-intro, duration: 1h -->
* `gdb` intro
<!-- chapter: the-toolchain-and-its-tools, duration: 5h -->
* the toolchain and its tools
    * `GCC`
    * ld
    * gas
    * readelf
    * nm
    * ldd
    * objcopy
    * objdump
    * LD_LIBRARY_PATH
    * dlopen
    * ar
    * ranlib
    * strip
    * gcore
    * customizing core file names
<!-- chapter: debug-information-problems, duration: 1h -->
* debug information problems
    * different debug information types
    * the problem of size
    * `C++` templates and their problems
    * ways of solving the issues
<!-- chapter: dynamic-libraries, duration: 1h -->
* dynamic libraries
    * how do they work? PLT, GOT
    * versions
    * the dynamic library cache (ldconfig)
<!-- chapter: static-libraries, duration: 1h -->
* static libraries
    * how do they work? `ar(1)`
    * speed and link time
<!-- chapter: c-name-mangling, duration: 1h -->
* `c++` name mangling
    * `c`++filt
    * mangling in your code
<!-- chapter: gdb, duration: 4h -->
* `gdb`
    * running and stepping
    * listing and ordering your files
    * breakpoints (software and hardware)
    * remote debugging + debugging agent
    * remote debugging in `eclipse`
    * scripting
    * viewing variables
    * changing variables
    * calling functions
    * viewing memory
    * viewing registers
    * multi-thread debugging
    * handling core files
<!-- chapter: gui-programs-for-gdb, duration: 1h -->
* GUI programs for `gdb`
    * gdbtui
    * xxgdb
    * `eclipse`+CDT

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
