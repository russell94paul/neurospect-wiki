---
tags: [distributed-workflow, active, neurospect, neurospect-learn, aura, backtesting, tradezella, session-runner, practice]
aliases: [Session Runner, Aura Runner, Backtest Runner, The Runner]
sources: []
created: 2026-08-12
updated: 2026-08-14
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
> none may be quoted from this run.**
> **Phase S1d ✅ BUILT 2026-08-14** (see §S1d as-built). The declared week `2025-05-26 → 05-30`
> is marked up: **1 entry · 4 stand-asides · 33 bounded shapes** on session `831607`, zero
> `horizontal_line`, so Paul's markup rejection is addressed at the primitive level. Weekly cycle,
> NWOG/NDOG, R21, R22, R13 and outcome simulation are all implemented; R8 is measured and
> deliberately left UNRESOLVED. **S1c's span reproduces with all 22 day-verdicts identical**, so
> every change is additive.
> ⛔ **The one entry has NO realised outcome.** It ran 1.20R in favour / 0.41R against and then the
> bars ran out — the replay is parked at 2025-05-30 16:59 ET (confirmed at 1m on all three futures
> legs) and advancing it is forbidden. `UNRESOLVED-AT-DATA-EDGE` is a measurement gap, not a
> breakeven. **Deliverable 2's "realised outcomes" is therefore only partly met, and cannot be met
> from this session's data** — see §S1d as-built.
> ⭐ **Six more defects were found, all producing confident-looking output** — including 15
> rectangles whose end preceded their start, and the chart **silently clamping 13 of 33 shapes to
> the loaded data window** while every success signal passed.
> **⭐⭐ 2026-08-15 (S1e-b) — THE DETECTORS WERE WRONG, and Paul's Pine indicators proved it.**
> Paul supplied three `QT[✦]` indicators (saved at `s1e/reference/`) — an independent
> implementation of the same model. Four corrections, all confirmed against the `concepts/aura/*`
> pages and not just the indicator:
> **(1) There are TWO SMT objects** — swing-point SMT (3-candle pivot → qualifies *range anchors*)
> and cycle SMT (segment-extreme divergence → sets *bias*). We conflated them; the old engine built
> only the first and used it for the second's job.
> **(2) The cycles are QUARTERLY-THEORY SEGMENTS, not timeframes** — "Daily cycle" = the four 6h
> quarters of the day (18:00 NY start); "Weekly cycle" = the days within the week. Rule 22 says so
> in as many words. This is why S1e found *no weekly SMT on 91%* of entries.
> **(3) Cycle labels are off by one rung** (aura-07's naming convention).
> **(4) The TARGET was the wrong object** — TP is the HTF range's **equilibrium**, then **liquidity
> WITHIN a gap**, *"not the gap boundary"*; the engine used the range extreme, which is what
> produced the `0.0R PLANNED` trades. Entry zone is the **LTF** range, not the HTF one.
> ⭐ **R17 measured:** Pearson vs NQ — ES **+0.93** · YM **+0.83** · **CHFUSD +0.04**. At r≈0 a
> divergence carries no information, yet the indicator **ORs** the legs so it can only add signal;
> CHFUSD produced **392 of 598** 90m divergences. **Rule 17 mandates the leg, rule 15 forbids it** —
> unresolved, and R17 is itself a *(flagged)* rule.
> ⭐ **Paul re-scoped:** *"the main goal is that you get the entry levels correct rather than the
> risk management and trade management"* (he takes half off at nearest IRL, rest to final TP, SL to
> BE). **The acceptance test is now LEVEL CORRECTNESS against the chart, not expectancy** — the
> 128-trade tally and the 384-cell sweep are **historical, not results**.
> **Built:** `aura_qt_smt.py` · `aura_pd_arrays.py` · `s1e/object-inventory.md` (exhaustive object
> list + coverage matrix). **Gating item: Paul's TradingView SSMT validation.**
>
> **Phase S1b ✅ BUILT 2026-08-29 — as a standalone Artifact, NOT in the app** (Paul chose
> "Artifact first, then port"). Six sections, spine is a **19-step guided run** where each step names
> the primitive to draw with and the chart builds up from recorded S1d geometry. Every step declares
> **DRAWN / NOT-RECORDED / UNRESOLVED / ACTION**, so a step the engine never instrumented cannot be
> mistaken for a trivial one; **stand aside is a first-class branch**, not a dead end.
> ⭐⭐ **Measured coverage gap — 47% of the Aura corpus (19,427 of 41,568 words, 11 pages) is never
> drawn on**, and it is one coherent half: risk management (the corpus's largest page),
> mind/emotional control, the journaling system, and **`exercises.md` — the drill library S1 exists
> to deliver.** 45/54 rules cited; R38/R42/R44/R46 (the risk spine) and R15 uncited; R23/R37
> correctly absent. **The app is untouched and nothing is committed.**
> **Phase S1e ⏳ PART-RUN 2026-08-15 — see §Boot Prompt (S1e-b), now ⏸ GATED on Paul’s
> TradingView SSMT check.** The span
> `2023-01-03 → 2025-04-30` was declared before any outcome was computed and the engine ran it:
> **128 entries · win 40.6% · expectancy +0.038R · +4.84R total — but −7.57R without one trade**,
> and 128 entries are only **32 independent episodes**.
> ⛔ **That is NOT a verdict on Aura.** The engine **reports** the model's quality rules and
> **gates on none** of them: **R17 violated on 100%** of entries, **R18 91%**, **R30 90%**,
> **R30/R32 56%**, **R45 38%**. Enforcing them collapses the sample to **n = 0**.
> **The strategy in `rules.md` has never actually been backtested.**
> ⭐⭐ **Root cause of R17's 100%: CHFUSD shares 0 of NQ's 3,794 daily timestamps** (ES 3,794/3,794,
> YM 3,792/3,794), so the exact-timestamp join makes the Aura Asset `NOT-VISIBLE` even when
> admitted. **Admitting the 4th leg is necessary but not sufficient** — the 384-cell sweep's
> Aura-Asset axis was therefore **inert**, and a session-date join (written, works, never run over
> the full span) is the first thing S1e-b must sweep.
> ⭐ **The 3-phase screenshot blocker was a WRONG DIAGNOSIS, now solved:** the page was `hidden`
> (window minimised/occluded), so Chrome throttled it and the chart never painted — canvases at the
> default 300×150 with zero pixels while 391 bars were loaded. CDP was never broken; a hidden page
> returns a **stale frame with no error**.
> **Phase S1e (original) ✅ SUPERSEDED** (Paul, 2026-08-14, promoted ahead of S1b): *"The review has to be a number
> of valid entries and then review the number of wins and losses… I want to review a backtest session
> and see what trades you take to see if you are reading the chart and concepts correctly."* S1d's
> single unscoreable entry cannot answer that. ⚠️ **Wins/losses need forward bars, so S1e's span must
> end well before the replay edge**, and at ~1 setup per 22 weekdays **a 10-entry tally needs ~10–11
> months of intraday history** — the measured 5m history bound is S1e's STEP 0 and decides what is
> deliverable. ⚠️ **A win/loss tally measures THE ENGINE's gates as much as it measures Aura** (R6
> rejected 13/21 in S1c, 4/5 in S1d), so the rejection census ships beside the tally, not instead of
> Paul's stand-aside review.
> ⭐⭐ **MARKUP QUALITY is "paramount" (Paul) and comes FIRST** — see §MARKUP QUALITY. Accuracy is
> proven by coordinate readback; **aesthetic quality is UNVERIFIED because no session has ever seen
> the rendered markup** (CDP screenshots time out on this page). The likely cause of poor appearance
> is that S1d's style overrides used guessed, shape-specific keys, which are **silently ignored when
> wrong** — the same failure class as the coordinate clamp.

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

### S1d — A full replayed WEEK, marked up as worked examples. ✅ **BUILT 2026-08-14** (see §S1d as-built)

Paul, after reviewing S1c's output and rejecting its markup quality:

> *"Should we keep improving it so that you can successfully mark up everything required to take a
> trade entry. Then when it is hardened and polished we can get you to replay a few days focusing
> only on the NY Session. Then I can review and learn from the trades you take and try mark out
> myself after."* … *"Show your read first, but I want an entire session of trade examples — maybe
> one week to begin with. Then I will run my own session and learn from your markups and entries."*

**Why this sequencing was accepted over "go practise first".** S1c stood aside on **21 of 22 days**
(R6 alone rejected 13), and *nothing available can tell us whether that is correct*. Re-reading the
rulebook cannot settle it; Paul running unmarked days cannot settle it. **His review of the engine's
stand-asides is the only calibration instrument that exists** for whether the gates are tuned right.
That is a genuine reason to harden first, and it overrode the session's own recommendation.

**The recall concern is answered by his plan, not dropped.** Reviewing worked examples before
marking up is normally tracing rather than recall — but he runs *his own session afterwards*, which
is pre-commitment at session granularity. The test still happens; it just happens once, later, and
bigger.

### ⚠️ The base rate collides with "one week" — and the answer is a DECLARED selection

At 1 setup per 22 weekdays, **a randomly chosen week yields zero entries as the overwhelmingly
likely outcome.** So the week is **selected, not sampled**: `2025-05-26 → 05-30`, because it contains
the one known qualifying setup (the 05-30 SHORT).

⛔ **That selection must be declared on the artifact itself, loudly.** A week chosen *because* it
contains a setup carries **no information whatsoever** about how often setups occur. If Paul infers a
frequency from it, the artifact has lied to him — and this is the same failure mode as every
"analysis" gate in the estate. Print the selection basis at the top of the deliverable.

Note the week contains **Memorial Day (Mon 26 May 2025)**, a shortened session. Kept, and flagged as
a teaching point rather than filtered out.

### The deliverable is a SESSION, not a highlight reel

Paul asked for *"an entire session of trade examples"*, and the correct reading is **every day fully
marked up** — swing points, SMT qualification, ranges, PD arrays, discount/premium — with entries
where they materialise and **named stand-aside reasons where they do not** (R51). A real session is
mostly markup and sitting on your hands. An artifact showing only the trade would teach the opposite.

### S1e — N valid entries with WINS AND LOSSES, plus premium markup. ⏭ **ACTIVE** *(Paul, 2026-08-14)*

Paul, after S1d produced one unscoreable entry:

