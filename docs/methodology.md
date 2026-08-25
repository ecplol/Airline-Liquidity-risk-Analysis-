# Method & data

<p class="lede">Every number on this site comes from one notebook run against Yahoo Finance's normalised statement feed. This page records where the data comes from, how it is normalised, and every judgement call the model makes.</p>

## Universe

Four European carriers, chosen to span the low-cost / legacy divide while remaining comparable:

| Ticker | Carrier | Listing | Fiscal year end |
|---|---|---|---|
| `RYAAY` | Ryanair Holdings | Nasdaq ADR | 31 March |
| `LHA.DE` | Deutsche Lufthansa | Xetra | 31 December |
| `AF.PA` | Air France-KLM | Euronext Paris | 31 December |
| `IAG.L` | International Airlines Group | LSE | 31 December |

All four report in EUR. Market caps are converted from the quote currency (USD for the Ryanair ADR, GBP for IAG) so the EV bridge is internally consistent.

**Ryanair's March year-end is not aligned with the other three.** Its "FY2026" ends March 2026 and covers a different twelve months than the December filers' FY2025. For a seasonal business this matters — a March year-end lands at the winter cash trough, a December year-end does not. Every cross-sectional comparison on this site carries that mismatch.

## Source

`yfinance`, annual frequency:

- Balance sheet — `Ticker.balance_sheet`
- Income statement — `Ticker.financials`
- Market data — `Ticker.info` / `Ticker.fast_info`

Four fiscal years are available per carrier, giving 16 carrier-years.

### Label normalisation

Filers label the same line differently, and Yahoo's normalisation is not complete. Each concept is resolved against a candidate list, first match wins:

| Concept | Candidate labels |
|---|---|
| Receivables | `Accounts Receivable`, `Receivables`, `Net Receivables` |
| Payables | `Accounts Payable`, `Payables`, `Payables And Accrued Expenses` |
| Inventory | `Inventory`, `Inventories` |
| Current assets | `Current Assets`, `Total Current Assets` |
| Current liabilities | `Current Liabilities`, `Total Current Liabilities` |
| Cash | `Cash And Cash Equivalents`, `Cash Cash Equivalents And Short Term Investments` |
| Revenue | `Total Revenue`, `Revenue` |
| COGS | `Cost Of Revenue`, `Reconciled Cost Of Revenue`, `Cost Of Goods Sold` |

A missing or `NaN` cell resolves to `None` rather than zero, and every downstream ratio is guarded: division returns `None` unless both sides exist and the denominator is non-zero. Nothing on this site is a zero that was really a gap.

A fetch failure on one ticker is reported and skipped rather than killing the run.

## Definitions

### Working capital

```text
DSO = receivables / revenue  × 365
DPO = payables    / COGS     × 365
DIO = inventory   / COGS     × 365
CCC = DSO + DIO - DPO
```

Flow items are per-period, so the day count must match the period. The notebook carries a `DAYS_IN_PERIOD` map (365 annual, 91 quarterly) precisely because using 365 against quarterly flows inflates all three by roughly 4x. This site uses annual throughout.

### Liquidity

```text
Current ratio = current assets                / current liabilities
Quick ratio   = (current assets - inventory)  / current liabilities
Cash ratio    = cash                          / current liabilities
```

### Stress test

Revenue falls by a shock `s` and stays there; variable cost falls with it, fixed cost does not.

```text
fixed        = (COGS / 12) × (1 - variable_share)
variable     = (COGS / 12) × variable_share × (1 - s)
monthly burn = fixed + variable - (revenue / 12) × (1 - s)

months of liquidity = cash / monthly burn        (infinite if burn ≤ 0)
breakeven shock     = 1 - fixed / (revenue/12 - (COGS/12) × variable_share)
```

`variable_share` defaults to **0.55** and is swept across `[0.45, 0.55, 0.65]`. Only cash counts as the buffer — receivables shrink alongside revenue in a demand shock rather than cushioning it, and undrawn credit lines are not in these statements at all.

### Composite score

Each metric is min-max rescaled across the four carriers to 0–100 (0 = worst of the group, 100 = best), sign-corrected so higher is always better, then weighted 30/25/20/15/10 across breakeven shock, months at -40%, CCC, cash ratio and current ratio. Infinite runways are capped at a `DISPLAY_CAP` before scaling so one carrier's "no burn" does not compress everyone else to zero.

### Valuation

```text
EV             = market cap + total debt + minority interest - cash
net debt       = total debt - cash
implied equity = peer median EV/EBITDA × EBITDA - total debt - minority + cash
implied upside = implied equity / market cap - 1
FCF yield      = free cash flow / market cap
```

Total debt includes IFRS 16 lease liabilities.

## Judgement calls

Everything below is a choice, not a disclosure. Each is stressed where the notebook can stress it.

| Call | Value | Stressed? |
|---|---|---|
| Variable / fixed cost split | 55 / 45 | Yes — 45%, 55%, 65% |
| Composite weights | 30/25/20/15/10 | Yes — vs flat 20% each |
| Cost base for burn | Cost of revenue only | No |
| Buffer in a shock | Cash only, no revolver | No — deliberately harsh |
| Leases in EV | Included | No |
| Peer median | Median of these four | No |
| Currency | EUR, reporting currency | No |

## Reproducibility

The notebook is deterministic given the same statement data, but the *data itself is not pinned* — Yahoo revises and backfills, and a rerun on a later date will produce different numbers than the ones on this site. See [Reproduce it](reproduce.md) for how to run it, and [Limitations](limitations.md) for what that means.
