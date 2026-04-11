---
tags:
  - infrastructure:linux
  - hardware-and-embedded:embedded
  - networking:networking
  - networking:tcp-ip
level: advanced
category: embedded
duration_hours: 16
audience:
  - audiences:embedded-engineers
  - audiences:firmware-developers
  - audiences:developers
---
<!-- course: embedded_linux_networking -->
# Embedded `Linux` Networking

## Description
This advanced course covers networking on embedded `Linux` platforms, from the kernel network stack to lightweight application-layer protocols. Participants will learn how to configure, optimize, and debug network connectivity on resource-constrained `Linux` devices, including working with lightweight `TCP`/`IP` stacks, embedded web servers, and IoT-specific protocols such as `CoAP` and mDNS/`DNS`-SD.

## Duration
16 hours / 2 days

## Intended Audience
* Embedded engineers building networked `Linux` devices.
* Firmware developers integrating network capabilities into embedded platforms.
* Developers working on IoT and connected device software.

## Prerequisites
* `Solid` understanding of networking fundamentals (`TCP`/`IP`, sockets).
* Experience with embedded systems development.

## Required Knowledge
* `Linux` Fundamentals
* `C` Programming

## Objectives
* Understand the `Linux` kernel network stack on embedded platforms.
* Implement socket-based communication for embedded applications.
* Configure and deploy lightweight embedded web servers.
* Work with IoT-specific protocols including `CoAP` and mDNS/`DNS`-SD.
* Configure and troubleshoot `Ethernet` and `WiFi` drivers on embedded targets.
* Debug network issues on constrained devices.

## Outline
<!-- chapter: linux-network-stack-on-embedded, duration: 2h -->
* `Linux` Network Stack on Embedded
    * Kernel networking subsystem overview
    * Network device drivers architecture
    * Lightweight `TCP`/`IP` stack alternatives
    * Network namespaces and isolation
    * Memory and performance considerations
<!-- chapter: socket-programming-for-embedded, duration: 2h -->
* Socket Programming for Embedded
    * Socket `API` on embedded `Linux`
    * `TCP` and `UDP` socket programming
    * Non-blocking `I/O` and event-driven networking
    * Socket options for constrained environments
    * Raw sockets and packet processing
<!-- chapter: service-discovery-and-iot-protocols, duration: 2h -->
* Service Discovery and IoT Protocols
    * mDNS and `DNS`-SD (Avahi)
    * `CoAP` protocol and `libcoap`
    * Lightweight messaging protocols
    * Protocol selection for embedded use cases
<!-- chapter: embedded-web-servers, duration: 2h -->
* Embedded Web Servers
    * lighttpd configuration and deployment
    * uhttpd for OpenWrt-based systems
    * `RESTful APIs` on embedded devices
    * Security considerations for embedded `web services`
    * `WebSocket` support on constrained devices
<!-- chapter: network-configuration, duration: 2h -->
* Network Configuration
    * `NetworkManager` on embedded platforms
    * `systemd`-networkd configuration
    * Static and dynamic `IP` configuration
    * `VLAN` and bridge configuration
    * Network bonding and failover
<!-- chapter: ethernet-and-wifi-drivers, duration: 2h -->
* `Ethernet` and `WiFi` Drivers
    * `Ethernet` PHY and MAC drivers
    * `WiFi` driver architecture (cfg80211, mac80211)
    * `WiFi` configuration with wpa_supplicant
    * Access point mode on embedded devices
    * Driver debugging and performance tuning
<!-- chapter: firewall-and-security, duration: 2h -->
* `Firewall` and Security
    * `iptables` and `nftables` on embedded
    * Minimal `firewall` configurations
    * `TLS` on constrained devices
    * Secure boot and network authentication
<!-- chapter: network-debugging-on-constrained-devices, duration: 2h -->
* Network Debugging on Constrained Devices
    * `tcpdump` on embedded targets
    * Remote packet capture
    * Network performance profiling
    * Common embedded networking issues and solutions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
