# 08 · Kundenstimmen

**Status:** offen · **Wartet auf:** 04 · **Schließt:** `Kundenstimme 1–3` in `projekte.html`

## Wo
`projekte.html`, Section „Was Kunden über die Zusammenarbeit sagen“, drei `ph`-Kästen in `<div class="cases">`.

## Umsetzung
1. Je Stimme: Zitat (2–3 Sätze, über die Zusammenarbeit, nicht nur das Ergebnis), Name, Funktion,
   Firma, Porträtfoto (quadratisch, 112 × 112 px als WebP unter `assets/kunden/`).
2. Markup, angelehnt an `.person` aus der Team-Section:
   ```html
   <figure class="case" style="padding:1.4rem">
     <blockquote>„…“</blockquote>
     <figcaption class="person" style="margin-top:1rem">
       <img src="/assets/kunden/name.webp" alt="" width="56" height="56" loading="lazy">
       <div><strong>Vorname Nachname</strong><span>Funktion, Firma</span></div>
     </figcaption>
   </figure>
   ```
   `alt=""` am Foto, weil der Name direkt daneben steht.
3. Am liebsten als kurzes Video (siehe Ticket 11 für Einbau, selbst gehostet).
4. Fotos in `assets/BILDER.md` eintragen, Platzhalter-Kommentar löschen.

## Fertig, wenn
- [ ] Drei Stimmen mit Name, Funktion, Firma, Foto
- [ ] Keine Stimme doppelt mit dem Zitat einer Fallstudie
