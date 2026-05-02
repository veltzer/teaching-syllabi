---
tags:
  - hardware-and-embedded:embedded
level: intermediate
category: embedded
duration_hours: 16
audience:
  - audiences:embedded-engineers
  - audiences:developers
---
<!-- course: vxworks_and_non_secure_operating_systems -->
# `VxWorks` and Non-Secure Embedded Operating Systems

## Description
This course covers the principles and practice of non-secure (non-`MMU`) embedded
operating systems, with a focus on `VxWorks`. Students will learn how these systems
differ from secure operating systems like `Linux` and `Windows`, and gain hands-on
understanding of real-time operating system concepts, task management, interrupt
handling, and inter-task communication. The course also covers comparisons with
other popular embedded `RTOS` platforms such as `FreeRTOS` and Zephyr.

## Duration
16 hours / 2 days

## Intended Audience
* Embedded engineers working with real-time and resource-constrained systems
* Developers transitioning to embedded software development

## Prerequisites
* Strong C programming skills
* Basic understanding of computer architecture (`CPU`, memory, interrupts)
* Familiarity with operating system concepts

## Objectives
* Understand the principles of non-secure (non-`MMU`) operating systems
* Know the differences between secure and non-secure operating systems
* Understand real-time operating system concepts and scheduling
* Be proficient in `VxWorks` architecture, task management, and `I/O`
* Handle interrupt-driven programming in `VxWorks`
* Use inter-task communication mechanisms (semaphores, message queues, pipes)
* Debug `VxWorks` applications effectively
* Compare `VxWorks` with `FreeRTOS` and Zephyr

## Outline
<!-- chapter: principles-of-non-secure-operating-systems, duration: 1h -->
* Principles of Non-Secure (Non-`MMU`) Operating Systems
    * What is a non-secure operating system
    * Memory protection vs no memory protection
    * Flat memory model
    * Implications for reliability and fault isolation
    * Use cases for non-`MMU` systems
<!-- chapter: comparison-with-secure-operating-systems, duration: 1h -->
* Comparison with Secure Operating Systems
    * How `Linux` and `Windows` use the `MMU`
    * Process isolation and virtual memory
    * What you give up without an `MMU`
    * What you gain (performance, determinism, simplicity)
    * `When` to choose a non-secure vs secure `OS`
<!-- chapter: real-time-operating-system-concepts, duration: 1h -->
* Real-Time Operating System Concepts
    * Hard real-time vs soft real-time
    * Determinism and latency
    * Priority-based scheduling
    * Preemption
    * Real-time constraints and deadlines
<!-- chapter: vxworks-architecture, duration: 1h -->
* `VxWorks` Architecture
    * Overview of `VxWorks`
    * `VxWorks` editions and licensing
    * System architecture and components
    * Boot process
    * Development environment and toolchain
<!-- chapter: vxworks-kernel, duration: 1h -->
* `VxWorks` Kernel (Wind Kernel)
    * Kernel architecture
    * Kernel objects
    * System clock and timers
    * Kernel configuration
<!-- chapter: tasks-and-scheduling, duration: 1h -->
* Tasks and Scheduling in `VxWorks`
    * Task creation and deletion
    * Task states and transitions
    * Priority-based preemptive scheduling
    * Round-robin scheduling
    * Task hooks
    * Task variables
<!-- chapter: interrupt-handling, duration: 1h -->
* Interrupt Handling
    * Interrupt architecture in `VxWorks`
    * Interrupt service routines (`ISRs`)
    * Connecting interrupts to handlers
    * Interrupt latency
    * Deferred interrupt processing
    * Restrictions within `ISR` context
<!-- chapter: memory-management-without-mmu, duration: 1h -->
* Memory Management Without `MMU`
    * Static vs dynamic memory allocation
    * Memory partitions
    * Memory pools
    * Avoiding memory fragmentation
    * Common pitfalls in non-`MMU` environments
<!-- chapter: inter-task-communication, duration: 2h -->
* Inter-Task Communication
    * Semaphores (binary, counting, `mutex`)
    * Priority inversion and priority inheritance
    * Message queues
    * Pipes
    * Shared memory
    * Events and signals
<!-- chapter: vxworks-io-system, duration: 1h -->
* `VxWorks` `I/O` System
    * `I/O` system architecture
    * Device drivers
    * `File` systems
    * Serial and network `I/O`
    * `I/O` redirection
<!-- chapter: board-support-packages, duration: 1h -->
* Board Support Packages
    * What is a `BSP`
    * `BSP` components and structure
    * Configuring a `BSP` for target hardware
    * Hardware initialization sequence
<!-- chapter: vxworks-networking, duration: 1h -->
* `VxWorks` Networking
    * Network stack overview
    * `TCP`/`IP` in `VxWorks`
    * Socket programming
    * Network configuration
    * Network debugging
<!-- chapter: debugging-vxworks-applications, duration: 2h -->
* Debugging `VxWorks` Applications
    * `VxWorks` shell and debugging tools
    * Task-level debugging
    * System-level debugging
    * Using the `WindSh` shell
    * Common debugging scenarios
    * Post-mortem analysis
<!-- chapter: comparison-with-freertos-and-zephyr, duration: 1h -->
* Comparison with `FreeRTOS` and Zephyr
    * `FreeRTOS` overview and architecture
    * Zephyr overview and architecture
    * Feature comparison
    * Licensing and ecosystem differences
    * Choosing between `VxWorks`, `FreeRTOS`, and Zephyr

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
