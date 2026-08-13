---
tags: [mastery, aura, rules, execution, neurospect]
aliases: [Aura Rules, Aura Model Rules, Sequential-SMT Rulebook]
sources: [concepts/aura/swing-points.md, concepts/aura/ranges.md, concepts/aura/gaps.md, concepts/aura/triads-asset-selection.md, concepts/aura/aura-asset.md, concepts/aura/sequential-smt.md, concepts/aura/htf-ltf-application.md, concepts/aura/risk-management.md, concepts/aura/journaling-system.md, concepts/aura/discipline-systems.md, concepts/aura/mind-and-emotional-control.md]
created: 2026-07-17
updated: 2026-07-17
---

# Aura Model — The Rules

The Aura (dOoMeR) Sequential-SMT model stated as an **executable rulebook**. This page distils the rules
already documented, with rationale, across `concepts/aura/*` — it does **not** re-explain the mechanics
(follow the link on each block for the *why*). Every rule cites the concept page and the `aura-NN` source
it comes from. Where dOoMeR states a rule as a preference or flags his own uncertainty, that is preserved
(marked *soft* / *flagged*), not hardened into a false certainty.

> **The one-line model.** Mark **swing points** → the significant ones define **ranges** → price seeks
> **gaps (and the liquidity within them)** inside a range's discount/premium → trust a level only when
> **Sequential SMT** confirms it across nested time cycles on a **correlated triad + the Aura Asset (6S)**
> → cascade **HTF→LTF** to a 5-minute **inverse-FVG** entry → manage risk as it **evolves**. See
> [[concepts/aura/gaps]] for dOoMeR's own compact summary ("ranges, gaps, what lies within, liquidity,
> highs and lows, swing points").

---

## A. Structural primitives

### A1 — Swing points ([[concepts/aura/swing-points]], aura-06/11)
1. A swing point is the **3-candle pivot** (candle 2 is the pivot: lower-low-then-higher-low for a swing
   low; the mirror for a swing high).
2. Swing points are **fractal** — identical across all timeframes; the mechanics don't change by TF.
3. **Not all swing points are equal.** A swing point **confirmed by SMT** across the triad holds more
   reliably; one without SMT is weak and more likely to be swept. This is the load-bearing filter for
   everything downstream — treat unqualified swings as provisional.

### A2 — Ranges ([[concepts/aura/ranges]], aura-08/11)
4. A range is the territory between a swing high and a swing low, identified by the **expansive-move
   method** (find the largest expansive move between two swing points — that move *is* the range). Do
   **not** use time-based ranges.
5. Reference zones inside a range are **discount / equilibrium / premium** only — **no quadrants**
   (0.25/0.75) in this model. *(Divergence from the ICT order-flow page, which does use quadrants — flagged
   in [[concepts/business-logic/ict-liquidity]].)*
6. A range is **invalidated only by a candle close** beyond its boundary — a wick through is not a break.
7. **New-range trigger:** a HTF **Sequential SMT** event **plus an expansive move away** anchors a new
   range at that swing point. Keep following the current range until either an **opposing** Sequential SMT
   or **another same-cycle** Sequential SMT forms.
8. **Anchor extremes only on SMT-qualified HTF swing points** (rule 3). If a swing looks false across the
   triad and there's a large gap between candidates, prefer the low/high **actually swept on all triad
   assets**, even if it isn't the most extreme candidate.
9. If the range isn't obvious, **zoom out** until it is (most-recent obvious low + most-prominent obvious
   high). Overlapping/ambiguous ranges are acceptable — do not force one canonical range. *(soft)*
10. This model **does not use "order block" terminology** — what others call an order block is just price
    returning to a range's discount/premium.

### A3 — Gaps and "what lies within" ([[concepts/aura/gaps]], aura-09)
11. Only four gap types matter: **FVG, iFVG, NWOG, NDOG**. No BPR / volume-imbalance vocabulary here.
12. Price is drawn to **gaps within a range's discount/premium**, and specifically to the **liquidity
    (a swing high/low) nested *inside* the gap** — that internal level is the precise target, not the gap
    boundary.
