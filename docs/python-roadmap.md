# Python Roadmap: JobRadar

## Handoff

The learner has used Python for about two years and wants to sharpen their skills through projects, not beginner exercises. They asked for a single path chosen for them. Nothing has been built yet; the next step is Phase 0.

Everything below this section is the roadmap exactly as it was given to the learner on 5 October 2026.

## Roadmap

I've built the roadmap around one project, **JobRadar**, a system that collects job postings, analyses them, serves them through an API and answers questions about them. Each phase builds on the previous one, so in about six months you'll have one deep, deployed portfolio piece instead of several disconnected exercises. It assumes **8–10 hours a week**; if you have more time, it compresses easily.

### Overview

| Phase | Weeks | You build | What it practises |
|---|---|---|---|
| 0. Setup | 1 | Project template with CI | Modern tooling |
| 1. Core | 2–4 | `jobradar` library + CLI | Advanced language features, typing, packaging |
| 2. Collect | 5–8 | Async ingester | `asyncio`, HTTP, resilience |
| 3. Pipeline | 9–12 | ETL into Postgres + dashboard | SQL, data wrangling, scheduling, Docker |
| 4. Serve | 13–17 | FastAPI service, deployed | API design, auth, caching, background jobs |
| 5. AI | 18–21 | Semantic search, RAG, matching | Embeddings, LLMs, evaluation |
| 6. Systems | 22–26 | Your own job queue, used in place of Celery/RQ | Concurrency, durability, internals |

### Phase 0: Setup (week 1)
- Set up `uv`, `ruff`, `mypy --strict`, `pytest`, `pre-commit` and a GitHub Actions workflow.
- **Done when:** an empty repo passes CI on every push. You'll reuse this template in every later phase.

### Phase 1: Core library and CLI (weeks 2–4)
- **Week 2:** domain models (`Job`, `Company`, `Salary`) using Pydantic, plus enums and parsing for salary ranges and locations.
- **Week 3:** utilities: a `@retry` decorator with backoff, a `timer` context manager, a config loader (env + TOML), and generators for streaming large files.
- **Week 4:** a `typer` CLI (`jobradar filter jobs.json --skill python --min-salary 80k`), packaged with `pyproject.toml` and published to TestPyPI.
- **Language features to cover:** decorators, context managers, generators, `Protocol`, generics, `match`.
- **Done when:** `pip install` works, `mypy` strict passes and test coverage is at least 90%.

### Phase 2: Async ingester (weeks 5–8)
- **Week 5:** a sync client for one public source, such as the HN "Who's Hiring" threads via the Algolia API, or the Remotive or Arbeitnow APIs.
- **Week 6:** rewrite it with `asyncio` + `httpx`, using a semaphore for rate limiting and your Phase 1 `@retry`.
- **Week 7:** add two or three sources behind a shared `Source` protocol, and store results in SQLite.
- **Week 8:** make runs resumable (checkpoints), deduplicate postings, and test with mocked HTTP using `respx`.
- **Done when:** it fetches 1,000+ postings concurrently, survives network failures and picks up where it stopped.

### Phase 3: Pipeline and dashboard (weeks 9–12)
- **Week 9:** move to Postgres in Docker Compose, using SQLAlchemy 2.0 and Alembic migrations.
- **Week 10:** transform the data with Polars: normalise salaries and currencies, extract skills, assign seniority levels.
- **Week 11:** schedule daily runs with Prefect or APScheduler, and make loads idempotent (running twice changes nothing).
- **Week 12:** build a Streamlit dashboard showing top skills over time, salary by skill, and remote vs on-site share.
- **Done when:** `docker compose up` brings up the whole stack and the data refreshes daily without you touching it.

### Phase 4: API service (weeks 13–17)
- **Week 13:** FastAPI endpoints for search, filtering and pagination, with Pydantic response models.
- **Week 14:** user accounts with JWT auth and saved searches.
- **Week 15:** alerts: when new postings match a saved search, notify the user on Telegram or by email (start with RQ or Celery).
- **Week 16:** Redis caching and integration tests with `testcontainers`.
- **Week 17:** deploy to Fly.io or Render, with structured logging and a health endpoint.
- **Done when:** the service has a public URL, OpenAPI docs, and CI that deploys after tests pass.

### Phase 5: AI layer (weeks 18–21)
- **Week 18:** generate embeddings for postings in `pgvector` and add a semantic search endpoint.
- **Week 19:** RAG: answer questions like "Which companies hiring Python devs in Europe pay over 90k?"
- **Week 20:** resume matching: upload a CV and get ranked matches with explanations.
- **Week 21:** write an evaluation set of 20+ questions with expected answers and measure accuracy. This step is what separates a demo from engineering.
- **Done when:** you have accuracy numbers in the README and a way to compare prompt or model changes against them.

### Phase 6: Systems project (weeks 22–26)
Build your own job queue and swap it in for RQ or Celery in the Phase 4 alerts.
- Workers using `multiprocessing`, retries with backoff, a dead-letter queue and visibility timeouts.
- Durability through an append-only log or a Postgres table using `SELECT … FOR UPDATE SKIP LOCKED`.
- Crash tests: kill a worker mid-job and show the job is never lost or run twice.
- **Done when:** production alerts run on your queue, and you've written up what you learned.

### Rules for the whole roadmap
- **Tests come with the feature, not afterwards.**
- **Each phase ends with a README section and a short write-up** (a blog post or LinkedIn post) of 300–500 words on what you learned.
- **Weekly rhythm:** about 70% building, 20% reading, 10% refactoring last week's code.
- **Reading alongside:** *Fluent Python* (2nd ed.) for Phases 1–2, *Architecture Patterns with Python* for Phases 3–4, and *Designing Data-Intensive Applications* chapters 3, 5 and 11 for Phase 6.

If you start this week, Phase 1 runs until about **late October**, the API should be deployed around **early February**, and the whole roadmap would finish around **early April 2027**.

I can turn Phase 0 and Phase 1 into a day-by-day checklist, or set up the starter template repo now.
