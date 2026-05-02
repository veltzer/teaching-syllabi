---
tags:
  - hardware-and-embedded:hardware
  - hardware-and-embedded:interrupts
  - hardware-and-embedded:dma
  - hardware-and-embedded:embedded
level: advanced
category: hardware
duration_hours: 96
audience:
  - audiences:embedded-engineers
  - audiences:developers
---
<!-- course: working_with_hardware -->
# Working with Hardware

## Description
Low level developers usually need to interact with hardware. This course explains
the various types of hardware devices that are out there and how to work with these
devices. It goes through interrupts, ports, memory mapping, `DMA`, interrupt less communication,
`i2c`, interrupt mitigation and other subjects.

## Duration
12 days / 96 hours

## Intended Audience
* Programmers who wish to understand all the intricacies of interacting with modern hardware

## Prerequisites
* C programming
* Understanding real time concepts is an advantage
* Familiarity with real time operating systems is an advantage.
* Familiarity with secure operating systems (`Linux`) is an advantage.
* `C++` is an advantage

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of Working with Hardware
* gain practical knowledge of Basics of hardware design
* gain practical knowledge of Reading data-sheets
* gain practical knowledge of Interrupts

## Outline
<!-- chapter: basics-of-hardware-design, duration: 9h -->
* Basics of hardware design
    * Traditional `CPU`
    * Micro controllers/MCU
    * System on chip/`SoC`
    * Multi core systems
    * Virtual cores
<!-- chapter: reading-data-sheets, duration: 1h -->
* Reading data-sheets
<!-- chapter: interrupts, duration: 13h -->
* Interrupts
    * What are interrupts?
    * Different types of interrupts at the hardware level
    * How to handle interrupts
    * Acknowledging IRQs to hardware
    * Interrupts `CPU` affinity in multi-core systems
    * Interrupts and priorities
    * Sharing interrupts
    * Deferring work on incoming data
<!-- chapter: io-ports, duration: 6h -->
* IO Ports
    * What are io ports?
    * Reading and writing
    * Buffer sizes
<!-- chapter: io-memory, duration: 7h -->
* IO memory
    * mapping memory
    * reading and writing
    * memory barriers
    * cycling through buffers
<!-- chapter: i2c, duration: 6h -->
* `I2C`
    * what is `i2c`?
    * Sending and receiving messages
    * `i2c` limitations
<!-- chapter: gpio, duration: 4h -->
* `GPIO`
    * What is `GPIO` hardware?
    * Reading and writing `GPIO`
<!-- chapter: dma, duration: 11h -->
* `DMA`
    * What is `DMA`?
    * Allocating memory for `DMA`
    * Different types of `DMA` buffers
    * Cycling through buffers to allow processing
    * Getting notified when `DMA` is done
    * `CPU` memory caching and `DMA`
<!-- chapter: storage, duration: 5h -->
* Storage
    * NAND flash
    * `File`-systems
<!-- chapter: bootloaders, duration: 6h -->
* Bootloaders
    * The role of the bootloader
    * Examples of bootloaders
    * Configuring bootloaders
<!-- chapter: power-management, duration: 5h -->
* Power management
    * Hardware support for power management
    * Things to deal with (cleanup, registration and more)
<!-- chapter: bsp, duration: 17h -->
* `BSP`
    * What is a `BSP`? Who write it?
    * Board Bring Up
    * Initialization Sequence
    * Device Trees
    * Memory
    * Interrupts and Timers
    * Device Drivers
    * IODevices
    * IORequest Model
    * Standard Driver Interfaces
<!-- chapter: debugging-hardware-issues, duration: 6h -->
* Debugging hardware issues
    * Hardware support for debugging - external
    * Hardware support for debugging - software
    * JTAG

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
