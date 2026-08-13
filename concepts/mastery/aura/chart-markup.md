---
tags: [mastery, aura, tradezella, chart, markup, drawing, indicators, probe, runner, neurospect]
aliases: [Aura Chart Markup, Chart Markup Protocol, Markup Order]
sources: [concepts/mastery/aura/rules.md, concepts/mastery/aura/checklist.md, processes/distributed-workflow/active/aura-session-runner.md]
created: 2026-08-12
updated: 2026-08-12
---

# Aura Chart Markup Protocol

What to draw on every chart, in what order, so **the same setup looks the same twice**. Marking by hand
is the Stage 2–3 requirement in [[concepts/mastery/aura/checklist]] §1 — *"Mark by hand at the learning
stage; indicator-assisted later"* — and, per the probe below, in Tradezella there **is no "later"**.

---

## ⭐ The probe — run 2026-08-12, and the answer is NO

Paul asked for *"what exactly to mark out on each chart (**or indicators to use that will mark out all
our levels**)"*. Whether that is a drawing protocol or a tooling spec depended on a fact nobody had
measured. It has now been measured, in the product, on the actual backtesting chart.

| Question | Verdict | How it was established |
|---|---|---|
| Can you add **custom** indicators to the backtest chart? | **NO** | The `Indicators` dialog is a single flat list under one `SCRIPT NAME` header. There is **no** Community Scripts tab, **no** My Scripts tab and **no** Pine editor anywhere in the surface. |
| Discriminating search | **NO** | Searching `smt` returns **"No indicators matched your criteria"**. |
| Can the *vendor* ship custom studies? | **YES** | Searching `session` returns **"Sessions Indicator by Tradezella"** — so the capability exists; it is simply not exposed to users. |
| What engine is it? | **TradingView Charting Library — PROVEN, not inferred** | The chart runs in a `blob:` iframe exposing **`TradingViewApi`**, `chartWidget` and `ChartApiInstance`, and `tradingViewApi.chart(i)` answers to the library's documented surface (`getAllShapes`, `createShape`, `removeEntity`, `getLineToolsState`). The UI evidence — built-in study names verbatim, the TV symbol-settings dialog with `Template ▾` / `Apply to all`, the drawing toolbar, `auto`/`log`/`%` scale controls — first suggested it; the API object settles it. |
| Built-in indicators? | **YES** | The full TV built-in set is available. None of them compute SMT. |
| Drawing tools? | **YES — the full TV toolbar** | Trend lines, horizontal lines/rays, fibs, patterns, brush, text, emoji, measure, magnet, lock, hide-all, cross-chart link, delete-all. |
| Chart-settings template? | **YES** | `Template ▾` in the settings dialog footer; `Apply to all` pushes settings across the 4 panes. |
| Do drawings persist across replay steps? | **YES — MEASURED** | Counted through the chart's own API before and after stepping the replay: **99 shapes → 99 shapes**. |
| Do drawings persist across sessions? | **YES — MEASURED** | The same 99 shapes were present on the NQ chart after a **fresh page navigation** to the session URL, so they are stored server-side, not just held in the page. |

### What this kills

**Pine Script does not work here.** The older `neurospect-app` shipped `public/neurospect-coach.pine`,
which made Pine look like a settled in-house capability — inheriting that assumption into this
workstream would have produced a markup step that could not be followed. TradeZella ≠ TradingView.

More sharply: **[[concepts/mastery/aura/rules]] R23 cannot be reproduced inside Tradezella.** R23
describes the Sequential-SMT *indicator* displaying only currently-valid signals. There is no way to put
that indicator on this chart. Every SMT read in a Tradezella backtest is a **hand read**, and R23's
"always read the current state, never a stale signal" becomes a discipline instruction rather than
something the tool enforces.

### What this does NOT change

The markup stays **in Tradezella**. The alternative — mark up in TradingView and use Tradezella only for
logging — was the fallback if the chart took no levels at all. It does take levels; it just takes them
by hand. Splitting across two applications would add a window to a workflow whose entire design
constraint is *one narrow window beside one chart*, and it would break the link between a drawing and
the order it justified.

**Hand-marking is also the correct Stage 2–3 answer independently of tooling.** The drills in
[[concepts/mastery/aura/exercises]] are built on ✋ hand reps precisely because the recognition has to
live in your head, not in a script.

---

## 0. One-time chart setup

- [ ] Four panes, one symbol each: **`NQ` `ES` `YM` `6S`**. **[R16, R17]**
- [ ] Timezone **`(UTC-4) New York`**, Session **`Extended trading hours`**, then `Apply to all`. **[R31]**
- [ ] Save a **chart settings Template** so every session starts identical.
- [ ] Turn the **magnet** on so levels snap to candle highs/lows — a swing point drawn 2 ticks off the
  actual high is a swing point you did not mark. **[R1]**
- [ ] Fix the colour convention below and never vary it. Consistency is what makes two sessions
  comparable at a glance.

### Colour convention

| Object | Colour | Why |
|---|---|---|
| Range boundary (high / low) | **White** | Structural, neutral — the frame everything else sits in |
| Discount / EQ / premium | **Grey, dashed** | Zones, not levels — should recede |
| SMT-qualified swing | **Yellow** | The load-bearing filter (R3); it must be visually distinct from an unqualified swing |
| Unqualified swing | **Grey, thin** | Provisional by definition — draw it, but do not let it look decisive |
| Gap (FVG / iFVG / NWOG / NDOG) | **Blue box** | The thing price is drawn to |
| Liquidity inside a gap | **Blue, dotted** | The *precise* target (R12), distinct from the gap's boundary |
| Entry / stop / target | **Green / red / green dashed** | Execution, not analysis |

---

## 1. The markup order — every replayed day, always this sequence

