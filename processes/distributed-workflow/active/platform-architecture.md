---
tags: [distributed-workflow, active, neurospect, architecture, monorepo, micro-frontend, platform, agent-factory, council]
aliases: [Platform Architecture, Suite Architecture, Micro-App Architecture, The Council]
sources: []
created: 2026-08-29
updated: 2026-08-29
---

# Platform Architecture — Workstream Tracker

Decide **whether — and if so how — the Neurospect estate becomes one product** instead of several
repos that share a name. Paul's framing: the apps are *micro-apps in a platform*. This workstream
tests whether that framing survives contact with what is actually on disk **and with the positioning
the estate already committed to**, and only then produces an architecture.

⚠️ **The title is a question, not a plan.** An earlier version of this line read *"Decide how the
estate becomes one product"*, which assumed the answer. F5 is why that was wrong.

> **STATUS (2026-08-29): COUNCIL RUN — verdict is PROCEED-WITH-CONDITIONS, and the conditions are
> two gates that cost nothing.** Nothing has been designed or built. The estate is measured
> (§Measured state), **eleven findings** recorded — F1–F7 and F11 in §The findings most likely to be lost,
> F8–F10 in §Council results — and a
> five-lens council has reported (§Council results).
>
> ⭐ **The council's answer was not an architecture.** It was: *the platform is closer to ready than
> the estate looks, the differentiator is narrower than claimed, and the next step involves no code
> at all.* See the `next:` line.
>
> ⚠️ **This workstream is not yet known to be legitimate.** F5 records that the estate committed on
> 2026-08-10 to a positioning close to the **opposite** of what this tracker proposes. Until Paul
> resolves that (§Blocked on a human), treat the whole tracker as a *proposal awaiting a decision*,
> not as an approved lane.

> ⚠️ **THREE TRACKERS ARE `⏭ ACTIVE`** (measured 2026-08-29): this one,
> `aura-session-runner.md` §Boot Prompt (Phase S1e-b), and `backtest-companion.md` (Phase B4,
> capture-first). That is deliberate, not drift — they are different lanes. `/neurospect-boot` will
> find all three and **must list them and ask Paul which lane**, per its own rule. Do not merge them
> and do not silently pick one.

---

## Boot Prompt (Phase P0b — run the two gates) ⏭ ACTIVE

> ⚠️ **SUPERSEDED 2026-08-29 (same day).** The original `next:` was *"run the council."*
> **The council RAN** — five lenses, results in §Council results. Its answer was not an
> architecture, and the `next:` below replaces the original entirely. The old plan is retired, not
> paused.

**TWO LANES RUN IN PARALLEL. They do not compete — they spend different resources.**

