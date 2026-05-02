---
tags:
  - infrastructure:aws
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
<!-- course: aws_networking -->
# `AWS` Advanced Networking

## Description
This course provides an in-depth exploration of networking services and architectures on `AWS`. Students will learn how to design, implement, and troubleshoot complex network topologies including multi-`VPC`, hybrid, and global architectures. The course covers core networking primitives, advanced routing and load balancing, edge networking, and network security to prepare students for building production-grade network infrastructure on `AWS`.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building distributed applications that require advanced networking on `AWS`.
* System administrators responsible for `AWS` network infrastructure.
* Architects designing multi-region and hybrid cloud network architectures.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `VPC`, `IAM`).
* `Solid` understanding of `TCP`/`IP` networking, `DNS`, and routing fundamentals.
* Familiarity with the `AWS` Management Console and `CLI`.

## Objectives
* Design and implement complex `VPC` architectures with multiple subnets and route tables.
* Configure hybrid connectivity using `Direct Connect` and `VPN`.
* Implement advanced load balancing and traffic distribution strategies.
* Set up global routing and edge networking with `Route 53`, `CloudFront`, and `Global Accelerator`.
* Secure network traffic using firewalls, security groups, and `NACLs`.
* Monitor and troubleshoot network connectivity issues.

## Outline
<!-- chapter: vpc-deep-dive, duration: 2h -->
* `VPC` Deep Dive
    * `VPC` architecture and design principles
    * `CIDR` block planning and allocation
    * Public, private, and isolated subnets
    * Route tables and routing logic
    * `IPv6` support in `VPC`
    * Multiple `VPC` `design patterns`
<!-- chapter: internet-gateway-and-nat-gateway, duration: 1h -->
* Internet Gateway and `NAT Gateway`
    * Internet Gateway configuration and routing
    * `NAT Gateway` setup and high availability
    * `NAT` instance vs `NAT Gateway`
    * Egress-only Internet Gateway for `IPv6`
    * Cost considerations for `NAT Gateway`
<!-- chapter: security-groups-and-network-acls, duration: 1h -->
* Security Groups and Network `ACLs`
    * Security group rules and evaluation
    * Stateful vs stateless filtering
    * Network `ACL` rules and precedence
    * Layered security with security groups and `NACLs`
    * Best practices for rule management
<!-- chapter: vpc-peering-and-transit-gateway, duration: 2h -->
* `VPC` Peering and `Transit Gateway`
    * `VPC` peering setup and limitations
    * Peering across regions and accounts
    * `AWS Transit Gateway` architecture
    * `Transit Gateway` route tables and associations
    * `Transit Gateway` inter-region peering
    * Multi-account networking with `RAM`
<!-- chapter: aws-direct-connect, duration: 2h -->
* `AWS Direct Connect`
    * `Direct Connect` concepts and connection types
    * Virtual interfaces (private, public, transit)
    * `Direct Connect Gateway`
    * Redundancy and resiliency patterns
    * `Link Aggregation Groups`
    * Migrating from `VPN` to `Direct Connect`
<!-- chapter: vpn-connectivity, duration: 1h -->
* `VPN` Connectivity
    * Site-to-site `VPN` configuration
    * `VPN` over `Transit Gateway`
    * `AWS Client VPN` setup and management
    * `VPN` monitoring and troubleshooting
    * Accelerated site-to-site `VPN`
<!-- chapter: vpc-endpoints-and-privatelink, duration: 1h -->
* `VPC` Endpoints and `PrivateLink`
    * Gateway endpoints for `S3` and `DynamoDB`
    * Interface endpoints and `PrivateLink`
    * Endpoint policies and access control
    * Cross-account and cross-region endpoint access
    * Endpoint services for custom applications
<!-- chapter: elastic-load-balancing, duration: 2h -->
* `Elastic Load Balancing`
    * Application Load Balancer advanced routing
    * Network Load Balancer configuration and use cases
    * Gateway Load Balancer for inline appliances
    * Target groups and health checks
    * `SSL`/`TLS` termination and `SNI`
    * Cross-zone load balancing
<!-- chapter: route-53, duration: 2h -->
* `Route 53`
    * Hosted zones and record types
    * Routing policies (simple, weighted, latency, failover, geolocation, geo-proximity)
    * `DNS` failover and health checks
    * `Route 53 Resolver` for hybrid `DNS`
    * `DNSSEC` signing
    * Traffic flow and traffic policies
<!-- chapter: cloudfront-and-edge-networking, duration: 2h -->
* `CloudFront` and Edge Networking
    * `CloudFront` distributions and origins
    * Cache behaviors and invalidation
    * Origin Access Control for `S3`
    * `Lambda@Edge` and `CloudFront Functions`
    * `CloudFront` security with `WAF` and signed URLs
    * Real-time logs and monitoring
<!-- chapter: aws-global-accelerator, duration: 2h -->
* `AWS Global Accelerator`
    * `Global Accelerator` architecture and anycast `IPs`
    * Endpoint groups and traffic dials
    * Health checking and failover
    * `Global Accelerator` vs `CloudFront`
    * Custom routing accelerators
<!-- chapter: network-monitoring-and-troubleshooting, duration: 2h -->
* Network Monitoring and Troubleshooting
    * `VPC` flow logs analysis
    * Traffic mirroring for packet inspection
    * `VPC Reachability Analyzer`
    * `Network Access Analyzer`
    * `CloudWatch` network metrics
    * Troubleshooting common connectivity issues
<!-- chapter: aws-network-firewall, duration: 2h -->
* `AWS Network Firewall`
    * Network `Firewall` architecture and deployment
    * Stateless and stateful rule groups
    * Domain filtering and intrusion prevention
    * Centralized `firewall` with `Transit Gateway`
    * Logging and monitoring `firewall` activity
<!-- chapter: hybrid-networking-patterns, duration: 2h -->
* Hybrid Networking Patterns
    * Hub-and-spoke network topology
    * Shared services `VPC`
    * Multi-region network architectures
    * Hybrid `DNS` resolution strategies
    * Network segmentation and isolation patterns
    * Migration strategies for on-premises networks

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
