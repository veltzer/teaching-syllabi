---
tags:
  - networking:networking
  - concepts:architecture
level: advanced
category: networking
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
---
<!-- course: software_defined_networking -->
# Software Defined Networking

## Description
Software Defined Networking (SDN) represents a fundamental shift in how networks are designed, built, and operated. By separating the control plane from the data plane, SDN enables programmable, flexible, and centrally managed network infrastructure. This course covers SDN architecture, protocols, controllers, network virtualization, and modern network automation techniques. Students will gain hands-on experience with SDN technologies used in data centers, cloud environments, and enterprise networks.

## Duration
24 hours / 3 days

## Intended Audience
* Network engineers looking to adopt programmable networking
* Software developers building network-aware applications
* System administrators managing cloud and data center networks
* Platform engineers designing container and cloud networking
* Architects evaluating SDN solutions for their organizations

## Prerequisites
* Strong understanding of `TCP`/`IP` networking and routing protocols
* Familiarity with `Linux` networking and command-line tools
* Basic programming experience (`Python` recommended)
* Understanding of virtualization concepts
* Experience with cloud platforms is helpful

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand SDN architecture and the separation of control and data planes
* Work with OpenFlow protocol and SDN controllers
* Design and implement overlay networks using VXLAN, GRE, and Geneve
* Automate network operations using `Ansible`, NETCONF, and YANG
* Understand cloud networking internals across `AWS`, `Azure`, and `GCP`
* Implement container networking with CNI, Calico, and Cilium
* Leverage `eBPF` for high-performance network programming

## Outline
<!-- chapter: sdn-concepts-and-architecture, duration: 2h -->
* SDN Concepts and Architecture
    * Traditional networking limitations
    * SDN definition and principles
    * Control plane vs data plane separation
    * SDN architecture layers: infrastructure, control, application
    * Northbound and southbound APIs
    * Benefits and challenges of SDN adoption
    * SDN history and evolution
<!-- chapter: openflow-protocol, duration: 2h -->
* OpenFlow Protocol
    * OpenFlow architecture and flow tables
    * Match fields and actions
    * OpenFlow message types
    * Flow table pipeline processing
    * Group tables and meter tables
    * OpenFlow versions and evolution
    * OpenFlow switch implementations
<!-- chapter: sdn-controllers, duration: 2h -->
* SDN Controllers
    * Controller role and responsibilities
    * OpenDaylight: architecture, features, and use cases
    * ONOS: distributed controller for service providers
    * Floodlight: lightweight `Java`-based controller
    * Controller clustering and high availability
    * Controller-switch communication
    * Building applications on `top` of controllers
<!-- chapter: network-functions-virtualization-nfv, duration: 2h -->
* Network Functions Virtualization (NFV)
    * NFV concepts and architecture
    * Virtual Network Functions (VNFs)
    * NFV infrastructure (NFVI)
    * Management and orchestration (MANO)
    * NFV use cases: virtual routers, firewalls, load balancers
    * Performance considerations for virtualized network functions
    * Transition from physical to virtual appliances
<!-- chapter: overlay-networks, duration: 2h -->
* Overlay Networks
    * Overlay vs underlay networking
    * VXLAN: encapsulation, VTEP, and flooding
    * GRE tunneling: configuration and use cases
    * Geneve: flexible encapsulation protocol
    * Overlay control planes
    * Multi-tenancy with overlay networks
    * Troubleshooting overlay networks
<!-- chapter: software-defined-wan-sd-wan, duration: 2h -->
* Software-Defined WAN (SD-WAN)
    * SD-WAN architecture and components
    * WAN optimization and traffic steering
    * Application-aware routing
    * SD-WAN security integration
    * SD-WAN orchestration and management
    * Comparing SD-WAN solutions
    * Migration from traditional WAN to SD-WAN
<!-- chapter: network-automation, duration: 2h -->
* Network Automation
    * Infrastructure as code for networking
    * `Ansible` for network automation
    * `Ansible` network modules and playbooks
    * NETCONF protocol and operations
    * YANG data modeling language
    * RESTCONF `API` for network devices
    * gNMI and streaming telemetry
    * Configuration management and compliance
<!-- chapter: cloud-networking, duration: 2h -->
* Cloud Networking
    * `AWS` `VPC` internals: subnets, route tables, security groups, NACLs
    * `AWS` networking services: `Transit Gateway`, PrivateLink, `VPC` peering
    * `Azure` `VNet`: architecture, NSGs, and service endpoints
    * `GCP` `VPC`: global networking, `firewall` rules, and shared `VPC`
    * Multi-cloud networking strategies
    * Cloud network automation with `Terraform`
    * Hybrid cloud connectivity
<!-- chapter: container-networking, duration: 2h -->
* Container Networking
    * Container networking fundamentals
    * Container Network Interface (CNI) specification
    * CNI plugin architecture and lifecycle
    * Calico: `BGP`-based networking and network policy
    * Cilium: `eBPF`-based networking and observability
    * `Kubernetes` networking model and services
    * Network policies and micro-segmentation
    * Service mesh networking: `Istio`, `Linkerd`
<!-- chapter: ebpf-for-networking, duration: 2h -->
* `eBPF` for Networking
    * `eBPF` fundamentals and architecture
    * `eBPF` programs for packet processing
    * XDP (eXpress Data Path) for high-performance packet processing
    * TC (Traffic Control) `eBPF` programs
    * Socket-level `eBPF` programs
    * `eBPF` maps for state management
    * Cilium and `eBPF` in production
    * Observability with `eBPF`
<!-- chapter: service-mesh-networking, duration: 1h -->
* Service Mesh Networking
    * Service mesh architecture and data plane proxies
    * `Envoy` proxy and its networking capabilities
    * Traffic management: routing, load balancing, retries
    * mTLS and service-to-service encryption
    * Observability through the service mesh
    * Service mesh performance considerations
<!-- chapter: network-programmability, duration: 1h -->
* Network Programmability
    * `Python` libraries for network programming (Scapy, Netmiko, NAPALM)
    * Building custom network applications
    * P4 programming language for data plane programming
    * Programmable switches and smart NICs
    * Intent-based networking
    * Network APIs and abstraction layers
<!-- chapter: testing-and-validation, duration: 2h -->
* Testing and Validation
    * Network simulation and emulation (Mininet, GNS3, Containerlab)
    * Network testing frameworks
    * Configuration validation and compliance checking
    * Chaos engineering for networks
    * Performance testing and benchmarking
    * Continuous integration for network changes

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