> *"The review has to be a number of valid entries and then review the number of wins and losses.
> But I want to review a backtest session and see what trades you take to see if you are reading the
> chart and concepts correctly."*
>
> *"The chart mark ups being high quality and accurate is paramount and we should try research a way
> to get them at premium aesthetic quality and accuracy."*

**Two hard constraints, both arithmetic rather than preference.** Outcomes need bars *after* each
entry, so the span must stop well short of the replay edge — S1d's entry was unresolvable *only*
because it sat on it. And at S1c's observed **1 setup per 22 weekdays**, ~10 entries needs **~10–11
months** of intraday history, so the measured 5m history bound decides whether this phase yields 10
entries or 2. That bound is STEP 0 and gets reported to Paul before any span is fixed.

**The confound that must ship with the tally:** R6 rejected 13 of 21 days in S1c and 4 of 5 in S1d.
If R6 is miscalibrated, the entries in the tally are survivors of an unvalidated filter and the
trades it *should* have taken are invisible. So `N entries` publishes alongside `M stand-asides by
failing rule` — a win rate without its rejection census is a number about a filter, and a win rate
without its R:R is meaningless outright (R44).

**Markup quality leads.** Accuracy is proven; **appearance is unverified** — no session has seen the
rendered markup because CDP screenshots time out. Drawing N entries' worth of shapes before the
appearance is checked would multiply an unverified result. See §MARKUP QUALITY.

### S1b — The walkthrough: guided setup + markup, with diagrams. *(after S1e)*

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
5. **Deliverable 3 (drawing computed levels on the chart) ✅ DONE** — added at Paul's explicit
   request after the phase closed. **8 shapes on the NQ pane**, each labelled with its rule ID and
   an `[S1c]` marker, verified by reading every shape back through the chart API and proved to
   persist across a full navigation. `createShape` returns a **Promise** in this build, so its
   return value is worthless as confirmation — enumeration is the only honest check. Shape IDs and
   a scoped removal snippet are in `api/docs/evidence/s1c/chart-shapes-drawn.md`.
   ⚠️ **They must be deleted before Paul marks that day by hand**, or a markup rep becomes tracing.
   The rendered view caught one thing the API could not: **R5's equilibrium is a computed midpoint
   that is not on NQ's 0.25 tick grid** (`21,144.625`), so the chart snapped the drawing to
   `21,144.75` — the only level not exactly where the arithmetic put it.

## S1d as-built (2026-08-14) — code is now ground truth

One new script, one modified script, one evidence folder. **No app code, no migration, no
endpoint, no table, no backend module.** The evidence layer and `app/` are untouched.

- **`api/scripts/aura_setup_engine.py`** — hardened to engine `S1d.1`. S1c's version is in
  git history; `docs/evidence/s1c/` remains the frozen record of that run.
- **`api/scripts/aura_bar_receiver.py`** — NEW. The localhost receiver S1c improvised, now a
  versioned script. Its `GET /whoami` returns a **signature string** and the browser side
  refuses to POST without it — a probe that only proves *something* is listening is not a
  liveness check (the `:8765` port-collision lesson, encoded).
