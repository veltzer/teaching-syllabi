---
tags:
  - hardware-and-embedded:embedded
  - networking:protocols
  - hardware-and-embedded:automotive
level: intermediate
category: embedded
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: can_bus_and_automotive -->
# CAN Bus and Automotive Protocols

## Description
This course provides a thorough exploration of the CAN bus protocol and related automotive communication technologies. Participants will learn the fundamentals of CAN signaling, frame formats, error handling, and higher-layer protocols used in automotive and industrial applications. The course also covers modern developments including `CAN FD`, `Automotive Ethernet`, and AUTOSAR, along with hands-on experience using industry-standard analysis tools.

## Duration
16 hours / 2 days

## Intended Audience
* Embedded software developers working on automotive or industrial systems
* Engineers developing ECU firmware and vehicle communication software
* Test and validation engineers working with in-vehicle networks
* Developers integrating CAN-based devices into larger systems

## Prerequisites
* Experience with embedded C or `C++` programming
* Basic understanding of serial communication concepts
* Familiarity with binary and hexadecimal data representation
* General knowledge of microcontroller peripherals

## Objectives
* Understand CAN bus physical layer, arbitration, and error handling mechanisms
* Work with `CAN 2.0A`, `CAN 2.0B`, and `CAN FD` frame formats
* Configure bit timing and baud rate settings for CAN controllers
* Implement CAN communication in embedded firmware
* Use higher-layer protocols including CANopen, J1939, OBD-II, and UDS
* Analyze CAN traffic using industry tools such as PCAN, `Vector CANoe`, and Kvaser
* Understand the role of `Automotive Ethernet` and AUTOSAR in modern vehicles

## Outline
<!-- chapter: can-bus-fundamentals, duration: 1h -->
* CAN Bus Fundamentals
    * History and motivation for CAN
    * Differential signaling and physical layer
    * Bus topology and termination
    * Arbitration mechanism and message priority
    * Non-destructive bitwise arbitration
    * Error handling and fault confinement
    * Error active, error passive, and bus-off states
<!-- chapter: can-frame-formats, duration: 1h -->
* CAN Frame Formats
    * `CAN 2.0A` standard frame (11-bit identifier)
    * `CAN 2.0B` extended frame (29-bit identifier)
    * Data frame, remote frame, error frame, overload frame
    * Bit stuffing
    * CRC calculation and error detection
    * Acknowledgment mechanism
<!-- chapter: can-fd, duration: 1h -->
* `CAN FD`
    * Motivation for `CAN FD` (flexible data rate)
    * `CAN FD` frame format differences
    * Higher data rates and larger payloads
    * Backward compatibility with classical CAN
    * Bit rate switching
    * `CAN FD` adoption considerations
<!-- chapter: bit-timing-and-baud-rates, duration: 1h -->
* Bit Timing and Baud Rates
    * CAN bit timing segments
    * Synchronization and resynchronization
    * Sample point configuration
    * Baud rate calculation and prescaler settings
    * Oscillator tolerance requirements
<!-- chapter: message-filtering, duration: 1h -->
* Message Filtering
    * Hardware acceptance filtering
    * Mask and identifier-based filtering
    * Receive FIFO and mailbox configurations
    * Software-level message dispatching
<!-- chapter: error-detection-and-handling, duration: 1h -->
* Error Detection and Handling
    * Five error detection mechanisms in CAN
    * Bit error, stuff error, CRC error, form error, acknowledgment error
    * Error counters and bus-off recovery
    * Designing robust error handling strategies
    * Bus diagnostics and health monitoring
<!-- chapter: higher-layer-protocols, duration: 1h -->
* Higher-Layer Protocols
    * CANopen protocol and object dictionary
    * `SAE J1939` for heavy-duty vehicles
    * OBD-II diagnostic protocol and PIDs
    * Protocol selection criteria for different applications
<!-- chapter: uds-unified-diagnostic-services, duration: 1h -->
* UDS (Unified Diagnostic Services)
    * UDS overview and `ISO 14229`
    * Diagnostic sessions and security access
    * DID read and write services
    * Routine control and ECU programming
    * DTC management and fault memory
    * Transport layer (ISO-TP / `ISO 15765`)
<!-- chapter: lin-bus-overview, duration: 1h -->
* LIN Bus Overview
    * LIN bus architecture and master-slave model
    * LIN frame structure
    * Scheduling and time-triggered communication
    * LIN vs CAN use cases
<!-- chapter: flexray-overview, duration: 1h -->
* FlexRay Overview
    * FlexRay architecture and dual-channel design
    * Time-triggered and event-triggered communication
    * FlexRay frame format
    * FlexRay applications in chassis and safety systems
<!-- chapter: automotive-ethernet, duration: 1h -->
* `Automotive Ethernet`
    * 100BASE-T1 and 1000BASE-T1
    * `Ethernet` in the vehicle: motivation and architecture
    * SOME/`IP` and service-oriented communication
    * AVB/TSN for time-sensitive networking
    * Coexistence with legacy bus systems
<!-- chapter: autosar-basics, duration: 1h -->
* AUTOSAR Basics
    * AUTOSAR Classic vs AUTOSAR Adaptive
    * Software component architecture
    * Communication stack overview
    * RTE (Runtime Environment)
    * AUTOSAR COM and PDU routing
<!-- chapter: can-hardware, duration: 1h -->
* CAN Hardware
    * CAN transceivers and controllers
    * Standalone CAN controllers vs integrated peripherals
    * Selecting CAN hardware for embedded projects
    * Development boards and evaluation kits
<!-- chapter: can-analysis-tools, duration: 1h -->
* CAN Analysis Tools
    * PCAN tools and interfaces
    * `Vector CANoe` and CANalyzer
    * Kvaser hardware and software
    * Open-source tools (can-utils, `python`-can)
    * Logging, replay, and simulation
<!-- chapter: embedded-can-programming, duration: 1h -->
* Embedded CAN Programming
    * CAN peripheral configuration on microcontrollers
    * Transmitting and receiving CAN frames
    * Interrupt-driven vs polling-based reception
    * `DMA` for CAN communication
    * Building a CAN application layer
<!-- chapter: security-considerations, duration: 1h -->
* Security Considerations
    * Threats to in-vehicle networks
    * CAN bus vulnerabilities (spoofing, injection, denial of service)
    * Authentication and encryption approaches
    * Intrusion detection for CAN networks
    * Secure ECU communication strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
