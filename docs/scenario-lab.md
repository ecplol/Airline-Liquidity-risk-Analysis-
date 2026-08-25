# Scenario lab

<p class="lede">The rest of the site reports one set of assumptions. This page lets you change them. Every calculator below runs the same maths as <a href="../notebook/main/">the notebook</a> — the defaults reproduce the published tables exactly — but the inputs are yours.</p>

!!! info "How this works"
    Everything runs in your browser. Nothing is uploaded, stored or sent anywhere, so you can put your own figures in. The carrier defaults are generated from the notebook's own output files, so they stay in step with the rest of the site.

<div data-scenario-lab data-src="../assets/scenario-data.json"></div>

## 1. Stress lab

<p class="lede">How deep a revenue decline does a balance sheet absorb, and how long does the cash last once it doesn't? Pick a carrier or enter your own numbers.</p>

<div class="sl-panel" markdown="0">
  <div class="sl-controls">
    <div class="sl-field">
      <label for="sl-carrier">Preset</label>
      <select id="sl-carrier"></select>
    </div>
    <div class="sl-field">
      <label for="sl-revenue">Revenue (€bn)</label>
      <input type="number" id="sl-revenue" step="0.1" min="0">
    </div>
    <div class="sl-field">
      <label for="sl-cogs">Cost of revenue (€bn)</label>
      <input type="number" id="sl-cogs" step="0.1" min="0">
    </div>
    <div class="sl-field">
      <label for="sl-cash">Cash (€bn)</label>
      <input type="number" id="sl-cash" step="0.1" min="0">
    </div>
  </div>

  <div class="sl-sliders">
    <div class="sl-slider">
      <label for="sl-shock">Revenue shock <output id="sl-shock-val">-40%</output></label>
      <input type="range" id="sl-shock" min="0" max="80" step="1" value="40">
    </div>
    <div class="sl-slider">
      <label for="sl-variable">Variable cost share <output id="sl-variable-val">55%</output></label>
      <input type="range" id="sl-variable" min="30" max="80" step="1" value="55">
    </div>
  </div>

  <div class="sl-tiles" id="sl-results"></div>
  <div class="sl-chart" id="sl-chart"></div>
  <div class="sl-peers" id="sl-peers"></div>
</div>

**What to try.** Drag the variable cost share and watch Lufthansa's runway at -40% move from roughly 3 to 7 months while the other three never burn at all. That single unobservable assumption is [the biggest lever in the model](stress-test.md#sensitivity-to-the-cost-split), and this is the fastest way to see which conclusions depend on it.

The vertical line on the chart is your current shock; the dashed line is the breakeven — the point where the curve begins.

## 2. Weight lab

<p class="lede">The <a href="../composite-risk/">composite ranking</a> weights five metrics 30/25/20/15/10. Those weights are a judgement call. Change them and see whether the ranking survives.</p>

<div class="sl-panel" markdown="0">
  <div id="wl-weights" class="wl-weights"></div>
  <div class="wl-meta">
    <span class="wl-total" id="wl-total">100%</span>
    <span class="wl-total-note" id="wl-total-note">weights sum to 100%</span>
    <span class="wl-buttons">
      <button type="button" id="wl-reset" class="md-button md-button--primary">Published weights</button>
      <button type="button" id="wl-equal" class="md-button">Equal weights</button>
    </span>
  </div>
  <div id="wl-results" class="wl-results"></div>
  <p id="wl-order" class="wl-order"></p>
</div>

