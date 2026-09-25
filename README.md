# Website
The official XPONext Website

## Tech Stack
- HTML/CSS — kein Framework, kein Build-Step
- Hosted via GitHub Pages

## Development
Dateien direkt bearbeiten, dann pushen — GitHub Pages aktualisiert sich automatisch.
Ausnahme: die generierten Seiten unter `_content/`, siehe unten.

## Generierte Seiten (`_content/`)

Die Leistungs-, Einzugsgebiet-, Kombi- und Blogseiten werden **nicht von Hand gepflegt**.
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

## Musterentwürfe (`musterentwuerfe/`)

Vollständige Muster-Websites für Architektur- und Innenarchitekturbüros, gebaut mit dem
`architect_website_creation`-Skill aus dem Repo `XPO_Agentic_Workflow`. Sie zeigen die Arbeitsweise,
ohne Kundenprojekte zu verwenden: Büros, Personen, Anschriften und Projekte sind erfunden und als
Musterangaben gekennzeichnet, die Fotografie ist Stockmaterial von Pexels.

**Nie als „Referenz" oder „umgesetztes Projekt" bezeichnen.** Beide Begriffe meinen im
Verkaufsgespräch: für einen Kunden geliefert. Erlaubt sind Musterentwurf, Muster-Website, Entwurf.

Jeder Entwurf liegt als eigenständige statische Site unter `musterentwuerfe/<slug>/` (relative
Pfade, eigene `assets/`, eigene Fonts, `noindex` auf jeder Seite, Hinweis in der Fußzeile).
Übersicht: `musterentwuerfe/index.html`, aktuell ebenfalls `noindex`.

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

**Livegang und Indexierung nur nach Freigabe durch Tim** — die Seiten sind Außendarstellung.
