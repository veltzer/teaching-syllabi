---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:serverless
  - practices:devops
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: aws_developer -->
<!-- Track gaps: Cognito for application user management, Step Functions orchestration details, Kinesis data streaming -->
# `AWS` Developer

## Description
This course is designed for developers who want to build and deploy applications on `AWS`. It covers the core developer services and serverless technologies that enable modern cloud-native application development. Participants will learn how to use `Lambda`, `DynamoDB`, `API Gateway`, infrastructure-as-code tools like SAM and CDK, messaging services, orchestration with `Step Functions`, and observability with `X-Ray`.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers and engineers looking to build applications on `AWS`.
* Backend developers transitioning to serverless and cloud-native architectures.
* `DevOps` engineers who want a deeper understanding of `AWS` developer services.

## Prerequisites
* Experience in at least one programming language (`Python`, `JavaScript`, or `Java` recommended).
* Basic familiarity with `AWS` concepts (regions, `IAM`, `S3`).
* Experience with command-line tools and version control.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Build and deploy serverless applications using `AWS Lambda` and `API Gateway`.
* Design and interact with `DynamoDB` tables for scalable data storage.
* Define and deploy infrastructure using SAM and CDK.
* Implement asynchronous and event-driven architectures using `SQS`, `SNS`, and `Step Functions`.
* Instrument and debug applications using `AWS X-Ray`.

## Outline
<!-- chapter: introduction-to-aws-for-developers, duration: 2h -->
* Introduction to `AWS` for Developers
    * `AWS` developer ecosystem overview
    * `AWS` `CLI` and `SDK` setup
    * `IAM` roles and policies for developers
    * Development workflow best practices
<!-- chapter: aws-lambda, duration: 2h -->
* `AWS Lambda`
    * `Lambda` execution model and runtime lifecycle
    * Writing and deploying `Lambda` functions
    * Environment variables and configuration
    * `Lambda` layers and versioning
    * Error handling and retry behavior
    * Cold starts and performance optimization
<!-- chapter: amazon-dynamodb, duration: 2h -->
* `Amazon DynamoDB`
    * `DynamoDB` data modeling concepts
    * Partition keys, sort keys, and indexes
    * `CRUD` operations with the `AWS` `SDK`
    * Global and local secondary indexes
    * `DynamoDB` Streams
    * Capacity modes and auto-scaling
<!-- chapter: amazon-api-gateway, duration: 2h -->
* `Amazon API Gateway`
    * `REST` APIs and `HTTP` APIs
    * Request and response transformations
    * Authorization and authentication
    * Stages, deployments, and versioning
    * Throttling and usage plans
    * Integration with `Lambda`
<!-- chapter: aws-sam-serverless-application-model, duration: 2h -->
* `AWS SAM` (Serverless Application Model)
    * SAM template anatomy
    * Defining serverless resources
    * Local development and testing with SAM `CLI`
    * Building and deploying with SAM
    * SAM policy templates
<!-- chapter: aws-cdk-cloud-development-kit, duration: 2h -->
* `AWS CDK` (Cloud Development Kit)
    * CDK concepts and constructs
    * Defining infrastructure in code
    * Stacks and environments
    * CDK patterns and best practices
    * Synthesizing and deploying with CDK
    * Comparison with SAM and `CloudFormation`
<!-- chapter: amazon-sqs-simple-queue-service, duration: 2h -->
* `Amazon SQS` (Simple Queue Service)
    * Standard and FIFO queues
    * Message lifecycle and visibility timeout
    * Dead-letter queues
    * `Lambda` integration with `SQS`
    * Fan-out patterns
<!-- chapter: amazon-sns-simple-notification-service, duration: 2h -->
* `Amazon SNS` (Simple Notification Service)
    * Topics and subscriptions
    * Message filtering
    * `SNS` and `SQS` fan-out pattern
    * Push notifications and email delivery
    * Integration with `Lambda` and other services
<!-- chapter: aws-step-functions, duration: 3h -->
* `AWS Step Functions`
    * State machine concepts
    * Amazon States Language
    * Task, choice, parallel, and map states
    * Error handling and retries
    * Standard vs. Express workflows
    * Orchestrating `Lambda` functions and services
<!-- chapter: aws-x-ray, duration: 3h -->
* `AWS X-Ray`
    * Distributed tracing concepts
    * Instrumenting applications with the `X-Ray` `SDK`
    * Trace maps and service graphs
    * Analyzing latency and errors
    * Integration with `Lambda`, `API Gateway`, and other services
    * Sampling rules and configuration
<!-- chapter: putting-it-all-together, duration: 2h -->
* Putting It All Together
    * Designing event-driven architectures
    * `CI/CD` for serverless applications
    * Security best practices for serverless
    * Cost optimization strategies
    * Monitoring and operational excellence

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
