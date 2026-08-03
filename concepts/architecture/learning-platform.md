---
tags: [architecture, frontend, backend, learning-platform, mastery, neurospect, phase5]
aliases: [Learning Platform Architecture, neurospect-learn, Learn App, Learning Platform Frontend]
sources: [processes/distributed-workflow/active/learning-platform-ui.md, concepts/mastery/README.md, concepts/mastery/unified/learning-path.md, concepts/mastery/unified/tracker.md, concepts/architecture/phase3-frontend-structure.md, concepts/architecture/phase2-project-structure.md, concepts/architecture/trade-schema.md]
created: 2026-07-18
updated: 2026-07-29
---

# Learning Platform — Architecture (Phase 5a design)

Canonical design doc for **`neurospect-learn`**, a **new, standalone** Learning Platform app that (a) surfaces
all Neurospect course content in a navigable layout and (b) tracks Paul's progress across three axes —
**learning exercises → backtesting → live trading** — graded on the **existing** mastery ladder / confidence
scale / Readiness-to-Live Gate defined in [[concepts/mastery/README]]. It is the delivery layer over the
[[processes/distributed-workflow/active/mastery-layer|Mastery Layer]] content (complete).

> **The Phase 5 arc is COMPLETE (5b → 5g shipped 2026-07-19 → 2026-07-24), and Phase 6 closed its debt
> (2026-07-25).** The app lives at
> `C:\Users\PaulRussell\repos\neurospect-learn` (`app/` + `api/`). Per [[CLAUDE]] §Architecture Doc Integrity the
> **code is ground truth**; this doc describes it *as implemented* — see the per-phase as-built sections
> (§5b · §5c · §5d · §5e-1 · §5e-1b · §5e-2 · §5e-3 · §5f · §5g · §6) for every divergence from the original design.
> Shipped: the scaffold + Discord auth (5b); the data model, 8 enums and Alembic `0002`/`0003` (5c); the content
> API + ingest + `/library`·`/concepts/:slug` (5d); the progress layer, stage exit-bars, `drills` +
> `drill_progress` (`0004`) (5e-1); the three-track curriculum — `/path` switcher + `/path/:track/:stage` as a
> Read → Drill → Track → Gate unit, `track_stages` + `cross_refs` (`0005`) (5e-1b); the Study Planner engine
> (`study_preferences` + `plan_items`, `0006`, the deterministic `scheduler`) (5e-2) and its
> `/today`·`/plan`·`/plan/setup` UI (5e-3); the model-aligned `/journal` + `/expectancy` dashboard (5f); and the
> computed, non-overridable `/gate` verdict + `gate_attestations` (`0007`) (5g); and the Phase-5 debt — stage exit
> bars wired to that evidence, the missed/canceled-trade log + opportunity cost in R, and `position_size`
> (`0008`) (6). **Every route in the taxonomy is
> implemented — no stubs remain.** **The learning-platform-ui workstream is CLOSED.**
>
> **Migrations are at `0010` as of 2026-08-02; seeds are 74 concepts / 23 track stages / 58 drills /
> 67 content pages, plus 44 rubrics / 104 rubric items.** The successor workstream
> [[processes/distributed-workflow/active/learning-enforcement]] shipped **Phase E2 (evidence layer)**, which
> closed the last two deferrals on this page (journal screenshots · `missed_trade_screenshots`) and **changed a
> shipped contract: `reps` is now DERIVED from uploaded evidence, not a writable integer**; then **Phase E3
> (rubrics + self-check)**, which added `rubrics`/`rubric_items` (Alembic `0010`) projected from the two wiki
> exercise libraries. Any statement below that treats `reps` as user-settable is superseded — canonical is
> [[concepts/architecture/learning-enforcement]] §E2 as-built / §E3 as-built.
>
> **The drill count moved 53 → 58 on purpose** (E3's content pass added the five aura Stage-0 drills the aura map
> table had always omitted, which `seed_drills.py` had been reporting as orphan refs). Earlier statements of
> "53 drills" on this page describe the pre-E3 seed.

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

## Multi-track path redefinition (Paul, 2026-07-20 — supersedes the single-path §Route taxonomy)

> **Decision (post-5e-1).** The path is **three first-class graded tracks, not one** — an **Aura** track, an
> **AXL/MrWitness (ict_course)** track, and the **Unified** track (the reconciliation, now framed as the advanced
> track). Each has its **own** graded concepts, its **own** stages, its **own** drills, and its **own** per-user
> progress; a concept taught by both mentors is **duplicated on purpose** (more reps + a second explanation in a
> different voice). Equivalent concepts across tracks carry **cross-links** (soft refs), surfaced as "Also taught
> in: …" so the user can jump to another track's take on the same idea. The 5e-1 `/path` becomes the Unified
> track; **5e-1b** (see §Implementation split) adds the Aura + AXL tracks + the track switcher + reshapes each
> stage into a **curriculum unit** (Read → Drill → Track → Gate). Rationale: the single unified spine read as a
> bare progress grid with no read/drill affordance; per-track curricula match how the mentors actually teach and
> how Paul wants to learn. The wiki's per-track paths ([[concepts/mastery/aura/learning-path]] +
> [[concepts/course/README]]) are the seed source — **consumed/linked, never restated**.

### Multi-track data model (5e-1b — as-built 2026-07-21)

> **As-built.** Shipped in `neurospect-learn` (Alembic `0005_multi_track`, `models/{concept,track_stage}.py`,
> `scripts/{seed_concepts,seed_tracks,seed_drills}.py`, `services/stages.py`, `routers/learning.py`). **Code is
> ground truth.** Confirmed decision: `track_stages` is **metadata only (no `concept_slugs`)** — a stage's
> concepts and drills are resolved by GROUPING on `concepts.(track, stage_code)` and `concept.drill_refs`, not by
> a denormalised array (avoids drift). See §5e-1b as-built for counts + divergences.

Approach: **per-track concept rows** (no shared spine). Reuses the 5c/5e-1 conventions; extends `concepts`.

- **`concepts` gains** `track` (VARCHAR CHECK `aura|ict_course|unified`; the 41 existing rows → `unified`),
  `stage_code` (generic per-track stage, e.g. `A1`/`M2`/`U1`), `stage_order` (SMALLINT), and `cross_refs`
  (TEXT[] — equivalent concept slugs in the *other* tracks). `u_stage` becomes **nullable** (unified-only; still
  drives the frontier CHECK + `content_pages` + the unified exit bars). Per-track slugs are distinct
  (`aura-swing-points` vs `ict-liquidity-swings` vs `u1-1-liquidity-draw`).
- **`track_stages`** — new seed table (no soft-delete, like `concepts`/`drills`): `track`, `stage_order`,
  `stage_code`, `title`, `summary`, `gate_text` (the descriptive exit bar from the learning-path page), UNIQUE
  `(track, stage_code)`. Holds the stage metadata `/path` renders.
- **Seed** grows 41 → ~72: keep the 41 unified (set `track='unified'`, backfill `stage_code`/`stage_order` from
  `u_stage`); author ~14 Aura + ~17 AXL concepts from `aura/learning-path.md` + `course/README.md` (+ the two
  `exercises.md` for drills), with `content_slug`/`drill_refs`/`is_core`/`rep_target`/`cross_refs` per row; author
  `track_stages` (~7 Aura + ~9 AXL + 7 Unified). Drills re-point `concept_slugs` to their own track's concepts.
- **`stages.py` generalizes**: a stage's gate = its `is_core` concepts at Can-mark (+ conf≥3, reps≥target where
  the track's page specifies), computed from `track_stages.concept_slugs` + concept flags — **not** hardcoded per
  U-stage. Unified keeps its exact U0–U4 rules; Aura/AXL use the generic rule + their `gate_text`. Still computed,
  never stored; still `auto_met`/`met`/`locked`.
- **Progress stays per-track** (separate `concept_progress` rows per track's concepts); the enforcement + the
  watch-only cap are unchanged. Cross-links are display-only (never merge progress).

## Route / page taxonomy

> **Multi-track — as-built (5e-1b, 2026-07-21).** `/path` is a **track switcher** (Aura · AXL · Unified;
> default Aura, persisted in `localStorage`) → the selected track's gated stage spine; a stage lives at
> `/path/:track/:stage` as the **curriculum unit** (Read → Drill → Track → Gate). The rows below are the shipped
> shape. **Code is ground truth** (`app/src/pages/{path,stage-detail}.tsx`).
>
> **Planner routes — as-built (5e-3, 2026-07-23).** `/today` (prescriptive ordered daily card list + streak /
> adherence / pace), `/plan` (custom CSS-grid month calendar + regenerate), `/plan/setup` (availability &
> preferences form) shipped, wired to the 5e-2 planner API. Nav gains **Today** (top) + **Plan**. `/` still
> redirects to `/path`. **Code is ground truth** (`app/src/pages/{today,plan,plan-setup}.tsx`).
>
> **Journal + expectancy — as-built (5f, 2026-07-24).** `/journal` (list + `mode`/`entry_model`/`instrument`
> filters + "New entry"), `/journal/new` + `/journal/:id` (one tabbed `JournalForm` — create/edit; delete is a
> two-step inline confirm, no native dialog), `/expectancy` (summary tiles + expectancy-by-model + win-rate
> backtest-vs-live + R-distribution charts + a per-model table). Journal + Expectancy were already in the nav
> (5b). **Code is ground truth** (`app/src/pages/{journal,journal-entry,expectancy}.tsx`).
>
> **Gate — as-built (5g, 2026-07-24).** `/gate` ships the computed per-model verdict: an overall banner, a
> `GateSignal` card per entry model (cleared / not-cleared + the three source pills + backtest n / expectancy /
> win-vs-break-even + the blocking list), the selected model's `GateChecklist`, a "credit progress from" selector
> (restricts which track may satisfy a concept requirement — **can only tighten**), and an explicit
> "Frontier — never gate-eligible" panel. Gate was already in the nav (5b). **This completes the route taxonomy:
> no route is a stub any more** (`pages/stub.tsx` was deleted). **Code is ground truth** (`app/src/pages/gate.tsx`).
>
> **Missed-trade log — as-built (6b, 2026-07-25).** `/journal` became **two tabs** — *Trades taken* and *Missed &
> canceled* — with `?tab=missed` in the URL so the view is linkable; the missed tab leads with the
> opportunity-cost panel, then filters, then the log. Its form lives at `/journal/missed/new` +
> `/journal/missed/:id` (two static segments, so they rank above `/journal/:id`). **No new nav item** — this is
> journaling, and the north star says the journal covers every trade *including the ones you didn't take*.
> **Code is ground truth** (`app/src/pages/{journal,missed-trade-entry}.tsx`).

| Route | Page | Surfaces |
|---|---|---|
| `/path` (home) | **Track switcher + the selected track's spine** — Aura · AXL · Unified; each an ordered, gated list of stages with per-stage progress rings | the three learning-paths |
| `/path/:track/:stage` | **Stage curriculum unit** — Read (content links) → Drill (the stage's drills) → Track (its concepts' progress) → the stage's Gate | learning-path + tracker |
| `/library` | **Content browser** — course modules · entry models · unified playbook · aura · frontier; searchable | all content |
| `/concepts/:slug` | **Content reader** — rendered markdown + **TIER / label badge** + a "track this" panel + "Also taught in" cross-links | any content page |
| `/drills` | **Exercise tracker** — the two drill libraries with ✋ hand-mark / 🛠 tool variants + rep counters + mark-complete | aura/ict-course exercises |
| `/today` | **Study Planner — Today view** (the differentiator) — the prescriptive ordered daily card list + streak / adherence / days-behind + U0 habits; mark each item done → feeds progress | planner (new data) |
| `/plan` | **Study Planner — calendar** — month/week grid: past frozen (done/skipped), today, future projected; "regenerate" | planner (new data) |
| `/plan/setup` | **Availability & preferences** — per-weekday minute budget + max-session + timezone + blackout dates + optional (pacing-only) target go-live date | planner (new data) |
| `/journal` · `/journal/new` · `/journal/:id` | **Model-aligned journal** — log entries with a `backtest \| live` mode toggle; list + filters. Two tabs (6b): *Trades taken* · *Missed & canceled* | (new data) |
| `/journal?tab=missed` · `/journal/missed/new` · `/journal/missed/:id` | **Missed-trade log (6b)** — the setups you didn't take + the opportunity-cost-in-R panel; never enters expectancy or the gate | aura/journaling-system |
| `/expectancy` | **Expectancy dashboard** — per-model win rate / avg R / expectancy / sample; backtest vs live (Recharts) | (new data) |
| `/gate` | **Readiness view** — computed "cleared to live?" signal per model + the Gate checklist | mastery/README §Gate |
| `/library` | **Content browser** — course modules · entry models · unified playbook · aura · frontier; searchable | all content | all |
| `/concepts/:slug` | **Content reader** — rendered markdown + **TIER / label badge** + a "track this" panel (ladder position, edit) | any content page | all |
| `/drills` | **Exercise tracker** — the two drill libraries with ✋ hand-mark / 🛠 tool variants + rep counters + mark-complete | aura/ict-course exercises | U0–U4 |
| `/today` | **Study Planner — Today view** (the differentiator) — the prescriptive ordered daily card list + streak / adherence / days-behind + U0 habits; mark each item done → feeds progress | planner (new data) | current unlocked |
| `/plan` | **Study Planner — calendar** — month/week grid: past frozen (done/skipped), today, future projected; "regenerate" | planner (new data) | current unlocked |
| `/plan/setup` | **Availability & preferences** — per-weekday minute budget + max-session + timezone + blackout dates + optional (pacing-only) target go-live date | planner (new data) | — |
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
  `CHECK 1–4`), `confidence` (SMALLINT, `CHECK 1–5`), `reps` (int, default 0 — **renamed `legacy_reps` in
  `0009`; the API's `reps` is now DERIVED as `legacy_reps + Σ evidence_assets.reps_claimed`**),
  `last_practiced`, `notes`.
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
  framing — expectancy is computed in R, not dollars), **`position_size`** (contracts/lots, nullable — added in
  **6c**, `NUMERIC(10,2)`; **record-keeping ONLY**: no expectancy, analytics or gate computation reads it),
  `exit_price`, `r_multiple`, `outcome` (`outcome` enum), `mae`, `mfe`.
