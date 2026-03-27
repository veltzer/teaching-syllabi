---
tags:
  - hardware
  - interrupts
  - dma
  - embedded
level: advanced
category: hardware
duration_days: 12
audience:
  - embedded-engineers
  - developers
---
# Working with Hardware

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Low level developers usually need to interact with hardware. This course explains
the various types of hardware devices that are out there and how to work with these
devices. It goes through interrupts, ports, memory mapping, `DMA`, interrupt less communication,
i2c, interrupt mitigation and other subjects.

## Duration
12 days / 96 hours

## Intended Audience
* Programmers who wish to understand all the intricacies of interacting with modern hardware

## Prerequisites
* C programming
* Understanding real time concepts is an advantage
* Familiarity with real time operating systems is an advantage.
* Familiarity with secure operating systems (`Linux`) is an advantage.
* C++ is an advantage

## Outline
* Basics of hardware design
    * Traditional CPU
    * Micro controllers/MCU
    * System on chip/SoC
    * Multi core systems
    * Virtual cores
* Reading data-sheets
* Interrupts
    * What are interrupts?
    * Different types of interrupts at the hardware level
    * How to handle interrupts
    * Acknowledging IRQs to hardware
    * Interrupts CPU affinity in multi-core systems
    * Interrupts and priorities
    * Sharing interrupts
    * Deferring work on incoming data
* IO Ports
    * What are io ports?
    * Reading and writing
    * Buffer sizes
* IO memory
    * mapping memory
    * reading and writing
    * memory barriers
    * cycling through buffers
* I2C
    * what is i2c?
    * Sending and receiving messages
    * i2c limitations
* `GPIO`
    * What is `GPIO` hardware?
    * Reading and writing `GPIO`
* `DMA`
    * What is `DMA`?
    * Allocating memory for `DMA`
    * Different types of `DMA` buffers
    * Cycling through buffers to allow processing
    * Getting notified when `DMA` is done
    * CPU memory caching and `DMA`
* Storage
    * NAND flash
    * File-systems
* Bootloaders
    * The role of the bootloader
    * Examples of bootloaders
    * Configuring bootloaders
* Power management
    * Hardware support for power management
    * Things to deal with (cleanup, registration and more)
* BSP
    * What is a BSP? Who write it?
    * Board Bring Up
    * Initialization Sequence
    * Device Trees
    * Memory
    * Interrupts and Timers
    * Device Drivers
    * IODevices
    * IORequest Model
    * Standard Driver Interfaces
* Debugging hardware issues
    * Hardware support for debugging - external
    * Hardware support for debugging - software
    * JTAG

## Copyright
Mark Veltzer, © 2026
