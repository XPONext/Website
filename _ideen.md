# Ideen für xponext.de

Sammelstelle für Ideen zur Website. Neue Ideen landen hier zuerst und werden nicht sofort
umgesetzt, sondern gemeinsam angegangen, wenn Zeit dafür ist.

Der Unterstrich im Dateinamen sorgt dafür, dass GitHub Pages die Datei nicht ausliefert. Das
Repo selbst ist aber öffentlich, also nichts Vertrauliches hier ablegen (Kundennamen ohne
Freigabe, interne Preise).

**Status:** `offen` · `in Arbeit` · `erledigt` · `verworfen`
**Aufwand (grob):** S = ein Nachmittag · M = ein bis zwei Tage · L = mehrere Tage oder
Abhängigkeiten nach außen

## Überblick

| Nr. | Idee | Bereich | Status | Aufwand |
|---|---|---|---|---|
| 1 | Blogartikel überarbeiten | Blog | offen | M |
| 2 | Partner und Büros verlinken | Vertrauen | offen | M |
| 3 | Video von uns aufnehmen | Vertrauen | offen | M |
| 4 | Website-Konfigurator mit Preisrahmen | Angebot | offen | L |
| 5 | Kundenstimmen entfernen | Startseite | offen | S |
| 6 | Startseite entschlacken | Startseite | offen | M |
| 7 | FAQ radikal kürzen | Startseite | offen | S |
| 8 | Leistungen übersichtlicher gestalten | Leistungen | offen | M |
| 9 | Einzugsgebiete ausbauen oder streichen | Einzugsgebiete | offen | M |
| 10 | Websites und Design in den Vordergrund | Positionierung | offen | M |
| 11 | Projekte selbst pflegen (CMS) in unseren Websites | Angebot | offen | M |
| 12 | KI-Pflegedienst auch für fremde Websites | Angebot | offen | L |
| 13 | Produktvision: KI-Redakteur für Websites, jede Branche | Produkt | Brainstorm | L+ |

---

## 1. Blogartikel überarbeiten

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Die Blogartikel wirken generisch und austauschbar. Sie sollen persönlicher,
konkreter und erkennbar von uns sein.

**Ausgangslage:**
- 16 Artikel, Quelle unter `_content/seiten_geo/blog/*.html.md`, gebaut mit
  `python3 _content/build_geo_pages.py`. Das HTML unter `blog/` nicht direkt bearbeiten.
- Die Themen wurden redaktionell gewählt, nicht mit Keyword-Daten geprüft.

**Nachtrag 25.09.2026:** „Wir haben einen Blog und ein FAQ. Das ist Quatsch.“ Vor dem
Überarbeiten also erst die Grundsatzfrage klären: Blog behalten und deutlich besser machen,
oder ganz rausnehmen? Zum FAQ siehe Idee 7.

**Offene Fragen / Ansätze:**
- Welche Artikel behalten, welche zusammenlegen oder streichen?
- Falls der Blog ganz wegfällt: Die Artikel sind in der Sitemap und bei Google indexiert.
  GitHub Pages kann keine echten Weiterleitungen, also mit Weiterleitungsseiten arbeiten oder
  die 404 in Kauf nehmen, und die Einträge aus `sitemap.xml` entfernen.
- Eigene Erfahrungen, Beispiele aus echten Projekten und klare Meinungen einbauen statt
  allgemeiner Ratgebertexte.
- Search Console ansehen: Welche Artikel bekommen überhaupt Impressionen?

---

## 2. Partner und Büros verlinken, mit denen wir zusammenarbeiten

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Die Büros, für die wir arbeiten, auf der Website zeigen und verlinken, etwa als
Bereich „Unsere Partner“ oder „Beispiele“.

**Ausgangslage:**
- Aktuell gibt es auf der Website keinen Referenz- oder Kundenbereich.
- Die Musterentwürfe unter `musterentwuerfe/` sind erfunden und dürfen nie als Referenz
  bezeichnet werden. Echte Kundenbüros und Musterentwürfe müssen klar getrennt bleiben.

**Offene Fragen / Ansätze:**
- Welche Büros dürfen genannt werden? Vorher jeweils Freigabe einholen (Name, Logo, Link,
  eventuell Screenshot).
