---
tags:
  - infrastructure:linux
  - hardware-and-embedded:embedded
  - infrastructure:kernel
  - hardware-and-embedded:bsp
  - infrastructure:cross-compilation
  - tools:u-boot
  - tools:yocto
  - tools:buildroot
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: embedded_linux_platform_development -->
# Embedded `Linux` Platform Development

## Description
This course deals with developing embedded systems based on the `Linux` kernel. It covers the various approaches for building such a system and compares their advantages and disadvantages as well as explaining other tools useful in this space such as various emulation, debugging and building tools.

The course also deals with the substantial task for configuring the `Linux` kernel, at compile time and at run time. This is a huge subject so it cannot be fully covered in a course such as this. The objective is not to fully cover the topic but to provide a good foundation from which the students can `go` on to expand their knowledge.

Major topics which are a must for embedded platform developers such as filesystems, flash, boot, cross compilation, hardware and are also covered.

## Duration
40 hours / 5 days

## Intended Audience
* People developing devices using the `Linux` kernel
* People supporting embedded `Linux` system developers
* Embedded `Linux` engineers who have never created a `Linux` image on their own
* Kernel developers who would like a better understanding of how embedded `Linux` systems are built

## Prerequisites
* Knowledge and practice of `UNIX` or GNU/`Linux` commands
* Some embedded experience (in `Linux` or other systems) is a must.
* Kernel `Linux` programming is an advantage.

## Objectives
* Be able to understand the overall architecture of Embedded `Linux` systems.
* Be able to choose, build, setup and use a cross-compilation toolchain.
* Be able to understand the booting sequence of an embedded `Linux` system, and to set up and use the `U-Boot` bootloader.
* Be able to select a `Linux` kernel version, to configure, build and install the `Linux` kernel on an embedded system.
* Be able to create from scratch a `Linux` root filesystem, including all its elements: directories, applications, configuration files, libraries.
* Be able to choose and setup the main `Linux` filesystems for block and flash storage devices, and understand their main characteristics.
* Be able to interact with hardware devices, configure the kernel with appropriate drivers and extend the `Device Tree`
* Be able to select, cross-compile and integrate open-source software components (libraries, applications) in an Embedded `Linux` system, and to handle license compliance.
* Be able to setup and use an embedded `Linux` build system, to build a complete system for an embedded platform.
* Be able to develop and debug applications on an embedded `Linux` system.

## Outline
<!-- chapter: introduction-to-embedded-linux, duration: 2h -->
* Introduction to embedded `Linux`
    * Advantages of `Linux` versus traditional embedded operating systems.
    * Typical hardware platforms used to run embedded `Linux` systems.
    * Overall architecture of embedded `Linux` systems: overview of the major software components.
    * Development environment for Embedded `Linux` development.
<!-- chapter: cross-compiling-toolchain-and-c-library, duration: 2h -->
* Cross-compiling toolchain and C library
    * What's inside a cross-compiling toolchain
    * Choosing the target C library
    * What's inside the C library
    * Ready to use cross-compiling toolchains
    * Building a cross-compiling toolchain with automated tools.
<!-- chapter: boot-process-firmware-bootloaders, duration: 2h -->
* Boot process, firmware, bootloaders
    * Booting process of embedded platforms, focus on the `x86` and `ARM` architectures
    * Boot process and bootloaders on `x86` platforms (legacy and `UEFI`)
    * Boot process on `ARM` platforms: ROM code, bootloaders, `ARM` Trusted Firmware
    * Focus on `U-Boot`: configuration, installation, and usage.
    * `U-Boot` commands, `U-Boot` environment, `U-Boot` scripts, `U-Boot` generic distro boot mechanism
<!-- chapter: linux-kernel, duration: 2h -->
* `Linux` kernel
    * Role and general architecture of the `Linux` kernel
    * Separation between kernel and user-space, and interfaces between user-space and the `Linux` kernel
    * Understanding `Linux` kernel versions: choosing between vendor-provided kernel and upstream kernel, Long Term Support
versions
    * Getting the `Linux` kernel source code
<!-- chapter: configuring-compiling-and-booting-the-linux-kernel, duration: 3h -->
* Configuring, compiling and booting the `Linux` kernel
    * Configuring the `Linux` kernel: ready-made configuration files, configuration interfaces
    * Concept of `Device Tree`
    * Cross-compiling the `Linux` kernel
    * Study of the generated files and their role
    * Installing and booting the `Linux` kernel
    * The `Linux` kernel command line
