---
tags: [concept, aura, neurospect, risk-management]
aliases: [Aura Risk Management, Evolving R, The Free Trade Lie, Blueprint for Trading Success]
sources: [sources/neurospect/aura/aura-13-risk-management.md]
created: 2026-07-16
updated: 2026-07-16
---

# Risk Management (Aura)

dOoMeR's risk-management video is framed as a document, not a topic: "risk management is not a chapter
in a trading book. It is the trading book." (aura-13) The entire framework is explicitly derived from
and attributed to **Tom Dante's "Blueprint for Trading Success"** — dOoMeR presents almost all of the
formulas and rules below as Dante's, refined through his own experience as a prop-firm floor trader
managing firm capital. The video has two halves: a conceptual/mathematical half (capital protection,
R, expectancy, drawdown math, prop-firm critique) and a short worked-chart half illustrating "evolving
R" in a live trade.

## Attribution and Source

- Core document: Tom Dante's **"Blueprint for Trading Success."** dOoMeR: "This document was derived
  [from] his video... [it] was the core foundation of where this information and where I learned and
  constantly refer back to for my risk management." (aura-13)
- Note for wiki reconciliation: this video repeatedly and clearly names **"Tom Dante"** in full — this
  resolves the ambiguous "Tom" / "Th[om]" attribution flagged in [[concepts/aura/psychology-foundations]]
  (aura-01), which cites the same figure without a confirmed surname. Worth updating that page's
  uncertainty note during reconciliation.

## The Risk Hierarchy

Dante's stated order of operations, which dOoMeR treats as non-negotiable (aura-13):

1. **Conserve capital.**
2. **Generate an income.**
3. **Roll the account.**

Most traders skip straight to step 3 — obsessed with upside, barely thinking about downside — "that is
the reason they never get to step two." The rule that governs step 1: **capital is protected before any
trade is placed.**

## Capital Protection: The 10/90 Split

- Dante keeps only **10% of his trading funds with his broker** and **90% in a savings account.**
- Rationale: brokers fail. "If your broker disappears tomorrow, a 10% exposure is a setback. A 100%
  exposure ends your trading career." (aura-13)
- **Risk percentages are calculated off the total pot** (broker + savings combined), not off the amount
  sitting at the broker. This matters for every per-trade % figure below — they are % of total capital,
  not % of account balance at the broker.

## Mindset: You Are the Edge

- "A trader with a mediocre edge and excellent risk management will beat a trader with an excellent edge
  and mediocre risk management every time" — the second trader "gets blown up before the edge has a
  chance to play." (aura-13)
- Corollary: **the trader is the edge, not the strategy.** If the strategy itself were the edge, success
  rates across students of the same strategy wouldn't vary — but they do, because execution, discipline,
  planning, and risk management vary.

## The Math: Break-Even Win Rate

Formula, stated directly: **Break-even win rate = 1 / (1 + Risk:Reward)** (aura-13)

| You risk 1 to make... | Break-even win rate |
|---|---|
| 0.5 | ~67% (must win 2 of every 3 trades) |
| 1 | 50% |
| 2 | 33% |
| 3 | 25% |

Takeaways stated explicitly:
- A **1:3 trader can be wrong 3 out of 4 times and still make money.**
- A **1:0.5 trader needs to win 2 out of every 3 trades just to break even.**
- The higher the risk:reward, the lower the win rate required — but retail traders gravitate toward
  tight targets (high win rate, low R:R) because "tight targets hit more often and feel good." The
  discomfort of losing more often at wider targets is "the price of admission to a sustainable edge."

## Win Rate Alone Is Meaningless

- "If someone tells you their strategy has a 70% win rate, your next question must be at what
  risk-to-reward. Without that second number, the win rate is useless." A 70% win rate at 1:0.5 is
  barely profitable; a 35% win rate at 1:3 is more profitable. (aura-13)
- **The 80/90% win-rate red flag:** if a strategy truly had a fixed 80-90% win rate with defined risk
  and reward, "it would be automated" and its discoverer would already be running it at scale. Social
  media educators advertising these numbers are describing something that requires discretion to
  execute — and discretion means win rate isn't a fixed property of the strategy at all.
- **Win rate is a fluid output of the trader, not the strategy.** The same strategy run by a disciplined
  trader might produce 55%; run by an undisciplined trader, 35%. "The strategy did not change, the
  trader did."
- **Even your own win rate moves.** Every stop moved, every profit taken early, every trade held past
  target or cut early changes the realized R and therefore the realized win rate. "Your win rate is a
  moving target because you are constantly changing the definition of a win and a loss."
- Stated takeaway: stop chasing win rate. Focus on **setup quality** and **risk management skill.** "A
  solid trader with a 45% win rate and ruthless risk management will outearn a sloppy trader with a 65%
  win rate and no discipline."

