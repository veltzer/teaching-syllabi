---
tags:
  - security:security
  - concepts:architecture
  - concepts:best-practices
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
  - audiences:architects
  - audiences:managers
---
<!-- course: threat_modeling -->
# Threat Modeling

## Description
Threat modeling is a structured approach to identifying, quantifying, and addressing security risks in software systems. This course covers the major threat modeling methodologies including STRIDE, DREAD, PASTA, and LINDDUN, along with practical techniques for creating data flow diagrams, identifying trust boundaries, and building attack trees. Participants will apply these techniques to real-world architectures including `microservices`, cloud, and APIs.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers building secure applications
* Security engineers and analysts
* Software and solution architects
* `DevSecOps` engineers integrating security into pipelines
* Technical leads responsible for application security
* Product managers who need to understand security risks

## Prerequisites
* Understanding of software architecture and `design patterns`
* Basic knowledge of web application architecture (`HTTP`, `REST`, databases)
* Familiarity with common security concepts (authentication, authorization, encryption)
* Understanding of networking basics (`TCP`/`IP`, firewalls, `DNS`)
* Experience with at least one software development lifecycle

## Objectives
* Understand threat modeling fundamentals and when to apply them
* Create data flow diagrams and identify trust boundaries
* Apply the STRIDE methodology to systematically identify threats
* Use DREAD for risk rating and prioritization
* Build attack trees to analyze complex threat scenarios
* Apply PASTA for risk-centric threat analysis
* Use LINDDUN for privacy-specific threat modeling
* Perform threat modeling for `microservices`, cloud, and `API` architectures
* Integrate threat modeling into the software development lifecycle
* Use threat modeling tools effectively

## Outline
<!-- chapter: threat-modeling-fundamentals, duration: 1h -->
* Threat Modeling Fundamentals
    * What is threat modeling and why it matters
    * `When` to perform threat modeling in the development process
    * Threat modeling scope and boundaries
    * Attacker profiles and motivation
    * Security assumptions and constraints
    * Iterative threat modeling and maintaining threat models
<!-- chapter: data-flow-diagrams, duration: 1h -->
* Data Flow Diagrams
    * Elements of data flow diagrams (processes, data stores, data flows, external entities)
    * Creating multi-level data flow diagrams
    * Identifying and documenting data flows
    * Diagramming distributed systems
    * Tools for creating data flow diagrams
<!-- chapter: trust-boundaries, duration: 1h -->
* Trust Boundaries
    * Defining trust boundaries in system architecture
    * Network boundaries, process boundaries, and privilege boundaries
    * Trust boundary analysis for multi-tier applications
    * Cloud-specific trust boundaries
    * Documenting trust assumptions
<!-- chapter: stride-methodology, duration: 1h -->
* STRIDE Methodology
    * Spoofing identity threats and mitigations
    * Tampering with data threats and mitigations
    * Repudiation threats and mitigations
    * Information disclosure threats and mitigations
    * Denial of service threats and mitigations
    * Elevation of privilege threats and mitigations
    * STRIDE-per-element and STRIDE-per-interaction approaches
<!-- chapter: dread-risk-rating, duration: 1h -->
* DREAD Risk Rating
    * Damage potential assessment
    * Reproducibility evaluation
    * Exploitability analysis
    * Affected users estimation
    * Discoverability assessment
    * Calculating and comparing DREAD scores
    * Limitations and alternatives to DREAD
<!-- chapter: attack-trees, duration: 1h -->
* Attack Trees
    * Building attack trees from root goals
    * AND/OR nodes and attack tree logic
    * Annotating attack trees with cost, probability, and difficulty
    * Using attack trees for risk analysis
    * Combining attack trees with other methodologies
<!-- chapter: pasta-process-for-attack-simulation-and-threat-analysis, duration: 1h -->
* PASTA (Process for Attack Simulation and Threat Analysis)
    * Stage 1: Define objectives
    * Stage 2: Define technical scope
    * Stage 3: Application decomposition
    * Stage 4: Threat analysis
    * Stage 5: Vulnerability and weakness analysis
    * Stage 6: Attack modeling and simulation
    * Stage 7: Risk and impact analysis
<!-- chapter: linddun-privacy-threats, duration: 2h -->
* LINDDUN (Privacy Threats)
    * Linkability threats
    * Identifiability threats
    * Non-repudiation (unwanted) threats
    * Detectability threats
    * Disclosure of information threats
    * Unawareness threats
    * Non-compliance threats
    * Mapping LINDDUN to privacy regulations (`GDPR`)
<!-- chapter: threat-modeling-tools, duration: 1h -->
* Threat Modeling Tools
    * `Microsoft Threat Modeling Tool`
    * `OWASP Threat Dragon`
    * IriusRisk for automated threat modeling
    * Diagram-as-code approaches (Threagile)
    * Choosing the right tool for your workflow
<!-- chapter: threat-modeling-for-microservices, duration: 1h -->
* Threat Modeling for `Microservices`
    * Service-to-service communication threats
    * `API gateway` security considerations
    * Service mesh security boundaries
    * Container and orchestration layer threats
    * Distributed authentication and authorization threats
<!-- chapter: threat-modeling-for-cloud, duration: 1h -->
* Threat Modeling for Cloud
    * Cloud shared responsibility model and threat implications
    * `IAM` and identity-related threats
    * Storage and data access threats
    * Network configuration and exposure threats
    * Serverless and managed service threats
    * Multi-cloud and hybrid cloud considerations
<!-- chapter: threat-modeling-for-apis, duration: 1h -->
* Threat Modeling for APIs
    * `REST` `API` threat surface
    * `GraphQL` security considerations
    * `API` authentication and authorization threats
    * Input validation and injection threats
    * Rate limiting and abuse scenarios
    * `WebSocket` and real-time `API` threats
<!-- chapter: integrating-threat-modeling-into-the-sdlc, duration: 1h -->
* Integrating Threat Modeling into the `SDLC`
    * Threat modeling in `agile` and `DevOps` workflows
    * Lightweight and incremental threat modeling
    * Automating threat model updates
    * Connecting threat models to issue trackers
    * Security sprints and threat model reviews
<!-- chapter: threat-libraries, duration: 1h -->
* Threat Libraries
    * Common threat libraries and catalogs
    * Industry-specific threat catalogs
    * Building and maintaining organizational threat libraries
    * Mapping threats to `MITRE ATT&CK` framework
<!-- chapter: prioritization-and-remediation, duration: 1h -->
* Prioritization and Remediation
    * Risk-based prioritization of identified threats
    * Mitigation strategies and security controls
    * Accepting, transferring, and avoiding risks
    * Tracking remediation progress
    * Validating mitigations through testing

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
