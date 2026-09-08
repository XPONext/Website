# Design-Brief: Nordkant Architekten

| | |
|---|---|
| **Projektart** | Referenz (fiktives Büro, `noindex`, Demo-Hinweis in der Fußzeile) |
| **Realität** | kleines Büro (2 Inhaber + 2 Mitarbeitende), 6 Projekte, je 3 Profi-Fotos (Stock, alle Querformat), private Bauherren (Neubau EFH, Umbau, Anbau), Münster und Münsterland, Wortmarke aus Text, keine Portraits |
| **Erstellt** | 2026-09-07, Rolle Designer |
| **Referenzen** | helenhard-no, pietboon-com, big-dk |

## 1. Konzept in zwei Sätzen

Nach fünf Sekunden: ein einziges Haus im Wald, das den ganzen Bildschirm füllt, ohne dass irgendjemand etwas behauptet — die Seite ist so ruhig wie das Haus. Nach dreißig Sekunden: ein kleines Büro in Münster baut Wohnhäuser für Menschen, die lange darin leben wollen, sechs davon kann man sich ansehen, und der Weg zum Erstgespräch ist eine Telefonnummer und eine Mailadresse, keine Formularstrecke.

**Der eine Wow-Faktor:** Das Hero-Foto trägt die gesamte erste Bildschirmhöhe, randlos und ohne Text darauf; alles andere auf der Seite — eine Serife in leichtem Schnitt, warmes Off-White, kleine 3:2-Kacheln — ist bewusst leiser als dieser erste Moment.

Das ist die Vorgabe des Nutzers (aus helenhard.no abgeleitet) und wird nicht mit einem zweiten Effekt ergänzt: keine Skizzenebene, kein Video, kein Slider, keine Einblendanimation.

## 2. Übernommene Features

Jedes Muster mit Feature-ID aus `patterns/_katalog.md`. Drei Referenzen kombiniert.

