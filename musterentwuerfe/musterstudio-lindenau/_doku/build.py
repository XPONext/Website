#!/usr/bin/env python3
"""Generator für den Musterentwurf Musterstudio Lindenau (Innenarchitektur, erfunden).

Erzeugt alle HTML-Seiten und die sitemap.xml aus einem Datenmodell, damit Kopf- und
Fußzeile überall identisch sind und die relativen Pfade je Ordnertiefe stimmen
(lokal unter http://localhost:8765/, live unter /musterentwuerfe/musterstudio-lindenau/).

Aufruf:  python3 _doku/build.py [--probe]
--probe  schreibt nur index.html mit Kopfzeile, Hero und Intro (Hero-Probe, Schritt 2).
"""
import sys
from pathlib import Path
from PIL import Image

SITE = Path("/Users/timbunger/Desktop/XPONext/Website XPO/Website/musterentwuerfe/musterstudio-lindenau")
URL = "https://www.xponext.de/musterentwuerfe/musterstudio-lindenau"
ROBOTS = "noindex, follow"
NAME = "Musterstudio Lindenau"
INHABERIN = "Inhaberin: Dipl.-Ing. Innenarchitektin (Musterangabe)"
STRASSE, PLZ, ORT = "Musterstraße 1", "20457", "Hamburg"
TEL, TEL_INTL = "040 000000", "+4940000000"
MAIL = "post@musterstudio-lindenau.de"
JAHR, DATUM, STAND = "2026", "2026-09-07", "September 2026"

PROBE = "--probe" in sys.argv

# ---------------------------------------------------------------- Bilder
_masse = {}
def masse(rel):
    if rel not in _masse:
        with Image.open(SITE / "assets" / "bilder" / rel) as im:
            _masse[rel] = im.size
    return _masse[rel]

def p(depth):
    return "../" * depth

def img(name, alt, depth, sizes, lazy=True, prio=False, anim=True, pos=None):
    """Projektbild mit srcset 960/1440/1920 (kacheln/ + Original in projekte/)."""
    src = f"kacheln/{name}-1440.webp"
    w, h = masse(src)
    ow, _ = masse(f"projekte/{name}.webp")
    srcset = ", ".join([
        f"{p(depth)}assets/bilder/kacheln/{name}-960.webp 960w",
        f"{p(depth)}assets/bilder/kacheln/{name}-1440.webp 1440w",
        f"{p(depth)}assets/bilder/projekte/{name}.webp {ow}w",
    ])
    a = [f'src="{p(depth)}assets/bilder/{src}"', f'srcset="{srcset}"', f'sizes="{sizes}"',
         f'alt="{alt}"', f'width="{w}"', f'height="{h}"']
    if pos:
        a.append(f'style="object-position:{pos}"')
    if prio:
        a.append('fetchpriority="high"')
    elif lazy:
        a.append('loading="lazy"')
    klasse = "bild bild--anim" if anim else "bild"
    return f'<div class="{klasse}"><img {" ".join(a)}></div>'

def hero_img(depth):
    w, h = masse("hero/hero-1440.webp")
    srcset = ", ".join(f"{p(depth)}assets/bilder/hero/hero-{s}.webp {s}w" for s in (960, 1440, 1920))
    return (f'<div class="bild hero__bild"><img src="{p(depth)}assets/bilder/hero/hero-1440.webp" '
            f'srcset="{srcset}" sizes="(max-width: 900px) 100vw, min(70vw, 896px)" '
            f'alt="Küche mit Einbaufronten aus heller Eiche und weißen Wänden, Penthouse Berlin-Mitte" '
            f'width="{w}" height="{h}" fetchpriority="high"></div>')

# ---------------------------------------------------------------- Daten
LEISTUNGEN = [
    ("wohnraeume", "Private Wohnräume",
     "Wohnungen, Häuser und Ferienhäuser, vom Grundriss über Einbauten bis zu Stoffen und Leuchten. "
     "Wir arbeiten mit dem Bestand, nicht gegen ihn, und mit Handwerkern, die wir seit Jahren kennen.",
     ["harvestehude", "blankenese", "kampen"]),
    ("gastronomie", "Gastronomie und Hotellerie",
     "Gasträume, Bars, Lobbys und Zimmer, die auch nach dem dritten Jahr Betrieb noch stimmen. "
     "Akustik, Licht und Laufwege planen wir mit der Küche und dem Service zusammen.",
     ["restaurant-fleet", "hotel-speicherstadt"]),
    ("praxen", "Praxen und Kanzleien",
     "Empfang, Wartebereich, Behandlungs- und Besprechungsräume. Technik und Hygiene bleiben unsichtbar, "
     "der Raum wirkt ruhig, für Patienten, Mandanten und die Menschen, die dort täglich arbeiten.",
     ["praxis-eppendorf", "kanzlei-hafencity"]),
    ("moebel", "Möbel- und Einbauentwurf",
     "Küchen, Schränke, Regale, Tresen und Tische, gezeichnet für den einen Raum und gebaut von "
     "Tischlereien in Hamburg und Umgebung. Zeichnung, Muster, Abnahme in der Werkstatt.",
     ["penthouse-berlin", "restaurant-fleet"]),
    ("material", "Farb- und Materialkonzept",
     "Wenn das Haus schon steht und nur Oberflächen, Farben und Textilien fehlen: ein Konzept mit "
     "Bemusterung vor Ort, Mengen und Bezugsquellen, das Sie selbst oder mit uns umsetzen.",
     ["kampen", "hotel-speicherstadt"]),
]
FELD = {k: t for k, t, _, _ in LEISTUNGEN}

