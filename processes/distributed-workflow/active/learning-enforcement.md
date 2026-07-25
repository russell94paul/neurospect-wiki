---
tags: [distributed-workflow, active, neurospect, mastery, enforcement, grading, gamification]
aliases: [Learning Enforcement Tracker, Drill Grading, Anti-Cheat, Gamification Workstream]
sources: []
created: 2026-07-25
updated: 2026-07-25
---

# Learning Enforcement — Workstream Tracker

Make `neurospect-learn` a platform that **enforces genuine learning**: a drill can only be completed by
producing **evidence of the work** (a screenshot of your markings for that concept — ranges, standard
deviations, swings, FVGs, SMT, …), that evidence is **graded**, and the whole loop is **gamified** so it drives
consistency. The Phase 5 arc built the skeleton (curriculum, progress, planner, journal, expectancy, gate);
this workstream makes the progress in it **impossible to fake**.

> **STATUS (2026-07-25): scoping only — no phases started, no boot prompt authored yet.** By Paul's sequencing,
> the first session's boot prompt (a **deep-research + design session, Opus 5**) is written **after Phase 6 of
> [[processes/distributed-workflow/active/learning-platform-ui]] lands**, so the research starts from the real
> post-Phase-6 code. This page exists now to hold the vision, the constraints, and the open questions that
> session must answer.

## Goal (Paul, 2026-07-25 — in his framing)

> "I really want to put a plan together that will ensure that **the user cannot cheat the app** in terms of
> completing exercises and understanding specific topics … we need to implement some sort of **grading system
> for the drills**, meaning **screenshots would have to be uploaded of the markings** for specific concepts
> ex. ranges, std-deviations and all other concepts and topics that are covered."
>
> "The selling point and the main thing I want to focus on is ensuring that this platform **enforces the user
> to learn**, **gamifies it** so it helps the user to remain consistent, and **tracks their progress**."

Three deliverables follow from that:

1. **Verified drills.** A rep counts only when evidence of the work exists and passes a grade — not when the
   user clicks "done".
2. **Anti-cheat.** The shortcuts (recycling one screenshot, bulk-marking 50 reps in a minute, self-declaring
   understanding) are closed off, or at minimum made *visible* rather than silent.
3. **Gamification for consistency.** The mechanics that keep Paul showing up daily, built on the streak /
   adherence / pace surfaces the Study Planner already computes.

Plus a content strand Paul named alongside these: **revisit the structure of the learning path and improve the
exercises/drills themselves** (see §Scope boundary — content vs app).

## North Star (inherited, and sharpened for this workstream)

This workstream inherits the platform north star — **discipline & accountability by design, not by choice**
(stated in full in [[processes/distributed-workflow/active/learning-platform-ui]] §North Star) — and sharpens
it with the framing that makes the "anti-cheat" problem tractable:

**The adversary is self-deception, not an attacker.** This is Paul's personal tool: nobody else gains from
faking a rep. So the goal is *not* tamper-proof security (which would be both impossible and pointless here) —
it is to make **the honest path the path of least resistance**, and to make any shortcut **visible and
recorded** rather than silently absorbed into a progress number Paul will later trust with real capital. A
design that merely *frustrates* honest work fails this north star just as badly as one that lets a rep be
faked: the gate's whole value is that its numbers mean something when it says "cleared".

## What already enforces the process (do NOT redesign these)

The research/design session must build on the shipped enforcement rather than reinvent it:

- **The Readiness-to-Live Gate is non-overridable** — no `cleared` column, endpoint, or UI control; the verdict
  is recomputed per read from the concept ladder + backtest expectancy + four attestations (§5g as-built in
  [[concepts/architecture/learning-platform]]).
- **Ladder advance is already gated** — `PATCH /api/progress` rejects Can-mark+ unless reps ≥ the parsed rep
  target *and* confidence is set; watch-only (U5 frontier) concepts are capped at Can-mark and are never
  gate-eligible (§5e-1 as-built).
