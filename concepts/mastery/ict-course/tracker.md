---
tags: [mastery, ict-course, tracker, progress, neurospect]
aliases: [ICT Mastery Tracker, MrWitness-AXL Progress Tracker, ICT Readiness Tracker]
sources: [concepts/mastery/README.md, concepts/mastery/ict-course/rules.md, concepts/mastery/ict-course/exercises.md, concepts/course/README.md, concepts/entry-models/README.md]
created: 2026-07-17
updated: 2026-07-17
---

# ICT Course (MrWitness-AXL) Mastery Tracker

**This is a living page — Paul edits it as he progresses.** It is the single place that answers "where am
I, and am I ready to go live?" for the ICT track. Scales are defined in [[concepts/mastery/README]]:

- **Ladder:** `1 Learned` → `2 Can-mark` → `3 Backtested` → `4 Live-ready`
- **Confidence:** `1` no feel · `2` shaky · `3` usually right · `4` reliable · `5` automatic
- Fill the ladder cell with the current stage number; tick reps as you go; date the last practice.

> All cells start blank/`0` — nothing is claimed until it's true (the tracker is evidence, not aspiration).

## Concept mastery — the 16 lessons

| # | Lesson concept | Module | Drill | Reps | Target | Ladder (1–4) | Conf (1–5) | Last | Notes |
|---|---|---|---|---|---|---|---|---|---|
| L1.1 | Liquidity & inefficiency (BSL/SSL, DOL) | M1 | D1-a | 0 | ≥5 | | | | **core** |
| L1.2 | Fair value gaps (FVG/IOFED/inversion) | M1 | D1-b | 0 | ≥20 | | | | **core** |
| L2.1 | Four stages of APD | M2 | D2-a | 0 | 5 sessions | | | | **core** |
| L2.2 | Consolidation model | M2 | D2-b | 0 | Class-2 hw | | | | |
| L2.3 | Expansion & Retracement | M2 | D2-c | 0 | ≥10 | | | | |
| L2.4 | Reversals (3 types) | M2 | D2-d | 0 | ≥10 | | | | |
| L3.1 | Power of Three (AMD) | M3 | D3-a | 0 | 10 days | | | | **core** |
| L3.2 | Session kill zones | M3 | D3-b | 0 | 1 week | | | | **core** |
| L3.3 | Deviations (Fib targeting) | M3 | D3-c | 0 | 10 days | | | | |
| L3.4 | Daily bias | M3 | D3-d | 0 | 10 days | | | | **core** |
| L4.1 | Swing classification (STH/ITH/LTH) | M4 | D4-a | 0 | 5 days | | | | **core** |
| L4.2 | Market structure fractality | M4 | D4-b | 0 | 5 days | | | | |
| L4.3 | Structure deviations (two-set) | M4 | D4-c | 0 | ≥10 | | | | |
| L4.4 | Model 2022 + OTE + CSD | M4 | D4-d | 0 | ≥10 | | | | |
| L5.1 | HTF/LTF order flow | M5 | D5-a | 0 | 1 week | | | | **core** |
| L5.2 | SMT divergence | M5 | D5-b | 0 | 5 days | | | | **core** |

*Core load-bearing concepts (must reach **Live-ready** for the gate): liquidity/inefficiency, FVG, four
stages, Power of Three, kill zones, daily bias, swing classification, order flow, SMT. Others need
**Backtested** minimum.*

## Entry-model mastery — the 7 strategies

Checklists are canonical in the entry-model YAML (consumed by the AI coach — follow them there, do not
copy). Track backtest progress per model here.

| Model | Page | Drill | Setups logged | Ladder (1–4) | Conf (1–5) | Last | Notes |
|---|---|---|---|---|---|---|---|
| Consolidation | [[concepts/entry-models/consolidation-model]] | D2-b + S7 | 0 | | | | |
| Expansion & Retracement | [[concepts/entry-models/expansion-retracement-model]] | D2-c + S7 | 0 | | | | |
| Reversal — Raid on Stops | [[concepts/entry-models/reversal-raid-on-stops]] | D2-d + S7 | 0 | | | | |
| London Model | [[concepts/entry-models/london-model]] | S7 | 0 | | | | |
| Model 2022 + OTE | [[concepts/entry-models/model-2022-ote]] | D4-d + S7 | 0 | | | | |
| Daily Bias (filter) | [[concepts/entry-models/daily-bias-model]] | D3-d | 0 | | | | bias filter, not an entry/exit model |
| SMT Confirmation | [[concepts/entry-models/smt-confirmation-entry]] | D5-b + S7 | 0 | | | | |

