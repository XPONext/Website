/*
 * Interaktives 3D-Logo im Hero der Startseite, nach dem Vorbild von ai.qestit.com.
 *
 * Quelle dieser Datei. Ausgeliefert wird das Bündel /js/hero-logo-3d.js,
 * gebaut mit `npm run build` in diesem Ordner (siehe README.md hier).
 *
 * Konfiguration im HTML, damit neue Formen keinen neuen Build brauchen:
 *   <div class="hero-logo3d" data-hero-logo3d
 *        data-shapes="logo, lupe, sprechblase, blitz:1.05"  → /assets/hero-shapes/<name>.svg,
 *                                                           erste = Hauptlogo, ":1.05" = eigene Größe
 *        data-colors="#1B6B45 #0F3A26"                     → Grundfarbe → Verlaufsfarbe
 *        data-light-colors="#1B6B45 #DCEDE3">              → Farben der beiden Punktlichter
 *     <img class="hero-logo3d__static" …>   statisches Logo, bleibt bei
 *                                          reduzierter Bewegung und ohne WebGL
 *     <canvas class="hero-logo3d__canvas"></canvas>
 *   </div>
 *
 * In den SVGs: Weiß gefüllte Pfade werden zur erhabenen Einlage auf der Vorderseite
 * (fill-opacity/opacity < 1 → halbtransparent und flacher), alle anderen zum Körper
 * mit Farbverlauf. So entsteht das XPONext-Zeichen: grüne Kachel, weißes N, X-Strich.
 *
 * Ablauf: IDLE → SENTIENT (Geste) → OUT (Spin zur neuen Form) → SHIFTED → OUT zur nächsten
 * Form … jeder LOGO_EVERY-te Wechsel ist BACK (Spin zurück zum Logo) → IDLE. Hover lässt die Form unter dem Cursor
 * zersplittern (wie bei Qestit), wechselt sie aber nicht. Klick/Tap treibt den Ablauf weiter.
 */
import {
  WebGLRenderer, Scene, PerspectiveCamera, Group, Mesh, Color, Vector2, Vector3, Raycaster,
  MeshPhysicalMaterial, ExtrudeGeometry, AmbientLight, DirectionalLight, PointLight, PMREMGenerator,
} from 'three';
import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { TessellateModifier } from 'three/examples/jsm/modifiers/TessellateModifier.js';

/* ── Stellschrauben ──────────────────────────────────────────────────────
 * Zeiten in Sekunden. Längen in Objektgröße: jede Form ist auf 1 Einheit
 * normiert (0.075 = 7,5 % der Formbreite, entspricht 9 bei einem 120er-SVG).
 * Lerp-Faktoren gelten pro Frame bei 60 fps und werden auf andere
 * Bildraten umgerechnet. */
