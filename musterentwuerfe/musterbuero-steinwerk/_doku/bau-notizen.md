# Bau-Notizen: Musterbüro Steinwerk (bis 08.09.2026 „Steinwerk Planungsgesellschaft mbH“)

Rolle Bauer, 2026-09-07. Grundlage: `design-brief.md` (Vorgabe) und `inhalte.md`.

## Entscheidungen zu Abschnitt 11 des Briefs (offene Fragen)

1. **IBM Plex Mono:** ja. Lag bereits im Skeleton (400, 500, 400 kursiv, latin + latin-ext); eigene
   @font-face-Blöcke in basis.css Abschnitt 1. Übrige Familien gelöscht, LICENSES.md gekürzt.
2. **Sortierung:** Jahr absteigend, innerhalb eines Jahres Foto → Rendering → Baustelle (Brief 8.3).
   Nummern 01–20 folgen dieser Reihenfolge.
3. **Statement-Wortlaut:** aus dem Brief übernommen: „Schulen, Kitas, Verwaltungs- und Gewerbebauten
   im Rheinland — von der Machbarkeitsstudie bis zur Übergabe."
4. **Doppelte Quelldatei:** `berufskolleg-01.webp` ist inzwischen ersetzt (anderes Motiv), kein
   Duplikat mehr. Nichts nachgeladen.
5. **Telefonnummer in der Kopfzeile:** wie im Brief (rechts, Mono, `tel:`-Link).
6. **Filter:** vier statische Filterseiten plus JS-in-place-Filter mit `aria-pressed`.

## Verlauf

- Skeleton kopiert; `danke/`, `formular.php`, `README.md` entfernt (kein Formular); Fonts auf
  Inter + IBM Plex Mono reduziert.
- Kacheln erzeugt (`assets/bilder/kacheln/`): 600×400 alle ≤ 60 KB (q ≥ 70); 900×600 (nur Retina-Mobil per
  srcset) bei q ≥ 60 bis 90 KB, weil drei detailreiche Motive (Büro Kalk, Grundschule Am Ring,
  Produktionshalle) unter 60 KB nur mit q 40 gingen. Beschnitt: `feuerwache` ohne das Schild am oberen
  Rand, `mensa` ohne die Schriftzeichen an den Wänden, Modellfotos auf die Gebäude. `berufskolleg-01`
  (Quelle) von 407 KB auf 1600 px / < 300 KB neu komprimiert, Register unverändert (Original-Spalte = Pexels).
- Bildbefund gegen die Texte (Bild schlägt Brief): mensa, produktionshalle, stadtwerke, sporthalle,
  schulzentrum, verwaltungszentrum sind Fotos, nicht Renderings → Bildart „Foto", Projekte 2025 als
  fertiggestellt statt „in Planung"; kita-sonnenhang und quartiersschule sind Modellfotos → Chip „Modell";
  berufskolleg zeigt einen Altbau → „Foto, Bestand vor der Sanierung"; schulzentrum ist ein Luftbild
  eines bestehenden Campus → Wettbewerb „Anerkennung", Foto des Wettbewerbsgebiets; verwaltungszentrum
  zeigt ein fertiges Gebäude → „Wettbewerb 1. Preis, realisiert 2022"; grundschule-ring zeigt
  Backstein-Bestand mit Glashalle → „Umbau und Erweiterung" statt Neubau. Kein Rendering auf der Seite,
  also Chips nur „Modell" und „Baustelle"; Tabelle nennt die Bildart für alle 20.
- Hero-Probe (`_doku/screenshots/hero-probe/`): Desktop 1440×900 zeigt Statement über drei Spalten,
  Metablock rechts, Filterzeile und die komplette erste Kachelreihe — Wow-Faktor erkennbar. Startseite
  960 KB, LCP lokal 92 ms, keine Fremddomains. Nachgebessert: Leerzeichen in Wortmarke/Telefon (Flex),
  Metablock mobil als eine Zeile, unsichtbare H2 „Projekte" gegen den Überschriftensprung h1→h3.
  Burger-Breakpoint bei 1099 px statt 719 (Wortmarke + 4 Punkte + Telefon passen erst ab 1100 in eine Zeile).
