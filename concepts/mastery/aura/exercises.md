---
tags: [mastery, aura, exercises, drills, backtesting, tape-reading, neurospect]
aliases: [Aura Drills, Aura Exercises, Aura Practice Library]
sources: [concepts/aura/swing-points.md, concepts/aura/ranges.md, concepts/aura/gaps.md, concepts/aura/sequential-smt.md, concepts/aura/triads-asset-selection.md, concepts/aura/aura-asset.md, concepts/aura/htf-ltf-application.md, concepts/aura/risk-management.md, concepts/aura/discipline-systems.md, concepts/aura/mind-and-emotional-control.md, concepts/aura/psychology-foundations.md, concepts/aura/journaling-system.md, concepts/aura/trade-reviews.md]
created: 2026-07-17
updated: 2026-07-30
---

# Aura Exercise Library

Every drill in the [[concepts/mastery/aura/learning-path]], in detail. Drills that involve marking/reading
structure have a **✋ hand-marking** variant (do this first — trains the eye) and a **🛠 tool-assisted**
variant (Sequential-SMT indicator / auto-ranges — for speed once the eye is trained). Rep targets come from
dOoMeR's own homework where he gave one; where he gave none, a target is proposed and flagged *(proposed)*.

Log each drill's reps / ladder stage / confidence in [[concepts/mastery/aura/tracker]].

**Tooling assumed:** TradingView bar-replay, the futures instruments (triads + 6S), and the Sequential-SMT
indicator (Paul has all three). The ✋ variants deliberately switch the indicator **off**.

---

## Stage 0 — Psychology & discipline (behavioural; no rep target)

- **D0-a — Routine & environment build** *(aura-04)*: write your *actual* daily routine (not aspirational);
  write a pre-market and post-market checklist; follow it the next day; implement **two** environment changes
  immediately (phone out of room, chat apps logged out on the trading PC, etc.). → [[concepts/aura/discipline-systems]]
- **D0-b — Identity & observer practice** *(aura-02)*: write your current trading identity + the identity to
  become + ≥3 first-person identity statements; run the week-long "there's the voice" observer practice.
  → [[concepts/aura/mind-and-emotional-control]]
- **D0-c — Circuit-breaker rules** *(aura-03)*: identify your dominant "four killer" with a specific recent
  example; write personal circuit breakers (loss cap, 10-min rule, pre-trade checklist, zoom-out-after-loss)
  and put them **where you see them while trading**. → [[concepts/aura/mind-and-emotional-control]]
- **D0-d — Journal setup** *(aura-05)*: stand up the journal (Neurospect app or a template) with the essentials
  + psychological fields + missed-trade log; use it as-is for two weeks before customizing. → [[concepts/aura/journaling-system]]
- **D0-e — Self-audit** *(aura-01)*: top-3 trading struggles (specific); last 3 rule-breaks (before/during/after
  + trigger + result); numeric self-rating on sleep/diet/stress/phone. → [[concepts/aura/psychology-foundations]]

## Stage 1 — Structural primitives (the eye-training core)

### D1-a — Swing points *(aura-06; target ≥50)*
- ✋ On **daily, 4H, 1H** (2 TFs min, 3 preferred), circle **≥50 swing points** — highs/lows only, nothing else.
- ✋ 2nd pass: for each, check across the triad whether **SMT** occurred there; recolour SMT-qualified vs not.
- 🛠 Re-run with the indicator on; confirm your hand-marks agree with what it plots. Note misses.
- **Advances:** swing points → Can-mark. **[R1–R3]**

### D1-b — Ranges *(aura-08 + aura-11; target ≥50)*
- ✋ Mark **≥50 ranges** across multiple TFs by the **expansive-move method** (not time-based).
- ✋ Refine: re-anchor each range's extremes onto **SMT-qualified** swings; where a swing is false across the
  triad, prefer the level swept on all assets. **[R8]**
- ✋ **Forward-bar live-read sim:** pick a random historical date, mark the HTF range, then step forward bar by
  bar, extending/flipping the range as new Sequential SMT + expansion occurs. (dOoMeR: no submission needed.)
