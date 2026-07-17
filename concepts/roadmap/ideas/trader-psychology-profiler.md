---
tags: [roadmap-idea, neurospect, later, ai]
aliases: []
sources: [concepts/aura/mind-and-emotional-control.md, concepts/aura/psychology-foundations.md, concepts/aura/journaling-system.md]
created: 2026-04-25
updated: 2026-07-16
horizon: later
status: backlog
---

# Trader Psychology Profiler

Type the trader from journal entries, trade behaviour, mistake patterns, emotional triggers, stated goals, and risk tendencies. The profile drives more accurate coaching — different traders need different mindset interventions.

## Why it matters

A revenge trader and a hesitation trader both fail prop challenges, but for opposite reasons. Generic coaching helps neither. A profile (built from the trader's own data, not a quiz) lets every other coaching feature be specific.

## Dependencies

- Sufficient journal corpus per user — depends on [[concepts/roadmap/ideas/reduce-journaling-friction]] shipping first.
- Stable mistake tagging conventions.

## Open questions

- Static profile vs. evolving profile (likely evolving — traders change).
- How is the profile communicated back to the trader (private to coach prompt vs. user-visible insights)?
- Privacy posture if multiple users on shared infrastructure.

## Aura (dOoMeR) — supporting evidence

External validation for both the *taxonomy* a profiler would classify traders into and the *raw signal* it would classify from:

- **A ready-made failure taxonomy.** dOoMeR condenses his 142-student survey into four dominant emotional patterns — "the four killers": FOMO, revenge trading, fear of entry, and premature exits (cutting winners / holding losers) — and has students self-identify their dominant one (aura-03, [[concepts/aura/mind-and-emotional-control]]). This is close to a starting label set for the profiler: a revenge trader and a fear-of-entry trader need opposite coaching, which is exactly this idea's "Why it matters" argument, independently made by a different source.
- **Self-image drives behavior, not stated intent** (Maxwell Maltz, *Psycho-Cybernetics*, via aura-02): "you perform based on who you believe yourself to be" — dOoMeR uses this to explain why traders self-sabotage right after a funded account or a good run (self-image correction). A profiler inferring identity from *behavior* rather than a self-report quiz — this idea's explicit design choice — is directly consistent with that framing, since self-image is exactly the thing traders can't accurately self-report ([[concepts/aura/mind-and-emotional-control]]).
- **Systems over goals** (James Clear, via aura-01/aura-02) reinforces evolving over static: identity/behavior shifts as systems change, so a one-time profile would go stale the same way a fixed goal does ([[concepts/aura/psychology-foundations]]).
- **Base-rate context for why this matters at scale**: dOoMeR's 142-student survey found 67% break-even-or-losing, 95% had blown at least one account, only 34% journal consistently, and 54% rate their stress management fair/poor (aura-01, [[concepts/aura/psychology-foundations]]) — independent evidence that the population this profiler would serve is dominated by a handful of recurring behavioral failure modes, not idiosyncratic one-offs.
- **Raw input signal**: the journaling system's per-trade emotional-state fields (before / during / after) plus "did you follow your rules, if not why" and "was this in your plan, if not what triggered it" (aura-05, [[concepts/aura/journaling-system]]) are the concrete data points a profiler would ingest and classify against the four-killers taxonomy above.

## See Also

- [[concepts/roadmap/README]]
- [[concepts/roadmap/ideas/neurospect-voice]]
- [[concepts/roadmap/ideas/mistake-driven-action-items]]
