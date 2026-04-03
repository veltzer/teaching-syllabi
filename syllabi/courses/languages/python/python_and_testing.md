---
tags:
  - languages:python
  - practices:testing
  - practices:automation
  - tools:selenium
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
---
<!-- course: python_and_testing -->
# `Python` and Testing

## Description
In the past couple of years, `Python` popularity as an automation tool has been rising.
`Python`, in comparison to other languages, contains less verbosity and is relatively easy to use.
As a result of its popularity, `Python` has become one of the most used automation languages.
`Python` offers a large variety of testing frameworks, with easy package installation, wide range of `IDEs`, quick integration with `CI/CD` and many more advantages.
In this course, you will learn the fundamentals of `Python`.
You will create a `Pytest` based automation project with `Selenium`, `Appium`, `REST` `API` support and Allure reports.

This is a rather lengthy course for testing as most testing courses are one day long. The idea of this syllabus is that the attendees can adjust it to their needs.

## Duration
16 hours / 2 days

## Intended Audience
* Automation developers
* Manual QA with development background
* `Python` developers that wish to expand their skills to testing

## Prerequisites
* Programming experience with any programming language
* Basic background in automation development
* Working knowledge of `Python`.

## Objectives
* Be able to test simple and complex systems.
* Acquire the skill to write robust tests.
* Know how to use the various `Python` mocking libraries.

## Outline
<!-- chapter: testing-theory, duration: 2h -->
* Testing Theory
    * Why testing is important
    * Testing as part of software development
        * Software testing life-cycle
        * V-model
        * `Agile` `CI/CD` and testing
    * Levels of testing
        * Unit testing
        * System testing
        * Function level
        * Module level
        * Sub system level
        * End to end
        * Acceptance testing
    * `Python` testing frameworks (`unittest`, `pytest`, etc)
    * Using aids
        * Stubs
        * Mocks
        * Recordings
        * Frameworks that incorporate testing in them.
<!-- chapter: unittest, duration: 1h -->
* `Unittest`
    * Creating test cases and suites
    * Assert methods
    * Running tests and reporting
<!-- chapter: pytest, duration: 1h -->
* `PyTest`
    * Introduction to `PyTest`
    * Creating a basic test
    * Test grouping (markers)
    * Fixtures & Hooks
    * Conftest.py
    * Parametrizing tests
    * XFail & Skip tests
    * `Selenium` & `Appium`
<!-- chapter: pytest-and-ci-cd-integration, duration: 1h -->
* `PyTest` and `CI/CD` integration
    * `Docker` considerations
    * `Jenkins`
    * `Github` workflows
<!-- chapter: web-testing, duration: 1h -->
* Web testing
    * `HTML`, `CSS` & `JavaScript` refresh
    * `Selenium` crash course
    * `Appium` crash course
    * Testing a real web application
<!-- chapter: rest-api-testing, duration: 1h -->
* `REST` `API` Testing
    * `REST` `API` & `JSON` in a Nutshell
    * `JSON` parsing using `Python`
    * `Rest` `API` testing using `Python` & `Pytest`
<!-- chapter: reporting-allure-reports-integration, duration: 1h -->
* Reporting - Allure reports integration
    * Allure introduction
    * `Pytest` - Allure configuration & customization
<!-- chapter: debugging-your-tests, duration: 1h -->
* Debugging your tests
    * Avoid debugging
    * Debugging using pydb
    * Debugging using `Pycharm`
<!-- chapter: ui-testing-pyqt-applications, duration: 1h -->
* UI testing PyQt applications
    * Running PyQt applications headless
    * Using QtTest
    * Using `pytest`-qt
    * Sending signals to your app.
    * Reading your app state.
<!-- chapter: basic-mocking, duration: 1h -->
* Basic Mocking
    * What is mocking and why is it useful
    * How to use the `unittest`.mock library
    * How to use the `pytest`-mock library
    * Patching objects and attributes
    * Mocking functions and methods
    * Controlling mock behavior and assertions
<!-- chapter: advanced-mocking-concepts, duration: 1h -->
* Advanced Mocking Concepts
    * Mocking classes with MagicMock
    * Isolating tests using mocks
    * Mock patching as context managers
    * Where patching makes sense vs refactoring
<!-- chapter: mock-use-cases, duration: 1h -->
* Mock Use Cases
    * Mocking external services calls
    * Using mocks for configuration
    * Mocking expensive modules/objects
    * Parametrizing mocks
<!-- chapter: testing-with-databases, duration: 1h -->
* Testing with Databases
    * Strategies for database testing
    * Using an in-memory database
    * Mocking the database layer
    * Rollback of database state
<!-- chapter: best-practices-when-writing-tests, duration: 1h -->
* Best practices `when` writing tests
    * Tests should be isolated
    * Tests should `clean` after themselves
    * Tests should measure time, but not precisely.
<!-- chapter: data-scraping-bonus-chapter-if-time-permits, duration: 1h -->
* Data scraping (bonus chapter - if time permits)
    * Introduction to data scraping?
    * `Scrapy`
    * Beautiful soup

## Installations
* Each student should have a machine with python3 installed on it
* A `Linux` machine is preferable to `Windows` but is not mandatory.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
