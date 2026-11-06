/*!
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
    _sampleJoints() {
      const live = this.animation !== 'none';
      const get = name => {
        const j = Object.assign({ wag: 0, earN: 0, earF: 0, quiver: 0 }, POSES[name]);
        const m = POSE_MOTION[name];
        if (m) m.run(j, live ? this.time * m.rate : m.still, !live);
        return j;
      };
      const j = this.poseMix.sample(get);
      this.applyAnimations(j, 0);
      return j;
    },
    _barkAmount(j) {
      if (this.animation === 'none') return { open: j.bite * 18, recoil: 0 };
      const w = this.animation === 'bark' ? 1 : j.bite;
      if (w <= 0.01) return { open: 0, recoil: 0 };
      const ph = (this.time * 3.2) % 1;
      const pulse = ph < 0.3 ? Math.sin(ph / 0.3 * Math.PI) : (ph > 0.42 && ph < 0.62 ? Math.sin((ph - 0.42) / 0.2 * Math.PI) * 0.7 : 0);
      return { open: pulse * 24 * w, recoil: pulse * w };
    },
    _build() {
      const n = this._n.bind(this), u = this.prefix;
      const svg = this.svg = n('svg', { viewBox: VIEWBOX, class: 'sth-rig', role: 'img', 'aria-label': 'Biscuit', preserveAspectRatio: 'xMidYMax meet', overflow: 'visible' }, this.host);
      const defs = n('defs', {}, svg);
      this.clipEyeR = n('path', {}, n('clipPath', { id: u + '-clip-eye-right' }, defs));
      this.clipEyeL = n('path', {}, n('clipPath', { id: u + '-clip-eye-left' }, defs));

      this.scaler = n('g', { transform: 'translate(0 ' + FLOOR + ') scale(' + VIEW_SCALE + ') translate(0 ' + -FLOOR + ')' }, svg, 'scale');
      this.shadow = n('ellipse', { cx: 0, cy: FLOOR + 5, fill: '#000', 'fill-opacity': 0.22 }, this.scaler, 'shadow');
      this.flip = n('g', {}, this.scaler, 'character');
      this._buildProps(this.flip);

      const rig = this.rig = n('g', {}, this.flip, 'root');
      this.tailNode = this._buildTail(n('g', {}, rig, 'layer-tail'));
      this.layerBehind = n('g', {}, rig, 'layer-legs-behind');
      this.legBN = this._buildLeg('back', 'right', 'b', 'n');
      this.legBF = this._buildLeg('back', 'left', 'b', 'f');
      this.legFF = this._buildLeg('front', 'left', 'f', 'f');
      this.layerBehind.append(this.legBF.root, this.legBN.root, this.legFF.root);

      const trunk = n('g', {}, rig, 'layer-body');
      this.bodyO = n('path', Object.assign({}, outlineStyle), trunk);
      this.neckO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 76 + LINE * 2, 'stroke-linecap': 'round' }, trunk);
      this.body = n('path', { fill: C.fur }, trunk, 'body');
      this.neck = n('path', { fill: 'none', stroke: C.fur, 'stroke-width': 76, 'stroke-linecap': 'round' }, trunk, 'neck');
      this.bodyShade = n('path', { fill: C.furShade }, trunk, 'body-shade');
      this.chest = n('path', { fill: C.chest }, trunk, 'chest-patch');

      this.layerFront = n('g', {}, rig, 'layer-legs-front');
      this.legFN = this._buildLeg('front', 'right', 'f', 'n');
      this.layerFront.appendChild(this.legFN.root);

      this._buildCollar(n('g', {}, rig, 'layer-collar'));
      this._buildHead(n('g', {}, rig, 'layer-head'));
      this.layerTop = n('g', {}, rig, 'layer-paw-over');
      this.zzz = n('g', {}, rig, 'zzz');
      this.zNodes = [0, 1, 2].map(() => n('path', { d: 'M-9 -9H9L-9 9H9', fill: 'none', stroke: C.zzz, 'stroke-width': 6, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, this.zzz));
      this.legBNInFront = false; this.legFFInFront = false;
    },
    _buildLeg(kind, side, a, b) {
      const n = this._n.bind(this);
      const name = kind + '-paw-' + side;
      const root = n('g', {}, null, 'leg-' + kind + '-' + side, kind === 'front' ? JOINT.frontNear : JOINT.backNear);
      const leg = { root, upper: [], lower: [], paw: [], up: [], lo: [], key: a + b, kind, tone: [] };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const style = isO ? outlineStyle : { fill: C.fur };
        const g = n('g', {}, root);
        const upper = n('g', {}, g, isO ? null : 'leg-' + kind + '-' + side + '-upper');
        const up = n('path', Object.assign({}, style), upper);
        const lower = n('g', {}, upper, isO ? null : 'leg-' + kind + '-' + side + '-lower');
        const lo = n('path', Object.assign({}, style), lower);
        const paw = n('g', {}, lower, isO ? null : name);
        const p = n('path', Object.assign({}, style), paw);
        leg.upper.push(upper); leg.lower.push(lower); leg.paw.push(paw); leg.up.push(up); leg.lo.push(lo);
        (leg.pawPaths || (leg.pawPaths = [])).push(p);
        if (!isO) {
          leg.tone.push(up, lo, p);
          leg.toes = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 3, 'stroke-linecap': 'round' }, paw);
        }
      });
      return leg;
    },
    _buildTail(parent) {
      const n = this._n.bind(this);
      const t = { root: n('g', {}, parent, 'tail', JOINT.tail), a: [], b: [] };
      ['o', 'f'].forEach(pass => {
        const isO = pass === 'o';
        const style = isO ? outlineStyle : { fill: C.fur };
        const g = n('g', {}, t.root);
        const a = n('g', {}, g, isO ? null : 'tail-base');
        n('path', Object.assign({ d: capsule(L.tailA, 13, 11) }, style), a);
        const b = n('g', {}, a, isO ? null : 'tail-tip');
        n('path', Object.assign({ d: capsule(L.tailB, 11, 6) }, style), b);
        t.a.push(a); t.b.push(b);
      });
      return t;
    },
    _buildCollar(parent) {
      const n = this._n.bind(this);
      const g = this.collarGroup = n('g', {}, parent, 'collar');
      this.collarO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 18 + LINE * 2, 'stroke-linecap': 'round' }, g);
      this.collarF = n('path', { fill: 'none', stroke: C.collar, 'stroke-width': 18, 'stroke-linecap': 'round' }, g, 'collar-band');
      this.collarLine = n('path', { fill: 'none', stroke: C.collarDark, 'stroke-width': 3, 'stroke-linecap': 'round' }, g);
      const m = this.medal = n('g', {}, g, 'medal');
      n('circle', Object.assign({ cx: 0, cy: 12, r: 13, fill: C.medal }, lineStyle), m);
      n('circle', { cx: 0, cy: 12, r: 6.5, fill: 'none', stroke: C.medalDark, 'stroke-width': 3 }, m);
    },
    _buildEar(parent, part) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, part);
      const fill = n('path', Object.assign({ fill: C.ear }, lineStyle), g);
      const line = n('path', { fill: 'none', stroke: C.earShade, 'stroke-width': 7, 'stroke-linecap': 'round' }, g);
      return { g, fill, line };
    },
    _buildEye(parent, side, clipId) {
      const n = this._n.bind(this);
      const g = n('g', {}, parent, 'eye-' + side);
      const white = n('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3.5, 'stroke-linejoin': 'round' }, g);
      const iris = n('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
      const ball = n('g', {}, iris, 'pupil-' + side);
      n('circle', { r: 15, fill: C.iris }, ball);
      n('circle', { r: 10, fill: '#120d0a' }, ball);
      n('circle', { cx: 5, cy: -6, r: 4.6, fill: '#fff' }, ball);
      const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 6, 'stroke-linecap': 'round' }, g);
      return { g, white, iris, ball, lid };
    },
    _drop(parent) {
      return this._n('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
    },
    _buildHead(parent) {
      const n = this._n.bind(this);
      const head = this.head = n('g', {}, parent, 'head', JOINT.head);
      this.earBackLayer = n('g', {}, head);
      this.earF = this._buildEar(this.earBackLayer, 'ear-left');
      this.headShape = n('path', Object.assign({ fill: C.fur }, lineStyle), head, 'face');
      this.brows = n('g', {}, head);

      this.mouthDark = n('path', Object.assign({ fill: C.mouth }, lineStyle), head, 'mouth');
      this.jawGroup = n('g', {}, head, 'jaw');
      this.jaw = n('path', Object.assign({ fill: C.muzzleShade }, lineStyle), this.jawGroup);
      this.tongueIn = n('ellipse', { fill: C.tongue }, this.jawGroup);
      this.tongue = n('g', {}, this.jawGroup, 'tongue');
      this.tongueShape = n('path', Object.assign({ fill: C.tongue }, lineStyle, { 'stroke-width': 4 }), this.tongue);
      this.tongueLine = n('path', { fill: 'none', stroke: C.tongueLine, 'stroke-width': 3, 'stroke-linecap': 'round' }, this.tongue);
      this.bone = n('g', {}, this.jawGroup, 'bone');
      const boneD = 'M-40 -6C-46 -18 -60 -14 -56 -2C-62 2 -60 16 -46 12C-42 10 -40 8 -38 6H38C40 8 42 10 46 12C60 16 62 2 56 -2C60 -14 46 -18 40 -6Z';
      n('path', Object.assign({ d: boneD, fill: C.bone }, lineStyle), this.bone);
      n('path', { d: 'M-34 3H34', stroke: C.boneShade, 'stroke-width': 4, 'stroke-linecap': 'round', fill: 'none' }, this.bone);

      this.muzzle = n('path', Object.assign({ fill: C.muzzle }, lineStyle), head, 'muzzle');
      this.fangs = n('path', { fill: C.teeth, stroke: C.ink, 'stroke-width': 2.5, 'stroke-linejoin': 'round' }, head, 'fangs');
      this.mouthLine = n('path', Object.assign({ fill: 'none' }, lineStyle), head, 'mouth-line');
      this.nose = n('g', {}, head, 'nose');
      this.noseShape = n('path', Object.assign({ fill: C.nose }, lineStyle, { 'stroke-width': 3 }), this.nose);
      n('ellipse', { cx: -4, cy: -4, rx: 5, ry: 2.8, fill: C.noseShine }, this.nose);

      this.eyeR = this._buildEye(head, 'right', this.prefix + '-clip-eye-right');
      this.eyeL = this._buildEye(head, 'left', this.prefix + '-clip-eye-left');
      const browStyle = { fill: 'none', stroke: C.brow, 'stroke-width': 9, 'stroke-linecap': 'round' };
      this.browR = n('path', browStyle, head, 'brow-right');
      this.browL = n('path', browStyle, head, 'brow-left');
      this.earFrontLayer = n('g', {}, head);
      this.earN = this._buildEar(this.earFrontLayer, 'ear-right');
      this.sweat = n('g', {}, head, 'sweat');
      this.sweat1 = this._drop(this.sweat); this.sweat2 = this._drop(this.sweat);
      this.tear = this._drop(head);
      this.drool = this._drop(head);
    },
    _buildProps(parent) {
      const n = this._n.bind(this);
      const b = this.bowl = n('g', {}, parent, 'bowl');
      n('ellipse', Object.assign({ cx: 0, cy: -44, rx: 58, ry: 12, fill: C.food }, lineStyle), b);
      n('path', { d: 'M-34 -46l10 -4l10 5l10 -6l12 5l12 -4l10 4', fill: 'none', stroke: C.foodDark, 'stroke-width': 4, 'stroke-linecap': 'round' }, b);
      n('path', Object.assign({ d: 'M-66 -40Q-58 0 -46 0H46Q58 0 66 -40Q0 -22 -66 -40Z', fill: C.bowl }, lineStyle), b);
      n('path', { d: 'M-48 -10H48', stroke: C.bowlDark, 'stroke-width': 6, 'stroke-linecap': 'round', fill: 'none' }, b);
      const ball = this.ball = n('g', {}, parent, 'ball');
      n('circle', Object.assign({ cx: 0, cy: -26, r: 26, fill: C.ball }, lineStyle), ball);
      n('path', { d: 'M-22 -40Q-2 -26 -22 -12M22 -40Q2 -26 22 -12', fill: 'none', stroke: C.ballLine, 'stroke-width': 4.5, 'stroke-linecap': 'round' }, ball);
    },
    _render(blink, dt) {
      const t = Math.abs(this.turn), st = smooth(t);
      const sign = this.turn < 0 ? -1 : 1;
      const live = this.animation !== 'none';
      const j = this._sampleJoints();
      const e = this.exprMix.sample(n => EXPRESSIONS[n]);
      this.eyes.gaze(this.time, dt, live);
      const bark = this._barkAmount(j);

      const yaw = st * Math.PI / 2, si = Math.sin(yaw), co = Math.cos(yaw);
      const P = j.pitch * RAD, cp = Math.cos(P), sp = Math.sin(P);
      const breath = this.breathing ? Math.sin(this.time * TAU / (j.shut > 0.5 ? 4.6 : 2.6)) : 0;

      /* esqueleto 3D girado pelo pitch e projetado para a tela */
      const J = (name) => {
        const [fw, y, s] = JOINT[name];
        const yb = y * lerp(1, -1, j.belly);
        return { f: fw * cp + yb * sp, y: yb * cp - fw * sp, s };
      };
      const X = p => p.f * si + p.s * co;
      const seg = (angle, len, lateral) => {
        const a = angle * RAD;
        const dx = -Math.sin(a) * len * si + (lateral || 0) * co, dy = Math.cos(a) * len;
        const screen = Math.max(Math.hypot(dx, dy), len * 0.22);
        return { theta: Math.atan2(-dx, dy) / RAD, len: screen, dy };
      };

      /* apoio no chão */
      const lens = {
        fn: [L.fu * j.frontLen, L.fl * j.frontLen], ff: [L.fu * j.frontLen, L.fl * j.frontLen],
        bn: [L.bu, L.bl], bf: [L.bu, L.bl]
      };
      const anchors = { fn: J('frontNear'), ff: J('frontFar'), bn: J('backNear'), bf: J('backFar') };
      const reach = k => anchors[k].y + Math.cos(j[k + 'u'] * RAD) * lens[k][0] + Math.cos(j[k + 'l'] * RAD) * lens[k][1] + L.paw;
      /* o corpo inclinado também encosta no chão: o pitch leva a traseira para baixo */
      const rump = 112 * Math.abs(sp) + 46 * cp * j.squash;
      const lowest = Math.max(reach('fn'), reach('ff'), reach('bn'), reach('bf'), rump);
      const base = FLOOR - lerp(106, lowest, j.plant) + j.lift;
      const quiver = j.quiver * 1.8 * Math.sin(this.time * 42);

      put(this.svg, 'opacity', String(Math.round(this.alpha * 100) / 100));
      put(this.svg, 'display', this.alpha <= 0.001 ? 'none' : 'inline');
      put(this.flip, 'transform', 'scale(' + sign + ' 1)');
      const centerX = key3(0, -16, -26, st) + j.rootF * si + quiver;
      put(this.rig, 'transform', tf(centerX, base, j.spin));

      /* corpo */
      const bodyAngle = -j.pitch * si;
      const raise = 1 + Math.abs(sp) * 0.5 * (1 - st);
      const bodyT = tf(0, 0, bodyAngle, 1 + breath * 0.012, (1 + breath * 0.022) * raise * j.squash * lerp(1, -1, j.belly));
      [this.bodyO, this.body, this.bodyShade, this.chest].forEach(el => put(el, 'transform', bodyT));
      const bodyD = spline(shape('body', st), true);
      put(this.bodyO, 'd', bodyD); put(this.body, 'd', bodyD);
      put(this.bodyShade, 'd', spline(shape('bodyShade', st < 0.5 ? 0 : 1), true));
      shown(this.bodyShade, Math.abs(1 - 2 * st));
      put(this.chest, 'd', spline(shape('chest', st), true));

      const nb = J('neckBase'), hp = J('head');
      const hx = X(hp) + j.headF * si, hy = hp.y + j.headY + e.headDrop + bark.recoil * 5;
      const nx = X(nb), ny = nb.y;
      const neckD = 'M' + f(nx) + ' ' + f(ny) + 'L' + f(hx) + ' ' + f(hy - 18);
      put(this.neckO, 'd', neckD); put(this.neck, 'd', neckD);

      /* pernas */
      this._renderLeg(this.legFN, j, 'fn', anchors, lens, X, seg, st, 0, si);
      this._renderLeg(this.legFF, j, 'ff', anchors, lens, X, seg, st, 14, si);
      this._renderLeg(this.legBN, j, 'bn', anchors, lens, X, seg, st, 0, si);
      this._renderLeg(this.legBF, j, 'bf', anchors, lens, X, seg, st, 14, si);
      const bnFront = st > 0.35, ffFront = st < 0.6;
      if (bnFront !== this.legBNInFront) {
        (bnFront ? this.layerFront : this.layerBehind).insertBefore(this.legBN.root, bnFront ? this.layerFront.firstChild : this.layerBehind.firstChild);
        this.legBNInFront = bnFront;
      }
      if (ffFront !== this.legFFInFront) {
        if (!ffFront) this.layerBehind.appendChild(this.legFF.root);
        else if (this.legFN.root.parentNode === this.layerFront) this.layerFront.insertBefore(this.legFF.root, this.legFN.root);
        else this.layerFront.appendChild(this.legFF.root);
        this.legFFInFront = ffFront;
      }
      const pawTop = j.pawOver > 0.5 ? this.layerTop : this.layerFront;
      if (this.legFN.root.parentNode !== pawTop) pawTop.appendChild(this.legFN.root);
      const farTone = clamp((st - 0.5) * 2);
      [this.legFF, this.legBF].forEach(l => l.tone.forEach(p => put(p, 'fill', farTone > 0.5 ? C.furFar : C.fur)));

      /* cauda */
      const tp = J('tail');
      const mood = e.tailMood;
      const tailA = j.tailA + mood + breath * 1.5;
      const a = seg(tailA, L.tailA, j.wag);
      const b = seg(tailA + j.tailB, L.tailB, j.wag * 0.8);
      const tailT = tf(X(tp), tp.y, 0);
      put(this.tailNode.root, 'transform', tailT);
      const sa = a.len / L.tailA, sb = b.len / L.tailB;
      this.tailNode.a.forEach(g => put(g, 'transform', tf(0, 0, a.theta, 1, sa)));
      this.tailNode.b.forEach(g => put(g, 'transform', tf(0, L.tailA, b.theta - a.theta, 1, sb / Math.max(sa, 0.01))));

      /* coleira no meio do pescoço */
      const cx = lerp(nx, hx, 0.62), cy = lerp(ny, hy - 18, 0.62);
      const dx = hx - nx, dy = hy - 18 - ny, dl = Math.max(Math.hypot(dx, dy), 1);
      const ux = dx / dl, uy = dy / dl, w = 41;
      const p0 = [cx - uy * w, cy + ux * w], p1 = [cx + uy * w, cy - ux * w];
      const bulge = key3(22, 20, 14, st);
      const mid = [cx - ux * bulge * 2, cy - uy * bulge * 2];
      const collarD = 'M' + f(p0[0]) + ' ' + f(p0[1]) + 'Q' + f(mid[0]) + ' ' + f(mid[1]) + ' ' + f(p1[0]) + ' ' + f(p1[1]);
      put(this.collarO, 'd', collarD); put(this.collarF, 'd', collarD); put(this.collarLine, 'd', collarD);
      const low = p0[1] > p1[1] ? p0 : p1;
      const medalX = lerp(cx - ux * bulge, low[0], key3(0, 0.45, 0.8, st)), medalY = lerp(cy - uy * bulge, low[1], key3(0, 0.45, 0.8, st));
      put(this.medal, 'transform', tf(medalX, medalY + 4, -j.spin));
      shown(this.collarGroup, this.accessories.collar ? 1 : 0);

      this._renderHead(j, e, st, blink, dt, hx, hy, bark);

      /* acessórios e sono */
      const a2 = this.accessories;
      shown(this.bowl, a2.bowl === true ? 1 : 0);
      put(this.bowl, 'transform', tf(key3(170, 210, 240, st), FLOOR + 2));
      const ballOn = a2.ball === 'auto' ? j.ball > 0.5 : a2.ball;
      shown(this.ball, ballOn ? 1 : 0);
      const roll = (live && j.ball > 0.5) ? 6 * Math.sin(this.time * 7) : 0;
      put(this.ball, 'transform', tf(key3(-120, 190, 230, st) + roll, FLOOR + 2));
      shown(this.shadow, a2.shadow ? 1 : 0);
      const air = clamp((FLOOR - lerp(106, lowest, 1) - base) / 120);
      put(this.shadow, 'rx', f(key3(84, 120, 150, st) * (1 - air * 0.5)));
      put(this.shadow, 'ry', f(14 * (1 - air * 0.3)));
      put(this.shadow, 'cx', f(centerX + key3(0, 10, 10, st)));

      const asleep = j.shut;
      shown(this.zzz, asleep > 0.5 && live ? 1 : 0);
      if (asleep > 0.5 && live) {
        this.zNodes.forEach((z, i) => {
          const u = (this.time * 0.45 + i / 3) % 1;
          put(z, 'transform', tf(hx + key3(40, 80, 100, st) + 34 * u + 8 * Math.sin(u * 7), hy - 110 - 90 * u, 0, 0.7 + u * 0.8));
          put(z, 'opacity', String(Math.round(Math.sin(u * Math.PI) * 100) / 100));
        });
      }
    },
    _renderLeg(leg, j, k, anchors, lens, X, seg, st, farShift, si) {
      const up = seg(j[k + 'u'], lens[k][0]), lo = seg(j[k + 'l'], lens[k][1]);
      const an = anchors[k];
      put(leg.root, 'transform', tf(X(an) + farShift * si, an.y));
      const uT = tf(0, 0, up.theta), lT = tf(0, up.len, lo.theta - up.theta), pT = tf(0, lo.len, -lo.theta);
      leg.upper.forEach(g => put(g, 'transform', uT));
      leg.lower.forEach(g => put(g, 'transform', lT));
      leg.paw.forEach(g => put(g, 'transform', pT));
      const big = leg.kind === 'back';
      const dU = capsule(up.len, big ? 33 : 21, big ? 18 : 17), dL = capsule(lo.len, big ? 17 : 16, 14);
      leg.up.forEach(p => put(p, 'd', dU));
      leg.lo.forEach(p => put(p, 'd', dL));
      const pd = spline(shape('paw', st), true);
      leg.pawPaths.forEach(p => put(p, 'd', pd));
      const tx = key3(0, 8, 16, st);
      put(leg.toes, 'd', 'M' + f(tx - 7) + ' 12V5M' + f(tx + 7) + ' 12V5');
    },
    _renderEye(eye, clip, x, y, sx, inner, e, shut, gx, gy) {
      put(eye.g, 'transform', tf(x, y, 0, sx, 1));
      const W = 21;
      const open = Math.max(0, e.eyeOpen * (1 - shut));
      const T = 25 * open * 1.33, B = 19 * e.eyeLow * (1 - shut * 0.9) * 1.33;
      const k = e.lidTilt;
      const topIn = T * (1 - k), topOut = T * (1 + k);
      const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
      const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
      const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
      put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
      const p = 0.72 + e.pupil * 0.28;
      put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
    },
    _renderBrow(el, x, inner, e, sx, skew) {
      const y = -112 + e.browY - skew;
      const w = 16 * sx;
      const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
      put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY + 2) + 'Q' + f(x) + ' ' + f(y - 7 - e.browTilt * 0.1) + ' ' + f(x + w * inner) + ' ' + f(inY));
    },
    _renderEar(ear, st, angle, flop, x, y) {
      const pts = shape('ear', st).map(p => [p[0] + flop * Math.pow(Math.max(p[1], 0) / 78, 2), p[1], p[2]]);
      put(ear.fill, 'd', spline(pts, true));
      put(ear.line, 'd', 'M' + f(2 + flop * 0.04) + ' 18Q' + f(10 + flop * 0.3) + ' 42 ' + f(2 + flop * 0.7) + ' 62');
      put(ear.g, 'transform', tf(x, y, angle));
    },
    _renderHead(j, e, st, blink, dt, hx, hy, bark) {
      const shut = Math.max(blink, j.shut);
      const si = Math.sin(st * Math.PI / 2);
      put(this.head, 'transform', tf(hx, hy, j.head * si + j.roll + e.tilt));
      put(this.headShape, 'd', spline(shape('head', st), true));
      put(this.muzzle, 'd', spline(shape('muzzle', st), true));

      /* orelhas com mola: seguem o movimento da cabeça */
      const goal = clamp((j.head + j.roll + j.pitch * 0.4) * -0.5 + j.lift * 0.14 + bark.recoil * 10, -24, 24);
      for (let left = dt; left > 0; left -= 0.016) {
        const step = Math.min(left, 0.016);
        this.earVel += ((goal - this.earSwing) * 70 - this.earVel * 7) * step;
        this.earSwing += this.earVel * step;
      }
      const lift = e.ear + j.ear;
      const up = Math.max(lift, 0), down = Math.max(-lift, 0);   // orelha baixa cai para fora e desce
      const pose = up + down * 0.45;
      const nearA = key3(20, 14, 10, st) + pose + j.earN;
      const farSign = key3(-1, -1, 1, st);
      const farA = key3(0, 0, 8, st) + farSign * (key3(20, 16, 0, st) + pose) + j.earF;
      const sink = down * 0.55;
      this._renderEar(this.earN, st, nearA, this.earSwing, key3(-62, -44, -14, st), key3(-92, -98, -106, st) + sink);
      this._renderEar(this.earF, st, farA, this.earSwing, key3(62, 60, 34, st), key3(-92, -100, -110, st) + sink);
      const farBehind = st > 0.45;
      const wanted = farBehind ? this.earBackLayer : this.earFrontLayer;
      if (this.earF.g.parentNode !== wanted) wanted.appendChild(this.earF.g);

      /* boca */
      const open = Math.max(e.mouthOpen, bark.open, this.animation === 'pant' ? 12 + 4 * Math.sin(this.time * 14) : 0, this.accessories.bone === true ? 8 : 0);
      const jaw = spline(shape('jaw', st), true);
      put(this.jaw, 'd', jaw);
      const hingeX = key3(0, 16, 44, st), hingeY = -18;
      put(this.jawGroup, 'transform', 'translate(0 ' + f(open * 0.8 * (1 - st * 0.7)) + ') rotate(' + f(-open * 0.42 * -st) + ' ' + f(hingeX) + ' ' + hingeY + ')');
      put(this.mouthDark, 'd', spline(shape('jaw', st).map(p => [p[0], p[1] + Math.min(open, 26) * 0.5, p[2]]), true));
      shown(this.mouthDark, open > 1.5 ? 1 : 0);
      const tx = key3(0, 40, 68, st), ty = key3(-12, -14, -16, st);
      put(this.tongueIn, 'cx', f(tx)); put(this.tongueIn, 'cy', f(ty)); put(this.tongueIn, 'rx', f(key3(17, 24, 26, st))); put(this.tongueIn, 'ry', 7);
      shown(this.tongueIn, open > 3 ? 1 : 0);
      const pant = this.animation === 'pant' ? 1 : e.tongue;
      const len = 30 * pant * (1 + (this.animation === 'pant' ? 0.1 * Math.sin(this.time * 14) : 0));
      shown(this.tongue, len > 3 && this.accessories.bone !== true ? 1 : 0);
      put(this.tongue, 'transform', tf(key3(6, 50, 80, st), key3(2, 0, -2, st), key3(0, 6, 8, st)));
      put(this.tongueShape, 'd', capsule(Math.max(len, 1), 13, 12));
      put(this.tongueLine, 'd', 'M0 4V' + f(Math.max(len - 2, 5)));
      shown(this.bone, this.accessories.bone === true ? 1 : 0);
      put(this.bone, 'transform', tf(key3(0, 36, 62, st), -6, 0, key3(1, 0.9, 0.74, st), 1));

      /* linha da boca */
      const lx = key3(0, 36, 64, st), half = key3(30, 40, 42, st), smile = e.smile;
      const lineY = key3(-13, -16, -19, st);
      const c0 = lx - half, c1 = lx + half;
      const lift0 = -smile * 12, lift1 = st > 0.7 ? 0 : -smile * 12 * (1 - st);
      put(this.mouthLine, 'd', 'M' + f(c0 - 4) + ' ' + f(lineY + lift0) + 'Q' + f(lx) + ' ' + f(lineY + smile * 7 + 3) + ' ' + f(c1) + ' ' + f(lineY + lift1) +
        (st < 0.7 ? 'M' + f(key3(0, 50, 84, st)) + ' ' + f(key3(-42, -44, -44, st)) + 'V' + f(lineY + smile * 3 + 2) : ''));
      const fx = key3(-14, 22, 46, st), fw = key3(28, 30, 24, st);
      const fy = lineY + 2;
      put(this.fangs, 'd', 'M' + f(fx - 6) + ' ' + f(fy) + 'L' + f(fx) + ' ' + f(fy + 13) + 'L' + f(fx + 6) + ' ' + f(fy) + 'ZM' + f(fx + fw - 6) + ' ' + f(fy) + 'L' + f(fx + fw) + ' ' + f(fy + 13) + 'L' + f(fx + fw + 6) + ' ' + f(fy) + 'Z');
      shown(this.fangs, e.fangs > 0.3 ? 1 : 0);

      /* nariz */
      put(this.nose, 'transform', tf(key3(0, 64, 104, st), key3(-60, -50, -60, st), 0, key3(1.1, 1.1, 1, st), 1.1));
      put(this.noseShape, 'd', 'M-15 -6C-15 -14 15 -14 15 -6C15 4 6 11 0 11C-6 11 -15 4 -15 -6Z');

      /* olhos */
      const gx = clamp(j.gx + e.exGx + this.eyes.x, -1, 1), gy = clamp(j.gy + e.exGy + this.eyes.y, -1, 1);
      const rx = key3(-27, 8, 40, st), lx2 = key3(27, 52, 68, st), ey = -84;
      const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.7, 0, st));
      this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, shut, gx, gy);
      shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
      this._renderEye(this.eyeL, this.clipEyeL, lx2, ey, Math.max(ls, 0.06), -1, e, shut, gx, gy);
      this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
      shown(this.browL, ls > 0.1 ? 1 : 0);
      this._renderBrow(this.browL, lx2, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

      const sw = clamp(e.sweat);
      shown(this.sweat, sw > 0.04 ? 1 : 0);
      put(this.sweat1, 'transform', tf(key3(-74, 78, 78, st), key3(-118, -112, -112, st), 12, 0.5 + sw * 0.5));
      put(this.sweat2, 'transform', tf(key3(78, 90, 92, st), key3(-112, -92, -92, st), -10, 0.38 + sw * 0.4));
      const fall = (this.time * 0.8) % 1;
      shown(this.tear, clamp(e.tear));
      put(this.tear, 'transform', tf(rx + 6, -52 + (this.animation === 'none' ? 0.5 : fall) * 16, 0, 0.75));
      shown(this.drool, clamp(e.drool));
      put(this.drool, 'transform', tf(key3(22, 64, 92, st), -2 + (this.animation === 'none' ? 0.4 : (this.time * 0.9) % 1) * 22, 0, 0.72));
    }
    };
  };
})(typeof self !== 'undefined' ? self : this);
