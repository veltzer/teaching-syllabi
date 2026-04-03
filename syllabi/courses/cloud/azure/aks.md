---
tags:
  - infrastructure:azure
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
<!-- course: aks -->
# `Azure` `Kubernetes` Service (AKS)

## Description
This course covers `Azure` `Kubernetes` Service (AKS), Microsoft's managed `Kubernetes` offering. Participants will learn how to provision and manage AKS clusters, integrate with `Azure` `Active Directory`, configure advanced networking with `Azure` CNI, and leverage `Azure`-native services such as `Azure` Monitor, `Azure` Policy, and `Azure` Key `Vault` to build secure, scalable, and cost-effective `Kubernetes` environments.

## Duration
16 hours / 2 days

## Intended Audience
* Developers and `DevOps` engineers deploying containerized workloads on `Azure`.
* Architects designing `Kubernetes`-based solutions on the `Azure` platform.
* SREs managing AKS clusters in production environments.

## Prerequisites
* Experience working in technical environments.
* Basic understanding of containerization concepts.

## Required Knowledge
* Introduction to `Kubernetes`
* Introduction to the `Azure` Cloud

## Objectives
* Understand AKS architecture and its integration with `Azure` services.
* Provision and configure AKS clusters for various workload requirements.
* Integrate AKS with `Azure` `Active Directory` for authentication and authorization.
* Configure advanced networking using `Azure` CNI and virtual nodes.
* Monitor AKS workloads with `Azure` Monitor for containers.
* Implement security and compliance using `Azure` Policy and `Azure` Key `Vault`.
* Scale workloads with KEDA and manage costs effectively.

## Outline
<!-- chapter: introduction-to-aks, duration: 1h -->
* Introduction to AKS
    * AKS overview and architecture
    * AKS vs self-managed `Kubernetes`
    * Control plane management
    * Supported `Kubernetes` versions and upgrade policies
<!-- chapter: cluster-provisioning, duration: 1h -->
* Cluster Provisioning
    * Creating AKS clusters via Portal, az `CLI`, and `Terraform`
    * Node pools and virtual machine scale sets
    * System and user node pools
    * Availability zones for AKS
    * Cluster configuration and settings
<!-- chapter: azure-ad-integration, duration: 2h -->
* `Azure` AD Integration
    * `Azure` AD-managed identity
    * `Azure` `RBAC` for `Kubernetes`
    * `Azure` AD workload identity
    * Conditional access policies
    * Integrating with `Azure` AD groups
<!-- chapter: azure-cni-networking, duration: 2h -->
* `Azure` CNI Networking
    * Kubenet vs `Azure` CNI
    * `Azure` CNI overlay
    * Network policies with `Azure` Network Policy Manager and Calico
    * `Ingress` controllers and `Azure` Application Gateway
    * Private clusters and `private link`
<!-- chapter: virtual-nodes, duration: 1h -->
* Virtual Nodes
    * Virtual nodes and `Azure` Container Instances
    * Serverless `Kubernetes` with virtual nodes
    * Burst scaling scenarios
    * Limitations and considerations
<!-- chapter: azure-monitor-for-containers, duration: 2h -->
* `Azure` Monitor for Containers
    * Enabling Container Insights
    * Log collection and analysis
    * Performance metrics and dashboards
    * Alerting on cluster and workload health
    * Integration with `Azure` Log Analytics
<!-- chapter: azure-policy-for-aks, duration: 2h -->
* `Azure` Policy for AKS
    * Policy concepts and built-in policies
    * Enforcing security baselines
    * Custom policy definitions
    * `Azure` Policy for `Kubernetes` (Gatekeeper)
    * Compliance reporting
<!-- chapter: azure-key-vault-integration, duration: 1h -->
* `Azure` Key `Vault` Integration
    * Secrets Store CSI Driver
    * Mounting secrets and certificates
    * Key rotation and lifecycle management
    * Access control with managed identities
<!-- chapter: keda-auto-scaling, duration: 2h -->
* KEDA Auto-Scaling
    * Introduction to KEDA
    * Event-driven auto-scaling
    * Supported scalers
    * Horizontal Pod Autoscaler vs KEDA
    * Custom scaling configurations
<!-- chapter: cost-management, duration: 2h -->
* Cost Management
    * Understanding AKS pricing
    * Right-sizing node pools
    * Spot node pools
    * Start/stop cluster capabilities
    * `Azure` Cost Management and budgets
    * Resource optimization recommendations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
