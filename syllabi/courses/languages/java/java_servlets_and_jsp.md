---
tags:
  - languages:java
  - networking:web
  - concepts:web-development
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: java_servlets_and_jsp -->
# `Java` Servlets & JSP

## Description
This course covers the fundamentals of `Java` web application development using Servlets
and `JavaServer Pages` (JSP). Participants will learn the servlet lifecycle, request and
response handling, session management, JSP syntax, and the MVC pattern. The course
also addresses deployment configuration, security constraints, and `WebSocket` support.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers who want to build server-side web applications.
* Developers transitioning to `Java` web development.

## Prerequisites
* Working knowledge of `Java` programming.
* Basic understanding of `HTML` and `HTTP`.

## Objectives
* Participants will gain a `solid` understanding of
    * The servlet lifecycle and request/response model.
    * Session management techniques.
    * JSP syntax and tag libraries.
    * The MVC architectural pattern for web applications.
    * Deployment descriptors and security configuration.
    * `WebSocket` communication in `Java`.

## Outline
<!-- chapter: servlet-fundamentals, duration: 1h -->
* Servlet Fundamentals
    * What is a servlet
    * Servlet container architecture
    * Servlet lifecycle — init, service, destroy
    * HttpServlet class
    * Servlet configuration and initialization parameters
<!-- chapter: request-and-response-handling, duration: 2h -->
* Request and Response Handling
    * HttpServletRequest object
    * HttpServletResponse object
    * Request parameters and attributes
    * Request dispatching and forwarding
    * Response headers and content types
    * `File` upload handling
<!-- chapter: filters, duration: 1h -->
* Filters
    * Filter interface and lifecycle
    * Filter chains
    * Common filter use cases
    * Character encoding filters
    * Logging and auditing filters
<!-- chapter: listeners, duration: 1h -->
* Listeners
    * Context listeners
    * Session listeners
    * Request listeners
    * Attribute listeners
    * Application event handling
<!-- chapter: session-management, duration: 1h -->
* Session Management
    * `HTTP` session `API`
    * Cookies
    * URL rewriting
    * Session timeout configuration
    * Distributed session management
<!-- chapter: jsp-syntax, duration: 1h -->
* JSP Syntax
    * JSP lifecycle
    * Directives, declarations, and scriptlets
    * Expression Language (EL)
    * Implicit objects
    * Error pages
<!-- chapter: jstl-and-custom-tags, duration: 2h -->
* JSTL and Custom Tags
    * Core tag library
    * Formatting tag library
    * `SQL` tag library
    * Functions tag library
    * Creating custom tag libraries
<!-- chapter: mvc-pattern, duration: 1h -->
* MVC Pattern
    * Model-View-Controller architecture
    * Front Controller pattern
    * Separating concerns in web applications
    * Integration with service and data layers
<!-- chapter: deployment-descriptors, duration: 2h -->
* Deployment Descriptors
    * web.`xml` configuration
    * Annotation-based configuration
    * Context parameters
    * Welcome files
    * Error page configuration
<!-- chapter: security-constraints, duration: 2h -->
* Security Constraints
    * Declarative security
    * Programmatic security
    * Authentication mechanisms
    * Role-based access control
    * `HTTPS` configuration
<!-- chapter: websocket-support, duration: 2h -->
* `WebSocket` Support
    * `WebSocket` protocol overview
    * `Java` `WebSocket` `API`
    * Server endpoints
    * Client endpoints
    * Message types and encoders/decoders

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
