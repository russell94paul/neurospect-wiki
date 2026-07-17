---
tags: [concept, business-logic, ict, smt, intermarket, order-flow, neurospect]
aliases: [SMT, Smart Money Technique, Smart Money Tool, SMT Divergence, Cracking Correlation, The Triad, NQ ES YM, Sequential SMT, Sequential Skip, Aura Asset, Triad Correlation]
sources:
  - sources/neurospect/2026-04-18-vol4-class2-smt-divergence.md
  - sources/neurospect/2026-04-18-vol1-class2-consolidation-model.md
  - sources/neurospect/2026-04-20-stream-0830-nfp-fri-tape-reading.md
  - sources/neurospect/2026-04-20-stream-tue-10-fed-chair-testifies.md
  - sources/neurospect/2026-04-22-youtube-1000-points-nq-2026-03-04.md
  - concepts/aura/sequential-smt.md
  - concepts/aura/triads-asset-selection.md
  - concepts/aura/aura-asset.md
  - concepts/aura/time-sum.md
created: 2026-04-18
updated: 2026-07-16
---

# SMT Divergence

SMT (Smart Money Technique / Smart Money Tool) is an intermarket analysis tool that uses divergence between correlated equity indices to confirm or signal a reversal. It is a **confluence tool**, not a standalone entry signal — you need a pre-existing bias before using it.

## The Triad

SMT is applied using the three major US equity futures indices:

| Name | Futures Ticker | Character |
|---|---|---|
| Nasdaq 100 | NQ | Most volatile, widest moves, fastest execution required |
| S&P 500 | ES | Most stable, mid-range volatility, preferred by MrWitness |
| Dow Jones 30 | YM | Special — diverges differently; often the confirming index |

These three indices run on the same algorithmic source code but with independent sub-algorithms. They normally **move in tandem**, so when one breaks correlation, it signals institutional intent.

---

## Cracking Correlation

A cracking (broken) correlation occurs when **one index fails to do the same thing as the other two** at an important price level. This is the core SMT signal.

When the correlation cracks:
- The algorithm has "recorded" the level as hit (because 2 of 3 hit it)
- The non-confirming index will not need to reach that level
- This creates **accumulation** (bullish) or **distribution** (bearish) at those levels

> "The algorithm sends a message to the source code: we hit the level. ES doesn't need to come all the way back because the source code thinks the level was already hit." — Vol 4 Class 2

---

## Bullish SMT (Accumulation Signal)

**Condition:** NQ and/or YM make a lower low at a major liquidity level, while **ES makes a higher low** (or fails to take that same low).

- Signals: smart money is accumulating long positions
- The ES "cracking" away from the lower low is the tell
- Expect a reversal higher from that zone

---

## Bearish SMT (Distribution Signal)

**Condition:** ES makes higher highs while **NQ makes lower highs** at a major liquidity level.

- Signals: smart money is distributing (selling) as retail buys the breakout
- NQ's inability to make new highs is the tell
- Expect a reversal lower from that zone

---

## Price SMT vs. PDR SMT

| Type | Description |
|---|---|
| **Price SMT** | One index makes lower low / higher low at a price level (big pool of liquidity) that another index takes or fails to take |
| **PDR SMT** | One index fails to tap the same PDA (order block, FVG) at the same time as the others — a fractured reaction at a shared PDA level |

PDR SMT example: NQ and YM both return to and bounce from a bullish breaker block; ES does not tap it at the same time. That crack in PDR reaction is the SMT. Enter on an inversion FVG or the next entry signal in the direction of the reversal.

---

## How to Set Up Charts

**Option 1 — Separate panes:**  
In TradingView: Add Symbol → ES (or NQ/YM) → New Pane. Shows both price charts stacked — easy to compare highs/lows visually.

**Option 2 — Overlay (same scale):**  
Add Symbol → Same Percentage Scale → Change to line chart → adjust color/thickness. Both instruments on one chart, easier for quick glances during live trading.

**Option 3 — Three-panel template:**  
Separate templates/charts for each: ES | YM | NQ side by side. Best for full analysis sessions.

---

## Context Requirements

1. **Have a bias first.** SMT is most powerful when you already know the market is bullish or bearish (via HTF FVG + opening price position from [[ict-narratives]]).
2. **SMT at the manipulation leg.** The manipulation leg of Power of Three is where SMT most frequently appears — price sweeps below midnight open, one index makes a lower low, another doesn't → accumulation, reversal imminent.
3. **Combine with a PDA entry.** After identifying SMT, wait for the entry signal: inversion FVG, rejection block, or OTE block at the reversal zone.

## Trusting the Buy/Sell Program

SMT divergence is one of the signals that a **program switch** has occurred. Once confirmed, all entry models become higher probability.

**Trust the buy program when:**
- The market has taken a sell-side liquidity pool (at minimum a 15-minute swing low) before the reversal
- After this sweep, bullish PDAs start holding and FVGs stay open (LRLR conditions begin)
- SMT at the sweep = strongest possible confirmation

**Trust the sell program when:**
- The market has taken a buy-side liquidity pool before the reversal
- Bearish PDAs start holding and FVGs stay open to the downside

