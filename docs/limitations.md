# Limitations

<p class="lede">What this analysis cannot tell you, stated plainly. Read this before quoting any number from the other pages.</p>

## The data is not the accounts

Everything here comes from Yahoo Finance's normalised statement feed, **not from the audited annual reports**. No figure on this site has been tied back to a primary filing. Yahoo's normalisation folds different filers' line items into common labels, and it does so imperfectly and silently. Where a line is missing entirely the model returns `None` rather than guessing — but where it is misclassified, nothing here would catch it.

The data is also **not pinned**. Yahoo revises and backfills; a rerun on a later date will produce different numbers from the ones published here. The site is a snapshot of one run.

## Four observations

Every statistic here is computed across four carriers.

- The "peer median" EV/EBITDA is the average of the middle two names. It moves if any one of them re-rates.
- The composite score is min-max scaled *within the group*: 100 means "best of these four", never "safe"; 0 means "worst of these four", never "distressed". Adding a fifth carrier changes every score on the site.
- The Spearman correlation on the [risk vs value](risk-vs-value.md) page cannot reach conventional significance at n=4 whatever the data does. It names a direction; it tests nothing.

## Non-comparable periods

Ryanair's fiscal year ends 31 March; the other three end 31 December. For a business with a summer revenue peak and a winter cash trough, the year-end balance sheet is taken at a materially different point in the cycle. This affects the cash ratio, the stress test's cash buffer and the composite score that consumes both — in Ryanair's case, conservatively.

## The stress test is a floor, not a forecast

The model deliberately excludes everything a real carrier would do:

- **No external liquidity.** Undrawn revolvers, sale-and-leaseback capacity, state support. In 2020 those were decisive, and the carrier that looks weakest here had the best access to them.
- **No management response.** Grounding fleet, deferring capex and furloughing crew all convert fixed cost to variable. Fixed cost is held flat.
- **No working-capital unwind.** A demand collapse means refunding tickets already sold. That outflow is not modelled and would make every runway shorter — most of all for carriers with the largest forward book.
- **Cost of revenue only.** Operating expense below the COGS line is not in the burn, which flatters every carrier and flatters the legacy carriers most.

The 55/45 variable/fixed split is the dominant input and is not observable. It is swept 45–65% on the [stress test page](stress-test.md); for three carriers the conclusion is unchanged across the range, for Lufthansa the runway moves 2.5x.

## The composite is a construction

Five metrics, one weighting, one ranking. The [weights are stressed](composite-risk.md#stress-test-2-the-weights) and the top two positions swap under a flat weighting — which is itself the finding. But the choice of *which five metrics*, and the decision to include a current ratio that the [liquidity page](liquidity.md) argues carries little information for airlines, are unstressed.

## What is not modelled at all

Fleet age and order book · route network and slot portfolio · hedging position on fuel and FX · pension deficits · state ownership and its implications for support · labour agreements and strike exposure · regulatory and emissions cost trajectory · management quality · anything forward-looking.

A real credit or equity view on these carriers requires most of that list. This is a balance-sheet exercise.

## Not investment advice

This is an educational project demonstrating financial-statement modelling in Python. It is not investment advice, not a recommendation to buy or sell any security, and not a substitute for reading the accounts. The author holds no position in any of the securities discussed and has no relationship with any of the companies.
