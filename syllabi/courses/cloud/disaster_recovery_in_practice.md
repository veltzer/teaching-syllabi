---
tags:
  - concepts:operations
  - concepts:scalability
  - concepts:distributed-systems
  - concepts:best-practices
  - concepts:cloud-economics
  - concepts:security
level: intermediate
category: cloud
duration_hours: 40
audience:
  - audiences:devops
  - audiences:sres
  - audiences:senior-developers
  - audiences:architects
  - audiences:dbas
---
<!-- course: disaster_recovery_in_practice -->
# Disaster Recovery In Practice

## Description
The architecting/disaster_recovery course in the catalog covers the conceptual side: `RPO`, `RTO`, multi-region
patterns, the cold-warm-hot spectrum. This course is the implementation complement. It is about the actual
engineering work: backups that are tested, runbooks that have been used, failover that has been rehearsed,
and the discipline that turns a `DR` plan from a slide deck into something that works the first time it has
to.

This five day course covers backup strategy and tooling across cloud platforms, restore-drill discipline,
multi-region failover for the major workloads (compute, databases, object storage, identity), the runbook and
game-day patterns that build muscle memory, the regulatory dimension, and the operational decisions you only
`make` well after you have done a real recovery. Examples are drawn from `AWS`, `GCP` and `Azure`. Participants
leave able to design, run and prove a `DR` capability rather than just document one.

## Duration
40 hours / 5 days

## Intended Audience
* `DevOps` and `SRE` engineers responsible for backup and recovery
* senior developers whose teams own production data
* architects designing resilient systems
* `DBAs` operating databases with RTO/`RPO` requirements
* engineers tasked with a `DR` audit or compliance review

## Prerequisites
* working knowledge of at least one cloud platform
* basic familiarity with at least one database, one object store, and `IaC`
* experience operating production systems
* exposure to the architectural-level `DR` material is helpful

## Objectives
* design and operate a backup program that is actually restorable
* measure `RTO` and `RPO` from real drills, not from documentation
* build multi-region failover for the main workload classes
* write runbooks that work at 3 AM under stress
* run game days that find gaps before incidents do
* respond to a real disaster with confidence
* meet the regulatory and audit dimension without ceremony

## Outline
<!-- chapter: dr-vs-ha-vs-business-continuity, duration: 2h -->
* `DR` vs `HA` vs business continuity
    * the difference between resilience and disaster recovery
    * `BCP` (business continuity plan) framing
    * defining "disaster" in your organization
    * the spectrum: backup, multi-`AZ`, multi-region, multi-cloud
    * cross-reference to the architectural Disaster Recovery course
    * what `DR` does not solve
<!-- chapter: rto-and-rpo-from-real-numbers, duration: 2h -->
* `RTO` and `RPO` from real numbers
    * the difference between aspirational and measured `RTO`/`RPO`
    * setting `RTO`/`RPO` from business impact
    * tier-based service classification
    * the cost curve of decreasing `RTO`/`RPO`
    * negotiating `RTO`/`RPO` with stakeholders
    * publishing `DR` `SLOs`
<!-- chapter: backup-fundamentals, duration: 2h -->
* Backup fundamentals
    * the 3-2-1 rule revisited
    * full, incremental, differential backups
    * snapshot vs application-consistent backup
    * encryption at `rest` for backups
    * immutability and air-gapped copies
    * retention policy from compliance
    * the backup that turns out to be empty
<!-- chapter: cloud-backup-services, duration: 3h -->
* Cloud backup services
    * `AWS Backup`, `Azure Backup`, `Google Cloud Backup and DR`
    * snapshot lifecycle management
    * cross-region and cross-account replication
    * `S3` versioning, `Object Lock`, lifecycle rules
    * `EBS`, `Persistent Disk` snapshots
    * comparing managed backup services vs custom
