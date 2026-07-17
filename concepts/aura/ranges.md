---
tags: [concept, aura, neurospect]
aliases: [Aura Ranges, Range Theory]
sources: [sources/neurospect/aura/aura-08-ranges.md, sources/neurospect/aura/aura-11-ranges-and-sequential-smt.md]
created: 2026-07-16
updated: 2026-07-16
---

# Aura Ranges

Ranges are dOoMeR's central structural concept — he says outright that "only highs and lows, ranges and gaps are important in the market," explicitly rejecting order blocks and other PDA-style terminology as unnecessary (aura-08). A range is simply the price territory between a swing high and a swing low, and the market's whole behavior — from the daily chart down to the 5-minute chart — is described as continuously ranging from high to low, retracing into premium/discount, then breaking into a new range and repeating (aura-08).

## What a Range Is

> "The market consists of highs and lows and just ranging from each high to each low. Going from higher time frame... premium and discount to lower time frame... premium discount to higher time frame." (aura-08)

A range is bounded by a swing high and a swing low (see [[concepts/aura/swing-points]]). Ranges nest inside each other at every timeframe — a large HTF range contains smaller LTF ranges, and price constantly moves from a lower-timeframe premium/discount position into a higher-timeframe one and back, "again and again and again" (aura-08). This nesting is the same fractality theme used for swing points and gaps.

## Two Ways to Identify a Range

dOoMeR names two approaches, but uses only the second in practice (aura-08):

1. **Time-based ranges** — e.g. a "quarter" on the 4-hour chart equals one calendar week. Mentioned once as an alternative method, not developed further in this lesson.
2. **Expansive-move-based ranges (his method)** — identify ranges off of expansive moves between HTF swing points. This is the method he uses exclusively and teaches in depth.

### The expansive-move method, step by step (aura-08)

1. Start from HTF swing points (from [[concepts/aura/swing-points]]).
2. Find the largest expansive move between two swing points — this expansive move *is* the range.
3. A **new range** is created when price expands above a prior significant high (for a bullish range) or below a prior significant low (for a bearish range): "once this opens and we have this expanse move that's above a large high right that becomes our range."
4. If price does **not** retrace into the discount of the current range, keep extending/marking the range higher rather than drawing a new one: "if we don't come into discount of this range, you just keep on marking higher, you continue to mark higher."
5. Once price does dip into discount (or premium, for a bearish range) of the current range, that dip can become the anchor for the **next** range.

### Rejecting "order block" as a concept

dOoMeR is explicit and repeated on this point (aura-08): what most traders would label an "order block" — the origin candle(s) of an expansive move that price later returns to test — he simply calls the range itself, and doesn't use order-block terminology or think in those terms:

> "I don't use order block, right? I'm not looking for order block. All I'm looking for are expansive moves." (aura-08)

He states multiple times across the lesson that a level "some may say" is an order block is, in his framing, just price returning to the discount/premium of the range that formed from that same expansive move (aura-08). This is presented purely as his own preferred lens on price — he doesn't argue the order-block framing is wrong, just that he doesn't use it.

## When Is a Range Still Valid? (The "Not Broken" Rule)

A range remains the operative range as long as it has not been invalidated by a close through it:

> "This range was not broken. So this can still be the range. What I mean by it not being broken is there was not price that closed below it." (aura-08)

Invalidation requires a **candle close** beyond the range boundary — a wick through the level, without a close beyond it, does not break the range.

## Finding a Range When It Isn't Obvious

> "If you come into a level within price and you cannot find the range... this is the most recent low and the most prominent high... If it's not obvious, guys, zoom out. It will not always be obvious, but... zoom out until it becomes obvious." (aura-08)

The fallback heuristic is simple: anchor to the most recent obvious low and most prominent obvious high, zooming out on the chart until that pair becomes visually unambiguous.

## Levels Within the Range

dOoMeR uses **discount**, **equilibrium**, and **premium** as the three reference zones within a range (aura-08) — e.g. "once we have gone into equilibrium of this range" and repeated references to price moving "into discount" or "into premium" of a range. He does **not** mention a quadrant subdivision (0.25/0.75 levels) anywhere in this material — only the three-part discount/equilibrium/premium framing appears in aura-08 or the ranges-relevant portion of aura-11.

## Ranges Are Fractal and Can Nest

