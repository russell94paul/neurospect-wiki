---
tags: [roadmap-idea, neurospect, next]
aliases: []
sources: [concepts/aura/journaling-system.md]
created: 2026-04-25
updated: 2026-07-16
horizon: next
status: backlog
---

# Mistake-Driven Action Items

Recurring mistake tags become concrete improvement tasks tied to playbooks, rules, or coaching prompts. "Took trade outside kill zone" three times in a week → action item: pre-trade kill-zone check enabled on next session.

## Why it matters

The journal already captures `mistake_tags` (TEXT[] in the trade schema). Today they're searchable but not actionable. Converting them into recurring tasks is the simplest path from "I journal" to "the journal changes my behaviour."

## Dependencies

- Existing mistake tagging in [[concepts/architecture/trade-schema]].
- Light task model (new table or reuse `coaching_events`?).

## Open questions

- Threshold for "recurring" — count, recency window, or model-driven?
- Should action items integrate with the AI Coach panel (next live session reads recent active items into the system prompt)?
- Manual override for trader to dismiss false positives.

## Aura (dOoMeR) — supporting evidence

Independent validation of the exact mechanism this idea automates — recurring tagged pattern → concrete rule change — plus a consistency rule worth encoding alongside it:

- **Pattern-extraction, worked example**: dOoMeR's own headline illustration is "if 80% of your losses come from taking trades after 11:00am, you now have data telling you to stop trading after 11:00am. That's not a feeling, that's evidence" (aura-05, [[concepts/aura/journaling-system]]). That is this idea's "took trade outside kill zone → pre-trade check" example in a different domain — the same recurring-signal-to-rule mechanism, done manually in Aura's method vs. automated here.
- Aura's method is manual/reflective (a human reviewing a Notion journal weekly) where this roadmap idea is closer to automated detection — the underlying signal (recurring tagged pattern → concrete, fixable rule) is the same mechanism in both ([[concepts/aura/journaling-system]] Product Reconciliation Notes).
- **"Never miss twice"**: dOoMeR's consistency rule — missing one journal entry is an accident, missing twice in a row is the start of a new bad habit; if you skip a day, journal the next day no matter what (aura-05, [[concepts/aura/journaling-system]]). Worth considering as a candidate action-item type in its own right (a generated item for "journaling gap," not just for trading mistakes), since it's the same recurring-lapse-to-corrective-action logic this idea already applies to `mistake_tags`.

## See Also

- [[concepts/roadmap/README]]
- [[concepts/architecture/trade-schema]]
- [[concepts/architecture/tradingview-connector]]
- [[concepts/roadmap/ideas/trader-psychology-profiler]]