The order is the point. It mirrors the top-down cascade (R27), so the drawing you make next is always
gated by the one you just made — you cannot draw the entry before you have drawn what justifies it.

- [ ] **M1 · Swing points.** Mark 3-candle pivots on the HTF being framed. Fractal — the mechanics do
  not change with timeframe. **[R1, R2]**
- [ ] **M2 · SMT-qualify them.** Across `NQ` `ES` `YM` (+`6S`), mark which swings hold on all legs and
  which are swept on some. Recolour: qualified → yellow, unqualified → grey. **This is the filter
  everything downstream leans on.** **[R3]** ← hard gate
- [ ] **M3 · The range.** Find the **largest expansive move between two swing points** — that move *is*
  the range. Draw its high and low. **Not** a time-based range. If it isn't obvious, zoom out until it
  is; overlapping ranges are acceptable, do not force one. **[R4, R9]**
- [ ] **M4 · Anchor the extremes** on SMT-qualified swings only. Where a candidate looks false across the
  triad, prefer the low/high **actually swept on all triad assets** over the most extreme one. **[R8]**
- [ ] **M5 · Discount / EQ / premium.** Use the **Fib Retracement** tool with **only the `0`, `0.5` and
  `1` levels enabled** — delete 0.236/0.382/0.618/0.786 from the tool's settings. This model uses
  **no quadrants**, and a fib left on defaults silently imports a different model's framework onto your
  chart. **[R5]** ← the divergence flagged in `rules.md`
- [ ] **M6 · Gaps.** Box every **FVG, iFVG, NWOG, NDOG** in the range's discount (long) / premium
  (short). Only these four types — no BPR, no volume-imbalance vocabulary. **[R11]**
- [ ] **M7 · Liquidity inside the gaps.** Mark the swing high/low nested *inside* each gap — **that**
  internal level is the target, not the gap boundary. If none is visible: *look left* for a resting
  untaken level, or *zoom in* until a lower-TF swing appears inside the same gap. **[R12, R13]**
- [ ] **M8 · The draw on liquidity.** Mark the one target you are actually playing for: the extreme of
  the timeframe being played, refined to the liquidity-within-a-gap in the range's discount/premium.
  **[R12, R35]**
- [ ] **M9 · Confluence.** Note where gaps overlap (NWOG × FVG), where liquidity-left and
  liquidity-inside stack, and where a gap sits near equilibrium — these raise a gap's probability
  additively. **[R14]**
- [ ] **M10 · Cascade down** to the entry timeframe: Monthly→Weekly→Daily/Session→4H→15m→**5m**. Repeat
  M1–M2 at the entry TF only — do not re-mark the whole HTF structure. **[R27]**
- [ ] **M11 · The entry objects.** On the 5m: the **iFVG** in the bias direction, the **stop** at the
  invalidation level (the qualifying daily/4H SMT or recent swing), and the **target**. **[R30, R33]**
- [ ] **M12 · Write the invalidation on the chart** as a text label, not only in your head. If price
  does *this*, the idea is wrong. **[R29]** ← hard gate

## 2. What NOT to draw

- [ ] **No quadrants** (0.25 / 0.75). Aura reads discount/EQ/premium only. **[R5]**
- [ ] **No "order blocks."** This model does not use the term — what others call an order block is just
  price returning to a range's discount/premium. Drawing one imports a vocabulary the model rejects.
  **[R10]**
- [ ] **No Time Sum (369) grid.** dOoMeR de-emphasises it himself as rare and subjective. Do not build
  the chart around it. **[R37]**
- [ ] **No indicator you would not be able to justify from [[concepts/mastery/aura/rules]].** The built-in
  TradingView set is available and almost none of it belongs to this model.

## 3. After the day

- [ ] Screenshot the marked chart **before** stepping past the setup — a replay that has moved on cannot
  be un-moved, and the screenshot is what travels into the Neurospect journal entry. **[R53]**
- [ ] Drawings themselves **do** survive (measured — see §The probe), so the chart stays a durable record
  of the markup. The screenshot is for the *journal*, not as insurance against losing the drawing.

### What Paul's charts already look like — `OBSERVED` 2026-08-12

Session `NQ Macro Po3 - Asia Session` carries **99 shapes on the NQ pane** (94 rectangles, 3 vertical
lines, 2 trend lines) and **zero on MNQ, ES and MES**. Two things follow:

- The markup habit already exists — this protocol is regularising it, not introducing it.
- **All the markup is on one chart.** Sequential SMT is read *across* the triad (R18), so the comparison
  legs need marking too. That reinforces §0: the panes must be `NQ` `ES` `YM` `6S`, and each needs its
  swing points marked (M1–M2) or there is nothing to compare.

## Open flags carried from `rules.md` — do not silently resolve

These are live divergences in the model, surfaced here because the markup step is where they bite:

- **Quadrants:** Aura uses discount/EQ/premium only (R5); the ICT order-flow model uses 0.25/0.75.
- **"Order block":** rejected by Aura (R10), used heavily in the ICT entry-models library.
- **Time Sum (369):** de-emphasised by dOoMeR himself (R37) — not load-bearing.
- **Firm vs personal stop-trailing:** dOoMeR trails tightly on firm capital, admits his personal account
  is looser, and does not say which standard students should hold. Treat the **firm standard** as the target.

## See Also

- [[concepts/mastery/aura/tradezella-setup]] — the session the chart belongs to
- [[concepts/mastery/aura/tradezella-rule-mapping]] — what gets ticked once the markup is done
- [[concepts/mastery/aura/rules]] · [[concepts/mastery/aura/checklist]]
- [[concepts/aura/gaps]] · [[concepts/aura/ranges]] · [[concepts/aura/swing-points]]
