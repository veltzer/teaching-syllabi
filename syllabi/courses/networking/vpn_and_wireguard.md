---
tags:
  - networking:vpn
  - networking:security
  - protocols:wireguard
  - protocols:ipsec
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:network-engineers
  - audiences:security-engineers
---
<!-- course: vpn_and_wireguard -->
# `VPN` and `WireGuard`

## Description
Virtual Private Networks are a cornerstone of secure remote access, site-to-site connectivity, and network segmentation, enabling organizations to extend trusted network boundaries across untrusted infrastructure. This course covers the full landscape of modern `VPN` technologies, from the classical `IPSec`/`IKEv2` suite used in enterprise and carrier-grade deployments to `OpenVPN` and the next-generation `WireGuard` protocol. `WireGuard` in particular has revolutionized `VPN` design with its minimal codebase, modern cryptography, and dramatically simplified configuration model. Participants will gain both theoretical understanding and hands-on skills to deploy, configure, and troubleshoot `VPN` solutions for remote access, site-to-site connectivity, and containerized environments.

## Duration
16 hours / 2 days

## Intended Audience
* System administrators and `DevOps` engineers who need to deploy and operate `VPN` infrastructure for secure remote access or multi-site connectivity.
* Network engineers evaluating and implementing `VPN` solutions for enterprise and cloud environments.
* Security engineers assessing `VPN` architectures and ensuring cryptographic hygiene in network connectivity.

## Prerequisites
* Strong understanding of `TCP/IP` networking: routing, subnetting, and `NAT`.
* `Linux` system administration proficiency, including `iptables`/`nftables` and network interface management.
* Basic understanding of public key cryptography and symmetric encryption.
* Familiarity with `Docker` or `Kubernetes` is useful for the container networking sections.

## Required Knowledge
* `TCP/IP` networking and routing fundamentals
* `Linux` networking and system administration

## Objectives
* Compare `VPN` technologies and select the appropriate solution for a given use case
* Understand `IPSec` architecture including `IKEv2`, ESP, `AH`, and Security Associations
* Configure `StrongSwan` or `Libreswan` for `IPSec`/`IKEv2` tunnels
* Deploy and configure `OpenVPN` for client-server remote access
* Explain `WireGuard`'s design principles, cryptographic model, and routing approach
* Install and configure `WireGuard` peers for road-warrior and site-to-site use cases
* Implement split tunneling and policy-based routing with `VPN` interfaces
* Design and deploy site-to-site `VPN` topologies
* Monitor `VPN` health and diagnose connectivity and performance issues

## Outline
<!-- chapter: introduction-to-vpn-technologies, duration: 1h -->
* Introduction to `VPN` Technologies
    * What `VPN`s solve: confidentiality, integrity, and tunnel abstraction
    * `VPN` modes: remote access, site-to-site, and overlay networks
    * Overview of major `VPN` protocols: `IPSec`, `OpenVPN`, `WireGuard`, `SSL VPN`
    * Layer 2 vs Layer 3 `VPN`s: MPLS, `VXLAN`, and `IP` tunnels
    * Performance and security trade-off overview
    * Common use cases: remote workforce, branch offices, cloud connectivity
<!-- chapter: ipsec-architecture-and-ikev2, duration: 3h -->
* `IPSec` Architecture and `IKEv2`
    * `IPSec` protocol suite: AH, `ESP`, and their roles
    * Transport mode vs tunnel mode
    * Security Associations (SA) and the Security Policy Database (SPD)
    * `IKE` evolution: `IKEv1` vs `IKEv2`
    * `IKEv2` phase 1 and phase 2 exchange (IKE_SA_INIT, IKE_AUTH, CREATE_CHILD_SA)
    * Authentication methods: pre-shared keys, certificates, and `EAP`
    * Cipher suites: encryption, integrity, and `DH` groups
    * Configuring `StrongSwan` for `IKEv2` road-warrior remote access
    * `IPSec` in cloud environments: `AWS` `VPN` and `Azure` `VPN` Gateway
    * Troubleshooting `IKEv2` negotiations with `tcpdump` and logs
