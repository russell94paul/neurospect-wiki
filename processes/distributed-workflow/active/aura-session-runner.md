---
tags: [distributed-workflow, active, neurospect, neurospect-learn, aura, backtesting, tradezella, session-runner, practice]
aliases: [Session Runner, Aura Runner, Backtest Runner, The Runner]
sources: []
created: 2026-08-12
updated: 2026-08-12
---

# Aura Session Runner — Workstream Tracker

Give Paul **a screen he can keep open beside Tradezella** that walks the Aura model the same way every
time: how to set the session up, what to mark on the chart, what to check before and at each entry, what
to tag, and how to review afterwards. The point is **repetition until the protocol is automatic** — not
another dashboard to read.

> **STATUS (2026-08-12): SCOPED, decisions taken, no code written.** Phase **S1 ⏭ ACTIVE** (boot prompt at
> the bottom). Nothing in this document is a finding about the Aura model or about Tradezella; the model
> content it projects is canonical elsewhere and must not be re-derived here.

## Goal (Paul, 2026-08-12 — in his framing)

> "I want a section that creates a guide/platform for practicing/backtesting using the Aura Model in
> tradezella, it should give the user the strategy/model checklist for each day/entry, but also give
> detailed steps of how to set up their session in tradezella, what data to track/tag, what exactly to
> mark out on each chart (or indicators to use that will mark out all our levels on our chart)."
>
> "I want a screen I can have open when doing backtesting in tradezella that i can follow over and over
> that will get me used to the steps and rules of the strategy."
>
> "I think once this is implemented I will be able to use it with tradezella from tomorrow onwards.
> because right now I have only been building and testing the app with you, not actually using it."

That last sentence is the most important line in this tracker. **The platform has never been used for real
practice.** Every number in E1–E6 came from fixtures. This workstream exists to change that.

## ⭐ Why this unlocks B2 rather than bypassing it

