---
tags:
  - linux
  - embedded
  - boot-time
  - optimization
  - kernel
  - buildroot
level: advanced
category: operating-systems
duration_days: 2
audience:
  - developers
  - embedded-engineers
---
# Embedded `Linux` boot time optimization

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This intensive one-day course focuses on techniques and strategies to reduce `Linux` kernel boot time. Participants will learn to analyze, optimize, and streamline the boot process for improved system performance.

## Duration
16 hours / 2 days

## Intended Audience
* People developing embedded `Linux` systems.
* People supporting embedded `Linux` system developers.

## Prerequisites
* Knowledge and practice of `UNIX` or GNU/`Linux` commands
* Minimal experience in embedded `Linux` development

## Objectives
* Be able to use various tools and techniques to measure the boot time of an embedded `Linux` system.
* Be able to reduce the boot time spent during the user-space initialization.
* Be able to reduce the boot time spent during the kernel initialization.
* Be able to reduce the boot time spent during the bootloader initialization.
* Be able to use advanced and alternatives techniques of boot time optimization.

## Outline
* Principles
    * How to measure boot time
    * Main ideas
* Demo - Prepping a system
    * Creating a system that we will be using to analyze boot time
* Measuring time
    * Generic software techniques
    * Hardware techniques
    * Specific solutions for each stage
* Demo - Measuring time - Software solution
    * Modify the system to measure time at various steps
    * Timing messages on the serial console
    * Timing the launching of the application
* Toolchain optimizations
    * Introduction to toolchains
    * C libraries
    * Size information
    * Measuring executable performance with time
* Demo - Toolchain optimizations
    * Measuring application execution time
    * Switching to a Thumb2 toolchain
    * Generate a `Buildroot` `SDK` to rebuild faster
* Application optimization
    * Using strace and ltrace
    * Other profiling techniques
* Demo - Application optimization
    * Finding unnecessary configuration options in applications
    * Modifying configuration options through `Buildroot`
    * Experiments with strace to trace program execution
* Optimizing system initialization
    * Using BusyBox bootchartd
    * Optimizing init scripts
    * Possibility to start your application directly
* Demo - Optimizing system initialization
    * Using `Buildroot` to remove unnecessary scripts and commands
    * Access-time based technique to identify unused files
    * Simplifying BusyBox
    * Starting the application as the init program
* Filesystem optimizations
    * Available filesystems, performance and boot time aspects
    * Making UBIFS faster
    * Tweaks for reducing boot time
    * Booting on an initramfs
    * Using static executables: licensing constraints
* Demo - Filesystem optimizations
    * Trying and measuring two block filesystems: ext4 and SquashFS.
    * Trying and measuring the initramfs solution. Constraints due to this solution.
* Kernel optimizations
    * Using Initcall debug to generate a boot graph
    * Compression and size features
    * Reducing or suppressing console output
    * Multiple tweaks to reduce boot time
* Demo - Kernel optimizations
    * Generating and analyzing a boot graph for the kernel
    * Find and eliminate unnecessary kernel features
    * Find the best kernel compression solution for our system

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
