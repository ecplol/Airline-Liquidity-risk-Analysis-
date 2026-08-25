# Using this inside a company

<p class="lede">The same eight line items that produce this comparison sit in your own ledger, usually a lot fresher than the annual filing this site reads. This page is how to benchmark against the four carriers here, and how to turn the stress test into a treasury KPI.</p>

## The eight inputs

Every metric on this site is derived from these, per period. Nothing else is needed:

| Input | Statement | Feeds |
|---|---|---|
| Receivables | Balance sheet | DSO, CCC |
| Payables | Balance sheet | DPO, CCC |
| Inventory | Balance sheet | DIO, CCC, quick ratio |
| Current assets | Balance sheet | Current ratio, quick ratio |
| Current liabilities | Balance sheet | All three liquidity ratios |
| Cash & equivalents | Balance sheet | Cash ratio, stress buffer |
| Revenue | Income statement | DSO, stress test |
| Cost of revenue | Income statement | DPO, DIO, stress test |

Two more — EBITDA and total debt including leases — are needed only for the [valuation half](valuation.md).

The formulas are on the [method page](methodology.md). They are deliberately plain: no adjustments, no normalisation, no add-backs. That is what makes the comparison hold.

!!! tip "Use your management accounts, not the filing"
    This site is stuck with annual data because that is what the public feed carries. You are not. The same eight lines monthly turn the [breakeven shock](#the-metric-worth-adopting) from an annual curiosity into a live indicator. If you run it quarterly, change `FREQ` to `"quarterly"` in the notebook — the day-count adjusts automatically, and using 365 against quarterly flows would otherwise inflate DSO, DPO and DIO roughly fourfold.

## Benchmark table

Where you sit against these four, latest fiscal year:

| Metric | Worst | Median | Best | Spread |
|---|---|---|---|---|
| DSO (days) | 24.5 | 18.5 | 1.0 | 24.5x |
| DPO (days) | 18.5 | 41.2 | 46.1 | 2.5x |
| DIO (days) | 17.3 | 12.4 | 0.1 | — |
| Cash conversion cycle | -0.7 | -12.0 | -17.6 | 25 days |
| Current ratio | 0.62 | 0.76 | 0.90 | 0.28 |
| Quick ratio | 0.56 | 0.70 | 0.90 | 0.34 |
| Cash ratio | 0.06 | 0.30 | 0.40 | 6.6x |
| Breakeven shock | -24% | -40% | -43% | 19pp |
| Net debt/EBITDA | 1.6x | 1.0x | -0.5x | 2.1x |
| FCF yield | -4.6% | 10.5% | 19.1% | 23.7pp |

The DSO column is the one to read carefully before benchmarking against it. The 1-day to 24.5-day spread is a **business model difference**, not a collections performance difference: direct-to-consumer card-on-file against agency, corporate and IATA interline settlement. Benchmark DSO against carriers with your distribution mix, or you will set a target nobody in your channel can hit.

DPO is the fairer efficiency comparison, and the fact that it fell at all four over the window suggests supplier-side pressure rather than four independent policy choices.

## The metric worth adopting

Most treasury dashboards carry "months of liquidity" against a named scenario. The problem is that the number is only as good as the scenario, and the scenario is usually chosen after the fact.

**Breakeven shock inverts it.** Instead of asking "how long do we last in a -40% world", it asks "how deep a decline do we absorb before we burn anything at all":

```text
breakeven shock = 1 - fixed cost / (revenue - variable cost)
```

Three properties make it a better board metric:

1. **Scenario-free.** It is a property of your cost structure, not of a forecast someone picked.
2. **Directly actionable.** It moves when you move fixed cost, contribution margin or the variable share — all things management controls, unlike a demand scenario.
3. **Comparable.** It puts a €1bn carrier and a €30bn carrier on the same axis. Months of cash does not.

Pair it with months of liquidity rather than replacing it. Breakeven tells you when the bleeding starts; months tells you how long you have once it does. Lufthansa is the case for carrying both: its -24% breakeven is the alarm, and the 4.3 months behind it is the response window.

!!! warning "Calibrate the cost split before you trust the number"
    Everything here assumes 55% of cost of revenue is variable. **You know your actual split and this site does not.** Substitute it — the [sensitivity analysis](stress-test.md#sensitivity-to-the-cost-split) shows a 45–65% range moving one carrier's runway by 2.5x. Also note this model uses cost of revenue only; if your SG&A is material, include it as fixed and your breakeven will be shallower than the numbers on this site.

!!! tip "Do it with your own numbers"
    The [ratio calculator](scenario-lab.md#3-ratio-calculator) takes these eight inputs and benchmarks the result against the four carriers, and the [stress lab](scenario-lab.md#1-stress-lab) takes your revenue, cost and cash. Everything runs in your browser — nothing is uploaded.

## Setting internal thresholds

A workable early-warning ladder, built from your own breakeven shock `B`:

| Level | Condition | Response |
|---|---|---|
| Green | Demand within 50% of `B` | Normal operation |
| Amber | Demand decline reaches 50% of `B` | Review discretionary capex; confirm facility headroom |
| Red | Demand decline reaches 75% of `B` | Draw plans activated; fixed-cost reduction begins |
| Burn | Decline exceeds `B` | Months of liquidity becomes the governing metric |

The percentages are illustrative — the point is anchoring the ladder to a cost-structure fact rather than to round-number scenarios. A carrier with a -43% breakeven and one with a -24% breakeven should not share a trigger table.

Two more worth wiring in, both drawn from what this analysis found across the four:

- **DPO falling more than 10 days year on year.** Suppliers reprice risk before markets do. All four carriers here saw payable days fall, Ryanair by 27 days.
- **Cash conversion cycle approaching zero.** For a prepaid business model, crossing into positive territory means the customer float that funds operations has gone. Air France-KLM sits at -0.7 days and crossed to +0.9 in FY2023.

## Benchmarking your own carrier

If your company is listed, add the ticker and the whole comparison rebuilds:

```python
TICKERS = ["RYAAY", "LHA.DE", "AF.PA", "IAG.L", "YOUR.TICKER"]
```

Add a colour to `SERIES_COLORS` so it gets a distinct line — unmapped tickers fall back to grey. Because scores are min-max scaled across the group, adding a fifth name **rescales everyone**: a score of 0 means worst of five, not distressed.

If you are not listed, the notebook's calculation functions take plain numbers. `calculate_ratios`, `monthly_burn`, `months_of_liquidity` and `breakeven_shock` have no dependency on the data feed — feed them your own revenue, cost of revenue and cash and the outputs are directly comparable to the tables on this site.

See [Reproduce it](reproduce.md) for setup.
