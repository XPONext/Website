#!/usr/bin/env python3
"""Generator für den Musterentwurf Musterbüro Steinwerk.

Eine Projektliste (PROJEKTE) erzeugt Raster, Tabelle, vier Filterseiten und Chips —
nichts wird zweimal gepflegt (Brief Abschnitt 6). Kopf- und Fußzeile sind auf jeder
Seite identisch, relative Pfade je Ordnertiefe (lokal unter /, live unter
/musterentwuerfe/musterbuero-steinwerk/).

Aufruf:  python3 build.py [--probe]
--probe  schreibt nur index.html mit Kopfzeile, Statement und Filter + Raster (Hero-Probe).
"""
import sys
from pathlib import Path

SITE = Path("/Users/timbunger/Desktop/XPONext/Website XPO/Website/musterentwuerfe/musterbuero-steinwerk")
URL = "https://www.xponext.de/musterentwuerfe/musterbuero-steinwerk"
ROBOTS = "noindex, follow"
NAME = "Musterbüro Steinwerk"
MARKE = "Musterbüro Steinwerk"
JAHR = "2026"
DATUM = "2026-09-08"
TEL = "0221 000000"
TEL_INTL = "+49221000000"
MAIL = "info@musterbuero-steinwerk.de"
STRASSE, PLZ, ORT = "Musterstraße 1", "50679", "Köln"
PROBE = "--probe" in sys.argv

def p(depth):
    return "../" * depth

# ---------------------------------------------------------------- Projekte
# Reihenfolge = Anzeige: Jahr absteigend, innerhalb eines Jahres Foto → Modell → Baustelle (Brief 8.3).
# bildart: "Foto" | "Modell" | "Baustelle" — Chip nur für Modell und Baustelle, Tabelle nennt alle.
TYPEN = {"bildung": "Bildung", "verwaltung": "Verwaltung", "gewerbe": "Gewerbe", "wettbewerb": "Wettbewerb"}
TYP_SEITEN = {"bildung": ("Bildungsbauten", "Schulen, Kitas und Berufskollegs für Kommunen und Schulträger im Rheinland: Neubau, Erweiterung und Sanierung im laufenden Betrieb."),
              "verwaltung": ("Verwaltungsbauten", "Rathäuser, Feuerwachen, Bürgerhäuser und Betriebsgebäude kommunaler Unternehmen: Bauten, die über Jahrzehnte im Alltag stehen."),
              "gewerbe": ("Gewerbebauten", "Hallen, Bürogebäude und ein Gewerbehof für Unternehmen zwischen Köln und Bonn: kurze Bauzeiten, klare Abläufe, belastbare Kosten."),
              "wettbewerbe": ("Wettbewerbe", "Drei Wettbewerbsbeiträge der letzten Jahre: zwei realisierte erste Preise und ein dritter Preis, den das Modell zeigt.")}
TYP_SLUG = {"bildung": "bildung", "verwaltung": "verwaltung", "gewerbe": "gewerbe", "wettbewerb": "wettbewerbe"}

def pr(titel, ort, jahr, typ, massnahme, bildart, datei, alt, pos="center"):
    return dict(titel=titel, ort=ort, jahr=jahr, typ=typ, massnahme=massnahme, bildart=bildart, datei=datei, alt=alt, pos=pos)

