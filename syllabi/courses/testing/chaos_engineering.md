---
tags:
  - practices:testing
  - practices:sre
  - concepts:distributed-systems
level: advanced
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sres
---
<!-- course: chaos_engineering -->
# Chaos Engineering

## Description
Chaos engineering is the discipline of experimenting on distributed systems to build confidence in their ability to withstand turbulent conditions in production. This course covers the principles and practices of chaos engineering, from foundational concepts to hands-on experience with tools like `Chaos Monkey`, `Litmus Chaos`, `Chaos Mesh`, and Gremlin. Participants will learn how to design and run chaos experiments, inject various types of failures, observe system behavior under stress, and integrate chaos practices into their development lifecycle.

## Duration
16 hours / 2 days

## Intended Audience
* Backend and platform developers building distributed systems
* `DevOps` and SRE engineers responsible for system reliability
* Infrastructure engineers managing `Kubernetes` and cloud environments
* Technical leads driving reliability and resilience initiatives

## Prerequisites
* Experience with distributed systems or `microservices` architectures
* Familiarity with `Kubernetes` and container orchestration
* Basic understanding of monitoring and observability tools
* Experience with `CI/CD` pipelines
* Comfort with command-line tools and scripting

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)

## Objectives
* Understand the principles and goals of chaos engineering
* Design chaos experiments with a steady state `hypothesis` and controlled blast `radius`
* Use `Chaos Monkey`, `Litmus Chaos`, `Chaos Mesh`, and Gremlin to inject failures
* Simulate network chaos with toxiproxy
* Inject failures including pod kills, network latency, disk pressure, and `CPU` stress
* Observe system behavior during chaos using monitoring and observability tools
* Integrate chaos experiments into `CI/CD` pipelines
* Drive organizational adoption of chaos engineering practices

## Outline
<!-- chapter: chaos-engineering-principles, duration: 1h -->
* Chaos Engineering Principles
    * What is chaos engineering and why it matters
    * The Principles of Chaos Engineering manifesto
    * Building confidence in system resilience
    * Chaos engineering vs traditional testing
    * Real-world examples of chaos engineering successes
    * The relationship between chaos engineering and SRE
<!-- chapter: designing-chaos-experiments, duration: 1h -->
* Designing Chaos Experiments
    * Defining steady state `hypothesis`
    * Identifying the blast `radius`
    * Selecting experiment scope and target
    * Formulating hypotheses about system behavior
    * Planning rollback and safety nets
    * Documenting and communicating experiments
    * Running game days: collaborative chaos exercises
<!-- chapter: netflix-and-chaos-monkey, duration: 1h -->
* Netflix and `Chaos Monkey`
    * Netflix's journey to chaos engineering
    * `Chaos Monkey`: random instance termination
    * The `Simian Army`: `Latency Monkey`, `Conformity Monkey`, `Chaos Gorilla`
    * Lessons learned from Netflix's approach
    * Setting up and configuring `Chaos Monkey`
    * Adapting Netflix's practices to your organization
<!-- chapter: litmus-chaos, duration: 1h -->
* `Litmus Chaos`
    * `Litmus Chaos` overview and `Kubernetes`-native approach
    * Installing Litmus on a `Kubernetes` cluster
    * ChaosEngine, ChaosExperiment, and ChaosResult resources
    * Built-in experiment library: pod delete, container kill, network loss
    * Creating custom chaos experiments
    * Litmus portal for experiment management
    * Scheduling and automating experiments
<!-- chapter: chaos-mesh, duration: 1h -->
* `Chaos Mesh`
    * `Chaos Mesh` overview and architecture
    * Installing `Chaos Mesh` on `Kubernetes`
    * PodChaos, NetworkChaos, StressChaos, IOChaos types
    * The `Chaos Mesh` dashboard
    * Defining chaos workflows
    * Role-based access control for chaos experiments
    * Comparing `Chaos Mesh` with `Litmus Chaos`
<!-- chapter: aws-fault-injection-simulator, duration: 1h -->
* `AWS Fault Injection Simulator`
    * Overview of `AWS FIS` and managed chaos
    * Experiment templates and actions
    * Targeting `EC2`, `ECS`, `EKS`, and `RDS` resources
    * Stop conditions and safety guardrails
    * Integration with `CloudWatch` alarms
    * Running experiments across multiple `AWS` services
<!-- chapter: gremlin, duration: 2h -->
* Gremlin
    * Gremlin platform overview
    * Resource attacks: `CPU`, memory, disk, IO
    * Network attacks: latency, packet loss, `DNS`
    * State attacks: process kill, shutdown, time travel
    * Gremlin scenarios for multi-step experiments
    * Gremlin for `Kubernetes` and container environments
    * Enterprise features and team management
<!-- chapter: network-chaos-with-toxiproxy, duration: 1h -->
* Network Chaos with toxiproxy
    * toxiproxy overview and architecture
    * Installing and configuring toxiproxy
    * Simulating latency, bandwidth limits, and connection resets
    * toxiproxy client libraries for `Go`, `Python`, `Ruby`, `Java`
    * Integrating toxiproxy with integration tests
    * Network partition simulation
<!-- chapter: failure-injection-techniques, duration: 2h -->
* Failure Injection Techniques
    * Pod and container termination
    * Network latency and packet loss injection
    * Disk pressure and IO throttling
    * `CPU` and memory stress testing
    * `DNS` failures and resolution delays
    * Clock skew and time drift
    * Dependency unavailability simulation
<!-- chapter: observability-during-chaos, duration: 2h -->
* Observability During Chaos
    * Monitoring system behavior during experiments
    * Key metrics to watch: latency, error rate, throughput, saturation
    * Using `Prometheus`, `Grafana`, and `Datadog` during chaos
    * Distributed tracing to identify cascading failures
    * Alerting and on-call considerations during experiments
    * Capturing and analyzing experiment results
    * Building dashboards for chaos experiments
<!-- chapter: automated-chaos-and-ci-cd-integration, duration: 1h -->
* Automated Chaos and `CI/CD` Integration
    * Shifting chaos left: chaos in the development lifecycle
    * Running chaos experiments in `CI/CD` pipelines
    * Gating deployments on chaos experiment results
    * Continuous chaos: scheduled experiments in production
    * Chaos as code: version-controlled experiment definitions
    * Integration with `GitHub Actions`, `GitLab CI`, and `Jenkins`
<!-- chapter: organizational-adoption-and-safety, duration: 2h -->
* Organizational Adoption and Safety
    * Building a chaos engineering culture
    * Starting small and scaling gradually
    * Getting buy-in from leadership and teams
    * Safety nets and abort conditions
    * Rollback strategies and automatic recovery
    * Incident response integration
    * Maturity model for chaos engineering adoption
    * Communicating results and building confidence

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
