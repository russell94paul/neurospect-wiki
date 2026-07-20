---
tags: [architecture, frontend, backend, learning-platform, mastery, neurospect, phase5]
aliases: [Learning Platform Architecture, neurospect-learn, Learn App, Learning Platform Frontend]
sources: [processes/distributed-workflow/active/learning-platform-ui.md, concepts/mastery/README.md, concepts/mastery/unified/learning-path.md, concepts/mastery/unified/tracker.md, concepts/architecture/phase3-frontend-structure.md, concepts/architecture/phase2-project-structure.md, concepts/architecture/trade-schema.md]
created: 2026-07-18
updated: 2026-07-19
---

# Learning Platform — Architecture (Phase 5a design)

Canonical design doc for **`neurospect-learn`**, a **new, standalone** Learning Platform app that (a) surfaces
all Neurospect course content in a navigable layout and (b) tracks Paul's progress across three axes —
**learning exercises → backtesting → live trading** — graded on the **existing** mastery ladder / confidence
scale / Readiness-to-Live Gate defined in [[concepts/mastery/README]]. It is the delivery layer over the
[[processes/distributed-workflow/active/mastery-layer|Mastery Layer]] content (complete).

> **Code now exists (Phase 5b shipped 2026-07-19).** The scaffold lives at
> `C:\Users\PaulRussell\repos\neurospect-learn` (`app/` + `api/`). Per [[CLAUDE]] §Architecture Doc Integrity
> the **code is ground truth**; this doc describes it *as implemented* (see §5b as-built for divergences).
> Remaining phases 5c–5g are sequenced in [[processes/distributed-workflow/active/learning-platform-ui]].

> **No-drift.** This doc states *structure and decisions*. It does **not** restate the mastery model, the
> playbook, the learning-path, the exercise libraries, the entry-model YAML, or any concept page — it **links**
> to them and the UI **renders/links** them. The wiki stays the single source of truth for content.

## Decisions (Paul, 2026-07-18)

Three product forks were put to Paul before this design was written:

1. **Backend: a separate, self-contained backend** (not sharing `neurospect-api`). Own FastAPI + Postgres +
   Discord auth + expectancy engine. Full isolation from the journal app.
2. **A brand-new, model-aligned journal** (not the generic `trades` schema, not a mirror of `neurospect-app`):
   a journal whose fields trace directly to the specific ICT/Aura/unified models this platform teaches, with a
   `mode` discriminator so the *same* journal powers both **backtest** and **live** axes.
3. **Content API from the backend** (not a build-time bundle, not a one-time port): the backend serves the
   markdown; an ingest job loads the curated wiki content into the backend so the API is self-contained. Wiki
   stays canonical; authoring stays in Obsidian.

## New-app shape

- **Repo:** `neurospect-learn`, structured internally as `app/` (frontend) + `api/` (backend) — a small
  two-package repo. This drops cleanly into the eventual `neurospect/learn/` under the
  [[processes/distributed-workflow/active/monorepo-migration|monorepo migration]] (a fourth sibling alongside
  `wiki/`, `api/`, `app/`). **No runtime dependency on `neurospect-api`.**
- **Discord OAuth:** reuse the same Discord *application* (OAuth client) with a new redirect URI; the learn
  backend mints its **own** JWTs and owns its **own** `users` table. *(One-line setup decision for 5b — a
  second Discord app is also fine.)*

### Frontend stack — lifted from `neurospect-app` (selective lift, not a fork)

Lift the **infrastructure spine unchanged**, rebuild the domain layer. Source of truth is the shipped code in
`C:\Users\PaulRussell\repos\neurospect-app`, **not** the versions in [[concepts/architecture/phase3-frontend-structure]]
(see §Contradiction flag).

