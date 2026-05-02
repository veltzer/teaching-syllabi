---
tags:
  - practices:testing
  - languages:javascript
  - concepts:web-development
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
---
<!-- course: cypress -->
# Cypress End-to-End Testing

## Description
Cypress is a modern, developer-friendly end-to-end testing framework that runs directly in the browser alongside your application. This course covers everything from basic test authoring to advanced topics like network interception, custom commands, and `CI/CD` integration. Participants will learn how to write reliable, fast, and maintainable tests for web applications using Cypress, and understand how it compares to other tools like `Playwright` and `Selenium`.

## Duration
16 hours / 2 days

## Intended Audience
* Frontend and full-stack developers building web applications
* QA engineers and test automation specialists
* Software developers responsible for end-to-end testing
* Teams adopting modern testing practices for web projects

## Prerequisites
* Proficiency in `JavaScript` or `TypeScript`
* Basic understanding of `HTML`, `CSS`, and the DOM
* Familiarity with web application architecture (client-server model)
* Basic command-line experience
* Understanding of `npm` or `yarn` package management

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Understand Cypress architecture and how it differs from traditional testing frameworks
* Install and configure Cypress for a web project
* Write end-to-end tests using selectors, assertions, and commands
* Interact with DOM elements and handle complex user interactions
* Test APIs directly using cy.request
* Create custom commands and implement the page object model
* Intercept and mock network requests with cy.intercept
* Integrate Cypress tests into `CI/CD` pipelines
* Use `Cypress Cloud` for dashboard analytics and parallelization
* Perform component testing and visual testing with Cypress

## Outline
<!-- chapter: cypress-overview-and-architecture, duration: 1h -->
* Cypress Overview and Architecture
    * What is Cypress and why it was created
    * Cypress architecture: running in the browser alongside the application
    * How Cypress differs from `Selenium`-based tools
    * Cypress test runner and command log
    * Supported browsers and limitations
    * The Cypress ecosystem: plugins, community, and documentation
<!-- chapter: installation-and-setup, duration: 1h -->
* Installation and Setup
    * Installing Cypress via `npm` or `yarn`
    * Project structure and configuration files (`cypress`.config.js)
    * Configuring base URL, viewports, and timeouts
    * Setting up `TypeScript` support
    * Environment variables and configuration overrides
    * Opening the Cypress test runner and running first tests
<!-- chapter: writing-tests-selectors-assertions-and-commands, duration: 1h -->
* Writing Tests: Selectors, Assertions, and Commands
    * Test file structure and organization
    * Selecting elements: cy.get, cy.contains, cy.find
    * Best practices for selectors: data-cy attributes
    * Assertions with should, expect, and assert
    * Chaining commands and understanding the command queue
    * Cypress automatic retry and timeout behavior
    * Using describe, it, before, beforeEach, after, afterEach
<!-- chapter: interacting-with-elements, duration: 1h -->
* Interacting with Elements
    * Clicking, typing, and clearing inputs
    * Working with dropdowns, checkboxes, and radio buttons
    * Handling file uploads
    * Drag and drop interactions
    * Scrolling and viewport manipulation
    * Working with iframes and shadow DOM
    * Handling alerts, confirmations, and prompts
<!-- chapter: api-testing-with-cy-request, duration: 1h -->
* `API` Testing with cy.request
    * Making `HTTP` requests directly from tests
    * Validating response status codes, headers, and bodies
    * Seeding data via `API` calls before tests
    * Authentication via `API` to bypass UI login
    * Chaining `API` requests for complex setup
<!-- chapter: fixtures-and-test-data, duration: 1h -->
* Fixtures and Test Data
    * Loading fixtures from `JSON` files
    * Using cy.fixture to inject test data
    * Dynamic data generation for tests
    * Managing test data across environments
    * Data cleanup strategies
<!-- chapter: custom-commands-and-the-page-object-model, duration: 1h -->
* Custom Commands and the Page Object Model
    * Creating custom commands with Cypress.Commands.add
    * Overwriting existing commands
    * Organizing custom commands in support files
    * Implementing the page object model in Cypress
    * Encapsulating page interactions and selectors
    * Reusable test helpers and utilities
<!-- chapter: intercepting-network-requests, duration: 1h -->
* Intercepting Network Requests
    * Introduction to cy.intercept
    * Stubbing responses for `API` calls
    * Waiting on network requests with cy.wait
    * Modifying request and response bodies
    * Simulating error responses and network failures
    * Asserting on request payloads
    * Intercepting `GraphQL` requests
<!-- chapter: waiting-retries-and-debugging, duration: 1h -->
* Waiting, Retries, and Debugging
    * Understanding Cypress automatic waiting
    * Configuring retry behavior and timeouts
    * Using cy.wait for explicit waits
    * Debugging with cy.debug and cy.pause
    * Using the browser developer tools with Cypress
    * Reading the command log for troubleshooting
    * Common pitfalls and flaky test prevention
<!-- chapter: screenshots-video-and-reporting, duration: 1h -->
* Screenshots, Video, and Reporting
    * Automatic screenshots on failure
    * Manual screenshots with cy.screenshot
    * Video recording of test runs
    * Configuring screenshot and video options
    * Integrating with reporting tools (Mochawesome, `JUnit`)
    * Generating `HTML` test reports
<!-- chapter: ci-cd-integration, duration: 2h -->
* `CI/CD` Integration
    * Running Cypress in headless mode
    * Integration with `GitHub Actions`
    * Integration with `GitLab CI`
    * Integration with `Jenkins`
    * `Docker` images for Cypress
    * Caching dependencies for faster builds
    * Parallel test execution in CI
    * Handling test artifacts (screenshots, videos) in pipelines
<!-- chapter: cypress-cloud, duration: 1h -->
* `Cypress Cloud`
    * Setting up `Cypress Cloud` (dashboard service)
    * Recording test runs and viewing results
    * Test parallelization and load balancing
    * Flaky test detection and management
    * Analytics and test insights
    * Integration with source control and CI providers
<!-- chapter: component-testing, duration: 1h -->
* Component Testing
    * Cypress component testing overview
    * Setting up component testing for React, Vue, and Angular
    * Mounting components in isolation
    * Testing component props, events, and slots
    * Stubbing dependencies in component tests
    * Component testing vs end-to-end testing trade-offs
<!-- chapter: visual-testing, duration: 1h -->
* Visual Testing
    * Visual regression testing concepts
    * Cypress plugins for visual testing
    * Snapshot comparison and diff detection
    * Handling dynamic content in visual tests
    * Visual testing in `CI/CD` pipelines
<!-- chapter: best-practices-and-comparison, duration: 1h -->
* Best Practices and Comparison
    * Test organization and naming conventions
    * Avoiding anti-patterns in Cypress tests
    * Performance optimization for large test suites
    * Cross-browser testing strategies
    * Cypress vs `Playwright`: strengths and trade-offs
    * Cypress vs `Selenium`: architectural differences and use cases
    * Choosing the right tool for your project

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
