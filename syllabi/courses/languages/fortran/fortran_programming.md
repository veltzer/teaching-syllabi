---
tags:
  - languages:fortran
  - concepts:programming
  - concepts:parallel-computing
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: fortran_programming -->
# Modern `Fortran` Programming

## Description
`Fortran` remains the dominant language in high-performance computing, scientific simulation,
and numerical analysis. Modern `Fortran` (2008/2018/2023) has evolved significantly from its
origins, offering features such as object-oriented programming, coarrays for parallel computing,
and interoperability with `C`. This course covers modern `Fortran` from fundamentals through
advanced topics including parallel programming, performance optimization, and integration with
scientific computing libraries. Students will gain practical skills for writing efficient,
maintainable `Fortran` code for computational science and engineering.
The course includes hands on exercises.

## Duration
32 hours / 4 days

## Intended Audience
* Scientists and engineers who need to write high-performance numerical code.
* Developers maintaining or extending existing `Fortran` codebases.
* HPC practitioners looking to leverage modern `Fortran` features.

## Prerequisites
* Prior programming experience in another language such as `C`, `Python`, or `MATLAB`.
* Basic understanding of linear algebra and numerical concepts.
* Familiarity with command-line interfaces.

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Write `clean`, modern `Fortran` code using current standards
* Use arrays and `array` operations effectively for numerical computation
* Create modular programs with procedures, modules, and derived types
* Write parallel code using coarrays and `DO CONCURRENT`
* Integrate `Fortran` with `C` and scientific computing libraries
* Apply performance optimization and debugging techniques

## Outline
<!-- chapter: introduction-to-modern-fortran, duration: 2h -->
* Introduction to Modern `Fortran`
    * History and evolution of `Fortran`
    * `Fortran` 2008, 2018, and 2023 standards
    * Setting up the development environment
    * Compilers: gfortran, ifort, nvfortran
    * Hello World and program structure
    * Free-form source and modern conventions
<!-- chapter: fundamental-data-types-and-operations, duration: 2h -->
* Fundamental Data Types and Operations
    * Intrinsic types: integer, real, complex, logical, character
    * Kind parameters and precision control
    * Constants and variables
    * Arithmetic, relational, and logical operators
    * Implicit typing and `IMPLICIT NONE`
    * Type conversion and mixed-mode arithmetic
<!-- chapter: arrays-and-array-operations, duration: 3h -->
* Arrays and `Array` Operations
    * `Array` declaration and initialization
    * `Array` slicing and sections
    * Whole-`array` operations
    * Intrinsic `array` functions (SUM, MAXVAL, MATMUL, etc.)
    * Allocatable arrays
    * `Array` constructors and reshape
    * WHERE and FORALL statements
<!-- chapter: control-structures, duration: 2h -->
* Control Structures
    * IF / ELSE IF / ELSE constructs
    * SELECT CASE
    * `DO-loops` and DO WHILE
    * `DO CONCURRENT`
    * EXIT and CYCLE statements
    * Block construct
<!-- chapter: procedures, duration: 2h -->
* Procedures
    * Functions and subroutines
    * Intent attributes (IN, OUT, INOUT)
    * Optional and keyword arguments
    * Recursive procedures
    * Pure and elemental procedures
    * Interface blocks and overloading
<!-- chapter: modules-and-program-organization, duration: 2h -->
* Modules and Program Organization
    * Module structure and USE statement
    * Public and private accessibility
    * Submodules
    * Module procedures
    * Encapsulation and information hiding
<!-- chapter: derived-types-and-object-oriented-programming, duration: 2h -->
* Derived Types and Object-Oriented Programming
    * Defining derived types
    * Type components and initialization
    * Type-bound procedures
    * Inheritance and type extension
    * `Abstract-types` and deferred bindings
    * Polymorphism and SELECT TYPE
<!-- chapter: pointers-and-dynamic-memory, duration: 2h -->
* Pointers and Dynamic Memory
    * Pointer declaration and association
    * ALLOCATE and DEALLOCATE
    * Pointer assignment vs data assignment
    * Linked data structures
    * Memory management best practices
<!-- chapter: input-output, duration: 2h -->
* Input/Output
    * Formatted and unformatted `I/O`
    * `File` handling (OPEN, CLOSE, READ, WRITE)
    * Internal files
    * Namelist `I/O`
    * Stream `I/O`
    * Error handling in `I/O` operations
<!-- chapter: parallel-programming-with-coarrays, duration: 2h -->
* Parallel Programming with Coarrays
    * Introduction to coarrays
    * Coarray declaration and usage
    * Image control statements (SYNC ALL, SYNC IMAGES)
    * Critical sections and locks
    * Collective operations
    * Teams and events (`Fortran` 2018)
<!-- chapter: additional-parallelism, duration: 2h -->
* Additional Parallelism
    * `DO CONCURRENT` and compiler optimization
    * `OpenMP` integration with `Fortran`
    * Parallel directives and clauses
    * Offloading to accelerators
<!-- chapter: interoperability-with-c, duration: 2h -->
* Interoperability with `C`
    * ISO_C_BINDING module
    * Matching `Fortran` and `C` types
    * Calling `C` functions from `Fortran`
    * Calling `Fortran` procedures from `C`
    * Handling strings and arrays across languages
<!-- chapter: build-tools-and-project-management, duration: 2h -->
* Build Tools and Project Management
    * `CMake` for `Fortran` projects
    * fpm (`Fortran` Package Manager)
    * Makefiles and build automation
    * Dependency management
<!-- chapter: scientific-computing-libraries, duration: 2h -->
* Scientific Computing Libraries
    * LAPACK and BLAS for linear algebra
    * Using optimized vendor libraries (MKL, OpenBLAS)
    * NetCDF and HDF5 for data `I/O`
    * Interfacing with numerical libraries
<!-- chapter: performance-optimization-and-debugging, duration: 3h -->
* Performance Optimization and Debugging
    * Compiler optimization flags
    * Profiling `Fortran` code
    * Vectorization and SIMD
    * Cache-friendly programming
    * Debugging tools (`gdb`, compiler diagnostics)
    * Common pitfalls and best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
