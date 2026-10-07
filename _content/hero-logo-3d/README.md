# 3D-Logo im Hero der Startseite

Glänzendes, schwebendes Objekt über der Eyebrow auf `index.html`, nach dem Vorbild von ai.qestit.com.

- **Ablauf:** IDLE (Logo schwebt, 3–6 s) → SENTIENT (zufällige Geste: Herzschlag, Einatmen, Hüpfen,
  Kopfschütteln) → OUT (federnder Spin zur nächsten Form) → SHIFTED (2,6–3,8 s) → weiter zur nächsten Form.
  Jeder dritte Wechsel führt per BACK zurück zum Logo (`LOGO_EVERY`), also Logo → Form → Form → Logo
- **Hover (nur Maus):** die Form zersplittert unter dem Cursor (Dreiecke springen entlang ihrer Flächen heraus, wie bei Qestit), kein Formwechsel
- **Klick/Tap:** im Ruhezustand Erschrecken, während der Geste sofort Wechsel, bei neuer Form direkt zur nächsten,
  während eines Spins ignoriert
- **Easter Egg:** fünf Klicks aufs Icon innerhalb von zwei Sekunden lassen feine grüne Linien vom Icon aus
  über den Bildschirm laufen und wieder verblassen (`EGG_*` im `CONFIG`-Block)
- **Farbe:** in Ruhe Grundfarbe, beim Wechsel Verlauf; zwei farbige Punktlichter driften und folgen der Maus leicht

- **Formen:** `assets/hero-shapes/<name>.svg`
- **Reihenfolge, Farben:** Attribute am `<div class="hero-logo3d">` in `index.html`
  (`data-shapes`, `data-colors` = Grund- → Verlaufsfarbe, `data-light-colors` = Punktlichter)
- **Code:** `hero-logo-3d.js` hier, ausgeliefert als Bündel `js/hero-logo-3d.js` (Three.js selbst gehostet, kein CDN)
- **Fallback:** Bei reduzierter Bewegung, ohne WebGL oder bis das 3D-Bild steht, ist das statische `favicon.svg` zu sehen.
  Das Bündel (~160 KB gzip) lädt erst nach dem `load`-Event der Seite.

## Neue Form hinzufügen (ohne Build)

1. SVG nach `assets/hero-shapes/` legen, z. B. `stern.svg`:
   - einfarbig gefüllt (`fill`), **keine Linien** (`stroke` wird ignoriert)
   - nur geschlossene Pfade; Löcher als zweiter Teilpfad mit `fill-rule="evenodd"`
   - Teile nicht überlappen lassen, sonst flackern die Flächen
   - Größe egal, die Form wird automatisch zentriert und auf gleiche Größe gebracht
   - **Weiß gefüllte Pfade** (`fill="#fff"`) werden zur erhabenen Einlage auf der Vorderseite,
     mit `fill-opacity` unter 1 halbtransparent und flacher. So ist `logo.svg` gebaut:
     grüne Kachel, weißes N, X-Strich mit `fill-opacity="0.3"` wie im Hauptlogo
2. In `index.html` den Namen in `data-shapes` eintragen. Die erste Form ist das Hauptlogo, die übrigen kommen
   bei den ersten Wechseln in dieser Reihenfolge, danach zufällig. Wirkt eine Form zu groß oder zu klein,
   eigene Größe anhängen: `data-shapes="logo, lupe, sprechblase, blitz, stern:0.9"`
3. Lokal ansehen (`python3 -m http.server 8000`). Eine fehlende oder kaputte Form wird übersprungen,
   der Hinweis steht in der Browser-Konsole.

## Code ändern (mit Build)

```bash
cd _content/hero-logo-3d
npm install      # einmalig, holt three und esbuild
npm run build    # schreibt ../../js/hero-logo-3d.js
```

Alle Zeiten, Amplituden und Lerp-Faktoren stehen im `CONFIG`-Block oben in `hero-logo-3d.js`.
Zum Feintuning am ehesten: `HOVER_AMP`/`HOVER_FLOW` (wie weit die Splitter herausspringen und zittern), `IDLE_MIN`/`IDLE_MAX` (wie oft etwas
passiert), `SPIN_FREQ`/`POP_FREQ` (Überschwingen), `LIGHT_INTENSITY` (wie stark die Punktlichter färben),
`TESSELLATE_EDGE` (Größe der Splitter: größer = lange Scherben, kleiner = feiner Bruch).

**Testen:** `python3 -m http.server 8000` im Website-Ordner, http://localhost:8000 mit Cmd+Shift+R laden.
Reduzierte Bewegung prüfen: macOS-Einstellungen → Bedienungshilfen → Anzeige → „Bewegung reduzieren“,
dann bleibt das statische Logo stehen.
