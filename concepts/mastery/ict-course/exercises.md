---
tags: [mastery, ict-course, exercises, drills, backtesting, tape-reading, neurospect]
aliases: [ICT Drills, ICT Exercises, MrWitness-AXL Practice Library]
sources: [concepts/course/module-1-foundations/03-homework-and-practice.md, concepts/course/module-3-session-and-bias/01-power-of-three.md, concepts/course/module-3-session-and-bias/02-session-kill-zones.md, concepts/course/module-3-session-and-bias/03-deviations.md, concepts/course/module-3-session-and-bias/04-daily-bias.md, concepts/course/module-4-market-structure/01-swing-classification.md, concepts/course/module-4-market-structure/02-fractality.md, concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow.md, concepts/course/module-5-order-flow-and-smt/02-smt-divergence.md, concepts/business-logic/ict-live-commentary.md, sources/neurospect/2026-04-22-youtube-1000-points-nq-2026-03-04.md, sources/neurospect/2026-04-22-youtube-first-week-march-2026-03-07.md]
created: 2026-07-17
updated: 2026-07-30
---

# ICT Course Exercise Library

The drill library for the MrWitness-AXL track. It is an **index + gap-fill**, not a new curriculum: the
**stages map 1:1 onto the existing course modules** ([[concepts/course/README]] is the learning path —
this page does not replace it). Each drill either **indexes** a lesson's own homework (cited) or
**fills a gap** where the lesson shipped none *(flagged `gap-fill`)*.

Marking/reading drills have a **✋ hand-marking** variant (do first — trains the eye) and a **🛠
tool-assisted** variant. Rep targets come from the lesson where one was given; otherwise proposed and
flagged *(proposed)*. Log every drill's reps / ladder stage / confidence in
[[concepts/mastery/ict-course/tracker]].

**Tooling assumed:** TradingView bar-replay, futures (NQ/ES/YM triad + the instruments each model names),
a multi-pane SMT layout, and an economic calendar. ✋ variants are done by hand; 🛠 variants add
indicators/auto-tools for speed once the eye is trained.

> **Reusable primitive.** [[concepts/course/module-1-foundations/03-homework-and-practice]] ships a
> `## Readiness Check` checkbox block (7 items) gating entry to Module 2. That checkbox pattern is the
> model for the **per-module readiness checks** in [[concepts/mastery/ict-course/tracker]].

---

## Stage 0 — Discipline & journal setup (behavioural; no rep target)

The ICT track's discipline canon lives in [[concepts/business-logic/ict-live-commentary]] §"Live Trading
Discipline (AXL)" (rules [R37]–[R41] in [[concepts/mastery/ict-course/rules]]).

- **D0-a — Loss-limit precommitment** *(R37, gap-fill drill)*: write your account tier and its **daily
  loss limit** ($1,000 if ≥$10K, else $500) where you see it while trading; write the "hit it → log out"
  rule and a place to log the day you first honour it under pressure.
- **D0-b — Set-and-forget contract** *(R38)*: write the **only three** exit conditions (break-even /
  planned partials / take profit) as a one-line contract; for two weeks, log any trade you closed
  *outside* those three and why.
- **D0-c — Three-requirements self-audit** *(R40)*: rate yourself 1–5 on ① psychology, ② rules, ③ a
  backtested model; the lowest score is your current bottleneck — name the next action for it.
- **D0-d — Bad-conditions recognition** *(R41)*: keep a running log of days you (correctly) stood aside —
  choppy/accumulation days, pre-11AM Thursday, "today is not conditions." Count "sat on hands" as a win.
- **D0-e — Journal setup**: stand up the journal (Neurospect app or template) with the essentials +
  missed/canceled log; use as-is two weeks before customizing. Maps to
  [[concepts/architecture/trade-schema]].

## Stage 1 — Module 1: Foundations (the eye-training core)

