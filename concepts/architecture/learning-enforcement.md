---
tags: [architecture, learning-enforcement, evidence, grading, rubrics, self-check, anti-cheat, gamification, mastery, neurospect, phase-e1, phase-e2, phase-e3]
aliases: [Learning Enforcement Architecture, Evidence Layer, Drill Grading, Verified Reps, Anti-Cheat Design, Rubric Layer, Self-Check]
sources:
  - processes/distributed-workflow/active/learning-enforcement.md
  - concepts/architecture/learning-platform.md
  - concepts/mastery/README.md
  - concepts/mastery/aura/exercises.md
  - concepts/mastery/ict-course/exercises.md
  - concepts/aura/journaling-system.md
  - concepts/architecture/phase2-project-structure.md
  - "MeasureBench — Do Vision-Language Models Measure Up? Benchmarking Visual Measurement Reading (arXiv 2510.26865)"
  - "Deci, Koestner & Ryan (1999) — A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation (128 studies)"
created: 2026-07-28
updated: 2026-08-02
---

# Learning Enforcement — Architecture (E1 design · E2 + E3 as-built)

Canonical design doc for the layer that makes progress in `neurospect-learn` **impossible to fake**: a rep
counts only when **evidence of the work** exists, that evidence is **graded**, and the loop is **gamified**
without rewarding activity over mastery. It extends the shipped platform described in
[[concepts/architecture/learning-platform]] and is sequenced by
[[processes/distributed-workflow/active/learning-enforcement]].

> **Status: E2 BUILT (2026-07-28) · E3 BUILT (2026-08-02); E4–E6 are still design.** The evidence layer, the
> deterministic tier, the derived `reps`, the rubric layer and the self-check **ship** in `neurospect-learn` at
> Alembic `0010` — per [[CLAUDE]] §Architecture Doc Integrity the **code is ground truth** for everything E2 and
> E3 cover, and §E2 as-built / §E3 as-built below record every divergence from the design in this doc. §§1–5 and
> §7–8 now describe *what is running*; **§2 tier 3 (AI vision), §9 (pre-commitment) and §6's mechanics remain
> unbuilt design for E4–E6.**

> **No-drift.** This doc states *structure and decisions*. It does not restate the mastery ladder, the
> confidence scale, the Readiness-to-Live Gate, any drill definition, or any rubric text — it **links** them,
> and the rubric layer is a **parsed projection** of the wiki rather than a second copy.

## The problem in one line

Every enforcement check the platform ships today ultimately trusts a **self-reported `reps` integer** and a
**self-rated confidence**. `PATCH /api/progress` gates ladder advance on `reps ≥ target`, `services/stages.py`
grades stage exit bars on the same integer, and `services/gate.py` computes live-readiness from it. `reps` is
a number the user increments. That is the single weakest link in the chain, and evidence-backed grading is
what replaces it.

Three consumers have been waiting on the same unbuilt primitive, deliberately: **drill evidence**, the
**journal's deferred screenshots** (5c), and **`missed_trade_screenshots`** (omitted from Alembic `0008` on
purpose). One evidence layer serves all three. `ict_course` **M6** (`stages.STAGE_UNWIRED`) is the acceptance
test — a correct design makes that map empty.

## Decisions (Paul, 2026-07-28)

| # | Fork | Decision |
|---|---|---|
| 1 | Grading mechanism | **Tiered hybrid** — deterministic blocks, self-check rubric is the rep's bar, AI vision is a non-blocking second reader |
| 2 | Grading lifecycle | **Provisional, graded asynchronously** — a grade may flag, never retract |
| 3 | Anti-cheat bite | **Block the certain, surface the rest** |
| 4 | Deploy dependency | **Localhost + clipboard paste** — hosting is not a prerequisite |

## Why tiered — the evidence that decided it

**MeasureBench** (arXiv 2510.26865) benchmarks frontier vision-language models reading precise values off
analog scales and linear gauges: **Gemini 2.5 Pro 30.3%**, **Qwen3-VL-235B 23.7%**, **GPT-5 19.8%** on real
images. Unit recognition exceeds **90%** while numeric value extraction sits near **30%**, and extended
thinking yields *negligible* gains — the authors conclude the limitation is **perceptual, not computational**,
and not solved by model scale.

Reading "which price level is this line drawn at" off a chart axis is that exact task. So a vision model must
**not** arbitrate *"is this swing marked at the right price."* It is reliable at coarse presence/structure
questions — *is this an annotated price chart; are range boundaries drawn; was a second SMT pass done* — which
is precisely the advisory tier's job and nothing more.

**Cost is not a constraint.** A 1920×1080 TradingView capture is ~2,765 image tokens (the high-resolution
tier caps at 4,784). With the rubric held in a `cache_control` prefix (cache reads ≈0.1×) and a ~500-token
structured verdict, Claude Sonnet 5 at $3/$15 per MTok costs **~$0.02–0.04 per grade** — **~$15–25 for the
entire ~500-evidence-unit curriculum**, halved again by the Batch API. The binding constraints are **latency**
(why grading is asynchronous) and **false negatives** (why it is advisory). This corrects the tracker's
original framing; see §Contradiction flags.

## What already enforces the process — do NOT redesign

This layer builds **on** the shipped enforcement, never around it: the Gate is non-overridable and computed
per read; ladder advance is already gated; frontier/watch-only concepts are capped at Can-mark and are never
gate-eligible; skips are logged and hurt adherence; backtest and live are never conflated. All canonical in
[[concepts/architecture/learning-platform]] §§3–4 + §5g/§6 as-built.