PROJEKTE = [
    pr("Schulzentrum Kerpen", "Kerpen", "2026", "wettbewerb", "Wettbewerb, 1. Preis, realisiert", "Foto", "schulzentrum-01",
       "Luftbild des erweiterten Schulgeländes mit Flachdachbauten, Sportplatz und Bäumen im Gegenlicht"),
    pr("Verwaltungsgebäude Stadtwerke", "Bonn", "2025", "verwaltung", "Neubau", "Foto", "stadtwerke-01",
       "Neubau mit heller Metallfassade, auskragendem Vordach und Glasfront vor blauem Himmel"),
    pr("Sporthalle Wesseling", "Wesseling", "2025", "gewerbe", "Neubau", "Foto", "sporthalle-01",
       "Sporthalle mit beigefarbener Stehfalzfassade und zweiflügeligem Tor in Rot und Blau"),
    pr("Grundschule Am Ring", "Köln-Ehrenfeld", "2024", "bildung", "Umbau und Erweiterung", "Foto", "grundschule-ring-01",
       "Backsteinschule mit vorgesetzter Glashalle und weißem Zaun"),
    pr("Kita Rheinufer", "Köln-Poll", "2024", "bildung", "Neubau", "Foto", "kita-rheinufer-01",
       "Eingeschossige Kita mit roter Fassade, Glasfront und aufgeklapptem Dach am Vorplatz"),
    pr("Produktionshalle Frechen", "Frechen", "2024", "gewerbe", "Neubau", "Foto", "produktionshalle-01",
       "Luftbild einer Produktionshalle mit Sheddach, Parkplatz und Straßen"),
    pr("Gesamtschule Nord", "Leverkusen", "2023", "bildung", "Erweiterung", "Foto", "gesamtschule-nord-01",
       "Langer heller Flur des Erweiterungsbaus mit Fensterband und Blick ins Grüne"),
    pr("Rathaus-Anbau Pulheim", "Pulheim", "2023", "verwaltung", "Anbau", "Foto", "rathaus-anbau-01",
       "Anbau aus Sichtbeton und Glas mit Freitreppe neben dem Bestandsgebäude"),
    pr("Logistikhalle Ost", "Hürth", "2023", "gewerbe", "Neubau", "Foto", "logistikhalle-01",
       "Fassade der Halle aus graugrünem Wellblech und hellem Klinkersockel"),
    pr("Quartiersschule Düsseldorf", "Düsseldorf", "2023", "wettbewerb", "Wettbewerb, 3. Preis", "Modell", "quartiersschule-01",
       "Umgebungsmodell des Quartiers mit Bestandsgebäuden und Neubauvolumen", "center 40%"),
    pr("Bürogebäude Kalk", "Köln-Kalk", "2022", "gewerbe", "Neubau", "Foto", "buero-kalk-01",
       "Klinkerfassade des Bürogebäudes mit gestaffelten Fensterbändern, von unten gesehen"),
    pr("Berufskolleg Süd", "Bonn", "2022", "bildung", "Sanierung", "Foto", "berufskolleg-01",
       "Sanierte Klinkerfassade des Berufskollegs mit neuen Fensterbändern, Photovoltaik auf dem Dach und überdachten Fahrradständern im Hof"),
    pr("Feuerwache Bergisch Gladbach", "Bergisch Gladbach", "2022", "verwaltung", "Neubau", "Foto", "feuerwache-01",
       "Fahrzeughalle der Feuerwache mit blauer Trapezblechfassade und breitem Rolltor"),
    pr("Verwaltungszentrum Aachen", "Aachen", "2022", "wettbewerb", "Wettbewerb, 1. Preis, realisiert", "Foto", "verwaltungszentrum-01",
       "Weiße Plattenfassade des Verwaltungszentrums mit auskragendem Obergeschoss und verglasten Eingängen unter bedecktem Himmel"),
    pr("Mensa Gymnasium Brühl", "Brühl", "2021", "bildung", "Neubau", "Foto", "mensa-01",
       "Blick durch die geöffnete Lamellen-Schiebewand in den holzverkleideten Speisesaal mit Stuhlreihen"),
    pr("Kita Sonnenhang", "Erftstadt", "2021", "bildung", "Neubau", "Modell", "kita-sonnenhang-01",
       "Lageplanmodell aus Bronze mit Baumkugeln und Gebäudevolumen", "center 40%"),
    pr("Kita Waldstraße", "Köln-Dellbrück", "2020", "bildung", "Neubau, Holzbau", "Baustelle", "kita-waldstrasse-01",
       "Dachstuhl aus Holzbindern im Rohbau, davor gestapelte Balken"),
    pr("Grundschule Troisdorf", "Troisdorf", "2020", "bildung", "Anbau", "Baustelle", "grundschule-troisdorf-01",
       "Eingerüsteter Rohbau des Anbaus unter blauem Himmel, im Vordergrund Betonfertigteile"),
    pr("Gewerbehof Mülheim", "Köln-Mülheim", "2019", "gewerbe", "Umbau", "Baustelle", "gewerbehof-01",
       "Rohbau im Bestand mit neuen Ziegelwänden und gelagerten Platten"),
    pr("Bürgerhaus Rösrath", "Rösrath", "2019", "verwaltung", "Sanierung", "Baustelle", "buergerhaus-01",
       "Eingerüstete Fassade des Bürgerhauses während der Sanierung"),
]
for i, x in enumerate(PROJEKTE, start=1):
    x["nr"] = f"{i:02d}"
assert len(PROJEKTE) == 20
ANZAHL = {t: sum(1 for x in PROJEKTE if x["typ"] == t) for t in TYPEN}
assert ANZAHL == {"bildung": 8, "verwaltung": 4, "gewerbe": 5, "wettbewerb": 3}, ANZAHL

# ---------------------------------------------------------------- Rahmen
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
<link rel="preload" href="{p(depth)}assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p(depth)}assets/css/basis.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>

<a class="sprung" href="#inhalt">Zum Inhalt springen</a>
"""

NAV = [("projekte/", "Projekte"), ("leistungen/", "Leistungen"), ("buero/", "Büro"), ("kontakt/", "Kontakt")]

def header(depth, aktiv):
    CUR = ' aria-current="page"'
    li = "\n".join(
        f'        <li><a href="{p(depth)}{pfad}"{CUR if pfad == aktiv else ""}>{text}</a></li>'
        for pfad, text in NAV)
    return f"""<!-- Kopfzeile: wolveridge-com-au-F1 Dreiteilung Wortmarke · Navigation · Ort + Telefon,
     wolveridge-com-au-F10 Mobile-Menü als Vollbild, Text-Button statt Icon -->
<header class="kopf">
  <div class="kopf__inhalt inhalt">
    <a class="marke" href="{p(depth) or './'}" aria-label="{NAME}, zur Startseite">Musterbüro<span class="marke__lang"> Steinwerk</span></a>
    <button class="kopf__schalter" type="button" aria-expanded="false" aria-controls="hauptnavigation">Menü</button>
    <a class="kopf__schalter-nojs" href="#fuss-navigation">Menü</a>
    <nav class="kopf__nav" aria-label="Hauptnavigation">
      <ul class="reiter" id="hauptnavigation">
{li}
        <li class="reiter__kontakt mono"><a href="tel:{TEL_INTL}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></li>
      </ul>
    </nav>
    <a class="kopf__tel mono" href="tel:{TEL_INTL}"><span class="kopf__ort">Köln ·</span>{TEL}</a>
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
    "streetAddress": "{STRASSE}",
    "postalCode": "{PLZ}",
    "addressLocality": "{ORT}",
    "addressCountry": "DE"
  }},
  "areaServed": ["Köln", "Rheinland", "Nordrhein-Westfalen"]
}}
</script>
"""
    return f"""
</main>

