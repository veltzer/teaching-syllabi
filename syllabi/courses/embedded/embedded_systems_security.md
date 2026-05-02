---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:certificates
  - concepts:pki
  - concepts:identity
level: advanced
category: embedded
duration_hours: 40
audience:
  - audiences:embedded-developers
  - audiences:firmware-developers
  - audiences:security-engineers
  - audiences:architects
---
<!-- course: embedded_systems_security -->
# Embedded Systems Security

## Description
Embedded systems are increasingly attractive targets, increasingly connected, and increasingly subject to
regulation that did not exist a decade ago. The security techniques that work for cloud workloads do not
transfer cleanly: there is no `WAF` in front of a thermostat, no centralized identity provider for a fleet
of pacemakers, no easy patching for a deployed industrial controller, and side-channel attacks that web
developers never have to think about become first-order concerns.

This five day course covers embedded security as its own discipline. It covers the threat model unique to
embedded systems, secure boot and chain-of-trust, hardware-backed keys and attestation, side-channel and
fault-injection attacks, firmware signing and `OTA` security, secure communication for resource-constrained
devices, and the regulatory dimension (`UNECE WP.29`, `IEC 62443`, `EU Cyber Resilience Act`, `FDA` guidance).
Examples are drawn from `ARM TrustZone`, secure elements, and modern `MCU` security features. Participants
leave able to design and ship embedded systems with a coherent security story rather than a checklist of
unrelated mitigations.

## Duration
40 hours / 5 days

## Intended Audience
* embedded and firmware developers shipping connected products
* security engineers expanding into embedded
* architects designing the security story of a hardware product
* engineers preparing for an embedded-security audit or certification

## Prerequisites
* working knowledge of C or `C++`
* basic embedded development experience
* basic familiarity with cryptographic primitives (hash, signature, symmetric vs asymmetric)
* exposure to at least one `MCU` family is helpful

## Objectives
* describe the embedded threat model precisely
* implement secure boot and a chain of trust on real hardware
* use hardware-backed keys and remote attestation correctly
* design firmware signing and `OTA` update systems
* mitigate side-channel and fault-injection attacks
* meet the major embedded-security regulatory requirements
* respond to a deployed-fleet security incident

## Outline
<!-- chapter: the-embedded-threat-model, duration: 2h -->
* The embedded threat model
    * the attacker has the hardware
    * physical, local-network, remote attackers
    * supply chain as part of the threat model
    * the lifecycle: development, manufacturing, field, decommission
    * what cloud-style mitigations do and do not transfer
<!-- chapter: secure-boot-and-chain-of-trust, duration: 4h -->
* Secure boot and chain of trust
    * the root of trust on `MCU` and `SoC`
    * boot ROM, first-stage bootloader, second-stage, OS
    * hashing, signing, anchoring
    * `ARM TrustZone-M` for `Cortex-M`
    * `ARM TrustZone-A` for `Cortex-A`
    * `Intel Boot Guard`, `AMD Platform Secure Boot`
    * key revocation and rollback protection
    * common secure-boot mistakes
<!-- chapter: hardware-backed-keys-and-secure-elements, duration: 3h -->
* Hardware-backed keys and secure elements
    * `OTP` fuses for device identity
    * `TPM` for `MCU`-class systems
    * secure elements: `ATECC608`, `Microchip Trust Platform`, `NXP EdgeLock`
    * `PUFs` (physically unclonable functions)
    * key provisioning at manufacture
    * key rotation in the field
<!-- chapter: remote-attestation, duration: 2h -->
* Remote attestation
    * what attestation actually proves
    * `RATS` (`IETF`) attestation architecture
    * `EAT` and entity attestation tokens
    * `PSA` attestation for `Arm`-based devices
    * verifying firmware version remotely
    * attestation in `OTA` flows