13. **If no internal liquidity is visible:** *look left* (a resting untaken level at similar price) or
    *zoom in* (a lower-TF swing usually appears inside the same gap).
14. **Confluence stacks additively:** overlapping gaps (e.g. NWOG × FVG), liquidity-left + liquidity-inside,
    and near-equilibrium gaps all raise a gap's probability as a target.

---

## B. The confirmation engine

### B1 — Triads & the Aura Asset ([[concepts/aura/triads-asset-selection]] aura-10, [[concepts/aura/aura-asset]] aura-15)
15. Run divergence on a **correlated triad** selected math-first: **Pearson correlation on daily returns**,
    ~2–3yr window; keep assets in the **sweet spot** (correlated enough that agreement is expected,
    independent enough that a divergence carries information). **Chart behaviour overrides the number** when
    they disagree.
16. The five triads: **Indices** ES/NQ/YM · **Metals** Gold/Silver/Platinum (Copper as extra check) ·
    **Forex** 6E/6B/6J (6A alt) · **Energy** CL/HeatingOil/Gasoline *(least reliable — trade sparingly)* ·
    **Crypto** BTC/ETH/SOL.
17. Add the **Aura Asset = Swiss Franc futures (6S)** as a 4th leg to **every** triad — a time-synchronized
    dollar-proxy (chosen over DXY because DXY's candles aren't sync'd to the traded futures). Read it
    **exactly like a normal divergence leg** (weekly/daily/session cycle). Most respected on indices, metals,
    forex; weakest on energy. Its *origin story* is dOoMeR's admitted speculation — the *chart behaviour* is
    the justification. *(flagged)*

### B2 — Sequential SMT ([[concepts/aura/sequential-smt]], aura-07/11/12/14)
18. **Sequential SMT** = ordinary SMT (cracking correlation across the triad) that shows up **nested across
    ≥2 adjacent time cycles** (e.g. weekly-cycle SMT with daily-cycle SMT inside it). Cross-cycle alignment
    is what precedes large expansive moves.
19. It is **probabilistic, not guaranteed** — the edge is "happens a high % of the time," made tradeable by
    precise risk management. Never treat a signal as certain.
20. **Confirm a Sequential SMT** by any of: (a) cross-cycle nesting; (b) **gap/SMT-fill** — one triad asset
    retraces into a shared gap while another doesn't; (c) **candle-level** — the swing candle also makes SMT
    vs. the immediately prior candle on that TF; (d) **Sequential Skip** (B3).
21. **Cross-cycle gap-pairing** for confirmation: weekly-cycle → check daily gaps; daily/session → 4H gaps;
    micro → 15m–1H gaps.
22. **Extreme-of-the-range targeting:** if SMT occurred *between* two segments of a larger cycle, expect the
    **extreme of that larger segment** to eventually be taken. "This goes for all cycles."
23. The indicator displays **only currently-valid** Sequential SMTs (invalidated ones disappear) — always
    read the current state, never a stale signal. *(Stage-2 drills still mark by hand — see [[concepts/mastery/aura/exercises]].)*

### B3 — Sequential Skip ([[concepts/aura/sequential-smt]] §Sequential Skip, aura-14)
24. When a HTF Sequential SMT forms but the **immediately adjacent** lower cycle does **not** confirm it, a
    cycle **further down** can confirm it directly, "skipping" the missing link. Fractal — works at any cycle
    pair.
25. **Cross-asset variant:** if the day's bias is set but the primary asset doesn't offer a clean entry (e.g.
    NQ gapped too far to chase), take the **same setup on another triad member** moving in the bias direction
    — same confirmation criteria (candle SMT + iFVG), only the asset changes.
26. This pre-planning (HTF context, premium/discount position, prior liquidity taken) is done in **post-/pre-
    market review**, not improvised live.

---

## C. Execution (framing → entry → management → exit)

### C1 — HTF→LTF cascade ([[concepts/aura/htf-ltf-application]], aura-17)
27. Analyse as an **if-then chain, top-down**, to remove impulse ("think like a machine"). Each cycle points
    to the next: Quadrennial→Yearly/Quarterly → … → Monthly→Weekly *(prefer confirming Monthly with Weekly)*
    → Weekly→Daily/Session → Daily/Session→4H → 4H→**15m→5m (preferred) / 3m**. 5m is preferred over 3m
    because 3m setups fail more often.
28. **HTF divergence dominates LTF** — higher-TF candles aggregate more data/volume/news, so their
    divergences carry more weight. A 1-minute microcycle divergence is low-influence; don't expect a big
    expansive move from one.
29. **Before every trade, define BOTH what confirms and what invalidates the bias.** The framework supplies
    the next question to ask; it is not a licence to guess. If the expected trigger **fails to appear**, treat
    its absence as invalidation — zoom out and re-read, don't keep waiting.

### C2 — Entry ([[concepts/aura/sequential-smt]] §Confirming, aura-12/14/17)
30. **Preferred entry: a 5-minute inverse FVG (iFVG)** in the confirmed direction; a plain FVG is the
    fallback. Preferably wait for a **session-cycle Sequential SMT within discount** (long) / premium (short)
    of the LTF range before entering — fewer signals, higher quality, more misses (needs disciplined risk).
31. On Sequential-Skip / news-open setups, **prefer waiting for the 9:30 NY open** rather than entering off a
    pre-9:30 gap formation — especially if consistency is still developing; a pre-9:30 setup can run away
    without a precise entry, and chasing it out of urgency is the doorway to revenge trading. *(soft — stated
    for struggling traders in particular)*
32. **Premium/discount position sets the R:R ceiling:** entering while in premium of a range means targeting
    a *lower* R:R, since price may retrace to equilibrium and stop you before a larger target.

### C3 — Stops, targets, management ([[concepts/aura/htf-ltf-application]], [[concepts/aura/risk-management]], aura-13/17)
33. **Stop** goes at the level whose respect would **invalidate the trade** — the high/low of the qualifying
    daily-cycle / 4H SMT (or the recent swing). Initial *technical* stop placement is the swing-point method;
    see [[concepts/aura/swing-points]].
34. **Alternate-asset entry for stop size:** if a primary asset's stop distance is uncomfortably large, take
    the same idea on a correlated triad member with a tighter equivalent gap (e.g. YM instead of ES).
35. **Target = the extreme of the timeframe you're playing** (e.g. previous week's low if trading off the
    monthly/weekly). Price will **not** run cleanly to target — it builds new ranges/Sequential SMT along the
    way — so trailing and active management are expected, not a sign the model failed.
