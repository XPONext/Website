# Prüfbericht Nordkant Architekten — 2026-09-07

**Ergebnis:** abgenommen (0 Blocker, 12 Warnungen)

Geprüft gegen `checklisten/qualitaet.md`, `_doku/design-brief.md` (Stand 2026-09-07) und die
Referenz-Screenshots helenhard-no, pietboon-com, big-dk. Objektiver Teil: `tools/website_qualitaet`
(14 Seiten, 17 Prüfungen ok, 0 Blocker, 1 Warnung) und `tools/website_screenshot` lokal
(42 Screenshots, alle gesichtet). Zusätzlich ein Playwright-Lauf für Fokus, Mobile-Menü,
Tap-Ziele, `prefers-reduced-motion` und den Hero bei 1920 px.

## Blocker

Keine.

## Warnungen

1. **7. Brief-Treue, Nachbildung (Grenzfall, kein Blocker)** — Die Startseite folgt in der oberen Hälfte der Abfolge von helenhard.no Punkt für Punkt: geteilte Serifen-Navigation mit zentrierter Wortmarke → großes Bild → zentrierter Intro-Absatz → 2×2-Kacheln mit zentriertem Titel über dem Bild und kursivem Satz darunter → zentrierter „Alle Projekte"-Link (`01_start_desktop_full.jpg` neben `helenhard-no/01_start_desktop_full.jpg`). Kein Blocker, weil die Seite als Ganzes klar abweicht (Kopfzeile auf Fläche, randloser Hero, Bildzeile, Chevron-Liste, Statement-Kasten, Kontaktkasten, heller Footer, Projektseiten nach Piet Boon) und der Brief genau diese Kombination vorgibt. Aber: helenhard-F1 + F7 zusammen sind der Punkt, an dem jemand, der helenhard.no kennt, die Vorlage erkennt. Vorschlag für den Nutzer, keine Vorgabe: Kacheltitel linksbündig an die Bildkante (big-dk-F3, im Brief für die Projektseite ohnehin gewählt) würde den Abstand deutlich vergrößern.
2. **5. Rechtliches, Bildnachweis (vor dem Livegang bereinigen)** — Es gibt zwei Nachweisdateien, die sich widersprechen. `assets/bilder/projekte/BILDER.md` belegt alle 20 Quellbilder mit Fotograf und Pexels-URL (rekonstruiert per Bildvergleich, r = 1,00); drei Stichproben per Aufruf der Pexels-Seiten stimmen (7598374 Vakhtbovych, 14953387 van der Wolf, 4353718 ArtHouse Studio). `assets/bilder/BILDER.md` — die Datei, die die Checkliste nennt — führt dagegen 17 von 20 Zeilen mit „nachzutragen" und einen „Offenen Punkt", der sagt, die Rekonstruktion sei nicht eindeutig gewesen. Zudem stimmt dort „gartenhaus-03: 1440 px Export" nicht (Datei ist 1280 × 855). Ein Nachweis ist vorhanden, deshalb kein Blocker; die veraltete Tabelle und der Hinweis müssen aber raus, sonst liest der nächste Prüfer „Quelle fehlt".
3. **5. Rechtliches, erkennbares reales Gebäude (Grenzfall)** — `kreuzviertel-02.webp` (Hero der Projektseite und Kachel auf `/projekte/`) zeigt lesbar die Hausnummer **536–542** an der Fassade und ein rosa Schild im Fenster (`06_projekte-wohnhaus-kreuzviertel_desktop_hero.jpg`). Das Gebäude ist damit über die Adresse identifizierbar und wird als „Neubau 2022, sieben Meter breit, Kreuzviertel Münster" ausgegeben — der Nummernbereich 536–542 widerspricht zudem „ein Stadthaus auf sieben Metern". Kein bekanntes Bauwerk, deshalb Warnung statt Blocker. Zuschnitt ohne Nummernschild oder Bildtausch (`narrow brick townhouse street facade`, wie im Brief 11.3 vorgeschlagen).
4. **1. Performance, Hero-Auflösung (Brief 8 verlangt 1920/1440/960)** — Das `srcset` des Heros endet bei 1440 px (`hero.webp` 1440 × 961, 244 KB). Bei 1920 × 1080 wählt der Browser `hero.webp` und skaliert auf 1920 × 936 hoch (Faktor 1,33, gemessen im Playwright-Lauf). Auf großen Monitoren ist der einzige Wow-Moment der Seite damit weicher als nötig. Eine 1920er-Stufe unter 250 KB fehlt.
5. **1. Performance, `og.jpg` nicht WebP** — Meldung aus `website_qualitaet`. Begründet stehen lassen: Open-Graph-Bilder müssen für Facebook/LinkedIn/WhatsApp JPG oder PNG sein, WebP wird dort nicht überall gerendert. Das Bild wird beim Seitenaufruf nicht geladen.
6. **3. Barrierefreiheit, Tap-Ziele unter 44 px (mobil, 390 px)** — Gemessen: Chevron-Links „Neubau › Umbau › Anbau › Bauberatung" 39 px hoch; Bildzeile „Haus im Wald · Nottuln · 2021" 19 px; „Alle sechs Projekte ›" und „Mehr über das Büro ›" 21 px; Telefon und Mail im Kontaktkasten 21 px (Startseite und `/kontakt/`); Footer-Links 30 px. Navigation (56 px), „Menü"-Button (50 × 44 px) und Kontakt-Button (50 px) sind in Ordnung. Am schwersten wiegen Telefon und Mail: das ist laut Brief der eigentliche Kontaktweg. `padding-block` auf diesen Links reicht, das Layout bleibt.
7. **3. Barrierefreiheit, Kontrast Nav-Punkte auf Fläche** — Inaktive Navigationspunkte in `--farbe-text-3` auf `--farbe-flaeche` nachgerechnet: **4,58:1** (Brief: 4,58). Erfüllt AA für Fließtext, aber ohne Reserve. Keine Änderung nötig, nur der Hinweis: wird die Kopfzeile je dunkler (Flächenton ändern), kippt der Wert.
8. **2. Datenschutz / nicht in Checkliste, verwaiste Formular-Reste** — `formular.php` (mit fiktiver Zieladresse) und `/danke/` liegen im Site-Ordner, obwohl es kein Formular gibt; die Datenschutzerklärung sagt korrekt „ohne Kontaktformular". `/danke/` ist von keiner Seite verlinkt, hat `noindex`, steht in `robots.txt` auf Disallow und nicht in der Sitemap — technisch sauber, aber ein PHP-Skript mit `mail()`-Aufruf auf einem Live-Server, das niemand braucht, ist ein unnötiges Ziel. Beide Dateien löschen, oder den Verbleib in den Bau-Notizen begründen.
9. **Nicht in Checkliste, Glaubwürdigkeit der Zweit- und Drittbilder** — Vier Fotos passen nicht zur Ortsbehauptung und fallen einem Bauherrn aus dem Münsterland auf: `haus-am-deich-02` zeigt eine Reihe alpiner Chalets mit Stromleitungen und Hangterrassen (`03_…_desktop_full.jpg`, rechtes Bild), `haus-im-wald-03` hat ein Gebirge im Hintergrund (`08_…_desktop_full.jpg`), `gartenhaus-02` ist ein freistehendes Gewächshaus auf Terrakotta (`05_…_desktop_full.jpg`), `kreuzviertel-03` ein mehrgeschossiges Mietshaus von unten (`06_…_desktop_full.jpg`). Die Alt-Texte sind ehrlich (kein Ortsbezug), der Demo-Hinweis deckt es rechtlich ab — für eine Referenz, die Kunden überzeugen soll, sind es aber die vier schwächsten Bilder der Seite.
10. **Nicht in Checkliste, Kachelgröße über Brief-Vorgabe** — Brief 8: Kacheln 1222 px unter 200 KB. `kacheln/gartenhaus.webp` hat 239 KB (die übrigen fünf 39–197 KB). Checklisten-Grenze (300 KB) eingehalten, deshalb nur Hinweis.
11. **Nicht in Checkliste, `assets/fonts/LICENSES.md` veraltet** — Die Tabelle listet sieben Familien (Inter, Source Sans 3, DM Sans, Instrument Serif, IBM Plex Mono, Cormorant Garamond), von denen nur Fraunces im Ordner liegt. Der Einleitungssatz sagt das zwar, die Tabelle nicht. Sechs Zeilen streichen.
12. **Nicht in Checkliste, mobiler erster Bildschirm ohne Text** — Bei 390 × 844 besteht der erste Bildschirm exakt aus Kopfzeile (64 px) + Hero (732 px) + Bildzeile (48 px); die H1 beginnt erst nach dem Scrollen (`mobil_start_viewport`, Playwright-Lauf). Das ist die Brief-Vorgabe (Abschnitt 5, offene Frage 11.5 „Entscheidung an der Hero-Probe"). Checkliste 6 „Hero-Höhe unter 100 vh" ist mit 732 px erfüllt. Nur festgehalten, damit die Entscheidung bewusst bleibt: ein Bauherr auf dem Handy sieht zuerst nur ein Haus und eine Versalzeile, keinen Satz, was das Büro tut.

## Messwerte

Lokal (http.server, kein Netz, kein Gzip). LCP-Werte sind deshalb nur als Reihenfolge belastbar,
nicht als Absolutwert für den Server. Der CSS-Posten des Tools (107 KB je Seite) passt nicht zur
Datei (`basis.css` 24 KB) — Tool-Artefakt der Resource-Timing-Zählung, die Gesamtwerte sind
entsprechend eher zu hoch als zu niedrig.

| Seite | Transfer | LCP | Fremd-Domains | Mobil-Querscroll |
|---|---|---|---|---|
| / | 1,27 MB (Bilder 1,08 MB) | 92 ms | keine | nein |
| /projekte/ | 1,09 MB | 40 ms | keine | nein |
| /projekte/haus-am-deich/ | 0,97 MB | 36 ms | keine | nein |
| /projekte/hofstelle-havixbeck/ | 0,61 MB | 36 ms | keine | nein |
| /projekte/anbau-hiltrup/ | 1,05 MB | 44 ms | keine | nein |
| /projekte/wohnhaus-kreuzviertel/ | 0,88 MB | 44 ms | keine | nein |
| /projekte/aufstockung-greven/ | 0,67 MB | 32 ms | keine | nein |
| /projekte/haus-im-wald/ | 1,01 MB | 44 ms | keine | nein |
| /buero/ | 0,33 MB | 48 ms | keine | nein |
| /leistungen/ | 0,52 MB | 24 ms | keine | nein |
| /kontakt/ | 0,18 MB | 20 ms | keine | nein |
| /impressum/ | 0,18 MB | 20 ms | keine | nein |
| /datenschutz/ | 0,18 MB | 24 ms | keine | nein |
| /danke/ | 0,18 MB | 20 ms | keine | nein |

Weitere Werte: Startseite 10 Requests, davon 2 Schriftdateien (67 KB + 82 KB woff2, Fraunces normal
und kursiv, erste per `preload`), 1 CSS, 1 JS (1,6 KB, `defer`), 6 Bilder. Hero `hero.webp` 244 KB
(≤ 250 KB), `fetchpriority="high"`, kein `loading="lazy"`; alle 33 übrigen `<img>` ≤ 300 KB, ≤ 1920 px,
WebP, mit `width`/`height`; Bilder unterhalb des ersten Bildschirms `loading="lazy"`. Kein Cookie,
kein localStorage, keine Google Fonts. `document.fonts`: nur Fraunces normal/italic geladen;
`font-weight` im DOM ausschließlich 300 und 400.

## Checkliste, Sichtprüfung der [A]-Punkte

- **1. Render-blockendes JS:** nur ein Inline-Einzeiler im `<head>` (`classList.add('js')`), `basis.js` mit `defer` am Body-Ende. Kein Preloader, kein Intro-Overlay — Hero-Screenshot zeigt nach 500 ms das fertige Bild.
- **2. Formular/Cookie:** kein Formular auf `/kontakt/`, Telefon und Mail als Klartext-Links; `document.cookie` leer, kein Storage. Siehe Warnung 8 zu den Resten.
- **3. Fokus:** Outline 3 px `#8B5A3C`, Offset 3 px — gemessen auf Nav-Link „Projekte" (Kopfzeile, Fläche), auf dem Ziegel-Button „Projekt besprechen" (auf Grund) und auf dem Telefon-Link im Kontaktkasten (auf Fläche, 4,65:1). Skip-Link „Zum Inhalt springen" erscheint bei erstem Tab oben links als dunkler Balken.
- **3. Menü-Button:** `aria-expanded` false → true beim Klick, `aria-controls="hauptnavigation"`, Beschriftung wechselt „Menü" → „Schließen", Liste klappt unter der Kopfzeile aus (kein Overlay), Escape schließt und setzt den Fokus auf den Button zurück, Klick auf „Projekte" navigiert und die Liste ist auf der Zielseite geschlossen.
- **3. Kontrast:** alle Brief-Werte nachgerechnet (WCAG-Formel): Text 14,31 / 12,75; Text-2 6,57 / 5,85; Text-3 5,14 / 4,58; Akzent 5,22 / 4,65; Invers auf Akzent 5,22 — jeweils auf Grund / Fläche. Stimmt mit dem Brief überein. Auf dem Button steht nur `--farbe-invers`, nie die Textfarbe (2,74:1 wäre durchgefallen).
- **3. Text auf Bild:** nirgends. Hero, Kacheln, Projekt-Hero, Bildpaare, Statement-Bild sind alle textfrei; Titel stehen daneben oder darunter.
- **3. `prefers-reduced-motion`:** unter Emulation `transition-duration: 0,00001 s`, `scroll-behavior: auto`, Hover auf der Kachel ergibt `transform: none`. Kein Parallax, keine Scroll-Einblendung im CSS.
- **3. Tap-Ziele:** siehe Warnung 6.
- **3. Hover:** Kacheltitel und kursiver Satz stehen dauerhaft, der Hover skaliert nur das Bild um 2 %.
- **4. URLs:** alle 14 Seiten als Ordner mit `index.html`, keine `.html` in Links. Titel 32–56 Zeichen, Beschreibungen 55–158 Zeichen, alle 14 unterschiedlich. `canonical`, `og:*`, `noindex, follow` auf jeder Seite. Sitemap: 11 Seiten, ohne danke/impressum/datenschutz, mit Präfix `/referenzen/nordkant-architekten/`. `robots.txt` erlaubt GPTBot, ClaudeBot, PerplexityBot.
- **4. Ortsbezug Startseite:** „Münsterland", „Münster", „am Hafen in Münster", „Telgte, Havixbeck, Hiltrup und Nottuln" im sichtbaren Text; JSON-LD `ArchitectOffice` mit Adresse, Telefon, `areaServed` Münster/Münsterland.
- **5. Impressum:** § 5 DDG, Partnerschaftsregister (als fiktiv markiert), Kammer AKNW mit Adresse, Berufsbezeichnung mit Verleihungsstaat, Berufsordnung, USt-IdNr. (Platzhalter, als solcher benannt), Berufshaftpflicht mit Geltungsbereich, Streitbeilegung, Bildnachweis-Absatz, Demo-Absatz „Büro, Personen und Projekte fiktiv".
- **5. Datenschutz:** passt zur Technik — keine Cookies, keine Analyse, kein Formular, keine Fremdinhalte; Server-Logs, E-Mail/Telefon, Betroffenenrechte, Aufsichtsbehörde NRW. Kein Absatz über Dinge, die es nicht gibt.
- **5. Referenz-Pflichten:** `noindex` auf allen 14 Seiten (Tool), Fußzeile „Demo-Website von XPONext. Büro und Projekte sind fiktiv, die Fotografie ist Stockmaterial." auf jeder Seite gesichtet (alle `*_desktop_full.jpg`), „fiktiv" im Impressum. Keine Personen auf irgendeinem Bild; Team ist eine Namensliste ohne Portraits (`09_buero_desktop_full.jpg`). Reale Gebäude: alle Fotos sind Stock ohne bekanntes Bauwerk; Grenzfall Hausnummer siehe Warnung 3.
- **6. Mobil:** kein Querscroll auf allen 14 Seiten (Tool, `scrollWidth` 390). Alle 14 `*_mobile_full.jpg` gesichtet: nichts abgeschnitten, nichts überlappt; Statement-Kasten und Bild stapeln mit 2 rem Überlappung sauber, Metadatenblock hält Label links / Wert rechts, Team-Liste bricht bei 390 px auf zwei Zeilen um, Bildpaare stehen untereinander ohne Versatz, Footer dreispaltig → einspaltig. Hero: Haus, Rasen und Baumkronen im Hochformat-Ausschnitt (`object-position: 66 % 50 %`), Bildzeile darunter sichtbar. Burger ist Textlink „Menü", Liste schließt nach Auswahl.

## Brief-Treue

| Feature-ID | umgesetzt | Beleg (Screenshot) |
|---|---|---|
| helenhard-no-F2 Hero textfrei, erste Bildschirmhöhe, stehendes `<img>` | ja — Kopf 88 + Hero 756 + Bildzeile 56 = 900 px bei 1440 × 900, randlos, kein Text, kein Video | `01_start_desktop_hero.jpg`, `mobil_start_viewport` (64 + 732 + 48 = 844) |
| big-dk-F4 Ort in Versalien als Unterzeile | ja — „HAUS IM WALD · NOTTULN · 2021" unter dem Hero, „TELGTE · 2024" im Projektkopf, „HAVIXBECK · 2023" unter „Nächstes Projekt" | `01_start_desktop_hero.jpg`, `03_projekte-haus-am-deich_desktop_full.jpg` |
| helenhard-no-F1 geteilte Navigation, Wortmarke zentriert | ja — Projekte · Leistungen — Nordkant Architekten — Büro · Kontakt, kein Sticky (`position: relative`), kein Button in der Leiste | alle `*_desktop_hero.jpg` |
| helenhard-no-F4 eine Serife in Leichtgewicht, Kursiv als einzige Auszeichnung | ja — nur Fraunces geladen, H1/H2 in 300, Kachelsätze und Untertitel kursiv | `01_start_desktop_full.jpg`, `document.fonts` |
| big-dk-F1 Hierarchie ohne Bold | ja — computed `font-weight` nur 300/400, Labels 13 px Versalien grau | `03_projekte-haus-am-deich_desktop_full.jpg` (Metadaten-Labels) |
| helenhard-no-F5 Off-White, kein Reinweiß/Reinschwarz | ja — Grund `#F5F3EE`, Text `#24221F`; Footer hell (bewusste Abweichung laut Brief) | `01_start_desktop_full.jpg` |
| pietboon-com-F2 zwei Flächenstufen, Akzent nur auf Schaltflächen | ja — Kopfzeile, Statement-Kasten, Kontaktkasten, Footer auf `#EAE6DE`; Ziegel gefüllt nur auf „Projekt besprechen"; Chevrons/Unterstreichungen in Akzent als Text, wie Brief 4 erlaubt | `01_start_desktop_full.jpg`, `11_kontakt_desktop_full.jpg` |
| pietboon-com-F15 zentrierter Intro-Block mit Chevron-Linkliste | ja — H1 + Absatz zentriert, max. 720 px, darunter Neubau › Umbau › Anbau › Bauberatung mit Ankern nach `/leistungen/#…` | `01_start_desktop_full.jpg`, `mobil_start_2` |
| helenhard-no-F7 Projektkachel, Titel oben, kursiver Satz unten | ja — 4 Kacheln Startseite, 6 auf `/projekte/`, 3:2, zwei Spalten, kein Hover-Overlay | `01_start_desktop_full.jpg`, `02_projekte_desktop_full.jpg` |
| pietboon-com-F6 versetzter Farbkasten, Bild überlappt | ja — Kasten von der Fensterkante bis über die Spaltengrenze, 4:5-Bild 4 rem in den Kasten gezogen; mobil gestapelt mit Überlappung | `01_start_desktop_full.jpg`, `09_buero_desktop_hero.jpg`, `09_buero_mobile_full.jpg` |
| pietboon-com-F11 Projektkopf 16:9 eingerückt, Text darunter | ja — Bild im 1280-px-Container, darunter Grid 5/7 mit gemeinsamer linker Kante | `03_projekte-haus-am-deich_desktop_hero.jpg` und `_full.jpg` |
| helenhard-no-F9 Metadatenblock Variante B | ja — fünf Zeilen (Ort, Fertigstellung, Leistung, Leistungsphasen, Wohnfläche), Label links Versalien, Wert rechts, Hairline je Zeile, auf allen sechs Projektseiten | `03`–`08 *_desktop_full.jpg` |
| pietboon-com-F7 zwei Fotos, ungleiche Breite, versetzter Beginn | ja — 7/5, rechts 6 rem tiefer; auf allen Projektseiten und `/leistungen/`; mobil untereinander | `03_projekte-haus-am-deich_desktop_full.jpg`, `10_leistungen_desktop_full.jpg` |
| helenhard-no-F13 Footer-Standortblock, Ort kursiv | ja — „Münster" kursiv, Adresse, Telefon, Mail; eine Standortspalte | alle `*_desktop_full.jpg` |
| helenhard-no-F12 Mobile-Kopfzeile aus Text | ja — Wortmarke 20 px links, `button` „Menü"/„Schließen" rechts mit `aria-expanded`/`aria-controls`, Liste 21 px / 56 px Zeilen | `01_start_mobile_full.jpg`, `mobil_menu_offen` (Playwright-Lauf) |

**Wow-Faktor:** auf `01_start_desktop_hero.jpg` erkennbar — das Foto trägt den ersten Bildschirm
vollständig, ohne Text, ohne Overlay; die Kopfzeile sitzt als schmale Fläche darüber. Auf Mobil
(`mobil_start_viewport`) ebenso.

**Abschnitt 10 „bewusst nicht":** nichts davon verbaut. Kein Video (`anzahl_videos: 0`), keine
Skizzenebene, keine Newsliste, kein Typologie-Filter, kein Preloader, kein Slider/Karussell, keine
Karte, kein Kontaktformular, kein Text/Claim/Button auf dem Hero, keine Team-Portraits, kein Sticky,
keine dunkle Sektion (Footer auf `#EAE6DE`), kein Kachelfuß nach pietboon-F9, keine Projektsignets,
H1 44 px statt 18 px, keine Sans.

**Abweichungen vom Brief (keine Feature-IDs):** Hero-`srcset` ohne 1920er-Stufe (Warnung 4);
`kacheln/gartenhaus.webp` über 200 KB (Warnung 10). Offene Fragen 11.1 (Wohnfläche: fiktive
Werte übernommen), 11.2 (sechs kursive Sätze vorhanden), 11.3/11.4 (Kachelbilder Kreuzviertel →
`kreuzviertel-02`, Hofstelle → `hofstelle-03`), 11.6 („Projekt besprechen") sind entschieden
umgesetzt; 11.5 siehe Warnung 12.

## Was gut ist

1. **Der erste Bildschirm.** Kopfzeile auf Fläche, randloses Foto, eine Versalzeile — exakt auf 900 px bzw. 844 px gerechnet, LCP 92 ms lokal, Hero 244 KB. Das ist der Wow-Faktor aus dem Brief, und er funktioniert auf Desktop und Mobil gleichermaßen. Nicht anfassen; nur die 1920er-Stufe ergänzen.
2. **Die Projektseite.** 16:9-Bild im Container, darunter Titel, kursiver Satz, Metadatenblock mit fünf Zeilen und rechts 60–73 Wörter Text mit dem Button — alles an einer linken Kante, dann das versetzte Bildpaar und „Nächstes Projekt" mit Ort in Versalien. Sechsmal identisch gebaut, mobil ohne Verlust. Das ist die reifste Seite des Auftritts.
3. **Das Handwerk darunter.** Fokusring auf jedem Untergrund, Menü mit Escape und Fokusrückgabe, `reduced-motion` wirklich abgeschaltet, keine Fremd-Requests, kein Cookie, zwei Schriftdateien, Kontraste nachgerechnet und stimmig, Impressum und Datenschutz passen zur Technik. Hier ist nichts zu reparieren.

## Gesichtete Screenshots

Aus `_doku/screenshots/` (Lauf `pruefung`, 2026-09-07, 1440 × 900 Hero, 1440 Full, 390 × 844 Full):

- 01_start_desktop_hero.jpg · 01_start_desktop_full.jpg · 01_start_mobile_full.jpg
- 02_projekte_desktop_hero.jpg · 02_projekte_desktop_full.jpg · 02_projekte_mobile_full.jpg
- 03_projekte-haus-am-deich_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 04_projekte-hofstelle-havixbeck_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 05_projekte-anbau-hiltrup_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 06_projekte-wohnhaus-kreuzviertel_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 07_projekte-aufstockung-greven_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 08_projekte-haus-im-wald_desktop_hero.jpg · _desktop_full.jpg · _mobile_full.jpg
- 09_buero_desktop_hero.jpg · 09_buero_desktop_full.jpg · 09_buero_mobile_full.jpg
- 10_leistungen_desktop_hero.jpg · 10_leistungen_desktop_full.jpg · 10_leistungen_mobile_full.jpg
- 11_kontakt_desktop_hero.jpg · 11_kontakt_desktop_full.jpg · 11_kontakt_mobile_full.jpg
- 12_impressum_desktop_hero.jpg · 12_impressum_desktop_full.jpg · 12_impressum_mobile_full.jpg
- 13_datenschutz_desktop_hero.jpg · 13_datenschutz_desktop_full.jpg · 13_datenschutz_mobile_full.jpg
- 14_danke_desktop_hero.jpg · 14_danke_desktop_full.jpg · 14_danke_mobile_full.jpg

Zusätzlich aus dem Playwright-Lauf (Scratchpad, nicht im Site-Ordner): Mobile-Viewport Startseite
(390 × 844), Mobile-Menü geöffnet, Fokus auf Nav-Link, Fokus auf Kontaktkasten-Link, Mobile-Viewport
Projektseite, Mobile-Viewport Kontakt. Referenzen zum Vergleich: helenhard-no, pietboon-com, big-dk
je `01_start_desktop_hero.jpg` und `01_start_desktop_full.jpg`.
