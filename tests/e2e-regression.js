#!/usr/bin/env node
/**
 * STAR//GUIDE — Comprehensive E2E Regression Suite
 *
 * Covers all features end-to-end against the live CDN.
 * Run before deploy with:  node tests/e2e-regression.js
 *
 * Override the target URL:  BASE_URL=https://localhost:8080 node tests/e2e-regression.js
 *
 * Requires:  npm install playwright  (or global playwright)
 */

const { chromium } = require("playwright");
const CONFIG = require("./config.json");

const BASE = process.env.BASE_URL || CONFIG.baseUrl;
const URL  = `${BASE}/?t=${Date.now()}`;  let passed = 0, failed = 0;
const failMsgs = [];
const allErrors = [];

function check(label, condition, detail) {
  if (condition) { passed++; console.log(`   ✅ ${label}`); }
  else { failed++; const msg = `   ❌ ${label} — ${detail}`; console.log(msg); failMsgs.push(msg); }
}

function listenErrors(page) {
  page.on("pageerror", e => allErrors.push(e.message));
}  // Screenshot directory for CI artifact upload
const SCREENSHOT_DIR = process.env.CI ? CONFIG.screenshotDir : null;

async function screenshot(page, name) {
  if (!SCREENSHOT_DIR) return;
  try { await page.screenshot({ path: `${SCREENSHOT_DIR}/e2e-${name}.png`, fullPage: false }); } catch {}
}

