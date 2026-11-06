/*!
 * SVGRenderer — base visual comum a todos os personagens e cenários.
 * Matemática de curvas, criação de nós SVG e estilos de traço.
 * Nenhuma regra de personagem mora aqui.
 */
(function (root) {
  'use strict';
  const STH = root.STH = root.STH || {};

  const NS = 'http://www.w3.org/2000/svg';
  const VIEWBOX = '-425 -480 850 860';   // todo personagem usa o mesmo quadro
  const FLOOR = 340;                     // e o mesmo chão
  const LINE = 4.5;                      // e o mesmo peso de contorno

  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const smooth = t => t * t * (3 - 2 * t);
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const f = n => Math.round(n * 10) / 10;
  const TAU = Math.PI * 2;
  /* Curva que passa por três chaves: frente (u=0), 3/4 (u=0.5) e perfil (u=1). */
  const key3 = (a, b, c, u) => a * (1 - 2 * u) * (1 - u) + 4 * b * u * (1 - u) + c * u * (2 * u - 1);
  const keyOf = (k, u) => key3(k[0], k[1], k[2], u);
  const lerpDict = (a, b, t) => {
    const o = {};
    for (const k in a) o[k] = lerp(a[k], b[k] === undefined ? a[k] : b[k], t);
    return o;
  };

  function rng(seed) {
    let a = seed >>> 0;
    return function () {
      a = (a + 0x6d2b79f5) >>> 0;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  /* Curva suave por uma lista de pontos. Terceiro valor do ponto = canto vivo. */
  function spline(pts, closed) {
    const n = pts.length;
    const at = i => (closed ? pts[(i + n) % n] : pts[clamp(i, 0, n - 1)]);
    let d = 'M' + f(pts[0][0]) + ' ' + f(pts[0][1]);
    const segs = closed ? n : n - 1;
    for (let i = 0; i < segs; i++) {
      const p0 = at(i - 1), p1 = at(i), p2 = at(i + 1), p3 = at(i + 2);
      const c1x = p1[2] ? p1[0] : p1[0] + (p2[0] - p0[0]) / 6;
      const c1y = p1[2] ? p1[1] : p1[1] + (p2[1] - p0[1]) / 6;
      const c2x = p2[2] ? p2[0] : p2[0] - (p3[0] - p1[0]) / 6;
      const c2y = p2[2] ? p2[1] : p2[1] - (p3[1] - p1[1]) / 6;
      d += 'C' + f(c1x) + ' ' + f(c1y) + ' ' + f(c2x) + ' ' + f(c2y) + ' ' + f(p2[0]) + ' ' + f(p2[1]);
    }
    return d + (closed ? 'Z' : '');
  }

  /* Cápsula afilada ao longo de +y, origem na articulação. */
  function capsule(len, r0, r1) {
    return 'M' + f(-r0) + ' 0A' + f(r0) + ' ' + f(r0) + ' 0 0 1 ' + f(r0) + ' 0L' + f(r1) + ' ' + f(len) +
      'A' + f(r1) + ' ' + f(r1) + ' 0 0 1 ' + f(-r1) + ' ' + f(len) + 'Z';
  }

  /* Formas com o mesmo número de pontos em frente, 3/4 (opcional) e perfil. */
  function shapeBook(SHAPE) {
    return function shape(name, t) {
      const S = SHAPE[name];
      if (!S.q) return S.front.map((p, i) => [lerp(p[0], S.side[i][0], t), lerp(p[1], S.side[i][1], t), p[2]]);
      return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
    };
  }

  function put(el, key, val) {
    const cache = el.__c || (el.__c = {});
    if (cache[key] !== val) { cache[key] = val; el.setAttribute(key, val); }
  }
  const tf = (x, y, r, sx, sy) => 'translate(' + f(x) + ' ' + f(y) + ')' + (r ? ' rotate(' + f(r) + ')' : '') +
    (sx !== undefined ? ' scale(' + (Math.round(sx * 1000) / 1000) + ' ' + (Math.round((sy === undefined ? 1 : sy) * 1000) / 1000) + ')' : '');
  const shown = (el, op) => {
    put(el, 'display', op > 0.01 ? 'inline' : 'none');
    put(el, 'opacity', String(Math.round(op * 100) / 100));
  };
  function hexMix(a, b, t) {
    const pa = parseInt(a.slice(1), 16), pb = parseInt(b.slice(1), 16);
    const ch = s => Math.round(lerp((pa >> s) & 255, (pb >> s) & 255, t));
    return 'rgb(' + ch(16) + ',' + ch(8) + ',' + ch(0) + ')';
  }
  /* Tom derivado de uma cor de identidade, em #rrggbb. */
  function tone(hex, k) {
    const p = parseInt(hex.slice(1), 16);
    const ch = s => clamp(Math.round(((p >> s) & 255) * k), 0, 255).toString(16).padStart(2, '0');
    return '#' + ch(16) + ch(8) + ch(0);
  }

  function element(tag, attrs, parent) {
    const el = document.createElementNS(NS, tag);
    for (const k in attrs || {}) el.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(el);
    return el;
  }
  const styles = ink => ({
    outlineStyle: { fill: ink, stroke: ink, 'stroke-width': LINE * 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' },
    lineStyle: { stroke: ink, 'stroke-width': LINE, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }
  });

  /* Carrega um SVG estático (model.svg ou arte de apoio) como <img>. */
  function loadSVG(url) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.onload = () => resolve(img);
      img.onerror = () => reject(new Error('SVGRenderer: não foi possível carregar ' + url));
      img.src = url;
    });
  }

  STH.SVGRenderer = { NS, VIEWBOX, FLOOR, LINE, TAU, lerp, clamp, smooth, ease, f, key3, keyOf, lerpDict, rng, spline, capsule, shapeBook, put, tf, shown, hexMix, tone, element, styles, loadSVG };
})(typeof self !== 'undefined' ? self : this);
