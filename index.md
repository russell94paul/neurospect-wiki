---
tags: [index, navigation]
created: 2026-04-18
updated: 2026-07-17
last_fork: 2026-04-26-broker-integration-forked-from-journaling-ux
last_build: 2026-04-26-phase4-deployment-complete
last_design: 2026-04-24-phase4-coach-frontend-design
last_ingest: 2026-07-16-aura-phase3-reconciliation
last_research: 2026-07-17-mastery-phase3-unified-model-and-frontier-ict
---

# Neurospect Wiki Index

Master catalog of all Neurospect wiki pages.

> **Isolation Rule:** This wiki is fully decoupled from the ALDC work wiki. The only allowed cross-wiki reference is ALDC research → Neurospect, by absolute path, from trackers. See [[CLAUDE]] § *Isolation Rule*.

---

## Entities

### Projects

- [[entities/projects/neurospect]] — core project entity (ICT trading journal + AI coach)

### People

- [[entities/people/mrwitness-axl]] — MrWitness and Axel (AXL), the two instructors delivering the mentorship curriculum
- [[entities/people/doomer]] — dOoMeR, instructor of the second "Aura" mentorship corpus (ICT/SMC, psychology-first)

### Tools

_None yet._

---

## Roadmap

Forward-looking product roadmap (horizons: Now / Next / Later / Strategic / Research / Compliance-Sensitive). Supersedes the v1 phased plan in `entities/projects/neurospect.md` for forward decisions.

- [[concepts/roadmap/README]] — main roadmap with horizon assignments, prioritization rationale, lifecycle convention
- [[concepts/roadmap/ideas/README]] — idea-backlog index (15 stubs)

---

## Concepts

### Business Logic

- [[concepts/business-logic/ict-liquidity]] — BSL/SSL, swing highs/lows, DOL, FVG (BISI/SIBI), IOFED, BAG — the two forces that move price
- [[concepts/business-logic/ict-narratives]] — 4 stages of algorithmic price delivery (consolidation/expansion/retracement/reversal), Power of Three (AMD), session kill zones, opening prices, daily bias (Vol 1–2)
- [[concepts/business-logic/ict-entry-models]] — FVG, order blocks, rejection blocks, breaker blocks, BPR, OTE, Model 2022, CSD, three-step execution framework (Vol 1, 3)
- [[concepts/business-logic/ict-market-structure]] — MSS, BOS, STH/ITH/LTH, STL/ITL/LTL, market structure fractality, CSD, reversal types (Vol 3)
- [[concepts/business-logic/ict-smt]] — SMT divergence, The Triad (NQ/ES/YM), cracking correlation, Price SMT, PDR SMT (Vol 4 Class 2); trust-the-program framework
- [[concepts/business-logic/ict-deviations]] — Fibonacci deviation targeting for HOD/LOD, HPDL, two-set market structure deviations (Vol 2 Class 3, Vol 3 Class 4)
- [[concepts/business-logic/ict-order-flow]] — HTF/LTF order flow, closing basis, quadrant levels, LRLR/HRLR, order block respect/disrespect (Vol 4 Class 1)
- [[concepts/business-logic/ict-live-commentary]] — live pre-market framework, day-of-week protocol, HOD/LOD calling, weekly opening price, first presentation FVG, liquidity void, contract rollover (stream + YouTube ingest)

### Architecture

- [[concepts/architecture/tech-stack]] — canonical backend stack decision (FastAPI + SQLAlchemy async + Postgres on Render + Discord OAuth2 + TradingView webhooks + Cloudflare R2); shared by AI Coach and Journal modules
- [[concepts/architecture/trade-schema]] — ICT trade data model: field definitions, Postgres DDL, indexes, REST API surface (Phase 1 of Journal & Analytics)
- [[concepts/architecture/phase2-project-structure]] — APPROVED project layout for `neurospect-api`: directory structure, Poetry deps, auth flow, analytics SQL approach, file creation order (Phase 2)
- [[concepts/architecture/tradingview-connector]] — AI Coach Phase 3 end-to-end design: Pine Script indicator, `/webhooks/tradingview/{user_token}` validation stack, `coaching_events` table, Claude prompt-cached call, polling endpoint
- [[concepts/architecture/transcript-pipeline]] — transcript ingestion decision doc (manual + Whisper)
- [[concepts/architecture/phase3-frontend-structure]] — **canonical frontend doc**: React 19 + TS + Vite project layout, route map, key patterns (auth, trade form, screenshot upload, analytics hooks), env vars
- [[concepts/architecture/phase4-coach-frontend]] — AI Coach frontend: routes, hooks, component tree, polling strategy, TV token UX, Pine asset sync

