/*!
 * BeaRivera — personagem de produção do canal Survive the Headline.
 *
 * Mesmo sistema de rig de Dan, Mia e Leo: escala, chão e peso de contorno idênticos.
 * Pose, expressão, direção e acessórios são valores aplicados a um único modelo SVG.
 *
 * Uso:
 *   const bea = new BeaRivera('#palco');
 *   bea.setExpression('curious');
 *   bea.setPose('asking_question');
 *   bea.setAnimation('idle');
 *   bea.setDirection('right');
 *   bea.setAccessory('teddy_bear', true);
 *   bea.setVisible(true);
 *   bea.setHeadTilt(8);                // inclinação da cabeça em graus
 *   bea.setArm('right', { shoulder: -40, elbow: -60, hand: 'open' });  // braço avulso
 *   bea.setViseme('A');                // sincronização labial; null encerra
 *
 * Acessórios: teddy_bear, backpack, colored_pencils, tablet.
 * true liga, false desliga, 'auto' devolve a decisão à pose (o ursinho aparece em hugging).
 *
 * Vídeo quadro a quadro (determinístico):
 *   const bea = new BeaRivera(el, { autoStart: false, seed: 42 });
 *   bea.tick(1000 / 30);
 *   const svg = bea.toSVG();
 *
 * CSS: toda parte tem data-part e id (#bea-head, #bea-pigtail-left, #bea-cheeks...).
 * "right" e "left" são os lados da própria personagem.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.BeaRivera = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- Paleta travada ---------- */
  const C = {
    ink: '#1b1a22', skin: '#f2c3a2', skinShade: '#e2a884',
    hair: '#6b4226', hairShine: '#8f6242', hairDeep: '#533218', brow: '#4a2c17',
    eyeWhite: '#ffffff', iris: '#6b4226', cheek: '#f28f8a',
    mouth: '#5a1c22', lip: '#e0848a', tongue: '#d9636a', teeth: '#fbf7ee', sweat: '#8fd6ff',
    metal: '#b9c2cc', metalDark: '#7f8a96', wood: '#a5764a', woodDark: '#7d5533',
    collar: '#fff4ec', star: '#ffd23f', tie: '#25b6c4', bead1: '#ffd23f', bead2: '#25b6c4', bead3: '#ff6f61',
    pack: '#8a5cd6', packDark: '#6c43b3', packStrap: '#5a3699',
    bear: '#b97a46', bearDark: '#8f5a2f', bearLight: '#e3bb8e',
    tablet: '#2a2d38', tabletCase: '#25b6c4', logo: '#e9edf2',
    pencil1: '#ff6f61', pencil2: '#ffd23f', pencil3: '#25b6c4', wood2: '#f1cf9f'
  };
  const OUTFITS = {
    main: {
      top: '#ff6f61', topShade: '#e95b4e', topDark: '#c9463a',
      pants: '#e6dcf4', pantsShade: '#cfc2e6', pantsLight: '#f3edfa',
      skirt: '#4c82c7', skirtDark: '#3a68a6', skirtLight: '#8fb6e4',
      shoe: '#25b6c4', sole: '#ffffff', stripe: '#ffd23f', sleeve: 26
    }
  };
  const LINE = 4.5;
  const VIEWBOX = '-425 -480 850 860';
  const FLOOR = 340;
  const BASE_ROOT = 158;       // Bea tem ~59% da altura do Dan, com o mesmo chão

  const M = { shoulderY: -104, upperArm: 58, foreArm: 54, hipY: 10, thigh: 70, shin: 72, headY: -128, footH: 30 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-50, M.shoulderY], shoulderLeft: [50, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-22, M.hipY], hipLeft: [22, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
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
      front: [[0, 8], [30, 6], [54, -12], [66, -50], [68, -92], [58, -126], [32, -146], [0, -151],
        [-32, -146], [-58, -126], [-68, -92], [-66, -50], [-54, -12], [-30, 6]],
      q: [[16, 8], [44, 4], [62, -16], [68, -52], [69, -92], [58, -126], [34, -146], [-2, -152],
        [-38, -146], [-64, -122], [-73, -86], [-68, -48], [-50, -14], [-12, 7]],
      side: [[38, 8], [54, 0], [62, -20], [64, -56], [65, -92], [58, -124], [36, -146], [-4, -153],
        [-44, -144], [-70, -118], [-78, -82], [-66, -46], [-38, -16], [8, 0]]
    },
    headShade: {
      front: [[30, 6], [54, -12], [66, -50], [68, -92], [63, -92], [60, -52], [46, -18], [24, 1]],
      side: [[50, 1], [26, 3], [8, 0], [-26, -11], [-20, -22], [2, -10], [26, -8], [44, -9]]
    },
    hairFront: {
      front: [[-66, 0, 1], [-78, -36], [-84, -84], [-78, -122], [-56, -150], [-20, -166], [20, -166], [56, -150], [78, -122],
        [84, -84], [78, -36], [66, 0, 1], [58, -30], [62, -72], [58, -100], [44, -118], [22, -124, 1], [2, -118],
        [-20, -122, 1], [-40, -114], [-58, -98], [-60, -40]],
      q: [[-52, 0, 1], [-70, -36], [-82, -86], [-76, -124], [-52, -152], [-14, -168], [26, -166], [60, -150], [76, -124],
        [78, -92], [72, -54], [66, -20, 1], [60, -48], [62, -84], [58, -104], [46, -118], [30, -124, 1], [10, -118],
        [-10, -122, 1], [-26, -112], [-36, -90], [-38, -34]],
      side: [[-24, 4, 1], [-50, -30], [-80, -76], [-84, -118], [-60, -150], [-24, -166], [14, -168], [46, -154], [64, -132],
        [72, -112], [66, -100], [58, -106, 1], [46, -118], [34, -124], [22, -126], [10, -122], [0, -112, 1], [-6, -92],
        [-10, -70], [-6, -44], [-6, -20], [-12, -4]]
    },
    hairBack: {
      front: [[-52, -146], [-80, -104], [-88, -60], [-80, -26], [-90, 12], [-62, 44], [-30, 36], [0, 42], [30, 36], [62, 44],
        [90, 12], [80, -26], [88, -60], [80, -104], [52, -146], [0, -160]],
      q: [[-42, -148], [-76, -114], [-92, -68], [-84, -26], [-94, 14], [-68, 46], [-42, 36], [-12, 42], [16, 36], [40, 44],
        [60, 26], [58, -6], [64, -52], [58, -104], [40, -144], [-4, -158]],
      side: [[-34, -154], [-72, -130], [-90, -86], [-88, -40], [-102, 6], [-86, 42], [-64, 46], [-42, 38], [-20, 44], [-2, 34],
        [6, 8], [12, -18], [16, -60], [26, -104], [18, -138], [-8, -158]]
    },
    torso: {
      front: [[-22, -128], [-50, -120], [-58, -100], [-52, -60], [-46, -24], [-48, 12, 1], [-24, 16], [0, 18], [24, 16], [48, 12, 1],
        [46, -24], [52, -60], [58, -100], [50, -120], [22, -128], [0, -114]],
      q: [[-16, -129], [-44, -120], [-52, -98], [-46, -60], [-42, -24], [-44, 12, 1], [-20, 16], [2, 18], [26, 16], [46, 12, 1],
        [44, -24], [48, -60], [52, -96], [42, -120], [18, -129], [4, -116]],
      side: [[-12, -130], [-32, -118], [-38, -96], [-36, -60], [-34, -24], [-36, 12, 1], [-16, 16], [0, 18], [20, 16], [38, 12, 1],
        [38, -24], [38, -60], [36, -94], [28, -118], [14, -130], [3, -119]]
    },
    torsoShade: {
      front: [[36, 15], [48, 12], [46, -24], [52, -60], [55, -90], [42, -66], [34, -30], [30, -6]],
      side: [[-22, 15], [-36, 12], [-34, -24], [-36, -60], [-37, -90], [-26, -66], [-22, -30], [-20, -6]]
    },
    skirt: {
      front: [[-42, -10], [-66, 40, 1], [-30, 46], [0, 48], [30, 46], [66, 40, 1], [42, -10], [0, -14]],
      q: [[-38, -10], [-60, 40, 1], [-26, 46], [2, 48], [30, 46], [62, 40, 1], [40, -10], [0, -14]],
      side: [[-34, -10], [-50, 40, 1], [-24, 46], [0, 48], [24, 46], [52, 40, 1], [36, -10], [0, -14]]
    },
    skirtSit: {
      front: [[-42, -10], [-60, 30, 1], [-30, 36], [0, 38], [30, 36], [60, 30, 1], [42, -10], [0, -14]],
      q: [[-38, -10], [-48, 26, 1], [-10, 34], [30, 40], [64, 44, 1], [78, 26, 1], [42, -10], [0, -14]],
      side: [[-34, -10], [-44, 22, 1], [-20, 30], [30, 32], [82, 32, 1], [86, 8, 1], [38, -12], [0, -14]]
    },
    shoe: {
      front: [[-17, -5], [-18, 6], [-22, 15], [-21, 23, 1], [21, 23, 1], [22, 15], [18, 6], [17, -5]],
      q: [[-17, -5], [-18, 7], [-21, 15], [-20, 23, 1], [40, 23, 1], [42, 15], [28, 6], [17, -5]],
      side: [[-17, -5], [-18, 8], [-20, 15], [-20, 23, 1], [52, 23, 1], [54, 15], [34, 5], [17, -5]]
    },
    sole: {
      front: [[-22, 20, 1], [-23, 30, 1], [23, 30, 1], [22, 20, 1]],
      q: [[-21, 20, 1], [-21, 30, 1], [44, 30, 1], [42, 20, 1]],
      side: [[-21, 20, 1], [-21, 30, 1], [56, 30, 1], [54, 20, 1]]
    },
    pack: {
      front: [[-46, -116], [46, -116], [50, -6], [-50, -6]],
      q: [[-74, -112], [14, -116], [14, -6], [-80, -8]],
      side: [[-102, -106], [-34, -114], [-30, -10], [-108, -14]]
    }
  };
  function shape(name, t) {
    const S = SHAPE[name];
    if (!S.q) return S.front.map((p, i) => [lerp(p[0], S.side[i][0], t), lerp(p[1], S.side[i][1], t), p[2]]);
    return S.front.map((p, i) => [key3(p[0], S.q[i][0], S.side[i][0], t), key3(p[1], S.q[i][1], S.side[i][1], t), p[2]]);
  }

  /* ---------- Expressões ---------- */
  const EXPRESSION_BASE = {
    browY: 0, browTilt: 0, browArch: 5, browSkew: 0, eyeOpen: 0.86, eyeLow: 0.95, eyeSkew: 0, lidTilt: 0, pupil: 1,
    mouthW: 17, mouthOpen: 0, smile: 0.32, teeth: 0, grit: 0, tongue: 0, skew: 0, mouthShift: 0,
    tint: 0, sweat: 0, tear: 0, blush: 0, exGx: 0, exGy: 0, tilt: 0
  };
  const EXPRESSIONS = {
    neutral: {},
    happy: { browY: -6, browArch: 7, eyeOpen: 0.86, eyeLow: 0.62, mouthW: 26, mouthOpen: 16, smile: 1, teeth: 1, tongue: 0.4, blush: 0.5 },
    curious: { browY: -9, browTilt: 4, browArch: 7, browSkew: 5, eyeOpen: 1.02, eyeLow: 0.98, pupil: 1.14, exGx: 0.22, exGy: -0.2, mouthW: 10, mouthOpen: 7, smile: 0.15, tilt: 8 },
    confused: { browY: -3, browTilt: 7, browSkew: -11, eyeOpen: 0.94, eyeSkew: -0.16, mouthW: 13, mouthOpen: 4, smile: -0.25, skew: -0.7, teeth: 0.3, exGx: -0.3, tilt: 7 },
    surprised: { browY: -13, browArch: 7, eyeOpen: 1.16, eyeLow: 1.08, pupil: 0.86, mouthW: 11, mouthOpen: 16, smile: 0, tongue: 0.3 },
    shocked: { browY: -15, browTilt: 4, browArch: 5, eyeOpen: 1.3, eyeLow: 1.18, pupil: 0.62, mouthW: 15, mouthOpen: 30, smile: 0, teeth: 0.3, tongue: 0.6 },
    scared: { browY: -10, browTilt: 13, eyeOpen: 1.26, eyeLow: 1.12, pupil: 0.54, mouthW: 26, mouthOpen: 16, smile: -0.55, teeth: 1, grit: 1, sweat: 0.9, tint: -0.6 },
    sad: { browY: -2, browTilt: 13, eyeOpen: 0.7, lidTilt: -0.42, exGy: 0.5, mouthW: 15, smile: -0.75, tear: 1 },
    laughing: { browY: -8, browArch: 8, eyeOpen: 0.72, eyeLow: -0.42, mouthW: 27, mouthOpen: 24, smile: 1, teeth: 1, tongue: 0.7, blush: 1, tilt: -4 },
    thinking: { browY: -3, browTilt: 4, browSkew: 7, eyeOpen: 0.86, exGx: 0.6, exGy: -0.75, mouthW: 10, smile: -0.05, skew: 0.35, mouthShift: 7, tilt: 4 },
    excited: { browY: -12, browArch: 7, eyeOpen: 1.16, eyeLow: 1, pupil: 1.18, mouthW: 27, mouthOpen: 25, smile: 1, teeth: 1, tongue: 0.5, blush: 0.9 },
    sleepy: { browY: 2, browTilt: 5, eyeOpen: 0.3, eyeLow: 0.8, lidTilt: -0.1, exGy: 0.4, mouthW: 9, mouthOpen: 6, smile: 0, tilt: 7 }
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
     farFront = braço distante continua à frente do tronco no 3/4. teddy = ursinho abraçado. */
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
    ru: 7, rf: -8, rh: 0, rfl: 1, lu: -7, lf: 8, lh: 0, lfl: 1,
    rt: 2, rs: -2, rfoot: 0, rty: 1, rsy: 1, lt: -2, ls: 2, lfoot: 0, lty: 1, lsy: 1,
    gx: 0, gy: 0, plant: 0, farFront: 1, seat: 0, teddy: 0
  }, hands('relaxed', 'relaxed'));
  const SIDE_BASE = { ru: 3, rf: -12, lu: -3, lf: -12, rt: -4, rs: 4, lt: 5, ls: 1 };
  const SEATED_FRONT = { rootY: 130, rt: 6, rs: -6, lt: -6, ls: 6, rty: 0.2, lty: 0.2 };
  const SEATED_SIDE = { rootX: -30, spine: -1, rt: -88, rs: 88, lt: -82, ls: 84 };
  const SEATED_QUARTER = { rootX: -16, rt: -70, rs: 70, rty: 0.72, lt: -64, ls: 64, lty: 0.72 };
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
      { rootX: 3, rootR: 0.6, spine: -1.4, head: 3, ru: 6, rf: -36, rh: -6, lu: -6, lf: 36, lh: 6, rt: 5, rs: -5, lt: -3, ls: 3 },
      { spine: -1, ru: 4, rf: -46, lu: 8, lf: -52 },
      { ru: 2, rf: -42, lu: -8, lf: 30 }),
    standing: pose({}, {}, {}, { farFront: 0 }),
    asking_question: pose(
      { head: 4, spine: -2, lu: -150, lf: -10, lh: -6, ru: 8, rf: -10, gy: -0.25 },
      { head: -3, lu: -138, lf: -10, lh: -4, ru: 6, rf: -14, gy: -0.25 },
      { head: 1, spine: -1, lu: -146, lf: -10, lh: -6, ru: 8, rf: -12, gy: -0.25 },
      Object.assign(hands('relaxed', 'point'), { farFront: 0 })),
    pointing: pose(
      { spine: -3, head: 6, lu: -84, lf: -6, ru: 8, rf: -12, gx: 0.8, gy: -0.1 },
      { spine: 2, head: -2, lu: -84, lf: -8, lh: -4, ru: 4, rf: -16, gx: 0.8 },
      { spine: 1, head: 2, lu: -84, lf: -6, ru: 8, rf: -18, gx: 0.6 },
      Object.assign(hands('relaxed', 'point'), { farFront: 0 })),
    hands_on_cheeks: pose(
      { headY: 8, ru: 90, rf: 141, rh: -27, lu: -90, lf: -141, lh: 27 },
      { headY: 8, ru: -83, rf: -141, rh: 40, lu: -80, lf: -136, lh: 40 },
      { headY: 8, ru: 78, rf: 145, rh: -20, lu: -90, lf: -141, lh: 27 }, hands('open', 'open')),
    thinking: pose(
      { head: -3, ru: -13, rf: -153, rh: 8, lu: -6, lf: 96, lfl: 0.85, lh: -4 },
      { head: -2, ru: -13, rf: -153, rh: 8, lu: -2, lf: -86, lfl: 0.45 },
      { head: -2, ru: -26, rf: -126, rh: -8, lu: -8, lf: 92, lfl: 0.85 }),
    shrugging: pose(
      { shrug: 1, head: 4, ru: 8, rf: 86, rh: 24, lu: -8, lf: -86, lh: -24 },
      { shrug: 1, head: -4, ru: 8, rf: -80, rfl: 0.6, rh: -40, lu: -6, lf: -70, lfl: 0.7, lh: -40 },
      { shrug: 1, ru: 6, rf: 78, rfl: 0.8, rh: 20, lu: -14, lf: -74, lfl: 0.9, lh: -20 },
      Object.assign(hands('open', 'open'), { farFront: 0 })),
    excited: pose(
      { ru: 20, rf: 120, rh: 6, lu: -20, lf: -120, lh: -6 },
      { ru: -20, rf: -120, lu: -30, lf: -110 },
      { ru: 10, rf: 130, lu: -30, lf: -110 }, Object.assign(hands('fist', 'fist'), { farFront: 0 })),
    jumping: pose(
      { ru: 150, rf: 15, lu: -150, lf: -15 },
      { spine: -2, ru: 242, rf: -12, lu: -118, lf: -12 },
      { ru: 150, rf: 15, lu: -128, lf: -10 }, Object.assign(hands('open', 'open'), { farFront: 0 })),
    sitting: pose(
      Object.assign({}, SEATED_FRONT, { ru: 14, rf: -46, rh: -6, lu: -14, lf: 46, lh: 6 }),
      Object.assign({}, SEATED_SIDE, { ru: -12, rf: -52, lu: -22, lf: -44 }),
      Object.assign({}, SEATED_QUARTER, { ru: -8, rf: -50, lu: -14, lf: 5, lfl: 0.7 }), { plant: 1, seat: 1 }),
    walking: pose({ spine: 1 }, { spine: 3, rf: -18, lf: -18 }, { spine: 2, rf: -14, lf: -14 }, { plant: 1, farFront: 0 }),
    running: pose(
      { spine: 2, ru: 30, rf: -110, lu: -30, lf: 110 },
      { spine: 9, head: -7, ru: 20, rf: -88, lu: -20, lf: -88 },
      { spine: 7, head: -6, rf: -96, lf: -92 }, Object.assign(hands('fist', 'fist'), { farFront: 0 })),
    hugging: pose(
      { head: 5, headY: 4, ru: 4, rf: -100, rh: 4, lu: -4, lf: 100, lh: -4 },
      { spine: 4, head: 6, headY: 4, ru: -22, rf: -86, rfl: 0.5, lu: -30, lf: -80, lfl: 0.5 },
      { spine: 2, head: 6, headY: 4, ru: -2, rf: -92, lu: -6, lf: 104, lfl: 0.66 },
      Object.assign(hands('open', 'open'), { teddy: 1 })),
    looking_up: pose(
      { headY: 3, gy: -0.95, ru: 14, rf: -6, lu: -14, lf: 6 },
      { spine: -3, head: -18, gy: -0.8, gx: 0.3, ru: 10, rf: -8, lu: 6, lf: -8 },
      { spine: -2, head: -10, headY: 2, gy: -0.9, gx: 0.2, ru: 12, rf: -8, lu: -8, lf: 6 }, { farFront: 0 })
  };

  /* Ciclos. view: 0 frente, 0.5 três quartos, 1 perfil. */
  const POSE_MOTION = {
    walking(j, ph, view) {
      const s = Math.sin(ph);
      if (view > 0) {
        const stride = view < 1 ? 0.8 : 1;
        const leg = a => [(-6 - 26 * Math.sin(a)) * stride, (10 + 36 * Math.max(0, Math.cos(a - 0.3))) * stride];
        const R = leg(ph), L = leg(ph + Math.PI);
        j.rt = R[0]; j.rs = R[1]; j.rfoot = -R[1] * 0.25;
        j.lt = L[0]; j.ls = L[1]; j.lfoot = -L[1] * 0.25;
        j.ru += 18 * s; j.lu -= 18 * s;
      } else {
        const lr = Math.max(0, s), ll = Math.max(0, -s);
        j.rty = 1 - 0.18 * lr; j.lty = 1 - 0.18 * ll;
        j.rsy = 1 - 0.06 * lr; j.lsy = 1 - 0.06 * ll;
        j.rootX += 2.5 * s; j.rootR += 1.2 * s; j.head -= 1.2 * s;
        j.ru += 6 * s; j.lu += 6 * s;
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
        j.rootY = BASE_ROOT + (quarter ? 8 : 14) - (quarter ? 13 : 15) * Math.abs(c);
      } else {
        const lr = Math.max(0, s), ll = Math.max(0, -s);
        j.rty = 1 - 0.62 * lr; j.lty = 1 - 0.62 * ll;
        j.rsy = 1 - 0.1 * lr; j.lsy = 1 - 0.1 * ll;
        j.rootY = BASE_ROOT + 8 - 13 * Math.abs(c);
        j.rootR = 2 * s; j.spine += 2.5 * s; j.head -= 2 * s;
        j.ru += 6 * s; j.lu += 6 * s; j.rf += 18 * s; j.lf += 18 * s;
      }
    },
    excited(j, ph) {
      const hop = Math.abs(Math.sin(ph));
      j.rootY = BASE_ROOT - 14 * hop;
      j.rootR += 1.5 * Math.sin(ph * 0.5);
      j.ru += 6 * Math.sin(ph); j.lu += 6 * Math.sin(ph);
      j.rf += 8 * Math.sin(ph * 2); j.lf -= 8 * Math.sin(ph * 2);
    },
    jumping(j, ph, view) {
      const hop = Math.abs(Math.sin(ph));
      j.rootY = BASE_ROOT - 70 * hop;
      const tuck = view > 0 ? hop : 0;
      j.rt += -30 * tuck; j.rs += 56 * tuck; j.lt += -22 * tuck; j.ls += 50 * tuck;
      if (view === 0) { j.rty = 1 - 0.3 * hop; j.lty = 1 - 0.3 * hop; }
      j.ru += 5 * Math.sin(ph * 2); j.lu -= 5 * Math.sin(ph * 2);
    }
  };
  const MOTION_RATE = { walking: 7, running: 12, excited: 8, jumping: 5 };
  const STILL_PHASE = { walking: 0.9, running: 0.9, jumping: 1.57 };

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

  const ANIMATIONS = ['none', 'idle', 'talk', 'nod', 'shake', 'head_tilt', 'wave', 'celebrate', 'tremble'];
  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const ACCESSORIES = ['teddy_bear', 'backpack', 'colored_pencils', 'tablet', 'bracelet', 'seat', 'shadow'];
  const ANIMATE = {
    head_tilt(j, t, w) { j.head += 9 * Math.sin(t * 1.5) * w; j.gx += 0.2 * Math.sin(t * 1.5) * w; },
    celebrate(j, t, w, st) {
      j.rootY -= 40 * Math.abs(Math.sin(t * 5.5)) * w;
      const swing = 6 * Math.sin(t * 11);
      j.ru = lerp(j.ru, key3(155, 150, 242, st) + swing, w);
      j.rf = lerp(j.rf, key3(8, 15, -15, st), w);
      j.rfl = lerp(j.rfl, 1, w);
      j.lu = lerp(j.lu, key3(-155, -128, -118, st) - swing, w);
      j.lf = lerp(j.lf, key3(-8, -12, -15, st), w);
      j.lfl = lerp(j.lfl, 1, w);
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

  class BeaRivera {
    constructor(target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: 'standing', animation: 'idle', direction: 'front', seed: 17, autoStart: true }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('BeaRivera: elemento de destino não encontrado.');
      instanceCount += 1;
      this.prefix = opt.idPrefix || (instanceCount === 1 ? 'bea' : 'bea' + instanceCount);
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
      this.accessories = { teddy_bear: 'auto', backpack: false, colored_pencils: false, tablet: false, bracelet: true, seat: 'auto', shadow: true };
      this.headTilt = 0; this.headTiltTarget = 0;
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
    /* Inclina a cabeça em graus; positivo para o lado do olhar. */
    setHeadTilt(deg) { this.headTiltTarget = clamp(deg, -20, 20); return this._after(); }
    /* Controla um braço sem depender da pose. Ângulos em graus; null devolve à pose. */
    setArm(side, values) {
      const k = side === 'right' ? 'r' : side === 'left' ? 'l' : null;
      if (!k) throw new Error('BeaRivera: braço desconhecido "' + side + '". Use: right, left');
      if (values && values.hand && !HANDS[values.hand]) throw new Error('BeaRivera: mão desconhecida "' + values.hand + '". Use: ' + Object.keys(HANDS).join(', '));
      const a = this.arms[k];
      a.on = !!values;
      if (values) a.v = Object.assign({ shoulder: 0, elbow: 0, wrist: 0 }, values);
      return this._after();
    }
    /* Sincronização labial: rest, A, E, I, O, U, M, F. null devolve a boca à expressão. */
    setViseme(name, o) {
      if (name !== null && !VISEMES[name]) throw new Error('BeaRivera: visema desconhecido "' + name + '". Use: ' + Object.keys(VISEMES).join(', '));
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
      if (!ACCESSORIES.includes(name)) throw new Error('BeaRivera: acessório desconhecido "' + name + '". Use: ' + ACCESSORIES.join(', '));
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
      this.headTilt = lerp(this.headTilt, this.headTiltTarget, clamp(dt * 10));
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
      if (!table[name]) throw new Error('BeaRivera: ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (!ANIMATIONS.includes(name)) throw new Error('BeaRivera: animação desconhecida "' + name + '". Use: ' + ANIMATIONS.join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error('BeaRivera: direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
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
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'bea-rig', role: 'img', 'aria-label': 'Bea Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = n('defs', {}, svg);
      this.clipEyeR = n('path', {}, n('clipPath', { id: u + '-clip-eye-right' }, defs));
      this.clipEyeL = n('path', {}, n('clipPath', { id: u + '-clip-eye-left' }, defs));
      this.clipMouth = n('path', {}, n('clipPath', { id: u + '-clip-mouth' }, defs));

      this.shadow = n('ellipse', { cx: 0, cy: FLOOR + 3, rx: 88, ry: 12, fill: '#000', 'fill-opacity': 0.22 }, svg, 'shadow');
      this.flip = n('g', {}, svg, 'character');
      this._buildSeat(this.flip);

      const rig = this.rig = n('g', {}, this.flip, 'pelvis', PIVOTS.pelvis);
      this.spineNodes = [];
      const layer = name => { const g = n('g', {}, rig, name, PIVOTS.torso); this.spineNodes.push(g); return g; };

      const packG = this.pack = n('g', {}, layer('layer-backpack'), 'backpack');
      this.packBody = n('path', Object.assign({ fill: C.pack }, lineStyle), packG, 'backpack-body');
      this.packFlap = n('path', { fill: C.packDark }, packG, 'backpack-pocket');
      this.backArmLayer = layer('layer-back-arm');
      this.legL = this._buildLeg(rig, 'l', 'left');
      this.legR = this._buildLeg(rig, 'r', 'right');
      this.skirt = n('path', Object.assign({}, lineStyle), rig, 'hips');
      this.skirtDetail = n('path', { fill: 'none', 'stroke-width': 3, 'stroke-linecap': 'round' }, rig, 'skirt-detail');

      const hairBackLayer = layer('layer-hair-back');
      this.hairBackGroup = n('g', {}, hairBackLayer);
      this.hairBack = n('path', Object.assign({ fill: C.hairDeep }, lineStyle), this.hairBackGroup, 'hair-back');
      
      const neck = this.neck = n('g', {}, layer('layer-neck'), 'neck');
      n('path', Object.assign({ d: capsule(30, 14, 16), fill: C.skin }, lineStyle), neck);
      n('path', { d: 'M-12 2H12V10Q0 18 -12 10Z', fill: C.skinShade }, neck);

      const torso = layer('torso');
      this.torsoShape = n('path', Object.assign({}, lineStyle), torso, 'torso-shape');
      this.torsoShade = n('path', {}, torso, 'torso-shade');
      this.wrinkles = n('path', { fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, torso);
      this.collar = n('path', Object.assign({ fill: C.collar }, lineStyle, { 'stroke-width': 3.5 }), torso, 'collar');
      this.star = n('path', Object.assign({ fill: C.star }, lineStyle, { 'stroke-width': 3 }), torso, 'star');
      this.straps = n('path', { fill: 'none', stroke: C.packStrap, 'stroke-width': 10, 'stroke-linecap': 'round' }, torso, 'backpack-straps');

      this._buildHead(layer('layer-head'));

      this.frontArmLayer = layer('layer-front-arm');
      this.teddyChest = this._buildTeddy(this.frontArmLayer, 'teddy-bear-hugged');
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
          leg.thighShade = n('path', { d: capsule(50, 4, 3.5) }, thigh);
          leg.shinShade = n('path', { d: capsule(54, 3.5, 3) }, shin);
          leg.knee = n('path', { d: 'M-8 -2Q0 5 8 -2', fill: 'none', 'stroke-width': 3.2, 'stroke-linecap': 'round' }, shin);
          leg.shoe = n('path', {}, foot);
          leg.stripe = n('path', { fill: 'none', 'stroke-width': 4.5, 'stroke-linecap': 'round' }, foot);
          leg.laces = n('path', { fill: 'none', stroke: C.metalDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, foot);
          leg.sole = n('path', {}, foot);
          leg.cuff = n('path', { d: 'M-14 -5H14', fill: 'none', 'stroke-width': 4, 'stroke-linecap': 'round' }, foot);
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
        const up = n('path', Object.assign({ d: capsule(M.upperArm, 13, 12) }, skin), upper);
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
            const b = this.bracelet = n('g', { transform: 'translate(0 42)' }, fore, 'bracelet');
            [[-8, C.bead1], [0, C.bead2], [8, C.bead3]].forEach(([x, c]) => n('circle', { cx: x, cy: 0, r: 4, fill: c, stroke: C.ink, 'stroke-width': 2 }, b));
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
      arm.propSlot = n('g', {}, hand, 'held-' + arm.side);
      arm.thumbO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.thumbF = n('path', { fill: 'none', stroke: C.skin, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
      arm.fingersOnTop = false;
      if (arm.k === 'r') {
        this._buildTablet(arm.propSlot);
        this._buildPencils(arm.propSlot);
      } else {
        this.teddyHand = this._buildTeddy(arm.propSlot, 'teddy-bear');
      }
    }
    _buildTeddy(parent, part) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, part);
      const round = (cx, cy, rx, ry, fill) => n('ellipse', Object.assign({ cx, cy, rx, ry, fill }, lineStyle, { 'stroke-width': 3.5 }), g);
      round(-20, -12, 11, 11, C.bear); round(20, -12, 11, 11, C.bear);
      round(-26, 40, 11, 13, C.bear); round(26, 40, 11, 13, C.bear);
      round(-15, 62, 12, 10, C.bear); round(15, 62, 12, 10, C.bear);
      round(0, 44, 24, 24, C.bear);
      round(0, 44, 13, 13, C.bearLight);
      round(0, 4, 26, 23, C.bear);
      round(0, 10, 12, 9, C.bearLight);
      n('circle', { cx: -9, cy: -2, r: 3.2, fill: C.ink }, g); n('circle', { cx: 9, cy: -2, r: 3.2, fill: C.ink }, g);
      n('path', { d: 'M-3 6H3L0 10Z', fill: C.ink, stroke: C.ink, 'stroke-width': 2, 'stroke-linejoin': 'round' }, g);
      return g;
    }
    _buildTablet(parent) {
      const n = this._n.bind(this);
      const p = this.tablet = n('g', {}, parent, 'tablet');
      n('rect', Object.assign({ x: -60, y: 12, width: 120, height: 84, rx: 10, fill: C.tabletCase }, lineStyle), p);
      n('circle', { cx: 0, cy: 54, r: 9, fill: C.logo }, p);
    }
    _buildPencils(parent) {
      const n = this._n.bind(this);
      const p = this.pencils = n('g', { transform: 'translate(0 -10) scale(1.5)' }, parent, 'colored-pencils');
      [[-16, C.pencil1], [-2, C.pencil2], [12, C.pencil3]].forEach(([y, c]) => {
        n('path', Object.assign({ d: 'M-32 ' + (y + 24) + 'H30V' + (y + 34) + 'H-32Z', fill: c }, lineStyle, { 'stroke-width': 3 }), p);
        n('path', Object.assign({ d: 'M30 ' + (y + 24) + 'L46 ' + (y + 29) + 'L30 ' + (y + 34) + 'Z', fill: C.wood2 }, lineStyle, { 'stroke-width': 3 }), p);
      });
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
      this.headShape = n('path', Object.assign({ fill: C.skin }, lineStyle), head, 'face');
      this.headShade = n('path', { fill: C.skinShade, 'fill-opacity': 0.7 }, head);
      this.tint = n('path', {}, head, 'tint');
      this.cheeks = n('path', { fill: C.cheek }, head, 'cheeks');

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
            const browStyle = { fill: 'none', stroke: C.brow, 'stroke-width': 8.5, 'stroke-linecap': 'round' };
      this.browR = n('path', browStyle, head, 'brow-right');
      this.browL = n('path', browStyle, head, 'brow-left');
      this.pigtailFar = this._pigtail(head, 'pigtail-left');
      this.pigtailNear = this._pigtail(head, 'pigtail-right');
      this.sweat = n('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat);
      this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
    }
    _drop(parent) {
      return this._n('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
    }
    _pigtail(parent, part) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, part);
      n('path', Object.assign({ d: 'M-9 0C-18 14 -14 36 0 48C14 36 18 14 9 0Z', fill: C.hair }, lineStyle), g);
      n('path', { d: 'M-4 12Q-7 26 -1 36', fill: 'none', stroke: C.hairShine, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, g);
      n('circle', Object.assign({ r: 8, fill: C.tie }, lineStyle, { 'stroke-width': 3.5 }), g);
      return g;
    }
    _eye(parent, side, clipId) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'eye-' + side);
      const white = n('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, g);
      const iris = n('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
      const ball = n('g', {}, iris, 'pupil-' + side);
      n('circle', { r: 15.5, fill: C.iris }, ball);
      n('circle', { r: 10, fill: '#120d0a' }, ball);
      n('circle', { cx: 5, cy: -6, r: 4.6, fill: '#fff' }, ball);
      const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 5, 'stroke-linecap': 'round' }, g);
      return { g, white, iris, ball, lid };
    }

    /* ---------- Desenho de um quadro ---------- */
    _render(blink, dt) {
      const t = Math.abs(this.turn), st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const O = OUTFITS.main;
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
      const seated = clamp(j.seat);
      const a = shape('skirt', st), b = shape('skirtSit', st);
      const flow = clamp(-(j.rt + j.lt) * 0.2, -16, 16) * (1 - seated) * st;
      const pts = a.map((p, i) => {
        const x = lerp(p[0], b[i][0], seated), y = lerp(p[1], b[i][1], seated);
        return [x + (y > 10 ? flow : 0), y + (y > 10 ? 5 * (1 - seated) : 0), p[2]];
      });
      put(this.skirt, 'd', spline(pts, true));
      put(this.skirt, 'fill', O.skirt);
      put(this.skirtDetail, 'stroke', O.skirtDark);
      put(this.skirtDetail, 'd', 'M' + f(pts[1][0] + 8) + ' ' + f(pts[1][1] - 6) + 'Q' + f(pts[3][0]) + ' ' + f(pts[3][1] + 1) + ' ' + f(pts[5][0] - 8) + ' ' + f(pts[5][1] - 6) +
        'M' + f(pts[0][0] + 4) + ' 6Q' + f(pts[7][0]) + ' 11 ' + f(pts[6][0] - 4) + ' 6');
      put(this.torsoShape, 'd', spline(shape('torso', st), true));
      put(this.torsoShape, 'fill', O.top);
      put(this.torsoShade, 'd', spline(shape('torsoShade', st < 0.5 ? 0 : 1), true));
      put(this.torsoShade, 'fill', O.topShade);
      shown(this.torsoShade, Math.abs(1 - 2 * st));
      const wx = key3(0, 6, 10, st), wr = key3(30, 26, 14, st);
      put(this.wrinkles, 'd', 'M' + f(wx - 26) + ' -8Q' + f(wx - 12) + ' -2 ' + f(wx) + ' -6M' + f(wx + wr) + ' -40Q' + f(wx + wr - 10) + ' -32 ' + f(wx + wr - 20) + ' -34');
      put(this.wrinkles, 'stroke', O.topDark);
      put(this.neck, 'transform', tf(key3(0, 3, 5, st), M.headY + 6));

      const cx = key3(0, 4, 6, st), cw = key3(26, 22, 14, st);
      put(this.collar, 'd', 'M' + f(cx - cw) + ' -127Q' + f(cx - cw * 0.9) + ' -106 ' + f(cx - 2) + ' -108L' + f(cx) + ' -116L' + f(cx + 2) + ' -108Q' + f(cx + cw * 0.9) + ' -106 ' + f(cx + cw) + ' -127Q' + f(cx) + ' -112 ' + f(cx - cw) + ' -127Z');
      const sc = key3(1, 0.86, 0.5, st), sxc = key3(0, 12, 24, st), R1 = 15, R2 = 6.5, sy = -66;
      let star = '';
      for (let i = 0; i < 10; i++) {
        const r = i % 2 ? R2 : R1, an = -Math.PI / 2 + i * Math.PI / 5;
        star += (i ? 'L' : 'M') + f(sxc + Math.cos(an) * r * sc) + ' ' + f(sy + Math.sin(an) * r);
      }
      put(this.star, 'd', star + 'Z');

      const packOn = this.accessories.backpack;
      shown(this.pack, packOn ? 1 : 0);
      shown(this.straps, packOn ? 1 : 0);
      if (packOn) {
        const body = shape('pack', st);
        put(this.packBody, 'd', spline(body, true));
        const m = (p, q, u) => [lerp(p[0], q[0], u), lerp(p[1], q[1], u)];
        const p1 = m(body[0], body[3], 0.55), p2 = m(body[1], body[2], 0.55), p3 = body[2], p4 = body[3];
        put(this.packFlap, 'd', 'M' + f(p1[0] + 7) + ' ' + f(p1[1]) + 'L' + f(p2[0] - 7) + ' ' + f(p2[1]) + 'L' + f(p3[0] - 10) + ' ' + f(p3[1] - 10) + 'L' + f(p4[0] + 10) + ' ' + f(p4[1] - 10) + 'Z');
        const near = key3(-34, -20, -14, st), far = key3(34, 32, 28, st);
        put(this.straps, 'd', 'M' + f(near) + ' -122Q' + f(near + key3(-3, -6, 14, st)) + ' -84 ' + f(near - key3(4, 8, 4, st)) + ' -52' +
          (st < 0.8 ? 'M' + f(far) + ' -122Q' + f(far + 3) + ' -84 ' + f(far + 4) + ' -52' : ''));
      }
    }
    _renderLeg(leg, j, k, st, far, O) {
      const ang = j[k + 't'], knee = j[k + 's'], ank = j[k + 'foot'];
      const ty = j[k + 'ty'], sy = j[k + 'sy'];
      const hipX = k === 'r' ? key3(-22, -16, -5, st) : key3(22, 18, 6, st);
      put(leg.root, 'transform', tf(hipX, M.hipY));
      const lenT = M.thigh * ty, lenS = M.shin * sy;
      const dT = capsule(lenT, 20, 16), dS = capsule(lenS, 16, 14);
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
      const lx = key3(0, 11, 20, st);
      put(leg.laces, 'd', 'M' + f(lx - 9) + ' 3H' + f(lx + 8) + 'M' + f(lx - 7) + ' 11H' + f(lx + 13));
      put(leg.stripe, 'stroke', O.stripe);
      put(leg.stripe, 'd', 'M' + f(key3(-13, -12, -10, st)) + ' 15H' + f(key3(13, 28, 40, st)));
      put(leg.cuff, 'stroke', O.pantsLight);
      const shadeOff = lerp(8, -7, st);
      put(leg.thighShade, 'transform', tf(shadeOff, 8, 0, 1, Math.max(ty, 0.05)));
      put(leg.shinShade, 'transform', tf(shadeOff, 14, 0, 1, sy));
      put(leg.thighShade, 'fill', O.pantsShade); put(leg.shinShade, 'fill', O.pantsShade);
      put(leg.knee, 'stroke', O.pantsShade);
      shown(leg.thighShade, ty > 0.4 ? 1 : 0);
      const col = far > 0.01 ? hexMix(O.pants, O.pantsShade, far * 0.85) : O.pants;
      leg.fills.forEach(p => put(p, 'fill', col));
    }
    _renderArm(arm, j, k, st, b, far, O) {
      const sx = k === 'r' ? key3(-50, -40, -6, st) : key3(50, 48, 12, st);
      const sy = M.shoulderY - j.shrug * 9 - b * 0.6;
      put(arm.root, 'transform', tf(sx, sy));
      const foreLen = M.foreArm * j[k + 'fl'];
      const uT = tf(0, 0, j[k + 'u']), fT = tf(0, M.upperArm, j[k + 'f']);
      const flip = k === 'r' ? 1 : lerp(-1, 1, smooth(clamp((st - 0.12) / 0.2)));
      const hs = Math.abs(flip) < 0.35 ? 0.35 * (flip < 0 ? -1 : 1) : flip;
      const hT = tf(0, foreLen, j[k + 'h'], hs * 0.68, 0.68);
      arm.upper.forEach(g => put(g, 'transform', uT));
      arm.fore.forEach(g => put(g, 'transform', fT));
      arm.hand.forEach(g => put(g, 'transform', hT));
      const dF = capsule(foreLen, 12, 10);
      arm.forePaths.forEach(p => put(p, 'd', dF));
      put(arm.foreShade, 'd', capsule(foreLen * 0.7, 3, 2.5));
      put(arm.foreShade, 'transform', tf(5, 6));

      const sl = O.sleeve;
      const dS = capsule(sl, 17, 15.5);
      put(arm.sleeveO, 'd', dS); put(arm.sleeve, 'd', dS);
      put(arm.sleeveHem, 'd', 'M-14 ' + (sl + 14) + 'H14');
      put(arm.sleeveHem, 'stroke', O.topDark);
      const sleeveCol = far > 0.01 ? hexMix(O.top, O.topShade, far) : O.top;
      put(arm.sleeve, 'fill', sleeveCol);
      const inFront = k === 'r' || this.armLParent === this.frontArmLayer;
      shown(arm.shoulder, inFront ? 1 : 0);
      put(arm.shoulder, 'fill', sleeveCol);
      put(arm.shoulder, 'cx', f((k === 'r' ? 1 : -1) * key3(8, 6, 0, st)));
      put(arm.shoulder, 'cy', f(key3(3, 0, -7, st)));
      put(arm.shoulder, 'rx', f(key3(18, 18, 19, st)));
      put(arm.shoulder, 'ry', f(key3(18, 17, 14, st)));

      const holding = k === 'r' ? (this.accessories.colored_pencils === true || this.accessories.tablet === true) : this.accessories.teddy_bear === true && j.teddy <= 0.5;
      const curls = [0, 1, 2, 3].map(i => (holding ? 0.82 : j[k + i]));
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
      const W = 23;
      const open = Math.max(0, e.eyeOpen * openMul * (1 - blink));
      const T = 26 * open * 1.33, B = 19 * e.eyeLow * (1 - blink * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const arc = e.eyeLow < 0;         // olhos fechados de riso: só o arco
      shown(eye.white, arc ? 0 : 1);
      shown(eye.iris, arc ? 0 : 1);
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    }
    _renderHead(j, e, st, blink, dt) {
      const headT = tf(key3(0, 4, 6, st), M.headY + j.headY - j.shrug * 5, j.head + e.tilt + this.headTilt);
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
      const drop = Math.max(0, e.mouthOpen + flap * 16 - 14) * 0.62;
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
      front.forEach((p, i) => { if (p[1] > -60 && i !== 16) p[0] += sway * (p[1] + 60) / 60; });
      put(this.hairFront, 'd', spline(front, true));
      const back = shape('hairBack', st);
      back.forEach(p => { if (p[1] > -40) p[0] += sway * 1.6 * (p[1] + 40) / 90; });
      put(this.hairBack, 'd', spline(back, true));
      const shine = key3(0, 8, -4, st);
      put(this.hairShine, 'd', 'M' + f(shine - 38) + ' -146Q' + f(shine - 14) + ' -156 ' + f(shine + 12) + ' -156');

      const gx = clamp(j.gx + e.exGx + this.gaze.x, -1, 1);
      const gy = clamp(j.gy + e.exGy + this.gaze.y, -1, 1);
      const rx = key3(-29, 8, 32, st), lx = key3(29, 52, 66, st), ey = -72;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.72, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, 1 + e.eyeSkew, blink, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx, ey, Math.max(ls, 0.06), -1, e, 1 - e.eyeSkew, blink, gx, gy);
      this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

      const nx = key3(0, 36, 62, st), ny = -46;
      const nrx = lerp(7, 9, st);
      put(this.noseFill, 'cx', f(nx)); put(this.noseFill, 'cy', ny);
      put(this.noseFill, 'rx', f(nrx)); put(this.noseFill, 'ry', 5.5);
      const aC = lerp(Math.PI / 2, 0.2, st), span = lerp(1.9, 1.5, st);
      const arc = [];
      for (let i = 0; i <= 6; i++) {
        const a = aC - span + (2 * span * i) / 6;
        arc.push([nx + Math.cos(a) * nrx, ny + Math.sin(a) * 5.5]);
      }
      put(this.noseLine, 'd', spline(arc, false));
      const cheekW = 15, oval = (x, w) => 'M' + f(x - w) + ' -42a' + f(w) + ' 9 0 1 0 ' + f(2 * w) + ' 0a' + f(w) + ' 9 0 1 0 ' + f(-2 * w) + ' 0Z';
      put(this.cheeks, 'd', oval(rx - 9, cheekW) + (ls > 0.3 ? oval(lx + 7 * ls, cheekW * ls) : ''));
      put(this.cheeks, 'opacity', String(Math.round((0.32 + 0.4 * clamp(e.blush)) * 100) / 100));

      this._renderMouth(e, st, flap);

      const bounce = sway * 2.6;
      put(this.pigtailNear, 'transform', tf(key3(-76, -68, -56, st), key3(-116, -124, -132, st), key3(24, 34, 58, st) - bounce));
      put(this.pigtailFar, 'transform', tf(key3(76, 72, 40, st), key3(-116, -128, -150, st), key3(-24, -14, 30, st) - bounce));
      shown(this.pigtailFar, st < 0.7 ? 1 : 0);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw > 0.04 ? 1 : 0);
      put(this.sweat1, 'transform', tf(lerp(82, 80, st), lerp(-104, -96, st), 12, 0.5 + sw * 0.5));
      put(this.sweat2, 'transform', tf(key3(-84, 84, 86, st), key3(-82, -74, -74, st), -10, 0.38 + sw * 0.38));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -46 + (this.animation === 'none' ? 0.5 : fall) * 20, 0, 0.72));
    }
    _renderBrow(el, x, inner, e, sx, skew) {
      const y = -105 + e.browY - skew;
      const w = 18 * sx;
      const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
      const cy = y - e.browArch * 2.6 - e.browTilt * 0.1;
      put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY + 2) + 'Q' + f(x - w * 0.15 * inner) + ' ' + f(cy) + ' ' + f(x + w * inner) + ' ' + f(inY));
    }
    _renderMouth(e, st, flap) {
      const open = e.mouthOpen + flap * 18;
      const w = (e.mouthW + flap * -3) * key3(1, 0.86, 0.62, st);
      const smile = e.smile, skew = e.skew;
      const lY = -smile * 11 + skew * 5, rY = -smile * 11 - skew * 5;
      put(this.mouth, 'transform', tf(key3(0, 22, 30, st) + e.mouthShift * (1 - st * 0.6), -25));
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
      shown(this.bracelet, a.bracelet ? 1 : 0);
      const hug = j.teddy > 0.5 && a.teddy_bear !== false;
      shown(this.teddyChest, hug ? 1 : 0);
      put(this.teddyChest, 'transform', tf(key3(0, 18, 46, st), -90, 0, key3(1, 0.94, 0.82, st), 1));
      shown(this.teddyHand, a.teddy_bear === true && !hug ? 1 : 0);
      put(this.teddyHand, 'transform', tf(0, 50, 0, 1.5, 1.5));
      shown(this.tablet, a.tablet === true ? 1 : 0);
      shown(this.pencils, a.colored_pencils === true ? 1 : 0);
      const seat = a.seat === 'auto' ? j.seat : (a.seat ? 1 : 0);
      shown(this.seatProp, seat > 0.5 ? 1 : 0);
      /* O banco acompanha o quadril: encosta nele em altura e fica sob ele em posição. */
      const seatScale = (FLOOR - (j.rootY + M.hipY + 20)) / (FLOOR - 192);
      put(this.seatProp, 'transform', 'translate(' + f(j.rootX + key3(0, -6, -16, st)) + ' ' + FLOOR + ') scale(0.74 ' + (Math.round(seatScale * 1000) / 1000) + ') translate(0 ' + -FLOOR + ')');
      shown(this.shadow, a.shadow ? 1 : 0);
      put(this.shadow, 'rx', f(lerp(88, 100, st) * (1 - clamp((BASE_ROOT - j.rootY) / 80) * 0.4)));
    }
  }

  BeaRivera.EXPRESSIONS = Object.keys(EXPRESSIONS);
  BeaRivera.POSES = Object.keys(POSES);
  BeaRivera.ANIMATIONS = ANIMATIONS.slice();
  BeaRivera.DIRECTIONS = Object.keys(DIRECTIONS);
  BeaRivera.ACCESSORIES = ACCESSORIES.slice();
  BeaRivera.VISEMES = Object.keys(VISEMES);
  BeaRivera.PIVOTS = PIVOTS;
  BeaRivera.PALETTE = C;
  return BeaRivera;
});
