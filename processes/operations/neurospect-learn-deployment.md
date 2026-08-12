---
tags: [process, operations, neurospect, deployment, render, cloudflare, r2, neurospect-learn]
aliases: [Learn Deployment, neurospect-learn Deploy, B3 Runbook]
sources: []
created: 2026-08-11
updated: 2026-08-11
---

# neurospect-learn — Deployment Runbook

How to put `neurospect-learn` (the learning platform: `api/` + `app/`) somewhere that is not Paul's
laptop, and how to prove it actually works once it is there. Written for Phase **B3** of
[[processes/distributed-workflow/active/backtest-companion]], which named deployment — not any
integration — as the binding constraint on the whole platform.

This is **adapted from**, not a replay of,
[[processes/distributed-workflow/active/deployment]] (the `neurospect-api` / `neurospect-app` pair,
live since 2026-04-25). §Differences records every place the two diverge and why. Where this page and
that one disagree about `neurospect-learn`, **this page wins**; where they disagree about
`neurospect-api`, that one does.

> **Code is ground truth.** Every claim below was checked against the repo on 2026-08-11, and the
> facts that were *measured* rather than assumed are marked `MEASURED`.

## Topology

```
GitHub (russell94paul/neurospect-learn, PRIVATE — one repo, two packages)
   │  push to main
   ├── rootDir: api ──▶ Render Web Service  ──DATABASE_URL──▶  Render Postgres 16
   │                    (FastAPI, uvicorn, 1 worker)            (basic-256mb, frankfurt)
   │                          │
   │                          └── R2_* ──▶ Cloudflare R2 bucket (evidence blobs)
   │
   └── root dir: app ──▶ Cloudflare Pages (React 19 SPA)
                              │
                              └── Discord OAuth ──▶ /auth/callback ──▶ POST /auth/discord/token
```

The **wiki is not part of the deployment.** `MEASURED`: only `scripts/` read
`settings.wiki_content_root` (`ingest_content.py`, `seed_drills.py`, `seed_rubrics.py`) — no router
and no service does. The deployed API therefore needs no wiki checkout, and the course corpus reaches
production by running the seed scripts **from Paul's laptop against the production database**
(§5). That keeps rubrics wiki-projected and read-only, exactly as the E3 invariant requires, and
keeps the mentor-derived corpus out of the deployed artifact.

## Cost

| Item | Plan | Note |
|---|---|---|
| Render web service | `starter` | Chosen 2026-08-11. `free` spins down after 15 min idle (~50s cold start). |
| Render Postgres | `basic-256mb` | **There is no permanent free Postgres** — free instances expire after ~30 days. |
| Cloudflare Pages | Free | |
| Cloudflare R2 | Free tier | 10 GB storage; chart captures are far below it. |

## Before you start

- **Use a personal account, not a company one**, for Cloudflare and Render. Paul's constraint,
  2026-08-11. Nothing in this runbook requires a company identity.
