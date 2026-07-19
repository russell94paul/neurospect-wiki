---
tags: [mastery, unified, playbook, neurospect, ict, aura, index]
aliases: [Unified Model, Unified Playbook, The Playbook]
created: 2026-07-17
updated: 2026-07-17
---

# The Unified Playbook

One principled model that reconciles the two ingested mentors — **MrWitness-AXL**
([[concepts/course/README|ICT-course]]) and **dOoMeR** ([[concepts/aura/README|Aura]]) — into a single
sequence a learner can actually follow. This fills the reserved "unified model" slot in
[[concepts/mastery/README]].

> **It is a reconciliation, not a mashup.** Every place the two mentors diverge has a *ruling* — supersede,
> coexist, or drop — with its justification and citation in [[concepts/mastery/unified/divergence-rulings]].
> This page is the playbook; that page is the reasoning behind it. Read the ruling (`R#`) whenever a step
> below cites one.

> **No-drift.** This page states the *sequence and the decisions*. It does **not** re-explain what each
> concept is — the canonical `ict-*`, `aura-*`, `course/*`, and `entry-models/*` pages own that, and every
> step links to them. If a concept page and this playbook ever disagree, the concept page wins.

## The core insight

The two models are not competing strategies — they are the **same ICT skeleton described at two altitudes**.
AXL teaches the *intraday execution mechanics* (four-stage delivery, killzones, PDA entries, PO3). Aura
teaches the *structural/probabilistic scaffolding* (cross-cycle SMT, correlation-validated triads,
psychology-first). Stacked, they cover each other's gaps. The playbook runs top-down through five layers.

```
Layer 0  PSYCHOLOGY & DISCIPLINE   ── the foundation everything else stands on
Layer 1  STRUCTURAL PRIMITIVES     ── read the chart: liquidity, ranges, swings, gaps, PO3
Layer 2  CONFIRMATION (SMT stack)  ── the nested SMT signal chain — the centrepiece
Layer 3  EXECUTION                 ── time filter → entry model → stop/target
Layer 4  RISK                      ── R-based sizing, daily stop, circuit-breaker
```

---

## Layer 0 — Psychology & discipline (foundation)

Ruling **R8** (psychology-first). Both mentors agree the model is the *last* of three requirements, behind
psychology and rules. Build this first and keep it running underneath every other layer.

- Mindset, emotional control, the "four killers", self-image → [[concepts/aura/mind-and-emotional-control]]
- Systems over goals; why traders fail → [[concepts/aura/psychology-foundations]]
- Pre/post-market routines + environment design → [[concepts/aura/discipline-systems]]
- Journaling every trade incl. misses; "never miss twice" → [[concepts/aura/journaling-system]]
- AXL's live-discipline expression (set-and-forget, no chasing, bad-conditions filter) → [[concepts/business-logic/ict-live-commentary]] §Live Trading Discipline

## Layer 1 — Structural primitives (read the chart)

The shared skeleton both mentors draw on. Read these in order to build the picture before looking for a trade.

1. **Liquidity & draw (DOL).** BSL/SSL, the two forces, where price is being drawn → [[concepts/business-logic/ict-liquidity]].
2. **Range & premium/discount.** Mark the dealing range; locate price vs. EQ. Use **discount/EQ/premium for
   bias**, **quadrants (0.25/0.75) only for target precision** — ruling **R3**. → [[concepts/aura/ranges]] · [[concepts/business-logic/ict-order-flow]] §Quadrants.
3. **Swing points — the double-qualified anchor.** The 3-candle pivot is shared. Grade every swing by ruling
   **R2**: FVG-qualified (AXL) *and* SMT-qualified (Aura) = top-tier anchor; one filter = second-tier; neither
   = ignore. → [[concepts/business-logic/ict-market-structure]] · [[concepts/aura/swing-points]].
4. **Gaps.** FVG / iFVG / NWOG / NDOG, plus Aura's "liquidity *within* the gap" refinement → [[concepts/aura/gaps]] · [[concepts/business-logic/ict-liquidity]] §Inefficiency.
5. **The delivery narrative (PO3 / four stages).** Consolidation → expansion → retracement → reversal;
   Accumulation-Manipulation-Distribution → [[concepts/business-logic/ict-narratives]] · [[concepts/course/module-2-price-delivery/01-four-stages-apd]].

## Layer 2 — Confirmation: the nested SMT stack ⭐

The centrepiece, and the reconciliation's key synthesis (ruling **R1**). SMT is used **twice, at two
altitudes**, and their agreement is the strongest signal in the model:

1. **Structural anchor (HTF):** run **Sequential SMT** across nested time cycles to decide which swings are
   load-bearing and where the range/bias is anchored → [[concepts/aura/sequential-smt]].
2. **Entry trigger (LTF):** at the manipulation leg you actually enter, use **same-timeframe triad SMT**
   (NQ/ES/YM) as confluence that the sweep is complete → [[concepts/business-logic/ict-smt]] §The Triad.
