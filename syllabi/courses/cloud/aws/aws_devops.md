---
tags:
  - infrastructure:aws
  - infrastructure:cloud
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
<!-- course: aws_devops -->
# `DevOps` Engineering on `AWS`

## Description
This course covers `DevOps` principles and practices on the `AWS` platform. Participants will learn how
to build and manage `CI/CD` pipelines, automate infrastructure provisioning, implement monitoring and
logging strategies, and operate containerized workloads at scale. The course emphasizes automation,
infrastructure as code, and operational best practices for running production systems on `AWS`.

## Duration
32 hours / 4 days

## Intended Audience
* `DevOps` engineers building and maintaining `AWS` infrastructure
* System administrators transitioning to cloud operations
* Developers who want to automate deployment and operations workflows
* Site reliability engineers working with `AWS`

## Prerequisites
* Working experience with `Linux` command line and scripting
* Familiarity with `AWS` core services (`EC2`, `S3`, `VPC`, `IAM`)
* Basic experience with `Git` and version control
* Understanding of `CI/CD` concepts

## Objectives
* Design and implement `CI/CD` pipelines on `AWS`
* Automate infrastructure provisioning using infrastructure as code
* Implement comprehensive monitoring, logging, and alerting
* Manage containerized workloads with `Amazon ECS` and `Amazon EKS`
* Apply `DevOps` best practices for security, compliance, and cost management

## Outline
<!-- chapter: devops-culture-and-practices-on-aws, duration: 3h -->
* `DevOps` Culture and Practices on `AWS`
    * `DevOps` principles: automation, collaboration, measurement, sharing
    * `AWS` `DevOps` tools overview
    * Continuous integration, delivery, and deployment
    * Infrastructure as code philosophy
<!-- chapter: source-control-and-collaboration, duration: 3h -->
* Source Control and Collaboration
    * `AWS` CodeCommit
    * Branching strategies and code review workflows
    * Integration with `GitHub` and `GitLab`
    * Mono-repo vs multi-repo strategies
<!-- chapter: continuous-integration, duration: 3h -->
* Continuous Integration
    * `AWS` CodeBuild: build specifications and environments
    * Building and testing applications
    * Artifact management with `AWS` CodeArtifact
    * Container image builds and `Amazon ECR`
    * Security scanning in the build pipeline
<!-- chapter: continuous-delivery-and-deployment, duration: 3h -->
* `Continuous Delivery` and Deployment
    * `AWS` CodePipeline: stages, actions, and transitions
    * `AWS` `CodeDeploy`: in-place and blue/green deployments
    * Deployment strategies: rolling, canary, blue/green
    * Automated rollback and approval gates
    * Multi-account and multi-region deployments
<!-- chapter: infrastructure-as-code, duration: 3h -->
* Infrastructure as Code
    * `AWS CloudFormation`: templates, stacks, and change sets
    * `AWS` CDK for programmatic infrastructure definitions
    * `Terraform` on `AWS`
    * Managing secrets and parameters with `AWS` Systems Manager and `Secrets Manager`
    * Drift detection and compliance
<!-- chapter: container-operations, duration: 4h -->
* Container Operations
    * `Docker` on `AWS`
    * `Amazon ECS`: task definitions, services, and clusters
    * `Amazon EKS`: `Kubernetes` cluster management
    * `AWS` Fargate for serverless containers
    * Service mesh with `AWS` App Mesh
    * Container security and image scanning
<!-- chapter: monitoring-logging-and-observability, duration: 4h -->
* Monitoring, Logging, and Observability
    * `Amazon CloudWatch`: metrics, logs, alarms, and dashboards
    * `AWS CloudTrail` for `API` activity logging
    * `AWS` `X-Ray` for distributed tracing
    * Centralized logging architecture
    * Custom metrics and application-level monitoring
    * Alerting strategies and incident response
<!-- chapter: automation-and-configuration-management, duration: 3h -->
* Automation and Configuration Management
    * `AWS` Systems Manager: Run Command, Automation, and State Manager
    * Patch management and compliance
    * `AWS` OpsWorks and configuration management
    * Event-driven automation with `Amazon EventBridge`
    * `Lambda`-based automation
<!-- chapter: security-and-compliance-in-devops, duration: 3h -->
* Security and Compliance in `DevOps`
    * Secrets management and encryption
    * `IAM` policies and roles for `CI/CD` pipelines
    * `AWS` Config for compliance monitoring
    * Security Hub and GuardDuty
    * Automated security testing in pipelines
<!-- chapter: scaling-and-high-availability, duration: 3h -->
* Scaling and High Availability
    * `Auto Scaling` strategies for `EC2`, `ECS`, and `EKS`
    * Load balancing patterns
    * Multi-AZ and multi-region deployments
    * Disaster recovery automation
    * Cost optimization in `DevOps` workflows

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
