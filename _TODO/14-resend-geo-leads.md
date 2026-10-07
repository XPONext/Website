# 14 · Resend für die GEO-Check-Leads

**Status:** offen · **Art:** Technik · **Platzhalter:** keiner (README-TODO)

## Problem
Wer im GEO-Check (`/geo-check.html`) seine E-Mail eingibt, landet nur im Cloudflare-KV-Speicher.
Es kommt **keine Sofort-Mail** an info@xponext.de. Leads fallen so leicht durch.

## Umsetzung (Details im README, Abschnitt „GEO-Check Leads“)
1. Konto auf resend.com anlegen (kostenlos).
2. Domain `xponext.de` verifizieren: Die DNS-Einträge (SPF/DKIM), die Resend anzeigt, beim Domain-Anbieter
   eintragen. Bestehende MX- und SPF-Einträge für das Postfach nicht überschreiben, sondern ergänzen.
3. API-Key erstellen (nur „Sending access“).
4. Cloudflare-Dashboard → Worker → Settings → Variables and Secrets → Add →
   Name `RESEND_API_KEY`, Typ **Secret**, Wert = API-Key → Deploy.
5. Absender `geo-check@xponext.de` in `sendNotification()` (`cloudflare-worker/geo-proxy.js`) muss zur
   verifizierten Domain passen. Code nur ändern, wenn nötig, dann im Dashboard neu einfügen und deployen.
6. Test: GEO-Check mit eigener Adresse durchspielen, Mail muss ankommen.
7. `datenschutz.html` Abschnitt 5.3 prüfen: Resend als Empfänger/Auftragsverarbeiter nennen, AVV abschließen.
8. TODO-Hinweis im README entfernen.

## Fertig, wenn
- [ ] Test-Lead erzeugt eine Mail an info@xponext.de
- [ ] Datenschutzerklärung nennt Resend
- [ ] README-TODO entfernt
