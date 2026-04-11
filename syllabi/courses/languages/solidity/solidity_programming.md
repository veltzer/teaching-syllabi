---
tags:
  - languages:solidity
  - concepts:blockchain
  - concepts:smart-contracts
  - concepts:ethereum
  - concepts:web3
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:blockchain-developers
---
<!-- course: solidity_programming -->
# `Solidity` Programming

## Description
`Solidity` is the primary smart contract programming language for the `Ethereum` blockchain and EVM-compatible networks.
It enables developers to write self-executing contracts that manage digital assets, implement decentralised protocols, and encode business logic directly on-chain.
Writing secure `Solidity` requires deep understanding of the EVM execution model, gas economics, and common vulnerability patterns such as reentrancy and integer overflow.
This course takes developers from `Solidity` syntax through token standards, security patterns, and deployment workflows with `Hardhat`.

## Duration
24 hours / 3 days

## Intended Audience
* Backend developers entering the blockchain and `Web3` space
* Smart contract developers seeking a structured foundation
* Architects designing decentralised applications (`dApps`)

## Prerequisites
* Proficiency in at least one programming language such as `JavaScript`, `Python`, or `Java`
* Basic understanding of cryptography and hashing concepts
* Familiarity with how blockchains work at a conceptual level

## Objectives
* Write and deploy `Solidity` smart contracts to EVM-compatible networks
* Understand the EVM execution model and gas mechanics
* Implement the most common token standards — ERC-20, ERC-721, ERC-1155
* Apply security patterns to prevent reentrancy, overflow, and access-control vulnerabilities
* Test contracts with `Hardhat` and `ethers.js`
* Use `OpenZeppelin` libraries for production-grade contract development

## Outline
<!-- chapter: introduction-to-blockchain-and-ethereum, duration: 2h -->
* Introduction to Blockchain and `Ethereum`
    * How blockchains work — consensus, blocks, transactions
    * The `Ethereum` Virtual Machine (EVM)
    * Accounts — EOAs vs contract accounts
    * Gas and transaction fees
    * `Ethereum` development networks — mainnet, testnets, local

<!-- chapter: solidity-basics-and-syntax, duration: 2h -->
* `Solidity` Basics and Syntax
    * Contract structure and layout
    * Pragma and license identifiers
    * `SPDX` license comments
    * Compilation and deployment overview
    * ABI and bytecode

<!-- chapter: data-types-and-state-variables, duration: 2h -->
* Data Types and State Variables
    * Value types — `uint`, `int`, `bool`, `address`, `bytes`
    * Reference types — `string`, `bytes`, `array`, `struct`, `mapping`
    * State variables and storage layout
    * Memory vs storage vs calldata
    * Constants and immutables

<!-- chapter: functions-and-modifiers, duration: 3h -->
* Functions and Modifiers
    * Function visibility — `public`, `private`, `internal`, `external`
    * State mutability — `pure`, `view`, `payable`
    * Function modifiers
    * Constructor functions
    * Fallback and receive functions
    * Function overloading

<!-- chapter: events-and-error-handling, duration: 2h -->
* Events and Error Handling
    * Emitting and indexing events
    * Using `require`, `revert`, and `assert`
    * Custom errors
    * `try/catch` for external call failures
    * Error propagation patterns

<!-- chapter: inheritance-and-interfaces, duration: 2h -->
* Inheritance and Interfaces
    * Single and multiple inheritance
    * `virtual` and `override`
    * Abstract contracts
    * Interfaces
    * Libraries

<!-- chapter: contract-security-patterns, duration: 3h -->
* Contract Security Patterns
    * Reentrancy vulnerabilities and the checks-effects-interactions pattern
    * Integer overflow and `SafeMath` (pre-0.8 vs 0.8+)
    * Access control with `Ownable` and roles
    * Front-running and commit-reveal schemes
    * Denial of service patterns
    * Using `OpenZeppelin` security primitives

<!-- chapter: tokens-and-erc-standards, duration: 2h -->
* Tokens and ERC Standards
    * ERC-20 fungible tokens
    * ERC-721 non-fungible tokens (NFTs)
    * ERC-1155 multi-token standard
    * Implementing tokens with `OpenZeppelin`
    * Token extensions — burnable, pausable, mintable

<!-- chapter: testing-with-hardhat, duration: 2h -->
* Testing with `Hardhat`
    * `Hardhat` project setup
    * Writing tests with `Mocha` and `Chai`
    * Using `ethers.js` in tests
    * Forking mainnet for integration tests
    * Gas reporting

<!-- chapter: deploying-smart-contracts, duration: 2h -->
* Deploying Smart Contracts
    * Deployment scripts with `Hardhat`
    * Verifying contracts on `Etherscan`
    * Upgradeable contracts with proxies
    * Deployment to testnets and mainnet

<!-- chapter: defi-protocol-patterns, duration: 2h -->
* DeFi Protocol Patterns
    * Automated Market Makers (AMM) concepts
    * Lending and borrowing patterns
    * Flash loans
    * Oracles and `Chainlink`
    * Governance contracts

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
