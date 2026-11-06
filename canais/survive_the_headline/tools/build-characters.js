/*
 * Gera characters/<nome>/config.js e engine/rigs/QuadrupedRig.js a partir dos
 * personagens aprovados, sem redesenhar nada. Só precisa rodar de novo se os
 * arquivos de origem mudarem: depois da migração, config.js é a fonte oficial.
 */
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const legacy = path.resolve(root, '_marca', 'personagens_originais');
const read = f => fs.readFileSync(path.join(legacy, f), 'utf8');

const between = (s, a, b) => { const i = s.indexOf(a); if (i < 0) throw new Error('sem início: ' + a); const k = s.indexOf(b, i + a.length); if (k < 0) throw new Error('sem fim: ' + b); return s.slice(i, k); };
/* Métodos no nível de 4 espaços de um bloco de código. */
function methods(text) {
  const out = {}; const lines = text.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^    (?:get )?([_a-zA-Z]+)\(.*\) \{(.*)$/);
    if (!m) continue;
    if (/},?$/.test(m[2].trim())) { out[m[1]] = lines[i].replace(/,$/, ''); continue; }
    let k = i; while (!/^    },?$/.test(lines[k])) k++;
    out[m[1]] = lines.slice(i, k + 1).join('\n'); i = k;
  }
  return out;
}
const pick = (table, names) => names.map(n => { if (!table[n]) throw new Error('sem método ' + n); return table[n]; }).join(',\n');

const HEAD = `  const { lerp, clamp, smooth, ease, f, key3, spline, capsule, lerpDict, put, tf, shown, hexMix, tone, styles, shapeBook, FLOOR, LINE, VIEWBOX } = STH.SVGRenderer;
  const { hands, poseMaker, cycles } = STH.PoseController;
  const { complete } = STH.ExpressionEngine;
  const { HUMAN } = STH.AnimationEngine;
`;
const footer = (name, block) => `  const shape = shapeBook(SHAPE);
  const { outlineStyle, lineStyle } = styles(C.ink);
${block}
`;
const talking = { talking: { smile: 0.2 } };
const writeConfig = (name, body) => {
  const dir = path.join(root, 'characters', name);
  fs.mkdirSync(path.join(dir, 'assets'), { recursive: true });
  fs.writeFileSync(path.join(dir, 'assets', 'README.txt'), 'Arte de apoio deste personagem (props extras, referencias). O personagem em si e desenhado pelo rig.\n');
  body = body.replace(/\},,/g, '},');
  fs.writeFileSync(path.join(dir, 'config.js'), `/*!
 * ${name} — tudo o que é próprio deste personagem. O resto mora em engine/.
 */
CharacterEngine.register('${name}', function (STH) {
${HEAD}${body}
});
`);
};
const humanCfg = (o) => `  const cfg = {
    rig: 'human', scale: ${o.scale}, seed: ${o.seed}, C, M, D, PIVOTS, SHAPE, OUTFITS, BASE_ROOT,
    defaultOutfit: '${o.outfit}'${o.hair ? ', HAIR: ' + o.hair : ''},
    EXPRESSIONS: complete(EXPRESSIONS, EXPRESSION_BASE), POSES, MOTION,
    ANIMATE: Object.assign({ talk() {} }, HUMAN, ${o.anim || '{}'}), ALIASES: { talking: 'talk' },
    accessories: ${o.acc},
    methods: () => ({
${o.methods}
    })
  };
  return cfg;`;

