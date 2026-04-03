---
tags:
  - practices:mutation-testing
  - practices:testing
  - concepts:test-quality
  - tools:pitest
  - tools:mutmut
level: advanced
category: testing
duration_hours: 8
audience:
  - audiences:developers
  - audiences:qa-engineers
---
<!-- course: mutation_testing -->
# Mutation Testing

## Description
This course introduces mutation testing, a powerful technique for evaluating the quality and effectiveness of an existing test suite by deliberately introducing small faults into the source code and checking whether tests detect them. Students will learn how mutation operators work, how to use `PIT (Pitest)` for `Java` projects and `mutmut` for `Python` projects, and how to interpret mutation scores to identify gaps in test coverage. The course goes beyond measuring quality to guiding improvements: participants will practice strengthening tests based on surviving mutants. Cost management and `CI/CD` integration strategies ensure the technique remains practical at scale.

## Duration
8 hours / 1 day

## Intended Audience
* Experienced developers who write tests and want to objectively measure their quality
* QA engineers responsible for test effectiveness in mature codebases
* Teams with high line coverage who still encounter production bugs

## Prerequisites
* `Solid` experience writing unit tests in `Java` or `Python` (or both)
* Familiarity with code coverage metrics and their limitations
* Experience with `Maven`/`Gradle` (for `Java` sections) or `pip`/`pytest` (for `Python` sections)

## Objectives
* Explain what mutation testing is and why line coverage alone is insufficient
* Describe the most common mutation operators and the kinds of bugs they simulate
* Run `PIT (Pitest)` against a `Java` project and interpret its `HTML` report
* Run `mutmut` against a `Python` project and triage surviving mutants
* Calculate and interpret mutation scores at project and module level
* Write targeted tests to kill specific surviving mutants
* Apply strategies to control the cost of mutation testing in large codebases
* Integrate mutation testing into a `CI/CD` pipeline with appropriate thresholds

## Outline
<!-- chapter: introduction-to-mutation-testing, duration: 1h -->
* Introduction to Mutation Testing
    * What mutation testing is and where it came from
    * The fundamental `hypothesis` behind mutation testing
    * Why line and branch coverage metrics can mislead
    * Mutation testing vs property-based testing vs fuzzing
    * Overview of available tools across languages
    * Setting realistic expectations for mutation scores
<!-- chapter: how-mutation-operators-work, duration: 1h -->
* How Mutation Operators Work
    * Definition of a mutant and a mutation operator
    * Arithmetic operator replacement: `+` → `-`, `*` → `/`
    * Relational operator replacement: `<` → `<=`, `==` → `!=`
    * Logical connector replacement: `&&` → `||`
    * Conditional boundary mutations
    * Statement deletion and `return-value` mutations
    * Equivalent mutants and why they cannot be killed
    * The concept of strong vs weak mutation testing
<!-- chapter: pit-pitest-for-java, duration: 2h -->
* `PIT (Pitest)` for `Java`
    * `Pitest` architecture and how it integrates with the `JVM`
    * Adding `Pitest` to a `Maven` or `Gradle` project
    * Running `Pitest` and understanding the `HTML` report
    * Mutation coverage vs line coverage comparison
    * Configuring target classes, target tests, and mutation operators
    * Incremental analysis to reduce runtime on large projects
    * Excluding generated code and third-party classes
    * `Pitest` with `JUnit 5` and common pitfalls
<!-- chapter: mutmut-for-python, duration: 1h -->
* `mutmut` for `Python`
    * Installing and configuring `mutmut`
    * Running `mutmut` against a `Python` project with `pytest`
    * Reading the `mutmut` results summary and `HTML` output
    * Applying surviving mutant patches to inspect the code change
    * Configuring paths, timeouts, and test runners
    * Alternative tools: `cosmic-ray` and their trade-offs
<!-- chapter: interpreting-mutation-scores, duration: 1h -->
* Interpreting Mutation Scores
    * Calculating mutation score: killed / (killed + survived)
    * What a good mutation score looks like in practice
    * Module-level vs class-level vs project-level scores
    * Distinguishing survived mutants from equivalent mutants
    * Prioritising which survived mutants matter most
    * Using mutation results to guide refactoring decisions
<!-- chapter: improving-tests-based-on-survivors, duration: 1h -->
* Improving Tests Based on Survivors
    * Reading a surviving mutant and understanding what it reveals
    * Writing a test that specifically targets a surviving mutant
    * The distinction between testing behaviour vs testing implementation
    * Avoiding the trap of writing tests that only kill mutants
    * Patterns for strengthening assertion quality
    * Reviewing test data: boundary values and edge cases
<!-- chapter: cicd-integration-and-cost-management, duration: 1h -->
* `CI/CD` Integration and Cost Management
    * Why mutation testing is expensive and how to manage it
    * Running mutation testing only on changed code with incremental modes
    * Setting mutation coverage thresholds for build gates
    * Scheduling full mutation runs nightly rather than on every commit
    * Integrating `Pitest` with `GitHub Actions` and `Jenkins`
    * Storing and trending mutation scores over time
    * Balancing thoroughness with feedback cycle speed

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
