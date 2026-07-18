---
tags: [concept, advanced, frontier, neurospect, ict, liquidity, ipda]
aliases: [IPDA Data Ranges, IPDA, Liquidity Matrix, IRL ERL, PD Array Matrix]
created: 2026-07-17
updated: 2026-07-17
---

# IPDA Data Ranges & the Liquidity Target Stack

The **WHERE** layer of the frontier stack: a non-discretionary way to *rank* draw-on-liquidity targets by
algorithmic "reach." Extends — does not restate — the canonical liquidity page
[[concepts/business-logic/ict-liquidity]] (BSL/SSL/DOL), adding a lookback-range method that page lacks.

## IPDA 20/40/60-day data ranges — **windows & trading-day count ESTABLISHED (Tier 1); ranking still Tier-3**

IPDA (Interbank Price Delivery Algorithm) is ICT's *conceptual* model for how the interbank market delivers
price — **not a literal disclosed algorithm.** Its most-corroborated mechanic (the single most
cross-source-consistent figure in the whole Phase-3 pass), now **Tier-1 verbatim** for the core structure:

- **Three nested daily-chart lookback windows: 20, 40, 60 days — Tier 1 (verbatim).** From the first trading
  day of the month (or a confirmed daily structure shift), count back 20/40/60 *trading* days; each window's
  highest-high / lowest-low forms a nested range cast forward. *Verbatim (ICT): "you have a 20 day, look back
  and cast forward range … a 40 day, look back and cast forward range … a 60 day look back and cast forward
  range"* (Month 5, "Using IPDA Data Ranges"); *"a 20 day range, a 40 day range and a 60 day range added to
  the right"* (Month 5, "Quarterly Shifts and IPDA Data Ranges").
- **Anchor = first trading day of the most recent month — Tier 1 (verbatim).** *Verbatim (ICT): "you want to
  be using that first trading day of that month, put a vertical line on your chart … And then I would look 60
  trading days, to the left."* The *anchor* is a calendar date; the *count* is in trading days.
- **Two purposes:** (a) locate resting **BSL/SSL** above/below those old highs/lows (the draw on liquidity);
  (b) locate **imbalances/FVGs** due to rebalance.
- **Ranking (the *claimed* edge) — still Tier-3, UNVERIFIED.** The community framing (20-day = nearest /
  most-probable objective; 40-day = escalation; 60-day = outer / rare) was **searched for and NOT found
  verbatim** in the two Month-5 lectures — ICT states the nested 20/40/60 structure and that "the algorithm's
  going to anticipate doing a shift in the marketplace, in that range between 60 and 20 days," but gives **no
  probabilistic 20>40>60 ranking language**. Treat the ranking as community inference (Tier-3), not settled;
  Month-7 "Blending IPDA Data Ranges & PD Arrays" (unchecked this pass) is the next place to look.
