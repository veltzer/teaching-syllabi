---
tags:
  - languages:java
  - practices:testing
  - practices:tdd
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
# `Java` `TDD`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course covers Test Driven Development (`TDD`) in `Java`, combining testing theory with hands-on practice using `JUnit` and related tools. Students will learn agile and `XP` methodologies, unit testing techniques, mock objects, code refactoring for testability, and tools such as `DbUnit`, `JMockit`, and `PMD`.

## Duration
24 hours / 3 days

## Intended Audience
* Java developers
* software engineers working with JVM-based technologies

## Prerequisites
* Development in `Java` for at least one year

## Objectives
People completing this course will have strong
understanding of what `TDD` and Agile programming is all about
with the knowledge to implement these development methodologies
in their work environments. They will acquire the technical
skills to use the tools that `Java` provides for these methodologies:
`JUnit`, `Eclipse` facilities, Ant support for testing and many other
third party tools that will be discussed in the development section.

## Outline
* Theory
    * Software Testing Overview
        * Testing Overview
        * Testing Fundamentals
        * Types of Tests
        * Test Techniques
    * Introduction to Unit Testing
        * Unit Testing Overview
        * Unit Testing - why not?
        * Unit Testing - why Yes?
        * Beyond pure unit testing
        * Unit testing techniques
    * Software Development Methodologies compared
        * Traditional methods:
            * Waterfall model
            * V model
            * Prototype model
            * Spiral model
        * Agile methods:
            * XP - eXtreme Programming
            * Test Driven Development
    * Introduction to Agile development
        * Agile Overview
        * Agile Manifesto and Principles
        * Agile Modeling Practices
        * Agile Testing
        * User Stories
        * Automated Testing in Agile
        * Glossary of Agile Terms
    * Extreme Programming
        * Traditional life cycle vs. XP
        * XP motto: "embrace change"
        * XP values
        * XP practices
        * Pair programming
        * More XP practices
        * An XP development road map
    * Test Driven Development
        * Traditional Software Testing
        * Functional/Regression/Integration/Unit testing
        * The "Test First" approach
        * Automated Testing
    * Test Doubles
        * What is a "Test Double"?
        * Creating and using Mock objects
* Practical
    * `JUnit` (big chapter, 2 days with exercises)
        * Creating unit tests with `JUnit`.
        * Exercise: Getting to know JUNIT.
            * Writing simple tests and running them.
            the participants will write their first `JUnit` tests. They will get
            to know the eclipse facilities for `JUnit`.
        * Advanced `JUnit` topics:
            * Test hierarchies
            * common fixtures
            * best practices
            * common pitfalls
        * Exercise: Writing good tests.
            * Writing good tests for a lecturer provided `Java` module.
            Objective: learn how to write the tests *CORRECTLY* so that they will cover
            as much of the functionality as possible.
        * Using `JUnit` with Ant
        * Exercise: Running ant for automated unit tests with reporting
            Objective: learn how to write your tests in such a way as to be easily runnable
            from ant. Learn how to produce test run results from ant in several formats.
    * Big exercise: learning to refactor code for testing
        The lecturer will provide a "badly" written code which is hard to test.
        The students will need to refactor the code, while preserving it's
        functionality, in order to make it "test ready" and write tests for it.
        Then the students will write tests for it covering as much of the functionality
        as possible.
        The exercise will be followed by a discussion of the various strategies and `Java`
        features that can be used to achieve such refactoring (extracting interfaces,
        creating parent classes, inner classes, anonymous classes, etc) with their
        relative advantages/disadvantages.
    * Technologies
        * JUnitEE
            * Configuring a JEE project with JUnitEE
            * Doing basic tests
            * Doing smart tests
            * JUnitEE TestRunner
            * JUnitEE Ant tasks
            * Security issues
        * DbUnit
            * Best practices when testing with a database
            * Cleaning a database
            * Importing/exporting a dataset
        * JMockit
            * The theory behind JMockit
            * JMockit by example
            * Exercise: Use JMockit to redo the big exercise.
                The idea is to see how JMockit eases the developers job
                using annotations, dependency injection and the like.
        * PMD
            * What is PMD for?
            * Using PMD from the command line
            * Using PMD from ant
            * Using PMD from eclipse

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
