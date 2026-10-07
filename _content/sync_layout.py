#!/usr/bin/env python3
"""
Schreibt Kopf-Bausteine, Kopfzeile und Fußzeile aus _content/layout.py in die
handgebauten Seiten. Ersetzt wird nur, was zwischen diesen Markierungen steht:

  <!-- @layout:head -->    … <!-- /@layout:head -->     (Icons, Styles, Analytics)
  <!-- @layout:header -->  … <!-- /@layout:header -->   (Kopfzeile, aktiver Menüpunkt aus <body data-nav="…">)
  <!-- @layout:footer -->  … <!-- /@layout:footer -->   (Fußzeile und Cookie-Banner)
  <!-- @layout:faq-schema --> … <!-- /@layout:faq-schema -->  (optional: FAQPage-Schema,
                             erzeugt aus den sichtbaren Fragen <details> in <div class="faq">)

Alles andere in den Seiten bleibt von Hand bearbeitbar. Das FAQ-Schema entsteht immer aus
dem sichtbaren Text, damit Schema und Seite nicht auseinanderlaufen.
Aufruf: python3 _content/sync_layout.py   (oder über build_all.py)
"""
import html as htmllib
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HANDGEBAUT = [
    "index.html", "leistungen.html", "projekte.html", "ueber-uns.html", "kontakt.html",
    "website-check.html", "geo-check.html", "impressum.html", "datenschutz.html", "agb.html",
    "404.html", "musterentwuerfe/index.html",
]


def replace_block(html, name, content, path):
    pattern = re.compile(r"(<!-- @layout:%s -->)(.*?)(<!-- /@layout:%s -->)" % (name, name), re.S)
    if not pattern.search(html):
        raise SystemExit(f"{path}: Markierung @layout:{name} fehlt")
    return pattern.sub(lambda m: m.group(1) + "\n  " + content + "\n  " + m.group(3), html, count=1)


def plain(fragment):
    text = re.sub(r"<li>", " ", fragment)
    text = re.sub(r"<[^>]+>", " ", text)
    text = htmllib.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def faq_schema(html):
    faq = re.search(r'<div class="faq"[^>]*>(.*?)</div>\s*<!-- /faq -->', html, re.S)
    if not faq:
        return None
    entities = []
    for q, a in re.findall(r"<summary>(.*?)</summary>\s*<div class=\"answer\">(.*?)</div>\s*</details>", faq.group(1), re.S):
        entities.append({"@type": "Question", "name": plain(q),
                         "acceptedAnswer": {"@type": "Answer", "text": plain(a)}})
    if not entities:
        return None
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def main():
    for rel in (sys.argv[1:] or HANDGEBAUT):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print("fehlt, übersprungen:", rel)
            continue
        html = open(path, encoding="utf-8").read()
        m = re.search(r'<body[^>]*data-nav="([^"]*)"', html)
        active = m.group(1) if m else ""
        new = replace_block(html, "head", layout.HEAD_COMMON, rel)
        new = replace_block(new, "header", layout.header(active), rel)
        new = replace_block(new, "footer", layout.footer(), rel)
        if "<!-- @layout:faq-schema -->" in new:
            schema = faq_schema(new)
            if not schema:
                raise SystemExit(f"{rel}: FAQ-Schema-Markierung vorhanden, aber keine Fragen gefunden")
            new = replace_block(new, "faq-schema", schema, rel)
        if new != html:
            open(path, "w", encoding="utf-8").write(new)
            print("aktualisiert:", rel)
        else:
            print("unverändert:", rel)


if __name__ == "__main__":
    main()
