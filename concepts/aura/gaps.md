---
tags: [concept, aura, neurospect]
aliases: [Aura Gaps, What Lies Within, Liquidity Within the Gap]
sources: [sources/neurospect/aura/aura-09-gaps-what-lies-within.md]
created: 2026-07-16
updated: 2026-07-16
---

# Aura Gaps — "What Lies Within"

The third structural primitive in dOoMeR's framework, after swing points and ranges. His core thesis: price is attracted not only to the premium/discount of a range, but specifically to **gaps sitting within that premium/discount** — and within those gaps, to whatever liquidity (a swing high or low) is nested inside them. He calls this "what lies within" the gap (aura-09).

## Which Gaps He Uses

dOoMeR names exactly four gap types, all standard ICT/SMC PDA terminology adopted as-is (not proprietary Aura vocabulary):

1. **Fair value gap (FVG)**
2. **Inverse fair value gap (iFVG)**
3. **New week opening gap (NWOG)**
4. **New day opening gap (NDOG)**

> "The only gaps I care about are... fair value gaps, inverse fair value gaps, or new week opening gaps and new day opening gaps." (aura-09)

No other gap type (e.g. Balanced Price Range, Volume Imbalance) is mentioned in this lesson.

## The Core Thesis

Building directly on [[concepts/aura/ranges]], dOoMeR's point is that "premium and discount" alone is not precise enough — within a range's discount (or premium), price is further drawn to specific gaps, and within those gaps, to specific liquidity:

> "If you studied the ranges from yesterday's homework, you might have noticed that price likes to go into premium discount. Yes, but also it likes to go to gaps within premium [and] discount." (aura-09)

## "What Lies Within": Liquidity Nested Inside a Gap

The central and repeated pattern in this lesson: a gap that contains a swing high or swing low *inside* its price range is a substantially higher-probability target than a gap alone. dOoMeR walks through roughly a dozen live chart examples across NQ, YM, and ES making the same point each time — a gap with a high or low resting inside it acts as a magnet, and price reliably reverses at that exact level once reached:

> "There is a gap here with liquidity within it and it was taken out. Price reversed at that level." (aura-09)

He frames this as something almost nobody else talks about, having found the pattern empirically from his own data: "This is one of the such important things that I don't hear anybody speak of. This was precisely from the data that I collected... where did price go and looking left at precise levels" (aura-09).

## Method: Finding Liquidity Within a Gap

Step-by-step, as demonstrated repeatedly across the lesson (aura-09):

1. Mark the current range (per [[concepts/aura/ranges]]).
2. Identify gaps sitting within the discount (for a short bias) or premium (for a long bias) of that range.
3. Look **inside** the gap's price range for a swing high or swing low — this nested liquidity is the precise target, more precise than the gap boundary alone.
4. **If no liquidity is visible inside the gap:** apply one of two fallbacks —
   - **Look left** — check for a resting level (an untaken high/low) at a similar price to the left on the chart.
   - **Zoom in** — drop to a lower timeframe within the same gap; a swing point will usually appear that wasn't visible at the original timeframe.

> "If you can't find one, either look left or zoom in." (aura-09)

He states this pattern is fractal and universal: "this happens on all time frames everywhere... absolutely everywhere on all time frames on all assets" (aura-09) — the same fractality claim made for swing points and ranges.

## Confluence Stacking

Several factors increase a gap's probability as a target, and dOoMeR treats them as additive:

- **Overlapping gaps** — e.g. a NWOG or NDOG that overlaps with a FVG. Price still reliably goes to that level: "you have two overlapping gaps. Price still went to that level." (aura-09)
- **Liquidity to the left of the gap, on top of liquidity inside it** — "what might make this a higher probable target? We have gap between the candles[,] fair value gap[,] liquidity to the left of it." A gap with both internal liquidity and liquidity to its left is a stronger target than either alone.
- **Near-equilibrium gaps** — a gap sitting close to a range's equilibrium is still counted as valid even if it isn't a clean discount/premium tag, provided it is "very close" and the swing lows involved are close to each other.

## Entry and Target Implications

The practical trading application dOoMeR gives directly (aura-09):

- **Short bias:** target = discount of the current range, specifically any liquidity within a gap in that discount (or the gap itself if no discrete internal liquidity is found).
- **Long bias:** target = premium of the current range, specifically liquidity within a gap in that premium.
- He references that Squash SMT (a divergence check, detailed in [[concepts/aura/sequential-smt]]) "can help gauge your targets" alongside gap liquidity, but defers the full mechanics of trade framing to a later lesson (aura-12) — out of scope here.

### Patience rule

dOoMeR flags a specific failure mode: taking a premature scalp off a level that looks like a gap-liquidity reversal, without waiting for price to actually reach the deeper discount/premium target where the larger expansive move originates:

> "You may have taken a set up here because you think that it was hit this level and reversed... but where did the large expansive move come from after we went into discount? ...You need to stay patient and allow for price to develop." (aura-09)

Price not tagging a marked discount/premium level exactly is explicitly framed as acceptable — "price can reverse if it does not hit pre discount that is okay" — the discipline required is staying patient rather than forcing an early entry.

## dOoMeR's Own Summary of the Framework (Videos 6, 8, 9)

Near the end of this lesson, dOoMeR states his own compact summary of the entire technical framework covered so far, in his own words and ordering — swing points feed ranges, ranges feed gaps, gaps feed liquidity targets:

> "In the simplest form of price action, this is how I break it down to you. Ranges, gaps, what lies within[,] liquidity, highs and lows, swing points. The same thing you were doing on day one of marking out swing points... that helps you to find the range." (aura-09)

This is the clearest single statement in the corpus of how these three lessons (swing points → ranges → gaps) compose into one system.

## Homework

Go back to the ~50 ranges marked out in the prior lesson's homework (aura-08) and, within each range on NQ and YM, find liquidity to the left and to the right of any gaps present. If none is found in a given range, zoom in and refocus specifically on premium/discount rather than forcing a gap-liquidity read (aura-09).

## See Also

- [[concepts/aura/ranges]] — gaps are located specifically within a range's discount/premium
- [[concepts/aura/swing-points]] — the liquidity nested inside a gap is itself a swing high/low
- [[concepts/aura/sequential-smt]] — Squash SMT referenced here as a target-gauging tool, detailed on that page
- [[entities/people/doomer]]
- [[concepts/aura/README]]