- Vollausbau: 12 Seiten (Start, /projekte/, 4 Filterseiten, Büro, Leistungen, Kontakt, Impressum,
  Datenschutz, Bildnachweis) aus `_doku/build.py`; alle Projektdaten in einer Liste (PROJEKTE).
  Filter/Umschalter: ohne JS Links auf statische Filterseiten bzw. `/projekte/`, mit JS Buttons mit
  `aria-pressed`, Filterung in derselben Seite, URL per `history.replaceState`.
- `website_qualitaet`: 0 Blocker. Zwei Warnungen bewusst stehen gelassen: (1) 8 Font-Dateien — der
  Browser lädt per unicode-range/font-style nur die genutzten (gemessen 3 Dateien, 48 KB); Kursiv und
  latin-ext liegen laut Vorgabe bei. (2) `og.jpg` nicht WebP — Open-Graph-Vorschauen brauchen JPEG/PNG.
- Abschluss-Screenshots `_doku/screenshots/final/` (12 Seiten × 3): kein horizontales Scrollen, keine
  Fremddomains, Startseite 937 KB, LCP lokal 92 ms. Nachgebessert: Tabelle mobil als Blockzeilen
  (table/tbody display:block, colgroup aus).
- Bekanntes Restrisiko für den Prüfer: `sporthalle-01` (Stock) könnte ein reales Stadion zeigen; als
  „Sporthalle mit gestreifter Fassade" beschrieben, kein Ortsbezug im Bild. `berufskolleg-01` zeigt
  einen Altbau mit Arkaden (Bestand vor Sanierung).

## Nachbesserung nach Prüfbericht (2026-09-08)

- Blocker 1, Warnungen 1–4: fünf Quellbilder ersetzt (Suche `stockfoto_suche` nur_suchen → Sichtung → per ids):
  `sporthalle-01` = Pexels 29750394 (Jan van der Wolf, Stehfalzfassade mit rot-blauem Tor),
  `verwaltungszentrum-01` = 9458996 (Stephen Andrews, weiße Plattenfassade), `berufskolleg-01` = 33470382
  (Sergej *****, sanierte Klinkerschule mit PV), `feuerwache-01` = 15602858 (Jan van der Wolf, blaue Halle mit
  Rolltor), `mensa-01` = 6344447 (cottonbro studio, holzverkleideter Saal). Alle in Vollgröße angesehen: keine
  Schrift, keine Wappen/Flaggen, keine Personen, kein bekanntes Gebäude. Register `projekte/BILDER.md` zeilenweise
  ersetzt (Altquelle in der Datumsspalte vermerkt), `assets/bilder/BILDER.md` und Bildnachweis-Seite nachgezogen,
  Alt-Texte und Kacheln 600/900 neu. Sonderbeschnitte (feuerwache, mensa) entfallen.
