#!/usr/bin/env python3
"""
Baut die Branchenseiten unter /fuer/<slug>/ aus den Datendateien in _content/landingpages/.

Eine Datei je Branche (YAML). Neue Kampagne = neue Datei kopieren, Texte anpassen, bauen.
Seiten im Test stehen auf `index: false`: Sie bekommen noindex, stehen nicht in der
Sitemap und sind nirgends verlinkt, nur aus der Kampagne selbst (Signatur, Folgemail,
Video-Mail). Trägt eine Hypothese, `index: true` setzen und auf der Startseite verlinken.

Aufbau der Seite (Reihenfolge fest, Vorbild: Branchenseiten von stark.marketing):
  Hero → Situationen aus dem Alltag → Was wir tun (Schritte) → Programme/Kontrolle/Daten
  → Beleg → Angebot → FAQ (optional) → Ansprechpartner → Abschluss

Felder siehe _content/landingpages/reisebueros.yaml. Texte immer in Sie-Form, nur belegte
Zahlen, die Überschrift wiederholt das Versprechen der Kampagnen-Mail.

Aufruf: python3 _content/build_landingpages.py   (oder über build_all.py)
"""
import glob, html, json, os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import layout
import yaml

ROOT = os.path.dirname(_HERE)
SRC = os.path.join(_HERE, "landingpages")


CHECK = ('<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5 10.5l3 3 7-7" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TRUST_ROW = ('<ul class="trust-row">'
             '<li><span class="badge-icon" aria-hidden="true"></span>Google Ads zertifiziert</li>'
             f'<li>{CHECK}Kunden in ganz Deutschland</li>'
             f'<li>{CHECK}Antwort innerhalb von 24 Stunden an Werktagen</li></ul>')


def inline(text):
    """Einfaches Inline-Format: **fett** und [Text](Link). Rest wird escaped."""
    import re
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a class="inline-link" href="\2">\1</a>', t)
    return t


def ph(text, key, cls="ph ph--block"):
    return f'<!-- PLATZHALTER-BLOCK: {html.escape(key)} -->\n        <div class="{cls}" data-ph="{html.escape(key)}">{inline(text)}</div>'


def section_head(eyebrow, title, lead=""):
    lead_html = f'<p class="lead">{inline(lead)}</p>' if lead else ""
    return f'<div class="section-head"><p class="eyebrow">{eyebrow}</p><h2>{inline(title)}</h2>{lead_html}</div>'


