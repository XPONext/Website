#!/usr/bin/env python3
"""Generator für den Musterentwurf Musterbüro Nordkant.

Erzeugt alle HTML-Seiten aus einem Datenmodell, damit Kopf- und Fußzeile auf
jeder Seite identisch sind und die relativen Pfade je Ordnertiefe stimmen
(die Seite läuft lokal unter / und live unter /musterentwuerfe/musterbuero-nordkant/).

Aufruf:  python3 build.py [--probe]
--probe  schreibt nur index.html mit Kopfzeile, Hero und Intro (Hero-Probe).
"""
import sys
from pathlib import Path
from PIL import Image

SITE = Path("/Users/timbunger/Desktop/XPONext/Website XPO/Website/musterentwuerfe/musterbuero-nordkant")
URL = "https://www.xponext.de/musterentwuerfe/musterbuero-nordkant"
ROBOTS = "noindex, follow"
NAME = "Musterbüro Nordkant"
JAHR = "2026"
TEL = "0251 000000"
TEL_INTL = "+49251000000"
MAIL = "info@musterbuero-nordkant.de"

PROBE = "--probe" in sys.argv

_masse = {}
def masse(rel):
    """Echte Pixelmaße einer Bilddatei unter assets/bilder/."""
    if rel not in _masse:
        with Image.open(SITE / "assets" / "bilder" / rel) as im:
            _masse[rel] = im.size
    return _masse[rel]

def img(rel, alt, depth, lazy=True, prio=False, sizes=None, srcset=None):
    w, h = masse(rel)
    a = [f'src="{p(depth)}assets/bilder/{rel}"', f'alt="{alt}"', f'width="{w}"', f'height="{h}"']
    if srcset:
        a.append('srcset="' + ", ".join(f"{p(depth)}assets/bilder/{r} {ww}w" for r, ww in srcset) + '"')
    if sizes:
        a.append(f'sizes="{sizes}"')
    if prio:
        a.append('fetchpriority="high"')
    elif lazy:
        a.append('loading="lazy"')
    return "<img " + " ".join(a) + ">"

def p(depth):
    return "../" * depth

