---
tags:
  - architecture:microservices
  - concepts:configuration
  - data-and-ai:agents
  - data-and-ai:ai
  - practices:documentation
  - practices:maintenance
  - practices:monorepo
level: intermediate
category: ai
duration_minutes: 120
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
---

<!-- blurb: documenting_large_projects_with_ai -->
# Documenting Very Large Projects with `AI`

**Technical leadership expert talk.** A practical method for using `AI` agents to document
codebases far too large to fit in any context window - and for keeping that documentation
accurate.

## The Challenge

Large codebases are where documentation is needed most and where it is most often missing or
out of date. `AI` agents can write documentation quickly, but asking an agent to "document the
whole project" fails: the codebase does not fit in its context, cross-module relationships are
lost, and the result is shallow, inconsistent, or simply invented. Documenting a large project
with `AI` needs a method, not a single prompt.

## What This Session Covers

A step-by-step approach to documenting very large projects with `AI` agents: working bottom-up
from folders small enough to understand completely, rolling the results up into higher-level
descriptions, running several passes to resolve circular dependencies, documenting services and
environments, and verifying and maintaining the output as the code changes.

## Agenda

* **Why "Document Everything" Fails** (10 min): Context limits, lost relationships, and invented details when an agent is pointed at a whole large codebase at once.
* **Bottom-Up: Small Folders First** (20 min): Splitting the tree into folders small enough to fit in context, documenting them in full, and rolling summaries up level by level to the top.
* **Several Passes for Circular References** (15 min): Why a single pass cannot describe modules that depend on each other, and how repeated passes refine cross-references until the documentation is consistent.
* **High-Level Microservice Documentation** (20 min): A service catalog with responsibilities, interfaces, data ownership, and interactions; the system-level view that no single folder reveals.
* **Environment Documentation** (15 min): Build and run instructions, configuration and environment variables, infrastructure, deployment, and local development setup.
* **Verifying `AI`-Written Documentation** (15 min): Catching hallucinated details, human review where it matters most, and testing documentation by having agents answer real questions with it.
* **Keeping It Current** (15 min): Regenerating only what changed, propagating changes upward, and adding documentation checks to the development workflow.
* **Key Takeaways and Q&A** (10 min): Actionable next steps for engineering teams.

## Takeaways

* A repeatable, bottom-up method for documenting codebases of any size with `AI` agents
* Techniques for handling circular dependencies, service-level views, and environment documentation
* Practical ways to verify `AI`-written documentation and keep it in sync with the code

## Who Should Attend

* Engineering managers
* Tech leads
* Software architects
* Developers working on large codebases

## Continue the Journey

This talk presents the method. A follow-on, hands-on workshop can apply it to the team's own
codebase and produce a first, verified layer of documentation together.

## Speaker

Mark Veltzer
