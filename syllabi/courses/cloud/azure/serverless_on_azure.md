---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - concepts:architecture
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: serverless_on_azure -->
# Serverless on `Azure`

## Description
This course covers the serverless computing landscape on `Microsoft Azure`. Participants will
learn to build event-driven, scalable applications using `Azure Functions`, `Logic Apps`, and
supporting services. The course addresses integration with `Azure` data and messaging services,
security best practices, monitoring, `CI/CD`, and cost management for serverless workloads.

## Duration
24 hours / 3 days

## Intended Audience
* developers building cloud-native applications on `Azure`.
* developers looking to adopt serverless architecture patterns.
* backend engineers seeking to reduce infrastructure management overhead.

## Prerequisites
* basic understanding of `cloud computing` concepts.
* experience with at least one programming language (`C#`, `JavaScript`, `Python`, or `Java`).
* familiarity with the `Azure` portal is helpful.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* understand serverless architecture principles on `Azure`.
* build and deploy applications using `Azure Functions` and `Logic Apps`.
* integrate serverless workloads with `Azure` messaging and data services.
* implement security, monitoring, and `CI/CD` for serverless applications.

## Outline
<!-- chapter: azure-serverless-overview, duration: 1h -->
* `Azure` serverless overview
    * what is serverless on `Azure`
    * serverless portfolio and service landscape
    * choosing the right serverless option
    * serverless `design patterns`
<!-- chapter: azure-functions, duration: 2h -->
* `Azure Functions`
    * triggers and bindings
    * `HTTP` triggers, timer triggers, queue triggers
    * input and output bindings
    * function app hosting plans (consumption, premium, dedicated)
    * local development and debugging
<!-- chapter: durable-functions, duration: 2h -->
* `Durable Functions`
    * orchestrations and activity functions
    * function chaining
    * fan-out/fan-in pattern
    * human interaction pattern
    * monitoring pattern
    * eternal orchestrations
<!-- chapter: azure-logic-apps, duration: 2h -->
* `Azure Logic Apps`
    * visual workflow designer
    * connectors and triggers
    * standard vs consumption plans
    * integration with `Azure Functions`
    * enterprise integration patterns
<!-- chapter: event-and-messaging-services, duration: 2h -->
* Event and messaging services
    * `Azure Event Grid`
    * `Azure Service Bus` (queues and topics)
    * event-driven architectures on `Azure`
    * choosing between `Event Grid`, `Service Bus`, and `Event Hubs`
<!-- chapter: api-management, duration: 2h -->
* `API` management
    * `Azure API Management`
    * policies and transformations
    * rate limiting and authentication
    * developer portal
<!-- chapter: data-services, duration: 1h -->
* Data services
    * `Cosmos DB` serverless tier
    * `Azure SQL` serverless
    * data modeling for serverless applications
<!-- chapter: azure-static-web-apps, duration: 2h -->
* `Azure Static Web Apps`
    * integrated hosting for static frontends
    * `API` backends with `Azure Functions`
    * authentication providers
    * staging environments
<!-- chapter: azure-container-apps, duration: 2h -->
* `Azure Container Apps`
    * serverless containers
    * scaling rules and KEDA
    * Dapr integration
    * comparison with `Azure Functions`
<!-- chapter: azure-signalr-service, duration: 1h -->
* `Azure SignalR Service`
    * real-time messaging in serverless apps
    * serverless mode
    * integration with `Azure Functions`
<!-- chapter: monitoring-and-security, duration: 2h -->
* Monitoring and security
    * `Application Insights` integration
    * distributed tracing
    * managed identities
    * `Key Vault` integration
    * network security and private endpoints
<!-- chapter: ci-cd-for-serverless, duration: 2h -->
* `CI/CD` for serverless
    * deployment with `Azure DevOps`
    * deployment with `GitHub Actions`
    * infrastructure as code with Bicep
    * deployment slots and blue-green deployments
<!-- chapter: cost-management, duration: 2h -->
* Cost management
    * pricing models across serverless services
    * cost analysis and budgets
    * optimization strategies
    * reserved capacity considerations
<!-- chapter: comparison-of-azure-serverless-options, duration: 1h -->
* Comparison of `Azure` serverless options
    * `Azure Functions` vs `Container Apps` vs `Logic Apps`
    * decision framework
    * migration considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
