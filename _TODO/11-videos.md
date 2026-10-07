# 11 · Videos „Vorstellung“ und „Über uns“

**Status:** offen · **Wartet auf:** Dreh
**Schließt:** `Video Vorstellung` in `index.html`, `Video Über uns` in `ueber-uns.html`

## Ziel
Ein Video von 60–90 Sekunden: wer wir sind, wie wir arbeiten. Ein Video kann beide Stellen bedienen.
**Selbst gehostet, kein YouTube/Vimeo**: kein Drittanbieter, kein Cookie-Banner-Thema.

## Umsetzung
1. Drehen (Handy reicht, Querformat 16:9, Ansteckmikro). Gliederung: wer wir sind → für wen → wie ein
   Projekt abläuft → Einladung zum Erstgespräch.
2. Untertitel als `.vtt` schreiben (Barrierefreiheit, viele schauen ohne Ton).
3. Komprimieren, Ziel unter 15 MB (GitHub Pages erlaubt Dateien bis 100 MB, die Seite soll aber schnell bleiben):
   ```bash
   ffmpeg -i roh.mov -vf scale=1280:-2 -c:v libx264 -crf 26 -preset slow -c:a aac -b:a 96k -movflags +faststart assets/video/vorstellung.mp4
   ffmpeg -i assets/video/vorstellung.mp4 -ss 3 -frames:v 1 -q:v 3 assets/video/vorstellung.jpg
   ```
4. Kasten ersetzen:
   ```html
   <video controls preload="none" playsinline poster="/assets/video/vorstellung.jpg" width="1280" height="720" style="border-radius:var(--radius);margin-top:1.4rem">
     <source src="/assets/video/vorstellung.mp4" type="video/mp4">
     <track kind="captions" src="/assets/video/vorstellung.de.vtt" srclang="de" label="Deutsch" default>
   </video>
   ```
   `preload="none"`, damit das Video erst beim Klick lädt.
5. Optional für SEO: `VideoObject`-Schema auf der Startseite ergänzen.

## Fertig, wenn
- [ ] Video an beiden Stellen, mit Untertiteln und Vorschaubild
- [ ] Datei unter 15 MB, lädt erst beim Abspielen