- **Credentials rule (Paul's global rule, and it applies to this page):** never paste a secret into
  chat, a commit, a log or this wiki. Values live only in the Render dashboard and the Cloudflare
  dashboard. This page names secrets; it never carries them.
- **Paul handles git.** A session may prepare files; it does not commit or push them.

---

## 1. Cloudflare R2 — the evidence bucket (do this FIRST)

⚠ **R2 is not optional on a deployed instance, and this is the single most important line on the
page.** `api/app/services/storage.py` falls back to `LocalBackend`, which writes chart captures to
the container filesystem. Render's filesystem is **ephemeral**: every deploy would delete every
stored capture *while the `evidence_assets` rows survived*, leaving reps derived from evidence that
no longer exists — and **nothing would raise an error**. E2's whole claim is that evidence is the only
thing that can mint a rep. Deploying on the local backend quietly voids it.

1. Sign in to Cloudflare with the **personal** account → **R2 Object Storage** → enable it (card
   required even on the free tier).
2. **Create bucket** → name `neurospect-learn-evidence` → location hint: **EU** (matches the
   `frankfurt` Render region and keeps the captures in-region).
3. **R2 → API → Manage API Tokens → Create API Token**:
   - Permission **Object Read & Write**
   - Scope it to **this bucket only** — not "all buckets"
   - Create, then copy the three values straight into a password manager: **Access Key ID**,
     **Secret Access Key**, and the **S3 endpoint** (`https://<accountid>.r2.cloudflarestorage.com`).
     The secret is shown **once**.

These become `R2_BUCKET`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_ENDPOINT_URL` in §3.
Setting `R2_ENDPOINT_URL` is what switches the backend over — it is a config flip, not a code change.

## 2. Discord — one redirect URI

The learn app reuses the existing Discord application; it only needs its own redirect URI.

1. <https://discord.com/developers/applications> → the **Neurospect** application → **OAuth2**.
2. Under **Redirects**, add — leaving the existing `neurospect-app` entries alone:
   - `https://neurospect-learn.pages.dev/auth/callback`
   - (keep `http://localhost:5173/auth/callback` for local dev)
3. Copy the **Client ID**; **Reset Secret** only if the current secret is not to hand — resetting it
   breaks the *other* deployed app until its env var is updated too.
4. Note **your own Discord user ID** — Settings → Advanced → Developer Mode on, then right-click your
   name → **Copy User ID**. This is the value for `ALLOWED_DISCORD_IDS`, and without it **nobody can
   log in** (§Auth).

## 3. Render — API + Postgres

`render.yaml` at the repo root is the source of truth for this service. Read its header comments
before changing anything there; every field carries the reason it holds that value.

1. Render dashboard (personal account) → **New → Blueprint** → connect GitHub → pick
   `russell94paul/neurospect-learn` → Render reads `render.yaml` and proposes
   `neurospect-learn-api` + `neurospect-learn-db`.
   - If the Blueprint route errors, create the two resources by hand instead: a **Web Service**
     (runtime Python, **Root Directory `api`**, build `pip install -r requirements.txt`, start
     command exactly as in `render.yaml`, health check `/health`) and a **Postgres**
     (`basic-256mb`, **version 16**, region `frankfurt`). Migrations still run either way —
     they live in the start command precisely so that manual creation works (§Differences).
2. **Environment** → set the variables marked `sync: false`. `DATABASE_URL` and `JWT_SECRET` are
   filled in by Render itself; **do not** add `DATABASE_URL_SYNC` (config.py derives the psycopg2 URL
   from `DATABASE_URL`, and a second copy could only drift).

   | Variable | Value |
   |---|---|
   | `ALLOWED_DISCORD_IDS` | your Discord user ID, e.g. `123456789012345678` |
   | `CORS_ORIGINS` | `https://neurospect-learn.pages.dev` |
   | `DISCORD_CLIENT_ID` | from §2 |
   | `DISCORD_CLIENT_SECRET` | from §2 |
   | `R2_ENDPOINT_URL` | from §1 |
   | `R2_ACCESS_KEY_ID` | from §1 |
   | `R2_SECRET_ACCESS_KEY` | from §1 |
   | `R2_BUCKET` | `neurospect-learn-evidence` |

   `MEASURED` (2026-08-11): the two list-valued vars accept a **JSON list**
   (`["a","b"]`), a **bare comma-separated list** (`a,b`), a **single value**, or **blank meaning
   unset** — all four are pinned by `tests/test_config_lists.py`. Before that validator existed,
   every form except JSON killed the app **at import**, and `sync: false` renders as an empty
   dashboard box, so the most likely first deploy would not have booted at all.

3. **Deploy.** Watch the log for `alembic upgrade head` running the 12 migrations, then uvicorn
   starting, then the health check going green.
4. Note the service URL (`https://neurospect-learn-api.onrender.com`).
5. `curl https://<service>/health` → `{"status":"ok"}`.

## 4. Cloudflare Pages — the frontend

1. Cloudflare → **Workers & Pages → Create → Pages → Connect to Git** → same repo.
2. Build settings:
   - **Project name:** `neurospect-learn` (this determines the `.pages.dev` host used everywhere above)
   - **Framework preset:** Vite
   - **Root directory:** `app` ← the monorepo difference; wrong here and the build finds no `package.json`
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
3. **Environment variables (Production):**

   | Variable | Value |
   |---|---|
   | `VITE_API_URL` | `https://neurospect-learn-api.onrender.com` |
   | `VITE_DISCORD_CLIENT_ID` | from §2 |
   | `VITE_DISCORD_REDIRECT_URI` | `https://neurospect-learn.pages.dev/auth/callback` |
   | `VITE_DEBUG` | `false` |

   `VITE_DEBUG=false` matters: it gates the debug-login form, which is backed by
   `POST /auth/debug/token` — an endpoint the API 404s whenever `DEBUG=false`. Shipping it `true`
   renders a button that can only fail.
4. Deploy. `app/public/_redirects` ships the SPA fallback (`/* /index.html 200`); without it a
   refresh on any deep route 404s — **including `/auth/callback`**, i.e. the first thing a login does.
5. If the Pages hostname differs from `neurospect-learn.pages.dev`, update **in lock-step**:
   `CORS_ORIGINS` (Render), `VITE_DISCORD_REDIRECT_URI` (Pages), and the Discord redirect URI (§2).

## 5. Seed the production database

Production starts with an empty schema: `alembic upgrade head` creates tables, **not content**. The
catalog is loaded by running the seed scripts from the laptop, where the wiki checkout lives.

> ⚠⚠ **The trap that has wiped the local seed twice.** Exporting `DATABASE_URL` alone does **not**
> redirect these scripts: `api/.env` also sets `DATABASE_URL_SYNC`, and `config.sync_database_url`
> prefers it. Set **both**, in the same shell, and then **prove where you are pointing before
> writing anything.** Never run `alembic downgrade` here at all — use `scripts/scratch_migrate.py`,
> which builds and drops its own throwaway database.

```powershell
cd C:\Users\PaulRussell\repos\neurospect-learn\api

# Render dashboard → the database → "External Database URL". Use the psql:// form.
# asyncpg rejects a ?sslmode= query parameter; leave it off the async URL (asyncpg
# negotiates TLS by itself). psycopg2 accepts it, so keep it on the sync URL.
$env:DATABASE_URL      = "<external url, no ?sslmode>"
$env:DATABASE_URL_SYNC = "<same url with postgresql+psycopg2:// and ?sslmode=require>"

# PROVE THE TARGET before writing. Prints host + database, never the password.
poetry run python -c "from app.config import settings; import sqlalchemy as sa; a=sa.engine.make_url(settings.async_database_url); s=sa.engine.make_url(settings.sync_database_url); print('async ->', a.host, a.port, a.database); print('sync  ->', s.host, s.port, s.database)"
```

**Both lines must show the Render host.** If either says `localhost:5433`, stop — the next command
would write to the working development database.

Then, in this order (each is idempotent and authoritative — a re-run replaces):

```powershell
poetry run python -m scripts.seed_concepts
poetry run python -m scripts.seed_tracks
poetry run python -m scripts.seed_drills      # depends on the concept seed
poetry run python -m scripts.ingest_content   # reads the wiki checkout
poetry run python -m scripts.seed_rubrics     # depends on drills
```

**Anchor the result against local** (`MEASURED` on the development DB, 2026-08-11):

| Table | Expected |
|---|---|
| `concepts` | 74 |
| `track_stages` | 23 |
| `drills` | 58 |
| `content_pages` | 67 |
| `rubrics` | 44 |
| `rubric_items` | 104 |
| `alembic_version` | `0012` |

Anything else means the seed did not land as it does locally — investigate before going further.
`users`, `journal_entries`, `evidence_assets` and `predictions` should all be **0** in production;
the local counts for those are fixtures and test residue, and none of it should be migrated.

Finally, close the shell, or unset both variables — a later local command inheriting them would run
against production.

## 6. Verification battery — the rendered surface, not the API

A query-layer pass is **not** a deployment check. E2, E3, E5 and E6 each caught a defect that only
the rendered surface showed, and the standing rule is that the consumer's layer is the page a person
looks at.

1. **Log in as a human.** Open `https://neurospect-learn.pages.dev` → Discord → back to the app.
   Confirm the debug-login form is **absent** (`VITE_DEBUG=false`).
2. **Every page paints.** Walk the whole sidebar and confirm no error state and no empty shell:
   course content, the three tracks, drills, Study Planner / today, journal, missed trades,
   analytics/expectancy, the Readiness Gate, predictions, the honesty strip.
3. **Anchor the numbers.** The Gate verdict, the expectancy figures and the drill/rep counts on the
   deployed instance are computed from a **freshly seeded, empty-of-user-data** database — so they
   should read as a clean start, *not* mirror the laptop's fixture-laden numbers. Confirm the catalog
   sizes (§5) rather than the progress figures.
4. **Exercise the one path that proves the deployment**: upload a chart capture as evidence, and
   confirm the thumbnail **renders**. That single action proves R2 credentials, the presigned URL and
   `evidenceSrc()`'s absolute/relative handling all work — `MEASURED`: `app/src/lib/evidence.ts`
   passes an absolute R2 URL through untouched and prefixes only app-relative ones, so R2 needs no
   frontend change.
5. **Then redeploy and look at that thumbnail again.** This is the test that R2 exists to pass: on
   the local backend the image is gone after a deploy while the row remains.
6. **Record which interactions respond and which are inert**, filter by filter. A silent no-op is a
   finding to write down, never an acceptable default.
7. **Capture labelled before/after screenshots** into the repo's evidence folder and link them from
   the tracker.

## 7. Rollback

| Failure | Rollback |
|---|---|
| Bad deploy | Render → the service → **Deploys** → **Rollback** to the previous successful deploy. |
| Bad migration | `alembic downgrade` is proven reversible to `0008`/`0009` and to `base` (`MEASURED` via `scripts/scratch_migrate.py`, 2026-08-11: `RESULT: REVERSIBLE`). Run it against **production only** with an explicit `-x db_url=`, never with a bare command. |
| Lost data | Render Postgres on a paid plan keeps daily backups; restore from the dashboard. |
| Locked out | Fix `ALLOWED_DISCORD_IDS` in Render env and redeploy; the check is per-request, so access returns immediately. |
| Total abandonment | Delete the Render Blueprint + the Pages project + the R2 bucket. Nothing outside those three holds state, and local development is untouched throughout. |

## Auth on a public URL

Before B3 the app trusted anyone, because only localhost could reach it. It is now allowlisted:

- `ALLOWED_DISCORD_IDS` (JSON list, comma list, or a single ID) decides who may hold an account.
- **It fails closed.** Empty means *everyone* when `DEBUG=true` (localhost, tests) and **nobody** when
  `DEBUG=false`. A forgotten env var therefore produces an immediate, obvious 403 naming the fix —
  never a silently open deployment.
- The check runs on **every authenticated request**, not just at login, because JWTs live 30 days.
  Removing an ID takes effect on that user's next request.
- A refused login **writes no `users` row**.

See `api/app/auth/allowlist.py` and `tests/test_auth_allowlist.py`.

## Differences from the `neurospect-api` runbook

Each of these would have been a defect if the earlier runbook had been replayed verbatim.

| # | `neurospect-api` | `neurospect-learn` | Why |
|---|---|---|---|
| 1 | Two repos | One repo, two packages | Render needs `rootDir: api`; Pages needs root directory `app`. |
| 2 | DB `plan: starter` | `plan: basic-256mb` | `starter` is a **legacy** Postgres type — Render no longer creates new databases on it, so the old value fails the Blueprint outright. |
| 3 | `postgresMajorVersion` 16 | 16, stated explicitly | Omitting it now defaults to **18**; 16 matches the local Docker DB (`postgres:16.13`). |
| 4 | gunicorn `-w 2` | uvicorn `--workers 1` | **Not a resource decision.** `services/ai_grade_queue.py` serialises with a per-*process* `asyncio.Lock` and has no DB-level claim, so two workers would drain the same `pending` grades — duplicate advisory grades and duplicate Anthropic spend. Raising it requires adding a DB claim first. |
| 5 | gunicorn dependency | plain uvicorn | With one worker the process manager buys nothing, and `uvicorn[standard]` is already a dependency while gunicorn is not. |
| 6 | R2 optional (screenshots 503 gracefully) | **R2 required** | There is no 503 path here: `make_backend()` silently falls back to the local filesystem, so an unconfigured deploy destroys evidence instead of refusing to store it. |
| 7 | Prompt files bundled into the repo | Wiki stays out entirely | Only `scripts/` read the wiki, and they run from the laptop. |
| 8 | `region: oregon` | `region: frankfurt` | Single UK user, interactive daily use. Web service and database must share a region. |
| 9 | Discord app created for it | Same Discord app, new redirect URI | Resetting the shared secret breaks the other deployment until its env var is updated too. |

Carried over unchanged, because they still bite: `preDeployCommand` and `pythonVersion` are **not**
honoured for manually-created services (which is why migrations live in the start command), and
`.python-version` is the only reliable way to pin the Python version.

## Known gaps at first deploy

- **Two clocks.** `planner._today_in(tz)` computes "today" in the user's `study_preferences.timezone`
  (default `"UTC"`), while migration `0012`'s rest-day trigger compares against the **server's UTC
  date**. They agree for a user at or ahead of UTC (Paul, UK) and can disagree for one west of it.
  Deployment makes this permanent rather than incidental — Render runs UTC. `MEASURED` 2026-08-11:
  this is what made `test_honesty_api.py` fail every evening on a Pacific-time machine; the tests now
  read the same clock as the code, but the underlying two-clock design is **unresolved** and is
  logged for B4.
- **`WIKI_CONTENT_ROOT` resolves to a path that does not exist on Render.** Harmless today because no
  runtime code reads it — but a seed script run *on the server* would silently find nothing.
- **`AI_GRADING_ENABLED=false`** at first deploy. Turning it on requires an `ANTHROPIC_API_KEY` in
  Render env, and see difference #4 before scaling the service.

## See Also

- [[processes/distributed-workflow/active/backtest-companion]] — the B-phase tracker this serves
- [[processes/distributed-workflow/active/deployment]] — the `neurospect-api` deployment it adapts
- [[concepts/architecture/learning-enforcement]] — the invariants a deploy must not weaken
- [[entities/projects/neurospect]] — project overview
