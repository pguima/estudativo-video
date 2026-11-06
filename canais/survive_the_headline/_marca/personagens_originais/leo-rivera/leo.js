/*!
 * LeoRivera — personagem de produção do canal Survive the Headline.
 *
 * Mesmo sistema de rig de Dan e Mia: escala, chão e peso de contorno idênticos.
 * Pose, expressão, direção e acessórios são valores aplicados a um único modelo SVG.
 *
 * Uso:
 *   const leo = new LeoRivera('#palco');
 *   leo.setExpression('confident');
 *   leo.setPose('using_phone');
 *   leo.setAnimation('idle');
 *   leo.setDirection('right');
 *   leo.setAccessory('smartphone', true);
 *   leo.setVisible(true);
 *   leo.setArm('right', { shoulder: -40, elbow: -60, hand: 'open' });  // braço avulso
 *   leo.setViseme('A');                // sincronização labial; null encerra
 *
 * Acessórios: true liga, false desliga, 'auto' devolve a decisão à pose.
 * smartphone e laptop começam em 'auto' e aparecem nas poses que os usam.
 *
 * Vídeo quadro a quadro (determinístico):
 *   const leo = new LeoRivera(el, { autoStart: false, seed: 42 });
 *   leo.tick(1000 / 30);
 *   const svg = leo.toSVG();
 *
 * CSS: toda parte tem data-part e id (#leo-head, #leo-hair-front, #leo-pupil-right...).
 * "right" e "left" são os lados do próprio personagem.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.LeoRivera = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- Paleta travada ---------- */
  const C = {
    ink: '#1b1a22', skin: '#efb995', skinShade: '#d99e78',
    hair: '#3a2519', hairShine: '#5e4130', hairDeep: '#2c1b11', brow: '#2c1b11',
    eyeWhite: '#ffffff', iris: '#5e3a20', freckle: '#c98a62',
    mouth: '#5a1c22', lip: '#d39a78', tongue: '#d9636a', teeth: '#fbf7ee', sweat: '#8fd6ff', blush: '#e8705f',
    metal: '#b9c2cc', metalDark: '#7f8a96', wood: '#a5764a', woodDark: '#7d5533',
    tee: '#e4e7ee', teeShade: '#c4cad6', string: '#eef0f5', zipper: '#c9ced8',
    device: '#ff8a1f', deviceEdge: '#3a3f4d', lens: '#0d0e13', screen: '#7fd8ff',
    laptop: '#aeb6c2', laptopDark: '#7f8896', logo: '#e9edf2',
    pack: '#c8452a', packDark: '#97321d', packStrap: '#7a2817',
    phones: '#2a2d38', phonesCup: '#ff8a1f', phonesPad: '#15161c'
  };
  const OUTFITS = {
    hoodie: {
      top: '#1b2c5a', topShade: '#14214a', topDark: '#0e1836',
      pants: '#343845', pantsShade: '#272a35', pantsLight: '#4c5163',
      shoe: '#f4f5f7', sole: '#c9ced6', stripe: '#c8452a'
    }
  };
  const LINE = 4.5;
  const VIEWBOX = '-425 -480 850 860';
  const FLOOR = 340;
  const BASE_ROOT = 2;         // Leo fica entre Mia e Dan em altura, com o mesmo chão

  const M = { shoulderY: -170, upperArm: 100, foreArm: 96, hipY: 10, thigh: 146, shin: 144, headY: -228, footH: 38 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-72, M.shoulderY], shoulderLeft: [72, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-28, M.hipY], hipLeft: [28, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
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
      front: [[0, 10], [26, 7], [48, -14], [60, -56], [64, -104], [56, -144], [30, -168], [0, -174],
        [-30, -168], [-56, -144], [-64, -104], [-60, -56], [-48, -14], [-26, 7]],
      q: [[16, 10], [42, 4], [57, -18], [63, -58], [65, -104], [56, -144], [32, -168], [-2, -175],
        [-36, -168], [-62, -140], [-70, -98], [-64, -54], [-46, -16], [-12, 8]],
      side: [[38, 10], [52, 0], [58, -22], [60, -60], [63, -104], [56, -140], [34, -168], [-4, -176],
        [-44, -166], [-70, -136], [-78, -94], [-66, -52], [-38, -18], [8, 2]]
    },
    headShade: {
      front: [[26, 7], [48, -14], [60, -56], [64, -104], [59, -104], [54, -58], [42, -20], [20, 2]],
      side: [[48, 1], [24, 5], [8, 2], [-26, -13], [-20, -25], [2, -11], [24, -8], [42, -9]]
    },
    hairFront: {
      front: [[-66, -88, 1], [-72, -118], [-82, -140, 1], [-70, -150], [-78, -176, 1], [-52, -174], [-46, -200, 1], [-20, -186], [-2, -208, 1],
        [22, -188], [44, -204, 1], [54, -176], [78, -178, 1], [72, -150], [84, -136, 1], [72, -116], [66, -88, 1], [60, -116],
        [46, -132, 1], [26, -124], [10, -140, 1], [-12, -124], [-30, -138, 1], [-46, -122], [-58, -130, 1], [-60, -106]],
      q: [[-48, -76, 1], [-66, -112], [-80, -134, 1], [-70, -150], [-76, -178, 1], [-50, -176], [-40, -202, 1], [-12, -188], [6, -208, 1],
        [30, -188], [50, -202, 1], [58, -174], [78, -172, 1], [72, -148], [80, -128, 1], [70, -114], [66, -92, 1], [60, -116],
        [50, -132, 1], [34, -124], [20, -140, 1], [0, -124], [-12, -138, 1], [-26, -122], [-36, -124, 1], [-42, -100]],
      side: [[-22, -60, 1], [-60, -52], [-92, -84, 1], [-84, -112], [-98, -140, 1], [-78, -156], [-82, -184, 1], [-50, -180], [-36, -204, 1],
        [-10, -190], [14, -204, 1], [30, -184], [56, -186, 1], [60, -162], [78, -152, 1], [68, -138], [72, -124, 1], [58, -132],
        [48, -124, 1], [36, -134], [26, -120, 1], [12, -130], [6, -108, 1], [-6, -116], [-12, -86, 1], [-18, -76]]
    },
    hairBack: {
      front: [[-40, -170], [-66, -140], [-70, -100], [-66, -70], [-56, -48], [-36, -36], [-16, -30], [0, -28], [16, -30], [36, -36],
        [56, -48], [66, -70], [70, -100], [66, -140], [40, -170], [0, -180]],
      q: [[-46, -172], [-78, -140], [-84, -100], [-80, -66], [-68, -44], [-50, -34], [-30, -34], [-10, -40], [10, -50], [24, -70],
        [30, -100], [34, -130], [34, -150], [24, -168], [8, -178], [-20, -182]],
      side: [[-40, -178], [-84, -150], [-96, -110], [-94, -70], [-80, -44], [-66, -30], [-50, -28], [-36, -40], [-24, -54], [-10, -70],
        [0, -100], [10, -130], [14, -150], [10, -168], [-6, -180], [-24, -182]]
    },
    hood: {
      front: [[-56, -196], [-54, -226], [-32, -246], [0, -250], [32, -246], [54, -226], [56, -196], [30, -188], [0, -186], [-30, -188]],
      q: [[-58, -194], [-64, -226], [-46, -246], [-14, -250], [14, -246], [34, -232], [40, -204], [24, -190], [-8, -186], [-38, -188]],
      side: [[-62, -168], [-78, -202], [-68, -232], [-40, -246], [-14, -244], [6, -230], [12, -206], [0, -190], [-30, -180], [-48, -168]]
    },
    torso: {
      front: [[-28, -208], [-70, -198], [-82, -168], [-74, -110], [-64, -50], [-66, 30, 1], [-30, 35], [0, 36], [30, 35], [66, 30, 1],
        [64, -50], [74, -110], [82, -168], [70, -198], [28, -208], [0, -188]],
      q: [[-20, -209], [-62, -198], [-74, -166], [-66, -110], [-56, -50], [-58, 30, 1], [-26, 35], [2, 36], [32, 35], [62, 30, 1],
        [58, -50], [66, -110], [72, -164], [60, -198], [26, -209], [6, -190]],
      side: [[-18, -210], [-46, -196], [-54, -160], [-50, -110], [-46, -50], [-48, 30, 1], [-22, 35], [0, 36], [28, 35], [50, 30, 1],
        [46, -50], [50, -110], [50, -160], [38, -196], [20, -210], [5, -196]]
    },
    torsoShade: {
      front: [[48, 33], [66, 30], [64, -50], [74, -110], [78, -150], [60, -116], [46, -56], [42, -10]],
      side: [[-30, 33], [-48, 30], [-46, -50], [-50, -110], [-52, -152], [-38, -116], [-30, -56], [-28, -10]]
    },
    tee: {
      front: [[-27, -206, 1], [0, -190], [27, -206, 1], [3, -92, 1], [-3, -92, 1]],
      q: [[-2, -207, 1], [22, -192], [46, -206, 1], [25, -92, 1], [19, -92, 1]],
      side: [[24, -208, 1], [36, -196], [49, -204, 1], [50, -96, 1], [45, -96, 1]]
    },
    pocketPatch: {
      front: [[-44, -48, 1], [44, -48, 1], [56, 16, 1], [-56, 16, 1]],
      q: [[-20, -48, 1], [56, -48, 1], [58, 16, 1], [-30, 16, 1]],
      side: [[0, -48, 1], [48, -48, 1], [50, 16, 1], [-6, 16, 1]]
    },
    hips: {
      front: [[-52, -8], [-58, 24], [-44, 46], [0, 50], [44, 46], [58, 24], [52, -8], [0, -12]],
      q: [[-46, -8], [-52, 24], [-40, 47], [-2, 51], [36, 46], [52, 24], [48, -8], [0, -12]],
      side: [[-40, -8], [-44, 24], [-34, 48], [-6, 52], [24, 46], [42, 24], [40, -8], [0, -12]]
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
    },
    pack: {
      front: [[-62, -192], [62, -192], [68, -24], [-68, -24]],
      q: [[-98, -186], [18, -192], [18, -24], [-106, -26]],
      side: [[-138, -176], [-48, -188], [-44, -28], [-146, -32]]
    }
  };
  function shape(name, t) {
    const S = SHAPE[name];
    if (!S.q) return S.front.map((p, i) => [lerp(p[0], S.side[i][0], t), lerp(p[1], S.side[i][1], t), p[2]]);
    return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
  }

  /* ---------- Expressões ---------- */
  const EXPRESSION_BASE = {
    browY: 0, browTilt: 0, browArch: 4, browSkew: 0, eyeOpen: 0.78, eyeLow: 0.9, eyeSkew: 0, lidTilt: 0.08, pupil: 1,
    mouthW: 21, mouthOpen: 0, smile: 0.1, teeth: 0, grit: 0, tongue: 0, skew: 0, mouthShift: 0,
    tint: 0, sweat: 0, tear: 0, blush: 0, exGx: 0, exGy: 0, tilt: 0
  };
  const EXPRESSIONS = {
    neutral: {},
    happy: { browY: -5, browArch: 6, eyeOpen: 0.84, eyeLow: 0.62, lidTilt: 0, mouthW: 30, mouthOpen: 17, smile: 1, teeth: 1, tongue: 0.4 },
    excited: { browY: -13, browArch: 6, eyeOpen: 1.16, eyeLow: 1.02, lidTilt: 0, pupil: 1.16, mouthW: 30, mouthOpen: 27, smile: 1, teeth: 1, tongue: 0.5, tint: 0.1 },
    confident: { browY: 3, browTilt: -5, browArch: 3, browSkew: 5, eyeOpen: 0.68, eyeLow: 0.8, lidTilt: 0.2, mouthW: 26, smile: 0.78, skew: 0.75, mouthShift: 5, tilt: -5 },
    skeptical: { browY: 1, browTilt: -2, browArch: 3, browSkew: 13, eyeOpen: 0.68, eyeSkew: 0.2, lidTilt: 0.15, mouthW: 19, smile: 0.05, skew: 0.8, mouthShift: 6, exGx: 0.45, tilt: -4 },
    confused: { browY: -3, browTilt: 7, browArch: 5, browSkew: -12, eyeOpen: 0.94, eyeSkew: -0.16, lidTilt: 0, mouthW: 15, mouthOpen: 5, smile: -0.25, skew: -0.7, teeth: 0.3, exGx: -0.3, tilt: 6 },
    shocked: { browY: -15, browTilt: 4, browArch: 5, eyeOpen: 1.28, eyeLow: 1.18, lidTilt: 0, pupil: 0.62, mouthW: 17, mouthOpen: 34, smile: 0, teeth: 0.3, tongue: 0.6 },
    worried: { browY: -6, browTilt: 11, eyeOpen: 1, lidTilt: -0.22, mouthW: 18, mouthOpen: 4, smile: -0.45, teeth: 0.6, sweat: 0.6, exGx: -0.2 },
    annoyed: { browY: 8, browTilt: -9, browArch: 2, eyeOpen: 0.6, lidTilt: 0.3, mouthW: 20, smile: -0.42, skew: 0.3, exGx: 0.6 },
    sarcastic: { browY: -2, browArch: 5, browSkew: 9, eyeOpen: 0.6, eyeLow: 0.86, lidTilt: 0.1, mouthW: 24, smile: 0.45, skew: -0.9, mouthShift: -5, exGx: 0.35, exGy: -0.55, tilt: 3 },
    thinking: { browY: -3, browTilt: 4, browSkew: 6, eyeOpen: 0.84, lidTilt: 0, exGx: 0.6, exGy: -0.75, mouthW: 12, smile: -0.05, skew: 0.3, mouthShift: 8, tilt: 3 },
    embarrassed: { browY: -5, browTilt: 10, eyeOpen: 0.8, lidTilt: -0.1, exGx: -0.7, exGy: 0.5, mouthW: 18, mouthOpen: 3, smile: 0.2, teeth: 0.8, skew: 0.4, blush: 1, sweat: 0.7, tilt: 4 }
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
     farFront = braço distante continua à frente do tronco no 3/4.
     pocket = mãos dentro do bolso do moletom. phoneHand / phoneChest / phoneLand / laptop = acessório pedido pela pose. */
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
    ru: 5, rf: -7, rh: 0, rfl: 1, lu: -5, lf: 7, lh: 0, lfl: 1,
    rt: 2, rs: -2, rfoot: 0, rty: 1, rsy: 1, lt: -2, ls: 2, lfoot: 0, lty: 1, lsy: 1,
    gx: 0, gy: 0, plant: 0, farFront: 1, seat: 0, pocket: 0, phoneHand: 0, phoneChest: 0, phoneLand: 0, laptop: 0
  }, hands('relaxed', 'relaxed'));
  const SIDE_BASE = { spine: 3, head: 2, ru: 2, rf: -12, lu: -3, lf: -12, rt: -4, rs: 4, lt: 5, ls: 1 };
  const SEATED_FRONT = { rootY: 130, rt: 6, rs: -6, lt: -6, ls: 6, rty: 0.2, lty: 0.2 };
  const SEATED_SIDE = { rootX: -44, spine: 2, rt: -88, rs: 88, lt: -82, ls: 84 };
  const SEATED_QUARTER = { rootX: -24, rt: -70, rs: 70, rty: 0.72, lt: -64, ls: 64, lty: 0.72 };
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
      { rootX: 4, rootR: 0.6, spine: -1.6, head: 3, ru: 7, rf: -33, rh: -6, lu: -7, lf: 33, lh: 6, rt: 5, rs: -5, lt: -3, ls: 3 },
      { spine: 4, head: 3, ru: 6, rf: -34, rfl: 0.55, lu: 2, lf: -34, lfl: 0.55 },
      { ru: 2, rf: -40, lu: -8, lf: 32, lfl: 0.85 }, Object.assign(hands('fist', 'fist'), { pocket: 1 })),
    standing: pose({}, {}, {}, { farFront: 0 }),
    using_phone: pose(
      { headY: 9, gy: 0.85, ru: -6, rf: -134, rh: -40, rfl: 0.8, lu: -5, lf: 7 },
      { spine: 6, head: 9, headY: 6, gy: 0.5, gx: 0.3, ru: -24, rf: -104, rh: -52, rfl: 0.9 },
      { head: 5, headY: 8, gy: 0.7, gx: 0.2, ru: -10, rf: -126, rh: -44, rfl: 0.85, lu: -5, lf: 7 },
      Object.assign(hands('grip', 'relaxed'), { phoneHand: 1, farFront: 0 })),
    texting: pose(
      { headY: 9, gy: 0.9, ru: -6, rf: -84, rfl: 0.6, rh: -80, lu: 6, lf: 84, lfl: 0.6, lh: 80 },
      { spine: 7, head: 10, headY: 6, gy: 0.5, gx: 0.3, ru: -12, rf: -100, rfl: 0.55, rh: -58, lu: -16, lf: -96, lfl: 0.6, lh: -58 },
      { head: 5, headY: 8, gy: 0.75, gx: 0.2, ru: -6, rf: -105, rfl: 0.57, rh: -70, lu: -8, lf: 138, lfl: 0.3, lh: 42 },
      Object.assign(hands('grip', 'grip'), { phoneChest: 1 })),
    explaining: pose(
      { spine: 1, head: -3, ru: 18, rf: 88, rh: 8, lu: -12, lf: 58, lh: -8, gx: -0.25 },
      { spine: 3, head: 2, ru: -32, rf: -60, rh: -8, lu: -14, lf: -46, lh: -8 },
      { spine: 2, head: 0, ru: 8, rf: -84, rh: -6, lu: -24, lf: -44, lh: -10, gx: 0.3 }, Object.assign(hands('open', 'open'), { farFront: 0 })),
    pointing: pose(
      { spine: -3, head: 6, lu: -84, lf: -6, ru: 8, rf: -12, gx: 0.8, gy: -0.1 },
      { spine: 3, head: -2, lu: -84, lf: -8, lh: -4, ru: 4, rf: -16, gx: 0.8 },
      { spine: 1, head: 2, lu: -84, lf: -6, ru: 8, rf: -18, gx: 0.6 }, Object.assign(hands('relaxed', 'point'), { farFront: 0 })),
    arms_crossed: pose(
      { head: 1, ru: 0, rf: -96, rh: 4, lu: 0, lf: 84, lh: -4 },
      { ru: 4, rf: -100, rfl: 0.3, rh: 22, lu: -2, lf: -92, lfl: 0.3 },
      { ru: 0, rf: -100, rfl: 0.95, lu: -2, lf: 88, lfl: 0.85 }),
    thinking: pose(
      { head: -3, headY: 8, ru: -14, rf: -146, rh: 4, rfl: 1.02, lu: -6, lf: 96, lh: -4 },
      { head: -2, headY: 8, ru: -24, rf: -150, rh: 4, rfl: 1.02, lu: -2, lf: -86, lfl: 0.7 },
      { head: -2, headY: 8, ru: -14, rf: -146, rh: 4, rfl: 1.02, lu: -8, lf: 92, lfl: 0.85 }),
    shrugging: pose(
      { shrug: 1, head: 4, ru: 8, rf: 86, rh: 24, lu: -8, lf: -86, lh: -24 },
      { shrug: 1, head: -4, ru: 8, rf: -80, rfl: 0.6, rh: -40, lu: -6, lf: -70, lfl: 0.7, lh: -40 },
      { shrug: 1, ru: 6, rf: 78, rfl: 0.8, rh: 20, lu: -14, lf: -74, lfl: 0.9, lh: -20 }, Object.assign(hands('open', 'open'), { farFront: 0 })),
    sitting: pose(
      Object.assign({}, SEATED_FRONT, { ru: 14, rf: -46, rh: -6, lu: -14, lf: 46, lh: 6 }),
      Object.assign({}, SEATED_SIDE, { ru: -12, rf: -52, lu: -22, lf: -44 }),
      Object.assign({}, SEATED_QUARTER, { ru: -8, rf: -50, lu: -14, lf: 5, lfl: 0.68 }), { plant: 1, seat: 1 }),
    using_laptop: pose(
      Object.assign({}, SEATED_FRONT, { headY: 7, gy: 0.7, ru: 10, rf: -62, rfl: 0.88, lu: -10, lf: 62, lfl: 0.88 }),
      Object.assign({}, SEATED_SIDE, { spine: 6, head: 8, headY: 5, gy: 0.45, gx: 0.3, ru: -14, rf: -33, rfl: 0.6, rh: -30, lu: -22, lf: -30, lfl: 0.6, lh: -30 }),
      Object.assign({}, SEATED_QUARTER, { spine: 3, head: 4, headY: 6, gy: 0.6, gx: 0.2, ru: -6, rf: -53, rfl: 0.56, rh: -22, lu: -8, lf: 57, lfl: 0.41, lh: -105 }),
      Object.assign(hands('relaxed', 'relaxed'), { plant: 1, seat: 1, laptop: 1 })),
    gaming: pose(
      Object.assign({}, SEATED_FRONT, { spine: 1, headY: 8, gy: 0.75, ru: 14, rf: -131, rfl: 0.45, rh: -60, lu: -14, lf: 131, lfl: 0.45, lh: 60 }),
      Object.assign({}, SEATED_SIDE, { spine: 9, head: 7, headY: 5, gy: 0.5, gx: 0.3, ru: -12, rf: -100, rfl: 0.55, rh: -58, lu: -16, lf: -96, lfl: 0.6, lh: -58 }),
      Object.assign({}, SEATED_QUARTER, { spine: 4, head: 5, headY: 7, gy: 0.65, gx: 0.2, ru: -6, rf: -113, rfl: 0.47, rh: -60, lu: -8, lf: 167, lfl: 0.26, lh: 11 }),
      Object.assign(hands('grip', 'grip'), { plant: 1, seat: 1, phoneChest: 1, phoneLand: 1 })),
    walking: pose({ spine: 1 }, { spine: 4, rf: -18, lf: -18 }, { spine: 2, rf: -14, lf: -14 }, { plant: 1, farFront: 0 }),
    running: pose(
      { spine: 2, ru: 30, rf: -110, lu: -30, lf: 110 },
      { spine: 10, head: -7, ru: 20, rf: -88, lu: -20, lf: -88 },
      { spine: 7, head: -6, rf: -96, lf: -92 }, Object.assign(hands('fist', 'fist'), { farFront: 0 })),
    celebrating: pose(
      { head: -2, gy: -0.3, ru: 155, rf: 8, lu: -155, lf: -8 },
      { spine: -2, head: -5, gy: -0.3, ru: 230, rf: -15, lu: -130, lf: -15 },
      { spine: 0, head: -3, gy: -0.3, ru: 150, rf: 15, lu: -135, lf: -12 }, hands('fist', 'fist'))
  };

  /* Digitação: polegares no celular, dedos no teclado. */
  function typingThumbs(j, ph) {
    j.r4 = 0.3 + 0.55 * Math.max(0, Math.sin(ph));
    j.l4 = 0.3 + 0.55 * Math.max(0, Math.sin(ph * 1.13 + 2));
    j.rh += 2.5 * Math.sin(ph); j.lh += 2.5 * Math.sin(ph * 1.13 + 2);
  }
  function typingFingers(j, ph) {
    for (let i = 0; i < 4; i++) {
      j['r' + i] = 0.2 + 0.4 * Math.max(0, Math.sin(ph * (1 + i * 0.13) + i * 1.7));
      j['l' + i] = 0.2 + 0.4 * Math.max(0, Math.sin(ph * (1.07 + i * 0.11) + i * 2.3));
    }
    j.rf += 1.5 * Math.sin(ph * 0.7); j.lf += 1.5 * Math.sin(ph * 0.61 + 1);
  }

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
    },
    texting: typingThumbs,
    gaming(j, ph) {
      typingThumbs(j, ph);
      j.rootR += 0.8 * Math.sin(ph * 0.37);
      j.spine += 1.4 * Math.sin(ph * 0.37);
      j.head += 1.2 * Math.sin(ph * 0.37 + 0.6);
    },
    using_laptop(j, ph) { typingFingers(j, ph); j.head += 0.6 * Math.sin(ph * 0.2); },
    using_phone(j, ph) { j.r4 = 0.35 + 0.45 * Math.max(0, Math.sin(ph * 0.8)); j.rh += 1.5 * Math.sin(ph * 0.4); },
    celebrating(j, ph, view) {
      const hop = Math.abs(Math.sin(ph));
      j.rootY = BASE_ROOT - 46 * hop;
      const bend = 1 - hop;
      j.rt += (view > 0 ? -14 : 6) * bend; j.rs += (view > 0 ? 28 : -6) * bend;
      j.lt += (view > 0 ? -14 : -6) * bend; j.ls += (view > 0 ? 28 : 6) * bend;
      j.ru += 5 * Math.sin(ph * 2); j.lu -= 5 * Math.sin(ph * 2);
      j.rf += 5 * Math.sin(ph * 2); j.lf -= 5 * Math.sin(ph * 2);
    }
  };
  const MOTION_RATE = { walking: 6.2, running: 11, texting: 9, gaming: 11, using_laptop: 10, using_phone: 3, celebrating: 5.5 };
  const STILL_PHASE = { walking: 0.9, running: 0.9, celebrating: 1.57 };

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

  const ANIMATIONS = ['none', 'idle', 'talk', 'typing', 'nod', 'shake', 'wave', 'tremble'];
  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const ACCESSORIES = ['smartphone', 'headphones', 'laptop', 'backpack', 'seat', 'shadow'];
  const ANIMATE = {
    typing(j, t, w) {
      const o = lerpDict(j, j, 1);
      typingFingers(o, t * 10);
      for (const k in j) j[k] = lerp(j[k], o[k], w);
    },
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

  class LeoRivera {
    constructor(target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: 'standing', animation: 'idle', direction: 'front', seed: 13, autoStart: true }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('LeoRivera: elemento de destino não encontrado.');
      instanceCount += 1;
      this.prefix = opt.idPrefix || (instanceCount === 1 ? 'leo' : 'leo' + instanceCount);
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
      this.accessories = { smartphone: 'auto', headphones: false, laptop: 'auto', backpack: false, seat: 'auto', shadow: true };
      this.visible = true; this.alpha = 1;
      this.arms = { r: { w: 0, on: false, v: null }, l: { w: 0, on: false, v: null } };
      this.viseme = { name: 'rest', w: 0, on: false, dur: 80 };
      this.hairSwing = 0; this.hairVel = 0;
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
    /* Controla um braço sem depender da pose. Ângulos em graus; null devolve à pose. */
    setArm(side, values) {
      const k = side === 'right' ? 'r' : side === 'left' ? 'l' : null;
      if (!k) throw new Error('LeoRivera: braço desconhecido "' + side + '". Use: right, left');
      if (values && values.hand && !HANDS[values.hand]) throw new Error('LeoRivera: mão desconhecida "' + values.hand + '". Use: ' + Object.keys(HANDS).join(', '));
      const a = this.arms[k];
      a.on = !!values;
      if (values) a.v = Object.assign({ shoulder: 0, elbow: 0, wrist: 0 }, values);
      return this._after();
    }
    /* Sincronização labial: rest, A, E, I, O, U, M, F. null devolve a boca à expressão. */
    setViseme(name, o) {
      if (name !== null && !VISEMES[name]) throw new Error('LeoRivera: visema desconhecido "' + name + '". Use: ' + Object.keys(VISEMES).join(', '));
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
      if (!ACCESSORIES.includes(name)) throw new Error('LeoRivera: acessório desconhecido "' + name + '". Use: ' + ACCESSORIES.join(', '));
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
      if (!table[name]) throw new Error('LeoRivera: ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (!ANIMATIONS.includes(name)) throw new Error('LeoRivera: animação desconhecida "' + name + '". Use: ' + ANIMATIONS.join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error('LeoRivera: direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
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
        if (motion && (live || STILL_PHASE[name] !== undefined)) {
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
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'leo-rig', role: 'img', 'aria-label': 'Leo Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
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

      const packG = this.pack = n('g', {}, layer('layer-backpack'), 'backpack');
      this.packBody = n('path', Object.assign({ fill: C.pack }, lineStyle), packG, 'backpack-body');
      this.packFlap = n('path', { fill: C.packDark }, packG, 'backpack-pocket');
      this.backArmLayer = layer('layer-back-arm');
      this.hipsO = n('path', Object.assign({}, outlineStyle), rig);
      this.legL = this._buildLeg(rig, 'l', 'left');
      this.legR = this._buildLeg(rig, 'r', 'right');
      this.hipsF = n('path', {}, rig, 'hips');

      const hairBackLayer = layer('layer-hair-back');
      this.hairBackGroup = n('g', {}, hairBackLayer);
      this.hairBack = n('path', Object.assign({ fill: C.hairDeep }, lineStyle), this.hairBackGroup, 'hair-back');

      this.hood = n('path', Object.assign({}, lineStyle), layer('layer-hood'), 'hood');
      const neck = this.neck = n('g', {}, layer('layer-neck'), 'neck');
      n('path', Object.assign({ d: capsule(62, 19, 22), fill: C.skin }, lineStyle), neck);
      n('path', { d: 'M-17 2H17V14Q0 24 -17 14Z', fill: C.skinShade }, neck);

      const torso = layer('torso');
      this.torsoShape = n('path', Object.assign({}, lineStyle), torso, 'torso-shape');
      this.torsoShade = n('path', {}, torso, 'torso-shade');
      this.wrinkles = n('path', { fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, torso);
      this.collar = n('path', { fill: 'none', 'stroke-width': 7, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, torso, 'collar');
      this.tee = n('path', Object.assign({ fill: C.tee }, lineStyle, { 'stroke-width': 3.5 }), torso, 'tshirt');
      this.teeCollar = n('path', { fill: 'none', stroke: C.teeShade, 'stroke-width': 5, 'stroke-linecap': 'round' }, torso);
      this.zipper = n('path', { fill: 'none', stroke: C.zipper, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, torso, 'zipper');
      this.strings = n('path', { fill: 'none', stroke: C.string, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, torso, 'drawstrings');
      this.pocket = n('path', Object.assign({ }, lineStyle, { 'stroke-width': 3.5 }), torso, 'pocket');
      this.hemLine = n('path', { fill: 'none', 'stroke-width': 3.5, 'stroke-linecap': 'round' }, torso, 'hem');
      this.straps = n('path', { fill: 'none', stroke: C.packStrap, 'stroke-width': 13, 'stroke-linecap': 'round' }, torso, 'backpack-straps');

      this._buildHead(layer('layer-head'));

      /* A base do notebook fica sob as mãos; a tampa, à frente delas. */
      const laptopDeck = this.laptopDeck = n('g', {}, rig, 'laptop-deck');
      this.laptopBase = n('path', Object.assign({ fill: C.laptop }, lineStyle), laptopDeck, 'laptop-base');
      this.laptopKeys = n('path', { fill: C.laptopDark }, laptopDeck, 'laptop-keys');
      this.frontArmLayer = layer('layer-front-arm');
      this._buildChestPhone(this.frontArmLayer);
      this.armL = this._buildArm(this.frontArmLayer, 'l', 'left');
      this.armR = this._buildArm(this.frontArmLayer, 'r', 'right');
      this.armLParent = this.frontArmLayer;
      this.pocketPatch = n('path', Object.assign({}, lineStyle, { 'stroke-width': 3.5 }), this.frontArmLayer, 'pocket-front');
      this._buildLaptop(rig);
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
          leg.thighShade = n('path', { d: capsule(118, 6, 5) }, thigh);
          leg.shinShade = n('path', { d: capsule(112, 5, 4.5) }, shin);
          leg.knee = n('path', { d: 'M-12 -3Q0 7 12 -3', fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, shin);
          leg.shoe = n('path', {}, foot);
          leg.stripe = n('path', { fill: 'none', 'stroke-width': 4.5, 'stroke-linecap': 'round' }, foot);
          leg.laces = n('path', { fill: 'none', stroke: C.metalDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, foot);
          leg.sole = n('path', {}, foot);
          leg.cuff = n('path', { d: 'M-17 -6H17', fill: 'none', 'stroke-width': 9, 'stroke-linecap': 'round' }, foot);
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
        const skin = isO ? outlineStyle : {};
        const passG = n('g', {}, g);
        const upper = n('g', {}, passG, isO ? null : 'upper-arm-' + side);
        const up = n('path', Object.assign({ d: capsule(M.upperArm, 22, 19) }, skin), upper);
        const fore = n('g', {}, upper, isO ? null : 'forearm-' + side, PIVOTS.elbow);
        const fp = n('path', Object.assign({}, skin), fore);
        arm.forePaths.push(fp);
        const hand = n('g', {}, fore, isO ? null : 'hand-' + side, PIVOTS.wrist);
        arm.upper.push(upper); arm.fore.push(fore); arm.hand.push(hand);
        if (isO) {
          n('path', Object.assign({ d: this._palm() }, outlineStyle), hand);
          arm.fingersO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14 + LINE, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
        } else {
          arm.skin.push(up, fp);
          arm.sleeveShade = n('path', {}, upper);
          arm.foreShade = n('path', {}, fore);
          arm.cuff = n('path', { fill: 'none', 'stroke-width': 7, 'stroke-linecap': 'round' }, fore, 'cuff-' + side);
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
      arm.propSlot = n('g', {}, hand, 'held-' + arm.side);
      arm.thumbO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.thumbF = n('path', { fill: 'none', stroke: C.skin, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.fingersOnTop = false;
      if (arm.k === 'r') this._buildHandPhone(arm.propSlot);
      else this._buildClosedLaptop(arm.propSlot);
    }
    _buildHandPhone(parent) {
      const n = this._n.bind(this);
      const p = this.handPhone = n('g', {}, parent, 'smartphone');
      n('rect', Object.assign({ x: -18, y: -8, width: 36, height: 74, rx: 7, fill: C.device }, lineStyle), p);
      n('circle', { cx: -8, cy: 2, r: 4.5, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
      n('circle', { cx: -8, cy: 14, r: 3.5, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
    }
    _buildClosedLaptop(parent) {
      const n = this._n.bind(this);
      const p = this.laptopClosed = n('g', {}, parent, 'laptop-closed');
      n('rect', Object.assign({ x: -62, y: 10, width: 124, height: 88, rx: 6, fill: C.laptop }, lineStyle), p);
      n('path', { d: 'M-58 90H58', stroke: C.laptopDark, 'stroke-width': 3 }, p);
      n('circle', { cx: 0, cy: 54, r: 11, fill: C.logo }, p);
    }
    _buildChestPhone(parent) {
      const n = this._n.bind(this);
      const p = this.chestPhone = n('g', {}, parent, 'smartphone-held');
      this.chestPhoneBody = n('rect', Object.assign({ rx: 7, fill: C.device }, lineStyle), p);
      this.chestPhoneLens = n('circle', { r: 4, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
    }
    _buildLaptop(parent) {
      const n = this._n.bind(this);
      const g = this.laptopOpen = n('g', {}, parent, 'laptop');
      this.laptopLidEdge = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 12, 'stroke-linecap': 'round' }, g);
      this.laptopLidEdgeF = n('path', { fill: 'none', stroke: C.laptop, 'stroke-width': 4, 'stroke-linecap': 'round' }, g);
      this.laptopLid = n('path', Object.assign({ fill: C.laptop }, lineStyle), g, 'laptop-lid');
      this.laptopLogo = n('ellipse', { ry: 11, fill: C.logo }, g, 'laptop-logo');
    }
    _buildHeadphones(parent) {
      const n = this._n.bind(this);
      const g = this.phones = n('g', {}, parent, 'headphones');
      this.phonesBand = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 15, 'stroke-linecap': 'round' }, g);
      this.phonesBandIn = n('path', { fill: 'none', stroke: C.phones, 'stroke-width': 8, 'stroke-linecap': 'round' }, g, 'headphones-band');
      const cup = name => {
        const c = n('g', {}, g, name);
        n('rect', Object.assign({ x: -15, y: -25, width: 30, height: 50, rx: 13, fill: C.phonesPad }, lineStyle), c);
        n('rect', Object.assign({ x: -10, y: -19, width: 20, height: 38, rx: 9, fill: C.phonesCup }, lineStyle, { 'stroke-width': 3.5 }), c);
        return c;
      };
      this.cupFar = cup('headphones-cup-far');
      this.cupNear = cup('headphones-cup-near');
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
      this.freckles = n('path', { fill: 'none', stroke: C.freckle, 'stroke-width': 3.6, 'stroke-linecap': 'round' }, head, 'freckles');
      this.blush = n('path', { fill: C.blush }, head, 'blush');

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
            const browStyle = { fill: 'none', stroke: C.brow, 'stroke-width': 10.5, 'stroke-linecap': 'round' };
      this.browR = n('path', browStyle, head, 'brow-right');
      this.browL = n('path', browStyle, head, 'brow-left');
      this.earTop = n('g', {}, head, 'ears-top');
      this._buildHeadphones(head);
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
      n('circle', { r: 12.5, fill: C.iris }, ball);
      n('circle', { r: 8.5, fill: '#120d0a' }, ball);
      n('circle', { cx: 4, cy: -5, r: 3.8, fill: '#fff' }, ball);
      const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 6, 'stroke-linecap': 'round' }, g);
      return { g, white, ball, lid };
    }

    /* ---------- Desenho de um quadro ---------- */
    _render(blink, dt) {
      const t = Math.abs(this.turn), st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const O = OUTFITS.hoodie;
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

      this._renderBody(st, O, j);
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
        this.frontArmLayer.insertBefore(this.armL.root, this.armR.root); this.armLParent = this.frontArmLayer;
      }
    }
    _renderBody(st, O, j) {
      const hips = spline(shape('hips', st), true);
      put(this.hipsO, 'd', hips); put(this.hipsF, 'd', hips); put(this.hipsF, 'fill', O.pants);
      put(this.torsoShape, 'd', spline(shape('torso', st), true));
      put(this.torsoShape, 'fill', O.top);
      put(this.torsoShade, 'd', spline(shape('torsoShade', st < 0.5 ? 0 : 1), true));
      put(this.torsoShade, 'fill', O.topShade);
      shown(this.torsoShade, Math.abs(1 - 2 * st));
      const wx = key3(0, 8, 14, st);
      const wr = key3(50, 42, 22, st);
      put(this.wrinkles, 'd', 'M' + f(wx - 44) + ' -66Q' + f(wx - 26) + ' -58 ' + f(wx - 12) + ' -62M' + f(wx + wr) + ' -112Q' + f(wx + wr - 14) + ' -100 ' + f(wx + wr - 30) + ' -102');
      put(this.wrinkles, 'stroke', O.topDark);
      put(this.neck, 'transform', tf(key3(0, 5, 10, st), M.headY + 6));
      put(this.hood, 'd', spline(shape('hood', st), true));
      put(this.hood, 'fill', O.topShade);

      put(this.tee, 'd', spline(shape('tee', st), true));
      const tc = key3(0, 22, 36, st), tw = key3(22, 18, 11, st);
      put(this.teeCollar, 'd', 'M' + f(tc - tw) + ' -200Q' + f(tc) + ' -180 ' + f(tc + tw) + ' -200');
      const cx = key3(0, 4, 5, st), cw = key3(30, 26, 18, st);
      put(this.collar, 'stroke', O.topDark);
      put(this.collar, 'd', 'M' + f(cx - cw) + ' -206Q' + f(cx - cw * 0.5) + ' -194 ' + f(cx - cw * 0.3) + ' -190M' + f(cx + cw) + ' -206Q' + f(cx + cw * 0.5) + ' -194 ' + f(cx + cw * 0.3) + ' -190');

      const zx = key3(0, 22, 48, st);
      put(this.zipper, 'd', 'M' + f(zx) + ' -92L' + f(key3(0, 26, 50, st)) + ' 34');
      const sx1 = key3(-13, 12, 38, st), sx2 = key3(13, 34, 44, st);
      put(this.strings, 'd', 'M' + f(sx1) + ' -196V-152M' + f(sx2) + ' -196V-142');

      const pk = shape('pocketPatch', st);
      const pd = spline(pk, true);
      put(this.pocket, 'd', pd); put(this.pocket, 'fill', O.top);
      put(this.pocketPatch, 'd', pd); put(this.pocketPatch, 'fill', O.top);
      shown(this.pocketPatch, j.pocket > 0.5 ? 1 : 0);
      put(this.hemLine, 'd', 'M' + f(key3(-64, -56, -46, st)) + ' 20L' + f(key3(64, 60, 48, st)) + ' 20');
      put(this.hemLine, 'stroke', O.topDark);

      const packOn = this.accessories.backpack;
      shown(this.pack, packOn ? 1 : 0);
      shown(this.straps, packOn ? 1 : 0);
      if (packOn) {
        const body = shape('pack', st);
        put(this.packBody, 'd', spline(body, true));
        const m = (a, b, u) => [lerp(a[0], b[0], u), lerp(a[1], b[1], u)];
        const a = m(body[0], body[3], 0.55), b = m(body[1], body[2], 0.55), c = body[2], d = body[3];
        put(this.packFlap, 'd', 'M' + f(a[0] + 8) + ' ' + f(a[1]) + 'L' + f(b[0] - 8) + ' ' + f(b[1]) + 'L' + f(c[0] - 12) + ' ' + f(c[1] - 12) + 'L' + f(d[0] + 12) + ' ' + f(d[1] - 12) + 'Z');
        const near = key3(-46, -28, -20, st), far = key3(46, 44, 40, st);
        put(this.straps, 'd', 'M' + f(near) + ' -200Q' + f(near + key3(-4, -8, 20, st)) + ' -140 ' + f(near - key3(6, 12, 6, st)) + ' -92' +
          (st < 0.8 ? 'M' + f(far) + ' -200Q' + f(far + 4) + ' -140 ' + f(far + 6) + ' -92' : ''));
      }
    }
    _renderLeg(leg, j, k, st, far, O) {
      const ang = j[k + 't'], knee = j[k + 's'], ank = j[k + 'foot'];
      const ty = j[k + 'ty'], sy = j[k + 'sy'];
      const hipX = k === 'r' ? key3(-28, -20, -6, st) : key3(28, 22, 7, st);
      put(leg.root, 'transform', tf(hipX, M.hipY));
      const lenT = M.thigh * ty, lenS = M.shin * sy;
      const dT = capsule(lenT, 29, 23), dS = capsule(lenS, 23, 18);
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
      const sx = k === 'r' ? key3(-72, -56, -8, st) : key3(72, 66, 16, st);
      const sy = M.shoulderY - j.shrug * 14 - b * 0.8;
      put(arm.root, 'transform', tf(sx, sy));
      const foreLen = M.foreArm * j[k + 'fl'];
      const uT = tf(0, 0, j[k + 'u']), fT = tf(0, M.upperArm, j[k + 'f']);
      const flip = k === 'r' ? 1 : lerp(-1, 1, smooth(clamp((st - 0.12) / 0.2)));
      const hs = Math.abs(flip) < 0.35 ? 0.35 * (flip < 0 ? -1 : 1) : flip;
      const hT = tf(0, foreLen, j[k + 'h'], hs * 0.86, 0.86);
      arm.upper.forEach(g => put(g, 'transform', uT));
      arm.fore.forEach(g => put(g, 'transform', fT));
      arm.hand.forEach(g => put(g, 'transform', hT));
      const dF = capsule(foreLen, 19, 16);
      arm.forePaths.forEach(p => put(p, 'd', dF));
      put(arm.foreShade, 'd', capsule(foreLen * 0.74, 4.5, 3.5));
      put(arm.foreShade, 'transform', tf(9, 8));
      put(arm.foreShade, 'fill', O.topShade);
      put(arm.sleeveShade, 'd', capsule(M.upperArm * 0.74, 5, 4));
      put(arm.sleeveShade, 'transform', tf(10, 12));
      put(arm.sleeveShade, 'fill', O.topShade);
      put(arm.cuff, 'd', 'M-13 ' + f(foreLen - 3) + 'H13');
      put(arm.cuff, 'stroke', O.topDark);

      const sleeveCol = far > 0.01 ? hexMix(O.top, O.topShade, far) : O.top;
      const inFront = k === 'r' || this.armLParent === this.frontArmLayer;
      shown(arm.shoulder, inFront ? 1 : 0);
      put(arm.shoulder, 'fill', sleeveCol);
      put(arm.shoulder, 'cx', f((k === 'r' ? 1 : -1) * key3(12, 10, 0, st)));
      put(arm.shoulder, 'cy', f(key3(4, 0, -10, st)));
      put(arm.shoulder, 'rx', f(k === 'r' ? key3(25, 25, 26, st) : key3(25, 20, 26, st)));
      put(arm.shoulder, 'ry', f(key3(25, 23, 19, st)));

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
      const seen = j.pocket > 0.5 ? 0 : 1;
      arm.hand.forEach(g => shown(g, seen));
      arm.skin.forEach(p => put(p, 'fill', sleeveCol));
    }
    _renderEye(eye, clip, x, y, sx, inner, e, openMul, blink, gx, gy) {
      put(eye.g, 'transform', tf(x, y, 0, sx, 1));
      const W = 20;
      const open = Math.max(0, e.eyeOpen * openMul * (1 - blink));
      const T = 24 * open * 1.33, B = 19 * e.eyeLow * (1 - blink * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    }
    _renderHead(j, e, st, blink, dt) {
      const headT = tf(key3(0, 6, 12, st), M.headY + j.headY - j.shrug * 4, j.head + e.tilt);
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

      const sway = this.hairSwing;
      const front = shape('hairFront', st);
      front.forEach(p => { if (p[1] < -165) p[0] += sway * 0.5; });
      put(this.hairFront, 'd', spline(front, true));
      put(this.hairBack, 'd', spline(shape('hairBack', st), true));
      const shine = key3(0, 8, -6, st);
      put(this.hairShine, 'd', 'M' + f(shine - 34) + ' -170Q' + f(shine - 12) + ' -180 ' + f(shine + 12) + ' -176');

      const gx = clamp(j.gx + e.exGx + this.gaze.x, -1, 1);
      const gy = clamp(j.gy + e.exGy + this.gaze.y, -1, 1);
      const rx = key3(-28, 8, 34, st), lx = key3(28, 50, 66, st), ey = -86;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.72, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, 1 + e.eyeSkew, blink, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx, ey, Math.max(ls, 0.06), -1, e, 1 - e.eyeSkew, blink, gx, gy);
      this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

      const nx = key3(0, 38, 64, st), ny = -54;
      const nrx = lerp(10, 13, st);
      put(this.noseFill, 'cx', f(nx)); put(this.noseFill, 'cy', ny);
      put(this.noseFill, 'rx', f(nrx)); put(this.noseFill, 'ry', 9);
      const aC = lerp(Math.PI / 2, 0.2, st), span = lerp(1.9, 1.5, st);
      const arc = [];
      for (let i = 0; i <= 6; i++) {
        const a = aC - span + (2 * span * i) / 6;
        arc.push([nx + Math.cos(a) * nrx, ny + Math.sin(a) * 9]);
      }
      put(this.noseLine, 'd', spline(arc, false));
      const fr = (x, y) => 'M' + f(x) + ' ' + f(y) + 'h.1';
      const freck = fr(rx - 8, -58) + fr(rx + 2, -54) + fr(rx + 12, -59) + (ls > 0.3 ? fr(lx - 12, -59) + fr(lx - 2 * ls, -54) + fr(lx + 8 * ls, -58) : '');
      put(this.freckles, 'd', freck);
      const bl = clamp(e.blush);
      shown(this.blush, bl > 0.02 ? 0.5 * bl : 0);
      const cheek = (x, w) => 'M' + f(x - w) + ' -46a' + f(w) + ' 9 0 1 0 ' + f(2 * w) + ' 0a' + f(w) + ' 9 0 1 0 ' + f(-2 * w) + ' 0Z';
      put(this.blush, 'd', cheek(rx - 2, 17) + (ls > 0.3 ? cheek(lx, 17 * ls) : ''));

      this._renderMouth(e, st, flap);

      const nearY = -72;
      put(this.earNear, 'transform', tf(lerp(-68, -18, st), nearY));
      put(this.earFar, 'transform', tf(lerp(68, 50, st), nearY, 0, -1, 1));
      shown(this.earFar, st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);

      const hx1 = key3(-69, -46, -18, st), hx2 = key3(69, 68, -2, st);
      const band = 'M' + f(hx1) + ' ' + (nearY - 18) + 'C' + f(hx1 - 8 * (1 - st)) + ' -236 ' + f(hx2 + 8 * (1 - st)) + ' -236 ' + f(hx2) + ' ' + (nearY - 18);
      put(this.phonesBand, 'd', band); put(this.phonesBandIn, 'd', band);
      put(this.cupNear, 'transform', tf(hx1, nearY));
      put(this.cupFar, 'transform', tf(hx2, nearY, 0, Math.max(0.3, 1 - st * 0.7), 1));
      shown(this.cupFar, st < 0.75 ? 1 : 0);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw > 0.04 ? 1 : 0);
      put(this.sweat1, 'transform', tf(lerp(84, 80, st), lerp(-112, -106, st), 12, 0.5 + sw * 0.5));
      put(this.sweat2, 'transform', tf(key3(-90, 86, 88, st), key3(-92, -82, -82, st), -10, 0.38 + sw * 0.38));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -56 + (this.animation === 'none' ? 0.5 : fall) * 20, 0, 0.72));
    }
    _renderBrow(el, x, inner, e, sx, skew) {
      const y = -116 + e.browY - skew;
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
      put(this.mouth, 'transform', tf(key3(0, 22, 30, st) + e.mouthShift * (1 - st * 0.6), -23));
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
      const phoneAllowed = a.smartphone !== false;
      const chest = phoneAllowed && j.phoneChest > 0.5;
      const inHand = phoneAllowed && (j.phoneHand > 0.5 || (a.smartphone === true && j.phoneChest <= 0.5));
      shown(this.handPhone, inHand ? 1 : 0);
      put(this.handPhone, 'transform', tf(0, 20, 0, key3(1, 0.7, 0.3, st), 1));
      shown(this.chestPhone, chest ? 1 : 0);
      if (chest) {
        const land = j.phoneLand > 0.5;
        const w = land ? key3(92, 80, 22, st) : key3(44, 40, 18, st), h = land ? 46 : 84;
        const cx = key3(0, 34, 76, st), cy = land ? key3(-104, -110, -126, st) : key3(-112, -136, -138, st);
        put(this.chestPhone, 'transform', 'rotate(' + f(key3(0, 6, 20, st)) + ' ' + f(cx) + ' ' + cy + ')');
        put(this.chestPhoneBody, 'x', f(cx - w / 2)); put(this.chestPhoneBody, 'y', f(cy - h / 2));
        put(this.chestPhoneBody, 'width', f(w)); put(this.chestPhoneBody, 'height', f(h));
        put(this.chestPhoneLens, 'cx', f(cx - w * 0.3)); put(this.chestPhoneLens, 'cy', f(cy - h * 0.32));
        shown(this.chestPhoneLens, st < 0.8 ? 1 : 0);
      }
      const open = j.laptop > 0.5 && a.laptop !== false;
      shown(this.laptopOpen, open ? 1 : 0);
      shown(this.laptopDeck, open ? 1 : 0);
      shown(this.laptopClosed, a.laptop === true && j.laptop <= 0.5 ? 1 : 0);
      if (open) {
        /* Caixa em 3D: s = largura, d = distância à frente do corpo, h = altura.
           A câmera vê o colo um pouco de cima, tanto menos quanto mais de perfil. */
        const yaw = st * Math.PI / 2, co = Math.cos(yaw), si = Math.sin(yaw), fall = 0.24 * (1 - st);
        const P = (s, d, h) => [s * co + d * si, -26 + h + d * fall];
        const poly = list => 'M' + list.map(p => f(p[0]) + ' ' + f(p[1])).join('L') + 'Z';
        const W = 66, near = 34, hinge = 126, back = 148, tall = -80;
        put(this.laptopBase, 'd', poly([P(-W, near, 0), P(W, near, 0), P(W, hinge, 0), P(W, hinge, 7), P(-W, hinge, 7), P(-W, near, 7)]));
        put(this.laptopKeys, 'd', poly([P(-W * 0.82, near + 12, 0), P(W * 0.82, near + 12, 0), P(W * 0.82, hinge - 16, 0), P(-W * 0.82, hinge - 16, 0)]));
        const tl = P(-W, back, tall), tr = P(W, back, tall), bl = P(-W, hinge, 0), br = P(W, hinge, 0);
        put(this.laptopLid, 'd', poly([bl, br, tr, tl]));
        const edge = 'M' + f(br[0]) + ' ' + f(br[1]) + 'L' + f(tr[0]) + ' ' + f(tr[1]);
        put(this.laptopLidEdge, 'd', edge); put(this.laptopLidEdgeF, 'd', edge);
        shown(this.laptopLidEdge, st > 0.85 ? 1 : 0); shown(this.laptopLidEdgeF, st > 0.85 ? 1 : 0);
        put(this.laptopLogo, 'cx', f((bl[0] + br[0] + tl[0] + tr[0]) / 4));
        put(this.laptopLogo, 'cy', f((bl[1] + br[1] + tl[1] + tr[1]) / 4));
        put(this.laptopLogo, 'rx', f(11 * co));
        shown(this.laptopLogo, st < 0.85 ? 1 : 0);
      }
      shown(this.phones, a.headphones ? 1 : 0);
      const seat = a.seat === 'auto' ? j.seat : (a.seat ? 1 : 0);
      shown(this.seatProp, seat > 0.5 ? 1 : 0);
      /* O banco acompanha o quadril: encosta nele em altura e fica sob ele em posição. */
      const seatScale = (FLOOR - (j.rootY + M.hipY + 29)) / (FLOOR - 192);
      put(this.seatProp, 'transform', 'translate(' + f(j.rootX + key3(0, -10, -26, st)) + ' ' + FLOOR + ') scale(1 ' + (Math.round(seatScale * 1000) / 1000) + ') translate(0 ' + -FLOOR + ')');
      shown(this.shadow, a.shadow ? 1 : 0);
      put(this.shadow, 'rx', f(lerp(120, 140, st) * (1 - clamp((BASE_ROOT - j.rootY) / 80) * 0.3)));
    }
  }

  LeoRivera.EXPRESSIONS = Object.keys(EXPRESSIONS);
  LeoRivera.POSES = Object.keys(POSES);
  LeoRivera.ANIMATIONS = ANIMATIONS.slice();
  LeoRivera.DIRECTIONS = Object.keys(DIRECTIONS);
  LeoRivera.ACCESSORIES = ACCESSORIES.slice();
  LeoRivera.VISEMES = Object.keys(VISEMES);
  LeoRivera.PIVOTS = PIVOTS;
  LeoRivera.PALETTE = C;
  return LeoRivera;
});
