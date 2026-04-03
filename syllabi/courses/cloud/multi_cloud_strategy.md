---
tags:
  - infrastructure:cloud
  - infrastructure:aws
  - infrastructure:azure
  - infrastructure:gcp
  - concepts:architecture
level: advanced
category: cloud
duration_hours: 16
audience:
  - audiences:architects
  - audiences:managers
---
<!-- course: multi_cloud_strategy -->
# Multi-Cloud Strategy

## Description
This course provides a comprehensive overview of multi-cloud strategies, helping architects
and managers `make` informed decisions about `when` and how to operate across multiple cloud
providers. The course covers service mapping across `AWS`, `Azure`, and `GCP`, abstraction
layers and tooling, networking, identity federation, compliance, cost management, and
organizational considerations. Participants will learn to evaluate trade-offs and develop
practical multi-cloud strategies aligned with business goals.

## Duration
16 hours / 2 days

## Intended Audience
* architects designing systems that span multiple cloud providers.
* engineering managers evaluating multi-cloud strategies.
* technical leaders responsible for cloud strategy decisions.

## Prerequisites
* experience with at least one major cloud provider (`AWS`, `Azure`, or `GCP`).
* understanding of cloud-native architecture principles.
* familiarity with infrastructure as code concepts.

## Required Knowledge
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)

## Objectives
* understand the motivations, benefits, and risks of multi-cloud adoption.
* map equivalent services across `AWS`, `Azure`, and `GCP`.
* evaluate abstraction tools and strategies for multi-cloud operations.
* develop practical multi-cloud strategies aligned with organizational needs.

## Outline
<!-- chapter: multi-cloud-motivations-and-trade-offs, duration: 1h -->
* Multi-cloud motivations and trade-offs
    * reasons for multi-cloud adoption
    * risks and complexity costs
    * multi-cloud vs hybrid cloud
    * common multi-cloud patterns
<!-- chapter: vendor-lock-in-assessment, duration: 1h -->
* Vendor lock-in assessment
    * identifying lock-in vectors
    * evaluating portability of workloads
    * managed services vs open-source alternatives
    * data gravity and exit costs
<!-- chapter: service-mapping-across-clouds, duration: 2h -->
* Service mapping across clouds
    * compute services (`EC2`, `Azure VMs`, `Compute Engine`)
    * container services (`EKS`, AKS, `GKE`)
    * serverless (`Lambda`, `Azure Functions`, `Cloud Functions`)
    * storage (`S3`, `Blob Storage`, `Cloud Storage`)
    * networking (`VPC` implementations across providers)
    * databases (managed relational, `NoSQL`, caching)
    * `AI`/`ML` services comparison
<!-- chapter: abstraction-layers-and-tooling, duration: 1h -->
* Abstraction layers and tooling
    * `Terraform` for multi-cloud provisioning
    * Pulumi and programmatic infrastructure
    * Crossplane for `Kubernetes`-native infrastructure
    * abstraction trade-offs (lowest common denominator)
<!-- chapter: kubernetes-as-cloud-abstraction, duration: 1h -->
* `Kubernetes` as cloud abstraction
    * managed `Kubernetes` across providers
    * workload portability
    * platform engineering with `Kubernetes`
    * limitations of `Kubernetes` as an abstraction
<!-- chapter: networking-across-clouds, duration: 1h -->
* Networking across clouds
    * cloud interconnects and `VPN`
    * `DNS` and traffic management
    * latency and data transfer costs
    * network architecture patterns
<!-- chapter: identity-federation, duration: 1h -->
* Identity federation
    * identity providers and SSO
    * cross-cloud `IAM`
    * workload identity federation
    * secrets management across clouds
<!-- chapter: data-sovereignty-and-compliance, duration: 1h -->
* Data sovereignty and compliance
    * data residency requirements
    * regulatory frameworks (`GDPR`, `HIPAA`, `SOC` 2)
    * audit and governance
    * compliance tooling across providers
<!-- chapter: cost-management-across-providers, duration: 1h -->
* Cost management across providers
    * unified cost visibility
    * FinOps practices for multi-cloud
    * committed use discounts and reservations
    * cost allocation and chargeback
<!-- chapter: disaster-recovery, duration: 1h -->
* Disaster recovery
    * multi-cloud DR strategies
    * RPO and RTO considerations
    * data replication across clouds
    * failover automation
<!-- chapter: organizational-models, duration: 1h -->
* Organizational models
    * team structures for multi-cloud
    * skills and training
    * center of excellence patterns
    * platform teams and self-service
<!-- chapter: migration-strategies, duration: 2h -->
* Migration strategies
    * assessing workloads for migration
    * phased migration approaches
    * data migration challenges
    * testing and validation
<!-- chapter: when-not-to-go-multi-cloud, duration: 2h -->
* `When` not to `go` multi-cloud
    * complexity vs benefit analysis
    * single-cloud optimization
    * scenarios where multi-cloud adds unnecessary cost
    * pragmatic decision framework

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
