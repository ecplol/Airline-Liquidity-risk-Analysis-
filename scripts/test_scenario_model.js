/* Check the Scenario lab's JavaScript model against the notebook's own output.
 *
 * docs/assets/scenario.js re-implements main.ipynb's stress and composite maths
 * so the lab can run client-side. Two implementations of one model drift, and
 * the drift would be invisible - the page would keep rendering, just wrongly.
 * This runs the shipped functions against output/stress_test.csv and the
 * published composite scores and fails loudly if they disagree.
 *
 * Run from the repository root:
 *
 *     node scripts/test_scenario_model.js
 *     osascript -l JavaScript scripts/test_scenario_model.js    # macOS, no node
 */
var read, root;
if (typeof require === "function") {
  var fs = require("fs"), path = require("path");
  root = path.join(__dirname, "..");
  read = function (p) { return fs.readFileSync(path.join(root, p), "utf8"); };
} else {
  ObjC.import("Foundation");
  root = $.NSFileManager.defaultManager.currentDirectoryPath.js;
  read = function (p) {
    return $.NSString.stringWithContentsOfFileEncodingError(
      root + "/" + p, $.NSUTF8StringEncoding, null).js;
  };
}

var src = read("docs/assets/scenario.js");

// Pull the model straight out of the shipped file, so this tests the real code.
var model = src.slice(src.indexOf("function monthlyBurn"), src.indexOf("// ---- formatting"));
var scaleFn = src.slice(src.indexOf("function scale("), src.indexOf("function bindRange"));
var api = new Function(model + scaleFn +
  "return {breakevenShock:breakevenShock, monthsOfLiquidity:monthsOfLiquidity, scale:scale}")();

var data = JSON.parse(read("docs/assets/scenario-data.json"));
var lines = read("output/stress_test.csv").trim().split("\n");
var hdr = lines[0].split(",");
var pub = {};
lines.slice(1).forEach(function (l) {
  var f = l.split(","), o = {};
  hdr.forEach(function (h, i) { o[h] = f[i]; });
  pub[o.ticker] = o;
});

var V = data.variableShare, out = [], fails = 0;

function check(ok, msg) { if (!ok) fails++; out.push((ok ? "PASS  " : "FAIL  ") + msg); }

Object.keys(data.carriers).forEach(function (t) {
  var c = data.carriers[t], p = pub[t];
  var be = api.breakevenShock(c.revenue, c.cogs, V);
  var m70 = api.monthsOfLiquidity(c.revenue, c.cogs, c.cash, 0.70, V);
  var m40 = api.monthsOfLiquidity(c.revenue, c.cogs, c.cash, 0.40, V);
  var pbe = parseFloat(p["Breakeven shock"]);
  var pm70 = parseFloat(p["COVID-like -70%"]);
  var pm40 = p["Severe -40%"] === "inf" ? Infinity : parseFloat(p["Severe -40%"]);
  check(Math.abs(be - pbe) < 1e-9, t + " breakeven " + be.toFixed(6) + " vs " + pbe.toFixed(6));
  check(Math.abs(m70 - pm70) < 1e-6, t + " months at -70% " + m70.toFixed(4) + " vs " + pm70.toFixed(4));
  check((!isFinite(m40) && !isFinite(pm40)) || Math.abs(m40 - pm40) < 1e-3,
        t + " months at -40% " + (isFinite(m40) ? m40.toFixed(3) : "no burn"));
});

var METRICS = ["Cash Ratio", "Current Ratio", "CCC", "Breakeven shock", "Severe -40%"];
var comp = {};
METRICS.forEach(function (m) {
  comp[m] = api.scale(data.order.map(function (t) {
    var c = data.carriers[t];
    if (m === "Cash Ratio") return c.cashRatio;
    if (m === "Current Ratio") return c.current;
    if (m === "CCC") return c.ccc;
    if (m === "Breakeven shock") return api.breakevenShock(c.revenue, c.cogs, V);
    return c.severe40 === null ? data.displayCap : Math.min(c.severe40, data.displayCap);
  }), data.directions[m]);
});
data.order.forEach(function (t, i) {
  var s = 0;
  METRICS.forEach(function (m) { s += comp[m][i] * data.weights[m]; });
  check(Math.abs(s - data.carriers[t].publishedScore) < 0.05,
        t + " composite " + s.toFixed(1) + " vs published " + data.carriers[t].publishedScore);
});

var report = out.join("\n") + "\n\n" +
  (fails === 0 ? "ALL " + out.length + " CHECKS PASSED"
               : fails + " OF " + out.length + " CHECKS FAILED");

if (typeof require === "function") {
  console.log(report);
  process.exit(fails === 0 ? 0 : 1);
}
report;
