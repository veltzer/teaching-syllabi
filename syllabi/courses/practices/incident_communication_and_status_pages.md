---
tags:
  - concepts:best-practices
  - concepts:operations
  - concepts:agile
level: intermediate
category: practices
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:devops
  - audiences:management
  - audiences:team-leads
---
<!-- course: incident_communication_and_status_pages -->
# Incident Communication and Status Pages

## Description
The catalog has `Incident Response and Postmortems`, `Incident Management`, and `Site Reliability
Engineering`. None is the focused course on the customer-facing-and-internal-stakeholder
communication side of an incident: who tells whom what when, the status page, the customer email,
the internal Slack-or-equivalent updates, the relationship between the engineering response and the
support response, the regulatory-disclosure timing, and the patterns that turn an incident from a
trust-destroying event into one that customers actually appreciate the response to.

This two day course covers incident communication as a focused engineering-and-operations practice.
It covers the canonical incident-communication roles (`Incident Commander`, `Communications Lead`,
`Customer Liaison`), the audiences (engineering, support, account management, executive, customer,
public, regulator) and what each needs, the status-page tooling (`Statuspage`, `Better Stack`,
`Instatus`, Stackpulse, Atlassian's and `Cachet`'s open source), the public-vs-private status
distinction, the timing question (when to update, how often, what to say when you do not know yet),
the message templates, the regulatory disclosure (`GDPR` data-breach 72-hour rule, `SEC` Form 8-K
within 4 days, `HIPAA` requirements), the relationship to the postmortem and the public writeup, the
trust-rebuilding-after-the-incident phase, and the patterns that distinguish good incident comms from
bad. Examples include real public incident-communications (good and bad). Participants leave able to
run the comms side of an incident.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers acting as incident commanders
* `DevOps` and operations engineers running incident response
* support and customer-facing leads
* engineering managers responsible for customer trust

## Prerequisites
* working experience handling at least one production incident
* exposure to the Incident Response and Postmortems course
* familiarity with at least one alerting and on-call tool
* basic understanding of communication norms

## Objectives
* assign the canonical incident-communication roles
* segment the audiences and tailor messages per audience
* operate a status page well
* time the customer-facing updates correctly
* meet the regulatory-disclosure deadlines
* connect the incident to the public writeup
* recognize the patterns that destroy customer trust

## Outline
<!-- chapter: why-comms-is-its-own-engineering-concern, duration: 1h -->
* Why comms is its own engineering concern
    * the canonical bad incident: silence
    * the canonical good incident: proactive, frequent, honest updates
    * cross-reference to the Incident Response and Postmortems course
    * the customer-trust outcome
    * the regulatory outcome
<!-- chapter: incident-communication-roles, duration: 2h -->
* Incident communication roles
    * `Incident Commander`
    * `Communications Lead`
    * `Customer Liaison`
    * `Internal Communicator`
    * the "everyone wrote a different message" failure
    * picking the role-set for the team's size
<!-- chapter: audience-segmentation, duration: 2h -->
* Audience segmentation
    * engineering on-call
    * customer support
    * account management
    * executives
    * affected customers
    * the public (status page, social media)
    * the regulator
    * each audience's actual needs
<!-- chapter: the-status-page, duration: 2h -->
* The status page
    * `Statuspage`, Instatus, `Better Stack`, `Cachet`
    * the public vs private model
    * the per-component model
    * the auto-updated status from probes
    * the "our status page lied because it was hosted on the same infra" disaster
<!-- chapter: the-update-timing-question, duration: 2h -->
* The update timing question
    * the first update SLA
    * the every-30-minutes rule
    * the "we have nothing new yet" message
    * the "we resolved the symptom but not the cause" honesty problem
    * the silence-as-a-failure-mode
<!-- chapter: message-templates, duration: 2h -->
* Message templates
    * the investigating template
    * the identified-cause template
    * the mitigating template
    * the resolved template
    * the no-incident-confirmed template
    * the post-incident-writeup-pending template
<!-- chapter: regulatory-disclosure, duration: 2h -->
* Regulatory disclosure
    * `GDPR` 72-hour breach notification
    * `SEC` Form 8-K within 4 business days
    * `HIPAA` and the breach-rule timeline
    * `PCI-DSS` and the card-brand notification
    * cross-reference to the `GDPR` and Compliance course
    * the "we did not know we had to tell anyone" disaster
<!-- chapter: internal-comms-during-the-incident, duration: 1h -->
* Internal comms during the incident
    * the dedicated incident channel
    * the periodic exec update
    * the "we were responding and the executive went straight to engineers" disruption
    * the all-hands-needed escalation
    * the post-incident debrief
<!-- chapter: the-public-writeup, duration: 1h -->
* The public writeup
    * the timing
    * the depth (vs the internal postmortem)
    * the canonical examples: `Cloudflare`, `GitLab`, `AWS`, `Heroku`
    * the "what happened, what we learned, what we are changing" structure
    * the no-blame-but-no-evasion principle
<!-- chapter: trust-rebuilding, duration: 1h -->
* Trust rebuilding
    * the followup credit
    * the announce-the-fix moment
    * the per-customer outreach for major-impact incidents
    * the "we never followed up" customer churn driver
    * the long-term reliability narrative

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
