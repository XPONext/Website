# 02 · Risikoumkehr

**Status:** offen · **Art:** Entscheidung + Einbau · **Schließt:** `Risikoumkehr` in `index.html`

## Ziel
Ein Satz mit einer klaren Bedingung, der dem Besucher das Risiko abnimmt, z. B. ein Versprechen zu
Ergebnis, Zeit oder Kündbarkeit. Er steht auf der Startseite unter dem Ablauf („Typischer Ablauf“).

## Wo
`index.html`, Kasten `data-ph="Risikoumkehr"` am Ende der Ablauf-Section (vor `<!-- Team -->`).

## Umsetzung
1. Entscheiden, was wir zusichern können, ohne dass es uns schadet. Muster:
   „Wenn …, dann …“, eine Bedingung, messbar, ohne Kleingedrucktes.
   Mit den AGB abgleichen (`agb.html`), damit Website und Vertrag dasselbe sagen.
2. Kasten ersetzen, Stil wie die übrigen Hinweise:
   ```html
   <p class="timeline__note" style="margin-top:1.2rem"><strong>Unser Versprechen:</strong> …</p>
   ```
3. Platzhalter-Kommentar löschen.

## Fertig, wenn
- [ ] Ein Satz, eine Bedingung, in Sie-Form
- [ ] Passt zu AGB und Vertrag (`vertrag_generator`-Skill)
