---
tags:
  - infrastructure:linux
  - languages:c
  - languages:c++
  - concepts:systems-programming
  - concepts:multithreading
  - infrastructure:ipc
  - practices:debugging
level: intermediate
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: linux_programming -->
# `Linux` programming

## Description
`Linux` is the widest protected operating system in use today and this course teaching you how to write system programs
over it in C or `C++` which `make` efficient use of it.

## Duration
40 hours / 5 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* experience with C programming
* familiarity with `Linux` command line

## Objectives
* understand the core concepts and principles of `Linux`` programming
* gain practical knowledge of Protected OS fundamentals
* gain practical knowledge of Basics of writing code
* gain practical knowledge of `Linux`` multi-processing

## Outline
<!-- chapter: protected-os-fundamentals, duration: 6h -->
* Protected OS fundamentals
    * Definition of protected operating system.
    * How does a protected operating system work.
    * The implications:
        * Commercial.
        * Debugging.
        * Stability.
        * Security.
        * Multi-user.
<!-- chapter: basics-of-writing-code, duration: 3h -->
* Basics of writing code
    * C and `C++` filename conventions.
    * Writing a program.
    * Writing a library.
    * Basics of makefiles.
<!-- chapter: linux-multi-processing, duration: 4h -->
* `Linux` multi-processing
    * Process number 1.
    * Forking and creating new processes.
    * Adoption and zombies.
    * Signals basics.
    * Killing processes.
    * Process groups.
<!-- chapter: linux-ipc, duration: 3h -->
* `Linux` `IPC`
    * `POSIX` shared memory.
    * `POSIX` message queue.
    * `POSIX` semaphore.
    * BSD and `UNIX` sockets.
    * Using inter-thread mechanisms in shared memory for efficiency.
<!-- chapter: linux-multi-threading, duration: 15h -->
* `Linux` multi-`threading`
    * `Linux` has no threads: the `Linux` implementation of threads.
    * Launching threads:
        * Simple.
        * With attributes.
    * `Ids` of threads: pthread `id` vs tid vs pid.
    * Mechanisms for multi-thread communication:
        * `mutex`.
        * spinlocks.
        * barriers.
        * conditions.
        * readers/writer locks.
        * atomic variables.
        * lock free algorithms.
        * RCU libraries and more.
    * How to stop a thread?
        * killing threads is bad.
        * canceling a thread.
        * preventing cancellation.
        * breaking out of system calls.
<!-- chapter: debugging-using-gdb-and-friends, duration: 6h -->
* Debugging using `gdb` and friends
    * Compiling code to be debuggable.
    * Configuring source code locations.
    * Efficiency of debugging.
    * Calling functions while debugging.
    * Changing variables on the fly.
    * Reverse debugging.
    * Pretty printing of structures.
    * Hardware breakpoints as opposed to software ones.
    * Hardware watchpoints as opposed to software ones.
<!-- chapter: other-tools-for-debugging, duration: 3h -->
* Other tools for debugging
    * /proc, /sys and friends.
    * ps, top and friends.
    * `strace`, `ltrace` and friends.
    * `valgrind`, cachegrind and friends.
    * Logging approaches and the system logger.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
