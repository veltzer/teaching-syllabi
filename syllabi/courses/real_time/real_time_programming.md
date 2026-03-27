---
tags:
  - real-time
  - c
  - linux
  - systems-programming
level: advanced
category: real-time
audience:
  - embedded-engineers
  - developers
---
# Real Time Programming

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Real time programming is a difficult subject since it requires understanding systems
from top to bottom. This course attempts to address precisely this difficulty and explain
all the topics involved with real time programming. This course is tailored to C programmers
and is accompanied with exercises in `Linux` as demonstration of the various issues involved.

## Duration
56 hours / 7 days

## Intended Audience
* Programmers who wish to work with low-level hard/soft/near real time systems

## Prerequisites
* C programming (C++ an advantage)

## Objectives
* understand the core concepts and principles of Real Time Programming
* gain practical knowledge of Definitions
* gain practical knowledge of Types of real time system
* gain practical knowledge of The connections between real time systems and operating systems

## Outline
* Definitions
    * The definition of a real time system
* Types of real time system
    * Near real time
    * Soft real time
    * Hard real time
* The connections between real time systems and operating systems
    * Traditional real time operating systems
    * `Linux` as a real time system
    * Deficiencies in traditional real time operating systems
* The sources of latency
    * Interrupt latency
    * OS scheduling latency
    * OS switching latency
    * Software latency
* Measuring time
    * Using hardware timing mechanisms
    * Context switches and measuring time
    * Wallclock time vs ticks
* Writing fast software
    * The importance of knowing the systems `APIs` (`memcpy`, etc)
    * Using CPU manufacturer libraries
    * Writing assembly
    * `DMA`
    * Memory mappings
    * Atomic variables
    * RCU/COW
    * Mutexes
    * Reader/Writer locks
    * Other ideas
* Real time and memory allocations
    * `malloc`() and realtime
    * buddy algorithms
    * allocation stacks
* Real time and scheduling
    * Designing the threads and priorities of a real time system
    * Threads and CPUs - affinity, migration and more
    * Interrupts as latency sources
    * Interrupts and CPUs
    * The priority inversion problem and it's various solutions
* Real time and logging
    * Cost of writing to files
    * Async logging
    * Shared memory logging
* Real time and the hardware
    * Problems relating to real time coming from hardware
    * IO busses and real time
    * Interrupts causing problems to real time systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
