# Design-Brief: Studio Lindenau

| | |
|---|---|
| **Projektart** | Referenz (fiktives Innenarchitektur-Studio, `noindex`, Demo-Hinweis in der Fußzeile) |
| **Realität** | Innenarchitektur-Studio, Inhaberin + 3 Mitarbeitende, 8 Projekte, je 4 Profi-Interieurfotos (Stock, alle Querformat 3:2), gehobene private Auftraggeber, Gastronomie/Hotellerie, Praxen; Hamburg, Norddeutschland, Berlin, Sylt; Wortmarke aus Text mit Serif, keine Portraits, sehr wenig Text auf der Startseite |
| **Erstellt** | 2026-09-07, Rolle Designer |
| **Referenzen** | pietboon-com, robmills-com-au, helenhard-no (dazu drei Einzelfeatures aus big-dk über den Katalog) |

## 1. Konzept in zwei Sätzen

Nach fünf Sekunden: eine dunkle, fast leere Fläche, darauf ein einziger Satz in einer feinen Serife und ein großes, ruhig einschwebendes Innenraumfoto — die Seite verhält sich wie ein gut gestalteter Raum, in dem nichts um Aufmerksamkeit kämpft. Nach dreißig Sekunden: ein kleines Hamburger Studio richtet Wohnungen, Restaurants, Hotels und Praxen ein, acht Projekte kann man sich als große Einzelbilder ansehen, und der Weg zum Gespräch ist eine Telefonnummer und eine Mailadresse am Ende jeder Seite.

**Der eine Wow-Faktor:** Die Projekte stehen als einzelne, große Bilder mit je zwei Zeilen Text auf abwechselnd dunklen und hellen Sektionen, gesetzt in einer leichten Serife mit viel Luft — jedes Bild blendet beim Erscheinen ruhig ein und kommt dabei minimal aus einem leichten Zoom zur Ruhe.

Das ist die Vorgabe des Nutzers (aus pietboon.com und robmills.com.au abgeleitet). Sie wird nicht mit einem zweiten Effekt ergänzt: kein Video, kein Slider, keine Skizzenebene, keine scrollgekoppelte Bewegung. Die Bewegung ist ausschließlich das Einblenden und der leichte Zoom, einmal je Bild, unter `prefers-reduced-motion` aus.

**Abgrenzung zu Nordkant Architekten** (erste Referenzseite): Nordkant setzt Fraunces, ein warmes Off-White ohne dunkle Sektion, einen Ziegel-Akzent und ein randloses Hero-Foto über die volle Höhe. Studio Lindenau setzt Cormorant Garamond mit DM Sans, beginnt auf jeder Seite mit einer **dunklen** Sektion, in der das erste Bild **eingerückt** auf der dunklen Fläche steht (kein randloses Vollbild), und wechselt danach zwischen hell und dunkel. Der einzige gemeinsame Nenner ist „warme Neutralpalette, Serife, kein Slider" — das ist der Stil der Zielgruppe, nicht der einer Seite.

## 2. Übernommene Features

Jedes Muster mit Feature-ID aus `patterns/_katalog.md`. Drei Referenzen kombiniert.

