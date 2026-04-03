---
tags:
  - infrastructure:cloud
  - infrastructure:gcp
  - security:iam
  - concepts:scalability
  - concepts:architecture
  - infrastructure:containers
  - infrastructure:kubernetes
  - practices:devops
level: intermediate
category: cloud
duration_hours: 32
audience:
  - audiences:devops
  - audiences:developers
  - audiences:architects
  - audiences:sysadmins
---
<!-- course: gcp_cloud_engineer -->
# `Google Cloud Platform` - Cloud Engineer

## Description
This course prepares participants to deploy applications, monitor operations, and manage
enterprise solutions on `Google Cloud Platform`. It covers core infrastructure services
including compute, networking, storage, and databases, along with identity management,
security, and infrastructure as code. Participants will gain hands-on experience with
`GCP` services aligned with the Associate Cloud Engineer certification path.

## Duration
32 hours / 4 days

## Intended Audience
* Cloud engineers deploying and managing applications on `GCP`
* System administrators transitioning to cloud operations
* `DevOps` engineers working with `Google Cloud Platform`
* Developers who need to understand `GCP` infrastructure

## Prerequisites
* Basic understanding of `cloud computing` concepts
* Familiarity with `Linux` command line
* Basic networking knowledge (`TCP`/`IP`, `DNS`, `HTTP`)
* Experience with at least one programming language

## Objectives
* Set up and configure `GCP` projects, billing, and `IAM`
* Deploy and manage compute resources: VMs, `GKE`, `Cloud Run`
* Design and implement `VPC` networks with security controls
* Select and configure appropriate storage and database services
* Monitor and troubleshoot `GCP` workloads using Cloud Operations

## Outline
<!-- chapter: introduction-to-google-cloud-platform, duration: 3h -->
* Introduction to `Google Cloud Platform`
    * `GCP` global infrastructure: regions, zones, and edge locations
    * Resource hierarchy: organizations, folders, and projects
    * Cloud Console, Cloud Shell, and `gcloud` `CLI`
    * Enabling `API`s and managing quotas
    * Billing accounts, budgets, and cost alerts
<!-- chapter: identity-and-access-management, duration: 3h -->
* Identity and Access Management
    * `IAM` roles: basic, predefined, and custom
    * Users, groups, and service accounts
    * `IAM` policies and resource-level permissions
    * Service account best practices and impersonation
    * Workload Identity for `GKE`
    * Cloud Identity and organizational policies
<!-- chapter: compute-engine, duration: 4h -->
* `Compute Engine`
    * Virtual machine instances and machine types
    * Spot VMs and preemptible instances
    * Persistent Disk and Hyperdisk
    * Instance templates and managed instance groups
    * Autoscaling and load balancing
    * OS Login and VM Manager
    * Snapshots and custom images
<!-- chapter: google-kubernetes-engine, duration: 3h -->
* `Google Kubernetes Engine`
    * `GKE` Autopilot and Standard clusters
    * Deploying containerized applications with `kubectl`
    * Services, `Ingress`, and networking
    * Node pools and cluster autoscaling
    * Private clusters and regional clusters
    * `GKE` security best practices
<!-- chapter: serverless-compute, duration: 3h -->
* Serverless Compute
    * `Cloud Run`: deploying from source and container images
    * `Cloud Run` functions (event-driven functions)
    * Eventarc for event routing
    * Cloud Tasks and Cloud Scheduler
    * Choosing between compute options
<!-- chapter: networking, duration: 4h -->
* Networking
    * `VPC` networks: custom mode and shared `VPC`
    * Subnets, `IP` addressing, and `DNS` configuration
    * Cloud `NAT` and `Cloud Router`
    * `Firewall` rules and network tags
    * Cloud `VPN` and Cloud Interconnect
    * `VPC` Peering and `Private Service Connect`
    * Load balancers: `HTTP`(S), `TCP`/`SSL`, network
    * Network Service Tiers
<!-- chapter: storage-and-databases, duration: 5h -->
* Storage and Databases
    * `Cloud Storage`: classes, lifecycle policies, and `IAM`
    * Filestore for managed `file` storage
    * Cloud `SQL`: `MySQL`, `PostgreSQL`, and `SQL Server`
    * Cloud Spanner for globally distributed relational data
    * `Firestore` for document databases
    * Bigtable for wide-column workloads
    * AlloyDB for `PostgreSQL`-compatible analytics
    * Memorystore for caching (`Redis`)
    * Choosing the right storage and database service
<!-- chapter: infrastructure-as-code, duration: 3h -->
* Infrastructure as Code
    * `Terraform` on `GCP`
    * Config Connector for `Kubernetes`-native resource management
    * Deployment Manager
    * `Helm` for `GKE` application deployment
<!-- chapter: monitoring-and-operations, duration: 4h -->
* Monitoring and Operations
    * `Cloud Monitoring`: metrics, dashboards, and alerts
    * `Cloud Logging`: log routing, retention, and analysis
    * Cloud Trace and Cloud Profiler
    * Error Reporting
    * Ops Agent and custom metrics
    * Managed Service for `Prometheus`
    * Active Assist and `Gemini` Cloud Assist

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
