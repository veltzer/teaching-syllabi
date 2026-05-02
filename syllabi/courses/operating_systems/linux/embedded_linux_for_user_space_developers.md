---
tags:
  - infrastructure:linux
  - hardware-and-embedded:embedded
  - infrastructure:real-time
  - infrastructure:user-space
  - infrastructure:ipc
  - networking:networking
level: intermediate
category: operating-systems
duration_hours: 56
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: embedded_linux_for_user_space_developers -->
# Embedded `Linux` for user space developers

## Description
This course introduces the participants to embedded development and embedded development in `Linux` in particular.
The course teaches the theoretical aspects of embedded and real time systems as well as the practical implications of those aspects and their implementation in `Linux`.

This is not a kernel development course and the participants will not learn how to write a device driver in `Linux`.
On the other hand this is a holistic course teaching how things are done in the kernel which is a must for embedded and/or
real time development.

This is a practical course with exercises covering most topics.

## Duration
56 hours / 7 days

## Intended Audience
* embedded systems engineers and kernel developers
* system programmers working on low-level software

## Prerequisites
* experience with C or `C++` programming
* basic understanding of computer architecture

## Objectives
* understand the core concepts and principles of Embedded `Linux` for user space developers
* gain practical knowledge of How protected operating systems work?
* gain practical knowledge of Real time operating systems
* gain practical knowledge of `Linux`` as a real time operating system

## Outline
<!-- chapter: how-protected-operating-systems-work, duration: 2h -->
* How protected operating systems work?
    * How preemption works
    * How memory management works
    * Why is protection important?
<!-- chapter: real-time-operating-systems, duration: 4h -->
* Real time operating systems
    * The definition of a real time system
    * The definition of a real time operating system
    * The sources of latency
    * No pre-emption.
    * How to limit runtime to fight bugs?
    * Reducing latency of a real time system.
<!-- chapter: linux-as-a-real-time-operating-system, duration: 10h -->
* `Linux` as a real time operating system
    * The `Linux` kernel as real time kernel.
    * The real time patch
    * `Linux` real time scheduling: how it works.
    * `Linux` and `CPU` affinity of threads and processes: how to use it.
    * The sources of latency in `Linux`
    * The story of an interrupt, from hardware to application.
    * Mutexes and real time
        * The problem (priority inversion).
        * The solution (priority inheritance).
    * Memory allocation and real time
        * The problems with `malloc`
        * Allocating at start and disabling allocations
        * Alternatives to `malloc`
    * How does `Linux` compare to traditional real time operating systems (task vs thread vs process)
    * How to measure the latency of your `Linux` embedded system?
<!-- chapter: linux-programming-topics-for-embedded-developers, duration: 21h -->
* `Linux` programming topics for embedded developers
    * System design issues
        * Multi process systems
        * Multi threaded systems
        * Comparison between the two
    * Interprocess communication
        * Signals / Real time signals
        * Pipes
        * Shared memory
        * Mutexes
        * Semaphores
        * Message queues
        * Barriers
    * Accessing hardware in `Linux`
        * Device files
        * using `read(2)` and `write(2)` for regular IO.
        * using `ioctl(2)` to control devices
        * using `mmap(2)` to access memory mapped regions.
    * Debugging and remote debugging in `Linux`
        * Compiling with debug information
        * Debugging locally
        * Debugging remotely via
            * Series
            * Serial over `USB`
            * `USB`
            * Network
<!-- chapter: linux-networking, duration: 3h -->
* `Linux` networking
    * The user space network `API`
    * The layers of the `Linux` network stack
    * The role of the `Linux` `ethernet` device driver
    * The full story of a packet (up and down the stack)
<!-- chapter: linux-serial-communication, duration: 3h -->
* `Linux` serial communication
    * The user space serial `API`
    * The layers of the `Linux` serial stack
    * The role of the serial device driver
    * The full story of a message (up and down the stack)
<!-- chapter: how-are-linux-embedded-systems-built, duration: 5h -->
* How are `Linux` embedded systems built
    * Creating a toolchain (crosstool-ng)
    * Choosing, configuring and cross compiling a kernel.
    * Choosing, configuring and cross compiling user space tools.
    * Packaging it all.
    * Adding a bootloader.
    * Testing with an emulator
    * Another approach: slimming down a distribution.
<!-- chapter: linux-boot-from-hardware-to-software, duration: 5h -->
* `Linux` boot, from hardware to software
    * The `BIOS`
    * The various bootloaders and their role
    * Loading the kernel
    * `initramfs`, `initrd` and more
    * Initializing hardware
    * Process number 1 - init
    * Spawning more processes in userspace.
<!-- chapter: hardware-testing, duration: 3h -->
* Hardware testing
    * What is BIT and how to use it correctly?
    * What is CBIT and how to use it correctly?
    * Power-on self tests
    * Division between software and hardware in BIT
    * BIT mandates in certain industries or hardware devices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
