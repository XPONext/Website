# Design-Brief: xponext.de, Relaunch Oktober 2026

| | |
|---|---|
| **Projektart** | eigene Website von XPONext (weder Kunden- noch Referenzprojekt) |
| **Realität** | Agentur mit zwei Gründern in Bonn, zwei Angebotsfamilien (Sichtbarkeit: Website, SEO, GEO, Google Ads; Zeit: KI-Automatisierung), fünf echte Kunden in Architektur, Innenausbau und Touristik, noch keine freigegebenen Logos, Fallstudien oder Kundenstimmen, ein bestehendes Teamfoto, neue Zielgruppen im Test (Bau und Planung, Reisebüros, Hausverwaltungen, Zulieferer) |
| **Erstellt** | 2026-10-07, **nachträglich vom Bauer dokumentiert**. Die Gestaltung entstand aus dem Plan im Claude-Doc „Website-Relaunch xponext.de: Audit und Plan“ und nicht über die Design-Library. |
| **Referenzen** | keine Library-Slugs. Vorbilder aus der Wettbewerbsrecherche: stark.marketing (Branchenseiten), buzzard-ai.de (Branchenweiche, Freigabe-Versprechen), kiworksolution.de (Zeitwert-Rechner, Menü nach Zeitfressern), mitarbyte.com (Zahlen und Stimmen im Hero), digitalxresults.de (Buchung mit Dauer und Format) |

## 1. Konzept in zwei Sätzen

Nach fünf Sekunden soll ein Besucher spüren, dass hinter XPONext zwei echte Menschen stehen, die konkret und ehrlich arbeiten. Nach dreißig Sekunden weiß er, dass es um zwei Dinge geht: gefunden werden und Zeit zurückgewinnen, und dass er mit einem 30-minütigen Erstgespräch anfangen kann.

**Der eine Wow-Faktor:** Die zweigeteilte Botschaft „Mehr Aufträge. / Weniger Zeitfresser.“ in sehr großer Schrift, die zweite Zeile grün, direkt neben dem echten Teamfoto statt einer Grafik.

## 2. Übernommene Features

Eigene Muster aus diesem Bau, IDs nach dem Schema `<site-slug>-F<n>` („aus eigenem Bau, noch nicht extern belegt“).

