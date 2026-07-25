---
tags: [distributed-workflow, active, neurospect, mastery, frontend, ui]
aliases: [Learning Platform UI Tracker, Phase 5 UI, Mastery UI]
sources: []
created: 2026-07-18
updated: 2026-07-24
---

# Learning Platform UI — Workstream Tracker

Give the completed learn-to-execute knowledge base a **front end**: a **new, clean Learning Platform app** that
surfaces all the course content **and** tracks Paul's progress across the three axes that carry a trader to
consistent profitability — **learning exercises → backtesting → live trading** — graded on the existing
[[concepts/mastery/README|mastery ladder + confidence + Readiness-to-Live Gate]]. This is the delivery layer
on top of the [[processes/distributed-workflow/active/mastery-layer|Mastery Layer]] workstream (content ✅
complete: mastery system, both tracks, unified playbook, frontier ICT, graded roadmap + tracker, Tier-1 sourcing).

> **STATUS: the Phase 5 arc (5a → 5g) is COMPLETE as of 2026-07-24.** All four goals below ship in
> `neurospect-learn`: read/navigate the corpus (5d), track learning progress (5e-1/5e-1b), log backtests and see
> expectancy build (5f), and see gate status (5g) — plus the Study Planner (5e-2/5e-3), which was added to the
> scope on 2026-07-20 and is the platform's differentiator. Every route in the taxonomy is implemented; no stubs
> remain. Migrations are at `0007`.
>
> **This tracker now carries ONE remaining phase: Phase 6 — Phase-5 debt** (boot prompt below, ⏭ ACTIVE). It
> closes the three follow-ups Paul scoped on 2026-07-25: wiring the stage attestations to the shipped gate,
> the deferred missed-trade log, and `position_size`. **When Phase 6 lands, this workstream is closed.**
>
> **The next big push is a SEPARATE workstream:**
> [[processes/distributed-workflow/active/learning-enforcement]] — verified drill grading (screenshot evidence of
> markings), anti-cheat, and gamification. Deploy/hosting and live commentary remain unscoped in either tracker.

## Goal

Turn the static markdown roadmap + per-concept trackers into a **living, interactive platform** so Paul can:
1. **Read / navigate** all course content (course, entry-models, unified playbook, frontier pages, exercise libraries).
2. **Track learning progress** per concept on the ladder (Learned → Can-mark → Backtested → Live-ready) + 1–5
   confidence + rep counters — the data that currently lives only in `*/tracker.md`.
3. **Log backtests** (replay sessions) per model and see **expectancy** build toward the gate (sample size,
   win rate, avg R, expectancy) — the empirical proof-of-edge loop.
4. **See gate status** — a clear "cleared to live?" signal per model driven by the Readiness-to-Live Gate.

## North Star (Paul, 2026-07-20) — read before designing ANY feature

**Discipline & accountability by design — not by choice.** Every feature must *structurally enforce* the
disciplined process and remove the user's ability to shortcut it. The platform is **opinionated and prescriptive**,
not a menu of optional tools. This is the differentiator that makes it one of the best ICT trading learning tools
ever built — most courses hand you content and let you cheat yourself; this one won't let you.

Concretely, features should default to enforcement over opt-in:
- **Gated progression** — you cannot open a stage / mark a concept advanced / be "cleared to live" until the
  objective bar is met (stage exit-bars, required backtest sample + positive expectancy, watch-only frontier never
  gate-eligible). No manual override of the gate.
- **Prescriptive, not optional** — the study planner tells you what to do *today*; the journal requires every
  trade **including misses**; rep targets must actually be met, not self-declared done.
- **Accountability surfaced** — streaks, adherence, skipped days, and honesty checks (e.g. journaling habit,
  precommitted risk, circuit-breaker) are visible and factored in, not hideable.
- **Guardrails the user can't switch off** where they protect the process (loss-limit precommitment, set-and-forget,
  no live-eligibility on unbacktested/EMERGING/SPECULATIVE concepts).

When a design choice is "let the user decide" vs "enforce the disciplined path," **default to enforce** and justify
any exception. Every phase's design + the plan-mode design session must be checked against this north star.

## Lane

- **This wiki** produces the DESIGN artifacts + this tracker only: `concepts/architecture/*` (a new canonical
  frontend doc), `processes/distributed-workflow/active/learning-platform-ui.md`, and additive cross-links.
- **The app code** lands in a **new repo** (propose the name/location in 5a — e.g. `neurospect-learn`) in
  later implementation sessions — NOT written from a wiki session. Features/patterns/schema are **lifted from
  the existing `neurospect-app` as needed** (clean-start, not a fork). Per Architecture Doc Integrity, once
  code exists the code is ground truth and the wiki doc describes it as implemented.
- Isolation Rule applies (Neurospect only; no ALDC content/refs).

## Decisions (Paul, 2026-07-18)

- **Phase 5 = Platform UI focus.** The next phase is the front end, not a backtesting-methodology workstream.
- **The UI tracks progress on backtesting + trading + learning exercises** — all three axes in one layout.
- **Next session is a PLANNING / design session** for the optimal frontend (plan mode; the plan is the artifact).
- Grading is the **existing** ladder/confidence/gate — the UI *visualizes* it, does not reinvent it.
- **Build it as a NEW app** (its own repo), then **integrate features from the existing `neurospect-app` as
  needed** — cleaner than bolting a module onto the journal app. Reuse the proven stack + lift components /
  schema / API patterns selectively rather than inheriting the whole app's coupling.

## Decisions (Paul, 2026-07-20)

- **Study Planner elevated to a headline feature.** An **adaptive daily/weekly study-schedule generator** — the
  user inputs availability (hours/slots), and the platform generates a concrete daily routine from the U0→U6
  curriculum sequence + rep targets + drills, **gated by progress** and re-planning as progress updates, with a
  Today view + calendar and spaced review of weak concepts. This is the platform's key differentiator ("tell me
  exactly what to do today"), net-new to the 5a design.
- **Planner sits on top of the progress layer (5e).** A smart scheduler needs current ladder position + stage
  gates + rep targets, so it depends on `concept_progress` (5e). Decision: **design the planner AND the minimal
  5e progress layer it needs together, shipping as one** (not planner-before-progress). The 5e build boot prompt
  written 2026-07-20 is therefore **superseded** — the design session below re-scopes it.
- **Next session is a PLAN-MODE design session** for the Study Planner + folded-in progress layer (the plan is
  the artifact; no code). Design-heavy: availability model, scheduling algorithm, adaptivity/spaced-repetition,
  data model, calendar UX, and the revised implementation split.

## Decisions (Paul, 2026-07-20 — post-5e-1: multi-track path)

After reviewing the shipped 5e-1 `/path`, Paul redefined the path layer (this **supersedes the single unified
path** in the 5a design; captured in [[concepts/architecture/learning-platform]] §Multi-track path redefinition):

- **Three first-class graded tracks, not one:** an **Aura** track, an **AXL/MrWitness** track, and the **Unified**
  track (the reconciliation, reframed as the advanced track). A track switcher on `/path`.
- **Per-track progress (separate), not a shared spine.** A concept taught by both mentors is **duplicated on
  purpose** — repeating it is *more reps*, and a second explanation in a different voice may resonate better.
- **Cross-links between equivalent concepts** across tracks (soft refs) — "Also taught in: …" — so the user can
  jump to another track's take for more reading, without merging progress.
