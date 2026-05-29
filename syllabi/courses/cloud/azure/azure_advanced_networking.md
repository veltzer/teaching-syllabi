---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - concepts:networking
  - concepts:network-security
  - practices:monitoring
  - practices:automation
level: advanced
category: cloud
audience:
  - audiences:network-engineers
  - audiences:architects
  - audiences:devops
  - audiences:sysadmins
duration_hours: 32
---
<!-- course: azure_advanced_networking -->
# `Azure` Advanced Networking with Labs

## Description
This is a practical, hands-on course for engineers who already know the `Azure`
basics and now need to design, build, secure, and operate production-grade
network infrastructure on `Microsoft Azure`. Almost every chapter is built
around a guided lab in which students provision real resources in their own
`Azure` subscription using the portal, the `Azure CLI`, and
infrastructure-as-code, then break things on purpose and use `Azure` tooling to
diagnose and fix them.

The course covers the full networking stack: `VNet` design and segmentation,
peering and hub-spoke topologies, all `Azure` load balancing options, hybrid
connectivity with `VPN Gateway` and `ExpressRoute`, global routing with
`Azure DNS`, `Azure Front Door` and `Traffic Manager`, network security with
`NSGs`, `Azure Firewall` and `Web Application Firewall`, and finally
observability and troubleshooting with `Network Watcher`, `NSG` flow logs and
`Azure Monitor`.

Although the focus is `Azure`, the networking concepts are deliberately framed
in a vendor-neutral way. Where an `AWS` or `GCP` equivalent exists (for example
`Azure WAF` vs `AWS WAF`, or `ExpressRoute` vs `Direct Connect`) the mapping is
called out so the skills transfer across clouds.

## Duration
32 hours / 4 days

## Intended Audience
* Network engineers moving their skills from on-premises to the `Azure` cloud.
* Cloud and solution architects designing multi-`VNet`, hybrid, and global networks.
* `DevOps` engineers who provision and automate network infrastructure.
* System administrators responsible for connectivity, security, and uptime on `Azure`.

## Prerequisites
* Working knowledge of `Azure` core services (`Virtual Machines`, `Storage`, `Entra ID`, and basic `VNet`).
* `Solid` understanding of `TCP`/`IP`, subnetting/`CIDR`, `DNS`, `HTTP`/`TLS`, and routing.
* Comfort with the `Azure` portal and the `Azure CLI`.
* Each student needs an `Azure` subscription with permission to create networking resources.

## Objectives
* Design and build multi-tier `VNet` topologies with correct subnet and `CIDR` planning.
* Connect networks at scale with `VNet` peering, hub-spoke, and `Virtual WAN`.
* Implement and tune `Azure Load Balancer`, `Application Gateway`, and global traffic distribution.
* Establish and troubleshoot hybrid connectivity with `VPN Gateway` and `ExpressRoute`.
* Secure traffic end to end with `NSGs`, `Azure Firewall`, and `Web Application Firewall`.
* Operate networks confidently using `Network Watcher` and `Azure Monitor`.
* Automate repeatable network builds with Bicep/`Terraform`.

## Exercises
* Every chapter includes a guided lab performed in the student's own `Azure` subscription.
* Labs use the `Azure` portal, the `Azure CLI`, and infrastructure-as-code (Bicep or `Terraform`).
* A recurring "break it and fix it" troubleshooting lab runs through the whole course.
* Students are encouraged to tear down resources after each lab to control cost.

## Outline
<!-- chapter: vnet-design-and-segmentation-lab, duration: 4h -->
* `VNet` Design and Segmentation (Lab)
    * `VNet` address spaces and `CIDR` planning at scale
    * Subnets, subnet delegation, and reserved addresses
    * Public and private `IP` addressing (static and dynamic)
    * User-defined routes and the effective route table
    * `NAT Gateway` for outbound connectivity
    * Lab: build a multi-tier `VNet` with public/private subnets and `NAT Gateway` egress
<!-- chapter: connecting-vnets-at-scale-lab, duration: 4h -->
* Connecting `VNets` at Scale (Lab)
    * Regional and global `VNet` peering
    * Hub-spoke topology and service chaining
    * `Virtual WAN` architecture and hubs
    * Network Virtual Appliances (`NVAs`) and forced tunneling
    * `IP` overlap problems and how to work around them
    * Lab: build a hub-spoke topology with peering and user-defined routes