<!-- chapter: database-backup-and-restore, duration: 4h -->
* Database backup and restore
    * `point-in-time recovery` (`PITR`)
    * `pg_dump` vs base backup vs `pg_basebackup`
    * `mysqldump`, `xtrabackup`, native binary log backup
    * `MongoDB` snapshot backups and `oplog` continuity
    * managed-database backup features (`RDS`, `Cloud SQL`, `Azure SQL`)
    * `DynamoDB` backup and `PITR`
    * the restore drill as the only honest test
<!-- chapter: restore-drills-the-actually-important-part, duration: 3h -->
* Restore drills: the actually important part
    * scheduled vs surprise drills
    * partial vs full restore drills
    * restore time as a measured `SLI`
    * restoring to a non-production environment
    * restore-of-restores: testing replicated backups
    * the post-drill report and findings tracking
<!-- chapter: multi-region-architectures, duration: 4h -->
* Multi-region architectures
    * active-passive
    * pilot-light
    * warm-standby
    * active-active
    * the cost-vs-`RTO` curve
    * data replication options across regions
    * the regional dependency map (`IAM`, Route53, `KMS`)
<!-- chapter: failover-mechanics, duration: 3h -->
* Failover mechanics
    * `DNS`-based failover and `TTL` realities
    * load-balancer-based failover
    * service mesh global routing
    * client-side failover patterns
    * cross-reference to the Load Balancing course
    * preventing split-brain on failover
    * the rollback plan when failover fails
<!-- chapter: runbooks-for-disaster-scenarios, duration: 3h -->
* Runbooks for disaster scenarios
    * the runbook that works at 3 AM
    * runbooks for: region outage, account compromise, ransomware, accidental delete
    * decision trees in runbooks
    * runbook discoverability during a real incident
    * keeping runbooks tested
    * cross-reference to the Incident Response courses
<!-- chapter: game-days-and-tabletop-exercises, duration: 3h -->
* Game days and tabletop exercises
    * the difference between a game day and chaos engineering
    * scoping a game day
    * inject design and surprise factor
    * facilitating without contaminating the test
    * the post-game-day debrief
    * cadence of game days vs cost
    * `chaos engineering` as the day-to-day complement
<!-- chapter: identity-and-access-during-disaster, duration: 2h -->
* Identity and access during disaster
    * break-glass accounts and the locked `vault`
    * `IdP` and `SSO` failover
    * `MFA` recovery during outage
    * cross-region `IAM` realities
    * cloud root account and emergency access
<!-- chapter: data-validation-after-restore, duration: 2h -->
* Data validation after restore
    * checking that the restore actually has the data
    * cross-reference to the Data Quality course
    * checksums and reconciliation
    * customer-facing comms after a partial restore
    * the gap between "restored" and "trusted"
<!-- chapter: ransomware-and-malicious-deletion, duration: 2h -->
* Ransomware and malicious deletion
    * threat model: insider deletion, attacker with admin
    * immutable backups and `Object Lock`
    * isolated backup accounts
    * detection of suspicious deletion patterns
    * recovery from ransomware specifically
    * cross-reference to the Security `IR` course
<!-- chapter: regulatory-and-compliance-dimension, duration: 2h -->
* Regulatory and compliance dimension
    * `SOC 2`, `ISO 27001`, `HIPAA`, `PCI-DSS` `DR` expectations
    * regulator-specified `RTO`/`RPO`
    * the audit interview
    * evidence: drill reports, runbook tests, retention
    * the gap between compliance and actual recovery capability
<!-- chapter: cost-of-disaster-recovery, duration: 2h -->
* Cost of disaster recovery
    * the cost of each `DR` posture
    * cross-region replication cost
    * standby capacity cost
    * restore-rarely vs always-warm tradeoffs
    * cross-reference to the Cloud Cost Optimization course
    * defending the `DR` budget
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * tabletop exercise: simulated region outage
    * group review of a real recovery runbook
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
