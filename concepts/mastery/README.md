---
tags: [mastery, learning, execution, neurospect, index]
aliases: [Mastery Layer, Learning System, Mastery Hub, Path to Live Trading]
created: 2026-07-17
updated: 2026-07-17
---

# Mastery Layer — Hub

This namespace is the **learn-to-execute** layer of the wiki. The rest of the wiki tells you *what*
each concept is (`concepts/business-logic/ict-*`, `concepts/aura/*`, `concepts/course/*`) and gives the
per-strategy execution specs (`concepts/entry-models/*`). This layer answers a different question:

> **How do I take a model from "I understand it" to "I can execute it live with confidence" — and how do
> I know, on evidence, when I'm actually ready?**

It is built for one user (Paul) working toward live-trading the models. The arc it supports:

```
Learn the concepts → mark them by hand (train the eye) → backtest in replay → read live tape
   → keep an annotated-screenshot journal → prove positive expectancy → go live
```

## The two tracks (+ a deferred third)

Each track is self-contained: a canonical rule set, an execution checklist, a learning path, an exercise
library, and a living mastery tracker.

| Track | Model | Status |
|---|---|---|
| [[concepts/mastery/aura/rules\|Aura (dOoMeR)]] | Sequential-SMT model — psychology-first; ranges + triads + Sequential SMT + Aura Asset; Dante risk | **Built (Phase 1)** |
| [[concepts/mastery/ict-course/rules\|ICT-course (MrWitness-AXL)]] | four-stage price delivery; consolidation / E&R / reversal / London / Model 2022 OTE / daily-bias / SMT; AXL discipline | **Built (Phase 2)** |
| [[concepts/mastery/unified/README\|Unified model]] | a single reconciled 5-layer playbook merging both, with per-divergence rulings | **Built (Phase 3, 2026-07-17)** |

> **Unified model — built.** The [[concepts/mastery/unified/README|Unified Playbook]] reconciles the two
> tracks into one principled sequence (psychology → structural primitives → nested-SMT confirmation →
> execution → risk); every AXL↔Aura divergence has a cited ruling in
> [[concepts/mastery/unified/divergence-rulings]]. Frontier ICT content that extends its execution/confirmation
> layers lives in [[concepts/advanced/README]]. *(The original "merge only after backtesting" precondition was
> dropped in the 2026-07-17 PM tracker amendment — this layer is course content, not a live-trading deliverable.)*

## How this layer relates to the rest of the wiki (no-drift rule)

Per [[CLAUDE]] §"Architecture Doc Integrity" / *canonical doc per topic*: mastery pages **link to** the
concept pages as source-of-truth and **must not restate** concept content. The division of altitude:

- **Concept / KB pages** are canonical for *what a thing is and why* (rationale, mechanics, worked theory).
- **Entry-model pages** (`concepts/entry-models/*` YAML) are canonical for *per-strategy execution specs*
  (and are consumed by the AI coach — never fork them).
- **Mastery pages** are canonical for *the imperative "how to drill it and execute it," and progress*.

Every rule and drill here cites its source (`aura-NN`, a course lesson, or an entry-model page). If a
concept page and a mastery rule ever disagree, the concept page wins and the mastery page is corrected.

## The mastery model (shared by every track)

### Per-concept mastery ladder (4 stages)

Each concept in a track is tracked up this ladder. A concept is not "done" until it reaches the stage the
track's readiness gate requires (normally **Backtested** minimum, **Live-ready** for the core few).

| Stage | Name | Bar to clear it |
|---|---|---|
| 1 | **Learned** | Can explain the concept unprompted, in your own words, incl. its failure mode. |
| 2 | **Can mark** | Can correctly identify it on unlabelled charts **by hand** — the eye-training stage. |
| 3 | **Backtested** | Applied across the drill's rep target in bar-replay, with outcomes logged in R. |
| 4 | **Live-ready** | Executed on live/sim tape using the checklist, and journaled. |

**Hand-marking first, tools second.** Tooling (the Sequential-SMT indicator, auto-plotted ranges) is
available and used at the Backtested/Live stages — but Stage 2 is deliberately done *by hand* so the eye
learns to see the structure without the indicator. Most drills in each track's `exercises.md` have both a
hand-marking and a tool-assisted variant for this reason.

### Confidence rating (1–5)

Alongside the ladder, self-rate confidence per concept. This is subjective but honest — it surfaces the
gap between "I marked it 50 times" and "I trust it live."

`1` no feel · `2` shaky · `3` usually right · `4` reliable · `5` automatic (see it without thinking)

### Rep counters

Marking/backtest drills carry a rep target (e.g. swing points 50/50). The tracker logs progress against
it. Reps are a *floor*, not the finish line — the ladder stage is what actually gates readiness.

## The Readiness-to-Live Gate

This is the concrete, **evidence-based** answer to "am I good enough to live-trade this model yet?" — in
the same spirit as Paul's global rule of never shipping on inference. Do **not** move from sim to live
capital until every box below is genuinely checked (each track's `tracker.md` holds the live copy):

- [ ] **Every core concept at Backtested+**, and the model's few load-bearing concepts at Live-ready.
- [ ] **A minimum backtest sample** (target: ≥50 setups per the drill reps, ideally ≥100 executed
  backtest trades) with a **positive expectancy in R** — computed with the risk-management formula
  `Expectancy = (win% × avg win R) − (loss% × avg loss R)` (see [[concepts/aura/risk-management]]).
- [ ] **Win rate is known *with its R:R*** and clears break-even for that R:R (break-even win rate
  `= 1 / (1 + R:R)`) — a win rate without its R:R is meaningless.
- [ ] **Risk rules internalized and precommitted, in writing**: per-trade 1–2% of total capital, daily
  stop 2–3R, 10R drawdown circuit-breaker, no sizing up in a drawdown (see [[concepts/aura/risk-management]]).
- [ ] **A demo/sim track record** long enough to show the discipline holds under live conditions, not just
  in hindsight replay.
- [ ] **An established journaling habit** — every trade (incl. missed/canceled) logged, weekly review run,
  "never miss twice" holding (see [[concepts/aura/journaling-system]]).
- [ ] **Circuit-breaker discipline demonstrated** — you have actually stopped at your daily stop / two-loss
  rule under real pressure, not just written it down.

Live trading starts **small** even after the gate clears; the gate certifies readiness to begin, not to
size up.

## See Also

- **Aura track:** [[concepts/mastery/aura/rules]] · [[concepts/mastery/aura/checklist]] · [[concepts/mastery/aura/learning-path]] · [[concepts/mastery/aura/exercises]] · [[concepts/mastery/aura/tracker]]
- **ICT-course track:** [[concepts/mastery/ict-course/rules]] · [[concepts/mastery/ict-course/exercises]] · [[concepts/mastery/ict-course/tracker]] *(learning-path + checklist reuse [[concepts/course/README]] and the entry-model YAML — not duplicated here)*
- **Unified track:** [[concepts/mastery/unified/README]] (the playbook) · [[concepts/mastery/unified/divergence-rulings]] (the reconciliation) · [[concepts/advanced/README]] (frontier ICT that extends it)
- [[concepts/aura/README]] — the Aura concept KB this track builds on
- [[concepts/course/README]] — the ICT-course learning path (Track 2 will build on it)
- [[concepts/entry-models/README]] — per-strategy execution checklists (canonical; the ICT track links here)
- [[concepts/architecture/trade-schema]] — the journal data model the tracking/journaling drills map onto
- [[entities/projects/neurospect]] — full project context
