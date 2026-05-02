---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - security:iam
level: intermediate
category: cloud
duration_hours: 32
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:architects
---
<!-- course: azure_administrator -->
# `Azure` Administrator (AZ-104)

## Description
This course prepares participants for the Microsoft `Azure` Administrator (AZ-104) certification and provides the skills needed to manage `Azure` infrastructure. The course covers identity and governance, storage, compute, networking, and monitoring, aligning with the official exam objectives. Participants will gain practical experience configuring and managing core `Azure` services in enterprise environments.

The course balances conceptual understanding with hands-on practice, ensuring participants can both pass the certification exam and apply their knowledge in real-world `Azure` administration scenarios.

## Duration
32 hours / 4 days

## Intended Audience
* System administrators transitioning to cloud infrastructure
* `DevOps` engineers working with `Azure` environments
* Cloud architects designing `Azure` solutions
* IT professionals preparing for the AZ-104 certification

## Prerequisites
* Basic understanding of networking concepts (`IP` addressing, `DNS`, `TCP`/`IP`)
* Experience with operating system administration (`Windows` or `Linux`)
* Familiarity with virtualization concepts
* Basic understanding of `PowerShell` or `Azure CLI`

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Manage `Azure Active Directory` identities and governance
* Configure and manage `Azure` storage solutions
* Deploy and manage `Azure` compute resources
* Implement and manage virtual networking
* Monitor and maintain `Azure` resources

## Outline
<!-- chapter: identity-and-governance, duration: 6h -->
* Identity and Governance
    * `Azure Active Directory` overview
    * Users, groups, and administrative units
    * Role-Based Access Control (`RBAC`)
    * Custom roles and role assignments
    * `Azure Policy` creation and management
    * Initiative definitions and compliance
    * Management groups and subscriptions
    * Resource locks and tags
    * `Azure AD` multi-factor authentication
    * Self-service password reset
<!-- chapter: storage, duration: 6h -->
* Storage
    * `Azure` storage accounts and types
    * Blob storage (hot, cool, archive tiers)
    * Lifecycle management policies
    * `Azure Files` and file share configuration
    * `Azure File Sync`
    * Table storage
    * Queue storage
    * Storage security (SAS tokens, access keys, `Azure AD` authorization)
    * Storage replication options (LRS, ZRS, GRS, RA-GRS)
    * AzCopy and Storage Explorer
    * Import/Export service
<!-- chapter: compute, duration: 6h -->
* Compute
    * Virtual machines (sizing, availability sets, availability zones)
    * VM scale sets and autoscaling
    * VM extensions and custom script extensions
    * Managed disks and disk encryption
    * `Azure App Service` plans and web apps
    * Deployment slots and application settings
    * `Azure Container Instances` (ACI)
    * `Azure Kubernetes Service` (AKS) overview
    * AKS deployment and scaling
    * `Azure` Resource Manager templates
    * Bicep for infrastructure as code
<!-- chapter: networking, duration: 8h -->
* Networking
    * Virtual networks (VNets) and subnets
    * `Network Security Groups` (NSGs) and rules
    * `Application Security Groups`
    * `VNet` peering and service endpoints
    * Private endpoints and `Private Link`
    * `Azure Load Balancer` (basic and standard)
    * `Application Gateway` and `WAF`
    * `Azure Front Door`
    * `VPN Gateway` and site-to-site connectivity
    * `ExpressRoute` overview
    * `Azure DNS` zones and record sets
    * Network Watcher and diagnostics
    * User-defined routes and forced tunneling
<!-- chapter: monitoring, duration: 6h -->
* Monitoring
    * `Azure Monitor` overview and data platform
    * Metrics and metric alerts
    * `Log Analytics` workspaces
    * KQL (Kusto Query Language) fundamentals
    * Diagnostic settings and log collection
    * Action groups and alert processing rules
    * `Azure` dashboards and workbooks
    * `Application Insights` overview
    * Network monitoring and connectivity checks
    * Backup and recovery with `Azure Backup`
    * `Azure Site Recovery` overview

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
