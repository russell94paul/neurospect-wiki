# Lanes — the tracker flow graph

`https://claude.ai/code/artifact/28c8ce18-6355-4357-92ab-854de3806ae5`

Answers the only two questions that matter at the start of a session: **what can be worked on right
now**, and **what is blocked on a person**.

## Build

```
python scripts/extract_flow.py     # active/*.md  ->  flow-graph.json
python processes/distributed-workflow/build_flow.py   # + flow.src.html -> flow.html
```

Then republish `flow.html` to the artifact URL above.

## What is parsed, and what is deliberately not

- **Phase status** comes from the boot-prompt heading's own marker
  (`⏭ ACTIVE`, `✅ RUN`, `⏸ GATED`, `SUPERSEDED`, `❌ NEVER RUN`, `⏸ NEXT`).
- **Gate reason** comes from that *same heading*. Body prose saying "blocked on …" is discussion,
  not status — parsing it produced ten false gates on the first run, including
  `"a human), treat the whole tracker as a proposal"`. Headings only.
- **Edges** are `[[processes/distributed-workflow/active/<name>]]` wikilinks. One tracker citing
  another IS the dependency; nothing is hand-declared.

Nothing in this pipeline is transcribed. A graph typed by hand has already drifted — which is the
failure this page exists to catch.

## The finding that justified building it

**14 of 50 phases carry no status marker the parser can read.** Some is heading-format variance
(`## Boot Prompts` plural, headings with no phase name) rather than genuine absence — but either
way *the state is not machine-readable*, and that is exactly how a stale lane survives unnoticed.
On 2026-08-29 two sessions ran in parallel and one left a cross-reference naming the wrong active
phase; this page would have shown that in a glance.

**Cheapest possible fix:** put a marker in every boot-prompt heading. The parser needs nothing else.
