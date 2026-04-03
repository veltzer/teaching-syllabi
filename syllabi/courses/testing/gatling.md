---
tags:
  - tools:gatling
  - practices:load-testing
  - practices:performance-testing
  - languages:scala
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:qa-engineers
  - audiences:devops
---
<!-- course: gatling -->
# `Gatling`

## Description
This course covers `Gatling`, a powerful open-source load testing tool built on `Scala` and the Akka actor model, designed for high-concurrency simulation at scale. Students will learn to structure realistic simulations, configure the `HTTP` protocol, model user behaviour with scenarios and feeders, and validate results with assertions and automated reports. Advanced topics include request chaining, session variables, dynamic data injection, distributed testing, and the managed `Gatling Enterprise` platform. Participants will gain practical skills to run production-grade performance tests and integrate them into `continuous delivery` workflows.

## Duration
16 hours / 2 days

## Intended Audience
* Backend developers and QA engineers responsible for service performance
* `DevOps` engineers who need to add performance gates to `CI/CD` pipelines
* Teams running `JVM`-based systems who want a code-first load testing approach

## Prerequisites
* Basic familiarity with the `JVM` ecosystem and `Maven` or `sbt`
* Working knowledge of `HTTP` and `REST` APIs
* No prior `Scala` experience is required, though basic familiarity is helpful

## Objectives
* Explain `Gatling`'s architecture and advantages over thread-based load tools
* Install `Gatling` and set up a simulation project with `Maven` or `sbt`
* Write simulations using the `Gatling` DSL for scenarios and virtual users
* Configure `HTTP` protocol settings including base URL, headers, and authentication
* Use feeders and session variables to inject and manage test data
* Define assertions to enforce SLA compliance in automated runs
* Interpret `Gatling`'s `HTML` reports and identify performance regressions
* Build advanced simulations with conditional logic and loops
* Run distributed load tests using `Gatling Enterprise`
* Integrate `Gatling` into `CI/CD` pipelines with failure gates

## Outline
<!-- chapter: introduction-to-gatling, duration: 1h -->
* Introduction to `Gatling`
    * Why `Gatling`: reactive architecture and non-blocking `I/O`
    * `Gatling` vs `k6`, `JMeter`, and `Locust`
    * Core concepts: simulation, scenario, virtual user, injection profile
    * Overview of the `Gatling` DSL and `Scala` syntax basics
    * Setting expectations for the course
<!-- chapter: installation-and-project-setup, duration: 1h -->
* Installation and Project Setup
    * Installing the `Gatling` bundle
    * `Maven` archetype and `sbt` project setup
    * Project directory structure: simulations, resources, results
    * Running a simulation from the command line
    * IDE setup: `IntelliJ IDEA` with the `Scala` plugin
    * Using the `Gatling` Recorder to generate initial simulations
<!-- chapter: simulation-structure, duration: 2h -->
* Simulation Structure
    * Anatomy of a `Gatling` simulation class
    * Extending `Simulation` and defining `setUp`
    * The `ScenarioBuilder` and chaining request steps
    * `exec`, `pause`, and `group` building blocks
    * Conditional and loop constructs: `doIf`, `repeat`, `foreach`, `asLongAs`
    * Organising simulations into reusable objects and traits
<!-- chapter: http-protocol-configuration, duration: 2h -->
* `HTTP` Protocol Configuration
    * Defining `httpProtocol` with `HttpProtocolBuilder`
    * Base URL, connection pools, and keep-alive settings
    * Default headers and request compression
    * Automatic cookie and cache management
    * Following redirects and handling `HTTPS`
    * Proxy configuration for traffic inspection
<!-- chapter: scenarios-and-feeders, duration: 2h -->
* Scenarios and Feeders
    * Injection profiles: `atOnceUsers`, `rampUsers`, `constantUsersPerSec`, `rampUsersPerSec`
    * Combining multiple injection profiles
    * Session variables: reading, writing, and transforming with `EL` expressions
    * Built-in feeders: `CSV`, `JSON`, `JDBC`, `Redis`
    * Custom feeder implementations
    * Feeder strategies: queue, random, shuffle, circular
    * Sharing feeder data across virtual users
<!-- chapter: assertions-and-reports, duration: 2h -->
* Assertions and Reports
    * The `Assertions` `API`: global, per-request, per-group
    * Asserting on response time percentiles, mean, and max
    * Asserting on success rate and request count
    * Failing CI builds `when` assertions are not met
    * Understanding the `Gatling` `HTML` report structure
    * Request statistics, response time distribution, and active users chart
    * Exporting results to external monitoring systems
<!-- chapter: advanced-request-building, duration: 2h -->
* Advanced Request Building
    * Capturing values from responses with `check` and `saveAs`
    * `JSON` path and XPath extraction
    * Regex and `CSS` selectors in checks
    * Multi-part form data and `file` upload requests
    * Request chaining with extracted session values
    * Managing authentication: Basic Auth, Bearer tokens, `OAuth 2.0`
    * Handling query parameters, form parameters, and request bodies dynamically
<!-- chapter: distributed-testing, duration: 2h -->
* Distributed Testing
    * Limitations of single-node load generation
    * Running `Gatling` on multiple nodes manually
    * Aggregating results from distributed runs
    * Containerising `Gatling` with `Docker`
    * Running simulations on `Kubernetes`
    * Resource sizing and worker node requirements
<!-- chapter: gatling-enterprise, duration: 1h -->
* `Gatling Enterprise`
    * `Gatling Enterprise` architecture and managed infrastructure
    * Uploading and managing simulation packages
    * Scheduling and running simulations in the cloud
    * Real-time monitoring and trend dashboards
    * Team management and access control
    * Comparing the open-source and enterprise feature sets
<!-- chapter: integration-with-cicd, duration: 1h -->
* Integration with `CI/CD`
    * Running `Gatling` in `GitHub Actions` and `GitLab CI`
    * `Maven` and `sbt` plugin configuration for automated runs
    * Passing environment variables for target URL and load profile
    * Archiving `HTML` reports as build artefacts
    * Enforcing performance gates with assertion exit codes
    * Scheduling regular regression performance tests

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
