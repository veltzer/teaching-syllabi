---
tags:
  - languages:php
  - concepts:web-development
  - networking:web
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: laravel -->
# `PHP` with Laravel

## Description
Laravel is the most popular `PHP` framework, providing an elegant and expressive syntax for building modern web applications. This course covers the full Laravel ecosystem, from MVC architecture and `Eloquent ORM` to Blade templates, routing, middleware, authentication, queues, events, testing, and deployment. Participants will learn to build robust, maintainable web applications following Laravel best practices and conventions. The course includes hands on exercises.

## Duration
24 hours / 3 days

## Intended Audience
* `PHP` developers who want to build modern web applications with Laravel.
* Web developers transitioning to the Laravel framework.
* Developers who need to build full-stack applications with a productive `PHP` framework.

## Prerequisites
* `Solid` understanding of `PHP` programming.
* Basic knowledge of `HTML`, `CSS`, and `SQL`.
* Familiarity with MVC concepts is helpful but not required.

## Objectives
* Understand Laravel's architecture and core concepts
* Build web applications using MVC patterns with Laravel
* Use `Eloquent ORM` for database interactions
* Implement authentication, authorization, and middleware
* Work with queues, events, and background processing
* Write tests and deploy Laravel applications

## Outline
<!-- chapter: introduction-to-laravel, duration: 2h -->
* Introduction to Laravel
    * What is Laravel and why use it?
    * Installing Laravel with `Composer`
    * Project structure and directory layout
    * Artisan command-line tool
    * Configuration and environment files
<!-- chapter: routing-and-controllers, duration: 2h -->
* Routing and Controllers
    * Defining routes and route groups
    * Route parameters and constraints
    * Named routes and URL generation
    * Controllers and resource controllers
    * Route model binding
    * `API` resource routes
<!-- chapter: blade-templating, duration: 2h -->
* Blade Templating
    * Blade syntax and directives
    * Template inheritance and layouts
    * Components and slots
    * Conditional rendering and loops
    * Including sub-views and partials
    * Blade and `JavaScript` frameworks
<!-- chapter: eloquent-orm, duration: 3h -->
* `Eloquent ORM`
    * Models and conventions
    * Migrations and schema builder
    * `CRUD` operations
    * Query scopes and accessors/mutators
    * Relationships: one-to-one, one-to-many, many-to-many, polymorphic
    * Eager loading and the N+1 problem
    * Collections and pagination
<!-- chapter: middleware, duration: 2h -->
* Middleware
    * Understanding the middleware pipeline
    * Creating custom middleware
    * Global vs route middleware
    * Middleware groups
    * Rate limiting middleware
    * Middleware parameters
<!-- chapter: authentication-and-authorization, duration: 2h -->
* Authentication and Authorization
    * `Laravel Breeze` and `Laravel Fortify`
    * Authentication scaffolding
    * Guards and providers
    * Policies and gates
    * Role-based access control
    * `API` authentication with Sanctum
<!-- chapter: validation-and-forms, duration: 2h -->
* Validation and Forms
    * Request validation and form requests
    * Custom validation rules
    * Error handling and display
    * `File` uploads and storage
    * `CSRF` protection
<!-- chapter: queues-and-jobs, duration: 2h -->
* Queues and Jobs
    * Queue configuration and drivers
    * Creating and dispatching jobs
    * Job middleware and chaining
    * Failed job handling and retries
    * `Laravel Horizon` for queue monitoring
    * Scheduled tasks with the task scheduler
<!-- chapter: events-and-listeners, duration: 2h -->
* Events and Listeners
    * Defining events and listeners
    * Event discovery and registration
    * Broadcasting events with WebSockets
    * Event subscribers
    * Model events and observers
<!-- chapter: testing-laravel-applications, duration: 2h -->
* Testing Laravel Applications
    * PHPUnit integration and test setup
    * Feature tests and `HTTP` tests
    * Database testing and factories
    * Mocking and faking services
    * Browser testing with `Laravel Dusk`
<!-- chapter: deployment, duration: 3h -->
* Deployment
    * Preparing for production
    * Configuration caching and optimization
    * Deploying with `Laravel Forge` and Envoyer
    * `Docker` and containerized deployments
    * `CI/CD` pipeline integration
    * Monitoring and logging in production

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
