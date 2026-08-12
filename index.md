---
tags: [index, navigation]
created: 2026-04-18
updated: 2026-08-11
last_fork: 2026-04-26-broker-integration-forked-from-journaling-ux
last_build: 2026-08-11-prospect-divergent-council-skill-authored-boundary-first-halts-on-closed
last_design: 2026-07-28-learning-enforcement-e1-evidence-grading-anticheat-gamification
last_ingest: 2026-07-16-aura-phase3-reconciliation
last_research: 2026-07-18-mastery-phase4b-tier1-ipda-silverbullet-asianrange
---

# Neurospect Wiki Index

Master catalog of all Neurospect wiki pages.

> **Isolation Rule:** This wiki is fully decoupled from the ALDC work wiki. The only allowed cross-wiki reference is ALDC research → Neurospect, by absolute path, from trackers. See [[CLAUDE]] § *Isolation Rule*.

---

## Entities

### Projects

- [[entities/projects/neurospect]] — core project entity (ICT trading journal + AI coach)

### People

- [[entities/people/mrwitness-axl]] — MrWitness and Axel (AXL), the two instructors delivering the mentorship curriculum
- [[entities/people/doomer]] — dOoMeR, instructor of the second "Aura" mentorship corpus (ICT/SMC, psychology-first)

### Tools

_None yet._

---

## Roadmap

Forward-looking product roadmap (horizons: Now / Next / Later / Strategic / Research / Compliance-Sensitive). Supersedes the v1 phased plan in `entities/projects/neurospect.md` for forward decisions.

