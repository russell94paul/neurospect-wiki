---
tags: [mastery, aura, tradezella, playbook, rules, tagging, adherence, runner, neurospect]
aliases: [Aura Playbook Mapping, Rule to Tag Mapping, Tradezella Rule Mapping]
sources: [concepts/mastery/aura/rules.md, concepts/mastery/aura/checklist.md, processes/distributed-workflow/active/aura-session-runner.md]
created: 2026-08-12
updated: 2026-08-12
---

# Aura Rules → Tradezella Playbook

The mapping that turns twenty replayed days into **data rather than anecdote**. Building this playbook
is the step [[processes/distributed-workflow/active/backtest-companion]] §B2 has always asked for and
never had — *"define rules in the Playbook Rules tab"* — and it is the reason the free discipline
instruments have only ever been able to read zero.

> **Do not paraphrase a rule into something crisper.** The wording in [[concepts/mastery/aura/rules]] is
> canonical; the text below compresses it to fit a one-line playbook row, and where the two disagree,
> `rules.md` wins and this page is wrong.

---

## The strategy builder's actual shape — `OBSERVED` 2026-08-12

`Strategies → + Create strategy → Create your own` (**not** a template — a template imports someone
else's rules). The form:

| Field | Notes |
|---|---|
| **Name** + icon/colour | |
| **Description** | Multi-line, accepts a full paragraph. |
| **Photo** | Optional. |
| **Rules** | `Add rule group` → a named group; `+ Add rule` → a row inside it. |

### ⚠️ Every rule row carries an OUTCOME FILTER, and every Aura rule must be `Always`

Each rule has a dropdown — **`Always` / `Winner` / `Loser` / `Break even`** — described in the product
as *"Only show this rule when the selected trade outcome or type applies."*

**Leave every Aura rule on `Always`.** A rule shown only on winners computes its follow rate over a
**biased subset**: you would never record breaking it on a loser, and the resulting number would look
like discipline while measuring nothing. The single most useful thing this playbook produces —
*which rule do I break, and what does breaking it cost* — requires the rule to be present on **every**
trade, especially the ones that went wrong.

This is the same failure the whole enforcement layer is built against: the adversary is
**self-deception**, not an attacker. An outcome-filtered rule is a device for not seeing.

*(`Winner`/`Loser` are legitimate for genuinely retrospective review prompts — "on this loser, had I
already hit the daily stop?" — but do not mix those into the adherence set; their follow rates are not
comparable with the rest.)*

## What the instrument actually is — `OBSERVED` 2026-08-12

The Strategy (Playbook) → **`Rules`** tab holds **named, drag-reorderable rule groups**, each containing
free-text rules. Per rule, Tradezella computes and displays:

| Column | What it gives you |
|---|---|
| **Follow rate** | % of trades on which you ticked this rule. **Per-rule adherence.** |
| **Net profit/loss** | P&L across trades where the rule was followed. |
| **Profit factor** | Same, as a ratio. |
| **Win rate** | Same, as a win %. |

This is materially better than the "tagging scheme" the workstream assumed. Mapping Aura rule IDs 1:1
onto playbook rows gives you, for free, **which Aura rule you break most and what breaking it costs** —
the exact question the Neurospect adherence layer exists to answer.

Each order in the `Orders` table then carries **`Rules followed`** (as `X / N`) and **`Tags`**.

### ⭐ `0 / 0` is a discriminating read, not an ambiguous one

The existing `Macro Model` session shows `Rules followed 0 / 0` on all five orders. The **denominator**
is the signal: `0 / N` would mean *rules existed and none were ticked* (a discipline finding);
`0 / 0` means **no rules were attached to that trade at all** (a missing-instrument finding). The
`AMD Playbook` on the same account already carries **10 rules across 2 groups** and would report a
denominator of 10.

So the council's `DON'T BUILD` verdict rested on a genuine `ZERO` — but a zero from an instrument that
had **no rules to measure against**. That is a `NOT-RECORDED`, not a `ZERO`, and this page is what
converts it.

### Expanding the playbook later is safe — the aggregate is not

Because **follow rate is computed per rule**, adding a rule in month two does not corrupt the follow
rate of a rule that existed in month one. What *does* change is the per-trade aggregate `X / N`.

**So: never compare `Rules followed X / N` across a playbook edit.** Compare per-rule follow rates,
which survive it. Record the date of any playbook change in the strategy `Notes`.

---

## Strategy identity — paste verbatim

**Name**

```
Aura - Sequential SMT (NQ triad)
```

**Description**

```
dOoMeR's Sequential-SMT model traded on the indices triad NQ/ES/YM plus 6S as the Aura Asset. Mark swing points, SMT-qualify them, build ranges by the expansive-move method, target the liquidity inside gaps in a range's discount/premium, confirm with Sequential SMT nested across at least two adjacent cycles, cascade HTF to LTF into a 5m inverse-FVG entry, and manage risk as it evolves. Every rule below is numbered to the Aura rulebook (R1-R54), so a per-rule follow rate maps back to exactly one rule.
```

---

## ⭐ The key data to track — and the half Tradezella already does for you

[[concepts/aura/journaling-system]] gives dOoMeR's own field list, and splitting it against what the
product captures automatically is what tells you where to spend effort. He is explicit that the survey
reason people quit journaling — *"I don't know what to track"* — is an **instruction problem, not a
motivation problem**, so this is the instruction.

### Tier 1 — the essentials. **Tradezella captures all of these for you.**

Date · session/time · entry price · exit price · stop-loss · target · R:R · result in R.

**Do not re-type any of it.** It is recorded from the trade itself, and the `Orders` table already
carries open/close time and average entry price. The only Tier-1 item needing a deliberate act is the
**screenshot** — and per [[concepts/mastery/aura/chart-markup]] §3, take it *before* stepping the replay
past the setup, because a replay that has moved on cannot be un-moved.

### Tier 2 — setup identity. **Your job, via `Tags`.**

Which *kind* of setup this was, so expectancy can be sliced by setup type rather than by feel. The
vocabulary is below (§Tags). This is dOoMeR's "Setup" field.

### Tier 3 — process adherence. **Your job, via `Rules followed`.**

The 32 rules above. This is the *"did you follow your rules?"* field, made per-rule and therefore
measurable rather than a yes/no feeling.

### ⭐ Tier 4 — the psychological layer. **Your job, and nothing captures it automatically.**

dOoMeR is explicit that this is where the value is: *"the numeric fields tell you what happened; this
layer tells you why."* Four fields, per trade, into the trade note:

- **Emotion before / during / after** — three separate readings, not one.
- **Was this trade in your plan? If not, what triggered you to take it?**
- **If a rule was broken — why?** (the rule tick records *that*; only this records *why*)

If you record nothing else by hand, record these. Tier 1 is free, Tier 4 is the entire reason the
journal changes behaviour rather than just describing it.

### Tier 5 — the comparisons that actually produce findings

Three specific analyses the course names, each of which needs a datum you must deliberately capture:

| Analysis | What it needs | Why it matters |
|---|---|---|
| **Active management vs. walking away** | The `MANAGED` / `SET-AND-LEFT` tag | Called out as one of the most important comparisons available. If the data shows you make *less* by managing, that is — his words — your personal holy grail: more money for less work. |
| **Time-of-day clustering** | Nothing — `Open time` is automatic | His worked example: *"if 80% of your losses come from taking trades after 11:00am, that's not a feeling, that's evidence."* His own accumulated finding was to wait for 9:30 NY **plus 5–10 minutes**. |
| **Missed and cancelled trades** | A deliberate log — see §The gap below | Dante's single biggest edge was found only because someone tracked his **cancelled** orders. This is the highest-value category and the one with no automatic capture at all. |

**Count the missed trades that would have LOST, too.** The instruction is explicit, and it is the
whole difference between a record and a highlight reel: *"count how many of these would have been
losers alongside the winners."* A missed-trade log containing only the ones that got away is a machine
for manufacturing regret.

## The scope decision: what belongs in the playbook

`Rules followed` is recorded **per order**. So the playbook holds the **per-trade gates only** —
phases 1–6 of [[concepts/mastery/aura/checklist]].

**Phases 0 (pre-market readiness) and 7 (post-market review) are per replayed *day*, not per trade.**
Putting them in the playbook would record the same answer once per trade, weighting busy days more
heavily and quietly turning a discipline measure into a trade-count measure. They live instead in the
session `Description` (written before the replay advances) and the day's `Notes` — and in the runner.

---

> **Paste these verbatim.** The `R##` prefix is the whole mechanism — it is what makes a follow rate map
> back to exactly one rule in [[concepts/mastery/aura/rules]], in both directions, and it survives
> Tradezella's own drag-reordering. Keep every row on the `Always` outcome filter.

## Group 1 · HTF framing (once per replayed day) — 7 rules

| # | Playbook rule text (paste verbatim) | Aura |
|---|---|---|
| 1 | `R4 - Range marked by the expansive-move method between two swing points, not a time-based range` | R4 |
| 2 | `R5 - Zones read as discount / equilibrium / premium only, no quadrants` | R5 |
| 3 | `R3+R8 - Range extremes anchored on SMT-qualified swings; where a swing looks false, prefer the level swept on ALL triad assets` | R3, R8 |
| 4 | `R7 - Current range still valid: no opposing and no same-cycle Sequential SMT has formed` | R7 |
| 5 | `R27 - Walked the if-then cascade top-down and named the cycle chain (Monthly confirmed with Weekly first)` | R27 |
| 6 | `R12+R35 - Draw on liquidity named: the liquidity INSIDE a gap in the range's discount (long) / premium (short)` | R12, R35 |
| 7 | `R29 - HARD GATE: wrote BOTH what confirms and what invalidates the bias, before entry` | R29 |

**Row 4 (`R7`) was missing from the first draft of this page.** `sequential-smt.md` §Range lifecycle
makes it a live per-trade question — *keep following the current range until either an opposing
Sequential SMT or another same-cycle Sequential SMT forms* — so trading a range that has already been
ended is a distinct, checkable error with no other home.

## Group 2 · Confirmation — Sequential SMT — 6 rules

| # | Playbook rule text | Aura |
|---|---|---|
| 1 | `R17+R18 - Sequential SMT nested across at least 2 adjacent cycles on NQ/ES/YM plus 6S` | R17, R18 |
| 2 | `R20 - Confirmed by at least one of: cross-cycle nesting, gap SMT-fill, or candle-level SMT vs the prior candle` | R20 |
| 3 | `R21 - Cross-cycle gap-pairing checked (weekly to daily gaps, daily/session to 4H, micro to 15m-1H)` | R21 |
| 4 | `R24+R25 - Adjacent cycle missing: a valid Sequential Skip identified (further-down cycle, or the same setup on another triad member)` | R24, R25 |
| 5 | `R22 - SMT formed between two segments of a larger cycle: expect that larger segment's extreme to be taken` | R22 |
| 6 | `R19 - HARD GATE: accepted as probabilistic, not treated as certain` | R19 |

**Row 5 (`R22`) was missing entirely from the first draft.** It is the *targeting* rule —
`sequential-smt.md` §"The extreme of the range" states it and adds *"this goes for all cycles"* — and
without it the confirmation group tells you a signal is valid but never asks what it implies about
where price is going.

## Group 3 · Entry (per setup) — 8 rules

| # | Playbook rule text | Aura |
|---|---|---|
| 1 | `R30 - Entry on a confirmed 5m inverse FVG in the bias direction (plain FVG is the fallback)` | R30 |
| 2 | `R30 - Session-cycle Sequential SMT within discount (long) / premium (short) of the LTF range` | R30 |
| 3 | `R31 - News or skip setup: waited for the 9:30 NY open rather than chasing a pre-9:30 gap` | R31 |
| 4 | `R32 - R:R ceiling set from premium/discount position (lower R:R when entering in premium)` | R32 |
| 5 | `R33 - Stop at the invalidation level: high/low of the qualifying daily-cycle or 4H SMT, or the recent swing` | R33 |
| 6 | `R34 - Stop distance acceptable, or switched to a triad member with a tighter equivalent gap` | R34 |
| 7 | `R39+R52 - Risk sized 1-2% of TOTAL capital, computed in R; negative visualization done` | R39, R52 |
| 8 | `R50 - HARD GATE: fits my plan? defined in advance? trading the market, not my P&L?` | R50 |

## Group 4 · In-trade management (per setup) — 4 rules

| # | Playbook rule text | Aura |
|---|---|---|
| 1 | `R35 - Managed expecting price NOT to run cleanly to target; new ranges and SMT form on the way` | R35 |
| 2 | `R45 - Risk recalculated from CURRENT price, not entry; held at least 1:1 from here` | R45 |
| 3 | `R45 - Trailed as structure developed; no static stop, and breakeven is not "free"` | R45 |
| 4 | `R29 - Expected trigger failed to appear: treated its absence as invalidation and zoomed out` | R29 |

## Group 5 · Exit (per setup) — 3 rules

| # | Playbook rule text | Aura |
|---|---|---|
| 1 | `R36 - Exited at plan: HTF-range equilibrium, or held for liquidity in the HTF range's discount/extreme` | R36 |
| 2 | `R35 - Target was the extreme of the timeframe being played` | R35 |
| 3 | `R43 - Outcome recorded in R, not dollars` | R43 |

## Group 6 · Circuit breakers (checkable any time) — 4 rules

| # | Playbook rule text | Aura |
|---|---|---|
| 1 | `R40 - Not past 2 losses today` | R40 |
| 2 | `R40 - Not past the 2-3R daily stop` | R40 |
| 3 | `R49 - 10-minute rule honoured after any loss: charts closed, then zoom out to HTF before re-entry` | R49 |
| 4 | `R42 - Did not size up in drawdown` | R42 |

**Total: 32 rules across 6 groups. Six are hard gates** — a "no" on any of them means no trade, and
ticking one you did not actually satisfy is the single most damaging thing you can do to this dataset.

> **Thirty-two ticks per trade is heavy, and that is the drill.** [[concepts/mastery/aura/checklist]]
> says to run the whole checklist on every replay setup *precisely so it becomes automatic before live*.
>
> But there is a real hazard on the other side, and it is worth naming: **a rule you tick without
> reading is worse than no rule**, because it manufactures a 100% follow rate that measures nothing.
> If, after a week, you find yourself batch-ticking, cut to the six hard gates — per-rule follow rates
> mean the rules you keep stay comparable across the change, and you can add the rest back later
> without corrupting what you have already measured.

---

## Tags — description, not adherence

Rules answer *"did I follow the process?"*. **Tags answer *"what kind of setup was this?"*** — which is
what lets you slice expectancy by setup type instead of by feel. Keep the two vocabularies disjoint;
a tag that duplicates a rule double-counts.

| Tag | Means | Aura |
|---|---|---|
| `SMT-NESTED` | Adjacent-cycle Sequential SMT — the ordinary case | R18 |
| `SKIP-DOWN` | Sequential Skip via a further-down cycle | R24 |
| `SKIP-CROSS` | Cross-asset skip — same setup on another triad member | R25 |
| `IFVG` | Entry on an inverse FVG (the preferred entry) | R30 |
| `FVG-FALLBACK` | Entry on a plain FVG — the fallback, not the preference | R30 |
| `DISCOUNT` / `PREMIUM` / `EQ` | Where in the range the entry sat | R5, R32 |
| `PRE-930` / `POST-930` | Relative to the 9:30 NY open | R31 |
| `NEWS` | Scheduled news in the window | R31 |
| `ALT-ASSET` | Traded a triad member other than the primary | R25, R34 |
| `MANAGED` / `SET-AND-LEFT` | Did you actively manage it, or set stop+target and walk away? | R45 — and the pair that powers the single most valuable comparison in §Tier 5 |

Add a tag for the **replayed day's span label** (`1w`, `1m`, …) only if Tradezella does not already
expose the session — it does, via the session filter, so **do not** duplicate it as a tag.

## The gap: a day you correctly stood aside

**R51 says missing a trade is discipline, and R53 says journal the missed and cancelled ones.** But a
stood-aside day produces **no order**, so it can carry neither `Rules followed` nor `Tags`. The
instrument cannot see the behaviour the model most wants to reward.

- `OBSERVED`: the Strategies list has a **`Missed trades`** column, so a missed-trade concept exists.
  **`UNVERIFIED`:** how — or whether — one is logged from *inside a backtesting session*.
- **Until that is verified, log the stand-aside in Neurospect**, which already has the surface:
  `/journal/missed/new`. That keeps the honest zero visible somewhere, rather than nowhere.
- Also note it in the replayed day's `Notes`, so the Tradezella-side record is not silently empty.

This is the clearest case in the whole workstream of *a zero from an instrument that cannot see*. A
day with no orders and no note is indistinguishable from a day you never sat down for.

## See Also

- [[concepts/mastery/aura/tradezella-setup]] — creating the session the playbook attaches to
- [[concepts/mastery/aura/chart-markup]] — what to draw before any of these can be ticked honestly
- [[concepts/mastery/aura/rules]] — the canonical wording of every **R##** above
- [[concepts/mastery/aura/checklist]] — the phase order these groups mirror