# ---------------------------------------------------------------- Projekte
PROJEKTE = [
    dict(slug="haus-am-deich", titel="Haus am Deich", ort="Telgte", jahr="2024",
         typ="Neubau Einfamilienhaus", leistung="Neubau, Holzrahmenbau", lp="1 bis 8", flaeche="185 m²",
         satz="Ein Holzhaus hinter dem Deich, für drei Generationen.",
         kachel="kacheln/haus-am-deich.webp",
         bilder=[("projekte/haus-am-deich-01.webp", "Zweigeschossiges Wohnhaus mit Holzfassade, hellem Naturstein und Flachdach, davor Rasen und ein flaches Wasserbecken"),
                 ("projekte/haus-am-deich-03.webp", "Holzterrasse mit dunkler Pergola vor einem anthrazitfarbenen Baukörper zwischen Birken"),
                 ("projekte/haus-am-deich-02.webp", "Wohnhäuser mit Holzbalkonen und Nadelgehölzen in einem terrassierten Garten")],
         text=["Das Grundstück liegt am Rand von Telgte, wo die Ems in den Wiesen verschwindet. Die Bauherren, ein Paar mit den Eltern im Haus, wollten zwei Wohnungen unter einem Dach, die sich später wieder zu einer zusammenlegen lassen.",
               "Das Haus ist ein Holzrahmenbau mit Lärchenschalung und einem Sockel aus hellem Naturstein. Die Wohnräume öffnen sich nach Süden zum Garten, die Haustechnik liegt in einem gemeinsamen Kern. Jede Wohnung hat einen eigenen Eingang."],
         beschreibung="Haus am Deich in Telgte: Neubau eines Einfamilienhauses in Holzrahmenbau mit zwei Wohnungen, fertiggestellt 2024. Musterbüro Nordkant, Münster."),
    dict(slug="hofstelle-havixbeck", titel="Umbau Hofstelle", ort="Havixbeck", jahr="2023",
         typ="Sanierung und Umbau", leistung="Umbau und Sanierung", lp="1 bis 8", flaeche="240 m²",
         satz="Ein Backsteinhof, der zum Wohnhaus wird und seine Tenne behält.",
         kachel="kacheln/hofstelle.webp",
         bilder=[("projekte/hofstelle-03.webp", "Treppenhaus mit weiß gestrichener Holzdecke, Holzgeländer und grün gestrichener Treppe"),
                 ("projekte/hofstelle-02.webp", "Ausgebautes Dachgeschoss mit sichtbarem Backsteinpfeiler, Dachfenstern und hellem Holzboden"),
                 ("projekte/hofstelle-01.webp", "Landhausküche mit Kochinsel aus Holz, weißen Schränken und drei Pendelleuchten")],
         text=["Die Hofstelle aus den 1920er Jahren stand acht Jahre leer. Das Mauerwerk war gesund, das Dach nicht. Wir haben den Dachstuhl ertüchtigt, das Dachgeschoss als offenen Raum unter den Sparren ausgebaut und die alte Tenne zum Wohnraum mit Küche gemacht.",
               "Neue Öffnungen sitzen dort, wo früher die Stalltüren waren. Die Backsteinpfeiler bleiben sichtbar und tragen weiter, die Treppe ins Dachgeschoss ist aus heimischer Eiche."],
         beschreibung="Umbau Hofstelle in Havixbeck: Sanierung eines Backsteinhofs zum Wohnhaus mit ausgebautem Dachgeschoss, fertiggestellt 2023. Musterbüro Nordkant."),
    dict(slug="anbau-hiltrup", titel="Anbau Gartenhaus", ort="Münster-Hiltrup", jahr="2023",
         typ="Anbau", leistung="Anbau an den Bestand", lp="1 bis 8", flaeche="45 m² Erweiterung",
         satz="Ein gläserner Raum zwischen Haus und Garten, zu jeder Jahreszeit.",
         kachel="kacheln/gartenhaus.webp",
         bilder=[("projekte/gartenhaus-03.webp", "Anbau mit grün verschaltem Giebel und raumhoher Verglasung, davor Bambus und Rasen"),
                 ("projekte/gartenhaus-01.webp", "Wohnhaus mit verglastem Terrassenanbau und Gartenmöbeln, im Vordergrund Rasen und ein roter Ahorn"),
                 ("projekte/gartenhaus-02.webp", "Gewächshaus aus Holz und Glas in einem Garten mit Terrakottaplatten und Topfpflanzen")],
         text=["Das Siedlungshaus aus den 1960er Jahren hatte eine Küche mit Blick auf die Garage und keinen Zugang zum Garten. Der Anbau setzt sich als eigener Baukörper mit Satteldach neben das Haus und öffnet sich mit raumhoher Verglasung nach Süden.",
               "Innen liegt jetzt der Ess- und Wohnraum, das alte Haus behält seine Zimmer. Fußbodenheizung und außenliegender Sonnenschutz machen den Raum das ganze Jahr nutzbar."],
         beschreibung="Anbau Gartenhaus in Münster-Hiltrup: Erweiterung eines Siedlungshauses um einen verglasten Wohnraum zum Garten, fertiggestellt 2023. Musterbüro Nordkant."),
    dict(slug="wohnhaus-kreuzviertel", titel="Wohnhaus Kreuzviertel", ort="Münster", jahr="2022",
         typ="Neubau Stadthaus", leistung="Neubau", lp="1 bis 8", flaeche="160 m²",
         satz="Ein Stadthaus in Backstein auf sieben Metern Breite.",
         kachel="kacheln/kreuzviertel.webp",
         bilder=[("projekte/kreuzviertel-02.webp", "Drei giebelständige Stadthäuser aus dunklem und rotem Backstein mit schmalen Hochfenstern unter blauem Himmel"),
                 ("projekte/kreuzviertel-03.webp", "Rotbraune Stadthausfassade mit Balkonen und weißen Fenstern, von unten fotografiert"),
                 ("projekte/kreuzviertel-01.webp", "Dreigeschossige Stadthäuser mit Flachdach, Holzverkleidung und großen Fenstern hinter Bäumen")],
         text=["Sieben Meter Breite zwischen zwei Nachbargiebeln, dahinter ein tiefer Garten. Das Haus nimmt die Traufhöhe der Straße auf und schließt die Lücke mit einer Fassade aus rotbraunem Backstein, wie er das Kreuzviertel prägt.",
               "Innen liegen die Räume über drei Geschosse übereinander, mit einer offenen Treppe an der Brandwand. Die Bauherren wollten wenig Flur und viel Raumhöhe. Beides ist geblieben."],
         beschreibung="Wohnhaus Kreuzviertel in Münster: Neubau eines Stadthauses in Backstein auf einem sieben Meter breiten Grundstück, fertiggestellt 2022. Musterbüro Nordkant."),
    dict(slug="aufstockung-greven", titel="Aufstockung Reihenhaus", ort="Greven", jahr="2022",
         typ="Aufstockung", leistung="Aufstockung in Holzbauweise", lp="1 bis 8", flaeche="60 m² Dachgeschoss",
         satz="Ein neues Geschoss aus Holz, in vier Wochen aufgesetzt.",
         kachel="kacheln/aufstockung.webp",
         bilder=[("projekte/aufstockung-03.webp", "Ausgebautes Dachgeschoss mit Dachflächenfenstern, weißer Decke und Eichenparkett"),
                 ("projekte/aufstockung-01.webp", "Blick nach oben in ein Oberlicht, umgeben von Holzlamellen"),
                 ("projekte/aufstockung-02.webp", "Offener Dachraum mit Dachfenstern, Holzboden und sichtbaren Balken")],
         text=["Die Familie war auf drei Kinder gewachsen, das Grundstück nicht. Statt umzuziehen, haben wir das Flachdach des Reihenmittelhauses durch ein Dachgeschoss in Holzbauweise ersetzt.",
               "Die Elemente wurden vorgefertigt und in vier Wochen montiert, die Familie blieb während der Bauzeit im Haus. Unter dem neuen Dach liegen zwei Kinderzimmer und ein Bad, ein Oberlicht bringt Tageslicht bis ins Treppenhaus."],
         beschreibung="Aufstockung Reihenhaus in Greven: neues Dachgeschoss in vorgefertigter Holzbauweise, montiert in vier Wochen, fertiggestellt 2022. Musterbüro Nordkant."),
    dict(slug="haus-im-wald", titel="Haus im Wald", ort="Nottuln", jahr="2021",
         typ="Neubau Einfamilienhaus", leistung="Neubau", lp="1 bis 8", flaeche="150 m²",
         satz="Ein Haus zwischen Kiefern, mit Türen nach allen Seiten.",
         kachel="kacheln/haus-im-wald.webp",
         bilder=[("projekte/haus-im-wald-01.webp", "Zweigeschossiges Wohnhaus mit Holzfassade im Obergeschoss und dunklem Ziegelsockel zwischen Kiefern"),
                 ("projekte/haus-im-wald-02.webp", "Eingeschossiger grauer Baukörper mit raumhohen Fenstern und Pergola am Waldrand"),
                 ("projekte/haus-im-wald-03.webp", "Vertikale Holzschalung mit auskragendem Obergeschoss im Abendlicht")],
         text=["Das Grundstück am Waldrand von Nottuln war lange unbebaut, weil kein Haus zwischen die Kiefern passen wollte. Der Entwurf folgt den Bäumen: zwei versetzt gestapelte Geschosse, unten dunkler Ziegel, oben Holz, mit Flachdach und Fenstern in alle Richtungen.",
               "Jedes Zimmer im Erdgeschoss hat eine Tür in den Garten. Geheizt wird mit einer Wärmepumpe, das Dach trägt eine Photovoltaikanlage. Die Kiefern stehen noch alle."],
         beschreibung="Haus im Wald in Nottuln: Neubau eines Einfamilienhauses mit Holzfassade und Ziegelsockel zwischen Kiefern, fertiggestellt 2021. Musterbüro Nordkant, Münster."),
]
STARTSEITE_KACHELN = ["haus-am-deich", "hofstelle-havixbeck", "anbau-hiltrup", "haus-im-wald"]