### D1-a — Liquidity & swing points *(indexes M1.1 + M1.3 Class-1 homework; target ≥5 marked setups, MrWitness "1–5 examples")*
- ✋ On **1H and 15M**, mark **swing highs = BSL / swing lows = SSL** as single price levels (3-candle,
  candle-2 level — not zones). Identify the **DOL**. → [[concepts/course/module-1-foundations/01-what-moves-the-market]]
- ✋ On **5M–1M**, find a displacement **FVG (BISI bull / SIBI bear)** aligned to the DOL; mark entry
  (candle-3 area, one tick), stop (below candle 1), target (the 1H/15M DOL). Screenshot with **entry time
  + economic calendar** (the exact submission MrWitness asks for).
- 🛠 Re-run with an FVG/liquidity indicator; confirm hand-marks agree. **Advances:** liquidity, swings → Can-mark.

### D1-b — FVG / IOFED / inversion *(indexes M1.2 + the lesson's IOFED checkbox; target ≥20 gaps, proposed)*
- ✋ Mark ≥20 FVGs (candle-1→candle-3 extremes); classify each **displacement vs. slow-range** (only
  displacement counts). Run the **IOFED checklist** (return to gap, no close below CE → highest
  probability); flag **BAG** skips and **inversion FVGs** (bearish gap closed above → bull zone). →
  [[concepts/course/module-1-foundations/02-fair-value-gaps]]
- 🛠 Confirm against an FVG indicator. **Advances:** FVG → Can-mark.

> **Gate:** clear the [[concepts/course/module-1-foundations/03-homework-and-practice]] `## Readiness
> Check` (7 boxes) before Module 2 — that's the built-in stage gate, reused in the tracker.

## Stage 2 — Module 2: Price delivery

### D2-a — Four stages of APD *(gap-fill — M2.1 has rules but no homework)*
- ✋ On 5 sessions, label every leg **Consolidation → Expansion → Retracement → (Expansion/Reversal)**.
  For each retracement, verify **both jobs** (inefficiency filled **and** discount ≤50%) → tag real vs.
  **fake retracement**. Apply the two read-checks (R12): if a "retracement/consolidation" became a
  reversal, re-label it. → [[concepts/course/module-2-price-delivery/01-four-stages-apd]]
- **Advances:** four-stages read → Can-mark. *(proposed target: 5 sessions × all legs)*

### D2-b — Consolidation model *(indexes M1.3 Class-2 homework via [[concepts/course/module-2-price-delivery/02-consolidation-model]])*
- ✋ Find a consolidation on 1M–5M (**bodies, not wicks**), mark **EQ (50%)**, find a **PDA at/below EQ**
  after an intra-range sweep; mark entry/stop/TP1(range low)/TP2(PDH-L), label kill zone + entry time.
- 🛠 Then run the canonical checklist at [[concepts/entry-models/consolidation-model]] against your mark
  (follow it there — do not re-key it here). **Advances:** consolidation → Can-mark → Backtested.

### D2-c — Expansion & Retracement *(gap-fill — M2.3 has no homework)*
- ✋ On 5 discount setups, measure the **expansion leg 50%**, mark the **FVG/OB at/below 50%**, confirm
  price reached discount (not a fake retracement), mark entry/stop/target. → [[concepts/course/module-2-price-delivery/03-expansion-retracement]] + spec [[concepts/entry-models/expansion-retracement-model]].
- **Advances:** E&R → Can-mark → Backtested. *(proposed ≥10)*

### D2-d — Reversals *(gap-fill — M2.4 has Key Rules but no homework)*
- ✋ Hunt reversals at **layered liquidity pools**: mark the origin swing (the reversal must reach it,
  R15), the sweep + rejection, and **plan partials at the rejection block** (R17). Tag HRLR context (R16)
  where a **type-1 failure swing** was likely. → [[concepts/course/module-2-price-delivery/04-reversals]] + spec [[concepts/entry-models/reversal-raid-on-stops]].