- [[concepts/roadmap/README]] — main roadmap with horizon assignments, prioritization rationale, lifecycle convention. **⚠ FLAGGED STALE 2026-08-10 (Rule #6): the horizons and the "no new features until deployed" Now-gate predate `neurospect-learn` entirely** (written 2026-04-25 for the `neurospect-api`/`neurospect-app` generation). Two complete workstreams have shipped against a different codebase since — the Phase 5 arc and the full **E1–E6 enforcement arc** — and neither appears on it; the 2026-08-09 "learning platform is THE focus" decision never propagated either. The **idea catalogue is still good; the horizon assignments and the Now-gate are not.** Re-horizon before trusting any assignment.
- [[concepts/roadmap/ideas/README]] — idea-backlog index (**19 stubs**)
- [[concepts/roadmap/ideas/backtest-companion-layer]] — **the committed lane as of 2026-08-10** (`designing`): `neurospect-learn` as the **discipline + insight layer around a backtesting session held in another tool** (Paul moved backtesting to **Tradezella**), and the **companion** positioning that follows — integrate with the apps a trader already chose rather than absorb them. Deliberately close to the **opposite** of [[concepts/roadmap/ideas/platform-consolidation]] / [[concepts/roadmap/ideas/vertical-ai-platform]], and the design session is required to argue the two against each other on merit. The wedge is the thing no journaling tool has: E1–E6 can say whether the work was **actually done** (evidence-derived reps), whether it **met its own bar** (wiki-projected rubrics), and whether the call **preceded the outcome** (the frozen ledger). Tracker: [[processes/distributed-workflow/active/backtest-companion]].

---

## Concepts

### Business Logic

- [[concepts/business-logic/ict-liquidity]] — BSL/SSL, swing highs/lows, DOL, FVG (BISI/SIBI), IOFED, BAG — the two forces that move price
- [[concepts/business-logic/ict-narratives]] — 4 stages of algorithmic price delivery (consolidation/expansion/retracement/reversal), Power of Three (AMD), session kill zones, opening prices, daily bias (Vol 1–2)
- [[concepts/business-logic/ict-entry-models]] — FVG, order blocks, rejection blocks, breaker blocks, BPR, OTE, Model 2022, CSD, three-step execution framework (Vol 1, 3)
- [[concepts/business-logic/ict-market-structure]] — MSS, BOS, STH/ITH/LTH, STL/ITL/LTL, market structure fractality, CSD, reversal types (Vol 3)
- [[concepts/business-logic/ict-smt]] — SMT divergence, The Triad (NQ/ES/YM), cracking correlation, Price SMT, PDR SMT (Vol 4 Class 2); trust-the-program framework
- [[concepts/business-logic/ict-deviations]] — Fibonacci deviation targeting for HOD/LOD, HPDL, two-set market structure deviations (Vol 2 Class 3, Vol 3 Class 4)
- [[concepts/business-logic/ict-order-flow]] — HTF/LTF order flow, closing basis, quadrant levels, LRLR/HRLR, order block respect/disrespect (Vol 4 Class 1)
- [[concepts/business-logic/ict-live-commentary]] — live pre-market framework, day-of-week protocol, HOD/LOD calling, weekly opening price, first presentation FVG, liquidity void, contract rollover (stream + YouTube ingest)

### Architecture

- [[concepts/architecture/tech-stack]] — canonical backend stack decision (FastAPI + SQLAlchemy async + Postgres on Render + Discord OAuth2 + TradingView webhooks + Cloudflare R2); shared by AI Coach and Journal modules
- [[concepts/architecture/trade-schema]] — ICT trade data model: field definitions, Postgres DDL, indexes, REST API surface (Phase 1 of Journal & Analytics)
- [[concepts/architecture/phase2-project-structure]] — APPROVED project layout for `neurospect-api`: directory structure, Poetry deps, auth flow, analytics SQL approach, file creation order (Phase 2)
- [[concepts/architecture/tradingview-connector]] — AI Coach Phase 3 end-to-end design: Pine Script indicator, `/webhooks/tradingview/{user_token}` validation stack, `coaching_events` table, Claude prompt-cached call, polling endpoint
- [[concepts/architecture/transcript-pipeline]] — transcript ingestion decision doc (manual + Whisper)
- [[concepts/architecture/phase3-frontend-structure]] — **canonical frontend doc**: React 19 + TS + Vite project layout, route map, key patterns (auth, trade form, screenshot upload, analytics hooks), env vars
- [[concepts/architecture/phase4-coach-frontend]] — AI Coach frontend: routes, hooks, component tree, polling strategy, TV token UX, Pine asset sync
- [[concepts/architecture/learning-enforcement]] — **canonical doc** for making progress in `neurospect-learn` **impossible to fake** (E1 design 2026-07-28 + **§E2 as-built 2026-07-28 + §E3 as-built 2026-08-02 — SHIPPED at Alembic `0010`, so code is ground truth for E2's and E3's scope**). **E3 added the rubric layer + self-check:** `rubrics`/`rubric_items` (Alembic `0010`, seed-content shape) holding **44 rubrics / 104 items projected VERBATIM** from the two `exercises.md` libraries — one item per ✋/🛠 bullet, split only on TOP-LEVEL semicolons (sentence-splitting was rejected on evidence: the corpus writes "vs." followed by a capital and every heuristic mangled it — *a parser that can mangle wiki text is a parser that authors it*), with a **programmatic no-drift proof** that every item text is a contiguous substring of a wiki bullet. The rubric API is **READ-ONLY** (405 on every write) so no rubric text can be authored in the app, and the self-check is an **additional** `evidence_grades` row — E3 added no grading table. **Its load-bearing decision: an UNCHECKED rep STILL COUNTS** — a self-check may flag but never retract, because `stages.py`/`gate.py` read `reps` and retraction would make progress non-monotonic; ungraded work is surfaced as an honest backlog, never deducted. E3 also ran the **targeted wiki content pass** (aura D1-c/D2-a/D2-d/D3-a/D3-c + ict D3-d + the **five** aura Stage-0 drills the map omitted ⇒ orphan refs **5 → 0**, drills **53 → 58**). 160 backend tests; **both items E3 handed to E4 are now CLOSED**: the default-parallelism flake never reproduced (3 clean runs + 12 workers + heavy load, 2026-08-07; both named suspects ruled out on measurement, and a real latent defect — blocking CPU/file-IO on the event loop — fixed anyway), and the live browser walkthrough of the self-check **passed 2026-08-09** (thumbnail decoded, wiki bullets as checkboxes with no raw `**`, partial + full check, `reps` unmoved, zero console errors). **E4 — AI vision second reader — is BUILT 2026-08-10** (§E4 as-built), with **two of the design's three mechanisms rejected on evidence**: the Batch API, and then the **cached prefix itself** — measured at **981 tokens against Sonnet 5's 1024-token minimum**, so it cached *nothing and reported no error*; withdrawn rather than padded, because chasing it was worth ~$1.35 across the whole curriculum and the 1.25× write premium would likely have made it a net loss (981 *does* clear Opus 5's 512, so the conclusion is model-specific). What shipped: a closed-enum verdict schema with **no numeric field anywhere** so a price claim is unrepresentable, a durable `pending`-row queue (**no migration** — the states existed since `0009`), full cost telemetry, and an advisory surface that renders **counts not a percentage** plus a two-directional **disagreement** signal (the useful part: where the reader and the trader's own check diverge, decided by neither). Cost is now **MEASURED at $0.0167/grade ⇒ ~$8.37** for the curriculum — about **half** this doc's own $0.02–0.04/$15–25 estimate, flagged under Rule #6, because the closed-enum verdict is tiny (204 output tokens vs an assumed ~500). Two defects that made the *documented* setup impossible were found and fixed: pydantic-settings' default `extra="forbid"` crashed the whole app on an `ANTHROPIC_API_KEY` in `.env`, and `.env` never reached the Anthropic SDK at all (it populates `Settings`, never `os.environ`). 181 backend tests · baseline byte-identical (`27ff7157…`) · live walkthrough clean (the walkthrough itself caught `AiReading` printing raw `*actual*` markers — the exact defect E3 verified the self-check against — now fixed by extracting one shared `RubricText`). **ONE item open: the Playwright battery has not run since E4 landed** (its `webServer` needs :5173, held by another project) — it is E5's STEP 0. **E2's load-bearing outcome: `reps` is DERIVED, not writable** — `0009` renamed `concept_progress.reps`/`drill_progress.reps` to `legacy_reps` and the API computes `legacy_reps + Σ evidence_assets.reps_claimed`, so `PATCH /api/drills`, `PATCH /api/progress` and the planner's mark-done **cannot mint a rep at all** (5g's structural non-overridability idiom applied to `reps`: a guard must be remembered, a derivation cannot be forgotten). Renaming rather than dropping keeps pre-evidence claims so no met stage un-meets, and surfaces the split as `reps`/`reps_evidenced`/`reps_legacy`. Also shipped: R2-**or**-local storage (localhost needs no bucket, signed key-scoped reads), the deterministic tier with **measured** phash thresholds (block ≤4 / flag 5–7, because one new marking on the same chart scores 8–10 — a real extra rep), paste-first capture, and **both inherited screenshot debts closed** (`missed_trade_screenshots` closed *by not building it*). 142 backend tests · Playwright 45 · analytics+gate byte-identical. Still design for E4–E6: AI vision, pre-commitment/calibration, gamification. The evidence model (5 kinds, incl. `prediction` committed *before* the reveal); **three grading tiers** — deterministic blocks, a self-check rubric **projected from** each drill's own ✋/🛠 `exercises.md` bullets (so no rubric text is authored in the app), and AI vision as a **non-blocking advisory second reader**, demoted from arbiter because **MeasureBench** puts frontier VLMs at **19–30%** on precise value readout from analog scales (perceptual limit, unhelped by more thinking) while cost is a non-issue (~$15–25 for the whole curriculum); **provisional-then-graded** lifecycle (a grade flags, never retracts, because `reps` feeds `stages.py`+the Gate and retraction would make progress non-monotonic); anti-cheat that **blocks the certain and surfaces the rest**; gamification that is **informational, not tangible** (Deci/Koestner/Ryan 1999: tangible contingent rewards undermine intrinsic motivation at d ≈ −0.34, praise/feedback does not → no XP/badges/points on rep count, a Goodhart-resistant **calibration score** instead); **ONE** polymorphic evidence layer (Alembic `0009` — `evidence_assets` + `evidence_grades`) serving drills **and** the journal's deferred screenshots **and** `missed_trade_screenshots`; storage lifted from `neurospect-api`'s proven R2 client + a local backend so localhost needs no bucket; and `ict_course` M6 wired via pre-commitment so `stages.STAGE_UNWIRED` empties. E2–E6 split + 3 corrected tracker premises inside **Phase E5 is BUILT 2026-08-10 (§E5 as-built) and `stages.STAGE_UNWIRED` IS NOW EMPTY — E1's acceptance test for the whole workstream is MET.** Alembic `0011` adds `predictions` (bias · DOL · `entry_model` **reused** from `0003` · target), a `prediction_bias` enum where **`neutral` means *stand aside* and is scored like any other call** (T-04 names standing aside), and a `predictions_freeze_the_call()` trigger. **Its load-bearing decision: build the honest form of "cannot be back-dated".** The app cannot see a TradingView replay, so it cannot prove the user did not peek — and claiming otherwise would have been the one unrecoverable error; what it proves instead is that **the record cannot lie**: `committed_at` is server-stamped and refused from the client (a 422 that *names* the field), the call is frozen **by a DB trigger** rather than router discipline (E2's argument reapplied — a guard must be remembered at every write path, a structural property cannot be forgotten), `resolved_at >= committed_at` is a schema CHECK, and the reveal is accepted exactly once. **`predictions` deliberately has NO `is_deleted` column** — breaking this repo's soft-delete convention on purpose, because the calibration score is a **ratio** and the attack is not adding volume but *deleting failures*: with no delete and no edit path the **denominator can only grow**. The Goodhart claim was **restated so it could be tested** — "more reps cannot inflate accuracy" is untestable as written, but as **scale invariance** (multiply the record by k, every percentage identical) it is a test at k = 2, 3, 10, 97; the one surviving bias (resolving only your winners) is **named and published** via `resolution_rate` beside every accuracy rather than claimed away. **M6 grades COMMITMENT, not correctness** — a test scores all 14 tape calls as complete misses and asserts the bar is met while calibration reports **0.0**, because gating a stage on accuracy would make the score a currency and teach the user to stop writing down losing calls. **A zero is never reported for an instrument that has seen nothing** (`accuracy: None`, never `0.0`). E4's one open item is CLOSED (Playwright 50/50 × 3 clean runs at STEP 0). 213 backend tests · Playwright 57 · baseline byte-identical (`27ff7157…`) · all 7 invariants walked. Flagged (Rule #6) and fixed in the wiki: the tape drills' `13 studies + live` rep target parsed to a **13-rep floor on each of the 14 tape drills**. Also flagged: the `--reload` reloader died again (a new router 404'd indistinguishably from a nonexistent route while the worker served stale code), and **one defect only the rendered surface could catch** — the calibration panel printed "0%" one line under "no outcome has been recorded", which a correct query-layer response could never have revealed. **Phase E6 is BUILT 2026-08-10 (§E6 as-built) — THE WORKSTREAM IS COMPLETE and this doc is now code-is-ground-truth end to end.** Alembic `0012` adds `rest_days` + a `rest_days_declared_in_advance()` trigger; the pure `services/honesty.py` computes the five §5 signals per read and stores **nothing**; `services/consistency.py` re-derives the shipped streak from days that carry evidence. **Its load-bearing decision: the honesty strip is a SEPARATE RESOURCE (`GET /api/gate/honesty`), not a field on `GateOut`** — so `services/gate.py` has no honesty value in scope to read, making "these gate nothing" structural rather than a rule to remember (E2's derive-don't-guard and E5's trigger-not-router-discipline, applied once more), and keeping `/api/gate` **byte-identical** to the baseline that has held since E2. Proven, not asserted: a test trips **all five** signals at once, requires the gate JSON unchanged, then asserts the signals really fired so it cannot pass vacuously. **Second decision: §6 says rest days live in `study_preferences`, and they CANNOT** — its existing `blackout_dates` is a `DATE[]` rewritten wholesale on every save, accepts **yesterday**, and records nothing about *when* a date was added, so it cannot answer "was this declared in advance?" in principle; wiring a streak to it would have built the retroactive freeze §6 rejects. `rest_days` has a trigger (a CHECK was impossible — Postgres refuses non-IMMUTABLE expressions, and every form of "today" is STABLE at best), **no `is_deleted`**, and no PATCH/DELETE; the streak reads it and **never** `blackout_dates`. **The rule the strip rests on: a zero from an instrument that cannot see is not a measurement** — every signal reports the population it could inspect and returns **NOT-MEASURED, never `0`**, when that population is empty (E5's `accuracy: None`, owed five times); the sharp case is back-dating, where a capture asserting no `captured_at` can be neither back-dated nor cleared of it and is excluded from the population and reported separately. Every threshold (60s burst, 24h back-dating) is **printed in the signal**; the other three need none. **No XP, no badges, no points, no target, no ring, no percentage.** 263 backend tests · Playwright 68 (three consecutive clean runs) · baseline byte-identical (`27ff7157…`) · all 7 invariants walked · walkthrough 18/18 with zero console errors. Flagged (Rule #6): **one defect only the rendered surface could catch, and it is E5's defect again** — the strip printed "0 of 5 signals had something to measure, across 0 captures" directly beneath five careful "not measured" rows, every word true and together a reassuring zero that undid the exact distinction the strip exists to draw (a query-layer check passes: `measured_count: 0` is a correct count of an empty set).
- [[concepts/architecture/learning-platform]] — **canonical doc** for the new `neurospect-learn` app (**migrations now at `0010`; seeds 74/23/**58**/67 + 44 rubrics / 104 items; `reps` is DERIVED since E2 and each capture is self-checked against the drill's wiki-projected bar since E3 — see [[concepts/architecture/learning-enforcement]] §E2 / §E3 as-built**): separate backend, model-aligned journal, content API, multi-track route taxonomy, 5b–5g split. **Phase 5b scaffold ✅ + 5c data model ✅ (2026-07-19) + 5d content API/ingest/library-reader ✅ + 5e-1 progress foundation ✅ (2026-07-20) + 5e-1b multi-track curriculum ✅ (2026-07-21) + 5e-2 Study Planner engine ✅ (2026-07-22)** (`C:\Users\PaulRussell\repos\neurospect-learn`; code is now ground truth — see §5b/§5c/§5d/§5e-1/§5e-1b/§5e-2 as-built: 9 tables + 11 enums + Alembic 0002–0006 + 74-concept/23-track-stage/53-drill seeds + 67-page content ingest + `/library`/`/concepts` reader + `/path` **three-track switcher** (Aura·AXL·Unified) + `/path/:track/:stage` **curriculum unit** (Read→Drill→Track→Gate) w/ per-track progress + cross-track "Also taught in" links + the **deterministic track-scoped Study-Planner engine + API** (`study_preferences`/`plan_items`, `scheduler.py`, preferences·today·calendar·regenerate·mark-done→progress; 16 tests) + the **Study-Planner UI** (5e-3, 2026-07-23 — `/today` prescriptive ordered plan · `/plan` custom CSS-grid calendar · `/plan/setup` availability form · `lib/planner.ts`; streak/adherence/pace surfaces; mark-done feeds progress) + Playwright 17/17) + **5f journal + expectancy ✅ (2026-07-24)** — model-aligned `/journal` (backtest\|live CRUD + filters + soft-delete) + `/expectancy` dashboard (per-model expectancy in R / win-rate / backtest-vs-live / R-distribution charts + per-model table), `journal`+`analytics` routers over the existing 5c table (no migration) + the pure `services/expectancy.py`, recharts re-added w/ a dataviz-validated palette; 33 backend tests + Playwright 20/20 + **5g gate/readiness ✅ (2026-07-24)** — the computed, **non-overridable** per-model "cleared to live?" verdict: the pure `services/gate.py` combining (a) the unified core ladder at Backtested+ / the model's own entry-model concept at Live-ready (cross-track `cross_refs` credit; `?track=` tightens only) + (b) the **reused** 5f `expectancy.py` (sample ≥50 · expectancy >0 · win rate ≥ break-even) + (c) four attested behavioural items (`gate_attestations`, Alembic `0007`) — no `cleared` column/endpoint/UI control anywhere, frontier never gate-eligible, seed gaps fail closed; `/gate` (`GateSignal`·`GateChecklist`·frontier panel·credit-track selector); 68 backend tests + Playwright 27/27. **THE PHASE 5 ARC IS COMPLETE — every route implemented, no stubs remain** + **Phase 6 Phase-5 debt ✅ (2026-07-25 — CLOSES the workstream)**: **6a** the stage exit bars WIRED to the shipped evidence (`stages.Evidence` + the explicit `STAGE_ATTESTATIONS`/`STAGE_EVIDENCE` maps → a /path row now reflects the `/gate` tick or is EARNED from journal expectancy; U4 corrected to *computability*, A4/M7 = ≥50+positive+above-break-even, U6 = the per-model verdict rolled up; `auto_met`/the lock chain provably unchanged; `/today` wired to the same bundle so the habit overlay finally stops; ict_course M6 honestly left un-wired), **6b** the missed/canceled-trade log + **opportunity cost in R** (`missed_trades` + 2 enums, Alembic `0008`, the pure `services/opportunity_cost.py`, `GET /api/analytics/missed-summary`, a second tab on `/journal`; screenshots deliberately omitted), **6c** `position_size` (record-keeping only); 114 backend tests + Playwright 36/36 + the evidence gate (`/api/analytics/*`+`/api/gate` byte-identical before/after, incl. after writing a +12.5R "would have won" miss) **E5 (2026-08-10) adds the pre-commitment ledger** — Alembic **`0011`** `predictions` (§3b) + `GET /api/calibration`, both computed-per-read, minting **no reps**; `PredictionCommit` renders on the 14 tape drills only and is **two steps that never coexist** (no outcome field exists until the call is committed), and `CalibrationPanel` has **no ring, target, streak or grade**. **E6 (2026-08-10) adds the honesty strip + evidence-backed consistency + declared rest days** — Alembic **`0012`** `rest_days`, `GET /api/gate/honesty` (a **separate resource** from `/api/gate`, so the verdict structurally cannot read it) and `GET | POST /api/rest-days` (no PATCH, no DELETE), plus a `consistency` block on `AdherenceOut` re-deriving the shipped streak from evidence and rendering **beside** the marked figures, never instead of them. Migrations now at **`0012`**; **263 backend tests · Playwright 68**.

### AI Coach

- [[concepts/ai-coach/strategies.json]] — machine-readable strategy library (generated from entry-models YAML blocks; loaded into Claude system prompt)
- [[concepts/ai-coach/system-prompt-template.md]] — full Claude system prompt template (ICT rules + strategy library + JSON output schema); v1.0
- [[concepts/ai-coach/chart-analysis-boot-prompt]] — standalone boot prompt for manual chart analysis sessions (copy-paste into any Claude session with vision)

### Course (Module 1 — Foundations)

- [[concepts/course/README]] — course overview and learning path (5 modules, prerequisite order)
- [[concepts/course/module-1-foundations/01-what-moves-the-market]] — Liquidity (BSL/SSL/DOL), Inefficiency (FVG), the daily price cycle (Vol 1 Cls 1)
- [[concepts/course/module-1-foundations/02-fair-value-gaps]] — FVG precision, BISI/SIBI, IOFED, BAG, inversion FVG, AXL sniper entries (Vol 1 Cls 1–2)
- [[concepts/course/module-1-foundations/03-homework-and-practice]] — Class 1 and Class 2 homework assignments + readiness checklist

### Course (Module 2 — Price Delivery)

- [[concepts/course/module-2-price-delivery/01-four-stages-apd]] — Consolidation/Expansion/Retracement/Reversal overview; real vs. fake retracement; BPR skipping (Vol 1 Cls 2–4)
- [[concepts/course/module-2-price-delivery/02-consolidation-model]] — Stage 1 in depth: range definition, EQ, two delivery paths, SMT at sweep, live NQ example (Vol 1 Cls 2)
- [[concepts/course/module-2-price-delivery/03-expansion-retracement]] — Stages 2 & 3: measuring expansion, real/fake retracement, healthy/choppy, algorithmic body signature, worked examples (Vol 1 Cls 3)
- [[concepts/course/module-2-price-delivery/04-reversals]] — Stage 4: three reversal types (failure swing ~10%, raid on stops ~80%, accumulation ~10%), layered liquidity rule (Vol 1 Cls 4)

### Course (Module 3 — Session Context & Bias)

- [[concepts/course/module-3-session-and-bias/01-power-of-three]] — AMD framework; four opening prices; daily candle anatomy; worked Asia trade example (Vol 2 Cls 1)
- [[concepts/course/module-3-session-and-bias/02-session-kill-zones]] — five KZ windows; opening price anchors; NY AM two-part structure; ORG size; highest-probability stack (Vol 2 Cls 2)
- [[concepts/course/module-3-session-and-bias/03-deviations]] — Fibonacci deviation targeting; HOD/LOD anchoring; HPDL; two worked London examples (Vol 2 Cls 3)
- [[concepts/course/module-3-session-and-bias/04-daily-bias]] — HTF FVG cycle; opening price position; 80% bias framework; live 4H FVG walk-through (Vol 2 Cls 4)

### Course (Module 4 — Market Structure)

- [[concepts/course/module-4-market-structure/01-swing-classification]] — STH/ITH/LTH; gap-qualification rule; why STLs are suspect; MSS trigger; daily chart ITL example (Vol 3 Cls 2)
- [[concepts/course/module-4-market-structure/02-fractality]] — FVG liquidity engineering; engineered swing inside a FVG; turtle soup pattern; multi-TF nesting; daily fractal walk-through (Vol 3 Cls 2)
- [[concepts/course/module-4-market-structure/03-structure-deviations]] — two-set deviation anchoring (ITL price leg + STL measuring swing); convergence zone = HOD/LOD; London and holiday worked examples (Vol 3 Cls 4)
- [[concepts/course/module-4-market-structure/04-model-2022-ote-csd]] — 62–79% OTE zone; OTE block selection (highest open, propulsion block, 0.705 concert); CSD pre-MSS signal; full entry sequence (Vol 3 Cls 5)

### Course (Module 5 — Order Flow & SMT)

- [[concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow]] — bodies vs. wicks; closing basis; quadrant levels (0/0.25/0.5/0.75/1.0); LRLR vs. HRLR; BPR behavior; 5M bearish ES session walk-through (Vol 4 Cls 1)
- [[concepts/course/module-5-order-flow-and-smt/02-smt-divergence]] — triad (NQ/ES/YM); cracking correlation; Price SMT vs. PDR SMT; chart setup (3 methods); distribution and accumulation examples; trust-the-program; Six Sisters distinction (Vol 4 Cls 2)

### Entry Models Library

- [[concepts/entry-models/README]] — library overview, universal minimum confluence, stop/target conventions
- [[concepts/entry-models/consolidation-model]] — consolidation range + EQ + PDA entry; YAML machine-readable strategy block (Vol 1 Cls 2)
- [[concepts/entry-models/expansion-retracement-model]] — FVG/OB in discount after expansion; real retracement checklist; YAML block (Vol 1 Cls 3)
- [[concepts/entry-models/reversal-raid-on-stops]] — liquidity sweep + immediate rejection; layered liquidity rule; YAML block (Vol 1 Cls 4)
- [[concepts/entry-models/london-model]] — London takes Asia side, delivers to other; SMT at sweep; 1–3x/week; YAML block (Vol 1 Cls 2, Vol 2 Cls 2)
- [[concepts/entry-models/model-2022-ote]] — MSS + deep OTE retracement (62–79%); CSD pre-MSS signal; propulsion block selection; YAML block (Vol 3 Cls 5)
- [[concepts/entry-models/daily-bias-model]] — HTF FVG + opening price prerequisite filter; integrates with all other models; YAML block (Vol 2 Cls 4)
- [[concepts/entry-models/smt-confirmation-entry]] — NQ/ES/YM divergence at manipulation leg; Price SMT + PDR SMT; trust-the-program; YAML block (Vol 4 Cls 2)

### Aura Framework (second mentor corpus)

Independent ICT/SMC corpus by [[entities/people/doomer]], captured on its own terms in `concepts/aura/`.
**Phase 3 reconciliation complete (2026-07-16):** attributed Aura content has been merged into the
canonical `ict-*` pages (SMT, liquidity, market-structure, order-flow), the entry-models library,
`trade-schema.md` (new `missed_trades` table), and the roadmap ideas — agreements and divergences
flagged, never silently merged, with two-way cross-refs. See [[processes/distributed-workflow/active/aura-ingest]].

- [[concepts/aura/README]] — Aura framework overview, at-a-glance table, learning path
- [[concepts/aura/psychology-foundations]] — why traders fail; systems > goals; 142-student survey (aura-01)
- [[concepts/aura/mind-and-emotional-control]] — self-image theory; the "four killers"; circuit-breaker rules (aura-02, 03)
- [[concepts/aura/discipline-systems]] — pre/post-market routines + environment design that force discipline (aura-04)
- [[concepts/aura/journaling-system]] — Aura journaling method; essentials + psychological fields; missed-trade tracking (aura-05)
- [[concepts/aura/swing-points]] — 3-candle pivot; SMT-qualification rule (aura-06)
- [[concepts/aura/ranges]] — expansive-move ranges; discount/EQ/premium; close-not-wick validity (aura-08, 11)
- [[concepts/aura/gaps]] — FVG/iFVG/NWOG/NDOG; liquidity within the gap (aura-09)
- [[concepts/aura/triads-asset-selection]] — Pearson-correlation triad selection; the 5 triads (aura-10)
- [[concepts/aura/sequential-smt]] — Sequential SMT (time-cycle nesting) + Sequential Skip (aura-07, 11, 12, 14)
- [[concepts/aura/aura-asset]] — the signature concept: Swiss Franc futures (6S) as universal 4th triad leg (aura-15)
- [[concepts/aura/time-sum]] — digital-root "369" check (dOoMeR de-emphasizes it); Aura Asset usage (aura-16)
- [[concepts/aura/htf-ltf-application]] — cascading HTF→LTF if-then workflow to a 5m trigger (aura-17)
- [[concepts/aura/risk-management]] — Dante "Blueprint": sizing, daily stop, 10R circuit-breaker, expectancy (aura-13)
- [[concepts/aura/trade-reviews]] — 13 consolidated worked examples (aura-18…30)

### Mastery (Learn-to-Execute)

The learn-to-execute layer: turning the models into live-trading skill, with drills and evidence-based
readiness tracking. Two parallel tracks (Aura + ICT-course) plus a Unified track that reconciles both into
one graded roadmap — all built.

- [[concepts/mastery/README]] — mastery hub: the 4-stage ladder, confidence scale, and Readiness-to-Live Gate. §Rep counters now records that a rep IS evidence, self-checked against the drill's own bar, and lists the six drill bars the E3 content pass materially changed
- **Aura (dOoMeR) track:**
  - [[concepts/mastery/aura/rules]] — the Aura model as an executable rulebook (54 rules, cited to aura-NN)
  - [[concepts/mastery/aura/checklist]] — pre-market → framing → entry → management → exit → review sheet
  - [[concepts/mastery/aura/learning-path]] — sequenced curriculum (Stage 0 psychology → Stage 6 live)
  - [[concepts/mastery/aura/exercises]] — drill library (hand-mark + tool-assisted + replay + tape + study-replicate). **The ✋/🛠 bullets are the RUBRIC SOURCE** projected into `neurospect-learn` (E3); updated 2026-08-02 by the E3 content pass — D1-c/D2-a/D2-d/D3-a/D3-c given usable rep floors, D3-a/D3-c's non-ladder `Learned→applied` corrected, and the **five Stage-0 drills added to the drill map** (they were orphan refs since 5e-1)
  - [[concepts/mastery/aura/tracker]] — living per-concept mastery + backtest-expectancy + readiness tracker
- **ICT-course (MrWitness-AXL) track:**
  - [[concepts/mastery/ict-course/rules]] — the 16 lessons' scattered rules normalized into one cited rulebook (41 rules), reconciling the two extra checklist/routine loci
  - [[concepts/mastery/ict-course/exercises]] — drills index + gap-fill (Module 2 + M4.3-4.4) + tape-reading drills from the 11 stream + 2 YouTube transcripts. **The ✋/🛠 bullets are the RUBRIC SOURCE** projected into `neurospect-learn` (E3); updated 2026-08-02 — D3-d's `Learned→applied` (not a ladder stage) corrected to `Can-mark`
  - [[concepts/mastery/ict-course/tracker]] — per-lesson + per-entry-model ladder/confidence/reps + backtest-expectancy + AXL readiness gate
  - *(no separate learning-path/checklist — reuses [[concepts/course/README]] and the entry-model YAML)*
- **Unified track (Phase 3–4 — reconciles both, then grades):**
  - [[concepts/mastery/unified/README]] — the Unified Playbook: one 5-layer sequence (psychology → structural primitives → nested-SMT confirmation → execution → risk) + one-glance decision flow
  - [[concepts/mastery/unified/divergence-rulings]] — 8 cited rulings (R1–R8) reconciling every flagged AXL↔Aura divergence; two new EMERGING confluences (nested SMT stack; double-qualified swing)
  - [[concepts/mastery/unified/learning-path]] — the graded roadmap (Phase 4): U0 psychology → U1 primitives → U2 nested SMT → U3 execution → U4 risk → U5 frontier stacking (study-and-watch) → U6 readiness gate; folds both per-track paths in by reference
  - [[concepts/mastery/unified/tracker]] — living per-concept + per-frontier progress grid (ladder/confidence/reps by U-stage) + Readiness-to-Live Gate

### Advanced / Frontier (Phase 3 deep research)

Deep, less-common ICT concepts researched from the wider body of knowledge to extend the unified playbook — every page source-tiered and labelled ESTABLISHED / EMERGING / SPECULATIVE-or-FRINGE.

- [[concepts/advanced/README]] — frontier hub: source-quality rubric + the cross-cutting WHERE/WHEN/DIRECTION/CONFIRM confluence stack + the unfalsifiability critique
- [[concepts/advanced/ict-macros-and-silver-bullet]] — ICT Macros, killzone micro-structure / Judas swing, Silver Bullet (one model at three zoom levels; SB windows + mechanics **Tier-1** from ICT's own 2023 video)
- [[concepts/advanced/ipda-data-ranges]] — IPDA 20/40/60-day ranges + IRL/ERL (windows + trading-day count **Tier-1**; ranking Tier-3); "liquidity matrix" debunked → PD Array Matrix
- [[concepts/advanced/quarterly-theory]] — Quarterly Theory / 90-min cycles / True-Day-Open disambiguation (community — Trader Daye, not ICT)
- [[concepts/advanced/cbdr-and-sd-projections]] — CBDR / Asian range / flout + standard-deviation projections (SD ≠ Fibonacci disambiguation)

### Patterns

_None yet._

---

## Processes

### Distributed Workflow

- [[processes/distributed-workflow/active/backtest-companion]] — **Backtest Companion** (created 2026-08-10; **Phase B1 deep-research + design ⏭ ACTIVE — SCOPED ONLY, no research done, no design decided, no code written**). Opened the same day the enforcement workstream closed, on Paul's redirect: **Tradezella is now the backtesting tool, chosen and kept**, and the question is what `neurospect-learn` becomes *around* a session it does not host — consistency and discipline during the session, capture and storage of what came out of it, insight across sessions — and whether that generalises into a **companion** positioning that integrates with existing trading apps for product-market fit. Holds **17 open questions** grouped so the **boundary facts come first** (what Tradezella actually exposes — API? export? what does its ToS permit? — because that answer changes the shape of everything downstream, the E4 "measure the thing that can kill the design first" lesson). Flags two hazards up front: **`neurospect-learn` is deployed nowhere** and an integration with a hosted third party may make hosting a genuine prerequisite for the first time (overturning design decision #4); and **n=1** — Paul is the only user this platform has ever had and every number in E1–E6 came from fixtures, so no PMF claim may rest on it. Also carries a **§Recommended tooling** section answering Paul's "council of 5" question: the four installed council skills (`conclave`/`inquest`/`assay`/`vigil`) are all **convergent** — they interrogate an artifact that already exists — and **none fits discovery**, so the recommendation was to author one *divergent* sibling with five orthogonal lenses over the evidence chain of a product bet, boundary-first and able to halt the rest. **That skill was authored 2026-08-11: `⛏ prospect`** (`C:\Users\PaulRussell\.claude\skills\prospect\`, lenses `claimant`/`scout`/`scholar`/`canvasser`/`devil`; signature gate = a boundary probe that **halts the council on CLOSED**; source tier `OBSERVED→MARKETED` where a vendor claim is never a design premise; four kinds of absence including **TRIED-AND-FAILED**; and boundary facts that **expire** with a re-check trigger). It was dry-run against the 17 questions before being called done, and the tracker's new **§Dry-run** section records what that exposed — the mapping is **not** 1:1 (Q4/Q10b/Q11 are internal design questions no external lens should get; Q3 and Q17 need splitting; the skill asks three questions the 17 do not). **B1 must read §Dry-run before briefing a council.** Origin record: [[concepts/roadmap/ideas/backtest-companion-layer]].
- [[processes/distributed-workflow/active/kickoff]] — kickoff workstream tracker (complete — wiki bootstrapped, transcripts ingested, KB populated).
- [[processes/distributed-workflow/active/course-and-kb]] — ICT course construction + entry models library with machine-readable YAML strategy blocks (do first).
- [[processes/distributed-workflow/active/ai-coach]] — AI trading coach module: Claude + TradingView integration, live strategy evaluation (depends on course-and-kb).
- [[processes/distributed-workflow/active/journal-analytics]] — trade journal + analytics module: ICT-specific trade schema, dashboard (parallel to ai-coach).
- [[processes/distributed-workflow/active/deployment]] — Render (backend) + Cloudflare Pages (frontend) + Discord OAuth + TradingView webhook deployment. Phase 4 complete 2026-04-26. R2 screenshots remaining.
- [[processes/distributed-workflow/active/journaling-ux]] — Trade form tab redesign + field reduction + R2 wiring. Phases 1 & 2 complete.
- [[processes/distributed-workflow/active/broker-integration]] — Tradovate REST integration, broker credentials, active-trade soft singleton, `/settings/broker`. Phase 1 spec approved 2026-04-26.
- [[processes/distributed-workflow/active/monorepo-migration]] — consolidate `neurospect-wiki` + `neurospect-api` + `neurospect-app` into one `neurospect` monorepo. Phase 0 (scoping).

- [[processes/distributed-workflow/active/aura-ingest]] — transcribe + synthesize the second mentor corpus (Aura / dOoMeR); reconcile into existing notes. **Complete** — all phases done (30 transcripts, 14 concept pages, reconciled into ict-*/entry-models/schema/roadmap).
- [[processes/distributed-workflow/active/mastery-layer]] — learn-to-execute layer (rules/checklist/learning-path/exercises/tracker per model). **Phases 1–4 done** (mastery system + Aura track + ICT-course track + unified model & frontier ICT + graded learning roadmap & progress tracker). Tier-1 upgrade pass **complete** (Phase 4b, 2026-07-18): CBDR + Midnight Open (Phase 4) → IPDA windows/trading-days, Silver Bullet windows/mechanics, and Asian-range hours (20:00–00:00 ET) all upgraded to Tier-1. Only open item: the IPDA 20→40→60 *ranking* (still Tier-3, unverified). **Content workstream complete → UI hand-off.**
- [[processes/distributed-workflow/active/learning-platform-ui]] — **Phase 5: Learning Platform UI** — a **new app** (integrating features from `neurospect-app` as needed) surfacing all course content + tracking progress across learning exercises / backtesting / live trading, graded on the mastery ladder + Readiness-to-Live Gate. Phase 5a design ✅ + 5b scaffold ✅ + 5c data model + migrations ✅ (2026-07-19) + 5d content API + ingest + library/reader ✅ + 5e-1 progress foundation ✅ (2026-07-20) + 5e-1b multi-track curriculum ✅ (2026-07-21 — three-track switcher + curriculum unit) + 5e-2 Study Planner engine ✅ (2026-07-22 — deterministic track-scoped scheduler + planner API, backend only) + 5e-3 Study Planner UI ✅ (2026-07-23 — `/today`·`/plan`·`/plan/setup`, streak/adherence/pace, mark-done→progress, Playwright 17/17) + 5f journal + expectancy ✅ (2026-07-24) + **5g gate/readiness ✅ (2026-07-24 — the computed, non-overridable per-model "cleared to live?" verdict; `gate_attestations`/Alembic `0007`; frontier never gate-eligible; 68 backend tests + Playwright 27/27)**; **the Phase 5 arc (5a→5g) is COMPLETE** + **Phase 6 — Phase-5 debt ✅ (2026-07-25)**: the stage exit bars wired to the shipped `gate_attestations`/expectancy evidence (no permanently-unmet rows; lock chain provably unchanged; `/path` and `/today` now agree), the missed/canceled-trade log + opportunity cost in R (Alembic `0008`), and `position_size`; 114 backend tests + Playwright 36/36. **✅ WORKSTREAM CLOSED** — all further work (verified drill grading, the deferred uploaded-evidence primitive, anti-cheat, gamification) is [[processes/distributed-workflow/active/learning-enforcement]].

- [[processes/distributed-workflow/active/learning-enforcement]] — **Learning Enforcement** (created 2026-07-25; **E1 + E2 + E3 + E4 ✅ — E4 built 2026-08-10, Playwright still to run; E5 ⏭ ACTIVE**) — make progress in `neurospect-learn` **impossible to fake**: **verified drills** (a rep counts only with uploaded evidence of your chart markings — ranges, std deviations, swings, FVGs, SMT — that is **graded**), **anti-cheat**, and **gamification** for consistency; plus a pass on the learning path's structure and drill quality. Owns the deferred screenshot/R2 evidence layer (journal + `missed_trade_screenshots`). Sharpened north star: *the adversary is self-deception, so the honest path must be the easy one*; **the honest gap it closes is that every existing check ultimately trusts a self-reported `reps` integer**. **Phase E1 design ✅ (2026-07-28)** — all 14 open questions answered (none deferred), all four load-bearing forks decided by Paul, and the design landed as the canonical [[concepts/architecture/learning-enforcement]]: tiered grading (deterministic blocks · self-check rubric projected from the wiki · AI vision advisory-only, demoted on **MeasureBench** evidence), provisional-then-graded lifecycle, block-the-certain/surface-the-rest anti-cheat, informational-not-tangible gamification (Deci/Koestner/Ryan 1999), ONE polymorphic evidence layer (Alembic `0009`) closing both inherited screenshot debts, and pre-commitment wiring for ict_course M6. **Three tracker premises corrected (Rule #6):** the vision-grading cost fear (~$15–25 total, not a real bill), "deploy is unscoped in every tracker" (a proven Render+Cloudflare runbook exists; only `neurospect-learn`'s deploy is unscoped), and the mobile-capture premise (every drill assumes desktop TradingView → paste-from-clipboard, so hosting is **not** a prerequisite). **Phase E2 BUILT ✅ (2026-07-28) — the layer is real, not theatre.** Alembic `0009`: ONE polymorphic `evidence_assets` (subject discriminator + a CHECK that fails closed) + `evidence_grades`; an R2-**or**-local storage service (localhost needs no bucket; signed key-scoped reads); the deterministic blocking tier; the evidence endpoints; **paste-first capture** on `DrillCard` **and `ConceptTrackPanel`**; and **both inherited screenshot debts CLOSED** — `missed_trade_screenshots` closed *by not building it*. **Its load-bearing call was answered by making `reps` DERIVED rather than guarded**, which removes the planner bypass structurally instead of relying on two enforcement points staying in sync; `legacy_reps` preserves pre-evidence claims so progress stays monotonic. 142 backend tests (114 → +28) · Playwright 45 (36 → +9) · `/api/analytics/*`+`/api/gate` byte-identical · all 7 invariants walked. **Flagged: two live bugs the rendered-surface check caught that a query-layer pass called green** — ky v2 consumes an error's response body (so every FastAPI `detail` was being swallowed, silently since 5e-1) and the local signed URL is app-relative (so every thumbnail rendered broken while the `src`-attribute assertion passed). Also retired the `downgrade base` footgun (`-x db_url=` + `scripts/scratch_migrate.py`). **Phase E3 BUILT ✅ (2026-08-02)** — Alembic `0010` (`rubrics`/`rubric_items`), `seed_rubrics.py` projecting **44 rubrics / 104 items** verbatim from the wiki's ✋/🛠 bullets with a programmatic no-drift proof, a **read-only** rubric API, the `self_check` grade, the self-check UI, and the targeted content pass (orphan refs **5 → 0**, drills **53 → 58**). **Decided: an unchecked rep still counts** (a grade may flag, never retract — progress must stay monotonic). Flagged (Rule #6): a phantom drill "Evolving" from a loose regex that also stole a bullet from aura D3-c; a version bump that could not write (ORM INSERTs before orphan DELETEs); the design's "4" aura Stage-0 drills is **five**; plus two defects found while verifying — **two N+1 request storms** (~116 requests per `/drills` load) and a **latent date-dependency in `planner.spec.ts`** that failed every Sunday. 160 backend tests; analytics+gate byte-identical; all 7 invariants walked. **OPEN, handed to E4:** a default-parallelism Playwright flake (`ECONNRESET`; green at `--workers=1`) and the unrun live browser walkthrough. **Phase E4 BUILT ✅ (2026-08-10)** — the AI-vision advisory second reader (closed-enum verdict schema, durable `pending`-row queue, cost telemetry, two-directional disagreement signal), with **two of the design's three mechanisms rejected on measurement** (Batch API; and the cached prefix, measured at 981 tokens against Sonnet 5's 1024-token minimum, so it cached nothing and reported no error). Cost **measured at $0.0167/grade ⇒ ~$8.37**, about half the design's estimate. **Phase E5 BUILT ✅ (2026-08-10) — and `stages.STAGE_UNWIRED` IS NOW EMPTY, meeting E1's acceptance test for the whole workstream.** The pre-commitment ledger (Alembic `0011` `predictions` + a freeze trigger) + the Goodhart-resistant calibration score, wiring `ict_course` **M6** — the row Phase 6 deliberately handed this workstream as debt — from a dead checkbox to evidence. **Decided: build the honest form of "cannot be back-dated"** — the app cannot prove the user did not peek at a replay, so it guarantees only that **the record cannot lie** (server-stamped `committed_at`, a DB-level freeze trigger, an ordering CHECK, a once-only reveal), and **`predictions` has NO `is_deleted` column** because a ratio whose denominator can shrink is gameable by deleting failures. **M6 grades commitment, not correctness** (pinned by a test where all 14 calls are wrong and the bar is still met). E4's open Playwright item closed at STEP 0 (50/50 × 3 clean runs). 213 backend tests · Playwright 57 · baseline byte-identical · all 7 invariants walked. Flagged: the tape drills' 13-rep parse artifact (fixed in the wiki); the `--reload` reloader dying again; and one contradiction only the rendered page could show. **Phase E6 BUILT ✅ (2026-08-10) — THE WORKSTREAM IS COMPLETE.** The honesty strip on `/gate` (five signals, computed per read, **stored nowhere**, gating nothing), the shipped streak/adherence re-derived from evidence and published **beside** the self-reported figures, and **declared rest days** (Alembic `0012`, trigger-enforced in-advance, no `is_deleted`, no PATCH/DELETE). **Decided: the strip is a separate resource, not a `GateOut` field** — so `services/gate.py` cannot read it, and `/api/gate` stays byte-identical to the E2 baseline; proven by tripping all five signals and requiring the verdict unchanged. **Decided: `study_preferences.blackout_dates` cannot host rest days** — it accepts past dates and records nothing about when a date was added, so honouring it would have built the retroactive streak freeze §6 rejects. **Every signal reports NOT-MEASURED rather than zero** when it had nothing to inspect, and every threshold it uses is printed. 263 backend tests · Playwright 68 (three consecutive clean runs) · baseline byte-identical · all 7 invariants walked · walkthrough 18/18, zero console errors. Flagged: the rendered strip printed "0 of 5 signals had something to measure" beneath five "not measured" rows — E5's defect class exactly, invisible at the query layer. **No boot prompt follows; see §Workstream retrospective** for the arc's lessons (make the property structural, not remembered; measure before building on a premise; read the rendered page) and for what remains unbuilt (`neurospect-learn` is deployed nowhere, R2 never exercised, AI cost measured at n=1, the 2026-08-07 Playwright flake never diagnosed).

#### Zeus OS (Product Suite)

- [[processes/distributed-workflow/active/zeus-memory]] — Zeus-Memory hybrid architecture research + implementation. Phase 1 design complete, implementation kickoff pending.

Pattern docs are in the ALDC wiki and consumed by absolute path:

- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\README.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\session-lifecycle.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\tracker-template.md`

### Operations

- [[processes/operations/neurospect-learn-deployment]] — **neurospect-learn deployment runbook** (created 2026-08-11, Phase B3). How to put the learning platform on Render (API + Postgres 16, `frankfurt`, **one worker**) + Cloudflare Pages (SPA, root dir `app`) + Cloudflare R2 (evidence blobs), and how to prove it works at the **rendered surface** rather than the API. Adapts — does not replay — the `neurospect-api` runbook, and tabulates **nine differences**, several of which would have been defects if the old page had been followed verbatim: Postgres `plan: starter` is now a **legacy** type Render refuses for new databases; `postgresMajorVersion` now defaults to **18** if omitted; and `-w 2` is unsafe here because `ai_grade_queue` serialises with a per-*process* lock and no DB-level claim. Records the load-bearing finding that **R2 is not optional on a deployed instance** — Render's filesystem is ephemeral, so the local storage backend would delete every captured chart on each deploy while the `evidence_assets` rows survived, silently voiding E2's claim that evidence is the only thing that mints a rep. Also documents that **the wiki is not part of the deployment** (only `scripts/` read `wiki_content_root`, so production is seeded from the laptop, keeping rubrics wiki-projected and read-only), the fail-closed Discord allowlist, a target-proving pre-flight for the seed step, the rollback table, and two known gaps carried into B4 (the **two-clock** rest-day/planner mismatch, and `WIKI_CONTENT_ROOT` resolving to a non-existent path on Render). **Status: prepared and locally proven, NOT yet provisioned** — every step in §1–§5 needs Paul's own Cloudflare/Render accounts.

---

## Tickets

_None yet._

---

## Sources

### Transcripts (Vol 1)
- `sources/neurospect/2026-04-18-vol1-class1-pt1-liquidity-and-inefficiency.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class1-pt2-liquidity-and-inefficiency.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class1-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class2-consolidation-model.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class2-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class3-expansion-and-retracement-model.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class3-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class4-notes.md` — PDF notes (no video)

### Transcripts (Vol 2)
- `sources/neurospect/2026-04-18-vol2-class1-power-of-three.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class1-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol2-class2-notes.md` — PDF notes (no video)
- `sources/neurospect/2026-04-18-vol2-class3-measuring-manipulation-deviations.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class3-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol2-class4-daily-bias-practice.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class4-notes.md` — PDF notes

### Transcripts (Vol 3)
- `sources/neurospect/2026-04-18-vol3-class2-market-structure-fractality.md` — video transcript
- `sources/neurospect/2026-04-18-vol3-class4-market-structure-deviations.md` — video transcript
- `sources/neurospect/2026-04-18-vol3-class5-model-2022-ote-csd.md` — video transcript

### Transcripts (Vol 4)
- `sources/neurospect/2026-04-18-vol4-class1-htf-ltf-orderflow.md` — video transcript
- `sources/neurospect/2026-04-18-vol4-class2-smt-divergence.md` — video transcript

### Stream Transcripts (2026-04-20)
- `sources/neurospect/2026-04-20-stream-0830-mid-mon-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-nfp-fri-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-uc-fomc-wed-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-uc-thu-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-1000-ism-pmi-1300-fed-speaks.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-1000-jolts-tue-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-fri-10-mid-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-no-news-mon-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-tapx-tape-reading-live-nq.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-thu-tape-reading-live-nq.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-tue-10-fed-chair-testifies.md` — stream transcript

### YouTube Transcripts (2026-04-22)
- `sources/neurospect/2026-04-22-youtube-1000-points-nq-2026-03-04.md` — YouTube weekly review (+1000 pts NQ, March 4 2026)
- `sources/neurospect/2026-04-22-youtube-first-week-march-2026-03-07.md` — YouTube weekly review (first week of March, March 7 2026)

### Aura Playlist — dOoMeR (2026-07-16)
30 auto-caption transcripts in `sources/neurospect/aura/` (`aura-01`…`aura-30`). Second mentor
corpus. Manifest + per-video titles in [[processes/distributed-workflow/active/aura-ingest]].
Sections: psychology (1–5), technical framework (6–17), trade/market reviews (18–30).

---

## Vault

Credentials live in `vault/credentials.md` (gitignored — see `.gitignore:vault/`). Never commit values here in `index.md` or any other tracked file. See [[CLAUDE]] § *Rules* #2.

---

## Daily

Handwritten notes inbox. Copy `daily/_template.md` as `daily/YYYY-MM-DD.md`.

- [[daily/_template]] — note format reference.
- [[daily/2026-04-18]] — bootstrap day.
- [[daily/2026-04-20]] — transcript ingest session checkpoint.
- [[daily/2026-04-22]] — stream + YouTube ingest session checkpoint.
- [[daily/2026-04-24]] — Phase 4 (AI Coach frontend) implemented + verified. Deployment tracker created.
