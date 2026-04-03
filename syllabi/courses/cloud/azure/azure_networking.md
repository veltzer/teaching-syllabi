---
tags:
  - infrastructure:azure
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
<!-- course: azure_networking -->
# `Azure` Networking

## Description
This course provides an in-depth exploration of networking in `Microsoft Azure`. Participants will learn how to design, implement, and manage virtual networks, load balancers, firewalls, `VPN` connections, and hybrid networking solutions. The course covers both foundational networking concepts and advanced topics such as `Azure Virtual WAN`, `ExpressRoute`, and network security patterns, enabling participants to build robust and secure network architectures on `Azure`.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building networked applications on `Azure`
* System administrators managing `Azure` network infrastructure
* Architects designing enterprise network topologies on `Azure`

## Prerequisites
* Basic understanding of `Azure` services and the `Azure` portal
* `Solid` understanding of networking fundamentals (OSI model, `TCP`/`IP`, `DNS`, routing)
* Familiarity with on-premises networking concepts (firewalls, VPNs, load balancers)

## Objectives
* Design and implement `Azure` virtual networks with proper segmentation
* Configure network security using `NSGs`, `Azure Firewall`, and `Application Security Groups`
* Implement load balancing and traffic distribution solutions
* Set up hybrid connectivity using `VPN Gateway` and `ExpressRoute`
* Secure network access with `Private Link`, private endpoints, and `Azure Bastion`
* Monitor and troubleshoot network issues using `Network Watcher`

## Outline
<!-- chapter: virtual-networks-deep-dive, duration: 2h -->
* Virtual Networks Deep Dive
    * `VNet` address spaces and planning
    * Subnets and subnet delegation
    * `IP` addressing (public, private, static, dynamic)
    * `IPv6` support on `Azure`
    * `DNS` resolution in virtual networks
    * Service endpoints and their use cases
<!-- chapter: network-security-groups-and-application-security-groups, duration: 1h -->
* `Network Security Groups` and `Application Security Groups`
    * `NSG` rules and priority evaluation
    * Inbound and outbound rule design
    * `Application Security Groups` for logical grouping
    * `NSG` flow logs and analysis
    * Effective security rules troubleshooting
<!-- chapter: azure-firewall-and-firewall-manager, duration: 2h -->
* `Azure Firewall` and `Firewall Manager`
    * `Azure Firewall` Standard and Premium
    * Network rules, application rules, and `NAT` rules
    * Threat intelligence-based filtering
    * `Azure Firewall Manager` and `firewall` policies
    * Centralized `firewall` management across subscriptions
<!-- chapter: load-balancing-solutions, duration: 2h -->
* Load Balancing Solutions
    * `Azure Load Balancer` (basic and standard SKUs)
    * Internal vs. public load balancers
    * Health probes and backend pools
    * `Application Gateway` and `Web Application Firewall` (`WAF`)
    * URL-based and path-based routing
    * `SSL` termination and end-to-end `SSL`
<!-- chapter: global-traffic-distribution, duration: 1h -->
* Global Traffic Distribution
    * `Azure Front Door` (routing, caching, `WAF`)
    * `Azure CDN` profiles and endpoints
    * `Azure Traffic Manager` (routing methods and health monitoring)
    * Choosing between Front Door, Traffic Manager, and CDN
<!-- chapter: azure-dns, duration: 1h -->
* `Azure DNS`
    * Public and private `DNS` zones
    * Record types and alias records
    * `DNS` delegation and custom domains
    * Private `DNS` zone integration with virtual networks
<!-- chapter: vpn-gateway, duration: 2h -->
* `VPN Gateway`
    * Site-to-site `VPN` configuration
    * Point-to-site `VPN` for remote access
    * `VPN` Gateway SKUs and performance
    * Active-active and zone-redundant gateways
    * `IPsec`/`IKE` policy customization
<!-- chapter: azure-expressroute, duration: 2h -->
* `Azure ExpressRoute`
    * `ExpressRoute` circuit provisioning
    * Peering types (private, Microsoft)
    * `ExpressRoute` Global Reach
    * `ExpressRoute` Direct
    * Redundancy and disaster recovery
<!-- chapter: virtual-wan, duration: 2h -->
* `Virtual WAN`
    * Virtual WAN architecture and hubs
    * Branch connectivity and automation
    * Hub-to-hub communication
    * Integration with `VPN Gateway` and `ExpressRoute`
    * Secured Virtual Hub with `Azure Firewall`
<!-- chapter: vnet-peering-and-service-chaining, duration: 2h -->
* `VNet` Peering and Service Chaining
    * Regional and global `VNet` peering
    * Peering properties and limitations
    * Hub-spoke network topology
    * User-defined routes and service chaining
    * Network Virtual Appliances (NVAs)
<!-- chapter: private-link-and-private-endpoints, duration: 2h -->
* `Private Link` and Private Endpoints
    * `Private Link` service architecture
    * Private endpoints for `Azure` PaaS services
    * `DNS` configuration for private endpoints
    * Approving and managing private endpoint connections
    * Private endpoints vs. service endpoints
<!-- chapter: azure-bastion, duration: 1h -->
* `Azure Bastion`
    * Secure RDP and `SSH` access without public `IPs`
    * Bastion SKUs and features
    * Native client support
    * Bastion deployment architecture
<!-- chapter: network-watcher-and-diagnostics, duration: 2h -->
* `Network Watcher` and Diagnostics
    * Connection troubleshoot and `IP` flow verify
    * Next hop and effective routes analysis
    * Packet capture
    * `VPN` diagnostics
    * Connection monitor and topology view
<!-- chapter: hybrid-networking-patterns, duration: 2h -->
* Hybrid Networking Patterns
    * Hub-spoke topology design
    * Transit connectivity patterns
    * Network segmentation strategies
    * Multi-region network design
    * On-premises to `Azure` migration networking

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
