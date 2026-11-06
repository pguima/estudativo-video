/*!
 * Câmera e efeitos de direção. Tudo é função pura do tempo do plano, então cada
 * plano continua podendo ser renderizado sozinho e sair idêntico.
 *
 * Um plano tem uma lista de tomadas:
 *   cam: 'push'                                  uma tomada só
 *   cuts: [{ at: 0, cam: 'wide' },               corte seco dentro do plano
 *          { at: '@cancelled', cam: 'crash:dan' }]
 *
 * at aceita fração do plano (0 a 1), segundos (> 1) ou '@palavra' / '@palavra#2',
 * que acerta o instante em que a narração diz aquela palavra.
 *
 * Câmeras:
 *   wide · push · pull · hold
 *   close:quem:zoom       aproxima devagar
 *   ecu:quem              olhos, muito perto
 *   crash:quem:zoom       zoom violento e segura
 *   rack:quem:zoom        recua rápido do rosto e abre
 *   pan:a:b:zoom          anda de um personagem até o outro
 *   track:quem:zoom       acompanha quem anda
 *   tilt:quem:zoom        sobe dos pés ao rosto
 *   vertigo:quem:zoom     fundo cresce e o personagem fica parado
 *   dutch:quem:zoom:graus horizonte torto
 *   [[x,y,z,roll,fundo], [x,y,z,roll,fundo]]     à mão
 *
 * Batidas de efeito: hits: [{ at, punch, shake, flash, stamp, color, x, y, rot, hold }]
 */