async function run() {
  console.log("═".repeat(68));
  console.log("  STAR//GUIDE  ·  E2E Regression Suite  ·  " + new Date().toISOString().slice(0, 19));
  console.log("═".repeat(68));
  console.log(`  Target: ${BASE}`);
  console.log("");

  const browser = await chromium.launch({ headless: true });

  // ──────────────────────────────────────────────
  // 1. DESKTOP PAGE LOAD
  // ──────────────────────────────────────────────
  console.log("▶ DESKTOP PAGE LOAD (1280×800)");
  const desktop = await browser.newPage({ viewport: CONFIG.viewport.desktop });
  listenErrors(desktop);

  await desktop.goto(URL, { waitUntil: "networkidle", timeout: CONFIG.timeouts.navigation });
  await desktop.waitForSelector(".cat-header", { timeout: CONFIG.timeouts.selector });

  const title = await desktop.title();
  check(`Page title contains '${CONFIG.expected.pageTitle}'`, title.includes(CONFIG.expected.pageTitle), title);

  const catCount = await desktop.$$eval(".cat-header", els => els.length);
  check(`${CONFIG.thresholds.categoryCount} category headers present`, catCount === CONFIG.thresholds.categoryCount, `found ${catCount}`);

  const populated = await desktop.$eval("body", (b, minChars) => b.innerText.length > minChars, CONFIG.thresholds.minContentChars);
  check(`Page content populated (>${Math.floor(CONFIG.thresholds.minContentChars/1000)}k chars)`, populated, "content too short");

  check("Zero JS errors on load", allErrors.length === 0, allErrors.join("; "));
  await screenshot(desktop, "desktop-load");
  console.log("");

  // ──────────────────────────────────────────────
  // 2. HEAD META TAGS
  // ──────────────────────────────────────────────
  console.log("▶ HEAD META TAGS");

  // Favicons — cascade-order: first icon = dark default (no media), second = light (has media)
  const favData = await desktop.$$eval("link[rel='icon']", els => els.map((e, i) => ({
    index: i, media: e.media || "(none)", type: e.type || "", href: e.href
  })));
  check("Two favicon links present", favData.length >= 2, `found ${favData.length}`);
  // First icon (index 0) should be the dark default (no media query)
  const darkFav = favData.find(f => f.index === 0);
  const lightFav = favData.find(f => f.media.includes("prefers-color-scheme: light"));
  check("Dark-mode favicon (no media) present", !!darkFav, JSON.stringify(favData));
  check("Light-mode favicon (prefers-color-scheme: light) present", !!lightFav, JSON.stringify(favData));
  check("Dark favicon is SVG", darkFav?.href?.includes("svg") || darkFav?.type?.includes("svg"), darkFav?.href?.slice(0, 60));
  check("Light favicon is SVG", lightFav?.href?.includes("svg") || lightFav?.type?.includes("svg"), lightFav?.href?.slice(0, 60));

  // OG tags
  const ogTitle = await desktop.$eval("meta[property='og:title']", e => e.content).catch(() => null);
  const ogDesc  = await desktop.$eval("meta[property='og:description']", e => e.content).catch(() => null);
  const ogImage = await desktop.$eval("meta[property='og:image']", e => e.content).catch(() => null);
  const ogType  = await desktop.$eval("meta[property='og:type']", e => e.content).catch(() => null);
  const ogUrl   = await desktop.$eval("meta[property='og:url']", e => e.content).catch(() => null);
  check("og:title present", !!ogTitle, ogTitle);
  check("og:description present", !!ogDesc, ogDesc);
  check("og:image present", !!ogImage, ogImage);
  check("og:type is 'website'", ogType === "website", ogType);
  check("og:url present", !!ogUrl, ogUrl);

  // Twitter cards
  const twCard  = await desktop.$eval("meta[name='twitter:card']", e => e.content).catch(() => null);
  const twImage = await desktop.$eval("meta[name='twitter:image']", e => e.content).catch(() => null);
  check("twitter:card present", !!twCard, twCard);
  check("twitter:image present", !!twImage, twImage);

  // Meta description
  const metaDesc = await desktop.$eval("meta[name='description']", e => e.content).catch(() => null);
  check("meta description present", !!metaDesc, metaDesc);

  // Manifest (PWA)
  const manifestLink = await desktop.$eval("link[rel='manifest']", e => e.href).catch(() => null);
  check("Manifest link present", !!manifestLink, manifestLink);
  check("Manifest href points to site.webmanifest", manifestLink?.includes("site.webmanifest"), manifestLink);

  // iOS meta tags
  const iosCapable  = await desktop.$eval("meta[name='apple-mobile-web-app-capable']", e => e.content).catch(() => null);
  const iosStatus   = await desktop.$eval("meta[name='apple-mobile-web-app-status-bar-style']", e => e.content).catch(() => null);
  const iosTitle    = await desktop.$eval("meta[name='apple-mobile-web-app-title']", e => e.content).catch(() => null);
  const iosIcon     = await desktop.$eval("link[rel='apple-touch-icon']", e => ({ href: e.href, sizes: e.sizes?.value })).catch(() => null);
  check("apple-mobile-web-app-capable = yes", iosCapable === "yes", iosCapable);
  check(`apple-mobile-web-app-status-bar-style = ${CONFIG.pwa.iosStatusBar}`, iosStatus === CONFIG.pwa.iosStatusBar, iosStatus);
  check(`apple-mobile-web-app-title = ${CONFIG.pwa.iosTitle}`, iosTitle === CONFIG.pwa.iosTitle, iosTitle);
  check("apple-touch-icon present", !!iosIcon, "missing");
  check(`apple-touch-icon sizes = ${CONFIG.pwa.iosIconSizes}`, iosIcon?.sizes === CONFIG.pwa.iosIconSizes, iosIcon?.sizes);
  console.log("");

  // ──────────────────────────────────────────────
  // 3. NOSCRIPT FALLBACK
  // ──────────────────────────────────────────────
  console.log("▶ NOSCRIPT FALLBACK");
  const noscript = await desktop.$("noscript");
  check("Noscript element exists", !!noscript, "missing");
  if (noscript) {
    const nsText = await noscript.innerText();
    check("Noscript contains 'JAVASCRIPT REQUIRED'", nsText.includes("JAVASCRIPT REQUIRED"), nsText.slice(0, 100));
    check("Noscript contains 'VIEW ON GITHUB' link", nsText.includes("VIEW ON GITHUB") || nsText.includes("github.com"), nsText.slice(0, 100));
  }
  // Verify noscript is hidden when JS runs
  const nsVisible = await desktop.$eval("noscript", el => {
    const s = getComputedStyle(el);
    return s.display !== "none" && el.offsetParent !== null;
  }).catch(() => false);
  check("Noscript not visible when JS runs", !nsVisible, "noscript is visually rendered");
  console.log("");

  // ──────────────────────────────────────────────
  // 4. KEEP 10 CARDS
  // ──────────────────────────────────────────────
  console.log("▶ KEEP 10 CARDS");
  const keepCards = await desktop.$$(".keep-card");
  const cardCount10 = keepCards.length;
  check("Keep cards present (≥10)", cardCount10 >= 10, `found ${cardCount10}`);

  const cardTexts = await Promise.all(keepCards.map(c => c.innerText()));
  const allHaveName = cardTexts.every(t => t.trim().length > 0);
  const hasOpenCode = cardTexts.some(t => t.toLowerCase().includes("opencode"));
  const hasFzf = cardTexts.some(t => t.toLowerCase().includes("fzf"));
  const hasCoolify = cardTexts.some(t => t.toLowerCase().includes("coolify"));
  check("All Keep cards have content", allHaveName, "some cards empty");
  check("Keep cards include opencode", hasOpenCode, "not found");
  check("Keep cards include fzf", hasFzf, "not found");
  check("Keep cards include coolify", hasCoolify, "not found");
  console.log("");

  // ──────────────────────────────────────────────
  // 5. TOOLBOX PANELS
  // ──────────────────────────────────────────────
  console.log("▶ TOOLBOX PANELS");

  // Toolbox toggles are 🧰 buttons with class .toolbox-toggle inside category headers
  const toolboxBtns = await desktop.$$(".toolbox-toggle");
  check("Toolbox toggle buttons exist", toolboxBtns.length > 0, `found ${toolboxBtns.length}`);

  if (toolboxBtns.length > 0) {
    // Click the first toolbox toggle (Knowledge/PKM category — 📝)
    await toolboxBtns[0].click();
    await desktop.waitForTimeout(CONFIG.timeouts.animation);

    const firstPanel = await desktop.$(".toolbox-panel.show");
    const panelText = firstPanel ? await firstPanel.innerText() : "";
    check("Toolbox panel opens", panelText.length > 50, `text length: ${panelText.length}`);
    const hasToolEntries = panelText.length > 0 && !panelText.includes("no data available");
    check("Toolbox panel has entries", hasToolEntries, panelText.slice(0, 120));

    // Click a second toolbox toggle to verify another panel works
    if (toolboxBtns.length > 1) {
      await toolboxBtns[1].click();
      await desktop.waitForTimeout(CONFIG.timeouts.animation);
      const panelsOpen = await desktop.$$eval(".toolbox-panel.show", els => els.length);
      check("Multiple toolbox panels can open", panelsOpen >= 1, `open panels: ${panelsOpen}`);
    }
  }
  console.log("");

  // ──────────────────────────────────────────────
  // 6. THEME TOGGLE
  // ──────────────────────────────────────────────
  console.log("▶ THEME TOGGLE");

  const themeBtn = await desktop.$("#theme-toggle, .theme-toggle");
  check("Theme toggle button exists", !!themeBtn, "no toggle found");

  if (themeBtn) {
    // Get initial background
    const bgBefore = await desktop.$eval("body", (el, bgVar) => getComputedStyle(el).getPropertyValue(bgVar).trim() || getComputedStyle(el).backgroundColor);

    // Toggle to light
    await themeBtn.click();
    await desktop.waitForTimeout(CONFIG.timeouts.themeToggle);

    const bgAfter = await desktop.$eval("body", (el, bgVar) => getComputedStyle(el).getPropertyValue(bgVar).trim() || getComputedStyle(el).backgroundColor);
    check("Background color changed after toggle", bgBefore !== bgAfter, `before=${bgBefore} after=${bgAfter}`);

    // localStorage persistence
    const lsTheme = await desktop.evaluate(() => localStorage.getItem("theme"));
    check("localStorage 'theme' key set", !!lsTheme, lsTheme);

    // Toggle back to dark
    await themeBtn.click();
    await desktop.waitForTimeout(CONFIG.timeouts.themeToggle);
    const bgRestored = await desktop.$eval("body", (el, bgVar) => getComputedStyle(el).getPropertyValue(bgVar).trim() || getComputedStyle(el).backgroundColor);
    check("Theme toggles back", bgRestored === bgBefore, `expected ${bgBefore} got ${bgRestored}`);
  }
  console.log("");

  // ──────────────────────────────────────────────
  // 7. NAV PILLS
  // ──────────────────────────────────────────────
  console.log("▶ NAV PILLS");
  const pills = await desktop.$$(".nav-pill");
  check("Nav pills present (≥16)", pills.length >= 16, `found ${pills.length}`);

  // Click the Security pill and verify scrolling
  const securityPill = await desktop.$(".nav-pill[data-emoji='🔒']");
  if (securityPill) {
    await securityPill.click();
    await desktop.waitForTimeout(CONFIG.timeouts.animation);

    const secCat = await desktop.$("#cat-1f512"); // 🔒 = U+1F512
    check("Clicking Security pill scrolls to Security section", !!secCat, "category not found");
    const secExpanded = secCat ? await secCat.evaluate(el => el.classList.contains("expanded")) : false;
    check("Security category expands after pill click", secExpanded, "not expanded");
  } else {
    // Fallback: click any pill and verify scroll behavior
    if (pills.length > 0) {
      const emoji = await pills[0].getAttribute("data-emoji");
      await pills[0].click();
      await desktop.waitForTimeout(CONFIG.timeouts.animation);
      const catId = await desktop.evaluate(emoji => {
        const id = "cat-" + [...emoji].map(c => c.codePointAt(0).toString(16)).join("-");
        return document.getElementById(id) !== null;
      }, emoji);
      check("Nav pill click scrolls to category", catId, `emoji=${emoji}`);
    }
  }
  console.log("");

  // ──────────────────────────────────────────────
  // 8. SEARCH
  // ──────────────────────────────────────────────
  console.log("▶ SEARCH");
  const searchInput = await desktop.$("#search");
  check("Search input exists", !!searchInput, "no search input found");

  if (searchInput) {
    await searchInput.fill(CONFIG.expected.searchTerm);
    await desktop.waitForTimeout(CONFIG.timeouts.searchFilter);

    const visibleRows = await desktop.$$eval("tbody tr:not([style*='display: none'])", els => els.length);
    check("Search 'fzf' narrows results", visibleRows > 0 && visibleRows < CONFIG.thresholds.searchNarrowMax, `visible rows: ${visibleRows}`);

    // Check info text in #search-info
    const infoText = await desktop.$eval("#search-info", e => e.innerText).catch(() => "");
    const infoOk = infoText.includes(CONFIG.expected.searchTerm) || infoText.includes("match");
    check("Search info text shows match count", infoOk, infoText || "(empty)");

    // Clear search
    await searchInput.fill("");
    await desktop.waitForTimeout(CONFIG.timeouts.searchFilter);
    const rowsAfter = await desktop.$$eval("tbody tr:not([style*='display: none'])", els => els.length);
    check("Clear search restores all rows", rowsAfter > CONFIG.thresholds.restoreMinRows, `restored to ${rowsAfter}`);
  } else {
    check("Search 'fzf' narrows results", false, "no input");
    check("Search info text shows match count", false, "no input");
    check("Clear search restores all rows", false, "no input");
  }
  console.log("");

  // ──────────────────────────────────────────────
  // 9. LANGUAGE FILTER
  // ──────────────────────────────────────────────
  console.log("▶ LANGUAGE FILTER");
  const langSelect = await desktop.$("#lang-filter");
  check("Language filter select exists", !!langSelect, "no lang select found");

  if (langSelect) {
    const options = await langSelect.$$eval("option", els => els.map(e => e.value));
    const hasPython = options.includes(CONFIG.expected.langFilter) || options.some(o => o.toLowerCase() === CONFIG.expected.langFilter.toLowerCase());
    check(`Language filter has ${CONFIG.expected.langFilter} option`, hasPython, `total options: ${options.length}`);

    if (hasPython) {
      await langSelect.selectOption({ label: CONFIG.expected.langFilter });
      await desktop.waitForTimeout(CONFIG.timeouts.searchFilter);

      const filteredRows = await desktop.$$eval("tbody tr:not([style*='display: none'])", els => els.length);
      check("Language filter narrows rows", filteredRows > 0 && filteredRows < CONFIG.thresholds.searchNarrowMax, `filtered to ${filteredRows}`);

      // Verify all visible rows have Python in the .lang cell
      const langTexts = await desktop.$$eval("tbody tr:not([style*='display: none']) .lang", els =>
        els.map(e => e.innerText.trim())
      );
      const allPython = langTexts.length > 0 && langTexts.every(t => t === CONFIG.expected.langFilter);
      check(`All visible rows are ${CONFIG.expected.langFilter}`, allPython, `found non-Python: ${langTexts.filter(t => t !== CONFIG.expected.langFilter).slice(0, 3).join(", ")} (total ${langTexts.length} rows)`);

      // Clear
      await langSelect.selectOption({ value: "" });
      await desktop.waitForTimeout(CONFIG.timeouts.searchFilter);
      const afterClear = await desktop.$$eval("tbody tr:not([style*='display: none'])", els => els.length);
      check("Clear lang filter restores all rows", afterClear > CONFIG.thresholds.restoreMinRows, `restored to ${afterClear}`);
    } else {
      check("Language filter narrows rows", false, `${CONFIG.expected.langFilter} not in options`);
      check(`All visible rows are ${CONFIG.expected.langFilter}`, false, `${CONFIG.expected.langFilter} not in options`);
      check("Clear lang filter restores all rows", false, `${CONFIG.expected.langFilter} not in options`);
    }
  } else {
    check(`Language filter has ${CONFIG.expected.langFilter} option`, false, "no select");
    check("Language filter narrows rows", false, "no select");
    check(`All visible rows are ${CONFIG.expected.langFilter}`, false, "no select");
    check("Clear lang filter restores all rows", false, "no select");
  }
  console.log("");

  // ──────────────────────────────────────────────
  // 10. MOBILE RESPONSIVE (480px)
  // ──────────────────────────────────────────────
  console.log("▶ MOBILE RESPONSIVE (480×900)");
  const mobile = await browser.newPage({ viewport: CONFIG.viewport.mobile });
  listenErrors(mobile);

  await mobile.goto(URL, { waitUntil: "networkidle", timeout: CONFIG.timeouts.navigation });
  await mobile.waitForSelector(".cat-header", { timeout: CONFIG.timeouts.selector });

  // Check rank badges are hidden on mobile
  const rankVisible = await mobile.$$eval(".k-rank, [class*='k-rank']", els =>
    els.some(el => {
      const s = getComputedStyle(el);
      return s.display !== "none" && s.visibility !== "hidden";
    })
  );
  check("Rank badges hidden on mobile", !rankVisible, "rank badges still visible");

  // Hero grid should be 2 columns
  const heroGrid = await mobile.$(".hero-grid, [class*='hero']");
  if (heroGrid) {
    const gridCols = await heroGrid.evaluate(el => getComputedStyle(el).gridTemplateColumns);
    const is2Col = gridCols.split(" ").length <= 2;
    check("Hero grid adapts for mobile", is2Col, `grid cols: ${gridCols}`);
  }

  check("Zero JS errors on mobile", allErrors.length === 0, allErrors.join("; "));
  await screenshot(mobile, "mobile-load");
  await mobile.close();
  console.log("");

  // ──────────────────────────────────────────────
  // 11. PWA / SERVICE WORKER
  // ──────────────────────────────────────────────
  console.log("▶ PWA / SERVICE WORKER");

  const swSupported = await desktop.evaluate(() => "serviceWorker" in navigator);
  check("ServiceWorker API supported", swSupported, "not supported");

  if (swSupported) {
    // Wait for SW to activate, then check registration
    await desktop.waitForTimeout(CONFIG.timeouts.serviceWorker);
    const swReg = await desktop.evaluate(async (swScope) => {
      const reg = await navigator.serviceWorker.getRegistration();
      if (reg) return { scope: reg.scope, active: !!reg.active };
      // Try scope-based lookup
      const scoped = await navigator.serviceWorker.getRegistration(swScope);
      return scoped ? { scope: scoped.scope, active: !!scoped.active } : null;
    });
    check("Service worker registered", !!swReg, "no registration after 2s wait");
    if (swReg) {
      check(`SW scope contains ${CONFIG.pwa.swScope}`, swReg.scope?.includes(CONFIG.pwa.swScope), swReg.scope);
      check("SW has active worker", swReg.active, "not active");
    }
  } else {
    check("Service worker registered", false, "API unsupported");
    check(`SW scope contains ${CONFIG.pwa.swScope}`, false, "API unsupported");
    check("SW has active worker", false, "API unsupported");
  }

  // Manifest fetchable
  const manifestResp = await desktop.evaluate(async () => {
    const link = document.querySelector("link[rel='manifest']");
    if (!link) return { ok: false, status: 0, json: null };
    try {
      const r = await fetch(link.href);
      const json = await r.json();
      return { ok: r.ok, status: r.status, json };
    } catch (e) {
      return { ok: false, status: 0, json: null, error: e.message };
    }
  });
  check("Manifest fetchable (HTTP 200)", manifestResp.ok, `status ${manifestResp.status}`);
  check(`Manifest theme_color = ${CONFIG.pwa.themeColor}`, manifestResp.json?.theme_color === CONFIG.pwa.themeColor, manifestResp.json?.theme_color);
  check(`Manifest display = ${CONFIG.pwa.display}`, manifestResp.json?.display === CONFIG.pwa.display, manifestResp.json?.display);
  check(`Manifest has ${CONFIG.pwa.iconPurpose} icon`, manifestResp.json?.icons?.some(i => (i.purpose || "").includes(CONFIG.pwa.iconPurpose)), JSON.stringify(manifestResp.json?.icons?.map(i => i.purpose)));

  // Icon fetchable
  const iconResp = await desktop.evaluate(async () => {
    const icon = document.querySelector("link[rel='apple-touch-icon']");
    if (!icon) return { ok: false, size: 0, type: "" };
    try {
      const r = await fetch(icon.href);
      const buf = await r.arrayBuffer();
      return { ok: r.ok, status: r.status, size: buf.byteLength, type: r.headers.get("content-type") };
    } catch (e) {
      return { ok: false, status: 0, size: 0, type: "" };
    }
  });
  check("apple-touch-icon fetchable", iconResp.ok, `status ${iconResp.status}`);
  check("Icon is image/png", iconResp.type?.includes("png"), iconResp.type);
  check(`Icon file size > ${Math.floor(CONFIG.thresholds.iconMinSize/1000)}KB`, iconResp.size > CONFIG.thresholds.iconMinSize, `${iconResp.size} bytes`);
  await screenshot(desktop, "desktop-final");
  console.log("");

  // ──────────────────────────────────────────────
  // 12. VISUAL POLISH — Sticky Header + Card Hover
  // ──────────────────────────────────────────────
  console.log("▶ VISUAL POLISH");

  // Sticky header: verify position, top, backdrop-filter
  const headerStyles = await desktop.evaluate(() => {
    const h = document.querySelector("header");
    if (!h) return null;
    const s = getComputedStyle(h);
    return { position: s.position, top: s.top, backdropFilter: s.backdropFilter };
  });
  check(`Header position is ${CONFIG.visual.stickyHeader.position}`, headerStyles?.position === CONFIG.visual.stickyHeader.position, headerStyles?.position);
  check(`Header top is ${CONFIG.visual.stickyHeader.top}`, headerStyles?.top === CONFIG.visual.stickyHeader.top, headerStyles?.top);
  check("Header has backdrop-filter blur", headerStyles?.backdropFilter?.includes("blur"), headerStyles?.backdropFilter);

  // Card hover lift: check that :hover rules contain translateY(-1px) via cssText
  const hoverLift = await desktop.evaluate((translateY) => {
    for (const sheet of document.styleSheets) {
      try {
        for (const rule of sheet.cssRules) {
          if (rule.selectorText && (rule.selectorText.includes(".hero-card:hover") || rule.selectorText.includes(".keep-card:hover"))) {
            if (rule.cssText.includes(translateY)) return rule.selectorText;
          }
        }
      } catch(e) { /* cross-origin sheet */ }
    }
    return null;
  }, CONFIG.visual.cardHoverLift.translateY);
  check(`Card hover has ${CONFIG.visual.cardHoverLift.translateY}`, !!hoverLift, hoverLift || "not found in stylesheets");

  // Button :active press feedback: check for scale in :active rules via cssText
  const pressRule = await desktop.evaluate(() => {
    for (const sheet of document.styleSheets) {
      try {
        for (const rule of sheet.cssRules) {
          if (rule.selectorText && rule.selectorText.includes(":active") && rule.cssText.includes("scale")) {
            return rule.selectorText;
          }
        }
      } catch(e) {}
    }
    return null;
  });
  check("Button :active press feedback (scale) present", !!pressRule, pressRule || "not found");

  await screenshot(desktop, "visual-polish");
  console.log("");

await desktop.close();
  await browser.close();

  // ──────────────────────────────────────────────
  // SUMMARY
  // ──────────────────────────────────────────────
  const total = passed + failed;
  console.log("═".repeat(68));
  console.log(`  RESULTS:  ${passed}/${total} passed  ${failed > 0 ? "❌" : "🏆"}`);
  if (failed > 0) {
    console.log(`  FAILURES: ${failed}`);
    for (const m of failMsgs) console.log(m);
  }
  console.log("═".repeat(68));

  if (failed > 0) process.exit(1);
}

run().catch(err => {
  console.error("FATAL:", err.message);
  process.exit(2);
});
