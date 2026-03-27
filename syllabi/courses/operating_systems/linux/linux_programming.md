---
tags:
  - linux
  - c
  - c++
  - systems-programming
  - multithreading
  - ipc
  - debugging
level: intermediate
category: operating-systems
duration_days: 5
audience:
  - developers
---
# `Linux` programming

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Linux` is the widest protected operating system in use today and this course teaching you how to write system programs
over it in C or C++ which make efficient use of it.

## Duration
40 hours / 5 days

## Outline
* Protected OS fundamentals
    * Definition of protected operating system.
    * How does a protected operating system work.
    * The implications:
        * Commercial.
        * Debugging.
        * Stability.
        * Security.
        * Multi-user.
* Basics of writing code
    * C and C++ filename conventions.
    * Writing a program.
    * Writing a library.
    * Basics of makefiles.
* `Linux` multi-processing
    * Process number 1.
    * Forking and creating new processes.
    * Adoption and zombies.
    * Signals basics.
    * Killing processes.
    * Process groups.
* `Linux` IPC
    * `POSIX` shared memory.
    * `POSIX` message queue.
    * `POSIX` semaphore.
    * BSD and `UNIX` sockets.
    * Using inter-thread mechanisms in shared memory for efficiency.
* `Linux` multi-threading
    * `Linux` has no threads: the `Linux` implementation of threads.
    * Launching threads:
        * Simple.
        * With attributes.
    * Ids of threads: `pthread` id vs tid vs pid.
    * Mechanisms for multi-thread communication:
        * mutex.
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
* Other tools for debugging
    * /proc, /sys and friends.
    * ps, top and friends.
    * strace, `ltrace` and friends.
    * valgrind, `cachegrind` and friends.
    * Logging approaches and the system logger.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