# ---------------------------------------------------------------- Rahmen
def head(depth, title, desc, pfad, og_image=True):
    assert len(title) <= 65, (title, len(title))
    assert len(desc) <= 160, (desc, len(desc))
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{URL}/{pfad}">
<meta name="robots" content="{ROBOTS}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="de_DE">
<meta property="og:image" content="{URL}/assets/bilder/og.jpg">
<link rel="icon" href="{p(depth)}assets/bilder/icon.svg" type="image/svg+xml">
<link rel="preload" href="{p(depth)}assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p(depth)}assets/css/basis.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>

<a class="sprung" href="#inhalt">Zum Inhalt springen</a>
"""

NAV = [("projekte/", "Projekte"), ("leistungen/", "Leistungen"), ("buero/", "Büro"), ("kontakt/", "Kontakt")]

def header(depth, aktiv):
    def li(pfad, text):
        cur = ' aria-current="page"' if pfad == aktiv else ""
        return f'        <li><a href="{p(depth)}{pfad}"{cur}>{text}</a></li>'
    links = "\n".join(li(*n) for n in NAV[:2])
    rechts = "\n".join(li(*n) for n in NAV[2:])
    return f"""<!-- Kopfzeile: helenhard-no-F1 geteilte Navigation mit zentrierter Wortmarke,
     helenhard-no-F12 Mobile-Schalter als Text-Button -->
<header class="kopf">
  <div class="kopf__inhalt inhalt">
    <a class="marke" href="{p(depth) or './'}" aria-label="{NAME}, zur Startseite">{NAME}</a>
    <button class="kopf__schalter" type="button" aria-expanded="false" aria-controls="hauptnavigation">Menü</button>
    <nav class="kopf__nav" id="hauptnavigation" aria-label="Hauptnavigation">
      <ul class="reiter reiter--links">
{links}
      </ul>
      <ul class="reiter reiter--rechts">
{rechts}
      </ul>
    </nav>
  </div>
</header>

<main id="inhalt">
"""

def footer(depth, jsonld=False):
    ld = ""
    if jsonld:
        ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ArchitectOffice",
  "@id": "{URL}/#buero",
  "name": "{NAME}",
  "url": "{URL}/",
  "email": "{MAIL}",
  "telephone": "{TEL_INTL}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Musterstraße 1",
    "postalCode": "48155",
    "addressLocality": "Münster",
    "addressCountry": "DE"
  }},
  "areaServed": ["Münster", "Münsterland"]
}}
</script>
"""
    return f"""
</main>

<!-- Fußzeile: helenhard-no-F13 Standortblock (Ort kursiv, Adresse, Telefon), hell auf Fläche -->
<footer class="fuss">
  <div class="inhalt">
    <div class="fuss__raster">
      <div>
        <p class="fuss__ort">Münster</p>
        <p>{NAME}<br>Musterstraße 1<br>48155 Münster</p>
        <p style="margin-top:0.75rem"><a href="tel:{TEL_INTL}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div>
        <p class="fuss__titel">Navigation</p>
        <ul class="fuss__liste">
          <li><a href="{p(depth)}projekte/">Projekte</a></li>
          <li><a href="{p(depth)}leistungen/">Leistungen</a></li>
          <li><a href="{p(depth)}buero/">Büro</a></li>
          <li><a href="{p(depth)}kontakt/">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <p class="fuss__titel">Rechtliches</p>
        <ul class="fuss__liste">
          <li><a href="{p(depth)}impressum/">Impressum</a></li>
          <li><a href="{p(depth)}datenschutz/">Datenschutz</a></li>
        </ul>
      </div>
    </div>
    <div class="fuss__schluss">
      <p>© {JAHR} {NAME}</p>
      <p>Mitglieder der Architektenkammer Nordrhein-Westfalen</p>
    </div>
    <p class="demo-hinweis">Musterentwurf von XPONext (xponext.de). Büro, Personen und Projekte sind erfunden, die Fotografie ist Stockmaterial.</p>
  </div>
</footer>

<script src="{p(depth)}assets/js/basis.js" defer></script>
{ld}</body>
</html>
"""

def schreiben(pfad, inhalt):
    ziel = SITE / pfad
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(inhalt, encoding="utf-8")
    print("geschrieben:", pfad)

def kachel(pr, depth, stufe="h3"):
    return f"""      <li class="kachel">
        <a href="{p(depth)}projekte/{pr['slug']}/">
          <{stufe} class="kachel__titel">{pr['titel']}</{stufe}>
          <div class="kachel__bild">{img(pr['kachel'], pr['bilder'][0][1], depth, sizes="(max-width: 720px) 100vw, 611px")}</div>
          <p class="kachel__satz">{pr['satz']}</p>
        </a>
      </li>"""

