/*!
 * mia — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('mia', function (STH) {
  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
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
  const BASE_ROOT = 18;        // Mia é ~7% mais baixa que Dan, com o mesmo chão

  const M = { shoulderY: -172, upperArm: 94, foreArm: 90, hipY: 10, thigh: 138, shin: 136, headY: -232, footH: 38 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-76, M.shoulderY], shoulderLeft: [76, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-34, M.hipY], hipLeft: [34, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  
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
  
  const D = {
    arm: { upper: [18, 16.5], fore: [16.5, 13], foreShade: [0.74, 4.5, 3.5, 8, 8], sleeve: [23, 21], hem: [20, 16], hemWidth: 4.5, shoulderR: [-76, -56, -8], shoulderL: [76, 60, 16], shrug: 12, breath: 0.8, hand: 0.86,
      patch: { cx: [12, 10, 0], cy: [4, 0, -10], rx: [27, 27, 28], ry: [27, 25, 20] } },
    leg: { thigh: [32, 24], shin: [24, 20], hipR: [-34, -24, -7], hipL: [34, 26, 8], footX: 4, thighShade: [112, 6.5, 5.5], shinShade: [104, 5.5, 5.5], shadeX: [12, -11], knee: 'M-12 -3Q0 7 12 -3', kneeWidth: 3.2,
      cuff: 'M-21 -9H21', cuffWidth: 5, stripeWidth: 4.5, stripe: st => 'M' + f(key3(-16, -14, -12, st)) + ' 20H' + f(key3(16, 36, 52, st)), laceColor: C.metalDark, laceWidth: 3,
      laces: st => { const x = key3(0, 14, 24, st); return 'M' + f(x - 9) + ' 3H' + f(x + 8) + 'M' + f(x - 7) + ' 11H' + f(x + 13); } },
    head: { x: [0, 5, 7], shrug: -8, flap: 18, jawFrom: 14, eyeR: [-31, 6, 34], eyeL: [31, 54, 70], eyeY: -80, eyeW: 21, eyeT: 24, iris: 13.5, pupil: 8.5, shine: [4, -5, 3.8], lid: 6, lash: true,
      browY: -113, browW: 21, browArch: 2.6, browOut: 2, browPull: 0.15, nose: [0, 40, 68], noseY: -50, noseR: [9, 11], noseRy: 7.5,
      mouth: { x: [0, 24, 33], y: -23, corner: 11, skew: 5, round: 26, bow: 7, upMax: 22, teethMax: 12 },
      sweat1: { x: [96, 90, 84], y: [-122, -117, -112], s: 0.5 }, sweat2: { x: [-100, 92, 92], y: [-96, -88, -88], s: 0.38 }, tear: [-52, 20, 0.72] }
  };
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
  
  Object.assign(EXPRESSIONS, {
    surprised: { browY: -12, browArch: 6, eyeOpen: 1.12, eyeLow: 1.06, pupil: 0.84, mouthW: 13, mouthOpen: 14, smile: 0, tongue: 0.3 },
    talking: { smile: 0.25 }
  });
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

  
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [14, 24, 20] });
  C.ink = '#242424';
  OUTFITS.casual.top = '#247F79'; OUTFITS.casual.topShade = tone('#247F79', 0.8); OUTFITS.casual.topDark = tone('#247F79', 0.62);
  OUTFITS.scrubs.top = tone('#247F79', 1.18); OUTFITS.scrubs.topShade = '#247F79'; OUTFITS.scrubs.topDark = tone('#247F79', 0.75);
  OUTFITS.scrubs.pants = tone('#247F79', 1.1); OUTFITS.scrubs.pantsShade = tone('#247F79', 0.85); OUTFITS.scrubs.pantsLight = tone('#247F79', 1.35); OUTFITS.scrubs.stripe = '#247F79';
  C.badgeStripe = '#247F79';
  const shape = shapeBook(SHAPE);
  const { outlineStyle, lineStyle } = styles(C.ink);
  const cfg = {
    rig: 'human', scale: 1, seed: 11, C, M, D, PIVOTS, SHAPE, OUTFITS, BASE_ROOT,
    defaultOutfit: 'casual', HAIR: ['down', 'up'],
    EXPRESSIONS: complete(EXPRESSIONS, EXPRESSION_BASE), POSES, MOTION,
    ANIMATE: Object.assign({ talk() {} }, HUMAN, {}), ALIASES: { talking: 'talk' },
    accessories: { watch: true, badge: true, seat: false },
    methods: () => ({
    _build() {
      const n = this._n.bind(this), u = this.prefix;
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'sth-rig', role: 'img', 'aria-label': 'Mia Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
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
    },
    _buildBadge(parent) {
      const n = this._n.bind(this);
      const b = this.badge = n('g', {}, parent, 'badge');
      n('rect', { x: -5, y: -10, width: 10, height: 12, rx: 2, fill: C.clip, stroke: C.ink, 'stroke-width': 2.5 }, b);
      n('rect', Object.assign({ x: -15, y: 0, width: 30, height: 38, rx: 3, fill: C.badge }, lineStyle, { 'stroke-width': 3 }), b);
      n('rect', { x: -13, y: 2, width: 26, height: 8, fill: C.badgeStripe }, b);
      n('circle', { cx: 0, cy: 19, r: 6, fill: C.skinShade }, b);
      n('path', { d: 'M-8 32H8', stroke: C.metalDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, b);
    },
    _buildSeat(parent) {
      const n = this._n.bind(this);
      const seat = this.seatProp = n('g', {}, parent, 'seat');
      n('rect', Object.assign({ x: -70, y: 192, width: 140, height: 22, rx: 6, fill: C.wood }, lineStyle), seat);
      n('path', Object.assign({ d: 'M-58 214L-70 340H-54L-38 214Z', fill: C.woodDark }, lineStyle), seat);
      n('path', Object.assign({ d: 'M58 214L70 340H54L38 214Z', fill: C.woodDark }, lineStyle), seat);
      n('path', Object.assign({ d: 'M-60 282H60V295H-60Z', fill: C.wood }, lineStyle), seat);
    },
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
    },
    _ear(parent) {
      const g = this._n('g', {}, parent);
      this._n('path', Object.assign({ d: 'M-3 -19Q-18 -21 -16 -2Q-14 19 2 16Q8 0 -3 -19Z', fill: C.skin }, lineStyle), g);
      this._n('path', { d: 'M-5 -9Q-11 -8 -9 2', fill: 'none', stroke: C.skinShade, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, g);
      return g;
    },
    _decorateForearm(fore, k) {
      const n = this._n.bind(this);
      if (k === 'r') {
            this.watch = n('g', { transform: 'translate(0 72)' }, fore, 'watch');
            n('rect', Object.assign({ x: -17, y: -5, width: 34, height: 10, rx: 3, fill: C.watchBand }, lineStyle, { 'stroke-width': 3 }), this.watch);
            n('circle', Object.assign({ r: 7.5, fill: C.watchFace }, lineStyle, { 'stroke-width': 3 }), this.watch);
          }
          
    },
    _renderBody(st, O, j, b) {
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
    },
    _renderHair(j, e, st, dt, jaw) {
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

      
    },
    _renderMarks(e, st, rx) {
      put(this.mole, 'cx', f(rx - 4)); put(this.mole, 'cy', -44);
    },
    _renderEars(j, e, st) {
      const down = this.hairStyle === 'down';
      const nearY = -70;
      put(this.earNear, 'transform', tf(lerp(-75, -18, st), nearY));
      put(this.earFar, 'transform', tf(lerp(75, 56, st), nearY, 0, -1, 1));
      shown(this.earNear, down ? 0 : 1);
      shown(this.earFar, !down && st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);

      
    },
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
    })
  };
  return cfg;

});
