/* XPONext: Menü auf dem Handy und Kontaktformular. Gilt für alle Seiten. */
(function () {
  'use strict';

  /* ── Menü ─────────────────────────────────────────────── */
  var header = document.getElementById('site-header');
  var toggle = header && header.querySelector('.nav-toggle');
  if (toggle) {
    var setOpen = function (open) {
      header.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
    };
    toggle.addEventListener('click', function () {
      setOpen(!header.classList.contains('nav-open'));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('nav-open')) {
        setOpen(false);
        toggle.focus();
      }
    });
    header.querySelectorAll('.site-nav a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (e) {
      if (e.matches) setOpen(false);
    });
  }

  /* ── Umschalter (Tabs) ─────────────────────────────────── */
  document.querySelectorAll('[data-tabs]').forEach(function (box) {
    var tabs = [].slice.call(box.querySelectorAll('[role="tab"]'));
    var zeige = function (tab, fokus) {
      tabs.forEach(function (t) {
        var an = t === tab;
        t.setAttribute('aria-selected', an ? 'true' : 'false');
        t.tabIndex = an ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !an;
      });
      if (fokus) tab.focus();
    };
    box.classList.add('js-tabs');
    zeige(tabs[0], false);
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { zeige(tab, false); });
      tab.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') zeige(tabs[(i + 1) % tabs.length], true);
        if (e.key === 'ArrowLeft') zeige(tabs[(i - 1 + tabs.length) % tabs.length], true);
      });
    });
  });

  /* ── Zeitstrahl: Balken wachsen mit dem Scrollen ─────────
     Der Fortschritt hängt an der Scrollposition, geht aber nie zurück: Einmal ganz
     aufgebaut, bleiben die Balken stehen, bis die Seite neu geladen oder erneut
     aufgerufen wird. Beide Tabs teilen sich den Fortschritt. */
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!ruhig) {
    var STAFFEL = 0.16;   // Versatz zwischen zwei Balken (Anteil des Scrollwegs)
    var DAUER = 0.5;      // Anteil des Scrollwegs, über den ein einzelner Balken wächst
    document.querySelectorAll('.timeline').forEach(function (t) { t.classList.add('is-scroll'); });
    var gruppen = [].slice.call(document.querySelectorAll('.timeline')).reduce(function (liste, t) {
      var box = t.closest('[data-tabs]') || t;
      var g = liste.filter(function (x) { return x.box === box; })[0];
      if (!g) { g = { box: box, teile: [], max: 0 }; liste.push(g); }
      g.teile.push(t);
      return liste;
    }, []);
    var setze = function (g) {
      g.teile.forEach(function (t) {
        var balken = t.querySelectorAll('.timeline__bar, .timeline__mark');
        var gesamt = (balken.length - 1) * STAFFEL + DAUER;
        balken.forEach(function (b, i) {
          var p = Math.min(Math.max((g.max * gesamt - i * STAFFEL) / DAUER, 0), 1);
          b.style.setProperty('--p', (1 - Math.pow(1 - p, 2)).toFixed(3));
        });
      });
    };
    var offen = [];
    var miss = function () {
      var vh = window.innerHeight;
      offen = offen.filter(function (g) {
        var r = g.box.getBoundingClientRect();
        if (!r.height) return true;
        // Start: Oberkante bei 85 % der Fensterhöhe. Fertig: Unterkante bei 75 %.
        var p = (vh * 0.85 - r.top) / (r.height + vh * 0.1);
        if (p > g.max) { g.max = Math.min(p, 1); setze(g); }
        return g.max < 1;
      });
      if (!offen.length) window.removeEventListener('scroll', anfrage);
    };
    var wartet = false;
    var anfrage = function () {
      if (wartet) return;
      wartet = true;
      requestAnimationFrame(function () { wartet = false; miss(); });
    };
    var start = function () {
      gruppen.forEach(function (g) { g.max = 0; setze(g); });
      offen = gruppen.slice();
      window.addEventListener('scroll', anfrage, { passive: true });
      miss();
    };
    start();
    // Zurück aus einer anderen Seite (Browser-Cache): wieder von vorn
    window.addEventListener('pageshow', function (e) { if (e.persisted) start(); });
  }

  /* ── Zeitwert-Rechner ─────────────────────────────────── */
  var calcH = document.getElementById('calc-h');
  var calcR = document.getElementById('calc-r');
  if (calcH && calcR) {
    var euro = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
    var rechne = function () {
      var h = Number(calcH.value), r = Number(calcR.value), jahr = h * r * 46;
      document.getElementById('calc-h-out').textContent = h;
      document.getElementById('calc-r-out').textContent = r;
      document.getElementById('calc-year').textContent = euro.format(Math.round(jahr / 100) * 100);
      document.getElementById('calc-month').textContent = euro.format(Math.round(jahr / 12 / 10) * 10);
    };
    calcH.addEventListener('input', rechne);
    calcR.addEventListener('input', rechne);
    rechne();
  }

  /* ── Kontaktformular ──────────────────────────────────── */
  var ENDPOINT = 'https://script.google.com/macros/s/AKfycbw0gr0qUcnscoGS-1qk3l5PXCpX0wMWFpJKlPi5zkiLc_LMliyTjEELHSh_Xsg_H1Ux/exec';
  var quelle = new URLSearchParams(window.location.search).get('quelle');
  document.querySelectorAll('form.contact-form').forEach(function (form) {
    if (quelle && /^[a-z0-9-]{1,40}$/.test(quelle)) form.dataset.quelle = (form.dataset.quelle || 'Kontakt') + ', ' + quelle;
    var geladen = Date.now();
    var status = form.parentNode.querySelector('.form-status');
    var submitBtn = form.querySelector('button[type="submit"]');
    var label = submitBtn ? submitBtn.textContent : '';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.website && form.website.value.trim()) return; // Honeypot
      if (Date.now() - geladen < 3000) { // Zeitsperre: Bots schicken sofort ab
        if (status) { status.hidden = false; status.classList.add('is-error'); status.textContent = 'Bitte einen Moment warten und dann erneut senden.'; }
        return;
      }

      var payload = {
        name: form.name.value.trim(),
        email: form.email.value.trim(),
        phone: form.phone ? form.phone.value.trim() : '',
        message: form.message.value.trim()
      };
      if (form.dataset.quelle) payload.message = '[' + form.dataset.quelle + '] ' + payload.message;

      submitBtn.disabled = true;
      submitBtn.textContent = 'Wird gesendet …';
      if (status) { status.hidden = true; status.classList.remove('is-error'); }

      fetch(ENDPOINT, {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload)
      }).then(function (res) { return res.json(); }).then(function (data) {
        if (!data || data.ok !== true) throw new Error(data && data.error);
        if (typeof window.gtag_report_conversion === 'function') window.gtag_report_conversion();
        form.reset();
        form.hidden = true;
        if (status) {
          status.hidden = false;
          status.textContent = 'Danke! Ihre Anfrage ist angekommen. Wir melden uns innerhalb von 24 Stunden an Werktagen.';
        }
      }).catch(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = label;
        if (status) {
          status.hidden = false;
          status.classList.add('is-error');
          status.textContent = 'Da ist leider etwas schiefgelaufen. Schreiben Sie uns direkt an info@xponext.de oder rufen Sie an: 0163 6857434.';
        }
      });
    });
  });
})();