# ---------------------------------------------------------------- Startseite
def startseite():
    d = 0
    hero = PROJEKTE[-1]
    teile = [head(d, "Musterbüro Nordkant, Münster: Wohnhäuser im Münsterland",
                  "Architekturbüro in Münster für Neubau, Umbau und Anbau von Wohnhäusern im Münsterland. Sechs Projekte, vier Leute, Entwurf und Bauleitung aus einer Hand.", ""),
             header(d, None)]
    teile.append(f"""
  <!-- Hero: helenhard-no-F2 textfrei über die erste Bildschirmhöhe, randlos, stehendes Bild -->
  <div class="hero">
    {img("projekte/hero.webp", "Zweigeschossiges Wohnhaus mit Holzfassade im Obergeschoss und dunklem Ziegelsockel zwischen Kiefern, davor eine Rasenfläche", d, lazy=False, prio=True, sizes="100vw", srcset=[("projekte/hero-960.webp", 960), ("projekte/hero.webp", 1440), ("projekte/hero-1920.webp", 1920)])}
  </div>
  <!-- Bildzeile: big-dk-F4 Ort in Versalien, verlinkt auf das Projekt -->
  <div class="inhalt bildzeile">
    <a href="projekte/{hero['slug']}/">{hero['titel']} · {hero['ort']} · {hero['jahr']}</a>
  </div>

  <!-- Intro: pietboon-com-F15 zentrierter Block mit Chevron-Linkliste zu den Leistungen -->
  <section class="sektion">
    <div class="inhalt intro">
      <h1>Wohnhäuser im Münsterland: Neubau, Umbau und Anbau für Menschen, die lange darin leben wollen.</h1>
      <p>Musterbüro Nordkant ist ein Büro mit vier Personen in Münster. Wir planen mit wenig Material, viel Licht und Grundrissen, die sich mit dem Leben ändern können.</p>
      <ul class="chevrons">
        <li><a href="leistungen/#neubau">Neubau</a></li>
        <li><a href="leistungen/#umbau">Umbau</a></li>
        <li><a href="leistungen/#anbau">Anbau</a></li>
        <li><a href="leistungen/#bauberatung">Bauberatung</a></li>
      </ul>
    </div>
  </section>
""")
    if not PROBE:
        kacheln = "\n".join(kachel(pr, d) for pr in PROJEKTE if pr["slug"] in STARTSEITE_KACHELN)
        teile.append(f"""
  <!-- Projekte: helenhard-no-F7 Kacheln, Titel über dem Bild, kursiver Satz darunter -->
  <section class="sektion" aria-labelledby="projekte-titel">
    <div class="inhalt">
      <div class="sektion__kopf">
        <p class="label">Projekte</p>
        <h2 id="projekte-titel">Vier Häuser aus Telgte, Havixbeck, Hiltrup und Nottuln</h2>
      </div>
      <ul class="raster-projekte" style="list-style:none;padding:0">
{kacheln}
      </ul>
      <p class="raster-projekte__mehr"><a href="projekte/">Alle sechs Projekte</a></p>
    </div>
  </section>

  <!-- Büro-Statement: pietboon-com-F6 versetzter Farbkasten, Bild überlappt den Kasten -->
  <section class="sektion statement-sektion" aria-labelledby="buero-titel">
    <div class="inhalt statement">
      <div class="statement__kasten">
        <p class="label">Büro</p>
        <h2 id="buero-titel">Zwei Partner, vier Leute, ein Tisch in Münster</h2>
        <p>Zwei Partner führen das Büro seit 2016 in Münster. Eine Architektin und ein Bauzeichner arbeiten an jedem Projekt mit, vom ersten Gespräch bis zur Abnahme. Entwurf und Bauleitung kommen aus einer Hand, weil sich beides nicht trennen lässt.</p>
        <p class="statement__mehr"><a href="buero/">Mehr über das Büro</a></p>
      </div>
      <div class="statement__bild">
        {img("statement.webp", "Blick nach oben in ein Oberlicht, umgeben von Holzlamellen", d, sizes="(max-width: 720px) 82vw, 500px")}
      </div>
    </div>
  </section>

  <!-- Kontakt-Aufforderung: pietboon-com-F2 Kasten auf Fläche, Akzent nur auf dem Button -->
  <section class="sektion" aria-labelledby="kontakt-titel">
    <div class="inhalt kontakt">
      <div class="kontakt__kasten">
        <p class="label">Kontakt</p>
        <p>{NAME}<br>Musterstraße 1<br>48155 Münster</p>
        <p class="kontakt__wege"><a href="tel:{TEL_INTL}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div class="kontakt__text">
        <h2 id="kontakt-titel">Sprechen Sie mit uns, bevor Sie ein Grundstück kaufen</h2>
        <p>Das erste Gespräch dauert eine Stunde und kostet nichts. Wir sehen uns Ihr Grundstück oder Ihr Haus an, hören zu, was Sie vorhaben, und sagen Ihnen, was daraus werden kann und was es ungefähr kostet.</p>
        <p><a class="knopf" href="kontakt/">Projekt besprechen</a></p>
      </div>
    </div>
  </section>
""")
    teile.append(footer(d, jsonld=True))
    schreiben("index.html", "".join(teile))