- **Advances:** reversals → Can-mark. *(proposed ≥10, mixed outcomes)*

## Stage 3 — Module 3: Session context & bias

### D3-a — Power of Three / AMD *(indexes M3.1 homework — 10 consecutive days)*
- ✋ Mark opening prices daily (midnight/8:30/9:30/1:30PM, colour-coded); after each day identify the
  **manipulation leg** (which open anchored it), count the 2–4 AMD cycles, and record over **10 days**
  which open most often anchors the low/high. → [[concepts/course/module-3-session-and-bias/01-power-of-three]]

### D3-b — Kill zones *(indexes M3.2 homework — 1 week)*
- ✋ Each day pre-open, mark all five opens; over a week track **which KZ sets the HOD vs. LOD**; on NY-AM
  days note whether 9:30 continues or manipulates 8:30. → [[concepts/course/module-3-session-and-bias/02-session-kill-zones]]

### D3-c — Deviations *(indexes M3.3 homework — 10 days, personal journal only)*
- ✋ Anchor deviation Fibs from the manipulation swings; record where HOD/LOD prints vs. the deviation
  levels and any **HPDL** (deviation + daily FVG) alignment. Practise **not** exiting at the obvious level
  — first partial one deviation beyond (R23). → [[concepts/course/module-3-session-and-bias/03-deviations]]

### D3-d — Daily bias *(indexes M3.4 homework + `## Daily Checklist` — 10 days)*
- ✋ Each evening write the one-sentence bias ("inside a [bull/bear] 4H FVG; target [level]"); each morning
  note opening-price position; after the session score whether HOD/LOD formed in the bias direction. Run
  the lesson's `## Daily Checklist` as the routine (reconciled with the pre-market routine, R36). →
  [[concepts/course/module-3-session-and-bias/04-daily-bias]]

## Stage 4 — Module 4: Market structure

### D4-a — Swing classification *(indexes M4.1 homework — 5 days)*
- ✋ On NQ/ES 15M, mark every swing low; classify **STL (no gap) vs. ITL (price leg creates/fills an
  FVG)**; draw **STL→ITL→STL→MSS**; record how often the STL right of the ITL held. → [[concepts/course/module-4-market-structure/01-swing-classification]]

### D4-b — Fractality *(indexes M4.2 homework — 5 days)*
- ✋ For 5 days, take one FVG, find the swing forming inside it on the retracement, classify STH/STL→ITH/ITL,
  trace the three-swing fractal to MSS, then find the **same pattern nested on a smaller TF**. → [[concepts/course/module-4-market-structure/02-fractality]]

### D4-c — Structure deviations *(gap-fill — M4.3 has a procedure but no homework)*
- ✋ On 10 post-MSS moves, **two-set anchor**: project deviation targets from the **structural** swing set
  (ITL→expansion), not only the session sweep; record how close price came to the −1/−2/−2.5 projections.
  → [[concepts/course/module-4-market-structure/03-structure-deviations]] *(proposed ≥10)*

### D4-d — Model 2022 + OTE + CSD *(gap-fill — M4.4 has Full Sequence but no homework)*
- ✋ Hunt setups with **no 50% retracement after MSS** (Model 2022 active); map the **OTE 62–79%**, select
  the block by the three rules (highest down-close body → propulsion block → concert with 0.705, R30);
  mark **CSD** (down-close opening price breached) as the early entry; stop below OTE block close; deviation
  targets. → [[concepts/course/module-4-market-structure/04-model-2022-ote-csd]] + spec [[concepts/entry-models/model-2022-ote]]. *(proposed ≥10)*

## Stage 5 — Module 5: Order flow & SMT

### D5-a — Order flow on a closing basis *(indexes M5.1 homework — 1 week)*
- ✋ On 5M ES/NQ, mark the dealing-range quadrants; watch the first OB after an LTH/LTL — does it hold on
  the 1st/2nd return? Tag **LRLR vs. HRLR**; note when order flow **breaks** (opposing candles stop being
  respected → step aside, R33). → [[concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow]]

