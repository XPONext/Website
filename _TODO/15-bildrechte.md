# 15 · Bildrechte bestätigen

**Status:** offen · **Art:** Recht · **Platzhalter:** keiner (`assets/BILDER.md`)

## Problem
In `assets/BILDER.md` stehen die Teamfotos (`team.webp`, `tim.webp`, `simon.webp`) mit Rechten
**„zu bestätigen“**. Sie sind prominent eingebunden (Hero, Über uns, Leistungs- und Branchenseiten).

## Umsetzung
1. Klären, wer die Fotos gemacht hat und ob ein Nutzungsrecht für Website und Werbung vorliegt.
   Bei Fremdfotografen: schriftliche Bestätigung, ggf. Namensnennung.
2. In `assets/BILDER.md` „zu bestätigen“ durch die Angabe ersetzen (Fotograf, Datum, Umfang).
3. Wenn keine Rechte zu bekommen sind: durch Fotos aus dem neuen Shooting ersetzen (Ticket 10).
4. Bei der Gelegenheit nicht mehr eingebundene Dateien löschen (`assets/team.png`,
   `assets/team/tim.jpg`, `assets/team/simon.jpg`, `assets/google-ads-badge.png`). Vorher mit
   `grep -rn "dateiname" --include=*.html .` prüfen, dass sie wirklich nirgends verwendet werden.

## Fertig, wenn
- [ ] Kein „zu bestätigen“ mehr in `assets/BILDER.md`
