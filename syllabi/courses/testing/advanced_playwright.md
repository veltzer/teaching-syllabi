---
tags:
  - practices:testing
  - practices:automation
  - concepts:web-development
level: advanced
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
  - audiences:devops
---
<!-- course: advanced_playwright -->
# Advanced `Playwright`

## Description
This two day advanced course takes participants beyond the basics of `Playwright` into production-grade testing patterns. Topics include the page object model, visual regression testing, `API` testing, network interception, parallel execution, custom fixtures, `CI/CD` integration, mobile emulation, and accessibility testing.

## Duration
16 hours / 2 days

## Intended Audience
* Automation engineers looking to deepen their `Playwright` expertise
* Developers responsible for end-to-end testing
* QA engineers transitioning to advanced test automation

## Prerequisites
* Basic experience with `Playwright` or similar browser automation tools
* Proficiency in `TypeScript` or `JavaScript`
* Understanding of `HTML`, `CSS`, and web application architecture

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Design maintainable test suites using the page object model.
* Implement visual regression testing workflows.
* Test APIs and intercept network requests within `Playwright`.
* Configure parallel execution and custom fixtures for scalable test runs.
* Integrate `Playwright` tests into `CI/CD` pipelines.
* Emulate mobile devices and perform accessibility audits.

## Outline
<!-- chapter: page-object-model, duration: 1h -->
* Page Object Model
    * Structuring page objects for maintainability
    * Encapsulating selectors and actions
    * Composing page objects for complex flows
    * Managing shared state between page objects
<!-- chapter: visual-regression-testing, duration: 1h -->
* Visual Regression Testing
    * Screenshot comparison strategies
    * Configuring visual thresholds and baselines
    * Handling dynamic content in visual tests
    * Integrating visual reports into review workflows
<!-- chapter: api-testing-with-playwright, duration: 2h -->
* `API` Testing with `Playwright`
    * Using APIRequestContext for direct `API` calls
    * Combining `API` and UI tests in a single scenario
    * Validating response schemas and payloads
    * Authentication via `API` for test setup
<!-- chapter: network-interception, duration: 2h -->
* Network Interception
    * Mocking and stubbing network requests
    * Intercepting and modifying responses
    * Simulating error conditions and latency
    * Recording and replaying network traffic
<!-- chapter: parallel-execution, duration: 2h -->
* Parallel Execution
    * Configuring workers and sharding
    * Managing test isolation and shared resources
    * Strategies for reducing flakiness in parallel runs
    * Distributing tests across multiple machines
<!-- chapter: custom-fixtures, duration: 2h -->
* Custom Fixtures
    * Creating reusable test fixtures
    * Fixture scoping and lifecycle management
    * Parameterized fixtures for data-driven testing
    * Composing fixtures for complex setups
<!-- chapter: ci-cd-integration, duration: 2h -->
* `CI/CD` Integration
    * Running `Playwright` in `Docker` containers
    * Configuring `GitHub Actions`, `GitLab CI`, and `Jenkins`
    * Managing test artifacts and reports
    * Retry strategies and failure notifications
<!-- chapter: mobile-emulation, duration: 2h -->
* Mobile Emulation
    * Configuring device profiles and viewports
    * Touch events and gesture simulation
    * Testing responsive layouts across breakpoints
    * Geolocation, locale, and permission emulation
<!-- chapter: accessibility-testing, duration: 2h -->
* Accessibility Testing
    * Automated accessibility audits with axe-core
    * WCAG compliance validation
    * Keyboard navigation testing
    * Integrating accessibility checks into test pipelines

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
