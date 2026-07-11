/* Cookie-Banner Logik (DSGVO-konform)
   - Blockt GA4 bis zur expliziten Einwilligung via Google Consent Mode v2
   - Speichert Auswahl 365 Tage im localStorage
   - Banner öffnet sich erneut bei Klick auf [data-action="cookie-settings"] */

(function () {
  "use strict";

  var CONSENT_KEY = "xpo-consent";
  var CONSENT_VERSION = 1;
  var CONSENT_TTL_DAYS = 365;

  var banner, options, acceptAllBtn, essentialsBtn, settingsToggleBtn, saveCustomBtn;
  var statisticsInput;

  function readConsent() {
    try {
      var raw = localStorage.getItem(CONSENT_KEY);
      if (!raw) return null;
      var c = JSON.parse(raw);
      if (!c || c.version !== CONSENT_VERSION) return null;
      var age = (Date.now() - new Date(c.timestamp).getTime()) / (1000 * 60 * 60 * 24);
      if (age > CONSENT_TTL_DAYS) return null;
      return c;
    } catch (e) { return null; }
  }

  function writeConsent(statistics) {
    var c = {
      version: CONSENT_VERSION,
      timestamp: new Date().toISOString(),
      statistics: !!statistics
    };
    try { localStorage.setItem(CONSENT_KEY, JSON.stringify(c)); } catch (e) {}
    applyConsent(c.statistics);
    hideBanner();
  }

  function applyConsent(statistics) {
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", {
        "analytics_storage": statistics ? "granted" : "denied",
        "ad_storage": "denied",
        "ad_user_data": "denied",
        "ad_personalization": "denied"
      });
    }
    if (statistics) loadClarity();
  }

  function loadClarity() {
    if (window.__xpoClarityLoaded) return;
    window.__xpoClarityLoaded = true;
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments);};
      t=l.createElement(r); t.async=1; t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "xkojypf2yc");
  }

  function showBanner(prefill) {
    if (!banner) return;
    if (prefill && statisticsInput) {
      statisticsInput.checked = !!prefill.statistics;
    }
    banner.classList.add("is-visible");
    banner.setAttribute("aria-hidden", "false");
  }

  function hideBanner() {
    if (!banner) return;
    banner.classList.remove("is-visible");
    banner.setAttribute("aria-hidden", "true");
    if (options) options.hidden = true;
    if (saveCustomBtn) saveCustomBtn.hidden = true;
    if (acceptAllBtn) acceptAllBtn.hidden = false;
  }

  function toggleSettings() {
    if (!options) return;
    var nowOpen = options.hidden;
    options.hidden = !nowOpen;
    if (saveCustomBtn) saveCustomBtn.hidden = !nowOpen;
    if (acceptAllBtn) acceptAllBtn.hidden = nowOpen;
  }

  function wireUp() {
    banner = document.getElementById("cookieBanner");
    if (!banner) return;
    options = document.getElementById("cookieOptions");
    acceptAllBtn = document.getElementById("cookieAcceptAll");
    essentialsBtn = document.getElementById("cookieEssentials");
    settingsToggleBtn = document.getElementById("cookieSettingsToggle");
    saveCustomBtn = document.getElementById("cookieSaveCustom");
    statisticsInput = document.getElementById("consentStatistics");

    if (acceptAllBtn)
      acceptAllBtn.addEventListener("click", function () { writeConsent(true); });
    if (essentialsBtn)
      essentialsBtn.addEventListener("click", function () { writeConsent(false); });
    if (settingsToggleBtn)
      settingsToggleBtn.addEventListener("click", toggleSettings);
    if (saveCustomBtn)
      saveCustomBtn.addEventListener("click", function () {
        writeConsent(statisticsInput && statisticsInput.checked);
      });

    document.addEventListener("click", function (e) {
      var t = e.target;
      if (t && t.closest && t.closest('[data-action="cookie-settings"]')) {
        e.preventDefault();
        var existing = readConsent();
        if (options) options.hidden = false;
        if (saveCustomBtn) saveCustomBtn.hidden = false;
        if (acceptAllBtn) acceptAllBtn.hidden = true;
        showBanner(existing || { statistics: false });
      }
    });

    var existing = readConsent();
    if (existing) {
      applyConsent(existing.statistics);
    } else {
      showBanner();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wireUp);
  } else {
    wireUp();
  }
})();
