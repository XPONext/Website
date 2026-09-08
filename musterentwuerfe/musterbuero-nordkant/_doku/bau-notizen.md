# Bau-Notizen: Nordkant Architekten

Rolle Bauer, 2026-09-07. Grundlage: `design-brief.md` (Vorgabe) und `inhalte.md`.

## Entscheidungen zu Abschnitt 11 des Briefs (offene Fragen)

1. **Wohnfläche je Projekt:** Vorschlag übernommen, fünfter Metadaten-Eintrag ist „Wohnfläche" mit
   fiktiven Werten: Haus am Deich 185 m², Hofstelle 240 m², Anbau 45 m² Erweiterung, Kreuzviertel
   160 m², Aufstockung 60 m² Dachgeschoss, Haus im Wald 150 m². Durch den Demo-Hinweis abgedeckt.
2. **Kursive Untertitel-Sätze** (helenhard-no-F7), je 6–10 Wörter:
   - Haus am Deich: „Ein Holzhaus hinter dem Deich, für drei Generationen."
   - Umbau Hofstelle: „Ein Backsteinhof, der zum Wohnhaus wird und seine Tenne behält."
   - Anbau Gartenhaus: „Ein gläserner Raum zwischen Haus und Garten, zu jeder Jahreszeit."
   - Wohnhaus Kreuzviertel: „Ein Stadthaus in Backstein auf sieben Metern Breite."
   - Aufstockung Reihenhaus: „Ein neues Geschoss aus Holz, in vier Wochen aufgesetzt."
   - Haus im Wald: „Ein Haus zwischen Kiefern, mit Türen nach allen Seiten."
3. **Kreuzviertel-Bilder:** `kreuzviertel-02.webp` ist inzwischen ein anderes Motiv (Backsteinfassade
   mit Eingangstreppe, Nachlieferung 18:22) — das Duplikat-Problem aus dem Brief besteht nicht mehr,
   das Projekt hat drei Bilder. Erstbild (Kachel und Projekt-Hero) ist `-02`; `-01` (Reihenhausanlage
   mit Verkaufszelt) steht nur als kleines rechtes Bild im Bildpaar, `-03` als großes linkes.
   Kein neues Bild nachgeladen (Vorgabe).
4. **Hofstelle-Erstbild:** wie vorgeschlagen `hofstelle-03` (Treppenhaus) als Kachel und Projekt-Hero,
   `hofstelle-01` (Landhausküche) als drittes Bild.
5. **Mobile-Hero:** Vollhöhe auch mobil beibehalten. In der Hero-Probe bei 390 × 844 bleiben Haus
   und Waldkante mit `object-position: 66% 50%` im Ausschnitt (Wert aus dem Brief für den Fall,
   dass 62 % nicht reicht; 62 % schnitt den Holzkörper rechts stärker an).
6. **Button-Beschriftung:** „Projekt besprechen".
7. Notiz für den nächsten Brief (Innenarchitektur-Referenz nicht Fraunces) — hier keine Entscheidung.

## Weitere Entscheidungen des Bauers

