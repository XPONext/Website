#!/usr/bin/env python3
"""
Baut aus den Markdown-Content-Paketen in _content/seiten_geo/ die echten HTML-Seiten
im Repo-Root: Leistungsseiten, Blogartikel samt blog/index.html und Ortsseiten.
Teil des programmatic_seo_geo-Workflows.

Die Markdown-Dateien sind die Quelle der Wahrheit für diese Seiten: HTML nicht direkt
bearbeiten, sondern die .md ändern und dieses Skript neu laufen lassen (oder build_all.py).
Beides muss committet bleiben, sonst gehen die Quellen bei einem Sitzungs-/Umgebungs-Reset
spurlos verloren (siehe _content/seiten_geo/sitemap_eintraege.md, Vorfall 2026-08-03).

Seit dem Relaunch (Oktober 2026) kommen Kopf, Kopfzeile, Fußzeile und Styles aus
_content/layout.py und css/site.css. Der Textteil einer .md kennt:
  - erster Absatz          → Kernaussage (Kasten oben, Antwort zuerst)
  - "## Überschrift"       → Zwischenüberschrift (gern als Frage)
  - "### Überschrift"      → Unterüberschrift
  - Zeilen mit "- "        → Liste, Zeilen mit "1. " → nummerierte Liste
  - Zeilen mit "|"         → Tabelle
  - "**Quelle(n):** …"     → Quellenzeile am Ende (fließt als citation ins Schema)

Ortsseiten (einzugsgebiet/) werden seit Oktober 2026 mit noindex gebaut und nicht mehr
verlinkt. Die Dateien bleiben, damit alte Links nicht ins Leere laufen.

Aufruf aus dem Repo-Root oder von überall: python3 _content/build_geo_pages.py
"""
import re, glob, os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import layout

SRC_DIR = os.path.join(_HERE, "seiten_geo")
OUT_DIR = os.path.dirname(_HERE)

# Alte Ziele, auf die Inhalte noch verlinken: werden beim Bauen umgeschrieben.
LINK_MAP = {
    "/effizienz.html": "/leistungen/ki-automatisierung.html",
    "/leistungen/zeitfresser-workshop.html": "/leistungen/ki-automatisierung.html",
    "/index.html#kontakt": "/kontakt.html",
}
# Ziele, die nicht mehr verlinkt werden (Link fällt weg, Text bleibt).
LINK_DROP = ("/musterentwuerfe/",)

ORT_LABEL = {"bonn": "Bonn", "koeln": "Köln"}

FEATURED_SLUG = "/blog/sichtbarkeit-chatgpt-google-ai-overviews-architekturbuero.html"

CLUSTER_META = {
    "Sichtbarkeit bei Bauherren & Kommunen": {
        "tag": "Sichtbarkeit",
        "desc": "Wie Architekturbüros online gefunden werden, von Google-Profil bis GEO.",
    },
    "Zeitfresser & Prozessoptimierung": {
        "tag": "Zeitfresser",
        "desc": "Wo im Büroalltag Zeit verloren geht, und wie Sie sie zurückgewinnen.",
    },
    "Kosten von Online-Marketing für Architekturbüros": {
        "tag": "Kosten",
        "desc": "Realistische Größenordnungen für Website, SEO und Google Ads.",
    },
}

STAND = "2026-10-07"

# Zeitwert-Rechner (Front Matter `rechner: true`). Rechnet nur die Eingaben des Besuchers,
# keine Annahme über Einsparungen. Logik in js/site.js, ohne JavaScript stehen die Startwerte da.
RECHNER = """<section class="calc" aria-labelledby="rechner">
            <h2 id="rechner">Was kostet Sie die Routine heute?</h2>
            <p>Schätzen Sie, wie viele Stunden Ihr Team pro Woche mit Protokollen, Mails, Angeboten und Ablage verbringt.</p>
            <div class="calc__grid">
              <label for="calc-h">Stunden pro Woche <output id="calc-h-out" for="calc-h">10</output></label>
              <input type="range" id="calc-h" min="1" max="60" step="1" value="10">
              <label for="calc-r">Stundensatz in Euro <output id="calc-r-out" for="calc-r">60</output></label>
              <input type="range" id="calc-r" min="20" max="150" step="5" value="60">
            </div>
            <p class="calc__result" aria-live="polite">Das sind rund <strong id="calc-month">2.300 €</strong> im Monat oder <strong id="calc-year">27.600 €</strong> im Jahr.</p>
            <p class="small muted">Gerechnet mit 46 Arbeitswochen im Jahr. Wie viel davon sich automatisieren lässt, klären wir in der Zeitfresser-Analyse.</p>
          </section>"""

