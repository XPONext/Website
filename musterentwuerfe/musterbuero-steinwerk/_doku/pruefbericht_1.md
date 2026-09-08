# Prüfbericht Steinwerk Planungsgesellschaft mbH — 2026-09-08

**Ergebnis:** nicht abgenommen (1 Blocker, 14 Warnungen)

Werkzeuge: `tools/website_qualitaet` (referenz: true, url_praefix `/referenzen/steinwerk-planung`) → 12 Seiten, 15 Prüfungen ok, 0 Blocker, 2 Warnungen. `tools/website_screenshot` lokal (localhost:8765) → 36 Screenshots unter `_doku/screenshots/pruefung/`, keine Fehler. Zusätzlich Playwright-Prüfung (JS aus/an, Tastatur, Tap-Ziele) und Sichtung aller 20 Quellbilder in `assets/bilder/projekte/` sowie der ausgelieferten Kachel-Zuschnitte.

## Blocker

1. Checkliste 5 (Referenzseiten: kein erkennbares reales Gebäude als eigenes Projekt) — `assets/bilder/projekte/sporthalle-01.webp` (Pexels 1091435, Artem Saranin) zeigt das **Stadion Kaliningrad** (WM-Stadion 2018, ca. 35.000 Plätze; weiß-petrol gestreifte Schüssel mit Mastreihe auf dem Dach, Fotograf aus Kaliningrad). Es steht als „Sporthalle Wesseling · 2025 · Neubau · Foto" in Reihe 1 des Rasters (`01_start_desktop_hero.jpg`, dritte Kachel), auf `/projekte/gewerbe/` als erste Kachel (`05_projekte-gewerbe_desktop_hero.jpg`) und in der Tabelle als Nr. 03. Bild ersetzen; Alt-Text, Tabelle, `BILDER.md` und Bildnachweis-Seite nachziehen.

## Warnungen