| Layer | Choice (shipped versions) |
|---|---|
| Framework / build | React 19 · Vite 8 · TypeScript 6 (project-references) |
| Routing | React Router v7 (data router) |
| Server state | TanStack Query v5 |
| Forms | React Hook Form 7 + Zod 4 (`@hookform/resolvers`) |
| HTTP | ky v2 |
| UI | shadcn/ui (Radix + Tailwind v4 via `@tailwindcss/vite`) |
| Charts | Recharts v3 |
| Utilities | date-fns v4, lucide-react |

**Lift wholesale:** `main.tsx` provider stack (`QueryClientProvider` → `AuthProvider` → router), `App.tsx`
`ProtectedLayout` pattern, `lib/api.ts` (ky instance — `beforeRequest` Bearer injection, `afterResponse` 401 →
`/login`), `lib/auth.ts` (Discord OAuth context; **rename the `localStorage` token key** to avoid same-origin
collision), `lib/utils.ts` (`cn` + formatters), all 25 `components/ui/` primitives, `components.json`, and the
`vite`/`tsconfig`/`eslint` config. **Reuse the patterns:** RHF+Zod form recipe (schema → `z.infer` →
`zodResolver`, `dirtyFields` PATCH, tabbed multi-status form), hierarchical query keys, per-domain flat hooks,
Recharts `ResponsiveContainer`+`Cell` conditional-color template, KPI stat-card grid.

**Leave behind:** everything under `components/{trade,coach,coach-setup,screenshot,settings}`, the ICT
`constants.ts`/`types/api.ts` domain vocab, the Tradovate/coach/screenshot hooks, and the journal/broker
branding + shell badges. *(Note: `neurospect-app` uses card-lists, not a data-grid — no TanStack Table. If a
tracker/journal view needs sortable grids, add that fresh.)*

### Backend stack — mirrors `neurospect-api`'s proven layout (distinct codebase)

FastAPI 0.115+ · SQLAlchemy 2.0 async (`asyncpg`) · Alembic · Postgres · Discord OAuth2 + JWT (python-jose) ·
Poetry. Mirror the [[concepts/architecture/phase2-project-structure]] skeleton (`config`/`database`/`deps`/
`auth`/`models`/`schemas`/`routers`/`services`) and its **raw-SQL-for-analytics** approach — as a *separate*
project with its own DB and secrets. Screenshot storage (R2) is **optional/deferred** for 5a.

## Route / page taxonomy (mapped to U0–U6)

Maps to the stages of [[concepts/mastery/unified/learning-path]].

| Route | Page | Surfaces | U-stage |
|---|---|---|---|
| `/path` (home) | **Curriculum spine** — U0→U6 as a gated visual path with per-stage progress rings; the one-glance stage map | learning-path | whole spine |
| `/path/:stage` | **Stage detail** — concepts in the stage + drills + the ladder-stage **exit-bar** gate status | learning-path + tracker | U0–U4 |
| `/library` | **Content browser** — course modules · entry models · unified playbook · aura · frontier; searchable | all content | all |
| `/concepts/:slug` | **Content reader** — rendered markdown + **TIER / label badge** + a "track this" panel (ladder position, edit) | any content page | all |
| `/drills` | **Exercise tracker** — the two drill libraries with ✋ hand-mark / 🛠 tool variants + rep counters + mark-complete | aura/ict-course exercises | U0–U4 |
| `/journal` · `/journal/new` · `/journal/:id` | **Model-aligned journal** — log entries with a `backtest \| live` mode toggle; list + filters | (new data) | U6 |
| `/expectancy` | **Expectancy dashboard** — per-model win rate / avg R / expectancy / sample; backtest vs live (Recharts) | (new data) | U6 |
| `/gate` | **Readiness view** — computed "cleared to live?" signal per model + the Gate checklist | mastery/README §Gate | U6 |

**Frontier (U5)** appears inside `/library` + `/concepts` carrying its exact TIER + ESTABLISHED/EMERGING/
SPECULATIVE label, marked **study-and-watch**; the UI must **never** let an EMERGING/SPECULATIVE concept count
toward gate eligibility (see §Gate).