# ---------------------------------------------------------------- Projekte-Übersicht
def projekte_uebersicht():
    d = 1
    kacheln = "\n".join(kachel(pr, d, "h2") for pr in PROJEKTE)
    html = head(d, "Projekte | Musterbüro Nordkant, Münster",
                "Sechs Wohnhäuser im Münsterland: Neubauten in Telgte, Nottuln und Münster, Umbau einer Hofstelle in Havixbeck, Anbau in Hiltrup, Aufstockung in Greven.", "projekte/")
    html += header(d, "projekte/")
    html += f"""
  <!-- Projekte-Übersicht: helenhard-no-F7 sechs Kacheln in zwei Spalten, ohne Filter -->
  <section class="sektion">
    <div class="inhalt">
      <div class="seitenkopf">
        <p class="label">Projekte</p>
        <h1>Sechs Häuser zwischen Telgte und Nottuln, gebaut zwischen 2021 und 2024.</h1>
      </div>
      <ul class="raster-projekte" style="list-style:none;padding:0">
{kacheln}
      </ul>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("projekte/index.html", html)

# ---------------------------------------------------------------- Projekt-Detail
def projekt_detail(i, pr):
    d = 2
    naechstes = PROJEKTE[(i + 1) % len(PROJEKTE)]
    b1, b2, b3 = pr["bilder"]
    text = "\n".join(f"        <p>{t}</p>" for t in pr["text"])
    html = head(d, f"{pr['titel']}, {pr['ort']} | {NAME}", pr["beschreibung"], f"projekte/{pr['slug']}/")
    html += header(d, "projekte/")
    html += f"""
  <!-- Projektkopf: pietboon-com-F11 Hero 16:9 im Container, Titel und Text darunter;
       big-dk-F4 Ort in Versalien; helenhard-no-F9 Metadatenblock (Variante B) -->
  <article class="sektion">
    <div class="inhalt projekt-kopf">
      <div class="projekt-kopf__bild">
        {img(b1[0], b1[1], d, lazy=False, prio=True, sizes="(max-width: 1280px) 100vw, 1280px")}
      </div>
      <div class="projekt-kopf__text">
        <div>
          <p class="label">{pr['ort']} · {pr['jahr']}</p>
          <h1>{pr['titel']}</h1>
          <p class="projekt-kopf__untertitel">{pr['satz']}</p>
          <dl class="meta">
            <div><dt>Ort</dt><dd>{pr['ort']}</dd></div>
            <div><dt>Fertigstellung</dt><dd>{pr['jahr']}</dd></div>
            <div><dt>Leistung</dt><dd>{pr['leistung']}</dd></div>
            <div><dt>Leistungsphasen</dt><dd>{pr['lp']}</dd></div>
            <div><dt>Wohnfläche</dt><dd>{pr['flaeche']}</dd></div>
          </dl>
        </div>
        <div class="projekt-kopf__lauf">
{text}
          <p><a class="knopf" href="{p(d)}kontakt/">Projekt besprechen</a></p>
        </div>
      </div>
    </div>
  </article>

  <!-- Bildpaar: pietboon-com-F7 zwei Fotos in ungleicher Breite, rechts versetzt -->
  <section class="sektion" aria-label="Weitere Bilder">
    <div class="inhalt bildpaar">
      <div>{img(b2[0], b2[1], d, sizes="(max-width: 720px) 100vw, 720px")}</div>
      <div>{img(b3[0], b3[1], d, sizes="(max-width: 720px) 100vw, 500px")}</div>
    </div>
  </section>

  <!-- Nächstes Projekt: big-dk-F4 Ort in Versalien -->
  <section class="sektion">
    <div class="inhalt weiter">
      <p class="label">Nächstes Projekt</p>
      <a href="{p(d)}projekte/{naechstes['slug']}/">
        <span class="weiter__titel">{naechstes['titel']}</span>
        <span class="label weiter__ort">{naechstes['ort']} · {naechstes['jahr']}</span>
      </a>
    </div>
  </section>
"""
    html += footer(d)
    schreiben(f"projekte/{pr['slug']}/index.html", html)

# ---------------------------------------------------------------- Büro
def buero():
    d = 1
    html = head(d, "Büro | Musterbüro Nordkant, Münster",
                "Musterbüro Nordkant: Architekturbüro in Münster mit vier Personen, seit 2016 von zwei Partnern geführt. Mitglieder der Architektenkammer NRW.", "buero/")
    html += header(d, "buero/")
    html += f"""
  <!-- Büro-Statement: pietboon-com-F6 versetzter Farbkasten mit überlappendem Bild -->
  <section class="sektion statement-sektion">
    <div class="inhalt statement">
      <div class="statement__kasten">
        <p class="label">Büro</p>
        <h1>Wir planen Wohnhäuser im Münsterland für Menschen, die lange darin leben wollen.</h1>
        <p>Neubauten, Umbauten und Anbauten, mit wenig Material, viel Licht und Grundrissen, die sich mit dem Leben ändern können. Das Büro sitzt seit 2016 in Münster, die Baustellen liegen zwischen Telgte, Greven und Nottuln.</p>
        <p>Wir übernehmen Entwurf und Bauleitung aus einer Hand. Wer den Grundriss gezeichnet hat, steht auch auf der Baustelle, wenn die Fensterbank falsch sitzt.</p>
      </div>
      <div class="statement__bild">
        {img("statement.webp", "Blick nach oben in ein Oberlicht, umgeben von Holzlamellen", d, sizes="(max-width: 720px) 82vw, 500px")}
      </div>
    </div>
  </section>

  <!-- Team: Namensliste mit Rolle, Hairlines, keine Portraits (Brief 6, Wunsch C) -->
  <section class="sektion" aria-labelledby="team-titel">
    <div class="inhalt">
      <p class="label">Team</p>
      <h2 id="team-titel">Vier Personen, ein Tisch</h2>
      <ul class="team">
        <li><span>Dipl.-Ing., Architekt</span><span>Partner, Entwurf</span></li>
        <li><span>Dipl.-Ing., Architektin</span><span>Partnerin, Bauleitung</span></li>
        <li><span>M. Sc., Architektin</span><span>Entwurf und Ausführungsplanung</span></li>
        <li><span>Bauzeichner</span><span>Zeichnung und Ausschreibung</span></li>
      </ul>
      <p class="klein" style="margin-top:2rem">Die Inhaberinnen und Inhaber sind in die Architektenliste der Architektenkammer Nordrhein-Westfalen eingetragen. Namen nennt dieser Musterentwurf bewusst nicht, weil die Personen dahinter erfunden wären.</p>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("buero/index.html", html)

