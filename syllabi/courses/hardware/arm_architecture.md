---
tags:
  - hardware-and-embedded:embedded
  - hardware-and-embedded:arm
  - concepts:systems-programming
level: intermediate
category: hardware
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: arm_architecture -->
# `ARM` Architecture

## Description
This course provides a comprehensive exploration of the `ARM` architecture, from the instruction
set and register model through memory management, security extensions, and bare-metal programming.
Students will work with both Cortex-M microcontrollers and Cortex-A application processors,
gaining hands-on experience with the `ARM` toolchain, debugging interfaces, and the boot process.

## Duration
32 hours / 4 days

## Intended Audience
* Embedded developers who need to understand and program `ARM`-based systems.
* Systems programmers moving from other architectures to `ARM`.

## Prerequisites
* `Solid` `C` programming skills.
* Basic understanding of computer architecture concepts.
* Familiarity with a `Linux` command-line environment.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of the `ARM` architecture family
* gain practical knowledge of the `ARM` instruction set and register model
* gain practical knowledge of memory management, caching, and security extensions
* gain practical knowledge of bare-metal programming and debugging on `ARM` targets

## Outline
<!-- chapter: arm-architecture-overview, duration: 2h -->
* `ARM` Architecture Overview
    * History and evolution of `ARM`
    * ARMv7 architecture
    * ARMv8/AArch64 architecture
    * `ARM` licensing model
    * `ARM` ecosystem and market segments
<!-- chapter: arm-instruction-set, duration: 2h -->
* `ARM` Instruction Set
    * `ARM` instruction encoding
    * Data processing instructions
    * Load and store instructions
    * Branch instructions
    * Conditional execution
<!-- chapter: registers-and-addressing-modes, duration: 2h -->
* Registers and Addressing Modes
    * General-purpose registers
    * Special-purpose registers (SP, LR, PC)
    * AArch64 register `file`
    * Addressing modes (immediate, register, scaled)
    * Status flags and condition codes
<!-- chapter: arm-vs-thumb-instruction-set, duration: 2h -->
* `ARM` vs Thumb Instruction Set
    * Thumb and Thumb-2 encoding
    * Interworking between `ARM` and Thumb
    * Code density trade-offs
    * `When` to use each instruction set
<!-- chapter: exception-handling-and-interrupt-model, duration: 2h -->
* Exception Handling and Interrupt Model
    * Exception types and priorities
    * Vector tables
    * Exception entry and return
    * NVIC on Cortex-M
    * GIC on Cortex-A
    * Interrupt latency considerations
<!-- chapter: memory-management, duration: 3h -->
* Memory Management
    * `MMU` architecture
    * Translation tables and page sizes
    * `TLB` operation and maintenance
    * Cache architecture (L1, L2, L3)
    * Cache coherency protocols
    * Memory ordering and barriers
<!-- chapter: neon-simd, duration: 2h -->
* NEON SIMD
    * NEON register `file`
    * NEON data types and operations
    * Vectorizing loops
    * Intrinsics vs `assembly`
    * Performance considerations
<!-- chapter: trustzone-security, duration: 2h -->
* TrustZone Security
    * TrustZone architecture overview
    * Secure and non-secure worlds
    * Secure monitor calls
    * Trusted execution environments
    * TrustZone for Cortex-M
<!-- chapter: arm-cortex-m-for-microcontrollers, duration: 2h -->
* `ARM` Cortex-M for Microcontrollers
    * Cortex-M processor family (M0, M3, M4, M7, M33)
    * Cortex-M programming model
    * Low-power modes
    * Peripheral access
    * SysTick timer
<!-- chapter: arm-cortex-a-for-application-processors, duration: 2h -->
* `ARM` Cortex-A for Application Processors
    * Cortex-A processor family
    * Multi-core configurations
    * Virtualization extensions
    * Running an operating system on Cortex-A
<!-- chapter: arm-toolchain, duration: 2h -->
* `ARM` Toolchain
    * `GCC` for `ARM` (`arm`-none-eabi-`gcc`, aarch64-`linux`-gnu-`gcc`)
    * `LLVM`/`Clang` for `ARM`
    * Linker scripts
    * `Assembly` syntax (unified `assembly` language)
    * Build systems for `ARM` targets
<!-- chapter: debugging-with-jtag-swd, duration: 3h -->
* Debugging with JTAG/SWD
    * JTAG protocol overview
    * SWD protocol overview
    * Debug probes and adapters
    * OpenOCD setup and usage
    * `GDB` remote debugging
    * Semihosting
<!-- chapter: boot-process, duration: 2h -->
* Boot Process
    * `ARM` boot sequence
    * Bootloaders (`U-Boot`, vendor-specific)
    * `Device tree` basics
    * Secure boot chain
    * Boot from different media
<!-- chapter: bare-metal-programming, duration: 2h -->
* Bare-Metal Programming
    * Startup code and vector table setup
    * Stack initialization
    * Peripheral initialization
    * Linker scripts for bare-metal
    * Minimal runtime environment
<!-- chapter: cmsis, duration: 2h -->
* CMSIS
    * CMSIS overview and components
    * CMSIS-Core for device access
    * CMSIS-DSP library
    * CMSIS-RTOS `API`
    * CMSIS-Pack and software distribution

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
