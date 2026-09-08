# Prüfbericht Studio Lindenau — 2026-09-07

**Ergebnis:** abgenommen (0 Blocker, 12 Warnungen)

Geprüft gegen `checklisten/qualitaet.md`, den Design-Brief (`_doku/design-brief.md`) und die
Referenz-Screenshots von pietboon-com, robmills-com-au, helenhard-no sowie die erste
XPO-Referenzseite Nordkant Architekten. Tool `website_qualitaet` (mit `url_praefix`
`/referenzen/studio-lindenau`): 15 Seiten, 18 Prüfungen ok, 0 Blocker, 1 Warnung.
Alle 45 Screenshots (15 Seiten × Desktop-Hero, Desktop-Full, Mobil-Full) gesichtet.

## Blocker

Keine.

## Warnungen

1. **Checkliste 5 (Datenschutz passend zur Technik)** — `/datenschutz/` nennt „STRATO AG,
   Otto-Ostrowski-Straße 7, 10249 Berlin" als Hoster mit Auftragsverarbeitung. Die Seite
   liegt unter `xponext.de/referenzen/…`; ob STRATO der tatsächliche Hoster ist, ist nicht
   belegt. Ein falscher Hoster in einer Datenschutzerklärung ist auch auf einer Demo ein
   Fehler, den ein Besucher nachschlagen kann. (15_datenschutz_desktop_full.jpg)
2. **Checkliste 3 (Fokus 3 px)** — Fokusring ist 2 px (`basis.css` Z. 131:
   `outline: 2px solid var(--farbe-akzent); outline-offset: 3px`), auf dunklen Sektionen in
   `--farbe-dunkel-akzent` (Z. 326). Der Brief (Abschnitt 9) schreibt selbst 2 px vor und
   widerspricht damit der Checkliste. Sichtbar ist der Ring auf beiden Untergründen, nur
   dünner als gefordert. Entscheidung Brief vs. Checkliste beim Nutzer.
