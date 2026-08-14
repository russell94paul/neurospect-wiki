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

> **STATUS (2026-08-12): S1 ✅ BUILT and render-verified.** The runner ships at `/runner` in
> `neurospect-learn`, the boundary probe has been **run in the product** (answer: **NO custom
> indicators** — see §The boundary probe, now answered), and the three missing pieces are authored as
> wiki pages, and the **Tradezella playbook is built and saved** (`Aura - Sequential SMT (NQ triad)`,
> 6 groups, **33 rules**, verified at the rendered layer). **S1b (the guided walkthrough with diagrams)
> is NEXT, not active**; **S2 is gated on real replayed sessions.** The model content this workstream
> projects is canonical in `concepts/mastery/aura/` and must not be
> re-derived here. **Phase S1c ✅ BUILT 2026-08-13** (see §S1c as-built): the rules now compute from
> real bars. `api/scripts/aura_setup_engine.py` + an independent audit script, run over
> **2025-05-01→05-30 → 1 setup · 21 rejections**, all quarantined to files.
> ⭐ **The phase's most valuable output is a defect, not a setup: a LOOKAHEAD bug had contaminated
> 75% of the output** — `known_at = pivot + N days` cannot see weekends, so a signal was dated four
> days early and traded on the session that produced it. Five defects were found and fixed in all;
> the setup count went **17 → 4 → 1**. ⚠️ **n = 1 supports no hit rate, win rate or expectancy, and
> none may be quoted from this run.** **Phase S1b ⏭ ACTIVE** — the guided walkthrough.

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

## ✅ The boundary probe — RUN 2026-08-12, and the answer is NO

**Superseded the section below.** Kept because the reasoning that made it a gate is still correct, and
because the negative result is the finding.

**Tradezella's backtesting chart takes NO custom indicators.** The `Indicators` dialog is a single flat
list under one `SCRIPT NAME` header — no Community Scripts tab, no My Scripts tab, no Pine editor.
Discriminating search: `smt` → *"No indicators matched your criteria"*; `session` →
*"Sessions Indicator by Tradezella"*, so the **vendor** can ship studies and you cannot. The engine is
the **TradingView Advanced Charts library** (built-in study names verbatim, the TV symbol-settings
dialog with `Template ▾` / `Apply to all`, the TV drawing toolbar, `auto`/`log`/`%` scale controls) —
so **Pine does not work**, and the `neurospect-app` Pine script was exactly the false premise this
section existed to catch.

Consequence, stated loudly as the section demanded: **[[concepts/mastery/aura/rules]] R23 cannot be
reproduced inside Tradezella.** R23 describes the Sequential-SMT indicator displaying only
currently-valid signals; there is no way to load it. Every SMT read in a Tradezella backtest is a hand
read, and piece 3 is a **manual drawing protocol** — [[concepts/mastery/aura/chart-markup]].

**Markup stays in Tradezella.** The TradingView-in-TradingView fallback was for a chart that took *no*
levels; this one takes them by hand, and splitting across two applications would break the one-narrow-
window constraint the whole surface is designed around.

**Not measured, and not claimed:** whether drawings persist across replay steps and sessions. The
layout shows `Autosaved` and the toolbar has lock/hide/delete-all, which is evidence, not proof.

Full probe record: `neurospect-learn/api/docs/evidence/s1/s1-render-walk.md`.

## ⚠️ The boundary probe that gates piece 3 — run it FIRST *(superseded — see above)*

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

### S1 — The read-only runner. ✅ **BUILT 2026-08-12** (see §S1 as-built)

Project `checklist.md` + `rules.md` into a followable session surface, and author the three missing pieces
above. **No database writes, no new tables, no capture wiring.** Paul captures into Tradezella's own
fields — which is B2. Decided 2026-08-12 in preference to building capture first, because the binding
constraint is *starting to practise*, and a v1 that slips across three sessions means tomorrow does not
happen.

### S1c — Computed setup detection: run the rules on real bars. ✅ **BUILT 2026-08-13** (see §S1c as-built)

Paul, 2026-08-13: *"the priority is to see if you can use the strategy rules to identify valid setups
and then log them for me to review."* Promoted ahead of S1b at his request.

**⭐ PROVEN POSSIBLE — and proven the honest way, not the plausible way.** The danger in this request is
obvious: an assistant that *looks* at a chart and narrates a confident-sounding Aura read produces
output indistinguishable from analysis, which Paul would then review and (per his tutorial idea) teach
from. Wrong reads would teach wrong. So the capability was **tested before it was promised**:

- **The chart exposes real OHLC.** `tradingViewApi.chart(i).exportData({includeTimeValues:true})` returns
  `{schema, data}` — 300 bars of `[time, o, h, l, c, volume]`, **time-aligned across all four panes**.
  Everything downstream is arithmetic on real numbers, not perception.
- **The discriminating test, with its result predicted BEFORE running.** Prediction: a genuine SMT
  computation must return ≈**zero** divergence between `NQ` and `MNQ` (same instrument, different
  multiplier) and a non-zero number against `ES`. Result on 300 1-minute bars, 57 three-candle pivots
  (R1), checked 20 bars forward for who took the level:

  | Pair | Divergent | Rate |
  |---|---|---|
  | **NQ vs MNQ** | **0 / 53** | **0.0%** |
  | NQ vs ES | 3 / 53 | 5.7% |
  | NQ vs MES | 2 / 53 | 3.8% |

### ⚠️ CORRECTED SAME DAY — Paul disputed it and was right

The first write-up called the MNQ zero *"structurally impossible to diverge"*. **That was wrong, and
overstated.** Paul said he had seen MNQ move slightly differently from NQ. Measured rather than argued:

- Over the same 300 bars, **only 8 have all four OHLC identical**; the **high differs on 184 of 300
  (61.3%)**, median 0.25 (one tick), max 3.00. They are separate contracts with separate order books.
- The 0/53 was an artifact of a **20-bar forward window being too coarse**. Tightening it surfaces the
  divergence Paul described:

  | Forward window | NQ vs MNQ | NQ vs ES |
  |---|---|---|
  | 3 bars | **1 / 56** | 9 / 56 |
  | 5 bars | **1 / 56** | 6 / 56 |
  | 20 bars | 0 / 53 | 3 / 53 |

**The conclusion survives, for a better reason.** MNQ diverges ~9× less often than ES, and its one
divergence has a **margin of 0.00** — the level was matched exactly and not exceeded by a single tick.
That is microstructure, not two markets disagreeing. **R15 requires legs "independent enough that a
divergence carries information."** MNQ fails *that* test — not the can-it-diverge test. Use `ES`/`YM`/`6S`
because MNQ's divergences carry **no information**, not because they cannot happen.

### ⭐ AND THE DISPUTE FOUND A REAL BUG IN THE ENGINE — carry this into S1c

Several of **ES's** divergences also have **0.00 margins**. So a naive "did it exceed the level?" test
**manufactures phantom SMT from zero-margin near-misses on the real triad too** — it would have shipped
into the engine and produced confident false signals.

