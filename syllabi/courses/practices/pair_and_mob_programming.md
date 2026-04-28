---
tags:
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:agile
  - concepts:clean-code
  - concepts:tdd
level: intermediate
category: practices
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
  - audiences:managers
---
<!-- course: pair_and_mob_programming -->
# Pair and Mob Programming

## Description
Pairing and mob (or ensemble) programming sound simple: more than one person at the keyboard. In practice they
are subtle social and technical disciplines that change the economics of software development in non-obvious
ways. Done well, they collapse review cycles, spread knowledge, eliminate single-points-of-failure on a team
and produce better code. Done poorly, they exhaust everyone, surface interpersonal friction, and cost twice
as much for half the result.

This five day course is a practical, hands-on treatment of pairing and mob programming. It covers the styles
(driver/navigator, `ping`-pong, strong-style, mob), the mechanics (rotation, breaks, environment), the social
skills (active listening, deferring opinions, recovering from conflict), the integration with `TDD`, code review
and `CI`, the remote and hybrid variants, and the ways teams adopt or fail to adopt these practices over time.
Participants leave able to pair and mob effectively, coach others, and judge `when` these practices are right
for the work in front of them.

## Duration
40 hours / 5 days

## Intended Audience
* developers wanting to pair or mob more effectively
* tech leads adopting these practices on their teams
* engineering managers evaluating pairing and mobbing for their organization
* coaches and consultants introducing these practices to client teams

## Prerequisites
* at least two years of professional software development experience
* working knowledge of at least one mainstream language and `IDE`
* some test-writing experience helps but is not required

## Objectives
* describe the major pairing and mobbing styles and pick between them
* run a productive pairing or mobbing session
* recognize and recover from common pairing failure modes
* coach others through a productive pairing session
* integrate pairing and mobbing with `TDD`, code review and `CI`
* run remote and hybrid pairing effectively
* introduce these practices to a team without forcing them

## Outline
<!-- chapter: why-pairing-and-mobbing, duration: 2h -->
* Why pairing and mobbing
    * the evidence base, such as it is
    * the four returns: defect rate, learning, focus, code quality
    * what pairing is not (peer pressure, surveillance, code review)
    * the economic argument and the bookkeeping mistake
    * `when` pairing is wrong for the work
<!-- chapter: pairing-styles, duration: 3h -->
* Pairing styles
    * driver/navigator
    * `ping`-pong (driver and navigator alternate per `TDD` cycle)
    * strong-style pairing (Llewellyn `Falco`)
    * unstructured pairing
    * the right style for the right person
    * switching styles mid-session
<!-- chapter: mob-and-ensemble-programming, duration: 3h -->
* Mob and ensemble programming
    * the original Hunter Industries practice
    * driver, navigator, mob roles
    * rotation timing and the typist as scribe
    * mob size: three, five, seven, more
    * mob programming as a learning practice
    * mob programming as a delivery practice
    * Woody Zuill's "all the brilliant people working on the same thing"
<!-- chapter: the-mechanics-of-a-session, duration: 3h -->
* The mechanics of a session
    * the workspace: monitor, keyboard, chairs, room
    * rotation timers and tools (`mobster`, `cuckoo`, `Mob.sh`)
    * breaks and the energy curve
    * starting a session with intent
    * ending a session deliberately
    * documenting what was done
<!-- chapter: social-skills-for-pairing, duration: 4h -->
* Social skills for pairing
    * active listening at the keyboard
    * deferring an idea instead of arguing it
    * the "yes, and" pattern from improv
    * surfacing disagreement productively
    * giving the keyboard up generously
    * recognizing fatigue in your pair
    * recovering from a session that went badly
<!-- chapter: handling-skill-and-experience-gaps, duration: 2h -->
* Handling skill and experience gaps
    * pairing across seniority levels
    * the senior-as-teacher trap
    * the "`let` me drive" anti-pattern
    * pacing for the less experienced person
    * the value of beginner-driven pairing
    * cross-functional pairing: dev with `QA`, `SRE`, designer
<!-- chapter: pairing-with-tdd, duration: 3h -->
* Pairing with `TDD`
    * `ping`-pong as a pairing technique
    * the test-as-conversation pattern
    * pair-programming the red-green-refactor cycle
    * keeping discipline at red and refactor
    * pairing on a refactor without tests
<!-- chapter: pairing-and-code-review, duration: 2h -->
* Pairing and code review
    * paired code as already-reviewed code
    * the trust contract with reviewers
    * second-pair review as a different lens
    * the question of `PR` size `when` paired
    * what to do `when` a paired change still gets review-rejected
<!-- chapter: remote-and-hybrid-pairing, duration: 3h -->
* Remote and hybrid pairing
    * tools: `VS Code` `Live Share`, `JetBrains` `Code With Me`, `tmate`, `tmux`
    * audio and video setup that does not exhaust people
    * latency and its effect on rotation
    * managing time zones for cross-region pairs
    * the "always-on" pairing channel pattern
    * hybrid pairing with one person remote
<!-- chapter: mobbing-remote-and-hybrid, duration: 2h -->
* Mobbing remote and hybrid
    * `Tuple`, `Pop`, `Mob.sh`, simple screen share
    * remote rotation mechanics
    * keeping the silent majority engaged
    * energy management in long remote mobs
    * recording and replay ethics
<!-- chapter: when-to-pair-or-mob, duration: 2h -->
* `When` to pair or mob
    * the kinds of work pairing helps most with
    * the kinds of work pairing hurts most
    * full-time vs occasional pairing
    * pairing as onboarding
    * mob programming for incident-time fixes
    * mob programming for hairy refactors
<!-- chapter: introducing-pairing-or-mobbing-to-a-team, duration: 3h -->
* Introducing pairing or mobbing to a team
    * the volunteer-led adoption pattern
    * proving value with one task
    * letting people opt out gracefully
    * the manager-mandated pairing failure mode
    * recovering `when` a team rejects pairing
    * keeping the practice alive after the initial enthusiasm
<!-- chapter: anti-patterns-and-failure-modes, duration: 2h -->
* Anti-patterns and failure modes
    * the rubber duck (one person silent)
    * the back-seat driver
    * the marathon (no breaks)
    * the broken pair (interpersonal friction)
    * the always-the-same-pair pattern
    * pairing only `when` the senior wants to teach
    * how to recognize each and what to do
<!-- chapter: pairing-for-managers, duration: 2h -->
* Pairing for managers
    * pairing on the productivity report
    * the cost-of-defect counter-argument
    * career growth and pair rotation
    * one-on-ones in a pairing-heavy team
    * promotion of pair contributors
<!-- chapter: case-studies, duration: 2h -->
* Case studies
    * Hunter Industries and the original mob
    * `Pivotal Labs` and full-time pairing
    * teams that tried and stopped, and why
    * teams that pair only on bugs
    * remote-first pairing teams
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * group pair and mob exercise on real code
    * group debrief and reflection
    * recommended reading: `Williams`, `Falco`, `Zuill`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
