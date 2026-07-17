---
tags: [distributed-workflow, active, neurospect, aura, ingest, transcription]
aliases: [Aura Ingest Tracker, dOoMeR Ingest Tracker]
sources: []
created: 2026-07-16
updated: 2026-07-16
---

# Aura Playlist Ingest — Workstream Tracker

Transcribe and synthesize a second ICT/SMC mentor corpus (**Aura**, by [[entities/people/doomer]])
into this wiki, then reconcile it against the existing [[entities/people/mrwitness-axl]] notes to
improve their quality, detail, and accuracy. Source: YouTube playlist "Aura"
(`https://www.youtube.com/playlist?list=PLRg7PuEB1dWf0D_PSdY2jSMX7gFYv-GuN`), 30 available videos.

## Goal

1. **Raw sources** — 30 immutable transcripts in `sources/neurospect/aura/` (DONE, Phase 1).
2. **Standalone Aura KB** — `concepts/aura/` pages capturing the framework on its own terms,
   isolated from the existing ICT notes until reconciliation (Phase 2).
3. **Reconciliation** — existing `concepts/business-logic/ict-*` and entry-model pages enriched
   with *attributed* Aura content; agreements and contradictions flagged, never silently merged
   (Phase 3).
4. Updated `index.md` and `log.md`.

## Lane