/* ---------- Dan ---------- */
{
  let s = read('dan-rivera/dan.js');
  const K = s;
  const all = methods(K);
  const norm = t => t.replace(/\bnode\(/g, 'this._n(').replace(/'dan-rig'/g, "'sth-rig'")
    .replace(/_buildLeg\(rig, 'l', 'leg-left'\)/, "_buildLeg(rig, 'l', 'left')").replace(/_buildLeg\(rig, 'r', 'leg-right'\)/, "_buildLeg(rig, 'r', 'right')")
    .replace("'l', 'arm-left'", "'l', 'left'").replace("'r', 'arm-right'", "'r', 'right'")
    .replace("this._eye(head, 'eye-right',", "this._eye(head, 'right',").replace("this._eye(head, 'eye-left',", "this._eye(head, 'left',").replace(/'-mouth/g, "'-clip-mouth").replace(/'-eye-r'/g, "'-clip-eye-r'").replace(/'-eye-l'/g, "'-clip-eye-l'");
  const C = between(K, 'const C = {', 'const LINE = 4.5;');
  const measures = between(K, 'const M = {', '/* ---------- Matemática');
  const shapes = between(K, 'const SHAPE = {', 'const shape = ').replace(/\n    boot: \{/, '\n    shoe: {');
  const expr = between(K, 'const EXPRESSION_BASE = {', 'Object.keys(EXPRESSIONS).forEach');
  const poses = between(K, 'const POSE_BASE = Object.assign({', '/* Movimento próprio');
  const handProps = between(K, "if (arm.k === 'r') {\n        const s = this.screwdriver", '\n    }\n\n    _buildBelt');
  const body = between(all._renderBody, '\n', '\n    }');
  writeConfig('dan', `  ${C}  const OUTFITS = {};
  const BASE_ROOT = 0;
  ${measures.replace('headY: -256', 'headY: -256, footH: 40')}
  ${shapes}
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
  ${expr}
  Object.assign(EXPRESSIONS, {
    surprised: { browY: -13, browArch: 6, eyeOpen: 1.14, eyeLow: 1.06, pupil: 0.84, mouthW: 15, mouthOpen: 16, smile: 0, tongue: 0.3 },
    thinking: { browY: -3, browTilt: 4, browSkew: 7, eyeOpen: 0.84, exGx: 0.6, exGy: -0.75, mouthW: 14, smile: -0.05, skew: 0.35, mouthShift: 8, tilt: 3 },
    talking: { smile: 0.2 }
  });
  ${poses}
  POSES.walking = pose({ spine: 1 }, { spine: 3, rf: -18, lf: -18 }, { plant: 1, farFront: 0 }, { spine: 2, rf: -14, lf: -14 });
  const MOTION = Object.assign(cycles({ root: 0, runBounce: [16, 26, 22] }), {
    working: { rate: 4.2, run(j, ph) { j.rh += 15 * Math.sin(ph * 1.6); j.rf += 4 * Math.sin(ph * 1.6 + 0.7); j.lh += 4 * Math.sin(ph * 0.8); j.head += 1.2 * Math.sin(ph * 0.5); } }
  });
  C.ink = '#242424'; C.navy = '#243B5A'; C.navyShade = tone('#243B5A', 0.78); C.navyDark = tone('#243B5A', 0.6);
  OUTFITS.main = { top: C.navy, topShade: C.navyShade, topDark: C.navyDark, pants: C.jeans, pantsShade: C.jeansShade, pantsLight: C.jeansLight, shoe: C.boot, sole: C.sole, stripe: C.bootShade, sleeve: 60 };
${footer('dan', humanCfg({ scale: 1, seed: 7, outfit: 'main', acc: '{ toolbelt: false, screwdriver: false, pliers: false, toolbox: false, seat: false }', methods: [
    norm(all._build), norm(all._buildBelt), norm(all._buildProps), norm(all._buildHead), norm(all._ear),
    `    _buildHandProps(arm) {\n      ${norm(handProps)}\n    }`,
    `    _renderBody(st, O, j, b) {${norm(body)}\n    }`,
    `    _renderHair(j, e, st, dt, jaw) {
      put(this.stubble, 'd', spline(jaw(shape('stubble', st), [2, 3, 4], [1, 5]), true));
      put(this.hair, 'd', spline(shape('hair', st), true));
      const shine = key3(0, 10, -2, st);
      put(this.hairShine, 'd', 'M' + f(shine - 44) + ' -170Q' + f(shine - 16) + ' -182 ' + f(shine + 16) + ' -181');
    }`,
    `    _renderEars(j, e, st) {
      const nearX = lerp(-81, -20, st), nearY = -66;
      put(this.earNear, 'transform', tf(nearX, nearY, 0, 1, 1));
      put(this.earFar, 'transform', tf(lerp(81, 60, st), nearY, 0, -1, 1));
      shown(this.earFar, st < 0.35 ? 1 : 0);
      const parent = st > 0.3 ? this.earTop : this.earBack;
      if (this.earNear.parentNode !== parent) parent.appendChild(this.earNear);
    }`,
    norm(all._renderProps)].join(',\n') }))}`.replace("const { outlineStyle, lineStyle } = styles(C.ink);\n", '').replace('const D = {', 'const { outlineStyle, lineStyle } = styles(\'#242424\');\n  const D = {'));
}

/* ---------- Mia, Leo e Bea: mesma origem ---------- */
function headParts(all) {
  const h = all._renderHead;
  const hair = between(h, 'const down = this.hairStyle', 'const gx = clamp(j.gx');
  return hair;
}
{
  const K = read('mia-rivera/mia.js'), all = methods(K);
  const marksMia = "      put(this.mole, 'cx', f(rx - 4)); put(this.mole, 'cy', -44);";
  const hair = headParts(all);
  const ears = between(all._renderHead, 'const nearY = -70;', 'const sw = clamp(e.sweat);');
  const watch = between(K, "if (k === 'r') {\n            this.watch", 'this._buildHand(arm, hand);');
  const body = all._renderBody.replace('_renderBody(st, O) {', '_renderBody(st, O, j, b) {');
  writeConfig('mia', `  ${between(K, 'const C = {', 'const LINE = 4.5;')}${between(K, 'const BASE_ROOT = 18;', '/* ---------- Matemática')}
  ${between(K, 'const SHAPE = {', 'function shape(name, t)')}
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
  ${between(K, 'const EXPRESSION_BASE = {', 'Object.keys(EXPRESSIONS).forEach')}
  Object.assign(EXPRESSIONS, {
    surprised: { browY: -12, browArch: 6, eyeOpen: 1.12, eyeLow: 1.06, pupil: 0.84, mouthW: 13, mouthOpen: 14, smile: 0, tongue: 0.3 },
    talking: { smile: 0.25 }
  });
  ${between(K, 'const POSE_BASE = Object.assign({', '/* Ciclos.')}
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [14, 24, 20] });
  C.ink = '#242424';
  OUTFITS.casual.top = '#247F79'; OUTFITS.casual.topShade = tone('#247F79', 0.8); OUTFITS.casual.topDark = tone('#247F79', 0.62);
  OUTFITS.scrubs.top = tone('#247F79', 1.18); OUTFITS.scrubs.topShade = '#247F79'; OUTFITS.scrubs.topDark = tone('#247F79', 0.75);
  OUTFITS.scrubs.pants = tone('#247F79', 1.1); OUTFITS.scrubs.pantsShade = tone('#247F79', 0.85); OUTFITS.scrubs.pantsLight = tone('#247F79', 1.35); OUTFITS.scrubs.stripe = '#247F79';
  C.badgeStripe = '#247F79';
${footer('mia', humanCfg({ scale: 1, seed: 11, outfit: 'casual', hair: "['down', 'up']", acc: '{ watch: true, badge: true, seat: false }', methods: [
    all._build.replace("'mia-rig'", "'sth-rig'").replace("'aria-label': 'Mia Rivera'", "'aria-label': 'Mia Rivera'"), all._buildBadge, all._buildSeat, all._buildHead, all._ear,
    `    _decorateForearm(fore, k) {\n      const n = this._n.bind(this);\n      ${watch}\n    }`,
    body,
    `    _renderHair(j, e, st, dt, jaw) {\n      ${hair.replace("put(this.bun, 'transform', tf(key3(0, -36, -86, st), key3(-188, -184, -152, st)));", "put(this.bun, 'transform', tf(key3(0, -36, -86, st), key3(-188, -184, -152, st)));")}\n    }`,
    `    _renderMarks(e, st, rx) {\n${marksMia}\n    }`,
    `    _renderEars(j, e, st) {\n      const down = this.hairStyle === 'down';\n      ${ears}\n    }`,
    all._renderProps].join(',\n') }))}`);
}
{
  const K = read('leo-rivera/leo.js'), all = methods(K);
  const hair = between(all._renderHead, 'const sway = this.hairSwing;', 'const gx = clamp(j.gx');
  const ears = between(all._renderHead, 'const nearY = -72;', 'const sw = clamp(e.sweat);');
  const marks = between(all._renderHead, 'const fr = (x, y) =>', 'this._renderMouth(');
  const handProps = "if (arm.k === 'r') this._buildHandPhone(arm.propSlot);\n      else this._buildClosedLaptop(arm.propSlot);";
  const motionText = between(K, 'const POSE_MOTION = {', '  const SWAP = [');
  const mt = methods(motionText);
  const typing = between(K, '/* Digitação: polegares', '/* Ciclos.');
  writeConfig('leo', `  ${between(K, 'const C = {', 'const LINE = 4.5;')}${between(K, 'const BASE_ROOT = 2;', '/* ---------- Matemática')}
  ${between(K, 'const SHAPE = {', 'function shape(name, t)')}
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
  ${between(K, 'const EXPRESSION_BASE = {', 'Object.keys(EXPRESSIONS).forEach')}
  Object.assign(EXPRESSIONS, {
    angry: { browY: 10, browTilt: -13, browArch: 1, eyeOpen: 0.76, lidTilt: 0.5, pupil: 0.82, mouthW: 25, mouthOpen: 12, smile: -0.55, teeth: 1, grit: 1, tint: 0.7 },
    surprised: { browY: -12, browArch: 6, eyeOpen: 1.12, eyeLow: 1.06, lidTilt: 0, pupil: 0.84, mouthW: 13, mouthOpen: 14, smile: 0, tongue: 0.3 },
    talking: { smile: 0.2 }
  });
  ${between(K, 'const POSE_BASE = Object.assign({', '/* Digitação: polegares')}
  ${typing}
  const POSE_MOTION = {
${pick(mt, ['gaming', 'using_laptop', 'using_phone', 'celebrating'])},
    texting: typingThumbs
  };
  const RATES = { texting: 9, gaming: 11, using_laptop: 10, using_phone: 3, celebrating: 5.5 };
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [14, 24, 20] });
  Object.keys(POSE_MOTION).forEach(k => { MOTION[k] = { rate: RATES[k], run: POSE_MOTION[k], still: k === 'celebrating' ? 1.57 : undefined }; });
  C.ink = '#242424';
  OUTFITS.hoodie.top = '#263B70'; OUTFITS.hoodie.topShade = tone('#263B70', 0.78); OUTFITS.hoodie.topDark = tone('#263B70', 0.56);
${footer('leo', humanCfg({ scale: 0.914, seed: 13, outfit: 'hoodie', anim: `{ typing(j, t, w) { const o = lerpDict(j, j, 1); typingFingers(o, t * 10); for (const k in j) j[k] = lerp(j[k], o[k], w); } }`,
    acc: "{ smartphone: 'auto', headphones: false, laptop: 'auto', backpack: false, seat: 'auto' }", methods: [
    all._build.replace("'leo-rig'", "'sth-rig'"), all._buildHandPhone, all._buildClosedLaptop, all._buildChestPhone, all._buildLaptop, all._buildHeadphones, all._buildSeat, all._buildHead, all._ear,
    `    _buildHandProps(arm) {\n      ${handProps}\n    }`,
    all._renderBody, `    _renderHair(j, e, st, dt, jaw) {\n      ${hair}\n    }`,
    `    _renderMarks(e, st, rx, lx, ls) {\n      ${marks}\n    }`,
    `    _renderEars(j, e, st) {\n      ${ears}\n    }`,
    all._renderProps].join(',\n') }))}`);
}
{
  const K = read('bea-rivera/bea.js'), all = methods(K);
  const hair = between(all._renderHead, 'const sway = this.hairSwing;', 'const gx = clamp(j.gx');
  const ears = between(all._renderHead, 'const bounce = sway * 2.6;', 'const sw = clamp(e.sweat);');
  const marks = between(all._renderHead, 'const cheekW = 15,', 'this._renderMouth(');
  const bracelet = between(K, "if (k === 'r') {\n            const b = this.bracelet", 'this._buildHand(arm, hand);');
  const handProps = between(K, "if (arm.k === 'r') {\n        this._buildTablet", '\n    }\n    _buildTeddy');
  const motionText = between(K, 'const POSE_MOTION = {', 'const MOTION_RATE');
  const mt = methods(motionText);
  const anim = methods(between(K, 'const ANIMATE = {', '  /* ---------- DOM'));
  const holding = "    _holding(k, j) {\n      return k === 'r' ? (this.accessories.colored_pencils === true || this.accessories.tablet === true) : this.accessories.teddy_bear === true && j.teddy <= 0.5;\n    }";
  writeConfig('bea', `  ${between(K, 'const C = {', 'const LINE = 4.5;')}${between(K, 'const BASE_ROOT = 158;', '/* ---------- Matemática')}
  ${between(K, 'const SHAPE = {', 'function shape(name, t)')}
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
  ${between(K, 'const EXPRESSION_BASE = {', 'Object.keys(EXPRESSIONS).forEach')}
  Object.assign(EXPRESSIONS, {
    worried: { browY: -6, browTilt: 11, eyeOpen: 1, lidTilt: -0.22, mouthW: 14, mouthOpen: 4, smile: -0.45, teeth: 0.6, sweat: 0.5, exGx: -0.2 },
    angry: { browY: 9, browTilt: -12, browArch: 1, eyeOpen: 0.8, lidTilt: 0.46, pupil: 0.84, mouthW: 16, smile: -0.7, tint: 0.55 },
    talking: { smile: 0.3 }
  });
  ${between(K, 'const POSE_BASE = Object.assign({', '/* Ciclos.')}
  const MOTION = cycles({ root: BASE_ROOT, runBounce: [8, 14, 13] });
  const RUNS = {
${pick(mt, ['walking', 'excited', 'jumping'])}
  };
  MOTION.walking = { rate: 7, still: 0.9, run: RUNS.walking };
  MOTION.running.rate = 12;
  MOTION.excited = { rate: 8, run: RUNS.excited };
  MOTION.jumping = { rate: 5, still: 1.57, run: RUNS.jumping };
  C.ink = '#242424';
  OUTFITS.main.top = '#F17C75'; OUTFITS.main.topShade = tone('#F17C75', 0.88); OUTFITS.main.topDark = tone('#F17C75', 0.72);
${footer('bea', humanCfg({ scale: 0.947, seed: 17, outfit: 'main', anim: `{\n${pick(anim, ['head_tilt', 'celebrate'])}\n    }`,
    acc: "{ teddy_bear: 'auto', backpack: false, colored_pencils: false, tablet: false, bracelet: true, seat: 'auto' }", methods: [
    all._build.replace("'bea-rig'", "'sth-rig'"), all._buildTeddy, all._buildTablet, all._buildPencils, all._buildSeat, all._buildHead, all._pigtail,
    `    _decorateForearm(fore, k) {\n      const n = this._n.bind(this);\n      ${bracelet}\n    }`,
    `    _buildHandProps(arm) {\n      ${handProps}\n    }`, holding,
    all._renderBody, `    _renderHair(j, e, st, dt, jaw) {\n      ${hair}\n    }`,
    `    _renderMarks(e, st, rx, lx, ls) {\n      ${marks}\n    }`,
    `    _renderEars(j, e, st) {\n      const sway = this.hairSwing;\n      ${ears}\n    }`,
    all._renderProps].join(',\n') }))}`);
}

/* ---------- Biscuit: rig de quatro patas ---------- */
{
  const K = read('biscuit-rivera/biscuit.js'), all = methods(K);
  const fix = t => t.replace(/this\._gaze\(dt, live\)/g, 'this.eyes.gaze(this.time, dt, live)').replace(/this\.gaze\./g, 'this.eyes.')
    .replace("this.anims.forEach(a => { if (ANIMATE[a.name]) ANIMATE[a.name](j, this.time, a.w); });", 'this.applyAnimations(j, 0);')
    .replace("'biscuit-rig'", "'sth-rig'");
  const list = ['_sampleJoints', '_barkAmount', '_build', '_buildLeg', '_buildTail', '_buildCollar', '_buildEar', '_buildEye', '_drop', '_buildHead', '_buildProps', '_render', '_renderLeg', '_renderEye', '_renderBrow', '_renderEar', '_renderHead'];
  fs.writeFileSync(path.join(root, 'engine', 'rigs', 'QuadrupedRig.js'), `/*!
 * QuadrupedRig — esqueleto de quatro patas. Cada pose é definida uma vez, em 3D,
 * e projetada para o ângulo atual; as patas se apoiam no chão sozinhas.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { lerp, clamp, smooth, f, key3, spline, capsule, shapeBook, put, shown, FLOOR, TAU } = STH.SVGRenderer;
  /* neste rig, escala com um valor só vale para os dois eixos */
  const tf = (x, y, r, sx, sy) => STH.SVGRenderer.tf(x, y, r, sx, sy === undefined ? sx : sy);
  const VIEWBOX = STH.SVGRenderer.VIEWBOX, RAD = Math.PI / 180;
  STH.Rigs = STH.Rigs || {};
  STH.Rigs.quadruped = function (cfg) {
    const { C, L, JOINT, SHAPE, POSES, POSE_MOTION, VIEW_SCALE, EXPRESSIONS } = cfg;
    const LINE = 4.5 / VIEW_SCALE;
    const shape = shapeBook(SHAPE);
    const outlineStyle = { fill: C.ink, stroke: C.ink, 'stroke-width': LINE * 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };
    const lineStyle = { stroke: C.ink, 'stroke-width': LINE, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' };
    return {
${list.map(n => fix(all[n])).join(',\n')}
    };
  };
})(typeof self !== 'undefined' ? self : this);
`);
  const anim = between(K, 'const ANIMATE = {', '  /* ---------- DOM');
  writeConfig('biscuit', `  const VIEW_SCALE = 0.8;
  ${between(K, 'const C = {', 'const VIEW_SCALE')}${between(K, 'const L = {', '/* ---------- Matemática')}
  ${between(K, 'const SHAPE = {', 'function shape(name, t)')}
  ${between(K, 'const EXPRESSION_BASE = {', 'Object.keys(EXPRESSIONS).forEach')}
  Object.keys(EXPRESSIONS).forEach(k => { EXPRESSIONS[k] = Object.assign({}, EXPRESSION_BASE, EXPRESSIONS[k]); });
  ${between(K, 'const POSE_BASE = {', '  class Mixer')}
  ${anim}
  ANIMATE.bark = function () {}; ANIMATE.pant = function () {};
  C.ink = '#242424'; C.fur = '#C58A45'; C.furShade = tone('#C58A45', 0.86); C.furFar = tone('#C58A45', 0.88); C.furDark = tone('#C58A45', 0.74);
  return {
    rig: 'quadruped', scale: 1.009, seed: 23, init() { this.earSwing = 0; this.earVel = 0; }, C, L, JOINT, SHAPE, VIEW_SCALE, POSES, POSE_MOTION,
    defaultDirection: 'right', EXPRESSIONS, ANIMATE, ALIASES: { talking: 'bark', talk: 'bark' },
    accessories: { collar: true, bone: false, bowl: false, ball: 'auto' }
  };`);
}
console.log('ok');