<!-- chapter: root-filesystem-in-linux, duration: 3h -->
* Root filesystem in `Linux`
    * Filesystems in `Linux`.
    * Role and organization of the root filesystem.
    * Location of the root filesystem: on storage, in memory, from the network.
    * Device files, virtual filesystems.
    * Contents of a typical root filesystem
<!-- chapter: busybox, duration: 1h -->
* `BusyBox`
    * Detailed overview. Detailed features.
    * Configuration, compiling and deploying.
<!-- chapter: accessing-hardware-devices, duration: 4h -->
* Accessing hardware devices
    * How to access hardware on popular busses: `USB`, `SPI`, `I2C`, `PCI`
    * Usage of kernel drivers and direct userspace access
    * The `Device Tree` syntax, and how to use it to describe additional devices and pin-muxing
    * Finding `Linux` kernel drivers for specific hardware devices
    * Using kernel modules
    * Hardware access using /dev and /sys
    * User-space interfaces for the most common hardware devices: storage, network, `GPIO`, LEDs, audio, graphics, video
<!-- chapter: block-filesystems, duration: 4h -->
* Block filesystems
    * Accessing and partitioning block devices.
    * Filesystems for block devices.
    * Usefulness of journaled filesystems.
    * Read-only block filesystems.
    * `RAM` filesystems.
    * How to create each of these filesystems.
    * Suggestions for embedded systems.
<!-- chapter: flash-filesystems, duration: 3h -->
* Flash filesystems
    * The Memory Technology Devices (MTD) filesystem.
    * Filesystems for MTD storage: JFFS2, Yaffs2, UBIFS.
    * Kernel configuration options
    * MTD storage partitions.
    * Focus on today's best solution, UBI and UBIFS: preparing, flashing and using UBI images.
<!-- chapter: cross-compiling-user-space-libraries-and-applications, duration: 3h -->
* Cross-compiling user-space libraries and applications
    * Configuring, cross-compiling and installing applications and libraries.
    * Concept of build system, and overview of a few common build systems used by open-source projects: `Makefile`, `autotools`, `CMake`, `meson`
    * Overview of the common issues encountered when cross-compiling.
<!-- chapter: embedded-system-building-tools, duration: 2h -->
* Embedded system building tools
    * Approaches for building embedded `Linux` systems: build systems and binary distributions
    * Principle of build systems, overview of `Yocto` Project/`OpenEmbedded` and `Buildroot`.
    * Principle of binary distributions and useful tools, focus on `Debian`/`Ubuntu`
    * Specialized software frameworks/distributions: Tizen, AGL, `Android`
<!-- chapter: open-source-licenses-and-compliance, duration: 2h -->
* Open source licenses and compliance
    * Presentation of the most important open-source licenses: GPL, LGPL, MIT, BSD, Apache, etc.
    * Concept of copyleft licenses
    * Differences between (L)GPL version 2 and 3
    * Compliance with open-source licenses: best practices
<!-- chapter: overview-of-major-embedded-linux-software-stacks, duration: 3h -->
* Overview of major embedded `Linux` software stacks
    * `systemd` as an init system
    * Hardware management with `udev`
    * Inter-process communication with `D-Bus`
    * The connectivity software stack: `Ethernet`, `WiFi`, modems, `Bluetooth`
    * The graphics software stack: DRM/`KMS`, X.org, `Wayland`, Qt, GTK, `OpenGL`
    * The multimedia software stack: Video4Linux, `GStreamer`, Pulseaudio, `Pipewire`
<!-- chapter: application-development-and-debugging, duration: 3h -->
* Application development and debugging
    * Programming languages and libraries available.
    * Build system for your application, an overview of `CMake` and `meson`
    * The `gdb` debugger: remote debugging with `gdbserver`, post-mortem debugging with core files
    * Performance analysis, tracing and profiling tools, memory checkers: `strace`, `ltrace`, `perf`, `valgrind`
<!-- chapter: useful-resources, duration: 1h -->
* Useful resources
    * Books about embedded `Linux` and system programming
    * Useful online resources
    * International conferences

## References
* [slides for this course](`https`://bootlin.com/doc/training/embedded-`linux`/)

## Installations
* A real, virtual or remote machine running `Ubuntu` LTS >= 22.04
* The machine should have *free* access to the internet to install software.
* The students should have an account on the machines with `sudo` privileges.
* In any case the student must have `sudo`/root on this virtual machine and the machines should be connected to the internet.
* There is no need for special installations on the machine. The instructor will guide the students to install whatever is needed.
* The machine should have at least 15GB free disk space.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