- **`api/docs/evidence/s1d/`** — `week-summary.md`, `accuracy.md` (supersedes S1c's),
  `chart-shapes-drawn.md`, `chart-shapes-spec.json`, `computed-setups.md` + `.json`, and
  `bars/` (native weekly export + the 1m week).

### The week: 1 entry · 4 stand-asides

⛔ **SELECTED, not sampled** — and the report now refuses to hide that: `--selection-basis` is
a CLI input, and omitting it prints a visible warning where the basis should be.

**Four of the five stand-asides are the SAME finding restated:** every one of 26–29 May
rejects at **R6** against the same dead range (`19,103.75–20,276.75`), killed 2025-05-12 by a
close above `20,948.75`. The week is thinner in independent lessons than "4 stand-asides"
suggests, and **Paul's judgement on whether those R6 stand-asides are right reads is the only
calibration instrument that exists.**

**Memorial Day (26 May) kept, as planned** — 48 five-minute RTH bars vs 84 on a normal day.
The data guard passed, so it was evaluated as an ordinary session and rejected at R6 like the
rest: **the holiday made no difference to the verdict**, because the range was already dead.

### ⛔ Deliverable 2 is only PARTLY met, and cannot be met from this data

The boot prompt asked for **realised** outcomes. Outcome simulation is built and works — but
the one entry in the week resolves to **`UNRESOLVED-AT-DATA-EDGE`**: 1.20R in favour, 0.41R
against, then the bars stop. The replay edge is **2025-05-30 16:59 ET**, confirmed at
1-minute resolution on all three futures legs, and advancing the replay is forbidden by this
phase. Measured before any engine work, not discovered at the end.

**Any expectancy work needs bars past that edge**, which needs either a new session or Paul's
own replay. That is his call, not the engine's. The engine keeps four distinct verdicts
(`TARGET` / `STOP` / `UNRESOLVED-AT-RESOLUTION` / `UNRESOLVED-AT-DATA-EDGE`) and refuses to
collapse an unresolved trade into a breakeven.

### ⭐ Six defects found, every one producing confident-looking output

| # | Defect | Effect | Caught by |
|---|---|---|---|
| 1 | **`attach_mitigation` anchored on FVG formation, not inversion** | for an iFVG the inverting move *is* the search's first hit, so **15 rectangles had `t2 < t1`** — geometrically impossible | printing the emitted coordinates and reading them |
| 2 | **⭐ The chart silently clamps shape coords to the LOADED DATA WINDOW** | **13 of 33 shapes wrong**; 7 collapsed to zero width. `createMultipointShape` threw nothing, the promise resolved, `getAllShapes()` returned the right **count** | per-shape comparison of requested vs read-back coordinates |
| 3 | **My own session-boundary measurement mis-classified CHFUSD's WEEKEND break as its daily boundary** | 75% "support" on 3 observations; every CHFUSD NDOG would sit at the wrong boundary | separating daily/weekly by **calendar days skipped**, not gap length |
| 4 | **R8 fired on every single setup** | the check ran on the driving SMT pivot — and an SMT is *by construction* a level the other legs did not take, so "not swept on all legs" was the signal's definition, not a warning. A check that can never pass trains you to skip UNRESOLVED lines | noticing it fired 16/22 days |
| 5 | **R22 double-counted the same price** as an independent second target | on 05-30 the weekly-segment extreme **is** R35's target (`20,727.00`) | the two numbers matching to the cent |
| 6 | **The outcome walk misreported its own instrument** | claimed 5m while 1m was loaded and already walked — each coarser attempt overwrote the finer one | the `res` field saying 5 with 1m data present |

**And S1c had no FVG size floor at all**, so a **one-tick** gap was an entry candidate on
equal footing with a six-tick one — the same defect class as phantom SMT. A declared 4-tick
floor was added, its exclusions are counted per day, and it is **proved not to change S1c's
result**.

⭐ **Defect 2 is the transferable one.** S1c taught that `createShape`'s *return value* proves
nothing. S1d adds that **enumeration by count proves nothing either** — and that one chart
resolution cannot hold both a month-long range and a 5-minute box, which is R27's cascade
reappearing in the drawing layer. Written up canonically in
[[concepts/mastery/aura/chart-markup]] **§0c**.

### Regression evidence (the change is additive)

Re-running **S1c's exact span** with the hardened engine gives **all 22 day-verdicts
identical**, the same setup on the same day with the same bias, and the **same entry gap**.
Every difference is an addition. `aura_verify_record.py` still passes all 12 checks including
the no-lookahead assertion.

### Instruments proved live (a zero from an unproven instrument is not a measurement)

- **Weekly SMT detector: 13 events** over full history (6 high / 7 low). So "no weekly SMT in
  the 12-week lookback" for this week is a genuine **ZERO**. ⚠️ The nearest prior weekly SMT
  (2025-01-20, knowable 02-17) falls **~14 weeks out — just outside** the declared lookback,
  a real sensitivity to a declared constant.
- **Weekly alignment positive control:** NQ/ES/YM share **every** weekly timestamp; CHFUSD
  shares **none** — the daily result reproduced at a new resolution.
- **Session boundaries measured:** futures 17:00→18:00 ET; **CHFUSD daily = NOT-MEASURABLE**
  (no daily halt), which vindicates S1c's refusal to guess it.
- **Outcome walker:** 1m and 5m give identical MFE/MAE, as they must if 5m aggregates 1m.

### ⚠️ FLAGGED — carry these into S1b

1. **Weekly is REPORTED, not gated** (`WEEKLY_IS_A_GATE = False`). R18 is satisfied by any two
   adjacent cycles. Whether weekly confirmation should become a gate is a **calibration
   question only Paul's review answers** — the engine declines to decide it.
2. **R8 is a rulebook CONTRADICTION, not just unimplemented.** Rule 8's first sentence says
   anchor extremes only on **SMT-qualified** swings (which diverge); its second says prefer the
   extreme swept on **all** triad assets (which does not). No single swing satisfies both.
   S1b must not render this as a clean branch.
3. **The entry window can hide an earlier retest.** On 05-30 the traded iFVG had already been
   re-entered at 20:40 the previous evening, outside 08:00–16:00, so the entry taken is a
   **later** touch. R30 does not say whether a re-tested iFVG is still valid.
4. **A strict 09:30 filter would delete the only entry in this week** — R31 must stay soft.
5. **33 `[S1d]`-marked shapes are LEFT ON the NQ pane** for Paul's review, with a tested
   removal snippet in `chart-shapes-drawn.md` (removal verified 33 → 0 in-session). **They
   must be removed before he marks the week by hand**, or a rep becomes tracing.
6. **Chart left on 5m**, not the 1m it was found at. Paul confirmed in-session that changing
   timeframes is fine. Replay position untouched.
7. **Screenshots time out on this page** (30 s, "renderer may be frozen") while the DOM and
   chart API answer instantly. Not retried — coordinate readback is the stronger evidence, and
   an image could not have shown that a box's end preceded its start.

## Session Log

### 2026-08-29 — S1b BUILT as a standalone Artifact: a guided run, and a measured coverage gap

- **approach:** Paul asked for *"an interactive checklist guide for aura strategy, visuals would be
  great"*, then *"more detailed examples with marked levels and entries"*, then *"can the walkthrough
  be step by step so the user can mark"* (invoking `/living-systems-ui`). Offered app-vs-Artifact as
  an explicit choice; **he chose Artifact first, then port**, so `neurospect-learn/app` is
  **untouched** — no route, no component, no migration, no Playwright.
- **decided:** built as ONE published page rather than a React phase, so the design could be judged
  before a session is spent wiring it. `https://claude.ai/code/artifact/2da34972-c89e-4a23-b064-a02e1df302b9`
- **did:** six sections — **§01 a 19-step guided run** (`SET · PRE · M1–M12 · D0 · SIZE · MAN · EXIT ·
  REV`) where each step names the primitive to draw with and the chart builds up progressively from
  the recorded S1d geometry, switching HTF/LTF as the cascade demands; §02 the 8 checklist phases,
  tickable; §03 the live D0 tree taken from the engine's own `HARD_GATES` order; §04 the §0b
  primitive argument shown as before/after on real bars; §05 four marked-up worked examples plus four
  corpus trades; §06 the five-tier card. New scripts: `api/scripts/aura_figure_pack.py`,
  `api/scripts/aura_guided_pack.py`. Evidence + build scripts + 4 verification scripts + 15 render
  artifacts in `api/docs/evidence/s1b/`.
- **⭐ the honesty grammar is the load-bearing part:** every step declares whether the engine
  produced an artifact — **DRAWN · NOT-RECORDED · UNRESOLVED · ACTION** — so a blank chart at M1 reads
  as *"only the qualified swing was ever recorded"* and M4 reads as *"R8 contradicts itself and the
  engine refused to pick"*, rather than as a trivial step. All four states are legended on the page.
- **⭐ the failure path is first-class:** D0 refuses to advance until you say how the gates ended.
  Stand aside strikes `SIZE`/`MAN`/`EXIT` out of the rail as not-applicable and goes to the review,
  citing R51. Four of five days in the recorded week end there; a walkthrough showing only the happy
  path would misrepresent the model.
- **⛔ flagged — the levels come from detectors later found WRONG.** S1d predates the 2026-08-15
  finding (two SMT objects conflated; cycles are quarterly-theory segments; the target was the wrong
  object). Every machine example is labelled *"Machine-generated · your review is the instrument"*
  and the page never presents them as correct play. **Paul's calibration on the four R6 stand-asides
  is still the only instrument that can settle whether R6 is too strict.**
- **⭐⭐ MEASURED COVERAGE GAP — the answer to Paul's "are capturing all concepts deeply":** NO.
  **45/54 rules** are cited somewhere, but **19,427 of 41,568 corpus words (47%) across 11 pages are
  never drawn on**, and it is one coherent half — *the chart-reading half is deep, the
  survive-and-improve half is a list of tick-boxes.* Untouched: `risk-management.md` (3,411w — the
  **largest page in the corpus**), `mind-and-emotional-control.md` (2,824w),
  `journaling-system.md` (2,000w), `exercises.md` (1,571w), plus triads / aura-asset /
  discipline-systems / psychology-foundations / time-sum / learning-path / tracker.
  Uncited rules **R38 R42 R44 R46** are the risk spine; **R15** governs the very Pearson numbers the
  page already prints without naming it. **R23 and R37 are correctly absent** (R23 cannot exist in
  Tradezella — the boundary probe proved it; R37 is flagged and de-emphasised in the corpus itself).
  ⭐ **The sharpest gap is `exercises.md`: S1 exists for "repetition until the protocol is automatic"
  and the drill library that builds each section to automatic is not in the product at all.**
- **verified — at the rendered layer, over CDP** (`verify.mjs`, `verify-run.mjs`,
  `verify-branch.mjs`, `verify-leaves.mjs` in `s1b/`): all 19 steps walked, chart reveal tracks the
  step and never runs ahead, both branch paths, persistence + reset, all six tree leaves reachable,
  **tree highlights 13 rules and auto-ticks 0** (the invariant holds), no horizontal overflow at 1280
  or 400, no console errors or warnings, reduced motion lands on end state, light + dark both render.
- **⛔ flagged — two defects found in our own instruments, both of the S1c/S1d family:**
  **(1)** `chrome --headless --window-size=400 --screenshot` showed text clipped and was read as a CSS
  grid-overflow bug; measuring over CDP gave `scrollWidth 385` against a 400px viewport — **there was
  never any overflow.** `--window-size` does not set the layout viewport. A `min-width:0` "fix" was
  applied that fixed nothing. **Device metrics must come from `Emulation.setDeviceMetricsOverride`
  before any narrow-viewport claim is believed.**
  **(2)** `chip()` falls back to a bare string when a rule is not shipped, so **R14 rendered as plain
  text with no error anywhere** — the subset shipped 41 of 54. All 54 now ship and a check asserts
  every declared rule on every step renders as a real chip.
- **⛔ flagged — the Chrome extension is not connected**, so nothing was seen in Paul's own browser.
  CDP is the stronger *measuring* instrument but it is not his environment.
- **⛔ S1e-b was NOT advanced.** It is now ⏸ GATED (previously the active lane) on Paul's TradingView SSMT
  validation. This session ran S1b — which the tracker had as ⏸ NEXT — because S1e-b is blocked on
  him and he asked for this directly. **The order was changed by his request, not by drift.**
- **next:** Paul reviews the page. Then either (a) close the coverage gap — risk + psychology +
  the drill library — or (b) port §01 into `/runner` as S1b proper, or (c) run the TradingView check
  and return to S1e-b. See §Boot Prompt (S1b-b).

### 2026-08-15 — S1e-b: the DETECTORS were wrong, and Paul's Pine indicators proved it

- **approach:** ran STEP 0's regression first (green), then Paul supplied three **Pine
  indicators** (`QT[✦]Ultimate++` ×2, `QT[✦]Pro`) — an *independent implementation* of the same
  model. Read them against `rules.md` and the `concepts/aura/*` pages rather than against memory.
  All three are saved verbatim at `neurospect-learn/api/docs/evidence/s1e/reference/`.
- **⭐⭐ THE HEADLINE — there are TWO SMT objects and we conflated them.**
  **Swing-point SMT** (3-candle pivot, qualifies *range anchors*, aura-06) and **cycle
  (Sequential) SMT** (segment-extreme divergence, sets *bias*, aura-07/12) are different
  objects doing different jobs. `aura_setup_engine.py` built only the first and then used it for
  the second's job. The new `aura_qt_smt.py` builds only the second. **The model needs both.**
- **⭐ THE CYCLES ARE QUARTERLY-THEORY SEGMENTS, NOT TIMEFRAMES.** "Daily cycle" = the four
  **6-hour quarters of the day** (day starts 18:00 NY); "Weekly cycle" = the **days within the
  week**. Confirmed by the corpus, not just the indicator — rule 22: *"between quarters within a
  week, between days within a session, between hours."* This is why S1e reported **no weekly SMT
  on 91%** of entries: we hunted pivots on weekly BARS over a 12-week lookback.
- **⭐ Cycle labels are off by one rung.** aura-07: *"mark swing points on the weekly time frame …
  what you're looking at is **monthly** cycle SMT."* Independent of the segment fix.
- **⭐ SMT lifecycle + nesting were both wrong.** An SSMT stays **active until price takes the
  diverged extreme** (R23), and "Sequential" is **activity OVERLAP of ≥2 cycles**, not
  co-formation. Implemented in `aura_qt_smt.py`.
- **⭐ R17 measured, and it fails R15's premise.** Pearson on daily returns vs NQ:
  **ES +0.9291 · YM +0.8319 · CHFUSD +0.0406** (n=2,931, session-date join). At r≈0 agreement is
  not expected, so a divergence carries no information — and the indicator **ORs** the legs
  (`array.set(X_SSMT,6,true)` from both the tertiary AND the quad), so an uncorrelated leg can
  only ADD signals. CHFUSD produced **392 of 598** 90m divergences; dropping it roughly **halves**
  every Sequential count. ⛔ Rule 17 mandates the leg, rule 15 forbids it — a real, unresolved
  contradiction, and R17 is itself a *(flagged)* rule.
- **⭐ The TARGET was the wrong object.** `gaps.md`/aura-12: TP is **equilibrium of the HTF range**,
  then **liquidity WITHIN a gap** in discount/premium — *"that internal level is the precise
  target, NOT the gap boundary."* The engine used **the range extreme**, which is what produced
  the `0.0R PLANNED` trades. Entry zone is likewise the **LTF** range, not the HTF one.
- **⭐ Paul re-scoped (2026-08-15):** *"the main goal is that you get the entry levels correct
  rather than the risk management and trade management."* He takes **half off at nearest IRL**,
  rest to final TP, SL to breakeven — so the engine's single-target model measured a trade he
  would never take. **The acceptance test is now LEVEL CORRECTNESS checked against the chart, not
  expectancy.** The 128-trade tally and the 384-cell sweep are **historical**, not results.
- **did:** `aura_qt_smt.py` (segment SMT + lifecycle + nesting); `aura_pd_arrays.py` (four gap
  types + "what lies within" + look-left/zoom-in fallbacks + confluence stacking);
  `s1e/object-inventory.md` (exhaustive object list built from the concept pages, with a coverage
  matrix); `s1e/reference/README.md`; killed the 72-config sweep as obsolete.
- **flagged — nobody implements these**, not us and not the indicator: range nesting · liquidity-
  within-gap fallbacks · confluence stacking · candle-level confirmation · cross-asset skip · the
  patience rule. **The indicators do NOT define iFVG at all** (0 matches across all three
  scripts), so that definition rests on the Aura corpus alone and cannot be cross-checked.
- **flagged — two bugs found in my own new PD code within an hour of writing it:** `lifecycle()`
  overwrote `kind` on inversion, **relabelling every NDOG/NWOG as an iFVG** (208 → 204 after fix,
  4 NDOGs recovered); and inversion was checked before mitigation, so **mitigation was never
  recorded**. Both found by reading the emitted numbers, not by anything erroring.
- **verified:** STEP 0 regression **0 differences** vs pre-refactor default (the session-date-join
  edit is now proven safe); the 3 `.pine` files verified populated (136K/132K/148K, placeholders
  gone); NDOG session gaps confirmed present by direct measurement before trusting the detector.
- **next:** Paul runs the **TradingView SSMT validation** (steps + expected active-sets are in the
  boot prompt). Everything downstream inherits from that detector, so no further layers until it
  passes.

### 2026-08-14/15 — S1e PART-RUN: 128 entries measured, and the strategy was never actually tested

- **approach:** fixed the blocking screenshot problem first, then STEP 0's history bound, then the
  declared span, then the tally — reporting each measurement to Paul before using it.
- **⭐ the headline is again a defect, and it is the biggest one yet:** the engine **reports**
  Aura's quality rules as soft branches and **gates on none of them**, so the 128-entry tally is a
  LOOSE SUPERSET of Aura with every quality filter off — **R17 violated on 100%** of entries,
  **R18 91%**, **R30 90%**, **R30/R32 56%**, **R45 38%**. Turning the preferences back on collapses
  the sample to **n=0** before the filters run out. So *"expectancy +0.038R"* is **not a verdict on
  Aura** — that measurement was never about Aura.
- **⭐⭐ root cause of the R17 100%:** **CHFUSD shares 0 of NQ's 3,794 daily timestamps** (ES shares
  3,794/3,794, YM 3,792/3,794). The Aura Asset's daily bars sit on a different session boundary, so
  the exact-timestamp join can never match and the leg reads `NOT-VISIBLE` even when admitted.
  **Admitting the 4th leg is necessary but NOT sufficient** — which is why the sweep's Aura-Asset
  axis was **inert** and question 1 has still not been tested.
