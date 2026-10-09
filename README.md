# Website
The official XPONext Website

## Tech Stack
- HTML/CSS — kein Framework, Hosting über GitHub Pages
- Ein gemeinsames Stylesheet `css/site.css` und ein Skript `js/site.js` (Menü auf dem Handy, Kontaktformular)
- Schrift Inter selbst gehostet (`assets/fonts/`), nie über Google Fonts

## Development

**Alles bauen:** `python3 _content/build_all.py`. Das baut die generierten Seiten, schreibt Kopf,
Kopfzeile und Fußzeile in die handgebauten Seiten, erzeugt `sitemap.xml` und listet offene Platzhalter.
Danach lokal ansehen: `python3 -m http.server 8000`, dann http://localhost:8000.

**Kopfzeile, Fußzeile, Analytics:** stehen nur noch in `_content/layout.py`. Handgebaute Seiten
(Startseite, Leistungen, Projekte, Über uns, Kontakt, Checks, Rechtliches, 404) enthalten Markierungen
`<!-- @layout:head -->`, `<!-- @layout:header -->` und `<!-- @layout:footer -->`. Was dazwischen steht,
wird beim Bauen ersetzt, alles andere bleibt von Hand bearbeitbar. Der aktive Menüpunkt kommt aus
`<body data-nav="…">`. Neue handgebaute Seite: Markierungen übernehmen und in `HANDGEBAUT` in
`_content/sync_layout.py` eintragen.

**FAQ-Schema:** Steht in einer Seite `<!-- @layout:faq-schema -->`, wird das FAQPage-Schema beim Bauen
aus den sichtbaren Fragen (`<div class="faq">` mit `<details>`) erzeugt. Schema und Seite können so
nicht auseinanderlaufen.

**Platzhalter:** Fehlende Inhalte (Kundenlogos, Fallstudien, Kundenstimmen, Fotos, Video, Kalender,
Preise) stehen als gelb gestreifte Kästen mit `data-ph="…"` in den Seiten, jeweils mit einem Kommentar
`PLATZHALTER-BLOCK`. Vor dem Push: Inhalt einsetzen oder den Block bewusst entfernen.
`python3 _content/build_all.py --streng` bricht ab, solange noch Platzhalter da sind.
Kundennamen, Logos und Zahlen nur mit schriftlicher Freigabe des Kunden. Das Repo ist öffentlich.

**Anrede:** Die Website siezt die Besucher (seit 28.09.2026, vorher du). Neue Texte,
Content-Pakete und Vorlagen im Generator ebenfalls in Sie-Form, auch Cookie-Banner,
Formular-Meldungen und die Ergebnis-Texte in GEO-Check und Website-Check.

**3D-Logo im Hero:** Formen in `assets/hero-shapes/`, Reihenfolge und Farben am `<div class="hero-logo3d">` in
`index.html`. Code und Anleitung für neue Formen: `_content/hero-logo-3d/README.md`.

**Kontaktformular:** Alle Formulare mit `class="contact-form"` senden über `js/site.js` an das
Google-Apps-Script. `data-quelle` und der URL-Parameter `?quelle=` landen vorn in der Nachricht,
so sieht man, von welcher Seite oder Kampagne eine Anfrage kommt.

## Generierte Seiten (`_content/`)

Die Leistungs-, Einzugsgebiet-, Kombi- und Blogseiten sowie die Branchenseiten unter `/fuer/`
werden **nicht von Hand gepflegt**.
Ihre Quelle sind die Markdown-Content-Pakete unter `_content/seiten_geo/`:

```
_content/seiten_geo/
├── leistungen/       → /leistungen/*.html
├── einzugsgebiet/    → /einzugsgebiet/*.html + /einzugsgebiet/{ort}/*.html
├── blog/             → /blog/*.html (+ blog/index.html)
└── sitemap_eintraege.md   Liste aller Slugs, Grundlage für sitemap.xml
```

Ändern: die `.md` bearbeiten, dann

```bash
python3 _content/build_geo_pages.py
```

Das Skript schreibt die fertigen `.html` in den Repo-Root. **Das HTML dieser Seiten nicht
direkt bearbeiten** — beim nächsten Lauf wird es überschrieben.

Seit dem Relaunch (Oktober 2026) kennen die `.md` Zwischenüberschriften (`## Frage?`), Listen
(`- `, `1. `) und Tabellen. Erster Absatz = Kernaussage, Antwort zuerst. Die Ortsseiten Bonn und Köln
werden mit `noindex` gebaut und sind nicht mehr verlinkt, die Dateien bleiben für alte Links.
`/effizienz.html` ist eine Weiterleitung auf `/leistungen/ki-automatisierung.html`.