### AI Coach

- [[concepts/ai-coach/strategies.json]] — machine-readable strategy library (generated from entry-models YAML blocks; loaded into Claude system prompt)
- [[concepts/ai-coach/system-prompt-template.md]] — full Claude system prompt template (ICT rules + strategy library + JSON output schema); v1.0
- [[concepts/ai-coach/chart-analysis-boot-prompt]] — standalone boot prompt for manual chart analysis sessions (copy-paste into any Claude session with vision)

### Course (Module 1 — Foundations)

- [[concepts/course/README]] — course overview and learning path (5 modules, prerequisite order)
- [[concepts/course/module-1-foundations/01-what-moves-the-market]] — Liquidity (BSL/SSL/DOL), Inefficiency (FVG), the daily price cycle (Vol 1 Cls 1)
- [[concepts/course/module-1-foundations/02-fair-value-gaps]] — FVG precision, BISI/SIBI, IOFED, BAG, inversion FVG, AXL sniper entries (Vol 1 Cls 1–2)
- [[concepts/course/module-1-foundations/03-homework-and-practice]] — Class 1 and Class 2 homework assignments + readiness checklist

### Course (Module 2 — Price Delivery)

- [[concepts/course/module-2-price-delivery/01-four-stages-apd]] — Consolidation/Expansion/Retracement/Reversal overview; real vs. fake retracement; BPR skipping (Vol 1 Cls 2–4)
- [[concepts/course/module-2-price-delivery/02-consolidation-model]] — Stage 1 in depth: range definition, EQ, two delivery paths, SMT at sweep, live NQ example (Vol 1 Cls 2)
- [[concepts/course/module-2-price-delivery/03-expansion-retracement]] — Stages 2 & 3: measuring expansion, real/fake retracement, healthy/choppy, algorithmic body signature, worked examples (Vol 1 Cls 3)
- [[concepts/course/module-2-price-delivery/04-reversals]] — Stage 4: three reversal types (failure swing ~10%, raid on stops ~80%, accumulation ~10%), layered liquidity rule (Vol 1 Cls 4)

### Course (Module 3 — Session Context & Bias)

- [[concepts/course/module-3-session-and-bias/01-power-of-three]] — AMD framework; four opening prices; daily candle anatomy; worked Asia trade example (Vol 2 Cls 1)
- [[concepts/course/module-3-session-and-bias/02-session-kill-zones]] — five KZ windows; opening price anchors; NY AM two-part structure; ORG size; highest-probability stack (Vol 2 Cls 2)
- [[concepts/course/module-3-session-and-bias/03-deviations]] — Fibonacci deviation targeting; HOD/LOD anchoring; HPDL; two worked London examples (Vol 2 Cls 3)
- [[concepts/course/module-3-session-and-bias/04-daily-bias]] — HTF FVG cycle; opening price position; 80% bias framework; live 4H FVG walk-through (Vol 2 Cls 4)

### Course (Module 4 — Market Structure)

- [[concepts/course/module-4-market-structure/01-swing-classification]] — STH/ITH/LTH; gap-qualification rule; why STLs are suspect; MSS trigger; daily chart ITL example (Vol 3 Cls 2)
- [[concepts/course/module-4-market-structure/02-fractality]] — FVG liquidity engineering; engineered swing inside a FVG; turtle soup pattern; multi-TF nesting; daily fractal walk-through (Vol 3 Cls 2)
- [[concepts/course/module-4-market-structure/03-structure-deviations]] — two-set deviation anchoring (ITL price leg + STL measuring swing); convergence zone = HOD/LOD; London and holiday worked examples (Vol 3 Cls 4)
- [[concepts/course/module-4-market-structure/04-model-2022-ote-csd]] — 62–79% OTE zone; OTE block selection (highest open, propulsion block, 0.705 concert); CSD pre-MSS signal; full entry sequence (Vol 3 Cls 5)

### Course (Module 5 — Order Flow & SMT)