const CONFIG = {
  // Ruhe (IDLE)
  IDLE_MIN: 3.0,               // Wartezeit bis zur nächsten Geste, zufällig zwischen MIN und MAX
  IDLE_MAX: 6.0,
  FLOAT_AMP: 0.035,            // Schweben auf und ab
  SWAY_X: 0.14,                // Pendeln um X (rad)
  SWAY_Y: 0.42,                // Pendeln um Y (rad)

  // Geste (SENTIENT)
  GESTURE_MIN: 1.1,
  GESTURE_MAX: 1.6,
  GESTURE_BASE_DAMP: 0.25,     // Grundbewegung während der Geste auf 25 %
  LERP_BASE_DAMP: 0.08,

  // Formwechsel (OUT / BACK)
  SWAP_DUR: 0.72,
  SWAP_AT: 0.45,               // Anteil der Zeit, bei dem die Form getauscht wird
  SWAP_MIN_SCALE: 0.04,
  SPIN_DAMP: 4.5,              // Feder des Spins: höher = schneller ruhig
  SPIN_FREQ: 7.0,              //                  höher = mehr Überschwingen
  POP_DAMP: 6.0,               // Feder beim Aufpoppen
  POP_FREQ: 10.0,

  // Neue Form (SHIFTED)
  SHIFTED_MIN: 2.6,
  SHIFTED_MAX: 3.8,
  SHIFTED_WOBBLE: 0.12,        // Wippen um Y (rad)
  SHIFTED_PULSE: 0.025,        // Pulsieren ±2,5 %
  FIXED_FIRST: 2,              // so viele Wechsel laufen in der Reihenfolge aus data-shapes, danach zufällig
  LOGO_EVERY: 3,               // jeder dritte Wechsel führt zurück zum Logo (2 = nach jeder Form)

  // Easter Egg: so viele Klicks in so kurzer Zeit lassen grüne Linien über den Bildschirm laufen
  EGG_CLICKS: 5,
  EGG_WINDOW: 2.0,             // Sekunden
  EGG_LINES: 16,               // Anzahl der Linien
  EGG_COLOR: '#1B6B45',
  EGG_DRAW: 1.4,               // Sekunden, bis eine Linie ganz gezeichnet ist
  EGG_STAGGER: 0.05,           // Versatz zwischen den Linien
  EGG_FADE: 0.9,               // Ausblenden am Ende
  EGG_EXTRA_CLICKS: 3,         // so viele weitere Klicks schießen danach je eine Extra-Salve …
  EGG_EXTRA_LINES: 6,          // … mit so vielen Linien

  // Hover: Zersplittern unter dem Cursor. Jedes Dreieck wird entlang seiner eigenen
  // Flächennormalen verschoben, dadurch reißen die Splitter an den Kanten auseinander.
  HOVER_AMP: 0.09,             // wie weit die Splitter herausspringen
  HOVER_FLOW: 0.025,           // wie stark sie unter dem Cursor zittern/fließen
  HOVER_RAD: 0.15,             // Radius = (Breite + Höhe) * HOVER_RAD
  FLOW_K1: 9.0,                // Wellen pro Einheit in x
  FLOW_K2: 7.0,                // Wellen pro Einheit in y
  LERP_HIT: 0.35,              // Trefferpunkt zieht nach
  LERP_AMP: 0.15,
  LERP_FLOW: 0.10,

  // Farbe und Licht
  LERP_GRAD: 0.04,             // Übergang Grundfarbe ↔ Verlauf
  LIGHT_CYCLE: 16,             // Farbzyklus der Punktlichter
  LIGHT_INTENSITY: 1.8,        // höher = farbigere, hellere Lichtflecken
  LIGHT_ORBIT: 1.4,            // Radius der Kreisbahnen
  LIGHT_FOLLOW_X: 120,         // Punktlichter folgen der Maus um max. ±120 px …
  LIGHT_FOLLOW_Y: 80,          // … und ±80 px
  LERP_MOUSE: 0.06,

  // Geometrie
  TESSELLATE_EDGE: 0.22,       // max. Kantenlänge der Splitter: größer = wenige lange Scherben, kleiner = feiner Bruch (0 = nicht unterteilen)
  AUTO_SCALE: 0.25,            // schmale Formen etwas größer, damit alle gleich groß wirken (0 = aus)
};

const SHAPE_DIR = '/assets/hero-shapes/';
const SVG_NS = 'http://www.w3.org/2000/svg';

const EXTRUDE = { depth: 8, bevelEnabled: true, bevelThickness: 2, bevelSize: 1.4, bevelSegments: 2, curveSegments: 16 };
// Einlagen (weiße Pfade): flacher, schmalere Fase, damit dünne Striche dünn bleiben
const INLAY = { depth: 1.2, bevelEnabled: true, bevelThickness: 0.6, bevelSize: 0.5, bevelSegments: 2, curveSegments: 16 };
const INLAY_FAINT_DEPTH = 0.2;

const root = document.querySelector('[data-hero-logo3d]');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (root && !reducedMotion.matches && hasWebGL()) {
  start(root).catch((err) => console.warn('[hero-logo-3d]', err));
}

function hasWebGL() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
  } catch (e) {
    return false;
  }
}

/* ── Formen laden ──────────────────────────────────────────────────────── */

/* SVG → Körper + Einlagen, zentriert, auf 1 Einheit normiert und fein unterteilt */
async function loadShape(name) {
  const res = await fetch(SHAPE_DIR + name + '.svg');
  if (!res.ok) throw new Error('Form fehlt: ' + name);
  const data = new SVGLoader().parse(await res.text());

  const bodyShapes = [];
  const inlays = [];
  for (const path of data.paths) {
    const shapes = path.toShapes();
    if (path.color.getHex() === 0xffffff) {
      const st = path.userData.style;
      inlays.push({ shapes, opacity: (st.fillOpacity ?? 1) * (st.opacity ?? 1) });
    } else {
      bodyShapes.push(...shapes);
    }
  }
  if (!bodyShapes.length) throw new Error('Form ohne farbigen Körper: ' + name);

  let body = new ExtrudeGeometry(bodyShapes, EXTRUDE);
  body.computeBoundingBox();
  const b = body.boundingBox;
  const cx = (b.min.x + b.max.x) / 2;
  const cy = (b.min.y + b.max.y) / 2;
  const cz = (b.min.z + b.max.z) / 2;
  const s = 1 / Math.max(b.max.x - b.min.x, b.max.y - b.min.y);
  // SVG zählt y nach unten. (s, -s, -s) dreht um 180° statt zu spiegeln,
  // so bleiben die Dreiecke richtig herum (keine Rückseiten sichtbar).
  body.translate(-cx, -cy, -cz).scale(s, -s, -s);
  body = tessellate(body);
  const bb = body.boundingBox;
  const width = bb.max.x - bb.min.x;
  const height = bb.max.y - bb.min.y;

  const parts = inlays.map(({ shapes, opacity }) => {
    const geo = new ExtrudeGeometry(shapes, opacity < 1 ? { ...INLAY, depth: INLAY_FAINT_DEPTH } : INLAY);
    geo.translate(-cx, -cy, 0).scale(s, -s, -s);
    geo.computeBoundingBox();
    // Auf die Vorderseite setzen, leicht eingesenkt, damit keine Fuge entsteht
    geo.translate(0, 0, bb.max.z - geo.boundingBox.min.z - 0.004);
    return { geo: tessellate(geo), opacity };
  });

  return {
    body,
    parts,
    rad: (width + height) * CONFIG.HOVER_RAD,
    gradSize: (width + height) / 2,
    autoScale: Math.min((1 / (width * height)) ** (CONFIG.AUTO_SCALE / 2), 1.25),
  };
}