1. Checkliste 5 / Bildplausibilität (nicht in Checkliste als eigener Punkt) — `verwaltungszentrum-01.webp` (Pexels 29913723, „modern university campus at sunset", Yusuf Çelik) zeigt einen Universitätscampus mit Emblem auf dem Torbau und Nationalflaggen im Vordergrund (im 900-px-Zuschnitt beides sichtbar). Als „Verwaltungszentrum Aachen · Wettbewerb, 1. Preis, realisiert · Foto" ausgegeben. Ich kann die Anlage nicht benennen, deshalb kein Blocker — aber Emblem und Flaggen machen sie identifizierbar. Ersetzen.
2. Bildplausibilität — `berufskolleg-01.webp` (Pexels 38235442, „historic colonial building", Sharath G.) zeigt einen verfallenen Kolonialbau mit Arkaden, tropischen Bäumen, Sandstraße und lesbarem Schild links unten (auch im Kachelzuschnitt sichtbar, `03_projekte-bildung_desktop_hero.jpg`, vierte Kachel). Als „Berufskolleg Süd, Bonn · 2022 · Sanierung · Foto" nicht glaubhaft — ein Vergabereferent sieht auf den ersten Blick, dass das nicht Bonn ist. Gebäude nicht benennbar, daher kein Blocker. Ersetzen.
3. Bildplausibilität / lesbare Kennzeichen — `feuerwache-01.webp`: das obere Sechstel mit „Bomberos de …" ist laut `BILDER.md` weggeschnitten, aber im Kachelzuschnitt bleiben Wappen der Feuerwehr auf der Tür, Fahrzeugnummer „58", Funkrufname „11-2" und eine Web-Adresse auf der Fahrertür lesbar (`kacheln/feuerwache-01-900.webp`). Ein spanischsprachiges Einsatzfahrzeug als „Feuerwache Bergisch Gladbach". Ersetzen oder Ausschnitt ohne Fahrzeug wählen.
4. Bildplausibilität / lesbare Schrift — `mensa-01.webp`: trotz Mittenbeschnitt bleiben chinesische Wandtexte links und rechts im Kachelzuschnitt sichtbar (`kacheln/mensa-01-900.webp`, `03_projekte-bildung_desktop_full.jpg` Reihe 2, erste Kachel). Als „Mensa Gymnasium Brühl · Neubau · Foto" nicht glaubhaft.
5. Projekttext passt nicht zum Bild (nicht in Checkliste) — „Schulzentrum Kerpen · 2026 · Wettbewerb, Anerkennung" trägt in Tabelle und Alt-Text die Bildart „Foto: Luftbild eines Schulgeländes". Eine Anerkennung 2026 ist nicht gebaut; ein Foto des fertigen Geländes widerspricht dem Text und genau der Ehrlichkeit, die Brief Abschnitt 8 und die Büro-Seite („Renderings und Modellfotos kennzeichnen wir") versprechen. Das ist Kachel 01, die erste im Raster (`01_start_desktop_hero.jpg`). Entweder Ergebnis auf „1. Preis, realisiert" mit passendem Jahr oder Bild als Modell/Rendering.
6. Brief-Treue Abschnitt 8 / F16 — Der Brief legt 8 Fotos, 6 Renderings, 6 Baustellenfotos fest und verlangt den Chip „Rendering". Gebaut sind 14 Foto, 2 Modell, 4 Baustelle, 0 Rendering; die Wettbewerbsergebnisse sind gegenüber dem Brief vertauscht (Kerpen: Brief „1. Preis" → Seite „Anerkennung"; Aachen: Brief „Anerkennung" → Seite „1. Preis, realisiert"). Die Kennzeichnung selbst funktioniert (Chip unter dem Bild, Spalte „Abbildung" für alle 20), aber die im Brief begründete Ordnung „Renderings 2025/2026 oben, Baustellen 2019/2020 unten" existiert so nicht mehr — oben stehen jetzt drei Fotos, davon eines (Nr. 03) das Stadion aus dem Blocker. Bitte den Brief-Abschnitt 8 oder die Projektdaten angleichen.
7. Checkliste 6 (Mobil: nichts überlappt) — Im geöffneten Mobil-Menü überlappt der Text „Schließen" die Wortmarke „Steinwerk" (Playwright-Aufnahme bei 390 px, geöffneter Zustand; Kopfzeile: „Schließe**S**teinwerk"). Zudem sitzt „Menü" nicht links am Rand (Brief 7: „links Menü, mittig Wortmarke"), sondern bei etwa x = 220 von 390 — die Kopfzeile ist rechtslastig (`01_start_mobile_full.jpg`, Kopfzeile bei y ≈ 2 380 im Vollbild).
8. Brief 7 (Mobil-Menü: „Fokus bleibt im Menü") — Playwright: nach den sechs Menüeinträgen wandert der Tab-Fokus aus dem geöffneten Vollbildmenü auf „Köln · 0221 …" und „Alle (20)" der dahinterliegenden Seite. Kein Fokus-Trap. Escape und Schließen-nach-Auswahl funktionieren.
9. Brief 5 (Filterleiste mobil) / Sichtbarkeit des aktiven Zustands (nicht in Checkliste) — Die Filterzeile scrollt horizontal ohne Scrollbar (scrollWidth 602 px bei 358 px Sichtbreite). Auf `/projekte/gewerbe/` und `/projekte/wettbewerbe/` liegt der **aktive** Eintrag außerhalb des Sichtfelds, sichtbar sind nur „Alle · Bildung · Verwaltung" (`05_projekte-gewerbe_mobile_full.jpg`, `06_projekte-wettbewerbe_mobile_full.jpg`). Der Nutzer sieht nicht, welcher Filter aktiv ist. Aktiven Eintrag per `scrollIntoView` einrücken oder Zeile umbrechen lassen.
10. Brief 6 / F5 (Filterseiten: „Raster, darunter die Tabelle derselben n Projekte") — Mit JavaScript blendet `data-ansicht="raster"` die Tabelle auf den Filterseiten aus; sie erscheint erst über den Umschalter (`03_projekte-bildung_desktop_full.jpg` zeigt nur das Raster). Ohne JavaScript stehen beide untereinander, wie im Brief. Bewusste Abweichung oder Versehen — bitte entscheiden und Brief/Seite angleichen.
11. Brief 8 / F3-Bedingung (Kacheln „jeweils unter 60 KB") — Die 600-px-Kacheln halten das ein, 10 der 20 900-px-Kacheln liegen zwischen 75 und 118 KB (`buero-kalk-01-900.webp` 118 KB, `produktionshalle-01-900.webp` 92 KB, `grundschule-ring-01-900.webp` 88 KB …). `BILDER.md` der Seite nennt „≤ 114 KB", der Brief 60 KB. Startseite bleibt mit 937 KB deutlich unter 1,5 MB; Retina-Mobil lädt aber ~1,6 MB Bilder.
12. Checkliste 1 (Fonts) — Tool: 8 woff2-Dateien, Grenze 5. Zwei davon sind `ibm-plex-mono-400-italic-*`, obwohl der Brief „keine Kursive auf der ganzen Seite" festlegt; geladen werden zur Laufzeit nur 3 Familien-Schnitte (Inter, Plex 400, Plex 500), die Italic-Dateien liegen ungenutzt im Ordner und in `@font-face`. Entfernen, dann sind es 6 — Latin-Ext-Dateien kosten ebenfalls, prüfen ob nötig.
13. Checkliste 1 (Bilder WebP) — Tool: `assets/bilder/og.jpg` (152 KB) ist kein WebP. Für Open-Graph-Vorschauen ist JPEG üblich; Hinweis übernommen, kein Handlungsbedarf.
14. Bildnachweis-Seite mobil (nicht in Checkliste) — Die vierspaltige Tabelle wird bei 390 px im eigenen Container abgeschnitten (Spalten Fotograf/Quelle nur per Scroll im Container erreichbar, kein Hinweis darauf; `12_bildnachweis_mobile_full.jpg`). Kein Seiten-Querscroll (390/390), also kein Blocker.

Geprüft und ohne Befund (Auszug, jeweils mit Beleg):
- Kein Preloader, kein Intro, keine Animation; `prefers-reduced-motion` setzt Übergänge auf 0,01 ms (`basis.css` Z. 321).
- Alle Schriften self-hosted, 0 Fremd-Domains auf allen 12 Seiten (Screenshot-Messung), keine Cookies, kein Storage (Playwright: 0/0), kein Formular (Kontakt per `mailto:`-Button), Datenschutzerklärung beschreibt genau das.
- `lang="de"`, Skip-Link „Zum Inhalt springen" ist erstes fokussierbares Element, sichtbar bei Fokus (Playwright: `left: 0`, Outline 3 px `#2B5876`); genau eine H1 je Seite; Überschriftenfolge ohne Sprung (Startseite h1 → h2 sr-only → h3).
- Fokusring: 3 px Stahlblau mit 3 px Abstand auf hellem Grund (Skip-Link, Telefon-Link in Kopfzeile) und auf dem gefüllten Akzent-Button der Kontaktseite — dort hebt der Offset den Ring vom gleichfarbigen Button ab (`fokus_knopf.jpg`, Playwright).
- Menü-Button mit `aria-expanded`/`aria-controls`, Escape schließt und setzt den Fokus auf den Button, Liste schließt nach Auswahl (Playwright: `/leistungen/`, `aria-expanded="false"`).
- Tap-Ziele: alle Links/Buttons ≥ 44 px hoch (Playwright Desktop und Mobil, einziger Treffer „Büro" im Footer 33 px breit bei 44 px Höhe).
- Text auf Bild: keiner. Chips liegen unter dem Bild.
- Kontrast: Werte laut Brief gerechnet; inaktive Filter `rgb(91,98,105)` = `#5B6269` auf `#EDEFF0` (5,36:1), gemessen per Playwright.
- Hover trägt keine Information (Kacheltitel und Metazeile dauerhaft sichtbar, `opacity: 1`).
- `title` ≤ 65, `description` ≤ 160, je Seite unterschiedlich; `canonical`, `og:*`, `noindex, follow` auf allen 12 Seiten; `sitemap.xml` mit `url_praefix` vollständig (10 URLs, ohne Impressum/Datenschutz); `robots.txt` erlaubt GPTBot, ClaudeBot, PerplexityBot; JSON-LD `ArchitectOffice` mit Adresse, Telefon, `areaServed`; Ortsbezug „Rheinland"/„Köln" sichtbar im Statement und Metadatenblock; sprechende Ordner-URLs.
- Impressum: § 5 DDG, Kammer (AKNW), Berufsbezeichnung, Berufshaftpflicht, USt-IdNr., Absatz „fiktiv" (`10_impressum_desktop_full.jpg`); Demo-Hinweis in der Fußzeile jeder Seite; Bildnachweis-Seite von der Fußzeile verlinkt.
- `BILDER.md`: alle 20 Quellbilder mit Fotograf, Pexels-URL, Lizenz; abgeleitete Dateien (Kacheln 600/900, Büro-Bild 1320, og.jpg, icon.svg) in `assets/bilder/BILDER.md`. Jede im HTML referenzierte Bilddatei ist belegt. Keine Personen im Bild, keine Portraits als Team.
- Mobil: kein Querscroll auf allen 12 Seiten (Messung), Hero-Text 32 px lesbar, erste Kachel bei y = 613 von 844 sichtbar, Tabelle als gestapelte Blöcke mit „·"-Trennern, alle sieben Angaben lesbar (`mob_tabelle.jpg`).
- Filter ohne JS: fünf Links auf statische Seiten, `aria-current="page"` auf dem aktiven; ohne JS ist „Menü" ein Anker auf die Fußzeilen-Navigation. Mit JS: Buttons mit `aria-pressed`, Filtern ohne Seitenwechsel (Gewerbe → 5 Kacheln, URL per `replaceState` auf `/projekte/gewerbe/`), Umschalter `[x] Liste` blendet Tabelle ein (`js_liste_gewerbe.jpg`).
- Render-blockendes JS: nur ein 1-Zeilen-Inline-Script (`.js`-Klasse), `basis.js` mit `defer`.

## Messwerte

| Seite | Transfer | davon Bilder | LCP (lokal) | Fremd-Domains | Mobil-Querscroll |
|---|---|---|---|---|---|
| / | 937 KB | 810 KB | 84 ms | 0 | nein |
| /projekte/ | 126 KB | 0 | 28 ms | 0 | nein |
| /projekte/bildung/ | 438 KB | 323 KB | 48 ms | 0 | nein |
| /projekte/verwaltung/ | 288 KB | 177 KB | 36 ms | 0 | nein |
| /projekte/gewerbe/ | 300 KB | 188 KB | 56 ms | 0 | nein |
| /projekte/wettbewerbe/ | 233 KB | 123 KB | 36 ms | 0 | nein |
| /buero/ | 228 KB | 119 KB | 20 ms | 0 | nein |
| /leistungen/ | 98 KB | 0 | 24 ms | 0 | nein |
| /kontakt/ | 106 KB | 0 | 24 ms | 0 | nein |
| /impressum/ | 97 KB | 0 | 24 ms | 0 | nein |
| /datenschutz/ | 99 KB | 0 | 20 ms | 0 | nein |
| /bildnachweis/ | 111 KB | 0 | 32 ms | 0 | nein |

Startseite: 20 Bilder, alle mit `alt`, `width`/`height`; erstes Bild `fetchpriority="high"`, 19 × `loading="lazy"`; 3 Font-Schnitte geladen (Inter variabel, Plex Mono 400/500), Inter per `preload`. Statement gemessen: 52 px / 500 / −1,3 px / 56 px Zeilenhöhe, 1.016 px breit, 3 Zeilen. Raster `296px × 4`, Kachelbild 296 × 197, Oberkante bei y = 598 (Brief: ≈ 380 — Metadatenblock und Abstände sind höher als geplant, erste Reihe trotzdem im 900-px-Hero sichtbar). Kopfzeile `sticky`, deckend.

## Brief-Treue

| Feature-ID | umgesetzt | Beleg (Screenshot) |
|---|---|---|
| wolveridge-com-au-F3 Projektraster feste Kachelbreite (4 Spalten, Gasse 64) | ja | `01_start_desktop_full.jpg` (4 × 5 Kacheln 296 px, gemessen `296px 296px 296px 296px`); 900-px-Kacheln über 60 KB → Warnung 11 |
| wolveridge-com-au-F4 Titel + Metazeile „Nr · Ort · Jahr · Maßnahme", Jahr absteigend | ja | `01_start_desktop_hero.jpg`: „01 · KERPEN · 2026 · WETTBEWERB, ANERKENNUNG"; Sortierung 2026 → 2019 in `02_projekte_desktop_full.jpg` |
| wolveridge-com-au-F5 Listenansicht als Tabelle mit Linien, mobil gestapelt | ja | `02_projekte_desktop_full.jpg` (7 Spalten, Hairlines, nicht verlinkt); `02_projekte_mobile_full.jpg`, `mob_tabelle.jpg`; auf Filterseiten mit JS nur per Umschalter → Warnung 10 |
| wolveridge-com-au-F2 Umschalter `[x] Raster [ ] Liste` | ja | `01_start_desktop_hero.jpg` rechts in der Filterzeile; ohne JS Links (`/projekte/`), mit JS Buttons `aria-pressed` (`js_liste_gewerbe.jpg`) |
| wolveridge-com-au-F16 Renderings und Fotos im selben Raster, Kennzeichnung | teilweise | Chips „MODELL"/„BAUSTELLE" unter dem Bild (`01_start_desktop_full.jpg` Reihen 3–5), Spalte „Abbildung" in der Tabelle; **kein** Rendering und kein Chip „Rendering" mehr auf der Seite, Bildverteilung weicht vom Brief ab → Warnung 6 |
| wolveridge-com-au-F7 Mono für Daten, Grotesk für Sprache | ja | `01_start_desktop_hero.jpg`: Statement/Titel Inter, Metazeile/Filter/Telefon IBM Plex Mono (Playwright: `font-family: "IBM Plex Mono"` auf Filtern) |
| wolveridge-com-au-F8 Drei Farbwerte, Grau = inaktiv | ja | Filterzeile: aktiv `#15181B` 500, inaktiv `#5B6269` 400 (Playwright `filter_farben`); `01_start_desktop_hero.jpg` |
| wolveridge-com-au-F1 Kopfzeile Dreiteilung, rechts „Köln · Telefon" | ja | `01_start_desktop_hero.jpg` Kopfzeile: Wortmarke / Projekte Leistungen Büro Kontakt / „KÖLN · 0221 55 44 33-0" |
| wolveridge-com-au-F10 Mobile Vollbildmenü | ja, mit Mängeln | `mob_menu.jpg`: Vollbild in Grundfarbe, 4 Einträge à 32 px mit Hairlines, Telefon/E-Mail darunter; Überlappung „Schließen/Steinwerk" → Warnung 7, kein Fokus-Trap → Warnung 8 |
| big-dk-F1 Hierarchie ohne Bold | ja | kein Gewicht über 500 gemessen (H1 500, Body 400, `strong` = 500 in CSS); `07_buero_desktop_full.jpg` |
| big-dk-F2 Metadatenblock rechtsbündig | ja | `01_start_desktop_hero.jpg` rechts „STANDORT Köln / TEAM 14 / PROJEKTE 20 / WETTBEWERBE 3"; `07_buero_desktop_hero.jpg` „GEGRÜNDET 2011 …" |
| big-dk-F3 Gemeinsame linke Kante, nichts zentriert | ja | `01_start_desktop_full.jpg`: Statement, Filter, Raster, Fußzeile auf einer Kante bei 32 px |
| big-dk-F4 Ort in Versalien in der Metazeile | ja | „04 · KÖLN-EHRENFELD · 2024 · …" (`01_start_desktop_hero.jpg`) |
| helenhard-no-F8 Filterleiste nach Typologie mit Anzahl | ja | `01_start_desktop_hero.jpg`: „ALLE (20) · BILDUNG (8) · VERWALTUNG (4) · GEWERBE (5) · WETTBEWERB (3)"; ohne JS statische Seiten (`03_…`–`06_…`); mobil aktiver Eintrag außer Sicht → Warnung 9 |
| helenhard-no-F9 Label-Wert-Tabelle mit Hairlines | ja | `07_buero_desktop_full.jpg` „Büro in Zahlen" (8 Zeilen); `08_leistungen_desktop_full.jpg` (5 Leistungsfelder als Hairline-Zeilen) |
| helenhard-no-F13 Footer mit Standortblock | ja | `02_projekte_desktop_full.jpg` Fußzeile: Standort / Navigation / Rechtliches / Projekte nach Typ, Demo-Hinweis |

**Wow-Faktor** (Satz in Inter 52/500 statt Hero-Bild, darunter 4 × 5-Raster mit Mono-Metazeile): auf `01_start_desktop_hero.jpg` klar erkennbar — Statement in drei Zeilen, Metadatenblock rechts, Filterzeile, erste Kachelreihe vollständig im 900-px-Ausschnitt.

**Abschnitt 10 („bewusst nicht")**: nichts davon verbaut — keine Projekt-Detailseiten, keine Auszeichnungstabelle, keine Portraits, kein zentriertes Mono-Intro, kein Laufband, kein Minimal-Footer, kein Preloader, keine Serife, keine warme Palette, keine Newsliste, kein Hero-Bild/Video, kein Slider, kein Parallax, keine Google Fonts, kein Text auf Bild, kein Hover als Informationsträger, keine dunkle Sektion (Fußzeile hell auf `#E0E4E7`).

**Nachbildungs-Vergleich**: Am nächsten liegt wolveridge.com.au (Raster + Tabelle + `[x] GRID / [ ] LIST`-Umschalter + Mono-Unterschriften + Kopfzeile mit Ort). Steinwerk setzt dagegen: Statement als H1 statt sofortigem Raster, Metadatenblock rechts, Filterzeile, 4 statt 3 Spalten, linksbündig statt zentriert, deckend-sticky Kopfzeile, voller Footer mit Rechtstexten, kühles Grau statt Weiß. Keine Nachbildung. big.dk (Signets, endlose Einspaltenliste) und helenhard.no (Serife, Video-Hero, Skizzen) sind nur in Einzelmustern wiederzuerkennen. Gegen Nordkant (Fraunces, warmes Off-White, randloses Hero-Foto) und Lindenau (Cormorant, Kohle-Dunkel, große Einzelbilder) ist Steinwerk auf den ersten Blick unterscheidbar (`ref_fulls`-Vergleich: nordkant `01_start_desktop_full.jpg`, studio-lindenau `01_start_desktop_full.jpg`).

## Was gut ist

1. **Filter und Umschalter in zwei Schichten**: ohne JavaScript fünf statische Filterseiten plus `/projekte/` mit `aria-current`, mit JavaScript Buttons mit `aria-pressed`, In-Place-Filtern und `replaceState` auf dieselben URLs. Das ist robust, verlinkbar und barrierefrei — nicht anfassen.
2. **Das Statement als Hero trägt.** 52 px Inter 500 mit −0,025 em, drei Zeilen über drei Rasterspalten, rechts der Metadatenblock, darunter die erste Kachelreihe im 900-px-Ausschnitt: der erste Bildschirm sieht aus wie ein Projektverzeichnis, genau wie im Brief beschrieben. Kein Bild, keine Bewegung, 84 ms LCP.
3. **Rechtstexte und Technik passen zusammen.** Datenschutzerklärung beschreibt eine Seite ohne Cookies, ohne Fremdserver, mit `mailto:` statt Formular — und genau das ist gemessen (0 Fremd-Domains, 0 Cookies, 0 Storage). Impressum mit Kammer, Berufsbezeichnung, Berufshaftpflicht, Absatz „fiktiv"; Demo-Hinweis in jeder Fußzeile; Bildnachweis als eigene Seite mit Pexels-URL je Datei.

## Gesichtete Screenshots

`_doku/screenshots/pruefung/` (36 Dateien, alle angesehen):
01_start_desktop_hero, 01_start_desktop_full, 01_start_mobile_full (Vollbild bei 6.000 px abgeschnitten, Fußzeile auf den Filterseiten geprüft) · 02_projekte_desktop_hero, 02_projekte_desktop_full, 02_projekte_mobile_full · 03_projekte-bildung_desktop_hero, 03_projekte-bildung_desktop_full, 03_projekte-bildung_mobile_full · 04_projekte-verwaltung_desktop_hero, 04_projekte-verwaltung_desktop_full, 04_projekte-verwaltung_mobile_full · 05_projekte-gewerbe_desktop_hero, 05_projekte-gewerbe_desktop_full, 05_projekte-gewerbe_mobile_full · 06_projekte-wettbewerbe_desktop_hero, 06_projekte-wettbewerbe_desktop_full, 06_projekte-wettbewerbe_mobile_full · 07_buero_desktop_hero, 07_buero_desktop_full, 07_buero_mobile_full · 08_leistungen_desktop_hero, 08_leistungen_desktop_full, 08_leistungen_mobile_full · 09_kontakt_desktop_hero, 09_kontakt_desktop_full, 09_kontakt_mobile_full · 10_impressum_desktop_hero, 10_impressum_desktop_full, 10_impressum_mobile_full · 11_datenschutz_desktop_hero, 11_datenschutz_desktop_full, 11_datenschutz_mobile_full · 12_bildnachweis_desktop_hero, 12_bildnachweis_desktop_full, 12_bildnachweis_mobile_full.

Hinweis zu den Vollbild-Aufnahmen: die sticky Kopfzeile erscheint im Vollbild-Screenshot einmal mitten auf der Seite (z. B. `01_start_mobile_full.jpg` bei y ≈ 2 380) — Artefakt des Screenshot-Tools bei `position: sticky`, im Browser nicht reproduzierbar, kein Befund.

Zusätzliche Playwright-Aufnahmen (Scratchpad, nicht im Site-Ordner): `mob_menu.jpg` (Menü offen, 390 px), `mob_tabelle.jpg` (Tabelle 390 px), `js_liste_gewerbe.jpg` (Filter Gewerbe + Liste, JS), `fokus_kontakt.jpg`, `fokus_knopf.jpg`.

Quellbilder: alle 20 Dateien in `assets/bilder/projekte/` in voller Größe gesichtet, dazu die 900-px-Kachelzuschnitte von feuerwache, mensa, berufskolleg, sporthalle, verwaltungszentrum, buergerhaus, quartiersschule, kita-sonnenhang.

Referenzen: wolveridge-com-au `01_start_desktop_hero`, `01_start_desktop_full`, `04_start-list_desktop_hero`, `04_start-list_desktop_full`; big-dk `01_start_desktop_hero`, `01_start_desktop_full`; helenhard-no `01_start_desktop_hero`, `01_start_desktop_full`; nordkant-architekten `final/01_start_desktop_full`; studio-lindenau `final/01_start_desktop_full`.
