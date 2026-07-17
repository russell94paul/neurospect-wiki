---
tags: [concept, advanced, frontier, neurospect, ict, cbdr, deviations]
aliases: [CBDR, Central Bank Dealers Range, Asian Range, Flout, Standard Deviation Projections]
created: 2026-07-17
updated: 2026-07-17
---

# CBDR, Asian Range, Flout & Standard-Deviation Projections

A **WHERE** layer that bounds *realistic target zones* by projecting a low-liquidity reference range forward.
It complements (does not restate) the canonical Fibonacci-deviation page
[[concepts/business-logic/ict-deviations]] — and the most important thing on this page is that **ICT's
"standard deviation" is arithmetic range-multiplication, not statistical std-dev, and not Fibonacci** (see
the disambiguation below).

> **Source caveat:** no Tier-1 verbatim source was captured; everything here is **corroborated Tier 2**
> unless marked. Confidence labels reflect that.

## CBDR (Central Bank Dealers Range) — **ESTABLISHED (Tier 2)**

- **Definition:** the high/low of price during **14:00–20:00 ET** (2pm–8pm, a 6-hr window).
- **Validity filter (not just a measurement):** ideal size **< 40 pips-equivalent**, preferably 20–30. An
  oversized CBDR **invalidates** the day's projection — the model has a built-in no-go.
- **Measurement — UNRESOLVED (flagged, not smoothed):** most Tier-2 sources say ICT prefers candle **bodies**
  ("wicks vary by broker"); one AI summary of an actual ICT video says **wicks** (for cross-broker
  consistency). Present both; do not silently pick one.

## Asian Range & "Flout" — **ESTABLISHED (Tier 2)**

- **Asian range:** high/low during **19:00–00:00 ET** (7pm–midnight), ideal 20–30 pips-equiv; used as a
  manipulation/liquidity reference (London/NY expected to sweep one side before reversing).
- **Flout:** a **genuine ICT-derived term** (adversarially checked — real, not a mishearing). It is the
  combined CBDR+Asian window (~15:00–24:00 ET), used as a **fallback range** when neither CBDR nor Asian range
  individually passes its size filter. Traced to ICT's **PA Model 5 / Mentorship "Month 9 — Filling The
  Numbers"** ("Michael recommends using central pivot, CBDR, Asian range, and flout altogether"), corroborated
  across multiple independent sources + dedicated TradingView indicators. Absent from ICT's general glossary →
  a PA-Model-5-specific term, not core vocabulary. Cite as ICT-derived, Tier 2.

## Standard-Deviation Projections — **ESTABLISHED method / EMERGING canonical multiples**

- **What it is:** `Target = Range_High/Low ± (multiplier × Range_Width)`. This is **ICT's own name for an
  arithmetic range-multiple projection — NOT a statistical (mean/variance) standard deviation.** No source
  produced an actual std-dev formula; all describe simple linear range extension.
- **Multiple sets vary by model version (genuinely, not a doc error):**
  - **CBDR / Judas-Swing framing:** 1×–3×, where 2×–3× is the Judas Swing's outer limit; beyond 3× the profile
    is considered invalidated.
  - **PA-Model / manipulation-leg framing:** {1, 0, −1, −2, −2.5, −4}, with **−2/−2.5 the common reaction zone**
    and **−4 the outer expansion target.**
  - Widest attested union: **{1, 2, 2.5, 3, 4}**, 2–2.5 = reaction/pause zone, 3–4 = outer/max target.
- **Applies to:** CBDR (primary), Asian range, flout, and the PO3 manipulation leg. No ICT-attributed source
  applies it to a generic "opening range."
- **Edge:** an ATR-style bounded-target heuristic anchored to a real low-liquidity window — useful as a
  **risk/target overlay, not a proven predictive trigger.** No source demonstrates a backtested edge.
- **Failure mode:** treating exactly 2.5× as a precise reversal point rather than a zone; ignoring the
  CBDR < 40-pip invalidation rule; **conflating with Fibonacci math** (below).

## ⚠ Disambiguation: SD projection ≠ Fibonacci ≠ statistical std-dev

A real, documented conflation to keep straight (several Tier-3 sources get this wrong):

| Term | What it actually is |
|---|---|
| **SD projection** (this page) | Arithmetic range-multiple: range width × {1,2,2.5,3,4} |
| **Fibonacci / OTE** ([[concepts/business-logic/ict-deviations]]) | Ratio-based swing retracement/extension (0.618/1.618, OTE 62–79%) |
| **Statistical std-dev** | Volatility of recent candle ranges (ICT's "2022 Mentorship" indicator uses it to validate displacement — a *third* meaning) |

They are **coincidentally drawn with the same TradingView Fib tool** (custom labels 1/0/−1/−2/−2.5/−4 override
the native ratios) — a UI convenience, unrelated math. Keep SD-projection and Fibonacci-deviation as separate
concepts on the wiki.

## ⚠ Open gap: index-futures calibration

**Every pip-based size filter (CBDR < 40, Asian 20–30) is forex-calibrated.** No source translates these to
NQ/ES/YM **points**. Do **not** assume a 1:1 pip-to-point transfer. Deriving an index-calibrated quality
filter (CBDR/Asian sizes in points on NQ/ES) is a flagged **future-backtest** item, not settled here.

## New confluences surfaced

- **SD × liquidity pool** *(community-synthesis, logically strong):* an SD level (especially the −2/−2.5
  reaction zone) that **also coincides with a prior day/week/session old high-or-low** should be weighted far
  higher than a bare SD number — two independent frameworks agreeing is the signal.
- **Judas "double duty":** the manipulation leg ideally sweeps the CBDR/Asian extreme **and** a nearby resting
  external liquidity pool in the same move — two independent reasons for the reversal.
- **Arrival-session check:** if the SD/DOL target would require price to travel there **outside** any killzone
  (e.g. NY-lunch dead zone), it is lower-conviction — ties to [[concepts/advanced/quarterly-theory]] and
  [[concepts/advanced/ict-macros-and-silver-bullet]].
- The **SD-validity-within-IRL/ERL-cycle** idea (SPECULATIVE) is documented on [[concepts/advanced/ipda-data-ranges]].

## How it interacts with the Unified Playbook

The **WHERE** filter that projects *toward* IPDA/ERL targets: CBDR/Asian-range SD levels give bounded target
zones for [[concepts/mastery/unified/README]] Layer 3, strongest when an SD level coincides with an IPDA
liquidity pool and the Layer-2 SMT stack confirms at the sweep.

## See Also

- [[concepts/business-logic/ict-deviations]] — canonical Fibonacci deviation targeting (distinct from SD — see disambiguation)
- [[concepts/advanced/ipda-data-ranges]] — the ranked liquidity targets SD projects toward
- [[concepts/advanced/README]] — frontier hub + confluence stack + the unfalsifiability critique
- [[concepts/mastery/unified/README]] — Layer 3 execution