| ID | Feature | Wo auf der Seite | Warum es zur Realität passt |
|---|---|---|---|
| pietboon-com-F11 | Projektdetail: Hero 16:9 eingerückt, Titel und Text erst darunter | Projekt-Detailseite, Kopf; **außerdem als Prinzip des Start-Heros** (Bild eingerückt auf der Fläche statt randlos, Text erst neben bzw. unter dem Bild) | Jedes Projekt hat genau ein gutes Querformat als Aufmacher und 40–80 Wörter Text — die Bedingung „ein gutes Querformat je Projekt, 60–100 Wörter" ist erfüllt. Das eingerückte Bild ist zugleich die Abgrenzung zum randlosen Nordkant-Hero. Urteil `übernehmen`. |
| pietboon-com-F2 | Warmgrauer Seitengrund mit zweiter Stufe für Flächen, ein Akzent nur auf Buttons | Alle hellen Sektionen; Kasten der Studio-Sektion; Kontakt-Button | Zwei Graustufen plus ein gedeckter Akzent tragen den Rhythmus auch dort, wo kein Foto steht (Leistungen, Studio, Kontakt). Für die dunklen Sektionen wird dasselbe Prinzip gespiegelt (Grund + eine hellere Stufe + ein heller Akzent). Urteil `übernehmen`. |
| pietboon-com-F15 | Zentrierter Intro-Textblock mit Chevron-Linkliste | Startseite, erste helle Sektion unter dem Hero | Das Studio hat genau einen Absatz Selbstbeschreibung und fünf Leistungsfelder — der Block ist der einzige Fließtext der Startseite und ersetzt einen Menüpunkt „Leistungen" im Sichtfeld. Urteil `übernehmen`. |
| pietboon-com-F6 | Versetzter Hintergrundkasten, Bild überlappt den Kasten | Startseite, Sektion „Studio" (hell); Seite /studio/ | Kein Portrait vorhanden — deshalb nicht robmills-F6 (das braucht ein Porträt), sondern ein Projektfoto, das über einen Farbkasten mit Selbstbeschreibung, Teamnamen und Kammerangabe ragt. Text bleibt unter 120 Wörtern. Urteil `übernehmen`. |
| pietboon-com-F7 | Zwei Fotos in ungleicher Höhe und versetztem Beginn | Projekt-Detailseite (Bild 3 + 4 als Paar); Seite /studio/ | Jedes Projekt hat vier Querformate; das zweite und dritte Bild als großes Einzelbild, das dritte und vierte als versetztes Paar — so entsteht mit vier Fotos ein Rhythmus ohne Raster. Urteil `übernehmen`. |
| helenhard-no-F7 | Projektkachel: Titel zentriert über dem Bild, Untertitel-Zeile zentriert darunter | Startseite (4 Projekte, dunkle Sektion); /projekte/ (alle 8, helle Sektion) | Acht Projekte, alle 3:2 — Bedingung „ab 4 Projekten, gleiches Format" erfüllt. Kein Hover-Overlay, kein Textfuß, keine Kachelfläche: nur Bild und zwei Zeilen, das ist der Wow-Faktor. Die kursive Untertitel-*Satz*-Zeile wird durch big-dk-F4 ersetzt (siehe nächste Zeile), weil `inhalte.md` keine Untertitelsätze liefert und keine erfunden werden. Urteil `übernehmen`. |
| big-dk-F4 | Ort in Versalien als Untertitel jeder Projektkachel | Zeile unter jedem Projektbild: „HAMBURG · 2024" | Ort und Jahr sind die einzigen belegten Metadaten je Projekt; als 12-px-Versalien in DM Sans sind sie die leiseste Textform der Seite und zugleich der lokale SEO-Baustein (Hamburg, Sylt, Berlin). Urteil `übernehmen`. |
| big-dk-F2 | Metadatenblock rechtsbündig neben dem Bild | Projekt-Detailseite: schmale Randspalte links neben dem ersten großen Bild (Ort, Jahr, Leistung, Fläche), rechtsbündig an die Bildkante gesetzt | Der Nutzer will „Text als kurze Randspalte" neben großen Bildern. wolveridge-F9 (Textspalte + Bildspalte) fällt weg, weil es 6+ Fotos verlangt; big-dk-F2 braucht nur Eckdaten und funktioniert mit 4 Bildern. Urteil `übernehmen`. |
| big-dk-F3 | Gemeinsame Kante statt Zentrierung | Alle zweispaltigen Blöcke: Metadaten-Randspalte und Bild auf der Detailseite, Kasten und Bild in der Studio-Sektion, Fußzeilen-Spalten | Die Seite lebt von Luft; Luft wirkt nur ruhig, wenn die Kanten fluchten. Zentrierung gibt es ausschließlich beim Intro-Block (F15) und bei Titel/Ort über und unter den Projektbildern (F7). Urteil `übernehmen`. |
| helenhard-no-F4 | Eine Serife in Leichtgewicht, Kursiv als einzige Auszeichnung | Wortmarke, Hero-Satz, alle Überschriften, kursive Bildunterschriften | Bedingung „selbst gehostete Serife mit vergleichbarem Kursiv" erfüllt: Cormorant Garamond (OFL, variabel 300–700, Kursiv) aus dem Skeleton-Ordner. Abweichung: die Serife trägt nur Display-Größen; Fließtext und Labels laufen in DM Sans, weil Cormorant bei 17 px zu wenig x-Höhe für Text auf dunklem Grund hat. Urteil `bedingt`, Bedingung erfüllt. |
| helenhard-no-F1 | Geteilte Navigation mit zentrierter Wortmarke | Kopfzeile aller Seiten (auf dunklem Grund) | „Studio Lindenau" sind zwei Wörter, breit genug für die Mitte. Vier Punkte, zwei links, zwei rechts, kein CTA-Button in der Leiste. Urteil `übernehmen`. |
| helenhard-no-F12 | Mobile-Kopfzeile aus drei Textelementen | Mobil: „Kontakt" links, Wortmarke mittig, „Menü" rechts | Textlinks statt Burger-Icon passen zur Serifen-Wortmarke; Bedingung erfüllt: `aria-expanded`/`aria-controls` am Menü-Button, Vollbild-Overlay auf dunklem Grund. Urteil `bedingt`, Bedingung erfüllt. |
| helenhard-no-F13 | Footer mit je einem Block pro Standort | Fußzeile (dunkel): ein Standort, eine Spalte mit Anschrift, Telefon, Mail | Ein Standort (Am Sandtorkai 4) — laut Bedingung eine Spalte statt zwei; daneben Navigation und Rechtstexte. Urteil `übernehmen`. |
| robmills-com-au-F3 | Vertikale Linie, die beim ersten Scroll aus dem Hero in den Folgeabschnitt wächst | Startseite: 1-px-Linie mittig, wächst aus der dunklen Hero-Sektion 8 rem in die helle Intro-Sektion hinein | Zehn Zeilen CSS, keine Bildvoraussetzung, und die Linie bindet den Hell-Dunkel-Wechsel optisch zusammen. Urteil `übernehmen`. |
| robmills-com-au-F10 | Lazy-Fade: jedes nachgeladene Bild blendet verzögert ein | Alle Projektbilder ab dem zweiten Bild jeder Seite | Das ist die „ruhige Bewegung" der Vorgabe. Bedingung erfüllt: jedes `<img>` mit `width`/`height` und nativem `loading="lazy"`, Einblenden per IntersectionObserver, kein lazysizes. Urteil `bedingt`, Bedingung erfüllt. |

## 3. Typografie

Zwei Familien, beide self-hosted aus `skeleton/assets/fonts/` (OFL): **Cormorant Garamond**
(variabel 300–700, mit Kursiv) für alles, was größer als 22 px ist, und **DM Sans** (variabel
300–700, opsz) für Fließtext, Navigation und Labels. Feste Rollenteilung: Cormorant kommt nie
unter 22 px vor, DM Sans nie über 17 px. Alle anderen Familien werden aus dem Fonts-Ordner
der Seite gelöscht. `font-optical-sizing: auto` für DM Sans.

| Rolle | Familie (aus skeleton/assets/fonts) | Größe Desktop | Größe Mobil | Gewicht | Laufweite | Zeilenhöhe |
|---|---|---|---|---|---|---|
| Hero (ein Satz auf dunklem Grund) | Cormorant Garamond | 64 px | 38 px | 300 | −0,01 em | 1,1 |
| H1 (Unterseiten, Projekttitel) | Cormorant Garamond | 56 px | 36 px | 300 | −0,01 em | 1,1 |
| H2 (Sektionstitel) | Cormorant Garamond | 40 px | 30 px | 400 | 0 | 1,15 |
| H3 (Projekttitel über dem Bild) | Cormorant Garamond | 30 px | 24 px | 400 | 0 | 1,2 |
| Kursiv-Zeile (Bildunterschrift, Standort im Footer) | Cormorant Garamond Italic | 22 px | 19 px | 400 | 0 | 1,4 |
| Body | DM Sans | 17 px | 16 px | 400 | 0 | 1,6 |
| Label/Meta (Ort · Jahr, Metadaten-Label, Demo-Hinweis) | DM Sans | 12 px, Versalien | 12 px, Versalien | 500 | 0,12 em | 1,5 |
| Navigation | DM Sans | 15 px | 17 px (im Vollbild-Menü 28 px) | 400 | 0,04 em | 1 |
| Wortmarke „Studio Lindenau" | Cormorant Garamond | 28 px | 22 px | 500 | 0,02 em | 1 |
| Button (nur Kontakt) | DM Sans | 15 px | 15 px | 500 | 0,04 em | 1 |