## Thinking in R, Not Dollars

- **R = the amount risked on a single trade.** Risk $200 → 1R = $200.
- A $400 winner on that risk = **+2R**. A stopped-out loser = **-1R**. A winner cut early for $100 =
  **+0.5R**.
- Why: dollar amounts are "emotionally distorted" — a string of $200 losses feels catastrophic when
  tired or stressed even if statistically routine. R strips that out: "a -1R loss is a -1R loss." The
  stated goal is to trade the *process*, not the P&L.

## Expectancy: The One Number That Matters

Formula, stated directly: **Expectancy = (win rate × average win) − (loss rate × average loss)**, in R
terms. (aura-13)

- An expectancy of **0.5R** means every trade nets 0.5R on average — over 100 trades, that's **+50R**.
- Positive expectancy = the definition of an edge. Negative expectancy = a losing strategy "no matter
  how good the trades feel."
- Worked contrast from the video: a 50% win rate at 1:2 R:R produces a *strong* edge, while a 70% win
  rate at 1:0.5 produces a *tiny* edge that "a small drop in win rate wipes out entirely." High win
  rate + low R:R is described as **the most fragile combination in trading.**

## Evolving Risk: Trade Management *Is* Risk Management

The video's central technical claim: **risk is not calculated once at entry and forgotten — it is
recalculated continuously from the current price and current stop.** (aura-13)

- **The "free trade" lie:** if you have a 10-pip stop and a 20-pip target (1:2 R:R) and price runs to
  19 pips in your favor, moving your stop to breakeven does **not** make the rest "free." From that
  point, you are risking **19 pips to make 1 pip.** If price reverses and stops you out at breakeven,
  "you did not get out flat. You just paid the market 19 pips of open equity. That is real loss dressed
  up as a non-event."
- The reframed question at every point in a trade: not "what was my risk when I entered?" but **"what is
  my risk from here, right now, given what's still on the table?"** If the honest answer is embarrassing
  (e.g., risking 19 to make 1), "that is the market telling you to take a profit or get out."
