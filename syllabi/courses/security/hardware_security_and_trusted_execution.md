---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:systems-programming
  - concepts:best-practices
level: advanced
category: security
duration_hours: 24
audience:
  - audiences:security-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:embedded-developers
---
<!-- course: hardware_security_and_trusted_execution -->
# Hardware Security and Trusted Execution

## Description
Hardware-rooted security — the `TPM`, the secure element, the `HSM`, the `TEE`, confidential computing
on `SEV-SNP`, `TDX`, and the `Apple Secure Enclave` — has gone from "the right thing for some
specialized cases" to "the foundation of consumer device security and increasingly of cloud workloads."
The catalog has `Cryptography Fundamentals`, `Cryptographic Engineering`, `Embedded Systems Security`,
`PKI and Certificates`, `Identity and Access Management`, and `Working with LLMs Securely`. None of
those is the focused course on hardware-backed trust: what these primitives actually do, how they
attest to a verifier, how a system designs around them, and the failure modes `when` they are
misunderstood.

This three day course covers hardware-rooted security and trusted execution as a focused engineering
practice. It covers the hardware primitives (`TPM 2.0`, secure elements, `HSMs`, `TEEs`), the
`Trusted Execution Environments` on the major platforms (`Intel SGX`, `Intel TDX`, `AMD SEV-SNP`,
`Arm CCA`, `Apple Secure Enclave`), the `Confidential Computing` model (cloud `VMs` with verified
runtime attestation), the attestation protocol (what the verifier checks and how), the `Confidential
Computing Consortium` standards, the application-level integration (`Microsoft Always Encrypted with
Secure Enclaves`, `Google Confidential VMs`, ``AWS` Nitro Enclaves`), the ``WebAuthn`` and `passkey`
foundations on hardware, the `mTLS`-with-hardware-key story, the operational realities, and the
patterns that distinguish "we have hardware-backed security" from "we have a checkbox." Examples cover
real production systems. Participants leave able to design a system that uses hardware trust
deliberately.

## Duration
24 hours / 3 days

## Intended Audience
* security engineers designing systems with hardware-backed trust
* senior developers shipping confidential computing or remote attestation
* architects responsible for trust boundaries
* embedded developers using `TPMs`, `HSMs`, or secure elements

## Prerequisites
* exposure to the Cryptography Fundamentals course
* familiarity with `PKI` and Certificates course
* basic understanding of `Linux` boot and `UEFI`
* working experience with at least one cloud provider helps

## Objectives
* explain the hardware primitives and their differences
* design a system that uses a `TPM`, `HSM`, or `TEE` correctly
* implement remote attestation
* deploy a confidential-computing workload
* integrate hardware-backed keys into `TLS` and signing
* recognize the threats hardware does not protect against
* compare the major `TEE` platforms

## Outline
<!-- chapter: the-hardware-primitives, duration: 2h -->
* The hardware primitives
    * `TPM 2.0` and what a `TPM` is
    * secure elements (`smartcards`, mobile `SE`)
    * `HSMs` for server-side
    * `TEEs` for in-`CPU` isolation
    * `HSM` vs `TEE` vs `TPM` — picking
    * cross-reference to the Cryptographic Engineering course
<!-- chapter: tpm-2-0-deep-dive, duration: 2h -->
* `TPM 2.0` deep dive
    * the platform-configuration registers (`PCRs`)
    * the endorsement key, the attestation key
    * `tpm2-tools` in practice
    * sealing and unsealing
    * measured boot and attestation
    * the "we never used the `TPM`" reality
<!-- chapter: hsms-in-production, duration: 2h -->
* `HSMs` in production
    * `Cloud HSM` offerings
    * `Thales`, `Utimaco`, `nCipher` on-prem
    * `FIPS 140-3` and what it means
    * the operational cost
    * the buy-vs-cloud question
<!-- chapter: intel-sgx-and-its-history, duration: 2h -->
* Intel `SGX` and its history
    * the enclave model
    * the side-channel attacks
    * `SGX`'s deprecation in client `CPUs`
    * what survived: `SGX2` on server
    * the lessons learned
<!-- chapter: intel-tdx, duration: 2h -->
* Intel `TDX`
    * the trust domain model
    * the entire-`VM`-as-enclave approach
    * the attestation flow
    * deployment in `Azure` and `Google Cloud`
    * the comparison with `SEV-SNP`
<!-- chapter: amd-sev-snp, duration: 2h -->
* `AMD SEV-SNP`
    * the secure encrypted virtualization model
    * `SEV-SNP`'s integrity protection
    * `Azure Confidential VMs`
    * `AWS` and `GCP` adoption
    * the maturity story
<!-- chapter: arm-cca-and-realms, duration: 1h -->
* `Arm` `CCA` and realms
    * the `Confidential Compute Architecture`
    * the realm vs normal world
    * the rollout timeline
    * the comparison with `TrustZone`
    * the future `Arm` server story
<!-- chapter: apple-secure-enclave, duration: 1h -->
* Apple Secure Enclave
    * the `SEP` model
    * `iOS` and `macOS` integration
    * `passkey` and `WebAuthn` on `SEP`
    * the no-export-of-keys property
    * the developer-facing story
<!-- chapter: remote-attestation, duration: 3h -->
* Remote attestation
    * what attestation actually proves
    * the verifier
    * the `RATS` `IETF` standard
    * `Veraison`, `Microsoft Azure Attestation`, `Google Confidential Space`
    * the integration with the application
    * the "we deployed in a `TEE` and never verified it" failure
<!-- chapter: confidential-computing-deployments, duration: 2h -->
* Confidential computing deployments
    * `Azure Confidential VMs`
    * `Google Confidential VMs` and `Confidential Space`
    * `AWS Nitro Enclaves`
    * the application-level integration
    * the "we did the work for nothing because we never attested" reality
<!-- chapter: hardware-backed-keys-in-tls, duration: 2h -->
* Hardware-backed keys in `TLS`
    * the private key on the `HSM`
    * the per-handshake `HSM` round-trip cost
    * the `KMS`-as-signer pattern
    * cross-reference to the `mTLS` course
    * the rotation story
<!-- chapter: webauthn-and-passkeys-on-hardware, duration: 1h -->
* `WebAuthn` and `passkeys` on hardware
    * `FIDO2` and the platform authenticator
    * the per-credential-on-`SEP`-or-`TPM` flow
    * the cross-device passkey flow
    * cross-reference to the Identity and Access Management course
    * the production integration
<!-- chapter: what-hardware-does-not-protect-against, duration: 1h -->
* What hardware does not protect against
    * the side-channel reality
    * the firmware-update threat
    * the supply-chain threat
    * the "we trusted hardware that we did not actually verify" trap
    * the threat model the hardware does and does not address
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * `Apple`'s `Advanced Data Protection` for `iCloud`
    * `Signal`'s contact-discovery on `SGX`
    * `Cloudflare`'s `Geo Key Manager`
    * `Confidential AI` deployments
    * recommended reading: `CCC` whitepapers, `RATS` `RFC`s

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
