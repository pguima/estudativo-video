/*!
 * leo — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('leo', function (STH) {
  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
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
  const BASE_ROOT = 2;         // Leo fica entre Mia e Dan em altura, com o mesmo chão

  const M = { shoulderY: -170, upperArm: 100, foreArm: 96, hipY: 10, thigh: 146, shin: 144, headY: -228, footH: 38 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-72, M.shoulderY], shoulderLeft: [72, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-28, M.hipY], hipLeft: [28, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  
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
  
  const D = {
    arm: { fullSleeve: true, upper: [22, 19], fore: [19, 16], foreShade: [0.74, 4.5, 3.5, 9, 8], shoulderR: [-72, -56, -8], shoulderL: [72, 66, 16], shrug: 14, breath: 0.8, hand: 0.86,
      patch: { cx: [12, 10, 0], cy: [4, 0, -10], rx: [25, 25, 26], rxFar: [25, 20, 26], ry: [25, 23, 19] } },
    leg: { thigh: [29, 23], shin: [23, 18], hipR: [-28, -20, -6], hipL: [28, 22, 7], footX: 4, thighShade: [118, 6, 5], shinShade: [112, 5, 4.5], shadeX: [12, -11], knee: 'M-12 -3Q0 7 12 -3', kneeWidth: 3.2,
      cuff: 'M-17 -6H17', cuffWidth: 9, stripeWidth: 4.5, stripe: st => 'M' + f(key3(-16, -14, -12, st)) + ' 20H' + f(key3(16, 36, 52, st)), laceColor: C.metalDark, laceWidth: 3,
      laces: st => { const x = key3(0, 14, 24, st); return 'M' + f(x - 9) + ' 3H' + f(x + 8) + 'M' + f(x - 7) + ' 11H' + f(x + 13); } },
    head: { x: [0, 6, 12], shrug: -4, flap: 18, jawFrom: 14, eyeR: [-28, 8, 34], eyeL: [28, 50, 66], eyeY: -86, eyeW: 20, eyeT: 24, iris: 12.5, pupil: 8.5, shine: [4, -5, 3.8], lid: 6, lash: false,
      browY: -116, browW: 21, browArch: 2.6, browOut: 2, browPull: 0.15, nose: [0, 38, 64], noseY: -54, noseR: [10, 13], noseRy: 9,
      mouth: { x: [0, 22, 30], y: -23, corner: 11, skew: 5, round: 26, bow: 7, upMax: 22, teethMax: 12 },
      sweat1: { x: [84, 82, 80], y: [-112, -109, -106], s: 0.5 }, sweat2: { x: [-90, 86, 88], y: [-92, -82, -82], s: 0.38 }, tear: [-56, 20, 0.72] }
  };
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
  
  Object.assign(EXPRESSIONS, {
    angry: { browY: 10, browTilt: -13, browArch: 1, eyeOpen: 0.76, lidTilt: 0.5, pupil: 0.82, mouthW: 25, mouthOpen: 12, smile: -0.55, teeth: 1, grit: 1, tint: 0.7 },
    surprised: { browY: -12, browArch: 6, eyeOpen: 1.12, eyeLow: 1.06, lidTilt: 0, pupil: 0.84, mouthW: 13, mouthOpen: 14, smile: 0, tongue: 0.3 },
    talking: { smile: 0.2 }
  });
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

  
  const POSE_MOTION = {
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
    },
    texting: typingThumbs
  };
  const RATES = { texting: 9, gaming: 11, using_laptop: 10, using_phone: 3, celebrating: 5.5 };
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [14, 24, 20] });
  Object.keys(POSE_MOTION).forEach(k => { MOTION[k] = { rate: RATES[k], run: POSE_MOTION[k], still: k === 'celebrating' ? 1.57 : undefined }; });
  C.ink = '#242424';
  OUTFITS.hoodie.top = '#263B70'; OUTFITS.hoodie.topShade = tone('#263B70', 0.78); OUTFITS.hoodie.topDark = tone('#263B70', 0.56);
  const shape = shapeBook(SHAPE);
  const { outlineStyle, lineStyle } = styles(C.ink);
  const cfg = {
    rig: 'human', scale: 0.914, seed: 13, C, M, D, PIVOTS, SHAPE, OUTFITS, BASE_ROOT,
    defaultOutfit: 'hoodie',
    EXPRESSIONS: complete(EXPRESSIONS, EXPRESSION_BASE), POSES, MOTION,
    ANIMATE: Object.assign({ talk() {} }, HUMAN, { typing(j, t, w) { const o = lerpDict(j, j, 1); typingFingers(o, t * 10); for (const k in j) j[k] = lerp(j[k], o[k], w); } }), ALIASES: { talking: 'talk' },
    accessories: { smartphone: 'auto', headphones: false, laptop: 'auto', backpack: false, seat: 'auto' },
    methods: () => ({
    _build() {
      const n = this._n.bind(this), u = this.prefix;
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'sth-rig', role: 'img', 'aria-label': 'Leo Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
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
    },
    _buildHandPhone(parent) {
      const n = this._n.bind(this);
      const p = this.handPhone = n('g', {}, parent, 'smartphone');
      n('rect', Object.assign({ x: -18, y: -8, width: 36, height: 74, rx: 7, fill: C.device }, lineStyle), p);
      n('circle', { cx: -8, cy: 2, r: 4.5, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
      n('circle', { cx: -8, cy: 14, r: 3.5, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
    },
    _buildClosedLaptop(parent) {
      const n = this._n.bind(this);
      const p = this.laptopClosed = n('g', {}, parent, 'laptop-closed');
      n('rect', Object.assign({ x: -62, y: 10, width: 124, height: 88, rx: 6, fill: C.laptop }, lineStyle), p);
      n('path', { d: 'M-58 90H58', stroke: C.laptopDark, 'stroke-width': 3 }, p);
      n('circle', { cx: 0, cy: 54, r: 11, fill: C.logo }, p);
    },
    _buildChestPhone(parent) {
      const n = this._n.bind(this);
      const p = this.chestPhone = n('g', {}, parent, 'smartphone-held');
      this.chestPhoneBody = n('rect', Object.assign({ rx: 7, fill: C.device }, lineStyle), p);
      this.chestPhoneLens = n('circle', { r: 4, fill: C.lens, stroke: C.deviceEdge, 'stroke-width': 2 }, p);
    },
    _buildLaptop(parent) {
      const n = this._n.bind(this);
      const g = this.laptopOpen = n('g', {}, parent, 'laptop');
      this.laptopLidEdge = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 12, 'stroke-linecap': 'round' }, g);
      this.laptopLidEdgeF = n('path', { fill: 'none', stroke: C.laptop, 'stroke-width': 4, 'stroke-linecap': 'round' }, g);
      this.laptopLid = n('path', Object.assign({ fill: C.laptop }, lineStyle), g, 'laptop-lid');
      this.laptopLogo = n('ellipse', { ry: 11, fill: C.logo }, g, 'laptop-logo');
    },
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
    },
    _ear(parent) {
      const g = this._n('g', {}, parent);
      this._n('path', Object.assign({ d: 'M-3 -19Q-18 -21 -16 -2Q-14 19 2 16Q8 0 -3 -19Z', fill: C.skin }, lineStyle), g);
      this._n('path', { d: 'M-5 -9Q-11 -8 -9 2', fill: 'none', stroke: C.skinShade, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, g);
      return g;
    },
    _buildHandProps(arm) {
      if (arm.k === 'r') this._buildHandPhone(arm.propSlot);
      else this._buildClosedLaptop(arm.propSlot);
    },
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
    },
    _renderHair(j, e, st, dt, jaw) {
      const sway = this.hairSwing;
      const front = shape('hairFront', st);
      front.forEach(p => { if (p[1] < -165) p[0] += sway * 0.5; });
      put(this.hairFront, 'd', spline(front, true));
      put(this.hairBack, 'd', spline(shape('hairBack', st), true));
      const shine = key3(0, 8, -6, st);
      put(this.hairShine, 'd', 'M' + f(shine - 34) + ' -170Q' + f(shine - 12) + ' -180 ' + f(shine + 12) + ' -176');

      
    },
    _renderMarks(e, st, rx, lx, ls) {
      const fr = (x, y) => 'M' + f(x) + ' ' + f(y) + 'h.1';
      const freck = fr(rx - 8, -58) + fr(rx + 2, -54) + fr(rx + 12, -59) + (ls > 0.3 ? fr(lx - 12, -59) + fr(lx - 2 * ls, -54) + fr(lx + 8 * ls, -58) : '');
      put(this.freckles, 'd', freck);
      const bl = clamp(e.blush);
      shown(this.blush, bl > 0.02 ? 0.5 * bl : 0);
      const cheek = (x, w) => 'M' + f(x - w) + ' -46a' + f(w) + ' 9 0 1 0 ' + f(2 * w) + ' 0a' + f(w) + ' 9 0 1 0 ' + f(-2 * w) + ' 0Z';
      put(this.blush, 'd', cheek(rx - 2, 17) + (ls > 0.3 ? cheek(lx, 17 * ls) : ''));

      
    },
    _renderEars(j, e, st) {
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

      
    },
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
    })
  };
  return cfg;

});
