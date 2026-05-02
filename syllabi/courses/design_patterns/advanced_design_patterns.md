---
tags:
  - concepts:design-patterns
  - concepts:oop
  - concepts:solid
  - concepts:uml
level: advanced
category: design-patterns
duration_hours: 40
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: advanced_design_patterns -->
# Advanced `design patterns`

## Description
`Design patterns` are solutions to software design problems that recur during real-world application
development and that apply good software design principles.
Through the use of patterns developers and architects reuse the valuable experience gained by
others who have successfully solved similar problems. The design pattern terminology also serves
as a common language to succinctly describe parts of system design.

During this course we will review the fundamental principles of object oriented software design and
understand how `design patterns` apply these principles to a set of design problems.
The course explain the advanced object oriented principles (`SOLID`, Layering, Contracts, ...) which are the heart of
all `design patterns`, and which on their own lead to more quality, flexible, reusable code.
The course provides a quick introduction to the Unified Modeling Language (`UML`) which is
commonly used to describe `design patterns`.
For each of studied patterns you will learn the motivation and context of the pattern and how it
solves the problem at hand. The study of each pattern will be accompanied by real-world examples
and a lab in which you will practice applying the pattern in the some programming language.
This is the full version of the `Design Patterns` Course covering all 24 GOF patterns.

## Duration
40 hours / 5 days

## Intended Audience
* Software developers with experience in an object oriented language

## Prerequisites
* At least one year experience in programming an object oriented language (`Java`, `Python`, ...).
* Understanding of the following:
    * abstract data type
    * encapsulation
    * overriding
    * overloading
    * inheritance
    * polymorphism
    * abstract classes
    * virtual methods

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Describe and apply good principles for object oriented software design
* Describe `design patterns` and provide examples of problems and their pattern solutions
* Cover the most important GOF patterns in depth, and provide an overview of the `rest`
* Recognize and understand patterns in existing code
* Learn when, how and which pattern to use, if appropriate for a new problem

## Outline
<!-- chapter: advanced-object-oriented-design-guideline, duration: 7h -->
* Advanced Object Oriented Design Guideline
    * Object Oriented Refresher
        * The real power of Object Oriented modeling
        * Importance of Encapsulation / Information Hiding
        * Correct Inheritance
        * Abstraction and Interfaces
    * Other Important Design Principles
        * Low Coupling and High Cohesion
        * Layered Architecture
    * `SOLID` principles
        * Single Responsibility Principle
        * The Open Closed Principle
        * The Liskov Substitution Principle
        * The Interface Segregation Principle
        * The Dependency Inversion Principle
    * Package Design Principles
        * The Reuse Release Principle
        * The Stable Dependencies Principle
        * The A cyclic Dependencies Principle
    * Introduction to `UML`
    * Contract based programming
        * What is it?
        * Interfaces as contracts
        * The importance holding interfaces and abstractions
<!-- chapter: design-patterns, duration: 10h -->
* `Design Patterns`
    * Introduction To `Design Patterns`
        * The Composite Pattern as An Example
        * What Are `Design Patterns`
        * `Design Patterns` vs. Data Structures
        * What's in A Design Pattern
        * The GOF Design Pattern Book
        * Creational, Behavioral and Structural Patterns
    * Inheritance
        * Inheritance as a design pattern
        * Inheritance over use
    * Our First Patterns
        * The Composite
        * The Interpreter
        * The Adapter
    * Practical Exercises
        * Exercise on The Composite
        * Exercise The Interpreter
        * Exercise on The Adapter
    * Behavioral Patterns
        * Template Method
        * Strategy
        * Inheritance vs. Composition in Patterns
        * Choosing the right Pattern
    * Creational Patterns
        * Factory Method
        * Factory method vs. Good old factories
        * Abstract Factory
        * The Creational vs. Behavioral Patterns
        * Choosing the right Pattern
<!-- chapter: solidifying-understanding-of-patterns, duration: 13h -->
* Solidifying understanding of Patterns
    * Practical Exercises
        * Template Method Exercise, Factory Method Exercise
        * Strategy Pattern Exercise, Abstract Factory Exercise
    * More Behavioral Patterns
        * Proxy
        * Decorator
        * Comparing Recursive Patterns
        * Comparing Delegating Patterns
        * Iterator
        * Observer
    * Encapsulating Functionality
        * The Command Pattern
        * Command vs. Visitor
    * Practical Exercises
        * Proxy Exercise
        * Decorator Exercise
        * Iterator Exercise
        * Observer Exercise
        * Command Exercise
        * Encapsulating Functionality
        * From Command to Visitor
        * Double Dispatch
        * A cyclic Visitor
        * Builder
        * Observer aka Listener
    * Practical Exercises
        * Visitor Exercise
        * Builder Exercise
        * Observer Exercise
    * Less Common GOF `Design Patterns`
        * Bridge
        * Facade
        * `Design patterns` Vs. Architectural Patterns
        * Flyweight
        * Chain of Responsibility
        * Mediator
        * Memento
        * State
<!-- chapter: conclusions-deep-comparison-and-implications-of-patterns, duration: 1h -->
* Conclusions, Deep Comparison and Implications of Patterns
    * Practical Exercises
        * Bridge Exercise
        * Facade Exercise
<!-- chapter: design-patterns-from-the-functional-world, duration: 1h -->
* `Design patterns` from the functional world
    * Monads
    * Maybe
    ...
<!-- chapter: meta-patterns, duration: 7h -->
* Meta patterns
    * Multi `threading`
    * Multi processing
    * OSGi
        * `Java`-based OSGi frameworks
            * Apache Felix
            * Eclipse Equinox
            * Knopflerfish
            * ProSyst mBS
        * `.NET`-based OSGi frameworks
            * Eclipse Concierge OSGi
            * nOSGi
        * `JavaScript`-based OSGi frameworks:
            * OSGi.js
        * `Python`-based OSGi frameworks:
            * Pelix
        * `C++`-based OSGi frameworks:
            * CppMicroServices
            * Celix
    * `Docker`
    * `docker`-compose
    * k8s
<!-- chapter: summary, duration: 1h -->
* Summary
    * Comparison of GOF Patterns
    * `When` to not to use patterns
    * Overview of other GOF and non GOF patterns

## Notes
This course could can be done with `Java`, `C#`, `Python` or `C++` materials.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
