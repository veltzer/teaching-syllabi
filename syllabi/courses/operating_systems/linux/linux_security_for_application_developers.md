---
tags:
  - infrastructure:linux
  - security:security
  - languages:c
  - security:vulnerabilities
  - infrastructure:containers
  - security:aslr
level: intermediate
category: operating-systems
duration_hours: 8
audience:
  - audiences:developers
---
# `Linux` security for application developers

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is intended to introduce the participants to `Linux` security issues, explain the various security threats that `C`/`C++` programs are subject to on the `Linux` platform and introduce the host of ways to combat these issues.

## Duration
8 hours / 1 day

## Intended Audience
* Experienced C application developers.
* `Linux` programming experience is recommended by not a must.

## Prerequisites
* C programming
* `UNIX` `API` familiarity is a plus
* If no such knowledge exists then the course could be made longer to accommodate with an intro about `UNIX`/`Linux` philosophy, command line usage, boot process and more.

## Objectives
* understand the core concepts and principles of Linux` security for application developers
* gain practical knowledge of Basic `Linux` security
* gain practical knowledge of C level security
* gain practical knowledge of How to combat C level vulnerabilities

## Exercises
This course is an instructor led course, with demos by the instructor and no exercises.

## Outline
* Basic `Linux` security
    * /etc/passwd and user login
    * effective user id, it's propagation via the process tree
    * how security is handled in the kernel
    * security of /dev files
    * SUID executables and how they work
    * the capabilities system and how to tune it
    * process pid=1 running as root with full capabilities
    * how to define a user on a full fledged system
    * how to define a user on an embedded system.
    * the boot on a full fledged system
    * the boot on an embedded system
* C level security
    * C level vulnerabilities
        * Buffer overflows
        * Format string vulnerabilities
        * Integer overflows
        * Unchecked array indexing
        * Null pointer dereferencing
        * Resource injection
        * Race conditions
        * Memory and resource leaks
        * Double free bugs
        * Use after free bugs
    * How to avoid C level vulnerabilities
* How to combat C level vulnerabilities
    * Using bounds checkers
    * Input validation
    * Overflow safe math libraries
    * Limiting allocations
    * Using memory safe functions
    * Memory tagging
    * Stack protection by the compiler
    * Handling errors gracefully
    * Limit privileges
    * Using static linking instead of dynamic linking
    * Use memory/thread safe libraries
    * Using static analysis
    * Using fuzz testing
    * Using Stack guards
    * Using Canaries
    * Using Checksums
    * Using multi-processing instead of multi-threading
    * Using processes with different users running them
    * Using `chroot` jails
    * Using namespaces
    * Using full fledged containers
        * `Docker`
        * `podman`
    * Using self made containers using `Linux` namespaces.
    * using ASLR
        * What is it? Why is it good?
        * How to enable it for libraries/binaries
        * How to disable it for various purposes (debugging, ...)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
