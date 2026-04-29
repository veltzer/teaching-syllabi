---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:best-practices
  - concepts:operations
level: advanced
category: security
duration_hours: 32
audience:
  - audiences:security-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:developers
---
<!-- course: cryptographic_engineering -->
# Cryptographic Engineering

## Description
The catalog has `Cryptography Fundamentals` (the theory course), `PKI and Certificates`, `Secrets
Management`, and the per-vendor ``Vault`` course. None of those is the focused course on the
engineering of cryptography in production systems: not "what is `AES`" but "we need to encrypt
customer data at `rest`, what library, what key, what mode, and how do we rotate it without
re-encrypting everything." Cryptography in production fails not because the algorithms are weak but
because the operational decisions around them are wrong: keys leak, key rotation is impossible, the
nonce is reused, the random source is weak, the library is misused, the mode is wrong, the cipher
is deprecated, and the path from "we want to encrypt this" to "we shipped it without a vulnerability"
is unforgiving.

This four day course covers cryptographic engineering as practiced today. It covers the canonical
primitives and their misuse cases (`AES-GCM` with reused nonces, `RSA` with `PKCS1v15` padding,
`HMAC` with timing-leaking comparison, the random-source mistake), the modern primitives
(`ChaCha20-Poly1305`, `Ed25519`, `X25519`, `Argon2`, `HKDF`), the libraries (`libsodium`, `Tink`,
`AWS KMS Encryption SDK`, `Tink for Go`, `cryptography.io`), the key-management infrastructure (`KMS`
across major clouds, `HashiCorp Vault`, `Hardware Security Modules`), the envelope-encryption pattern,
the rotation story, the at-`rest` vs in-transit story, the application-level encryption (`when`, where,
how), the end-to-end encryption design, the post-quantum migration plan, and the patterns that `make`
cryptographic systems survive contact with reality. Examples include real production deployments and
real production failures. Participants leave able to `make` the cryptographic engineering decisions
without reaching for a Stack Overflow snippet.

## Duration
32 hours / 4 days

## Intended Audience
* security engineers reviewing cryptographic designs
* senior developers shipping cryptographic features
* architects designing systems with strong-confidentiality requirements
* developers handling personal or financial data

## Prerequisites
* exposure to the Cryptography Fundamentals course
* working experience in at least one general-purpose language
* familiarity with the Secrets Management course
* basic understanding of `TLS` and `PKI`

## Objectives
* pick the right cryptographic primitive for a given problem
* use a high-level library safely
* design a key-management plan with rotation
* apply envelope encryption correctly
* design an end-to-end encryption protocol
* operate cryptographic systems in production
* plan the post-quantum migration

## Outline
<!-- chapter: why-cryptographic-engineering-is-its-own-discipline, duration: 1h -->
* Why cryptographic engineering is its own discipline
    * the algorithms are not the problem
    * the operations around them are
    * cross-reference to the Cryptography Fundamentals course
    * the canonical disasters: nonce reuse, weak randomness, padding `oracle`
    * the rule: do not invent
<!-- chapter: the-canonical-primitives-and-their-misuse, duration: 3h -->
* The canonical primitives and their misuse
    * `AES-GCM` and the nonce problem
    * `AES-CBC` and the padding-`oracle` attack
    * `RSA-PKCS1v15` and `RSA-OAEP`
    * `ECDSA` and the nonce reuse
    * `HMAC` and the timing-leaking comparison
    * the random-number generator: getting it right
<!-- chapter: modern-primitives, duration: 2h -->
* Modern primitives
    * `ChaCha20-Poly1305`
    * `Ed25519` and `X25519`
    * `Argon2` and password hashing
    * `HKDF` for key derivation
    * `AES-GCM-SIV` for nonce-misuse resistance
    * picking the modern primitive
<!-- chapter: high-level-libraries, duration: 3h -->
* High-level libraries
    * `libsodium` and `NaCl`
    * `Tink` (`Google`)
    * `AWS Encryption SDK`
    * `cryptography.io` (`Python`)
    * `BoringSSL` and `OpenSSL` underneath
    * the rule: prefer high-level
<!-- chapter: key-management-infrastructure, duration: 3h -->
* Key-management infrastructure
    * `AWS KMS`, `Azure Key Vault`, `GCP KMS`
    * `HashiCorp Vault`
    * `Hardware Security Modules` (`HSMs`)
    * `Cloud HSM` offerings
    * the per-tenant key question
    * cross-reference to the Secrets Management course
<!-- chapter: envelope-encryption, duration: 2h -->
* Envelope encryption
    * the data-key and the key-encryption-key
    * the rotation story
    * the `KMS` integration pattern
    * the "we encrypted with the master key directly" anti-pattern
    * worked example
<!-- chapter: key-rotation, duration: 2h -->
* Key rotation
    * the rotation policy
    * the re-encryption-on-rotation question
    * the key-versioning approach
    * the "we cannot rotate because re-encryption would take a year" reality
    * the lazy re-encryption pattern
<!-- chapter: encryption-at-rest, duration: 2h -->
* Encryption at `rest`
    * the disk-level encryption (cloud-managed)
    * the database-level encryption
    * the field-level encryption
    * picking the level
    * the "we encrypted at the disk and an attacker stole an unlocked instance" reality
<!-- chapter: encryption-in-transit, duration: 2h -->
* Encryption in transit
    * `TLS` 1.3 as the baseline
    * the certificate-management story
    * cross-reference to the `PKI` and Certificates course
    * the `mTLS` pattern
    * cross-reference to the Zero Trust Networking and `mTLS` course
    * the "we ran `TLS` 1.0" embarrassment
<!-- chapter: application-level-encryption, duration: 2h -->
* Application-level encryption
    * `when` in-transit-and-at-`rest` is not enough
    * the searchable-encryption problem
    * `format-preserving encryption`
    * `tokenization` as the pragmatic alternative
    * the "we cannot decrypt because we lost the key" disaster
<!-- chapter: end-to-end-encryption, duration: 3h -->
* End-to-end encryption
    * the principle: only the endpoints have the key
    * the key-distribution problem
    * `Signal Protocol` as the canonical example
    * group `E2EE` and the `MLS` standard
    * the "we said `E2EE` but the server has the keys" misrepresentation
    * worked example
<!-- chapter: post-quantum-readiness, duration: 2h -->
* Post-quantum readiness
    * the harvest-now-decrypt-later threat
    * the `NIST` post-quantum standards
    * the migration plan
    * cross-reference to the Post-Quantum Cryptography course
    * the "we will deal with it later" failure
<!-- chapter: random-numbers-in-practice, duration: 1h -->
* Random numbers in practice
    * `/dev/urandom` and the `getrandom` syscall
    * the language standard libraries
    * the embedded-systems random problem
    * the "we used `Math.random()` for a session token" disaster
    * the entropy-on-boot question
<!-- chapter: cryptographic-code-review, duration: 1h -->
* Cryptographic code review
    * what to look for
    * the timing-channel
    * the side-channel
    * the test that proves correctness
    * the third-party audit
<!-- chapter: incident-response-for-crypto-failures, duration: 2h -->
* Incident response for crypto failures
    * the leaked key
    * the disclosed vulnerability in a library
    * the rotation-now scenario
    * cross-reference to the Incident Response and Postmortems course
    * the "we discovered we had been encrypting with `null`" reality
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * the `Heartbleed` aftermath
    * the `WhatsApp` `E2EE` design
    * the `iCloud` `Advanced Data Protection` design
    * the `Zoom` `E2EE` rollout
    * recommended reading: `Cryptography Engineering` (`Ferguson` et al.), `latacora/blog`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