// Große, flache Dreiecke unterteilen, damit sich die Fläche unter der Maus wölben kann
function tessellate(geo) {
  if (!CONFIG.TESSELLATE_EDGE) {
    geo.computeBoundingBox();
    geo.computeBoundingSphere();
    return geo;
  }
  const iterations = Math.ceil(Math.log2(1 / CONFIG.TESSELLATE_EDGE)) * 2 + 2;
  const out = new TessellateModifier(CONFIG.TESSELLATE_EDGE, iterations).modify(geo);
  geo.dispose();
  out.computeBoundingBox();
  out.computeBoundingSphere();
  return out;
}

/* ── Material ──────────────────────────────────────────────────────────── */

/* Gemeinsame Uniforms für alle Teile: Körper und Einlagen verformen sich gleich */
function makeUniforms(colA, colB) {
  return {
    uHit: { value: new Vector3(0, 0, 1) },
    uAmp: { value: 0 },
    uRad: { value: 0.3 },
    uTime: { value: 0 },
    uFlow: { value: 0 },
    uGrad: { value: 0 },
    uGradSize: { value: 1 },
    uColA: { value: new Color(colA) },
    uColB: { value: new Color(colB) },
  };
}

const VERTEX_HEAD = /* glsl */`
uniform vec3 uHit;
uniform float uAmp, uRad, uTime, uFlow, uGradSize;
varying float vGradPos;
vec3 xpoDisp;
`;

// Zersplittern: Gauß-Falloff um den Trefferpunkt plus Wellen (Fließen), nur im Hover-Bereich.
// Verschoben wird entlang der Normalen jedes Dreiecks. Die Extrusion hat flache Normalen je
// Fläche, deshalb bewegen sich Nachbarflächen in verschiedene Richtungen und die Form bricht
// an den Kanten auf. flatShading im Material zeigt die gekippten Splitter als Facetten.
const VERTEX_DEFORM = /* glsl */`
#include <beginnormal_vertex>
{
  vec3 rel = position - uHit;
  float mask = exp(-dot(rel, rel) / (uRad * uRad));
  float flow = sin(position.x * float(${CONFIG.FLOW_K1}) + uTime * 1.15)
             * cos(position.y * float(${CONFIG.FLOW_K2}) + uTime * 0.75) * uFlow;
  xpoDisp = normalize(objectNormal) * (uAmp + flow) * mask;
  vGradPos = clamp(0.5 + (position.x - position.y) / (uGradSize * 1.4), 0.0, 1.0);
}
`;

function makeMaterial(uniforms, { gradient, opacity = 1 }) {
  const mat = new MeshPhysicalMaterial({
    color: 0xffffff,
    metalness: 0,
    roughness: 0.4,
    specularIntensity: 0.35,
    clearcoat: 1,
    clearcoatRoughness: gradient ? 0.08 : 0.1,
    envMapIntensity: 0.45,
    transparent: opacity < 1,
    opacity,
    flatShading: true,
  });
  mat.onBeforeCompile = (shader) => {
    Object.assign(shader.uniforms, uniforms);
    shader.vertexShader = VERTEX_HEAD + shader.vertexShader
      .replace('#include <beginnormal_vertex>', VERTEX_DEFORM)
      .replace('#include <begin_vertex>', '#include <begin_vertex>\n  transformed += xpoDisp;');
    if (gradient) {
      // uGrad 0 = Grundfarbe, 1 = Verlauf Grundfarbe → Verlaufsfarbe
      shader.fragmentShader = 'uniform vec3 uColA;\nuniform vec3 uColB;\nuniform float uGrad;\nvarying float vGradPos;\n' +
        shader.fragmentShader.replace(
          '#include <color_fragment>',
          '#include <color_fragment>\n  diffuseColor.rgb = mix(uColA, mix(uColA, uColB, vGradPos), uGrad);'
        );
    }
  };
  // Körper und Einlage haben verschiedene Shader, trotz gleicher onBeforeCompile-Quelle
  mat.customProgramCacheKey = () => (gradient ? 'xpo-body' : 'xpo-inlay');
  return mat;
}

