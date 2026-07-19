---
tags:
  - infrastructure:windows
  - infrastructure:kernel
  - infrastructure:device-drivers
  - concepts:systems-programming
  - practices:debugging
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:systems-programmers
  - audiences:embedded-developers
  - audiences:firmware-developers
---
<!-- course: windows_driver_development -->
# `Windows` Driver Development

## Description
This course teaches how to design, write, debug and ship device drivers for the
`Windows` operating system. Students will learn the rules of kernel mode programming,
the structure of the `Windows` driver stack, and how `I/O` requests flow from an
application all the way down to the hardware. The course focuses on the modern
`Windows` Driver Frameworks (`KMDF` and `UMDF`) while also covering the underlying
`WDM` model that the frameworks are built upon. Substantial time is dedicated to the
practical side of driver work: setting up a kernel debugging environment, diagnosing
crashes with `WinDbg`, verifying drivers with `Driver Verifier`, writing secure driver
code, and signing and deploying drivers to real machines. Throughout the course
students write and extend real drivers and test them on a virtual machine.

## Duration
40 hours / 5 days

## Intended Audience
* Developers who need to write device drivers for `Windows`.
* Systems programmers moving into kernel mode development on `Windows`.
* Embedded and firmware developers whose hardware must be supported on `Windows`.
* Engineers who maintain, debug or extend existing `Windows` drivers.
* Security engineers who need to understand how drivers work in order to analyze them.

## Prerequisites
* Good working knowledge of the C programming language. `C++` is an advantage.
* Experience developing on `Windows`.
* Knowledge of `Windows` internals (processes, memory, `I/O` system) is a significant advantage.

## Objectives
* understand the core concepts and principles of kernel mode programming on `Windows`
* gain practical knowledge of writing drivers with `KMDF` and `UMDF`
* gain practical knowledge of handling `I/O` requests, Plug and Play and power management
* gain practical knowledge of debugging, verifying, signing and deploying `Windows` drivers

## Exercises
* Done with `Visual Studio`, the `WDK` and `WinDbg`, deploying to a `Windows` virtual machine.

## Outline
<!-- chapter: introduction-to-windows-drivers, duration: 2h -->
* Introduction to `Windows` Drivers
    * The role of drivers in the `Windows` architecture
    * User mode vs kernel mode revisited
    * The `I/O` manager, driver objects and device objects
    * Device stacks and the layered driver model
    * Types of drivers: function, filter, bus and software drivers
    * `WDM`, `KMDF` and `UMDF`: history and how to choose
    * The driver development landscape: `WDK`, signing, `HLK`
<!-- chapter: development-and-debugging-environment, duration: 2h -->
* Development and Debugging Environment
    * Installing `Visual Studio` and the `WDK`
    * Driver project structure and build configurations
    * Setting up a target virtual machine
    * Test signing and enabling test mode
    * Deploying and installing drivers on the target
    * Setting up kernel debugging over the network
    * `WinDbg` basics: symbols, breakpoints, source level debugging
<!-- chapter: kernel-programming-basics, duration: 4h -->
* Kernel Programming Basics
    * How kernel code differs from user code
    * The kernel `API` and its conventions
    * `NTSTATUS` and error handling
    * Interrupt Request Levels (`IRQLs`) and the rules they impose
    * Memory allocation: paged pool, non-paged pool and lookaside lists
    * Pool tags and tracking allocations
    * Strings in the kernel: `UNICODE_STRING`
    * Linked lists and other kernel data structures
    * Structured exception handling in the kernel
    * Accessing user buffers safely
    * Common kernel programming pitfalls
<!-- chapter: your-first-driver, duration: 3h -->
* Your First Driver
    * `DriverEntry` and driver initialization
    * The unload routine
    * Creating device objects
    * Device names and symbolic links
    * Opening a driver from user mode
    * `INF` files: structure and directives
    * Installing drivers with `INF` files and `devcon`
    * Viewing your driver with `WinObj` and `Device Manager`
<!-- chapter: irps-and-io-processing, duration: 4h -->
* `IRPs` and `I/O` Processing
    * The `I/O` Request Packet (`IRP`) structure
    * `I/O` stack locations
    * Dispatch routines
    * Create and close handling
    * Read and write requests
    * Device `I/O` control (`IOCTLs`) and defining control codes
    * Buffered `I/O`, direct `I/O` and neither `I/O`
    * Completing, pending and cancelling `IRPs`
    * Forwarding `IRPs` down the device stack
    * Completion routines