## 1. The evidence model

The unit is an **evidence asset** attached to a subject, carrying `reps_claimed` (default 1). It is
deliberately **not** one image per rep: `services/rep_targets.py` already distinguishes
`reps`/`days`/`sessions`/`qualitative`/`habit`, and a `"1 week"` habit target has no rep to photograph.

| Kind | What it is | Drills it serves |
|---|---|---|
| `chart_markup` | A marked-up chart capture | aura D1-a/b/c, D2-b/c/d; ict D1–D5 |
| `written_artifact` | A written deliverable (routine, identity statements, circuit-breakers, contracts) | aura D0-a…e; ict D0-a…e |
| `computation` | A computed number or table | aura D2-a (Pearson), D3-c (R / break-even / expectancy) |
| `prediction` | A call **committed before the outcome is revealed** | D1-b forward-bar sim, D2-c NY-open, D4-a, D5-a, T-01…T-14 |
| `tape_read` | A narrated live/delayed session read | aura D5-a, ict T-14 |

`days`/`sessions` targets take **one asset per day** (matching the scheduler's existing one-session-per-day
treatment of longitudinal drills). `qualitative`/`habit` targets take a single asset and gate on ladder +
confidence, exactly as `rep_targets.meets()` already does.

## 2. Grading — three tiers, each doing only what it is reliable at

1. **Deterministic — BLOCKS.** Content-type + magic-byte sniff, size bounds, SHA-256 exact-duplicate and
   perceptual-hash near-duplicate. Zero false positives, no LLM, works offline.
2. **Self-check rubric — the rep's own bar.** The user answers the drill's own wiki bullets as checkable
   items (see §3). This is what "graded" means for the rep.
3. **AI vision — advisory second reader.** Claude Sonnet 5 with a structured-output verdict schema, the
   rubric in a cached system prefix, run through the Batch API. Emits an advisory `score`, per-item findings,
   and flags. **Never blocks, never retracts.**

**The advisory `score` never writes `confidence` or `ladder_stage`.** Those stay user-owned, so the shipped
ladder-advance gate in `routers/learning.py` is unchanged.

## 3. Rubric provenance — a projection, not new content

Each drill's ✋/🛠 bullets in [[concepts/mastery/aura/exercises]] and
[[concepts/mastery/ict-course/exercises]] *already are* checkable assertions — "circle **≥50 swing points** —
highs/lows only, nothing else"; "re-anchor each range's extremes onto **SMT-qualified** swings". A new
`scripts/seed_rubrics.py` parses each drill's bullet list into **one rubric item per bullet**, tagged
hand/tool by the glyph — the same projection `scripts/seed_drills.py` already performs on the map tables.

**No rubric text is authored in the app.** The wiki stays canonical, a re-seed propagates edits, and there is
no second copy to drift. Rubrics carry a `version` so a historical grade records which bar it was judged
against.

## 4. Grading lifecycle

Upload → deterministic tier → **rep counts (provisional)** → asynchronous grade attaches. A failing grade
**flags**; it does not retract, because `stages.py` and `gate.py` read `reps`: retraction would make progress
**non-monotonic** — a met stage exit bar could un-meet and a Gate verdict could flip backwards with no user
action. Offline or API-down leaves rows `ungraded`, which reads honestly as such and is surfaced (§5).

## 5. Anti-cheat

**Blocked** (certain, zero-false-positive): duplicate/recycled image, non-image upload.

**Surfaced and recorded** — computed per read, never stored, following the `stages.py`/`gate.py` convention:
implausible rep pacing, back-dated `captured_at`, bulk marking, ungraded backlog, flagged-grade count. These
render as an honesty strip on `/gate` beside the attestations, in the same **"corroboration, not threshold"**
idiom §5g established: shown in the face of the record, gating nothing on an invented rule.

**No appeal path is required.** Nothing is refused on judgement, so there is nothing to appeal — which means
the Gate's deliberate absence of an override is never reopened.

Rationale is the workstream's sharpened north star: the adversary is **self-deception, not an attacker**. A
wrongly refused honest rep fails that north star exactly as hard as a fakeable one.

## 6. Gamification — informational, not tangible

**Deci, Koestner & Ryan (1999)**, a meta-analysis of 128 experiments, find tangible engagement-, completion-
and performance-contingent rewards **undermine** free-choice intrinsic motivation (d ≈ **−0.34**), while
**verbal praise and positive informational feedback do not**. That is decisive here:

- **No XP, no badges, no points on rep count.** That is precisely the *rewards activity over mastery* failure
  mode, and it would actively undermine the Gate.
- **Informational feedback** — the grade's specific per-item findings are the reward.
- **A calibration score** on `prediction` evidence: your pre-committed call versus the revealed outcome. This
  is the one genuinely new mechanic, and it is **Goodhart-resistant** — more reps cannot inflate accuracy.
- **The already-shipped surfaces become evidence-backed** rather than self-reported: streak, adherence %,
  days-behind, pace (`routers/planner.py::_adherence`). No new currency, so nothing double-counts.
- **Declared rest days** in `study_preferences` — declared *in advance*, unlike a retroactive streak freeze,
  which keeps the streak honest.

