---
tags:
  - concepts:testing
  - concepts:tdd
  - concepts:test-quality
  - concepts:bdd
  - concepts:best-practices
  - concepts:functional-programming
level: intermediate
category: testing
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:qa-engineers
  - audiences:testers
---
<!-- course: property_based_testing -->
# Property-Based Testing

## Description
Most automated tests are example-based: the developer chooses a few inputs, hard-codes the expected output, and trusts
that the chosen inputs cover the interesting behavior. Property-based testing inverts this: the developer states a
property that must hold for *all* valid inputs, and the framework generates many inputs to try and falsify it. `When` it
finds a counterexample, it shrinks it to the smallest case that still fails.

This five day course teaches property-based testing as a practical engineering discipline. It covers the underlying
ideas (generators, shrinking, stateful models), the major frameworks (`Hypothesis` for `Python`, `fast-check` for
`JavaScript`/`TypeScript`, `QuickCheck` and its descendants in `Haskell`, `Erlang`, `Scala`, `Rust` and others),
patterns for finding properties in real systems, and the integration of property-based tests into existing test suites
and `CI` pipelines. Participants leave able to apply property-based testing to APIs, parsers, data structures, state
machines, and entire distributed systems.

## Duration
40 hours / 5 days

## Intended Audience
* developers who already write unit tests and want to `find` more bugs with less code
* `QA` and `SDET` engineers responsible for test strategy
* engineers maintaining libraries, parsers, protocols or other components with rich input domains
* anyone debugging classes of bugs that example-based tests miss

## Prerequisites
* `solid` programming experience in at least one of: `Python`, `JavaScript`/`TypeScript`, `Java`, `Scala`, `Haskell`, `Rust`
* experience writing unit tests in a mainstream framework
* basic familiarity with the `TDD` cycle is helpful but not required

## Objectives
* explain what property-based testing is and where it fits relative to example-based and fuzz testing
* identify properties in real-world code
* write generators for non-trivial input domains
* apply shrinking to produce minimal failing cases
* build stateful and model-based property tests
* integrate property-based tests into `CI` cost-effectively
* avoid the most common pitfalls: weak properties, biased generators, shrinking that goes too far
* extend property-based testing to APIs, distributed systems and `concurrency`

## Outline
<!-- chapter: why-property-based-testing, duration: 2h -->
* Why property-based testing
    * the limits of example-based testing
    * the idea: properties over many inputs
    * brief history: `QuickCheck`, `Hypothesis`, `fast-check`
    * property-based testing vs fuzzing vs example-based testing
    * what kinds of bugs property-based testing finds
<!-- chapter: thinking-in-properties, duration: 3h -->
* Thinking in properties
    * what is a property
    * universal properties: idempotence, commutativity, associativity, identity
    * round-trip properties: encode/decode, parse/print
    * `oracle` properties: comparing to a reference implementation
    * invariant properties: things that must always hold
    * metamorphic properties: relations between inputs and outputs
    * the "can I `find` a property here" workshop
<!-- chapter: generators-fundamentals, duration: 3h -->
* Generators: fundamentals
    * primitive generators: integers, floats, strings, booleans
    * composing generators: tuples, lists, dicts
    * filtering and mapping generators
    * conditional generators and the assume primitive
    * controlling distribution and bias
    * generating from grammars
<!-- chapter: shrinking, duration: 3h -->
* Shrinking
    * what shrinking is and why it matters
    * type-based shrinking vs integrated shrinking
    * how `Hypothesis` and `fast-check` shrink
    * shrinking custom types
    * stuck-shrink and overshrink failure modes
    * reading and reproducing shrunk failures
<!-- chapter: hypothesis-deep-dive, duration: 3h -->
* `Hypothesis` deep dive
    * `@given`, `strategies`, settings
    * `composite` and `recursive` strategies
    * the `example database` and reproducible failures
    * `assume` and filtering
    * `target` for guided generation
    * stateful testing with `RuleBasedStateMachine`
    * integration with `pytest`
<!-- chapter: fast-check-deep-dive, duration: 2h -->
* `fast-check` deep dive
    * `fc.assert`, arbitraries, runners
    * built-in arbitraries
    * model-based testing with `fast-check`
    * `async` properties
    * integration with `Jest`, `Vitest`, `Mocha`
<!-- chapter: quickcheck-and-its-descendants, duration: 2h -->
* `QuickCheck` and its descendants
    * the original `Haskell` `QuickCheck`
    * `Erlang QuickCheck` and `PropEr`
    * `ScalaCheck`
    * `proptest` and `quickcheck` for `Rust`
    * `jqwik` for `Java`
    * common idioms across languages
<!-- chapter: writing-good-properties, duration: 3h -->
* Writing good properties
    * the universal-property smell: tautologies and weak properties
    * the "if I delete the implementation, would the property still pass" `check`
    * coverage as a sanity `check` on properties
    * tightening properties incrementally
    * combining example-based and property-based tests
<!-- chapter: testing-data-structures, duration: 2h -->
* Testing data structures
    * algebraic laws as properties
    * model-based testing against a reference implementation
    * testing serializers and parsers with round-trip properties
    * testing collections, maps and trees
    * testing custom data structures
<!-- chapter: stateful-and-model-based-testing, duration: 3h -->
* Stateful and model-based testing
    * the model-based pattern: model, system, equivalence
    * commands, preconditions, postconditions
    * generating sequences of operations
    * shrinking command sequences
    * applying model-based testing to APIs and services
    * applying it to caches, queues and key-value stores
<!-- chapter: testing-apis-and-protocols, duration: 2h -->
* Testing APIs and protocols
    * generating valid `HTTP` requests against an `OpenAPI` spec
    * `schemathesis` and `restler`
    * property-based contract testing
    * fuzzing serialization formats
    * testing `gRPC` services
<!-- chapter: testing-concurrency, duration: 2h -->
* Testing `concurrency`
    * the difficulty of testing concurrent code
    * linearizability checking with `Jepsen`-style tests
    * `Stateright` and similar model checkers
    * randomized scheduling
    * limits of property-based testing for `concurrency`
<!-- chapter: integrating-with-ci, duration: 2h -->
* Integrating with `CI`
    * deterministic seeds vs random search
    * time budget for property tests in `CI`
    * the database of failing examples
    * scheduled long-running property runs
    * flaky property tests and how to triage them
<!-- chapter: pitfalls-and-anti-patterns, duration: 2h -->
* Pitfalls and anti-patterns
    * tautological properties
    * over-constrained generators that `find` nothing
    * tests that pass for the wrong reason
    * over-reliance on randomness in unit tests
    * properties that mirror the implementation rather than the spec
    * mitigation strategies for each
<!-- chapter: case-studies, duration: 3h -->
* Case studies
    * property-based testing in `Stripe`'s billing engine
    * `Volkswagen`-detectors and `Hypothesis` finding real bugs
    * `Jepsen` results on real distributed databases
    * applying property-based testing to a legacy codebase
    * cost/benefit retrospectives
<!-- chapter: workshop-and-wrap-up, duration: 3h -->
* Workshop and wrap up
    * hands-on: derive properties for a sample codebase
    * group review of properties
    * recommended reading and further study

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