- Anecdote from managing firm capital on the trading floor: newer traders sitting relaxed, disengaged,
  with a stop at breakeven and price near target, treating a reversal-to-breakeven as a non-event ("not
  a win, not a loss"). dOoMeR's framing: that reversal cost the firm the difference between a large
  realized gain and zero — "how horrible does that sound?"
- Stated general goal as a trade develops: **maintain at least a 1:1 risk:reward from the current price**
  — don't let open risk exceed remaining potential reward. This is presented as a floor/office-trading
  standard tied to managing capital that isn't the trader's own, applied more loosely (his words: "may
  not be always doing this") on his personal account.

> **Scope note:** this video's "stop placement" content is entirely about *dynamic* stop management
> (trailing/breakeven decisions as the trade evolves), not the technical method for placing an initial
> stop (e.g., behind a swing point). That's presumably covered in [[concepts/aura/swing-points]] — not
> addressed here.

## The Asymmetry of Losses

Stated directly: **losses and gains are not symmetrical**, and the video closes with the formula:
**Recovery % = Drawdown / (1 − Drawdown).** (aura-13)

| Drawdown | Gain required to recover |
|---|---|
| 10% | 11.1% |
| 50% | 100% (double the remaining capital) |

- Why: you recover from a shrinking base. Lose 50% of $10,000 → $5,000 remains → recovering to $10,000
  requires earning $5,000 *on a $5,000 base*, i.e. a 100% return.
- Practical corollary flagged in the video: if you hold **per-trade risk constant as a % of total
  capital**, the dollar amount shrinks as the account shrinks (1% of $10,000 = $100; 1% of $5,000 = $50).
  If you don't recalculate and keep risking the original dollar figure after a drawdown, that fixed
  dollar amount becomes a larger % of the (now smaller) account — silently increasing your real risk
  exposure. *(The video's own worked numbers in this passage are garbled in the auto-caption — see
  Transcription Notes below — but the underlying rule is clear and consistent with the rest of the
  framework: recalculate % risk off current capital, not a fixed dollar figure.)*
- Framing: a 10% drawdown is "a bad week," recoverable. A 50% drawdown is "a career-threatening event"
  — and the strategy that produced it is "possibly broken."

## Drawdown Circuit Breaker (Dante's 10R Rule)

- **Dante's rule: stop trading completely at a 10R drawdown on any strategy, until a full
  investigation is done.** At his stated 2% risk per trade, 10R = a **20% drawdown.** (aura-13)
- His own worst-ever drawdown was **12R**, which he describes as "genuinely painful."
- The rule must be **written down before the drawdown starts** — precommitted "so that when emotion
  takes over, the decision has already been made." dOoMeR presents 10R as "the right number for every
  trader" (i.e., a general recommendation, not just Dante's personal figure).
- **The revenge trap:** sizing *up* during a drawdown to recover faster is explicitly rejected — "it is
  doubling the probability of reaching a catastrophic drawdown from which there is no return." The rule
  is: **sizing must go down in a drawdown, not up** — reduce risk per trade, reduce trade frequency, or
  stop entirely until the process is revalidated.

## Per-Trade and Per-Day Risk Limits

**Per-trade risk:**
- Standard range: **1-2% of total capital per trade.** Dante uses **2%**, calculated off the total pot
  (broker + savings), not the broker-only balance.
- At 2% risk, a 10-loss streak is roughly a **20% drawdown** — "painful but survivable."
- At 5% risk, the same 10-loss streak becomes a **40% drawdown** — "the recovery math gets ugly fast."
  Higher per-trade risk "does not make you more aggressive. It makes you more fragile."
- **Sizing rule of thumb:** losing streaks are normal — at a 50% win rate, a 5-loss streak happens
  "roughly every 30 trades," and a 7-loss streak "is not rare over the course of a year." **If 10
  consecutive losses would draw you down more than 20%, your per-trade risk is too high.**
- Firm-capital framing: there is no restart button on managed capital — "you have to size accordingly
  to get out. There is no restart." This is presented as the standard a trader should hold themselves to
  even on a personal account.

**Daily stop:**
- A **hard cap on loss per session** — "how much you are willing to lose in a single session."
- **Common daily stop: 2 to 3R.** Once hit, "the trading day is over. No more setups, no matter how
  good they look."
- Rationale: some days simply aren't conducive to the strategy, and continuing to trade on them is how
  "good setups get mishandled and bad setups get taken." Framed explicitly as survival, not defeat:
  "there is nothing wrong with saying I can't beat the market today... there is always tomorrow."
- **The case for it:** without a daily stop, variance and tilt compound — two losses produce
  frustration, frustration produces a marginal setup taken to "get it back," that loss produces sizing
  up, and a controlled session turns into an extended, uncontrolled one *(the transcript's specific
  phrase here — "turns a 2-hour trade into an 8 hour trade" — is unclear/possibly a caption artifact;
  see Transcription Notes)*. The accepted trade-off: you'll occasionally miss a setup that would have
  worked. "You are buying protection against the tail risk of your own emotion."

## Prop Firms and Challenge Accounts: The Social-Media Trap

dOoMeR treats this as a direct extension of risk management, not a separate topic (aura-13):

- **The business model:** social-media-advertised prop/challenge firms profit from traders **failing**
  the challenge and paying to re-enter — "every failed trader, every failed challenge is a sale... it's
  a lot harder for them to make money when you make money."
- **Typical challenge structure cited:** an **8-10% profit target within 30 days**, a **5% daily loss
  limit**, and a **10% total drawdown** cap. dOoMeR's read: these rules make the mathematically sound
  path (small risk, patient execution) "nearly impossible in the time window," so sizing up to hit the
  target fast becomes "the only way most participants can realistically pass" — and the firm profits
  from that mismatch either way.
- **Why the psychological damage is worse than the money:** on a live account, a 20% drawdown is 20% of
  real net worth — it forces review and hard decisions. On a challenge account, the consequence of a
  drawdown is losing the account and paying another entry fee — "the worst outcome is losing the entry
  fee. That is not a consequence. That is a cost of entry." No real capital is on the line, so no real
  psychological weight pushes the trader to protect it.
- **The gambling loop:** pay fee → take losses near the daily limit → oversize to recover because only
  the fee is at risk → blow the account → pay again → repeat. No drawdown-management skill is ever
  built, because the trader "never actually had to manage one. They simply restarted." A live account
  has no restart button; the only way out of a real drawdown is smaller size, better setups, and
  patience — "the single most valuable skill a professional trader develops," and one the challenge
  model specifically prevents from forming.
- **Not a blanket condemnation:** "I'm not saying that you must stay away from these firms... you can
  leverage them." The caution is narrower: they're "built to exploit... your vices," incentivizing
  overleverage and overtrading, so a trader using them needs *more* self-imposed accountability, not
  less.
- **The honest alternative:** build a small but verifiable track record on a real account, over enough
  trades to prove the edge and the risk discipline are both real — "that record opens doors to actual
  firms with actual seats."

## Psychological Rules Tied to Risk

- **No sizing up after losses / in a drawdown** — explicitly the opposite of what's required (see 10R
  rule above).
- **The daily stop removes in-the-moment decision-making** — the rule is set in advance specifically so
  a tilted trader doesn't get to relitigate it mid-session.
- **Survival is the explicit goal**, not being right most often: "the trader who is still in the game 6
  months from now will always beat the trader who was right more often but did not survive... did not
  size to survive variance."
- Closing framing of the whole video: **"discipline over drama, survival over speed. Get the sizing
  right and the rest becomes possible. Get it wrong and nothing else matters."**

## Worked Chart Example (Evolving R)

The video closes with a brief chart walkthrough (continuing a trade setup from the prior day's lesson)
illustrating the "evolving R" concept live:

- Entry against a higher-timeframe-range equilibrium target, trade develops with a large favorable move.
- As price extends, the stop is trailed up toward the highest point price has visited, rather than left
  static — described as "constantly managing the trade, managing your risk."
- Restated general rule: **the goal is to always maintain at least a 1:1 risk:reward from wherever
  price currently is** — never risk more (from current price) than you're willing to make.
- dOoMeR distinguishes his **personal account posts on X** (where the stop shown in screenshots doesn't
  always reflect the stop he actually trailed to, deliberately, to prevent setup reverse-engineering)
  from his **firm-capital management on the floor**, where trailing is done tightly and consistently
  because of "strict expectations" tied to managing money that isn't his own.
- Closing principle repeated from earlier in the video: a loss taken *while following the plan and
  managing risk correctly* is acceptable — "that is a part of the job." A loss taken because a stop was
  left static and never trailed (i.e., a management failure) is the failure mode being warned against.

*Note: the specific pip-by-pip numeric table dOoMeR narrates in this section (references to "-10 1R,"
"19 to 1," "15 pip stop trailed at plus 10," "five pips over profit") is heavily garbled in the
auto-caption — likely because he was reading values off an on-screen chart/table rather than stating
them in clean prose. The two fully legible data points — the 10-pip-stop/20-pip-target (1:2) setup and
the "19 pips in profit, moved to breakeven = risking 19 to make 1" example — are captured above with
confidence; the intermediate trailing stages are not reliably reconstructable from this transcript.*

## Quick-Reference: Concrete Numbers

| Rule | Number (aura-13) |
|---|---|
| Broker exposure | 10% at broker / 90% in savings |
| Per-trade risk | 1-2% of total capital (Dante: 2%, off total pot) |
| Daily stop | 2-3R, hard stop for the session |
| Drawdown circuit breaker | 10R (= 20% at 2% risk) → stop trading, full investigation |
| Dante's worst drawdown | 12R |
| Break-even win rate @ 1:0.5 | ~67% |
| Break-even win rate @ 1:2 | 33% |
| Break-even win rate @ 1:3 | 25% |
| 10-loss streak @ 2% risk | ~20% drawdown |
| 10-loss streak @ 5% risk | ~40% drawdown |
| Recovery from 10% drawdown | 11.1% gain needed |
| Recovery from 50% drawdown | 100% gain needed |
| Typical prop-firm challenge | 8-10% target/30 days, 5% daily loss limit, 10% total drawdown |
| "Too high" per-trade risk test | 10 straight losses would drop account >20% |

## Transcription Notes (Jargon/Mis-hearing Corrections)

- "trail risk of your own emotion" → almost certainly **"tail risk"** (standard risk/finance term);
  corrected silently in the prose above.
- "riskto-reward," "port trade risk," "draw on," "torch to trail" → cleaned to "risk-to-reward,"
  "per-trade risk," "drawdown," "choice to trail" respectively — clear auto-caption artifacts.
- "This document was derived his video" → read as "derived **from** his video."
- The pip-by-pip trailing-stop numeric sequence in the Worked Chart Example section is flagged above as
  not reliably reconstructable — presented as-is where legible, omitted where not.
- "turns a 2-hour trade into an 8 hour trade" (daily-stop section) is preserved as spoken but flagged as
  semantically unclear — possibly describing a controlled session extending into an uncontrolled one
  rather than a literal single trade's duration.

## Contradictions / Open Questions

- None of dOoMeR's own stated rules contradict each other in this video — the 2%/2-3R-daily/10R-circuit-
  breaker framework is internally consistent throughout.
- One notable **tension worth flagging for reconciliation**, not a contradiction within this video: he
  states firm-capital management requires very tight, continuous stop-trailing ("strict expectations"),
  but also admits his **personal account** and public X posts don't always reflect that same tightness
  ("on my personal account I may not be always doing this"). He doesn't reconcile which standard he
  recommends *students* hold themselves to — the firm standard or the looser personal-account practice.

## See Also

- [[entities/people/doomer]]
- [[concepts/aura/README]]
- [[concepts/aura/psychology-foundations]] — resolves the "Tom"/"Th[om]" attribution ambiguity from aura-01
- [[concepts/aura/discipline-systems]]
- [[concepts/aura/swing-points]] — initial technical stop placement (not covered in this video)
- [[concepts/aura/trade-reviews]] — worked examples continuing this video's chart walkthrough
