# 06 · Fallstudien auf der Startseite

**Status:** offen · **Wartet auf:** 04
**Schließt:** `Fallstudie 1–3 Screenshot`, `Fallstudie 1–3 Zahl`, `Fallstudie 1–3 Zitat` in `index.html`

## Wo
`index.html`, Section „Was wir für Kunden umgesetzt haben“, `<div class="cases">` mit drei
`<article class="case">`. Die Überschriften (Architektur, …) stehen schon, ggf. an den echten Fall anpassen.
Der Lead-Satz darüber verspricht „Architektur, Innenausbau und Touristik“, bei anderer Auswahl anpassen.

## Umsetzung je Fall
1. Screenshot als WebP, 1600 × 1000 px (16:10), unter `assets/projekte/<kurzname>.webp`.
   Umwandeln z. B.: `cwebp -q 80 screenshot.png -o assets/projekte/kurzname.webp`
2. Markup ersetzen (CSS-Klassen gibt es schon):
   ```html
   <article class="case">
     <img class="case__media" src="/assets/projekte/kurzname.webp" alt="Startseite der neuen Website von …" width="1600" height="1000" loading="lazy">
     <div class="case__body">
       <span class="case__tag">Architektur</span>
       <h3>Neue Website für ein Architekturbüro</h3>
       <p class="case__metric">+60 %<small>Anfragen pro Monat, Jan–Jun 2026 gegenüber Vorjahr</small></p>
       <blockquote>„…“ <cite>Name, Funktion, Firma</cite></blockquote>
     </div>
   </article>
   ```
3. Für Bilder in `css/site.css` ergänzen: `img.case__media { width: 100%; height: auto; object-fit: cover; }`
4. Bild in `assets/BILDER.md` eintragen, Platzhalter-Kommentar löschen.

## Fertig, wenn
- [ ] Drei Fälle mit Bild, Zahl (mit Zeitraum) und Zitat
- [ ] Zahlen identisch mit denen auf der Projekte-Seite (Ticket 07)