(function (root) {
  'use strict';
  const { clamp, lerp } = root.GfxUtil;
  const S = k => k * k * (3 - 2 * k);
  const EASE = {
    smooth: S,
    linear: k => k,
    expo: k => 1 - Math.pow(1 - k, 4),
    back: k => { const c = 2.2, x = k - 1; return 1 + (c + 1) * x * x * x + c * x * x; }
  };
  const HEAD = { dan: 400, mia: 430, leo: 440, bea: 660, biscuit: 780 };
  const EYE = { dan: 372, mia: 398, leo: 410, bea: 636, biscuit: 760 };
  const HAND = { day: 0.25, dusk: 0.35, tense: 0.75, night: 0.5, dark: 0.95 };
  const TRANS = 0.2;

  /* quando a narração diz cada palavra: mesma conta da legenda */
  function wordTimes(s) {
    if (s.wt) return s.wt;
    s.wt = [];
    if (!s.n) return s.wt;
    const list = s.n.trim().split(/\s+/), total = list.reduce((a, w) => a + w.length + 2, 0), span = s.dur - 0.45 - (s.hold || 0);
    let at = 0.2;
    list.forEach(w => { s.wt.push([w.toLowerCase().replace(/[^a-z0-9$%-]/g, ''), at]); at += span * (w.length + 2) / total; });
    return s.wt;
  }
  function when(s, at) {
    if (typeof at === 'string' && at[0] === '@') {
      const [w, nth] = at.slice(1).toLowerCase().split('#');
      const hits = wordTimes(s).filter(x => x[0].startsWith(w));
      if (!hits.length) throw new Error('Plano ' + s.id + ': a narração não tem a palavra "' + w + '".');
      return hits[Math.min((+nth || 1) - 1, hits.length - 1)][1];
    }
    return at <= 1 ? at * s.dur : at;
  }

  function spot(s, who, over) { const a = (over && over[who]) || s.cast[who]; return a; }

  /* Traduz o nome da câmera em { a, b, ease, move } */
  function resolve(s, spec, span, place) {
    if (Array.isArray(spec)) return { a: spec[0], b: spec[1], ease: 'smooth' };
    if (spec && typeof spec === 'object') return Object.assign({ ease: 'smooth' }, spec);
    const name = spec || (s.gfx && !s.bg ? 'drift' : 'push'), list = Object.keys(s.cast || {}).filter(n => !(s.cast[n].fg));
    const mid = list.length ? list.reduce((v, n) => v + s.cast[n].x, 0) / list.length : 960;
    const p = name.split(':'), kind = p[0], who = p[1], X = who && s.cast && s.cast[who] ? spot(s, who, place).x : 960;
    const Y = who ? (HEAD[who] || 420) + 90 : 540, E = who ? EYE[who] || 400 : 400, n = +p[2];
    switch (kind) {
      case 'wide': return { a: [960, 540, 1], b: [960, 540, 1.045], ease: 'linear' };
      case 'drift': { const d = s.i % 2 ? 1 : -1; return { a: [960 - d * 28, 540, 1.02], b: [960 + d * 28, 540, 1.09], ease: 'linear' }; }
      case 'hold': return { a: [960, 540, 1], b: [960, 540, 1.01], ease: 'linear' };
      case 'pull': return { a: [mid, 600, 1.24], b: [960, 540, 1.02] };
      case 'push': return { a: [960, 540, 1.02], b: [mid, 575, 1.2] };
      case 'close': { const z = n || 1.8; return { a: [X, Y, z * 0.93], b: [X, Y, z * 1.03], ease: 'linear' }; }
      case 'ecu': { const z = n || 3.1; return { a: [X, E, z * 0.94], b: [X, E, z * 1.05], ease: 'linear' }; }
      case 'crash': { const z = n || 2.2; return { a: [X, Y, z * 0.5], b: [X, Y, z], ease: 'expo', move: 0.34, creep: 0.018 }; }
      case 'rack': { const z = n || 1.1; return { a: [X, Y, 2.3], b: [X, 540, z], ease: 'expo', move: 0.5, creep: 0.008 }; }
      case 'pan': { const z = +p[3] || 1.7, B = spot(s, p[2], place); return { a: [X, Y, z], b: [B.x, (HEAD[p[2]] || 420) + 90, z] }; }
      case 'track': { const z = n || 1.5, w = (s.walks || []).find(v => v.who === who); return { a: [X, Y + 110, z], b: [w ? w.to : X, Y + 110, z], ease: 'linear' }; }
      case 'tilt': { const z = n || 2; return { a: [X, 820, z], b: [X, Y, z * 1.05] }; }
      case 'vertigo': { const z = n || 1.7; return { a: [X, Y, z, 0, 1], b: [X, Y, z * 1.06, 0, 1.75], ease: 'smooth' }; }
      case 'dutch': { const z = n || 1.7, r = +p[3] || -7; return { a: [X, Y, z * 0.95, r * 0.6], b: [X, Y, z * 1.05, r], ease: 'linear' }; }
      default: throw new Error('Plano ' + s.id + ': câmera desconhecida "' + name + '".');
    }
  }

  function build(s) {
    const list = s.cuts || [{ at: 0, cam: s.cam }];
    s.paths = list.map(c => Object.assign({}, c, { t0: when(s, c.at || 0) })).sort((a, b) => a.t0 - b.t0);
    s.paths[0].t0 = 0;
    let place = null;
    s.paths.forEach((p, i) => {
      p.t1 = i + 1 < s.paths.length ? s.paths[i + 1].t0 : s.dur;
      if (p.place) place = Object.assign({}, s.cast, place, p.place);
      p.path = resolve(s, p.cam, p.t1 - p.t0, place);
      p.fired = false;
    });
    s.hitList = (s.hits || []).map(h => Object.assign({}, h, { t: when(s, h.at) })).sort((a, b) => a.t - b.t);
  }

  function pathAt(s, t) {
    let c = s.paths[0];
    s.paths.forEach(p => { if (t >= p.t0) c = p; });
    const P = c.path, local = t - c.t0, span = Math.max(0.01, c.t1 - c.t0), fn = EASE[P.ease || 'smooth'];
    const k = P.move ? fn(clamp(local / P.move)) : fn(clamp(local / span));
    const pick = i => { const a = P.a[i] === undefined ? (i === 4 ? 1 : 0) : P.a[i], b = P.b[i] === undefined ? (i === 4 ? 1 : 0) : P.b[i]; return lerp(a, b, k); };
    const v = [pick(0), pick(1), pick(2), pick(3), pick(4)];
    if (P.move && local > P.move) v[2] *= 1 + (P.creep || 0) * (local - P.move);
    return { v, cut: c };
  }

  /* Batidas somadas no instante t */
  function impulse(s, t) {
    let punch = 0, shake = 0;
    (s.hitList || []).forEach(h => {
      const age = t - h.t;
      if (age < 0) return;
      if (h.punch) punch += h.punch * Math.exp(-age * 7) * Math.cos(age * 16);
      if (h.shake && age < 0.7) shake = Math.max(shake, h.shake * (1 - age / 0.7));
    });
    if (s.shake && t < s.shake.dur) shake = Math.max(shake, s.shake.amp * (1 - t / s.shake.dur));
    return { punch, shake };
  }

  /* Mão no ombro: soma de senos lentos com fase vinda do plano */
  function handheld(s, t, amt) {
    const p = s.i * 1.7;
    return {
      x: (Math.sin(t * 0.83 + p) + 0.5 * Math.sin(t * 2.1 + p * 2)) * 11 * amt,
      y: (Math.sin(t * 1.07 + p * 3) + 0.5 * Math.cos(t * 2.6 + p)) * 8 * amt,
      roll: Math.sin(t * 0.61 + p) * 0.34 * amt
    };
  }

  function state(s, t, stress) {
    const { v, cut } = pathAt(s, t), hit = impulse(s, t);
    const amt = s.hand !== undefined ? s.hand : HAND[cut.mood || s.mood || 'day'] || 0.25;
    const h = handheld(s, t, amt);
    /* acima de 75 de stress, a imagem pulsa como batimento */
    const tense = clamp((stress - 75) / 25), beat = Math.pow(Math.max(0, Math.sin(t * 5.2)), 12) * 0.016 * tense;
    return {
      x: v[0] + h.x + Math.sin(t * 61) * hit.shake, y: v[1] + h.y + Math.cos(t * 47) * hit.shake,
      z: v[2] * (1 + hit.punch + beat), roll: v[3] + h.roll, bg: v[4], cut
    };
  }

  /* Aplica no cenário: viewBox + paralaxe do fundo e da frente + giro */
  function applyScene(scene, c) {
    const w = 1920 / c.z, h = 1080 / c.z;
    const vx = clamp(c.x - w / 2, 0, 1920 - w), vy = clamp(c.y - h / 2, 0, 1080 - h);
    scene.svg.setAttribute('viewBox', vx.toFixed(2) + ' ' + vy.toFixed(2) + ' ' + w.toFixed(2) + ' ' + h.toFixed(2));
    const cx = vx + w / 2, cy = vy + h / 2, dx = cx - 960, dy = cy - 540;
    const s = 1.05 * c.bg;
    scene.back.setAttribute('transform', 'translate(' + (cx + dx * 0.05).toFixed(2) + ' ' + (cy + dy * 0.03).toFixed(2) + ') scale(' + s.toFixed(4) + ') translate(' + (-cx).toFixed(2) + ' ' + (-cy).toFixed(2) + ')');
    scene.front.setAttribute('transform', 'translate(' + (-dx * 0.07).toFixed(2) + ' ' + (-dy * 0.04).toFixed(2) + ')');
    const rot = c.roll, fit = 1 + Math.abs(rot) * 0.034;
    document.getElementById('tela').style.transform = rot ? 'rotate(' + rot.toFixed(3) + 'deg) scale(' + fit.toFixed(4) + ')' : 'none';
  }

  function applyGfx(c) {
    const el = document.getElementById('gfx'), z = Math.max(1, c.z), w = 1920 / z, h = 1080 / z;
    const vx = clamp(c.x - w / 2, 0, 1920 - w), vy = clamp(c.y - h / 2, 0, 1080 - h);
    el.style.transform = 'rotate(' + c.roll.toFixed(3) + 'deg) scale(' + (z * (1 + Math.abs(c.roll) * 0.034)).toFixed(4) + ') translate(' + (-vx).toFixed(2) + 'px ' + (-vy).toFixed(2) + 'px)';
    el.style.transformOrigin = '0 0';
  }

  /* Transição: saída e entrada correm em planos separados, cada um faz metade */
  function transition(s, t) {
    const world = document.getElementById('world'), mb = document.getElementById('mbx');
    let k = 0, kind = null, sign = 1;
    if (s.tin && t < TRANS) { k = 1 - t / TRANS; kind = s.tin; sign = -1; }
    else if (s.tout && t > s.dur - TRANS) { k = (t - (s.dur - TRANS)) / TRANS; kind = s.tout; sign = 1; }
    if (!kind) { world.style.transform = 'none'; world.style.filter = 'none'; return; }
    const e = k * k, d = s.i % 2 ? 1 : -1;
    if (kind === 'whip') {
      mb.setAttribute('stdDeviation', (e * 90).toFixed(1) + ' 0');
      world.style.filter = 'url(#mb)';
      world.style.transform = 'scale(' + (1 + e * 0.24).toFixed(3) + ') translateX(' + (sign * d * e * 170).toFixed(1) + 'px)';
    } else {  // zoom através
      world.style.filter = 'blur(' + (e * 16).toFixed(1) + 'px)';
      world.style.transform = 'scale(' + (sign > 0 ? 1 + e * 0.9 : 1 + e * 0.5).toFixed(3) + ')';
    }
  }

  /* Palavra carimbada na tela e clarão */
  function effects(s, t) {
    const flash = document.getElementById('flash');
    let f = 0, color = '#fff';
    (s.hitList || []).forEach(h => {
      if (h.flash && t >= h.t && t - h.t < 0.28) { f = Math.max(f, 1 - (t - h.t) / 0.28); color = h.flash; }
      if (!h.el) return;
      const age = t - h.t, hold = h.hold || 1.5;
      if (age < 0 || age > hold + 0.25) { h.el.style.display = 'none'; return; }
      const k = clamp(age / 0.13), sc = 1 + 1.7 * Math.pow(1 - k, 3);
      h.el.style.display = 'block';
      h.el.style.opacity = age > hold ? 1 - (age - hold) / 0.25 : k;
      h.el.style.transform = 'translate(-50%,-50%) rotate(' + (h.rot === undefined ? -3 : h.rot) + 'deg) scale(' + sc.toFixed(3) + ')';
    });
    flash.style.background = color; flash.style.opacity = f.toFixed(3);
    const bars = s.bars ? S(clamp(t / 0.45)) : 0;
    document.getElementById('barT').style.transform = 'scaleY(' + bars + ')';
    document.getElementById('barB').style.transform = 'scaleY(' + bars + ')';
  }

  function mountStamps(s) {
    const fx = document.getElementById('fx');
    fx.innerHTML = '';
    (s.hitList || []).forEach(h => {
      if (!h.stamp) return;
      const el = document.createElement('div');
      el.className = 'stamp'; el.textContent = h.stamp;
      el.style.left = (h.x || 960) + 'px'; el.style.top = (h.y || 500) + 'px'; el.style.color = h.color || '#ff3b3b';
      if (h.size) el.style.fontSize = h.size + 'px';
      el.style.display = 'none';
      fx.appendChild(el); h.el = el;
    });
  }

  root.Camera = { build, when, wordTimes, state, applyScene, applyGfx, transition, effects, mountStamps, HEAD };
})(typeof self !== 'undefined' ? self : this);
