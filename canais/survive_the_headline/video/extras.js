/*!
 * Figurantes. Cada um nasce de um dos corpos da família (dan, mia, leo, bea) com
 * outra pele, cabelo, roupa e proporção, mais acessórios por papel. Não existe
 * config próprio: Extras.ensure(papel, n) registra a variante na primeira vez.
 *
 * O número n escolhe a variante; o mesmo (papel, n) sai sempre igual.
 */
(function (root) {
  'use strict';
  const CE = root.CharacterEngine;
  const builds = {}, register = CE.register.bind(CE);
  CE.register = (name, build) => { builds[name] = build; return register(name, build); };

  const NS = 'http://www.w3.org/2000/svg';
  const hash = (a, b) => { let x = (Math.imul(a, 2654435761) + Math.imul(b, 40503)) >>> 0; x ^= x >>> 13; x = Math.imul(x, 1274126177) >>> 0; return (x ^ (x >>> 16)) >>> 0; };
  const pick = (list, h, salt) => list[hash(h, salt) % list.length];
  const shade = (hex, k) => {
    const n = parseInt(hex.slice(1), 16), c = s => Math.max(0, Math.min(255, Math.round(((n >> s) & 255) * k)));
    return '#' + [c(16), c(8), c(0)].map(v => v.toString(16).padStart(2, '0')).join('');
  };

  const SKIN = [['#f3c7a6', '#dfa684'], ['#eab48e', '#d6976f'], ['#d59a6e', '#bb8055'], ['#b5784e', '#99633e'], ['#8d5a38', '#74482b'], ['#6a4129', '#55331f']];
  const HAIR = ['#1b1512', '#2f2119', '#4a2f1f', '#7a5230', '#b98a4a', '#a8482a', '#8d8d92', '#c9c9ce'];
  const PANTS = ['#2b3346', '#3a4258', '#4a4a52', '#39506f', '#5a4a3a', '#6b6f78'];
  const SHOE = ['#2a2420', '#5f381b', '#3a3f4b', '#e8e8ea'];
  const TOPS = ['#c0392b', '#2e7d6b', '#d98e2b', '#6a4c93', '#3f7cc0', '#8a9a5b', '#b0577a', '#4a5568', '#e0d3b8', '#2d6a4f', '#a0522d'];

  const ROLES = {
    crew:     { base: ['dan', 'leo', 'dan'], top: ['#ef7a1a', '#f0a51e', '#d9c021'], pants: ['#3a4258', '#39506f'], hat: ['#f4c20d', '#f7f7f2', '#ef7a1a'], vest: true },
    trader:   { base: ['dan', 'mia', 'dan'], top: ['#f2f4f8', '#dfe8f4', '#f6e9e0', '#20293d'], pants: ['#1d2333', '#2b3346'], tie: ['#c0392b', '#2e5fa8', '#7a2e8a', '#d98e2b'] },
    office:   { base: ['dan', 'mia', 'mia'], top: ['#2a3550', '#4a5568', '#6a4c93', '#f2f4f8'], pants: ['#1d2333', '#2b3346'], tie: ['#2e5fa8', '#7a2e8a'] },
    nurse:    { base: ['mia', 'mia', 'dan'], top: ['#2f7fb0', '#5a6fc0', '#1f9e8f', '#c86a9a'], pants: null, badge: true },
    doctor:   { base: ['dan', 'mia'], top: ['#f4f6f8'], pants: ['#2b3346', '#4a5568'], badge: true },
    student:  { base: ['leo', 'leo', 'mia', 'leo'], top: TOPS, pants: PANTS, teen: true },
    kid:      { base: ['bea'], top: TOPS, pants: PANTS },
    shopper:  { base: ['dan', 'mia', 'mia', 'leo', 'dan'], top: TOPS, pants: PANTS },
    cashier:  { base: ['mia', 'leo'], top: ['#b3262c'], pants: ['#2b3346'], badge: true },
    neighbor: { base: ['dan', 'mia', 'dan', 'mia'], top: TOPS, pants: PANTS, older: true },
    anchor:   { base: ['mia'], top: ['#7a1f3a'], pants: ['#1d2333'], skin: 3, hair: 0 },
    agent:    { base: ['mia', 'dan', 'mia'], top: ['#3f7cc0'], pants: ['#2b3346'], badge: true },
    boss:     { base: ['dan'], top: ['#20293d'], pants: ['#1d2333'], hat: ['#f7f7f2'], tie: ['#c0392b'], skin: 0, hair: 6 }
  };

  /* Troca as cores no objeto que o próprio config usa ao desenhar. */
  function paint(cfg, look) {
    const C = cfg.C;
    C.skin = look.skin[0]; C.skinShade = look.skin[1];
    if (C.stubble) C.stubble = shade(look.skin[0], 0.93);
    C.hair = look.hair; C.brow = shade(look.hair, 0.72);
    if (C.hairShine) C.hairShine = shade(look.hair, 1.35);
    if (C.hairDeep) C.hairDeep = shade(look.hair, 0.72);
    C.iris = look.iris;
    if (C.freckle) C.freckle = look.skin[1];
    if (C.mole) C.mole = look.skin[1];
    if (C.blush) C.blush = shade(look.skin[1], 0.9);
    Object.keys(cfg.OUTFITS || {}).forEach(name => {
      const o = cfg.OUTFITS[name];
      if (o.top) { o.top = look.top; o.topShade = shade(look.top, 0.82); o.topDark = shade(look.top, 0.66); }
      if (o.pants) { o.pants = look.pants; o.pantsShade = shade(look.pants, 0.82); o.pantsLight = shade(look.pants, 1.3); }
      if (o.shoe) { o.shoe = look.shoe; if (o.stripe) o.stripe = shade(look.shoe, 0.8); }
      if (o.badge !== undefined) o.badge = !!look.badge;
    });
    ['navy', 'hoodie', 'dress', 'shirt'].forEach(k => { if (C[k]) { C[k] = look.top; if (C[k + 'Shade']) C[k + 'Shade'] = shade(look.top, 0.82); if (C[k + 'Dark']) C[k + 'Dark'] = shade(look.top, 0.66); } });
    ['jeans', 'pants'].forEach(k => { if (C[k]) { C[k] = look.pants; if (C[k + 'Shade']) C[k + 'Shade'] = shade(look.pants, 0.82); if (C[k + 'Light']) C[k + 'Light'] = shade(look.pants, 1.3); } });
    ['boot', 'shoe'].forEach(k => { if (C[k]) { C[k] = look.shoe; if (C[k + 'Shade']) C[k + 'Shade'] = shade(look.shoe, 0.8); } });
  }

  const SPEC = {};
  function ensure(role, n) {
    const name = 'x_' + role + '_' + n;
    if (SPEC[name]) return SPEC[name];
    const R = ROLES[role];
    if (!R) throw new Error('Figurante: papel desconhecido ' + role);
    const h = hash(role.length * 131 + role.charCodeAt(0), n + 1), base = pick(R.base, h, 1);
    const look = {
      skin: SKIN[R.skin !== undefined ? R.skin : hash(h, 2) % SKIN.length],
      hair: R.older && hash(h, 3) % 2 ? pick(HAIR.slice(6), h, 4) : HAIR[R.hair !== undefined ? R.hair : hash(h, 4) % (R.older ? 8 : 6)],
      iris: pick(['#3b2a1a', '#5a3a22', '#2d5a7a', '#3f6a4a'], h, 5),
      top: pick(R.top, h, 6),
      pants: R.pants ? pick(R.pants, h, 7) : null,
      shoe: pick(SHOE, h, 8),
      badge: !!R.badge
    };
    if (!look.pants) look.pants = look.top;   // conjunto de enfermagem
    register(name, STH => { const cfg = builds[base](STH); paint(cfg, look); return cfg; });
    const adult = !R.teen && base !== 'bea';
    SPEC[name] = {
      name, base, role,
      height: (adult ? 0.94 + (hash(h, 9) % 13) / 100 : 0.97 + (hash(h, 9) % 7) / 100) * (base === 'leo' && !R.teen ? 1.04 : 1),
      girth: 0.93 + (hash(h, 10) % 20) / 100,
      hat: R.hat ? pick(R.hat, h, 11) : null,
      tie: R.tie ? pick(R.tie, h, 12) : null,
      vest: !!R.vest,
      coat: role === 'doctor',
      outfit: base === 'mia' ? (role === 'nurse' ? 'scrubs' : 'casual') : undefined
    };
    return SPEC[name];
  }

  const add = (tag, attrs, parent) => { const n = document.createElementNS(NS, tag); Object.keys(attrs).forEach(k => n.setAttribute(k, attrs[k])); parent.appendChild(n); return n; };
  const LINE = { stroke: '#1b1a22', 'stroke-width': 5, 'stroke-linejoin': 'round' };

  /* Acessórios por cima do corpo. Moram nos grupos da cabeça e do tronco, então seguem o personagem. */
  function dress(c, spec) {
    if (spec.hat && c.head) {
      const g = add('g', {}, c.head);
      add('path', Object.assign({ d: 'M-96 -128Q-90 -214 0 -218Q90 -214 96 -128Z', fill: spec.hat }, LINE), g);
      add('path', Object.assign({ d: 'M-112 -128H112Q118 -112 104 -110H-104Q-118 -112 -112 -128Z', fill: shade(spec.hat, 0.86) }, LINE), g);
      add('rect', { x: -12, y: -216, width: 24, height: 88, fill: shade(spec.hat, 0.86) }, g);
    }
    const torso = c.torsoShape && c.torsoShape.parentNode;
    if (!torso) return;
    if (spec.tie) add('path', Object.assign({ d: 'M-13 -214L13 -214L9 -196L22 -74L0 -48L-22 -74L-9 -196Z', fill: spec.tie }, LINE), torso);
    if (spec.vest) {
      add('rect', { x: -92, y: -132, width: 184, height: 20, fill: '#f6f7d8', opacity: 0.92 }, torso);
      add('rect', { x: -88, y: -70, width: 176, height: 20, fill: '#f6f7d8', opacity: 0.92 }, torso);
    }
    if (spec.coat) {
      add('path', { d: 'M-100 -204L-30 -228L-6 -120L-18 46H-96Z', fill: '#ffffff', stroke: '#c9d2dc', 'stroke-width': 3 }, torso);
      add('path', { d: 'M100 -204L30 -228L6 -120L18 46H96Z', fill: '#ffffff', stroke: '#c9d2dc', 'stroke-width': 3 }, torso);
    }
  }

  /* Plateia barata: figuras chapadas de fundo, sem esqueleto, para dar massa à cena. */
  function silhouettes(parent, o) {
    const g = add('g', { 'data-crowd': 1 }, parent), people = [];
    let x = hash(o.seed || 1, 1);
    const rnd = () => { x = hash(x, 7); return (x % 1000) / 1000; };
    for (let r = 0; r < (o.rows || 2); r++) {
      const y = o.y + r * (o.gap || 46), s = (o.scale || 0.42) * (1 + r * 0.16), step = 118 * s * (o.spread || 1);
      for (let px = (o.from || 40) + rnd() * step; px < (o.to || 1880); px += step * (0.8 + rnd() * 0.6)) {
        const hue = pick(o.colors || ['#3a4358', '#2f3749', '#454f66', '#343c50'], Math.floor(rnd() * 1e6), 3);
        const f = add('g', {}, g), up = rnd() < (o.raised || 0.18), side = rnd() < 0.5 ? -1 : 1;
        add('path', { d: 'M-46 170Q-52 40 -34 22Q0 6 34 22Q52 40 46 170Z', fill: hue }, f);
        add('circle', { cx: 0, cy: -8, r: 26, fill: shade(hue, 1.28) }, f);
        if (up) add('path', { d: 'M' + side * 30 + ' 34L' + side * 66 + ' -46', stroke: hue, 'stroke-width': 19, 'stroke-linecap': 'round', fill: 'none' }, f);
        people.push({ f, px, y: y + rnd() * 10, s: s * (0.92 + rnd() * 0.18), ph: rnd() * 6.28, sp: 1.2 + rnd() * 2.2 + (o.panic || 0) * 3, amp: 2 + (o.panic || 0) * 8 });
      }
    }
    const update = t => people.forEach(p => {
      p.f.setAttribute('transform', 'translate(' + (p.px + Math.sin(t * p.sp * 0.5 + p.ph) * p.amp).toFixed(1) + ' ' + (p.y - Math.abs(Math.sin(t * p.sp + p.ph)) * p.amp).toFixed(1) + ') scale(' + p.s.toFixed(3) + ')');
    });
    update(0);
    return { g, update };
  }

  root.Extras = { ensure, dress, silhouettes, ROLES };
})(typeof self !== 'undefined' ? self : this);
