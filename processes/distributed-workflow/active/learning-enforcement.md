---
tags: [distributed-workflow, active, neurospect, mastery, enforcement, grading, gamification]
aliases: [Learning Enforcement Tracker, Drill Grading, Anti-Cheat, Gamification Workstream]
sources: []
created: 2026-07-25
updated: 2026-08-02
---

# Learning Enforcement — Workstream Tracker

Make `neurospect-learn` a platform that **enforces genuine learning**: a drill can only be completed by
producing **evidence of the work** (a screenshot of your markings for that concept — ranges, standard
deviations, swings, FVGs, SMT, …), that evidence is **graded**, and the whole loop is **gamified** so it drives
consistency. The Phase 5 arc built the skeleton (curriculum, progress, planner, journal, expectancy, gate);
this workstream makes the progress in it **impossible to fake**.

> **STATUS (2026-08-02): Phases E1 + E2 + E3 are ✅ COMPLETE.** E3 added the **rubric layer + self-check** —
> Alembic `0010` (`rubrics` + `rubric_items`), `scripts/seed_rubrics.py` projecting **44 rubrics / 104 items**
> verbatim from the two `exercises.md` libraries (with a programmatic no-drift proof that every item text appears
> in a wiki bullet), a **read-only** rubric API, the `self_check` grade, the self-check UI, and the targeted wiki
> content pass (all seven named drills fixed; `seed_drills.py` orphan refs **5 → 0**; drills **53 → 58**).
> **The decision E3 owed: an unchecked rep STILL COUNTS** — a self-check may flag but never retract, so ungraded
> work is surfaced as an honest backlog rather than deducted (progress stays monotonic). Migrations at `0010`;
> **160 backend tests**; Playwright 50 green at `--workers=1` with a **parallelism flake still open** (handed to
> E4 — see its boot prompt). As-built + every divergence:
> [[concepts/architecture/learning-enforcement]] §E3 as-built. **Phase E4's boot prompt is WRITTEN and ⏭ ACTIVE.**
>
> *Historical (2026-07-28): Phases E1 + E2 complete. The layer is REAL, not theatre — `reps` is no longer
> writable by any endpoint.* E1 landed the canonical design at [[concepts/architecture/learning-enforcement]]
> with all four forks decided (§Decisions). **E2 shipped it**: Alembic `0009` (`evidence_assets` +
> `evidence_grades`), the R2-or-local storage service, the deterministic anti-cheat tier, paste-first capture,
> and — the load-bearing call — **`reps` became DERIVED (`legacy_reps + Σ reps_claimed`) rather than merely
> guarded**, so the planner's mark-done bypass cannot exist rather than being remembered. Both inherited
> screenshot debts are **closed** (journal + missed trade attach to the same polymorphic layer). Migrations are
> at `0009`; 142 backend tests, Playwright 45. **Phase E3's boot prompt is WRITTEN and ⏭ ACTIVE (below)** —
> rubrics + self-check, plus the targeted wiki content pass.
>
> *Historical (2026-07-25): scoped, and Phase E1's boot prompt written.* By Paul's sequencing the first session's boot prompt (a **deep-research + design session, Opus 5**) is
> written **after Phase 6 of [[processes/distributed-workflow/active/learning-platform-ui]] lands** — and it landed
> on **2026-07-25** (that workstream is now closed), so the research starts from the real post-Phase-6 code:
> migrations at `0008`, the missed-trade log + opportunity cost shipped, and the stage exit bars wired to the
> `gate_attestations` + expectancy evidence. **Phase 6 also handed this workstream one concrete piece of debt on
> purpose:** `ict_course` **M6**'s exit bar (13 tape studies + a blind live-read, T-01…T-14) is the ONE stage row
> deliberately left self-attested, because grading a drill as genuinely done is exactly what this workstream must
> define — see [[concepts/architecture/learning-platform]] §Stage exit-bar derivation (`stages.STAGE_UNWIRED`).
> This page holds the vision, the constraints, and the open questions that session must answer.

## Goal (Paul, 2026-07-25 — in his framing)

> "I really want to put a plan together that will ensure that **the user cannot cheat the app** in terms of
> completing exercises and understanding specific topics … we need to implement some sort of **grading system
> for the drills**, meaning **screenshots would have to be uploaded of the markings** for specific concepts
> ex. ranges, std-deviations and all other concepts and topics that are covered."
>
> "The selling point and the main thing I want to focus on is ensuring that this platform **enforces the user
> to learn**, **gamifies it** so it helps the user to remain consistent, and **tracks their progress**."

Three deliverables follow from that:

1. **Verified drills.** A rep counts only when evidence of the work exists and passes a grade — not when the
   user clicks "done".
2. **Anti-cheat.** The shortcuts (recycling one screenshot, bulk-marking 50 reps in a minute, self-declaring
   understanding) are closed off, or at minimum made *visible* rather than silent.
3. **Gamification for consistency.** The mechanics that keep Paul showing up daily, built on the streak /
   adherence / pace surfaces the Study Planner already computes.

Plus a content strand Paul named alongside these: **revisit the structure of the learning path and improve the
exercises/drills themselves** (see §Scope boundary — content vs app).

## North Star (inherited, and sharpened for this workstream)

This workstream inherits the platform north star — **discipline & accountability by design, not by choice**
(stated in full in [[processes/distributed-workflow/active/learning-platform-ui]] §North Star) — and sharpens
it with the framing that makes the "anti-cheat" problem tractable:

**The adversary is self-deception, not an attacker.** This is Paul's personal tool: nobody else gains from
faking a rep. So the goal is *not* tamper-proof security (which would be both impossible and pointless here) —
it is to make **the honest path the path of least resistance**, and to make any shortcut **visible and
recorded** rather than silently absorbed into a progress number Paul will later trust with real capital. A
design that merely *frustrates* honest work fails this north star just as badly as one that lets a rep be
faked: the gate's whole value is that its numbers mean something when it says "cleared".

## What already enforces the process (do NOT redesign these)

The research/design session must build on the shipped enforcement rather than reinvent it:

- **The Readiness-to-Live Gate is non-overridable** — no `cleared` column, endpoint, or UI control; the verdict
  is recomputed per read from the concept ladder + backtest expectancy + four attestations (§5g as-built in
  [[concepts/architecture/learning-platform]]).
- **Ladder advance is already gated** — `PATCH /api/progress` rejects Can-mark+ unless reps ≥ the parsed rep
  target *and* confidence is set; watch-only (U5 frontier) concepts are capped at Can-mark and are never
  gate-eligible (§5e-1 as-built).
- **The planner is prescriptive and logs skips** — `/today` says what to do; a skip is recorded and hurts
  adherence, never hidden; streak / adherence / days-behind / pace are surfaced (§5e-3 as-built).
- **The journal separates backtest from live** and expectancy is computed only over closed trades, with sample
  size visible so an under-evidenced model reads as such (§5f as-built).

**The honest gap this workstream closes:** every one of the above ultimately trusts a **self-reported rep
count** and a **self-rated confidence**. `reps` is just an integer the user increments. That is the single
weakest link in the chain, and it is exactly what evidence-backed grading replaces.

## Open questions the research + design session must answer

Recorded now so the session starts from the real problem, not a blank page. None of these are decided.

**Evidence + grading**
1. What *is* a unit of evidence — one screenshot per rep, per drill session, or per concept? What does a rep
   mean for a day/session-based drill (the `rep_targets` parser already distinguishes reps / days / sessions /
   qualitative / habit)?
2. **How is a marking graded?** Candidates to evaluate, not assume: AI vision grading (Claude, against a
   per-concept rubric), a structured self-check rubric, deterministic/heuristic checks, human-in-the-loop
   review, or a hybrid that escalates. What is the false-negative cost — a wrongly rejected rep is the fastest
   way to make Paul abandon the tool.
3. Where do the **rubrics** come from? The per-concept bar is canonical in the wiki
   ([[concepts/mastery/README]] ladder, the two `exercises.md` drill maps, the entry-model YAML) — a rubric must
   be *derived from* those, never invented alongside them.
4. Is grading **blocking** (a rep does not count until graded) or **asynchronous** (rep provisional, confirmed
   later)? What happens offline / when grading fails?
5. Does a grade carry a **score** (feeding confidence / ladder position) or just pass-fail?

**Anti-cheat**
6. Which shortcuts actually need closing? Candidates: reusing/duplicating an image (perceptual hashing),
   implausible rep pacing, screenshots that aren't charts at all, back-dating, bulk marking. Which are worth the
   complexity, and which should merely be **surfaced** (an honesty signal) rather than blocked?
7. What is the **appeal / override path**, and who can use it? (The gate has none by design — does grading need
   one, and does that reopen the hole?)

**Gamification**
8. Which mechanics actually drive consistency for a solo learner, per the evidence — and which are noise?
   (XP/levels, badges, quests, streak-freeze economics, loss aversion, variable reward, self-competition —
   there is no leaderboard in a single-user app.) This is the part that most warrants genuine external research.
9. How do the mechanics interact with the existing streak / adherence / pace surfaces without double-counting?
10. **The failure mode to design against:** gamification that rewards *activity* over *mastery* would actively
    undermine the gate. What keeps the points honest?

**Storage + platform**
11. Object storage (R2 is already in the wider Neurospect stack) — keys, size/format limits, retention,
    cost, and privacy of chart screenshots.
12. Does this need the app deployed off localhost to be useful (uploads from a phone/tablet while marking
    charts)? Deploy/hosting is currently unscoped in **any** tracker — flag if it becomes a dependency.
13. What does the evidence layer owe the **missed-trade log** and the **journal** (both deferred screenshots to
    this workstream — see §Inherited debt)?

**Curriculum**
14. Which drills in the two `exercises.md` libraries are weak, ambiguous, or ungradable as written — and what
    would make them gradable? (Content work; see the scope boundary below.)

## Scope boundary — content vs app (read before planning phases)

Paul's ask spans two different kinds of work, and conflating them is how this workstream would stall:

- **Wiki/content work** — the *structure of the learning path* and the *quality of the exercises/drills* live in
  [[concepts/mastery/README]], the two `exercises.md` drill maps, and the per-track learning-path pages. The
  wiki is canonical; the app ingests/consumes it. Improving a drill = editing the wiki, then re-seeding.
- **App work** — evidence capture, grading, anti-cheat, gamification mechanics, and their data model live in
  `neurospect-learn` (code is ground truth once written).

A drill can only be graded if its wiki definition states a gradable bar, so the **content pass likely has to
lead** (or at least run alongside) the app phases. The research session should propose the split.

## Inherited debt this workstream owns

Deferred *into* this workstream by earlier decisions — do not build these ad hoc elsewhere:

- ~~**Journal screenshots / R2**~~ — ✅ **CLOSED in E2 (2026-07-28)**: `/journal/:id` §Screenshots attaches to
  `evidence_assets` via `subject_type='journal_entry'`. The deferral was right — it *was* the same primitive.
- ~~**`missed_trade_screenshots`**~~ — ✅ **CLOSED in E2, by NOT building it**: missed trades attach to the same
  polymorphic layer, so the child table specced in [[concepts/architecture/trade-schema]] §Missed Trades will
  never exist here. That page belongs to another lane and is **flagged, not edited** (see the doc's
  §Contradiction flags).
- **`ict_course` M6's exit bar** — the one stage requirement Phase 6 left self-attested (`stages.STAGE_UNWIRED`),
  because its bar *is* drill completion. Wiring it to self-declared drill marks would have baked in the very
  assumption this workstream exists to replace, so E1 should decide what evidence makes T-01…T-14 count.

