---
tags: [mastery, aura, checklist, execution, neurospect]
aliases: [Aura Execution Checklist, Aura Pre-Trade Checklist, Aura Trade Sheet]
sources: [concepts/mastery/aura/rules.md, concepts/aura/htf-ltf-application.md, concepts/aura/sequential-smt.md, concepts/aura/discipline-systems.md, concepts/aura/risk-management.md]
created: 2026-07-17
updated: 2026-07-17
---

# Aura Execution Checklist

The operational sheet for trading the Aura model. Each step is gated by a rule in
[[concepts/mastery/aura/rules]] (rule numbers in **[R##]**). Work it top to bottom; a "no" at a **hard
gate** means no trade. Copy the *Per-Trade Card* at the bottom for each individual setup (paper, journal,
or the Neurospect app).

> **How to use it while learning:** at Stage 2–3 (backtest/replay) run the whole checklist on every drill
> setup so it becomes automatic before live. The fitness check at the foot of this page shows the checklist
> walked against a real worked trade (aura-24).

---

## 0. Pre-market — readiness [R47–48, R54]

Do **not** proceed to framing until all are checked.

- [ ] Slept ~7h, consistent wake time; morning light + movement done; last caffeine before noon (NY).
- [ ] Environment set: phone out of the room / airplane; chats (Discord/X/Telegram) closed on the trading PC.
- [ ] Circuit breakers written and **visible**: 2-loss daily max, daily stop 2–3R, 10-min-after-loss rule. **[R40, R49]**
- [ ] I can answer the three questions: **What am I looking for? Where? What would make me stand aside?** **[R48]**
- [ ] Prior session reviewed + today's plan written **before** price moves (HTF context, prior liquidity taken). **[R26, R48]**

## 1. HTF framing — top-down cascade [R27–29]

Build the bias from the highest timeframe down. Mark by hand at the learning stage; indicator-assisted later.

- [ ] Marked HTF ranges (expansive-move method; discount/EQ/premium; no quadrants). **[R4–R5]**
- [ ] Range extremes anchored on **SMT-qualified** HTF swing points (not just any high/low). **[R3, R8]**
- [ ] Walked the if-then cascade and noted the current cycle chain (e.g. Monthly→Weekly→Daily→Session). **[R27]**
- [ ] Noted the **draw on liquidity** / target: the extreme of the timeframe being played, refined to the
  **liquidity within a gap** in the range's discount (long) / premium (short). **[R12, R35]**
- [ ] Written **both**: what would **confirm** the bias **and** what would **invalidate** it. **[R29]** ← hard gate

## 2. Confirmation — Sequential SMT [R18–R25]

- [ ] Bias supported by **Sequential SMT** nested across ≥2 adjacent cycles on the triad **+ Aura Asset (6S)**. **[R17–R18]**
- [ ] Confirmed by at least one of: cross-cycle nesting / gap-SMT-fill / candle-level SMT. **[R20]**
- [ ] Cross-cycle gap-pairing checked (weekly→daily gaps, daily/session→4H, micro→15m–1H). **[R21]**
- [ ] If the adjacent cycle is missing: valid **Sequential Skip** identified instead (further-down cycle, or
  same setup on another triad member in the bias direction). **[R24–R25]**
- [ ] I accept this is **probabilistic** — not treating the signal as certain. **[R19]** ← hard gate

## 3. Entry [R30–R34]

- [ ] On the 5-minute: a confirmed **inverse FVG (iFVG)** in the bias direction (plain FVG = fallback). **[R30]**
- [ ] Preferably a **session-cycle Sequential SMT within discount** (long) / premium (short) of the LTF range. **[R30]**
- [ ] For news/skip setups: waited for the **9:30 NY open** rather than chasing a pre-9:30 gap. **[R31]**
- [ ] Checked premium/discount position → set a realistic **R:R ceiling** (lower R:R if entering in premium). **[R32]**
- [ ] **Stop** at the invalidation level (high/low of the qualifying daily/4H SMT or recent swing). **[R33]**
- [ ] Stop distance acceptable — or switched to an **alternate triad asset** with a tighter equivalent gap. **[R34]**
- [ ] **Risk sized: 1–2% of total capital**, computed in **R**. Negative visualization done (pre-accepted the loss). **[R39, R43, R52]**
- [ ] Pre-trade check: *fits my plan? a setup I defined in advance? trading the market, not my P&L?* **[R50]** ← hard gate

## 4. In-trade management [R35, R45]

- [ ] Expecting price **not** to run cleanly to target (new ranges/SMT form along the way) — managing, not hoping. **[R35]**
- [ ] Risk recalculated **from current price**, not entry — maintaining ≥1:1 from here; not leaving a static stop. **[R45]**
- [ ] Trailing as structure develops; not treating a move-to-breakeven as "free." **[R45]**
- [ ] If the **expected trigger failed to appear** → treated as invalidation, zoomed out, did not keep waiting. **[R29]**

## 5. Exit [R35–R36]

- [ ] Exited at plan: HTF-range equilibrium, **or** held for liquidity in the HTF range's discount/extreme. **[R36]**
- [ ] Target was the **extreme of the timeframe played**; multi-level TP only if using the Aura Asset. **[R35–R36]**
- [ ] Recorded outcome in **R** (not dollars). **[R43]**

## 6. Circuit-breaker checkpoints (any time) [R40–R42, R49–R50]

- [ ] Hit **2 losses** today → **stop for the session.** No exceptions.
- [ ] Hit the **2–3R daily stop** → day over.
- [ ] After **any loss**: 10-minute rule (charts closed), then zoom out to HTF before considering re-entry.
- [ ] Feeling the urge to "get it back"? → that's the revenge spiral. Intervene **before the next trade.**
- [ ] Down **10R** overall → full stop + investigation before trading again. **[R41]**

## 7. Post-market review [R53]

- [ ] Daily check (~5 min): *Did I follow my plan? If not, what happened? One thing to do better tomorrow?* **[R49]**
- [ ] Journaled the trade(s) **and any missed/canceled setups** — with screenshot + emotional state. **[R53]**
- [ ] Weekly: ran the review on Dante's three questions (more from winners / less on losers / more ideas). **[R53]**
- [ ] "Never miss twice" holding — if I skipped journaling yesterday, I did it today. **[R53]**

---

## Per-Trade Card (copy one per setup)

```
Date/session:            Instrument (+triad):            Aura Asset (6S) read:
Bias (HTF cascade):                                      Confirm | Invalidate defined? [Y/N]
Sequential SMT (cycles nested):                          Skip used? [N / down-cycle / cross-asset]
Entry (5m iFVG @):        In discount/premium?            Stop @ (invalidation):
Target (TF extreme / gap-liquidity):                     Planned R:R:        Risk %/R:
--- management ---
Trailed? risk-from-here ≥1:1?     Trigger-failed→zoomed out?      Exit @:        Result (R):
--- review ---
Plan followed? [Y/N]  Rule broken (why):    Emotion (before/during/after):    Grade (A+/A/B/C):
```

*(Field names mirror [[concepts/architecture/trade-schema]] — `setup_type`, `entry_pda`,
`smt_confirmation`, `r_multiple`, `plan_followed`, `mistake_tags`, `quality_grade` — so a paper card
transfers cleanly into the Neurospect journal app.)*

---

## Fitness check — checklist vs. a real worked trade

Walked against **aura-24 (050726, "double sequential skip", replay 2026-05-07)** from
[[concepts/aura/trade-reviews]], to confirm each step maps to a real decision:

| Checklist step | In the aura-24 trade |
|---|---|
| §1 HTF framing + confirm/invalidate | Multi-day NQ long framed off the full HTF cascade + range context. |
| §2 Sequential SMT / Skip | The setup's whole identity is a **double Sequential Skip** (adjacent cycle missing twice → skipped). **[R24]** |
| §3 Entry (5m iFVG, stop at invalidation) | Entry on the iFVG in the bias direction; stop at the qualifying-swing invalidation. **[R30, R33]** |
| §4 management (price won't run clean) | Multi-day hold with trailing as new ranges/SMT formed — exactly R35's expectation. |
| §7 review | Captured as a teaching review — the study-then-replicate target in [[concepts/mastery/aura/exercises]]. |

Every checklist section maps to a real decision in the trade; no step is dead weight, and no decision in the
review lacks a checklist home. ✅

## See Also

- **Practising this checklist in Tradezella** (authored 2026-08-12; these three pages plus this one are
  projected into `neurospect-learn`'s `/runner` — edit the wiki, never the app):
  - [[concepts/mastery/aura/tradezella-setup]] — session setup + the declared counting basis
  - [[concepts/mastery/aura/tradezella-rule-mapping]] — these phases as Playbook rule groups
  - [[concepts/mastery/aura/chart-markup]] — what to draw, in what order
- [[concepts/mastery/aura/rules]] — the rule behind each **[R##]**
- [[concepts/mastery/aura/exercises]] — drills that build each checklist section to automatic
- [[concepts/mastery/aura/tracker]] · [[concepts/mastery/README]]
- [[concepts/aura/trade-reviews]] — worked trades to walk this checklist against
