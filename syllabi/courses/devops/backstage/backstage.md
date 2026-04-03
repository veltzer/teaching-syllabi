---
tags:
  - tools:backstage
  - practices:devops
  - concepts:architecture
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: backstage -->
# Backstage

## Description
This course covers Backstage, the open-source developer portal platform originally created
by Spotify. Participants will learn how to set up, customize, and extend Backstage to create
an internal developer portal that unifies software catalog management, documentation,
software templates, and integrations with infrastructure and `CI/CD` systems. The course
includes building custom plugins and deploying Backstage in production environments.

## Duration
16 hours / 2 days

## Intended Audience
* developers who want to build or contribute to an internal developer portal.
* `devops` engineers responsible for developer experience and platform tooling.
* platform engineers designing self-service developer platforms.

## Prerequisites
* experience with `TypeScript` and `React`.
* familiarity with `Node.js` and `npm`/`yarn`.
* basic understanding of `Kubernetes` and `CI/CD` concepts.

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)
* `React` (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* understand Backstage architecture and its role as a developer portal.
* configure and manage the software catalog.
* create software templates for scaffolding new projects.
* build custom plugins to extend Backstage functionality.
* deploy and maintain Backstage in production.

## Outline
<!-- chapter: developer-portal-concepts, duration: 1h -->
* Developer portal concepts
    * what is a developer portal
    * developer experience and productivity
    * internal developer platforms
    * Backstage history and community
<!-- chapter: backstage-architecture, duration: 1h -->
* Backstage architecture
    * app frontend
    * backend services
    * plugin system
    * database and storage
    * configuration system
<!-- chapter: software-catalog, duration: 1h -->
* Software catalog
    * entities and kinds (components, APIs, systems, domains)
    * catalog `YAML` format
    * entity relationships and dependencies
    * catalog ingestion and discovery
    * entity providers and processors
<!-- chapter: software-templates-scaffolder, duration: 1h -->
* Software templates (scaffolder)
    * template `YAML` structure
    * input parameters and forms
    * template actions (fetch, publish, register)
    * custom template actions
    * self-service project creation
<!-- chapter: techdocs-documentation-as-code, duration: 1h -->
* TechDocs (documentation as code)
    * MkDocs integration
    * documentation alongside code
    * publishing and storage backends
    * search integration
<!-- chapter: search, duration: 1h -->
* Search
    * search architecture
    * search engines and collators
    * customizing search results
    * indexing strategies
<!-- chapter: backstage-plugins, duration: 1h -->
* Backstage plugins
    * core plugins overview
    * community plugins
    * plugin marketplace
    * installing and configuring plugins
<!-- chapter: creating-custom-plugins, duration: 2h -->
* Creating custom plugins
    * plugin development setup
    * frontend plugins with `React`
    * backend plugins
    * plugin APIs and services
    * publishing and sharing plugins
<!-- chapter: api-integration, duration: 1h -->
* `API` integration
    * `API` catalog and documentation
    * `OpenAPI` and `gRPC` support
    * `API` lifecycle management
    * connecting external APIs
<!-- chapter: authentication-and-authorization, duration: 1h -->
* Authentication and authorization
    * identity providers (`OAuth`, `OIDC`)
    * guest access and user management
    * permission framework
    * role-based access control
<!-- chapter: kubernetes-plugin, duration: 1h -->
* `Kubernetes` plugin
    * viewing `Kubernetes` resources
    * cluster configuration
    * workload monitoring
    * multi-cluster support
<!-- chapter: ci-cd-plugin, duration: 1h -->
* `CI/CD` plugin
    * build status integration
    * `GitHub Actions`, `GitLab CI`, `Jenkins` plugins
    * deployment tracking
    * pipeline visibility
<!-- chapter: cost-insights, duration: 1h -->
* Cost insights
    * cost tracking and visualization
    * cloud cost integration
    * cost allocation by team and project
<!-- chapter: deployment, duration: 1h -->
* Deployment
    * `Docker` deployment
    * `Kubernetes` deployment
    * database setup and migrations
    * scaling considerations
<!-- chapter: customization-and-theming, duration: 1h -->
* Customization and theming
    * custom themes and branding
    * homepage customization
    * custom sidebar and navigation
    * extending the UI

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
