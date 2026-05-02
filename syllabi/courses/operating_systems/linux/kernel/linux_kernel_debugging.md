---
tags:
  - infrastructure:linux
  - infrastructure:kernel
  - practices:debugging
  - linuxkernel:ftrace
  - practices:perf
  - linuxkernel:kprobes
  - practices:crash
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: linux_kernel_debugging -->
# `Linux` Kernel Debugging

## Description
This course is a `Linux` Kernel Debugging course and explores the various tools
and techniques that enable efficient debugging of code in the `Linux` kernel.

## Duration
* 3 days for experienced programmer.
* 5 days for non experienced programmers.

## Intended Audience
This course is intended for kernel developers which either do not have many
years experience in `Linux` kernel development or for developers who want to
expand their knowledge about the tools and techniques for debugging code
in the `Linux` kernel.

## Prerequisites
* C language
* `Linux` command line
* `Linux` kernel programming

## Objectives
* understand the core concepts and principles of `Linux`` Kernel Debugging
* gain practical knowledge of Basics
* gain practical knowledge of Kernel Features (reminder)
* gain practical knowledge of Techniques for finding the problem

## Outline
<!-- chapter: basics, duration: 1h -->
* Basics
    * Procedures
    * Kernel Versions
    * Kernel Sources and Use of `git`
<!-- chapter: kernel-features-reminder, duration: 2h -->
* Kernel Features (reminder)
    * Components of the Kernel
    * User-Space vs. Kernel-Space
    * What are System Calls?
    * Available System Calls
    * Scheduling Algorithms and Task Structures
    * Process Context
<!-- chapter: techniques-for-finding-the-problem, duration: 1h -->
* Techniques for finding the problem
    * Binary search for your bug
    * Building in debugging capabilities into your module
    * Building in configurability into your module
<!-- chapter: correct-locking-in-the-kernel, duration: 2h -->
* Correct locking in the kernel
    * Review of locking rules in the kernel
    * Using lockdep
    * Keeping the types of your locks flexible
    * Avoiding locks altogether
<!-- chapter: kernel-debugging-overview, duration: 2h -->
* Kernel debugging overview
    * Using the kernel log.
    * The debugfs filesystem.
    * `ioctl`
    * The proc filesystem.
    * The `sysfs` filesystem.
<!-- chapter: malloc-debugging-in-the-kernel, duration: 1h -->
* `Malloc` debugging in the kernel
    * Debugging caches via your code and /proc/slabinfo
    * KASAN
    * Kmemleak
<!-- chapter: monitoring-and-debugging, duration: 2h -->
* Monitoring and Debugging
    * Debuginfo Packages
    * Tracing and Profiling
    * Using sysctl
    * SysRq Key
    * oops Messages
    * Kernel Debuggers
    * debugfs
<!-- chapter: the-proc-filesystem, duration: 2h -->
* The proc Filesystem
    * What is the proc Filesystem?
    * Creating and Removing Entries
    * Reading and Writing Entries
    * The seq_file Interface
<!-- chapter: kprobes, duration: 1h -->
* kprobes
    * kprobes
    * kretprobes
    * SystemTap
<!-- chapter: ftrace, duration: 3h -->
* `Ftrace`
    * What is `ftrace`?
    * `ftrace`, trace-cmd and kernelshark
    * Available Tracers
    * Using `ftrace`
    * Files in the Tracing Directory
    * Tracing Options
    * Printing with `trace_printk()`
    * Trace Markers
    * Dumping the Buffer
    * trace-cmd
<!-- chapter: perf, duration: 2h -->
* `Perf`
    * What is `perf`?
    * `perf` stat
    * `perf` list
    * `perf` record
    * `perf` report
    * `perf` annotate
    * `perf` top
<!-- chapter: crash, duration: 1h -->
* Crash
    * Crash
    * Main Commands
<!-- chapter: kernel-core-dumps, duration: 1h -->
* Kernel Core Dumps
    * Generating Kernel Core Dumps
    * kexec
    * Setting Up Kernel Core Dumps
<!-- chapter: linux-kernel-debuggers, duration: 2h -->
* `Linux` Kernel debuggers
    * `Linux` Kernel (built-in) tools and helpers
    * kdb
    * `qemu`+`gdb`
    * kgdb: hardware+serial+`gdb`
<!-- chapter: netlink-sockets, duration: 1h -->
* `Netlink` Sockets
    * What are `netlink` Sockets?
    * Opening a `netlink` Socket
    * `netlink` Messages

## Notes
Several of the chapters in this course are based on chapters from
[`linux`-kernel-debugging-and_security](`https`://training.linuxfoundation.org/training/`linux`-kernel-debugging-and-security).
Other chapters are written by [me](mailto:mark.veltzer@gmail.com).
This course does not teach `Linux` Kernel Programming from the ground up. Kernel knowledge
is assumed and should have been acquired in a previous course or some years with hands
on experience in kernel programming.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
