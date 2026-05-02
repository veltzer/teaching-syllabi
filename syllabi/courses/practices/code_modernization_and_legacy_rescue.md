---
tags:
  - concepts:best-practices
  - concepts:migration
  - concepts:clean-code
  - concepts:testing
  - concepts:design-patterns
  - concepts:architecture
level: intermediate
category: practices
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:architects
---
<!-- course: code_modernization_and_legacy_rescue -->
# Code Modernization and Legacy Rescue

## Description
The catalog has `Legacy Modernization` (architectural-scale) and `Technical Debt and Refactoring` (code-scale).
This course is the missing middle: rescuing a single team's legacy codebase. The codebase that nobody wants
to touch, that fails subtly in production, that survives because three people understand it and is
otherwise opaque. Most engineers will inherit one of these at some point in their careers and most have
not been taught what to do.

This five day course is hands-on. It covers the diagnostic phase (figuring out what you actually have),
the safety-net phase (characterization tests, golden-master tests), the seam-finding and dependency-breaking
techniques from `Michael Feathers`, the strangler patterns at the service level, the framework and
language-version-upgrade discipline, the documentation-and-onboarding work that turns tribal knowledge
into team knowledge, and the team-level practices that prevent the next legacy codebase from forming.
Examples are drawn across `Java`, `Python`, `C++`, `JavaScript`, and `C#`. Participants leave able to
inherit a legacy codebase and get it under control.

## Duration
40 hours / 5 days

## Intended Audience
* developers and tech leads inheriting legacy codebases
* engineers tasked with a modernization project
* architects bridging architectural and code-level modernization
* engineers preparing to leave a codebase to others

## Prerequisites
* several years of professional software development experience
* working knowledge of at least one mainstream language
* exposure to either the Technical Debt and Refactoring or Legacy Modernization course is helpful

## Objectives
* diagnose what you have inherited honestly
* establish a test safety net before changing legacy code
* apply `Feathers`'s seam techniques to break dependencies
* run a strangler-pattern modernization at the team scale
* upgrade languages and frameworks safely
* turn tribal knowledge into team documentation
* prevent the next legacy codebase from forming

## Outline
<!-- chapter: what-makes-code-legacy, duration: 2h -->
* What makes code legacy
    * `Feathers`'s definition: code without tests
    * the broader definition: code that nobody wants to change
    * the difference between legacy and bad
    * the difference between legacy and old
    * the value-vs-cost matrix for legacy code
    * the case for not touching it
<!-- chapter: diagnosing-what-you-inherited, duration: 3h -->
* Diagnosing what you inherited
    * the first-week reading-the-code plan
    * `git log`, `git blame` archaeology
    * complexity and churn analysis: `CodeScene`, tokei, `lizard`
    * cross-reference to the Technical Debt and Refactoring course's measurement chapter
    * runbooks and tribal-knowledge interviews
    * the "what could `go` wrong" list
    * the diagnostic report deliverable
<!-- chapter: getting-the-build-and-tests-running, duration: 3h -->
* Getting the build and tests running
    * the build that nobody can reproduce
    * pinning dependencies to known-working versions
    * containerizing the build environment
    * tests that have not been run in years
    * the "`make` it green even if it lies" first step
    * the bus-factor mitigation step
<!-- chapter: characterization-tests, duration: 4h -->
* Characterization tests
    * cross-reference to the Technical Debt course's testing chapter
    * the `Feathers` characterization-test technique
    * approval testing and golden-master tests
    * `ApprovalTests`, Touca, `pytest-snapshot`, `Verify.NET`
    * snapshot tests for `HTTP`, `IO`, side effects
    * trusting the snapshot enough to refactor against it
    * the "is the snapshot wrong" check
<!-- chapter: feathers-seam-techniques, duration: 4h -->
* `Feathers` seam techniques
    * the seam concept revisited
    * preprocessing seams
    * link seams
    * object seams
    * extract interface
    * subclass and override
    * sprout method, sprout class
    * wrap method, wrap class
    * dependency-breaking algorithm
<!-- chapter: working-effectively-without-tests, duration: 3h -->
* Working effectively without tests
    * the chicken-and-egg problem
    * tiny safe steps with `IDE` refactoring tools
    * pair-program-the-change
    * cross-reference to the Pair and Mob Programming course
    * the "I will not change behavior" rule
    * recovering from a refactor that went wrong
<!-- chapter: language-and-framework-upgrades, duration: 3h -->
* Language and framework upgrades
    * the `Java 8` to `Java 21` jump
    * `Python 2` to `Python 3` (the historical lesson)
    * `Python 3.x` to current
    * Spring and `Spring Boot` major-version migrations
    * `Node.js` `LTS` migrations
    * `.NET Framework` to `.NET` Core/`.NET`
    * codemods, automated migration tools
    * the test-coverage-prerequisite
<!-- chapter: dependency-modernization, duration: 2h -->
* Dependency modernization
    * the dependency that has not been updated in five years
    * the abandoned-library problem
    * Renovate, `Dependabot` for ongoing maintenance
    * the major-version-bump strategy
    * cross-reference to the `SAST`/`DAST` course's `SCA` chapter
    * deprecation cascades
<!-- chapter: strangler-fig-at-the-service-level, duration: 3h -->
* Strangler-fig at the service level
    * the service-level strangler pattern
    * `branch by abstraction` revisited
    * traffic-shadowing as a verification step
    * incremental migration over months
    * keeping the old system running during transition
    * cross-reference to the Legacy Modernization course
<!-- chapter: rewriting-vs-refactoring-the-decision, duration: 2h -->
* Rewriting vs refactoring: the decision
    * cross-reference to the Technical Debt course
    * the second-system effect
    * the "this is hopeless" honest assessment
    * the partial-rewrite middle ground
    * keeping a rewrite from running forever
    * the cases where neither rewrite nor refactor is right
<!-- chapter: data-and-schema-modernization, duration: 2h -->
* Data and schema modernization
    * the schema that grew organically
    * cross-reference to the Data Modeling in Depth course's evolution chapter
    * online migration patterns
    * the dual-write window
    * data quality as a prerequisite
    * cross-reference to the Data Quality and Validation course
<!-- chapter: documentation-and-onboarding, duration: 3h -->
* Documentation and onboarding
    * tribal-knowledge extraction
    * cross-reference to the Internal Documentation and DevEx course
    * the `ADR` archive for retroactive decisions
    * runbook capture
    * the bus-factor metric
    * onboarding the next person
<!-- chapter: dealing-with-the-original-authors, duration: 1h -->
* Dealing with the original authors
    * when the original authors are still around
    * when they are not
    * the politics of "we are modernizing"
    * preserving the genuinely good decisions
    * recognizing where the legacy choice was actually correct
<!-- chapter: keeping-modernized-code-modern, duration: 3h -->
* Keeping modernized code modern
    * the next-decade plan
    * automated dependency updates as a default
    * the architecture-fitness-function pattern
    * cross-reference to the Trunk-Based Development course
    * the documentation-debt prevention
    * the "do not let it `go` legacy again" team practice
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * a successful `Java` 8 to 21 migration
    * a `Python 2` to 3 rescue
    * a frontend rewrite that worked
    * a frontend rewrite that did not
    * lessons across the cases
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * group review of a real legacy codebase
    * design walkthrough of a modernization plan
    * recommended reading: `Feathers`, Fowler, `Hunt/Thomas`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
