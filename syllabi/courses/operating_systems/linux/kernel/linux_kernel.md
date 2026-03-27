---
tags:
  - linux
  - kernel
  - device-drivers
  - embedded
  - bsp
  - real-time
level: advanced
category: operating-systems
duration_days: 5
audience:
  - developers
  - embedded-engineers
---
# `Linux` Kernel

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This `Linux` kernel is now the most widely used operating system on the planet and many development
teams need to know how to add device support to it, understand it's performance characteristics,
tune it, compile it, reduce it's size, provide board support for it, develop platforms based on it,
understand it's real time support and much more.

This course is all about the `Linux` kernel but is focused on writing device drivers for the kernel as
this is the first typical thing one learns when becoming a kernel developer.

No kernel prior knowledge is required but knowledge of `Linux` user space `API` and programming tools is
required.

## Duration
40 hours / 5 days

## Intended Audience
* embedded systems engineers and kernel developers
* system programmers working on low-level software

## Prerequisites
* experience with C programming
* familiarity with Linux system administration

## Objectives
* understand the core concepts and principles of Linux` Kernel
* gain practical knowledge of Linux` Kernel Introduction
* gain practical knowledge of Kernel Sources
* gain practical knowledge of Compiling

## Outline
* `Linux` Kernel Introduction
    * System and kernel overview
    * Kernel code specifics
    * Kernel subsystems
    * History and versioning scheme
    * Understanding the development process
    * Specific legal issues
    * Kernel user interface
* Kernel Sources
    * Getting the sources
    * Using the patch command
    * Structure of source files
    * Kernel source code browsers
* Compiling
    * Kernel configuration
    * Useful settings for embedded systems
    * Compiling
    * Generated files
    * Make commands for configuring, compiling or installing a kernel
* Booting
    * `Linux` system booting overview
    * The boot-loader's job
    * Review of `Linux` boot-loaders
    * U-boot details
    * `Linux` kernel booting
    * Advantages of initramfs over initrd
    * Booting parameters
    * NFS boot example
    * System startup
* Cross-compiling
    * Kernel cross-compiling setup
    * Ready-made configuration files for specific architectures & boards
    * Cross-compiling
* Basic Driver Development
    * `Linux` device drivers
    * A simple module
    * Programming constraints
    * Loading, unloading modules
    * Module parameters and dependencies
    * Adding sources to the kernel tree
* `Linux` Memory Management
    * `Linux` memory management
    * Physical and virtual (kernel and user) address spaces
    * `Linux` memory management implementation
    * Allocating with `kmalloc`, by pages and with `vmalloc`
* I/O Memory
    * I/O register and memory range registration
    * I/O register and memory access
    * Read / write memory barriers
* Character Drivers
    * Device numbers
    * Getting free device numbers
    * File operations
    * Character driver registration
* Kernel Debugging
    * Using `printk`, /proc or /sys
    * Debugfs
    * Using an ioctl interface, `gdb` and kgdb
* Processes and scheduling
    * Process life
    * Timer frequency
    * Priorities and timeslices
    * Sleeping and waking up `API`
* Interrupts
    * Waiting for the availability of resources
    * Interrupt handler registration
    * Scheduling deferred work
* Concurrency management
    * Managing concurrent access to resources: mutexes, spinlocks
    * Atomic operations
* Advice and resources
    * Getting help and contributions
    * Bug report and patch submission to `Linux` developers
    * References: websites, books & international conferences
* Kernel boot-up details
    * Detailed description of the kernel boot-up process, from execution by the boot-loader to the execution of the first userspace program
    * Initcalls: how to register your own initialization routines?
* Introduction to BSP development
    * Board Support Packages (BSP)
    * Porting U-boot and the `Linux` kernel
    * Creating board dependent code
    * Studying code for an ARM board
* Introduction to power management
    * Supporting frequency scaling
    * CPU and board specific power management
    * Power management in device drivers
    * Control from user space
    * Saving power in the idle loop
    * Studying power management implementations in the `Linux` kernel
* Introduction to `Linux` Real-Time Programming
    * Understanding the sources of latency in standard `Linux`
    * Soft real-time solutions for `Linux`: improvements in `Linux` 2.6
    * Use the latest RT preempt patches for mainstream `Linux`
    * Real-time kernel debugging.
    * Measuring and analyzing latency
    * Hard real-time solutions for `Linux`
    * RTLinux issues, the RTAI and Xenomai projects
    * Comparing with RT preempt patches
    * Real-time offerings from commercial `Linux` vendors: MontaVista, TimeSys, Wind River, LynuxWorks etc.
* C library and cross-compiling tool-chain
    * Choosing the target C library
    * Ready to use cross-compiling tool-chains
    * Building a cross-compiling tool-chain with automated tools
    * Installing cross-compiled libraries in the root filesystem
* Embedded system development tools
    * Commercial toolsets and distributions
    * Community toolsets (focus on `Buildroot` & Scratchbox)
    * How to find existing Free Software for a particular need
* BusyBox
    * Detailed Overview and features
    * Configuration, compiling and deploying
    * Saving space by implementing your own applets
* Lightweight tools for embedded systems
    * `HTTP` and ssh servers
    * Graphical toolkits
    * Web browsers
    * Text editors
    * Precompiled packages and distributions
* Choosing file-systems
    * File-systems for block devices
    * Usefulness of journaled filesystems
    * Read-only block file-systems
    * RAM file-systems
    * File-systems for Memory Technology Devices (MTD)
    * Suggestions for embedded systems
* Udev and hot-plugging
    * Handling hardware events from userspace
    * Creating and removing device files
    * Identifying drivers, notifying programs and users

## References
* [slides for this course](https://bootlin.com/doc/training/linux-kernel/)

## Installations
* A real, virtual or remote machine running `Ubuntu` >= 22.04
* The machine should have *free* access to the internet to install software.
* The students should have an account on the machines with sudo privileges.
* In any case the student must have sudo/root on this virtual machine and the machines should be connected to the internet.
* There is no need for special installations on the machine. The instructor will guide the students to install whatever is needed.
* The machine should have at least 15GB free disk space.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
