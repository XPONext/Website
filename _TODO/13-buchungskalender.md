# 13 · Buchungskalender auf der Kontaktseite

**Status:** offen · **Art:** Technik + Datenschutz · **Schließt:** `Kalender` in `kontakt.html`

## Ziel
Besucher buchen das 30-minütige Erstgespräch direkt selbst (Video oder Telefon), ohne Mail-Pingpong.

## Umsetzung
1. Anbieter wählen. Kriterien: Serverstandort EU, Auftragsverarbeitungsvertrag (AVV) möglich, Sync mit
   unseren Kalendern. Kandidaten: Cal.com (EU-Region beim Anlegen prüfen), Microsoft Bookings, Calendly
   (US-Anbieter, nur mit AVV und EU-Standardvertragsklauseln).
2. Termintyp anlegen: 30 Minuten, Video oder Telefon, Puffer 15 Minuten, max. Vorlauf z. B. 4 Wochen.
   Abfragen: Name, E-Mail, Firma, Thema. Nicht mehr.
3. **Einbau, datenschutzfreundlich:** Kein Skript beim Seitenaufruf laden. Zwei Möglichkeiten:
   - **Einfach (empfohlen):** Button, der die Buchungsseite in neuem Tab öffnet. Kein Einwilligungsthema.
     ```html
     <a class="btn btn--primary" href="https://…/erstgespraech" target="_blank" rel="noopener">Termin im Kalender wählen</a>
     ```
   - **Eingebettet:** Kalender erst nach Klick laden (Zwei-Klick-Lösung) mit Hinweis
     „Beim Laden werden Daten an [Anbieter] übertragen“. Aufwendiger, bringt aber den Kalender direkt auf die Seite.
4. Platzhalter-Kasten ersetzen, die „Anrufen“- und Formular-Wege darunter stehen lassen.
5. `datenschutz.html` ergänzen: Anbieter, Zweck, Rechtsgrundlage, Speicherdauer, Drittland ja/nein.
6. Konversion messen: Klick auf den Button als Ereignis in GA4 (läuft nur nach Einwilligung,
   siehe `gtag_report_conversion` im Kopf der Seiten).

## Fertig, wenn
- [ ] Testbuchung geht durch, Einladung kommt bei beiden Gründern an
- [ ] Datenschutzerklärung ergänzt, AVV abgeschlossen
- [ ] Platzhalter weg, alternative Kontaktwege noch da
