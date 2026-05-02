---
tags:
  - concepts:gitops
  - concepts:operations
  - concepts:best-practices
  - concepts:scalability
level: advanced
category: devops
duration_hours: 16
audience:
  - audiences:devops
  - audiences:senior-developers
  - audiences:sres
  - audiences:architects
---
<!-- course: configuration_management_at_scale -->
# Configuration Management at Scale

## Description
Application configuration — feature flags, runtime parameters, per-environment values, per-tenant
overrides, secrets — is one of the most-touched parts of any system, and one of the most likely root
causes of an incident. The catalog has `Feature Flags and Progressive Delivery`, `Secrets Management`,
the `IaC` courses, and the `12-Factor App` course. None of those is the focused course on the
discipline of operating application configuration at scale: where configuration lives, how it changes,
how change propagates, how it is validated, how it is audited, and how teams keep it from being the
next outage.

This two day course covers configuration management as a focused engineering practice. It covers the
canonical layers (build-time, deploy-time, runtime), the storage options (config files in `Git`,
`ConfigMaps`, etcd, Consul, `AWS AppConfig`, `Azure App Configuration`, dedicated services like
`LaunchDarkly` for flags), the schema-and-validation story, the change-propagation model (push vs
poll vs subscribe), the per-environment and per-tenant override pattern, the gradual-rollout model
(closely related to feature flags), the audit-and-rollback story, the secrets-vs-config split, the
multi-region story, the local-development story, and the patterns that `make` configuration changes
boring instead of the most-feared deploy. Examples include real production incidents caused by
configuration changes. Participants leave able to design the configuration layer for a non-trivial
system.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers operating production systems
* senior developers maintaining configuration code
* `SREs` reviewing configuration-change incidents
* architects designing configuration interfaces

## Prerequisites
* working experience with at least one production deployment
* exposure to the Feature Flags and Progressive Delivery course
* familiarity with the Secrets Management course is helpful
* basic understanding of `IaC`

## Objectives
* identify the canonical configuration layers
* pick the right storage for each layer
* validate configuration changes before they ship
* propagate change with the right model
* roll back configuration changes safely
* audit configuration history
* recognize when configuration changes are the wrong primitive

## Outline
<!-- chapter: why-configuration-causes-outages, duration: 1h -->
* Why configuration causes outages
    * the canonical incident: a flag flip took prod down
    * cross-reference to the Feature Flags and Progressive Delivery course
    * the "it was a config change, we did not need a code review" reality
    * the public examples: `Cloudflare`, Reddit, `GCP`, `AWS` outages
    * configuration as deployable code
<!-- chapter: the-canonical-layers, duration: 2h -->
* The canonical layers
    * build-time configuration
    * deploy-time configuration
    * runtime configuration
    * picking the layer per setting
    * the "we baked a value into the binary that needed to change weekly" failure
<!-- chapter: storage-options, duration: 2h -->
* Storage options
    * `Git`-managed config files (the `12-Factor` heritage)
    * `Kubernetes` ConfigMap and `Secret`
    * `etcd`, Consul, `Zookeeper`
    * `AWS AppConfig`, `Azure App Configuration`, `GCP Secret Manager` for config
    * dedicated services: `LaunchDarkly`, Statsig, Unleash, `GrowthBook`
    * picking
<!-- chapter: schema-and-validation, duration: 2h -->
* Schema and validation
    * the typed-config-object pattern
    * `JSON Schema`, Cue, Pkl, `Dhall`
    * the `CI` validator
    * the deploy-time validator
    * the runtime validator
    * the "we shipped a typo and crashed every pod on restart" failure
<!-- chapter: change-propagation, duration: 2h -->
* Change propagation
    * push: the deploy
    * poll: the periodic refresh
    * subscribe: the long-lived watch
    * the propagation latency-vs-cost trade-off
    * the "the config changed but the service did not pick it up for an hour" reality
<!-- chapter: per-environment-and-per-tenant, duration: 1h -->
* Per-environment and per-tenant
    * the override hierarchy
    * the default-and-overlay pattern
    * the per-tenant configuration risk
    * the "we shipped a tenant-specific change to everyone" failure
    * the testing strategy for overrides
<!-- chapter: gradual-rollout, duration: 1h -->
* Gradual rollout
    * percentage rollout
    * per-cohort rollout
    * the canary-config-change pattern
    * cross-reference to the Feature Flags and Progressive Delivery course
    * the "we changed the flag for 100 percent and it broke" failure
<!-- chapter: audit-and-rollback, duration: 1h -->
* Audit and rollback
    * the change-history log
    * the who-changed-what audit
    * the rollback-to-previous primitive
    * the "we cannot tell what changed before the outage" reality
    * the time-bounded change-window
<!-- chapter: secrets-vs-configuration, duration: 1h -->
* Secrets vs configuration
    * the boundary
    * the cost of treating everything as a secret
    * cross-reference to the Secrets Management course
    * the "we put a secret in `ConfigMap`" disaster
    * the rotation question for both
<!-- chapter: multi-region-and-multi-cluster, duration: 1h -->
* Multi-region and multi-cluster
    * the per-region propagation
    * the global-vs-regional configuration question
    * the failure when one region's config diverges
    * cross-reference to the Multi-Region Architecture course
    * the convergence guarantee
<!-- chapter: configuration-in-development, duration: 1h -->
* Configuration in development
    * the local-overlay
    * the secret-in-development question
    * the "the dev environment did not match prod" debugging cost
    * the test-environment management
    * the local-development pattern
<!-- chapter: the-incident-of-a-config-change, duration: 1h -->
* The incident of a config change
    * the timeline reconstruction
    * the "this was a config change, not a code change" misconception
    * the response runbook
    * the postmortem template
    * cross-reference to the Incident Response and Postmortems course

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