- [[concepts/course/module-5-order-flow-and-smt/01-htf-ltf-order-flow]] — bodies vs. wicks; closing basis; quadrant levels (0/0.25/0.5/0.75/1.0); LRLR vs. HRLR; BPR behavior; 5M bearish ES session walk-through (Vol 4 Cls 1)
- [[concepts/course/module-5-order-flow-and-smt/02-smt-divergence]] — triad (NQ/ES/YM); cracking correlation; Price SMT vs. PDR SMT; chart setup (3 methods); distribution and accumulation examples; trust-the-program; Six Sisters distinction (Vol 4 Cls 2)

### Entry Models Library

- [[concepts/entry-models/README]] — library overview, universal minimum confluence, stop/target conventions
- [[concepts/entry-models/consolidation-model]] — consolidation range + EQ + PDA entry; YAML machine-readable strategy block (Vol 1 Cls 2)
- [[concepts/entry-models/expansion-retracement-model]] — FVG/OB in discount after expansion; real retracement checklist; YAML block (Vol 1 Cls 3)
- [[concepts/entry-models/reversal-raid-on-stops]] — liquidity sweep + immediate rejection; layered liquidity rule; YAML block (Vol 1 Cls 4)
- [[concepts/entry-models/london-model]] — London takes Asia side, delivers to other; SMT at sweep; 1–3x/week; YAML block (Vol 1 Cls 2, Vol 2 Cls 2)
- [[concepts/entry-models/model-2022-ote]] — MSS + deep OTE retracement (62–79%); CSD pre-MSS signal; propulsion block selection; YAML block (Vol 3 Cls 5)
- [[concepts/entry-models/daily-bias-model]] — HTF FVG + opening price prerequisite filter; integrates with all other models; YAML block (Vol 2 Cls 4)
- [[concepts/entry-models/smt-confirmation-entry]] — NQ/ES/YM divergence at manipulation leg; Price SMT + PDR SMT; trust-the-program; YAML block (Vol 4 Cls 2)

### Aura Framework (second mentor corpus)

Independent ICT/SMC corpus by [[entities/people/doomer]], captured on its own terms in `concepts/aura/`.
**Phase 3 reconciliation complete (2026-07-16):** attributed Aura content has been merged into the
canonical `ict-*` pages (SMT, liquidity, market-structure, order-flow), the entry-models library,
`trade-schema.md` (new `missed_trades` table), and the roadmap ideas — agreements and divergences
flagged, never silently merged, with two-way cross-refs. See [[processes/distributed-workflow/active/aura-ingest]].

- [[concepts/aura/README]] — Aura framework overview, at-a-glance table, learning path
- [[concepts/aura/psychology-foundations]] — why traders fail; systems > goals; 142-student survey (aura-01)
- [[concepts/aura/mind-and-emotional-control]] — self-image theory; the "four killers"; circuit-breaker rules (aura-02, 03)
- [[concepts/aura/discipline-systems]] — pre/post-market routines + environment design that force discipline (aura-04)
- [[concepts/aura/journaling-system]] — Aura journaling method; essentials + psychological fields; missed-trade tracking (aura-05)
- [[concepts/aura/swing-points]] — 3-candle pivot; SMT-qualification rule (aura-06)
- [[concepts/aura/ranges]] — expansive-move ranges; discount/EQ/premium; close-not-wick validity (aura-08, 11)
- [[concepts/aura/gaps]] — FVG/iFVG/NWOG/NDOG; liquidity within the gap (aura-09)
- [[concepts/aura/triads-asset-selection]] — Pearson-correlation triad selection; the 5 triads (aura-10)
- [[concepts/aura/sequential-smt]] — Sequential SMT (time-cycle nesting) + Sequential Skip (aura-07, 11, 12, 14)
- [[concepts/aura/aura-asset]] — the signature concept: Swiss Franc futures (6S) as universal 4th triad leg (aura-15)
- [[concepts/aura/time-sum]] — digital-root "369" check (dOoMeR de-emphasizes it); Aura Asset usage (aura-16)
- [[concepts/aura/htf-ltf-application]] — cascading HTF→LTF if-then workflow to a 5m trigger (aura-17)
- [[concepts/aura/risk-management]] — Dante "Blueprint": sizing, daily stop, 10R circuit-breaker, expectancy (aura-13)
- [[concepts/aura/trade-reviews]] — 13 consolidated worked examples (aura-18…30)

### Mastery (Learn-to-Execute)

The learn-to-execute layer: turning the models into live-trading skill, with drills and evidence-based
readiness tracking. Two parallel tracks (Aura + ICT-course, both built); a unified model is deferred.

