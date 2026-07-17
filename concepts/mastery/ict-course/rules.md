---
tags: [mastery, ict-course, rules, execution, neurospect]
aliases: [ICT Rules, MrWitness-AXL Rulebook, ICT Course Rules]
sources: [concepts/course/module-1-foundations/01-what-moves-the-market.md, concepts/course/module-1-foundations/02-fair-value-gaps.md, concepts/course/module-2-price-delivery/01-four-stages-apd.md, concepts/course/module-2-price-delivery/04-reversals.md, concepts/course/module-3-session-and-bias/01-power-of-three.md, concepts/course/module-3-session-and-bias/02-session-kill-zones.md, concepts/course/module-3-session-and-bias/03-deviations.md, concepts/course/module-3-session-and-bias/04-daily-bias.md, concepts/course/module-4-market-structure/01-swing-classification.md, concepts/course/module-4-market-structure/04-model-2022-ote-csd.md, concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow.md, concepts/business-logic/ict-entry-models.md, concepts/business-logic/ict-live-commentary.md]
created: 2026-07-17
updated: 2026-07-17
---

# ICT Course (MrWitness-AXL) — The Rules

The MrWitness-AXL model stated as one **executable rulebook**, aggregating rules that are today
**scattered across 16 lessons** under inconsistent headings (`## Rules` in some, `Key Rules` /
`Closing Basis Rules` / `The Rule` / `Daily Checklist` / `Full Sequence` in others, and absent
entirely in several). This page **normalizes** them into one cited list — it does **not** re-explain the
mechanics (follow the link on each block for the *why*) and it does **not** fork the per-strategy
execution specs.

> **No-drift / canonical-doc rule** ([[CLAUDE]] §Architecture Doc Integrity). Two things are canonical
> elsewhere and are **linked, never restated** here:
> - The **learner-facing lesson pages** (`concepts/course/*`) are canonical for concept + worked example.
> - The **entry-model YAML** (`concepts/entry-models/*`, the `# --- MACHINE_READABLE_STRATEGY ---`
>   blocks) is canonical for per-strategy `conditions:`/`checklist:` — it is **consumed by the AI coach**.
>   This page points at each model's checklist; it does **not** copy the checklist items.

> **The one-line model.** Read the **HTF FVG bias** and where price sits vs. the **opening price** →
> identify the **draw on liquidity** (the swing high/low price is reaching for) → wait for the **kill
> zone** and the **four stages** to deliver price into **discount/premium** → take the entry the active
> **model** (consolidation / E&R / reversal / London / Model 2022+OTE / SMT) specifies off a **PDA**,
> confirmed on the **entry timeframe** → target **liquidity + one deviation beyond it**. See
> [[concepts/course/README]] for the module order and [[concepts/entry-models/README]] §"Minimum
> Confluence" for the five gates every trade must clear.

---

## A. Foundations — liquidity & inefficiency (Module 1 · Vol 1 Class 1)

### A1 — Liquidity is the target ([[concepts/course/module-1-foundations/01-what-moves-the-market]])
1. **Above swing highs = buy-side liquidity (BSL); below swing lows = sell-side liquidity (SSL).** These
   pools are the daily targets — price moves *to* liquidity. **[R1]**
2. A swing is exactly **three candles**; mark **candle 2's single price level**, not a zone. One tick
   beyond the high/low is enough to collect the stops. **[R2]**
3. Mark the swing highs/lows for the **draw on liquidity (DOL)** on **1H and 15M**; find the entry on
   **5M–1M**. **[R3]**

### A2 — Inefficiency is the entry ([[concepts/course/module-1-foundations/02-fair-value-gaps]])
4. A **fair value gap (FVG)** is a **three-candle pattern only** — mark candle 1's extreme to candle 3's
   extreme. An FVG **requires displacement**; a slow-moving range does **not** create a valid FVG. **[R4]**
5. When bullish look for a **BISI**; when bearish a **SIBI**. The FVG must point in the **DOL direction**. **[R5]**
6. **Enter into candle 3's area** (the top edge of a bullish FVG), not the midpoint. Price only needs to
   **dip into** the FVG — it need not fully fill it. **Stop below candle 1** of the FVG. **[R6]**
7. **IOFED (highest-probability):** if price returns to the gap but does **not** close below its CE (50%),
   that is the highest-probability entry. If price **skips** the FVG entirely (**BAG**) → do not wait for
   a fill, look for the next opportunity. **[R7]**
8. A bearish FVG that price **closes above becomes a bullish** entry zone (**inversion FVG**). On multiple
   FVGs in one displacement, enter the **first** and allow stop for the second. **[R8]**

---

