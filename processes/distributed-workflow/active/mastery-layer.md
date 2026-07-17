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
4. **Unified model** — merge both into one playbook. ⛔ Deferred to a dedicated deep-research session
   *after* both tracks exist and have been backtested (Phase 3).

## Lane

Wiki: Neurospect (`C:\Users\PaulRussell\repos\neurospect-wiki\`). Owned paths (write here):
- `concepts/mastery/` (the new namespace)
- Additive cross-links only into `concepts/aura/README.md`, `concepts/course/README.md`,
  `concepts/entry-models/README.md`, `index.md`, `log.md`

Read-as-source, never modify: `concepts/aura/*`, `concepts/course/*`, `concepts/entry-models/*`,
`concepts/business-logic/ict-*`, `concepts/architecture/trade-schema.md`, `sources/neurospect/*`.

## Decisions (approved 2026-07-17, do not re-litigate)

- **Two parallel tracks**, then a **later** unified-model deep-research session. Do NOT merge the two
  models until both tracks are complete and backtested.
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

### Phase 3 — Unified-model deep-research ⛔ (deferred)
Reconcile Aura + ICT-course into one playbook; fills the reserved slot in `concepts/mastery/README.md`.

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
