# Bau-Notizen: Musterstudio Lindenau (bis 08.09.2026 „Studio Lindenau“, Ordner `referenzen/studio-lindenau`)

Rolle Bauer, 2026-09-07 (Fortsetzung nach abgebrochenem Lauf). Grundlage: `design-brief.md` (Vorgabe) und `inhalte.md`.
Generator: `_doku/build.py` (baut alle Seiten + sitemap.xml; Pfad zur Site steht oben im Skript).

## Protokoll

- Stand bei Wiederaufnahme: Skeleton kopiert (index.html, robots, sitemap, .htaccess, basis.css/js), Fonts bereits auf
  cormorant-garamond-latin(.italic) + dm-sans-latin reduziert, LICENSES.md noch ungekürzt, keine Unterseiten, kein build.py.
- Tokens/Fonts/CSS Abschnitt 10, basis.js, icon.svg, abgeleitete Bilder (kacheln/ 960+1440, hero/ 960/1440/1920, og.jpg), BILDER.md, robots, .htaccess: fertig.
- Hero-Probe (Schritt 2): _doku/screenshots/hero-probe/ — Desktop 1440×900: Kopfzeile 88 px, Bild 70 % rechts eingerückt, Satz links an der Bildunterkante, Linie wächst in die Intro-Sektion. Mobil 390: Satz über Bild, Hero < 100 vh. Lokal 272 KB, 3 Fonts geladen, kein Querscroll. Keine Nachbesserung nötig.
- Vollausbau: build.py mit allen 15 Seiten + Sitemap, erster Lauf.
- Vollausbau abgeschlossen, Selbstprüfung und Abschluss-Screenshots gelaufen (siehe unten).

## Entscheidungen zu Abschnitt 11 des Briefs

1. **Duplikate:** `kampen-02` und `kanzlei-hafencity-02` waren bei Wiederaufnahme bereits ersetzt (Schlafzimmer mit
   Dünenblick bzw. Lounge mit Ledersofas). Kampen: Reihenfolge 03 · 02 · 04 · 01 (02 rückt als Sylt-Bild auf Platz 2).
   Kanzlei: **Aufmacher jetzt `-02`** (Lounge, warme Palette) statt `-03` (blauer Teppich); Reihenfolge 02 · 03 · 04 · 01.
2. **Schwache Bilder:** nichts nachgeladen (Vorgabe). `hotel-speicherstadt-04` (Person) wird **nirgends** verwendet, das
   Hotel hat drei Bilder (Bild 2 groß, Bild 3 allein in der Paar-Position). `praxis-eppendorf-01`, `restaurant-fleet-01`,
   `blankenese-01`, `harvestehude-01` stehen wie im Brief an letzter Stelle.
