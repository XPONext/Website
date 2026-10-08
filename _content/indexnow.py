"""Meldet geänderte Seiten per IndexNow an Bing (und alle anderen IndexNow-Suchmaschinen).

Aufruf:
  python3 _content/indexnow.py --alle               # alle Seiten aus sitemap.xml
  python3 _content/indexnow.py index.html blog/x.html  # nur diese Dateien

Gemeldet werden nur Seiten, die in sitemap.xml stehen (also indexierbar sind).
Läuft automatisch nach jedem Push nach main, siehe .github/workflows/indexnow.yml.
Der Schlüssel liegt als <KEY>.txt im Wurzelordner und muss online erreichbar bleiben.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.xponext.de"
KEY = "f9b9752001c4c27cae0eea23a35fae11"
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    xml = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def url_for(path):
    """Datei → öffentliche Adresse über den canonical-Link der Seite."""
    full = os.path.join(ROOT, path)
    if not path.endswith(".html") or not os.path.isfile(full):
        return None
    m = re.search(r'<link rel="canonical" href="([^"]+)"', open(full, encoding="utf-8").read())
    return m.group(1) if m else None


def main(args):
    known = sitemap_urls()
    if not args:
        print(__doc__)
        return 1
    if "--alle" in args or "sitemap.xml" in args:
        urls = known
    else:
        urls = [u for u in (url_for(p) for p in args) if u in known]
    urls = sorted(set(urls))
    if not urls:
        print("IndexNow: keine indexierbaren Seiten geändert, nichts zu melden.")
        return 0

    body = json.dumps({
        "host": SITE.split("//")[1],
        "key": KEY,
        "keyLocation": f"{SITE}/{KEY}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status = r.status
    except urllib.error.HTTPError as e:
        status = e.code
    # 200 = angenommen, 202 = angenommen, Schlüssel wird noch geprüft
    print(f"IndexNow: {len(urls)} Seite(n) gemeldet, Antwort {status}")
    for u in urls:
        print("  " + u)
    return 0 if status in (200, 202) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
