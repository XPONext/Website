# 01 · Einstiegspreise je Leistung

**Status:** offen · **Art:** Entscheidung + Einbau · **Schließt:** `Einstiegspreise` in `leistungen.html`

## Ziel
Unter der Preistabelle auf `/leistungen.html` stehen konkrete „ab“-Preise je Leistung, damit Besucher
vor dem Erstgespräch wissen, in welcher Größenordnung sie liegen.

## Wo
`leistungen.html`, Abschnitt mit der Tabelle „Leistung / Abrechnung / Rahmen“, Kasten
`<div class="ph ph--block" data-ph="Einstiegspreise">` direkt unter `</table></div>`.

## Umsetzung
1. Intern festlegen (Tim und Simon): ein „ab“-Preis je Zeile der Tabelle (Website, SEO/GEO/Google Ads,
   KI-Automatisierung). Netto oder brutto entscheiden und dazuschreiben.
2. Am einfachsten die Tabelle um eine Spalte ergänzen statt eines eigenen Kastens:
   ```html
   <th>ab</th>
   …
   <td data-label="ab">ab X.XXX € netto</td>
   ```
   `data-label` ist nötig, weil die Tabelle auf dem Handy gestapelt wird (`content-table--stack`).
3. Den Platzhalter-Kommentar und den `ph`-Kasten löschen.
4. Prüfen, ob die FAQ „Was kostet die Zusammenarbeit?“ auf der Startseite (`index.html`) noch passt.
   Das FAQ-Schema baut sich beim Build automatisch aus dem sichtbaren Text neu.

## Fertig, wenn
- [ ] Jede Leistung hat einen „ab“-Preis, netto/brutto ist klar
- [ ] Handy-Ansicht der Tabelle geprüft
- [ ] FAQ und Leistungsseite widersprechen sich nicht