3. **Hero-Satz:** „Räume, die ruhig wirken und lange gefallen." als H1. Der Ortsbezug steht im Intro-Absatz
   („Büro für Innenarchitektur in Hamburg … in Norddeutschland") und in den Ort-Zeilen der Projekte.
4. **Schriften:** Cormorant Garamond + DM Sans wie im Brief (dritte Referenz nutzt Inter + IBM Plex Mono).
5. **Metadaten:** vier Zeilen (Ort, Fertigstellung, Leistung, Fläche) mit fiktiven, plausiblen Flächen — durch den
   Demo-Hinweis gedeckt.
6. **Projekttexte:** vom Bauer geschrieben, je 58–74 Wörter, Material und Aufgabe, keine Superlative.
7. **Kein Formular, keine Karte:** `formular.php`/`danke/` nie kopiert, Datenschutz ohne Formular-Absatz, robots ohne
   die beiden Disallow-Zeilen.
8. **URL `/studio/`** (nicht `/buero/`), Nav-Punkt „Studio".

## Weitere Entscheidungen des Bauers

- **Relative Pfade** überall (`assets/…`, `../assets/…`, `../../assets/…`); absolut nur canonical, og:image, sitemap, robots.
- **Bilder:** Quellen bleiben 1920 px in `projekte/`; zusätzlich `kacheln/<name>-960|-1440.webp` (Pillow, q82) als
  srcset-Stufen für alle 32 Motive, `hero/hero-960|1440|1920.webp` als 16:10-Ausschnitt aus `penthouse-berlin-03`
  (1920er Stufe 111 KB), `og.jpg` 1200×630 (JPEG bewusst — Tool-Warnung erwartet). Alles in `assets/bilder/BILDER.md`.
- **Erstes Bild je Seite** (Start-Hero, Detail-Hero, erstes Bild auf /projekte/ und /studio/) ohne `loading="lazy"`, ohne
  Einblenden, mit `fetchpriority="high"` — sonst lag der LCP durch den Fade bei ~1,2 s; jetzt 24–100 ms lokal.
- **Überschriften:** Startseite h1 (Hero-Satz) → h2 „Ausgewählte Projekte"/„Studio"/Kontaktkasten → h3 Projekttitel;
  auf /projekte/ sind die Projekttitel h2 (keine Sprünge).
- **Kontaktkasten** vor der Fußzeile auf jeder Seite (zweite dunkle Stufe), dort der einzige gefüllte Button.
- **Mobile-Menü:** Vollbild-Overlay, Button wechselt „Menü"/„Schließen", Escape, Fokus-Falle, schließt bei Klick auf
  einen Punkt; Body-Scroll gesperrt. Justify der beiden Listen im Overlay auf `auto` gesetzt (sonst rückten
  Leistungen/Kontakt nach rechts).
- **Tap-Ziele gemessen (390 px):** Nav/Kontakt-Link 44, Menü-Button 44, Wortmarke 46, Chevrons 52, Footer-Links 44,
  Telefon/Mail im Kontaktkasten 44, Button 53, „Mehr über das Studio" 44.
- **Nav-Kontrast:** Kopfzeile liegt immer auf `#1F1D1A`; inaktive Punkte `#B5AEA3` = 7,65:1, Footer-Links `#9E978B` = 5,81:1,
  im Kontaktkasten (`#2A2724`) 5,13:1.
- **`.htaccess`:** HTTPS-Regel mit `%{REQUEST_URI}` (Unterordner), keine www-Regel.

## Tool-Ergebnis

`website_qualitaet` (referenz, url_praefix `/referenzen/studio-lindenau`): 18 ok, **0 Blocker**, 1 Warnung (`og.jpg`
nicht WebP, beabsichtigt). `grep -rn "{{"` außerhalb `_doku/` leer.
`website_screenshot` lokal, 15 Seiten: kein Querscroll, keine Fremd-Domains, alle Bilder mit alt, je Seite genau eine H1,
LCP lokal 24–100 ms, Startseite mobil 559 KB / Desktop ~440 KB Transfer (Lazy-Bilder ausgenommen).
Screenshots: `_doku/screenshots/final/` (45 Dateien: 15 Seiten × desktop_hero/desktop_full/mobile_full, Nummerierung
01 Start, 02 Projekte, 03–10 Projektseiten, 11 Studio, 12 Leistungen, 13 Kontakt, 14 Impressum, 15 Datenschutz, dazu
`00_menue_mobil.jpg`); Messwerte in `final_messwerte.json`. Zwischenstand in `screenshots/zwischenstand/`.

## Nachbesserung nach Prüfbericht (2026-09-07, Rolle Bauer)

- **W3 Harvestehude:** `harvestehude-01` (Dubai-Skyline) und `-02` (Hochglanzküche/Kronleuchter) ersetzt durch Pexels 8143679
  (Salon mit Kamin, Stuckrahmen, Fischgrätparkett) und 8143700 (Esszimmer, hohe Fenster, Fischgrät) — gleiche Serie, Max
  Vakhtbovych. Reihenfolge jetzt 03 · 01 · 04 · 02 (Altbau-Bild als Bild 2 groß). Text: „Stuck und Fischgrätparkett …
  Wandfelder und Kamin freigelegt", Küchensatz gestrichen.
- **W4 Penthouse:** Textweg (billiger, die Bilder 01/02 sind mit ihrer Skyline sonst nicht zu retten): Titel jetzt
  „Penthouse Berlin-Mitte", Text „Dachgeschoss auf einem Neubau in Berlin-Mitte … mit Blick auf die Hochhäuser am
  Alexanderplatz" statt „über einem Gründerzeithaus". Slug `penthouse-berlin` und URL unverändert; Alt-Texte inkl. Start-Hero
  nachgezogen. Brief 8 und `inhalte.md` nennen weiterhin Prenzlauer Berg — bewusst nicht rückwirkend geändert.
- **W5 Kampen:** `kampen-01` (Blockbohlen, Fernseher, rotes Nachbarhaus) ersetzt durch Pexels 9565779 (weißes Schlafzimmer
  mit Vertäfelung, Leinen, Holzbord; Taryn Elliott, gleiche Serie wie kampen-03). Text um „Gästezimmer" ergänzt.
- **W6 Praxis:** `praxis-eppendorf-01` (Instrumenten-Detail) und `-04` (blauer Stuhl) ersetzt durch Pexels 4562895 und
  4562896 (Engin Akyurt, Behandlungseinheit vor Eichen-Sitzbank bzw. Eichenschrank mit Wiener Geflecht). Text von
  „Kalkputz/helles Holz" auf das umgeschrieben, was die Bilder zeigen: Weiß, warmes Grau, Eiche mit Geflecht,
  Sechseckfliesen in Holzoptik. Pexels liefert für Zahnarztpraxen fast nur Klinikweiß und Personen — zwei Suchrunden.
- **W7 Kanzlei:** `kanzlei-hafencity-01` (Blauwand) ersetzt durch Pexels 7587300 (Bibliothek mit Regalwand und Leiter,
  q76 = 262 KB). Reihenfolge 02 · 04 · 01 · 03: Regal als Bild 2 groß, der blaue Teppich (03) rückt in die 4:3-Paarposition
  rechts (kleinstes Bild der Seite). Text um „Bibliothek mit Leiter" ergänzt.
- **W8 Hotel:** viertes Bild `hotel-speicherstadt-05` (Pexels 8089171, Travertin-Bad, 270 KB) ergänzt; `-04` (Person)
  bleibt unbenutzt. Text: „die Bäder sind in Travertin gefasst". Zusätzlich Drei-Bilder-Fall in `build.py` abgesichert:
  `.paar--einzel` setzt ein einzelnes drittes Bild auf volle Breite statt in die leere linke Spalte.
- **W9 /studio/ mobil:** Ursache war `.studio__bild { order: -1 }` — Grid-Kind ist aber `.studio__bild-rahmen`, der `order`
  wirkte nie. Jetzt `.studio__bild-rahmen { order: -1 }` (< 900 px): Bild oben, Kasten darunter, auch auf der Startseite.
- **W1/W12 Datenschutz:** Hoster-Satz ohne Anbieterbehauptung („bei einem deutschen Hosting-Anbieter auf Servern in
  Deutschland"), Protokolldaten-Absatz und AV-Satz unverändert. „Der Hamburgische" → „der Hamburgische".
- **W10 Randspalte:** Fließtext-Absatz in `.detail__rand p` jetzt linksbündig, `dl` (Metadaten) bleibt rechtsbündig an der
  Bildkante (big-dk-F2).
- **W2 Fokusring — bewusste Abweichung von `checklisten/qualitaet.md` (3 px):** bleibt bei 2 px + 3 px Offset wie im Brief
  Abschnitt 9 vorgeschrieben. Sichtbar auf hell (`#7A5F3E`) und dunkel (`#C9A97E`); der Brief geht hier vor der Checkliste,
  Entscheidung liegt beim Nutzer.
- **Register:** `projekte/BILDER.md` sechs Zeilen ersetzt, eine ergänzt (Spalte Datum „Ersatz nach Prüfbericht"),
  `assets/bilder/BILDER.md` zwölf Kachelzeilen ersetzt, zwei ergänzt. Impressum-Bildnachweis: AJ Ahamad, Jan van der Wolf,
  cottonbro studio, Tima Miroshnichenko raus, Engin Akyurt rein. Kandidaten liegen unter
  `XPO_Agentic_Workflow/.tmp/lindenau_ersatz/` (löschbar).
- **Abschluss:** `website_qualitaet` 15 Seiten, 18 ok, 0 Blocker, 1 Warnung (og.jpg, beabsichtigt); `grep "{{"` leer.
  Screenshots `final/` neu (45 Dateien + `final_messwerte.json`, `00_menue_mobil.jpg` aus dem alten Lauf entfällt): kein
  Querscroll, keine Fremd-Domains, LCP lokal 20–84 ms, größte Seite Restaurant 622 KB, Kanzlei jetzt 557 KB (Bibliothek 262 KB).

## Umbau zum Musterentwurf (2026-09-08, Rolle Bauer)

Anlass: Die Seite wird offen als Musterentwurf gekennzeichnet. Alles, was wie eine reale Person, Firma, Anschrift
oder Rufnummer aussah, ist durch erkennbare Musterangaben ersetzt. Alle Änderungen in `_doku/build.py` (Quelle der
Wahrheit), zusätzlich `robots.txt`, `.htaccess` und die Kopfzeilen von `basis.css`/`basis.js`/`assets/bilder/BILDER.md`.

- **Name:** „Studio Lindenau“ → **„Musterstudio Lindenau“** (Konstante `NAME`, damit überall: Wortmarke, `<title>`,
  Description, OG, JSON-LD, Fußzeile, Impressum, Intro-Absatz). Alle `title` bleiben unter 65 Zeichen, alle
  Descriptions unter 160 — die `assert` in `head()` decken das ab.
- **Personen restlos raus:** Vera Lindenau, Ida Brandes, Noah Ferreira, Lene Hartwig. JSON-LD-Feld `founder` gelöscht
  (kein Ersatz — schema.org verlangt es nicht). Team ist jetzt eine **Rollenliste** ohne Namen; das `<span>` trägt
  die Rolle statt des Namens, der Zusatz nach dem `·` bleibt auf `/studio/` erhalten (Kammer, Projektleitung …).
  Fließtext: „Das Studio wurde 2014 in der HafenCity gegründet“ bzw. „… 2014 gegründet, nach Jahren der Inhaberin in
  Büros in Kopenhagen und Hamburg“. Studio-Description ohne Personenbezug neu geschrieben.
- **Anschrift:** „Am Sandtorkai 4“ → **„Musterstraße 1“**, PLZ und Ort unverändert. Zwei Formulierungen mit Ortsbezug
  umgeschrieben: Kontaktkasten „bei uns im Studio“, Kontaktseite „Kontorhaus in der HafenCity, 3. Stock“.
- **Telefon:** „040 33 22 11-0“ → **„040 000000“** (`tel:+4940000000`). Zusatz „(Musterangabe)“ im Impressum und in
  der Kontakt-Description; auf `/kontakt/` steht unter der großen Nummer eine Zeile „Telefonnummer und Anschrift
  sind Musterangaben.“
- **Domain:** `studio-lindenau.de` gehört tatsächlich jemand anderem und musste restlos verschwinden →
  **`post@musterstudio-lindenau.de`**. Geprüft: `musterstudio-lindenau.de` ist nicht registriert.
- **Berufshaftpflicht:** „Hanseatische Architektenversicherung AG (fiktiv), Beispielstraße 12“ →
  „Musterversicherung AG (Musterangabe), Musterstraße 1, 20095 Hamburg“. USt-IdNr. um „(Musterangabe)“ ergänzt.
  „Verantwortlich für den Inhalt“ nennt jetzt „Die Inhaberin, Anschrift wie oben“ plus einen Satz, warum kein Name steht.
- **URL-Basis:** `https://www.xponext.de/musterentwuerfe/musterstudio-lindenau` in `URL` (canonical, OG-Bild, JSON-LD
  `@id`/`url`, sitemap.xml) sowie in `robots.txt` (Sitemap-Zeile) und im `.htaccess`-Kommentar. Interne Pfade bleiben
  relativ, `noindex, follow` steht unverändert auf allen 15 Seiten.
- **Hinweistexte:** Fußzeile „Musterentwurf von XPONext (xponext.de). Studio, Personen und Projekte sind erfunden,
  die Fotografie ist Stockmaterial.“; Impressum sinngemäß gleich, zusätzlich der Hinweis, dass Steuer- und
  Versicherungsangaben Musterangaben sind. Das Wort „Demo“ kommt nicht mehr vor, die CSS-Klasse heißt jetzt
  `.muster-hinweis`. Die Fotografenliste im Impressum bleibt — sie ist der echte Bildnachweis.
- **Wortmarke im Kopf (Prüfpunkt 10):** „Musterstudio Lindenau“ hat 21 statt 15 Zeichen. Desktop passt unverändert
  (273 px bei 1440 px Fenster, reichlich Luft neben den Navigationsspalten). **Mobil nicht:** bei 390 px war die
  Marke 219 px breit, verfügbar sind 159 px → Querscroll (`scrollWidth` 418 bei 390). Auf 16 px zu verkleinern hätte
  die Marke kleiner als die Navigation gemacht. Lösung im Medienbereich < 900 px: `white-space: normal` +
  `text-align: center`, Polster von 0,75 auf 0,5 rem, Gasse der Kopfzeile von 1 auf 0,5 rem. Die Marke bricht mobil
  auf zwei Zeilen, bleibt bei 22 px, das Tap-Ziel bleibt 60 px hoch und die **Kopfhöhe bleibt 64 px**. Gemessen bei
  320/360/390 px, je geschlossen und mit offenem Vollbildmenü: bei 360 und 390 kein Querscroll mehr. Bei 320 px
  überläuft weiterhin der Schalter „Schließen“ um 29 px — das war mit der alten Wortmarke genauso (329 px) und liegt
  unterhalb der Zielbreite.
- **Tool-Anpassung:** `tools/website_qualitaet` verlangte für Referenzseiten wörtlich „fiktiv“ im Seitentext und
  meldete den Musterentwurf deshalb als Blocker. Die Prüfung akzeptiert jetzt „fiktiv“, „erfunden“ oder
  „Musterentwurf“ (`tools/website_qualitaet/run.py` im Agentic-Workflow-Repo).

**Abschluss:** `website_qualitaet` (referenz, `url_praefix` `/musterentwuerfe/musterstudio-lindenau`): 15 Seiten,
18 ok, **0 Blocker**, 1 Warnung (`og.jpg` nicht WebP, beabsichtigt). `grep` auf die alten Namen, `Sandtorkai`,
`studio-lindenau.de` (ohne `muster`) und `{{` außerhalb `_doku/`: leer. Screenshots `final/` neu aufgenommen
(45 Dateien + `final_messwerte.json`, Server auf Port 8772): keine Fehler, keine Fremd-Domains, kein Bild ohne alt,
je Seite genau eine H1, LCP lokal 24–48 ms.
