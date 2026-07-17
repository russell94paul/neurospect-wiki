---
tags: [concept, aura, neurospect, smt]
aliases: [Sequential SMT, Sequential S&T, Sequential Skip]
sources: [sources/neurospect/aura/aura-07-sequential-smt.md, sources/neurospect/aura/aura-11-ranges-and-sequential-smt.md, sources/neurospect/aura/aura-12-confirming-sequential-smt-and-framing-trades.md, sources/neurospect/aura/aura-14-sequential-skip.md]
created: 2026-07-16
updated: 2026-07-16
---

# Sequential SMT

Sequential SMT is dOoMeR's signature technical concept and, by his own account, "one of the only
concepts from [an earlier mentor's] teaching that I still use" (aura-07) — he deliberately dropped
that mentor's other tools (push, swing points, opens) in favor of simplicity. At its core, Sequential
SMT is ordinary SMT (cracking correlation across a correlated triad of assets — see
[[concepts/aura/triads-asset-selection]]) filtered through **time-cycle nesting**: a swing point only
counts as carrying real weight when its SMT shows up in a fractal, sequenced relationship across two or
more adjacent time cycles, not just on one chart in isolation. "It allows you to catch higher time
frame move on the lower time. It allows you to fractalize SMT" (aura-07).

> **Transcription note:** the auto-captions render "SMT" inconsistently as "S&T," "S&P," "sequen S&T,"
> "sequential cent," and similar — silently normalized to **SMT** throughout this page per the ICT
> glossary. The mentor referenced in aura-07 as the source of the original (non-Sequential) SMT/swing
> point/opens teaching is transcribed only as "DA's teaching" — the correct name is not recoverable
> from this transcript and is flagged rather than guessed.

## What Is Sequential SMT

dOoMeR works a stack of nested time cycles — he states he focuses on "quadrennial [captioned
'quadrrenial'] to the session cycle or the 90 minutes," explicitly skipping the micro cycle (aura-07).
Sequential SMT is the observation that swing points which show **SMT confirmed at more than one
adjacent cycle in the stack** — e.g., a weekly-cycle swing point that also carries daily-cycle SMT
nested inside it, or a monthly swing point echoed by weekly SMT — have "a higher chance of holding
compared to [swing points] that don't" (aura-11), and that when a higher-time-frame SMT lines up with
a lower-time-frame SMT at the same level, "large expansive moves tend to happen" (aura-07). This
alignment across cycles is the "sequential" in Sequential SMT: it is not one SMT signal, it is a
*sequence* of SMT confirmations nested fractally from a higher cycle down into a lower one.

dOoMeR is explicit that this is a probabilistic filter, not a guarantee: "this does not happen every
single time, but it happens a large percent of the time. And within trading, you don't need something
that happens every time. If you manage your risk precisely, you need something that happens a higher
percentage of the time" (aura-07).

### Worked examples (aura-07)

- **Weekly cycle, indices triad:** a previous week's high was taken out on ES and NQ but **failed to
  be taken out on YM** — bearish SMT at that high, within the weekly cycle — which preceded a large
  expansive move.
- **Daily nested in weekly:** within the same week, Wednesday failed to take out Tuesday's high on one
  asset while it was taken on ES — SMT within the weekly cycle at the day level, nested inside the
  larger weekly structure.

### The cycle-naming convention

A swing point's "cycle" name depends on which chart you're viewing it on, one level up: mark swing
points on the weekly time frame and filter for the ones carrying SMT, and what you're looking at is
**monthly cycle SMT** (aura-07 homework framing). This nesting convention — the chart you're reading
determines the cycle label one level higher — recurs throughout the rest of this concept.

## Using Sequential SMT to Anchor and Flip Ranges

(Range/premium/discount/equilibrium mechanics themselves are covered in [[concepts/aura/ranges]] —
this section is specifically how Sequential SMT is used to build and manage them, per aura-11.)

- **Anchor range extremes at higher-time-frame swing points that carry SMT**, not at just any local
  high/low. A swing point with confirmed SMT is treated as the trustworthy edge of a range; one
  without it is not.
- **The indicator only displays currently-valid Sequential SMTs** — as soon as one is invalidated it
  disappears, so the trader is always reading the current, correct state rather than stale signals
  (aura-11).
