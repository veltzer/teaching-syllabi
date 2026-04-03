---
tags:
  - languages:typescript
  - languages:javascript
  - concepts:programming
level: advanced
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: advanced_typescript -->
# Advanced `TypeScript`

## Description
This course covers advanced `TypeScript` features for experienced developers who want to master the type system and apply sophisticated patterns. Topics include conditional types, mapped types, template literal types, decorators, type guards, utility types, declaration files, and project architecture for large-scale `TypeScript` applications.

## Duration
16 hours / 2 days

## Intended Audience
* Experienced `TypeScript` developers looking to master the advanced type system
* Frontend and backend developers building large-scale typed applications
* Library authors who need to create expressive `type-definitions`

## Prerequisites
* `Solid` experience with `TypeScript` programming
* Familiarity with generics, interfaces, and basic type patterns
* Understanding of `JavaScript` module systems

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Master conditional types, mapped types, and template literal types
* Create precise and expressive `type-definitions` for complex APIs
* Apply advanced type guards and narrowing techniques
* Build and consume declaration files for third-party code
* Architect large `TypeScript` projects for maintainability and type safety

## Outline
<!-- chapter: advanced-type-system-foundations, duration: 1h -->
* Advanced Type System Foundations
    * Review of union, intersection, and literal types
    * Type inference and type widening/narrowing
    * The infer keyword
    * Distributive conditional types
    * Recursive type aliases
    * Variance and covariance in `TypeScript`
<!-- chapter: conditional-types, duration: 2h -->
* Conditional Types
    * Basic conditional type syntax
    * Inferring types within conditional types
    * Distributive behavior over unions
    * Nested conditional types
    * Practical patterns with conditional types
    * Building type-level logic
<!-- chapter: mapped-types, duration: 2h -->
* Mapped Types
    * Basic mapped type syntax
    * Key remapping with as
    * Filtering keys with conditional types
    * Homomorphic mapped types
    * Combining mapped and conditional types
    * Creating custom type transformations
<!-- chapter: template-literal-types, duration: 2h -->
* Template Literal Types
    * Template literal type syntax
    * String manipulation at the type level
    * Uppercase, Lowercase, Capitalize, Uncapitalize
    * Parsing string patterns with template literals
    * Building typed routing and event systems
    * Combining template literals with mapped types
<!-- chapter: utility-types-in-depth, duration: 1h -->
* Utility Types in Depth
    * Standard utility types (Partial, Required, Pick, Omit, Record, Exclude, Extract)
    * ReturnType, Parameters, ConstructorParameters
    * Awaited and promise-related types
    * Building custom utility types
    * Composing utility types for complex transformations
<!-- chapter: type-guards-and-narrowing, duration: 2h -->
* Type Guards and Narrowing
    * User-defined type guards with type predicates
    * Discriminated unions and exhaustive checks
    * Assertion functions
    * The satisfies operator
    * const assertions
    * Narrowing with in, instanceof, and `typeof`
    * Control flow analysis
<!-- chapter: decorators, duration: 2h -->
* Decorators
    * The TC39 decorators proposal
    * Class decorators
    * Method and accessor decorators
    * Field decorators
    * Decorator metadata
    * Practical decorator patterns (logging, validation, memoization)
    * Legacy vs stage 3 decorators
<!-- chapter: declaration-files, duration: 2h -->
* Declaration Files
    * Writing .d.ts files
    * Ambient declarations and declare keyword
    * Module augmentation and declaration merging
    * Global augmentation
    * Working with DefinitelyTyped and @types packages
    * Typing untyped `JavaScript` libraries
    * Triple-slash directives
<!-- chapter: project-architecture, duration: 2h -->
* Project Architecture
    * Monorepo strategies with `TypeScript` project references
    * Path aliases and module resolution
    * Strict compiler options and their impact
    * Incremental compilation and build performance
    * Barrel files and module organization
    * Shared types across packages
    * `API` `design patterns` for type-safe libraries

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
