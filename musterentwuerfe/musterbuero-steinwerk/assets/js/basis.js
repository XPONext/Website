/* Grundverhalten: Mobile-Navigation, Projektfilter und Ansicht-Umschalter in derselben Seite.
   Kein Framework, keine Abhängigkeit, kein Tracking. Ohne dieses Skript funktioniert alles:
   die Filter sind Links auf statische Filterseiten, der Umschalter führt auf /projekte/ bzw. /. */
(function () {
  'use strict';

  // Mobile-Navigation: Schalter öffnet/schließt die Vollbild-Liste, aria-expanded folgt, Esc schließt.
  var schalter = document.querySelector('.kopf__schalter');
  var reiter = document.getElementById('hauptnavigation');
  if (schalter && reiter) {
    var setzen = function (offen) {
      reiter.setAttribute('data-offen', String(offen));
      schalter.setAttribute('aria-expanded', String(offen));
      schalter.textContent = offen ? 'Schließen' : 'Menü';
    };
    schalter.addEventListener('click', function () {
      setzen(reiter.getAttribute('data-offen') !== 'true');
    });
    // Fokus bleibt im offenen Vollbildmenü (Brief 7): Tab/Shift+Tab kreisen über Schalter + Einträge,
    // Escape schließt und gibt den Fokus an den Schalter zurück.
    document.addEventListener('keydown', function (e) {
      if (reiter.getAttribute('data-offen') !== 'true') return;
      if (e.key === 'Escape') {
        e.preventDefault();
        setzen(false);
        schalter.focus();
        return;
      }
      if (e.key !== 'Tab') return;
      var ziele = [schalter].concat(Array.prototype.slice.call(reiter.querySelectorAll('a[href]')));
      var erstes = ziele[0], letztes = ziele[ziele.length - 1];
      var aktiv = document.activeElement;
      var drinnen = ziele.indexOf(aktiv) !== -1;
      if (!drinnen) { e.preventDefault(); (e.shiftKey ? letztes : erstes).focus(); return; }
      if (e.shiftKey && aktiv === erstes) { e.preventDefault(); letztes.focus(); }
      else if (!e.shiftKey && aktiv === letztes) { e.preventDefault(); erstes.focus(); }
    });
    // Fokus, der per Maus/Programm aus dem Menü fällt, zurückholen
    document.addEventListener('focusin', function (e) {
      if (reiter.getAttribute('data-offen') !== 'true') return;
      if (e.target === schalter || reiter.contains(e.target)) return;
      schalter.focus();
    });
    reiter.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setzen(false);
    });
  }

  // Projektfilter und Umschalter: Links werden zu Buttons mit aria-pressed, Filtern ohne Seitenwechsel.
  var bereich = document.querySelector('[data-projekte]');
  if (!bereich) return;
  var kacheln = bereich.querySelectorAll('.kachel');
  var zeilen = bereich.querySelectorAll('.liste tbody tr');

  function zuButton(link, gedrueckt) {
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = link.textContent;
    b.setAttribute('aria-pressed', String(gedrueckt));
    b.dataset.href = link.getAttribute('href');
    Array.prototype.forEach.call(link.attributes, function (a) {
      if (a.name.indexOf('data-') === 0) b.setAttribute(a.name, a.value);
    });
    link.parentNode.replaceChild(b, link);
    return b;
  }

  var filterButtons = [];
  bereich.querySelectorAll('.filter a').forEach(function (a) {
    filterButtons.push(zuButton(a, a.hasAttribute('aria-current')));
  });
  filterButtons.forEach(function (b) {
    b.addEventListener('click', function () {
      var typ = b.dataset.filter || '';
      filterButtons.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      kacheln.forEach(function (k) { k.hidden = !!typ && k.dataset.typ !== typ; });
      zeilen.forEach(function (z) { z.hidden = !!typ && z.dataset.typ !== typ; });
      if (window.history && history.replaceState) {
        try { history.replaceState(null, '', b.dataset.href); } catch (err) { /* file:// */ }
      }
    });
  });

  // Filterseiten zeigen Raster und Tabelle untereinander (Brief 6, data-ansicht="beide"):
  // dort bleiben die Umschalter-Einträge Sprunglinks, kein Ein-/Ausblenden.
  if (bereich.getAttribute('data-ansicht') === 'beide') return;
  var ansichtButtons = [];
  bereich.querySelectorAll('.umschalter a').forEach(function (a) {
    ansichtButtons.push(zuButton(a, a.hasAttribute('aria-current')));
  });
  ansichtButtons.forEach(function (b) {
    b.addEventListener('click', function () {
      ansichtButtons.forEach(function (x) {
        x.setAttribute('aria-pressed', String(x === b));
        x.textContent = (x === b ? '[x] ' : '[ ] ') + x.textContent.replace(/^\[.\] /, '');
      });
      bereich.setAttribute('data-ansicht', b.dataset.ansicht);
    });
  });
  if (ansichtButtons.length) {
    var aktiv = ansichtButtons.filter(function (x) { return x.getAttribute('aria-pressed') === 'true'; })[0];
    if (aktiv) bereich.setAttribute('data-ansicht', aktiv.dataset.ansicht);
  }
})();
