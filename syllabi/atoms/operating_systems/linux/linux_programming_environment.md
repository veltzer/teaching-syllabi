---
tags:
  - linux
  - gcc
  - gdb
  - toolchain
  - make
  - git
level: beginner
category: operating-systems
duration_days: 2
audience:
  - developers
---
# `Linux` programming environment

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Course is intended for `C`/`C++` programmers who want to find their way in the `Linux` programming environment.

## Duration
16 hours / 2 days

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