<!-- Fußzeile: helenhard-no-F13 ein Standortblock, hell auf Fläche, vier Spalten -->
<footer class="fuss">
  <div class="inhalt">
    <div class="fuss__raster">
      <div>
        <p class="fuss__titel">Köln</p>
        <p>{NAME}<br>{STRASSE}<br>{PLZ} {ORT}</p>
        <p><a class="mono" href="tel:{TEL_INTL}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div>
        <p class="fuss__titel" id="fuss-navigation">Navigation</p>
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
          <li><a href="{p(depth)}bildnachweis/">Bildnachweis</a></li>
        </ul>
      </div>
      <div>
        <p class="fuss__titel">Projekte nach Typ</p>
        <ul class="fuss__liste">
          <li><a href="{p(depth)}projekte/bildung/">Bildungsbauten ({ANZAHL['bildung']})</a></li>
          <li><a href="{p(depth)}projekte/verwaltung/">Verwaltungsbauten ({ANZAHL['verwaltung']})</a></li>
          <li><a href="{p(depth)}projekte/gewerbe/">Gewerbebauten ({ANZAHL['gewerbe']})</a></li>
          <li><a href="{p(depth)}projekte/wettbewerbe/">Wettbewerbe ({ANZAHL['wettbewerb']})</a></li>
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

# ---------------------------------------------------------------- Projektbausteine
def chip(x):
    return f' <span class="chip">{x["bildart"]}</span>' if x["bildart"] != "Foto" else ""

def kachel(x, depth, erstes=False):
    lade = 'fetchpriority="high"' if erstes else 'loading="lazy"'
    stil = f' style="object-position:{x["pos"]}"' if x["pos"] != "center" else ""
    return f"""      <li class="kachel" data-typ="{x['typ']}">
        <div class="kachel__bild"><img src="{p(depth)}assets/bilder/kacheln/{x['datei']}-600.webp" srcset="{p(depth)}assets/bilder/kacheln/{x['datei']}-600.webp 600w, {p(depth)}assets/bilder/kacheln/{x['datei']}-900.webp 900w" sizes="(max-width: 719px) calc(100vw - 2rem), (max-width: 1099px) calc(50vw - 3rem), 296px" alt="{x['titel']}, {x['ort']} — {x['bildart']}: {x['alt']}" width="600" height="400" {lade}{stil}></div>
        <h3 class="kachel__titel">{x['titel']}</h3>
        <p class="kachel__meta mono"><span>{x['nr']} · {x['ort']} · {x['jahr']} · {x['massnahme']}</span>{chip(x)}</p>
      </li>"""

def raster(liste, depth, klasse="", stufe_h=None):
    items = "\n".join(kachel(x, depth, erstes=(i == 0 and depth == 0)) for i, x in enumerate(liste))
    return f"""
    <!-- Projektraster: wolveridge-com-au-F3 kleine 3:2-Kacheln, wolveridge-com-au-F4 Titel + Metazeile
         (Jahr absteigend), big-dk-F4 Ort in Versalien, wolveridge-com-au-F16 Chip „Modell"/„Baustelle" -->
    <ul class="raster raster4{klasse}" id="raster" aria-label="Projekte als Raster">
{items}
    </ul>"""

def tabelle(liste, klasse="", caption="Alle Projekte als Liste"):
    zeilen = "\n".join(
        f'          <tr data-typ="{x["typ"]}"><td class="nr">{x["nr"]}</td><td class="projekt">{x["titel"]}</td>'
        f'<td class="meta">{x["ort"]}</td><td class="meta">{x["jahr"]}</td><td class="meta">{TYPEN[x["typ"]]}</td>'
        f'<td class="meta">{x["massnahme"]}</td><td class="meta">{x["bildart"]}</td></tr>'
        for x in liste)
    return f"""
    <!-- Projektliste: wolveridge-com-au-F5 bildlose Tabelle mit Hairlines, alle sieben Spalten auch mobil -->
    <div class="liste{klasse}" id="liste">
      <table>
        <caption class="nur-sr">{caption}</caption>
        <colgroup><col style="width:48px"><col><col style="width:200px"><col style="width:64px"><col style="width:120px"><col style="width:220px"><col style="width:112px"></colgroup>
        <thead><tr><th scope="col">Nr</th><th scope="col">Projekt</th><th scope="col">Ort</th><th scope="col">Jahr</th><th scope="col">Typ</th><th scope="col">Maßnahme</th><th scope="col">Abbildung</th></tr></thead>
        <tbody>
{zeilen}
        </tbody>
      </table>
    </div>"""

CUR = ' aria-current="page"'

