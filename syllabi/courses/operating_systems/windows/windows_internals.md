---
tags:
  - infrastructure:windows
  - infrastructure:kernel
  - concepts:systems-programming
  - practices:debugging
level: advanced
category: operating-systems
duration_hours: 40
audience:
  - audiences:developers
  - audiences:systems-programmers
  - audiences:security-engineers
  - audiences:performance-engineers
---
<!-- course: windows_internals -->
# `Windows` Internals

## Description
This course takes an in-depth look at the internal architecture and mechanisms of the
`Windows` operating system. Students will learn how the `Windows` kernel is structured,
how processes and `threads` are created and scheduled, how memory is managed, how the
`I/O` system and device drivers work, and how the security subsystem enforces access
control. The course makes heavy use of tools such as the `Sysinternals` suite and the
`WinDbg` debugger so that every internal mechanism discussed is also observed live on a
running system. This knowledge is essential for developers writing system-level software,
for engineers debugging hard problems in production, for performance tuning, and for
security research on the `Windows` platform.

## Duration
40 hours / 5 days

## Intended Audience
* Developers writing system-level or performance-sensitive software on `Windows`.
* Engineers who need to debug complex application or system problems on `Windows`.
* Security engineers and researchers who need to understand how `Windows` works under the hood.
* Performance engineers who tune and troubleshoot `Windows` systems.
* Device driver developers who want a solid understanding of the kernel they are working in.

## Prerequisites
* Solid experience using `Windows`.
* Programming experience in a compiled language such as C, `C++`, Rust or `C#`.
* Basic understanding of general operating system concepts (processes, memory, files) is an advantage.

## Objectives
* understand the core architecture of the `Windows` operating system
* gain practical knowledge of process, `thread` and memory internals
* gain practical knowledge of the `I/O` system, the registry and the security subsystem
* gain practical knowledge of investigating a live system with `Sysinternals` tools and `WinDbg`

## Exercises
* Done with the `Sysinternals` suite and `WinDbg` on a `Windows` virtual machine.

## Outline
<!-- chapter: windows-architecture-overview, duration: 2h -->
* `Windows` Architecture Overview
    * History and evolution of the `NT` kernel
    * User mode vs kernel mode
    * The Executive, the kernel and the `HAL`
    * `ntoskrnl.exe`, `ntdll.dll` and system processes
    * Environment subsystems and the `Win32` `API`
    * The Native `API`
    * Symmetric `multiprocessing` in `Windows`
    * `Windows` editions and internals differences
<!-- chapter: system-mechanisms, duration: 3h -->
* System Mechanisms
    * Trap dispatching: interrupts and exceptions
    * Interrupt Request Levels (`IRQLs`)
    * Deferred Procedure Calls (`DPCs`)
    * Asynchronous Procedure Calls (`APCs`)
    * System call dispatching from user mode to kernel mode
    * The object manager
    * Objects, handles and reference counting
    * The object namespace
    * `Windows` global flags
<!-- chapter: tools-of-the-trade, duration: 2h -->
* Tools of the Trade
    * The `Sysinternals` suite
    * `Process Explorer` in depth
    * `Process Monitor` in depth
    * `Task Manager` and `Resource Monitor`
    * Event Tracing for `Windows` (`ETW`)
    * `Performance Monitor` and performance counters
    * `WinDbg`: user mode and kernel mode debugging
    * Setting up kernel debugging on a virtual machine
    * Working with symbols and symbol servers
<!-- chapter: processes, duration: 4h -->
* Processes
    * Process data structures: `EPROCESS` and the `PEB`
    * The flow of `CreateProcess`
    * Process listing and inspection tools
    * `Image` loading and the loader
    * `DLLs` and the import address table
    * Jobs and job objects
    * Minimal processes and pico processes
    * Protected processes and `PPL`
    * `UWP` and packaged processes
    * Process termination
<!-- chapter: threads-and-scheduling, duration: 4h -->
* `Threads` and Scheduling
    * `Thread` data structures: `ETHREAD` and the `TEB`
    * `Thread` creation and termination
    * `Thread` states and state transitions
    * Priorities and priority boosting
    * Quantum and quantum accounting
    * The dispatcher and context switching
    * Multiprocessor scheduling: affinity, ideal processor, `NUMA`
    * `CPU` sets
    * `Thread` pools
    * Fibers and User Mode Scheduling (`UMS`)
