---
tags:
  - hardware-and-embedded:embedded
  - hardware-and-embedded:riscv
  - concepts:systems-programming
level: intermediate
category: hardware
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: riscv_architecture -->
# `RISC-V` Architecture

## Description
This course covers the `RISC-V` open-source instruction set architecture from its design
philosophy through practical application. Students will learn the base and extension instruction
sets, the privileged architecture, and how to work with the `RISC-V` toolchain and simulators.
The course also explores the growing `RISC-V` ecosystem for embedded and application-class processors.

## Duration
24 hours / 3 days

## Intended Audience
* Developers interested in the `RISC-V` open-source architecture.
* Embedded engineers evaluating `RISC-V` for new designs.
* Systems programmers who want to understand `RISC-V` internals.

## Prerequisites
* `Solid` C programming skills.
* Basic understanding of computer architecture concepts.
* Familiarity with at least one other `ISA` (`ARM`, `x86`) is an advantage.

## Objectives
* understand the core concepts and philosophy of the `RISC-V` `ISA`
* gain practical knowledge of the base and extension instruction sets
* gain practical knowledge of the `RISC-V` privileged architecture and memory model
* gain practical knowledge of the `RISC-V` toolchain, simulators, and ecosystem

## Outline
<!-- chapter: risc-v-isa-overview-and-philosophy, duration: 1h -->
* `RISC-V` `ISA` Overview and Philosophy
    * History and motivation behind `RISC-V`
    * Open-source `ISA` advantages
    * `RISC-V` Foundation and standardization
    * Modular `ISA` design principles
    * `RISC-V` vs proprietary `ISAs`
<!-- chapter: base-integer-instruction-sets, duration: 1h -->
* Base Integer Instruction Sets
    * RV32I base integer instructions
    * RV64I base integer instructions
    * Register file and calling conventions
    * Instruction encoding formats
    * Immediate handling and addressing
<!-- chapter: standard-extensions, duration: 2h -->
* Standard Extensions
    * M extension (integer multiply/divide)
    * A extension (atomic operations)
    * F extension (single-precision floating point)
    * D extension (double-precision floating point)
    * C extension (compressed instructions)
    * V extension (vector operations)
    * Combining extensions (e.g., RV64GC)
<!-- chapter: privileged-architecture, duration: 2h -->
* Privileged Architecture
    * Machine mode
    * Supervisor mode
    * User mode
    * Control and Status Registers (CSRs)
    * Privilege level transitions
    * PMP (Physical Memory Protection)
<!-- chapter: memory-model, duration: 1h -->
* Memory Model
    * `RISC-V` weak memory ordering
    * Fence instructions
    * Atomic memory operations
    * Memory consistency guarantees
    * Cache management
<!-- chapter: interrupt-handling, duration: 1h -->
* Interrupt Handling
    * Interrupt and exception model
    * Trap delegation
    * CLINT and PLIC interrupt controllers
    * Timer interrupts
    * External interrupt handling
<!-- chapter: risc-v-toolchain, duration: 1h -->
* `RISC-V` Toolchain
    * `GCC` for `RISC-V`
    * `LLVM`/`Clang` for `RISC-V`
    * Assembler and linker
    * Newlib and musl C libraries
    * Build system integration
<!-- chapter: simulators, duration: 2h -->
* Simulators
    * `QEMU` for `RISC-V`
    * Spike `ISA` simulator
    * Verilator for RTL simulation
    * Debugging with `GDB` on simulators
    * Simulation-driven development workflow
<!-- chapter: soc-ecosystem, duration: 2h -->
* `SoC` Ecosystem
    * `RISC-V` `SoC` design considerations
    * Bus protocols (TileLink, AXI)
    * Peripheral integration
    * Open-source `SoC` projects (BOOM, Rocket)
    * `FPGA` prototyping
<!-- chapter: comparison-with-arm-and-x86, duration: 2h -->
* Comparison with `ARM` and `x86`
    * `ISA` complexity comparison
    * Ecosystem maturity
    * Performance considerations
    * Licensing and cost differences
    * Migration strategies
<!-- chapter: risc-v-for-embedded, duration: 2h -->
* `RISC-V` for Embedded
    * SiFive product line
    * ESP32-C3 and ESP32-C6
    * Bare-metal programming on `RISC-V`
    * RTOS support for `RISC-V`
    * Peripheral libraries
<!-- chapter: linux-on-risc-v, duration: 2h -->
* `Linux` on `RISC-V`
    * Kernel support status
    * Boot process on `RISC-V`
    * OpenSBI firmware
    * `U-Boot` for `RISC-V`
    * Available `Linux` distributions
<!-- chapter: custom-extensions, duration: 1h -->
* Custom Extensions
    * Designing custom instructions
    * Reserved opcode space
    * Toolchain support for custom extensions
    * Verification of custom extensions
<!-- chapter: debugging, duration: 2h -->
* Debugging
    * `RISC-V` debug specification
    * Debug module interface
    * JTAG debugging
    * OpenOCD support for `RISC-V`
    * Trace and profiling
<!-- chapter: future-of-risc-v, duration: 2h -->
* Future of `RISC-V`
    * Upcoming standard extensions
    * Industry adoption trends
    * `RISC-V` in high-performance computing
    * `RISC-V` in automotive and safety-critical systems
    * Community and ecosystem growth

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
