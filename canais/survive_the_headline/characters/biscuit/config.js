/*!
 * biscuit — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('biscuit', function (STH) {
  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
  const VIEW_SCALE = 0.8;
  const C = {
    ink: '#1b1a22', fur: '#e0a24a', furShade: '#c9863a', furFar: '#c98a3f', furDark: '#b5752f',
    ear: '#6b3f22', earShade: '#54301a', muzzle: '#f7e6c8', muzzleShade: '#e8cfa6', chest: '#fff8ec',
    nose: '#1f1b1e', noseShine: '#6a6470', brow: '#6b3f22',
    eyeWhite: '#ffffff', iris: '#6b4226', mouth: '#5a1c22', tongue: '#ec7d86', tongueLine: '#c95d68', teeth: '#fbf7ee',
    sweat: '#8fd6ff', collar: '#d9302f', collarDark: '#a81f22', medal: '#ffc62e', medalDark: '#d99a12',
    bone: '#f4efe2', boneShade: '#d9d0ba', bowl: '#2a7fb8', bowlDark: '#1f608c', food: '#9a5a2c', foodDark: '#744119',
    ball: '#c8e03a', ballLine: '#fbfbf4', zzz: '#9fb4d9'
  };
  const L = { fu: 38, fl: 34, bu: 36, bl: 36, paw: 14, tailA: 34, tailB: 28 };

  /* Pontos do esqueleto: f = para a frente, y = para baixo, s = lateral. */
  const JOINT = {
    frontNear: [72, 20, -30], frontFar: [72, 20, 30], backNear: [-76, 20, -38], backFar: [-76, 20, 38],
    neckBase: [68, -28, 0], head: [92, -50, 0], tail: [-106, -30, 0]
  };

  
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


  ANIMATE.bark = function () {}; ANIMATE.pant = function () {};
  C.ink = '#242424'; C.fur = '#C58A45'; C.furShade = tone('#C58A45', 0.86); C.furFar = tone('#C58A45', 0.88); C.furDark = tone('#C58A45', 0.74);
  return {
    rig: 'quadruped', scale: 1.009, seed: 23, init() { this.earSwing = 0; this.earVel = 0; }, C, L, JOINT, SHAPE, VIEW_SCALE, POSES, POSE_MOTION,
    defaultDirection: 'right', EXPRESSIONS, ANIMATE, ALIASES: { talking: 'bark', talk: 'bark' },
    accessories: { collar: true, bone: false, bowl: false, ball: 'auto' }
  };
});