Fließtext-Zeilenbreite höchstens 60 Zeichen (≈ 560 px bei 17 px); der zentrierte Intro-Block
darf 64 Zeichen breit werden. Kursiv ist die einzige Auszeichnung in Cormorant, Versalien gibt
es nur in DM Sans 12 px. Textlinks im Fließtext: 1 px Unterstreichung in `--farbe-akzent`
(hell) bzw. `--farbe-dunkel-akzent` (dunkel), 3 px Abstand. Keine Schriftgewichte über 500.

Begründung: Das Verhältnis Hero : Body von 64 : 17 (3,8) ist bewusst weiter als bei Nordkant
(2,3) und Helen & Hard (2,2) — die Seite hat fast keinen Fließtext, also darf die Display-Stufe
das Bild begleiten statt sich unterzuordnen; darunter fällt die Leiter schnell (56 → 40 → 30),
weil jede Stufe nur ein- bis zweimal je Seite vorkommt. Cormorant Garamond statt Fraunces, weil
sie in 300 bei 64 px die feinste Strichstärke der verfügbaren Serifen hat (Instrument Serif hat
nur einen Schnitt, Fraunces ist an Nordkant vergeben); DM Sans als Textschrift, weil Cormorant
bei 17 px auf `#1F1D1A` zu wenig x-Höhe hat und eine niedrig-kontrastige Grotesk neben einer
kontrastreichen Serife ruhig bleibt.

## 4. Farben

Zwei Paletten, eine je Sektionsart. Jede Seite beginnt dunkel (Kopfzeile + erstes Bild), der
Körper ist hell, die Fußzeile dunkel; die Startseite wechselt zusätzlich in der Mitte noch
einmal (Projekte dunkel, Studio hell).

**Helle Sektionen**

| Token | Hex | Einsatz | Kontrast gegen Grund |
|---|---|---|---|
| --farbe-grund | `#F4F1EA` | Grund aller hellen Sektionen (Intro, Studio, Leistungen, Projektliste, Detail-Körper) | — |
| --farbe-flaeche | `#E9E4DA` | Kasten der Studio-Sektion (F6), Metadaten-Hintergrund, Formularfelder | 1,12:1 gegen Grund (nur als Fläche, nie als Text) |
| --farbe-text | `#1F1D1A` | Fließtext, Überschriften, Navigation im Vollbild-Menü | 14,91:1 auf Grund · 13,27:1 auf Fläche |
| --farbe-text-2 | `#5C574F` | Metadaten-Werte, Bildunterschriften, Demo-Hinweis | 6,35:1 auf Grund · 5,65:1 auf Fläche |
| --farbe-text-3 | `#665E56` | Labels in Versalien (Ort · Jahr, Metadaten-Label) | 5,64:1 auf Grund · 5,02:1 auf Fläche (muss ≥ 4,5 — erfüllt auf beiden) |
| --farbe-linie | `#D9D3C8` | Hairlines (Metadaten, Leistungsliste, Chevron-Liste) | 1,32:1 (Dekor, kein Text) |
| --farbe-akzent | `#7A5F3E` | Nussbaum-Ton: Textlinks, Chevrons, Fokusring, Rahmen des Outline-Buttons auf hell | 5,27:1 auf Grund · 4,69:1 auf Fläche |
| --farbe-invers | `#F4F1EA` | Text auf dem gefüllten Akzent-Button (= Grundfarbe) | 5,27:1 auf Akzent |

**Dunkle Sektionen**

| Token | Hex | Einsatz | Kontrast gegen Grund |
|---|---|---|---|
| --farbe-dunkel | `#1F1D1A` | Grund von Kopfzeile + Hero, Projektsektion der Startseite, Fußzeile, Vollbild-Menü, Detail-Kopf | — |
| --farbe-dunkel-flaeche | `#2A2724` | Zweite Stufe: Kontaktkasten in der Fußzeile, Platzhalter der Bilder vor dem Laden | 1,13:1 gegen Dunkel (nur als Fläche) |
| --farbe-dunkel-text | `#F4F1EA` | Hero-Satz, Wortmarke, Navigation, Projekttitel, Fließtext auf dunkel | 14,91:1 auf Dunkel · 13,16:1 auf Dunkel-Fläche |
| --farbe-dunkel-text-2 | `#B5AEA3` | Sekundärtext auf dunkel (Adresse im Footer, Bildunterschrift) | 7,65:1 auf Dunkel · 6,75:1 auf Dunkel-Fläche |
| --farbe-dunkel-text-3 | `#9E978B` | Labels in Versalien auf dunkel (Ort · Jahr unter den Projektbildern, Rechtstexte-Links) | 5,81:1 auf Dunkel · 5,13:1 auf Dunkel-Fläche (muss ≥ 4,5 — erfüllt) |
| --farbe-dunkel-linie | `#3A3631` | Hairlines auf dunkel, die wachsende Linie (F3) im dunklen Teil | 1,40:1 (Dekor, kein Text) |
| --farbe-dunkel-akzent | `#C9A97E` | Heller Nussbaum/Messing-Ton: Textlinks auf dunkel, Fokusring auf dunkel, gefüllter Kontakt-Button in der Fußzeile | 7,57:1 auf Dunkel · 6,69:1 auf Dunkel-Fläche |
| (Text auf --farbe-dunkel-akzent) | `#1F1D1A` | Beschriftung des hellen Buttons auf dunkel | 7,57:1 |

