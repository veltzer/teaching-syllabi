---
tags:
  - networking:security
  - concepts:pki
  - protocols:tls
  - concepts:cryptography
  - concepts:certificates
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sysadmins
  - audiences:security-engineers
---
<!-- course: pki_and_certificates -->
# `PKI` and Certificates

## Description
Public Key Infrastructure (`PKI`) underpins the security of virtually every encrypted communication on the internet, from `HTTPS` websites to mutual `TLS` in `microservices` and `VPN` authentication. Despite its foundational role, `PKI` is frequently misunderstood, leading to misconfigured certificates, broken trust chains, and serious security vulnerabilities. This course provides a rigorous, practical understanding of `PKI` from first principles — covering asymmetric cryptography, `X.509` certificate structure, certificate authority hierarchies, the `TLS` handshake, and the full certificate lifecycle. Participants will gain hands-on experience with `OpenSSL`, `Let's Encrypt`/`ACME`, and internal `CA` solutions including `CFSSL` and `HashiCorp Vault`, enabling them to design and operate `PKI` infrastructure confidently.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who need to understand `TLS` configuration, certificate validation, and mutual `TLS` for their applications and services.
* `DevOps` engineers and system administrators responsible for provisioning, renewing, and rotating certificates across infrastructure.
* Security engineers performing `PKI` design, certificate policy authoring, and audit of `TLS` configurations.

## Prerequisites
* Understanding of `TCP/IP` networking and `HTTP`/`HTTPS` basics.
* `Linux` command-line proficiency, including working with files and running administrative commands.
* Basic familiarity with concepts like encryption and hashing is helpful but not required — the course covers cryptographic fundamentals.

## Required Knowledge
* `Linux` command-line proficiency
* `Networking` fundamentals (`TCP/IP`, `HTTP`)

## Objectives
* Explain the mathematical foundations of asymmetric cryptography relevant to `PKI`
* Describe the structure and trust model of a Public Key Infrastructure
* Read and interpret `X.509` certificates, extensions, and certificate chains
* Understand the roles and responsibilities of root, intermediate, and issuing CAs
* Trace the `TLS` handshake step by step and explain the role of certificates within it
* Configure `TLS` securely: cipher suites, protocol versions, certificate pinning
* Manage the certificate lifecycle: issuance, renewal, revocation, and rotation
* Automate certificate issuance with `Let's Encrypt` and the `ACME` protocol
* Build and operate an internal `CA` using `CFSSL` and `HashiCorp Vault PKI`

## Outline
<!-- chapter: cryptography-fundamentals-for-pki, duration: 2h -->
* Cryptography Fundamentals for `PKI`
    * Symmetric vs asymmetric encryption: key concepts and trade-offs
    * `RSA`: key generation, encryption, and digital signatures
    * Elliptic Curve Cryptography (`ECC`): `ECDSA` and `ECDH`
    * Hash functions: `SHA-256`, `SHA-384`, and collision resistance
    * Digital signatures: signing and verification with private/public key pairs
    * Message Authentication Codes (`HMAC`) and their role
    * Key Derivation Functions (`HKDF`, `PBKDF2`)
    * Random number generation and the importance of entropy
<!-- chapter: pki-architecture, duration: 2h -->
* Public Key Infrastructure Architecture
    * The problem `PKI` solves: binding identity to public keys
    * Certificate Authorities: root CAs, intermediate CAs, and issuing CAs
    * `CA` hierarchy design: two-tier and three-tier models
    * Offline root `CA` best practices for air-gapped security
    * Trust stores: browser, OS, and `JVM` trust anchors
    * Certificate policies and Certificate Practice Statements (CPS)
    * Cross-certification and bridge CAs
    * Public `PKI` vs private `PKI`: `when` to use each
