/*!
 * dan — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('dan', function (STH) {
  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
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
    const OUTFITS = {};
  const BASE_ROOT = 0;
  const M = {
    shoulderY: -192, upperArm: 104, foreArm: 98, hipY: 10, thigh: 146, shin: 146,
    neckY: -226, headY: -256, footH: 40
  };

  /* Pontos de articulação de cada parte, em coordenadas do modelo. */
  const PIVOTS = {
    pelvis: [0, 0], torso: [0, 0], head: [0, M.headY],
    shoulderRight: [-92, M.shoulderY], shoulderLeft: [92, M.shoulderY],
    elbow: [0, M.upperArm], wrist: [0, M.foreArm],
    hipRight: [-38, M.hipY], hipLeft: [38, M.hipY], knee: [0, M.thigh], ankle: [0, M.shin]
  };

  
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
    shoe: {
      front: [[-25, -8], [-26, 10], [-33, 24], [-32, 36, 1], [32, 36, 1], [33, 24], [26, 10], [25, -8]],
      side: [[-25, -8], [-27, 12], [-29, 24], [-29, 36, 1], [76, 36, 1], [80, 23], [52, 6], [25, -8]]
    },
    sole: {
      front: [[-33, 27, 1], [-34, 40, 1], [34, 40, 1], [33, 27, 1]],
      side: [[-30, 27, 1], [-30, 40, 1], [82, 40, 1], [80, 27, 1]]
    }
  };
  
  const { outlineStyle, lineStyle } = styles('#242424');
  const D = {
    arm: { upper: [23, 21], fore: [21, 17], foreShade: [0.8, 6, 5, 10, 8], sleeve: [29, 28], hem: [27, 16], hemWidth: 5, shoulderR: [-90, -62, -8], shoulderL: [90, 66, 18], shrug: 10, breath: 0.8, hand: 1,
      patch: { cx: [15, 12, 0], cy: [5, 0, -12], rx: [33, 33, 35], ry: [33, 30, 24] } },
    leg: { thigh: [34, 27], shin: [27, 26], hipR: [-38, -22.5, -7], hipL: [38, 23.5, 9], footX: 5, thighShade: [120, 8, 7], shinShade: [112, 7, 7], shadeX: [15, -14], knee: 'M-15 -3Q0 8 15 -3', kneeWidth: 3.5,
      cuff: 'M-26 -10H26', cuffWidth: 6, stripeWidth: 4, stripe: () => 'M-26 10Q0 16 26 10', laceColor: C.lace, laceWidth: 3.5,
      laces: st => { const x = lerp(0, 26, st); return 'M' + f(x - 12) + ' 2H' + f(x + 10) + 'M' + f(x - 10) + ' 12H' + f(x + 16); } },
    head: { x: [0, 4, 8], shrug: 4, flap: 20, jawFrom: 16, eyeR: [-34, 6, 36], eyeL: [34, 58, 74], eyeY: -84, eyeW: 20, eyeT: 22, iris: 12.5, pupil: 8.5, shine: [4, -5, 3.6], lid: 6.5, lash: false,
      browY: -121, browW: 23, browArch: 2.4, browOut: 0, browPull: 0, nose: [0, 44, 72], noseY: -55, noseR: [14, 15], noseRy: 12,
      mouth: { x: [0, 26, 36], y: -24, corner: 12, skew: 6, round: 30, bow: 8, upMax: 26, teethMax: 14 },
      sweat1: { x: [84, 86, 88], y: [-128, -120, -112], s: 0.55 }, sweat2: { x: [-90, 98, 98], y: [-100, -92, -92], s: 0.4 }, tear: [-56, 22, 0.8] }
  };
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
  
  Object.assign(EXPRESSIONS, {
    surprised: { browY: -13, browArch: 6, eyeOpen: 1.14, eyeLow: 1.06, pupil: 0.84, mouthW: 15, mouthOpen: 16, smile: 0, tongue: 0.3 },
    thinking: { browY: -3, browTilt: 4, browSkew: 7, eyeOpen: 0.84, exGx: 0.6, exGy: -0.75, mouthW: 14, smile: -0.05, skew: 0.35, mouthShift: 8, tilt: 3 },
    talking: { smile: 0.2 }
  });
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

  
  POSES.walking = pose({ spine: 1 }, { spine: 3, rf: -18, lf: -18 }, { plant: 1, farFront: 0 }, { spine: 2, rf: -14, lf: -14 });
  const MOTION = Object.assign(cycles({ root: 0, runBounce: [16, 26, 22] }), {
    working: { rate: 4.2, run(j, ph) { j.rh += 15 * Math.sin(ph * 1.6); j.rf += 4 * Math.sin(ph * 1.6 + 0.7); j.lh += 4 * Math.sin(ph * 0.8); j.head += 1.2 * Math.sin(ph * 0.5); } }
  });
  C.ink = '#242424'; C.navy = '#243B5A'; C.navyShade = tone('#243B5A', 0.78); C.navyDark = tone('#243B5A', 0.6);
  OUTFITS.main = { top: C.navy, topShade: C.navyShade, topDark: C.navyDark, pants: C.jeans, pantsShade: C.jeansShade, pantsLight: C.jeansLight, shoe: C.boot, sole: C.sole, stripe: C.bootShade, sleeve: 60 };
  const shape = shapeBook(SHAPE);
    const cfg = {
    rig: 'human', scale: 1, seed: 7, C, M, D, PIVOTS, SHAPE, OUTFITS, BASE_ROOT,
    defaultOutfit: 'main',
    EXPRESSIONS: complete(EXPRESSIONS, EXPRESSION_BASE), POSES, MOTION,
    ANIMATE: Object.assign({ talk() {} }, HUMAN, {}), ALIASES: { talking: 'talk' },
    accessories: { toolbelt: false, screwdriver: false, pliers: false, toolbox: false, seat: false },
    methods: () => ({
    _build() {
      const u = this.uid;
      const svg = this.svg = this._n('svg', { viewBox: VIEWBOX, class: 'sth-rig', role: 'img', 'aria-label': 'Dan Rivera', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = this._n('defs', {}, svg);
      this.clipEyeR = this._n('path', {}, this._n('clipPath', { id: u + '-clip-eye-r' }, defs));
      this.clipEyeL = this._n('path', {}, this._n('clipPath', { id: u + '-clip-eye-l' }, defs));
      this.clipMouth = this._n('path', {}, this._n('clipPath', { id: u + '-clip-mouth' }, defs));

      this.shadow = this._n('ellipse', { cx: 0, cy: FLOOR + 6, rx: 150, ry: 17, fill: '#000', 'fill-opacity': 0.22 }, svg, 'shadow');
      this.flip = this._n('g', {}, svg, 'character');
      this._buildProps(this.flip);

      const rig = this.rig = this._n('g', {}, this.flip, 'pelvis', PIVOTS.pelvis);
      this.spineNodes = [];
      const spineLayer = (name) => { const g = this._n('g', {}, rig, name, PIVOTS.torso); this.spineNodes.push(g); return g; };

      this.backArmLayer = spineLayer('layer-back-arm');
      this.hipsO = this._n('path', Object.assign({}, outlineStyle), rig, 'hips-outline');
      this.legL = this._buildLeg(rig, 'l', 'left');
      this.legR = this._buildLeg(rig, 'r', 'right');
      this.hipsF = this._n('path', { fill: C.jeans }, rig, 'hips');

      const neck = this.neck = this._n('g', {}, spineLayer('layer-neck'), 'neck');
      this._n('path', Object.assign({ d: capsule(46, 29, 31), fill: C.skin }, lineStyle), neck);
      this._n('path', { d: 'M-27 2H27V16Q0 28 -27 16Z', fill: C.skinShade }, neck);

      const torso = spineLayer('torso');
      this.torsoShape = this._n('path', Object.assign({ fill: C.navy }, lineStyle), torso);
      this.torsoShade = this._n('path', { fill: C.navyShade }, torso);
      this.wrinkles = this._n('path', { fill: 'none', stroke: C.navyDark, 'stroke-width': 3.5, 'stroke-linecap': 'round' }, torso);

      this.collar = this._n('path', { fill: 'none', stroke: C.navyDark, 'stroke-width': 9, 'stroke-linecap': 'round' }, torso, 'collar');

      this.belt = this._buildBelt(spineLayer('toolbelt'));

      this.headLayer = spineLayer('layer-head');
      this._buildHead(this.headLayer);

      this.frontArmLayer = spineLayer('layer-front-arm');
      this.armL = this._buildArm(this.frontArmLayer, 'l', 'left');
      this.armR = this._buildArm(this.frontArmLayer, 'r', 'right');
      this.armLParent = this.frontArmLayer;
    },
    _buildBelt(g) {
      const belt = { g };
      belt.band = this._n('path', Object.assign({ fill: C.leather }, lineStyle), g, 'belt');
      belt.buckle = this._n('rect', Object.assign({ width: 26, height: 22, rx: 3, fill: C.metal }, lineStyle), g);
      belt.pouch = this._n('g', {}, g, 'pouch');
      this._n('rect', Object.assign({ x: 8, y: -24, width: 9, height: 28, rx: 3, fill: C.toolAlt }, lineStyle), belt.pouch);
      this._n('path', Object.assign({ d: 'M-14 -30L-6 -30L-4 4L-12 4Z', fill: C.metal }, lineStyle), belt.pouch);
      this._n('path', Object.assign({ d: 'M-26 0H26L22 52Q0 62 -22 52Z', fill: C.leatherDark }, lineStyle), belt.pouch);
      this._n('path', { d: 'M-22 14H22', stroke: C.leather, 'stroke-width': 4, fill: 'none' }, belt.pouch);
      belt.pouch2 = this._n('g', {}, g, 'pouch-far');
      this._n('path', Object.assign({ d: 'M-22 0H22L18 42Q0 50 -18 42Z', fill: C.leatherDark }, lineStyle), belt.pouch2);
      return belt;
    },
    _buildProps(parent) {
      const seat = this.seatProp = this._n('g', {}, parent, 'seat');
      this._n('rect', Object.assign({ x: -74, y: 182, width: 148, height: 24, rx: 6, fill: C.wood }, lineStyle), seat);
      this._n('path', Object.assign({ d: 'M-62 206L-74 340H-58L-40 206Z', fill: C.woodDark }, lineStyle), seat);
      this._n('path', Object.assign({ d: 'M62 206L74 340H58L40 206Z', fill: C.woodDark }, lineStyle), seat);
      this._n('path', Object.assign({ d: 'M-64 276H64V290H-64Z', fill: C.wood }, lineStyle), seat);

      const box = this.boxProp = this._n('g', { transform: 'translate(232 ' + (FLOOR - 98) + ')' }, parent, 'toolbox');
      this._n('path', Object.assign({ d: 'M-42 0V-22Q-42 -30 -34 -30H34Q42 -30 42 -22V0H30V-18H-30V0Z', fill: C.metalDark }, lineStyle), box);
      this._n('rect', Object.assign({ x: -82, y: 0, width: 164, height: 98, rx: 8, fill: C.tool }, lineStyle), box);
      this._n('rect', { x: -80, y: 30, width: 160, height: 7, fill: '#a92d1f' }, box);
      this._n('rect', Object.assign({ x: -14, y: 24, width: 28, height: 22, rx: 3, fill: C.metal }, lineStyle), box);
    },
    _buildHead(parent) {
      const u = this.uid;
      const head = this.head = this._n('g', {}, parent, 'head', PIVOTS.head);
      this.earBack = this._n('g', {}, head, 'ears-back');
      this.earFar = this._ear(this.earBack);
      this.earNear = this._ear(this.earBack);
      this.headShape = this._n('path', Object.assign({ fill: C.skin }, lineStyle), head, 'face');
      this.stubble = this._n('path', { fill: C.stubble }, head, 'stubble');
      this.headShade = this._n('path', { fill: C.skinShade, 'fill-opacity': 0.75 }, head);
      this.tint = this._n('path', {}, head, 'tint');

      const mouth = this.mouth = this._n('g', {}, head, 'mouth');
      this.mouthShape = this._n('path', Object.assign({ fill: C.mouth }, lineStyle), mouth);
      const inner = this._n('g', { 'clip-path': 'url(#' + u + '-clip-mouth)' }, mouth);
      this.tongue = this._n('ellipse', { fill: C.tongue }, inner);
      this.teeth = this._n('rect', { fill: C.teeth, x: -60, width: 120 }, inner);
      this.gritLines = this._n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 2.5 }, inner);
      this.mouthLine = this._n('path', Object.assign({ fill: 'none' }, lineStyle), mouth);

      this.eyeR = this._eye(head, 'right', u + '-clip-eye-r');
      this.eyeL = this._eye(head, 'left', u + '-clip-eye-l');
      this.noseFill = this._n('ellipse', { fill: C.skin }, head, 'nose');
      this.noseLine = this._n('path', Object.assign({ fill: 'none' }, lineStyle), head);
      this.hair = this._n('path', Object.assign({ fill: C.hair }, lineStyle), head, 'hair');
      this.hairShine = this._n('path', { fill: 'none', stroke: '#5a4231', 'stroke-width': 7, 'stroke-linecap': 'round' }, head);
      this.browR = this._n('path', { fill: 'none', stroke: C.brow, 'stroke-width': 11.5, 'stroke-linecap': 'round' }, head, 'brow-right');
      this.browL = this._n('path', { fill: 'none', stroke: C.brow, 'stroke-width': 11.5, 'stroke-linecap': 'round' }, head, 'brow-left');
      this.earTop = this._n('g', {}, head, 'ears-top');
      this.sweat = this._n('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat);
      this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
    },
    _ear(parent) {
      const g = this._n('g', {}, parent);
      this._n('path', Object.assign({ d: 'M-4 -24Q-22 -26 -20 -2Q-18 24 2 20Q10 0 -4 -24Z', fill: C.skin }, lineStyle), g);
      this._n('path', { d: 'M-6 -12Q-14 -10 -11 3', fill: 'none', stroke: C.skinShade, 'stroke-width': 4, 'stroke-linecap': 'round' }, g);
      return g;
    },
    _buildHandProps(arm) {
      if (arm.k === 'r') {
        const s = this.screwdriver = this._n('g', {}, arm.propSlot, 'screwdriver');
        this._n('rect', Object.assign({ x: -28, y: 22, width: 54, height: 20, rx: 8, fill: C.toolAlt }, lineStyle), s);
        this._n('rect', Object.assign({ x: 26, y: 28, width: 58, height: 8, fill: C.metal }, lineStyle), s);
        this._n('path', Object.assign({ d: 'M84 28L96 32L84 36Z', fill: C.metalDark }, lineStyle), s);
      } else {
        const p = this.pliers = this._n('g', {}, arm.propSlot, 'pliers');
        this._n('path', Object.assign({ d: 'M-20 24Q0 16 26 26L26 32Q0 26 -20 34Z', fill: C.tool }, lineStyle), p);
        this._n('path', Object.assign({ d: 'M-20 42Q0 44 26 36L26 30Q0 36 -20 34Z', fill: C.tool }, lineStyle), p);
        this._n('path', Object.assign({ d: 'M24 24L66 28L68 31L24 38Z', fill: C.metal }, lineStyle), p);
        this._n('path', { d: 'M28 31H64', stroke: C.ink, 'stroke-width': 2.5, fill: 'none' }, p);
      }
    },
    _renderBody(st, O, j, b) {
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
    },
    _renderHair(j, e, st, dt, jaw) {
      put(this.stubble, 'd', spline(jaw(shape('stubble', st), [2, 3, 4], [1, 5]), true));
      put(this.hair, 'd', spline(shape('hair', st), true));
      const shine = key3(0, 10, -2, st);
      put(this.hairShine, 'd', 'M' + f(shine - 44) + ' -170Q' + f(shine - 16) + ' -182 ' + f(shine + 16) + ' -181');
    },
    _renderEars(j, e, st) {
      const nearX = lerp(-81, -20, st), nearY = -66;
      put(this.earNear, 'transform', tf(nearX, nearY, 0, 1, 1));
      put(this.earFar, 'transform', tf(lerp(81, 60, st), nearY, 0, -1, 1));
      shown(this.earFar, st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);
    },
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
    })
  };
  return cfg;

});
