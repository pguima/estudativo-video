/*!
 * DanRivera — personagem de produção do canal Survive the Headline.
 *
 * Um único modelo-base em SVG. Pose, expressão e direção são apenas números
 * aplicados ao mesmo esqueleto; nenhuma variação tem desenho próprio.
 *
 * Uso:
 *   const dan = new DanRivera('#palco');
 *   dan.setExpression('worried');
 *   dan.setPose('standing');
 *   dan.setAnimation('idle');
 *   dan.setDirection('left');
 *   dan.setVisible(true);
 *
 * Vídeo quadro a quadro (determinístico, sem requestAnimationFrame):
 *   const dan = new DanRivera(el, { autoStart: false, seed: 42 });
 *   dan.setPose('running', { duration: 0 });
 *   dan.tick(1000 / 30);          // avança um quadro
 *   const svg = dan.toSVG();      // SVG autônomo do quadro atual
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.DanRivera = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- Paleta travada: fonte única das cores do personagem ---------- */
  const C = {
    ink: '#1b1a22', skin: '#eab48e', skinShade: '#d6976f', stubble: '#e0ac88',
    hair: '#3b2a20', brow: '#2c1f18', eyeWhite: '#ffffff', iris: '#5a3a22',
    navy: '#20386b', navyShade: '#182a52', navyDark: '#14213f',
    jeans: '#3f74b5', jeansShade: '#315e98', jeansLight: '#6f9dd2',
    boot: '#7a4a26', bootShade: '#5f381b', sole: '#35200f', lace: '#d9b98a',
    mouth: '#5a1c22', tongue: '#d9636a', teeth: '#fbf7ee',
    sweat: '#8fd6ff', leather: '#8a5a2e', leatherDark: '#65401f', metal: '#b9c2cc',
    metalDark: '#7f8a96', tool: '#e0422f', toolAlt: '#f4b41a', wood: '#a5764a', woodDark: '#7d5533'
  };
  const LINE = 4.5;            // peso do contorno em todas as partes
  const VIEWBOX = '-425 -480 850 860';
  const FLOOR = 340;

  /* ---------- Medidas do esqueleto ---------- */
  const M = {
    shoulderY: -192, upperArm: 104, foreArm: 98, hipY: 10, thigh: 146, shin: 146,
    neckY: -226, headY: -256
  };

  /* Pontos de articulação de cada parte, em coordenadas do modelo. */
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-92, M.shoulderY], shoulderLeft: [92, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-38, M.hipY], hipLeft: [38, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  /* ---------- Matemática ---------- */
  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const smooth = t => t * t * (3 - 2 * t);
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const f = n => Math.round(n * 10) / 10;
  const TAU = Math.PI * 2;

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
  const morph = (a, b, t) => a.map((p, i) => [lerp(p[0], b[i][0], t), lerp(p[1], b[i][1], t), p[2]]);
  /* Curva que passa por três chaves: frente (u=0), 3/4 (u=0.5) e perfil (u=1). */
  const key3 = (a, b, c, u) => a * (1 - 2 * u) * (1 - u) + 4 * b * u * (1 - u) + c * u * (2 * u - 1);

  /* Cápsula afilada ao longo de +y, origem na articulação. */
  function capsule(len, r0, r1) {
    return 'M' + f(-r0) + ' 0A' + f(r0) + ' ' + f(r0) + ' 0 0 1 ' + f(r0) + ' 0L' + f(r1) + ' ' + f(len) +
      'A' + f(r1) + ' ' + f(r1) + ' 0 0 1 ' + f(-r1) + ' ' + f(len) + 'Z';
  }

  /* ---------- Formas: cada uma tem versão de frente e de lado com os mesmos pontos ---------- */
  const SHAPE = {
    head: {
      q: [[20, 8], [50, 3], [68, -18], [75, -58], [78, -100], [66, -140], [36, -162], [0, -169],
        [-40, -162], [-72, -136], [-83, -96], [-76, -54], [-56, -18], [-14, 6]],
      front: [[0, 8], [34, 5], [62, -16], [74, -58], [78, -100], [66, -140], [34, -162], [0, -168],
        [-34, -162], [-66, -140], [-78, -100], [-74, -58], [-62, -16], [-34, 5]],
      side: [[46, 8], [62, -2], [68, -24], [71, -60], [74, -100], [66, -136], [38, -162], [-4, -170],
        [-48, -160], [-80, -130], [-88, -90], [-76, -52], [-44, -20], [8, 0]]
    },
    headShade: {
      front: [[34, 5], [62, -16], [74, -58], [78, -100], [72, -100], [66, -60], [52, -22], [26, 0]],
      side: [[60, -1], [30, 3], [8, 0], [-30, -13], [-24, -26], [2, -14], [30, -11], [52, -12]]
    },
    stubble: {
      q: [[76, -52], [66, -14], [46, 6], [20, 10], [-16, 6], [-50, -12], [-68, -50], [-48, -52],
        [-26, -38], [6, -42], [20, -38], [38, -42], [52, -38], [66, -50]],
      front: [[74, -58], [62, -16], [34, 5], [0, 8], [-34, 5], [-62, -16], [-74, -58], [-56, -56],
        [-40, -40], [-16, -44], [0, -40], [16, -44], [40, -40], [56, -56]],
      side: [[71, -46], [68, -24], [62, -2], [46, 8], [8, 0], [-14, -10], [-34, -36], [-22, -50],
        [-8, -34], [12, -32], [26, -40], [40, -42], [52, -46], [62, -46]]
    },
    hair: {
      q: [[-80, -60, 1], [-93, -100], [-88, -142], [-64, -174], [-28, -190], [12, -194], [50, -184], [76, -160],
        [84, -132], [78, -100, 1], [70, -118], [66, -140, 1], [44, -152], [18, -155], [-4, -147, 1], [-22, -132],
        [-34, -112], [-38, -82, 1], [-60, -70]],
      front: [[-80, -84, 1], [-87, -118], [-81, -152], [-58, -178], [-22, -192], [18, -194], [54, -182], [81, -154],
        [87, -118], [80, -84, 1], [71, -108], [66, -138, 1], [42, -153], [12, -157], [-8, -150, 1], [-30, -157],
        [-58, -150], [-68, -136, 1], [-71, -106]],
      side: [[-66, -42, 1], [-96, -90], [-92, -134], [-66, -168], [-30, -187], [10, -192], [46, -183], [72, -162],
        [83, -146], [72, -139, 1], [52, -150], [32, -148, 1], [14, -132], [2, -108], [-4, -80, 1], [-15, -110],
        [-40, -114], [-50, -84, 1], [-60, -56]]
    },
    torso: {
      front: [[-38, -234], [-92, -218], [-104, -188], [-97, -120], [-86, -40], [-90, 30, 1], [-40, 36], [0, 38], [40, 36],
        [90, 30, 1], [86, -40], [97, -120], [104, -188], [92, -218], [38, -234], [0, -212]],
      side: [[-22, -236], [-58, -216], [-68, -180], [-68, -120], [-62, -40], [-64, 30, 1], [-30, 36], [0, 38], [34, 36],
        [68, 30, 1], [74, -40], [69, -120], [62, -180], [50, -216], [26, -236], [6, -218]]
    },
    torsoShade: {
      front: [[64, 34], [90, 30], [86, -40], [97, -120], [100, -160], [78, -130], [66, -60], [62, -10]],
      side: [[-40, 34], [-64, 30], [-62, -40], [-68, -120], [-66, -170], [-50, -130], [-44, -60], [-44, -10]]
    },
    hips: {
      front: [[-78, -8], [-80, 26], [-58, 48], [0, 52], [58, 48], [80, 26], [78, -8], [0, -12]],
      side: [[-60, -8], [-66, 24], [-44, 52], [-6, 56], [34, 50], [58, 26], [60, -8], [0, -12]]
    },
    boot: {
      front: [[-25, -8], [-26, 10], [-33, 24], [-32, 36, 1], [32, 36, 1], [33, 24], [26, 10], [25, -8]],
      side: [[-25, -8], [-27, 12], [-29, 24], [-29, 36, 1], [76, 36, 1], [80, 23], [52, 6], [25, -8]]
    },
    sole: {
      front: [[-33, 27, 1], [-34, 40, 1], [34, 40, 1], [33, 27, 1]],
      side: [[-30, 27, 1], [-30, 40, 1], [82, 40, 1], [80, 27, 1]]
    }
  };
  const shape = (name, t) => {
    const S = SHAPE[name];
    if (!S.q) return morph(S.front, S.side, t);
    return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
  };

  const lerpDict = (a, b, t) => {
    const o = {};
    for (const k in a) o[k] = lerp(a[k], b[k], t);
    return o;
  };

  /* ---------- Expressões: valores do rosto ---------- */
  const EXPRESSION_BASE = {
    browY: 0, browTilt: 0, browArch: 4, eyeOpen: 0.88, eyeLow: 0.92, lidTilt: 0, pupil: 1,
    mouthW: 26, mouthOpen: 0, smile: 0.15, teeth: 0, grit: 0, tongue: 0, skew: 0,
    tint: 0, sweat: 0, tear: 0, exGx: 0, exGy: 0
  };
  const EXPRESSIONS = {
    neutral: {},
    happy: { browY: -7, browArch: 7, eyeOpen: 0.86, eyeLow: 0.62, mouthW: 37, mouthOpen: 22, smile: 1, teeth: 1, tongue: 0.5, tint: 0.14 },
    worried: { browY: -7, browTilt: 12, eyeOpen: 1.08, lidTilt: -0.25, mouthW: 22, mouthOpen: 5, smile: -0.5, teeth: 0.7, sweat: 0.6, exGx: 0.3 },
    shocked: { browY: -16, browTilt: 4, browArch: 5, eyeOpen: 1.3, eyeLow: 1.2, pupil: 0.62, mouthW: 21, mouthOpen: 37, smile: 0, teeth: 0.35, tongue: 0.6 },
    scared: { browY: -11, browTilt: 14, eyeOpen: 1.32, eyeLow: 1.15, pupil: 0.52, mouthW: 35, mouthOpen: 21, smile: -0.55, teeth: 1, grit: 1, sweat: 1, tint: -0.7 },
    angry: { browY: 11, browTilt: -15, browArch: 1, eyeOpen: 0.8, lidTilt: 0.55, pupil: 0.8, mouthW: 33, mouthOpen: 15, smile: -0.6, teeth: 1, grit: 1, tint: 0.9 },
    sad: { browY: -2, browTilt: 14, eyeOpen: 0.66, lidTilt: -0.42, exGy: 0.5, mouthW: 22, smile: -0.75, tear: 1 },
    determined: { browY: 7, browTilt: -9, browArch: 2, eyeOpen: 0.9, lidTilt: 0.24, mouthW: 26, smile: 0.2, skew: 0.5 }
  };
  Object.keys(EXPRESSIONS).forEach(k => { EXPRESSIONS[k] = Object.assign({}, EXPRESSION_BASE, EXPRESSIONS[k]); });

  /* ---------- Poses: ângulos das articulações ----------
     Prefixo r = braço/perna da direita do personagem (esquerda do público de frente,
     lado próximo no perfil); l = o outro. u/f/h = ombro, cotovelo, punho.
     fl = comprimento visível do antebraço (perspectiva). t/s/foot = quadril, joelho, tornozelo. ty/sy = encurtamento em perspectiva.
     r0..r3 = dobra dos dedos, r4 = abertura do polegar. */
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
  const POSE_BASE = Object.assign({
    rootX: 0, rootY: 0, rootR: 0, spine: 0, shrug: 0, head: 0, headY: 0,
    ru: 7, rf: -9, rh: 0, rfl: 1, lu: -7, lf: 9, lh: 0, lfl: 1,
    rt: 3, rs: -3, rfoot: 0, rty: 1, rsy: 1, lt: -3, ls: 3, lfoot: 0, lty: 1, lsy: 1,
    gx: 0, gy: 0, plant: 0, farFront: 1, screwdriver: 0, pliers: 0, toolbox: 0, seat: 0
  }, hands('relaxed', 'relaxed'));
  const SIDE_BASE = { ru: 3, rf: -14, lu: -3, lf: -14, rt: -4, rs: 4, lt: 5, ls: 1 };

  const pose = (front, side, extra, quarter) => {
    const shared = extra || {};
    const out = {
      front: Object.assign({}, POSE_BASE, shared, front),
      side: Object.assign({}, POSE_BASE, SIDE_BASE, shared, side)
    };
    out.q = Object.assign(lerpDict(out.front, out.side, 0.5), quarter);
    return out;
  };

  const POSES = {
    standing: pose({}, {}, { farFront: 0 }),
    idle: pose(
      { rootX: 5, rootR: 0.6, spine: -1.6, head: 2, lu: -30, lf: 72, lh: 16, rt: 5, rs: -5, lt: -6, ls: 5 },
      { spine: -1.5, ru: 5, rf: -18, lu: -2, lf: -20 }, Object.assign(hands('relaxed', 'relaxed'), { farFront: 0 })),
    explaining: pose(
      { spine: 1, head: -3, ru: 20, rf: 92, rh: 10, lu: -13, lf: 62, lh: -8, gx: -0.25 },
      { spine: 2, head: 2, ru: -34, rf: -62, rh: -8, lu: -14, lf: -46, lh: -8 }, Object.assign(hands('open', 'open'), { farFront: 0 }),
      { spine: 1.5, head: 0, ru: 8, rf: -86, rh: -6, lu: -26, lf: -44, lh: -10, gx: 0.3 }),
    pointing: pose(
      { spine: -3, head: 7, lu: -84, lf: -6, lh: 0, ru: 30, rf: -78, rh: -12, gx: 0.8, gy: -0.1 },
      { spine: 2, head: -2, lu: -84, lf: -8, lh: -4, ru: 6, rf: -20, gx: 0.8 }, Object.assign(hands('relaxed', 'point'), { farFront: 0 })),
    hands_on_head: pose(
      { shrug: 1, head: 0, headY: 4, ru: 152, rf: 66, rh: 30, lu: -152, lf: -66, lh: -30, gy: -0.15 },
      { shrug: 1, headY: 4, spine: -2, ru: 210, rf: -44, rh: -30, lu: -138, lf: -58, lh: -30, gy: -0.15 },
      hands('open', 'open'),
      { ru: 150, rf: 70, rh: 30, lu: -148, lf: -64, lh: -30 }),
    arms_crossed: pose(
      { head: 1, ru: 0, rf: -96, rh: 4, lu: 0, lf: 84, lh: -4 },
      { ru: 4, rf: -100, rfl: 0.36, rh: 22, lu: -2, lf: -92, lfl: 0.34 }, {},
      { ru: 0, rf: -100, rfl: 0.95, lu: -2, lf: 88, lfl: 0.85 }),
    shrugging: pose(
      { shrug: 1, head: 4, ru: 8, rf: 86, rh: 24, lu: -8, lf: -86, lh: -24 },
      { shrug: 1, head: -4, ru: 8, rf: -80, rfl: 0.6, rh: -40, lu: -6, lf: -70, lfl: 0.7, lh: -40 }, Object.assign(hands('open', 'open'), { farFront: 0 }),
      { shrug: 1, ru: 6, rf: 78, rfl: 0.8, rh: 20, lu: -14, lf: -74, lfl: 0.9, lh: -20 }),
    running: pose(
      { spine: 2, ru: 32, rf: -110, lu: -32, lf: 110 },
      { spine: 9, head: -7, ru: 20, rf: -88, lu: -20, lf: -88 }, Object.assign(hands('fist', 'fist'), { farFront: 0 }),
      { spine: 7, head: -6, rf: -96, lf: -92 }),
    sitting: pose(
      { rootY: 118, plant: 1, ru: 16, rf: -46, rh: -6, lu: -16, lf: 46, lh: 6, rt: 14, rs: -14, lt: -14, ls: 14, rty: 0.2, lty: 0.2, seat: 1 },
      { rootX: -46, rootY: 141, plant: 1, spine: -2, ru: -14, rf: -52, lu: -24, lf: -44, rt: -88, rs: 88, lt: -82, ls: 84, rfoot: 0, lfoot: -2, seat: 1 },
      {}, { rootX: -26, ru: -10, rf: -50, lu: -12, lf: 6, lfl: 0.8, rt: -70, rs: 70, rty: 0.72, lt: -64, ls: 64, lty: 0.72 }),
    working: pose(
      { head: 0, headY: 7, gy: 0.75, ru: 24, rf: -104, rh: 6, lu: -24, lf: 104, lh: -6 },
      { spine: 5, head: 9, gy: 0.5, gx: 0.3, ru: -46, rf: -54, rh: -2, lu: -30, lf: -70, lh: -6 },
      Object.assign(hands('grip', 'grip'), { screwdriver: 1, pliers: 1, toolbox: 1 }),
      { spine: 3, head: 5, gx: 0.2, gy: 0.6, ru: -28, rf: -62, rh: -2, lu: -14, lf: -66, lh: -4 })
  };

  /* Movimento próprio da pose, ativo quando há animação. */
  const POSE_MOTION = {
    /* view: 0 frente, 0.5 três quartos, 1 perfil. */
    running(j, ph, view) {
      const s = Math.sin(ph), c = Math.cos(ph);
      if (view > 0) {
        const quarter = view < 1;
        const stride = quarter ? 0.8 : 1;
        const leg = a => [(-16 - 44 * Math.sin(a)) * stride, (44 + 52 * Math.max(0, Math.cos(a - 0.2))) * stride];
        const R = leg(ph), L = leg(ph + Math.PI);
        j.rt = R[0]; j.rs = R[1]; j.rfoot = -R[1] * 0.28;
        j.lt = L[0]; j.ls = L[1]; j.lfoot = -L[1] * 0.28;
        j.ru = quarter ? 12 + 34 * s : 40 * s;
        j.lu = quarter ? -8 - 34 * s : -40 * s;
        j.rootY = (quarter ? 16 : 26) - (quarter ? 22 : 26) * Math.abs(c);
      } else {
        const lr = Math.max(0, s), ll = Math.max(0, -s);
        j.rty = 1 - 0.62 * lr; j.lty = 1 - 0.62 * ll;
        j.rsy = 1 - 0.1 * lr; j.lsy = 1 - 0.1 * ll;
        j.rootY = 16 - 22 * Math.abs(c);
        j.rootR = 2 * s; j.spine += 2.5 * s; j.head -= 2 * s;
        j.ru += 6 * s; j.lu += 6 * s; j.rf += 18 * s; j.lf += 18 * s;
      }
    },
    working(j, ph) {
      j.rh += 15 * Math.sin(ph * 1.6);
      j.rf += 4 * Math.sin(ph * 1.6 + 0.7);
      j.lh += 4 * Math.sin(ph * 0.8);
      j.head += 1.2 * Math.sin(ph * 0.5);
    }
  };
  const MOTION_RATE = { running: 11, working: 4.2 };
  const RUN_STILL_PHASE = 0.9;

  const SWAP = [['ru', 'lu', -1], ['rf', 'lf', -1], ['rh', 'lh', -1], ['rfl', 'lfl', 1], ['rt', 'lt', -1], ['rs', 'ls', -1],
    ['rfoot', 'lfoot', -1], ['rty', 'lty', 1], ['rsy', 'lsy', 1], ['r0', 'l0', 1], ['r1', 'l1', 1],
    ['r2', 'l2', 1], ['r3', 'l3', 1], ['r4', 'l4', 1]];
  function mirror(p) {
    const o = Object.assign({}, p);
    SWAP.forEach(([a, b, s]) => { o[a] = p[b] * s; o[b] = p[a] * s; });
    ['rootX', 'rootR', 'spine', 'head', 'gx'].forEach(k => { o[k] = -p[k]; });
    return o;
  }

  /* Mistura camadas com interrupção segura: trocar no meio da transição não dá salto. */
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
      for (let i = 1; i < this.layers.length; i++) {
        out = lerpDict(out, get(this.layers[i].name), ease(this.layers[i].p));
      }
      return out;
    }
  }

  const ANIMATIONS = ['none', 'idle', 'talk', 'nod', 'shake', 'wave', 'tremble'];
  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const ACCESSORIES = ['toolbelt', 'screwdriver', 'pliers', 'toolbox', 'seat', 'shadow'];

  /* Cada animação escreve nos valores da pose, ponderada por w (0 a 1). */
  const ANIMATE = {
    idle(j, t, w) {
      j.spine += 0.8 * Math.sin(t * 1.1) * w;
      j.head += 1.6 * Math.sin(t * 0.7 + 1) * w;
      j.headY += 1 * Math.sin(t * 0.9) * w;
      j.ru += 1.2 * Math.sin(t * 1.3) * w;
      j.lu -= 1.2 * Math.sin(t * 1.15 + 0.5) * w;
      j.rh += 3 * Math.sin(t * 1.7) * w;
      j.lh -= 3 * Math.sin(t * 1.5 + 1) * w;
    },
    nod(j, t, w) { j.headY += (5 + 5 * Math.sin(t * 7)) * w; j.spine += 0.8 * Math.sin(t * 7) * w; },
    shake(j, t, w) { j.head += 7 * Math.sin(t * 8) * w; j.gx += 0.5 * Math.sin(t * 8) * w; },
    wave(j, t, w, st) {
      j.lu = lerp(j.lu, lerp(-146, -126, st), w);
      j.lf = lerp(j.lf, -14 + 20 * Math.sin(t * 9), w);
      j.lfl = lerp(j.lfl, 1, w);
      j.lh = lerp(j.lh, 14 * Math.sin(t * 9 - 0.8), w);
      j.spine -= 2 * w;
      ['l0', 'l1', 'l2', 'l3'].forEach(k => { j[k] = lerp(j[k], 0, w); });
      j.l4 = lerp(j.l4, 1, w);
    },
    tremble(j, t, w) {
      const s = Math.sin(t * 42), c = Math.cos(t * 37);
      j.rootX += 1.8 * s * w; j.spine += 0.5 * c * w; j.head += 0.9 * c * w;
      j.ru += 1.6 * c * w; j.lu += 1.6 * s * w; j.rh += 3 * s * w; j.lh += 3 * c * w;
    }
  };

  /* ---------- DOM ---------- */
  const NS = 'http://www.w3.org/2000/svg';
  let uidCounter = 0;
  function node(tag, attrs, parent, part, pivot) {
    const el = document.createElementNS(NS, tag);
    for (const k in attrs || {}) el.setAttribute(k, attrs[k]);
    if (part) el.setAttribute('data-part', part);
    if (pivot) el.setAttribute('data-pivot', pivot.join(','));
    if (parent) parent.appendChild(el);
    return el;
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
  const outlineStyle = { fill: C.ink, stroke: C.ink, 'stroke-width': LINE * 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };
  const lineStyle = { stroke: C.ink, 'stroke-width': LINE, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };

  function hexMix(a, b, t) {
    const pa = parseInt(a.slice(1), 16), pb = parseInt(b.slice(1), 16);
    const ch = s => Math.round(lerp((pa >> s) & 255, (pb >> s) & 255, t));
    return 'rgb(' + ch(16) + ',' + ch(8) + ',' + ch(0) + ')';
  }

  class DanRivera {
    constructor(target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: 'standing', animation: 'idle', direction: 'front', seed: 7, autoStart: true }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('DanRivera: elemento de destino não encontrado.');
      this.uid = 'dan' + (++uidCounter);
      this.random = rng(opt.seed);
      this.time = 0;
      this.turn = this._dir(opt.direction);
      this.turnFrom = this.turn; this.turnTo = this.turn; this.turnP = 1; this.turnDur = 1;
      this.poseMix = new Mixer(this._check(opt.pose, POSES, 'Pose'));
      this.exprMix = new Mixer(this._check(opt.expression, EXPRESSIONS, 'Expressão'));
      this.anims = [{ name: this._anim(opt.animation), w: 1 }];
      this.breathing = true;
      this.blinking = true;
      this.talking = 0; this.talkTarget = 0;
      this.look = null; this.gaze = { x: 0, y: 0, tx: 0, ty: 0, next: 1.5 };
      this.nextBlink = 1.2; this.blinkT = -1;
      this.accessories = { toolbelt: false, screwdriver: false, pliers: false, toolbox: false, seat: false, shadow: true };
      this.visible = true; this.alpha = 1;
      this._build();
      this.tick(0);
      this._raf = null;
      if (opt.autoStart) this.play();
    }

    /* ---------- API pública ---------- */
    setExpression(name, o) {
      this.exprMix.to(this._check(name, EXPRESSIONS, 'Expressão'), this._ms(o, 260));
      return this._after();
    }
    setPose(name, o) {
      this.poseMix.to(this._check(name, POSES, 'Pose'), this._ms(o, 480));
      return this._after();
    }
    setAnimation(name, o) {
      this._anim(name);
      const dur = this._ms(o, 300);
      if (dur <= 0) this.anims = [{ name, w: 1 }];
      else if (this.animation !== name) this.anims.push({ name, w: 0, dur });
      return this._after();
    }
    setDirection(dir, o) {
      return this.setTurn(this._dir(dir), o);
    }
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
    setTalking(on) { this.talkTarget = on ? 1 : 0; return this; }
    /* Direção do olhar de -1 a 1; sem argumentos, volta ao olhar automático. */
    lookAt(x, y) { this.look = x === undefined ? null : { x: clamp(x, -1, 1), y: clamp(y || 0, -1, 1) }; return this._after(); }
    blink() { this.blinkT = 0; return this; }
    setAccessory(name, on) {
      if (!ACCESSORIES.includes(name)) throw new Error('DanRivera: acessório desconhecido "' + name + '". Use: ' + ACCESSORIES.join(', '));
      this.accessories[name] = !!on;
      return this._after();
    }
    getState() {
      return {
        expression: this.exprMix.name, pose: this.poseMix.name, animation: this.animation,
        direction: Object.keys(DIRECTIONS).find(k => DIRECTIONS[k] === this.turnTo) || 'custom', turn: this.turnTo, visible: this.visible, accessories: Object.assign({}, this.accessories)
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
    /* SVG autônomo do quadro atual. */
    toSVG() {
      const clone = this.svg.cloneNode(true);
      clone.setAttribute('xmlns', NS);
      clone.removeAttribute('class');
      return new XMLSerializer().serializeToString(clone);
    }
    destroy() { this.pause(); this.svg.remove(); }

    /* Avança dt milissegundos e redesenha. */
    tick(dtMs) {
      const dt = dtMs / 1000;
      this.time += dt;
      this.poseMix.update(dtMs); this.exprMix.update(dtMs);
      if (this.turnP < 1) {
        this.turnP = clamp(this.turnP + dtMs / this.turnDur);
        this.turn = lerp(this.turnFrom, this.turnTo, ease(this.turnP));
      }
      this._updateAnims(dtMs);
      this.talking = lerp(this.talking, this.talkTarget, clamp(dt * 12));
      const target = this.visible ? 1 : 0;
      this.alpha += clamp(target - this.alpha, -dtMs / 200, dtMs / 200);
      this._render(this._blinkAmount(dt), dt);
      return this;
    }

    /* ---------- Internos ---------- */
    _check(name, table, label) {
      if (!table[name]) throw new Error('DanRivera: ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (!ANIMATIONS.includes(name)) throw new Error('DanRivera: animação desconhecida "' + name + '". Use: ' + ANIMATIONS.join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error('DanRivera: direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
      return DIRECTIONS[dir];
    }
    _ms(o, fallback) { return o && o.duration !== undefined ? o.duration : fallback; }
    _after() { if (this._raf === null) this.tick(0); return this; }

    _updateAnims(dtMs) {
      const n = this.anims.length;
      const dur = this.anims[n - 1].dur || 300;
      this.anims.forEach((a, i) => { a.w = clamp(a.w + (i === n - 1 ? 1 : -1) * dtMs / dur); });
      if (n > 1 && this.anims[n - 1].w >= 1) this.anims = [this.anims[n - 1]];
    }
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

    _sampleJoints(t, st) {
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const get = name => {
        const P = POSES[name];
        const a = Object.assign({}, P.front), q = Object.assign({}, P.q), b = Object.assign({}, P.side);
        const motion = POSE_MOTION[name];
        if (motion && (live || name === 'running')) {
          const ph = live ? this.time * MOTION_RATE[name] : RUN_STILL_PHASE;
          motion(a, ph, 0);
          motion(q, ph, 0.5);
          motion(b, ph, 1);
        }
        const start = sign < 0 ? mirror(a) : a;
        const out = {};
        for (const k in start) out[k] = key3(start[k], q[k], b[k], st);
        return out;
      };
      const j = this.poseMix.sample(get);
      this.anims.forEach(a => { if (ANIMATE[a.name]) ANIMATE[a.name](j, this.time, a.w, st); });
      if (j.plant > 0.01) {
        const reach = k => {
          const a = j[k + 't'] * Math.PI / 180, b = a + j[k + 's'] * Math.PI / 180;
          return M.hipY + M.thigh * j[k + 'ty'] * Math.cos(a) + M.shin * j[k + 'sy'] * Math.cos(b) + 40;
        };
        j.rootY = lerp(j.rootY, FLOOR - Math.max(reach('r'), reach('l')), j.plant);
      }
      if (this.animation === 'talk' || this.talking > 0.01) {
        const w = this.animation === 'talk' ? 1 : this.talking;
        j.head += 1.6 * Math.sin(this.time * 5.3) * w;
        j.headY += 1.6 * Math.abs(Math.sin(this.time * 4.1)) * w;
      }
      return j;
    }

    _mouthFlap() {
      const w = this.animation === 'talk' ? 1 : this.talking;
      if (w < 0.01) return 0;
      const t = this.time;
      const n = Math.abs(Math.sin(t * 13.1) * 0.6 + Math.sin(t * 7.3 + 1) * 0.4);
      return n * w;
    }

    /* ---------- Construção ---------- */
    _build() {
      const u = this.uid;
      const svg = this.svg = node('svg', { viewBox: VIEWBOX, class: 'dan-rig', role: 'img', 'aria-label': 'Dan Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = node('defs', {}, svg);
      this.clipEyeR = node('path', {}, node('clipPath', { id: u + '-eye-r' }, defs));
      this.clipEyeL = node('path', {}, node('clipPath', { id: u + '-eye-l' }, defs));
      this.clipMouth = node('path', {}, node('clipPath', { id: u + '-mouth' }, defs));

      this.shadow = node('ellipse', { cx: 0, cy: FLOOR + 6, rx: 150, ry: 17, fill: '#000', 'fill-opacity': 0.22 }, svg, 'shadow');
      this.flip = node('g', {}, svg, 'character');
      this._buildProps(this.flip);

      const rig = this.rig = node('g', {}, this.flip, 'pelvis', PIVOTS.pelvis);
      this.spineNodes = [];
      const spineLayer = (name) => { const g = node('g', {}, rig, name, PIVOTS.torso); this.spineNodes.push(g); return g; };

      this.backArmLayer = spineLayer('layer-back-arm');
      this.hipsO = node('path', Object.assign({}, outlineStyle), rig, 'hips-outline');
      this.legL = this._buildLeg(rig, 'l', 'leg-left');
      this.legR = this._buildLeg(rig, 'r', 'leg-right');
      this.hipsF = node('path', { fill: C.jeans }, rig, 'hips');

      const neck = this.neck = node('g', {}, spineLayer('layer-neck'), 'neck');
      node('path', Object.assign({ d: capsule(46, 29, 31), fill: C.skin }, lineStyle), neck);
      node('path', { d: 'M-27 2H27V16Q0 28 -27 16Z', fill: C.skinShade }, neck);

      const torso = spineLayer('torso');
      this.torsoShape = node('path', Object.assign({ fill: C.navy }, lineStyle), torso);
      this.torsoShade = node('path', { fill: C.navyShade }, torso);
      this.wrinkles = node('path', { fill: 'none', stroke: C.navyDark, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, torso);

      this.collar = node('path', { fill: 'none', stroke: C.navyDark, 'stroke-width': 9, 'stroke-linecap': 'round' }, torso, 'collar');

      this.belt = this._buildBelt(spineLayer('toolbelt'));

      this.headLayer = spineLayer('layer-head');
      this._buildHead(this.headLayer);

      this.frontArmLayer = spineLayer('layer-front-arm');
      this.armL = this._buildArm(this.frontArmLayer, 'l', 'arm-left');
      this.armR = this._buildArm(this.frontArmLayer, 'r', 'arm-right');
      this.armLParent = this.frontArmLayer;
    }

    _buildLeg(parent, k, part) {
      const g = node('g', {}, parent, part, k === 'r' ? PIVOTS.hipRight : PIVOTS.hipLeft);
      const leg = { root: g, thigh: [], shin: [], foot: [], thighPaths: [], shinPaths: [], fills: [], k };
      ['o', 'f'].forEach(pass => {
        const style = pass === 'o' ? outlineStyle : { fill: C.jeans };
        const passG = node('g', {}, g);
        const thigh = node('g', {}, passG, pass === 'f' ? 'thigh' : null);
        const tp = node('path', Object.assign({}, style), thigh);
        const shin = node('g', {}, thigh, pass === 'f' ? 'shin' : null, PIVOTS.knee);
        const sp = node('path', Object.assign({}, style), shin);
        const foot = node('g', {}, shin, pass === 'f' ? 'foot' : null, PIVOTS.ankle);
        leg.thigh.push(thigh); leg.shin.push(shin); leg.foot.push(foot);
        leg.thighPaths.push(tp); leg.shinPaths.push(sp);
        if (pass === 'o') {
          leg.bootO = node('path', Object.assign({}, outlineStyle), foot);
          leg.soleO = node('path', Object.assign({}, outlineStyle), foot);
        } else {
          leg.fills.push(tp, sp);
          leg.thighShade = node('path', { fill: C.jeansShade, d: capsule(120, 8, 7) }, thigh);
          leg.shinShade = node('path', { fill: C.jeansShade, d: capsule(112, 7, 7) }, shin);
          leg.knee = node('path', { d: 'M-15 -3Q0 8 15 -3', fill: 'none', stroke: C.jeansShade, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, shin);
          leg.boot = node('path', { fill: C.boot }, foot);
          leg.bootLine = node('path', { fill: 'none', stroke: C.bootShade, 'stroke-width': 4, 'stroke-linecap': 'round' }, foot);
          leg.laces = node('path', { fill: 'none', stroke: C.lace, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, foot);
          leg.sole = node('path', { fill: C.sole }, foot);
          leg.cuff = node('path', { d: 'M-26 -10H26', fill: 'none', stroke: C.jeansLight, 'stroke-width': 6, 'stroke-linecap': 'round' }, foot);
        }
      });
      return leg;
    }

    _buildArm(parent, k, part) {
      const g = node('g', {}, parent, part, k === 'r' ? PIVOTS.shoulderRight : PIVOTS.shoulderLeft);
      const arm = { root: g, upper: [], fore: [], hand: [], skin: [], forePaths: [], k };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const skin = isO ? outlineStyle : { fill: C.skin };
        const passG = node('g', {}, g);
        const upper = node('g', {}, passG, isO ? null : 'upper-arm');
        const up = node('path', Object.assign({ d: capsule(M.upperArm, 23, 21) }, skin), upper);
        const fore = node('g', {}, upper, isO ? null : 'forearm', PIVOTS.elbow);
        const fp = node('path', Object.assign({}, skin), fore);
        arm.forePaths.push(fp);
        const hand = node('g', {}, fore, isO ? null : 'hand', PIVOTS.wrist);
        arm.upper.push(upper); arm.fore.push(fore); arm.hand.push(hand);
        if (isO) {
          node('path', Object.assign({ d: capsule(60, 29, 28) }, outlineStyle), upper);
          arm.palmO = node('path', Object.assign({ d: this._palm() }, outlineStyle), hand);
          arm.fingersO = node('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14 + LINE, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
        } else {
          arm.skin.push(up, fp);
          arm.sleeve = node('path', { d: capsule(60, 29, 28), fill: C.navy }, upper);
          node('path', { d: 'M-27 76H27', stroke: C.navyDark, 'stroke-width': 5, 'stroke-linecap': 'round', fill: 'none' }, upper);
          arm.foreShade = node('path', { fill: C.skinShade, transform: 'translate(10 8)' }, fore);
          this._buildHand(arm, hand);
        }
      });
      arm.shoulder = node('ellipse', { fill: C.navy }, g, 'shoulder');
      return arm;
    }

    _palm() { return 'M-19 -4Q-23 16 -20 34Q0 42 20 34Q23 16 19 -4Q0 -10 -19 -4Z'; }

    _buildHand(arm, hand) {
      arm.fingerGroup = node('g', {}, hand, 'fingers');
      arm.fingers = [0, 1, 2, 3].map(() => ({
        o: node('path', { fill: 'none', stroke: C.ink, 'stroke-width': 12.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, arm.fingerGroup),
        f: node('path', { fill: 'none', stroke: C.skin, 'stroke-width': 8.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, arm.fingerGroup)
      }));
      arm.palm = node('path', { d: this._palm(), fill: C.skin }, hand, 'palm');
      arm.propSlot = node('g', {}, hand, 'held-prop');
      arm.thumbO = node('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.thumbF = node('path', { fill: 'none', stroke: C.skin, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.fingersOnTop = false;
      if (arm.k === 'r') {
        const s = this.screwdriver = node('g', {}, arm.propSlot, 'screwdriver');
        node('rect', Object.assign({ x: -28, y: 22, width: 54, height: 20, rx: 8, fill: C.toolAlt }, lineStyle), s);
        node('rect', Object.assign({ x: 26, y: 28, width: 58, height: 8, fill: C.metal }, lineStyle), s);
        node('path', Object.assign({ d: 'M84 28L96 32L84 36Z', fill: C.metalDark }, lineStyle), s);
      } else {
        const p = this.pliers = node('g', {}, arm.propSlot, 'pliers');
        node('path', Object.assign({ d: 'M-20 24Q0 16 26 26L26 32Q0 26 -20 34Z', fill: C.tool }, lineStyle), p);
        node('path', Object.assign({ d: 'M-20 42Q0 44 26 36L26 30Q0 36 -20 34Z', fill: C.tool }, lineStyle), p);
        node('path', Object.assign({ d: 'M24 24L66 28L68 31L24 38Z', fill: C.metal }, lineStyle), p);
        node('path', { d: 'M28 31H64', stroke: C.ink, 'stroke-width': 2.5, fill: 'none' }, p);
      }
    }

    _buildBelt(g) {
      const belt = { g };
      belt.band = node('path', Object.assign({ fill: C.leather }, lineStyle), g, 'belt');
      belt.buckle = node('rect', Object.assign({ width: 26, height: 22, rx: 3, fill: C.metal }, lineStyle), g);
      belt.pouch = node('g', {}, g, 'pouch');
      node('rect', Object.assign({ x: 8, y: -24, width: 9, height: 28, rx: 3, fill: C.toolAlt }, lineStyle), belt.pouch);
      node('path', Object.assign({ d: 'M-14 -30L-6 -30L-4 4L-12 4Z', fill: C.metal }, lineStyle), belt.pouch);
      node('path', Object.assign({ d: 'M-26 0H26L22 52Q0 62 -22 52Z', fill: C.leatherDark }, lineStyle), belt.pouch);
      node('path', { d: 'M-22 14H22', stroke: C.leather, 'stroke-width': 4, fill: 'none' }, belt.pouch);
      belt.pouch2 = node('g', {}, g, 'pouch-far');
      node('path', Object.assign({ d: 'M-22 0H22L18 42Q0 50 -18 42Z', fill: C.leatherDark }, lineStyle), belt.pouch2);
      return belt;
    }

    _buildProps(parent) {
      const seat = this.seatProp = node('g', {}, parent, 'seat');
      node('rect', Object.assign({ x: -74, y: 182, width: 148, height: 24, rx: 6, fill: C.wood }, lineStyle), seat);
      node('path', Object.assign({ d: 'M-62 206L-74 340H-58L-40 206Z', fill: C.woodDark }, lineStyle), seat);
      node('path', Object.assign({ d: 'M62 206L74 340H58L40 206Z', fill: C.woodDark }, lineStyle), seat);
      node('path', Object.assign({ d: 'M-64 276H64V290H-64Z', fill: C.wood }, lineStyle), seat);

      const box = this.boxProp = node('g', { transform: 'translate(232 ' + (FLOOR - 98) + ')' }, parent, 'toolbox');
      node('path', Object.assign({ d: 'M-42 0V-22Q-42 -30 -34 -30H34Q42 -30 42 -22V0H30V-18H-30V0Z', fill: C.metalDark }, lineStyle), box);
      node('rect', Object.assign({ x: -82, y: 0, width: 164, height: 98, rx: 8, fill: C.tool }, lineStyle), box);
      node('rect', { x: -80, y: 30, width: 160, height: 7, fill: '#a92d1f' }, box);
      node('rect', Object.assign({ x: -14, y: 24, width: 28, height: 22, rx: 3, fill: C.metal }, lineStyle), box);
    }

    _buildHead(parent) {
      const u = this.uid;
      const head = this.head = node('g', {}, parent, 'head', PIVOTS.head);
      this.earBack = node('g', {}, head, 'ears-back');
      this.earFar = this._ear(this.earBack);
      this.earNear = this._ear(this.earBack);
      this.headShape = node('path', Object.assign({ fill: C.skin }, lineStyle), head, 'face');
      this.stubble = node('path', { fill: C.stubble }, head, 'stubble');
      this.headShade = node('path', { fill: C.skinShade, 'fill-opacity': 0.75 }, head);
      this.tint = node('path', {}, head, 'tint');

      const mouth = this.mouth = node('g', {}, head, 'mouth');
      this.mouthShape = node('path', Object.assign({ fill: C.mouth }, lineStyle), mouth);
      const inner = node('g', { 'clip-path': 'url(#' + u + '-mouth)' }, mouth);
      this.tongue = node('ellipse', { fill: C.tongue }, inner);
      this.teeth = node('rect', { fill: C.teeth, x: -60, width: 120 }, inner);
      this.gritLines = node('path', { fill: 'none', stroke: C.ink, 'stroke-width': 2.5 }, inner);
      this.mouthLine = node('path', Object.assign({ fill: 'none' }, lineStyle), mouth);

      this.eyeR = this._eye(head, 'eye-right', u + '-eye-r');
      this.eyeL = this._eye(head, 'eye-left', u + '-eye-l');
      this.noseFill = node('ellipse', { fill: C.skin }, head, 'nose');
      this.noseLine = node('path', Object.assign({ fill: 'none' }, lineStyle), head);
      this.hair = node('path', Object.assign({ fill: C.hair }, lineStyle), head, 'hair');
      this.hairShine = node('path', { fill: 'none', stroke: '#5a4231', 'stroke-width': 7, 'stroke-linecap': 'round' }, head);
      this.browR = node('path', { fill: 'none', stroke: C.brow, 'stroke-width': 11.5, 'stroke-linecap': 'round' }, head, 'brow-right');
      this.browL = node('path', { fill: 'none', stroke: C.brow, 'stroke-width': 11.5, 'stroke-linecap': 'round' }, head, 'brow-left');
      this.earTop = node('g', {}, head, 'ears-top');
      this.sweat = node('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat);
      this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
    }
    _drop(parent) {
      return node('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
    }
    _ear(parent) {
      const g = node('g', {}, parent);
      node('path', Object.assign({ d: 'M-4 -24Q-22 -26 -20 -2Q-18 24 2 20Q10 0 -4 -24Z', fill: C.skin }, lineStyle), g);
      node('path', { d: 'M-6 -12Q-14 -10 -11 3', fill: 'none', stroke: C.skinShade, 'stroke-width': 4, 'stroke-linecap': 'round' }, g);
      return g;
    }
    _eye(parent, part, clipId) {
      const g = node('g', {}, parent, part);
      const white = node('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, g);
      const iris = node('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
      const ball = node('g', {}, iris);
      node('circle', { r: 12.5, fill: C.iris }, ball);
      node('circle', { r: 8.5, fill: '#120d0a' }, ball);
      node('circle', { cx: 4, cy: -5, r: 3.6, fill: '#fff' }, ball);
      const lid = node('path', { fill: 'none', stroke: C.ink, 'stroke-width': 6.5, 'stroke-linecap': 'round' }, g);
      return { g, white, ball, lid };
    }

    /* ---------- Desenho de um quadro ---------- */
    _render(blink, dt) {
      const t = Math.abs(this.turn);
      const st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const j = this._sampleJoints(t, st);
      const e = this.exprMix.sample(n => EXPRESSIONS[n]);
      this._gaze(dt, live);

      const b = this.breathing ? Math.sin(this.time * TAU / 3.7) : 0;
      put(this.svg, 'opacity', String(Math.round(this.alpha * 100) / 100));
      put(this.svg, 'display', this.alpha <= 0.001 ? 'none' : 'inline');
      put(this.flip, 'transform', 'scale(' + sign + ' 1)');
      put(this.rig, 'transform', tf(j.rootX, j.rootY, j.rootR));

      const spineT = tf(0, 0, j.spine, 1 + b * 0.007, 1 + b * 0.011);
      this.spineNodes.forEach(g => put(g, 'transform', spineT));

      this._renderBody(j, t, st, b);
      this._renderLeg(this.legR, j, 'r', st, 0);
      const farTone = clamp((st - 0.5) * 2);
      this._renderLeg(this.legL, j, 'l', st, farTone);
      this._renderArm(this.armR, j, 'r', st, b, 0);
      this._renderArm(this.armL, j, 'l', st, b, farTone);
      this._renderHead(j, e, st, blink);
      this._renderProps(j, st);

      const toBack = st > (j.farFront > 0.5 ? 0.75 : 0.3);
      if (toBack && this.armLParent !== this.backArmLayer) {
        this.backArmLayer.appendChild(this.armL.root); this.armLParent = this.backArmLayer;
      } else if (!toBack && this.armLParent !== this.frontArmLayer) {
        this.frontArmLayer.insertBefore(this.armL.root, this.frontArmLayer.firstChild); this.armLParent = this.frontArmLayer;
      }
    }

    _renderBody(j, t, st, b) {
      const hips = spline(shape('hips', st), true);
      put(this.hipsO, 'd', hips); put(this.hipsF, 'd', hips);
      put(this.torsoShape, 'd', spline(shape('torso', st), true));
      put(this.torsoShade, 'd', spline(shape('torsoShade', st < 0.5 ? 0 : 1), true));
      shown(this.torsoShade, Math.abs(1 - 2 * st));
      const wx = lerp(0, 16, st);
      put(this.wrinkles, 'd', 'M' + f(wx - 58) + ' -34Q' + f(wx - 30) + ' -22 ' + f(wx - 8) + ' -28M' + f(wx + 62) + ' -86Q' + f(wx + 44) + ' -70 ' + f(wx + 20) + ' -72');
      put(this.neck, 'transform', tf(lerp(0, 6, st), M.headY + 6));
      const cw = lerp(38, 22, st), cx = lerp(0, 5, st);
      put(this.collar, 'd', 'M' + f(cx - cw) + ' -232Q' + f(cx) + ' ' + f(lerp(-192, -202, st)) + ' ' + f(cx + cw) + ' -232');

      const belt = this.belt;
      const beltOn = this.accessories.toolbelt ? 1 : 0;
      shown(belt.g, beltOn);
      if (beltOn) {
        const w = lerp(93, 70, st), dx = lerp(0, 4, st);
        put(belt.band, 'd', 'M' + f(dx - w) + ' 14Q' + f(dx) + ' 26 ' + f(dx + w) + ' 14V38Q' + f(dx) + ' 50 ' + f(dx - w) + ' 38Z');
        put(belt.buckle, 'transform', tf(lerp(-13, 42, st), lerp(24, 19, st)));
        put(belt.pouch, 'transform', tf(lerp(-72, -22, st), 30));
        put(belt.pouch2, 'transform', tf(72, 30));
        shown(belt.pouch2, st < 0.4 ? 1 : 0);
      }
    }

    _renderLeg(leg, j, k, st, far) {
      const ang = j[k + 't'], knee = j[k + 's'], ank = j[k + 'foot'];
      const ty = j[k + 'ty'], sy = j[k + 'sy'];
      const hipX = k === 'r' ? lerp(-38, -7, st) : lerp(38, 9, st);
      put(leg.root, 'transform', tf(hipX, M.hipY));
      const lenT = M.thigh * ty, lenS = M.shin * sy;
      const dT = capsule(lenT, 34, 27), dS = capsule(lenS, 27, 26);
      const footX = (k === 'r' ? -5 : 5) * (1 - st);
      const fT = tf(0, 0, ang), sT = tf(0, lenT, knee), footT = tf(footX, lenS, ank);
      leg.thighPaths.forEach(p => put(p, 'd', dT));
      leg.shinPaths.forEach(p => put(p, 'd', dS));
      leg.thigh.forEach(g => put(g, 'transform', fT));
      leg.shin.forEach(g => put(g, 'transform', sT));
      leg.foot.forEach(g => put(g, 'transform', footT));

      const boot = spline(shape('boot', st), true), sole = spline(shape('sole', st), true);
      put(leg.bootO, 'd', boot); put(leg.boot, 'd', boot);
      put(leg.soleO, 'd', sole); put(leg.sole, 'd', sole);
      put(leg.bootLine, 'd', 'M-26 10Q0 16 26 10');
      const lx = lerp(0, 26, st);
      put(leg.laces, 'd', 'M' + f(lx - 12) + ' 2H' + f(lx + 10) + 'M' + f(lx - 10) + ' 12H' + f(lx + 16));

      const shadeOff = lerp(15, -14, st);
      put(leg.thighShade, 'transform', tf(shadeOff, 8, 0, 1, Math.max(ty, 0.05)));
      put(leg.shinShade, 'transform', tf(shadeOff, 14, 0, 1, sy));
      shown(leg.thighShade, ty > 0.4 ? 1 : 0);

      const col = far > 0.01 ? hexMix(C.jeans, C.jeansShade, far * 0.85) : C.jeans;
      leg.fills.forEach(p => put(p, 'fill', col));
    }

    _renderArm(arm, j, k, st, b, far) {
      const sx = k === 'r' ? key3(-90, -62, -8, st) : key3(90, 66, 18, st);
      const sy = M.shoulderY + j.shrug * -10 - b * 0.8;
      put(arm.root, 'transform', tf(sx, sy));
      const inFront = k === 'r' || this.armLParent === this.frontArmLayer;
      shown(arm.shoulder, inFront ? 1 : 0);
      put(arm.shoulder, 'cx', f((k === 'r' ? 1 : -1) * key3(15, 12, 0, st)));
      put(arm.shoulder, 'cy', f(key3(5, 0, -12, st)));
      put(arm.shoulder, 'rx', f(key3(33, 33, 35, st)));
      put(arm.shoulder, 'ry', f(key3(33, 30, 24, st)));
      const uT = tf(0, 0, j[k + 'u']), fT = tf(0, M.upperArm, j[k + 'f']);
      const handFlip = k === 'r' ? 1 : lerp(-1, 1, smooth(clamp((st - 0.12) / 0.2)));
      const foreLen = M.foreArm * j[k + 'fl'];
      const dF = capsule(foreLen, 21, 17);
      arm.forePaths.forEach(p => put(p, 'd', dF));
      put(arm.foreShade, 'd', capsule(foreLen * 0.8, 6, 5));
      const hT = tf(0, foreLen, j[k + 'h'], Math.abs(handFlip) < 0.35 ? 0.35 * (handFlip < 0 ? -1 : 1) : handFlip, 1);
      arm.upper.forEach(g => put(g, 'transform', uT));
      arm.fore.forEach(g => put(g, 'transform', fT));
      arm.hand.forEach(g => put(g, 'transform', hT));

      const curls = [0, 1, 2, 3].map(i => j[k + i]);
      const X = [-14.5, -5, 5, 14.5];
      let all = '';
      arm.fingers.forEach((fin, i) => {
        const c = clamp(curls[i]);
        const y0 = 28, len = (i === 1 || i === 2 ? 25 : 21) * (i === 3 ? 0.92 : 1);
        const a1 = c * Math.PI * 0.5, a2 = c * Math.PI * 1.05;
        const y1 = y0 + len * 0.55 * Math.cos(a1);
        const y2 = y1 + len * 0.5 * Math.cos(a2);
        const d = 'M' + X[i] + ' ' + y0 + 'L' + X[i] + ' ' + f(y1) + 'L' + X[i] + ' ' + f(y2);
        put(fin.o, 'd', d); put(fin.f, 'd', d);
        all += d;
      });
      put(arm.fingersO, 'd', all);
      const onTop = (curls[0] + curls[1] + curls[2] + curls[3]) / 4 > 0.5 || curls[1] > 0.5;
      if (onTop !== arm.fingersOnTop) {
        const handG = arm.hand[1];
        if (onTop) handG.insertBefore(arm.fingerGroup, arm.thumbO);
        else handG.insertBefore(arm.fingerGroup, arm.palm);
        arm.fingersOnTop = onTop;
      }
      const th = clamp(j[k + '4']);
      const thumb = 'M15 8L' + f(lerp(12, 30, th)) + ' ' + f(lerp(20, 18, th)) + 'L' + f(lerp(0, 36, th)) + ' ' + f(lerp(24, 36, th));
      put(arm.thumbO, 'd', thumb); put(arm.thumbF, 'd', thumb);

      const sleeve = far > 0.01 ? hexMix(C.navy, C.navyShade, far) : C.navy;
      put(arm.sleeve, 'fill', sleeve);
      const skin = far > 0.01 ? hexMix(C.skin, C.skinShade, far * 0.6) : C.skin;
      arm.skin.forEach(p => put(p, 'fill', skin));
    }

    _renderEye(eye, clip, x, y, sx, inner, e, blink, gx, gy) {
      put(eye.g, 'transform', tf(x, y, 0, sx, 1));
      const W = 20;
      const open = Math.max(0, e.eyeOpen * (1 - blink));
      const T = 22 * open * 1.33, B = 19 * e.eyeLow * (1 - blink * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    }

    _renderHead(j, e, st, blink) {
      put(this.head, 'transform', tf(lerp(0, 8, st), M.headY + j.headY + j.shrug * 4, j.head));
      const flap = this._mouthFlap();
      const drop = Math.max(0, e.mouthOpen + flap * 20 - 16) * 0.62;
      const jaw = (pts, full, half) => {
        full.forEach(i => { pts[i][1] += drop; });
        half.forEach(i => { pts[i][1] += drop * 0.5; });
        return pts;
      };
      const headD = spline(jaw(shape('head', st), [0, 1, 13], [2, 12]), true);
      put(this.headShape, 'd', headD);
      put(this.headShade, 'd', spline(jaw(shape('headShade', st < 0.5 ? 0 : 1), [0, 7], [1, 6]), true));
      shown(this.headShade, Math.abs(1 - 2 * st));
      put(this.stubble, 'd', spline(jaw(shape('stubble', st), [2, 3, 4], [1, 5]), true));
      put(this.hair, 'd', spline(shape('hair', st), true));
      put(this.tint, 'd', headD);
      put(this.tint, 'fill', e.tint >= 0 ? '#e0392b' : '#7fb2d9');
      put(this.tint, 'opacity', String(Math.round(Math.abs(e.tint) * 26) / 100));
      put(this.noseFill, 'fill', hexMix(C.skin, e.tint >= 0 ? '#e0392b' : '#7fb2d9', Math.abs(e.tint) * 0.26));
      const shine = key3(0, 10, -2, st);
      put(this.hairShine, 'd', 'M' + f(shine - 44) + ' -170Q' + f(shine - 16) + ' -182 ' + f(shine + 16) + ' -181');

      const gx = clamp(j.gx + e.exGx + this.gaze.x, -1, 1);
      const gy = clamp(j.gy + e.exGy + this.gaze.y, -1, 1);

      const rx = key3(-34, 6, 36, st), lx = key3(34, 58, 74, st), ey = -84;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.72, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, blink, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx, ey, Math.max(ls, 0.06), -1, e, blink, gx, gy);

      this._renderBrow(this.browR, rx, 1, e, rs);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx, -1, e, Math.max(ls, 0.1));

      const nx = key3(0, 44, 72, st), ny = -55;
      put(this.noseFill, 'cx', f(nx)); put(this.noseFill, 'cy', ny);
      put(this.noseFill, 'rx', f(lerp(14, 15, st))); put(this.noseFill, 'ry', 12);
      const aC = lerp(Math.PI / 2, 0.2, st), span = lerp(1.9, 1.5, st);
      const arc = [];
      for (let i = 0; i <= 6; i++) {
        const a = aC - span + (2 * span * i) / 6;
        arc.push([nx + Math.cos(a) * lerp(14, 15, st), ny + Math.sin(a) * 12]);
      }
      put(this.noseLine, 'd', spline(arc, false));

      this._renderMouth(e, st);

      const nearX = lerp(-81, -20, st), nearY = -66;
      put(this.earNear, 'transform', tf(nearX, nearY, 0, 1, 1));
      put(this.earFar, 'transform', tf(lerp(81, 60, st), nearY, 0, -1, 1));
      shown(this.earFar, st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw);
      put(this.sweat1, 'transform', tf(lerp(84, 88, st), lerp(-128, -112, st), 12, 0.55 + sw * 0.55));
      put(this.sweat2, 'transform', tf(key3(-90, 98, 98, st), key3(-100, -92, -92, st), -10, 0.4 + sw * 0.4));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -56 + (this.animation === 'none' ? 0.5 : fall) * 22, 0, 0.8));
    }

    _renderBrow(el, x, inner, e, sx) {
      const y = -121 + e.browY;
      const w = 23 * sx;
      const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
      const cy = y - e.browArch * 2.4 - e.browTilt * 0.1;
      put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY) + 'Q' + f(x) + ' ' + f(cy) + ' ' + f(x + w * inner) + ' ' + f(inY));
    }

    _renderMouth(e, st) {
      const flap = this._mouthFlap();
      const open = e.mouthOpen + flap * 20;
      const w = (e.mouthW + flap * -3) * key3(1, 0.86, 0.62, st);
      const smile = e.smile;
      const skew = e.skew;
      const lY = -smile * 12 + skew * 6, rY = -smile * 12 - skew * 6;
      const cx = key3(0, 26, 36, st);
      const my = -24;
      put(this.mouth, 'transform', tf(cx, my));
      const rnd = 0.55 + 0.42 * clamp(open / 30);
      const up = smile * 8 - Math.min(open, 26) * 0.1;
      const low = smile * 8 + open * 1.33;
      const top = 'M' + f(-w) + ' ' + f(lY) + 'C' + f(-w * rnd) + ' ' + f(up) + ' ' + f(w * rnd) + ' ' + f(up) + ' ' + f(w) + ' ' + f(rY);
      const d = top + 'C' + f(w * rnd) + ' ' + f(low) + ' ' + f(-w * rnd) + ' ' + f(low) + ' ' + f(-w) + ' ' + f(lY) + 'Z';
      const isOpen = open > 1.5;
      put(this.mouthShape, 'd', d);
      put(this.clipMouth, 'd', d);
      shown(this.mouthShape, isOpen ? 1 : 0);
      put(this.mouthLine, 'd', top);
      shown(this.mouthLine, isOpen ? 0 : 1);

      const band = Math.min(open * 0.42, 14) * e.teeth + (e.grit > 0.5 ? open : 0);
      put(this.teeth, 'y', f(up - 16)); put(this.teeth, 'height', f(Math.max(0, 16 + band)));
      shown(this.teeth, e.teeth > 0.02 && isOpen ? 1 : 0);
      put(this.tongue, 'cx', 0); put(this.tongue, 'cy', f(smile * 8 + open * 1.05));
      put(this.tongue, 'rx', f(w * 0.62)); put(this.tongue, 'ry', f(Math.max(0, open * 0.42)));
      shown(this.tongue, e.tongue > 0.02 && isOpen ? 1 : 0);
      const mid = (up + low) / 2 - open * 0.12;
      put(this.gritLines, 'd', e.grit > 0.5
        ? 'M' + f(-w) + ' ' + f(mid) + 'H' + f(w) + 'M' + f(-w * 0.5) + ' -30V40M0 -30V40M' + f(w * 0.5) + ' -30V40'
        : 'M0 0');
    }

    _renderProps(j, st) {
      const a = this.accessories;
      shown(this.screwdriver, Math.max(j.screwdriver, a.screwdriver ? 1 : 0));
      shown(this.pliers, Math.max(j.pliers, a.pliers ? 1 : 0));
      shown(this.boxProp, Math.max(j.toolbox, a.toolbox ? 1 : 0));
      shown(this.seatProp, Math.max(j.seat, a.seat ? 1 : 0));
      /* O banco acompanha o quadril: encosta nele em altura e fica sob ele em posição. */
      const seatScale = (FLOOR - (j.rootY + M.hipY + 34)) / (FLOOR - 182);
      put(this.seatProp, 'transform', 'translate(' + f(j.rootX + key3(0, -10, -26, st)) + ' ' + FLOOR + ') scale(1 ' + (Math.round(seatScale * 1000) / 1000) + ') translate(0 ' + -FLOOR + ')');
      shown(this.shadow, a.shadow ? 1 : 0);
      put(this.shadow, 'rx', f(lerp(150, 170, st) * (1 - clamp(-j.rootY / 80) * 0.3)));
    }
  }

  DanRivera.EXPRESSIONS = Object.keys(EXPRESSIONS);
  DanRivera.POSES = Object.keys(POSES);
  DanRivera.ANIMATIONS = ANIMATIONS.slice();
  DanRivera.DIRECTIONS = Object.keys(DIRECTIONS);
  DanRivera.ACCESSORIES = ACCESSORIES.slice();
  DanRivera.PIVOTS = PIVOTS;
  DanRivera.PALETTE = C;
  return DanRivera;
});