/* ── Gesten (SENTIENT) ─────────────────────────────────────────────────────
 * fn(p, o): p läuft 0..1, o ist die Pose-Abweichung, die die Funktion setzt. */
const bump = (p, c, w) => Math.exp(-(((p - c) / w) ** 2));
const smooth = (t) => t * t * (3 - 2 * t);

const GESTURES = {
  herzschlag(p, o) {
    o.s = 1 + 0.10 * bump(p, 0.18, 0.07) + 0.14 * bump(p, 0.42, 0.08);
  },
  einatmen(p, o) {
    if (p < 0.7) {
      o.s = 1 + 0.16 * smooth(p / 0.7);
    } else {
      const q = (p - 0.7) / 0.3;
      o.s = 1 + 0.16 * Math.exp(-5 * q) * Math.cos(9 * q);
    }
  },
  huepfen(p, o) {
    const h = Math.abs(Math.sin(2 * Math.PI * p));
    o.py = 0.11 * h * (p < 0.5 ? 1 : 0.7);
    o.sy = 1 + 0.07 * h;
    o.sx = o.sz = 1 - 0.035 * h;
  },
  kopfschuetteln(p, o) {
    o.ry = 0.55 * Math.sin(p * Math.PI * 6) * (1 - p) ** 1.5;
  },
  erschrecken(p, o) {
    const d = (1 - p) ** 2;
    o.s = 1 - 0.12 * bump(p, 0.06, 0.07);
    o.px = 0.025 * Math.sin(p * 90) * d;
    o.rz = 0.09 * Math.sin(p * 75) * d;
  },
};
// Erschrecken ist für Klicks reserviert
const RANDOM_GESTURES = ['herzschlag', 'einatmen', 'huepfen', 'kopfschuetteln'];

/* ── Hilfen ────────────────────────────────────────────────────────────── */
const lerp = (a, b, t) => a + (b - a) * t;
const rand = (a, b) => a + Math.random() * (b - a);
const pick = (list) => list[Math.floor(Math.random() * list.length)];
const clamp = (v, a, b) => Math.min(Math.max(v, a), b);
// Lerp-Faktor pro 60-fps-Frame → passend zur tatsächlichen Framezeit
const k = (factor, dt) => 1 - Math.pow(1 - factor, dt * 60);
const spring = (p, damp, freq) => 1 - Math.exp(-damp * p) * Math.cos(freq * p);