- **Gartenhaus-Erstbild:** `gartenhaus-03` (Glasanbau mit grünem Giebel) statt `gartenhaus-01`
  (vom Brief als „unruhig, alpin" bewertet). `-01` und `-02` bilden das Bildpaar.
- **Haus im Wald:** `inhalte.md` nennt „Neubau Bungalow", das Hero-/Kachelmotiv zeigt aber zwei
  Geschosse. Text und Metadaten sagen deshalb „Neubau Einfamilienhaus, zwei versetzt gestapelte
  Geschosse" — kein Widerspruch zwischen Bild und Text.
- **Hero-Datei:** `hero.webp` lag mit 259 KB über der 250-KB-Grenze. Neu exportiert aus der
  1920-px-Fassung in `.tmp/hero/hero-01.webp` (gleiche Quelle 7598374): 1440 px bei q66 = 237 KB
  als `src` und 1440w-Kandidat, dazu `hero-960.webp` (110 KB) als 960w-Kandidat. Die vom Brief
  gewünschte 1920er-Stufe wäre bei diesem Motiv (Wald, viel Detail) erst ab ~420 KB scharf und
  wurde zunächst weggelassen — in der Nachbesserung als `hero-1920.webp` (372 KB) ergänzt, siehe unten.
- **Kacheln:** eigene Dateien unter `assets/bilder/kacheln/` (1222 × 815, 3:2, 37–233 KB) statt
  der 1600–1920-px-Quellbilder — Startseite bleibt so unter 1,5 MB (gemessen ~1,2 MB).
- **Statement-Bild:** `statement.webp` (1000 × 1250, 4:5-Ausschnitt aus `aufstockung-01`).
- **Nachverdichtet:** `gartenhaus-03` (320 → 270 KB, auf 1280 px) und `kreuzviertel-02`
  (302 → 287 KB, q66), beide waren über 300 KB.
- **Fonts:** Der Brief nennt eine Familie (Fraunces). Nur `fraunces-latin.woff2` und
  `fraunces-latin-italic.woff2` behalten (149 KB), alle anderen Dateien und @font-face-Blöcke
  gelöscht. Kein Inter, obwohl im Bauauftrag erwähnt — der Brief ist die Vorgabe.
- **Kein Kontaktformular:** Brief 6 und 10 schließen es aus. `formular.php` und `danke/` sind seit der
  Nachbesserung gelöscht (siehe unten). Die Datenschutzerklärung beschreibt deshalb nur E-Mail/Telefon und Hosting, keinen
  Formular-Absatz.
- **Relative Pfade** auf allen Seiten (`assets/…`, `../assets/…`, `../../assets/…`), damit die Seite
  lokal unter `/` und live unter `/referenzen/nordkant-architekten/` läuft. Absolute Pfade nur in
  `canonical`, `og:image`, `sitemap.xml`, `robots.txt` und den PHP-Redirects.
- **`og.jpg`** (1200 × 630 aus dem Hero) angelegt, obwohl optional — als JPEG, weil Vorschau-Crawler
  WebP nicht zuverlässig lesen. Das Tool warnt „nicht als WebP", das ist beabsichtigt.
- **`.htaccess`:** HTTPS-Regel auf `%{REQUEST_URI}` umgestellt, weil die Skeleton-Regel im
  Unterordner den Präfix verlieren würde. Keine www-Regel (regelt die Hauptdomain).
- **Statement-Kasten:** Der Brief beschreibt den Kasten „von der linken Fensterkante bis 55 %".
  Damit das Bild den Kasten tatsächlich überlappt (pietboon-com-F6), reicht die Fläche bis
  ~3 rem in die rechte Spalte; das Bild hängt 4 rem oben über (mobil 2 rem).
- **Bildnachweis:** Quellregister ist `assets/bilder/projekte/BILDER.md` (alle Quellbilder mit Fotograf
  und Pexels-URL), `assets/bilder/BILDER.md` listet nur die abgeleiteten Dateien (Stand Nachbesserung).

## Hero-Probe (Schritt 2)

Screenshots: `_doku/screenshots/hero-probe/01_start_desktop_hero.jpg`, `…_desktop_full.jpg`,
`…_mobile_full.jpg`. Desktop 1440 × 900: Kopfzeile 88 px auf Fläche, Bild randlos bis 844 px,
Bildzeile „HAUS IM WALD · NOTTULN · 2021" als einzige Zeile darunter — der eine Wow-Faktor aus
dem Brief ist da, nichts liegt auf dem Bild. Mobil 390 × 844: Hero ~732 px hoch, Haus und
Waldkante im Bild. Messwerte lokal: 5 Requests, 426 KB, LCP 96 ms, keine Fremd-Domains.
Keine Nachbesserung nötig.

## Offener Punkt für Prüfer und Nutzer (erledigt)

Der ursprünglich hier notierte unvollständige Bildnachweis ist erledigt: Der Prüfer hat alle Quellen per
Bildvergleich rekonstruiert (`assets/bilder/projekte/BILDER.md`), die widersprüchliche Tabelle in
`assets/bilder/BILDER.md` wurde in der Nachbesserung entfernt.

## Tool-Ergebnis (Schritt 4)

`tools/website_qualitaet` mit `referenz: true`, letzter Lauf 2026-09-07 nach Abschluss: 14 Seiten,
**0 Blocker**, 23 Warnungen, davon:
- 22 × Sitemap: „Seite fehlt in sitemap.xml" / „nennt nicht vorhandene Seite". Das Tool vergleicht
  URL-Pfade relativ zur Site-Wurzel; die Sitemap trägt korrekt den Live-Präfix
  `/referenzen/nordkant-architekten/…`. Stehen gelassen, weil die Sitemap für den Live-Ort stimmen
  muss. (Bei `noindex` ohnehin ohne Wirkung.)
- 1 × `og.jpg` nicht als WebP: beabsichtigt, siehe oben.
`grep -rn "{{"` außerhalb `_doku/` ist leer.

`tools/website_screenshot` (lokal, 14 Seiten): kein horizontales Scrollen bei 390 px auf keiner
Seite, keine Fremd-Domains, Startseite 1.240 KB Transfer, LCP lokal 100–104 ms, alle Bilder mit
`alt`. Mobile-Menü geprüft: Schalter wechselt „Menü" ↔ „Schließen", `aria-expanded` folgt,
Escape schließt, Klick auf einen Punkt schließt. Behobener Fehler dabei: Chrome wendet
`justify-self` auch auf Block-Boxen an, die beiden Listen schrumpften im Ausklappmenü auf
Textbreite — im Mobile-Block auf `justify-self: auto` gesetzt.

Screenshots: `_doku/screenshots/final/` (42 Dateien, je Seite `desktop_hero`, `desktop_full`,
`mobile_full`, nummeriert 01–14 in der Reihenfolge Start, Projekte, sechs Projektseiten, Büro,
Leistungen, Kontakt, Impressum, Datenschutz, Danke).
- Generator für alle Seiten liegt als `_doku/build.py` bei (python3 _doku/build.py baut alle 14 Seiten und die Sitemap neu; Pfad zur Site steht oben im Skript).

## Nachbesserung nach Prüfbericht (2026-09-07, zweiter Bauer)

Grundlage: `_doku/pruefbericht.md` (0 Blocker, 12 Warnungen). Alle Seiten über `_doku/build.py` neu
gebaut, HTML nicht von Hand gepatcht. `danke/` und `formular.php` sind aus dem Generator entfernt.

1. **Bildnachweis (Warnung 2):** `assets/bilder/BILDER.md` neu geschrieben — enthält nur noch die
   abgeleiteten Dateien (Kacheln, Statement, Hero-Stufen, og.jpg, Icon) mit Verweis auf die Quelldatei
   und Pexels-ID; die 17 „nachzutragen"-Zeilen und der falsche Offene-Punkt-Absatz sind weg. Quellregister
   bleibt `assets/bilder/projekte/BILDER.md` (dort `hero-1920.webp` ergänzt, `kreuzviertel-02` ersetzt).
2. **kreuzviertel-02 (Warnung 3):** Bild getauscht. Suche `modern brick townhouse facade minimal` plus
   drei weitere `nur_suchen`-Läufe; von den Treffern ohne `warnung` zeigten 33162457 und 26735733 wieder
   Hausnummern, 19563032 eine Person. Gewählt: Pexels 14128509 (Jan van der Wolf), drei giebelständige
   Backsteinhäuser, keine Nummer, kein Schild, keine Person — passt zu „Stadthaus in Backstein auf sieben
   Metern". Export 1920 × 1280, q70 = 265 KB; Kachel `kacheln/kreuzviertel.webp` 1222 × 815, q75 = 119 KB.
   Alt-Text im Generator angepasst. Rohdatei liegt in `.tmp/kreuzviertel-ersatz/`.
3. **Hero 1920 (Warnung 4):** `projekte/hero-1920.webp` aus `.tmp/hero/hero-01.webp`, 1920 × 1281,
   q55 = **372 KB** (q58 399 KB, q62 424 KB). Über 300 KB, deshalb eine Tool-Warnung; bewusst als größte
   srcset-Stufe aufgenommen, `src` und 1440w bleiben `hero.webp` (244 KB). Playwright: bei 1440 px lädt der
   Browser `hero.webp`, bei 1920 px `hero-1920.webp`, mobil `hero-960.webp`.
4. **Tap-Ziele (Warnung 6), gemessen bei 390 px / 1440 px:** Chevron-Links 45,5 / 48,6 px (Padding
   0.6 rem; `margin-top` und `row-gap` der Liste so verrechnet, dass die Textkanten unverändert bleiben);
   Bildzeile 48 / 56 px (Link füllt die Zeile per `inline-flex`); „Alle sechs Projekte" und „Mehr über das
   Büro" 50 / 53 px (Padding mit negativem Rand, Zeilenhöhe unverändert); Telefon/Mail im Kontaktkasten
   45,5 / 48,6 px auf Startseite und `/kontakt/` — dafür sind die beiden Links jetzt Blocklinks
   (`.kontakt__wege`, kein `<br>` mehr), nicht überlappend; der Kasten wird ~30 px höher (mobil 266 px
   statt 236), Textkanten oben/unten bleiben. Footer-Links (30 px) nicht angefasst, waren nicht gefordert.
5. **Verwaiste Reste (Warnung 8):** `formular.php` und `danke/` gelöscht, `danke()` aus `build.py`
   entfernt, beide Disallow-Zeilen aus `robots.txt` raus. Sitemap unverändert (hatte `danke/` nie).
6. **LICENSES.md (Warnung 11):** Tabelle auf Fraunces reduziert.
7. **Nav-Kontrast (Warnung 7):** neues Token `--farbe-nav: #605B54` nur für inaktive Punkte in
   `.reiter a`. WCAG-Rechnung: **5,40:1** auf `--farbe-flaeche` (#EAE6DE), 6,07:1 auf Grund
   (`--farbe-text-3` lag bei 4,58 / 5,14). Kandidaten: #625D56 5,24 · #605B54 5,40 · #5E5952 5,57 —
   der hellste mit Reserve über 5 gewählt. Labels, Bildzeile und Metadaten bleiben auf `--farbe-text-3`.
8. **Gartenhaus-Kachel (Warnung 10):** von 239 KB auf 192 KB, dafür q45 nötig (q60 lag noch bei 219 KB);
   Sichtprüfung: Bambus und Glas ohne sichtbare Artefakte in Kachelgröße.

**Nicht behoben, offen für Tim (Warnung 9):** Glaubwürdigkeit der Zweit-/Drittbilder — `haus-am-deich-02`
(alpine Chalets mit Stromleitungen), `haus-im-wald-03` (Gebirge im Hintergrund), `gartenhaus-02`
(freistehendes Gewächshaus), `kreuzviertel-03` (Mietshaus von unten) passen nicht zur Münsterland-
Behauptung. Bildtausch nur nach Entscheidung des Nutzers; die Alt-Texte sind ehrlich, rechtlich ist es
über den Demo-Hinweis gedeckt. Ebenfalls unverändert: Warnung 1 (Kacheltitel linksbündig, Vorschlag an
den Nutzer), Warnung 12 (mobiler erster Bildschirm ohne Text, Brief-Vorgabe).

**Prüfung danach:** `website_qualitaet` (13 Seiten, 16 ok): 0 Blocker, 2 Warnungen — `og.jpg` nicht WebP
(beabsichtigt) und `hero-1920.webp` 372 KB (siehe 3). `grep -rn "{{"` außerhalb `_doku/` leer.
`website_screenshot` lokal: 39 Screenshots in `_doku/screenshots/final/` (13 Seiten × hero/full/mobile,
alte Dateien vorher gelöscht), kein Querscroll, keine Fremd-Domains, Startseite 1,23 MB Transfer,
LCP lokal 108 ms.

## Umbau zum Musterentwurf (2026-09-08)

Die Seite ist von einer Referenzseite mit erfundenen, aber real wirkenden Angaben zu einem offen
gekennzeichneten **Musterentwurf** geworden. Ordner und URL heißen jetzt
`musterentwuerfe/musterbuero-nordkant`. Alles über `_doku/build.py` geändert und neu gebaut, kein
HTML von Hand gepatcht. Design, Farben, Schriften, Layout, Projektnamen, Projektorte und Bilder
sind unverändert.

1. **Büroname:** „Nordkant Architekten" → **„Musterbüro Nordkant"** (Konstante `NAME`, dazu alle
   hart geschriebenen `<title>`- und Description-Texte). Die Rechtsform „Partnerschaft mbB" ist
   ersatzlos gestrichen — Fußzeile, Kontaktkasten, Impressum, Datenschutz.
2. **Personen raus.** Jonas Wiegand, Carla Reuter, Merle Fasching und Tobias Kahl kommen nirgends
   mehr vor, auch nicht in JSON-LD (`founder` entfernt), in Alt-Texten oder in Meta-Descriptions.
   Ersetzt durch Rollen: Startseite „Zwei Partner führen das Büro seit 2016 in Münster. Eine
   Architektin und ein Bauzeichner arbeiten an jedem Projekt mit …"; die Team-Liste auf `/buero/`
   nennt nur noch Qualifikation und Aufgabe (Dipl.-Ing., Architekt · Partner, Entwurf …), der
   Kammer-Satz spricht von „den Inhaberinnen und Inhabern" und erklärt in einem Halbsatz, warum
   keine Namen dastehen. Impressum: „Verantwortlich für den Inhalt: die Büroleitung (Musterangabe)".
3. **Anschrift:** „Hafenweg 12" → **„Musterstraße 1"**, PLZ und Stadt bleiben (48155 Münster), weil
   sie den regionalen Bezug der Projekte tragen. Umschrieben, wo der Hafenweg im Fließtext stand:
   Startseite „ein Tisch am Hafenweg" → „ein Tisch in Münster", „Büro mit vier Personen am Hafen in
   Münster" → „… in Münster", Büroseite „sitzt seit 2016 am Hafenweg" → „sitzt seit 2016 in
   Münster", Kontaktseite „Das Büro liegt am Stadthafen, Parkplätze gibt es am Hafenweg" →
   „Telefon und Anschrift sind Musterangaben".
4. **Telefon:** „0251 98 76 54-0" → **„0251 000000"**, `tel:`-Link `+49251000000`. Der Zusatz
   „(Musterangabe)" steht einmal je Seite dort, wo er hilft: im Impressum an der Nummer, auf
   `/kontakt/` in der Zeile unter den Öffnungszeiten. Nicht in Fußzeile und Kontaktkasten, sonst
   stünde er dreimal auf derselben Seite.
5. **E-Mail und Domain:** `info@musterbuero-nordkant.de`, Domain `musterbuero-nordkant.de`
   (als nicht registriert geprüft).
6. **Berufshaftpflicht:** die reale VHV Allgemeine Versicherung AG ist raus, an ihrer Stelle steht
   „Musterversicherung AG (Musterangabe), Musterstraße 1, 48155 Münster". Register („Amtsgericht
   Musterstadt, PR 0000") und USt-IdNr. sind ebenfalls als Musterangabe gekennzeichnet.
7. **URL-Basis** überall `https://www.xponext.de/musterentwuerfe/musterbuero-nordkant`: `canonical`,
   `og:image`, JSON-LD `@id`/`url`, `sitemap.xml` (Datum auf 2026-09-08) und die Sitemap-Zeile in
   `robots.txt`. Interne Pfade bleiben relativ, die Seite läuft weiter lokal unter `/`.
   `.htaccess` und `robots.txt` erzeugt `build.py` nicht — dort nur die Kopfkommentare und die
   Sitemap-URL angepasst.
8. **`noindex, follow`** steht unverändert auf allen 13 Seiten (geprüft).
9. **Hinweistexte:** Fußzeile jetzt „Musterentwurf von XPONext (xponext.de). Büro, Personen und
   Projekte sind erfunden, die Fotografie ist Stockmaterial." Der Impressum-Absatz sagt dasselbe und
   nennt zusätzlich Anschrift, Telefon, E-Mail, Register, Umsatzsteuer und Versicherung als
   Musterangaben. Datenschutz-Fußnote entsprechend. Das Wort „Demo" kommt im ausgelieferten Text
   nirgends mehr vor; die CSS-Klasse `.demo-hinweis` heißt weiter so (Struktur bleibt unverändert),
   der Kommentar daneben spricht vom Musterentwurf-Hinweis.
10. **Wortmarke geprüft.** „Musterbüro Nordkant" ist mit 19 Zeichen kürzer als „Nordkant
    Architekten" (20), passt also enger. Gemessen im Browser: bei 1440 px liegt die Marke 590–850,
    die linke Nav-Gruppe endet bei 358, die rechte beginnt bei 1135. Bei 901 px — der schmalsten
    Desktop-Breite vor dem Umbruch — Marke 321–580, links bis 248, rechts ab 706: 73 bzw. 126 px
    Luft, der Umbruchpunkt bei 900 px bleibt richtig. Mobil 390 px: Marke 21–223, Schalter „Menü"
    ab 318; selbst bei 320 px noch 29 px Abstand, kein Querscroll auf keiner Breite.

**Prüfung danach:** `tools/website_qualitaet` mit `referenz: true` und
`url_praefix: /musterentwuerfe/musterbuero-nordkant`: 13 Seiten, **0 Blocker**, 2 Warnungen — beide
alt und bewusst (`og.jpg` nicht als WebP, `hero-1920.webp` 372 KB). Die 22 Sitemap-Warnungen des
letzten Laufs sind weg, weil der Präfix jetzt zum Ordner passt.
`grep -rniE "wiegand|reuter|fasching|kahl|hafenweg|VHV|nordkant-architekten\.de"` außerhalb `_doku/`
ist leer, `grep -rn "{{"` ebenfalls.
`tools/website_screenshot` lokal auf Port 8771: 39 Screenshots in `_doku/screenshots/final/`
(13 Seiten × hero/full/mobile), alte Dateien vorher gelöscht — dabei auch der veraltete Satz, der
noch direkt in `_doku/screenshots/` lag und die gelöschte Seite `danke/` enthielt. Kein
horizontales Scrollen bei 390 px, keine Fremd-Domains, kein Bild ohne `alt`.
Hinweis zum Werkzeug: `website_screenshot` benennt die Dateien nach der eigenen Zählung
(`01_start`, dann `02_…` je Eintrag in `unterseiten`) und ignoriert `slug` für den Dateinamen —
alle Seiten müssen also in **einem** Aufruf über `unterseiten` übergeben werden, sonst überschreibt
jeder Aufruf `01_start_*`.
