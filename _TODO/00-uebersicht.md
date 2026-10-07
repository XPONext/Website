# Offene Aufgaben Website

Stand: 07.10.2026. Ein Ticket je Datei. Die gelben Platzhalter-Kästen auf der Website (`class="ph"`,
`data-ph="…"`) sind der Maßstab: Jedes Ticket sagt, welche Kästen es schließt.

> Das Repo ist öffentlich. In diese Tickets keine Kundennamen, Preise, Zugangsdaten oder internen
> Absprachen schreiben. `_TODO/` wird von GitHub Pages nicht ausgeliefert, ist auf GitHub aber lesbar.

## Live-Stand (Branch `website-live`)

Live ist die Website ohne Platzhalter. So ist das gelöst, damit Inhalte später nur eingesetzt werden müssen:

- `css/site.css` (am Ende): `.ph { display: none }` blendet alle gelben Kästen aus.
- Abschnitte, die nur aus Platzhaltern bestehen, tragen das Attribut `hidden`, z. B. die Fallstudien auf
  der Startseite, die Kundenlogos, „Warum es XPONext gibt“ auf Über uns, Fallstudien und Kundenstimmen
  auf der Projekte-Seite, die Teamfoto-Spalte und die Karte „Termin buchen“ auf der Startseite.
- Projekte-Seite: `noindex`, nicht im Menü und nicht in der Fußzeile (`PROJEKTE_ZEIGEN = False` in
  `_content/layout.py`), steht deshalb auch nicht in der Sitemap.
- Branchenseiten: Beleg- oder Angebotsspalte ohne Text in der YAML wird automatisch ausgeblendet.
- Kontaktseite: Überschrift „So erreichen Sie uns“ statt „Termin wählen“, bis der Kalender steht.

**Beim Erledigen eines Tickets daher immer auch:** `hidden` am betroffenen Abschnitt entfernen,
bei der Projekte-Seite `PROJEKTE_ZEIGEN = True` und `index, follow` setzen. Alle Stellen findet
`grep -rn " hidden" --include=*.html .` bzw. `grep -rn "Live-Stand" .`.

## Arbeitsweise

1. Ticket öffnen, Status oben auf `in Arbeit` setzen.
2. Umsetzen wie beschrieben, dann `python3 _content/build_all.py` laufen lassen.
   Die Ausgabe listet die noch offenen Platzhalter.
3. Lokal prüfen: `python3 -m http.server 8000` → http://localhost:8000, mit Cmd+Shift+R neu laden.
4. Ticket-Datei löschen (oder nach `_TODO/erledigt/` verschieben) und im selben Commit mitcommitten.

Vor dem Livegang: `python3 _content/build_all.py --streng` bricht ab, solange noch ein Kasten offen ist.

## Reihenfolge

Erst entscheiden, dann Freigaben holen, dann einbauen. Die Entscheidungen blockieren andere Tickets.

| Nr. | Ticket | Art | Wartet auf |
|---|---|---|---|
| 01 | [Einstiegspreise](01-einstiegspreise.md) | Entscheidung | – |
| 02 | [Risikoumkehr](02-risikoumkehr.md) | Entscheidung | – |
| 03 | [Angebote Branchenseiten](03-angebote-branchenseiten.md) | Entscheidung | – |
| 04 | [Kundenfreigaben einholen](04-kundenfreigaben.md) | Organisation | – |
| 05 | [Kundenlogos](05-kundenlogos.md) | Inhalt | 04 |
| 06 | [Fallstudien Startseite](06-fallstudien-startseite.md) | Inhalt | 04 |
| 07 | [Projekte-Seite](07-projekte-seite.md) | Inhalt | 04, 06 |
| 08 | [Kundenstimmen](08-kundenstimmen.md) | Inhalt | 04 |
| 09 | [Belege Branchenseiten](09-belege-branchenseiten.md) | Inhalt | 04 |
| 10 | [Teamfoto aus dem Shooting](10-teamfoto.md) | Inhalt | Shooting |
| 11 | [Videos](11-videos.md) | Inhalt | Dreh |
| 12 | [Gründergeschichte](12-gruendergeschichte.md) | Text | – |
| 13 | [Buchungskalender](13-buchungskalender.md) | Technik | – |
| 14 | [Resend für GEO-Check-Leads](14-resend-geo-leads.md) | Technik | – |
| 15 | [Bildrechte bestätigen](15-bildrechte.md) | Recht | – |
| 16 | [3D-Logo abschließen](16-3d-logo-abschliessen.md) | Technik | – |