Rechnung nach WCAG-Formel (relative Luminanz, sRGB-Linearisierung) per Python, alle Werte
oben sind gerechnet, nicht geschätzt. Zwei Werte wurden im Rechenlauf korrigiert: ein erster
Akzent `#8A6E4B` lag mit 4,22:1 auf Grund unter der Schwelle und wurde auf `#7A5F3E`
abgedunkelt; ein erstes `--farbe-text-3` `#6E6860` lag auf der Fläche bei 4,35:1 und wurde
auf `#665E56` gesetzt. Die dunkle Textfarbe auf dem dunklen Akzent-Button geht (7,57:1), die
helle Textfarbe auf dem hellen Akzent-Button geht (5,27:1) — die Textfarbe `#1F1D1A` auf dem
Akzent `#7A5F3E` läge bei 2,83:1 und ist deshalb verboten. Text steht **nie auf einem Foto**;
die Navigation liegt auf der dunklen Fläche über dem eingerückten Bild, nicht darauf.

Farbe kommt aus den Fotos: Eiche, Nussbaum, Leinen, Messing, gedämpftes Grün. Die Palette
selbst ist warm-neutral (Off-White, Sand, Kohle), die beiden Akzente sind zwei Helligkeiten
desselben Holztons. Reinweiß und Reinschwarz kommen nirgends vor; das dunkle `#1F1D1A` ist ein
warmes Kohleschwarz mit sichtbarem Braunanteil, damit die Fotos darauf nicht kalt wirken.
Ein Foto auf dunklem Grund braucht keine Abdunklung, weil kein Text darauf steht.

## 5. Raster und Rhythmus

- Container: 1280 px (bei 1440 px Fenster also 80 px Rand beidseitig), Rand 5 rem ab 1024 px,
  2,5 rem bis 1024 px, 1,25 rem unter 640 px. Kopfzeile, Bilder, Text und Fußzeile teilen
  sich dieselben Containerkanten — auch in den dunklen Sektionen; die dunkle **Fläche** läuft
  über die volle Fensterbreite, ihr **Inhalt** hält den Container.
- Eingerückte Bilder: 75 % der Containerbreite (960 px), an eine Containerkante gesetzt —
  Startseite abwechselnd links (Projekt 1, 3) und rechts (Projekt 2, 4), `/projekte/` gleiches
  Wechselspiel über alle acht. Start-Hero-Bild 70 % (896 px), rechtsbündig an der Containerkante,
  der Hero-Satz links davon auf 30 % minus 4 rem Abstand, vertikal an der Bildunterkante
  ausgerichtet (gemeinsame Kante, big-dk-F3). Detail-Hero volle Containerbreite (1280 px).
- Spalten je Sektion: Intro einspaltig 640 px zentriert (F15) · Projekte einspaltig, ein Bild
  je Reihe (F7) · Studio-Sektion `55fr 45fr` mit Kasten links und Bild, das 4 rem in den
  Kasten ragt (F6) · Detail-Körper `280px 1fr` mit 4 rem Gasse: Randspalte rechtsbündig,
  Bild 960 px (F2) · F7-Paar `560px 640px` mit 5 rem Gasse, linkes Bild beginnt 4 rem tiefer ·
  Fußzeile `1fr 1fr 1fr` (Standort, Navigation, Rechtstexte).
- Hero-Höhe Startseite: `min-height: clamp(560px, 85vh, 900px)`, nicht 100 vh — man soll
  sehen, dass es weitergeht. Detail-Kopf: Kopfzeile + Bild + Titel, keine Mindesthöhe.
- Sektionsabstand: 10 rem Desktop, 5 rem Mobil. Abstand innerhalb: 4 rem Desktop, 2,5 rem
  Mobil. Zwischen zwei Projektbildern: 8 rem Desktop, 4 rem Mobil. Titel über dem Bild 1,5 rem
  Abstand, Ort-Zeile unter dem Bild 1 rem.
- Ausrichtung: linksbündig an der Containerkante als Regel; zentriert nur Intro-Block, Titel
  und Ort-Zeile über/unter den Projektbildern und der Kopf der Detailseite (H1 + Kursiv-Zeile).
- Hell-Dunkel-Regel für jede Seite: Kopfzeile + erste Bildsektion dunkel → Körper hell →
  Kontakt + Fußzeile dunkel. Nur die Startseite hat zusätzlich in der Mitte die dunkle
  Projektsektion (Reihenfolge: dunkel · hell · dunkel · hell · dunkel). Zwei gleiche Sektionen
  stoßen nie aneinander.
- Mobil (< 640 px): alles einspaltig, eingerückte Bilder auf volle Containerbreite, F7-Paar
  stapelt ohne Versatz, Studio-Kasten ohne Überlappung (Bild oben, Kasten darunter), Hero-Satz
  über dem Bild statt daneben.

## 6. Seiteninventar

