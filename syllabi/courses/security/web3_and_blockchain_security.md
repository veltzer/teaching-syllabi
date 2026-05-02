---
tags:
  - concepts:security
  - concepts:blockchain
  - concepts:smart-contracts
  - concepts:cryptography
  - concepts:ethereum
  - concepts:web3
level: advanced
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:blockchain-developers
  - audiences:senior-developers
  - audiences:penetration-testers
---
<!-- course: web3_and_blockchain_security -->
# `Web3` and Blockchain Security

## Description
Smart contracts deploy code that holds money to a public, immutable, adversarial environment, and most of them
do it badly. The history of `Web3` is mostly the history of avoidable bugs causing nine-figure losses. The
security skills required to ship safe smart contracts and to audit other people's smart contracts are
specialized, learnable, and in short supply.

This five day course covers `Web3` security as a focused engineering discipline. It covers the threat model
unique to smart contracts, the major vulnerability classes (reentrancy, `oracle` manipulation, access control,
arithmetic, signature replay, `MEV`), the auditing process end to end, the tooling (Slither, `Mythril`,
`Echidna`, Foundry invariants, Halmos), DeFi-specific risks, bridge and `L2` risks, the post-deployment
operational story (monitoring, incident response, upgrades), and the bug-bounty ecosystem. Examples are drawn
from public audit reports, post-mortem analyses of major exploits, and the audit content from `Trail of Bits`,
`OpenZeppelin`, `ConsenSys Diligence` and Code4rena. The course is `Ethereum`-centric but covers
non-`EVM` systems where it matters.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers expanding into `Web3` and smart contract security
* blockchain developers wanting to ship safer contracts
* auditors building or refining their methodology
* engineers preparing for `Code4rena` or similar audit contests

## Prerequisites
* working knowledge of Solidity or another smart-contract language
* basic familiarity with `Ethereum` and the `EVM`
* basic understanding of cryptographic primitives (hashes, signatures)
* exposure to at least one general-purpose security course is helpful

## Objectives
* describe the smart-contract threat model precisely
* recognize and exploit the major vulnerability classes
* run a complete smart-contract audit from kickoff to report
* operate the major `Web3` security tools effectively
* design contracts that are resistant to common attacks
* respond to a smart-contract incident
* contribute to the bug-bounty ecosystem responsibly

## Outline
<!-- chapter: the-smart-contract-threat-model, duration: 2h -->
* The smart contract threat model
    * what makes smart contracts different from web apps
    * the public, adversarial, immutable environment
    * the financial-loss-on-bug economics
    * the attack surface: contracts, oracles, frontends, bridges, governance
    * the actor model: users, attackers, miners/validators, governance
    * what cryptographic primitives do and do not protect
<!-- chapter: ethereum-and-evm-fundamentals-for-security, duration: 3h -->
* `Ethereum` and `EVM` fundamentals for security
    * the `EVM` execution model
    * gas, gas refunds, gas griefing
    * storage, memory, calldata
    * `delegatecall` and proxy patterns
    * the call stack and reentrancy mechanics
    * `tx.origin` vs `msg.sender`
    * block timestamps and validators
<!-- chapter: reentrancy-the-classic-bug, duration: 3h -->
* Reentrancy: the classic bug
    * the `DAO` exploit revisited
    * single-function reentrancy
    * cross-function reentrancy
    * cross-contract reentrancy
    * read-only reentrancy
    * `ERC-777` callback hooks and the new reentrancy
    * the checks-effects-interactions pattern
    * `ReentrancyGuard` and its limits
<!-- chapter: access-control-and-authorization, duration: 3h -->
* Access control and authorization
    * function-level access control
    * `onlyOwner`, role-based access (`OpenZeppelin`)
    * the time-locked admin pattern
    * `delegatecall` and the storage-collision attack
    * forgotten `initialize()` and unguarded upgrade calls
    * front-running governance proposals
    * the rugpull architecture
<!-- chapter: arithmetic-and-rounding-bugs, duration: 2h -->
* Arithmetic and rounding bugs
    * pre-`0.8.0` overflow and underflow
    * `SafeMath` and built-in checked arithmetic
    * rounding direction and the dust attack
    * fixed-point math and precision loss
    * the integer-division-then-multiply trap
    * unit confusion: wei vs ether vs tokens