## Content delivery — Content API + ingest

> **As-built (Phase 5d shipped 2026-07-20).** The ingest, slug scheme, endpoints, and reader below are the
> shipped behaviour in `neurospect-learn` (`api/scripts/ingest_content.py`, `api/app/routers/content.py`,
> `app/src/{lib/content.ts,pages/{library,concept-reader}.tsx,components/content/*}`). **Code is ground truth.**
> See §5d as-built for the sketch→final decisions. The MACHINE_READABLE_STRATEGY parse is **deferred to 5f**
> (5d ingests entry-model pages as ordinary content).

The backend owns the content. The **ingest job** `api/scripts/ingest_content.py` (async, `AsyncSessionLocal` +
`pg_insert … on_conflict_do_update`, idempotent UPSERT on `slug`, prunes rows no longer in the corpus; `--dry-run`
flag) parses the curated wiki dirs — `concepts/{course,entry-models,mastery,advanced,business-logic,aura}/**`
(67 pages) — into `content_pages`, storing the raw markdown body, frontmatter `tags`, a derived `title` (first
`# H1`), `category` (top-level dir), `source_path`, and the set of **resolved internal wikilink target slugs**.
Frontmatter YAML that fails to parse (one file: `aura/aura-asset.md`) falls back to body-only (Rule #1 — sources
are never edited). `tier`/`label`/`u_stage` on `content_pages` are nullable and effectively unused here (no page
carries them in frontmatter — the reader badge comes from the referencing **concept** instead); u_stage is not
load-bearing.

- **Slug scheme** (the load-bearing 5d decision): basename minus `.md`, lowercased, leading `NN-` lesson prefix
  stripped; `README` → its parent dir name; de-collided by extending leftward one path segment, with a **depth
  tiebreak** so the shallowest (canonical) page keeps the bare slug. Result: `entry-models/consolidation-model`
  → `consolidation-model` (wins over the course lesson, which becomes `module-2-price-delivery-consolidation-model`);
  mastery meta-files → `aura-tracker`/`unified-learning-path`/… The scheme makes **every** non-null
  `concepts.content_slug` seeded in 5c resolve with **no seed change and no Alembic 0004** (verified: 0 unresolved;
  the 4 intentionally-NULL synthesis concepts — `u2-4`, `u3-1b`, `u5-smt-confirm-axis`, `u5-confluence-stack` — stay NULL).
- **Endpoints** (`api/app/routers/content.py`, mounted at `/api/content`, all require `get_current_user` — content
  is shared, not user-scoped): `GET /pages` (summaries, frontend groups by category), `GET /pages/{slug}` (full
  body + `wikilink_targets` + a `badge` sourced from the referencing concept — frontier TIER/label + `watch_only`),
  `GET /search?q=` (ILIKE on title+body, `q` min-length 2, limit 50). Schemas in `app/schemas/content.py`.
- **Frontend:** `/library` (grouped/searchable browser) + `/concepts/:slug` (reader). Markdown via `react-markdown`
  + `remark-gfm`; `[[wikilinks]]` resolve to `/concepts/:slug` — the **backend owns the slug scheme; the frontend
  resolves by lookup** against path/basename maps built from the page list (no scheme duplication). Unresolved
  links (anchor-only, or out-of-corpus like `[[entities/…]]`) render **inert**. `TierBadge`/`LabelBadge`/watch-only
  enforce the frontier labels. `@tailwindcss/typography` with prose colours bound to the shadcn theme tokens (the
  media-based `dark:prose-invert` mismatches the class-based theme — see §5d as-built).
- **Config:** `WIKI_CONTENT_ROOT` (`app/config.py`, documented in `.env.example`) — the neurospect-wiki checkout
  the ingest reads, default the sibling `../neurospect-wiki`. **READ-ONLY**; skips `sources/` + `vault/`; never
  writes back to the wiki. Re-run ingest to refresh (wiki stays canonical, author in Obsidian).

## Progress + journal data model

