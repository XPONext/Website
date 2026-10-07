# 10 · Teamfoto aus dem Shooting

**Status:** offen · **Wartet auf:** Fotoshooting · **Schließt:** `Teamfoto Shooting` in `index.html`

## Ziel
In der Team-Section der Startseite („Wer steckt hinter XPONext?“) ein echtes Arbeitsfoto: Tim und
Simon im Gespräch mit einem Kunden oder bei der Arbeit. Kein zweites Freisteller-Porträt, das gibt es
schon im Hero.

## Umsetzung
1. Foto im Querformat 4:3, mindestens 1600 × 1200 px. Mit Fotograf schriftlich klären: Nutzungsrecht
   für Website und Social Media, Namensnennung ja/nein. Abgebildete Kunden brauchen eine Einwilligung.
2. Als WebP speichern: `cwebp -q 80 foto.jpg -resize 1600 0 -o assets/team/arbeit.webp`
3. Kasten ersetzen:
   ```html
   <img src="/assets/team/arbeit.webp" alt="Tim Bünger und Simon Meding im Gespräch mit einem Kunden" width="1600" height="1200" loading="lazy" style="border-radius:var(--radius-lg);aspect-ratio:4/3;object-fit:cover">
   ```
4. In `assets/BILDER.md` eintragen (Fotograf, Datum, Rechte).
5. Optional: Mit dem Foto auch `assets/og-image.jpg` erneuern (1200 × 630 px).

## Zusätzlich: Einzelporträt Simon
Auf `ueber-uns.html` (Karte „Wer macht was?“) steht übergangsweise `assets/team/simon-karte.webp`,
ein Ausschnitt aus dem Teamfoto. Beim Shooting ein Einzelporträt im Stil von `tim.webp` machen
(Querformat, Büro im Hintergrund), als `assets/team/simon.webp` speichern und auf der Karte die Klasse
`person-card__img--frei` entfernen.

## Fertig, wenn
- [ ] Foto eingebaut, Rechte schriftlich geklärt und in `BILDER.md` dokumentiert
