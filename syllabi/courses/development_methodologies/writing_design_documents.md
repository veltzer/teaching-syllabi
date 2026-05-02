---
tags:
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:architecture
  - concepts:design-patterns
level: intermediate
category: methodology
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:architects
---
<!-- course: writing_design_documents -->
# Writing Design Documents

## Description
Design documents are the unit of work for technical leaders. They are how new systems get justified, how risk
gets surfaced before it becomes an outage, how teams reach alignment without an exhausting sequence of meetings,
and how decisions get preserved past the memory of their authors. Most engineers receive no formal training in
writing them, and most design documents in most organizations are correspondingly bad.

This five day course is dedicated to design documents as a discipline. It covers the genres (one-pager, full
design doc, `RFC`, `ADR`, post-implementation review), the structure that makes a doc readable, the tradeoff and
alternatives sections that `make` it useful, the review process around it, the lifecycle from draft to archive,
and the writing skills that turn good ideas into convincing prose. The course is grounded in the publicly
documented practices of `Google`, Stripe, Amazon, Square, `Spotify` and the engineering blogs of similar
organizations. Participants leave able to write a design doc that gets read, reviewed and remembered, and to
build the design-doc culture on a team that does not have one.

## Duration
40 hours / 5 days

## Intended Audience
* developers writing design docs for the first time
* senior developers and tech leads writing design docs regularly
* architects shaping the design-doc culture of an organization
* engineers running an `RFC` or `ADR` process

## Prerequisites
* several years of professional software development experience
* basic familiarity with at least one architecture style and one common system
* willingness to write and accept critique on your writing

## Objectives
* describe the major design-document genres and pick the right one
* structure a design doc so that it gets read
* write the tradeoff and alternatives sections that `make` a doc useful
* run a review process that improves docs without grinding them to halt
* build a design-doc culture on a team that does not have one
* recognize and fix the most common design-doc anti-patterns

## Outline
<!-- chapter: why-design-docs, duration: 2h -->
* Why design docs
    * the meeting tax that good docs replace
    * the alignment problem and the silent disagreement
    * the long-tail value of an archived doc
    * "writing is thinking"
    * what design docs do not solve
    * counter-arguments and their limits
<!-- chapter: the-genres, duration: 3h -->
* The genres
    * the one-pager and the executive memo
    * the full design doc
    * the architecture decision record (`ADR`)
    * the request-for-comments (`RFC`)
    * the engineering proposal
    * the post-implementation review
    * matching genre to audience and stage
<!-- chapter: structure-of-a-good-design-doc, duration: 3h -->
* Structure of a good design doc
    * context, problem, goals, non-goals
    * proposed solution
    * detailed design
    * alternatives considered
    * tradeoffs
    * security, privacy, operational concerns
    * rollout, rollback, migration plan
    * open questions and known unknowns
<!-- chapter: the-context-and-problem-section, duration: 2h -->
* The context and problem section
    * stating the problem in user-relevant units
    * resisting the urge to start with the solution
    * giving readers the minimum context to evaluate the doc
    * goals and non-goals as a contract
    * "we will not solve" as a useful sentence
<!-- chapter: the-detailed-design-section, duration: 3h -->
* The detailed design section
    * the right level of detail for a given audience
    * sequence diagrams and architecture diagrams
    * data model and `API` contract sketches
    * how to use code in a design doc, and when not to
    * boundaries between docs and reference docs
    * the "is this enough to start coding" test
<!-- chapter: the-alternatives-and-tradeoffs-section, duration: 3h -->
* The alternatives and tradeoffs section
    * the alternative that is the status quo
    * three alternatives, briefly considered
    * the tradeoff matrix and its honest use
    * recording rejected alternatives
    * cross-reference to the Distributed Systems Tradeoffs course
    * resisting the strawman alternative
<!-- chapter: writing-style-for-engineers, duration: 3h -->
* Writing style for engineers
    * concrete vs vague language
    * naming the moving parts consistently
    * sentence length and paragraph length
    * the inverted pyramid for engineering writing
    * the right use of jargon and acronyms
    * editing your own draft
    * `Strunk` and `White` for engineers
<!-- chapter: diagrams-that-help-not-distract, duration: 3h -->
* Diagrams that help, not distract
    * the principle: a diagram should add information, not decoration
    * sequence, architecture, state, dataflow
    * tools: `Excalidraw`, `draw.io`, PlantUML, Mermaid, `tldraw`
    * the diagram that should be a table
    * keeping diagrams maintainable over time
    * the limit: prose still has to carry the doc
<!-- chapter: the-design-review-process, duration: 3h -->
* The design review process
    * inline comments vs review meetings
    * the "comments first, meeting second" rule
    * single owner, multiple reviewers
    * `LGTM` vs approval vs `RFC` resolution
    * deadlines on review
    * archiving vs continuing the conversation
<!-- chapter: rfcs-and-the-public-comment-period, duration: 2h -->
* `RFCs` and the public comment period
    * the `RFC` model: Rust, `Python`, `IETF`
    * scoping an `RFC` so it can actually finish
    * driving an `RFC` through controversy
    * the rejected-`RFC` archive as a feature
    * `RFCs` for company-internal versus public consumption
<!-- chapter: adrs-and-decision-logs, duration: 2h -->
* `ADRs` and decision logs
    * `Michael Nygard`'s `ADR` template
    * `MADR` and other variants
    * how `ADRs` complement design docs
    * the decision log as a queryable artifact
    * `ADRs` and architecture fitness functions
<!-- chapter: writing-for-non-technical-audiences, duration: 2h -->
* Writing for non-technical audiences
    * exec summaries that actually summarize
    * surfacing risk in business language
    * cost framing
    * the one-page version of a 20-page doc
    * the "what could `go` wrong" appendix
<!-- chapter: building-a-design-doc-culture, duration: 3h -->
* Building a design-doc culture
    * the volunteer-led adoption pattern
    * the manager who mandates docs and kills them
    * the doc template that survives a year
    * the searchable archive
    * keeping docs current vs archiving them
    * mentoring engineers into writing
<!-- chapter: anti-patterns-and-failure-modes, duration: 3h -->
* Anti-patterns and failure modes
    * the doc that is just a meeting agenda
    * the doc with no alternatives section
    * the doc that begins with the solution
    * the doc that nobody reads
    * the doc that is too long to review
    * the perpetual draft
    * the rubber-stamp review
    * how to recognize each and recover
<!-- chapter: case-studies, duration: 2h -->
* Case studies
    * walkthrough of a public `Google` design doc
    * walkthrough of a public Stripe `RFC`
    * walkthrough of a public Rust `RFC`
    * a real production failure traced to a missing design doc
    * before-and-after revision of a real internal doc
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * group review of a participant's draft design doc
    * recommended reading: `Williams`, McMurrey, Gallo, `Strunk and White`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
