// Mobile Navigation: ergänzt die Leiste um „Termin buchen“ und einen Menü-Button,
// der die Menüpunkte aufklappt. Stile in /css/nav-mobile.css.
(function () {
  var links = document.querySelector('nav .nav-links');
  if (!links) return;
  var nav = links.closest('nav');

  if (!links.id) links.id = 'nav-links';
  var box = document.createElement('div');
  box.className = 'nav-mobile';

  var cta = links.querySelector('.nav-cta');
  if (cta) box.appendChild(cta.cloneNode(true));

  var toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'nav-toggle';
  toggle.setAttribute('aria-controls', links.id);
  toggle.innerHTML = '<span></span><span></span><span></span>';
  box.appendChild(toggle);
  nav.appendChild(box);

  function setOpen(open) {
    nav.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  }
  setOpen(false);

  toggle.addEventListener('click', function () {
    setOpen(!nav.classList.contains('nav-open'));
  });
  // Sprungmarken auf derselben Seite (#faq, #kontakt): Menü danach schließen
  links.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('nav-open')) {
      setOpen(false);
      toggle.focus();
    }
  });
  window.matchMedia('(min-width: 769px)').addEventListener('change', function (e) {
    if (e.matches) setOpen(false);
  });
})();
