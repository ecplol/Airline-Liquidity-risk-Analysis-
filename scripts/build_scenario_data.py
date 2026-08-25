#!/usr/bin/env python3
"""Build docs/assets/scenario-data.json for the interactive Scenario lab.

The lab needs the raw per-carrier inputs (revenue, cost of revenue, cash, and
the EV bridge), but the notebook only exports ratios. Rather than ask for a
notebook change and a re-fetch - which would move every number on the site -
this recovers the inputs from what is already exported.

Revenue and cost of revenue come out of the stress-test CSV exactly. With
v = variable share, monthly r and c, the notebook's model is:

    breakeven   s* = 1 - (1-v)c / (r - vc)
    burn(s)        = (1-v)c + vc(1-s) - r(1-s)

The first equation fixes c/r from s* alone; substituting into the second at
s = 0.70 and dividing cash by the published runway fixes r. Both are inverted
in closed form below, and `--verify` round-trips them back through the forward
model and asserts they reproduce the published CSV.

The EV bridge has no CSV, so it is parsed from the notebook's stored stdout.

Run via scripts/sync_outputs.sh, or directly:

    python3 scripts/build_scenario_data.py --verify
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
DEST = ROOT / "docs" / "assets" / "scenario-data.json"

VARIABLE_SHARE = 0.55   # notebook VARIABLE_COST_SHARE
DISPLAY_CAP = 36        # notebook DISPLAY_CAP, months

# notebook RISK_METRICS: metric -> (direction, weight)
RISK_METRICS = {
    "Cash Ratio":      ("higher", 0.15),
    "Current Ratio":   ("higher", 0.10),
    "CCC":             ("lower",  0.20),
    "Breakeven shock": ("higher", 0.30),
    "Severe -40%":     ("higher", 0.25),
}

NAMES = {
    "RYAAY": "Ryanair",
    "LHA.DE": "Lufthansa",
    "AF.PA": "Air France-KLM",
    "IAG.L": "IAG",
}
# pinned in the notebook's SERIES_COLORS so the lab matches the static charts
COLORS = {
    "RYAAY": "#2a78d6",
    "LHA.DE": "#008300",
    "AF.PA": "#e87ba4",
    "IAG.L": "#eda100",
}


def _num(x):
    """Float, or None for blanks and the inf sentinel pandas writes."""
    if x is None:
        return None
    x = str(x).strip()
    if not x or x.lower() in {"inf", "nan", ""}:
        return None
    try:
        return float(x)
    except ValueError:
        return None


def read_csv(name):
    with (OUTPUT / name).open() as fh:
        return list(csv.DictReader(fh))


# --- forward model, mirroring the notebook -------------------------------

def monthly_burn(revenue, cogs, shock, v=VARIABLE_SHARE):
    r, c = revenue / 12, cogs / 12
    return c * (1 - v) + c * v * (1 - shock) - r * (1 - shock)


def breakeven_shock(revenue, cogs, v=VARIABLE_SHARE):
    r, c = revenue / 12, cogs / 12
    contribution = r - c * v
    if contribution <= 0:
        return None
    return 1 - c * (1 - v) / contribution


def months_of_liquidity(revenue, cogs, cash, shock, v=VARIABLE_SHARE):
    burn = monthly_burn(revenue, cogs, shock, v)
    return None if burn <= 0 else cash / burn


# --- inversion -----------------------------------------------------------

def recover_inputs(cash, breakeven, months_at_70, v=VARIABLE_SHARE):
    """Annual revenue and cost of revenue implied by the published stress row."""
    one_minus_s = 1 - breakeven
    k = one_minus_s / ((1 - v) + v * one_minus_s)          # cogs / revenue
    burn_factor = k * ((1 - v) + v * 0.30) - 0.30          # burn at -70%, per unit monthly revenue
    if burn_factor <= 0:
        raise ValueError("carrier does not burn at -70%; cannot invert")
    monthly_revenue = cash / (months_at_70 * burn_factor)
    return monthly_revenue * 12, k * monthly_revenue * 12


# --- EV bridge -----------------------------------------------------------

BRIDGE_ROW = re.compile(
    r"^(?P<ticker>\S+)\s+(?P<fy>\d{4}-\d{2}-\d{2})\s+(?P<quote>[A-Z]{3})\s+"
    r"(?P<mktcap>-?[\d.]+)\s+(?P<debt>-?[\d.]+)\s+(?P<leases>-?[\d.]+)\s+"
    r"(?P<minority>-?[\d.]+)\s+(?P<cash>-?[\d.]+)\s+(?P<ev>-?[\d.]+)\s*$"
)


def parse_bridge(notebook: Path):
    """Pull the EV bridge out of the notebook's stored stdout."""
    nb = json.loads(notebook.read_text())
    bridge = {}
    for cell in nb.get("cells", []):
        for out in cell.get("outputs", []):
            if out.get("output_type") != "stream":
                continue
            text = "".join(out.get("text", []))
            if "Enterprise value bridge" not in text:
                continue
            for line in text.splitlines():
                m = BRIDGE_ROW.match(line.strip())
                if m:
                    d = m.groupdict()
                    bridge[d["ticker"]] = {
                        "fy": d["fy"],
                        "quote": d["quote"],
                        "mktcap": float(d["mktcap"]),
                        "debt": float(d["debt"]),
                        "leases": float(d["leases"]),
                        "minority": float(d["minority"]),
                        "cash": float(d["cash"]),
                        "ev": float(d["ev"]),
                    }
    return bridge


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="round-trip recovered inputs through the forward model")
    args = ap.parse_args()

    stress = {r["ticker"]: r for r in read_csv("stress_test.csv")}
    multiples = {r["ticker"]: r for r in read_csv("valuation_multiples.csv")}
    composite = {r["ticker"]: r for r in read_csv("composite_risk.csv")}
    bridge = parse_bridge(ROOT / "main.ipynb")

    # latest period per ticker
    wc_latest = {}
    for row in read_csv("working_capital_ratios.csv"):
        t = row["ticker"]
        if t not in wc_latest or row["period"] > wc_latest[t]["period"]:
            wc_latest[t] = row

    carriers = {}
    for ticker, srow in stress.items():
        cash = float(srow["Cash (bn)"]) * 1e9
        be = float(srow["Breakeven shock"])
        m70 = float(srow["COVID-like -70%"])
        revenue, cogs = recover_inputs(cash, be, m70)

        if args.verify:
            got_be = breakeven_shock(revenue, cogs)
            got_m70 = months_of_liquidity(revenue, cogs, cash, 0.70)
            assert abs(got_be - be) < 1e-9, f"{ticker} breakeven {got_be} != {be}"
            assert abs(got_m70 - m70) < 1e-6, f"{ticker} m70 {got_m70} != {m70}"
            pub40 = _num(srow["Severe -40%"])
            got40 = months_of_liquidity(revenue, cogs, cash, 0.40)
            if pub40 is None:
                assert got40 is None, f"{ticker} expected no burn at -40%"
            else:
                assert abs(got40 - pub40) < 1e-3, f"{ticker} m40 {got40} != {pub40}"

        wc = wc_latest.get(ticker, {})
        mult = multiples.get(ticker, {})
        br = bridge.get(ticker, {})

        # The bridge is printed to one decimal, so re-adding the components does
        # not always land back on the printed EV (Air France-KLM: 14.7 vs 14.6).
        # The lab recomputes EV from the inputs a user can edit, so derive EBITDA
        # from that same recomputed figure - otherwise the lab would show a
        # multiple that contradicts the published table by a tenth of a turn.
        ev_printed = br.get("ev")
        ev = None
        if all(br.get(k) is not None for k in ("mktcap", "debt", "minority", "cash")):
            ev = br["mktcap"] + br["debt"] + br["minority"] - br["cash"]
        elif ev_printed is not None:
            ev = ev_printed
        ev_mult = _num(mult.get("EV/EBITDA"))
        ebitda = ev / ev_mult if (ev is not None and ev_mult) else None

        carriers[ticker] = {
            "name": NAMES.get(ticker, ticker),
            "color": COLORS.get(ticker, "#898781"),
            "fy": br.get("fy") or wc.get("period"),
            # stress inputs, EUR
            "revenue": revenue,
            "cogs": cogs,
            "cash": cash,
            # working capital, latest FY
            "dso": _num(wc.get("DSO")), "dpo": _num(wc.get("DPO")),
            "dio": _num(wc.get("DIO")), "ccc": _num(wc.get("CCC")),
            "current": _num(wc.get("Current Ratio")),
            "quick": _num(wc.get("Quick Ratio")),
            "cashRatio": _num(wc.get("Cash Ratio")),
            # composite raw inputs (Severe -40% is None where the carrier never burns)
            "severe40": _num(composite.get(ticker, {}).get("Severe -40%")),
            "publishedScore": _num(composite.get(ticker, {}).get("Score")),
            # EV bridge, EUR bn as printed
            "mktcap": br.get("mktcap"), "debt": br.get("debt"),
            "leases": br.get("leases"), "minority": br.get("minority"),
            "bridgeCash": br.get("cash"), "ev": ev, "ebitda": ebitda,
        }

    payload = {
        "variableShare": VARIABLE_SHARE,
        "displayCap": DISPLAY_CAP,
        "weights": {m: w for m, (_, w) in RISK_METRICS.items()},
        "directions": {m: d for m, (d, _) in RISK_METRICS.items()},
        "order": ["RYAAY", "LHA.DE", "AF.PA", "IAG.L"],
        "carriers": carriers,
    }

    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {DEST.relative_to(ROOT)} ({len(carriers)} carriers)"
          + (" - round-trip verified" if args.verify else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