## B. Price delivery — the four stages (Module 2 · Vol 1 Classes 2–4)

### B1 — The four stages ([[concepts/course/module-2-price-delivery/01-four-stages-apd]])
9. The four stages are **sequential: Consolidation → Expansion → Retracement → (Expansion or
   Reversal)**. Every price run is structured by them; do not skip Stage 1. **[R9]**
10. A **real retracement does both jobs**: fills the inefficiency **AND** reaches **discount (≤ 50%)**. If
    only the inefficiency is filled (not discount) → **fake retracement** → expect continuation. **[R10]**
11. **Never chase expansion in premium** — wait for the retracement into discount. If price skips the
    retracement (BPR conditions), do not chase; wait for the next opportunity. **[R11]**
12. **Two read-checks** (self-diagnostics, [[concepts/course/module-2-price-delivery/01-four-stages-apd]]):
    "a Retracement that becomes a Reversal was **not** a Retracement"; "a Consolidation that becomes a
    Reversal was **not** a Consolidation." If either fires, re-read the structure. **[R12]**

### B2 — Consolidation & Expansion-Retracement (the two continuation models)
13. **Consolidation model** — trade the return to the range **EQ (50%)** off a **PDA at or below EQ**,
    after an intra-range sweep. Bodies define the range, **not wicks**. Execution spec is canonical in the
    entry-model YAML → [[concepts/entry-models/consolidation-model]] (checklist consumed by the AI coach —
    follow it there, do not re-key it). Lesson: [[concepts/course/module-2-price-delivery/02-consolidation-model]]. **[R13]**
14. **Expansion & Retracement model** — after an expansion leg, enter a **FVG/OB at or below the 50%** of
    that leg once price is in discount (not a fake retracement). Spec:
    [[concepts/entry-models/expansion-retracement-model]]; lesson:
    [[concepts/course/module-2-price-delivery/03-expansion-retracement]]. **[R14]**

### B3 — Reversals ([[concepts/course/module-2-price-delivery/04-reversals]])
15. **Always target the origin swing** — a *true* reversal must reach it. If price does not take out the
    origin swing, it was a **retracement**, not a reversal. **[R15]**
16. **Failure swings (type 1) are more likely under HRLR** — high-resistance / choppy / news-week
    conditions raise the odds of a failed reversal. **[R16]**
17. **Always take partials at rejection blocks** — you cannot know in real time whether you are in a
    type-1 failure swing or a continuation, so partials are the rule, not the exception. **[R17]**
18. **Best-probability reversals happen at layered liquidity pools** (multiple stacked highs/lows at one
    price). **Accumulation looks like consolidation but sits at extremes** — use HTF (weekly/daily) context
    to distinguish. Execution spec: [[concepts/entry-models/reversal-raid-on-stops]]. **[R18]**

---

## C. Session context & bias (Module 3 · Vol 2 Classes 1–4)

### C1 — Power of Three / AMD ([[concepts/course/module-3-session-and-bias/01-power-of-three]])
19. **Narrative first, pattern second** — a textbook AMD on the wrong narrative still fails. **[R19]**
20. **The manipulation leg is the wick**; the body above the open is distribution (where you exit, not
    enter). On a **bullish day, below the open is the buy zone** — the further below all three AM opens
    (midnight / 8:30 / 9:30), the higher the probability. **[R20]**
21. **The daily (midnight) open is the most important**; for an intraday entry the relevant open depends on
    the session traded. You get **four chances a day** (one per session open) — missing one is not the end
    of the day. **[R21]**

### C2 — Kill zones ([[concepts/course/module-3-session-and-bias/02-session-kill-zones]])
22. **The kill-zone edge, stated once:** during a KZ, on a **bullish day** if price is **below** the
    relevant opening price → look for longs back through and away from it; on a **bearish day** if price is
    **above** it → look for shorts. Each KZ anchors to one opening price = one AMD cycle. The four windows
    (Asia 8PM–12AM, London 2–5AM, NY AM 8:30–11:30, NY PM 1:30–4:00) are canonical in
    [[concepts/business-logic/ict-entry-models]] §Kill Zone Context — reference, don't re-list. **[R22]**

### C3 — Deviations ([[concepts/course/module-3-session-and-bias/03-deviations]])
23. **Do not exit at the obvious liquidity level** (the swing high/low itself). Always aim for **at least
    one deviation beyond it** as the first partial. Anchor the deviation Fibonacci from the correct
    manipulation swings; watch for **HPDL** alignment (deviation + daily FVG). **[R23]**

