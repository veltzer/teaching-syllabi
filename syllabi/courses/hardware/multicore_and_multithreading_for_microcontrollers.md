---
tags:
  - microcontrollers
  - multi-core
  - multithreading
  - concurrency
  - embedded
  - rtos
level: advanced
category: hardware
duration_days: 2
audience:
  - embedded-engineers
  - firmware-developers
---
# Multi-Core and Multi-Threading for Microcontrollers

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Modern microcontrollers increasingly feature multiple cores and hardware threading
capabilities. This course provides an in-depth look at how to write concurrent and
parallel software for multi-core microcontrollers such as the `ARM Cortex-M` dual-core
families, `ESP32`, and `RP2040`. Topics range from memory architecture and atomic
operations to inter-core communication, real-time scheduling, and hardware-assisted
synchronization. The course emphasizes practical, bare-metal and `RTOS`-based approaches
to building correct, deterministic, multi-threaded firmware.

## Duration
16 hours / 2 days

## Intended Audience
* Firmware developers working with multi-core microcontrollers
* Embedded engineers moving from single-core to multi-core platforms
* `RTOS` application developers who need to understand low-level concurrency
* Engineers developing high-throughput or safety-critical embedded systems

## Prerequisites
* C programming (mandatory)
* Basic microcontroller programming (peripherals, interrupts, registers)
* Familiarity with at least one `RTOS` is an advantage
* Understanding of computer architecture (caches, buses) is helpful

## Outline
* Multi-Core Microcontroller Architectures
    * Why multi-core in embedded systems
    * Symmetric vs asymmetric multi-processing (`SMP` vs `AMP`)
    * Common multi-core `MCU` families (`RP2040`, `ESP32`, `STM32H7`, `NXP i.MX RT`)
    * Core topologies: homogeneous and heterogeneous cores
    * Boot sequences for multi-core `MCUs` (primary core, secondary core startup)
    * Inter-core hardware: mailboxes, hardware semaphores, shared peripherals
* Memory Architecture and Layouts
    * Unified vs split memory models
    * Tightly-coupled memory (`TCM`) and per-core `SRAM`
    * Shared `SRAM` regions and memory partitioning
    * Linker scripts for multi-core: placing code and data per core
    * Memory protection units (`MPU`) in a multi-core context
    * Stack placement strategies for multiple threads and cores
    * Flash execution vs `RAM` execution trade-offs
* Cache Coherency and Memory Ordering
    * Instruction and data caches on `Cortex-M7` and similar cores
    * Cache coherency problems in multi-core `MCUs`
    * Memory barriers: `DMB`, `DSB`, `ISB` on `ARM`
    * Compiler barriers and the `volatile` keyword
    * Write-through vs write-back caching strategies
    * Cache maintenance operations (clean, invalidate, flush)
    * When caches matter and when they do not (cache-less `Cortex-M0+`)
* Atomic Operations and Lock-Free Programming
    * Why atomics matter on multi-core `MCUs`
    * `ARM` exclusive access instructions (`LDREX`/`STREX`, `LDAEX`/`STLEX`)
    * C11 `<stdatomic.h>` on embedded targets
    * Atomic read-modify-write patterns (increment, compare-and-swap, test-and-set)
    * Building lock-free data structures: ring buffers, single-producer/single-consumer queues
    * `ABA` problem and sequence counters
    * Hardware semaphores (`HSEM`) on `STM32` dual-core parts
* Mutual Exclusion and Synchronization Primitives
    * Spinlocks: when they make sense on microcontrollers
    * Priority inversion and priority inheritance
    * Disabling interrupts as a synchronization mechanism (single-core vs multi-core)
    * Critical sections that span multiple cores
    * Mutexes and binary semaphores under an `RTOS`
    * Counting semaphores
    * Reader-writer locks
    * Condition variables and event groups
    * Deadlock detection and avoidance strategies
* Inter-Core Communication: Message Queues
    * Hardware mailbox peripherals (registers, interrupts, flow control)
    * Software message queues: fixed-size vs variable-size messages
    * Zero-copy message passing using shared memory and pointers
    * `FreeRTOS` message buffers and stream buffers for multi-core
    * `OpenAMP` and `RPMsg` frameworks
    * Designing protocols between cores (command/response, publish/subscribe)
    * Latency and throughput considerations
    * Backpressure and queue overflow strategies
* Threading Models and `RTOS` Integration
    * Bare-metal super-loop on each core
    * Running an `RTOS` on one core vs both cores
    * `FreeRTOS` `SMP` support
    * Thread creation, priorities, and core affinity (pinning tasks to cores)
    * Idle tasks and per-core idle hooks
    * Tick synchronization across cores
    * Choosing the right threading model for your application
* Interrupts in a Multi-Core Environment
    * Interrupt routing: which core handles which interrupt
    * `NVIC` per core on dual-core `ARM` systems
    * Inter-processor interrupts (`IPI`)
    * Sharing peripherals between cores and interrupt ownership
    * ISR-to-task communication across cores
    * Nested vectored interrupt controller configuration for `SMP`
* Shared Peripheral Access
    * Peripheral ownership models (exclusive, shared, arbitrated)
    * Hardware semaphore-guarded peripheral access
    * `DMA` channels and multi-core coordination
    * Shared `GPIO`, `UART`, `SPI`, and `I2C` across cores
    * Clock and power domain considerations
* Memory-Mapped Communication Patterns
    * Shared-memory ring buffers between cores
    * Dual-port `SRAM` and its uses
    * Descriptor-based communication (scatter-gather)
    * Memory-mapped command and status registers
    * Doorbell interrupts to signal data availability
* Debugging and Profiling Multi-Core Firmware
    * Multi-core aware `JTAG`/`SWD` debugging
    * Setting breakpoints per core
    * Trace and profiling tools (`ETM`, `ITM`, `SWO`)
    * Diagnosing race conditions and deadlocks
    * Logging from multiple cores without corruption
    * Deterministic replay and record-based debugging
    * Common multi-threading bugs in firmware
* Real-Time and Safety Considerations
    * Worst-case execution time analysis with multiple cores
    * Priority ceiling protocols
    * Lock-free designs for hard real-time paths
    * Functional safety standards (`IEC 61508`, `ISO 26262`) and multi-core
    * Core-to-core latency measurement
    * Watchdog strategies for multi-core (per-core vs global watchdog)
    * Graceful degradation when one core fails
* Practical Patterns and Anti-Patterns
    * Producer-consumer between cores
    * Pipeline processing across cores
    * Partitioning workloads: data parallelism vs task parallelism
    * Shared-nothing architectures on multi-core `MCUs`
    * When not to use multi-core (overhead vs benefit)
    * Power consumption implications of running multiple cores

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
