---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
  - infrastructure:kubernetes
  - infrastructure:containers
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:architects
  - audiences:sres
---
<!-- course: gke -->
# Google `Kubernetes` Engine (`GKE`)

## Description
This course provides a comprehensive guide to Google `Kubernetes` Engine (`GKE`), `Google Cloud`'s managed `Kubernetes` service. Participants will learn how to create and manage `GKE` clusters, understand the differences between Autopilot and Standard modes, configure networking and security, and integrate with the broader `GCP` ecosystem including `Cloud Monitoring`, `Cloud Logging`, and `Anthos`.

## Duration
16 hours / 2 days

## Intended Audience
* Developers and `DevOps` engineers who want to deploy and manage containerized applications on `GCP`.
* Architects evaluating managed `Kubernetes` solutions on `Google Cloud`.
* SREs responsible for operating `Kubernetes` workloads on `GKE`.

## Prerequisites
* Experience working in technical environments.
* Basic understanding of containerization concepts.

## Required Knowledge
* Introduction to `Kubernetes`
* `GCP` Fundamentals

## Objectives
* Understand `GKE` architecture and its integration with `GCP` services.
* Choose between Autopilot and Standard cluster modes based on requirements.
* Create, configure, and manage `GKE` clusters and node pools.
* Implement `GKE` networking with `VPC`-native clusters.
* Secure `GKE` workloads using Workload Identity and other security features.
* Monitor and troubleshoot `GKE` clusters using `Cloud Monitoring` and Logging.
* Optimize costs for `GKE` deployments.

## Outline
<!-- chapter: introduction-to-gke, duration: 1h -->
* Introduction to `GKE`
    * `GKE` overview and architecture
    * `GKE` vs self-managed `Kubernetes`
    * `GKE` control plane and node components
    * Release channels and versioning
<!-- chapter: cluster-creation-and-configuration, duration: 1h -->
* Cluster Creation and Configuration
    * Autopilot vs Standard mode
    * Creating clusters via Console, gcloud, and `Terraform`
    * Cluster configuration options
    * Regional vs zonal clusters
<!-- chapter: node-pools, duration: 2h -->
* Node Pools
    * Node pool concepts and configuration
    * Machine types and custom images
    * Node auto-scaling
    * Node auto-provisioning
    * Spot and preemptible VMs
    * Node taints and tolerations
<!-- chapter: gke-networking, duration: 2h -->
* `GKE` Networking
    * `VPC`-native clusters
    * Pod and Service `IP` addressing
    * `GKE` `Ingress` and load balancing
    * Network policies
    * Private clusters
    * Shared `VPC` configurations
<!-- chapter: workload-identity, duration: 2h -->
* Workload Identity
    * Workload Identity concepts
    * Configuring Workload Identity
    * Migrating from node-level service accounts
    * Best practices for identity management
<!-- chapter: gke-security, duration: 2h -->
* `GKE` Security
    * Cluster security hardening
    * `Binary Authorization`
    * Pod security policies and standards
    * Secrets management
    * `GKE` Sandbox (gVisor)
    * Network security and `firewall` rules
<!-- chapter: monitoring-and-logging, duration: 2h -->
* Monitoring and Logging
    * `Cloud Monitoring` integration
    * `Cloud Logging` for `GKE`
    * Custom metrics and dashboards
    * Alerting policies
    * `GKE` usage metering
<!-- chapter: anthos-overview, duration: 2h -->
* `Anthos` Overview
    * What is `Anthos`?
    * `Anthos` Service Mesh
    * `Anthos` Config Management
    * Multi-cluster management
    * Hybrid and multi-cloud scenarios
<!-- chapter: cost-optimization, duration: 2h -->
* Cost Optimization
    * Understanding `GKE` pricing
    * Resource requests and limits optimization
    * Committed use discounts
    * Right-sizing workloads
    * Cluster autoscaler tuning
    * Cost monitoring and budgets

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