PROJEKTE = [
    dict(slug="harvestehude", titel="Altbauwohnung Harvestehude", ort="Hamburg", jahr="2024", feld="wohnraeume",
         leistung="Umbau, Einrichtung, Möbelentwurf", flaeche="ca. 165 m²",
         bilder=[("harvestehude-03", "Wohnzimmer mit grünem Samtsofa und hellen Vorhängen, Altbauwohnung Harvestehude"),
                 ("harvestehude-01", "Salon mit Kamin, Stuckrahmen und Fischgrätparkett, Altbauwohnung Harvestehude"),
                 ("harvestehude-04", "Großer Wohnraum mit hellen Sofas und Teppich, Altbauwohnung Harvestehude"),
                 ("harvestehude-02", "Esszimmer mit runder Tafel, hohen Fenstern und Fischgrätparkett, Altbauwohnung Harvestehude")],
         text="Eine Etagenwohnung aus den 1910er Jahren mit hohen Decken, Stuck und Fischgrätparkett, die lange als Kanzlei genutzt wurde. "
              "Wir haben die Zimmerflucht wieder geöffnet, Wandfelder und Kamin freigelegt und das Parkett aufgearbeitet. "
              "Die Einbauten in Räuchereiche und Leinen sind für diese Räume gezeichnet; die Polstermöbel kommen von zwei "
              "Werkstätten, mit denen wir seit Jahren arbeiten. Farbe kommt aus Textil und Kunst, nicht von den Wänden."),
    dict(slug="restaurant-fleet", titel="Restaurant am Fleet", ort="Hamburg", jahr="2024", feld="gastronomie",
         leistung="Innenausbau, Lichtplanung, Möbelentwurf", flaeche="ca. 220 m², 78 Plätze",
         bilder=[("restaurant-fleet-02", "Gastraum mit Eichenlamellen an der Decke und gemusterten Fliesen, Restaurant am Fleet"),
                 ("restaurant-fleet-03", "Bar aus geöltem Holz mit Regal und Pflanzen, Restaurant am Fleet"),
                 ("restaurant-fleet-04", "Gastraum mit dunklen Stühlen und orangefarbenen Leuchten, Restaurant am Fleet"),
                 ("restaurant-fleet-01", "Bar mit dunklem Holz und Pendelleuchten, Restaurant am Fleet")],
         text="Ein Restaurant im Erdgeschoss eines Kontorhauses, mit Blick auf das Fleet. Der Gastraum ist mit Eichenlamellen "
              "an Decke und Wänden gefasst, die die Akustik ruhig halten und das Licht am Abend warm machen. Die Bar aus "
              "geöltem Nussbaum trennt Küche und Gastraum, ohne die Sicht zu nehmen. Tische, Bänke und Leuchten sind eigens "
              "entworfen; die Fliesen im Eingang nehmen das Muster des historischen Bodens auf."),
    dict(slug="kampen", titel="Ferienhaus Kampen", ort="Sylt", jahr="2023", feld="wohnraeume",
         leistung="Einrichtung, Farb- und Materialkonzept", flaeche="ca. 140 m²",
         bilder=[("kampen-03", "Wohnzimmer mit hellem Sofa, Kaminofen und Pflanzen, Ferienhaus Kampen"),
                 ("kampen-02", "Schlafzimmer mit hellen Dielen und Blick auf die Dünen, Ferienhaus Kampen"),
                 ("kampen-04", "Sideboard aus hellem Holz mit Trockengras, Ferienhaus Kampen"),
                 ("kampen-01", "Schlafzimmer mit weißer Wandvertäfelung, Leinen und Holzbord, Ferienhaus Kampen")],
         text="Ein Reetdachhaus aus den 1970er Jahren, das die Bauherren für Wochen am Meer nutzen. Das Innere ist auf wenige "
              "Materialien zurückgeführt: geweißte Dielen, Kalkputz, Leinen und helles Holz. Der Wohnraum wurde zum Garten "
              "hin geöffnet, ein Kaminofen trennt Sitz- und Essbereich. Im großen Schlafzimmer bleibt der Blick auf die Dünen das "
              "einzige Bild an der Wand, das Gästezimmer bekommt eine Vertäfelung und ein Bord. Alle Möbel sind robust genug für Sand und nasse Hunde."),
    dict(slug="praxis-eppendorf", titel="Zahnarztpraxis Eppendorf", ort="Hamburg", jahr="2023", feld="praxen",
         leistung="Innenausbau, Empfang und Behandlungsräume", flaeche="ca. 260 m², 5 Behandlungsräume",
         bilder=[("praxis-eppendorf-03", "Behandlungsraum mit schwarzem Stuhl und sechseckigen Fliesen, Zahnarztpraxis Eppendorf"),
                 ("praxis-eppendorf-02", "Behandlungsraum mit weißem Stuhl vor großem Fenster, Zahnarztpraxis Eppendorf"),
                 ("praxis-eppendorf-01", "Behandlungseinheit vor Sitzbank aus Eiche mit grauen Polstern, Zahnarztpraxis Eppendorf"),
                 ("praxis-eppendorf-04", "Instrumententräger vor Einbauschrank aus Eiche mit Wiener Geflecht, Zahnarztpraxis Eppendorf")],
         text="Eine Praxis für Zahnmedizin mit fünf Behandlungsräumen in einem Neubau. Die Aufgabe war, die Technik unauffällig "
              "zu halten und Wartezeit angenehm zu machen. Wände und Decken in Weiß, ein Boden in warmem Grau und Einbauten aus Eiche "
              "mit Wiener Geflecht nehmen den Behandlungsräumen ihre Kälte; sechseckige Fliesen in Holzoptik sind das einzige Muster. Das Licht ist indirekt geführt und wird nur am Stuhl gebündelt. "
              "Empfang und Wartebereich liegen so, dass niemand an offenen Türen vorbeigeht."),
    dict(slug="penthouse-berlin", titel="Penthouse Berlin-Mitte", ort="Berlin", jahr="2023", feld="wohnraeume",
         leistung="Ausbau, Küchen- und Möbelentwurf", flaeche="ca. 190 m²",
         bilder=[("penthouse-berlin-03", "Küche mit Einbaufronten aus heller Eiche und weißen Wänden, Penthouse Berlin-Mitte"),
                 ("penthouse-berlin-02", "Esszimmer mit Glaswänden und rundem Tisch, Penthouse Berlin-Mitte"),
                 ("penthouse-berlin-01", "Küche mit Eichenfronten und schwarzer Theke, Penthouse Berlin-Mitte"),
                 ("penthouse-berlin-04", "Weiße Küchenzeile mit Einbaugeräten, Penthouse Berlin-Mitte")],
         text="Ein Dachgeschoss auf einem Neubau in Berlin-Mitte, das als Rohbau übernommen wurde, mit Blick auf die Hochhäuser "
              "am Alexanderplatz. Die Küche ist das Zentrum: Fronten "
              "aus heller Eiche, eine Insel aus geschliffenem Beton, kein Griff, keine offene Ablage. Die Wohnräume gruppieren "
              "sich um die Dachterrasse; ein Esszimmer mit Glaswänden macht sie auch im Winter nutzbar. Türen, Regale und Bad "
              "sind aus demselben Holz, damit das Geschoss trotz vieler Räume als eines gelesen wird."),
    dict(slug="hotel-speicherstadt", titel="Boutique-Hotel Speicherstadt", ort="Hamburg", jahr="2022", feld="gastronomie",
         leistung="Lobby, Bar und Zimmer", flaeche="ca. 1.400 m², 24 Zimmer",
         bilder=[("hotel-speicherstadt-03", "Lobby mit Empfangstresen aus gemustertem Furnier und Pendelleuchten, Boutique-Hotel Speicherstadt"),
                 ("hotel-speicherstadt-02", "Zimmer mit Doppelbett und grauer Wand, Boutique-Hotel Speicherstadt"),
                 ("hotel-speicherstadt-01", "Zimmer mit gemusterter Tapete und Ledersesseln, Boutique-Hotel Speicherstadt"),
                 ("hotel-speicherstadt-05", "Bad mit Wänden aus Travertin und freistehender Wanne, Boutique-Hotel Speicherstadt")],
         text="Ein Hotel mit 24 Zimmern in einem ehemaligen Speicher aus rotem Backstein. Die Lobby verbindet Empfang und Bar "
              "in einem Raum; der Tresen aus geometrisch gelegtem Furnier ist das einzige Muster im Haus. Die Zimmer sind ruhig "
              "gehalten, mit Textiltapete, dunklem Holz und Leuchten aus Messing; die Bäder sind in Travertin gefasst. Wo der Backstein sichtbar bleiben durfte, ist "
              "er es geblieben. Die Stoffe folgen der Farbe der Speicherfassaden gegenüber."),
    dict(slug="blankenese", titel="Stadthaus Blankenese", ort="Hamburg", jahr="2022", feld="wohnraeume",
         leistung="Umbau, Treppe und Einbauten", flaeche="ca. 240 m² auf drei Ebenen",
         bilder=[("blankenese-02", "Wohnraum mit Nussbaumwand, Ledersofa und Treppe aus Eiche und Glas, Stadthaus Blankenese"),
                 ("blankenese-03", "Treppenhaus mit dunklem Geländer und gerahmten Bildern, Stadthaus Blankenese"),
                 ("blankenese-04", "Historisches Treppengeländer aus Schmiedeeisen, Stadthaus Blankenese"),
                 ("blankenese-01", "Flur mit Treppe und Küche in Weiß, Stadthaus Blankenese")],
         text="Ein Stadthaus am Hang mit drei Ebenen, die vorher kaum zusammenhingen. Die neue Treppe aus Eiche und Glas verbindet "
              "Wohnraum, Galerie und Dachgeschoss und bringt Tageslicht bis ins Erdgeschoss. Die Wandverkleidung aus Nussbaum "
              "fasst Kamin, Fernseher und Stauraum in einem Element zusammen. Im Obergeschoss blieb das historische Geländer "
              "erhalten und wurde aufgearbeitet. Farbig sind nur Leder und Teppich."),
    dict(slug="kanzlei-hafencity", titel="Kanzlei HafenCity", ort="Hamburg", jahr="2021", feld="praxen",
         leistung="Empfang, Besprechungsräume, Arbeitsplätze", flaeche="ca. 480 m², 22 Arbeitsplätze",
         bilder=[("kanzlei-hafencity-02", "Empfang als Lounge mit Ledersofas und Terrazzoboden, Kanzlei HafenCity"),
                 ("kanzlei-hafencity-04", "Regal aus geräucherter Eiche mit Stahlrahmen, Kanzlei HafenCity"),
                 ("kanzlei-hafencity-01", "Bibliothek mit Regalwand aus Kirschbaum und Leiter, Kanzlei HafenCity"),
                 ("kanzlei-hafencity-03", "Besprechungsraum hinter Glas mit Holzlamellen an der Decke, Kanzlei HafenCity")],
         text="Eine Kanzlei für Wirtschaftsrecht auf einer Etage in der HafenCity. Der Empfang ist als Lounge angelegt, mit "
              "Ledersofas, Terrazzo und viel Tageslicht, damit Mandanten nicht warten, sondern ankommen. Der große "
              "Besprechungsraum liegt hinter Glas und wird durch Holzlamellen an der Decke ruhig. Die Arbeitsplätze sind mit "
              "Regalen aus geräucherter Eiche gegliedert, die zugleich Akten aufnehmen; die Bibliothek mit Leiter dient als Rückzugsraum. Kein Teppich im Flur, dafür ein Boden, "
              "der Schritte schluckt."),
]
P = {pr["slug"]: pr for pr in PROJEKTE}
START_PROJEKTE = ["harvestehude", "restaurant-fleet", "hotel-speicherstadt", "blankenese"]

