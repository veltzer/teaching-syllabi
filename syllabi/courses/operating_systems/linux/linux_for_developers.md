---
tags:
  - infrastructure:linux
  - concepts:systems-programming
  - practices:command-line
level: intermediate
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: linux_for_developers -->
# `Linux` for Developers

## Description
This course equips software developers with the `Linux` knowledge they need to build, debug, and deploy applications effectively on `Linux` systems. Topics include file `I/O`, processes, signals, `IPC`, sockets, memory management, debugging tools, build systems, package management, and containerization basics. Students will gain practical skills for working productively in `Linux` development environments.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers transitioning to or working on `Linux` platforms
* Backend engineers building server-side applications on `Linux`
* Embedded engineers developing user-space applications

## Prerequisites
* Programming experience in C or `C++` (or willingness to read C code).
* Basic familiarity with the `Linux` command line.
* Understanding of fundamental operating system concepts.

## Objectives
* Perform file `I/O` operations using system calls and standard library functions.
* Create and manage processes, and understand process lifecycle.
* Handle signals for process communication and control.
* Implement inter-process communication using pipes, FIFOs, shared memory, and message queues.
* Develop networked applications using sockets.
* Understand `Linux` memory management and virtual memory concepts.
* Use debugging tools such as `gdb`, `strace`, `ltrace`, and `valgrind`.
* Work with build systems including `make` and `CMake`.
* Manage software packages and dependencies.
* Understand containerization basics with `Docker`.

## Outline
<!-- chapter: file-i-o, duration: 2h -->
* `File` `I/O`:
    * System calls: open, read, write, close, lseek.
    * `File` descriptors and file tables.
    * Buffered vs. unbuffered `I/O`.
    * `File` locking and advisory locks.
    * Filesystem hierarchy and file metadata.
<!-- chapter: processes, duration: 2h -->
* Processes:
    * Process creation with fork and exec.
    * Process states and lifecycle.
    * Zombie and orphan processes.
    * Process groups and sessions.
    * The /proc filesystem.
<!-- chapter: signals, duration: 2h -->
* Signals:
    * Signal types and default actions.
    * Signal handlers and sigaction.
    * Signal masks and blocking.
    * Real-time signals.
    * Signal safety and best practices.
<!-- chapter: inter-process-communication, duration: 2h -->
* Inter-Process Communication:
    * Pipes and named pipes (FIFOs).
    * System V and `POSIX` shared memory.
    * Message queues.
    * Semaphores for synchronization.
    * Choosing the right `IPC` mechanism.
<!-- chapter: sockets, duration: 2h -->
* Sockets:
    * Socket `API` and address families.
    * `TCP` and `UDP` communication.
    * Client-server architecture.
    * Non-blocking `I/O` and multiplexing with select, poll, and `epoll`.
    * `Unix` domain sockets.
<!-- chapter: memory-management, duration: 3h -->
* Memory Management:
    * Virtual memory and address spaces.
    * Stack, heap, and memory-mapped regions.
    * Dynamic memory allocation and fragmentation.
    * Memory-mapped files with `mmap`.
    * Understanding and preventing memory leaks.
<!-- chapter: debugging-tools, duration: 3h -->
* Debugging Tools:
    * Debugging with `gdb`: breakpoints, watchpoints, and backtraces.
    * Tracing system calls with `strace`.
    * Tracing library calls with `ltrace`.
    * Memory analysis with `valgrind`.
    * Core dumps and post-mortem debugging.
<!-- chapter: build-systems, duration: 3h -->
* Build Systems:
    * `make` and `Makefile` fundamentals.
    * `CMake` for cross-platform builds.
    * Compiler flags and optimization levels.
    * Static and shared libraries.
    * Build automation and dependency management.
<!-- chapter: package-management, duration: 2h -->
* Package Management:
    * Package managers: `apt`, `yum`, dnf.
    * Managing dependencies and repositories.
    * Building packages from source.
    * Creating distributable packages.
<!-- chapter: containerization-basics, duration: 3h -->
* Containerization Basics:
    * Introduction to containers and `Docker`.
    * Building and running containers.
    * Container images and layers.
    * Volumes and networking basics.
    * Development workflows with containers.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
