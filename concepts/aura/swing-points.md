---
tags: [concept, aura, neurospect]
aliases: [Aura Swing Points, Swing Point SMT]
sources: [sources/neurospect/aura/aura-06-swing-points.md, sources/neurospect/aura/aura-11-ranges-and-sequential-smt.md]
created: 2026-07-16
updated: 2026-07-16
---

# Aura Swing Points

Swing points are the atomic unit of dOoMeR's entire framework — he states directly that they are "the basis for pretty much everything": they are how he catches large higher-timeframe (HTF) expansion moves, and how he identifies ranges (aura-06). Every later concept (ranges, gaps, Sequential SMT) is built on top of correctly marking swing points first.

## Definition

The source transcript for this lesson is short (6:47) and the auto-captions are rough on this exact line, but reconstructed against dOoMeR's own candle-numbering language later in the same video, the definition is the standard 3-candle swing pattern:

- **Swing low**: a candle whose low is lower than the low of the candle before it, followed by a candle whose low is higher than it — i.e. price makes a "lower low" into the point and a "higher low" out of it. The middle candle is the swing point.
- **Swing high**: the mirror image — a "higher high" into the point, then a "lower high" out of it.

> Note on source clarity: the raw caption reads "Swing point is obviously a low. Lower low. Higher low. That's one. High. Higher. High. Lower high. It's another." (aura-06) This is garbled auto-caption text: dOoMeR never explicitly says "three candles" in this lesson. The 3-candle read above is inferred from his own candle-1/candle-2/candle-3 references later in the same video when he discusses SMT at swing points ("candle two failed to take out... candle 3 failed to take out the high") (aura-06). Treat the exact wording as a reconstruction, not a verbatim quote, until corroborated elsewhere in the corpus.

The candle numbering convention: **candle 2 is the swing point itself** (the center/pivot candle), flanked by candle 1 (before) and candle 3 (after) (aura-06).

## Swing Points Are Fractal

dOoMeR's central point in this lesson: swing points look identical across every timeframe. Strip the timeframe label off a chart and a daily swing point is visually indistinguishable from a 5-minute or 1-minute swing point (aura-06):

> "If you didn't know what time frame we were on by this lower label, they would all look identical, right? Because the daily can look like the five minute, the five minute can look like the one minute." (aura-06)

This fractality is a recurring theme across the whole technical framework — the same statement is repeated almost verbatim for ranges (aura-08) and gaps (aura-09). Swing points, ranges, and gaps are the same three structural primitives repeating at every scale.

## Why Swing Points Matter

dOoMeR lists three direct uses, in his own words (aura-06):

1. **Catching HTF expansion moves** — swing points mark where an expansive move begins/ends on a higher timeframe.
2. **Identifying the correct ranges** — a range's extremes are anchored on swing points (see [[concepts/aura/ranges]]).
3. **Basis for "pretty much everything"** — every later concept in the curriculum builds on correctly-marked swing points.

## Qualification Rule: SMT at the Swing Point

The homework in this lesson (see below) has students color-code swing points by whether SMT divergence occurred there between correlated assets in the triad (e.g. NQ vs. YM at the same swing) — but this lesson does not yet state *why* that matters. The payoff is delivered explicitly two lessons later, in aura-11:

> "Swing points that have sequential or SMT within them have a higher chance of holding compared to sweet points that don't." (aura-11)

This is the load-bearing rule that connects swing points to everything downstream: **not all swing points are equal.** A swing point confirmed by SMT divergence across the triad is treated as structurally significant; one without it is weaker and more likely to be swept/invalidated. In aura-11, dOoMeR uses this rule to decide *which* swing points are valid anchors for a range's extremes (see [[concepts/aura/ranges]] §"Refinement via SMT-Qualified Anchors"). The mechanics of Sequential SMT itself (what qualifies as "sequential," how the indicator detects it) are covered in [[concepts/aura/sequential-smt]] — not here.

### Worked example of SMT at a swing point (aura-06)

dOoMeR walks through a live example: at a given swing point, "candle 2 failed to take out or candle 3 failed to take out the high" on NQ, "however, on YM, it took it out." This divergence — one asset in the triad fails to make the corresponding high/low while a correlated asset does — is what qualifies that swing point as an SMT swing point. He then works backward through several more swing points asking "was there SMT? No. What about here? No" — establishing that SMT swing points are the exception, not the norm, at any given moment (aura-06).

## Homework / Drilling Method

The assigned drill, verbatim in substance (aura-06):

1. On the **daily, 4-hour, and 1-hour** charts (two timeframes minimum, all three preferred), use the circle tool to highlight **at least 50 swing points** — highs and lows, nothing else yet.
2. Second pass: go back through each of those 50 swing points and check, across the triad, whether SMT occurred there. Recolor/relabel swing points that had SMT vs. those that didn't.
3. Goal is repetition-driven pattern recognition — dOoMeR frames this as reframing groundwork for a later lesson (the SMT-qualification rule above, delivered in aura-11), not a one-off exercise.

This same "mark 50, then refine" two-pass homework structure recurs for ranges (aura-08: "mark out ranges... at least 50") and is explicitly revisited/upgraded in aura-11 ("just expanding on and refining the ranges that you had marked out for last week's homework").

## See Also

- [[concepts/aura/ranges]] — ranges are anchored on swing points, refined further by SMT qualification
- [[concepts/aura/sequential-smt]] — the mechanics of Sequential SMT referenced here as the qualification signal
- [[entities/people/doomer]]
- [[concepts/aura/README]]
