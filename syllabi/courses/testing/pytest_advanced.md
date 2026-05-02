---
tags:
  - tools:pytest
  - languages:python
  - practices:testing
  - concepts:tdd
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:qa-engineers
---
<!-- course: pytest_advanced -->
# Advanced `pytest`

## Description
This course takes developers and QA engineers beyond the basics of `pytest` and into its advanced capabilities for building robust, scalable, and maintainable test suites. Students will gain deep mastery of fixtures, parameterization, mocking, async testing, and plugin development. The course also covers coverage measurement, performance profiling of test runs, and configuration strategies for large projects. By the end, participants will be equipped to design sophisticated test architectures and leverage the full power of the `pytest` ecosystem.

## Duration
16 hours / 2 days

## Intended Audience
* `Python` developers who already use `pytest` and want to deepen their expertise
* QA engineers responsible for building and maintaining automated test suites
* Team leads seeking to standardize testing practices across `Python` projects

## Prerequisites
* `Solid` experience writing `Python` applications
* Familiarity with basic `pytest` usage: writing test functions, running tests, and reading output
* Basic understanding of unit testing concepts such as arrange-act-assert

## Objectives
* Recall and consolidate core `pytest` mechanics before moving to advanced topics
* Design reusable and composable fixtures using scoping, factories, and autouse
* Apply parameterization and property-based testing with Hypothesis to maximise coverage
* Mock external dependencies effectively with `unittest.mock` and `pytest-mock`
* Test asynchronous code using `pytest-asyncio` and related tools
* Develop custom `pytest` plugins and hooks to extend framework behaviour
* Configure `pytest` for large mono-repos and CI environments
* Measure and improve test coverage with `pytest-cov` and analyse performance bottlenecks

## Outline
<!-- chapter: pytest-fundamentals-recap, duration: 1h -->
* `pytest` Fundamentals Recap
    * Test discovery and collection rules
    * Running subsets of tests with expressions and markers
    * Built-in fixtures: `tmp_path`, capsys, monkeypatch, `caplog`
    * Understanding conftest.py and its scope hierarchy
    * Markers: built-in and custom
    * Reading and interpreting failure output
<!-- chapter: fixtures-deep-dive, duration: 3h -->
* Fixtures Deep Dive
    * Fixture scopes: function, class, module, package, session
    * Fixture dependencies and dependency injection
    * Parameterized fixtures and indirect parameterization
    * Factory fixtures for flexible object creation
    * Autouse fixtures and their appropriate use cases
    * Fixture finalisation and teardown patterns
    * Sharing fixtures across packages with conftest.py hierarchies
    * Overriding fixtures in nested directories
<!-- chapter: parameterization-and-hypothesis-based-testing, duration: 2h -->
* Parameterization and Hypothesis-Based Testing
    * `pytest.mark.parametrize`: basic and nested usage
    * Combining multiple parametrize decorators
    * Parametrize with fixtures using `indirect`
    * Introduction to property-based testing concepts
    * Writing tests with Hypothesis: strategies and examples
    * Stateful testing and model-based approaches
    * Integrating Hypothesis with `pytest` effectively
<!-- chapter: mocking-with-unittest-mock-and-pytest-mock, duration: 2h -->
* Mocking with `unittest.mock` and `pytest-mock`
    * `MagicMock`, Mock, and `AsyncMock` fundamentals
    * Patching with `patch` decorator and context manager
    * The `mocker` fixture from `pytest-mock`
    * Spying on real objects with `mocker.spy`
    * Mocking module-level and class-level attributes
    * Asserting call counts, call arguments, and call order
    * Common pitfalls: patching in the right namespace
<!-- chapter: testing-async-code, duration: 2h -->
* Testing `Async` Code
    * Overview of async patterns in `Python`
    * Setting up `pytest-asyncio` and event loop configuration
    * Writing async test functions and async fixtures
    * Testing `asyncio` tasks, coroutines, and queues
    * Mocking `async-functions` and context managers
    * Testing code built on `aiohttp`, httpx, or `FastAPI`
    * Handling timeouts and cancellation in async tests
<!-- chapter: plugins-and-custom-plugins, duration: 2h -->
* Plugins and Custom Plugins
    * Overview of the `pytest` plugin ecosystem
    * Useful third-party plugins: `pytest-xdist`, `pytest-timeout`, `pytest-randomly`
    * `pytest` hook system: entry points and hook specifications
    * Writing a minimal plugin in conftest.py
    * Packaging a plugin as a distributable `Python` package
    * Writing tests for your own plugin
    * Plugin best practices and versioning considerations
<!-- chapter: pytest-configuration-and-best-practices, duration: 2h -->
* `pytest` Configuration and Best Practices
    * `pytest.ini`, `pyproject.toml`, and `setup.cfg` configuration
    * Defining default options and test paths
    * Organising large test suites: file layout and naming conventions
    * Managing test dependencies and environment isolation
    * Skipping and xfail strategies for flaky or pending tests
    * Parallelising tests with `pytest-xdist`
    * Ensuring deterministic test ordering
<!-- chapter: performance-and-coverage, duration: 2h -->
* Performance and Coverage
    * Measuring test suite execution time and identifying slow tests
    * Profiling with `pytest-profiling` and `pytest-benchmark`
    * Collecting coverage data with `pytest-cov` and `.coveragerc`
    * Coverage reports: terminal, `HTML`, and `XML` for CI
    * Branch coverage vs line coverage
    * Excluding code from coverage and justifying exclusions
    * Setting coverage thresholds and failing builds on regression

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
