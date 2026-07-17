---
tags: [roadmap-idea, neurospect, later, ux, ai]
aliases: [Strategy Adjustment Request, Plan Change Portal]
sources: [aldc-shipyard brainstorm 2026-05-26]
created: 2026-05-12
updated: 2026-05-12
horizon: later
status: backlog
---

# Strategy Adjustment Portal

A structured interface where traders propose changes to their trading plan with a rationale. The AI coach evaluates the request against the trader's historical performance, risk profile, and psychology profile — then presents ranked alternatives with pros/cons before the trader commits. Approved adjustments are logged and tracked for impact.

## Why it matters

Traders change their plans impulsively after bad sessions ("I'm switching to 15-min charts") or never change them despite evidence they should. This feature adds a friction layer that forces reflection: state the change, state why, and let the coach weigh in before committing. It creates an audit trail of plan evolution — invaluable for later review.

Cross-pollinated from the ALDC Launchpad "Client Change Request Portal" — same pattern (user requests change → AI analyzes against context → ranked options → approval → tracked), applied to trading plans instead of analytics products.

## Dependencies

- [[concepts/roadmap/ideas/trader-psychology-profiler]] — coach needs profile context to evaluate whether a change is data-driven or emotional.
- [[concepts/roadmap/ideas/neurospect-voice]] — voice interface for discussing proposed changes naturally.
- Stable trading plan schema (what fields define "the plan" that can be changed).

## Open questions

- What constitutes a "trading plan" in structured data (entry criteria, risk parameters, session rules, instrument list)?
- How to prevent the feature from feeling like a gate rather than a tool (opt-in vs. required)?
- Should the coach block obviously emotional changes ("you lost 3 trades and now want to switch timeframes") or just flag them?

## See Also

- [[concepts/roadmap/README]]
- [[concepts/roadmap/ideas/trader-psychology-profiler]]
- [[concepts/roadmap/ideas/neurospect-voice]]
- [[concepts/roadmap/ideas/overtrading-risk-limits]]
