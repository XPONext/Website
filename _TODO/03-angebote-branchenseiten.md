# 03 · Angebote auf den Branchenseiten

**Status:** offen · **Art:** Entscheidung + Einbau
**Schließt:** `Angebot bau-und-planung`, `Angebot hausverwaltungen`, `Angebot reisebueros`, `Angebot zulieferer`

## Ziel
Jede Branchenseite unter `/fuer/<branche>/` nennt im Abschnitt „So starten wir“ ein konkretes
Einstiegsangebot. Architekturbüros hat schon einen Text und dient als Vorbild.

## Wo
Nicht im HTML! Die Seiten werden gebaut aus `_content/landingpages/<branche>.yaml`, Block `angebot:`.

## Umsetzung
1. Je Branche entscheiden: Was ist der erste Schritt, was kostet er, was bekommt der Kunde?
2. In der YAML `text:` ausfüllen und die Zeile `platzhalter:` löschen:
   ```yaml
   angebot:
     titel: "So starten wir"
     text: "Im Erstgespräch … Danach bekommen Sie …"
   ```
   `text` versteht einfache Links im Markdown-Stil: `[Linktext](/kontakt.html)`.
3. `python3 _content/build_all.py` baut `/fuer/<branche>/index.html` neu.
4. Keine Kampagnendetails in die YAML (Repo ist öffentlich), siehe README, Abschnitt Branchenseiten.
5. Wenn eine Seite damit „trägt“: `index: true` setzen und auf der Startseite in der Branchenleiste
   (`chip-row` in `index.html`) verlinken. Erst dann wird sie indexiert.

## Fertig, wenn
- [ ] Alle vier YAMLs haben `angebot.text`, keine `platzhalter`-Zeile mehr
- [ ] Build gelaufen, Seiten lokal angesehen