36. Take-profit (pre-Aura-Asset baseline): full TP at HTF-range equilibrium, **or** hold for liquidity in the
    HTF range's discount/extreme. More granular multi-level TP requires the Aura Asset.
37. **Time Sum (369) is optional and de-emphasized** — dOoMeR downplays it himself as a rare, subjective
    extra confluence. Do not build the model around it. *(flagged — see [[concepts/aura/time-sum]])*

---

## D. Risk rules (non-negotiable) ([[concepts/aura/risk-management]], aura-13)

38. **Protect capital first.** Order of operations: conserve capital → generate income → roll the account.
    Capital protection is decided **before** any trade.
39. **Per-trade risk: 1–2% of *total* capital** (broker + savings), Dante uses 2%. Not % of the broker
    balance. Keep ~10% at broker / 90% in savings (broker-failure protection). *(soft on the 10/90 split for a
    personal account; the % principle is firm.)*
40. **Daily stop: 2–3R.** Once hit, the day is over — no more setups, no matter how good they look.
41. **Drawdown circuit-breaker: stop completely at 10R drawdown** (≈20% at 2% risk) until a full investigation
    is done. Precommit this **in writing** before the drawdown starts.
42. **Never size up in a drawdown.** Sizing must go *down* — reduce risk/frequency or stop. If 10 straight
    losses would draw you down >20%, your per-trade risk is too high.