[[processes/distributed-workflow/active/backtest-companion]] §COUNCIL VERDICT gates everything behind
**B2**: *define rules in the Tradezella Playbook → Rules tab and run ~20 backtesting sessions using the
in-product fields that already exist.* B2 has never been run, and the council's `DON'T BUILD` verdict
rested on three free Tradezella discipline instruments reading **genuine ZERO**.

Read the basis of that ZERO carefully, because it changes what this workstream is:

- The measurement was honest but **thin**: `2 sessions, 1 trade, 8 minutes`. The instrument was proved
  live (a trade completed, so the fields rendered), so `ZERO` and not `NOT-RECORDED` was the correct
  verdict **for that window**.
- But the same section records the reason nothing was captured: **"with zero rules defined."**

So B2 asks Paul to run twenty sessions against rules that **were never written into Tradezella**. The gate
is not blocked on his discipline; it is blocked on a **missing instrument**. This workstream builds that
instrument — the rules, made followable and taggable — which is precisely B2's unstated prerequisite.

**This does not overrule the council.** S1 deliberately writes **nothing** to `neurospect-learn`'s
database: capture during S1 happens in **Tradezella's own fields**, which *is* B2's free test. If twenty
sessions still come back empty, the council's verdict stands and S2 must not be built. S1 makes the gate
runnable without prejudging its outcome.

## The asset this workstream projects — do NOT re-author it

The model content already exists, wiki-canonical, and this workstream is a **projection** of it — the same
pattern the rubric layer already uses (wiki-projected, read-only). Treat these two files as the source of
truth and the app as a view over them:

- **[[concepts/mastery/aura/checklist.md]]** (134 lines) is *already* session-shaped, and its phases are
  the runner's spine:

  | Phase | Rules |
  |---|---|
  | 0. Pre-market — readiness | R47–48, R54 |
  | 1. HTF framing — top-down cascade | R27–29 |
  | 2. Confirmation — Sequential SMT | R18–R25 |
  | 3. Entry | R30–R34 |
  | 4. In-trade management | R35, R45 |
  | 5. Exit | R35–R36 |
  | 6. Circuit-breaker checkpoints (any time) | R40–R42, R49–R50 |
  | 7. Post-market review | R53 |

  It also already contains a **"Per-Trade Card (copy one per setup)"** — which is exactly Paul's
  "checklist for each day/entry" — and a **"Fitness check — checklist vs. a real worked trade"**.

- **[[concepts/mastery/aura/rules.md]]** (215 lines) holds the numbered rules the phases cite, grouped
  **A** structural primitives · **B** confirmation engine · **C** execution · **D** risk (non-negotiable)
  · **E** psychology & discipline.

⚠️ **`rules.md` ends with §"Divergences & open flags (do not silently resolve)".** The runner must surface
those as open flags, **not** quietly pick a side to make a checkbox render. Flattening a known divergence
into a confident instruction would be the worst failure available to this workstream.

## What genuinely does not exist yet, and must be authored

Three pieces, none of which the wiki currently holds. This is the real work of S1:

1. **Tradezella session setup steps** — the exact click-path to start a comparable backtest session every
   time (instrument, timeframe, replay range, session window), so runs are consistent enough to compare.
2. **The tagging scheme** — a mapping from Aura rule IDs to Tradezella's own fields: `Custom Tags`,
   `Mistakes`, `Rating`, `Reviewed`, and the Backtesting Session Notes folder. **This is literally B2's
   "define rules in the Playbook Rules tab" step**, and it is the deliverable that makes B2 measurable.
   Design it so a tag maps back to a rule ID unambiguously — that is what turns twenty sessions into data
   rather than anecdote.
3. **The chart markup protocol** — what to draw on every chart, in what order, so the same setup looks the
   same twice. Gated by the probe below.

## ⚠️ The boundary probe that gates piece 3 — run it FIRST

Paul asked for *"what exactly to mark out on each chart (or indicators to use that will mark out all our
levels)"*. Whether that is a **manual drawing protocol** or a **tooling spec** depends on a fact nobody has
measured: **what Tradezella's backtesting chart actually permits.**

Establish, by looking rather than by assuming — this project's own rule is that **a vendor claim is never a
design premise**:

- Can you add indicators to the backtest chart at all? Custom ones?
- Do drawings persist across replay steps, and across sessions? Can a drawing template be saved and reused?
- Is the chart a TradingView widget or Tradezella's own engine? **Do not assume Pine works.** The older
  `neurospect-app` shipped a Pine script (`public/neurospect-coach.pine`), so Pine is a known in-house
  capability — but Tradezella ≠ TradingView, and inheriting that assumption is exactly the kind of
  premise this project has been burned by.

**If the chart takes no custom levels**, piece 3 becomes a written markup protocol plus a decision about
whether markup happens in TradingView (where bar-replay drills already live) and Tradezella is used only
for logging. Say so loudly if the probe forces that, because it changes the shape of the session.

## Where this lives in the app

**A new top-level section.** Recommended, and the reason is shape, not taste: every existing page — Today,
Path, Library, Drills, Plan, Journal, Expectancy, Gate — is a **dashboard you read**. This is a **runner
you follow**, live, in a narrow window docked beside another application, returned to dozens of times in
one session. Bolting it onto Drills or Today would compromise both surfaces.

**Design constraints, all non-negotiable:**

- **Narrow-viewport first.** It will live in perhaps a third of a screen, beside Tradezella. If it only
  works maximised, it has failed its only job. Verify at a narrow width, not just at 1568px.
- **Wire into existing primitives; never build a parallel data model.** This is B4's question Q11
  (*"a new data model or a new source for the existing one?"*) and the answer is **source**:
  pre-commitment → the **E5 frozen ledger** (`predictions`); per-trade capture → `journal_entries` with
  the **existing** `mode='backtest'`; adherence → the rubric layer; evidence → `evidence_assets` (E2).
- **S1 writes nothing.** No migration, no new table, no endpoint that mutates. A read-only projection
  cannot corrupt the evidence layer, and that is why it ships first.
- **Rubrics and rules stay wiki-projected and read-only** (the E3 invariant). The app must not become a
  second home for model content that can drift from the wiki.

## Plan

### S1 — The read-only runner. Ships first, usable immediately. ⏭ **ACTIVE**

Project `checklist.md` + `rules.md` into a followable session surface, and author the three missing pieces
above. **No database writes, no new tables, no capture wiring.** Paul captures into Tradezella's own
fields — which is B2. Decided 2026-08-12 in preference to building capture first, because the binding
constraint is *starting to practise*, and a v1 that slips across three sessions means tomorrow does not
happen.

### S2 — Capture-first. **Absorbs B4** from the backtest-companion tracker.

Decided 2026-08-12: B4 (*"Capture in `neurospect-learn` FIRST, not imported after"*) **becomes S2** rather
than running as a parallel phase — two trackers describing overlapping work is how the B3b misdirection
happened. B4's constraints carry across intact:

- A **pre-session pre-commitment** in the frozen E5 ledger, authored *before* the replay is advanced — the
  one artifact whose ordering can be trusted, because `neurospect-learn` stamps it.
- **Consistency across similar setups** — one rubric, many captures, variance in cue usage (`CI`).
  Interleaved presentation, per Brunmair & Richter 2019 (`META`, g = .67 for visual category induction).
- Tradezella stays the **execution surface**; nothing is imported.
- ⚠️ **The two-clock finding is a design input here, not a bug to swat.** The planner counts "today" in
  the user's timezone (`study_preferences.timezone`, default `"UTC"`) while migration `0012`'s trigger
  enforces server UTC. A pre-commitment **is a claim about ordering in time**, so S2 cannot dodge choosing
  a clock the way earlier phases could. Changing it touches E6 semantics.
- If backtest-derived data is ever imported it must be permanently and visibly quarantined as
  `SELF-REPORTED` and excluded from the evidence streak, the calibration score and the Readiness Gate
  (`devil`'s criterion #2).

**S2 is gated on S1 + real sessions.** Do not design the capture surface before Paul has run the protocol
and can say which steps he actually kept.

### S3 — Review and insight across sessions (not yet scoped)

Only meaningful once S1 has produced sessions and S2 has captured them. Left deliberately thin.

## Open questions for S1 (answer or defer with a reason)

1. What is "one session"? A fixed replay range, a fixed number of setups, or a fixed clock duration? This
   is the counting basis, and per the estate rule it must be **declared before** any number is produced.
2. Does the runner track position within a session (step 3 of 8), and if so, where does that state live
   given S1 writes nothing? (`localStorage` is a legitimate answer; say so explicitly if chosen.)
3. One runner, or one per track? The Path has three (Aura / AXL / Unified) and this workstream is
   Aura-only by name. Does the surface generalise later, or stay Aura-specific?
4. How does the per-trade card repeat without losing the day-level framing above it?
5. Which of the 8 phases are per-session versus per-entry? Paul asked for "each day/entry" — the checklist
   mixes both, and the runner has to make that split explicit.

## Session Log

### 2026-08-12 — workstream created (scoping + decisions only; no code)

- approach: opened at the end of the B3-local closeout session, from Paul's own framing. Grounded the
  scope by reading the actual Aura content rather than designing against a guess.
- **found (the finding that shaped everything): the model content already exists.**
  `concepts/mastery/aura/checklist.md` is already an 8-phase session checklist with a per-trade card, and
  `rules.md` already holds R18–R54 grouped A–E. So this workstream is a **projection**, matching the
  existing wiki-projected rubric pattern — not new content authoring, and far smaller than it first read.
- ⭐ **found: this unlocks B2 rather than bypassing it.** The council's `DON'T BUILD` rested on three free
  Tradezella instruments reading genuine ZERO — but that was measured against **2 sessions, 1 trade, 8
  minutes**, and the same section records **"with zero rules defined."** B2 asks for twenty sessions
  against rules that were never written into Tradezella. The gate was blocked on a missing instrument, not
  on Paul's discipline. Recorded so no future session reads this workstream as overruling the council.
