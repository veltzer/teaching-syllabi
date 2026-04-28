---
tags:
  - concepts:operations
  - concepts:observability
  - concepts:best-practices
  - concepts:developer-experience
  - concepts:scalability
level: intermediate
category: devops
duration_hours: 40
audience:
  - audiences:sres
  - audiences:devops
  - audiences:developers
  - audiences:senior-developers
  - audiences:team-leads
---
<!-- course: incident_response_and_postmortems -->
# Incident Response and Postmortems

## Description
The difference between organizations that handle outages well and organizations that handle them badly is rarely
a difference in technology. It is a difference in process, communication and culture. This five day course is a
deep treatment of incident response as a learnable engineering discipline.

The course covers the full incident lifecycle: detection, declaration, command structure, mitigation, communication
to internal and external stakeholders, postmortem authorship and review, and the action-item discipline that turns
incidents into lasting improvements. It is grounded in the practices of organizations that operate at scale
(`Google` `SRE`, `PagerDuty`, `Atlassian`, `Honeycomb`) but is applicable to teams of any size. Participants leave
able to be on-call effectively, run an incident as commander, write a postmortem worth reading, and build the
program-level practices that prevent the same incident from happening again.

## Duration
40 hours / 5 days

## Intended Audience
* `SRE`s, `DevOps` engineers and developers carrying production pagers
* on-call engineers wanting to operate more effectively
* tech leads and engineering managers responsible for on-call programs
* incident commanders building a formal `IC` rotation
* leaders establishing a postmortem culture

## Prerequisites
* on-call experience in production, or imminent on-call rotation
* basic familiarity with at least one observability stack (`Prometheus`, `Datadog`, `New Relic`)
* working knowledge of at least one production system you operate

## Objectives
* describe the phases of an incident and the roles within each
* operate effectively as `responder`, scribe and incident commander
* mitigate first, investigate after, with appropriate confidence
* communicate during an incident to internal and external audiences
* author a blameless postmortem that drives action
* design and run a postmortem review process
* build a sustainable on-call rotation
* establish program-level practices: severity definitions, `SLOs`, error budgets

## Outline
<!-- chapter: what-an-incident-is-and-is-not, duration: 2h -->
* What an incident is and is not
    * the spectrum from minor degradation to full outage
    * defining an incident in your organization
    * severity tiers and the cost of getting them wrong
    * incident vs maintenance vs operational toil
    * the relationship to `SLO`s and error budgets
<!-- chapter: incident-detection-and-declaration, duration: 3h -->
* Incident detection and declaration
    * monitoring vs alerting vs paging
    * symptom-based vs cause-based alerts
    * the alert that should never have paged
    * automated vs human-driven declaration
    * the "is this an incident" decision tree
    * declaring early and unde-declaring later
<!-- chapter: roles-and-the-incident-command-system, duration: 3h -->
* Roles and the incident command system
    * incident commander, ops lead, comms lead, scribe
    * single accountable person per role
    * scaling the command structure to incident size
    * handing off the `IC` role across time zones
    * the `IC` is not the most senior engineer
    * delegating away from the keyboard
<!-- chapter: mitigation-first-investigation-second, duration: 3h -->
* Mitigation first, investigation second
    * stop the bleeding before finding the cause
    * mitigation patterns: rollback, kill switch, drain, fail over
    * accepting partial mitigation
    * the false comfort of a `hypothesis`
    * making one change at a time
    * preserving evidence for the postmortem
<!-- chapter: incident-communication, duration: 3h -->
* Incident communication
    * internal updates: `slack` channel, status calls, exec briefings
    * external updates: status page, customer comms, regulator notification
    * tone and content of incident messages
    * the cadence of updates
    * what to say `when` you do not know what is happening
    * the language of "we are investigating"
<!-- chapter: tools-of-the-incident-room, duration: 2h -->
* Tools of the incident room
    * `PagerDuty`, `OpsGenie`, `Splunk On-Call`, `incident.io`, `FireHydrant`
    * dedicated incident channels and bots
    * runbook tooling
    * status page systems
    * recording the incident timeline automatically
    * choosing tools for your scale and budget
<!-- chapter: on-call-rotation-design, duration: 3h -->
* On-call rotation design
    * primary, secondary and escalation tiers
    * follow-the-sun vs single-region rotations
    * rotation length and burnout
    * compensation models
    * onboarding new on-callers
    * rotating production access
    * measuring on-call health
<!-- chapter: runbooks-and-playbooks, duration: 2h -->
* Runbooks and playbooks
    * what makes a runbook actually useful at 3 `AM`
    * runbook discoverability from the alert
    * keeping runbooks honest with on-call drills
    * playbooks for common incident classes
    * runbook ownership and decay
<!-- chapter: production-readiness-and-game-days, duration: 2h -->
* Production readiness and game days
    * production readiness reviews
    * launch checklists
    * tabletop exercises
    * `chaos engineering` and game days
    * disaster recovery drills
    * the value of dry runs before real incidents
<!-- chapter: writing-the-postmortem, duration: 4h -->
* Writing the postmortem
    * blameless writing as a discipline
    * timeline reconstruction from logs, chat, paging records
    * impact in user-relevant units
    * root cause vs contributing factors
    * the "five whys" and its limits
    * counterfactuals and hindsight bias
    * action items: specific, owned, sized, dated
<!-- chapter: postmortem-review-and-publication, duration: 2h -->
* Postmortem review and publication
    * the postmortem review meeting
    * cross-team review for breadth
    * publishing internally and externally
    * the postmortem archive as an asset
    * keeping postmortems searchable
<!-- chapter: action-item-discipline, duration: 2h -->
* Action item discipline
    * action items as commitments
    * sizing and prioritizing action items
    * tracking completion across teams
    * detecting recurrent themes across postmortems
    * `when` an action item should become a project
<!-- chapter: psychological-safety-and-blameless-culture, duration: 2h -->
* Psychological safety and blameless culture
    * blame as the enemy of learning
    * the new view vs the old view of human error
    * how to talk about an engineer's mistake without naming them
    * leaders' role in modeling blamelessness
    * detecting `when` blame is creeping back in
<!-- chapter: severity-slos-and-error-budgets, duration: 2h -->
* Severity, `SLOs` and error budgets
    * defining severity levels operationally
    * `SLI`/`SLO`/`SLA` distinctions
    * error budgets as a tool for tradeoffs
    * burn-rate alerting
    * communicating budget exhaustion to product
<!-- chapter: case-studies-and-anti-patterns, duration: 2h -->
* Case studies and anti-patterns
    * walkthroughs of well-known public incidents
    * the hero culture and why it loses
    * the incident that nobody declared
    * the postmortem that named names
    * the action item list that grew forever
    * lessons learned and changes adopted
<!-- chapter: workshop-and-wrap-up, duration: 3h -->
* Workshop and wrap up
    * tabletop exercise: simulated incident from declaration to postmortem
    * group review of a real postmortem
    * recommended reading: `Google` `SRE` books, `Kepner-Tregoe`, `STELLA Report`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
