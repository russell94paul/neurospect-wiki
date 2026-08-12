---
tags: [distributed-workflow, active, neurospect, backtesting, integration, tradezella, learning-science, product-market-fit, research]
aliases: [Backtest Companion Tracker, Tradezella Lane, Companion Positioning Workstream]
sources: []
created: 2026-08-10
updated: 2026-08-12
---

# Backtest Companion — Workstream Tracker

Make `neurospect-learn` improve **backtesting sessions that happen in another tool**: consistency and
discipline while the session runs, capture and storage of what came out of it, and insight across sessions —
and use that as the wedge for a broader **companion** positioning, integrating with the trading apps a trader
has already chosen rather than replacing them.

> **STATUS (2026-08-11): STILL SCOPED ONLY — no research done, no design decided, no code written.** This
> tracker exists so the first session starts from the real question rather than a blank page. Nothing in this
> document is a finding about Tradezella, the market, or the literature; everything in it is a question or a
> constraint.
>
> **The skill-authoring session is DONE (2026-08-11).** `⛏ prospect` now exists at
> `C:\Users\PaulRussell\.claude\skills\prospect\` — the divergent fifth council sibling, boundary-first and
> able to halt. It was dry-run against the 17 open questions below, which **changed how B1 should be briefed**:
> three of the 17 are internal design questions no external lens should touch, one needs splitting, and the
> skill asks three questions the 17 do not. See §Dry-run of `prospect` against the 17 questions.
>
> **⭐ B1 IS COMPLETE (2026-08-11) AND THE ANSWER WAS NO.** Gate 3 returned `OPEN`; the five-lens `⛏ prospect`
> council returned **DON'T BUILD the Tradezella importer**. Read **§COUNCIL VERDICT** before anything else on
> this page — several sections above it were written while the bet was still open and read as though it were.
>
> The one-line reason: **the boundary is `OPEN` and points downstream, while both genuine differentiators
> (pre-trade intent, behavioural scoring) live upstream of it.** The decisive evidence was a measurement, not
> an argument — three shipped, free, one-click discipline instruments inside Tradezella all read **genuine
> ZERO** for the only user, with the instrument proved live.
>
> **⭐ B3 IS CLOSED (2026-08-12) — but locally, not hosted.** Paul decided **hosting is premature**;
> `neurospect-learn` now runs as a one-command **local Docker daily driver** (`docker compose up -d`,
> :8001 / :5174), render-verified with 12 artifacts in `api/docs/evidence/b3-local/`. The Render + R2 path
> stays written and proven but **PARKED and unprovisioned** — the B3b boot prompt is retired **unrun**, and
> executing it would spend money against a reversed decision.
>
> **⭐ THIS TRACKER NO LONGER HOLDS THE ACTIVE LANE (2026-08-12).** B4 was **absorbed as S2** of
> [[processes/distributed-workflow/active/aura-session-runner]] — the screen Paul keeps open beside
> Tradezella and follows every session. Go there for the active boot prompt (**S1**). This page remains the
> canonical record of the B1 council verdict, the boundary facts, and B3's local close.
>
> **B2 still sits before everything and is Paul's own work, not a session's**: define rules in the Playbook
> Rules tab and run ~20 backtesting sessions using the in-product fields that already exist. That test is
> free, gates everything else — including B4 — and **has still not been run**.
>
> Boundary facts expire. This verdict is scoped to **2026-08-11, Pro tier**; Tradezella ships weekly — see
> §The re-check trigger before acting on this page after ~2026-11.
>
> **Why this lane, and why now.** [[processes/distributed-workflow/active/learning-enforcement]] closed on
> 2026-08-10 with E1–E6 complete, and its retrospective recommended the repo-integration lane next. Paul
> redirected the same day: the backtesting tool is now **Tradezella**, chosen and kept, and the question is
> what `neurospect-learn` becomes around it. That is a **positioning change** — see
> [[concepts/roadmap/ideas/backtest-companion-layer]] — so it takes precedence over integration plumbing.

## Goal (Paul, 2026-08-10 — in his framing)

> "I will be using Tradezella for backtesting, but I am wondering how I can use the neurospect-learn platform
> to improve my backtesting sessions, increasing consistency and discipline and gathering, storing and gaining
> insights from my backtests etc."
>
> "I am trying to see how I can increase the product market fit of this platform so it can integrate in
> innovative ways with existing trading apps or platforms for different purposes."

Three deliverables follow, and they are deliberately in this order:

1. **What can actually cross the boundary** — established as fact before anything is designed.
2. **What the platform should become** around a backtesting session it does not host, grounded in evidence
   about the incumbent, the market, and how people actually learn skills.
3. **A build split** into boot-promptable phases, the way E1 produced E2–E6.

## The asset this lane is built on — do NOT redesign it

`neurospect-learn` already ships something no journaling tool has, and this lane's whole value rests on it.
Canonical in [[concepts/architecture/learning-enforcement]]; summarised here only so the first session does not
rediscover it:

- **`reps` are DERIVED from evidence** — no endpoint can mint one (E2).
- **Every capture is checked against the drill's own wiki-projected bar**, and an unchecked rep still counts —
  a grade may flag but never retract (E3).
- **An advisory AI second reader** that never blocks and never retracts, with a closed-enum verdict schema in
  which a numeric price claim is unrepresentable (E4).
- **A frozen pre-commitment ledger + calibration score** — a call cannot be back-dated, edited, re-resolved or
  deleted, and the score is scale-invariant so more reps cannot inflate it (E5).
- **Computed-per-read honesty signals that gate nothing and store nothing**, and an evidence-backed streak
  published beside the self-reported one (E6).
- **The Readiness-to-Live Gate is non-overridable** and computed per read.

A backtesting tool records *what you did*. This is the only thing in the stack that can say whether the work
was **actually done**, whether it **met its own bar**, and whether the call **preceded the outcome**. That is
the wedge; anything this lane designs should sharpen it rather than dilute it into a second journal.

## Open questions B1 must answer (or explicitly defer, with a reason)

Recorded now so the research session starts from the real problem. **None of these are decided, and none of
the phrasing below should be read as a hypothesis to confirm.**

**Boundary — the facts that change the shape of everything else**
1. What does Tradezella expose? Public API, OAuth, webhooks, CSV/Excel export, nothing? With which fields?
2. What does its **ToS** permit — automated access, scraping, derivative storage of a user's own data?
3. Is there a partner/integration/affiliate programme, or public evidence of third parties integrating?
4. If the only path is **manual export**, what is the least-friction honest flow, and is it good enough?
5. Does any of this make **hosting a prerequisite** for the first time? (Decision #4 of 2026-07-28 held it was
   not, *because* every drill is desktop TradingView bar-replay and capture is paste-first. A third-party
   integration may break that premise — say so loudly if it does.)

**The incumbent — seams, not feature lists**
6. What does Tradezella's backtesting flow actually look like end to end, and what does it deliberately NOT do?
7. Where do its users say attention leaks — reviews, communities, churn reasons, feature requests?
8. What does it charge, and what does that imply about what a companion can ask for?

**The session — where discipline is actually won or lost**
9. What does a *good* backtesting session look like, concretely, and which parts are behavioural rather than
   analytical? (This is where the enforcement layer plugs in, if anywhere.)
10. What should be captured **before** a session (a plan, a pre-commitment), **during** it (adherence, pacing),
    and **after** it (a scored review) — and which of those is already covered by E1–E6 primitives?
11. How do backtest sessions relate to the existing `journal_entries.mode = 'backtest'` and the Gate's
    ≥50-sample expectancy requirement? Is this a new data model or a new *source* for the existing one?

**Learning science — the part most likely to go wrong**
12. Which findings are robust enough to design on? Expect: spaced retrieval / the testing effect, interleaving,
    desirable difficulties, feedback timing, implementation intentions, self-explanation. Expect to **reject**:
    learning styles, left/right-brain, "10,000 hours" as a law, and dopamine-loop justifications for streaks.
13. What does the literature say about **deliberate practice in domains with noisy, delayed feedback** — which
    trading is, and which is why most "practice more" advice fails here?
14. Does anything in it contradict what this platform already built? (Deci/Koestner/Ryan 1999 is already
    load-bearing: no XP, no badges, no points. A finding that overturns it must be strong and stated.)

**Product-market fit — held to the analysis gate, not to enthusiasm**
15. Who is the user beyond Paul? **n=1 today** — every number in the E1–E6 arc came from fixtures. Any PMF
    claim needs external evidence or must be labelled a hypothesis.
16. Is this a product or a feature? The kill-shot question: what stops Tradezella shipping it themselves?
17. Which *other* platforms does the companion positioning generalise to, and does designing for two make the
    first one worse?

## Gate 3 — Boundary probe (2026-08-11): **VERDICT `OPEN`** — answers Q1, Q2, Q3a, Q5

Run with `⛏ prospect`'s Gate 3 before any council was convened, on Paul's **reactivated Pro account**.
This section is the boundary contract B1 must design against. **It supersedes any inference from the
public docs — including two of my own, both of which were wrong.**

```
BET:            Can neurospect-learn improve backtesting sessions hosted in Tradezella?
DIRECTION:      ONE-WAY, OUT, BY FILE. Nothing goes back in.
MECHANISM:      Manual CSV export. NO API, NO OAuth, NO webhooks, NO developer programme.
OBSERVED ON:    Pro plan ($59/mo) · web app · 2026-08-11 · Paul's own account
PAYLOAD:        48 columns, 39 populated on a real futures trade (see below)
TERMS:          ToS effective 2020-10-29 — §7 permits "a single copy made for personal use only";
                §20 forbids use "for any commercial purposes". Automated access: NO CLAUSE EXISTS.
LIMITS:         Per-trade rows only. No session linkage, no notes, no images, no stable ID.
VERDICT:        OPEN (narrow in shape — a file hatch, not an integration)
RE-CHECK:       Any pricing-page change, any ToS revision (it is 6 years stale and WILL be rewritten),
                or the appearance of a developer/API page. Re-run this probe before B2 builds anything.