- 🛠 Repeat with auto-ranges on for speed once the by-hand read is reliable.
- **Advances:** ranges → Can-mark. **[R4–R10]**

### D1-c — Gaps & what lies within *(aura-09; reuses the ≥50 range set)*
- ✋ Within each range **on NQ and YM**, mark liquidity to the **left and right** of any gaps (FVG/iFVG/NWOG/NDOG),
  and the **liquidity nested inside** the gap. If none visible: *look left* or *zoom in*.
- ✋ Flag confluence stacks (overlapping gaps; liquidity-left + liquidity-inside; near-EQ gaps).
- **Advances:** gaps → Can-mark. **[R11–R14]**

## Stage 2 — The confirmation engine

### D2-a — Triad correlation *(aura-10; proposed: 1 full triad + 1 spot-check)*
- Pull daily-returns data for one triad (e.g. metals) over ~2–3yr; compute **Pearson correlation**; check each
  pair lands in the **sweet spot**. Then validate against the live chart — does the number's promise hold? Note
  where chart behaviour **overrides** the number (dOoMeR's forex/energy lessons). **[R15–R16]**

### D2-b — Aura Asset overlay *(aura-16; proposed ≥20 weekly instances)*
- ✋ Overlay **6S** on a triad; on the **weekly timeframe**, find cases where 6S produced a divergence that
  explains a move the standard triad alone would **not** — self-check "would I have seen it without or with it?"
  **[R17]**

### D2-c — Sequential SMT *(aura-11/12; target ~50)*
- ✋ **NY-open drill:** repeatedly review price around the NY open without looking ahead — was there HTF
  (weekly/daily) Sequential SMT above/below? Confirmed by session-cycle SMT (e.g. 9:00 candle vs prior)? Repeat
  until pattern recognition is automatic, then test candle-by-candle on unseen dates.
- ✋ **Range flip:** the D1-b forward-bar sim, now explicitly tracking each Sequential-SMT confirm/invalidate.
- 🛠 Confirm hand-reads against the indicator (which shows only currently-valid SMTs). **[R18–R23]**

### D2-d — Sequential Skip *(aura-14; start simple — proposed target ≥10)*
- ✋ Hunt skip setups where the adjacent cycle is missing: **down-cycle skip** (weekly→session, daily→micro)
  **and** the **cross-asset variant** (same setup on another triad member in the bias direction); target modest,
  realistic R:R (1:2, 1:3). **[R24–R26]**

## Stage 3 — Cascade & risk

### D3-a — HTF→LTF cascade *(aura-17; proposed target ≥20 practice entries)*
- Run the full top-down if-then chain to a 5m iFVG entry; **before each practice entry write BOTH the confirm
  and the invalidate condition**; practise the discipline checkpoint: when the expected trigger fails to appear,
  zoom out — do not keep waiting. **[R27–R32]**

### D3-c — Risk math & evolving-R *(aura-13; proposed drill — proposed target ≥3 batches)*
- Compute, for a batch of your backtest trades: **R per trade**, **break-even win rate** for each R:R
  (`1/(1+R:R)`), and overall **expectancy** (`(win%×avgWinR)−(loss%×avgLossR)`).
- **Evolving-R reps:** on replayed winners, practise recalculating risk **from current price** and trailing so
  you never leave a static stop or treat breakeven as "free." **[R43–R45]**

*(Time Sum D3-b intentionally omitted as a drill — de-emphasized by dOoMeR; awareness only. [R37])*

## Stage 4 — Backtest in bar-replay

### D4-a — Study-then-replicate the worked reviews
For each review below: pull the **exact date in bar-replay**, read it **blind** (full checklist, no peeking),
then compare your read against the write-up in [[concepts/aura/trade-reviews]]. Score how much you saw
unaided.

| Review | Replay date | Concept it drills |
|---|---|---|
| aura-19 | **2026-04-30** (043026) | Sequential SMT, gap "SMT fill", swing points; news-timing |
| aura-20 | **2026-05-01** (050126) | Cracking correlation in gaps, EQ retest |
| aura-21 | **2025-11-26** (112625) | Ranges (premium/discount); a non-compliant entry |
| aura-23 | **2025-12-11** (121125) | Gold/silver cracking correlation; recovering a losing day |
| aura-24 | **2026-05-07** (050726) | **Double Sequential Skip**, full cascade (checklist fitness-check trade) |
| aura-26 | **2026-05-12** (051226) | Triads / asset-selection, cross-asset review (no trade) |
| aura-27 | **2026-05-13** (051326) | SMT within gaps around CPI; patience; declined 3rd position |
| aura-28 | **2026-05-13 × 2025-04-26** (051326 × 042625) | Cross-asset / inverse correlation; Sequential Skip |
| aura-30 | **2026-05-21** (05212026) | Aura Asset refinement ("Notorious" rule); Sequential Skip |

*(aura-18 "late February", aura-22/25/29 are overviews/synthesis with no single precise replay date — study as
narrated walk-throughs.)*

### D4-b — Blind forward-replay
On **unseen** dates, run the full [[concepts/mastery/aura/checklist]] per setup and **log every trade in R**.
Build toward ≥50 setups / ≥100 executed backtest trades with a computed expectancy (feeds the readiness gate).

## Stage 5 — Live tape reading

- **D5-a — Narrated live read:** during a live/delayed session, watch the triad + 6S and **call the read before
  it resolves** (in notes or aloud): where's HTF Sequential SMT, what confirms/invalidates, where's the gap
  liquidity target. Grade yourself after.
- **D5-b — Sim execution:** execute the called reads in sim with the full checklist + risk rules; the point is
  discipline under real-time pressure, not P&L.

## Stage 6 — Journal-driven refinement (continuous)

- **D6-a — Weekly review** *(aura-05)*: Dante's three questions — make more from winners / lose less on losers /
  generate more winning ideas.
- **D6-b — Manage-vs-walk-away** *(aura-05)*: log, per trade, actual managed outcome vs. set-and-walk-away
  outcome. If managing earns *less*, that's "your personal holy grail."
- **D6-c — Missed/canceled-trade log** *(aura-05)*: log trades you almost took / hesitated on / canceled, and
  count how many would have **lost** (Dante's canceled-order edge). Maps to the planned `missed_trades` journal
  surface — see [[concepts/architecture/trade-schema]] §Missed Trades.

## Drill → concept → ladder-stage map

| Drill | Concept | Advances to | Rep target |
|---|---|---|---|
| D0-a…e | discipline / journal | (habit) | behavioural |
| D1-a | swing points | Can-mark | ≥50 |
| D1-b | ranges | Can-mark | ≥50 |
| D1-c | gaps | Can-mark | (no separate target — reuses D1-b's range set) |
| D2-a | triads | Learned→Can-mark | 2 *(1 full triad + 1 spot-check)* |
| D2-b | Aura Asset | Can-mark | ≥20 *(proposed)* |
| D2-c | Sequential SMT | Can-mark | ~50 |
| D2-d | Sequential Skip | Can-mark | ≥10 *(proposed)* |
| D3-a | HTF→LTF cascade | Learned→Backtested | ≥20 practice entries *(proposed)* |
| D3-c | risk / evolving-R | Learned→Backtested | ≥3 batches *(proposed)* |
| D4-a/b | whole model | Backtested | ≥50 setups / ≥100 trades |
| D5-a/b | whole model | Live-ready | sim track record |
| D6-a/b/c | journaling | (habit) | weekly / continuous |

## See Also

- [[concepts/mastery/aura/learning-path]] — the stage each drill belongs to
- [[concepts/mastery/aura/tracker]] — log reps/stage/confidence
- [[concepts/mastery/aura/rules]] · [[concepts/mastery/aura/checklist]] · [[concepts/mastery/README]]
- [[concepts/aura/trade-reviews]] — the worked trades behind D4-a
