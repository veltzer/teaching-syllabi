---
tags:
  - security:compliance
  - security:privacy
  - concepts:gdpr
  - concepts:data-protection
level: beginner
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:managers
  - audiences:legal
---
<!-- course: gdpr_and_compliance -->
# `GDPR` and Compliance

## Description
The General Data Protection Regulation (`GDPR`) fundamentally changed how organizations collect, process, and protect personal data, imposing significant obligations on any business that handles data belonging to European residents. This course provides a comprehensive and practical introduction to `GDPR` — its principles, legal bases, data subject rights, breach notification requirements, and the accountability obligations it places on both controllers and processors. Participants will also gain an overview of related global privacy regulations including `CCPA`, `HIPAA`, and emerging data protection laws, enabling them to contribute to compliance programs with confidence. The course is designed for a mixed audience of technical, managerial, and legal professionals, bridging the gap between legal text and practical implementation.

## Duration
16 hours / 2 days

## Intended Audience
* Developers and engineers building systems that handle personal data
* Solution architects designing data flows and storage for `GDPR`-compliant systems
* Managers and product owners responsible for data-processing products and services
* Legal, compliance, and privacy professionals new to technology-focused privacy regulation

## Prerequisites
* No technical programming background is required
* Basic understanding of how web applications and databases work is helpful
* Familiarity with general business processes and the concept of customer data
* Awareness of the existence of data privacy as a concept is sufficient to begin

## Objectives
* Explain the scope, territorial reach, and core principles of `GDPR`
* Identify and apply an appropriate lawful basis for each personal data processing activity
* Describe and operationalize the eight data subject rights, including access, erasure, and portability
* Apply Privacy by Design and Privacy by Default principles to system and product design
* Outline the requirements for valid consent and the conditions for legitimate interest assessment
* Follow `GDPR` breach notification timelines and procedures for supervisory authorities and data subjects
* Draft and review Data Processing Agreements (`DPA`s) with third-party processors
* Assess the requirements for international personal data transfers under `GDPR`
* Define the role and responsibilities of a Data Protection Officer (`DPO`)
* Compare `GDPR` with `CCPA` and `HIPAA` to understand global privacy obligations

## Outline
<!-- chapter: introduction-to-data-privacy, duration: 1h -->
* Introduction to Data Privacy
    * Why privacy matters: individual rights, societal impact, and business trust
    * The history of data protection regulation: from `OECD` guidelines to `GDPR`
    * Key terminology: personal data, data subject, controller, processor, recipient
    * What counts as personal data: names, identifiers, location data, online identifiers, biometrics
    * Special categories of sensitive personal data and their heightened protections
    * The regulatory landscape: `GDPR`, `CCPA`, `LGPD`, `PDPA`, and the global patchwork
    * Consequences of non-compliance: fines, enforcement actions, and reputational damage

<!-- chapter: gdpr-principles-and-scope, duration: 2h -->
* `GDPR` Principles and Scope
    * Territorial scope: `when` `GDPR` applies to non-EU organizations (`Article 3`)
    * Material scope: what types of processing activities are covered
    * The seven principles of `GDPR`: lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, and accountability
    * Accountability as an active obligation: records of processing, policies, and controls
    * Roles in detail: data controllers vs data processors vs joint controllers
    * Supervisory authorities: structure, powers, and how enforcement works
    * Rights of natural persons vs legal persons under `GDPR`

<!-- chapter: lawful-bases-for-processing, duration: 2h -->
* Lawful Bases for Processing
    * The six lawful bases under `Article 6`: consent, contract, legal obligation, vital interests, public task, legitimate interests
    * Consent requirements: freely given, specific, informed, unambiguous indication
    * Consent mechanics: opt-in design, withdrawal mechanisms, and records of consent
    * Legitimate Interests Assessment (`LIA`): the three-part balancing test
    * Contract performance as a lawful basis: `when` it applies and its limits
    * Children's data and the age of digital consent across EU member states
    * Documenting lawful bases in Records of Processing Activities (`ROPA`)