```

### The path, exercised end to end (`OBSERVED`)

`Backtesting → Trade View → [select rows] → Bulk actions → Export trades to CSV → All columns → Download`

- **Positive control:** the export returned Paul's real data — 2 sessions, 1 trade, 8m invested. A null
  result here would therefore have meant something.
- **Negative control:** `Backtesting → Sessions → Bulk action` offers **only `Delete` and
  `Add to strategies`**. The export is trade-level, not session-level. Same UI idiom, different menu —
  which is what makes the positive finding discriminating rather than incidental.

### The export surface, enumerated (2026-08-11, Pro, manual backtesting only)

| Surface | Export? | Evidence |
|---|---|---|
| Sessions | ✗ | Bulk menu = `Delete` / `Add to strategies` |
| **Trade View** | ✅ **the only data crossing** | `Bulk actions → Export trades to CSV` |
| Reports | ✗ | The `…` control is a *which-stats-to-display* picker |
| Notebook | ✗ | No export control |
| Session results → Trade Log | ✅ same control, session-scoped | Same `Bulk actions`, session filter applied |
| Share (session dashboard) | **image only** | `Style image` · `Download image` · `Copy image`. **No URL, no hosted page** |

⚠️ **SCOPE CORRECTION to the line above.** "The only export surface" is true of the surfaces **reachable
with zero automated-backtest runs**, which is Paul's state — *not* of everything the product has.
First-party docs describe a **separate `Export CSV` button in the Automated Backtesting Trade Log**
(help art. 16140732), which could not be reached without spending a Pro run. Unresolved, and deliberately
so: Paul does **manual** backtesting, so that surface informs **Bet B only**. Recorded because an
unqualified "only" would have been an over-claim.

### ⭐ Per-session export IS achievable — the session identity rides on the filter, not the data

The session-scoped Dashboard (`⋮ → Session results`) has its own `Trade Log` tab with the same
`Bulk actions`, and a session filter in the top right. So: **filter to one session → select → export.**

**Consequence for the design:** the file still contains no session identifier, so the *importer must be
told* which session it is receiving, and importing two sessions in one file makes them permanently
unseparable. A one-session-per-import discipline is therefore a hard requirement, not a nicety.

### Tradezella already ships a rules/adherence mechanism — and Paul has not used it

`Strategies → <playbook> → Rules` offers "groups and rules"; per the help centre a trader defines rules
up front and ticks compliance **on a completed trade**, after the fact. Paul's `Macro Model` playbook
("Liquidity Sweep at Key Levels + iFVG/CISD + Strong Displacement") reads **"No Strategy Rules"**, and
his `Backtesting Session Notes` folder is empty.

**Both halves of that matter and they cut in opposite directions.** The discipline space is *not* empty —
which is `devil`'s material. But the mechanism is self-reported and post-hoc, structurally unlike E5's
frozen ledger, and the "Rule Adherence Score" exists **only in marketing copy**, never in the 42-article
help centre (`MARKETED`, therefore not a design premise).

**NOT-DETERMINED, and the access is named:** whether a ticked rule-checkmark can be **re-toggled later**.
Testing it requires creating rule groups in Paul's live account and ticking adherence on his real trade —
a write to his data, so it was not done. This is the question of whether Tradezella has anything
resembling a frozen commitment, and it needs one sentence of permission to settle.

### Other boundary facts established

- **CSV export is NOT tier-gated.** Manual backtesting is available on Essential ($35), and it populates
  the same Trade Log. Automated backtesting is the Pro/Ultra gate (10 / 100 runs per month).
- **Strategy-level peer sharing exists** (`Shared with me` tab, `Shared strategies` column) even though
  *session* sharing does not — the session-sharing help article still says "under development… coming
  weeks" and is dated **September 2024**, i.e. ~23 months stale. Docs rot is the norm here; re-check.
- **Tradezella tracks "Missed trades"** as a strategy-level column, overlapping `neurospect-learn`'s own
  missed-trade log.
- **No API, no Zapier/Make/n8n connector, no confirmed mobile app.** `api.tradezella.com` resolves to a
  bare branded page with no developer surface.

### ⭐ Two things the public docs got wrong — both caught only by pressing the buttons

1. **The 42-article "Backtesting & Replay" help collection contains NO export article at all**, and the
   Sessions tab genuinely has no export. Reading the docs, the honest verdict was `NARROW`/possibly
   `CLOSED`. **The capability exists anyway**, one tab over. `DOCUMENTED` was not `OBSERVED`, in the
   direction that *understates* — the opposite of the usual failure, and worth recording because it is
   the one a sceptical researcher walks into.
2. **A vendor claim was directionally right for the wrong reason.** Tradezella's marketing blog says
   backtested trades land in "the same journal" and can be exported. The help centre says backtesting
   data lives in a **separate dedicated section** — and the help centre is right: the export carries
   `Account Name = Backtesting`. Had the design leaned on the blog's "same journal" framing it would
   have looked for these rows in the wrong place. **`MARKETED` was not usable even when its conclusion
   was true.**

### The payload — 48 columns, verbatim

`Account Name · Adjusted Cost · Adjusted Proceeds · Avg Buy Price · Avg Sell Price · Exit Efficiency ·
Best Exit · Best Exit Price · Best Exit Time · Close Date · Close Time · Commission · Custom Tags ·
Duration · Entry Price · Executions · Exit Price · Gross P&L · Trade Risk · Initial Target · Instrument ·
Spread Type · Mistakes · Net P&L · Net ROI · Open Date · Open Time · Pips · Reward Ratio · Points ·
Position MAE · Position MFE · Price MAE · Price MFE · Realized RR · Return Per Pip · Reviewed · Side ·
Status · Playbook · Symbol · Ticks Value · Ticks Per Contract · Fee · Swap · Rating · Quantity ·
Zella Score`

**39 populated** on a real NQ futures trade. **9 empty:** `Exit Efficiency`, `Best Exit`, `Best Exit
Price`, `Best Exit Time`, `Pips`, `Return Per Pip` (the last two are forex-only and legitimately N/A on a
futures trade), plus `Custom Tags`, `Mistakes`, `Rating` — which are **user-entered and simply unfilled**,
not unavailable. That distinction matters: the qualitative/behavioural fields *do* cross, if the trader
populates them.

**What crosses that the enforcement layer can actually use:** `Account Name = Backtesting` (a machine
discriminator for backtest rows), `Playbook` (= the strategy — the link to the model-aligned journal),
`Reviewed` (a boolean review flag), `Realized RR` / `Reward Ratio` / `Initial Target` / `Trade Risk`,
`Position MAE`/`MFE` + `Price MAE`/`MFE`, `Duration`, `Executions`, and `Mistakes`/`Custom Tags`/`Rating`
when filled.

### ⭐ What does NOT cross — and the one that changes the design

Verified absent from the header, not assumed: **no trade ID or stable unique key · no session ID or
session name · no notes/Notebook text · no screenshots or chart images · no record-creation timestamp.**

1. **⭐ The export carries SIMULATED market time, not wall-clock work time.** `Open Date = 2026-01-01`,
   `Open Time = 19:08:29 EST` are the *replayed historical bar times*, not when Paul sat down and did the
   work. The Sessions UI knows the real figure — it shows `Time spent 6 min` and `Time invested 8m` — but
   **that number is session-level and does not appear in the trade export at all.**

   **This is decisive.** [[concepts/architecture/learning-enforcement]]'s E5 pre-commitment ledger and E6
   evidence-backed streak both rest on *when the work actually happened*. A CSV row dated 2026-01-01
   cannot tell you whether the rep was done today, and cannot establish that a call preceded an outcome.
   **An import that trusted `Open Date` would silently back-date every rep** — precisely the failure E5's
   frozen ledger was built to make structurally impossible. Any B2 design must take the work-time from
   the *act of importing* (or from a session-level capture), never from the row.

2. **No session linkage** means a trade cannot be tied back to the plan or pre-commitment made for that
   session from the CSV alone. Session-level context (name, strategy, date range, time spent, completion)
   lives only in the Sessions table and is **not exportable** — it would have to be captured separately.

3. **No stable ID** means re-import is not idempotent by construction; de-duplication would have to be
   synthesised from a composite key. Compounded by their own documented constraint: *"the exported CSV
   file cannot be re-uploaded back into the platform."*

### The ToS finding — the bet splits in two

Read in full and rendered (the earlier fetch returned only a JS shell; **that was NOT-VISIBLE, not
silence**, and was re-routed rather than reported as "unrestricted").

- **§7:** *"Except for a single copy made for personal use only, you may not copy, reproduce, modify,
  republish, upload, post, transmit, or distribute any documents or information from this site."*
- **§20:** *"You agree not to sell, resell, reproduce, duplicate, copy or use for **any commercial
  purposes** any portion of this site, or use of or access to this site."*
- **Genuinely ABSENT** (whole document read): no clause on automated access, bots, scrapers, crawlers,
  rate limits, reverse engineering, or API terms. Not permitted, not forbidden — **no clause exists.**
- Effective **2020-10-29**, which **predates the backtesting feature entirely**. Treat as volatile.

**Consequence for the lane, stated plainly:** Paul's own personal use is squarely inside §7. A
**commercial** companion product sold to other Tradezella users runs into §20 and would need written
permission. The two halves of Paul's goal — *"improve my backtesting sessions"* and *"increase the
product-market fit of this platform"* — therefore have **different boundary verdicts**, and B1 must
decide which it is designing for rather than treating them as one bet.

### Still open after this gate

`Q3b` (has anyone built and *abandoned* a Tradezella companion — the `TRIED-AND-FAILED` check) and all of
the incumbent/learning-science/demand/kill-shot questions. Those need the council.

## ⭐ COUNCIL VERDICT (2026-08-11) — **DON'T BUILD THE IMPORTER.** Bet A redirected, Bet B dead.

Five lenses ran with `⛏ prospect` after Gate 3 returned `OPEN`. **`OPEN` was the right boundary verdict and
it does not save the bet** — that distinction is the whole finding, and it is the failure mode the skill
was written to catch: *a beautiful design for a boundary that opens onto the wrong thing.*

| Lens | Verdict |
|---|---|
| `claimant` — boundary | Weakens anything beyond CSV. Share is an image, not data. No API, no connector, no inbound path. |
| `scout` — incumbent | **Supports the premise.** No pre-trade intent capture anywhere; Zella Score is 100% P&L-derived. The gaps are real. |
| `scholar` — literature | **Supports Bet A, weakens Bet B.** The frozen ledger has the strongest evidential warrant in the platform — but for a different reason than assumed. |
| `canvasser` — demand | **Weakens Bet B.** Tradezella's own feature board: 0 of the top 10 requests concern discipline. Bet A untouched (n=1). |
| `devil` — kill-shot | **KILLS.** |

### The convergence that decides it, reached from two independent directions

- **`devil`:** the two genuine differentiators (pre-trade intent, behavioural scoring) sit **upstream** of a
  **downstream-only** crossing. *The gap is real and the crossing cannot reach it.*
- **`scholar`, independently and from the literature:** what a companion **can** deliver is cue-usage (`CI`)
  and **consistency**; what the evidence says actually drives improvement is **task information (`TI`)** —
  which needs ground truth about which cues predict, and is out of reach. And CI/consistency require data
  captured **during** the session, which the export does not carry.

Two lenses, different evidence bases, same conclusion: **the value is upstream of the export.** This is not
correlated brief-error — `scholar` reached it from meta-analyses that never saw the brief's product facts.

### ⭐ The decisive measurement: three live instruments, all reading genuine ZERO

`devil`'s strongest finding, and it is a **measurement**, not an impression. Three shipped, free, one-click
discipline surfaces exist inside the tool Paul already pays $59/mo for:

1. `Mistakes` / `Custom Tags` / `Rating` — **empty**
2. Playbook → Rules — **"No Strategy Rules"**, none defined
3. Backtesting Session Notes folder — **zero notes**

Against 2 sessions, 1 trade, 8 minutes. **The instrument is PROVED LIVE** — a trade completed, so the fields
rendered and would have recorded input. Per the estate rule, these are **ZERO**, not `NOT-RECORDED`.

**The implication is not "weak demand" — it is counter-evidence, and it inverts the order of operations.**
You build the automated version because the manual version is being done so often it hurts. Here the manual
version has **never been done once**, at zero cost. And with zero rules defined, an adherence-grading layer
would import a CSV and **grade it against nothing**.

### ⭐ The contamination argument — why this is worse than underdelivering

The six E-phases are worth something **precisely because no endpoint can mint a rep.** A CSV importer *is*
that endpoint: reps derived from a file the user hand-produced, at a time they chose, with a column set they
selected, carrying **no key, no wall-clock stamp, no attestation**. In a replay the outcome already exists in
history, so a "pre-commitment" can be authored *after reading the answer* with no ordering evidence in the
file.

**That is self-report in CSV clothing, rendering with the authority of "evidence-backed."** The bet does not
merely underdeliver — it launders assertion through the one property that made the platform credible.

### The incumbent shipped into this exact space during the research window — VERIFIED

Orchestrator re-verified `devil`'s claim directly at https://tradezella.canny.io/changelog (2026-08-11).
Confirmed, and **understated**. Weekly release cadence:

| Date | Shipped |
|---|---|
| **2026-08-04** | **"SMT divergence signature labels on backtesting trades"** — one week ago, in Paul's own methodology |
| 2026-08-04 | Filters and sorting in backtesting Trade Log |
| 2026-07-28 | **"Scenario Sharing — share scenarios by link or email"** |
| 2026-07-21 | **"ICT/SMC Concept Library (Tier 1) for Automated Backtesting"** |
| 2026-07-21 | "Zella AI Analysis panel in backtesting is now collapsible" |
| 2026-07-14 | "Automated Backtesting now live for all users" |
| **2026-07-07** | **"Zella AI: improved 'check trades against my playbook' prompt"** — AI rubric-checking, shipped |
| 2026-06-16 | **"Zella AI Session Review summary now appears in Notebook journal"** |
| 2026-06-02 | "Zella AI + Agents now live for all users" |

*"What stops them shipping it next quarter"* is the wrong question. **They shipped the load-bearing parts last
quarter**, including Paul's own ICT/SMC concepts three weeks ago and SMT labels one week ago. They hold what
the file cannot carry — wall-clock time, notes, screenshots, stable IDs — and they need no export: they own
the database. Treat the Zella-Score behavioural gap as **perishable**: they already collect rule ticks, so
adding adherence to the weights is a weights change over data they have.

### Two corrections the synthesiser owes `devil` (both reduce its case; neither rescues the bet)

1. **The backtesting export is NOT a 48-checkbox picker.** `devil` costed the friction with one. **OBSERVED:
   the modal is a single dropdown — `Active columns` / `All columns` → `Download`.** Its 17-step friction
   count is overstated at that step.
2. **`devil`'s own "single check that could rescue the bet" has already been run, and it fails.** It asked
   whether the picker offers a creation-timestamp or session-ID column. The orchestrator exported with
   **`All columns` selected** and got **48 columns containing neither.** The rescue is closed, by
   measurement, against the fullest column set the product offers.

### What `scholar` establishes that changes the CLAIM, not the verdict

The frozen ledger is **strongly supported as an INSTRUMENT and weakly supported as a TRAINER** — and the
design has been conflating them.

- **Strong (the real warrant):** hindsight bias — Guilbault et al. 2004, `META`, 95 studies, Md = .39; outcome
  bias — Baron & Hershey replicated at N = 692, **d = 0.77–1.10**, *larger* than the original. A retrospective
  "was that a good decision?" is known-corrupted at effect sizes near d = 1.0, and an immutable prior record
  is the only thing that removes the corruption. **This is the best-evidenced element in the whole platform.**
- **And it is a literature-grounded competitive claim:** Tradezella's adherence is ticked *after the fact* on a
  completed trade and its only quality signal is P&L-derived — **precisely the condition under which hindsight
  and outcome bias operate at maximum strength.**
- **Weak:** that calibration scoring improves decision quality. Chang et al. 2016 `RCT` (Brier +6–12%) was
  *training content plus practice*, not scoring alone; Martin 2025 is a `REPLICATED-NULL` at N = 610/871. **No
  study anywhere links calibration training to trading P&L.**
- **So the honest claim is "an uncontaminated record of what you actually believed", NOT "this makes you a
  better trader."** Claim 1 survives scrutiny; claim 2 does not.
- **DKR 1999 STANDS** — no XP, no badges, no points. Nothing overturns it; Sailer & Homner 2020's gamification
  effects were weakest exactly for reward-and-status mechanics. **And positive informational feedback is
  affirmatively supported (d ≈ 0.31–0.33)** — the rubric grade and the AI reader are the evidence-backed side
  of that meta, not merely tolerated.
- **Constraint the design must respect:** process-focus is *not* unconditionally supported. Sharon et al. 2022
  `META` finds **outcome** accountability better at *high* task complexity (SMD −0.48). Do not market
  process-focus as proven.

### Verdict, plainly

**`DON'T BUILD` the Tradezella importer** — boundary `OPEN` but pointing downstream, demand measured at ZERO
in the one user across three live instruments, and the import path would contaminate the platform's only
genuine asset. **Bet B is additionally dead**: ToS §20, a market that ignored a shipped analogue (Temper,
$12.99/mo, "not enough ratings to display an overview"), and an incumbent shipping AI agents weekly.