| ID | Feature | Wo auf der Seite | Warum es zur Realität passt |
|---|---|---|---|
| relaunch-F1 | Hero zweispaltig: Text links, Teamfoto rechts mit Bildunterschrift-Karte. Unter 600 px ersetzt eine Porträtzeile (zwei runde Porträts mit Namen) das große Foto, damit der Hero in den ersten Bildschirm passt | Startseite | Gegen den Eindruck „anonym“ aus dem Audit |
| relaunch-F2 | Vertrauenszeile unter dem Button (Google Ads zertifiziert, Bonn, Antwortzeit) und Mikrotext „Sie sprechen direkt mit uns“ | Startseite, Branchenseiten | Ersetzt den Abschnitt „Worauf Sie sich verlassen können“ |
| relaunch-F3 | Kundenleiste (Logos) mit Branchen-Chips darunter | Startseite | Zeigt Breite, ohne Testbranchen zu nennen |
| relaunch-F4 | Zwei große Angebotskarten, eine hell, eine dunkelgrün | Startseite | Die zwei Angebotsfamilien auf einen Blick |
| relaunch-F5 | Fallstudien-Karten: Bild, Branche, Titel, Zahl, Zitat | Startseite, Projekte | Belege mit Name und Zahl, sobald freigegeben |
| relaunch-F6 | Drei nummerierte Schritte als Karten | Kontakt, Branchenseiten | Ablauf ohne Fließtext |
| relaunch-F16 | Ablauf als Zeitstrahl (Wochen 1 bis 12, Balken je Phase, füllen sich beim Hineinscrollen), per Umschalter getrennt nach Sichtbarkeit und Prozessoptimierung | Startseite | Tims Feedback vom 07.10.2026: Abläufe unterscheiden sich, Zeitplan auf einen Blick |
| relaunch-F7 | Team-Abschnitt zweispaltig mit Porträts und Video | Startseite, Über uns | Gesichter und Rollen |
| relaunch-F8 | FAQ als aufklappbare `details`, Schema automatisch aus dem sichtbaren Text | Startseite, Branchenseite Architekturbüros | Ohne JavaScript, GEO-Grundlage |
| relaunch-F9 | Kontakt: drei Wege (Termin, Telefon, Mail) neben dem Formular | Startseite, Kontakt | Jede Vorliebe bedient |
| relaunch-F10 | Dunkelgrünes CTA-Band mit Ansprechpartner-Karte | Unterseiten | Persönlicher Abschluss |
| relaunch-F11 | Leistungsseite mit Randspalte: Kontaktkarte, Links zu den anderen Leistungen, auf Desktop mitlaufend | Leistungsseiten | Nutzt den leeren rechten Rand für die Conversion |
| relaunch-F12 | Branchenseite nach festem Ablauf: Situationen, Schritte, Einwände, Beleg und Angebot, FAQ, Abschluss | /fuer/* | Vorbild Branchenseiten von stark.marketing |
| relaunch-F13 | Zeitwert-Rechner (Stunden × Stundensatz × 46 Wochen) | Leistungsseite KI-Automatisierung | Zeitersparnis greifbar, ohne eine Einsparung zu versprechen |
| relaunch-F14 | Dunkle Fußzeile mit Kontaktdaten und vier Spalten | alle Seiten | Telefonnummer und Adresse überall sichtbar |
| relaunch-F15 | Gelb gestreifte Platzhalter mit `data-ph` | wo Inhalte fehlen | Fehlendes sichtbar statt erfunden, vor dem Livegang zu ersetzen |

## 3. Typografie

Eine Familie: Inter (variabel, `assets/fonts/inter-variable.woff2`), selbst gehostet, per `preload`.

| Rolle | Familie | Größe Desktop | Größe Mobil | Gewicht | Laufweite | Zeilenhöhe |
|---|---|---|---|---|---|---|
| Hero/H1 | Inter | 4,1 rem | 2,3 rem | 800 | −0,035 em | 1,03 |
| H1 Unterseiten | Inter | 3,3 rem | 2 rem | 800 | −0,035 em | 1,03 |
| H2 | Inter | 2,6 rem | 1,75 rem | 780 | −0,03 em | 1,12 |
| H3 | Inter | 1,22 rem | 1,22 rem | 700 | −0,01 em | 1,3 |
| Body | Inter | 1,0625 rem | 1,0625 rem | 400 | 0 | 1,65 |
| Label/Eyebrow | Inter | 0,8 rem, Versalien | 0,8 rem | 650 | 0,09 em | normal |

Große, enge Überschriften tragen die Marke, ruhiger Fließtext trägt die Inhalte. Silbentrennung in Überschriften nur unter 480 px.

## 4. Farben

| Token | Hex | Einsatz | Kontrast gegen Grund |
|---|---|---|---|
| `--grund` | #FFFFFF | Seitengrund | |
| `--soft` | #F6F7F5 | abwechselnde Abschnitte | |
| `--ink` | #0D0D0D | Überschriften | 19,4:1 auf Weiß |
| `--text` | #374151 | Fließtext | 10,3:1 auf Weiß |
| `--muted` | #5F6670 | Nebentext | 5,8:1 auf Weiß, 5,4:1 auf #F6F7F5 |
| `--line` | #E5E7EB | Linien, Kartenränder | |
| `--green` | #1B6B45 | Akzent, Buttons, Eyebrows (Farbe aus dem Logo) | 6,5:1 auf Weiß, Weiß auf Grün 6,5:1 |
| `--green-ink` | #0F3A26 | dunkle Angebotskarte, CTA-Band | Weiß 12,7:1, #D7E6DD 9,8:1, #8FD3AE 7,3:1 |
| `--dark` | #0E1712 | Fußzeile | #A7B3AC 8,4:1 |
| Platzhalter | #78590A auf #FEF3C7 | nur Platzhalter | 5,8:1 |

Farbe kommt aus dem Logo, nicht aus Fotos. Dunkel sind nur die zweite Angebotskarte, das CTA-Band und die Fußzeile.

## 5. Raster und Rhythmus

- Container: 1160 px, Rand 20 px
- Spalten: Hero 1,08 : 0,92, Zweispalter 1 : 1, Karten 2er oder 3er Raster, Leistungsseiten 46 rem Text plus Randspalte
- Sektionsabstand: 4 bis 6,5 rem (clamp), Abstand innerhalb 1 bis 1,2 rem
- Ausrichtung: linksbündig an gemeinsamer Kante, zentriert nur bei den bestehenden Check-Seiten und der Musterentwürfe-Übersicht

## 6. Seiteninventar

| Seite | URL | Zweck | Besonderheit |
|---|---|---|---|
| Startseite | / | Dach für alle Zielgruppen | FAQ-Schema, Kontaktformular |
| Leistungen | /leistungen.html | Überblick über beide Bereiche | Preistabelle, Platzhalter Einstiegspreise |
| Leistungsseiten | /leistungen/*.html | je Leistung, generiert | Randspalte, Rechner auf KI-Automatisierung |
| Projekte | /projekte.html | Fallstudien, Messmethode | nur Platzhalter für Fälle und Stimmen |
| Über uns | /ueber-uns.html | Gründer, Arbeitsweise | Platzhalter Gründergeschichte und Video |
| Kontakt | /kontakt.html | Erstgespräch | Platzhalter Kalender, `?quelle=` |
| Branchenseiten | /fuer/<slug>/ | je Kampagne | nur Architekturbüros indexiert |
| Blog | /blog/ | bestehende Artikel | nur im Footer verlinkt |
| Checks | /website-check.html, /geo-check.html | Werkzeuge | bestehende Seiten, nur Kopf und Fuß neu |
| Impressum, Datenschutz, AGB, 404 | | Rechtliches | noindex |

## 7. Navigation

- Punkte: Leistungen (mit Aufklappmenü in zwei Gruppen plus Checks), Projekte, Über uns, Kontakt. Telefonnummer und Button „Erstgespräch buchen“ rechts.
- Sticky, weißer Hintergrund mit leichter Transparenz.
- Mobil: Burger mit Ausklappen, Button bleibt in der Leiste, Telefon im Menü.

## 8. Bildkonzept

- Hero: Teamfoto 4 : 3,4 mit `object-fit: cover`, Freisteller auf Schwarz. Bis zum Fotoshooting das bestehende Foto. Auf dem Handy (unter 600 px) Porträtzeile statt Foto.
- Porträts rund (Kontaktkarten) oder quadratisch (Über uns).
- Keine Stockfotos. Fehlende Bilder sind Platzhalter, keine Symbolbilder.

## 9. Motion

- Nur Übergänge an Hover und Menü (0,15 bis 0,2 s), unter `prefers-reduced-motion` abgeschaltet.
- Kein Preloader, kein Laufband, kein Autoplay.

## 10. Bewusst nicht übernommen

- FAQ-Laufband, Slider und Karussells
- Emojis als Icons
- Stockfotos und KI-Symbolbilder
- Google Fonts
- Branchen-Tabs im Hero (Buzzard): die Startseite nennt nur Branchen mit echten Kunden
- Verlinkung der Musterentwürfe und der Ortsseiten
- Kennzahlenleiste mit Zahlen, die nicht belegt oder nicht freigegeben sind

**Bewusste Abweichungen von der Qualitätscheckliste** (die Checkliste ist für Architekten-Kundenseiten geschrieben):
- Analytics (GA4, Microsoft Clarity, Google-Ads-Konversion) mit Cookie-Banner, bestehende Technik. `gtag.js` und Clarity laden erst nach Einwilligung.
- Kontaktformular über ein Google-Apps-Script, bestehende Technik.
- Bestehende Adressen mit `.html` bleiben, damit indexierte Seiten nicht verloren gehen. Neue Branchenseiten als Ordner.
- JSON-LD `ProfessionalService` statt `ArchitectOffice`, Impressum ohne Kammerangaben (Agentur, kein Architekturbüro).
- `google96bd4cd907a7704c.html` ist die Verifizierungsdatei der Google Search Console und muss unverändert bleiben.

## 11. Offene Fragen an den Nutzer

Liegen bei Tim, nicht vom Bauer entschieden: Preisrahmen, Risikoumkehr je Angebot, Name der GEO-Messmethode, Förderfähigkeit, Freigaben für Logos, Fallstudien und Stimmen, Kalender-Tool, Rechte an den Teamfotos, Datenschutzerklärung (Google-Ads-Konversion), Firmierung in den AGB.
