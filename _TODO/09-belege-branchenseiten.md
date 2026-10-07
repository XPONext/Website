# 09 · Belege auf den Branchenseiten

**Status:** offen · **Wartet auf:** 04
**Schließt:** `Beleg architekturbueros`, `Beleg bau-und-planung`, `Beleg hausverwaltungen`, `Beleg reisebueros`, `Beleg zulieferer`

## Ziel
Jede Branchenseite zeigt im Abschnitt „Beleg“ einen echten Fall aus genau dieser Branche
(Ausgangslage, Lösung, Ergebnis, z. B. gesparte Stunden pro Woche).

## Wo
`_content/landingpages/<branche>.yaml`, Block `beleg:`. Nicht im HTML, das wird überschrieben.

## Umsetzung
1. Fall aus der Branche mit Freigabe (Ticket 04). Gibt es noch keinen: Feld so lassen, die Seite
   bleibt in der Testphase (`index: false`).
2. In der YAML `text:` mit dem Fall füllen (Ausgangslage, Lösung, Zahl) und `platzhalter:` löschen:
   ```yaml
   beleg:
     titel: "Für Architekturbüros umgesetzt"
     text: "Ein Büro mit … Mitarbeitenden hat … Seitdem … (Zahl, Zeitraum)."
   ```
3. Gibt es eine passende Fallstudie auf `/projekte.html`, im Text darauf verlinken: `[Zum Projekt](/projekte.html)`.
4. `python3 _content/build_all.py`, Seite lokal ansehen.
5. Architekturbüros ist schon indexiert. Hier zuerst, das ist die wichtigste Branchenseite.

## Fertig, wenn
- [ ] Keine `platzhalter`-Zeile mehr in `beleg:` der fünf YAMLs
- [ ] Jede Zahl hat Zeitraum und Quelle