# ---------------------------------------------------------------- Rahmen
NAV = [("projekte/", "Projekte"), ("studio/", "Studio"), ("leistungen/", "Leistungen"), ("kontakt/", "Kontakt")]

def head(depth, title, desc, pfad):
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
<link rel="preload" href="{p(depth)}assets/fonts/cormorant-garamond-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p(depth)}assets/fonts/dm-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p(depth)}assets/css/basis.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>

<a class="sprung" href="#inhalt">Zum Inhalt springen</a>
"""

def header(depth, aktiv):
    def li(pfad, text):
        cur = ' aria-current="page"' if pfad == aktiv else ""
        return f'        <li><a href="{p(depth)}{pfad}"{cur}>{text}</a></li>'
    links = "\n".join(li(*n) for n in NAV[:2])
    rechts = "\n".join(li(*n) for n in NAV[2:])
    return f"""<!-- Kopfzeile: helenhard-no-F1 geteilte Navigation mit zentrierter Wortmarke,
     helenhard-no-F12 mobile Kopfzeile aus drei Textelementen (Kontakt · Marke · Menü), statisch (Brief 7) -->
<header class="kopf">
  <div class="kopf__inhalt inhalt">
    <a class="kopf__kontakt" href="{p(depth)}kontakt/">Kontakt</a>
    <a class="marke" href="{p(depth) or './'}" aria-label="{NAME}, zur Startseite">{NAME}</a>
    <button class="kopf__schalter" type="button" aria-expanded="false" aria-controls="hauptnavigation">Menü</button>
    <nav class="kopf__nav" id="hauptnavigation" aria-label="Hauptnavigation" data-offen="false">
      <ul class="reiter reiter--links">
{links}
      </ul>
      <ul class="reiter reiter--rechts">
{rechts}
      </ul>
      <div class="kopf__nav-kontakt">
        <a href="tel:{TEL_INTL}">{TEL}</a><br>
        <a href="mailto:{MAIL}">{MAIL}</a>
      </div>
    </nav>
  </div>
