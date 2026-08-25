# Using this as an investor

<p class="lede">This is a screen, not a recommendation. It answers one narrow question well — how much demand shock does this balance sheet absorb, and what is the market charging for that — and hands you a shortlist and a set of questions. Everything that decides an actual investment case sits outside it.</p>

!!! danger "Read this first"
    Nothing on this site is investment advice or a recommendation to buy or sell any security. The figures come from a third-party normalised data feed, have not been tied back to the audited accounts, and are a snapshot of one notebook run. See [Limitations](limitations.md) in full before acting on anything here.

## What the screen is good for

**Sizing downside, not forecasting upside.** The [stress test](stress-test.md) asks how deep a revenue decline a carrier absorbs before it burns cash at all. That is a floor-finding exercise. It says nothing about margin trajectory, capacity discipline or fare environment — the things that actually drive returns in a good year.

**Making a levered comparison honest.** These four sit between net cash and 1.6x net debt/EBITDA, and lease liabilities range from €0.1bn to €10.8bn. Any equity multiple across that spread is mostly measuring leverage. The [EV bridge](valuation.md) is the part of this site most worth reusing on other names.

**Separating a cheap multiple from a cheap asset.** Air France-KLM's 2.1x P/E and Lufthansa's 3.2x EV/EBITDA both look cheap. The composite says one of those discounts is better earned than the other.

## What it cannot do

| Not modelled | Why it matters |
|---|---|
| Undrawn revolvers, sale-and-leaseback capacity, state support | Decisive in 2020, and the carrier that scores worst here had the best access |
| Management response — grounding fleet, deferring capex, furloughs | Converts fixed cost to variable; the model holds fixed cost flat |
| Refunds on the forward book | A demand collapse turns deferred revenue into cash *out*; every runway here would shorten |
| Fuel and FX hedging | Can dominate a single year's cost base |
| Fleet age, order book, slots, network quality | The actual competitive position |
| Pensions, labour agreements, emissions cost trajectory | Large, carrier-specific, and entirely absent here |

A credit view or an equity case needs most of that list. This is a balance-sheet exercise that tells you where to spend your reading time.

## Monitoring triggers

If you already hold or follow these names, these are the lines worth re-checking each reporting period. The thresholds are calibrated to *this group of four* and are starting points for your own judgement, not standards.

| Trigger | Threshold | Why | Currently |
|---|---|---|---|
| Cash ratio | below **0.15** | The ratio that discriminates; the peer median is 0.30 | LHA.DE at 0.06 |
| Breakeven shock | shallower than **-30%** | Below this the carrier burns in an ordinary recession, not a crisis | LHA.DE at -24% |
| Cash conversion cycle | crossing **0** | The supplier float is gone exactly when it is most needed | AF.PA at -0.7, crossed once in FY2023 |
| FCF yield | **negative** | Cash balance is being consumed, not rebuilt | LHA.DE at -4.6% |
| Net debt/EBITDA | above **2.0x** | None of the four is there; the group tops out at 1.6x | — |
| DPO | falling **>10 days** year on year | Suppliers withdrawing terms is an early credit signal | RYAAY fell 27 days over four years |

The DPO trigger is the least obvious and possibly the most useful. Payables terms tighten before anything shows up in a ratio, because suppliers reprice risk faster than markets do.

## Questions this analysis hands to IR

The model's biggest gaps are all disclosable. If you can get answers to these, you can replace the assumptions with facts:

1. **What is the fixed/variable cost split?** This site assumes 55/45 and it is the [single largest lever](stress-test.md#sensitivity-to-the-cost-split). Carriers rarely disclose it; many will discuss it.
2. **How much undrawn committed liquidity is there, and what are the covenants?** This turns a cash-only floor into a realistic one.
3. **What is the size and duration of the forward book?** It sets the refund exposure the model omits.
4. **What is the lease maturity profile?** EV treats a €10.8bn lease book as debt; the repayment shape decides whether that is fair.
5. **What share of revenue is direct versus agency?** It explains the DSO spread — 1 day at Ryanair against 24.5 at Air France-KLM — and how durable it is.
6. **What drove the fall in payable days?** Supplier terms, a mix shift, or a deliberate working-capital choice are three very different stories.

## Reading the quadrants

The [risk vs value](risk-vs-value.md) chart splits on peer medians. What each quadrant means in practice:

- **Resilient and cheap** — the cell worth hunting. *Empty here.* If a name lands there, the first job is finding what the screen is missing, not buying it.
- **Resilient and expensive** — you are paying for the balance sheet. Fine, if the premium is proportionate. The question becomes whether resilience is what you want to own at that price.
- **Fragile and cheap** — the discount may be earned. Distinguish "cheap because levered" from "cheap because impaired" using the EV multiples, not the P/E.
- **Fragile and expensive** — the cell to be sceptical of. Nothing is here, though Lufthansa is the closest thing to it: fourth on the composite by 48 points, trading above the carrier ranked third.

!!! warning "The x-axis is soft at the top"
    IAG and Ryanair separate by 2.2 composite points and [swap under equal weights](composite-risk.md#stress-test-2-the-weights). Their order relative to each other is not stable; their position relative to the other two is. Do not build a pairwise view on a 2.2-point gap.

## Running it on your own universe

The screen is four tickers because that is a comparable set, not because four is enough. To point it elsewhere, change one line in the notebook:

```python
TICKERS = ["RYAAY", "LHA.DE", "AF.PA", "IAG.L"]
```

Two things to hold onto:

- **Every score is scaled within the group.** 100 means "best of these", never "safe". Change the list and every number changes — including the peer median that drives implied upside.
- **Keep fiscal year ends comparable where you can.** Ryanair's March year-end already introduces a seasonal mismatch against three December filers, and that flows into the cash ratio, the stress buffer and the composite.

Full instructions on [Reproduce it](reproduce.md).
