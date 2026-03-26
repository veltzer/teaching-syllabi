---
tags:
  - linux
  - debugging
  - gdb
  - c
  - c++
  - memory
level: intermediate
category: operating-systems
duration_days: 3
audience:
  - developers
---
# `Linux` Debugging

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
The debugging course aims to give programmers and team leaders a broader view
that debugging plays in systems engineering. In addition this course introduces
the participants to tools they did not know existed. This combination enables to
build software
which is easier to debug both at the development and client sites. This ultimately
saves precious time and produces systems which are more stable and more extendable
and delays the stasis that most `C`/`C++` systems reach at some point.

## Duration
24 hours / 3 days

## Prerequisites
* The course is ONLY for `C`/`C++` developers.
* The course is ONLY for `UNIX`/`Linux` developers.
* The course is ONLY for programmers who have been programming for at least one year.

## Outline
* The `C`/`C++` languages and their pitfalls.
    * How the MMU works.
    * What can a program do?
    * What can't a program do?
    * Memory pages are not the ultimate protection.
* Programming for better debugging.
    * Sanity checking objects.
    * Using the preprocessor for debug info.
    * Using logging libraries when programming.
    * Compiling with debug information.
    * Writing modular code - why is it important for debugging ?.
    * Build problems leading to bugs - how to fix your build system.
    * Unit testing.
    * Managing change sets to reduce debug time.
    * Passing -Wall.
    * Avoiding using the preprocessor for programming.
    * Writing naive versions of objects.
    * Making sure that bugs never come back: tests and assertions.
* Using `gdb` efficiently.
    * What is debug info ?
    * Preparing debug info.
    * Using debug versions of basic libraries.
    * The most useful commands and techniques.
    * Graphical front ends.
    * Remote debugging (serial port, remote machine over `TCP`/ip, USB).
* Memory overrun
    * Stack overrun, characterization of such faults, and techniques for guarding against
    * Heap overrun, characterization of such faults, and techniques for guarding against
    * Global storage overrun, characterization of such faults, and techniques for guarding against
* Multi-threading
    * And synchronization mechanisms
    * Thread stack
    * `TLS`
    * Shared resources and keeping data integrity
* Using external libraries/tools
    * `Efence`
    * `dmalloc`
    * `MPatrol`
* The earliest point principle
    * The importance of finding the bug at the earliest point.
    * Using assertions.
    * Playing with memory allocation methods.
    * Playing with data.
    * Playing with optimization.
    * Playing with the architecture.
    * Using a sparse allocator.
    * Checking your heap periodically.
    * `ulimit`
    * Changing read/write attributes of your memory pages.
    * Injecting errors to check robustness.
* Dynamic allocations and memory leaks
    * Allocating memory without de-allocation
    * De-allocating non allocated memory
    * De-allocating already de-allocated memory
* Post mortem
    * Using core files correctly.
    * At the client side.
    * Techniques to have the software send you post mortem automatically from the client site.
* Stack structure
    * What can go wrong?
    * Stacks and multi-threading
    * Stacks and interrupts
    * Stacks and infinite recursion.
* Tools: `nm`, `ldd`, `objdump`, `strace`, `ltrace`
    * runtime memory allocation information.
    * taking snapshots of your heap.
    * `ld` - the dynamic linker.
    * overriding symbols.
    * `LD_PRELOAD`
    * printing unmangled names.
* Misc issues:
    * Dynamically loading unloading code.
    * Name mangling in C++.
    * Some basic assembly can help.
    * Using the system logger.
    * Using the proc filesystem.
    * Listing open files.
    * Listing open ports.