## Lane

- **This wiki** produces the design artifacts + this tracker: `concepts/architecture/*` (a canonical
  enforcement/grading doc), improvements to `concepts/mastery/*` content, and this page.
- **The app code** lands in `C:\Users\PaulRussell\repos\neurospect-learn` (the Phase 5 app — not a new repo).
  Per [[CLAUDE]] §Architecture Doc Integrity, once code exists the code is ground truth.
- Isolation Rule applies (Neurospect only; no ALDC content/refs).
- The distributed-workflow pattern docs are referenced by absolute path (never wikilink):
  `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`,
  `…\session-lifecycle.md`, `…\tracker-template.md`.

## Plan

### Phase E1 — Deep research + design session ✅ **COMPLETE 2026-07-28**
Delivered the ONE canonical design doc [[concepts/architecture/learning-enforcement]] + the E2–E6 split below.
All 14 open questions answered, none deferred. The load-bearing call (grading mechanism) was settled on
external evidence rather than assumption — see §Decisions and the doc's §"Why tiered".

### Phase E2 — Evidence layer + capture ✅ **COMPLETE 2026-07-28**
Shipped as designed, with one call made harder than the plan required: **`reps` was made DERIVED rather than
guarded**, so no endpoint can mint one and the planner bypass is structurally impossible (the Gate's own
"no `cleared` column" idiom, applied to `reps`). Alembic `0009` (`evidence_assets` with a fail-closed subject
CHECK + `evidence_grades`, plus the `reps` → `legacy_reps` rename), an R2-**or**-local storage service (localhost
needs no bucket), the deterministic tier (magic-byte sniff · size bounds · SHA-256 · perceptual hash, with
measured thresholds), the evidence endpoints, and paste-first capture on `DrillCard` **and `ConceptTrackPanel`**.
Both inherited debts closed. As-built + every divergence:
[[concepts/architecture/learning-enforcement]] §E2 as-built.

### Phase E3 — Rubrics + self-check ✅ **COMPLETE 2026-08-02**
Shipped as designed, with the parser rule refined on measurement: **one item per bullet, split only on TOP-LEVEL
semicolons.** Sentence-splitting was tried and rejected on evidence — this corpus writes "vs." followed by a
capital (`HOD vs. LOD`, `STL (no gap) vs. ITL`, `LRLR vs. HRLR`, `real vs. fake retracement`) and every sentence
heuristic mangled all four; a parser that can mangle wiki text is a parser that *authors* it. Alembic `0010`,
`seed_rubrics.py` (idempotent, stale-pruning, reports everything it could not project), the read-only rubric API,
the `self_check` `evidence_grades` row, `SelfCheck` on the capture surface, and the wiki content pass.
As-built + every divergence: [[concepts/architecture/learning-enforcement]] §E3 as-built.

### Phase E4 — AI vision second reader
Claude Sonnet 5 with a structured-output verdict schema, the rubric held in a `cache_control` system prefix,
run through the Batch API. Advisory `score` + per-item findings + flags, with model/token cost telemetry.
**Never blocks, never retracts, and never writes `confidence` or `ladder_stage`.**

### Phase E5 — Pre-commitment + calibration
`prediction` evidence captured **before** the outcome is revealed (bias · DOL · model · target, timestamped),
then self-scored against the reveal. A **calibration score** — Goodhart-resistant, since more reps cannot
inflate accuracy. Wires `ict_course` **M6** on 14 committed-before-outcome rows so **`stages.STAGE_UNWIRED`
becomes empty** — E1's stated acceptance test.

### Phase E6 — Gamification + honesty surfaces
Computed (never stored) honesty signals on `/gate` — pacing, back-dating, bulk marking, ungraded backlog,
flagged grades — in the 5g "corroboration, not threshold" idiom. The already-shipped streak / adherence /
days-behind / pace surfaces become evidence-backed rather than self-reported. **Declared rest days** in
`study_preferences`. **No XP, no badges, no points on rep count** (see §Decisions).

## Decisions

### 2026-07-28 (Paul, via AskUserQuestion at the E1 design session)

1. **Grading mechanism = tiered hybrid.** Deterministic checks block; a self-check rubric projected from the
   wiki is the rep's own bar; AI vision is a **non-blocking second reader**. Decided on external evidence:
   **MeasureBench** (arXiv 2510.26865) puts frontier VLMs at **19–30%** on precise value readout from analog
   scales — 90%+ unit recognition but ~30% numeric extraction, with *negligible* gains from extended thinking
   because the limit is **perceptual, not computational**. So a vision model cannot arbitrate "is this swing at
   the right price," but is reliable on coarse presence/structure questions. **Cost was NOT the deciding
   factor** — it is ~$15–25 for the whole curriculum (see §Session Log for the correction).
2. **Lifecycle = provisional, graded asynchronously.** A grade may **flag**, never retract — because
   `stages.py` and `gate.py` read `reps`, so retraction would make progress non-monotonic (a met stage could
   un-meet; a Gate verdict could flip backwards untouched).
3. **Anti-cheat = block the certain, surface the rest.** Hard-block only zero-false-positive checks
   (duplicate image, non-image upload); record and display everything judgement-shaped. Follows directly from
   the sharpened north star: a wrongly refused honest rep fails it as hard as a fakeable one. **No appeal path
   is needed**, so the Gate's deliberate no-override property is never reopened.
4. **Deploy = localhost + clipboard paste; hosting is NOT a prerequisite.** Every drill's stated tooling is
   desktop TradingView bar-replay, so capture is paste-first. Storage stays backend-swappable so R2 is a config
   flip later.

**Also decided in E1 (design calls, not forks put to Paul):** the content pass does **not** lead (the
tracker's hypothesis, partially overturned — rubrics project from bullets that already exist, so most drills
are gradable as written); gamification is **informational, not tangible** (Deci/Koestner/Ryan 1999, 128
studies: tangible contingent rewards undermine intrinsic motivation at d ≈ −0.34 while praise and
informational feedback do not); and the evidence layer is **one polymorphic table**, not the per-owner child
tables `neurospect-api` used.

## Session Log

### 2026-07-25 — workstream created (scoping only)
- trigger: at the Phase 5g sign-off Paul set the next direction — verified drill grading via uploaded screenshots
  of chart markings, anti-cheat, and gamification for consistency — and chose (via AskUserQuestion) to give it
  **its own tracker** rather than extend the completed `learning-platform-ui` workstream.
- decided: Phase 6 of `learning-platform-ui` closes the Phase-5 debt first (stage-attestation wiring, missed-trade
  log, `position_size`); **screenshots/evidence storage are deferred into THIS workstream on purpose**, since the
  journal's deferred screenshots and `missed_trade_screenshots` are the same primitive the grading model must
  define; and this workstream's first boot prompt is authored **after Phase 6 lands** (Paul's sequencing), for an
  Opus 5 deep-research session.
- did (wiki only, no code): created this tracker — goal in Paul's framing, the sharpened north star (the
  adversary is self-deception; the honest path must be the easy one), an inventory of what already enforces the
  process plus **the honest gap** (every existing check ultimately trusts a self-reported `reps` integer and a
  self-rated confidence), 14 open questions for E1, the content-vs-app scope boundary, and the inherited debt.
  Cross-linked from `learning-platform-ui`; updated index.md; appended log.md.
- next: land Phase 6 in [[processes/distributed-workflow/active/learning-platform-ui]], then author the E1
  deep-research boot prompt here.

### 2026-07-25 — unblocked by Phase 6 landing (no work done here)
- Phase 6 of [[processes/distributed-workflow/active/learning-platform-ui]] shipped and **closed** that workstream
  the same day (stage-attestation wiring · missed-trade log + opportunity cost, Alembic `0008` · `position_size`).
- Confirmed the two deferrals held: **no screenshots table and no upload endpoint were built**, so the evidence
  primitive is still unshaped and still belongs to E1. Phase 6 additionally left `ict_course` M6's drill-completion
  exit bar self-attested rather than trusting self-declared drill marks — added to §Inherited debt above.
- **Phase E1's boot prompt is now the next thing to author** (Paul's sequencing satisfied); nothing was written for
  it in the Phase-6 session, since scoping a deep-research session is E1's own design act.

### 2026-07-25 — Phase E1 boot prompt authored (wiki only, no design work done)
- trigger: Paul asked for it immediately after the Phase-6 sign-off so he can run E1 in a fresh session.
- did: wrote the **Phase E1 boot prompt** (ACTIVE at the time; ✅ run 2026-07-28 — now in §Boot Prompt Archive)
  and updated the STATUS block + the E1 Plan entry. It is
  built to CONSUME this tracker rather than restate it: the 14 open questions become the session's answer-or-defer
  checklist, §Scope boundary becomes the phase-split constraint, §What already enforces the process becomes a
  do-not-redesign list, and §Inherited debt becomes a data-model requirement (**one** evidence layer serving drills +
  the journal + missed trades, not a drill-only table the journal must later duplicate).
- shaped the prompt around four things the tracker implies but did not spell out: **(1)** the false-negative cost is
  a first-class design constraint, not a footnote — a wrongly rejected rep fails the north star as hard as a
  fakeable one, so the grading step must be *costed* (per-rep vision calls × ~50-rep targets × 53 drills) rather
  than assumed; **(2)** `rep_targets` already distinguishes reps/days/sessions/qualitative/habit, so "one screenshot
  per rep" cannot be the whole answer (a "1 week" habit target has no rep to photograph); **(3)** the app has **no
  storage layer at all** — `boto3` was dropped in the 5b lift — so R2 is a genuinely new dependency with new env
  vars, not a wiring job; **(4)** `stages.STAGE_UNWIRED` (ict_course M6) is E1's concrete acceptance test — a
  successful design makes that map empty.
- also required of E1: research discipline matching this wiki's TIER convention (prefer primary sources, label the
  unverified, never let a vendor claim become a design premise) and an explicit walk of the shipped invariants to
  prove none is weakened — including that `reps` must not become *easier* to satisfy than it is today.
- next: **run the E1 boot prompt in a fresh session** (`claude --model opus[1m]`, `/effort xhigh`, plan mode). Its
  own output writes `concepts/architecture/learning-enforcement.md`, the E2+ phase list, and the Decisions block.

### 2026-07-28 — Phase E1 ✅ deep research + design (wiki only, no app code)
- approach: ran the E1 boot prompt on **Opus 5**, plan mode. Read the wiki CLAUDE.md, this tracker, the
  as-built [[concepts/architecture/learning-platform]] (all 1,191 lines), the mastery corpus + both drill
  libraries, and the shipped enforcement code (`services/{stages,rep_targets}.py`, `routers/learning.py`,
  `routers/planner.py::_adherence`, `models/drill_progress.py`, `alembic/0008`, `scripts/seed_drills.py`,
  `config.py`, `.env.example`, `pyproject.toml`). Then genuine external research, then the four forks to Paul
  **before** writing anything.
- **the finding that decided the design:** searched for the feasibility of vision-model grading of annotated
  charts and found **MeasureBench** (arXiv 2510.26865) — frontier VLMs score **Gemini 2.5 Pro 30.3% / Qwen3-VL
  23.7% / GPT-5 19.8%** on precise value readout from analog scales, with unit recognition >90% but numeric
  extraction ~30%, and **extended thinking giving negligible gains because the limitation is perceptual**. That
  is precisely the "which price level is this line at" task, so AI vision was demoted from arbiter to advisory
  second reader. Also found **Deci/Koestner/Ryan 1999** (128 studies): tangible contingent rewards undermine
  intrinsic motivation (d ≈ −0.34) while **praise/informational feedback does not** → no XP, no badges, no
  points on rep count.
