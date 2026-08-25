# Is resilience priced?

<p class="lede">The two halves of the analysis finally meet. The composite score ranks these carriers by how well they survive a demand shock; EV/EBITDA says what the market charges for them. Plotting one against the other asks whether you are paying for the resilience the first half measured.</p>

<figure markdown>
  ![Composite resilience score on the x-axis against EV/EBITDA on the y-axis, split into quadrants on the peer medians](assets/risk_vs_value.png)
  <figcaption>Quadrants split on the peer medians: 3.4x EV/EBITDA and a composite score of 76.</figcaption>
</figure>

## The answer is yes

Spearman rank correlation between composite score and EV/EBITDA: **+0.60** (n=4).

!!! warning "What n=4 can and cannot support"
    At four observations this correlation cannot be significant at any conventional threshold — the smallest achievable p-value with n=4 is above 0.05 whatever the data does. It is here to name the direction, not to test it. Four carriers is a description of these four carriers, not a finding about the airline sector.

With that caveat, the direction is unambiguous and it is confirmed by the quadrants, which don't depend on the correlation statistic at all:

| Quadrant | Carriers |
|---|---|
| Resilient, cheap | *— empty —* |
| Resilient, expensive | IAG.L, RYAAY |
| Fragile, cheap | AF.PA, LHA.DE |
| Fragile, expensive | *— empty —* |

**Both off-diagonal quadrants are empty.** The two carriers that survive the deepest shocks are the two the market charges most for; the two that don't are the two it discounts. There is no free resilience on offer here, and no carrier being charged a premium it hasn't earned.

## What that means for each name

**Ryanair (score 90.7, 6.1x)** — the most expensive carrier in the group and, on the equal-weighted composite, the most resilient. Net cash, a 1-day collection cycle and a -39% breakeven. The premium is defensible on the balance sheet; whether 1.9x the peer median is the *right* premium is a judgement this analysis does not attempt.

**IAG (score 92.9, 3.6x)** — the most interesting position on the chart. It ranks first on the judgement-weighted composite and is best or near-best on four of five component metrics, yet it trades only slightly above the peer median and at 60% of Ryanair's multiple. If anything on this chart approaches the empty resilient-and-cheap quadrant, it is IAG.

**Air France-KLM (score 62.2, 2.4x)** — cheap on every enterprise multiple, and the composite says the discount is not baseless: a cash cycle that has gone to zero and the worst current ratio in the group. But it also ties the leaders on both stress metrics. The thin equity slice on a €14.6bn enterprise means the multiple is doing double duty as a leverage signal.

**Lufthansa (score 13.8, 3.2x)** — the position that does *not* fit the pattern. It scores 48 points below third place, is the only carrier that breaks at a -24% shock, and is the only one with negative free cash flow — yet it trades *above* Air France-KLM on EV/EBITDA and close to IAG. The correlation is positive overall, but this is the point where the market is charging least like the balance sheet suggests it should.

## Reading the chart honestly

Three things constrain how far this goes:

1. **The x-axis is soft at the top.** IAG and Ryanair separate by 2.2 composite points and [swap under equal weights](composite-risk.md#stress-test-2-the-weights). Their horizontal order on this chart is not stable; their position relative to the other two is.
2. **The y-axis is a snapshot.** One multiple, at one date, on one fiscal year's EBITDA — three of which end in December and one in March. A cyclical sector at a cyclical point.
3. **Correlation is not causation, and here it isn't even inference.** A market that prices resilience correctly and a market that happens to like the same carriers for unrelated reasons — network quality, margin trajectory, ownership structure — produce the same scatter at n=4.

What survives all three: **there is no cheap resilience in this group of four.** If you want the balance sheet, you pay for it.
