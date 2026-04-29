---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:best-practices
  - concepts:migration
level: advanced
category: security
duration_hours: 16
audience:
  - audiences:security-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:developers
---
<!-- course: post_quantum_cryptography -->
# Post-Quantum Cryptography

## Description
The catalog has `Cryptography Fundamentals`, `Cryptographic Engineering`, `PKI and Certificates`, and
`Web3 and Blockchain Security`. None of those is the focused course on the post-quantum (`PQ`)
transition: what `NIST` standardized in 2024, what the harvest-now-decrypt-later threat actually
implies for a deployed system, what the migration plan looks like for a real organization, and what
the cost of getting it wrong (or doing nothing) is. This is now an active engineering topic, not a
research one. `Cloudflare`, `Google`, and `Apple` have shipped `PQ` `TLS`. `AWS KMS` has hybrid
`PQ` key-exchange. `OpenSSH` 9.0+ has hybrid post-quantum key exchange by default. The migration is
real and the timeline is short.

This two day course covers post-quantum cryptography from a practical engineering perspective. It
covers the threat (a sufficiently large quantum computer breaks `RSA`, `Diffie-Hellman`, `ECDSA`,
`ECDH`), the harvest-now-decrypt-later attack model, the `NIST` standards (`ML-KEM` formerly `Kyber`,
`ML-DSA` formerly `Dilithium`, `SLH-DSA` formerly `SPHINCS+`, the deprecated `FALCON` waiting
standardization), the hybrid mode as the migration approach, the per-use-case migration (transport
encryption, signatures, long-term-confidential data, code signing, certificate hierarchies), the
performance and size implications, the deployment landscape today, the timeline pressure (`NSA`'s
`CNSA 2.0` mandate, regulator deadlines), and the patterns that work for a real migration. Examples
cover real `PQ` deployments. Participants leave able to plan and execute a `PQ` migration for their
systems.

## Duration
16 hours / 2 days

## Intended Audience
* security engineers planning a `PQ` migration
* senior developers shipping cryptographic systems
* architects designing systems with long-confidentiality requirements
* developers in regulated industries facing a `PQ` deadline

## Prerequisites
* exposure to the Cryptography Fundamentals course
* familiarity with the Cryptographic Engineering course
* basic understanding of `TLS` and `PKI`
* working knowledge of at least one general-purpose language

## Objectives
* explain the quantum threat and its real timeline
* identify systems vulnerable to harvest-now-decrypt-later
* pick the right `NIST` standard for a given use case
* deploy hybrid `PQ` `TLS` and `KEX`
* plan a multi-year migration
* manage the performance and size cost
* recognize the patterns that doom `PQ` migrations

## Outline
<!-- chapter: the-quantum-threat-in-practical-terms, duration: 1h -->
* The quantum threat in practical terms
    * `Shor`'s algorithm and what it breaks
    * `Grover`'s algorithm and the symmetric impact
    * the timeline question and the disagreement
    * cross-reference to the Cryptographic Engineering course
    * what is and is not at risk
<!-- chapter: harvest-now-decrypt-later, duration: 1h -->
* Harvest-now-decrypt-later
    * the attacker records ciphertext today
    * the attacker decrypts `when` a quantum computer arrives
    * which data this matters for
    * the "we have nothing confidential for 20 years" comfort and its limits
    * who is collecting today
<!-- chapter: the-nist-pq-standards, duration: 2h -->
* The `NIST` `PQ` standards
    * `ML-KEM` (formerly `Kyber`) for key encapsulation
    * `ML-DSA` (formerly `Dilithium`) for signatures
    * `SLH-DSA` (formerly `SPHINCS+`) for hash-based signatures
    * `FALCON` and the standardization roadmap
    * `FIPS 203`, `FIPS 204`, `FIPS 205`
    * the rejected algorithms and lessons
<!-- chapter: hybrid-as-the-migration-approach, duration: 2h -->
* Hybrid as the migration approach
    * the principle: classical plus `PQ` together
    * the per-handshake combination
    * `Cloudflare` and `Google`'s hybrid `TLS` deployment
    * `AWS KMS` hybrid `KEM`
    * the no-regression-if-one-breaks property
<!-- chapter: pq-tls-deployment, duration: 2h -->
* `PQ` `TLS` deployment
    * the current state of `TLS 1.3` `PQ` extension
    * `OpenSSL` 3.x support
    * `BoringSSL` support
    * `Java` and `Bouncy Castle`
    * the "the client did not negotiate `PQ`" reality
<!-- chapter: pq-key-exchange-in-ssh-and-vpn, duration: 1h -->
* `PQ` key exchange in `SSH` and `VPN`
    * `OpenSSH` 9.0+ hybrid `KEX`
    * `WireGuard`'s position
    * `IKEv2` and the `PQ` key exchange
    * cross-reference to the `VPN` and `WireGuard` course
    * the operational reality
<!-- chapter: pq-signatures-and-pki, duration: 2h -->
* `PQ` signatures and `PKI`
    * the certificate-size problem
    * the chain-size cost
    * code signing and the long-validity problem
    * `SLH-DSA` for very long-validity signatures
    * cross-reference to the `PKI` and Certificates course
<!-- chapter: long-term-confidential-data, duration: 1h -->
* Long-term confidential data
    * archived data
    * legal-records data
    * `PQ` re-encryption strategies
    * the "we did not migrate the archive and it is still vulnerable" reality
    * the per-data-class plan
<!-- chapter: performance-and-size-costs, duration: 1h -->
* Performance and size costs
    * `ML-KEM` key and ciphertext sizes
    * `ML-DSA` signature sizes
    * `SLH-DSA` very large signatures
    * the latency impact on handshakes
    * the network-and-storage cost
<!-- chapter: regulatory-and-mandate-landscape, duration: 1h -->
* Regulatory and mandate landscape
    * `NSA`'s `CNSA 2.0` requirements and timeline
    * `NIST`'s deprecation timeline
    * the `EU` and `UK` positions
    * industry-specific deadlines
    * the audit-readiness story
<!-- chapter: building-a-migration-plan, duration: 1h -->
* Building a migration plan
    * the cryptographic-inventory step
    * the per-system priority
    * the hybrid-first rollout
    * the libraries-and-vendors `check`
    * the multi-year roadmap
<!-- chapter: testing-and-validation, duration: 1h -->
* Testing and validation
    * the test vectors
    * the interoperability test
    * the side-channel testing
    * the implementation-review requirement
    * the "we used a non-standard implementation" trap

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
