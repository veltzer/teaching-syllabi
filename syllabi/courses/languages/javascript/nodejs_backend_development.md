---
tags:
  - languages:javascript
  - languages:typescript
  - concepts:web-development
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: nodejs_backend_development -->
# `Node.js` Backend Development

## Description
This course provides a comprehensive guide to building backend applications and `REST APIs` with `Node.js`. Students will learn the `Node.js` runtime architecture, asynchronous programming patterns, `Express.js` framework, authentication, database integration, testing, and deployment. The course emphasizes production-ready practices including security, logging, containerization, and scaling. `TypeScript` integration is covered throughout.

## Duration
32 hours / 4 days

## Intended Audience
* `JavaScript` developers moving into backend and server-side development
* Frontend developers who want to become full-stack with `Node.js`
* Backend developers from other languages transitioning to `Node.js`
* Software engineers building `REST APIs` and `microservices` with `JavaScript`
* Development teams adopting `Node.js` for their server-side stack

## Prerequisites
* `Solid` understanding of `JavaScript` (`ES6`+ features including promises and `async`/`await`)
* Familiarity with `HTTP` protocol and `REST API` concepts
* Basic knowledge of `JSON` and working with APIs
* Experience with `npm` and command-line tools
* Understanding of basic database concepts (`SQL` or `NoSQL`)
* Familiarity with `TypeScript` basics is helpful but not required

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Understand `Node.js` architecture including the event loop, V8, and `libuv`
* Manage packages and dependencies with `npm`, `yarn`, and pnpm
* Write asynchronous code using callbacks, promises, and `async`/`await`
* Build `REST APIs` with `Express.js` including routing, middleware, and error handling
* Implement authentication and authorization using `JWT`, `OAuth2`, and Passport
* Integrate `PostgreSQL` (with `Sequelize` and Prisma) and `MongoDB` (with Mongoose)
* Validate input, handle `file` uploads, and implement `WebSocket` communication
* Write tests with `Jest` and Supertest for reliable backend code
* Configure logging with Winston and Pino
* Containerize `Node.js` applications with `Docker` and deploy with PM2
* Apply security best practices following `OWASP` guidelines for `Node.js`
* Use `TypeScript` with `Node.js` for type-safe backend development

## Outline
<!-- chapter: node-js-architecture-and-fundamentals, duration: 2h -->
* `Node.js` Architecture and Fundamentals
    * What is `Node.js` and its use cases
    * The V8 engine, `libuv`, and the event loop
    * Single-threaded model and non-blocking `I/O`
    * The event loop phases and microtask queue
    * REPL and running `Node.js` scripts
    * Global objects and the process module
<!-- chapter: package-management-and-modules, duration: 2h -->
* Package Management and Modules
    * `npm`, `yarn`, and pnpm comparison and usage
    * package.`json` configuration and scripts
    * Semantic versioning and dependency management
    * CommonJS modules (`require`/module.exports)
    * ES modules (import/export) and interoperability
    * Creating and publishing packages
<!-- chapter: asynchronous-programming, duration: 3h -->
* Asynchronous Programming
    * Understanding the asynchronous nature of `Node.js`
    * Callbacks and callback patterns
    * Promises and promise chaining
    * `async`/`await` syntax and error handling
    * Promise.all, Promise.allSettled, Promise.race
    * Event emitters and streams
    * Worker threads for `CPU`-intensive tasks
<!-- chapter: express-js-framework, duration: 3h -->
* `Express.js` Framework
    * Setting up an `Express.js` application
    * Routing: methods, parameters, query strings, and route groups
    * Middleware: built-in, third-party, and custom middleware
    * Request and response objects
    * Error handling middleware and centralized error management
    * Serving static files and template engines
    * Application structure and project organization
<!-- chapter: rest-api-design-and-implementation, duration: 3h -->
* `REST API` Design and Implementation
    * `REST` principles and resource design
    * `CRUD` operations and `HTTP` methods
    * Request validation with Joi and Zod
    * Response formatting and status codes
    * Pagination, filtering, and sorting
    * `API` versioning strategies
    * `API` documentation with Swagger/`OpenAPI`
<!-- chapter: authentication-and-authorization, duration: 3h -->
* Authentication and Authorization
    * Authentication strategies overview
    * `JSON Web Tokens` (`JWT`): creation, verification, and refresh tokens
    * `OAuth2` flows and third-party authentication
    * Passport.js strategies and configuration
    * Password hashing with bcrypt
    * Role-based access control
    * Session management and token storage best practices
<!-- chapter: database-integration, duration: 3h -->
* Database Integration
    * Connecting to `PostgreSQL` with `Sequelize` `ORM`
    * `Sequelize` models, migrations, and associations
    * Prisma `ORM`: schema, client, and migrations
    * Connecting to `MongoDB` with Mongoose
    * Mongoose schemas, models, and queries
    * Database transactions and connection pooling
    * Choosing between `SQL` and `NoSQL` for different use cases
<!-- chapter: input-validation-file-uploads-and-websockets, duration: 2h -->
* Input Validation, `File` Uploads, and WebSockets
    * Input validation and sanitization strategies
    * `File` upload handling with Multer
    * Streaming large `file` uploads and downloads
    * Introduction to WebSockets with Socket.IO
    * Real-time communication patterns
    * Broadcasting and rooms
<!-- chapter: testing-node-js-applications, duration: 2h -->
* Testing `Node.js` Applications
    * Setting up `Jest` for `Node.js` testing
    * Unit testing services and utility functions
    * Integration testing with Supertest
    * Mocking databases and external services
    * Test fixtures and factories
    * Code coverage and testing strategies
<!-- chapter: logging-monitoring-and-error-handling, duration: 3h -->
* Logging, Monitoring, and Error Handling
    * Structured logging with Winston
    * High-performance logging with Pino
    * Log levels, transports, and log rotation
    * Centralized error handling patterns
    * Health `check` endpoints
    * Application monitoring and metrics
<!-- chapter: typescript-with-node-js, duration: 2h -->
* `TypeScript` with `Node.js`
    * Setting up `TypeScript` in a `Node.js` project
    * Configuring tsconfig.`json` for backend development
    * Typing Express request, response, and middleware
    * Using `TypeScript` with `ORMs` and database clients
    * Type-safe environment variables and configuration
<!-- chapter: security-deployment-and-production, duration: 4h -->
* Security, Deployment, and Production
    * `OWASP` `Node.js` security best practices
    * Preventing common vulnerabilities: injection, `XSS`, `CSRF`
    * Rate limiting and CORS configuration
    * Helmet and security headers
    * `Docker` containerization for `Node.js` applications
    * Process management with PM2
    * Cluster mode and scaling strategies
    * Environment configuration and secrets management
    * `CI/CD` pipeline considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