</header>

<main id="inhalt">
"""

def kontakt_kasten():
    return f"""
  <!-- Kontaktkasten: zweite dunkle Stufe (pietboon-com-F2 gespiegelt), einziger gefüllter Button (Brief 7) -->
  <section class="kontakt-kasten" aria-labelledby="kontakt-titel">
    <div class="inhalt kontakt-kasten__inhalt">
      <div>
        <h2 id="kontakt-titel">Sprechen wir über Ihr Projekt.</h2>
        <p class="kursiv">Ein erstes Gespräch ist unverbindlich, bei uns im Studio oder bei Ihnen vor Ort.</p>
      </div>
      <div class="kontakt-kasten__wege">
        <a href="tel:{TEL_INTL}">{TEL}</a>
        <a class="knopf knopf--hell" href="mailto:{MAIL}">Anfrage per E-Mail</a>
      </div>
    </div>
  </section>
"""

def footer(depth, jsonld=False):
    ld = ""
    if jsonld:
        ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ArchitectOffice",
  "@id": "{URL}/#studio",
  "name": "{NAME}",
  "description": "Innenarchitektur für Wohnungen, Häuser, Gastronomie, Hotellerie und Praxen in Hamburg und Norddeutschland.",
  "url": "{URL}/",
  "email": "{MAIL}",
  "telephone": "{TEL_INTL}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{STRASSE}",
    "postalCode": "{PLZ}",
    "addressLocality": "{ORT}",
    "addressCountry": "DE"
  }},
  "areaServed": ["Hamburg", "Norddeutschland", "Berlin", "Sylt"]
}}
</script>
"""
    return f"""{kontakt_kasten()}
</main>

<!-- Fußzeile: helenhard-no-F13 ein Standortblock (Ort kursiv, Anschrift, Telefon, Mail), Navigation, Rechtstexte -->
<footer class="fuss">
  <div class="inhalt">
    <div class="fuss__raster">
      <div>
        <p class="fuss__ort">Hamburg, HafenCity</p>
        <p>{NAME}<br>{STRASSE}<br>{PLZ} {ORT}</p>
        <p class="fuss__wege"><a href="tel:{TEL_INTL}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div>
        <p class="fuss__titel">Navigation</p>
        <ul class="fuss__liste">
          <li><a href="{p(depth)}projekte/">Projekte</a></li>
          <li><a href="{p(depth)}studio/">Studio</a></li>
          <li><a href="{p(depth)}leistungen/">Leistungen</a></li>
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
      <p>Mitglied der Hamburgischen Architektenkammer</p>
    </div>
    <!-- Nur bei Musterentwürfen. -->
    <p class="muster-hinweis">Musterentwurf von XPONext (xponext.de). Studio, Personen und Projekte sind erfunden, die Fotografie ist Stockmaterial.</p>
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

def projekt_eintrag(pr, i, depth, stufe, sizes, erstes=False):
    """helenhard-no-F7 Titel zentriert über dem Bild + big-dk-F4 Ort · Jahr darunter.
    erstes=True: erstes Bild der Seite (auf /projekte/), ohne lazy und ohne Einblenden (Brief 9: ab dem zweiten Bild)."""
    seite = "links" if i % 2 == 0 else "rechts"
    name, alt = pr["bilder"][0]
    bild = img(name, alt, depth, sizes, lazy=not erstes, prio=erstes, anim=not erstes)
    return f"""      <li class="projekt projekt--{seite}">
        <a href="{p(depth)}projekte/{pr['slug']}/">
          <{stufe} class="projekt__titel">{pr['titel']}</{stufe}>
          {bild}
          <p class="label projekt__ort">{pr['ort']} · {pr['jahr']}</p>
        </a>
      </li>"""

# ---------------------------------------------------------------- Startseite
def startseite():
    depth = 0
    html = head(depth, "Musterstudio Lindenau · Innenarchitektur in Hamburg",
                "Innenarchitektur für Wohnungen, Häuser, Restaurants, Hotels und Praxen in Hamburg und "
                "Norddeutschland. Vom Grundriss bis zum letzten Stoff.", "")
    html += header(depth, "")
    html += f"""
  <!-- Hero: pietboon-com-F11-Prinzip, Bild eingerückt auf dunkler Fläche (70 %, rechts), Satz links,
       gemeinsame Unterkante (big-dk-F3); Bewegung nur beim Laden (Brief 9) -->
  <section class="sektion--dunkel hero">
    <div class="inhalt">
      <div class="hero__inhalt">
        <h1 class="hero__satz">Räume, die ruhig wirken und lange gefallen.</h1>
        {hero_img(depth)}
      </div>
      <!-- robmills-com-au-F3 wachsende Linie, dunkler Teil -->
      <span class="linie linie--dunkel" aria-hidden="true"></span>
    </div>
  </section>

  <!-- Intro: pietboon-com-F15 zentrierter Textblock mit Chevron-Linkliste -->
  <section class="sektion intro">
    <div class="inhalt">
      <span class="linie linie--hell" aria-hidden="true"></span>
      <div class="intro__block">
        <p class="intro__text">Musterstudio Lindenau ist ein Büro für Innenarchitektur in Hamburg. Wir gestalten Wohnungen, Häuser, Restaurants, Hotels und Praxen in Norddeutschland, vom Grundriss bis zum letzten Stoff, mit Handwerkern, die wir seit Jahren kennen.</p>
        <ul class="chevrons">
