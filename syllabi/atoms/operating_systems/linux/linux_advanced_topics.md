---
tags:
  - linux
  - performance
  - synchronization
  - epoll
  - cgroups
  - namespaces
  - zero-copy
level: advanced
category: operating-systems
duration_days: 2
audience:
  - developers
---
# `Linux` Advanced Topics

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This seminar deals with several `Linux` topics:
advanced `APIs` (zero copy, multiplexing, `io_uring` and more)
locking (or the avoidance of it)
high performance programming for calculation
advanced `APIs` for segregation
IO advanced `APIs`

## Duration
16 hours / 2 days

## Intended Audience
* Advanced `Linux` `C`/`C++` programmers who want to write high performance or low latency applications over `Linux`.
* Seasoned `Linux` `C`/`C++` programmers who want a deep dive into advanced areas of the `Linux` `API`.

## Prerequisites
* C programming
* `Linux` systems programming
* `Linux` real time programming

## Outline
* the IO layer and it's lies.
    * flush, sync and batteries.
* using the CPU to the max
    * MMX, SSE, SIMD
    * transactional memory on `Linux`
* advanced synchronization topics:
    * futexes
    * robust futexes
    * `pthread` barriers
    * `pthread` spinlocks
    * `pthread` readers/writer locks
    * RCU in user space
    * volatile and it's pitfalls
* advanced `APIs` in `Linux`
    * cgroups
    * namespaces
    * containers
    * `memfd`
* multiplexing in `Linux`: epoll
    * timer fds
    * signal fds
    * event fds
    * real time signals
    * communicating with the kernel (`AF_NETLINK`)
* `malloc` performance
    * how `malloc` allocates large vs small areas of memory
    * arenas in `malloc`
    * the process mm semaphore in the kernel.
* zero copy `APIs`
    * splice
    * tee
    * vmsplice

## Copyright
Mark Veltzer, © 2026
