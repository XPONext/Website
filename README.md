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
