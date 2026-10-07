"""
Gemeinsame Bausteine aller Seiten: Kopf (head), Kopfzeile, Fußzeile, Cookie-Banner.

Eine Quelle für alles, was auf jeder Seite gleich ist. Genutzt von
- _content/build_geo_pages.py   (Leistungs-, Blog-, Ortsseiten)
- _content/build_landingpages.py (Branchenseiten unter /fuer/)
- _content/sync_layout.py       (handgebaute Seiten wie index.html, Bereiche zwischen
                                 den Markierungen <!-- @layout:… --> werden ersetzt)

Navigation oder Fußzeile ändern: hier ändern, dann `python3 _content/build_all.py`.
"""
import json

SITE = "https://www.xponext.de"
PHONE_DISPLAY = "0163 6857434"
PHONE_TEL = "+491636857434"
EMAIL = "info@xponext.de"
FIRMA = "XPO Next GbR"

LOGO_SVG = (
    '<svg viewBox="0 0 120 120" aria-hidden="true" focusable="false">'
    '<rect width="120" height="120" rx="28" fill="#1B6B45"/>'
    '<line x1="32" y1="88" x2="32" y2="32" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    '<line x1="88" y1="32" x2="88" y2="88" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    '<line x1="32" y1="32" x2="88" y2="88" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    '<line x1="32" y1="88" x2="88" y2="32" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity="0.3"/>'
    '</svg>'
)

CARET = ('<svg class="caret" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5l3 3 3-3" '
         'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>')

# Gemeinsamer Teil im <head>: Icons, Schrift, Styles, Analytics (gtag.js lädt erst nach Einwilligung).
HEAD_COMMON = """<link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preload" href="/assets/fonts/inter-variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/site.css">
  <link rel="stylesheet" href="/css/cookie-banner.css">
  <script>
    /* Google-Tag (gtag.js) wird erst nach Einwilligung im Cookie-Banner geladen, siehe js/cookie-banner.js. */
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent', 'default', {
      'analytics_storage': 'denied', 'ad_storage': 'denied', 'ad_user_data': 'denied', 'ad_personalization': 'denied'
    });
    gtag('js', new Date());
    gtag('config', 'G-S0KYC5QEKH', { 'anonymize_ip': true });
    function gtag_report_conversion(url) {
      var callback = function () { if (typeof(url) != 'undefined') { window.location = url; } };
      gtag('event', 'conversion', { 'send_to': 'AW-18218623343/-EIFCNn-hbocEO_CqO9D', 'value': 1.0, 'currency': 'EUR', 'event_callback': callback });
      return false;
    }
  </script>
  <script src="/js/site.js" defer></script>"""


def _cur(active, key):
    return ' aria-current="page"' if active == key else ""


