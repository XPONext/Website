# 16 · 3D-Logo im Hero abschließen

**Status:** offen · **Art:** Technik · **Platzhalter:** keiner

## Stand
Das 3D-Logo (N, Lupe, Sprechblase, Blitz) läuft lokal. Code und Anleitung: `_content/hero-logo-3d/README.md`.
Noch nicht committet (Branch `website-aufraeumen`).

## Umsetzung
1. **Handy prüfen:** Seite lokal starten, in Chrome DevTools (Cmd+Alt+I → Gerätesymbol) iPhone- und
   Android-Größe ansehen. Prüfen: Größe des Logos, kein Überlappen mit der Eyebrow, Tap löst Geste/Wechsel aus.
   Besser zusätzlich auf einem echten Handy im selben WLAN: `http://<IP-des-Macs>:8000`.
2. **Reduzierte Bewegung prüfen:** macOS-Einstellungen → Bedienungshilfen → Anzeige → „Bewegung reduzieren“.
   Es muss das statische Logo stehen bleiben.
3. **Ladezeit prüfen:** Lighthouse in Chrome (DevTools → Lighthouse → Mobile). Das Bündel (~160 KB gzip)
   lädt nach dem `load`-Event und sollte LCP nicht verschlechtern. Vorher/Nachher-Wert notieren.
4. **Feintuning** bei Bedarf über den `CONFIG`-Block in `_content/hero-logo-3d/hero-logo-3d.js`,
   danach `npm run build` in diesem Ordner.
5. **Committen und pushen:** neue Dateien `assets/hero-shapes/`, `js/hero-logo-3d.js`,
   `_content/hero-logo-3d/` (ohne `node_modules`, steht in `.gitignore`) plus Änderungen an
   `index.html`, `css/site.css`, `README.md`, `.gitignore`. Danach PR von `website-aufraeumen` nach `main`.

## Fertig, wenn
- [ ] Handy, reduzierte Bewegung und Lighthouse geprüft
- [ ] Committet, PR gemergt, live auf xponext.de angesehen
