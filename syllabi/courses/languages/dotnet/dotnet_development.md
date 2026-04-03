---
tags:
  - languages:csharp
  - tools:aspnet
  - tools:entity-framework
  - concepts:web-development
level: beginner
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: dotnet_development -->
# `.NET` Development

## Description
This course provides a comprehensive introduction to modern `.NET` development with `C#`. Starting from `C#` language fundamentals, the course covers building web applications and APIs with `ASP.NET Core`, data access with `Entity Framework Core`, dependency injection, middleware pipelines, `Minimal APIs`, and an overview of Blazor for interactive web UIs. Students will gain the skills to build full-featured `.NET` applications from the ground up.

## Duration
24 hours / 3 days

## Intended Audience
* Developers new to the `.NET` ecosystem looking to build modern applications
* Programmers with experience in other languages transitioning to `C#` and `.NET`
* Software engineers who want to build web applications and APIs with `ASP.NET Core`
* Full-stack developers exploring `.NET` as a backend platform
* Students and professionals seeking a `solid` foundation in `.NET` development

## Prerequisites
* Basic programming experience in any language (variables, loops, functions, classes)
* Understanding of object-oriented programming concepts
* Familiarity with `HTTP` protocol and basic web concepts
* Basic knowledge of relational databases and `SQL`
* Experience using a command-line interface
* A development environment with `.NET SDK` installed (or willingness to install it)

## Objectives
* Understand `C#` language fundamentals including types, classes, interfaces, generics, and `LINQ`
* Build `RESTful APIs` and web applications using `ASP.NET Core`
* Implement data access and persistence with `Entity Framework Core`
* Apply dependency injection patterns using the built-in `.NET` `DI` container
* Understand and configure the `ASP.NET Core` middleware pipeline
* Create lightweight APIs using the `Minimal APIs` approach
* Gain an overview of Blazor for building interactive web UIs with `C#`

## Outline
<!-- chapter: c-fundamentals, duration: 4h -->
* `C#` Fundamentals
    * Introduction to `.NET` platform and the CLR
    * `C#` syntax, data types, and variables
    * Control flow: conditionals, loops, and pattern matching
    * Methods, parameters, and `return-types`
    * Classes, objects, and constructors
    * Properties, fields, and access modifiers
    * Inheritance, interfaces, and polymorphism
    * Generics and generic constraints
    * Delegates, events, and `lambda` expressions
    * Exception handling with try/catch/finally
    * Collections: List, Dictionary, arrays, and IEnumerable
    * `LINQ` queries and extension methods
    * Asynchronous programming with `async`/`await` and Task
    * Nullable reference types and null safety
    * Records, structs, and value types
<!-- chapter: asp-net-core-fundamentals, duration: 4h -->
* `ASP.NET Core` Fundamentals
    * Introduction to `ASP.NET Core` and the hosting model
    * Project structure and the Program.cs entry point
    * Request processing pipeline overview
    * Controllers and action methods
    * Routing: attribute routing and conventional routing
    * Model binding and request validation
    * Action results and response formatting
    * Content negotiation and `JSON` serialization with System.Text.`Json`
    * Error handling and exception middleware
    * Configuration with appsettings.`json` and environment variables
    * Logging with the built-in logging framework
    * Environments and environment-specific configuration
<!-- chapter: entity-framework-core, duration: 4h -->
* `Entity Framework Core`
    * Introduction to `Entity Framework Core` and `ORM` concepts
    * DbContext configuration and setup
    * Entity classes and data annotations
    * Fluent `API` configuration
    * Relationships: one-to-many, many-to-many, and one-to-one
    * Migrations: creating, applying, and managing schema changes
    * Querying data with `LINQ` to entities
    * Tracking vs. no-tracking queries
    * Insert, update, and delete operations
    * Transactions and concurrency handling
    * Seeding data and database initialization
    * Performance considerations and query optimization
<!-- chapter: dependency-injection, duration: 3h -->
* Dependency Injection
    * Introduction to dependency injection and inversion of control
    * The built-in `.NET` `DI` container
    * Service lifetimes: transient, scoped, and singleton
    * Registering services in Program.cs
    * Constructor injection in controllers and services
    * The IServiceProvider and service resolution
    * Options pattern with IOptions, IOptionsSnapshot, and IOptionsMonitor
    * Keyed services and factory-based registration
    * Best practices and common anti-patterns
<!-- chapter: middleware, duration: 3h -->
* Middleware
    * Understanding the `ASP.NET Core` middleware pipeline
    * Built-in middleware: static files, routing, authentication, authorization
    * Request and response flow through middleware
    * Writing custom middleware classes
    * Inline middleware with app.Use and app.Run
    * Middleware ordering and its impact on behavior
    * Branching the pipeline with app.Map and app.MapWhen
    * Error handling middleware and exception pages
    * CORS middleware configuration
<!-- chapter: minimal-apis, duration: 3h -->
* `Minimal APIs`
    * Introduction to `Minimal APIs` and `when` to use them
    * Defining endpoints with app.MapGet, app.MapPost, and related methods
    * Route parameters and query string binding
    * Request body binding and validation
    * Returning results with Results and TypedResults
    * Endpoint filters
    * Grouping endpoints with MapGroup
    * Adding authentication and authorization to minimal endpoints
    * `Minimal APIs` vs. controller-based APIs
<!-- chapter: blazor-overview, duration: 3h -->
* Blazor Overview
    * Introduction to Blazor and component-based UI development
    * `Blazor Server` vs. `Blazor WebAssembly` vs. `Blazor United`
    * Razor components and Razor syntax
    * Data binding and event handling
    * Component parameters and cascading values
    * Dependency injection in Blazor components
    * Navigation and routing in Blazor
    * Calling `REST APIs` from Blazor with HttpClient
    * `JavaScript` interop
    * `When` to choose Blazor and its trade-offs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