- **decided:** span `2023-01-03 → 2025-04-30`, chosen by Paul from the measured history bound and
  written down **before** any outcome was computed (`declared-span.md`). Sweep grid + reporting
  rule **pre-registered** before running (`sweep-preregistration.md`).
- **did:** solved the 3-phase screenshot blocker; measured the 5m history bound; 24 bar exports;
  `aura_s1e_pack_bars.py`, `aura_s1e_derive_15m.py`, `aura_s1e_sweep.py`; added 5 config axes to the
  engine; ran the span (128 entries) and a 384-cell sweep; wrote `execution-audit.md`.
- **⭐ the screenshot blocker was a WRONG DIAGNOSIS, not a broken tool.** Three phases recorded
  *"`Page.captureScreenshot` times out, renderer may be frozen"*. The page was **`hidden`** —
  window minimised/occluded — so Chrome throttled it and TradingView never painted: canvases sat at
  the default 300×150 with **zero** non-transparent pixels while 391 bars were loaded. Un-minimise
  and it paints instantly. **No new API was needed.** Focus is irrelevant; **occlusion** is the
  trigger, and a hidden page returns a **stale frame with no error** — caught in the act when
  hiding all 33 shapes changed the canvas hash not at all.
- **flagged — two instrument artefacts that would have become false findings:** CHFUSD 5m first
  read gave **678 bars / 4 days** (lazy loading — 177,074 after nudges); **NQ 15m is genuinely
  capped** at 4,492 bars from 2025-03-23 (reproduced by two independent probes), recovered by
  aggregating 5m with a positive control (4,489 buckets, **0 mismatches**).
- **verified:** S1c regression through the NEW export pipeline — 20/22 days identical, same setup,
  same bias; the 2 differences are exactly the days S1c reported `DATA` for lack of lookback.
  Config refactor re-verified at **0 differences**. Per-shape markup style diff **0 drift / 33**.
