---
tags:
  - infrastructure:linux
  - tools:gcc
  - tools:gdb
  - hardware-and-embedded:toolchain
  - tools:make
  - tools:git
level: beginner
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
---
# `Linux` programming environment

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Course is intended for `C`/`C++` programmers who want to find their way in the `Linux` programming environment.

## Duration
16 hours / 2 days

## Intended Audience
* software developers working on Linux-based systems
* system administrators and DevOps engineers

## Prerequisites
* experience with C programming
* familiarity with Linux command line

## Objectives
* understand the core concepts and principles of Linux` programming environment
* gain practical knowledge of The shell:
* gain practical knowledge of The compiler (`GCC`/g++):
* gain practical knowledge of libraries:

## Outline
* The shell:
    * Basic organization of the file system.
    * Login/logout.
    * Shell basics.
    * Writing basic scripts.
    * Security basics.
* The compiler (`GCC`/g++):
    * Installing.
    * Toolchain compilers.
    * Running the compiler: compiling/linking.
    * Important flags and their semantics.
* libraries:
    * Making shared libraries
    * `ld`, `ld.so`
    * `ldd`
    * `LD_PRELOAD`, `LD_LIBRARY_PATH`
    * `pmap`, /proc/[pid]/maps
* Miscellaneous tools:
    * `nm`, `objdump`, `strip`, `strings`
* core dumps:
    * allowing core dumps
    * using core dumps
    * taking core dump snapshots of running processes
* monitoring:
    * GUI tools (gnome, KDE)
    * console tools (ps, top, netstat, ...)
* debugging
    * basic `gdb` usage.
    * `gdb` important commands
    * remote `gdb` usage
    * embedded remote `gdb` usage.
    * using eclipse for debugging and remote debugging.
* makefiles introduction
    * writing a simple makefile
    * handling dependencies
* git introduction
    * creating a repo
    * your first commit
    * branching?
    * push and pulling

## We will not cover
* The `C`/`C++` languages themselves.
* The peculiarities of `GCC`/g++ as regards the `C`/`C++` standard.
* The `Linux` kernel or user space (glibc?) `APIs` and their correct usage.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
