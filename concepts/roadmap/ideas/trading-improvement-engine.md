---
tags: [roadmap-idea, neurospect, later, ai, analytics]
aliases: [Trading Improvement Engine, AI Improvement Proposals]
sources: [aldc-shipyard brainstorm 2026-05-26]
created: 2026-05-12
updated: 2026-05-12
horizon: later
status: backlog
---

# Trading Improvement Engine

Analyze journal entries, mistake patterns, P&L curves, and session behavior to proactively propose concrete trading plan adjustments — each with expected impact, risk assessment, and implementation steps. The trader reviews and approves proposals, which become action items tracked in the journal.

## Why it matters

Traders accumulate data in their journal but rarely synthesize it into actionable plan changes. This feature closes the loop: data → insight → proposal → approval → tracked adjustment. Moves Neurospect from "records what happened" to "tells you what to change."

Cross-pollinated from the ALDC Launchpad "Zeus Improvement Engine" concept — same closed-loop pattern (detect bottleneck → propose fix → approve → track), applied to trading instead of business operations. The ALDC version is first-of-its-kind in the B2B analytics space; applying it to trading would be equally novel.

## Dependencies

- [[concepts/roadmap/ideas/trader-psychology-profiler]] — needs trader profile to weight proposals (a revenge trader gets different proposals than a hesitation trader).
- [[concepts/roadmap/ideas/mistake-driven-action-items]] — action items infrastructure must exist for proposals to land.
- Sufficient journal corpus (~30+ trades minimum for meaningful pattern detection).

## Open questions

- Proposal frequency: weekly digest vs. real-time after each session?
- How to estimate "expected impact" without forward-looking data (backtesting against historical trades?).
- Should proposals include specific dollar amounts or stay percentage-based?
- Confidence scoring: how does the engine communicate uncertainty in its proposals?

## See Also

- [[concepts/roadmap/README]]
- [[concepts/roadmap/ideas/trader-psychology-profiler]]
- [[concepts/roadmap/ideas/mistake-driven-action-items]]
- [[concepts/roadmap/ideas/neurospect-voice]]