- **The planner is prescriptive and logs skips** — `/today` says what to do; a skip is recorded and hurts
  adherence, never hidden; streak / adherence / days-behind / pace are surfaced (§5e-3 as-built).
- **The journal separates backtest from live** and expectancy is computed only over closed trades, with sample
  size visible so an under-evidenced model reads as such (§5f as-built).

**The honest gap this workstream closes:** every one of the above ultimately trusts a **self-reported rep
count** and a **self-rated confidence**. `reps` is just an integer the user increments. That is the single
weakest link in the chain, and it is exactly what evidence-backed grading replaces.

## Open questions the research + design session must answer

Recorded now so the session starts from the real problem, not a blank page. None of these are decided.

**Evidence + grading**
1. What *is* a unit of evidence — one screenshot per rep, per drill session, or per concept? What does a rep
   mean for a day/session-based drill (the `rep_targets` parser already distinguishes reps / days / sessions /
   qualitative / habit)?
2. **How is a marking graded?** Candidates to evaluate, not assume: AI vision grading (Claude, against a
   per-concept rubric), a structured self-check rubric, deterministic/heuristic checks, human-in-the-loop
   review, or a hybrid that escalates. What is the false-negative cost — a wrongly rejected rep is the fastest
   way to make Paul abandon the tool.
3. Where do the **rubrics** come from? The per-concept bar is canonical in the wiki
   ([[concepts/mastery/README]] ladder, the two `exercises.md` drill maps, the entry-model YAML) — a rubric must
   be *derived from* those, never invented alongside them.
4. Is grading **blocking** (a rep does not count until graded) or **asynchronous** (rep provisional, confirmed
   later)? What happens offline / when grading fails?
5. Does a grade carry a **score** (feeding confidence / ladder position) or just pass-fail?

**Anti-cheat**
6. Which shortcuts actually need closing? Candidates: reusing/duplicating an image (perceptual hashing),
   implausible rep pacing, screenshots that aren't charts at all, back-dating, bulk marking. Which are worth the
   complexity, and which should merely be **surfaced** (an honesty signal) rather than blocked?
7. What is the **appeal / override path**, and who can use it? (The gate has none by design — does grading need
   one, and does that reopen the hole?)

**Gamification**
8. Which mechanics actually drive consistency for a solo learner, per the evidence — and which are noise?
   (XP/levels, badges, quests, streak-freeze economics, loss aversion, variable reward, self-competition —
   there is no leaderboard in a single-user app.) This is the part that most warrants genuine external research.
9. How do the mechanics interact with the existing streak / adherence / pace surfaces without double-counting?
10. **The failure mode to design against:** gamification that rewards *activity* over *mastery* would actively
    undermine the gate. What keeps the points honest?

**Storage + platform**
11. Object storage (R2 is already in the wider Neurospect stack) — keys, size/format limits, retention,
    cost, and privacy of chart screenshots.
12. Does this need the app deployed off localhost to be useful (uploads from a phone/tablet while marking
    charts)? Deploy/hosting is currently unscoped in **any** tracker — flag if it becomes a dependency.
13. What does the evidence layer owe the **missed-trade log** and the **journal** (both deferred screenshots to
    this workstream — see §Inherited debt)?

**Curriculum**
14. Which drills in the two `exercises.md` libraries are weak, ambiguous, or ungradable as written — and what
    would make them gradable? (Content work; see the scope boundary below.)

## Scope boundary — content vs app (read before planning phases)

Paul's ask spans two different kinds of work, and conflating them is how this workstream would stall:

- **Wiki/content work** — the *structure of the learning path* and the *quality of the exercises/drills* live in
  [[concepts/mastery/README]], the two `exercises.md` drill maps, and the per-track learning-path pages. The
  wiki is canonical; the app ingests/consumes it. Improving a drill = editing the wiki, then re-seeding.
- **App work** — evidence capture, grading, anti-cheat, gamification mechanics, and their data model live in
  `neurospect-learn` (code is ground truth once written).