Wiki: Neurospect (`C:\Users\PaulRussell\repos\neurospect-wiki\`)

Owned paths (write here):
- `sources/neurospect/aura/` (immutable transcripts)
- `concepts/aura/` (new standalone KB)
- `entities/people/doomer.md`
- Existing `concepts/business-logic/ict-*.md` + `concepts/entry-models/*` (Phase 3 only, additive/attributed)
- `index.md`, `log.md`

## Approach Decisions (approved 2026-07-16)

- **Transcription:** YouTube auto-captions + targeted Whisper fallback. Whisper is CPU-only on
  this machine (no CUDA) → full-playlist Whisper ≈ 12–18 hrs, so captions are the fast path.
  Result: all 30 captioned cleanly, **zero videos needed Whisper**.
- **Scope:** all 30 videos (curriculum + trade reviews).
- **Integration model:** standalone-first, then reconcile. Protects already-verified
  MrWitness-AXL notes from contamination before Aura is understood on its own terms.
- **Parallelism:** Phase 2 synthesis fans out to specialized subagents (per content block).
  Phase 1 was a single batch (network-bound; subagents add no value and risk YT throttling).

## Video Manifest

Section key: **P** = psychology, **T** = technical, **R** = trade/market review.

| # | Title | Dur | Video ID | Source file | Sec |
|---|---|---|---|---|---|
| 1 | The Foundation Is Broken | 24:27 | 2ZJiQUHl_Rw | aura-01-the-foundation-is-broken.md | P |
| 2 | How Your Mind Works Against You | 21:20 | qUwzgxFkV_Y | aura-02-how-your-mind-works-against-you.md | P |
| 3 | Emotional Control In Trading | 18:29 | cYZhahCBfLY | aura-03-emotional-control-in-trading.md | P |
| 4 | Building Systems That Force Discipline | 22:00 | KtIgmKjJB5I | aura-04-building-systems-that-force-discipline.md | P |
| 5 | The Journaling System | 16:55 | FixwlMsnakI | aura-05-the-journaling-system.md | P |
| 6 | Swing Points | 6:47 | ZbQ9qz4ftqc | aura-06-swing-points.md | T |
| 7 | Sequential SMT | 15:06 | pK5Pdud8kLA | aura-07-sequential-smt.md | T |
| 8 | Ranges | 29:36 | 5uhO1X6Erpc | aura-08-ranges.md | T |
| 9 | Gaps — What Lies Within | 23:03 | ZiVRYVunyvM | aura-09-gaps-what-lies-within.md | T |
| 10 | Why These Assets, Why These Triads | 17:45 | ICx_BLcFwN8 | aura-10-why-these-assets-why-these-triads.md | T |
| 11 | Ranges and Sequential SMT | 32:20 | IlN-xCnxiR0 | aura-11-ranges-and-sequential-smt.md | T |
| 12 | Confirming Sequential SMT and Framing Trades | 26:11 | UAkGEalDjiQ | aura-12-confirming-sequential-smt-and-framing-trades.md | T |
| 13 | Risk Management | 38:25 | BQMAuampgp0 | aura-13-risk-management.md | T |
| 14 | Sequential Skip | 12:53 | jA1Tc1xr_X8 | aura-14-sequential-skip.md | T |
| 15 | AURA ASSET | 12:00 | J9oXjAXEO7U | aura-15-aura-asset.md | T |
| 16 | Time Sum and Using The Aura Asset | 22:59 | MCkwfbKeXIo | aura-16-time-sum-and-using-the-aura-asset.md | T |
| 17 | Using the Aura Asset to Analyse HTF to LTF | 35:19 | VJoJiJP5UlA | aura-17-using-the-aura-asset-htf-to-ltf.md | T |
| 18 | Understanding The Weekly Range Through a Trade Review | 40:41 | OHZ1VoXuZeg | aura-18-understanding-the-weekly-range-trade-review.md | R |
| 19 | 043026 Trade Review | 21:18 | NYdDXvdDoTw | aura-19-043026-trade-review.md | R |
| 20 | 050126 Trade Review | 13:50 | EXe8mLy3NSM | aura-20-050126-trade-review.md | R |
| 21 | 112625 Trade Review | 14:36 | K8FlI8A0VLc | aura-21-112625-trade-review.md | R |
| 22 | Complete Market Overview | 28:52 | tN7RF81wOTg | aura-22-complete-market-overview.md | R |
| 23 | 121125 Trade Review | 23:29 | _ox9BC1dQ5Q | aura-23-121125-trade-review.md | R |
| 24 | 050726 Trade Review | 35:03 | dUKjlaKAMag | aura-24-050726-trade-review.md | R |
| 25 | Triad Synchronization Trade Review + Trading Expectations | 24:59 | 5UbTdh85fvg | aura-25-triad-synchronization-trade-review.md | R |
| 26 | 051226 Market Review | 14:45 | iA5hPUuKeKQ | aura-26-051226-market-review.md | R |
| 27 | 051326 Trade Review | 26:00 | S0yUP4XVW6I | aura-27-051326-trade-review.md | R |
| 28 | 051326 x 042625 Trade Review | 43:58 | l2pTi0Ko9E8 | aura-28-051326-x-042625-trade-review.md | R |
| 29 | Trade Review x Market Overview | 1:16:48 | MQt7lXNT8B0 | aura-29-trade-review-x-market-overview.md | R |
| 30 | 05212026 Trade Review | 18:50 | aq9F0HnjTgY | aura-30-05212026-trade-review.md | R |

One additional playlist video is hidden/unavailable (ID `tuG0aakI_LU`) — not transcribable.

## Plan

### Phase 0 — Setup ✅ (2026-07-16)
Create `sources/neurospect/aura/`, `concepts/aura/`, this tracker, and the `doomer.md` mentor
entity. Resolve mentor identity (dOoMeR, `@doomer312`).

### Phase 1 — Transcription ✅ (2026-07-16)
Fetch auto-captions for all 30 via `yt-dlp`, dedup the rollup artifact, write immutable source
files with frontmatter. Reusable script:
`…/scratchpad/aura_transcribe.py` (video list + `clean_vtt` dedup + `write_source`).
Result: 30/30 clean (~93k words total); proprietary jargon transcribed reliably; no Whisper needed.

### Phase 2 — Standalone Aura synthesis ✅ (2026-07-16)
Build `concepts/aura/` — Aura's framework on its own terms, **no edits to existing ict-\* pages**.
Fan out to specialized subagents per content block:
- **Psychology block (1–5):** foundations, emotional control, discipline systems, journaling system.
- **Technical block (6–17):** swing-points, sequential-smt, ranges, gaps, triads-asset-selection,
  risk-management, sequential-skip, aura-asset, time-sum, htf-ltf-application.
- **Reviews block (18–30):** one consolidated worked-examples page linking back to concepts.
Each page: cite source file(s), extract rules/definitions/examples, apply an ICT glossary to
correct any caption mis-hearings. Build `concepts/aura/README.md` framework overview.

### Phase 3 — Reconciliation ✅ (2026-07-16)
Enrich canonical pages with attributed Aura content (additive only; flag contradictions):
- `ict-smt` ← sequential-smt / sequential-skip / triads
- `ict-liquidity` ← ranges, gaps · `ict-market-structure` ← swing-points
- entry-models library ← aura-asset, time-sum, trade framing
- `journal-analytics` tracker + roadmap ideas ← journaling-system + psychology block
- `trade-schema.md` ← spec a new lightweight `missed_trades` table (decided — see the
  Phase 2 log's "next" block for the field list).
Deepen `entities/people/doomer.md`. Two-way cross-refs.

### Phase 4 — Close-out
Update `index.md` (Aura concept section + sources), append `log.md` per phase, lint pass
(orphans, cross-refs, isolation-rule check).

## Session Log

### 2026-07-16 — Phase 0 + Phase 1 (setup + transcription)

- did:
  - Confirmed tooling: `yt-dlp` installed, `ffmpeg` present, `whisper` present but **torch CPU-only**.
  - Enumerated playlist: 30 available videos (1 hidden). Resolved mentor = dOoMeR (`@doomer312`).
  - Verified auto-caption dedup approach on video 6 (last-line-of-cue rule collapses YT rollup).
  - Wrote `aura_transcribe.py`; transcribed all 30 → `sources/neurospect/aura/` (~93k words).
  - Spot-checked jargon: "aura asset", "sequential smt", etc. render correctly (195 hits).
  - Created `entities/people/doomer.md`, `concepts/aura/`, this tracker.
  - Updated `index.md` and `log.md`.
- decided:
  - No Whisper pass needed — captions clean across all 30.
  - Sources kept in a dedicated `aura/` subfolder (first non-flat source namespace) for provenance.
- next:
  - Phase 2: standalone synthesis into `concepts/aura/` via parallel subagents. Boot prompt below.

### 2026-07-16 — Phase 2 (standalone synthesis) + caption-accuracy verification

- did:
  - Fanned out 7 specialized Sonnet subagents in parallel (no write overlaps). Built 14 pages in
    `concepts/aura/`: psychology-foundations, mind-and-emotional-control, discipline-systems,
    journaling-system, swing-points, ranges, gaps, triads-asset-selection, sequential-smt,
    aura-asset, time-sum, htf-ltf-application, risk-management, trade-reviews. Upgraded README to a
    real framework overview. Verified lane-compliance via git (agents touched only assigned files).
  - Updated `index.md` (all 14 pages) and README at-a-glance table + learning path.
- key framework findings (decoded from corpus):
  - **Aura Asset = Swiss Franc futures (6S)** — a universal 4th triad leg / dollar-proxy tell.
    Chosen over DXY because DXY is not a synchronized futures contract. Origin story (Switzerland
    "neutrality"/elite thesis, Springmeier's *Bloodlines*) framed by dOoMeR as an unverified
    personal theory, explicitly separate from the quantitative correlation work.
  - **Sequential SMT** = SMT confirmed across ≥2 nested time cycles (probabilistic).
    **Sequential Skip** = fallback confirmation when the adjacent-cycle link is absent.
  - **Triad** = assets chosen by Pearson correlation on daily returns (2–3yr window); 5 triads
    (metals/indices/energy/forex/crypto) documented with coefficients.
  - **Time Sum** (digital-root "369") — dOoMeR *de-emphasizes it himself*; captured honestly.
  - Psychology/risk material is largely built on **Tom Dante** ("Blueprint for Trading Success"),
    Mark Douglas, *Atomic Habits*, Huberman. Resolves the "Tom" attribution flagged in aura-01.
- caption-accuracy verification (answers the "is the caption route accurate enough?" question):
  - A/B: re-transcribed video 6 (Swing Points) + video 15 (Aura Asset) with local Whisper `medium`
    (CPU) and diffed vs the caption transcripts. v6 = 91.2% word match; v15 = 95.1%.
  - Divergences are filler/formatting (numerals vs words) + a wash on jargon: Whisper won proper
    names (Springmeier, Bloodlines, "franc"), caption won "triad" (Whisper misheard as "tried").
    Neither engine uniformly better. **Content agreement ~99%.**
  - The synthesis layer already recovered every jargon slip from context (identified Swiss Franc
    despite caption mangling "franc"; corrected Springmeier/Bloodlines). **Captions validated;
    no re-transcription warranted.** Whisper A/B artifacts in `…/scratchpad/whisper/`.
- decided:
  - Kept Aura fully isolated in `concepts/aura/` — zero edits to `ict-*` pages (that is Phase 3).
  - Ran subagents on Sonnet (synthesis/ingest work) per model-selection strategy; Opus main session
    did review + README + close-out.
- next (Phase 3 reconciliation — cross-agent targets surfaced this session):
  - `ict-smt.md` ← Sequential SMT (cycle-nesting layer) + math-first Triad selection + Aura Asset
    (no DXY/dollar-index concept exists in `ict-*` yet — wholly new material).
  - `ict-liquidity.md` / `ict-market-structure.md` / `ict-order-flow.md` ← ranges (note: Aura uses
    discount/EQ/premium, **no quadrants**), gaps, swing points, HTF→LTF cascade.
  - `trade-schema.md` **gap**: missed/canceled trades are not modeled — Aura's strongest journaling
    anecdote (Dante tracking canceled orders). **DECIDED 2026-07-16 (Paul): new lightweight
    `missed_trades` table** (separate from `trades`, so executed-trade analytics aren't diluted).
    Phase 3 should spec this table (fields: date/session, setup, why-missed/canceled, the
    hesitation reason, screenshot, and the price outcome vs. the plan) and note it in
    `trade-schema.md` + the `journal-analytics` tracker.
  - roadmap ideas ← journaling-system (reduce-journaling-friction), psychology "four killers"
    (trader-psychology-profiler), risk rules (overtrading-risk-limits), never-miss-twice
    (mistake-driven-action-items).
  - Patch: `ranges.md`/`gaps.md` cross-ref "cracking correlation" (documented in sequential-smt.md;
    `structure` agent dropped it as garbled — it is a real term).
  - Deepen `entities/people/doomer.md` from the now-synthesized pages.

### 2026-07-16 — Phase 3 (reconciliation)

- did:
  - Reviewed the 4 canonical `ict-*` targets + all 14 `concepts/aura/` sources; wrote precise per-target
    subagent lanes. Fanned out **4 parallel Sonnet subagents** on non-overlapping write lanes; Opus main
    session wrote the decided-spec pieces and **reviewed every merge via git diff** before finalizing.
  - **`ict-smt.md`** ← Sequential SMT (time-cycle nesting), Sequential Skip, math-first Pearson triad
    selection (5 triads), Aura Asset (6S, flagged wholly-new dollar-proxy material). Convergence callout
    (YM's diverging role, independently derived) + primary-vs-confluence divergence callout.
  - **`ict-liquidity` / `ict-market-structure` / `ict-order-flow`** ← Aura ranges (discount/EQ/premium),
    gaps + "what lies within", 3-candle swing pivot w/ SMT-qualification, HTF→LTF if-then cascade. Two
    required divergence callouts flagged: quadrants (order-flow 0.25/0.75 vs Aura's 3-zone-only) and
    order-block vocabulary (Aura rejects the term).
  - **entry-models** `README` + `smt-confirmation-entry` ← Aura Sequential SMT entry model (iFVG-first in
    range discount, Sequential Skip fallback, cross-asset variant), minimal-PDA divergence callout.
  - **4 roadmap ideas** ← attributed Aura evidence (reduce-journaling-friction, trader-psychology-profiler,
    overtrading-risk-limits, mistake-driven-action-items).
  - **`trade-schema.md`** — specced the decided lightweight **`missed_trades`** table (separate from
    `trades`): fields per the Phase-2 "next" block (miss_type almost_took/hesitated/canceled, hesitation_tags,
    planned entry/stop/target, hypothetical_outcome + hypothetical_r, screenshot child table), full DDL
    (2 ENUMs, 2 tables, 4 indexes, trigger), REST API, 3 analytics endpoints (headline: opportunity cost —
    forgone R vs R-saved-by-canceling). Noted in `journal-analytics.md`. Fixed a pre-existing duplicate
    `sources:` frontmatter key. Status: **designed, not implemented** (no code written).
  - **`entities/people/doomer.md`** deepened from the 14 synthesized pages.
  - Patched `concepts/aura/ranges.md` + `gaps.md` with "cracking correlation" cross-refs (real term the
    Phase-2 structure agent dropped as garbled) and added reverse aura→ict links across 7 aura pages.
  - Updated `index.md`, `log.md`, this tracker.
- verified:
  - Additive-only confirmed via git: all 20 deletions across the 11 agent-edited files were frontmatter
    lines (`aliases:`/`updated:`/`sources:`) replaced by expanded versions — **zero body content removed**.
  - Every merged Aura claim attributed ("Aura (dOoMeR): …" + `aura-NN` cite); direct parallels use
    "MrWitness-AXL: X; Aura (dOoMeR): Y"; contradictions/divergences flagged in blockquote callouts.
  - Isolation rule held — no ALDC references introduced by any lane.
- decided:
  - Subagents produced the merges but **edited verified notes directly**; Opus reviewed all diffs before
    sign-off (per the boot prompt's "review each merge" instruction) rather than a proposal-then-apply loop.
  - Aura-page patches (cracking-correlation + reverse links) done by the main session *after* subagents
    finished, to avoid a read/write race on those files.
- next: Phase 4 close-out is effectively folded into this session (index/log/tracker updated, lint run).
  Ask Paul before committing. The `missed_trades` table awaits a future backend build cycle.

## Next Session Boot Prompt (Phase 3 — reconciliation)

Paste this into a fresh/cleared session pointed at `C:\Users\PaulRussell\repos\neurospect-wiki`:

```
We are doing PHASE 3 of the Aura ingest workstream. Boot up:
1. Read CLAUDE.md (esp. the Isolation Rule + Architecture Doc Integrity + Rules #6 "flag
   contradictions, never silently overwrite").
2. Read processes/distributed-workflow/active/aura-ingest.md IN FULL — especially the
   2026-07-16 Phase 2 session log and its "next (Phase 3)" target list, which IS the work plan.
3. Read index.md for the catalog.

Context: Phases 0–2 are complete and committed (commit a4701a2). 30 immutable transcripts live
in sources/neurospect/aura/; 14 standalone Aura concept pages live in concepts/aura/ (fully
isolated from the existing notes so far).

Task — Phase 3 reconciliation: enrich the canonical concepts/business-logic/ict-* pages (plus the
entry-models library, the journal-analytics tracker, roadmap ideas, and trade-schema.md) with
ATTRIBUTED Aura content, using the per-target list in the Phase 2 log.

Hard rules:
- Additive only. Attribute every merged claim, e.g. "MrWitness-AXL: X; Aura (dOoMeR): Y".
- Flag contradictions explicitly (CLAUDE #6) — never silently overwrite verified notes.
- Add two-way cross-refs between the ict-* pages and the concepts/aura/ pages.
- Respect the Isolation Rule (no ALDC references).

Decided inputs (do NOT re-litigate):
- trade-schema.md: add a NEW lightweight `missed_trades` table (separate from `trades`). Spec
  fields per the Phase 2 log's "next" block; note it in trade-schema.md + journal-analytics.
- Patch concepts/aura/ranges.md + gaps.md to cross-ref "cracking correlation" (it is a real term,
  documented in concepts/aura/sequential-smt.md; the structure agent dropped it as garbled).

Approach: consider fanning out per-target subagents on Sonnet (as Phase 2 did), but since this
edits VERIFIED notes, review each merge before finalizing. Then deepen entities/people/doomer.md
from the synthesized pages, run a lint pass (orphans, cross-refs, isolation-rule check), and
update index.md + log.md. Ask Paul before committing.
```

## See Also

- [[entities/people/doomer]] — the Aura mentor entity
- [[entities/people/mrwitness-axl]] — first mentor corpus; Phase 3 reconciliation target
- [[concepts/architecture/transcript-pipeline]] — pipeline decision doc (captions = Option C)
- [[processes/distributed-workflow/active/course-and-kb]] — the analogous MrWitness-AXL synthesis
- [[concepts/roadmap/README]] — psychology/journaling content feeds journal + coach roadmap
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`
