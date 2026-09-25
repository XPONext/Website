/**
 * XPONext GEO-Check Proxy — Cloudflare Worker
 *
 * Holt eine beliebige URL serverseitig ab (HTML, robots.txt, sitemap.xml) und
 * gibt sie mit CORS-Headern zurück, damit geo-check.html sie im Browser lesen
 * kann. Browser-JS kann fremde Domains wegen CORS nicht direkt abrufen — dieser
 * Worker übernimmt genau diesen Schritt zuverlässig, statt eines freien
 * öffentlichen CORS-Proxys (die erfahrungsgemäß häufig ausfallen).
 *
 * Deployment: siehe README.md, Abschnitt "GEO-Check Proxy".
 *
 * CORS bewusst offen (Access-Control-Allow-Origin: *) statt auf xponext.de
 * beschränkt — sonst schlägt jeder lokale Test (localhost, file://) fehl,
 * weil der Browser die Antwort verwirft. Der Worker reicht ohnehin nur
 * öffentliche Webseiten durch (kein Schreibzugriff, keine sensiblen Daten),
 * das Risiko einer offenen Origin ist hier gering.
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
};

export default {
  async fetch(request) {
    const headers = CORS_HEADERS;

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers });
    }
    if (request.method !== 'GET') {
      return new Response('Method not allowed', { status: 405, headers });
    }

    const reqUrl = new URL(request.url);
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
  },
};
