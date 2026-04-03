---
tags:
  - practices:testing
  - practices:tdd
  - practices:bdd
  - practices:refactoring
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
  - audiences:architects
---
<!-- course: test_driven_development -->
# Test-Driven Development

## Description
This course covers the principles and practices of Test-Driven Development (`TDD`), guiding developers through the red-green-refactor cycle and beyond. Students will learn how to write effective tests first, use test doubles and mocking strategies, apply Behavior-Driven Development (`BDD`), and design robust test architectures that support continuous refactoring and long-term code quality.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers looking to adopt `TDD` practices
* QA engineers and test automation specialists
* Team leads and architects aiming to improve code quality

## Prerequisites
* `Solid` experience in at least one programming language
* Basic understanding of unit testing concepts
* Familiarity with a testing framework (e.g., `JUnit`, `pytest`, `Jest`)

## Objectives
* Understand the philosophy and benefits of Test-Driven Development
* Apply the red-green-refactor cycle effectively
* Use test doubles including mocks, stubs, fakes, and spies
* Write `BDD`-style tests with Gherkin syntax and `BDD` frameworks
* Design scalable and maintainable test architectures
* Refactor production code safely with comprehensive test coverage

## Outline
<!-- chapter: introduction-to-tdd, duration: 1h -->
* Introduction to `TDD`
    * What is Test-Driven Development
    * History and motivation behind `TDD`
    * The red-green-refactor cycle
    * Benefits and trade-offs of `TDD`
    * `TDD` vs test-after development
    * `When` to use and `when` not to use `TDD`
<!-- chapter: the-red-green-refactor-cycle, duration: 1h -->
* The Red-Green-Refactor Cycle
    * Writing the first failing test
    * Making the test pass with minimal code
    * Refactoring for `clean` design
    * Iterating through the cycle
    * Triangulation and generalization
    * Baby steps vs larger increments
<!-- chapter: unit-testing-foundations-for-tdd, duration: 1h -->
* Unit Testing Foundations for `TDD`
    * Writing effective unit tests
    * Test structure: Arrange-Act-Assert
    * Naming conventions for tests
    * Testing edge cases and boundary conditions
    * Test independence and isolation
    * Keeping tests fast and deterministic
<!-- chapter: test-doubles, duration: 2h -->
* Test Doubles
    * Types of test doubles: dummies, stubs, spies, mocks, fakes
    * `When` to use each type of test double
    * Hand-rolled test doubles
    * The role of test doubles in isolation
    * Over-mocking and its pitfalls
    * Testing interactions vs testing state
<!-- chapter: mocking-strategies, duration: 2h -->
* Mocking Strategies
    * Mocking frameworks: `Mockito`, `unittest`.mock, Sinon, `Jest` mocks
    * Setting up expectations and `return-values`
    * Verifying interactions and call counts
    * Partial mocking and spy patterns
    * Mocking external dependencies: databases, APIs, `file` systems
    * Mocking time, randomness, and environment
<!-- chapter: behavior-driven-development, duration: 2h -->
* Behavior-Driven Development
    * `BDD` principles and philosophy
    * Gherkin syntax: Given-`When`-Then
    * Feature files and scenarios
    * `BDD` frameworks: `Cucumber`, Behave, SpecFlow
    * Mapping steps to code
    * Collaboration between developers, testers, and business stakeholders
    * Living documentation from `BDD` specifications
<!-- chapter: test-architecture, duration: 2h -->
* Test Architecture
    * The testing pyramid: unit, integration, end-to-end
    * Organizing test suites and test projects
    * Test fixtures and shared setup
    * Test data management strategies
    * Test configuration and environment handling
    * Parallel test execution considerations
    * Test coverage metrics and their limitations
<!-- chapter: refactoring-with-tests, duration: 2h -->
* Refactoring with Tests
    * What is refactoring and why tests enable it
    * Common refactoring patterns: extract method, rename, inline
    * Refactoring legacy code with the strangler pattern
    * Characterization tests for untested code
    * Safe refactoring workflows
    * Continuous refactoring as part of `TDD`
<!-- chapter: tdd-in-different-contexts, duration: 1h -->
* `TDD` in Different Contexts
    * `TDD` for web applications
    * `TDD` for APIs and `microservices`
    * `TDD` for data processing and algorithms
    * `TDD` with databases and persistence layers
    * `TDD` in legacy codebases
<!-- chapter: advanced-tdd-practices, duration: 2h -->
* Advanced `TDD` Practices
    * Outside-in vs inside-out `TDD`
    * London school vs Detroit school
    * Property-based testing and `TDD`
    * Acceptance `TDD` (ATDD)
    * Continuous integration and `TDD`
    * Code review practices for test quality

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