- Nur Logo und Link, oder kurze Fallbeispiele mit Ergebnis?
- Wo platzieren: Startseite, „Über uns“ oder eigene Seite?
- Die Musterentwürfe sind noch `noindex` und warten auf Freigabe. Passt das in denselben
  Schritt?

---

## 3. Video von uns aufnehmen

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Ein Video, in dem wir selbst erklären, wie wir arbeiten. Kernbotschaft: Wir bauen
Websites ab jetzt standardisierter, und Interessenten können sich ihre Website auf unserer
Seite selbst zusammenstellen (siehe Idee 4).

**Offene Fragen / Ansätze:**
- Länge und Ort: kurz auf der Startseite, ausführlicher auf „Über uns“?
- Hosting: YouTube-Einbettung braucht Einwilligung, dann auch `datenschutz.html` anpassen.
  Selbst gehostet ist datenschutzfreundlicher, aber die Datei ist größer.
- Ergibt erst Sinn, wenn Idee 4 steht oder zumindest feststeht, wie das Angebot aussieht.

---

## 4. Website-Konfigurator mit Preisrahmen

- **Status:** offen
- **Aufwand:** L
- **Eingebracht:** 25.09.2026

**Idee:** Interessenten stellen sich ihre Website auf xponext.de selbst zusammen: Aussehen,
Umfang, Anzahl der Projekte und so weiter. Daraus ergibt sich ein ungefährer Preisrahmen.
Passt zum Schritt hin zu standardisierteren Websites.

**Ausgangslage:**
- Statische Seite ohne Backend, der Konfigurator liefe also komplett im Browser (JavaScript).
- Für die Stil-Auswahl könnten die drei Musterentwürfe als Vorlagen dienen (Nordkant,
  Lindenau, Steinwerk).
- Der Blogartikel `website-erstellung-kosten-architekturbuero` könnte auf den Konfigurator
  verlinken.

**Offene Fragen / Ansätze:**
- Die Preisbausteine müssen aus unserer echten Kalkulation kommen, nicht aus Marktrecherche.
  Zuerst festlegen: Grundpaket, Preis pro Seite oder Projekt, Zusatzmodule.
- Welche Stellschrauben: Stil, Anzahl Seiten, Anzahl Projekte, Sprachen, Texte von uns oder
  vom Büro, Fotografie, SEO-Paket, laufende Betreuung?
- Ergebnis als Spanne („zwischen X und Y“) statt als fester Preis.
- Am Ende direkt eine Anfrage mit der gewählten Konfiguration senden, am besten über das
  bestehende Kontaktformular auf der Startseite.

---

## 5. Kundenstimmen entfernen

- **Status:** offen
- **Aufwand:** S
- **Eingebracht:** 25.09.2026

**Idee:** Den Abschnitt „Was unsere Kunden sagen“ auf der Startseite definitiv rausnehmen.

**Ausgangslage:**
- Nur auf `index.html`, aber an zwei Stellen: im Abschnitt „Was unsere Kunden sagen“ mit zwei
  Zitaten (Martin B., Architekt, Bad Honnef und Volker G., Werbeagentur, Pfullendorf) und
  zusätzlich im Hero ganz oben als Karte „Letzte Bewertung“ mit dem Zitat von Martin B.
  Kein Bewertungs-Schema im Quelltext, es hängt also nichts weiter daran.
- Die Unterzeile lautet „Echte Ergebnisse von Architekturbüros wie deinem“, obwohl eine der
  beiden Stimmen von einer Werbeagentur stammt.

**Offene Fragen / Ansätze:**
- Schneller Gewinn, lässt sich unabhängig von allem anderen sofort erledigen.
- Die zugehörigen CSS-Regeln (`.testimonial-*`) gleich mit entfernen.
- Später könnte Idee 2 (echte Partnerbüros) diesen Platz übernehmen.

---

## 6. Startseite entschlacken

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Die Startseite ist viel zu voll. Weniger Abschnitte, weniger Text, klarere
Botschaft.