- **decided (S1 scope): read-only runner first**, no DB writes, capture into Tradezella's own fields.
  Rationale: the binding constraint is *starting to practise*, and S1 cannot corrupt the evidence layer.
- **decided: B4 is absorbed as S2**, and its boot prompt retired unrun — one lane, not two overlapping ones.
- **decided: a new top-level app section**, narrow-viewport-first, wiring into E5 / `journal_entries`
  (`mode='backtest'`) / the rubric layer rather than any parallel data model.
- **flagged — a boundary fact gates the chart-markup piece and has NOT been measured:** what Tradezella's
  backtest chart permits (custom indicators? persistent drawings? saved templates? TradingView widget or
  own engine?). **Pine must not be assumed to work** just because the older `neurospect-app` shipped a Pine
  script. S1 runs this probe before designing markup.
- **flagged — `rules.md` §"Divergences & open flags (do not silently resolve)"** must surface as open flags
  in the runner. Flattening a known divergence into a confident checkbox is this workstream's worst
  available failure.
- next: **S1** — boot prompt below.

---

## Boot Prompt (Phase S1 — the read-only Aura session runner) ⏭ ACTIVE

**Launch:** `claude --model opus[1m]`, `/effort high`. This phase contains real design work (the session
protocol, the tagging scheme, the runner's information architecture) and authors content Paul will practise
against for months. Do not economise on the design; do economise on the build, which is deliberately small.

**Task: build a screen Paul can keep open beside Tradezella and follow, start to finish, every session —
and have it usable at the end of this session.**

**State, exactly.** Nothing is built. The model content **already exists** and must be projected, not
re-authored (`concepts/mastery/aura/checklist.md`, `concepts/mastery/aura/rules.md`). Three pieces do not
exist and are yours to author: Tradezella session setup steps, the rule→tag mapping, and the chart markup
protocol. `neurospect-learn` runs locally via `docker compose up -d` (:8001 API / :5174 UI, DB :5433);
hosting is parked. **S1 writes NOTHING to the database** — no migration, no new table, no mutating
endpoint.

READ FIRST:
1. The wiki `CLAUDE.md` — **code is ground truth**, the MANDATORY post-implementation reconciliation
   checklist, Rules #3/#4/#6, Context Management (tell Paul at >50%). **Paul handles git.**
2. This tracker in full — especially §"Why this unlocks B2", §"The asset this workstream projects",
   and §"The boundary probe that gates piece 3".
3. `concepts/mastery/aura/checklist.md` and `rules.md` — **the source of truth for every rule and phase
   the runner shows.** Read them completely before designing the surface.
4. [[concepts/architecture/learning-enforcement]] §Invariants — S1 touches none of them, and must not.
5. `neurospect-learn/api/docs/evidence/b3-local/b3-local-render-walk.md` — how to run and verify the local
   stack, and the three UI paths still unverified.

⚠️ **Run the Tradezella chart probe BEFORE designing the markup step.** Ask Paul to look, or walk him
through looking — the session cannot log into his Tradezella account. If the chart takes no custom levels,
**say so and redesign that step openly** rather than shipping instructions that cannot be followed.

⚠️ **Ask Paul for the session-setup facts you cannot observe.** The exact instrument, timeframe, replay
range and session window he intends to practise are *his* decisions, not the session's to invent. A
protocol built on guessed settings is worse than no protocol, because he will follow it.

**Non-negotiables:**
- **Project, do not re-author.** If the runner and `rules.md` disagree, `rules.md` wins and the runner is
  wrong. Do not paraphrase a rule into something crisper — the wording is canonical.
- **Surface `rules.md`'s divergences as open flags.** Never silently resolve one to make a checkbox work.
- **Narrow viewport is the primary target**, not an afterthought. Verify at roughly a third of a screen.
- **No new data model, no writes.** If step state must persist, `localStorage` is acceptable — state that
  choice explicitly in the docs.
- **Never `docker compose down -v`** (the volume is `external: true` as of 2026-08-12, which is what makes
  that survivable — do not undo it). Never `alembic downgrade base`; use `scripts/scratch_migrate.py`.
  Do not trust `--reload`. `VITE_*` are **build args**, not `environment`.

DELIVERABLES:
1. The runner, reachable as a **new top-level section**, projecting all 8 checklist phases with their rule
   references, plus the repeating per-trade card.
2. The three authored pieces, written into the **wiki** (canonical) and projected into the app: session
   setup steps, the **rule→Tradezella-tag mapping** (the piece that makes B2 measurable), and the chart
   markup protocol — with the probe's actual result recorded, including a negative one.
3. **Render-verified at a narrow viewport**, with labelled screenshots into
   `neurospect-learn/api/docs/evidence/s1/`, and a written note of which interactions respond and **which
   are inert**. Five phases running have each caught a defect only the rendered surface showed.
4. Answers to §"Open questions for S1", or an explicit deferral with a reason — especially **Q1, the
   definition of one session**, which is the counting basis and must be declared before any number exists.
5. Tracker + `log.md` + `index.md` reconciled, including every divergence from this prompt — then the S2
   boot prompt, carrying the two-clock finding.
6. **Then tell Paul plainly whether he can use it tomorrow.** If the honest answer is "the runner works but
   the markup step is blocked on the probe", say that rather than implying completeness.

**THIS PHASE IS NOT:** building capture, writing to the E5 ledger, or creating any table (that is S2);
building the Tradezella importer (B1 killed it); provisioning Render or R2 (parked); or reopening any
E1–E6 invariant.