/* ── Start ─────────────────────────────────────────────────────────────── */
async function start(root) {
  const canvas = root.querySelector('.hero-logo3d__canvas');
  const entries = (root.dataset.shapes || 'logo').split(',').map((s) => s.trim()).filter(Boolean)
    .map((s) => { const [name, scale] = s.split(':'); return { name: name.trim(), scale: Number(scale) || 0 }; });
  const colors = (root.dataset.colors || '').split(/\s+/).filter(Boolean);
  const lightColors = (root.dataset.lightColors || '').split(/\s+/).filter(Boolean);
  const lightA = new Color(lightColors[0] || '#1B6B45');
  const lightB = new Color(lightColors[1] || '#DCEDE3');

  // Alle Geometrien vorab bauen; eine fehlerhafte Form wird übersprungen
  const loaded = (await Promise.all(entries.map((e) => loadShape(e.name)
    .then((shape) => ({ ...shape, targetScale: e.scale || shape.autoScale }))
    .catch((err) => { console.warn('[hero-logo-3d]', err.message); return null; })
  ))).filter(Boolean);
  if (!loaded.length) return;

  const uniforms = makeUniforms(colors[0] || '#1B6B45', colors[1] || '#0F3A26');
  const bodyMat = makeMaterial(uniforms, { gradient: true });
  const inlayMats = new Map();
  const inlayMat = (o) => inlayMats.get(o) || inlayMats.set(o, makeMaterial(uniforms, { gradient: false, opacity: o })).get(o);
  const models = loaded.map(({ body, parts }) => {
    const g = new Group();
    g.add(new Mesh(body, bodyMat));
    for (const { geo, opacity } of parts) g.add(new Mesh(geo, inlayMat(opacity)));
    return g;
  });

  // Schwache Geräte: weniger Pixel, keine Kantenglättung
  const weak = (navigator.hardwareConcurrency || 8) < 4 || (navigator.deviceMemory || 8) < 4;
  const renderer = new WebGLRenderer({ canvas, alpha: true, antialias: !weak, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, weak ? 1.5 : 2));
  renderer.setClearColor(0x000000, 0);

  const scene = new Scene();
  const pmrem = new PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  pmrem.dispose();

  scene.add(new AmbientLight(0xffffff, 0.5));
  const key = new DirectionalLight(0xffffff, 2.0);
  key.position.set(3, 4, 1.2);
  const rim = new DirectionalLight(0xdcede3, 1.2);
  rim.position.set(-3, 1.5, -2);
  const fill = new DirectionalLight(0xffffff, 0.45);
  fill.position.set(0, -2, 3);
  scene.add(key, rim, fill);

  // Zwei farbige Punktlichter, die um das Objekt driften
  const lights = [0, 1].map(() => new PointLight(0xffffff, CONFIG.LIGHT_INTENSITY, 0, 2));
  scene.add(...lights);

  const camera = new PerspectiveCamera(30, 1, 0.1, 20);
  camera.position.set(0, 0, 2.55);

  // pivot: Schweben/Pendeln · holder: Geste, Spin, Größe
  const pivot = new Group();
  const holder = new Group();
  pivot.add(holder);
  scene.add(pivot);

  let index = 0;
  function showModel(i) {
    holder.remove(models[index]);
    index = i;
    holder.add(models[index]);
    // Shader an die neue Form anpassen
    uniforms.uRad.value = loaded[index].rad;
    uniforms.uGradSize.value = loaded[index].gradSize;
  }
  showModel(0);

  let worldPerPx = 0.013;
  function resize() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    worldPerPx = (2 * camera.position.z * Math.tan((camera.fov * Math.PI) / 360)) / h;
  }
  resize();
  new ResizeObserver(resize).observe(canvas);

  /* ── Zustände ─────────────────────────────────────────────────────────── */
  let T = 0;                 // eigene Uhr in s, läuft nur, solange gerendert wird
  let state = 'IDLE';
  let stateStart = 0;
  let stateDur = rand(CONFIG.IDLE_MIN, CONFIG.IDLE_MAX);
  let gesture = null;
  let spin = { axis: 'y', dir: 1 };
  let swapTo = 0;
  let swapped = false;
  let fromScale = loaded[0].targetScale;
  let switches = 0;
  let lastShape = -1;
  let sinceLogo = 0;         // Wechsel seit dem letzten Logo

  function enter(next, dur = 0) {
    state = next;
    stateStart = T;
    stateDur = dur;
  }

  function startGesture(name) {
    gesture = GESTURES[name];
    enter('SENTIENT', rand(CONFIG.GESTURE_MIN, CONFIG.GESTURE_MAX));
  }

  // Nächste Form: erst feste Reihenfolge, dann zufällig, nie zweimal dieselbe hintereinander
  function pickNext() {
    if (switches < CONFIG.FIXED_FIRST && switches + 1 < models.length && switches + 1 !== index) return switches + 1;
    const pool = [];
    for (let i = 1; i < models.length; i++) if (i !== index && i !== lastShape) pool.push(i);
    if (!pool.length) for (let i = 1; i < models.length; i++) if (i !== index) pool.push(i);
    return pool.length ? pick(pool) : 0;
  }

  function startSwap(to) {
    swapTo = to;
    swapped = false;
    fromScale = holder.scale.x || loaded[index].targetScale;
    spin = { axis: pick(['x', 'y', 'z']), dir: Math.random() < 0.5 ? -1 : 1 };
    if (to !== 0) { switches++; lastShape = to; }
    enter(to === 0 ? 'BACK' : 'OUT', CONFIG.SWAP_DUR);
  }

  // Nächster Wechsel: zu einer anderen Form, jeder LOGO_EVERY-te zurück zum Logo
  function advance() {
    sinceLogo = index === 0 ? 1 : sinceLogo + 1;
    if (models.length > 1) startSwap(sinceLogo >= CONFIG.LOGO_EVERY ? 0 : pickNext());
    else enter('IDLE', rand(CONFIG.IDLE_MIN, CONFIG.IDLE_MAX));
  }

  /* ── Maus, Klick, Tap ─────────────────────────────────────────────────── */
  const raycaster = new Raycaster();
  const pointer = new Vector2();
  let mouseOnCanvas = false;
  const mouse = { x: 0, y: 0 };      // Abstand zur Canvas-Mitte in px, für die Punktlichter
  const mouseSmooth = { x: 0, y: 0 };

  function toNdc(e) {
    const r = canvas.getBoundingClientRect();
    pointer.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  }
  function hitTest() {
    raycaster.setFromCamera(pointer, camera);
    return raycaster.intersectObject(holder, true)[0] || null;
  }

  // Zersplittern nur mit der Maus, nicht bei Touch
  canvas.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    toNdc(e);
    mouseOnCanvas = true;
  });
  canvas.addEventListener('pointerleave', () => { mouseOnCanvas = false; });
  window.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    const r = canvas.getBoundingClientRect();
    mouse.x = clamp(e.clientX - (r.left + r.width / 2), -CONFIG.LIGHT_FOLLOW_X, CONFIG.LIGHT_FOLLOW_X);
    mouse.y = clamp(e.clientY - (r.top + r.height / 2), -CONFIG.LIGHT_FOLLOW_Y, CONFIG.LIGHT_FOLLOW_Y);
  }, { passive: true });

  // Klick und Tap (click kommt bei beiden)
  let eggClicks = [];
  canvas.addEventListener('click', (e) => {
    // Easter Egg: EGG_CLICKS Klicks aufs Icon-Feld innerhalb von EGG_WINDOW Sekunden.
    // Gezählt wird jeder Klick aufs Feld, nicht nur Treffer: Während des Formwechsels
    // ist die Form kurz winzig und würde sonst nicht getroffen.
    // Läuft der Effekt schon, schießen die nächsten Klicks Extra-Linien hinterher.
    const t = performance.now();
    const r = canvas.getBoundingClientRect();
    const cx = r.left + r.width / 2;
    const cy = r.top + r.height / 2;
    if (egg && egg.extra > 0) {
      egg.extra--;
      greenLines(cx, cy, CONFIG.EGG_EXTRA_LINES);
    } else {
      eggClicks = eggClicks.filter((c) => t - c < CONFIG.EGG_WINDOW * 1000).concat(t);
      if (eggClicks.length >= CONFIG.EGG_CLICKS && !egg) {
        eggClicks = [];
        greenLines(cx, cy, CONFIG.EGG_LINES);
      }
    }
    toNdc(e);
    if (!hitTest()) return;
    if (state === 'IDLE') startGesture('erschrecken');
    else if (state === 'SENTIENT' || state === 'SHIFTED') advance();
    // OUT / BACK: ignorieren, immer nur ein Wechsel gleichzeitig
  });

  /* ── Render-Loop, nur solange sichtbar ───────────────────────────────── */
  const pose = { px: 0, py: 0, rx: 0, ry: 0, rz: 0, s: 1, sx: 1, sy: 1, sz: 1 };
  const hitLocal = new Vector3();
  let baseFactor = 1;
  let running = false;
  let raf = 0;
  let last = 0;
  let first = true;

  function frame(now) {
    raf = requestAnimationFrame(frame);
    const dt = Math.min((now - last) / 1000, 0.1);
    last = now;
    T += dt;
    uniforms.uTime.value = T;

    Object.assign(pose, { px: 0, py: 0, rx: 0, ry: 0, rz: 0, s: 1, sx: 1, sy: 1, sz: 1 });
    let scale = loaded[index].targetScale;
    const p = stateDur ? Math.min((T - stateStart) / stateDur, 1) : 1;

    switch (state) {
      case 'IDLE':
        if (p >= 1) startGesture(pick(RANDOM_GESTURES));
        break;

      case 'SENTIENT':
        gesture(p, pose);
        if (p >= 1) advance();
        break;

      case 'OUT':
      case 'BACK': {
        // Federnder Spin um eine zufällige Achse, volle 360°
        pose['r' + spin.axis] = p >= 1 ? 0 : 2 * Math.PI * spring(p, CONFIG.SPIN_DAMP, CONFIG.SPIN_FREQ) * spin.dir;
        if (p < CONFIG.SWAP_AT) {
          // Quadratisch schrumpfen
          scale = lerp(fromScale, CONFIG.SWAP_MIN_SCALE, (p / CONFIG.SWAP_AT) ** 2);
        } else {
          if (!swapped) { showModel(swapTo); swapped = true; }
          // Mit Feder auf die Zielgröße der neuen Form aufpoppen
          const q = (p - CONFIG.SWAP_AT) / (1 - CONFIG.SWAP_AT);
          const target = loaded[index].targetScale;
          scale = p >= 1 ? target : lerp(CONFIG.SWAP_MIN_SCALE, target, spring(q, CONFIG.POP_DAMP, CONFIG.POP_FREQ));
        }
        if (p >= 1) {
          if (state === 'BACK') enter('IDLE', rand(CONFIG.IDLE_MIN, CONFIG.IDLE_MAX));
          else enter('SHIFTED', rand(CONFIG.SHIFTED_MIN, CONFIG.SHIFTED_MAX));
        }
        break;
      }

      case 'SHIFTED': {
        const t = T - stateStart;
        pose.ry = Math.sin(t * 3.2) * CONFIG.SHIFTED_WOBBLE;
        pose.s = 1 + Math.sin(t * 4.5) * CONFIG.SHIFTED_PULSE;
        if (p >= 1) advance();
        break;
      }
    }

    // Grundbewegung, während einer Geste gedämpft
    baseFactor = lerp(baseFactor, state === 'SENTIENT' ? CONFIG.GESTURE_BASE_DAMP : 1, k(CONFIG.LERP_BASE_DAMP, dt));
    pivot.rotation.x = Math.sin(T * 0.8) * CONFIG.SWAY_X * baseFactor;
    pivot.rotation.y = Math.sin(T * 0.55) * CONFIG.SWAY_Y * baseFactor;
    pivot.position.y = Math.sin(T * 1.3) * CONFIG.FLOAT_AMP * baseFactor;

    holder.position.set(pose.px, pose.py, 0);
    holder.rotation.set(pose.rx, pose.ry, pose.rz);
    holder.scale.set(scale * pose.s * pose.sx, scale * pose.s * pose.sy, scale * pose.s * pose.sz);
    pivot.updateMatrixWorld(true);

    // Hover: Zersplittern unter dem Cursor
    const hit = mouseOnCanvas ? hitTest() : null;
    canvas.style.cursor = hit ? 'pointer' : '';
    if (hit) {
      models[index].worldToLocal(hitLocal.copy(hit.point));
      uniforms.uHit.value.lerp(hitLocal, k(CONFIG.LERP_HIT, dt));
    }
    // Amplituden durch die Größe teilen, damit jede Form gleich stark reagiert
    const size = loaded[index].targetScale;
    uniforms.uAmp.value = lerp(uniforms.uAmp.value, hit ? CONFIG.HOVER_AMP / size : 0, k(CONFIG.LERP_AMP, dt));
    uniforms.uFlow.value = lerp(uniforms.uFlow.value, hit ? CONFIG.HOVER_FLOW / size : 0, k(CONFIG.LERP_FLOW, dt));

    // Verlauf: in Ruhe Grundfarbe, während und nach dem Wechsel Verlauf
    const gradOn = state === 'OUT' || state === 'SHIFTED' || state === 'BACK';
    uniforms.uGrad.value = lerp(uniforms.uGrad.value, gradOn ? 1 : 0, k(CONFIG.LERP_GRAD, dt));

    // Punktlichter: Kreisbahnen, folgen der Maus leicht, Farben wandern
    mouseSmooth.x = lerp(mouseSmooth.x, mouse.x, k(CONFIG.LERP_MOUSE, dt));
    mouseSmooth.y = lerp(mouseSmooth.y, mouse.y, k(CONFIG.LERP_MOUSE, dt));
    const mx = mouseSmooth.x * worldPerPx;
    const my = -mouseSmooth.y * worldPerPx;
    const o = CONFIG.LIGHT_ORBIT;
    lights[0].position.set(Math.cos(T * 0.35) * o + mx, Math.sin(T * 0.5) * o * 0.6 + my, 1.2 + Math.sin(T * 0.3) * 0.3);
    lights[1].position.set(Math.cos(T * 0.27 + Math.PI) * o + mx, Math.sin(T * 0.41 + 2) * o * 0.6 + my, 1.0 + Math.cos(T * 0.23) * 0.3);
    const cyc = (T / CONFIG.LIGHT_CYCLE) * Math.PI * 2;
    lights[0].color.lerpColors(lightA, lightB, 0.5 + 0.5 * Math.sin(cyc));
    lights[1].color.lerpColors(lightA, lightB, 0.5 - 0.5 * Math.sin(cyc));

    renderer.render(scene, camera);
    if (first) {
      first = false;
      root.classList.add('is-3d'); // statisches Logo ausblenden, Canvas einblenden
    }
  }

  function play() {
    if (running) return;
    running = true;
    last = performance.now();
    raf = requestAnimationFrame(frame);
  }
  function pause() {
    running = false;
    cancelAnimationFrame(raf);
  }

  new IntersectionObserver(([entry]) => (entry.isIntersecting ? play() : pause())).observe(root);

  // Wer während des Besuchs reduzierte Bewegung einschaltet, bekommt das statische Logo
  reducedMotion.addEventListener('change', (e) => {
    if (!e.matches) return;
    pause();
    root.classList.remove('is-3d');
  });
}

