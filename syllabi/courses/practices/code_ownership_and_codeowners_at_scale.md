---
tags:
  - concepts:best-practices
  - concepts:code-review
  - concepts:operations
  - concepts:agile
level: intermediate
category: practices
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:management
  - audiences:architects
---
<!-- course: code_ownership_and_codeowners_at_scale -->
# Code Ownership and `CODEOWNERS` at Scale

## Description
The catalog has `Code Review`, `Code Review Best Practices`, `Engineering Metrics and DORA`,
`Technical Leadership`, and `Engineering Onboarding at Scale`. None of those is the focused course on
the discipline of code ownership in a large repository: who owns which directory, how the
`CODEOWNERS` `file` is structured, how reviews are routed, how ownership transitions work, what happens
`when` an owner leaves, and how ownership relates to the Conway's-law shape of the organization. In a
small repository ownership is implicit. In a large repository — especially a monorepo — ownership has
to be engineered or every `PR` becomes a coordination problem.

This two day course covers code ownership as an engineering practice. It covers the canonical
ownership models (per-team, per-domain, per-component, hybrid), the `GitHub` and `GitLab`
`CODEOWNERS` mechanics, the `Bitbucket` and `Gerrit` equivalents, the per-directory granularity
question, the relationship to `RFCs`, design docs, and `ADRs`, the review-routing strategy (eager
vs lazy, blocking vs advisory), the no-owner pile (the directory that nobody owns), the
ownership-handoff workflow `when` teams reorganize, the ownership-and-on-call relationship, the
relationship to the codebase's directory structure (Conway's law), the metrics (review latency by
owner, ownership coverage), and the patterns that `make` ownership hold up at scale. Examples are
drawn from public engineering writing of `Shopify`, `Stripe`, `Square`, and the `Google` and `Facebook`
monorepo posts. Participants leave able to design a `CODEOWNERS` strategy for a real repository.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers maintaining a large repository
* team leads designing the team's review model
* engineering managers responsible for code-quality outcomes
* architects shaping the codebase's evolution

## Prerequisites
* working experience on a non-trivial codebase
* familiarity with at least one code review system (`GitHub`, `GitLab`, `Gerrit`)
* exposure to the Code Review course is helpful

## Objectives
* explain the trade-offs of the canonical ownership models
* design a `CODEOWNERS` `file` for a real repository
* route reviews efficiently
* manage ownership transitions and reorganizations
* connect ownership to on-call and to incident response
* measure the ownership program with the right metrics
* recognize the patterns that doom ownership programs

## Outline
<!-- chapter: why-ownership-is-an-engineering-decision, duration: 1h -->
* Why ownership is an engineering decision
    * the canonical incident: a critical change with no clear owner
    * the canonical bottleneck: every change goes through one team
    * cross-reference to the Code Review course
    * the cost of implicit ownership
    * the Conway's-law observation
<!-- chapter: ownership-models, duration: 2h -->
* Ownership models
    * per-team
    * per-domain
    * per-component
    * hybrid models
    * the rotating-owner anti-pattern
    * picking
<!-- chapter: codeowners-mechanics-github, duration: 2h -->
* `CODEOWNERS` mechanics (`GitHub`)
    * the `file` format
    * the per-directory and glob rules
    * the `*` catch-all
    * required reviews from owners
    * the team vs user vs both
    * the "we required two owners and never merged again" trap
<!-- chapter: codeowners-elsewhere, duration: 1h -->
* `CODEOWNERS` elsewhere
    * `GitLab`'s implementation
    * `Bitbucket` Pipelines
    * `Gerrit` and code-owners plugin
    * `Phabricator`'s legacy
    * picking the platform feature
<!-- chapter: granularity, duration: 2h -->
* Granularity
    * per-directory vs per-`file`
    * the deeply-nested-directory cost
    * the catch-all-on-the-root question
    * the "we had 1000 lines of `CODEOWNERS`" reality
    * the audit-the-`file` workflow
<!-- chapter: review-routing-strategy, duration: 2h -->
* Review-routing strategy
    * eager: every owner is requested
    * lazy: only one owner is required
    * blocking vs advisory
    * the per-team rotation tool (`PR-owner`, `Pickaxe`, internal scripts)
    * the "everyone-was-requested-and-nobody-reviewed" failure
<!-- chapter: the-no-owner-pile, duration: 1h -->
* The no-owner pile
    * the unowned directory
    * the no-owner-found `CI` `check`
    * the orphan-after-reorg case
    * the "we ignored it for a year" reality
    * the periodic ownership-audit workflow
<!-- chapter: ownership-handoff, duration: 1h -->
* Ownership handoff
    * the team reorganization
    * the bulk-update tool
    * the migration-period dual-ownership
    * the "we reorged and forgot to update `CODEOWNERS`" reality
    * the tooling
<!-- chapter: ownership-and-on-call, duration: 1h -->
* Ownership and on-call
    * code owner = on-call?
    * the cross-reference between systems
    * the "the owner did not respond and the on-call did not know the code" failure
    * cross-reference to the Incident Response and Postmortems course
    * the runbook ownership question
<!-- chapter: ownership-and-conways-law, duration: 1h -->
* Ownership and Conway's law
    * the codebase that mirrors the org chart
    * the org chart that mirrors the codebase
    * the misalignment failure
    * the change-the-codebase-or-change-the-org question
    * the staged restructure
<!-- chapter: metrics-of-an-ownership-program, duration: 1h -->
* Metrics of an ownership program
    * review latency by owner
    * ownership coverage
    * orphan count
    * the per-team review load
    * the "the metric was good and the program failed" reality
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * `Shopify`'s monorepo ownership
    * `Stripe`'s ownership program
    * `Google`'s `OWNERS` system
    * `Meta`'s ownership at scale
    * recommended reading: `Software Engineering at Google`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