SERVICES = [
    ("/leistungen/website-erstellung.html", "Website"),
    ("/leistungen/seo.html", "SEO"),
    ("/leistungen/geo.html", "GEO"),
    ("/leistungen/google-ads.html", "Google Ads"),
    ("/leistungen/ki-automatisierung.html", "KI-Automatisierung"),
]


def map_link(url):
    return LINK_MAP.get(url, url)


def reading_minutes(text):
    words = len(re.findall(r"\w+", text))
    return max(2, round(words / 200))


def excerpt(capsule, max_len=150):
    plain = re.sub(r'\*\*(.+?)\*\*', r'\1', capsule)
    plain = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', plain)
    if len(plain) <= max_len:
        return plain
    return plain[:max_len].rsplit(" ", 1)[0] + "…"


def parse_md(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    import yaml
    return yaml.safe_load(m.group(1)), m.group(2).strip()


def md_inline(s):
    s = s.replace("&", "&amp;")
    def link_sub(mm):
        label, url = mm.group(1), map_link(mm.group(2))
        if url in LINK_DROP or url.startswith("/einzugsgebiet/"):
            return label
        ext = url.startswith("http")
        attrs = ' rel="noopener"' if ext else ""
        return f'<a href="{url}"{attrs}>{label}</a>'
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_sub, s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    return s


def slug_id(text):
    t = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def render_table(block):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in block.strip().split("\n") if l.strip()]
    header, _sep, *body = rows
    out = ['<div class="table-wrap"><table class="content-table"><thead><tr>']
    out += [f"<th>{md_inline(h)}</th>" for h in header]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_body(body):
    """Gibt (capsule_md, html_blocks, sources_md, plain_text) zurück."""
    blocks = [b.strip() for b in re.split(r'\n\n+', body.strip()) if b.strip()]
    capsule, sources, html, plain = None, None, [], []
    for b in blocks:
        if re.match(r'^\*\*Quelle', b):
            sources = b
            continue
        if capsule is None and not b.startswith(("#", "|", "- ", "1. ")):
            capsule = b
            plain.append(b)
            continue
        if b.startswith("### "):
            t = b[4:].strip()
            html.append(f'<h3 id="{slug_id(t)}">{md_inline(t)}</h3>')
        elif b.startswith("## "):
            t = b[3:].strip()
            html.append(f'<h2 id="{slug_id(t)}">{md_inline(t)}</h2>')
        elif b.startswith("|"):
            html.append(render_table(b))
        elif all(l.startswith("- ") for l in b.split("\n")):
            items = "".join(f"<li>{md_inline(l[2:])}</li>" for l in b.split("\n"))
            html.append(f"<ul>{items}</ul>")
        elif all(re.match(r"^\d+\. ", l) for l in b.split("\n")):
            entries = [re.sub(r"^\d+\. ", "", l) for l in b.split("\n")]
            items = "".join("<li>" + md_inline(e) + "</li>" for e in entries)
            html.append(f"<ol>{items}</ol>")
        else:
            html.append(f"<p>{md_inline(b)}</p>")
        plain.append(b)
    return capsule or "", html, sources, " ".join(plain)