- **Attribution (Tier-1, 2026-07-18 pass):** ICT **2016 Premium Mentorship Core Content, Month 5** — Lecture
  **#39 "Quarterly Shifts and IPDA Data Ranges"** and Lecture **#41 "Using IPDA Data Ranges."** Verbatim
  transcripts fetched from the quagmyre archive of ICT's own recorded audio; lecture numbers/titles
  independently corroborated against the quagmyre XWiki lecture index. (Month 7 "Blending IPDA Data Ranges &
  PD Arrays" remains a Tier-2 reference — not fetched this pass.) *Provenance caveat: transcript hosted on a
  third-party archive (quagmyre.com) of ICT's own audio; the corroborating index is the same archivist's
  XWiki catalog, so this is Tier-1-with-single-archive-corroboration.*

**Failure mode:** marking all three ranges then retroactively declaring whichever "worked" as the target
(unfalsifiable unless fixed in the plan first). **Trading-days vs. calendar-days — RESOLVED (Tier 1):** the
count is in **trading days**, verbatim — *"60 trading days 40 trading days and 20 trading days" … "the 60 to
40 and the 20 trading days left of the most recent calendar month."* The prior "favoured, pending verbatim"
caveat is now settled. The 20→40→60 "redirect cascade" ranking, by contrast, remains single-sourced
community inference (Tier-3, **UNVERIFIED** — see above); don't treat as settled.

> **⚠ Misattribution caution (2026-07-17 pass).** A widely-surfaced X/rattibha thread titled "IPDA DATA
> RANGES. 20 40 60 DAYS" that *tags* @I_Am_The_ICT is **not** ICT's own writing — it was authored by a
> different community user (@FlawInTheMatrix) applying the concept to a personal chart. Do **not** cite it as
> Tier-1; it is at best single-author Tier-3. Flagged so future sessions don't mistake the tag for authorship.

Citations: **Tier-1 primary (verbatim, quagmyre archive of ICT's own audio):** Month 5 #39 "Quarterly Shifts
and IPDA Data Ranges" — <https://files.quagmyre.com/files/ICTStudies/ICT-2016-Premium-Mentorship-Core-Content/srt/39-ICT%20Mentorship%20Core%20Content%20-%20Month%205%20-%20Quarterly%20Shifts%20and%20IPDA%20Data%20Ranges.srt>
· Month 5 #41 "Using IPDA Data Ranges" — <https://files.quagmyre.com/files/ICTStudies/ICT-2016-Premium-Mentorship-Core-Content/srt/41-ICT%20Mentorship%20Core%20Content%20-%20Month%205%20-%20Using%20IPDA%20Data%20Ranges.srt>
· lecture index (corroboration) <https://info.quagmyre.com/xwiki/bin/view/Forex/The-Inner-Circle-Trader/ICT-2016-Premium-Mentorship-Core-Content-Lectures/> ·
YouTube originals (un-fetchable 402/403): <https://www.youtube.com/watch?v=n7SPAK_tpN8> · <https://www.youtube.com/watch?v=LRKtiysz4nA>.
**Tier-2/3 (ranking + secondary):** <https://forum.ictsharks.com/t/ict-mentorship-core-content-month-5-using-ipda-data-ranges/69> ·
<https://innercircletrader.net/tutorials/ict-ipda/> · <https://www.tradingview.com/script/rTJEJb5v-ICT-IPDA-Look-Back/>.

## "Liquidity Matrix" — **SPECULATIVE-or-FRINGE as an ICT term**

Adversarially checked because it was on the research shortlist. Verdict: **not a stable ICT-originated
concept.** It is (a) a loose descriptor and (b) a **vendor brand name** — ≥3 unrelated commercial indicators
are named "Liquidity Matrix," each defined differently, none attributing the term to ICT. Detailed community
notes on the exact episodes cited as its "origin" **do not use the phrase** (direct negative evidence).

- **The real ancestor is ICT's "PD Array Matrix"** — a genuine, mechanically-specific ranked hierarchy of
  FVGs / order blocks / breaker blocks / mitigation blocks used to prioritize *which* array to trade.
- **Ruling for this wiki:** do not build a "liquidity matrix" concept. Where the idea is wanted (liquidity is
  layered across timeframes), use ICT's real vocabulary — liquidity pool, BSL/SSL, DOL, **PD Array Matrix**.

Citations: <https://ictflow.com/blog/ict-pd-array-matrix-explained> (the real term) ·
<https://forum.ictsharks.com/t/2023-ict-mentorship-one-trading-setup-for-life/371> (phrase absent from source notes).

## IRL / ERL — **ESTABLISHED (Tier 2)**

Genuine, well-sourced ICT vocabulary that *is* the defensible version of a "liquidity stack":

- **ERL (External Range Liquidity):** liquidity *outside* the current dealing range — old highs/lows, the DOL magnet.
- **IRL (Internal Range Liquidity):** liquidity *inside* the range — unmitigated FVGs, minor swings.
- Price cycles **external → internal → external**. This composes cleanly with IPDA (the 20/40/60 highs/lows
  are the ERL targets) and with premium/discount ([[concepts/aura/ranges]]).

## Multi-timeframe liquidity cascade & LRLR/HRLR — **EMERGING / community shorthand**

- **"Weekly → daily → session → intraday" cascade** is a *reasonable extrapolation* from genuine ICT blocks
  (multi-TF bias; larger-TF levels carry more weight because resting orders are larger) — but **no source
  documents ICT stating it as one named sequence. Label: EMERGING / community-synthesis**, not verbatim ICT.
- **LRLR vs HRLR** (Low/High Resistance Liquidity Run): widely circulated, consistently defined (LRLR = clean
  fast run, minimal opposing structure; HRLR = grinding run through order blocks/PD arrays) — but at least one
  dedicated source (ictflow.com) **explicitly disclaims any direct ICT citation**. **Label: SPECULATIVE** as
  ICT-coined; treat as community shorthand for a real underlying idea (resistance quality of a run).
- **Failure mode:** weighting every old high/low equally regardless of timeframe; relabeling a "failed" LRLR
  as HRLR after the fact (unfalsifiable in real time).

## New confluence surfaced

> **SD-validity within the IRL/ERL cycle** *(SPECULATIVE — offered for a future backtest, documented nowhere):*
> an unreached standard-deviation / IPDA target stays "live" as the external magnet only while price is inside
> an IRL consolidation; once external liquidity is actually taken, a **new** IRL/ERL cycle begins and prior
> projections should be recomputed from the new range rather than carried forward. Bridges two genuinely
> separate ICT ideas (SD-projection validity + IRL/ERL cycling) that the sources never connect. See
> [[concepts/advanced/cbdr-and-sd-projections]].

## How it interacts with the Unified Playbook

The **WHERE** filter in the [[concepts/advanced/README|confluence stack]]: mark 20/40/60-day highs/lows on
NQ/ES/YM; the nearest level is the active near-term draw. A setup ([[concepts/mastery/unified/README]] Layer 3)
gains conviction when its target *is* an IPDA/ERL level, its manipulation sweeps that level, and the Layer-2
SMT stack confirms non-confirmation across the triad at the sweep.

## See Also

- [[concepts/business-logic/ict-liquidity]] — canonical BSL/SSL/DOL (this page extends it with ranked targets)
- [[concepts/advanced/cbdr-and-sd-projections]] — the SD projections that price *toward* these targets
- [[concepts/advanced/README]] — frontier hub + confluence stack
- [[concepts/mastery/unified/README]] — Layer 3 execution
