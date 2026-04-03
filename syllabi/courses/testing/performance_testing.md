---
tags:
  - practices:testing
  - practices:performance
  - practices:load-testing
  - practices:benchmarking
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
  - audiences:architects
  - audiences:devops
  - audiences:sres
---
<!-- course: performance_testing -->
# Performance Testing

## Description
This course provides a focused introduction to performance testing, covering load testing, profiling, benchmarking, and capacity planning. Students will gain hands-on experience with industry tools such as `k6`, `Locust`, and `Gatling`, and learn how to define and validate SLAs, identify bottlenecks, and ensure applications meet performance requirements under realistic conditions.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers responsible for application performance
* QA engineers and test automation specialists
* `DevOps` and SRE engineers
* Performance engineers and architects

## Prerequisites
* Basic software development experience in at least one programming language
* Understanding of `HTTP` protocol and web application architecture
* Familiarity with command-line tools
* Basic understanding of monitoring concepts

## Objectives
* Understand performance testing types: load, stress, endurance, spike, and scalability
* Design performance test plans with meaningful metrics and acceptance criteria
* Write and execute load tests using `k6`, `Locust`, and `Gatling`
* Profile applications to identify performance bottlenecks
* Establish benchmarks and track performance over time
* Apply capacity planning techniques based on test results
* Define, validate, and report against SLAs

## Outline
<!-- chapter: performance-testing-fundamentals, duration: 1h -->
* Performance Testing Fundamentals
    * What is performance testing and why it matters
    * Performance testing vs functional testing
    * Types of performance tests: load, stress, endurance, spike, scalability
    * Key metrics: response time, throughput, error rate, latency
    * Understanding percentiles: p50, p90, p95, p99
    * Common performance anti-patterns
<!-- chapter: slas-slos-and-slis, duration: 1h -->
* SLAs, SLOs, and SLIs
    * Defining Service Level Agreements
    * Service Level Objectives and Service Level Indicators
    * Mapping business requirements to performance targets
    * Monitoring SLA compliance
    * Reporting and alerting on SLA breaches
<!-- chapter: load-testing-with-k6, duration: 2h -->
* Load Testing with `k6`
    * `k6` architecture and execution model
    * Writing test scripts in `JavaScript`
    * Virtual users, iterations, and scenarios
    * Thresholds and pass/fail criteria
    * Checks for response validation
    * Executors: constant VUs, ramping VUs, constant arrival rate
    * Custom metrics and data parameterization
<!-- chapter: load-testing-with-locust, duration: 1h -->
* Load Testing with `Locust`
    * `Locust` architecture and distributed mode
    * Writing test scripts in `Python`
    * User classes and task sets
    * Weight distribution and wait times
    * Custom event hooks and listeners
    * Web UI for real-time monitoring
<!-- chapter: load-testing-with-gatling, duration: 2h -->
* Load Testing with `Gatling`
    * `Gatling` architecture and recorder
    * `Scala` DSL for simulation scripts
    * Scenario building and injection profiles
    * Feeders for test data
    * Checks, assertions, and reports
    * Throttling and pacing strategies
<!-- chapter: profiling, duration: 2h -->
* Profiling
    * `CPU` profiling and flame graphs
    * Memory profiling and allocation tracking
    * Thread dump analysis and concurrency issues
    * Garbage collection analysis
    * Database query profiling and execution plans
    * Network latency and throughput analysis
    * Correlating profiles with load test results
<!-- chapter: benchmarking, duration: 2h -->
* Benchmarking
    * Establishing performance baselines
    * Micro-benchmarking vs macro-benchmarking
    * Benchmarking tools and methodologies
    * Avoiding common benchmarking pitfalls
    * Tracking benchmarks over time
    * Regression detection and trend analysis
<!-- chapter: capacity-planning, duration: 2h -->
* Capacity Planning
    * Capacity planning methodology
    * Extrapolating from load test results
    * Vertical vs horizontal scaling analysis
    * Resource utilization modeling
    * Predicting growth and planning for peak load
    * Cost optimization through right-sizing
    * Auto-scaling validation and testing
<!-- chapter: identifying-and-resolving-bottlenecks, duration: 1h -->
* Identifying and Resolving Bottlenecks
    * `CPU`, memory, `I/O`, and network bottlenecks
    * Database bottlenecks: slow queries, connection pools, locks
    * Application-level bottlenecks: thread pools, caching, serialization
    * Operating system limits and tuning
    * Infrastructure and cloud resource constraints
<!-- chapter: reporting-and-ci-integration, duration: 2h -->
* Reporting and CI Integration
    * Performance test reports: structure and content
    * Visualizing results with `Grafana` and dashboards
    * Automated performance testing in `CI/CD` pipelines
    * Performance gates and quality thresholds
    * Comparing results across test runs
    * Communicating findings to stakeholders

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
