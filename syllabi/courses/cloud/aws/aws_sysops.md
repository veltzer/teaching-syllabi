---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:operations
level: intermediate
category: cloud
duration_hours: 32
audience:
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: aws_sysops -->
# `AWS` Systems Operations

## Description
This course covers the essential skills for operating and managing workloads on `AWS`. Students will learn how to monitor, automate, secure, and optimize `AWS` environments at scale. The course focuses on day-to-day operational tasks including monitoring and observability, configuration management, patch management, incident response, and cost control using native `AWS` services and best practices.

## Duration
32 hours / 4 days

## Intended Audience
* System administrators responsible for managing `AWS` infrastructure.
* `DevOps` engineers looking to deepen their operational expertise on `AWS`.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `VPC`, `IAM`).
* Basic understanding of `Linux` or `Windows` system administration.
* Familiarity with the `AWS` Management Console and `CLI`.

## Objectives
* Configure comprehensive monitoring and alerting with `CloudWatch`.
* Automate operational tasks using `AWS Systems Manager`.
* Manage `EC2` instances, storage, and networking at scale.
* Implement advanced `auto scaling` and load balancing strategies.
* Set up multi-account governance with `AWS Organizations`.
* Troubleshoot common operational issues and optimize costs.

## Outline
<!-- chapter: amazon-cloudwatch-monitoring-and-observability, duration: 3h -->
* `Amazon CloudWatch` Monitoring and Observability
    * `CloudWatch` metrics, namespaces, and custom metrics
    * Alarms, composite alarms, and alarm actions
    * `CloudWatch` dashboards and cross-account observability
    * `CloudWatch Logs` and `Logs Insights` queries
    * `CloudWatch` agent installation and configuration
    * Metric filters and subscription filters
    * `CloudWatch` anomaly detection
<!-- chapter: aws-cloudtrail-and-auditing, duration: 2h -->
* `AWS CloudTrail` and Auditing
    * Configuring multi-region trails
    * Log `file` integrity validation
    * Integration with `CloudWatch Logs` and `S3`
    * Querying `CloudTrail` events with `Athena`
    * Organizational trails
<!-- chapter: aws-config, duration: 2h -->
* `AWS Config`
    * Config rules and managed rules
    * Custom rules with `Lambda`
    * Conformance packs
    * Remediation actions and auto-remediation
    * Multi-account aggregation
<!-- chapter: aws-systems-manager, duration: 3h -->
* `AWS Systems Manager`
    * `Session Manager` for secure shell access
    * `Patch Manager` for automated patching
    * `Parameter Store` for configuration management
    * `Run Command` for remote execution at scale
    * `Automation` runbooks for operational workflows
    * `State Manager` for desired state configuration
    * `Inventory` and `Explorer` for fleet visibility
<!-- chapter: ec2-management, duration: 2h -->
* `EC2` Management
    * `AMI` creation, sharing, and lifecycle management
    * Instance types and selection strategies
    * Placement groups and tenancy options
    * Instance metadata and user data
    * Spot Instances, Reserved Instances, and Savings Plans
    * Troubleshooting instance connectivity and boot issues
<!-- chapter: ebs-and-storage-management, duration: 2h -->
* `EBS` and Storage Management
    * `EBS` volume types and performance characteristics
    * Snapshots, lifecycle policies, and cross-region copies
    * `EBS` encryption and key management
    * `EFS` and `FSx` operational management
    * Storage performance monitoring and optimization
<!-- chapter: networking-operations, duration: 2h -->
* Networking Operations
    * `VPC` flow logs analysis and troubleshooting
    * Network connectivity troubleshooting tools
    * `VPC Reachability Analyzer`
    * `DNS` resolution troubleshooting with `Route 53 Resolver`
    * Elastic `IP` management
    * Network performance monitoring
<!-- chapter: advanced-auto-scaling, duration: 3h -->
* Advanced `Auto Scaling`
    * `Auto Scaling` group lifecycle hooks
    * Scaling policies (target tracking, step, scheduled)
    * Predictive scaling
    * Instance warm pools
    * Mixed instance policies
    * Troubleshooting scaling events
<!-- chapter: advanced-elastic-load-balancing, duration: 3h -->
* Advanced `Elastic Load Balancing`
    * `ALB` advanced routing rules
    * `NLB` configuration and use cases
    * `SSL`/`TLS` termination and certificate management
    * Access logs and monitoring
    * Connection draining and target de-registration delay
    * Cross-zone load balancing
<!-- chapter: route-53-health-checks-and-dns-operations, duration: 2h -->
* `Route 53` Health Checks and `DNS` Operations
    * Health `check` types and configuration
    * Calculated health checks
    * `DNS` failover routing
    * `Route 53 Resolver` for hybrid environments
    * `DNS` query logging
<!-- chapter: aws-organizations-and-multi-account-management, duration: 2h -->
* `AWS Organizations` and Multi-Account Management
    * Organizational units and account hierarchy
    * Service control policies
    * Tag policies and backup policies
    * `AWS Control Tower` for landing zones
    * Consolidated billing and cost allocation
<!-- chapter: cost-optimization-and-trusted-advisor, duration: 3h -->
* Cost Optimization and `Trusted Advisor`
    * `AWS Cost Explorer` and cost allocation tags
    * `AWS Budgets` and alerts
    * `Trusted Advisor` checks and recommendations
    * `Compute Optimizer` for right-sizing
    * Reserved capacity planning
    * Cost anomaly detection
<!-- chapter: incident-response-and-troubleshooting, duration: 3h -->
* Incident Response and Troubleshooting
    * Building operational runbooks
    * Common failure scenarios and resolution steps
    * Service health dashboard and Personal Health Dashboard
    * `AWS Support` plans and case management
    * Post-incident review process
    * Automating incident response with `EventBridge` and `Lambda`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