- decided: see §Decisions (all four forks + the three design calls).
- did: created the canonical [[concepts/architecture/learning-enforcement]]; added the new topic to the
  wiki CLAUDE.md **Canonical doc per topic** table; additive cross-links from
  [[concepts/architecture/learning-platform]] and [[concepts/mastery/README]]; marked Phase E1 ✅ and replaced
  the "Phases E2+ — TBD" stub with the real E2–E6 list; added this §Decisions block; bumped index.md; appended
  to log.md. **No app code — nothing in `neurospect-learn` was touched.**
- **flagged (Rule #6) — three tracker premises corrected:**
  **(1) Cost.** This tracker warned per-rep vision calls "across ~50-rep targets × 53 drills is a real token
  bill." The real curriculum is ~500 evidence units (rep targets are per *drill*, not per drill-per-concept) at
  ~$0.02–0.04 each ⇒ **~$15–25 total**, halved again by the Batch API. Latency and false negatives bind; spend
  does not.
  **(2) "Deploy/hosting is unscoped in EVERY tracker" is not true** —
  [[processes/distributed-workflow/active/deployment]] holds a proven, pitfall-annotated Render + Cloudflare
  Pages runbook, `neurospect-app`/`neurospect-api` have been live since 2026-04-25, and that `render.yaml`
  already declares the `R2_*` vars. What is unscoped is deploying **`neurospect-learn`** specifically. R2 was
  never actually wired there (screenshots still 503); that tracker's Phase-5 boot prompt is still unrun.
  **(3) The mobile-capture premise looks wrong** — every drill assumes desktop TradingView bar-replay, so
  paste-from-clipboard is the high-leverage affordance, and the friction it names is already tracked as
  [[concepts/roadmap/ideas/chrome-screenshot-extension]] + [[concepts/roadmap/ideas/reduce-journaling-friction]].
- also found, and reused rather than reinvented: `neurospect-api` already ships a **working boto3 R2 client**
  (`app/services/r2.py` + `routers/screenshots.py`, with the `r2 is None → 503` degradation), the R2 key
  pattern and env-var names are canonical in [[concepts/architecture/phase2-project-structure]], and
  `python-multipart` is **already** a dependency of `neurospect-learn` — so `UploadFile` needs no new dep.
  And the strongest in-corpus support for friction-first design was already written down:
  [[concepts/aura/journaling-system]]'s finding that 50% of surveyed traders don't journal consistently for
  **instruction reasons, not motivation reasons**.
- verified (doc integrity): isolation clean (Neurospect only; the distributed-workflow pattern docs stay
  absolute paths, never wikilinks); no-drift honoured (the design links the mastery corpus and both drill
  libraries and restates neither — rubrics are a *parsed projection*, so no rubric text lives outside the
  wiki); **every shipped invariant walked one by one and none weakened** — the Gate stays non-overridable and
  computed-per-read, frontier stays never-gate-eligible, skips stay logged, backtest≠live holds, `auto_met`/
  `locked` stay concept-based, the advisory score never writes `confidence`/`ladder_stage`, and **`reps` gets
  strictly *harder* to satisfy (it gains an evidence precondition and loses nothing)**; all 14 open questions
  answered with none deferred; every E2–E6 phase is boot-promptable from this tracker alone.
- next: **write the E2 boot prompt** (evidence layer + capture, incl. journal + missed-trade attachment), then
  run it.

### 2026-07-28 — Phase E2 boot prompt authored (wiki only, no code)
- trigger: Paul asked for it in the same session as the E1 sign-off so he can run E2 fresh.
- did: wrote the **Phase E2 boot prompt** below in §Next Session Boot Prompt (⏭ ACTIVE) and updated the STATUS
  block + the E2 Plan entry. It
  is built to CONSUME the E1 design rather than restate it — the canonical doc's §7 is the DDL spec, §8 the
  storage spec, and §Invariants becomes the verification checklist.
- shaped it around the traps a fresh session would otherwise walk into: **(1)** `drill_progress.reps` /
  `concept_progress.reps` are written by **two** paths — `learning.py` *and* `planner.py`'s mark-done — so
  gating only the learning router leaves the planner as a rep-minting bypass and makes the whole layer theatre;
  the prompt names this as the phase's load-bearing call and requires a test that attempts the bypass and fails.
  **(2)** the `downgrade base` footgun that has already wiped the seed twice (an exported `DATABASE_URL` does
  **not** override the `.env` Alembic reads) → scratch-DB-only reversibility testing, pinned by config.
  **(3)** the three as-built gotchas worth reusing rather than rediscovering: the textual `NOT is_deleted`
  ON CONFLICT predicate, the `expire_on_commit=False` stale-identity-map trap, and `NULLS NOT DISTINCT`.
  **(4)** a STEP 0 that captures an analytics/gate **baseline** so the Phase-6 byte-identical no-regression
  evidence gate can be repeated — an evidence layer must not move expectancy or the Gate.
  **(5)** the upload path is the app's first user-supplied-file surface, so magic-byte sniffing (never trust
  the client `content_type`), filename sanitisation, size caps and presigned-only reads are stated explicitly.
- also required of E2: **close both inherited debts in-phase** (journal + missed-trade evidence attach to the
  same polymorphic table — the whole reason the design rejected per-owner child tables), and **flag rather
  than edit** `trade-schema.md`'s `missed_trade_screenshots` spec, since that page belongs to the
  journal-analytics lane (the precedent §Contradiction flag set for `phase3-frontend-structure`).
- next: **run the E2 boot prompt in a fresh session** (`claude --model opus[1m]`, `/effort high`, DB up on
  :5433). Its own output writes the E2 as-built sections, the E3 boot prompt, and the bookkeeping.

### 2026-07-28 — Phase E2 ✅ evidence layer + capture (the layer is real, not theatre)

- approach: ran the E2 boot prompt on Opus 5. STEP 0 first, as evidence not assumption: `alembic current` =
  `0008 (head)`, seeds **74/23/53/67**, `pytest` **114 passed**, Playwright **36 passed**, and a fixture-user
  baseline of `/api/analytics/*` + `/api/gate` captured to
  `neurospect-learn/api/docs/evidence/e2-baseline-before.json` (sha256 `27ff7157…`).
- **decided — THE LOAD-BEARING CALL: make `reps` DERIVED, not guarded.** The prompt named the risk exactly
  right (`reps` is written by `learning.py` *and* `planner.py`, so gating one leaves the other as a rep-minting
  bypass). Rather than apply the same precondition in two places — which a future third write path would
  silently reopen — `0009` **renames** the columns to `legacy_reps` and the API computes
  `reps = legacy_reps + Σ evidence_assets.reps_claimed`. `reps` left `ProgressPatch`/`DrillPatch` entirely and
  `planner._feed_*` stopped incrementing. **This is the Gate's own idiom:** 5g made non-overridability
  structural ("no `cleared` column, no endpoint that sets one"); E2 does the same for `reps`. A guard has to be
  remembered at every new write path; a derivation cannot be forgotten.
- decided: **rename rather than drop**, so `legacy_reps` preserves pre-evidence claims and no already-met stage
  un-meets (the same monotonicity argument behind "a grade flags, never retracts") — and it yields the
  declared-vs-derived signal for free (`reps` / `reps_evidenced` / `reps_legacy`, rendered as
  "12 / 50 reps · 5 evidenced · 7 pre-evidence"). Also decided beyond the prompt's minimum: **capture on
  `ConceptTrackPanel`, not just `DrillCard`** — `PATCH /api/progress` gates on *concept* reps, so without it
  every concept carrying a numeric target would have become unreachable, which is precisely the catastrophic
  false negative the north star forbids.