<!-- chapter: openvpn-deep-dive, duration: 2h -->
* `OpenVPN` Deep Dive
    * `OpenVPN` architecture: TUN/`TAP` interfaces and control/data channels
    * `TLS` for control channel security and session establishment
    * Certificate-based authentication with a custom `PKI`
    * Username and password authentication with `PAM` and `LDAP`
    * `OpenVPN` server configuration: topology, cipher, and protocol
    * Client profile distribution and `ovpn` file structure
    * `OpenVPN` with `obfs4` and traffic obfuscation
    * Scalability: `OpenVPN` Access Server and multi-daemon setups
<!-- chapter: wireguard-architecture-and-design, duration: 2h -->
* `WireGuard` Architecture and Design
    * `WireGuard` design philosophy: simplicity and minimal attack surface
    * `WireGuard` in the `Linux` kernel vs userspace implementations
    * The `WireGuard` cryptographic model: `Noise_IKpsk2` protocol
    * Key pairs: public and private keys, and preshared keys
    * `WireGuard` peers and the AllowedIPs routing model
    * Connection initiation and cryptographic handshake
    * Roaming support and how `WireGuard` handles changing endpoints
    * Comparing `WireGuard` to `IPSec` and `OpenVPN`: code size, performance, and ease of use
<!-- chapter: wireguard-setup-and-configuration, duration: 3h -->
* `WireGuard` Setup and Configuration
    * Installing `WireGuard` on `Linux`, `macOS`, `Windows`, `iOS`, and `Android`
    * Generating key pairs and distributing public keys
    * `wg` and `wg-quick` tools and configuration file format
    * Road-warrior configuration: server and client setup
    * Full tunnel vs split tunnel in `WireGuard`
    * `PostUp`/PostDown hooks and `iptables` masquerading
    * `systemd-networkd` integration for persistent `WireGuard` interfaces
    * Multi-peer configuration for mesh networking
    * `wg-easy` and `wireguard-ui` for simplified management
<!-- chapter: split-tunneling-and-routing, duration: 2h -->
* Split Tunneling and Routing
    * How `WireGuard` AllowedIPs implements routing decisions
    * Full tunnel configuration: routing all traffic through the `VPN`
    * Split tunnel configuration: routing only specific subnets
    * Policy-based routing with `ip rule` and `ip route`
    * `DNS` leak prevention in split tunnel mode
    * `WireGuard` and container networking: `Docker` and `Kubernetes` integration
    * Routing internet traffic through a `VPN` exit node
<!-- chapter: site-to-site-vpns, duration: 2h -->
* Site-to-Site `VPN`s
    * `Design patterns` for site-to-site connectivity: hub-and-spoke, full mesh
    * `WireGuard` site-to-site tunnel between two `Linux` gateways
    * `IPSec` site-to-site with `StrongSwan` and certificate-based authentication
    * Overlapping subnet handling with `NAT` over `VPN`
    * Dynamic routing over `VPN` tunnels with `BGP` and `OSPF`
    * High availability: failover between redundant `VPN` endpoints
    * Cloud provider `VPN` interoperability: `AWS`, `Azure`, `GCP`
<!-- chapter: vpn-monitoring-and-troubleshooting, duration: 1h -->
* `VPN` Monitoring and Troubleshooting
    * Monitoring `WireGuard` peers: `wg show` and latest handshake timestamps
    * `IPSec` SA inspection with `ip xfrm`
    * Capturing `VPN` traffic with `tcpdump` and `Wireshark`
    * Common connectivity issues: `NAT` traversal, `firewall` rules, and MTU problems
    * MTU and `MSS` clamping for fragmentation prevention
    * Exporting `VPN` metrics to `Prometheus` and `Grafana`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
