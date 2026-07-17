---
tags: [concept, advanced, frontier, neurospect, ict, liquidity, ipda]
aliases: [IPDA Data Ranges, IPDA, Liquidity Matrix, IRL ERL, PD Array Matrix]
created: 2026-07-17
updated: 2026-07-17
---

# IPDA Data Ranges & the Liquidity Target Stack

The **WHERE** layer of the frontier stack: a non-discretionary way to *rank* draw-on-liquidity targets by
algorithmic "reach." Extends — does not restate — the canonical liquidity page
[[concepts/business-logic/ict-liquidity]] (BSL/SSL/DOL), adding a lookback-range method that page lacks.

## IPDA 20/40/60-day data ranges — **ESTABLISHED (Tier 2, unanimous)**

IPDA (Interbank Price Delivery Algorithm) is ICT's *conceptual* model for how the interbank market delivers
price — **not a literal disclosed algorithm.** Its most-corroborated mechanic (the single most
cross-source-consistent figure in the whole Phase-3 pass):

- **Three nested daily-chart lookback windows: 20, 40, 60 days.** From the first trading day of the month
  (or a confirmed daily structure shift), count back 20/40/60 days; each window's highest-high / lowest-low
  forms a nested range.
- **Two purposes:** (a) locate resting **BSL/SSL** above/below those old highs/lows (the draw on liquidity);
  (b) locate **imbalances/FVGs** due to rebalance.
- **Ranking (the actual edge):** 20-day = nearest / most-probable objective; 40-day = escalation if the
  20-day doesn't halt the move; 60-day = outer / rare objective. New pools reportedly re-form ~every 20 days.
- **Attribution:** ICT 2022 Mentorship Core Content (Months 5, 7, 8). Videos not transcript-fetchable → rests
  on two independent Tier-2 note sets (ICT Sharks forum + innercircletrader.net) that agree closely.

**Failure mode:** marking all three ranges then retroactively declaring whichever "worked" as the target
(unfalsifiable unless fixed in the plan first). **Trading-days vs. calendar-days is ambiguous** — 60 trading
days ≈ 12 weeks vs. 60 calendar days ≈ 8.5 weeks; pick one, hold it constant. *(This distinction, and a
20→40→60 "redirect cascade" rule, are single-sourced Tier-3 — **UNVERIFIED**; don't treat as settled.)*

Citations: <https://forum.ictsharks.com/t/ict-mentorship-core-content-month-5-using-ipda-data-ranges/69> ·
<https://innercircletrader.net/tutorials/ict-ipda/> · <https://www.tradingview.com/script/rTJEJb5v-ICT-IPDA-Look-Back/>.

## "Liquidity Matrix" — **SPECULATIVE-or-FRINGE as an ICT term**

Adversarially checked because it was on the research shortlist. Verdict: **not a stable ICT-originated
concept.** It is (a) a loose descriptor and (b) a **vendor brand name** — ≥3 unrelated commercial indicators
are named "Liquidity Matrix," each defined differently, none attributing the term to ICT. Detailed community
notes on the exact episodes cited as its "origin" **do not use the phrase** (direct negative evidence).

- **The real ancestor is ICT's "PD Array Matrix"** — a genuine, mechanically-specific ranked hierarchy of
  FVGs / order blocks / breaker blocks / mitigation blocks used to prioritize *which* array to trade.
- **Ruling for this wiki:** do not build a "liquidity matrix" concept. Where the idea is wanted (liquidity is
  layered across timeframes), use ICT's real vocabulary — liquidity pool, BSL/SSL, DOL, **PD Array Matrix**.

Citations: <https://ictflow.com/blog/ict-pd-array-matrix-explained> (the real term) ·
<https://forum.ictsharks.com/t/2023-ict-mentorship-one-trading-setup-for-life/371> (phrase absent from source notes).

## IRL / ERL — **ESTABLISHED (Tier 2)**

Genuine, well-sourced ICT vocabulary that *is* the defensible version of a "liquidity stack":

- **ERL (External Range Liquidity):** liquidity *outside* the current dealing range — old highs/lows, the DOL magnet.
- **IRL (Internal Range Liquidity):** liquidity *inside* the range — unmitigated FVGs, minor swings.
- Price cycles **external → internal → external**. This composes cleanly with IPDA (the 20/40/60 highs/lows
  are the ERL targets) and with premium/discount ([[concepts/aura/ranges]]).

## Multi-timeframe liquidity cascade & LRLR/HRLR — **EMERGING / community shorthand**

- **"Weekly → daily → session → intraday" cascade** is a *reasonable extrapolation* from genuine ICT blocks
  (multi-TF bias; larger-TF levels carry more weight because resting orders are larger) — but **no source
  documents ICT stating it as one named sequence. Label: EMERGING / community-synthesis**, not verbatim ICT.
- **LRLR vs HRLR** (Low/High Resistance Liquidity Run): widely circulated, consistently defined (LRLR = clean
  fast run, minimal opposing structure; HRLR = grinding run through order blocks/PD arrays) — but at least one
  dedicated source (ictflow.com) **explicitly disclaims any direct ICT citation**. **Label: SPECULATIVE** as
  ICT-coined; treat as community shorthand for a real underlying idea (resistance quality of a run).
- **Failure mode:** weighting every old high/low equally regardless of timeframe; relabeling a "failed" LRLR
  as HRLR after the fact (unfalsifiable in real time).

## New confluence surfaced

> **SD-validity within the IRL/ERL cycle** *(SPECULATIVE — offered for a future backtest, documented nowhere):*
> an unreached standard-deviation / IPDA target stays "live" as the external magnet only while price is inside
> an IRL consolidation; once external liquidity is actually taken, a **new** IRL/ERL cycle begins and prior
> projections should be recomputed from the new range rather than carried forward. Bridges two genuinely
> separate ICT ideas (SD-projection validity + IRL/ERL cycling) that the sources never connect. See
> [[concepts/advanced/cbdr-and-sd-projections]].

## How it interacts with the Unified Playbook

The **WHERE** filter in the [[concepts/advanced/README|confluence stack]]: mark 20/40/60-day highs/lows on
NQ/ES/YM; the nearest level is the active near-term draw. A setup ([[concepts/mastery/unified/README]] Layer 3)
gains conviction when its target *is* an IPDA/ERL level, its manipulation sweeps that level, and the Layer-2
SMT stack confirms non-confirmation across the triad at the sweep.

## See Also

- [[concepts/business-logic/ict-liquidity]] — canonical BSL/SSL/DOL (this page extends it with ranked targets)
- [[concepts/advanced/cbdr-and-sd-projections]] — the SD projections that price *toward* these targets
- [[concepts/advanced/README]] — frontier hub + confluence stack
- [[concepts/mastery/unified/README]] — Layer 3 execution