""" + "\n".join(f'          <li><a href="leistungen/#{k}">{t}</a></li>' for k, t, _, _ in LEISTUNGEN) + """
        </ul>
      </div>
    </div>
  </section>
"""
    if PROBE:
        return html + footer(depth, jsonld=True)
    html += """
  <!-- Projekte: helenhard-no-F7 + big-dk-F4, ein Bild je Reihe, 75 % abwechselnd links/rechts,
       robmills-com-au-F10 Einblenden (der eine Wow-Faktor) -->
  <section class="sektion sektion--dunkel" aria-labelledby="projekte-titel">
    <div class="inhalt">
      <h2 id="projekte-titel">Ausgewählte Projekte</h2>
      <p class="kursiv" style="margin-bottom:var(--raum-doppel)">Vier von acht. Alle Projekte unter <a href="projekte/">Projekte</a>.</p>
      <ul class="projekte">
""" + "\n".join(projekt_eintrag(P[s], i, depth, "h3", "(max-width: 640px) 100vw, min(75vw, 960px)") for i, s in enumerate(START_PROJEKTE)) + f"""
      </ul>
    </div>
  </section>

  <!-- Studio: pietboon-com-F6 versetzter Kasten, Bild ragt 4 rem in den Kasten -->
  <section class="sektion" aria-labelledby="studio-titel">
    <div class="inhalt studio">
      <div class="studio__kasten">
        <h2 id="studio-titel">Studio</h2>
        <p>Das Studio wurde 2014 in der HafenCity gegründet. Heute arbeiten hier vier Personen an vier bis sechs Projekten im Jahr, damit jedes davon die Zeit bekommt, die es braucht.</p>
        <ul class="team">
          <li><span>Inhaberin, Dipl.-Ing. Innenarchitektin</span></li>
          <li><span>Innenarchitektin</span></li>
          <li><span>Innenarchitekt</span></li>
          <li><span>Projektassistenz</span></li>
        </ul>
        <p><a class="studio__mehr" href="studio/">Mehr über das Studio</a></p>
      </div>
      <div class="studio__bild-rahmen">
        {img("kampen-03", "Wohnzimmer mit hellem Sofa, Kaminofen und Pflanzen, Ferienhaus Kampen", depth, "(max-width: 900px) 100vw, min(45vw, 576px)").replace('class="bild bild--anim"', 'class="bild bild--anim studio__bild"')}
      </div>
    </div>
  </section>
"""
    return html + footer(depth, jsonld=True)

# ---------------------------------------------------------------- Sitemap
def sitemap():
    seiten = [("", "1.0", "monthly"), ("projekte/", "0.9", "monthly")]
    seiten += [(f"projekte/{pr['slug']}/", "0.8", "yearly") for pr in PROJEKTE]
    seiten += [("studio/", "0.7", "yearly"), ("leistungen/", "0.8", "yearly"), ("kontakt/", "0.6", "yearly")]
    zeilen = "\n".join(f"  <url><loc>{URL}/{pf}</loc><lastmod>{DATUM}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
                       for pf, pr, cf in seiten)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{zeilen}\n</urlset>\n'


def seitenkopf(h1, zeile="", extra=""):
    return f"""
  <!-- Seitenkopf dunkel: H1 + eine Zeile (Hell-Dunkel-Regel, Brief 5) -->
  <section class="sektion--dunkel seitenkopf">
    <div class="inhalt">
      <h1>{h1}</h1>
      {zeile}{extra}
    </div>
  </section>
"""

# ---------------------------------------------------------------- Projekte-Übersicht
def projekte_uebersicht():
    depth = 1
    html = head(depth, "Projekte · Musterstudio Lindenau, Innenarchitektur Hamburg",
                "Acht Projekte aus Hamburg, Berlin und Sylt: Wohnungen, Häuser, ein Restaurant, ein Hotel, "
                "eine Praxis und eine Kanzlei, eingerichtet von Musterstudio Lindenau.", "projekte/")
    html += header(depth, "projekte/")
    html += seitenkopf("Projekte", "<p>Private Wohnräume · Gastronomie und Hotellerie · Praxen und Kanzleien</p>")
    html += """
  <!-- Projektliste hell: helenhard-no-F7 + big-dk-F4, acht Bilder 75 % abwechselnd links/rechts, robmills-com-au-F10 -->
  <section class="sektion">
    <div class="inhalt">
      <ul class="projekte">