3. **Brief 8 / Checkliste 5 (Bilder, die ein anderes Gebäude erzählen), nicht in Checkliste
   als eigener Punkt** — `/projekte/harvestehude/`: Text „Etagenwohnung aus den 1910er
   Jahren mit hohen Decken und Stuck"; Bild 3 (`harvestehude-02`) zeigt eine moderne
   Wohnung mit weißer Hochglanzküche und Kronleuchter, Bild 4 (`harvestehude-01`) eine
   Hochhaus-Skyline im Fenster (Pexels-Titel „modern dubai living room"). Der Brief
   (Abschnitt 11, Frage 2) hatte Ersatz für `harvestehude-01` vorgeschlagen; verbaut ist es
   trotzdem. Kein reales Gebäude als eigenes Projekt (kein Blocker), aber die Bilder
   widerlegen den Text. (03_projekte-harvestehude_desktop_full.jpg, unteres Bildpaar)
4. **Brief 8, nicht in Checkliste** — `/projekte/penthouse-berlin/`: Text „Dachgeschoss über
   einem Gründerzeithaus"; Bild 2 (`penthouse-02`) und Bild 3 (`penthouse-01`) zeigen je eine
   Hochhaus-Skyline durch Glasfronten. Prenzlauer Berg hat keine solche Skyline.
   (07_projekte-penthouse-berlin_desktop_full.jpg)
5. **Brief 8, nicht in Checkliste** — `/projekte/kampen/`: Text „Reetdachhaus … geweißte
   Dielen, Kalkputz, Leinen"; Bild 4 (`kampen-01`) zeigt Blockbohlenwände, Fernseher und
   ein rot-graues Nachbarhaus im Fenster — liest sich als skandinavisches Ferienhaus, nicht
   als Sylt. Der Brief nannte das Bild selbst als Grenzfall. (05_projekte-kampen_desktop_full.jpg)
6. **Brief 8, nicht in Checkliste** — `/projekte/praxis-eppendorf/`: Text „Wände in
   Kalkputz, Boden in warmem Grau, Einbauten aus hellem Holz"; alle vier Bilder zeigen
   weiße Klinikräume, Bild 2 (`praxis-04`) mit kräftig blauem Behandlungsstuhl, Bild 4
   (`praxis-01`) ein Instrumenten-Detail ohne Raum (Brief 11: „sollte ersetzt werden").
   (06_projekte-praxis-eppendorf_desktop_full.jpg)
7. **Brief 4 (Palette) / Brief 11, nicht in Checkliste** — `/projekte/kanzlei-hafencity/`:
   Bild 4 (`kanzlei-hafencity-01`) ist eine kräftig blaue Wand über die halbe Bildfläche,
   Bild 2 hat einen leuchtend blauen Teppich. Der Brief nennt `kanzlei-01` selbst als
   palettenbrechend und legt es „ans Ende" — es steht trotzdem groß auf der Seite.
   (10_projekte-kanzlei-hafencity_desktop_full.jpg)
8. **Brief 6 (Detailseite „vier Bilder")** — `/projekte/hotel-speicherstadt/` hat drei Bilder,
   weil `hotel-speicherstadt-04` (Person auf Badewanne) korrekt nicht verwendet wird. Das
   dritte Bild steht allein in der linken Spalte des F7-Paar-Rasters (560 px), rechts bleibt
   die Fläche leer — auf Desktop sichtbar unfertig. Brief 11 Frage 1 hatte als Alternative
   „Bild 3 allein statt als Paar" genannt, gemeint war aber ein Einzelbild in voller Breite.
   (08_projekte-hotel-speicherstadt_desktop_full.jpg, Bereich unter dem Fließtext)
9. **Brief 5 (Mobil: Studio-Kasten „Bild oben, Kasten darunter")** — auf `/studio/` steht
   mobil der Kasten „Wie wir arbeiten" über dem Bild, nicht darunter. Layout ist sauber,
   nur die Reihenfolge weicht vom Brief ab. (11_studio_mobile_full.jpg)
10. **Nicht in Checkliste (Lesbarkeit)** — Der 40–80-Wörter-Absatz in der Randspalte der
    Detailseiten ist rechtsbündig gesetzt (gemeinsame Kante zum Bild, big-dk-F3), dadurch
    Flatterrand links über 11–13 Zeilen bei 280 px Breite. Der Brief verlangt die
    Rechtsbündigkeit nur für die Metadaten; für den Absatz ist sie eine Auslegung des
    Bauers. (03_projekte-harvestehude_desktop_full.jpg, linke Spalte)
11. **Tool-Warnung (Checkliste 1)** — `assets/bilder/og.jpg` ist kein WebP. Laut
    `BILDER.md` bewusst JPEG, weil Vorschau-Crawler WebP nicht zuverlässig lesen —
    begründet, stehen lassen.
12. **Nicht in Checkliste (Textdetail)** — `/datenschutz/`, Abschnitt „Ihre Rechte":
    „Zuständig ist Der Hamburgische Beauftragte …" — Großschreibung von „Der" mitten im
    Satz. (15_datenschutz_desktop_full.jpg)

## Messwerte

Lokal, `tools/website_screenshot` mit `lokal: true`. Keine Fremd-Domain auf einer der 15
Seiten, kein Google Fonts, kein horizontales Scrollen bei 390 px.

| Seite | Transfer | LCP | Fremd-Domains | Mobil-Querscroll |
|---|---|---|---|---|
| / | 449 KB | 76 ms | keine | nein |
| /projekte/ | 482 KB | 32 ms | keine | nein |
| /projekte/harvestehude/ | 433 KB | 32 ms | keine | nein |
| /projekte/restaurant-fleet/ | 622 KB | 36 ms | keine | nein |
| /projekte/kampen/ | 449 KB | 36 ms | keine | nein |
| /projekte/praxis-eppendorf/ | 303 KB | 32 ms | keine | nein |
| /projekte/penthouse-berlin/ | 389 KB | 32 ms | keine | nein |
| /projekte/hotel-speicherstadt/ | 430 KB | 36 ms | keine | nein |
| /projekte/blankenese/ | 450 KB | 32 ms | keine | nein |
| /projekte/kanzlei-hafencity/ | 492 KB | 36 ms | keine | nein |
| /studio/ | 313 KB | 28 ms | keine | nein |
| /leistungen/ | 178 KB | 24 ms | keine | nein |
| /kontakt/ | 176 KB | 24 ms | keine | nein |
| /impressum/ | 177 KB | 24 ms | keine | nein |
| /datenschutz/ | 179 KB | 24 ms | keine | nein |

Startseite: 9 Requests; 274 KB Bilder, 101 KB Fonts (3 woff2: Cormorant Garamond normal +
italic, DM Sans), 69 KB CSS, 4 KB JS, 12 KB HTML. Hero-Bild `hero-1440.webp` 66 KB (≤ 250 KB),
`fetchpriority="high"`, ohne `loading="lazy"`; größtes Bild der Startseite
`restaurant-fleet-02-960.webp` 125 KB. Größte Einzeldatei der Site
`kacheln/restaurant-fleet-02-1440.webp` 209 KB (≤ 300 KB).

## Checkliste — Sichtprüfung [A]

**1. Performance**
- Kein render-blockendes JS: nur ein Inline-Einzeiler (`js`-Klasse) im Head, `basis.js` mit
  `defer` am Body-Ende, JSON-LD danach.
- Kein Preloader, kein Intro-Overlay: Hero-Screenshot zeigt sofort Satz und Bild
  (01_start_desktop_hero.jpg).

**2. Fonts und Datenschutz**
- Kein Kontaktformular (Brief 6: bewusst nur Telefon und `mailto:`); `grep "<form"` leer.
- Kein Cookie, kein `localStorage` in `basis.js`; Datenschutzerklärung sagt korrekt „ohne
  Cookies, ohne Analyse-Werkzeuge, ohne Kontaktformular". Kein Banner.

**3. Barrierefreiheit**
- Fokus: `:focus-visible` Outline 2 px `#7A5F3E` mit 3 px Abstand auf hell, `#C9A97E` in
  Kopfzeile, dunklen Sektionen und Fußzeile — sichtbar auf beiden Gründen, aber 2 statt
  3 px (Warnung 2). Skip-Link „Zum Inhalt springen" als erstes fokussierbares Element,
  bei Fokus eingeblendet (`.sprung:focus { left: 0 }`).
- Menü-Button: `<button aria-expanded="false" aria-controls="hauptnavigation">Menü`,
  Text wechselt zu „Schließen", Escape schließt und setzt Fokus auf den Button zurück,
  Tab-Fokusfalle im Overlay, Klick auf Link schließt, Fokus geht auf den ersten Link
  (`basis.js` Z. 11–45).
- Kontrast: Brief-Werte per WCAG-Formel gerechnet (Text-3 `#665E56` 5,64:1 auf Grund,
  Dunkel-Text-3 `#9E978B` 5,81:1 auf Kohle, Akzent-Button `#1F1D1A` auf `#C9A97E`
  7,57:1). Die Screenshots zeigen die 12-px-Ort-Zeilen auf Kohle lesbar, wenn auch als
  leiseste Textform der Seite (01_start_desktop_full.jpg, „HAMBURG · 2024").
- Text auf Bild: nirgends. Navigation liegt auf der dunklen Fläche, Hero-Satz neben dem
  eingerückten Bild, Projekttitel über und Ort-Zeile unter dem Bild (01, 02).
- `prefers-reduced-motion`: alle Animationen (Hero-Einblenden, Lazy-Fade, wachsende Linie,
  Hover-Zoom) stehen ausschließlich in `@media (prefers-reduced-motion: no-preference)`;
  unter `reduce` zusätzlich Transitions auf 0,01 ms, `basis.js` zeigt alle Bilder sofort und
  setzt die Linie auf volle Länge. Ohne JS keine `opacity: 0` (nur `.js`-Selektor).
- Tap-Ziele: `min-height: 44px` auf Nav-Links, Menü-Button, Chevron-Liste (52 px),
  Telefon-/Mail-Links, Fußzeilen-Links, Buttons (`basis.css` Z. 216–609). Mobil-Screenshots
  zeigen ausreichend Abstand zwischen den Fußzeilen-Links (01_start_mobile_full.jpg).
- Hover nie einziger Weg: Projekttitel und Ort stehen ohne Hover sichtbar
  (02_projekte_desktop_full.jpg); Hover ergänzt nur Unterstreichung und 2 %-Zoom.

**4. SEO-Grundstruktur**
- Sprechende Ordner-URLs für alle 15 Seiten, keine `.html`-Endungen.
- Ortsbezug im sichtbaren Text der Startseite: Intro „Büro für Innenarchitektur in
  Hamburg … in Norddeutschland", Ort-Zeilen HAMBURG/SYLT/BERLIN, Fußzeile „Hamburg, HafenCity"
  (01_start_desktop_full.jpg).
- `title` 27–54 Zeichen, `description` 62–153 Zeichen, alle 15 unterschiedlich.
- JSON-LD `ArchitectOffice` mit Adresse, Telefon, `areaServed` [Hamburg, Norddeutschland,
  Berlin, Sylt] auf der Startseite. Sitemap 13 URLs (ohne Impressum/Datenschutz), robots.txt
  erlaubt GPTBot, ClaudeBot, PerplexityBot ausdrücklich.
- Leistungen als eigene Seiten: nur bei Kundenseiten gefordert; hier eine `/leistungen/` mit
  Ankern, dem Brief entsprechend.

**5. Rechtliches**
- Impressum: § 5 DDG, Hamburgische Architektenkammer mit Anschrift, Berufsbezeichnung
  „Innenarchitektin (verliehen in der Bundesrepublik Deutschland)", Berufshaftpflicht
  „(fiktiv)", USt-IdNr. `DE000000000`, Absatz „Das Büro, die Personen und die Projekte sind
  fiktiv" (14_impressum_desktop_full.jpg).
- Datenschutz passt zur Technik (keine Cookies, keine Einbettungen, E-Mail/Telefon) — bis
  auf den nicht belegten Hoster (Warnung 1).
- Bildnachweis: alle 98 im HTML referenzierten Bilddateien nachvollziehbar —
  `hero/*`, `kacheln/*`, `og.jpg`, `icon.svg` in `assets/bilder/BILDER.md` mit Quellverweis
  auf die Projektdatei; die 31 per `srcset 1920w` direkt referenzierten `projekte/*.webp` im
  Quellregister `assets/bilder/projekte/BILDER.md` mit Fotograf und Pexels-URL.
  `hotel-speicherstadt-04.webp` (Person) wird auf keiner Seite verwendet (grep leer).
- `noindex, follow` auf allen 15 Seiten; Demo-Hinweis „DEMO-WEBSITE VON XPONEXT. BÜRO UND
  PROJEKTE SIND FIKTIV, DIE FOTOGRAFIE IST STOCKMATERIAL." in jeder Fußzeile.
- Keine erkennbaren Personen als Team: Teamliste auf `/studio/` ist reiner Text, kein
  Portrait. Das einzige Bild mit Person (hotel-04) ist unbenutzt. Im Hotel-Hero
  (`hotel-speicherstadt-03`) hängt ein Schwarzweiß-Foto mit Personen als Wandbild — Kunst im
  Raum, nicht als Team ausgegeben. Keine lesbaren Hausnummern oder Schilder: im
  Restaurant-Hero ein kleines farbiges Logo-Schild und eine Tafel an der Wand, bei 1440 px
  nicht lesbar; im Kanzlei-Hero ein Neon-Schriftzug an der Wand, unleserlich klein.
- Reale Gebäude: kein Bild zeigt ein bekanntes reales Gebäude als eigenes Projekt. Die
  Pexels-Titel verraten aber Orte, die den Projekttexten widersprechen (Dubai, Miami Beach) —
  siehe Warnungen 3 und 4; Alt-Texte enthalten keine Ortsbehauptungen außer dem Projektnamen.

**6. Mobile (390 px)**
- Alle 15 Mobil-Screenshots: nichts abgeschnitten, nichts überlappt. Bilder auf volle
  Containerbreite, F7-Paar gestapelt ohne Versatz, Metadaten zweispaltig.
- Hero mobil: Satz in 38 px über dem Bild, Hero endet deutlich vor dem Fensterende
  (01_start_mobile_full.jpg, oberer Bereich). Desktop `min-height: clamp(560px, 85vh, 900px)`.
- Navigation mobil: drei Textelemente „Kontakt · Studio Lindenau · Menü" (helenhard-F12),
  Vollbild-Overlay `position: fixed; inset: 0` auf Kohle, schließt nach Auswahl (JS).

**7. Brief-Treue** — siehe Tabelle unten. Wow-Faktor auf dem Hero erkennbar: dunkle Fläche,
ein Satz in leichter Cormorant 64 px, eingerücktes Bild rechts mit gemeinsamer Unterkante
(01_start_desktop_hero.jpg); die Bildfolge darunter als große Einzelbilder mit zwei Textzeilen
auf Kohle (01_start_desktop_full.jpg).

## Brief-Treue

| Feature-ID | umgesetzt | Beleg (Screenshot) |
|---|---|---|
| pietboon-com-F11 (Detail-Hero 16:9 eingerückt, Titel darunter; Prinzip des Start-Heros) | ja | 03_projekte-harvestehude_desktop_hero.jpg (Bild volle Containerbreite auf Kohle, H1 + Kursivzeile darunter); 01_start_desktop_hero.jpg (Bild eingerückt rechts, 70 %) |
| pietboon-com-F2 (Grund + Fläche + ein Akzent, gespiegelt für dunkel) | ja | 01_start_desktop_full.jpg: Off-White-Grund, Sand-Kasten der Studio-Sektion, Kontaktkasten `#2A2724` auf Kohle, einziger gefüllter Button in Messing |
| pietboon-com-F15 (zentrierter Intro-Block mit Chevron-Liste) | ja | 01_start_desktop_full.jpg, erste helle Sektion: ein Absatz, fünf Zeilen mit Chevron und Hairlines |
| pietboon-com-F6 (versetzter Kasten, Bild überlappt) | ja | 01_start_desktop_full.jpg Studio-Sektion; 11_studio_desktop_full.jpg (Bild ragt in den Kasten) |
| pietboon-com-F7 (zwei Fotos, ungleiche Höhe, versetzter Beginn) | ja | 03_projekte-harvestehude_desktop_full.jpg unteres Paar (links 3:2 tiefer, rechts 4:3 höher); 11_studio_desktop_full.jpg |
| helenhard-no-F7 (Titel zentriert über Bild, Zeile darunter) | ja | 01_start_desktop_full.jpg (4 Projekte), 02_projekte_desktop_full.jpg (8 Projekte) |
| big-dk-F4 (Ort in Versalien als Untertitel) | ja | 02_projekte_desktop_full.jpg: „HAMBURG · 2024", „SYLT · 2023", „BERLIN · 2023" |
| big-dk-F2 (Metadatenblock rechtsbündig neben dem Bild) | ja | 04_projekte-restaurant-fleet_desktop_full.jpg: ORT / FERTIGSTELLUNG / LEISTUNG / FLÄCHE rechtsbündig an der Bildkante |
| big-dk-F3 (gemeinsame Kante statt Zentrierung) | ja | 01_start_desktop_hero.jpg (Satz-Unterkante = Bild-Unterkante); Randspalte/Bild auf allen Detailseiten; Fußzeilen-Spalten 13_kontakt_desktop_full.jpg |
| helenhard-no-F4 (leichte Serife, Kursiv als einzige Auszeichnung) | ja | Cormorant Garamond 300 im Hero (64 px, gemessen), Kursivzeile unter H1 (03_…_desktop_hero.jpg), Fußzeile „Hamburg, HafenCity" kursiv |
| helenhard-no-F1 (geteilte Navigation, Wortmarke mittig) | ja | 01_start_desktop_hero.jpg: Projekte · Studio — Studio Lindenau — Leistungen · Kontakt, kein CTA in der Leiste |
| helenhard-no-F12 (Mobile-Kopfzeile aus drei Textelementen) | ja | 01_start_mobile_full.jpg: „Kontakt" links, Wortmarke mittig, „Menü" rechts; `aria-expanded`/`aria-controls` im HTML |
| helenhard-no-F13 (Footer mit Standort-Block) | ja | 13_kontakt_desktop_full.jpg: „Hamburg, HafenCity" kursiv, Anschrift, Telefon, Mail; daneben Navigation, Rechtliches |
| robmills-com-au-F3 (wachsende vertikale Linie) | ja | 01_start_desktop_full.jpg: 1-px-Linie mittig aus dem Hero in die Intro-Sektion (Full-Screenshot nach Scroll, Linie in voller Länge) |
| robmills-com-au-F10 (Lazy-Fade der Bilder) | ja | `bild--anim` auf allen Bildern ab dem zweiten je Seite (Startseite 5), IntersectionObserver 15 %/−10 %, `loading="lazy"` 37×, `width`/`height` überall (Tool: 0 ohne Maße); im Full-Screenshot alle Bilder sichtbar |

**Abschnitt 10 („bewusst nicht") — nichts davon verbaut:** kein Slider/Karussell (grep
`slider|carousel|swiper` leer, keine Pfeile in Screenshots), kein Video (`<video>` 0, Tool:
0 Videos), kein randloser Vollbild-Hero (Bild eingerückt, 01), keine Navigation auf dem
Bild, kein Dreier-Raster/Kachelfuß (ein Bild je Reihe, 02), kein Typologie-Filter
(Kopf von `/projekte/` ist eine Klartextzeile), keine Bildpaar-Galerie mit wechselnden
Breiten (nur ein F7-Paar je Detailseite), kein Architekten-Zitat, keine zentrierte
Metadaten-Tabelle, keine Skizzen, kein Porträt-Statement, kein Weiß-auf-Taupe (Kohle
`#1F1D1A` gemessen `rgb(31,29,26)`), kein Login/Sprachwahl/Broschüre, keine Kopfzeile unten,
keine Newsliste, keine Karte/Suche/Filter auf `/kontakt/` (kein `iframe`), keine HubSpot-
Leiste, keine unsichtbare H1 (je Seite genau eine sichtbare H1, Tool), Rechtstexte in der
Fußzeile, kein Tracking (0 Fremd-Domains), kein Lazy Loading ohne Maße, kein Cookie-Banner.
Kopfzeile statisch: Skeleton-`sticky` (Z. 200) wird in Z. 346 mit `position: static`
überschrieben — im Full-Screenshot bleibt die Leiste oben.

## Nachbildungs-Vergleich

- **pietboon-com** (01_start_desktop_hero/full): hellgrauer Grund, Hero-Slider mit Text auf
  Bild und Pfeilen, zweizeilige Kopfzeile mit Login/Sprache/Brochure-Button, Dreier-Kacheln
  mit Karussell, Produktbereich. Lindenau: Kohlegrund, statisches eingerücktes Bild,
  einzeilige geteilte Navigation, ein Bild je Reihe. Übernommen sind nur Kompositions-
  prinzipien (Kasten mit überlappendem Bild, Intro-Block) — keine Nachbildung.
- **robmills-com-au** (01_start_desktop_hero/full): fensterhohes Video mit Bildmarke, Taupe-
  Grund mit Weiß, horizontaler Hochformat-Slider, Schwarzweiß-Porträt. Lindenau hat davon
  nur die wachsende Linie und das Einblenden — keine Nachbildung.
- **helenhard-no** (01_start_desktop_hero/full, 02_work): Off-White-Grund, große
  Fraunces-artige Wortmarke, randloses Hero-Video, Handskizzen-Ebene, Newsliste, zweispaltiges
  Projektraster mit kursiven Untertitelsätzen, Graubraun-Footer. Lindenau teilt die geteilte
  Navigation mit Text-Wortmarke und „Titel über dem Bild" — auf Kohle statt Off-White,
  einspaltig, ohne Skizzen, ohne News. Erkennbar eigene Seite.
- **Nordkant Architekten** (nordkant …/final/01_start_desktop_full.jpg): warmes Off-White
  durchgehend, randloses Vollbild-Hero-Foto, Fraunces, Ziegel-Akzent, zweispaltiges
  Projektraster mit Kursiv-Unterzeile, Kontaktkasten hell. Lindenau: Kohle-Kopf mit
  eingerücktem Bild, Cormorant/DM Sans, Hell-Dunkel-Wechsel, ein Bild je Reihe, Messing-
  Akzent. Beide XPO-Referenzseiten unterscheiden sich auf den ersten Blick — keine Warnung.

## Was gut ist

1. Der Hero: Kohlefläche, ein Satz in Cormorant 300, eingerücktes Eichen-Küchenbild mit
   gemeinsamer Unterkante — genau der Wow-Faktor des Briefs, ohne zweiten Effekt. Nicht
   anfassen (01_start_desktop_hero.jpg).
2. Technik und Recht sind sauber: 0 Fremd-Requests, 3 woff2 self-hosted, LCP lokal 24–76 ms,
   Startseite 449 KB, `noindex` und Demo-Hinweis überall, vollständige Bildkette
   (HTML → kacheln/BILDER.md → projekte/BILDER.md mit Pexels-URL), Menü mit Escape,
   Fokusfalle und `aria-*`, alles unter `prefers-reduced-motion` abgeschaltet.
3. Rhythmus und Typografie: Hell-Dunkel-Folge dunkel · hell · dunkel · hell · dunkel auf
   der Startseite, ein Bild je Reihe abwechselnd links/rechts, Ort-Versalien in 12 px als
   leiseste Textform, Metadaten-Randspalte rechtsbündig an der Bildkante. Das trägt die
   Seite auch dort, wo Fotos schwächer sind.

## Gesichtete Screenshots

`_doku/screenshots/` (Lauf `pruefung`, 2026-09-07):

01_start_desktop_hero.jpg · 01_start_desktop_full.jpg (bei 6000 px abgeschnitten, Fußzeile
über Mobil und Unterseiten geprüft) · 01_start_mobile_full.jpg ·
02_projekte_desktop_hero.jpg · 02_projekte_desktop_full.jpg (bei 6000 px abgeschnitten) ·
02_projekte_mobile_full.jpg ·
03_projekte-harvestehude_desktop_hero.jpg · 03_projekte-harvestehude_desktop_full.jpg · 03_projekte-harvestehude_mobile_full.jpg ·
04_projekte-restaurant-fleet_desktop_hero.jpg · 04_projekte-restaurant-fleet_desktop_full.jpg · 04_projekte-restaurant-fleet_mobile_full.jpg ·
05_projekte-kampen_desktop_hero.jpg · 05_projekte-kampen_desktop_full.jpg · 05_projekte-kampen_mobile_full.jpg ·
06_projekte-praxis-eppendorf_desktop_hero.jpg · 06_projekte-praxis-eppendorf_desktop_full.jpg · 06_projekte-praxis-eppendorf_mobile_full.jpg ·
07_projekte-penthouse-berlin_desktop_hero.jpg · 07_projekte-penthouse-berlin_desktop_full.jpg · 07_projekte-penthouse-berlin_mobile_full.jpg ·
08_projekte-hotel-speicherstadt_desktop_hero.jpg · 08_projekte-hotel-speicherstadt_desktop_full.jpg · 08_projekte-hotel-speicherstadt_mobile_full.jpg ·
09_projekte-blankenese_desktop_hero.jpg · 09_projekte-blankenese_desktop_full.jpg · 09_projekte-blankenese_mobile_full.jpg ·
10_projekte-kanzlei-hafencity_desktop_hero.jpg · 10_projekte-kanzlei-hafencity_desktop_full.jpg · 10_projekte-kanzlei-hafencity_mobile_full.jpg ·
11_studio_desktop_hero.jpg · 11_studio_desktop_full.jpg · 11_studio_mobile_full.jpg ·
12_leistungen_desktop_hero.jpg · 12_leistungen_desktop_full.jpg · 12_leistungen_mobile_full.jpg ·
13_kontakt_desktop_hero.jpg · 13_kontakt_desktop_full.jpg · 13_kontakt_mobile_full.jpg ·
14_impressum_desktop_hero.jpg · 14_impressum_desktop_full.jpg · 14_impressum_mobile_full.jpg ·
15_datenschutz_desktop_hero.jpg · 15_datenschutz_desktop_full.jpg · 15_datenschutz_mobile_full.jpg

Die Desktop-Hero-Screenshots sind der obere Ausschnitt der jeweiligen Full-Screenshots und
wurden über diese gesichtet.

Referenzen: `knowledge/design_library/architektur/_screens/pietboon-com/01_start_desktop_hero.jpg`,
`…/01_start_desktop_full.jpg`, `…/03_private-projects-haarlem-canal-house_desktop_full.jpg`;
`…/robmills-com-au/01_start_desktop_hero.jpg`, `…/01_start_desktop_full.jpg`,
`…/03_architecture-howqua-river-lodge_desktop_full.jpg`; `…/helenhard-no/01_start_desktop_hero.jpg`,
`…/01_start_desktop_full.jpg`, `…/02_work_desktop_full.jpg`;
`referenzen/nordkant-architekten/_doku/screenshots/final/01_start_desktop_full.jpg`.