- **Frontier stack (watch-only tags):** `confluence_tags` (TEXT[], GIN — which WHERE/WHEN/DIRECTION/CONFIRM
  filters aligned; for study, **never** gate-eligible).
- **Review:** `plan_followed`, `mistake_tags` (TEXT[], GIN), `grade` (`grade` enum a_plus/a/b/c), `notes`.

**The 5c deferred list — closed in Phase 6 (2026-07-25), except screenshots:**

- ~~`position_size` / dollar sizing~~ → **shipped in 6c** (above). Expectancy stays R-based; the column is
  record-keeping and is read by nothing that computes.
- ~~the Aura canceled-order `missed_trades` surface~~ → **shipped in 6b** as its own table (see
  §Missed-trade log below).
- ~~**Screenshots / uploaded evidence: still deferred, deliberately.**~~ → **CLOSED in Phase E2 (2026-07-28).**
  The deferral held for exactly the reason it was made: it is the same primitive verified drill grading needs, so
  E2 built **one** polymorphic `evidence_assets` layer (Alembic **`0009`**) that the journal, the missed-trade log,
  drills and concepts all attach to via a `subject_type` discriminator — no per-owner child table, no duplication.
  The journal's captures live at `/journal/:id` §Screenshots. Canonical:
  [[concepts/architecture/learning-enforcement]] §7 + §E2 as-built.
  **Note:** journal evidence is a **record, not a rep** — it carries no rep credit and provably does not move
  expectancy or the Gate.

### 2b. Missed-trade log (6b, as-built 2026-07-25) — the trades you did NOT take

**`missed_trades`** (Alembic **`0008`**, `api/app/models/missed_trade.py`) — a **separate lightweight table**, not
columns on `journal_entries`, so executed-trade analytics are never diluted by trades that were never taken.
Adapted from [[concepts/architecture/trade-schema]] §Missed Trades (read + adapted, **not** edited — that doc
describes the older `neurospect-app` `trades` schema) to this app's model-aligned conventions:

- **Adapted:** `entry_model` (the learn app's grouping key, NOT NULL) replaces that doc's `setup_type`;
  `entry_date` replaces `trade_date` (matching `journal_entries`); `rr_planned` added so a planned R:R can be
  recorded with the plan you didn't take.
- **As specified:** `miss_type` (`almost_took|hesitated|canceled` — `canceled` is Dante's category), `reason`,
  `hesitation_tags` (TEXT[], GIN), `planned_entry`/`planned_stop`/`planned_target`,
  `hypothetical_outcome` (`would_win|would_lose|would_breakeven|unknown`), `hypothetical_r`, `narrative`, `notes`.
  Two new enums (`miss_type`, `hypothetical_outcome`); `session_type` + `entry_model` reused from 0003.
  User-scoped + soft-deleted + `update_updated_at()` trigger; partial indexes on (user, date), (user, model),
  (user, miss_type) + a GIN on the tag array.
- **Provenance** is canonical in [[concepts/aura/journaling-system]] (aura-05) — reused by reference, not restated.
- **`missed_trade_screenshots` — the omission is now CLOSED (Phase E2, 2026-07-28), and not by building it.**
  6b deliberately left out the child table [[concepts/architecture/trade-schema]] §Missed Trades specs, because
  user-uploaded evidence was the learning-enforcement workstream's to shape. E2 shaped it as ONE polymorphic
  `evidence_assets` table (Alembic **`0009`**), so a miss's captures attach via `subject_type='missed_trade'` at
  `/journal/missed/:id` §Screenshots and **no `missed_trade_screenshots` table exists or will**. Canonical:
  [[concepts/architecture/learning-enforcement]] §7 + §E2 as-built. See §Contradiction flag — `trade-schema.md`
  still specs the child table and belongs to another lane.
- **The analytic it exists for:** opportunity cost in R, in the pure `api/app/services/opportunity_cost.py` →
  `GET /api/analytics/missed-summary`. `forgone_r` (Σ positive R) vs `saved_r` (Σ |negative R|) vs `net_r`;
  **a negative `net_r` means standing down was PROTECTIVE** — the sign carries the whole insight. Sliced by
  `miss_type`, by `hesitation_tags` (ranked by frequency — the recurring hesitation to attack first) and by
  `entry_model`. A miss with no `hypothetical_r` is counted as logged but never enters a sum.
- **Invariant (proven, not asserted):** nothing here reaches `services/expectancy.py` or `services/gate.py`.
  `/api/analytics/expectancy|summary|r-distribution` and `/api/gate` load `journal_entries` only, and the
  frontend's `missedKeys` subtree deliberately does **not** invalidate `analyticsKeys`. See §6 as-built for the
  byte-identical before/after evidence.

### 3. The gate (computed, not stored)

> **As-built (Phase 5g shipped 2026-07-24).** `GET /api/gate` is live; the verdict is computed by the pure
> `api/app/services/gate.py` on every read and is **not stored** — there is no `cleared` column and no endpoint
> that sets one. The only new persistence is `gate_attestations` (Alembic **`0007`**) for source (c). **Code is
> ground truth** (`api/app/{services/gate.py,routers/gate.py,schemas/gate.py,models/gate_attestation.py}`;
> `app/src/{pages/gate.tsx,components/gate/*,lib/gate.ts}`). See §5g as-built for the decisions.

`GET /api/gate` computes readiness **per model** by combining all three sources — it does not duplicate the
Gate text, which is canonical in [[concepts/mastery/README]] §Readiness-to-Live Gate:

- **(a)** every **core** concept (U1–U4) at **Backtested+** (from `concept_progress`); load-bearing few at Live-ready.
  **As-built:** the requirement set is anchored on the **unified** curriculum (the only track whose taxonomy
  enumerates all seven entry models, as U3.2a–g) — the shared core is its 10 `is_core` U1–U4 concepts at
  **Backtested+ (ladder ≥3)**, and the model's own entry-model concept is the load-bearing one at
  **Live-ready (ladder 4)**. Progress on another track still counts via `cross_refs` equivalents.
- **(b)** `mode='backtest'` sample ≥ target (≥50 setups / ≥100 trades) with **positive expectancy in R** per
  model — expectancy `= (win% × avg win R) − (loss% × avg loss R)`, break-even `= 1/(1+R:R)`
  (see [[concepts/aura/risk-management]]). **The expectancy math is shipped as of 5f** (the pure
  `services/expectancy.py` + `/api/analytics/expectancy`, surfaced on `/expectancy`) and 5g **REUSES it
  verbatim** — the gate router calls `expectancy.compute_groups` exactly as the analytics router does, and
  reimplements nothing. **As-built:** three requirements — sample ≥50 closed backtest trades, expectancy
  strictly `> 0`, and win rate ≥ break-even for its planned R:R. The README's "ideally ≥100" is surfaced as a
  non-gating stretch marker. See §5f + §5g as-built.
- **(c)** the behavioural checklist items — user-attested, stored in `gate_attestations`. **As-built: all four**
  README items (risk precommitted in writing · a demo/sim track record · journaling habit · circuit-breaker
  demonstrated), per-user (behaviour belongs to the trader, not a model) and revocable.

**Invariants (enforced server-side in `services/gate.py`, not merely in the UI):** no frontier (U5 / watch-only)
concept is ever a requirement **or** a source of cross-ref credit; a model is never cleared without the required
sample **and** positive expectancy; live-eligibility is gated on the established playbook (U1–U4), never on
unbacktested confluence (`confluence_tags` are unread by the gate). Attesting (c) can never satisfy (a) or (b),
and a missing/unseeded concept **fails closed** (an unmet requirement) rather than vanishing from the checklist.

### 4. Study Planner + progress-editing (Phase 5e)

> **As-built: 5e-1 + 5e-2 shipped; only the planner UI (5e-3) remains design.** The `concept_progress`
> lifecycle, the `drills` catalog, `drill_progress`, and the stage exit-bar derivation below **shipped in Phase
> 5e-1 (2026-07-20)** — Alembic **`0004`** (`drills` + `drill_progress` + the `drill_variant` enum), models under
> `app/models/`, seed `scripts/seed_drills.py`, services `app/services/{rep_targets,stages}.py`, router
> `app/routers/learning.py`. The `study_preferences` + `plan_items` tables **shipped in Phase 5e-2 (2026-07-22)** —
> Alembic **`0006`** (+ the `plan_activity`/`plan_item_status` enums; `drill_variant` reused from 0004), models
> `app/models/{study_preferences,plan_item}.py`, the pure `app/services/scheduler.py`, router
> `app/routers/planner.py`. **Code is ground truth** (see §5e-1 + §5e-2 as-built for divergences). Conventions
> reuse [[concepts/architecture/trade-schema]] §Schema Conventions (UUID PK · TIMESTAMPTZ · `updated_at` trigger ·
> user-scoped · soft-delete + partial unique `WHERE NOT is_deleted`) exactly as `concept_progress` (5c) does.

The planner reads `concepts` + `concept_progress` (unchanged from 5c; **no columns added**). 5e-1 added two
tables (`drills`, `drill_progress`) + the `drill_variant` enum; 5e-2 added two more (`study_preferences`,
`plan_items`) + the `plan_activity` (`learn|drill|review|observe|habit|backtest`) / `plan_item_status`
(`pending|done|partial|skipped`) enums (Alembic **`0006`**). New model files are registered in
`app/models/__init__.py` **and** imported in `alembic/env.py`.

- **`concept_progress` lifecycle (5e-1, as-built — the 5c seed populates `concepts` only).** Per-user **lazy
  upsert**: `GET /api/progress` LEFT JOINs `concepts` × the user's rows (untracked → null ladder/confidence);
  `PATCH /api/progress` inserts-or-updates one concept via `on_conflict` on the partial unique index (predicate
  `NOT is_deleted`, matched textually) — **never** pre-seeds rows. Per-user isolation (a second user sees none of
  the first's). Honors the DB `CHECK`s (ladder 1–4, confidence 1–5, enforced again by Pydantic `ge/le`) +
  soft-delete. **Enforcement:** the API rejects a ladder advance to Can-mark+ unless the concept's reps ≥ its
  parsed rep target **and** confidence is set (no self-declared skips); and a **watch-only (U5) concept is capped
  at Can-mark** (observation-only, never live-gate-eligible). **E2 update:** the reps that gate now come from the
  evidence ledger, not the request body — `reps` was removed from `ProgressPatch`/`DrillPatch` and sending it is
  a 422 naming `POST /api/evidence`.
- **`drills` (5e-1, as-built)** — seed/content (no soft-delete, like `concepts`), the drill catalog: `drill_ref`
  (UNIQUE, e.g. `"aura D1-b"`), `track` (a CHECK-constrained VARCHAR `aura|ict_course` — only `drill_variant` is
  an enum in 0004), `stage_code`, `title`, `advances_to`, `rep_target` (freetext, canonical), `concept_slugs`
  (TEXT[] back-link, GIN). Seeded by `scripts/seed_drills.py` parsing the **structured "Drill → concept →
  ladder-stage map" tables** at the foot of [[concepts/mastery/aura/exercises]] +
  [[concepts/mastery/ict-course/exercises]] → **53 drills** (compound refs like `D0-a…e`/`D4-a/b`/`T-01…14`/
  `Stage 7`→`S7` expanded to atomic refs; `concept_slugs` reverse-derived from the concept seed's `drill_refs`).
  Drill *definitions* stay canonical in the wiki; this is a projection of them.
- **`drill_progress` (5e-1, as-built)** — user-scoped, soft-deleted: `drill_ref` (TEXT soft ref, matching the
  `concepts.drill_refs` convention), `reps` → **renamed `legacy_reps` in `0009`**, `hand_done` + `tool_done`
  (the ✋/🛠 variant marks), `last_practiced`, `notes`. `UNIQUE (user_id, drill_ref) WHERE NOT is_deleted`.
- **`evidence_assets` + `evidence_grades` (E2, Alembic `0009`)** — the ONE polymorphic evidence layer serving
  drills, concepts, journal entries and missed trades, and **the only way a rep is created**. DDL, the
  fail-closed subject CHECK, and the storage/key conventions are canonical in
  [[concepts/architecture/learning-enforcement]] §7–8 (linked, not restated here).
- **`rubrics` + `rubric_items` (E3, Alembic `0010`)** — **seed content, not user data**: no soft-delete and no
  user scoping, mirroring `drills`/`concepts`, because a re-seed replaces. One rubric per drill, keyed by a TEXT
  `drill_ref` soft ref, holding one item per ✋/🛠 bullet clause **projected verbatim** from the two wiki exercise
  libraries by `scripts/seed_rubrics.py`. `version` bumps if and only if `content_hash` (a sha256 over the
  projected items) changes, so a historical grade's `rubric_version` still names the bar it was judged against.
  **E3 added NO grading table** — the user's answer is an `evidence_grades` row with `grader='self_check'`, which
  `0009` already provided. Canonical in [[concepts/architecture/learning-enforcement]] §3 + §E3 as-built.
- **`study_preferences` (5e-2, as-built — Alembic 0006)** — user-scoped, soft-deleted, one active row/user
  (`UNIQUE (user_id) WHERE NOT is_deleted`): `timezone` (IANA text, default `UTC`), `mon_minutes … sun_minutes`
  (7 `SMALLINT`, 0 = day off; `CHECK ≥ 0`), `max_session_minutes` (`CHECK > 0`, default 60), `blackout_dates`
  (`DATE[]`), `target_go_live_date` (nullable, **pacing-only**), **`active_track`** (`VARCHAR(16)` `CHECK
  aura|ict_course|unified`, default `aura` — which of the three graded tracks the planner schedules; added in the
  5e-1b reconciliation), `plan_version` (INT, default 1) + `generated_at`.
- **`plan_items` (5e-2, as-built — Alembic 0006)** — user-scoped, soft-deleted; the **frozen** past/today
  assignments (see §Study Planner persist-vs-compute): `plan_version`, `scheduled_date`, `activity`
  (`plan_activity`), `concept_id` (nullable FK → `concepts`), `drill_ref` (nullable soft ref), `drill_variant`
  (nullable, the 0004 enum), `target_qty` + `target_unit` (nullable), `est_minutes`, `status`
  (`plan_item_status`), `done_qty`, `completed_at`, `sort_order`. Index `(user_id, scheduled_date) WHERE NOT
  is_deleted`; partial-unique on `(user_id, scheduled_date, activity, concept_id, drill_ref, drill_variant)
  **NULLS NOT DISTINCT** WHERE NOT is_deleted` to keep daily materialization idempotent (the `NULLS NOT DISTINCT`
  — PG 15+ — makes a concept-less/all-NULL-ref `backtest` item still de-duplicate).

**Stage exit-bar derivation (5e-1, as-built)** — a pure `app/services/stages.py`, **computed never stored**,
encoding the exit bars from [[concepts/mastery/unified/learning-path]] §Stage gate (LINKED as canonical — the
rules are *not* restated here): U0 = U0 concepts ≥ Can-mark + held-habit attest; U1 = all five primitives ≥
Can-mark, conf ≥3, reps ≥ parsed target; U2 = triad + Sequential SMT ≥ Can-mark, conf ≥3; U3 = U3 core + entry
models ≥ Can-mark; U4 = U4 concepts ≥ Can-mark + expectancy/risk-precommit attest. **U5 = observation-only,
never live-gate-eligible; U6 = an attest row that POINTS AT `/gate`** (5g ships the real verdict, but it is
**per model** and a stage is not, so the U6 stage links to the Gate rather than mirroring it — see §5g as-built).
The service exposes **`auto_met`** (objective, concept-based)
distinct from **`met`** (every requirement satisfied) and computes **`locked`** off the *auto_met* chain, so
behavioural evidence can never freeze the curriculum. The `reps ≥ target` check uses the
shared **`app/services/rep_targets.py`** freetext parser (reps/days/sessions/qualitative/habit; conservative,
never invents a target). *Integrity flag:* these rules live in code as the *as-implemented* gate — if
learning-path changes, `stages.py` must be reconciled (per [[CLAUDE]] §Architecture Doc Integrity).

**Evidence wiring (6a, as-built 2026-07-25).** Until 6a the behavioural/empirical rows were emitted
`attest=True, met=False` and could **never** become met — a dead checkbox that teaches the user the process is
theatre. They now grade on evidence that already shipped. `compute_stages(...)` takes an optional
**`evidence: stages.Evidence`** bundle (pure data; loaded by `learning.load_stage_evidence`, so `stages.py` stays
DB-free). Omitting it reproduces the pre-6a result exactly.

- **Behavioural rows → the 5g `gate_attestations` store**, mapped explicitly in **`stages.STAGE_ATTESTATIONS`**
  (keyed `(track, stage_code)`, the `_U2_GATE_SLUGS` idiom): unified **U0** → `circuit_breaker` +
  `journaling_habit`; unified **U4** → `risk_precommitted`; aura **A0** → `circuit_breaker` + `journaling_habit`;
  aura **A5** → `sim_track_record`; aura **A6** → `journaling_habit`; ict_course **M0** → `risk_precommitted` +
  `circuit_breaker`; ict_course **M8** → `journaling_habit`. **ONE source of truth:** the row *reflects* the tick
  made on `/gate` and links there — `/path` never carries a checkbox of its own. Objective journal
  **corroboration** (journaling days · misses logged · live entries) is shown beside a self-attest, exactly as
  `/gate` does, and gates nothing.
- **Empirical rows → the shipped 5f expectancy service**, mapped in **`stages.STAGE_EVIDENCE`**. Where the
  learning-path page NAMES a bar it is encoded verbatim, and nowhere else:
  - unified **U4** = `expectancy_computable` — the page says "**can compute** a trade's expectancy contribution in
    R", so the bar is *computability* (≥1 closed backtest trade). **Not positivity** — this corrects the 5e-1
    label, which over-stated it as "Positive expectancy…".
  - aura **A4** / ict_course **M7** = `backtest_edge` — "≥50 setups … logged with **positive expectancy in R** and
    a known win-rate-with-R:R clearing break-even": all three conditions, with `expectancy.SAMPLE_TARGET` as the
    50 (reused, never re-typed) and the shipped `above_break_even`.
  - unified **U6** = `gate_verdict` — "run the full Readiness-to-Live Gate": the shipped per-model verdict rolled
    up to *at least one model cleared*. A bundle loaded without the verdict reads unmet rather than guessing.
  - Pooling uses the new **`expectancy.compute_pooled(trades, mode)`**, which *delegates* to `compute_groups` over
    a re-labelled copy — a stage is not per-model, but the math is literally the same code path.
- **Where nothing covers the bar, the row stays self-attested and SAYS SO** (`stages.STAGE_UNWIRED`). The only
  such row is ict_course **M6**, whose bar is drill completion (T-01…T-14): its detail names `/drills` and states
  that no gate attestation covers it. Self-declared drill marks were deliberately **not** promoted to stage-gate
  evidence — what makes a drill genuinely done is the subject of
  [[processes/distributed-workflow/active/learning-enforcement]].
- **The lock chain is unchanged.** `auto_met` remains concept-only, so `locked` is byte-identical to 5e-1b for
  every track and progress state (asserted in `tests/test_stages.py` + through the live API). `met` generalized to
  *every requirement satisfied*, which is what lets a concept-less backtest stage finally read "met" once its
  evidence is really in.
- **`/path` and `/today` agree.** The planner also calls `compute_stages`, so `routers/planner.py` passes the same
  bundle (`with_gate=False` — it cannot use the verdict). The scheduler's foundation-habit overlay was always
  written to run "until the gate holds"; before 6a that gate could never hold, so habits recurred forever. They
  now stop exactly when the foundation stage's bar is met. `scheduler.schedule(...)`'s new `evidence=` kwarg
  defaults to None, so the 5e-2 no-DB unit tests are unaffected.

## Study Planner

> **Engine as-built (Phase 5e-2, 2026-07-22); UI as-built (Phase 5e-3, 2026-07-23).** The platform's headline
> differentiator: an **adaptive, gate-aware, retention-aware** daily/weekly study-schedule generator that tells
> Paul exactly what to study/drill *today*, driven by his availability + the chosen track's curriculum + his
> current progress. It **schedules the existing curriculum — it never restates or forks it** (concepts,
> `drill_refs`, freetext rep targets, and the learning-path stage gates are consumed/linked). The pure
> `app/services/scheduler.py` + the `app/routers/planner.py` API shipped in 5e-2 (**code is ground truth** — see
> §5e-2 as-built); the `/today`, `/plan`, `/plan/setup` UI shipped in 5e-3 (see §5e-3 as-built). Data model in
> §Progress + journal data model ("Study Planner + progress-editing"). North star: **discipline & accountability
> by design** — every choice defaults to *enforce the disciplined path* over *let the user decide*.

### Availability / preferences

Entered on `/plan/setup` → `study_preferences` (one active row/user): a **per-weekday minute budget**
(`mon_minutes…sun_minutes`; 0 = off, weekends can be longer), a **max single-session** cap (splits a day's
budget into blocks), **timezone** (load-bearing — "today" and day-of-week matter to the ICT curriculum),
**blackout dates**, and an optional **target go-live date**. The target date is **pacing-only**: it drives the
ETA projection and an on-pace/behind flag but **never advances a gate or unlocks a stage** — the
Readiness-to-Live Gate stays evidence-based ([[concepts/mastery/README]] §Gate).

### Scheduling algorithm (deterministic, gate-aware, retention-aware)

A pure function `schedule(today, prefs, concepts, drills, concept_progress, drill_progress, past_items)` → dated
`plan_items`, in `app/services/scheduler.py` (+ `stages.py`, `rep_targets.py`). **Deterministic + re-runnable**
(strict ordering, no randomness; same inputs → same plan), unit-testable without a DB.

> **As-built reconciliation (5e-2).** The scheduler is **track-scoped** — it schedules `prefs.active_track` only.
> Because unlock reuses the generalized `stages.compute_stages(track, stage_metas, …)`, the shipped signature
> takes an extra `stage_metas` argument: `schedule(today, prefs, stage_metas, concepts, drills, concept_progress,
> drill_progress, past_items, *, horizon_days)` and returns a `ScheduleResult` bundle (`items` + `projected_clear`
> / `projected_go_live` / `on_pace` + `days_behind` / `carried_over` + `unplaced`) rather than a bare list — the
> API needs the adherence/pace surfaces. Foundation-stage concepts get their one-time Learn/Drill backlog **and**
> a recurring daily Habit overlay. Pipeline (unchanged in intent):

1. **Unlock.** Via the exit-bar service, find the highest unlocked stage `S` (first stage whose gate is unmet).
   **Schedulable concepts = stages ≤ S only;** later stages are locked and **never scheduled**. **U5 unlocks only
   after U1–U4 met**, and its work is always observe-only (never "go-live"/backtest-toward-live) — enforced by
   `watch_only`.
2. **Backlog** (ordered by `u_stage`, `sort_order`). Per schedulable concept: untracked → a **Learn** task (read
   `content_slug`); each drill in `drill_refs` below its parsed rep target → **Drill** tasks for the remaining
   reps; `watch_only` (U5) → **Observe** only, capped at Can-mark; U0 concepts → recurring daily **Habit** tasks
   until the U0 gate holds.
3. **Rep-target parsing** (`rep_targets.py`). `rep_target` is freetext ("≥50 ranges", "10 days", "1 week",
   "5 sessions", "score by hand", "—"). Normalize → `reps=N` (count-y) · `days=N` (longitudinal drills spread
   **1 session/day** — the planner respects that daily-bias/PO3 drills are inherently longitudinal and won't cram
   them) · `sessions=N` · `qualitative` (small default; gate on ladder+confidence, not reps) · `habit`/none (U0).
   The freetext stays canonical in the seed; the parser **defaults conservatively and never invents a target**
   (no-drift). *Flag:* an optional future additive seed column (`rep_target_count`/`unit`) would make this
   explicit — recommended, not required.
4. **Spaced review** (mandatory retention guardrail — no off switch). Concepts at ladder ≥ Can-mark get a due date
   from `confidence` + `last_practiced` on a Leitner-style interval ladder (conf 3 ≈ 3d, 4 ≈ 7d, 5 ≈ 21d);
   past-due → short **Review** tasks interleaved into daily plans.
5. **Daily packing** (deterministic). Iterate dates from `today` in the user's tz; skip blackout dates + 0-budget
   weekdays. Per day: budget = that weekday's minutes, each block ≤ `max_session_minutes`; fill order
   (a) U0 habits, (b) due reviews, (c) current-focus backlog in curriculum order, (d) day-based drills get one
   slot/day. Minutes estimated per activity type. Overflow rolls to the next eligible day.
6. **Projection / ETA / pacing.** Continue packing hypothetically to estimate when each future gate (U1..U4)
   clears at current pace → "projected U1 clear", "projected go-live"; compare to `target_go_live_date` if set
   (on-pace/behind — pacing only). Horizon = open-ended to the next gate, coarse projection beyond.
7. **Slippage / carry-over.** Past `plan_items` still `pending` are **re-queued** at the front of today's backlog;
   "N items / N days behind" is surfaced (accountability, not hideable). Missed work is never silently dropped.

### Persist vs compute — hybrid

Preferences **persisted**; the **future schedule computed on read** (pure function of curriculum + progress +
prefs + today); **past + today frozen** into `plan_items`. `GET /api/plan/today` materializes the current date's
computed items once (idempotent via the partial unique index); future calendar days are computed/projected, not
frozen, until their date arrives. Marking an item done/partial/skip updates the item **and** feeds
`concept_progress`/`drill_progress` (**E2: `last_practiced` + the ✋/🛠 mark only — no longer reps**, since a
mark-done that minted a rep would have been a bypass around the evidence layer; `plan_items.done_qty` still
records how much was worked). Net effect — **the past is a fixed accountability
record; the future is always recomputed from current state** — is the elite adaptivity property. `POST
/api/plan/regenerate` bumps `plan_version` and recomputes; frozen past items keep their original version.

### How the planner enforces the north star (per feature)

- **Prescriptive Today** — ordered, not a menu; skipping is logged as a **skip** (hurts adherence), never hidden.
- **Gated progression** — locked stages never scheduled; ladder-advance blocked until reps ≥ target + confidence
  set; no manual gate override; U5 never live-eligible.
- **Rep targets enforced** — tracked in `drill_progress`/`concept_progress`; the gate checks reps ≥ parsed target.
- **Accountability surfaced** — streak, adherence %, days-behind, carried-over items: visible, not hideable.
- **Spaced review mandatory** — no off switch. **U0 habits recur daily** until the held-habit gate (prerequisite
  to size). **Missed work re-queued**, never dropped. **Frontier watch-only** enforced in the scheduler.
  **Target date pacing-only** — never advances the evidence gate.

## Component structure + API surface

- **Progress components (5e-1, as-built):** `StagePath`/`StageNode` (SVG progress ring + locked/watch-only),
  `ExitBarGate`, `LadderBadge` (1–4), `ConfidenceRating` (1–5), `RepCounter`, `ConceptTrackPanel` (on the reader
  + on `/path/:stage`), `DrillCard` (✋/🛠). Under `components/{progress,drills}/`. Plus the already-built
  `TierBadge`/`LabelBadge`/`MarkdownRenderer` (5d).
- **Planner components (5e-3, as-built):** `TodayList`/`PlanItemCard` (activity icon + concept/drill title +
  target + est-minutes + done/partial/skip → `useUpdatePlanItem`; carried-over + status styling; computed future
  items render read-only), `StudyCalendar` (the **lightweight custom CSS-grid month calendar** using `date-fns` —
  *not* `react-day-picker`, which was never added; a Mon-first grid with per-day status dots, today ring-highlit,
  past frozen / future projected, + a Regenerate button + an `unplaced` warning), `AvailabilityForm` (RHF + Zod),
  `StreakBadge`/`AdherenceMeter`/`PaceProjection`. Under `components/planner/`. See §5e-3 as-built.
- **Journal components (5f, as-built):** `JournalForm` (tabbed RHF+Zod — mode toggle + Context / Decision-flow /
  Execution&risk / Review; optional numbers held as strings + coerced on submit; enum selects use a `__none__`
  sentinel; `confluence_tags`/`mistake_tags` are local-state chip inputs), `JournalCard` (mode-color-coded badge +
  R/outcome), `JournalFilters` (mode/model/instrument). Under `components/journal/`.
- **Analytics components (5f, as-built):** `ExpectancyChart` (per-model expectancy in R, grouped backtest/live,
  zero reference line), `BacktestVsLiveChart` (per-model win-rate %, backtest vs live — the honesty view),
  `RDistributionChart` (R histogram, an addition beyond the two named), and `chart-common.tsx` (validated 2-hue
  categorical palette [blue backtest / orange live] as `--chart-*` CSS vars in `index.css`, a theme-aware
  `ChartTooltip`, `EmptyChart`). Under `components/analytics/`. **`recharts` re-added** (dropped in the 5b lift).
- **Gate components (5g, as-built):** `GateSignal` (one model's cleared/not-cleared signal — the three source
  pills, backtest n / expectancy / win-vs-break-even, and the blocking list; no control that could mark it
  cleared) and `GateChecklist` (the three source groups with per-group `met/total`; concept + evidence rows are
  read-only *earned* rows carrying their `detail` and a "work it" link to `/path/:track/:stage`, while the four
  behavioural items are the page's **only** writable control — a server-controlled Radix checkbox, deliberately
  not optimistic, above a corroboration strip of objective journal facts). Under `components/gate/`.
- **Missed-trade components (6b, as-built):** `MissedTradeForm` (RHF+Zod; a miss-type segmented control —
  *Almost took it* · *Hesitated at the trigger* · *Canceled a working order* — the plan you didn't take, and the
  hypothetical outcome/R; `hesitation_tags` is a chip input with the trade-schema vocabulary offered as one-click
  suggestions, still freeform), `MissedTradeCard` (dashed border to read as "not taken"; R coloured by MEANING —
  amber *forgone* for positive, emerald *saved* for negative — and `unresolved` when there is no R yet),
  `MissedFilters` (miss type / model / hypothetical outcome / instrument), `OpportunityCost` (the three tiles —
  Forgone · Saved by standing down · Net, with the net's verdict in words — plus by-miss-type / by-hesitation-tag /
  by-entry-model chip rows and the "never enters expectancy or the Gate" line). Under `components/journal/`.
- **Evidence components (E2, as-built 2026-07-28):** `EvidenceCapture` (`components/evidence/`) — the
  **paste-first** capture zone: a focus-scoped `paste` handler reading `ClipboardEvent.clipboardData.files` so
  `Ctrl+V` from a TradingView snapshot works, plus drag-and-drop and a file input as fallbacks; thumbnails with
  their rep claim, an inline **rejection reason**, and a flagged marker. Wired into `DrillCard`,
  `ConceptTrackPanel`, `/journal/:id` and `/journal/missed/:id` (the last two with `showRepsClaimed={false}` —
  a trade screenshot is a record, not a rep). `RepCounter` became **read-only** and now shows the
  derived/evidenced/pre-evidence split; its +/− control is gone, because a rep is no longer a number you type.
  `lib/evidence.ts` holds `evidenceKeys` + `useEvidence`/`useUploadEvidence`/`useDeleteEvidence`, and — unlike
  `missedKeys` — **a write invalidates `learningKeys.all` AND `plannerKeys.all`**, since evidence moves reps and
  the schedule is computed from reps still owed.
- **Self-check components (E3, as-built 2026-08-02):** `SelfCheck` (`components/evidence/self-check.tsx`) — one
  per captured asset, rendering **the drill's own wiki bullets as checkable items**. Collapsed it shows either the
  recorded verdict (*Meets the bar* / *Partly met* + %) or, when never checked, "not checked yet — the reps still
  count"; expanded it lists the rubric items with a ✋/🛠 icon per item, cites the source wiki path, warns when the
  last check was against an older `rubric_version`, and offers a rubric picker when a concept's bar spans several
  drills. `RubricText` renders the wiki's markdown emphasis rather than restating the words — **no criterion text
  exists in the frontend**. `EvidenceCapture` gained an `unchecked` count ("N awaiting your check") and switched to
  a per-capture ROW layout when a bar exists. `lib/rubrics.ts` holds `rubricKeys` + `useRubricCatalog`/`useRubrics`
  + `useSelfCheck` and the grading-state helpers; a self-check invalidates **only** `evidenceKeys.all` — not
  `learningKeys`/`plannerKeys` — because a grade deliberately moves no rep.
- **E3 perf note — two N+1 query fixes:** `/drills` mounts an `EvidenceCapture` per drill (58 of them), and both
  `useEvidence` and the first cut of `useRubrics` keyed per subject, so a single page load fired **~116**
  near-identical requests, saturated the browser's 6-connection-per-origin limit and queued the user's own upload
  behind the pile. Both now fetch **once** under a shared query key (`useEvidenceCatalog` / `useRubricCatalog`) and
  slice client-side; a concept's bar resolves from `ProgressRow.drill_refs`, which the row already carried. The
  server-side `subject_type`/`drill_ref`/`concept_id` filters are unchanged and still used. Measured effect: the
  Playwright suite went from ~47s to ~31s.
- **6a note — `ExitBarGate` rewritten:** three row kinds now read differently because they are graded differently.
  Concept rows unchanged; **derived** rows are tagged *earned* / *from your log* and carry the numbers (Σ glyph
  when unmet — objectively short, not "pending a declaration"); **attested** rows link to `/gate` and say
  "attested on the Gate" / "attest it on the Gate once it is true" with their corroboration. The blanket
  "(self-attested)" suffix is gone, and the stage header's pending hint links to `/gate`. `StagePath` now reads
  "graded on your logged evidence" for a concept-less stage instead of "0/0 at Can-mark+".
- **Infra note (5e-1, as-built):** the progress/drill mutations are the **first `useMutation`s in this codebase**
  (5b–5d were read-only) — `lib/learning.ts` establishes `learningKeys` + `useUpdateProgress`/`useUpdateDrill`
  with `onSuccess: invalidateQueries` (a progress write also invalidates `stages`), following the `contentKeys`
  hierarchical-key convention in `lib/content.ts`; `useUpdateProgress` surfaces the server's 422 gate message.
  Added the shadcn `progress` primitive (`components/ui/progress.tsx`, Radix). **Fixed the `dark:` mismatch**
  (media-based variant vs class-based theme, §5d as-built) by adding `@custom-variant dark (&:where(.dark,
  .dark *))` to `index.css`.
- **New endpoints (separate API):**
  - `auth`: `POST /auth/discord/token`, `GET /auth/me`, `POST /auth/debug/token` (debug-gated).
  - `content`: `GET /api/content/pages`, `/pages/{slug}`, `/search`.
  - `learning` (5e-1, as-built — `app/routers/learning.py`, prefix `/api`, auth-gated + user-scoped):
    `GET /api/concepts` (`?stage=`), `GET|PATCH /api/progress`, `GET /api/stages`,
    `GET /api/drills` (`?track=`/`?stage=`), `PATCH /api/drills`. Schemas in `app/schemas/learning.py`.
  - `planner` (5e-2, auth-gated, user-scoped): `GET|PUT /api/preferences`, `GET /api/plan/today`
    (materialize+persist today; items + adherence + pace), `GET /api/plan?from=&to=`,
    `POST /api/plan/regenerate`, `PATCH /api/plan/items/{id}` (status + `done_qty` → feeds
    `concept_progress`/`drill_progress`).
  - `journal` (5f, as-built — `app/routers/journal.py`, prefix `/api`, auth-gated + user-scoped, soft-delete):
    `POST /api/journal`, `GET /api/journal` (`?mode=`/`?entry_model=`/`?instrument=`/`?from=`/`?to=`, newest
    first), `GET|PATCH|DELETE /api/journal/{id}`. Schemas in `app/schemas/journal.py`.
  - `analytics` (5f, as-built — `app/routers/analytics.py`, prefix `/api/analytics`, read-only aggregation over
    the user's entries; math in the pure `app/services/expectancy.py`): `GET /expectancy` (by model × mode),
    `/summary` (per mode), `/r-distribution` (R histogram split by mode). No gate verdict (5g owns it).
  - `gate` (5g, as-built — `app/routers/gate.py`, prefix `/api`, auth-gated + user-scoped; verdict in the pure
    `app/services/gate.py`): `GET /api/gate` (`?track=` restricts which track may supply credit — tightens only),
    `GET|PATCH /api/gate/attestations` (the four behavioural items; lazy upsert, revocable). Schemas in
    `app/schemas/gate.py`. **No endpoint writes a verdict** — `cleared` is computed per read.
  - `missed-trades` (6b, as-built — `app/routers/missed_trades.py`, prefix `/api`, auth-gated + user-scoped,
    soft-delete, mirroring `journal.py`): `POST /api/missed-trades`, `GET /api/missed-trades`
    (`?miss_type=`/`?entry_model=`/`?hypothetical_outcome=`/`?instrument=`/`?from=`/`?to=`, newest first),
    `GET|PATCH|DELETE /api/missed-trades/{id}` (PATCH is how a miss gets *resolved* after watching price).
    Plus `GET /api/analytics/missed-summary` on the analytics router (math in the pure
    `app/services/opportunity_cost.py`). Schemas in `app/schemas/missed_trade.py`.
  - `evidence` (E2, as-built — `app/routers/evidence.py`, prefix `/api`, auth-gated + user-scoped, soft-delete):
    `POST /api/evidence` (**multipart** — file + subject + kind + `reps_claimed` + optional `captured_at`/`notes`),
    `GET /api/evidence` (filter by subject), `GET|DELETE /api/evidence/{id}`, and
    `GET /api/evidence/file?token=` — the local storage backend's **signed, key-scoped, expiring** read, the one
    route deliberately not behind `get_current_user` (the token is the authorisation, exactly as an R2 presigned
    URL is). Schemas in `app/schemas/evidence.py`; services `app/services/{storage,evidence_checks}.py`.
    **This is the only endpoint that can create a rep.**
    Plus, added in E3: **`POST /api/evidence/{id}/self-check`** — appends a `self_check` `evidence_grades` row
    carrying the ticked items in `findings` plus `rubric_slug`/`rubric_version`, and returns the asset with its
    full grade history. It **cannot** change a rep count (see §E3 as-built for why retraction is forbidden).
  - `rubrics` (E3, as-built — `app/routers/rubrics.py`, prefix `/api`, auth-gated): **`GET /api/rubrics`** only
    (`?drill_ref=` / `?concept_id=` / `?concept_slug=` / `?track=`, or unfiltered for the whole catalog).
    **Deliberately read-only — POST/PATCH/PUT/DELETE all 405**, so no rubric text can be authored in the app; a
    bar changes by editing the wiki and re-seeding. Schemas in `app/schemas/rubric.py`. Seeded by
    `scripts/seed_rubrics.py`.
  - **Shared loaders (6a):** `routers/learning.py` owns `load_concepts_and_ladder` (all tracks × the user's ladder —
    **moved here from `routers/gate.py`**, which now imports it: gate already depended on learning, so this removes
    a duplicate query rather than adding one) and `load_stage_evidence` (the gate-attestation / pooled-expectancy /
    gate-verdict bundle; `with_gate=False` skips the verdict for the planner). They live in a router, not
    `app/services/*`, because that package is deliberately pure and DB-free.

## Implementation split (5b → 6)

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
- **5e — Progress layer + Study Planner** (redefined 2026-07-20, designed together, three sessions):
  - **5e-1 — Progress foundation.** ✅ **Built 2026-07-20.** `concept_progress` lazy-upsert lifecycle, the derived
    stage exit-bars service (+ the shared `rep_targets` freetext parser), the `drills` catalog (53 rows) +
    `drill_progress` (Alembic `0004`), the `learning` endpoints; frontend `/path`, `/path/:stage`, `/drills`, and
    the `ConceptTrackPanel` on the reader. See §5e-1 as-built below.
  - **5e-1b — Multi-track curriculum.** ✅ **Built 2026-07-21.** Turned the single unified `/path` into **three
    graded tracks** (Aura · AXL · Unified) with a switcher; per-track concepts + `track_stages` (Alembic `0005`) +
    `cross_refs`; generalized `stages.py`; reshaped `/path/:track/:stage` into a **curriculum unit** (Read → Drill
    → Track → Gate). Ships *before* the planner (which schedules the chosen track). **Bumped the planner migration
    to `0006`.** See §5e-1b as-built below.
  - **5e-2 — Planner engine.** ✅ **Built 2026-07-22.** `study_preferences` + `plan_items` (Alembic `0006`), the
    deterministic pure `scheduler` service (reusing the 5e-1 `rep_targets` parser + the generalized `stages.py`),
    and the planner API (preferences, today, calendar, regenerate, mark-item-done → progress). No UI; verified by
    16 tests (9 scheduler unit + 7 API). See §5e-2 as-built below.
  - **5e-3 — Planner UI.** ✅ **Built 2026-07-23.** `/today` (prescriptive ordered daily plan), `/plan` (custom
    CSS-grid calendar + regenerate), `/plan/setup` (availability form); `lib/planner.ts` (query/mutation layer);
    mark-done/partial/skip → feeds progress; streak / adherence / days-behind / pace surfaces. Frontend-only
    (consumes the 5e-2 API). See §5e-3 as-built below.
- **5f — Journal + expectancy.** ✅ **Built 2026-07-24.** Model-aligned `/journal` (backtest|live CRUD +
  filters, soft-delete) + `/expectancy` dashboard (per-model expectancy in R, win rate, backtest-vs-live, R
  distribution, per-model table). Backend `journal` + `analytics` routers over the existing 5c `journal_entries`
  table (no migration); pure `services/expectancy.py`; recharts re-added. See §5f as-built below.
- **5g — Gate/readiness.** ✅ **Built 2026-07-24.** The computed, non-overridable per-model "cleared to live?"
  verdict: the pure `services/gate.py` combining (a) `concept_progress` + (b) the reused 5f `expectancy.py` +
  (c) `gate_attestations` (Alembic `0007`), the `gate` router, and the `/gate` UI (`GateSignal` ·
  `GateChecklist` · frontier panel · credit-track selector). See §5g as-built below.
  **This completes the Phase 5 arc** — every route in the taxonomy is implemented.
- **6 — Phase-5 debt.** ✅ **Built 2026-07-25.** The three scoped follow-ups that **close the
  learning-platform-ui workstream**: **(6a)** the stage exit bars wired to the shipped `gate_attestations` +
  expectancy evidence (no more permanently-unmet rows; the lock chain provably unchanged); **(6b)** the
  missed/canceled-trade log + opportunity cost in R (Alembic `0008`, `services/opportunity_cost.py`, a second tab
  on `/journal`); **(6c)** `position_size` (same migration, record-keeping only). See §6 as-built below.
- **E2 — the evidence layer** (a *different* workstream:
  [[processes/distributed-workflow/active/learning-enforcement]]). ✅ **Built 2026-07-28.** Alembic `0009`;
  `evidence_assets` + `evidence_grades`; the storage service (R2 **or** local, so localhost needs no bucket); the
  deterministic anti-cheat tier; paste-first capture; and **`reps` became derived from the evidence ledger** —
  which is what finally closed the "screenshots deferred" note in §2. Design + as-built are canonical in
  [[concepts/architecture/learning-enforcement]]; this page records only how it changed the shipped surface.

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

### 5e-1 as-built (2026-07-20) — code is now ground truth

Progress foundation shipped and verified end-to-end (see §Progress + journal data model §4 + §Component/API
surface for the shipped shapes). Alembic `0004` (one enum, two tables), two models, one seed, two pure services,
one router, and the `/path`·`/path/:stage`·`/drills` frontend + reader track panel. Decisions made while building
(the calls the design left open):

- **Migration/model.** `0004_drills_progress` created the `drill_variant` enum (`hand|tool`) + `drills`
  (seed/content, no soft-delete) + `drill_progress` (user-scoped, soft-deleted). **`track` is a CHECK-constrained
  VARCHAR, not an enum** — only `drill_variant` is an enum in 0004 (per the design); `drill_variant` is created
  here but consumed by `plan_items` in 0005 (5e-2), so no 0004 column uses it yet. `drills.concept_slugs` gets a
  GIN index; `drill_progress` gets the partial-unique `(user_id, drill_ref) WHERE NOT is_deleted`. Fully
  reversible (verified up/down/up).
- **`seed_drills.py` — projection of the two drill-map tables → 53 drills** (aura 16, ict_course 37). Compound
  cells are **expanded to atomic `drill_ref`s** so they match the `concepts.drill_refs` convention: `D0-a…e`
  (letter range), `D4-a/b` / `D6-a/b/c` (slash suffixes), `T-01…14` (numeric range), `Stage 7`→`S7` (which makes
  London's `"ict-course S7"` ref resolve). `drill_ref` uses the `"ict-course "` hyphen prefix (matching the
  concept seed) while `track` uses the `ict_course` underscore. `concept_slugs` is **reverse-derived in-memory
  from the concept seed's `drill_refs`** (single source of truth, no DB round-trip). The 4 aura Stage-0 drills the
  aura map table omits are **reported as orphan refs** (concepts reference them but they aren't in the map — a
  faithful wiki asymmetry, not invented). Idempotent on `drill_ref` + stale-prune (mirrors `ingest_content.py`).
- **`rep_targets.py`** — a pure freetext→`RepTarget(kind, count)` parser: `reps`/`days`(`1 week`→7)/`sessions`/
  `qualitative`(no floor)/`habit`. Multi-number strings bind the **largest** floor (`"≥5 + ≥50 swings"`→50); a
  number embedded in an identifier (`"Class-2 hw"`, `"Model 2022"`) is **not** treated as a count (lookbehind
  guard) so it defaults to qualitative — it never invents a target.
- **`stages.py`** — the as-implemented exit-bar gate (see §Stage exit-bar derivation). Splits `auto_met`
  (objective) from `met` (incl. self-attest) and locks off the `auto_met` chain so U0/U4's un-wired attestations
  don't freeze the curriculum. The two U2-gating SMT concepts (`u2-2-triad-smt`, `u2-3-sequential-smt`) are named
  explicitly; U3 gates on `is_core` + the `U3.2*` entry-model concepts; frontier U5 is `watch_only` +
  `never_gate_eligible`; U6 is a 5g placeholder.
- **`learning` router — two real fixes caught in verification** (evidence-gated, not inferred): (1) `ON CONFLICT`
  index inference needs the partial-index predicate **textually** — SQLAlchemy's `is_deleted.is_(False)` emits
  `IS false`, which does **not** match the index's `WHERE NOT is_deleted`; fixed with `text("NOT is_deleted")`.
  (2) with `expire_on_commit=False`, re-`SELECT`ing after a Core upsert returned the **stale identity-map row**
  (and `expire_all()` then triggered an async lazy-load / `MissingGreenlet`); fixed by building the PATCH response
  **from the committed values** instead of re-reading. PATCH also enforces the ladder-advance gate (reps ≥ target
  + confidence set) and the watch-only Can-mark cap.
- **Frontend.** `lib/learning.ts` holds the first `useMutation`s (`useUpdateProgress` invalidates `progress` +
  `stages`; `useUpdateDrill` invalidates `drills`). `ConceptTrackPanel` mirrors the server gate client-side
  (`advanceBlocked`) to disable Save + show why. **ExitBarGate shows the true bar status** (`met`/`not met`)
  regardless of lock — the StageDetail page shows a separate "Locked" notice — so a **met-but-locked** stage still
  reads "Exit bar met" (a UX fix surfaced by the e2e). `shadcn add progress` mis-wrote to a literal `@/` folder
  (alias glitch) and was relocated to `components/ui/`. Added `@custom-variant dark` (the §5d-flagged fix).
- **Playwright.** `e2e/learning.spec.ts` adds 4 specs (path spine, reader edit-persist, API-seeded stage exit-bar
  flip, drill-mark persist) under a `serial` describe (they share the one debug user); with the 6 content specs,
  **10/10 green**.

### 5e-1b as-built (2026-07-21) — code is now ground truth

Multi-track curriculum shipped and verified end-to-end. One migration, two model changes, three seeds, a
generalized service, two new endpoints, and the reshaped `/path` + curriculum unit. **Code is ground truth.**

- **Migration `0005_multi_track`** (raw-SQL, mirrors 0002–0004; reuses `update_updated_at()`). `concepts` ADD
  `track` VARCHAR(16) NOT NULL DEFAULT `'unified'` + CHECK `(aura|ict_course|unified)`, `stage_code` VARCHAR(16),
  `stage_order` SMALLINT, `cross_refs` TEXT[]; `u_stage` DROP NOT NULL (unified-only henceforth — still drives the
  U5-core CHECK, which passes on NULL, + the content join + the unified bars). NEW `track_stages` (seed/content, no
  soft-delete): `track`, `stage_order`, `stage_code`, `title`, `summary`, `gate_text`, trigger, UNIQUE
  `(track, stage_code)` — **no `concept_slugs`** (grouping is by `concepts.(track, stage_code)`). **Reversibility
  fix (evidence-gated):** the downgrade clears `concept_progress` rows FK-referencing non-unified concepts *before*
  deleting those concepts and restoring `u_stage NOT NULL`; verified `0001→base→head` up/down/up clean.
- **Seed counts (reported):** `concepts` 41 → **74** (unified=41 backfilled `track='unified'`, `stage_code`=U-stage,
  `stage_order`; **aura=14** A0–A3 concepts; **ict_course=19** M0–M5 concepts). `track_stages` **23** (aura A0–A6=7,
  ict_course M0–M8=9, unified U0–U6=7). `drills` unchanged at **53**. All seeds idempotent (re-run → stable, no
  dupes). Every non-null `content_slug` resolves against the 5d scheme (**0 unresolved**, SQL-verified); every
  `cross_ref` resolves to a concept slug (**0 unresolved**; **44** concepts carry cross_refs).
- **`cross_refs` from `EQUIV_GROUPS`** (in `seed_concepts.py`): equivalence groups list a concept's cross-track
  twins; assignment is **symmetric, never same-track, and validated at build** (an unknown slug raises) — so
  "Also taught in …" always resolves. Never merges progress (display-only).
- **`drills.concept_slugs` re-pointed to same-track** (`seed_drills._build_ref_to_slugs` now keys by
  `(concept.track, drill_ref)`): a drill_ref like `"aura D1-a"` — referenced by both a unified and an aura concept —
  links to the **aura** concept (SQL-verified: **0 cross-track drill links**). Unified-only refs (`"ict-course S7"`,
  tape `T-*`) simply carry no same-track concept.
- **Concept-less stages are faithful, not gaps:** unified **U6**, aura **A4–A6**, ict **M6–M8** (backtest / live /
  journal) carry **no gradable concept rows** — the wiki authors those as drills, not concepts. Their `track_stages`
  metadata + `gate_text` stand alone; `stages.py` emits a single attest placeholder (auto_met False) so the lock
  chain honestly holds them behind the concept work (5f/5g wire the evidence). Their `/path` unit shows the gate
  text + "backtest/journal by reference" notes.
- **`stages.py` generalized.** Unified keeps its **exact** U0–U6 rules (unchanged from 5e-1). Aura/ict use the
  generic rule: **foundation stage** (stage_order 0 — psychology/discipline) = every concept ≥ Can-mark
  (behavioural) + a held-habit attest; **concept stage** = its `is_core` concepts ≥ Can-mark, conf ≥3, reps ≥
  parsed floor (falls back to all concepts if none flagged core); **concept-less stage** = attest placeholder. Lock
  chain: unified keeps its exact chain (U0–U4 on auto_met; U5/U6 on U1–U4); aura/ict use a sequential auto_met
  chain. `compute_stages(track, stage_metas, concepts, progress)` is the new signature (DB-agnostic, unit-testable).
  **Verified:** marking Aura A1's 3 core concepts flips **only** Aura A1 to met — Unified U1 (0/5) and ICT M1 (0/2)
  stay untouched, and the Unified `u1-1` row stays `None` (per-track isolation is real, not shared).
- **Endpoints (`learning.py`).** NEW `GET /api/tracks` → the 3 tracks + per-stage rollups (switcher/spine).
  `GET /api/stages?track=` (default `unified`; 404 on unknown track) → full per-stage requirements. `?track=` added
  to `GET /api/concepts` + `GET /api/progress`. `PATCH /api/progress|drills` unchanged (the watch-only cap + the
  reps≥target/confidence gate still apply). `_compute_track_stages()` is shared by `/tracks` + `/stages`. Schemas:
  `ConceptOut`/`ProgressRow` gained `track`/`stage_code`/`stage_order`/`cross_refs` (`u_stage` now optional);
  `StageOut` split into `StageRollup` (+ `track`/`stage_code`/`summary`/`gate_text`, no `u_stage`) and `StageOut`
  (rollup + requirements); new `TrackOut`.
- **Frontend.** `/path` is a **track switcher** (`TRACKS` = Aura·AXL·Unified; default Aura, persisted in
  `localStorage['neurospect_learn_track']`) rendering the selected track's `StagePath` (now keyed on
  `track`/`stage_code`, links to `/path/:track/:stage`). `StageDetailPage` is the **curriculum unit** — Read
  (deduped `content_slug` links) → Drill (`DrillCard`s for the stage concepts' `drill_refs`) → Track
  (`ConceptTrackPanel`s) → Gate (`gate_text` + `ExitBarGate`). `ConceptTrackPanel` resolves `cross_refs` via a new
  `useConceptIndex()` (a slug→concept map over all tracks) into "Also taught in: {Track} — {title}" links to the
  twin's `/path/:track/:stage`; the reader inherits these on its per-concept panels. `lib/learning.ts` added
  `useTracks`/`useConceptIndex`, track-scoped `useStages(track)`/`useProgress(track)`, and widened the mutation
  invalidations to the whole progress/stages/tracks subtrees. `tsc -b` + `vite build` clean.
- **Playwright.** `e2e/learning.spec.ts` rewritten for multi-track — 6 specs (track switch shows each track's own
  spine; curriculum unit renders Read→Drill→Track→Gate; reader edit persists; **per-track isolation** — Unified U1
  met leaves Aura A1 unmet; **cross-link jumps tracks**; drill-mark persists). With the 6 content specs, **12/12
  green**. (The live claude-in-chrome visual walkthrough was **not** separately run — the Chromium e2e covers the
  same behaviours; a manual visual pass remains optional.)
- **Ops note (not code):** during verification Docker Desktop stopped, dropping the `neurospect-learn-db`
  container; a full `alembic downgrade base` had also emptied `content_pages`. Restarted Docker + the container,
  re-ran all seeds **and `ingest_content` (67 pages)** — the 5e-1b work assumes the 5d ingest is present.

### 5e-2 as-built (2026-07-22) — code is now ground truth

Study-Planner engine shipped and verified end-to-end (backend only — no UI; that is 5e-3). One migration, two
models, one pure service, one router, 16 tests. **Code is ground truth.** Decisions made while building:

- **Migration `0006_study_planner`** (raw-SQL, reversible, mirrors 0002–0005; reuses `update_updated_at()`). NEW
  enums `plan_activity` (`learn|drill|review|observe|habit|backtest`) + `plan_item_status`
  (`pending|done|partial|skipped`); **`drill_variant` reused from 0004** (not recreated — 0006 downgrade does not
  drop it). `study_preferences` (user-scoped, soft-deleted, `UNIQUE (user_id) WHERE NOT is_deleted`) + `plan_items`
  (user-scoped, soft-deleted). **Idempotency fix (evidence-gated):** the `ux_plan_items_slot` partial-unique index
  uses **`NULLS NOT DISTINCT`** (PG 16) so a concept-less `backtest` item (concept_id + drill_ref both NULL) still
  de-duplicates on re-materialization — without it Postgres treats every NULL-ref row as distinct and daily
  materialize would dupe. Verified `0001→head→base→head` clean on a throwaway DB; `0006` down/up on the working DB
  keeps the seed + `drill_variant`.
- **Models** `study_preferences.py` + `plan_item.py`, registered in `models/__init__.py` + `alembic/env.py`.
  `plan_item.drill_variant` binds the 0004 enum by name (`create_type=False`), matching the `enums.pg_enum` idiom.
- **`app/services/scheduler.py` — a pure, DB-agnostic, deterministic function** over view dataclasses (no clock
  reads, no randomness, no DB — unit-tested with none). **Signature reconciled for multi-track:**
  `schedule(today, prefs, stage_metas, concepts, drills, concept_progress, drill_progress, past_items, *,
  horizon_days)` (the `stage_metas` arg is new — `compute_stages` needs it), returning a `ScheduleResult`
  (dated `items` + `projected_clear`/`projected_go_live`/`on_pace` + `days_behind`/`carried_over`/`unplaced`).
  Pipeline as designed: unlock via `compute_stages(prefs.active_track, …)` (locked stages **never** scheduled) →
  backlog (untracked → Learn, each drill below its `rep_targets.parse` floor → Drill [count-y = one task carrying
  remaining reps; `days`/`sessions` = one session/day, longitudinal], watch_only/U5 → Observe capped at Can-mark,
  foundation stage_order 0 → Learn/Drill **plus** a recurring daily Habit, lowest unlocked concept-less stage → a
  single Backtest placeholder) → mandatory spaced review (Leitner by confidence: 1→1d…3→3d,4→7d,5→21d; `None`→3d)
  → deterministic daily packing (tz-resolved `today`; skip blackout + 0-budget weekdays; fill order habits → due
  reviews → backlog in curriculum order; day-based drills one slot/day; est-minutes per activity capped at
  `max_session_minutes`; overflow rolls to the next eligible day; habits are mandatory and may drive a day's
  budget negative) → projection/ETA (pacing-only vs `target_go_live_date` — never gates) → slippage carry-over
  (past pending backlog re-queued at the FRONT of today; `days_behind`/`carried_over` surfaced). Anything that
  can't fit the horizon is returned in `unplaced` (surfaced, never silently dropped).
- **`app/routers/planner.py`** (prefix `/api`, auth-gated + user-scoped). `GET|PUT /api/preferences` (defaults
  returned with `is_configured=false` when unset). `GET /api/plan/today` — resolves `today` in the user's tz (the
  one clock read; the scheduler stays clock-free), runs the scheduler (`horizon_days=1`), **materializes today's
  items via `pg_insert … on_conflict_do_update`** on the slot index with `WHERE status='pending'` (never clobbers
  a mark), then returns the frozen rows + adherence + pace. `GET /api/plan?from=&to=` — past/today **frozen** (DB
  rows, `id` set) + future **computed** (scheduler specs, `id` null). `POST /api/plan/regenerate` — bumps
  `plan_version` + `generated_at`, soft-deletes today's **pending** items (done/partial/skipped kept as the
  accountability record), re-materializes at the new version. `PATCH /api/plan/items/{id}` — sets status +
  `done_qty`, and for a done/partial concept/drill item **feeds `concept_progress`/`drill_progress`** (reps +
  `last_practiced`) via the same lazy-upsert as `learning.py`; it **never advances the ladder** (that gate stays
  owned by `/api/progress`), honouring the north star. Schemas in `app/schemas/planner.py`; router mounted in
  `main.py`.
- **DB-session reuse (test infra, real fix):** the app's module-global async engine pools connections bound to one
  event loop; pytest's per-test loops then hit "Event loop is closed". The API tests use a dedicated **`NullPool`**
  engine + `app.dependency_overrides[get_db]` so no connection outlives its loop.
- **Ops note (not code) — evidence-gating lesson relearned:** a `downgrade base → upgrade head` chain intended for
  a throwaway DB ran against the **working** DB (an exported `DATABASE_URL` did **not** override the `.env`-derived
  settings that Alembic reads), wiping the 5c/5d/5e-1b seed. Recovered by re-running all seeds + `ingest_content`
  (74 concepts / 23 track_stages / 53 drills / 67 content_pages restored; Playwright 12/12 green after). Lesson:
  never run `downgrade base` against the working DB — pin scratch tests to a scratch DB by editing config, not an
  env export, or run migrations there via an explicit `-x`/`-c` the tool actually honours.
- **Verified:** scheduler unit tests (determinism; per-track unlock; locked stages never scheduled; U5
  observe-only + capped; blackout/0-budget skips; max-session cap; spaced-review due dates; slippage re-queue;
  pacing-only projection) — 9 green with **no DB**. API tests (preferences round-trip; `/plan/today` idempotent
  materialization [2nd call, 0 dupes]; PATCH-done feeds concept + drill progress; regenerate bumps `plan_version`
  and preserves a done item; per-user isolation; 5e-1b `/tracks` + `/stages` no-regression) — 7 green. Live
  uvicorn boot confirms all five planner routes mount and a full `PUT prefs → GET /plan/today` flow returns
  tz-aware habits/learn + adherence + pace.

### 5e-3 as-built (2026-07-23) — code is now ground truth

Study-Planner **UI** shipped and verified end-to-end (frontend only — consumes the 5e-2 API unchanged). Three
pages, seven components, one query/mutation layer, five Playwright specs. **Code is ground truth** (`app/src/
{pages/{today,plan,plan-setup}.tsx, components/planner/*, lib/planner.ts, types/api.ts}`). Decisions + notes:

- **`lib/planner.ts`** mirrors `lib/learning.ts`: hierarchical `plannerKeys` (`preferences`/`today`/`range`),
  queries `usePreferences`/`usePlanToday`/`usePlanRange`, mutations `useUpdatePreferences`/`useUpdatePlanItem`/
  `useRegenerate`. A **mark (`useUpdatePlanItem`) invalidates BOTH `plannerKeys.all` AND `learningKeys.all`** —
  since a done/partial item feeds `concept_progress`/`drill_progress`, `/path` + `/drills` must refetch. Prefs +
  regenerate invalidate `plannerKeys.all` (whole schedule recomputes).
- **Custom CSS-grid calendar (`StudyCalendar`)** — Mon-first month grid via `date-fns` (`startOfWeek`/`endOfWeek`
  `{weekStartsOn:1}` + `eachDayOfInterval`); items grouped by `scheduled_date`; per-day status dots + count; today
  ring-highlit; out-of-month cells muted; future-only days rendered as "projected" (lighter). `usePlanRange` is
  fetched for the visible grid `[gridStart, gridEnd]`; prev/next month via local state. **`react-day-picker` was
  NOT re-added** (a date picker, not a content calendar; keeps the CSP surface minimal, per the design).
- **`AvailabilityForm`** — RHF + `zodResolver`; per-weekday minute inputs (`valueAsNumber`), max-session, timezone
  (defaulted from `Intl…resolvedOptions().timeZone`), `active_track` via a `Controller`-wrapped shadcn `Select`,
  and an optional **pacing-only** target go-live date (labeled as never gating). **Blackout dates** are managed in
  local component state (add/remove chips) and merged on submit rather than through RHF — simpler and equally
  valid. Zod number schemas use plain `.int().min().max()` (dropped `invalid_type_error` — the option changed in
  Zod 4).
- **`PlanItemCard`** — activity→icon map (`learn`→BookOpen, `drill`→Dumbbell, `review`→History, `observe`→Eye,
  `habit`→Repeat, `backtest`→Rewind); done sends `done_qty = target_qty` when present (feeds the right reps);
  `data-status`/`data-activity` attributes for the e2e specs; **computed future items (`id===null`) render
  read-only** (no controls) — only frozen/today items are markable. A **skip is a logged skip** (strikethrough +
  adherence drop), never hidden.
- **Bug caught + fixed in the live browser walkthrough:** `AdherenceMeter` initially multiplied `adherence_pct` by
  100 (rendered **2500%**). The backend already returns a **0–100 percentage**
  (`planner.py`: `round(100 * (done + 0.5·partial) / total, 1)`) — the Pydantic schema comment
  `# (done + 0.5·partial) / total` omits the ×100. Fixed to render the value directly; the `types/api.ts` comment
  now says "0–100 percentage".
- **Nav** gains **Today** (top — the differentiator) + **Plan**; `/` still redirects to `/path` (unchanged).
- **Verified (evidence):** `tsc -b` + `vite build` clean. **Playwright 17/17** (12 existing regression + 5 new
  planner: setup saves → Today renders an ordered non-empty plan; mark-done flips `data-status` + surfaces
  adherence + **feeds progress** [API cross-check on `/api/progress`]; skip logs a SKIP; calendar shows today with
  its dots; regenerate bumps `plan_version`). The planner specs run **serially against their own isolated debug
  user** (injected via `addInitScript`) so they never race with `learning.spec` on the shared `e2e` user. Live
  claude-in-chrome walkthrough (debug-login → `/plan/setup` save → `/today` mark-done + skip → `/plan` calendar →
  regenerate) with **NO console errors**; the 2500% bug was caught here and fixed. (Note: the API `CORS_ORIGINS`
  allows only `http://localhost:5173` — the dev server must run on `:5173` for `/auth/me` to pass.)

### 5f as-built (2026-07-24) — code is now ground truth

Model-aligned **journal** + **expectancy dashboard** shipped and verified end-to-end, built over the existing
5c `journal_entries` table — **no migration** (the deferred items — screenshots, `missed_trades`,
`position_size` — stay deferred). **Code is ground truth** (`api/app/{routers/{journal,analytics}.py,
schemas/{journal,analytics}.py, services/expectancy.py}`; `app/src/{pages/{journal,journal-entry,expectancy}.tsx,
components/{journal,analytics}/*, lib/{journal,analytics}.ts, types/api.ts}`). Decisions + notes:

- **Backend `journal` router** — CRUD over `journal_entries`, auth-gated + user-scoped + soft-deleted (mirrors the
  `drill_progress` idiom). `mode` + `entry_model` + `entry_date` + `instrument` required on create; `entry_pda`
  **defaults to `fvg`** in the Pydantic `JournalEntryIn` (so an omitted value applies R4 rather than writing NULL).
  PATCH is partial (`exclude_unset`); DELETE sets `is_deleted`/`deleted_at`. List supports
  `mode`/`entry_model`/`instrument`/`from`/`to`, newest-first.
- **Expectancy math is a pure service (`services/expectancy.py`)** — DB-agnostic, so it's unit-tested against
  hand-built fixtures (mirrors `scheduler.py`). **Win/loss/breakeven are classified by the SIGN of `r_multiple`**
  (r>0 / r<0 / r==0), NOT by the `outcome` enum — this keeps the math self-consistent and makes the identity
  **`expectancy == mean(r_multiple)`** exact (asserted both ways in tests). Only CLOSED trades (non-null
  `r_multiple`) enter the sample; a group is emitted per (model, mode) with ≥1 non-deleted entry, its stats over
  the closed subset. `win_rate`/`break_even` are returned as **fractions 0–1** (the UI formats as %); break-even
  `= 1/(1+avg rr_planned)`. A `SAMPLE_TARGET = 50` (design gate ≥50 setups) is surfaced as a **reference** only —
  under-evidenced models read amber — and is explicitly **NOT** the live-eligibility verdict (5g owns that).
- **`analytics` router** — three read-only endpoints (`/expectancy` by model × mode, `/summary` per mode,
  `/r-distribution` R histogram split by mode) that load the user's non-deleted entries once, map to
  `expectancy.TradeR`, and delegate to the pure service. No gate verdict.
- **Frontend libs** — `lib/journal.ts` (`journalKeys` + `useJournalEntries`/`useJournalEntry` + create/update/
  delete mutations; **every write invalidates BOTH `journalKeys.all` AND `analyticsKeys.all`** since expectancy
  derives from entries) + `lib/analytics.ts` (`analyticsKeys` + the three read hooks + `pct()`/`rMultiple()`
  formatters). Enum label maps live in `lib/journal.ts`.
- **`JournalForm`** — tabbed RHF+Zod (Context / Decision-flow / Execution&risk / Review) with a prominent
  **backtest|live segmented toggle above the tabs** (drives both axes). Optional numeric fields are registered as
  **strings and coerced on submit** (empty → null) to avoid RHF `valueAsNumber` NaN; optional enum selects use a
  `__none__` sentinel (Radix Select can't hold `""`); `confluence_tags`/`mistake_tags` are local-state chip inputs
  (the blackout-date pattern). `plan_followed` defaults **true**. All fields trace to the model-aligned field set
  (§2) — NOT the generic `trades` shape.
- **Charts + validated palette** — the two axes map to two **dataviz-validated** categorical hues (slot-1 blue =
  backtest, slot-2 orange = live; the pair PASSES all six checks in both light + dark — CVD ΔE 24.7 / 26.8, ≥8
  target), declared as `--chart-*` CSS vars in `index.css` (light + `.dark` steps). `ExpectancyChart` (expectancy
  R, zero reference line), `BacktestVsLiveChart` (win-rate %, the honesty view), plus an **added**
  `RDistributionChart` (R histogram). A theme-aware `ChartTooltip` (shadcn popover tokens — the default white
  tooltip is unreadable in dark). `recharts` re-added (`npm install recharts`); `react-day-picker` stays out.
- **`/expectancy` page** — summary tiles (per mode: expectancy/trade in R, win%, total R, n/logged closed), the
  three charts, and a **per-model table** (the accessible table view + exact numbers: n, win%, avg win/loss R,
  expectancy, break-even) with amber under-reference sample sizes and a footnote clarifying the reference-vs-gate
  distinction + confluence-is-study-only + "the Readiness-to-Live decision lives on the Gate."
- **Verified (evidence, not inference; local Postgres :5433):** backend **33 tests** (16 prior + **9 pure
  expectancy** hand-built-fixture unit tests [by-hand win%/avgWinR/avgLossR/expectancy/break-even + the
  `expectancy == mean r` identity + open/breakeven/grouping/mode-summary/R-distribution] + **8 journal API**
  [CRUD, filters narrow, soft-delete (gone from API, row still in DB flagged), per-user isolation, enum/CHECK 422,
  no-token 403, and the expectancy VIEW over created entries]). `tsc -b` + `vite build` clean. **Playwright 20/20**
  (17 prior regression + 3 new journal: create backtest → list + feeds expectancy; mode filter narrows [Radix
  select]; charts render per-model bars). Live claude-in-chrome walkthrough (debug-login → `/journal/new` create a
  backtest entry → `/journal` list → `/expectancy` dashboard) with **NO console errors**; the rendered expectancy
  table + charts were cross-checked against hand-computed values (Backtest +0.64R / win 55%, Live −0.33R / win 33%
  — backtest-vs-live honesty view stark; London backtest +0.20R vs live −0.33R). No migration was needed.

### 5g as-built (2026-07-24) — code is now ground truth

The **Readiness-to-Live Gate** shipped and verified end-to-end — the north-star payoff, and the last phase of the
Phase 5 arc. One migration (`0007`), one model, one pure service, one router + schemas, and the `/gate` UI.
**Code is ground truth** (`api/app/{services/gate.py,routers/gate.py,schemas/gate.py,models/gate_attestation.py}`,
`api/alembic/versions/0007_gate_attestations.py`; `app/src/{pages/gate.tsx,components/gate/*,lib/gate.ts}`).
Decisions + notes:

- **Anchor track (the load-bearing call the design left open).** `journal_entries.entry_model` — the gate's
  grouping key — maps **1:1 onto the unified track's seven U3.2a–g entry-model concepts**, and no other track
  enumerates a per-model set. So the requirement set is defined by the **unified** curriculum: the shared core is
  its 10 `is_core` U1–U4 concepts at **Backtested+**, plus the model's own entry-model concept at **Live-ready**.
  The seven slugs are named **explicitly** in `gate.ENTRY_MODEL_CONCEPTS` (the `stages._U2_GATE_SLUGS` idiom —
  greppable, and immune to a re-seed shifting a code-letter ordering).
- **`unified` carries the hardest bar.** The unified decision flow routes into every model at runtime, so
  `entry_model='unified'` requires **all seven** entry-model concepts at Live-ready (north star: default to
  enforce; 5e-1b reframed Unified as the advanced track, and the shipped unified U3 stage gate already requires
  all seven at Can-mark).
- **Cross-track credit, and `?track=` tightens only.** A requirement is satisfied by its anchor concept **or** by
  any `cross_refs` equivalent that reached the bar — studying the same primitive in Aura is real evidence, and
  refusing it would make the gate unreachable for an Aura-only student (per-track progress stays separate
  everywhere else, per 5e-1b). `?track=` restricts which track may supply that credit, so it can only ever
  **remove** evidence: no caller-supplied parameter can loosen a verdict. Default = any track.
- **Non-overridability is structural, not cosmetic.** There is no `cleared` column, no request schema field, and
  no endpoint that sets one; `cleared` is the conjunction `(a) ∧ (b) ∧ (c)`, recomputed on every read (a unit test
  asserts exactly that identity). The only write on the whole gate surface is PATCH-ing one behavioural item.
- **Fails closed, never vacuously.** An absent curriculum concept emits an **unmet** requirement pointing at
  `scripts.seed_concepts`, and an empty core set emits an unmet "unseeded" requirement — an empty requirement list
  would otherwise make `all()` report a model as cleared.
- **(b) is reuse, not reimplementation.** `routers/gate.py` calls the pure 5f `expectancy.compute_groups` exactly
  as the analytics router does. Three requirements: sample ≥ `SAMPLE_TARGET` (50) closed **backtest** trades,
  expectancy strictly `> 0`, and `above_break_even`. An unknown planned R:R fails the third with "a win rate
  without its R:R is meaningless" (README §Gate item 3). `SAMPLE_STRETCH = 100` is the README's "ideally" —
  surfaced, never gating. **Live trades never gate** (a losing live record is shown for honesty only).
- **(c) = all four README items** (not the boot prompt's three): risk precommitted in writing · demo/sim track
  record · journaling habit · circuit-breaker demonstrated. `gate_attestations` (Alembic `0007`, new
  `gate_attestation_item` enum) is per-user, revocable, soft-deleted with the partial-unique lazy-upsert idiom of
  `concept_progress`/`drill_progress`. **Corroboration, not thresholds:** the API returns objective journal facts
  (entries logged, distinct journaling days, backtest/live split, last entry) so a self-attest is made in the face
  of the record — no invented rule gates on them.
- **Frontier stays study-only.** `watch_only` concepts are excluded from the requirement set **and** from the
  credit candidates, and are returned separately so `/gate` can name them "never gate-eligible" (12 seeded U5
  rows). `confluence_tags` are not read by the gate at all.
- **Frontend.** `lib/gate.ts` (`gateKeys` + `useGate`/`useAttestations`/`useUpdateAttestation`; a mark invalidates
  the whole gate subtree). The attestation checkbox is **server-controlled — deliberately not optimistic**: an
  attestation should not flip in the UI before it is recorded (the e2e therefore uses `click()`, not `check()`).
  `/gate` replaced the last stub and **`pages/stub.tsx` was deleted** — the route taxonomy is fully implemented.
- **Verified (evidence, not inference; local Postgres :5433):** `alembic upgrade head` 0006→0007 + `downgrade
  0006` and back up clean (table + enum dropped and recreated; the 74-concept seed preserved). Backend **68 tests**
  (33 prior + **24 pure gate** hand-fixture unit tests + **11 gate API**). The pure suite pins the cleared case
  then flips each input (core ladder, load-bearing ladder, sample, expectancy, break-even-with-positive-expectancy,
  each of the four attestations) and asserts the right blocking reason, plus: frontier never a requirement nor a
  creditor, cross-track credit, `credit_track` tightening both ways, unified-needs-all-seven, missing/empty
  curriculum fails closed, `ALL_MODELS` ≡ the `EntryModel` enum (drift guard), live activity never gates. The API
  suite builds a **fully satisfied London against the real 74-concept seed**, proves it clears, then flips all
  four sources back; plus attest round-trip/revoke (one row, upserted in place), non-overridability (all four
  attested + full ladder + no sample → still blocked; a stray `cleared` field in the body changes nothing),
  per-user isolation, corroboration, unknown track 404, unknown item 422, no-token 403. `tsc -b` + `vite build`
  clean. **Playwright 27/27** (20 prior regression + 7 new gate: cleared renders cleared, blocked renders blocked
  *with reasons*, revoking an attestation blocks it and re-ticking it in the UI clears it again, attesting cannot
  clear an unevidenced model, frontier listed as never-eligible, credit-track tightening, and a seed-drift guard).
  Live claude-in-chrome walkthrough on the fixture user: London **Cleared** (50/50, +0.80R, win 60% vs break-even
  33%, all three pills green) while all seven other models stayed blocked *with all four discipline boxes ticked*
  — non-overridability visible on the rendered surface; checklist groups 11/11 · 3/3 · 4/4; frontier panel showing
  12 watch-only concepts; the credit-track selector toggled to "Aura only" and back, flipping London
  Cleared → Not cleared → Cleared. **No console errors.** One copy wart caught in-browser and fixed
  ("across 1 days" → "1 day").

### 6 as-built (2026-07-25) — code is now ground truth

Phase-5 debt closed; **this is the last phase of the learning-platform-ui workstream**. One migration (`0008`), one
new table, two new pure services' worth of math (`opportunity_cost.py` + `expectancy.compute_pooled`), one new
router, and the `stages.py` evidence wiring. **Code is ground truth**
(`api/app/{services/{stages,opportunity_cost,expectancy}.py, routers/{learning,missed_trades,analytics,planner,gate}.py,
models/missed_trade.py, schemas/missed_trade.py}`, `api/alembic/versions/0008_missed_trades_position_size.py`;
`app/src/{pages/{journal,missed-trade-entry}.tsx, components/journal/*, components/progress/exit-bar-gate.tsx,
lib/missed-trades.ts}`). The design decisions live in §Stage exit-bar derivation (6a) and §2b (6b/6c); the notes
that belong only to the build:

- **6a's load-bearing call — does a wired attestation feed `auto_met` / the lock chain? NO.** `auto_met` stays
  concept-only, so `locked` is byte-identical to 5e-1b; only `met` / `attest_pending` / the row's own status move.
  Rationale: freezing a *track* on behavioural evidence would be a different (and harsher) product decision than
  the one 6a was scoped to make, and the lock chain is the curriculum's spine. Proven, not asserted — a unit test
  compares the full `(locked, auto_met)` signature across all three tracks × four progress states with the richest
  possible evidence bundle, and an API test does the same against the real 74-concept seed.
- **Two label corrections the wiring forced.** U4's row was "Positive expectancy in R computable from journal" but
  the learning-path bar is "**can compute** a trade's expectancy contribution in R" — positivity is A4/M7's bar,
  so the row is now computability and a *negative* expectancy satisfies it (asserted). U0's single composite row
  was split into the two attestations it actually names, so each row maps to exactly one `/gate` tick.
- **The planner was wired too** (beyond the boot prompt's minimum), because leaving it would have made `/path` and
  `/today` disagree: `/path` would say the foundation bar is met while `/today` kept prescribing its habits
  forever. `scheduler.schedule(..., evidence=None)` keeps every 5e-2 test valid.
- **ict_course M6 is the one bar left un-wired, on purpose** — see §Stage exit-bar derivation. It is recorded here
  as the workstream's only remaining stage-gate debt, owned by the learning-enforcement tracker.
- **6b conventions:** `entry_model` (not `setup_type`) + `entry_date` (not `trade_date`); `entry_model` NOT NULL so
  the by-model slice is meaningful; the analytic sits on the **analytics** router (`/api/analytics/missed-summary`,
  matching the trade-schema naming) rather than under `/api/missed-trades/…`, which would have collided with the
  `{id}` route. The opportunity-cost sums are keyed off the **sign of `hypothetical_r`**, not the
  `hypothetical_outcome` enum — the same self-consistency rule 5f applied to `r_multiple`.
- **6b UI placement:** a **tab on `/journal`**, not a new nav item (the journal covers every trade, including the
  ones not taken). `/expectancy`'s footnote now states the exclusion explicitly and links to the log — the honesty
  view the north star asks for.
- **Verified (evidence, not inference; local Postgres :5433):** `0008` up + `downgrade 0007` + up clean (table,
  both enums, all four indexes, the trigger and the `position_size` column dropped and recreated; seeds preserved
  74/23/53/67). **114 backend tests** (68 prior + **18 pure stage-evidence** + **7 stage/planner API** + **9 pure
  opportunity-cost** + **4 `compute_pooled`** + **8 missed-trade API**). `tsc -b` + `vite build` clean.
  **Playwright 36/36** (27 prior regression + 9 new: 4 stage-evidence + 5 missed/position-size).
- **THE PHASE-6 EVIDENCE GATE — no regression in the numbers, in three parts.** (1) `/api/analytics/*` + `/api/gate`
  captured for a fixture user **before** any Phase-6 code and re-captured after: **byte-identical** (file hashes
  compared). (2) On the same fixture, writing three missed trades — including a **+12.5R "would have won"** that
  would visibly inflate expectancy if it leaked — plus a `position_size` on every entry: **byte-identical again**.
  (3) The same assertion as a durable pytest
  (`test_missed_trades_and_position_size_never_move_expectancy_or_the_gate`) and as a Playwright spec, so it cannot
  silently rot. Live claude-in-chrome walkthrough of every changed surface (`/path/unified/U0` before → after
  ticking two `/gate` boxes, `/path/unified/U4`, `/path/aura/A4`, `/path/unified/U6`, the missed tab + its form +
  its opportunity-cost panel recomputing live, the journal form's Position size, `/expectancy`'s unchanged
  +0.20R London row and its new footnote) with **NO console errors**.

## Contradiction flags (per [[CLAUDE]] Rule #6)

**1. `trade-schema.md` still specs `missed_trade_screenshots` (flagged at E2, 2026-07-28).**
[[concepts/architecture/trade-schema]] §Missed Trades describes a `missed_trade_screenshots` **child table**.
Phase E2 deliberately did **not** build it: `neurospect-learn` ships ONE polymorphic `evidence_assets` layer that
missed trades attach to via `subject_type`, which is precisely the duplication the enforcement design exists to
avoid. That page is the **journal-analytics lane's** canonical doc, so it is flagged here for Paul rather than
edited from an enforcement session — the same call made for `phase3-frontend-structure` below. *Nuance worth
keeping:* that doc primarily describes the older `neurospect-app` `trades` schema, where a per-owner child table
is still the right shape; what is stale is only any implication that **this** app will grow one.

**2. `phase3-frontend-structure.md` stack versions.**
[[concepts/architecture/phase3-frontend-structure]] lists the `neurospect-app` stack as **Vite 6 · ky v1**
(and does not pin TS/Recharts/Tailwind/Zod majors). The shipped code is actually **Vite 8 · TypeScript 6 ·
ky v2 · Zod 4 · Recharts 3 · Tailwind v4 · React Router 7.14**. Code is ground truth. That doc is the
`journal-analytics` lane's canonical page, so it is **flagged here for Paul, not edited from this session** —
its owning lane should reconcile it (or the monorepo migration's same-PR rule will). *E2 addendum:* **ky v2
consumes an error's response body** to populate `error.data`, so `error.response.json()` throws — any lifted
code that reads a FastAPI `detail` that way silently shows ky's generic message instead. `lib/api.ts` now owns
`apiErrorDetail()`; `neurospect-app` has the same pattern and may have the same latent bug.

## See Also

- [[processes/distributed-workflow/active/learning-platform-ui]] — the workstream tracker (5b–5g phases)
- [[concepts/architecture/learning-enforcement]] — **canonical** for the evidence layer, drill grading,
  anti-cheat and gamification that replace the self-reported `reps` integer (the next push; owns the deferred
  screenshot primitive and the `stages.STAGE_UNWIRED` M6 debt)
- [[concepts/mastery/README]] — the ladder / confidence / Readiness-to-Live Gate the platform visualizes
- [[concepts/mastery/unified/learning-path]] · [[concepts/mastery/unified/tracker]] — the U0–U6 spine + grid the UI renders
- [[concepts/mastery/unified/README]] — the Unified Playbook the journal fields trace to
- [[concepts/advanced/README]] — frontier content + the TIER/label + watch-only rules the UI enforces
- [[concepts/architecture/phase3-frontend-structure]] — the `neurospect-app` frontend lifted from (see §Contradiction flag)
- [[concepts/architecture/phase2-project-structure]] — the backend layout the new API mirrors
- [[concepts/architecture/trade-schema]] — the journal conventions reused (schema is new, conventions shared)
- [[processes/distributed-workflow/active/monorepo-migration]] — where `neurospect-learn` eventually sites