43. **Think in R, not dollars.** R = amount risked on one trade. Judge trades and the whole system in R.
44. **Expectancy is the number that matters:** `(win% × avg win R) − (loss% × avg loss R)`. Positive = an
    edge. **A win rate without its R:R is meaningless** (break-even win rate `= 1/(1+R:R)`).
45. **Risk evolves — recalculate from the current price/stop, not entry.** "Free trade" is a lie: moving to
    breakeven after price ran 19 of a 20-pip target means risking 19 to make 1. Rule of thumb: **maintain at
    least 1:1 from where price is now.** A loss taken while managing correctly is fine; a loss from a
    never-trailed static stop is the failure mode.
46. **Prop-challenge caution:** these firms profit from failure; their rules push overleverage. Usable but
    demand *more* self-imposed accountability. The honest path is a small verifiable real-account track record.

---

## E. Psychology & discipline rules ([[concepts/aura/discipline-systems]] aura-04, [[concepts/aura/mind-and-emotional-control]] aura-02/03, [[concepts/aura/journaling-system]] aura-05)

47. **Systems over willpower** — willpower depletes exactly when it's needed most; design routines/environment
    so the disciplined choice is the default.
48. **Pre-market, answer three questions or don't trade:** *What am I looking for? Where? What would make me
    stand aside?* Write the plan before price moves.
49. **Circuit breakers are absolute, precommitted, visible:** a two-loss (max) daily stop; the **10-minute
    rule** (close charts 10 min after any loss); a pre-trade checklist; the **zoom-out-after-loss** rule
    (re-assess HTF before re-entering).
50. **Trade the market, not your P&L.** Intervene *before the second (revenge) trade*, not after the third.
51. **Missing a trade is discipline, not a loss** — the market gives setups nearly every day; there is no
    single unrepeatable trade. Sit on your hands when there's nothing to do.
52. **Confidence is a byproduct of doing the work, not a prerequisite** — execute the edge regardless of feel;
    use **negative visualization** (pre-accept the loss) before entering.
53. **Journal every trade — including missed/canceled ones.** Recording ≠ analyzing; the journal exists to
    change behaviour. Run a **weekly review** on Dante's three questions (make more from winners / lose less
    on losers / generate more winning ideas). **Never miss twice** — one skip is an accident, two is a habit.
54. **Environment & health are performance inputs, not wellness extras:** phone out of the room / chats closed
    during sessions; 7h sleep + consistent wake time; morning light + movement; caffeine cutoff by noon (NY
    session). *(soft — dOoMeR relaxes specifics; the principle is firm.)*

---

## Divergences & open flags (do not silently resolve)

- **Quadrants:** Aura uses discount/EQ/premium only; the ICT order-flow model uses 0.25/0.75 quadrants
  (rule 5).
- **"Order block":** Aura rejects the term (rule 10) where the ICT entry-models library uses it heavily.
- **Time Sum (369):** de-emphasized by dOoMeR himself (rule 37) — not load-bearing.
- **Firm vs personal stop-trailing:** dOoMeR trails tightly on firm capital but admits his personal account
  is looser; he doesn't say which standard students should hold. Treat the **firm standard** as the target.
- **Unrecoverable specifics** (non-blocking, flagged in the concept pages): the originating-mentor name
  ("DA"), the garbled pip-by-pip trailing sequence in aura-13, "cup filling", the energy-triad "war" reference.

## See Also

- [[concepts/mastery/aura/checklist]] — these rules turned into a step-by-step execution checklist
- [[concepts/mastery/aura/tradezella-rule-mapping]] — these rules as Tradezella Playbook rows (per-rule
  follow rate + expectancy). ⚠️ **R23 cannot be reproduced there** — Tradezella's backtest chart takes no
  custom indicators, so every SMT read in a backtest is a hand read; see
  [[concepts/mastery/aura/chart-markup]] §The probe
- [[concepts/mastery/aura/learning-path]] · [[concepts/mastery/aura/exercises]] · [[concepts/mastery/aura/tracker]]
- [[concepts/mastery/README]] — the mastery model + readiness gate
- [[concepts/aura/README]] — the concept KB every rule here links back to