def build(d):
    slug = d["slug"]
    url = f"{layout.SITE}/fuer/{slug}/"
    robots = "index, follow" if d.get("index") else "noindex, follow"
    crumbs = [("/", "Startseite"), (None, d["kurzname"])]
    schemas = [layout.breadcrumb_schema(crumbs, url)]
    if d.get("index"):
        schemas.insert(0, {"@context": "https://schema.org", "@type": "Service", "name": d["service_name"],
                           "description": d["meta_description"], "url": url, "provider": layout.ORGANIZATION_REF,
                           "audience": {"@type": "BusinessAudience", "name": d["kurzname"]},
                           "areaServed": {"@type": "Country", "name": "Deutschland"}})
    faq = d.get("faq") or []
    if faq and d.get("index"):
        schemas.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["frage"], "acceptedAnswer": {"@type": "Answer", "text": f["antwort"]}}
            for f in faq]})

    kontakt = f"/kontakt.html?quelle={slug}"
    parts = []

    # Hero
    parts.append(f"""<section class="page-hero">
      <div class="container">
        {layout.breadcrumb_html(crumbs)}
        <p class="eyebrow">{d["eyebrow"]}</p>
        <h1>{inline(d["h1"])}</h1>
        <p class="lead">{inline(d["lead"])}</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{kontakt}">Erstgespräch buchen</a>
          <a class="btn btn--secondary" href="tel:{layout.PHONE_TEL}">{layout.PHONE_DISPLAY}</a>
        </div>
        <p class="cta-note">{inline(d.get("cta_note", "30 Minuten, kostenlos und unverbindlich. Sie sprechen direkt mit Tim Bünger, nicht mit einem Vertriebsteam."))}</p>
        {TRUST_ROW}
      </div>
    </section>""")

    # Situationen
    cards = "".join(f'<article class="situation"><h3>{inline(s["titel"])}</h3><p>{inline(s["text"])}</p></article>'
                    for s in d["situationen"])
    note = f'<p class="small muted" style="margin-top:1.2rem">{inline(d["situationen_quelle"])}</p>' if d.get("situationen_quelle") else ""
    parts.append(f"""<section class="section section--soft">
      <div class="container">
        {section_head("Aus dem Alltag", d["situationen_titel"], d.get("situationen_lead", ""))}
        <div class="situations">{cards}</div>
        {note}
      </div>
    </section>""")

    # Was wir tun
    steps = "".join(f'<li><h3>{inline(s["titel"])}</h3><p>{inline(s["text"])}</p></li>' for s in d["schritte"])
    parts.append(f"""<section class="section">
      <div class="container">
        {section_head("Was wir tun", d["schritte_titel"], d.get("schritte_lead", ""))}
        <ol class="steps">{steps}</ol>
      </div>
    </section>""")

    # Programme, Kontrolle, Daten
    if d.get("einwaende"):
        tags = ""
        if d.get("programme"):
            tags = '<div class="tags">' + "".join(f'<span class="tag">{html.escape(t)}</span>' for t in d["programme"]) + "</div>"
        items = "".join(f'<div class="objection"><h3>{inline(e["titel"])}</h3><p>{inline(e["text"])}</p></div>'
                        for e in d["einwaende"])
        parts.append(f"""<section class="section section--soft">
      <div class="container">
        {section_head("Bevor Sie fragen", d.get("einwaende_titel", "Die drei Fragen, die wir am häufigsten hören"))}
        <div class="objections">{items}</div>
        {tags}
      </div>
    </section>""")

    # Beleg und Angebot
    beleg = d.get("beleg", {})
    beleg_html = inline(beleg["text"]) if beleg.get("text") else ""
    beleg_ph = ph(beleg["platzhalter"], f"Beleg {slug}") if beleg.get("platzhalter") else ""
    angebot = d.get("angebot", {})
    angebot_html = f'<p>{inline(angebot["text"])}</p>' if angebot.get("text") else ""
    angebot_ph = ph(angebot["platzhalter"], f"Angebot {slug}") if angebot.get("platzhalter") else ""
    parts.append(f"""<section class="section">
      <div class="container split split--top">
        <div>
          {section_head("Beleg", beleg.get("titel", "Was wir schon gemacht haben"))}
          {f'<p>{beleg_html}</p>' if beleg_html else ''}
          {beleg_ph}
        </div>
        <div>
          {section_head("Angebot", angebot.get("titel", "So starten wir"))}
          {angebot_html}
          {angebot_ph}
        </div>
      </div>
    </section>""")

    # FAQ
    if faq:
        items = "".join(f'<details><summary>{inline(f["frage"])}</summary><div class="answer"><p>{inline(f["antwort"])}</p></div></details>'
                        for f in faq)
        parts.append(f"""<section class="section section--soft">
      <div class="container container--narrow">
        {section_head("FAQ", "Häufige Fragen")}
        <div class="faq">{items}</div>
      </div>
    </section>""")

    # Weiterführende Links (nur indexierte Seiten brauchen das für Google)
    if d.get("links"):
        links = "".join(f'<a href="{l["href"]}">{inline(l["text"])}</a>' for l in d["links"])
        parts.append(f"""<section class="section section--tight">
      <div class="container">
        <aside class="related" style="margin-top:0"><h2>Mehr zum Thema</h2><div class="related-grid">{links}</div></aside>
      </div>
    </section>""")

    cta = d["abschluss"]
    band = layout.cta_band(cta["titel"], cta["text"]).replace('href="/kontakt.html"', f'href="{kontakt}"')

    return f"""{layout.head(d["title"], d["meta_description"], url, robots, schemas)}
<body>
  {layout.header("")}

  <main id="inhalt">
    {"".join(parts)}
    {band}
  </main>

  {layout.footer()}
</body>
</html>
"""


def main():
    count = 0
    for f in sorted(glob.glob(os.path.join(SRC, "*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        out_dir = os.path.join(ROOT, "fuer", d["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(build(d))
        count += 1
        print(f"/fuer/{d['slug']}/  ({'index' if d.get('index') else 'noindex'})")
    print(f"Geschrieben: {count} Branchenseiten")


if __name__ == "__main__":
    main()
