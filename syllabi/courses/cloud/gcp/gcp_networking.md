---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
  - concepts:networking
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
---
<!-- course: gcp_networking -->
# `GCP` Networking

## Description
This course provides an in-depth exploration of networking services and architecture on the `Google Cloud Platform`. Participants will learn to design and implement robust network topologies using `VPC` networks, configure load balancing and traffic management, establish hybrid connectivity, and secure workloads with `Cloud Armor` and `firewall` policies. The course covers both foundational networking concepts and advanced patterns for enterprise-scale deployments.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building network-aware applications on `GCP`
* System administrators managing cloud network infrastructure
* Cloud architects designing enterprise networking solutions

## Prerequisites
* Basic understanding of `GCP` core services
* Familiarity with `TCP/IP` networking fundamentals
* Understanding of `DNS`, `HTTP`, and `TLS` concepts
* Experience with command-line tools

## Objectives
* Design and implement `VPC` networks with subnets, routes, and `firewall` rules
* Configure `Shared VPC` and `VPC` peering for multi-project architectures
* Deploy and manage `Cloud Load Balancing` for various traffic patterns
* Establish hybrid connectivity using `Cloud Interconnect` and `Cloud VPN`
* Secure network traffic with `Cloud Armor` and `firewall` policies
* Implement private connectivity with `Private Google Access` and `Private Service Connect`
* Monitor and troubleshoot networks using `Network Intelligence Center`
* Design hybrid and multi-cloud networking patterns

## Outline
<!-- chapter: vpc-deep-dive, duration: 2h -->
* `VPC` Deep Dive
    * `VPC` network architecture and modes (auto vs. custom)
    * Subnets and `IP` address management
    * Secondary `IP` ranges and alias `IPs`
    * Routes and routing tables
    * `Firewall` rules and `firewall` policies
    * Network tags and service accounts for traffic control
<!-- chapter: shared-vpc-and-vpc-peering, duration: 1h -->
* `Shared VPC` and `VPC` Peering
    * `Shared VPC` architecture and use cases
    * Host and service project configuration
    * `VPC` peering setup and limitations
    * Transitive peering considerations
    * Cross-project networking patterns
<!-- chapter: cloud-nat-and-cloud-router, duration: 1h -->
* `Cloud NAT` and `Cloud Router`
    * `Cloud NAT` gateway configuration
    * Static and dynamic `NAT` `IP` allocation
    * `Cloud Router` and `BGP` session management
    * Custom route advertisements
    * Logging and monitoring `NAT` traffic
<!-- chapter: cloud-load-balancing, duration: 2h -->
* `Cloud Load Balancing`
    * Global vs. regional load balancing
    * `HTTP(S)` load balancing with URL maps and backend services
    * `SSL` proxy and `TCP` proxy load balancing
    * Internal `TCP/UDP` load balancing
    * Internal `HTTP(S)` load balancing
    * Health checks and session affinity
    * Traffic management with weighted routing
<!-- chapter: cloud-cdn, duration: 1h -->
* `Cloud CDN`
    * Enabling `Cloud CDN` with load balancers
    * Cache modes and cache keys
    * Signed URLs and signed cookies
    * Cache invalidation strategies
    * Performance monitoring and logging
<!-- chapter: cloud-dns, duration: 1h -->
* `Cloud DNS`
    * Public and private `DNS` zones
    * `DNS` policies and forwarding
    * `DNSSEC` configuration
    * Cross-project `DNS` peering
    * Split-horizon `DNS` patterns
<!-- chapter: cloud-interconnect, duration: 2h -->
* `Cloud Interconnect`
    * `Dedicated Interconnect` setup and provisioning
    * `Partner Interconnect` configuration
    * `VLAN` attachments and `BGP` sessions
    * Redundancy and high availability designs
    * Capacity planning and monitoring
<!-- chapter: cloud-vpn, duration: 2h -->
* `Cloud VPN`
    * `HA VPN` architecture and configuration
    * Classic `VPN` tunnels
    * `IKEv2` and routing options
    * `VPN` with `Cloud Router` for dynamic routing
    * Multi-tunnel and multi-gateway designs
<!-- chapter: network-intelligence-center, duration: 2h -->
* `Network Intelligence Center`
    * Network topology visualization
    * Connectivity tests
    * Performance dashboard
    * `Firewall` insights
    * Network Analyzer recommendations
<!-- chapter: packet-mirroring, duration: 1h -->
* `Packet Mirroring`
    * Configuring packet mirroring policies
    * Mirrored traffic collection and analysis
    * Integration with third-party security tools
    * Filtering and scoping mirrored traffic
<!-- chapter: private-google-access-and-private-service-connect, duration: 2h -->
* `Private Google Access` and `Private Service Connect`
    * `Private Google Access` for on-premises and `VPC`
    * `Private Service Connect` endpoints
    * Publishing and consuming services privately
    * `DNS` configuration for private access
    * Service Directory integration
<!-- chapter: cloud-armor, duration: 2h -->
* `Cloud Armor`
    * Web Application `Firewall` (`WAF`) rules
    * `DDoS` protection and adaptive protection
    * Pre-configured `WAF` rules and `OWASP` `top` 10
    * Rate limiting and bot management
    * Security policy configuration and tuning
<!-- chapter: network-service-tiers, duration: 1h -->
* Network Service Tiers
    * Premium vs. Standard tier networking
    * Performance and cost trade-offs
    * Configuring service tiers per resource
    * Global vs. regional routing implications
<!-- chapter: traffic-director-and-service-mesh, duration: 2h -->
* `Traffic Director` and Service Mesh
    * `Traffic Director` architecture and concepts
    * `Envoy` proxy integration
    * Traffic management policies
    * Health checking and outlier detection
    * Service mesh with `Anthos Service Mesh`
<!-- chapter: hybrid-networking-patterns, duration: 2h -->
* Hybrid Networking Patterns
    * Hub-and-spoke network topologies
    * Multi-region networking designs
    * Hybrid connectivity with on-premises data centers
    * Multi-cloud networking strategies
    * Network segmentation and micro-segmentation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
