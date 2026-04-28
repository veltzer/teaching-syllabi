---
tags:
  - concepts:best-practices
  - concepts:clean-code
  - concepts:design-patterns
  - concepts:testing
  - concepts:migration
  - concepts:developer-experience
level: intermediate
category: practices
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:architects
---
<!-- course: technical_debt_and_refactoring -->
# Technical Debt and Refactoring

## Description
Every codebase past its first year carries debt. Most teams either ignore that debt until it becomes a crisis or
swing the other way and rewrite from scratch. The middle path is a learnable engineering discipline: how to
recognize debt accurately, prioritize it against feature work, and pay it down through refactoring without
breaking anything.

This five day course covers technical debt as a concept (and why most uses of the term are confused), the diagnostic
tools and metrics that surface it, the refactoring techniques that actually move the needle, and the team-level
practices that prevent debt from rebounding. The course is grounded in the work of `Fowler`, `Feathers`, `Beck` and
`Hunt`/`Thomas`, and is illustrated with examples in `Java`, `Python`, `TypeScript` and `Go`. Participants leave
able to assess their own codebase, plan a debt program and execute it.

## Duration
40 hours / 5 days

## Intended Audience
* developers maintaining codebases more than a year old
* tech leads owning the long-term health of a codebase
* architects setting standards across multiple teams
* engineers tasked with rescuing or modernizing legacy systems

## Prerequisites
* several years of professional software development experience
* working knowledge of at least one mainstream programming language
* experience with at least one test framework
* basic familiarity with version control workflows

## Objectives
* distinguish technical debt from poor code, churn and accidental complexity
* measure the cost of debt in concrete units
* prioritize debt repayment against feature work
* apply core refactoring techniques safely
* characterize legacy code with tests before changing it
* break large refactorings into safe, reviewable steps
* establish team practices that prevent debt from accumulating

## Outline
<!-- chapter: what-technical-debt-actually-is, duration: 3h -->
* What technical debt actually is
    * Cunningham's original metaphor
    * the four-quadrant model: deliberate/inadvertent, prudent/reckless
    * debt vs poor code vs natural change of context
    * "we knew at the time" vs "we did not know"
    * debt as a communication tool with non-engineers
    * common misuses of the term
<!-- chapter: measuring-debt-and-its-cost, duration: 3h -->
* Measuring debt and its cost
    * code metrics worth measuring: complexity, churn, coupling
    * `SonarQube`, `CodeScene`, `Code Climate`, `tokei`
    * hot-spot analysis: code that changes a lot and is also complex
    * lead time and change failure rate as outcome metrics
    * surveying engineers for perceived friction
    * the difference between symptoms and root causes
<!-- chapter: prioritizing-debt-repayment, duration: 3h -->
* Prioritizing debt repayment
    * the "is anyone going to touch this code" filter
    * cost of delay
    * pareto and the 80/20 of debt impact
    * making the case to product
    * dedicated time vs ambient cleanup
    * cleanup tied to feature work
<!-- chapter: refactoring-fundamentals, duration: 3h -->
* Refactoring fundamentals
    * Fowler's definition and the two-hat rule
    * red-green-refactor in `TDD`
    * the simplest refactorings: rename, extract method, inline
    * extract variable, replace temp with query
    * the role of `IDE` refactoring tools
    * the discipline of small steps
<!-- chapter: refactoring-classes-and-modules, duration: 3h -->
* Refactoring classes and modules
    * extract class, inline class, move method, move field
    * replace conditional with polymorphism
    * replace inheritance with delegation
    * decomposing god classes
    * splitting modules along change-axis lines
    * taming long parameter lists and feature envy
<!-- chapter: refactoring-data-and-state, duration: 2h -->
* Refactoring data and state
    * encapsulate field, encapsulate collection
    * replace primitive with object
    * replace magic number with symbolic constant
    * separating value objects from entities
    * making implicit state explicit
    * untangling shared mutable state
<!-- chapter: testing-as-the-safety-net-for-refactoring, duration: 3h -->
* Testing as the safety net for refactoring
    * why refactoring without tests is rewriting
    * the test-coverage threshold for safe change
    * characterization tests for legacy code
    * approval tests and golden-master testing
    * integration tests as a refactoring net
    * mutation testing to validate the safety net
<!-- chapter: working-with-feathers-legacy-code, duration: 3h -->
* Working with `Feathers'` legacy code
    * the seam concept
    * sprout method and sprout class
    * wrap method and wrap class
    * extract interface
    * subclass and override method
    * dependency-breaking techniques
    * Michael `Feathers'` legacy code change algorithm
<!-- chapter: refactoring-large-systems, duration: 3h -->
* Refactoring large systems
    * branch by abstraction
    * the strangler fig pattern
    * parallel implementations and traffic shadowing
    * keystone interface refactorings
    * incremental migration over months
    * keeping the system shippable throughout
<!-- chapter: refactoring-databases, duration: 2h -->
* Refactoring databases
    * `Ambler`/`Sadalage` patterns
    * adding columns safely
    * splitting and merging tables
    * data migration with backfill
    * dual-write `windows`
    * the cost of a schema change at scale
<!-- chapter: refactoring-apis-and-contracts, duration: 2h -->
* Refactoring `APIs` and contracts
    * non-breaking changes by default
    * deprecation and the long tail
    * versioning `when` you must
    * client migration with telemetry
    * cross-reference to the `API` Evolution and Versioning course
<!-- chapter: refactoring-and-design-patterns, duration: 2h -->
* Refactoring and `design patterns`
    * patterns as targets and as smells
    * over-pattern-matching and abstraction debt
    * removing premature abstractions
    * adding abstraction only `when` justified
    * recognizing patterns latent in code
<!-- chapter: tooling-for-large-scale-refactoring, duration: 2h -->
* Tooling for large-scale refactoring
    * `IDE` refactoring features in depth
    * codemods: `jscodeshift`, `comby`, `ast-grep`, `ruff` rewrites
    * tree-sitter-based transformations
    * monorepo-wide refactoring
    * automating the boring 80% of a migration
<!-- chapter: rewrite-vs-refactor, duration: 2h -->
* Rewrite vs refactor
    * `when` a rewrite actually makes sense
    * the second-system effect
    * keeping the old system running during a rewrite
    * sunk cost and identity attachment
    * cases where refactoring is hopeless
<!-- chapter: preventing-debt-from-rebounding, duration: 2h -->
* Preventing debt from rebounding
    * design review and architecture decision records
    * code review with a debt lens
    * boy-scout-rule cleanup
    * fitness functions and architecture tests
    * paying down debt as part of definition-of-done
    * organizational practices that keep debt low
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * walkthrough of debt assessment on a sample legacy codebase
    * group refactoring exercise on real code
    * recommended reading: `Fowler`, `Feathers`, `Beck`, `Hunt`/`Thomas`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
