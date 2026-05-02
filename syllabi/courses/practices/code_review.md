---
tags:
  - concepts:code-review
  - concepts:best-practices
  - concepts:clean-code
  - concepts:security
  - concepts:testing
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
<!-- course: code_review -->
# Code Review

## Description
Code review is one of the highest-leverage activities a software team performs and one of the most poorly taught. Done
well, it catches defects, spreads knowledge, mentors juniors and shapes architecture. Done poorly, it slows delivery,
demoralizes contributors and produces inconsistent codebases.

This five day course treats code review as a learnable skill rather than a personality trait. It covers the reviewer's
mindset, the mechanics of pull requests, what to look for technically and architecturally, how to write comments that
land and do not bruise, how to scale review across a growing team, and how to use review for deliberate mentoring.
The course also covers security-aware review, performance-aware review, and the specific challenges of reviewing
`AI`-generated code. Participants will leave able to give and receive review that improves both code and people.

## Duration
40 hours / 5 days

## Intended Audience
* developers who want to review code more effectively
* senior developers and tech leads who set the review bar for their team
* engineering managers establishing or fixing the review process
* architects whose review comments carry organizational weight

## Prerequisites
* at least two years of professional software development experience
* working knowledge of `git` and pull-request-based workflows
* prior experience either giving or receiving code review

## Objectives
* describe the goals of code review and prioritize between them in a given context
* read a diff effectively and quickly identify what matters
* write comments that are clear, actionable and respectful
* recognize the most common defect classes in pull requests
* perform security-aware and performance-aware review
* mentor through review without slowing delivery
* receive review feedback constructively and respond well
* design and tune a team's code review process

## Outline
<!-- chapter: why-code-review-and-what-its-actually-for, duration: 2h -->
* Why code review and what it's actually for
    * the multiple goals of review: defects, design, mentoring, ownership
    * what review is good at and what it is bad at
    * the evidence base: studies on review effectiveness
    * review vs pair programming vs `TDD`
    * setting the goal of a specific review
<!-- chapter: how-to-read-a-pull-request, duration: 3h -->
* How to read a pull request
    * starting from the `PR` description, not the diff
    * understanding the change set as a whole
    * reading commits in order vs reading the squashed diff
    * checking out and running the branch
    * the order of attention: tests, public `API`, core logic, edge cases
    * recognizing what's missing from a `PR`
<!-- chapter: the-reviewer-mindset, duration: 2h -->
* The reviewer mindset
    * curiosity over judgement
    * the principle of charitable interpretation
    * separating preference from defect
    * "would I be comfortable maintaining this in two years"
    * recognizing when you are not the right reviewer
    * managing your own bias and fatigue
<!-- chapter: writing-comments-that-land, duration: 3h -->
* Writing comments that land
    * concrete, specific, actionable
    * the difference between blocking and non-blocking comments
    * `nit:`, `suggestion:`, `question:`, `blocker:` prefixes
    * showing instead of telling: code suggestions
    * comments that mentor vs comments that police
    * tone, register and avoiding the loaded word
    * length: when one line is enough and when it is not
<!-- chapter: technical-review-correctness, duration: 3h -->
* Technical review: correctness
    * boundary conditions, null/empty/zero
    * concurrency and race conditions
    * error and exception paths
    * resource lifecycle: files, sockets, transactions, locks
    * `time` zones, locales and floating point
    * accidental `O(N²)` and similar complexity surprises
<!-- chapter: technical-review-design, duration: 3h -->
* Technical review: design
    * separation of concerns and cohesion
    * coupling and dependency direction
    * abstraction at the right level
    * naming as design
    * `API` shape and ergonomic surface
    * recognizing premature abstraction and accidental coupling
<!-- chapter: technical-review-tests, duration: 2h -->
* Technical review: tests
    * what tests are missing
    * tests that test the implementation rather than the contract
    * brittle tests vs robust tests
    * test naming, structure and readability
    * mocks, stubs and the line where they `go` too far
    * coverage as a signal vs coverage as a target
<!-- chapter: technical-review-readability, duration: 2h -->
* Technical review: readability
    * cognitive load of a piece of code
    * naming and what makes a name good
    * comments: when they help and when they lie
    * function shape and length
    * file and module organization
    * dead code and incidental complexity
<!-- chapter: security-aware-review, duration: 4h -->
* Security-aware review
    * input validation and trust boundaries
    * authentication and authorization checks
    * injection: `SQL`, command, template, log
    * cryptographic mistakes and what to spot
    * secrets and credentials in code
    * the `OWASP` top 10 through a reviewer's lens
    * dependency and supply-chain red flags
<!-- chapter: performance-aware-review, duration: 2h -->
* Performance-aware review
    * algorithmic complexity at a glance
    * `N+1` queries and database round trips
    * unnecessary allocations and copies
    * the cost of synchronous remote calls in a hot path
    * lazy vs eager evaluation
    * when not to optimize during review
<!-- chapter: reviewing-tests-infrastructure-and-config, duration: 1h -->
* Reviewing tests, infrastructure and config
    * `IaC` and `Terraform` review
    * `Kubernetes` manifests and Helm charts
    * `CI` pipeline changes
    * configuration changes that look small but are not
    * database migrations and the rollback plan
<!-- chapter: reviewing-ai-generated-code, duration: 2h -->
* Reviewing `AI`-generated code
    * what `AI`-generated code tends to get right
    * what `AI`-generated code tends to get wrong
    * over-engineering, hallucinated APIs, copy-paste
    * subtle correctness issues and confident wrongness
    * adjusting your reviewer attention for `AI` contributions
    * setting team norms for `AI`-assisted PRs
<!-- chapter: large-pull-requests, duration: 2h -->
* Large pull requests
    * why large PRs are a smell
    * how to review one when you cannot avoid it
    * asking for a `PR` to be split, productively
    * stacked `PRs` and review-friendly decomposition
    * reviewing rebases and force-pushes safely
<!-- chapter: receiving-review-well, duration: 2h -->
* Receiving review well
    * separating self from code
    * reading comments charitably
    * disagreeing productively
    * when to push back and when to defer
    * negotiating "we can do this in a follow-up"
    * what to do when reviews keep blocking you
<!-- chapter: review-as-mentoring, duration: 2h -->
* Review as mentoring
    * teaching through review without lecturing
    * the line between mentoring and gatekeeping
    * adjusting depth for junior, mid, senior contributors
    * pairing review with one-on-one conversation
    * review as a tool for growing reviewers
<!-- chapter: process-and-tooling, duration: 2h -->
* Process and tooling
    * `GitHub`, `GitLab`, `Gerrit`, `Phabricator` review models
    * required reviewers, code owners and `CODEOWNERS`
    * review automation: linters, formatters, type checkers, security scanners
    * `merge` queues and `merge` trains
    * review `SLA`s and queue management
<!-- chapter: scaling-review-across-a-team, duration: 2h -->
* Scaling review across a team
    * tuning the review bar over time
    * distributing review load fairly
    * preventing reviewer burnout
    * keeping standards consistent across teams
    * post-mortems from review escapes
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * group review of real-world pull requests
    * comparing review philosophies
    * recommended reading and further study

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
