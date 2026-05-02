---
tags:
  - hardware-and-embedded:embedded
  - networking:protocols
  - hardware-and-embedded:iot
level: intermediate
category: embedded
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: ble_bluetooth_low_energy -->
# BLE - `Bluetooth` Low Energy

## Description
This course provides a thorough understanding of `Bluetooth` Low Energy (BLE), covering the
full protocol stack, GATT-based services, security mechanisms, and practical development on
embedded and mobile platforms. Students will learn to design, implement, and debug BLE
applications with a focus on power efficiency and interoperability.

## Duration
16 hours / 2 days

## Intended Audience
* Embedded developers building BLE-enabled devices.
* Mobile developers integrating BLE into `Android` or `iOS` applications.
* IoT engineers designing wireless sensor networks.

## Prerequisites
* C programming experience.
* Basic understanding of wireless communication concepts.
* Familiarity with embedded development is an advantage.

## Objectives
* understand the core concepts and principles of the BLE protocol stack
* gain practical knowledge of GATT services, characteristics, and profiles
* gain practical knowledge of BLE security, pairing, and bonding
* gain practical knowledge of BLE development on embedded and mobile platforms

## Outline
<!-- chapter: ble-overview, duration: 1h -->
* BLE Overview
    * `Bluetooth` evolution and BLE motivation
    * BLE vs classic `Bluetooth`
    * BLE use cases and market
    * BLE specification versions
    * Key terminology
<!-- chapter: ble-protocol-stack, duration: 2h -->
* BLE Protocol Stack
    * Physical layer (PHY)
    * Link Layer
    * L2CAP (Logical Link Control and Adaptation Protocol)
    * ATT (Attribute Protocol)
    * GATT (Generic Attribute Profile)
    * GAP (Generic Access Profile)
    * SMP (Security Manager Protocol)
    * Host Controller Interface (HCI)
<!-- chapter: advertising-and-scanning, duration: 1h -->
* Advertising and Scanning
    * Advertising types and intervals
    * Advertising data format
    * Scan request and scan response
    * Extended advertising (BLE 5.x)
    * Advertising strategies for power optimization
<!-- chapter: connections, duration: 1h -->
* Connections
    * Connection establishment
    * Connection parameters (interval, latency, timeout)
    * Connection parameter negotiation
    * PHY selection (1M, 2M, coded)
    * Data length extension
<!-- chapter: gatt-services-and-characteristics, duration: 1h -->
* GATT Services and Characteristics
    * GATT hierarchy (services, characteristics, descriptors)
    * Standard services and custom services
    * UUIDs (16-bit vs 128-bit)
    * Characteristic properties (read, write, notify, indicate)
    * Service discovery
<!-- chapter: profiles, duration: 1h -->
* Profiles
    * Standard BLE profiles (Heart Rate, HID, Battery)
    * Designing custom profiles
    * Profile interoperability
    * `Bluetooth` SIG adopted profiles
<!-- chapter: descriptors-and-notifications, duration: 1h -->
* Descriptors and Notifications
    * Client Characteristic Configuration Descriptor (CCCD)
    * Notifications vs indications
    * Subscription management
    * Throughput considerations
<!-- chapter: security, duration: 1h -->
* Security
    * Pairing methods (Just Works, Passkey, Numeric Comparison, OOB)
    * Bonding and key storage
    * Encryption (`AES`-CCM)
    * LE Secure Connections
    * Privacy and address randomization
    * Common security pitfalls
<!-- chapter: ble-on-embedded-platforms, duration: 1h -->
* BLE on Embedded Platforms
    * nRF52 series (`nRF Connect SDK`, SoftDevice)
    * ESP32 (NimBLE, Bluedroid)
    * STM32WB series
    * Zephyr RTOS BLE stack
    * Peripheral and central role implementation
<!-- chapter: ble-on-mobile, duration: 1h -->
* BLE on Mobile
    * BLE on `Android` (android.`bluetooth`.le)
    * BLE on `iOS` (CoreBluetooth)
    * Platform-specific limitations and quirks
    * Background BLE operations
    * Cross-platform frameworks
<!-- chapter: ble-on-linux, duration: 1h -->
* BLE on `Linux`
    * BlueZ stack overview
    * bluetoothctl and gatttool
    * `D-Bus` `API` for BLE
    * Programming with BlueZ in C and `Python`
    * `Linux` as a BLE peripheral
<!-- chapter: ble-mesh, duration: 1h -->
* BLE Mesh
    * BLE mesh overview and topology
    * Provisioning
    * Mesh models and messages
    * Relay, proxy, and friend nodes
    * Use cases for BLE mesh
<!-- chapter: power-optimization, duration: 1h -->
* Power Optimization
    * Connection interval tuning
    * Advertising interval trade-offs
    * Latency settings
    * Sleep modes and wake strategies
    * Measuring power consumption
<!-- chapter: debugging-tools, duration: 1h -->
* Debugging Tools
    * `nRF Sniffer` for BLE
    * `Wireshark` BLE dissector
    * HCI logging on `Linux` and mobile
    * Signal analysis
    * Common debugging scenarios
<!-- chapter: ble-5-x-features, duration: 1h -->
* BLE 5.x Features
    * 2M PHY for higher throughput
    * Coded PHY for extended range
    * Extended advertising
    * Periodic advertising
    * Direction finding (AoA/AoD)
    * Isochronous channels (BLE 5.2+)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
