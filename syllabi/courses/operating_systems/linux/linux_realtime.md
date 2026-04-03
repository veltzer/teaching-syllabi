---
tags:
  - infrastructure:linux
  - infrastructure:real-time
  - practices:performance
  - concepts:scheduling
  - hardware-and-embedded:embedded
  - practices:latency
level: advanced
category: operating-systems
duration_hours: 32
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: linux_realtime -->
# `Linux` real time programming

## Description
`Linux` has become the dominant operating system in many real work, real time applications but it is also the most complicated operating system to be used in that space and so requires quite a high degree of understanding in order to be utilized properly. This is a course designed to achieve exactly that. The course could be taught at a theoretical level with no exercises covering more ground or less theoretically with exercises for new comers to the `Linux` Real Time playing field.

## Duration
32 hours / 4 days

## Intended Audience
* Experienced `C`/`C++` programmers (3 years minimum).

## Prerequisites
* `C` programming (`C++` if `C++` issues are to be discussed)
* `UNIX` `API` familiarity
* Knowledge of `UNIX` philosophy and design.
* If no such knowledge exists then the course could be made longer to accommodate with an intro about `UNIX`/`Linux` philosophy, command line usage, boot process and more.

## Objectives
* understand the core concepts and principles of `Linux`` real time programming
* gain practical knowledge of Definitions
* gain practical knowledge of `Linux`` and real time
* gain practical knowledge of Real time and being fast

## Outline
<!-- chapter: definitions, duration: 2h -->
* Definitions
    * What is realtime?
    * Near real time scenarios
    * Traditional real time operating systems
    * Deficiencies in traditional real time operating systems
    * The sources of latency
<!-- chapter: linux-and-real-time, duration: 1h -->
* `Linux` and real time
    * Is `Linux` real time?
    * The `Linux` real time patch
    * real time APIs in `Linux`
<!-- chapter: real-time-and-being-fast, duration: 1h -->
* Real time and being fast
    * The importance of knowing the systems APIs (memcpy, etc)
    * Intel libraries for `Linux`
    * Writing `assembly` in `Linux`
<!-- chapter: real-time-and-the-operating-system, duration: 4h -->
* Real time and the operating system
    * cost of a system calls
    * the cost of regular read and write system calls.
    * "do many" system calls (readv, writev, ...)
    * multiplexing IO in `Linux` (select, poll, `epoll`)
    * asynchronous IO in `Linux`
    * io_uring interface
    * `mmap` with drivers and files
    * avoiding system calls (caching, getpid, gettid and more)
    * virtual memory, page faults and their cost.
    * avoiding pagefaults
    * avoiding swap
    * shared memory and how it's implemented
    * cost of DSOs
<!-- chapter: real-time-and-locking, duration: 2h -->
* Real time and locking
    * How are locks implemented?
    * spinlocks
    * futexes
    * readers/writer lock
    * RCU
    * lock free data structures
<!-- chapter: real-time-and-devices, duration: 2h -->
* Real time and devices
    * read, write
    * aio
    * `ioctl`
    * `mmap`
    * get_user_pages
<!-- chapter: real-time-and-clocks, duration: 2h -->
* Real time and clocks
    * The various types of clocks supported by `Linux`.
    * Accuracy of the various clocks.
    * `sleep(3)`, `usleep(3)`, `nanosleep(2)`
    * `clock_*(2)`
    * `timerfd(2)`: multiplexing clocks and other events
<!-- chapter: real-time-and-files, duration: 2h -->
* Real time and files
    * cost of reading files
    * cost of writing files
    * cost of seeking files
    * cost of deleting files
    * cost of many files in a folder
    * using `tmpfs`/ramfs as an alternative
<!-- chapter: real-time-and-memory-allocation, duration: 2h -->
* Real time and memory allocation
    * performance of `malloc`
    * mlock
    * obstacks
    * `mmap`
    * other memory allocators
    * kernel memory allocation
<!-- chapter: real-time-and-scheduling, duration: 2h -->
* Real time and scheduling
    * Scheduling real time threads
    * user space threads vs kernel threads vs `IRQ` handlers
    * Real time threads can hurt your system
    * debugging your threads preemption
    * examining interrupts and thread priorities
<!-- chapter: real-time-and-signals, duration: 2h -->
* Real time and signals
    * What is signal handling?
    * The problems of traditional signal handling
    * RT signals in `Linux`
    * eventfd as alternative to RT signals
    * performance of pipes
<!-- chapter: real-time-and-measurements, duration: 3h -->
* Real time and measurements
    * gettimeofday
    * problems with gettimeofday
    * performance counters intro
    * `perf`
    * doing it on your own (RDTSC, PAPI)
    * measuring embedded `Linux` latency
    * measuring latency using external methods (oscilloscope, logic analyzer)
    * kernel profiling
<!-- chapter: real-time-and-logging, duration: 1h -->
* Real time and logging
    * cost of `syslog`
    * cost of writing to files
    * alternatives to both using shared memory
<!-- chapter: real-time-and-software-design, duration: 1h -->
* Real time and software design
    * Designing a real time `Linux` system - intro
    * `CPU` affinity for threads and processes.
    * `CPU` affinity for interrupt handlers and kernel threads.
<!-- chapter: real-time-and-the-hardware, duration: 1h -->
* Real time and the hardware
    * hardware built for real time
    * IO busses and real time
    * problems caused by the hardware (Self monitoring IRQs (SMIs) and similar issues)
<!-- chapter: hypervisors-intro, duration: 2h -->
* Hypervisors intro
    * Host-Guest OS terminology
    * Hypervisors
    * Virtualization technologies: Full Virtualization, Para-Virtualization, Os-Level Virtualization
    * Virtual machine privileges.
    * Advantages & disadvantages of using virtual machines
    * Additional option: basic demo on `KVM`
    * Quick review of common hypervisors (`KVM`, `VMWare`, `Hyper-V`) and their capabilities.
<!-- chapter: real-time-and-hypervisors, duration: 2h -->
* Real time and hypervisors
    * Comparing native (bare metal) and hosted hypervisors for real time needs.
    * Real time drivers and real time.
    * `PCI` pass through.
    * Hypervisors scheduling.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