def filterzeile(depth, aktiv_typ, ansicht, alle_href):
    """aktiv_typ: None (alle) oder Typ-Schlüssel. ansicht: 'raster' | 'liste' | 'beide'."""
    def f(href, text, typ, cur):
        return f'          <li><a href="{href}" data-filter="{typ}"{CUR if cur else ""}>{text}</a></li>'
    eintraege = [f(alle_href, f"Alle ({len(PROJEKTE)})", "", aktiv_typ is None)]
    for t, name in TYPEN.items():
        eintraege.append(f(f"{p(depth)}projekte/{TYP_SLUG[t]}/", f"{name} ({ANZAHL[t]})", t, aktiv_typ == t))
    if ansicht == "beide":
        # Filterseiten (Brief 6): Raster und darunter die Tabelle, beide sichtbar — die Einträge sind
        # Sprunglinks, beide als gesetzt markiert; basis.js lässt sie auf diesen Seiten unangetastet.
        r = f'          <li><a href="#raster" data-ansicht="raster" class="an">[x] Raster</a></li>'
        l = f'          <li><a href="#liste" data-ansicht="liste" class="an">[x] Liste</a></li>'
    elif ansicht == "raster":
        r = f'          <li><a href="{p(depth)}#projekte" data-ansicht="raster" aria-current="page">[x] Raster</a></li>'
        l = f'          <li><a href="{p(depth)}projekte/" data-ansicht="liste">[ ] Liste</a></li>'
    else:
        r = f'          <li><a href="{p(depth)}#projekte" data-ansicht="raster">[ ] Raster</a></li>'
        l = f'          <li><a href="{p(depth)}projekte/" data-ansicht="liste" aria-current="page">[x] Liste</a></li>'
    return f"""
    <!-- Filterzeile: helenhard-no-F8 Filter nach Typologie (Links auf statische Filterseiten, mit JS in-place),
         wolveridge-com-au-F2 Umschalter [x] Raster [ ] Liste, wolveridge-com-au-F8 Grau = inaktiv -->
    <div class="filterzeile" id="projekte">
      <nav aria-label="Projekte nach Typ filtern">
        <ul class="filter">
{chr(10).join(eintraege)}
        </ul>
      </nav>
      <nav aria-label="Ansicht wählen">
        <ul class="umschalter">
{r}
{l}
        </ul>
      </nav>
    </div>"""

# ---------------------------------------------------------------- Startseite
def startseite():
    d = 0
    html = head(d, "Musterbüro Steinwerk, Köln: Schulen, Kitas, Verwaltung",
                "Architekturbüro in Köln für Schulen, Kitas, Verwaltungs- und Gewerbebauten im Rheinland. 20 Projekte, 14 Mitarbeitende, Wettbewerbe und VgV-Verfahren.", "")
    html += header(d, None)
    html += f"""
  <!-- Statement als H1 statt Hero-Bild (Wow-Faktor, Brief 1 und 3); Metadatenblock rechts: big-dk-F2, big-dk-F3 -->
  <section class="inhalt statement raster4" aria-label="Über das Büro">
    <h1>Schulen, Kitas, Verwaltungs- und Gewerbebauten im Rheinland — von der Machbarkeitsstudie bis zur Übergabe.</h1>
    <div class="metablock">
      <dl>
        <div class="trenner"><dt class="mono">Standort</dt> <dd>Köln</dd></div>
        <div class="trenner"><dt class="mono">Team</dt> <dd>14</dd></div>
        <div class="trenner"><dt class="mono">Projekte</dt> <dd>20</dd></div>
        <div><dt class="mono">Wettbewerbe</dt> <dd>3</dd></div>
      </dl>
    </div>
  </section>

  <section class="inhalt" aria-labelledby="projekte-titel" data-projekte>
    <h2 class="nur-sr" id="projekte-titel">Projekte</h2>
{filterzeile(d, None, "raster", "#projekte")}
{raster(PROJEKTE, d)}
{tabelle(PROJEKTE, " nur-js")}
  </section>
"""
    html += footer(d, jsonld=True)
    schreiben("index.html", html)

# ---------------------------------------------------------------- Projekte (Liste) und Filterseiten
def projekte_liste():
    d = 1
    html = head(d, "Projekte | Musterbüro Steinwerk, Köln",
                "Alle 20 Projekte von Musterbüro Steinwerk als Liste: Bildung, Verwaltung, Gewerbe und Wettbewerbe mit Ort, Jahr, Maßnahme und Bildart. Köln, Rheinland, NRW.", "projekte/")
    html += header(d, "projekte/")
    html += f"""
  <section class="inhalt seitenkopf raster4" aria-label="Projekte">
    <h1>Projekte</h1>
    <p class="einleitung">Zwanzig Bauten und Wettbewerbe zwischen Aachen, Düsseldorf und Bonn, nach Jahr geordnet. Die Spalte „Abbildung" sagt, was das Bild im Raster zeigt: ein Foto des fertigen Gebäudes, ein Modell oder die Baustelle.</p>
  </section>

  <section class="inhalt" aria-labelledby="liste-titel" data-projekte>
    <h2 class="nur-sr" id="liste-titel">Alle Projekte</h2>
{filterzeile(d, None, "liste", "./")}
{raster(PROJEKTE, d, " nur-js")}
{tabelle(PROJEKTE)}
  </section>
"""
    html += footer(d)
    schreiben("projekte/index.html", html)

def filterseite(typ):
    d = 2
    slug = TYP_SLUG[typ]
    h1, einleitung = TYP_SEITEN[slug]
    liste = [x for x in PROJEKTE if x["typ"] == typ]
    orte = ", ".join(dict.fromkeys(x["ort"].split("-")[0] for x in liste))
    desc = f"{h1} von Musterbüro Steinwerk, Köln: {len(liste)} Projekte in {orte}. Mit Jahr, Maßnahme und Bildart."
    if len(desc) > 160:
        desc = f"{h1} von Musterbüro Steinwerk, Köln: {len(liste)} Projekte im Rheinland mit Ort, Jahr, Maßnahme und Bildart."
    html = head(d, f"{h1} | Musterbüro Steinwerk, Köln", desc, f"projekte/{slug}/")
    html += header(d, "projekte/")
    html += f"""
  <section class="inhalt seitenkopf raster4" aria-label="{h1}">
    <h1>{h1}</h1>
    <p class="einleitung">{einleitung}</p>
  </section>

  <!-- Filterseite ohne JavaScript-Pflicht: Raster und Tabelle derselben {len(liste)} Projekte -->
  <section class="inhalt" aria-labelledby="auswahl-titel" data-projekte data-ansicht="beide">
    <h2 class="nur-sr" id="auswahl-titel">{h1} als Raster und Liste</h2>
{filterzeile(d, typ, "beide", p(d) + "#projekte")}
{raster(liste, d)}
{tabelle(liste, caption=f"{h1} als Liste")}
  </section>
"""
    html += footer(d)
    schreiben(f"projekte/{slug}/index.html", html)

