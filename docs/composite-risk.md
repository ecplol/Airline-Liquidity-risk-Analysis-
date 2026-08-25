# Composite risk ranking

<p class="lede">The three views so far disagree about who is fragile. This collapses them into one score — and then tries hard to break it.</p>

## Why a composite

The cash cycle, the liquidity ratios and the stress test each rank the four carriers differently. Lufthansa has the second-best current ratio and the worst cash ratio. Air France-KLM has the worst current ratio and the second-best breakeven shock. Ryanair has the best current ratio and a mid-pack cash ratio.

A composite forces the trade-off to be explicit rather than resolved by whichever chart you looked at last.

## Construction

Five metrics, each rescaled 0–100 across the four carriers (0 = worst of this group, 100 = best), then weighted:

| Metric | Weight | Rationale |
|---|---|---|
| Breakeven shock | 30% | How deep a decline is absorbed before burning at all — the single most informative number |
| Months at -40% | 25% | Runway once burning has started |
| CCC | 20% | Structural supplier funding |
| Cash ratio | 15% | Money against near-term obligations |
| Current ratio | 10% | Weakest signal here (see [Liquidity](liquidity.md)), kept for completeness |

!!! note "The scale is relative, not absolute"
    A score of 100 means "best of these four", not "safe". A score of 0 means "worst of these four", not "distressed". Adding a fifth carrier would move every number on this page.

## Result

| Ticker | Rank | Score | Cash ratio | Current ratio | CCC | Breakeven | -40% |
|---|---|---|---|---|---|---|---|
| IAG.L | <span class="rank">1</span> | **92.9** | 0.40 | 0.70 | -17.6d | -43% | no burn |
| RYAAY | <span class="rank">2</span> | **90.7** | 0.32 | 0.90 | -17.4d | -39% | >36 mo |
| AF.PA | <span class="rank">3</span> | **62.2** | 0.28 | 0.62 | -0.7d | -41% | no burn |
| LHA.DE | <span class="rank">4</span> | **13.8** | 0.06 | 0.81 | -6.6d | -24% | 4.3 mo |

Component scores, 0 = worst of the four on that metric:

| Ticker | Cash ratio | Current ratio | CCC | Breakeven | -40% |
|---|---|---|---|---|---|
| IAG.L | 100.0 | 28.6 | 100.0 | 100.0 | 100.0 |
| RYAAY | 76.5 | 100.0 | 98.8 | 81.5 | 100.0 |
| AF.PA | 64.7 | 0.0 | 0.0 | 91.6 | 100.0 |
| LHA.DE | 0.0 | 67.9 | 34.9 | 0.0 | 0.0 |

The shape of the table is the finding. **IAG is best or near-best on four of five metrics** and only stumbles on the ratio that carries the least information. **Lufthansa is worst on three of five, including both stress metrics**, and its one good score is on that same low-information ratio.

Air France-KLM's 62.2 is a genuinely mixed picture rather than a middling one: it ties the leaders on the -40% scenario and on breakeven, and scores zero on both the current ratio and the cash cycle.

## Stress test 1 — the cost-split assumption

Re-ranking at 45%, 55% and 65% variable cost:

```text
  45% variable: IAG.L > RYAAY > AF.PA > LHA.DE
  55% variable: IAG.L > RYAAY > AF.PA > LHA.DE
  65% variable: IAG.L > RYAAY > AF.PA > LHA.DE
```

The order is unchanged across the range. The ranking is **not** an artefact of the 55% split.

## Stress test 2 — the weights

!!! tip "Move the weights yourself"
    The [Scenario lab](scenario-lab.md#2-weight-lab) re-ranks live as you drag each weight. The component scores stay fixed, so what you are changing is the opinion, not the evidence.

The weights are a judgement call, so re-rank at a flat 20% each:

| Ticker | Judgement score | Rank | Equal score | Rank |
|---|---|---|---|---|
| IAG.L | 92.9 | 1 | 85.7 | **2** |
| RYAAY | 90.7 | 2 | 91.4 | **1** |
| AF.PA | 62.2 | 3 | 51.3 | 3 |
| LHA.DE | 13.8 | 4 | 20.6 | 4 |

**The top two swap.** Where the weighted contribution moved (equal minus judgement):

| Ticker | Cash ratio | Current ratio | CCC | Breakeven | -40% | Net |
|---|---|---|---|---|---|---|
| IAG.L | +5.0 | +2.9 | 0.0 | **-10.0** | -5.0 | **-7.1** |
| RYAAY | +3.8 | **+10.0** | 0.0 | -8.1 | -5.0 | **+0.7** |

Flattening the weights takes 10 points off IAG's contribution from the breakeven shock — the metric it leads — and hands Ryanair 10 points on the current ratio, the metric it leads and the one with the least economic content. The swap is entirely mechanical, and it happens because IAG and Ryanair were 2.2 points apart to begin with.

!!! success "How to read this"
    **The bottom of the table is a verdict.** Lufthansa ranks fourth under every weighting and every cost-split assumption tested, and it is 48 points clear of third place. That is robust.

    **The top of the table is a tie.** IAG and Ryanair separate by 2.2 points under one weighting and swap under another. Any claim that one is *the* most resilient of these four is a claim about the weights, not about the carriers.

## Data

- [`composite_risk.csv`](assets/composite_risk.csv) — inputs, score and rank per carrier.