**next: (Paul's lane — his time, not engineering time)** **Run the two gates in §The experiment.
28 days, ZERO code.** Gate A: define rules in the Tradezella Playbook and run **10 replayed
sessions** with `/runner` open — this is **B2**, written 2026-08-10 and **unrun for 19 days**.
Gate B: offer **5 traders a 4-week cohort at £150** over Discord and the existing tunnel.
**Both must pass before any PLATFORM work starts.**

**next: (engineering lane — added 2026-08-29 on Paul's direction)** **Deep code review of
`agent-factory`, and a plan to make it able to build the platform.** Paul's framing: *"agent-factory
is to eventually build out the platform — this is why a deep code review and plan needs to be run."*
This is legitimate alongside the gates because it consumes engineering time while the gates consume
Paul's, and because the factory build-out is a prerequisite for everything after the gates pass.

⭐ **THE CORRECTION THAT MAKES THIS LANE NECESSARY — the session made the error it was warning about.**
Earlier notes here said *"the factory cannot build the platform — 10 of 30 gates."* **That conflated
two questions.** `factory/readiness.py`'s own first line reads: *"Readiness: can an agent team run a
**connector migration** unattended?"* — and it measures against `$PREFECT_CONNECTORS`, **a different
repo** (31 references to `pipelines.py`, the wave scheduler, connector promote-gates).

⛔ **So 10/30 is NOT a measurement of "can the factory build product software." That question has
NO INSTRUMENT AT ALL — the honest verdict is `NOT-MEASURED`, not `FAIL`.** Collapsing a measurement
gap into a failure is exactly the error Paul's Evidence-Gated Analysis rule #3 forbids, and this
tracker committed it while citing that rule. ⚠️ The *properties* those 30 gates encode (attempt cap,
spend ceiling, concurrency bound, orphan reaper, verdict-from-history) **are** general to unattended
agent work — so 10/30 is a strong **prior** about the factory's discipline. It is not evidence about
this question.

**The load-bearing deliverable of the review is therefore an INSTRUMENT, not a plan:** a
`readiness`-shaped module scoped to *product build*, so "can the factory build this" stops being an
opinion and becomes a number that can be re-run. Proposed lanes: (1) what `product_contract.py` must
assert for "a feature in `neurospect-learn` is done" — **the verifier already exists**: 25 backend
test files, 68 Playwright specs, `check-tokens.mjs`, `check-contrast.mjs`, `render-walk.mjs`;
(2) triage the 0/4 bound gates — general vs connector-specific; (3) same for the 0/8 judgement gates,
flagging which failures could reach a student credential; (4) can `deploy.py` + worktrees safely put
a bounded worker into `neurospect-learn` today; (5) the sequenced plan.
⛔ **Single worker + non-LLM verifier, per F6 — not a build team.**
⭐ **FIRST ACTION OF THIS LANE: diff conductor's tested ICT detectors against
`neurospect-learn/api/scripts/aura_*.py` (F11).** It may be the largest piece of avoidable
duplicated effort in the estate, and it is cheap to check.

> ⛔ **Do not begin architecture, consolidation, multi-tenancy or the agentic layer.** All of it is
> retired ahead of the gates — not because it is wrong, but because it is **unfalsifiable in the
> short run and cannot produce a "no"**, while both gates can, in 28 days, for free.
>
> ⛔ **The premise that consolidation gates anything is REFUTED.** Commit `6c586d8` already shipped
> tunnel access. A real student can be served today, from the machine the platform already runs on.
>
> ⭐ **Gate A's threshold, stated before the test:** 8 of 10 sessions completed by day 14, each with
> rules-followed showing a **non-zero denominator**. B1's "ZERO" was really a `0/0` —
> **a second `0/0` is a KILL, not a pass.** Gate B: **2 of 5 paid before delivery starts** — money
> received, not "interested".

> ⛔ **Do not start by designing the platform.** The obvious move — "read the 13-component product
> hierarchy in `neurospect/CLAUDE.md` and design the shell around it" — is retired before it starts.
> That hierarchy is a **declaration, not a measurement**: 13 components are named, roughly 4 have
> code, and the roadmap that grades them (`neurospect/roadmap/status.md`) was last updated
> **2026-05-23 — over three months stale**. Designing against it means designing against a fiction.
>
> ⛔ **Do not begin by treating the four `neurospect*` repos as four apps to integrate.** Two of the
> four are fossils. See §The findings most likely to be lost — both were established with a
> discriminating test, and re-deriving them costs a session.
>
> ~~⛔ **Do not author a new five-lane council.**~~ **MOOT 2026-08-29 — the council already ran.**
> It was assembled ad hoc rather than via `⛏ prospect`; see §NOT done for what that cost. Do not
> convene another one: the next action is a test in the world, not more analysis.
>
> ⚠️ **STILL OPEN — ASK PAUL** (§Blocked on a human). This workstream may be a **reversal of a
> committed strategic decision** — the estate committed on 2026-08-10 to the *companion*
> positioning, described in the wiki as close to the **opposite** of platform consolidation. See
> **F5**. The council did **not** settle it, and neither did the student model. It is Paul's call to
> make knowingly. ⭐ **But it does not block the `next:` line** — both gates are worth running under
> either answer, which is precisely why they come first.

---

## Measured state — 2026-08-29

Run at scoping time. Re-measure rather than trusting these; they are stamped, not eternal.

```
repo               last commit   head
neurospect         2026-05-24    a2dc731 docs: update roadmap status to reflect actual codebase state
                                 branch: research/phase-0-research   dirty: 0
neurospect-app     2026-05-02    02447c4 broker: settings UI + active-trade guard (Phase 1c)
                                 branch: main   dirty: 0   tag: pre-monorepo-snapshot
neurospect-learn   2026-08-20    6c586d8 feat(learn): remote access — local stack via tunnel
                                 branch: main   dirty: 88 FILES
neurospect-wiki    2026-08-20    33e6852 docs(log): 2026-08-20 — neurospect-learn reachable via tunnel
                                 branch: main   dirty: 4
agent-factory      2026-08-23    f66c71c docs(findings): F75 + §17
                                 branch: feat/readiness-generator   dirty: 0

conductor/projects/neurospect                          <- FOUND LATE. See F11.
                   2026-06-18    e160160 feat(neurospect): ICT Event Intelligence engine (Phase 4)
                                 686 tracked files · NEWER than the monorepo by 25 days
```

⚠️ **This table was built by a NAME-PREFIX scan and therefore missed `conductor` entirely** — the
sixth codebase, and the newest Neurospect product code in the estate. **The basis was wrong, not
just the result.** Re-enumerate by CONTENT (`git grep -ril neurospect` across every repo) before
trusting any inventory, including this one.

Tracked-file counts inside the `neurospect` monorepo:

```
api 76 · app 125 · site 60 · neurospect-ui 63 · platform 3 · neurospect-api 0 (untracked clone)
wiki/ 125 (frozen 2026-05-20)   paul-wiki + vlad-wiki 63
```

⚠️ **CORRECTED.** An earlier version of this line read *"Only two repos have been touched since May."*
**That was an artefact of the name-prefix basis and is false.** `conductor/projects/neurospect`
carried Neurospect feature work through **2026-06-18**, 25 days after the monorepo went quiet.

The accurate statement: **product development moved from `neurospect` → `conductor/projects/neurospect`
and stopped there in June; separately, `neurospect-learn` + `neurospect-wiki` have run continuously
to 2026-08-20.** Those are two different lineages, not one. Any architecture has to explain both,
and must not assume the monorepo was ever the live centre after May.

---

## ⭐ The findings most likely to be lost

Each kills a premise a fresh session would otherwise adopt in its first ten minutes.

**F1 — `neurospect-app` is an archived predecessor, not a live micro-app. MEASURED.**
It carries the git tag `pre-monorepo-snapshot`. The monorepo README states the monorepo was created
2026-05-02 by merging three predecessor repos via `git filter-repo --to-subdirectory-filter`, and
that predecessor tips are tagged exactly that. It is also *older* (2026-05-02) and *smaller*
(9 pages vs 13) than `neurospect/app/`. The natural assumption — that a standalone repo with
recent-looking Phase 1c broker commits is a live fork that diverged — is wrong in the opposite
direction to how it reads. Discriminating test used: the tag, not the file contents. **Do not count
it as an app.**

**F2 — the wiki split back OUT of the monorepo, and three stale copies remain. MEASURED.**
`neurospect-wiki` is canonical: 217 tracked files, live to 2026-08-20. Inside the monorepo,
`wiki/` holds 125 files frozen at 2026-05-20, plus `paul-wiki/` and `vlad-wiki/` (63 more). So the
monorepo migration described in `monorepo-migration.md` **was partially reversed** and nothing
recorded it. Four wiki copies exist; three are fossils. Any content-ingest pipeline (and
`neurospect-learn` has one) that reads the wrong copy silently serves May's course content.

**F3 — `agent-factory` already has the council machinery. Do not hand-roll five agents. MEASURED.**
`factory/lanes.py` implements parallel lanes with a shared `PREAMBLE`/`POSTAMBLE`, file-locality
grouping, and validation of lane membership at import. `factory/teamplan.py` computes dependency
closure over `board.DEPENDS`. `docs/findings.md` is a cross-lane corrected-premise ledger the lane
preamble makes every agent read first. There is also a basis vocabulary already in use —
`MEASURED` / `ASSUMED` / `UNMEASURABLE` / `NOT_RUN` — and `factory.certify` to enforce it.
⚠️ **CORRECTED 2026-08-29 — see F6, which supersedes the rest of this paragraph.** This finding
originally repeated the factory README's line that "the instruments are not wired". **That README is
stale**: `certify` now returns `PASS (PASS=12)`, not the `PASS=11 + 1 UNMEASURABLE` the README
prints. The real constraint is not what the README says — it is what `factory.readiness` measures,
and that is **10 of 30 gates**, with the loop, the bounds and the success/failure discrimination all
at zero. Its lane grouping is also explicitly flagged `ASSUMED` and scoped to the *factory's own* 30
gates, not to a Neurospect architecture question. So: **borrow the discipline and the
findings-ledger pattern; do not assume the factory can execute this workstream for you.** F6 has the
numbers.

**F4 — the council of five ALREADY EXISTS. It is `⛏ prospect`. MEASURED.**
Paul asked for a council of five once before (recorded in `backtest-companion.md` §Recommended
tooling). The answer was to author one, and it was authored and dry-run on **2026-08-11**:
`C:\Users\PaulRussell\.claude\skills\prospect\SKILL.md`, lenses **`claimant` · `scout` · `scholar` ·
`canvasser` · `devil`**. It is *divergent* (discovery-shaped), boundary-first, and its boundary lens
**can halt the other four** — which is the property this workstream needs. It already enforces the
three disciplines this tracker would otherwise re-specify: boundary runs first and can halt; every
claim carries a source tier and a vendor claim is never a design premise; a zero from an unproven
instrument is not a measurement.
⚠️ **Read `backtest-companion.md` §Dry-run BEFORE briefing it** — the recorded lesson is that the
question-to-lens mapping is **not 1:1**, and that internal design questions must not be handed to an
external-facing lens. That caveat bites harder here than it did for B1: `prospect` was built for a
**product bet against an external incumbent**, and this is an **internal architecture** question with
no incumbent vendor. `scholar` and `canvasser` in particular have thin subjects. Adapt the brief
deliberately and write down what you changed; do not silently repurpose the lenses.
⛔ **Do not use `army`** — generic parallelism with no discipline attached. This was already decided.

**F5 — the committed lane is the OPPOSITE of platform consolidation. MEASURED — and this is the
finding most likely to cause expensive rework.**
`index.md` records the committed lane as of **2026-08-10**: `backtest-companion-layer` —
`neurospect-learn` as *the discipline + insight layer around a backtesting session held in another
tool*, with the **companion** positioning that follows: **"integrate with the apps a trader already
chose rather than absorb them."** The index states in terms that this is *"deliberately close to the
**opposite** of `platform-consolidation` / `vertical-ai-platform`"*, and that a design session is
required to argue the two against each other **on merit**.
⚠️ **A naming trap sits on top of this.** The existing `concepts/roadmap/ideas/platform-consolidation`
page is about absorbing **Discord + TradingView + Tradovate** — *third-party* workflow consolidation.
Paul's 2026-08-29 request is about **our own repos and micro-apps**. Same word, different question.
A council that greps for "platform consolidation" will read the wrong page and argue the wrong bet.
**Both readings must be kept distinct in every artifact this workstream produces.**

**F6 — the factory CANNOT orchestrate a build today, and its own instrument says so. MEASURED
2026-08-29.** Paul asked for `agent-factory` to build the estate. Measured directly:

```
pytest -q                                    247 passed
python -m factory.certify blueprints/windsorai_gep.yaml --calibrate
                                             PASS (PASS=12)   ← README says PASS=11 + 1 UNMEASURABLE; README is STALE
                                             but "REPLAYED, not a live measurement"
python -m factory.readiness                  10 of 30 gates pass
    Can the loop run?                        0 / 3
    Is it bounded?                           0 / 4
    Can it tell success from failure?        0 / 8
```

⭐ **The single most disqualifying line: "Has any gate ever refused a run? — 22 gate events
recorded, 0 of them a refusal."** That is Paul's own Evidence-Gated Analysis rule #3 firing inside
his own tooling: a zero from an instrument never proved able to register a non-zero is not a
measurement. The factory's safety gates have **never once said no**. Alongside it: no attempt cap on
the restart path (**worst observed 352 restarts of one stage in one run**, 1,004 `restart_from_stage`
events), no spend ceiling checked before dispatch, no reaper for dispatched work, and a terminal
verdict computed from last-write-wins current state rather than history — so **three runs recorded
`succeeded` over 115, 21 and 15 failures respectively**.

⛔ **And there is no contract for this domain.** `contract.py` is the root the README says everything
depends on, and only two real ones exist — `connector_contract.py` and `pbi_contract.py`, both
ALDC data-pipeline shaped (`demo.py` is a fake). **Nothing can express "a feature in a React +
FastAPI product is done."** A team with no contract is `UNGATED`, which `launch.py` and `teamplan.py`
deliberately render as *"nothing can be measured yet"* — not as *"nothing to do."*

⛔ **A multi-agent build team is already rejected by evidence.** `blueprints/orchestrator_team.yaml`
opens with `SUPERSEDED BY EVIDENCE 2026-08-21 — DO NOT BUILD THIS TEAM`, citing R2: a
180-configuration study across 5 architectures found multi-agent averaging **−3.5%** against
single-agent baselines, with **sequential tasks degrading 39–70%** — and building a product is
exactly that class. The recommended topology is **ONE worker agent + a non-LLM verifier in a clean
environment**, with no LLM manager, architect or tester, and the worker unable to author its own
PASS bit. The unlock threshold is written down and is a governance bar, not a vibe.

⚠️ **This does not say "never."** It says the ordering is fixed: contract → eval that can fail →
bounded loop → then a worker. Asking the factory to build the estate before that ordering is
satisfied is asking the 965-run loop question again, which is the exact failure the factory was
built to prevent.

**F7 — "agentically RUN" is a different claim from "agentically BUILT", and it is the more
interesting one. DERIVED from F6 + measured code.**
Paul, 2026-08-29: *"platform vision as an agentically run platform, once we build out
agent-factory."* F6 answers whether the factory can **build** the estate (not yet, and its own
instrument says so). This is a separate question: whether agents can **operate** the product —
grade student evidence, coach, watch cohort health.

⭐ **The estate already answers it, and the answer is yes-with-a-boundary.** Phase E4 shipped an
**AI-vision advisory second reader** that grades uploaded chart evidence in production, at a
measured **$0.0167/grade**. It is safe for exactly one reason, recorded at the time: it is
**advisory-only and structurally cannot move the Gate.** The same shape recurs in E6 — the honesty
strip is computed per read, **stored nowhere, gating nothing**, and `/api/gate` was proven
byte-identical to prove the strip could not leak into the verdict.

⭐⭐ **The deeper connection nobody has written down: `agent-factory`'s four-verdict discipline is
the right instrument for STUDENT assessment, not just for CI.** `PASS` / `FAIL` / `UNMEASURABLE` /
`NOT_RUN`, never collapsed, with the rule that *"a check whose instrument could not run has not
passed"* — that is precisely the distinction an instructor-led readiness credential needs. A student
who was never measured must not read as a student who failed, and neither may read as a pass. The
factory is therefore relevant to this platform as a **runtime discipline**, not only as a build tool
— and that is a materially larger claim than "the factory writes our code."

⛔ **The invariant this generates, and it is load-bearing for the whole business:** *no agent may
author the Gate verdict.* The Gate's non-overridability is the asset being sold to students and
(potentially) relied on downstream. An agentic layer that can move it destroys the product it is
supposed to run. Every agent role designed for this platform must state what it **may never decide**.

**F11 — ⭐⭐ THERE IS A SIXTH NEUROSPECT CODEBASE, IT IS NEWER THAN THE MONOREPO, AND IT HOLDS CODE
THAT EXISTS NOWHERE ELSE. MEASURED 2026-08-29. This is the most consequential finding in the
tracker.**

`C:\Users\PaulRussell\repos\conductor\projects\neurospect\` — **686 tracked files**, tracked by
`conductor` itself (not a nested clone, not session data). Its Neurospect commit history runs to
**2026-06-18 — 25 days AFTER the monorepo's last commit (2026-05-24).**

⛔ **Development did not stop at the monorepo. It MOVED to `conductor` and stopped there.** Any
survey that treats `neurospect` as the cold end of the estate is looking one repo short.

**What it holds that is in NO other repo — discriminating test run, both came back 0:**

```
git -C neurospect      ls-files 'api/app/ict'  ->  0 files
git -C neurospect-learn ls-files | grep -ci "ict/|market_event|detectors/"  ->  0
```

Commit `e160160` (2026-06-18) *"feat(neurospect): ICT Event Intelligence engine (Phase 4)"* —
**21 files, 1,677 insertions, 0 deletions** (net-new, not a copy):

- **7 detectors**: `fvg.py` · `liquidity_sweep.py` · `market_structure.py` · `opening_price.py` ·
  `order_block.py` · `session.py` · `swing.py`
- models `bar.py` · `market_event.py` · `trade_event_link.py`; router `market_events.py`;
  services `event_runner.py` · `market_data.py`; migration `0008_ict_events.py`
- ⭐ **`tests/test_ict_detectors.py` — 491 lines of tests.**

⚠️ **The roadmap says this phase is `not_started`.** `neurospect/roadmap/status.md` grades
Phase 4 (ICT Event Engine) as **not_started**. It is built and tested, in a repo the roadmap does
not name. Third independent confirmation that the roadmap is fiction (see F-block above).

⭐⭐ **THE REUSABILITY CONSEQUENCE, and it is expensive if missed.** `neurospect-learn/api/scripts/`
has been **re-deriving setup detection from scratch** across S1c/S1e — `aura_setup_engine.py`,
`aura_qt_smt.py`, `aura_pd_arrays.py`, `aura_erl.py` — and that hand-rolled work accumulated
**five defects found by reading logs**, including the lookahead bug that contaminated 75% of output.
Meanwhile a **tested** detector library for the same primitive objects (FVG, sweep, market
structure, swings, sessions, order blocks) has existed since June, one repo away.
**Before any more detector work: diff the two. This may be the single largest piece of avoidable
duplicated effort in the estate.** (⚠️ `NOT-VERIFIED`: whether conductor's detectors implement the
*same* definitions Aura needs — S1e corrected two SMT objects and the target definition. The
detectors may be right, wrong, or right-for-a-different-model. **Diff them; do not assume either
direction.**)

⛔ **AND THE COUNTING-BASIS LESSON, which is why this was missed for the whole session.** The
scoping pass enumerated repos by **name prefix** (`neurospect*`) plus `agent-factory`. That basis
cannot see a Neurospect codebase living inside a differently-named repo — and the most important one
does. **The correct basis is content, not name.** A content scan
(`git grep -ril neurospect` across every repo) surfaced it immediately.
⚠️ **Therefore the inventory is now "at least six", not "six".** A complete enumeration is a
deliverable of the review, not something this tracker may claim to have finished. Other repos with
incidental hits, all unassessed: `wiki` (15 files), `aldc-launchpad` (5), `aldc-shipyard` (1),
`snakeplane` (1), `triage-agent` (1).

⚠️ **Also unassessed in `conductor/projects/neurospect`:** commits marking *Phase P2 Trader
Workspace complete*, *Phase 0 acceptance suite — 115 tests*, *Phase 0B — CI/CD + 18 tests*, three
interactive walkthroughs, redesigned pricing, and phases *P12 Live Futures Trading* / *P13
NeuroSync* that appear in no roadmap this session read. **686 files. Nobody has surveyed them.**

---

## The council — use `prospect`, adapted

⛔ **Do not invent a new lane split.** Use `⛏ prospect` (F4) and adapt its brief. The adaptation
below is `ASSUMED` — a judgement, written down so it can be argued with rather than improvised — and
the lens names are `prospect`'s, not new ones.

| `prospect` lens | Adapted subject for this workstream | Halts the workstream if |
|---|---|---|
| **Boundary** (runs first, can halt) | What can *actually* compose at runtime across our own apps? Auth, JWT issuers, DBs, ports, deploy targets, CORS. Two backends currently mint their own JWTs on purpose. | **Nothing can cross.** If the apps cannot share a session or a user without a rewrite, "micro-apps in a platform" is dead as stated and the workstream re-scopes before anyone designs a shell. |
| **Incumbent** | Our own estate as the incumbent: enumerate every repo, app, surface and duplicate copy; which is canonical, which is fossil, on what evidence. Plus the wiki → ingest → API path and where overlapping domain models sit. | — |
| **Scholar** ⚠️ thin subject | Retarget from learning science to **architecture evidence**: monorepo vs polyrepo, micro-frontend composition, shared design systems. Same tiering rule — a vendor's or framework's marketing claim is never a design premise. | — |
| **Canvasser** ⚠️ thin subject | Retarget from market demand to **cost of carry**: what each composition model costs to build and maintain at n=1 developer. State the population honestly — this estate has one developer and, per B1, one user. | — |
| **Devil** | Argue the bet is wrong. The strongest available case: the estate already committed to the opposite (F5), only two repos have moved since May, and consolidation is a large refactor with no user asking for it. | — |

**Add one more subject, not a sixth lens: `agent-factory` leverage.** What the factory can genuinely
do for this platform *today*, verified, versus what is aspiration — its own README says Phase A is in
progress and "the instruments are not wired" (F3). Read-only on that repo. Fold it into **Incumbent**
rather than growing the council; five orthogonal lenses is the design, and a sixth would overlap.

### Rules every lane inherits

1. **Declare the counting basis before producing any count.** "How many apps do we have" has no
   answer until *one app* is defined. Write the definition down before counting, not after seeing
   the data.
2. **Enumerate the population. Never sample and generalise.** These sets are small enough to walk
   completely. "I checked the three obvious repos" is a hint, not a finding.
3. **Every claim carries its basis: `MEASURED` / `DERIVED` / `ASSUMED` / `NOT-SEARCHED`.** Borrow
   the factory's vocabulary so the artifacts interoperate. An unmarked claim is rejected at review.
4. **Never inherit a premise — including from this tracker.** The measured state above is stamped
   2026-08-29. Re-run it. If a number moved, the finding is that it moved.
5. **Separate ABSENT from NOT-SEARCHED.** "There is no shared auth layer" and "I did not look for
   one" are different verdicts and must not collapse into the same sentence.
6. **Read-only. No lane commits, edits, or deletes anything in any repo.** Fossil repos especially:
   identifying `neurospect-app` as dead is a finding, deleting it is not this workstream's call.

---

## Council results — 2026-08-29

Five lenses ran in parallel, read-only. **Every load-bearing claim was independently re-verified
against source before being recorded here, and two were REFUTED.** Those two are written down as
corrections rather than findings, because the corrected version is what the next session needs.

### The experiment (the deliverable — see `next:`)

| Gate | Test | KILL | PROCEED |
|---|---|---|---|
| **A — does the builder use it?** | 10 replayed sessions, `/runner` beside Tradezella. This is B2. | < 8 of 10 by day 14, **or a second `0/0` denominator** | 8+, each with a non-zero rules-followed denominator |
| **B — will anyone pay?** | 5 traders, 4-week cohort, £150, over Discord + the tunnel, using the **57 teachable wiki pages** that already exist | < 2 of 5 **paid** before delivery starts | 2+ paid |

Both must pass. Gate A alone is `n = 1` again; Gate B alone sells a discipline product its author
does not practise. Cost if it kills the bet: 28 days and no code — and Gate A produces the
wins-and-losses tally **S1e needs anyway**, so it is not a detour from the roadmap, it *is* the
roadmap's own gate.

### ⛔ Two council claims REFUTED on re-verification — do not re-inherit either

**R1 — "the Gate is known to be wrong."** The devil lens argued S1e's detector defects (2026-08-15)
invalidate the Gate. **Refuted by discriminating test:**
`grep -rn "aura_setup_engine\|aura_qt_smt\|aura_pd_arrays" api/app/` returns **empty** — the engine
lives in `api/scripts/` and is imported nowhere in the app. `compute_readiness` takes
`concepts, ladder, groups, attested, corroboration`; no detector output reaches it. The lens
accepted the correction and downgraded its own argument. **What survives is narrower and real:** the
Aura model's *definition* changed 14 days ago, so progress and journal rows recorded before it were
recorded against the old definition. That is **curriculum freshness feeding a sound instrument** —
a different problem with a different fix.

**R2 — "multi-tenancy is foundational."** Written into an earlier version of this tracker and the
artifact. **Refuted:** 10 models already carry `ForeignKey("users.id")`; all 12 routers resolve the
caller via `get_current_user` and scope to `user.id` — **212 references**. The five verdict services
are pure and DB-free (`gate.py`: *"PURE and DB-agnostic (no DB, no I/O)"*). An instructor viewing a
student is the same pure function with a different `user_id`. **Actual remaining work: one migration
(`users.role`, `cohorts`, `enrollments`), one dependency (`get_viewed_user`), one replacement of the
`ALLOWED_DISCORD_IDS` env var that is currently the entire enrolment system.**

### F8 — the market bound. MEASURED, population stated.

Searched 9 prop firms, 6 journals, 2 verification services, 8 cohort platforms, ~14 Discord price
points. **Prop firms accept ONLY their own paid evaluation — ABSENT across all 9.** Every industry
"fast track" means *pay more to skip our eval*, never *prove yourself elsewhere*; the one
near-exception is intra-group and discretionary, and that firm's own site says the education arm
"is education, not evaluation."

Population named, so this is ABSENT and not NOT-SEARCHED: Topstep, Apex, MyFundedFutures, Take
Profit Trader, FTMO, Earn2Trade, Bulenox, Tradeify, Alpha Futures. Every industry "fast track" —
Apex instant funding, Alpha "Direct", Tradeify "Lightning", Bulenox "Momentum" — means *pay us more
to skip our own evaluation*. The one near-exception (a £3,999 Ofqual L5 diploma offering a "direct
pathway… for the right candidates") is **intra-group and discretionary**, and that firm's own site
says the education arm "is education, not evaluation."

⛔ **Therefore "Funded" CANNOT be a step the platform delivers — only one it predicts.** The honest
terminal state is *ready to attempt an evaluation*. Context for the funnel: one major firm publishes
a **16.8% evaluation pass rate** and **33.3% of funded traders ever taking a payout**.

⭐⭐ **The datum that makes the reposition STRONGER, not weaker — and it is the best commercial
finding of the council.** `REPORTED` tier: **~70% of evaluation failures are daily-loss or drawdown
breaches, concentrated in week one — failures of RULE ADHERENCE, not of strategy.**

That is precisely what a computed gate can measure, and precisely what `prop_shield.py` (232 lines,
in the frozen monorepo) already implements — trailing drawdown monitoring, daily loss limits,
lockouts. So:

- **"We get you funded" is not a claim you may make.** No firm accepts outside evidence.
- **"We make you pass their evaluation" IS defensible**, because the dominant failure mode is the
  one thing this platform is built to instrument.
- ⭐ **This re-ranks the absorb list.** `prop_shield.py` moves up beside `tradovate.py`: broker-sync
  makes the evidence un-fakeable, and prop-rule tracking addresses the actual thing that kills 70%
  of candidates. Together they are the product's commercial core, not peripheral features.
- ⚠️ `REPORTED`, not `OBSERVED` — sourced from industry reporting, not from a firm's own published
  cohort data. **Verify before it appears in any marketing copy.** It is strong enough to steer the
  roadmap and not yet strong enough to sell on.

⭐ **And the differentiator is narrower than claimed.** No one sells an evidence-derived readiness
*credential* (genuinely ABSENT, searched). But **two of the three legs already ship cheaply**: one
journal computes a non-self-declared PASS/FAIL against prop rule sets from **broker-synced** futures
fills at ~$20/mo; another issues un-fakeable broker-connected track records; a free academy gives
auto-graded drills. **What is actually absent is the instructor-graded leg and the binding of the
three.**

⭐⭐ **Consequence nobody had ranked correctly: `tradovate.py` (389 lines, in the frozen monorepo) is
the COMPETITIVE PARITY item, not a nice-to-have.** A competitor verifies from broker-synced fills;
this platform's evidence leg rests on manually logged journal rows, and **four of the Gate's seven
checks are the student's own attestations** — `compute_readiness(attested: dict[str, bool])`, with
`detail="self-attested"` in the code. **"Non-overridable" describes the arithmetic, not the
inputs**, and that must be stated rather than marketed past under a sold credential.

### F9 — what agents may do. MEASURED.

Verdict: **PROCEED, premise narrowed.** An agent already operates on student evidence in production
(E4) and is safe for one reason that generalises carefully: **it was made structurally incapable of
holding a verdict, not trusted to hold one well.** Three constructions, none a prompt — a schema
with no free-text and no numeric field (`test_the_schema_cannot_carry_a_number_anywhere`); `failed`
unreachable by construction so every crash lands on `ungraded`; no write surface on progress.
*"A prompt instruction could be ignored; a schema cannot."*

- **NEVER agent-authored, permanently:** the Gate verdict; the four attestations (first-person
  claims about an *unobservable past* — an agent asserting one is fabricating, not inferring);
  ladder/rep advancement; any judgement of chart *correctness* (MeasureBench: frontier VLMs 19–30%).
- **Two things break COMMERCIALLY though the technical boundary holds:** free-text coaching has no
  schema, so it reintroduces exactly the hole E4's schema closed, and paid personalised commentary
  is a lawyer's question (⚠️ `NOT-SEARCHED` — no legal analysis performed, no check for existing
  disclaimers); and the Gate as a *sold* credential rests partly on self-report.
- ⛔ **No per-user grading cap or budget exists** — grep across `config.py`, `ai_grade_queue.py`,
  `routers/evidence.py` returns nothing. Spend is bounded only by the Discord allowlist. Adequate
  for one user; **not a COGS control for a paying cohort.** Build before the first student.
- ⚠️ **Subtlest risk:** `summarise()` already emits a 0–100 advisory score that **nothing reads
  today**. The moment a planner or coach reads it, a 19–30%-reliable perceptual signal becomes a
  curriculum driver. No gate added — a number just got read.

### F10 — brand. Decisions, not adjectives.

**Positioning: *"The only trading academy where you cannot mark your own homework."*** All three
proof points verified in code: reps derived not minted (`0009` renamed the writable column to
`legacy_reps`); the call frozen by a DB trigger (`predictions_freeze_the_call()`); no `cleared`
column exists anywhere.

- **Keep the name.** "neuro-" baggage is a marketing liability, not a credibility one, and the
  product never claims a brain mechanism. ⛔ **But cut the 13 declared sub-brands to three** —
  academy, prop wedge, verdict. A solo operator publishing an org chart of 13 named products reads
  as the fake-institution signalling the brand exists to oppose.
- ⚠️ **Casing defect, verified:** `pages/library.tsx:72` and `pages/runner.tsx:230` say
  "Neurospect"; canonical is "NeuroSpect" (`wordmark.tsx`, `index.html`). Also 3 instances in
  `data/aura-runner.json` — projected content, so fix at the **wiki** source, not the JSON.
- **Canonical accent: hue 210 (`cyan`)** — structural, not taste: the only preset far from the
  entire status scale, so a brand accent can never be misread as a verdict. Keep all five as
  settings (configurability is itself a rigour signal); ship 210 in every screenshot.
- ⭐ **`logo.tsx` hardcodes rung opacities `0.45/0.65/0.82/1.0`. Bind them to `--ladder-1…4` and the
  mark renders a specific student's tier** — one token change turns decoration into something earned.
- **Every measured figure gets `tabular-nums`; targets and aspirations do not.**
- **The Gate Card** (shareable verdict): denominator always on the face; blockers as prominent as
  clears (*a card that can only say good things is an ad*); cannot be self-issued, so it carries a
  live-recompute verification link; carries the NOT-MEASURED states; dated, and it expires.

---

## Phase P1 — the co5 review (RETIRED — the council already ran; see §Council results)

Verify the council's load-bearing claims adversarially before any of them become architecture.
Every claim that would *change the design if false* gets a verifier whose job is to refute it
against real code. Anything that survives is promoted; anything that does not goes into a findings
ledger modelled on `agent-factory/docs/findings.md`, so the next session does not rebuild it.

The three claims most likely to be wrong, and most expensive if wrong:

- "These apps can share a session." (**Boundary** — two backends currently mint their own JWTs.
  `neurospect-learn`'s README says so explicitly and calls it deliberate.)
- "The wiki ingest reads the canonical copy." (**Incumbent** — see F2. Four copies exist.)
- "The design system is portable." (**Incumbent** — the token layer is coupled to Tailwind v4
  `@theme inline` semantics and a `.dark` class contract; the monorepo app may not be on v4 at all.)

## Phase P2 — architecture, and only then product framing

Deliberately last. Produces the composition model (shell? module federation? separate deploys with
a shared identity service? one monorepo again?), the migration path, and what it costs — grounded
in P0's inventory and P1's surviving claims.

---

## NOT done — read this before claiming anything is in flight

- ~~**The council has not run.**~~ ✅ **CORRECTED — it ran 2026-08-29.** Five lenses, results in
  §Council results, two of its claims refuted on re-verification. This line is kept struck through
  rather than deleted so the correction stays auditable.
- **NEITHER GATE HAS BEEN RUN.** Gate A (10 replayed sessions) and Gate B (5 paid seats) are the
  `next:` action and **nothing has been attempted on either**. Everything downstream is blocked on
  them by the council's own verdict.
- **No architecture exists in any form.** No diagram, no decision, no ADR, no spec.
- **`⛏ prospect` was NOT used.** The council was assembled ad hoc from five briefed general agents,
  because Paul asked for it mid-session and the lens subjects needed adapting (F4 predicted exactly
  this: `prospect` is built for a bet against an *external* incumbent, and two of its five lenses
  have thin subjects here). ⚠️ **So the council ran without `prospect`'s enforced source-tiering and
  halt machinery** — the disciplines were briefed in prose instead. Treat its output as good but
  less structurally guaranteed than a `prospect` run, and note that F4's advice was therefore
  followed only in spirit.
- **`neurospect-learn` has 88 uncommitted files on disk.** They were NOT reviewed during scoping and
  their contents are unknown to this tracker. Read them before touching that repo — this has bitten
  twice per `/neurospect-boot`'s own pre-flight. Paul commits; never commit for him.
- **A design-spec workstream for `neurospect-learn` was started and abandoned mid-question** in the
  2026-08-29 session, in favour of this one. The design questions (visual direction, redesign depth,
  audience) were **asked and never answered**. If platform architecture lands first, that spec should
  be re-scoped as a *platform* design system rather than one app's reskin. Nothing was written.
- **`neurospect/roadmap/status.md` has not been re-measured** against code since 2026-05-23. Its
  per-phase `complete` / `in_progress` grades are unverified and must not be quoted as current.
- **No decision on where this tracker lives.** It is in the wiki so `/neurospect-boot` finds it;
  the generic `/boot` skill would put it in `aldc-launchpad/boot-prompts/`. Paul to confirm.

## Blocked on a human

**⭐ THE ONE THAT GATES EVERYTHING — ask it at STEP 0, before any lane is dispatched.**

**Is this a reversal of the companion positioning, or a question about internal code structure only?**
They are compatible or contradictory depending on the answer, and the council's brief is completely
different in each case:

- **(a) Internal structure only** — the repos are messy, share code badly, and should be organised as
  one coherent codebase. The *product* stays a companion that integrates with the tools a trader
  already chose. **No strategic reversal. The council scopes to code architecture.**
- **(b) Genuine product reversal** — Neurospect becomes the platform that absorbs the workflow, and
  the micro-apps are its surfaces. **This contradicts the 2026-08-10 commitment** and the index's
  requirement that the two be argued against each other *on merit* before either is adopted. The
  council must then include that argument as its primary output, not a footnote.

⛔ **Do not infer this from the phrase "micro apps in the platform".** It reads naturally as either.
Paul said both "integrate all neurospect repos" (structure) and "architect this platform as a
product" (positioning) in the same message.

Also open:

- **Lane choice.** Two trackers are `⏭ ACTIVE`. Paul picks: this one, or Aura S1e-b.
- **Scope of "all neurospect repos".** Scoping found
  `conductor/.conductor-sessions/…/projects/neurospect/` — a *fifth* full copy of the monorepo
  inside another repo's session data. Almost certainly noise, but confirm it is excluded rather
  than assuming.
- ~~**Commercial intent.**~~ ✅ **ANSWERED by Paul, 2026-08-29** — and it changes the architecture
  more than anything else in this tracker. Paul's words: *"a seamless prop traders dream platform.
  I would manage students through them."*

  **The business model is instructor-led education for prop-firm traders.** Consequences, none of
  which the earlier fork (§Blocked, branches a/b) anticipated — **this is a third option, not
  either of the two**:
  - **Multi-tenancy is now a requirement, not a maybe.** Students are users. Today the estate is
    single-user in every measured respect and every number in E1–E6 came from one person's fixtures.
  - **An instructor surface does not exist anywhere.** No cohort view, no roster, no
    student-progress rollup, no permissioning. This is net-new, not integration.
  - **`neurospect-learn` becomes the spine, not a peer.** It already holds the mastery ladder, the
    evidence-derived reps, and the non-overridable Readiness-to-Live Gate — which is precisely the
    instrument an instructor manages students *against*. It is also the only live app.
  - **The Gate becomes the credential.** Its existing property — *computed, not declarable, not
    overridable* — is exactly what makes it defensible when a third party (a prop firm, or a paying
    student) is relying on it. That is a product asset the monorepo has no equivalent of.
  - **Prop Shield gains a reason to be absorbed.** Prop-firm rule tracking is the monorepo's one
    component with direct relevance to *prop* traders specifically.
  - ⚠️ **It does NOT settle the companion-vs-consolidation question (F5).** "I manage students
    through the platform" is compatible with the companion positioning — students can still trade in
    Tradezella and TradingView. The reversal question stays open and still needs Paul.
  - ⛔ **New compliance surface.** Managing students against a readiness verdict is closer to
    instruction than to journaling. `neurospect/roadmap/status.md` already lists per-phase compliance
    gates including *"not financial advice"* and content licensing. Unscoped here; must not be
    designed around silently.

## Gotchas earned

- ⭐⭐ **PAUL RUNS SESSIONS IN PARALLEL (stated 2026-08-29). Every measurement in this tracker is
  therefore VOLATILE, and a cold session must re-measure rather than trust a stamp.** Observed live:
  `neurospect-learn`'s uncommitted count moved **88 → 90 during this session**, and this session
  wrote nothing to that repo. Consequences that have already nearly bitten:
  - A "dirty: N" figure is a reading, not a fact. Re-run `git status --short` before acting on one.
  - **Another session may hold the same files.** Before editing `neurospect-learn`, check whether
    the working tree is mid-change from elsewhere — and never `git checkout`/`stash`/`reset` to
    "clean up" what looks like stray work.
  - Two `⏭ ACTIVE` trackers plus this one means parallel lanes are the norm here, not an accident.
    `/neurospect-boot` must list all three and **ask**, never pick.
- ⛔ **Do not conflate an instrument's SCOPE with its VERDICT.** `factory.readiness` answers
  *"can an agent team run a connector migration unattended?"* against `prefect-connectors`. Quoting
  its 10/30 as a verdict on Neurospect platform-build readiness is a category error this tracker
  made and had to correct. Read a measurement tool's own docstring before citing its number.
- ⛔ **Enumerate repos by CONTENT, never by name prefix.** The name-prefix basis missed
  `conductor/projects/neurospect` — 686 files, the newest Neurospect product code in the estate.
  See F11.

- `/neurospect-boot`'s pre-flight is not optional: uncommitted work in `neurospect-learn` and
  `neurospect-wiki` has twice been described by a boot prompt as already written.
- Do not trust uvicorn `--reload` for before/after measurement — the reloader has died silently
  leaving a worker on stale code.
- `neurospect/neurospect-api/` has **0 tracked files** — it is an untracked local clone sitting
  inside the monorepo, not a component. `neurospect-ui.zip` and `neurospect-ui-extracted/` alongside
  it are likewise artifacts, not source.
- The monorepo is on branch `research/phase-0-research`, **not** `main`. A session that assumes
  `main` reads different code.

## Where things live

| What | Path |
|---|---|
| This tracker | `neurospect-wiki/processes/distributed-workflow/active/platform-architecture.md` |
| Canonical wiki (live) | `C:\Users\PaulRussell\repos\neurospect-wiki` — 217 files |
| Stale wiki copies | `neurospect/wiki`, `neurospect/paul-wiki`, `neurospect/vlad-wiki` |
| Monorepo | `C:\Users\PaulRussell\repos\neurospect` (branch `research/phase-0-research`) |
| Live learning platform | `C:\Users\PaulRussell\repos\neurospect-learn` (`app/` React 19 + Vite 8 + TW v4, `api/` FastAPI) |
| Design token layer | `neurospect-learn/app/src/index.css` + `app/scripts/check-tokens.mjs`, `check-contrast.mjs` |
| Archived predecessor | `C:\Users\PaulRussell\repos\neurospect-app` (tag `pre-monorepo-snapshot`) |
| Agent factory | `C:\Users\PaulRussell\repos\agent-factory` (branch `feat/readiness-generator`) |
| Factory lane machinery | `agent-factory/factory/lanes.py`, `teamplan.py`, `board.py`, `certify.py` |
| Factory findings ledger | `agent-factory/docs/findings.md` |
| Product hierarchy (declared, unverified) | `neurospect/CLAUDE.md` §Product Hierarchy |
| Roadmap (stale 2026-05-23) | `neurospect/roadmap/status.md` |
| **The council skill** | `C:\Users\PaulRussell\.claude\skills\prospect\SKILL.md` (+ `references/prospect-brief-template.md`) |
| **Its dry-run lessons — read first** | `neurospect-wiki/processes/distributed-workflow/active/backtest-companion.md` §Dry-run and §Recommended tooling |
| Committed lane (the opposite bet) | `concepts/roadmap/ideas/backtest-companion-layer.md` |
| The *other* platform-consolidation (3rd-party, not ours) | `concepts/roadmap/ideas/platform-consolidation.md` |
| Positioning page | `concepts/roadmap/ideas/vertical-ai-platform.md` |
| Prior UI/design idea page | `concepts/roadmap/ideas/ui-design-exploration.md` |
