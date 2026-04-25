---
tags: [roadmap-idea, neurospect, next]
aliases: []
sources: []
created: 2026-04-25
updated: 2026-04-25
horizon: next
status: backlog
---

# Reduce Journaling Friction

Make journaling so cheap that it happens consistently: voice journaling, auto-populated trade data, templates and guided prompts that match the ICT trade lifecycle.

## Why it matters

Journal data is the substrate every later horizon depends on (profiler, edge detection, voice coach, action items). Inconsistent journaling = no data = nothing for AI to learn from. This is the highest-leverage friction reduction in the product.

## Sub-features

- **Voice journaling** — speech-to-text into pre/during/post-trade fields; reuses AI Coach pipeline.
- **Auto-populated trade data** — broker fills, instrument, session, kill zone, day-of-week prefilled (depends on [[concepts/roadmap/ideas/tradovate-integration]]).
- **Guided prompts / templates** — ICT-specific pre-trade narrative form templates (HTF bias, draw on liquidity, invalidation), post-trade review templates.

## Dependencies

- Tradovate integration for auto-fill (partial — voice + templates can ship without it).
- AI Coach pipeline for STT + structured extraction.

## Open questions

- STT cost at scale (Whisper local vs. API).
- Default templates per setup type (FVG entry vs. OTE vs. raid-on-stops) — derive from [[concepts/entry-models/README]]?
- Mobile capture path — is the Chrome extension enough, or do we need a thin mobile companion?

## See Also

- [[concepts/roadmap/README]]
- [[concepts/architecture/trade-schema]]
- [[concepts/architecture/tradingview-connector]]
- [[concepts/roadmap/ideas/tradovate-integration]]
- [[concepts/roadmap/ideas/chrome-screenshot-extension]]