> "How do you know to trust a buy program? The market has taken a big sell-side pool. Or at least a minor one. Once that happens, whatever model you use — even a breakout model — is going to work." — YouTube: +1000 Points NQ (2026-03-04)

Conversely, if the market is delivering toward your bias WITHOUT taking any opposing liquidity first, expect high-resistance conditions and deep retracements even after SMT signals.

## NQ vs. ES vs. YM: Strongest/Weakest in Trending Markets

In strongly trending conditions, the three indices do not contribute equally:

- **Weakest asset on a bullish day:** NQ ("the sixth sister" — lags behind, doesn't take highs as cleanly)
  → Use ES for cleaner long entries on bullish trending days
- **Weakest asset on a bearish day:** ES often holds up longer than NQ or YM
  → NQ can lead the decline; YM provides the clearest confirmation

Live trading note (streams): "YM and ES made higher highs for the day; NQ is the sixth sister, still dancing." → MrWitness uses this to confirm the bullish bias is still intact even when NQ lags.

This is distinct from the "Six Sisters" concept (a separate intramarket pattern, Vol 4 future class). Here "sixth sister" is informal stream language for the lagging index.

Source: `sources/neurospect/2026-04-20-stream-0830-nfp-fri-tape-reading.md`, `sources/neurospect/2026-04-20-stream-tue-10-fed-chair-testifies.md`

---

## SMT in the London Model / Consolidation Model

In the 2022 model (Vol 1 Class 2), MrWitness demonstrates SMT at the London session low:
- Asia consolidates; London takes the SSL (Asia low)
- At that exact SSL, ES fails to make a new lower low while NQ does → classic bullish SMT
- Entry: expansion retracement model or consolidation model above the EQ

---

## SMT vs. Six Sisters

A related but **different** concept called "Six Sisters" is referenced in Vol 4 as a future topic (not yet in the captured curriculum). Do not confuse the two:
- **SMT**: intermarket divergence between NQ/ES/YM
- **Six Sisters**: a different intramarket pattern (details pending curriculum capture)

---

## Aura Extension: Sequential SMT

> **Aura (dOoMeR):** Sequential SMT is ordinary SMT — cracking correlation across a correlated triad of assets — filtered through **time-cycle nesting**: a swing point only carries real weight when its SMT is confirmed across two or more adjacent time cycles (e.g. a weekly-cycle SMT with a daily-cycle SMT nested inside it). "It allows you to catch higher time frame move on the lower time. It allows you to fractalize SMT" (aura-07). This is explicitly a probabilistic filter, not a guarantee: "this does not happen every single time, but it happens a large percent of the time... within trading, you don't need something that happens every time" (aura-07).

### Cycle-naming convention (Aura)

The cycle label is set one level up from the chart you're reading it on: mark swing points on the weekly chart and filter for SMT, and what you're looking at is **monthly-cycle SMT** (aura-07).

### Cross-cycle gap-pairing (Aura)

To confirm SMT at a given cycle, Aura checks gaps at a matching lower time frame:

| Cycle being confirmed | Gap time frame to check |
|---|---|
| Weekly cycle SMT | Daily gaps |
| Daily / session cycle SMT | 4H gaps |
| Micro cycle SMT | 15m–1H gaps |

(aura-12)

### "Extreme of the range" targeting rule (Aura)

If SMT occurs *between* two segments of a larger cycle (between quarters within a week, between days within a session, between hours), Aura expects the **extreme of that larger segment** to eventually be taken — "this goes for all cycles" (aura-12).

### LTF entry (Aura)

Aura's preferred lower-time-frame entry once a Sequential SMT is confirmed is off the formation of an **inverse fair value gap (iFVG)**, with a plain FVG formation as fallback (aura-12) — compare MrWitness-AXL's own PDA-entry list above ([[#Context Requirements]]: inversion FVG, rejection block, OTE block), which already includes the inversion FVG as an option.

### Sequential Skip (Aura)

**Aura (dOoMeR):** Sequential Skip is the fallback confirmation path used when the immediately-adjacent lower cycle does **not** confirm a higher-time-frame Sequential SMT — a cycle further down the stack confirms directly instead, "skipping" the missing intermediate link. It is fractal and works at any pair of cycles (quarterly→monthly, weekly→daily→session, daily→micro) (aura-14).

- **Cross-asset variant:** if the day's directional bias is set but the primary asset in the triad doesn't offer a clean entry, Aura looks for the same setup on a **different triad member** moving in the bias direction — e.g. NQ sells off too hard to chase, but YM continues higher into the open; since the trader is bearish within the triad, that YM strength is used to frame the short (candle-level SMT + iFVG entry) (aura-14).

Full mechanics, worked examples, and homework: [[concepts/aura/sequential-smt]].

---

## Aura Extension: Math-First Triad Selection

**Aura (dOoMeR):** rather than picking correlated assets "by feel," Aura validates every triad with the **Pearson correlation coefficient** computed on each asset's **daily returns** (a 2–3 year window) before it ever reaches a chart: "the math came first. The data backs it up" (aura-10).

- **The sweet spot principle:** a good triad is correlated enough that agreement is the expected baseline, independent enough that a divergence carries real information — too tight and divergences are noise/data artifacts, too loose and divergences are constant and untrustworthy (aura-10).
- **The five triads:** Metals (Gold/Silver/Platinum), Indices (ES/NQ/YM), Energy (CL/Heating Oil/Gasoline), Forex (6E/6B/6J), Crypto (BTC/ETH/SOL) (aura-10). The indices triad is the one referenced throughout this page.
- Math is necessary but not sufficient — Aura confirms every candidate triad against live chart behavior and fundamental research before adoption, and explicitly trusts the chart over the correlation number when the two disagree (aura-10).

> **Convergence (independent derivation):** MrWitness-AXL states YM "diverges differently / often the confirming index" within the ES/NQ/YM triad ([[#The Triad]] above). Aura (dOoMeR) independently arrives at the same structural role via the correlation math: "ES and NQ alone are nearly identical and too tightly correlated to diverge often. YM is added specifically to lower the correlation just enough to catch more reversals" (aura-10). Two different mentors, two different methods (observational vs. Pearson-correlation-first), same conclusion about YM's role in the triad.

Full selection process, all five triads, and the numbers-vs-charts discussion: [[concepts/aura/triads-asset-selection]].

---

## Aura Extension: The Aura Asset (6S)

**Aura (dOoMeR):** wholly new material relative to the curriculum above — no dollar-index or DXY-proxy concept currently exists elsewhere on this page. The **Aura Asset** is dOoMeR's name for the Swiss Franc futures contract (CME ticker **6S**), added as a **universal fourth leg to every triad** (metals, indices, energy, forex, crypto) — a synchronized dollar-proxy divergence tell (aura-15).

- **Why 6S over DXY:** DXY is not a time-synchronized futures contract — its candles don't open/close in sync with the futures actually traded across the system (gold, indices, currency futures), which Aura treats as inconsistent with a methodology built entirely around time-based divergence and time-based confirmation. 6S is a properly listed CME futures contract on the same clock, while still tracking DXY's shape closely on higher timeframes (aura-15).
- **How it's read:** the Aura Asset is fed into the same Sequential SMT divergence framework already used on the standard triads — watched for weekly-, daily-, and session-cycle divergence as an extra comparison leg (aura-16). Worked examples show it explaining chop and reversal sequences that produced **no visible divergence at all** on the standard triad.
- **Reliability by triad:** strongest on indices, metals ("bullion"), and forex; weakest on energy, which Aura already flags as an unreliable triad on the correlation math alone (see above) (aura-15, aura-16).
- **dOoMeR's own caveat:** the *origin story* for why 6S specifically — a personal chain of reasoning running from gold-as-elite-currency through a Springmeier document to a thesis about Switzerland's neutrality — is explicitly flagged by dOoMeR as an unverified personal theory, separate from and not a substitute for the quantitative triad-correlation work: "I am not presenting any of what follows as fact... at that point I went and checked the charts and the charts did the rest of the talking" (aura-15). Aura's own **Time Sum ("369")** concept, covered in the same lesson, is similarly de-emphasized by dOoMeR as a minor, subjective, rarely-used confluence — not adopted here as a core concept (aura-16; see [[concepts/aura/time-sum]] for detail).

Full reasoning chain, chart validation, and scope of use: [[concepts/aura/aura-asset]].

---

> **Divergence (attribution):** MrWitness-AXL uses SMT as a **confluence tool** at the Power-of-Three manipulation leg — it requires a pre-existing bias and confirms rather than initiates ([[#Context Requirements]] above). Aura (dOoMeR) elevates **nested Sequential SMT** to the primary structural signal that anchors and flips entire trading ranges — ranges are built and re-anchored directly off which swing points carry confirmed cross-cycle SMT, ahead of and independent from any separate bias-formation step (aura-11, aura-12). Both are retained as described by their respective mentors; not merged into a single rule.

---

## See Also

- [[ict-market-structure]] — SMT confirms market structure at the ITL/ITH
- [[ict-liquidity]] — SMT often signals that a liquidity sweep is completing
- [[ict-narratives]] — SMT is most powerful at the manipulation leg of Power of Three
- [[ict-entry-models]] — entry patterns to use after SMT signals accumulation/distribution
- [[ict-order-flow]] — SMT as an order flow distribution/accumulation signal
- [[ict-live-commentary]] — live "cracking correlation" calls and trust-the-program framework in practice
- [[concepts/aura/sequential-smt]] — Aura (dOoMeR): time-cycle-nested SMT filter (Sequential SMT / Sequential Skip)
- [[concepts/aura/triads-asset-selection]] — Aura (dOoMeR): Pearson-correlation-first triad selection (the 5 triads)
- [[concepts/aura/aura-asset]] — Aura (dOoMeR): universal 4th triad leg (Swiss Franc futures, 6S)
- [[concepts/aura/time-sum]] — Aura (dOoMeR): how the Aura Asset is read as an SMT leg (369 concept de-emphasized)