**What to try.** Hit *Equal weights*. IAG and Ryanair swap — the finding the [composite page](composite-risk.md#stress-test-2-the-weights) reports. Then try to construct a weighting that moves Lufthansa off the bottom. Zeroing everything except the current ratio is the only way, and that is [the ratio with the least meaning for an airline](liquidity.md#below-10x-is-normal-here). That asymmetry is the real result: **the top of the ranking is a judgement, the bottom is not.**

Component scores are fixed — only the weighting changes — so what you are moving is the opinion, not the evidence.

## 3. Ratio calculator

<p class="lede">The eight line items from your own accounts, turned into the same ratios, benchmarked against the four carriers. Use any currency and any unit, as long as you are consistent.</p>

<div class="sl-panel" markdown="0">
  <div class="sl-controls rc-controls">
    <div class="sl-field"><label for="rc-revenue">Revenue</label><input type="number" id="rc-revenue" step="1" min="0" value="1000"></div>
    <div class="sl-field"><label for="rc-cogs">Cost of revenue</label><input type="number" id="rc-cogs" step="1" min="0" value="875"></div>
    <div class="sl-field"><label for="rc-receivables">Receivables</label><input type="number" id="rc-receivables" step="1" min="0" value="61"></div>
    <div class="sl-field"><label for="rc-payables">Payables</label><input type="number" id="rc-payables" step="1" min="0" value="110"></div>
    <div class="sl-field"><label for="rc-inventory">Inventory</label><input type="number" id="rc-inventory" step="1" min="0" value="41"></div>
    <div class="sl-field"><label for="rc-cash">Cash &amp; equivalents</label><input type="number" id="rc-cash" step="1" min="0" value="29"></div>
    <div class="sl-field"><label for="rc-currentassets">Current assets</label><input type="number" id="rc-currentassets" step="1" min="0" value="396"></div>
    <div class="sl-field"><label for="rc-currentliabilities">Current liabilities</label><input type="number" id="rc-currentliabilities" step="1" min="0" value="489"></div>
    <div class="sl-field"><label for="rc-days">Days in period</label><input type="number" id="rc-days" step="1" min="1" value="365"></div>
  </div>
  <p class="rc-actions"><button type="button" id="rc-load" class="md-button">Load a worked example</button></p>
  <div id="rc-results" class="rc-results"></div>
</div>

!!! warning "Read the DSO benchmark carefully"
    The peer range for DSO runs from 1.0 to 24.5 days. That spread is a **distribution model** difference — direct-to-consumer against agency and interline settlement — not a collections performance difference. "Below peer range" on DSO is not automatically good news, and "above" is not automatically bad. DPO and the cash cycle are the fairer comparisons.

Use `Days in period` = 365 for annual figures and 91 for quarterly. Mixing an annual day count with quarterly flows inflates all three day-counts roughly fourfold — the same trap the [notebook guards against](methodology.md#working-capital).

## 4. Valuation lab

<p class="lede">Build the enterprise value bridge, then re-rate it. Change any input, or the target multiple, and the implied equity moves with it.</p>

<div class="sl-panel" markdown="0">
  <div class="sl-controls">
    <div class="sl-field"><label for="vl-carrier">Preset</label><select id="vl-carrier"></select></div>
    <div class="sl-field"><label for="vl-mktcap">Market cap (€bn)</label><input type="number" id="vl-mktcap" step="0.1"></div>
    <div class="sl-field"><label for="vl-debt">Total debt incl. leases</label><input type="number" id="vl-debt" step="0.1"></div>
    <div class="sl-field"><label for="vl-minority">Minority interest</label><input type="number" id="vl-minority" step="0.1"></div>
    <div class="sl-field"><label for="vl-cash">Cash</label><input type="number" id="vl-cash" step="0.1"></div>
    <div class="sl-field"><label for="vl-ebitda">EBITDA</label><input type="number" id="vl-ebitda" step="0.1"></div>
  </div>
  <div class="sl-sliders">
    <div class="sl-slider">
      <label for="vl-target">Target EV/EBITDA <output id="vl-target-val">3.4x</output></label>
      <input type="range" id="vl-target" min="10" max="120" step="1" value="34">
    </div>
  </div>
  <div class="vl-bridge" id="vl-bridge"></div>
  <div class="sl-tiles" id="vl-results"></div>
</div>

**What to try.** Air France-KLM loads by default because it is the clearest demonstration of leverage. Its equity is a fifth of its enterprise value, so drag the target multiple one turn and watch implied upside swing by a huge percentage. That is the arithmetic behind the [+181% figure](valuation.md#implied-upside) — and the reason the valuation page tells you to read the sign and not the magnitude.

Set the target to the peer median of 3.4x to land near the published implied-upside column.

!!! note "Why it won't match to the last point"
    The presets use the EV bridge **as printed on the [valuation page](valuation.md), to one decimal**, and the slider steps in tenths of a turn. The published column re-rates to the exact median of 3.412x off unrounded inputs. Expect agreement within a point or two, not to the digit — and treat that gap as a fair reminder of how much a levered equity multiple moves on rounding alone.

## What the lab does not change

These calculators expose the assumptions the notebook makes. They do not fix the ones it cannot make at all:

- **No external liquidity.** Cash only. Undrawn facilities, sale-and-leasebacks and state support are still absent, so every runway remains a floor.
- **No management response.** Fixed cost stays fixed no matter how deep the shock.
- **No refund unwind.** A demand collapse also refunds the forward book; that outflow is not here.
- **Cost of revenue only.** If your SG&A is material, add it to the cost figure as fixed and your breakeven will be shallower.
- **Still four carriers.** Every peer band and every scaled score is relative to this group.

The full list is on [Limitations](limitations.md). Changing an input does not make an omitted factor go away.