> **As-built (Phase 5c shipped 2026-07-19).** The field set below is the finalized schema now live in
> `neurospect-learn/api` (migrations `0002_learning_progress` + `0003_journal_entries`, models under
> `app/models/`). **Code is ground truth.** See §5c as-built for the sketch→final decisions.

Three axes map to three concerns. `concept_progress` + `journal_entries` are `user_id`-scoped + soft-deleted;
`concepts` + `content_pages` are seed/content (UUID PK + timestamps, **no** soft-delete — re-seed/re-ingest
replaces). All tables use UUID PKs + `TIMESTAMPTZ` + the `update_updated_at()` trigger — same conventions as
[[concepts/architecture/trade-schema]] §Schema Conventions (reused, not restated).

### 1. Learning progress (the exercise axis)

- **`concepts`** — one row per gradable concept, **seeded** (41 rows) from the U0–U6 taxonomy in
  [[concepts/mastery/unified/learning-path]] + [[concepts/mastery/unified/tracker]] via
  `api/scripts/seed_concepts.py` (idempotent UPSERT on `slug`). Columns: `slug` (UNIQUE), `code` (e.g.
  "U1.3"), `u_stage` (`u_stage` enum U0–U6), `title`, `is_core`, `tier` + `label` + `axis` (frontier only),
  `watch_only`, `rep_target` (freetext — targets are "≥50 ranges"/"1 week", not always numeric),
  `content_slug` (**nullable soft ref** → `content_pages.slug`), `drill_refs` (TEXT[] soft refs, e.g.
  `{"aura D2-c"}`), `sort_order`, `notes`. Seeded data, not user-editable. **DB-enforced invariant:**
  `CHECK (u_stage <> 'U5' OR NOT is_core)` — no frontier concept is ever core.
- **`concept_progress`** — the live tracker grid, one row per (user, concept): `ladder_stage` (SMALLINT,
  `CHECK 1–4`), `confidence` (SMALLINT, `CHECK 1–5`), `reps` (int, default 0), `last_practiced`, `notes`.
  Exactly the `tracker.md` grid made editable. UNIQUE partial `(user_id, concept_id) WHERE NOT is_deleted`;
  FKs → `users`, `concepts`. **Rows are created per-user at runtime (later phases) — the 5c seed populates
  `concepts` only.** Stage status (U0–U6 gate cleared?) is **derived**, never stored.
- **`content_pages`** — created **empty** in 5c; the 5d ingest fills it. `slug` (UNIQUE), `title`, `body`
  (markdown), `u_stage` + `tier` + `label` + `category` + `tags` (TEXT[], GIN) + `wikilink_targets` (TEXT[])
  + `source_path`. `concepts.content_slug` soft-references its `slug` (the 5d ingest owns the slug scheme).

### 2. Model-aligned journal (the backtest + live axes)

The **`journal_entries`** table — deliberately **not** the generic `trades` schema — whose fields trace to
the [[concepts/mastery/unified/README|Unified Playbook]] one-glance decision flow and the entry-model
checklists. `mode` (`journal_mode` enum `backtest|live`) makes the same journal power both axes and lets the
gate compare them. **Finalized field set (as-built):**

- **Identity/context:** `user_id`, `entry_date`, `instrument`, `session` (`session_type` enum), `mode` (NOT NULL).
- **Model:** `entry_model` (`entry_model` enum → the 7 entry models + `unified`, NOT NULL) — the
  expectancy-grouping key (indexed).
- **Decision-flow capture (the model-aligned part):** `draw_on_liquidity` (TEXT), `range_position`
  (`range_position` enum discount/eq/premium), `swing_qualification` (SMALLINT `CHECK 0–2` — the
  double-qualified-swing score, **R2**), `seq_smt_confirmed` (HTF, bool), `triad_smt_confirmed` (LTF, bool),
  `aura_asset_leg` (bool, optional 6S **R7** — **included**, nullable), `time_window_valid` (bool),
  `entry_pda` (`entry_pda` enum, **DEFAULT `'fvg'`** per **R4**).