A drill can only be graded if its wiki definition states a gradable bar, so the **content pass likely has to
lead** (or at least run alongside) the app phases. The research session should propose the split.

## Inherited debt this workstream owns

Deferred *into* this workstream by earlier decisions — do not build these ad hoc elsewhere:

- **Journal screenshots / R2** — deferred at 5c, still deferred at Phase 6 (Paul, 2026-07-25) precisely because
  it is the same primitive as drill evidence.
- **`missed_trade_screenshots`** — the child table specced in [[concepts/architecture/trade-schema]] §Missed
  Trades is deliberately omitted from Phase 6's missed-trade log for the same reason.

## Lane

- **This wiki** produces the design artifacts + this tracker: `concepts/architecture/*` (a canonical
  enforcement/grading doc), improvements to `concepts/mastery/*` content, and this page.
- **The app code** lands in `C:\Users\PaulRussell\repos\neurospect-learn` (the Phase 5 app — not a new repo).
  Per [[CLAUDE]] §Architecture Doc Integrity, once code exists the code is ground truth.
- Isolation Rule applies (Neurospect only; no ALDC content/refs).
- The distributed-workflow pattern docs are referenced by absolute path (never wikilink):
  `C:\Users\PaulRussell\repos\wiki\processes\distributed-workflow\orchestration-pattern.md`,
  `…\session-lifecycle.md`, `…\tracker-template.md`.

## Plan

### Phase E1 — Deep research + design session (NOT YET STARTED; boot prompt authored after Phase 6)
An **Opus 5**, plan-mode, research-heavy session whose artifact is the plan: answer the open questions above,
propose the grading/evidence model, the anti-cheat set, the gamification mechanics, the data model, and the
phase split. Expected to include genuine external research (learning science + what comparable trading/skill
platforms do) alongside a read of the shipped code and the mastery corpus.

### Phases E2+ — TBD by E1
Not enumerated until the design lands. Likely shape: a content/curriculum pass to make drills gradable, an
evidence-capture + storage phase, a grading phase, then gamification — but E1 owns that call.

## Session Log

### 2026-07-25 — workstream created (scoping only)
- trigger: at the Phase 5g sign-off Paul set the next direction — verified drill grading via uploaded screenshots
  of chart markings, anti-cheat, and gamification for consistency — and chose (via AskUserQuestion) to give it
  **its own tracker** rather than extend the completed `learning-platform-ui` workstream.
- decided: Phase 6 of `learning-platform-ui` closes the Phase-5 debt first (stage-attestation wiring, missed-trade
  log, `position_size`); **screenshots/evidence storage are deferred into THIS workstream on purpose**, since the
  journal's deferred screenshots and `missed_trade_screenshots` are the same primitive the grading model must
  define; and this workstream's first boot prompt is authored **after Phase 6 lands** (Paul's sequencing), for an
  Opus 5 deep-research session.
- did (wiki only, no code): created this tracker — goal in Paul's framing, the sharpened north star (the
  adversary is self-deception; the honest path must be the easy one), an inventory of what already enforces the
  process plus **the honest gap** (every existing check ultimately trusts a self-reported `reps` integer and a
  self-rated confidence), 14 open questions for E1, the content-vs-app scope boundary, and the inherited debt.
  Cross-linked from `learning-platform-ui`; updated index.md; appended log.md.
- next: land Phase 6 in [[processes/distributed-workflow/active/learning-platform-ui]], then author the E1
  deep-research boot prompt here.

## See Also

- [[processes/distributed-workflow/active/learning-platform-ui]] — the completed Phase 5 workstream this builds on
- [[concepts/architecture/learning-platform]] — the canonical app architecture (as-built through 5g)
- [[concepts/mastery/README]] — the mastery ladder, confidence scale, and Readiness-to-Live Gate (canonical)
- [[concepts/mastery/aura/exercises]] · [[concepts/mastery/ict-course/exercises]] — the two drill libraries the
  grading rubrics must derive from
- [[concepts/aura/journaling-system]] — the journaling discipline the enforcement loop is meant to instil