# ---------------------------------------------------------------- Büro
def buero():
    d = 1
    html = head(d, "Büro | Musterbüro Steinwerk, Köln",
                "Musterbüro Steinwerk: 14 Mitarbeitende, drei Geschäftsführende, Sitz in Köln. Planung für Kommunen, Schulträger und Unternehmen im Rheinland.", "buero/")
    html += header(d, "buero/")
    html += f"""
  <section class="inhalt seitenkopf raster4" aria-label="Büro">
    <h1>Ein Büro mit vierzehn Leuten in Köln, das die Abläufe öffentlicher Auftraggeber kennt.</h1>
  </section>

  <!-- Bürotext Spalten 1–2, Metadatenblock rechts: big-dk-F2, big-dk-F3 -->
  <section class="inhalt raster4 fliesstext" aria-label="Über uns" style="margin-top:3rem">
    <div class="buero__text">
      <p>Wir planen Schulen, Kitas, Verwaltungs- und Gewerbebauten im Rheinland, von der Machbarkeitsstudie bis zur Übergabe. Viele unserer Projekte entstehen aus Wettbewerben und VgV-Verfahren. Wir wissen, wie ein Schulträger entscheidet, was ein Gemeinderat sehen will und welche Unterlagen ein Fördermittelgeber braucht.</p>
      <p>Das Büro wurde 2011 gegründet und wird von drei Geschäftsführenden geleitet, alle in die Architektenliste der Architektenkammer Nordrhein-Westfalen eingetragen. Die Projektverantwortung liegt bei ihnen, nicht bei einer wechselnden Bürostruktur.</p>
      <h2>Team</h2>
      <p>Vierzehn Personen: neun Architektinnen und Architekten, drei Bauzeichnerinnen und Bauzeichner, zwei in der Verwaltung. Jedes Projekt hat eine feste Projektleitung, die vom ersten Termin bis zur Abnahme dieselbe bleibt. Tragwerk, Haustechnik und Brandschutz koordinieren wir als Generalplaner mit festen Fachplanern.</p>
      <h2>Arbeitsweise</h2>
      <p>Bei Sanierungen und Erweiterungen planen wir den Bauablauf so, dass der Betrieb weiterläuft: Bauabschnitte nach Schulferien, Lärmfenster, getrennte Wege für Baustelle und Kinder. Kosten führen wir ab der Vorplanung nach DIN 276 fort und legen sie in jeder Phase offen. Renderings und Modellfotos kennzeichnen wir auch auf dieser Website als solche, damit niemand ein Bild für ein fertiges Gebäude hält.</p>
    </div>
    <div class="buero__meta metablock">
      <dl>
        <div class="trenner"><dt class="mono">Gegründet</dt> <dd>2011</dd></div>
        <div class="trenner"><dt class="mono">Team</dt> <dd>14</dd></div>
        <div class="trenner"><dt class="mono">Projekte</dt> <dd>20</dd></div>
        <div><dt class="mono">Wettbewerbe</dt> <dd>3</dd></div>
      </dl>
    </div>

    <!-- Ein Bild statt Portraits: die Baustelle als Bürofoto, Chip „Baustelle" (wolveridge-com-au-F16) -->
    <figure class="buero__bild">
      <div class="kachel__bild"><img src="{p(d)}assets/bilder/kacheln/buero-kita-waldstrasse-1320.webp" alt="Kita Waldstraße, Köln-Dellbrück — Baustelle: Dachstuhl aus Holzbindern im Rohbau, davor gestapelte Balken" width="1320" height="880" loading="lazy"></div>
      <figcaption class="kachel__meta mono"><span>Kita Waldstraße · Köln-Dellbrück · 2020</span> <span class="chip">Baustelle</span></figcaption>
    </figure>

    <!-- Büro in Zahlen: helenhard-no-F9 Label-Wert-Tabelle mit Hairlines -->
    <div class="zahlen">
      <h2>Büro in Zahlen</h2>
      <dl style="margin-top:1.5rem">
        <dt class="mono">Sitz</dt><dd>Köln</dd>
        <dt class="mono">Geschäftsführung</dt><dd>Drei Geschäftsführende, alle in die Architektenliste der Architektenkammer NRW eingetragen</dd>
        <dt class="mono">Mitarbeitende</dt><dd>9 Architektinnen und Architekten, 3 Bauzeichnerinnen und Bauzeichner, 2 Verwaltung</dd>
        <dt class="mono">Kammer</dt><dd>Architektenkammer Nordrhein-Westfalen</dd>
        <dt class="mono">Leistungsphasen</dt><dd>1 bis 9 nach HOAI, Generalplanung mit Fachplanern</dd>
        <dt class="mono">Auftraggeber</dt><dd>Kommunen, Schulträger, kommunale Unternehmen, Gewerbe</dd>
        <dt class="mono">Region</dt><dd>Köln, Rheinland, Nordrhein-Westfalen</dd>
        <dt class="mono">Verfahren</dt><dd>Wettbewerbe, VgV-Verfahren, Direktbeauftragung</dd>
      </dl>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("buero/index.html", html)

# ---------------------------------------------------------------- Leistungen
def leistungen():
    d = 1
    html = head(d, "Leistungen | Musterbüro Steinwerk, Köln",
                "Bildungsbauten, Verwaltungs- und Gewerbebau, Sanierung im laufenden Betrieb, Wettbewerbe, VgV-Verfahren und Generalplanung: Leistungen von Musterbüro Steinwerk.", "leistungen/")
    html += header(d, "leistungen/")
    html += f"""
  <section class="inhalt seitenkopf raster4" aria-label="Leistungen">
    <h1>Fünf Leistungsfelder, alle Leistungsphasen.</h1>
    <p class="einleitung">Wir übernehmen die Leistungsphasen 1 bis 9 nach HOAI, einzeln oder als Generalplanung mit Fachplanern für Tragwerk, Haustechnik und Brandschutz. Bei öffentlichen Auftraggebern beginnt die Zusammenarbeit meist mit einem Wettbewerb oder VgV-Verfahren.</p>
  </section>

  <!-- Leistungen: helenhard-no-F9 Zeilen mit Hairline, Label Spalten 1–2, Text Spalten 3–4 -->
  <section class="inhalt fliesstext" aria-label="Leistungsfelder">
    <ul class="leistungen">
      <li class="leistung raster4" id="bildung">
        <h2>Bildungsbauten</h2>
        <div>
          <p>Schulen, Kitas und Berufskollegs: Neubau, Erweiterung und Sanierung. Wir kennen die Raumprogramme der Schulträger, die Anforderungen an Inklusion, Ganztag und Brandschutz und die Förderprogramme, mit denen Kommunen diese Bauten finanzieren.</p>
          <p>Acht Projekte, von der Kita in Holzbauweise bis zur Erweiterung einer Gesamtschule: <a href="{p(d)}projekte/bildung/">Bildungsbauten ansehen</a>.</p>
        </div>
      </li>
      <li class="leistung raster4" id="verwaltung">
        <h2>Verwaltungsbau</h2>
        <div>
          <p>Rathäuser, Feuerwachen, Bürgerhäuser und Betriebsgebäude kommunaler Unternehmen. Flexible Grundrisse, die sich nach Jahren umnutzen lassen, und Gebäudetechnik, die der Bauhof selbst betreiben kann.</p>
          <p>Vier Projekte: <a href="{p(d)}projekte/verwaltung/">Verwaltungsbauten ansehen</a>.</p>
        </div>
      </li>
      <li class="leistung raster4" id="gewerbe">
        <h2>Gewerbebau</h2>
        <div>
          <p>Produktions- und Logistikhallen, Bürogebäude und Gewerbehöfe für Unternehmen im Rheinland. Termin- und Kostensicherheit stehen hier über allem: Wir planen mit Fertigteilen und Systembauweisen, wo es passt, und schreiben so aus, dass die Angebote vergleichbar sind.</p>
          <p>Fünf Projekte: <a href="{p(d)}projekte/gewerbe/">Gewerbebauten ansehen</a>.</p>
        </div>
      </li>
      <li class="leistung raster4" id="sanierung">
        <h2>Sanierung und Erweiterung im laufenden Betrieb</h2>
        <div>
          <p>Ein Schulgebäude wird während des Unterrichts saniert, ein Rathaus während der Öffnungszeiten erweitert. Wir planen Bauabschnitte, Ausweichflächen und Baustellenlogistik so, dass der Betrieb weitergeht, und stimmen den Ablauf mit Schulleitung, Hausmeister und Ordnungsamt ab.</p>
          <p>Beispiele: Berufskolleg Süd in Bonn, Gesamtschule Nord in Leverkusen, Bürgerhaus Rösrath.</p>
        </div>
      </li>
      <li class="leistung raster4" id="wettbewerbe">
        <h2>Wettbewerbe und VgV-Verfahren</h2>
        <div>
          <p>Wir nehmen an offenen und nichtoffenen Wettbewerben teil und bewerben uns in VgV-Verfahren, allein oder in Arbeitsgemeinschaft mit Landschaftsarchitekten und Fachplanern. Die Referenzliste auf dieser Website ist so aufgebaut, wie Vergabestellen sie abfragen: Ort, Jahr, Maßnahme, Bildart.</p>
          <p>Drei Ergebnisse der letzten Jahre: <a href="{p(d)}projekte/wettbewerbe/">Wettbewerbe ansehen</a>.</p>
        </div>
      </li>
    </ul>
  </section>