def header(active=""):
    """Kopfzeile. active: leistungen | projekte | ueber-uns | kontakt | '' """
    return f"""<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
  {COOKIE_BANNER}
  <header class="site-header" id="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="/" aria-label="XPONext, zur Startseite">{LOGO_SVG}<span>XPO<em>Next</em></span></a>
      <nav class="site-nav" id="site-nav" aria-label="Hauptnavigation">
        <ul>
          <li class="has-sub">
            <a href="/leistungen.html"{_cur(active, "leistungen")}>Leistungen {CARET}</a>
            <div class="sub">
              <div>
                <p class="sub__group-title">Gefunden werden</p>
                <a href="/leistungen/website-erstellung.html">Website<span>Gestaltet, schnell, gut auffindbar</span></a>
                <a href="/leistungen/seo.html">SEO<span>Bei Google weiter oben</span></a>
                <a href="/leistungen/geo.html">GEO<span>Genannt in ChatGPT und KI-Suche</span></a>
                <a href="/leistungen/google-ads.html">Google Ads<span>Sofort sichtbar, planbares Budget</span></a>
              </div>
              <div>
                <p class="sub__group-title">Zeit zurückgewinnen</p>
                <a href="/leistungen/ki-automatisierung.html">KI-Automatisierung<span>Protokolle, Mails, Angebote</span></a>
                <p class="sub__group-title">Kostenlos prüfen</p>
                <a href="/website-check.html">Website-Check<span>Tempo, SEO, Barrierefreiheit</span></a>
                <a href="/geo-check.html">GEO-Check<span>Bereit für KI-Suchmaschinen?</span></a>
              </div>
              <div class="sub__all"><a href="/leistungen.html">Alle Leistungen im Überblick</a></div>
            </div>
          </li>
          <li><a href="/projekte.html"{_cur(active, "projekte")}>Projekte</a></li>
          <li><a href="/ueber-uns.html"{_cur(active, "ueber-uns")}>Über uns</a></li>
          <li><a href="/kontakt.html"{_cur(active, "kontakt")}>Kontakt</a></li>
        </ul>
        <div class="site-nav__mobile">
          <a class="btn btn--secondary" href="tel:{PHONE_TEL}">Anrufen: {PHONE_DISPLAY}</a>
        </div>
      </nav>
      <div class="site-header__actions">
        <a class="btn btn--primary btn--sm" href="/kontakt.html">Erstgespräch buchen</a>
        <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Menü öffnen"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>"""


# Cookie-Banner: Markup direkt nach dem Skip-Link (früh in der Tab-Reihenfolge), Skript am Seitenende.
COOKIE_BANNER = """<div class="cookie-banner" id="cookieBanner" role="dialog" aria-live="polite" aria-label="Cookie-Einstellungen" aria-hidden="true">
    <div class="cookie-banner__card">
      <div class="cookie-banner__head">
        <div class="cookie-banner__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 109 9 3 3 0 01-3.5-3A3 3 0 0114 5.5 3 3 0 0112 3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="9" cy="10" r="1.1" fill="currentColor"/><circle cx="14" cy="15" r="1.1" fill="currentColor"/><circle cx="8.5" cy="15.5" r="1.1" fill="currentColor"/></svg></div>
        <div>
          <h2 class="cookie-banner__title">Cookies & Datenschutz</h2>
          <p class="cookie-banner__text">Wir nutzen technisch notwendige Cookies, damit die Website funktioniert. Mit Ihrer Zustimmung setzen wir zusätzlich Google Analytics und Microsoft Clarity ein, um die Nutzung anonymisiert zu analysieren. Details in unserer <a href="/datenschutz.html">Datenschutzerklärung</a>.</p>
        </div>
      </div>
      <div class="cookie-banner__options" id="cookieOptions" hidden>
        <label class="cookie-option">
          <div>
            <div class="cookie-option__title">Notwendig</div>
            <div class="cookie-option__desc">Speichert Ihre Cookie-Einstellungen im Browser. Kein Tracking.</div>
          </div>
          <span class="cookie-option__always">Immer aktiv</span>
        </label>
        <label class="cookie-option">
          <div>
            <div class="cookie-option__title">Statistik</div>
            <div class="cookie-option__desc">Anonyme Nutzungsanalyse via Google Analytics 4 und Microsoft Clarity.</div>
          </div>
          <input type="checkbox" id="consentStatistics" class="cookie-switch">
          <span class="cookie-switch__slider" aria-hidden="true"></span>
        </label>
      </div>
      <div class="cookie-banner__actions">
        <button class="cookie-btn cookie-btn--ghost" id="cookieEssentials" type="button">Nur notwendige</button>
        <button class="cookie-btn cookie-btn--ghost" id="cookieSettingsToggle" type="button">Einstellungen</button>
        <button class="cookie-btn cookie-btn--primary" id="cookieAcceptAll" type="button">Alle akzeptieren</button>
        <button class="cookie-btn cookie-btn--primary" id="cookieSaveCustom" type="button" hidden>Auswahl speichern</button>
      </div>
    </div>
  </div>"""
