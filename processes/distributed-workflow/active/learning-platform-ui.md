---
tags: [distributed-workflow, active, neurospect, mastery, frontend, ui]
aliases: [Learning Platform UI Tracker, Phase 5 UI, Mastery UI]
sources: []
created: 2026-07-18
updated: 2026-07-18
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

### Phase 5b — Scaffold ⏭ NEXT (in `neurospect-learn`)
Create the `neurospect-learn` repo (`app/` + `api/`); lift the frontend infra spine + backend skeleton;
Discord OAuth end-to-end; app shell + nav + protected routes.

### Phase 5c — Data model + migrations
`concepts` + `concept_progress` + `journal_entries` + `content_pages`; Alembic migrations; seed `concepts`
from the U0–U6 taxonomy; **finalize the model-aligned journal field set** (the biggest new-authoring piece).

### Phase 5d — Content API + ingest + library/reader
Ingest job (wiki markdown → `content_pages`, TIER/label preserved); content endpoints; `/library` + `/concepts`
(markdown render, wikilink resolver, badges, search).

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

## Next Session Boot Prompt (Phase 5b — scaffold `neurospect-learn`) ⏭ ACTIVE

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
