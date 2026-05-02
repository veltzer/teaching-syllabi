---
tags:
  - languages:groovy
  - languages:java
  - concepts:programming
  - concepts:scripting
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: groovy_programming -->
# Groovy Programming

## Description
Groovy is a powerful, optionally typed, dynamic language for the `Java` platform. It integrates
seamlessly with existing `Java` code and libraries while offering concise syntax, closures,
and metaprogramming capabilities that `boost` developer productivity. Groovy is widely used in
build automation through `Gradle`, `CI/CD` pipelines with `Jenkins`, and testing with the Spock
framework. This course covers Groovy from language fundamentals through advanced topics
such as metaprogramming, DSL creation, and practical usage in `Gradle` and `Jenkins`.
The course includes hands on exercises.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers looking to increase productivity with a more expressive `JVM` language.
* `DevOps` engineers working with `Gradle` or `Jenkins` who want a deeper understanding of Groovy.
* Developers interested in building domain-specific languages.

## Prerequisites
* `Solid` programming experience in `Java` or another object-oriented language.
* Familiarity with the `JVM` ecosystem.
* Basic understanding of build tools and `CI/CD` concepts is helpful.

## Objectives
* Write concise and idiomatic Groovy code
* Understand the differences and interplay between Groovy and `Java`
* Use closures, collections, and dynamic features effectively
* Apply metaprogramming and AST transformations
* Write `Gradle` build scripts and `Jenkins` pipelines in Groovy
* Build tests with the Spock framework
* Create domain-specific languages

## Outline
<!-- chapter: groovy-basics, duration: 2h -->
* Groovy Basics
    * Introduction to Groovy and its place in the `JVM` ecosystem
    * Installing Groovy and development environment setup
    * Groovy vs `Java`: similarities and differences
    * Dynamic and static typing
    * GStrings and string interpolation
    * Groovy truth and coercion
    * Running Groovy scripts and classes
<!-- chapter: closures, duration: 1h -->
* Closures
    * Closure syntax and semantics
    * Parameters, delegation, and owner
    * Closures as method parameters
    * Currying and composition
    * Closure scope and variable capture
<!-- chapter: operators-and-collections, duration: 1h -->
* Operators and Collections
    * Operator overloading
    * The spaceship operator and comparisons
    * Spread operator and safe navigation operator
    * Lists, maps, and ranges
    * Collection methods (each, collect, find, findAll, inject)
    * Sorting and grouping
<!-- chapter: regular-expressions, duration: 1h -->
* Regular Expressions
    * Pattern and Matcher in Groovy
    * The `=~` and `==~` operators
    * String matching and replacement
    * Practical regex patterns
<!-- chapter: file-i-o-and-data-processing, duration: 2h -->
* `File` `I/O` and Data Processing
    * Reading and writing files
    * Working with directories
    * Processing `CSV` and text data
    * `XML` processing with XmlParser and XmlSlurper
    * MarkupBuilder for `XML` generation
    * `JSON` parsing and generation with JsonSlurper and JsonBuilder
<!-- chapter: metaprogramming, duration: 2h -->
* Metaprogramming
    * The Meta-Object Protocol (MOP)
    * methodMissing and propertyMissing
    * Categories and mixins
    * ExpandoMetaClass
    * AST transformations (@ToString, @EqualsAndHashCode, @Immutable, etc.)
    * Writing custom AST transformations
<!-- chapter: dependency-management-with-grape, duration: 1h -->
* Dependency Management with Grape
    * The @Grab annotation
    * Resolving dependencies at runtime
    * Repository configuration
    * Using external libraries in scripts
<!-- chapter: groovy-in-gradle, duration: 1h -->
* Groovy in `Gradle`
    * `Gradle` build script fundamentals
    * Tasks, dependencies, and plugins
    * Custom task creation
    * Multi-project builds
    * Leveraging Groovy features in build scripts
<!-- chapter: groovy-in-jenkins-pipelines, duration: 1h -->
* Groovy in `Jenkins` Pipelines
    * Scripted vs Declarative pipelines
    * Writing pipeline stages in Groovy
    * Shared libraries
    * Pipeline best practices
    * Common patterns and pitfalls
<!-- chapter: testing-with-spock, duration: 2h -->
* Testing with Spock
    * Spock framework overview
    * Specification structure (given/when/then)
    * Data-driven testing with where blocks
    * Mocking and stubbing
    * Interaction-based testing
    * Integration testing
<!-- chapter: domain-specific-languages, duration: 1h -->
* Domain-Specific Languages
    * What is a DSL and why build one
    * Builder pattern in Groovy
    * Using closures and delegation for DSLs
    * Command chains
    * Designing a readable DSL
<!-- chapter: integration-with-the-java-ecosystem, duration: 1h -->
* Integration with the `Java` Ecosystem
    * Calling `Java` from Groovy and vice versa
    * Using `Java` libraries in Groovy
    * Joint compilation
    * Deploying Groovy applications

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
