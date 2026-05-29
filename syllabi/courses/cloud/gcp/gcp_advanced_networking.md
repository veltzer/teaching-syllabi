---
tags:
  - infrastructure:gcp
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
<!-- course: gcp_advanced_networking -->
# `GCP` Advanced Networking with Labs

## Description
This is a practical, hands-on course for engineers who already know the `GCP`
basics and now need to design, build, secure, and operate production-grade
network infrastructure on the `Google Cloud Platform`. Almost every chapter is
built around a guided lab in which students provision real resources in their
own `GCP` project using the console, the `gcloud CLI`, and
infrastructure-as-code, then break things on purpose and use `GCP` tooling to
diagnose and fix them.

The course covers the full networking stack: `VPC` design and segmentation,
`Shared VPC` and peering, `Cloud Load Balancing` in all its forms, hybrid
connectivity with `Cloud VPN` and `Cloud Interconnect`, edge and global routing
with `Cloud DNS` and `Cloud CDN`, network security with `firewall` policies,
`Cloud Armor` and `Cloud NGFW`, and finally observability and troubleshooting
with `Network Intelligence Center`, `VPC Flow Logs` and `Cloud Monitoring`.

Although the focus is `GCP`, the networking concepts are deliberately framed in a
vendor-neutral way. Where an `AWS` or `Azure` equivalent exists (for example
`Cloud Armor` vs `AWS WAF`, or `Cloud Interconnect` vs `Direct Connect`) the
mapping is called out so the skills transfer across clouds.

## Duration
32 hours / 4 days

## Intended Audience
* Network engineers moving their skills from on-premises to the `GCP` cloud.
* Cloud and solution architects designing multi-`VPC`, hybrid, and global networks.
* `DevOps` engineers who provision and automate network infrastructure.
* System administrators responsible for connectivity, security, and uptime on `GCP`.

## Prerequisites
* Working knowledge of `GCP` core services (`Compute Engine`, `Cloud Storage`, `IAM`, and basic `VPC`).
* `Solid` understanding of `TCP`/`IP`, subnetting/`CIDR`, `DNS`, `HTTP`/`TLS`, and routing.
* Comfort with the `Google Cloud Console` and the `gcloud CLI`.
* Each student needs a `GCP` project with permission to create networking resources.

## Objectives
* Design and build multi-tier `VPC` topologies with correct subnet and `CIDR` planning.
* Connect networks at scale with `Shared VPC`, `VPC` peering, and `Private Service Connect`.
* Implement and tune every `Cloud Load Balancing` type and `Cloud DNS` routing policy.
* Establish and troubleshoot hybrid connectivity with `Cloud VPN` and `Cloud Interconnect`.
* Secure traffic end to end with `firewall` policies, `Cloud Armor`, and `Cloud NGFW`.
* Operate networks confidently using `Network Intelligence Center` and `VPC Flow Logs`.
* Automate repeatable network builds with `Terraform`/`Deployment Manager`.

## Exercises
* Every chapter includes a guided lab performed in the student's own `GCP` project.
* Labs use the `Google Cloud Console`, the `gcloud CLI`, and infrastructure-as-code (`Terraform`).
* A recurring "break it and fix it" troubleshooting lab runs through the whole course.
* Students are encouraged to tear down resources after each lab to control cost.

## Outline
<!-- chapter: vpc-design-and-segmentation-lab, duration: 4h -->
* `VPC` Design and Segmentation (Lab)
    * Auto mode vs custom mode `VPC` networks
    * Subnets, regions, and `CIDR` planning at scale
    * Secondary `IP` ranges and alias `IPs` for `GKE`
    * Routes, the implicit router, and routing precedence
    * `Cloud NAT` and `Cloud Router` for egress
    * Lab: build a custom-mode multi-region `VPC` with public/private subnets and `Cloud NAT` egress
<!-- chapter: connecting-networks-at-scale-lab, duration: 4h -->
* Connecting Networks at Scale (Lab)
    * `Shared VPC` host and service projects
    * `VPC` peering and its non-transitive limitation
    * Cross-project and cross-organization patterns
    * `Network Connectivity Center` as a hub
    * `IP` overlap problems and how to work around them
    * Lab: wire a host project and two service projects together with `Shared VPC`