**Ausgangslage:** Die Startseite hat derzeit diese Abschnitte, alle untereinander:
1. Hero
2. „Die meisten Architekturbüros verlieren täglich Aufträge“
3. „Deine Website hat eine neue Zielgruppe. Und sie ist nicht menschlich.“
4. „Unsere Leistungen“
5. „Worauf du dich bei XPONext verlassen kannst“
6. „Was unsere Kunden sagen“ (fällt weg, siehe Idee 5)
7. „Häufig gestellte Fragen“ mit 16 Fragen (siehe Idee 7)
8. „Bereit anzufangen?“ mit Kontaktformular

**Offene Fragen / Ansätze:**
- Was soll ein Besucher nach zehn Sekunden verstanden haben? Davon ausgehend Abschnitte
  streichen oder zusammenlegen.
- Hängt mit Idee 3 (Video) und Idee 4 (Konfigurator) zusammen: Wenn beides kommt, bekommt
  es wahrscheinlich einen festen Platz auf der Startseite. Am besten alles zusammen planen.

---

## 7. FAQ radikal kürzen

- **Status:** offen
- **Aufwand:** S
- **Eingebracht:** 25.09.2026

**Idee:** Das FAQ unter den Kundenstimmen ist viel zu lang. Grundsätzlich infrage gestellt
(„Blog und FAQ, das ist Quatsch“).

**Ausgangslage:**
- 16 Fragen in drei Kategorien auf der Startseite, dazu ein FAQPage-Schema mit denselben 16
  Fragen im Quelltext.

**Offene Fragen / Ansätze:**
- Ganz weg oder auf die fünf wichtigsten Fragen kürzen?
- Beim Kürzen das FAQPage-Schema im Quelltext mit anpassen. Es darf nur Fragen enthalten,
  die auch sichtbar auf der Seite stehen.

---

## 8. Leistungen übersichtlicher gestalten

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Die Leistungen (und die Website allgemein) sehen schlecht aus: zu viel untereinander
gestapelt, zu viel Inhalt.

**Ausgangslage:**
- `leistungen.html` ist die Übersicht mit fünf Blöcken untereinander: Webseite, Google Ads &
  AI Ads, GEO, Bewertungsmanagement, Lokales SEO. Diese Seite ist von Hand gebaut.
- Dazu kommen vier Detailseiten unter `leistungen/` mit jeweils rund 1.500 Wörtern. Die sind
  generiert, Layout-Änderungen also in `_content/build_geo_pages.py`, Text in
  `_content/seiten_geo/leistungen/`.

**Offene Fragen / Ansätze:**
- Übersicht als Raster mit kurzen Karten statt langer Blöcke untereinander.
- Detailseiten kürzen und stärker gliedern (Zwischenüberschriften, klare Leistungspakete,
  weniger Fließtext).
- Wenn die Websites standardisierter werden (Idee 4), könnte sich das Leistungsangebot selbst
  vereinfachen. Dann zuerst das Angebot klären, danach die Seite.

---

## 9. Einzugsgebiete ausbauen oder streichen

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Entweder deutlich mehr Einzugsgebiete anlegen oder die Einzugsgebiete komplett
rausnehmen.

**Ausgangslage:**
- Aktuell nur Bonn und Köln, je eine Übersichtsseite plus fünf Kombiseiten (Website, SEO,
  GEO, Google Ads, Zeitfresser-Workshop), zusammen 12 Seiten. Generiert aus
  `_content/seiten_geo/einzugsgebiet/`.
- Die Leistungsseiten verlinken intern auf die Kombiseiten.

**Offene Fragen / Ansätze:**
- Zuerst entscheiden: ausbauen oder streichen.
- Ausbauen: Welche Orte? Am besten dort, wo tatsächlich Kunden sitzen oder hinsollen. Jede
  Stadtseite braucht echten lokalen Bezug, sonst sind es austauschbare Kopien, die Google
  schlecht bewertet.
- Streichen: interne Links aus den Leistungsseiten entfernen, Einträge aus `sitemap.xml` und
  `_content/seiten_geo/sitemap_eintraege.md` nehmen, alte Adressen per Weiterleitungsseite
  abfangen.

---

## 10. Websites und Design in den Vordergrund

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Websites sind unser Hauptgeschäft, und wir können richtig gut gestalten. Beides sieht
man auf der Website aktuell kaum. Der Fokus soll deutlicher auf Websites und Design liegen.