- **⛔ flagged — UNVERIFIED WORK ON DISK:** the **session-date join edit** to
  `aura_setup_engine.py` has **not** had its regression run (Paul's laptop was dying). The default
  path is *believed* unchanged but is **not proven**. Run that first next session.
- **next:** superseded by the 2026-08-29 session — see §Boot Prompt (S1b-b), the active lane.

### 2026-08-14 — S1d BUILT: the week is marked up, and the one trade cannot be scored

- **approach:** measured the hard constraint *first* — walked the 05-30 trade forward on the
  existing 5m bars before writing any engine code, and found neither stop nor target is
  reached before the data edge. Reported that collision with deliverable 2 immediately rather
  than discovering it at sign-off. Then exported the missing cycles (native weekly, 1m week),
  hardened the engine, and gated every change on re-running S1c's span unchanged.
- **decided:** weekly is a **reported rung, not a gate** — promoting it would delete setups on
  no calibration evidence, and that judgement is Paul's. R8 is **measured but not resolved**,
  because the rulebook contradicts itself on it. 1m is admitted for **outcome sequencing and
  R13 zoom-in only**, never as a signal cycle (R28).
- **did:** engine → `S1d.1` (weekly cycle, NWOG/NDOG on measured boundaries, R21, R22, R13
  both routes, R8 anchor check, outcome simulation, bounded shape spec, declared FVG floor,
  `--selection-basis`); new `aura_bar_receiver.py`; native weekly + 1m exports; ran the
  declared week (1 entry, 4 stand-asides); drew and verified **33 bounded shapes**, zero
  `horizontal_line`; wrote `week-summary.md`, `accuracy.md`, `chart-shapes-drawn.md`.
- **⭐ flagged — the headline is again a defect, not a trade:** the chart **silently clamped 13
  of 33 shapes** to the loaded data window while every success signal passed, and 15
  rectangles had been emitted with their end before their start. Also: **my own** session-
  boundary measurement classified CHFUSD's weekend break as its daily boundary, and **R8's
  check could never pass** by construction. The cheap check that found most of them was
  reading the emitted numbers like a trader, not confirming the code ran.
- **flagged — scope honesty:** deliverable 2's *realised* outcomes is **only partly met** and
  cannot be met from this session's data. Deliverable 3's "day-by-day shape" is thinner than
  it looks: 4 of 5 stand-asides are one finding restated.
- **verified:** S1c regression — 22/22 day-verdicts identical, same setup, same entry gap;
  `aura_verify_record.py` 12/12 including no-lookahead; per-shape coordinate readback 0 drift
  on both markup sets; 0 `horizontal_line` by enumeration; shapes persist 33→33 across a full
  navigation; removal proved 33→0; weekly SMT detector proved live (13 events); weekly
  alignment positive control; 1m/5m outcome cross-check identical.
- **next:** **S1b** — the guided walkthrough and the **D0 decision tree**, which does not
  exist in the app (18 routes, none of them a tree). Paul went looking for it because this
  tracker's `✅ DECIDED` heading read as `✅ DONE`; heading corrected. **Before S1b builds
  anything, Paul should review the week's 1 entry and 4 stand-asides** — that review is the
  calibration input S1d exists to produce.

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

## Boot Prompt Archive (Phase S1d — a full replayed week, marked up) ✅ RUN 2026-08-14

> **HISTORY — do not execute.** See §S1d as-built for what it produced, and note two places it
> asked for something the data cannot give: **realised outcomes** (the replay edge forbids them)
> and **deeper 5m history** (not needed at one week).

**Launch:** `claude --model opus[1m]`, `/effort high`. This phase produces the artifact Paul will
**learn the model from**. Wrong reads teach wrong, and S1c proved that is not theoretical — it
shipped five defects whose output looked competent at every stage.

**Task: mark up one full replayed week as worked examples, hardened enough that everything
required to take a trade entry is on the chart.** Deliver a session, not a highlight reel.

### ⛔ READ THESE FIRST — in this order

1. Wiki `CLAUDE.md` — code is ground truth, the MANDATORY reconciliation checklist, Rules #3/#4/#6,
   Context Management (tell Paul at >50%). **Paul handles git unless he asks in-session.**
2. This tracker: **§S1c as-built** (the five defects — do not reintroduce them) and **§S1d above**
   (the declared week, and why it is selected rather than sampled).
3. `neurospect-learn/api/docs/evidence/s1c/accuracy.md` — **the whole file.** It states what the
   engine does not do, and every gap in it is scope for this phase.
4. [[concepts/mastery/aura/chart-markup]] **§0b — Markup primitives**. Paul rejected S1c's markup:
   infinite horizontal lines instead of shapes bounded to where the level applied. **This is a
   correctness rule, not a style note** — an infinite line contradicts R6 and R7.
5. [[concepts/mastery/aura/rules]] — canonical wording.
6. `~/.claude/skills/web-automation/claude-in-chrome-driving.md` — **required.** Also note:
   `createShape` returns a **Promise** in this build, so its return value proves nothing;
   enumerate with `getAllShapes()` / `getShapeById()` to confirm anything.

### The decisions Paul already made — do not reopen them

| Decision | Value |
|---|---|
| Artifact order | **Worked examples first** — his read visible up front. He runs his own session afterwards; that is where recall gets tested |
| Span | **One week**, `2025-05-26 → 05-30`, expandable later if he asks |
| Selection | **Declared, not sampled** — chosen because it contains the known 05-30 setup |
| NY session | **08:00–16:00 ET** (covers the AM killzone). R31's 9:30 preference stays a **soft branch**, never a filter — the known setup enters 08:05 and a strict 09:30 window deletes it |
| Markup | **Bounded shapes only** — rectangles/rays with computed start *and* end |

### What must be hardened — this is the phase's real work

The engine currently computes a setup but does **not** mark up everything needed to take one.
From `accuracy.md`'s own gap list:

1. **Bounded markup primitives** (Paul's rejection). The engine *already computes every boundary
   it needs* — gap `formed_time`/`inverted_time`, the range's `move_to`, R6's `broken_by` — so this
   is a drawing change, not new analysis. Rectangles for PD arrays formation→mitigation; rays for
   live levels; **range boundaries terminated at the invalidating close**.
2. **NWOG / NDOG** (R11) — declared in the rulebook, unimplemented. Needs a per-symbol session
   boundary; CHFUSD's do not match the futures', which is why S1c refused to approximate it.
3. **The weekly cycle** — absent entirely. Weekly→daily is R18's canonical nesting pair, so its
   absence weakens every Sequential SMT claim the engine makes. Export `W` natively; do **not**
   aggregate daily bars into fake weeks.
4. **R21** cross-cycle gap-pairing · **R22** extreme-of-the-larger-segment targeting · **R13**
   look-left / zoom-in for liquidity · **R8**'s false-sweep tiebreak (or keep R8 UNRESOLVED and say so).
5. **⭐ Outcome simulation.** The engine plans entry/stop/target and never walks price forward, so
   every `R` is **planned, not realised**. Paul asked to learn from *"the trades you take"* — a trade
   with no outcome is an intention. Walk the 5m/1m bars forward: stop-first or target-first, the bar
   it happened on, and the realised R. Where both are touched inside one bar, that is
   **UNRESOLVED at this resolution** — say so, do not guess the sequence.
6. **Deeper 5m history** — S1c pulled ~26 days via `setVisibleRange`. One week needs far less, so
   this is *not* blocking here; it becomes blocking the moment Paul expands the span.

### ⚠️ THE TRAPS — every one of these is measured, not hypothetical

- **Lookahead.** `known_at` must come from real bar timestamps plus a bar for closure, never
  calendar arithmetic. This bug contaminated **75%** of S1c's output while the log reported
  confident dates. **Re-run `aura_verify_record.py` and keep its no-lookahead assertion passing.**
- **The engine must stay auditable.** Every logged line keeps `rule ID · computed value · source bar`.
- **Never resolve a judgement rule.** R9/R8/R31 stay `UNRESOLVED` or render as soft branches. An
  engine that resolves everything cleanly teaches Paul that Aura is deterministic, which it is not.
- **State the selection basis on the artifact.** The week was chosen because it contains a setup, so
  it carries **zero** information about frequency. Print it at the top.
- **QUARANTINE holds.** These are machine-generated tutorial artifacts: no `evidence_assets`, no rep
  credit, nothing feeding the streak, calibration or the Readiness Gate. Every drawn shape keeps a
  visible machine-generated marker.
- **Clean up the chart.** Anything drawn onto session `831607` must be removable by a scoped snippet
  and **must be deleted before Paul marks that week himself** — pre-drawn levels turn a rep into
  tracing. Verify `0` shapes after removal, by enumeration and after a navigation.

### DELIVERABLES

1. The hardened engine (still versioned, still re-runnable, still no app/DB changes).
2. **One artifact per trading day** in the declared week: the marked chart (bounded shapes), the
   rule log, the entry **or the named stand-aside reason**, and — where there is an entry — the
   **realised** outcome in R.
3. A week-level summary carrying the **declared selection basis** and the day-by-day shape.
4. An updated `accuracy.md`: what is now implemented, what remains deferred, and what the week's
   results do and do not support.
5. Tracker + `log.md` + `index.md` reconciled; then hand back to **S1b**.

**THIS PHASE IS NOT:** writing to the database or the evidence layer; building the walkthrough UI
(S1b); quoting a hit rate, win rate or expectancy from a selected week; advancing Paul's replay
position; or leaving shapes on his chart.

---

## ⭐⭐ MARKUP QUALITY — Paul, 2026-08-14: *"paramount"*. Do this FIRST, inside S1e's STEP 0

> *"The chart mark ups being high quality and accurate is paramount and we should try research a
> way to get them at premium aesthetic quality and accuracy."*

**Accuracy is now proven; AESTHETIC QUALITY IS UNVERIFIED, and that must be stated plainly.** S1d
proved the *geometry* by per-shape coordinate readback (0 drift, 33/33) — but **no session has ever
seen the rendered markup.** `Page.captureScreenshot` times out on this page (30 s, "renderer may be
frozen") while the DOM answers instantly, so every S1c/S1d visual claim rests on coordinates, not on
an image. Paul's own consumer-layer rule applies: *the rendered surface a user sees* is the
consumer's layer, and it has not been checked.

### The blocking item: get an image WITHOUT CDP

Everything else is unjudgeable until this works. Do not retry `Page.captureScreenshot`.

- The **TradingView Charting Library screenshots itself** — probe for `takeScreenshot()` /
  `getScreenshotData()` on the widget and on `chart(i)`, plus the `onScreenshotReady` /
  `screenshot_ready` subscription. This path never touches the broken CDP route.
- Failing that, the chart iframe is same-origin (`blob:`) so its `<canvas>` layers can be
  composited and read with `toDataURL()`, then POSTed to `api/scripts/aura_bar_receiver.py` — the
  receiver already lands arbitrary payloads to disk and is the natural sink for a PNG.

### ⚠️ The likely cause of poor appearance: override keys are SILENTLY IGNORED when wrong

S1d passed a single guessed bag of overrides to every shape —
`{linecolor, color, backgroundColor, transparency, linewidth, showLabel, textcolor}` — but
**TradingView override keys are shape-specific**, and an unrecognised key is dropped without error.
**This is the same failure class as the coordinate clamp**: accepted, no exception, wrong result.
So the drawn shapes may be carrying library defaults, not the colour convention.

**Verify, don't assume:** read `getShapeById(id).getProperties()` back and **diff the style fields
against what was intended**, per shape, exactly as the geometry is diffed. Expect roughly
`rectangle` → `color` · `backgroundColor` · `fillBackground` · `transparency` · `linewidth` ·
`linestyle`; `trend_line`/`ray` → `linecolor` · `linewidth` · `linestyle` · `extendLeft`/`extendRight`
· `showLabel` · `textcolor` · `fontsize`. Confirm the real names from the read-back, not from memory.

### What "premium" means concretely here — the quality bar to design against

[[concepts/mastery/aura/chart-markup]] §Colour convention already fixes the palette; these are the
things it does not yet say, and they are what separate a readable chart from a wall of ink:

1. **Visual hierarchy.** Zones must *recede* (grey, dashed, high transparency, behind everything);
   range boundaries are structural (white, solid); SMT swings are the load-bearing filter (yellow,
   and visibly distinct from unqualified swings); execution objects sit in front. Encode this as
   **line-width and z-order rules**, not just colour.
2. **Label collision is a real problem at this density.** 33 labelled objects on one pane will
   overlap. Candidate fix: label only structural objects and the **traded** gap, set
   `showLabel:false` on the context gaps, and move the `[S1d]`-style marker into a single legend
   object rather than repeating it 33 times — the marker requirement is *visible provenance*, which
   one unmissable label satisfies better than 33 competing ones.
3. **Fill vs outline.** Zone rectangles want a high-transparency fill; overlapping gap boxes are
   more legible outlined or very lightly filled, or adjacent boxes merge into one blue smear.
4. **Density is still an open question.** S1d cut 27 boxes → 15 (a declared 4-tick FVG floor, an
   M6 zone filter, and excluding gaps that inverted *after* the entry — hindsight has no place on the
   chart that justifies the entry). **15 may still be too many.** Consider separating *"the traded
   gap plus its immediate context"* from *"the full census"* as two views, and **say what was
   omitted** either way — a silent cap reads as "there was nothing there".
5. **Only then judge it.** Capture the image, look at it, and iterate against the bar above. An
   aesthetic claim with no image behind it is worth nothing, which is precisely the position S1d
   ended in.

⛔ **Accuracy still outranks aesthetics where they conflict.** A prettier chart that asserts a level
applies when R6 says it died is worse than an ugly correct one — that is exactly what the infinite
horizontal lines did.

---

## Boot Prompt (Phase S1b-b — close the coverage gap, or port) ⏭ ACTIVE

**Launch:** `claude --model opus[1m]`, `/effort high`. Written 2026-08-29 at a context checkpoint.
S1b shipped **as an Artifact, not in the app** — read §Session Log 2026-08-29 before anything.

### ⛔ STEP 0 — before any new work

1. **Everything is uncommitted, in BOTH repos, and it is now a lot.** `neurospect-learn` carries the
   whole S1d/S1e body *plus* `api/docs/evidence/s1b/` and two new scripts
   (`aura_figure_pack.py`, `aura_guided_pack.py`); `neurospect-wiki` carries this tracker, `log.md`
   and `index.md`. **Paul commits.** Ask before touching git.
2. **The app is untouched and must stay that way until Paul says otherwise.** `/runner` has no
   guided run in it. A green tick in this tracker means the *design* is settled, never that the code
   exists — the same distinction that sent Paul looking for a decision tree that was never built
   (2026-08-14).
3. **⛔ Do NOT re-derive the coverage measurement.** It was run: `45/54` rules cited, **19,427 of
   41,568 corpus words (47%) never drawn on**. The script is
   `neurospect-learn/api/docs/evidence/s1b/`-adjacent (`coverage.py`, in the session scratch — re-create
   from the numbers above if needed, it is ~50 lines). Re-running it is fine; re-*discovering* it is
   a wasted hour.
4. **S1e-b is ⏸ GATED on Paul's TradingView SSMT validation** (see its own prompt below) and
   nothing this session did touches that gate. It was the active lane until 2026-08-29.

5. **⚠️ A PARALLEL LANE EXISTS, and it was written the same day.**
   `processes/distributed-workflow/active/platform-architecture.md` (created 2026-08-29 04:50, still
   **untracked in git**) carries its own `⏭ ACTIVE` prompt — Phase P0b, after a five-lens council —
   and states that three trackers were ACTIVE when it was written. **That statement is now stale in
   one respect: this tracker's active lane is S1b-b, not S1e-b** (S1e-b was demoted to ⏸ GATED on
   2026-08-29). It was left unedited deliberately — it is another session's live work and clobbering
   it would be exactly the overlap failure the reground rules exist to prevent. **Tell Paul the two
   lanes exist and let him pick; do not merge them.**

### ⭐ THE DECISION THAT OPENS THIS SESSION — ask Paul, do not assume

Three routes, and they are genuinely different work. **Ask which.**

**(a) Close the coverage gap.** The measured finding: the chart-reading half is deep, the
survive-and-improve half is tick-boxes. Three named gaps, in the order they matter:
  - **The drill library.** `concepts/mastery/aura/exercises.md` (1,571w) + `learning-path.md` +
    `tracker.md`. **This is the sharpest one** — S1 exists for *"repetition until the protocol is
    automatic"* and the layer that delivers repetition is not in the product at all.
  - **The risk spine.** `risk-management.md` is the **largest page in the corpus** (3,411w) and the
    guided run reduces it to one tick. **R38 R42 R44 R46** are cited nowhere. R44 (expectancy, with
    the break-even formula `1/(1+R:R)`) must be *taught* even though the page correctly claims no
    expectancy number of its own.
  - **The psychological half.** `mind-and-emotional-control` + `psychology-foundations` +
    `discipline-systems` + `journaling-system` = 7,742 words, zero coverage — while §06 already
    asserts *"dOoMeR puts the value here."* The page makes the claim and does not teach it.
  - Also uncited: **R15** (triad selection is math-first, Pearson on daily returns over 2–3 years)
    — which is the rule the CHFUSD **+0.04** number already on the page is measuring against.
  - ⚠️ **R23 and R37 are correctly absent.** R23 cannot exist in Tradezella (the boundary probe
    proved it); R37 is flagged and de-emphasised in the corpus itself. Do not "fix" them.

**(b) Port §01 into `/runner` as S1b proper.** Bigger than it was on 2026-08-27: 19 steps, the
progressive chart reveal, the branch, the artifact-state grammar. Needs `e2e/runner.spec.ts`
extended, render-verification at 400px, and evidence into `s1b/`. ⚠️ It would build on top of the
**uncommitted 2026-08-20 UI overhaul** — see the deployment/UI note below.

**(c) Run the TradingView SSMT check and go back to S1e-b.** Only Paul can do the check.

### ⚠️ THE OTHER OPEN THING — a workstream with no tracker

The **2026-08-20 UI overhaul** in `neurospect-learn` (brand system, dark mode that was *built but
unreachable*, motion layer, 166 classes swept to semantic tokens, public landing page, `/settings`,
plus `check-tokens` and `check-contrast` gates that were both deliberately broken to prove they can
fail) has **no tracker, no `log.md` entry and no `index.md` line**, and is uncommitted. Evidence is
good — `api/docs/evidence/ui/README.md` — but nothing in the wiki points at it.
`learning-platform-ui.md` is **✅ CLOSED (2026-07-25)** and is not its home. **Paul agreed a new
`platform-design-system.md` tracker is needed; it has not been written.** Offer it early.

### WHAT S1b ACTUALLY BUILT

`https://claude.ai/code/artifact/2da34972-c89e-4a23-b064-a02e1df302b9` — republish by passing that
URL, or the same file path if the session already published it.

Six sections: **§01 the 19-step guided run** · §02 the 8 checklist phases · §03 the live D0 tree ·
§04 the markup-primitive argument · §05 four marked-up worked examples + four corpus trades ·
§06 the five-tier card. Source and build in `api/docs/evidence/s1b/` — `build_artifact.py` assembles
`aura-protocol.src.html` + `part2/3/4.js` + the figure packs; `worked.py` and
`api/scripts/aura_guided_pack.py` produce the figures.

**Two invariants that must survive any edit:**
- **The tree never auto-ticks a rule.** Verified: 13 highlighted, 0 checked. Manufacturing adherence
  the user did not assert is the same failure as batch-ticking 33 boxes.
- **Every step declares its artifact state** — DRAWN / NOT-RECORDED / UNRESOLVED / ACTION. A blank
  chart at M1 must keep reading as *"only the qualified swing was recorded"*, never as a blank step.

### ⚠️ INSTRUMENT LESSONS EARNED THIS SESSION — do not re-learn these

- **`chrome --headless --window-size=W` does NOT set the layout viewport.** A 400px screenshot showed
  text clipped; CDP measured `scrollWidth 385` against a 400px viewport — **there was no overflow at
  all**, and a `min-width:0` "fix" was applied that fixed nothing. Use
  `Emulation.setDeviceMetricsOverride` before believing any narrow-viewport claim.
- **`chip()` degrades a missing rule to plain text with no error.** R14 rendered untagged because the
  subset shipped 41 of 54 rules. All 54 now ship; the check asserts every declared rule renders as a
  real chip. Same failure class as the silently-ignored style keys and the silent coordinate clamp.
- **The Chrome extension is not connected.** Everything was verified over CDP through headless
  Chrome. That is the stronger *measuring* instrument, but **nothing has been seen in Paul's own
  browser.**
- The Playwright MCP runs in a container and cannot reach a host `127.0.0.1` server; `host.docker.internal`
  was blocked. Serve locally and drive headless Chrome over `--remote-debugging-port` instead — and
  serve `.html` as `text/html; charset=utf-8` or the page mojibakes (`serve.py` in `s1b/`).

### THIS PHASE IS NOT

Advancing the replay · writing to the database or the evidence layer · claiming an edge or an
expectancy · presenting the S1d levels as correct play (the detectors under them were found wrong on
2026-08-15) · committing anything without asking Paul.

---

## Boot Prompt (Phase S1e-b — finish the sweep, then review) ⏸ GATED on Paul's TradingView SSMT check

**Launch:** `claude --model opus[1m]`, `/effort high`. Written 2026-08-15 mid-phase; S1e is
**PART-RUN, not finished**. The S1e prompt below it is **✅ SUPERSEDED — do not re-run its STEP 0**;
its measurements are done and recorded.

### ⛔ STEP 0 — THE FIRST THING, BEFORE ANY NEW WORK

1. ✅ **STEP 0's regression RAN 2026-08-15 and is GREEN** — 0 differences vs the pre-refactor
   default; the only 2 differences from S1c's published run are the known `DATA → R3` lookback
   days. The session-date-join edit is proven safe. **Do not re-derive this.**
2. ⏳ **THE GATING ITEM IS PAUL'S TRADINGVIEW CHECK — see §SSMT VALIDATION below.** Everything
   downstream (range, premium/discount, entry) inherits from the rebuilt SMT detector. **Do not
   stack layers on it until it passes.**
3. **Everything is uncommitted** — all of S1d *and* all of S1e, plus 8 scripts. Paul commits.

### ⏳ SSMT VALIDATION — what Paul is running, and what to do with the answer

**Indicator:** `s1e/reference/qt-ultimate.pine` (script 2, **no quad**, so the Aura Asset cannot
contribute and it matches our index-legs-only sheet). TradingView, **NQ1!**.
**Settings:** Calculation Mode `Auto` · Type of SSMT **`Normal`** (default is "All") · Triad
`Auto` (confirm it resolves to ES+YM) · Normal Daily + Normal Weekly **on**, everything else off ·
Timezone `UTC-4` (correct — late May is EDT, matching our DST-aware calc) · Day Start Hour `18`.

⚠️ **Chart TF gates which cycle is visible**: Daily-cycle shows only on **15m–30m**; Weekly-cycle
only on **1H–3H**. Two passes.
⚠️ **The indicator DELETES invalidated SSMT lines**, so scrolling back shows almost nothing. Use
**Bar Replay**.

Expected **active sets** (index legs, computed by `aura_qt_smt.py`):

| Replay to (ET) | expected |
|---|---|
| Tue 2025-05-27 12:30 | Daily **LONG** vs YM, NQ 21,145.00 → 21,192.75 |
| Wed 2025-05-28 15:00 | same, still live |
| Thu 2025-05-29 10:00 | same, still live |
| Fri 2025-05-30 15:00 | Daily **SHORT** vs ES, NQ 21,412.25 → 21,421.00 |
| Fri 2025-05-30 17:00 (**1H**) | Weekly **LONG** vs YM, NQ 21,301.00 → 21,071.50 |

Caveats to give Paul: the indicator draws an SSMT **live as the segment develops** while we date it
at the **segment close** (no lookahead), so it may appear earlier — what matters is presence at the
checkpoint. Price offsets by a constant are contract/backadjustment, not a detector error.

**If it PASSES** → build in this order: range framing (A3/A4/A5 on the segment model) →
premium/discount vs the **LTF** range (D2) → wire the PD arrays (already built) → entry level.
**If it FAILS** → fix the detector before anything else; do not proceed on a broken foundation.

### WHERE S1e GOT TO

**The tally (baseline config, declared span `2023-01-03 → 2025-04-30`, 607 weekdays):**
**128 entries · 52 TARGET / 76 STOP · win 40.6% · avg win +1.56R · avg loss −1.00R ·
expectancy +0.038R · total +4.84R · median −1.00R.** All 128 resolved, 0 unresolved.
**−7.57R without its single best trade.** 128 entries = **32 episodes**; two carry the whole result.
Rejections: R6 335 · R3 81 · R29 56 · R35 3 · R30 2 · DATA 2.

**⛔ Do not quote that as a verdict on Aura.** The engine gates on **none** of Aura's quality rules:
R17 violated 100% · R18 91% · R30 90% · R30/R32 56% · R45 38%. Enforcing them → **n = 0**.
The strategy in `rules.md` **has never actually been backtested**.

### ❌ OBSOLETE 2026-08-15 — the sweep below was KILLED, do not resume it

The 72-config sweep varied a **12/16/20/26-week weekly lookback that does not exist** under the
segment model ("weekly cycle" = the days within the week). Running it would produce a tidy table
nobody should read. `sweep/sweep-results.json` (run 1, 384 cells) stays on disk as **history**.
The section below is kept only so the decision is auditable.

### ~~THE ONE THING THAT MUST HAPPEN NEXT — the sweep did NOT test question 1~~

Paul answered **yes to all four** open questions and said *"exhaust all configurations then
review."* A 48-run / 384-cell sweep exists (`sweep/sweep-results.json`) — **but its Aura-Asset axis
is INERT.** Admitting the leg only removed a refusal note; it changed **not one trade**, because
**CHFUSD shares 0 of NQ's 3,794 daily timestamps** and the exact-timestamp join returns nothing.

`--aura-asset-join session_date` was written to fix exactly this and **works** — in a half-year
probe the leg finally voted (`TOOK 4 · DID-NOT-TAKE 44 · WITHIN-NOISE 1`, 48 → 49 setups). It has
**never been run over the full span**.

**So: amend the pre-registration IN WRITING (say the axis was added mid-sweep and why — the
original axis was inert), then re-run the sweep with the join axis added:**

| Axis | Values |
|---|---|
| Aura Asset | `(off, timestamp)`, `(on, timestamp)`, **`(on, session_date)`** |
| Weekly lookback | 12, 16, 20, 26 |
| Retest | report, require_first, session_first |
| Zone ref | htf, ltf |

= **72 runs** (skip `off × session_date`, it is a no-op) × 8 post-hoc enforcement filters.
`aura_s1e_sweep.py` needs the axis added to its grid.

⛔ **The pre-registered reporting rule still binds:** publish **every** cell; adopt **no** cell on
expectancy alone; cells under **n=20** are `UNDERPOWERED`; record `total_r_ex_best` everywhere.
384→576 cells against ~32 independent episodes **will** produce a flattering winner by chance.

### What the sweep already established (do not re-derive)

- **`session_first` takes R30 violations 89.8% → 0% while keeping all 128 entries** — every "not the
  first retest" case was an **overnight** touch, i.e. an artefact of the 08:00–16:00 window.
- **`zone=ltf` genuinely changes the read** (violations 56.2% → 51.6%, 38.5% → 30.8%).
- **Weekly SMT is genuinely rare** — 12 → 26 weeks only moves "no weekly SMT" 91% → 83.6%.
- Weekly-lookback and zone-ref act **through branches**, so they move only the enforcement cells,
  not the base cells. That is by design, not a broken axis.

### ⚠️ THE CHART — read before touching it

- **33 `[S1d]` shapes are still on NQ** (session `831607`), 0 on ES/CHFUSD/YM. Paul has **not**
  reviewed that week and **does not intend to** — he wants a week with real executions instead — so
  they are **cleared for removal**.
- ⛔ **THE REMOVAL SNIPPET IN `s1d/chart-shapes-drawn.md` IS NOW UNSAFE.** It matches on label text
  starting `[S1d]`, and this session **cleared the text on 22 of the 33 shapes** as part of the
  restyle. It would delete 11 and silently leave 22. **Remove by id** (all 33, captured before the
  text was cleared):

  ```
  DpXZGc V1tss5 8TH79V pPhrhQ eJE9Qf pRq4zz l3UtTu c9k1W2 d7gq6D Ezbo9f HySfUL tUUTgR 7LSSkm
  NeWy5G 2DkjrO DEoIbp NyOAuu kk3LGD gpFqdk SomsQh r3BmYz MZXFE6 KAwTMv xLO3E1 gFdFpl LzoW04
  0XrWOh P3jOLg 0O7ZOa daacPF pgTgVn v23oek SU8xSr
  ```
  Verify **33 → 0**, and re-verify after a reload (shapes are server-side).
- **Replay is UNTOUCHED.** Session clock reads **Sun 2025-06-01 17:00 ET**; last futures bar is
  `2025-05-30 20:55 UTC` (Friday close). ⚠️ The tracker's older claim that the replay is "parked at
  2025-05-30 20:59 UTC" is the **data edge of one leg**, not the replay position.
- **Chrome must be VISIBLE (not minimised or fully covered) or the chart does not paint** and
  captures return **stale frames with no error**. Prove the renderer is live before trusting any
  image: hide a shape → canvas pixel-hash must change → restore it.
- `createMultipointShape`'s **return value is not a usable shape handle** (`getShapeById` throws);
  find shapes via `getAllShapes()`.
- Override keys are **shape-specific and silently dropped when wrong**: `rectangle` wants
  `textColor`/`fontSize`; `trend_line`/`ray` want `textcolor`/`fontsize`. **`showLabel` does not
  exist** — suppress a label with `text: ''`. Z-order **is** settable (`sendToBack`/`bringToFront`).
- `isAutoScale` was found **false**; re-enable it or the HTF view renders as vertical streaks.

### DELIVERABLES (in order)

1. STEP 0's regression, green.
2. Amended pre-registration + the **72-run** sweep including the working Aura-Asset join.
3. The sensitivity map — every cell — with `UNDERPOWERED` marked and `total_r_ex_best` shown.
4. **Then the visual review Paul asked for:** remove the `[S1d]` shapes by id, and mark up a
   representative set of entry days with the S1e hierarchy (see `markup-quality.md`) so he can
   judge **the read**, not the arithmetic. Pick days that each answer one open question — a
   100%-R17 case, an overnight-retest case, a premium-LONG, and the two big winners — rather than
   at random.
5. Per-entry reviewable records: rule log · marked chart · soft branches · outcome.
6. `accuracy.md`; tracker + `log.md` + `index.md` reconciled.

**THIS PHASE IS NOT:** advancing the replay; writing to the database or evidence layer; claiming an
edge; adopting a sweep cell because it looked good; or reporting a win rate without its R:R and its
rejection census.

### Paul's standing asks, in his words

> *"I want to review a backtest session and see what trades you take to see if you are reading the
> chart and concepts correctly."* · *"This should completely comprehensive so we both can really
> understand for this execution of this strategy. I want to become an expert in executing it and
> understanding its nuances etc"* · *"We need to exhaust all configurations then review."*

He also asked for **HTF and LTF views** as the standing markup split, and agreed strongly with it.

---

## Boot Prompt (Phase S1e — N valid entries, with WINS AND LOSSES) — ✅ SUPERSEDED 2026-08-15 (part-run; STEP 0 measurements DONE, do not redo)

**Launch:** `claude --model opus[1m]`, `/effort high`.

### Paul's ask, 2026-08-14 — in his words

> *"The review has to be a number of valid entries and then review the number of wins and losses.
> But I want to review a backtest session and see what trades you take to see if you are reading
> the chart and concepts correctly."*

**Promoted ahead of S1b at his direction.** S1d produced exactly **one** entry and it could not be
scored, so it cannot answer the question he is actually asking. This phase exists to produce a
reviewable set of entries **with resolved outcomes**.

### ⭐⭐ MEASURED 2026-08-14 BEFORE ANY EXPORT — the gate census, and it corrects the estimate

`api/scripts/aura_gate_census.py`, run over **2025-01-02 → 05-30 (107 weekdays enumerated, not
sampled)**. Counting basis declared in the script before any number: one unit = one ET weekday,
verdict = the **first** gate to reject, buckets mutually exclusive and summing to the population.

| Bucket | Days | Share |
|---|---:|---:|
| `R6` — range dead | 59 | 55.1% |
| **`REACHED-ENTRY-STAGE`** | **28** | **26.2%** |
| `R3` — no SMT-qualified daily swing | 20 | 18.7% |

**⛔ THIS CORRECTS THE "~1 SETUP PER 22 WEEKDAYS ⇒ 10–11 MONTHS" ESTIMATE, WHICH WAS WRONG.**
The HTF gates are **not** the bottleneck — **26% of weekdays clear every one of them** (R3 → R7 →
R4 → R6 → R18). Extrapolating a *setup* rate as if it were a *gate* rate was an error; the census
measures the gates directly.

**But the real constraint is worse, and it is CLUSTERING, not scarcity.** Those 28 days collapse to
**7 distinct driving episodes** (same SMT pivot + same range + same bias), from only **5 distinct
SMT pivots**:

| Bias | Driving SMT | Range | Days |
|---|---|---|---:|
| SHORT | 2024-12-11 | 20,983.75–22,111.25 | 6 |
| SHORT | 2024-12-11 | 20,694.00–22,093.50 | 11 |
| SHORT | 2025-01-31 | 20,763.75–22,078.25 | 4 |
| SHORT | 2025-02-07 | 18,976.75–20,536.75 | 2 |
| SHORT | 2025-02-07 | 16,460.00–20,044.25 | 3 |
| LONG | 2025-05-02 | 19,103.75–20,276.75 | 1 |
| SHORT | 2025-05-20 | 20,727.00–21,562.25 | 1 |

**26 of 28 are SHORT, and 17 of 28 hang off a single SMT pivot (2024-12-11).**

### ⛔ THE COUNTING-BASIS DECISION THIS FORCES — Paul's call, before any tally is computed

**Consecutive entry-stage days are not independent trades.** They are the same idea, re-entered
because the same daily SMT and the same range are still live (R7 keeps following that range until an
opposing or same-cycle SMT forms). So:

- **basis = one entry-DAY** → 28 units per 5 months ⇒ ~10 units in under 2 months. But a win rate
  over 28 correlated days is **28 samples of ~7 bets**, and would overstate the sample size by ~4×.
  This is the FU92-420 failure exactly: a counting basis that flatters the number.
- **basis = one EPISODE** (one driving SMT + range) → **7 units per 5 months** ⇒ ~10 independent
  ideas needs **~7 months** of 5m history. Honest, and expensive.

**Either way, R30's 5m iFVG step cuts further** — in S1c's window 2 entry-stage days yielded 1
setup — so entries are a fraction of the 28.

**Do not compute expectancy (R44) over correlated entry-days as if they were independent.** If the
day-level basis is chosen, the artifact must report **both** counts and say which one the ratios use.

### ⛔ THE THREE CONSTRAINTS THAT DEFINE THIS PHASE — read before planning

**1. Outcomes need forward bars, so the span must END WELL BEFORE the replay edge.**
S1d's entry was unresolvable *only* because it sat on the edge (2025-05-30 16:59 ET, confirmed at
1m). Entries earlier in history have bars after them. So the declared span must stop far enough
short of the edge that every entry in it can resolve — and any that still cannot **stay
`UNRESOLVED-AT-DATA-EDGE`**, never a breakeven.

**2. ⭐ The arithmetic of "a number of entries" is brutal, and it must be stated to Paul BEFORE
the export work.** At S1c's observed rate — **1 setup per 22 weekdays** — a tally of ~10 entries
needs roughly **10–11 months** of intraday history. STEP 0 is therefore to measure **how much 5m
history the chart will actually give up** (`setVisibleRange` forces deeper loading; S1c's
300-bar ceiling was a viewport artifact), because that bound decides whether this phase delivers
10 entries, 4, or 1. **Report the measured bound and the implied entry count before building
anything**, and let him choose the span with the real number in front of him.

**3. ⭐⭐ A win/loss tally from these gates measures THE ENGINE as much as it measures Aura.**
R6 alone rejected 13 of 21 days in S1c and 4 of 5 in S1d. If R6 is too strict, the entries in the
tally are survivors of a possibly-miscalibrated filter, and the trades it *should* have taken are
invisible. **So the stand-aside review does not disappear — it becomes the control on the tally.**
Publish both: `N entries` alongside `M stand-asides by failing rule`. A win rate without the
rejection census is a number about a filter nobody has validated.

### The counting basis — DECLARE IT BEFORE PRODUCING ANY NUMBER

Per the estate's analysis gate, and it applies with full force here:

- **One unit = one entry the engine took**, in a **contiguous declared span**, chosen and written
  down **before** any outcome is computed. Not cherry-picked, not extended after seeing results.
- **Report EVERY entry in the span.** No dropping an ugly one, no stopping early on a good run.
- **Outcome verdicts stay four-way:** `TARGET` / `STOP` / `UNRESOLVED-AT-RESOLUTION` /
  `UNRESOLVED-AT-DATA-EDGE`. Unresolved trades are reported **separately and never folded into a
  win rate** — the engine already refuses to guess in-bar sequence, and that refusal must survive
  into the summary table.
- **A win rate alone is meaningless (R44).** Publish `win%`, `avg win R`, `avg loss R` and
  `expectancy = (win% × avg win R) − (loss% × avg loss R)` together, or publish none of them.
- **State the sample size next to every ratio.** At n = 10, a single trade moves the win rate by
  10 points. Say so on the artifact rather than hoping he infers it.

### What to build

1. **Deeper export.** 5m (and 15m/60m as needed) back as far as the chart will give, all four
   symbols, into `docs/evidence/s1e/bars/` via `api/scripts/aura_bar_receiver.py` (its
   `GET /whoami` signature guard is the port-collision lesson — keep it).
2. **Run the hardened engine over the declared span.** It is already re-runnable and versioned;
   this phase should need little or no rule work. If it does, **re-prove the S1c regression** (all
   22 day-verdicts identical) before trusting anything.
3. **The tally**, per the counting basis above, with the rejection census beside it.
4. **Markup for each entry day** — bounded shapes, `[S1e]`-marked, drawn per
   [[concepts/mastery/aura/chart-markup]] **§0c** (split HTF/LTF across resolutions, snap to loaded
   bars, and **diff read-back coordinates per shape** — a matching count proves nothing).
5. **A reviewable per-entry record** so Paul can judge the *read*, not just the result: the rule
   log, the marked chart, the soft branches, and the outcome. That is the actual request —
   *"see what trades you take to see if you are reading the chart and concepts correctly."*

### ⚠️ THE TRAPS

- **Do not advance Paul's replay** (still parked 2025-05-30 20:59 UTC). Work behind the edge.
- **Do not quote expectancy as an edge.** Ten or twenty machine trades on one instrument over one
  regime is not a validated edge, and S1c/S1d found **eleven** defects that each produced
  confident-looking output. Assume a twelfth exists.
- **`QUARANTINE` holds.** Machine trades never touch `evidence_assets`, rep credit, the streak,
  calibration or the Readiness Gate.
- **Remove all `[S1d]` shapes first** (snippet in `s1d/chart-shapes-drawn.md`) and confirm zero,
  or the two phases' markup will be indistinguishable on the chart.
- **Never resolve a judgement rule** — R8 (a rulebook contradiction), R9, R31 stay UNRESOLVED or
  render as soft branches.

### ⭐ RUN THE VERIFICATION FAN-OUT HERE — this is the phase that justifies it

Paul asked about workflows on 2026-08-14 and the assessment is in the S1b prompt below. This is
where it pays: with N entries instead of 1, hand-checking every rule on every trade stops being
feasible. Build `.claude/workflows/aura-verify.js` — **one agent per rule** (R3, R6, R8, R11, R13,
R18, R21, R22, R30, R33, R35), each re-deriving that rule's verdict from `rules.md` and the raw
bars and prompted to **refute** the engine, with the engine's output withheld until it commits.
Rules are independent → `pipeline()`, no barrier. **Do not** parallelise chart interaction (one
Chrome, one session, Paul's replay state, and the chart silently clamps geometry to whatever data
is loaded — a racing sibling changes another agent's output without either erroring), and **do
not** have agents judge markup from screenshots (the whole architecture is
arithmetic-on-exported-OHLC precisely because perception cannot be audited).

### DELIVERABLES

0. **⭐ MARKUP QUALITY FIRST** — see §MARKUP QUALITY above. Get a rendered image by a route that is
   not CDP, diff the **style** properties back per shape as well as the geometry, and fix the
   hierarchy/label-density problems before drawing N entries' worth of shapes. Paul called this
   *paramount*, and drawing many more shapes before the appearance is verified would multiply an
   unverified result.
1. The measured 5m history bound and the implied entry count — **reported to Paul before the span
   is fixed.**
2. The declared span, written down before outcomes are computed.
3. `N` entries with four-way outcome verdicts, `win%` + `avg win R` + `avg loss R` + expectancy,
   **each carrying its sample size**, and the **rejection census** beside them.
4. A per-entry reviewable record: rule log · marked chart · soft branches · outcome.
5. `accuracy.md` updated; tracker + `log.md` + `index.md` reconciled; then hand back to **S1b**.

**THIS PHASE IS NOT:** advancing the replay; writing to the database or evidence layer; building
the walkthrough UI (S1b); claiming an edge; or reporting a win rate without its R:R and its
rejection census.

---

## Boot Prompt Archive (Phase S1b — the guided walkthrough, with diagrams) — ✅ RUN 2026-08-29 as an Artifact, not in the app

### ⛔ STEP 0 — WHAT S1d HANDED YOU (2026-08-14). Read before designing anything.

**FIRST ACTION: ask Paul whether he has reviewed the S1d week yet, and whether he agrees with
the four R6 stand-asides.** That review is the calibration input S1d exists to produce, and it
changes S1b's content: if he thinks R6 is too strict, the walkthrough must teach the judgement
rather than the gate. Read `neurospect-learn/api/docs/evidence/s1d/week-summary.md` **whole**
before asking, and `s1d/accuracy.md` before writing a single number into UI.

**Also confirm the 33 `[S1d]` shapes have been removed** from session `831607` — the removal
snippet is in `s1d/chart-shapes-drawn.md`. They were left deliberately for review; they must be
gone before Paul marks that week by hand.

**Three things S1d changed that S1b's design must absorb:**

1. **D0's soft/hard split has MORE material now.** The engine's `HARD_GATES` / `SOFT_BRANCHES`
   lists are still the tree's spine, but S1d added: weekly is **reported, not a gate**; R8 is a
   **rulebook contradiction** (rule 8's two sentences cannot both be satisfied by one swing);
   R22 can degenerate to the same price as R35; and the entry window can **hide an earlier
   retest**. Every one of those is a place the tree will want to draw a clean branch and must
   not. Take the lists from code — do not re-decide them.
2. **⛔ There is NO realised outcome to display, for any trade.** The one entry in the declared
   week is `UNRESOLVED-AT-DATA-EDGE` (1.20R in favour, 0.41R against, then the bars stop). If
   S1b renders an outcome, R or win/loss anywhere, it must render **that verdict**, not a blank
   and not a breakeven. `n = 1` still holds, and the week was **selected**.
3. **The real worked example now exists and is machine-generated.** If S1b shows it, it renders
   permanently and visibly marked as such. Do not fabricate price data — see §THE DIAGRAM RULE.

### ⭐ The workflow idea (Paul, 2026-08-14) — scoped, with the parts that would backfire

Paul asked whether multi-agent orchestration could speed this up and be specialised for
chart/markup work. Assessment, so it is not re-litigated from scratch:

**Worth building — an `aura-verify` workflow (verification, not building).** Every defect across
S1c and S1d was found by re-deriving a number by a *different route*: 11 defects in two phases,
all of which produced confident-looking output. That is a fan-out: **one agent per rule** (R3,
R6, R8, R11, R13, R18, R21, R22, R30, R33, R35), each re-deriving that rule's verdict from
`rules.md` and the raw bars and prompted to **refute** the engine, with the engine's own output
withheld until it has committed. Rules are independent, so `pipeline()` with no barrier. Same
shape works per-day when the span grows past one week — which is the point at which this stops
being optional.

**Would backfire, and why:**
- **Chart interaction must stay single-threaded.** One Chrome, one Tradezella session, holding
  Paul's real replay state. Parallel agents setting resolution / visible range / shapes would
  race — and S1d proved the chart silently clamps geometry to whatever data happens to be
  loaded, so a racing sibling changes another agent's *output* without either erroring.
- **Markup quality did not come from compute.** It came from reading emitted coordinates and
  noticing they ran backwards. A fleet would have drawn 15 nonsense rectangles faster and
  produced a confident screenshot of them.
- **Vision-based chart reading is a trap for this project specifically.** The whole S1c/S1d
  design is arithmetic-on-exported-OHLC *because* perception cannot be audited. Agents judging
  markup from screenshots would reintroduce exactly the unfalsifiable reads the architecture
  exists to prevent. Images have one legitimate job: proving shapes painted.
- **Agent fleets converge on answers**, and R8/R9/R31 must stay UNRESOLVED. Adversarial
  *verification* is safe; adversarial *resolution* would teach Paul that Aura is deterministic.

Build it as `.claude/workflows/aura-verify.js` and invoke it from a boot prompt — not as a
build-the-app workflow.

### 📝 Skill gap to close (offer at session end, don't do it mid-work)

`~/.claude/skills/web-automation/claude-in-chrome-driving.md` should gain S1d's §7b lesson:
**enumeration by count proves nothing** — the chart silently clamps shape coordinates to the
loaded data window, and only a per-shape requested-vs-read-back comparison catches it. Also that
the chart iframe's id **changes between page loads**, so a hardcoded id silently matches nothing.

---


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

#### ⭐ PAUL'S FEEDBACK ON THE MARKUP (2026-08-13) — this is S1b's problem, not S1c's

S1c drew its computed levels as **infinite horizontal lines**, and Paul rejected the markup
quality outright: *"you drew horizontal lines across the whole chart, not just in the area
where the FVG was… if we are getting you to run a backtest session and mark up levels and PD
Arrays for trades the marking up has to be more refined and clear."*

**He is right, and the reason is structural.** An infinite line asserts *"this level applies at
all times"* — which contradicts **R6** (a range dies at a close beyond it) and **R7** (follow the
current range only until the next Sequential SMT). The primitive was making a claim the rules
explicitly deny. Now written up canonically as
[[concepts/mastery/aura/chart-markup]] **§0b — Markup primitives**, with a
what-to-draw-with table: **rectangles** for PD arrays bounded formation→mitigation, **rays**
for live levels from their anchor, **bounded segments** for levels that have already ended,
and range boundaries **terminated at the invalidating close**.

**M1–M12 in the walkthrough must teach the primitive alongside the level.** "Box every FVG" is
not enough guidance to produce a re-readable chart; *"box it from the bar that formed it to the
bar that mitigated it"* is. This is the difference between a chart Paul can read back in a week
and a wall of lines — and it is exactly the kind of thing a walkthrough exists to make automatic.

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

### ⏳ DESIGN DECIDED 2026-08-13 (Paul), NOT YET BUILT: **LIVE**, with the full map one tap away

> ⚠️ **This heading previously read `✅ DECIDED`, and Paul went looking for the decision tree in the
> running app because of it** (2026-08-14). Nothing is built: `app/src/App.tsx` registers 18 routes
> and none is a decision tree; there is no `DecisionTree` / `branchAnswer` / "full map" identifier
> anywhere in `app/src`. A green tick means **the design question is settled**, never that the code
> exists. Keep the distinction visible in this tracker.

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