COOKIE_SCRIPT = '<script src="/js/cookie-banner.js"></script>'


def footer():
    return f"""<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="/" aria-label="XPONext, zur Startseite">{LOGO_SVG}<span>XPO<em>Next</em></span></a>
          <p>Websites, Sichtbarkeit in Google und KI-Suche und KI-Automatisierung für Büros. Aus Bonn, für Unternehmen in ganz Deutschland.</p>
          <address>
            {FIRMA}<br>Adrianstraße 88<br>53227 Bonn<br>
            <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </address>
        </div>
        <div class="footer-col">
          <h2>Leistungen</h2>
          <ul>
            <li><a href="/leistungen/website-erstellung.html">Website</a></li>
            <li><a href="/leistungen/seo.html">SEO</a></li>
            <li><a href="/leistungen/geo.html">GEO</a></li>
            <li><a href="/leistungen/google-ads.html">Google Ads</a></li>
            <li><a href="/leistungen/ki-automatisierung.html">KI-Automatisierung</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h2>XPONext</h2>
          <ul>
            <li><a href="/projekte.html">Projekte</a></li>
            <li><a href="/ueber-uns.html">Über uns</a></li>
            <li><a href="/kontakt.html">Kontakt</a></li>
            <li><a href="/fuer/architekturbueros/">Für Architekturbüros</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h2>Kostenlos prüfen</h2>
          <ul>
            <li><a href="/website-check.html">Website-Check</a></li>
            <li><a href="/geo-check.html">GEO-Check</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 {FIRMA}</p>
        <ul>
          <li><a href="/impressum.html">Impressum</a></li>
          <li><a href="/datenschutz.html">Datenschutz</a></li>
          <li><a href="/agb.html">AGB</a></li>
          <li><button data-action="cookie-settings" class="cookie-reopen" type="button">Cookie-Einstellungen</button></li>
        </ul>
      </div>
    </div>
  </footer>

  {COOKIE_SCRIPT}"""


def cta_band(title_html, text, note="Kostenlos und unverbindlich, 30 Minuten per Video oder Telefon."):
    return f"""<section class="cta-band" aria-labelledby="cta-titel">
    <div class="container cta-band__grid">
      <div>
        <h2 id="cta-titel">{title_html}</h2>
        <p>{text}</p>
        <div class="btn-row">
          <a class="btn btn--light" href="/kontakt.html">Erstgespräch buchen</a>
          <a class="btn btn--ghost-light" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        </div>
        <p class="cta-note">{note}</p>
      </div>
      <div class="cta-band__person">
        <img src="/assets/team/tim.webp" alt="Tim Bünger" width="64" height="64" loading="lazy">
        <div><strong>Tim Bünger</strong>Mitgründer, Ihr Ansprechpartner<br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      </div>
    </div>
  </section>"""


def head(title, description, canonical, robots="index, follow", schemas=(), og_type="website", extra=""):
    """Kompletter <head> für generierte Seiten."""
    schema_html = "\n  ".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas
    )
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/og-image.jpg">
  <meta property="og:locale" content="de_DE">
  <meta name="twitter:card" content="summary_large_image">
  {schema_html}
  {HEAD_COMMON}{extra}
</head>"""


def breadcrumb_html(crumbs):
    """crumbs: Liste aus (href oder None, Label). Letzter Eintrag = aktuelle Seite."""
    items = []
    for href, label in crumbs:
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li><span aria-current="page">{label}</span></li>')
    return f'<nav class="breadcrumb" aria-label="Brotkrumen"><ol>{"".join(items)}</ol></nav>'


def breadcrumb_schema(crumbs, current_url):
    items = []
    for i, (href, label) in enumerate(crumbs, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        item["item"] = SITE + href if href else current_url
        items.append(item)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


ORGANIZATION_REF = {"@type": "ProfessionalService", "@id": SITE + "/#organisation", "name": FIRMA, "url": SITE + "/"}
