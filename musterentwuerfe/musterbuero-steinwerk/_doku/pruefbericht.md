# Prüfbericht Steinwerk Planungsgesellschaft mbH — 2026-09-08 (zweiter Durchlauf)

**Ergebnis:** abgenommen (0 Blocker, 8 Warnungen)

Werkzeuge: `tools/website_qualitaet` (referenz: true, url_praefix `/referenzen/steinwerk-planung`) → 12 Seiten, 15 Prüfungen ok, 0 Blocker, 2 Warnungen (Fonts, og.jpg). `tools/website_screenshot` lokal (localhost:8765) → 36 Screenshots unter `_doku/screenshots/pruefung2/`, 0 Fehler. Playwright-Prüfung (Mobil-Menü mit Focus-Trap, Filter mobil, Filterseiten mit JS, alles ohne JS, Tap-Ziele, Fokusring, Cookies/Storage). Sichtung der fünf Ersatz-Quellbilder in Vollgröße (1920 px) und ihrer 900-px-Kachelzuschnitte. Jeder Blocker und jede Warnung aus dem ersten Durchlauf wurde gegen den aktuellen Stand nachgeprüft (Ergebnis je Punkt im Abschnitt „Erster Durchlauf").

## Blocker

Keine.

Der Blocker des ersten Durchlaufs (Stadion Kaliningrad als „Sporthalle Wesseling") ist behoben: `sporthalle-01.webp` ist jetzt Pexels 29750394 (Jan van der Wolf) — eine beigefarbene Stehfalz-/Trapezblechfassade mit zweiflügeligem rot-blauem Tor, frontal, ohne Umfeld. Kein bekanntes Gebäude, keine Schrift, kein Wappen, keine Flagge, keine Person. Im Raster Kachel 03 (`01_start_desktop_hero.jpg`, dritte Kachel; `05_projekte-gewerbe_desktop_hero.jpg`, erste Kachel).

**Die fünf Ersatzbilder im Einzelnen (Vollgröße gesichtet):**

| Datei | Pexels | Motiv | Bekanntes Gebäude / Schrift / Wappen / Flagge / Person |
|---|---|---|---|
| sporthalle-01 | 29750394 | Beige Blechfassade, rot-blaues Tor | nein / nein / nein / nein / nein |
| verwaltungszentrum-01 | 9458996 | Schwarz-weiß, weiße Plattenfassade mit auskragendem Kubus, zwei Glasvorbauten, Tür | nein / „Bell"-Schriftzug auf einer kleinen Satellitenschüssel rechts unten (Quellbild lesbar, im 900-px-Zuschnitt ca. 15 px und nicht lesbar) / nein / nein / nein |
| berufskolleg-01 | 33470382 | Dreigeschossiger Klinkerbau mit Fensterbändern, PV auf dem Dach, blau-gelbe Fahrradüberdachung, Pausenhof | nein — typische bundesdeutsche Schule der 1970er, passt zu „Bonn, Sanierung" / nein / nein / nein / nein |
| feuerwache-01 | 15602858 | Blaue Trapezblechhalle mit grauem Rolltor, Bauzaun davor | nein / winzige gelbe Zaunetiketten, unlesbar / nein / nein / nein |
| mensa-01 | 6344447 | Blick durch schwarze Lamellen-Schiebewand in holzverkleideten Saal mit Stuhlreihen, Pflanzen, weißem Flügel | nein / nein / nein / nein / nein |

Alle fünf sind in `assets/bilder/projekte/BILDER.md` mit Fotograf, Pexels-URL und Altquelle eingetragen, auf der Bildnachweis-Seite gelistet (`12_bildnachweis_desktop_full.jpg`), Alt-Texte beschreiben das neue Motiv (geprüft in `index.html` Z. 95, 140, 145, 150, 155). Jede im HTML referenzierte Bilddatei existiert.

## Warnungen

1. Brief 8 / wolveridge-F3-Bedingung („Kacheln jeweils unter 60 KB") — Die 600-px-Kacheln halten das ein (Maximum `grundschule-ring-01-600.webp` mit 60,7 KB, also 0,7 KB drüber). Sechs 900-px-Kacheln liegen darüber: `buero-kalk-01-900` 112 KB, `produktionshalle-01-900` 87 KB, `grundschule-ring-01-900` 80 KB, `stadtwerke-01-900` 72 KB, `kita-waldstrasse-01-900` 70 KB, `berufskolleg-01-900` 67 KB. `assets/bilder/BILDER.md` nennt dafür eine eigene Grenze von 120 KB. Startseite insgesamt 869 KB (1×) — die Warnung ist eine Brief-Abweichung, kein Performance-Problem. Entweder Brief 8 auf „600 px ≤ 60 KB, 900 px ≤ 120 KB" ändern oder die sechs Motive weiter drücken.
2. Checkliste 1 (höchstens 5 woff2) — Tool: 6 Font-Dateien. Die zwei Italic-Dateien aus dem ersten Durchlauf sind weg; geblieben sind je eine `latin`- und `latin-ext`-Datei für Inter, Plex 400 und Plex 500. Zur Laufzeit lädt der Browser drei Dateien (48,7 KB, Messung auf allen 12 Seiten). Brief 3 sieht `latin-ext` ausdrücklich vor. Mit dieser Begründung stehen lassen — oder `latin-ext` streichen, wenn keine polnischen/tschechischen Ortsnamen erwartet werden (deutsche Umlaute und ß liegen in `latin`).
3. Checkliste 1 (Bilder WebP) — Tool: `assets/bilder/og.jpg` (152 KB) ist JPEG. Für Open-Graph-Vorschauen üblich, kein Handlungsbedarf.
4. Brief-Treue Abschnitte 5, 7, 8 — Der Brief ist nach der Nachbesserung nicht nachgezogen worden, die Seite weicht an drei begründeten Stellen von ihm ab: (a) Abschnitt 8 nennt 8 Fotos / 6 Renderings / 6 Baustellenfotos und den Chip „Rendering"; gebaut sind 14 Foto / 2 Modell / 4 Baustelle, Chips „Modell" und „Baustelle", kein Rendering (Tabelle `02_projekte_desktop_full.jpg`, Spalte Abbildung). (b) Abschnitt 5 verlangt die Filterleiste mobil als „eine Zeile, `overflow-x: auto`, keine drei Umbruchzeilen"; gebaut ist Umbruch in zwei Zeilen plus Umschalterzeile (`mobhero_start.jpg`, Filterhöhe 135 px), was die Warnung 9 des ersten Durchlaufs richtig behebt. (c) Abschnitt 7 beschreibt den Umschalter als Radio-Paar `[x]/[ ]`; auf den vier Filterseiten sind es jetzt zwei Sprunglinks `[x] Raster [x] Liste` auf `#raster`/`#liste` (`03_projekte-bildung_desktop_hero.jpg`). Alles drei funktioniert und ist vertretbar, aber der nächste Prüfer prüft wieder gegen den alten Brief. Bitte Brief angleichen (nicht in Checkliste, Hinweis zur Dokumentation).
5. Bildplausibilität (nicht in Checkliste) — `mensa-01`: Pexels-Titel „entrance of an empty concert hall with chairs and a piano"; im Saal stehen ein weißer Flügel und eine Sessel-Sitzgruppe, keine Tische. Als „Mensa" nur bedingt glaubhaft, als Aula/Mehrzweckraum sofort. Kein Kennzeichen, kein Blocker. Vorschlag: Titel „Mensa und Aula Gymnasium Brühl" oder Alt-Text „Speise- und Veranstaltungssaal".
6. Bildplausibilität (nicht in Checkliste) — `verwaltungszentrum-01`: „Bell"-Schriftzug auf der Satellitenschüssel rechts unten (kanadischer Telekomanbieter) ist im 1920-px-Quellbild lesbar, in den ausgelieferten 600/900-px-Kacheln nicht (`kacheln/verwaltungszentrum-01-900.webp` gesichtet). Solange nur die Kacheln ausgeliefert werden, kein Handlungsbedarf; bei einer späteren Großansicht des Quellbilds die Schüssel wegschneiden (`object-position` links oder Beschnitt).
7. Projektdaten (nicht in Checkliste) — „Schulzentrum Kerpen · 2026 · Wettbewerb, 1. Preis, realisiert" mit Foto des fertigen Geländes: Fertigstellung im laufenden Jahr (Stand September 2026) ist möglich, aber die Metazeile nennt nur ein Jahr, und ein Wettbewerb mit Realisierung im selben Jahr wirkt auf einen Vergabereferenten unglaubwürdig. Vorschlag: 2025, oder Maßnahme „Wettbewerb 2021, 1. Preis, realisiert 2026". Gleiches Muster bei Aachen (2022) ist unauffällig.
8. Tap-Ziele (Checkliste 3) — Playwright mobil: „Anfahrt auf OpenStreetMap" 39 px hoch (zweizeilig umbrochener Fließtext-Link, `09_kontakt_mobile_full.jpg`); „Büro" im Footer 33 px breit bei 44 px Höhe. Beides Inline-Text bzw. Listenlink mit ausreichender Höhe — WCAG-2.5.8-Ausnahme, kein Handlungsbedarf.

**Geprüft und ohne Befund** (Auszug mit Beleg):
- Kein Preloader, kein Intro, keine Animation; `prefers-reduced-motion` in `basis.css` Z. 302.
- Alle Schriften self-hosted, 0 Fremd-Domains auf allen 12 Seiten, 0 Cookies, 0 Storage-Einträge (Playwright), kein Formular (`mailto:`-Button), Datenschutzerklärung beschreibt genau das (`11_datenschutz_desktop_full.jpg`: „ohne Cookies, ohne Analyse-Werkzeuge, ohne Inhalte von fremden Servern").
- `lang="de"`; Skip-Link „Zum Inhalt springen" erstes fokussierbares Element, bei Fokus bei `left: 0, top: 0` sichtbar mit Outline 3 px `#2B5876`, Offset 3 px; genau eine H1 je Seite, Überschriftenfolge ohne Sprung (Startseite h1 → h2 „Projekte" → h3; Datenschutz h2 → h3 „Hosting").
- Fokusring auf dem gefüllten Akzent-Button der Kontaktseite: 3 px `#2B5876` mit 3 px Offset auf `#E0E4E7`-Fläche, klar vom gleichfarbigen Button abgesetzt (`fokus_knopf.jpg`).
- Mobil-Menü (390 px, Playwright): geschlossen „Menü" bei x = 16, Wortmarke „Steinwerk" bei x = 155–234, Telefon rechts — Kopfzeile dreigeteilt wie Brief 7 (`mobhero_start.jpg`). Geöffnet: „Schließen" x = 16–86, Wortmarke unverändert bei 155 → **keine Überlappung** (`mob_menu_offen.jpg`). `aria-expanded` wechselt true/false. **Focus-Trap belegt:** Tab-Folge Projekte → Leistungen → Büro → Kontakt → Telefon → E-Mail → Schließen → Projekte (kreist); Shift+Tab rückwärts Kontakt → … → Schließen → E-Mail (kreist); programmatischer Fokus auf einen Footer-Link wird sofort auf „Schließen" zurückgeholt; Escape schließt und setzt den Fokus auf den Schalter; Auswahl „Leistungen" schließt das Menü (`aria-expanded="false"`, URL `/leistungen/`).
- Filter mobil: `scrollWidth = clientWidth = 358`, kein horizontaler Scroll mehr; aktiver Eintrag auf `/`, `/projekte/gewerbe/` und `/projekte/wettbewerbe/` bei x = 16 sichtbar in Gewicht 500 (`05_projekte-gewerbe_mobile_full.jpg`, `06_projekte-wettbewerbe_mobile_full.jpg`).
- Filterseiten mit JS: `data-ansicht="beide"`, Raster (`display: grid`) und darunter die Tabelle (`display: block`, y = 1122 auf `/projekte/bildung/`) derselben n Projekte (Bildung 8/8, Verwaltung 4/4, Gewerbe 5/5, Wettbewerbe 3/3) — genau wie Brief 6 (`03_projekte-bildung_desktop_full.jpg`, `04_projekte-verwaltung_desktop_full.jpg`, `05_projekte-gewerbe_desktop_full.jpg`, `06_projekte-wettbewerbe_desktop_full.jpg`).
- Ohne JS: Filterchips sind fünf `<a>` auf `#projekte` bzw. `projekte/{typ}/`, aktiver mit `aria-current="page"`; Umschalter zwei Links `#projekte` / `projekte/`; der Menü-Button ist `display: none`, stattdessen der Anker-Link „Menü" auf `#fuss-navigation` (`nojs_menu.jpg`); `/projekte/gewerbe/` ohne JS: 5 Kacheln + 5 Tabellenzeilen, aktiver Chip „Gewerbe (5)" (`nojs_gewerbe.jpg`).
- Mit JS auf `/`: Chips werden `<button aria-pressed>`, Klick „Gewerbe" → 5 sichtbare Kacheln, URL per `replaceState` auf `/projekte/gewerbe/`; Umschalter „[x] Liste" → `data-ansicht="liste"`, 5 sichtbare Zeilen (`desk_liste_gewerbe.jpg`).
- Tabelle mobil als gestapelte Blöcke, alle sieben Angaben lesbar (`mob_tabelle.jpg`); Bildnachweis-Tabelle mobil im Wrapper scrollbar (794/358) mit Hinweistext, Seite selbst 390/390 (`mob_nachweis.jpg`).
- Text auf Bild: keiner; Chips unter dem Bild. Hover trägt keine Information. Inaktive Filter `#5B6269` auf `#EDEFF0` = 5,36:1 (Brief 4, gerechnet).
- `title`/`description`, `canonical`, `og:*`, `noindex, follow` auf allen 12 Seiten (grep: 12/12), `sitemap.xml` mit Präfix, `robots.txt` mit KI-Crawlern, JSON-LD `ArchitectOffice` — Tool 15/15 ok. Sprechende Ordner-URLs, Ortsbezug „Rheinland" im Statement, „Köln" im Metadatenblock und in der Kopfzeile.
- Impressum: § 5 DDG, AKNW, Berufsbezeichnung, Berufshaftpflicht („fiktive Angabe"), USt-IdNr., Absatz „Demo von XPONext … fiktiv" (`10_impressum_desktop_full.jpg`); Demo-Hinweis in jeder Fußzeile; Bildnachweis-Seite von Fußzeile und Impressum verlinkt.
- `BILDER.md` (Register) und `assets/bilder/BILDER.md` (abgeleitete Dateien) vollständig, 20 Quellbilder, alle referenzierten Dateien belegt. Keine Personen, keine Portraits als Team, kein erkennbares reales Gebäude.
- Render-blockendes JS: nur das 1-Zeilen-Inline-Script (`.js`-Klasse), `basis.js` mit `defer`.

## Messwerte

| Seite | Transfer | davon Bilder | LCP (lokal) | Fremd-Domains | Mobil-Querscroll |
|---|---|---|---|---|---|
| / | 869 KB | 738 KB | 76 ms | 0 | nein |
| /projekte/ | 130 KB | 0 | 28 ms | 0 | nein |
| /projekte/bildung/ | 431 KB | 313 KB | 36 ms | 0 | nein |
| /projekte/verwaltung/ | 262 KB | 147 KB | 44 ms | 0 | nein |
| /projekte/gewerbe/ | 295 KB | 179 KB | 44 ms | 0 | nein |
| /projekte/wettbewerbe/ | 213 KB | 99 KB | 40 ms | 0 | nein |
| /buero/ | 234 KB | 122 KB | 24 ms | 0 | nein |
| /leistungen/ | 101 KB | 0 | 16 ms | 0 | nein |
| /kontakt/ | 110 KB | 0 | 24 ms | 0 | nein |
| /impressum/ | 100 KB | 0 | 24 ms | 0 | nein |
| /datenschutz/ | 102 KB | 0 | 24 ms | 0 | nein |
| /bildnachweis/ | 115 KB | 0 | 20 ms | 0 | nein |

Geladene Fonts überall: Inter (variabel), IBM Plex Mono 400, IBM Plex Mono 500 — 48,7 KB. Größtes Bild der Startseite: `grundschule-ring-01-600.webp` 61 KB. Startseite gegenüber dem ersten Durchlauf 68 KB leichter (937 → 869 KB).

## Brief-Treue

| Feature-ID | umgesetzt | Beleg (Screenshot) |
|---|---|---|
| wolveridge-com-au-F3 Projektraster feste Kachelbreite | ja, 4 × 5, 296 px, `width`/`height` gesetzt | `01_start_desktop_full.jpg` (fünf volle Reihen) |
| wolveridge-com-au-F4 Unterschrift + Jahressortierung | ja, Titel + Mono-Zeile „Nr · Ort · Jahr · Maßnahme", 2026 → 2019 | `01_start_desktop_hero.jpg` |
| wolveridge-com-au-F5 Listenansicht als Tabelle | ja, `/projekte/` und unterer Teil jeder Filterseite | `02_projekte_desktop_full.jpg`, `03_projekte-bildung_desktop_full.jpg` |
| wolveridge-com-au-F2 Umschalter `[x] Raster [ ] Liste` | ja (Radio auf `/` und `/projekte/`; auf Filterseiten beide `[x]` als Sprunglinks, s. Warnung 4c) | `01_start_desktop_hero.jpg`, `02_projekte_desktop_hero.jpg`, `desk_liste_gewerbe.jpg` |
| wolveridge-com-au-F16 Bildart gekennzeichnet | ja, Chips „Modell"/„Baustelle" unter dem Bild, Spalte „Abbildung" für alle 20 (statt „Rendering", s. Warnung 4a) | `01_start_desktop_full.jpg` Reihen 3–5, `02_projekte_desktop_full.jpg` |
| wolveridge-com-au-F7 Mono für Struktur, Grotesk für Text | ja, Inter ≤ 500, Plex Mono für Meta/Filter/Tabelle/Telefon | alle Desktop-Heros |
| wolveridge-com-au-F8 drei Farbwerte, Grau als Zustand | ja, inaktive Filter/Umschalter grau, Akzent nur Links/Fokus/Button | `05_projekte-gewerbe_desktop_hero.jpg`, `09_kontakt_desktop_hero.jpg` |
| wolveridge-com-au-F1 Kopfzeile dreigeteilt | ja: Wortmarke / vier Punkte / „KÖLN · 0221 …"; mobil Menü / Steinwerk / Nummer | `01_start_desktop_hero.jpg`, `mobhero_start.jpg` |
| wolveridge-com-au-F10 Menü mobil Vollbild | ja, `aria-expanded`, `nav`-Landmark, Focus-Trap, Escape | `mob_menu_offen.jpg` |
| big-dk-F1 Hierarchie ohne Bold | ja, 52/40/28/17, kein Gewicht über 500 | `07_buero_desktop_hero.jpg` |
| big-dk-F2 Metadatenblock rechtsbündig | ja, Start (Standort/Team/Projekte/Wettbewerbe) und Büro (Gegründet/Team/Projekte/Wettbewerbe) | `01_start_desktop_hero.jpg`, `07_buero_desktop_hero.jpg` |
| big-dk-F3 gemeinsame linke Kante | ja, nichts zentriert | `08_leistungen_desktop_full.jpg` |
| big-dk-F4 Ort in Versalien je Kachel | ja, „KÖLN-EHRENFELD", „BERGISCH GLADBACH" | `01_start_desktop_full.jpg` |
| helenhard-no-F8 Filterleiste nach Typologie | ja, „Alle (20) · Bildung (8) · Verwaltung (4) · Gewerbe (5) · Wettbewerb (3)", statische Filterseiten + JS | `06_projekte-wettbewerbe_desktop_hero.jpg` |
| helenhard-no-F9 Label-Wert-Tabelle | ja, „Büro in Zahlen" (8 Zeilen), Leistungen (5 Zeilen) | `07_buero_desktop_full.jpg`, `08_leistungen_desktop_full.jpg` |
| helenhard-no-F13 Footer mit Standortblock | ja, Köln / Navigation / Rechtliches / Projekte nach Typ + Demo-Hinweis | jede `*_desktop_full.jpg` |

**Wow-Faktor** (Statement in Inter 52/500 über drei Spalten statt Hero-Bild, darunter Metadatenblock, Filterzeile und die erste vollständige Kachelreihe im 900-px-Ausschnitt): auf `01_start_desktop_hero.jpg` erkennbar. Mobil (`mobhero_start.jpg`): Statement 32 px in sechs Zeilen, Metadaten als eine Mono-Zeile, Filter, erste Kachel ab y ≈ 660 von 844 sichtbar.

**Abschnitt 10 („bewusst nicht")**: nichts davon verbaut — keine Detailseiten, keine Auszeichnungstabelle, keine Portraits, kein zentriertes Mono-Intro, kein Laufband, kein Minimal-Footer, keine ausblendende Kopfzeile, keine Signets, kein Preloader, keine Disziplin-Navigation, kein Hero-Bild/-Video, keine Skizzen, keine Serife, keine warme Palette, keine Newsliste, keine zentrierten Kacheltitel, keine Kursive, kein Lazy-Loading ohne Maße, kein Slider, kein Parallax, keine Google Fonts, kein Text auf Bild, kein Hover als Informationsträger.

**Nachbildungs-Vergleich**: unverändert gegenüber dem ersten Durchlauf — wolveridge.com.au liegt am nächsten (Raster + Tabelle + `[x]`-Umschalter + Mono-Unterschriften), Steinwerk unterscheidet sich durch Statement-H1, Metadatenblock, Filterzeile, 4 statt 3 Spalten, linksbündig statt zentriert, sticky statt ausblendend, vollen Footer, kühles Grau. Keine Nachbildung. Gegen Nordkant und Lindenau auf den ersten Blick unterscheidbar.

## Was gut ist

1. **Der Focus-Trap ist sauber und ohne Bibliothek.** Tab und Shift+Tab kreisen über Schalter und sechs Einträge, ein `focusin`-Listener fängt entwichenen Fokus ab, Escape schließt und gibt den Fokus zurück, Auswahl schließt. Die Kopfzeile bleibt im offenen Zustand dreigeteilt ohne Überlappung. Nicht anfassen.
2. **Filterseiten zeigen jetzt beides**, Raster und Tabelle, ohne dass JavaScript den Zustand umbiegt (`data-ansicht="beide"`); ohne JS identisch. Damit ist die Filterseite genau die Referenzliste, die Brief 6 verspricht, und verlinkbar aus Footer und Leistungen-Seite.
3. **Die fünf Ersatzbilder sind bewusst unspektakulär gewählt** — Fassadenausschnitte ohne Umfeld (Sporthalle, Feuerwache, Verwaltungszentrum) und ein Klinkerbau, der wirklich nach NRW-Schule aussieht (Berufskolleg). Genau das macht eine Stockfoto-Referenz glaubwürdig: nichts, an dem ein Vergabereferent hängen bleibt.

## Gesichtete Screenshots

`_doku/screenshots/pruefung2/` (36 Dateien, alle angesehen):
01_start_desktop_hero, 01_start_desktop_full, 01_start_mobile_full · 02_projekte_desktop_hero, 02_projekte_desktop_full, 02_projekte_mobile_full · 03_projekte-bildung_desktop_hero, 03_projekte-bildung_desktop_full, 03_projekte-bildung_mobile_full · 04_projekte-verwaltung_desktop_hero, 04_projekte-verwaltung_desktop_full, 04_projekte-verwaltung_mobile_full · 05_projekte-gewerbe_desktop_hero, 05_projekte-gewerbe_desktop_full, 05_projekte-gewerbe_mobile_full · 06_projekte-wettbewerbe_desktop_hero, 06_projekte-wettbewerbe_desktop_full, 06_projekte-wettbewerbe_mobile_full · 07_buero_desktop_hero, 07_buero_desktop_full, 07_buero_mobile_full · 08_leistungen_desktop_hero, 08_leistungen_desktop_full, 08_leistungen_mobile_full · 09_kontakt_desktop_hero, 09_kontakt_desktop_full, 09_kontakt_mobile_full · 10_impressum_desktop_hero, 10_impressum_desktop_full, 10_impressum_mobile_full · 11_datenschutz_desktop_hero, 11_datenschutz_desktop_full, 11_datenschutz_mobile_full · 12_bildnachweis_desktop_hero, 12_bildnachweis_desktop_full, 12_bildnachweis_mobile_full.

Hinweis: In den Mobil-Vollbildern erscheint die sticky Kopfzeile einmal mitten auf der Seite (z. B. `01_start_mobile_full.jpg` bei y ≈ 2 380) — Artefakt des Screenshot-Tools bei `position: sticky`, im Browser nicht reproduzierbar (eigene Viewport-Aufnahmen zeigen die Kopfzeile oben), kein Befund.

Zusätzliche Playwright-Aufnahmen (Scratchpad, nicht im Site-Ordner): `mob_menu_offen.jpg` (Menü offen, 390 px), `mobhero_start/projekte/buero/kontakt/impressum/leistungen.jpg` (erster Bildschirm 390 px), `mob_tabelle.jpg`, `mob_mensa.jpg`, `mob_nachweis.jpg`, `mob_gewerbe_full.jpg`, `nojs_gewerbe.jpg`, `nojs_menu.jpg`, `desk_liste_gewerbe.jpg`, `fokus_knopf.jpg`.

Quellbilder: die fünf Ersatzdateien in `assets/bilder/projekte/` in voller Größe (1920 × 1280) gesichtet, dazu die 900-px-Zuschnitte von verwaltungszentrum und feuerwache. Die übrigen 15 Quellbilder wurden im ersten Durchlauf gesichtet und sind unverändert (Dateidatum 2026-09-07).

## Erster Durchlauf

Datum: 2026-09-08 (früher am Tag), Bericht gesichert unter `_doku/pruefbericht_1.md`, Screenshots unter `_doku/screenshots/pruefung/`. Ergebnis damals: **nicht abgenommen, 1 Blocker, 14 Warnungen.**

- **Blocker 1** — `sporthalle-01.webp` zeigte das Stadion Kaliningrad (Pexels 1091435). **Behoben:** ersetzt durch Pexels 29750394 (Blechfassade mit rot-blauem Tor), Register, Bildnachweis-Seite, Alt-Text und Kacheln nachgezogen.
- **Warnung 1** (Verwaltungszentrum, Campus mit Emblem und Flaggen) — **behoben**, jetzt Pexels 9458996; Restnotiz zur „Bell"-Schüssel siehe Warnung 6 oben.
- **Warnung 2** (Berufskolleg, Kolonialbau mit Schild) — **behoben**, jetzt Pexels 33470382, Klinkerschule mit PV.
- **Warnung 3** (Feuerwache, Fahrzeug mit Wappen/URL) — **behoben**, jetzt Pexels 15602858, blaue Halle mit Rolltor, Sonderbeschnitt entfällt.
- **Warnung 4** (Mensa, chinesische Wandtexte) — **behoben**, jetzt Pexels 6344447, holzverkleideter Saal; Restnotiz zur Plausibilität siehe Warnung 5 oben.
- **Warnung 5** (Kerpen: „Anerkennung" mit Foto des fertigen Geländes) — **behoben** durch „Wettbewerb, 1. Preis, realisiert", Alt „Luftbild des erweiterten Schulgeländes"; Restnotiz zum Jahr 2026 siehe Warnung 7 oben.
- **Warnung 6** (Brief 8 vs. Seite: 8/6/6, Chip „Rendering", vertauschte Wettbewerbsergebnisse) — **teilweise:** Kerpen ist wieder „1. Preis" wie im Brief, Aachen bleibt abweichend „1. Preis, realisiert", Bildarten weiter 14/2/4; der Brief ist nicht angeglichen → jetzt Warnung 4.
- **Warnung 7** (Mobil: „Schließen" überlappt Wortmarke, „Menü" nicht am linken Rand) — **behoben**, gemessen: Schalter x = 16, Wortmarke x = 155, keine Überlappung im offenen Zustand.
- **Warnung 8** (kein Focus-Trap) — **behoben**, Tab/Shift+Tab kreisen, `focusin`-Rückholung, Escape.
- **Warnung 9** (Filter mobil scrollt, aktiver Eintrag außerhalb) — **behoben** durch Umbruch, aktiver Eintrag bei x = 16 sichtbar; Brief 5 sagt noch „eine Zeile mit Scroll" → Teil von Warnung 4.
- **Warnung 10** (Filterseiten blenden Tabelle mit JS aus) — **behoben**, `data-ansicht="beide"`, Raster und Tabelle untereinander.
- **Warnung 11** (900-px-Kacheln bis 118 KB) — **teilweise:** neu komprimiert, jetzt 14 von 20 ≤ 60 KB, sechs bei 67–112 KB → Warnung 1.
- **Warnung 12** (8 Fonts, davon zwei ungenutzte Italic) — **teilweise:** Italic gelöscht, 6 Dateien → Warnung 2.
- **Warnung 13** (og.jpg kein WebP) — unverändert, kein Handlungsbedarf → Warnung 3.
- **Warnung 14** (Bildnachweis-Tabelle mobil abgeschnitten ohne Hinweis) — **behoben**, Wrapper scrollt (794/358) mit Hinweistext, Seite ohne Querscroll.
