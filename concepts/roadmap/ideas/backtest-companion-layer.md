---
tags: [roadmap, idea, neurospect, backtesting, integration, tradezella, learning-science, product-market-fit, neurospect-learn]
aliases: [Backtest Companion Layer, Tradezella Integration, Backtesting Discipline Layer, Companion Positioning]
sources: []
status: designing
created: 2026-08-10
updated: 2026-08-10
---

# Backtest Companion Layer — Neurospect around the tool, not instead of it

**The shift, in Paul's framing (2026-08-10):** *"I will be using Tradezella for backtesting, but I am
wondering how I can use the neurospect-learn platform to improve my backtesting sessions, increasing
consistency and discipline and gathering, storing and gaining insights from my backtests… I am trying to see
how I can increase the product market fit of this platform so it can integrate in innovative ways with
existing trading apps or platforms for different purposes."*

## Why this is a positioning change, not a feature

[[concepts/roadmap/README]]'s Strategic horizon holds [[concepts/roadmap/ideas/platform-consolidation]] and
[[concepts/roadmap/ideas/vertical-ai-platform]] — both premised on Neurospect **absorbing** the work spread
across other tools ("the trader does not switch tabs"). This idea points the other way: the backtesting tool
is **chosen and kept**, and Neurospect becomes the layer that makes sessions in it produce *learning* rather
than just records.

That is a different bet with a different risk profile. Absorption competes with incumbents on feature
surface; companionship competes on a capability incumbents structurally lack — and the whole
E1–E6 [[concepts/architecture/learning-enforcement]] arc is exactly such a capability. A journal tool records
what you did. This platform is the only thing in the stack that can say **whether the work was actually done**
(evidence-derived reps), **whether it met its own bar** (wiki-projected rubrics), and **whether the call
preceded the outcome** (the frozen pre-commitment ledger). None of those are things a backtesting tool wants
to build, because none of them make its own product look better.

## What is genuinely unknown, and must not be assumed

- **What can actually cross the boundary.** API? CSV export, and with which columns? ToS position on automated
  access? A partner/integration programme? The design is a different shape for each answer, and the answer is
  cheap to establish and expensive to guess.
- **Whether the incumbent already does this.** Tradezella ships journaling, analytics and a backtester; the
  useful question is not its feature list but its **seams** — what it deliberately does not do, and where its
  users say attention leaks.
- **Which learning-science claims survive contact with the literature.** "Neuroscience-backed" is where
  pop-science enters a product. See §The evidence bar below.
- **Whether there is demand beyond n=1.** Paul is the only user this platform has ever had. Every number in
  the E1–E6 arc came from fixtures.
- **Whether this makes deployment a prerequisite for the first time.** Design decision #4 (2026-07-28) held
  that hosting was not required *because every drill is desktop TradingView bar-replay and capture is
  paste-first*. An integration with a hosted third party may break that premise — which would be a genuine
  finding, not a detail.

## The evidence bar this idea is held to

Two precedents in this corpus, both of which changed a design rather than decorating one:

- **MeasureBench** (arXiv 2510.26865) demoted AI vision from arbiter to advisory second reader at E1, on
  measured benchmark numbers.
- **Deci, Koestner & Ryan (1999)**, 128 experiments, is why there is **no XP, no badges and no points** in this
  platform — tangible contingent rewards undermine intrinsic motivation (d ≈ −0.34) while informational
  feedback does not.

Anything proposed here inherits that bar: a design claim traces to a source, a vendor claim is never a design
premise, and unreplicated findings are labelled as such. Pop-neuroscience that must be refused by name:
learning styles, left/right-brain, "10,000 hours" as a law, and dopamine-loop hand-waving used to justify
streak mechanics — the last is directly contradicted by the finding already in this corpus.

## Related, and how

- [[concepts/roadmap/ideas/platform-consolidation]] · [[concepts/roadmap/ideas/vertical-ai-platform]] — the
  **opposite** bet (absorb vs. accompany). Not superseded; this idea should be weighed against them.
- [[concepts/roadmap/ideas/tradovate-integration]] — the only prior external-platform-integration idea, and the
  nearest precedent for the boundary questions above.
- [[concepts/roadmap/ideas/trading-improvement-engine]] · [[concepts/roadmap/ideas/mistake-driven-action-items]]
  — both turn journal data into improvement actions; overlapping intent, different data source.
- [[concepts/architecture/learning-enforcement]] — **the asset this bet is built on.** Complete E1–E6; its
  invariants are not reopened by this lane.
- [[concepts/architecture/learning-platform]] — the app's as-built surface.

## Status

`designing` — scoped as a workstream on 2026-08-10, ahead of the repo-integration lane the E6 retrospective
recommended. Tracker: [[processes/distributed-workflow/active/backtest-companion]].