- **Execution/risk:** `entry_price`, `stop_price`, `target_price`, `rr_planned`, `risk_pct` (the %/R
  framing — expectancy is computed in R, not dollars), `exit_price`, `r_multiple`, `outcome` (`outcome`
  enum), `mae`, `mfe`.
- **Frontier stack (watch-only tags):** `confluence_tags` (TEXT[], GIN — which WHERE/WHEN/DIRECTION/CONFIRM
  filters aligned; for study, **never** gate-eligible).
- **Review:** `plan_followed`, `mistake_tags` (TEXT[], GIN), `grade` (`grade` enum a_plus/a/b/c), `notes`.

**Deferred (documented, not built in 5c):** screenshots/R2 (no storage this phase); `position_size` / dollar
sizing (expectancy is R-based — `risk_pct` carries the %/R framing); the Aura canceled-order `missed_trades`
surface per [[concepts/architecture/trade-schema]] §Missed Trades (separate lightweight table, out of scope).

### 3. The gate (computed, not stored)

`GET /api/gate` computes readiness **per model** by combining all three sources — it does not duplicate the
Gate text, which is canonical in [[concepts/mastery/README]] §Readiness-to-Live Gate:

- **(a)** every **core** concept (U1–U4) at **Backtested+** (from `concept_progress`); load-bearing few at Live-ready.
- **(b)** `mode='backtest'` sample ≥ target (≥50 setups / ≥100 trades) with **positive expectancy in R** per
  model — expectancy `= (win% × avg win R) − (loss% × avg loss R)`, break-even `= 1/(1+R:R)`
  (reimplemented over `journal_entries`; see [[concepts/aura/risk-management]]).
- **(c)** the behavioural checklist items (risk precommitted in writing, journaling habit, circuit-breaker
  demonstrated) — user-attested.

**Invariants the UI must enforce:** no frontier (U5) concept counts toward "core at Backtested+"; a model is
never "Backtested+" without the required sample; live-eligibility is gated on the established playbook (U1–U4),
never on unbacktested confluence.

## Component structure + API surface

- **New components:** `StagePath`/`StageNode`, `LadderBadge` (1–4), `ConfidenceRating` (1–5), `RepCounter`,
  `ExitBarGate`, `TierBadge`, `LabelBadge`, `MarkdownRenderer`, `SearchCommand`, `DrillCard` (✋/🛠),
  `ConceptTrackPanel`, `JournalForm` (tabbed, RHF+Zod, `mode` toggle — lifts the `trade-form` recipe),
  `JournalCard`/`JournalFilters`, `ExpectancyChart`, `BacktestVsLiveChart`, `GateChecklist`, `GateSignal`.
- **New endpoints (separate API):**
  - `auth`: `POST /auth/discord/token`, `GET /auth/me`, `POST /auth/debug/token` (debug-gated).
  - `content`: `GET /api/content/pages`, `/pages/{slug}`, `/search`.
  - `learning`: `GET /api/concepts`, `GET|PATCH /api/progress`, `GET /api/stages`.
  - `journal`: `POST|GET|GET{id}|PATCH|DELETE /api/journal` (filters incl. `mode`, `entry_model`).
  - `analytics`: `GET /api/analytics/expectancy` (by model × mode), `/summary`, `/r-distribution`.
  - `gate`: `GET /api/gate`.

## Implementation split (5b → 5g)

Each phase is a boot-promptable unit; sequenced in [[processes/distributed-workflow/active/learning-platform-ui]].

- **5b — Scaffold.** ✅ **Built 2026-07-19** (`C:\Users\PaulRussell\repos\neurospect-learn`). Create the
  `neurospect-learn` repo (app + api); lift the frontend spine + backend skeleton; Discord OAuth working
  end-to-end; app shell + nav + protected routes. See §5b as-built below.
