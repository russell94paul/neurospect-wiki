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

> **Source caveat (updated 2026-07-18 Tier-1 pass):** the CBDR window, the body-vs-wick measurement, the
> pip-size filter, the flout window, and now the **Asian-range hours (20:00–00:00 ET)** are all **Tier-1** —
> sourced to verbatim transcript of ICT's own 2016 Premium Mentorship Core Content (Month 8 #74 "Defining The
> Daily Range" / #75 "Central Bank Dealers Range" / Month 9 #82 "Filling The Numbers"). Remaining items (SD
> multiple *sets*, index-futures calibration) stay **corroborated Tier 2 / EMERGING** as marked. Transcripts
> hosted on a third-party archive (quagmyre.com) of ICT's own recorded audio — lecture titles/numbers
> corroborated against the quagmyre XWiki lecture index; cited with the archive URLs + the YouTube video IDs
> as a hedge.

## CBDR (Central Bank Dealers Range) — **ESTABLISHED (Tier 1)**

- **Definition:** the high/low of price during **14:00–20:00 ET** (2pm–8pm, a 6-hr window). *Verbatim (ICT):
  "The time period that frames the central bank dealers range is 2pm to 8pm New York time."*
- **Validity filter (not just a measurement):** ideal size **< 40 pips-equivalent**, preferably 20–30. An
  oversized CBDR **invalidates** the day's projection — the model has a built-in no-go. *Verbatim (ICT):
  "The ideal range is less than 40 pips, preferably the range should be no more than 20 to 30 pips in total
  range."* **Rationale (his own):** the daily candle's average daily range is "typically around 100 pips,"
  and ⅓ of that ≈ 33 pips — which is why 20–30 is the target and 40 the ceiling.
- **Measurement — RESOLVED (Tier-1): use candle BODIES.** *Verbatim (ICT): "I like to use the bodies
  predominantly because the wicks are always going to show erroneous price because of your dealing spread
  through your broker."* The prior "one AI summary says wicks" reading is contradicted by this direct primary
  quote and should be treated as an outlier — measure the CBDR on bodies.

> **Tier-1 citation:** ICT, 2016 Premium Mentorship Core Content, **Month 8 — "Central Bank Dealers Range"
> (Lecture 75)**, verbatim transcript — <https://files.quagmyre.com/files/ICTStudies/ICT-2016-Premium-Mentorship-Core-Content/srt/75-ICT%20Mentorship%20Core%20Content%20-%20Month%208%20-%20Central%20Bank%20Dealers%20Range.srt>
> (third-party archive of ICT's own audio; YouTube video ID `nI1AMOC1pro`). Re-verified independently this session.

## Asian Range & "Flout" — **flout ESTABLISHED (Tier 1); Asian-range hours RESOLVED (Tier 1)**

- **Asian range: 20:00–00:00 ET (8pm–midnight, 4 hr) — Tier 1 (verbatim).** Ideal 20–30 pips-equiv; used as a
  manipulation/liquidity reference (London/NY expected to sweep one side before reversing).
  > **✅ Contradiction RESOLVED (2026-07-18 Tier-1 pass).** The window is **20:00–00:00 ET**, not the
  > 19:00–00:00 (7pm start) this page previously carried. Settled from ICT's own definitional statement in
  > **Month 8, Lecture #74 "Defining The Daily Range"**: *"…at 8pm eastern standard time in New York time.
  > This begins the Asian range. Every day at midnight Eastern Standard Time New York ends the Asian range."*
  > This is fully consistent with the Month-8 CBDR lecture's applied fragment (*"At 8pm, starting the Asian
  > range, project that range that we created for central bank dealers range"*): the CBDR closes at 8pm and
  > 8pm is also the Asian-range start, running to midnight ET. The old 7pm-start reading is dropped.
  > *Provenance caveat: transcript + corroborating lecture index both hosted on the quagmyre archive (same
  > archivist, different subsystems) → Tier-1-with-single-archive-corroboration.*
  > **Tier-1 citation:** ICT, 2016 Premium Mentorship Core Content, Month 8 #74 "Defining The Daily Range",
  > verbatim transcript — <https://files.quagmyre.com/files/ICTStudies/ICT-2016-Premium-Mentorship-Core-Content/srt/74-ICT%20Mentorship%20Core%20Content%20-%20Month%208%20-%20Defining%20The%20Daily%20Range.srt>
- **Flout — Tier 1.** A **genuine ICT-derived term** (adversarially checked — real, not a mishearing). The
  combined CBDR+Asian window, used as a **fallback range** when neither CBDR nor Asian range individually
  passes its size filter. *Verbatim (ICT): "the range from 3pm to midnight, New York time"* → exactly
  **15:00–24:00 ET** (tightened from the prior "~"). Its equilibrium-to-high and equilibrium-to-low are each
  counted as 1 standard deviation for projection. From ICT's **Mentorship "Month 9 — Filling The Numbers"
  (Lecture 82)**; absent from ICT's general glossary → a PA-Model-specific term, not core vocabulary.
  > **Tier-1 citation:** ICT, 2016 Premium Mentorship Core Content, Month 9 "Filling The Numbers" (Lecture
  > 82), verbatim transcript — <https://files.quagmyre.com/files/ICTStudies/ICT-2016-Premium-Mentorship-Core-Content/srt/82-ICT%20Mentorship%20Core%20Content%20-%20Month%209%20-%20Filling%20The%20Numbers.srt>
  > (third-party archive of ICT's own audio; YouTube video ID `zanmou0ic5U`). *Flout window re-verified via
  > the subagent's dual-path fetch; not independently re-fetched by the main session this pass.*

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
