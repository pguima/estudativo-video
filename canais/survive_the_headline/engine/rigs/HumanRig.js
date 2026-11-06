/*!
 * HumanRig — esqueleto e desenho comuns aos quatro humanos.
 *
 * Pernas, braços, mãos, olhos, sobrancelhas, nariz e boca são um código só,
 * alimentado pelas medidas de config.js (cfg.D). O que é próprio de cada pessoa
 * vem do personagem: _build, _buildHead, _renderBody, _renderHair, _renderEars,
 * _renderMarks e _renderProps.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { lerp, clamp, smooth, f, key3, keyOf, spline, capsule, shapeBook, put, tf, shown, hexMix, styles, FLOOR, LINE, TAU } = STH.SVGRenderer;

  STH.Rigs = STH.Rigs || {};
  STH.Rigs.human = function (cfg) {
    const { C, M, D, PIVOTS, OUTFITS, SHAPE, BASE_ROOT } = cfg;
    const shape = shapeBook(SHAPE);
    const { outlineStyle } = styles(C.ink);
    const A = D.arm, G = D.leg, H = D.head;

    return {
      _sampleJoints(st) { return STH.PoseController.sampleHuman(this, st); },

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
            leg.thighShade = n('path', { d: capsule.apply(null, G.thighShade) }, thigh);
            leg.shinShade = n('path', { d: capsule.apply(null, G.shinShade) }, shin);
            leg.knee = n('path', { d: G.knee, fill: 'none', 'stroke-width': G.kneeWidth, 'stroke-linecap': 'round' }, shin);
            leg.shoe = n('path', {}, foot);
            leg.stripe = n('path', { fill: 'none', 'stroke-width': G.stripeWidth, 'stroke-linecap': 'round' }, foot);
            leg.laces = n('path', { fill: 'none', stroke: G.laceColor, 'stroke-width': G.laceWidth, 'stroke-linecap': 'round' }, foot);
            leg.sole = n('path', {}, foot);
            leg.cuff = n('path', { d: G.cuff, fill: 'none', 'stroke-width': G.cuffWidth, 'stroke-linecap': 'round' }, foot);
          }
        });
        return leg;
      },

      _buildArm(parent, k, side) {
        const n = this._n.bind(this);
        const g = n('g', {}, parent, 'arm-' + side, k === 'r' ? PIVOTS.shoulderRight : PIVOTS.shoulderLeft);
        const arm = { root: g, upper: [], fore: [], hand: [], skin: [], forePaths: [], k, side };
        ['o', 'f'].forEach(pass => {
          const isO = pass === 'o';
          const skin = isO ? outlineStyle : (A.fullSleeve ? {} : { fill: C.skin });
          const passG = n('g', {}, g);
          const upper = n('g', {}, passG, isO ? null : 'upper-arm-' + side);
          const up = n('path', Object.assign({ d: capsule(M.upperArm, A.upper[0], A.upper[1]) }, skin), upper);
          const fore = n('g', {}, upper, isO ? null : 'forearm-' + side, PIVOTS.elbow);
          const fp = n('path', Object.assign({}, skin), fore);
          arm.forePaths.push(fp);
          const hand = n('g', {}, fore, isO ? null : 'hand-' + side, PIVOTS.wrist);
          arm.upper.push(upper); arm.fore.push(fore); arm.hand.push(hand);
          if (isO) {
            if (!A.fullSleeve) arm.sleeveO = n('path', Object.assign({}, outlineStyle), upper);
            n('path', Object.assign({ d: this._palm() }, outlineStyle), hand);
            arm.fingersO = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 14 + LINE, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, hand);
          } else {
            arm.skin.push(up, fp);
            if (A.fullSleeve) {
              arm.sleeveShade = n('path', {}, upper);
              arm.foreShade = n('path', {}, fore);
              arm.cuff = n('path', { fill: 'none', 'stroke-width': 7, 'stroke-linecap': 'round' }, fore, 'cuff-' + side);
            } else {
              arm.sleeve = n('path', {}, upper, 'sleeve-' + side);
              arm.sleeveHem = n('path', { fill: 'none', 'stroke-width': A.hemWidth, 'stroke-linecap': 'round' }, upper);
              arm.foreShade = n('path', { fill: C.skinShade }, fore);
            }
            if (this._decorateForearm) this._decorateForearm(fore, k);
            this._buildHand(arm, hand);
          }
        });
        arm.shoulder = n('ellipse', {}, g, 'shoulder-' + side);
        return arm;
      },
      _palm() { return 'M-19 -4Q-23 16 -20 34Q0 42 20 34Q23 16 19 -4Q0 -10 -19 -4Z'; },
      _buildHand(arm, hand) {
        const n = this._n.bind(this);
        const stroke = (color, width) => ({ fill: 'none', stroke: color, 'stroke-width': width, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
        arm.fingerGroup = n('g', {}, hand, 'fingers-' + arm.side);
        arm.fingers = [0, 1, 2, 3].map(() => ({ o: n('path', stroke(C.ink, 12.5), arm.fingerGroup), f: n('path', stroke(C.skin, 8.5), arm.fingerGroup) }));
        arm.palm = n('path', { d: this._palm(), fill: C.skin }, hand, 'palm-' + arm.side);
        arm.propSlot = n('g', {}, hand, 'held-' + arm.side);
        arm.thumbO = n('path', stroke(C.ink, 14.5), hand);
        arm.thumbF = n('path', stroke(C.skin, 10), hand);
        arm.fingersOnTop = false;
        if (this._buildHandProps) this._buildHandProps(arm);
      },
      _drop(parent) {
        return this._n('path', { d: 'M0 -14Q11 2 7 8A8 8 0 0 1 -7 8Q-11 2 0 -14Z', fill: C.sweat, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, parent);
      },
      _eye(parent, side, clipId) {
        const n = this._n.bind(this);
        const g = n('g', {}, parent, 'eye-' + side);
        const white = n('path', { fill: C.eyeWhite, stroke: C.ink, 'stroke-width': 3, 'stroke-linejoin': 'round' }, g);
        const iris = n('g', { 'clip-path': 'url(#' + clipId + ')' }, g);
        const ball = n('g', {}, iris, 'pupil-' + side);
        n('circle', { r: H.iris, fill: C.iris }, ball);
        n('circle', { r: H.pupil, fill: '#120d0a' }, ball);
        n('circle', { cx: H.shine[0], cy: H.shine[1], r: H.shine[2], fill: '#fff' }, ball);
        const lid = n('path', { fill: 'none', stroke: C.ink, 'stroke-width': H.lid, 'stroke-linecap': 'round' }, g);
        const lash = H.lash ? n('path', { fill: 'none', stroke: C.ink, 'stroke-width': 4, 'stroke-linecap': 'round' }, g, 'lash-' + side) : null;
        return { g, white, iris, ball, lid, lash };
      },

      /* ---------- Desenho de um quadro ---------- */
      _render(blink, dt) {
        const t = Math.abs(this.turn), st = smooth(t);
        const sign = this.turn < 0 ? -1 : 1;
        const live = this.animation !== 'none';
        const O = OUTFITS[this.outfit];
        const j = this._sampleJoints(st);
        const e = this.faceFrame();
        this.eyes.gaze(this.time, dt, live);

        const b = this.breathing ? Math.sin(this.time * TAU / 3.7) : 0;
        put(this.svg, 'opacity', String(Math.round(this.alpha * 100) / 100));
        put(this.svg, 'display', this.alpha <= 0.001 ? 'none' : 'inline');
        put(this.flip, 'transform', 'scale(' + sign + ' 1)');
        put(this.rig, 'transform', tf(j.rootX, j.rootY, j.rootR));
        const spineT = tf(0, 0, j.spine, 1 + b * 0.007, 1 + b * 0.011);
        this.spineNodes.forEach(g => put(g, 'transform', spineT));

        this._renderBody(st, O, j, b);
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
      },
      _renderLeg(leg, j, k, st, far, O) {
        const ang = j[k + 't'], knee = j[k + 's'], ank = j[k + 'foot'];
        const ty = j[k + 'ty'], sy = j[k + 'sy'];
        put(leg.root, 'transform', tf(keyOf(k === 'r' ? G.hipR : G.hipL, st), M.hipY));
        const lenT = M.thigh * ty, lenS = M.shin * sy;
        const dT = capsule(lenT, G.thigh[0], G.thigh[1]), dS = capsule(lenS, G.shin[0], G.shin[1]);
        const footX = (k === 'r' ? -G.footX : G.footX) * (1 - st);
        const fT = tf(0, 0, ang), sT = tf(0, lenT, knee), footT = tf(footX, lenS, ank);
        leg.thighPaths.forEach(p => put(p, 'd', dT));
        leg.shinPaths.forEach(p => put(p, 'd', dS));
        leg.thigh.forEach(g => put(g, 'transform', fT));
        leg.shin.forEach(g => put(g, 'transform', sT));
        leg.foot.forEach(g => put(g, 'transform', footT));

        const shoe = spline(shape('shoe', st), true), sole = spline(shape('sole', st), true);
        put(leg.shoeO, 'd', shoe); put(leg.shoe, 'd', shoe); put(leg.shoe, 'fill', O.shoe);
        put(leg.soleO, 'd', sole); put(leg.sole, 'd', sole); put(leg.sole, 'fill', O.sole);
        put(leg.laces, 'd', G.laces(st));
        put(leg.stripe, 'stroke', O.stripe);
        put(leg.stripe, 'd', G.stripe(st));
        put(leg.cuff, 'stroke', O.pantsLight);
        const shadeOff = lerp(G.shadeX[0], G.shadeX[1], st);
        put(leg.thighShade, 'transform', tf(shadeOff, 8, 0, 1, Math.max(ty, 0.05)));
        put(leg.shinShade, 'transform', tf(shadeOff, 14, 0, 1, sy));
        put(leg.thighShade, 'fill', O.pantsShade); put(leg.shinShade, 'fill', O.pantsShade);
        put(leg.knee, 'stroke', O.pantsShade);
        shown(leg.thighShade, ty > 0.4 ? 1 : 0);
        const col = far > 0.01 ? hexMix(O.pants, O.pantsShade, far * 0.85) : O.pants;
        leg.fills.forEach(p => put(p, 'fill', col));
      },
      _renderArm(arm, j, k, st, b, far, O) {
        const sx = keyOf(k === 'r' ? A.shoulderR : A.shoulderL, st);
        const sy = M.shoulderY - j.shrug * A.shrug - b * A.breath;
        put(arm.root, 'transform', tf(sx, sy));
        const foreLen = M.foreArm * j[k + 'fl'];
        const uT = tf(0, 0, j[k + 'u']), fT = tf(0, M.upperArm, j[k + 'f']);
        const flip = k === 'r' ? 1 : lerp(-1, 1, smooth(clamp((st - 0.12) / 0.2)));
        const hs = Math.abs(flip) < 0.35 ? 0.35 * (flip < 0 ? -1 : 1) : flip;
        const hT = tf(0, foreLen, j[k + 'h'], hs * A.hand, A.hand);
        arm.upper.forEach(g => put(g, 'transform', uT));
        arm.fore.forEach(g => put(g, 'transform', fT));
        arm.hand.forEach(g => put(g, 'transform', hT));
        const dF = capsule(foreLen, A.fore[0], A.fore[1]);
        arm.forePaths.forEach(p => put(p, 'd', dF));
        put(arm.foreShade, 'd', capsule(foreLen * A.foreShade[0], A.foreShade[1], A.foreShade[2]));
        put(arm.foreShade, 'transform', tf(A.foreShade[3], A.foreShade[4]));

        const sleeveCol = far > 0.01 ? hexMix(O.top, O.topShade, far) : O.top;
        if (A.fullSleeve) {
          put(arm.foreShade, 'fill', O.topShade);
          put(arm.sleeveShade, 'd', capsule(M.upperArm * 0.74, 5, 4));
          put(arm.sleeveShade, 'transform', tf(10, 12));
          put(arm.sleeveShade, 'fill', O.topShade);
          put(arm.cuff, 'd', 'M-13 ' + f(foreLen - 3) + 'H13');
          put(arm.cuff, 'stroke', O.topDark);
          arm.skin.forEach(p => put(p, 'fill', sleeveCol));
        } else {
          const sl = O.sleeve;
          const dS = capsule(sl, A.sleeve[0], A.sleeve[1]);
          put(arm.sleeveO, 'd', dS); put(arm.sleeve, 'd', dS);
          put(arm.sleeveHem, 'd', 'M' + -A.hem[0] + ' ' + (sl + A.hem[1]) + 'H' + A.hem[0]);
          put(arm.sleeveHem, 'stroke', O.topDark);
          put(arm.sleeve, 'fill', sleeveCol);
          const skin = far > 0.01 ? hexMix(C.skin, C.skinShade, far * 0.6) : C.skin;
          arm.skin.forEach(p => put(p, 'fill', skin));
        }
        const inFront = k === 'r' || this.armLParent === this.frontArmLayer;
        shown(arm.shoulder, inFront ? 1 : 0);
        put(arm.shoulder, 'fill', sleeveCol);
        put(arm.shoulder, 'cx', f((k === 'r' ? 1 : -1) * keyOf(A.patch.cx, st)));
        put(arm.shoulder, 'cy', f(keyOf(A.patch.cy, st)));
        put(arm.shoulder, 'rx', f(keyOf(k === 'l' && A.patch.rxFar ? A.patch.rxFar : A.patch.rx, st)));
        put(arm.shoulder, 'ry', f(keyOf(A.patch.ry, st)));

        const holding = this._holding ? this._holding(k, j) : false;
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
          arm.hand[1].insertBefore(arm.fingerGroup, onTop ? arm.thumbO : arm.palm);
          arm.fingersOnTop = onTop;
        }
        const th = clamp(j[k + '4']);
        const thumb = 'M15 8L' + f(lerp(12, 30, th)) + ' ' + f(lerp(20, 18, th)) + 'L' + f(lerp(0, 36, th)) + ' ' + f(lerp(24, 36, th));
        put(arm.thumbO, 'd', thumb); put(arm.thumbF, 'd', thumb);
        const seen = j.pocket > 0.5 ? 0 : 1;
        arm.hand.forEach(g => shown(g, seen));
      },
      _renderEye(eye, clip, x, y, sx, inner, e, openMul, blink, gx, gy) {
        put(eye.g, 'transform', tf(x, y, 0, sx, 1));
        const W = H.eyeW;
        const open = Math.max(0, e.eyeOpen * openMul * (1 - blink));
        const T = H.eyeT * open * 1.33, B = 19 * e.eyeLow * (1 - blink * 0.9) * 1.33;
        const k = e.lidTilt;
        const topIn = T * (1 - k), topOut = T * (1 + k);
        const c1 = inner > 0 ? topOut : topIn, c2 = inner > 0 ? topIn : topOut;
        const top = 'M' + -W + ' 0C' + f(-W * 0.72) + ' ' + f(-c1) + ' ' + f(W * 0.72) + ' ' + f(-c2) + ' ' + W + ' 0';
        const d = top + 'C' + f(W * 0.72) + ' ' + f(B) + ' ' + f(-W * 0.72) + ' ' + f(B) + ' ' + -W + ' 0Z';
        put(eye.white, 'd', d); put(clip, 'd', d); put(eye.lid, 'd', top);
        const arc = e.eyeLow < 0;         // olhos fechados de riso: só o arco
        shown(eye.white, arc ? 0 : 1);
        shown(eye.iris, arc ? 0 : 1);
        if (eye.lash) {
          const o = inner > 0 ? -1 : 1;
          put(eye.lash, 'd', 'M' + o * W + ' 0L' + o * (W + 8) + ' -6M' + o * (W - 4) + ' ' + f(-T * 0.3) + 'L' + o * (W + 4) + ' ' + f(-T * 0.3 - 7));
        }
        const p = 0.72 + e.pupil * 0.28;
        put(eye.ball, 'transform', tf(gx * 8.5, gy * 7, 0, p, p));
      },
      _renderBrow(el, x, inner, e, sx, skew) {
        const y = H.browY + e.browY - skew;
        const w = H.browW * sx;
        const inY = y - e.browTilt, outY = y + e.browTilt * 0.45;
        const cy = y - e.browArch * H.browArch - e.browTilt * 0.1;
        put(el, 'd', 'M' + f(x - w * inner) + ' ' + f(outY + H.browOut) + 'Q' + f(x - w * H.browPull * inner) + ' ' + f(cy) + ' ' + f(x + w * inner) + ' ' + f(inY));
      },
      _renderHead(j, e, st, blink, dt) {
        const headT = tf(keyOf(H.x, st), M.headY + j.headY + j.shrug * H.shrug, j.head + e.tilt + this.headTilt);
        put(this.head, 'transform', headT);
        if (this.hairBackGroup) put(this.hairBackGroup, 'transform', headT);
        /* cabelo acompanha a cabeça com atraso de mola, estável em qualquer passo de tempo */
        const goal = clamp(-(j.spine + j.head) * 0.5 + (j.rootY - BASE_ROOT) * 0.12, -14, 14);
        for (let left = dt; left > 0; left -= 0.016) {
          const step = Math.min(left, 0.016);
          this.hairVel += ((goal - this.hairSwing) * 90 - this.hairVel * 10) * step;
          this.hairSwing += this.hairVel * step;
        }
        const flap = this.mouthFlap();
        const drop = Math.max(0, e.mouthOpen + flap * H.flap - H.jawFrom) * 0.62;
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
        this._renderHair(j, e, st, dt, jaw);

        const gx = clamp(j.gx + e.exGx + this.eyes.x, -1, 1), gy = clamp(j.gy + e.exGy + this.eyes.y, -1, 1);
        const rx = keyOf(H.eyeR, st), lx = keyOf(H.eyeL, st), ey = H.eyeY;
        const rs = key3(1, 0.96, 0.84, st), ls = Math.max(0, key3(1, 0.72, 0, st));
        this._renderEye(this.eyeR, this.clipEyeR, rx, ey, rs, 1, e, 1 + e.eyeSkew, blink, gx, gy);
        shown(this.eyeL.g, ls > 0.06 ? 1 : 0);
        this._renderEye(this.eyeL, this.clipEyeL, lx, ey, Math.max(ls, 0.06), -1, e, 1 - e.eyeSkew, blink, gx, gy);
        this._renderBrow(this.browR, rx, 1, e, rs, e.browSkew);
        shown(this.browL, ls > 0.1 ? 1 : 0);
        this._renderBrow(this.browL, lx, -1, e, Math.max(ls, 0.1), -e.browSkew * 0.5);

        const nx = keyOf(H.nose, st), ny = H.noseY, nrx = lerp(H.noseR[0], H.noseR[1], st);
        put(this.noseFill, 'cx', f(nx)); put(this.noseFill, 'cy', ny);
        put(this.noseFill, 'rx', f(nrx)); put(this.noseFill, 'ry', H.noseRy);
        const aC = lerp(Math.PI / 2, 0.2, st), span = lerp(1.9, 1.5, st);
        const arc = [];
        for (let i = 0; i <= 6; i++) {
          const a = aC - span + (2 * span * i) / 6;
          arc.push([nx + Math.cos(a) * nrx, ny + Math.sin(a) * H.noseRy]);
        }
        put(this.noseLine, 'd', spline(arc, false));
        if (this._renderMarks) this._renderMarks(e, st, rx, lx, ls);
        this._renderMouth(e, st, flap);
        this._renderEars(j, e, st);

        const sw = clamp(e.sweat), S1 = H.sweat1, S2 = H.sweat2;
        shown(this.sweat, sw > 0.04 ? 1 : 0);
        put(this.sweat1, 'transform', tf(keyOf(S1.x, st), keyOf(S1.y, st), 12, S1.s + sw * S1.s));
        put(this.sweat2, 'transform', tf(keyOf(S2.x, st), keyOf(S2.y, st), -10, S2.s + sw * S2.s));
        const fall = (this.time * 0.8) % 1;
        shown(this.tear, clamp(e.tear));
        put(this.tear, 'transform', tf(rx + 6, H.tear[0] + (this.animation === 'none' ? 0.5 : fall) * H.tear[1], 0, H.tear[2]));
      },
      _renderMouth(e, st, flap) {
        const K = H.mouth;
        const open = e.mouthOpen + flap * H.flap;
        const w = (e.mouthW + flap * -3) * key3(1, 0.86, 0.62, st);
        const smile = e.smile, skew = e.skew;
        const lY = -smile * K.corner + skew * K.skew, rY = -smile * K.corner - skew * K.skew;
        put(this.mouth, 'transform', tf(keyOf(K.x, st) + e.mouthShift * (1 - st * 0.6), K.y));
        const rnd = 0.55 + 0.42 * clamp(open / K.round);
        const up = smile * K.bow - Math.min(open, K.upMax) * 0.1;
        const low = smile * K.bow + open * 1.33;
        const top = 'M' + f(-w) + ' ' + f(lY) + 'C' + f(-w * rnd) + ' ' + f(up) + ' ' + f(w * rnd) + ' ' + f(up) + ' ' + f(w) + ' ' + f(rY);
        const d = top + 'C' + f(w * rnd) + ' ' + f(low) + ' ' + f(-w * rnd) + ' ' + f(low) + ' ' + f(-w) + ' ' + f(lY) + 'Z';
        const isOpen = open > 1.5;
        put(this.mouthShape, 'd', d); put(this.clipMouth, 'd', d);
        shown(this.mouthShape, isOpen ? 1 : 0);
        put(this.mouthLine, 'd', top);
        shown(this.mouthLine, isOpen ? 0 : 1);
        if (this.lowerLip) {
          const ly = Math.max(up, low * 0.75) * 0.75 + 7;
          put(this.lowerLip, 'd', 'M' + f(-w * 0.42) + ' ' + f(ly + 1) + 'Q0 ' + f(ly + 4) + ' ' + f(w * 0.42) + ' ' + f(ly + 1));
          shown(this.lowerLip, isOpen ? 0 : 1);
        }
        const band = Math.min(open * 0.42, K.teethMax) * e.teeth + (e.grit > 0.5 ? open : 0);
        put(this.teeth, 'y', f(up - 16)); put(this.teeth, 'height', f(Math.max(0, 16 + band)));
        shown(this.teeth, e.teeth > 0.02 && isOpen ? 1 : 0);
        put(this.tongue, 'cx', 0); put(this.tongue, 'cy', f(smile * K.bow + open * 1.05));
        put(this.tongue, 'rx', f(w * 0.62)); put(this.tongue, 'ry', f(Math.max(0, open * 0.42)));
        shown(this.tongue, e.tongue > 0.02 && isOpen ? 1 : 0);
        const mid = (up + low) / 2 - open * 0.12;
        put(this.gritLines, 'd', e.grit > 0.5
          ? 'M' + f(-w) + ' ' + f(mid) + 'H' + f(w) + 'M' + f(-w * 0.5) + ' -30V40M0 -30V40M' + f(w * 0.5) + ' -30V40'
          : 'M0 0');
      }
    };
  };
  void FLOOR;
})(typeof self !== 'undefined' ? self : this);
