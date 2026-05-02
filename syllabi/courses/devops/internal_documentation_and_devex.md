---
tags:
  - concepts:developer-experience
  - concepts:best-practices
  - concepts:operations
  - concepts:gitops
level: intermediate
category: devops
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:team-leads
  - audiences:architects
---
<!-- course: internal_documentation_and_devex -->
# Internal Documentation and DevEx

## Description
Engineering organizations spend extraordinary amounts on tooling and surprisingly little on the
documentation that determines whether the tooling actually gets used. The Writing Design Documents course
covers the design-doc artifact specifically; this course covers the broader internal documentation surface
and how it shapes developer experience: the wikis nobody reads, the runbooks nobody can find at 3 AM, the
onboarding docs that take three months instead of three weeks, and the `IDP` content that ages out the
moment it ships.

This five day course covers internal documentation as an engineering discipline integrated with the
platform and developer-experience effort. It covers documentation genres and audiences, the writing
discipline that makes docs survive over time, runbook quality, onboarding-doc design, the `IDP`
documentation surface (`Backstage TechDocs`, Cortex, Port), the RFC/`ADR` archive, the searchable
wiki, the relationship between docs and search/`AI`, and the metrics and ownership patterns that keep docs
honest. The course is grounded in `Diátaxis`, the Google and `GitLab` documentation playbooks, and the
`Write the Docs` community.

## Duration
40 hours / 5 days

## Intended Audience
* engineers writing internal docs as part of their job
* tech leads owning a team's documentation surface
* `DevOps` and platform engineers operating documentation tooling
* engineers driving the developer-experience program
* engineers tasked with rescuing a documentation system that has decayed

## Prerequisites
* several years of professional software development experience
* willingness to write more than you currently do
* exposure to at least one wiki, `IDP`, or runbook system in production

## Objectives
* describe documentation genres precisely and pick the right one
* write documentation that ages well
* design runbooks that work under stress
* build onboarding docs that compress time-to-first-value
* operate the `IDP` documentation surface
* measure documentation effectiveness with appropriate metrics
* keep documentation honest over years rather than months

## Outline
<!-- chapter: why-internal-docs-decay, duration: 2h -->
* Why internal docs decay
    * the docs-rot pattern
    * the "I will document later" trap
    * the wiki that is everyone's and nobody's
    * the documentation tax on senior engineers
    * the "`AI` will fix this" complacency
    * what good looks like
<!-- chapter: the-diataxis-framework, duration: 3h -->
* The `Diátaxis` framework
    * tutorials, how-to guides, reference, explanation
    * the four-quadrant model
    * picking the right genre for the right need
    * mixed-genre docs and why they fail
    * the `Diátaxis` migration of an existing wiki
<!-- chapter: tutorials-and-onboarding, duration: 3h -->
* Tutorials and onboarding
    * the first-day, first-week, first-month engineer plan
    * the "first `PR` in week one" goal
    * tutorial design that does not skip steps
    * keeping a tutorial green after the underlying system changes
    * the cross-functional onboarding doc
    * onboarding for managers and senior hires
<!-- chapter: how-to-guides, duration: 2h -->
* How-to guides
    * task-oriented writing
    * the "I have a problem, get me to the answer" structure
    * keeping how-tos focused on a single goal
    * the relationship between how-tos and runbooks
    * keeping how-tos discoverable
<!-- chapter: reference-documentation, duration: 2h -->
* Reference documentation
    * `API` reference, configuration reference, error reference
    * generated vs hand-written reference
    * keeping generated reference current
    * the cost of stale reference
    * reference vs explanation
<!-- chapter: explanation-and-architecture-docs, duration: 2h -->
* Explanation and architecture docs
    * the "why" doc that lasts
    * cross-reference to the Writing Design Documents course
    * `ADRs` and the decision log
    * the architecture overview that survives a year
    * keeping explanation honest
<!-- chapter: runbooks-the-3am-test, duration: 4h -->
* Runbooks: the 3 `AM` test
    * what makes a runbook actually useful at 3 `AM`
    * cross-reference to the Incident Response course
    * runbook discoverability from the alert
    * runbook structure: symptoms, `hypothesis`, action, verification
    * keeping runbooks honest with on-call drills
    * runbook ownership and decay
    * the playbook-vs-runbook distinction
<!-- chapter: the-internal-developer-platform-doc-surface, duration: 3h -->
* The internal developer platform doc surface
    * `Backstage TechDocs`
    * `Cortex` and `Port` doc surfaces
    * `MkDocs` and similar docs-as-code tools
    * cross-reference to the Platform Engineering course
    * the service catalog as the documentation entry point
    * scorecards for documentation quality
<!-- chapter: docs-as-code, duration: 3h -->
* Docs as code
    * docs in the repo, reviewed in `PRs`
    * `Markdown`, AsciiDoc, `MDX` as authoring formats
    * static-site generators: `MkDocs`, Docusaurus, Hugo, `mdBook`
    * docs `CI` and link checking
    * the docs-style-guide as code
    * detecting stale docs from `Git` history
<!-- chapter: search-discoverability-and-ai, duration: 3h -->
* Search, discoverability and `AI`
    * the search problem in internal docs
    * `Algolia DocSearch`, `Elasticsearch`, native wiki search
    * `LLM`-backed internal Q&A and its risks
    * `RAG` over internal docs done well
    * cross-reference to the `LLM` Application Engineering course
    * the "`AI` gives confident wrong answers from old docs" failure mode
<!-- chapter: the-rfc-and-adr-archive, duration: 2h -->
* The `RFC` and `ADR` archive
    * cross-reference to the Writing Design Documents course
    * the archive as a queryable engineering asset
    * the rejected-`RFC` collection
    * keeping decision context preserved as systems change
    * preventing the "we did this and forgot why" loop
<!-- chapter: tribal-knowledge-and-its-discontents, duration: 2h -->
* Tribal knowledge and its discontents
    * the senior engineer who is the only person who knows
    * detecting tribal knowledge in Slack searches
    * extraction interviews and the buddy system
    * post-mortem-driven documentation
    * the bus-factor metric
<!-- chapter: documentation-ownership-and-incentives, duration: 3h -->
* Documentation ownership and incentives
    * who owns each doc
    * documentation in promotion criteria
    * docs as a definition-of-done item
    * paying down the doc backlog
    * the "doc fix Friday" cadence
    * cross-reference to the Engineering Metrics and `DORA` course
<!-- chapter: measuring-documentation, duration: 2h -->
* Measuring documentation
    * page-view metrics and what they mean
    * search-no-result metrics
    * docs satisfaction surveys
    * time-to-first-`PR` for new hires
    * `RAG`-eval for `AI`-backed docs
    * acting on metrics without overreacting
<!-- chapter: anti-patterns-and-failure-modes, duration: 2h -->
* Anti-patterns and failure modes
    * the unmaintained wiki
    * the "documentation lives in Slack" problem
    * the doc that is just an outdated screenshot
    * the over-templated doc
    * the doc that is a half-written ticket
    * the docs-team-of-one
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * audit a sample team's documentation surface
    * draft a documentation strategy for your team
    * recommended reading: `Diátaxis`, Procida, `Write the Docs`, `GitLab` handbook

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
