/*!
 * AnimationEngine — biblioteca de animações em camadas.
 * Uma animação recebe as juntas da pose e as altera, ponderada por w (0 a 1).
 * Cada personagem herda as comuns e acrescenta as suas em config.js.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { lerp, clamp, ease } = STH.SVGRenderer;

  const HUMAN = {
    idle(j, t, w) {
      j.spine += 0.8 * Math.sin(t * 1.1) * w;
      j.head += 1.7 * Math.sin(t * 0.7 + 1) * w;
      j.headY += 1 * Math.sin(t * 0.9) * w;
      j.ru += 1.2 * Math.sin(t * 1.3) * w;
      j.lu -= 1.2 * Math.sin(t * 1.15 + 0.5) * w;
      j.rh += 3 * Math.sin(t * 1.7) * w;
      j.lh -= 3 * Math.sin(t * 1.5 + 1) * w;
    },
    nod(j, t, w) { j.headY += (5 + 5 * Math.sin(t * 7)) * w; j.spine += 0.8 * Math.sin(t * 7) * w; },
    shake(j, t, w) { j.head += 7 * Math.sin(t * 8) * w; j.gx += 0.5 * Math.sin(t * 8) * w; },
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
      j.rootX += 1.7 * s * w; j.spine += 0.5 * c * w; j.head += 0.9 * c * w;
      j.ru += 1.6 * c * w; j.lu += 1.6 * s * w; j.rh += 3 * s * w; j.lh += 3 * c * w;
    }
  };

  class Layers {
    constructor(name) { this.list = [{ name, w: 1 }]; }
    get current() { return this.list[this.list.length - 1].name; }
    set(name, dur) {
      if (dur <= 0) this.list = [{ name, w: 1 }];
      else if (this.current !== name) this.list.push({ name, w: 0, dur });
    }
    update(dtMs) {
      const n = this.list.length, dur = this.list[n - 1].dur || 300;
      this.list.forEach((a, i) => { a.w = clamp(a.w + (i === n - 1 ? 1 : -1) * dtMs / dur); });
      if (n > 1 && this.list[n - 1].w >= 1) this.list = [this.list[n - 1]];
    }
  }

  /* Braço controlado à parte da pose (setArm). */
  const armState = () => ({ w: 0, on: false, v: null });

  STH.AnimationEngine = { HUMAN, Layers, armState, ease };
})(typeof self !== 'undefined' ? self : this);
