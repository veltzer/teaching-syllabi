---
tags:
  - infrastructure:linux
  - tools:gcc
  - tools:gdb
  - hardware-and-embedded:toolchain
  - tools:make
level: beginner
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: linux_programming_environment -->
# `Linux` programming environment

## Description
Course is intended for C/`C++` programmers who want to find their way in the `Linux` programming environment.

## Duration
16 hours / 2 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* experience with C programming
* familiarity with `Linux` command line

## Required Knowledge
* Introduction to `Git` (or equivalent `Git` experience)

## Objectives
* understand the core concepts and principles of `Linux`` programming environment
* gain practical knowledge of The shell:
* gain practical knowledge of The compiler (`GCC`/g++):
* gain practical knowledge of libraries:

## Outline
<!-- chapter: the-shell, duration: 2h -->
* The shell:
    * Basic organization of the file system.
    * Login/logout.
    * Shell basics.
    * Writing basic scripts.
    * Security basics.
<!-- chapter: the-compiler-gcc-g, duration: 2h -->
* The compiler (`GCC`/g++):
    * Installing.
    * Toolchain compilers.
    * Running the compiler: compiling/linking.
    * Important flags and their semantics.
<!-- chapter: libraries, duration: 2h -->
* libraries:
    * Making shared libraries
    * ld, ld.so
    * ldd
    * LD_PRELOAD, LD_LIBRARY_PATH
    * pmap, /proc/[pid]/maps
<!-- chapter: miscellaneous-tools, duration: 1h -->
* Miscellaneous tools:
    * nm, objdump, strip, strings
<!-- chapter: core-dumps, duration: 2h -->
* core dumps:
    * allowing core dumps
    * using core dumps
    * taking core dump snapshots of running processes
<!-- chapter: monitoring, duration: 2h -->
* monitoring:
    * GUI tools (gnome, KDE)
    * console tools (ps, top, `netstat`, ...)
<!-- chapter: debugging, duration: 3h -->
* debugging
    * basic `gdb` usage.
    * `gdb` important commands
    * remote `gdb` usage
    * embedded remote `gdb` usage.
    * using `eclipse` for debugging and remote debugging.
<!-- chapter: makefiles-introduction, duration: 2h -->
* makefiles introduction
    * writing a simple `makefile`
    * handling dependencies

## We will not cover
* The C/`C++` languages themselves.
* The peculiarities of `GCC`/g++ as regards the C/`C++` standard.
* The `Linux` kernel or user space (glibc?) APIs and their correct usage.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
