---
tags:
  - concepts:domain-driven-design
  - concepts:architecture
  - concepts:design-patterns
  - concepts:best-practices
  - concepts:microservices
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:architects
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
---
<!-- course: event_storming_and_domain_modeling -->
# Event Storming and Domain Modeling

## Description
Event storming is a workshop technique for rapidly exploring and modeling complex business domains together with the
people who actually own the work. It produces a shared, visual model of how a business operates, surfaces hidden
assumptions and edge cases, and feeds directly into bounded-context design and service decomposition.

This five day course teaches event storming as a practical discipline, end to end. It covers the three levels of
event storming (big picture, process modeling, software design), how to facilitate the workshops, how to translate
sticky notes into bounded contexts, aggregates and read models, and how to integrate the results into a wider
`domain-driven design` and architecture practice. Participants leave able to run event storming workshops in their
own organizations, model unfamiliar domains effectively, and turn the output into concrete architectural decisions.

## Duration
40 hours / 5 days

## Intended Audience
* architects designing or refactoring systems with non-trivial business logic
* senior developers working closely with domain experts
* team leads and tech leads driving service decomposition
* engineers learning `domain-driven design` and looking for a practical entry point

## Prerequisites
* several years of software development experience
* some exposure to `domain-driven design` is helpful but not required
* basic familiarity with at least one architecture style (`monolith`, `microservices`, event-driven)

## Objectives
* facilitate big-picture, process-level and software-design event storming workshops
* identify hot spots, pivotal events and bounded contexts from a workshop output
* translate event-`storm` artefacts into aggregates, commands, policies and read models
* integrate event storming with `domain-driven design`, `CQRS` and `event-driven architecture`
* recognize the most common workshop failure modes and recover from them
* run event storming remotely as well as in person

## Outline
<!-- chapter: introduction-to-event-storming, duration: 2h -->
* Introduction to event storming
    * the origin of event storming and Alberto Brandolini's work
    * what event storming is good for and what it is not
    * the three levels: big picture, process modeling, software design
    * relationship to `domain-driven design`
    * comparing event storming to other modeling techniques
<!-- chapter: the-language-of-events, duration: 3h -->
* The language of events
    * domain events as the unit of analysis
    * past tense, business language, irreversible facts
    * timeline as the dominant axis
    * event granularity choices
    * good event names and bad event names
    * common event modeling traps
<!-- chapter: workshop-mechanics, duration: 3h -->
* Workshop mechanics
    * physical materials: sticky notes, color conventions, paper roll
    * digital tools: `Miro`, Mural, `EventStorming.com`, `Whimsical`
    * room setup, group size and composition
    * the role of the facilitator
    * pacing, breaks and energy management
    * documenting the result for later use
<!-- chapter: big-picture-event-storming, duration: 3h -->
* Big-picture event storming
    * goals: shared understanding, exploration, surfacing pain
    * who should be in the room
    * the chaotic exploration phase
    * enforcing the timeline
    * hot spots, pivotal events, swimlanes
    * pivotal events as candidate context boundaries
    * outputs you can act on
<!-- chapter: process-level-event-storming, duration: 3h -->
* Process-level event storming
    * adding actors, commands and policies
    * read models and information needs
    * external systems and integration boundaries
    * triggering events vs reaction events
    * spotting missing process steps
    * walking the timeline backwards as a sanity check
<!-- chapter: software-design-event-storming, duration: 3h -->
* Software design event storming
    * aggregates and consistency boundaries
    * commands as aggregate inputs
    * events as aggregate outputs
    * policies and reactive logic
    * read models and `CQRS`
    * deriving service contracts from a design-level model
<!-- chapter: from-stickies-to-bounded-contexts, duration: 3h -->
* From stickies to bounded contexts
    * recognizing context boundaries on the wall
    * naming bounded contexts
    * ubiquitous language per context
    * context maps and integration patterns
    * shared kernel, customer/supplier, anti-corruption layer
    * splitting and merging contexts after the workshop
<!-- chapter: aggregates-and-invariants, duration: 3h -->
* Aggregates and invariants
    * what an aggregate is and is not
    * identifying invariants from events and commands
    * sizing aggregates
    * eventual consistency between aggregates
    * the cost of getting aggregate boundaries wrong
    * refactoring aggregates after they prove unworkable
<!-- chapter: commands-policies-and-reactive-flows, duration: 2h -->
* Commands, policies and reactive flows
    * commands as expressions of intent
    * policies as "whenever this then that"
    * orchestration vs choreography
    * sagas as long-running policies
    * keeping reactive flows debuggable
<!-- chapter: read-models-and-projections, duration: 2h -->
* Read models and projections
    * the read side as a first-class design concern
    * deriving projections from events
    * multiple read models per write model
    * keeping projections fresh
    * choosing storage for read models
<!-- chapter: integrating-with-event-driven-architecture, duration: 2h -->
* Integrating with `event-driven architecture`
    * domain events vs integration events
    * event-carried state transfer vs event notification
    * schema evolution for events
    * the relationship between event storming and `Kafka`-shaped architectures
    * outbox and inbox patterns
<!-- chapter: facilitation-skills, duration: 2h -->
* Facilitation skills
    * preparing stakeholders before the workshop
    * starting the workshop without losing the room
    * dealing with dominant voices and silent participants
    * keeping arguments productive
    * recognizing when to slow down or speed up
    * closing the workshop with concrete outputs
<!-- chapter: remote-and-hybrid-event-storming, duration: 2h -->
* Remote and hybrid event storming
    * choosing a digital canvas tool
    * adapting workshop mechanics to async work
    * managing time zones
    * splitting big workshops into smaller sessions
    * pitfalls unique to remote facilitation
<!-- chapter: anti-patterns-and-failure-modes, duration: 2h -->
* Anti-patterns and failure modes
    * the workshop that becomes a meeting
    * over-modeling a small problem
    * skipping the chaotic exploration phase
    * letting `IT` design without domain experts
    * the post-workshop drift back to the old model
    * recovering a workshop that has gone off the rails
<!-- chapter: case-studies, duration: 3h -->
* Case studies
    * walkthrough of a big-picture workshop on a billing domain
    * walkthrough of a process-level workshop on order fulfillment
    * walkthrough of a software-design workshop on a payments engine
    * deriving services and contracts from each
    * lessons learned and what changed in production
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * hands-on facilitation exercise on a sample domain
    * group debrief and feedback
    * recommended reading and further study

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