# ---------------------------------------------------------------- Leistungen
def leistungen():
    d = 1
    html = head(d, "Leistungen | Musterbüro Nordkant, Münster",
                "Neubau, Umbau und Sanierung, Anbau und Aufstockung, Bauberatung vor dem Grundstückskauf: Leistungen von Musterbüro Nordkant in Münster, HOAI-Phasen 1 bis 8.", "leistungen/")
    html += header(d, "leistungen/")
    html += f"""
  <!-- Leistungen: Liste mit Hairlines, Grid 4/8 je Eintrag, Anker je Leistung (Brief 5 und 6) -->
  <section class="sektion">
    <div class="inhalt">
      <div class="seitenkopf">
        <p class="label">Leistungen</p>
        <h1>Vier Aufgaben, die wir von der ersten Skizze bis zur Abnahme begleiten.</h1>
        <p>Alle Leistungen umfassen die Leistungsphasen 1 bis 8 der HOAI: vom ersten Gespräch über Entwurf, Bauantrag und Ausschreibung bis zur Bauleitung. Auf Wunsch übernehmen wir auch einzelne Phasen.</p>
      </div>
      <ul class="leistungen">
        <li class="leistung" id="neubau">
          <h2>Neubau</h2>
          <div>
            <p>Ein Einfamilienhaus auf einem Grundstück, das Sie kennen oder gerade kaufen wollen. Wir beginnen mit dem Ort: Wo steht die Sonne, wo die Nachbarn, wo der Baum, der bleiben soll. Daraus entsteht ein Entwurf, den wir mit Ihnen in zwei oder drei Runden festlegen, bevor der Bauantrag geschrieben wird.</p>
            <p>Danach schreiben wir die Gewerke aus, vergleichen die Angebote und leiten die Baustelle bis zur Abnahme. Beispiele: <a href="{p(d)}projekte/haus-am-deich/">Haus am Deich</a>, <a href="{p(d)}projekte/haus-im-wald/">Haus im Wald</a>.</p>
          </div>
        </li>
        <li class="leistung" id="umbau">
          <h2>Umbau und Sanierung</h2>
          <div>
            <p>Ein Haus, das zu Ihnen passt, aber nicht mehr zu Ihrem Leben: zu viele kleine Zimmer, zu wenig Licht, ein Dach, das erneuert werden muss. Wir sehen uns die Substanz an, sagen Ihnen, was tragfähig ist und was nicht, und planen den Umbau so, dass das Haus seinen Charakter behält.</p>
            <p>Bei Sanierungen kümmern wir uns um Dämmung, Fenster und Haustechnik in einem Zug, damit Sie nur einmal bauen. Beispiel: <a href="{p(d)}projekte/hofstelle-havixbeck/">Umbau Hofstelle</a>.</p>
          </div>
        </li>
        <li class="leistung" id="anbau">
          <h2>Anbau und Aufstockung</h2>
          <div>
            <p>Mehr Platz auf dem Grundstück, das Sie schon haben. Ein Anbau öffnet das Haus zum Garten, eine Aufstockung schafft ein ganzes Geschoss, ohne dass Sie Gartenfläche verlieren. Beides planen wir so, dass Sie während der Bauzeit im Haus bleiben können.</p>
            <p>Vorgefertigte Holzbauteile verkürzen die Bauzeit auf wenige Wochen. Beispiele: <a href="{p(d)}projekte/anbau-hiltrup/">Anbau Gartenhaus</a>, <a href="{p(d)}projekte/aufstockung-greven/">Aufstockung Reihenhaus</a>.</p>
          </div>
        </li>
        <li class="leistung" id="bauberatung">
          <h2>Bauberatung vor dem Grundstückskauf</h2>
          <div>
            <p>Bevor Sie ein Grundstück oder ein altes Haus kaufen, sehen wir es uns mit Ihnen an. Wir prüfen Bebauungsplan, Baulasten und Erschließung, schätzen, was auf dem Grundstück gebaut werden darf, und was Bestand und Umbau kosten würden.</p>
            <p>Sie bekommen eine schriftliche Einschätzung, bevor Sie beim Notar sitzen. Diese Beratung rechnen wir nach Stunden ab, sie verpflichtet Sie zu nichts Weiterem.</p>
          </div>
        </li>
      </ul>
    </div>
  </section>

  <!-- Bildpaar: pietboon-com-F7 -->
  <section class="sektion" aria-label="Bilder aus zwei Projekten">
    <div class="inhalt bildpaar">
      <div>{img("projekte/haus-am-deich-03.webp", "Holzterrasse mit dunkler Pergola vor einem anthrazitfarbenen Baukörper zwischen Birken", d, sizes="(max-width: 720px) 100vw, 720px")}</div>
      <div>{img("projekte/hofstelle-02.webp", "Ausgebautes Dachgeschoss mit sichtbarem Backsteinpfeiler, Dachfenstern und hellem Holzboden", d, sizes="(max-width: 720px) 100vw, 500px")}</div>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("leistungen/index.html", html)

# ---------------------------------------------------------------- Kontakt
def kontakt():
    d = 1
    html = head(d, "Kontakt | Musterbüro Nordkant, Münster",
                "Musterbüro Nordkant, Musterstraße 1, 48155 Münster. Telefon 0251 000000 (Musterangabe), info@musterbuero-nordkant.de. Erstgespräch im Büro oder vor Ort.", "kontakt/")
    html += header(d, "kontakt/")
    html += f"""
  <!-- Kontakt: Grid 5/7, Kasten auf Fläche (pietboon-com-F2), kein Formular, keine Karte (Brief 6) -->
  <section class="sektion">
    <div class="inhalt">
      <div class="seitenkopf">
        <p class="label">Kontakt</p>
        <h1>Rufen Sie an oder schreiben Sie uns. Das erste Gespräch kostet nichts.</h1>
      </div>
      <div class="kontakt">
        <div class="kontakt__kasten">
          <p>{NAME}<br>Musterstraße 1<br>48155 Münster</p>
          <p class="kontakt__wege"><a href="tel:{TEL_INTL}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></p>
          <p class="klein">Montag bis Freitag, 9 bis 17 Uhr.<br>Telefon und Anschrift sind Musterangaben.</p>
        </div>
        <div class="kontakt__text">
          <h2>Was beim Erstgespräch passiert</h2>
          <p>Wir treffen uns bei uns im Büro oder auf Ihrem Grundstück, wenn es eines gibt. Sie erzählen, was Sie vorhaben, wie Sie wohnen wollen und was Sie ausgeben können.</p>
          <p>Wir sagen Ihnen, was daraus werden kann, was es ungefähr kostet und wie lange es dauert. Dazu gehört auch, wenn wir Ihnen von etwas abraten.</p>
          <p>Danach bekommen Sie ein Angebot für die Planung. Bis dahin entstehen keine Kosten.</p>
        </div>
      </div>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("kontakt/index.html", html)

