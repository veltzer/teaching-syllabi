---
tags:
  - infrastructure:linux
  - hardware-and-embedded:embedded
  - infrastructure:real-time
  - infrastructure:user-space
  - concepts:scheduling
  - tools:buildroot
  - tools:yocto
level: intermediate
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: embedded_linux_topics_for_linux_user_space_developers -->
# Embedded `Linux` topics for `Linux` user space developers

## Description
This is a course that covers embedded `Linux` topics that user space developers need to know.
These include: `CPU` affinity, real time apis, avoiding page faults, avoiding swap, using `mmap`, using your
own `malloc` implementation, talking to device drivers, using `mmap` with device drivers, `Linux` hotplug or
the lack thereof and others.

## Duration
24 hours / 3 days

## Intended Audience
* embedded systems engineers and kernel developers
* system programmers working on low-level software

## Prerequisites
* experience with C or `C++` programming
* basic understanding of computer architecture

## Objectives
* understand the core concepts and principles of Embedded `Linux` topics for `Linux` user space developers
* gain practical knowledge of Programming topics for embedded
* gain practical knowledge of Embedded topics for `Linux` embedded developers
* apply Embedded `Linux` topics for `Linux` user space developers techniques and best practices in real-world scenarios

## Outline
<!-- chapter: programming-topics-for-embedded, duration: 15h -->
* Programming topics for embedded
    * `Linux` support for real time: the real time patch.
    * high precision and real time clock APIs.
    * `Linux` scheduling mechanisms for real time.
    * Scheduling and priorities under `Linux`.
    * `CPU` affinity under `Linux`
        * for processes
        * for threads
        * for kernel threads
    * Avoiding page faults and swap.
        * `mlock(2)`
        * swapon, swapoff
        * `mmap` with populate
        * `malloc` with populate
    * Fast `malloc` for `Linux`
    * Disabling `malloc` for real time stages of programs
    * Measuring system latency: cyclictest
    * Finding sources of latency (tools).
    * `Linux` `API` for manipulating devices via device drivers.
        * `mmap`
        * `ioctl`
<!-- chapter: embedded-topics-for-linux-embedded-developers, duration: 9h -->
* Embedded topics for `Linux` embedded developers
    * Boot sequence.
    * Plug and play under `Linux`.
    * Shutdown sequence.
    * How is the `Linux` kernel developed.
    * How are distributions derived from the `Linux` kernel.
    * Various approaches for making embedded `Linux` systems.
        * `Linux` from scratch.
        * Tools: ptxdist, `buildroot`, `Yocto`.
        * The distribution path.
    * `BSP` and `Linux`.
    * Bootloaders and `Linux`.
        * uboot, lilo, `grub`, syslinux, xloader.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
