# Intermediate Python Project Ideas

A curated list of intermediate-level projects that touch multiple architectures, packages, and Python built-ins. Pick one to explore many patterns and systems.

## Personal Finance Manager
- What: Full-stack app (CLI + web UI + REST API) to track income, budgets, investments, and reports.
- Tech: FastAPI, SQLAlchemy, Alembic, asyncio, httpx, Jinja2, click, pytest
- Key features: import CSV/bank feeds, reconciliation, scheduled jobs, role-based auth, export/visualizations
- Learning: async IO, ORMs/migrations, background scheduling, testing, CLI + web integration

## Job Aggregator & Normalizer
- What: Aggregates job listings from web APIs and scrapers, normalizes data, exposes search API.
- Tech: requests/httpx, BeautifulSoup or Playwright, pydantic, Elasticsearch or SQLite, celery/dramatiq, pytest
- Key features: scrapers, deduplication, canonical model, worker queue, full-text search, rate-limiting
- Learning: parsing, validation, queues, retry/backoff, search indexing, data normalization

## Plugin-based Static Site Generator
- What: Markdown → HTML generator with plugin system, dev server and themes.
- Tech: markdown, watchdog, Jinja2, plugin API (entry points), Typer/click, unittest
- Key features: CLI, incremental builds, plugin hooks, templating, asset pipeline
- Learning: packaging, plugin architecture, filesystems, watchers, CLI UX

## Microservice E‑commerce (mini)
- What: Multiple services (catalog, orders, payments, auth) communicating over HTTP/gRPC and async tasks.
- Tech: FastAPI, gRPC/protobuf, Redis, Postgres, Docker, pytest, pydantic
- Key features: service boundaries, centralized auth, background order processing, idempotency, integration tests
- Learning: service decomposition, contracts, containerization, CI, testing across services

## Data Pipeline / ETL Framework
- What: Build connectors, transformations, and sinks with a pluggable pipeline definition (batch + streaming).
- Tech: pandas, asyncio, kafka or mq, sqlalchemy, click, observability libs
- Key features: connector plugins, schema evolution, checkpointing, retries, monitoring
- Learning: streaming vs batch, backpressure, data validation, observability, robust error handling

## ML Model Serving + Registry
- What: Model registry, versioning, REST inference endpoint, batch/online inference, metrics.
- Tech: FastAPI, pydantic, docker, protobuf/ONNX, prometheus, sqlalchemy
- Key features: upload/register models, A/B rollout, concurrency controls, latency metrics
- Learning: deployment patterns, serialization, performance tuning, CI/CD, feature flags

## Workflow Automation Engine
- What: Define workflows in YAML/DSL and execute tasks with retries, concurrency, and dependencies.
- Tech: asyncio, concurrent.futures, pyyaml, plugin task runners, sqlite or redis for state
- Key features: DAGs, retry policies, monitoring UI, pluggable task types, persistence
- Learning: scheduling, concurrency, state persistence, DSL parsing, error semantics

## Telemetry / IoT Ingest Platform
- What: Ingest telemetry over MQTT/HTTP, process and store time-series, real-time query + alerting.
- Tech: paho-mqtt, asyncio, influxdb or timescaledb, websockets, prometheus
- Key features: device auth, backfilling, aggregation, alert rules, dashboard
- Learning: network programming, streaming ingestion, time-series storage, scaling concerns

## Code Analysis / Linter with AST Plugins
- What: Custom linter/transform tool that uses AST to find/auto-fix patterns and supports plugins.
- Tech: ast, parso/lib2to3, astor, black integration, packaging entry points
- Key features: rule engine, autofix, CLI, editor integration (LSP optional), test suite for rules
- Learning: AST manipulation, static analysis, packaging plugins, editor tooling

## Realtime Collaborative Editor (toy)
- What: Minimal collaborative text editor backend with websockets, OT/CRDT basics, client demo.
- Tech: FastAPI/Starlette websockets, uvicorn, basic CRDT lib or custom, sqlite for snapshots
- Key features: presence, change sync, conflict resolution, persistence, simple front-end demo
- Learning: real-time protocols, concurrency, data structures (CRDT/OT), websockets, consistency trade-offs

---

Would you like one of these expanded into a starter scaffold (project layout, requirements, and initial files)?
