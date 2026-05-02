---
tags:
  - practices:testing
  - languages:javascript
  - languages:typescript
  - concepts:web-development
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
---
<!-- course: playwright -->
# `Playwright` End-to-End Testing

## Description
`Playwright` is a powerful, multi-browser end-to-end testing framework developed by Microsoft that provides auto-waiting, reliable selectors, and built-in tooling for debugging and tracing. This course covers the full range of `Playwright` capabilities, from writing basic tests to advanced features like network mocking, authentication state management, and visual comparisons. Participants will also explore `Playwright` support for multiple languages and mobile emulation.

## Duration
16 hours / 2 days

## Intended Audience
* Frontend and full-stack developers building web applications
* QA engineers and test automation specialists
* Software developers adopting modern testing frameworks
* Teams migrating from `Selenium` or other testing tools

## Prerequisites
* Proficiency in `JavaScript` or `TypeScript`
* Basic understanding of `HTML`, `CSS`, and the DOM
* Familiarity with web application architecture
* Basic command-line experience
* Understanding of `npm` or `yarn` package management

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Understand `Playwright` architecture and its multi-browser capabilities
* Write reliable tests using locators, assertions, and actions
* Use the test generator (codegen) to scaffold tests quickly
* Implement fixtures, hooks, and the page object model
* Perform `API` testing and mock network requests
* Manage authentication state across tests
* Debug tests with the trace viewer and inspector
* Integrate `Playwright` tests into `CI/CD` pipelines
* Perform visual comparisons with screenshot assertions
* Understand `Playwright` support for `Python`, `Java`, and `.NET`

## Outline
<!-- chapter: playwright-overview-and-architecture, duration: 1h -->
* `Playwright` Overview and Architecture
    * What is `Playwright` and its design goals
    * Multi-browser support: Chromium, Firefox, WebKit
    * Auto-waiting and built-in reliability
    * `Playwright` vs `Selenium` vs Cypress comparison
    * Browser contexts and isolation model
    * The `Playwright` ecosystem and community
<!-- chapter: installation-and-project-setup, duration: 1h -->
* Installation and Project Setup
    * Installing `Playwright` with `npm init playwright`
    * Project structure and configuration (`playwright`.config.ts)
    * Configuring browsers, base URL, and timeouts
    * Installing browser binaries
    * Setting up `TypeScript` and ESLint integration
    * Running the first test
<!-- chapter: writing-tests-locators-assertions-and-actions, duration: 1h -->
* Writing Tests: Locators, Assertions, and Actions
    * Test file structure and test syntax
    * Locator strategies: getByRole, getByText, getByLabel, getByTestId
    * `CSS` and XPath selectors as fallback
    * Web-first assertions with expect
    * Performing actions: click, fill, select, check, hover
    * Working with lists and tables
    * Handling multiple pages and popups
<!-- chapter: test-generator-codegen, duration: 1h -->
* Test Generator (codegen)
    * Using `npx playwright codegen` to record tests
    * Generating locators interactively
    * Editing and refining generated tests
    * Limitations and best practices for generated code
<!-- chapter: fixtures-and-hooks, duration: 1h -->
* Fixtures and Hooks
    * Built-in fixtures: page, context, browser
    * Creating custom fixtures
    * beforeAll, afterAll, beforeEach, afterEach hooks
    * Worker-scoped vs test-scoped fixtures
    * Sharing state between tests safely
    * Fixture dependencies and composition
<!-- chapter: page-object-model, duration: 1h -->
* Page Object Model
    * Implementing page objects in `Playwright`
    * Encapsulating selectors and actions
    * Composing page objects for complex flows
    * Page objects with fixtures
    * Maintaining page objects as the application evolves
<!-- chapter: api-testing, duration: 1h -->
* `API` Testing
    * Using request fixture for `API` calls
    * Making `HTTP` requests: GET, POST, PUT, DELETE
    * Validating response status, headers, and `JSON` body
    * Combining `API` and UI tests
    * Seeding test data via `API`
    * Standalone `API` testing without a browser
<!-- chapter: mocking-network-requests, duration: 1h -->
* Mocking Network Requests
    * Intercepting requests with page.route
    * Stubbing `API` responses
    * Modifying requests and responses on the fly
    * Simulating error conditions and slow networks
    * Aborting requests
    * Mocking `WebSocket` connections
<!-- chapter: authentication-and-storage-state, duration: 1h -->
* Authentication and Storage State
    * Authenticating once and reusing state
    * Saving and loading storage state (`JSON` file)
    * Multi-user authentication scenarios
    * Global setup for authentication
    * Handling token refresh in long test suites
<!-- chapter: parallel-execution-and-sharding, duration: 1h -->
* Parallel Execution and Sharding
    * `Playwright` parallel test execution model
    * Worker processes and isolation
    * Configuring parallelism and retries
    * Sharding tests across CI machines
    * Managing shared resources in parallel runs
<!-- chapter: visual-comparisons, duration: 1h -->
* Visual Comparisons
    * Screenshot assertions with toHaveScreenshot
    * Configuring snapshot thresholds and options
    * Updating baseline screenshots
    * Handling dynamic content in visual tests
    * Full-page vs element screenshots
    * Visual comparison in CI environments
<!-- chapter: tracing-and-debugging, duration: 1h -->
* Tracing and Debugging
    * The `Playwright` trace viewer
    * Recording and viewing traces
    * The `Playwright` inspector for step-by-step debugging
    * Using page.pause for interactive debugging
    * Console logs and error capture
    * Video recording of test runs
    * Debugging in `VS Code` with the `Playwright` extension
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` Integration
    * Running `Playwright` in CI environments
    * `GitHub Actions` configuration
    * `GitLab CI` and `Jenkins` integration
    * `Docker` images for `Playwright`
    * Handling test artifacts: reports, traces, screenshots
    * `HTML` reporter and other reporting options
    * Retries and flaky test management in CI
<!-- chapter: playwright-for-python-java-and-net, duration: 1h -->
* `Playwright` for `Python`, `Java`, and `.NET`
    * `Playwright` for `Python`: installation and usage
    * `Playwright` for `Java`: integration with `JUnit` and `Maven`
    * `Playwright` for `.NET`: usage with `NUnit` and MSTest
    * Cross-language feature parity and differences
    * Choosing the right language binding for your team
<!-- chapter: mobile-emulation-and-accessibility-testing, duration: 1h -->
* Mobile Emulation and Accessibility Testing
    * Emulating mobile devices and viewports
    * Geolocation, locale, and timezone emulation
    * Testing responsive designs
    * Accessibility testing with `Playwright`
    * ARIA snapshots and accessibility assertions
<!-- chapter: best-practices-and-advanced-topics, duration: 1h -->
* Best Practices and Advanced Topics
    * Test organization and naming conventions
    * Avoiding flaky tests and common pitfalls
    * Performance optimization for large test suites
    * Custom matchers and assertions
    * `Playwright` vs Cypress vs `Selenium`: choosing the right tool

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