<!-- chapter: private-connectivity-with-private-service-connect-lab, duration: 3h -->
* Private Connectivity with `Private Service Connect` (Lab)
    * `Private Google Access` for on-premises and `VPC`
    * `Private Service Connect` endpoints and backends
    * Publishing and consuming services privately
    * `DNS` configuration and `Service Directory` integration
    * Lab: reach a `Google` `API` and a private service with no public `IP`
<!-- chapter: cloud-load-balancing-deep-dive-lab, duration: 4h -->
* `Cloud Load Balancing` Deep Dive (Lab)
    * Global external Application Load Balancer with URL maps and backend services
    * Regional external and internal Application Load Balancers
    * Proxy and passthrough Network Load Balancers
    * Health checks, session affinity, and backend services
    * `SSL`/`TLS` termination, `SSL` policies, and `SNI`
    * Lab: deploy a global Application Load Balancer in front of managed instance groups and test failover
<!-- chapter: cloud-dns-and-cloud-cdn-lab, duration: 4h -->
* `Cloud DNS` and `Cloud CDN` (Lab)
    * `Cloud DNS` public and private zones, record types
    * `DNS` policies, forwarding, and peering
    * `DNSSEC` configuration and split-horizon `DNS`
    * `Cloud CDN` cache modes, cache keys, and invalidation
    * Signed URLs and signed cookies
    * Lab: serve a global app via `Cloud CDN` with private and public `Cloud DNS` zones
<!-- chapter: hybrid-connectivity-vpn-and-interconnect-lab, duration: 4h -->
* Hybrid Connectivity: `VPN` and `Interconnect` (Lab)
    * `HA VPN` architecture and `Classic VPN` tunnels
    * `IKEv2`, static vs `BGP` routing with `Cloud Router`
    * `Dedicated Interconnect` and `Partner Interconnect`
    * `VLAN` attachments and `BGP` sessions
    * Redundancy and high-availability designs
    * Lab: build a `BGP`-routed `HA VPN` to a simulated on-premises gateway
<!-- chapter: network-security-firewall-armor-and-ngfw-lab, duration: 5h -->
* Network Security: `Firewall`, `Cloud Armor`, and `NGFW` (Lab)
    * `Firewall` rules vs hierarchical `firewall` policies
    * Network tags and service accounts for traffic control
    * `Cloud NGFW` and intrusion prevention
    * `Cloud Armor`: `WAF` rules, `OWASP` top 10, rate limiting, bot management
    * `Cloud Armor` adaptive protection and `DDoS` defense
    * Cross-cloud note: how this maps to `AWS WAF` and `Azure WAF`
    * Lab: attach a `Cloud Armor` policy to a load balancer and block an attack
<!-- chapter: network-observability-and-troubleshooting-lab, duration: 4h -->
* Network Observability and Troubleshooting (Lab)
    * `VPC Flow Logs`: capture, formats, and analysis
    * `Network Intelligence Center`: topology, connectivity tests, `firewall` insights
    * `Packet Mirroring` for packet-level inspection
    * `Cloud Monitoring` network metrics, alerts, and dashboards
    * A systematic method for diagnosing connectivity failures
    * Lab: break a path on purpose and use connectivity tests + flow logs to find the fault

## We will not cover
* `GCP` fundamentals and basic `VPC` creation (assumed as a prerequisite).
* Application-level and compute services beyond what the network labs require.
* `GKE` networking internals, which are covered in a dedicated containers course.

## Installations
Each student should have:

* A `GCP` project with `IAM` permissions to create `VPC` networks, `Shared VPC`,
  load balancers, `Cloud VPN`/`Interconnect` (or simulated) resources, `Cloud DNS`
  zones, `Cloud CDN`, `Cloud Armor`, `Cloud NGFW`, and `Cloud Monitoring` resources.
* The `gcloud CLI` installed and configured with credentials.
* `Terraform` (or familiarity with `Deployment Manager`) for the infrastructure-as-code labs.
* A modern web browser for the `Google Cloud Console`.
* Free, wide-band internet access without corporate firewalls blocking `GCP` endpoints.
* Awareness that running labs incurs `GCP` charges; tearing down resources after each lab is recommended.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
