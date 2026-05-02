---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:operations
  - concepts:best-practices
level: advanced
category: embedded
duration_hours: 24
audience:
  - audiences:embedded-developers
  - audiences:firmware-developers
  - audiences:embedded-engineers
  - audiences:security-engineers
---
<!-- course: firmware_update_and_ota -->
# Firmware Update and `OTA`

## Description
The catalog has multiple embedded courses covering bare-metal programming, embedded `Linux`, embedded
security, and protocol stacks. None of them covers the discipline of updating the firmware on a
device after it has shipped — and this is the single most consequential operational decision a
hardware product makes. A device that cannot be updated safely is a device whose security model is
frozen at ship date. A device with a buggy update mechanism is one bad release away from a brick-pile
of physical units that need a truck roll.

This three day course covers firmware update and over-the-air (`OTA`) delivery as practiced on real
products. It covers the boot architecture choices that `make` safe update possible (`A/B` partitions,
recovery slot, fail-safe rollback, the `bootloader` contract), the cryptographic story (signing,
verification, anti-rollback, the secure-boot chain), the `delta`-update story for bandwidth-constrained
devices, the `OTA` delivery layer (`MQTT`, `HTTPS`, `LwM2M`), the campaign-management problem (staged
rollout, fleet segmentation, abort criteria), the on-device update agent, the failure modes
(interrupted update, power loss mid-flash, corrupted image, divergent fleet), and the regulatory
requirements (`FDA`, automotive `UNECE R155/R156`, `CE RED`). Examples and labs use `Mender`,
`SWUpdate`, RAUC, fwup, `esp-idf` OTA, and `MCUboot`. Participants leave able to design and
operate an update system that does not brick the fleet.

## Duration
24 hours / 3 days

## Intended Audience
* embedded developers shipping connected products
* firmware engineers designing the update path
* `IoT` engineers operating a fleet
* security engineers reviewing update mechanisms

## Prerequisites
* working experience with at least one embedded platform
* familiarity with `bootloaders` at a conceptual level
* exposure to the `Embedded Systems Security` course is helpful
* basic cryptography knowledge

## Objectives
* design a boot architecture that supports safe update
* implement signed firmware with anti-rollback
* deploy a `delta`-update path for bandwidth-constrained fleets
* operate a staged `OTA` campaign
* recognize the failure modes that brick devices
* meet the regulatory requirements for the relevant industry
* select among `Mender`, SWUpdate, RAUC, `fwup`, custom

## Outline
<!-- chapter: why-firmware-update-is-the-foundation, duration: 1h -->
* Why firmware update is the foundation
    * the security model is frozen at ship date without update
    * the cost of a truck roll
    * the regulatory pressure to ship updates
    * the "we cannot patch the `CVE` because we have no `OTA`" reality
    * cross-reference to the Embedded Systems Security course
<!-- chapter: boot-architectures-for-safe-update, duration: 3h -->
* Boot architectures for safe update
    * `A/B` partitions
    * recovery slot
    * fail-safe rollback
    * the bootloader as the trust anchor
    * `MCUboot` as a canonical example
    * the "we updated and the device booted into nothing" failure
<!-- chapter: cryptographic-foundations, duration: 3h -->
* Cryptographic foundations
    * image signing
    * the verification chain
    * key management for fleet
    * anti-rollback counters
    * the secure-boot chain
    * cross-reference to the Cryptography Fundamentals course
<!-- chapter: image-formats-and-packaging, duration: 1h -->
* Image formats and packaging
    * the manifest as the truth
    * `SWU`, `mender-artifact`, RAUC bundles, `swupdate`
    * the multi-component update
    * the "we updated firmware but not the calibration data" failure
<!-- chapter: delta-updates, duration: 2h -->
* Delta updates
    * the bandwidth case
    * `bsdiff`, xdelta, `courgette`-style approaches
    * the patch-from-which-version question
    * the "`delta` only works from the last version" trap
    * fall-back to full image
<!-- chapter: ota-delivery-protocols, duration: 2h -->
* `OTA` delivery protocols
    * `HTTPS` pull
    * `MQTT` push
    * `LwM2M`
    * `CoAP` for tiny devices
    * the resumable-download requirement
    * cross-reference to the `MQTT` and `IoT` Protocols course
<!-- chapter: the-on-device-update-agent, duration: 2h -->
* The on-device update agent
    * download, verify, apply, commit
    * the watchdog interaction
    * the power-loss-anywhere requirement
    * the storage-wear consideration
    * the "the agent itself had a bug" failure
<!-- chapter: open-source-update-systems, duration: 2h -->
* Open-source update systems
    * `Mender`
    * `SWUpdate`
    * `RAUC`
    * `fwup`
    * `esp-idf` OTA for `ESP32`
    * picking the system
<!-- chapter: campaign-management, duration: 2h -->
* Campaign management
    * staged rollout
    * fleet segmentation by hardware revision, region, customer
    * the abort criterion
    * the "we shipped to 100 percent and bricked everything" failure
    * the rollout-pause control
<!-- chapter: failure-modes, duration: 2h -->
* Failure modes
    * interrupted download
    * power loss mid-flash
    * corrupted image that passes verification
    * the boot loop after update
    * fleet divergence after partial rollout
    * the "we cannot tell what version is in the field" reality
<!-- chapter: observability-of-the-fleet, duration: 1h -->
* Observability of the fleet
    * the version inventory
    * the update-success metric
    * the device-health metric post-update
    * the silent-rollback signal
    * the "we shipped and never knew if it worked" failure
<!-- chapter: secure-update-in-practice, duration: 2h -->
* Secure update in practice
    * the threat model for update
    * the supply-chain risk for the build pipeline
    * cross-reference to the Supply Chain Security course
    * the `SBOM` and the update story
    * the "the signing key was on the build server" disaster
<!-- chapter: regulatory-requirements, duration: 1h -->
* Regulatory requirements
    * automotive `UNECE R155/R156`
    * medical device update under `FDA` cybersecurity guidance
    * `CE RED` (`EU 2014/53`) cybersecurity essential requirements
    * the "the regulator asked for an `SBOM`" reality
    * the audit trail for an update

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