### C4 — Daily bias ([[concepts/course/module-3-session-and-bias/04-daily-bias]])
24. **Bias = the 4H FVG you are inside + opening-price position.** State it in one sentence *before* the
    session: "I am inside a [bullish/bearish] 4H FVG; the target is [level]." If no FVG, use the nearest
    external liquidity. The lesson's `## Daily Checklist` is the canonical evening/pre-session routine —
    run it from [[concepts/course/module-3-session-and-bias/04-daily-bias]], reconciled with §F below. **[R24]**
25. **Stand aside when bias is overridden** (canonical list in the YAML `stand_aside_conditions:` →
    [[concepts/entry-models/daily-bias-model]]): among them — 4H FVG violated; price above all three AM
    opens on a bull day (distributing) / below on a bear day (accumulating); **Thursday pre-NFP**; CPI-week
    Monday; small ORG with no HRLR entry model. **[R25]**

---

## D. Market structure (Module 4 · Vol 3 Classes 2, 4, 5)

### D1 — Swing classification & fractality ([[concepts/course/module-4-market-structure/01-swing-classification]], [[concepts/course/module-4-market-structure/02-fractality]])
26. **A swing is promoted by its price leg, not its size.** STH/STL = a raw 3-candle swing (unqualified,
    "suspect"). It becomes **ITH/ITL** only when its price leg **creates or fills an FVG**. An ITH/ITL
    becomes **LTH/LTL** once a later move takes it out. The protected level in a trade is the **ITL/ITH**.
    (Canonical detail: [[concepts/business-logic/ict-market-structure]].) **[R26]**
27. **The tradeable fractal is STL → ITL → STL → MSS** (mirror for shorts). Structure is fractal: the same
    three-swing pattern nests on smaller timeframes inside the same move — but fractality does **not** mean
    "any timeframe is equal"; HTF structure sets the context LTF structure delivers within. **[R27]**

### D2 — Structure deviations ([[concepts/course/module-4-market-structure/03-structure-deviations]])
28. **Two-set anchoring:** anchor deviation targets from the **structural** swing set (the ITL→expansion
    move), not only the session sweep — it projects where price is *actually* drawn after an MSS. (Lesson
    has a step-by-step procedure and no separate rule list — this is the operative rule.) **[R28]**