**This is a success, not a failure.** The lane cost one skill, one boundary probe, one council and zero code —
and it stopped a four-week build that would have degraded the evidence layer. That is exactly what a
boundary-first divergent council is for.

## Lane

- **This wiki** produces the design artifacts: a canonical spec under `concepts/architecture/`, updates to
  [[concepts/roadmap/ideas/backtest-companion-layer]], and this tracker.
- **The app code** lands in `C:\Users\PaulRussell\repos\neurospect-learn`. Code is ground truth once written.
- Isolation Rule applies (Neurospect only; no ALDC content or references).
- Distributed-workflow pattern docs are referenced by absolute path, never wikilink:
  `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`,
  `…\session-lifecycle.md`, `…\tracker-template.md`.

## Plan

### Phase B1 — Deep research + design session — ✅ **COMPLETE 2026-08-11** (verdict: §COUNCIL VERDICT)
Answer the 17 questions above from **external evidence**, decide the positioning, and produce ONE canonical
design doc plus a boot-promptable B2+ split. **Writes no app code.**

### Phase B2+ — **the importer is NOT built.** Three things replace it, in this order.

The council's phase split. B1's research killed the phase it was supposed to design, which is the outcome
E1's precedent explicitly allows for.

#### B2 — ⭐ THE FREE TEST, and it gates everything else. Zero code. Paul only.

**Before any build: define rules in the Tradezella Playbook → Rules tab, and run ~20 backtesting sessions
using the in-product fields that already exist** — `Mistakes`, `Custom Tags`, `Rating`, `Reviewed`, and the
Backtesting Session Notes folder.

This is `devil`'s success criterion #1 and it is the honest gate. Three live, free, one-click discipline
instruments currently read **ZERO**. If they stay empty after twenty sessions, **no companion of any design
survives** — and that will have been established for the price of the practice Paul was going to do anyway.
If they fill up, the residue that Tradezella *still* cannot do becomes the real, evidenced spec.

**Note what this phase actually is: it asks the trader to use the incumbent properly before building
anything beside it.** A council that recommends its sponsor do nothing for twenty sessions is doing its job.

#### B3 — Run `neurospect-learn` somewhere it can actually be used. — ✅ **CLOSED 2026-08-12 (locally, not hosted)**

**Status, stated exactly.** The phase closed by being **re-timed, not completed as written**. Paul decided
on 2026-08-12 that **hosting is premature**, so the deliverable became a **one-command local Docker daily
driver** (:8001 / :5174, sharing the dev DB on :5433), which is built, running, and **render-verified** —
all eight pages painted, seed anchored at the rendered layer, and the evidence-persistence test passed
across a forced container recreate. Evidence: `api/docs/evidence/b3-local/` (12 artifacts +
`b3-local-render-walk.md`); runbook §Local stack in
[[processes/operations/neurospect-learn-deployment]].

**The hosted path is PARKED, not cancelled.** `render.yaml`, `requirements.txt`, the SPA fallback, the
fail-closed Discord allowlist, tolerant env parsing and runbook §1–§7 all remain written and
config-proven; **nothing is provisioned and nothing is deployed**, and the B3b boot prompt that would have
provisioned it is retired unrun. B3's original argument is not overturned — `devil`'s criterion #5 made
deployment the binding constraint *on showing the platform to a second person*, and **B2 is what
determines whether there is anyone to show it to**. Un-park when B2 returns full instruments, or when a
second user actually exists.

Six enforcement phases of real work are reachable only from one laptop. There is no Dockerfile, no CI, no
container, no deploy config. **Until this is fixed the platform cannot be used away from the desk, cannot be
shown to a second user, and every "high-friction flow" argument is moot because there is no flow.**
`devil`'s success criterion #5. This is the highest-value phase available today and it depends on nobody else.

#### B4 — Capture in `neurospect-learn` FIRST, not imported after. — ➡️ **ABSORBED 2026-08-12 as S2 of [[processes/distributed-workflow/active/aura-session-runner]]**

> **This phase has MOVED. Do not run it from this tracker.** On 2026-08-12 Paul opened the **Aura Session
> Runner** lane — a screen he can keep open beside Tradezella and follow every session — and B4's
> capture-first brief is its **S2**. One lane, not two overlapping ones: two trackers describing the same
> work is how the B3b misdirection happened. Everything below is preserved as the origin of S2's
> constraints (E5 pre-commitment, consistency/`CI`, the `SELF-REPORTED` quarantine rule, and the two-clock
> finding), all of which carried across intact.
>
> **B2 still gates the capture layer** — and the new lane's **S1** exists precisely to make B2 runnable:
> the council's ZERO was measured against 2 sessions / 8 minutes **with zero rules defined**, so the gate
> was blocked on a missing instrument rather than on Paul's discipline. S1 builds that instrument and
> writes nothing, so it cannot prejudge the gate's outcome.

`scholar`'s deliverable targets are **cue-usage (`CI`)** and **consistency** — both require data captured
*during* the session, which is exactly what the export cannot carry. So the correct surface is the
platform's **own** paste-first capture, before/while a Tradezella session runs:

- A **pre-session pre-commitment** in the existing frozen ledger (E5), authored *before* the replay is
  advanced. This is the one artifact whose ordering can be trusted, because `neurospect-learn` stamps it.
- **Consistency across similar setups** — one rubric, many captures, measure variance in cue usage. Needs
  N and interleaved presentation (Brunmair & Richter 2019, `META`, g = .67 for visual category induction —
  the material class chart-setup recognition actually belongs to).
- Tradezella stays the **execution surface**. Nothing is imported; the screenshot Paul already pastes is the
  evidence, and it carries a real wall-clock timestamp because the platform created it.

**If backtest-derived data is ever imported, it must be permanently and visibly quarantined as
`SELF-REPORTED`** and excluded from the evidence streak, the calibration score and the Readiness Gate.
`devil`'s criterion #2 — and the design must then state what value remains, because that residue *is* the bet.

#### Deferred, with the reason recorded

- **The repo-integration lane is strictly better on the platform's core axis** and should be reconsidered
  ahead of any journaling integration: git commits carry **authenticated wall-clock timestamps and content
  hashes** — exactly the provenance property the CSV structurally cannot supply — from data Paul owns, with
  no vendor who can change the schema on a Tuesday.
- **Bet B (a product for other traders) is closed** pending: written permission under ToS §20, and evidence
  that a market which ignored Temper at $12.99/mo would pay for a second subscription that adds work.

### The re-check trigger on this whole verdict

Per `prospect`'s rule that **boundary facts expire**, this verdict is scoped to **2026-08-11, Pro tier**, and
is invalidated by any of: a Tradezella API or webhook appearing; a session-ID or record-creation-timestamp
column entering the export; the ToS being revised from its 2020-10-29 text; or B2 returning full instruments
after twenty sessions. Tradezella ships **weekly** — re-run Gate 3 before acting on this page after ~2026-11.

## Session Log

### 2026-08-10 — workstream created (scoping only, no research)
- trigger: immediately after the learning-enforcement workstream closed (E6 committed + pushed), Paul
  redirected the next lane: Tradezella is now the backtesting tool, and the question is what `neurospect-learn`
  becomes around it — plus a broader companion/integration positioning for product-market fit.
- **answered a question worth recording: yes, next lanes ARE outlined in the wiki — and that page is stale.**
  [[concepts/roadmap/README]] holds six horizons and 18 idea stubs with a full lifecycle, but it was created
  and last updated **2026-04-25** and describes the *earlier* `neurospect-api`/`neurospect-app` generation. Its
  "Now" horizon is deploying that app and its operating principle reads "no new features until the existing
  build is deployed" — which, read literally, would have blocked the entire Phase 5 arc **and** all six
  enforcement phases. It never mentions `neurospect-learn`, and the 2026-08-09 "learning platform is THE focus"
  decision never propagated to it. Flagged there under Rule #6 rather than silently rewritten.
- did (wiki only, no code, **no research**): created
  [[concepts/roadmap/ideas/backtest-companion-layer]] (status `designing`) and this tracker — Paul's framing
  verbatim, the asset this lane is built on stated as do-not-redesign, 17 open questions grouped so the
  boundary facts come first, and the evidence bar the lane inherits from E1. Authored the **B1 boot prompt**.
- **decided how the research should be run, and flagged a genuine gap.** Paul asked for a "council of 5"
  and a deep-research pass. The installed council skills — `conclave` (reviews PRs), `inquest` (resolves
  defects), `assay` (answers data/API questions), `vigil` (watches unattended mechanisms) — are all
  *convergent*: they take an existing artifact and interrogate it. **None fits discovery**, where the artifact
  does not exist yet and the inputs are external. `assay` is closest in machinery but its core discipline
  (declare a counting basis, enumerate the population) has no referent here. There is also **no
  `deep-research` skill installed**; research would be WebSearch/WebFetch driven. Recommendation recorded in
  §Recommended tooling below.
- next: **author the council skill (small dedicated session), then run the B1 boot prompt.** The skill is
  itself a design artifact and deserves fresh context; B1 can run without it, but less well.

### 2026-08-11 — `⛏ prospect` authored (skill session; still no research, no design, no app code)

- **approach:** followed the skill-authoring boot prompt as written — read `assay` in full as the format of
  record, skimmed `conclave`/`inquest`/`vigil` for how the four differ, then the E4 as-built and
  §Contradiction flags for the precedents the prompt named. No app environment started (the prompt said none
  was needed, and none was).
- **decided: kept the recommended name `prospect`**, glyph **⛏**, completing the metaphor `assay` established
  — *you prospect to find the ore, then you assay what you found*, which is exactly the divergent→convergent
  relation. Lenses named `claimant` · `scout` · `scholar` · `canvasser` · `devil`; `devil` deliberately keeps
  the house name it has in all four siblings rather than being renamed "kill-shot".
