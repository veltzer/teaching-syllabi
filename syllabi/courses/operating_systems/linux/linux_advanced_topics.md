---
tags:
  - infrastructure:linux
  - practices:performance
  - concepts:synchronization
  - infrastructure:epoll
  - infrastructure:cgroups
  - infrastructure:namespaces
  - hardware-and-embedded:zero-copy
level: advanced
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: linux_advanced_topics -->
# `Linux` Advanced Topics

## Description
This seminar deals with several `Linux` topics:
advanced APIs (zero copy, multiplexing, io_uring and more)
locking (or the avoidance of it)
high performance programming for calculation
advanced APIs for segregation
IO advanced APIs

## Duration
16 hours / 2 days

## Intended Audience
* Advanced `Linux` `C`/`C++` programmers who want to write high performance or low latency applications over `Linux`.
* Seasoned `Linux` `C`/`C++` programmers who want a deep dive into advanced areas of the `Linux` `API`.

## Prerequisites
* `C` programming
* `Linux` systems programming
* `Linux` real time programming

## Objectives
* understand the core concepts and principles of `Linux`` Advanced Topics
* gain practical knowledge of the IO layer and it's lies.
* gain practical knowledge of using the `CPU` to the max
* gain practical knowledge of advanced synchronization topics:

## Outline
<!-- chapter: the-io-layer-and-it-s-lies, duration: 1h -->
* the IO layer and it's lies.
    * flush, sync and batteries.
<!-- chapter: using-the-cpu-to-the-max, duration: 1h -->
* using the `CPU` to the max
    * MMX, `SSE`, SIMD
    * transactional memory on `Linux`
<!-- chapter: advanced-synchronization-topics, duration: 4h -->
* advanced synchronization topics:
    * futexes
    * robust futexes
    * pthread barriers
    * pthread spinlocks
    * pthread readers/writer locks
    * RCU in user space
    * volatile and it's pitfalls
<!-- chapter: advanced-apis-in-linux, duration: 3h -->
* advanced APIs in `Linux`
    * `cgroups`
    * namespaces
    * containers
    * memfd
<!-- chapter: multiplexing-in-linux-epoll, duration: 3h -->
* multiplexing in `Linux`: `epoll`
    * timer fds
    * signal fds
    * event fds
    * real time signals
    * communicating with the kernel (AF_NETLINK)
<!-- chapter: malloc-performance, duration: 2h -->
* `malloc` performance
    * how `malloc` allocates large vs small areas of memory
    * arenas in `malloc`
    * the process mm semaphore in the kernel.
<!-- chapter: zero-copy-apis, duration: 2h -->
* zero copy APIs
    * splice
    * tee
    * vmsplice

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
