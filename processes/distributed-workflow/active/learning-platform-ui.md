---
tags: [distributed-workflow, active, neurospect, mastery, frontend, ui]
aliases: [Learning Platform UI Tracker, Phase 5 UI, Mastery UI]
sources: []
created: 2026-07-18
updated: 2026-07-19
---

# Learning Platform UI — Workstream Tracker

Give the completed learn-to-execute knowledge base a **front end**: a **new, clean Learning Platform app** that
surfaces all the course content **and** tracks Paul's progress across the three axes that carry a trader to
consistent profitability — **learning exercises → backtesting → live trading** — graded on the existing
[[concepts/mastery/README|mastery ladder + confidence + Readiness-to-Live Gate]]. This is the delivery layer
on top of the [[processes/distributed-workflow/active/mastery-layer|Mastery Layer]] workstream (content ✅
complete: mastery system, both tracks, unified playbook, frontier ICT, graded roadmap + tracker, Tier-1 sourcing).

## Goal

Turn the static markdown roadmap + per-concept trackers into a **living, interactive platform** so Paul can:
1. **Read / navigate** all course content (course, entry-models, unified playbook, frontier pages, exercise libraries).
2. **Track learning progress** per concept on the ladder (Learned → Can-mark → Backtested → Live-ready) + 1–5
   confidence + rep counters — the data that currently lives only in `*/tracker.md`.
3. **Log backtests** (replay sessions) per model and see **expectancy** build toward the gate (sample size,
   win rate, avg R, expectancy) — the empirical proof-of-edge loop.
4. **See gate status** — a clear "cleared to live?" signal per model driven by the Readiness-to-Live Gate.

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

### Phase 5e — Progress tracker
`/path` + `/path/:stage` + concept-progress editing (ladder/confidence/reps) + `/drills`.

### Phase 5f — Journal + expectancy
Model-aligned `/journal` (backtest|live) + `/expectancy` dashboard (per-model, backtest vs live).

### Phase 5g — Gate/readiness view
`/gate` computed readiness over progress + backtest expectancy + checklist; watch-only enforcement for frontier.

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

## Next Session Boot Prompt (Phase 5e — progress tracker) ⏭ ACTIVE

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