def parse_citations(src):
    if not src:
        return []
    return [{"@type": "CreativeWork", "name": n.strip(), "url": u.strip()}
            for n, u in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', src)]


def load_all():
    entries = {}
    for f in sorted(glob.glob(os.path.join(SRC_DIR, "**/*.html.md"), recursive=True)):
        fm, body = parse_md(f)
        entries[fm["slug"]] = (fm, body, f)
    return entries


def build_link_labels(entries):
    labels = {"/": "Startseite", "/leistungen.html": "Alle Leistungen im Überblick",
              "/kontakt.html": "Erstgespräch vereinbaren", "/geo-check.html": "Kostenloser GEO-Check",
              "/website-check.html": "Kostenloser Website-Check", "/projekte.html": "Projekte"}
    for slug, (fm, body, f) in entries.items():
        labels[slug] = fm.get("h1") or fm.get("title")
    return labels


def kind_of(slug):
    return slug.strip("/").split("/")[0]


def breadcrumbs(slug, fm):
    parts = slug.strip("/").replace(".html", "").split("/")
    crumbs = [("/", "Startseite")]
    if parts[0] == "leistungen":
        crumbs += [("/leistungen.html", "Leistungen"), (None, fm.get("kurzname") or fm["h1"])]
    elif parts[0] == "einzugsgebiet":
        ort = ORT_LABEL.get(parts[1], parts[1].title())
        crumbs += [(None, ort)] if len(parts) == 2 else [(f"/einzugsgebiet/{parts[1]}.html", ort), (None, fm["h1"])]
    elif parts[0] == "blog":
        crumbs += [("/blog/index.html", "Blog"), (None, fm["h1"])]
    return crumbs


def schemas_for(fm, slug, canonical, crumbs, citations):
    out = []
    typ = fm["seitentyp"]
    if typ == "leistungsseite":
        out.append({"@context": "https://schema.org", "@type": "Service",
                    "name": fm.get("kurzname") or fm["h1"], "serviceType": fm.get("kurzname") or fm["h1"],
                    "description": fm["meta_description"], "url": canonical,
                    "provider": layout.ORGANIZATION_REF,
                    "areaServed": {"@type": "Country", "name": "Deutschland"}})
    elif typ in ("einzugsgebiet-haupt", "einzugsgebiet-leistung"):
        ort = slug.strip("/").split("/")[1].replace(".html", "")
        out.append({"@context": "https://schema.org", "@type": "ProfessionalService",
                    "@id": layout.SITE + "/#organisation", "name": layout.FIRMA, "url": layout.SITE + "/",
                    "address": {"@type": "PostalAddress", "streetAddress": "Adrianstraße 88",
                                "addressLocality": "Bonn", "postalCode": "53227", "addressCountry": "DE"},
                    "areaServed": {"@type": "City", "name": ORT_LABEL.get(ort, ort.title())}})
    elif typ == "blogartikel":
        out.append({"@context": "https://schema.org", "@type": "Article", "headline": fm["h1"],
                    "description": fm["meta_description"], "url": canonical,
                    "datePublished": "2026-07-26", "dateModified": STAND,
                    "author": layout.ORGANIZATION_REF, "publisher": layout.ORGANIZATION_REF})
    if citations and out:
        out[0]["citation"] = citations
    out.append(layout.breadcrumb_schema(crumbs, canonical))
    return out


def cta_for(kind):
    if kind == "leistungen":
        return layout.cta_band("Passt das zu Ihrem Unternehmen? <em>Fragen Sie uns.</em>",
                               "Im Erstgespräch sehen wir uns Ihre Ausgangslage an und sagen Ihnen ehrlich, ob und wie wir helfen können.")
    return layout.cta_band("Sie möchten das für Ihr Büro angehen? <em>Sprechen wir darüber.</em>",
                           "30 Minuten, kostenlos. Danach wissen Sie, wo Sie stehen und was sich lohnt.")


def build_page(fm, body, slug, labels):
    canonical = layout.SITE + slug
    kind = kind_of(slug)
    crumbs = breadcrumbs(slug, fm)
    capsule, blocks, sources, plain = render_body(body)
    robots = "noindex, follow" if kind == "einzugsgebiet" else "index, follow"
    schemas = schemas_for(fm, slug, canonical, crumbs, parse_citations(sources))

    eyebrow = {"leistungen": "Leistung", "einzugsgebiet": "Region", "blog": fm.get("cluster", "Blog")}.get(kind, "XPONext")
    if kind == "blog":
        eyebrow = CLUSTER_META.get(fm.get("cluster"), {}).get("tag", "Blog")
    lead = f'<p class="lead">{md_inline(fm["lead"])}</p>' if fm.get("lead") else ""
    meta = ""
    if kind == "blog":
        meta = f'<p class="page-meta">{reading_minutes(plain)} Minuten Lesezeit · XPONext · aktualisiert am 7. Oktober 2026</p>'
    elif kind == "leistungen":
        meta = '<div class="btn-row"><a class="btn btn--primary" href="/kontakt.html">Erstgespräch buchen</a><a class="btn btn--secondary" href="/leistungen.html">Alle Leistungen</a></div>'

    related = []
    for link in fm.get("interne_links", []) or []:
        target = map_link(link)
        if target in LINK_DROP or target.startswith("/einzugsgebiet/"):
            continue
        related.append(f'<a href="{target}">{labels.get(target, target)}</a>')
    related_html = ""
    if related:
        related_html = f'<aside class="related"><h2>Das könnte Sie auch interessieren</h2><div class="related-grid">{"".join(related)}</div></aside>'

    sources_html = f'<p class="sources">{md_inline(sources)}</p>' if sources else ""
    active = "leistungen" if kind == "leistungen" else ""
    rechner = RECHNER if fm.get("rechner") else ""
    article = f"""<article class="prose">
          <div class="capsule">{md_inline(capsule)}</div>
          {rechner}
          {"".join(blocks)}
          {sources_html}
        </article>"""
    if kind == "leistungen":
        current = ' aria-current="page"'
        links = "".join(
            f'<li><a href="{href}"{current if href == slug else ""}>{label}</a></li>'
            for href, label in SERVICES)
        article = f"""<div class="with-aside">
        {article}
        <aside class="aside-card" aria-label="Kontakt und weitere Leistungen">
          <div class="person"><img src="/assets/team/tim.webp" alt="Tim Bünger" width="52" height="52" loading="lazy"><div><strong>Tim Bünger</strong><span>Mitgründer, Ihr Ansprechpartner</span></div></div>
          <h2>Fragen zu {fm.get("kurzname") or "dieser Leistung"}?</h2>
          <p class="small">30 Minuten, kostenlos. Sie sprechen direkt mit uns.</p>
          <a class="btn btn--primary" href="/kontakt.html">Erstgespräch buchen</a>
          <a class="text-link" href="tel:{layout.PHONE_TEL}">{layout.PHONE_DISPLAY}</a>
          <ul>{links}</ul>
        </aside>
      </div>"""

    return f"""{layout.head(fm["title"], fm["meta_description"], canonical, robots, schemas, "article" if kind == "blog" else "website")}
<body>
  {layout.header(active)}

  <main id="inhalt">
    <section class="page-hero">
      <div class="container">
        {layout.breadcrumb_html(crumbs)}
        <p class="eyebrow">{eyebrow}</p>
        <h1>{fm["h1"]}</h1>
        {lead}
        {meta}
      </div>
    </section>

    <section class="section">
      <div class="container">
        {article}
        {related_html}
      </div>
    </section>

    {cta_for(kind)}
  </main>

  {layout.footer()}
</body>
</html>
"""


def build_blog_index(entries):
    clusters = {}
    for slug, (fm, body, f) in entries.items():
        if fm["seitentyp"] == "blogartikel":
            clusters.setdefault(fm["cluster"], []).append((slug, fm, body))
    order = list(CLUSTER_META)
    canonical = layout.SITE + "/blog/index.html"
    title = "Blog für Architekturbüros | XPONext"
    desc = "Praxiswissen für Architekturbüros: Sichtbarkeit bei Auftraggebern, Zeitfresser im Büroalltag und Kosten von Online-Marketing, mit Quellen belegt."
    crumbs = [("/", "Startseite"), (None, "Blog")]
    schemas = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "description": desc, "url": canonical},
               layout.breadcrumb_schema(crumbs, canonical)]
    parts = []
    for cluster in order:
        cards = []
        for slug, fm, body in sorted(clusters.get(cluster, []), key=lambda x: x[1]["h1"]):
            capsule, _b, _s, plain = render_body(body)
            cards.append(f'''<a class="service-card" href="{slug}">
              <span class="case__tag">{CLUSTER_META[cluster]["tag"]}</span>
              <h3>{fm["h1"]}</h3>
              <p>{excerpt(capsule, 120)}</p>
              <span class="small muted">{reading_minutes(plain)} Minuten Lesezeit</span>
            </a>''')
        parts.append(f'''<div class="pillar">
          <div class="pillar__head"><div><h2>{cluster}</h2></div><p class="muted">{CLUSTER_META[cluster]["desc"]}</p></div>
          <div class="service-grid">{"".join(cards)}</div>
        </div>''')
    return f"""{layout.head(title, desc, canonical, "index, follow", schemas)}
<body>
  {layout.header("")}

  <main id="inhalt">
    <section class="page-hero">
      <div class="container">
        {layout.breadcrumb_html(crumbs)}
        <p class="eyebrow">Blog</p>
        <h1>Praxiswissen für Architekturbüros</h1>
        <p class="lead">Wie Architekturbüros online gefunden werden, wo im Büroalltag Zeit verloren geht und was Online-Marketing realistisch kostet. Jeder Artikel nennt seine Quellen.</p>
      </div>
    </section>
    <section class="section section--tight">
      <div class="container">
        {"".join(parts)}
      </div>
    </section>
    {cta_for("blog")}
  </main>

  {layout.footer()}
</body>
</html>
"""


def main():
    entries = load_all()
    labels = build_link_labels(entries)
    written = 0
    for slug, (fm, body, srcfile) in entries.items():
        out_path = os.path.join(OUT_DIR, slug.lstrip("/"))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(build_page(fm, body, slug, labels))
        written += 1
    with open(os.path.join(OUT_DIR, "blog", "index.html"), "w", encoding="utf-8") as f:
        f.write(build_blog_index(entries))
    print(f"Geschrieben: {written + 1} Dateien (inkl. blog/index.html)")


if __name__ == "__main__":
    main()
