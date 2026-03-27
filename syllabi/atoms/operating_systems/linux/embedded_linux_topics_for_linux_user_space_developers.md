---
tags:
  - linux
  - embedded
  - real-time
  - user-space
  - scheduling
  - buildroot
  - yocto
level: intermediate
category: operating-systems
duration_days: 3
audience:
  - developers
  - embedded-developers
---
# Embedded `Linux` topics for `Linux` user space developers

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This is a course that covers embedded `Linux` topics that user space developers need to know.
These include: CPU affinity, real time apis, avoiding page faults, avoiding swap, using `mmap`, using your
own `malloc` implementation, talking to device drivers, using `mmap` with device drivers, `Linux` hotplug or
the lack thereof and others.

## Duration
24 hours / 3 days

## Outline
* Programming topics for embedded
    * `Linux` support for real time: the real time patch.
    * high precision and real time clock `APIs`.
    * `Linux` scheduling mechanisms for real time.
    * Scheduling and priorities under `Linux`.
    * CPU affinity under `Linux`
        * for processes
        * for threads
        * for kernel threads
    * Avoiding page faults and swap.
        * `mlock(2)`
        * `swapon`, `swapoff`
        * `mmap` with populate
        * `malloc` with populate
    * Fast `malloc` for `Linux`
    * Disabling `malloc` for real time stages of programs
    * Measuring system latency: cyclictest
    * Finding sources of latency (tools).
    * `Linux` `API` for manipulating devices via device drivers.
        * `mmap`
        * ioctl
* Embedded topics for `Linux` embedded developers
    * Boot sequence.
    * Plug and play under `Linux`.
    * Shutdown sequence.
    * How is the `Linux` kernel developed.
    * How are distributions derived from the `Linux` kernel.
    * Various approaches for making embedded `Linux` systems.
        * `Linux` from scratch.
        * Tools: ptxdist, buildroot, `Yocto`.
        * The distribution path.
    * BSP and `Linux`.
    * Bootloaders and `Linux`.
        * uboot, lilo, grub, syslinux, xloader.

## Copyright
Mark Veltzer, © 2026
