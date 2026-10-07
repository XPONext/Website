#!/usr/bin/env python3
"""
Baut die ganze Website in einem Lauf:
  1. Leistungs-, Blog- und Ortsseiten aus _content/seiten_geo/      (build_geo_pages.py)
  2. Branchenseiten unter /fuer/ aus _content/landingpages/         (build_landingpages.py)
  3. Kopf, Kopfzeile, Fußzeile und FAQ-Schema in die handgebauten Seiten (sync_layout.py)
  4. sitemap.xml aus allen Seiten mit robots "index"
  5. Liste der offenen Platzhalter (data-ph). Vor dem Livegang muss sie leer sein,
     oder die Platzhalter-Blöcke werden bewusst entfernt.

Aufruf: python3 _content/build_all.py            (baut alles, listet Platzhalter)
        python3 _content/build_all.py --streng   (Exit 1, solange Platzhalter da sind)
"""
import datetime, glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = "https://www.xponext.de"


def run(script):
    subprocess.run([sys.executable, os.path.join(HERE, script)], check=True)


def all_pages():
    for path in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(path, ROOT)
        if rel.startswith(("_", ".")) or "/_" in rel:
            continue
        yield rel, path


def build_sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for rel, path in sorted(all_pages()):
        html = open(path, encoding="utf-8").read()
        robots = re.search(r'<meta name="robots" content="([^"]+)"', html)
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        if not robots or "noindex" in robots.group(1) or not canonical:
            continue
        loc = canonical.group(1)
        if not loc.startswith(SITE):
            continue
        depth = loc[len(SITE):].strip("/").count("/")
        prio = "1.0" if loc == SITE + "/" else ("0.8" if depth <= 1 and "/blog/" not in loc else "0.6")
        urls.append((loc, prio))
    seen, lines = set(), ['<?xml version="1.0" encoding="UTF-8"?>',
                          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, prio in sorted(urls, key=lambda u: (u[1] != "1.0", u[0])):
        if loc in seen:
            continue
        seen.add(loc)
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{prio}</priority></url>")
    lines.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"sitemap.xml: {len(seen)} Seiten")


def list_placeholders():
    found = []
    for rel, path in sorted(all_pages()):
        for key in re.findall(r'data-ph="([^"]+)"', open(path, encoding="utf-8").read()):
            found.append((rel, key))
    if found:
        print(f"\nOffene Platzhalter: {len(found)}")
        last = None
        for rel, key in found:
            if rel != last:
                print(f"  {rel}")
                last = rel
            print(f"    - {key}")
    else:
        print("\nKeine Platzhalter mehr.")
    return found


if __name__ == "__main__":
    run("build_geo_pages.py")
    run("build_landingpages.py")
    run("sync_layout.py")
    build_sitemap()
    open_ph = list_placeholders()
    if "--streng" in sys.argv and open_ph:
        sys.exit(1)
