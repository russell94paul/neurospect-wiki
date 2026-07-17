---
tags: [distributed-workflow, active, neurospect, mastery, learning]
aliases: [Mastery Layer Tracker, Learn-to-Execute Tracker]
sources: []
created: 2026-07-17
updated: 2026-07-17
---

# Mastery Layer — Workstream Tracker

Build the **learn-to-execute** layer on top of the synthesized trading KBs: turn each model into a
rulebook + execution checklist + sequenced learning path + drill library + evidence-based mastery
tracker, so Paul can go from "understands the concepts" to "cleared to live-trade" — the arc being
*learn → mark by hand → backtest in replay → read live tape → annotated-screenshot journal → prove
positive expectancy → go live.*

## Goal

1. **Mastery system** — a shared model (4-stage ladder, confidence scale, readiness-to-live gate). ✅
2. **Aura track** — rules / checklist / learning-path / exercises / tracker for the dOoMeR Sequential-SMT
   model. ✅ (Phase 1)
3. **ICT-course track** — the same for the MrWitness-AXL model, built as an *aggregator + gap-fill*
   (much already exists). ✅ (Phase 2, 2026-07-17)
4. **Unified model + frontier content** — synthesize both tracks into one playbook **and** research
   deep / unique / frontier ICT content that accelerates the path to mastery. A course-content
   deep-research session (Phase 3). Backtesting is **out of scope** (reframe 2026-07-17). ✅ (2026-07-17)
5. **Graded learning roadmap + progress tracker** — sequence the unified playbook + frontier content into
   one ordered path graded on the existing ladder/confidence/gate; plus a bounded Tier-1 upgrade pass on the
   frontier pages (Phase 4). Backtesting remains out of scope. ⏭ **NEXT.**

## Lane