- Warnung 5/6 (Kerpen): Bild zeigt ein fertiges Schulgelände → „Wettbewerb, 1. Preis, realisiert" 2026 (wie im
  Brief), Alt „Luftbild des erweiterten Schulgeländes". Aachen bleibt „1. Preis, realisiert" (Foto eines fertigen
  Baus). Damit zwei erste Preise + ein dritter Preis (Modell); Einleitung `/projekte/wettbewerbe/` angepasst.
  Alle 20 Kacheln geprüft: Chip/Text/Bild widerspruchsfrei (Foto = fertig, Modell = Wettbewerb bzw. Modellfoto,
  Baustelle = 2019/2020). Brief 8 (8/6/6, Chip „Rendering") bleibt als Abweichung „Bild schlägt Brief" bestehen.
- Warnung 7: Ursache war der leere Flex-Posten `.kopf__nav` (order 0) — er stand vor dem Schalter, `space-between`
  rückte „Menü" in die Mitte. `.kopf__nav { order: 2 }`; gemessen 390 px: Schalter x=16, Wortmarke x=155–235,
  Telefon rechts; geöffnet „Schließen" x=16–86, keine Überlappung.
- Warnung 8: Focus-Trap in basis.js: Tab/Shift+Tab kreisen über Schalter + sechs Einträge, `focusin` holt
  entwichenen Fokus zurück, Escape schließt und fokussiert den Schalter. Playwright: Tab-Folge Projekte … E-Mail →
  Schließen → Projekte; Shift+Tab rückwärts; nach Escape `aria-expanded=false`, Fokus auf `.kopf__schalter`.
- Warnung 9: Filterleiste bricht um (`flex-wrap`), kein horizontaler Scroll mehr (scrollWidth = clientWidth 358);
  aktiver Eintrag auf allen Filterseiten sichtbar.
- Warnung 10: Brief 6 verlangt auf Filterseiten Raster und darunter die Tabelle — umgesetzt: `data-ansicht="beide"`,
  basis.js wandelt dort die Umschalter-Einträge nicht in Buttons um, sie bleiben Sprunglinks `#raster`/`#liste` und
  zeigen beide `[x]` (Klasse `an`). Auf `/` und `/projekte/` unverändert Radio-Verhalten.
- Warnung 11: 900-px-Kacheln aus der Quelle neu bei q 56–82: 14 ≤ 60 KB, sechs detailreiche Motive 65–109 KB
  (buero-kalk 109, produktionshalle 85, grundschule-ring 78, stadtwerke 70, kita-waldstrasse 68, berufskolleg 65) —
  unter 60 KB nur mit sichtbaren Artefakten, Grenze 120 KB eingehalten. 600-px-Kacheln alle ≤ 60 KB.
- Warnung 12: zwei Plex-Mono-Italic-Dateien und ihre `@font-face`-Blöcke gelöscht, LICENSES.md angepasst → 6 Dateien
  (Tool-Warnung „mehr als 5" bleibt: latin-ext für Inter/Plex behalten, wird nur bei Bedarf geladen).
- Warnung 14: Bildnachweis-Tabelle `min-width: 44rem` im Wrapper `.nachweis { overflow-x: auto }`, Dateispalte
  `nowrap`, mobiler Hinweistext über der Tabelle. Gemessen: Wrapper scrollt (794/358), kein Seiten-Querscroll.
- Abschluss: `website_qualitaet` 0 Blocker (Warnungen: 6 Fonts, og.jpg), `grep "{{"` leer, Screenshots
  `_doku/screenshots/final/` neu (12 Seiten × 3, 0 Fehler, 0 Fremd-Domains, kein Querscroll, Startseite 869 KB).

## Umbau zum Musterentwurf (2026-09-08)

Die Seite ist kein „fiktives Referenzbüro“ mehr, sondern ein offen gekennzeichneter **Musterentwurf**:
alles, was wie eine reale Person, Firma, Anschrift oder Rufnummer aussah, ist jetzt eine erkennbare
Musterangabe. Alle Änderungen in `_doku/build.py` (Konstanten und Textbausteine), Neubau mit
`python3 _doku/build.py`; `robots.txt`, `.htaccess`, `assets/bilder/BILDER.md`, `assets/bilder/icon.svg`
und der Kopfkommentar in `basis.css` sind Handdateien und wurden einzeln nachgezogen.

- **Name:** „Steinwerk Planungsgesellschaft mbH“ → **„Musterbüro Steinwerk“** in Wortmarke, `<title>`,
  Meta/OG, JSON-LD, Fußzeile, Impressum und Fließtext. Die Rechtsform mbH entfällt vollständig; im
  Impressum steht statt des Handelsregisters „Rechtsform und Registereintrag: Musterangabe“, in „Büro in
  Zahlen“ statt der Rechtsform-Zeile die Zeile „Sitz — Köln“.
- **Keine erfundenen Personen mehr:** Hanna Sturm, Malte Brenner und Yusuf Demirci sind restlos raus —
  aus dem `founder`-Array des JSON-LD (Feld ganz entfernt), aus Impressum („Vertreten durch …“,
  „Verantwortlich für den Inhalt“), Datenschutz, Bürotext und der Zahlen-Tabelle. An ihrer Stelle stehen
  Rollen: „von drei Geschäftsführenden geleitet, alle in die Architektenliste der Architektenkammer
  Nordrhein-Westfalen eingetragen“ bzw. „die Geschäftsführung (Musterangabe)“.
- **Anschrift:** „Deutz-Kalker Straße 88“ → „Musterstraße 1“, PLZ und Stadt bleiben (50679 Köln).
  „Köln-Deutz“ ist überall zu „Köln“ geworden (H1 Büro, Label im Kontaktkasten, Meta). Der
  Anfahrtstext nennt keine Straße und keinen Bahnhof mehr, der **OpenStreetMap-Link auf die konkrete
  Adresse ist entfallen** — damit hat die Seite keinen einzigen externen Link mehr außer `aknw.de`;
  der entsprechende Absatz im Datenschutz („etwa den Anfahrtslink“) verweist jetzt auf die Kammer.
- **Telefon:** „0221 55 44 33-0“ → „0221 000000“ (`tel:+49221000000`), auf der Kontaktseite einmal mit
  dem Zusatz „(Musterangabe)“. **E-Mail/Domain:** `info@musterbuero-steinwerk.de`, Domain geprüft
  (nicht registriert). **Berufshaftpflicht:** „Musterversicherung AG (Musterangabe), Musterstraße 1,
  50672 Köln“.
- **URL-Basis** überall `https://www.xponext.de/musterentwuerfe/musterbuero-steinwerk` — canonical, OG,
  JSON-LD `@id`/`url`, `sitemap.xml`, `robots.txt`. Interne Pfade bleiben relativ, `noindex, follow`
  steht unverändert auf allen 12 Seiten.
- **Hinweistexte:** Fußzeile „Musterentwurf von XPONext (xponext.de). Büro, Personen und Projekte sind
  erfunden, die Fotografie ist Stockmaterial.“ Der Impressum-Absatz sagt dasselbe und ergänzt, dass
  Anschrift, Rufnummer, E-Mail sowie Register-, Steuer- und Versicherungsangaben Musterangaben sind.
  Das Wort „Demo“ kommt im Text nicht mehr vor; die CSS-Klasse heißt weiter `.demo-hinweis`, weil die
  Qualitätscheckliste sie so erwartet. Das Wort „fiktiv“ steht bewusst noch im Bildnachweis — der
  `referenz`-Modus von `website_qualitaet` sucht danach.
- **Umbruchpunkt der Kopfzeile: 1099 px → 959 px.** Die Wortmarke ist von 296 px auf 187 px geschrumpft.
  Gemessen wurde nicht die Box (die Grid-Spalte ist `minmax(0,1fr)` und schneidet den `nowrap`-Text ab,
  was in der ersten Messung eine Lücke von 64 px vortäuschte, während sich Wortmarke und „Projekte“ im
  Screenshot schon berührten), sondern der tatsächliche Textbereich per `Range.getBoundingClientRect()`.
  Ergebnis: Abstand Wortmarke → „Projekte“ 88 px bei 1100, 53 px bei 960, 38 px bei 900, 13 px bei 800,
  Überlappung ab 727 px. Gewählt: 959 px, dort bleiben 53 px — mehr als der halbe Rasterabstand (64 px)
  und mehr als der Seitenrand (32 px). Belege: `_doku/screenshots/kopfzeile-umbruch/kopf-{1440,1100,960,
  959,720,450,449,390}.jpg`.
- **Zweiter Umbruchpunkt: 380 px → 449 px.** Mobil steht die Wortmarke mittig; „Musterbüro Steinwerk“
  ist bei 16 px 176 px breit und überlappte bei 390 px die Telefonnummer um 3 px. Unter 450 px steht die
  Wortmarke daher links statt mittig und die Telefonnummer entfällt (wie vorher unter 380 px). Die Regel
  `.marke__lang { display: none }` unter 720 px ist gelöscht — sie hätte mobil nur noch „Musterbüro“
  übrig gelassen; der Name bleibt jetzt auf jeder Breite vollständig.
- **Vorschaubild der Übersicht:** `musterentwuerfe/assets/musterbuero-steinwerk.webp` zeigte noch die
  alte Wortmarke und die alte Telefonnummer und wurde aus der neuen Startseite nachgezogen
  (1440×900 aufgenommen, auf 1200×750 skaliert, WebP q80, 58 KB).
- **Abschluss:** `website_qualitaet` (referenz, Präfix `/musterentwuerfe/musterbuero-steinwerk`) 0 Blocker,
  dieselben zwei bekannten Warnungen (6 Font-Dateien, `og.jpg` als JPEG). `grep` auf die alten Namen,
  die alte Straße, die alte Domain, „Planungsgesellschaft“ und `{{` jeweils leer. Screenshots
  `_doku/screenshots/final/` neu (12 Seiten × 3, 0 Fehler), Startseite 870 KB, LCP lokal 68 ms, keine
  Fremd-Domains.