3. **Optional 4th leg:** add the **Aura Asset (6S)** as a dollar-proxy divergence tell — ruling **R7**
   (adopt the quantitative case; ignore the origin story) → [[concepts/aura/aura-asset]].
4. **Triad selection is validated, not guessed:** Pearson-correlation on daily returns → [[concepts/aura/triads-asset-selection]].

> **The confluence to wait for:** a same-TF triad SMT at the entry leg sitting *inside* a confirmed
> higher-cycle Sequential SMT pointing the same direction (R1). Fewer setups, far higher conviction.
> When the adjacent cycle link is missing, use **Sequential Skip** → [[concepts/aura/sequential-smt]].

## Layer 3 — Execution (time → entry → levels)

Once Layers 1–2 align, execute with the [[concepts/entry-models/README|entry-model library]]. Ruling **R4**:
**default to FVG/iFVG entries**; reach for the richer PDA set (OTE block, breaker, rejection block, CSD)
only when the setup specifically calls for it.

- **Time filter first.** Only take setups inside a valid session window; respect day-of-week probability
  (Tuesday highest, pre-NFP Thursday off-limits) → [[concepts/course/module-3-session-and-bias/02-session-kill-zones]] · [[concepts/business-logic/ict-live-commentary]] §day-of-week. *(Frontier time-refinements — ICT Macros, killzone micro-structure, Quarterly Theory — are in [[concepts/advanced/README]] and slot in here.)*
- **Entry models** (pick the one the structure matches):
  - Consolidation → [[concepts/entry-models/consolidation-model]]
  - Expansion/retracement → [[concepts/entry-models/expansion-retracement-model]]
  - Reversal / raid-on-stops → [[concepts/entry-models/reversal-raid-on-stops]]
  - London → [[concepts/entry-models/london-model]]
  - Model 2022 OTE (deep 62–79% retrace + CSD) → [[concepts/entry-models/model-2022-ote]]
  - Daily-bias prerequisite filter → [[concepts/entry-models/daily-bias-model]]
  - SMT-confirmation entry (the Layer-2 stack made executable) → [[concepts/entry-models/smt-confirmation-entry]]
- **Stop & target conventions** are canonical in each entry-model YAML — never fork them → [[concepts/entry-models/README]].

## Layer 4 — Risk

Ruling **R5**: the **R-multiple Blueprint supersedes** the fixed-dollar cap (which is just its prop-account
expression). Canonical numbers live on the risk page — do not restate them here:

- Per-trade 1–2% of total capital · daily stop 2–3R · 10R drawdown circuit-breaker · positive expectancy in R → [[concepts/aura/risk-management]].
- On a prop account with a fixed-dollar daily limit, convert the 2–3R daily stop into dollars and keep it
  at/under the firm cap (R5).
- Readiness to move from sim to live is gated on evidence → [[concepts/mastery/README]] §Readiness-to-Live Gate.

---

## One-glance decision flow

```
0. Am I in state to trade? (routine done, not tilted)         → else stop.       [Layer 0]
1. What is the draw on liquidity, and where is EQ?             → bias.            [Layer 1]
2. Is my anchor swing double-qualified (FVG + SMT)?            → conviction 0/1/2 [R2]
3. Higher-cycle Sequential SMT set the bias direction?         → structural yes.  [R1]
4. Same-TF triad SMT (± 6S) confirming at the entry leg?       → trigger yes.     [R1/R7]
5. Inside a valid time window on a tradeable day?              → else wait.       [Layer 3]
6. FVG/iFVG entry present at the level?                        → enter.           [R4]
7. Risk ≤1–2%, daily stop in R set, target mapped?             → size + execute.  [Layer 4]
```

Any "no" at 2–6 → no trade. The edge is in the *stack*, not any single signal.

## Status & provenance

- **ESTABLISHED** — Layers 0–4 are built entirely from the two ingested corpora + the canonical wiki pages
  they cite. The two *new confluences* (nested SMT stack R1; double-qualified swing R2) are labelled
  **EMERGING** — they are principled syntheses of established components, not separately corroborated claims.
- Frontier time-based and liquidity refinements that extend this playbook live in [[concepts/advanced/README]].

## See Also

- [[concepts/mastery/unified/learning-path]] — the graded, sequenced curriculum over this playbook (U0→U6)
- [[concepts/mastery/unified/tracker]] — the living per-concept progress grid (ladder / confidence / reps)
- [[concepts/mastery/unified/divergence-rulings]] — the reconciliation decisions (R1–R8) behind this playbook
- [[concepts/mastery/README]] — the mastery hub (ladder + Readiness-to-Live Gate)
- [[concepts/mastery/aura/rules]] · [[concepts/mastery/ict-course/rules]] — the two source rulebooks
- [[concepts/advanced/README]] — frontier ICT content that extends the execution/confirmation layers
- [[concepts/architecture/learning-platform]] — the Learning Platform app whose journal fields trace to this playbook
- [[entities/projects/neurospect]] — full project context
