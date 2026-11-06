/*!
 * MiaRivera — personagem de produção do canal Survive the Headline.
 *
 * Mesmo sistema de rig de DanRivera: escala, chão e peso de contorno idênticos,
 * para os dois dividirem a cena. Pose, expressão, direção e figurino são valores
 * aplicados a um único modelo SVG.
 *
 * Uso:
 *   const mia = new MiaRivera('#palco');
 *   mia.setExpression('skeptical');
 *   mia.setPose('arms_crossed');
 *   mia.setAnimation('idle');
 *   mia.setDirection('left');
 *   mia.setVisible(true);
 *   mia.setOutfit('scrubs');           // 'casual' | 'scrubs'
 *   mia.setHair('up');                 // 'down' | 'up'
 *   mia.setArm('right', { shoulder: -40, elbow: -60, hand: 'open' });  // braço avulso
 *   mia.setArm('right', null);         // devolve o braço à pose
 *   mia.setViseme('A');                // sincronização labial; null encerra
 *
 * Vídeo quadro a quadro (determinístico):
 *   const mia = new MiaRivera(el, { autoStart: false, seed: 42 });
 *   mia.tick(1000 / 30);
 *   const svg = mia.toSVG();
 *
 * CSS: toda parte tem data-part e id (#mia-head, #mia-hair-front, #mia-pupil-right...).
 * "right" e "left" são os lados da própria personagem.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.MiaRivera = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- Paleta travada ---------- */
  const C = {
    ink: '#1b1a22', skin: '#f0bf9c', skinShade: '#dda27c',
    hair: '#43291c', hairShine: '#6a4630', hairDeep: '#33200f', brow: '#33200f',
    eyeWhite: '#ffffff', iris: '#6b4226', mole: '#8a5a3c',
    mouth: '#5a1c22', lip: '#c9757a', tongue: '#d9636a', teeth: '#fbf7ee', sweat: '#8fd6ff',
    metal: '#b9c2cc', metalDark: '#7f8a96', wood: '#a5764a', woodDark: '#7d5533',
    watchBand: '#3a3f4b', watchFace: '#e8edf2', badge: '#ffffff', badgeStripe: '#1c8c96', clip: '#c7ced6'
  };
  const OUTFITS = {
    casual: {
      top: '#0f5f6e', topShade: '#0b4a57', topDark: '#083a45',
      pants: '#2f4a78', pantsShade: '#253b61', pantsLight: '#4f6d9e',
      shoe: '#f4f5f7', sole: '#c9ced6', stripe: '#8fb8c4',
      sleeve: 72, hem: 0, neck: 0, badge: false, hair: 'down'
    },
    scrubs: {
      top: '#1c8c96', topShade: '#157580', topDark: '#0f5e68',
      pants: '#1a808a', pantsShade: '#136770', pantsLight: '#3aa3ad',
      shoe: '#e9edf1', sole: '#aab2bd', stripe: '#1c8c96',
      sleeve: 58, hem: 18, neck: 24, badge: true, hair: 'up'
    }
  };
  const LINE = 4.5;
  const VIEWBOX = '-425 -480 850 860';
  const FLOOR = 340;
  const BASE_ROOT = 18;        // Mia é ~7% mais baixa que Dan, com o mesmo chão

  const M = { shoulderY: -172, upperArm: 94, foreArm: 90, hipY: 10, thigh: 138, shin: 136, headY: -232, footH: 38 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-76, M.shoulderY], shoulderLeft: [76, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-34, M.hipY], hipLeft: [34, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  /* ---------- Matemática ---------- */
  const lerp = (a, b, t) => a + (b - a) * t;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const smooth = t => t * t * (3 - 2 * t);
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const f = n => Math.round(n * 10) / 10;
  const TAU = Math.PI * 2;
  /* Curva que passa por três chaves: frente (u=0), 3/4 (u=0.5) e perfil (u=1). */
  const key3 = (a, b, c, u) => a * (1 - 2 * u) * (1 - u) + 4 * b * u * (1 - u) + c * u * (2 * u - 1);

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
  const lerpDict = (a, b, t) => {
    const o = {};
    for (const k in a) o[k] = lerp(a[k], b[k], t);
    return o;
  };

  /* ---------- Formas: frente, 3/4 e perfil com os mesmos pontos ---------- */
  const SHAPE = {
    head: {
      front: [[0, 8], [30, 5], [54, -14], [68, -54], [72, -98], [62, -136], [32, -158], [0, -163],
        [-32, -158], [-62, -136], [-72, -98], [-68, -54], [-54, -14], [-30, 5]],
      q: [[18, 8], [46, 2], [63, -18], [71, -56], [73, -98], [62, -136], [34, -158], [-2, -164],
        [-38, -158], [-68, -132], [-77, -92], [-71, -52], [-52, -16], [-12, 6]],
      side: [[42, 8], [57, -2], [63, -22], [66, -58], [69, -98], [62, -132], [36, -158], [-4, -165],
        [-46, -156], [-76, -128], [-83, -88], [-71, -50], [-40, -18], [8, 0]]
    },
    headShade: {
      front: [[30, 5], [54, -14], [68, -54], [72, -98], [67, -98], [62, -56], [48, -20], [24, 0]],
      side: [[54, -1], [28, 3], [8, 0], [-28, -13], [-22, -25], [2, -13], [28, -10], [47, -11]]
    },
    hairFront: {
      front: [[-72, 2, 1], [-84, -40], [-92, -96], [-86, -140], [-62, -172], [-22, -188], [22, -190], [62, -174], [86, -142],
        [92, -96], [84, -40], [72, 2, 1], [62, -34], [66, -84], [60, -118], [44, -138], [20, -152, 1], [-4, -146],
        [-32, -136], [-54, -118], [-62, -92], [-62, -34]],
      q: [[-56, 2, 1], [-76, -40], [-90, -96], [-84, -142], [-58, -174], [-16, -190], [28, -190], [64, -174], [82, -146],
        [84, -104], [78, -60], [72, -20, 1], [66, -50], [68, -92], [62, -122], [48, -140], [30, -152, 1], [8, -146],
        [-14, -136], [-34, -118], [-42, -90], [-42, -36]],
      side: [[-22, 6, 1], [-54, -34], [-88, -84], [-92, -132], [-66, -170], [-26, -188], [16, -190], [52, -176], [72, -152],
        [80, -128], [74, -112], [66, -120, 1], [54, -136], [38, -146], [26, -150], [12, -146], [2, -134, 1], [-6, -110],
        [-10, -80], [-6, -50], [-4, -24], [-10, -6]]
    },
    hairUp: {
      front: [[-72, -78, 1], [-78, -100], [-78, -128], [-70, -152], [-48, -172], [-16, -184], [20, -184], [50, -172], [72, -152],
        [78, -128], [78, -100], [72, -78, 1], [67, -96], [66, -116], [56, -130], [42, -142], [20, -152, 1], [-4, -146],
        [-32, -136], [-52, -120], [-64, -104], [-67, -94]],
      q: [[-56, -64, 1], [-78, -80], [-82, -120], [-76, -150], [-52, -172], [-16, -186], [24, -186], [56, -172], [72, -150],
        [78, -124], [76, -100], [70, -80, 1], [66, -98], [66, -116], [58, -130], [46, -142], [30, -152, 1], [8, -146],
        [-14, -136], [-32, -118], [-42, -96], [-48, -76]],
      side: [[-30, -50, 1], [-66, -40], [-84, -84], [-86, -130], [-62, -168], [-24, -184], [16, -186], [48, -174], [66, -152],
        [74, -130], [70, -116], [62, -124, 1], [52, -138], [40, -146], [28, -150], [14, -146], [4, -134, 1], [-4, -112],
        [-12, -92], [-16, -76], [-18, -64], [-24, -56]]
    },
    hairBack: {
      front: [[-60, -170], [-92, -120], [-102, -72], [-92, -30], [-106, 12], [-72, 56], [-36, 44], [0, 50], [36, 44], [72, 56],
        [106, 12], [92, -30], [102, -72], [92, -120], [60, -170], [0, -185]],
      q: [[-50, -172], [-88, -132], [-106, -80], [-96, -30], [-110, 16], [-80, 56], [-50, 44], [-16, 50], [18, 44], [46, 52],
        [70, 30], [68, -6], [76, -60], [68, -120], [46, -168], [-4, -184]],
      side: [[-40, -178], [-84, -150], [-104, -100], [-100, -46], [-118, 6], [-100, 50], [-76, 56], [-50, 46], [-24, 52], [-2, 40],
        [8, 10], [14, -20], [20, -70], [30, -120], [20, -160], [-10, -182]]
    },
    torso: {
      front: [[-30, -212], [-74, -198], [-86, -170], [-76, -110], [-62, -50], [-72, 26, 1], [-34, 32], [0, 34], [34, 32], [72, 26, 1],
        [62, -50], [76, -110], [86, -170], [74, -198], [30, -212], [0, -192]],
      q: [[-22, -213], [-66, -198], [-78, -168], [-68, -110], [-56, -50], [-66, 26, 1], [-30, 32], [2, 34], [34, 32], [68, 26, 1],
        [60, -50], [74, -110], [78, -166], [64, -198], [28, -213], [6, -194]],
      side: [[-18, -214], [-48, -196], [-56, -164], [-52, -110], [-46, -50], [-56, 26, 1], [-26, 32], [0, 34], [30, 32], [60, 26, 1],
        [50, -50], [64, -110], [56, -160], [42, -196], [22, -214], [5, -198]]
    },
    torsoShade: {
      front: [[54, 30], [72, 26], [62, -50], [76, -110], [82, -150], [64, -116], [50, -56], [46, -10]],
      side: [[-34, 30], [-56, 26], [-46, -50], [-52, -110], [-54, -156], [-40, -116], [-32, -56], [-32, -10]]
    },
    hips: {
      front: [[-60, -8], [-68, 24], [-50, 48], [0, 52], [50, 48], [68, 24], [60, -8], [0, -12]],
      q: [[-54, -8], [-62, 24], [-44, 49], [-2, 53], [42, 48], [62, 24], [56, -8], [0, -12]],
      side: [[-46, -8], [-52, 24], [-38, 50], [-6, 54], [28, 48], [50, 24], [46, -8], [0, -12]]
    },
    shoe: {
      front: [[-20, -6], [-21, 8], [-26, 20], [-25, 30, 1], [25, 30, 1], [26, 20], [21, 8], [20, -6]],
      q: [[-20, -6], [-22, 9], [-25, 20], [-24, 30, 1], [50, 30, 1], [52, 20], [34, 8], [20, -6]],
      side: [[-20, -6], [-22, 10], [-24, 20], [-24, 30, 1], [66, 30, 1], [68, 20], [44, 7], [20, -6]]
    },
    sole: {
      front: [[-26, 26, 1], [-27, 38, 1], [27, 38, 1], [26, 26, 1]],
      q: [[-25, 26, 1], [-25, 38, 1], [54, 38, 1], [52, 26, 1]],
      side: [[-25, 26, 1], [-25, 38, 1], [70, 38, 1], [68, 26, 1]]
    }
  };
  function shape(name, t) {
    const S = SHAPE[name];
    if (!S.q) return S.front.map((p, i) => [lerp(p[0], S.side[i][0], t), lerp(p[1], S.side[i][1], t), p[2]]);
    return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
  }

  /* ---------- Expressões ---------- */
  const EXPRESSION_BASE = {
    browY: 0, browTilt: 0, browArch: 4, browSkew: 0, eyeOpen: 0.82, eyeLow: 0.9, eyeSkew: 0, lidTilt: 0, pupil: 1,
    mouthW: 22, mouthOpen: 0, smile: 0.22, teeth: 0, grit: 0, tongue: 0, skew: 0, mouthShift: 0,
    tint: 0, sweat: 0, tear: 0, exGx: 0, exGy: 0, tilt: 0
  };
  const EXPRESSIONS = {
    neutral: {},
    happy: { browY: -6, browArch: 6, eyeOpen: 0.84, eyeLow: 0.6, mouthW: 31, mouthOpen: 18, smile: 1, teeth: 1, tongue: 0.4, tint: 0.1 },
    worried: { browY: -6, browTilt: 11, eyeOpen: 1.02, lidTilt: -0.22, mouthW: 18, mouthOpen: 4, smile: -0.45, teeth: 0.6, sweat: 0.5, exGx: -0.2 },
    shocked: { browY: -15, browTilt: 4, browArch: 5, eyeOpen: 1.28, eyeLow: 1.18, pupil: 0.62, mouthW: 17, mouthOpen: 34, smile: 0, teeth: 0.3, tongue: 0.6 },
    angry: { browY: 10, browTilt: -13, browArch: 1, eyeOpen: 0.78, lidTilt: 0.5, pupil: 0.82, mouthW: 26, mouthOpen: 12, smile: -0.55, teeth: 1, grit: 1, tint: 0.75 },
    skeptical: { browY: 1, browTilt: -2, browArch: 3, browSkew: 13, eyeOpen: 0.72, eyeSkew: 0.2, lidTilt: 0.15, mouthW: 20, smile: 0.1, skew: 0.8, mouthShift: 6, exGx: 0.45, tilt: -4 },
    thinking: { browY: -3, browTilt: 4, browSkew: 6, eyeOpen: 0.86, exGx: 0.6, exGy: -0.75, mouthW: 12, smile: -0.05, skew: 0.3, mouthShift: 8, tilt: 3 },
    determined: { browY: 6, browTilt: -8, browArch: 2, eyeOpen: 0.88, lidTilt: 0.22, mouthW: 22, smile: 0.12, skew: 0.35 },
    sad: { browY: -2, browTilt: 13, eyeOpen: 0.64, lidTilt: -0.4, exGy: 0.5, mouthW: 18, smile: -0.7, tear: 1 },
    reassuring: { browY: -4, browTilt: 6, browArch: 6, eyeOpen: 0.78, eyeLow: 0.62, lidTilt: -0.12, mouthW: 27, smile: 0.85, tilt: 5, tint: 0.08 }
  };
  Object.keys(EXPRESSIONS).forEach(k => { EXPRESSIONS[k] = Object.assign({}, EXPRESSION_BASE, EXPRESSIONS[k]); });

  /* Bocas de fala para sincronização labial. Sobrepõem a boca da expressão. */
  const VISEMES = {
    rest: { mouthW: 20, mouthOpen: 0, smile: 0.1, teeth: 0, tongue: 0 },
    A: { mouthW: 22, mouthOpen: 26, smile: 0, teeth: 0.5, tongue: 0.5 },
    E: { mouthW: 26, mouthOpen: 12, smile: 0.4, teeth: 1, tongue: 0.2 },
    I: { mouthW: 27, mouthOpen: 6, smile: 0.5, teeth: 1, tongue: 0 },
    O: { mouthW: 14, mouthOpen: 22, smile: 0, teeth: 0.1, tongue: 0.4 },
    U: { mouthW: 10, mouthOpen: 10, smile: 0, teeth: 0, tongue: 0 },
    M: { mouthW: 19, mouthOpen: 0, smile: 0, teeth: 0, tongue: 0 },
    F: { mouthW: 21, mouthOpen: 5, smile: 0.1, teeth: 1, tongue: 0 }
  };

  /* ---------- Poses ----------
     r = direita da personagem (lado próximo no perfil), l = esquerda.
     u/f/h = ombro, cotovelo, punho. fl = comprimento visível do antebraço (perspectiva).
     t/s/foot = quadril, joelho, tornozelo. ty/sy = encurtamento da coxa e da canela.
     r0..r3 = dobra dos dedos, r4 = abertura do polegar. plant = pé apoiado no chão.
     farFront = braço distante continua à frente do tronco no 3/4. */
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
    rootX: 0, rootY: BASE_ROOT, rootR: 0, spine: 0, shrug: 0, head: 0, headY: 0,
    ru: 6, rf: -8, rh: 0, rfl: 1, lu: -6, lf: 8, lh: 0, lfl: 1,
    rt: 2, rs: -2, rfoot: 0, rty: 1, rsy: 1, lt: -2, ls: 2, lfoot: 0, lty: 1, lsy: 1,
    gx: 0, gy: 0, plant: 0, farFront: 1, seat: 0
  }, hands('relaxed', 'relaxed'));
  const SIDE_BASE = { ru: 2, rf: -12, lu: -3, lf: -12, rt: -4, rs: 4, lt: 5, ls: 1 };
  const pose = (front, side, quarter, extra) => {
    const shared = extra || {};
    const out = {
      front: Object.assign({}, POSE_BASE, shared, front),
      side: Object.assign({}, POSE_BASE, SIDE_BASE, shared, side)
    };
    out.q = Object.assign(lerpDict(out.front, out.side, 0.5), quarter);
    return out;
  };
  const POSES = {
    idle: pose(
      { rootX: 4, rootR: 0.5, spine: -1.4, head: 2, ru: 7, rf: -36, rh: -8, lu: -7, lf: 36, lh: 8, rt: 5, rs: -5, lt: -3, ls: 3 },
      { spine: -1, ru: 4, rf: -44, lu: 8, lf: -50 },
      { ru: 2, rf: -44, lu: -8, lf: 30 }),
    standing: pose({}, {}, {}, { farFront: 0 }),
    explaining: pose(
      { spine: 1, head: -3, ru: 18, rf: 88, rh: 8, lu: -12, lf: 58, lh: -8, gx: -0.25 },
      { spine: 2, head: 2, ru: -32, rf: -60, rh: -8, lu: -14, lf: -46, lh: -8 },
      { spine: 1.5, head: 0, ru: 8, rf: -84, rh: -6, lu: -24, lf: -44, lh: -10, gx: 0.3 }, Object.assign(hands('open', 'open'), { farFront: 0 })),
    pointing: pose(
      { spine: -3, head: 6, lu: -84, lf: -6, ru: 34, rf: -72, rh: -20, gx: 0.8, gy: -0.1 },
      { spine: 2, head: -2, lu: -84, lf: -8, lh: -4, ru: 6, rf: -18, gx: 0.8 },
      { spine: 0, head: 2, lu: -84, lf: -6, ru: 16, rf: -50, gx: 0.6 }, Object.assign(hands('relaxed', 'point'), { farFront: 0 })),
    arms_crossed: pose(
      { head: 1, ru: 0, rf: -96, rh: 4, lu: 0, lf: 84, lh: -4 },
      { ru: 4, rf: -100, rfl: 0.34, rh: 22, lu: -2, lf: -92, lfl: 0.32 },
      { ru: 0, rf: -100, rfl: 0.95, lu: -2, lf: 88, lfl: 0.85 }),
    hands_on_hips: pose(
      { ru: 36, rf: -72, rh: -20, lu: -36, lf: 72, lh: 20 },
      { ru: 34, rf: -68, rh: -10, lu: 36, lf: -66, lh: -10 },
      { ru: 34, rf: -72, rh: -18, lu: -28, lf: 70, lh: 18 }, hands('open', 'open')),
    thinking: pose(
      { head: -3, headY: 8, ru: -14, rf: -141, rh: 4, rfl: 1.05, lu: -6, lf: 96, lh: -4 },
      { head: -2, headY: 8, ru: -24, rf: -147, rh: 4, rfl: 1.05, lu: -2, lf: -86, lfl: 0.7 },
      { head: -2, headY: 8, ru: -14, rf: -141, rh: 4, rfl: 1.05, lu: -8, lf: 92, lfl: 0.85 }),
    worried: pose(
      { shrug: 0.6, spine: 1, headY: 4, ru: 12, rf: -140, rh: 10, lu: -12, lf: 140, lh: -10 },
      { shrug: 0.6, spine: 4, head: 6, headY: 4, ru: -14, rf: -118, lu: -22, lf: -112 },
      { shrug: 0.6, spine: 2, head: 3, headY: 4, ru: 6, rf: -136, rh: 8, lu: -10, lf: 126, lh: -8 }, hands('grip', 'grip')),
    sitting: pose(
      { rootY: 130, ru: 14, rf: -46, rh: -6, lu: -14, lf: 46, lh: 6, rt: 6, rs: -6, lt: -6, ls: 6, rty: 0.2, lty: 0.2 },
      { rootX: -44, spine: -2, ru: -12, rf: -52, lu: -22, lf: -44, rt: -88, rs: 88, lt: -82, ls: 84 },
      { rootX: -24, ru: -8, rf: -50, lu: -12, lf: 7, lfl: 0.73, rt: -70, rs: 70, rty: 0.72, lt: -64, ls: 64, lty: 0.72 }, { plant: 1, seat: 1 }),
    shrugging: pose(
      { shrug: 1, head: 4, ru: 8, rf: 86, rh: 24, lu: -8, lf: -86, lh: -24 },
      { shrug: 1, head: -4, ru: 8, rf: -80, rfl: 0.6, rh: -40, lu: -6, lf: -70, lfl: 0.7, lh: -40 },
      { shrug: 1, ru: 6, rf: 78, rfl: 0.8, rh: 20, lu: -14, lf: -74, lfl: 0.9, lh: -20 }, Object.assign(hands('open', 'open'), { farFront: 0 })),
    walking: pose({ spine: 1 }, { spine: 3, rf: -18, lf: -18 }, { spine: 2, rf: -14, lf: -14 }, { plant: 1, farFront: 0 }),
    running: pose(
      { spine: 2, ru: 30, rf: -110, lu: -30, lf: 110 },
      { spine: 9, head: -7, ru: 20, rf: -88, lu: -20, lf: -88 },
      { spine: 7, head: -6, rf: -96, lf: -92 }, Object.assign(hands('fist', 'fist'), { farFront: 0 })),
    comforting: pose(
      { spine: -3, head: 6, headY: 3, lu: -66, lf: -16, lh: 6, ru: 8, rf: -132, rh: 8, gx: 0.6 },
      { spine: 5, head: 5, headY: 3, lu: -68, lf: -14, ru: 2, rf: -112, rfl: 0.72, rh: 6, gx: 0.6 },
      { spine: 3, head: 5, headY: 3, lu: -68, lf: -14, ru: 6, rf: -128, gx: 0.5 }, Object.assign(hands('open', 'open'), { farFront: 0 }))
  };

  /* Ciclos. view: 0 frente, 0.5 três quartos, 1 perfil. */
  const POSE_MOTION = {
    walking(j, ph, view) {
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
    },
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
        j.rootY = BASE_ROOT + (quarter ? 14 : 24) - (quarter ? 20 : 24) * Math.abs(c);
      } else {
        const lr = Math.max(0, s), ll = Math.max(0, -s);
        j.rty = 1 - 0.62 * lr; j.lty = 1 - 0.62 * ll;
        j.rsy = 1 - 0.1 * lr; j.lsy = 1 - 0.1 * ll;
        j.rootY = BASE_ROOT + 14 - 20 * Math.abs(c);
        j.rootR = 2 * s; j.spine += 2.5 * s; j.head -= 2 * s;
        j.ru += 6 * s; j.lu += 6 * s; j.rf += 18 * s; j.lf += 18 * s;
      }
    }
  };
  const MOTION_RATE = { walking: 6.2, running: 11 };
  const STILL_PHASE = { walking: 0.9, running: 0.9 };

  const SWAP = [['ru', 'lu', -1], ['rf', 'lf', -1], ['rh', 'lh', -1], ['rfl', 'lfl', 1], ['rt', 'lt', -1], ['rs', 'ls', -1],
    ['rfoot', 'lfoot', -1], ['rty', 'lty', 1], ['rsy', 'lsy', 1], ['r0', 'l0', 1], ['r1', 'l1', 1],
    ['r2', 'l2', 1], ['r3', 'l3', 1], ['r4', 'l4', 1]];
  function mirror(p) {
    const o = Object.assign({}, p);
    SWAP.forEach(([a, b, s]) => { o[a] = p[b] * s; o[b] = p[a] * s; });
    ['rootX', 'rootR', 'spine', 'head', 'gx'].forEach(k => { o[k] = -p[k]; });
    return o;
  }

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

  const ANIMATIONS = ['none', 'idle', 'talk', 'nod', 'shake', 'wave', 'tremble'];
  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const ACCESSORIES = ['watch', 'badge', 'seat', 'shadow'];
  const ANIMATE = {
    idle(j, t, w) {
      j.spine += 0.8 * Math.sin(t * 1.1) * w;
      j.head += 1.8 * Math.sin(t * 0.7 + 1) * w;
      j.headY += 1 * Math.sin(t * 0.9) * w;
      j.ru += 1.1 * Math.sin(t * 1.3) * w;
      j.lu -= 1.1 * Math.sin(t * 1.15 + 0.5) * w;
      j.rh += 3 * Math.sin(t * 1.7) * w;
      j.lh -= 3 * Math.sin(t * 1.5 + 1) * w;
    },
    nod(j, t, w) { j.headY += (4 + 4 * Math.sin(t * 7)) * w; j.spine += 0.7 * Math.sin(t * 7) * w; },
    shake(j, t, w) { j.head += 6 * Math.sin(t * 8) * w; j.gx += 0.5 * Math.sin(t * 8) * w; },
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
      j.rootX += 1.6 * s * w; j.spine += 0.5 * c * w; j.head += 0.8 * c * w;
      j.ru += 1.5 * c * w; j.lu += 1.5 * s * w; j.rh += 3 * s * w; j.lh += 3 * c * w;
    }
  };

  /* ---------- DOM ---------- */
  const NS = 'http://www.w3.org/2000/svg';
  let instanceCount = 0;
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

  class MiaRivera {
    constructor(target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: 'standing', animation: 'idle', direction: 'front', outfit: 'casual', seed: 11, autoStart: true }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('MiaRivera: elemento de destino não encontrado.');
      instanceCount += 1;
      this.prefix = opt.idPrefix || (instanceCount === 1 ? 'mia' : 'mia' + instanceCount);
      this.random = rng(opt.seed);
      this.time = 0;
      this.turn = this._dir(opt.direction);
      this.turnFrom = this.turn; this.turnTo = this.turn; this.turnP = 1; this.turnDur = 1;
      this.poseMix = new Mixer(this._check(opt.pose, POSES, 'Pose'));
      this.exprMix = new Mixer(this._check(opt.expression, EXPRESSIONS, 'Expressão'));
      this.anims = [{ name: this._anim(opt.animation), w: 1 }];
      this.breathing = true; this.blinking = true;
      this.talking = 0; this.talkTarget = 0;
      this.look = null; this.gaze = { x: 0, y: 0, tx: 0, ty: 0, next: 1.5 };
      this.nextBlink = 1.4; this.blinkT = -1;
      this.accessories = { watch: true, badge: true, seat: false, shadow: true };
      this.visible = true; this.alpha = 1;
      this.arms = { r: { w: 0, on: false, v: null }, l: { w: 0, on: false, v: null } };
      this.viseme = { name: 'rest', w: 0, on: false, dur: 80 };
      this.hairSwing = 0; this.hairVel = 0;
      if (!OUTFITS[opt.outfit]) throw new Error('MiaRivera: figurino desconhecido "' + opt.outfit + '". Use: ' + Object.keys(OUTFITS).join(', '));
      this.outfit = opt.outfit;
      this.hairStyle = opt.hair || OUTFITS[opt.outfit].hair;
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
    /* Troca o figurino. O uniforme prende o cabelo; setHair depois disso muda a escolha. */
    setOutfit(name, o) {
      if (!OUTFITS[name]) throw new Error('MiaRivera: figurino desconhecido "' + name + '". Use: ' + Object.keys(OUTFITS).join(', '));
      this.outfit = name;
      this.hairStyle = (o && o.hair) || OUTFITS[name].hair;
      return this._after();
    }
    setHair(style) {
      if (style !== 'down' && style !== 'up') throw new Error('MiaRivera: penteado desconhecido "' + style + '". Use: down, up');
      this.hairStyle = style;
      return this._after();
    }
    /* Controla um braço sem depender da pose. Ângulos em graus; null devolve à pose. */
    setArm(side, values) {
      const k = side === 'right' ? 'r' : side === 'left' ? 'l' : null;
      if (!k) throw new Error('MiaRivera: braço desconhecido "' + side + '". Use: right, left');
      if (values && values.hand && !HANDS[values.hand]) throw new Error('MiaRivera: mão desconhecida "' + values.hand + '". Use: ' + Object.keys(HANDS).join(', '));
      const a = this.arms[k];
      a.on = !!values;
      if (values) a.v = Object.assign({ shoulder: 0, elbow: 0, wrist: 0 }, values);
      return this._after();
    }
    /* Sincronização labial: rest, A, E, I, O, U, M, F. null devolve a boca à expressão. */
    setViseme(name, o) {
      if (name !== null && !VISEMES[name]) throw new Error('MiaRivera: visema desconhecido "' + name + '". Use: ' + Object.keys(VISEMES).join(', '));
      this.viseme.on = name !== null;
      if (name !== null) this.viseme.name = name;
      this.viseme.dur = this._ms(o, 80);
      if (this.viseme.dur <= 0) this.viseme.w = name !== null ? 1 : 0;
      return this._after();
    }
    setBreathing(on) { this.breathing = !!on; return this; }
    setBlinking(on) { this.blinking = !!on; return this; }
    setTalking(on) { this.talkTarget = on ? 1 : 0; return this; }
    /* Direção do olhar de -1 a 1; sem argumentos, volta ao olhar automático. */
    lookAt(x, y) { this.look = x === undefined ? null : { x: clamp(x, -1, 1), y: clamp(y || 0, -1, 1) }; return this._after(); }
    blink() { this.blinkT = 0; return this; }
    setAccessory(name, on) {
      if (!ACCESSORIES.includes(name)) throw new Error('MiaRivera: acessório desconhecido "' + name + '". Use: ' + ACCESSORIES.join(', '));
      this.accessories[name] = !!on;
      return this._after();
    }
    getState() {
      return {
        expression: this.exprMix.name, pose: this.poseMix.name, animation: this.animation,
        direction: Object.keys(DIRECTIONS).find(k => DIRECTIONS[k] === this.turnTo) || 'custom', turn: this.turnTo,
        outfit: this.outfit, hair: this.hairStyle, visible: this.visible, accessories: Object.assign({}, this.accessories)
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
      this._updateAnims(dtMs);
      this.talking = lerp(this.talking, this.talkTarget, clamp(dt * 12));
      ['r', 'l'].forEach(k => { const a = this.arms[k]; a.w = clamp(a.w + (a.on ? 1 : -1) * dtMs / 260); });
      const v = this.viseme;
      if (v.dur > 0) v.w = clamp(v.w + (v.on ? 1 : -1) * dtMs / v.dur);
      const target = this.visible ? 1 : 0;
      this.alpha += clamp(target - this.alpha, -dtMs / 200, dtMs / 200);
      this._render(this._blinkAmount(dt), dt);
      return this;
    }

    /* ---------- Internos ---------- */
    _check(name, table, label) {
      if (!table[name]) throw new Error('MiaRivera: ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (!ANIMATIONS.includes(name)) throw new Error('MiaRivera: animação desconhecida "' + name + '". Use: ' + ANIMATIONS.join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error('MiaRivera: direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
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
    _sampleJoints(st) {
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const get = name => {
        const P = POSES[name];
        const a = Object.assign({}, P.front), q = Object.assign({}, P.q), b = Object.assign({}, P.side);
        const motion = POSE_MOTION[name];
        if (motion) {
          const ph = live ? this.time * MOTION_RATE[name] : STILL_PHASE[name];
          motion(a, ph, 0); motion(q, ph, 0.5); motion(b, ph, 1);
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
          return M.hipY + M.thigh * j[k + 'ty'] * Math.cos(a) + M.shin * j[k + 'sy'] * Math.cos(b) + M.footH;
        };
        j.rootY = lerp(j.rootY, FLOOR - Math.max(reach('r'), reach('l')), j.plant);
      }
      const talk = this.animation === 'talk' ? 1 : this.talking;
      if (talk > 0.01) {
        j.head += 1.6 * Math.sin(this.time * 5.3) * talk;
        j.headY += 1.6 * Math.abs(Math.sin(this.time * 4.1)) * talk;
      }
      ['r', 'l'].forEach(k => {
        const a = this.arms[k];
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
    _mouthFlap() {
      const w = this.animation === 'talk' ? 1 : this.talking;
      if (w < 0.01) return 0;
      const t = this.time;
      return Math.abs(Math.sin(t * 13.1) * 0.6 + Math.sin(t * 7.3 + 1) * 0.4) * w;
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
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'mia-rig', role: 'img', 'aria-label': 'Mia Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = n('defs', {}, svg);
      this.clipEyeR = n('path', {}, n('clipPath', { id: u + '-clip-eye-right' }, defs));
      this.clipEyeL = n('path', {}, n('clipPath', { id: u + '-clip-eye-left' }, defs));
      this.clipMouth = n('path', {}, n('clipPath', { id: u + '-clip-mouth' }, defs));

      this.shadow = n('ellipse', { cx: 0, cy: FLOOR + 4, rx: 130, ry: 15, fill: '#000', 'fill-opacity': 0.22 }, svg, 'shadow');
      this.flip = n('g', {}, svg, 'character');
      this._buildSeat(this.flip);

      const rig = this.rig = n('g', {}, this.flip, 'pelvis', PIVOTS.pelvis);
      this.spineNodes = [];
      const layer = name => { const g = n('g', {}, rig, name, PIVOTS.torso); this.spineNodes.push(g); return g; };

      this.backArmLayer = layer('layer-back-arm');
      this.hipsO = n('path', Object.assign({}, outlineStyle), rig);
      this.legL = this._buildLeg(rig, 'l', 'left');
      this.legR = this._buildLeg(rig, 'r', 'right');
      this.hipsF = n('path', {}, rig, 'hips');

      const hairBackLayer = layer('layer-hair-back');
      this.hairBackGroup = n('g', {}, hairBackLayer);
      this.hairBack = n('path', Object.assign({ fill: C.hairDeep }, lineStyle), this.hairBackGroup, 'hair-back');
      this.bun = n('g', {}, this.hairBackGroup, 'hair-bun');
      n('circle', Object.assign({ r: 31, fill: C.hair }, lineStyle), this.bun);
      n('path', { d: 'M-16 -8Q0 -22 16 -10M-14 8Q2 -4 18 6', fill: 'none', stroke: C.hairShine, 'stroke-width': 4, 'stroke-linecap': 'round' }, this.bun);

      const neck = this.neck = n('g', {}, layer('layer-neck'), 'neck');
      n('path', Object.assign({ d: capsule(62, 21, 24), fill: C.skin }, lineStyle), neck);
      n('path', { d: 'M-19 2H19V14Q0 24 -19 14Z', fill: C.skinShade }, neck);

      const torso = layer('torso');
      this.torsoShape = n('path', Object.assign({}, lineStyle), torso, 'torso-shape');
      this.torsoShade = n('path', {}, torso, 'torso-shade');
      this.wrinkles = n('path', { fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, torso);
      this.collar = n('path', { fill: 'none', 'stroke-width': 7, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, torso, 'collar');
      this.pocket = n('path', { fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, torso, 'pocket');
      this._buildBadge(torso);

      this._buildHead(layer('layer-head'));

      this.frontArmLayer = layer('layer-front-arm');
      this.armL = this._buildArm(this.frontArmLayer, 'l', 'left');
      this.armR = this._buildArm(this.frontArmLayer, 'r', 'right');
      this.armLParent = this.frontArmLayer;
    }
    _buildLeg(parent, k, side) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'leg-' + side, k === 'r' ? PIVOTS.hipRight : PIVOTS.hipLeft);
      const leg = { root: g, thigh: [], shin: [], foot: [], thighPaths: [], shinPaths: [], fills: [], k };
      ['o', 'f'].forEach(pass => {
        const isF = pass === 'f';
        const style = isF ? {} : outlineStyle;
        const passG = n('g', {}, g);
        const thigh = n('g', {}, passG, isF ? 'thigh-' + side : null);
        const tp = n('path', Object.assign({}, style), thigh);
        const shin = n('g', {}, thigh, isF ? 'shin-' + side : null, PIVOTS.knee);
        const sp = n('path', Object.assign({}, style), shin);
        const foot = n('g', {}, shin, isF ? 'foot-' + side : null, PIVOTS.ankle);
        leg.thigh.push(thigh); leg.shin.push(shin); leg.foot.push(foot);
        leg.thighPaths.push(tp); leg.shinPaths.push(sp);
        if (!isF) {
          leg.shoeO = n('path', Object.assign({}, outlineStyle), foot);
          leg.soleO = n('path', Object.assign({}, outlineStyle), foot);
        } else {
          leg.fills.push(tp, sp);
          leg.thighShade = n('path', { d: capsule(112, 6.5, 5.5) }, thigh);
          leg.shinShade = n('path', { d: capsule(104, 5.5, 5.5) }, shin);
          leg.knee = n('path', { d: 'M-12 -3Q0 7 12 -3', fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, shin);
          leg.shoe = n('path', {}, foot);
          leg.stripe = n('path', { fill: 'none', 'stroke-width': 4.5, 'stroke-linecap': 'round' }, foot);
          leg.laces = n('path', { fill: 'none', stroke: C.metalDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, foot);
          leg.sole = n('path', {}, foot);
          leg.cuff = n('path', { d: 'M-21 -9H21', fill: 'none', 'stroke-width': 5, 'stroke-linecap': 'round' }, foot);
        }
      });
      return leg;
    }
    _buildArm(parent, k, side) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'arm-' + side, k === 'r' ? PIVOTS.shoulderRight : PIVOTS.shoulderLeft);
      const arm = { root: g, upper: [], fore: [], hand: [], skin: [], forePaths: [], k, side };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const skin = isO ? outlineStyle : { fill: C.skin };
        const passG = n('g', {}, g);
        const upper = n('g', {}, passG, isO ? null : 'upper-arm-' + side);
        const up = n('path', Object.assign({ d: capsule(M.upperArm, 18, 16.5) }, skin), upper);
        const fore = n('g', {}, upper, isO ? null : 'forearm-' + side, PIVOTS.elbow);
        const fp = n('path', Object.assign({}, skin), fore);
        arm.forePaths.push(fp);
        const hand = n('g', {}, fore, isO ? null : 'hand-' + side, PIVOTS.wrist);
        arm.upper.push(upper); arm.fore.push(fore); arm.hand.push(hand);
        if (isO) {
          arm.sleeveO = n('path', Object.assign({}, outlineStyle), upper);
          n('path', Object.assign({ d: this._palm() }, outlineStyle), hand);
          arm.fingersO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14 + LINE, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
        } else {
          arm.skin.push(up, fp);
          arm.sleeve = n('path', {}, upper, 'sleeve-' + side);
          arm.sleeveHem = n('path', { fill: 'none', 'stroke-width': 4.5, 'stroke-linecap': 'round' }, upper);
          arm.foreShade = n('path', { fill: C.skinShade }, fore);
          if (k === 'r') {
            this.watch = n('g', { transform: 'translate(0 72)' }, fore, 'watch');
            n('rect', Object.assign({ x: -17, y: -5, width: 34, height: 10, rx: 3, fill: C.watchBand }, lineStyle, { 'stroke-width': 3 }), this.watch);
            n('circle', Object.assign({ r: 7.5, fill: C.watchFace }, lineStyle, { 'stroke-width': 3 }), this.watch);
          }
          this._buildHand(arm, hand);
        }
      });
      arm.shoulder = n('ellipse', {}, g, 'shoulder-' + side);
      return arm;
    }
    _palm() { return 'M-19 -4Q-23 16 -20 34Q0 42 20 34Q23 16 19 -4Q0 -10 -19 -4Z'; }
    _buildHand(arm, hand) {
      const n = this._n.bind(this);
      arm.fingerGroup = n('g', {}, hand, 'fingers-' + arm.side);
      arm.fingers = [0, 1, 2, 3].map(() => ({
        o: n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 12.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, arm.fingerGroup),
        f: n('path', { fill: 'none', stroke: C.skin, 'stroke-width': 8.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, arm.fingerGroup)
      }));
      arm.palm = n('path', { d: this._palm(), fill: C.skin }, hand, 'palm-' + arm.side);
      arm.thumbO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.thumbF = n('path', { fill: 'none', stroke: C.skin, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.fingersOnTop = false;
    }
    _buildBadge(parent) {
      const n = this._n.bind(this);
      const b = this.badge = n('g', {}, parent, 'badge');
      n('rect', { x: -5, y: -10, width: 10, height: 12, rx: 2, fill: C.clip, stroke: C.ink, 'stroke-width': 2.5 }, b);
      n('rect', Object.assign({ x: -15, y: 0, width: 30, height: 38, rx: 3, fill: C.badge }, lineStyle, { 'stroke-width': 3 }), b);
      n('rect', { x: -13, y: 2, width: 26, height: 8, fill: C.badgeStripe }, b);
      n('circle', { cx: 0, cy: 19, r: 6, fill: C.skinShade }, b);
      n('path', { d: 'M-8 32H8', stroke: C.metalDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, b);
    }
    _buildSeat(parent) {
      const n = this._n.bind(this);
      const seat = this.seatProp = n('g', {}, parent, 'seat');
      n('rect', Object.assign({ x: -70, y: 192, width: 140, height: 22, rx: 6, fill: C.wood }, lineStyle), seat);
      n('path', Object.assign({ d: 'M-58 214L-70 340H-54L-38 214Z', fill: C.woodDark }, lineStyle), seat);
      n('path', Object.assign({ d: 'M58 214L70 340H54L38 214Z', fill: C.woodDark }, lineStyle), seat);
      n('path', Object.assign({ d: 'M-60 282H60V295H-60Z', fill: C.wood }, lineStyle), seat);
    }
    _buildHead(parent) {
      const n = this._n.bind(this), u = this.prefix;
      const head = this.head = n('g', {}, parent, 'head', PIVOTS.head);
      this.earBack = n('g', {}, head, 'ears-back');
      this.earFar = this._ear(this.earBack);
      this.earNear = this._ear(this.earBack);
      this.headShape = n('path', Object.assign({ fill: C.skin }, lineStyle), head, 'face');
      this.headShade = n('path', { fill: C.skinShade, 'fill-opacity': 0.7 }, head);
      this.tint = n('path', {}, head, 'tint');
      this.mole = n('circle', { r: 2.6, fill: C.mole }, head, 'mole');

      const mouth = this.mouth = n('g', {}, head, 'mouth');
      this.mouthShape = n('path', Object.assign({ fill: C.mouth }, lineStyle), mouth);
      const inner = n('g', { 'clip-path': 'url(#' + u + '-clip-mouth)' }, mouth);
      this.tongue = n('ellipse', { fill: C.tongue }, inner);
      this.teeth = n('rect', { fill: C.teeth, x: -60, width: 120 }, inner);
      this.gritLines = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 2.5 }, inner);
      this.mouthLine = n('path', Object.assign({ fill: 'none' }, lineStyle), mouth);
      this.lowerLip = n('path', { fill: 'none', stroke: C.lip, 'stroke-width': 4, 'stroke-linecap': 'round' }, mouth, 'lower-lip');

      this.eyeR = this._eye(head, 'right', u + '-clip-eye-right');
      this.eyeL = this._eye(head, 'left', u + '-clip-eye-left');
      this.noseFill = n('ellipse', { fill: C.skin }, head, 'nose');
      this.noseLine = n('path', Object.assign({ fill: 'none' }, lineStyle, { 'stroke-width': 4 }), head);
      this.hairFront = n('path', Object.assign({ fill: C.hair }, lineStyle), head, 'hair-front');
      this.hairShine = n('path', { fill: 'none', stroke: C.hairShine, 'stroke-width': 7, 'stroke-linecap': 'round' }, head);
      this.hairWave = n('path', { fill: 'none', stroke: C.hairShine, 'stroke-width': 4, 'stroke-linecap': 'round' }, head, 'hair-wave');
      const browStyle = { fill: 'none', stroke: C.brow, 'stroke-width': 8.5, 'stroke-linecap': 'round' };
      this.browR = n('path', browStyle, head, 'brow-right');
      this.browL = n('path', browStyle, head, 'brow-left');
      this.earTop = n('g', {}, head, 'ears-top');
      this.sweat = n('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat);
      this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
    }
    _drop(parent) {
      return this._n('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
    }
    _ear(parent) {
      const g = this._n('g', {}, parent);
      this._n('path', Object.assign({ d: 'M-3 -19Q-18 -21 -16 -2Q-14 19 2 16Q8 0 -3 -19Z', fill: C.skin }, lineStyle), g);
      this._n('path', { d: 'M-5 -9Q-11 -8 -9 2', fill: 'none', stroke: C.skinShade, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, g);
      return g;
    }
    _eye(parent, side, clipId) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'eye-' + side);
      const white = n('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, g);
      const iris = n('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
      const ball = n('g', {}, iris, 'pupil-' + side);
      n('circle', { r: 13.5, fill: C.iris }, ball);
      n('circle', { r: 8.5, fill: '#120d0a' }, ball);
      n('circle', { cx: 4, cy: -5, r: 3.8, fill: '#fff' }, ball);
      const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 6, 'stroke-linecap': 'round' }, g);
      const lash = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 4, 'stroke-linecap': 'round' }, g, 'lash-' + side);
      return { g, white, ball, lid, lash };
    }

    /* ---------- Desenho de um quadro ---------- */
    _render(blink, dt) {
      const t = Math.abs(this.turn), st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const O = OUTFITS[this.outfit];
      const j = this._sampleJoints(st);
      let e = this.exprMix.sample(n => EXPRESSIONS[n]);
      if (this.viseme.w > 0) e = lerpDict(e, Object.assign({}, e, VISEMES[this.viseme.name]), ease(this.viseme.w));
      this._gaze(dt, live);

      const b = this.breathing ? Math.sin(this.time * TAU / 3.7) : 0;
      put(this.svg, 'opacity', String(Math.round(this.alpha * 100) / 100));
      put(this.svg, 'display', this.alpha <= 0.001 ? 'none' : 'inline');
      put(this.flip, 'transform', 'scale(' + sign + ' 1)');
      put(this.rig, 'transform', tf(j.rootX, j.rootY, j.rootR));
      const spineT = tf(0, 0, j.spine, 1 + b * 0.007, 1 + b * 0.011);
      this.spineNodes.forEach(g => put(g, 'transform', spineT));

      this._renderBody(st, O);
      const farTone = clamp((st - 0.5) * 2);
      this._renderLeg(this.legR, j, 'r', st, 0, O);
      this._renderLeg(this.legL, j, 'l', st, farTone, O);
      this._renderArm(this.armR, j, 'r', st, b, 0, O);
      this._renderArm(this.armL, j, 'l', st, b, farTone, O);
      this._renderHead(j, e, st, blink, dt);
      this._renderProps(j, st);

      const toBack = st > (j.farFront > 0.5 ? 0.75 : 0.3);
      if (toBack && this.armLParent !== this.backArmLayer) {
        this.backArmLayer.appendChild(this.armL.root); this.armLParent = this.backArmLayer;
      } else if (!toBack && this.armLParent !== this.frontArmLayer) {
        this.frontArmLayer.insertBefore(this.armL.root, this.frontArmLayer.firstChild); this.armLParent = this.frontArmLayer;
      }
    }
    _renderBody(st, O) {
      const hips = spline(shape('hips', st), true);
      put(this.hipsO, 'd', hips); put(this.hipsF, 'd', hips); put(this.hipsF, 'fill', O.pants);
      const pts = shape('torso', st);
      [5, 6, 7, 8, 9].forEach(i => { pts[i][1] += O.hem; });
      pts[15][1] += O.neck;
      put(this.torsoShape, 'd', spline(pts, true));
      put(this.torsoShape, 'fill', O.top);
      const shade = shape('torsoShade', st < 0.5 ? 0 : 1);
      [0, 1].forEach(i => { shade[i][1] += O.hem; });
      put(this.torsoShade, 'd', spline(shade, true));
      put(this.torsoShade, 'fill', O.topShade);
      shown(this.torsoShade, Math.abs(1 - 2 * st));
      const wx = key3(0, 8, 14, st);
      put(this.wrinkles, 'd', 'M' + f(wx - 44) + ' -26Q' + f(wx - 22) + ' -16 ' + f(wx - 6) + ' -22M' + f(wx + 46) + ' -74Q' + f(wx + 32) + ' -60 ' + f(wx + 14) + ' -62');
      put(this.wrinkles, 'stroke', O.topDark);
      put(this.neck, 'transform', tf(key3(0, 4, 6, st), M.headY + 6));

      const cx = key3(0, 4, 5, st), cw = key3(30, 26, 18, st), top = key3(-211, -212, -212, st);
      put(this.collar, 'stroke', O.topDark);
      put(this.collar, 'd', O.neck
        ? 'M' + f(cx - cw) + ' ' + f(top) + 'L' + f(cx) + ' ' + f(top + 46) + 'L' + f(cx + cw) + ' ' + f(top)
        : 'M' + f(cx - cw) + ' ' + f(top) + 'Q' + f(cx) + ' ' + f(top + 36) + ' ' + f(cx + cw) + ' ' + f(top));

      put(this.pocket, 'stroke', O.topDark);
      const px = key3(-34, -14, 22, st);
      put(this.pocket, 'd', 'M' + f(px - 16) + ' -128H' + f(px + 16) + 'V-98H' + f(px - 16) + 'Z');
      shown(this.pocket, O.badge ? 1 : 0);
      put(this.badge, 'transform', tf(key3(36, 42, 34, st), -124));
      shown(this.badge, O.badge && this.accessories.badge ? 1 : 0);
    }
    _renderLeg(leg, j, k, st, far, O) {
      const ang = j[k + 't'], knee = j[k + 's'], ank = j[k + 'foot'];
      const ty = j[k + 'ty'], sy = j[k + 'sy'];
      const hipX = k === 'r' ? key3(-34, -24, -7, st) : key3(34, 26, 8, st);
      put(leg.root, 'transform', tf(hipX, M.hipY));
      const lenT = M.thigh * ty, lenS = M.shin * sy;
      const dT = capsule(lenT, 32, 24), dS = capsule(lenS, 24, 20);
      const footX = (k === 'r' ? -4 : 4) * (1 - st);
      const fT = tf(0, 0, ang), sT = tf(0, lenT, knee), footT = tf(footX, lenS, ank);
      leg.thighPaths.forEach(p => put(p, 'd', dT));
      leg.shinPaths.forEach(p => put(p, 'd', dS));
      leg.thigh.forEach(g => put(g, 'transform', fT));
      leg.shin.forEach(g => put(g, 'transform', sT));
      leg.foot.forEach(g => put(g, 'transform', footT));

      const shoe = spline(shape('shoe', st), true), sole = spline(shape('sole', st), true);
      put(leg.shoeO, 'd', shoe); put(leg.shoe, 'd', shoe); put(leg.shoe, 'fill', O.shoe);
      put(leg.soleO, 'd', sole); put(leg.sole, 'd', sole); put(leg.sole, 'fill', O.sole);
      const lx = key3(0, 14, 24, st);
      put(leg.laces, 'd', 'M' + f(lx - 9) + ' 3H' + f(lx + 8) + 'M' + f(lx - 7) + ' 11H' + f(lx + 13));
      put(leg.stripe, 'stroke', O.stripe);
      put(leg.stripe, 'd', 'M' + f(key3(-16, -14, -12, st)) + ' 20H' + f(key3(16, 36, 52, st)));
      put(leg.cuff, 'stroke', O.pantsLight);
      const shadeOff = lerp(12, -11, st);
      put(leg.thighShade, 'transform', tf(shadeOff, 8, 0, 1, Math.max(ty, 0.05)));
      put(leg.shinShade, 'transform', tf(shadeOff, 14, 0, 1, sy));
      put(leg.thighShade, 'fill', O.pantsShade); put(leg.shinShade, 'fill', O.pantsShade);
      put(leg.knee, 'stroke', O.pantsShade);
      shown(leg.thighShade, ty > 0.4 ? 1 : 0);
      const col = far > 0.01 ? hexMix(O.pants, O.pantsShade, far * 0.85) : O.pants;
      leg.fills.forEach(p => put(p, 'fill', col));
    }
    _renderArm(arm, j, k, st, b, far, O) {
      const sx = k === 'r' ? key3(-76, -56, -8, st) : key3(76, 60, 16, st);
      const sy = M.shoulderY - j.shrug * 12 - b * 0.8;
      put(arm.root, 'transform', tf(sx, sy));
      const foreLen = M.foreArm * j[k + 'fl'];
      const uT = tf(0, 0, j[k + 'u']), fT = tf(0, M.upperArm, j[k + 'f']);
      const flip = k === 'r' ? 1 : lerp(-1, 1, smooth(clamp((st - 0.12) / 0.2)));
      const hs = Math.abs(flip) < 0.35 ? 0.35 * (flip < 0 ? -1 : 1) : flip;
      const hT = tf(0, foreLen, j[k + 'h'], hs * 0.86, 0.86);
      arm.upper.forEach(g => put(g, 'transform', uT));
      arm.fore.forEach(g => put(g, 'transform', fT));
      arm.hand.forEach(g => put(g, 'transform', hT));
      const dF = capsule(foreLen, 16.5, 13);
      arm.forePaths.forEach(p => put(p, 'd', dF));
      put(arm.foreShade, 'd', capsule(foreLen * 0.74, 4.5, 3.5));
      put(arm.foreShade, 'transform', tf(8, 8));

      const sl = O.sleeve;
      const dS = capsule(sl, 23, 21);
      put(arm.sleeveO, 'd', dS); put(arm.sleeve, 'd', dS);
      put(arm.sleeveHem, 'd', 'M-20 ' + (sl + 16) + 'H20');
      put(arm.sleeveHem, 'stroke', O.topDark);
      const sleeveCol = far > 0.01 ? hexMix(O.top, O.topShade, far) : O.top;
      put(arm.sleeve, 'fill', sleeveCol);
      const inFront = k === 'r' || this.armLParent === this.frontArmLayer;
      shown(arm.shoulder, inFront ? 1 : 0);
      put(arm.shoulder, 'fill', sleeveCol);
      put(arm.shoulder, 'cx', f((k === 'r' ? 1 : -1) * key3(12, 10, 0, st)));
      put(arm.shoulder, 'cy', f(key3(4, 0, -10, st)));
      put(arm.shoulder, 'rx', f(key3(27, 27, 28, st)));
      put(arm.shoulder, 'ry', f(key3(27, 25, 20, st)));

      const curls = [0, 1, 2, 3].map(i => j[k + i]);
      const X = [-14.5, -5, 5, 14.5];
      let all = '';
      arm.fingers.forEach((fin, i) => {
        const c = clamp(curls[i]);
        const y0 = 28, len = (i === 1 || i === 2 ? 25 : 21) * (i === 3 ? 0.92 : 1);
        const y1 = y0 + len * 0.55 * Math.cos(c * Math.PI * 0.5);
        const y2 = y1 + len * 0.5 * Math.cos(c * Math.PI * 1.05);
        const d = 'M' + X[i] + ' ' + y0 + 'L' + X[i] + ' ' + f(y1) + 'L' + X[i] + ' ' + f(y2);
        put(fin.o, 'd', d); put(fin.f, 'd', d);
        all += d;
      });
      put(arm.fingersO, 'd', all);
      const onTop = (curls[0] + curls[1] + curls[2] + curls[3]) / 4 > 0.5 || curls[1] > 0.5;
      if (onTop !== arm.fingersOnTop) {
        const handG = arm.hand[1];
        handG.insertBefore(arm.fingerGroup, onTop ? arm.thumbO : arm.palm);
        arm.fingersOnTop = onTop;
      }
      const th = clamp(j[k + '4']);
      const thumb = 'M15 8L' + f(lerp(12, 30, th)) + ' ' + f(lerp(20, 18, th)) + 'L' + f(lerp(0, 36, th)) + ' ' + f(lerp(24, 36, th));
      put(arm.thumbO, 'd', thumb); put(arm.thumbF, 'd', thumb);
      const skin = far > 0.01 ? hexMix(C.skin, C.skinShade, far * 0.6) : C.skin;
      arm.skin.forEach(p => put(p, 'fill', skin));
    }
    _renderEye(eye, clip, x, y, sx, inner, e, openMul, blink, gx, gy) {
      put(eye.g, 'transform', tf(x, y, 0, sx, 1));
      const W = 21;
      const open = Math.max(0, e.eyeOpen * openMul * (1 - blink));
      const T = 24 * open * 1.33, B = 19 * e.eyeLow * (1 - blink * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const o = inner > 0 ? -1 : 1;     // lado externo do olho
      put(eye.lash, 'd', 'M' + o * W + ' 0L' + o * (W + 8) + ' -6M' + o * (W - 4) + ' ' + f(-T * 0.3) + 'L' + o * (W + 4) + ' ' + f(-T * 0.3 - 7));
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    }
    _renderHead(j, e, st, blink, dt) {
      const headT = tf(key3(0, 5, 7, st), M.headY + j.headY - j.shrug * 8, j.head + e.tilt);
      put(this.head, 'transform', headT);
      /* O cabelo traseiro acompanha a cabeça com um pequeno atraso de mola. */
      put(this.hairBackGroup, 'transform', headT);
      const goal = clamp(-(j.spine + j.head) * 0.5 + (j.rootY - BASE_ROOT) * 0.12, -14, 14);
      for (let left = dt; left > 0; left -= 0.016) {
        const step = Math.min(left, 0.016);
        this.hairVel += ((goal - this.hairSwing) * 90 - this.hairVel * 10) * step;
        this.hairSwing += this.hairVel * step;
      }
      const flap = this._mouthFlap();
      const drop = Math.max(0, e.mouthOpen + flap * 18 - 14) * 0.62;
      const jaw = (pts, full, half) => {
        full.forEach(i => { pts[i][1] += drop; });
        half.forEach(i => { pts[i][1] += drop * 0.5; });
        return pts;
      };
      const headD = spline(jaw(shape('head', st), [0, 1, 13], [2, 12]), true);
      put(this.headShape, 'd', headD);
      put(this.headShade, 'd', spline(jaw(shape('headShade', st < 0.5 ? 0 : 1), [0, 7], [1, 6]), true));
      shown(this.headShade, Math.abs(1 - 2 * st));
      put(this.tint, 'd', headD);
      put(this.tint, 'fill', e.tint >= 0 ? '#e0392b' : '#7fb2d9');
      put(this.tint, 'opacity', String(Math.round(Math.abs(e.tint) * 26) / 100));
      put(this.noseFill, 'fill', hexMix(C.skin, e.tint >= 0 ? '#e0392b' : '#7fb2d9', Math.abs(e.tint) * 0.26));

      const down = this.hairStyle === 'down';
      const sway = this.hairSwing;
      const front = shape(down ? 'hairFront' : 'hairUp', st);
      if (down) front.forEach((p, i) => { if (p[1] > -60 && i !== 16) p[0] += sway * (p[1] + 60) / 60; });
      put(this.hairFront, 'd', spline(front, true));
      const back = shape('hairBack', st);
      back.forEach(p => { if (p[1] > -40) p[0] += sway * 1.6 * (p[1] + 40) / 90; });
      put(this.hairBack, 'd', spline(back, true));
      shown(this.hairBack, down ? 1 : 0);
      shown(this.bun, down ? 0 : 1);
      put(this.bun, 'transform', tf(key3(0, -36, -86, st), key3(-188, -184, -152, st)));
      const shine = key3(0, 10, -4, st);
      put(this.hairShine, 'd', 'M' + f(shine - 44) + ' -166Q' + f(shine - 16) + ' -178 ' + f(shine + 14) + ' -178');
      const wx = key3(-74, -60, -44, st), wr = key3(74, 74, -44, st);
      put(this.hairWave, 'd', 'M' + f(wx) + ' -82Q' + f(wx - 7) + ' -60 ' + f(wx + 2) + ' -44Q' + f(wx + 6) + ' -30 ' + f(wx + 1) + ' -16' +
        (st < 0.6 ? 'M' + f(wr) + ' -82Q' + f(wr + 7) + ' -60 ' + f(wr - 2) + ' -44Q' + f(wr - 6) + ' -30 ' + f(wr - 1) + ' -16' : ''));
      shown(this.hairWave, down ? 1 : 0);

      const gx = clamp(j.gx + e.exGx + this.gaze.x, -1, 1);
      const gy = clamp(j.gy + e.exGy + this.gaze.y, -1, 1);
      const rx = key3(-31, 6, 34, st), lx = key3(31, 54, 70, st), ey = -80;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.72, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, 1 + e.eyeSkew, blink, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx, ey, Math.max(ls, 0.06), -1, e, 1 - e.eyeSkew, blink, gx, gy);
      this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

      const nx = key3(0, 40, 68, st), ny = -50;
      const nrx = lerp(9, 11, st);
      put(this.noseFill, 'cx', f(nx)); put(this.noseFill, 'cy', ny);
      put(this.noseFill, 'rx', f(nrx)); put(this.noseFill, 'ry', 7.5);
      const aC = lerp(Math.PI / 2, 0.2, st), span = lerp(1.9, 1.5, st);
      const arc = [];
      for (let i = 0; i <= 6; i++) {
        const a = aC - span + (2 * span * i) / 6;
        arc.push([nx + Math.cos(a) * nrx, ny + Math.sin(a) * 7.5]);
      }
      put(this.noseLine, 'd', spline(arc, false));
      put(this.mole, 'cx', f(rx - 4)); put(this.mole, 'cy', -44);

      this._renderMouth(e, st, flap);

      const nearY = -70;
      put(this.earNear, 'transform', tf(lerp(-75, -18, st), nearY));
      put(this.earFar, 'transform', tf(lerp(75, 56, st), nearY, 0, -1, 1));
      shown(this.earNear, down ? 0 : 1);
      shown(this.earFar, !down && st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw > 0.04 ? 1 : 0);
      put(this.sweat1, 'transform', tf(lerp(96, 84, st), lerp(-122, -112, st), 12, 0.5 + sw * 0.5));
      put(this.sweat2, 'transform', tf(key3(-100, 92, 92, st), key3(-96, -88, -88, st), -10, 0.38 + sw * 0.38));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -52 + (this.animation === 'none' ? 0.5 : fall) * 20, 0, 0.72));
    }
    _renderBrow(el, x, inner, e, sx, skew) {
      const y = -113 + e.browY - skew;
      const w = 21 * sx;
      const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
      const cy = y - e.browArch * 2.6 - e.browTilt * 0.1;
      put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY + 2) + 'Q' + f(x - w * 0.15 * inner) + ' ' + f(cy) + ' ' + f(x + w * inner) + ' ' + f(inY));
    }
    _renderMouth(e, st, flap) {
      const open = e.mouthOpen + flap * 18;
      const w = (e.mouthW + flap * -3) * key3(1, 0.86, 0.62, st);
      const smile = e.smile, skew = e.skew;
      const lY = -smile * 11 + skew * 5, rY = -smile * 11 - skew * 5;
      put(this.mouth, 'transform', tf(key3(0, 24, 33, st) + e.mouthShift * (1 - st * 0.6), -23));
      const rnd = 0.55 + 0.42 * clamp(open / 26);
      const up = smile * 7 - Math.min(open, 22) * 0.1;
      const low = smile * 7 + open * 1.33;
      const top = 'M' + f(-w) + ' ' + f(lY) + 'C' + f(-w * rnd) + ' ' + f(up) + ' ' + f(w * rnd) + ' ' + f(up) + ' ' + f(w) + ' ' + f(rY);
      const d = top + 'C' + f(w * rnd) + ' ' + f(low) + ' ' + f(-w * rnd) + ' ' + f(low) + ' ' + f(-w) + ' ' + f(lY) + 'Z';
      const isOpen = open > 1.5;
      put(this.mouthShape, 'd', d); put(this.clipMouth, 'd', d);
      shown(this.mouthShape, isOpen ? 1 : 0);
      put(this.mouthLine, 'd', top);
      shown(this.mouthLine, isOpen ? 0 : 1);
      const ly = Math.max(up, low * 0.75) * 0.75 + 7;
      put(this.lowerLip, 'd', 'M' + f(-w * 0.42) + ' ' + f(ly + 1) + 'Q0 ' + f(ly + 4) + ' ' + f(w * 0.42) + ' ' + f(ly + 1));
      shown(this.lowerLip, isOpen ? 0 : 1);

      const band = Math.min(open * 0.42, 12) * e.teeth + (e.grit > 0.5 ? open : 0);
      put(this.teeth, 'y', f(up - 16)); put(this.teeth, 'height', f(Math.max(0, 16 + band)));
      shown(this.teeth, e.teeth > 0.02 && isOpen ? 1 : 0);
      put(this.tongue, 'cx', 0); put(this.tongue, 'cy', f(smile * 7 + open * 1.05));
      put(this.tongue, 'rx', f(w * 0.62)); put(this.tongue, 'ry', f(Math.max(0, open * 0.42)));
      shown(this.tongue, e.tongue > 0.02 && isOpen ? 1 : 0);
      const mid = (up + low) / 2 - open * 0.12;
      put(this.gritLines, 'd', e.grit > 0.5
        ? 'M' + f(-w) + ' ' + f(mid) + 'H' + f(w) + 'M' + f(-w * 0.5) + ' -30V40M0 -30V40M' + f(w * 0.5) + ' -30V40'
        : 'M0 0');
    }
    _renderProps(j, st) {
      const a = this.accessories;
      shown(this.watch, a.watch ? 1 : 0);
      shown(this.seatProp, Math.max(j.seat, a.seat ? 1 : 0));
      /* O banco acompanha o quadril: encosta nele em altura e fica sob ele em posição. */
      const seatScale = (FLOOR - (j.rootY + M.hipY + 32)) / (FLOOR - 192);
      put(this.seatProp, 'transform', 'translate(' + f(j.rootX + key3(0, -10, -26, st)) + ' ' + FLOOR + ') scale(1 ' + (Math.round(seatScale * 1000) / 1000) + ') translate(0 ' + -FLOOR + ')');
      shown(this.shadow, a.shadow ? 1 : 0);
      put(this.shadow, 'rx', f(lerp(130, 148, st) * (1 - clamp((BASE_ROOT - j.rootY) / 80) * 0.3)));
    }
  }

  MiaRivera.EXPRESSIONS = Object.keys(EXPRESSIONS);
  MiaRivera.POSES = Object.keys(POSES);
  MiaRivera.ANIMATIONS = ANIMATIONS.slice();
  MiaRivera.DIRECTIONS = Object.keys(DIRECTIONS);
  MiaRivera.ACCESSORIES = ACCESSORIES.slice();
  MiaRivera.OUTFITS = Object.keys(OUTFITS);
  MiaRivera.VISEMES = Object.keys(VISEMES);
  MiaRivera.PIVOTS = PIVOTS;
  MiaRivera.PALETTE = C;
  return MiaRivera;
});
