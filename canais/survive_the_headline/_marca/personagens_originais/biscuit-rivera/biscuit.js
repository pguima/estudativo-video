/*!
 * BiscuitRivera — o cachorro e mascote de Survive the Headline.
 *
 * Mesma linguagem visual dos Rivera (contorno, olhos, sombras, chão comum), com
 * esqueleto próprio de quatro patas. Cada pose é definida uma única vez, em um
 * esqueleto 3D, e projetada para o ângulo atual: frente, 3/4 e perfil saem da
 * mesma conta, e as patas se apoiam no chão sozinhas.
 *
 * Uso:
 *   const biscuit = new BiscuitRivera('#palco');
 *   biscuit.setExpression('curious');
 *   biscuit.setPose('sitting');
 *   biscuit.setAnimation('tail_wag');
 *   biscuit.setDirection('right');
 *   biscuit.setAccessory('collar', true);
 *   biscuit.setVisible(true);
 *
 * Acessórios: collar (ligada por padrão), bone (na boca), bowl e ball (no chão).
 * true liga, false desliga, 'auto' devolve a decisão à pose (a bolinha aparece em playing).
 *
 * Vídeo quadro a quadro (determinístico):
 *   const biscuit = new BiscuitRivera(el, { autoStart: false, seed: 42 });
 *   biscuit.tick(1000 / 30);
 *   const svg = biscuit.toSVG();
 *
 * CSS: toda parte tem data-part e id (#biscuit-head, #biscuit-ear-left, #biscuit-tail...).
 * "right" e "left" são os lados do próprio cachorro.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.BiscuitRivera = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- Paleta travada ---------- */
  const C = {
    ink: '#1b1a22', fur: '#e0a24a', furShade: '#c9863a', furFar: '#c98a3f', furDark: '#b5752f',
    ear: '#6b3f22', earShade: '#54301a', muzzle: '#f7e6c8', muzzleShade: '#e8cfa6', chest: '#fff8ec',
    nose: '#1f1b1e', noseShine: '#6a6470', brow: '#6b3f22',
    eyeWhite: '#ffffff', iris: '#6b4226', mouth: '#5a1c22', tongue: '#ec7d86', tongueLine: '#c95d68', teeth: '#fbf7ee',
    sweat: '#8fd6ff', collar: '#d9302f', collarDark: '#a81f22', medal: '#ffc62e', medalDark: '#d99a12',
    bone: '#f4efe2', boneShade: '#d9d0ba', bowl: '#2a7fb8', bowlDark: '#1f608c', food: '#9a5a2c', foodDark: '#744119',
    ball: '#c8e03a', ballLine: '#fbfbf4', zzz: '#9fb4d9'
  };
  const VIEW_SCALE = 0.8;        // cachorro pequeno-médio ao lado dos Rivera
  const LINE = 4.5 / VIEW_SCALE; // mesmo traço na tela que os humanos
  const VIEWBOX = '-425 -480 850 860';
  const FLOOR = 340;

  const L = { fu: 38, fl: 34, bu: 36, bl: 36, paw: 14, tailA: 34, tailB: 28 };

  /* Pontos do esqueleto: f = para a frente, y = para baixo, s = lateral. */
  const JOINT = {
    frontNear: [72, 20, -30], frontFar: [72, 20, 30], backNear: [-76, 20, -38], backFar: [-76, 20, 38],
    neckBase: [68, -28, 0], head: [92, -50, 0], tail: [-106, -30, 0]
  };

  /* ---------- Matemática ---------- */
  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const smooth = t => t * t * (3 - 2 * t);
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const f = n => Math.round(n * 10) / 10;
  const RAD = Math.PI / 180, TAU = Math.PI * 2;
  /* Curva que passa por três chaves: frente (u=0), 3/4 (u=0.5) e perfil (u=1). */
  const key3 = (a, b, c, u) => a * (1 - 2 * u) * (1 - u) + 4 * b * u * (1 - u) + c * u * (2 * u - 1);
  const lerpDict = (a, b, t) => {
    const o = {};
    for (const k in a) o[k] = lerp(a[k], b[k], t);
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
  function capsule(len, r0, r1) {
    return 'M' + f(-r0) + ' 0A' + f(r0) + ' ' + f(r0) + ' 0 0 1 ' + f(r0) + ' 0L' + f(r1) + ' ' + f(len) +
      'A' + f(r1) + ' ' + f(r1) + ' 0 0 1 ' + f(-r1) + ' ' + f(len) + 'Z';
  }

  /* ---------- Formas: frente, 3/4 e perfil com os mesmos pontos ---------- */
  const SHAPE = {
    body: {
      front: [[-60, 0], [-56, -40], [-34, -58], [0, -62], [34, -58], [56, -40], [60, 0], [56, 36], [30, 52], [0, 54], [-30, 52], [-56, 36]],
      q: [[-92, -6], [-84, -42], [-46, -56], [2, -58], [44, -58], [76, -42], [84, -4], [74, 32], [40, 50], [-6, 50], [-54, 50], [-84, 32]],
      side: [[-112, -10], [-100, -44], [-50, -56], [10, -54], [64, -58], [102, -44], [112, -6], [100, 30], [56, 46], [-4, 44], [-64, 48], [-104, 30]]
    },
    chest: {
      front: [[0, -30], [24, -24], [34, 0], [22, 34], [0, 44], [-22, 34], [-34, 0], [-24, -24]],
      q: [[44, -22], [66, -12], [74, 12], [64, 34], [44, 42], [28, 30], [24, 8], [30, -12]],
      side: [[88, -26], [106, -10], [106, 16], [90, 34], [64, 38], [54, 22], [62, 0], [74, -16]]
    },
    head: {
      front: [[0, 6], [36, 0], [60, -26], [66, -60], [56, -94], [30, -112], [0, -116], [-30, -112], [-56, -94], [-66, -60], [-60, -26], [-36, 0]],
      q: [[6, 8], [40, 2], [64, -26], [70, -60], [58, -94], [32, -113], [-2, -117], [-34, -111], [-58, -90], [-64, -54], [-54, -22], [-26, 2]],
      side: [[14, 10], [44, 2], [66, -26], [72, -60], [60, -94], [32, -114], [-2, -118], [-36, -110], [-56, -86], [-60, -50], [-46, -18], [-18, 4]]
    },
    muzzle: {
      front: [[-40, -34], [-34, -56], [-14, -66], [14, -66], [34, -56], [40, -34], [34, -18], [14, -10], [-14, -10], [-34, -18]],
      q: [[-2, -30], [8, -52], [32, -62], [58, -62], [76, -54], [82, -36], [76, -22], [58, -14], [30, -12], [6, -20]],
      side: [[22, -30], [34, -58], [60, -68], [86, -68], [104, -58], [110, -40], [104, -24], [84, -16], [56, -14], [34, -18]]
    },
    jaw: {
      front: [[-24, -18], [24, -18], [28, -4], [12, 10], [-12, 10], [-28, -4]],
      q: [[14, -20], [62, -22], [70, -10], [56, 0], [30, 0], [14, -8]],
      side: [[40, -22], [92, -24], [100, -14], [88, -4], [60, -2], [44, -10]]
    },
    ear: {
      front: [[-12, -4], [14, -4], [26, 24], [24, 56], [6, 78], [-16, 66], [-24, 30]],
      q: [[-12, -4], [14, -4], [26, 24], [24, 56], [6, 78], [-16, 66], [-24, 30]],
      side: [[-14, -4], [14, -6], [28, 22], [26, 56], [6, 80], [-18, 66], [-26, 30]]
    },
    paw: {
      front: [[-19, -8], [19, -8], [24, 6], [14, 14, 1], [-14, 14, 1], [-24, 6]],
      q: [[-17, -8], [22, -8], [32, 6], [24, 14, 1], [-15, 14, 1], [-20, 6]],
      side: [[-17, -8], [24, -8], [38, 6], [30, 14, 1], [-15, 14, 1], [-20, 6]]
    },
    bodyShade: {
      front: [[40, 44], [56, 34], [60, 0], [56, -34], [48, 0], [44, 26], [30, 44], [32, 46]],
      side: [[-70, 44], [-20, 40], [50, 42], [96, 30], [50, 30], [-16, 28], [-72, 34], [-92, 34]]
    }
  };
  function shape(name, t) {
    const S = SHAPE[name];
    if (!S.q) return S.front.map((p, i) => [lerp(p[0], S.side[i][0], t), lerp(p[1], S.side[i][1], t), p[2]]);
    return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
  }

  /* ---------- Expressões ---------- */
  const EXPRESSION_BASE = {
    browY: 0, browTilt: 0, browSkew: 0, eyeOpen: 0.92, eyeLow: 0.95, lidTilt: 0, pupil: 1, exGx: 0, exGy: 0,
    ear: 0, mouthOpen: 0, smile: 0.35, tongue: 0, fangs: 0, sweat: 0, tear: 0, drool: 0, tilt: 0, headDrop: 0, tailMood: 0
  };
  const EXPRESSIONS = {
    neutral: {},
    happy: { browY: -5, eyeOpen: 0.86, eyeLow: 0.62, ear: 8, mouthOpen: 14, smile: 1, tongue: 0.55, tailMood: 14 },
    excited: { browY: -12, eyeOpen: 1.16, eyeLow: 1.02, pupil: 1.16, ear: 22, mouthOpen: 20, smile: 1, tongue: 0.75, tailMood: 26 },
    curious: { browY: -9, browTilt: 4, browSkew: 6, eyeOpen: 1.04, pupil: 1.12, exGy: -0.2, ear: 14, smile: 0.2, tilt: 10, tailMood: 8 },
    confused: { browY: -3, browTilt: 7, browSkew: -11, eyeOpen: 0.94, ear: -4, smile: -0.2, mouthOpen: 3, exGx: -0.3, tilt: -9 },
    shocked: { browY: -15, browTilt: 4, eyeOpen: 1.3, eyeLow: 1.18, pupil: 0.6, ear: 30, mouthOpen: 24, smile: 0, tailMood: 20 },
    scared: { browY: -9, browTilt: 13, eyeOpen: 1.24, eyeLow: 1.1, pupil: 0.54, ear: -22, mouthOpen: 8, smile: -0.5, fangs: 0.6, sweat: 0.9, headDrop: 8, tailMood: -70 },
    sad: { browY: -2, browTilt: 13, eyeOpen: 0.72, lidTilt: -0.42, exGy: 0.5, ear: -20, smile: -0.7, tear: 1, headDrop: 8, tailMood: -44 },
    angry: { browY: 9, browTilt: -14, eyeOpen: 0.78, lidTilt: 0.5, pupil: 0.8, ear: -14, mouthOpen: 9, smile: -0.5, fangs: 1, tailMood: 10 },
    sleepy: { browY: 2, browTilt: 5, eyeOpen: 0.3, eyeLow: 0.8, lidTilt: -0.1, exGy: 0.4, ear: -8, smile: 0.05, tilt: 6, headDrop: 6, tailMood: -20 },
    hungry: { browY: -9, browTilt: 8, eyeOpen: 1.1, pupil: 1.26, exGy: 0.3, ear: 10, mouthOpen: 7, smile: 0.6, tongue: 0.4, drool: 1, tilt: 4, tailMood: 18 },
    suspicious: { browY: 5, browTilt: -6, browSkew: 8, eyeOpen: 0.56, lidTilt: 0.26, exGx: 0.75, ear: -6, smile: -0.1, tilt: -5, tailMood: -8 },
    guilty: { browY: -4, browTilt: 12, eyeOpen: 0.82, lidTilt: -0.3, exGx: -0.8, exGy: 0.45, ear: -26, smile: -0.25, sweat: 0.5, tilt: -6, headDrop: 12, tailMood: -66 }
  };
  Object.keys(EXPRESSIONS).forEach(k => { EXPRESSIONS[k] = Object.assign({}, EXPRESSION_BASE, EXPRESSIONS[k]); });

  /* ---------- Poses ----------
     Ângulos em graus no plano lateral do cachorro, medidos no mundo: 0 = para baixo,
     negativo = para a frente. u = ombro/quadril, l = segmento inferior.
     fn/ff = dianteira próxima/distante, bn/bf = traseira próxima/distante.
     pitch = corpo erguido (nariz para cima). lift = altura acima do apoio.
     plant = 1 apoia a pata mais baixa no chão. frontLen estica a dianteira ao sentar. */
  const POSE_BASE = {
    lift: 0, rootF: 0, pitch: 0, spin: 0, squash: 1, head: 0, headF: 0, headY: 0, roll: 0,
    fnu: 0, fnl: 0, ffu: 4, ffl: 4, bnu: -10, bnl: 18, bfu: -14, bfl: 14, frontLen: 1,
    tailA: 135, tailB: -40, ear: 0, gx: 0, gy: 0, plant: 1, shut: 0, ball: 0, bite: 0, pawOver: 0, belly: 0
  };
  const SIT = { pitch: 24, frontLen: 1.25, fnu: -2, fnl: -2, ffu: 3, ffl: 3, bnu: -82, bnl: 122, bfu: -76, bfl: 116, tailA: 96, tailB: -24, head: -8, headY: -6 };
  const LIE = { fnu: -78, fnl: -90, ffu: -72, ffl: -88, bnu: -82, bnl: 100, bfu: -76, bfl: 96, squash: 0.92, headF: 8, headY: 14, tailA: 100, tailB: -20 };
  const pose = o => Object.assign({}, POSE_BASE, o);
  const POSES = {
    idle: pose({ head: -3, gy: 0 }),
    standing: pose({ tailA: 142, tailB: -44 }),
    sitting: pose(SIT),
    lying_down: pose(LIE),
    sleeping: pose(Object.assign({}, LIE, { head: 22, headF: 16, headY: 40, ear: -8, shut: 1, tailA: 78, tailB: -10 })),
    running: pose({ pitch: 2, head: 6, headF: 6, tailA: 118, tailB: -20, ear: -14, plant: 0 }),
    walking: pose({ head: -2 }),
    jumping: pose({ pitch: 14, head: -8, fnu: -52, fnl: -18, ffu: -44, ffl: -12, bnu: 40, bnl: 66, bfu: 34, bfl: 60, tailA: 150, tailB: -30, ear: 18, plant: 0, lift: -96 }),
    begging: pose({ pitch: 60, frontLen: 1, fnu: -64, fnl: -150, ffu: -58, ffl: -144, bnu: -84, bnl: 118, bfu: -78, bfl: 112, tailA: 60, tailB: -8, head: -40, headF: -4, headY: 8, gy: -0.5 }),
    playing: pose({ pitch: -20, fnu: -62, fnl: -72, ffu: -56, ffl: -66, bnu: -6, bnl: 14, bfu: -12, bfl: 10, head: 14, headF: 8, headY: 6, tailA: 160, tailB: -24, ear: 10, ball: 1, gy: 0.2 }),
    sniffing: pose({ pitch: -7, head: 34, headF: 26, headY: 62, fnu: -8, fnl: -8, ffu: 4, ffl: 4, gy: 0.7, ear: -4, tailA: 130 }),
    barking: pose({ pitch: 5, head: -12, fnu: -6, fnl: -6, ffu: 2, ffl: 2, bnu: -2, bnl: 14, ear: 8, tailA: 150, bite: 1 }),
    looking_up: pose(Object.assign({}, SIT, { head: -42, headF: -6, headY: 2, gy: -0.8, ear: -6 })),
    head_tilt: pose(Object.assign({}, SIT, { roll: 15, ear: 12, gy: -0.1 })),
    rolling: pose({ belly: 1, fnu: 158, fnl: 196, ffu: 166, ffl: 204, bnu: 196, bnl: 150, bfu: 188, bfl: 142, tailA: 72, tailB: -14, roll: -90, headY: -100, headF: 6, ear: 10, lift: -14 }),
    hiding: pose(Object.assign({}, LIE, { fnu: -120, fnl: -140, head: 24, headF: 4, headY: 34, ear: -22, tailA: 76, tailB: -8, gy: 0.3, pawOver: 1 }))
  };

  /* Ciclos próprios das poses. rate em rad/s; still = fase usada sem animação. */
  const POSE_MOTION = {
    walking: {
      rate: 7, still: 0.9,
      run(j, ph) {
        const leg = (a, k) => { const s = Math.sin(a); return [-26 * s + k, -26 * s + k + 24 * Math.max(0, Math.cos(a))]; };
        [j.fnu, j.fnl] = leg(ph, 0); [j.ffu, j.ffl] = leg(ph + Math.PI, 0);
        const b = (a) => { const s = Math.sin(a); return [-26 * s - 10, -26 * s + 18 + 10 * Math.max(0, -Math.cos(a))]; };
        [j.bnu, j.bnl] = b(ph + Math.PI * 1.5); [j.bfu, j.bfl] = b(ph + Math.PI * 0.5);
        j.head += 2 * Math.sin(ph * 2); j.tailA += 10 * Math.sin(ph * 2); j.pitch += Math.sin(ph * 2);
      }
    },
    running: {
      rate: 15, still: 0.6,
      run(j, ph) {
        const fore = a => { const s = Math.sin(a); return [-54 * s - 4, -54 * s - 4 + 34 * Math.max(0, Math.cos(a))]; };
        const hind = a => { const s = Math.sin(a); return [-54 * s - 8, -54 * s + 14 + 22 * Math.max(0, -Math.cos(a))]; };
        [j.fnu, j.fnl] = fore(ph); [j.ffu, j.ffl] = fore(ph + 0.5);
        [j.bnu, j.bnl] = hind(ph + 2.6); [j.bfu, j.bfl] = hind(ph + 3.1);
        j.pitch += 7 * Math.sin(ph + 0.8);
        j.lift = -22 * Math.abs(Math.sin(ph * 0.5 + 0.4));
        j.head += 3 * Math.cos(ph + 0.8); j.tailA += 12 * Math.sin(ph);
      }
    },
    jumping: {
      rate: 5, still: 1.57,
      run(j, ph, still) {
        const hop = Math.abs(Math.sin(ph));
        j.lift = -96 * hop;
        const land = 1 - hop;
        j.fnu = lerp(j.fnu, 0, land); j.fnl = lerp(j.fnl, 0, land); j.ffu = lerp(j.ffu, 4, land); j.ffl = lerp(j.ffl, 4, land);
        j.bnu = lerp(j.bnu, -10, land); j.bnl = lerp(j.bnl, 18, land); j.bfu = lerp(j.bfu, -14, land); j.bfl = lerp(j.bfl, 14, land);
        j.pitch *= hop; void still;
      }
    },
    begging: {
      rate: 6, still: 0,
      run(j, ph) { j.fnu += 7 * Math.sin(ph); j.ffu += 7 * Math.sin(ph + 0.4); j.fnl += 10 * Math.sin(ph); j.ffl += 10 * Math.sin(ph + 0.4); j.head += 1.5 * Math.sin(ph * 0.5); }
    },
    playing: {
      rate: 7, still: 0,
      run(j, ph) { j.tailA += 16 * Math.sin(ph * 1.6); j.rootF += 5 * Math.sin(ph); j.pitch += 1.6 * Math.sin(ph); j.head += 3 * Math.sin(ph); }
    },
    sniffing: {
      rate: 9, still: 0,
      run(j, ph) { j.head += 2.4 * Math.sin(ph * 1.4); j.headF += 8 * Math.sin(ph * 0.3); j.headY += 2 * Math.sin(ph); }
    },
    rolling: {
      rate: 7, still: 0,
      run(j, ph) { j.spin = 9 * Math.sin(ph); j.fnu += 18 * Math.sin(ph * 2); j.ffu -= 18 * Math.sin(ph * 2); j.fnl += 18 * Math.sin(ph * 2); j.ffl -= 18 * Math.sin(ph * 2); j.bnu += 16 * Math.cos(ph * 2); j.bfu -= 16 * Math.cos(ph * 2); j.bnl += 16 * Math.cos(ph * 2); j.bfl -= 16 * Math.cos(ph * 2); j.roll += 6 * Math.sin(ph); }
    },
    hiding: {
      rate: 40, still: 0,
      run(j, ph) { j.tailA += 1.6 * Math.sin(ph); j.head += 0.5 * Math.sin(ph * 0.9); }
    }
  };

  class Mixer {
    constructor(name) { this.layers = [{ name, p: 1, dur: 0 }]; }
    get name() { return this.layers[this.layers.length - 1].name; }
    to(name, dur) {
      if (dur <= 0) { this.layers = [{ name, p: 1, dur: 0 }]; return; }
      this.layers.push({ name, p: 0, dur });
    }
    update(dt) {
      this.layers.forEach(l => { if (l.p < 1) l.p = clamp(l.p + dt / l.dur); });
      let last = 0;
      this.layers.forEach((l, i) => { if (l.p >= 1) last = i; });
      if (last) this.layers = this.layers.slice(last);
    }
    sample(get) {
      let out = get(this.layers[0].name);
      for (let i = 1; i < this.layers.length; i++) out = lerpDict(out, get(this.layers[i].name), ease(this.layers[i].p));
      return out;
    }
  }

  const ANIMATIONS = ['none', 'idle', 'tail_wag', 'bark', 'pant', 'sleep', 'ear_flap', 'head_shake', 'tremble'];
  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const ACCESSORIES = ['collar', 'bone', 'bowl', 'ball', 'shadow'];
  const ANIMATE = {
    idle(j, t, w) {
      j.head += 1.8 * Math.sin(t * 0.8) * w;
      j.tailA += 5 * Math.sin(t * 2.2) * w;
      j.ear += 1.5 * Math.sin(t * 0.6) * w;
    },
    tail_wag(j, t, w) { j.wag += 24 * Math.sin(t * 15) * w; j.tailA += 20 * Math.sin(t * 15) * w; j.tailB += 10 * Math.sin(t * 15 - 1) * w; },
    ear_flap(j, t, w) { j.earN += 14 * Math.sin(t * 13) * w; j.earF += 14 * Math.sin(t * 13 + 1.6) * w; },
    head_shake(j, t, w) { j.roll += 12 * Math.sin(t * 16) * w; j.earN += 12 * Math.sin(t * 16 - 1) * w; j.earF -= 12 * Math.sin(t * 16 - 1) * w; },
    tremble(j, t, w) { j.quiver += w; j.head += 0.9 * Math.cos(t * 37) * w; j.tailA += 2 * Math.sin(t * 42) * w; },
    sleep(j, t, w) { j.shut = Math.max(j.shut, w); j.ear -= 4 * w; }
  };

  /* ---------- DOM ---------- */
  const NS = 'http://www.w3.org/2000/svg';
  let instanceCount = 0;
  function put(el, key, val) {
    const cache = el.__c || (el.__c = {});
    if (cache[key] !== val) { cache[key] = val; el.setAttribute(key, val); }
  }
  const tf = (x, y, r, sx, sy) => 'translate(' + f(x) + ' ' + f(y) + ')' + (r ? ' rotate(' + f(r) + ')' : '') +
    (sx !== undefined ? ' scale(' + (Math.round(sx * 1000) / 1000) + ' ' + (Math.round((sy === undefined ? sx : sy) * 1000) / 1000) + ')' : '');
  const shown = (el, op) => {
    put(el, 'display', op > 0.01 ? 'inline' : 'none');
    put(el, 'opacity', String(Math.round(op * 100) / 100));
  };
  const outlineStyle = { fill: C.ink, stroke: C.ink, 'stroke-width': LINE * 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };
  const lineStyle = { stroke: C.ink, 'stroke-width': LINE, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };

  class BiscuitRivera {
    constructor(target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: 'standing', animation: 'idle', direction: 'right', seed: 23, autoStart: true }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('BiscuitRivera: elemento de destino não encontrado.');
      instanceCount += 1;
      this.prefix = opt.idPrefix || (instanceCount === 1 ? 'biscuit' : 'biscuit' + instanceCount);
      this.random = rng(opt.seed);
      this.time = 0;
      this.turn = this._dir(opt.direction);
      this.turnFrom = this.turn; this.turnTo = this.turn; this.turnP = 1; this.turnDur = 1;
      this.poseMix = new Mixer(this._check(opt.pose, POSES, 'Pose'));
      this.exprMix = new Mixer(this._check(opt.expression, EXPRESSIONS, 'Expressão'));
      this.anims = [{ name: this._anim(opt.animation), w: 1 }];
      this.breathing = true; this.blinking = true;
      this.look = null; this.gaze = { x: 0, y: 0, tx: 0, ty: 0, next: 1.5 };
      this.nextBlink = 1.2; this.blinkT = -1;
      this.accessories = { collar: true, bone: false, bowl: false, ball: 'auto', shadow: true };
      this.visible = true; this.alpha = 1;
      this.earSwing = 0; this.earVel = 0;
      this._build();
      this.tick(0);
      this._raf = null;
      if (opt.autoStart) this.play();
    }

    /* ---------- API pública ---------- */
    setExpression(name, o) { this.exprMix.to(this._check(name, EXPRESSIONS, 'Expressão'), this._ms(o, 260)); return this._after(); }
    setPose(name, o) { this.poseMix.to(this._check(name, POSES, 'Pose'), this._ms(o, 480)); return this._after(); }
    setAnimation(name, o) {
      this._anim(name);
      const dur = this._ms(o, 300);
      if (dur <= 0) this.anims = [{ name, w: 1 }];
      else if (this.animation !== name) this.anims.push({ name, w: 0, dur });
      return this._after();
    }
    setDirection(dir, o) { return this.setTurn(this._dir(dir), o); }
    /* Giro contínuo: -1 perfil esquerdo, 0 frente, 1 perfil direito. */
    setTurn(value, o) {
      const dur = this._ms(o, 420);
      this.turnTo = clamp(value, -1, 1);
      if (dur <= 0) { this.turn = this.turnTo; this.turnP = 1; }
      else { this.turnFrom = this.turn; this.turnP = 0; this.turnDur = dur; }
      return this._after();
    }
    setVisible(on, o) {
      this.visible = !!on;
      if (this._ms(o, 200) <= 0) this.alpha = on ? 1 : 0;
      return this._after();
    }
    setBreathing(on) { this.breathing = !!on; return this; }
    setBlinking(on) { this.blinking = !!on; return this; }
    /* Direção do olhar de -1 a 1; sem argumentos, volta ao olhar automático. */
    lookAt(x, y) { this.look = x === undefined ? null : { x: clamp(x, -1, 1), y: clamp(y || 0, -1, 1) }; return this._after(); }
    blink() { this.blinkT = 0; return this; }
    setAccessory(name, on) {
      if (!ACCESSORIES.includes(name)) throw new Error('BiscuitRivera: acessório desconhecido "' + name + '". Use: ' + ACCESSORIES.join(', '));
      this.accessories[name] = on === 'auto' ? 'auto' : !!on;
      return this._after();
    }
    getState() {
      return {
        expression: this.exprMix.name, pose: this.poseMix.name, animation: this.animation,
        direction: Object.keys(DIRECTIONS).find(k => DIRECTIONS[k] === this.turnTo) || 'custom', turn: this.turnTo,
        visible: this.visible, accessories: Object.assign({}, this.accessories)
      };
    }
    get animation() { return this.anims[this.anims.length - 1].name; }
    play() {
      if (this._raf !== null) return this;
      let last = null;
      const loop = now => {
        if (last !== null) this.tick(Math.min(now - last, 50));
        last = now;
        this._raf = requestAnimationFrame(loop);
      };
      this._raf = requestAnimationFrame(loop);
      return this;
    }
    pause() {
      if (this._raf !== null) cancelAnimationFrame(this._raf);
      this._raf = null;
      return this;
    }
    toSVG() {
      const clone = this.svg.cloneNode(true);
      clone.setAttribute('xmlns', NS);
      clone.removeAttribute('class');
      return new XMLSerializer().serializeToString(clone);
    }
    destroy() { this.pause(); this.svg.remove(); }

    tick(dtMs) {
      const dt = dtMs / 1000;
      this.time += dt;
      this.poseMix.update(dtMs); this.exprMix.update(dtMs);
      if (this.turnP < 1) {
        this.turnP = clamp(this.turnP + dtMs / this.turnDur);
        this.turn = lerp(this.turnFrom, this.turnTo, ease(this.turnP));
      }
      const n = this.anims.length, dur = this.anims[n - 1].dur || 300;
      this.anims.forEach((a, i) => { a.w = clamp(a.w + (i === n - 1 ? 1 : -1) * dtMs / dur); });
      if (n > 1 && this.anims[n - 1].w >= 1) this.anims = [this.anims[n - 1]];
      const target = this.visible ? 1 : 0;
      this.alpha += clamp(target - this.alpha, -dtMs / 200, dtMs / 200);
      this._render(this._blinkAmount(dt), dt);
      return this;
    }

    /* ---------- Internos ---------- */
    _check(name, table, label) {
      if (!table[name]) throw new Error('BiscuitRivera: ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (!ANIMATIONS.includes(name)) throw new Error('BiscuitRivera: animação desconhecida "' + name + '". Use: ' + ANIMATIONS.join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error('BiscuitRivera: direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
      return DIRECTIONS[dir];
    }
    _ms(o, fallback) { return o && o.duration !== undefined ? o.duration : fallback; }
    _after() { if (this._raf === null) this.tick(0); return this; }
    _blinkAmount(dt) {
      if (this.blinking && this.time >= this.nextBlink && this.blinkT < 0) {
        this.blinkT = 0;
        this.nextBlink = this.time + 1.8 + this.random() * 3.6;
      }
      if (this.blinkT < 0) return 0;
      this.blinkT += dt;
      const p = this.blinkT / 0.16;
      if (p >= 1) { this.blinkT = -1; return 0; }
      return Math.sin(p * Math.PI);
    }
    _gaze(dt, autoOn) {
      const g = this.gaze;
      if (this.look) { g.tx = this.look.x; g.ty = this.look.y; }
      else if (autoOn && this.time >= g.next) {
        const away = this.random() < 0.35;
        g.tx = away ? (this.random() - 0.5) * 0.9 : 0;
        g.ty = away ? (this.random() - 0.5) * 0.4 : 0;
        g.next = this.time + 1.4 + this.random() * 2.8;
      } else if (!autoOn) { g.tx = 0; g.ty = 0; }
      const k = clamp(dt * 18);
      g.x = lerp(g.x, g.tx, k); g.y = lerp(g.y, g.ty, k);
    }
    _sampleJoints() {
      const live = this.animation !== 'none';
      const get = name => {
        const j = Object.assign({ wag: 0, earN: 0, earF: 0, quiver: 0 }, POSES[name]);
        const m = POSE_MOTION[name];
        if (m) m.run(j, live ? this.time * m.rate : m.still, !live);
        return j;
      };
      const j = this.poseMix.sample(get);
      this.anims.forEach(a => { if (ANIMATE[a.name]) ANIMATE[a.name](j, this.time, a.w); });
      return j;
    }
    _barkAmount(j) {
      if (this.animation === 'none') return { open: j.bite * 18, recoil: 0 };
      const w = this.animation === 'bark' ? 1 : j.bite;
      if (w <= 0.01) return { open: 0, recoil: 0 };
      const ph = (this.time * 3.2) % 1;
      const pulse = ph < 0.3 ? Math.sin(ph / 0.3 * Math.PI) : (ph > 0.42 && ph < 0.62 ? Math.sin((ph - 0.42) / 0.2 * Math.PI) * 0.7 : 0);
      return { open: pulse * 24 * w, recoil: pulse * w };
    }

    /* ---------- Construção ---------- */
    _n(tag, attrs, parent, part, pivot) {
      const el = document.createElementNS(NS, tag);
      for (const k in attrs || {}) el.setAttribute(k, attrs[k]);
      if (part) { el.setAttribute('data-part', part); el.setAttribute('id', this.prefix + '-' + part); }
      if (pivot) el.setAttribute('data-pivot', pivot.join(','));
      if (parent) parent.appendChild(el);
      return el;
    }
    _build() {
      const n = this._n.bind(this), u = this.prefix;
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'biscuit-rig', role: 'img', 'aria-label': 'Biscuit', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = n('defs', {}, svg);
      this.clipEyeR = n('path', {}, n('clipPath', { id: u + '-clip-eye-right' }, defs));
      this.clipEyeL = n('path', {}, n('clipPath', { id: u + '-clip-eye-left' }, defs));

      this.scaler = n('g', { transform: 'translate(0 ' + FLOOR + ') scale(' + VIEW_SCALE + ') translate(0 ' + -FLOOR + ')' }, svg, 'scale');
      this.shadow = n('ellipse', { cx: 0, cy: FLOOR + 5, fill: '#000', 'fill-opacity': 0.22 }, this.scaler, 'shadow');
      this.flip = n('g', {}, this.scaler, 'character');
      this._buildProps(this.flip);

      const rig = this.rig = n('g', {}, this.flip, 'root');
      this.tailNode = this._buildTail(n('g', {}, rig, 'layer-tail'));
      this.layerBehind = n('g', {}, rig, 'layer-legs-behind');
      this.legBN = this._buildLeg('back', 'right', 'b', 'n');
      this.legBF = this._buildLeg('back', 'left', 'b', 'f');
      this.legFF = this._buildLeg('front', 'left', 'f', 'f');
      this.layerBehind.append(this.legBF.root, this.legBN.root, this.legFF.root);

      const trunk = n('g', {}, rig, 'layer-body');
      this.bodyO = n('path', Object.assign({}, outlineStyle), trunk);
      this.neckO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 76 + LINE * 2, 'stroke-linecap': 'round' }, trunk);
      this.body = n('path', { fill: C.fur }, trunk, 'body');
      this.neck = n('path', { fill: 'none', stroke: C.fur, 'stroke-width': 76, 'stroke-linecap': 'round' }, trunk, 'neck');
      this.bodyShade = n('path', { fill: C.furShade }, trunk, 'body-shade');
      this.chest = n('path', { fill: C.chest }, trunk, 'chest-patch');

      this.layerFront = n('g', {}, rig, 'layer-legs-front');
      this.legFN = this._buildLeg('front', 'right', 'f', 'n');
      this.layerFront.appendChild(this.legFN.root);

      this._buildCollar(n('g', {}, rig, 'layer-collar'));
      this._buildHead(n('g', {}, rig, 'layer-head'));
      this.layerTop = n('g', {}, rig, 'layer-paw-over');
      this.zzz = n('g', {}, rig, 'zzz');
      this.zNodes = [0, 1, 2].map(() => n('path', { d: 'M-9 -9H9L-9 9H9', fill: 'none', stroke: C.zzz, 'stroke-width': 6, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, this.zzz));
      this.legBNInFront = false; this.legFFInFront = false;
    }
    _buildLeg(kind, side, a, b) {
      const n = this._n.bind(this);
      const name = kind + '-paw-' + side;
      const root = n('g', {}, null, 'leg-' + kind + '-' + side, kind === 'front' ? JOINT.frontNear : JOINT.backNear);
      const leg = { root, upper: [], lower: [], paw: [], up: [], lo: [], key: a + b, kind, tone: [] };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const style = isO ? outlineStyle : { fill: C.fur };
        const g = n('g', {}, root);
        const upper = n('g', {}, g, isO ? null : 'leg-' + kind + '-' + side + '-upper');
        const up = n('path', Object.assign({}, style), upper);
        const lower = n('g', {}, upper, isO ? null : 'leg-' + kind + '-' + side + '-lower');
        const lo = n('path', Object.assign({}, style), lower);
        const paw = n('g', {}, lower, isO ? null : name);
        const p = n('path', Object.assign({}, style), paw);
        leg.upper.push(upper); leg.lower.push(lower); leg.paw.push(paw); leg.up.push(up); leg.lo.push(lo);
        (leg.pawPaths || (leg.pawPaths = [])).push(p);
        if (!isO) {
          leg.tone.push(up, lo, p);
          leg.toes = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 3, 'stroke-linecap': 'round' }, paw);
        }
      });
      return leg;
    }
    _buildTail(parent) {
      const n = this._n.bind(this);
      const t = { root: n('g', {}, parent, 'tail', JOINT.tail), a: [], b: [] };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const style = isO ? outlineStyle : { fill: C.fur };
        const g = n('g', {}, t.root);
        const a = n('g', {}, g, isO ? null : 'tail-base');
        n('path', Object.assign({ d: capsule(L.tailA, 13, 11) }, style), a);
        const b = n('g', {}, a, isO ? null : 'tail-tip');
        n('path', Object.assign({ d: capsule(L.tailB, 11, 6) }, style), b);
        t.a.push(a); t.b.push(b);
      });
      return t;
    }
    _buildCollar(parent) {
      const n = this._n.bind(this);
      const g = this.collarGroup = n('g', {}, parent, 'collar');
      this.collarO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 18 + LINE * 2, 'stroke-linecap': 'round' }, g);
      this.collarF = n('path', { fill: 'none', stroke: C.collar, 'stroke-width': 18, 'stroke-linecap': 'round' }, g, 'collar-band');
      this.collarLine = n('path', { fill: 'none', stroke: C.collarDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, g);
      const m = this.medal = n('g', {}, g, 'medal');
      n('circle', Object.assign({ cx: 0, cy: 12, r: 13, fill: C.medal }, lineStyle), m);
      n('circle', { cx: 0, cy: 12, r: 6.5, fill: 'none', stroke: C.medalDark, 'stroke-width': 3 }, m);
    }
    _buildEar(parent, part) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, part);
      const fill = n('path', Object.assign({ fill: C.ear }, lineStyle), g);
      const line = n('path', { fill: 'none', stroke: C.earShade, 'stroke-width': 7, 'stroke-linecap': 'round' }, g);
      return { g, fill, line };
    }
    _buildEye(parent, side, clipId) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'eye-' + side);
      const white = n('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3.5, 'stroke-linejoin': 'round' }, g);
      const iris = n('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
      const ball = n('g', {}, iris, 'pupil-' + side);
      n('circle', { r: 15, fill: C.iris }, ball);
      n('circle', { r: 10, fill: '#120d0a' }, ball);
      n('circle', { cx: 5, cy: -6, r: 4.6, fill: '#fff' }, ball);
      const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 6, 'stroke-linecap': 'round' }, g);
      return { g, white, iris, ball, lid };
    }
    _drop(parent) {
      return this._n('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
    }
    _buildHead(parent) {
      const n = this._n.bind(this);
      const head = this.head = n('g', {}, parent, 'head', JOINT.head);
      this.earBackLayer = n('g', {}, head);
      this.earF = this._buildEar(this.earBackLayer, 'ear-left');
      this.headShape = n('path', Object.assign({ fill: C.fur }, lineStyle), head, 'face');
      this.brows = n('g', {}, head);

      this.mouthDark = n('path', Object.assign({ fill: C.mouth }, lineStyle), head, 'mouth');
      this.jawGroup = n('g', {}, head, 'jaw');
      this.jaw = n('path', Object.assign({ fill: C.muzzleShade }, lineStyle), this.jawGroup);
      this.tongueIn = n('ellipse', { fill: C.tongue }, this.jawGroup);
      this.tongue = n('g', {}, this.jawGroup, 'tongue');
      this.tongueShape = n('path', Object.assign({ fill: C.tongue }, lineStyle, { 'stroke-width': 4 }), this.tongue);
      this.tongueLine = n('path', { fill: 'none', stroke: C.tongueLine, 'stroke-width': 3, 'stroke-linecap': 'round' }, this.tongue);
      this.bone = n('g', {}, this.jawGroup, 'bone');
      const boneD = 'M-40 -6C-46 -18 -60 -14 -56 -2C-62 2 -60 16 -46 12C-42 10 -40 8 -38 6H38C40 8 42 10 46 12C60 16 62 2 56 -2C60 -14 46 -18 40 -6Z';
      n('path', Object.assign({ d: boneD, fill: C.bone }, lineStyle), this.bone);
      n('path', { d: 'M-34 3H34', stroke: C.boneShade, 'stroke-width': 4, 'stroke-linecap': 'round', fill: 'none' }, this.bone);

      this.muzzle = n('path', Object.assign({ fill: C.muzzle }, lineStyle), head, 'muzzle');
      this.fangs = n('path', { fill: C.teeth, stroke: C.ink, 'stroke-width': 2.5, 'stroke-linejoin': 'round' }, head, 'fangs');
      this.mouthLine = n('path', Object.assign({ fill: 'none' }, lineStyle), head, 'mouth-line');
      this.nose = n('g', {}, head, 'nose');
      this.noseShape = n('path', Object.assign({ fill: C.nose }, lineStyle, { 'stroke-width': 3 }), this.nose);
      n('ellipse', { cx: -4, cy: -4, rx: 5, ry: 2.8, fill: C.noseShine }, this.nose);

      this.eyeR = this._buildEye(head, 'right', this.prefix + '-clip-eye-right');
      this.eyeL = this._buildEye(head, 'left', this.prefix + '-clip-eye-left');
      const browStyle = { fill: 'none', stroke: C.brow, 'stroke-width': 9, 'stroke-linecap': 'round' };
      this.browR = n('path', browStyle, head, 'brow-right');
      this.browL = n('path', browStyle, head, 'brow-left');
      this.earFrontLayer = n('g', {}, head);
      this.earN = this._buildEar(this.earFrontLayer, 'ear-right');
      this.sweat = n('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat); this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
      this.drool = this._drop(head);
    }
    _buildProps(parent) {
      const n = this._n.bind(this);
      const b = this.bowl = n('g', {}, parent, 'bowl');
      n('ellipse', Object.assign({ cx: 0, cy: -44, rx: 58, ry: 12, fill: C.food }, lineStyle), b);
      n('path', { d: 'M-34 -46l10 -4l10 5l10 -6l12 5l12 -4l10 4', fill: 'none', stroke: C.foodDark, 'stroke-width': 4, 'stroke-linecap': 'round' }, b);
      n('path', Object.assign({ d: 'M-66 -40Q-58 0 -46 0H46Q58 0 66 -40Q0 -22 -66 -40Z', fill: C.bowl }, lineStyle), b);
      n('path', { d: 'M-48 -10H48', stroke: C.bowlDark, 'stroke-width': 6, 'stroke-linecap': 'round', fill: 'none' }, b);
      const ball = this.ball = n('g', {}, parent, 'ball');
      n('circle', Object.assign({ cx: 0, cy: -26, r: 26, fill: C.ball }, lineStyle), ball);
      n('path', { d: 'M-22 -40Q-2 -26 -22 -12M22 -40Q2 -26 22 -12', fill: 'none', stroke: C.ballLine, 'stroke-width': 4.5, 'stroke-linecap': 'round' }, ball);
    }

    /* ---------- Desenho de um quadro ---------- */
    _render(blink, dt) {
      const t = Math.abs(this.turn), st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const j = this._sampleJoints();
      const e = this.exprMix.sample(n => EXPRESSIONS[n]);
      this._gaze(dt, live);
      const bark = this._barkAmount(j);

      const yaw = st * Math.PI / 2, si = Math.sin(yaw), co = Math.cos(yaw);
      const P = j.pitch * RAD, cp = Math.cos(P), sp = Math.sin(P);
      const breath = this.breathing ? Math.sin(this.time * TAU / (j.shut > 0.5 ? 4.6 : 2.6)) : 0;

      /* esqueleto 3D girado pelo pitch e projetado para a tela */
      const J = (name) => {
        const [fw, y, s] = JOINT[name];
        const yb = y * lerp(1, -1, j.belly);
        return { f: fw * cp + yb * sp, y: yb * cp - fw * sp, s };
      };
      const X = p => p.f * si + p.s * co;
      const seg = (angle, len, lateral) => {
        const a = angle * RAD;
        const dx = -Math.sin(a) * len * si + (lateral || 0) * co, dy = Math.cos(a) * len;
        const screen = Math.max(Math.hypot(dx, dy), len * 0.22);
        return { theta: Math.atan2(-dx, dy) / RAD, len: screen, dy };
      };

      /* apoio no chão */
      const lens = {
        fn: [L.fu * j.frontLen, L.fl * j.frontLen], ff: [L.fu * j.frontLen, L.fl * j.frontLen],
        bn: [L.bu, L.bl], bf: [L.bu, L.bl]
      };
      const anchors = { fn: J('frontNear'), ff: J('frontFar'), bn: J('backNear'), bf: J('backFar') };
      const reach = k => anchors[k].y + Math.cos(j[k + 'u'] * RAD) * lens[k][0] + Math.cos(j[k + 'l'] * RAD) * lens[k][1] + L.paw;
      /* o corpo inclinado também encosta no chão: o pitch leva a traseira para baixo */
      const rump = 112 * Math.abs(sp) + 46 * cp * j.squash;
      const lowest = Math.max(reach('fn'), reach('ff'), reach('bn'), reach('bf'), rump);
      const base = FLOOR - lerp(106, lowest, j.plant) + j.lift;
      const quiver = j.quiver * 1.8 * Math.sin(this.time * 42);

      put(this.svg, 'opacity', String(Math.round(this.alpha * 100) / 100));
      put(this.svg, 'display', this.alpha <= 0.001 ? 'none' : 'inline');
      put(this.flip, 'transform', 'scale(' + sign + ' 1)');
      const centerX = key3(0, -16, -26, st) + j.rootF * si + quiver;
      put(this.rig, 'transform', tf(centerX, base, j.spin));

      /* corpo */
      const bodyAngle = -j.pitch * si;
      const raise = 1 + Math.abs(sp) * 0.5 * (1 - st);
      const bodyT = tf(0, 0, bodyAngle, 1 + breath * 0.012, (1 + breath * 0.022) * raise * j.squash * lerp(1, -1, j.belly));
      [this.bodyO, this.body, this.bodyShade, this.chest].forEach(el => put(el, 'transform', bodyT));
      const bodyD = spline(shape('body', st), true);
      put(this.bodyO, 'd', bodyD); put(this.body, 'd', bodyD);
      put(this.bodyShade, 'd', spline(shape('bodyShade', st < 0.5 ? 0 : 1), true));
      shown(this.bodyShade, Math.abs(1 - 2 * st));
      put(this.chest, 'd', spline(shape('chest', st), true));

      const nb = J('neckBase'), hp = J('head');
      const hx = X(hp) + j.headF * si, hy = hp.y + j.headY + e.headDrop + bark.recoil * 5;
      const nx = X(nb), ny = nb.y;
      const neckD = 'M' + f(nx) + ' ' + f(ny) + 'L' + f(hx) + ' ' + f(hy - 18);
      put(this.neckO, 'd', neckD); put(this.neck, 'd', neckD);

      /* pernas */
      this._renderLeg(this.legFN, j, 'fn', anchors, lens, X, seg, st, 0, si);
      this._renderLeg(this.legFF, j, 'ff', anchors, lens, X, seg, st, 14, si);
      this._renderLeg(this.legBN, j, 'bn', anchors, lens, X, seg, st, 0, si);
      this._renderLeg(this.legBF, j, 'bf', anchors, lens, X, seg, st, 14, si);
      const bnFront = st > 0.35, ffFront = st < 0.6;
      if (bnFront !== this.legBNInFront) {
        (bnFront ? this.layerFront : this.layerBehind).insertBefore(this.legBN.root, bnFront ? this.layerFront.firstChild : this.layerBehind.firstChild);
        this.legBNInFront = bnFront;
      }
      if (ffFront !== this.legFFInFront) {
        if (!ffFront) this.layerBehind.appendChild(this.legFF.root);
        else if (this.legFN.root.parentNode === this.layerFront) this.layerFront.insertBefore(this.legFF.root, this.legFN.root);
        else this.layerFront.appendChild(this.legFF.root);
        this.legFFInFront = ffFront;
      }
      const pawTop = j.pawOver > 0.5 ? this.layerTop : this.layerFront;
      if (this.legFN.root.parentNode !== pawTop) pawTop.appendChild(this.legFN.root);
      const farTone = clamp((st - 0.5) * 2);
      [this.legFF, this.legBF].forEach(l => l.tone.forEach(p => put(p, 'fill', farTone > 0.5 ? C.furFar : C.fur)));

      /* cauda */
      const tp = J('tail');
      const mood = e.tailMood;
      const tailA = j.tailA + mood + breath * 1.5;
      const a = seg(tailA, L.tailA, j.wag);
      const b = seg(tailA + j.tailB, L.tailB, j.wag * 0.8);
      const tailT = tf(X(tp), tp.y, 0);
      put(this.tailNode.root, 'transform', tailT);
      const sa = a.len / L.tailA, sb = b.len / L.tailB;
      this.tailNode.a.forEach(g => put(g, 'transform', tf(0, 0, a.theta, 1, sa)));
      this.tailNode.b.forEach(g => put(g, 'transform', tf(0, L.tailA, b.theta - a.theta, 1, sb / Math.max(sa, 0.01))));

      /* coleira no meio do pescoço */
      const cx = lerp(nx, hx, 0.62), cy = lerp(ny, hy - 18, 0.62);
      const dx = hx - nx, dy = hy - 18 - ny, dl = Math.max(Math.hypot(dx, dy), 1);
      const ux = dx / dl, uy = dy / dl, w = 41;
      const p0 = [cx - uy * w, cy + ux * w], p1 = [cx + uy * w, cy - ux * w];
      const bulge = key3(22, 20, 14, st);
      const mid = [cx - ux * bulge * 2, cy - uy * bulge * 2];
      const collarD = 'M' + f(p0[0]) + ' ' + f(p0[1]) + 'Q' + f(mid[0]) + ' ' + f(mid[1]) + ' ' + f(p1[0]) + ' ' + f(p1[1]);
      put(this.collarO, 'd', collarD); put(this.collarF, 'd', collarD); put(this.collarLine, 'd', collarD);
      const low = p0[1] > p1[1] ? p0 : p1;
      const medalX = lerp(cx - ux * bulge, low[0], key3(0, 0.45, 0.8, st)), medalY = lerp(cy - uy * bulge, low[1], key3(0, 0.45, 0.8, st));
      put(this.medal, 'transform', tf(medalX, medalY + 4, -j.spin));
      shown(this.collarGroup, this.accessories.collar ? 1 : 0);

      this._renderHead(j, e, st, blink, dt, hx, hy, bark);

      /* acessórios e sono */
      const a2 = this.accessories;
      shown(this.bowl, a2.bowl === true ? 1 : 0);
      put(this.bowl, 'transform', tf(key3(170, 210, 240, st), FLOOR + 2));
      const ballOn = a2.ball === 'auto' ? j.ball > 0.5 : a2.ball;
      shown(this.ball, ballOn ? 1 : 0);
      const roll = (live && j.ball > 0.5) ? 6 * Math.sin(this.time * 7) : 0;
      put(this.ball, 'transform', tf(key3(-120, 190, 230, st) + roll, FLOOR + 2));
      shown(this.shadow, a2.shadow ? 1 : 0);
      const air = clamp((FLOOR - lerp(106, lowest, 1) - base) / 120);
      put(this.shadow, 'rx', f(key3(84, 120, 150, st) * (1 - air * 0.5)));
      put(this.shadow, 'ry', f(14 * (1 - air * 0.3)));
      put(this.shadow, 'cx', f(centerX + key3(0, 10, 10, st)));

      const asleep = j.shut;
      shown(this.zzz, asleep > 0.5 && live ? 1 : 0);
      if (asleep > 0.5 && live) {
        this.zNodes.forEach((z, i) => {
          const u = (this.time * 0.45 + i / 3) % 1;
          put(z, 'transform', tf(hx + key3(40, 80, 100, st) + 34 * u + 8 * Math.sin(u * 7), hy - 110 - 90 * u, 0, 0.7 + u * 0.8));
          put(z, 'opacity', String(Math.round(Math.sin(u * Math.PI) * 100) / 100));
        });
      }
    }
    _renderLeg(leg, j, k, anchors, lens, X, seg, st, farShift, si) {
      const up = seg(j[k + 'u'], lens[k][0]), lo = seg(j[k + 'l'], lens[k][1]);
      const an = anchors[k];
      put(leg.root, 'transform', tf(X(an) + farShift * si, an.y));
      const uT = tf(0, 0, up.theta), lT = tf(0, up.len, lo.theta - up.theta), pT = tf(0, lo.len, -lo.theta);
      leg.upper.forEach(g => put(g, 'transform', uT));
      leg.lower.forEach(g => put(g, 'transform', lT));
      leg.paw.forEach(g => put(g, 'transform', pT));
      const big = leg.kind === 'back';
      const dU = capsule(up.len, big ? 33 : 21, big ? 18 : 17), dL = capsule(lo.len, big ? 17 : 16, 14);
      leg.up.forEach(p => put(p, 'd', dU));
      leg.lo.forEach(p => put(p, 'd', dL));
      const pd = spline(shape('paw', st), true);
      leg.pawPaths.forEach(p => put(p, 'd', pd));
      const tx = key3(0, 8, 16, st);
      put(leg.toes, 'd', 'M' + f(tx - 7) + ' 12V5M' + f(tx + 7) + ' 12V5');
    }
    _renderEye(eye, clip, x, y, sx, inner, e, shut, gx, gy) {
      put(eye.g, 'transform', tf(x, y, 0, sx, 1));
      const W = 21;
      const open = Math.max(0, e.eyeOpen * (1 - shut));
      const T = 25 * open * 1.33, B = 19 * e.eyeLow * (1 - shut * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    }
    _renderBrow(el, x, inner, e, sx, skew) {
      const y = -112 + e.browY - skew;
      const w = 16 * sx;
      const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
      put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY + 2) + 'Q' + f(x) + ' ' + f(y - 7 - e.browTilt * 0.1) + ' ' + f(x + w * inner) + ' ' + f(inY));
    }
    _renderEar(ear, st, angle, flop, x, y) {
      const pts = shape('ear', st).map(p => [p[0] + flop * Math.pow(Math.max(p[1], 0) / 78, 2), p[1], p[2]]);
      put(ear.fill, 'd', spline(pts, true));
      put(ear.line, 'd', 'M' + f(2 + flop * 0.04) + ' 18Q' + f(10 + flop * 0.3) + ' 42 ' + f(2 + flop * 0.7) + ' 62');
      put(ear.g, 'transform', tf(x, y, angle));
    }
    _renderHead(j, e, st, blink, dt, hx, hy, bark) {
      const shut = Math.max(blink, j.shut);
      const si = Math.sin(st * Math.PI / 2);
      put(this.head, 'transform', tf(hx, hy, j.head * si + j.roll + e.tilt));
      put(this.headShape, 'd', spline(shape('head', st), true));
      put(this.muzzle, 'd', spline(shape('muzzle', st), true));

      /* orelhas com mola: seguem o movimento da cabeça */
      const goal = clamp((j.head + j.roll + j.pitch * 0.4) * -0.5 + j.lift * 0.14 + bark.recoil * 10, -24, 24);
      for (let left = dt; left > 0; left -= 0.016) {
        const step = Math.min(left, 0.016);
        this.earVel += ((goal - this.earSwing) * 70 - this.earVel * 7) * step;
        this.earSwing += this.earVel * step;
      }
      const lift = e.ear + j.ear;
      const up = Math.max(lift, 0), down = Math.max(-lift, 0);   // orelha baixa cai para fora e desce
      const pose = up + down * 0.45;
      const nearA = key3(20, 14, 10, st) + pose + j.earN;
      const farSign = key3(-1, -1, 1, st);
      const farA = key3(0, 0, 8, st) + farSign * (key3(20, 16, 0, st) + pose) + j.earF;
      const sink = down * 0.55;
      this._renderEar(this.earN, st, nearA, this.earSwing, key3(-62, -44, -14, st), key3(-92, -98, -106, st) + sink);
      this._renderEar(this.earF, st, farA, this.earSwing, key3(62, 60, 34, st), key3(-92, -100, -110, st) + sink);
      const farBehind = st > 0.45;
      const wanted = farBehind ? this.earBackLayer : this.earFrontLayer;
      if (this.earF.g.parentNode !== wanted) wanted.appendChild(this.earF.g);

      /* boca */
      const open = Math.max(e.mouthOpen, bark.open, this.animation === 'pant' ? 12 + 4 * Math.sin(this.time * 14) : 0, this.accessories.bone === true ? 8 : 0);
      const jaw = spline(shape('jaw', st), true);
      put(this.jaw, 'd', jaw);
      const hingeX = key3(0, 16, 44, st), hingeY = -18;
      put(this.jawGroup, 'transform', 'translate(0 ' + f(open * 0.8 * (1 - st * 0.7)) + ') rotate(' + f(-open * 0.42 * -st) + ' ' + f(hingeX) + ' ' + hingeY + ')');
      put(this.mouthDark, 'd', spline(shape('jaw', st).map(p => [p[0], p[1] + Math.min(open, 26) * 0.5, p[2]]), true));
      shown(this.mouthDark, open > 1.5 ? 1 : 0);
      const tx = key3(0, 40, 68, st), ty = key3(-12, -14, -16, st);
      put(this.tongueIn, 'cx', f(tx)); put(this.tongueIn, 'cy', f(ty)); put(this.tongueIn, 'rx', f(key3(17, 24, 26, st))); put(this.tongueIn, 'ry', 7);
      shown(this.tongueIn, open > 3 ? 1 : 0);
      const pant = this.animation === 'pant' ? 1 : e.tongue;
      const len = 30 * pant * (1 + (this.animation === 'pant' ? 0.1 * Math.sin(this.time * 14) : 0));
      shown(this.tongue, len > 3 && this.accessories.bone !== true ? 1 : 0);
      put(this.tongue, 'transform', tf(key3(6, 50, 80, st), key3(2, 0, -2, st), key3(0, 6, 8, st)));
      put(this.tongueShape, 'd', capsule(Math.max(len, 1), 13, 12));
      put(this.tongueLine, 'd', 'M0 4V' + f(Math.max(len - 2, 5)));
      shown(this.bone, this.accessories.bone === true ? 1 : 0);
      put(this.bone, 'transform', tf(key3(0, 36, 62, st), -6, 0, key3(1, 0.9, 0.74, st), 1));

      /* linha da boca */
      const lx = key3(0, 36, 64, st), half = key3(30, 40, 42, st), smile = e.smile;
      const lineY = key3(-13, -16, -19, st);
      const c0 = lx - half, c1 = lx + half;
      const lift0 = -smile * 12, lift1 = st > 0.7 ? 0 : -smile * 12 * (1 - st);
      put(this.mouthLine, 'd', 'M' + f(c0 - 4) + ' ' + f(lineY + lift0) + 'Q' + f(lx) + ' ' + f(lineY + smile * 7 + 3) + ' ' + f(c1) + ' ' + f(lineY + lift1) +
        (st < 0.7 ? 'M' + f(key3(0, 50, 84, st)) + ' ' + f(key3(-42, -44, -44, st)) + 'V' + f(lineY + smile * 3 + 2) : ''));
      const fx = key3(-14, 22, 46, st), fw = key3(28, 30, 24, st);
      const fy = lineY + 2;
      put(this.fangs, 'd', 'M' + f(fx - 6) + ' ' + f(fy) + 'L' + f(fx) + ' ' + f(fy + 13) + 'L' + f(fx + 6) + ' ' + f(fy) + 'ZM' + f(fx + fw - 6) + ' ' + f(fy) + 'L' + f(fx + fw) + ' ' + f(fy + 13) + 'L' + f(fx + fw + 6) + ' ' + f(fy) + 'Z');
      shown(this.fangs, e.fangs > 0.3 ? 1 : 0);

      /* nariz */
      put(this.nose, 'transform', tf(key3(0, 64, 104, st), key3(-60, -50, -60, st), 0, key3(1.1, 1.1, 1, st), 1.1));
      put(this.noseShape, 'd', 'M-15 -6C-15 -14 15 -14 15 -6C15 4 6 11 0 11C-6 11 -15 4 -15 -6Z');

      /* olhos */
      const gx = clamp(j.gx + e.exGx + this.gaze.x, -1, 1), gy = clamp(j.gy + e.exGy + this.gaze.y, -1, 1);
      const rx = key3(-27, 8, 40, st), lx2 = key3(27, 52, 68, st), ey = -84;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.7, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, shut, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx2, ey, Math.max(ls, 0.06), -1, e, shut, gx, gy);
      this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx2, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw > 0.04 ? 1 : 0);
      put(this.sweat1, 'transform', tf(key3(-74, 78, 78, st), key3(-118, -112, -112, st), 12, 0.5 + sw * 0.5));
      put(this.sweat2, 'transform', tf(key3(78, 90, 92, st), key3(-112, -92, -92, st), -10, 0.38 + sw * 0.4));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -52 + (this.animation === 'none' ? 0.5 : fall) * 16, 0, 0.75));
      shown(this.drool, clamp(e.drool));
      put(this.drool, 'transform', tf(key3(22, 64, 92, st), -2 + (this.animation === 'none' ? 0.4 : (this.time * 0.9) % 1) * 22, 0, 0.72));
    }
  }

  BiscuitRivera.EXPRESSIONS = Object.keys(EXPRESSIONS);
  BiscuitRivera.POSES = Object.keys(POSES);
  BiscuitRivera.ANIMATIONS = ANIMATIONS.slice();
  BiscuitRivera.DIRECTIONS = Object.keys(DIRECTIONS);
  BiscuitRivera.ACCESSORIES = ACCESSORIES.slice();
  BiscuitRivera.JOINTS = JOINT;
  BiscuitRivera.PALETTE = C;
  return BiscuitRivera;
});
