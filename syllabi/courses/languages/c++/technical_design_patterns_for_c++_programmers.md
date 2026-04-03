---
tags:
  - languages:c++
  - languages:c
  - concepts:design-patterns
  - concepts:concurrency
  - practices:performance
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: technical_design_patterns_for_c++_programmers -->
# Technical `design patterns` for `C`/`C++` programmers

## Description
This course deals with `design patterns` which solve technical issues.
The patterns presented in this course are not *data* patterns. They deal
not with the evolution of interfaces but instead they all deal, in one way
or another, with concurrency, speed and reliability and are all technical
patterns in nature as opposed to data driven patterns. So this is not
a regular *`Design patterns`* course but a collection of technical patterns
used throughout the industry.

## Duration
24 hours / 3 days

## Intended Audience
* `C++` developers
* software engineers working on performance-critical applications

## Prerequisites
Three years experience in `C++`

## Objectives
Understand the different technical `design patterns` in the realm of `C`/`C++` programming
and which are used in different types of systems (hard real time, soft
real time, fast time, embedded and server).

## Exercises
This course is for expert `C++` programmers. Some exercises will be presented but
a lot of the material will not be exercised due to time constraints and the
nature of the `C`/`C++` languages where exercises take a long time to complete.
Code examples will be shown and given to the students for many of the patterns.

## Outline
<!-- chapter: definitions, duration: 4h -->
* Definitions
    * what is `real time` programming
    * what is embedded programming
    * what is `fast time` programming
    * why are special patterns required?
    * are these patterns applicable only for `real time` or `fast time` ?
    * `C` vs `C++` in the application of these patterns
    * the compilers role
<!-- chapter: memory-patterns, duration: 5h -->
* Memory patterns
    * why are they needed?
    * using smart pointers
    * avoiding memory allocation
    * using your own memory allocator
    * using a multi core memory allocators
    * using a memory cache
    * using a per thread cache
    * obstack pattern for memory allocation
<!-- chapter: resource-and-concurrency-patterns, duration: 9h -->
* Resource and concurrency patterns
    * why are they needed?
    * cyclic executor
    * static priority
    * guarded call
    * critical region
    * queuing patterns
    * rendezvous patterns
    * simultaneous locking
    * ordered locking
    * fine grained locking patterns
    * no locking patterns
        * copy on write
        * RCU
        * full multi versioning
    * no locking algorithms
    * double checked locking
<!-- chapter: safety-and-reliability-patterns, duration: 3h -->
* Safety and Reliability patterns
    * why are they needed?
    * smart data
    * channel pattern
    * protected channel
    * dual channels
<!-- chapter: distribution-patterns, duration: 3h -->
* Distribution patterns
    * why are they needed?
    * reactor pattern
    * `async` completion (future) pattern
    * proactor pattern
    * object monitor

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
