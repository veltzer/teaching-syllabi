---
tags:
  - languages:java
  - tools:spring
  - concepts:design-patterns
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: spring_core -->
# `Spring` Core

## Description
This course provides a deep and thorough understanding of the `Spring` Framework core. Students will learn the `IoC` container, dependency injection patterns, bean lifecycle management, and the various configuration styles. The course also covers AOP, the `Spring` Expression Language, profiles, the event system, resource handling, internationalization, and validation. A comparison of `Spring` Framework with `Spring Boot` is included to clarify `when` and how to use each.

## Duration
24 hours / 3 days

## Intended Audience
* `Java` developers building enterprise applications with the `Spring` ecosystem
* Software engineers who want a `solid` foundation in `Spring` before moving to `Spring Boot`
* Architects evaluating the `Spring` Framework for their projects

## Prerequisites
* Intermediate `Java` programming skills (classes, interfaces, generics, annotations)
* Understanding of object-oriented design principles
* Familiarity with a build tool such as `Maven` or `Gradle`
* Basic knowledge of `design patterns` (Factory, Proxy, Observer)

## Objectives
* Understand the `Spring` `IoC` container and how it manages beans
* Apply dependency injection using constructor, setter, and field injection
* Configure `Spring` applications using annotations, `Java` configuration, and `XML`
* Manage bean lifecycle, scopes, and initialization callbacks
* Implement cross-cutting concerns with `Spring` AOP
* Use SpEL for dynamic expression evaluation in configuration
* Leverage profiles for environment-specific configuration
* Understand the differences between `Spring` Framework and `Spring Boot`

## Outline
<!-- chapter: introduction-to-the-spring-framework, duration: 1h -->
* Introduction to the `Spring` Framework
    * History and evolution of `Spring`
    * The `Spring` ecosystem overview
    * Core principles: `IoC` and `DI`
    * Setting up a `Spring` project
<!-- chapter: the-ioc-container, duration: 2h -->
* The `IoC` Container
    * ApplicationContext and BeanFactory
    * Container initialization and refresh
    * Bean definitions and metadata
    * Singleton vs prototype and other scopes
    * Lazy initialization
    * Container extension points
<!-- chapter: dependency-injection, duration: 2h -->
* Dependency Injection
    * Constructor injection
    * Setter injection
    * Field injection and why it is discouraged
    * Autowiring strategies
    * Qualifier and primary beans
    * Optional dependencies
    * Circular dependency handling
    * Injection of collections and maps
<!-- chapter: bean-lifecycle, duration: 2h -->
* Bean Lifecycle
    * Bean instantiation and population
    * @PostConstruct and @PreDestroy
    * InitializingBean and DisposableBean interfaces
    * Custom init and destroy methods
    * BeanPostProcessor and BeanFactoryPostProcessor
    * Aware interfaces
    * Bean definition inheritance
<!-- chapter: configuration-styles, duration: 2h -->
* Configuration Styles
    * Annotation-based configuration: @Component, @Service, @Repository, @Controller
    * Component scanning and filters
    * `Java`-based configuration with @Configuration and @Bean
    * `XML`-based configuration
    * Mixing configuration styles
    * @Import and modular configuration
    * Conditional bean registration with @Conditional
<!-- chapter: aspect-oriented-programming-aop, duration: 2h -->
* Aspect-Oriented Programming (AOP)
    * Cross-cutting concerns and the need for AOP
    * AOP concepts: aspect, join point, advice, pointcut
    * `Spring` AOP proxy mechanism
    * @Aspect and @Around, @Before, @After advice types
    * Pointcut expressions and designators
    * Introduction and mix-ins
    * AOP vs AspectJ
<!-- chapter: spring-expression-language-spel, duration: 2h -->
* `Spring` Expression Language (SpEL)
    * SpEL syntax and evaluation
    * Property access and method invocation
    * Operators and comparisons
    * Collection selection and projection
    * Using SpEL in annotations and `XML`
    * Template expressions
<!-- chapter: profiles-and-environment-abstraction, duration: 2h -->
* Profiles and Environment Abstraction
    * Defining profiles
    * Activating profiles
    * Profile-specific beans and configuration
    * The Environment abstraction
    * Property sources and @PropertySource
    * Externalized configuration with @Value
<!-- chapter: events, duration: 2h -->
* Events
    * The ApplicationEvent model
    * Publishing and listening to events
    * @EventListener and @TransactionalEventListener
    * Asynchronous event handling
    * Custom event types
    * Ordered event listeners
<!-- chapter: resource-handling, duration: 1h -->
* Resource Handling
    * The Resource abstraction
    * Built-in Resource implementations
    * ResourceLoader and ResourcePatternResolver
    * Loading classpath, filesystem, and URL resources
    * Resource injection with @Value
<!-- chapter: internationalization-i18n, duration: 2h -->
* Internationalization (i18n)
    * MessageSource interface
    * Configuring message bundles
    * Resolving messages with parameters
    * Locale resolution strategies
    * Using MessageSource in applications
<!-- chapter: validation, duration: 2h -->
* Validation
    * `Spring` Validator interface
    * `Bean Validation` (JSR-380) integration
    * Custom constraint annotations
    * Validation groups
    * DataBinder and binding results
    * Programmatic validation
<!-- chapter: spring-framework-vs-spring-boot, duration: 2h -->
* `Spring` Framework vs `Spring Boot`
    * What `Spring Boot` adds on `top` of `Spring`
    * Auto-configuration explained
    * Starters and opinionated defaults
    * `When` to use `Spring` Framework directly
    * Migrating from `Spring` to `Spring Boot`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