| ID | Feature | Wo auf der Seite | Warum es zur Realität passt |
|---|---|---|---|
| helenhard-no-F2 | Hero textfrei über den ersten Bildschirm (Pattern `hero-vollbild-ohne-overlay`) | Startseite, erster Bildschirm | Bedingung „als stehendes Foto, kein Video" erfüllt: `<img>` unter 250 KB, `fetchpriority="high"`. Das Büro hat ein Foto, das das tragen kann (`haus-im-wald-01`, siehe 8.). Abweichung von helenhard: randlos statt mit 80-px-Rand, und exakt die erste Bildschirmhöhe statt „über den Fold hinaus" — das ist die Nutzer-Vorgabe |
| big-dk-F4 | Ort in Versalien als Unterzeile | Bildzeile direkt unter dem Hero („Haus im Wald · Nottuln · 2021"), Projektkopf auf der Detailseite | Die eine Zeile unter dem Hero ist der Hinweis, dass es weitergeht (das Pattern warnt vor 100 vh ohne Fortsetzung); Ortsnamen sind zugleich der lokale SEO-Baustein für „Architekt Münsterland" |
| helenhard-no-F1 | Geteilte Navigation mit zentrierter Wortmarke | Kopfzeile aller Seiten | „Nordkant Architekten" sind zwei Wörter, breit genug für die Mitte (Bedingung erfüllt). Vier Punkte, zwei links, zwei rechts, kein Sticky, kein CTA-Button in der Leiste |
| helenhard-no-F4 | Eine Serife in Leichtgewicht, Kursiv als einzige Auszeichnung | gesamter Auftritt | Bedingung erfüllt: Fraunces aus `skeleton/assets/fonts`, self-hosted, mit eigenem Kursiv-Schnitt (`fraunces-latin-italic.woff2`). Kein Fremd-Request, keine zweite Familie. „Ruhige, edle Schrift" ist Teil der Vorgabe |
| big-dk-F1 | Hierarchie über Größe, Grauwert und Versalien statt Bold | gesamter Auftritt | Kein Gewicht über 400 auf der ganzen Seite; Labels und Ortszeilen in 13-px-Versalien in Grau. Abweichung von BIG: zwei Gewichte (300 für Überschriften, 400 für Text) statt einem, weil Fraunces 300 im Fließtext für Bauherren 50+ zu dünn wäre |
| helenhard-no-F5 | Off-White-Grund, beiger Button, kein Reinweiß, kein Reinschwarz | Farbsystem | Bedingung erfüllt: Sekundärtext ist `#6B665E` (5,14:1 auf dem Grund), nicht halbtransparent. Abweichung: kein graubrauner Footer — der Footer liegt auf `--farbe-flaeche`, die Seite hat keine dunkle Sektion (Abgrenzung zur Innenarchitektur-Referenz, siehe unten) |
| pietboon-com-F2 | Zwei Graustufen für Flächen, ein gedeckter Akzent nur auf Schaltflächen | Kopfzeile, Kachelfuß der Metadaten, Kontaktkasten, Footer, Button | „Wirkt gerade bei wenig Bildern" — sechs Projekte, das Flächenspiel trägt den Rhythmus zwischen den Fotos. Akzent ist ein Ziegelton aus den Fotos (`#8B5A3C`), nicht Blaugrau |
| pietboon-com-F15 | Zentrierter Intro-Block mit Chevron-Linkliste | Startseite, direkt unter der Hero-Bildzeile | Genau vier Leistungsfelder (Neubau › Umbau › Anbau › Bauberatung): die Linkliste ersetzt einen Leistungs-Teaser und bringt die Leistungsseiten ohne Menüpunkt-Wildwuchs unter |
| helenhard-no-F7 | Projektkachel: Titel zentriert über dem Bild, kursiver Satz darunter (Pattern `projektkachel-titel-ort`) | Startseite (4 Kacheln), `/projekte/` (6 Kacheln) | Bedingung „ab 4 Projekten, Fotos im gleichen Format 3:2" erfüllt — alle 18 Bilder Querformat. Kein Hover-Overlay, funktioniert auf Mobile ohne Anpassung |
| pietboon-com-F6 | Versetzter Farbkasten, Bild überlappt den Kasten (Pattern `statement-bild-text`) | Startseite Büro-Abschnitt, `/buero/` | Das Büro hat keine Portraits — der Kasten macht aus einem Detailfoto (`aufstockung-01`, Oberlicht) und einem Absatz Selbstbeschreibung eine Komposition, ohne dass ein Gesicht fehlt |
| pietboon-com-F11 | Projektkopf: Hero 16:9 eingerückt, Titel und Text erst darunter | Projekt-Detailseite | Ein gutes Querformat und 60–100 Wörter je Projekt sind genau das, was vorliegt. Das eingerückte Bild im Container (statt randlos) hält den randlosen Hero der Startseite als einzigen randlosen Moment |
| helenhard-no-F9 | Metadatenblock, Label links, Wert rechts, Hairline je Zeile (Pattern `metadatenblock-projektseite`, Variante B) | Projekt-Detailseite, neben dem Projekttext | Fünf Eckdaten je Projekt (Ort, Fertigstellung, Leistung, Leistungsphasen, Wohnfläche) — genug, damit der Block nicht wie ein leeres Formular wirkt. Private Bauherren lesen daran ab, ob das Büro „bis Bauleitung" macht |
| pietboon-com-F7 | Zwei Fotos in ungleicher Breite und versetztem Beginn | Projekt-Detailseite (Bild 2 + 3), `/leistungen/` | Es gibt drei Fotos je Projekt und keine Pläne — helenhard-F10 (Foto + Plan) fällt damit weg, das versetzte Paar gibt zwei Querformaten Spannung, ohne eine Profi-Serie zu brauchen |
| helenhard-no-F13 | Footer mit Standortblock: Ortsname kursiv, darunter Adresse und Telefon | Footer aller Seiten | Ein Standort → eine Spalte (Bedingung). Telefon und Mail als Klartext sind für Bauherren der eigentliche Kontaktweg |
| helenhard-no-F12 | Mobile-Kopfzeile aus Textelementen statt Icon | Mobile-Navigation | Bedingung erfüllt: Auslöser ist ein `button` mit `aria-expanded` und `aria-controls`; Wortmarke bleibt als Text „Nordkant Architekten" (kein Monogramm nötig, passt bei 16 px in 390 px) |

**Abgrenzung zu den beiden anderen Referenzseiten** (`eigene/README.md` ist noch leer, die Abgrenzung
gilt gegenüber den geplanten Seiten): Das mittlere Büro für öffentliche Auftraggeber bekommt Grotesk,
dichtes Raster, kein Hero-Bild — hier das Gegenteil: Serife, luftiges Zweierraster, ein Hero, der den
Bildschirm füllt. Das Innenarchitektur-Studio bekommt ebenfalls eine edle Serife, aber dunkle und helle
Sektionen im Wechsel und große Bilder überall. Diese Seite hat **keine dunkle Sektion** (durchgehend
Off-White mit einer zweiten hellen Stufe), das große Bild gibt es **nur einmal** (Hero), danach werden
die Bilder klein und gleichförmig (3:2-Kacheln, 611 px) — die Spannung liegt im Kontrast zwischen dem
einen großen und den vielen kleinen Bildern, nicht zwischen Hell und Dunkel. Die Schrift ist Fraunces
in 300/400 mit optischer Größe; die Innenarchitektur-Seite sollte deshalb Cormorant Garamond oder
Instrument Serif nehmen, nicht Fraunces (siehe 11.).

## 3. Typografie

Eine Familie: **Fraunces** (variabel 300–700, optische Größe 9–144, mit Kursiv), self-hosted aus
`skeleton/assets/fonts/`. `font-optical-sizing: auto`, Achsen `SOFT` und `WONK` auf Standard (0).
Kein Gewicht über 400. Alle anderen Familien werden aus dem Fonts-Ordner der Seite gelöscht.

| Rolle | Familie (aus skeleton/assets/fonts) | Größe Desktop | Größe Mobil | Gewicht | Laufweite | Zeilenhöhe |
|---|---|---|---|---|---|---|
| Hero | — kein Text auf dem Bild. Bildzeile darunter: Fraunces | 13 px, Versalien | 12 px, Versalien | 400 | 0,10 em | 1,6 (Zeile 56 px hoch, mittig) |
| H1 | Fraunces | 44 px | 32 px | 300 | −0,01 em | 1,15 |
| H2 | Fraunces | 32 px | 26 px | 300 | −0,005 em | 1,2 |
| H3 | Fraunces (Kacheltitel, Zwischentitel) | 24 px | 21 px | 400 | 0 | 1,3 |
| Body | Fraunces | 19 px | 17 px | 400 | 0 | 1,55 |
| Untertitel kursiv (Kachel, Projektkopf) | Fraunces Italic | 19 px | 17 px | 400 | 0 | 1,5 |
| Label/Meta | Fraunces | 13 px, Versalien | 12 px, Versalien | 400 | 0,10 em | 1,6 |
| Navigation | Fraunces | 17 px | 16 px | 400 | 0,01 em | 1 |
| Wortmarke | Fraunces | 26 px | 20 px | 400 | −0,01 em | 1 |

Fließtext-Zeilenbreite höchstens 62 Zeichen (etwa 640 px bei 19 px); der zentrierte Intro-Block
darf 68 Zeichen breit werden. Kursiv ist die einzige Auszeichnung im Text (Untertitel, Ortsname im
Footer), Versalien gibt es nur in 12–13 px als Label. Keine Unterstreichung außer bei Textlinks im
Fließtext (1 px, `--farbe-akzent`, 3 px Abstand).

Begründung: Das Verhältnis H1 : Body von 44 : 19 (2,3) übernimmt das Maß von helenhard (44 : 20),
das Überschriften groß genug für die Suche und für Bauherren 50+ macht, ohne das Bild zu
überstimmen; darunter wird die Leiter eng (32 → 24 → 19), weil die Seite wenig Text hat und
jede Stufe selten vorkommt. Fraunces statt Cormorant, weil Cormorant bei 19 px zu wenig
x-Höhe für Fließtext hat und Instrument Serif nur einen Schnitt besitzt — Fraunces liefert
mit der optischen Größe eine feine Display-Form für 44 px und eine robuste Textform für 19 px
aus derselben Datei.

## 4. Farben

| Token | Hex | Einsatz | Kontrast gegen Grund |
|---|---|---|---|
| --farbe-grund | `#F5F3EE` | Seitenhintergrund aller Seiten, warmes Off-White | — |
| --farbe-flaeche | `#EAE6DE` | Kopfzeile, Statement-Kasten, Metadaten-Kasten, Kontaktkasten, Footer | 1,12:1 gegen Grund (nur als Fläche, nie als Text) |
| --farbe-text | `#24221F` | Fließtext, Überschriften, Navigation, Wortmarke | 14,31:1 auf Grund · 12,75:1 auf Fläche |
| --farbe-text-2 | `#5A5650` | Metadaten-Werte, Bildunterschriften, Fußnoten, Demo-Hinweis | 6,57:1 auf Grund · 5,85:1 auf Fläche |
| --farbe-text-3 | `#6B665E` | Labels in Versalien, Bildzeile unter dem Hero, inaktive Navigationspunkte | 5,14:1 auf Grund · 4,58:1 auf Fläche (muss ≥ 4,5 — erfüllt auf beiden) |
| --farbe-linie | `#D8D2C7` | Hairlines (Metadaten, Leistungsliste, Footer-Trenner), Bildrahmen gibt es keine | 1,36:1 (Dekor, kein Text) |
| --farbe-akzent | `#8B5A3C` | Ziegel-/Holzton: Textlinks im Fließtext, Chevron-Links, gefüllter Kontakt-Button, Fokusring | 5,22:1 auf Grund · 4,65:1 auf Fläche |
| --farbe-invers | `#F5F3EE` | Text auf dem Akzent-Button (= Grundfarbe) | 5,22:1 auf Akzent |

Rechnung nach WCAG-Formel (relative Luminanz, sRGB-Linearisierung) per Python, alle Werte
oben sind gerechnet, nicht geschätzt. Der Textfarbe auf Akzent-Fläche (`#24221F` auf `#8B5A3C`)
läge bei 2,74:1 — deshalb steht auf dem Button ausschließlich `--farbe-invers`, nie die Textfarbe.

Farbe kommt aus den Fotos: Holzfassaden, dunkler Ziegel, Rasen, Wald. Die Palette selbst ist
warm-neutral (Off-White, Sand, Graubraun), der einzige gesetzte Farbton ist der Ziegel-Akzent,
und der erscheint nur auf Links, dem Kontakt-Button und dem Fokusring. **Keine dunkle
Sektion** auf der ganzen Seite — auch der Footer bleibt hell auf `--farbe-flaeche`. Reinweiß
kommt nur in Fotos vor, Reinschwarz nirgends.

## 5. Raster und Rhythmus

- Container: 1280 px, Rand `clamp(1.25rem, 5.5vw, 5rem)` (bei 1440 px Fensterbreite 80 px beidseitig wie helenhard; bei 390 px 20 px). Nur zwei Elemente verlassen den Container: der Hero der Startseite (randlos, 100 vw) und der Footer-Hintergrund (Fläche randlos, Inhalt im Container).
- Kopfzeile: 88 px hoch Desktop, 64 px Mobil, auf `--farbe-flaeche`, statisch.
- Hero Startseite: Höhe `calc(100svh − 88px − 56px)` Desktop, `calc(100svh − 64px − 48px)` Mobil, mindestens 420 px; darunter die Bildzeile (56 px / 48 px hoch) im Container, linksbündig. Erster Bildschirm = Kopfzeile + Bild + eine Zeile, sonst nichts.
- Spalten je Sektion:
  - Intro-Block: eine Spalte, zentriert, max. 720 px.
  - Projektraster: 2 Spalten (611 px), Gutter 58 px; ab 720 px Breite eine Spalte. Mit 4 bzw. 6 Projekten gehen die Reihen immer auf — keine halbe Reihe.
  - Statement (Büro): Grid 55 fr / 45 fr, Kasten auf `--farbe-flaeche` von der linken Fensterkante bis 55 % Breite, Innenabstand 4 rem; Bild in der rechten Spalte mit `margin-top: −4rem` in den Kasten gezogen. Mobil untereinander, Überlappung −2 rem.
  - Projektseite Kopf: Hero 16:9 im Container; darunter Grid 5 fr / 7 fr — links H1, kursiver Untertitel, Metadatenblock; rechts der Text (max. 62 Zeichen). Gemeinsame linke Kante mit dem Hero-Bild.
  - Projektseite Bildpaar: Grid 7 fr / 5 fr, Gutter 58 px, rechtes Bild beginnt 6 rem tiefer; mobil untereinander ohne Versatz.
  - Leistungen: Liste mit Hairlines, Grid 4 fr / 8 fr je Eintrag (Leistung links als H3, Text rechts); darunter ein Bildpaar wie auf der Projektseite.
  - Kontakt: Grid 5 fr / 7 fr — links Kasten auf `--farbe-flaeche` mit Adresse, Telefon, Mail; rechts drei Sätze, was beim Erstgespräch passiert.
- Sektionsabstand: 9 rem Desktop, 5 rem Mobil. Abstand innerhalb einer Sektion: 2,5 rem; zwischen Kachelreihen 5 rem; Titel über dem Kachelbild 1,25 rem, kursiver Satz darunter 1 rem.
- Ausrichtung: Kopfzeile, Intro-Block und Kacheltitel zentriert (helenhard); alle Textsektionen linksbündig an der Container-Kante; auf der Projektseite teilen sich Bild, H1, Metadaten und Bildpaar dieselbe linke Kante.

## 6. Seiteninventar

| Seite | URL | Zweck | Besonderheit |
|---|---|---|---|
| Startseite | / | Hero, Intro mit Leistungslinks, 4 Projekte, Büro-Statement, Kontakt-Aufforderung, Footer | H1 ist der Intro-Satz („Wohnhäuser im Münsterland …"), nicht ein Text auf dem Bild; Hero randlos über die erste Bildschirmhöhe |
| Projekte | /projekte/ | alle 6 Projekte als Kacheln in 2 Spalten, ohne Filter | Kurzer Einleitungssatz als H1 über dem Raster, sonst nur Kacheln |
| Projekt-Detail | /projekte/{slug}/ | Hero 16:9, Titel, kursiver Untertitel, Metadaten, 60–100 Wörter Text, Bildpaar, Link zum nächsten Projekt | ja, für alle 6 (jedes hat 3 Bilder — ab 3 Bildern Detailseite, darunter nicht). Slugs: haus-am-deich, hofstelle-havixbeck, anbau-hiltrup, wohnhaus-kreuzviertel, aufstockung-greven, haus-im-wald |
| Büro | /buero/ | Statement-Kasten mit Bild, Team als Namensliste mit Rolle (vier Zeilen, Hairlines), Kammer-Hinweis | Keine Portraits (Wunsch C); Namensliste statt Personenraster |
| Leistungen | /leistungen/ | vier Leistungen als Liste mit je 60–90 Wörtern, Bildpaar, Hinweis auf Bauberatung vor Grundstückskauf | Anker je Leistung (`#neubau`, `#umbau`, `#anbau`, `#bauberatung`), die Chevron-Links der Startseite zielen darauf |
| Kontakt | /kontakt/ | Adresse, Telefon, Mail als Klartext, drei Sätze zum Erstgespräch | Kein Formular, keine Karte (Google Maps ohne Einwilligung nicht ladbar; für ein fiktives Büro ohnehin sinnlos) |
| Impressum, Datenschutz | /impressum/, /datenschutz/ | Skeleton | Impressum-Absatz „fiktiv", Demo-Hinweis, Versicherer als fiktiv gekennzeichnet |

Alle Seiten `noindex, follow`; Fußzeile mit „Demo-Website von XPONext, Büro und Projekte fiktiv".

## 7. Navigation

- Punkte: **Projekte · Leistungen — Wortmarke — Büro · Kontakt**. Vier Punkte, zwei links und zwei rechts der zentrierten Wortmarke (helenhard-no-F1). Kontakt als Textlink rechts außen, kein Button in der Leiste. Aktiver Punkt in `--farbe-text`, die übrigen in `--farbe-text-3` (5,14:1), Hover/Fokus wechselt auf `--farbe-text`.
- Wortmarke: „Nordkant Architekten" als Text in Fraunces 26 px / 400, verlinkt auf `/`. Kein SVG, kein Zeichen.
- Verhalten beim Scrollen: statisch, kein Sticky. Die Kopfzeile liegt auf `--farbe-flaeche`, nie über dem Bild — deshalb entfällt jede Abdunklung und der Kontrast der Nav-Links ist unabhängig vom Foto.
- Der Kontakt-Button („Projekt besprechen", gefüllt in `--farbe-akzent`, Text in `--farbe-invers`, rechteckig, 0 px Radius) steht einmal am Ende der Startseite und einmal unter dem Text jeder Projektseite. Außerdem stehen Telefon und Mail in jedem Footer.
- Mobil (bis 900 px): Kopfzeile 64 px, Wortmarke links (20 px), rechts ein Textlink **„Menü"** als `button` mit `aria-expanded` und `aria-controls` (helenhard-no-F12, Bedingung erfüllt); geöffnet wird eine Liste der vier Punkte unter der Kopfzeile auf `--farbe-flaeche` (Ausklappen, kein Vollbild-Overlay), Punkte 21 px mit 56 px Zeilenhöhe als Tap-Ziele. Beschriftung wechselt auf „Schließen". `nav`-Landmark, Skip-Link als erstes Element der Seite.

## 8. Bildkonzept

- Formate je Sektion:
  - Hero Startseite: randlos, Höhe wie in 5. beschrieben, Breite 100 vw — das ergibt bei 1440 × 900 etwa 1440 × 756 (≈ 1,9:1), bei 1920 × 1080 etwa 2:1, bei 390 × 844 ein Hochformat von etwa 390 × 732. `object-fit: cover`, `object-position: 62% 55%` (Haus rechts der Mitte, Rasen unten mitnehmen, Baumkronen oben anschneiden). Mobil dieselbe Datei, Ausschnitt per `object-position` — der Bauer prüft in der Hero-Probe bei 390 × 844, dass Haus und Waldkante im Ausschnitt bleiben; sonst `object-position` auf 66 % 50 % nachziehen.
  - Bildzeile unter dem Hero: „Haus im Wald · Nottuln · 2021", verlinkt auf die Projektseite.
  - Kacheln (Startseite, `/projekte/`): 3:2, 611 px breit, `aspect-ratio: 3 / 2`, `object-fit: cover`.
  - Projektseite Hero: 16:9 im Container (1280 × 720), eingerückt, nicht randlos.
  - Projektseite Bildpaar: beide 3:2, links 7/12 (≈ 720 px), rechts 5/12 (≈ 500 px), rechts 6 rem tiefer beginnend.
  - Statement-Bild (Startseite, `/buero/`): 4:5 Hochformat-Ausschnitt aus `aufstockung-01` (Oberlicht, Holzlamellen) — 500 px breit, `object-position: 50% 45%`.
- Zuschnitt: überall `object-fit: cover` mit `object-position` je Motiv; keine Rahmen, keine Rundungen, keine Schatten, keine Überblendungen. Jedes `<img>` mit `width`/`height`, ab der zweiten Kachelreihe `loading="lazy"`; Hero und Projekt-Hero mit `fetchpriority="high"` und ohne Lazy Loading.
- Anzahl je Seite: Startseite 6 (Hero, 4 Kacheln, Statement), `/projekte/` 6, Projektseite 3, `/buero/` 1, `/leistungen/` 2, `/kontakt/` 0.
- Dateien: WebP, Hero in 1920 / 1440 / 960 px als `srcset`, Ziel unter 250 KB für die 1920er-Stufe (das vorhandene `haus-im-wald-01.webp` hat 1600 px bei 298 KB — für den Hero neu aus dem Pexels-Original mit 1920 px und q75 exportieren, 1600 px reicht auf 1920er-Displays nicht ohne Unschärfe). Kacheln 611 / 1222 px unter 80 KB bzw. 200 KB.
- Stockfoto-Suchbegriffe (nur Referenz, aus `BILDER.md`): Haus am Deich `modern timber house exterior garden` (Querformat) · Hofstelle `renovated brick farmhouse interior` (Querformat) · Gartenhaus `glass extension house garden` (Querformat) · Kreuzviertel `narrow modern townhouse facade` (Querformat 16:9) · Aufstockung `wooden roof extension interior light` (Querformat) · Haus im Wald `minimalist house forest exterior` (Querformat). Alt-Texte beschreiben das Gezeigte ohne Ortsbehauptung („Zweigeschossiges Wohnhaus mit Holzfassade und dunklem Ziegelsockel zwischen Kiefern"), da die Motive keine realen Projekte in Nottuln oder Telgte sind.
- **Hero-Bild: `haus-im-wald-01.webp`.** Gründe: (1) Es ist das ruhigste der sechs Erstbilder — warme Holzfassade, dunkler Ziegel, Wald, weiches Licht, fast kein Himmel; genau die Palette der Seite, und kein heller Himmelsstreifen direkt unter der Kopfzeile. (2) Das Haus sitzt rechts der Mitte mit Rasen davor, das Motiv verträgt den Beschnitt auf 2:1 und auf Hochformat. (3) Es zeigt ein Wohnhaus, nicht ein Interieur — private Bauherren sehen im ersten Moment die Aufgabe, für die sie ein Büro suchen. Nicht gewählt: `haus-am-deich-01` (gesättigter blauer Himmel und leuchtendes Grün überstimmen die Palette, wirkt wie Stock), `aufstockung-01` (starkes Motiv, aber ein Oberlicht sagt einem Bauherrn nichts über Häuser — als Statement-Bild besser aufgehoben), `gartenhaus-01` (unruhig, alpin), `kreuzviertel-01` (Verkaufszelt und Schild im Bild, siehe 11.), `hofstelle-01` (volle Landhausküche, gelbe Wand).
- Kachel-Zuordnung Startseite (4 von 6): Haus am Deich, Umbau Hofstelle, Anbau Gartenhaus, Haus im Wald — die beiden mit den schwächsten Erstbildern (Kreuzviertel, Aufstockung) erscheinen nur auf `/projekte/`, bis die Bildfrage aus 11. geklärt ist.

## 9. Motion

- Textlinks: Unterstreichung `--farbe-akzent` wechselt bei Hover/Fokus auf `--farbe-text`, 200 ms `ease-out`. Navigationspunkte: Farbwechsel `--farbe-text-3` → `--farbe-text`, 200 ms.
- Kachelbild: bei Hover/Fokus der Kachel `transform: scale(1.02)` innerhalb eines `overflow: hidden`-Rahmens, 500 ms `cubic-bezier(0.2, 0, 0, 1)`. Titel und Untertitel bleiben unverändert — Hover trägt keine Information.
- Mobile-Menü: Ausklappen der Liste über `max-height`, 250 ms `ease-out`.
- Sonst nichts: kein Fade-in des Heros (würde den LCP-Zeitpunkt verschieben), keine Scroll-Einblendungen, kein Parallax, kein Sticky.
- Alles unter `prefers-reduced-motion: reduce` abgeschaltet (Transitions auf 0 ms, Scale entfällt).
- Kein Preloader, kein Video, kein Autoplay — der Hero ist ein `<img>`.

## 10. Bewusst nicht übernommen

Der Prüfer prüft, dass diese Muster tatsächlich nicht verbaut sind.

| Muster | Grund |
|---|---|
| helenhard-no-F2 als **Video** | Urteil bedingt; 16,5 MB bei der Referenz. Hier ein Standbild — die Wirkung kommt aus der Größe, nicht aus Bewegung |
| helenhard-no-F3 Handskizzen-Ebene | Urteil `nicht`: Eigenschöpfung von Studio Oker, im Nachbau als Kopie erkennbar; das Büro hat keine eigenen Skizzen |
| helenhard-no-F6 Newsliste | bedingt (Redaktion): ein fiktives Büro hat keine Aktualitäten; ein Eintrag von 2021 würde die Seite datieren |
| helenhard-no-F8 Typologie-Filter | bedingt (ab ~12 Projekten): bei sechs Projekten zeigt „Anbau" eine Kachel |
| helenhard-no-F10 Foto + Plan | übernehmen, aber Bedingung „ein Plan je Projekt" nicht erfüllbar — Stockfotos haben keine Grundrisse. Ersatz: pietboon-com-F7 |
| helenhard-no-F11 Lazy Loading ohne Maße | Urteil `nicht` |
| helenhard-no-F5 graubrauner Footer | Teil von F5 weggelassen: keine dunkle Sektion, Abgrenzung zur Innenarchitektur-Referenz |
| helenhard Rand um den Hero (80 px) | Nutzer-Vorgabe „offenes Bild über die ganze erste Bildschirmhöhe" — randlos; und ein Unterschied zur Referenz, damit die Seite nicht wie helenhard aussieht |
| big-dk-F2 Metadaten rechtsbündig neben dem Bild | übernehmen laut Katalog, aber die Seite ist auf der Projektseite in zwei Spalten unter dem Bild organisiert (pietboon-F11); zwei Metadaten-Varianten wären eine zu viel. Helenhard-F9 gewählt |
| big-dk-F3 gemeinsame Kante statt Zentrierung | nur teilweise: Projektseite ja, Startseite zentriert (Intro, Kacheltitel). Nicht als Muster beansprucht |
| big-dk-F5 Navigation nach Disziplin | bedingt: vier Leistungen sind trennbar, aber vier Leistungs-Menüpunkte plus Projekte/Büro/Kontakt wären sieben — die Leistungen laufen über die Chevron-Liste (pietboon-F15) und Anker |
| big-dk-F6 Endlos-Liste ohne Hero | bedingt (30+ Projekte); sechs Projekte, und die Vorgabe verlangt einen Hero |
| big-dk-F7 Projektsignets, big-dk-F8 Preloader | Urteil `nicht` |
| big-dk 18-px-H1 | H1 hier 44 px — Such- und Orientierungsanker für Bauherren 50+ |
| pietboon-com-F1 Avenir-Prinzip (Sans, 400/500) | bedingt (Ersatzschrift); die Seite nimmt ohnehin eine Serife |
| pietboon-com-F3 zweizeiliger Kopf, F10 Filter + Google Maps, F13 fixierte Kontaktleiste | Urteil `nicht` |
| pietboon-com-F4 Hero-Slider | bedingt (≥ 3 aktuelle Motive); Slider ist Anti-Muster und Wunsch C schließt ihn aus |
| pietboon-com-F5 Abschnittslinie mit Karussell | Karussell ist ein Slider; übernehmen-Teil (Titel + 1-px-Linie) nicht nötig, die Seite hat nur eine Projektsektion |
| pietboon-com-F8 Wechsel 3 Kacheln / 1 Featured | bedingt (ab 8 Projekten, Vielfache von 4) |
| pietboon-com-F9 Kachel mit grauem Textfuß | übernehmen, aber es gibt nur ein Kachelmuster auf der Seite: helenhard-F7. Zwei Kachelformen wären unruhig |
| pietboon-com-F12 Galerie mit Versatz | bedingt (8–12 Fotos je Projekt); drei Fotos, reduziert auf F7 |
| pietboon-com-F14 Kopfzeile am unteren Rand (Mobil) | bedingt erfüllbar, aber unnötig: vier Punkte, kurze Seiten; Text-„Menü" oben reicht |
| Text auf dem Hero, Claim, Button auf dem Bild | Wow-Faktor ist das textfreie Bild; Claim folgt darunter als H1 |
| Team-Portraits, Stock-Personen | Wunsch C — Namensliste |
| Kontaktformular, Karte | Kein Formular (Datenschutz, fiktives Büro), keine Karte (Fremd-Request) |

## 11. Offene Fragen an den Nutzer

Wird am Checkpoint 2 (Brief + Hero-Probe) geklärt.

1. **Wohnfläche je Projekt:** Der Metadatenblock braucht fünf gefüllte Einträge; „Wohnfläche" steht nicht in `inhalte.md`. Vorschlag: plausible fiktive Werte (Haus am Deich 185 m², Hofstelle 240 m², Anbau 45 m² Erweiterung, Kreuzviertel 160 m², Aufstockung 60 m² Dachgeschoss, Haus im Wald 150 m²) — mit dem Demo-Hinweis abgedeckt. Einverstanden, oder Wohnfläche weglassen und stattdessen „Bauweise" (Holzbau, Ziegel, Glas/Stahl) als fünften Eintrag?
2. **Kursive Untertitel-Sätze** je Projekt (helenhard-F7, ein Satz von 5–9 Wörtern unter der Kachel, z. B. „Ein Holzhaus hinter dem Deich, für drei Generationen"): Der Bauer formuliert sie aus den Eckdaten in `inhalte.md`; Freigabe der sechs Sätze mit der Hero-Probe.
3. **`kreuzviertel-01.webp`:** Das Bild zeigt eine Reihenhaus-Anlage mit Verkaufszelt und Bauträger-Schild im Vordergrund — als „Stadthaus auf schmalem Grundstück im Kreuzviertel" wenig glaubwürdig. Dazu kommt: `kreuzviertel-01` und `kreuzviertel-02` sind laut `BILDER.md` dasselbe Pexels-Foto (gleiche URL, gleiche Dateigröße 243.344 Byte) — das Projekt hat faktisch nur zwei Bilder und fällt damit unter die Schwelle „Detailseite ab 3 Bildern". Ersatz durch `kreuzviertel-03` (nicht gesichtet) als Erstbild prüfen und ein zweites Motiv neu suchen (`narrow brick townhouse street facade`).
4. **`hofstelle-01.webp`:** Volle Landhausküche mit gelber Wand — als Kachelbild neben Holz und Ziegel ein Fremdkörper. Vorschlag: `hofstelle-03` (Dachgeschoss mit Balken, laut `BILDER.md`) als Erstbild der Kachel, `hofstelle-01` als drittes Bild auf der Projektseite.
5. **Mobile-Hero:** Der Brief setzt auch auf Mobil die ganze erste Bildschirmhöhe (Hochformat-Ausschnitt aus dem Querformat). Alternative wäre ein 4:5-Bild mit sichtbarer Bildzeile und Intro-Anfang. Entscheidung an der Hero-Probe bei 390 × 844.
6. **Button-Beschriftung:** „Projekt besprechen" (Vorschlag) oder „Erstgespräch anfragen"? Kein „Termin buchen".
7. **Schriftwahl der Innenarchitektur-Referenz:** Damit die Abgrenzung hält, sollte die dritte Referenzseite nicht Fraunces nehmen (Cormorant Garamond oder Instrument Serif liegen im Skeleton). Das ist eine Notiz für den nächsten Brief, keine Entscheidung dieser Seite.

---

**Kombinierte Referenzen:** helenhard-no (Hero ohne Text, geteilte Navigation, eine Serife in Leichtgewicht, Kacheln mit Titel oben und kursivem Satz unten, Metadatenblock, Standort-Footer) + pietboon-com (zwei Graustufen mit einem Akzent nur auf Schaltflächen, zentrierter Intro-Block mit Leistungslinks, Statement-Kasten mit überlappendem Bild, eingerückter 16:9-Projektkopf, versetztes Bildpaar) + big-dk (Hierarchie ohne Bold, Ort in Versalien). Genau diese, weil ein Büro mit sechs Projekten und drei Querformaten je Projekt weder ein Endlos-Raster noch eine Versatz-Galerie füllen kann — helenhard liefert den ruhigen Ton und den einen großen Moment, den der Nutzer vorgegeben hat, Piet Boon liefert die Flächen, die bei wenig Bildmaterial den Rhythmus tragen, und BIG die Disziplin, alles ohne Fettschrift und Akzentfarbe im Text zu ordnen.
