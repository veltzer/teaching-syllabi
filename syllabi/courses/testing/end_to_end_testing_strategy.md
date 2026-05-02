---
tags:
  - concepts:testing
  - concepts:test-quality
  - concepts:best-practices
  - concepts:operations
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:qa-engineers
  - audiences:team-leads
  - audiences:developers
---
<!-- course: end_to_end_testing_strategy -->
# End-to-End Testing Strategy

## Description
The catalog has tool-focused courses on `Playwright`, Cypress, `Selenium`, `Robot Framework`, plus
the broader `Testing Theory` course. None of those is the focused course on the strategy question that
every team has to answer: how much end-to-end testing do we do, where in the pyramid, what flows do we
cover, who maintains them, and how do we keep them from becoming the most-flaky and most-hated part
of the test suite. This is the question that determines whether end-to-end tests are an asset or a
liability.

This two day course covers end-to-end testing strategy as a focused engineering decision. It covers
the testing pyramid debate (`Mike Cohn`'s pyramid vs `Kent Beck`'s vs `Google`'s), the test-coverage
question (which flows justify an `E2E`), the flake-reduction discipline (the canonical sources of
flake and the canonical fixes), the ownership-and-maintenance question (test ownership is a real
engineering concern), the parallelization-and-speed story, the data-management story (the test users,
the test data, the cleanup), the environment story (production-like vs minimum-viable), the visual-
and-non-visual interaction, the relationship to monitoring and synthetic checks (which can replace
some `E2E` tests), the cost shape, and the patterns that make `E2E` tests survive. Examples are
drawn from public engineering writing of `Spotify`, Slack, Atlassian, and the `Google Testing
Blog`. Participants leave able to write a coherent `E2E` testing strategy for their team.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers writing the team's testing strategy
* `QA` engineers managing the `E2E` test suite
* team leads accountable for `CI` reliability
* developers tired of flaky tests

## Prerequisites
* working experience writing tests in at least one framework
* exposure to the Testing Theory course
* familiarity with `Playwright`, Cypress, or `Selenium`
* basic `CI/CD` knowledge

## Objectives
* place `E2E` tests correctly in the test pyramid
* pick the flows that justify an `E2E` test
* eliminate the canonical sources of flakiness
* assign clear ownership of `E2E` tests
* speed up the suite without losing coverage
* compare `E2E` tests with synthetic monitoring
* recognize when an `E2E` test is the wrong tool

## Outline
<!-- chapter: the-testing-pyramid-revisited, duration: 1h -->
* The testing pyramid revisited
    * `Mike Cohn`'s pyramid
    * `Kent Beck`'s critique
    * `Google`'s "test sizes" model
    * the trophy and the diamond
    * cross-reference to the Testing Theory course
    * picking the model for the team
<!-- chapter: what-justifies-an-e2e-test, duration: 2h -->
* What justifies an `E2E` test
    * the user-critical flow
    * the integration that no smaller test can verify
    * the cross-system contract
    * the flow that has broken before
    * the "we wrote `E2E` for everything and the suite became unmaintainable" failure
<!-- chapter: the-canonical-sources-of-flake, duration: 2h -->
* The canonical sources of flake
    * timing and the implicit-wait
    * shared state and test pollution
    * test data that drifted
    * external services that were not mocked
    * date and time
    * the "this test fails on tuesdays" reality
<!-- chapter: eliminating-flake, duration: 2h -->
* Eliminating flake
    * deterministic-by-construction
    * `Playwright`'s auto-wait model
    * Cypress's retry-ability model
    * the test-data-isolation pattern
    * the "we retried until it passed" anti-pattern
<!-- chapter: ownership-and-maintenance, duration: 1h -->
* Ownership and maintenance
    * who owns each `E2E` test
    * the per-team subset
    * the "the `QA` team owns all `E2E` tests" trap
    * the "every team owns its own" model
    * the test that nobody owned
<!-- chapter: parallelization-and-speed, duration: 1h -->
* Parallelization and speed
    * the per-test isolation requirement
    * the parallel runner
    * the test-sharding strategy
    * the "we made it fast and broke isolation" failure
    * the time-budget for the suite
<!-- chapter: data-management, duration: 2h -->
* Data management
    * the test users and their lifecycle
    * the per-test data setup
    * the cleanup story
    * the "we polluted prod data" disaster
    * the snapshot and replay approach
<!-- chapter: environment-strategy, duration: 1h -->
* Environment strategy
    * production-like staging
    * the per-`PR` ephemeral environment
    * the testing-against-prod question
    * the cost shape of each
    * picking
<!-- chapter: page-objects-and-test-architecture, duration: 1h -->
* Page objects and test architecture
    * the page-object pattern
    * the modern alternative: locator factories
    * the test-as-feature-spec
    * the test-readability question
    * the "we have abstractions on abstractions" failure
<!-- chapter: synthetic-monitoring-as-an-alternative, duration: 1h -->
* Synthetic monitoring as an alternative
    * the always-on user-flow check
    * `Datadog Synthetics`, Checkly, `Pingdom`
    * the production-vs-staging question
    * cross-reference to the `SLOs` and Error Budgets course
    * the "we replaced `E2E` with synthetics for the critical flow" pattern
<!-- chapter: the-cost-of-the-suite, duration: 1h -->
* The cost of the suite
    * the `CI` time
    * the developer-frustration cost
    * the maintenance cost
    * the per-test value calculation
    * the "we deleted half the suite and quality improved" reality
<!-- chapter: writing-the-strategy-document, duration: 1h -->
* Writing the strategy document
    * the goals
    * the pyramid the team agrees to
    * the ownership rules
    * the metrics
    * the periodic review
    * cross-reference to the Writing Design Documents course

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
