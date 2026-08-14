---
tags: [mastery, aura, tradezella, backtesting, session-setup, runner, neurospect]
aliases: [Tradezella Session Setup, Aura Session Setup, Backtest Session Setup]
sources: [concepts/mastery/aura/checklist.md, concepts/mastery/aura/rules.md, processes/distributed-workflow/active/aura-session-runner.md]
created: 2026-08-12
updated: 2026-08-12
---

# Tradezella Session Setup — the Aura backtest session

How to start a backtesting session that is **comparable to the last one**. Consistency is the whole
point: if the instrument, the symbols, the timezone or the data session change between runs, twenty
sessions produce twenty anecdotes instead of one dataset.

Every click-path below was **walked in the product on 2026-08-12** and is marked `OBSERVED`. Anything
not walked is marked `UNVERIFIED` and must not be followed as if it were fact.

> **Companion pages:** [[concepts/mastery/aura/tradezella-rule-mapping]] (what to tick and tag) ·
> [[concepts/mastery/aura/chart-markup]] (what to draw) · [[concepts/mastery/aura/checklist]] (the
> protocol itself) · [[concepts/mastery/aura/rules]] (the rules behind every **[R##]**).

---

## ⭐ The counting basis — declared before any number exists

This is stated **first and in writing** because a basis chosen after seeing the data is a conclusion
wearing a method's clothes.

| Term | Definition |
|---|---|
| **Session** | One sitting over a **declared replay span** — the `Start date` → `End date` pair entered when the session is created. The span is chosen *before* the replay is advanced, and never changed mid-session. |
| **Replayed day** | **The counted unit.** One trading day of replayed price, walked through checklist phases 0 → 7. |
| **Setup** | One worked entry opportunity inside a replayed day. Phases 3–5 repeat per setup. A day can hold 0..n setups. |

**Why the day and not the session.** A one-week session and a one-year session are not comparable, so
the session cannot be the unit. **A day on which you correctly stood aside still counts as a replayed
day** — R51 is explicit that missing a trade is discipline, not a loss, and any setup-counted basis
silently deletes those days from the record. That deletion is exactly the bias that would make a
twenty-session dataset flatter you.

**So B2's "~20 backtesting sessions" reads as ~20 replayed days**, which may be four sittings of a
trading week each. Record the span; count the days.

**What would fail to be counted:** a replayed day abandoned mid-phase (do not count it — mark it
abandoned); a day replayed twice (count once); a day where the market was closed (not a trading day at
all — the Jan 1 holiday sitting is the worked example, and it is why the first probe chart showed
almost no price).

---

## 0. Before the first session — one-time setup

- [ ] **The playbook exists and carries the Aura rules.** Build it from
  [[concepts/mastery/aura/tradezella-rule-mapping]] *before* the first session. This is the step B2 has
  never had — a session run against an empty playbook can only ever report `Rules followed 0 / 0`. **[R48]** ← hard gate
- [ ] Decide the **start balance** and keep it fixed across all sessions. `$50,000` is what the existing
  sessions use; leverage is fixed at 1:1. Changing it between sessions makes P&L incomparable — though
  R43 says judge in **R**, not dollars, which insulates you from most of this.
- [ ] Fix the **per-trade risk** in R terms: 1–2% of total capital. At $50,000 and 2%, 1R = $1,000. **[R39, R43]**

## 1. Create the session — `OBSERVED` click-path

- [ ] **Backtesting → `+ Create session` → `Backtest on your own`.** (The other option, `Automated
  backtest (BETA)`, has Zella AI run hundreds of trades from a plain-words description — that is not
  practice, and it defeats the entire purpose of this workstream.)
- [ ] Choose **`Start from scratch`**, not `Pick a scenario`. A scenario pins someone else's date range,
  symbols and playbook; the whole point here is that *you* declare the span. *(Scenarios remain useful
  later for a fixed shared drill — see §Scenarios below.)*
- [ ] **Session name** — required. Use the fixed convention so sessions sort and compare:
  `AURA · NQ · YYYY-MM-DD→YYYY-MM-DD · <span>`, e.g. `AURA · NQ · 2025-06-02→2025-06-06 · 1w`.
- [ ] **Description** — the pre-commitment. Write **before** advancing the replay: the span, what you are
  looking for, where, and what would make you stand aside. That is R48's three questions, and writing
  them here timestamps them against the session. **[R48, R26]** ← hard gate
- [ ] **Strategy** — select the Aura playbook. The form warns *"No strategy selected · Add one to track
  consistency and improve results"*, and it is right: **with no strategy attached there is no rule
  instrument at all**, and every order reports `Rules followed 0 / 0`.
- [ ] **Symbols** — **maximum 5**, `OBSERVED` in the form's own hint. Enter the indices triad:
  **`NQ`, `ES`, `YM`**. **[R16]** *(On the Aura Asset, see §The 6S problem below — do not block on it.)*
- [ ] **Start date / End date** — `MM/DD/YYYY hh:mm:ss`, to the second. This pair **is** the declared
  replay span. See §Choosing the span.
- [ ] **Start balance** — presets `5K / 10K / 25K / 50K / 100K / 250K`; leverage is 1:1. Keep it fixed.
- [ ] `Create session`.

### ⚠️ The 6S problem — and why it does NOT block you (2026-08-13)

**Paul reports `6S` is not offered in Tradezella's symbol search.** *(Not independently verified: the
in-session datafeed's `searchSymbols` is scoped to that session's own symbols — it returns the same four
regardless of the query, including for a nonsense string — so a "not found" from it would have been a
zero from an instrument that cannot see. Paul's observation stands; the catalogue was not checked.)*

**Start with the three-leg triad and do not wait.** R16 defines the indices triad as **ES / NQ / YM** —
that is the complete divergence set, and R18's Sequential SMT operates on the triad. **R17 adds 6S as a
*fourth* leg and is itself `flagged`**: dOoMeR calls the origin story his own speculation and rests the
case on chart behaviour, not theory. So the Aura Asset is an enhancement, not a prerequisite, and the
5-symbol limit leaves room to add it later without losing anything.

### ✅ RESOLVED 2026-08-13 — `CHFUSD` exists, and it is the correct one

Paul found `CHFUSD` in the symbol search (a **filter was suppressing results**, which is also why the
first automated attempts found nothing — the failure was a UI filter, not only automation). Session
`831607` was created with **`NQ` `ES` `YM` `CHFUSD`** and all four load data.

**The direction question is settled empirically, not from memory:** `CHFUSD` printed **1.2139** — a
franc costing $1.21, i.e. **USD per CHF**, which is 6S's convention. `USDCHF` would have printed ≈0.82.
**Use `CHFUSD`.** Tradezella reports it as `spread_type: "forex"`.

> ⚠️ **Open, and the reason S1c must test it: candle alignment.** On first load, `CHFUSD` bars ran to
> `2025-06-01 21:00` while `NQ`/`ES`/`YM` stopped at `2025-05-30 20:59` — a ~2-day coverage difference.
> That may be nothing more than different fetch windows, **or** it may be exactly the sync problem that
> disqualified DXY (R17). **Not concluded.** Test it properly by comparing candle *boundaries*, not
> coverage, via `exportData` timestamps.

**If a substitute is ever reconsidered, two facts decide it — and the first is a trap:**

1. **Direction. `6S` is the CME Swiss Franc future, quoted USD per 1 CHF — i.e. it is `CHF/USD`.**
   `USD/CHF` is the **inverse** and moves the opposite way, and it is the conventional quote most feeds
   default to. Substituting `USDCHF` would invert every divergence read — plausible-looking and exactly
   wrong. Only a **USD-per-CHF** quote — i.e. `CHFUSD` — is directionally equivalent to 6S.
2. **⭐ Candle synchronisation — R17's ACTUAL stated criterion.** 6S was chosen over DXY *"because DXY's
   candles aren't sync'd to the traded futures."* So the test a substitute must pass is **not** "does it
   move the same" but **"do its daily/weekly candle boundaries align with the CME futures session?"** A
   spot-forex feed can be directionally identical and still fail this, which would reintroduce precisely
   the defect R17 rejected DXY for. Spot forex and CME FX futures also differ by **carry/forward points**
   (a small, drifting basis) and futures carry **quarterly roll discontinuities**.

**How to settle it when it matters:** put the candidate on a chart beside `NQ` and compare *candle
boundaries*, not just direction — the same `exportData` comparison used to test MNQ. Until that is done,
treat any substitute as **UNVERIFIED** and run the three-leg triad.

### ⚠️ The symbol mistake already on the account

The existing session `NQ Macro Po3 - Asia Session` carries **`NQ`, `MNQ`, `ES`, `MES`**. `MNQ` is the
micro contract of `NQ` and `MES` the micro of `ES` — they are the *same instrument at a different
multiplier*. **Two of the four panes are duplicates, and a divergence between `NQ` and `MNQ` is
impossible by construction.** The confirmation engine (R18) has nothing to read. Use `NQ` `ES` `YM`.

### Choosing the span

The span is configurable and that is deliberate — but declare it up front and keep the *sitting* honest.

| Span | Replayed days | Use it for |
|---|---|---|
| `1w` | ~5 | The default. One sitting, one trading week, phases 0→7 five times. |
| `1m` | ~21 | A monthly-cycle read; the HTF cascade has room to actually turn over. **[R27]** |
| `3m` / `6m` | ~63 / ~126 | Quarterly framing; expect several sittings — the span is the container, not the sitting. |
| `1y` | ~252 | Only once the protocol is automatic. Do not start here. |

**Start at `1w`.** Twenty replayed days is four weekly sittings, which is a reachable B2 sample rather
than an aspiration.

## 2. Configure the chart — `OBSERVED`

Done once per session; the layout reports **`Autosaved`** in the top bar.

- [ ] Confirm the **multi-symbol layout** shows `NQ`, `ES`, `YM` — one symbol per pane. The
  panes are what make SMT readable at a glance. **[R18]**
- [ ] Open **chart settings (gear) → Symbol** and set **Timezone = `(UTC-4) New York`**. Every time
  reference in the Aura model is a New York time — the 9:30 open in R31 above all. A chart on another
  timezone silently invalidates the entry rule.
- [ ] Set **Session = `Extended trading hours`** (ETH). The status bar should read `ETH`. Keep it
  identical across sessions — RTH and ETH produce *different gaps*, and gaps are what the model targets.
  **[R11, R12]**
- [ ] Use **`Apply to all`** so all four panes share the settings, then **`Template ▾` → save** so the
  next session starts identical. `OBSERVED` — the Template control is in the settings dialog footer.
- [ ] Set the working timeframe for framing. The cascade is
  Monthly→Weekly→Daily/Session→4H→15m→**5m** (5m preferred over 3m: 3m setups fail more often). **[R27]**

## 3. Run the replay — `OBSERVED`

- [ ] Replay controls sit under the charts: **speed (`1x`)**, **step back**, **play**, **step forward**,
  **jump-to**, and a **bar-interval selector** (`10sec` on the existing session).
- [ ] **Step, do not play.** Playing at 1x is watching; stepping is deciding. The protocol is a sequence
  of decisions, and a decision you did not have to make is a rep you did not do.
- [ ] Trade entry is the **`QTY` + `Buy` / `Sell`** panel at bottom right. Positions appear under
  **`Orders` / `Open Positions` / `Closed Positions`**.
- [ ] The `Orders` table carries **`Rules followed`** and **`Tags`** per order — the two fields that make
  this measurable. See [[concepts/mastery/aura/tradezella-rule-mapping]].

## 4. Close the session

- [ ] Phase 7 of [[concepts/mastery/aura/checklist]] — the post-market review — happens **per replayed
  day**, not once at the end of a 1-year span. **[R53]**
- [ ] Record the day's review in the strategy's **`Notes`** tab or the **`Notebook`**. `OBSERVED` — both
  exist; the exact field shapes inside them are `UNVERIFIED`.
- [ ] **Never miss twice.** One skipped review is an accident; two is a habit. **[R53]**

---

## Scenarios — what they are, and when they help

`OBSERVED`: a **scenario** is a saved starting point carrying a **date range, symbols and a playbook**
(e.g. *"NQ Liquidity Sweeps & Displacement · Jun 27 → Jun 13, 2025 · NQ, MNQ"*). Scenarios can be
authored by you or by TradeZella, and the strategy page has its own `Scenarios` tab.

They are the wrong tool for **building** the habit (they pin someone else's span) and the right tool for
**re-running a fixed drill** — the same week, twice, months apart, to measure whether the protocol
actually became automatic. Park that until S1 has produced sessions.

## What is NOT verified

Recorded so no future session mistakes an inference for a measurement:

- **`Mistakes`, `Rating` and `Reviewed` fields** — assumed by the workstream tracker, **never observed**
  in the backtesting order surface. Only `Rules followed` and `Tags` were seen on the `Orders` table.
- **The `Notebook` and strategy `Notes` field shapes** — the surfaces exist; their contents were not opened.
- **Whether drawings persist across replay steps and across sessions** — see
  [[concepts/mastery/aura/chart-markup]] §The probe. `Autosaved` is displayed, which is evidence, not proof.
- **The `Backtest Scenarios` and `Templates` tabs** on the Strategies page — seen, not opened.

## See Also

- [[concepts/mastery/aura/tradezella-rule-mapping]] — the rule→playbook mapping (what makes B2 measurable)
- [[concepts/mastery/aura/chart-markup]] — the drawing protocol and the indicator probe result
- [[concepts/mastery/aura/checklist]] · [[concepts/mastery/aura/rules]]
- [[concepts/aura/triads-asset-selection]] · [[concepts/aura/aura-asset]] — why the triad is ES/NQ/YM + 6S
