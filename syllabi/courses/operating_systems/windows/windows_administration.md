---
tags:
  - infrastructure:windows
  - practices:sysadmin
level: intermediate
category: operating-systems
duration_hours: 40
audience:
  - audiences:sysadmins
---
<!-- course: windows_administration -->
# `Windows` Administration

## Description
This course provides comprehensive training in `Windows Server` administration. Students
will learn how to install, configure, and manage `Windows Server` environments, including
`Active Directory`, networking services, virtualization, and security. The course
emphasizes hands-on `PowerShell` administration and modern management practices for
enterprise `Windows` infrastructure.

## Duration
40 hours / 5 days

## Intended Audience
* System administrators responsible for `Windows Server` environments.
* IT professionals preparing for `Windows` infrastructure roles.
* Engineers transitioning from `Linux` administration to `Windows`.

## Prerequisites
* Basic understanding of networking concepts (`TCP`/`IP`, `DNS`, `DHCP`).
* Familiarity with `Windows` desktop operating systems.
* Basic command line experience.

## Objectives
* understand the core concepts and principles of `Windows Server` administration
* gain practical knowledge of `Active Directory` and Group Policy
* gain practical knowledge of `PowerShell` for server administration
* gain practical knowledge of `Windows` security and monitoring

## Outline
<!-- chapter: windows-server-architecture, duration: 2h -->
* `Windows Server` Architecture
    * Server editions and licensing
    * Server Core vs Desktop Experience
    * System requirements and planning
    * `Windows Server` roles and features
<!-- chapter: installation-and-deployment, duration: 2h -->
* Installation and Deployment
    * Installation methods
    * Unattended installation
    * `Windows` Deployment Services (WDS)
    * Server imaging and cloning
    * Initial configuration tasks
<!-- chapter: active-directory, duration: 3h -->
* `Active Directory`
    * Domain Services (AD DS) overview
    * Domains, forests, and trusts
    * Organizational Units (OUs)
    * Users, groups, and computers
    * Group Policy Objects (GPOs)
    * GPO design and troubleshooting
    * Sites and replication
    * AD backup and recovery
<!-- chapter: dns-and-dhcp, duration: 3h -->
* `DNS` and `DHCP`
    * `DNS` server configuration
    * `DNS` zones and records
    * `DNS` integration with `Active Directory`
    * `DHCP` server setup
    * `DHCP` scopes and options
    * `DHCP` failover
<!-- chapter: file-services-and-storage, duration: 3h -->
* `File` Services and Storage
    * `File` server roles
    * `NTFS` and ReFS `file` systems
    * Share permissions and `NTFS` permissions
    * Distributed `File` System (DFS)
    * Storage Spaces
    * Disk management and `RAID`
<!-- chapter: hyper-v-virtualization, duration: 3h -->
* `Hyper-V` Virtualization
    * `Hyper-V` architecture
    * Creating and managing virtual machines
    * Virtual networking
    * Virtual hard disks
    * Snapshots and checkpoints
    * Live migration
    * Replication
<!-- chapter: powershell-administration, duration: 2h -->
* `PowerShell` Administration
    * `PowerShell` fundamentals for server management
    * Cmdlets for AD, `DNS`, `DHCP` management
    * Scripting and automation
    * Remote management with `PowerShell`
    * Desired State Configuration (DSC)
<!-- chapter: windows-networking, duration: 3h -->
* `Windows` Networking
    * Network adapter configuration
    * NIC teaming
    * `Windows` `Firewall` with Advanced Security
    * `VPN` and Remote Access
    * Network Policy Server (NPS)
    * `IP` Address Management (IPAM)
<!-- chapter: security, duration: 3h -->
* Security
    * `Windows` `Firewall` configuration
    * BitLocker drive encryption
    * `Windows Defender` and antimalware
    * Security baselines
    * User rights and privileges
    * Audit policies
<!-- chapter: certificate-services, duration: 2h -->
* Certificate Services
    * Public Key Infrastructure (`PKI`) overview
    * `Active Directory` Certificate Services (AD CS)
    * Certificate templates
    * Certificate enrollment
    * Certificate revocation
<!-- chapter: iis-web-server, duration: 2h -->
* `IIS` Web Server
    * `IIS` installation and configuration
    * Hosting websites and applications
    * Application pools
    * `SSL`/`TLS` configuration
    * `IIS` security hardening
<!-- chapter: windows-update-and-wsus, duration: 2h -->
* `Windows` Update and WSUS
    * `Windows` Update for servers
    * WSUS deployment and configuration
    * Approval and deployment workflows
    * Reporting and compliance
<!-- chapter: backup-and-recovery, duration: 2h -->
* Backup and Recovery
    * `Windows Server` Backup
    * Backup strategies and scheduling
    * System state backup
    * Bare metal recovery
    * `Active Directory` recovery options
<!-- chapter: monitoring, duration: 2h -->
* Monitoring
    * `Event Viewer` and event logs
    * `Performance Monitor` and data collectors
    * Resource Monitor
    * `Windows Admin Center`
    * Centralized logging strategies
<!-- chapter: remote-management, duration: 2h -->
* Remote Management
    * Remote Desktop Services
    * `Windows` Remote Management (WinRM)
    * `PowerShell` remoting
    * `Windows Admin Center`
    * Remote Server Administration Tools (RSAT)
<!-- chapter: failover-clustering, duration: 2h -->
* Failover Clustering
    * Cluster architecture
    * Cluster setup and validation
    * Clustered roles and services
    * Quorum configuration
    * Cluster-Aware Updating
<!-- chapter: windows-containers, duration: 2h -->
* `Windows` Containers
    * Container concepts on `Windows`
    * `Windows` Server containers vs `Hyper-V` containers
    * `Docker` on `Windows Server`
    * Container images and registries
    * Orchestration basics

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
