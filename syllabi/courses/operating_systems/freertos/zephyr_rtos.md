---
tags:
  - hardware-and-embedded:rtos
  - hardware-and-embedded:embedded
  - concepts:systems-programming
level: intermediate
category: operating-systems
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: zephyr_rtos -->
# Zephyr RTOS

## Description
Zephyr is a scalable, open-source real-time operating system designed for
resource-constrained devices. This course provides a thorough exploration of the Zephyr
RTOS, from its build system and kernel fundamentals to advanced topics such as networking,
security, and porting to new hardware. Students will gain the skills needed to develop,
test, and debug embedded applications on Zephyr-supported platforms.

## Duration
32 hours / 4 days

## Intended Audience
* Embedded developers looking to adopt Zephyr for new or existing projects.
* Firmware engineers transitioning from other RTOS platforms.
* Developers who want to understand modern embedded RTOS architecture.

## Prerequisites
* `Solid` C programming skills.
* Basic understanding of embedded systems and microcontrollers.
* Familiarity with `Linux` command line and build tools.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of Zephyr RTOS
* gain practical knowledge of the Zephyr build system and tooling
* gain practical knowledge of kernel primitives and synchronization
* gain practical knowledge of device drivers and networking in Zephyr

## Outline
<!-- chapter: zephyr-overview-and-architecture, duration: 2h -->
* Zephyr Overview and Architecture
    * What is Zephyr RTOS
    * Project history and governance
    * Architecture overview
    * Supported hardware and boards
    * Comparison with other RTOS platforms
<!-- chapter: build-system, duration: 3h -->
* Build System
    * west meta-tool
    * `CMake` integration
    * Kconfig configuration system
    * Devicetree basics
    * Application structure and build flow
    * Managing external modules
<!-- chapter: kernel-fundamentals, duration: 2h -->
* Kernel Fundamentals
    * Threads and thread priorities
    * Scheduling algorithms (cooperative and preemptive)
    * Interrupt Service Routines (ISRs)
    * System clock and timers
    * Workqueues and deferred processing
<!-- chapter: synchronization-primitives, duration: 2h -->
* Synchronization Primitives
    * Semaphores
    * Mutexes
    * Condition variables
    * Atomic operations
    * Spinlocks
<!-- chapter: data-passing-mechanisms, duration: 3h -->
* Data Passing Mechanisms
    * FIFOs
    * LIFOs
    * Message queues
    * Pipes
    * Mailboxes
    * Choosing the right mechanism
<!-- chapter: memory-management, duration: 3h -->
* Memory Management
    * Kernel heaps
    * Memory pools
    * Memory slabs
    * Stack management
    * Memory protection (MPU integration)
<!-- chapter: device-driver-model, duration: 3h -->
* Device Driver Model
    * Driver model architecture
    * Device initialization levels
    * Writing a custom driver
    * Sensor subsystem
    * `GPIO`, `I2C`, `SPI`, `UART` interfaces
<!-- chapter: networking-stack, duration: 3h -->
* Networking Stack
    * `TCP`/`IP` networking
    * `Bluetooth` (BLE)
    * Wi-Fi support
    * IEEE 802.15.4
    * `LoRa` and LoRaWAN
    * Network management `API`
    * Sockets `API`
<!-- chapter: logging-and-shell, duration: 2h -->
* Logging and Shell
    * Logging subsystem and backends
    * Log levels and filtering
    * Shell subsystem
    * Custom shell commands
<!-- chapter: power-management, duration: 2h -->
* Power Management
    * Power states and transitions
    * Device power management
    * System power management
    * Tickless idle
<!-- chapter: security, duration: 2h -->
* Security
    * TF-M (Trusted Firmware-M) integration
    * Secure boot
    * Cryptography APIs
    * Secure storage
<!-- chapter: testing-and-debugging, duration: 3h -->
* Testing and Debugging
    * Zephyr testing framework (ztest)
    * Native `POSIX` port for testing
    * Twister test runner
    * Debugging with `GDB` and OpenOCD
    * Tracing and profiling
<!-- chapter: porting-to-new-hardware, duration: 2h -->
* Porting to New Hardware
    * Board porting guide
    * `SoC`-level support
    * Devicetree customization
    * Writing board-specific code

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