**S1c requirement: SMT detection needs a noise floor, normalised per instrument.** Tick sizes differ
across the legs (NQ 0.25 · ES 0.25 · YM 1.0 · 6S 0.00005), so a raw price comparison is not
apples-to-apples either. Declare the threshold, print it in every signal (the E6 rule: an unstated
threshold is an invented rule wearing a fact's clothes), and **report the margin alongside every SMT**
so a near-miss is visible as a near-miss.

*(Method note for the estate: the client disputing a number was, again, the only thing that surfaced the
error — and it surfaced two, the overstated claim and the missing noise floor.)*

**This is, in effect, building the Sequential-SMT indicator R23 describes and the S1 probe proved
Tradezella cannot provide.** That is the gap; that is the value.

### S1b — The walkthrough: guided setup + markup, with diagrams. *(next after S1c)*

Paul's ask, 2026-08-13: *"a step by step process / guide to have open alongside tradezella… a
walkthrough guide on how to set everything up and mark everything out — should be done in detail"*,
plus *"other things I should be filling in or tracking in trades"*, and diagrams if they can be made
honestly. **This is the page he keeps open for both backtesting AND live trading.**

Extended the same day with the request that became the phase's centrepiece: **an if-then decision tree
for the entry/no-entry process, whose leaves are the different entry types** — see §D0 in the boot
prompt. It fits because the model already *is* an if-then chain, and it absorbs two diagrams that were
otherwise going to redraw the same content.

**The gap this closes.** S1 shipped the **live protocol** (phases 0→7, tickable) and three **reference
documents**. A document is not a walkthrough: the setup steps and the M1–M12 markup order are ordered,
dependency-bearing procedures rendered as read-only prose in a collapsible. The runner already proves
the right shape — position, progress, hard gates — and it is applied to only one of the three
procedures.

⚠️ **Scope discipline, stated up front.** This adds app surface *before* Paul has run a single
replayed day, which is the exact pattern S1 existed to break — six phases were built on fixtures.
So **S1b is bounded to what gets session ONE to happen** and nothing beyond it. Anything that wants
knowledge of how he actually practises belongs to S2, after real days exist.

### S2 — Capture-first. **Absorbs B4** from the backtest-companion tracker. *(gated on real sessions)*

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

## Open questions for S1 — ✅ ANSWERED 2026-08-12

1. **What is "one session"? → Two levels, because one was not enough.** Paul asked for a
   **configurable** span (week / month / months / year), and a configurable span cannot be the counted
   unit — a 1-week session and a 1-year session are not comparable, so "twenty sessions" would not be a
   measurement. Declared basis: a **session** is one sitting over a span *declared before the replay is
   advanced*; the **counted unit is the replayed trading day**. **A day you correctly stood aside still
   counts** — R51 says missing a trade IS discipline, and any setup-counted basis silently deletes
   those days from the record. So **B2's "~20 sessions" reads as ~20 replayed days**. Canonical in
   [[concepts/mastery/aura/tradezella-setup]] §The counting basis; enforced in the UI, which counts
   `traded + stood aside`.
2. **Step state → `localStorage`, explicitly.** S1 writes nothing to the database, so there is nowhere
   else honest to put it. Stated on the surface itself and in `app/src/lib/runner.ts`. ⚠️ The
   pre-commitment textarea carries a **device-clock** timestamp and the UI says so in the face of the
   record: it is a note, not evidence of ordering. The pre-commitment whose ordering can be trusted is
   E5's frozen ledger — S2's job.
3. **One runner, Aura-only, and deliberately not generalised yet.** The projection script names the
   Aura wiki pages directly. Generalising to AXL/Unified before a single real session has been run
   would be designing a second surface against zero evidence — the failure mode this whole workstream
   exists to end. Revisit only if Paul actually practises a second model.
4. **The per-trade card repeats via a setup selector, not by duplicating the day.** Phases 3–5 are
   `scope: setup` and re-key their ticks per setup (`d{day}:s{setup}:p{phase}:i{item}`); phases 0–2 and
   7 are `scope: day` and do not. The day-level framing stays in the sticky header above, so adding a
   setup never scrolls the date and progress out of reach.
5. **Which phases are per-day vs per-entry → declared in one place.** `PHASE_SCOPE` in
   `api/scripts/project_aura_runner.py`: `0,1,2,7 = day` · `3,4,5 = setup` · `6 = any` (circuit
   breakers are checkable at any moment). Declared in the projection rather than inferred in the UI, so
   one answer serves the runner and the docs, and it is printed on the face of every phase card.

## S1 as-built (2026-08-12) — code is now ground truth

Shipped at **`/runner`**, a new top-level section (second in the nav, directly under Today — it is the
screen you open to *do* the work, not to review it).

**The load-bearing call: the content is a build-time projection to a FILE, not a seed to the database.**
`api/scripts/project_aura_runner.py` parses the five wiki pages into
`app/src/data/aura-runner.json`, which the bundle imports. Three reasons, in order of weight:
S1 is defined as writing nothing to the DB, so a seed was never available; the runner then needs **no
API at all** to paint, which matters for a screen kept open for an hour; and it keeps the E3 invariant
— the wiki stays canonical, a re-run propagates edits, and there is no second copy to drift. The script
takes `--check` and fails if the committed JSON has drifted from the wiki.

It also **fails closed on a broken projection**: <50 rules parsed, zero divergences, zero phases, or a
checklist citing a rule `rules.md` does not define all raise rather than rendering a runner with dead
references.

**Authored (the three pieces that genuinely did not exist):**
[[concepts/mastery/aura/tradezella-setup]] · [[concepts/mastery/aura/tradezella-rule-mapping]] ·
[[concepts/mastery/aura/chart-markup]].

**The rule instrument is better than this tracker assumed, and that changes the deliverable.** The
Playbook `Rules` tab holds **named, reorderable rule groups** and reports **Follow rate · Net P/L ·
Profit factor · Win rate _per rule_**. So the mapping is not "rule → tag" but **rule → playbook row,
1:1**, which buys per-rule adherence *and* per-rule expectancy for free — exactly what the Neurospect
adherence layer wants. 30 rules across 6 groups, six of them hard gates. Tags are kept for a **disjoint**
job — *what kind of setup was this* (`SKIP-DOWN`, `IFVG`, `DISCOUNT`, `PRE-930`…) — because a tag that
duplicates a rule double-counts. Because follow rate is **per rule**, adding rules later does not
corrupt history; only the per-trade aggregate `X / N` does, which is recorded as a comparison hazard.

**⭐ B1's `ZERO` was a `NOT-RECORDED`, and the discriminating read is the denominator.** `AMD Playbook`
already carries **10 rules** (and 0 trades); `Macro Model`, the playbook holding the one real trade,
reports `Rules followed **0 / 0**` on all five orders. `0 / N` would be a discipline finding; `0 / 0`
means no rules were attached to that trade at all. The gate was blocked on a missing instrument, as
this tracker argued — now measured rather than reasoned.

**A finding about Paul's actual setup:** the live session uses **`NQ`, `MNQ`, `ES`, `MES`** — `MNQ` and
`MES` are the *micro contracts* of `NQ` and `ES`, so two of four panes are duplicates and a divergence
between them is **impossible by construction**. R18's confirmation engine has nothing to read. Correct
set `NQ ES YM 6S` (4 of the 5 the form allows), and the runner prints the correction beside the
copyable symbol list rather than leaving it in a doc.

### Three defects only the rendered surface caught

1. **The Tradezella paste block vanished exactly when it was needed** — entering the start date flipped
   the tab to the protocol and collapsed the name/date/symbol block into a `<details>`, at the precise
   moment you go and create the session.
2. **R54 was unreachable.** Phase-*level* `[R##]` refs were parsed and never rendered; R54 appears only
   in phase 0's heading, so it existed in the projection and nowhere in the product.
3. **Prose rendered as a ransom note** — one paragraph per *physical source line*, and the wiki
   hard-wraps at ~100 columns, so the reference tabs were a column of orphaned half-sentences at 400px.

A fourth was a **bad artifact, not a bad product**: `TabsTrigger` has `transition-all` and
`page.screenshot()` allows animations by default, so the first captures showed the *previous* tab
highlighted beside the new tab's content. DOM was correct throughout; captures now freeze animations.
Recorded because an evidence artifact that misrepresents the product is its own defect.

### ⚠️ FLAGGED — a pre-existing defect found, measured, and NOT fixed

**`app/src/lib/auth.ts:50-53` clears the stored token on ANY `auth/me` failure, network errors
included.** It cannot tell "this token is invalid" from "the server is unreachable", so an API blip, a
container restart or a slept laptop **logs you out and discards the session**. Wider than this phase
and security-adjacent, so S1 documents rather than changes it — Paul's call.

It bounds a claim that would otherwise have shipped half-true: the runner's *content* needs no API
(asserted — **zero `/api` requests** while the protocol paints), but the runner is **not usable
offline**, because the shell's auth gate is not. Proposed fix, unapplied: clear the token only on a
real 401/403; leave it alone on a transport failure.

### Verified

- **Full Playwright suite 77 passed** (68 pre-existing + **9 new** in `app/e2e/runner.spec.ts`).
- **No horizontal body overflow at 400 / 620 / 1280px**, re-asserted on every reference tab — the one
  property that decides whether this thing works docked beside Tradezella.
- Rule popovers serve the **canonical** wiki text with dOoMeR's hedges intact (*"Preserved as stated —
  not hardened"*); `rules.md` §Divergences renders as flags with **zero checkboxes**, asserted.
- A **stood-aside day counts** — `0 replayed days` → `1 replayed day counted · 1 stood aside`.
- `tsc -b` + `vite build` clean; container rebuilt and the served bundle re-checked (still `:8001`).
- **No migration, no new table, no mutating endpoint, no backend code changed** — the 294-test backend
  suite is untouched and was not re-run.
- 14 labelled artifacts + `s1-render-walk.md` in `neurospect-learn/api/docs/evidence/s1/`.

### Divergences from the S1 boot prompt

- **The prompt assumed `Mistakes` / `Rating` / `Reviewed` fields.** Only **`Rules followed`** and
  **`Tags`** were observed on the backtesting order surface. The mapping uses what was seen; the rest is
  recorded as unverified rather than designed against.
- **The prompt expected a tagging scheme; the instrument turned out to be a per-rule adherence engine.**
  Deliverable adjusted upward accordingly.
- **Drawing persistence was not measured.** `Autosaved` is displayed and the toolbar has lock/hide/
  delete-all, which is evidence, not proof. Left explicitly unverified.
- **The three new wiki pages are NOT ingested into `content_pages`.** They sit under `concepts/mastery/`,
  which `scripts/ingest_content.py` globs, so the next ingest run will add them to the Library (67 → 70).
  That is a DB write and therefore not S1's to make. Harmless and additive when someone runs it.
- **A stray drawing may exist on Paul's Tradezella chart.** During the drawing probe a horizontal-line
  tool was selected and clicked once on the `NQ` pane of `NQ Macro Po3 - Asia Session`. Placement was
  never confirmed (the panes were rendering without visible candles) and it was not deleted.

## S1c as-built (2026-08-13) — code is now ground truth

Two versioned scripts in `neurospect-learn`, plus an evidence folder. **No app code, no
migration, no endpoint, no table, no backend module** — the evidence layer is untouched.

- **`api/scripts/aura_setup_engine.py`** — extraction-fed rule engine. Reads the exported
  bars, computes the rules as arithmetic, emits setups **and rejections** in the boot
  prompt's output contract (rule ID · computed value · the bar/time it came from).
- **`api/scripts/aura_verify_record.py`** — an **independent** audit that re-derives one
  logged record straight from the JSON, importing nothing from the engine, and asserts
  every engine claim. Exits non-zero on disagreement, so it is a gate not a printout.
- **`api/docs/evidence/s1c/`** — `bars/tradezella-831607-export.json` (2.3 MB, the raw
  export), `computed-setups.md` + `.json`, and `accuracy.md`.

**The bars are real and now versioned.** `setVisibleRange` was found to force the chart to
load deeper history — the previous session's 300-bar ceiling was a viewport artifact, not a
limit. Exported `D`/`240`/`60`/`15`/`5` for all four symbols (~45k bars) and shipped them out
of the browser to a localhost receiver, so the extraction is a re-runnable file rather than a
console paste.

⚠️ **A port collision nearly produced a phantom result.** The receiver was first pointed at
`:8765`, which is held by Paul's `prefect-connectors` orchestrator; it answered the liveness
probe `204`, which read as "my server is up". It was not — the bind had failed silently and
the browser POST hung. **A liveness check that does not identify *which* service answered is
not a liveness check.** Moved to `:8791`; the orchestrator was not touched.

### The declared span, and why it is not the session's own

Session `831607`'s replay is parked at **2025-05-30 20:59 UTC** and has never been advanced.
Advancing it would consume days Paul intends to replay himself, so the engine was pointed at
the real history sitting *behind* the replay edge: **2025-05-01 → 2025-05-30 (ET), 22
weekdays**. No session state was changed. The span deliberately overruns the 5m data (which
starts 05-04) so the boundary shows up as explicit `DATA` rejections rather than vanishing.

**Result: 1 setup · 21 rejections.** Rejections by failing rule: `R6` 13 · `R3` 5 · `DATA` 2 ·
`R35` 1.

### ⭐ Five defects found and fixed — and the count went 17 → 4 → 1

Every one of these produces output that *looks* like analysis. Recorded because the pattern
matters more than the fix.

| # | Defect | Effect | Caught by |
|---|---|---|---|
| 1 | **R6 never implemented** | a range used long after price closed through it; entries scored at `1.22 of range`; a five-week-old 3,584-pt "range" | reading the rendered log |
| 2 | **`abs()` in the reward calc** | a target the trade had already passed rendered as `0.7R` | reading the rendered log |
| 3 | **One stale daily SMT drove every day** (R7/R23) | the same 05-02 signal reused for a week | reading the rendered log |
| 4 | **⭐ LOOKAHEAD** — `known_at = pivot + N days` | calendar arithmetic ignores weekends/holidays: dated a signal **4 days early** (05-25 vs the true 05-28) and traded it on the session that produced it | the independent audit |
| 5 | **⭐ Tick measured as float noise** | CHFUSD's tick came back `5.98e-09` (IEEE-754 dust), collapsing that leg's noise floor to ~zero — **reintroducing the phantom-SMT bug on the one leg too small to eyeball** | a column that printed a measured value |

**Defect 4 alone removed three of the four surviving setups.** Before that fix **75% of the
setups were contaminated** by information that did not exist when the engine claimed to act on
it — and any accuracy statistic computed beforehand would have looked entirely reasonable.
This is the phase's most important output: *the engine was wrong in a way that reads as
competent*, and only an instrument that re-derived the numbers by a different route found it.

Defects 1–3 were caught by reading the output **like a trader**, not by checking that the code
ran. That is the cheap check and it found three of five.

### What the tracker asked for, and what it got

- **Noise floor: DONE and two-sided** — the taking leg must exceed by more than the floor *and*
  the diverging leg must miss by more than it. Floor is `2 ticks` of each instrument's **measured**
  tick size, printed in the run header, and the margin is reported on every leg of every signal.
- **Measured tick sizes recovered the contract specs without being told them: NQ `0.25` · ES
  `0.25` · YM `1.0`.** That is the positive control for the measurement itself.
- **CHFUSD refused at daily, admitted intraday** — encoded as a rule (`admissible_legs`), and the
  refusal prints as a branch on every record rather than being silent.
- **Legs joined by TIMESTAMP throughout.** `NOT-VISIBLE` is a distinct verdict from
  `DID-NOT-TAKE`, so a missing bar can never masquerade as a divergence.
- **Positive control passed on fresh data** — `NQ`/`ES`/`YM` share every daily timestamp,
  `CHFUSD` shares none. Independently reproduces the 2026-08-13 alignment measurement.

### ⚠️ FLAGGED — carry these into S1b

1. **n = 1 supports no rate of any kind.** One setup over 22 days demonstrates the rules *can* be
   computed; it measures nothing about whether they work. There is **no** hit rate, win rate or
   expectancy in this run and none may be quoted from it.
2. **No outcome simulation.** The engine never walks price forward to see whether stop or target
   was hit first. Every `R` figure is **planned, not realised**.
3. **CHFUSD's tick is not reliably measurable** — `1e-06` intraday vs `5.2e-06` daily, against a
   conventional `1e-05`. Its measured tick varying *by resolution* is the tell. Its noise floor is
   the softest of the four, and **the one surviving setup's Sequential Skip diverges on CHFUSD
   alone** — the record now carries that warning on its face.
4. **Declared-but-unimplemented rules**, stated rather than approximated: **NWOG/NDOG** (need a
   per-symbol session boundary, and CHFUSD's do not match the futures'), **R21** cross-cycle
   gap-pairing, **R22** extreme-of-the-larger-segment targeting, and **R8**'s false-sweep tiebreak.
   **Weekly and monthly cycles are absent entirely** — daily is the deepest cycle the export
   supports, and nothing was aggregated to fake the missing rungs.
5. **Deliverable 3 (drawing computed levels on the chart) NOT DONE.** `createShape` is available
   and proven, but it writes into Paul's live session, which he would then have to clean up.
   Optional per the boot prompt; left for his say-so.

## Session Log

### 2026-08-13 — S1c BUILT: the rules compute, and the engine was wrong five ways first

- approach: proved the extraction first, versioned it, then wrote the engine — and then
  **built a second instrument whose only job was to disbelieve the first**. That instrument is
  what justified the phase.
- **⭐ the headline is a defect, not a setup: a lookahead bug had contaminated 75% of the
  output** and was invisible in the log, which said "knowable 2025-05-25" with total confidence.
  Real bar timestamps put it at 05-28 — the session it then traded. `pivot + N days` cannot see
  weekends. Fixed to derive `known_at` from actual bars, plus a full bar for the window to close.
- **found: `setVisibleRange` forces deeper history loading** — the 300-bar ceiling the previous
  session hit was a viewport artifact. ~45k bars extracted across five resolutions.
- **found: the tick-size measurement was itself a phantom-SMT generator.** Taking the plain
  minimum non-zero price difference returns IEEE-754 dust on a forex feed. A candidate increment
  must **recur** before it is believed. The futures ticks (0.25/0.25/1.0) are the control that
  proves the fixed version works.
- **found: `:8765` belongs to `prefect-connectors`**, and it answered my liveness probe `204`,
  which read as success. Not touched; moved to `:8791`. A liveness check that cannot say *who*
  answered is not one.
- decided: **span 2025-05-01→05-30, behind the replay edge**, rather than advancing Paul's
  replay — those are his days to run.
- decided: **quarantine by construction** — output goes to files under `api/docs/evidence/s1c/`,
  nothing writes to the DB, and the report leads with the machine-generated banner.
- verified: 12/12 independent audit checks pass, including the no-lookahead relation; positive
  control (NQ/ES/YM daily alignment) reproduced on fresh data; measured ticks match contract specs.
- verified: **Paul's session left exactly as found** — all four panes restored to `1m`, `0` shapes
  on every pane, no replay advance, no orders, no playbook edits.
- flagged: n=1, no outcome simulation, CHFUSD's soft floor, and five declared-but-unimplemented
  rules — all in `accuracy.md` and §FLAGGED above.
- next: **S1b** — the guided walkthrough. Boot prompt below.

### 2026-08-12 (S1 follow-on) — the playbook authored from the COURSE content; entry blocked on tooling

Paul asked for the playbook to be built from the course content in `neurospect-learn` rather than from
the S1 mapping doc alone, and for the full Tradezella setup with the key tracked data identified.

- **Reading the underlying concept pages (not just `rules.md`) found two genuine omissions.** The
  mapping was built from `rules.md`, which is a *distillation*; going back to
  [[concepts/aura/sequential-smt]] and [[concepts/aura/htf-ltf-application]] surfaced:
  - **`R22` was missing entirely** — the targeting rule (*SMT between two segments of a larger cycle →
    expect that segment's extreme to be taken*, which the source says generalises to all cycles).
    Without it the confirmation group validates a signal but never asks what it implies about where
    price is going.
  - **`R7` had no tickable row** — the range lifecycle (*follow the current range until an opposing or
    same-cycle Sequential SMT forms*), which makes "trading a range that has already ended" a distinct,
    checkable error. **30 → 32 rules.**
- **⚠️ FOUND IN THE BUILDER — every rule row carries an OUTCOME FILTER** (`Always / Winner / Loser /
  Break even`, *"only show this rule when the selected trade outcome or type applies"*). **Every Aura
  rule must stay `Always`**: an outcome-filtered rule computes its follow rate over a biased subset, so
  it would read as discipline while measuring nothing — the self-deception failure the enforcement
  layer exists to prevent, offered as a product feature.
- **Answered "what data do I track" from [[concepts/aura/journaling-system]], split by who captures it.**
  Tier 1 (date, session, entry, exit, stop, target, R:R, result in R) is **automatic** — do not re-type
  it. Tier 4, the psychological layer, is **automatic nowhere** and is where dOoMeR says the value is
  (*"the numeric fields tell you what happened; this layer tells you why"*). Added the
  `MANAGED`/`SET-AND-LEFT` tag pair, which is what powers the active-management-vs-walking-away
  comparison the course calls a potential "personal holy grail".
- **⚠️ BLOCKED — the playbook was NOT entered into Tradezella, and the reason is tooling, not scope.**
  Three compounding browser-automation failures: the renderer froze on roughly half of all screenshot
  calls (recovering each time, 10–40s); one `type` silently did not land; and then a rule landed in the
  **wrong row, overwriting R4 with R5**. The third is disqualifying for this task — a playbook whose
  rows do not say what they are believed to say produces confidently wrong follow-rate data, which is
  worse than an empty playbook. Stopped and **cancelled cleanly: `My Strategies (2)` verified unchanged,
  nothing created in Paul's account.**
- **Delivered instead:** the complete setup as paste-ready blocks in
  [[concepts/mastery/aura/tradezella-rule-mapping]] — strategy name, full description, 6 group names,
  all 32 rule texts, the tag vocabulary, and the five data tiers — re-projected into `/runner`'s Rules
  tab (9/9 runner tests still pass).
- **RESOLVED same session — the playbook is BUILT and SAVED.** Retried after researching the tool
  surface, and three of the four original failures turned out to be technique, not tooling:
  `form_input` (never loaded the first time) sets values by ref **and reports the previous value**,
  which is exactly the guard that would have caught the R5-over-R4 overwrite; screenshots time out
  while `find` / `read_page` / `javascript_tool` stay healthy on the same tab, so "renderer frozen"
  was the wrong diagnosis; and MUI ignores `.click()` but obeys a full pointer sequence. The genuine
  tool limit was the save button, which fired only when React's own `onClick` was invoked from the
  element's `__reactProps$` key.
  **Result: `Aura - Sequential SMT (NQ triad)`, 6 groups, 33 rules, all on the `Always` outcome
  filter — verified at the RENDERED layer** (all 33 rule strings + 6 group headings read back off the
  Rules tab, not merely "saved successfully"). Grew 32 → 33 with **R23** (read the *current* SMT
  state — a hand read, since the probe proved no indicator can exist here).
- **⭐ The last unmeasured probe question is now closed: drawings DO persist.** Across a replay step
  **99 shapes → 99 shapes**; across sessions, the same 99 present after a fresh navigation, so they are
  server-side. Also upgraded the engine identity from inferred to **proven** — the chart is a `blob:`
  iframe exposing `TradingViewApi` / `chartWidget` / `ChartApiInstance`.
- **Correction: no stray drawing was left.** The S1 log warned one *might* exist. Enumerated via
  `getAllShapes()`: 99 shapes on NQ (94 rectangles, 3 vertical, 2 trend) and **zero horizontal-line-like
  shapes** — the probe click never created anything. `MNQ`/`ES`/`MES` carry zero shapes each, which is a
  finding in itself: **all of Paul's markup lives on one pane**, so the triad legs SMT is read across
  have nothing marked on them.
- **Skill authored** (Paul asked): `~/.claude/skills/web-automation/claude-in-chrome-driving.md`,
  registered in `~/.claude/skills/INDEX.md`. Nine rules, each tied to a measured failure.
- next: **S2 is still gated on real sessions.** The instrument now exists; nobody has used it.

### 2026-08-12 (later) — S1 BUILT: the runner ships, and the probe came back NO

- approach: ran the boundary probe **first**, as the boot prompt demanded, driving Paul's own logged-in
  Chrome rather than asking him to describe what he saw. Then authored the three missing wiki pages,
  built the projection + surface, and verified at 400px with a reproducible spec rather than by eye.
- **⭐ the probe answered NO, and that is the phase's most valuable output.** No custom/Pine indicators
  — `smt` → *"No indicators matched your criteria"*, while `session` → *"Sessions Indicator by
  Tradezella"* proves the vendor can and you cannot. Engine identified as the **TradingView Advanced
  Charts library**. So the `neurospect-app` Pine script was precisely the false premise the tracker
  warned about, and **R23 cannot be reproduced inside Tradezella** — every SMT read there is a hand read.
- **found: the Playbook `Rules` tab reports per-rule Follow rate, P/L, profit factor and win rate.**
  Materially better than the assumed tagging scheme; the mapping became rule→playbook-row 1:1.
- **found: `0 / 0` is discriminating.** The traded playbook has a zero *denominator* — no rules attached
  — while the other playbook already has 10 rules. B1's `ZERO` is a `NOT-RECORDED`.
- **found: two of Paul's four chart symbols are micro duplicates** (`MNQ`/`MES` of `NQ`/`ES`), so SMT is
  impossible by construction on his current layout. Surfaced in the product, not just the docs.
- **decided: the counting basis is two-level** — a configurable declared *span* (Paul's requirement) with
  the **replayed day** as the counted unit, because a configurable span cannot be a unit of measure and
  a stood-aside day must still count (R51).
- **decided: project to a JSON file, not the database** — S1 writes nothing, and it makes the runner
  render with no API call at all.
- **flagged — `auth.ts` logs you out on any network failure.** Pre-existing, wider than this phase,
  measured and left unfixed for Paul's approval. It is why "renders offline" is only half true.
- **flagged — three rendered-surface defects** (paste block collapsing at the moment of use; R54
  unreachable; prose split per source line) and one **misleading evidence artifact** (animations not
  frozen). Fixed all four.
- verified: 77/77 Playwright, no horizontal overflow at three widths, canonical rule text with hedges,
  divergences as flags with zero checkboxes, zero `/api` requests to paint the protocol.
- next: **S2** — boot prompt below. Do not design the capture surface until Paul has run real days.

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

## Boot Prompt Archive (Phase S1c — computed setup detection) ✅ RUN 2026-08-13

**Launch:** `claude --model opus[1m]`, `/effort high`. This phase produces numbers Paul will trade
against and may teach from. Every one must be auditable.

**Task: compute Aura setups from real bars and log them for review.** Not "look at the chart and
describe it" — extract OHLC, run the rules as arithmetic, and emit a record where every line can be
checked against the chart.

### ✅ PREREQUISITE MET + a finding S1c must build around (2026-08-13)

Session **`831607`** exists: `NQ` `ES` `YM` `CHFUSD`, Aura playbook attached, 2025-06-01 → 2025-06-30,
$50k. All four export bars.

**⭐ Candle alignment was measured before any engine code, and it constrains the design:**

| Resolution | NQ↔ES | NQ↔YM | NQ↔CHFUSD |
|---|---|---|---|
| Daily | 300/300 | 300/300 | **0 / 242** |
| 60m | 300/300 | 300/300 | 285/300 |
| 5m | 300/300 | 300/300 | 288/300 |

Root cause is structural: `NQ`/`ES`/`YM` are `America/Chicago`, `CHFUSD` is `Etc/UTC`, so daily bars
bucket on different exchange days (13:30 UTC vs 21:00 UTC stamps). **CHFUSD reproduces the exact defect
R17 rejected DXY for, at the daily cycle.**

**Engine requirements that follow — these are correctness constraints, not preferences:**
1. **Never treat CHFUSD as a daily/weekly-cycle leg.** R18 nests SMT across adjacent cycles; the cycles
   do not correspond. The engine must refuse this combination rather than silently produce a signal.
2. **Join legs by TIMESTAMP, never by bar index.** Series have different lengths and windows (CHFUSD 252
   daily bars vs 300 for the futures). Index-joining would silently compare different moments.
3. CHFUSD is admissible **intraday only** (R21's gap-pairing range).
4. `NQ`/`ES`/`YM` aligning perfectly at every resolution is the **positive control** — if a future run
   shows them misaligned, the measurement is broken, not the market.

### ⛔ HARD PREREQUISITE — the symbols *(met — see above)*

Sequential SMT is a comparison **across the triad**. On `NQ / MNQ / ES / MES`, two of four legs carry
**zero** information (measured: 0.0% divergence). **The session must be `NQ ES YM 6S` or this phase
cannot run at all.** Verify it before writing a line of analysis code.

READ FIRST:
1. Wiki `CLAUDE.md` — code is ground truth, reconciliation checklist, Rules #3/#4/#6, >50% context.
   **Paul handles git.**
2. This tracker: **§S1c above** (the proven mechanism + the discriminating test), §S1 as-built.
3. [[concepts/mastery/aura/rules]] — the rulebook being computed. **The wording is canonical.**
4. [[concepts/mastery/aura/chart-markup]] §The probe — why no indicator can exist here.
5. `~/.claude/skills/web-automation/claude-in-chrome-driving.md` — **required.** Screenshots time out
   while the DOM stays healthy; drive by `javascript_tool`.

### What is COMPUTABLE vs what is JUDGEMENT — do not blur the line

| Computable from bars | Rule |
|---|---|
| 3-candle swing pivots | R1, R2 |
| SMT qualification across the triad | R3, R18, R20 |
| Range by expansive move | R4 |
| Discount / EQ / premium position | R5, R32 |
| Gaps (FVG, iFVG, NWOG, NDOG) + liquidity nested inside | R11, R12, R13 |
| Cross-cycle gap-pairing | R21 |
| **SMT margin** — how far the level was exceeded/missed, reported on every signal | R3, R18 |
| Cascade across resolutions | R27 |
| 5m iFVG entry, stop at invalidation, target at TF extreme | R30, R33, R35 |
| R:R and risk in R | R39, R43, R44 |

**NOT computable — surface candidates and mark `UNRESOLVED`, never pick silently:**
- **R9** — *"if the range isn't obvious, zoom out"*, *"the most-prominent obvious high"*, and
  *"overlapping/ambiguous ranges are acceptable — do not force one"*. Explicitly judgement.
- **R8's false-sweep tiebreak** where candidates are close.
- Anything resting on a **soft/flagged** rule (R31's 9:30 preference above all) — report the branch,
  do not resolve it.

### ⭐ THE OUTPUT CONTRACT — auditable or it does not ship

Every logged setup carries, per line, **the rule ID, the computed value, and the bar/time it came from**,
so Paul can check it against the chart. Worked shape:

```
2025-06-03 09:47 ET · NQ
  R1  swing high 21,884.25 @ 09:31  (pivot bars 12/13/14)
  R3  SMT-qualified: NQ took it 09:44 · YM did NOT (high 40,112 vs level 40,140)
  R4  range 21,802.50-21,884.25  (expansive move 09:12->09:31)
  R5  entry in DISCOUNT (0.31 of range)
  R30 5m iFVG 21,838.75-21,843.00, confirmed 09:47
  R33 stop 21,801.75  ·  risk 37.0 pts
  R35 target 21,884.25 (range extreme)  ·  2.2R
  UNRESOLVED: R9 - two candidate ranges (see note)
```

**Rules for the log:**
- **A setup that fails a hard gate is still logged, as a rejection with the failing rule.** The
  stand-asides are the most valuable records Paul has (R51) and the ones no instrument currently keeps.
- **Never emit a figure the data did not produce.** If the export window is too short for the cycle
  being framed, say so and stop — do not extrapolate.
- **State the sample.** Bars, resolution, date range, and which symbols were actually present.

### ⚠️ QUARANTINE — machine-found setups are NOT Paul's reps

These are **not** evidence of practice, and they must never touch the evidence layer: no
`evidence_assets`, no rep credit, nothing that feeds the streak, the calibration score or the Readiness
Gate. That is `devil`'s criterion #2 and the E2 invariant *"reps gets strictly harder, never easier"*.
Log to **files** under `api/docs/evidence/s1c/`, and if anything is ever surfaced in the app it renders
**visibly and permanently marked as machine-generated**. A tutorial artifact is not a training record.

DELIVERABLES:
1. The extraction + rule engine (a script, versioned, re-runnable — not a one-off console paste), with
   the sample it ran on stated.
2. A logged set of setups **and rejections** over a declared span, in the contract above.
3. **Optional and only if it earns its place:** draw the computed levels onto the chart via
   `createShape` / `createMultipointShape`, so a marked chart accompanies the arithmetic.
4. An honest accuracy statement — what the engine finds, what it misses, and where it defers to Paul.
5. Tracker + `log.md` + `index.md` reconciled, then hand back to **S1b**.

**THIS PHASE IS NOT:** narrating a chart from perception; writing to the evidence layer; fabricating
bars or levels; resolving a soft rule into a hard branch; or building the walkthrough UI (S1b).

---

## Boot Prompt (Phase S1b — the guided walkthrough, with diagrams) ⏭ ACTIVE

### ⚠️ WHAT S1c HANDED YOU — read §S1c as-built before designing anything

S1c built a working rule engine (`api/scripts/aura_setup_engine.py`) and, more usefully,
**a list of five ways a confident-looking Aura read can be wrong**. Three of them are
things the S1b walkthrough will be tempted to render as clean UI:

- **A range is dead once price CLOSES beyond it (R6).** 13 of 21 rejections were this. A
  walkthrough that draws a range without a liveness state teaches Paul to trade a corpse.
- **A signal is not knowable when it forms** — it is knowable when its forward window
  closes, counted in *bars*, not days. Any "as of" the walkthrough displays must respect it.
- **The Aura Asset leg is the weakest link**, and one setup's confirmation rested on it alone.

And the standing constraint: **n = 1**. S1c produced one setup over 22 days. The
walkthrough must not imply a frequency, a hit rate, or an expectancy — none exists.

#### ⭐ D0 gets a gift from S1c — use it instead of re-deriving the tree

**The engine already enumerates D0's branches, in code, declared rather than inferred.**
`aura_setup_engine.py` holds a `HARD_GATES` list and a `SOFT_BRANCHES` list at module top,
and every rejection names the exact rule that stopped it. So:

- **The hard gates are D0's decision nodes** — R3, R18, R6, R7, R30, R35, R29 — and they are
  already in the order the model evaluates them.
- **The rejection reasons are D0's STAND-ASIDE leaves**, and they come with *real observed
  frequencies from a real run* (`R6` 13 · `R3` 5 · `DATA` 2 · `R35` 1). That is honest source
  material for the tree that fabricates nothing — the exact opposite of an invented example.
- **The soft branches are already tagged as soft** in the same file, which is precisely the
  hedge-hardening failure §"The tree's own failure mode" warns about. Do not re-decide which
  rules are soft; take the list.

⚠️ **But do NOT wire the app to the engine.** The engine is an offline script over an exported
file; S1b stays a wiki-projected read-only surface with no API call. Take the *structure*, not
a runtime dependency — and if you project the gate list, project it the way `/runner` already
projects rules (build-time, with a `--check` drift guard), never by importing Python into the app.

⚠️ **And do not surface machine-found setups in the walkthrough.** S1c's output is quarantined
by construction. If S1b ever displays one, it renders permanently and visibly marked as
machine-generated — it is a tutorial artifact, never a training record.

**Launch:** `claude --model opus[1m]`, `/effort high`. Design-heavy: this authors a procedure Paul will
follow every session for months, and a set of diagrams that must be honest about what they depict.

**Task: turn the two read-only procedures into GUIDED walkthroughs, add a per-trade capture card, and
illustrate them.** Still read-only with respect to the database — S1's constraint holds.

READ FIRST:
1. The wiki `CLAUDE.md` — code is ground truth, the MANDATORY reconciliation checklist, Rules #3/#4/#6,
   Context Management (tell Paul at >50%). **Paul handles git.**
2. This tracker: **§S1 as-built**, **§S1c as-built**, §Open questions (all answered — the counting basis
   is canonical and must not be reopened), and the **§S1b scope discipline note above**.
3. `neurospect-learn/api/docs/evidence/s1/s1-render-walk.md`.
3b. **`neurospect-learn/api/docs/evidence/s1c/accuracy.md`** — the five defects, the declared-but-
   unimplemented rules, and the `n = 1` constraint. Read this before writing a single number into UI.
   Then skim `api/scripts/aura_setup_engine.py`'s declared-constants block for `HARD_GATES` /
   `SOFT_BRANCHES` — D0's nodes and its soft/hard split are already decided there.
4. [[concepts/mastery/aura/tradezella-setup]] · [[concepts/mastery/aura/chart-markup]] ·
   [[concepts/mastery/aura/tradezella-rule-mapping]] — the three pages being projected.
5. `app/src/lib/runner.ts` + `app/src/pages/runner.tsx` — the existing shape to extend, **not** replace.
6. `~/.claude/skills/web-automation/claude-in-chrome-driving.md` — **required before any browser work.**
   Tradezella freezes screenshots while the DOM stays healthy, MUI ignores `.click()`, and coordinates
   from a screenshot misfire on a mutating DOM.

### ⚠️ FIRST ACTION — ask Paul whether he has run a replayed day yet

Not a blocker, but it changes the work. If he has, **read what came out of it first** and let the real
friction drive the walkthrough. If he has not, build the smallest thing that gets session one to happen
and say so plainly. Do **not** design capture surfaces on speculation — that is S2, and S2 is gated.

### ⭐ THE DIAGRAM RULE — the one thing this phase can get badly wrong

**Never fabricate price data.** No invented candlesticks, no "example" FVG or SMT setup drawn from
imagination. This model's entire skill is reading *actual* structure, so a plausible-looking fake teaches
geometry that never happened — and it would be indistinguishable from a real example once it is sitting
in the app. This is the sharpest form of the estate's own rule: a figure that is not measured must not
render as though it were.

### ⭐⭐ D0 — THE DECISION TREE. Paul's request 2026-08-13, and the spine of this phase

> *"a decision tree or diagram with if-then statements would be a powerful intuitive way to visualise the
> decision process for entering/not entering trades and the different types of entries that are possible
> based on what route you go down the decision tree."*

**Build this first, and let the other diagrams orbit it.** It is the best-fitting visualisation this
model has, because **the model already IS an if-then tree** — [[concepts/aura/htf-ltf-application]]
presents the cascade as an explicit if-then table and states the reason outright: *"a great way to
eliminate your impulses and a great way to notice when you have impulses is to think like a machine."*

**It ABSORBS D1 and most of D4** — do not draw those separately, or the same content is drawn twice.
Pay for the extra work by dropping **D6/D7 to "if budget allows"**.

The leaves Paul asked for — *the different types of entries* — are real and already distinguishable in
the corpus: standard nested-SMT entry · **Sequential Skip (down-cycle)** · **Sequential Skip
(cross-asset)** (R25) · **alt-asset entry taken for stop size** (R34) · pre-9:30 vs post-9:30 (R31) ·
and the terminal that matters most, **STAND ASIDE** (R51 — missing a trade is discipline, so it must be
a first-class leaf drawn as an outcome, never as a dead end).

### ⚠️ The tree's own failure mode: it will harden hedges into gates unless you stop it

A decision tree renders everything as a clean branch — that is exactly its appeal, and exactly its
danger here. dOoMeR does **not** state every rule as a gate, and the runner's whole design refuses to
flatten that.

- **R31 is the sharp case.** *Wait for the 9:30 open, or take the pre-9:30 gap?* is a natural branch —
  but R31 is marked **soft**, stated as a preference aimed particularly at traders still building
  consistency. Drawn as a hard branch, the tree silently promotes a preference into a rule.
- **R9** (overlapping/ambiguous ranges are acceptable — do not force one) is the same shape.

**So: every branch carries its `R##`, and a soft/flagged rule renders as a SOFT branch — visibly a
preference, never a gate.** Reuse the shipped idiom rather than inventing one: `RuleChip` already marks
soft/flagged rules with `*` and an amber ring, and the popover already says *"Preserved as stated — not
hardened."* Hard gates keep the existing amber hard-gate treatment; the two must be visually distinct.

### ✅ DECIDED 2026-08-13 (Paul): **LIVE**, with the full map one tap away

Not a poster. The tree shows **the path you are on**, plus the choice at the current node, with a
`[full map]` toggle revealing the whole static tree for study. Live **absorbs** static — build one
surface, not two.

**The decisive argument was legibility, not power.** A decision tree is two-dimensional and the window
is ~400px, so a static tree is a postage stamp you scroll around inside — worst exactly when you are
mid-setup and least able to spare attention. **The path you are on is one-dimensional**, so live
collapses a wide branching diagram into a short vertical list. Static is also most useful while
*learning* and least useful while *executing*, which is backwards for a screen docked beside a live
chart.

### ⚠️ TWO DESIGN FINDINGS — do not rediscover these the hard way

**1. Tick state alone CANNOT drive the tree.** The checklist is a linear list of things to verify; the
tree branches on *facts about the market*. Ticking `R24+R25 — a valid Sequential Skip identified`
records **that** a skip was used but not **which** — down-cycle or cross-asset are different leaves. So
the tree needs its own small set of **branch answers** (~5–7 choices), stored in `localStorage`
alongside `ticks` — same shape, keyed per day and per setup, since the entry decision is
`scope: setup` and repeats.

**2. ⭐ The tree must NOT auto-tick the rules.** It is tempting — the node was answered, why not tick
R24? Because that **manufactures adherence the user never consciously asserted**, which is the same
failure as batch-ticking 33 boxes and is precisely what corrupts the per-rule follow rate the whole
playbook exists to produce. The tree may **highlight** which rules just came into scope; the user still
ticks them. Keeping branch answers and rule ticks separate is what keeps the measurement honest — the
same structural argument as E2's derived `reps`.

---

**Three honest sources, in order of preference:**

1. **Schematic diagrams of RULES** — hand-authored inline SVG, theme-aware, each labelled visibly as a
   schematic. These depict definitions and logic, not market observations:
   - ~~**D1 · The HTF→LTF cascade**~~ — **absorbed into D0.**
   - **D2 · Range anatomy** — discount / equilibrium / premium with fib levels **0 / 0.5 / 1 only**, and
     a visible "no quadrants" callout (**R4, R5** — this is a flagged divergence, so the diagram is where
     it becomes unmissable).
   - **D3 · Markup order M1→M12** — as a dependency chain, showing what gates what.
   - **D4 · Sequential SMT logic** — three triad legs + 6S; one fails to take the level. Abstract shapes,
     explicitly not a chart (**R18**). *Mostly absorbed into D0 — build only the residue D0 cannot carry.*
   - **D5 · The gap family** — FVG / iFVG / NWOG / NDOG as definitional 3-candle schematics, plus
     **liquidity nested inside the gap** as the actual target (**R11, R12**).
   - **D6 · Counting basis** — declared span vs the replayed day vs the setup. *If budget allows.*
   - **D7 · Rule → Tradezella field map** — which Aura rule lands in which field. *If budget allows.*
2. **Annotated real screenshots** of the Tradezella UI for the click-path (create-session form, Rules
   tab, chart toolbar). Real, already navigated in S1 — see the skill doc for capturing them when
   screenshots time out.
3. **A real worked trade** — `aura-24` in [[concepts/aura/trade-reviews]] is already documented. Point at
   it; do not invent a substitute.

**Rendering:** the app uses `react-markdown`; there is no mermaid renderer wired in. Prefer hand-authored
SVG React components — precise, theme-token-aware, and they scroll inside their own box at 400px. Adding
a mermaid dependency is a bigger call than this phase needs; if you take it, justify it.

DELIVERABLES:
1. **The setup walkthrough** — the `tradezella-setup` steps as an ordered, tickable, position-aware
   sequence, with the one-time §0 items separated from the per-session ones.
2. **The markup walkthrough** — M1→M12 tickable, with each step's diagram beside it, and the dependency
   made visible (a step whose predecessor is unticked should read as not-yet-reachable, **not** be
   blocked — S1's hard-gate idiom is *surfaced, never refused*).
3. **The per-trade capture card** — the five data tiers from
   [[concepts/mastery/aura/tradezella-rule-mapping]] §"The key data to track", made explicit about
   **which tier Tradezella captures for you** (Tier 1 — do not re-type it) and which is yours alone
   (**Tier 4, the psychological layer**, where dOoMeR says the value is). Include the
   `MANAGED`/`SET-AND-LEFT` tag, which powers the active-management-vs-walking-away comparison.
4. **⭐ D0, the LIVE entry decision tree** — built first, absorbing D1/D4. Shows the path taken plus the
   current node's choice, with a `[full map]` toggle for the whole tree. Every branch carries its `R##`;
   every soft/flagged rule renders as a **soft branch**; `STAND ASIDE` is a first-class leaf. Branch
   answers live in `localStorage` beside `ticks` and **never auto-tick a rule**. Then the remaining
   diagrams per the rule above, each carrying its `R##` references.
5. **Render-verified at 400px**, artifacts into `api/docs/evidence/s1b/`, plus which interactions respond
   and **which are inert**. Extend `app/e2e/runner.spec.ts`; keep the no-horizontal-overflow assertion,
   and add one asserting **every diagram scrolls inside its own box**.
6. Tracker + `log.md` + `index.md` reconciled, including divergences — then hand back to **S2**, whose
   prompt is below and still gated on real sessions.

**THIS PHASE IS NOT:** writing to the database (still zero — no migration, no table, no mutating
endpoint); reopening the counting basis; building capture *storage* (S2); fabricating any chart; or
fixing `auth.ts` without Paul's approval.

---

## Boot Prompt (Phase S2 — capture-first, and the two-clock decision) — ⏸ GATED on real sessions

**Launch:** `claude --model opus[1m]`, `/effort high`. This phase writes to the **frozen** E5 ledger and
must choose a clock. Both are one-way doors.

> **⛔ GATE — do not build until Paul has actually practised.** S2 is gated on **S1 + real sessions**.
> The whole point of S1 was that *"right now I have only been building and testing the app with you, not
> actually using it."* Designing the capture surface before Paul has run replayed days and can say which
> steps he actually kept would repeat that exact error one layer up.
>
> **First action of the S2 session: ask Paul how many replayed days he has run, and read what came out
> of them.** If the answer is zero, **stop and say so** — the correct next move is to help him run one,
> not to build S2. Report it plainly rather than building something defensible.

**Task: capture the session in `neurospect-learn` FIRST — not imported after.** Absorbs B4 from
[[processes/distributed-workflow/active/backtest-companion]]; B4's own prompt was retired unrun.

READ FIRST:
1. The wiki `CLAUDE.md` — code is ground truth, the MANDATORY reconciliation checklist, Rules #3/#4/#6,
   Context Management (tell Paul at >50%). **Paul handles git.**
2. This tracker in full — especially **§S1 as-built**, §Open questions (all five answered; the counting
   basis in Q1 is now canonical and S2 must not re-open it), and §Why this unlocks B2.
3. `neurospect-learn/api/docs/evidence/s1/s1-render-walk.md` — the probe result, the three rendered
   defects, and **the `auth.ts` finding**.
4. [[concepts/architecture/learning-enforcement]] §Invariants, and the E5 as-built section on the
   **structural** freeze (migration `0011`: no `is_deleted`, no PATCH, no DELETE).
5. [[concepts/mastery/aura/tradezella-setup]] + [[concepts/mastery/aura/tradezella-rule-mapping]] —
   what Paul is actually doing in the other tool, so the capture surface matches it.

**The decision this phase owes: WHICH CLOCK.** The planner counts "today" in the user's timezone
(`study_preferences.timezone`, default `"UTC"`) while migration `0012`'s trigger enforces **server UTC**.
Earlier phases could dodge this; S2 cannot, because **a pre-commitment is a claim about ordering in
time**. Changing it touches E6 semantics. Decide it explicitly, write down what breaks either way, and
put the reasoning in [[concepts/architecture/learning-enforcement]] — not only in a session log.

**Constraints carried intact from B4:**
- A **pre-session pre-commitment** in the frozen E5 ledger, authored *before* the replay is advanced —
  the one artifact whose ordering can be trusted, because `neurospect-learn` stamps it. S1's textarea is
  a `localStorage` note on a **device clock** and says so on screen; replacing it is S2's job.
- **Consistency across similar setups** — one rubric, many captures, variance in cue usage (`CI`).
  Interleaved presentation, per Brunmair & Richter 2019 (`META`, g = .67 for visual category induction).
- Tradezella stays the **execution surface**; nothing is imported.
- If backtest-derived data is ever imported it must be permanently and visibly quarantined as
  `SELF-REPORTED` and excluded from the evidence streak, the calibration score and the Readiness Gate
  (`devil`'s criterion #2).
- Wire into **existing primitives**: E5 `predictions`, `journal_entries` with `mode='backtest'`, the
  rubric layer, `evidence_assets`. **No parallel data model.**

**Non-negotiables:**
- **The counted unit is the replayed day** and a stood-aside day counts. Whatever S2 stores must be able
  to represent *a day worked with zero trades* — R51/R53. S1 records those in `localStorage` only, and
  the Tradezella side literally cannot see them (no order → no `Rules followed`, no `Tags`), which is the
  clearest live case of *an instrument that cannot see the behaviour the model most wants to reward*.
- **Rubrics and rules stay wiki-projected and read-only** (the E3 invariant). If the runner needs new
  content, author the wiki page and re-run `scripts/project_aura_runner.py` — never type it into the app.
- **Re-run `poetry run python -m scripts.project_aura_runner --check`** after any wiki edit to those five
  pages; it fails if the committed JSON has drifted.
- **Narrow viewport is the primary target.** Assert `scrollWidth - clientWidth <= 0` at 400px, as
  `app/e2e/runner.spec.ts` does. Three of S1's four defects were invisible at desktop width.
- Never `docker compose down -v`. Never `alembic downgrade base` — use `scripts/scratch_migrate.py`.
  Do not trust `--reload`. `VITE_*` are **build args**, not `environment`.

DELIVERABLES:
1. The capture surface, wired to existing tables, with a migration only if one is genuinely unavoidable
   — and if so, reversible, proven on a **scratch** DB.
2. The clock decision, written into the canonical architecture doc with its consequences.
3. Render-verified at a narrow viewport, labelled artifacts into `api/docs/evidence/s2/`, plus a written
   note of which interactions respond and **which are inert**.
4. Tracker + `log.md` + `index.md` reconciled, including every divergence — then the S3 boot prompt.
5. **A straight answer on whether B2's gate has moved**: how many replayed days exist, what the per-rule
   follow rates actually say, and whether the council's `DON'T BUILD` still stands. If the twenty days
   still come back empty, **say so** — S1 was built so the gate could be run, not so it could be passed.

**THIS PHASE IS NOT:** re-opening the counting basis; re-authoring model content in the app; building the
Tradezella importer (B1 killed it); provisioning Render or R2 (parked); or fixing `auth.ts` without
Paul's approval.

---

## Boot Prompt Archive (Phase S1 — the read-only Aura session runner) ✅ RUN 2026-08-12

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