/* ── Easter Egg: grüne Linien ─────────────────────────────────────────────
 * Feine, leicht geschwungene Linien laufen vom Logo aus über den Bildschirm,
 * jede mit einem Verlauf, der zum Ende hin ausläuft. Weitere Klicks während des
 * Effekts hängen neue Linien an und schieben das Ausblenden nach hinten.
 * Ein SVG über der Seite, ohne Klicks abzufangen, wird danach wieder entfernt. */
let egg = null; // { svg, defs, extra, ids, until, fade }

function greenLines(x0, y0, count) {
  if (!document.body.animate) return;
  const w = window.innerWidth;
  const h = window.innerHeight;

  if (!egg) {
    const svg = document.createElementNS(SVG_NS, 'svg');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    svg.style.cssText = 'position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:90;overflow:visible';
    const defs = document.createElementNS(SVG_NS, 'defs');
    svg.appendChild(defs);
    document.body.appendChild(svg);
    egg = { svg, defs, extra: CONFIG.EGG_EXTRA_CLICKS, ids: 0, until: 0, fade: null };
  }
  const { svg, defs } = egg;

  // Zielpunkte entlang des Bildschirmrands verteilen (oben → rechts → unten → links),
  // damit jede Linie über die Seite läuft, egal wo das Logo sitzt
  const perimeter = 2 * (w + h);
  const edgePoint = (u) => {
    let d = (((u % 1) + 1) % 1) * perimeter;
    if (d < w) return [d, 0];
    d -= w;
    if (d < h) return [w, d];
    d -= h;
    if (d < w) return [w - d, h];
    return [0, h - (d - w)];
  };
  const offset = Math.random(); // jede Salve in andere Richtungen

  const now = document.timeline.currentTime || performance.now();
  for (let i = 0; i < count; i++) {
    const [tx, ty] = edgePoint(offset + (i + rand(0.15, 0.85)) / count);
    const angle = Math.atan2(ty - y0, tx - x0);
    const len = Math.hypot(tx - x0, ty - y0) * rand(0.9, 1.15);
    const ex = x0 + Math.cos(angle) * len;
    const ey = y0 + Math.sin(angle) * len;
    // Zwei Kontrollpunkte seitlich versetzt: sanfte S- oder Bogenform
    const bend = len * rand(0.12, 0.28) * (Math.random() < 0.5 ? -1 : 1);
    const nx = -Math.sin(angle);
    const ny = Math.cos(angle);
    const c1x = x0 + Math.cos(angle) * len * 0.33 + nx * bend;
    const c1y = y0 + Math.sin(angle) * len * 0.33 + ny * bend;
    const c2x = x0 + Math.cos(angle) * len * 0.66 - nx * bend * rand(0.2, 1);
    const c2y = y0 + Math.sin(angle) * len * 0.66 - ny * bend * rand(0.2, 1);

    const id = 'xpo-egg-' + egg.ids++;
    const grad = document.createElementNS(SVG_NS, 'linearGradient');
    grad.id = id;
    grad.setAttribute('gradientUnits', 'userSpaceOnUse');
    grad.setAttribute('x1', x0); grad.setAttribute('y1', y0);
    grad.setAttribute('x2', ex); grad.setAttribute('y2', ey);
    const strength = rand(0.35, 0.7);
    grad.innerHTML = `<stop offset="0" stop-color="${CONFIG.EGG_COLOR}" stop-opacity="${strength}"/>`
      + `<stop offset="0.6" stop-color="${CONFIG.EGG_COLOR}" stop-opacity="${strength * 0.45}"/>`
      + `<stop offset="1" stop-color="${CONFIG.EGG_COLOR}" stop-opacity="0"/>`;
    defs.appendChild(grad);

    const path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', `M${x0},${y0} C${c1x},${c1y} ${c2x},${c2y} ${ex},${ey}`);
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', `url(#${id})`);
    path.setAttribute('stroke-width', rand(0.8, 2.2).toFixed(2));
    path.setAttribute('stroke-linecap', 'round');
    svg.appendChild(path);

    const L = path.getTotalLength();
    const delay = (i * CONFIG.EGG_STAGGER + rand(0, 0.12)) * 1000;
    const dur = CONFIG.EGG_DRAW * 1000 * rand(0.85, 1.15);
    egg.until = Math.max(egg.until, now + delay + dur);
    path.style.strokeDasharray = `${L}`;
    path.style.strokeDashoffset = `${L}`;
    path.animate(
      [{ strokeDashoffset: L }, { strokeDashoffset: 0 }],
      { duration: dur, delay, easing: 'cubic-bezier(0.22, 0.8, 0.25, 1)', fill: 'forwards' }
    );
  }

  // Ausblenden erst, wenn die letzte Linie fertig ist; ein laufendes Ausblenden zurücknehmen
  if (egg.fade) egg.fade.cancel();
  const current = egg;
  current.fade = svg.animate(
    [{ opacity: 1 }, { opacity: 0 }],
    { duration: CONFIG.EGG_FADE * 1000, delay: Math.max(current.until - now - 200, 0), easing: 'ease-out', fill: 'forwards' }
  );
  current.fade.onfinish = () => {
    current.svg.remove();
    if (egg === current) egg = null;
  };
}
