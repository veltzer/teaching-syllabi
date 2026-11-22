---
tags:
  - concepts:data-architecture
  - concepts:database-design
  - concepts:migration
  - concepts:web-development
  - data-and-ai:agents
  - data-and-ai:ai
  - databases:migrations
  - practices:architecture
  - practices:refactoring
  - practices:testing
level: intermediate
category: architecture
duration_minutes: 120
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
---

<!-- blurb: rewriting_systems_with_ai -->
# Rewriting Whole Systems with `AI`: New Language, New Database, New Web, Same Business

**Technical leadership expert talk.** `AI` agents have turned the full system rewrite from a
career-ending gamble into a realistic project. How to choose the new stack, move the data,
and arrive with the business intact.

## The Challenge

For decades the advice was never to rewrite: the old system holds years of undocumented
behavior, the new one takes longer than promised, and the business stands still while both
are maintained. `AI` coding agents change the arithmetic - translating a codebase is now
cheap and fast - but they do not change the risks. An agent will happily produce a clean new
system that drops a business rule nobody wrote down, a schema that cannot hold the old data,
or a migration that loses a fraction of the records. Writing the new code has become the easy
part; deciding what to build and proving that it behaves like the old system has not.

## What This Session Covers

A practical, technical guide to replacing a whole system with the help of `AI` agents: how to
recover what the old system really does, how to choose the new language, database
architecture, and web architecture when agents write most of the code, how to move the data
without losing it, and how to cut over without betting the company on a single weekend.

## Agenda

* **Why the Rewrite Is Back on the Table** (10 min): What `AI` agents make cheap, what stays expensive, and how to tell a system worth rewriting from one worth leaving alone.
* **Recovering What the Old System Does** (15 min): Using agents to read legacy code, extract business rules, and turn undocumented behavior into a specification and a test suite.
* **Choosing the New Language** (15 min): Agent proficiency, compile-time verification, and ease of review as selection criteria; one language or several across the new system.
* **Choosing the New Database Architecture** (15 min): Redesigning the schema instead of copying it; relational, document, and event-based models, and which decisions are hard to reverse later.
* **Choosing the New Web Architecture** (15 min): Server-rendered versus single-page front ends, the shape of the `API`, and monolith versus services when agents maintain the code.
* **Moving the Data** (20 min): Mapping the old model to the new one, cleaning decades of inconsistent records, repeatable migration scripts, reconciliation, and rehearsing the move until it is boring.
* **Proving Equivalence and Cutting Over** (20 min): Running old and new side by side, comparing their output on real traffic, migrating in slices, and keeping a way back.
* **Key Takeaways and Q&A** (10 min): A checklist for deciding on, planning, and running an `AI`-assisted rewrite.

## Takeaways

* A realistic picture of what `AI` agents change about system rewrites and what they leave as hard as ever
* Criteria for choosing the language, database architecture, and web architecture of the replacement system
* A practical approach to data migration that can be rehearsed, verified, and repeated
* A cut-over strategy that proves the new system against the old one before the business depends on it

## Who Should Attend

* Engineering managers
* Tech leads
* Software architects
* Developers maintaining systems that are due for replacement

## Continue the Journey

This talk covers the whole journey at altitude. A follow-on, hands-on workshop can take one of
the team's own systems, recover its behavior into tests, and plan the target stack, the data
migration, and the cut-over with it.

## Speaker

Mark Veltzer