""" + "\n".join(projekt_eintrag(pr, i, depth, "h2", "(max-width: 640px) 100vw, min(75vw, 960px)", erstes=(i == 0)) for i, pr in enumerate(PROJEKTE)) + """
      </ul>
    </div>
  </section>
"""
    return html + footer(depth)

# ---------------------------------------------------------------- Projekt-Detail
def projekt_detail(i, pr):
    depth = 2
    naechst = PROJEKTE[(i + 1) % len(PROJEKTE)]
    b = pr["bilder"]
    title = f"{pr['titel']} · Musterstudio Lindenau"
    desc = f"{pr['titel']}, {pr['ort']} {pr['jahr']}: {FELD[pr['feld']].lower()} von Musterstudio Lindenau, Innenarchitektur Hamburg. {pr['leistung']}."
    html = head(depth, title, desc[:160], f"projekte/{pr['slug']}/")
    html += header(depth, "projekte/")
    html += f"""
  <!-- Detail-Kopf dunkel: pietboon-com-F11 Hero 16:9 volle Containerbreite, Titel und Kursiv-Zeile erst darunter -->
  <section class="sektion--dunkel detail-kopf">
    <div class="inhalt">
      {img(b[0][0], b[0][1], depth, "(max-width: 1280px) 100vw, 1280px", lazy=False, prio=True, anim=False).replace('class="bild"', 'class="bild"')}
      <div class="detail-kopf__titel">
        <h1>{pr['titel']}</h1>
        <p class="kursiv">{FELD[pr['feld']]}, {pr['ort']}</p>
      </div>
    </div>
  </section>

  <!-- Detail-Körper hell: big-dk-F2 Metadaten rechtsbündig an der Bildkante, Absatz 40–80 Wörter darunter,
       pietboon-com-F7 Bildpaar 560/640 versetzt (rechts 4:3-Ausschnitt), robmills-com-au-F10 Einblenden -->
  <section class="sektion">
    <div class="inhalt detail">
      <aside class="detail__rand">
        <dl>
          <div><dt>Ort</dt><dd>{pr['ort']}</dd></div>
          <div><dt>Fertigstellung</dt><dd>{pr['jahr']}</dd></div>
          <div><dt>Leistung</dt><dd>{pr['leistung']}</dd></div>
          <div><dt>Fläche</dt><dd>{pr['flaeche']}</dd></div>
        </dl>
        <p>{pr['text']}</p>
      </aside>
      <div class="detail__gross">
        {img(b[1][0], b[1][1], depth, "(max-width: 900px) 100vw, min(75vw, 936px)")}
      </div>
"""
    if len(b) >= 4:
        html += f"""      <div class="paar">
        <div class="paar__links">{img(b[2][0], b[2][1], depth, "(max-width: 900px) 100vw, 560px")}</div>
        <div class="paar__rechts">{img(b[3][0], b[3][1], depth, "(max-width: 900px) 100vw, 640px")}</div>
      </div>
"""
    else:
        html += f"""      <div class="paar paar--einzel">
        <div>{img(b[2][0], b[2][1], depth, "(max-width: 1280px) 100vw, 1280px")}</div>
      </div>
"""
    html += f"""      <div class="detail__weiter">
        <p class="label">Nächstes Projekt</p>
        <a href="{p(depth)}projekte/{naechst['slug']}/">{naechst['titel']} →</a>
      </div>
    </div>
  </section>
"""
    return html + footer(depth)

# ---------------------------------------------------------------- Studio
def studio():
    depth = 1
    html = head(depth, "Studio · Musterstudio Lindenau, Innenarchitektur Hamburg",
                "Ein Studio für Innenarchitektur in der Hamburger HafenCity: vier Personen, "
                "vier bis sechs Projekte im Jahr, vom Grundriss bis zum letzten Stoff.", "studio/")
    html += header(depth, "studio/")
    html += seitenkopf("Studio", "<p>Vier Personen, ein Tisch, vier bis sechs Projekte im Jahr.</p>")
    html += f"""
  <!-- Studio-Körper hell: pietboon-com-F6 Kasten mit überlappendem Bild, dann pietboon-com-F7 Bildpaar -->
  <section class="sektion">
    <div class="inhalt studio">
      <div class="studio__kasten">
        <h2>Wie wir arbeiten</h2>
        <p>Das Studio wurde 2014 gegründet, nach Jahren der Inhaberin in Büros in Kopenhagen und Hamburg. Wir übernehmen Projekte vom ersten Gespräch bis zur Abnahme: Grundriss, Einbauten, Licht, Oberflächen, Möbel und Textil. Pläne zeichnen wir selbst, Muster legen wir vor Ort an, und die Werkstätten, die unsere Entwürfe bauen, kennen wir seit Jahren.</p>
        <p>Wir nehmen nur so viele Projekte an, wie wir mit vier Personen gut begleiten können. Das sind vier bis sechs im Jahr, in Hamburg, an der Küste und in Berlin.</p>
        <ul class="team">
          <li><span>Inhaberin, Dipl.-Ing. Innenarchitektin</span> · Hamburgische Architektenkammer</li>
          <li><span>Innenarchitektin</span> · Projektleitung</li>
          <li><span>Innenarchitekt</span> · Möbel- und Einbauentwurf</li>
          <li><span>Projektassistenz</span> · Bemusterung und Ausschreibung</li>
        </ul>
      </div>
      <div class="studio__bild-rahmen">
        {img("kampen-04", "Sideboard aus hellem Holz mit Trockengras, Ferienhaus Kampen", depth, "(max-width: 900px) 100vw, min(45vw, 576px)", lazy=False, prio=True, anim=False).replace('class="bild"', 'class="bild studio__bild"')}
      </div>
    </div>
    <div class="inhalt" style="margin-top:var(--abstand-sektion)">
      <div class="paar">
        <div class="paar__links">{img("harvestehude-04", "Großer Wohnraum mit hellen Sofas und Teppich, Altbauwohnung Harvestehude", depth, "(max-width: 900px) 100vw, 560px")}</div>
        <div class="paar__rechts">{img("blankenese-03", "Treppenhaus mit dunklem Geländer und gerahmten Bildern, Stadthaus Blankenese", depth, "(max-width: 900px) 100vw, 640px")}</div>
      </div>
    </div>
  </section>