# ---------------------------------------------------------------- Rechtstexte
def impressum():
    d = 1
    html = head(d, "Impressum | Musterbüro Nordkant",
                "Impressum von Musterbüro Nordkant, Musterstraße 1, 48155 Münster. Angaben nach § 5 DDG, Kammer, Berufshaftpflicht, alles Musterangaben.", "impressum/")
    html += header(d, None)
    html += f"""
  <section class="sektion">
    <div class="inhalt inhalt--schmal">
      <p class="label">Rechtliches</p>
      <h1>Impressum</h1>

      <h2>Angaben gemäß § 5 DDG</h2>
      <p>
        {NAME}<br>
        Musterstraße 1<br>
        48155 Münster
      </p>
      <p>Partnerschaftsregister: Amtsgericht Musterstadt, PR 0000 (Musterangabe)</p>

      <h2>Kontakt</h2>
      <p>
        Telefon: <a href="tel:{TEL_INTL}">{TEL}</a> (Musterangabe)<br>
        E-Mail: <a href="mailto:{MAIL}">{MAIL}</a>
      </p>

      <h2>Berufsbezeichnung und Kammer</h2>
      <p>
        Berufsbezeichnung: Architekt/in (verliehen in der Bundesrepublik Deutschland)<br>
        Zuständige Kammer: Architektenkammer Nordrhein-Westfalen, Zollhof 1, 40221 Düsseldorf<br>
        Berufsrechtliche Regelungen: Baukammerngesetz NRW und Berufsordnung, einsehbar über
        <a href="https://www.aknw.de" rel="noopener">aknw.de</a>
      </p>

      <h2>Umsatzsteuer</h2>
      <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE000000000 (Musterangabe)</p>

      <h2>Berufshaftpflichtversicherung</h2>
      <p>
        Musterversicherung AG (Musterangabe), Musterstraße 1, 48155 Münster<br>
        Räumlicher Geltungsbereich: Deutschland
      </p>

      <h2>Verantwortlich für den Inhalt</h2>
      <p>Die Büroleitung (Musterangabe), Anschrift wie oben</p>

      <h2>Streitbeilegung</h2>
      <p>
        Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
        Verbraucherschlichtungsstelle teilzunehmen.
      </p>

      <h2>Bildnachweise</h2>
      <p>Alle Fotografien auf dieser Website sind Stockmaterial von Pexels (Lizenz: kostenlos, kommerziell nutzbar, keine Namensnennung erforderlich). Kein Bild zeigt ein Projekt dieses Büros.</p>

      <p class="klein">
        Diese Website ist ein Musterentwurf von XPONext (xponext.de). Büro, Personen und Projekte
        sind erfunden; Anschrift, Telefonnummer, E-Mail-Adresse sowie die Angaben zu Register,
        Umsatzsteuer und Versicherung sind Musterangaben. Die Fotografie ist Stockmaterial,
        Nachweis siehe oben.
      </p>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("impressum/index.html", html)

def datenschutz():
    d = 1
    html = head(d, "Datenschutz | Musterbüro Nordkant",
                "Datenschutzerklärung von Musterbüro Nordkant: keine Cookies, keine Analyse-Werkzeuge, keine fremden Server, kein Formular.", "datenschutz/")
    html += header(d, None)
    html += f"""
  <section class="sektion">
    <div class="inhalt inhalt--schmal">
      <p class="label">Rechtliches</p>
      <h1>Datenschutzerklärung</h1>
      <p>
        Diese Website kommt ohne Cookies, ohne Analyse-Werkzeuge, ohne Kontaktformular und ohne
        Inhalte von fremden Servern aus. Was beim Besuch und bei einer Kontaktaufnahme per E-Mail
        oder Telefon mit Ihren Daten geschieht, steht hier.
      </p>

      <h2>Verantwortliche Stelle</h2>
      <p>
        {NAME}<br>
        Musterstraße 1, 48155 Münster<br>
        Telefon: <a href="tel:{TEL_INTL}">{TEL}</a><br>
        E-Mail: <a href="mailto:{MAIL}">{MAIL}</a>
      </p>
      <p>Ein Datenschutzbeauftragter ist nicht bestellt, weil die gesetzlichen Voraussetzungen dafür nicht vorliegen.</p>

      <h2>Besuch der Website</h2>
      <p>
        Beim Aufruf der Seiten werden keine Cookies gesetzt und keine Analyse- oder
        Statistikwerkzeuge eingesetzt. Alle Schriften, Bilder und Skripte liegen auf dem eigenen
        Webspace. Es werden keine Inhalte von fremden Servern nachgeladen.
      </p>

      <h3>Hosting und Server-Protokolle</h3>
      <p>
        Die Website wird bei STRATO AG, Otto-Ostrowski-Straße 7, 10249 Berlin betrieben. Wie jeder
        Webserver zeichnet der Server bei jedem Aufruf technische Daten in Protokolldateien auf:
      </p>
      <ul>
        <li>IP-Adresse des aufrufenden Geräts</li>
        <li>Datum und Uhrzeit des Aufrufs</li>
        <li>aufgerufene Seite und übertragene Datenmenge</li>
        <li>Browser und Betriebssystem, soweit übermittelt</li>
        <li>die zuvor besuchte Seite, soweit der Browser sie übermittelt</li>
      </ul>
      <p>
        Diese Daten dienen dem sicheren und störungsfreien Betrieb des Servers und werden nicht
        mit anderen Daten zusammengeführt. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Der
        Hoster verarbeitet die Daten in unserem Auftrag auf Grundlage eines Vertrags zur
        Auftragsverarbeitung und löscht die Protokolle nach Ablauf der dort geltenden Fristen.
      </p>

      <h2>E-Mail und Telefon</h2>
      <p>
        Wenn Sie uns per E-Mail oder telefonisch kontaktieren, verarbeiten wir die Angaben, die
        Sie uns dabei machen: Name, Kontaktdaten und Ihr Anliegen. Wir verwenden die Daten
        ausschließlich, um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b
        DSGVO, wenn Ihre Anfrage auf einen Auftrag zielt, im Übrigen Art. 6 Abs. 1 lit. f DSGVO
        aus unserem Interesse, Anfragen zu beantworten.
      </p>
      <p>
        Ihre Nachricht bleibt so lange in unserem Postfach, wie es für die Bearbeitung nötig
        ist. Kommt es zu einem Auftrag, bewahren wir den Schriftverkehr im Rahmen der handels-
        und steuerrechtlichen Aufbewahrungspflichten auf. Andernfalls löschen wir die Nachricht,
        sobald Ihr Anliegen erledigt ist.
      </p>

      <h2>Verweise auf andere Websites</h2>
      <p>
        Wo wir auf fremde Websites verweisen, handelt es sich um gewöhnliche Links, es wird
        nichts eingebettet. Erst wenn Sie einen solchen Link anklicken, gelten die
        Datenschutzbestimmungen des jeweiligen Anbieters.
      </p>

      <h2>Ihre Rechte</h2>
      <p>Sie haben gegenüber uns das Recht auf</p>
      <ul>
        <li>Auskunft über die zu Ihrer Person gespeicherten Daten (Art. 15 DSGVO)</li>
        <li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li>
        <li>Löschung, soweit keine Aufbewahrungspflicht entgegensteht (Art. 17 DSGVO)</li>
        <li>Einschränkung der Verarbeitung (Art. 18 DSGVO)</li>
        <li>Datenübertragbarkeit (Art. 20 DSGVO)</li>
        <li>Widerspruch gegen eine Verarbeitung, die auf Art. 6 Abs. 1 lit. f DSGVO beruht (Art. 21 DSGVO)</li>
      </ul>
      <p>
        Wenden Sie sich dazu formlos an die oben genannte Adresse. Sie haben außerdem das
        Recht, sich bei einer Aufsichtsbehörde zu beschweren. Zuständig ist die Landesbeauftragte
        für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2-4,
        40213 Düsseldorf.
      </p>

      <h2>Keine automatisierten Entscheidungen</h2>
      <p>Wir treffen keine Entscheidungen, die ausschließlich auf einer automatisierten Verarbeitung beruhen, und erstellen keine Profile.</p>

      <p class="klein">Stand: September 2026. Diese Website ist ein Musterentwurf von XPONext; Büro, Personen und Kontaktdaten sind Musterangaben.</p>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("datenschutz/index.html", html)

def sitemap():
    heute = "2026-09-08"
    urls = [("", "1.0", "monthly"), ("projekte/", "0.9", "monthly")]
    urls += [(f"projekte/{pr['slug']}/", "0.8", "yearly") for pr in PROJEKTE]
    urls += [("leistungen/", "0.8", "yearly"), ("buero/", "0.7", "yearly"), ("kontakt/", "0.6", "yearly")]
    zeilen = "\n".join(f"  <url><loc>{URL}/{u}</loc><lastmod>{heute}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>" for u, pr, c in urls)
    schreiben("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{zeilen}\n</urlset>\n')

if __name__ == "__main__":
    startseite()
    if not PROBE:
        projekte_uebersicht()
        for i, pr in enumerate(PROJEKTE):
            projekt_detail(i, pr)
        buero()
        leistungen()
        kontakt()
        impressum()
        datenschutz()
        sitemap()