- **5c — Data model + migrations.** ✅ **Built 2026-07-19.** `concepts` + `concept_progress` +
  `journal_entries` + `content_pages`; Alembic `0002`/`0003`; 41 `concepts` seeded from the U0–U6 taxonomy;
  the model-aligned journal field set finalized. See §5c as-built below.
- **5d — Content API + ingest + browser/reader.** ✅ **Built 2026-07-20.** Ingest job (67 pages); content
  endpoints; `/library` + `/concepts` (markdown render, wikilink resolver, TIER/label badges, search). See §5d
  as-built below.
- **5e — Progress tracker.** `/path` + `/path/:stage` + concept-progress editing (ladder/confidence/reps) +
  `/drills`.
- **5f — Journal + expectancy.** Model-aligned `/journal` (backtest|live) + `/expectancy` dashboard.
- **5g — Gate/readiness.** `/gate` computed readiness + watch-only enforcement.

### 5b as-built (2026-07-19) — code is now ground truth

Scaffold shipped and verified end-to-end (backend: `poetry install`, `alembic upgrade head` creates `users`,
`/health`=200, `/docs` loads, `POST /auth/debug/token` → JWT, `GET /auth/me` returns the user, no-token → 403;
frontend: `npm install`, `tsc -b` + `vite build` clean, debug-login lands on `/path`, logged-out protected
route redirects to `/login`, sidebar renders all six nav items with active-state highlighting, param stub route
renders its slug, no console errors). Divergences from the design above, recorded per Architecture Doc Integrity:

- **Repo shape as designed:** `neurospect-learn/{app,api}`, two independently-installable packages, `git init`
  only (no commit — Paul handles git). Backend lift source was `…\repos\neurospect\neurospect-api` (not
  `…\repos\neurospect-api`).
- **Tailwind v4 token bridge (real fix, not cosmetic):** the lifted `neurospect-app/src/index.css` defines the
  shadcn HSL token triples in `:root`/`.dark` but has **no `@theme` block**, so Tailwind v4 emitted **none** of
  the semantic utilities (`bg-primary`, `bg-card`, `text-muted-foreground`, `border-border`, hover/focus
  variants…) the shadcn components rely on — verified by grepping the built CSS. Added an `@theme inline` block
  mapping each `--<token>` → `--color-<token>: hsl(var(--<token>))` (+ `--radius-*`); rebuilt and confirmed the
  utilities now emit. Any future lift from `neurospect-app` inherits this same gap.
- **Frontend deps pruned for the scaffold:** dropped `recharts` (charts arrive in **5f** — re-add then) and
  `react-day-picker` + its sole consumer `components/ui/calendar.tsx` (unused in 5b; re-add via `npx shadcn add
  calendar` when a date field lands). 20 of the `ui/` primitives carried over. All other spine files
  (`main.tsx`, `lib/{api,auth,utils}`, layout shell, `login`/`auth-callback`) lifted; `api.ts`/`auth.ts` token
  key renamed to `neurospect_learn_token`; `types/api.ts` reduced to the auth `User`/`TokenResponse` shapes.
- **Backend stripped to the users-only slice:** dropped `boto3`, `anthropic`, `gunicorn`; added `python-dotenv`
  explicitly (`alembic/env.py` imports it). `config.py` keeps only DB/JWT/Discord/CORS/DEBUG. Auth endpoints as
  designed, with `TokenResponse`/`UserResponse` factored into `app/schemas/auth.py`. `models/enums.py` is an
  empty placeholder. `alembic 0001_initial_users` = `update_updated_at()` trigger fn + `users` table + trigger
  only. `GET /auth/me` returns **403** (not 401) when the Bearer header is absent — FastAPI `HTTPBearer`
  default, unchanged from `neurospect-api`.
- **Discord:** reuse-the-same-application decision left to Paul; `.env.example` documents a new redirect URI for
  the learn app. Not exercised live in 5b (debug-login covers local verification).

### 5c as-built (2026-07-19) — code is now ground truth