<!-- chapter: data-subject-rights, duration: 2h -->
* Data Subject Rights
    * Overview of the eight data subject rights under `GDPR`
    * Right of access (`SAR`): what must be provided, timelines, and exemptions
    * Right to rectification: correcting inaccurate or incomplete personal data
    * Right to erasure ("right to be forgotten"): `when` it applies and `when` it does not
    * Right to restriction of processing and right to object
    * Right to data portability: technical requirements and common formats
    * Rights in relation to automated decision-making and profiling (`Article 22`)
    * Building operational processes to respond to data subject requests within 30 days

<!-- chapter: data-protection-by-design-and-default, duration: 2h -->
* Data Protection by Design and Default
    * `Article 25`: the legal obligation to embed privacy into systems and processes
    * Privacy by Design principles: proactive, embedded, respect for privacy as default
    * Practical techniques: data minimisation, pseudonymisation, anonymisation
    * Difference between pseudonymisation and anonymisation under `GDPR`
    * Privacy Impact Assessments and Data Protection Impact Assessments (`DPIA`)
    * `When` a `DPIA` is mandatory: high-risk processing activities
    * Embedding privacy reviews into product development and architecture review processes

<!-- chapter: data-breach-notification, duration: 1h -->
* Data Breach Notification
    * What constitutes a personal data breach under `GDPR` (`Article 4(12)`)
    * The 72-hour notification requirement to supervisory authorities
    * Risk-based thresholds: `when` notification to data subjects is required
    * Content of a breach notification: required information and structured format
    * Building an internal breach detection and escalation process
    * Documenting breaches in the breach register regardless of reporting obligation
    * Post-breach lessons learned and remediation obligations

<!-- chapter: third-party-processors-and-dpas, duration: 2h -->
* Third-Party Processors and DPAs
    * Controller-processor relationship and the responsibilities of each
    * `Article 28` requirements: what must be covered in a Data Processing Agreement
    * Standard contractual clauses (`SCC`) and their role in processor relationships
    * Due diligence on processors: security assessments and sub-processor oversight
    * Sub-processor chains: notification obligations and flow-down requirements
    * Joint controller arrangements: shared responsibility and documented allocation
    * Practical review of a sample `DPA` and identifying compliance gaps

<!-- chapter: international-data-transfers, duration: 2h -->
* International Data Transfers
    * The `GDPR` restriction on transfers to third countries (`Articles 44-49`)
    * Adequacy decisions: countries and territories with recognized protection levels
    * Standard Contractual Clauses (`SCCs`): the 2021 revised clauses and their modules
    * Binding Corporate Rules (`BCR`s) for intra-group international transfers
    * Transfer Impact Assessments (`TIA`): evaluating third-country legal frameworks
    * The `EU-US Data Privacy Framework` and its political and legal context
    * Derogations under `Article 49`: `when` exceptional transfers are permitted

<!-- chapter: dpo-role-and-responsibilities, duration: 1h -->
* DPO Role and Responsibilities
    * `When` a Data Protection Officer (`DPO`) is mandatory under `Article 37`
    * DPO independence, expertise requirements, and position within the organization
    * Core DPO tasks: monitoring compliance, providing advice, and cooperating with authorities
    * DPO as a point of contact for supervisory authorities and data subjects
    * Internal DPO vs outsourced DPO: pros, cons, and practical considerations
    * Protecting the DPO: non-penalisation and conflict-of-interest rules
    * Building a privacy governance structure around the DPO function

<!-- chapter: other-regulations-ccpa-hipaa-overview, duration: 1h -->
* Other Regulations — `CCPA`, `HIPAA` Overview
    * `California Consumer Privacy Act` (`CCPA`) and `CPRA`: scope, rights, and obligations
    * Key differences between `GDPR` and `CCPA`: opt-out model, business thresholds, categories
    * `HIPAA` (Health Insurance Portability and Accountability Act): who it applies to and what it protects
    * `HIPAA` Privacy Rule, Security Rule, and Breach Notification Rule essentials
    * Emerging global privacy laws: `Brazil LGPD`, `India DPDP Act`, `Canada PIPEDA`/`CPPA`
    * Building a global privacy compliance framework that addresses multiple jurisdictions
    * Practical guidance for multi-jurisdictional organizations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
