---
tags:
  - hardware-and-embedded:embedded
  - hardware-and-embedded:iot
  - networking:protocols
level: intermediate
category: embedded
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: lorawan_and_lpwan -->
# LoRaWAN and LPWAN

## Description
This course provides a comprehensive exploration of Low-Power Wide-Area Network (LPWAN) technologies with a primary focus on LoRaWAN. Participants will learn the `LoRa` physical layer, LoRaWAN network architecture, device classes, security model, and practical device development. The course also covers competing LPWAN technologies including Sigfox, NB-IoT, and LTE-M, enabling participants to `make` informed technology choices for their IoT projects.

## Duration
16 hours / 2 days

## Intended Audience
* Embedded developers building long-range, low-power IoT devices
* IoT solution architects selecting communication technologies
* Engineers deploying sensor networks and asset tracking systems
* Developers working with `The Things Network` or similar LoRaWAN platforms

## Prerequisites
* Basic understanding of wireless communication concepts
* Familiarity with embedded development (microcontrollers, `GPIO`, serial interfaces)
* Experience with at least one programming language (C, `C++`, `Python`, or Arduino)
* General awareness of IoT concepts and use cases

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Understand LPWAN concepts and compare available technologies
* Explain the `LoRa` physical layer including spread spectrum modulation and spreading factors
* Design LoRaWAN networks with appropriate device classes, activation methods, and data rate strategies
* Implement LoRaWAN security using `AES`-128 encryption and session key management
* Build LoRaWAN devices using Arduino, ESP32, or STM32 platforms
* Deploy and configure LoRaWAN gateways and network servers
* Optimize power consumption and range for real-world deployments

## Outline
<!-- chapter: lpwan-concepts-and-comparison, duration: 2h -->
* LPWAN Concepts and Comparison
    * What is LPWAN and why it matters for IoT
    * LPWAN vs `WiFi`, cellular, and short-range wireless
    * LoRaWAN overview and ecosystem
    * Sigfox architecture and capabilities
    * NB-IoT (Narrowband IoT)
    * LTE-M (Long Term Evolution for Machines)
    * Technology comparison: range, power, cost, data rate, and coverage
    * Choosing the right LPWAN technology for your application
<!-- chapter: lora-physical-layer, duration: 1h -->
* `LoRa` Physical Layer
    * Spread spectrum modulation principles
    * Chirp Spread Spectrum (`CSS`) modulation
    * Spreading factors (SF7 through SF12)
    * Bandwidth and frequency band considerations
    * Link budget calculation
    * Trade-offs between range, data rate, and airtime
    * Regulatory constraints (ISM bands, duty cycle, EIRP limits)
<!-- chapter: lorawan-architecture, duration: 2h -->
* LoRaWAN Architecture
    * End devices (nodes)
    * Gateways and their role
    * Network server
    * Application server
    * Star-of-stars topology
    * Uplink and downlink communication
    * Network architecture design considerations
<!-- chapter: device-classes, duration: 1h -->
* Device Classes
    * Class A: baseline, lowest power
    * Class B: beacon-synchronized receive `windows`
    * Class C: continuous receive, lowest latency
    * Choosing the right class for your application
    * Power consumption implications of each class
<!-- chapter: activation-methods, duration: 1h -->
* Activation Methods
    * Over-the-Air Activation (OTAA)
    * Activation by Personalization (ABP)
    * Join procedure and join servers
    * Device provisioning workflows
    * OTAA vs ABP trade-offs and recommendations
<!-- chapter: adaptive-data-rate, duration: 1h -->
* Adaptive Data Rate
    * ADR algorithm and purpose
    * Network-managed vs device-managed data rates
    * ADR behavior in mobile vs stationary deployments
    * Configuring and tuning ADR
<!-- chapter: lorawan-security, duration: 1h -->
* LoRaWAN Security
    * `AES`-128 encryption
    * Network session key (NwkSKey) and application session key (AppSKey)
    * Application key (AppKey) and join process security
    * Frame counter management
    * LoRaWAN 1.1 security enhancements
    * Security best practices for device provisioning
<!-- chapter: the-things-network-the-things-industries, duration: 1h -->
* `The Things Network` / `The Things Industries`
    * TTN community network overview
    * `The Things Industries` commercial platform
    * Console and `CLI` usage
    * Application and device registration
    * Payload formatters and integrations
    * `MQTT` and `HTTP` integration options
<!-- chapter: building-lorawan-devices, duration: 1h -->
* Building LoRaWAN Devices
    * `LoRa` radio modules (SX1276, SX1262)
    * Arduino-based LoRaWAN development
    * ESP32 with `LoRa` (e.g., TTGO, Heltec)
    * STM32 with `LoRa` (STM32WL, external modules)
    * LoRaWAN stacks (LMIC, LoRaMac-node, RadioLib)
    * Antenna selection and design considerations
<!-- chapter: gateway-setup, duration: 1h -->
* Gateway Setup
    * Gateway hardware options (indoor, outdoor, DIY)
    * Single-channel vs multi-channel gateways
    * Gateway configuration and registration
    * Backhaul connectivity (`Ethernet`, `WiFi`, cellular)
    * Gateway placement and coverage planning
<!-- chapter: payload-encoding, duration: 1h -->
* Payload Encoding
    * Why payload encoding matters (airtime optimization)
    * CayenneLPP (Cayenne Low Power Payload)
    * Custom binary encoding
    * Payload decoders and formatters
    * Balancing payload size with data richness
<!-- chapter: power-optimization, duration: 1h -->
* Power Optimization
    * Sleep modes and wake-up strategies
    * Transmission scheduling and duty cycle management
    * Battery selection and capacity planning
    * Solar and energy harvesting considerations
    * Measuring and profiling power consumption
<!-- chapter: range-planning, duration: 1h -->
* Range Planning
    * Site survey techniques
    * Propagation models and path loss
    * Antenna height and placement optimization
    * Urban vs rural deployment considerations
    * Dealing with obstructions and interference
<!-- chapter: use-cases, duration: 1h -->
* Use Cases
    * Smart agriculture (soil moisture, weather monitoring)
    * Smart cities (parking, waste management, street lighting)
    * Asset tracking and logistics
    * Environmental monitoring
    * Building management and smart metering
    * Industrial monitoring and predictive maintenance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