- **did:** wrote `~/.claude/skills/prospect/SKILL.md` (323 lines) + `references/prospect-brief-template.md`
  (147 lines).
  Structure follows the house shape: three gates before convening, with **Gate 3 = the boundary probe** as the
  signature gate (`OPEN | NARROW | CLOSED`, and **CLOSED halts the council**), five lenses each with an
  explicit *may not* column, a human gate before the output becomes a design, and design as a **separate phase**
  after the verdict. Reconciled all four siblings + `army` (see flagged below).
- **built three disciplines beyond the three the prompt asked for**, each earned from a precedent in this
  corpus rather than invented:
  - **A five-rung source tier** `OBSERVED | DOCUMENTED | REPORTED | MARKETED | ASSUMED`, with **`DOCUMENTED`
    is not `OBSERVED`** as its own starred rule. Earned from E4: the phase's *own boot prompt* asserted the
    SDK picks the credential up from `api/.env` with no code change, and that was false; the same session
    found a config default that killed `alembic`, `uvicorn` and `pytest` on import. If our documentation can
    be wrong about our own code, a third party's is not evidence about theirs.
  - **Four kinds of absence** — `ABSENT | UNSEARCHABLE | UNSPOKEN | TRIED-AND-FAILED` — the discovery form of
    "a zero from an instrument you have not proved can see is not a measurement". `TRIED-AND-FAILED` is the
    one that matters: it reads exactly like good news.
  - **⭐ Boundary facts expire.** The discipline none of the four convergent siblings needs, because a diff
    does not change while you review it and a third party's product does. Every boundary fact carries its
    scope (tier · version · region · date) and the event that invalidates it. Straight from E4's probe, which
    **re-measures its conclusion every run and prints `⚠ REOPENED`** rather than asserting it, and which
    scoped the 981-token finding to one model with instructions to re-measure if it changed.
- **verified — the prompt's "do not ship a skill that has never been pointed at anything":** dry-ran it
  against all 17 questions. Full result in §Dry-run above. Headline: **it is not a clean 17-of-17 mapping** —
  3 questions (Q4, Q10b, Q11) are internal design questions no external lens should touch, 2 (Q3, Q17) need
  splitting, and the skill asks 3 questions the 17 do not. Halt condition confirmed mechanical (fails closed
  on empty `PAYLOAD` + `MECHANISM: none`), and four structural disagreements between lenses confirmed.
- **flagged (1) — the tracker has had two active markers all along, one invisible to the boot skill.**
  The Phase B1 *status* heading carried the glyph followed by a bolded `ACTIVE` (asterisks *inside* the
  marker), which `/neurospect-boot`'s literal grep cannot match — so the chain resolved cleanly by luck, not
  by design. Normalised that heading to `**NEXT UP**` with no glyph. **Two conventions worth keeping:** the
  marker belongs on the *boot-prompt* heading only, never on a phase-status heading; and **prose must not
  quote the marker verbatim** — this log deliberately describes it instead, because every quoted instance
  becomes a false hit in the next session's grep. Verified after editing: exactly one match in this file.
- **flagged (2) — `~/.claude/skills/INDEX.md` did not list a single council skill.** Not `prospect`, and not
  `conclave`/`inquest`/`assay`/`vigil`/`army` either; it is the older ALDC "CCE Skills Library" taxonomy, last
  revised 2026-01-13, and the whole council family postdates it. Adding one orphan `prospect` row would have
  been worse than useless, so a new **§Adversarial Councils** section was added listing all six with their
  signature gates and a routing line. **Its header totals (63 skills / 20,492 lines) were left alone rather
  than guessed at**, with a dated note saying so.
- **flagged (3) — the `army` sibling list was already stale** (named three councils, predating `vigil`), and
  its Phase 5 **mirror contract is unfulfillable from a Neurospect session**. It requires a byte-identical copy
  to `wiki/concepts/patterns/skills/` — the **ALDC** wiki — which the Isolation Rule forbids writing to from
  this lane. Checked: `army`, `inquest` and `conclave` are mirrored there; **`assay`, `vigil` and now
  `prospect` are not.** `~/.claude/` is not a git repo, so those three are currently unbacked. **This needs
  Paul to run it from an ALDC session** — it is not a Neurospect decision to make.
- **flagged (4) — three PowerShell instruments misfired silently while verifying this work.** Each returned a
  confident wrong answer rather than an error, which is the exact failure the new skill is about:
  1. **`Measure-Object -Line` silently drops blank lines** (an empty string counts as zero lines) — it
     understated every skill file by ~30%. Two of the six line counts published in INDEX.md were wrong before
     being re-counted with `@(Get-Content …).Count` and corrected.
  2. **`-like` returned no-match on a string that demonstrably contained the pattern** (confirmed by
     `IndexOf`), which would have aborted a correct edit as "target not found".
  3. **`.Split('(321 lines)')` splits on each *character*, not the string** — it reported 58,958 remaining
     occurrences of a substring that had already been removed.

  All three were caught only because the result was checked against a second method. **Prefer
  `[System.IO.File]::ReadAllText` + `IndexOf`/`Replace` for verifying file content in this estate**, and never
  let a PowerShell one-liner be the sole witness to a published number.
- **NOT done, and not to be called green:** no research on Tradezella, the market or the literature; no
  design; no app code. The skill has been dry-run against questions, never against **evidence** — its first
  real exercise is B1, and B1 is where it will show whether the lenses hold.
- next: **Phase B1** — run the boot prompt at the bottom of this file, invoking `/prospect`, and read §Dry-run
  first so the council is briefed on the right 14 questions.

### 2026-08-11 (later) — Gate 3 boundary probe RUN; verdict `OPEN`. First real use of `prospect`.

- **approach:** ran the new skill's **Gate 3 only**, solo, before convening anything — which is what the
  skill prescribes and what kept the cost down. Paul authorised the council decision as *"boundary probe
  first, then decide"*, so no subagents were spawned.
- **decided: told Paul NOT to reactivate Pro yet**, and ran the probe on public primary sources first. The
  reasoning was the skill's own: the cheap step that can invalidate everything runs first, and a `CLOSED`
  verdict would have meant paying for a subscription to confirm a wall. He reactivated only once the public
  sources had been exhausted and the remaining questions provably needed the product.
- **did:** established the full boundary contract — see §Gate 3. Verdict **`OPEN`**: a manual, one-way,
  per-trade CSV export at `Backtesting → Trade View → Bulk actions`, 48 columns, 39 populated. No API, no
  OAuth, no webhooks, no developer programme on any tier; the Partner Programme is affiliate-only.
- **⭐ flagged — the finding that will shape B2:** the export carries **simulated market time, not wall-clock
  work time**. `Open Date = 2026-01-01` is the replayed bar, not when the work was done. The real figure
  (`Time spent 6 min`) exists in the Sessions UI and **is not in the export**. An importer that trusted
  `Open Date` would back-date every rep — the exact failure E5's frozen ledger exists to prevent.
- **flagged — the bet splits in two on the ToS.** §7 permits "a single copy made for personal use only";
  §20 forbids use "for any commercial purposes". Paul's personal use is fine; a commercial companion is not,
  absent written permission. B1 must choose which bet it is designing for.
- **flagged — two instrument failures, both caught, neither reported as a finding:**
  1. `app.tradezella.com/information/terms` returned a **JS shell containing only the word "TradeZella"**.
     Reporting "the ToS is silent on automated access" from that would have been a fabricated negative. It
     was classified **NOT-VISIBLE** and re-routed through the browser, where the full document rendered —
     at which point "no automated-access clause exists" became a real, verified finding.
  2. `www.tradezella.com/terms` 404s. Absence of a page is not absence of terms.
- **⭐ verified — the docs were wrong in the direction that UNDERSTATES.** The 42-article backtesting help
  collection has **no export article**, and the Sessions tab has no export. From documentation alone the
  honest verdict was `NARROW`/possibly `CLOSED`. The capability exists one tab over. Recorded because the
  skill's `DOCUMENTED ≠ OBSERVED` rule is usually framed as guarding against over-claiming, and here it
  guarded against **under**-claiming — which would have killed a viable lane.
- **verified — controls held.** Positive: the export returned Paul's real 2 sessions / 1 trade. Negative:
  the Sessions-tab bulk menu offers only `Delete` / `Add to strategies`, so the positive finding is
  discriminating rather than incidental.
- next: **the council.** Q3b (`TRIED-AND-FAILED` — has anyone built a Tradezella companion and abandoned it)
  plus the incumbent / learning-science / demand / kill-shot lenses. Paul's call whether to convene.

### 2026-08-11 (later still) — B1 COMPLETE. Council ran; verdict **DON'T BUILD**. No app code written.

- **approach:** five lenses (`claimant`/`scout`/`scholar`/`canvasser`/`devil`) spawned in parallel with ONE
  shared brief file, after Gate 3 had already settled the boundary. Sonnet for the three search-heavy lenses,
  Opus for `scholar` and `devil`. **Conflict rule written into the brief: the browser and Paul's live account
  had a single owner (the orchestrator)** — five agents driving one logged-in session would have corrupted
  each other's reads and could have mutated his data. Lenses got WebSearch/WebFetch only, and each named what
  it needed in-product; the orchestrator ran those.
- **decided: DON'T BUILD the Tradezella importer.** Bet A redirected to capture-first (B4); Bet B closed.
  Full reasoning in §COUNCIL VERDICT. The one-line version: **the boundary is `OPEN` and points downstream,
  while both genuine differentiators live upstream of it.**
- **⭐ the finding that decided it was a measurement, not an argument:** three shipped, free, one-click
  discipline instruments inside Tradezella all read **genuine ZERO** for the only user — instrument proved
  live, so `ZERO` not `NOT-RECORDED`. Demand for structured discipline capture, at zero friction, in a tool
  already paid for, is **0 for 3**.
- **verified rather than stapled.** Re-ran `devil`'s load-bearing external claim myself against
  https://tradezella.canny.io/changelog — **confirmed and understated**: they shipped ICT/SMC concepts
  (Jul 21), AI playbook-checking (Jul 7), AI session review into the journal (Jun 16), and **SMT divergence
  labels on 2026-08-04, one week ago**, on a weekly cadence, directly into Paul's own methodology.
- **corrected two of `devil`'s claims** (both reduce its case; neither rescues the bet): the backtesting
  export is a two-option dropdown, **not** a 48-checkbox picker, so its friction count is overstated; and its
  self-nominated "single check that could rescue the bet" **had already been run and failed** — the export
  was taken with `All columns` and the 48-column header contains no session ID and no creation timestamp.
- **flagged — `scholar` changed the CLAIM, not the verdict.** The frozen ledger is strongly supported as an
  **instrument** (hindsight bias `META` Md = .39; outcome bias replicated at **d = 0.77–1.10**) and weakly
  supported as a **trainer** (calibration-training evidence is contested; Martin 2025 is a replicated null;
  **no study links calibration training to trading P&L**). The honest claim is *"an uncontaminated record of
  what you actually believed"*, not *"this makes you a better trader"*. **The platform's own docs should be
  corrected accordingly** — this is a Rule #6 contradiction against any page claiming the latter.
- **flagged — DKR 1999 STANDS**, checked adversarially. No XP/badges/points. And **positive informational
  feedback is affirmatively supported (d ≈ .31–.33)**, so the rubric grade and AI reader are the
  evidence-backed side of that meta, not merely tolerated. New constraint: process-focus is **not**
  unconditionally supported (Sharon et al. 2022 `META`: outcome accountability better at high complexity),
  so it must not be marketed as proven.
- **flagged — boundary nuance found late:** Tradezella shipped **"Scenario Sharing — share scenarios by link
  or email"** (2026-07-28). So link-sharing exists for *scenarios* even though session-dashboard Share is
  image-only. Recorded because it partially qualifies the §Gate 3 share finding.