| Seite | URL | Zweck | Besonderheit |
|---|---|---|---|
| Startseite | / | In 30 Sekunden zeigen, was das Studio macht, für wen und wo | Dunkler Hero (Satz + eingerücktes Bild, F11-Prinzip) → Intro hell (F15) → 4 Projekte dunkel (F7 + big-dk-F4, F10-Einblenden) → Studio hell (F6) → Kontaktkasten + Fußzeile dunkel (F13). Sechs Bilder, ein Absatz Fließtext, fünf Chevron-Links |
| Projekte | /projekte/ | Alle acht Projekte als große Einzelbilder | Kopf dunkel (H1 „Projekte", eine Zeile mit den drei Leistungsfeldern als Klartext, kein Filter), Liste hell: acht Bilder 960 px abwechselnd links/rechts, Titel darüber, Ort · Jahr darunter (F7 + big-dk-F4) |
| Projekt-Detail | /projekte/{slug}/ | Ein Projekt mit vier Bildern und 40–80 Wörtern | ja, für alle 8 (jedes hat 4 Bilder). Kopf dunkel: Bild 1 volle Containerbreite 16:9 (F11), darunter H1 + Kursiv-Zeile (Leistungsfeld, Ort) zentriert. Körper hell: Randspalte mit Metadaten rechtsbündig an Bild 2 (big-dk-F2), Absatz 40–80 Wörter in der Randspalte darunter, Bild 3 + 4 als versetztes Paar (F7). Am Ende „Nächstes Projekt" mit Titel als Textlink, kein Bild-Slider |
| Studio | /studio/ | Wer dahintersteht, wie gearbeitet wird | Kopf dunkel mit H1 „Studio" und einem Satz; Körper hell: F6-Kasten (Selbstbeschreibung, Teamliste ohne Portraits, Kammer), F7-Bildpaar aus zwei Projektfotos; Kontakt + Fußzeile dunkel. URL `/studio/` statt `/buero/`, weil das Büro sich „Studio" nennt |
| Leistungen | /leistungen/ | Die fünf Leistungsfelder als Liste | Kopf dunkel (H1 „Leistungen"); Körper hell: fünf Einträge mit Hairlines, je H2 + 1–2 Sätze + Verweis auf ein bis zwei passende Projekte als Textlink; kein Bild, keine Preise |
| Kontakt | /kontakt/ | Anschrift, Telefon, Mail | Kopf dunkel mit H1 und Telefonnummer als große Zeile in Cormorant; Körper hell mit Anschrift, Mail, Öffnungszeiten-Hinweis „nach Vereinbarung"; **kein Formular, keine Karte** (Google Maps lädt Google Fonts, siehe pietboon-F10) |
| Impressum, Datenschutz | /impressum/, /datenschutz/ | Skeleton | Kopf dunkel, Körper hell, Absatz „fiktiv" im Impressum, Demo-Hinweis in jeder Fußzeile, alle Seiten `noindex, follow` |

## 7. Navigation

- Punkte (4): links **Projekte**, **Studio** · Wortmarke „Studio Lindenau" mittig (Cormorant
  500, 28 px, als Text, Link zur Startseite) · rechts **Leistungen**, **Kontakt** (helenhard-F1).
  Kontakt ist ein normaler Textlink, **kein Button in der Leiste** — der einzige gefüllte Button
  der Seite sitzt im Kontaktkasten der Fußzeile („Anfrage per E-Mail", `mailto:`).
- Verhalten beim Scrollen: **statisch**, kein Sticky, kein Einblenden. Die Kopfzeile ist Teil
  der dunklen Startsektion (Grund `--farbe-dunkel`, Höhe 88 px Desktop / 64 px Mobil), Links
  in `--farbe-dunkel-text-2`, aktiver Punkt und Wortmarke in `--farbe-dunkel-text`, Hover
  `--farbe-dunkel-text` mit 250 ms Farbwechsel. Kein Hintergrundwechsel nötig, weil die Leiste
  nie über hellen Sektionen liegt.
- Skip-Link „Zum Inhalt" als erstes fokussierbares Element, sichtbar bei Fokus.
- Mobil (< 900 px): drei Textelemente (helenhard-F12) — „Kontakt" links, Wortmarke mittig
  (22 px), „Menü" rechts. „Menü" ist ein `<button aria-expanded aria-controls>` und öffnet ein
  Vollbild-Overlay auf `--farbe-dunkel` mit den vier Punkten in DM Sans 28 px, Zeilenabstand
  1,5, darunter Telefonnummer und Mail als Klartext; Schließen über denselben Button
  („Schließen"), Escape und Fokus-Falle im Overlay; `nav`-Landmark. Kein Burger-Icon, kein
  Ausklappen unter der Leiste.
- Fußzeile (dunkel) wiederholt die vier Punkte plus Impressum und Datenschutz als Textlinks in
  `--farbe-dunkel-text-3` (5,81:1).

## 8. Bildkonzept

- Bildlage: alle 32 Dateien sind Querformat 3:2 (1920 × 1280, zwei Restaurant-Bilder
  1600 × 1067), Innenräume. Kein Muster im Brief verlangt Hochformat.
- Formate je Sektion:
  - Start-Hero: Ausschnitt **16:10** auf 896 px Breite (`aspect-ratio: 16/10`,
    `object-fit: cover`, `object-position: 50% 55%` für das Penthouse-Bild, damit die
    Arbeitsplatte und der Boden bleiben und die Deckenleuchten angeschnitten werden dürfen)
  - Projektbilder Startseite und `/projekte/`: **3:2** auf 960 px, unbeschnitten
  - Detail-Hero: **16:9** auf 1280 px (`object-position` je Motiv, Standard `50% 50%`)
  - Detail Bild 2: 3:2 auf 960 px · F7-Paar: links 560 px in 3:2, rechts 640 px als
    **4:3-Ausschnitt** (`aspect-ratio: 4/3`, cover) — die ungleiche Höhe entsteht durch den
    Ausschnitt, nicht durch ein Hochformat
  - Studio-Sektion (F6): 3:2 auf 45 % Container (≈ 576 px)
- Zuschnitt: `object-fit: cover` mit `object-position` wo nötig; Bilder ohne Rahmen, ohne
  Rundung, ohne Schatten, ohne Abdunklung (kein Text darauf).
- Auslieferung: WebP, `srcset` 960/1440/1920 mit `sizes`; Hero ≤ 250 KB bei 1792 px, übrige
  ≤ 200 KB bei 1920 px; **jedes `<img>` mit `width`/`height`**; Hero `fetchpriority="high"`
  ohne `loading="lazy"`, alle anderen `loading="lazy"` (Bedingung robmills-F10). Platzhalter
  `--farbe-dunkel-flaeche` bzw. `--farbe-flaeche` bis zum Laden.
- Anzahl je Seite: Startseite 6 (Hero, 4 Projekte, Studio) · `/projekte/` 8 · Detail 4 ·
  `/studio/` 3 (F6-Bild + F7-Paar) · Leistungen, Kontakt, Rechtstexte 0.
- **Aufmacher je Projekt** (Bild auf Startseite, in der Liste und als Detail-Hero — gewählt
  nach Ruhe, Raumwirkung und Palette; die `-01`-Dateien sind mehrfach ungeeignet, siehe 11):

  | Projekt | Aufmacher | Detail-Reihenfolge | Bemerkung |
  |---|---|---|---|
  | Altbauwohnung Harvestehude | harvestehude-03 | 03 · 04 · 02 · 01 | 01 zeigt eine Hochhaus-Skyline im Fenster (Dubai) — nur als viertes Bild, nie als Aufmacher |
  | Restaurant am Fleet | restaurant-fleet-02 | 02 · 03 · 04 · 01 | 01 ist unscharf und wirkt wie ein Diner |
  | Ferienhaus Kampen | kampen-03 | 03 · 04 · 01 · (02 = Duplikat von 01) | Blockbohlenwände in 01/02 lesen sich nicht als Sylt |
  | Zahnarztpraxis Eppendorf | praxis-eppendorf-03 | 03 · 04 · 02 · 01 | 01 ist ein Instrumenten-Detail ohne Raum |
  | Penthouse Prenzlauer Berg | penthouse-berlin-03 | 03 · 02 · 01 · 04 | 03 ist zugleich der Start-Hero |
  | Boutique-Hotel Speicherstadt | hotel-speicherstadt-03 | 03 · 02 · 01 · 04 | 04 zeigt eine Person auf der Badewanne — nur als letztes Bild, besser ersetzen |
  | Stadthaus Blankenese | blankenese-02 | 02 · 03 · 04 · 01 | 01 wirkt wie eine leere Mietwohnung |
  | Kanzlei HafenCity | kanzlei-hafencity-03 | 03 · 04 · 01 · (02 = Duplikat von 01) | 01/02 ist ein Detail mit kräftigem Blau, bricht die Palette |

- Startseite zeigt vier Projekte in dieser Reihenfolge: Harvestehude (privat), Restaurant am
  Fleet (Gastronomie), Boutique-Hotel Speicherstadt (Hotellerie), Stadthaus Blankenese
  (privat) — die drei Zielgruppen in der ersten Bildschirmfolge, Praxis und Kanzlei auf
  `/projekte/`. Studio-Sektion: kampen-03 (hellstes, ruhigstes Bild). `/studio/` F7-Paar:
  harvestehude-04 links, blankenese-03 rechts.
- Stockfoto-Suchbegriffe (nur Referenz, aus `inhalte.md`): elegant apartment interior living
  room natural light · restaurant interior warm wood design · scandinavian beach house
  interior · modern dental clinic interior design · penthouse interior minimalist kitchen ·
  boutique hotel room interior design · townhouse interior staircase design · law office
  interior modern wood — alle Querformat.
- **Hero-Bild: `penthouse-berlin-03.webp`** (Küche mit heller Eichenfront und weißen Wänden,
  Max Vakhtbovych, Pexels). Warum: das ruhigste Bild des Bestands — große ungestörte Flächen,
  keine Deko, keine Personen, kein Fenster mit fremder Stadt; Eiche und Off-White sind exakt
  die Palette der Seite, das Bild steht deshalb auf dem Kohlegrund wie eingelassen; es hat
  keine harte Bildkante, an der der leichte Zoom auffiele. Alt-Text: „Küche mit Einbaufronten
  aus heller Eiche und weißen Wänden, Penthouse Prenzlauer Berg". Auf 896 px in 16:10
  beschnitten, 2×-Variante 1792 px.
- Alt-Texte für alle Bilder: Raum, Material, Projektname — keine Fotografennamen, keine
  Ortsangaben, die ein reales Gebäude behaupten. Bildnachweis bleibt in `BILDER.md`.

## 9. Motion

- **Hero beim Laden (einmal):** Bild `opacity 0 → 1` und `transform: scale(1.05) → scale(1)`
  in 1600 ms, Kurve `cubic-bezier(0.22, 1, 0.36, 1)` (Ease-out), Verzögerung 200 ms.
  Hero-Satz `opacity 0 → 1`, `translateY(12px) → 0` in 900 ms, Verzögerung 500 ms. Kopfzeile
  ohne Animation. Danach steht alles still.
- **Wachsende Linie (robmills-F3):** 1 px breit, horizontal mittig, beginnt an der Unterkante
  des Hero-Satzes und wächst 8 rem in die helle Intro-Sektion hinein; `transform-origin: top`,
  `scaleY(0) → scaleY(1)` in 900 ms, gleiche Kurve, ausgelöst bei `scrollY > 40` (Klasse am
  `html`), einmal. Farbe: im dunklen Teil `--farbe-dunkel-text-3`, im hellen Teil
  `--farbe-text-3` (zwei gestapelte Elemente, kein Verlauf). Auf der Startseite nur; auf
  Unterseiten gibt es keine Linie.
- **Einblenden der Bilder (robmills-F10, die „ruhige Bewegung" der Vorgabe):** jedes Bild ab
  dem zweiten Bild der Seite `opacity 0 → 1` in 700 ms und `scale(1.03) → scale(1)` in 1200 ms,
  gleiche Kurve, ausgelöst per IntersectionObserver bei 15 % Sichtbarkeit
  (`rootMargin: 0px 0px -10% 0px`), einmal je Bild, danach Observer lösen. Das Bild liegt in
  einem Wrapper mit `overflow: hidden`, damit der Zoom nichts verschiebt. Der Ausgangszustand
  (`opacity: 0`) wird nur gesetzt, wenn JS läuft (Klasse `js` am `html`); ohne JS sind alle
  Bilder sofort sichtbar. Texte werden **nicht** eingeblendet — nur Bilder bewegen sich.
- **Hover:** Projektbild `scale(1.02)` in 600 ms innerhalb des Wrappers; Projekttitel bekommt
  eine 1-px-Unterstreichung. Beides Zusatz, keine Information hängt am Hover (Titel und Ort
  stehen immer sichtbar).
- **Links und Buttons:** `color`/`background-color` 250 ms linear; Fokusring 2 px in
  `--farbe-akzent` bzw. `--farbe-dunkel-akzent` mit 3 px Abstand, nie entfernt.
- **Vollbild-Menü:** `opacity 0 → 1` 250 ms; kein Slide.
- Alles unter `prefers-reduced-motion: reduce` abgeschaltet: keine Transitionen, keine
  Animationen, Bilder sofort sichtbar, Linie steht in voller Länge, Hover ohne Zoom.
- Kein Preloader, kein Autoplay-Video, kein Parallax (auch nicht auf Desktop), keine
  scrollgekoppelte Bewegung, kein Slider, keine Bewegung von Text außer dem Hero-Satz beim
  Laden.

## 10. Bewusst nicht übernommen

Muster aus den Referenzen, die zur Realität nicht passen, mit Grund. Der Prüfer prüft, dass
sie tatsächlich nicht verbaut sind.

**Slider und Karussells (Anti-Muster, dazu Wunsch des Nutzers „kein Slider"):**
- **pietboon-com-F4** eingerückter Hero-Slider — statisches eingerücktes Bild stattdessen (F11-Prinzip).
- **pietboon-com-F5** Abschnittstitel mit Linie **und Karussell** — das Karussell fällt, und ohne Karussell bleibt nur eine Linie, die die Seite nicht braucht; die Sektionstitel stehen frei.
- **robmills-com-au-F4** horizontaler Projekt-Slider mit Hochformat-Kacheln — Slider, und alle Fotos sind Querformat.
- **robmills-com-au-F9** Projekt-Hero als Slider zwischen Projekten — Urteil `nicht`; „Nächstes Projekt" ist ein Textlink am Seitenende.

**Video und Vollbild-Hero:**
- **robmills-com-au-F1** fensterhohes Hero-Video mit zentrierter Bildmarke — kein Clip vorhanden; als Standbild wäre es ein randloses Vollbild und damit das Nordkant-Prinzip. Bewusst anders: dunkle Fläche mit eingerücktem Bild.
- **helenhard-no-F2** textfreies Hero-Video über die Nutzbreite — gleicher Grund.
- **robmills-com-au-F7** Medienmodul mit vier Autoplay-Videos — Urteil `nicht`.
- **robmills-com-au-F2** Navigation ohne Leiste über dem Medium — Text auf Bild ist tabu; die Navigation liegt auf der dunklen Fläche, nie auf dem Foto.

**Raster und Kacheln, die gegen „einzelne, groß gestellte Bilder" laufen:**
- **pietboon-com-F8** Wechsel 3 Kacheln / 1 Featured-Reihe — acht Projekte wären ein Vielfaches von 4, aber ein Dreier-Raster ist das Gegenteil des Wow-Faktors; Infinite Scroll ohnehin nicht.
- **pietboon-com-F9** Kachel mit grauem Textfuß — Flächen unter jedem Bild statt Luft.
- **robmills-com-au-F8** vier fensterhohe Bildspalten — braucht Hochformat-Fotos und vier gleichwertige Kategorien; Bestand ist Querformat, Kategorien sind drei.
- **helenhard-no-F8** Typologie-Filter — erst ab ~12 Projekten; acht Projekte in drei Feldern ergäben Filter mit zwei Treffern.
- **wolveridge-com-au-F3** Dreier-Raster mit breiten Gassen — ab 9 Projekten, und Raster.

**Projektseite:**
- **pietboon-com-F12** Galerie aus Bildpaaren mit wechselnden Breiten — verlangt 8–12 Fotos mit Hochformaten und Details; vier Querformate ergeben keinen Versatzrhythmus. Reduzierte Form ist genau das, was verbaut wird (F11 + F7), unter deren IDs.
- **wolveridge-com-au-F9** Textspalte links, Bildspalte rechts — nur für Projekte mit 6+ Fotos; big-dk-F2 übernimmt die Randspalte.
- **robmills-com-au-F11** kursives Zitat des Architekten als Einstieg — braucht ein echtes Zitat und 6 Fotos; Zitate werden für ein fiktives Büro nicht erfunden.
- **helenhard-no-F9** zentrierte Metadaten-Tabelle über die volle Breite — der Nutzer will die Metadaten als Randspalte neben dem Bild, nicht als Block zwischen den Bildern.
- **helenhard-no-F10** Bildrhythmus Foto + Skizze — es gibt keine Pläne oder Skizzen (Stock).

**Statement und Über-uns:**
- **robmills-com-au-F6** Statement mit Schwarzweiß-Porträt — keine Portraits vorhanden; pietboon-F6 mit Projektfoto stattdessen.

**Farbe:**
- **robmills-com-au-F5** Weiß auf Taupe — 2,1:1, Urteil `nicht`. Die dunklen Sektionen hier laufen auf `#1F1D1A` mit 14,9:1.
- **helenhard-no-F5** Off-White, Beige-Buttons, Graubraun-Footer — der Footer hier ist Kohle, nicht Graubraun, und der Button-Ton ist der Holz-Akzent; die Off-White-Idee steckt schon in pietboon-F2.

**Navigation und Kopfzeile:**
- **pietboon-com-F3** zweizeiliger Kopf mit Login, Sprachwahl, Broschüren-Button — Urteil `nicht`.
- **pietboon-com-F14** Mobile-Kopfzeile am unteren Rand — nicht nötig, weil das Vollbild-Menü über einen Textlink oben erreichbar ist und die Seite keine Kontaktleiste unten hat.
- **wolveridge-com-au-F1 / F10** Dreiteilung mit Standortstapel, aufklappende Kopfzeile — ein Standort, vier Punkte, helenhard-F1/F12 reichen.
- **helenhard-no-F6** Newsliste — keine Redaktion.

**Technik und Rechtliches:**
- **pietboon-com-F10** Filter, Suche, Google-Maps-Karte — Urteil `nicht`, kein Fremd-Request; auch auf `/kontakt/` keine Karte.
- **pietboon-com-F13** fixierte HubSpot-Kontaktleiste — Urteil `nicht`.
- **robmills-com-au-F12** unsichtbare Keyword-H1 am Seitenende — Urteil `nicht`; jede Seite hat genau eine sichtbare H1 (Startseite: der Hero-Satz).
- **robmills-com-au-F13** Fußzeile ohne Rechtstexte — Impressum, Datenschutz, Anschrift stehen in der Fußzeile; Breadcrumb wird nicht gebraucht (Seitentiefe 2).
- **robmills-com-au-F14** Tracking-Stack — nichts davon; kein Analytics auf der Referenzseite.
- **helenhard-no-F3** Handskizzen-Ebene — Eigenschöpfung der Referenz, Urteil `nicht`.
- **helenhard-no-F11** Lazy Loading ohne Bildmaße — Urteil `nicht`; alle Bilder mit `width`/`height`.
- Kein Cookie-Banner nötig, weil nichts Einwilligungspflichtiges geladen wird (Schriften self-hosted, keine Karte, kein Tracking).

## 11. Offene Fragen an den Nutzer

1. **Zwei Bild-Duplikate im Bestand.** `kampen-01.webp` und `kampen-02.webp` sind dieselbe
   Pexels-Datei (ID 7061396), ebenso `kanzlei-hafencity-01.webp` und `-02.webp` (ID 9419044).
   Damit haben Ferienhaus Kampen und Kanzlei HafenCity faktisch nur drei Bilder. Je eines
   ersetzen (Vorschlag: Kampen ein helles Schlaf- oder Esszimmer mit Holz und Textil, Kanzlei
   ein Empfang oder Flur mit Holz und Glas), oder die Detailseiten dieser beiden Projekte mit
   drei Bildern bauen (Bild 2 groß, Bild 3 allein statt als Paar)?
2. **Vier Bilder passen nicht zur Zielgruppe und sollten ersetzt werden:**
   `praxis-eppendorf-01` (Instrumenten-Detail ohne Raum), `restaurant-fleet-01` (unscharf,
   wirkt wie ein Diner), `blankenese-01` (leere Mietwohnung mit Fliesen, liest sich nicht als
   Stadthaus), `hotel-speicherstadt-04` (Person auf der Badewanne — kein Interieurbild).
   Grenzfälle, die bleiben können, aber nicht als Aufmacher taugen: `kampen-01`
   (Blockbohlenwände + Fernseher, eher Ferienpark als Sylt), `kanzlei-hafencity-01` (kräftiges
   Blau bricht die Palette), `hotel-speicherstadt-01` (Tapetenmuster wirkt älter als 2022),
   `harvestehude-01` (Hochhaus-Skyline im Fenster, erkennbar nicht Hamburg). Der Brief arbeitet
   mit dem Bestand und legt die schwachen Bilder ans Ende der Reihenfolge — soll ich vor dem Bau
   Ersatz laden lassen?
3. **Hero-Satz.** Vorgesehen ist der erste Satz der Selbstbeschreibung als H1 und einzige
   Textzeile des Heros: „Räume, die ruhig wirken und lange gefallen." Einverstanden, oder soll
   dort etwas Ortsbezogenes stehen („Innenarchitektur in Hamburg")? Für SEO wäre der Ort im
   Hero-Satz besser; für die Ruhe des Bildes der kurze Satz.
4. **DM Sans und die dritte Referenzseite.** Die parallel entstehende dritte Seite ist als
   „Grotesk, dichtes Raster" beschrieben. Nimmt sie DM Sans, wechsle ich hier den Textschnitt
   auf Source Sans 3 (gleiche Rolle, gleiche Größen) — Cormorant bleibt in jedem Fall die
   prägende Schrift. Bitte kurz Bescheid geben, welche Grotesk die dritte Seite nutzt.
5. **Metadaten der Randspalte.** `inhalte.md` liefert je Projekt nur Ort und Jahr. Die
   Randspalte (big-dk-F2) sollte vier Zeilen haben: Ort, Fertigstellung, Leistung (aus dem
   Leistungsfeld ableitbar), Fläche. Dürfen fiktive, plausible Flächen (z. B. „Wohnfläche
   ca. 140 m²") ergänzt werden, oder bleibt die Spalte bei drei Zeilen?
6. **Projekttexte.** Je Projekt sind 40–80 Wörter für die Detailseite vorgesehen; in
   `inhalte.md` steht kein Projekttext. Der Builder muss sie schreiben (sachlich, ohne
   Superlative, Material und Aufgabe benennen). In Ordnung, oder lieferst du sie?
7. **Kein Kontaktformular, keine Karte.** Kontakt läuft über Telefon und `mailto:`. Falls die
   Referenz ein Formular zeigen soll, braucht es ein Backend (oder einen statischen
   Dienst) und einen Datenschutz-Absatz — dann bitte sagen.
8. **URL `/studio/` statt `/buero/`.** Abweichung von der Vorlage, weil das Büro „Studio"
   heißt. Falls das Skeleton `/buero/` fest verdrahtet, bleibt `/buero/` mit sichtbarem Titel
   „Studio".

---

**Kombinierte Referenzen:** pietboon-com (eingerücktes Bild statt Vollbild, Grau-Stufen-Palette,
Intro-Block, Kasten mit überlappendem Bild, versetztes Bildpaar), robmills-com-au (wachsende
Linie, Lazy-Fade als einzige Bewegung), helenhard-no (leichte Serife mit Kursiv, geteilte
Navigation mit Text-Wortmarke, Projektbild mit Titel darüber, Standort-Footer, mobile
Textkopfzeile) — ergänzt um drei Katalog-Einzelfeatures aus big-dk (Ort-Versalien,
Metadaten-Randspalte, gemeinsame Kante). Genau diese passen, weil das Studio acht gleichformatige
Profi-Querformate, einen Absatz Text, keine Portraits, keine Pläne und keinen Videoclip hat:
pietboon liefert die Komposition für wenig Material auf Flächen, robmills die ruhige Bewegung
ohne Bildvoraussetzung, helenhard die typografische Haltung — und keines der drei die Seite als
Ganzes, weil deren tragende Muster (Slider, Video, Taupe-Weiß, Skizzenebene) hier alle entfallen.