**Ausgangslage:**
- Der Hero sagt „Mehr Projekte. Weniger Zeitfresser.“ Die Website ist dort nur ein Punkt in
  der Aufzählung „Webseite, SEO, GEO, Ads und effiziente Prozesse mit KI“.
- Auf `leistungen.html` ist die Website einer von fünf gleichrangigen Blöcken.
- Nirgends auf der Website ist eine Arbeit von uns zu sehen. Die drei Musterentwürfe unter
  `musterentwuerfe/` zeigen genau das, sind aber noch `noindex` und nirgends verlinkt
  (Livegang nur nach Tims Freigabe).

**Offene Fragen / Ansätze:**
- Hero und Seitentitel auf Websites für Architekturbüros zuspitzen, SEO, GEO und Ads als
  Ergänzung dahinter.
- Einen sichtbaren Bereich mit Arbeiten schaffen: Musterentwürfe (als solche gekennzeichnet,
  nie „Referenz“) und, sobald freigegeben, echte Kundenwebsites aus Idee 2.
- Die eigene Website muss selbst zeigen, dass wir gut gestalten können. Sonst wirkt der
  Anspruch unglaubwürdig. Das spricht dafür, Idee 6 und 8 zusammen mit dieser Idee anzugehen.
- Passt zu Idee 4: Die Stil-Auswahl im Konfigurator zeigt gleichzeitig die Bandbreite
  unserer Gestaltung.

---

## 11. Projekte selbst pflegen (CMS) in unseren Websites

- **Status:** offen
- **Aufwand:** M
- **Eingebracht:** 25.09.2026

**Idee:** Vielen Architekturbüros ist wichtig, ihre Projekte selbst einpflegen zu können, aber
sie haben keine Zeit für komplizierte Systeme. Wir bauen einmal ein einfaches Pflege-Tool ein,
mit dem das richtig schnell geht.

**Ausgangslage:**
- Unsere Websites sind statisch (siehe Musterentwürfe: Inhalte in Markdown, Seiten erzeugt
  von `build.py`). Dazu passt ein Git-basiertes CMS: Das Büro füllt ein Formular aus (Titel,
  Ort, Jahr, Text, Fotos), das CMS speichert das im Repo, die Seite wird automatisch neu
  gebaut und ist kurz danach live. Die Website bleibt schnell und sicher, es gibt keine
  Datenbank und keine Plugins, die man aktualisieren muss.
- Kandidaten zum Prüfen: Pages CMS, Decap CMS, Sveltia CMS. Alle kostenlos, alle arbeiten
  direkt mit GitHub.

**Offene Fragen / Ansätze:**
- KI-Schritt beim Speichern: Text für Google und KI-Suche aufbereiten, Alt-Texte erzeugen,
  Fotos verkleinern. Als Vorschlag, den das Büro annimmt, nicht stillschweigend überschrieben.
- Hosting: bleibt die Kundenseite bei uns (GitHub Pages) oder beim Büro (z. B. Strato)? Im
  zweiten Fall lädt der automatische Build per SFTP hoch.
- Prüfen, ob `build.py` Projekte aus einzelnen Dateien lesen kann, sonst anpassen.
- Gehört als Option in den Konfigurator (Idee 4) und ist ein starkes Verkaufsargument für
  die standardisierten Websites.
- Baustein der Produktvision in Idee 13.

---

## 12. KI-Pflegedienst auch für fremde Websites

- **Status:** offen
- **Aufwand:** L
- **Eingebracht:** 25.09.2026

**Idee:** Das Pflege-Tool auch Büros anbieten, deren Website von einer anderen Agentur stammt
oder vor Jahren gebaut wurde. Das Büro gibt nur seine Projekte ein, die KI verbessert Text und
Bilder und stellt alles auf die Website. Das Büro hinterlegt dafür einmal seine Zugangsdaten
(z. B. Strato).

**Einschätzung: geht, aber nicht mit einer Lösung für alle Websites.** Es hängt davon ab,
worauf die Website läuft:

| Plattform | Machbar? | Wie |
|---|---|---|
| WordPress | gut | Offizielle Schnittstelle mit eigenem Anwendungspasswort. Knackpunkt: Themes und Page-Builder sind überall anders. |
| Selbst gebautes HTML per FTP | mittel | KI nimmt eine bestehende Projektseite als Vorlage, baut die neue im selben Stil, lädt per SFTP hoch. Jede Seite ist anders. |
| Typo3, Joomla | mittel | Schnittstellen vorhanden, aber aufwendig einzurichten. |
| Baukästen (Wix, Jimdo, Strato- oder IONOS-Baukasten, Squarespace) | kaum | Keine oder nur eingeschränkte Schnittstellen. Hier eher einen Relaunch anbieten. |

**Worauf es ankommt:**
- **Nie direkt live.** Die KI erstellt einen Entwurf, das Büro sieht eine Vorschau und gibt
  frei, erst dann wird veröffentlicht. Vorher automatisch ein Backup.
- **Zugangsdaten eingeschränkt.** Nie das Strato-Hauptkonto, sondern einen eigenen
  SFTP-Zugang nur für das Web-Verzeichnis oder ein WordPress-Anwendungspasswort. Sicher
  aufbewahren und prüfen, ob die AV-Vereinbarung in den AGB das abdeckt.
- **Andere Agentur.** Klären, ob dort ein Wartungsvertrag läuft und ob Updates unsere
  Änderungen überschreiben würden. Das Büro muss die Rechte an seiner Website haben.
- **Technik.** Claude Code ist ein Werkzeug für uns, nicht für Kunden. Als Produkt liefe das
  über die Claude API hinter einem einfachen Formular.

**Vorschlag für den Einstieg:** Erst als Dienstleistung verkaufen, nicht gleich als Produkt
bauen. Das Büro schickt ein Projekt (Formular oder Mail mit Text und Fotos), wir setzen es mit
Claude Code um, das Büro gibt frei. So testen wir Nachfrage und Zahlungsbereitschaft und
lernen, welche Plattformen am häufigsten vorkommen. Automatisiert wird dann, was sich
wiederholt, vermutlich WordPress zuerst.

**Offene Fragen / Ansätze:**
- Marktgröße prüfen: `tools/website_existenz_check` im Workflow-Repo erkennt bisher nur, ob
  eine Website existiert. Um eine Plattform-Erkennung erweitert, zeigt es, wie viele unserer
  Leads auf WordPress, Baukästen oder eigenem HTML laufen.
- Vertrieb: Türöffner zu Büros, die gerade keine neue Website wollen. Wer auf einem Baukasten
  sitzt, ist ein Kandidat für einen Relaunch.
- Preismodell (pro Projekt oder monatlich) aus unserer eigenen Kalkulation festlegen.
- Baustein der Produktvision in Idee 13.

---

## 13. Produktvision: KI-Redakteur für Websites, jede Branche

- **Status:** Brainstorm, mit dem Kollegen besprechen
- **Aufwand:** L+ (eigenes Produkt)
- **Eingebracht:** 25.09.2026

**Die Idee, sinngemäß in Tims Worten:** Die meisten Unternehmen haben keine Lust, sich um
ihre Website zu kümmern. Sie sollen nur noch eingeben, was drauf soll, in Stichpunkten. Sie
müssen weder kreativ sein noch Texte schreiben. Die Software steckt voller Wissen darüber, wie
gute Websites aussehen, macht daraus gute und individuelle Inhalte und stellt sie online, egal
wo die Website gebaut wurde oder liegt. Sie lernt ständig dazu. Das lässt sich an jede Branche
verkaufen: „Ihr habt etwas Neues? Los geht's.“ Auch ein aktueller Blog, der für die
Sichtbarkeit in KI-Suchen wichtig ist, läuft damit fast von selbst.

### Müssten wir dafür ein CMS entwickeln?

Nein. Ein CMS ist genau der Teil, den niemand bedienen will. Gebaut würde eine Schicht
darüber, ein KI-Redakteur aus vier Bausteinen:

1. **Eingang:** so einfach wie eine Nachricht an einen Mitarbeiter. Formular, E-Mail, WhatsApp
   oder Sprachnachricht: „Neues Projekt, Einfamilienhaus in Bonn, Holzbau, fertig 2026, fünf
   Fotos anbei.“
2. **Wissen:** unser Know-how, wie gute Projektseiten und Artikel aufgebaut sind, SEO und GEO,
   dazu pro Kunde ein Profil mit Stil, Tonfall und Fachbegriffen. Technisch die Claude API mit
   unseren Regeln. Vieles davon gibt es schon als Skills im Workflow-Repo:
   `architect_website_creation`, `design_library`, `geo_content_recherche`,
   `programmatic_seo_geo`, `seo_geo_audit`.