<!-- chapter: private-link-and-private-endpoints-lab, duration: 3h -->
* `Private Link` and Private Endpoints (Lab)
    * `Private Link` service architecture
    * Private endpoints for `Azure` PaaS services
    * Private endpoints vs service endpoints
    * `DNS` configuration for private endpoints
    * Lab: reach `Azure Storage` privately through a private endpoint with private `DNS`
<!-- chapter: load-balancing-deep-dive-lab, duration: 4h -->
* Load Balancing Deep Dive (Lab)
    * `Azure Load Balancer` standard SKU, public and internal
    * Health probes, backend pools, and load-balancing rules
    * `Application Gateway` with URL/path-based routing
    * `SSL`/`TLS` termination and end-to-end `SSL`
    * Web Application `Firewall` (`WAF`) on `Application Gateway`
    * Lab: deploy `Application Gateway` + `Load Balancer` in front of a VM scale set and test failover
<!-- chapter: dns-and-global-traffic-distribution-lab, duration: 4h -->
* `DNS` and Global Traffic Distribution (Lab)
    * `Azure DNS` public and private zones, record and alias types
    * Private `DNS` zone integration with virtual networks
    * `Azure Front Door`: routing, caching, and `WAF`
    * `Azure Traffic Manager` routing methods and health monitoring
    * Choosing between Front Door, Traffic Manager, and `CDN`
    * Lab: serve a global app via `Front Door` with `Traffic Manager` failover
<!-- chapter: hybrid-connectivity-vpn-and-expressroute-lab, duration: 4h -->
* Hybrid Connectivity: `VPN` and `ExpressRoute` (Lab)
    * `VPN Gateway`: site-to-site and point-to-site
    * Active-active and zone-redundant gateways
    * `IPsec`/`IKE` policy customization
    * `ExpressRoute` circuits, peering types, and Global Reach
    * Redundancy and disaster-recovery patterns
    * Lab: build a `BGP`-routed site-to-site `VPN` to a simulated on-premises gateway
<!-- chapter: network-security-firewall-and-waf-lab, duration: 5h -->
* Network Security: `Firewall` and `WAF` (Lab)
    * `Network Security Groups` and `Application Security Groups`
    * `NSG` rule priority and effective security rules
    * `Azure Firewall` Standard and Premium: network, application, and `NAT` rules
    * `Azure Firewall Manager` and `firewall` policies
    * Web Application `Firewall` policies and `OWASP` top 10
    * Cross-cloud note: how this maps to `AWS WAF` and `GCP Cloud Armor`
    * Lab: deploy a secured `Virtual Hub` with `Azure Firewall` and block an attack
<!-- chapter: network-observability-and-troubleshooting-lab, duration: 4h -->
* Network Observability and Troubleshooting (Lab)
    * `NSG` flow logs and traffic analytics
    * `Network Watcher`: connection troubleshoot, `IP` flow verify, next hop
    * Packet capture and connection monitor
    * `Azure Monitor` network metrics, alerts, and workbooks
    * A systematic method for diagnosing connectivity failures
    * Lab: break a path on purpose and use `Network Watcher` + flow logs to find the fault

## We will not cover
* `Azure` fundamentals and basic `VNet` creation (assumed as a prerequisite).
* Application-level and compute services beyond what the network labs require.
* `AKS` networking internals, which are covered in a dedicated containers course.

## Installations
Each student should have:

* An `Azure` subscription with permissions to create `VNets`, peerings, load
  balancers, `VPN Gateway`/`ExpressRoute` (or simulated) resources, `Azure DNS`
  zones, `Front Door`, `Azure Firewall`, `WAF`, and `Azure Monitor` resources.
* The `Azure CLI` installed and configured with credentials.
* Bicep (or `Terraform`) for the infrastructure-as-code labs.
* A modern web browser for the `Azure` portal.
* Free, wide-band internet access without corporate firewalls blocking `Azure` endpoints.
* Awareness that running labs incurs `Azure` charges; tearing down resources after each lab is recommended.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
