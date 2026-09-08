/* Grundverhalten: Mobile-Navigation. Kein Framework, keine Abhängigkeit, kein
   Tracking. Alles ist ohne dieses Skript benutzbar — auf Desktop ist die
   Navigation immer sichtbar, das Skript bedient nur den Text-Schalter „Menü".
   (helenhard-no-F12: Auslöser ist ein button mit aria-expanded/aria-controls,
   Beschriftung wechselt auf „Schließen", Liste schließt nach Auswahl und mit Escape.) */
(function () {
  'use strict';

  var schalter = document.querySelector('.kopf__schalter');
  var ziel = schalter && document.getElementById(schalter.getAttribute('aria-controls'));
  if (!schalter || !ziel) return;

  function setzen(offen) {
    ziel.setAttribute('data-offen', String(offen));
    schalter.setAttribute('aria-expanded', String(offen));
    schalter.textContent = offen ? 'Schließen' : 'Menü';
  }

  schalter.addEventListener('click', function () {
    setzen(ziel.getAttribute('data-offen') !== 'true');
  });

  // Nach Auswahl eines Punktes schließt die Liste (auch bei Ankern auf derselben Seite).
  ziel.addEventListener('click', function (e) {
    if (e.target.closest('a')) setzen(false);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && ziel.getAttribute('data-offen') === 'true') {
      setzen(false);
      schalter.focus();
    }
  });
})();