<!-- chapter: kmdf-fundamentals, duration: 4h -->
* `KMDF` Fundamentals
    * The `WDF` object model: objects, attributes and context
    * Object hierarchy, parenting and lifetime
    * `WDFDRIVER` and `WDFDEVICE` creation
    * Device interfaces vs device names
    * `I/O` queues and dispatching types
    * `WDFREQUEST`: retrieving buffers and completing requests
    * Request forwarding between queues and to `I/O` targets
    * `KMDF` and `IRPs`: what the framework does for you
    * Framework versioning and co-installers
<!-- chapter: plug-and-play-and-power-management, duration: 3h -->
* Plug and Play and Power Management
    * The `PnP` system and device enumeration
    * Hardware `IDs`, compatible `IDs` and driver ranking
    * The `PnP` state machine of a device
    * Resource assignment: ports, registers, interrupts, `DMA` channels
    * `KMDF` `PnP` and power callbacks
    * `EvtDevicePrepareHardware` and `EvtDeviceReleaseHardware`
    * Device and system power states
    * Idle detection and wake support
    * Surprise removal and orderly removal
<!-- chapter: hardware-access-interrupts-and-dma, duration: 3h -->
* Hardware Access, Interrupts and `DMA`
    * Mapping device registers into system space
    * Reading and writing hardware registers
    * Interrupt objects and connecting interrupts
    * Interrupt Service Routines (`ISRs`) and their constraints
    * Deferring work: `DPCs` for `ISRs`
    * Message Signaled Interrupts (`MSI`/`MSI-X`)
    * `DMA` concepts: common buffer and packet-based `DMA`
    * `DMA` in `KMDF`: enablers, transactions and callbacks
<!-- chapter: synchronization-in-drivers, duration: 3h -->
* Synchronization in Drivers
    * Concurrency in the kernel: why driver code races
    * Spinlocks and interrupt spinlocks
    * Mutexes, fast mutexes and executive resources
    * Work items for passive level work
    * Timers and `DPC` routines
    * `KMDF` synchronization scope and execution level
    * Lock hierarchies and avoiding deadlocks
    * Common concurrency bugs in drivers
<!-- chapter: filter-drivers, duration: 3h -->
* Filter Drivers
    * Where filters fit in the device stack
    * Upper and lower device filters
    * Class filters vs device filters
    * Writing a filter driver with `KMDF`
    * Attaching, forwarding and completing requests in filters
    * `File` system minifilters and the filter manager
    * Altitudes and load ordering
    * A minifilter skeleton: registration and operation callbacks
<!-- chapter: umdf-drivers, duration: 2h -->
* `UMDF` Drivers
    * Why user mode drivers: isolation and reliability
    * `UMDF` architecture: host process, reflector and framework
    * Differences between `UMDF` and `KMDF` code
    * When `UMDF` is the right choice
    * Writing and debugging a `UMDF` driver
<!-- chapter: debugging-and-testing-drivers, duration: 4h -->
* Debugging and Testing Drivers
    * Kernel debugging workflows with `WinDbg`
    * Debugging extensions for drivers: `!devobj`, `!drvobj`, `!irp`, `!wdfkd`
    * Analyzing driver crashes and interpreting bugchecks
    * `Driver Verifier`: options, workflow and interpreting violations
    * Detecting memory leaks and pool corruption
    * Static analysis: `Code Analysis` and `SAL` annotations
    * Static Driver Verifier (`SDV`)
    * Tracing with `WPP` and `ETW`
    * Testing with the Hardware Lab Kit (`HLK`)
<!-- chapter: driver-security, duration: 2h -->
* Driver Security
    * The driver attack surface
    * Validating and probing user mode input
    * Handle and object security in drivers
    * Securing device objects with security descriptors and `SDDL`
    * `IOCTL` hardening
    * Kernel exploit mitigations: `HVCI` and driver blocklists
    * Common driver vulnerability patterns and how to avoid them
<!-- chapter: signing-and-distribution, duration: 1h -->
* Signing and Distribution
    * The driver signing requirements landscape
    * Attestation signing vs `WHQL` certification
    * The `Windows` Hardware Developer Center workflow
    * `Windows Update` distribution
    * Servicing and updating shipped drivers

## Installations
Each student should have:

* A `Windows` 10 or `Windows` 11 development machine, real or virtual, with administrator privileges.
* A second `Windows` virtual machine as a deployment and kernel debugging target
(nested virtualization is fine).
* 16 GB `RAM` recommended for the host machine to run `Visual Studio` and the target virtual machine comfortably.
* `Visual Studio` (community edition is fine) with the `C++` desktop development workload.
* The `Windows` Driver Kit (`WDK`) matching the installed `Visual Studio` version.
* `WinDbg` installed from the Microsoft Store or as part of the `Windows` `SDK`.
* The `Sysinternals` suite downloaded from Microsoft.
* Free access to the internet from all machines for downloading tools and debugging symbols.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
