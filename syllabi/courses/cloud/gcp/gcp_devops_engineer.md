---
tags:
  - infrastructure:cloud
  - infrastructure:gcp
  - infrastructure:containers
  - infrastructure:kubernetes
  - practices:devops
  - practices:ci-cd
  - practices:monitoring
  - practices:observability
  - tools:terraform
  - tools:docker
level: intermediate
category: devops
duration_hours: 32
audience:
  - audiences:devops
  - audiences:developers
  - audiences:sysadmins
---
<!-- course: gcp_devops_engineer -->
# `Google Cloud Platform` - `DevOps` Engineer

## Description
This course teaches `DevOps` engineering practices on `Google Cloud Platform`. Participants will
learn to build `CI/CD` pipelines, manage infrastructure as code, implement SRE practices, and
operate observability systems at scale. The course covers `Cloud Build`, Cloud Deploy, `GKE`,
`Cloud Run`, and the full Cloud Operations suite. It is aligned with the Professional Cloud
`DevOps` Engineer certification path.

## Duration
32 hours / 4 days

## Intended Audience
* `DevOps` engineers building and operating systems on `GCP`
* Site reliability engineers implementing SRE practices
* Platform engineers managing `Kubernetes` and serverless infrastructure
* Developers responsible for deployment and operations

## Prerequisites
* Working experience with `Linux` command line and scripting
* Familiarity with `GCP` core services or equivalent cloud platform
* Basic experience with `Git`, `Docker`, and `CI/CD` concepts
* Understanding of `Kubernetes` fundamentals

## Objectives
* Design and implement `CI/CD` pipelines using `GCP` native tools
* Manage infrastructure as code with `Terraform` and Config Connector
* Implement SRE practices: SLIs, SLOs, and error budgets
* Build comprehensive observability with Cloud Operations
* Operate and scale containerized workloads on `GKE` and `Cloud Run`

## Outline
<!-- chapter: devops-and-sre-on-google-cloud, duration: 3h -->
* `DevOps` and SRE on `Google Cloud`
    * `DevOps` principles and SRE practices
    * `GCP` `DevOps` toolchain overview
    * Resource hierarchy and multi-project organization
    * Shared `VPC` and cross-project networking
    * `IAM` for `DevOps` workflows
<!-- chapter: continuous-integration, duration: 3h -->
* Continuous Integration
    * `Cloud Build`: build configs, triggers, and substitutions
    * Building and testing applications
    * Container image builds and Artifact Registry
    * Vulnerability scanning with Artifact Analysis
    * `Binary Authorization` for supply chain security
    * Integration with `GitHub`, `GitLab`, and `Bitbucket`
<!-- chapter: continuous-delivery-and-deployment, duration: 3h -->
* `Continuous Delivery` and Deployment
    * Cloud Deploy: delivery pipelines, targets, and releases
    * Deployment strategies: canary, blue/green, rolling
    * Traffic splitting for gradual rollouts
    * Automated rollback and approval workflows
    * Multi-environment promotion (dev, staging, production)
    * Feature flags and progressive delivery
<!-- chapter: infrastructure-as-code, duration: 3h -->
* Infrastructure as Code
    * `Terraform` on `GCP`: providers, modules, and state management
    * Infrastructure Manager for managed `Terraform`
    * Config Connector for `Kubernetes`-native `GCP` resources
    * Cloud Foundation Toolkit and blueprints
    * `GitOps` patterns for infrastructure
    * `Helm` and `Kustomize` for `Kubernetes` configuration
<!-- chapter: container-operations, duration: 3h -->
* Container Operations
    * `GKE` cluster management: Autopilot and Standard
    * `GKE` fleet management for multi-cluster operations
    * `Cloud Run` for serverless containers
    * Deployment patterns: Skaffold and kpt
    * Container security: image scanning, runtime security
    * Service mesh with Cloud Service Mesh
<!-- chapter: observability-and-monitoring, duration: 4h -->
* Observability and Monitoring
    * `Cloud Monitoring`: metrics, dashboards, and uptime checks
    * `Cloud Logging`: log routing, retention, and analytics
    * Cloud Trace: distributed tracing and latency analysis
    * Managed Service for `Prometheus` and PromQL
    * `OpenTelemetry` integration
    * Custom metrics and log-based metrics
    * Synthetic monitors
<!-- chapter: sre-practices, duration: 4h -->
* SRE Practices
    * Defining SLIs and SLOs
    * Error budgets and alerting policies
    * Capacity planning: quotas, limits, and reservations
    * Autoscaling for `Compute Engine`, `GKE`, and `Cloud Run`
    * Incident management and postmortems
    * Chaos engineering and failure testing
<!-- chapter: alerting-and-incident-response, duration: 3h -->
* Alerting and Incident Response
    * Alert policies: threshold, absence, and SLO-based
    * Notification channels and escalation
    * Playbooks and incident documentation
    * `Gemini` Cloud Assist for log analysis
    * Integration with `PagerDuty` and third-party tools
<!-- chapter: security-in-devops, duration: 3h -->
* Security in `DevOps`
    * Secret management: Secret Manager, Cloud `KMS`, and Parameter Manager
    * Workload Identity Federation
    * `CI/CD` pipeline security
    * `SLSA` framework and build provenance
    * `IAM` best practices for automation
<!-- chapter: cost-optimization, duration: 3h -->
* Cost Optimization
    * Spot VMs and preemptible instances
    * Committed-use and sustained-use discounts
    * Network Service Tiers
    * `GKE` and `Cloud Run` cost optimization
    * Active Assist and cost recommenders

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