- [[concepts/mastery/README]] — mastery hub: the 4-stage ladder, confidence scale, and Readiness-to-Live Gate
- **Aura (dOoMeR) track:**
  - [[concepts/mastery/aura/rules]] — the Aura model as an executable rulebook (54 rules, cited to aura-NN)
  - [[concepts/mastery/aura/checklist]] — pre-market → framing → entry → management → exit → review sheet
  - [[concepts/mastery/aura/learning-path]] — sequenced curriculum (Stage 0 psychology → Stage 6 live)
  - [[concepts/mastery/aura/exercises]] — drill library (hand-mark + tool-assisted + replay + tape + study-replicate)
  - [[concepts/mastery/aura/tracker]] — living per-concept mastery + backtest-expectancy + readiness tracker
- **ICT-course (MrWitness-AXL) track:**
  - [[concepts/mastery/ict-course/rules]] — the 16 lessons' scattered rules normalized into one cited rulebook (41 rules), reconciling the two extra checklist/routine loci
  - [[concepts/mastery/ict-course/exercises]] — drills index + gap-fill (Module 2 + M4.3-4.4) + tape-reading drills from the 11 stream + 2 YouTube transcripts
  - [[concepts/mastery/ict-course/tracker]] — per-lesson + per-entry-model ladder/confidence/reps + backtest-expectancy + AXL readiness gate
  - *(no separate learning-path/checklist — reuses [[concepts/course/README]] and the entry-model YAML)*
- **Unified track (Phase 3 — reconciles both):**
  - [[concepts/mastery/unified/README]] — the Unified Playbook: one 5-layer sequence (psychology → structural primitives → nested-SMT confirmation → execution → risk) + one-glance decision flow
  - [[concepts/mastery/unified/divergence-rulings]] — 8 cited rulings (R1–R8) reconciling every flagged AXL↔Aura divergence; two new EMERGING confluences (nested SMT stack; double-qualified swing)

### Advanced / Frontier (Phase 3 deep research)

Deep, less-common ICT concepts researched from the wider body of knowledge to extend the unified playbook — every page source-tiered and labelled ESTABLISHED / EMERGING / SPECULATIVE-or-FRINGE.

- [[concepts/advanced/README]] — frontier hub: source-quality rubric + the cross-cutting WHERE/WHEN/DIRECTION/CONFIRM confluence stack + the unfalsifiability critique
- [[concepts/advanced/ict-macros-and-silver-bullet]] — ICT Macros, killzone micro-structure / Judas swing, Silver Bullet (one model at three zoom levels)
- [[concepts/advanced/ipda-data-ranges]] — IPDA 20/40/60-day ranges + IRL/ERL; "liquidity matrix" debunked → PD Array Matrix
- [[concepts/advanced/quarterly-theory]] — Quarterly Theory / 90-min cycles / True-Day-Open disambiguation (community — Trader Daye, not ICT)
- [[concepts/advanced/cbdr-and-sd-projections]] — CBDR / Asian range / flout + standard-deviation projections (SD ≠ Fibonacci disambiguation)

### Patterns

_None yet._

---

## Processes

### Distributed Workflow

- [[processes/distributed-workflow/active/kickoff]] — kickoff workstream tracker (complete — wiki bootstrapped, transcripts ingested, KB populated).
- [[processes/distributed-workflow/active/course-and-kb]] — ICT course construction + entry models library with machine-readable YAML strategy blocks (do first).
- [[processes/distributed-workflow/active/ai-coach]] — AI trading coach module: Claude + TradingView integration, live strategy evaluation (depends on course-and-kb).
- [[processes/distributed-workflow/active/journal-analytics]] — trade journal + analytics module: ICT-specific trade schema, dashboard (parallel to ai-coach).
- [[processes/distributed-workflow/active/deployment]] — Render (backend) + Cloudflare Pages (frontend) + Discord OAuth + TradingView webhook deployment. Phase 4 complete 2026-04-26. R2 screenshots remaining.
- [[processes/distributed-workflow/active/journaling-ux]] — Trade form tab redesign + field reduction + R2 wiring. Phases 1 & 2 complete.
- [[processes/distributed-workflow/active/broker-integration]] — Tradovate REST integration, broker credentials, active-trade soft singleton, `/settings/broker`. Phase 1 spec approved 2026-04-26.
- [[processes/distributed-workflow/active/monorepo-migration]] — consolidate `neurospect-wiki` + `neurospect-api` + `neurospect-app` into one `neurospect` monorepo. Phase 0 (scoping).

