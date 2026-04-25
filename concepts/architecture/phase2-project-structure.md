---
tags: [architecture, backend, fastapi, neurospect, journal, analytics]
aliases: [Phase 2 Project Structure, neurospect-api Layout]
sources: [processes/distributed-workflow/active/journal-analytics.md]
created: 2026-04-22
updated: 2026-04-23
---

# Phase 2 — Backend Project Structure (APPROVED)

Canonical reference for the `neurospect-api` backend layout. This document captures the approved design from the Phase 2 planning session. Implementation sessions read this instead of re-planning.

## Repository

`C:\Users\PaulRussell\repos\neurospect-api` — empty git repo, building from scratch.

## Stack

| Component | Choice | Notes |
|---|---|---|
| Framework | FastAPI 0.115+ | Async-native, OpenAPI auto-docs |
| ORM | SQLAlchemy 2.0 async | `asyncpg` driver at runtime |
| Migrations | Alembic | Sync `psycopg2` connection for migration runner |
| Database | Postgres (Render managed) | |
| Screenshot storage | Cloudflare R2 | boto3 S3-compatible client |
| Auth | Discord OAuth2 + JWT | python-jose for token signing |
| HTTP client | httpx | Discord API calls |
| Package manager | Poetry | `pyproject.toml` |

## Directory Layout

```
neurospect-api/
├── pyproject.toml           # Poetry — deps + metadata
├── .env.example             # Env var template (no real values)
├── .gitignore
├── alembic.ini
├── alembic/
│   ├── env.py               # Sync Alembic env (psycopg2, not asyncpg)
│   └── versions/
│       ├── 0001_initial.py  # 11 ENUMs, 3 tables, 7 indexes, triggers
│       └── 0002_coach_tables.py  # coaching_event_status ENUM, tradingview_tokens, coaching_events
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, router mounts, lifespan
│   ├── config.py            # pydantic-settings — all env vars
│   ├── database.py          # Async engine + AsyncSessionLocal factory
│   ├── deps.py              # get_db() + get_current_user() dependencies
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── discord.py       # exchange_code(), get_discord_user() via httpx
│   │   ├── jwt.py           # create_access_token(), verify_token()
│   │   └── router.py        # POST /auth/discord/token, GET /auth/me, POST /auth/debug/token
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py          # SQLAlchemy DeclarativeBase
│   │   ├── enums.py         # Python Enum mirrors of all 12 Postgres ENUMs
│   │   ├── user.py          # User ORM model
│   │   ├── trade.py         # Trade ORM model (all columns from DDL)
│   │   ├── screenshot.py    # TradeScreenshot ORM model
│   │   ├── tv_token.py      # TradingViewToken ORM model
│   │   └── coaching_event.py # CoachingEvent ORM model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── trade.py         # TradeCreate, TradeUpdate, TradeResponse, TradeListResponse
│   │   ├── screenshot.py    # ScreenshotResponse (includes presigned URL)
│   │   ├── analytics.py     # One response model per analytics endpoint
│   │   └── coach.py         # Layer2Payload, Layer3Response, WebhookAccepted, CoachingEventResponse, TvTokenResponse
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── trades.py        # 5 CRUD endpoints
│   │   ├── screenshots.py   # 3 screenshot endpoints
│   │   ├── analytics.py     # 7 analytics endpoints
│   │   └── tv_tokens.py     # Per-user TradingView webhook token CRUD
│   ├── services/
│   │   ├── __init__.py
│   │   ├── r2.py            # R2Client: upload_bytes(), delete(), presign()
│   │   └── analytics.py     # Raw SQL analytics queries
│   └── coach/
│       ├── __init__.py
│       ├── router.py        # Webhook ingestion + events polling (full implementation)
│       ├── claude_client.py  # Claude API call orchestration (BackgroundTask)
│       ├── prompt_loader.py  # System prompt assembly from wiki files
│       └── validation.py     # Webhook secret + IP allowlist checks
├── tests/
│   ├── __init__.py
│   ├── test_coach_pine_payload.py   # Layer2Payload parsing regression tests
│   ├── test_coach_prompt_loader.py  # Prompt assembly + error cases
│   └── test_coach_validation.py     # Secret + IP allowlist tests
```

## Dependencies

```toml
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.115"
uvicorn = {extras = ["standard"], version = "^0.34"}
sqlalchemy = {extras = ["asyncio"], version = "^2.0"}
asyncpg = "^0.30"
alembic = "^1.14"
pydantic-settings = "^2.7"
httpx = "^0.28"
python-jose = {extras = ["cryptography"], version = "^3.3"}
python-multipart = "^0.0.20"
boto3 = "^1.37"
psycopg2-binary = "^2.9"
anthropic = "^0.40"
```

## Auth Design

SPA pattern — backend is a pure API, no server-side redirects.

1. Frontend redirects user to Discord OAuth2 authorization URL
2. Discord redirects back to the **frontend** with `?code=...`
3. Frontend POSTs `{code, redirect_uri}` to `POST /auth/discord/token`
4. Backend exchanges code for Discord user info via Discord API
5. Backend upserts `users` row (keyed on `discord_id`)
6. Backend returns `{access_token, token_type: "bearer"}` JWT
7. All subsequent requests use `Authorization: Bearer <jwt>`