3. **Vorschau und Freigabe:** Der Kunde sieht das Ergebnis und sagt „passt“ oder „zweiter
   Absatz kürzer“. Live geht es erst nach der Freigabe.
4. **Veröffentlichen:** ein Anschluss pro Plattform. Eigene Websites über GitHub, WordPress
   über die Schnittstelle, alte HTML-Seiten per SFTP. Das ist der schwierigste Teil, siehe
   Idee 12.

**Hosting ist nicht die Frage, die Bauweise ist es.** Strato ist nur der Ort, an dem die
Dateien liegen. Ob es klappt, entscheidet, womit die Seite gebaut ist: WordPress bei Strato
geht gut, eine alte HTML-Seite bei Strato geht mit Aufwand, der Strato-Baukasten kaum.

**„Lernt ständig dazu“, realistisch gemeint:** Wir trainieren kein eigenes KI-Modell. Das
System merkt sich pro Kunde, was er vor der Freigabe geändert hat, und berücksichtigt das
beim nächsten Mal. Was sich bei vielen Kunden bewährt, fließt in unsere Regeln ein.

### Einschätzung

- **Das Potenzial ist echt.** An fehlender Pflege veralten die meisten Websites, und der
  Bedarf kommt immer wieder. Das ergibt ein monatliches Abo statt eines Einmalprojekts.
- **„Jede Website“ ist das schwierigste Versprechen.** Am saubersten funktioniert es auf
  Websites, die wir selbst bauen. Daraus folgt eine Strategie: Neue Kunden bekommen die
  standardisierte Website mit eingebautem KI-Redakteur (Idee 4 und 11). Bestehende Websites
  schließen wir an, wo es geht. Wo nicht, bieten wir den Umzug auf unsere Plattform an.
- **Die Qualität steht und fällt mit der Eingabe.** Aus echten Stichpunkten macht die KI gute
  Texte, aus nichts wird Füllmaterial. Genau das haben wir beim eigenen Blog gemerkt (Idee 1).
  Das Produkt muss also gezielt nach Fakten fragen (Was war besonders? Welches Material? Was
  sagt der Bauherr?), statt aus drei Wörtern einen Artikel aufzublasen.
- **Wettbewerb, genauer prüfen:** Baukästen wie Wix, Squarespace oder Jimdo haben inzwischen
  KI-Assistenten, und es gibt KI-Website-Baukästen für kleine Unternehmen. Dort muss man sich
  aber selbst einloggen und alles selbst machen. Unser Unterschied: kein Login, nur
  Stichpunkte schicken; Branchenwissen; eine Agentur, die dahintersteht.
- **Aufwand:** Als echtes Produkt ist das Softwareentwicklung mit Logins, Abrechnung, sicherer
  Aufbewahrung von Zugangsdaten, Support und Haftung. Für ein kleines Team nur in Stufen
  machbar.

### Weg in Stufen

1. **Sofort, ohne Entwicklung:** als Dienstleistung im Abo. Kunden schicken Stichpunkte und
   Fotos per Mail oder WhatsApp, wir erstellen die Inhalte mit Claude Code und unseren Skills,
   der Kunde gibt frei, wir veröffentlichen. Das zeigt, ob Kunden dafür zahlen und was immer
   wieder vorkommt.
2. **Eigene Websites automatisieren:** Eingabe, KI, Vorschau, Freigabe, live (Idee 11).
3. **Fremde Websites anschließen**, WordPress zuerst (Idee 12).
4. **Selbstbedienung für Kunden**, danach weitere Branchen.

### Zum Besprechen

- Wollen wir ein Produkt bauen, oder bleiben wir eine Agentur mit KI im Hintergrund?
- Architekturbüros als erste Branche? Und welche als nächste?
- Wie viel Zeit können wir investieren, und ab wann bräuchten wir Hilfe bei der Entwicklung?
- Preislogik: Abo pro Monat, pro Beitrag, oder in die Website-Pakete eingerechnet?
- Mit welchen zwei oder drei Bestandskunden testen wir Stufe 1?