- [[processes/distributed-workflow/active/aura-ingest]] — transcribe + synthesize the second mentor corpus (Aura / dOoMeR); reconcile into existing notes. **Complete** — all phases done (30 transcripts, 14 concept pages, reconciled into ict-*/entry-models/schema/roadmap).
- [[processes/distributed-workflow/active/mastery-layer]] — learn-to-execute layer (rules/checklist/learning-path/exercises/tracker per model). **Phases 1–2 done** (mastery system + Aura track + ICT-course track); Phase 3 (unified model) deferred.

#### Zeus OS (Product Suite)

- [[processes/distributed-workflow/active/zeus-memory]] — Zeus-Memory hybrid architecture research + implementation. Phase 1 design complete, implementation kickoff pending.

Pattern docs are in the ALDC wiki and consumed by absolute path:

- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\README.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\session-lifecycle.md`
- `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\tracker-template.md`

### Operations

_None yet._

---

## Tickets

_None yet._

---

## Sources

### Transcripts (Vol 1)
- `sources/neurospect/2026-04-18-vol1-class1-pt1-liquidity-and-inefficiency.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class1-pt2-liquidity-and-inefficiency.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class1-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class2-consolidation-model.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class2-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class3-expansion-and-retracement-model.md` — video transcript
- `sources/neurospect/2026-04-18-vol1-class3-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol1-class4-notes.md` — PDF notes (no video)

### Transcripts (Vol 2)
- `sources/neurospect/2026-04-18-vol2-class1-power-of-three.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class1-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol2-class2-notes.md` — PDF notes (no video)
- `sources/neurospect/2026-04-18-vol2-class3-measuring-manipulation-deviations.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class3-notes.md` — PDF notes
- `sources/neurospect/2026-04-18-vol2-class4-daily-bias-practice.md` — video transcript
- `sources/neurospect/2026-04-18-vol2-class4-notes.md` — PDF notes

### Transcripts (Vol 3)
- `sources/neurospect/2026-04-18-vol3-class2-market-structure-fractality.md` — video transcript
- `sources/neurospect/2026-04-18-vol3-class4-market-structure-deviations.md` — video transcript
- `sources/neurospect/2026-04-18-vol3-class5-model-2022-ote-csd.md` — video transcript

### Transcripts (Vol 4)
- `sources/neurospect/2026-04-18-vol4-class1-htf-ltf-orderflow.md` — video transcript
- `sources/neurospect/2026-04-18-vol4-class2-smt-divergence.md` — video transcript

### Stream Transcripts (2026-04-20)
- `sources/neurospect/2026-04-20-stream-0830-mid-mon-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-nfp-fri-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-uc-fomc-wed-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-0830-uc-thu-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-1000-ism-pmi-1300-fed-speaks.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-1000-jolts-tue-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-fri-10-mid-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-no-news-mon-tape-reading.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-tapx-tape-reading-live-nq.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-thu-tape-reading-live-nq.md` — stream transcript
- `sources/neurospect/2026-04-20-stream-tue-10-fed-chair-testifies.md` — stream transcript

### YouTube Transcripts (2026-04-22)
- `sources/neurospect/2026-04-22-youtube-1000-points-nq-2026-03-04.md` — YouTube weekly review (+1000 pts NQ, March 4 2026)
- `sources/neurospect/2026-04-22-youtube-first-week-march-2026-03-07.md` — YouTube weekly review (first week of March, March 7 2026)

### Aura Playlist — dOoMeR (2026-07-16)
30 auto-caption transcripts in `sources/neurospect/aura/` (`aura-01`…`aura-30`). Second mentor
corpus. Manifest + per-video titles in [[processes/distributed-workflow/active/aura-ingest]].
Sections: psychology (1–5), technical framework (6–17), trade/market reviews (18–30).

---

## Vault

Credentials live in `vault/credentials.md` (gitignored — see `.gitignore:vault/`). Never commit values here in `index.md` or any other tracked file. See [[CLAUDE]] § *Rules* #2.

---

## Daily

Handwritten notes inbox. Copy `daily/_template.md` as `daily/YYYY-MM-DD.md`.

- [[daily/_template]] — note format reference.
- [[daily/2026-04-18]] — bootstrap day.
- [[daily/2026-04-20]] — transcript ingest session checkpoint.
- [[daily/2026-04-22]] — stream + YouTube ingest session checkpoint.
- [[daily/2026-04-24]] — Phase 4 (AI Coach frontend) implemented + verified. Deployment tracker created.
