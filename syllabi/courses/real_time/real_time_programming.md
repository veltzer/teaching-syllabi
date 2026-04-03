---
tags:
  - infrastructure:real-time
  - languages:c
  - infrastructure:linux
  - concepts:systems-programming
level: advanced
category: real-time
duration_hours: 56
audience:
  - audiences:embedded-engineers
  - audiences:developers
---
<!-- course: real_time_programming -->
# Real Time Programming

## Description
Real time programming is a difficult subject since it requires understanding systems
from `top` to bottom. This course attempts to address precisely this difficulty and explain
all the topics involved with real time programming. This course is tailored to `C` programmers
and is accompanied with exercises in `Linux` as demonstration of the various issues involved.

## Duration
56 hours / 7 days

## Intended Audience
* Programmers who wish to work with low-level hard/soft/near real time systems

## Prerequisites
* `C` programming (`C++` an advantage)

## Objectives
* understand the core concepts and principles of Real Time Programming
* gain practical knowledge of Definitions
* gain practical knowledge of Types of real time system
* gain practical knowledge of The connections between real time systems and operating systems

## Outline
<!-- chapter: definitions, duration: 2h -->
* Definitions
    * The definition of a real time system
<!-- chapter: types-of-real-time-system, duration: 4h -->
* Types of real time system
    * Near real time
    * Soft real time
    * Hard real time
<!-- chapter: the-connections-between-real-time-systems-and-operating-systems, duration: 4h -->
* The connections between real time systems and operating systems
    * Traditional real time operating systems
    * `Linux` as a real time system
    * Deficiencies in traditional real time operating systems
<!-- chapter: the-sources-of-latency, duration: 6h -->
* The sources of latency
    * Interrupt latency
    * OS scheduling latency
    * OS switching latency
    * Software latency
<!-- chapter: measuring-time, duration: 5h -->
* Measuring time
    * Using hardware timing mechanisms
    * Context switches and measuring time
    * Wallclock time vs ticks
<!-- chapter: writing-fast-software, duration: 13h -->
* Writing fast software
    * The importance of knowing the systems APIs (memcpy, etc)
    * Using `CPU` manufacturer libraries
    * Writing `assembly`
    * `DMA`
    * Memory mappings
    * Atomic variables
    * RCU/`COW`
    * Mutexes
    * Reader/Writer locks
    * Other ideas
<!-- chapter: real-time-and-memory-allocations, duration: 5h -->
* Real time and memory allocations
    * `malloc`() and realtime
    * buddy algorithms
    * allocation stacks
<!-- chapter: real-time-and-scheduling, duration: 7h -->
* Real time and scheduling
    * Designing the threads and priorities of a real time system
    * Threads and CPUs - affinity, migration and more
    * Interrupts as latency sources
    * Interrupts and CPUs
    * The priority inversion problem and it's various solutions
<!-- chapter: real-time-and-logging, duration: 5h -->
* Real time and logging
    * Cost of writing to files
    * `Async` logging
    * Shared memory logging
<!-- chapter: real-time-and-the-hardware, duration: 5h -->
* Real time and the hardware
    * Problems relating to real time coming from hardware
    * IO busses and real time
    * Interrupts causing problems to real time systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