- **False-sweep / ambiguous-low rule:** when a higher-time-frame swing low looks "false" (price didn't
  cleanly take the prior asset's low) and there are two candidate lows with a large gap between them,
  prefer the low that was **actually swept on all assets in the triad**, even if it isn't the most
  extreme candidate — that's the level the whole triad agrees on (aura-11).
- **Range lifecycle:** once a range is established, keep following it until either (a) an **opposing**
  Sequential SMT forms, or (b) **another** Sequential SMT of the same cycle forms — either ends/extends
  the current range. dOoMeR explicitly says not to overthink simultaneous/overlapping ranges: "if you
  want, you can have two ranges if you prefer that... it shouldn't be very complicated" (aura-11).
- **New range creation:** a new higher-time-frame Sequential SMT plus an expansive move away from it
  creates a **new** range, anchored at that new swing point.
- **Fractal, self-similar loop observed live (aura-11):** HTF range established → price retraces
  toward discount of the HTF range, targeting liquidity within a gap → a lower-cycle Sequential SMT
  forms in that discount zone → expansive move up creates a new, smaller range targeting the *previous*
  range's premium liquidity → a Sequential SMT then forms at that premium → expansive move down flips
  into a new range targeting the *original* range's discount liquidity. This repeats as price develops
  — "very boring... but it's very simple. And that's how it should be — repetitive" (aura-11).
- dOoMeR notes in passing that not every asset in the triad needs to confirm for the range logic to
  hold — e.g., a retracement into discount may show on YM but not NQ/ES — and foreshadows that the
  [[concepts/aura/aura-asset]] surfaces additional Sequential SMT catches the standard triad misses
  (aura-11; Aura Asset itself is out of scope for this page).

**Homework (aura-11):** without looking ahead, pick a random historical date, mark the higher-time-
frame range, then step forward bar by bar — simulating live price reading — extending or flipping the
range as new Sequential SMT + expansion occurs. Target ~50 reps.

## Confirming Sequential SMT

aura-12 gives an explicit list of ways to confirm a Sequential SMT before trusting it:

1. **Cross-cycle confirmation.** A higher-time-frame Sequential SMT confirmed by a lower-time-frame
   Sequential SMT, or vice versa — the core fractal-nesting mechanic described above.
2. **Gap confirmation ("SMT fill" / "SMT fail").** Look at how the triad's assets react to a shared
   gap (FVG, NWOG/NDOG): if one asset retraces *into* the gap while another does not, that
   non-uniform reaction is itself a confirming signal — "a form of what many call an SMT fail." Works
   especially well for daily/session-cycle SMT, confirmed using 4H/1H candles.
3. **Candle-level confirmation.** A cycle's swing point is confirmed if the candle that creates it
   *also* creates SMT against the immediately preceding candle on the same time frame (e.g., a daily
   cycle formed on a 4H candle that also shows SMT vs. the prior 4H candle).
4. **Sequential Skip** — a distinct, more advanced confirmation path used specifically when the clean
   two-stage HTF→LTF relationship isn't present. Covered in its own section below.

### Worked example — "playing the weekly range" (aura-12)

A full confluence stack, walked through live:

1. **Pre-market/desk routine.** Arrive at the desk (~7:45–8:00 AM), observe the higher time frame
   first (weekly, ideally the Aura Asset once available). Note weekly-cycle SMT above and below.
2. **Confirm the HTF level with nested confirmations:** a daily-cycle SMT forms in support of the
   weekly level; that daily swing point is itself confirmed by 4H SMT against the previous 4H candle;
   an SMT fail within a gap adds a third layer (one asset, e.g. YM, retraces into the gap while the
   others don't).
3. Once the HTF level is trusted through that stack — even while price sits in premium — it becomes
   the anchor for a new, lower-time-frame range.
4. **Entry execution.** Drop to the 3-minute or 5-minute chart. Preferred entry is off the formation of
   an **inverse fair value gap (iFVG)**, or a plain FVG formation as a fallback. dOoMeR prefers to wait
   for a session-cycle (or micro-cycle) Sequential SMT *within discount* of this LTF range before
   entering, for a more precise/lower-risk entry — explicitly trading fewer signals for higher quality,
   which requires disciplined risk management since it produces more misses.
5. **Premium vs. discount entries and R:R:** entering while in premium of a range means targeting a
   *lower* risk-to-reward, because price may retrace to equilibrium and stop the trade out before a
   larger target is reached.

### The "extreme of the range" targeting rule

If SMT occurred *between* two segments of a larger cycle — between quarters within a week, between
days within a session, between hours — expect the **extreme of that larger segment** to eventually be
taken. dOoMeR states this generalizes across all nested cycles: "this goes for all cycles" (aura-12).

### Take-profit framework (pre-Aura-Asset, "to be safe" version)

- Full take-profit at equilibrium of the HTF range, **or**
- Hold for liquidity within discount of the HTF range / the HTF range's extremes, **or**
- (Advanced, deferred) exit-to-re-entry systems — described as adding unnecessary stress at this stage
  of the framework.

More granular, multi-level take-profit systems require the Aura Asset, which surfaces additional
Sequential SMT levels — deferred to [[concepts/aura/aura-asset]].

### Cross-cycle gap-pairing rule (aura-12)

To confirm SMT at a given cycle, compare gaps at the matching lower time frame:

| Cycle being confirmed | Gap time frame to check |
|---|---|
| Weekly cycle SMT | Daily gaps |
| Daily / session cycle SMT | 4H gaps |
| Micro cycle SMT | 15m–1H gaps |

**Homework (aura-12):** either (1) mark historical weekly ranges and identify where the optimal entries
occurred, or (2) the "New York open" drill — repeatedly review price around the NY open without
looking ahead: was there HTF (weekly/daily) Sequential SMT above? Was it confirmed by session-cycle SMT
(e.g., forming on the 9:00 candle, confirmed against the prior candle)? Repeat until pattern
recognition is automatic, then test candle-by-candle on unseen dates.

## Sequential Skip

Sequential Skip is the confirmation path used when price does **not** deliver a clean two-stage
HTF→adjacent-cycle relationship — dOoMeR: "it may not always be a weekly to daily or a daily to
session cycle or a quarterly to monthly... this is where I came to the sequential skip" (aura-14).

**Definition:** when a higher-time-frame Sequential SMT forms but the *immediately adjacent* lower
cycle does **not** confirm it, a cycle **further down** the stack can confirm it directly instead,
"skipping" the missing intermediate link. It is fractal and works at any pair of cycles: quarterly→
monthly, weekly→daily→session, daily→micro (aura-14: "it is fractal. The sequential skip can work on
the higher time frame cycles or the lower time frame cycles").

### Worked example (aura-14)

- A weekly-cycle SMT forms with monthly-cycle support — but the daily cycle does **not** confirm it.
- Observing live from the 8:00 candle: a new-day-opening-gap is present, price sits in premium of the
  weekly range.
- At 8:55, a **session-cycle** SMT forms instead — confirmed by SMT against the previous hourly candle
  (8:00 vs. 9:00) — and a gap forms. This session-cycle confirmation is treated as sufficient to trust
  the HTF (weekly) bias even without the missing daily link.
- Entry: the stated-preferred 5-minute inverse FVG, either off the gap's formation (before 9:30) or
  after waiting for the 9:30 NY open for confirmation.

### Execution discipline around Sequential Skip

dOoMeR explicitly recommends **waiting for the 9:30 open** rather than entering off the pre-9:30 gap
formation, especially for traders who "struggle" or "may not have consistency" — a pre-9:30 setup can
run away without offering a precise entry. He frames the alternative explicitly: entering pre-9:30 out
of urgency (needing to hit a goal, pass an account, make a payout), getting stopped out at 9:30 as
price reverses, and spiraling into revenge trading. The stated escape valve is patience: "you can live
to trade another day," including trading a different asset that day, or not trading at all — tied
directly back to the risk-management lesson from the previous day (aura-13).

### Cross-asset variant of Sequential Skip (aura-14)

If the day's directional bias is set but the primary asset doesn't offer a clean entry (e.g. NQ gaps
too far to chase at 9:30), look for the **same setup on a different triad member** moving in the
overall bias direction. Worked example: NQ sells off hard and is "too large" to chase; meanwhile YM
continues higher into the open — since the trader is bearish within the triad, that YM strength (not
NQ's own price action) is used to frame the short: an inverse FVG entry on YM, confirmed by candle-
level SMT, executed in the direction of the original bias. The setup still requires the same
confirmation criteria (candle SMT + iFVG) — only the asset chosen from the triad changes.

dOoMeR stresses this pre-planning (HTF range context, premium/discount position, prior liquidity
already taken) should be done during post-market review of the prior session or pre-market review of
the current day — not improvised live.

**Homework (aura-14):** find Sequential Skip setups, starting simple (weekly→session or daily→micro).
Target modest, achievable risk-to-reward (examples given: 1:2, 1:3) rather than chasing outsized R:R —
note dOoMeR phrases this as "low risk-to-reward setups," which reads inconsistently against those same
1:2/1:3 numbers; likely intended as "realistic/achievable" rather than literally low, flagged rather
than silently resolved.

## See Also

- [[entities/people/doomer]]
- [[concepts/aura/README]]
- [[concepts/aura/triads-asset-selection]]
- [[concepts/aura/ranges]]
- [[concepts/aura/swing-points]]
- [[concepts/aura/aura-asset]]
- [[concepts/aura/risk-management]]