"""
    return html + footer(depth)

# ---------------------------------------------------------------- Leistungen
def leistungen():
    depth = 1
    html = head(depth, "Leistungen · Musterstudio Lindenau, Innenarchitektur Hamburg",
                "Private Wohnräume, Gastronomie und Hotellerie, Praxen und Kanzleien, Möbel- und Einbauentwurf, "
                "Farb- und Materialkonzept. Innenarchitektur aus Hamburg.", "leistungen/")
    html += header(depth, "leistungen/")
    html += seitenkopf("Leistungen", "<p>Fünf Felder, ein Ablauf: Gespräch, Entwurf, Bemusterung, Werkstatt, Abnahme.</p>")
    eintraege = []
    for k, t, txt, refs in LEISTUNGEN:
        links = ", ".join(f'<a href="{p(depth)}projekte/{r}/">{P[r]["titel"]}</a>' for r in refs)
        eintraege.append(f"""        <li id="{k}">
          <h2>{t}</h2>
          <div>
            <p>{txt}</p>
            <p class="klein">Beispiele: {links}</p>
          </div>
        </li>""")
    html += """
  <!-- Leistungen hell: fünf Einträge mit Hairlines, Verweis auf Projekte als Textlink, kein Bild (Brief 6) -->
  <section class="sektion">
    <div class="inhalt">
      <ul class="leistungen">
""" + "\n".join(eintraege) + """
      </ul>
    </div>
  </section>
"""
    return html + footer(depth)

# ---------------------------------------------------------------- Kontakt
def kontakt():
    depth = 1
    html = head(depth, "Kontakt · Musterstudio Lindenau, Hamburg",
                f"{NAME}, {STRASSE}, {PLZ} {ORT}. Telefon {TEL} (Musterangabe), {MAIL}. Termine nach Vereinbarung.", "kontakt/")
    html += header(depth, "kontakt/")
    html += seitenkopf("Kontakt", "<p>Am einfachsten telefonisch, montags bis freitags von 9 bis 17 Uhr.</p>",
                       f'\n      <a class="telefon" href="tel:{TEL_INTL}">{TEL}</a>\n      <p class="klein">Telefonnummer und Anschrift sind Musterangaben.</p>')
    html += f"""
  <!-- Kontakt-Körper hell: Anschrift, Mail, Hinweis. Kein Formular, keine Karte (Brief 6) -->
  <section class="sektion">
    <div class="inhalt raster raster--2">
      <div>
        <p class="label">Anschrift</p>
        <p>{NAME}<br>{STRASSE}<br>{PLZ} {ORT}</p>
        <p class="klein" style="margin-top:1rem">Kontorhaus in der HafenCity, 3. Stock. Besuche nach Vereinbarung.</p>
      </div>
      <div>
        <p class="label">Schreiben</p>
        <p><a class="studio__mehr" style="margin-top:0" href="mailto:{MAIL}">{MAIL}</a></p>
        <p class="klein" style="margin-top:1rem">Für eine erste Einschätzung reichen ein paar Sätze zum Vorhaben, der Ort und der gewünschte Zeitraum. Wir antworten innerhalb von zwei Werktagen.</p>
      </div>
    </div>
  </section>
"""
    return html + footer(depth)

# ---------------------------------------------------------------- Rechtstexte
def impressum():
    depth = 1
    html = head(depth, "Impressum · Musterstudio Lindenau", f"Impressum von {NAME}, {STRASSE}, {PLZ} {ORT}.", "impressum/")
    html += header(depth, "")
    html += seitenkopf("Impressum", '<p class="label">Rechtliches</p>')
    html += f"""
  <section class="sektion rechtstext">
    <div class="inhalt inhalt--schmal">
      <h2>Angaben gemäß § 5 DDG</h2>
      <p>{NAME}<br>{INHABERIN}<br>{STRASSE}<br>{PLZ} {ORT}</p>

      <h2>Kontakt</h2>
      <p>Telefon: <a href="tel:{TEL_INTL}">{TEL}</a> (Musterangabe)<br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

      <h2>Berufsbezeichnung und Kammer</h2>
      <p>Berufsbezeichnung: Innenarchitektin (verliehen in der Bundesrepublik Deutschland)<br>
        Zuständige Kammer: Hamburgische Architektenkammer, Grindelhof 40, 20146 Hamburg<br>
        Berufsrechtliche Regelungen: Hamburgisches Architektengesetz und Berufsordnung, einsehbar über
        <a href="https://www.akhh.de" rel="noopener">akhh.de</a></p>

      <h2>Umsatzsteuer</h2>
      <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE000000000 (Musterangabe)</p>

      <h2>Berufshaftpflichtversicherung</h2>
      <p>Musterversicherung AG (Musterangabe), Musterstraße 1, 20095 Hamburg<br>Räumlicher Geltungsbereich: Deutschland</p>

      <h2>Verantwortlich für den Inhalt</h2>
      <p>Die Inhaberin, Anschrift wie oben. Ein Name wird nicht genannt, weil dieser Musterentwurf keine reale Person abbildet.</p>

      <h2>Streitbeilegung</h2>
      <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

      <h2>Bildnachweise</h2>
      <p>Alle Fotografien sind Stockmaterial von Pexels (Pexels-Lizenz, kommerziell nutzbar): Max Vakhtbovych, Alexander F Ungerer,
        Huy Quang Nguyễn, Abhishek Navlakha, Dmitry Zvolskiy, Taryn Elliott, myHQ-Workspaces, Ajit Singh, Cedric Fauntleroy,
        Engin Akyurt, Pixabay, Quang Nguyen Vinh, Matheus Bertelli, Valeria Boltneva. Kein Bild zeigt ein reales Projekt.</p>

      <p class="klein">Diese Website ist ein Musterentwurf von XPONext (xponext.de). Das Studio, die Personen und die Projekte
        sind erfunden; Anschrift, Telefonnummer, E-Mail-Adresse sowie Steuer- und Versicherungsangaben sind Musterangaben.
        Die Fotografie ist Stockmaterial, Nachweis siehe oben.</p>
    </div>
  </section>