Supporting evidence already in this corpus, not imported: [[concepts/aura/journaling-system]] records
dOoMeR's survey finding that **50% of respondents don't journal consistently**, and frames all three stated
reasons as **instruction problems, not motivation problems**. That is the in-corpus case for friction-first
design over reward-first gamification — and it is why §10 puts capture friction ahead of hosting.

## 7. Data model — ONE evidence layer (Alembic `0009`)

**`evidence_assets`** — user-scoped, soft-deleted. A subject discriminator (`subject_type`) plus exactly one
of `subject_drill_ref` (TEXT soft ref, matching the `drill_progress.drill_ref` convention), `concept_id`,
`journal_entry_id`, `missed_trade_id`, enforced by a CHECK that **fails closed**. Plus `kind`, `storage_key`,
`content_type`, `original_filename`, `byte_size`, `sha256`, `perceptual_hash`, `captured_at` (user-asserted),
`reps_claimed`, `notes`.

**`evidence_grades`** — child, **one row per grading pass** so a re-grade is additive rather than destructive:
`grader` (`deterministic|self_check|ai_vision`), `state` (`ungraded|pending|passed|flagged|failed`), advisory
`score`, `rubric_slug` + `rubric_version`, `findings` JSONB, and model/token telemetry for cost tracking.

This is deliberately **not** the per-owner child-table shape `neurospect-api` used
(`trade_screenshots` + `missed_trade_screenshots`, see [[concepts/architecture/trade-schema]] §Missed Trades)
— that duplication is the thing this layer exists to avoid. Conventions reused exactly: UUID PK ·
`TIMESTAMPTZ` · `update_updated_at()` trigger · user-scoped · soft-delete + partial unique
`WHERE NOT is_deleted` · raw-SQL `op.execute` mirroring `0004`–`0008`.

## 8. Storage

Lift `neurospect-api/app/services/r2.py` — a proven boto3 S3-compatible client (`storage_key`,
`upload_bytes`, `delete`, `presign`) with a module-level `r2 is None` sentinel and graceful 503 — and add a
**local-filesystem backend so localhost needs no bucket at all**. `neurospect-learn` has no storage layer
today (`boto3` was dropped in the 5b lift); `python-multipart` **is** already a dependency, so `UploadFile`
needs nothing new. New deps: `boto3`, `Pillow` + `imagehash`, `anthropic`.

