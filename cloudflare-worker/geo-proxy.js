/**
 * XPONext GEO-Check Proxy & Lead-Endpoint — Cloudflare Worker
 *
 * Zwei Aufgaben:
 *
 * 1. GET /?url=<ziel>  Holt eine beliebige URL serverseitig ab (HTML,
 *    robots.txt, sitemap.xml) und gibt sie mit CORS-Headern zurück, damit
 *    geo-check.html sie im Browser lesen kann. Browser-JS kann fremde
 *    Domains wegen CORS nicht direkt abrufen — dieser Worker übernimmt
 *    genau diesen Schritt zuverlässig, statt eines freien öffentlichen
 *    CORS-Proxys (die erfahrungsgemäß häufig ausfallen).
 *
 * 2. POST /lead  Nimmt die E-Mail-Adresse entgegen, die jemand einträgt, um
 *    den vollständigen GEO-Check-Bericht freizuschalten. Validiert Format +
 *    MX-Record der E-Mail-Domain, legt den Lead in Cloudflare KV ab und
 *    verschickt optional eine Benachrichtigung über Resend.
 *
 * Deployment & Setup (KV-Binding, Resend-Secret): siehe README.md,
 * Abschnitt "GEO-Check Proxy" und "GEO-Check Leads".
 *
 * CORS bewusst offen (Access-Control-Allow-Origin: *) statt auf xponext.de
 * beschränkt — sonst schlägt jeder lokale Test (localhost, file://) fehl,
 * weil der Browser die Antwort verwirft. Der Worker reicht ohnehin nur
 * öffentliche Webseiten durch bzw. nimmt ein einfaches Lead-Formular an
 * (kein Schreibzugriff auf sensible Systeme), das Risiko einer offenen
 * Origin ist hier gering.
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

function json(data, status, headers) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: Object.assign({ 'Content-Type': 'application/json; charset=utf-8' }, headers),
  });
}

export default {
  async fetch(request, env) {
    const headers = CORS_HEADERS;

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers });
    }

    const reqUrl = new URL(request.url);

    if (reqUrl.pathname === '/lead' && request.method === 'POST') {
      return handleLead(request, env, headers);
    }

    if (request.method !== 'GET') {
      return new Response('Method not allowed', { status: 405, headers });
    }

    return handleProxy(reqUrl, headers);
  },
};

/* ── 1. URL-Proxy ── */

async function handleProxy(reqUrl, headers) {
  const target = reqUrl.searchParams.get('url');
  if (!target) {
    return new Response('Missing "url" parameter', { status: 400, headers });
  }

  let targetUrl;
  try {
    targetUrl = new URL(target);
  } catch (e) {
    return new Response('Invalid URL', { status: 400, headers });
  }
  if (targetUrl.protocol !== 'http:' && targetUrl.protocol !== 'https:') {
    return new Response('Only http/https URLs are allowed', { status: 400, headers });
  }

  try {
    const upstream = await fetch(targetUrl.toString(), {
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; XPONextGeoCheck/1.0; +https://www.xponext.de/geo-check.html)',
      },
      redirect: 'follow',
    });
    const body = await upstream.text();
    const contentType = upstream.headers.get('content-type') || 'text/plain; charset=utf-8';
    return new Response(body, {
      status: upstream.status,
      headers: Object.assign({}, headers, { 'Content-Type': contentType }),
    });
  } catch (e) {
    return new Response('Upstream fetch failed: ' + (e && e.message ? e.message : 'unknown error'), { status: 502, headers });
  }
}

/* ── 2. Lead-Endpoint ── */

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function handleLead(request, env, headers) {
  let body;
  try {
    body = await request.json();
  } catch (e) {
    return json({ error: 'invalid_json' }, 400, headers);
  }

  const email = String(body.email || '').trim();
  const domain = String(body.domain || '').trim();
  const score = Number.isFinite(body.score) ? body.score : null;
  const honeypot = String(body.website || '').trim();

  // Honeypot: unsichtbares Feld für Menschen, das Bots trotzdem oft ausfüllen.
  // Anfrage so tun als ob erfolgreich, aber nichts speichern/verschicken.
  if (honeypot) {
    return json({ ok: true }, 200, headers);
  }

  if (!EMAIL_REGEX.test(email) || email.length > 254) {
    return json({ error: 'invalid_email' }, 400, headers);
  }

  const emailDomain = email.split('@')[1];
  const hasMx = await checkMx(emailDomain);
  if (!hasMx) {
    return json({ error: 'invalid_email' }, 400, headers);
  }

  const record = {
    email: email,
    domain: domain || null,
    score: score,
    createdAt: new Date().toISOString(),
  };

  if (env.LEADS) {
    const id = new Date().toISOString() + '-' + crypto.randomUUID();
    await env.LEADS.put('lead:' + id, JSON.stringify(record));
  }

  if (env.RESEND_API_KEY) {
    await sendNotification(env, record).catch(function () {
      // Benachrichtigung ist "nice to have" — ein Mail-Fehler soll die
      // Freischaltung für den Nutzer nicht blockieren.
    });
  }

  return json({ ok: true }, 200, headers);
}

async function checkMx(domain) {
  try {
    const res = await fetch(
      'https://cloudflare-dns.com/dns-query?name=' + encodeURIComponent(domain) + '&type=MX',
      { headers: { Accept: 'application/dns-json' } }
    );
    if (!res.ok) return true; // fail open — DNS-Check selbst fehlgeschlagen, Nutzer nicht blockieren
    const data = await res.json();
    return Array.isArray(data.Answer) && data.Answer.length > 0;
  } catch (e) {
    return true; // fail open
  }
}

async function sendNotification(env, record) {
  const subject = 'Neue GEO-Check-Anfrage: ' + (record.domain || 'unbekannte Domain');
  const text = [
    'Domain: ' + (record.domain || '-'),
    'E-Mail: ' + record.email,
    'GEO-Score: ' + (record.score !== null ? record.score : '-'),
    'Zeitpunkt: ' + record.createdAt,
  ].join('\n');

  await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer ' + env.RESEND_API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: 'GEO-Check <geo-check@xponext.de>',
      to: ['info@xponext.de'],
      subject: subject,
      text: text,
    }),
  });
}