Data model + migrations shipped and verified end-to-end (see §Progress + journal data model for the final
field set). Four tables, eight enums, two migrations, one idempotent seed. Verification: `alembic upgrade head`
runs `0001→0003` clean, `downgrade base` + back up clean (fully reversible); `\d` confirms all tables/enums/
constraints/indexes/triggers + FKs (`concept_progress→users,concepts`; `journal_entries→users`); seed loads 41
concepts, re-run idempotent (41 rows, 41 distinct slugs, no dupes); both CHECK constraints reject bad rows
(U5-core, ladder=9); models import clean; `uvicorn app.main:app` → `/health`=200 with the new models
registered. Decisions made while finalizing (the sketch→final calls the design left open):

- **Journal field-set resolutions.** `aura_asset_leg` — **included** (nullable bool): a single cheap column
  that traces to R7; deferring it would force a later migration on the load-bearing journal. `entry_pda` —
  `entry_pda` enum with **`DEFAULT 'fvg'`** (R4). `position_size` — **deferred** (there is no broker
  integration here and expectancy is computed in R; `risk_pct` carries the %/R framing). Screenshots and the
  `missed_trades` surface — **deferred** (documented, out of 5c scope). `swing_qualification` gets a `CHECK
  0–2`; `ladder_stage`/`confidence` get `CHECK 1–4`/`1–5`.
- **Enums defined fresh** (not imported from `neurospect-api`): `u_stage`, `journal_mode`, `entry_model`
  (7 models + `unified`, values e.g. `reversal_raid_on_stops`/`smt_confirmation`), `range_position`,
  `session_type`, `entry_pda`, `outcome`, `grade`. Migrations own the `CREATE TYPE`; the ORM references them
  with `create_type=False` via an `enums.pg_enum()` helper (mirrors the raw-SQL migration idiom from 0001).
- **`concepts` columns beyond the sketch:** added `code` (e.g. "U1.3"), `axis` (WHERE/WHEN/DIRECTION/CONFIRM/
  STACK — frontier), `watch_only` (bool), `sort_order`, `notes`. `is_core` follows the **tracker's explicit
  `**core**` annotations** (10 core: U1.1–U1.5, U2.2–U2.4, U3.1a, U3.1c) — evidence-based, not invented; a
  data edit (re-seed) can adjust it later. `content_slug` + `drill_refs` are **soft refs** (nullable slug +
  TEXT[]), never hard FKs — `content_pages` is empty until 5d and drill IDs live in the wiki. Seeded
  `content_slug` values are **provisional** (wiki page basenames); the 5d ingest owns the real slug scheme and
  reconciles them.
- **Frontier invariant enforced in the DB:** `CHECK (u_stage <> 'U5' OR NOT is_core)` on `concepts`; all 12
  U5 rows carry `watch_only=true` + their exact TIER/label from the tracker. `confluence_tags` on the journal
  are watch-only (never gate-eligible). The gate itself remains **computed, not stored** (5g).
- **Content ingest NOT built** (5d): `content_pages` is created empty; only the table shape exists.

### 5d as-built (2026-07-20) — code is now ground truth

Content API + ingest + library/reader shipped and verified end-to-end. See §Content delivery for the shipped
shape. Decisions made while building (the calls the design left open):

