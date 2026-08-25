# Enterprise value & multiples

<p class="lede">Everything up to here is balance-sheet risk: who survives a shock. It says nothing about what you pay for that survival. This page builds the price side.</p>

## The bridge

Enterprise value is the cost of the whole business, independent of how it is financed:

```text
EV = market cap + total debt + minority interest - cash
```

For airlines the debt line is the one that matters. Post-IFRS 16, aircraft operating leases sit on the balance sheet as lease liabilities and are included in total debt here. That is deliberate: **a leased aircraft is an aircraft**, and a carrier that leases its fleet is no cheaper than one that owns it just because the obligation has a different name.

| Ticker | FY end | Quote | Mkt cap | + Debt | *of which leases* | + Minority | − Cash | = EV |
|---|---|---|---|---|---|---|---|---|
| RYAAY | 2026-03-31 | USD | 25.2 | 1.5 | *0.1* | 0.0 | 3.5 | **23.1** |
| IAG.L | 2025-12-31 | GBP | 22.7 | 14.3 | *7.0* | 0.0 | 8.3 | **28.7** |
| LHA.DE | 2025-12-31 | EUR | 9.6 | 14.6 | *3.5* | 0.1 | 8.1 | **16.1** |
| AF.PA | 2025-12-31 | EUR | 3.2 | 15.4 | *10.8* | 2.1 | 6.0 | **14.6** |

*EUR bn. Market caps converted from the quote currency; all four report in EUR.*

The bridge is where the story is, before any multiple is computed. **Air France-KLM's equity is €3.2bn and its EV is €14.6bn** — the equity is a 22% sliver of the enterprise, and €10.8bn of the rest is lease obligations. **Ryanair is the mirror image**: €25.2bn of equity against €1.5bn of debt and €3.5bn of cash, so its EV is *below* its market cap. It is the only net-cash carrier in the group.

That difference alone explains most of what follows. Comparing these four on any equity multiple is comparing four different levels of financial risk.

## Trading multiples

| Ticker | EV/EBITDA | EV/EBIT | EV/Sales | P/E | Net debt/EBITDA | FCF yield | Implied upside |
|---|---|---|---|---|---|---|---|
| AF.PA | **2.5x** | 5.4x | 0.44x | 2.1x | 1.6x | 19.0% | +180% |
| LHA.DE | **3.2x** | 6.5x | 0.41x | 7.2x | 1.3x | -4.6% | +10% |
| IAG.L | **3.6x** | 5.4x | 0.86x | 6.8x | 0.8x | 13.9% | -7% |
| RYAAY | **6.0x** | 9.4x | 1.49x | 11.6x | **-0.5x** | 7.2% | -40% |

Peer median EV/EBITDA: **3.4x**.

### EV/EBITDA is the airline comp

Post-IFRS 16, rent has left operating expense and reappeared as lease depreciation and lease interest, both below EBITDA. Today's EBITDA is therefore already the old EBITDAR, and the hand-built lease-adjusted multiple analysts used pre-2019 is simply EV/EBITDA — *provided lease liabilities are inside EV*. They are, from the bridge above.

Ryanair trades at **1.9x the peer median** and 2.4x Air France-KLM. On EV/Sales the gap is wider still: 1.49x against 0.41–0.44x for the two legacy carriers. The market is not valuing these as the same kind of asset.

### P/E is carried but not leaned on

Air France-KLM's 2.1x P/E looks like the cheapest equity in Europe. It mostly measures the leverage in the bridge: a thin equity slice on a levered enterprise produces a small denominator and a violent multiple. The same leverage is why its EV/EBITDA of 2.5x is a much smaller discount than its P/E implies. **Read the enterprise multiples; treat the equity multiple as a leverage readout.**

### FCF yield

Free cash flow over market cap. Air France-KLM's 19.0% and IAG's 13.9% are high; Lufthansa's **-4.6%** is the number to note — it is the only carrier of the four not generating free cash flow, which is consistent with everything the [stress test](stress-test.md) found about its cash balance.

### Implied upside

Each carrier is re-rated to the peer median EV/EBITDA of 3.4x, and the bridge is unwound back to an equity value:

```text
implied equity = 3.4x × EBITDA - total debt - minority + cash
implied upside = implied equity / market cap - 1
```

!!! danger "This is a cross-check, not a price target"
    With n=4 the "peer median" is the average of the middle two names, and it moves if any one of them re-rates. Air France-KLM's +180% is arithmetic, not a forecast — the leverage that compresses its equity slice also amplifies every point of multiple expansion into a huge percentage on a small base. Treat the sign and the ordering as the signal, and the magnitude as noise.

    The honest reading: the market has priced Ryanair and IAG *above* the group's central multiple and Air France-KLM and Lufthansa below it. Whether that is a mispricing or a correct assessment of risk is exactly the question the [next page](risk-vs-value.md) asks.

## Data

- [`valuation_multiples.csv`](assets/valuation_multiples.csv) — every multiple on this page.
