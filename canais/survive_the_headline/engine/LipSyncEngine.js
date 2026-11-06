/*!
 * LipSyncEngine — toca uma sequência de bocas de fala em um personagem.
 *
 * A linha do tempo é uma lista [{ t: segundos, v: 'A' }, ...], que pode vir de uma
 * ferramenta de alinhamento de áudio. Sem essa ferramenta, fromText() faz uma
 * aproximação pelas vogais do texto: serve para rascunho, não para fala final.
 */
(function (root) {
  'use strict';
  const STH = root.STH;

  const LETTER = { a: 'A', á: 'A', â: 'A', ã: 'A', à: 'A', e: 'E', é: 'E', ê: 'E', i: 'I', í: 'I', y: 'I', o: 'O', ó: 'O', ô: 'O', õ: 'O', u: 'U', ú: 'U', w: 'U', m: 'M', b: 'M', p: 'M', f: 'F', v: 'F' };

  function fromText(text, seconds) {
    const letters = text.toLowerCase().split('').filter(c => /[\p{L}\s]/u.test(c));
    const step = seconds / Math.max(letters.length, 1);
    const line = [];
    let last = null;
    letters.forEach((c, i) => {
      const v = /\s/.test(c) ? 'rest' : (LETTER[c] || null);
      if (v && v !== last) { line.push({ t: i * step, v }); last = v; }
    });
    line.push({ t: seconds, v: null });
    return line;
  }

  class LipSync {
    constructor(character) { this.c = character; this.line = null; this.t = 0; this.i = 0; }
    play(line) { this.line = line; this.t = 0; this.i = 0; return this; }
    stop() { this.line = null; this.c.setViseme(null); return this; }
    update(dt) {
      if (!this.line) return;
      this.t += dt;
      while (this.line && this.i < this.line.length && this.line[this.i].t <= this.t) {
        const v = this.line[this.i].v;
        this.i += 1;
        this.c.setViseme(v);
      }
      if (this.line && this.i >= this.line.length) this.line = null;
    }
  }

  STH.LipSyncEngine = { LipSync, fromText };
})(typeof self !== 'undefined' ? self : this);