"""
    return html + footer(depth)

def datenschutz():
    depth = 1
    html = head(depth, "Datenschutz · Musterstudio Lindenau",
                f"Datenschutzerklärung von {NAME}: keine Cookies, keine Analyse-Werkzeuge, keine fremden Server.", "datenschutz/")
    html += header(depth, "")
    html += seitenkopf("Datenschutzerklärung", '<p class="label">Rechtliches</p>')
    html += f"""
  <section class="sektion rechtstext">
    <div class="inhalt inhalt--schmal">
      <p>Diese Website kommt ohne Cookies, ohne Analyse-Werkzeuge, ohne Kontaktformular und ohne Inhalte von fremden
        Servern aus. Was beim Besuch und bei einer Kontaktaufnahme mit Ihren Daten geschieht, steht hier.</p>

      <h2>Verantwortliche Stelle</h2>
      <p>{NAME}<br>{INHABERIN}<br>{STRASSE}, {PLZ} {ORT}<br>
        Telefon: <a href="tel:{TEL_INTL}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Ein Datenschutzbeauftragter ist nicht bestellt, weil die gesetzlichen Voraussetzungen dafür nicht vorliegen.</p>

      <h2>Besuch der Website</h2>
      <p>Beim Aufruf der Seiten werden keine Cookies gesetzt und keine Analyse- oder Statistikwerkzeuge eingesetzt.
        Alle Schriften, Bilder und Skripte liegen auf dem eigenen Webspace. Es werden keine Inhalte von fremden Servern nachgeladen.</p>

      <h3>Hosting und Server-Protokolle</h3>
      <p>Die Website wird bei einem deutschen Hosting-Anbieter auf Servern in Deutschland betrieben. Wie jeder Webserver zeichnet
        der Server bei jedem Aufruf technische Daten in Protokolldateien auf:</p>
      <ul>
        <li>IP-Adresse des aufrufenden Geräts</li>
        <li>Datum und Uhrzeit des Aufrufs</li>
        <li>aufgerufene Seite und übertragene Datenmenge</li>
        <li>Browser und Betriebssystem, soweit übermittelt</li>
        <li>die zuvor besuchte Seite, soweit der Browser sie übermittelt</li>
      </ul>
      <p>Diese Daten dienen dem sicheren und störungsfreien Betrieb des Servers und werden nicht mit anderen Daten
        zusammengeführt. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Der Hoster verarbeitet die Daten in unserem
        Auftrag auf Grundlage eines Vertrags zur Auftragsverarbeitung und löscht die Protokolle nach Ablauf der dort geltenden Fristen.</p>

      <h2>E-Mail und Telefon</h2>
      <p>Wenn Sie uns per E-Mail oder telefonisch kontaktieren, verarbeiten wir Ihre Angaben (Name, Kontaktdaten, Ihr
        Anliegen) ausschließlich, um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn
        Ihre Anfrage auf einen Auftrag zielt, im Übrigen Art. 6 Abs. 1 lit. f DSGVO aus unserem Interesse, Anfragen zu beantworten.</p>
      <p>Ihre Nachricht bleibt so lange in unserem Postfach, wie es für die Bearbeitung nötig ist. Kommt es zu einem
        Auftrag, bewahren wir den Schriftverkehr im Rahmen der handels- und steuerrechtlichen Aufbewahrungspflichten
        auf. Andernfalls löschen wir die Nachricht, sobald Ihr Anliegen erledigt ist.</p>

      <h2>Verweise auf andere Websites</h2>
      <p>Wo wir auf fremde Websites verweisen, handelt es sich um gewöhnliche Links, es wird nichts eingebettet. Erst
        wenn Sie einen solchen Link anklicken, gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>

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
      <p>Wenden Sie sich dazu formlos an die oben genannte Adresse. Sie haben außerdem das Recht, sich bei einer
        Aufsichtsbehörde zu beschweren. Zuständig ist der Hamburgische Beauftragte für Datenschutz und
        Informationsfreiheit, Ludwig-Erhard-Str. 22, 20459 Hamburg.</p>

      <h2>Keine automatisierten Entscheidungen</h2>
      <p>Wir treffen keine Entscheidungen, die ausschließlich auf einer automatisierten Verarbeitung beruhen, und erstellen keine Profile.</p>

      <p class="klein">Stand: {STAND}</p>
    </div>
  </section>
"""
    return html + footer(depth)

SEITEN = {"projekte/index.html": projekte_uebersicht, "studio/index.html": studio,
          "leistungen/index.html": leistungen, "kontakt/index.html": kontakt,
          "impressum/index.html": impressum, "datenschutz/index.html": datenschutz}
for _i, _pr in enumerate(PROJEKTE):
    SEITEN[f"projekte/{_pr['slug']}/index.html"] = (lambda i, pr: (lambda: projekt_detail(i, pr)))(_i, _pr)

if __name__ == "__main__":
    schreiben("index.html", startseite())
    if not PROBE:
        for pfad, fn in SEITEN.items():
            schreiben(pfad, fn())
        schreiben("sitemap.xml", sitemap())
