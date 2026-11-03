/* Trade journal storage (same design as the reversal scanner).
 *
 * Trades live in trades.json in the GitHub repository, so they are permanent, work on
 * any device, and are read by learn.py on every review. Saving needs a fine-grained
 * GitHub token with "Contents: read and write" (and "Actions: read and write" for the
 * Run buttons) on this repository. The token is stored only in this browser.
 * Live prices: Finnhub's free US quote service (stocks/ETFs). Futures fall back to
 * the last scanned price.
 */
const Store = (() => {
  const CFG = window.CFG || {};
  const KEY = "gh_token";
  const ls = {get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
              set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} }};
  const api = path => `https://api.github.com/repos/${CFG.repo}/${path}`;
  const enc = s => btoa(unescape(encodeURIComponent(s)));
  const dec = s => decodeURIComponent(escape(atob(s.replace(/\n/g, ""))));
  let cache = {trades: [], sha: null};

  const token = () => ls.get(KEY);
  const quoteKey = () => ls.get("fh_key");
  const canWrite = () => !!(CFG.repo && token());
  const headers = () => ({Authorization: `Bearer ${token()}`, Accept: "application/vnd.github+json"});

  async function quote(ticker) {
    const k = quoteKey();
    if (!k || ticker.includes("=")) return null;   // Finnhub free has no futures
    try {
      const r = await fetch(`https://finnhub.io/api/v1/quote?symbol=${encodeURIComponent(ticker)}&token=${encodeURIComponent(k)}`, {cache: "no-store"});
      if (!r.ok) return null;
      const j = await r.json();
      return j.c > 0 ? Math.round(j.c * 100) / 100 : null;
    } catch (e) { return null; }
  }

  async function load() {
    if (canWrite()) {
      const r = await fetch(api(`contents/trades.json?ref=${CFG.branch || "main"}&t=${Date.now()}`), {headers: headers(), cache: "no-store"});
      if (r.status === 404) { cache = {trades: [], sha: null}; return cache.trades; }
      if (!r.ok) throw new Error(`GitHub read failed (${r.status}). Check the token.`);
      const j = await r.json();
      cache = {trades: JSON.parse(dec(j.content) || "[]"), sha: j.sha};
      return cache.trades;
    }
    try { const r = await fetch(`data/trades.json?t=${Date.now()}`, {cache: "no-store"}); if (r.ok) cache.trades = await r.json(); } catch (e) {}
    return cache.trades;
  }

  async function update(mutate, message) {
    if (!canWrite()) throw new Error("Add your GitHub token (Settings) to save trades.");
    for (let attempt = 0; attempt < 3; attempt++) {
      await load();
      const trades = JSON.parse(JSON.stringify(cache.trades));
      mutate(trades);
      const body = {message, content: enc(JSON.stringify(trades, null, 1)), branch: CFG.branch || "main"};
      if (cache.sha) body.sha = cache.sha;
      const r = await fetch(api("contents/trades.json"), {method: "PUT", headers: headers(), body: JSON.stringify(body)});
      if (r.ok) { cache = {trades, sha: (await r.json()).content.sha}; return trades; }
      if (r.status !== 409 && r.status !== 422) throw new Error(`GitHub save failed (${r.status}). The token needs "Contents: read and write".`);
    }
    throw new Error("Could not save after 3 attempts; please try again.");
  }

  async function dispatch(inputs) {
    const r = await fetch(api(`actions/workflows/${CFG.workflow || "fvg.yml"}/dispatches`),
      {method: "POST", headers: headers(), body: JSON.stringify({ref: CFG.branch || "main", inputs})});
    if (r.status !== 204) throw new Error(`GitHub refused the request (${r.status}). Check the token.`);
  }

  function mountSettings(el, onSave) {
    el.innerHTML = `<details class="settings"><summary>Settings: GitHub token ${token() ? "✓" : "(needed to save trades)"} · live prices ${quoteKey() ? "✓" : "(off)"}</summary>
      <div>GitHub fine-grained token for this repository with <b>Contents</b> and <b>Actions</b> set to read and write.</div>
      <input type="password" placeholder="github_pat_..." aria-label="GitHub token" data-k="tok">
      <div style="margin-top:6px">Finnhub API key for live stock prices (free at finnhub.io).</div>
      <input type="password" placeholder="Finnhub key" aria-label="Finnhub API key" data-k="fh">
      <button>Save</button><div class="hint">Both are stored only in this browser.</div></details>`;
    el.querySelector("button").onclick = () => {
      const t = el.querySelector("[data-k=tok]").value.trim(), f = el.querySelector("[data-k=fh]").value.trim();
      if (t) ls.set(KEY, t);
      if (f) ls.set("fh_key", f);
      mountSettings(el, onSave); onSave && onSave();
    };
  }

  return {load, update, dispatch, canWrite, quote, mountSettings, ls, get trades() { return cache.trades; }};
})();
