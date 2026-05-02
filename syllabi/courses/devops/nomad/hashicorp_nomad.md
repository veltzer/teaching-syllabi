---
tags:
  - tools:nomad
  - practices:devops
  - concepts:distributed-systems
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: hashicorp_nomad -->
# `HashiCorp Nomad`: Workload Orchestrator

## Description
This course provides a comprehensive guide to `HashiCorp Nomad`, a flexible workload orchestrator that deploys and manages containers, legacy applications, and batch jobs. Participants will learn Nomad architecture, job specifications, scheduling strategies, networking, service discovery, secrets management, and multi-region federation. The course includes comparisons with `Kubernetes` and practical migration strategies.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers evaluating or adopting Nomad for workload orchestration
* Infrastructure engineers managing distributed systems
* Platform teams looking for a simpler alternative to `Kubernetes`

## Prerequisites
* Familiarity with containerization concepts (`Docker` or similar).
* Basic understanding of distributed systems.
* Experience with `Linux` command line and HCL or `JSON` configuration.

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the Nomad architecture including servers, clients, regions, and datacenters.
* Write and deploy job specifications using HCL.
* Configure task drivers for containers, binaries, and batch jobs.
* Implement service discovery with Consul and secrets management with Vault.
* Set up networking, `ACLs`, and namespaces for multi-team environments.
* Deploy applications using rolling, canary, and blue-green strategies.
* Operate multi-region federated Nomad clusters.

## Outline
<!-- chapter: introduction-to-nomad, duration: 1h -->
* Introduction to Nomad:
    * What is Nomad and why use it
    * Comparison with `Kubernetes`
    * Nomad in the HashiCorp ecosystem
    * Use cases and deployment scenarios
<!-- chapter: nomad-architecture, duration: 1h -->
* Nomad Architecture:
    * Servers and clients
    * Regions and datacenters
    * Consensus protocol (Raft)
    * Scheduling architecture
    * Gossip protocol for communication
<!-- chapter: job-specifications, duration: 1h -->
* Job Specifications:
    * HCL job specification syntax
    * Job, group, and task hierarchy
    * Parameterized jobs
    * Periodic jobs (cron-like scheduling)
    * Dispatch jobs
    * Job validation and planning
<!-- chapter: task-drivers, duration: 1h -->
* Task Drivers:
    * `Docker` driver
    * exec driver
    * `Java` driver
    * raw_exec driver
    * Isolated task drivers
    * Plugin-based architecture
<!-- chapter: scheduling, duration: 2h -->
* Scheduling:
    * Service scheduler
    * Batch scheduler
    * System scheduler
    * Sysbatch scheduler
    * Bin packing and spread strategies
    * Constraints and affinities
<!-- chapter: networking, duration: 1h -->
* Networking:
    * Bridge networking
    * Host networking
    * CNI plugin integration
    * Service ports and dynamic ports
    * `Consul Connect` for service mesh
<!-- chapter: service-discovery-with-consul, duration: 1h -->
* Service Discovery with Consul:
    * Consul integration overview
    * Service registration and health checks
    * `DNS` and `API`-based discovery
    * Consul template for dynamic configuration
<!-- chapter: secrets-management-with-vault, duration: 1h -->
* Secrets Management with Vault:
    * Vault integration overview
    * Accessing secrets in jobs
    * Dynamic secrets and leases
    * Vault token management
<!-- chapter: acl-system, duration: 1h -->
* ACL System:
    * ACL architecture
    * Policies and tokens
    * Capability-based access control
    * Bootstrapping `ACLs`
<!-- chapter: namespaces, duration: 1h -->
* Namespaces:
    * Creating and managing namespaces
    * Resource quotas
    * Multi-team isolation
<!-- chapter: resource-management, duration: 1h -->
* Resource Management:
    * `CPU` and memory allocation
    * `GPU` scheduling
    * Device plugins
    * Resource oversubscription
<!-- chapter: deployment-strategies, duration: 1h -->
* Deployment Strategies:
    * Rolling deployments
    * Canary deployments
    * Blue-green deployments
    * Deployment monitoring and auto-revert
    * Health checks during deployments
<!-- chapter: monitoring-and-logging, duration: 1h -->
* Monitoring and Logging:
    * Nomad metrics and telemetry
    * Log collection and aggregation
    * Integration with `Prometheus` and `Grafana`
    * Audit logging
<!-- chapter: multi-region-federation, duration: 1h -->
* Multi-Region Federation:
    * Federated cluster setup
    * Multi-region job specifications
    * Cross-region failover
    * Global and regional jobs
<!-- chapter: migration-strategies, duration: 1h -->
* Migration Strategies:
    * Migrating from `Kubernetes` to Nomad
    * Migrating from traditional deployments
    * Hybrid deployment approaches
    * Gradual adoption patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