### Branchenseiten (`/fuer/<branche>/`)

Eine YAML-Datei je Branche unter `_content/landingpages/`, gebaut von `_content/build_landingpages.py`.
`index: false` = Testphase: `noindex`, nicht in der Sitemap, nirgends verlinkt, nur aus der jeweiligen
Kampagne (Signatur, Folgemail, Video-Mail). Trägt eine Hypothese, `index: true` setzen und auf der
Startseite in der Branchenleiste verlinken. Indexiert ist bisher nur `/fuer/architekturbueros/`.
Die Buttons führen auf `/kontakt.html?quelle=<branche>`. Keine internen Kampagnendetails in die YAML
schreiben, das Repo ist öffentlich.

`_content/` beginnt mit einem Unterstrich und wird von GitHub Pages/Jekyll nicht
ausgeliefert. Quelle und Generator lagen bis 14.08.2026 im Repo `XPO_Agentic_Workflow`
(`eigene_website/`, `tools/geo_page_generator/`) und sind hierher gezogen, damit Quelle
und Ausgabe im selben Repo liegen. Erzeugt werden die Content-Pakete vom
`programmatic_seo_geo`-Skill.

## GEO-Check Proxy (`cloudflare-worker/`)

`geo-check.html` (Startseite → „GEO-Check") lässt Besucher eine beliebige URL auf GEO-Signale
prüfen (Schema.org, KI-Crawler-Zugang in robots.txt, Content-Struktur, Sitemap). Da die Seite
statisch ist, kann der Browser fremde Domains wegen CORS nicht direkt abrufen — dafür holt ein
kleiner eigener Cloudflare Worker (`cloudflare-worker/geo-proxy.js`) die Zielseite serverseitig
und gibt sie mit CORS-Headern zurück. Bewusst **kein** freier öffentlicher CORS-Proxy
(allorigins.win o.ä.) — die fallen erfahrungsgemäß häufig aus oder werden kostenpflichtig.

**Einmaliges Setup (falls der Worker noch nicht deployt ist):**

1. Kostenloses Konto auf [dash.cloudflare.com](https://dash.cloudflare.com) anlegen (keine Kreditkarte nötig).
2. Workers & Pages → Create → Create Worker → einen Namen vergeben (z.B. `xponext-geo-proxy`) → Deploy.
3. Im Worker auf „Edit code" gehen, den Inhalt von `cloudflare-worker/geo-proxy.js` einfügen, Deploy.
4. Die zugewiesene `*.workers.dev`-URL kopieren und in `geo-check.html` bei der Konstante `PROXY`
   eintragen (`YOUR-SUBDOMAIN` ersetzen), z.B. `https://xponext-geo-proxy.<konto>.workers.dev/?url=`.
5. Committen & pushen.

Das kostenlose Cloudflare-Kontingent (100.000 Requests/Tag) reicht für dieses Tool bei Weitem.
Änderungen am Worker-Code: `cloudflare-worker/geo-proxy.js` bearbeiten, dann im Cloudflare-
Dashboard erneut „Edit code" → einfügen → Deploy (kein automatisches Deployment aus dem Repo).

### GEO-Check Leads

`geo-check.html` zeigt nur den Score + einen Teaser-Punkt frei; der vollständige Befund wird erst
nach Eingabe einer E-Mail-Adresse freigeschaltet (`POST /lead` am selben Worker). Der Worker prüft
Format + MX-Record der Adresse, legt den Lead in Cloudflare KV ab und verschickt optional eine
Benachrichtigung über [Resend](https://resend.com). Kein Direktvertrieb/Kaltakquise — Zweck ist,
bei Rückfragen zur Anfrage Kontakt aufnehmen zu können (siehe `datenschutz.html`, Abschnitt 5.3).

**TODO:** Resend ist noch nicht eingerichtet — Leads landen aktuell nur in KV, es kommt noch
**keine** Sofort-Benachrichtigung per E-Mail an info@xponext.de. Siehe Schritt 2 unten.

**Einmaliges Setup zusätzlich zum Proxy-Setup oben:**

1. ~~**KV-Namespace:**~~ ✅ erledigt (`xponext-geo-leads`, Variable `LEADS`, gebunden & getestet).
2. **Resend (offen — für die Sofort-Benachrichtigung):**
   - Kostenloses Konto auf [resend.com](https://resend.com) anlegen.
   - Domain `xponext.de` verifizieren (DNS-Einträge, die Resend vorgibt).
   - API-Key erstellen.
   - Im Worker → Settings → Variables and Secrets → „Add" → Name `RESEND_API_KEY`, Typ **Secret**,
     Wert = der API-Key → Deploy.
   - Ohne diesen Schritt funktioniert die Freischaltung trotzdem (Leads landen in KV), es kommt
     nur keine Sofort-Mail.
3. **Leads einsehen:** Cloudflare-Dashboard → Storage & Databases → KV → `xponext-geo-leads` →
   Einträge durchsuchen (Key-Präfix `lead:`, Wert ist JSON mit `email`, `domain`, `score`, `createdAt`).

Der Sender `geo-check@xponext.de` in `sendNotification()` (in `geo-proxy.js`) muss zur in Resend
verifizierten Domain passen — sonst schlägt der Mail-Versand fehl (Lead wird trotzdem gespeichert).

### GEO-Check Testzugang

Zum Testen lässt sich der vollständige Bericht ohne E-Mail freischalten: Statt der E-Mail-Adresse
das Passwort ins Feld eintragen (ohne @, die Checkbox ist dann nicht nötig). Die Prüfung läuft im
Browser, es geht nichts an den Worker, es entsteht kein Lead. Ein falsches Passwort sieht aus wie
eine ungültige E-Mail-Adresse.

1. `.env.example` nach `.env` kopieren (liegt in `.gitignore`, bleibt lokal) und
   `GEO_CHECK_PASSWORT=` ausfüllen.
2. `python3 _content/build_all.py` laufen lassen. Das schreibt den SHA-256-Hash des Passworts in
   `geo-check.html` (`ZUGANG_HASH`), nie das Passwort selbst, das Repo ist öffentlich.
3. Committen und pushen.

Passwort ändern: `.env` anpassen, Schritt 2 und 3. Leerer Wert schaltet den Zugang aus. Ohne `.env`
(z. B. auf einem anderen Rechner) lässt der Build den vorhandenen Hash unverändert.
Kein echter Schutz: der Bericht steht ohnehin im Seitenquelltext, das Overlay ist nur ein Hinweis.

## Musterentwürfe (`musterentwuerfe/`)

Vollständige Muster-Websites für Architektur- und Innenarchitekturbüros, gebaut mit dem
`architect_website_creation`-Skill aus dem Repo `XPO_Agentic_Workflow`. Sie zeigen die Arbeitsweise,
ohne Kundenprojekte zu verwenden: Büros, Personen, Anschriften und Projekte sind erfunden und als
Musterangaben gekennzeichnet, die Fotografie ist Stockmaterial von Pexels.

**Nie als „Referenz" oder „umgesetztes Projekt" bezeichnen.** Beide Begriffe meinen im
Verkaufsgespräch: für einen Kunden geliefert. Erlaubt sind Musterentwurf, Muster-Website, Entwurf.

Jeder Entwurf liegt als eigenständige statische Site unter `musterentwuerfe/<slug>/` (relative
Pfade, eigene `assets/`, eigene Fonts, `noindex` auf jeder Seite, Hinweis in der Fußzeile).
Übersicht: `musterentwuerfe/index.html`. **Seit dem Relaunch (07.10.2026) nur noch per Link:** Tim will
die Entwürfe nicht mehr auf der Website zeigen, sondern Interessenten direkt schicken. Deshalb ist auch
die Übersicht `noindex`, steht nicht in der Sitemap und wird von keiner Seite verlinkt. Nicht per
robots.txt sperren, sonst sieht Google das `noindex` nicht.

Unter `_doku/` (von GitHub Pages nicht ausgeliefert) liegt je Entwurf die komplette Entstehung:
`inhalte.md` → `design-brief.md` → `build.py` (erzeugt alle Seiten) → `pruefbericht.md` →
`bau-notizen.md` → `screenshots/`. Änderungen immer über `build.py`, nicht im HTML. Bildnachweise
in `assets/bilder/projekte/BILDER.md` (Stock-Quellen) und `assets/bilder/BILDER.md` (abgeleitete
Dateien).

| Slug | Musterbüro | Handschrift |
|---|---|---|
| `musterbuero-nordkant` | kleines Wohnbau-Büro, Münster | Vollbild-Titelbild, Fraunces, Off-White & Ziegel |
| `musterstudio-lindenau` | Innenarchitektur-Studio, Hamburg | dunkel/hell im Wechsel, Cormorant & DM Sans, Messing |
| `musterbuero-steinwerk` | mittleres Büro für öffentliche Bauten, Köln | kein Titelbild, Raster + Liste + Filter, Inter & IBM Plex Mono |

**Neue Entwürfe erst nach Freigabe durch Tim verschicken**, die Seiten sind Außendarstellung.
`noindex` auf den Entwürfen nicht entfernen, solange sie erfundene Bürodaten enthalten.