"""
    html += footer(d)
    schreiben("leistungen/index.html", html)

# ---------------------------------------------------------------- Kontakt
def kontakt():
    d = 1
    html = head(d, "Kontakt | Musterbüro Steinwerk, Köln",
                f"Musterbüro Steinwerk, {STRASSE}, {PLZ} {ORT}. Telefon {TEL}, {MAIL}. Montag bis Freitag 8 bis 17 Uhr.", "kontakt/")
    html += header(d, "kontakt/")
    html += f"""
  <section class="inhalt seitenkopf raster4" aria-label="Kontakt">
    <h1>Kontakt</h1>
  </section>

  <!-- Kontakt: Kasten auf Fläche mit Klartext-Kontaktwegen, einziger gefüllter Button (mailto), keine Karte, kein Formular -->
  <section class="inhalt kontakt raster4 fliesstext" aria-label="Anschrift und Erreichbarkeit">
    <div class="kontakt__kasten">
      <p class="label">Köln</p>
      <p>{NAME}<br>{STRASSE}<br>{PLZ} {ORT}</p>
      <p style="margin-top:1rem"><a class="mono" href="tel:{TEL_INTL}">{TEL}</a> <span class="mono">(Musterangabe)</span><br><a href="mailto:{MAIL}">{MAIL}</a></p>
      <p><a class="knopf" href="mailto:{MAIL}">E-Mail schreiben</a></p>
    </div>
    <div class="kontakt__text">
      <h2>So erreichen Sie uns</h2>
      <p>Montag bis Freitag von 8 bis 17 Uhr telefonisch über das Sekretariat, das Sie mit der zuständigen Projektleitung verbindet. Für Anfragen zu Wettbewerben und VgV-Verfahren schreiben Sie bitte an die Geschäftsführung über die E-Mail-Adresse links; wir antworten innerhalb von zwei Arbeitstagen.</p>
      <p>Das Büro liegt im rechtsrheinischen Köln, wenige Gehminuten von einer Haltestelle des Nahverkehrs entfernt. Parkplätze gibt es im Hof, bitte melden Sie sich vorher an. Anschrift und Rufnummer auf dieser Seite sind Musterangaben.</p>
    </div>
  </section>
