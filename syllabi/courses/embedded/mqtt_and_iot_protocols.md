---
tags:
  - networking:protocols
  - hardware-and-embedded:iot
  - networking:networking
level: intermediate
category: embedded
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: mqtt_and_iot_protocols -->
# `MQTT` and IoT Protocols

## Description
This course provides a comprehensive introduction to messaging protocols used in the
Internet of Things. The primary focus is on `MQTT`, the most widely adopted lightweight
messaging protocol for IoT, but the course also covers complementary protocols such as
`CoAP` and `AMQP`. Students will learn how to design reliable, secure, and scalable IoT
communication architectures using modern brokers, serialization formats, and edge
computing patterns.

## Duration
16 hours / 2 days

## Intended Audience
* Developers building IoT solutions and connected device systems.
* Embedded engineers who need to integrate devices with cloud platforms.
* Backend developers designing message-driven IoT architectures.

## Prerequisites
* Basic networking knowledge (`TCP`/`IP`, `HTTP`).
* Familiarity with at least one programming language (`Python`, `C`, `JavaScript`, or similar).

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of IoT communication protocols
* gain practical knowledge of `MQTT` publish/subscribe messaging
* gain practical knowledge of broker deployment and configuration
* gain practical knowledge of securing IoT communications

## Outline
<!-- chapter: iot-communication-overview, duration: 1h -->
* IoT Communication Overview
    * The IoT landscape
    * Communication patterns in IoT
    * Constrained devices and networks
    * Protocol selection criteria
<!-- chapter: mqtt-protocol-fundamentals, duration: 3h -->
* `MQTT` Protocol Fundamentals
    * Publish/subscribe model
    * Topics and topic hierarchy
    * Wildcards (single-level and multi-level)
    * QoS levels (0, 1, 2)
    * Retained messages
    * Last Will and Testament
    * `Clean` and persistent sessions
    * Keep-alive and connection management
<!-- chapter: mqtt-brokers, duration: 2h -->
* `MQTT` Brokers
    * Mosquitto setup and configuration
    * HiveMQ overview
    * EMQX overview
    * Broker clustering and high availability
    * Bridging brokers
<!-- chapter: mqtt-5-0-features, duration: 2h -->
* `MQTT` 5.0 Features
    * Shared subscriptions
    * Message expiry
    * Topic aliases
    * User properties
    * Request/response pattern
    * Flow control
<!-- chapter: complementary-protocols, duration: 2h -->
* Complementary Protocols
    * `CoAP` (Constrained Application Protocol)
    * `AMQP` overview
    * `HTTP` vs `MQTT` for IoT
    * `WebSocket` transport for `MQTT`
    * Protocol bridging
<!-- chapter: security, duration: 1h -->
* Security
    * `TLS` encryption for `MQTT`
    * Authentication mechanisms (username/password, certificates, tokens)
    * Authorization and `ACLs`
    * Securing broker deployments
<!-- chapter: message-serialization, duration: 1h -->
* Message Serialization
    * `JSON` for IoT payloads
    * `Protocol Buffers` (`Protobuf`)
    * CBOR (Concise Binary Object Representation)
    * Schema management and evolution
<!-- chapter: iot-gateways-and-edge-computing, duration: 2h -->
* IoT Gateways and Edge Computing
    * Gateway patterns and roles
    * Edge computing basics
    * Protocol translation at the edge
    * Local processing and filtering
<!-- chapter: device-management-and-iot-platforms, duration: 2h -->
* Device Management and IoT Platforms
    * Device provisioning and lifecycle
    * Over-the-air updates
    * IoT platforms overview (`AWS` IoT, `Azure` IoT Hub, `Google Cloud` IoT)
    * Telemetry and command patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