Key pattern: `{user_id}/evidence/{subject_type}/{subject}/{uuid4}.{ext}` — extending the convention canonical
in [[concepts/architecture/phase2-project-structure]] §R2 Client (referenced, not restated). Env vars reuse
the **existing names verbatim** — `R2_ENDPOINT_URL`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`
— canonical in `neurospect-learn/api/.env.example`.

**Privacy + retention:** chart captures contain no PII and no account numbers; they are user-scoped and
presigned-read only. Retention is indefinite by default (the evidence *is* the accountability record) with
soft-delete for user-initiated removal.

## 9. The M6 case — what makes a tape study count

`ict_course` M6's bar is T-01…T-13 ("study the mentor's read, then replicate blind on a comparable session")
plus T-14 (a live blind read). Their honest form **requires commitment before the reveal**, so evidence is a
`prediction` asset — bias · DOL · model · target — timestamped **before** the replay steps forward, plus the
marked chart and a self-scored comparison against the mentor's write-up.

`stages.py` then grades M6 on 14 committed-before-outcome prediction rows on `ict-course T-01…T-14`, and
**`STAGE_UNWIRED` becomes empty** — E1's acceptance test. Pre-commitment is the strongest anti-cheat
primitive in the whole design and it is essentially free: faking it requires fabricating a prediction that
will then be scored against reality, which is self-defeating.

*(External precedent, same shape: Tonara verified music practice by comparing a student recording against a
teacher's reference performance — verification against ground truth, not against an abstract rubric. The
Neurospect analogue already exists in the corpus: aura **D4-a**'s nine worked reviews on exact replay dates,
and **T-12/T-13**'s precisely dated sessions.)*

## 10. Deploy — not a dependency

Every drill's stated tooling in both exercise libraries is **TradingView bar-replay on a desktop**. So the
capture path is **paste-from-clipboard first** — `Ctrl+V` from a TradingView snapshot straight into the drill
card — plus file-drop. That works on localhost today, and because the storage layer is backend-swappable,
hosting stays a separate, already-runbooked workstream rather than a blocking prerequisite. See
§Contradiction flags for what the tracker got wrong here.

## Implementation split (E2 → E6)

Each phase is a boot-promptable unit; sequenced in
[[processes/distributed-workflow/active/learning-enforcement]].

- **E2 — Evidence layer + capture.** ✅ **BUILT 2026-07-28** — Alembic `0009`; both tables; storage service
  (R2 + local); upload/list/delete endpoints; paste-first capture on `DrillCard` **and `ConceptTrackPanel`**;
  the deterministic tier; **`reps` became DERIVED rather than merely guarded** (see §E2 as-built). Closed both
  inherited debts: the journal's deferred screenshots and `missed_trade_screenshots` attach to the same layer.
- **E3 — Rubrics + self-check.** ✅ **BUILT 2026-08-02** — Alembic `0010` (`rubrics` + `rubric_items`);
  `seed_rubrics.py` projecting 44 rubrics / 104 items from the two exercise libraries with a programmatic
  no-drift proof; the read-only rubric API; the `self_check` grade; the self-check UI; and the targeted wiki
  content pass (all seven named drills fixed, orphan refs 5 → 0). **An unchecked rep still counts** — see §E3
  as-built.
- **E4 — AI vision second reader.** Sonnet 5 + structured outputs + cached rubric prefix + Batch API;
  advisory grades, flags, cost telemetry.
- **E5 — Pre-commitment + calibration.** Prediction capture before reveal; calibration score; wires M6 and
  empties `STAGE_UNWIRED`.
- **E6 — Gamification + honesty surfaces.** Computed honesty signals on `/gate`; evidence-backed streak /
  adherence; declared rest days.

**Why the content pass does not lead** (the tracker's hypothesis, partially overturned): because rubrics
project from bullets that already exist, most drills are gradable **as written**, so E2 is not blocked on
content. Only the ungradable subset needs editing, and that is E3's own scope.

### Drills ungradable or ambiguous as written (✅ ALL FIXED IN E3 — see §E3 as-built for before→after)

- aura **D1-c** — rep target `(reuses 50 ranges)` parses to a 50-rep floor via the parser's largest-number
  rule, though the intent is "no separate target".
- aura **D2-d** `simple-first`, **D2-a** `1 triad + spot-check`, **D3-a** `per practice entry`, **D3-c**
  `per backtest batch` — no countable floor, so evidence-backed grading has no target to compare against.
- ict **D3-d** — advances `Learned→applied`, which names no observable artifact.
- The **~~4~~ 5 aura Stage-0 drills the map table omits** — already reported as orphan refs by `seed_drills.py`; a
  faithful wiki asymmetry, but they cannot carry evidence until the map lists them.
  **Corrected at E3 (Rule #6): there are FIVE, not four** — `seed_drills.py` reports
  `['aura D0-a', 'aura D0-b', 'aura D0-c', 'aura D0-d', 'aura D0-e']`. E1 undercounted by one.

## E2 as-built (2026-07-28) — code is now ground truth

Shipped in `neurospect-learn`: Alembic **`0009`**, `models/evidence.py`, `services/storage.py`,
`services/evidence_checks.py`, `routers/evidence.py`, `schemas/evidence.py`, the derived-`reps` rewiring of
`routers/{learning,planner}.py`, and the frontend `lib/evidence.ts` + `components/evidence/evidence-capture.tsx`
wired into `DrillCard`, `ConceptTrackPanel`, `/journal/:id` and `/journal/missed/:id`. Verification evidence +
the re-run recipe: `neurospect-learn/api/docs/evidence/e2-learning-enforcement.md`.

### THE LOAD-BEARING CALL — `reps` is DERIVED, so the bypass cannot exist

The phase's one real decision was how `reps` becomes evidence-backed **without leaving the planner's
mark-done path as a hole**. `drill_progress.reps` / `concept_progress.reps` were written by **two** modules:
`routers/learning.py` (`PATCH /api/drills`, `PATCH /api/progress`) *and* `routers/planner.py`
(`PATCH /api/plan/items/{id}` on mark-done). Guarding only the learning router would have made marking a plan
item done a rep-minting bypass — and the whole layer theatre.

**Chosen: make `reps` derived, not guarded.** `0009` **renames** `concept_progress.reps` and
`drill_progress.reps` to `legacy_reps`; the API's `reps` is computed as
`legacy_reps + Σ evidence_assets.reps_claimed` by a shared `learning.load_evidence_reps` loader used by every
progress / drill / stage / planner read. `reps` is removed from `ProgressPatch` / `DrillPatch`
(`extra="forbid"` plus a validator so the 422 *names* `POST /api/evidence` rather than saying "extra inputs
are not permitted"), and `planner._feed_concept` / `_feed_drill` no longer increment anything.

This is the **same structural non-overridability the Gate has**: 5g's rationale was "there is no `cleared`
column and no endpoint that sets one", and the analogue is *there is no writable `reps`, so there is nothing
to bypass*. A guard has to be remembered at every new write path; a derivation cannot be forgotten.

Consequences accepted deliberately:

- **The planner still records the practice** — `last_practiced` and the ✋/🛠 variant marks still move on
  mark-done (spaced review schedules off `last_practiced`, and a review *is* practice). What a mark no longer
  does is *count as proof*. `plan_items.done_qty` still records how much was worked.
- **`legacy_reps` is preserved, not wiped.** Renaming rather than dropping means no already-met stage
  un-meets — the same monotonicity argument that made a failing grade flag rather than retract (§4). It also
  gives the declared-vs-derived divergence signal for free: the API returns `reps` / `reps_evidenced` /
  `reps_legacy`, and `RepCounter` renders "12 / 50 reps · 5 evidenced · 7 pre-evidence". E6 can read
  `reps_legacy > 0` as an honesty signal without new plumbing.
- **The concept panel gained capture too.** Only drill capture was named in the plan, but `PATCH /api/progress`
  gates ladder advance on *concept* reps — so without a concept-level affordance every concept with a numeric
  rep target would have become unreachable. That would have been the catastrophic false negative.

### Divergences from §§7–8 of the design

- **Local storage is a real backend, not a degradation.** `neurospect-api`'s `r2 is None → 503` sentinel was
  *not* copied: E2 has `R2Backend` and `LocalBackend` behind one interface, chosen by config, and localhost
  needs no bucket. `LocalBackend.presign()` mints a short-lived **JWT bound to one storage key**, served by an
  unauthenticated-but-signed `GET /api/evidence/file?token=` — so the frontend renders evidence with a plain
  `<img src>` identically against either backend.
- **`anthropic` was NOT added** (design §8 lists it) — it belongs to E4, and E2 must not grow an LLM dependency.
  Added: `boto3`, `Pillow`, `imagehash`.
- **Perceptual-hash thresholds are measured, not asserted.** Block at Hamming ≤ **4**, flag 5–**7**. Measured on
  chart captures: identical / re-encoded / rescaled = 0, a 0.5% crop = 2, a 1% crop = 6, **the same chart with
  one new marking drawn on it = 8–10**, a 2% crop = 14, a different chart = 26–34. The decisive number is the
  middle one: re-marking one chart is a *real* extra rep ("≥50 ranges" on one instrument), and it sits inside
  the range a 2% crop occupies — so past distance ~7 the signal genuinely cannot separate recycling from honest
  work, and the design claims nothing there rather than refusing real reps.
- **A near-duplicate blocks; a *similar* upload is flagged.** §5 listed "duplicate image" as a single blocked
  check; in practice it splits: exact `sha256` and phash ≤ 4 are refused (409, naming the asset they duplicate),
  while 5–7 is accepted with a `flagged` deterministic grade carrying the distance — "block the certain, surface
  the rest", applied inside one check.
- **Every asset gets a `deterministic` grade row on arrival**, so grading history exists from the moment of
  capture and E3/E4 append rather than backfill.
- **Rejections are typed.** `{code, message, duplicate_of, distance}` with 415 / 413 / 409 / 422 status codes,
  rendered inline on the capture surface — a silent refusal is the failure mode this workstream exists to avoid.
- **`reps_claimed` is capped at 100** per asset (DB CHECK + form bound). One capture may honestly cover ten
  marked ranges; it may not cover a whole 50-rep target.
- **Soft delete keeps the object.** Deleting an asset removes it from the ledger (so its reps go with it) but
  the blob stays — retention is indefinite by design. It frees the `sha256` for a re-upload, which restores
  exactly the one rep it carried, so this is not a way to inflate a count.
- **The `downgrade base` footgun is retired.** `alembic/env.py` now honours `-x db_url=…`, and
  `scripts/scratch_migrate.py` drives reversibility tests at a throwaway DB it creates and drops. An exported
  `DATABASE_URL` never redirected Alembic (the `.env` also sets `DATABASE_URL_SYNC`, which wins), which is what
  wiped the seed twice.

### Two bugs the rendered-surface check caught (a query-layer pass would have missed both)

1. **ky v2 consumes the response body** to populate `error.data`, so `error.response.json()` throws. Every
   FastAPI `detail` was being replaced by ky's generic "Request failed with status code 4xx" — including,
   silently since **5e-1**, the ladder-advance gate's own reason. Fixed with a shared `apiErrorDetail()` in
   `lib/api.ts`; `lib/learning.ts` was on the same broken path and now uses it.
2. **The local signed URL is app-relative**, so `<img src>` resolved it against the SPA origin (`:5173`) and
   every thumbnail rendered broken — while the Playwright assertion passed, because it checked the `src`
   attribute rather than whether the image loaded. Fixed with `evidenceSrc()`; the spec now polls
   `naturalWidth > 0`.

### Verified

`0009` up/down/up/base reversible on a scratch DB, working-DB seeds intact (74/23/53/67); the subject CHECK
rejects zero-subject, two-subject and discriminator-mismatched rows **at the database**; exact and
near-duplicate uploads refused with reasons; **the bypass test asserts all three rep-writing endpoints fail to
mint a rep**; `/api/analytics/*` + `/api/gate` **byte-identical** to the pre-phase baseline (and pinned as a
durable pytest); per-user isolation; no-token 403; the local backend works with no R2 config. **142 backend
tests** (114 → +28), `tsc -b` + `vite build` clean, **Playwright 45** (36 → +9) stable over three consecutive
full runs, and a live browser walkthrough of every changed surface with **no console errors**.

## E3 as-built (2026-08-02) — code is now ground truth

Shipped in `neurospect-learn`: Alembic **`0010`** (`rubrics` + `rubric_items` + the `rubric_variant` enum),
`models/rubric.py`, `scripts/seed_rubrics.py`, `routers/rubrics.py`, `schemas/rubric.py`, the `self_check` grade
write in `routers/evidence.py`, and the frontend `lib/rubrics.ts` + `components/evidence/self-check.tsx` wired
into `EvidenceCapture` (so it reaches `DrillCard` and `ConceptTrackPanel`). Plus the targeted wiki content pass on
both `exercises.md` libraries. **44 rubrics / 104 items**, seeds now **74/23/58/67**.

### THE DECISION THIS PHASE OWED: an unchecked rep STILL COUNTS

**A self-check can never un-count a rep.** `reps` is derived from `evidence_assets.reps_claimed`, and
`services/stages.py` + `services/gate.py` read `reps` — so deducting on a missing or partial check would make
progress **non-monotonic**: a met stage exit bar could un-meet and a Gate verdict could flip backwards with no
user action. That is exactly what §4 forbids ("a grade may flag, never retract") and what invariant 5 means:
`reps` gets harder to **create**, not revocable after the fact.

So "ungraded" is **surfaced, never deducted** — `EvidenceCapture` renders "N awaiting your check" and each
unchecked capture says *"not checked yet — the reps still count"*. A partial check records `flagged` plus the
specific unticked items (informational feedback, §6) and **never `failed`**. Pinned by
`tests/test_rubrics.py::test_a_self_check_never_moves_a_rep`, which attacks the adversarial case — an **empty**
self-check on a 4-rep capture — and asserts the count is unchanged, then that a full check does not inflate it
either. The *aggregate* honesty strip over that backlog remains **E6's**; E3 changed no rep count, no stage bar
and no Gate verdict.

### The parser: one item per bullet, split ONLY on top-level semicolons

§3 said "one rubric item per bullet". Measurement refined it in two ways, and the reasoning is the phase's real
content:

- **Compound bullets split on `;`.** Several bullets carry multiple deliverables joined by semicolons — aura
  **D0-a** is four in one bullet. One checkbox for four deliverables forces a **dishonest tick** when three are
  done, which is the self-deception this workstream exists to prevent.
- **Sentence splitting was tried and REJECTED on evidence.** This corpus writes "vs." mid-sentence followed by a
  capital — *"**which KZ sets the HOD vs. LOD**"*, *"**STL (no gap) vs. ITL (…)**"*, *"Tag **LRLR vs. HRLR**"*,
  *"tag real vs. **fake retracement**"* — and every sentence heuristic mangled all four into garbage fragments.
  **A parser that can mangle wiki text is a parser that authors wiki text.** A top-level semicolon is
  unambiguous; a sentence boundary is not. Pinned by `test_sentence_boundaries_are_not_clause_boundaries`.
- The split is **depth-aware** (a `;` inside `()`, `[]` or `""` is not a boundary) because the corpus has those
  too: *"(overlapping gaps; liquidity-left …)"*, *'("inside a [bull/bear] 4H FVG; target [level]")'*.
- Only **structural markers** are stripped, each edge-anchored so what remains is a contiguous substring: the
  leading `*(source)*:` marker, a trailing `→ [[wikilink]]` trailer (required to be `→` **then** `[[`, since the
  corpus also uses a bare mid-sentence `→`), a trailing `[R8]`-style rule ref (captured into `rule_refs`), and a
  `**Advances:**` tail (`drills.advances_to` already carries it).

**The no-drift proof is programmatic, not asserted.** `verify_no_drift()` checks that **every** item's text is a
contiguous substring of a whitespace-normalised wiki bullet, over the whole seed; it runs inside every seed run
*and* as `test_no_rubric_text_is_authored`. An item that is not verbatim wiki text is a **bug**, not a variation.

### Divergences from the design

- **`version` excludes provenance from its hash.** `content_hash` covers only what the user ticks
  (variant + text + rule refs). `source_path` / `source_ref` update in place **without** a bump, so a cosmetic
  marker edit cannot imply the bar moved. Consequence worth knowing: E3's D1-c / D2-a / D2-d / D3-a / D3-c
  *map-table* fixes changed rep targets **without** bumping any rubric version; only the two **bullet** edits
  (D2-d, D3-a) bumped, to v2.
- **`item_key` is a positional TEXT key** (`aura-d1-a#3`), not the row UUID, because a re-seed replaces
  `rubric_items` and a stored grade must stay legible afterwards — which is also why `findings` stores the item
  **text** alongside the key.
- **E3 added no grading table.** The self-check is an `evidence_grades` row, so the deterministic row E2 writes on
  arrival survives untouched and grading stays append-only.
- **The self-check write lives in `routers/evidence.py`, not `routers/rubrics.py`** — it appends a grade rather
  than touching a rubric, and one router owning all `/evidence` paths is the cleaner split.
- **A concept's bar is the union of its drills' bars.** 10 of the 74 concepts resolve 2–3 rubrics, so `SelfCheck`
  offers a picker; a grade records exactly one `rubric_slug`.
- **`either` is a first-class variant, not a fallback.** 40 of 104 items come from bullets with **no** glyph (the
  Stage-0 written artifacts, aura D2-a's Pearson computation, D3-a/D3-c's procedures). Recording the wiki's
  silence beats inventing a ✋/🛠 claim it never made.

### Two bugs the DB and the browser caught (neither was visible at the query layer)

1. **A phantom drill named "Evolving".** The inline-drill regex was loose enough that the bolded lead-in
   `**Evolving-R reps:**` inside aura **D3-c** matched as a drill definition — inventing a rubric AND **stealing
   that bullet from D3-c**. Fixed by anchoring the code pattern to the four shapes the corpus actually uses
   (`D4-a` · `T-01` · `J-a` · `S7`), the same shapes `seed_drills._expand()` emits.
2. **The version bump could not write.** Replacing a rubric's items via the ORM collection emitted this mapper's
   INSERTs **before** its orphan DELETEs, so the positional `item_key` (`…#1`) collided on
   `ux_rubric_items_key` and every re-seed containing a changed bullet died with an `IntegrityError`. Fixed with an
   explicit `clear()` + `flush()` before re-adding, and pinned by
   `test_reseed_after_a_wiki_edit_bumps_the_version` — **verified to fail on exactly that constraint with the fix
   reverted.**

### The content pass — before → after, with the parse as evidence

The wiki is canonical, so each bar was fixed **in the wiki and re-seeded**, never patched around in code. Parses
via `services/rep_targets.py`:

| Drill | Before | After |
|---|---|---|
| aura **D1-c** | `(reuses 50 ranges)` → **reps=50 floor** (bogus — the heading says "reuses the ≥50 range set") | `(no separate target — reuses D1-b's range set)` → **qualitative, no floor** |
| aura **D2-a** | `1 triad + spot-check` → **reps=1** (understates "1 full triad + 1 spot-check") | `2 *(1 full triad + 1 spot-check)*` → **reps=2** |
| aura **D2-d** | `simple-first` → **qualitative, no floor** | `≥10 *(proposed)*` → **reps=10**; bullet split → **1 → 2 items, v2** |
| aura **D3-a** | `per practice entry` → **no floor**; advances `Learned→applied` | `≥20 practice entries *(proposed)*` → **reps=20**; advances **`Learned→Backtested`**; bullet split → **1 → 3 items, v2** |
| aura **D3-c** | `per backtest batch` → **no floor**; advances `Learned→applied` | `≥3 batches *(proposed)*` → **reps=3**; advances **`Learned→Backtested`** |
| ict **D3-d** | advances `Learned→applied` — **not a ladder stage**, so it named no observable artifact | advances **`Can-mark`**, matching its Stage-3 siblings and the README's real vocabulary |
| aura **D0-a…e** | **absent from the map table** — `seed_drills.py` had reported them as orphan refs since 5e-1 | one row `\| D0-a…e \| discipline / journal \| (habit) \| behavioural \|`, mirroring the ict library |

Result: **`seed_drills.py` orphan refs 5 → 0**, drills **53 → 58**, and rubrics whose drill the map omits **8 → 3**.
Every proposed number is flagged *(proposed)*, which is the convention the aura page's own preamble already states.
Two edits went slightly beyond a map-table cell and are called out honestly: the **D2-d / D3-a bullet punctuation**
(sentence-final periods → semicolons, plus the case change that follows, so a compound bar becomes tickable) and
the **aura D3-a / D3-c `advances_to`** values, fixed alongside ict D3-d because they carried the identical
non-ladder value — `advances_to` is **display-only** (model → schema → `DrillCard`), so nothing gates on it.

### Verified

`0010` up/down/up/base reversible on a **scratch** DB, including a tightened single-step proof that
`downgrade 0009` removes exactly E3's objects and **leaves E2's evidence layer untouched**; working-DB seeds intact
across the migration (74/23/53/67 → 58 only from the deliberate content fix). The **no-drift proof passes over all
104 items**. Re-seeding twice is a genuine no-op (0 bumped / 44 unchanged); a wiki bullet edit bumps **only** the
edited rubric (`aura-d2-d` v2, `aura-d3-a` v2, `aura-d1-a` still v1). A self-check attaches as an **additional**
`evidence_grades` row with the deterministic row surviving; refusals name the offending item key / slug / drill.
**`reps` is untouched in both directions** — E2's bypass test still passes and the empty-self-check test proves no
deduction. `/api/analytics/*` + `/api/gate` **byte-identical** to the STEP-0 baseline (same sha256 `27ff7157…`).
**160 backend tests** (142 → +18), `tsc -b` + `vite build` clean, and the new `self-check.spec.ts` (5 tests) plus
`planner.spec.ts` green.

**One item is NOT closed and is handed to E4:** the **full** Playwright suite (50) is green at `--workers=1` and was
green once at default parallelism immediately after the N+1 fixes, but subsequent default-parallelism runs went
flaky (2–3 rotating failures, wall-clock drifting 31s → 1.5m) with `ECONNRESET` against the dev API. The two
genuine defects found on the way — the N+1 request storms and a **latent date-dependency in `planner.spec.ts`**
(the availability form ships `sun_minutes: 0`, so a plan for a Sunday is correctly empty and that spec failed every
Sunday, fixed by giving *today* explicit capacity) — are both fixed. What remains is unproven and must not be
called green: see the tracker's E4 boot prompt for the first diagnostic step.

## Invariants this layer must preserve (checked at every phase)

1. The Gate stays **non-overridable and computed per read** — no `cleared` column, and evidence adds no write
   path to a verdict.
2. Frontier / `watch_only` concepts stay **never gate-eligible**, and remain capped at Can-mark.
3. Skips stay **logged**; missed work stays re-queued, never silently dropped.
4. Backtest and live stay **unconflated**; missed trades still never enter expectancy or the Gate.
5. **`reps` gets strictly harder to satisfy, never easier** — it gains an evidence precondition and loses
   nothing.
6. `auto_met` / `locked` stay **concept-based**, so the lock chain is unchanged.
7. The advisory `score` never writes `confidence` or `ladder_stage`.

### Walked at E2 (2026-07-28) — each one, explicitly

1. **Gate non-overridable ✔** — no `cleared` column, request field or endpoint was added; `services/gate.py`
   is untouched and does not read `reps` at all. `/api/gate` is byte-identical to the pre-phase baseline.
2. **Frontier never gate-eligible ✔** — `watch_only` handling is untouched, and the `PATCH /api/progress`
   Can-mark cap still fires *before* the rep check. Evidence on a frontier concept cannot lift its ladder cap.
3. **Skips still logged ✔** — `plan_item_status` and `_adherence` are unchanged; a skip still hurts adherence.
   Mark-done still writes `status` and `done_qty`; only the rep credit was removed.
4. **Backtest ≠ live ✔** — nothing in the evidence layer touches `journal_entries.mode`, `expectancy.py` or
   `opportunity_cost.py`. Journal and missed-trade evidence carry **no** `reps_claimed` effect (they attach to
   subjects that are not rep-bearing), proven by the byte-identical analytics snapshot.
5. **`reps` strictly harder, never easier ✔** — and this is the phase's whole point. It gained an evidence
   precondition and lost *three* write paths. `legacy_reps` is frozen at its pre-`0009` value, so no user can
   reach a rep count today that they could not have reached yesterday.
6. **`auto_met` / `locked` still concept-based ✔** — `services/stages.py` is unmodified; it receives a
   `ProgressView` whose `reps` is now the derived number. The lock chain reads `auto_met`, which is computed
   from ladder positions, so it moves only when a ladder does.
7. **Advisory score never writes `confidence` / `ladder_stage` ✔** — `evidence_grades.score` exists but E2
   writes only `state` (and `findings`) on the `deterministic` grader, and nothing reads `score` yet. The two
   user-owned columns are written exclusively by `PATCH /api/progress` from the request body.

### Walked at E3 (2026-08-02) — each one, explicitly

1. **Gate non-overridable ✔** — no `cleared` column, request field or endpoint was added; `services/gate.py` is
   untouched and reads no rubric or grade. `/api/gate` is byte-identical to the STEP-0 baseline, pinned as a
   durable pytest.
2. **Frontier never gate-eligible ✔** — `watch_only` handling is untouched. A rubric is drill-scoped content and a
   self-check writes only a grade, so neither can lift a frontier concept's Can-mark cap.
3. **Skips still logged ✔** — `plan_item_status` and `_adherence` are unmodified; E3 added no planner path. (The
   one planner touch this session was to a *Playwright spec*, fixing a date-dependency — not to the planner.)
4. **Backtest ≠ live ✔** — nothing in the rubric layer touches `journal_entries.mode`, `expectancy.py` or
   `opportunity_cost.py`. Journal / missed-trade evidence has no bar at all: `_resolve_rubric` refuses to guess one
   (422 naming `rubric_slug`) rather than attaching an unrelated drill's rubric.
5. **`reps` strictly harder, never easier ✔ — and unchanged in E3.** The derivation is untouched: no new write
   path, and the self-check deliberately cannot deduct (above) *or* mint. Both directions are pinned by
   `test_a_self_check_never_moves_a_rep`, and E2's three-endpoint bypass test still passes.
6. **`auto_met` / `locked` still concept-based ✔** — `services/stages.py` is unmodified and reads no rubric. The
   content pass changed *drill* rep targets and `advances_to`; `advances_to` is display-only, and the concept rep
   targets that feed the ladder gate were not touched.
7. **Advisory score never writes `confidence` / `ladder_stage` ✔** — the self-check *does* now write
   `evidence_grades.score` (k/N × 100, informational feedback per §6), and nothing reads it into either
   user-owned column; both remain written exclusively by `PATCH /api/progress` from the request body.

## Contradiction flags (per [[CLAUDE]] Rule #6)

1. **Cost.** The tracker warned that per-rep vision calls "across ~50-rep targets × 53 drills is a real token
   bill." The curriculum is ~500 evidence units (rep targets are per **drill**, not per drill-per-concept) at
   ~$0.02–0.04 each ⇒ **~$15–25 total**. Latency and false negatives bind; spend does not.
2. **Deploy is not unscoped in every tracker.**
   [[processes/distributed-workflow/active/deployment]] holds a proven, pitfall-annotated Render + Cloudflare
   Pages runbook — `neurospect-app` / `neurospect-api` have been live since 2026-04-25 — and its `render.yaml`
   already declares the `R2_*` vars. What is unscoped is deploying **`neurospect-learn`** specifically. R2 was
   never actually wired there (screenshots still 503); that tracker's Phase-5 boot prompt is unrun.
3. **The mobile-capture premise.** The tracker asks whether uploads from a phone/tablet make hosting a
   prerequisite. Every drill assumes desktop TradingView, so the answer is no — and the friction it names is
   already tracked as [[concepts/roadmap/ideas/chrome-screenshot-extension]] and
   [[concepts/roadmap/ideas/reduce-journaling-friction]].
4. **`trade-schema.md` §Missed Trades still specs `missed_trade_screenshots`** — a per-owner child table this
   design deliberately does NOT build (E2 shipped the one polymorphic `evidence_assets` instead, and
   `/journal/missed/:id` attaches to it). That page is the **journal-analytics lane's** canonical doc, so it is
   flagged here for Paul rather than edited from an enforcement session — the same call §Contradiction flag in
   [[concepts/architecture/learning-platform]] made for `phase3-frontend-structure`. Note the spec also describes
   the older `neurospect-app` `trades` schema, where a child table is still the right shape; what is stale is
   only the implication that `neurospect-learn` will grow one.
5. **Unverified sources, labelled.** Duolingo's streak-freeze figures (≈21% churn reduction, +14% D14
   retention) come only from vendor and secondary blogs — **unverified**, and no decision here rests on them.
   MeasureBench and Deci/Koestner/Ryan 1999 are primary and are what the design leans on.

## See Also

- [[processes/distributed-workflow/active/learning-enforcement]] — the workstream tracker (E1–E6)
- [[concepts/architecture/learning-platform]] — the as-built platform this extends (canonical)
- [[concepts/mastery/README]] — the ladder, confidence scale, and Readiness-to-Live Gate (canonical)
- [[concepts/mastery/aura/exercises]] · [[concepts/mastery/ict-course/exercises]] — the drill libraries the
  rubrics are projected from (canonical)
- [[concepts/aura/journaling-system]] — the journaling discipline, and the friction-not-motivation evidence
- [[concepts/architecture/phase2-project-structure]] — the R2 client + key pattern reused (canonical)
- [[concepts/architecture/trade-schema]] — the schema conventions reused, and the child-table shape not repeated