### D3 — Model 2022 + OTE + CSD ([[concepts/course/module-4-market-structure/04-model-2022-ote-csd]])
29. **When there is no 50% retracement after the MSS, Model 2022 is active** → wait for the **OTE zone
    (62–79%)**. If price *does* retrace to 50%, use the standard E&R entry instead (the lesson's `## Full
    Sequence` diagnostic). **[R29]**
30. **Selecting the OTE block** (three lesson rules, in priority): **(1) highest down-close body wins**;
    **(2) prefer the propulsion block** (a second OB nested inside the first); **(3) prefer an OB in concert
    with the 0.705** Fibonacci level. **[R30]**
31. **CSD is the pre-MSS early trigger:** in the OTE zone, when the **opening price of the down-close
    candles is breached**, that change-in-state-of-delivery is the entry (optionally wait for the full OTE
    block tap if CSD is unclear). **Stop below the OTE block closing price**; target first deviation above
    the initiating high, runner to the −2/−2.5 convergence. Full execution spec:
    [[concepts/entry-models/model-2022-ote]]. **[R31]**

---

## E. Order flow & SMT (Module 5 · Vol 4 Classes 1–2)

### E1 — Order flow on a closing basis ([[concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow]])
32. **Order flow is read on a *closing* basis, not wicks.** Bullish order flow is confirmed when: down-close
    candles (bullish OBs) are **supported** (bodies close above them on return); bearish FVGs above are left
    **unfilled** (LRLR); retracements make **lower highs** with bodies closing higher; bodies do not close
    below key levels. Mirror the four for bearish (up-close candles respected as resistance, etc.). **[R32]**
33. **Order flow has broken when the opposing candles stop being respected** — e.g. bullish order flow is
    gone once up-close candles no longer act as resistance / bodies close above previously-respected bearish
    PDAs / FVGs above start filling. When it breaks, **step aside**. **[R33]**

### E2 — SMT divergence ([[concepts/course/module-5-order-flow-and-smt/02-smt-divergence]])
34. **SMT is a confluence filter, not a standalone signal** — at the **manipulation leg** of Power of
    Three, check the triad (**NQ / ES / YM**); **cracking correlation** (one index makes the extreme, the
    others don't) confirms the reversal. Use fresh front-month contracts. Execution spec:
    [[concepts/entry-models/smt-confirmation-entry]]; reference KB: [[concepts/business-logic/ict-smt]]. **[R34]**

---

## F. Execution discipline & routine (reconciled — one home for two scattered loci)

This section is the **single reconciled home** for the two extra checklist/routine loci that previously
sat apart from the lessons. It **links** to them and states the operative rules; the pre-trade *gating*
checklist itself stays canonical where the AI coach and the KB expect it.

### F1 — The universal entry gate
35. Before any model-specific trigger, the **five minimum-confluence gates** must all pass (canonical:
    [[concepts/entry-models/README]] §"Minimum Confluence" — HTF FVG bias · opening-price aligned · kill
    zone active · PDA in discount/premium · entry-TF confirmation). This **subsumes** the 7-point
    `## Entry Checklist` in [[concepts/business-logic/ict-entry-models]] — treat the entry-models/README
    five as the live gate and the KB's seven as its longer-form reference. Do **not** maintain a third
    competing copy. **[R35]**

### F2 — Pre-market routine ([[concepts/business-logic/ict-live-commentary]] §Pre-Market Opening Routine)
36. **Run the MrWitness pre-market routine before price moves:** mark opening prices (midnight / 8:30 /
    9:30 / prior-RTH settlement) + weekly 50% + visible HTF FVGs → identify the DOL (nearest 1H/15M BSL &
    SSL) → **state the bias explicitly** in one sentence with a reason → give the **two-scenario framework**
    ("if they take X first I want Y; if instead Z, the approach changes") → **declare the expected
    HOD/LOD** in advance. This is the same content as the Daily-Bias `## Daily Checklist` (R24) at the
    session-open altitude — run one, not two divergent copies. **[R36]**

### F3 — Live trading discipline ([[concepts/business-logic/ict-live-commentary]] §Live Trading Discipline (AXL))
37. **Daily loss limit is absolute:** accounts ≥ $10K → **$1,000/day** max; accounts < $10K → **$500/day**;
    hit it → **log out, return tomorrow**. **[R37]**
38. **Set and forget** — only ever close at **(1) break-even, (2) planned partials, (3) take profit**.
    Never manually close outside those three, even when price action looks messy. **[R38]**
39. **No chasing expansions** — "if you see an expansion without a good opportunity, you're going to lose."
    If price leaves without you, let it go; another setup forms. **[R39]**
40. **The three requirements to win (AXL), in order:** ① good psychology (impulse control under pressure),
    ② rules (loss limit, set-and-forget, no chasing), ③ a backtested model — *"the model doesn't matter if
    you don't have psychology and rules."* **[R40]**
41. **Recognize and respect bad conditions** — AXL's "today is not conditions for trades" means stay out;
    choppy action-to-reaction (accumulation) = do not trade; **pre-11AM Thursday (pre-NFP) is off-limits
    regardless of setup quality**. **[R41]**

---

## Relationship to the Aura track (do not merge here)

This rulebook is the **MrWitness-AXL (ICT)** track. The **Aura (dOoMeR)** track has its own rulebook at
[[concepts/mastery/aura/rules]]. The two use **deliberately different vocabularies** (ICT uses order
blocks, OTE, breakers, quadrants; Aura rejects those in favour of ranges + gaps + Sequential SMT — see
[[concepts/entry-models/README]] §Aura). They are **not reconciled here** — the unified playbook is the
**deferred Phase 3** deep-research workstream (see [[concepts/mastery/README]]). Keep ICT vocabulary in
this track and Aura vocabulary in that one.

## Open flags (do not silently resolve)

- **Rules absent in several lessons** — M2.2/M2.3 (consolidation, E&R) carry their rules in the entry-model
  YAML, not the lesson; M4.2/M4.3 (fractality, structure-deviations) state rules only inline. Where a
  lesson had no rule list, the operative rule above is drawn from the lesson body and flagged in its cite.
- **Two routine loci overlap** — the Daily-Bias `## Daily Checklist` (R24) and the pre-market routine (R36)
  are the same routine at slightly different altitudes; run one. Flagged, not deleted, pending a session
  that folds them into a single canonical routine page.
- **`name:` vs `strategy_name:`** — four entry-model YAML blocks use `strategy_name:` (Model 2022, Daily
  Bias, SMT) rather than `name:`; noted so the AI-coach loader keys on the right field.

## See Also

- [[concepts/mastery/ict-course/exercises]] — the drills that build each rule to Can-mark/Backtested
- [[concepts/mastery/ict-course/tracker]] — log ladder stage / confidence / reps per lesson & model
- [[concepts/mastery/README]] — the mastery ladder + Readiness-to-Live Gate
- [[concepts/course/README]] — the learner-facing curriculum (the "learning path" for this track)
- [[concepts/entry-models/README]] — canonical per-strategy checklists (linked, never forked)
- [[concepts/mastery/aura/rules]] — the parallel Aura rulebook (not merged; Phase 3)
