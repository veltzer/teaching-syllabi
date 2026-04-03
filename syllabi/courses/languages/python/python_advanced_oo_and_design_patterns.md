---
tags:
  - languages:python
  - concepts:design-patterns
  - concepts:oop
  - concepts:solid
level: advanced
category: language
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: python_advanced_oo_and_design_patterns -->
# `Design Patterns` and Advanced Object-Oriented Design for `Python` Developers

## Description
`Design patterns` are solutions to software design problems that recur during real-world application development and that apply good software design principles.
Through the use of patterns developers and architects reuse the valuable experience gained by others who have successfully solved similar problems.
The design pattern terminology also serves as a common language to succinctly describe parts of system design.

During this course we will review the fundamental principles of object oriented software design and understand how `design patterns` apply these principles to a set of design problems.
The course explain the advanced object oriented principles (`SOLID`,OCP,`DI`) which are the heart of all `design patterns`, and which on their own lead to more quality, flexible, reusable code.
The course provides a quick introduction to the Unified Modeling Language (`UML`) which is commonly used to describe `design patterns`.
For each of studied patterns you will learn the motivation and context of the pattern and how it solves the problem at hand.
The study of each pattern will be accompanied by real-world examples and a lab in which you will practice applying the pattern in the `Java` programming language.

## Duration
32 hours / 4 days

## Intended Audience
* Software developers with experience in an object oriented language
* Experience in Object Oriented Development with `Python`
* Any `Java`/`C#`, `C++`, or `Typescript` experience is beneficial

## Prerequisites
* working experience with `design patterns` and object-oriented design for `python` developers
* experience with `Python` programming

## Objectives
* Describe and apply good principles for object oriented software design.
* Describe `design patterns` and provide examples of problems and their pattern solutions in `Java`
* Cover the most important GOF patterns in depth, and provide an overview of the `rest`
* Recognize and understand patterns in existing code
* Learn `when`, how and which pattern to use, if appropriate for a new problem

## Outline
<!-- chapter: object-orientation-refresher, duration: 11h -->
* Object Orientation Refresher
    * What is the Object Oriented Paradigm
        * Object oriented vs procedural vs functional
        * Object Orientation as a modeling technique
        * What are Objects - Data and functionality together
        * state and identity
    * Instances
        * instances and identity
        * the new keyword and the heap
        * The need for constructors
        * The default constructor
        * class declaration syntax
        * member functions
        * function signatures and function overloading
        * the `self-keyword`
        * scoping, locals vs instance members
    * Encapsulation : private, public and protected
        * The need for encapsulation
        * getters and setters
    * Statics and Globals:
        * static data
        * `static-member` functions
        * problems with static
    * Delegation and composition
        * objects with subobjects
        * objects calling objects
        * null members
    * Inheritance
        * classes and classification
        * "is a kind of" relationships
        * the extends keyword
        * delegating to base constructors, the `super-keyword`
        * private vs protected in inheritance
        * inheritance, inherited members and class memory layout
        * polymorphism, virtual/runtime functions
        * overriding base class functions
    * Abstraction
        * abstract classes / interfaces in `Python`
        * abstract algorithms
        * abstract data structures
        * object oriented abstraction vs Templates
<!-- chapter: advanced-object-oriented-design-guidelines, duration: 7h -->
* Advanced Object Oriented Design Guidelines
    * Object Oriented Principles refresher
        * The real power of Object Oriented modeling
        * Importance of Encapsulation / Information Hiding
        * Correct Inheritance
        * Abstraction and Interfaces
    * Other Important Design Principles
        * Low Coupling and High Cohesion
        * Layered Architecture
        * Keep it simple
        * Test, test test
    * `SOLID` principles
        * Single Responsibility Principle
        * The Open Closed Principle
        * The Liskov Substitution Principle
        * The Interface Segregation Principle
        * The Dependency Inversion Principle
    * Package Design Principles
        * The Reuse Release Principle
        * The Stable Dependencies Principle
        * The Acyclic Dependencies Principle
    * Dependency Injection
        * Introduction to `UML`
        * Interfaces as contracts
        * The importance holding interfaces and abstractions
<!-- chapter: design-patterns, duration: 14h -->
* `Design Patterns`
    * Introduction To `Design Patterns`
        * The Composite Pattern as An Example
        * What Are `Design Patterns`
        * `Design Patterns` vs. Data Structures
        * What's in A Design Pattern
        * The GOF Design Pattern Book
        * Creational , Behavioral and Structural Patterns
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
    * Summary
        * Comparison of GOF Patterns
        * `When` to not to use patterns
        * Overview of other GOF and non GOF patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
