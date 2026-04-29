---
tags:
  - concepts:best-practices
  - concepts:agile
  - concepts:developer-experience
level: intermediate
category: methodology
duration_hours: 16
audience:
  - audiences:developers
  - audiences:team-leads
  - audiences:management
  - audiences:senior-developers
---
<!-- course: asynchronous_collaboration -->
# Asynchronous Collaboration

## Description
The catalog has `Effective Remote Engineering`, which is the broader course on remote work as a
practice. This course is the focused complement on the specific skill of asynchronous collaboration:
the ability to `make` progress on shared work without everyone being available at the same time. `Async`
is not a remote-only concern. Even fully co-located teams operate `async` whenever they cross time
zones, sleep, or focus blocks. The teams that do `async` badly waste hours per person per day in
synchronous waiting; the teams that do it well `make` decisions overnight.

This two day course covers asynchronous collaboration as a teachable engineering skill. It covers the
two-mode model (sync and `async`), the document-as-the-meeting pattern, the `async` stand-up, the `async`
design review, the `async` code review (which is most code review), the decision-record-as-output
pattern, the right way to write a `PR` description, the right way to ask a question that does not
need a meeting, the calendar-and-focus-time architecture, the meeting-that-should-be-an-email
heuristic and its inverse, the across-time-zones handover, the `async` incident response, the
`async`-leadership question, and the failure modes (the silent decision, the decision that nobody
heard, the chat-stream-of-consciousness). Examples are drawn from the public writing of `GitLab`,
`Automattic`, `Doist`, `Basecamp`, and `Stripe`. Participants leave able to ship more work with fewer
meetings.

## Duration
16 hours / 2 days

## Intended Audience
* developers wanting more focus time and fewer meetings
* tech leads coordinating across time zones
* engineering managers running distributed teams
* senior developers introducing `async` habits to a sync team

## Prerequisites
* working experience on a software team
* exposure to the Effective Remote Engineering course is helpful but not required
* familiarity with at least one chat tool and one document tool

## Objectives
* recognize `when` work belongs sync vs `async`
* run an `async` design review
* run an `async` code review
* write a `PR` description that does not need a meeting
* run an `async` stand-up that is actually informative
* execute an across-time-zones handover
* avoid the failure modes that turn `async` into chaos

## Outline
<!-- chapter: the-two-mode-model, duration: 1h -->
* The two-mode model
    * sync mode and `async` mode
    * the cost of mixing them
    * the cost of all-sync
    * the cost of all-`async`
    * picking per work-item, not per team
<!-- chapter: when-work-belongs-async, duration: 1h -->
* `When` work belongs `async`
    * the work that benefits from thinking time
    * the work that crosses time zones
    * the work that involves more than five people
    * the work where a written record matters
    * the work where someone will be wrong on the spot
<!-- chapter: when-work-belongs-sync, duration: 1h -->
* `When` work belongs sync
    * the negotiation
    * the brainstorm with high uncertainty
    * the conflict that needs reading the room
    * the new-relationship 1-1
    * the incident triage call
<!-- chapter: the-document-as-the-meeting, duration: 2h -->
* The document as the meeting
    * the comment-on-the-doc pattern
    * the read-and-comment time-box
    * the meeting that becomes the read
    * cross-reference to the Writing Design Documents course
    * the doc that everyone will read
<!-- chapter: the-async-stand-up, duration: 1h -->
* The `async` stand-up
    * the daily message format
    * the blocker as the most important field
    * the stand-up that nobody reads
    * the stand-up that becomes a status report
    * `Geekbot` and friends as a forcing function
<!-- chapter: the-async-design-review, duration: 1h -->
* The `async` design review
    * the design-doc-as-review-vehicle
    * the comment-with-resolution flow
    * the time-box for resolution
    * the escalation to sync `when` stuck
    * the "we never reached a decision" failure
<!-- chapter: the-async-code-review, duration: 1h -->
* The `async` code review
    * most code review is already `async`
    * the comment that needs a response vs the nit
    * the back-and-forth that should have been a call
    * cross-reference to the Code Review course
    * the response-time `SLO` for review
<!-- chapter: the-pr-description-as-async-artifact, duration: 1h -->
* The `PR` description as `async` artifact
    * the why, the what, the how-to-test
    * the screenshots and the loom link
    * the linked design doc
    * the "the `PR` says nothing" failure
    * the template that captures the right things
<!-- chapter: chat-discipline, duration: 1h -->
* Chat discipline
    * `DM` vs channel
    * the threaded vs unthreaded debate
    * the "no hello" rule
    * the "do not @everyone" norm
    * the chat-as-decision-record anti-pattern
<!-- chapter: decision-records-and-the-paper-trail, duration: 1h -->
* Decision records and the paper trail
    * the architecture decision record
    * the decision-was-made-in-chat-and-lost reality
    * the captured-decision habit
    * the "we made the same decision twice" failure
    * the searchable archive
<!-- chapter: across-time-zones-handovers, duration: 1h -->
* Across-time-zones handovers
    * the follow-the-sun model
    * the handover document
    * the in-progress-state question
    * the "I left them with no context" failure
    * the timezone-asymmetric team
<!-- chapter: async-leadership, duration: 1h -->
* `Async` leadership
    * the lead who never blocks the team
    * the decision-by-default time-box
    * the "leader replied last and unblocked everything" pattern
    * the inversion: the leader who is the blocker
    * the `async` 1-1
<!-- chapter: failure-modes, duration: 1h -->
* Failure modes
    * the silent decision
    * the decision that nobody heard
    * the `async`-as-procrastination trap
    * the chat-driven attention drain
    * the meeting-disguised-as-`async`
<!-- chapter: building-an-async-culture-and-wrap-up, duration: 2h -->
* Building an `async` culture and wrap up
    * the team agreement
    * the response-time expectations
    * the no-meetings day
    * the documentation incentive
    * a walkthrough of an `async`-first week
    * the meetings that survived, the docs written, the decisions made
    * cross-reference to the Effective Remote Engineering course
    * recommended reading: `GitLab Handbook`, `Automattic` posts, `Doist`'s `async-first` writing

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