## Module readiness gates (reuse the `## Readiness Check` primitive)

Each module clears when its drills reach Can-mark, ≥ target reps, conf ≥3, by hand. The Module-1 gate is
the built-in checkbox block in [[concepts/course/module-1-foundations/03-homework-and-practice]] — reused
here; add the analogous per-module boxes as you build them.

| Module | Clears when | Status |
|---|---|---|
| M1 Foundations | Readiness Check (7 boxes) passed; D1-a/b at Can-mark | ☐ |
| M2 Price delivery | D2-a…d at Can-mark; real vs. fake retracement automatic | ☐ |
| M3 Session & bias | D3-a…d at Can-mark; bias written pre-session 10 days | ☐ |
| M4 Market structure | D4-a…d at Can-mark; STL→ITL→MSS fractal automatic | ☐ |
| M5 Order flow & SMT | D5-a/b at Can-mark; cracking correlation spotted live | ☐ |
| Tape reading | ≥8 of the 13 studies done + ≥1 blind live-read graded | ☐ |

## Backtest sample (Stage 7 — the expectancy evidence)

Update as the sample grows. Formulas: break-even win rate `= 1/(1+R:R)`; expectancy
`= (win% × avg win R) − (loss% × avg loss R)`.

| Metric | Value | Target |
|---|---|---|
| Setups logged | 0 | ≥50 |
| Executed backtest trades | 0 | ≥100 |
| Win rate | — | (known *with* its R:R) |
| Avg R:R | — | — |
| Break-even win rate for that R:R | — | win rate must exceed this |
| Avg win (R) / Avg loss (R) | — / — | — |
| **Expectancy (R/trade)** | — | **> 0** |
| Max drawdown observed (R) | — | < daily-loss-limit discipline holds |

Link the backtest log (spreadsheet / Neurospect journal export) here: _______________________

## Readiness-to-Live Gate

Copied from [[concepts/mastery/README]], with the ICT track's risk-rule specifics (AXL daily loss limit)
substituted. **Do not move to live capital until every box is honestly checked.** Even then, **start
small** — the gate certifies readiness to begin, not to size up.

- [ ] Every core concept at **Backtested+**; the load-bearing few at **Live-ready**.
- [ ] Backtest sample met (≥50 setups / ≥100 trades) with **positive expectancy in R**.
- [ ] Win rate known **with its R:R** and clearing break-even for that R:R.
- [ ] Risk rules precommitted **in writing**: **AXL daily loss limit** ($1,000 if ≥$10K account, else
  $500 → log out), **set-and-forget** (close only at BE / partials / TP), **no chasing expansions**.
- [ ] Demo/sim track record long enough to show discipline holds live (not just in hindsight).
- [ ] Journaling habit established — every trade incl. missed/canceled; weekly review; set-and-forget audit.
- [ ] **Bad-conditions / stand-aside discipline demonstrated** under real pressure (actually sat out a
  choppy / pre-NFP / "not conditions" day, and honoured the daily loss limit at least once).

**Gate status:** ☐ NOT READY  ·  ☐ READY (date: __________)

## Progress log

*(append dated one-liners — what you drilled, reps added, stage cleared)*

- 2026-07-17 — tracker created; all concepts + models at baseline. Start at Stage 0 (discipline/journal)
  and Module 1.

## See Also

- [[concepts/mastery/ict-course/exercises]] · [[concepts/mastery/ict-course/rules]]
- [[concepts/mastery/README]] — scales + gate definitions
- [[concepts/course/README]] — the module curriculum (learning path for this track)
- [[concepts/entry-models/README]] — canonical per-strategy checklists
- [[concepts/mastery/aura/tracker]] — the parallel Aura tracker (format mirrored here)
