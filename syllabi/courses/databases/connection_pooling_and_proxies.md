---
tags:
  - concepts:databases
  - concepts:performance
  - concepts:scalability
  - concepts:operations
  - concepts:best-practices
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:dbas
  - audiences:devops
  - audiences:developers
---
<!-- course: connection_pooling_and_proxies -->
# Connection Pooling and Database Proxies

## Description
Connection management is the most under-engineered part of most database integrations. The catalog
covers the database tier and the application tier; it does not cover the layer between them, where
connections are pooled, multiplexed, routed, and rate-limited. A bad connection-pool configuration is
one of the most common root causes of production outages: connections starve, the database hits its
`max_connections`, the application waits forever, and a small spike turns into a full incident.

This two day course covers connection pooling and database proxies as a focused engineering topic. It
covers the per-database connection model (how `Postgres` and `MySQL` actually handle connections, and
why both can and do collapse under high connection counts), client-side pools (`HikariCP`, `pgx`,
`SQLAlchemy`'s pool, `Node.js` pools), proxy-side pools (`PgBouncer`, pgcat, `pgpool-II`,
`ProxySQL`, `RDS Proxy`, `Cloud SQL Auth Proxy`), the transaction-pooling vs session-pooling vs
statement-pooling distinction and what breaks at each level, the wait-pile-up failure mode, the
right-sizing methodology, observability of pools, and the patterns that `make` connection management
boring instead of hostile. Examples cover `Postgres` and `MySQL` primarily. Participants leave able to
size and operate a connection-management layer that does not collapse under load.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers configuring connection pools
* `DBAs` and `DevOps` running database proxies
* developers debugging "why is the app slow" incidents
* engineers operating a serverless application against a relational database

## Prerequisites
* working experience with at least one relational database
* basic familiarity with database concepts
* exposure to the Database Internals course is helpful

## Objectives
* explain why `Postgres` and `MySQL` connections are expensive
* configure a client-side connection pool correctly
* deploy and operate `PgBouncer` or `RDS Proxy`
* choose between transaction, session, and statement pooling
* recognize the wait-pile-up failure mode
* observe and alert on pool health
* serve a serverless workload against a relational database

## Outline
<!-- chapter: why-connections-are-expensive, duration: 2h -->
* Why connections are expensive
    * `Postgres`: one process per connection
    * `MySQL`: one thread per connection (and the cost)
    * the per-connection memory cost
    * the `max_connections` ceiling
    * cross-reference to the `Postgres` and `MySQL` courses
<!-- chapter: client-side-pooling, duration: 2h -->
* Client-side pooling
    * `HikariCP` for the `JVM`
    * `pgx` and `database/sql` for Go
    * `SQLAlchemy` pool for `Python`
    * `node-postgres` for `Node.js`
    * the per-instance pool size question
<!-- chapter: the-pool-saturation-failure, duration: 2h -->
* The pool saturation failure
    * the canonical incident: pool exhausted
    * the request waiting for a connection
    * the timeout that turns into a `500`
    * the cascade: every request is now waiting
    * the "we set the pool too small" reality
<!-- chapter: proxy-side-pooling-pgbouncer, duration: 3h -->
* Proxy-side pooling: `PgBouncer`
    * what `PgBouncer` is
    * pool modes: session, transaction, statement
    * what each pool mode breaks (prepared statements, advisory locks, `LISTEN/NOTIFY`)
    * `PgBouncer` configuration
    * the deployment topology
<!-- chapter: rds-proxy-and-cloud-sql-proxy, duration: 1h -->
* `RDS Proxy` and `Cloud SQL` Proxy
    * `RDS Proxy` for Postgres and `MySQL`
    * `Cloud SQL Auth Proxy`
    * the managed-proxy value proposition
    * the cost-and-latency overhead
    * when each is the right answer
<!-- chapter: proxysql-and-mysql, duration: 1h -->
* `ProxySQL` and `MySQL`
    * `ProxySQL` features
    * read/write splitting
    * query routing
    * the configuration model
    * the deployment topology
<!-- chapter: pgcat-and-modern-postgres-proxies, duration: 1h -->
* `pgcat` and modern `Postgres` proxies
    * `pgcat` as the modern Rust alternative
    * `Supabase`'s `Supavisor`
    * the read replica routing question
    * the per-tenant routing question
    * picking
<!-- chapter: serverless-and-pooling, duration: 2h -->
* Serverless and pooling
    * the canonical problem: every `Lambda` creates a connection
    * the `RDS Proxy` answer
    * the `Aurora Serverless v2` story
    * the `Neon` and `pgbouncer` story
    * the "we melted the database with `Lambda`" failure
<!-- chapter: pool-observability, duration: 1h -->
* Pool observability
    * pool size, in-use, waiting
    * the wait-time histogram
    * the connection-acquire latency
    * cross-reference to the Database Observability course
    * the alerts that page
<!-- chapter: right-sizing-methodology, duration: 1h -->
* Right-sizing methodology
    * the `(cores * 2) + spindles` rule and its limits
    * the workload-driven approach
    * the "we set 100 because the docs said so" anti-pattern
    * the load-test approach
    * iterating

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
