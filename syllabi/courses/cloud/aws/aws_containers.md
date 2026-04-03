---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - infrastructure:containers
  - infrastructure:kubernetes
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:devops
  - audiences:developers
  - audiences:sres
---
<!-- course: aws_containers -->
# `AWS` Containers (`ECS`/`EKS`)

## Description
This course covers container orchestration on `AWS`, focusing on both `Amazon ECS`
and `Amazon EKS`. Participants will learn how to build, deploy, and manage
containerized applications using `AWS` container services including Fargate,
`ECR`, and `App Mesh`. The course covers service discovery, load balancing,
auto-scaling, monitoring, and `CI/CD` pipelines for container workloads on `AWS`.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers responsible for deploying and managing containerized workloads on `AWS`.
* Developers building and shipping containerized applications on `AWS`.
* Site reliability engineers managing container infrastructure at scale.

## Prerequisites
* Basic knowledge of `Docker` and containerization concepts.
* Familiarity with `AWS` core services (`EC2`, `VPC`, `IAM`).
* Basic understanding of networking concepts.

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* Deploy and manage containerized applications using `Amazon ECS` and `Amazon EKS`.
* Configure Fargate for serverless container workloads.
* Build and manage container images with `Amazon ECR`.
* Implement service mesh, service discovery, and load balancing for container services.
* Set up auto-scaling and monitoring for containerized applications.
* Design and implement `CI/CD` pipelines for container deployments on `AWS`.

## Outline
<!-- chapter: introduction-to-containers-on-aws, duration: 2h -->
* Introduction to Containers on `AWS`
    * Overview of container services on `AWS`
    * Choosing between `ECS` and `EKS`
    * Container networking fundamentals on `AWS`
<!-- chapter: amazon-ecr, duration: 2h -->
* `Amazon ECR`
    * Creating and managing repositories
    * Image scanning and lifecycle policies
    * Cross-region and cross-account replication
<!-- chapter: amazon-ecs, duration: 2h -->
* `Amazon ECS`
    * Task definitions and task placement strategies
    * Services and service schedulers
    * `ECS` cluster management
    * `ECS` networking modes
<!-- chapter: aws-fargate, duration: 2h -->
* `AWS Fargate`
    * Serverless container execution
    * Fargate task configuration
    * Fargate Spot for cost optimization
    * Comparing Fargate with `EC2` launch type
<!-- chapter: amazon-eks, duration: 2h -->
* `Amazon EKS`
    * `EKS` cluster setup and configuration
    * Managed node groups and Fargate profiles
    * `EKS` networking with `Amazon VPC CNI`
    * `EKS` add-ons and `Kubernetes` operators
<!-- chapter: service-discovery-and-load-balancing, duration: 2h -->
* Service Discovery and Load Balancing
    * `AWS Cloud Map` for service discovery
    * Application Load Balancer integration
    * Network Load Balancer for high-performance workloads
    * Target group configuration for containers
<!-- chapter: aws-app-mesh, duration: 3h -->
* `AWS App Mesh`
    * Service mesh concepts and architecture
    * Virtual services, virtual nodes, and virtual routers
    * Traffic management and routing policies
    * Observability with `App Mesh`
<!-- chapter: auto-scaling, duration: 3h -->
* Auto-Scaling
    * `ECS` service auto-scaling
    * `EKS` Cluster Autoscaler and Karpenter
    * Scaling based on custom metrics
    * Capacity providers
<!-- chapter: monitoring-and-logging, duration: 3h -->
* Monitoring and Logging
    * `Amazon CloudWatch` Container Insights
    * `AWS X-Ray` for distributed tracing
    * Logging strategies with `CloudWatch Logs` and FireLens
    * `Prometheus` and `Grafana` on `EKS`
<!-- chapter: ci-cd-for-containers, duration: 3h -->
* `CI/CD` for Containers
    * `AWS CodePipeline` and CodeBuild for container workflows
    * Blue/green and canary deployments
    * `GitOps` with `Flux` and `ArgoCD` on `EKS`
    * Image promotion across environments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
