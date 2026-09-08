/* Grundverhalten Musterstudio Lindenau: Vollbild-Menü (mobil), Einblenden der Bilder
   (robmills-com-au-F10), wachsende Linie beim ersten Scroll (robmills-com-au-F3).
   Kein Framework, kein Tracking. Alles ist ohne dieses Skript benutzbar. */
(function () {
  'use strict';
  var html = document.documentElement;
  var reduziert = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Vollbild-Menü: Schalter öffnet/schließt, aria-expanded folgt, Escape schließt,
  // Fokus bleibt im Overlay, Klick auf einen Punkt schließt (helenhard-no-F12).
  var schalter = document.querySelector('.kopf__schalter');
  var nav = document.getElementById('hauptnavigation');
  if (schalter && nav) {
    var fokussierbar = 'a[href], button:not([disabled])';
    function setzen(offen) {
      nav.setAttribute('data-offen', String(offen));
      schalter.setAttribute('aria-expanded', String(offen));
      schalter.textContent = offen ? 'Schließen' : 'Menü';
      if (offen) { document.body.setAttribute('data-menue', 'offen'); }
      else { document.body.removeAttribute('data-menue'); }
    }
    schalter.addEventListener('click', function () {
      var offen = nav.getAttribute('data-offen') === 'true';
      setzen(!offen);
      if (!offen) { var erster = nav.querySelector(fokussierbar); if (erster) erster.focus(); }
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.getAttribute('data-offen') === 'true') setzen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (nav.getAttribute('data-offen') !== 'true') return;
      if (e.key === 'Escape') { setzen(false); schalter.focus(); return; }
      if (e.key === 'Tab') {
        var elemente = [schalter].concat(Array.prototype.slice.call(nav.querySelectorAll(fokussierbar)));
        var erstes = elemente[0], letztes = elemente[elemente.length - 1];
        if (e.shiftKey && document.activeElement === erstes) { e.preventDefault(); letztes.focus(); }
        else if (!e.shiftKey && document.activeElement === letztes) { e.preventDefault(); erstes.focus(); }
      }
    });
    // Beim Wechsel auf Desktop-Breite schließen, damit der Zustand nicht hängen bleibt.
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (mq) {
      if (mq.matches && nav.getAttribute('data-offen') === 'true') setzen(false);
    });
  }

  // Einblenden der Bilder beim Scrollen. Ohne IntersectionObserver oder bei
  // reduzierter Bewegung bleibt alles sofort sichtbar (CSS setzt opacity nur mit .js).
  var bilder = document.querySelectorAll('.bild--anim');
  function alleZeigen() { bilder.forEach(function (el) { el.classList.add('sichtbar'); }); }
  if (!reduziert && 'IntersectionObserver' in window && bilder.length) {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('sichtbar'); beobachter.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.15 });
    bilder.forEach(function (el) { beobachter.observe(el); });
    setTimeout(alleZeigen, 4000); // Sicherheitsnetz
  } else {
    alleZeigen();
  }

  // Wachsende Linie: einmal, sobald scrollY > 40 (nur Startseite hat .linie).
  if (document.querySelector('.linie')) {
    function pruefen() {
      if (window.scrollY > 40) { html.classList.add('gescrollt'); window.removeEventListener('scroll', pruefen); }
    }
    if (reduziert) { html.classList.add('gescrollt'); }
    else { window.addEventListener('scroll', pruefen, { passive: true }); pruefen(); }
  }
})();