<!-- chapter: firmware-signing-and-ota, duration: 4h -->
* Firmware signing and `OTA`
    * signing keys and the `HSM` story
    * signature verification at boot vs at update
    * `A`/`B` partition update model
    * fail-safe rollback
    * `delta` updates for low-bandwidth devices
    * `Mender`, RAUC, swupdate, SUOTA (`BLE`)
    * `OTA` from `AWS IoT`, `Azure IoT Hub`, `Google Cloud IoT`
    * the legacy device that cannot be updated
<!-- chapter: secure-communication-for-constrained-devices, duration: 3h -->
* Secure communication for constrained devices
    * `TLS` 1.3 vs `DTLS` 1.3
    * `mTLS` for device-to-cloud
    * pre-shared key (`PSK`) modes
    * `OSCORE` and EDHOC for `CoAP`
    * `MQTT` over `TLS`
    * `LoRaWAN` security model
    * cross-reference to the Zero Trust Networking course
<!-- chapter: cryptography-on-mcus, duration: 3h -->
* Cryptography on `MCUs`
    * hardware crypto accelerators on modern `MCUs`
    * the `mbedTLS`, wolfSSL, `tinycrypt` libraries
    * key sizes for resource-constrained devices
    * `ECC` over `RSA` for embedded
    * post-quantum readiness for embedded
    * common cryptographic implementation mistakes
<!-- chapter: side-channel-attacks, duration: 3h -->
* Side-channel attacks
    * timing attacks
    * power-analysis attacks (`SPA`, `DPA`)
    * electromagnetic side-channels
    * cache-based side-channels in shared `SoCs`
    * countermeasures: constant-time code, masking, blinding
    * realistic threat assessment for your product
<!-- chapter: fault-injection-and-glitching, duration: 2h -->
* Fault injection and glitching
    * voltage and clock glitching
    * laser and `EM` fault injection
    * effects: bypassed checks, leaked keys, instruction skipping
    * countermeasures: redundancy, double-check critical operations
    * glitch detectors in modern `MCUs`
<!-- chapter: secure-storage-of-data-at-rest, duration: 2h -->
* Secure storage of data at `rest`
    * encrypted flash and external memory
    * key management for storage encryption
    * anti-tamper switches and self-erase
    * data protection during decommission
    * the difference between storage encryption and secure boot
<!-- chapter: hardening-the-os-and-the-application, duration: 2h -->
* Hardening the OS and the application
    * `MPU`/`MMU` use on `MCUs`
    * memory-safe languages: Rust for embedded
    * `stack canaries`, `ASLR` on capable `MCUs`
    * privilege separation in `RTOS`
    * cross-reference to the embedded Rust course
<!-- chapter: ota-key-and-credential-lifecycle, duration: 2h -->
* `OTA` key and credential lifecycle
    * device-onboarding flows: `FDO`, EST, `BRSKI`
    * device identity rotation
    * fleet-wide credential rotation
    * compromised-device revocation
    * end-of-life key handling
<!-- chapter: regulatory-and-certification, duration: 3h -->
* Regulatory and certification
    * `EU Cyber Resilience Act` (`CRA`)
    * `UK PSTI` and similar consumer-`IoT` laws
    * `IEC 62443` for industrial systems
    * `UNECE WP.29` for automotive
    * `FDA` guidance for medical devices
    * `Common Criteria` and `EAL` levels
    * how to map a product to the relevant standard
<!-- chapter: incident-response-for-deployed-fleets, duration: 2h -->
* Incident response for deployed fleets
    * detecting compromise in the field
    * containment options for unpatchable devices
    * customer comms after a fleet vulnerability
    * coordinated disclosure with security researchers
    * the long-tail problem of legacy fleets
    * cross-reference to the Security Incident Response course
<!-- chapter: workshop-and-wrap-up, duration: 3h -->
* Workshop and wrap up
    * design walkthrough of a secure connected product
    * tabletop incident on a sample fleet vulnerability
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
