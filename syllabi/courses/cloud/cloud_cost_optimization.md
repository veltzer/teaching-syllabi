---
tags:
  - concepts:cloud-economics
  - concepts:operations
  - concepts:scalability
  - concepts:performance
  - concepts:best-practices
  - concepts:architecture
level: intermediate
category: cloud
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:architects
---
<!-- course: cloud_cost_optimization -->
# Cloud Cost Optimization

## Description
Cloud bills tend to grow quietly for years until somebody finally adds them up. Engineers are usually the only
people who can do anything about it, but they are rarely taught how. This five day course is a hands-on, technical
course on reducing cloud spend without breaking systems or slowing development.

The course is engineer-facing rather than finance-facing. It covers cost models for the major cloud providers,
practical tactics for compute, storage, networking, data and `AI` workloads, the architectural patterns that scale
economically, observability and showback for cost, and the lightweight `FinOps` practices that engineering teams
can adopt without standing up a separate function. Examples are drawn from `AWS`, `GCP` and `Azure`. Participants
leave able to `find` waste in their own infrastructure, prioritize the high-impact fixes, and build the habits that
keep costs from creeping back.

## Duration
40 hours / 5 days

## Intended Audience
* developers and `SREs` whose teams are responsible for their own cloud bill
* tech leads and architects designing systems on the cloud with a cost lens
* `DevOps` engineers operating cloud infrastructure
* engineers tasked with a cost-reduction initiative

## Prerequisites
* working knowledge of at least one cloud provider (`AWS`, `GCP` or `Azure`)
* basic familiarity with containers, virtual machines and `cloud storage`
* some experience operating production workloads

## Objectives
* read and reason about a cloud bill at the resource level
* identify the high-impact waste in a typical cloud environment
* apply rightsizing, scheduling and lifecycle tactics across compute and storage
* design architectures that scale economically and not just technically
* exploit commitment-based discounts (reserved, savings plans, committed use)
* reduce data egress and inter-zone networking costs
* set up cost observability with showback and budget alerts
* build cost-awareness into engineering practice without bureaucracy

## Outline
<!-- chapter: how-cloud-providers-charge-you, duration: 3h -->
* How cloud providers charge you
    * the dimensions of cost: compute, storage, networking, data, services
    * the cost model differences between `AWS`, `GCP` and `Azure`
    * on-demand, reserved, savings plan, committed use, spot
    * billing granularity and the gap between resources and bills
    * support, premium tiers and "soft" costs
    * where the hidden costs live
<!-- chapter: reading-and-attributing-the-bill, duration: 2h -->
* Reading and attributing the bill
    * the `AWS` Cost and Usage Report
    * `GCP` billing export to `BigQuery`
    * `Azure` Cost Management exports
    * tagging and labeling discipline
    * showback and chargeback models
    * cost per team, service, customer
<!-- chapter: rightsizing-compute, duration: 3h -->
* Rightsizing compute
    * `EC2`, `Compute Engine`, `Azure VM` instance families
    * recognizing over-provisioned instances
    * automated recommendations and their limits
    * `ARM`/`Graviton` and similar architecture switches
    * `Kubernetes` request and limit tuning
    * vertical pod autoscaling
    * cost of right-sizing badly
<!-- chapter: autoscaling-and-scheduling, duration: 3h -->
* Autoscaling and scheduling
    * horizontal vs vertical autoscaling
    * scaling on `CPU` vs custom metrics
    * `Kubernetes` `HPA`, `VPA`, `Cluster Autoscaler`, `Karpenter`
    * scaling down to zero `when` possible
    * dev/test environment scheduling
    * batch and `async` workloads off-peak
<!-- chapter: spot-and-preemptible-compute, duration: 2h -->
* Spot and preemptible compute
    * spot pricing dynamics
    * fault-tolerant workloads and spot
    * spot fleets and diversification
    * `Kubernetes` on spot nodes
    * stateful workloads on spot
    * cost vs reliability trade-offs
<!-- chapter: commitment-based-discounts, duration: 2h -->
* Commitment-based discounts
    * reserved instances, savings plans, committed use discounts
    * choosing term length and coverage
    * convertible vs standard reservations
    * the marketplace for unused commitments
    * managing commitments at portfolio level
    * common commitment mistakes
<!-- chapter: storage-cost-optimization, duration: 3h -->
* Storage cost optimization
    * object storage tiers: standard, infrequent access, archive, deep archive
    * lifecycle policies and intelligent tiering
    * `EBS`/`Persistent Disk` types and their cost
    * snapshot management and orphan cleanup
    * compression, deduplication, columnar formats
    * deleting data you do not need
<!-- chapter: data-and-database-costs, duration: 3h -->
* Data and database costs
    * managed database pricing models
    * read-replica costs and right-sizing
    * `RDS`/`Aurora`, `Cloud SQL`, `Azure SQL` cost dynamics
    * `DynamoDB`, `BigTable` provisioned vs on-demand
    * data warehouse cost (`BigQuery`, `Redshift`, `Snowflake`)
    * partition pruning and query optimization for cost
    * storage vs compute separation in modern warehouses
<!-- chapter: networking-and-egress-costs, duration: 3h -->
* Networking and egress costs
    * the egress price structure across clouds
    * inter-zone, inter-region and inter-cloud transfer
    * `NAT` gateway costs
    * `CloudFront`/`Cloud CDN`/`Azure CDN` for offload
    * `VPC` endpoints and `PrivateLink`
    * architectural patterns to reduce data movement
<!-- chapter: cost-of-managed-services, duration: 2h -->
* Cost of managed services
    * the build vs rent calculus
    * recognizing expensive convenience services
    * `Lambda`/`Cloud Functions` cost models
    * `API Gateway`, `Cloud Run`, `App Service`
    * service-specific pricing pitfalls
    * `when` managed is worth it and `when` it is not
<!-- chapter: cost-of-ai-and-gpu-workloads, duration: 3h -->
* Cost of `AI` and `GPU` workloads
    * `GPU` instance pricing
    * inference cost optimization: batching, caching, distillation
    * `LLM` `API` token cost engineering
    * managed `ML` services vs self-hosted
    * spot `GPUs` for training
    * `GPU` utilization as the dominant lever
<!-- chapter: kubernetes-cost-optimization, duration: 3h -->
* `Kubernetes` cost optimization
    * the `Kubernetes` cost gap problem
    * cost allocation per namespace, pod, label
    * `OpenCost`, `Kubecost`, native cloud allocation
    * bin-packing and node selection
    * `Karpenter` for cost-aware provisioning
    * cluster consolidation
<!-- chapter: architectural-patterns-for-cost, duration: 3h -->
* Architectural patterns for cost
    * scale-to-zero designs
    * caching aggressively at every layer
    * `async` over sync where possible
    * the right service for the workload
    * regional design and data locality
    * multi-region cost trade-offs
<!-- chapter: cost-observability-and-budgets, duration: 2h -->
* Cost observability and budgets
    * cost dashboards that engineers actually look at
    * budget alerts and forecasting
    * anomaly detection on spend
    * tying cost to deploy events
    * `SLO`-style cost objectives
<!-- chapter: finops-without-the-bureaucracy, duration: 2h -->
* `FinOps` without the bureaucracy
    * the lightweight engineering version of `FinOps`
    * cost as a non-functional requirement
    * the cost review meeting
    * embedding cost into design review
    * keeping cost from rebounding after a cleanup
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * audit walkthrough of a sample cloud account
    * prioritization exercise: which fixes matter most
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
