---
tags:
  - tools:robot-framework
  - practices:testing
  - practices:acceptance-testing
  - concepts:bdd
level: intermediate
category: testing
duration_hours: 24
audience:
  - audiences:qa-engineers
  - audiences:developers
  - audiences:testers
---
<!-- course: robot_framework -->
# `Robot Framework`

## Description
This course provides a thorough introduction to `Robot Framework`, the keyword-driven acceptance testing and automation framework widely adopted for both web UI and `API` testing. Students will learn to write readable test cases using built-in and external libraries, create reusable keywords, manage variables, and drive data-driven testing at scale. The course covers browser automation with `SeleniumLibrary`, `REST API` testing with `RequestsLibrary`, and writing custom `Python` libraries to extend the framework for domain-specific needs. Participants will also set up `Robot Framework` in a CI environment and produce meaningful reports for stakeholders.

## Duration
24 hours / 3 days

## Intended Audience
* QA engineers and testers who want to adopt a readable, keyword-driven automation approach
* Developers collaborating with QA teams on acceptance test automation
* Teams seeking a framework suitable for both technical and semi-technical contributors

## Prerequisites
* Basic familiarity with `Python` syntax (variables, functions, loops)
* Understanding of `HTTP` and `REST API` fundamentals
* Some exposure to web testing concepts is helpful but not required

## Objectives
* Understand the `Robot Framework` architecture and keyword-driven testing philosophy
* Write well-structured test suites using standard syntax and resource files
* Create reusable keywords and manage variables at all scopes
* Use built-in libraries for string handling, `file` `I/O`, collections, and processes
* Automate web browser interactions using `SeleniumLibrary`
* Test `REST` APIs using `RequestsLibrary`
* Apply data-driven testing with external data sources
* Develop custom `Python` libraries to provide domain-specific keywords
* Configure `Robot Framework` in a `CI/CD` pipeline
* Read and interpret `Robot Framework` reports and debug failing tests

## Outline
<!-- chapter: introduction-to-robot-framework, duration: 2h -->
* Introduction to `Robot Framework`
    * What `Robot Framework` is and where it fits in the testing landscape
    * Keyword-driven vs script-driven automation
    * Architecture: the core framework, test libraries, and runners
    * Installing `Robot Framework` with `pip` and setting up a project
    * Running your first test with `robot` command
    * Understanding the output: report.`html`, log.`html`, output.`xml`
<!-- chapter: test-structure-and-syntax, duration: 2h -->
* Test Structure and Syntax
    * Test suite files and directory structure
    * Settings, Variables, Keywords, and Test Cases sections
    * Writing test cases: steps, arguments, and documentation
    * Suite and test setup and teardown
    * Tags for categorising and filtering tests
    * Resource files and importing keywords
<!-- chapter: variables-and-keywords, duration: 3h -->
* Variables and Keywords
    * Scalar, list, and dictionary variable syntax
    * Variable scopes: local, test, suite, and global
    * Setting variables with `Set Variable`, `Set Test Variable`, and `Set Global Variable`
    * Keyword definition: arguments, `return-values`, and documentation
    * Keyword libraries vs resource files
    * Nested keywords and keyword composition
    * Built-in control flow: `IF`, `FOR`, `WHILE`, `TRY`
    * Using `Run Keyword If` and related conditional keywords
<!-- chapter: built-in-libraries, duration: 2h -->
* Built-in Libraries
    * `BuiltIn` library: assertions, logging, and flow control
    * `String` library: manipulation, matching, and conversion
    * `Collections` library: list and dictionary operations
    * `OperatingSystem` library: `file` system interactions
    * `Process` library: running and managing external processes
    * `DateTime` library: date and time calculations
    * `XML` library: parsing and querying `XML` documents
<!-- chapter: selenium2library-for-web-testing, duration: 3h -->
* `SeleniumLibrary` for Web Testing
    * Setting up `SeleniumLibrary` and WebDriver executables
    * Opening browsers and navigating to URLs
    * Locating elements: XPath, `CSS`, `ID`, name, and accessibility roles
    * Interacting with forms, dropdowns, checkboxes, and `file` uploads
    * Waiting strategies: `Wait Until Element Is Visible`, `Wait Until Page Contains`
    * Taking screenshots on failure
    * Cross-browser testing configuration
    * Page Object pattern with `Robot Framework` resource files
<!-- chapter: rest-api-testing, duration: 2h -->
* `REST API` Testing
    * Setting up `RequestsLibrary` and creating sessions
    * Making GET, POST, PUT, PATCH, and DELETE requests
    * Handling request headers, query parameters, and `JSON` bodies
    * Validating response status codes and `JSON` content
    * Chaining requests with extracted values
    * Authentication: `API` keys, Basic Auth, and Bearer tokens
    * Using `JSONLibrary` for advanced `JSON` assertions
<!-- chapter: data-driven-testing, duration: 2h -->
* Data-Driven Testing
    * Template-based test cases with `[Template]`
    * Data tables in test cases
    * Driving tests from `CSV` files with `DataDriver` library
    * Looping over datasets with `FOR` loops and collections
    * Generating test data with `Python` helpers
    * Organising data-driven suites for maintainability
<!-- chapter: custom-libraries-in-python, duration: 3h -->
* Custom Libraries in `Python`
    * `When` built-in and third-party libraries are not enough
    * Writing a `Python` class as a `Robot Framework` library
    * Keyword naming conventions and argument handling
    * `Return-values` and raising failures
    * Accessing the `BuiltIn` library from `Python` code
    * Handling state and setup/teardown in library classes
    * Packaging and distributing a custom library
    * Testing the library itself with unit tests
<!-- chapter: continuous-integration-setup, duration: 2h -->
* Continuous Integration Setup
    * Running `Robot Framework` in `GitHub Actions` and `Jenkins`
    * Headless browser execution with `Xvfb` or Chrome headless
    * Passing variables via command-line `--variable` flags
    * Parallelising test execution with `pabot`
    * Generating and archiving reports as CI artefacts
    * Sending results to test management tools
<!-- chapter: reports-and-debugging, duration: 2h -->
* Reports and Debugging
    * Understanding report.`html` and log.`html` structure
    * Keyword-level logging with `Log` and `Log To Console`
    * Setting log levels: TRACE, DEBUG, INFO, WARN, ERROR
    * Screenshots and `HTML` page sources on failure
    * Using `--dryrun` to validate syntax without executing
    * Debugging with `robotframework-debuglibrary`
    * Filtering and rerunning failed tests with `--rerunfailed`
<!-- chapter: best-practices, duration: 1h -->
* Best Practices
    * Naming conventions for suites, tests, keywords, and variables
    * Keeping keywords focused and at the right abstraction level
    * Avoiding over-reliance on `Run Keyword If` for control flow
    * Test independence and avoiding state leakage
    * Version controlling test suites alongside application code
    * Maintainability patterns for large test portfolios

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
