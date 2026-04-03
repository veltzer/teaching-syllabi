---
tags:
  - hardware-and-embedded:embedded
  - hardware-and-embedded:fpga
  - concepts:parallel-computing
level: advanced
category: embedded
duration_hours: 40
audience:
  - audiences:developers
---
<!-- course: fpga_programming -->
# `FPGA` Programming

## Description
This course provides a thorough introduction to `FPGA` programming, covering digital design fundamentals, hardware description languages (VHDL and Verilog), and the complete `FPGA` development workflow from design to deployment. Participants will learn `FPGA` architecture, simulation, synthesis, timing analysis, and debugging techniques. The course also covers advanced topics including HLS (high-level synthesis), communication interfaces, and `SoC` integration with platforms such as Xilinx Zynq and Intel `SoC` `FPGA`.

## Duration
40 hours / 5 days

## Intended Audience
* Embedded developers transitioning to `FPGA`-based designs
* Hardware engineers looking to deepen their `FPGA` expertise
* Software engineers working on hardware/software co-design projects
* Engineers developing high-performance or real-time systems with FPGAs

## Prerequisites
* `Solid` understanding of digital logic fundamentals (gates, flip-flops, combinational and sequential circuits)
* Experience with at least one programming language (`C`, `C++`, or `Python`)
* Basic understanding of computer architecture (registers, memory, buses)
* Familiarity with binary and hexadecimal number systems

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Understand `FPGA` architecture and how it differs from processors and ASICs
* Design and implement digital circuits using VHDL and Verilog
* Write simulation testbenches and verify designs before synthesis
* Apply timing constraints and resolve timing closure issues
* Implement communication interfaces (`UART`, `SPI`, `I2C`, AXI) on FPGAs
* Use Xilinx Vivado and Intel Quartus toolchains for synthesis, implementation, and debugging
* Apply HLS techniques to accelerate development from `C`/`C++` code

## Outline
<!-- chapter: fpga-architecture, duration: 3h -->
* `FPGA` Architecture
    * `FPGA` vs `ASIC` vs microcontroller
    * Configurable Logic Blocks (CLBs)
    * Input/Output Blocks (IOBs)
    * Block `RAM` and distributed memory
    * DSP slices
    * Routing architecture and interconnect
    * Clock resources and clock management tiles
    * `FPGA` families and device selection
<!-- chapter: digital-design-fundamentals, duration: 2h -->
* Digital Design Fundamentals
    * Combinational logic review
    * Sequential logic review
    * Timing concepts (setup, hold, propagation delay)
    * Synchronous design principles
    * Reset strategies (synchronous vs asynchronous)
    * Design partitioning and hierarchy
<!-- chapter: vhdl, duration: 3h -->
* VHDL
    * Entities and architectures
    * Signals and variables
    * Data types and operators
    * Processes and sensitivity lists
    * Concurrent and sequential statements
    * Packages and libraries
    * Generics and generate statements
    * Structural vs behavioral descriptions
<!-- chapter: verilog, duration: 3h -->
* Verilog
    * Modules and ports
    * Wire and reg types
    * always blocks and assign statements
    * Blocking vs non-blocking assignments
    * Parameterized modules
    * Continuous and procedural assignments
    * Task and `function-definitions`
<!-- chapter: systemverilog-basics, duration: 2h -->
* SystemVerilog Basics
    * Enhancements over Verilog
    * New data types (logic, enum, struct, union)
    * Interfaces and modports
    * always_comb, always_ff, always_latch
    * Assertions for design verification
<!-- chapter: simulation-and-testbenches, duration: 3h -->
* Simulation and Testbenches
    * Writing self-checking testbenches
    * Stimulus generation
    * Clock and reset generation
    * `File` `I/O` in testbenches
    * Waveform analysis
    * Simulation tools and workflows
    * Code coverage and functional coverage basics
<!-- chapter: synthesis-and-implementation, duration: 2h -->
* Synthesis and Implementation
    * RTL synthesis concepts
    * Synthesis constraints and directives
    * Resource utilization analysis
    * Place and route
    * Implementation strategies and optimization
    * Bitstream generation and device programming
<!-- chapter: timing-constraints, duration: 2h -->
* Timing Constraints
    * Clock definition and clock groups
    * Input and output delay constraints
    * Multicycle and false paths
    * Timing reports and analysis
    * Timing closure strategies
    * Static timing analysis fundamentals
<!-- chapter: clock-domain-crossing, duration: 2h -->
* Clock Domain Crossing
    * Metastability and its consequences
    * Synchronizer circuits (two-flop, three-flop)
    * Handshake-based crossing
    * FIFO-based crossing
    * Gray code counters for FIFO pointers
    * CDC verification techniques
<!-- chapter: state-machines, duration: 2h -->
* State Machines
    * Moore and Mealy state machines
    * One-hot vs binary encoding
    * State machine `design patterns`
    * Safe state machines and error recovery
    * State machine optimization
<!-- chapter: memory-interfaces, duration: 2h -->
* Memory Interfaces
    * Block `RAM` instantiation and inference
    * Single-port and dual-port memories
    * ROM implementation
    * External memory interfaces (DDR, SRAM)
    * Memory controllers
<!-- chapter: communication-interfaces, duration: 2h -->
* Communication Interfaces
    * `UART` implementation
    * `SPI` master and slave
    * `I2C` controller design
    * AXI protocol family (AXI4, AXI4-Lite, AXI4-Stream)
    * Custom bus protocols
<!-- chapter: ip-cores, duration: 2h -->
* `IP` Cores
    * Using vendor-provided `IP` cores
    * `IP` catalog and configuration
    * Integrating third-party `IP`
    * Creating reusable `IP` blocks
    * `IP` packaging and versioning
<!-- chapter: xilinx-vivado-intel-quartus-toolchains, duration: 2h -->
* Xilinx Vivado / Intel Quartus Toolchains
    * Project creation and management
    * Design entry and source management
    * Synthesis and implementation workflows
    * Constraint management
    * Device programming and configuration
    * Tool comparison and selection
<!-- chapter: debugging, duration: 2h -->
* Debugging
    * Integrated Logic Analyzer (ILA) in Vivado
    * SignalTap in Quartus
    * Virtual `I/O` for runtime control
    * Hardware debugging methodology
    * Common debugging scenarios and solutions
<!-- chapter: hls-high-level-synthesis, duration: 3h -->
* HLS (High-Level Synthesis)
    * HLS concepts and workflow
    * Writing `C`/`C++` for synthesis
    * Pragmas and directives for optimization
    * Pipeline and loop optimization
    * Interface synthesis
    * HLS vs RTL design trade-offs
<!-- chapter: soc-integration, duration: 3h -->
* `SoC` Integration
    * Xilinx Zynq architecture (`PS` + PL)
    * Intel `SoC` `FPGA` architecture
    * Hardware/software partitioning
    * AXI interconnect for `PS`-PL communication
    * Embedded software development for `SoC` FPGAs
    * Boot process and system configuration

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