- **NOT done, deliberately:** the automated-backtest probe (would spend a Pro credit and informs Bet B only,
  which is now closed); the rule-checkmark lock test (needs a write to Paul's live account); the Zella AI
  Analysis panel inspection (needs an automated run). None change the verdict.
- next: **B2 is Paul's** — define rules in the Playbook Rules tab, run ~20 sessions using the existing
  in-product fields. **B3 (deploy) is the next session's work and now carries the marker.**

### 2026-08-11 (later still, second session) — B3 **HALF DONE**: deploy prep written and proven; nothing provisioned

- approach: took the B3 prompt as written. Read the wiki `CLAUDE.md`, §COUNCIL VERDICT, the `neurospect-api`
  deployment tracker and the E-invariants, then checked every "ESTABLISHED" claim against the code before
  building on it. Confirmed: no `.github/workflows` (only Copilot instruction files), migrations at `0012`,
  local DB on :5433, CORS localhost-only, R2 unwired. Repo is **private** and `main` is in sync with origin.
- **decided (storage): R2, and it is NOT optional.** Render's container filesystem is ephemeral, so
  `storage.make_backend()`'s local fallback would delete every captured chart on each deploy **while the
  `evidence_assets` rows survived** — reps derived from evidence that no longer exists, and *nothing raises*.
  That is a silent void of E2's central claim, so "defer storage" was rejected rather than deferred. Paul
  chose R2 with the constraint that the Cloudflare account must be **personal, not company**; the runbook is
  written that way throughout.
- **decided (auth): a fail-closed Discord allowlist.** The Discord app is Public, so a reachable URL means
  anyone who finds it can mint an account. `ALLOWED_DISCORD_IDS` unset = everyone on localhost, **nobody** in
  prod. Fail-open was rejected: forgetting one env var would leave the instance silently open, where
  fail-closed produces an immediate 403 whose message names the fix. Enforced **per request**, not only at
  token issue, because a 30-day JWT would otherwise outlive removal by a month — and a refused login writes
  no `users` row, asserted against the DB rather than assumed.
- **decided (hosting): Render + Cloudflare Pages, `frankfurt`, ~$14/mo.** Reusing the proven stack; region
  moved from `oregon` because the only user is in the UK and uses it daily.
- did: `render.yaml` (Blueprint, `rootDir: api`, Postgres 16 `basic-256mb`); `requirements.txt` committed —
  56 pinned lines, needed because `poetry.lock` is **gitignored**, so Render's pip build had nothing to
  install; `app/public/_redirects`; `app/auth/allowlist.py` + enforcement in the auth router and `deps.py`;
  tolerant parsing for the two list-valued settings; `.env.example` updated on both sides; and the runbook at
  [[processes/operations/neurospect-learn-deployment]] with a nine-row §Differences table.
- **flagged — four things the old runbook would have got wrong, each MEASURED, not inferred:**
  1. **`plan: starter` on Postgres is a LEGACY type** Render no longer creates new databases on, and
     `postgresMajorVersion` now defaults to **18** when omitted. Copying the 2026-04 runbook verbatim fails
     the Blueprint outright. Checked against Render's Blueprint spec rather than assumed.
  2. **`-w 2` is unsafe here.** `services/ai_grade_queue.py` serialises drains with a per-*process*
     `asyncio.Lock` and has **no** DB-level claim (no `FOR UPDATE SKIP LOCKED`), so two workers would drain
     the same `pending` rows — duplicate advisory grades and duplicate Anthropic spend. `--workers 1`, and
     raising it requires adding a DB claim first. This is a correctness constraint, not a tuning knob.
  3. **Both list-valued env vars accepted JSON ONLY.** A bare origin, `a,b`, and an **empty** value each
     raised inside the settings source and killed the app **at import** — not a 4xx, a process that never
     serves. `sync: false` renders as an empty dashboard box, so the most likely first deploy would not have
     booted. Fixed with `NoDecode` + a before-validator; the accepted forms are pinned by 15 tests.
  4. **The wiki is not a runtime dependency** — only `scripts/` read `wiki_content_root`. So production is
     seeded from the laptop against the external connection string, the corpus never enters the deployed
     artifact, and rubrics stay wiki-projected and read-only. The seed step carries a **target-proving**
     pre-flight that prints host+database before anything is written, because exporting `DATABASE_URL` alone
     does not redirect these scripts and that trap has wiped the local seed twice.
- **flagged — a PRE-EXISTING defect the suite surfaced, fixed, and one that is NOT fixed.**
  `test_honesty_api.py` built its dates from `date.today()` — the *machine's* local date — while both clocks
  in the code are UTC-based (`study_preferences.timezone` defaults to `"UTC"`, and `0012`'s trigger compares
  against `(now() AT TIME ZONE 'UTC')::date`). On this Pacific-time machine the suite therefore went red
  every evening after 17:00 local, `rest_days_upcoming` short by exactly one. The tests now read the same
  clock as the code and were re-run **inside the failing window** to prove it. **Unfixed and deliberately
  out of scope:** the underlying **two-clock** design — the planner counts in the user's timezone while the
  trigger enforces in server UTC. They agree for a user at or ahead of UTC (Paul) and can disagree west of
  it. Deployment makes this permanent, since Render runs UTC. Carried to B4.
- **invariants ([[concepts/architecture/learning-enforcement]] §Invariants): none touched, and one
  actively defended.** No service, model, router or migration outside `auth/` was modified — `gate.py`,
  `stages.py`, the evidence layer, the rubric layer and the prediction ledger are byte-unchanged, so
  invariants 1–3 and 6–7 have nothing in scope to move, and 4 (backtest ≠ live) sees no new data path. The
  phase's contact with the enforcement layer is invariant **5** (`reps` strictly harder, never easier), and
  it is a *defence*: deploying on the ephemeral local storage backend would have left rep-bearing evidence
  rows whose blobs had been deleted, which makes `reps` accidentally **easier** to hold than to have earned.
  Requiring R2 is what keeps that from happening. The allowlist can only ever deny access; it mints nothing.
- verified: **294 backend tests pass** (263 baseline + 16 allowlist + 15 config-parsing), against a 263-pass
  baseline captured *before* any edit; frontend `tsc -b` + `vite build` clean, with `_redirects` confirmed
  present in `dist/`; `scripts/scratch_migrate.py` → `RESULT: REVERSIBLE`, which is the real evidence that
  the 12 migrations Render will run against an **empty** database actually work; catalog row counts
  re-measured as the seed anchor (74 / 23 / 58 / 67 / 44 / 104, `alembic_version` `0012`) and they match this
  tracker's claims exactly.
- **NOT done, and it is the majority of the phase's value:** nothing is provisioned, nothing is deployed,
  and therefore **nothing has been rendered or verified**. No R2 bucket, no Render service, no Pages project,
  no Discord redirect URI. Every one of those needs Paul's own accounts and a payment method. The
  verification battery in the runbook §6 is written but **unrun**, and until it is run this phase has not
  demonstrated the thing it exists to demonstrate.
- next: **B3b** — Paul provisions (runbook §1–§4), the session seeds (§5) and then runs §6 against the
  rendered surface, including the redeploy-and-look-again test that is the whole reason R2 is in scope.

### 2026-08-12 — hosting PARKED; local Docker daily driver built, render-verified and **CLOSED**

- **context this entry exists to repair: VS Code crashed mid-session**, so the work below was written to
  disk and then left completely unrecorded. The next session found seven untracked files, a running
  three-container stack, and a tracker whose `⏭ ACTIVE` prompt said *provision Render* — i.e. the
  tracker actively misdirected. **The on-disk artifacts were the only surviving record of the pivot**
  (the decision was recoverable solely because `docker-compose.yml`'s header comment stated it). Lesson:
  a decision that lives only in a code comment is one crash away from being lost — but a decision
  written into a code comment is what made recovery possible at all.
- ⭐ **decided (Paul, 2026-08-12): hosting is premature. B3's Render path is PARKED, not cancelled.**
  He is the only user, every drill is desktop TradingView bar-replay, and a public URL buys only the two
  things not needed yet — a second person reaching it, and access away from the desk. `render.yaml`, the
  R2 decision, the fail-closed allowlist and the runbook all **stay written and proven**; none of it is
  provisioned. This does **not** overturn B3's reasoning, it re-times it: `devil`'s criterion #5 argued
  deployment was the binding constraint *on showing the platform to someone*, and there is nobody to
  show it to until B2 has been run.
- did (the pivot, unlogged until now): `docker-compose.yml`, `api/Dockerfile`, `app/Dockerfile`,
  `app/nginx.conf`, root `.env.example`, two `.dockerignore` files — a one-command local stack on
  **:8001 / :5174**, deliberately not the dev ports (:8000 / :5173), sharing the **same** DB on :5433.
  Data was **copied** (never moved) from the old anonymous volume into `neurospect_learn_pgdata`, so the
  anonymous volume survives as the rollback.
- did (this session): **closed the phase properly** — fixed the healthcheck defect below, walked every
  page, ran the persistence proof, wrote §Local stack into
  [[processes/operations/neurospect-learn-deployment]], and retired the B3b prompt.
- **flagged — a defect that had been failing 1350 times in a row, in silence.** `app` reported
  `unhealthy` for its entire 4-hour life **while serving perfectly**. Discriminating test, predicted
  before running: in-container `wget http://localhost/` → refused, `wget http://127.0.0.1/` →
  **SUCCESS**; `netstat` shows one socket, `0.0.0.0:80`, and **no IPv6 socket at all** — musl resolves
  `localhost` to `::1` first. **The obvious fix was the wrong one:** adding `listen [::]:80;` to
  `nginx.conf` would have made nginx fail to bind and refuse to **start**, converting a cosmetic false
  alarm into a real outage. Fixed in `app/Dockerfile` instead (check dials `127.0.0.1`). After:
  `healthy`, streak **0**, and `healthy` in **7 seconds** on a later forced recreate. It mattered
  despite the site being fine, because nothing could ever gate on `app` being healthy and a
  permanently-red status teaches you to ignore health output.
- **flagged — `docker compose down -v` would destroy the seed and every captured chart.** Compose warns
  `volume "neurospect_learn_pgdata" already exists but was not created by Docker Compose. Use external:
  true`, and it is right: the volume is not declared `external`, so `down -v` is in scope to delete it.
  **NOT fixed** — one-line change, left for the next session rather than slipped in unverified.
- ⭐ **verified — the persistence proof, which is the one test this phase existed for.** The compose
  header *claims* "nothing here is ephemeral"; that was asserted, never run. Now run end to end:
  `aura D1-a` at `0/50 · 0 evidenced` → uploaded a capture through the real UI → `1/50 · 1 evidenced`
  with the thumbnail rendering → **`docker compose up -d --force-recreate api app`** → blob still
  present (14192 bytes) and **thumbnail still renders with the rep intact**, zoomed to prove it is the
  real image and not a broken-image placeholder. This is precisely the failure mode that made R2
  non-optional on Render: blob deleted, `evidence_assets` row surviving, rep derived from evidence that
  no longer exists, **nothing raising**.
- verified: **all eight pages paint** — Today (E6 honesty strip live), Path, Library, Drills, Plan,
  Journal, Expectancy, Gate — navigated by **direct URL**, which also proves the nginx SPA fallback
  (a refresh on `/journal`, or Discord's `/auth/callback`, would otherwise 404). Library prints
  **"67 pages"** and Drills **"58 drills"** *on the page*, anchoring the seed at the consumer's layer
  rather than inferring it from matching values; `alembic_version` `0012` and all six catalog counts
  (74/23/58/67/44/104) match the tracker exactly after the volume copy. The served bundle contains
  `localhost:8001` twice and `localhost:8000` **zero** times, so the `VITE_*` build-arg mechanism
  worked — as `environment:` it would have silently baked the dev API. 12 labelled artifacts +
  `b3-local-render-walk.md` in `neurospect-learn/api/docs/evidence/b3-local/`.
- **invariants: none touched; two observed working at the rendered layer.** The only source change was
  one `HEALTHCHECK` line in `app/Dockerfile` — no service, model, router or migration was modified. The
  walk *observed* E2 (the capture **derived** the rep; nothing minted it) and E3 (*"not checked yet —
  the reps still count"*) behaving as specified.
- **NOT done, stated plainly:** the `external: true` volume fix; Expectancy/Journal **filtering** was
  rendered but never driven to a result, and `Check against the bar` was deliberately not clicked, so
  the E3 grade path is **unverified at the UI**; E4's second reader is untested locally
  (`AI_GRADING_ENABLED=false`); the fail-closed allowlist is **not** exercised by this stack
  (`DEBUG=true` admits everyone by design — it is a `DEBUG=false` property); and **nothing is deployed**.
- **residue:** one real evidence asset + one derived rep on the fixture account `e2e-evidence`
  (`aura D1-a`), left in place deliberately — evidence is not retractable under E2/E5, and hand-deleting
  it would set a worse precedent than a documented fixture rep.
- next: **B4** — capture-first in `neurospect-learn`, per §Phase B2+. Carry the **two-clock** finding.
  B2 (Paul's twenty Tradezella sessions) still gates everything and is still unrun.

## Dry-run of `prospect` against the 17 questions (2026-08-11) — B1 MUST READ THIS

The skill was pointed at the 17 questions before being called done. **It does not ship a clean 17-of-17
mapping, and that is the finding** — the dry-run changed how B1 should brief its council.

**Lens assignment (14 of 17 are external-evidence questions):**

| Lens | Questions it owns |
|---|---|
| `claimant` (boundary) | 1, 2, **3a** (partner/affiliate programme), 5 |
| `scout` (incumbent) | 6, 8a (what Tradezella charges, observed) |
| `scholar` (mechanism) | 9, **10a** (what *should* be captured), 12, 13, 14 |
| `canvasser` (demand) | **3b** (who else has integrated), **7**, 8b (what the price implies), 15 |
| `devil` (kill-shot) | 16, **17b** (does designing for two make the first worse) |

**⭐ Three of the 17 are NOT lens questions — do not brief a council on them.** They are internal design
questions about our own code, and an external-evidence lens has nothing to say about them. They belong to the
synthesiser, in the design phase, *after* the boundary verdict:

- **Q4** ("if the only path is manual export, what is the least-friction honest flow, and is it good enough")
  — this is Phase 3 design, gated behind the boundary. Answering it during research is how a council designs
  against a boundary that has not been established yet.
- **Q10b** ("which of those is already covered by E1–E6 primitives")
- **Q11** ("new data model or a new *source* for the existing one")
  — both are the "reuse primitives before inventing schema" step, and both are already answered by reading
  our own code. Sending them to a research lens invites a proposal to rebuild what E2 settled.

**Two questions need splitting** before they go in a brief, because each has two halves that land in different
lenses and would otherwise be answered on whichever half is easier:

- **Q3** → *3a* the partner/affiliate programme (a boundary term, `claimant`) and *3b* whether third parties
  have integrated (`canvasser`). Sharp point the tier ladder gets right and a human easily gets wrong:
  **another company's working integration is `REPORTED` evidence about the boundary, never `OBSERVED`** — they
  may hold a private agreement that is not available to us.
- **Q17** → *17a* which other platforms this generalises to (needs a second boundary probe — **explicitly defer
  it** unless the bet requires it, or the gate cost doubles) and *17b* the scope-expansion risk (`devil`).

**One deliberate divergence from §Recommended tooling's lens table.** That table put *"where do users say
attention leaks"* (Q7) under **Incumbent**. The skill puts it under **Demand**, and the cut is now
`scout` **= the product's behaviour, first-hand** / `canvasser` **= what people say and pay, population
stated**. Reason: the dissent positive-control discipline ("prove your search can find complaints before
reporting there are none") has to live in exactly one seat, and two lenses searching the same forums produce
**correlated** findings that read as corroboration. Recorded because it contradicts the table above.

**Three questions the skill asks that the 17 do not** — evidence the lens set is not just a restatement of the
tracker, and all three should be added to B1's brief:

1. **Has anyone built a Tradezella companion and abandoned it?** Q3 asks who has integrated, never who *tried
   and quit*. This is the skill's `TRIED-AND-FAILED` absence class, and it is the one that reads most exactly
   like good news: "nobody has built this" is an opportunity or a graveyard, and the difference is decisive.
2. **What is the maintenance burden, in sessions per year, of tracking someone else's release cycle?** — and
   who notices when their API changes.
3. **What is the re-check trigger on every boundary fact?** A third party's product changes on their schedule.
   A `CLOSED` verdict in particular is a fact with an expiry date, and it is the one most likely to be quoted
   years later as settled.

**Halt condition is checkable, not rhetorical** — verified: the Gate 3 contract fails closed on an empty
`PAYLOAD` + `MECHANISM: none`. The test is *"name the fields that cross"*, which is mechanical. For this lane
specifically: the export file exists and its columns have been read, or the verdict is `CLOSED`/"could not
determine".

**The lenses disagree by construction**, which was the other thing to verify. Four structural conflicts are
built in, not incidental: `scout` "they deliberately omit X" (opportunity-shaped) vs `devil` "they omit it
because it does not work, or they ship it next quarter"; `scholar` "spaced retrieval works" vs `canvasser`
"nobody asks for it or would pay"; `claimant` "manual CSV only" vs `scholar` "the mechanism requires in-session
capture" — **that one decides the product**; and `canvasser` "demand evidenced" vs `devil` "n=1, you are the
market".

## Recommended tooling for B1 (Paul asked; this is the recommendation, not a survey)

> **✅ DONE 2026-08-11 — the recommendation below was accepted and executed.** The skill is `⛏ prospect`
> at `C:\Users\PaulRussell\.claude\skills\prospect\SKILL.md` (+ `references/prospect-brief-template.md`).
> The five lenses are named `claimant` · `scout` · `scholar` · `canvasser` · `devil`. Read §Dry-run above
> **before** briefing a council with it — the question mapping is not 1:1.

**Recommendation: author ONE new skill — a *divergent* council for product bets — and run B1 with it.**

The four existing council skills share a shape: N independent lenses over **something that already exists**,
adversarial verification, then a gated deliverable. That shape is right; the *inputs* are wrong. B1 has no
artifact to interrogate — it has an incumbent product, a literature, and a market, none of which are in the
repo. So the sibling to write is discovery-shaped, and the five lenses should be orthogonal **links in the
evidence chain of a product bet**, not five opinions about the same thing:

| Lens | Its job | The failure it exists to prevent |
|---|---|---|
| **Boundary** | What can *actually* cross — API, export, auth, ToS, rate limits | Designing a feature the platform forbids or cannot feed |
| **Incumbent** | The tool's real flow and its deliberate omissions; where users say attention leaks | A feature list mistaken for an opportunity |
| **Learning science** | Only replicated findings, each tiered; names what it refuses | Pop-neuroscience smuggled in as rigour |
| **Demand** | Who else exists, what they charge, what evidence of want exists — population stated honestly | PMF asserted from n=1 |
| **Kill-shot** | Argues the bet is wrong: platform risk, "feature not product", maintenance, ToS | A council that only agrees with itself |

**Three disciplines the skill must enforce, each earned from a real failure in this repo's history:**

1. **The boundary lens runs FIRST and can halt the rest.** E4's precedent — "do STEP 6 (measure) first, it is
   the only step that can invalidate what is already committed" — and it *did*. If Tradezella exports nothing,
   four lenses of feature design are wasted.
2. **Every claim carries a source and a tier; a vendor claim is never a design premise.** E1's MeasureBench
   finding *changed* the design; Duolingo's streak-freeze numbers were labelled unverified and nothing was
   built on them. Both behaviours are already in the corpus and should be the skill's bar.
3. **A zero from an instrument you have not proved can see is not a measurement.** Straight from Paul's global
   Evidence-Gated Analysis gate, and the exact rule E6 just implemented five times. "No one is complaining
   about X" is not evidence of no complaints unless the search would have found them.

**What NOT to do:** do not use `army` (generic parallelism, no discipline attached); do not stretch `assay`
(its counting-basis machinery has nothing to count here); and do not run B1 as one long solo session — the
whole reason for a council is that a single context will not hold Tradezella's product surface, a literature
review, and a market scan without one of them becoming decoration.

**Sequencing:** author the skill in its own short session → run B1 with it → B1 outputs the canonical design
doc + the B2+ split. B1 can be run without the skill using the boot prompt alone; it will simply be more
vulnerable to the three failures above.

## Boot Prompt (Skill authoring — the divergent council) — ✅ RUN 2026-08-11

> **HISTORY — do not execute.** Ran 2026-08-11; `⛏ prospect` was authored and the ACTIVE marker moved to the
> Phase B1 boot prompt at the bottom of this file. See §Session Log 2026-08-11.

> **This runs BEFORE Phase B1.** B1's own prompt is further down, marked QUEUED; **this session's last act is to
> move the ACTIVE marker onto it** (see §Ending this session below).
> **Launch:** `claude --model opus[1m]`, then `/effort high`. Plan mode optional — the output is one file.
> **No app environment is needed** — this session writes a skill, not code. Docker/uvicorn/vite can stay down.

**Task: author the fifth council skill — a DIVERGENT sibling for discovery, then use it on the B1 lane.**

READ FIRST, IN THIS ORDER:
1. `C:\Users\PaulRussell\.claude\skills\assay\SKILL.md` **in full** (329 lines) — the closest sibling and the
   format of record. Also skim `conclave` (347), `vigil` (394) and `inquest` (539) to see how the four differ
   from each other. Note the house shape: YAML frontmatter with a long `description` ending *"Sibling of X
   (does Y)…; this one does Z"*, an italic epigraph, a numbered method, explicit refusals, and an optional
   `references/<name>-brief-template.md`. Also check `~/.claude/skills/SKILL_TEMPLATE.md` and `INDEX.md`.
2. `processes/distributed-workflow/active/backtest-companion.md` (this file) — §Recommended tooling holds the
   five lenses and the three disciplines; §Open questions is what the skill must actually be able to chew.
3. `concepts/architecture/learning-enforcement.md` §E4 as-built (the measure-first-because-it-can-kill-the-design
   precedent) and the §Contradiction flags (how an unverified source is labelled rather than leaned on).

**THE GAP, stated precisely, because it is the whole design rationale:** all four existing council skills are
**convergent** — they take an artifact that already exists (a diff, a defect, a dataset, a live mechanism) and
interrogate it from orthogonal angles. Discovery has no artifact. Its inputs are an incumbent product, a
literature and a market, none of which are in the repo, so nothing can be enumerated and there is no counting
basis to declare. That is why `assay` cannot simply be pointed at it.

**RECOMMENDED NAME: `prospect`.** It completes the metaphor `assay` already established — *you prospect to find
the ore, then you assay what you found* — which is exactly the divergent→convergent relationship between the
new skill and its siblings. Overrule it if something better appears, but keep the single evocative noun + glyph
convention (⚔ ARMY, ⚗ ASSAY).

BUILD:
  · The **five lenses** from §Recommended tooling — Boundary · Incumbent · Learning science · Demand ·
    Kill-shot — as genuinely orthogonal links in the evidence chain of a product bet, not five opinions about
    one thing. State for each what it is *not* allowed to do.
  · **Boundary runs FIRST and can halt the council.** This is the skill's structural signature, the way
    "declare the counting basis before producing a number" is `assay`'s. If what can cross the boundary turns
    out to be nothing, four lenses of feature design are already wasted.
  · **Source tiering, and the vendor-claim refusal.** Every claim carries a source and a tier; a vendor or
    marketing claim is never a design premise. Both behaviours already exist in this corpus (MeasureBench
    *changed* the E1 design; Duolingo's streak-freeze numbers were labelled unverified and nothing was built on
    them) — cite them as the bar.
  · **"A zero from an instrument you have not proved can see is not a measurement."** Carry it over from Paul's
    global Evidence-Gated Analysis gate and from E6, which implemented it five times. In discovery it reads:
    *"I found no complaints"* is not a finding unless the search would have surfaced complaints.
  · **A named pop-science refusal list** for the learning-science lens — learning styles, left/right-brain,
    "10,000 hours" as a law, dopamine-loop justifications for streaks. The last is directly contradicted by
    Deci/Koestner/Ryan 1999, which is already load-bearing in this platform (no XP, no badges, no points).
  · **A human gate before the output becomes a design**, mirroring how `assay` gates the client-facing artifact.
  · A `references/prospect-brief-template.md`, matching `assay`'s and `conclave`'s use of a brief template.

RECONCILE (easy to miss): `assay`'s body says **"Four siblings, one method, four artifacts"** and the four
descriptions cross-reference each other by name. Adding a fifth makes all four stale — update the sibling lists
and counts in `conclave`, `inquest`, `assay` and `vigil`, and add the new skill to
`~/.claude/skills/INDEX.md`.

VERIFY BEFORE DECLARING IT DONE — **do not ship a skill that has never been pointed at anything.** Dry-run it
against this tracker's **17 open questions**: does each question land cleanly in exactly one lens? Does the
Boundary lens produce a halt condition that is checkable rather than rhetorical? Is there a question none of
the five lenses would ask? A lens that never disagrees with the others is not a lens.

THIS SKILL IS NOT: a research-report generator; a replacement for `assay` (which stays the right tool once
there are numbers to enumerate); or a workflow that needs the `Workflow` tool — it is a skill, like its four
siblings. **Paul handles git — commit only when he asks.**

### Ending this session (MANDATORY — the boot chain depends on it)

`/neurospect-boot` resolves the single ACTIVE marker in `active/`, so leaving two headings marked (or none)
breaks the next session's entry point. Before signing off:

1. **Move the marker.** Remove it from this section's heading and put it on the **Phase B1** heading below
   (currently ending `— QUEUED, activate after the skill session`), so the next boot lands on the research
   session. Keep exactly one marked heading in this file at all times.
2. Add a **§Session Log** entry here: approach / decided / did / **flagged** / verified / next — including the
   skill's final name if `prospect` was overruled, and anything the dry-run against the 17 questions exposed.
3. If the skill was **not** finished, say so explicitly and leave the marker on this section. An overstated
   status is worse than an unfinished phase.
4. Bump `log.md` and `index.md` if the skill landed.

## Boot Prompt (Phase B1 — deep research + design) — ✅ RUN 2026-08-11

> **HISTORY — do not execute.** Ran 2026-08-11 with `⛏ prospect`. Gate 3 returned `OPEN`; the five-lens
> council returned **DON'T BUILD the importer**. See §COUNCIL VERDICT and §Phase B2+. The marker now sits on
> the **B3 deployment** prompt at the bottom of this file — B2 is Paul's own free test, not a session's work.

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort xhigh`**, in **plan mode**. This is a
research and design session and its output is a document, not code. **Write no app code in this session** —
E1's precedent, and for the same reason: the design is the load-bearing artifact and building against an
unvalidated one is how the phase gets rewritten.

**The council skill EXISTS — invoke it: `/prospect`.** Authored 2026-08-11 at
`C:\Users\PaulRussell\.claude\skills\prospect\SKILL.md`, with a brief template at
`references/prospect-brief-template.md`. Its five lenses are `claimant` (boundary) · `scout` (incumbent) ·
`scholar` (mechanism/literature) · `canvasser` (demand) · `devil` (kill-shot).

⚠️ **Read §Dry-run of `prospect` against the 17 questions BEFORE writing the brief.** The mapping from the 17
questions to the five lenses is **not** 1:1: three of them (Q4, Q10b, Q11) are internal design questions that
no external-evidence lens should be given, two (Q3, Q17) need splitting, and the skill asks three questions the
17 do not — including *"has anyone built this and abandoned it?"*, which is the difference between an opening
and a graveyard. Briefing a council on all 17 verbatim will waste two seats and invite a proposal to rebuild
what E2 settled.

⚠️ **STEP 0 — ESTABLISH THE BOUNDARY BEFORE DESIGNING ANYTHING.** Find out, from primary sources, what
Tradezella actually exposes: public API? OAuth? webhooks? CSV/Excel export and with which columns? What does
its **Terms of Service** say about automated access and about a user extracting their own data? Is there a
partner or integration programme? **This is the only step that can invalidate the rest** — a "manual CSV
export only" answer and a "documented REST API" answer produce different products — and it is the E4 lesson
applied (measure the thing that can kill the design *first*, because it costs little and it did kill one).
**Report what you actually found, including "could not determine", and never infer capability from marketing
copy.** If the ToS forbids the obvious approach, say so before designing around it.

⚠️ **`neurospect-learn` IS DEPLOYED NOWHERE, and that may stop being acceptable in this lane.** Design decision
#4 (2026-07-28) held that hosting was not a prerequisite *because* every drill is desktop TradingView
bar-replay and capture is paste-first on localhost. An integration with a hosted third party can break that
premise — OAuth callbacks and webhooks do not reach a laptop. **If this lane makes deployment a genuine
dependency, that is a first-class finding, not a footnote.** The only deployment runbook that exists
([[processes/distributed-workflow/active/deployment]]) covers the *earlier* `neurospect-api`/`neurospect-app`
pair, and its Phase-5 boot prompt is unrun.

GROUNDING: `neurospect-learn` is Paul's standalone learn-to-execute app for the Neurospect ICT /
Smart-Money-Concepts trading-mastery project — FastAPI + Postgres (`api/`) + React 19 / Vite / TanStack Query
(`app/`), running on localhost, **deployed nowhere**. The Phase 5 arc, its Phase-6 debt, and the **entire
learning-enforcement arc E1–E6** are COMPLETE: curriculum + three graded tracks, Study Planner, model-aligned
journal, expectancy, the computed non-overridable Readiness-to-Live Gate, the missed-trade log, stage exit bars
on real evidence, `evidence_assets`/`evidence_grades` with `reps` **DERIVED**, wiki-projected `rubrics` + a
`self_check` that may flag but never retract, the **AI vision second reader**, the **pre-commitment ledger +
calibration score**, and the **honesty strip + evidence-backed streak + declared rest days**. Migrations at
**`0012`**; seeds 74 concepts / 23 track stages / 58 drills / 67 content pages / 44 rubrics / 104 items;
**263 backend tests**, **Playwright 68**. **Paul is the only user it has ever had, and every number in it came
from fixtures.**

BOOT / CONTEXT — read in this order, and read the first two IN FULL:
1. The wiki `CLAUDE.md` — Isolation Rule, Architecture Doc Integrity (**code is ground truth; ONE canonical doc
   per topic; LINK the corpus, never restate it**), the MANDATORY post-implementation reconciliation checklist,
   Rules #1 (**never modify `sources/`**) #3 (index.md) #4 (log.md) #6 (flag contradictions), Context
   Management (tell Paul at >50%). **Paul handles git — commit only when he asks.**
2. This tracker — §Goal, §The asset this lane is built on (**do NOT redesign it**), and the **17 open
   questions**, which are your answer-or-defer checklist exactly as E1's 14 were.
3. [[concepts/architecture/learning-enforcement]] — **§E2–§E6 as-built and §Invariants.** This is the asset the
   whole bet rests on. Know precisely what is already enforced before proposing anything that touches it.
4. [[concepts/roadmap/README]] — the horizons, **and note it is stale** (2026-04-25, predates
   `neurospect-learn`; flagged in §Contradiction flags there). Read
   [[concepts/roadmap/ideas/platform-consolidation]] and [[concepts/roadmap/ideas/vertical-ai-platform]]
   specifically: they are the **opposite bet** (absorb the other tools), and this lane must argue against them
   on merit rather than ignore them.
5. [[concepts/roadmap/ideas/backtest-companion-layer]] — the strategic origin record for this lane.
6. THE CODE TO KNOW BEFORE PROPOSING A SURFACE: `api/app/services/{gate,stages,calibration,honesty,consistency}.py`
   (all pure, all computed-per-read — the idiom any new signal should follow), `api/app/models/evidence.py`
   (the ONE polymorphic evidence layer that already serves drills, concepts, journal entries and missed
   trades — a backtest artifact probably belongs here rather than in a new table), `api/app/models/prediction.py`
   (the frozen-call primitive), and `api/app/routers/journal.py` + `api/app/services/expectancy.py` (where
   `mode='backtest'` entries already live and are already scored).

RESEARCH — five orthogonal lenses. Keep them genuinely separate; a council that produces five versions of the
same answer has learned nothing:
  1. **Boundary** (STEP 0 above) — what crosses, on what terms.
  2. **Incumbent** — Tradezella's actual backtesting flow, layout and functionality end to end; what it does
     well; **what it deliberately does not do**; what its users complain about; what it charges.
  3. **Learning science** — what genuinely survives replication for skill acquisition under **noisy, delayed
     feedback**. Tier every source. **Name what you refuse and why** (learning styles, left/right-brain,
     "10,000 hours" as a law, dopamine-loop justifications for streaks). Check for anything that contradicts
     Deci/Koestner/Ryan 1999, which is load-bearing here — no XP, no badges, no points.
  4. **Demand** — who else occupies this space, pricing, and what evidence of want actually exists. **State the
     population honestly.** "I found no complaints" is only a finding if you can show the search would have
     surfaced them.
  5. **Kill-shot** — argue the bet is wrong. Platform risk, ToS, "this is a feature Tradezella ships next
     quarter", maintenance burden, and the n=1 problem. If it survives this lens it is worth building.

DESIGN — then, and only then:
  · **Decide the positioning** — companion vs. absorb — explicitly, against
    [[concepts/roadmap/ideas/platform-consolidation]], and say what would change your mind.
  · **Decide what a backtest session is in the data model.** Strong prior to argue *against*: it is a new
    SOURCE for primitives that already exist (evidence assets · predictions · journal `mode='backtest'` ·
    expectancy), not a new parallel schema. The E2 lesson — one polymorphic layer, not per-owner child tables —
    was hard-won; do not re-litigate it casually.
  · **Decide where the enforcement layer plugs in**: before a session (a plan / a pre-commitment), during it
    (adherence, pacing), after it (a scored review). Which of these already has a primitive?
  · **Cost the friction honestly.** The north star is that the honest path must be the path of least
    resistance; a design that frustrates real work fails it as hard as one that can be faked.
  · **Produce the B2+ phase split**, each phase boot-promptable from this tracker alone (E1's bar).

THIS LANE IS NOT: rebuilding a backtester (Tradezella is the chosen tool); a second journal; reopening that
`reps` are derived, that a grade may flag but never retract, that rubrics are wiki-projected and read-only,
that a prediction is frozen, or that the Gate has no override; adding XP/badges/points; or the repo-integration
/ "master platform" lane, which stays deferred.

DELIVERABLES: ONE canonical design doc under `concepts/architecture/` (added to the wiki `CLAUDE.md`
**Canonical doc per topic** table); this tracker updated with §Decisions, the B2+ plan and a session log; the
idea page moved forward; `log.md` + `index.md` bumped. **Every claim carries its source; anything unverified is
labelled unverified. Answer all 17 questions or defer them explicitly with a reason.** Then write the B2 boot
prompt. **Paul handles git — commit only when he asks.**

---

## Boot Prompt (Phase B3 — deploy `neurospect-learn`) — ✅ **CLOSED 2026-08-12** (ran 2026-08-11; closed locally, not hosted)

> **DO NOT EXECUTE.** History, kept for auditability. Its prep half ran on 2026-08-11; the phase then
> **closed locally** on 2026-08-12 when Paul parked hosting (see §B3 in the Plan and the 2026-08-12 log
> entry). Its `ESTABLISHED` block below is now **stale**: the repo *does* have Dockerfiles and a compose
> stack, and the test count moved 263 → 294.

> **Do not re-run this prompt.** Its preparation half is done and its findings are in the session log
> above; its provisioning half became the B3b prompt at the foot of this file. Kept unedited as the
> record of what B3 was asked to do.

> **B2 is NOT a session's work — it is Paul's.** Define rules in the Tradezella Playbook → Rules tab and run
> ~20 backtesting sessions using the existing in-product fields. Do not build anything that depends on that
> test until it has produced data. **Do not build the Tradezella importer** — see §COUNCIL VERDICT.

**Launch:** `claude --model sonnet[1m]` is sufficient (this is execution against a known runbook, not
design), `/effort medium`. Escalate to Opus only if the hosting decision turns out to be genuinely open.

**Task: make `neurospect-learn` reachable from somewhere that is not Paul's laptop.**

**Why this phase, and why now.** The B1 council closed the integration lane and named deployment as the
**actual binding constraint**. Six enforcement phases (E1–E6) of real, working code — derived reps, a frozen
pre-commitment ledger, an advisory AI second reader, a non-overridable Readiness Gate — are reachable only by
starting Postgres + uvicorn + vite by hand. Until that changes: the platform cannot be used away from the
desk, cannot be shown to a second person, and **every argument about capture friction is moot, because there
is no flow to have friction in.** `devil` made this its success criterion #5 and it is the highest-value work
available that depends on nobody else.

READ FIRST:
1. The wiki `CLAUDE.md` — Isolation Rule, **code is ground truth**, the MANDATORY post-implementation
   reconciliation checklist, Rules #3/#4/#6, Context Management (tell Paul at >50%).
   **Paul handles git — commit only when he asks.**
2. This tracker — §COUNCIL VERDICT (why integration was dropped) and §Phase B2+ (why this phase exists).
3. [[processes/distributed-workflow/active/deployment]] — a **proven, pitfall-annotated Render + Cloudflare
   Pages runbook**. ⚠️ It covers the *earlier* `neurospect-api`/`neurospect-app` pair, live since 2026-04-25,
   and **its Phase-5 boot prompt is unrun**. Treat it as a template to adapt, not a script to replay, and say
   plainly where `neurospect-learn` differs.
4. [[concepts/architecture/learning-enforcement]] §Invariants — nothing in this phase may weaken them.

ESTABLISHED (do not re-derive): the repo has **no Dockerfile, no `.github/workflows`, no deploy config**.
Migrations at **`0012`**; **263 backend tests**, Playwright 68. Local DB is `neurospect-learn-db` on **:5433**;
CORS currently allows **only** `http://localhost:5173`. R2 was never wired for `neurospect-learn` (screenshots
still 503 there) — decide explicitly whether storage is in scope for B3 or deferred.

⚠️ **Known traps, both of which have already cost a session here:**
- **Never run `alembic downgrade base` against the working DB.** An exported `DATABASE_URL` does *not*
  redirect Alembic — `.env` also sets `DATABASE_URL_SYNC`, which wins. This has wiped the seed twice. Use
  `scripts/scratch_migrate.py`.
- **Do not trust `--reload`.** The uvicorn reloader has died silently, leaving a worker serving stale code
  through a whole before/after measurement.
- **:5173 is held by a different project of Paul's.** Playwright's `webServer` reuse would test the wrong
  codebase — the E4 session left the suite unrun for exactly this reason.

DELIVERABLES: a deployed, reachable instance with its auth story stated; the CORS origin list updated away
from localhost-only; a **rollback path**; secrets handled per Paul's global rule (**ask before retrieving any
credential, name the secret and source, never echo a value**); the runbook written or adapted under
`processes/`; and this tracker + `log.md` + `index.md` reconciled. **Render the deployed surface and confirm
it paints** — a query-layer pass is not a deployment check (the E2/E3/E5/E6 sessions each caught a defect that
only the rendered surface showed). Then write the B4 boot prompt.

**THIS PHASE IS NOT:** building the Tradezella importer; adding features; or reopening any E1–E6 invariant.

---

## Boot Prompt (Phase B3b — provision, seed, and RENDER-verify) — ❌ **SUPERSEDED, NEVER RUN** (2026-08-12)

> **DO NOT EXECUTE THIS PROMPT.** It is kept only so the decision that killed it stays auditable.
> Paul decided on 2026-08-12 that **hosting is premature**, and `neurospect-learn` got a local Docker
> daily driver instead (§B3-local). Everything below describes provisioning Render, Cloudflare Pages and
> R2 — work that is now **parked, not cancelled**. Running it would provision paid infrastructure
> against an explicit decision not to. See the **2026-08-12** session log entry and the ⏭ ACTIVE prompt
> at the very bottom of this file.

> **This phase needs Paul at a browser.** The session cannot create a Cloudflare account, enter card
> details, or click through Render. Read §"Paul does / the session does" below before starting, and if
> Paul is not available to provision, say so and stop rather than inventing adjacent work.

**Launch:** `claude --model sonnet[1m]`, `/effort medium`. This is execution against a runbook that now
exists; nothing here is a design question. Escalate only if provisioning uncovers something the runbook
did not anticipate.

**Task: finish B3. Get `neurospect-learn` reachable, seeded, and PROVEN at the rendered surface.**

**State, exactly.** The preparation half is committed-ready and locally proven: `render.yaml`,
`requirements.txt`, `app/public/_redirects`, the fail-closed Discord allowlist, tolerant env parsing,
`.env.example` on both sides, and the runbook. 294 backend tests pass, the frontend builds, and
`scripts/scratch_migrate.py` reports `RESULT: REVERSIBLE`. **Nothing is provisioned. Nothing is
deployed. Nothing has been rendered or verified.** Do not let the volume of finished config read as a
finished phase — the phase's value is the last mile, and none of it is done.

READ FIRST:
1. The wiki `CLAUDE.md` — **code is ground truth**, the MANDATORY post-implementation reconciliation
   checklist, Rules #3/#4/#6, Context Management (tell Paul at >50%). **Paul handles git.**
2. [[processes/operations/neurospect-learn-deployment]] — **the runbook. Follow it; do not re-derive
   it.** Its §Differences table exists because the older `neurospect-api` page would mislead you in
   nine specific places.
3. This tracker's **2026-08-11 (second session)** log entry — the four measured findings, and the one
   defect deliberately left unfixed.

**Paul does** (runbook §1–§4, browser only): the R2 bucket + scoped API token on a **personal**
Cloudflare account; the Discord redirect URI; the Render Blueprint + env vars; the Pages project with
root directory `app`. **The session does**: talk him through each step with exact values to paste, then
§5 (seed production from the laptop) and §6 (verify).

⚠️ **Non-negotiables, each of which has already cost something:**
- **Ask before touching any credential**, name the secret and its source, and **never echo a value** into
  chat, a log, a commit or the wiki. Paul's standing rule.
- **The seed step writes to a live database.** Run the runbook's target-proving pre-flight first and
  read it: if either line says `localhost:5433`, stop. Exporting `DATABASE_URL` alone does **not**
  redirect these scripts, and that trap has wiped the local seed twice. **Never** run a bare
  `alembic downgrade`.
- **Anchor the seed** against 74 / 23 / 58 / 67 / 44 / 104 and `alembic_version` `0012`. User-data tables
  must be **0** in production; the local counts for those are fixtures and test residue.
- **A green health check is not a deployment check.** E2, E3, E5 and E6 each caught a defect that only
  the rendered surface showed.

DELIVERABLES:
1. **Every page painted**, walked one by one, with **labelled screenshots** captured to the repo's
   evidence folder — and a written note of which interactions respond and **which are inert**. A silent
   no-op is a finding, never an acceptable default.
2. **The R2 proof, which is the one test this phase exists for:** upload a chart capture, confirm the
   thumbnail renders, **then redeploy and confirm it still renders.** On the local backend it would be
   gone while the row survived. If this is not run, B3 is not done.
3. The allowlist proven from the outside: Paul logs in; a non-allowlisted account is refused.
4. Runbook + tracker + `log.md` + `index.md` reconciled with what actually happened — **including every
   step where reality diverged from the runbook**, which is the part that pays off next time.
5. Then the **B4** boot prompt (capture-first in `neurospect-learn`, per §Phase B2+), which should carry
   the **two-clock** finding: the planner counts "today" in the user's timezone while migration `0012`'s
   trigger enforces server UTC, and deployment makes that permanent.

**THIS PHASE IS NOT:** building the Tradezella importer; adding features; reopening any E1–E6 invariant;
or fixing the two-clock design (record it for B4 — changing it touches E6 semantics).

---

## Boot Prompt (Phase B4 — capture-first in `neurospect-learn`) — ➡️ **MOVED 2026-08-12, NEVER RUN**

> **DO NOT EXECUTE FROM HERE.** B4 was absorbed as **S2** of
> [[processes/distributed-workflow/active/aura-session-runner]] on 2026-08-12, before it ever ran. Its
> constraints were carried across intact; this text is kept only so the move stays auditable. The active
> lane for Neurospect is now that tracker's **S1** boot prompt. Everything below is superseded — including
> its "State, exactly" paragraph, which predates the runner lane.

**Launch:** `claude --model opus[1m]`, `/effort high`. Unlike B3, this phase contains **real design
questions** — what a pre-session pre-commitment *is*, and how consistency is measured — and it touches the
E5 ledger and E6 semantics, where a wrong shape is expensive to undo. Escalate rather than economise.

**Task: build capture-first support for a backtesting session `neurospect-learn` does not host.**

**State, exactly.** B1 is complete and said **DON'T BUILD the Tradezella importer** — read §COUNCIL VERDICT
before anything else; several sections above it were written while that bet was still open and read as
though it were. B3 is **closed**: the platform now runs as a local Docker daily driver on **:8001 / :5174**
(`docker compose up -d`), render-verified 2026-08-12, sharing the dev database on :5433. Hosting is
**parked, not cancelled**. **B2 — Paul's twenty Tradezella sessions — still gates this phase and is still
unrun**; see §"The honest thing to do first" below before writing code.

READ FIRST:
1. The wiki `CLAUDE.md` — **code is ground truth**, the MANDATORY post-implementation reconciliation
   checklist, Rules #3/#4/#6, Context Management (tell Paul at >50%). **Paul handles git.**
2. §COUNCIL VERDICT, then §Phase B2+ **B4** — `scholar`'s deliverable targets are **cue-usage (`CI`)** and
   **consistency**, and the reason capture must happen *during* the session is that the export
   structurally cannot carry it.
3. [[concepts/architecture/learning-enforcement]] §Invariants — in particular **E5** (a call cannot be
   back-dated, edited, re-resolved or deleted) and **E6** (computed-per-read, gates nothing, stores
   nothing). This phase writes *into* the frozen ledger, so it is the first phase whose bugs are
   permanent.
4. The **2026-08-12** session log entry — the local stack, the traps, and the four things left NOT done.
5. `api/docs/evidence/b3-local/b3-local-render-walk.md` — what is proven about the running surface, and
   the three UI paths still **unverified** (filtering driven to a result, `Check against the bar`, E4).

⚠️ **The honest thing to do first.** B2 is a gate, not a formality: three live, free, one-click discipline
instruments in Tradezella currently read **genuine ZERO**. If they stay empty after twenty sessions, *no
companion of any design survives* — including this one. **Ask Paul whether B2 has been run before building
capture surfaces**, and if it has not, say so plainly and offer to scope B4 against the existing E5/E6
primitives *without* building new capture UI yet. A council that tells its sponsor to practise for twenty
sessions before writing code was doing its job; do not quietly overrule it.

⚠️ **Carry the two-clock finding, and treat it as a design input, not a bug to swat.** The planner counts
"today" in the user's timezone (`study_preferences.timezone`, default `"UTC"`) while migration `0012`'s
trigger enforces server UTC (`(now() AT TIME ZONE 'UTC')::date`). They agree for a user at or ahead of UTC
(Paul) and disagree west of it. **A pre-session pre-commitment is precisely a claim about ordering in
time**, so B4 cannot avoid choosing a clock the way earlier phases could. Changing it touches E6 semantics
— decide deliberately and write the decision down.

**Local-stack gotchas that have already cost something (from §Local stack in the runbook):**
- **Never `docker compose down -v`** — the volume is not declared `external: true`, so it would delete the
  seed *and* every captured chart. **Fixing that one-line declaration is the cheapest win available and is
  still open.**
- **Never `alembic downgrade base`** against the working DB — exporting `DATABASE_URL` does not redirect
  Alembic (`.env`'s `DATABASE_URL_SYNC` wins). This has wiped the seed twice. Use
  `scripts/scratch_migrate.py`.
- **Do not trust `--reload`** on the host dev server; the reloader has died silently and served stale code
  through a whole before/after measurement.
- If you rebuild `app`, remember `VITE_*` are **build args** — as `environment:` they silently do nothing
  and the bundle falls back to the **dev** API on :8000.

DELIVERABLES:
1. A decision, written down, on whether B4 builds now or waits on B2 — and if it builds, **what it builds
   without new capture UI**.
2. If it builds: a pre-session pre-commitment authored *before* the replay is advanced, stamped by
   `neurospect-learn` (the one artifact whose ordering can be trusted), plus consistency-across-setups
   measurement — one rubric, many captures, variance in cue usage.
3. Any backtest-derived data that is ever imported must be permanently and visibly quarantined as
   `SELF-REPORTED` and excluded from the evidence streak, the calibration score and the Readiness Gate
   (`devil`'s criterion #2) — and the design must then state what value remains, because that residue *is*
   the bet.
4. **Render-verify at the surface** on :5174, with labelled screenshots into
   `api/docs/evidence/b4/`, and a written note of which interactions respond and **which are inert**. Four
   phases in a row have caught a defect only the rendered surface showed; B3-local made that five.
5. Runbook + tracker + `log.md` + `index.md` reconciled, **including every place reality diverged** — then
   the B5 boot prompt.

**THIS PHASE IS NOT:** building the Tradezella importer (B1 killed it); provisioning Render or R2 (parked —
do not spend Paul's money on a decision he reversed); or reopening any E1–E6 invariant.
