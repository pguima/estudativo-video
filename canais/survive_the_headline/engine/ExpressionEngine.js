/*!
 * ExpressionEngine — estado do rosto: mistura de expressões, piscadas, olhar e bocas de fala.
 * Também fornece o Mixer usado por expressões e poses: trocar no meio de uma
 * transição nunca dá salto.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { clamp, ease, lerpDict, lerp } = STH.SVGRenderer;

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

  /* Valores neutros: toda expressão de todo personagem aceita estes campos. */
  const NEUTRAL_FACE = {
    browY: 0, browTilt: 0, browArch: 4, browSkew: 0, eyeOpen: 0.88, eyeLow: 0.92, eyeSkew: 0, lidTilt: 0, pupil: 1,
    mouthW: 22, mouthOpen: 0, smile: 0.15, teeth: 0, grit: 0, tongue: 0, skew: 0, mouthShift: 0,
    tint: 0, sweat: 0, tear: 0, blush: 0, exGx: 0, exGy: 0, tilt: 0
  };

  /* Bocas de fala comuns a todos os humanos. Sobrepõem a boca da expressão. */
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

  const complete = (table, base) => {
    const out = {};
    Object.keys(table).forEach(k => { out[k] = Object.assign({}, NEUTRAL_FACE, base, table[k]); });
    return out;
  };

  /* Piscadas e olhar automático: iguais para todos, com semente própria. */
  class Eyes {
    constructor(random) {
      this.random = random;
      this.nextBlink = 1.3; this.blinkT = -1; this.enabled = true;
      this.look = null; this.x = 0; this.y = 0; this.tx = 0; this.ty = 0; this.next = 1.5;
    }
    blink() { this.blinkT = 0; }
    blinkAmount(time, dt) {
      if (this.enabled && time >= this.nextBlink && this.blinkT < 0) {
        this.blinkT = 0;
        this.nextBlink = time + 1.8 + this.random() * 3.6;
      }
      if (this.blinkT < 0) return 0;
      this.blinkT += dt;
      const p = this.blinkT / 0.16;
      if (p >= 1) { this.blinkT = -1; return 0; }
      return Math.sin(p * Math.PI);
    }
    gaze(time, dt, auto) {
      if (this.look) { this.tx = this.look.x; this.ty = this.look.y; }
      else if (auto && time >= this.next) {
        const away = this.random() < 0.35;
        this.tx = away ? (this.random() - 0.5) * 0.9 : 0;
        this.ty = away ? (this.random() - 0.5) * 0.4 : 0;
        this.next = time + 1.4 + this.random() * 2.8;
      } else if (!auto) { this.tx = 0; this.ty = 0; }
      const k = clamp(dt * 18);
      this.x = lerp(this.x, this.tx, k); this.y = lerp(this.y, this.ty, k);
    }
  }

  STH.ExpressionEngine = { Mixer, Eyes, NEUTRAL_FACE, VISEMES, complete };
})(typeof self !== 'undefined' ? self : this);
