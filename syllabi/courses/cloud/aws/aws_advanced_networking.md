---
tags:
  - infrastructure:aws
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
<!-- course: aws_advanced_networking -->
# `AWS` Advanced Networking with Labs

## Description
This is a practical, hands-on course for engineers who already know the `AWS`
basics and now need to design, build, secure, and operate production-grade
network infrastructure on `AWS`. Almost every chapter is built around a guided
lab in which students provision real resources in their own `AWS` account using
the console, the `CLI`, and infrastructure-as-code, then break things on
purpose and use `AWS` tooling to diagnose and fix them.

The course covers the full networking stack: `VPC` design and segmentation,
all flavours of `Elastic Load Balancing`, hybrid connectivity with
`Site-to-Site VPN` and `Direct Connect`, edge and global routing with
`Route 53`, `CloudFront` and `Global Accelerator`, network security with
security groups, `NACLs`, `AWS Network Firewall`, `WAF` and `AWS Shield`, and
finally observability and troubleshooting with flow logs,
`Reachability Analyzer` and `CloudWatch`.

Although the focus is `AWS`, the networking concepts are deliberately framed in a
vendor-neutral way. Where a `GCP` or `Azure` equivalent exists (for example
`Cloud Armor` vs `AWS WAF`, or `Cloud Interconnect` vs `Direct Connect`) the
mapping is called out so the skills transfer across clouds.

## Duration
32 hours / 4 days

## Intended Audience
* Network engineers moving their skills from on-premises to the `AWS` cloud.
* Cloud and solution architects designing multi-`VPC`, hybrid, and global networks.
* `DevOps` engineers who provision and automate network infrastructure.
* System administrators responsible for connectivity, security, and uptime on `AWS`.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `IAM`, and basic `VPC`).
* `Solid` understanding of `TCP`/`IP`, subnetting/`CIDR`, `DNS`, `HTTP`/`TLS`, and routing.
* Comfort with the `AWS` Management Console and the `AWS CLI`.
* Each student needs an `AWS` account with permission to create networking resources.

## Objectives
* Design and build multi-tier, multi-`VPC` topologies with correct `CIDR` planning and routing.
* Connect `VPCs` at scale with peering, `Transit Gateway`, `PrivateLink`, and `RAM`.
* Implement and tune all `Elastic Load Balancing` types and `Route 53` routing policies.
* Establish and troubleshoot hybrid connectivity with `Site-to-Site VPN` and `Direct Connect`.
* Secure traffic end to end with security groups, `NACLs`, `Network Firewall`, `WAF`, and `Shield`.
* Operate networks confidently using flow logs, `Reachability Analyzer`, and `CloudWatch`.
* Automate repeatable network builds with `CloudFormation`/`Terraform`.

## Exercises
* Every chapter includes a guided lab performed in the student's own `AWS` account.
* Labs use the `AWS` console, the `AWS CLI`, and infrastructure-as-code (`CloudFormation` or `Terraform`).
* A recurring "break it and fix it" troubleshooting lab runs through the whole course.
* Students are encouraged to tear down resources after each lab to control cost.

## Outline
<!-- chapter: vpc-design-and-segmentation-lab, duration: 4h -->
* `VPC` Design and Segmentation (Lab)
    * `CIDR` planning and `IP` address management at scale
    * Public, private, and isolated subnets across Availability Zones
    * Route tables, the implicit router, and routing precedence
    * Internet Gateway, `NAT Gateway` and `NAT` instance, egress-only Gateway for `IPv6`
    * Dual-stack `IPv4`/`IPv6` `VPC` design
    * Lab: build a three-tier, multi-`AZ` `VPC` with public/private/isolated subnets and working egress
<!-- chapter: connecting-vpcs-at-scale-lab, duration: 4h -->
* Connecting `VPCs` at Scale (Lab)
    * `VPC` peering and its non-transitive limitation
    * `AWS Transit Gateway` architecture, route tables, and associations
    * Inter-region peering and centralized egress
    * `Resource Access Manager` (`RAM`) for multi-account sharing
    * `IP` overlap problems and how to work around them
    * Lab: connect three `VPCs` through a `Transit Gateway` with segmented routing
