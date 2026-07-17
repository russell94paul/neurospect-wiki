---
tags: [concept, aura, neurospect, triads, correlation]
aliases: [Triads, Triad Selection, Correlation Sweet Spot]
sources: [sources/neurospect/aura/aura-10-why-these-assets-why-these-triads.md]
created: 2026-07-16
updated: 2026-07-16
---

# Triads & Asset Selection

A **Triad** in Aura terms is a set of correlated assets — usually three — that dOoMeR watches together
specifically to run SMT / cracking-correlation divergence analysis (see
[[concepts/aura/sequential-smt]]). Unlike picking correlated assets "by feel" (his example: "gold and
silver move together... that is not wrong, but it is not enough"), dOoMeR selects and validates every
triad with a specific statistical method before ever looking at a chart: "the math came first. The
data backs it up. That is the order of operations for every triad in this system" (aura-10).

> **Note on framing:** dOoMeR discloses this material was adapted from a compliance/research write-up
> he had to produce for the proprietary trading firm he works for, and says plainly that some of its
> institutional-style language ("institutional behavior," etc.) is not fully what he personally
> believes — he uses it "to satisfy the institutional beliefs and practices," not as his own analytical
> framing (aura-10). Treat the statistical apparatus as his actual method, but the institutional prose
> around it as borrowed packaging.

## How Correlation Is Measured

- All correlation figures use the **Pearson correlation coefficient**, computed on each asset's
  **daily returns** — not raw price levels. Two assets can both run from $100 to $200 without being
  correlated at all day-to-day; returns capture how they actually move together in real time, which is
  what matters for divergence analysis (aura-10).
- The correlation number is calculated **once**, over a long window — typically **2–3 years of daily
  returns** — because a long window is what gives the figure stability.
- A short-term divergence between two normally-correlated assets does **not** invalidate the baseline
  correlation number — that divergence *is* the trade signal, not evidence the correlation broke.
- The number only needs to be revisited if something **structurally** changes about a market — dOoMeR's
  example: a metal permanently losing most of its industrial demand. Otherwise it holds indefinitely.
- Worked figure given: gold vs. silver Pearson correlation on 3 years of daily returns comes out to
  approximately **0.90**, and the same figure holds whether measured on 3 years or 5 years of data —
  "the number is not a guess. It's an output of this exact calculation run at scale" (aura-10).

> **Transcription note:** "based on daily price data from CMA futures" almost certainly mis-hears
> **CME futures** (Chicago Mercantile Exchange) — all instruments discussed (indices, metals, energy)
> are CME Group products. Corrected silently in this page's prose below.

## The Sweet Spot Principle

Correlation alone doesn't make a good triad — the *level* of correlation determines whether a
divergence means anything:

- **Too loosely correlated** → the assets diverge constantly for unrelated reasons; you can't trust any
  given divergence as a signal (too much noise).
- **Too tightly correlated** → the assets rarely diverge at all, and when they do, it's "usually a data
  or timing artifact, not institutional behavior" — not something to trade.
- **The sweet spot:** correlated enough that agreement is the expected baseline, independent enough
  that a divergence carries real information. "Close enough that agreement is expected. Spread enough
  that divergences carry meaning rather than noise" (aura-10).

dOoMeR is explicit that the math is necessary but **not sufficient** — the correlation number tells you
how strongly two assets *were supposed to* move together; only the live chart tells you whether the
resulting divergences are actually catchable and reliable. He flags his own energy triad as a
counter-example: its correlation numbers are just as tight/reliable-looking as the indices triad's, yet
it performs far less cleanly live (see below) — proof that "the numbers may show one thing but when
you actually go and gather data the chart will show another" (aura-10).

## Selection Process (Order of Operations)

1. Screen candidate assets with the Pearson correlation coefficient on daily returns.
2. Keep the ones that land in the sweet spot — correlated enough that agreement is expected,
   independent enough that differences are meaningful.
3. Confirm against live chart/market behavior and fundamental research, to make sure the relationship
   has "a structural reason behind it, not just a number."
4. Only after both the math and the chart agree does an asset make it into a triad.

## The Five Triads

### 1. Metals — Gold, Silver, Platinum

- **Gold + Silver:** both monetary metals, driven by dollar strength, inflation expectations, and
  safe-haven institutional demand — very high correlation (~0.90, see above).
- **Platinum** adds an industrial-demand layer (primarily consumed as an auto-catalyst for emission
  control), giving the triad "a fundamental split between pure monetary demand and real-world industry
  cycles." Gold–Platinum correlation is high but *not as high* as Gold–Silver — exactly the gap that
  produces catchable divergences, structurally analogous to how YM is used against ES/NQ in the
  indices triad (see below).
- dOoMeR chose Platinum over **Copper** as the third leg because, over time, Platinum (combined with
  the [[concepts/aura/aura-asset|Aura Asset]]) showed more opportunities to catch reversals — but he
  states Copper is an acceptable substitute/supplement. When Gold, Silver, and Platinum (or the Aura
  Asset) show *no* divergence, Copper will sometimes still show Sequential SMT as an extra confluence
  check.

### 2. Indices — ES, NQ, YM

- ES and NQ alone are "nearly identical" and too tightly correlated to diverge often. **YM is added
  specifically to lower the correlation just enough to catch more reversals** — the same sweet-spot
  logic as Gold/Silver/Platinum, applied to equity indices. (This is the "standard"/"normal" triad
  referenced throughout [[concepts/aura/sequential-smt]].)

### 3. Energy — Crude Oil (CL), Heating Oil, Gasoline

- Correlation figures here are described as **all very high** across the board — by the sweet-spot
  theory this predicts divergences that aren't prominent/reliable enough to trust.
- Consistent with that prediction, dOoMeR says this is **not one of his favorite triads to trade**,
  though setups do still occur. He attributes some of its unreliability to elevated volatility and
  manipulation tied to an unnamed, ongoing geopolitical conflict he refers to only as "this... war"
  (undated/unspecified in the transcript — flagged rather than assumed).

### 4. Forex — Euro (6E), British Pound (6B), Japanese Yen (6J)

- Traded as **futures**, not the retail-standard CFD-against-DXY approach (he notes DXY is used
  elsewhere, not detailed in this video).
- This triad is dOoMeR's clearest stated example of numbers *undershooting* reality: raw correlation
  between the Euro and Pound alone reads low, "you wouldn't think the yen would have any importance,"
  yet watching actual charts he found EUR/GBP frequently did **not** diverge meaningfully together,
  while pairing in the **Yen** produced reliable, tradeable divergence. His explicit lesson from this:
  treat the correlation number "not as the end-all-be-all, but just a place to start."
  - The **Australian Dollar (6A)** is mentioned as a usable alternative third leg, but the Yen is his
    stated preference.
  - The Aura Asset is noted as "very good for this triad" (forward reference only, not elaborated here
    — see [[concepts/aura/aura-asset]]).

### 5. Crypto — Bitcoin, Ethereum, Solana

- dOoMeR uses **Solana** as the third leg rather than a "Total3 excluding BTC/ETH" index, which he says
  another mentor (transcribed only as "day" — likely the same figure referenced elsewhere in the corpus
  as Tom Dante, but not confirmed by name in this transcript) reportedly uses instead.
- He chose Solana because it showed similarly reliable divergence characteristics to the other triads,
  "also having to do with time" — an unexplained forward reference, presumably to
  [[concepts/aura/time-sum]], not elaborated in this video.

## Numbers vs. Charts: The Explicit Counter-Example

dOoMeR draws a direct contrast between the indices triad and the energy triad to make the point that
correlation strength alone doesn't predict live reliability: "the assessment is it's very tight as well
as the energy triad with oil. However, we know that this triad [indices] is very reliable as well as
this one [metals]. Yet oil does not perform as cleanly as the indices triad." Same statistical profile,
different real-world outcome — "that may be for many other environmental reasons," left unresolved in
the transcript. His conclusion is to trust the chart over the number whenever they disagree.

## How This Feeds Sequential SMT

The triad is the substrate that [[concepts/aura/sequential-smt]] is applied to: a divergence between
two assets is only meaningful *because* the correlation math (plus validated live behavior) has already
established that those specific assets are "supposed to" move together. Every "cracking correlation"
event described in the Sequential SMT material — one asset failing to confirm a high/low the others
already took — is read against the correlation baseline established here. The
[[concepts/aura/aura-asset]] is described as a further refinement layered on top of these standard
triads, surfacing additional Sequential SMT reversals the standard 3-asset triad alone misses — out of
scope for this page, covered in its own.

## See Also

- [[entities/people/doomer]]
- [[concepts/aura/README]]
- [[concepts/aura/sequential-smt]]
- [[concepts/aura/aura-asset]]
- [[concepts/aura/time-sum]]
