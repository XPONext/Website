# Design-Brief: Steinwerk Planungsgesellschaft mbH

| | |
|---|---|
| **Projektart** | Referenz (fiktives Büro, `noindex, follow`, Demo-Hinweis in der Fußzeile, Impressum-Absatz „fiktiv") |
| **Realität** | mittleres Büro, 14 Mitarbeitende, 3 Geschäftsführer, 20 Projekte in vier Typen (Bildung 8, Verwaltung 4, Gewerbe 5, Wettbewerb 3), Bildmaterial gemischt: 8 Profi-Fotos, 6 Renderings, 6 Baustellen-/Handyfotos, je ein Bild je Projekt (Stock, alle Querformat); öffentliche Auftraggeber und Gewerbe, Wettbewerbe und VgV; Köln, Rheinland, NRW; Wortmarke aus Text, keine Portraits |
| **Erstellt** | 2026-09-07, Rolle Designer |
| **Referenzen** | wolveridge-com-au, big-dk, helenhard-no |

## 1. Konzept in zwei Sätzen

Nach fünf Sekunden: kein Bild, das für sich wirbt, sondern ein Satz in großer Grotesk und darunter ein Raster aus zwanzig gleich großen Kacheln mit schmalen Monospace-Zeilen — die Seite sieht aus wie ein sauber geführtes Projektverzeichnis, und genau das ist sie. Nach dreißig Sekunden: ein Kölner Büro mit vierzehn Leuten plant Schulen, Kitas, Verwaltungs- und Gewerbebauten für Kommunen und Unternehmen, drei Wettbewerbserfolge stehen ehrlich neben Baustellen und Renderings, jedes Projekt ist nach Typ filterbar und als Tabellenzeile mit Ort, Jahr und Maßnahme nachlesbar, und die Telefonnummer steht in der Kopfzeile.

**Der eine Wow-Faktor:** Ein Projektraster in vier Spalten mal fünf Reihen, das zwanzig Projekte mit ungleichem Bildmaterial durch einheitlichen 3:2-Beschnitt, kleine Kachelgröße, Jahressortierung und eine durchnummerierte Monospace-Metazeile je Kachel in eine Ordnung bringt — über dem Raster ein einziger Satz in Inter, 52 px, Gewicht 500, eng gesetzt, als Ersatz für jedes Hero-Bild.

Das ist die Vorgabe des Nutzers (aus wolveridge.com.au abgeleitet). Sie wird nicht mit einem zweiten Effekt ergänzt: kein Hero-Bild, kein Video, kein Slider, keine Einblendanimation, keine Skizzenebene, keine dunkle Sektion. Was das Raster ordnet, ist in Abschnitt 8 belegt; was die Schrift markant macht, in Abschnitt 3.

**Abgrenzung zu Nordkant Architekten und Studio Lindenau** (die beiden fertigen Referenzseiten): Nordkant setzt Fraunces auf warmem Off-White mit Ziegel-Akzent und ein randloses Hero-Foto; Lindenau setzt Cormorant Garamond mit DM Sans, wechselt zwischen Kohle-Dunkel und Hell und arbeitet mit einem Messington-Akzent und großen Einzelbildern. Steinwerk hat **keine Serife, kein Hero-Bild, keine warme Farbe und keine dunkle Sektion**: eine Grotesk (Inter) plus ein Monospace (IBM Plex Mono), ein kühles Grau als Grund, ein Stahlblau als einziger Akzent, und als erster Bildschirm ein Satz plus ein dichtes Raster aus kleinen Kacheln. Von den drei Seiten ist das die sachliche, typografische — die, die ein Vergabereferent als Referenzliste liest.

## 2. Übernommene Features

Jedes Muster mit Feature-ID aus `patterns/_katalog.md`. Drei Referenzen.

| ID | Feature | Wo auf der Seite | Warum es zur Realität passt |
|---|---|---|---|
| wolveridge-com-au-F3 | Projektraster mit fester Kachelbreite | Startseite und Filterseiten, das Raster | Bedingung (630-px-Bild unter 60 KB, `width`/`height` gesetzt) wird erfüllt: Kacheln als 600×400-WebP unter 60 KB, jedes `<img>` mit Maßen. **Abgewandelt:** 4 statt 3 Spalten und Gasse 64 px statt 152 px — 20 Projekte ergeben 5 volle Reihen ohne Restreihe (bei 3 Spalten blieben 2 Kacheln übrig), und die Seite soll dicht sein, nicht luftig. Die kleine Kachel (296 px) ist zugleich das Mittel, das Handy- und Profi-Fotos angleicht: bei dieser Größe trägt der Beschnitt, nicht die Auflösung. |
| wolveridge-com-au-F4 | Bildunterschrift „Name, Jahr" als einzige Textzeile je Kachel, Sortierung nach Jahr absteigend | Raster, unter jeder Kachel | **Abgewandelt** auf zwei Zeilen: Titel in Inter, darunter eine Monospace-Zeile „Nr · Ort · Jahr · Maßnahme". Die Jahressortierung ist hier der eigentliche Ordnungstrick: die Renderings der Projekte 2025/2026 stehen oben, die Baustellenfotos 2019/2020 unten — die Chronologie sortiert das Bildmaterial von selbst nach Art, ohne dass jemand es sortieren muss. |
| wolveridge-com-au-F5 | List-Ansicht als bildlose Tabelle mit Linien | `/projekte/` (Liste) und unterer Teil jeder Filterseite | 20 Projekte liegen über der Schwelle von 15. Bedingungen erfüllt: keine grauen Zeilen nötig, weil kein Projekt eine Detailseite hat und daher alle Zeilen gleich behandelt werden (nicht verlinkt, in `--farbe-text`); mobil bleiben alle Spalten erhalten, als gestapelter Zeilenblock (siehe Abschnitt 5). Für öffentliche Auftraggeber ist die Tabelle die Referenzliste, die sie ohnehin anfordern würden. |
| wolveridge-com-au-F2 | Umschalter in Checkbox-Schreibweise `[x] Raster  [ ] Liste` | Unter dem Statement auf der Startseite, über der Tabelle auf `/projekte/`, auf jeder Filterseite | Nur zusammen mit F5 (erfüllt). Umgesetzt ohne JavaScript-Pflicht: die beiden Einträge sind Links auf `/#projekte` bzw. `/projekte/`, der aktive Eintrag trägt `aria-current="page"`. Mit JavaScript werden sie zu `button`-Elementen mit `aria-pressed`, die in derselben Seite umschalten. |
| wolveridge-com-au-F16 | Renderings und Fotos im selben Raster | Raster und Tabelle | Bedingung übernommen und verschärft: jedes Rendering trägt in der Metazeile den Chip „Rendering", jedes Baustellenfoto den Chip „Baustelle"; in der Tabelle steht die Bildart für alle 20 in einer eigenen Spalte („Foto / Rendering / Baustelle"). Kein Label auf dem Bild selbst (Text auf Bild ohne Kontrastsicherung ist tabu), sondern in der Textzeile darunter. Das ist die Bedingung des Kritikers und ausdrücklicher Wunsch aus `inhalte.md`. |
| wolveridge-com-au-F7 | Zwei Schriften mit fester Rollenteilung: Monospace für Struktur, Grotesk für Text | Gesamte Seite | Bedingung erfüllt: beide Familien frei (OFL) und self-hosted — Inter aus dem Skeleton, IBM Plex Mono lädt der Bauer nach; 12-px-Versalien nur für Chips, alle Labels 13 px, Tabellen 14 px. Die Rollenteilung ist der Grund, warum die Seite ohne Farbe und ohne Bold strukturiert wirkt: alles, was Daten sind (Nr, Ort, Jahr, Typ, Filter, Umschalter, Telefon), steht in Mono; alles, was Sprache ist, in Inter. |
| wolveridge-com-au-F8 | Drei Farbwerte, Grau als Zustandsfarbe | Filter, Umschalter, Navigation | Bedingung erfüllt: der Zustandsgrau `--farbe-text-3` liegt bei 5,36:1 auf dem Grund (gefordert mindestens `rgb(118,118,118)`, das wären 4,5:1 auf Weiß). Grau bedeutet auf der ganzen Seite genau eines: inaktiv (Filter, der nicht gewählt ist; Ansicht, die nicht aktiv ist). |
| wolveridge-com-au-F1 | Fixierte Kopfzeile in Dreiteilung | Kopfzeile aller Seiten | Bedingung (ein Standort → rechts Ort und Telefonnummer) erfüllt: links Wortmarke, mittig die vier Navigationspunkte, rechts in Mono „Köln · 0221 55 44 33-0". Mobil links „Menü", mittig Wortmarke, rechts Telefonnummer als `tel:`-Link. |
| wolveridge-com-au-F10 | Menü: Desktop klappt aus, Mobile geht auf Vollbild | Mobile Navigation | Übernommen mit `aria-expanded` am Auslöser und `nav`-Landmark, wie vom Kritiker verlangt. Desktop braucht kein Ausklappen (vier Punkte passen in die Zeile); mobil Vollbild in `--farbe-grund` mit vier Einträgen à 32 px und Hairlines. |
| big-dk-F1 | Hierarchie über Grauwert und Versalien statt Bold | Gesamte Seite | **Abgewandelt:** zwei Familien statt einer (siehe F7), aber wie bei BIG kein Gewicht über 500 und kein Bold. Hierarchie entsteht aus Größe (52 → 40 → 28 → 17), Grauwert (drei Textstufen) und Mono-Versalien. Genau das lässt ein Büro ohne Profi-Fotos hochwertig wirken. |
| big-dk-F2 | Metadatenblock rechtsbündig neben dem Hauptelement | Startseite rechts vom Statement; Büro-Seite rechts vom Bürotext | Bedingung „ab 3 Projekten mit Eckdaten" erfüllt. Hier nicht je Projekt (keine Detailseite), sondern für das Büro: Label klein in Mono-Versalien, Wert darunter — „Standort Köln", „Team 14", „Projekte 20", „Wettbewerbe 3". Rechtsbündig an der Kante der vierten Rasterspalte. |
| big-dk-F3 | Gemeinsame Kante statt Zentrierung | Alle Seiten | Statement, Filterleiste, Raster, Tabelle und Fußzeile teilen sich die linke Kante bei 2 rem; der Metadatenblock teilt sich die rechte Kante mit der vierten Spalte. Nichts ist zentriert, auch der Umschalter nicht (bei wolveridge mittig — hier links, damit er in der Kante bleibt). |
| big-dk-F4 | Ort in Versalien als Untertitel jeder Projektkachel | Raster, Metazeile | Übernommen als Teil der Mono-Zeile („KÖLN-EHRENFELD"). 20 Ortsnamen aus Köln, Rheinland und NRW auf einer Seite sind zugleich der lokale SEO-Baustein für ein Büro, das kommunale Auftraggeber in genau diesen Städten sucht. |
| helenhard-no-F8 | Filterleiste nach Typologie | Startseite über dem Raster, `/projekte/` über der Tabelle | Bedingung erfüllt: 20 Projekte, vier Typen mit 8 / 4 / 5 / 3 Einträgen (mindestens drei je Typ), inaktive Einträge in `--farbe-text-3` bei 5,36:1. **Abgewandelt:** linksbündig statt zentriert, mit Anzahl in Klammern („Bildung (8)"), und ohne JavaScript-Pflicht — jeder Filter ist ein Link auf eine statische Filterseite (`/projekte/bildung/` …); mit JavaScript filtert er in derselben Seite. Mobil bleibt die Leiste eine Zeile mit horizontalem Scroll, keine drei Umbruchzeilen. |
| helenhard-no-F9 | Metadaten als zweispaltige Tabelle, Label links, Wert rechts, Hairline je Zeile | Büro-Seite („Büro in Zahlen"), Leistungen-Seite (fünf Leistungsfelder als Zeilen) | Variante B aus dem Pattern `metadatenblock-projektseite`. Team ohne Portraits als Zahlen und Rollen (9 Architekt/innen, 3 Bauzeichner/innen, 2 Verwaltung), Kammer, Leistungsphasen — genau die Angaben, die ein VgV-Verfahren abfragt. |
| helenhard-no-F13 | Footer mit einem Block je Standort | Fußzeile aller Seiten | Ein Standort → eine Spalte: Adresse, Telefon, E-Mail als Klartext; daneben Navigation, Rechtstexte und Demo-Hinweis. Bedingung des wolveridge-Kritikers zu F15 (Platz für Impressum und Datenschutz) damit erfüllt. |

Pattern-Belege: `projektkachel-titel-ort` (wolveridge-F4, big-dk-F4), `metadatenblock-projektseite` (big-dk-F2, helenhard-F9). Das Pattern `hero-vollbild-ohne-overlay` wird bewusst **nicht** verwendet (siehe Abschnitt 10).

## 3. Typografie

Zwei Familien, beide OFL, beide self-hosted: **Inter** (variabel 100–900, aus `skeleton/assets/fonts/`) für Statement, Überschriften, Fließtext, Navigation und Kacheltitel; **IBM Plex Mono** (OFL 1.1, IBM; der Bauer lädt `ibm-plex-mono-latin.woff2` und `-latin-ext.woff2` in den Gewichten 400 und 500 nach und trägt sie in `LICENSES.md` der Seite ein) für alles, was Daten sind: Metazeile, Chips, Filter, Umschalter, Tabellen, Telefonnummer, Labels des Metadatenblocks. Feste Rollenteilung: Mono kommt nie über 16 px vor, Inter nie in Versalien. Inter wird nie über Gewicht 500 gesetzt (kein 600, kein 700, kein 900). Alle anderen Familien werden aus dem Fonts-Ordner der Seite gelöscht. `font-feature-settings: "tnum"` für Inter und Mono überall dort, wo Zahlen in Spalten stehen.

| Rolle | Familie (aus skeleton/assets/fonts) | Größe Desktop | Größe Mobil | Gewicht | Laufweite | Zeilenhöhe |
|---|---|---|---|---|---|---|
| Hero (Statement-Satz, zugleich H1 der Startseite) | Inter | 52 px | 32 px | 500 | −0,025 em | 1,08 |
| H1 (Unterseiten) | Inter | 40 px | 30 px | 500 | −0,02 em | 1,1 |
| H2 (Sektionstitel) | Inter | 28 px | 24 px | 500 | −0,01 em | 1,2 |
| H3 (Kacheltitel, Leistungsfeld) | Inter | 17 px | 16 px | 500 | 0 | 1,35 |
| Body | Inter | 17 px | 16 px | 400 | 0 | 1,55 |
| Label/Meta (Kachel-Metazeile, Filter, Umschalter, Metadaten-Label, Telefon in Kopfzeile) | IBM Plex Mono (nachgeladen) | 13 px, Versalien | 13 px, Versalien | 400 (aktiv 500) | 0,06 em | 1,5 |
| Chip („Rendering", „Baustelle") | IBM Plex Mono | 12 px, Versalien | 12 px, Versalien | 500 | 0,06 em | 1 (Box 22 px hoch) |
| Tabelle (Kopf und Zellen) | IBM Plex Mono | 14 px, Kopf in Versalien | 14 px | 400 (Kopf 500) | 0,02 em (Kopf 0,06 em) | 1,5 (Zeile 44 px) |
| Metadaten-Wert (Block rechts) | Inter | 28 px | 22 px | 500 | −0,01 em | 1,1 |
| Navigation | Inter | 15 px | 32 px (Vollbild-Menü) | 400 (aktiv 500) | 0,01 em | 1 |
| Wortmarke „Steinwerk Planungsgesellschaft" | Inter | 17 px | 16 px | 500 | 0,02 em | 1 |

Fließtext-Zeilenbreite höchstens 66 Zeichen (etwa 620 px bei 17 px); das Statement läuft über drei der vier Rasterspalten (bis 1.016 px) und bricht in höchstens drei Zeilen. Keine Kursive auf der ganzen Seite. Versalien nur in Mono. Textlinks im Fließtext: 1 px Unterstreichung in `--farbe-akzent`, 3 px Abstand; Navigationspunkte ohne Unterstreichung, aktiver Punkt in Gewicht 500.

Begründung: Das Verhältnis Statement : Body von 52 : 17 (3,1) liegt zwischen Nordkant (2,3) und Lindenau (3,8) — die Seite hat keinen Hero, also muss der Satz allein den ersten Bildschirm tragen, darf aber das dichte Raster darunter nicht erdrücken. „Markant" entsteht nicht durch Gewicht (Inter 900 ist die XPO-Marke und tabu), sondern durch Größe, enge Laufweite (−0,025 em) und knappe Zeilenhöhe (1,08): ein Satz in Inter 500 bei 52 px mit negativem Tracking liest sich als Setzkasten, nicht als Werbeheadline. Inter statt Source Sans 3, weil Inter die größere x-Höhe und die klareren Ziffern hat und bei 13 px neben Plex Mono nicht zu zierlich wird; Plex Mono statt JetBrains Mono, weil Plex die ruhigere, weniger „Code-Editor"-hafte Zeichnung hat und mit Inter denselben neutralen Duktus teilt.

## 4. Farben

Eine Palette, keine dunkle Sektion. Kühles Grau statt Off-White, Stahlblau statt Ziegel oder Messing.

| Token | Hex | Einsatz | Kontrast gegen Grund |
|---|---|---|---|
| --farbe-grund | `#EDEFF0` | Seitenhintergrund aller Seiten, Kopfzeile, Vollbild-Menü | — |
| --farbe-flaeche | `#E0E4E7` | Bild-Platzhalter vor dem Laden, Tabellenkopf, Kontaktkasten, Fußzeile | 1,11:1 gegen Grund (nur als Fläche, nie als Text) |
| --farbe-text | `#15181B` | Statement, Überschriften, Fließtext, Kacheltitel, Tabellenzellen, Navigation, aktiver Filter, aktiver Umschalter | 15,45:1 auf Grund · 13,94:1 auf Fläche |
| --farbe-text-2 | `#454B51` | Kachel-Metazeile, Chip-Text, Metadaten-Werte in der Tabelle, Demo-Hinweis, Bildnachweis | 7,65:1 auf Grund · 6,90:1 auf Fläche |
| --farbe-text-3 | `#5B6269` | Labels in Mono-Versalien (Metadaten-Label, Tabellenkopf), inaktive Filter, inaktiver Umschalter-Eintrag, Chip-Rahmen | 5,36:1 auf Grund · 4,84:1 auf Fläche (muss ≥ 4,5 — erfüllt auf beiden) |
| --farbe-linie | `#C4CACF` | Hairlines (Kopfzeile unten, Tabellenzeilen, Leistungsliste, Metadatenblock, Fußzeile oben) | 1,43:1 (Dekor, kein Text) |
| --farbe-akzent | `#2B5876` | Stahlblau: Textlinks im Fließtext, Fokusring (2 px, 2 px Abstand), gefüllter Kontakt-Button auf der Kontaktseite, `tel:`- und `mailto:`-Links | 6,60:1 auf Grund · 5,95:1 auf Fläche |
| --farbe-invers | `#EDEFF0` | Text auf dem Akzent-Button (= Grundfarbe) | 6,60:1 auf Akzent |

Rechnung nach WCAG-Formel (relative Luminanz, sRGB-Linearisierung) per Python, alle Werte oben sind gerechnet, nicht geschätzt. Geprüft und verworfen: `--farbe-text-3` als `#626970` läge auf der Fläche bei 4,35:1 und fiele durch, deshalb `#5B6269`; die Textfarbe `#15181B` auf dem Akzent läge bei 2,34:1 und ist deshalb auf dem Button verboten — dort steht ausschließlich `--farbe-invers`. Text steht nie auf einem Foto; Chips liegen unter dem Bild, nicht darauf.

Farbe kommt aus den Bildern, und die sind hier gemischt: Ziegelrot der Schule, Grün-Grau der Logistikhalle, Beton, Holz, Gerüstrot. Gerade weil das Material so uneinheitlich ist, bleibt die Palette selbst farblos — ein kühles, leicht bläuliches Grau (`#EDEFF0`, deutlich kälter als Nordkants `#F5F3EE` und Lindenaus `#F4F1EA`), das rote und grüne Fassaden gleichermaßen trägt, ohne sie zu färben. Der Stahlblau-Akzent erscheint nur auf Links, Fokus und dem einen Button. **Keine dunkle Sektion**, auch die Fußzeile bleibt hell auf `--farbe-flaeche`. Reinweiß kommt nur in Fotos vor, Reinschwarz nirgends.

## 5. Raster und Rhythmus

- Container: `max-width: 1440px`, zentriert, Rand 2 rem (32 px) beidseitig → 1.376 px Nutzbreite bei 1440; unter 720 px Rand 1 rem (16 px). Kein Zentrieren von Inhalten innerhalb des Containers, alles hängt an der linken Kante (big-dk-F3).
- Grundraster: 4 Spalten à 296 px, Gasse 64 px (4 × 296 + 3 × 64 = 1.376). Jede Sektion belegt Spalten dieses Rasters:
  - Kopfzeile: Wortmarke Spalte 1, Navigation Spalten 2–3 (linksbündig ab Spalte 2), Telefon rechtsbündig Spalte 4. Höhe 64 px, `position: sticky; top: 0`, Grund `--farbe-grund`, 1 px `--farbe-linie` unten.
  - Statement (Startseite): Spalten 1–3 (1.016 px), rechts daneben in Spalte 4 der Metadatenblock (big-dk-F2), rechtsbündig. Abstand Kopfzeile → Statement 96 px.
  - Filterleiste und Umschalter: eine Zeile, Filter links (Spalten 1–3), Umschalter rechts (Spalte 4, rechtsbündig). 1 px `--farbe-linie` oben und unten, Zeilenhöhe 48 px. Abstand Statement → Filterzeile 64 px, Filterzeile → erste Kachelreihe 48 px.
  - Projektraster: `display: grid; grid-template-columns: repeat(4, 1fr); column-gap: 64px; row-gap: 56px`. Kachel = Bild 296 × 197 (3:2, `aspect-ratio: 3/2`) + 12 px + Titel (17/1,35) + 4 px + Metazeile (13/1,5) + ggf. Chip in derselben Zeile. Reihenhöhe ≈ 312 px, fünf Reihen ≈ 1.560 px, das Raster endet auf dem Desktop bei rund 2.000 px Seitenhöhe. Erste Bildoberkante bei etwa y = 380 — im Hero-Screenshot (900 px) ist die erste Reihe vollständig sichtbar.
  - Tabelle (`/projekte/`, Filterseiten): volle Nutzbreite 1.376 px, Spalten Nr 48 px / Projekt 1fr / Ort 200 px / Jahr 64 px / Typ 120 px / Maßnahme 200 px / Abbildung 112 px. Zeile 44 px, 1 px `--farbe-linie` unter jeder Zeile, Kopfzeile in `--farbe-text-3` auf `--farbe-flaeche`. Keine Zebra-Streifen, keine Hover-Farbe (Zeilen sind nicht verlinkt).
  - Büro-Seite: Bürotext Spalten 1–2 (656 px, entspricht 66 Zeichen bei 17 px), Metadatenblock Spalte 4 rechtsbündig, Spalte 3 leer; darunter „Büro in Zahlen" als Label-Wert-Tabelle (helenhard-no-F9) über Spalten 1–3.
  - Leistungen-Seite: fünf Leistungsfelder als Zeilen mit Hairline, Label (Inter 17/500) Spalten 1–2, Beschreibung (Body) Spalten 3–4; „Wettbewerbe und VgV-Verfahren" verlinkt auf `/projekte/wettbewerbe/`.
  - Fußzeile: `--farbe-flaeche`, 1 px `--farbe-linie` oben, vier Spalten: Standortblock (helenhard-no-F13) Spalte 1, Navigation Spalte 2, Rechtstexte Spalte 3, Demo-Hinweis und Bildnachweis-Link Spalte 4. Innenabstand 48 px oben und unten.
- Sektionsabstand: 96 px (6 rem) zwischen Sektionen auf Unterseiten; auf der Startseite gibt es nur Statement → Filter → Raster → Fußzeile, dort gelten die Abstände oben. Abstand innerhalb einer Sektion: 24 px zwischen Absätzen, 12 px zwischen Titel und Metazeile.
- Breakpoints: ab 1100 px vier Spalten; 720–1099 px zwei Spalten (Gasse 40 px, Kachel bis 480 px breit — die Kacheln werden größer, das Raster hat dann zehn Reihen); unter 720 px eine Spalte, Kachel volle Nutzbreite (358 px bei 390), Reihenabstand 40 px. Statement mobil über volle Breite, Metadatenblock darunter linksbündig als Zeile „Köln · 14 Mitarbeitende · 20 Projekte · 3 Wettbewerbe" in Mono 13.
- Tabelle mobil (unter 720 px): keine Spalten entfernen (Bedingung wolveridge-F5). Jede Zeile wird ein Block: Zeile 1 „Nr Projekt" (Inter 16/500), Zeile 2 in Mono 13 „Ort · Jahr · Typ · Maßnahme · Abbildung", Hairline darunter. Alle sieben Angaben bleiben lesbar, nichts wird mit „…" abgeschnitten.
- Filterleiste mobil: eine Zeile, `overflow-x: auto`, `scroll-snap`, ohne sichtbare Scrollbar, 24 px Abstand zwischen Einträgen; Umschalter darunter in eigener Zeile linksbündig.
- Ausrichtung: linksbündig, gemeinsame Kante; einzige rechtsbündige Elemente sind Telefon in der Kopfzeile, Metadatenblock und Umschalter — alle drei an der rechten Kante von Spalte 4.

## 6. Seiteninventar

Alle Projektdaten liegen in einer Datei (`_doku/projekte.json` oder als Frontmatter-Liste im Generator): Nr, Titel, Ort, Jahr, Typ, Maßnahme, Bildart, Wettbewerbsergebnis, Bilddatei. Raster, Tabelle, Filterseiten und Chips werden aus derselben Liste erzeugt — nichts wird zweimal gepflegt (wolveridge-Kritiker: „ein Büro pflegt eine Projektliste und bekommt Bildunterschrift, Tabelle und Award-Zeile daraus").

| Seite | URL | Zweck | Besonderheit |
|---|---|---|---|
| Startseite | / | Statement (H1), Metadatenblock, Filter + Umschalter, Raster aller 20 Projekte, Fußzeile | Kein Hero-Bild, kein Einstiegstext außer dem Statement. `#projekte` als Anker auf die Filterzeile. Der Umschalter zeigt `[x] Raster [ ] Liste` |
| Projekte (Liste) | /projekte/ | H1 „Projekte", Filter + Umschalter, Tabelle aller 20 Projekte | Bildlose Tabelle (wolveridge-F5), Umschalter zeigt `[ ] Raster [x] Liste`; „Raster" verlinkt auf `/#projekte` |
| Filterseiten | /projekte/bildung/, /projekte/verwaltung/, /projekte/gewerbe/, /projekte/wettbewerbe/ | H1 je Typ („Bildungsbauten", „Verwaltungsbauten", „Gewerbebauten", „Wettbewerbe"), ein Satz Einleitung, Filterleiste mit aktivem Eintrag, Raster der n Projekte, darunter die Tabelle derselben n Projekte | Das ist der JavaScript-freie Filter: vier statische Seiten aus derselben Datenquelle. Mit JavaScript ersetzt der Filter auf `/` und `/projekte/` den Seitenwechsel durch Ein-/Ausblenden und schreibt die URL per `history.replaceState` auf die Filterseite. `/projekte/wettbewerbe/` nennt zusätzlich je Projekt das Ergebnis (1. Preis, 3. Preis, Anerkennung) in der Metazeile — Wettbewerbe sind damit an drei Stellen sichtbar: Filter, Maßnahme-Spalte, eigene Seite |
| Projekt-Detail | /projekte/{slug}/ | — | **nein.** Ein Bild je Projekt reicht nicht für eine Detailseite (`inhalte.md` D). Eckdaten stehen in der Tabelle |
| Büro | /buero/ | Selbstbeschreibung, Geschäftsführung (drei Namen als Text), Team als Zahlen und Rollen, „Büro in Zahlen", Kammer | Metadatenblock rechts (big-dk-F2), Label-Wert-Tabelle (helenhard-F9); ein Bild: `kita-waldstrasse-01.webp` mit Chip „Baustelle" als 3:2 über Spalten 1–2 — die Baustelle als ehrliches Bürofoto statt Portraits |
| Leistungen | /leistungen/ | Fünf Leistungsfelder als Hairline-Zeilen mit je zwei bis drei Sätzen; Hinweis auf Generalplanung mit Fachplanern | Kein Bild. „Wettbewerbe und VgV-Verfahren" verlinkt auf `/projekte/wettbewerbe/`, „Bildungsbauten" auf `/projekte/bildung/` usw. |
| Kontakt | /kontakt/ | Adresse, Telefon, E-Mail als Klartext-Links, Anfahrt als Textlink auf einen Kartendienst (keine eingebettete Karte), ein Absatz „So erreichen Sie uns" | Einziger gefüllter Button der Seite: `mailto:` als Akzent-Button; kein Formular (kein Backend auf der Referenzseite) |
| Impressum, Datenschutz | /impressum/, /datenschutz/ | Skeleton | Impressum-Absatz „fiktiv", `noindex, follow` auf allen Seiten, Demo-Hinweis in der Fußzeile |
| Bildnachweis | /bildnachweis/ | Tabelle aus `BILDER.md` (Datei, Fotograf, Quelle) | Gleicher Tabellenstil wie die Projektliste; von der Fußzeile verlinkt |

## 7. Navigation

- Punkte (vier): **Projekte** (→ `/projekte/`), **Leistungen**, **Büro**, **Kontakt** — in dieser Reihenfolge. Kein Kontakt-Button in der Kopfzeile; stattdessen steht rechts die Telefonnummer als `tel:`-Link in Mono („KÖLN · 0221 55 44 33-0"), das ist für Kommunen und Schulträger der erwartete Kontaktweg. Wortmarke links verlinkt auf `/`. Aktiver Punkt in Gewicht 500 und `aria-current="page"`; auf Filterseiten ist „Projekte" aktiv.
- Verhalten beim Scrollen: `position: sticky; top: 0`, Grund `--farbe-grund` (deckend, keine Transparenz, kein Blur), 1 px `--farbe-linie` unten. Kein Ausblenden beim Scrollen: das Raster ist 1.560 px hoch und die Filterzeile ist nicht sticky, also muss die Kopfzeile bleiben, damit „Projekte" und die Telefonnummer auf der ganzen Höhe erreichbar sind. Wer zurück zum Filter will, scrollt; der Anker `#projekte` sitzt auf der Filterzeile.
- Skip-Link „Zum Inhalt" als erstes fokussierbares Element, sichtbar bei Fokus.
- Mobil (unter 720 px): Kopfzeile 56 px, links Text-Button „Menü" (kein Icon; `button` mit `aria-expanded`, `aria-controls`), mittig Wortmarke, rechts Telefonnummer als „0221 55 44 33-0" in Mono 13. Geöffnet: Vollbild in `--farbe-grund` (wolveridge-F10), Button wird zu „Schließen", vier Einträge à 32 px Inter 400, linksbündig bei 16 px Rand, 1 px `--farbe-linie` zwischen den Einträgen, darunter Telefon und E-Mail in Mono 13. `nav`-Landmark, `Esc` schließt, Fokus bleibt im Menü. Ohne JavaScript: Menü ist ein Anker-Link auf die Navigation in der Fußzeile.
- Zweite Ebene (nur auf `/`, `/projekte/` und Filterseiten): die Filterzeile mit Umschalter. Filtereinträge: „Alle (20) · Bildung (8) · Verwaltung (4) · Gewerbe (5) · Wettbewerb (3)", Mono 13, Versalien, aktiv `--farbe-text` Gewicht 500 mit `aria-current="page"`, inaktiv `--farbe-text-3`. Umschalter rechts: `[x] RASTER   [ ] LISTE` in Mono 13, aktiv `--farbe-text`, inaktiv `--farbe-text-3` — ohne JavaScript zwei Links, mit JavaScript zwei `button` mit `aria-pressed` (Bedingung wolveridge-F2).

## 8. Bildkonzept

- Formate: ausschließlich 3:2 Querformat. Raster 296 × 197 px (Desktop), 480 × 320 (Tablet), 358 × 239 (Mobil); Büro-Seite ein Bild 656 × 437. Kein Hero-Bild, kein Vollbreiten-Bild, kein Bildpaar.
- Zuschnitt: `aspect-ratio: 3/2; object-fit: cover`, `object-position` je Bild in der Projektdatei pflegbar (Standard `center`; `kita-sonnenhang-01` und `quartiersschule-01` als Modellfotos auf `center 40%`, damit die Gebäude und nicht der Vordergrund im Ausschnitt liegen). Bild-Platzhalter `--farbe-flaeche`, damit vor dem Laden kein Weiß aufblitzt.
- Auslieferung: WebP 600 × 400 (1×) und 900 × 600 (1,5×/2× für Mobil-Retina) über `srcset`, jeweils unter 60 KB (Bedingung wolveridge-F3); `width="600" height="400"` an jedem `<img>`; erste Reihe (vier Bilder) `loading="eager"`, ab der zweiten Reihe `loading="lazy"`; das erste Bild `fetchpriority="high"`. Kein Bild über 1.200 px Breite auf der Seite. Die Quelldateien liegen bei 1.920 px und werden vom Bauer verkleinert.
- Anzahl je Seite: Startseite 20, `/projekte/` 0, Filterseiten 8 / 4 / 5 / 3, Büro 1, Leistungen 0, Kontakt 0. Gesamttransfer der Startseite unter 1,2 MB Bilder (20 × < 60 KB).
- `alt`-Text je Bild: „{Titel}, {Ort} — {Foto | Rendering | Baustellenfoto}", z. B. „Kita Sonnenhang, Erftstadt — Rendering". Die Bildart steht also auch im `alt`, nicht nur im Chip.
- **Wie das Raster das ungleiche Material ordnet** (das ist der Wow-Faktor, hier belegt):
  1. Ein Beschnitt für alle: 3:2, `cover`. Modellfotos, Fassadenfotos und Gerüstfotos bekommen dieselbe Kante.
  2. Kleine Kachel: bei 296 px Breite trägt ein 6000-px-Handyfoto genauso wie ein Profi-Foto; Unschärfe und Rauschen verschwinden, was bleibt, ist Motiv und Farbe. Das ist der Grund, warum wolveridge mit 315-px-Kacheln 55 Projekte ohne Qualitätsbruch zeigt.
  3. Jahressortierung: absteigend nach Jahr, innerhalb eines Jahres Foto → Rendering → Baustelle. Mit den vorliegenden Daten ergibt das eine Reihenfolge, in der die Renderings der Planungen 2025/2026 oben stehen und die vier Baustellenfotos von 2019/2020 die letzte Reihe bilden — die Chronologie sortiert das Bildmaterial von selbst nach Art. Reihe 1: Schulzentrum Kerpen (Rendering, Wettbewerb 1. Preis), Verwaltungsgebäude Stadtwerke Bonn (Rendering), Sporthalle Wesseling (Rendering), Grundschule Am Ring (Foto). Reihe 2: Kita Rheinufer (Foto), Produktionshalle Frechen (Rendering), Gesamtschule Nord (Foto), Rathaus-Anbau Pulheim (Foto). Reihe 3: Logistikhalle Ost (Foto), Quartiersschule Düsseldorf (Rendering, 3. Preis), Bürogebäude Kalk (Foto), Berufskolleg Süd (Foto). Reihe 4: Feuerwache Bergisch Gladbach (Foto), Verwaltungszentrum Aachen (Rendering, Anerkennung), Mensa Gymnasium Brühl (Rendering), Kita Sonnenhang (Rendering). Reihe 5: Kita Waldstraße, Grundschule Troisdorf, Gewerbehof Mülheim, Bürgerhaus Rösrath (alle Baustelle). Die Nummern 01–20 folgen dieser Reihenfolge, nicht der Reihenfolge in `inhalte.md`.
  4. Kennzeichnung als Teil der Metazeile: „01 · KERPEN · 2026 · WETTBEWERB, 1. PREIS" plus Chip „RENDERING"; Fotos tragen keinen Chip — Abwesenheit des Chips heißt Foto, in der Tabelle steht es für alle 20 ausdrücklich. Der Chip liegt nie auf dem Bild.
  5. Gleiche Kachelhöhe je Reihe durch Grid, unabhängig davon, ob ein Chip die Metazeile verlängert (Chip in derselben Zeile, Umbruch der Metazeile erlaubt, Reihenhöhe über `align-items: start` und feste Bildhöhe).
- Stockfoto-Suchbegriffe (nur Referenz, alle Querformat, aus `BILDER.md`): modern school building facade (grundschule-ring, Foto) · kindergarten building exterior modern (kita-rheinufer, Foto) · empty school hallway modern architecture (gesamtschule-nord, Foto) · modern public building facade concrete glass (rathaus-anbau, Foto) · industrial warehouse architecture facade (logistikhalle, Foto) · modern office building brick facade (buero-kalk, Foto) · renovated school facade (berufskolleg, Foto) · fire station building exterior (feuerwache, Foto) · school canteen rendering (mensa, Rendering) · architectural model building rendering (kita-sonnenhang, Rendering) · modern office building facade glass wood (stadtwerke, Rendering) · sports hall building exterior modern (sporthalle, Rendering) · factory building architectural rendering (produktionshalle, Rendering) · school campus rendering aerial (schulzentrum, Rendering) · construction site wooden building (kita-waldstrasse, Baustelle) · construction site building shell concrete (grundschule-troisdorf, Baustelle) · renovation construction site brick (gewerbehof, Baustelle) · building renovation scaffolding (buergerhaus, Baustelle) · architectural model school building (quartiersschule, Rendering) · modern administration building exterior (verwaltungszentrum, Rendering). Hinweis für den Bauer: `grundschule-ring-01` und `berufskolleg-01` sind laut `BILDER.md` dieselbe Quelldatei — bitte im Bildnachweis so ausweisen und, falls möglich, für eines der beiden ein anderes Motiv ziehen (offene Frage 4).
- Hero-Bild: **keines.** Der erste Bildschirm ist Statement plus erste Rasterreihe. Ein Hero-Bild müsste eines der 20 Projekte über die anderen stellen, und bei gemischtem Material (die aktuellsten sind Renderings) wäre das entweder ein Rendering als Aushängeschild oder ein älteres Foto — beides widerspricht der Ehrlichkeit, die die Zielgruppe verlangt.

## 9. Motion

- Keine Animation auf der Seite. Kein Einblenden der Kacheln, kein Zoom, kein Scroll-Effekt, keine wachsende Linie. Die Seite lädt fertig und steht.
- Einzige Übergänge: Unterstreichung der Textlinks und Farbwechsel der Filter- und Umschalter-Einträge in 120 ms `ease-out`; der Fokusring erscheint ohne Übergang. Mit JavaScript wechselt der Filter Kacheln sofort (kein Fade), damit das Raster nicht springt; die Zeilenzahl ändert sich, die Kopfzeile bleibt.
- Mobile-Menü: öffnet und schließt ohne Übergang.
- Alles unter `prefers-reduced-motion: reduce` abgeschaltet — betrifft hier nur die 120-ms-Übergänge, `scroll-behavior` bleibt `auto`.
- Kein Preloader, kein Autoplay-Video, kein Laufband, kein Hover als einziger Informationsträger (jede Kachel zeigt Titel und Metazeile dauerhaft; Hover verändert nichts, wie bei wolveridge gemessen).

## 10. Bewusst nicht übernommen

| Muster | Grund |
|---|---|
| wolveridge-com-au-F9 Projektdetail (Textspalte links, Bildspalte rechts) | Braucht 6+ Fotos je Projekt; hier gibt es eines. Keine Detailseiten, siehe Abschnitt 6 |
| wolveridge-com-au-F13 Auszeichnungs- und Presse-Tabelle | Übertragbar erst ab 5 Auszeichnungen; das Büro hat drei Wettbewerbsergebnisse. Die stehen stattdessen in der Maßnahme-Spalte der Projektliste, im Filter „Wettbewerb (3)" und auf `/projekte/wettbewerbe/` — sichtbar, aber nicht als eigene Tabelle, die mit drei Zeilen dünn wirkt |
| wolveridge-com-au-F14 Team-Porträts 2+1 | Keine Portraits vorhanden; Team als Zahlen und Rollen (big-dk-F2, helenhard-F9) |
| wolveridge-com-au-F11 Intro-Statement in Mono-Versalien, zentriert | Das Statement ist hier der Wow-Faktor und steht deshalb in der Grotesk, groß, linksbündig — Mono-Versalien bei 16 px würden den Satz zur Beschriftung machen |
| wolveridge-com-au-F6 „Region (Ort)" | Urteil `nicht` — australisches Acknowledgement, in Köln eine leere Hülle |
| wolveridge-com-au-F12 Laufband | Urteil `nicht` — WCAG 2.2.2, und es gibt keine Studiofotos |
| wolveridge-com-au-F15 Minimal-Footer | Urteil `nicht` — kein Platz für Impressum und Datenschutz |
| wolveridge Kopfzeile, die beim Scrollen verschwindet | Die Startseite ist 2.000 px hoch mit einem Raster ohne Zwischenüberschriften; „Projekte" und Telefon müssen erreichbar bleiben. Sticky statt ausblendend |
| wolveridge 12-px-Versalien für Tabellen und Unterschriften | Bedingung F7: Labels 13 px, Tabellen 14 px. 12 px nur im Chip |
| big-dk-F6 Startseite als endlose Projektliste ohne Einstieg | Bedingt ab 30 Projekten gleicher Bildqualität; hier 20 in drei Qualitäten. Deshalb das Statement als H1 und Einstieg vor dem Raster, und ein endliches Raster (5 Reihen), keine Liste ohne Ende |
| big-dk-F7 Projektsignets | Urteil `nicht` — Eigenschöpfung, je Projekt zu zeichnen |
| big-dk-F8 Preloader | Urteil `nicht` |
| big-dk-F5 Navigation nach Disziplin | Die Leistungsfelder (Bildung, Verwaltung, Gewerbe) sind trennbar, aber sie sind bereits der Filter — sie zusätzlich in die Hauptnavigation zu heben, hieße zwei Navigationen mit denselben Wörtern. Hauptnavigation bleibt Projekte / Leistungen / Büro / Kontakt |
| helenhard-no-F2 Hero als Video oder randloses Bild, Pattern `hero-vollbild-ohne-overlay` | Vorgabe des Nutzers: kein Hero-Bild. Begründung in Abschnitt 8 |
| helenhard-no-F3 Skizzenebene | Urteil `nicht`, und Eigenschöpfung |
| helenhard-no-F4 leichte Serife | Serifen sind an Nordkant (Fraunces) und Lindenau (Cormorant) vergeben; diese Seite ist die Grotesk-Seite |
| helenhard-no-F5 Off-White, Beige-Buttons, Graubraun-Footer | Warme Palette ist an Nordkant und Lindenau vergeben; hier kühles Grau, heller Footer |
| helenhard-no-F6 Newsliste | Keine Redaktion auf einer Referenzseite, und ein Büro dieser Größe pflegt selten vierteljährlich Einträge |
| helenhard-no-F7 Kachel mit zentriertem Titel über dem Bild und kursivem Satz | Zentrierung widerspricht der gemeinsamen Kante; Kursiv gibt es auf dieser Seite nicht; ein Satz je Projekt liegt nicht vor |
| helenhard-no-F10 Bildrhythmus Vollbreite → Text → Foto + Skizze | Braucht Detailseiten und Pläne; beides gibt es nicht |
| helenhard-no-F11 Lazy Loading ohne Maße | Urteil `nicht`; hier jedes Bild mit `width`/`height` |
| helenhard-no-F12 mobile Kopfzeile aus drei Textelementen | Das Prinzip (Text statt Icon) ist übernommen, aber ohne Monogramm — „Steinwerk" passt als volle Wortmarke in die Mitte; als Feature deshalb nicht gezählt |
| Carousel/Slider, Hero-Video, Parallax, Google Fonts, Text auf Bild, Hover als Informationsträger | Anti-Muster aus dem Rollen-Prompt und Ausschlüsse aus `inhalte.md` C |

## 11. Offene Fragen an den Nutzer

1. **IBM Plex Mono nachladen:** Das Skeleton enthält kein Monospace. Die Vorgabe erlaubt es optional; ich habe damit gerechnet, dass der Bauer Plex Mono (OFL) in 400 und 500 als `latin`/`latin-ext`-woff2 nachlädt und `LICENSES.md` ergänzt. Alternative ohne Nachladen: Inter für die Metazeile mit `"tnum"` und 0,08 em Laufweite — die Rollenteilung (wolveridge-F7) ginge dann verloren. Bitte bestätigen.
2. **Sortierung:** Jahr absteigend mit Foto → Rendering → Baustelle innerhalb eines Jahres (Abschnitt 8). Alternativ nach Typ gruppiert (Bildung, Verwaltung, Gewerbe, Wettbewerb) — dann stünden die Baustellenfotos verstreut und das Raster würde weniger von selbst ordnen. Ich empfehle Jahr.
3. **Statement-Wortlaut:** Vorschlag aus der Selbstbeschreibung: „Schulen, Kitas, Verwaltungs- und Gewerbebauten im Rheinland — von der Machbarkeitsstudie bis zur Übergabe." (14 Wörter, drei Zeilen bei 52 px auf 1.016 px). Der zweite Satz („Viele unserer Projekte entstehen aus Wettbewerben …") kommt als Body-Absatz auf die Büro-Seite, nicht auf die Startseite. Passt der Satz, oder soll der Wettbewerbs-Hinweis ins Statement?
4. **Doppelte Quelldatei:** `grundschule-ring-01.webp` und `berufskolleg-01.webp` stammen laut `BILDER.md` von derselben Pexels-Datei. Im Raster stünden zwei identische Kacheln in Reihe 1 und Reihe 3. Soll für eines der beiden ein neues Motiv gezogen werden (Empfehlung: Berufskolleg, Suchbegriff „renovated school building facade brick")?
5. **Telefonnummer in der Kopfzeile:** Für ein Büro mit öffentlichen Auftraggebern habe ich die Nummer rechts in die Kopfzeile gesetzt statt eines Kontakt-Buttons. Einverstanden, oder lieber nur „Kontakt" als Navigationspunkt?
6. **Filter ohne JavaScript als vier statische Seiten:** Das ist die robusteste Lösung (funktioniert, ist verlinkbar, trägt `aria-current`), kostet aber vier zusätzliche Seiten aus derselben Datenquelle. Alternative wäre reines CSS über `:target`, das ohne JS funktioniert, aber keinen aktiven Zustand auszeichnen kann. Ich habe die statischen Seiten gewählt; Einspruch?

---

**Kombinierte Referenzen:** wolveridge.com.au (Raster + Liste + Umschalter, Mono/Grotesk-Rollenteilung, drei Farbwerte, Kopfzeile mit Standort, Kennzeichnung der Renderings als Bedingung), big.dk (gemeinsame Kante statt Zentrierung, Metadatenblock rechtsbündig, Hierarchie ohne Bold, Ort in Versalien unter der Kachel), helenhard.no (Filterleiste nach Typologie, Label-Wert-Tabelle mit Hairlines, Standort-Footer). Warum genau diese: wolveridge zeigt, wie 55 ungleiche Projekte in einem kleinen 3:2-Raster mit Jahressortierung und einer bildlosen Tabelle als Verzeichnis funktionieren — das ist die Aufgabe hier bei 20 Projekten in drei Bildqualitäten; big.dk liefert das Mittel, ohne Akzentfarbe und ohne Bold Hierarchie zu bauen, was bei gemischtem Material die Palette farblos halten muss; helenhard liefert den Filter ab zwölf Projekten mit drei Typologien (hier vier mit 8/4/5/3) und die Metadaten-Tabelle, die ein Vergabereferent als Referenzliste liest. Keine der drei Seiten wird nachgebaut: wolveridge ist 3-spaltig und zentriert ohne Filter, big.dk einspaltig ohne Einstieg, helenhard eine Serife mit Video-Hero — diese Seite ist 4-spaltig, linksbündig, mit Filter, Grotesk plus Mono, ohne Hero.