- **Slug scheme + reconciliation.** Chose basename-with-`NN-`-strip + README→dir + leftward de-collision with a
  **depth tiebreak** (see §Content delivery). This resolves **all 27** non-null `concepts.content_slug` soft-refs
  with **zero seed edits and no Alembic 0004** — `content_pages`'s 5c shape already sufficed. Verified by SQL
  left-join (unresolved = 0). The one genuine basename collision — `consolidation-model` (the entry-model page vs
  the course lesson) — resolves to the entry-model page (the concept's "YAML canonical" target) via the depth
  tiebreak; the course lesson takes `module-2-price-delivery-consolidation-model`.
- **Wikilink resolution split.** Backend owns slug derivation and stores each page's `source_path` + resolved
  `wikilink_targets`; the frontend resolves raw `[[tokens]]` by **lookup** against path/basename maps built from
  the page list — no slug-scheme duplication (only trivial token normalization is shared). Bare, full-path
  (`[[concepts/…]]`), aliased (`|display`), and anchor-only (`[[#x]]`) forms all handled; out-of-corpus + anchor
  links render inert. Display text prefers an explicit alias, else the resolved page **title** (not the raw path).
- **Reader badge from the concept, not the page.** No wiki page carries `tier`/`label` in frontmatter, so
  `GET /pages/{slug}` derives the badge from the concept(s) referencing the page (prefer one carrying a label;
  `watch_only` true if **any** does) — so a frontier page reads `U5 · Tier · EMERGING · Study & watch · Never
  gate-eligible`.
- **Auth parity.** Content is shared (not user-scoped) but every endpoint requires `get_current_user`, matching
  the protected SPA (401/403 without a Bearer token).
- **Frontend fixes surfaced by browser verification (real, not cosmetic):** (1) react-markdown v10's default
  `urlTransform` stripped the custom `wikilink:` href scheme → every link pointed at the current page; fixed with
  a passthrough `urlTransform`. (2) `dark:prose-invert` is **media-query** based while the shadcn theme is
  **class** (`.dark`) based — on an OS-dark machine it inverted prose text to near-white on a white page; fixed by
  binding the `--tw-prose-*` colours to the shadcn tokens. (3) the reader showed the title twice (card header +
  body's leading `# H1`); the body's leading H1 is now stripped.
- **Deps added.** Backend: `python-frontmatter`. Frontend: `react-markdown`, `remark-gfm`,
  `@tailwindcss/typography` (via `@plugin` in `index.css`), and `@playwright/test` (dev).
- **Playwright harness (new, per Paul 2026-07-20).** `app/playwright.config.ts` + `app/e2e/` — a `global-setup`
  mints a debug JWT from the API and writes it into a Playwright `storageState`; `content.spec.ts` pins the 6 5d
  behaviours (library grouping, reader markdown+table, frontier badge/watch-only, wikilink click-through,
  unresolved-inert, search). `npm run test:e2e`; all 6 green. This is the standing UI-test pattern for 5e+.

## Contradiction flag (per [[CLAUDE]] Rule #6)

[[concepts/architecture/phase3-frontend-structure]] lists the `neurospect-app` stack as **Vite 6 · ky v1**
(and does not pin TS/Recharts/Tailwind/Zod majors). The shipped code is actually **Vite 8 · TypeScript 6 ·
ky v2 · Zod 4 · Recharts 3 · Tailwind v4 · React Router 7.14**. Code is ground truth. That doc is the
`journal-analytics` lane's canonical page, so it is **flagged here for Paul, not edited from this session** —
its owning lane should reconcile it (or the monorepo migration's same-PR rule will).

## See Also

- [[processes/distributed-workflow/active/learning-platform-ui]] — the workstream tracker (5b–5g phases)
- [[concepts/mastery/README]] — the ladder / confidence / Readiness-to-Live Gate the platform visualizes
- [[concepts/mastery/unified/learning-path]] · [[concepts/mastery/unified/tracker]] — the U0–U6 spine + grid the UI renders
- [[concepts/mastery/unified/README]] — the Unified Playbook the journal fields trace to
- [[concepts/advanced/README]] — frontier content + the TIER/label + watch-only rules the UI enforces
- [[concepts/architecture/phase3-frontend-structure]] — the `neurospect-app` frontend lifted from (see §Contradiction flag)
- [[concepts/architecture/phase2-project-structure]] — the backend layout the new API mirrors
- [[concepts/architecture/trade-schema]] — the journal conventions reused (schema is new, conventions shared)
- [[processes/distributed-workflow/active/monorepo-migration]] — where `neurospect-learn` eventually sites
