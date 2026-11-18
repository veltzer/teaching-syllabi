---
tags:
  - data-and-ai:ai
  - data-and-ai:agents
  - practices:best-practices
  - practices:code-review
  - practices:documentation
  - practices:security
  - practices:testing
level: intermediate
category: ai
duration_minutes: 120
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
---

<!-- blurb: ai_bad_practices -->
# `AI` Bad Practices: How Teams Undermine `AI`-Assisted Development

**Technical leadership expert talk.** The most common ways teams misuse `AI` coding agents,
why they backfire, and what to do instead.

## The Challenge
`AI` coding agents make it easy to produce a lot of code very quickly. Used carelessly, they
produce a lot of wrong code just as quickly. Teams that adopt `AI` without documentation,
without tests, and without guardrails get fast output they cannot trust, review, or safely
run - and often conclude that `AI` does not work, when the real problem is how it was used.

## What This Session Covers
A practical tour of the anti-patterns that show up again and again in `AI`-assisted
development: what each one looks like in a real codebase, why it causes failures, and the
concrete practice that replaces it.

## Agenda
* **Why Bad Practices Spread So Fast** (10 min): How the speed and confidence of `AI` output hide problems that used to surface early.
* **Using `AI` Without Documentation** (20 min): Agents guessing at conventions, architecture, and workflows; why missing project context produces confident but wrong code.
* **Using `AI` Without Tests** (20 min): Why untested `AI` output cannot be trusted, how agents "fix" failing tests by weakening them, and why tests are the agent's feedback loop.
* **Using `AI` Without Guardrails** (20 min): Unrestricted permissions, destructive commands, leaked secrets, and disabled checks; sandboxing, permission models, and safe defaults.
* **Accepting Output Without Review** (15 min): Rubber-stamping large diffs, losing ownership of the code, and how to keep review meaningful at `AI` speed.
* **Neglected Context and Oversized Tasks** (15 min): One huge prompt for one huge change, polluted context, and no version-control discipline; working in small, verifiable steps.
* **Over-Reliance and Skill Erosion** (10 min): When developers stop understanding the code they ship, and how teams keep their core skills sharp.
* **Key Takeaways and Q&A** (10 min): A checklist of practices for engineering teams adopting `AI` agents.

## Takeaways
* A clear picture of the most common `AI` anti-patterns and the damage each one causes
* An understanding of why documentation, tests, and guardrails are prerequisites for reliable `AI` output
* A practical checklist for reviewing how your team uses `AI` coding agents today

## Who Should Attend
* Engineering managers
* Tech leads
* Software architects
* Developers adopting `AI` coding assistants

## Continue the Journey
This talk names the problems and their remedies. A follow-on, hands-on workshop can audit the
team's own repositories and workflows and put documentation, tests, and guardrails in place
for its `AI` agents.

## Speaker
Mark Veltzer
