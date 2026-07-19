---
tags: [architecture, frontend, backend, learning-platform, mastery, neurospect, phase5]
aliases: [Learning Platform Architecture, neurospect-learn, Learn App, Learning Platform Frontend]
sources: [processes/distributed-workflow/active/learning-platform-ui.md, concepts/mastery/README.md, concepts/mastery/unified/learning-path.md, concepts/mastery/unified/tracker.md, concepts/architecture/phase3-frontend-structure.md, concepts/architecture/phase2-project-structure.md, concepts/architecture/trade-schema.md]
created: 2026-07-18
updated: 2026-07-18
---

# Learning Platform — Architecture (Phase 5a design)

Canonical design doc for **`neurospect-learn`**, a **new, standalone** Learning Platform app that (a) surfaces
all Neurospect course content in a navigable layout and (b) tracks Paul's progress across three axes —
**learning exercises → backtesting → live trading** — graded on the **existing** mastery ladder / confidence
scale / Readiness-to-Live Gate defined in [[concepts/mastery/README]]. It is the delivery layer over the
[[processes/distributed-workflow/active/mastery-layer|Mastery Layer]] content (complete).

> **Design-only (Phase 5a).** No app code exists yet. Once code lands, per [[CLAUDE]] §Architecture Doc
> Integrity the **code becomes ground truth** and this doc describes it *as implemented*. Implementation is
> sequenced in [[processes/distributed-workflow/active/learning-platform-ui]] (Phases 5b–5g).

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

The backend owns the content. An **ingest CLI/job** parses the curated wiki dirs — `concepts/course/*`,
`concepts/entry-models/*`, `concepts/mastery/**`, `concepts/advanced/*` (and the concept pages they link) —
into a `content_pages` table, preserving frontmatter (**TIER + label + tags**), a U-stage mapping, and the set
of internal wikilink targets. The entry-model `# --- MACHINE_READABLE_STRATEGY ---` YAML blocks parse into
structured strategy records (reused to seed the journal's model picker).

- **Endpoints:** `GET /api/content/pages` (list/tree), `GET /api/content/pages/{slug}`, `GET /api/content/search?q=`.
- **Frontend:** renders markdown (e.g. `react-markdown`), rewrites `[[wikilinks]]` → `/concepts/:slug`, and
  renders TIER/label badges from frontmatter.
- **Sync:** wiki stays canonical (author in Obsidian); re-run ingest to refresh. Ingest reads the wiki repo
  checked out alongside the backend (a sibling dir post-monorepo). **Never writes back to the wiki.**

## Progress + journal data model

Three axes map to three concerns. All tables are `user_id`-scoped, soft-deleted, UUID PKs, `TIMESTAMPTZ` —
same conventions as [[concepts/architecture/trade-schema]] §Schema Conventions (reused, not restated).

### 1. Learning progress (the exercise axis)

- **`concepts`** — one row per gradable concept, **seeded from the U0–U6 taxonomy** in
  [[concepts/mastery/unified/learning-path]] + [[concepts/mastery/unified/tracker]]. Columns: `slug`,
  `u_stage` (U0–U6), `title`, `is_core` (bool), `tier` + `label` (frontier only), `rep_target`,
  `content_slug` (→ `content_pages`), `drill_refs` (the canonical drill IDs, e.g. `aura D2-c`). Seeded data,
  not user-editable.
- **`concept_progress`** — the live tracker grid, one row per (user, concept): `ladder_stage` (1–4),
  `confidence` (1–5), `reps` (int), `last_practiced`, `notes`. This is exactly the `tracker.md` grid made
  editable. Stage status (U0–U6 gate cleared?) is **derived** from the concepts in each stage meeting their
  exit bar.

### 2. Model-aligned journal (the backtest + live axes)

A **new** `journal_entries` table — deliberately **not** the generic `trades` schema — whose fields trace to
the [[concepts/mastery/unified/README|Unified Playbook]] one-glance decision flow and the entry-model
checklists. `mode ENUM('backtest','live')` makes the same journal power both axes and lets the gate compare
them. Sketch (field-by-field DDL is a **5c deliverable**):

- **Identity/context:** `user_id`, `entry_date`, `instrument`, `session`, `mode`.
- **Model:** `entry_model` (FK/enum → the 7 entry models + unified) — the expectancy-grouping key.
- **Decision-flow capture (the model-aligned part):** `draw_on_liquidity`, `range_position`
  (discount/EQ/premium), `swing_qualification` (0/1/2 — the double-qualified-swing score, **R2**),
  `seq_smt_confirmed` (HTF, bool), `triad_smt_confirmed` (LTF, bool), `aura_asset_leg` (optional 6S, **R7**),
  `time_window_valid` (bool), `entry_pda` (default FVG/iFVG per **R4**).
- **Execution/risk:** `entry_price`, `stop_price`, `target_price`, `rr_planned`, `position_size`/`risk_pct`,
  `exit_price`, `r_multiple`, `outcome`, `mae`, `mfe`.
- **Frontier stack (watch-only tags):** `confluence_tags` (TEXT[] — which WHERE/WHEN/DIRECTION/CONFIRM filters
  aligned; for study, **never** gate-eligible).
- **Review:** `plan_followed`, `mistake_tags` (TEXT[], GIN), `grade`, `notes`, screenshots (deferred).

*(Optional, deferred: a `missed_trades`-style surface per [[concepts/architecture/trade-schema]] §Missed
Trades — the Aura canceled-order edge. Not core to 5a.)*

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

- **5b — Scaffold.** Create the `neurospect-learn` repo (app + api); lift the frontend spine + backend
  skeleton; Discord OAuth working end-to-end; app shell + nav + protected routes.
- **5c — Data model + migrations.** `concepts` + `concept_progress` + `journal_entries` + `content_pages`;
  Alembic migrations; seed `concepts` from the U0–U6 taxonomy; **finalize the model-aligned journal field set**.
- **5d — Content API + ingest + browser/reader.** Ingest job; content endpoints; `/library` + `/concepts`
  (markdown render, wikilink resolver, TIER/label badges, search).
- **5e — Progress tracker.** `/path` + `/path/:stage` + concept-progress editing (ladder/confidence/reps) +
  `/drills`.
- **5f — Journal + expectancy.** Model-aligned `/journal` (backtest|live) + `/expectancy` dashboard.
- **5g — Gate/readiness.** `/gate` computed readiness + watch-only enforcement.

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