<!-- chapter: x509-certificates-deep-dive, duration: 2h -->
* `X.509` Certificates Deep Dive
    * `ASN.1` encoding and `DER`/`PEM` formats
    * Certificate fields: version, serial number, validity period, subject, issuer
    * Subject Alternative Names (`SAN`) and wildcard certificates
    * Key Usage and Extended Key Usage extensions
    * Basic Constraints and the `CA` flag
    * Authority Key Identifier and Subject Key Identifier
    * Certificate Policies and Policy Constraints extensions
    * Parsing certificates with `OpenSSL` and online tools
    * Common certificate mistakes and how to spot them
<!-- chapter: certificate-authorities-and-trust-chains, duration: 2h -->
* Certificate Authorities and Trust Chains
    * How browsers and operating systems build and validate trust chains
    * Intermediate `CA` certificates and chain ordering
    * Creating a root `CA` and intermediate `CA` with `OpenSSL`
    * Signing end-entity certificates with a `CA`
    * Certificate Revocation Lists (`CRL`): structure and distribution
    * Online Certificate Status Protocol (`OCSP`) and `OCSP` stapling
    * Certificate Transparency (`CT`) logs and their security role
    * Public `CA` ecosystem: DigiCert, Sectigo, `Let's Encrypt`, and browser trust requirements
<!-- chapter: tls-handshake-and-configuration, duration: 3h -->
* `TLS` Handshake and Configuration
    * `TLS` 1.2 handshake: ClientHello, ServerHello, certificate exchange, key exchange
    * `TLS` 1.3 handshake: improvements, 0-RTT, and reduced round trips
    * Cipher suites: AEAD ciphers, forward secrecy, and deprecated algorithms
    * Certificate validation during the handshake: chain building and revocation checking
    * Mutual `TLS` (mTLS): client certificate authentication
    * Configuring `TLS` in `Nginx`, `Apache`, and application servers
    * `TLS` configuration best practices and the Mozilla `SSL` Configuration Generator
    * Testing `TLS` configuration with `testssl.sh` and Qualys `SSL` Labs
    * Common `TLS` vulnerabilities: `BEAST`, `POODLE`, `Heartbleed`, and `ROBOT`
<!-- chapter: certificate-lifecycle-management, duration: 2h -->
* Certificate Lifecycle Management
    * Certificate validity periods and best practices
    * Automated certificate discovery and inventory
    * Certificate expiry monitoring and alerting
    * Renewal workflows: pre-expiry, automated, and emergency renewal
    * Certificate revocation and key compromise response procedures
    * Certificate rotation for zero-downtime deployments
    * Managing certificates in `Kubernetes` with `cert-manager`
    * Secrets management integration: storing certificates in `Vault` and `AWS Secrets Manager`
<!-- chapter: lets-encrypt-and-acme, duration: 1h -->
* `Let's Encrypt` and the `ACME` Protocol
    * `Let's Encrypt` history and mission: free, automated, and open
    * `ACME` protocol (`RFC 8555`): account creation, order, challenge, and finalization
    * `HTTP-01`, `DNS-01`, and `TLS-ALPN-01` challenge types
    * Using `Certbot` for `ACME` certificate issuance and renewal
    * `ACME` client libraries: `acme.sh`, `Lego`, `Caddy` built-in
    * `DNS-01` challenge for wildcard certificates and internal services
    * `ACME` in enterprise environments with `step-ca` and private `ACME` servers
<!-- chapter: internal-pki-with-cfssl-and-vault, duration: 2h -->
* Internal `PKI` with `CFSSL` and `Vault`
    * `When` to run an internal `CA`: air-gapped systems, mTLS meshes, short-lived certificates
    * `CFSSL` architecture: `CA` server, `API`, and `CLI`
    * Setting up a `CFSSL`-based two-tier `CA` hierarchy
    * Issuing and signing certificates with `CFSSL` `API`
    * `HashiCorp Vault PKI` secrets engine overview
    * Configuring root and intermediate CAs in `Vault`
    * Issuing short-lived certificates with `Vault` for service-to-service mTLS
    * Integrating `Vault PKI` with `cert-manager` in `Kubernetes`
    * Certificate lifecycle automation with short TTLs and high-frequency renewal

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
