---
tags:
  - infrastructure:linux
  - practices:sre
  - concepts:scalability
  - practices:sysadmin
level: advanced
category: operating-systems
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:architects
  - audiences:sres
---
<!-- course: linux_high_availability -->
# `Linux` High Availability

## Description
This advanced course covers the design and implementation of highly available `Linux` infrastructure using industry-standard clustering technologies. Participants will learn to deploy and manage Pacemaker clusters with Corosync, configure DRBD for replicated storage, and implement fencing mechanisms to ensure data integrity. The course addresses both active/passive and active/active cluster configurations for various workloads.

The course provides hands-on experience with real-world HA scenarios, equipping participants to build and maintain resilient `Linux` infrastructure that meets stringent uptime requirements.

## Duration
16 hours / 2 days

## Intended Audience
* System administrators building highly available `Linux` infrastructure
* `DevOps` engineers automating cluster deployments
* Architects designing fault-tolerant systems
* Site reliability engineers responsible for uptime and availability

## Prerequisites
* Strong `Linux` system administration skills
* Experience with `Linux` networking configuration
* Familiarity with storage concepts (block devices, `file` systems)
* Basic understanding of clustering concepts
* Command line proficiency

## Objectives
* Deploy and configure Pacemaker and Corosync clusters
* Set up DRBD for replicated block-level storage
* Implement fencing and STONITH for data protection
* Configure resource agents for various services
* Design active/passive and active/active cluster topologies
* Integrate cluster `file` systems (GFS2, OCFS2)
* Integrate `HAProxy` for load-balanced services
* Monitor and troubleshoot cluster health and split-brain scenarios

## Outline
<!-- chapter: pacemaker-cluster-manager, duration: 1h -->
* Pacemaker Cluster Manager
    * Pacemaker architecture and components
    * Cluster Information Base (CIB)
    * Policy engine and resource management
    * Cluster resource manager daemon
    * Using pcs and crm shell for cluster management
    * Cluster properties and options
<!-- chapter: corosync, duration: 1h -->
* Corosync
    * Corosync communication layer
    * Configuring Corosync (corosync.conf)
    * Redundant ring configuration
    * Encryption and authentication
    * Corosync with Kronosnet
    * Troubleshooting Corosync communication
<!-- chapter: drbd-distributed-replicated-block-device, duration: 1h -->
* DRBD (Distributed Replicated Block Device)
    * DRBD architecture and replication modes
    * Configuring primary/secondary DRBD resources
    * Dual-primary configuration
    * Synchronization and resynchronization
    * Performance tuning for DRBD
    * Split-brain recovery with DRBD
<!-- chapter: fencing-and-stonith, duration: 1h -->
* Fencing and STONITH
    * Why fencing is essential in clusters
    * STONITH device types and agents
    * Configuring fence devices (`IPMI`, iLO, libvirt, SBD)
    * Fencing levels and topology
    * Testing fencing configuration
    * Fencing best practices
<!-- chapter: resource-agents, duration: 1h -->
* Resource Agents
    * Resource agent types (OCF, LSB, `systemd`, service)
    * Configuring primitive resources
    * Multi-state (promotable) resources
    * Clone resources
    * Resource groups
    * Resource operations (start, stop, monitor intervals)
<!-- chapter: constraints, duration: 1h -->
* Constraints
    * Location constraints
    * Colocation constraints
    * Order constraints
    * Resource stickiness and migration thresholds
    * Constraint rules and expressions
    * Constraint management and troubleshooting
<!-- chapter: quorum, duration: 1h -->
* Quorum
    * Quorum concepts and voting
    * Quorum policies (ignore, freeze, stop, suicide)
    * Two-node cluster quorum considerations
    * Quorum device (QDevice) and QNetd
    * Last-man-standing and auto-tie-breaker
<!-- chapter: active-passive-and-active-active-configurations, duration: 2h -->
* Active/Passive and Active/Active Configurations
    * Active/passive failover design
    * Virtual `IP` address management
    * Active/active `design patterns`
    * Load distribution across nodes
    * Service placement strategies
    * Choosing between active/passive and active/active
<!-- chapter: gfs2-and-ocfs2, duration: 2h -->
* GFS2 and OCFS2
    * Shared storage cluster `file` systems overview
    * GFS2 architecture and configuration
    * OCFS2 architecture and configuration
    * Distributed lock management
    * Fencing requirements for cluster `file` systems
    * Performance considerations
<!-- chapter: haproxy-integration, duration: 1h -->
* `HAProxy` Integration
    * `HAProxy` as a cluster-managed resource
    * Configuring `HAProxy` with Pacemaker
    * Health `check` configuration
    * Load balancing algorithms
    * Failover of `HAProxy` instances
<!-- chapter: monitoring-cluster-health, duration: 2h -->
* Monitoring Cluster Health
    * Cluster status commands and tools
    * Monitoring node and resource state
    * Log analysis for cluster events
    * Integration with monitoring systems (`Nagios`, `Zabbix`, `Prometheus`)
    * Alerting on cluster state changes
    * Capacity planning for HA clusters
<!-- chapter: troubleshooting-split-brain, duration: 2h -->
* Troubleshooting Split-Brain
    * Understanding split-brain scenarios
    * Causes of split-brain in clusters
    * Prevention mechanisms (fencing, quorum)
    * Detecting split-brain conditions
    * Recovery procedures after split-brain
    * Post-incident analysis and prevention

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
