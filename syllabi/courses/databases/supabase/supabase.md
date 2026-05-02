---
tags:
  - tools:supabase
  - tools:postgresql
  - concepts:web-development
level: beginner
category: database
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: supabase -->
# Supabase: The Open-Source Firebase Alternative

## Description
This course introduces Supabase, an open-source backend-as-a-service platform built on top of `PostgreSQL`. Participants will learn how to use Supabase for database management, authentication, real-time subscriptions, file storage, and edge functions. The course covers both the hosted platform and self-hosted options, giving developers the skills to build full-stack applications rapidly.

## Duration
16 hours / 2 days

## Intended Audience
* Full-stack developers building web and mobile applications
* Frontend developers looking for a managed backend solution
* Developers migrating from Firebase to an open-source alternative

## Prerequisites
* Basic understanding of relational databases and `SQL`.
* Familiarity with `JavaScript` or `Python`.
* Basic knowledge of web development concepts (`REST` APIs, authentication).

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand the Supabase architecture and its `PostgreSQL` foundation.
* Design and manage database schemas, tables, and migrations.
* Implement authentication with email, `OAuth`, and magic links.
* Secure data access using Row Level Security (RLS).
* Build real-time features using Supabase subscriptions.
* Use Supabase storage for file uploads and management.
* Deploy edge functions for serverless backend logic.
* Integrate Supabase with client applications using official libraries.

## Outline
<!-- chapter: introduction-to-supabase, duration: 1h -->
* Introduction to Supabase:
    * What is Supabase and how it compares to Firebase
    * Architecture overview
    * `PostgreSQL` as the core database
    * Supabase dashboard tour
<!-- chapter: database-management, duration: 2h -->
* Database Management:
    * Creating tables and schemas
    * Data types and constraints
    * Relationships and foreign keys
    * Database migrations
    * `SQL` editor in the dashboard
<!-- chapter: postgrest-api, duration: 1h -->
* PostgREST `API`:
    * Auto-generated RESTful `API`
    * Filtering, sorting, and pagination
    * Embedded resources and joins
    * RPC (Remote Procedure Call) for custom functions
<!-- chapter: row-level-security-rls, duration: 1h -->
* Row Level Security (RLS):
    * Understanding RLS concepts
    * Creating security policies
    * Policies for different operations (SELECT, INSERT, UPDATE, DELETE)
    * Testing and debugging RLS policies
<!-- chapter: authentication, duration: 2h -->
* Authentication:
    * Email and password authentication
    * `OAuth` providers (Google, `GitHub`, Apple, etc.)
    * Magic link authentication
    * User management and profiles
    * Session handling and JWTs
<!-- chapter: real-time-subscriptions, duration: 1h -->
* Real-Time Subscriptions:
    * Supabase Realtime architecture
    * Subscribing to database changes
    * Broadcast and presence channels
    * Building real-time features
<!-- chapter: storage, duration: 2h -->
* Storage:
    * Storage buckets and objects
    * `File` uploads and downloads
    * Access control for storage
    * Image transformations
    * Resumable uploads
<!-- chapter: edge-functions, duration: 2h -->
* Edge Functions:
    * Introduction to Supabase Edge Functions
    * Writing functions in `TypeScript`/Deno
    * Deploying and invoking edge functions
    * Connecting edge functions to the database
    * Use cases for edge functions
<!-- chapter: client-libraries, duration: 1h -->
* Client Libraries:
    * `JavaScript`/`TypeScript` client (supabase-js)
    * `Python` client
    * `Flutter`/Dart client
    * Client configuration and best practices
<!-- chapter: supabase-cli-and-local-development, duration: 1h -->
* Supabase `CLI` and Local Development:
    * Installing and configuring the Supabase `CLI`
    * Local development environment
    * Database migrations with the `CLI`
    * Testing locally before deployment
<!-- chapter: deployment-pricing-and-scaling, duration: 2h -->
* Deployment, Pricing, and Scaling:
    * Supabase hosting plans
    * Self-hosting Supabase
    * Scaling considerations
    * Connection pooling with `PgBouncer`
    * Monitoring and logging

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
