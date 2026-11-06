/*!
 * bea — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('bea', function (STH) {
  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
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
  const BASE_ROOT = 158;       // Bea tem ~59% da altura do Dan, com o mesmo chão

  const M = { shoulderY: -104, upperArm: 58, foreArm: 54, hipY: 10, thigh: 70, shin: 72, headY: -128, footH: 30 };
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-50, M.shoulderY], shoulderLeft: [50, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-22, M.hipY], hipLeft: [22, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  
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
  
  const D = {
    arm: { upper: [13, 12], fore: [12, 10], foreShade: [0.7, 3, 2.5, 5, 6], sleeve: [17, 15.5], hem: [14, 14], hemWidth: 4.5, shoulderR: [-50, -40, -6], shoulderL: [50, 48, 12], shrug: 9, breath: 0.6, hand: 0.68,
      patch: { cx: [8, 6, 0], cy: [3, 0, -7], rx: [18, 18, 19], ry: [18, 17, 14] } },
    leg: { thigh: [20, 16], shin: [16, 14], hipR: [-22, -16, -5], hipL: [22, 18, 6], footX: 4, thighShade: [50, 4, 3.5], shinShade: [54, 3.5, 3], shadeX: [8, -7], knee: 'M-8 -2Q0 5 8 -2', kneeWidth: 3.2,
      cuff: 'M-14 -5H14', cuffWidth: 4, stripeWidth: 4.5, stripe: st => 'M' + f(key3(-13, -12, -10, st)) + ' 15H' + f(key3(13, 28, 40, st)), laceColor: C.metalDark, laceWidth: 3,
      laces: st => { const x = key3(0, 11, 20, st); return 'M' + f(x - 9) + ' 3H' + f(x + 8) + 'M' + f(x - 7) + ' 11H' + f(x + 13); } },
    head: { x: [0, 4, 6], shrug: -5, flap: 16, jawFrom: 14, eyeR: [-29, 8, 32], eyeL: [29, 52, 66], eyeY: -72, eyeW: 23, eyeT: 26, iris: 15.5, pupil: 10, shine: [5, -6, 4.6], lid: 5, lash: false,
      browY: -105, browW: 18, browArch: 2.6, browOut: 2, browPull: 0.15, nose: [0, 36, 62], noseY: -46, noseR: [7, 9], noseRy: 5.5,
      mouth: { x: [0, 22, 30], y: -25, corner: 11, skew: 5, round: 26, bow: 7, upMax: 22, teethMax: 12 },
      sweat1: { x: [82, 81, 80], y: [-104, -100, -96], s: 0.5 }, sweat2: { x: [-84, 84, 86], y: [-82, -74, -74], s: 0.38 }, tear: [-46, 20, 0.72] }
  };
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
  
  Object.assign(EXPRESSIONS, {
    worried: { browY: -6, browTilt: 11, eyeOpen: 1, lidTilt: -0.22, mouthW: 14, mouthOpen: 4, smile: -0.45, teeth: 0.6, sweat: 0.5, exGx: -0.2 },
    angry: { browY: 9, browTilt: -12, browArch: 1, eyeOpen: 0.8, lidTilt: 0.46, pupil: 0.84, mouthW: 16, smile: -0.7, tint: 0.55 },
    talking: { smile: 0.3 }
  });
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

  
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [8, 14, 13] });
  const RUNS = {
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
  MOTION.walking = { rate: 7, still: 0.9, run: RUNS.walking };
  MOTION.running.rate = 12;
  MOTION.excited = { rate: 8, run: RUNS.excited };
  MOTION.jumping = { rate: 5, still: 1.57, run: RUNS.jumping };
  C.ink = '#242424';
  OUTFITS.main.top = '#F17C75'; OUTFITS.main.topShade = tone('#F17C75', 0.88); OUTFITS.main.topDark = tone('#F17C75', 0.72);
  const shape = shapeBook(SHAPE);
  const { outlineStyle, lineStyle } = styles(C.ink);
  const cfg = {
    rig: 'human', scale: 0.947, seed: 17, C, M, D, PIVOTS, SHAPE, OUTFITS, BASE_ROOT,
    defaultOutfit: 'main',
    EXPRESSIONS: complete(EXPRESSIONS, EXPRESSION_BASE), POSES, MOTION,
    ANIMATE: Object.assign({ talk() {} }, HUMAN, {
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
    }), ALIASES: { talking: 'talk' },
    accessories: { teddy_bear: 'auto', backpack: false, colored_pencils: false, tablet: false, bracelet: true, seat: 'auto' },
    methods: () => ({
    _build() {
      const n = this._n.bind(this), u = this.prefix;
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'sth-rig', role: 'img', 'aria-label': 'Bea Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
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
    },
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
    },
    _buildTablet(parent) {
      const n = this._n.bind(this);
      const p = this.tablet = n('g', {}, parent, 'tablet');
      n('rect', Object.assign({ x: -60, y: 12, width: 120, height: 84, rx: 10, fill: C.tabletCase }, lineStyle), p);
      n('circle', { cx: 0, cy: 54, r: 9, fill: C.logo }, p);
    },
    _buildPencils(parent) {
      const n = this._n.bind(this);
      const p = this.pencils = n('g', { transform: 'translate(0 -10) scale(1.5)' }, parent, 'colored-pencils');
      [[-16, C.pencil1], [-2, C.pencil2], [12, C.pencil3]].forEach(([y, c]) => {
        n('path', Object.assign({ d: 'M-32 ' + (y + 24) + 'H30V' + (y + 34) + 'H-32Z', fill: c }, lineStyle, { 'stroke-width': 3 }), p);
        n('path', Object.assign({ d: 'M30 ' + (y + 24) + 'L46 ' + (y + 29) + 'L30 ' + (y + 34) + 'Z', fill: C.wood2 }, lineStyle, { 'stroke-width': 3 }), p);
      });
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
    },
    _pigtail(parent, part) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, part);
      n('path', Object.assign({ d: 'M-9 0C-18 14 -14 36 0 48C14 36 18 14 9 0Z', fill: C.hair }, lineStyle), g);
      n('path', { d: 'M-4 12Q-7 26 -1 36', fill: 'none', stroke: C.hairShine, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, g);
      n('circle', Object.assign({ r: 8, fill: C.tie }, lineStyle, { 'stroke-width': 3.5 }), g);
      return g;
    },
    _decorateForearm(fore, k) {
      const n = this._n.bind(this);
      if (k === 'r') {
            const b = this.bracelet = n('g', { transform: 'translate(0 42)' }, fore, 'bracelet');
            [[-8, C.bead1], [0, C.bead2], [8, C.bead3]].forEach(([x, c]) => n('circle', { cx: x, cy: 0, r: 4, fill: c, stroke: C.ink, 'stroke-width': 2 }, b));
          }
          
    },
    _buildHandProps(arm) {
      if (arm.k === 'r') {
        this._buildTablet(arm.propSlot);
        this._buildPencils(arm.propSlot);
      } else {
        this.teddyHand = this._buildTeddy(arm.propSlot, 'teddy-bear');
      }
    },
    _holding(k, j) {
      return k === 'r' ? (this.accessories.colored_pencils === true || this.accessories.tablet === true) : this.accessories.teddy_bear === true && j.teddy <= 0.5;
    },
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
    },
    _renderHair(j, e, st, dt, jaw) {
      const sway = this.hairSwing;
      const front = shape('hairFront', st);
      front.forEach((p, i) => { if (p[1] > -60 && i !== 16) p[0] += sway * (p[1] + 60) / 60; });
      put(this.hairFront, 'd', spline(front, true));
      const back = shape('hairBack', st);
      back.forEach(p => { if (p[1] > -40) p[0] += sway * 1.6 * (p[1] + 40) / 90; });
      put(this.hairBack, 'd', spline(back, true));
      const shine = key3(0, 8, -4, st);
      put(this.hairShine, 'd', 'M' + f(shine - 38) + ' -146Q' + f(shine - 14) + ' -156 ' + f(shine + 12) + ' -156');

      
    },
    _renderMarks(e, st, rx, lx, ls) {
      const cheekW = 15, oval = (x, w) => 'M' + f(x - w) + ' -42a' + f(w) + ' 9 0 1 0 ' + f(2 * w) + ' 0a' + f(w) + ' 9 0 1 0 ' + f(-2 * w) + ' 0Z';
      put(this.cheeks, 'd', oval(rx - 9, cheekW) + (ls > 0.3 ? oval(lx + 7 * ls, cheekW * ls) : ''));
      put(this.cheeks, 'opacity', String(Math.round((0.32 + 0.4 * clamp(e.blush)) * 100) / 100));

      
    },
    _renderEars(j, e, st) {
      const sway = this.hairSwing;
      const bounce = sway * 2.6;
      put(this.pigtailNear, 'transform', tf(key3(-76, -68, -56, st), key3(-116, -124, -132, st), key3(24, 34, 58, st) - bounce));
      put(this.pigtailFar, 'transform', tf(key3(76, 72, 40, st), key3(-116, -128, -150, st), key3(-24, -14, 30, st) - bounce));
      shown(this.pigtailFar, st < 0.7 ? 1 : 0);

      
    },
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
    })
  };
  return cfg;

});
