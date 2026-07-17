---
tags: [entry-models, library, neurospect]
aliases: [Entry Models Library, Strategy Library]
sources:
  - sources/neurospect/aura/aura-08-ranges.md
  - sources/neurospect/aura/aura-09-gaps-what-lies-within.md
  - sources/neurospect/aura/aura-11-ranges-and-sequential-smt.md
  - sources/neurospect/aura/aura-12-confirming-sequential-smt-and-framing-trades.md
  - sources/neurospect/aura/aura-15-aura-asset.md
created: 2026-04-22
updated: 2026-07-16
---

# Entry Models Library

One page per tradeable strategy. Each page contains: human-readable explanation, setup conditions, step-by-step checklist, timeframe requirements, stop/target logic, and a machine-readable YAML block at the bottom.

> **Prerequisite:** Complete all five course modules before using this library in live trading. The checklist items only make sense with the underlying concepts. See [[concepts/course/README]].

---

## Library Index

| Strategy | File | Core Trigger |
|----------|------|-------------|
| Consolidation Model | [[consolidation-model]] | Range EQ + PDA after intra-range sweep |
| Expansion & Retracement Model | [[expansion-retracement-model]] | FVG/OB in discount after expansion |
| Reversal — Raid on Stops | [[reversal-raid-on-stops]] | Liquidity sweep + immediate rejection |
| London Model | [[london-model]] | London takes Asia side, delivers to other |
| Model 2022 + OTE | [[model-2022-ote]] | MSS + deep OTE retracement (62–79%) |
| Daily Bias Model | [[daily-bias-model]] | HTF FVG + below/above opening price |
| SMT Confirmation Entry | [[smt-confirmation-entry]] | SMT divergence + PDA reversal |

---

## How to Use the Checklists

Every page ends with a `# --- MACHINE_READABLE_STRATEGY ---` YAML block. The checklist items are in priority order:

1. HTF bias and narrative items come first — if they fail, stop.
2. Structural items come second — these are the setup prerequisites.
3. Entry-timing items come last — these are your final trigger.

**Check them in order.** Don't skip to the entry items because the chart "looks good."

---

## Minimum Confluence (Universal)

Every strategy, regardless of specific conditions, requires:

- **HTF FVG bias confirmed** (4H or Daily is inside a bullish/bearish FVG, or targeting the nearest external liquidity)
- **Opening price position aligned** (below midnight/8:30 open for longs; above for shorts)
- **Kill zone active** at the time of entry
- **PDA in discount** (for longs: below 50% of the relevant expansion leg)
- **Entry on 1M or below** (a COS, CSD, or structural confirmation on the entry timeframe)

If any of these five are missing, do not take the trade regardless of how clean the specific model looks.

---

## Stop and Target Conventions

**Stop loss defaults:**
- FVG entry: below the three candles that create the gap (candle 1 of the FVG)
- OB entry: below the body low of the order block (bodies only, not wicks)
- OTE entry: below the OTE block low

**Target defaults:**
- First partial: opposite side of the range or the first deviation beyond the obvious liquidity level
- Runner: previous day high/low; -2 to -2.5 Fibonacci deviation from the manipulation swing

---

## Aura (dOoMeR) — A Parallel Entry Philosophy

**Attribution:** Aura (dOoMeR) is a second mentor corpus ingested into this wiki (see [[concepts/aura/README]]). Its entry philosophy runs in parallel to the MrWitness-AXL models above — it is not merged into a single checklist with them.

Aura frames every entry off two structural primitives — [[concepts/aura/ranges|ranges]] (discount/equilibrium/premium) and [[concepts/aura/gaps|gaps]] (specifically the liquidity resting *within* a gap in the range's discount/premium) — confirmed by [[concepts/aura/sequential-smt|Sequential SMT]], a fractal, cross-time-cycle divergence filter, rather than same-timeframe triad divergence alone. Every triad additionally carries a fourth divergence leg, the [[concepts/aura/aura-asset|Aura Asset]] (6S, Swiss Franc futures), used as a time-synchronized dollar reference. The full top-down application, cascading from quadrennial cycle down to a 5m entry trigger, is documented in [[concepts/aura/htf-ltf-application]].

> **Divergence:** Aura deliberately uses a narrower PDA vocabulary than this library. Ranges, gaps, and the liquidity nested within them are the only structural elements dOoMeR names — order blocks, breaker blocks, and OTE are explicitly rejected as unnecessary ("all I'm looking for are expansive moves," per [[concepts/aura/ranges]]). This contrasts with this library's richer PDA set (FVG, OB, OTE, breaker, rejection block, CSD, etc. — see [[concepts/business-logic/ict-entry-models]]). Noted here rather than reconciled — the two vocabularies are not merged.

See [[smt-confirmation-entry]] for the fully attributed, merged Sequential SMT entry mechanics (HTF cascade → iFVG entry → Sequential Skip fallback → cross-asset variant).

---

## See Also

- [[concepts/course/README]] — complete the course before using these checklists
- [[concepts/business-logic/ict-entry-models]] — reference KB for PDA mechanics
- [[concepts/business-logic/ict-narratives]] — bias and session context
- [[processes/distributed-workflow/active/ai-coach]] — the AI coach module that consumes these YAML blocks
- [[concepts/mastery/ict-course/tracker]] — the mastery layer's per-model backtest/readiness tracker (Stage 7 drills each of these checklists in bar-replay toward positive expectancy; it **links** to these YAML blocks, never forks them)
