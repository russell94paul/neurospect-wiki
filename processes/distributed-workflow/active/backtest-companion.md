---
tags: [distributed-workflow, active, neurospect, backtesting, integration, tradezella, learning-science, product-market-fit, research]
aliases: [Backtest Companion Tracker, Tradezella Lane, Companion Positioning Workstream]
sources: []
created: 2026-08-10
updated: 2026-08-10
---

# Backtest Companion — Workstream Tracker

Make `neurospect-learn` improve **backtesting sessions that happen in another tool**: consistency and
discipline while the session runs, capture and storage of what came out of it, and insight across sessions —
and use that as the wedge for a broader **companion** positioning, integrating with the trading apps a trader
has already chosen rather than replacing them.

> **STATUS (2026-08-10): SCOPED ONLY — no research done, no design decided, no code written.** This tracker
> exists so the first session starts from the real question rather than a blank page. Nothing in this document
> is a finding; everything in it is a question or a constraint.
>
> **Two sessions are queued, in this order.** The ⏭ ACTIVE prompt is the **skill authoring** session — it
> writes the divergent council skill that Phase B1 then uses (see §Recommended tooling for why none of the four
> installed council skills fits). **Phase B1** — the deep-research + design session — is written and QUEUED
> below; the skill session's last act is to move the ACTIVE marker onto it. B1 *can* be run without the skill,
> using its prompt alone; it will simply be more vulnerable to the three failures §Recommended tooling names.
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

## Lane

- **This wiki** produces the design artifacts: a canonical spec under `concepts/architecture/`, updates to
  [[concepts/roadmap/ideas/backtest-companion-layer]], and this tracker.
- **The app code** lands in `C:\Users\PaulRussell\repos\neurospect-learn`. Code is ground truth once written.
- Isolation Rule applies (Neurospect only; no ALDC content or references).
- Distributed-workflow pattern docs are referenced by absolute path, never wikilink:
  `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`,
  `…\session-lifecycle.md`, `…\tracker-template.md`.

## Plan

### Phase B1 — Deep research + design session ⏭ **ACTIVE** (boot prompt below)
Answer the 17 questions above from **external evidence**, decide the positioning, and produce ONE canonical
design doc plus a boot-promptable B2+ split. **Writes no app code.**

### Phase B2+ — TBD
Deliberately unwritten. E1's precedent: the phase split is B1's own output, and inventing it now would bake in
the assumption that the research is supposed to overturn.

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

## Recommended tooling for B1 (Paul asked; this is the recommendation, not a survey)

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

## Next Session Boot Prompt (Skill authoring — the divergent council) ⏭ ACTIVE

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

## Boot Prompt (Phase B1 — deep research + design) — QUEUED, activate after the skill session

Recommended launch: **Opus** (`claude --model opus[1m]`), then **`/effort xhigh`**, in **plan mode**. This is a
research and design session and its output is a document, not code. **Write no app code in this session** —
E1's precedent, and for the same reason: the design is the load-bearing artifact and building against an
unvalidated one is how the phase gets rewritten.

**If the council skill (§Recommended tooling) has been authored, invoke it.** If it has not, run this prompt
directly and consider authoring the skill first — but do not block on it.

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
