---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:architecture
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: aws_lambda_and_serverless -->
# `AWS Lambda` and Serverless

## Description
This course provides a deep dive into serverless computing on `Amazon Web Services`, with a primary focus on `AWS Lambda` and its surrounding ecosystem. Participants will learn to design, build, deploy, and operate serverless applications using a variety of `AWS` services. The course covers event-driven architectures, orchestration, monitoring, security, and cost optimization, giving participants the skills to build production-ready serverless solutions.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building cloud-native applications on `AWS`
* Architects designing serverless and event-driven systems

## Prerequisites
* Working knowledge of at least one programming language (`Python`, `Node.js`, or `Java`)
* Basic familiarity with `AWS` services (`IAM`, `S3`, `VPC`)
* Understanding of `REST` APIs and `HTTP` fundamentals
* Experience with command-line tools

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* Understand serverless computing concepts and the `AWS` serverless ecosystem
* Write, configure, and deploy `AWS Lambda` functions with runtimes, layers, versions, and aliases
* Build `REST` and `HTTP` APIs using `API Gateway`
* Design event-driven architectures with `S3`, EventBridge, `SQS`, and `SNS`
* Orchestrate serverless workflows using `Step Functions`
* Use `DynamoDB` as a serverless data store
* Define and deploy serverless infrastructure using SAM and CDK
* Monitor and trace serverless applications with `CloudWatch` and `X-Ray`
* Optimize serverless performance, including cold start mitigation
* Apply security best practices using `IAM` roles, policies, and `VPC` configurations
* Implement cost optimization strategies for serverless workloads

## Outline
<!-- chapter: introduction-to-serverless-computing, duration: 1h -->
* Introduction to Serverless Computing
    * What is Serverless?
    * Benefits and trade-offs of serverless architectures
    * Overview of the `AWS` serverless ecosystem
    * Serverless vs. containers vs. traditional compute
    * Common serverless use cases and patterns
<!-- chapter: aws-lambda-core-concepts, duration: 1h -->
* `AWS Lambda` - Core Concepts
    * `Lambda` execution model and lifecycle
    * Supported runtimes (`Python`, `Node.js`, `Java`, Go, `.NET`)
    * Writing and deploying `Lambda` functions
    * Memory, timeout, and concurrency configuration
    * Environment variables and configuration management
    * Execution context and reuse
<!-- chapter: aws-lambda-advanced-features, duration: 2h -->
* `AWS Lambda` - Advanced Features
    * `Lambda` Layers for shared code and dependencies
    * Function versions and aliases
    * Provisioned concurrency
    * `Lambda` extensions
    * Container image support
    * `Lambda` SnapStart for `Java`
<!-- chapter: api-gateway, duration: 2h -->
* `API Gateway`
    * `REST` APIs vs. `HTTP` APIs
    * Creating and configuring `API` endpoints
    * Request/response transformations
    * Authorization: `IAM`, Cognito, and `Lambda` authorizers
    * Throttling, caching, and usage plans
    * Custom domains and stage management
<!-- chapter: dynamodb-for-serverless, duration: 2h -->
* `DynamoDB` for Serverless
    * `DynamoDB` data modeling fundamentals
    * Partition keys, sort keys, and secondary indexes
    * On-demand vs. provisioned capacity
    * `DynamoDB Streams` and event processing
    * Single-table `design patterns`
    * Integration with `Lambda`
<!-- chapter: event-sources-and-triggers, duration: 2h -->
* Event Sources and Triggers
    * `S3` event notifications
    * EventBridge rules and event patterns
    * `SQS` as a `Lambda` event source
    * `SNS` notifications and fan-out patterns
    * `Kinesis Data Streams` integration
    * Event source mapping configuration
<!-- chapter: step-functions, duration: 2h -->
* `Step Functions`
    * Introduction to state machines
    * Standard vs. Express workflows
    * Task, Choice, Parallel, and Map states
    * Error handling and retries
    * Integration with `Lambda` and other `AWS` services
    * Workflow patterns for orchestration
<!-- chapter: sam-framework, duration: 2h -->
* SAM Framework
    * Introduction to the `Serverless Application Model`
    * SAM template anatomy
    * Local development and testing with `SAM CLI`
    * Packaging and deploying with SAM
    * SAM policy templates
    * `SAM Accelerate` for rapid iteration
<!-- chapter: cdk-for-serverless, duration: 2h -->
* CDK for Serverless
    * Introduction to the `AWS Cloud Development Kit`
    * Defining serverless infrastructure in code
    * L1, L2, and L3 constructs
    * Stacks and deployment
    * Testing infrastructure with CDK
    * Comparing SAM vs. CDK approaches
<!-- chapter: monitoring-and-observability, duration: 2h -->
* Monitoring and Observability
    * `CloudWatch` Logs and metrics for `Lambda`
    * Creating alarms and dashboards
    * `CloudWatch` Insights for log analysis
    * Distributed tracing with `X-Ray`
    * Instrumenting `Lambda` functions for tracing
    * Structured logging best practices
<!-- chapter: cold-starts-and-performance-optimization, duration: 2h -->
* Cold Starts and Performance Optimization
    * Understanding cold starts
    * Factors affecting cold start duration
    * Provisioned concurrency and warm-up strategies
    * Runtime and package size optimization
    * Memory tuning with `AWS Lambda Power Tuning`
    * Connection pooling and reuse patterns
<!-- chapter: security, duration: 2h -->
* Security
    * `Lambda` execution roles and `IAM` policies
    * Principle of least privilege for functions
    * `VPC`-attached `Lambda` functions
    * Secrets management with `Secrets Manager` and `Parameter Store`
    * `API` security and input validation
    * Encryption at `rest` and in transit
<!-- chapter: cost-optimization, duration: 2h -->
* Cost Optimization
    * `Lambda` pricing model
    * Monitoring and analyzing costs
    * Right-sizing memory and timeout
    * Choosing between on-demand and provisioned concurrency
    * Architectural patterns for cost efficiency
    * `AWS` `Cost Explorer` and budgets for serverless

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
