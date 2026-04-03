---
tags:
  - tools:jest
  - languages:javascript
  - languages:typescript
  - practices:testing
  - concepts:tdd
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:frontend-developers
---
<!-- course: jest -->
# `Jest`

## Description
This course provides a thorough grounding in `Jest`, the most widely used testing framework for `JavaScript` and `TypeScript` applications. Students will learn to write unit and integration tests, leverage `Jest`'s extensive matcher `API`, mock modules and timers, and test asynchronous code with confidence. The course also covers snapshot testing, `React` component testing with `React Testing Library`, and strategies for integrating `Jest` into CI pipelines. Participants will leave with the skills to build reliable, fast test suites for modern front-end and `Node.js` projects.

## Duration
16 hours / 2 days

## Intended Audience
* `JavaScript` and `TypeScript` developers new to or looking to deepen their `Jest` skills
* Front-end engineers building `React`, Vue, or `Angular` applications
* Full-stack developers who want consistent testing practices across the `Node.js` ecosystem

## Prerequisites
* `Solid` working knowledge of `JavaScript` (`ES6`+) or `TypeScript`
* Familiarity with `Node.js` and `npm`/`yarn` package management
* Basic understanding of testing concepts: what a test is and why it matters

## Objectives
* Understand `Jest`'s architecture, configuration, and test runner model
* Write clear, well-structured tests using `describe`, `it`, and `expect`
* Use the full range of `Jest` matchers for assertions
* Mock functions, modules, and timers to isolate units under test
* Test promises, `async`/`await`, and callback-based asynchronous code
* Generate and interpret code coverage reports
* Apply snapshot testing judiciously for UI and serialised output
* Test `React` components using `React Testing Library` and `Jest`
* Tune `Jest` configuration for performance in large monorepos

## Outline
<!-- chapter: introduction-to-jest, duration: 1h -->
* Introduction to `Jest`
    * Why `Jest`: design goals and ecosystem position
    * `Jest` vs `Mocha`, Vitest, and other `JavaScript` test runners
    * Installing `Jest` and configuring `package.json`
    * Project structure for test files
    * Running tests from the command line and watch mode
    * Understanding test results and error output
<!-- chapter: writing-and-running-tests, duration: 2h -->
* Writing and Running Tests
    * `describe` blocks and test organisation
    * `it` and `test` functions
    * `beforeEach`, `afterEach`, `beforeAll`, `afterAll` hooks
    * Test isolation and avoiding shared mutable state
    * Skipping and focusing tests with `.skip` and `.only`
    * Running a single `file` or test by name pattern
<!-- chapter: matchers-and-assertions, duration: 2h -->
* Matchers and Assertions
    * Common matchers: `toBe`, `toEqual`, `toStrictEqual`
    * Truthiness matchers: `toBeNull`, `toBeTruthy`, `toBeFalsy`
    * Number and string matchers
    * `Array` and iterable matchers
    * Object partial matching with `expect.objectContaining`
    * Custom matchers with `expect.extend`
    * Negating expectations with `.not`
<!-- chapter: mocking-functions-modules-and-timers, duration: 3h -->
* Mocking: Functions, Modules, and Timers
    * `jest.fn()` and mock function properties
    * Asserting calls, arguments, and `return-values`
    * `jest.spyOn` for spying on existing methods
    * Automatic module mocking with `jest.mock()`
    * Manual mocks in `__mocks__` directories
    * Mocking ES modules and CommonJS modules
    * Resetting and restoring mocks between tests
    * Fake timers: `jest.useFakeTimers`, `jest.runAllTimers`, `jest.advanceTimersByTime`
    * Mocking `Date` and other globals
<!-- chapter: testing-asynchronous-code, duration: 2h -->
* Testing Asynchronous Code
    * Callbacks and the `done` parameter
    * Testing promise-based code with `.resolves` and `.rejects`
    * `async`/`await` in test functions
    * Handling unhandled promise rejections
    * Timeouts for long-running `async` tests
    * Testing event emitters and observable streams
<!-- chapter: code-coverage, duration: 1h -->
* Code Coverage
    * Enabling coverage with `--coverage`
    * Understanding statement, branch, function, and line coverage
    * Configuring coverage thresholds in `jest.config`
    * `HTML`, LCOV, and text coverage reports
    * Excluding files and directories from coverage
    * Coverage in CI: integrating with Codecov or similar services
<!-- chapter: snapshot-testing, duration: 2h -->
* Snapshot Testing
    * What snapshot testing is and `when` to use it
    * Creating and updating snapshots with `toMatchSnapshot`
    * Inline snapshots with `toMatchInlineSnapshot`
    * Snapshot serialisers for custom output formats
    * Snapshot testing for non-UI data structures
    * Managing snapshot drift and avoiding brittle tests
    * Reviewing and committing snapshots in version control
<!-- chapter: testing-react-components, duration: 2h -->
* Testing `React` Components
    * Introduction to `React Testing Library` philosophy
    * Rendering components with `render` and querying the DOM
    * Querying by role, label, text, and test `ID`
    * Simulating user interactions with `userEvent`
    * Testing component state and side effects
    * Mocking child components and hooks
    * Accessibility-first testing approaches
<!-- chapter: configuration-and-performance, duration: 1h -->
* Configuration and Performance
    * `jest.config.js` vs `jest.config.ts`
    * Transform configuration for `TypeScript` and JSX
    * Module name mapping and path aliases
    * Running tests in parallel with workers
    * Caching and incremental test runs
    * `--testPathPattern` and `--changedSince` for targeted runs
    * Debugging slow tests with `--verbose` and `--detectOpenHandles`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