`get_current_user()` FastAPI dependency: decodes JWT → queries `users` table → injects `User` ORM object into route handler.

**Debug endpoint:** `POST /auth/debug/token {discord_id}` — mints JWT without OAuth, gated on `settings.debug == true`. Never deployed to prod.

## Alembic Migrations

### `0001_initial.py`

1. `CREATE OR REPLACE FUNCTION update_updated_at()` trigger function
2. 11 `CREATE TYPE ... AS ENUM` (via `op.execute()`) — all journal ENUMs
3. `CREATE TABLE users` + `BEFORE UPDATE` trigger
4. `CREATE TABLE trades` + `BEFORE UPDATE` trigger
5. `CREATE TABLE trade_screenshots`
6. All 7 indexes

Downgrade reverses in opposite order: indexes → tables → ENUMs → trigger function.

### `0002_coach_tables.py`

1. `CREATE TYPE coaching_event_status AS ENUM` (12th ENUM overall)
2. `CREATE TABLE tradingview_tokens` + partial indexes (`ix_tv_tokens_token`, `uq_tv_tokens_user_active`)
3. `CREATE TABLE coaching_events` + composite unique constraint (`user_id`, `idempotency_key`) + index

**Alembic env note:** Uses `DATABASE_URL_SYNC` (postgresql+psycopg2) — separate from the runtime `DATABASE_URL` (postgresql+asyncpg). Both point to the same DB; different drivers for sync vs async use.

## Analytics SQL Approach

ORM for CRUD, raw `text()` SQL for all 7 analytics endpoints (in `services/analytics.py`).

| Endpoint | SQL pattern |
|---|---|
| `/summary` | Aggregate counts + CTE streak window function |
| `/by-setup`, `/by-session`, `/by-instrument` | `GROUP BY <field>` |
| `/by-day-of-week` | `GROUP BY EXTRACT(DOW FROM trade_date)` |
| `/mistakes` | `SELECT unnest(mistake_tags) as tag, COUNT(*) GROUP BY tag` |
| `/r-distribution` | `WIDTH_BUCKET(r_multiple, -10, 10, 40)` — 40 bins |

Streak query: ROW_NUMBER difference method over `ORDER BY trade_date DESC WHERE status = 'closed'`.

All analytics filter: `WHERE user_id = :user_id AND NOT is_deleted AND outcome IS NOT NULL`.

## R2 Client

```python
boto3.client(
    "s3",
    endpoint_url=settings.r2_endpoint_url,
    aws_access_key_id=settings.r2_access_key_id,
    aws_secret_access_key=settings.r2_secret_access_key,
    region_name="auto",
)
```

Storage key pattern: `{user_id}/{trade_id}/{phase}/{uuid4()}.{ext}`

Methods: `upload_bytes(key, data, content_type)`, `delete(key)`, `presign(key, expires=3600)`.

## Env Vars

```
DATABASE_URL=postgresql+asyncpg://user:pass@host/neurospect
DATABASE_URL_SYNC=postgresql+psycopg2://user:pass@host/neurospect
JWT_SECRET=changeme
JWT_EXPIRE_MINUTES=43200
DISCORD_CLIENT_ID=
DISCORD_CLIENT_SECRET=
R2_ENDPOINT_URL=https://<account>.r2.cloudflarestorage.com
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=
R2_BUCKET=neurospect-screenshots
DEBUG=false
```

## File Creation Order

1. `pyproject.toml`, `.gitignore`, `.env.example`
2. `alembic.ini`, `alembic/env.py`
3. `app/config.py`, `app/database.py`
4. `app/models/` (base → enums → user → trade → screenshot → tv_token → coaching_event)
5. `alembic/versions/0001_initial.py`
6. `alembic/versions/0002_coach_tables.py`
7. `app/schemas/` (trade → screenshot → analytics → coach)
8. `app/services/` (r2 → analytics)
9. `app/auth/` (jwt → discord → router)
10. `app/deps.py`
11. `app/routers/` (trades → screenshots → analytics → tv_tokens)
12. `app/coach/` (validation → prompt_loader → claude_client → router)
13. `app/main.py`
14. `tests/` (test_coach_pine_payload → test_coach_prompt_loader → test_coach_validation)

## Verification Checklist

After implementation:
1. `poetry install` — no errors
2. `cp .env.example .env` + fill test DB URL + dummy secrets + `DEBUG=true`
3. `alembic upgrade head` — 0001 (11 ENUMs + 3 tables + 7 indexes) + 0002 (1 ENUM + 2 tables + 3 indexes)
4. `uvicorn app.main:app --reload` — server starts, `/docs` loads
5. Hit `POST /auth/debug/token` (DEBUG=true) → get JWT
6. **Journal flow:** create trade → PATCH to add entry fields → PATCH to close → list analytics
7. **Coach flow:** `POST /api/coach/tv-token` → get webhook URL → POST to webhook with Layer2 payload → poll `GET /api/coach/events/latest`
8. `pytest` — all unit tests pass (coach validation, prompt loader, Pine payload parsing)

## See Also

- [[concepts/architecture/trade-schema]] — canonical DDL and API spec (the source of truth)
- [[processes/distributed-workflow/active/journal-analytics]] — workstream tracker
- [[processes/distributed-workflow/active/ai-coach]] — shares this backend (coach router stub in Phase 2)