<!-- chapter: private-connectivity-with-endpoints-and-privatelink-lab, duration: 3h -->
* Private Connectivity with Endpoints and `PrivateLink` (Lab)
    * Gateway endpoints for `S3` and `DynamoDB`
    * Interface endpoints and `AWS PrivateLink`
    * Endpoint policies and access control
    * Publishing a custom endpoint service for other accounts
    * Lab: reach `S3` and a private service with no traffic leaving the `AWS` network
<!-- chapter: elastic-load-balancing-deep-dive-lab, duration: 4h -->
* `Elastic Load Balancing` Deep Dive (Lab)
    * Application Load Balancer: listeners, rules, path/host routing
    * Network Load Balancer: static `IPs`, `TLS` passthrough, ultra-low latency
    * Gateway Load Balancer for inline security appliances
    * Target groups, health checks, and connection draining
    * `TLS` termination, `SNI`, and cross-zone load balancing
    * Lab: deploy `ALB` + `NLB` in front of `Auto Scaling` targets and test failover
<!-- chapter: dns-and-global-edge-routing-lab, duration: 4h -->
* `DNS` and Global Edge Routing (Lab)
    * `Route 53` hosted zones, record types, and alias records
    * Routing policies: weighted, latency, failover, geolocation, geo-proximity
    * Health checks and `DNS` failover
    * `Route 53 Resolver` for hybrid `DNS`
    * `CloudFront` distributions, cache behaviors, and `Origin Access Control`
    * `AWS Global Accelerator` and when to choose it over `CloudFront`
    * Lab: serve a global app via `CloudFront` with latency-based `Route 53` failover
<!-- chapter: hybrid-connectivity-vpn-and-direct-connect-lab, duration: 4h -->
* Hybrid Connectivity: `VPN` and `Direct Connect` (Lab)
    * `Site-to-Site VPN`: tunnels, `IKEv2`, static vs `BGP` routing
    * `AWS Client VPN` for remote users
    * `Direct Connect` connection types and virtual interfaces (private/public/transit)
    * `Direct Connect Gateway` and `Transit Gateway` integration
    * Redundancy, accelerated `VPN`, and resiliency patterns
    * Lab: build a `BGP`-routed `Site-to-Site VPN` to a simulated on-premises gateway
<!-- chapter: network-security-firewall-waf-and-shield-lab, duration: 5h -->
* Network Security: `Firewall`, `WAF`, and `Shield` (Lab)
    * Security groups vs network `ACLs`: stateful vs stateless, layered defense
    * `AWS Network Firewall`: stateless/stateful rule groups and domain filtering
    * Centralized inspection with `Transit Gateway` and `Network Firewall`
    * `AWS WAF`: managed rule groups, `OWASP` top 10, rate limiting, bot control
    * `AWS Shield` Standard and Advanced for `DDoS` protection
    * Cross-cloud note: how this maps to `GCP Cloud Armor` and `Azure WAF`
    * Lab: deploy a `WAF` web `ACL` and a centralized `Network Firewall`, then block an attack
<!-- chapter: network-observability-and-troubleshooting-lab, duration: 4h -->
* Network Observability and Troubleshooting (Lab)
    * `VPC` flow logs: capture, formats, and analysis
    * `VPC Reachability Analyzer` and `Network Access Analyzer`
    * Traffic mirroring for packet-level inspection
    * `CloudWatch` network metrics, alarms, and dashboards
    * A systematic method for diagnosing connectivity failures
    * Lab: break a path on purpose and use `Reachability Analyzer` + flow logs to find the fault

## We will not cover
* `AWS` fundamentals and basic `VPC` creation (assumed as a prerequisite).
* Application-level and compute services beyond what the network labs require.
* `Kubernetes` (`EKS`) networking internals, which are covered in a dedicated containers course.

## Installations
Each student should have:

* An `AWS` account with `IAM` permissions to create `VPCs`, `Transit Gateways`,
  load balancers, `VPN`/`Direct Connect` (or simulated) resources, `Route 53`
  zones, `CloudFront`, `WAF`, `Network Firewall`, and `CloudWatch` resources.
* The `AWS CLI` v2 installed and configured with credentials.
* `Terraform` (or familiarity with `CloudFormation`) for the infrastructure-as-code labs.
* A modern web browser for the `AWS` Management Console.
* Free, wide-band internet access without corporate firewalls blocking `AWS` endpoints.
* Awareness that running labs incurs `AWS` charges; tearing down resources after each lab is recommended.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