Wiki: Neurospect (`C:\Users\PaulRussell\repos\neurospect-wiki\`). Owned paths (write here):
- `concepts/mastery/` (the new namespace)
- Additive cross-links only into `concepts/aura/README.md`, `concepts/course/README.md`,
  `concepts/entry-models/README.md`, `index.md`, `log.md`

Read-as-source, never modify: `concepts/aura/*`, `concepts/course/*`, `concepts/entry-models/*`,
`concepts/business-logic/ict-*`, `concepts/architecture/trade-schema.md`, `sources/neurospect/*`.

## Decisions (approved 2026-07-17, do not re-litigate)

- **Two parallel tracks**, then a **later** unified-model deep-research session. ~~Do NOT merge the two
  models until both tracks are complete and backtested.~~
- **[AMENDED 2026-07-17 PM — approved by Paul]** Reframe confirmed: this mastery layer is **course
  content**, not a personal live-trading / Neurospect-app deliverable. Consequences: (a) **backtesting is
  out of scope** for this workstream and the **"backtested-first" precondition on Phase 3 is dropped**;
  (b) Phase 3 proceeds **next** as a **course-content deep-research** session, **broadened** from a pure
  A+B merge to *"deep, rich, unique, frontier ICT content that accelerates the path to mastery"* — the
  unified playbook is its centrepiece, not its whole scope; (c) a **subsequent** session may then build a
  **graded learning roadmap + progress tracker** over the resulting content.
- **Full tooling available** (Sequential-SMT indicator, TradingView bar-replay, futures incl. 6S) →
  drills are tool-assisted **and** include hand-marking variants (eye-training / muscle memory).
- **No-drift rule:** mastery pages LINK to concept/entry-model pages as source-of-truth; never restate.
  The entry-model YAML `checklist:` blocks are canonical (AI-coach consumes them) — index them, don't fork.
- **No blocking data gaps.** No annotated chart images exist (all sources are transcripts) → mitigation is
  replay on the exact historical dates + the learner's own annotated journal.

## Plan

### Phase 1 — Mastery system + Aura track ✅ (2026-07-17)
`concepts/mastery/README.md` + `concepts/mastery/aura/{rules,checklist,learning-path,exercises,tracker}.md`.

### Phase 2 — ICT-course track ✅ (2026-07-17)
Aggregator + gap-fill (see boot prompt below). Delivered:
`concepts/mastery/ict-course/{rules,exercises,tracker}.md` (no new learning-path/checklist — reuse
existing). Additive cross-links from `course/README.md` + `entry-models/README.md`.

### Phase 3 — Course-content deep-research (unified model + frontier ICT) ✅ (2026-07-17)
Reframed 2026-07-17 (see Decisions amendment): backtest gate **dropped**. A deep-research session that
(a) reconciles Aura + ICT-course into **one unified playbook** (fills the reserved slot in
`concepts/mastery/README.md`), and (b) researches + synthesizes **deep / unique / frontier ICT content**
— cited, source-quality-vetted, pedagogically organized. A later session builds the graded learning
roadmap + tracker over the result. Boot prompt provided to Paul 2026-07-17 (see chat/handoff).

### Phase 4 — Graded learning roadmap + progress tracker (+ Tier-1 upgrade) ⏭ NEXT
Sequence the [[concepts/mastery/unified/README|Unified Playbook]] and `concepts/advanced/*` into ONE ordered
curriculum graded on the **existing** ladder/confidence/Readiness-to-Live Gate (reuse, don't reinvent):
`concepts/mastery/unified/learning-path.md` (the sequenced spine, folding in the two per-track paths by
reference) + `concepts/mastery/unified/tracker.md` (the living per-concept progress grid). Second thrust
(context permitting): a bounded **Tier-1 upgrade pass** on the frontier pages. Boot prompt below.

## Session Log

### 2026-07-17 — Phase 1 (mastery system + Aura track)
- did:
  - Scoped via 2 Explore agents (ICT-track inventory + exercise-source inventory) — findings baked into the
    Phase 2 boot prompt below so the next session needn't re-scout.
  - Created `concepts/mastery/` namespace. Wrote the hub (`README.md`: ladder Learned→Can-mark→Backtested→
    Live-ready, 1–5 confidence, rep counters, evidence-gated Readiness-to-Live Gate) + the 5-page Aura track.
  - `aura/rules.md` = 54-rule executable rulebook, every rule cited to `aura-NN`; divergences/soft-flags
    preserved. `aura/checklist.md` = 7-section execution sheet with `[R##]` refs + copyable Per-Trade Card
    (fields mirror `trade-schema.md`); fitness-checked vs aura-24. `aura/learning-path.md` = Stage 0→6.
    `aura/exercises.md` = drills D0-a…D6-c with ✋ hand-mark + 🛠 tool variants + 13 replay dates.
    `aura/tracker.md` = living per-concept + backtest-expectancy + gate.
  - Updated `index.md` (new Mastery section), appended `log.md`, added two-way links from `aura/README.md`.
- verified: isolation clean (no ALDC refs); 102/102 wikilinks resolve; no-drift honored (links, not restates).
- next: Phase 2 (ICT-course track) — boot prompt below.

### 2026-07-17 — Phase 2 (ICT-course / MrWitness-AXL track)
- did:
  - Scoped via 3 parallel Explore agents (Sonnet): (1) rules+homework inventory across the 16 lessons,
    (2) entry-model YAML extraction (7 models — `conditions:`/`checklist:`/stop/target), (3) the two
    business-logic checklist loci. Findings fed authoring directly; no re-scout needed.
  - Wrote `ict-course/rules.md` = 41-rule aggregator (A foundations · B price delivery · C session/bias ·
    D market structure · E order flow/SMT · F execution discipline), normalizing rules scattered under
    inconsistent lesson headings; every rule LINKS to its lesson + entry-model YAML (never forks the
    AI-coach `checklist:` arrays). Reconciled the two extra loci: `ict-entry-models`#Entry Checklist →
    subsumed by entry-models/README §Minimum Confluence; `ict-live-commentary` pre-market routine + AXL
    discipline → §F. Open flags preserved (rules-absent lessons; overlapping routines; `name:` vs
    `strategy_name:` YAML key).
  - Wrote `ict-course/exercises.md` = drills index + gap-fill, stages mapped 1:1 onto course Modules 1–5
    (not a new system), ✋ hand-mark + 🛠 tool variants. Indexed existing homework (incl. the reusable
    `## Readiness Check` checkbox primitive); gap-filled M2.1/2.3/2.4 + M4.3/4.4; added 13 tape-reading
    drills from the 11 stream + 2 YouTube transcripts, tagged by news context.
  - Wrote `ict-course/tracker.md` = per-lesson(16)+per-model(7) ladder/confidence/reps, module readiness
    gates, backtest-expectancy table, Readiness-to-Live Gate with AXL daily-loss-limit substituted.
  - Did NOT create learning-path.md/checklist.md (reuse course/README + entry-model YAML, per Decisions).
  - Cross-links: additive pointers up into mastery from course/README + entry-models/README; mastery/README
    ICT row = Built; index.md Mastery section expanded + tracker line (Phases 1–2 done); log.md appended.
- accuracy note: the 11 stream transcripts are `video_date: unknown` → drills are "study read → replay a
  *comparable* news-context session," not exact-date replay (only the 2 YouTube examples carry exact dates).
  This corrects the boot prompt's "these carry precise dates" claim for the streams.
- verified: isolation clean (no ALDC refs); no-drift honored (LINKED to — did not restate — entry-model
  YAML); all new intra-wiki wikilinks resolve to real pages.
- next: Phase 3 (unified-model deep-research) — deferred until both tracks are backtested.

### 2026-07-17 — Phase 3 (course-content deep research: unified model + frontier ICT)
- approach: Opus main session. Surveyed via 2 Explore agents (flagged AXL↔Aura divergences w/ file:line; frontier-topic
  coverage gaps). Presented plan; Paul approved via AskUserQuestion — **focused** web iteration (not an exhaustive
  Workflow), unified playbook → `concepts/mastery/unified/`. Thrust A written as direct synthesis; Thrust B via 3
  parallel Sonnet research agents (WebSearch/WebFetch → adversarial verify → tier+label).
- did (Thrust A — unified model, no web): `concepts/mastery/unified/README.md` (5-layer playbook: psychology →
  structural primitives → nested-SMT confirmation → execution → risk; one-glance decision flow) +
  `divergence-rulings.md` (R1–R8, each cited: SMT-role→COEXIST-LAYERED, swing-filter→COEXIST, quadrants→COEXIST,
  order-block→SUPERSET, **risk fixed-$ vs %/R→SUPERSEDE-%/R [previously-unflagged, surfaced per Rule #6]**,
  Time-Sum→DROP, 6S→ADOPT-additive, sequencing→psychology-first; + convergences). Two new **EMERGING** confluences:
  nested SMT stack (R1), double-qualified swing (R2).
- did (Thrust B — frontier, focused web): `concepts/advanced/` = README (Tier rubric + label key + WHERE/WHEN/
  DIRECTION/CONFIRM confluence stack + unfalsifiability critique) + 4 pages: ict-macros-and-silver-bullet (SB
  ESTABLISHED/Tier-1; macros community-reconstructed; killzone-boundary contradiction flagged), ipda-data-ranges
  (20/40/60 ESTABLISHED; "liquidity matrix"→SPECULATIVE, real term = PD Array Matrix; IRL/ERL; LRLR/HRLR), 
  quarterly-theory (EMERGING — Trader Daye, NOT ICT; True-Day-Open 3-referent disambiguation), cbdr-and-sd-projections
  (CBDR/flout ESTABLISHED; SD=arithmetic ≠ Fibonacci ≠ statistical-std-dev; index-futures pip→point gap). Every
  claim cited; contradictions surfaced; marketing win-rates rejected.
- honesty note: web pass captured almost **no Tier-1 verbatim** (YouTube transcripts + X threads un-fetchable,
  402/403) → most Thrust-B claims are corroborated-**Tier-2**. Upgrading key claims to Tier-1 (pull actual ICT
  video transcripts) is the highest-value follow-up. Whole frontier confluence stack is **EMERGING, unbacktested.**
- bookkeeping: `mastery/README.md` Unified row Deferred→Built (+ slot note, See Also); `index.md` (Unified track +
  Advanced/Frontier section, `last_research`); `log.md` appended; this tracker Phase 3 ✅.
- verified: isolation clean (no ALDC refs); no-drift honored (LINK, never restate canonical `ict-*`/`aura-*`/
  entry-model pages); new intra-wiki wikilinks target real pages.
- next: **graded learning roadmap + progress tracker** over the unified playbook + frontier pages (following
  session, per amendment). Optional: Tier-1 upgrade pass on the frontier pages; later, backtesting (separate workstream).

## Next Session Boot Prompt (Phase 4 — graded learning roadmap + Tier-1 upgrade) ⏭ ACTIVE

Recommended launch: **Sonnet** (aggregation/sequencing that mirrors the two existing tracks; escalate to
`opus` only if the cross-track sequencing gets genuinely hard). For the Tier-1 thrust the `/deep-research`
skill / direct WebSearch+WebFetch is the tool. Working dir: `C:\Users\PaulRussell\repos\neurospect-wiki`. Paste:

```
Neurospect wiki — Phase 4: GRADED LEARNING ROADMAP + progress tracker (over the unified model + frontier ICT).
Working dir: C:\Users\PaulRussell\repos\neurospect-wiki

BOOT / CONTEXT
1. Read CLAUDE.md IN FULL — obey: Isolation Rule (Neurospect lane only; NO ALDC content or refs),
   Architecture Doc Integrity (canonical-doc / no-drift: LINK to existing pages, never restate), Page Format,
   Rules #3 (update index.md), #4 (append log.md), #5 (prefer updating over creating), #6 (flag contradictions),
   #7 (cite every claim). Paul handles git commits — NEVER commit.
2. Read processes/distributed-workflow/active/mastery-layer.md IN FULL — the Decisions (note the 2026-07-17 PM
   amendment: backtesting is OUT OF SCOPE) and the Phase 3 session log. This is the work plan.
3. Survey what Phase 3 produced so you neither duplicate nor contradict it:
   - concepts/mastery/README.md — the SHARED grading model (4-stage ladder Learned→Can-mark→Backtested→
     Live-ready, 1–5 confidence, rep counters, the evidence-based Readiness-to-Live Gate). REUSE this; do not
     invent a new grading system.
   - concepts/mastery/unified/README.md — the 5-layer Unified Playbook + one-glance decision flow.
   - concepts/mastery/unified/divergence-rulings.md — the 8 AXL↔Aura rulings (R1–R8).
   - concepts/advanced/* — frontier hub + 4 pages (ict-macros-and-silver-bullet, ipda-data-ranges,
     quarterly-theory, cbdr-and-sd-projections); each carries a source TIER + an ESTABLISHED/EMERGING/
     SPECULATIVE label. Preserve those labels when the concept enters the roadmap.
   - The tracks you sequence OVER (fold in by reference, do NOT restate): concepts/mastery/aura/{learning-path,
     exercises,tracker}.md, concepts/mastery/ict-course/{exercises,tracker}.md, concepts/course/README.md.

OBJECTIVE (pre-answered; refine only if genuinely ambiguous)
Build the GRADED LEARNING ROADMAP + PROGRESS TRACKER that sequences the Unified Playbook and the frontier
content into ONE ordered path to mastery, graded on the EXISTING ladder/confidence/gate. This is the deferred
follow-on named in the tracker amendment. Two deliverables:

  A. concepts/mastery/unified/learning-path.md — ONE unified, sequenced curriculum. Order the 5 playbook
     layers (psychology → structural primitives → nested-SMT confirmation → execution → risk) into stages;
     each stage lists: the concepts to master (LINK to the unified README layer + canonical concept pages),
     the drills to run (LINK to aura/exercises + ict-course/exercises — never fork them), the ladder-stage
     exit bar, and where each frontier concept (concepts/advanced/*) slots in as a LATER, confluence-stacking
     stage (they depend on the primitives + SMT stack first). Fold aura/learning-path + course/README into this
     single spine by REFERENCE, not restatement.
  B. concepts/mastery/unified/tracker.md — the living per-concept progress grid, mirroring aura/tracker.md +
     ict-course/tracker.md: every unified-playbook concept + every frontier concept gets a ladder-stage /
     confidence(1–5) / rep-count row, grouped by learning-path stage, plus the Readiness-to-Live Gate (link it
     from mastery/README — keep the evidence gate). Tag EMERGING/SPECULATIVE frontier rows as study-and-watch,
     NOT trade-live-on.

  Grading model: REUSE mastery/README's ladder + 1–5 confidence + rep counters + Readiness-to-Live Gate by
  LINK. "Graded" = each concept carries its ladder stage + exit criteria + rep target, sequenced so earlier
  stages gate later ones. Do NOT duplicate the mastery-model text.

SECOND THRUST (only if context allows; otherwise leave for a follow-up and SAY SO in the session log):
  Tier-1 UPGRADE PASS on concepts/advanced/*. Phase 3 captured almost no Tier-1 verbatim (YouTube/X
  un-fetchable). Try to pull ACTUAL ICT primary sources to upgrade the highest-value corroborated-Tier-2
  claims — prioritise: IPDA 20/40/60 mechanics, CBDR window + body/wick measurement, Midnight-Open bias,
  Silver Bullet step-by-step (its video titles are already Tier-1; the mechanics are Tier-3). Update tier
  labels + citations ONLY where a genuine primary source is found. Do NOT downgrade the honesty caveats or
  inflate confidence. Bounded — no rabbit-holing.

QUALITY BAR
- No-drift: LINK to the mastery model, playbook, rulings, concept pages, entry-model YAML, and exercise
  libraries — never restate them. If the roadmap needs a concept the wiki lacks, flag it; do not invent.
- Keep EMERGING/SPECULATIVE labels attached when frontier concepts enter the roadmap — a learner must never be
  told to trade live on unbacktested confluence. The Readiness-to-Live Gate governs sim→live.
- Cite any new claim (Tier-1 pass). Surface contradictions; never smooth them.

WORKFLOW / OUTPUT
- FIRST present a short PLAN (plan mode) for approval before writing: the stage sequence, where each frontier
  concept slots in, and the tracker grid shape. Do not create pages until approved.
- THEN on approval: write learning-path.md + tracker.md; additive cross-links from unified/README + mastery/
  README (add the Unified track's learning-path/tracker to See Also); update index.md (extend the Unified
  track lines), append log.md, add a Phase 4 session-log entry to this tracker.
- OUT OF SCOPE (do NOT do): backtesting (separate workstream), Neurospect-app integration.
- Paul handles git commits — never commit. Respect the Isolation Rule throughout.
```

## Next Session Boot Prompt (Phase 3 — course-content deep research) — ✅ EXECUTED 2026-07-17

> **This phase is complete** (see the 2026-07-17 Phase 3 session log above). The prompt below is retained as
> a record of the plan. The next open work is a **graded learning roadmap + progress tracker** over the
> unified playbook + frontier pages (deliberately deferred to a following session, per the amendment).

Recommended launch: `claude --model opus[1m]`, then `/effort high`. The `/deep-research` skill is a
**tool, not a requirement** — used for Thrust B's web fan-out; Thrust A is direct synthesis. Paste:

```
Neurospect wiki — Phase 3: course-content DEEP RESEARCH (unified model + frontier ICT).
Working dir: C:\Users\PaulRussell\repos\neurospect-wiki

BOOT / CONTEXT
1. Read CLAUDE.md in full — obey: Isolation Rule (Neurospect lane only; NO ALDC content or refs),
   Architecture Doc Integrity (canonical-doc / no-drift: LINK to existing pages, never restate),
   Page Format, and Rules #3 (update index.md), #4 (append log.md), #5 (prefer updating over creating),
   #6 (flag contradictions, never silently overwrite), #7 (cite every factual claim).
2. Read processes/distributed-workflow/active/mastery-layer.md IN FULL — especially the Decisions
   (note the 2026-07-17 PM amendment: backtesting is OUT OF SCOPE; the backtested-first gate is DROPPED)
   and the Phase 3 description. This is the work plan.
3. Survey what already exists so you neither duplicate nor contradict it:
   - concepts/mastery/README.md + both built tracks (aura/*, ict-course/*) — the learn-to-execute layer.
   - concepts/business-logic/ict-*.md — the reference KB (liquidity, narratives, entry-models, smt,
     market-structure, order-flow, deviations, live-commentary).
   - concepts/course/* (16 learner lessons), concepts/entry-models/* (7 execution specs + AI-coach YAML),
     concepts/aura/* (the dOoMeR corpus).
   Produce a one-page "current coverage map" so the research targets GAPS and the FRONTIER, not restatement.

OBJECTIVE (pre-answered so you don't need to ask; refine only if genuinely ambiguous)
Audience: Paul — an intermediate→advancing ICT / Smart Money Concepts trader building a personal course /
knowledge base toward mastery. Markets: index futures (NQ/ES/YM) primary, plus the Aura triads
(metals, forex incl. 6S, energy, crypto). Timeframes: intraday 1m–4H with HTF context to weekly/quarterly.
Lineage: ICT (Michael J. Huddleston / Inner Circle Trader) + the two ingested mentors (MrWitness-AXL;
dOoMeR / "Aura"). Deliver TWO thrusts:

  THRUST A — UNIFIED MODEL (centrepiece). Reconcile the MrWitness-AXL (ICT-course) and dOoMeR (Aura)
  models into ONE coherent, principled playbook — not a mashup. The two use deliberately different
  vocabularies and the wiki already flags specific divergences (quadrants vs discount/EQ/premium;
  "order block" terminology; Time Sum/369; same-TF triad SMT vs cross-cycle Sequential SMT; DXY vs the
  6S Aura Asset). For each divergence, decide and justify: when to use which, or why one supersedes the
  other, or why both coexist. Output a single unified framework (structural primitives → confirmation →
  execution → risk → psychology) that a learner can actually follow. Fills the reserved "unified model"
  slot in concepts/mastery/README.md.

  THRUST B — DEEP / UNIQUE / FRONTIER CONTENT. Research the broader ICT body of knowledge and the best
  community refinements to surface high-impact concepts NOT yet covered in this wiki, that materially
  accelerate mastery. Candidate areas to investigate (guide, not limit — rank by impact, drop the weak):
  IPDA data ranges & the liquidity matrix; interbank price delivery algorithm logic; time-based models
  (ICT macros, time-of-day algorithmic behavior, killzone micro-structure); Quarterly Theory / 90-min
  cycles; PO3 & dealing-range mechanics at scale; seasonal tendencies & day-of-week edge; high- vs
  low-probability day classification; news-embargo / high-impact-event delivery behavior; institutional
  order-flow refinements; standard-deviation projection nuance; multi-timeframe liquidity runs.

QUALITY BAR (this is what makes it "best/most thorough" rather than a noise dump)
- Research method: use the /deep-research skill FOR THRUST B's web fan-out (fan-out searches → fetch
  PRIMARY sources → adversarially verify claims → cite). Do THRUST A as DIRECT SYNTHESIS of the existing
  corpus (reasoning, not web search). The skill is a tool, not a requirement — WebSearch/WebFetch directly
  is fine; what is mandatory is this quality bar. (Optional, for max thoroughness: drive Thrust B's
  fan-out with a Workflow. Opus, high effort.)
- Source hierarchy: ICT's OWN primary teachings first; the two ingested corpora second; reputable
  community work third; treat random YouTube/marketing as unverified until corroborated.
- Label every concept ESTABLISHED / EMERGING / SPECULATIVE-or-FRINGE. Flag unfalsifiable or
  marketing claims explicitly and do NOT present them as edge. Surface contradictions rather than
  smoothing them over.
- CITE every claim (source URL / video / the ingested transcript path). Where a wiki page is already
  canonical for a concept, LINK and extend it — do not restate (no-drift).
- Keep it pedagogical: for each frontier concept give what it is, why it matters to execution/edge,
  how it interacts with the unified model, and its common failure mode — organized so the NEXT session
  can sequence it into a learning roadmap.

WORKFLOW / OUTPUT
- FIRST present a PLAN (use plan mode) for approval before writing: the proposed page taxonomy (where the
  unified playbook lives — suggest concepts/mastery/unified/ — and where frontier pages live — propose
  concepts/advanced/ or extensions to concepts/business-logic/), the RANKED research agenda, and the
  source-quality rubric. Do not create pages until the plan is approved.
- THEN on approval: write the deep-research synthesis + the cited pages; update index.md, append log.md,
  and add a Phase 3 entry to the mastery-layer tracker session log.
- OUT OF SCOPE this session (do NOT do): backtesting, Neurospect-app integration, and the graded
  learning roadmap / progress tracker (that is the FOLLOWING session).
- Paul handles git commits — never commit. Respect the Isolation Rule throughout.
```

## Next Session Boot Prompt (Phase 2 — ICT-course track) — ✅ EXECUTED 2026-07-17

> **This phase is complete** (see the 2026-07-17 session log above). The prompt below is retained as a
> record of the Phase 2 plan. The next open work is **Phase 3 (unified-model deep-research)**, which is
> deliberately deferred until both tracks have been backtested — do not start it as a routine follow-on.

Recommended model: **Sonnet** (aggregation/authoring following an approved pattern; escalate only if a
merge decision gets hard). Working dir: `C:\Users\PaulRussell\repos\neurospect-wiki`.

```
We are doing PHASE 2 of the Mastery Layer workstream: the ICT-course (MrWitness-AXL) track. Boot up:
1. Read CLAUDE.md (Isolation Rule + Architecture Doc Integrity / canonical-doc / no-drift; Rules #3
   update index.md, #4 append log.md, #5 prefer updating over creating).
2. Read processes/distributed-workflow/active/mastery-layer.md IN FULL (this tracker) — the Decisions
   and this boot prompt are the work plan.
3. Read concepts/mastery/README.md (the shared mastery model) and the whole Aura track
   (concepts/mastery/aura/{rules,checklist,learning-path,exercises,tracker}.md) — MIRROR this structure
   and tone for the ICT track. Do NOT invent a different system.

Context — the ICT track is mostly AGGREGATION + GAP-FILL, not new authoring, because much already exists
(three-tier split, all deliberate — do not duplicate it):
  - Reference KB: concepts/business-logic/ict-*.md (dense, non-linear).
  - Learner-facing course: concepts/course/ (5 modules / 16 lessons; concept + worked example + homework).
    concepts/course/README.md ALREADY IS the learning path (path + prerequisite order + how-to-use).
  - Execution library: concepts/entry-models/ (7 strategies; each page ends with a
    `# --- MACHINE_READABLE_STRATEGY ---` YAML block containing a `checklist:` array — CONSUMED BY THE AI
    COACH, so index/link it, NEVER fork it). entry-models/README.md has a universal 5-point
    minimum-confluence checklist.

Deliverables (write only these + additive cross-links):
  A. concepts/mastery/ict-course/rules.md — a rules AGGREGATOR. The per-lesson "Rules" are scattered and
     inconsistently named (`## Rules` in M1.1/M1.2/M2.1/M3.1; renamed to "Key Rules"/"Closing Basis
     Rules"/"The Rule"/"Daily Checklist"/"Full Sequence" elsewhere; largely ABSENT in Module 4). Normalize
     them into one cited rulebook that LINKS to each lesson + to the entry-model `conditions:`/`checklist:`
     YAML — do not restate the YAML. RECONCILE the two extra checklist/routine loci rather than adding a
     competing copy: business-logic/ict-entry-models.md#Entry Checklist and
     business-logic/ict-live-commentary.md (pre-market routine + "Live Trading Discipline (AXL)").
  B. concepts/mastery/ict-course/exercises.md — a drills INDEX + gap-fill, mirroring aura/exercises.md
     (✋ hand-mark + 🛠 tool variants; drill→concept→ladder-stage map).
     - Index existing homework: the dedicated concepts/course/module-1-foundations/03-homework-and-practice.md
       (has a `## Readiness Check` checkbox primitive worth reusing) + inline `## Homework` in all of Module 3,
       Module 4 lessons 1-2, and both Module 5 lessons.
     - FILL THE GAPS (these lessons have NO real homework): all of Module 2 (four-stages / consolidation /
       expansion-retracement / reversals) and Module 4 lessons 3-4 (structure-deviations, model-2022-ote-csd).
     - Add TAPE-READING drills seeded from the 11 stream transcripts sources/neurospect/2026-04-20-stream-*.md
       (each is a real candle-by-candle NQ/ES/YM read; tag by news context: NFP-Fri, FOMC-Wed, no-news-Mon,
       all-time-highs, JOLTS-Tue, ISM/PMI+Powell, Fed-Chair-testifies, plus explicit "don't-trade" days) and
       the 2 YouTube weekly examples sources/neurospect/2026-04-22-youtube-*.md (2026-03-04 "+1000pts NQ";
       2026-03-07 "first week of March", weekly-opening-price rule). These carry precise dates → bar-replay
       study-then-replicate drills.
  C. concepts/mastery/ict-course/tracker.md — mirror aura/tracker.md: per-concept ladder/confidence/reps
     across the 16 lessons + 7 entry models, backtest-expectancy table, and the same Readiness-to-Live Gate.
  D. Do NOT create ict-course/learning-path.md or ict-course/checklist.md — course/README.md and the
     entry-model YAML already fill those roles. The mastery hub should LINK to them.

Then: additive cross-links from concepts/course/README.md and concepts/entry-models/README.md up into
concepts/mastery/README.md + the ict-course track (like the pointer already added to concepts/aura/README.md).
Update index.md (extend the Mastery section with the ict-course pages), append log.md, update this tracker's
session log. Run the lint (isolation-rule; all wikilinks resolve; confirm you LINKED to — did not restate —
the entry-model YAML). Vocabulary caution: the streams/youtube are ICT (MrWitness-AXL) vocabulary; keep them
out of the Aura track. Paul handles git commits — never commit.
```

## See Also

- [[concepts/mastery/README]] — the mastery model (ladder + readiness gate)
- [[concepts/mastery/aura/rules]] — the completed Aura track (the pattern to mirror)
- [[processes/distributed-workflow/active/aura-ingest]] — the ingest that produced the Aura KB
- [[processes/distributed-workflow/active/course-and-kb]] — the MrWitness-AXL course/entry-models build
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`