- did (code, `neurospect-learn`): Alembic `0009` (2 tables, 4 enums, 8 indexes, 2 triggers, the rename);
  `models/evidence.py`; `services/storage.py` (R2 **and** a local-filesystem backend — no `503` sentinel,
  because localhost is the primary path, with a signed key-scoped JWT read so `<img src>` works identically
  either way); `services/evidence_checks.py` (the deterministic tier); `routers/evidence.py` +
  `schemas/evidence.py`; the derived-`reps` rewiring of `routers/{learning,planner}.py`; frontend
  `lib/evidence.ts` + `components/evidence/evidence-capture.tsx` wired into `DrillCard`, `ConceptTrackPanel`,
  `/journal/:id`, `/journal/missed/:id`; `RepCounter` made read-only. Deps: `boto3`, `Pillow`, `imagehash`
  (**not** `anthropic` — that is E4's). Plus two durable scripts: `scripts/evidence_baseline.py` and
  `scripts/scratch_migrate.py`.
- **also retired the `downgrade base` footgun for good.** `alembic/env.py` now honours `-x db_url=…`, and
  `scratch_migrate.py` creates and drops its own throwaway DB. The reason an exported `DATABASE_URL` never
  redirected Alembic: `.env` *also* sets `DATABASE_URL_SYNC`, which wins for the sync URL Alembic reads — that
  is what wiped the seed twice.
- **flagged (Rule #6) — two live bugs the RENDERED-SURFACE check caught, both of which a query-layer pass
  reported as green:**
  **(1) ky v2 consumes an error's response body** to populate `error.data`, so `error.response.json()` throws.
  Every FastAPI `detail` was being replaced by ky's generic "Request failed with status code 4xx" — including,
  silently **since 5e-1**, the ladder-advance gate's own reason. Fixed with a shared `apiErrorDetail()` in
  `lib/api.ts`; `lib/learning.ts` was on the same broken path. `neurospect-app` may carry the same latent bug.
  **(2) The local backend's signed URL is app-relative**, so `<img src>` resolved it against the SPA origin
  (`:5173`) and **every thumbnail rendered broken** — while the Playwright assertion passed, because it checked
  the `src` attribute rather than whether the image loaded. Fixed with `evidenceSrc()`; the spec now polls
  `naturalWidth > 0`. A textbook case for validating at the rendered surface.
- flagged (Rule #6): **`trade-schema.md` §Missed Trades still specs `missed_trade_screenshots`**, which this
  design deliberately does not build. That page is the journal-analytics lane's — **flagged, not edited**,
  following the `phase3-frontend-structure` precedent.
- **measured rather than guessed:** the perceptual-hash thresholds. Block ≤ **4**, flag 5–**7**. On chart
  captures: identical / re-encode / rescale = 0, a 0.5% crop = 2, a 1% crop = 6, **the same chart with one new
  marking = 8–10**, a 2% crop = 14, a different chart = 26–34. Re-marking one chart is a *real* extra rep
  ("≥50 ranges" on one instrument) and it sits inside the range a 2% crop occupies — so past ~7 the signal
  genuinely cannot separate recycling from honest work, and the design claims nothing there rather than
  refusing real reps. Pinned in `tests/test_evidence_checks.py::test_measured_phash_separation`.
- verified (evidence, not inference): `0009` up/down/up/base reversible on a **scratch** DB, working-DB seeds
  intact 74/23/53/67; the subject CHECK rejects zero-subject, two-subject and mismatched-discriminator rows **at
  the database**; exact + near-duplicate uploads refused **with reasons**; **the bypass test asserts all three
  rep-writing endpoints fail to mint a rep**; `/api/analytics/*` + `/api/gate` **byte-identical** to the STEP-0
  baseline (same sha256 `27ff7157…`, and pinned as a durable pytest); per-user isolation; no-token 403; the local
  backend works with no R2 config. **142 backend tests** (114 → +28), `tsc -b` + `vite build` clean,
  **Playwright 45** (36 → +9) stable across three consecutive full runs, and a live claude-in-chrome walkthrough
  of every changed surface (paste → thumbnail → rep; a duplicate refused with its reason on screen; journal +
  missed attach) with **NO console errors**. All 7 design invariants walked one by one — see the doc's
  §Walked at E2.
- **ops note:** the running uvicorn had no `--reload`, so it served pre-`0009` code against the post-`0009`
  schema and every learning endpoint 500'd until it was restarted (with `--reload`). Worth remembering: after a
  migration that renames a column, a stale dev server fails loudly but confusingly.
- next: **run the E3 boot prompt** (rubrics + self-check + the targeted wiki content pass).

### 2026-08-02 — Phase E3 ✅ rubrics + self-check + the wiki content pass

- approach: ran the E3 boot prompt on Opus 5. STEP 0 as evidence first: `alembic current` = `0009 (head)`, seeds
  **74/23/53/67**, `pytest` **142 passed**, Playwright **45 passed**, baseline captured to
  `docs/evidence/e3-baseline-before.json` (sha256 `27ff7157…`, identical to E2's). Then **read how the bullets are
  actually written before designing the parser** — which is what settled the phase's real decision.
- **decided — THE PARSER RULE, on measurement not preference: one item per bullet, split ONLY on top-level
  semicolons.** Two facts refined the design's "one item per bullet": (1) several bullets are compound
  (aura **D0-a** is four deliverables in one), and one checkbox for four forces a **dishonest tick** — the exact
  self-deception this workstream exists to prevent; (2) adding a sentence split **mangled four real bullets**,
  because this corpus writes "vs." mid-sentence followed by a capital (`**which KZ sets the HOD vs. LOD**`,
  `**STL (no gap) vs. ITL (…)**`, `Tag **LRLR vs. HRLR**`, `tag real vs. **fake retracement**`). A parser that can
  mangle wiki text is a parser that **authors** wiki text, so the ambiguous rule was rejected and the unambiguous
  one kept. Depth-aware, because the corpus also puts semicolons inside parens and inside a quoted bias statement.
- **decided — an UNCHECKED rep still counts.** The prompt flagged this as the one open question and the answer
  follows from E2: `stages.py`/`gate.py` read `reps`, so deducting on a missing or partial check would make
  progress **non-monotonic** (a met stage exit bar could un-meet; a Gate verdict could flip backwards untouched).
  A partial check records `flagged` + the specific unticked items and **never `failed`**; the backlog is
  **surfaced** ("N awaiting your check", "not checked yet — the reps still count"), never deducted. The
  adversarial case — an **empty** self-check on a 4-rep capture — is a pinned test.
- did (code, `neurospect-learn`): Alembic `0010` (2 tables, 1 enum, 5 indexes, 2 triggers); `models/rubric.py`;
  `scripts/seed_rubrics.py` (**44 rubrics / 104 items**, idempotent UPSERT, stale-prune, `--dry-run` and
  `--show <drill_ref>`, and a report of everything it could not project); `routers/rubrics.py` (**read-only** —
  POST/PATCH/PUT/DELETE all 405); the `self_check` grade write in `routers/evidence.py`; `schemas/rubric.py`;
  frontend `lib/rubrics.ts` + `components/evidence/self-check.tsx` wired through `EvidenceCapture`. Extended
  `scratch_migrate.py` with **separate E2/E3 object groups** so a single-step downgrade proves `0010` removes only
  its own objects. 18 new pytests, 5 new Playwright tests.
- **the no-drift proof is programmatic, not asserted:** `verify_no_drift()` checks that **every** item's text is a
  contiguous substring of a whitespace-normalised wiki bullet, across the whole seed — inside every seed run *and*
  as `test_no_rubric_text_is_authored`. `version` bumps iff a sha256 over the items changes, so provenance edits
  don't imply the bar moved and re-seeding twice is a genuine no-op (0 bumped / 44 unchanged).
- **flagged (Rule #6) — two bugs the DB and the corpus caught, plus a doc undercount:**
  **(1) A phantom drill named "Evolving."** A loose inline-drill regex matched the bolded lead-in
  `**Evolving-R reps:**` inside aura **D3-c** as a drill definition — inventing a rubric AND **stealing that bullet
  from D3-c**. Fixed by anchoring the code pattern to the four shapes the corpus uses (`D4-a`·`T-01`·`J-a`·`S7`).
  **(2) The version bump could not write.** Replacing a rubric's items via the ORM collection emitted the INSERTs
  **before** the orphan DELETEs, colliding on `ux_rubric_items_key`; every re-seed with a changed bullet died with
  an `IntegrityError`. Fixed with `clear()` + `flush()`, and the regression test was **verified to fail on exactly
  that constraint with the fix reverted**.
  **(3) The design said "4 aura Stage-0 drills the map omits" — there are FIVE** (D0-a…e). Corrected in the doc.
- did (wiki content pass — the wiki is canonical, so every fix is a wiki edit + re-seed, never a code patch):
  aura **D1-c** (bogus 50-rep floor → qualitative), **D2-a** (1 → 2), **D2-d** (→ ≥10), **D3-a** (→ ≥20 practice
  entries), **D3-c** (→ ≥3 batches), ict **D3-d** (`Learned→applied`, not a ladder stage → `Can-mark`), and the
  **five aura Stage-0 drills** added to the map table. Result: orphan refs **5 → 0**, drills **53 → 58**, rubrics
  whose drill the map omits **8 → 3**. Two edits went beyond a map cell and are called out: the D2-d/D3-a **bullet
  punctuation** (so a compound bar becomes tickable — these are the two rubrics that bumped to v2) and aura
  D3-a/D3-c's `advances_to`, fixed alongside ict D3-d because they carried the identical non-ladder value
  (`advances_to` is display-only, so nothing gates on it).
- **also fixed two genuine defects the verification surfaced, neither of them E3 features:**
  **(1) Two N+1 request storms.** `/drills` mounts an `EvidenceCapture` per drill (58), and both `useEvidence`
  (pre-existing, E2) and the first cut of `useRubrics` keyed **per subject** — ~116 near-identical requests per page
  load, saturating the browser's 6-connection limit and queueing the user's own upload behind the pile. Both now
  fetch once under a shared key and slice client-side. Suite wall-clock ~47s → ~31s.
  **(2) A latent date-dependency in `planner.spec.ts`.** The availability form ships `sun_minutes: 0`, so a plan for
  a Sunday is **correctly empty** — and that spec, which relied on the defaults, failed *every Sunday*. This session
  ran Wed → Sun and hit it. Fixed by giving **today** explicit capacity, making the spec date-independent.
- verified (evidence, not inference): `0010` up/down/up/base reversible on a **scratch** DB **plus** a single-step
  proof that `downgrade 0009` leaves E2's layer untouched; seeds intact across the migration; the no-drift proof
  over all 104 items; idempotent re-seed; a bullet edit bumps **only** the edited rubric (`aura-d2-d` v2,
  `aura-d3-a` v2, `aura-d1-a` still v1); a self-check attaches as an **additional** grade with the deterministic row
  surviving; refusals name the offending key/slug/drill; **`reps` moved in neither direction** (E2's bypass test
  plus the empty-self-check test); `/api/analytics/*` + `/api/gate` **byte-identical** to STEP 0 (same sha256
  `27ff7157…`); all 7 invariants walked one by one (doc §Walked at E3). **160 backend tests** (142 → +18),
  `tsc -b` + `vite build` clean, `self-check.spec.ts` 5/5 and `planner.spec.ts` 5/5.
- **NOT closed, handed to E4 — do not call the suite green:** the **full** Playwright suite (50) passes at
  `--workers=1` and passed once at default parallelism right after the N+1 fixes, but later default-parallelism runs
  went flaky (2–3 rotating failures, wall-clock drifting 31s → 1.5m) with `ECONNRESET` against the dev API. The two
  real defects found on the way are fixed; the residue is undiagnosed. Also **not done**: the live claude-in-chrome
  walkthrough of the self-check surface (the boot prompt asked for it; the session ran out of room first).
- next: **run the E4 boot prompt** (AI vision second reader) — which opens by closing E3's two open items.

## Next Session Boot Prompt (Phase E4 — AI vision second reader) ⏭ ACTIVE

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort high`**. Not for the API plumbing — for
two judgement calls: the **verdict schema** (what a vision model may and may not be asked, given that
MeasureBench puts it at ~30% on precise value readout) and **cost/latency control** (Batch API + a cached rubric
prefix), plus the discipline that this tier **never blocks and never retracts**.

Before you start: Docker `neurospect-learn-db` up on :5433 with seeds present, and start the API with `--reload`
(a stale dev server after a migration is what cost E2 time). `ANTHROPIC_API_KEY` will be needed — **ask Paul
before using any credential**, and never echo it.

GROUNDING: `neurospect-learn` is Paul's standalone learn-to-execute app for the Neurospect ICT / Smart-Money-Concepts
trading-mastery project — FastAPI + Postgres (`api/`) + React 19 / Vite / TanStack Query (`app/`). Phase 5, its
Phase-6 debt, and learning-enforcement **E2 (evidence layer)** and **E3 (rubrics + self-check)** are COMPLETE and
shipped: curriculum + three graded tracks, Study Planner, model-aligned journal, expectancy, the computed
non-overridable Readiness-to-Live Gate, the missed-trade log, stage exit bars on real evidence, `evidence_assets`/
`evidence_grades` with `reps` **DERIVED** from uploaded evidence, and `rubrics`/`rubric_items` **projected verbatim
from the wiki** with a `self_check` grade that may flag but never retract. Migrations at `0010`; seeds 74 concepts /
23 track stages / **58** drills / 67 content pages + **44 rubrics / 104 items**; **160 backend tests**, Playwright 50.

STEP 0 — CLOSE E3's TWO OPEN ITEMS FIRST, before writing any E4 code:
  1. **The Playwright parallelism flake.** `npx playwright test` is green at `--workers=1` but flaky at default
     parallelism with `ECONNRESET` against the dev API. Diagnose it properly rather than pinning `workers: 1`:
     start by checking the **SQLAlchemy async pool** (`create_async_engine` defaults to pool_size 5 + overflow 10,
     shared by one uvicorn process across all Playwright workers) and whether `/api/plan/regenerate` or the
     `/drills` page load exhausts it; also check whether the e2e debug users have accumulated enough
     `evidence_assets` rows to slow the per-upload duplicate scan. Fix the cause, then prove **three consecutive
     clean full runs at default parallelism**.
  2. **The live claude-in-chrome walkthrough of the self-check surface** — E3 shipped it verified by tests but
     never by eye. Assert the **RENDERED** result (E2's lesson: a Playwright assertion on an attribute passed while
     every thumbnail rendered broken). Paste a capture on a drill card, open "Check against the bar", confirm the
     wiki's own bullets render as checkboxes **with no raw `**` markers**, record a partial and a full check, and
     confirm **NO console errors**. `CORS_ORIGINS` allows only `http://localhost:5173`.

BOOT / CONTEXT — read in this order, and read the first two IN FULL:
1. The wiki `CLAUDE.md` — Isolation Rule, Architecture Doc Integrity (**code is ground truth; ONE canonical doc per
   topic; LINK the corpus, never restate it**), the MANDATORY post-implementation reconciliation checklist, Rules
   #1 (**never modify `sources/`**) #3 (index.md) #4 (log.md) #6 (flag contradictions), Context Management (tell
   Paul at >50%). **Paul handles git — NEVER commit.**
2. `concepts/architecture/learning-enforcement.md` — especially **§2 tier 3** (your spec: advisory only), **§"Why
   tiered — the evidence that decided it"** (MeasureBench: ~19–30% on precise value readout, >90% on unit
   recognition, negligible gains from extended thinking **because the limit is perceptual** — this is WHY vision
   may not arbitrate "is this swing at the right price"), **§4 lifecycle**, **§7 the data model** (`evidence_grades`
   already has `grader='ai_vision'`, `score`, `rubric_slug`/`rubric_version`, `findings`, **and `model` /
   `input_tokens` / `output_tokens` / `cost_usd` waiting to be filled**), **§E2 as-built**, **§E3 as-built** (the
   rubric you will send, and why `reps` must not move), **§Invariants + §Walked at E2 / §Walked at E3**.
3. `processes/distributed-workflow/active/learning-enforcement.md` — §Decisions (fork 1: **AI vision is a
   NON-BLOCKING second reader**), §What already enforces the process (**DO NOT redesign these**).
4. THE CODE TO REUSE, NOT REINVENT: `api/app/routers/evidence.py` (the `self_check` write is the shape an
   `ai_vision` write mirrors — additive, never destructive), `api/app/models/evidence.py` (the telemetry columns),
   `api/scripts/seed_rubrics.py` (how to load a rubric to send as the prompt's bar), `api/app/services/storage.py`
   (reading the stored image bytes), `api/tests/{test_rubrics.py,evidence_helpers.py}` (the harness), and
   `api/app/config.py` + `api/.env.example` (**CANONICAL** for env config).
5. **Load the `claude-api` skill before writing any Anthropic call** — model ids, pricing, structured outputs,
   `cache_control`, the Batch API and token counting. Do not answer from memory.

BUILD — in this order:
  1. **`services/ai_grader.py`** — a pure-ish service: given image bytes + a rubric, return a structured verdict.
     **The schema is the load-bearing design.** Ask ONLY what a VLM is reliable at: coarse presence/structure
     (*is this an annotated price chart · are range boundaries drawn · was a second pass done · which rubric items
     are visibly evidenced*). It must be **incapable** of expressing "this swing is at the wrong price" — if the
     schema cannot say it, the model cannot assert it. Rubric text goes in a **`cache_control` system prefix**.
  2. **Async, never blocking.** A grade is requested after capture and lands later; upload latency must not change.
     Decide and justify the mechanism (FastAPI `BackgroundTasks` vs a polled queue table vs the **Batch API**) —
     §2 says Batch, and the cost note says ~$0.02–0.04/grade, ~$15–25 for the whole curriculum. Offline / API-down
     must leave the row honestly `ungraded`, which is already a first-class enum value.
  3. **Write telemetry.** `model`, `input_tokens`, `output_tokens`, `cost_usd` per grade — the design costed this
     phase, so the code must measure it rather than trust the estimate.
  4. **Surface it as INFORMATIONAL FEEDBACK (§6), never as a verdict on the rep.** Per-item findings beside the
     user's own self-check, visibly labelled advisory + second-reader. Where the AI and the self-check DISAGREE is
     the genuinely useful signal — show it, decide nothing from it.

E4 IS NOT: prediction capture, the calibration score, or wiring `ict_course` M6 / emptying `stages.STAGE_UNWIRED`
(E5); gamification, XP, or the `/gate` honesty strip (E6); deploying or provisioning R2 (storage stays local);
re-opening that `reps` is derived, that a grade may not retract, or that rubrics are wiki-projected and read-only;
redesigning the shipped enforcement (the non-overridable Gate, the ladder-advance gate, the watch-only cap, logged
skips, backtest≠live) — build ON those.

VERIFY (evidence, not inference — Paul's evidence-gated rule and the house standard from 5g / Phase 6 / E2 / E3):
  · Any migration reversible via `scripts/scratch_migrate.py` (extend its object lists); ⚠️ **NEVER
    `alembic downgrade base` against the working DB**; seeds still 74/23/58/67 + 44/104 afterwards.
  · **An `ai_vision` grade is ADDITIVE** — the `deterministic` and `self_check` rows both survive.
  · **It never blocks and never retracts:** prove an AI grade cannot change `reps`, `confidence`, `ladder_stage`,
    any stage exit bar or the Gate. Re-run E2's bypass test and E3's `test_a_self_check_never_moves_a_rep`.
  · **API-down / no-key degrades honestly** to `ungraded` with the upload path unaffected — test it with the key
    absent, since that is Paul's normal local state.
  · **Cost is measured, not assumed:** report real token counts and $ for a handful of grades against the design's
    $0.02–0.04 estimate, and flag it (Rule #6) if it is wrong.
  · **THE NO-REGRESSION EVIDENCE GATE:** `poetry run python scripts/evidence_baseline.py --seed --out
    docs/evidence/e4-baseline-before.json` at STEP 0, re-capture at the end, prove **byte-identical** (E2 and E3
    both hit sha256 `27ff7157…`).
  · Walk the design's §Invariants one by one and state each explicitly (§Walked at E2 / §Walked at E3 is the format).
  · `pytest` (report the new total vs **160**) · `tsc -b` + `vite build` clean · `npx playwright test` (vs **50**)
    **at default parallelism, three consecutive clean runs** · a live claude-in-chrome walkthrough with **NO
    console errors**.

RECONCILE + BOOKKEEP (MANDATORY — wiki CLAUDE.md §Architecture Doc Integrity):
  · Update **`concepts/architecture/learning-enforcement.md`** with an "§E4 as-built" section recording every
    divergence, the real measured cost, and a §Walked at E4.
  · Update **`concepts/architecture/learning-platform.md`** §Progress data model + §Component/API surface.
  · In the tracker: mark Phase E4 ✅, add a Session Log entry (approach / decided / did / flagged / verified / next),
    and write the **E5 boot prompt**.
  · Append a row to `log.md`; bump `index.md`. **Paul handles git — NEVER commit.**

## Boot Prompt Archive (Phase E3 — rubrics + self-check) ✅ RUN 2026-08-02

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort high`**. The code is mostly a seed
script and a form, but two things need judgement: the **parser** that projects wiki bullets into rubric items
(get it wrong and rubric text starts being authored in the app, which is the drift the design forbids), and the
**content pass** on the drills E1 named ungradable — that is wiki editing, and the wiki is canonical.
Working dirs: `C:\Users\PaulRussell\repos\neurospect-learn` (the build; **code is ground truth**) +
`C:\Users\PaulRussell\repos\neurospect-wiki` (the rubric SOURCE, and reconciliation). **You need the DB
running** (Docker `neurospect-learn-db`, local Postgres :5433) with seeds present, and the API dev server
started with `--reload`. Paste:

````
GROUNDING: `neurospect-learn` is Paul's standalone learn-to-execute app for the Neurospect ICT / Smart-Money-Concepts trading-mastery project — FastAPI + Postgres (`api/`) + React 19 / Vite / TanStack Query (`app/`). The Phase 5 arc, its Phase-6 debt, and the learning-enforcement Phase E2 evidence layer are all COMPLETE and shipped: curriculum + three graded tracks, Study Planner, model-aligned journal, expectancy, the computed non-overridable Readiness-to-Live Gate, the missed-trade log, stage exit bars on real evidence, and — since E2 — `evidence_assets`/`evidence_grades` with `reps` DERIVED from uploaded evidence rather than writable by any endpoint. Migrations are at `0009`; seeds are 74 concepts / 23 track stages / 53 drills / 67 content pages; 142 backend tests + Playwright 45 green.

Neurospect — Phase E3 of the LEARNING-ENFORCEMENT workstream: BUILD the rubric layer + self-check. The design is APPROVED — this is an EXECUTION session with one genuine content strand. E2 made a rep require EVIDENCE; E3 makes it require evidence THE USER HAS CHECKED AGAINST THE DRILL'S OWN BAR.
Working dir: C:\Users\PaulRussell\repos\neurospect-learn  |  Wiki (the rubric SOURCE + reconcile at the end): C:\Users\PaulRussell\repos\neurospect-wiki

BOOT / CONTEXT — read in this order, and read the first two IN FULL:
1. The wiki CLAUDE.md — Isolation Rule (Neurospect ONLY), Architecture Doc Integrity (code is ground truth; ONE canonical doc per topic; LINK the corpus, never restate it), the MANDATORY post-implementation reconciliation checklist, Rules #1 (**never modify `sources/`**) #3 (index.md) #4 (log.md) #6 (flag contradictions), Context Management (tell Paul at >50%). Paul handles git — NEVER commit.
2. concepts/architecture/learning-enforcement.md — the approved design AND the E2 as-built. §3 rubric provenance (your spec), §2 tier 2 (the self-check IS the rep's bar), §4 lifecycle, §7 the data model you extend, **§E2 as-built** (what actually shipped — especially that `reps` is DERIVED and `evidence_grades` already exists with a `deterministic` row per asset, so you are ADDING a `self_check` grader, not inventing the table), §Invariants + §Walked at E2, and §"Drills ungradable or ambiguous as written" — that list IS your content scope.
3. processes/distributed-workflow/active/learning-enforcement.md — the tracker: §Decisions, §Scope boundary (content vs app — E3 is the one phase that does BOTH), §What already enforces the process (DO NOT redesign these).
4. concepts/mastery/aura/exercises.md + concepts/mastery/ict-course/exercises.md **IN DETAIL** — the ✋/🛠 bullets under each drill are the rubric SOURCE, and the map tables at their foot are what `seed_drills.py` already parses. Read how the bullets are actually written before designing the parser: they are not uniform.
5. THE CODE TO REUSE, NOT REINVENT: `api/scripts/seed_drills.py` (**the projection idiom your seeder mirrors** — parses the wiki, idempotent UPSERT, stale-prune, reports orphans), `api/scripts/ingest_content.py` (the markdown/frontmatter reading idiom), `api/alembic/versions/0009_evidence_layer.py` (the migration idiom + the enums you extend), `api/app/routers/evidence.py` (where a self-check grade attaches), `api/app/models/evidence.py`, `api/tests/{evidence_helpers.py,test_evidence_api.py}` (the harness + the `give_*_reps` helpers), `app/src/components/evidence/evidence-capture.tsx` (where the self-check UI lands), `app/src/lib/evidence.ts` (the query-key + invalidation idiom).
6. `api/.env.example` — CANONICAL for env config.

STEP 0 — PROVE THE STARTING STATE (evidence, not assumption): `alembic current` == `0009 (head)`; seeds exactly 74/23/53/67; `pytest` == 142 passed; `npx playwright test` == 45 passed. Capture a BASELINE with the EXISTING script — `poetry run python scripts/evidence_baseline.py --seed --out docs/evidence/e3-baseline-before.json` — you will diff it at the end. Reversibility testing goes through `scripts/scratch_migrate.py` (it creates and drops its own throwaway DB); ⚠️ NEVER run `alembic downgrade base` against the working DB.

BUILD — in this order:

  1. **`scripts/seed_rubrics.py` — a PROJECTION, not authorship.** Parse each drill's ✋/🛠 bullet list out of the two `exercises.md` files into ONE RUBRIC ITEM PER BULLET, tagged hand/tool by the glyph, keyed to the `drill_ref` the existing map-table parse already yields. **NO rubric text may be authored in the app or in the seed** — if a bullet does not make a checkable assertion, that is a WIKI problem to fix in step 6, not a sentence to invent in Python. Mirror `seed_drills.py` exactly: idempotent UPSERT, stale-prune, and REPORT anything it could not project rather than silently skipping it. Rubrics carry a `version` that bumps when the projected text changes, so a historical grade records which bar it was judged against (design §3).
  2. **Migration `0010` + models** for the rubric tables (`rubrics` + `rubric_items`, or justify a single table). Seed/content shape — no soft-delete, like `drills`/`concepts` — since a re-seed replaces. Raw-SQL `op.execute` mirroring `0004`–`0009`; reuse `update_updated_at()`; register in `models/__init__.py` AND `alembic/env.py`. Verify with `scratch_migrate.py` (extend its object lists).
  3. **Rubric API** — `GET /api/rubrics?drill_ref=` (+ concept lookup). Read-only: rubrics are seed content.
  4. **The SELF-CHECK — tier 2, and the thing that makes a rep "graded".** A `self_check` row in the EXISTING `evidence_grades` (the grader enum already has the value), carrying which items were ticked in `findings` plus `rubric_slug`/`rubric_version`. Decide and justify the ONE open question: **does an unchecked rep still count?** E2's lifecycle says a rep counts provisionally on upload and a grade may FLAG but never RETRACT — so a self-check almost certainly cannot un-count a rep, which means "ungraded" must be SURFACED (an honest backlog) rather than deducted. State the decision explicitly, and do not let E3 quietly make progress non-monotonic.
  5. **Self-check UI** on the capture surface — the drill's own bullets as checkable items, shown after a capture lands. Follow `lib/evidence.ts`'s invalidation idiom; a grade write must refresh whatever displays grading state.
  6. **THE TARGETED WIKI CONTENT PASS** (this is wiki editing — the wiki is canonical, so edit it and RE-SEED, never patch around it in code). Fix exactly the drills the design named: aura **D1-c** (`(reuses 50 ranges)` parses to a bogus 50-rep floor via the largest-number rule), aura **D2-d** `simple-first` / **D2-a** `1 triad + spot-check` / **D3-a** `per practice entry` / **D3-c** `per backtest batch` (no countable floor), ict **D3-d** (`Learned→applied` names no observable artifact), and the **4 aura Stage-0 drills the map table omits** (already reported as orphans by `seed_drills.py`). For each: state the problem, propose the minimal wiki edit, then re-seed and show the parse changed. **Rule #1 — `sources/` is immutable**; these are `concepts/mastery/**` pages, which are editable.

E3 IS NOT: any AI/vision grading or an `anthropic` dependency (E4); prediction capture, the calibration score, or wiring `ict_course` M6 / emptying `stages.STAGE_UNWIRED` (E5); gamification, XP, or the honesty-signal surfaces on /gate (E6); deploying or provisioning R2 (leave storage on local); re-opening the E2 decision that `reps` is derived; redesigning the shipped enforcement (the non-overridable Gate, the ladder-advance gate, the watch-only cap, logged skips, backtest≠live) — build ON those.

VERIFY (evidence, not inference — Paul's evidence-gated rule and the house standard from 5g / Phase 6 / E2):
  · `0010` up/down/up clean via `scratch_migrate.py`; working-DB seeds still 74/23/53/67 afterwards.
  · **The no-drift proof:** every rubric item's text appears VERBATIM in a wiki `exercises.md` bullet — assert it programmatically over the whole seed, not by eyeball. An item whose text is not in the wiki is a bug.
  · A wiki edit → re-seed → the rubric changes and its `version` bumps; re-running the seed twice is idempotent (no dupes).
  · A self-check grade attaches as an ADDITIONAL `evidence_grades` row (the deterministic row survives — grading is additive, never destructive).
  · **`reps` did not become easier OR harder to satisfy by accident** — E2's derivation is untouched; re-run the bypass test.
  · **THE NO-REGRESSION EVIDENCE GATE:** re-capture with `scripts/evidence_baseline.py` and prove byte-identical to STEP 0 (compare hashes). Rubrics must not move expectancy or the Gate.
  · Walk the design's §Invariants one by one and state each explicitly (§Walked at E2 is the format to follow).
  · `pytest` (report the new total vs 142) · `tsc -b` + `vite build` clean · `npx playwright test` (vs 45) with a new spec for the self-check flow.
  · A live claude-in-chrome walkthrough of the self-check surface with **NO console errors** — and remember E2's lesson: assert the RENDERED result, not just an attribute or an API response. `CORS_ORIGINS` allows only `http://localhost:5173`.

RECONCILE + BOOKKEEP (MANDATORY — wiki CLAUDE.md §Architecture Doc Integrity):
  · Update **concepts/architecture/learning-enforcement.md** with an "§E3 as-built" section recording every divergence, and mark the unchecked-rep decision from step 4 explicitly.
  · Update **concepts/architecture/learning-platform.md** §Progress data model + §Component/API surface with the new tables/endpoints/components.
  · The two `exercises.md` pages you edit are CANONICAL CONTENT — update them properly (frontmatter `updated:`), and note in [[concepts/mastery/README]] if a drill's bar materially changed.
  · In the tracker: mark Phase E3 ✅, add a Session Log entry (approach / decided / did / flagged / verified / next), and write the **E4 boot prompt**.
  · Append a row to `log.md`; bump `index.md`. Paul handles git — NEVER commit.
````

## Boot Prompt Archive (Phase E2 — evidence layer + capture) ✅ RUN 2026-07-28

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort high`**. Not because the code is
hard — the migration and the storage lift are mechanical — but because **one call in this phase decides
whether the whole workstream is real or theatre** (the `reps` / planner-bypass question in step 2), and
because this is the app's first user-supplied-file surface. Working dirs: `C:\Users\PaulRussell\repos\neurospect-learn`
(the build; **code is ground truth**) + `C:\Users\PaulRussell\repos\neurospect-wiki` (reconciliation).
**You need the DB running** (Docker `neurospect-learn-db`, local Postgres :5433) and the seeds present. Paste:

````
GROUNDING: `neurospect-learn` is Paul's standalone learn-to-execute app for the Neurospect ICT / Smart-Money-Concepts trading-mastery project — FastAPI + Postgres (`api/`) + React 19 / Vite / TanStack Query (`app/`). The whole Phase 5 arc and its Phase-6 debt are COMPLETE and shipped: curriculum + three graded tracks, Study Planner, model-aligned journal, expectancy, the computed non-overridable Readiness-to-Live Gate, the missed-trade log, and stage exit bars wired to real evidence. Migrations are at `0008`; seeds are 74 concepts / 23 track stages / 53 drills / 67 content pages; 114 backend tests + Playwright 36/36 green.

Neurospect — Phase E2 of the LEARNING-ENFORCEMENT workstream: BUILD the evidence layer + capture. The design is APPROVED — this is an EXECUTION session, not a design session. The problem it closes: every enforcement check the app ships today ultimately trusts a self-reported `reps` integer, and this phase makes a rep require EVIDENCE OF THE WORK.
Working dir: C:\Users\PaulRussell\repos\neurospect-learn  |  Wiki (reconcile at the end): C:\Users\PaulRussell\repos\neurospect-wiki

BOOT / CONTEXT — read in this order, and read the first two IN FULL:
1. The wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; no ALDC content or refs), Architecture Doc Integrity (code is ground truth; ONE canonical doc per topic; LINK the corpus, never restate it), the MANDATORY post-implementation reconciliation checklist, Rules #3 (index.md) #4 (log.md) #6 (flag contradictions), Context Management (tell Paul at >50%). Paul handles git — NEVER commit.
2. concepts/architecture/learning-enforcement.md — **the approved design you are building.** §1 evidence model (5 kinds), §2 the three grading tiers (E2 builds ONLY the deterministic tier), §4 lifecycle, §5 anti-cheat, §7 the `0009` data model, §8 storage, §Invariants (the 7-item checklist you must not break), §Implementation split (your scope is E2 and nothing beyond it).
3. processes/distributed-workflow/active/learning-enforcement.md — the tracker: §Decisions (the four forks Paul settled), §What already enforces the process (DO NOT redesign these), §Inherited debt (E2 closes two of the three).
4. concepts/architecture/learning-platform.md — the as-built app. Focus: §Progress + journal data model (§1 `concept_progress`, §2 the journal field set **+ its "screenshots still deferred" note, which YOU are closing**, §2b missed-trade log, §4 `drills`/`drill_progress` DDL), §Component/API surface, and as-built §5c (conventions + enum idiom), §5e-1 (the TWO real fixes: ON CONFLICT needs the partial-index predicate TEXTUALLY as `text("NOT is_deleted")`, and with `expire_on_commit=False` you must build the PATCH response from committed values, not a re-SELECT), §5e-2 (the `NULLS NOT DISTINCT` idempotency fix + the NullPool test-engine fix), §6 (the evidence-gate no-regression pattern you will repeat).
5. THE CODE TO REUSE, NOT REINVENT:
   - `C:\Users\PaulRussell\repos\neurospect\neurospect-api\app\services\r2.py` + `app\routers\screenshots.py` — a WORKING boto3 R2 client (`storage_key`/`upload_bytes`/`delete`/`presign`, module-level `r2 = R2Client() if settings.r2_endpoint_url else None`, and a `get_r2()` dependency that 503s when unconfigured) and a working multipart upload/list/delete router. Lift the shape; do not redesign it.
   - In `neurospect-learn`: `api/alembic/versions/0008_missed_trades_position_size.py` (the raw-SQL `op.execute` migration idiom + reversible downgrade), `api/app/models/drill_progress.py` (the user-scoped soft-delete model shape), `api/app/routers/learning.py` (`PATCH /api/drills` + the lazy-upsert idiom), `api/app/routers/planner.py` (`PATCH /api/plan/items/{id}` — **it also writes `drill_progress.reps`; see step 2**), `api/app/routers/missed_trades.py` + `api/app/schemas/missed_trade.py` (the CRUD idiom to mirror), `app/src/lib/{learning,missed-trades}.ts` (query-key + mutation-invalidation idiom), `app/src/components/drills/drill-card.tsx` (where capture lands).
6. `api/.env.example` — CANONICAL for env config. Add the storage vars here; reference, never duplicate.

STEP 0 — PROVE THE STARTING STATE before writing anything (evidence, not assumption):
`alembic current` == `0008 (head)`; the DB is up on :5433; seed counts are exactly 74 concepts / 23 track_stages / 53 drills / 67 content_pages; `pytest` == 114 passed; `npx playwright test` == 36 passed. If seeds are missing, re-run all seeds AND `ingest_content` before proceeding. Capture a BASELINE of `/api/analytics/expectancy|summary|r-distribution|missed-summary` and `/api/gate` for a fixture user to files — you will diff against these at the end.
⚠️ NEVER run `alembic downgrade base` against the working DB. An exported `DATABASE_URL` does NOT override the `.env`-derived settings Alembic reads (this has already wiped the seed twice — see §5e-2 as-built). Pin scratch reversibility tests to a throwaway DB by editing config, not by exporting an env var.

BUILD — in this order:

  1. MIGRATION `0009` + models. `evidence_assets` (user-scoped, soft-deleted) per design §7: `subject_type` enum + exactly one of `subject_drill_ref` (TEXT soft ref, matching the `drill_progress.drill_ref` convention — NOT a hard FK) / `concept_id` / `journal_entry_id` / `missed_trade_id`, enforced by a CHECK that FAILS CLOSED (a row with zero or two subjects must be rejected, and the CHECK must agree with `subject_type`). Plus `kind`, `storage_key`, `content_type`, `original_filename`, `byte_size`, `sha256`, `perceptual_hash`, `captured_at` (user-asserted), `reps_claimed`, `notes`. Child `evidence_grades` — ONE ROW PER GRADING PASS (a re-grade is additive, never destructive): `grader`/`state` enums, advisory `score`, `rubric_slug` + `rubric_version`, `findings` JSONB, model/token telemetry columns. Raw-SQL `op.execute` mirroring 0004–0008; reuse `update_updated_at()` (do NOT recreate it); partial indexes + partial-unique `WHERE NOT is_deleted`; a UNIQUE on `(user_id, sha256) WHERE NOT is_deleted` is the exact-duplicate block. Register both models in `models/__init__.py` AND import them in `alembic/env.py`. Verify up/down/up reversible on a SCRATCH DB.

  2. ⚠️ THE LOAD-BEARING CALL — HOW `reps` BECOMES EVIDENCE-BACKED, AND THE PLANNER BYPASS. `drill_progress.reps` and `concept_progress.reps` are written by TWO paths today: `PATCH /api/drills` + `PATCH /api/progress` (learning.py) AND `PATCH /api/plan/items/{id}` (planner.py, on mark-done). If you add an evidence precondition to the learning router only, **marking a plan item done becomes a bypass that mints reps with no evidence — and the entire workstream is theatre.** Decide, justify in the doc, and TEST both paths. Guidance from the design (§Invariants item 5): `reps` must get strictly HARDER to satisfy and never easier, so whichever shape you choose, a rep with no evidence must not be creatable by ANY endpoint. Deriving `reps` from `SUM(reps_claimed)` is the unfakeable option but changes a shipped write path; keeping the column with a precondition preserves the planner flow but needs the same gate applied in both routers plus a declared-vs-derived divergence signal. Prove whichever you pick with a test that attempts the bypass and fails.

  3. STORAGE SERVICE — `api/app/services/storage.py`. Lift the R2 client shape from `neurospect-api` AND add a LOCAL-FILESYSTEM backend so localhost needs NO bucket (Paul's decision #4: localhost is not a stopgap here, it is the primary path). Backend selected by config; the same interface either way. Key pattern `{user_id}/evidence/{subject_type}/{subject}/{uuid4}.{ext}`, extending the convention canonical in wiki `concepts/architecture/phase2-project-structure.md` §R2 Client. Env vars reuse the EXISTING names verbatim — `R2_ENDPOINT_URL`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET` — plus whatever local-backend var you add; document all of them in `.env.example`. Add deps: `boto3`, `Pillow`, `imagehash`. **`python-multipart` is ALREADY a dependency** — `UploadFile` needs nothing new.

  4. THE DETERMINISTIC TIER — the ONLY tier that blocks, and the only grading E2 builds. Magic-byte sniff (do NOT trust the client's `content_type` header), size bounds, SHA-256 exact-duplicate, perceptual-hash near-duplicate. This is a user-supplied-file surface: sanitize the filename (never build a path from it — `neurospect-api` uses `PurePosixPath(file.filename).suffix`), enforce the size cap BEFORE reading the whole body where you can, and serve reads only via presigned/short-lived URLs. A rejected upload must say WHY (duplicate vs not-an-image) — a silent refusal is the failure mode this workstream exists to avoid.

  5. ENDPOINTS — auth-gated + user-scoped + soft-delete, mirroring `routers/missed_trades.py`: `POST /api/evidence` (multipart: file + subject + kind + `reps_claimed` + optional `captured_at`/`notes`), `GET /api/evidence` (filter by subject), `GET|DELETE /api/evidence/{id}`. Schemas in `app/schemas/evidence.py`; response carries a presigned/served URL. Mount in `main.py`.

  6. CLOSE THE TWO INHERITED DEBTS IN THIS PHASE — do not defer them again. The journal's deferred screenshots (5c) and `missed_trade_screenshots` (deliberately omitted from `0008`) attach to the SAME `evidence_assets` layer via `subject_type`. Wire both: attach-evidence on `/journal/:id` and `/journal/missed/:id`. This is the whole reason the design chose one polymorphic table over `neurospect-api`'s per-owner child tables.

  7. FRONTEND — **paste-first capture** (Paul's decision #4). A `paste` handler on the drill card reading `ClipboardEvent.clipboardData.files` so `Ctrl+V` straight from a TradingView snapshot works, PLUS drag-and-drop and a file input as fallbacks. Show the captured thumbnail, the rep it counted, and any rejection reason inline. `app/src/lib/evidence.ts` following the `evidenceKeys` hierarchical-key + invalidate-on-write idiom in `lib/learning.ts` — **an evidence write must invalidate the progress/drills/stages subtrees**, since it now moves reps.

E2 IS NOT: the self-check rubric or `seed_rubrics.py` (E3); ANY AI/vision grading or `anthropic` dependency (E4); prediction capture or the calibration score (E5); gamification, XP, or the honesty-signal surfaces on /gate (E6); deploying anything or provisioning a real R2 bucket (a separate, already-runbooked workstream — build the backend switch, leave it on local); editing the drill libraries (E3); redesigning the shipped enforcement (the non-overridable Gate, the ladder-advance gate, the watch-only cap, logged skips, backtest≠live) — build ON those.

VERIFY (evidence, not inference — this is Paul's evidence-gated rule and the house standard from 5g/Phase 6):
  · `alembic upgrade head` 0008→0009 clean; `downgrade 0008` and back up clean on a SCRATCH DB (tables, both enum types, every index and trigger dropped and recreated); the 74/23/53/67 seeds still intact on the working DB afterwards.
  · The CHECK fails closed — a zero-subject row and a two-subject row are both REJECTED by the DB, not just by Pydantic.
  · Duplicate detection works: the same file twice is refused with a reason; a visually-near-identical crop is caught by the perceptual hash.
  · **THE BYPASS TEST** — a rep cannot be minted with no evidence through `PATCH /api/drills`, `PATCH /api/progress`, OR `PATCH /api/plan/items/{id}`. Assert all three.
  · **THE NO-REGRESSION EVIDENCE GATE (repeat the Phase-6 pattern):** re-capture `/api/analytics/*` + `/api/gate` for the fixture user and prove them **byte-identical** to the STEP 0 baseline (compare file hashes) — an evidence layer must not move expectancy or the Gate. Land it as a durable pytest too, so it cannot silently rot.
  · Walk the design's 7 §Invariants one by one and state each explicitly. Especially: `reps` is strictly HARDER, never easier; `auto_met`/`locked` unchanged; no `cleared` column or write path added anywhere near the Gate.
  · Per-user isolation (a second user sees none of the first's evidence); no-token → 403; local storage backend works with NO R2 config set.
  · `pytest` (report the new total vs 114) · `tsc -b` + `vite build` clean · `npx playwright test` (report the new total vs 36) with new specs for paste-capture, the duplicate refusal, and evidence→reps.
  · A live claude-in-chrome walkthrough of the changed surfaces (drill card paste → thumbnail → rep increments; a duplicate refused with its reason; journal + missed-trade attach) with **NO console errors**. Note: the API's `CORS_ORIGINS` allows only `http://localhost:5173`, so the dev server must run on :5173.

RECONCILE + BOOKKEEP (MANDATORY — wiki CLAUDE.md §Architecture Doc Integrity):
  · Update **concepts/architecture/learning-enforcement.md** to describe E2 **as-built** — add an "§E2 as-built" section recording every divergence from this design, and mark the `reps` decision from step 2 explicitly as the load-bearing call it is.
  · Update **concepts/architecture/learning-platform.md**: §2's "Screenshots / uploaded evidence: still deferred" note and §2b's omitted-`missed_trade_screenshots` note are now CLOSED — say so and link the enforcement doc. Add the new tables/endpoints/components to §Progress + journal data model and §Component/API surface.
  · `concepts/architecture/trade-schema.md` §Missed Trades still specs a `missed_trade_screenshots` child table that this design deliberately does NOT build. That doc is the journal-analytics lane's canonical page — **FLAG the contradiction for Paul (Rule #6), do not edit it from this session** (the same call §Contradiction flag made for phase3-frontend-structure).
  · In the tracker: mark Phase E2 ✅, add a Session Log entry (approach / decided / did / flagged / verified / next), and write the **E3 boot prompt**.
  · Append a row to `log.md`; bump `index.md` (`last_build`, the architecture lines, the workstream line).
  · Paul handles git — NEVER commit.
````

## Boot Prompt Archive (Phase E1 — deep research + design) ✅ RUN 2026-07-28

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort xhigh`**, in **plan mode** — the reasoning
*is* the bottleneck here: this one design carries a multi-phase workstream, and the grading-mechanism call decides
cost, latency and whether the app grows an LLM dependency. **No app code this session.** Working dir:
`C:\Users\PaulRussell\repos\neurospect-wiki` (the design doc lives here; the app to design against is
`C:\Users\PaulRussell\repos\neurospect-learn`, where **code is ground truth**). No DB or dev server needed — this
session reads code, it does not run it. Paste:

````
GROUNDING: Neurospect is Paul's personal ICT / Smart-Money-Concepts trading-mastery project, and `neurospect-learn` is its standalone learn-to-execute app — a FastAPI + Postgres backend (`api/`) and a React 19 / Vite / TanStack Query SPA (`app/`) — that surfaces the wiki's course corpus and tracks his progress up the mastery ladder (learn → backtest → live) toward being cleared to trade live. The whole Phase 5 arc plus its Phase-6 debt is COMPLETE and shipped: curriculum + three graded tracks, Study Planner, model-aligned journal, expectancy, the computed Readiness-to-Live Gate, the missed-trade log, and stage exit bars wired to real evidence. Migrations are at `0008`.

Neurospect — Phase E1 of the LEARNING-ENFORCEMENT workstream: a DEEP-RESEARCH + DESIGN session, in plan mode. THE PLAN IS THE ARTIFACT. The problem in one line: every enforcement check the platform ships today ultimately trusts a self-reported `reps` integer and a self-rated confidence — so design the layer that makes a rep count only when there is EVIDENCE OF THE WORK, graded, and gamify the loop so it drives consistency.
Working dir: C:\Users\PaulRussell\repos\neurospect-wiki  |  App to design against (code = ground truth): C:\Users\PaulRussell\repos\neurospect-learn

BOOT / CONTEXT — read in this order, and read the first three IN FULL:
1. The wiki CLAUDE.md — Isolation Rule (Neurospect ONLY; NO ALDC content or refs), Architecture Doc Integrity (code in `neurospect-learn` is ground truth; ONE canonical doc per topic; LINK the corpus, never restate it), plan-mode discipline (present the plan for approval BEFORE writing any page), Rules #3 (index.md) #4 (log.md) #6 (flag contradictions), Context Management (tell Paul at >50%). Paul handles git — NEVER commit.
2. processes/distributed-workflow/active/learning-enforcement.md — THIS workstream's tracker. It is not a blank page: it already holds Paul's goal in his own words, the SHARPENED NORTH STAR (**the adversary is self-deception, not an attacker** — make the honest path the path of least resistance, and make any shortcut VISIBLE rather than silently absorbed; a design that merely frustrates honest work fails just as badly as one that lets a rep be faked), §What already enforces the process (DO NOT redesign these), §The honest gap, **14 numbered open questions you must answer**, §Scope boundary (content vs app), and §Inherited debt this workstream owns.
3. concepts/architecture/learning-enforcement.md — **if it exists**, it is your canonical doc and you EXTEND it. If it does not (expected on the first run), you will create it.
4. concepts/architecture/learning-platform.md — the as-built app you are extending. Focus: §Progress + journal data model (§1 concepts/`concept_progress`, §2 the journal field set, **§2b the missed-trade log**, §3 the gate, §4 the planner + `drills`/`drill_progress` DDL), §Stage exit-bar derivation (**incl. `stages.STAGE_UNWIRED` — the M6 case handed to you**), §Component/API surface, and the as-built sections §5b (**note: `boto3` was DROPPED in the 5b lift — there is NO object-storage layer in this app today**), §5e-1, §5f, §5g, §6.
5. The CURRICULUM the rubrics must DERIVE FROM (consume + link; NEVER restate or fork): concepts/mastery/README (the ladder Learned→Can-mark→Backtested→Live-ready = 1–4, the 1–5 confidence scale, the Readiness-to-Live Gate), the three per-track learning-paths (unified/learning-path, aura/learning-path, course/README) for the exit bars, and **concepts/mastery/aura/exercises.md + concepts/mastery/ict-course/exercises.md IN DETAIL** — the drill definitions and the "Drill → concept → ladder-stage map" tables at their foot are what seeded the 53 `drills` rows, and they are the raw material a grading rubric has to come from. Also skim the entry-model pages for the per-model checklists.
6. The SHIPPED ENFORCEMENT CODE, so the design is buildable against it and does not re-invent it: `api/app/routers/learning.py` (the `PATCH /api/progress` ladder-advance gate + the watch-only cap + `load_stage_evidence`), `api/app/services/stages.py` (the exit-bar service + the 6a evidence maps + `STAGE_UNWIRED`), `api/app/services/gate.py` (the non-overridable verdict), `api/app/models/{drill,drill_progress,concept_progress}.py`, `api/app/routers/planner.py` (`_adherence` — streak / adherence / days-behind / skips), `api/alembic/versions/{0004_drills_progress.py,0008_missed_trades_position_size.py}` (the raw-SQL migration idiom you will follow), and on the frontend `app/src/lib/{learning,missed-trades}.ts` + `app/src/components/{progress,journal}/*` (the mutation + form idioms). Note the app has NO file-upload path anywhere today.

OBJECTIVE
Design the enforcement layer end to end and split it into buildable phases. Answer ALL 14 open questions in the tracker — or explicitly defer one WITH a reason (an unanswered question silently dropped is the failure mode). Decide and justify, in the plan, at least:

  0. PHASE SPLIT + SEQUENCING (E2, E3, …) — each a boot-promptable unit, and each honouring §Scope boundary: WIKI/content work (making a drill's bar gradable) is a different kind of work from APP work (capture, grading, anti-cheat, gamification). The tracker's hypothesis is that the CONTENT PASS has to lead, because a drill can only be graded if its wiki definition states a gradable bar — confirm or overturn that, with reasons.
  1. THE EVIDENCE MODEL — what IS a unit of evidence (per rep? per session? per concept?), and what it means for each `rep_targets` kind the shipped parser already distinguishes (reps / days / sessions / qualitative / habit — read `api/app/services/rep_targets.py`). A "1 week" habit target cannot take a screenshot per rep.
  2. THE GRADING MECHANISM — the load-bearing call. EVALUATE the candidates rather than assuming one: AI vision grading (Claude, against a per-concept rubric), a structured self-check rubric, deterministic/heuristic checks, human-in-the-loop, or an escalating hybrid. Cost the realistic option: per-rep vision calls across ~50-rep targets × 53 drills is a real token bill and a real latency budget — state the numbers you are assuming. Weigh the FALSE-NEGATIVE COST explicitly: a wrongly rejected rep is the fastest way to make Paul abandon the tool, and that outcome fails the north star exactly as hard as a fakeable rep.
  3. RUBRIC PROVENANCE — where a per-concept rubric comes from (it must be DERIVED from the wiki bars in step 5, never invented alongside them) and where it LIVES (a wiki page the ingest consumes? a seed column? a new table?). Apply the no-drift rule: one source of truth for "what good marking looks like".
  4. GRADING LIFECYCLE — blocking (a rep does not count until graded) vs asynchronous (provisional, confirmed later); what happens when grading fails or the machine is offline; whether a grade carries a SCORE that feeds confidence/ladder position or is pass/fail; and whether a provisional rep may satisfy a stage exit bar (careful: `stages.py` and the Gate consume `reps`).
  5. THE ANTI-CHEAT SET — which shortcuts to CLOSE vs merely SURFACE. Candidates: duplicate/recycled images (perceptual hashing), implausible rep pacing, non-chart uploads, back-dating, bulk marking. Per the north star, "surfaced and recorded" is often the right answer and always better than silently absorbed. Decide the appeal/override path — and say plainly whether it reopens the hole the Gate deliberately has no override for.
  6. GAMIFICATION — the mechanics that actually drive consistency for a SOLO learner (there is no leaderboard in a single-user app), grounded in the research from the RESEARCH step, not in vibes. Design against the killer failure mode: mechanics that reward ACTIVITY over MASTERY would actively undermine the Gate. Say what keeps the points honest, and how they compose with the ALREADY-SHIPPED streak / adherence / days-behind / pace surfaces without double-counting them.
  7. DATA MODEL — new tables + enums + a DDL sketch (Alembic `0009`+), reusing the shipped conventions exactly (UUID PK · TIMESTAMPTZ · `update_updated_at()` trigger · user-scoped · soft-delete + partial unique `WHERE NOT is_deleted`; raw-SQL `op.execute` mirroring 0004–0008). It MUST serve the inherited debt too — the journal's deferred screenshots AND `missed_trade_screenshots` are the same primitive, so design ONE evidence layer that all three consumers attach to; do not design a drill-only table that the journal then has to duplicate.
  8. STORAGE + PLATFORM — object storage (R2 is already in the wider Neurospect stack; `boto3` was dropped from THIS app in 5b so it is a genuinely new dependency): key pattern, size/format limits, retention, cost, and the privacy of chart screenshots. Name the new env vars for `.env.example` (which is canonical for env config per the wiki CLAUDE.md — reference it, don't duplicate it).
  9. THE M6 CASE — `ict_course` M6's exit bar (13 tape studies T-01…T-13 + a blind live-read T-14) is the ONE stage requirement Phase 6 deliberately left self-attested, precisely because "a drill is done" is yours to define. Decide what evidence makes those 14 count, and what `stages.py` reads to grade it. This is your concrete acceptance test: your design should make `STAGE_UNWIRED` empty.
  10. DEPLOY DEPENDENCY — if capturing a marked chart realistically means uploading from a phone/tablet, hosting stops being someone else's problem and becomes a PREREQUISITE. Deploy/hosting is currently unscoped in EVERY tracker. Do not silently assume localhost: state the assumption, and if it is a blocker, say so loudly and put it to Paul.

RESEARCH (this is a research session — do it properly, then let it constrain the design)
Use WebSearch/WebFetch for genuine external research on: (a) what actually drives consistency and retention for a solo adult learner — spaced/interleaved practice, deliberate practice with feedback, self-explanation — AND the counter-evidence that extrinsic rewards (points, badges, streak pressure) can crowd out intrinsic motivation and warp behaviour toward the metric; (b) how comparable skill platforms VERIFY that work was really done (language, coding-practice, music-practice, chess-training tools) — what they check, what they only nudge, and where users report the friction becomes quitting-level; (c) the feasibility of vision-model grading of annotated price charts — prompt/rubric patterns, known failure modes, calibration, and how to bound false rejections.
Discipline on sources, matching how this wiki already treats evidence (see the mastery workstream's TIER convention): prefer PRIMARY sources; label a claim you could not verify as unverified rather than promoting it; NEVER let a vendor's marketing claim become a design premise. Cite what you used in the doc's frontmatter `sources:` and inline where a decision rests on it. If the research contradicts something in the tracker's framing, say so (Rule #6) instead of quietly designing around it.

PUT TO PAUL BEFORE FINALIZING (AskUserQuestion, the house pattern for load-bearing forks — ask BEFORE you write the doc, not after)
At minimum: (1) the GRADING MECHANISM — it decides cost, latency and whether the app gains an LLM dependency; (2) BLOCKING vs ASYNCHRONOUS grading; (3) HOW HARD ANTI-CHEAT SHOULD BITE — block the shortcut vs surface it; (4) the DEPLOY/MOBILE question from step 10. Give Paul a recommendation with each, not just a menu.

E1 IS NOT: writing any app code (nothing in `neurospect-learn` is touched this session); building the storage layer or the upload endpoint; EDITING the drill libraries yet (E1 IDENTIFIES which drills are weak/ambiguous/ungradable as written — question 14 — and the content phase fixes them, unless your plan argues otherwise and Paul approves); redesigning the enforcement that already ships (the non-overridable Gate, the ladder-advance gate, the watch-only frontier cap, logged skips, backtest≠live) — build ON those; deploy/hosting itself (flag it as a dependency, don't scope it); ALDC anything.

VERIFY (a design session's verification is DOC INTEGRITY, so state each of these explicitly before sign-off)
Isolation clean (Neurospect only; no ALDC refs — the distributed-workflow pattern docs stay absolute paths, never wikilinks). No-drift honoured: the design LINKS the mastery corpus and the drill libraries, and restates neither. **No shipped invariant is weakened** — walk them one by one and say so: the Gate stays non-overridable and computed-per-read, frontier/watch-only concepts stay never-gate-eligible, skips stay logged, backtest and live stay unconflated, and `reps` cannot become EASIER to satisfy than it is today. All 14 open questions answered or explicitly deferred with a reason. Every proposed phase is boot-promptable (a fresh session could execute it from the tracker alone). No app code written.

RECONCILE + BOOKKEEP (mandatory)
Create the ONE canonical doc **concepts/architecture/learning-enforcement.md** (frontmatter with tags/aliases/sources/created/updated; if you conclude this belongs inside learning-platform.md instead, justify the one-doc-vs-two call against the drift rule before choosing). Add it to the **Canonical doc per topic** table in the wiki CLAUDE.md — it is a new topic. Add additive cross-links from concepts/architecture/learning-platform.md and concepts/mastery/README (link only; do not restate). In this tracker: mark Phase E1 ✅, replace the "Phases E2+ — TBD by E1" stub with the real phase list, add a Decisions block for Paul's AskUserQuestion answers, and add a Session Log entry (approach / decided / did / flagged / verified / next). Append a row to log.md and bump index.md. Write the E2 boot prompt only when E2 starts — not now. Paul handles git — NEVER commit.
````

## See Also

- [[concepts/architecture/learning-enforcement]] — **this workstream's canonical design doc** (E1 output: the
  evidence model, the three grading tiers, rubric provenance, anti-cheat, gamification, the `0009` data model)
- [[processes/distributed-workflow/active/learning-platform-ui]] — the completed Phase 5 workstream this builds on
- [[concepts/architecture/learning-platform]] — the canonical app architecture (as-built through 5g)
- [[concepts/architecture/phase2-project-structure]] — the R2 client + storage key pattern E2 reuses (canonical)
- [[processes/distributed-workflow/active/deployment]] — the proven hosting runbook (a later, separate workstream)
- [[concepts/mastery/README]] — the mastery ladder, confidence scale, and Readiness-to-Live Gate (canonical)
- [[concepts/mastery/aura/exercises]] · [[concepts/mastery/ict-course/exercises]] — the two drill libraries the
  grading rubrics must derive from
- [[concepts/aura/journaling-system]] — the journaling discipline the enforcement loop is meant to instil
