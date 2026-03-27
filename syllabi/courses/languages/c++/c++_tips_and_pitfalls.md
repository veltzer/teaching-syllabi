---
tags:
  - languages:c++
  - practices:performance
  - concepts:best-practices
  - languages:stl
level: advanced
category: language
duration_days: 3
audience:
  - audiences:developers
---
# C++ Tips and Pitfalls

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
The course divided into following parts:
* The pass through all features of C++ but on higher level ( example: no explanation
what is the meaning of Constructor and Destructor, but the cost of these functions and
ways to decrease number of there invocations will be discussed ).
* Standard Template Library, C++ Streams,
* Object Oriented Design
* Pitfalls, Tips, Optimizations

## Duration
24 hours / 3 days

## Intended Audience
* C++ developers
* software engineers working on performance-critical applications

## Prerequisites
This course is for programmers which already have C++ experience.

## Objectives
The main goal of the course is to provide deep understanding of C++ internals - the look on
some C++ features from the compiler point of view; how these features are implemented in
compiler and why. To show, how this knowledge can help to write short and efficient code.
We'll discuss the cost of C++ features and the ways to decrease resources needed for
application ( memory, time ).

## Exercises
The set of small exercises, built as riddles will bring participants to the real world of
understanding of C++.

## Outline
* What's going in CTOR & DTOR - the look from Compiler point of view
    * Temporary objects
    * Why always to provide CTOR and DTOR
* When to return by Reference and when by Value
    * Use reference everywhere it possible
* Behind "inline" mechanism
    * What happens if compiler doesn't succeed to INLINE function?
    * When really to use INLINE mechanism
    * Does it make sense to declare virtual function as inline?
* Operators and Operator Overloading
    * Overloading of some specific operators
    * Conversion operator and it pitfalls
    * Operators New and Delete
        * Overloading
        * How to use overloaded NEW and DELETE to find memory leaks
        * Placement NEW operator
* Templates
    * Internals
    * How to write efficient code using template mechanism
* Exception Handler - www - what, when, why
    * Exception Handler in CTORs and DTORs
    * Uncaught Exceptions and recovery ( terminate, set_terminate functions)
* Polymorphism
    * Do you really understand the mechanism?
    * Internals
    * Polymorphism and multiple inheritance
* Pointers to member-functions
    * How to declare and to use
    * How to save a lot of code
* Run Time Type Identification (`RTTI`)
* `STL` - Standard Template Library:
    * Containers
    * Algorithms
    * `auto_ptr`
    * locale
* C++ - Standard I/O Library - Streams
    * Stream manipulators
    * Unusual examples of stream usage
* Class Design
    * CONST correctness
    * When to declare member-function as virtual and when not
    * Data-members: when private and when protected
* Tips and Pitfalls
    * CTOR & DTOR pitfalls
    * Inheritance pitfalls
    * Tips for good C++ programming
* Code Optimization
    * Trivial optimizations
    * Object size
* Coding Rules and Naming Conventions

## References
* [B.Stroustrup, The C++ Programming Language, Second Edition, Addison-Wesley Publishing Company](https://www.stroustrup.com/4th.html)
* [B.Stroustrup, The Design and Evolution of C++, Addison-Wesley Publishing Company](https://www.stroustrup.com/dne.html)
* [S.Lippman, C++ Primer, Second Edition,Addison-Wesley Publishing Company](https://zhjwpku.com/assets/pdf/books/C++.Primer.5th.Edition_2013.pdf)
* [Scott Meyers, Effective C++, Addison-Wesley Publishing Company](https://www.dsi.fceia.unr.edu.ar/downloads/informatica/info_II/c++/Effective%20C++%20+%20More%20Effective%20C++.pdf)
* [Scott Meyers, More Effective C++, Addison-Wesley Publishing Company](https://www.dsi.fceia.unr.edu.ar/downloads/informatica/info_II/c++/Effective%20C++%20+%20More%20Effective%20C++.pdf)
* [Scott Meyers, Effective Modern C++, Addison-Wesley Publishing Company](https://zhjwpku.com/assets/pdf/books/C++.Primer.5th.Edition_2013.pdf)
* [E.Gamma, R.Helm, R.Johnson, J.Vlissides, Design Patterns, Addison-Wesley Publishing Company](http://www.javier8a.com/itc/bd1/articulo.pdf)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
