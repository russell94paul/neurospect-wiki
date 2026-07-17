---
tags: [roadmap-idea, neurospect, later, risk]
aliases: []
sources: [concepts/aura/risk-management.md, concepts/aura/mind-and-emotional-control.md]
created: 2026-04-25
updated: 2026-07-16
horizon: later
status: backlog
---

# Overtrading & Risk Limit System

Detect overtrading behaviour and enforce trader-survival rules: daily loss limits, max trades per day, cooldowns after losses, drawdown awareness, account-protection thresholds aligned with prop-firm rules.

## Why it matters

In prop trading, the rules that kill accounts are universal (daily loss limit, max contracts, news embargo). Most blow-ups are behavioural, not analytical. Building this in turns Neurospect from a review tool into a live discipline layer — a much stickier value prop.

## Dependencies

- Live broker data ([[concepts/roadmap/ideas/tradovate-integration]]).
- Account-rule schema (per-firm thresholds).

## Open questions

- Hard block vs. friction (cooldown timer, forced checklist) vs. notification-only?
- Per-firm preset rule sets (Topstep, Apex, etc.) vs. user-defined?
- How does the risk system interact with the AI Coach — does the coach refuse to evaluate setups when a daily loss limit is hit?

## Aura (dOoMeR) — supporting evidence

Concrete, codifiable limit values plus the behavioral mechanism the "live discipline layer" framing needs — both attributed to Tom Dante's "Blueprint for Trading Success" as taught by dOoMeR:

- **Per-trade risk:** 1-2% of total capital per trade; Dante's own figure is 2%, calculated off *total* capital (broker + savings), not broker balance alone (aura-13, [[concepts/aura/risk-management]]).
- **Daily stop:** a hard cap of 2-3R loss per session — once hit, "the trading day is over, no matter how good the setups look." Framed as removing an in-the-moment decision, not a suggestion evaluated mid-session (aura-13, [[concepts/aura/risk-management]]).
- **Drawdown circuit breaker:** Dante's 10R rule — stop trading entirely at a 10R drawdown (≈20% at 2% per-trade risk) until a full investigation is done; the rule must be written down *before* the drawdown starts, "so that when emotion takes over, the decision has already been made" (aura-13, [[concepts/aura/risk-management]]).
- **No sizing up in a drawdown / no revenge trading:** explicitly rejected — "sizing must go down in a drawdown, not up." This is a direct, ready-made rule for this idea's cooldown/hard-block question above (aura-13, [[concepts/aura/risk-management]]).
- **The revenge-spiral mechanism** (aura-03, [[concepts/aura/mind-and-emotional-control]]): loss → frustration → an off-plan trade to "feel better" → that trade loses too → a third trade at bigger size, now trading P&L instead of the market → session-ending account damage. dOoMeR's stated intervention point is **before the second trade, not after the third** — "once the spiral starts, you will not think your way out of it." This is the strongest argument in the corpus for why this idea should lean hard-block/cooldown rather than notification-only: a notification arrives inside the spiral, where dOoMeR's own framing says willpower has already failed.
- Complementary circuit breakers cited alongside the above: a **two-loss stop** (stop trading for the session after two consecutive losses) and a **10-minute rule** (close charts for 10 minutes after any loss, no checking price) — both designed to physically remove the trader from the market before emotion compounds (aura-03, [[concepts/aura/mind-and-emotional-control]]).

## See Also

- [[concepts/roadmap/README]]
- [[concepts/roadmap/ideas/tradovate-integration]]
- [[concepts/roadmap/ideas/trader-psychology-profiler]]
- [[entities/projects/neurospect]] § *Moonshot Ideas* — Execution Guardian