A smaller range can sit entirely inside a larger one, and the smaller range's key level (typically its low, in a bullish HTF range) becomes a meaningful reversal/attraction level even after price has moved on to the larger range:

> "As price develops, we take out the previous range low that was inside of a higher time frame range. Now, these levels can serve as high attractions of price and reversal areas." (aura-08)

He calls this explicitly "a range within a range" (aura-08).

## Ambiguity Is Acceptable

dOoMeR repeatedly says that when two candidate ranges are both defensible (e.g. keeping the same low but debating which high to pair it with), it is fine to track both: "You can either continue this low and just move the high or you have a new range here... you can have two, right?" (aura-08). He does not force a single canonical range when the chart is genuinely ambiguous.

## Refinement via SMT-Qualified Anchors (aura-11)

One week later, dOoMeR refines the method taught in aura-08 by introducing indicators (built by a collaborator referred to as "no degree" in the transcript) that auto-plot Sequential SMT on the chart, and uses Sequential SMT to decide **which swing points are valid range anchors**:

> "I want to position the extremes of my ranges... on swing points, higher time frame swing points that have SMT within them." (aura-11)

This directly builds on the qualification rule from [[concepts/aura/swing-points]] — swing points with SMT hold more reliably, so they make better range anchors than unqualified swing points. Key refinements from aura-11:

- **New range trigger (refined):** a HTF Sequential SMT event plus an expansive move away from the prior trend is the confirmation signal to anchor a new range at that swing point. Tracking continues "until we either have an opposing sequential SMT or another sequential [SMT] of the same time frame" — either can validly close out the range.
- **Handling false/ambiguous swing points across the triad:** if a HTF swing point is "false" — it doesn't take the previous swing's low on all assets in the triad — dOoMeR gives two options: use the original low, or, "if there is a large gap," prefer the low confirmed by whichever correlated asset actually took that level. He notes a general preference for "the low to the right" (the swing confirmed across assets) over marking from an unconfirmed candidate.
- **Ranges nest across cycles:** the same range logic applies recursively to the session, daily, weekly, quarterly, and yearly cycles — not just the standard weekly/daily triad view. Higher-cycle SMT (e.g. a yearly-level SMT signal) raises confidence that a given HTF level will hold: "we did have that yearly above. So, I do not expect this high to be taken."
- **Anchoring must use the true HTF swing point, not a lesser nearby one.** dOoMeR corrects himself mid-lesson to emphasize zooming out to confirm which swing point is genuinely the higher-timeframe one before anchoring: "if you remember the previous lower high that I'm talking about, that is not the higher time frame swing point. This is the higher time frame swing point."

The mechanics of what qualifies as "Sequential" SMT (as distinct from ordinary SMT divergence) are covered in [[concepts/aura/sequential-smt]], not here — this page only covers how SMT qualification is *used* to anchor ranges.

## How Ranges Drive Trade Framing

Once a range is established, dOoMeR uses its discount/premium as the primary target zone, further refined by liquidity sitting inside gaps within that discount/premium (see [[concepts/aura/gaps]]):

> "As we get a higher time frame sequential SMT and expansion again away, you have a new range that has developed... Now we can target the previous ranges premium [liquidity]. Now you can already start to gather how you can frame setups and targets and models within these basic concepts." (aura-11)

Full trade-framing mechanics (entries without Sequential SMT, model construction) are deferred to a later lesson (aura-12) and are out of scope for this page.

## Homework

- **aura-08:** Mark out at least 50 ranges, across multiple timeframes, using the expansive-move method (not time-based ranges).
- **aura-11:** Refine and expand the same 50 ranges using Sequential SMT as the anchor-qualification filter. Framed as *simulating live price-action reading* rather than mindlessly marking ranges in hindsight — start from a random point in chart history and build the range forward, bar by bar, the way it would have looked live. No submission required, unlike prior homework.

## See Also

- [[concepts/aura/swing-points]] — ranges are anchored on swing points; SMT-qualified swing points make stronger anchors
- [[concepts/aura/gaps]] — liquidity within gaps refines exactly where inside a range's discount/premium price is headed
- [[concepts/aura/sequential-smt]] — the SMT mechanics used in aura-11 to qualify range anchors
- [[entities/people/doomer]]
- [[concepts/aura/README]]