<!-- chapter: memory-management, duration: 5h -->
* Memory Management
    * Virtual address space layout (32 bit and 64 bit)
    * Address translation and page tables
    * Virtual Address Descriptors (`VADs`)
    * Reserved, committed and shared memory
    * Page faults and their types
    * Working sets and working set trimming
    * The page frame number database
    * Paging files and commit charge
    * Memory mapped files and sections
    * Copy on write
    * The user mode heap and heap types
    * Kernel pools: non-paged and paged pool
    * Large pages
    * Memory compression
    * Investigating memory with `VMMap` and `RAMMap`
<!-- chapter: synchronization, duration: 2h -->
* Synchronization
    * Why synchronization is needed in the kernel
    * Spinlocks and queued spinlocks
    * Dispatcher objects: events, mutexes, semaphores, timers
    * Waiting and the wait block mechanism
    * Executive resources and pushlocks
    * User mode synchronization: critical sections, `SRW` locks, condition variables
    * `WaitOnAddress` and `futex`-style waits
    * Detecting deadlocks
<!-- chapter: the-io-system, duration: 4h -->
* The `I/O` System
    * `I/O` system components and the `I/O` manager
    * Device drivers: types and structure
    * The `Windows` Driver Model (`WDM`) and `WDF` (`KMDF`/`UMDF`)
    * Driver objects and device objects
    * `I/O` Request Packets (`IRPs`) and their flow
    * Device stacks and filter drivers
    * Synchronous and asynchronous `I/O`
    * `I/O` completion ports
    * Plug and Play (`PnP`) and device enumeration
    * The power manager and power states
    * Investigating drivers and `IRPs` with `WinDbg`
<!-- chapter: the-registry, duration: 1h -->
* The Registry
    * Registry structure and root keys
    * Hives and hive files on disk
    * How the configuration manager works internally
    * Transactional registry operations
    * Monitoring registry activity with `Process Monitor`
<!-- chapter: services, duration: 2h -->
* Services
    * The Service Control Manager (`SCM`)
    * Service processes and service accounts
    * Shared service processes and `svchost.exe`
    * Service triggers and delayed start
    * Protected services
    * Investigating and troubleshooting services
<!-- chapter: security, duration: 4h -->
* Security
    * Security components: `LSASS`, `SRM` and the security database
    * Security Identifiers (`SIDs`)
    * Access tokens: primary and impersonation tokens
    * Security descriptors and Access Control Lists (`ACLs`)
    * The access check algorithm
    * Privileges and rights
    * Integrity levels and mandatory integrity control
    * User Account Control (`UAC`) internals
    * `AppContainer` and sandboxing
    * Virtualization Based Security (`VBS`) and `Hyper-V` isolation
    * `Credential Guard` and `Device Guard`
    * Logon and authentication flow
<!-- chapter: file-systems-and-the-cache-manager, duration: 3h -->
* `File` Systems and the Cache Manager
    * `File` system drivers and file system filter drivers
    * `NTFS` on-disk structure and the Master `File` Table (`MFT`)
    * `NTFS` features: hard links, reparse points, compression, sparse files
    * `NTFS` journaling and recovery
    * `ReFS` overview
    * The cache manager and how caching works
    * Read ahead and write behind
    * Investigating file system activity with `Process Monitor`
<!-- chapter: boot-process-and-startup, duration: 2h -->
* Boot Process and Startup
    * `UEFI` and Secure Boot
    * The `Windows` Boot Manager and `winload`
    * Kernel initialization phases
    * `smss.exe`, `csrss.exe`, `wininit.exe` and `winlogon.exe`
    * Driver loading order and boot drivers
    * Measured boot and `ELAM`
    * Troubleshooting boot problems
<!-- chapter: crash-dump-analysis, duration: 2h -->
* Crash Dump Analysis
    * Why systems crash: the bugcheck mechanism
    * Blue screen anatomy and common stop codes
    * Crash dump types and configuration
    * Analyzing crash dumps with `WinDbg`
    * The `!analyze` command and beyond
    * Finding the guilty driver
    * Analyzing user mode process dumps
    * Hung system analysis

## Installations
Each student should have:

* A `Windows` 10 or `Windows` 11 machine, real or virtual, with administrator privileges.
* A second `Windows` virtual machine (or nested virtualization support) for kernel debugging exercises.
* 8 GB `RAM` or more for the host machine.
* The `Sysinternals` suite downloaded from Microsoft.
* `WinDbg` installed from the Microsoft Store or as part of the `Windows` `SDK`.
* Free access to the internet from all machines for downloading tools and debugging symbols.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
