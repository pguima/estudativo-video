/*!
 * PoseController — tabelas de pose e amostragem por ângulo.
 * Cada pose humana tem três chaves (frente, 3/4, perfil); o giro passa pelas três.
 * Sobrevivem aqui as regras que custaram correções: pé apoiado no chão (plant),
 * braço avulso e espelhamento sem salto ao cruzar a frente.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { lerp, lerpDict, key3, ease, FLOOR } = STH.SVGRenderer;

  /* r0..r3 = dobra dos dedos, r4 = abertura do polegar. */
  const HANDS = {
    open: [0, 0, 0, 0, 1], relaxed: [0.3, 0.35, 0.4, 0.45, 0.5], fist: [1, 1, 1, 1, 0.1],
    point: [0, 1, 1, 1, 0.2], grip: [0.82, 0.82, 0.82, 0.82, 0.35]
  };
  const hands = (r, l) => {
    const o = {};
    HANDS[r].forEach((v, i) => { o['r' + i] = v; });
    HANDS[l].forEach((v, i) => { o['l' + i] = v; });
    return o;
  };

  /* Monta { front, q, side } a partir da pose-base. */
  const poseMaker = (base, sideBase) => (front, side, quarter, extra) => {
    const shared = extra || {};
    const out = {
      front: Object.assign({}, base, shared, front),
      side: Object.assign({}, base, sideBase, shared, side)
    };
    out.q = Object.assign(lerpDict(out.front, out.side, 0.5), quarter);
    return out;
  };

  const SWAP = [['ru', 'lu', -1], ['rf', 'lf', -1], ['rh', 'lh', -1], ['rfl', 'lfl', 1], ['rt', 'lt', -1], ['rs', 'ls', -1],
    ['rfoot', 'lfoot', -1], ['rty', 'lty', 1], ['rsy', 'lsy', 1], ['r0', 'l0', 1], ['r1', 'l1', 1],
    ['r2', 'l2', 1], ['r3', 'l3', 1], ['r4', 'l4', 1]];
  function mirror(p) {
    const o = Object.assign({}, p);
    SWAP.forEach(([a, b, s]) => { o[a] = p[b] * s; o[b] = p[a] * s; });
    ['rootX', 'rootR', 'spine', 'head', 'gx'].forEach(k => { o[k] = -p[k]; });
    return o;
  }

  /* Amostra as juntas de um humano no ângulo atual. */
  function sampleHuman(c, st) {
    const { POSES, MOTION, M, hipY = M.hipY } = c.cfg;
    const sign = c.turn < 0 ? -1 : 1;
    const live = c.animation !== 'none';
    const get = name => {
      const P = POSES[name];
      const a = Object.assign({}, P.front), q = Object.assign({}, P.q), b = Object.assign({}, P.side);
      const m = MOTION[name];
      if (m && (live || m.still !== undefined)) {
        const ph = live ? c.time * m.rate : m.still;
        m.run(a, ph, 0); m.run(q, ph, 0.5); m.run(b, ph, 1);
      }
      const start = sign < 0 ? mirror(a) : a;
      const out = {};
      for (const k in start) out[k] = key3(start[k], q[k], b[k], st);
      return out;
    };
    const j = c.poseMix.sample(get);
    c.applyAnimations(j, st);
    if (j.plant > 0.01) {
      const reach = k => {
        const a = j[k + 't'] * Math.PI / 180, b = a + j[k + 's'] * Math.PI / 180;
        return hipY + M.thigh * j[k + 'ty'] * Math.cos(a) + M.shin * j[k + 'sy'] * Math.cos(b) + M.footH;
      };
      j.rootY = lerp(j.rootY, FLOOR - Math.max(reach('r'), reach('l')), j.plant);
    }
    const talk = c.talkWeight();
    if (talk > 0.01) {
      j.head += 1.6 * Math.sin(c.time * 5.3) * talk;
      j.headY += 1.6 * Math.abs(Math.sin(c.time * 4.1)) * talk;
    }
    ['r', 'l'].forEach(k => {
      const a = c.arms[k];
      if (a.w <= 0 || !a.v) return;
      const w = ease(a.w);
      j[k + 'u'] = lerp(j[k + 'u'], a.v.shoulder, w);
      j[k + 'f'] = lerp(j[k + 'f'], a.v.elbow, w);
      j[k + 'h'] = lerp(j[k + 'h'], a.v.wrist, w);
      j[k + 'fl'] = lerp(j[k + 'fl'], 1, w);
      if (a.v.hand) HANDS[a.v.hand].forEach((v, i) => { j[k + i] = lerp(j[k + i], v, w); });
    });
    return j;
  }

  /* Ciclo de caminhada e corrida comuns aos humanos; base = altura do quadril em pé. */
  const cycles = base => ({
    walking: {
      rate: 6.2, still: 0.9,
      run(j, ph, view) {
        const s = Math.sin(ph);
        if (view > 0) {
          const stride = view < 1 ? 0.8 : 1;
          const leg = a => [(-6 - 24 * Math.sin(a)) * stride, (10 + 34 * Math.max(0, Math.cos(a - 0.3))) * stride];
          const R = leg(ph), L = leg(ph + Math.PI);
          j.rt = R[0]; j.rs = R[1]; j.rfoot = -R[1] * 0.25;
          j.lt = L[0]; j.ls = L[1]; j.lfoot = -L[1] * 0.25;
          j.ru += 16 * s; j.lu -= 16 * s;
        } else {
          const lr = Math.max(0, s), ll = Math.max(0, -s);
          j.rty = 1 - 0.18 * lr; j.lty = 1 - 0.18 * ll;
          j.rsy = 1 - 0.06 * lr; j.lsy = 1 - 0.06 * ll;
          j.rootX += 3 * s; j.rootR += 0.8 * s; j.head -= 0.8 * s;
          j.ru += 5 * s; j.lu += 5 * s;
        }
      }
    },
    running: {
      rate: 11, still: 0.9,
      run(j, ph, view) {
        const s = Math.sin(ph), c = Math.cos(ph);
        const k = base.runBounce;
        if (view > 0) {
          const quarter = view < 1;
          const stride = quarter ? 0.8 : 1;
          const leg = a => [(-16 - 44 * Math.sin(a)) * stride, (44 + 52 * Math.max(0, Math.cos(a - 0.2))) * stride];
          const R = leg(ph), L = leg(ph + Math.PI);
          j.rt = R[0]; j.rs = R[1]; j.rfoot = -R[1] * 0.28;
          j.lt = L[0]; j.ls = L[1]; j.lfoot = -L[1] * 0.28;
          j.ru = quarter ? 12 + 34 * s : 40 * s;
          j.lu = quarter ? -8 - 34 * s : -40 * s;
          j.rootY = base.root + (quarter ? k[0] : k[1]) - (quarter ? k[2] : k[1]) * Math.abs(c);
        } else {
          const lr = Math.max(0, s), ll = Math.max(0, -s);
          j.rty = 1 - 0.62 * lr; j.lty = 1 - 0.62 * ll;
          j.rsy = 1 - 0.1 * lr; j.lsy = 1 - 0.1 * ll;
          j.rootY = base.root + k[0] - k[2] * Math.abs(c);
          j.rootR = 2 * s; j.spine += 2.5 * s; j.head -= 2 * s;
          j.ru += 6 * s; j.lu += 6 * s; j.rf += 18 * s; j.lf += 18 * s;
        }
      }
    }
  });

  STH.PoseController = { HANDS, hands, poseMaker, mirror, sampleHuman, cycles };
})(typeof self !== 'undefined' ? self : this);