<!-- chapter: oracle-manipulation, duration: 3h -->
* Oracle manipulation
    * the `oracle` problem
    * spot-price vs `TWAP` oracles
    * `Uniswap` V2/V3 as an `oracle`, safely and unsafely
    * `Chainlink` push oracles
    * flash-loan-driven `oracle` manipulation
    * cross-chain `oracle` risks
    * the `oracle` attack pattern in real exploits
<!-- chapter: signature-and-cryptographic-bugs, duration: 2h -->
* Signature and cryptographic bugs
    * `ecrecover` and signature malleability
    * `EIP-712` typed-data signatures
    * replay across chains and replay across contracts
    * `permit` and `permit2` patterns
    * signature deadline mistakes
    * signature aggregation pitfalls
<!-- chapter: mev-and-frontrunning, duration: 3h -->
* `MEV` and frontrunning
    * the `MEV` ecosystem
    * sandwich attacks
    * frontrun and backrun patterns
    * private mempools and `Flashbots`
    * commit-reveal schemes
    * `MEV`-aware contract design
    * `MEV` as a feature vs `MEV` as a bug
<!-- chapter: defi-specific-risks, duration: 3h -->
* `DeFi`-specific risks
    * `AMM` invariants and how they break
    * lending-protocol risks: bad debt, liquidation games
    * flash-loan attack patterns
    * yield-aggregator and `vault` accounting bugs
    * stablecoin de-pegs and contagion
    * governance-token attacks
    * cross-reference to historical exploits
<!-- chapter: bridges-and-cross-chain-risks, duration: 2h -->
* Bridges and cross-chain risks
    * the bridge as the highest-value target
    * lock-and-mint vs liquidity-pool bridges
    * the `Wormhole`, `Ronin`, Nomad exploits
    * cross-chain message verification
    * bridge custody patterns
    * the case for and against bridges
<!-- chapter: l2-and-rollup-security, duration: 2h -->
* `L2` and rollup security
    * optimistic vs `ZK` rollups for security
    * fraud proofs and the challenge window
    * sequencer trust assumptions
    * `L1`-`L2` message-passing risks
    * upgrade authority on `L2`
    * `L2`-specific attack patterns
<!-- chapter: tooling-static-and-dynamic-analysis, duration: 3h -->
* Tooling: static and dynamic analysis
    * `Slither` for static analysis
    * `Mythril` and `MythX`
    * `Foundry` and invariant testing
    * `Echidna` for property-based fuzzing
    * `Halmos` for symbolic execution
    * `Manticore` for symbolic execution
    * integrating tools into `CI`
<!-- chapter: the-audit-process, duration: 3h -->
* The audit process
    * scoping the audit
    * code review methodology for contracts
    * threat modeling per protocol
    * the severity rubric
    * writing audit findings
    * the audit report deliverable
    * post-audit fixes and re-review
<!-- chapter: secure-design-patterns, duration: 2h -->
* Secure `design patterns`
    * pull-over-push payment patterns
    * pause and circuit-breaker patterns
    * upgradeability patterns: `UUPS`, transparent proxy, beacon
    * timelocks on critical operations
    * minimal-trust admin keys
    * the multi-sig and `MPC` admin pattern
<!-- chapter: monitoring-and-incident-response, duration: 2h -->
* Monitoring and incident response
    * on-chain monitoring: `Tenderly`, Forta, `OpenZeppelin Defender`
    * incident-time pause and rescue patterns
    * working with white-hat hackers
    * cross-reference to the Security Incident Response course
    * post-incident comms and `MEV`-driven recovery
<!-- chapter: bug-bounty-and-audit-contests, duration: 1h -->
* Bug bounty and audit contests
    * `Immunefi`, Code4rena, Sherlock, `Cantina`
    * scope and rules of engagement
    * responsible disclosure on-chain
    * career path: solo auditor, contest judge, audit firm
    * keeping current with the threat landscape
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * audit walkthrough of a vulnerable sample contract
    * group review of a public audit report
    * recommended reading: `Mastering Ethereum`, public `Trail of Bits` reports

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
