# Airline balance-sheet risk & valuation

Working capital, liquidity stress and trading multiples for four European carriers — Ryanair (`RYAAY`), Lufthansa (`LHA.DE`), Air France-KLM (`AF.PA`) and IAG (`IAG.L`) — built from filed annual statements in one reproducible notebook.

**📊 [Read the site → ecplol.github.io/Valuation-project](https://ecplol.github.io/Valuation-project/)**

Two questions: how long does each carrier survive a demand shock, and does the market charge for that survival?

| | |
|---|---|
| **Analysis** | [`main.ipynb`](main.ipynb) — fetch, normalise, compute, chart |
| **Data source** | Yahoo Finance normalised statements via `yfinance` |
| **Output** | 4 charts + 4 CSVs in [`output/`](output/) |
| **Site** | MkDocs Material, sources in [`docs/`](docs/) |

## What it does

1. **Working capital** — DSO, DPO, DIO and the cash conversion cycle over four fiscal years.
2. **Liquidity** — current, quick and cash ratios, and why only the last discriminates for an airline.
3. **Stress test** — months of cash under a sustained revenue shock, swept continuously, with the fixed/variable cost split stressed 45–65%.
4. **Composite ranking** — five metrics into one score, re-run under a second weighting to show how much the order actually holds.
5. **Valuation** — a lease-inclusive EV bridge and the trading multiples it feeds.
6. **Risk vs value** — the resilience score plotted against EV/EBITDA.

## Run it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab main.ipynb        # Kernel > Restart Kernel and Run All Cells
```

The notebook shares state across cells by design; dependent cells guard their inputs and name the fix, but restart-and-run-all is the supported path. Data is fetched live and Yahoo revises, so a fresh run will not reproduce the published figures exactly.

## Build the site

```bash
python3 -m venv .venv-docs && source .venv-docs/bin/activate
pip install -r requirements-docs.txt

./scripts/sync_outputs.sh     # copy output/ + main.ipynb into docs/
mkdocs serve                  # http://127.0.0.1:8000
mkdocs gh-deploy              # publish to the gh-pages branch
```

`sync_outputs.sh` copies notebook artefacts into `docs/`, which is the only tree MkDocs serves. Run it after every notebook run or the prose and the charts will drift apart.

## Disclaimer

Educational analysis of public filings, built to demonstrate financial-statement modelling in Python. Not investment advice, not a recommendation, and not tied back to the primary annual reports. See [Limitations](https://ecplol.github.io/Valuation-project/limitations/).
