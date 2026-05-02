---
tags:
  - hardware-and-embedded:rtos
  - hardware-and-embedded:embedded
  - hardware-and-embedded:iot
  - infrastructure:rtos
level: advanced
category: operating-systems
duration_hours: 24
audience:
  - audiences:embedded-engineers
  - audiences:firmware-developers
---
<!-- course: advanced_zephyr_rtos -->
# Advanced Zephyr RTOS

## Description
This advanced course takes participants beyond the basics of Zephyr RTOS into its more sophisticated subsystems and workflows. Topics include the device driver model, power management, `Bluetooth` stack (BLE and Mesh), sensor subsystem, networking protocols (`LwM2M`, `CoAP`, `MQTT`), custom board porting, and establishing `CI/CD` pipelines for Zephyr projects. The course is designed for engineers who already have introductory Zephyr experience and want to build production-grade firmware.

## Duration
24 hours / 3 days

## Intended Audience
* Embedded engineers developing production firmware on Zephyr.
* Firmware developers extending Zephyr with custom drivers and board support packages.

## Prerequisites
* Experience with real-time and embedded systems concepts.
* Familiarity with build systems and version control.

## Required Knowledge
* Zephyr RTOS (intro)
* C Programming

## Objectives
* Develop custom device drivers using the Zephyr driver model.
* Configure and optimize Zephyr power management for battery-powered devices.
* Implement `Bluetooth` Low Energy and `Bluetooth` Mesh applications.
* Integrate sensors using the Zephyr sensor subsystem.
* Port Zephyr to custom hardware boards.
* Build networked IoT applications using `LwM2M`, `CoAP`, and `MQTT`.
* Set up `CI/CD` pipelines for Zephyr firmware projects.

## Outline
<!-- chapter: zephyr-device-driver-model, duration: 2h -->
* Zephyr Device Driver Model
    * Driver architecture and lifecycle
    * Writing custom drivers
    * Devicetree bindings and overlays
    * Driver configuration via Kconfig
    * `DMA` integration
<!-- chapter: power-management-subsystem, duration: 2h -->
* Power Management Subsystem
    * Power states and transitions
    * Device power management `API`
    * System power management policies
    * Low-power peripheral operation
    * Battery life optimization strategies
<!-- chapter: bluetooth-stack, duration: 3h -->
* `Bluetooth` Stack
    * `Bluetooth` Low Energy (BLE) architecture in Zephyr
    * GATT services and characteristics
    * BLE advertising and scanning
    * `Bluetooth` Mesh networking
    * Mesh provisioning and configuration
    * BLE security and pairing
<!-- chapter: sensor-subsystem, duration: 2h -->
* Sensor Subsystem
    * Sensor `API` and architecture
    * Integrating sensor drivers
    * Sensor data channels and triggers
    * Sensor fusion techniques
<!-- chapter: flash-storage, duration: 2h -->
* Flash Storage
    * Flash area `API`
    * NVS (Non-Volatile Storage)
    * LittleFS and FAT file systems
    * Flash partitioning and management
    * Firmware update storage strategies
<!-- chapter: custom-board-porting, duration: 2h -->
* Custom Board Porting
    * Board definition files
    * Devicetree for custom hardware
    * `SoC` and board-level Kconfig
    * Pin multiplexing and configuration
    * Validation and testing of custom ports
<!-- chapter: zephyr-networking, duration: 3h -->
* Zephyr Networking
    * Network stack architecture
    * `LwM2M` client implementation
    * `CoAP` server and client
    * `MQTT` client integration
    * Network management and connection handling
    * Socket `API` and BSD sockets
<!-- chapter: posix-compatibility-layer, duration: 2h -->
* `POSIX` Compatibility Layer
    * `POSIX` `API` support in Zephyr
    * Porting `POSIX` applications to Zephyr
    * Limitations and differences
    * pthreads and synchronization primitives
<!-- chapter: testing-framework, duration: 3h -->
* Testing Framework
    * Ztest framework
    * Unit testing and integration testing
    * Mocking and stubbing hardware
    * Test suites and test automation
    * Twister test runner
<!-- chapter: ci-cd-for-zephyr-projects, duration: 3h -->
* `CI/CD` for Zephyr Projects
    * Build system integration (west, `CMake`)
    * Automated builds with `GitHub Actions` and `GitLab CI`
    * Hardware-in-the-loop testing
    * Firmware artifact management
    * Release and versioning strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