### D5-b — SMT divergence *(indexes M5.2 homework — 5 days)*
- ✋ Set a multi-pane **NQ+ES(+YM)** layout; at each Power-of-Three manipulation leg check for **cracking
  correlation**; record how often SMT appeared and the outcome (reversal vs. continuation). → [[concepts/course/module-5-order-flow-and-smt/02-smt-divergence]] + spec [[concepts/entry-models/smt-confirmation-entry]].

## Stage 6 — Tape reading (from the stream + YouTube corpus)

Study-then-replicate drills built on the ingested **candle-by-candle NQ/ES/YM reads**. **Important:** the
11 stream transcripts have `video_date: unknown`, so you **cannot replay the exact session** — instead
**study the read, then pull a *comparable news-context* session in bar-replay and replicate it blind**.
The **2 YouTube examples carry precise dates** → true exact-date replay.

Method for each: read the transcript's live read → note bias call, DOL, the model used, entry/target →
find a matching session (by the news tag below) → run the full pre-market routine (R36) + entry gate
(R35) blind → compare your read to the mentor's.

| Drill | Source | Session / news context | Drills | Replay |
|---|---|---|---|---|
| T-01 | `2026-04-20-stream-no-news-mon-tape-reading` | No-news Monday | patience; range/consolidation reads on a quiet day | comparable no-news Monday |
| T-02 | `2026-04-20-stream-0830-mid-mon-tape-reading` | Mid-month Monday, 08:30 | AMD off the 8:30 open, DOL framing | comparable mid-month Monday |
| T-03 | `2026-04-20-stream-1000-jolts-tue-tape-reading` | JOLTS Tuesday, 10:00 | trading a 10:00 data release; kill-zone timing | comparable JOLTS/10:00-data Tuesday |
| T-04 | `2026-04-20-stream-tue-10-fed-chair-testifies` | Tuesday, Fed Chair testifies 10:00 | daily-FVG bias into a speaker event; standing aside | comparable Fed-speaker day |
| T-05 | `2026-04-20-stream-0830-uc-fomc-wed-tape-reading` | FOMC Wednesday, 08:30 | high-impact event day; two-scenario framework | comparable FOMC Wednesday |
| T-06 | `2026-04-20-stream-0830-uc-thu-tape-reading` | Thursday, 08:30 | Thursday delivery; pre-NFP caution context | comparable Thursday |
| T-07 | `2026-04-20-stream-thu-tape-reading-live-nq` | Thursday, live NQ | live NQ read; discipline under a running trade | comparable Thursday |
| T-08 | `2026-04-20-stream-0830-nfp-fri-tape-reading` | **NFP Friday**, 08:30 | NFP-day read; the pre-11AM-Thursday/NFP off-limits rule (R41) | comparable NFP Friday |
| T-09 | `2026-04-20-stream-fri-10-mid-tape-reading` | Mid-month Friday, 10:00 | Friday 10:00 read; end-of-week liquidity | comparable mid-month Friday |
| T-10 | `2026-04-20-stream-1000-ism-pmi-1300-fed-speaks` | ISM/PMI 10:00 + Fed speaks 13:00 | double-event day; PM-session opening price | comparable ISM/PMI + Fed-speaker day |
| T-11 | `2026-04-20-stream-tapx-tape-reading-live-nq` | Live NQ (general) | general live-tape execution read | any comparable NY-AM session |
| T-12 | `2026-04-22-youtube-1000-points-nq-2026-03-04` | **2026-03-04** "+1000pts NQ" | a full high-follow-through NQ delivery | **exact date 2026-03-04** |
| T-13 | `2026-04-22-youtube-first-week-march-2026-03-07` | **2026-03-07** "first week of March" | weekly-opening-price rule; weekly framing | **exact date 2026-03-07** |

