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

  /* ── Zeitstrahl: Balken füllen sich beim Hineinscrollen ── */
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!ruhig && 'IntersectionObserver' in window) {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); beobachter.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -20% 0px' });
    document.querySelectorAll('.timeline').forEach(function (t) {
      t.classList.add('is-armed');
      beobachter.observe(t);
    });
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