- **Each stage is a curriculum unit:** Read (content) → Drill (that track's drills) → Track (its concepts) → Gate.
  The bare progress-grid stage was the "no value" complaint; this is the fix.
- **Sequencing:** build this (**5e-1b**) *before* the Study Planner — the planner schedules whichever track is
  active, so the track model must land first.

## Plan

### Phase 5a — Frontend/app design session ✅ (2026-07-18)
Delivered the canonical design doc [[concepts/architecture/learning-platform]] covering the route taxonomy,
content-delivery, progress + model-aligned journal data model, component structure + API surface, and the
5b–5g implementation split. Paul's three forks (see Decisions) resolved: **separate backend · brand-new
model-aligned journal · content API**. See the 2026-07-18 session log.

### Phase 5b — Scaffold ✅ (2026-07-19, in `neurospect-learn`)
Created the `neurospect-learn` repo (`app/` + `api/`, `git init` only); lifted the frontend infra spine +
backend users-only skeleton; Discord OAuth wired (real OAuth + debug-login); app shell + sidebar nav +
protected routes with stub pages for the full route taxonomy. Verified end-to-end (see 2026-07-19 session log).
Code is now ground truth — [[concepts/architecture/learning-platform]] §5b as-built records the divergences.

### Phase 5c — Data model + migrations ✅ (2026-07-19, in `neurospect-learn`)
Built the four tables (`concepts`, `concept_progress`, `journal_entries`, `content_pages`), eight fresh Postgres
enums, Alembic `0002`/`0003` (raw-SQL, reversible), and an idempotent 41-concept seed from the U0–U6 taxonomy.
Finalized the model-aligned journal field set (the biggest new-authoring piece). Verified end-to-end (see
2026-07-19 session log). Code is now ground truth — [[concepts/architecture/learning-platform]] §5c as-built
records the sketch→final decisions.

### Phase 5d — Content API + ingest + library/reader ✅ (2026-07-20, in `neurospect-learn`)
Ingest job (`api/scripts/ingest_content.py`, 67 wiki pages → `content_pages`); content endpoints
(`/api/content/pages|/pages/{slug}|/search`); `/library` browser + `/concepts/:slug` reader (react-markdown +
remark-gfm, wikilink resolver, TIER/label + watch-only badges, search). Chose the content-page slug scheme
(basename + `NN-`-strip + README→dir + depth-tiebreak de-collision) → **all 27 provisional
`concepts.content_slug` soft-refs resolve with zero seed edits and no Alembic 0004**. Added a Playwright harness
(Paul's request). Verified end-to-end. Code is ground truth — [[concepts/architecture/learning-platform]]
§Content delivery + §5d as-built record the decisions.

### Phase 5e — Progress layer + Study Planner (DESIGNED ✅ 2026-07-20 — three build sub-phases)
The progress layer (ladder/confidence/reps editing + stage exit-bars + `/drills`) and the **Study Planner**
(availability → adaptive, gate-aware, retention-aware daily/weekly schedule + Today view + calendar + spaced
review) were **designed together** (plan-mode session 2026-07-20) and split into three boot-promptable build
sessions that ship as the 5e arc. Design is canonical in [[concepts/architecture/learning-platform]] (§Study
Planner + §Progress + journal data model "Study Planner + progress-editing" subsection + §Component/API surface).

- **5e-1 — Progress foundation. ✅ Built 2026-07-20 (in `neurospect-learn`).** `concept_progress` lazy-upsert
  lifecycle, the derived stage exit-bars service (+ the shared `rep_targets` parser), the `drills` catalog
  (53 rows, seeded from the two `exercises.md` drill-map tables) + `drill_progress` (Alembic `0004`), the
  `learning` endpoints; frontend `/path`, `/path/:stage`, `/drills`, `ConceptTrackPanel` on the reader. Code is
  ground truth — [[concepts/architecture/learning-platform]] §5e-1 as-built records the decisions.
- **5e-1b — Multi-track curriculum. ✅ Built 2026-07-21 (in `neurospect-learn`).** Redefined
  `/path` from one unified spine into **three graded tracks** (Aura · AXL/MrWitness · Unified) with a track
  switcher; **per-track concepts** (own stages, own drills, own progress — a shared primitive is duplicated on
  purpose for more reps + a second explanation) + **cross-links** between equivalents; `track_stages` seed +
  `cross_refs` (Alembic `0005`); generalized `stages.py`; reshaped `/path/:track/:stage` into a **curriculum unit**
  (Read → Drill → Track → Gate). Ships **before** the planner (which schedules the chosen track). Code is ground
  truth — [[concepts/architecture/learning-platform]] §5e-1b as-built records the counts + decisions.
- **5e-2 — Planner engine. ✅ Built 2026-07-22 (in `neurospect-learn`).** `study_preferences` + `plan_items`
  (Alembic `0006` + the `plan_activity`/`plan_item_status` enums; `active_track` on prefs for the 5e-1b
  reconciliation), the deterministic pure `app/services/scheduler.py` (track-scoped; reuses the 5e-1
  `rep_targets` parser + `stages.compute_stages`), and the planner API (preferences · today · calendar ·
  regenerate · mark-item-done → progress). Backend-only; verified by 16 tests (9 scheduler unit with no DB + 7
  API). Code is ground truth — [[concepts/architecture/learning-platform]] §5e-2 as-built records the decisions.
- **5e-3 — Planner UI. ✅ Built 2026-07-23 (in `neurospect-learn`).** The three planner pages — `/today`
  (prescriptive ordered daily card list), `/plan` (custom CSS-grid month calendar + regenerate), `/plan/setup`
  (availability & preferences form) — + the `planner/` components (`TodayList`/`PlanItemCard`, `StudyCalendar`,
  `AvailabilityForm`, `StreakBadge`/`AdherenceMeter`/`PaceProjection`) + `lib/planner.ts` (query/mutation layer),
  wired to the live 5e-2 API; mark-done/partial/skip feeds progress; streak / adherence / days-behind / pace
  surfaced (never hideable). Nav gains Today + Plan. Code is ground truth —
  [[concepts/architecture/learning-platform]] §5e-3 as-built records the decisions (incl. the adherence-% bug
  caught in-browser).

Write each sub-phase's build boot prompt when that sub-phase starts (5e-1 first). The standalone 5e build boot
prompt below (⛔ SUPERSEDED) is folded into 5e-1's scope.

### Phase 5f — Journal + expectancy ✅ (2026-07-24, in `neurospect-learn`)
Model-aligned `/journal` (backtest|live CRUD + filters + soft-delete) + `/expectancy` dashboard (per-model
expectancy in R, win rate, backtest-vs-live honesty view, R distribution, per-model table). Backend `journal` +
`analytics` routers over the existing 5c `journal_entries` table (**no migration**); the pure
`services/expectancy.py` (win/loss by `r_multiple` sign; `expectancy == mean r` identity; break-even
`1/(1+rr)`; sample-target 50 is a reference, NOT the gate); recharts re-added with a dataviz-validated 2-hue
palette. Verified: 33 backend tests (9 pure expectancy + 8 journal API), Playwright 20/20, live browser
walkthrough (no console errors, expectancy cross-checked by hand). Code is ground truth —
[[concepts/architecture/learning-platform]] §5f as-built records the decisions.

### Phase 5g — Gate/readiness view ✅ (2026-07-24, in `neurospect-learn`) — **COMPLETES THE PHASE 5 ARC**
`/gate` computed readiness over progress + backtest expectancy + checklist; watch-only enforcement for frontier.
The pure `services/gate.py` combines (a) the unified core ladder at Backtested+ / the model's own entry-model
concept at Live-ready, (b) the **reused** 5f `expectancy.py` (sample ≥50 · expectancy > 0 · win rate ≥ break-even),
and (c) four attested behavioural items (`gate_attestations`, Alembic `0007`) into a per-model `cleared` that is
**computed on every read and impossible to set** — no `cleared` column, no endpoint, no UI control. Frontier
(watch-only) concepts are neither requirements nor sources of cross-track credit; a seed gap fails closed.
`?track=` restricts which track may supply credit and can only **tighten**. Frontend `/gate` (`GateSignal` ·
`GateChecklist` · frontier panel · credit-track selector) replaced the last stub — **every route in the taxonomy
is now implemented** (`pages/stub.tsx` deleted). Verified: 68 backend tests (24 pure gate + 11 gate API new),
Playwright 27/27, live browser walkthrough. Code is ground truth —
[[concepts/architecture/learning-platform]] §5g as-built records the decisions.

### Phase 6 — Phase-5 debt (⏭ boot prompt below) — **closes this workstream**
Three scoped follow-ups from the 5g sign-off (Paul, 2026-07-25): **(6a)** wire the stage attestations in
`services/stages.py` to the evidence that now exists (the 5g `gate_attestations` store + the 5f expectancy
service) so `/path` stops showing permanently-unmet placeholder rows; **(6b)** the deferred **missed-trade log**
(Aura canceled orders — the "how much is hesitation costing you?" analytic), adapted to the learn app's
model-aligned conventions and **without** the screenshots child table; **(6c)** `position_size` + any remaining
small journal field gaps, with expectancy staying R-based. Screenshots/evidence storage is **deliberately
excluded** — see the Decisions block.

## Decisions (Paul, 2026-07-25 — post-5g)

- **Phase 6 = the last phase of this workstream**, scoped to three items: the stage-attestation wiring, the
  missed-trade log, and `position_size` + small journal gaps. **Deploy/hosting is explicitly NOT in it** (it is
  different in kind and unscoped for now); live commentary likewise.
- **Screenshots / evidence storage stay deferred — on purpose.** The deferred 5c journal item ("screenshots/R2")
  and the `missed_trade_screenshots` child table in [[concepts/architecture/trade-schema]] §Missed Trades are
  the *same primitive* the drill-grading vision needs: user-uploaded evidence of chart markings, attached to a
  concept and judged. Building it now for the journal alone would pre-commit its shape (what it attaches to,
  grading state, who verifies) before the grading model exists. It belongs to
  [[processes/distributed-workflow/active/learning-enforcement]], which owns that design.
- **The grading / anti-cheat / gamification vision gets its OWN tracker**
  ([[processes/distributed-workflow/active/learning-enforcement]]) rather than becoming Phase 6+ here — the
  Phase 5 arc is closed and that vision is a multi-phase workstream in its own right.
- **Its first session is a deep-research + design session**, and its boot prompt is authored **after Phase 6
  lands** (Paul's sequencing), so the research starts from the real post-Phase-6 code.

## Session Log

### 2026-07-18 — workstream created
- Mastery Layer content workstream reached content-complete (Phases 1–4 + 4b Tier-1 pass). Paul chose the next
  phase: a Learning Platform UI (see Decisions). Spun this tracker off from mastery-layer; wrote the Phase 5a
  design boot prompt below. No app code yet — 5a is design-only.

### 2026-07-18 — Phase 5a (design session) ✅
- approach: Opus main session. Read CLAUDE.md + this tracker; surveyed the content spine (mastery/README,
  unified/learning-path + tracker, unified/README) and the canonical architecture docs (phase3-frontend,
  trade-schema, phase2-project-structure, phase4-coach-frontend, monorepo-migration); ran one Explore agent
  over the actual `neurospect-app/src` to inventory lift-vs-leave-behind. Put the three load-bearing forks to
  Paul via AskUserQuestion before designing.
- decided (Paul's forks, redirected from my recommendations): **(1) separate self-contained backend** (not
  sharing `neurospect-api`); **(2) a brand-new model-aligned journal** (fields trace to the taught unified/
  entry-model decision flow; `mode: backtest|live` powers both axes) — not the generic `trades` schema;
  **(3) Content API** served by the new backend via an ingest job (wiki stays canonical).
- did: wrote the ONE canonical design doc [[concepts/architecture/learning-platform]] (new-app shape, lifted
  frontend stack + mirrored backend, U0–U6 route taxonomy, content API + ingest, the three-part data model
  [concepts/concept_progress + model-aligned journal_entries + computed gate], component + API surface, 5b–5g
  split). Named it `learning-platform.md` (not the boot prompt's `-frontend`) because the design spans a full
  backend — one doc avoids two-doc drift. Added 5b–5g phases above; additive cross-links from mastery/README +
  unified/README + phase3-frontend-structure; updated index.md; appended log.md.
- flagged (Rule #6): shipped `neurospect-app` versions (Vite 8 · TS 6 · ky 2 · Zod 4 · Recharts 3 · Tailwind 4
  · Router 7.14) diverge from [[concepts/architecture/phase3-frontend-structure]] (Vite 6 · ky 1). Code is
  ground truth; that doc is the `journal-analytics` lane's — flagged for Paul, NOT edited from this session.
- verified: isolation clean (no ALDC refs); no-drift honored (the doc LINKS the mastery/content pages, never
  restates); design-only (no app code written).
- next: Phase 5b — scaffold `neurospect-learn` (boot-promptable; write its boot prompt when 5b starts).

### 2026-07-19 — Phase 5b (scaffold) ✅
- approach: Sonnet main session executing the approved 5b boot prompt. Read the design doc + tracker in full,
  surveyed both lift sources, then COPY-not-author: bulk-copied the proven spine and pruned/renamed/rewrote only
  the domain files.
- did: created `C:\Users\PaulRussell\repos\neurospect-learn` (`app/` frontend + `api/` backend, `git init` only,
  no commit). **Frontend:** lifted `main.tsx`/`lib/{api,auth,utils}`/20 `ui/` primitives/layout shell/
  `login`+`auth-callback`; renamed the localStorage token key → `neurospect_learn_token`; rewrote `App.tsx`
  route table (public `/login`+`/auth/callback`; `ProtectedLayout` wrapping `/path`,`/path/:stage`,`/library`,
  `/concepts/:slug`,`/drills`,`/journal`,`/journal/new`,`/journal/:id`,`/expectancy`,`/gate`; `/`→`/path`);
  new sidebar navItems (Path/Library/Drills/Journal/Expectancy/Gate, lucide icons); generic `StubPage`;
  `types/api.ts` reduced to auth shapes; rebranded to "Neurospect Learn". **Backend:** stripped to the
  users-only slice — `config` (DB/JWT/Discord/CORS/DEBUG only), `database`/`deps`/`auth/{discord,jwt,router}`
  lifted, `schemas/auth.py` (TokenResponse/UserResponse), `models/{base,user}` + empty `enums.py`, fresh
  `main.py` (health + auth router) and `alembic 0001_initial_users` (trigger fn + `users` + trigger).
- diverged (recorded in [[concepts/architecture/learning-platform]] §5b as-built): **(1)** the lifted
  `index.css` had no Tailwind-v4 `@theme` block, so shadcn semantic utilities weren't emitted — added an
  `@theme inline` token bridge (verified against the built CSS); **(2)** dropped `recharts` (→5f) and
  `react-day-picker`+`ui/calendar.tsx` (unused in 5b); **(3)** dropped `boto3`/`anthropic`/`gunicorn`, added
  `python-dotenv`. Backend lift source was `…\neurospect\neurospect-api`.
- verified (evidence, not inference): backend — `poetry install` clean, `alembic upgrade head` created `users`
  (+ unique `discord_id`, trigger) against a throwaway Postgres 16 container, `/health`=200, `/docs` loads,
  `POST /auth/debug/token`→JWT, `GET /auth/me` w/ Bearer→the user, no-token→403. frontend — `npm install` clean,
  `tsc -b`+`vite build` clean, browser (claude-in-chrome): logged-out `/journal`→`/login`, debug-login→`/path`,
  all six nav items render with active-state highlighting, `/concepts/:slug` stub shows the slug param, no
  console errors. Throwaway DB container + dev servers torn down after.
- isolation: clean (Neurospect-only; no ALDC refs). git: `git init` only — Paul handles commits.
- next: Phase 5c — data model + migrations (write its boot prompt when 5c starts).

### 2026-07-19 — Phase 5c (data model + migrations) ✅
- approach: Sonnet main session executing the approved 5c boot prompt. Read the design spec + trade-schema
  conventions + the U0–U6 taxonomy (learning-path + tracker) + the live `api/` pattern (models/user.py,
  0001 migration, env.py), then built to the established idiom (raw-SQL `op.execute`, reuse `update_updated_at()`).
- did: **enums** (`app/models/enums.py`, 8 fresh Postgres enums + a `pg_enum()` `create_type=False` helper).
  **Models** (SQLAlchemy 2.0 `Mapped`/`mapped_column`, mirroring user.py): `concept`, `concept_progress`,
  `content_page`, `journal_entry`; registered in `models/__init__.py` + `alembic/env.py`. **Migrations**:
  `0002_learning_progress` (`u_stage` enum + `concepts` + `concept_progress` + `content_pages` + triggers +
  indexes + the `U5≠core` CHECK), `0003_journal_entries` (7 journal enums + `journal_entries` + trigger + GIN
  on `mistake_tags`/`confluence_tags`). **Seed** `api/scripts/seed_concepts.py` — idempotent UPSERT-on-slug,
  41 concepts from the taxonomy (`is_core` traces to the tracker's `**core**` tags; all 12 U5 rows watch-only
  with their TIER/label). **Finalized the journal field set** (§5c as-built in the design doc): `aura_asset_leg`
  included, `entry_pda DEFAULT 'fvg'` (R4), `position_size`/screenshots/`missed_trades` deferred with rationale.
- verified (evidence, not inference; local Postgres 16 on :5433): `alembic upgrade head` 0001→0003 clean +
  `downgrade base` and back up clean (reversible); `\d` confirms 4 tables, 8 enums, 5 triggers, all
  constraints/indexes/GIN + FKs (`concept_progress→users,concepts`; `journal_entries→users`); seed → 41 rows
  (10 core, 0 U5-core, spot-checks correct), re-run idempotent (41 rows / 41 distinct slugs, no dupes); both
  CHECK constraints reject bad rows (U5-core, ladder=9); `import app.models.concept, …journal_entry` clean;
  `uvicorn app.main:app` → `/health`=200 with new models registered.
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Progress + journal data model
  to the as-built field set + added §5c as-built; did NOT touch trade-schema.md or phase3-frontend-structure.md.
- isolation: clean (Neurospect-only; no ALDC refs). git: untouched — Paul handles commits.
- next: Phase 5d — content API + ingest + library/reader (write its boot prompt when 5d starts).

### 2026-07-20 — Phase 5d (content API + ingest + library/reader) ✅
- approach: Opus main session executing the approved 5d boot prompt. Read the design spec §Content delivery +
  §5c as-built + the live 5b/5c backend/frontend idioms, surveyed the wiki content dirs + the seeded
  `content_slug` values, then built to the established pattern (ingest mirrors `seed_concepts.py`; router mirrors
  `auth/router.py`; schemas mirror `schemas/auth.py`; frontend data-fetch mirrors `lib/api.ts` + TanStack Query).
- did: **ingest** `api/scripts/ingest_content.py` (async UPSERT-on-slug + stale-prune, `--dry-run`) parsing 67
  pages across the six curated dirs → `content_pages` (title from H1, tags/category/source_path, resolved
  wikilink slugs; tolerant of one malformed-frontmatter file). **Slug scheme** = basename + `NN-`-strip +
  README→dir + leftward de-collision with a **depth tiebreak**. **Backend**: `WIKI_CONTENT_ROOT` config +
  `.env.example`; `app/schemas/content.py`; `app/routers/content.py` (`/api/content/pages|/pages/{slug}|/search`,
  auth-gated, badge from the referencing concept); mounted in `main.py`. **Frontend**: `react-markdown` +
  `remark-gfm` + `@tailwindcss/typography`; `lib/content.ts` (hooks + lookup-based wikilink resolver);
  `components/content/{badges,markdown-renderer}.tsx`; `pages/{library,concept-reader}.tsx`; wired the two 5d
  routes (replaced stubs). **Playwright** harness (Paul's request): config + `global-setup` (debug-JWT →
  storageState) + `e2e/content.spec.ts` (6 specs).
- decided (the calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5d as-built):
  slug scheme + the depth-tiebreak that keeps `consolidation-model` on the entry-model page; backend-owns-scheme /
  frontend-resolves-by-lookup split; reader badge sourced from the concept (no page carries tier/label); content
  shared but auth-gated. **No seed change and no Alembic 0004** — the 5c `content_pages` shape sufficed and all 27
  non-null `content_slug`s resolve as-is.
- verified (evidence, not inference; local Postgres :5433 + wiki readable): ingest → 67 rows, re-run idempotent;
  **reconciliation SQL: 0 unresolved non-null `content_slug`** (4 intentional NULLs remain); spot-checks correct
  (collision winner, numeric-stripped course lessons, de-collided mastery slugs, tags/wikilinks populated).
  endpoints — no-token 403, list 67 grouped, page detail w/ body + frontier badge `{U5,Tier 2,EMERGING,
  watch_only}`, 404 unknown, search hits, `q<2` → 422. frontend — `tsc -b` + `vite build` clean, no console
  errors; browser (claude-in-chrome, debug-login): library grouped corpus, reader markdown+table+blockquote,
  wikilink SPA click-through (`quarterly-theory` → `power-of-three`), unresolved `[[entities/people/doomer]]`
  inert, frontier badges, search filters to 4. Two real bugs caught + fixed in-browser (react-markdown
  `urlTransform` stripping the `wikilink:` scheme; media-vs-class `dark:prose-invert` contrast) + a duplicate-H1
  wart. Playwright: **6/6 green** (`npm run test:e2e`). Dev servers/DB left running for the session; Paul handles git.
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Content delivery to as-built +
  added §5d as-built + marked 5d ✅ in the split; did NOT touch trade-schema.md or phase3-frontend-structure.md.
- flagged: the app's `dark:` variant is media-based while the shadcn theme is class-based — a latent mismatch
  inherited from the 5b lift that will bite any future `dark:` utility (handled locally for the reader).
- next: Phase 5e — progress tracker (`/path` + `/path/:stage` + concept-progress editing + `/drills`); write its
  boot prompt when 5e starts.

### 2026-07-20 — Phase 5e (Study Planner + progress layer) DESIGN ✅
- approach: Opus main session, plan mode, `/effort high`. Read the wiki CLAUDE.md + this tracker + the design
  doc [[concepts/architecture/learning-platform]] in full; read the curriculum the planner schedules against
  ([[concepts/mastery/README]] ladder/confidence/gate, [[concepts/mastery/unified/learning-path]] U0→U6 stages +
  exit bars, [[concepts/mastery/unified/tracker]] grid, both `exercises.md` drill libraries); ran two Explore
  agents (Sonnet) over the live `neurospect-learn` `api/` + `app/` to pin the exact build-against idioms.
- decided (put 3 product forks to Paul via AskUserQuestion): **(availability)** per-weekday minute budget +
  max-session + timezone + blackout dates + optional target date; **(horizon)** plan to each stage gate with a
  **pacing-only ETA** — a target go-live date never gates (the evidence-based Readiness Gate stands);
  **(build split)** deferred to me → **3 sub-phases** 5e-1 progress foundation / 5e-2 planner engine / 5e-3
  planner UI. Engineering calls I made: **hybrid persist-vs-compute** (future computed on read, past+today frozen
  into `plan_items` for a real adherence record); a **deterministic gate-aware scheduler** (unlock → backlog →
  rep-target parse → mandatory spaced review → daily packing → ETA projection → slippage carry-over); a `drills`
  catalog **seeded from the two `exercises.md` drill-map tables**; a `rep_targets` freetext parser that defaults
  conservatively and never invents targets.
- did: extended the ONE canonical doc [[concepts/architecture/learning-platform]] — added §Study Planner
  (availability, scheduler, hybrid persist/compute, ETA/pacing, north-star enforcement per feature), folded the
  redefined 5e into §Progress + journal data model (new subsection: `concept_progress` lifecycle,
  `study_preferences`/`plan_items`/`drill_progress`/`drills` DDL sketch + 3 enums, the stage exit-bar
  derivation), §Route/page taxonomy (`/today`,`/plan`,`/plan/setup`), §Component/API surface (planner components
  + `learning`+`planner` endpoints + the first-`useMutation` + `dark:`-fix infra notes), and revised the
  §Implementation split (5e → 5e-1/5e-2/5e-3). Marked Phase 5e DESIGNED ✅ above; added additive cross-links from
  [[concepts/mastery/README]] + [[concepts/mastery/unified/learning-path]]; updated index.md; appended log.md.
- surfaced from the code survey (fed into the design): the planner introduces the **first `useMutation`** in the
  app (5b–5d were read-only); `progress`/`calendar`/`slider` shadcn primitives + `recharts`/`react-day-picker`
  are **not present** (calendar → lightweight custom CSS-grid + `date-fns`); the `dark:` media-vs-class mismatch
  (§5d as-built) to fix in 5e-1.
- flagged (integrity): the stage exit-bar rules live in code (`services/stages.py`) as *as-implemented* — reconcile
  if learning-path changes; U0/U4 gates partly self-attested until 5f/5g; freetext `rep_target` → conservative
  parser, optional future structured seed column recommended not required.
- verified (design-session = doc integrity): isolation clean (no ALDC refs); no-drift honored (design LINKS the
  curriculum + extends the single canonical doc, no competing doc, no restated curriculum); frontier watch-only /
  never-live-eligible preserved; all 7 boot-prompt decision areas covered; no app code written.
- next: Phase 5e-1 — progress foundation (write its build boot prompt when 5e-1 starts).

### 2026-07-20 — Phase 5e-1 (progress foundation) ✅
- approach: Opus main session executing the approved 5e-1 boot prompt. Read the design doc contract (§Progress
  data model 5e subsection + §Route taxonomy + §Component/API surface), the grading model (mastery/README +
  unified/learning-path stage gates + tracker) and both `exercises.md` drill-map tables, then the live 5b–5d
  backend/frontend idioms, and built to the established pattern (raw-SQL Alembic mirroring 0002/0003; router +
  schemas mirroring content; seed mirroring seed_concepts; frontend data-fetch mirroring lib/content.ts).
- did: **migration** `0004_drills_progress` (raw-SQL, reversible) — `drill_variant` enum + `drills` (seed/content,
  no soft-delete; `drill_ref` UNIQUE, `track` CHECK, `concept_slugs[]` + GIN) + `drill_progress` (user-scoped,
  soft-deleted; `UNIQUE(user_id,drill_ref) WHERE NOT is_deleted`). **models** `drill.py`/`drill_progress.py`
  (registered in `models/__init__.py` + `alembic/env.py`). **seed** `scripts/seed_drills.py` — parses the two
  drill-map tables, expands compound refs (`D0-a…e`, `D4-a/b`, `T-01…14`, `Stage 7`→`S7`), `concept_slugs`
  reverse-derived from the concept seed's `drill_refs`; **53 drills** (aura 16, ict_course 37), idempotent on
  `drill_ref`. **services** `rep_targets.py` (pure freetext→(kind,count) parser — reps/days/sessions/qualitative/
  habit; conservative, never invents a target) + `stages.py` (pure exit-bar service, computed never stored;
  U0–U4 gates encoded as the as-implemented gate, U5 watch-only/never-gate-eligible, U6 = 5g placeholder).
  **`learning` router** (`/api`, auth-gated, user-scoped): GET concepts/progress/stages/drills, PATCH progress
  (lazy upsert + the ladder-advance enforcement + the frontier watch-only cap), PATCH drills; mounted in main.py.
  **frontend**: `lib/learning.ts` (learningKeys + the FIRST `useMutation`s in the app); `types/api.ts` learning
  types; components StagePath/StageNode (rings + locked/watch-only), ExitBarGate, LadderBadge, ConfidenceRating,
  RepCounter, ConceptTrackPanel, DrillCard; pages `/path`, `/path/:stage`, `/drills` (replaced the stubs) + the
  track panel on the reader; `shadcn add progress`; added `@custom-variant dark` (the §5d-flagged mismatch fix).
- decided (the calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5e-1 as-built):
  `track` as a CHECK-VARCHAR (only `drill_variant` is an enum in 0004); compound drill-ref expansion so refs
  match `concepts.drill_refs`; the 4 aura Stage-0 drills the aura map omits are reported as orphan refs (faithful,
  not invented); PATCH builds its response from the committed values (not an ORM re-read — `expire_on_commit=False`
  returns the stale row); `stages.py` splits `auto_met` (objective) from `met` (incl. self-attest) so U0/U4's
  un-wired attestations don't hard-lock the curriculum; ExitBarGate shows the true bar status (lock shown
  separately) so a met-but-locked stage still reads "met".
- verified (evidence, not inference; local Postgres :5433 + wiki readable): `alembic upgrade head` 0001→0004 +
  `downgrade 0003` and back up clean (reversible); seed_drills 53 rows, re-run idempotent (53/53 distinct).
  **API 15/15** (self-written harness): lazy create; re-PATCH updates in place (unique partial index holds);
  per-user isolation (2nd user sees none); CHECK/validation reject ladder=9/confidence=9; ladder-advance
  enforcement rejects premature Can-mark (reps<target or no confidence); U1 gate flips met↔not on the 5-primitive
  fixture; U5 watch_only + never_gate_eligible; drill mark persists; unknown concept 404; no-token 403.
  `tsc -b` + `vite build` clean. **Playwright 10/10** (6 content + 4 new learning: path spine, reader edit-persist,
  stage exit-bar flip, drill mark). Browser (claude-in-chrome, debug-login): `/path` U0→U6 spine with rings +
  locked/unlocked + watch-only + attestation-pending; `/path/U1` exit-bar checklist reflecting concept_progress +
  the editable ConceptTrackPanel; `/drills` cards with ✋/🛠 + rep counters + concept back-links; no console errors.
  Two real fixes caught mid-verify: ON CONFLICT partial-index predicate (`IS false` ≠ `NOT is_deleted`) and the
  stale-ORM-read on PATCH response. Dev servers/DB left running for the session; Paul handles git.
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Progress data model (5e subsection)
  + §Component/API surface to as-built + added §5e-1 as-built + marked 5e-1 ✅ in the split; did NOT touch
  trade-schema.md or phase3-frontend-structure.md.
- isolation: clean (Neurospect-only; no ALDC refs). git: untouched — Paul handles commits.
- next: Phase 5e-2 — planner engine (`study_preferences` + `plan_items` / Alembic 0005 + the scheduler service +
  planner API; reuses the 5e-1 `rep_targets` parser). Write its build boot prompt when 5e-2 starts.

### 2026-07-20 — Phase 5e-1b (multi-track curriculum) DESIGN ✅ / build queued
- trigger: on reviewing the shipped 5e-1 `/path`, Paul flagged it delivered little value — a bare progress grid,
  not a curriculum (no read/drill affordance) — and wanted **per-track paths** (Aura / AXL / Unified), not one
  unified spine. Design dialogue (2 AskUserQuestion rounds) settled it: **parallel tracks**, **separate per-track
  progress** (duplicating a shared primitive is *more reps* + a second explanation that may resonate better), with
  **cross-links** between equivalent concepts across tracks, and **fix the path before the planner**.
- decided (see Decisions 2026-07-20 post-5e-1): three first-class graded tracks with a switcher; per-track
  concepts/stages/drills/progress; `cross_refs` soft links; each stage a curriculum unit (Read → Drill → Track →
  Gate). Engineering shape I set: `concepts` gains `track`/`stage_code`/`stage_order`/`cross_refs` + `u_stage`
  nullable; new `track_stages` seed table; seed grows 41 → ~72 (author ~14 Aura + ~17 AXL rows faithfully from the
  two per-track learning-path pages); `stages.py` generalizes to a data-driven per-stage gate; new `GET /api/tracks`
  + `/path/:track/:stage`; Alembic `0005` (planner bumped to `0006`).
- did (this session = wiki design only, no app code): extended the canonical doc [[concepts/architecture/learning-platform]]
  — added §Multi-track path redefinition + §Multi-track data model, rewrote §Route taxonomy (switcher +
  `/path/:track/:stage` curriculum unit), inserted **5e-1b** into §Implementation split (planner → 0006); added
  the Decisions block + the 5e-1b Plan entry + the 5e-1b build boot prompt above; appended log.md; bumped index.md.
- verified: read both per-track curricula (aura/learning-path.md, course/README.md) to confirm the seed mapping is
  a faithful projection (no invention); isolation clean (no ALDC); no-drift (tracks CONSUME/LINK the wiki paths).
- next: execute the 5e-1b build boot prompt (fresh session recommended — the current session already shipped 5e-1
  end-to-end). Then 5e-2 planner.

### 2026-07-21 — Phase 5e-1b (multi-track curriculum) BUILD ✅
- approach: Opus main session executing the approved 5e-1b boot prompt (no plan mode). Read the design contract
  (§Multi-track path redefinition + §Multi-track data model + §Route taxonomy + §5e-1 as-built), both per-track
  curricula + both `exercises.md`, the grading model, and the live code extended (`concept.py`, `seed_concepts.py`,
  `stages.py`, `learning.py`/`schemas`, `seed_drills.py`, `path.tsx`/`stage-detail.tsx`/`stage-path.tsx`/
  `concept-track-panel.tsx`/`lib/learning.ts`/`types/api.ts`).
- built: Alembic `0005_multi_track` (concepts +track/stage_code/stage_order/cross_refs, u_stage nullable;
  `track_stages` metadata table — **no concept_slugs**, grouping by (track, stage_code)); `models/track_stage.py`
  + registration; `seed_concepts.py` (unified backfill + 14 Aura + 19 AXL rows + `EQUIV_GROUPS` cross_refs);
  new `seed_tracks.py` (23 track stages); `seed_drills.py` re-pointed to same-track `concept_slugs`; generalized
  `stages.py` (`compute_stages(track, metas, concepts, progress)` — unified keeps exact U0–U6, aura/ict generic
  rule); `learning.py` (`GET /api/tracks`, `GET /api/stages?track=`, `?track=` on concepts/progress) + schemas
  (`StageRollup`/`StageOut`/`TrackOut`); frontend `/path` track switcher + `/path/:track/:stage` curriculum unit
  (Read→Drill→Track→Gate) + `useConceptIndex` "Also taught in" cross-links.
- decided (calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5e-1b as-built):
  `track_stages` metadata-only (group by concept columns, no denormalised slug array — anti-drift); concept-less
  stages (unified U6, aura A4–A6, ict M6–M8 = backtest/live/journal) carry no gradable concepts + an attest
  placeholder gate (faithful — the wiki authors those as drills); generic gate = foundation-stage behavioural +
  attest / concept-stage core@Can-mark+conf3+reps / concept-less attest; `cross_refs` from validated `EQUIV_GROUPS`
  (symmetric, never same-track); `drills.concept_slugs` keyed by (track, ref) so back-links stay same-track. Final
  counts: concepts 41→74 (aura 14 / ict 19 / unified 41), track_stages 23, drills 53.
- verified (evidence): alembic `0001→base→head` up/down/up clean (fixed a downgrade FK bug — clear dependent
  `concept_progress` before deleting non-unified concepts); seeds idempotent + per-track counts reported; SQL —
  0 unresolved content_slug, 0 unresolved cross_ref, 0 orphan concept stages, 0 cross-track drill links, 44
  concepts carry cross_refs; `GET /api/tracks` → 3 tracks w/ their stages; **per-track isolation proven** (marking
  Aura A1's cores flips only Aura A1; Unified U1 0/5 + ICT M1 0/2 untouched; unified `u1-1` stays None); gate flips
  per track; `tsc -b` + `vite build` clean; **Playwright 12/12 green** (6 content + 6 multi-track: switch,
  curriculum unit, reader edit, per-track isolation, cross-link jump, drill mark). The live claude-in-chrome visual
  walkthrough was **not** separately run (Chromium e2e covers the behaviours).
- reconciled: updated [[concepts/architecture/learning-platform]] §Multi-track data model + §Route taxonomy →
  as-built + added §5e-1b as-built + marked 5e-1b ✅ in the split + the top banner; did NOT touch trade-schema.md
  or phase3-frontend-structure.md. Appended log.md; bumped index.md. Paul handles git — did NOT commit.
- ops note (not code): mid-verification Docker Desktop stopped (DB container dropped) and an earlier full
  `alembic downgrade base` had emptied `content_pages`; restarted Docker + the container, re-ran all seeds **and
  `ingest_content` (67 pages)**. Several stray background uvicorns were spawned during verification and cleaned up;
  one server currently runs on :8000 with current code.
- next: Phase 5e-2 — planner engine (`study_preferences` + `plan_items` / Alembic `0006` + the deterministic
  `scheduler` service + planner API; reuses the 5e-1 `rep_targets` parser). Write its build boot prompt when 5e-2
  starts.

### 2026-07-22 — Phase 5e-2 (Study Planner engine) BUILD ✅
- approach: Opus main session executing the approved 5e-2 boot prompt (no plan mode). Ran STEP 0 (all pass:
  alembic 0005, seeds 74/23/53/67, `/api/tracks`=3, `/stages?track=aura`=A0–A6, frontend `tsc -b`+`vite build`
  clean). Read the design contract in full (§Study Planner + §Progress data model §4 + §Component/API surface +
  §5e-1/§5e-1b as-built) and the live code reused (`stages.py`/`rep_targets.py`/`learning.py`/`concept*` +
  `drill*` models/`enums.pg_enum`/`0004`+`0005` migration idiom).
- built: Alembic `0006_study_planner` (raw-SQL, reversible; enums `plan_activity` + `plan_item_status`;
  `drill_variant` reused from 0004; `study_preferences` [+ `active_track`, per the 5e-1b reconciliation] +
  `plan_items` with the `NULLS NOT DISTINCT` slot index for idempotent materialize); models
  `study_preferences.py` + `plan_item.py` (registered in `models/__init__.py` + `alembic/env.py`); the pure
  DB-agnostic deterministic `app/services/scheduler.py` (unlock→backlog→rep-parse→spaced-review→daily-pack→
  projection→slippage; signature reconciled with an added `stage_metas` arg + a `ScheduleResult` bundle);
  `app/schemas/planner.py`; `app/routers/planner.py` (GET|PUT `/preferences`, GET `/plan/today`, GET `/plan`,
  POST `/plan/regenerate`, PATCH `/plan/items/{id}`) mounted in `main.py`.
- decided (calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5e-2 as-built):
  `schedule(…, stage_metas, …)` track-scoped signature + `ScheduleResult` (design predated multi-track);
  foundation concepts get Learn/Drill **and** a recurring daily Habit; count-y drills = one task carrying
  remaining reps, day/session drills = one session/day (longitudinal); lowest unlocked concept-less stage = one
  `backtest` placeholder; Leitner intervals conf 1→1d…5→21d; est-minutes per activity capped at
  `max_session_minutes`; habits mandatory (may drive a day's budget negative); PATCH-item feeds reps +
  last_practiced but never advances the ladder (gate stays with `/api/progress`).
- verified (evidence): alembic `0001→head→base→head` clean on a **throwaway** DB + `0006` down/up on the working
  DB (seed + `drill_variant` preserved); **9 scheduler unit tests with NO DB** (determinism, per-track unlock,
  locked stages never scheduled, U5 observe-only+capped, blackout/0-budget skips, max-session cap, spaced-review
  due dates, slippage re-queue, pacing-only projection); **7 API tests** (prefs round-trip, `/plan/today`
  idempotent [0 dupes], PATCH feeds concept + drill progress, regenerate bumps `plan_version` + preserves a done
  item, per-user isolation, 5e-1b `/tracks`+`/stages` no-regression); live uvicorn boot — all 5 routes mount, a
  `PUT prefs → GET /plan/today` flow returns tz-aware habits/learn + adherence + pace; **Playwright 12/12 green**
  (5e-1b regression after the reseed below).
- reconciled: updated [[concepts/architecture/learning-platform]] §Study Planner (header + as-built scheduling
  reconciliation) + §Progress data model §4 (`study_preferences`/`plan_items` → as-built, `0005`→`0006`,
  `active_track`, `NULLS NOT DISTINCT`) + added §5e-2 as-built + marked 5e-2 ✅ in the split; did NOT touch
  trade-schema.md or phase3-frontend-structure.md. Appended log.md; bumped index.md. Paul handles git — did NOT
  commit.
- ops note (evidence-gating lesson): a scratch `alembic downgrade base → upgrade head` intended for a throwaway DB
  ran against the **working** DB (an exported `DATABASE_URL` did not override the `.env`-derived settings Alembic
  reads), wiping the seed. Recovered by re-running all seeds + `ingest_content` (74/23/53/67 restored; Playwright
  12/12 green after). Never run `downgrade base` against the working DB — pin scratch tests to a scratch DB via
  config, not an env export.
- next: **Phase 5e-3 — Planner UI** (`/today` prescriptive daily view, `/plan` calendar, `/plan/setup` availability
  form; wire mark-done → progress; streak / adherence / pace surfaces). Write its build boot prompt when 5e-3
  starts. The planner engine + API it consumes are live and tested.

### 2026-07-23 — Phase 5e-3 (Study Planner UI) BUILD ✅
- approach: Opus main session executing the approved 5e-3 boot prompt (no plan mode). Ran STEP 0 (all pass:
  alembic `0006 (head)`; seeds 74/23/53/67; planner API live — prefs round-trip + `/plan/today` items>0 + range +
  regenerate + patch all respond; backend `pytest` 16/16; frontend `tsc -b`+`vite build` clean + Playwright 12/12).
  Read the design contract in full (§Study Planner + §Route taxonomy + §Component/API surface + §5e-2 as-built —
  the exact Pydantic schemas in `schemas/planner.py`) + the live frontend idioms (`lib/learning.ts` query/mutation
  pattern, `App.tsx`/`sidebar.tsx`, `stage-detail`/`concept-track-panel`/`drill-card`/`rep-counter`, the e2e
  harness). Frontend-only — consumed the 5e-2 API unchanged.
- built: `types/api.ts` planner types (mirroring `schemas/planner.py`); `lib/planner.ts` (`plannerKeys` +
  `usePreferences`/`useUpdatePreferences`/`usePlanToday`/`usePlanRange`/`useUpdatePlanItem`/`useRegenerate` — a mark
  invalidates the learning subtrees too, since it feeds progress); `components/planner/` — `TodayList`,
  `PlanItemCard` (done/partial/skip → PATCH; carried-over + status styling; computed future items read-only),
  `StudyCalendar` (a **custom Mon-first CSS-grid month calendar** via `date-fns`, per-day status dots + count,
  today ring-highlit, past frozen / future projected, Regenerate + `unplaced` warning — **no `react-day-picker`**),
  `AvailabilityForm` (RHF+Zod — weekday minutes, max-session, timezone auto-default, `active_track` Select,
  blackout chips, pacing-only target date), `StreakBadge`/`AdherenceMeter`/`PaceProjection`; pages `/today`,
  `/plan`, `/plan/setup` + the three routes in `App.tsx` + Today/Plan in `sidebar.tsx`.
- decided (recorded in [[concepts/architecture/learning-platform]] §5e-3 as-built): mark → invalidate BOTH
  `plannerKeys.all` + `learningKeys.all`; blackout dates in local state merged on submit (not RHF); Zod number
  schemas plain `.int().min().max()` (dropped `invalid_type_error` — changed in Zod 4); done sends
  `done_qty=target_qty`; computed future items (`id===null`) render read-only.
- bug caught + fixed IN THE LIVE BROWSER: `AdherenceMeter` multiplied `adherence_pct` by 100 → rendered **2500%**;
  the backend already returns a 0–100 percentage (the schema comment omits the ×100). Fixed to render directly.
- verified (evidence, not inference): `tsc -b` + `vite build` clean; **Playwright 17/17** (12 existing regression +
  5 new planner: setup→ordered non-empty Today; mark-done flips `data-status` + surfaces adherence + **feeds
  progress** via `/api/progress` cross-check; skip logs a SKIP; calendar shows today's dots; regenerate bumps
  `plan_version`) — the planner specs run serially against their **own isolated debug user** (`addInitScript`) so
  they don't race with `learning.spec`. Live claude-in-chrome walkthrough (debug-login → `/plan/setup` save →
  `/today` mark-done + skip → `/plan` calendar → regenerate) with **NO console errors** (the 2500% bug was caught
  here). Ops note: the API `CORS_ORIGINS` allows only `:5173`, so the dev server must run there for `/auth/me`.
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Study Planner header + §Route
  taxonomy + §Component/API surface → as-built + added §5e-3 as-built + marked 5e-3 ✅ in the split; did NOT touch
  trade-schema.md or phase3-frontend-structure.md. Appended log.md; bumped index.md.
- isolation: clean (Neurospect-only; no ALDC refs). git: untouched — Paul handles commits.
- next: **Phase 5f — Journal + expectancy** (model-aligned `/journal` [backtest|live] + `/expectancy` dashboard
  per-model, backtest vs live; recharts re-added here). Write its build boot prompt when 5f starts.

### 2026-07-24 — Phase 5f (journal + expectancy) ✅
- approach: Opus main session executing the approved 5f boot prompt (no plan mode). Ran STEP 0 (all pass: alembic
  0006 head; seeds concepts=74/track_stages=23/drills=53/content_pages=67; `journal_entries` + 7 enums present;
  16 backend tests; `tsc -b`+`vite build` clean; Playwright 17/17). Read the design contract (§Progress + journal
  data model §2/§3 + §Route taxonomy + §Component/API surface + §5c as-built) and the live 5b–5e idioms
  (journal_entry/enums models, planner/learning routers + schemas, lib/planner+learning, App.tsx stubs, ui
  primitives), then built to the established pattern (router+schemas mirror planner/learning; frontend fetch
  mirrors lib/planner; pure service + no-DB unit tests mirror scheduler).
- built: **backend** — `schemas/journal.py` (In/Update/Out mirroring the 5c table + 7 enums; `entry_pda` defaults
  fvg), `schemas/analytics.py`, the **pure** `services/expectancy.py` (win/loss by `r_multiple` sign;
  `expectancy == mean r` identity; break-even `1/(1+rr)`; `SAMPLE_TARGET=50` reference, not the gate),
  `routers/journal.py` (CRUD + filters + soft-delete, user-scoped) + `routers/analytics.py` (`/expectancy`,
  `/summary`, `/r-distribution`), mounted in main.py. **NO migration** (built over the existing 5c
  `journal_entries`; deferred items stay deferred). **frontend** — `recharts` re-added; Journal+Analytics types in
  `types/api.ts`; `lib/journal.ts` (a write invalidates journal **and** analytics) + `lib/analytics.ts`;
  components `journal/{journal-form (tabbed RHF+Zod, mode toggle),journal-card,journal-filters}` +
  `analytics/{chart-common,expectancy-chart,backtest-vs-live-chart,r-distribution-chart}`; pages
  `{journal,journal-entry,expectancy}` (replaced the 4 stubs in App.tsx). `--chart-*` palette tokens in index.css.
- decided (calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5f as-built):
  win/loss classified by `r_multiple` sign (not the `outcome` enum) so expectancy is self-consistent + equals
  mean r; `win_rate`/`break_even` returned as fractions 0–1 (UI formats %); sample-target 50 surfaced as a
  reference (amber), explicitly not the 5g verdict; expectancy math in a pure service for hand-fixture unit tests;
  optional form numbers held as strings + coerced on submit; enum selects use a `__none__` sentinel; charts use a
  **dataviz-validated** 2-hue palette (blue backtest / orange live — all six checks pass both modes); added an
  `RDistributionChart` beyond the two named charts; delete is a two-step inline confirm (no native dialog).
- verified (evidence, not inference; local Postgres :5433): backend **33 tests** (16 prior + 9 pure expectancy +
  8 journal API — CRUD, filters narrow, soft-delete [gone from API, row still in DB flagged], per-user isolation,
  enum/CHECK 422, no-token 403, expectancy VIEW over created entries). `tsc -b`+`vite build` clean. **Playwright
  20/20** (17 prior regression + 3 journal: create→list→feeds expectancy, Radix mode filter narrows, charts render
  per-model bars). Live claude-in-chrome walkthrough (debug-login → `/journal/new` create a backtest entry →
  `/journal` list → `/expectancy` dashboard) with **NO console errors**; rendered table + charts cross-checked
  against hand-computed expectancy (Backtest +0.64R/win 55%, Live −0.33R/win 33% — honesty view; London backtest
  +0.20R vs live −0.33R). Dev servers + DB left running; Paul handles git.
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Route taxonomy + §Progress +
  journal data model §3 + §Component/API surface → as-built + added §5f as-built + marked 5f ✅ in the split;
  did NOT touch trade-schema.md or phase3-frontend-structure.md. Appended log.md; bumped index.md.
- isolation: clean (Neurospect-only; no ALDC refs). git: untouched — Paul handles commits.
- next: **Phase 5g — Gate/readiness** (`/gate` computed readiness over progress + backtest expectancy + checklist;
  watch-only enforcement for frontier). Boot prompt written below (✅ EXECUTED 2026-07-24).

### 2026-07-24 — Phase 5g (gate / readiness view) ✅ — **PHASE 5 ARC COMPLETE**
- approach: Opus main session executing the approved 5g boot prompt (no plan mode). Ran STEP 0 (all pass: alembic
  `0006 (head)`; seeds 74/23/53/67; backend 33 tests; `tsc -b`+`vite build` clean; Playwright 20/20). Read the
  design contract (§Progress + journal data model §3 + §Route taxonomy + §Component/API surface + §5e-1/§5f
  as-built) and the canonical Gate in [[concepts/mastery/README]] §Readiness-to-Live Gate, then the live code it
  combines (`services/{expectancy,stages,rep_targets}.py`, `routers/{analytics,learning}.py`, the `0006` migration
  idiom, `concept*`/`journal_entry` models; frontend `lib/{analytics,learning}.ts`, `pages/expectancy.tsx`,
  `App.tsx`, the e2e harness) and built to the established pattern.
- built: **backend** — Alembic `0007_gate_attestations` (raw-SQL, reversible; the `gate_attestation_item` enum +
  `gate_attestations`, user-scoped/soft-deleted with the partial-unique lazy-upsert index), `models/gate_attestation.py`
  (registered in `models/__init__.py` + `alembic/env.py`), the **pure** `services/gate.py` (the verdict — anchor
  track, cross-ref credit, three evidence requirements delegating to the 5f expectancy service, four behavioural
  items, blocking reasons, frontier exclusion, fail-closed guards), `schemas/gate.py`, `routers/gate.py`
  (`GET /api/gate?track=`, `GET|PATCH /api/gate/attestations`) mounted in `main.py`. **frontend** — gate types in
  `types/api.ts`, `lib/gate.ts`, `components/gate/{gate-signal,gate-checklist}.tsx`, `pages/gate.tsx` + the route;
  **deleted `pages/stub.tsx`** (no route is a stub any more).
- decided (the calls the design left open; recorded in [[concepts/architecture/learning-platform]] §5g as-built):
  the gate is **anchored on the unified curriculum** (only track whose taxonomy enumerates all 7 models, as
  U3.2a–g — mapped by explicit slug, the `_U2_GATE_SLUGS` idiom); **`unified` requires all seven at Live-ready**
  (it routes into every model — the advanced track carries the hardest bar); **cross-track `cross_refs` credit
  counts** (Aura study of the same primitive is real evidence) but **`?track=` can only tighten**, so no parameter
  can loosen a verdict; **(c) is all four README items** (not the boot prompt's three), per-user + revocable, with
  **objective journal corroboration shown beside it** rather than invented thresholds; the attestation checkbox is
  **server-controlled, deliberately not optimistic**; `SAMPLE_STRETCH=100` surfaced as non-gating.
- verified (evidence, not inference; local Postgres :5433): `0007` up + `downgrade 0006` + up clean (table + enum
  dropped/recreated, 74-concept seed preserved). **68 backend tests** (33 prior + **24 pure hand-fixture gate
  units** + **11 gate API**): the cleared case then **each of the four inputs flipped** with the right blocking
  reason (incl. positive-expectancy-but-below-break-even, and unknown R:R), frontier never a requirement nor a
  creditor, cross-track credit + `credit_track` tightening both ways, unified-needs-all-seven, missing/empty
  curriculum fails closed, `ALL_MODELS` ≡ the `EntryModel` enum, live activity never gates; the API suite clears a
  **fully satisfied London against the real seed** then flips all four back, plus attest round-trip/revoke,
  non-overridability (all four attested + full ladder + no sample → blocked; a stray `cleared` field ignored),
  per-user isolation, 404/422/403. `tsc -b`+`vite build` clean. **Playwright 27/27** (20 prior regression + 7 new).
  Live claude-in-chrome walkthrough: London **Cleared** (50/50, +0.80R, win 60% vs BE 33%) while all seven other
  models stayed blocked **with all four discipline boxes ticked** — non-overridability visible on the rendered
  surface; checklist 11/11 · 3/3 · 4/4; frontier panel (12 concepts); credit-track selector toggled to "Aura only"
  and back, flipping London Cleared → Not cleared → Cleared. **No console errors.** One copy wart caught
  in-browser and fixed ("across 1 days" → "1 day").
- reconciled (mandatory): updated [[concepts/architecture/learning-platform]] §Progress + journal data model §3
  (the gate → as-built), §Route taxonomy (`/gate` → as-built), §Component/API surface (`gate` endpoints +
  `GateSignal`/`GateChecklist`), §Stage exit-bar derivation (U6 now points at `/gate`), the **stale top banner**
  (it still claimed the Study Planner was unbuilt — 5e-2/5e-3/5f had shipped), and added §5g as-built + marked 5g ✅
  in the split. Also fixed three now-misleading in-app strings that forward-referenced "Phase 5f/5g" as unbuilt
  (`stages.py` ×2, `exit-bar-gate.tsx`) — copy only, no logic change. Did NOT touch trade-schema.md or
  phase3-frontend-structure.md. Appended log.md; bumped index.md.
- isolation: clean (Neurospect-only; no ALDC refs). git: untouched — Paul handles commits.
- ops note: the stale uvicorn on :8000 predated the gate router, so it was restarted (`poetry run uvicorn
  app.main:app --port 8000`); the DB container + dev server on :5173 were already up and are left running.
- next: **Phase 5 is complete.** *(Amended 2026-07-25: the candidate follow-ups listed here were scoped with
  Paul into **Phase 6 — Phase-5 debt**, now ⏭ ACTIVE below — the stage-attestation wiring, the missed-trade log,
  and `position_size`. Screenshots were deliberately excluded and, with the grading/anti-cheat/gamification
  vision, moved to [[processes/distributed-workflow/active/learning-enforcement]]. Deploy/hosting and live
  commentary remain unscoped.)*

## Next Session Boot Prompt (Phase 6 — Phase-5 debt) ⏭ ACTIVE

Recommended launch: **Opus** (`claude --model opus[1m]`), `/effort high` — 6a changes a service every `/path`
stage reads and must not regress the curriculum's lock chain, and 6b/6c touch the journal that expectancy and the
gate compute from (evidence-gated). No plan mode. Full-stack. Working dir:
`C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from the wiki to read the design
first. **Prereq:** the `neurospect-learn-db` container on :5433 with the 5c–5g schema/seed + ingest. If gone:
`docker start neurospect-learn-db`, then `cd api && poetry run alembic upgrade head && poetry run python -m
scripts.seed_concepts && poetry run python -m scripts.seed_tracks && poetry run python -m scripts.seed_drills &&
poetry run python -m scripts.ingest_content`. Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live. The Phase 5 arc (scaffold → data model → content → progress → multi-track curriculum → Study Planner → journal/expectancy → the Readiness-to-Live Gate) is COMPLETE and shipped; migrations are at `0007`.

Neurospect — Phase 6: PHASE-5 DEBT. Three scoped follow-ups that close this workstream. The through-line is the north star — DISCIPLINE & ACCOUNTABILITY BY DESIGN: 6a removes checkboxes the app shows as permanently unmet (a dead checkbox teaches the user the process is theatre), and 6b adds the journaling category the Aura corpus says carries the biggest hidden edge. Do all three; they are independent enough to land in any order.

STEP 0 — CONFIRM 5g SHIPPED (do this FIRST; if any check fails, STOP and tell Paul):
  - Migrations at 0007: `cd api && poetry run alembic current` shows `0007 (head)`.
  - Seeds present: concepts=74, track_stages=23, drills=53, content_pages=67.
  - Backend tests green: `cd api && poetry run pytest tests/ -q` → 68 passed.
  - Frontend baseline: `cd app && npx tsc -b && npx vite build` clean; start the API on :8000 (DEBUG=true) then `npx playwright test` → 27/27 green. (Dev server on :5173 — CORS allows only :5173.)
  Only once ALL pass, proceed.

Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model §2 (the model-aligned journal field set + the DEFERRED list) + §3 (the gate as-built) + §Stage exit-bar derivation + §5c/§5f/§5g as-built. For 6b also read C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\trade-schema.md §Missed Trades (the field set + rationale — **that doc is the `journal-analytics` lane's and describes the OLD `neurospect-app` `trades` schema; READ it, ADAPT it, and do NOT edit it**). The Aura provenance is canonical in C:\Users\PaulRussell\repos\neurospect-wiki\concepts\aura\journaling-system.md — REUSE by reference, do NOT restate.

SCOPE — 6a: WIRE THE STAGE ATTESTATIONS TO REAL EVIDENCE.
  `app/services/stages.py` emits `Requirement(attest=True, met=False)` rows that can NEVER become met — U0's "routine + circuit-breakers held; journaling live", U4's "positive expectancy in R computable from journal" and "risk rules precommitted in writing", the generic foundation-stage attest, and the concept-less (backtest/live/journal) stage attest. All the evidence they were waiting on now EXISTS: the 5g `gate_attestations` store (`risk_precommitted` · `sim_track_record` · `journaling_habit` · `circuit_breaker`, tickable on `/gate`) and the 5f pure `services/expectancy.py`.
  - Map each behavioural attest onto the **5g attestation it already corresponds to** — ONE source of truth, do NOT add a second checkbox on `/path`; the row should reflect the `/gate` tick and link there.
  - Derive the evidence-backed ones (U4's expectancy row; the concept-less backtest/live/journal stages) from the SHIPPED services — REUSE `expectancy.compute_groups` / `compute_mode_summaries` and/or `services/gate.py`, do NOT reimplement any math. Where the wiki names a bar, encode THAT bar; where it does not, keep the row self-attested rather than inventing a threshold, and say so.
  - `stages.py` must stay PURE and DB-agnostic — extend `compute_stages(...)` with an evidence bundle argument (the 5e-2 `stage_metas` precedent) and load it in `learning._compute_track_stages`. The planner also calls `compute_stages` — keep it working (5e-2 tests must stay green).
  - **DECIDE + RECORD, with evidence: does a wired attest now feed `auto_met` / the lock chain?** Today `locked` is computed off `auto_met` precisely so un-wired attests can't freeze the curriculum (§5e-1 as-built). My recommendation: keep `locked` on the concept-based chain (do not freeze a track on behavioural evidence) but make `met` honest. Whatever you choose, prove the lock chain does not regress.
  - Frontend: `ExitBarGate` currently tags every unmet attest "(self-attested)" — update so an objectively-derived row reads as earned, and a genuinely self-attested one links to `/gate`.
SCOPE — 6b: THE MISSED-TRADE LOG (the deferred Aura surface).
  A separate lightweight `missed_trades` table (NOT columns on `journal_entries`) so executed-trade analytics are never diluted by trades never taken. **Adapt the trade-schema field set to THIS app's conventions**: the learn app's journal is deliberately model-aligned, so use the existing `entry_model` + `session_type` enums (not `setup_type`), and follow the `journal_entries` idiom (UUID PK · TIMESTAMPTZ · `update_updated_at()` trigger · user-scoped · soft-delete + partial unique where relevant · GIN on the tag array). New enums `miss_type` (`almost_took|hesitated|canceled`) + `hypothetical_outcome`. **OMIT `missed_trade_screenshots` entirely** — evidence storage belongs to the learning-enforcement workstream (see that tracker); note the omission rather than half-building it.
  - Backend: Alembic `0008` (raw-SQL, reversible, mirroring 0004–0007), model + registration, schemas, a `missed_trades` router (CRUD + filters + soft-delete, mirroring `routers/journal.py`), and the analytic the table exists FOR: **opportunity cost in R** — total/average `hypothetical_r`, split by `miss_type` and by `hesitation_tags`, so "I keep missing runners" becomes a number (and may show that pulling the order was protective). Put the math in a pure service if it is more than a sum, so it can be unit-tested like `expectancy.py`.
  - Frontend: a log + form + the opportunity-cost surface. **DECIDE + RECORD where it lives** — my recommendation is inside `/journal` (a mode/tab alongside entries: this IS journaling, and the north star says the journal covers every trade *including misses*), not a new top-level nav item.
  - **The missed-trade log must NOT enter expectancy or the gate.** Prove it: these are trades that were never taken.
SCOPE — 6c: `position_size` + small journal gaps.
  Add nullable `position_size` (contracts) to `journal_entries` + the form (same `0008` migration is fine — decide and record). Re-read §2 + the §5c as-built DEFERRED list and close anything else genuinely small. **Expectancy stays R-based** — `position_size` is record-keeping; it must not appear in any expectancy, analytics, or gate computation. Screenshots stay deferred.

6 IS NOT: deploy/hosting (explicitly out of scope, Paul 2026-07-25); screenshots / evidence upload / R2 (owned by the learning-enforcement workstream); drill grading, anti-cheat or gamification (same); live-trading or broker integration; changing the expectancy math or the gate verdict; ALDC anything.

VERIFY (evidence, not inference; local Postgres :5433): `alembic upgrade head` + down/up clean (reversible), seeds preserved. **The evidence-gate for this phase is NO REGRESSION IN THE NUMBERS: capture `/api/analytics/expectancy` + `/api/gate` for a fixture user BEFORE and AFTER, and show they are byte-identical** — 6b and 6c add data that must not move expectancy or the verdict. For 6a: pure unit tests (mirroring test_gate.py) proving each wired attest flips with its evidence and stays unmet without it, that the lock chain is unchanged, and that the 5e-2 scheduler still gets the stages it expects; plus a `/path` check that a previously-permanently-unmet row now reflects a `/gate` tick. For 6b: CRUD + filters + soft-delete + per-user isolation + no-token 403, the opportunity-cost analytic on a hand-built fixture with a by-hand answer (incl. a negative `hypothetical_r` reading as protective), and proof missed trades are absent from expectancy/gate. All existing backend tests + Playwright 27/27 still green, EXTENDED for the new surfaces; `tsc -b` + `vite build` clean; a live claude-in-chrome walkthrough of every changed surface (`/path` stage gate, the missed-trade log, the journal form) with NO console errors.
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md — §Progress + journal data model §2 (the deferred list shrinks; `position_size` + `missed_trades` as-built) + §Stage exit-bar derivation (the attests are wired) + §Route taxonomy + §Component/API surface + a §6 as-built; mark Phase 6 ✅ in the tracker + a session-log entry; append log.md; bump index.md. **Do NOT edit trade-schema.md** (the `journal-analytics` lane's) or phase3-frontend-structure.md. **This CLOSES the learning-platform-ui workstream** — say so in the tracker, and point the reader at processes/distributed-workflow/active/learning-enforcement.md, whose deep-research boot prompt is authored once this lands. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5g — Gate / readiness view) — ✅ EXECUTED 2026-07-24

Recommended launch: **Opus** (`claude --model opus[1m]`), `/effort high` — this is the north-star payoff (the
"cleared to live?" verdict) and the readiness logic must be correct + non-overridable (evidence-gated). No plan
mode — this executes the approved [[concepts/architecture/learning-platform]] §Progress + journal data model §3
(the gate) + §Route taxonomy (`/gate`) + §Component/API surface. Full-stack (a `gate` API that COMBINES the
three existing sources + the `/gate` UI). Working dir: `C:\Users\PaulRussell\repos\neurospect-learn` (code is
ground truth), or start from the wiki to read the design first. **Prereq:** the `neurospect-learn-db` container
on :5433 with the 5c+5d+5e+5f schema/seed + ingest. If gone: `docker start neurospect-learn-db`, then
`cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python -m
scripts.seed_tracks && poetry run python -m scripts.seed_drills && poetry run python -m scripts.ingest_content`.
Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live.

Neurospect — Phase 5g: GATE / READINESS VIEW for `neurospect-learn`. Build the "cleared to live?" verdict — a `/gate` that COMPUTES per-model live-readiness by combining the three sources that already exist: (a) core-concept ladder position from `concept_progress` (5e-1), (b) backtest sample + positive expectancy from the journal/analytics (5f), and (c) a behavioural checklist (risk precommitted in writing, journaling habit, circuit-breaker demonstrated — user-attested). This is the north-star payoff: DISCIPLINE & ACCOUNTABILITY BY DESIGN — the gate is NON-OVERRIDABLE (no manual "mark cleared"), frontier (U5/EMERGING/SPECULATIVE) concepts NEVER count toward eligibility, and a model is never "cleared" without the required backtest sample AND positive expectancy AND its core concepts at Backtested+. The expectancy math is ALREADY shipped (5f `services/expectancy.py` + `/api/analytics/expectancy`) — REUSE it, do NOT reinvent it.

STEP 0 — CONFIRM 5f SHIPPED (do this FIRST; if any check fails, STOP and tell Paul):
  - Migrations at 0006: `cd api && poetry run alembic current` shows `0006 (head)`.
  - Seeds present: concepts=74, track_stages=23, drills=53, content_pages=67.
  - Backend tests green: `cd api && poetry run pytest tests/ -q` → 33 passed.
  - Frontend baseline: `cd app && npx tsc -b && npx vite build` clean; start the API on :8000 (DEBUG=true) then `npx playwright test` → 20/20 green (6 content + 6 multi-track + 5 planner + 3 journal). (Dev server on :5173 — CORS allows only :5173.)
  Only once ALL pass, proceed.

Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model §3 (THE GATE: the three sources (a)/(b)/(c), the expectancy formula [now shipped in 5f — reuse], and the INVARIANTS the UI must enforce: no frontier toward "core at Backtested+", never "Backtested+" without the sample, live-eligibility on U1–U4 not confluence), §Route taxonomy (`/gate` row) + §Component/API surface (`gate: GET /api/gate`; `GateChecklist`/`GateSignal`), §5e-1 as-built (the `stages.py` derivation + `concept_progress` shape you read (a) from), §5f as-built (the `expectancy.py` + `/api/analytics/expectancy` you read (b) from — the sample-target 50 is the reference; 5g turns it into the verdict). The Gate text is CANONICAL in [[concepts/mastery/README]] §Readiness-to-Live Gate — REUSE by reference, do NOT restate.

SCOPE — 5g IS:
  - BACKEND `gate` router (`app/routers/gate.py`, prefix /api, auth-gated + user-scoped; schemas `app/schemas/gate.py`): `GET /api/gate` (optionally `?track=`) → per-model readiness: for each entry_model, does it clear (a) its core concepts (U1–U4, is_core, NOT watch_only) at Backtested+ (ladder≥3), (b) backtest sample ≥ target with positive expectancy in R (from the 5f expectancy service — REUSE, do NOT reimplement), (c) the attested behavioural checklist items — and an overall `cleared: bool` per model + the blocking reasons. The (c) checklist attestation needs a store — add a minimal `gate_attestations` table (Alembic 0007, reversible) OR fold into a small user-settings row; decide + record it. Pure readiness logic in `app/services/gate.py` (DB-agnostic, hand-fixture unit-tested like expectancy.py). NON-OVERRIDABLE: no endpoint sets `cleared` directly.
  - FRONTEND: `lib/gate.ts` (`gateKeys` + `useGate` + the attestation mutation); `components/gate/{GateSignal (per-model cleared / blocked signal), GateChecklist (the three source groups with met/unmet + the attestable (c) items)}`; `/gate` page (replaces the 5g stub) — per-model readiness cards + the checklist; frontier concepts shown as never-eligible; a clear "what's blocking live" list per model.
  - North star surfaced: the gate is the one place the whole disciplined process pays off; nothing here is manually overridable; watch-only/frontier never counts; expectancy must be POSITIVE with a real sample, not just logged.

5g IS NOT: changing the expectancy math (reuse 5f); a live-trading integration / broker anything; changing the journal or planner; Claude/AI coaching; ALDC anything.

VERIFY (evidence, not inference; local Postgres :5433): if you added a migration, `alembic upgrade head` + down/up clean (reversible); **gate logic correct on a HAND-BUILT fixture** (a model with core@Backtested+ + sample≥target + positive expectancy + all (c) attested → cleared; flip each of the four → not cleared with the right blocking reason — this is the evidence-gated core); frontier concept never counts toward (a); per-user isolation; no-token 403; `tsc -b` + `vite build` clean; EXTEND Playwright (a fully-satisfied model shows cleared; an unmet one shows blocked with reasons) green AND the existing 20 still green; a live claude-in-chrome walkthrough (debug-login → `/gate` renders per-model readiness + blocking reasons) with NO console errors.
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md §Progress + journal data model §3 → as-built (the gate as shipped) + §Route taxonomy (`/gate` → as-built) + §Component/API surface (`gate` endpoint + `GateSignal`/`GateChecklist` shipped) + add a §5g as-built; mark 5g ✅ in the split + tracker + a session-log entry; append log.md; bump index.md. This COMPLETES the Phase 5 arc — note that in the tracker. Do NOT edit trade-schema.md / phase3-frontend-structure.md. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5f — Journal + expectancy) — ✅ EXECUTED 2026-07-24

Recommended launch: **Opus** (`claude --model opus[1m]`), `/effort high` — the expectancy math must be correct
(evidence-gated) and this introduces the app's **first charts**. No plan mode — this executes the approved
[[concepts/architecture/learning-platform]] §Progress + journal data model + §Route taxonomy + §Component/API
surface. Full-stack (journal API + analytics API + the `/journal`·`/expectancy` UI). Working dir:
`C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from the wiki to read the design
first. **Prereq:** the `neurospect-learn-db` container on :5433 with the 5c+5d+5e-1+5e-1b+5e-2 schema/seed +
ingest. If gone: `docker start neurospect-learn-db`, then `cd api && poetry run alembic upgrade head && poetry run
python -m scripts.seed_concepts && poetry run python -m scripts.seed_tracks && poetry run python -m
scripts.seed_drills && poetry run python -m scripts.ingest_content`. Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live.

Neurospect — Phase 5f: MODEL-ALIGNED JOURNAL + EXPECTANCY DASHBOARD for `neurospect-learn`. Build the empirical proof-of-edge loop: a `/journal` that logs entries with a `backtest | live` mode toggle against the model-aligned field set, and an `/expectancy` dashboard showing per-model win rate / avg R / expectancy / sample size, backtest vs live. The `journal_entries` TABLE ALREADY EXISTS (5c, Alembic 0003) — you build the API + the UI over it; NO new migration is expected (the deferred items — screenshots, `missed_trades`, `position_size` — STAY deferred unless you deliberately add one, in which case Alembic 0007). This is the axis the Readiness Gate (5g) will read; 5f delivers the journal + the expectancy VIEW, NOT the live-eligibility gate. North star: DISCIPLINE & ACCOUNTABILITY BY DESIGN — the journal is prescriptive and honest (backtest vs live never conflated; expectancy shown per model with its true sample; no "cleared to live" signal here — that's 5g).

STEP 0 — CONFIRM 5e-3 SHIPPED (do this FIRST; if any check fails, STOP and tell Paul — do not build on a broken base):
  - Migrations at 0006: `cd api && poetry run alembic current` shows `0006 (head)`.
  - Seeds present: `docker exec neurospect-learn-db psql -U learn -d neurospect_learn -tAc "SELECT 'concepts='||count(*) FROM concepts; SELECT 'track_stages='||count(*) FROM track_stages; SELECT 'drills='||count(*) FROM drills;"` → concepts=74, track_stages=23, drills=53 (content_pages=67).
  - `journal_entries` table exists: `docker exec neurospect-learn-db psql -U learn -d neurospect_learn -tAc "\d journal_entries"` lists the columns + the 7 journal enums.
  - Backend tests green: `cd api && poetry run pytest tests/ -q` → 16 passed.
  - Frontend baseline: `cd app && npx tsc -b && npx vite build` clean; start the API on :8000 (DEBUG=true) then `npx playwright test` → 17/17 green (6 content + 6 multi-track + 5 planner). (Playwright needs the API up on :8000; the dev server must run on :5173 — the API CORS_ORIGINS allows only :5173.)
  Only once ALL pass, proceed.

Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model §2 (the model-aligned `journal_entries` field set — decision-flow capture, execution/risk, frontier stack, review) + §3 (the gate math you REUSE for expectancy: `expectancy = (win% × avg win R) − (loss% × avg loss R)`, break-even `= 1/(1+R:R)`), §Route/page taxonomy (`/journal`·`/journal/new`·`/journal/:id`·`/expectancy` rows), §Component/API surface (the `journal` + `analytics` endpoint lists + `JournalForm`/`JournalCard`/`JournalFilters`/`ExpectancyChart`/`BacktestVsLiveChart`), §5c as-built (CODE is ground truth — the journal enums + field resolutions). Expectancy formula canonical in mastery/README §Readiness-to-Live Gate + [[concepts/aura/risk-management]] — REUSE by reference, do NOT restate.

THE SCHEMA YOU BUILD OVER (code is ground truth — DO NOT change it): `api/app/models/journal_entry.py` + `api/app/models/enums.py` (the 7 journal enums: `journal_mode` backtest|live, `entry_model` [7 models + unified], `range_position`, `session_type`, `entry_pda` [DEFAULT fvg], `outcome`, `grade`). Read them for the EXACT columns + enum values before writing schemas — mirror them in `app/schemas/journal.py` + `types/api.ts`. Expectancy is computed in R (`r_multiple`/`rr_planned`/`risk_pct`), never dollars.

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki content; never touch sources/ or vault/), Architecture Doc Integrity (CODE is ground truth — you MUST reconcile learning-platform.md + add a §5f as-built before sign-off), "Paul handles git — NEVER commit".
2. Run STEP 0 above.
3. Read learning-platform.md §Progress + journal data model §2/§3 + §Route taxonomy + §Component/API surface + §5c as-built IN FULL, and skim §5e-3 as-built (the mutation-domain + charts-absent notes).
4. Skim the live code you extend: api/app/models/{journal_entry,enums}.py, api/alembic/versions/0003_journal_entries.py (the enums + table as-built), api/app/routers/{planner,learning}.py + schemas/{planner,learning}.py (the auth-gated + user-scoped router idiom + Pydantic mirroring you copy), app/src/lib/{planner,learning}.ts (the `<domain>Keys` + `useQuery`/`useMutation`-invalidate pattern — `lib/journal.ts` + `lib/analytics.ts` mirror it), app/src/App.tsx (the /journal* + /expectancy STUBS to replace), components/ui/* (form/input/select/tabs/badge/card already present; RHF+Zod+date-fns installed), and the entry-model pages under concepts/entry-models/** (the decision-flow the JournalForm fields trace to — CONSUME/LINK, never restate).

SCOPE — 5f IS:
  - BACKEND `journal` router (`app/routers/journal.py`, prefix /api, auth-gated + user-scoped; schemas `app/schemas/journal.py`; mount in main.py): `POST /api/journal` (create — validate against the enums; `mode` + `entry_model` required), `GET /api/journal` (this user's entries; filters `?mode=` / `?entry_model=` / `?instrument=` / date range; newest first), `GET /api/journal/{id}`, `PATCH /api/journal/{id}` (partial update), `DELETE /api/journal/{id}` (SOFT-delete — `journal_entries` is soft-deleted). Per-user isolation like `learning`/`planner`.
  - BACKEND `analytics` router (`app/routers/analytics.py`, prefix /api, auth-gated + user-scoped; schemas `app/schemas/analytics.py`): `GET /api/analytics/expectancy` (group `journal_entries` by `entry_model` × `mode`; per group → sample n, win%, avg win R, avg loss R, **expectancy in R** `= (win% × avgWinR) − (loss% × avgLossR)`, break-even `= 1/(1+avg RR)`, computed ONLY over closed trades with a non-null `r_multiple`), `GET /api/analytics/summary` (top-line per mode), `GET /api/analytics/r-distribution` (r_multiple histogram buckets for the chart). Pure aggregation over the user's entries; NO gate verdict (that's 5g). REUSE the expectancy formula from mastery/README §Gate — do NOT reinvent it.
  - FRONTEND lib: `lib/journal.ts` (`journalKeys` + `useJournalEntries`/`useJournalEntry`/`useCreateEntry`/`useUpdateEntry`/`useDeleteEntry` — a write invalidates the journal lists AND the analytics subtree, since expectancy depends on entries) + `lib/analytics.ts` (`analyticsKeys` + `useExpectancy`/`useSummary`/`useRDistribution`). Journal + analytics types in `types/api.ts` (mirror the Pydantic schemas).
  - FRONTEND components under `app/src/components/journal/` + `components/analytics/`: `JournalForm` (tabbed RHF+Zod — Context/Model · Decision-flow · Execution/Risk · Review; the `mode` backtest|live toggle drives both axes; all model-aligned fields per §2; lifts the tabbed trade-form recipe from `neurospect-app` but the field set is the NEW model-aligned one — do NOT copy the generic `trades` shape), `JournalCard` + `JournalFilters` (mode + entry_model + instrument), `ExpectancyChart` (per-model expectancy/win-rate bars), `BacktestVsLiveChart` (the same models, backtest vs live side-by-side — the honesty view). **Re-add `recharts`** (dropped in the 5b lift; `npm install recharts`) for the charts; **do NOT re-add `react-day-picker`** (date inputs, per 5e-3). Before writing ANY chart, load the `/dataviz` skill.
  - PAGES (replace the 4 stubs): `/journal` (list + JournalFilters + a "New entry" button + the mode toggle), `/journal/new` + `/journal/:id` (JournalForm — create/edit), `/expectancy` (ExpectancyChart + BacktestVsLiveChart + the per-model table with sample sizes). Journal + Expectancy are already in the sidebar navItems (5b) — no nav change needed.
  - North star surfaced: backtest vs live NEVER conflated (separate expectancy, separate charts); each model's expectancy shows its TRUE sample size (a small-n model is visibly under-evidenced); frontier `confluence_tags` are stored + shown as study-only; NO "cleared to live" verdict here (5g owns it).

5f IS NOT: the `/gate` live-readiness view + its computation (5g — 5f delivers the expectancy VIEW, not the gate verdict); the `missed_trades` surface / the entry-model YAML→strategy (MACHINE_READABLE_STRATEGY) parser / R2 screenshots / `position_size` (all deferred in 5c — keep deferred unless Paul asks, and if added, Alembic 0007 + reconcile); Claude/AI coaching; backtesting methodology; ALDC anything.

VERIFY (evidence, not inference; local Postgres :5433): if you added a migration, `alembic upgrade head` + down/up clean (reversible); journal CRUD (create → GET returns it; filter by `mode`/`entry_model` narrows correctly; PATCH updates in place; DELETE soft-deletes [row gone from GET, still in DB]; per-user isolation — a 2nd debug user sees none; enum/CHECK validation rejects a bad `mode`/`swing_qualification`; no-token 403); **expectancy math correct on a HAND-BUILT fixture** (insert N trades with known `r_multiple`s per model×mode → assert win%, avg win R, avg loss R, expectancy, break-even match the formula by hand — this is the evidence-gated core); `tsc -b` + `vite build` clean; EXTEND Playwright (create a backtest entry → appears in `/journal` list + feeds `/expectancy`; filter by mode; expectancy chart renders per-model bars; backtest-vs-live split renders) green AND the existing 17 still green (no regression); a live claude-in-chrome walkthrough (debug-login → `/journal/new` create a backtest entry → `/journal` list + filter → `/expectancy` dashboard renders the charts) with NO console errors.
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md §Progress + journal data model §2/§3 → as-built (the journal API + the expectancy computation as shipped) + §Route taxonomy (`/journal`·`/expectancy` → as-built) + §Component/API surface (`journal`+`analytics` endpoints + the shipped component names + recharts re-added) + add a §5f as-built; mark 5f ✅ in the split + tracker + a session-log entry (next=5g gate/readiness); append log.md; bump index.md. Do NOT edit trade-schema.md / phase3-frontend-structure.md. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5e-3 — Study Planner UI) — ✅ EXECUTED 2026-07-23

Recommended launch: **Sonnet** (`claude --model sonnet[1m]`), `/effort medium` — frontend execution against an
**approved design + a live, tested API** (5e-2). Escalate to Opus only if the custom CSS-grid calendar or the
adherence/streak wiring stalls. No plan mode — this executes the approved [[concepts/architecture/learning-platform]]
§Study Planner + §Route taxonomy + §Component structure. Frontend-only (no backend/scheduler change — 5e-2 is
done). Working dir: `C:\Users\PaulRussell\repos\neurospect-learn\app` (code is ground truth), or start from the
wiki to read the design first. **Prereq:** the `neurospect-learn-db` container on :5433 with the
5c+5d+5e-1+5e-1b+**5e-2** schema/seed + the running 5e-2 planner API. If gone: `docker start neurospect-learn-db`,
then `cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python
-m scripts.seed_tracks && poetry run python -m scripts.seed_drills && poetry run python -m scripts.ingest_content`.
Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live.

Neurospect — Phase 5e-3: STUDY PLANNER UI for `neurospect-learn` (FRONTEND ONLY — the 5e-2 engine + API are built + tested; you CONSUME them, never recompute or fork the schedule). Build the three planner pages — `/today` (the prescriptive ordered daily card list — the platform's headline differentiator), `/plan` (the month/week calendar), `/plan/setup` (availability & preferences) — plus their components + the `lib/planner.ts` query/mutation layer, wired to the live planner endpoints. North star: DISCIPLINE & ACCOUNTABILITY BY DESIGN — Today is prescriptive (ordered, not a menu); skipping logs a SKIP (hurts adherence, never hidden); streak / adherence % / days-behind / carried-over are VISIBLE, not hideable; the target go-live date is PACING-ONLY (shown as an ETA, NEVER a gate/unlock).

STEP 0 — CONFIRM 5e-2 SHIPPED (do this FIRST; if any check fails, STOP and tell Paul — do not build on a broken base):
  - Migrations at 0006: `cd api && poetry run alembic current` shows `0006 (head)`.
  - Seeds present: `docker exec neurospect-learn-db psql -U learn -d neurospect_learn -tAc "SELECT 'concepts='||count(*) FROM concepts; SELECT 'track_stages='||count(*) FROM track_stages; SELECT 'drills='||count(*) FROM drills;"` → concepts=74, track_stages=23, drills=53 (content_pages=67).
  - Planner API live: start uvicorn, mint a debug token, `PUT /api/preferences` (a weekday-minutes + active_track body) then `GET /api/plan/today` returns `{items, adherence, pace}` with items > 0 for a fresh aura user; `GET /api/plan?from=&to=`, `POST /api/plan/regenerate`, `PATCH /api/plan/items/{id}` all respond.
  - Backend tests green: `cd api && poetry run pytest tests/ -q` → 16 passed (9 scheduler unit + 7 API).
  - Frontend baseline: `cd app && npx tsc -b && npx vite build` clean; `npx playwright test` → 12/12 green (6 content + 6 multi-track). (Playwright needs the API up on :8000 with DEBUG=true — see playwright.config.ts.)
  Only once ALL pass, proceed.

Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Study Planner (the differentiator + how the planner enforces the north star per feature), §Route / page taxonomy (the `/today` · `/plan` · `/plan/setup` rows), §Component structure + API surface (the planner component list + the endpoint list), and §5e-2 as-built (CODE is ground truth — the API + Pydantic schemas you consume). Grading model context (do NOT restate): mastery/README.

THE API YOU CONSUME (5e-2 as-built — code is ground truth in `api/app/{routers,schemas}/planner.py`; DO NOT change it):
  - `GET|PUT /api/preferences` → PreferencesOut (`is_configured=false` + defaults when unset; timezone, mon_minutes…sun_minutes, max_session_minutes, blackout_dates[], target_go_live_date, active_track, plan_version, generated_at). PUT body = PreferencesIn (same, validated ge/le).
  - `GET /api/plan/today` → TodayOut `{date, active_track, plan_version, items:[PlanItemOut], adherence:AdherenceOut, pace:PaceOut}`. Materializes today idempotently server-side — just render it.
  - `GET /api/plan?from=&to=` → PlanRangeOut `{date_from, date_to, items, pace, unplaced}` — past/today FROZEN (`id` set, `frozen=true`), future COMPUTED (`id=null`, `frozen=false`).
  - `POST /api/plan/regenerate` → TodayOut (bumps plan_version; frozen done/partial/skipped kept).
  - `PATCH /api/plan/items/{id}` body PlanItemPatch `{status: pending|done|partial|skipped, done_qty?}` → PlanItemOut (server feeds concept_progress/drill_progress reps+last_practiced; never advances the ladder).
  - PlanItemOut fields to render: activity (learn|drill|review|observe|habit|backtest), concept_title/content_slug, drill_ref/drill_title/drill_variant, target_qty/target_unit, est_minutes, status, done_qty, completed_at, sort_order, carried_over, frozen. AdherenceOut: total/done/partial/skipped/pending/adherence_pct/current_streak/days_behind/carried_over. PaceOut: target_go_live_date/projected_go_live/on_pace/projected_clear{stage_code→date}.

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki content; never touch sources/ or vault/), Architecture Doc Integrity (CODE is ground truth — you MUST reconcile learning-platform.md + add a §5e-3 as-built before sign-off), "Paul handles git — NEVER commit".
2. Run STEP 0 above.
3. Read learning-platform.md §Study Planner + §Route taxonomy + §Component structure + API surface + §5e-2 as-built IN FULL.
4. Skim the live frontend you extend (the conventions to match): `app/src/App.tsx` (router — add the new routes), `app/src/components/layout/sidebar.tsx` (`navItems` — add Today + Plan), `app/src/lib/{learning,content}.ts` (the hierarchical query-key + `useQuery`/`useMutation`-with-invalidation pattern — `lib/planner.ts` mirrors it), `app/src/types/api.ts` (add the planner types), the 5e-1 components under `components/{progress,drills}/` + `components/ui/*` (shadcn primitives already present: card/button/badge/checkbox/dialog/form/input/select/tabs/skeleton/tooltip/progress/popover/…; RHF+Zod+@hookform/resolvers + date-fns are installed), pages `{path,stage-detail,drills}.tsx`, and the Playwright harness `e2e/{global-setup,content.spec,learning.spec}.ts` + `playwright.config.ts`.

SCOPE — 5e-3 IS:
  - `app/src/lib/planner.ts` — `plannerKeys` + hooks `usePreferences`/`useUpdatePreferences`/`usePlanToday`/`usePlanRange`/`useRegenerate`/`useUpdatePlanItem`, following the `learningKeys` + `useMutation`→invalidate convention (a mark-done invalidates plan/today + plan range + the learning progress/stages/drills subtrees, since it feeds progress). Planner types in `types/api.ts`.
  - Components under `app/src/components/planner/`: `TodayList` + `PlanItemCard` (activity icon + concept/drill title + target_qty/unit + est-minutes + done/partial/skip controls → `useUpdatePlanItem`; carried-over + status styling; frozen vs computed), `StudyCalendar` (a LIGHTWEIGHT CUSTOM CSS-grid month/week calendar using `date-fns` — NOT `react-day-picker` [never re-add it — it's a date picker, not a content calendar, and the CSP surface stays minimal]; past frozen [done/skip], today, future projected; a Regenerate button), `AvailabilityForm` (RHF+Zod — per-weekday minutes, max-session, timezone, blackout dates, optional pacing-only target go-live date), `StreakBadge`/`AdherenceMeter`/`PaceProjection`.
  - Pages (replace nothing existing — ADD): `/today` (TodayList + streak/adherence/days-behind + pace), `/plan` (StudyCalendar + regenerate), `/plan/setup` (AvailabilityForm). Add the three routes to `App.tsx` and Today + Plan to `sidebar.tsx` `navItems`.
  - North star surfaced in the UI: prescriptive ordered Today; skip → a logged skip (adherence drop shown); days-behind / carried-over / streak visible + not hideable; the target date shown as an ETA / on-pace-or-behind flag only (never gates or unlocks).

5e-3 IS NOT: any backend/API/scheduler/migration change (5e-2 is built + tested — consume it, do not fork or recompute the schedule client-side); journal/expectancy/gate UI (5f/5g); re-adding `react-day-picker` or `recharts` (charts arrive in 5f); ALDC anything.

VERIFY (evidence): `npx tsc -b` + `npx vite build` clean; extend the Playwright suite with planner specs (setup form saves prefs → `/today` renders prescriptive ordered items; mark an item done → adherence/streak update AND progress fed [cross-check on `/path` or `/drills`]; skip logs a SKIP; `/plan` calendar shows frozen past/today + projected future; regenerate bumps plan_version) — all green AND the existing 12 still green (no regression); a live claude-in-chrome walkthrough (debug-login → `/plan/setup` save → `/today` mark-done + skip → `/plan` calendar → regenerate) with NO console errors.
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md §Route taxonomy + §Component structure + API surface → as-built (the shipped component names + the custom-calendar decision) + add a §5e-3 as-built; mark 5e-3 ✅ in the split + tracker + a session-log entry (next=5f journal + expectancy); append log.md; bump index.md. Do NOT edit trade-schema.md / phase3-frontend-structure.md. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5e-2 — Study Planner engine) ✅ EXECUTED 2026-07-22

Recommended launch: **Opus** (`claude --model opus[1m]`), `/effort high` for the deterministic scheduler +
the track-aware unlock/backlog logic. No plan mode — this executes the approved [[concepts/architecture/learning-platform]]
§Study Planner. Backend-only (no UI — that's 5e-3). Working dir: `C:\Users\PaulRussell\repos\neurospect-learn`
(code is ground truth), or start from the wiki to read the design first. **Prereq:** the `neurospect-learn-db`
container on :5433 with the 5c+5d+5e-1+**5e-1b** schema/seed/ingest. If gone: `docker start neurospect-learn-db`,
then `cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python
-m scripts.seed_tracks && poetry run python -m scripts.seed_drills && poetry run python -m scripts.ingest_content`.
Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live.

Neurospect — Phase 5e-2: STUDY PLANNER ENGINE for `neurospect-learn` (BACKEND ONLY — no UI; that is 5e-3). Build the adaptive, gate-aware, retention-aware daily/weekly study-schedule generator: `study_preferences` + `plan_items` (Alembic 0006), the deterministic `scheduler` service, and the planner API. It SCHEDULES the existing curriculum — it NEVER restates or forks it (concepts, drill_refs, freetext rep targets, the learning-path stage gates are consumed/linked). North star: DISCIPLINE & ACCOUNTABILITY BY DESIGN — every choice defaults to enforce the disciplined path over let-the-user-decide.

STEP 0 — CONFIRM 5e-1b SHIPPED (do this FIRST, before any 5e-2 work; if any check fails, STOP and tell Paul — do not build on a broken base):
  - Migrations at 0005: `cd api && poetry run alembic current` shows `0005 (head)`.
  - Seeds present: `docker exec neurospect-learn-db psql -U learn -d neurospect_learn -tAc "SELECT 'concepts='||count(*) FROM concepts; SELECT 'track_stages='||count(*) FROM track_stages; SELECT 'drills='||count(*) FROM drills;"` → concepts=74, track_stages=23, drills=53 (and content_pages=67).
  - API multi-track live: start uvicorn, mint a debug token, `GET /api/tracks` returns 3 tracks (aura/ict_course/unified) with their stages; `GET /api/stages?track=aura` returns A0–A6.
  - Frontend builds: `cd app && npx tsc -b && npx vite build` clean; `npx playwright test` → 12/12 green (6 content + 6 multi-track).
  Only once ALL pass, proceed.

Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Study Planner (availability · the deterministic gate-aware/retention-aware scheduling algorithm · persist-vs-compute hybrid · how the planner enforces the north star), §Progress + journal data model §4 (the `study_preferences` + `plan_items` table shapes + the `plan_activity`/`plan_item_status` enums), §Component structure + API surface (the planner endpoint list), §5e-1 + §5e-1b as-built (CODE is ground truth — `concepts`/`concept_progress`/`drills`/`drill_progress`/`track_stages`/`stages.py`/`rep_targets.py`/`learning` router already exist and are what you reuse). Grading model (reuse, do NOT restate): mastery/README (ladder 1–4, confidence 1–5, reps, gate).

MULTI-TRACK RECONCILIATION (the design predates 5e-1b — you MUST reconcile it): the planner now schedules ONE CHOSEN TRACK (per 5e-1b there are three: aura/ict_course/unified). So: (a) `study_preferences` gains `active_track` (VARCHAR(16) CHECK aura|ict_course|unified, default 'aura'); (b) the scheduler is TRACK-SCOPED — unlock uses the generalized `stages.py compute_stages(track, stage_metas, concepts, progress)`; backlog iterates THAT track's concepts (ordered stage_order, sort_order) + their `drill_refs`; concept-less stages (backtest/live/journal — unified U6, aura A4–A6, ict M6–M8) are NOT scheduled as learn/drill (observe/backtest only, gated behind the concept work). Update §Study Planner + §4 in the doc to the as-built multi-track shape when you reconcile.

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki content; never touch sources/ or vault/), Architecture Doc Integrity (CODE is ground truth — you MUST reconcile learning-platform.md + add a §5e-2 as-built before sign-off), "Paul handles git — NEVER commit".
2. Run STEP 0 above.
3. Read learning-platform.md §Study Planner + §Progress data model §4 + §Component/API surface IN FULL, and §5e-1/§5e-1b as-built (the shapes you reuse: the lazy-upsert progress lifecycle, `rep_targets.parse/meets`, `compute_stages`, the per-track concept/drill grouping).
4. Skim the live code you extend: api/app/models/{concept,concept_progress,drill,drill_progress,track_stage}.py, api/app/services/{stages,rep_targets}.py, api/app/routers/learning.py + schemas/learning.py, api/alembic/versions/0005_multi_track.py (the migration idiom), api/app/models/enums.py (the pg_enum helper).

SCOPE — 5e-2 IS:
  - MIGRATION alembic 0006_study_planner (raw-SQL, reversible, mirroring 0002–0005; reuse update_updated_at()): NEW enums `plan_activity` (learn|drill|review|observe|habit|backtest) + `plan_item_status` (pending|done|partial|skipped) (drill_variant already exists from 0004 — do NOT recreate); NEW `study_preferences` (user-scoped, soft-deleted, UNIQUE (user_id) WHERE NOT is_deleted): timezone (IANA text), mon_minutes…sun_minutes (7 SMALLINT, 0=off), max_session_minutes, blackout_dates DATE[], target_go_live_date (nullable, PACING-ONLY), active_track (CHECK aura|ict_course|unified), plan_version INT, generated_at; NEW `plan_items` (user-scoped, soft-deleted): plan_version, scheduled_date, activity, concept_id (nullable FK→concepts), drill_ref (nullable soft ref), drill_variant (nullable), target_qty + target_unit (nullable), est_minutes, status, done_qty, completed_at, sort_order; index (user_id, scheduled_date) WHERE NOT is_deleted + partial-unique (user_id, scheduled_date, activity, concept_id, drill_ref, drill_variant) WHERE NOT is_deleted.
  - MODELS: `study_preferences.py` + `plan_item.py` (registered in models/__init__.py + alembic/env.py).
  - SERVICE: pure `app/services/scheduler.py` — `schedule(today, prefs, concepts, drills, concept_progress, drill_progress, past_items)` → dated plan_items. Deterministic + re-runnable (strict ordering, NO randomness; same inputs → same plan), unit-testable WITHOUT a DB. Pipeline: unlock (highest unlocked stage via compute_stages for prefs.active_track) → backlog (learn untracked / drill below rep target / observe U5 watch-only / habit U0-equivalent) → rep-target parse (reuse rep_targets.py — NEVER invent) → mandatory spaced review (Leitner from confidence+last_practiced; no off switch) → daily packing (tz-aware, skip blackout + 0-budget days, blocks ≤ max_session_minutes) → projection/ETA (pacing-only vs target_go_live_date; NEVER gates) → slippage carry-over (past pending re-queued; days-behind surfaced, never hidden).
  - ENDPOINTS (new `app/routers/planner.py`, prefix /api, auth-gated + user-scoped; schemas in `app/schemas/planner.py`; mount in main.py): GET|PUT /api/preferences; GET /api/plan/today (materialize+persist today's computed items once — idempotent via the partial-unique index; return items + adherence + pace); GET /api/plan?from=&to= (past+today frozen, future computed/projected); POST /api/plan/regenerate (bump plan_version, recompute; frozen past keeps its version); PATCH /api/plan/items/{id} (status + done_qty → FEED concept_progress/drill_progress reps + last_practiced, honoring the existing ladder-advance gate + watch-only cap).

5e-2 IS NOT: any UI (/today, /plan, /plan/setup — that is 5e-3); journal/expectancy/gate (5f/5g); backtesting methodology; ALDC anything.

VERIFY (evidence): alembic 0001→0006 up/down/up clean; scheduler UNIT TESTS with no DB (determinism: same inputs→identical plan; unlock respects the per-track gate; locked stages never scheduled; U5 observe-only; blackout/0-budget days skipped; max-session honored; spaced-review due dates; slippage re-queue) — pytest green; API checks (self-written harness or pytest): PUT/GET preferences round-trip, GET /plan/today materializes idempotently (2nd call no dupes), PATCH item done feeds concept_progress reps+last_practiced and respects the gate, regenerate bumps plan_version, per-user isolation; confirm 5e-1b endpoints still green (no regression).
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md §Study Planner + §Progress data model §4 (the `study_preferences`/`plan_items` parts — fix any stale "Alembic 0005" → 0006, add `active_track`, describe the track-scoped scheduler) → as-built + add a §5e-2 as-built; mark 5e-2 ✅ in the split + tracker + a session-log entry (next=5e-3); append log.md; bump index.md. Do NOT edit trade-schema.md / phase3-frontend-structure.md. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5e-1b — multi-track curriculum) — ✅ EXECUTED 2026-07-21

Recommended launch: **Opus** (`claude --model opus[1m]`), `/effort high` for the per-track concept authoring +
the `stages.py` generalization. No plan mode — this executes the approved [[concepts/architecture/learning-platform]]
§Multi-track path redefinition. Working dir: `C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth),
or start from the wiki to read the design + the two per-track curricula first. **Prereq:** the `neurospect-learn-db`
container on :5433 with the 5c+5d+5e-1 schema/seed/ingest. If gone: `docker start neurospect-learn-db`, then
`cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python -m
scripts.seed_drills && poetry run python -m scripts.ingest_content`. Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live.

Neurospect — Phase 5e-1b: MULTI-TRACK CURRICULUM for `neurospect-learn`. Redefine `/path` from ONE unified spine into THREE first-class graded tracks (Aura · AXL/MrWitness · Unified) with a track switcher; each track has its OWN graded concepts, OWN stages, OWN drills, OWN per-user progress (a shared primitive is DUPLICATED across tracks ON PURPOSE — more reps + a second explanation); equivalent concepts across tracks carry CROSS-LINKS ("Also taught in: …"). Reshape each stage into a CURRICULUM UNIT (Read → Drill → Track → Gate). This ships BEFORE the Study Planner.
Design spec (READ FIRST — it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Multi-track path redefinition (the model + the data model), §Route/page taxonomy (the /path switcher + /path/:track/:stage curriculum unit), §5c + §5e-1 as-built (CODE is ground truth — concepts/concept_progress/drills/drill_progress/stages.py/learning router already exist).
Per-track curricula to SEED FROM (consume/link, NEVER restate or fork): Aura → C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\aura\learning-path.md (Stages 0–6: concepts + drills + gate per stage) + \aura\exercises.md (drills/reps). AXL → C:\Users\PaulRussell\repos\neurospect-wiki\concepts\course\README.md (Modules 1–5) + \ict-course\exercises.md (Stage 0 discipline + M1–M5 drills + tape/backtest/journal). Unified → the EXISTING 41 concepts (mastery\unified\learning-path.md). Grading model (reuse, do NOT restate): mastery\README.md (ladder 1–4, confidence 1–5, reps, gate).
Content slugs already ingested (5d): the concept KB pages (aura/*, course/module-*/*, entry-models/*, business-logic/ict-*) resolve via the 5d slug scheme — reuse `concepts.content_slug` lookups; do NOT re-derive.
Repo: C:\Users\PaulRussell\repos\neurospect-learn (api/, app/). Wiki content source (READ-ONLY): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\**.

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki content; never touch sources/ or vault/), Architecture Doc Integrity (CODE is ground truth — you MUST reconcile learning-platform.md + add a §5e-1b as-built before sign-off), "Paul handles git — NEVER commit".
2. Read learning-platform.md §Multi-track path redefinition + §Multi-track data model + §Route taxonomy IN FULL, and §5e-1 as-built (the concept/stages/drills/router shapes you extend).
3. Read the two per-track curricula (aura/learning-path.md + course/README.md) + both exercises.md to map, PER TRACK, each stage → its concepts (with content_slug + drill_refs + is_core + rep_target) → its gate. Derive rows faithfully; NEVER invent a concept/drill/target the source lacks — flag gaps.
4. Skim the live code you extend: api/app/models/concept.py, api/scripts/seed_concepts.py (the seed idiom + the 41 unified rows), api/app/services/stages.py (generalize it), api/app/routers/learning.py + schemas/learning.py, api/scripts/seed_drills.py (drills carry track already), app/src/pages/{path,stage-detail}.tsx + components/progress/* + lib/learning.ts + types/api.ts.

SCOPE — 5e-1b IS:
  - MIGRATION alembic 0005_multi_track (raw-SQL, reversible, mirroring 0002–0004; reuse update_updated_at()): ALTER `concepts` ADD `track` VARCHAR(16) NOT NULL DEFAULT 'unified' + CHECK (track IN ('aura','ict_course','unified')), ADD `stage_code` VARCHAR(16), ADD `stage_order` SMALLINT, ADD `cross_refs` TEXT[]; ALTER `u_stage` DROP NOT NULL (unified-only henceforth). NEW seed table `track_stages` (no soft-delete): `track`, `stage_order`, `stage_code`, `title`, `summary`, `gate_text`, timestamps + trigger, UNIQUE (track, stage_code). (Planner tables move to 0006 — do NOT build them.)
  - MODEL: extend concept.py (track/stage_code/stage_order/cross_refs; u_stage nullable) + new track_stage.py; register + import in env.py.
  - SEED: extend seed_concepts.py — set track='unified' + backfill stage_code (='U'+n)/stage_order on the 41; ADD ~14 Aura + ~17 AXL concept rows (distinct slugs e.g. `aura-swing-points`, `ict-liquidity-swings`) with content_slug + drill_refs + is_core + rep_target + cross_refs (equivalent slugs in the other tracks). NEW seed_tracks.py → `track_stages` (Aura A0–A6, AXL M0–M8, Unified U0–U6: title + summary + gate_text from the learning-path pages). Re-point seed_drills.py `concept_slugs` to the same-track concept slugs. Report per-track counts; all seeds idempotent.
  - SERVICE: generalize stages.py — a stage's gate computed from `track_stages.concept_slugs` + concept flags (is_core at Can-mark, conf≥3, reps≥parsed target where the page specifies); keep auto_met/met/locked + the unified U0–U4 exact rules as a special case; frontier U5 watch-only unchanged.
  - ENDPOINTS (extend learning.py): GET /api/tracks (tracks + their stages from track_stages + per-stage progress rollup + gate), GET /api/progress?track= (filter), keep PATCH progress/drills; generalize GET /api/stages → per track. Add cross_refs to the concept/progress responses.
  - FRONTEND: `/path` track switcher (Aura|AXL|Unified) → the selected track's StagePath; route `/path/:track/:stage`; reshape StageDetail into the CURRICULUM UNIT (Read = content links via content_slug; Drill = DrillCards for the stage's drill_refs; Track = ConceptTrackPanels for the stage's concepts; Gate = ExitBarGate/gate_text). Add "Also taught in: …" cross-links on the ConceptTrackPanel + reader. Update lib/learning.ts (useTracks) + types/api.ts.

5e-1b IS NOT: the Study Planner (prefs/plan_items/scheduler/today/plan/setup — 5e-2/5e-3, Alembic 0006); journal/expectancy/gate (5f/5g); backtesting methodology; ALDC anything.

VERIFY (evidence): alembic 0001→0005 up/down/up clean; seeds idempotent + per-track counts reported; GET /api/tracks returns 3 tracks with their stages; per-track progress isolation (marking Aura swings does NOT mark AXL/Unified swings); cross_refs resolve; stages.py gate flips per track on a fixture; tsc -b + vite build clean; Playwright extended (track switch, per-track stage unit, cross-link) green; browser (claude-in-chrome): switch tracks, a stage shows Read+Drill+Track+Gate, cross-link jumps tracks, no console errors.
RECONCILE + BOOKKEEP (mandatory): update learning-platform.md §Multi-track data model + §Route taxonomy → as-built + add a §5e-1b as-built; mark 5e-1b ✅ in the split + tracker + a session-log entry (next=5e-2); append log.md; bump index.md. Do NOT edit trade-schema.md / phase3-frontend-structure.md. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5e-1 — progress foundation) — ✅ EXECUTED 2026-07-20

Recommended launch: **Sonnet** (`claude --model sonnet[1m]`), `/effort high` for the three design-heavy seams —
the **per-user `concept_progress` lifecycle**, the **stage exit-bar derivation** (computed, never stored), and
the **`drills` catalog parse + data model**. No plan mode — this executes the approved
[[concepts/architecture/learning-platform]] design. Working dir: open at
`C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from the wiki to read the design +
grading model first. **Prereq:** local Postgres with the 5c schema + seed **and** the 5d content ingest (the
`neurospect-learn-db` container on :5433, matching `api/.env`). If gone/stopped: `docker start
neurospect-learn-db` (or re-create per the 5c prereq), then `cd api && poetry run alembic upgrade head && poetry
run python -m scripts.seed_concepts && poetry run python -m scripts.ingest_content` (→ 41 concepts + 67 content
pages). Frontend + backend both installable (5b–5d verified). Paste:

````
Neurospect — Phase 5e-1: PROGRESS FOUNDATION for `neurospect-learn` — the substrate the Study Planner (5e-2/5e-3) reads. Build: per-user `concept_progress` editing (ladder/confidence/reps) via a "track this" panel on the reader; the DERIVED stage exit-bars; a `drills` catalog + `drill_progress`; the `learning` endpoints; and the `/path` + `/path/:stage` + `/drills` frontend. VISUALIZE the existing mastery ladder/confidence/gate — do NOT reinvent it.
Design spec (READ FIRST, it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model (the "Study Planner + progress-editing (Phase 5e)" subsection: concept_progress lifecycle + `drills`/`drill_progress` DDL + the stage exit-bar derivation — the PLANNER tables study_preferences/plan_items are 5e-2, NOT this phase), §Route/page taxonomy (/path, /path/:stage, /drills; the ConceptTrackPanel on /concepts/:slug), §Component structure + API surface (the `learning` endpoints + the "first useMutation" + `dark:`-fix infra notes), §5c as-built (concept_progress shape — CODE is ground truth), §5d as-built (content API + reader + badges live).
Grading model to VISUALIZE (reuse by reference, do NOT restate): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\README.md §Per-concept mastery ladder (4 stages = ladder_stage 1–4) · §Confidence rating (1–5) · §Rep counters · §Readiness-to-Live Gate. Stage exit-bars + ordering: C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\unified\learning-path.md (each U0–U4 stage's "Stage gate"/"Exit bar"; earlier stages gate later) + \tracker.md (the grid). Drill libraries (✋ hand-mark / 🛠 tool) + the structured "Drill → concept → ladder-stage map" tables to SEED the catalog from: C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\{aura,ict-course}\exercises.md; concepts.drill_refs holds soft refs like "aura D2-c".
Conventions (reuse, do NOT restate): trade-schema.md §Schema Conventions; the 5b–5d backend idiom (SQLAlchemy 2.0 `Mapped`/`mapped_column`; Pydantic schemas per app/schemas/{auth,content}.py; routers per app/routers/content.py — auth-gated via `dependencies=[Depends(get_current_user)]`, per-route `db: AsyncSession = Depends(get_db)`; raw-SQL Alembic mirroring 0002/0003, reuse `update_updated_at()`; seed per scripts/{seed_concepts,ingest_content}.py — `pg_insert().on_conflict_do_update`); the 5d frontend idiom (lib/content.ts hooks + TanStack Query hierarchical keys; shadcn primitives; MarkdownRenderer/badges already built).
Repo: C:\Users\PaulRussell\repos\neurospect-learn (api/ backend, app/ frontend). Wiki content source (READ-ONLY): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\**.

PREREQ: local Postgres with the 5c schema + seed + the 5d content ingest. Dev container `neurospect-learn-db` on :5433 (matches api/.env). If gone/stopped: `docker start neurospect-learn-db` (or re-create per 5c prereq), then `cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python -m scripts.ingest_content` (→ 41 concepts + 67 content pages).

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki, never write back,
   never read sources/ or vault/), Architecture Doc Integrity (CODE is ground truth; finalizing the
   concept_progress lifecycle + the stage-exit-bar service + the drills data model IS EXPECTED to diverge from
   the sketch, so you MUST reconcile learning-platform.md + add a §5e-1 as-built before sign-off), "Paul handles
   git — NEVER commit".
2. Read learning-platform.md §Progress data model (the 5e subsection) + §Route/page taxonomy + §Component/API
   surface IN FULL. `concepts` + `concept_progress` ALREADY EXIST (5c); `concept_progress` rows are created
   per-user AT RUNTIME — that is THIS phase. Stage status is DERIVED, never stored. Read mastery/README +
   unified/learning-path for the ladder + the per-stage exit-bar rules the /path/:stage gate visualizes.
3. Skim the live code: backend — app/models/{concept,concept_progress}.py, app/models/{base,enums}.py,
   app/routers/content.py + app/deps.py (get_current_user) + app/database.py (AsyncSessionLocal/get_db),
   app/schemas/content.py, scripts/seed_concepts.py (the pg_insert on_conflict idiom), alembic/versions/
   0002_learning_progress.py + 0003_journal_entries.py (raw-SQL DDL; `update_updated_at()` already exists —
   reuse; the partial-unique `WHERE NOT is_deleted` idiom), alembic/env.py (import every new model). frontend —
   app/src/App.tsx (the /path, /path/:stage, /drills STUB routes still live), lib/content.ts + lib/api.ts (the
   ky client + TanStack Query pattern to mirror — NOTE there is NO useMutation yet; you establish it),
   components/content/* + components/ui/*, pages/concept-reader.tsx (add the track panel here), e2e/ (extend the
   Playwright harness).

SCOPE — 5e-1 IS (and is ONLY):
  - MIGRATION `alembic/versions/0004_drills_progress.py` (raw-SQL, reversible, mirroring 0002/0003; reuse
    `update_updated_at()`; NEVER edit 0002/0003): the `drill_variant` enum (`hand|tool`); `drills` (SEED/content,
    NO soft-delete like `concepts`): `drill_ref` UNIQUE, `track` (`aura|ict_course`), `stage_code`, `title`,
    `advances_to`, `rep_target` (freetext), `concept_slugs` TEXT[] + timestamps + trigger; `drill_progress`
    (user-scoped, soft-deleted): `user_id` FK, `drill_ref` TEXT (soft ref), `reps` (default 0), `hand_done` +
    `tool_done` (bool), `last_practiced` DATE, `notes`, timestamps + trigger + `UNIQUE (user_id, drill_ref) WHERE
    NOT is_deleted`. (study_preferences + plan_items are 5e-2 / Alembic 0005 — DO NOT build them.)
  - MODELS `app/models/{drill,drill_progress}.py` (SQLAlchemy 2.0, mirroring concept.py/concept_progress.py);
    register in models/__init__.py + import in alembic/env.py.
  - SEED `scripts/seed_drills.py` (idempotent `pg_insert().on_conflict_do_update` on `drill_ref`, mirroring
    seed_concepts.py) parsing the "Drill → concept → ladder-stage map" tables at the foot of BOTH
    mastery/{aura,ict-course}/exercises.md → `drills` rows (drill_ref e.g. "aura D1-b" / "ict-course D3-b", track,
    stage_code, title=Concept col, advances_to, rep_target, concept_slugs back-link). READ-ONLY on the wiki.
    Report the drill count; re-run must be idempotent.
  - SERVICES: `app/services/rep_targets.py` — a pure freetext→(kind,count) parser (reps=N | days=N | sessions=N |
    qualitative | habit/none) per the design; defaults conservatively, NEVER invents a target. `app/services/
    stages.py` — a pure exit-bar service computing each U0–U4 stage's gate "met?" from the user's concept_progress
    against the rules in unified/learning-path §Stage gate (e.g. U1 = all five primitives ≥ Can-mark, conf ≥3,
    reps ≥ parsed target). COMPUTED, never stored. LINK the rules; do not restate them in the wiki. U5 (frontier)
    is watch-only — NEVER live-gate-eligible; U6 readiness is OUT OF SCOPE (that live gate is 5g). *Integrity:*
    stages.py IS the as-implemented gate — record it in §5e-1 as-built.
  - LEARNING endpoints (new `app/routers/learning.py`, prefix `/api`, `dependencies=[Depends(get_current_user)]`,
    user-scoped; schemas in `app/schemas/learning.py`; mount in main.py): GET /api/concepts (list; optional
    ?stage=U1), GET /api/progress (this user's grid — LEFT JOIN concepts × the user's concept_progress so
    untracked concepts return null ladder/confidence), PATCH /api/progress (UPSERT one concept's
    ladder/confidence/reps/notes/last_practiced for the current user — on_conflict on the unique partial index;
    LAZY create, no bulk pre-seed; **ENFORCE: reject a ladder advance to Can-mark+ unless reps ≥ parsed target AND
    confidence is set** — north-star gating, no self-declared skips), GET /api/stages (per U-stage: its concepts +
    this user's progress + the DERIVED exit-bar status + locked/unlocked), GET /api/drills (catalog + this user's
    drill_progress; ?track= / ?stage=), PATCH /api/drills (UPSERT one drill_progress: reps / hand_done / tool_done
    / last_practiced).
  - FRONTEND (replace the 5b stubs for /path, /path/:stage, /drills; add the track panel to /concepts/:slug):
    components per the design — StagePath/StageNode (the U0→U6 spine with per-stage progress rings + gate state +
    LOCKED styling), ExitBarGate, LadderBadge (1–4), ConfidenceRating (1–5), RepCounter, ConceptTrackPanel
    (editable ladder/confidence/reps → PATCH /api/progress; surfaces the ladder-advance gate), DrillCard (✋/🛠 +
    reps + mark-complete → PATCH /api/drills). Establish the FIRST mutation pattern (`<domain>Keys` +
    `use<Domain>Mutation` with `onSuccess: queryClient.invalidateQueries`, mirroring `contentKeys` in
    lib/content.ts) in new `lib/learning.ts`; add types to types/api.ts (comment-linked to app/schemas/learning.py).
    `npx shadcn add progress` (rings/bars). FIX the `dark:` mismatch: add `@custom-variant dark (&:where(.dark,
    .dark *))` to src/index.css (flagged in §5d as-built) so new `dark:` utilities fire on the class-based theme.
    RHF+Zod only if a form gets non-trivial (the small edits can be controlled inputs).

5e-1 IS NOT (build NONE — later phases): the Study Planner — study_preferences + plan_items (Alembic 0005), the
  scheduler service, /today, /plan, /plan/setup, the planner API (5e-2/5e-3); the model-aligned journal + /journal
  (5f); the /expectancy dashboard + recharts (5f — not re-added until then); the entry-model YAML→strategy parser
  (5f); the /gate live readiness view + its computation (5g — 5e-1 does per-STAGE exit bars only, NOT the
  live-eligibility gate); R2/screenshots; Claude; backtesting methodology; ALDC anything.

EFFICIENT PATH: mirror the established idioms — router like app/routers/content.py, schemas like
  app/schemas/content.py, DDL like alembic 0002/0003 (raw op.execute, reuse update_updated_at()), the drills parse
  like scripts/ingest_content.py/seed_concepts.py, frontend data-fetch like lib/content.ts + TanStack Query. Keep
  progress edits simple (invalidate-on-success or optimistic).

VERIFY (evidence, not inference — needs the local Postgres + wiki):
  - `alembic upgrade head` 0001→0004 clean + `downgrade` and back up clean (reversible). seed_drills → the parsed
    drill count (report it), re-run idempotent (no dupes on drill_ref).
  - PATCH /api/progress creates exactly one row for the CURRENT user; GET /api/progress returns the merged grid
    with that value; re-PATCH updates in place (no dup — the unique partial index holds); a SECOND debug user sees
    NONE of the first's rows (per-user isolation); CHECK constraints reject ladder=9 / confidence=9; the
    ladder-advance ENFORCEMENT rejects a premature Can-mark (reps < target or confidence unset) — spot-check.
  - GET /api/stages exit-bar status flips correctly against a hand-set concept_progress fixture (set U1's five core
    primitives to Can-mark+conf3+reps ≥ target → U1 gate "met"; drop one → "not met"). U5 never counts toward a
    live gate.
  - /drills mark-complete + rep increment persist (reload). Endpoints require a Bearer token (401/403 without).
    `tsc -b` + `vite build` clean.
  - Browser (claude-in-chrome, debug-login): /path renders the U0→U6 spine with progress rings + locked/unlocked;
    /path/:stage shows its concepts + the ExitBarGate reflecting concept_progress; the ConceptTrackPanel on
    /concepts/:slug edits ladder/confidence/reps and persists on reload; /drills marks a drill + bumps reps. No
    console errors. App boots (/health=200) with the learning router mounted.
  - EXTEND the Playwright harness: add e2e specs for progress edit-persist, stage exit-bar flip, and a drill mark —
    `npm run test:e2e` green. (global-setup already mints a per-user debug token.)

RECONCILE + BOOKKEEP (mandatory per Architecture Doc Integrity):
  - UPDATE learning-platform.md §Progress data model (the 5e subsection) + §Component/API surface to AS-BUILT
    (concept_progress lifecycle, the stage exit-bar derivation + the rep_targets parser, the drills data model +
    Alembic 0004, the learning endpoints) + add a §5e-1 as-built note (like §5d). Code is ground truth.
  - Mark 5e-1 ✅ in the tracker Plan; add a 5e-1 session-log entry (did / verified / next=5e-2); append log.md;
    bump index.md last_build. Write the 5e-2 boot prompt when 5e-2 starts (not now).
  - Do NOT edit trade-schema.md or phase3-frontend-structure.md (other lanes).

OUT OF SCOPE: the planner (prefs/plan_items/scheduler/today/calendar/setup), journal, expectancy, charts,
strategy-YAML parsing, the live gate, R2, Claude, backtesting methodology, ALDC anything. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Study Planner + progress layer — PLAN-MODE DESIGN) — ✅ EXECUTED 2026-07-20

Recommended launch: `claude --model opus[1m]`, then `/effort high`, in **plan mode** — this is a design session
and the plan is the load-bearing artifact. Working dir: `C:\Users\PaulRussell\repos\neurospect-wiki` (the design
doc lives here; the app to design against is `C:\Users\PaulRussell\repos\neurospect-learn`, code = ground truth).
No code this session. Paste:

````
Neurospect — DESIGN (plan mode) the STUDY PLANNER — an adaptive daily/weekly study-schedule generator — for `neurospect-learn`, together with the minimal PROGRESS layer (the redefined Phase 5e) it depends on, so they ship as one. Goal: the platform tells me exactly what to study/drill each day, driven by my availability + the U0→U6 curriculum + my current progress, gated + adaptive. This is the platform's key differentiator — design it to be elite.
Working dir: C:\Users\PaulRussell\repos\neurospect-wiki  |  App to design against (code = ground truth): C:\Users\PaulRussell\repos\neurospect-learn

BOOT / CONTEXT
1. Read the wiki CLAUDE.md IN FULL — Isolation Rule (Neurospect ONLY; NO ALDC), Architecture Doc Integrity (code
   in neurospect-learn is ground truth; write ONE canonical design — extend learning-platform.md, do NOT restate
   content; LINK it), plan-mode discipline (present the plan for approval BEFORE writing any page; no app code),
   Rules #3 (index.md) #4 (log.md) #6 (flag contradictions). Paul handles git — commit only if he asks.
2. Read the tracker processes/distributed-workflow/active/learning-platform-ui.md IN FULL — the Goal, the Decisions
   (esp. 2026-07-20: Study Planner elevated; planner sits on the 5e progress layer; design them together), and the
   superseded standalone 5e build boot prompt below (its scope — concept_progress editing, stage exit-bars,
   /drills — is the progress layer to FOLD IN, now re-scoped by this design).
3. Read learning-platform.md IN FULL — esp. §Progress + journal data model (the concept_progress part), §Route/
   page taxonomy (/path, /path/:stage, /drills, the reader track panel), §Component/API surface, §5c + §5d as-built
   (CODE is ground truth: concepts + concept_progress + content_pages already exist and are seeded/ingested).
4. Read the CURRICULUM the planner schedules against (VISUALIZE/CONSUME, do NOT restate or fork): mastery/README
   (ladder Learned→Can-mark→Backtested→Live-ready = 1–4, confidence 1–5, rep counters, Readiness-to-Live Gate) +
   mastery/unified/learning-path.md (U0→U6 ordered stages, each with an explicit exit-bar + rep target; earlier
   gates later) + tracker.md (the per-concept grid) + the drill libraries mastery/{aura,ict-course}/exercises.md
   (✋ hand-mark / 🛠 tool variants). concepts.drill_refs holds soft refs like "aura D2-c"; rep_target is freetext.
5. Skim the live code so the design is buildable against it: api/app/models/{concept,concept_progress}.py,
   api/alembic/versions/0002_learning_progress.py, api/app/routers/content.py (the auth-gated router idiom),
   app/src/App.tsx (the /path,/path/:stage,/drills STUBS + the /concepts reader), app/src/lib/content.ts (hooks +
   TanStack Query), app/src/components/{content,ui}/*. Note: recharts + react-day-picker were dropped in 5b (re-add
   if the planner UI needs a calendar/date lib) — and the app's `dark:` variant is media-based while the theme is
   class-based (flagged in learning-platform.md §5d as-built — account for it in any new themed UI).

OBJECTIVE
Design (a) a minimal PROGRESS layer — per-user concept_progress editing (ladder/confidence/reps), the DERIVED
stage exit-bars, and /drills — and (b) the STUDY PLANNER that consumes it: input availability → generate a
concrete, dated study routine from the curriculum, gate-aware, rep-target-driven, adaptive (re-plan on progress
change + slippage), with spaced review of weak/stale concepts, a Today view + a calendar. Design them as ONE
coherent feature that ships together.

Decide and justify, in the plan, at least:
  0. SCOPE + SEQUENCING — how the progress layer and the planner split into buildable sub-phases that ship together
     (e.g. progress foundation → planner data+algorithm → planner UI). Each a boot-promptable unit.
  1. AVAILABILITY / PREFERENCES MODEL — how the user enters availability (recurring weekly slots? hours-per-day?
     days-per-week? session length? blackout dates? target go-live date?) + the data model for it.
  2. SCHEDULING ALGORITHM — the core. Map the curriculum GRAPH (U0→U6 ordered + gated; per-concept ladder targets +
     rep targets; drills ✋/🛠) + current concept_progress + availability → a dated plan. Must: respect stage gates
     (never schedule a locked stage's work), never schedule "go-live" on a watch-only/EMERGING/SPECULATIVE frontier
     concept, allocate reps toward targets, order within a stage, size each day to available time, INTERLEAVE spaced
     review (resurface concepts by confidence + last_practiced for retention), and RE-PLAN on progress change or a
     missed day. Deterministic + re-runnable. Decide horizon (rolling N weeks vs to-go-live) + slippage handling.
  3. DATA MODEL — new tables (e.g. study_plan / plan_items [scheduled_date, ref to concept/drill, activity type,
     target, status], availability/preferences); relation to concepts + concept_progress + drills; regenerate-vs-
     persist (is the plan stored, or computed on read + only completions stored?). Show DDL sketch + enums; reuse
     trade-schema.md conventions (UUID/TIMESTAMPTZ/updated_at trigger/user-scoped/soft-delete) — new Alembic 0004+.
  4. PROGRESS LAYER (folded in) — concept_progress lifecycle (per-user lazy upsert), the stage exit-bar derivation
     (computed, never stored; rules LINKED from unified/learning-path), /drills + drill progress. The learning
     endpoints (concepts/progress/stages/drills).
  5. ROUTES / UI — the planner section (Today view; Week/Calendar view; availability/preferences setup; "regenerate")
     + how it ties into /path, /path/:stage, /drills + the reader track panel. Marking a plan item done feeds
     concept_progress reps. New components. Calendar approach (lightweight custom vs a lib — mind CSP/deps).
  6. API SURFACE — endpoints (generate/get plan, get Today, mark item done → progress, availability CRUD) + the
     progress endpoints from (4). Auth-gated, user-scoped, mirroring the content router idiom.

QUALITY BAR
- NORTH STAR (read the tracker's ## North Star section — it governs EVERY design choice): discipline &
  accountability BY DESIGN, not by choice. The planner + progress layer must STRUCTURALLY ENFORCE the disciplined
  path, not offer it as an option — prescriptive daily plan (not a menu), gated progression (no manual gate
  override), rep targets that must actually be met, adherence/streaks/skipped-days surfaced, guardrails the user
  can't switch off where they protect the process. When a choice is "let the user decide" vs "enforce," DEFAULT TO
  ENFORCE and justify any exception. Call out in the plan exactly how each feature enforces discipline.
- No-drift: the planner SCHEDULES the existing curriculum (learning-path sequence, rep targets, drills, gates) — it
  CONSUMES/LINKS them, it does not restate or fork them. If it needs data the wiki/app lacks, flag it; don't invent.
- Preserve every frontier TIER + ESTABLISHED/EMERGING/SPECULATIVE label + watch-only rule; NEVER schedule a
  frontier concept as trade-live-eligible (study-and-watch only).
- ELITE bar: adaptive, gate-aware, retention-aware (spaced review), respects real availability, actionable every
  day. This is the differentiator — design for it, and call out what makes it best-in-class vs a static syllabus.
- Reuse the proven stack + the 5b–5d idioms (auth-gated routers, Pydantic schemas, SQLAlchemy 2.0 + raw-SQL
  Alembic, TanStack Query hooks, shadcn primitives). Cite the canonical docs; surface any contradiction with code.

WORKFLOW / OUTPUT
- FIRST present the PLAN in plan mode for approval: scope/sequencing, availability model, scheduling algorithm,
  data-model sketch, routes/UI, API surface, and the revised implementation split. Do NOT write pages or code until
  approved.
- THEN on approval: extend the ONE canonical doc concepts/architecture/learning-platform.md (add a §Study Planner
  section + fold the redefined 5e into §Progress data model + §Route taxonomy + §Component/API surface + revise the
  implementation split); update this tracker (redefined phases + a session-log entry); additive cross-links from
  mastery/README + unified/learning-path; update index.md; append log.md.
- OUT OF SCOPE this session: writing app code (design only); the 5f journal/expectancy + 5g gate internals (except
  where the planner reads progress); backtesting methodology; ALDC anything. Paul handles git — commit only if asked.
````

## Next Session Boot Prompt (Phase 5e — progress tracker) — ⛔ SUPERSEDED 2026-07-20 (folded into the Study Planner design session above)

> **Superseded.** The standalone 5e progress-tracker build is now designed *together with* the Study Planner (see
> the plan-mode design boot prompt above and the 2026-07-20 Decisions). Keep this prompt as the reference for the
> progress-layer scope (concept_progress editing, stage exit-bars, `/drills`) the design session folds in; do not
> execute it standalone.

Recommended launch: **Sonnet** (`claude --model sonnet[1m]`), `/effort high` for the three design-heavy seams —
the **per-user `concept_progress` lifecycle**, the **stage exit-bar derivation** (computed, never stored), and the
**drills data model**. No plan mode — this executes the approved [[concepts/architecture/learning-platform]]
design. Working dir: open at `C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from
the wiki to read the grading model + stage exit-bars first. **Prereq:** local Postgres with the 5c schema + seed
**and** the 5d content ingest run (the `neurospect-learn-db` container on :5433, matching `api/.env`). If gone/
stopped: `docker start neurospect-learn-db` (or re-create per the 5c prereq), then `cd api && poetry run alembic
upgrade head && poetry run python -m scripts.seed_concepts && poetry run python -m scripts.ingest_content`
(41 concepts + 67 content pages). Paste:

````
Neurospect — Phase 5e: PROGRESS TRACKER for `neurospect-learn` (`/path` curriculum spine + `/path/:stage` detail with the ladder-stage exit-bar + per-concept progress editing [ladder/confidence/reps] via a "track this" panel on the reader + `/drills` exercise tracker). VISUALIZE the existing mastery ladder/confidence/gate — do NOT reinvent it.
Design spec (READ FIRST, it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model (the concept_progress part ONLY — journal is 5f), §Route/page taxonomy (/path, /path/:stage, /drills; the "track this" panel on /concepts/:slug), §Component structure + API surface (the `learning` endpoints), §5c as-built (concept_progress shape — CODE is ground truth), §5d as-built (content API + reader + badges already live).
Grading model to VISUALIZE (reuse by reference, do NOT restate): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\README.md §Per-concept mastery ladder (4 stages Learned→Can-mark→Backtested→Live-ready = ladder_stage 1–4) · §Confidence rating (1–5) · §Rep counters · §Readiness-to-Live Gate. Stage exit-bars + ordering: C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\unified\learning-path.md (each U0–U4 stage carries an explicit "Stage gate"/"Exit bar"; earlier stages gate later ones) + \tracker.md (the grid). Drill libraries (✋ hand-mark / 🛠 tool): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\{aura,ict-course}\exercises.md; concepts.drill_refs holds soft refs like "aura D2-c".
Conventions (reuse, do NOT restate): trade-schema.md §Schema Conventions; the 5b/5c/5d backend idiom (SQLAlchemy 2.0 models; Pydantic schemas per app/schemas/{auth,content}.py; routers per app/routers/content.py — auth-gated via get_current_user; raw-SQL Alembic mirroring 0002/0003 if any DDL is needed); the 5d frontend idiom (lib/content.ts hooks + TanStack Query hierarchical keys + PATCH-then-invalidate; shadcn primitives; the MarkdownRenderer/badges already built).
Repo: C:\Users\PaulRussell\repos\neurospect-learn (api/ backend, app/ frontend). Wiki content source (READ-ONLY): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\**.

PREREQ: local Postgres with the 5c schema + seed + the 5d content ingest. Dev container `neurospect-learn-db` on :5433 (matches api/.env). If gone/stopped: `docker start neurospect-learn-db` (or re-create per 5c prereq), then `cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts && poetry run python -m scripts.ingest_content` (→ 41 concepts + 67 content pages). Frontend + backend both installable (5b–5d verified).

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC; READ-ONLY on the wiki, never write back,
   never read sources/ or vault/), Architecture Doc Integrity (CODE is ground truth; finalizing the concept_progress
   lifecycle + the drills data model is EXPECTED to diverge from the sketch, so you MUST reconcile learning-platform.md
   before sign-off), and "Paul handles git — NEVER commit".
2. Read learning-platform.md §Progress data model (concept_progress: ladder_stage SMALLINT CHECK 1–4, confidence 1–5,
   reps, last_practiced, notes; user_id-scoped + soft-deleted; UNIQUE partial (user_id, concept_id) WHERE NOT is_deleted;
   FKs → users, concepts. **Rows are created per-user AT RUNTIME — that is THIS phase.** Stage status is DERIVED, never
   stored). Plus §Route/page taxonomy + §Component/API surface. Read mastery/README + unified/learning-path for the
   ladder + the per-stage exit-bar rules the /path/:stage gate visualizes.
3. Skim the live code: backend — app/models/{concept,concept_progress}.py, app/routers/content.py + app/deps.py
   (get_current_user), app/schemas/content.py, scripts/seed_concepts.py (the AsyncSessionLocal + pg_insert on_conflict
   idiom), alembic/versions/0002_learning_progress.py (concept_progress DDL; the update_updated_at() trigger already
   exists — reuse). frontend — app/src/App.tsx (the /path, /path/:stage, /drills STUB routes still live), lib/content.ts
   (hooks + TanStack Query pattern to mirror), components/content/* + components/ui/*, pages/concept-reader.tsx (add the
   track panel here), e2e/ (the Playwright harness — EXTEND it with 5e specs).

SCOPE — 5e IS (and is ONLY):
  - LEARNING endpoints (new app/routers/learning.py, mounted in main.py; auth-gated via get_current_user; concept_progress
    is user-scoped): GET /api/concepts (list; optional ?stage=U1 filter), GET /api/progress (this user's grid — LEFT JOIN
    concepts × the user's concept_progress so untracked concepts return null ladder/confidence), PATCH /api/progress
    (UPSERT one concept's ladder/confidence/reps/notes/last_practiced for the current user — on_conflict on the unique
    partial index; **lazy create**, no bulk pre-seed), GET /api/stages (per U-stage: its concepts + this user's progress
    + the DERIVED exit-bar status). Pydantic schemas in app/schemas/learning.py.
  - PER-USER concept_progress LIFECYCLE (design-heavy #1): decide + implement lazy upsert (recommend: GET merges via
    LEFT JOIN; PATCH inserts-or-updates; never pre-create rows). Enforce per-user isolation (a second user sees none of
    the first's rows). Respect the CHECK(1–4)/(1–5) constraints; soft-delete semantics as in 5c.
  - STAGE EXIT-BAR derivation (design-heavy #2): a small pure service (e.g. app/services/stages.py) that computes each
    U0–U4 stage's exit-bar "met?" from the user's concept_progress against the rules in unified/learning-path §Stage gate
    (e.g. U1 = all five primitives at ≥Can-mark, conf ≥3, reps ≥ target). COMPUTED, never stored. LINK the rules; do not
    restate them in the wiki. U5 (frontier) is watch-only — never gate-eligible; U6 readiness is OUT OF SCOPE (that live
    "cleared to trade?" gate is 5g — 5e computes only the per-STAGE exit bars for the path view).
  - DRILLS data model (design-heavy #3 — READ mastery/{aura,ict-course}/exercises.md FIRST, then decide): /drills shows
    the two drill libraries (✋ hand-mark / 🛠 tool variants) with rep counters + mark-complete. Pick the drill-definition
    source (parse the two exercise pages into structured drills, vs. derive the drill list from concepts.drill_refs) AND
    the progress store — RECOMMEND a lightweight `drill_progress` table (a NEW Alembic 0004, raw-SQL + reversible,
    mirroring 0002/0003) keyed (user_id, drill_ref TEXT) with reps + variant marks + last_practiced; drill DEFINITIONS
    stay in the wiki. Justify the call in §5e as-built. If you add 0004, never edit 0002/0003.
  - FRONTEND (replace the 5b stubs for /path, /path/:stage, /drills; add the track panel to /concepts/:slug): new
    components per the design — StagePath/StageNode (the U0→U6 spine with per-stage progress rings + gate state),
    ExitBarGate, LadderBadge (1–4), ConfidenceRating (1–5), RepCounter, ConceptTrackPanel (editable ladder/confidence/
    reps → PATCH /api/progress), DrillCard (✋/🛠 + reps + mark-complete). Wire TanStack Query hooks (hierarchical keys +
    PATCH-then-invalidate) + the ky client; reuse the shadcn primitives; RHF+Zod only if a form gets non-trivial (the
    small edits can be controlled inputs). Add a sortable grid ONLY if a view needs one (none shipped yet).

5e IS NOT (build NONE — later phases): the model-aligned journal + its form + /journal (5f), the /expectancy dashboard
  + Recharts (5f — recharts is not re-added until then), the entry-model MACHINE_READABLE_STRATEGY YAML → strategy-record
  parser (5f), the /gate live readiness view + its computation (5g — 5e does per-STAGE exit bars only, NOT the
  live-eligibility gate), R2/screenshots, Claude, backtesting methodology, ALDC anything. No journal/analytics/gate
  endpoints this phase.

EFFICIENT PATH: mirror the established idioms — router like app/routers/content.py (auth-gated, Pydantic responses),
  schemas like app/schemas/content.py, any DDL like alembic 0002/0003 (raw op.execute, reuse update_updated_at()), any
  drill parse like scripts/ingest_content.py, frontend data-fetch like lib/content.ts + TanStack Query. Keep the progress
  edits simple (optimistic or invalidate-on-success).

VERIFY (evidence, not inference — needs the local Postgres + wiki):
  - PATCH /api/progress creates exactly one row for the CURRENT user (spot-check the row); GET /api/progress returns the
    merged grid with that value; re-PATCH updates in place (no dup — the unique partial index holds); a SECOND debug user
    sees NONE of the first user's progress (per-user isolation); CHECK constraints reject ladder=9 / confidence=9.
  - GET /api/stages returns per-stage exit-bar status that flips correctly against a hand-set concept_progress fixture
    (e.g. set U1's five core primitives to Can-mark+conf3+reps → U1 gate "met"; drop one → "not met"). U5 never counts.
  - /drills mark-complete + rep increment persist (reload); if a `drill_progress` table was added, `alembic upgrade head`
    0001→0004 clean + `downgrade` and back up clean.
  - Endpoints require a Bearer token (401/403 without). `tsc -b` + `vite build` clean.
  - Browser (claude-in-chrome, debug-login): /path renders the U0→U6 spine with progress rings; /path/:stage shows its
    concepts + the ExitBarGate reflecting concept_progress; the ConceptTrackPanel on /concepts/:slug edits ladder/
    confidence/reps and the change persists on reload; /drills marks a drill + bumps reps. No console errors. App boots
    (/health=200) with the learning router mounted.
  - EXTEND the Playwright harness (per Paul's standing pattern): add e2e specs for progress edit-persist, stage exit-bar,
    and a drill mark — `npm run test:e2e` green. (global-setup already mints a per-user debug token.)

RECONCILE + BOOKKEEP (mandatory per Architecture Doc Integrity):
  - UPDATE learning-platform.md §Progress data model + §Component/API surface to AS-BUILT (concept_progress lifecycle,
    the stage exit-bar derivation approach, the drills data model + any Alembic 0004, the learning endpoints) + add a
    §5e as-built note (like §5d). Code is ground truth.
  - Mark 5e ✅ in the tracker Plan; add a 5e session-log entry (did / verified / next=5f); append log.md; bump index.md
    last_build. Write the 5f boot prompt when 5f starts (not now).
  - Do NOT edit trade-schema.md or phase3-frontend-structure.md (other lanes).

OUT OF SCOPE: journal, journal form, expectancy, charts, strategy-YAML parsing, the live gate, R2, Claude, backtesting
methodology, ALDC anything. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5d — content API + ingest + library/reader) — ✅ EXECUTED 2026-07-20

Recommended launch: **Sonnet** (`claude --model sonnet[1m]`), `/effort high` for the slug-scheme + wikilink-
resolution + `content_slug` reconciliation seam (the one genuinely design-heavy part; the rest is a parser +
CRUD + a markdown reader). No plan mode — this executes the approved [[concepts/architecture/learning-platform]]
design. Working dir: open at `C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from
the wiki to read §Content delivery first. **Prereq:** local Postgres with the 5c schema+seed (the
`neurospect-learn-db` container on :5433, matching `api/.env`) **and** the wiki readable at
`C:\Users\PaulRussell\repos\neurospect-wiki`. If the DB is gone/stopped: `docker start neurospect-learn-db`
(or re-create per the 5c prereq), then `cd api && poetry run alembic upgrade head && poetry run python -m
scripts.seed_concepts` (41 concepts). Paste:

````
Neurospect — Phase 5d: CONTENT API + INGEST + LIBRARY/READER for `neurospect-learn` (wiki markdown → content_pages; read/search endpoints; `/library` browser + `/concepts/:slug` reader with markdown render, [[wikilink]] resolution, TIER/label badges, search).
Design spec (READ FIRST, it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Content delivery, §Route/page taxonomy (/library, /concepts/:slug), §Component structure + API surface, §5c as-built (content_pages shape + the PROVISIONAL concepts.content_slug soft refs — CODE is ground truth).
Conventions (reuse, do NOT restate): trade-schema.md §Schema Conventions; the 5b/5c backend idiom (SQLAlchemy 2.0 models; Pydantic schemas per app/schemas/auth.py; routers per app/auth/router.py; raw-SQL Alembic if any DDL is needed).
Repo: C:\Users\PaulRussell\repos\neurospect-learn (api/ backend, app/ frontend). Wiki content source (READ-ONLY): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\**.

PREREQ: local Postgres with the 5c schema + seed. Dev container `neurospect-learn-db` on :5433 (matches api/.env). If gone/stopped: `docker start neurospect-learn-db` (or re-create per 5c prereq), then `cd api && poetry run alembic upgrade head && poetry run python -m scripts.seed_concepts` (→ 41 concepts). Frontend + backend both installable (5b/5c verified).

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC — the ingest READS Neurospect wiki content
   and must NEVER write back to the wiki, and must never read from `sources/`, `vault/`, or any ALDC path),
   Architecture Doc Integrity (CODE is ground truth; the 5d ingest OWNS the real content-page slug scheme, so you
   MUST reconcile the PROVISIONAL concepts.content_slug values seeded in 5c — see the reconciliation task — and
   UPDATE learning-platform.md §Content delivery to as-built before sign-off), and "Paul handles git — NEVER commit".
2. Read learning-platform.md §Content delivery + §Route/page taxonomy + §Component/API surface + §5c as-built IN
   FULL. content_pages ALREADY EXISTS (empty) with: slug (UNIQUE), title, body, u_stage, tier, label, category,
   tags (TEXT[], GIN), wikilink_targets (TEXT[]), source_path. NO schema change should be needed — if you add a
   column/index, do it in a NEW Alembic 0004 (raw-SQL, reversible, mirroring 0002/0003), never edit 0002.
3. Skim the live code: backend — app/main.py (router mount), app/auth/router.py + app/deps.py (get_current_user),
   app/models/{content_page,concept}.py, scripts/seed_concepts.py (the AsyncSessionLocal + pg_insert on_conflict
   idiom to mirror). frontend — app/src/App.tsx (the /library + /concepts/:slug STUB routes from 5b),
   app/src/lib/api.ts (ky + TanStack Query patterns), app/src/components/ui/* + layout shell.

SCOPE — 5d IS (and is ONLY):
  - INGEST job (e.g. api/scripts/ingest_content.py via AsyncSessionLocal, idempotent UPSERT on slug) parsing the
    curated wiki dirs → content_pages. Dirs (cover every concepts.content_slug target): concepts/course/**,
    concepts/entry-models/*, concepts/mastery/**, concepts/advanced/*, concepts/business-logic/*, concepts/aura/*.
    Per page: parse YAML frontmatter (tags, aliases, tier/label if present), derive title (first # H1 or
    frontmatter), set category from the top-level dir, set u_stage where determinable (frontmatter/tags; else NULL
    — not load-bearing), extract the set of internal [[wikilink]] targets → wikilink_targets, store the raw
    markdown body, set source_path. Wiki root CONFIGURABLE (add WIKI_CONTENT_ROOT to app/config.py, default the
    sibling ../neurospect-wiki; document in .env.example). READ-ONLY on the wiki; skip sources/ + vault/.
  - SLUG SCHEME + content_slug RECONCILIATION (the load-bearing decision): pick ONE deterministic content-page
    slug scheme (recommend: path under concepts/ minus .md, README → the dir name, de-collided — YOUR call,
    justify it). Then reconcile the 5c-seeded PROVISIONAL concepts.content_slug values (wiki page basenames, e.g.
    ict-liquidity, ranges, session-kill-zones, daily-bias, consolidation-model) so they RESOLVE to real
    content_pages.slug rows — EITHER make the ingest emit matching slugs OR update scripts/seed_concepts.py
    content_slug values + re-seed. VERIFY every non-null concepts.content_slug resolves (report any that don't; a
    few synthesis concepts are intentionally NULL — u2-4, u5-smt-confirm-axis, u5-confluence-stack).
  - CONTENT endpoints (new app/routers/content.py, mounted in main.py; auth via get_current_user for parity with
    the protected SPA; content is SHARED, not user-scoped): GET /api/content/pages (list/tree — slug, title,
    category, u_stage, tier, label; grouped for the library), GET /api/content/pages/{slug} (full page incl. body
    + wikilink_targets), GET /api/content/search?q= (simple — ILIKE on title/body or Postgres to_tsvector; small
    corpus, keep it simple). Pydantic response schemas in app/schemas/content.py.
  - FRONTEND: /library (content browser — grouped/tree by category: course / entry-models / mastery / aura /
    business-logic / advanced; searchable) and /concepts/:slug (content reader — render markdown, resolve
    [[wikilinks]] → /concepts/:target-slug, show TIER/LabelBadge — prefer the referencing concept's badge from
    the concepts table). Add react-markdown (+ remark-gfm) to app/ deps. New components: MarkdownRenderer
    (wikilink rewrite → internal links; UNRESOLVED links render inert/disabled), TierBadge, LabelBadge, a search
    input/command. Replace the 5b STUB pages; wire TanStack Query hooks (hierarchical keys) + the ky client.

5d IS NOT (build NONE — later phases): concept-progress editing / the "track this" ConceptTrackPanel (5e),
  /path + /path/:stage + /drills (5e), the journal + form + expectancy (5f), the entry-model
  MACHINE_READABLE_STRATEGY YAML → structured strategy-record extraction for the journal model picker (5f — 5d
  ingests those pages as ordinary content; do NOT build the strategy parser), the gate (5g), R2/screenshots,
  Claude. No user-scoped data this phase.

EFFICIENT PATH: mirror the established idioms — ingest script like scripts/seed_concepts.py (AsyncSessionLocal +
  pg_insert on_conflict_do_update), router like app/auth/router.py, schemas like app/schemas/auth.py, frontend
  data-fetch like the 5b lib/api.ts + TanStack Query. Use a lightweight frontmatter parser (e.g. python-
  frontmatter or a small YAML split — add the dep if used). Keep search simple.

VERIFY (evidence, not inference — needs the local Postgres + the wiki readable):
  - Run the ingest → content_pages count matches the ingested files; spot-check a page (frontmatter parsed,
    title/category/tags/wikilink_targets correct, body present); re-run → idempotent (no dupes).
  - EVERY non-null concepts.content_slug resolves to a content_pages.slug (SQL left-join: unresolved count = 0,
    excluding the intentionally-null synthesis concepts).
  - Endpoints: GET /api/content/pages returns the tree; GET /pages/{slug} returns a known page w/ body;
    /search?q= returns hits; all require a Bearer token (401/403 without).
  - Frontend: `tsc -b` + `vite build` clean; /library renders the grouped corpus; /concepts/:slug renders
    markdown with a [[wikilink]] click-through to another /concepts route; an unresolved wikilink is inert;
    TIER/label badge shows on a frontier concept page; search returns results. Browser-verify via claude-in-chrome
    (debug-login). App still boots (/health=200) with the content router mounted.

RECONCILE + BOOKKEEP (mandatory per Architecture Doc Integrity):
  - UPDATE learning-platform.md §Content delivery to AS-BUILT (chosen slug scheme, ingest dirs, endpoints,
    wikilink-resolution approach, WIKI_CONTENT_ROOT) + add a §5d as-built note (like §5c). If you changed
    concepts.content_slug or added Alembic 0004, record it. Code is ground truth.
  - Mark 5d ✅ in the tracker Plan; add a 5d session-log entry (did / verified / next=5e); append log.md; bump
    index.md last_build. Write the 5e boot prompt when 5e starts (not now).
  - Do NOT edit trade-schema.md or phase3-frontend-structure.md (other lanes).

OUT OF SCOPE: progress editing, drills, journal, expectancy, gate, strategy-YAML parsing, R2, Claude,
backtesting methodology, ALDC anything. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5c — data model + migrations) — ✅ EXECUTED 2026-07-19

Recommended launch: **Sonnet** (`claude --model sonnet[1m]`) with `/effort high` for the journal field-set
finalization (the one genuinely design-heavy part; the rest is mechanical DDL + a seed). No plan mode — this
executes the approved [[concepts/architecture/learning-platform]] design. Working dir: open at
`C:\Users\PaulRussell\repos\neurospect-learn` (code is ground truth), or start from the wiki to read the spec +
taxonomy first. **Prereq:** a local Postgres — the 5b throwaway container is gone; spin one up (e.g.
`docker run -d --name neurospect-learn-db -e POSTGRES_USER=learn -e POSTGRES_PASSWORD=learn -e
POSTGRES_DB=neurospect_learn -p 5433:5432 postgres:16`) and point `api/.env` `DATABASE_URL[_SYNC]` at it. Paste:

````
Neurospect — Phase 5c: DATA MODEL + MIGRATIONS for `neurospect-learn` (concepts, concept_progress, journal_entries, content_pages) + seed concepts + FINALIZE the model-aligned journal field set.
Design spec (READ FIRST, it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md — §Progress + journal data model, §Content delivery, §5b as-built (code is ground truth).
Conventions (reuse, do NOT restate): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\trade-schema.md §Schema Conventions (UUID PK, TIMESTAMPTZ, soft-delete, user_id-scoped, updated_at trigger, GIN for TEXT[]).
Taxonomy to SEED from: C:\Users\PaulRussell\repos\neurospect-wiki\concepts\mastery\unified\learning-path.md + \tracker.md (U0–U6 stages, per-concept ladder/confidence/reps + rep-target, is_core, frontier TIER+label, drill refs).
Repo: C:\Users\PaulRussell\repos\neurospect-learn (api/ = backend; the 5b scaffold is live — users table + Discord/JWT auth only).

BOOT / CONTEXT
1. Read the wiki CLAUDE.md — Isolation Rule (Neurospect only; NO ALDC), Architecture Doc Integrity (CODE is
   ground truth; diverging from the design doc's data-model SKETCH is EXPECTED here — finalizing the journal
   field set is explicitly a 5c deliverable — so you MUST reconcile learning-platform.md §Progress+journal data
   model before sign-off), and "Paul handles git — NEVER commit" (git is untouched; leave it that way).
2. Read learning-platform.md §Progress + journal data model IN FULL — the three-part model: (1) learning
   progress [concepts + concept_progress], (2) model-aligned journal [journal_entries, mode backtest|live],
   (3) the gate is COMPUTED, never stored (do NOT build gate here). Plus §Content delivery for the
   content_pages shape (frontmatter TIER+label+tags, U-stage mapping, wikilink targets). Honor the invariants:
   no frontier (U5) concept is is_core; confluence_tags are watch-only (never gate-eligible).
3. Skim the live api/ code so new models/migrations match the established pattern: app/models/{base,user}.py
   (Mapped/mapped_column style), app/models/enums.py (empty — populate it), alembic/env.py (register every new
   model module), alembic/versions/0001_initial_users.py (raw-SQL op.execute migrations; the update_updated_at()
   trigger fn ALREADY EXISTS from 0001 — REUSE it, do not recreate).

SCOPE — 5c IS (and is ONLY):
  - SQLAlchemy 2.0 models (mirror app/models/user.py) for: concepts, concept_progress, journal_entries, content_pages.
  - Postgres ENUMs in app/models/enums.py + created in the migration: u_stage (U0..U6), journal mode (backtest|live),
    entry_model (the 7 entry models + unified — enumerate from concepts/entry-models/*), range_position
    (discount|eq|premium), plus outcome/grade/session/entry_pda aligned to the taught models. Define these FRESH —
    this is the model-aligned journal, NOT the generic trades schema (do not import neurospect-api's enums).
  - Alembic migrations, raw-SQL op.execute matching 0001: recommend 0002_learning_progress (concepts +
    concept_progress + content_pages + their enums + updated_at triggers) and 0003_journal_entries
    (journal_entries + its enums + trigger + GIN on mistake_tags & confluence_tags). Register new modules in env.py.
  - A re-runnable, IDEMPOTENT seed for concepts (UPSERT on slug) sourced from unified/learning-path.md +
    tracker.md — as a standalone script (e.g. api/scripts/seed_concepts.py via AsyncSessionLocal), NOT baked
    into a schema migration. Seed concepts ONLY; concept_progress rows get created per-user at runtime later.
  - FINALIZE the journal field set: turn the design doc's field SKETCH into concrete columns/enums, resolving
    every "optional/deferred" call explicitly (aura_asset_leg → include or defer; screenshots → deferred;
    missed_trades → deferred). This is the load-bearing authoring task of 5c.
  - IMPORTANT soft-reference rule: concepts.content_slug and drill_refs are a NULLABLE slug + TEXT[] of slugs,
    NOT hard FKs — content_pages is empty until the 5d ingest and drill IDs live in the wiki; a hard FK would
    break the concepts seed.

5c IS NOT (build NONE of these — later phases): any router/endpoint (content 5d; learning 5e; journal/analytics
  5f; gate 5g), any Pydantic request/response schema, the content INGEST job (5d — 5c only creates the empty
  content_pages table), the gate computation (5g — computed, never stored), frontend anything, R2/screenshots,
  Claude. No API surface at all this phase.

EFFICIENT PATH: mirror the 0001 idiom exactly (op.execute raw SQL, CREATE TYPE … AS ENUM, TIMESTAMPTZ DEFAULT
  now(), trg_<table>_updated_at BEFORE UPDATE triggers reusing the existing update_updated_at() fn).
  concept_progress + journal_entries are user_id-scoped + soft-deleted; concepts + content_pages are seed/content
  (concepts not user-editable; still UUID PK + timestamps). Add the indexes the conventions imply (per-user +
  per-grouping-key incl. entry_model & mode on journal_entries; GIN on the TEXT[] columns; UNIQUE on
  concepts.slug + content_pages.slug).

VERIFY (evidence, not inference — needs a local Postgres):
  - `alembic upgrade head` runs 0001→0003 clean; then `alembic downgrade base` and back up clean (reversible).
  - `\d` shows all four tables with correct columns/enums/constraints/indexes + updated_at triggers; UNIQUE on
    concepts.slug + content_pages.slug; FKs (concept_progress→users,concepts; journal_entries→users).
  - Run the concepts seed → row count matches the U0–U6 taxonomy; spot-check a row's u_stage/is_core/rep_target/
    drill_refs; re-run the seed → idempotent (no dupes, no error).
  - Models import clean (`python -c "import app.models.concept, app.models.journal_entry …"`); app still boots
    (`uvicorn app.main:app` → /health=200) with the new models registered.

RECONCILE + BOOKKEEP (mandatory per Architecture Doc Integrity):
  - UPDATE learning-platform.md §Progress + journal data model to the AS-BUILT field set (sketch → final
    columns/enums; record every deferred/added field + why). Add a §5c as-built note (like §5b). Code is ground truth.
  - Mark 5c ✅ in the tracker Plan; add a 5c session-log entry (did / verified / next=5d); append log.md; bump
    index.md last_build.
  - Do NOT edit trade-schema.md (other lane's canonical doc — reference it, don't restate) or phase3-frontend-structure.md.

OUT OF SCOPE: endpoints, Pydantic schemas, content ingest, gate logic, frontend, R2, Claude, backtesting
methodology, ALDC anything. Paul handles git — NEVER commit.
````

## Next Session Boot Prompt (Phase 5b — scaffold `neurospect-learn`) — ✅ EXECUTED 2026-07-19

Recommended launch: **Sonnet** (5b is mechanical lift + scaffold following an approved design; escalate to
`opus` only if the auth wiring or Tailwind-v4 token lift gets genuinely hard). No plan mode — this executes the
approved [[concepts/architecture/learning-platform]] design. **Prerequisite (Paul, optional for local dev):**
real Discord OAuth needs a redirect URI registered on the Discord app; **local 5b can be fully verified with
debug-login** (`VITE_DEBUG=true` + backend `DEBUG=true`), so this is not a blocker. Paste:

````
Neurospect — Phase 5b: SCAFFOLD the new `neurospect-learn` app (repo + lifted spine + Discord auth + shell/nav).
Design spec (READ FIRST, it is the contract): C:\Users\PaulRussell\repos\neurospect-wiki\concepts\architecture\learning-platform.md
Lift sources (COPY FROM, do not modify): C:\Users\PaulRussell\repos\neurospect-app (frontend) + C:\Users\PaulRussell\repos\neurospect-api (backend)
New repo to create: C:\Users\PaulRussell\repos\neurospect-learn  (structure: app/ = frontend, api/ = backend)

BOOT / CONTEXT
1. Read the wiki schema + rules: C:\Users\PaulRussell\repos\neurospect-wiki\CLAUDE.md — obey the Isolation Rule
   (Neurospect only; NO ALDC), Architecture Doc Integrity (once code exists, CODE is ground truth; if you
   diverge from the design doc you MUST reconcile learning-platform.md before sign-off), and "Paul handles git
   — never commit" (initializing the new repo with `git init` is fine; do NOT `git commit`).
2. Read the design doc learning-platform.md IN FULL — §New-app shape, §Frontend stack (lift list), §Backend
   stack, §Route taxonomy, §Component/API surface, §Implementation split. This session builds ONLY Phase 5b.
3. Read the tracker C:\Users\PaulRussell\repos\neurospect-wiki\processes\distributed-workflow\active\learning-platform-ui.md
   (Decisions + the 5b–5g split). 5b is the scaffold ONLY.

SCOPE — 5b IS (and is ONLY):
  - The `neurospect-learn` repo with app/ + api/ as two independently-installable packages.
  - Frontend: the lifted infra spine + rebranded app shell + sidebar nav + protected-route layout + STUB pages
    for every route in the taxonomy + Discord auth (real OAuth wiring + debug-login).
  - Backend: the FastAPI skeleton + Discord OAuth/JWT + a users table (Alembic 0001) + get_current_user +
    /health. NOTHING ELSE.
5b IS NOT (leave for later phases — do NOT build): concepts/concept_progress/journal_entries/content_pages
  tables, the content ingest job, any /content|/learning|/journal|/analytics|/gate endpoint, the journal form,
  charts. Those are 5c–5g. Build stubs, not features.

EFFICIENT PATH — COPY, DON'T AUTHOR. The spine is proven; regenerating it by hand is waste and risk. Bulk-copy
files from the lift sources (PowerShell Copy-Item / cp), THEN prune + rename + rewrite the few domain files.

  FRONTEND (into app/) — COPY VERBATIM from neurospect-app, then edit only where noted:
    • Root config, copy as-is: package.json (then PRUNE deps — drop recharts/react-day-picker only if unused
      in 5b; keep the rest), vite.config.ts, tsconfig*.json, eslint.config.js, components.json, index.html.
    • Copy as-is: src/index.css (Tailwind v4 token blocks — verify the `hsl(var(--...))` setup transfers; the
      survey flagged there is no `@theme inline` block), src/lib/utils.ts, ALL of src/components/ui/ (25 files).
    • Copy then EDIT: src/main.tsx (provider stack unchanged), src/lib/api.ts (rename TOKEN_KEY export +
      localStorage key → `neurospect_learn_token`), src/lib/auth.ts (same rename; keep the Discord OAuth +
      debugLogin logic), src/types/api.ts (KEEP only the User/auth-token shape; DELETE all ICT domain types),
      src/components/layout/{app-shell,sidebar,user-menu}.tsx (REMOVE ActiveTradeBadge + BrokerDisconnectedBanner
      from app-shell; REPLACE sidebar navItems + the "Neurospect / ICT Trading Journal" brand; keep the mobile
      Sheet + NavLink active-styling pattern), src/pages/{login,auth-callback}.tsx (rebrand only).
    • REWRITE: src/App.tsx — new createBrowserRouter route table per the taxonomy: public /login + /auth/callback;
      ProtectedLayout (unchanged pattern) wrapping /path (index), /path/:stage, /library, /concepts/:slug,
      /drills, /journal, /journal/new, /journal/:id, /expectancy, /gate. Each protected route = a STUB page
      component rendering the page title + "Phase 5x — coming soon". sidebar navItems: Path, Library, Drills,
      Journal, Expectancy, Gate (lucide icons). Redirect / → /path.
    • DO NOT COPY (leave behind): src/components/{trade,coach,coach-setup,screenshot,settings}, the domain hooks
      (use-trades/tradovate/tv-token/coaching/screenshots/active-trade/analytics), src/lib/constants.ts (rebuild
      later), src/pages/{trades,trade-detail,new-trade,dashboard,coach,coach-setup,settings-broker}.

  BACKEND (into api/) — COPY the skeleton from neurospect-api, then STRIP to the users-only slice:
    • Copy then PRUNE: pyproject.toml (keep fastapi, uvicorn, sqlalchemy[asyncio], asyncpg, alembic,
      pydantic-settings, httpx, python-jose[cryptography], python-multipart, psycopg2-binary; DROP boto3 +
      anthropic — no R2/Claude in 5b), .gitignore, alembic.ini, alembic/env.py (the sync-URL env pattern).
    • Copy then EDIT: app/config.py (keep DATABASE_URL[_SYNC], JWT_*, DISCORD_*, DEBUG; drop R2/Claude/TV vars),
      app/database.py (async engine + AsyncSessionLocal), app/deps.py (get_db + get_current_user), app/auth/
      {discord.py, jwt.py, router.py} (exchange_code, get_discord_user, create/verify token, POST /auth/discord/
      token + GET /auth/me + debug-gated POST /auth/debug/token), app/models/{base.py, user.py} (+ enums.py may
      be empty for now), app/schemas/ (auth: TokenResponse, UserResponse).
    • WRITE FRESH: alembic/versions/0001_initial_users.py — update_updated_at() trigger fn + users table +
      trigger ONLY (mirror neurospect-api 0001 but users-only; NO trades/coach/broker tables). app/main.py —
      FastAPI app, lifespan, mount auth router, GET /health → {"status":"ok"}.
    • .env.example — DATABASE_URL (asyncpg), DATABASE_URL_SYNC (psycopg2), JWT_SECRET, JWT_EXPIRE_MINUTES,
      DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, DEBUG. app/.env.example (frontend) — VITE_API_URL,
      VITE_DISCORD_CLIENT_ID, VITE_DISCORD_REDIRECT_URI, VITE_DEBUG.

  Discord: reuse the SAME Discord application (client id) with a new redirect URI for the learn app; the backend
  mints its OWN JWTs against its OWN users table (independent of neurospect-api). A second Discord app is also
  fine — Paul's call; default to reuse + new redirect URI.

VERIFY (must pass before sign-off — evidence, not inference):
  Backend: `poetry install` clean; `cp .env.example .env` + local test DB URL + dummy secrets + DEBUG=true;
    `alembic upgrade head` creates the users table; `uvicorn app.main:app --reload` → /docs loads, GET /health
    = 200; POST /auth/debug/token {discord_id:"test"} → JWT; GET /auth/me with `Bearer <jwt>` → the user.
  Frontend: `npm install` clean; `cp .env.example .env` (VITE_DEBUG=true, VITE_API_URL=http://localhost:8000);
    `npm run dev` → localhost:5173; `tsc -b` clean; debug-login → lands on /path; hitting a protected route
    while logged out redirects to /login; sidebar renders all six nav items + each stub route loads.

RECONCILE + BOOKKEEP (in the wiki — this is mandatory per Architecture Doc Integrity):
  - If implementation diverged from the design doc (final dep versions, repo layout, an auth detail), UPDATE
    concepts/architecture/learning-platform.md to match the code (code is ground truth) and note the change.
  - Mark Phase 5b ✅ in the tracker Plan; add a 5b session-log entry (did / verified / next=5c); append log.md.
  - Do NOT touch phase3-frontend-structure.md (other lane) beyond the version-drift note already flagged.

OUT OF SCOPE: any 5c–5g feature (data tables, content ingest, journal, charts, gate), R2, Claude, backtesting
methodology, ALDC anything. Paul handles git — `git init` the new repo is fine; NEVER `git commit`.
````

## Next Session Boot Prompt (Phase 5a — Learning Platform UI design) — ✅ EXECUTED 2026-07-18

Recommended launch: `claude --model opus[1m]`, then `/effort high`, in **plan mode** — this is a design
session and the plan is the load-bearing artifact. Working dir: `C:\Users\PaulRussell\repos\neurospect-wiki`
(design lives here; the NEW app will get its own repo, and the existing app to lift from is
`C:\Users\PaulRussell\repos\neurospect-app`). Paste:

```
Neurospect — Phase 5a: DESIGN the Learning Platform as a NEW app (course frontend + progress tracking).
Working dir: C:\Users\PaulRussell\repos\neurospect-wiki  |  Existing app to lift from: C:\Users\PaulRussell\repos\neurospect-app

BOOT / CONTEXT
1. Read CLAUDE.md IN FULL — obey the Isolation Rule (Neurospect lane only; NO ALDC content/refs), Architecture
   Doc Integrity (code in neurospect-app is ground truth; write ONE canonical frontend doc; no-drift: LINK,
   never restate), Page Format, Rules #3 (index.md), #4 (log.md), #5 (prefer updating), #6 (flag
   contradictions), #7 (cite). Paul handles git — commit only if he asks.
2. Read processes/distributed-workflow/active/learning-platform-ui.md IN FULL — this tracker; the Goal,
   Decisions (2026-07-18), and this boot prompt are the work plan.
3. Survey the CONTENT the UI must surface (do NOT restate it — the UI renders/links it):
   - concepts/mastery/README.md — the grading model the UI VISUALIZES (ladder Learned→Can-mark→Backtested→
     Live-ready, 1–5 confidence, rep counters, Readiness-to-Live Gate). This is the spine of the tracking UI.
   - concepts/mastery/unified/{README,learning-path,tracker,divergence-rulings}.md — the sequenced curriculum
     + the living per-concept progress grid the UI turns into real data.
   - concepts/mastery/{aura,ict-course}/{rules,exercises,tracker,...}.md — the two per-track corpora + drill
     libraries (✋ hand-mark / 🛠 tool variants) the UI must expose as trackable exercises.
   - concepts/course/* (16 lessons), concepts/entry-models/* (7 models + AI-coach YAML), concepts/advanced/*
     (frontier pages, each carrying a source TIER + ESTABLISHED/EMERGING/SPECULATIVE label — the UI MUST
     preserve those labels and never let a learner "go live" on an EMERGING/SPECULATIVE concept).
4. Survey the EXISTING APP as a SOURCE to LIFT FROM (proven stack + patterns + schema) — the Learning Platform
   is a NEW app, NOT a module bolted onto this one, but it should reuse what already works:
   - concepts/architecture/phase3-frontend-structure.md — CANONICAL frontend doc (React 19 + TS + Vite 6 +
     React Router v7 + TanStack Query v5 + React Hook Form/Zod + ky + shadcn/ui + Recharts; app-shell +
     sidebar nav + trade journal + analytics + settings/broker modules). Lift the stack + shell/nav pattern.
   - concepts/architecture/phase4-coach-frontend.md — the AI-coach frontend module (pattern to mirror).
   - concepts/architecture/{phase2-project-structure,trade-schema,tech-stack,tradingview-connector}.md — backend
     project layout, the trade data model + ENUMs + API surface, the stack, the coach pipeline.
   - Read the actual code in C:\Users\PaulRussell\repos\neurospect-app (src/) — it is ground truth for the
     patterns you lift (auth flow, TanStack Query setup, shadcn config, trade forms/tables). Note what is
     cleanly reusable vs. what is journal-app-specific coupling you should leave behind.

OBJECTIVE
Design the optimal **new, standalone Learning Platform app** that (a) surfaces ALL course content in a clean,
navigable layout, and (b) tracks Paul's progress across THREE axes in one place — **learning exercises,
backtesting, and live trading** — graded on the EXISTING ladder/confidence/gate, so the platform visibly
drives him toward consistent profitability (proven positive expectancy → gate → live). Build it fresh and
integrate features from neurospect-app as needed (clean start, selective lift — not a fork).

Decide and justify, in a written design doc, at least:
  0. NEW-APP SHAPE — propose the repo name/location (e.g. `neurospect-learn`), the stack (default: reuse the
     neurospect-app stack unless there's a reason to diverge), and — critically — the BACKEND decision: does the
     new app SHARE `neurospect-api` (add learning/backtest endpoints there, reuse Discord auth + Postgres) or
     stand up its own backend? Recommend one; note the monorepo-migration workstream
     ([[processes/distributed-workflow/active/monorepo-migration]]) so siting is consistent.
  1. ROUTE / PAGE TAXONOMY — the app's sections + pages (e.g. Curriculum/roadmap view, Concept detail,
     Exercise/drill tracker, Backtest logger + expectancy dashboard, Gate/readiness view). Map to the U0–U6
     stages of unified/learning-path.md.
  2. CONTENT-DELIVERY approach — how the markdown corpus reaches the UI: build-time MDX/markdown import vs. a
     content API vs. a one-time port. Trade-offs (authoring stays in the wiki? sync? search?). Pick one, justify.
  3. PROGRESS + BACKTEST DATA MODEL — the biggest decision. The tracker.md grids (ladder 1–4 / confidence 1–5 /
     reps / target per concept), exercise completion (hand-mark vs tool variant), and BACKTEST results per model
     (sample size, win rate, avg R, expectancy) need to be real data. Decide: reuse the trade-schema.md trades
     table (e.g. a `mode: backtest|live` flag so the SAME journal powers backtest expectancy AND live stats) vs.
     a new learning-progress schema (concepts + exercises + backtest_sessions tables) — and where it lives given
     the backend decision in step 0. Show the tables/ENUMs and how expectancy is computed and compared to the
     gate threshold. Preserve the Readiness-to-Live Gate logic (no concept counts as "Backtested+" without the
     required sample) — and NEVER surface an EMERGING/SPECULATIVE frontier concept as trade-live-eligible.
  4. COMPONENT STRUCTURE + API SURFACE — reuse the shadcn components, TanStack Query patterns, and Recharts
     (for the expectancy/progress charts) lifted from neurospect-app. List new components + new backend endpoints.
  5. IMPLEMENTATION SPLIT — sequence 5b+ into buildable sessions (e.g. scaffold new app + auth → schema+API →
     content browser → progress tracker → backtest logger + expectancy → gate view), each a boot-promptable unit.

QUALITY BAR
- No-drift: the UI VISUALIZES the mastery model, roadmap, trackers, exercise libraries, and entry-model YAML —
  it LINKS/renders them; the design doc does not restate their content. If the UI needs data the wiki/app lacks,
  flag it; don't invent silently.
- Preserve every source TIER + ESTABLISHED/EMERGING/SPECULATIVE label in the UI; the gate governs sim→live.
- New app, but REUSE the proven neurospect-app stack + patterns by selective lift; justify any divergence. Cite
  the canonical architecture docs; surface any contradiction with the current code.

WORKFLOW / OUTPUT
- FIRST present the PLAN in plan mode for approval: the route taxonomy, the content-delivery choice, the
  data-model decision (with the schema sketch), and the implementation split. Do NOT write pages or code until
  approved.
- THEN on approval: write ONE canonical frontend design doc under concepts/architecture/ (propose
  `learning-platform-frontend.md`), add its implementation phases to this tracker, additive cross-links from
  mastery/README + unified/README + phase3-frontend-structure.md, update index.md, append log.md, add a Phase
  5a session-log entry here.
- OUT OF SCOPE this session: writing app code (design only), the backtesting METHODOLOGY/curriculum content
  (separate), and ALDC anything. Paul handles git — commit only if he asks. Respect the Isolation Rule.
```

## See Also

- [[processes/distributed-workflow/active/mastery-layer]] — the content workstream this UI delivers (✅ complete)
- [[concepts/mastery/README]] — the grading model the UI visualizes
- [[concepts/mastery/unified/learning-path]] · [[concepts/mastery/unified/tracker]] — the roadmap + grid the UI renders
- [[concepts/architecture/phase3-frontend-structure]] — the existing neurospect-app frontend (extend this)
- [[processes/distributed-workflow/active/journal-analytics]] — the journal/analytics app workstream
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`