"""
    html += footer(d)
    schreiben("kontakt/index.html", html)

# ---------------------------------------------------------------- Rechtstexte
def rechtstext(pfad, title, desc, inhalt):
    d = 1
    html = head(d, title, desc, pfad) + header(d, None)
    html += f"""
  <section class="inhalt recht">
    <div class="inhalt--schmal fliesstext" style="padding:0">
{inhalt}
    </div>
  </section>
"""
    html += footer(d)
    schreiben(f"{pfad}index.html", html)

def impressum():
    rechtstext("impressum/", "Impressum | Musterbüro Steinwerk, Köln",
               "Impressum von Musterbüro Steinwerk, Köln: Anschrift, Geschäftsführung, Kammer, Berufshaftpflicht, Umsatzsteuer-Identifikationsnummer.", f"""
      <p class="label">Rechtliches</p>
      <h1>Impressum</h1>

      <h2>Angaben gemäß § 5 DDG</h2>
      <p>{NAME}<br>{STRASSE}<br>{PLZ} {ORT}</p>
      <p>Vertreten durch die Geschäftsführung: drei Architektinnen und Architekten, alle in die Architektenliste der Architektenkammer Nordrhein-Westfalen eingetragen</p>
      <p>Rechtsform und Registereintrag: Musterangabe</p>

      <h2>Kontakt</h2>
      <p>Telefon: <a href="tel:{TEL_INTL}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

      <h2>Berufsbezeichnung und Kammer</h2>
      <p>Berufsbezeichnung: Architektin / Architekt (verliehen in der Bundesrepublik Deutschland)<br>
        Zuständige Kammer: Architektenkammer Nordrhein-Westfalen, Zollhof 1, 40221 Düsseldorf<br>
        Berufsrechtliche Regelungen: Baukammerngesetz NRW und Berufsordnung, einsehbar über <a href="https://www.aknw.de" rel="noopener">aknw.de</a></p>

      <h2>Umsatzsteuer</h2>
      <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE000000000</p>

      <h2>Berufshaftpflichtversicherung</h2>
      <p>Musterversicherung AG (Musterangabe), Musterstraße 1, 50672 Köln<br>Räumlicher Geltungsbereich: Deutschland</p>

      <h2>Verantwortlich für den Inhalt</h2>
      <p>Die Geschäftsführung (Musterangabe), Anschrift wie oben</p>

      <h2>Streitbeilegung</h2>
      <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

      <h2>Bildnachweise</h2>
      <p>Alle Fotografien auf dieser Website sind Stockmaterial von Pexels (Lizenz: kommerziell nutzbar, keine Namensnennung erforderlich). Die Zuordnung je Datei steht im <a href="../bildnachweis/">Bildnachweis</a>.</p>

      <p class="klein">Diese Website ist ein Musterentwurf von XPONext (xponext.de). Büro, Personen und Projekte sind erfunden. Anschrift, Rufnummer, E-Mail-Adresse sowie sämtliche Register-, Steuer- und Versicherungsangaben sind Musterangaben. Die Fotografie ist Stockmaterial, Nachweis siehe oben.</p>""")

def datenschutz():
    rechtstext("datenschutz/", "Datenschutz | Musterbüro Steinwerk, Köln",
               "Datenschutzerklärung von Musterbüro Steinwerk: keine Cookies, keine Analyse-Werkzeuge, keine fremden Server. Protokolle, E-Mail, Ihre Rechte.", f"""
      <p class="label">Rechtliches</p>
      <h1>Datenschutzerklärung</h1>
      <p>Diese Website kommt ohne Cookies, ohne Analyse-Werkzeuge und ohne Inhalte von fremden Servern aus. Was beim Besuch und bei einer Kontaktaufnahme per E-Mail oder Telefon mit Ihren Daten geschieht, steht hier.</p>

      <h2>Verantwortliche Stelle</h2>
      <p>{NAME}<br>Vertreten durch die Geschäftsführung<br>{STRASSE}, {PLZ} {ORT}<br>Telefon: <a href="tel:{TEL_INTL}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Ein Datenschutzbeauftragter ist nicht bestellt, weil die gesetzlichen Voraussetzungen dafür nicht vorliegen.</p>

      <h2>Besuch der Website</h2>
      <p>Beim Aufruf der Seiten werden keine Cookies gesetzt und keine Analyse- oder Statistikwerkzeuge eingesetzt. Alle Schriften, Bilder und Skripte liegen auf dem eigenen Webspace. Es werden keine Inhalte von fremden Servern nachgeladen.</p>

      <h3>Hosting und Server-Protokolle</h3>
      <p>Die Website wird bei einem deutschen Hosting-Anbieter betrieben. Wie jeder Webserver zeichnet der Server bei jedem Aufruf technische Daten in Protokolldateien auf:</p>
      <ul>
        <li>IP-Adresse des aufrufenden Geräts</li>
        <li>Datum und Uhrzeit des Aufrufs</li>
        <li>aufgerufene Seite und übertragene Datenmenge</li>
        <li>Browser und Betriebssystem, soweit übermittelt</li>
        <li>die zuvor besuchte Seite, soweit der Browser sie übermittelt</li>
      </ul>
      <p>Diese Daten dienen dem sicheren und störungsfreien Betrieb des Servers und werden nicht mit anderen Daten zusammengeführt. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Der Hoster verarbeitet die Daten in unserem Auftrag auf Grundlage eines Vertrags zur Auftragsverarbeitung und löscht die Protokolle nach Ablauf der dort geltenden Fristen.</p>

      <h2>E-Mail und Telefon</h2>
      <p>Wenn Sie uns per E-Mail oder telefonisch kontaktieren, verarbeiten wir Ihre Angaben ausschließlich, um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn Ihre Anfrage auf einen Auftrag zielt, im Übrigen Art. 6 Abs. 1 lit. f DSGVO aus unserem Interesse, Anfragen zu beantworten.</p>
      <p>Ihre Nachricht bleibt so lange in unserem Postfach, wie es für die Bearbeitung nötig ist. Kommt es zu einem Auftrag, bewahren wir den Schriftverkehr im Rahmen der handels- und steuerrechtlichen Aufbewahrungspflichten auf. Andernfalls löschen wir die Nachricht, sobald Ihr Anliegen erledigt ist.</p>

      <h2>Verweise auf andere Websites</h2>
      <p>Wo wir auf fremde Websites verweisen (etwa auf die Architektenkammer im Impressum), handelt es sich um gewöhnliche Links, es wird nichts eingebettet. Erst wenn Sie einen solchen Link anklicken, gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>

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
      <p>Wenden Sie sich dazu formlos an die oben genannte Adresse. Sie haben außerdem das Recht, sich bei einer Aufsichtsbehörde zu beschweren. Zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit NRW, Kavalleriestraße 2-4, 40213 Düsseldorf.</p>

      <h2>Keine automatisierten Entscheidungen</h2>
      <p>Wir treffen keine Entscheidungen, die ausschließlich auf einer automatisierten Verarbeitung beruhen, und erstellen keine Profile.</p>

      <p class="klein">Stand: September 2026</p>""")

# ---------------------------------------------------------------- Bildnachweis (aus BILDER.md der Projektbilder)
def bildnachweis():
    zeilen = []
    for line in (SITE / "assets/bilder/projekte/BILDER.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("| Datei") or line.startswith("|---"):
            continue
        z = [c.strip() for c in line.strip("|").split("|")]
        datei, fotograf, quelle = z[0], z[1], z[2]
        proj = next((x for x in PROJEKTE if x["datei"] + ".webp" == datei), None)
        titel = f'{proj["titel"]} ({proj["bildart"]})' if proj else datei
        zeilen.append(f'          <tr><td class="projekt">{titel}</td><td>{datei}</td><td>{fotograf}</td><td><a href="{quelle}" rel="noopener">pexels.com/photo/{quelle.rstrip("/").split("-")[-1]}</a></td></tr>')
    rechtstext("bildnachweis/", "Bildnachweis | Musterbüro Steinwerk, Köln",
               "Bildnachweis des Musterentwurfs: alle 20 Projektbilder sind Stockfotografie von Pexels, hier je Datei mit Fotograf und Quelle aufgeführt.", f"""
      <p class="label">Rechtliches</p>
      <h1>Bildnachweis</h1>
      <p>Alle Bilder auf dieser Website sind Stockmaterial von Pexels (Pexels-Lizenz: kommerziell nutzbar, keine Namensnennung erforderlich). Kein Bild zeigt ein Projekt des Büros; das Büro und seine Projekte sind fiktiv (Musterentwurf). Die Kacheln im Raster sind aus den hier genannten Quellbildern auf 600 und 900 Pixel Breite beschnitten.</p>
      <p class="klein nachweis__hinweis">Die Tabelle lässt sich auf schmalen Bildschirmen seitlich verschieben.</p>
      <div class="nachweis">
      <table>
        <caption class="nur-sr">Bildquellen je Datei</caption>
        <thead><tr><th scope="col">Verwendung</th><th scope="col">Datei</th><th scope="col">Fotograf</th><th scope="col">Quelle</th></tr></thead>
        <tbody>
{chr(10).join(zeilen)}
        </tbody>
      </table>
      </div>""")

# ---------------------------------------------------------------- Sitemap
def sitemap():
    seiten = [("", "1.0"), ("projekte/", "0.9")] + [(f"projekte/{TYP_SLUG[t]}/", "0.8") for t in TYPEN] + \
             [("leistungen/", "0.8"), ("buero/", "0.7"), ("kontakt/", "0.6"), ("bildnachweis/", "0.2")]
    urls = "\n".join(f"  <url><loc>{URL}/{pf}</loc><lastmod>{DATUM}</lastmod><priority>{pr}</priority></url>" for pf, pr in seiten)
    schreiben("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

if __name__ == "__main__":
    startseite()
    if not PROBE:
        projekte_liste()
        for t in TYPEN:
            filterseite(t)
        buero()
        leistungen()
        kontakt()
        impressum()
        datenschutz()
        bildnachweis()
        sitemap()
