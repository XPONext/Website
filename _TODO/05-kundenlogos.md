# 05 · Kundenlogos auf der Startseite

**Status:** offen · **Wartet auf:** 04 · **Schließt:** `Kundenlogo 1` bis `Kundenlogo 5` in `index.html`

## Wo
`index.html`, Section „Zufriedene Partner“, `<div class="logo-row">` mit fünf `ph`-Kästen.

## Umsetzung
1. Logos ablegen unter `assets/kunden/<kurzname>.svg` (oder `.webp`, ca. 320 px breit).
   Einheitlich: transparenter Hintergrund, keine weißen Kästen.
2. Kästen ersetzen:
   ```html
   <div class="logo-row">
     <img src="/assets/kunden/kurzname.svg" alt="Firmenname" width="160" height="48" loading="lazy">
     …
   </div>
   ```
3. In `css/site.css` nach `.logo-row > *` ergänzen, damit Logos ruhig und gleich groß wirken:
   ```css
   .logo-row img { max-height: 48px; width: auto; margin: auto; filter: grayscale(1); opacity: 0.75; }
   ```
4. Weniger als fünf Logos? Überzählige Kästen löschen, das Raster passt sich an.
5. Jedes Logo in `assets/BILDER.md` eintragen (Quelle, Freigabe vom …).
6. Platzhalter-Kommentar löschen.

## Fertig, wenn
- [ ] Nur freigegebene Logos, alle mit `alt`-Text
- [ ] In `assets/BILDER.md` eingetragen
- [ ] Desktop und Handy geprüft