*Note the two `-uc-` streams and the "all-time-highs" / explicit "don't-trade" framing the boot inventory
called out live inside these transcripts — surface those as extra tags on first study; they are not in the
frontmatter.*

- **T-14 — Blind live-read** *(mirror of the Aura live drill)*: during a live/delayed session, watch the
  triad + call the read (bias, DOL, model, target) **before it resolves**; grade after.

## Stage 7 — Backtest in bar-replay (the expectancy evidence)

For each of the 7 entry models, run its canonical checklist blind in replay and **log every trade in R**.
Build toward **≥50 setups / ≥100 executed backtest trades** with a computed expectancy — this feeds the
Readiness-to-Live Gate in [[concepts/mastery/ict-course/tracker]] and [[concepts/mastery/README]].

- Per-model checklists (canonical, follow in place — do not fork): [[concepts/entry-models/consolidation-model]] ·
  [[concepts/entry-models/expansion-retracement-model]] · [[concepts/entry-models/reversal-raid-on-stops]] ·
  [[concepts/entry-models/london-model]] · [[concepts/entry-models/model-2022-ote]] ·
  [[concepts/entry-models/daily-bias-model]] · [[concepts/entry-models/smt-confirmation-entry]].
- Compute per batch: **R per trade**, **break-even win rate** `1/(1+R:R)`, **expectancy**
  `(win%×avgWinR)−(loss%×avgLossR)`.

## Stage 8 — Journal-driven refinement (continuous)

- **J-a — Weekly review**: what to make more from winners / lose less on losers / more winning ideas.
- **J-b — Set-and-forget audit** *(R38)*: log managed-vs-planned outcome per trade; if manual
  intervention earned *less*, that proves the set-and-forget rule.
- **J-c — Missed/canceled log**: log hesitations/cancels and how many would have lost. Maps to the planned
  `missed_trades` surface — [[concepts/architecture/trade-schema]] §Missed Trades.

## Drill → concept → ladder-stage map

| Drill | Concept | Advances to | Rep target |
|---|---|---|---|
| D0-a…e | discipline / journal | (habit) | behavioural |
| D1-a | liquidity & swings | Can-mark | ≥5 (1–5 submission) |
| D1-b | FVG / IOFED | Can-mark | ≥20 *(proposed)* |
| D2-a | four stages APD | Can-mark | 5 sessions *(gap-fill)* |
| D2-b | consolidation | Can-mark→Backtested | Class-2 homework |
| D2-c | E&R | Can-mark→Backtested | ≥10 *(gap-fill)* |
| D2-d | reversals | Can-mark | ≥10 *(gap-fill)* |
| D3-a | Power of Three | Can-mark | 10 days |
| D3-b | kill zones | Can-mark | 1 week |
| D3-c | deviations | Can-mark | 10 days |
| D3-d | daily bias | Can-mark | 10 days |
| D4-a | swing classification | Can-mark | 5 days |
| D4-b | fractality | Can-mark | 5 days |
| D4-c | structure deviations | Can-mark | ≥10 *(gap-fill)* |
| D4-d | Model 2022 / OTE / CSD | Can-mark | ≥10 *(gap-fill)* |
| D5-a | order flow | Can-mark | 1 week |
| D5-b | SMT divergence | Can-mark | 5 days |
| T-01…14 | whole-model tape read | Learned→Can-mark | 1 per drill *(T-01…T-13 studies + the T-14 live read)* |
| Stage 7 | all 7 entry models | Backtested | ≥50 setups / ≥100 trades |
| Stage 8 | journaling | (habit) | weekly / continuous |

## See Also

- [[concepts/mastery/ict-course/rules]] — the rule each drill builds
- [[concepts/mastery/ict-course/tracker]] — log reps / stage / confidence
- [[concepts/course/README]] — the module curriculum these stages mirror (the learning path)
- [[concepts/entry-models/README]] — canonical per-strategy checklists for Stage 7
- [[concepts/mastery/aura/exercises]] — the parallel Aura drill library (format mirrored here)
