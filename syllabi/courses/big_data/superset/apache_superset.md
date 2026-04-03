---
tags:
  - tools:superset
  - data-and-ai:data-analysis
  - practices:monitoring
level: beginner
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:managers
  - audiences:devops
---
<!-- course: apache_superset -->
# `Apache` Superset

## Description
`Apache Superset` is a modern, open-source data exploration and visualization platform. This course covers installation, configuration, connecting to various databases, building charts and dashboards, using `SQL Lab`, configuring security, and deploying Superset at scale. Participants will learn to create compelling data visualizations and share insights across their organization.

## Duration
16 hours / 2 days

## Intended Audience
* Data analysts and business intelligence professionals
* Data engineers building self-service analytics platforms
* Software developers creating data-driven applications
* Data scientists sharing results and visualizations
* Managers and decision-makers consuming data dashboards
* `DevOps` engineers deploying and maintaining Superset

## Prerequisites
* Basic knowledge of `SQL`
* Understanding of relational database concepts
* Familiarity with web browsers and web application usage
* Basic understanding of data visualization principles
* Optional: experience with `Docker` for deployment topics

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* Install and configure `Apache Superset` for development and production
* Connect Superset to various databases (`PostgreSQL`, `MySQL`, ClickHouse, `BigQuery`, `Snowflake`)
* Write and execute queries in `SQL Lab`
* Create a variety of chart types (line, bar, pie, scatter, heatmap, geo)
* Build interactive dashboards with filters and cross-filtering
* Configure alerts and scheduled reports
* Set up role-based access control and row-level security
* Use Jinja templating for dynamic `SQL` queries
* Deploy Superset with `Docker` and `Kubernetes`

## Outline
<!-- chapter: apache-superset-overview, duration: 1h -->
* `Apache Superset` Overview
    * What is `Apache Superset` and its history
    * Architecture: web server, metadata database, cache, and workers
    * Feature overview and use cases
    * Comparison with `Grafana`, Metabase, and Tableau
    * Community and ecosystem
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installing Superset with `pip` and `Docker`
    * Configuration `file` (superset_config.py) essentials
    * Setting up metadata database (`PostgreSQL` recommended)
    * Cache configuration (`Redis`, Memcached)
    * Feature flags and customization options
<!-- chapter: connecting-to-databases, duration: 1h -->
* Connecting to Databases
    * Database connection setup via SQLAlchemy URIs
    * Connecting to `PostgreSQL` and `MySQL`
    * Connecting to ClickHouse for analytics workloads
    * Connecting to `BigQuery` and `Snowflake`
    * Managing database credentials securely
    * Testing connections and troubleshooting
<!-- chapter: sql-lab, duration: 1h -->
* `SQL Lab`
    * Writing and executing `SQL` queries
    * Query history and saved queries
    * Exploring table schemas and metadata
    * Exporting query results
    * Templated queries with Jinja
    * Query cost estimation
<!-- chapter: creating-charts, duration: 2h -->
* Creating Charts
    * Dataset creation from tables and `SQL` queries
    * Line and area charts for time series
    * Bar charts and histograms
    * Pie and donut charts
    * Scatter plots and bubble charts
    * Heatmaps and pivot tables
    * Geographic visualizations (deck.gl maps)
    * Chart configuration options and formatting
<!-- chapter: dashboards, duration: 2h -->
* Dashboards
    * Creating and laying out dashboards
    * Adding charts and `markdown` components
    * Dashboard tabs and sections
    * Dynamic dashboard titles and descriptions
    * Sharing and publishing dashboards
    * Dashboard refresh and auto-refresh settings
<!-- chapter: filters, duration: 1h -->
* Filters
    * Native filter configuration
    * Cross-filter interactions between charts
    * Filter scoping and dependencies
    * Time range filters and time grains
    * Pre-filtering datasets
<!-- chapter: alerts-and-reports, duration: 1h -->
* Alerts and Reports
    * Setting up email and `Slack` notifications
    * Configuring alert conditions on queries
    * Scheduled report delivery (`PDF`, PNG, `CSV`)
    * Celery worker configuration for `async` tasks
<!-- chapter: rbac-and-row-level-security, duration: 1h -->
* `RBAC` and Row-Level Security
    * Role-based access control model
    * Built-in roles and custom role creation
    * Dataset-level and dashboard-level permissions
    * Row-level security policies and filters
    * Ownership and access request workflows
<!-- chapter: jinja-templating-in-sql, duration: 1h -->
* Jinja Templating in `SQL`
    * Template syntax and available variables
    * User context and time macros
    * Dynamic filters and parameterized queries
    * Caching considerations with templates
<!-- chapter: custom-visualizations, duration: 1h -->
* Custom Visualizations
    * Visualization plugin architecture
    * Installing community plugins
    * Building custom visualization plugins with `React`
    * Registering and deploying custom plugins
<!-- chapter: embedding-dashboards, duration: 1h -->
* Embedding Dashboards
    * Embedded dashboard configuration
    * Guest token authentication for embedded access
    * Iframe embedding and CORS configuration
    * White-labeling and customization options
<!-- chapter: deployment, duration: 1h -->
* Deployment
    * `Docker Compose` deployment for small teams
    * `Kubernetes` deployment with `Helm` charts
    * Scaling Superset components (web, worker, scheduler)
    * Load balancer and reverse proxy configuration
    * Backup and disaster recovery
<!-- chapter: performance-tuning, duration: 1h -->
* Performance Tuning
    * Caching strategies (query cache, dashboard cache, data cache)
    * `Async` query execution for long-running queries
    * Database connection pooling
    * Optimizing chart rendering and dashboard load times
    * Monitoring Superset performance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
