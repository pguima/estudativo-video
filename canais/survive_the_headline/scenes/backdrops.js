/*!
 * Backdrops — biblioteca de cenários vetoriais de Survive the Headline.
 *
 * Linguagem visual: sem contorno no ambiente, forma feita por planos de cor,
 * perspectiva de um ponto, muito objeto, luz em gradiente e sombra de contato.
 * O fundo fica mais suave que os personagens, que têm contorno, para eles saltarem.
 *
 * Tela de 1920 x 1080, com o chão dos personagens em y = 948.
 * Cada cenário tem draw(k) e, se quiser, front(k): a camada à frente do elenco.
 * Para criar um novo, acrescente uma entrada em SCENES usando o kit abaixo.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { element, rng, tone, lerp } = STH.SVGRenderer;
  const VP = [960, 470];      // ponto de fuga

  function kit(g, seed, label) {
    /* ids vêm do cenário, não de um contador global: a mesma cena gera o mesmo SVG */
    let gradientId = 0;
    const random = rng(seed);
    const defs = element('defs', {}, g);
    const pct = v => Math.round(v * 100) + '%';
    const k = {
      random,
      pick: list => list[Math.floor(random() * list.length) % list.length],
      /* gradiente linear: de cima para baixo, ou angulado com a = [x1,y1,x2,y2] */
      grad(stops, a) {
        const id = 'sth-' + label + '-' + (++gradientId);
        const c = a || [0, 0, 0, 1];
        const el = element('linearGradient', { id, x1: pct(c[0]), y1: pct(c[1]), x2: pct(c[2]), y2: pct(c[3]) }, defs);
        stops.forEach((s, i) => element('stop', { offset: pct(s[1] === undefined ? i / (stops.length - 1) : s[1]), 'stop-color': s[0], 'stop-opacity': s[2] === undefined ? 1 : s[2] }, el));
        return 'url(#' + id + ')';
      },
      glow(color, o) {
        const id = 'sth-' + label + '-' + (++gradientId);
        const el = element('radialGradient', { id }, defs);
        element('stop', { offset: '0%', 'stop-color': color, 'stop-opacity': o === undefined ? 0.7 : o }, el);
        element('stop', { offset: '100%', 'stop-color': color, 'stop-opacity': 0 }, el);
        return 'url(#' + id + ')';
      },
      rect: (x, y, w, h, fill, r, o) => element('rect', { x, y, width: w, height: h, rx: r || 0, fill, opacity: o === undefined ? 1 : o }, g),
      oval: (cx, cy, rx, ry, fill, o) => element('ellipse', { cx, cy, rx, ry, fill, opacity: o === undefined ? 1 : o }, g),
      path: (d, fill, o) => element('path', { d, fill, opacity: o === undefined ? 1 : o }, g),
      poly: (pts, fill, o) => element('path', { d: 'M' + pts.map(p => p[0] + ' ' + p[1]).join('L') + 'Z', fill, opacity: o === undefined ? 1 : o }, g),
      line: (d, color, w, o) => element('path', { d, fill: 'none', stroke: color, 'stroke-width': w, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', opacity: o === undefined ? 1 : o }, g),
      toVP: (p, d) => [lerp(p[0], VP[0], d), lerp(p[1], VP[1], d)],
      /* caixa em perspectiva: frente (x,y,w,h) e profundidade d para o ponto de fuga */
      box(x, y, w, h, front, d, tones) {
        const dep = d === undefined ? 0.1 : d;
        const a = [x, y], b = [x + w, y], c = [x + w, y + h], e = [x, y + h];
        const A = k.toVP(a, dep), B = k.toVP(b, dep), C = k.toVP(c, dep), E = k.toVP(e, dep);
        const t = tones || {};
        const side = t.side || tone(front, 0.76), top = t.top || tone(front, 1.14);
        if (x + w < VP[0]) k.poly([b, B, C, c], side);
        if (x > VP[0]) k.poly([a, A, E, e], side);
        if (y > VP[1]) k.poly([a, b, B, A], top);
        if (y + h < VP[1]) k.poly([e, c, C, E], tone(front, 0.62));
        k.rect(x, y, w, h, front);
      },
      /* sala em perspectiva: b = parede do fundo [x0,y0,x1,y1] */
      room(c, b) {
        const [x0, y0, x1, y1] = b;
        k.b = b;
        k.rect(0, 0, 1920, 1080, c.wall);
        k.poly([[0, 0], [1920, 0], [x1, y0], [x0, y0]], c.ceiling || tone(c.wall, 1.08));
        k.poly([[0, 1080], [1920, 1080], [x1, y1], [x0, y1]], c.floor);
        k.poly([[0, 0], [x0, y0], [x0, y1], [0, 1080]], c.left || tone(c.wall, 0.86));
        k.poly([[1920, 0], [x1, y0], [x1, y1], [1920, 1080]], c.right || tone(c.wall, 0.8));
        k.rect(x0, y0, x1 - x0, y1 - y0, k.grad([[tone(c.wall, 1.06)], [c.wall], [tone(c.wall, 0.9)]]));
        k.poly([[x0, y1], [x1, y1], [x1 + 60, y1 + 14], [x0 - 60, y1 + 14]], '#000', 0.14);
      },
      /* ponto em parede lateral: u 0 no fundo, 1 perto da câmera; v 0 teto, 1 chão */
      onWall(side, u, v) {
        const [x0, y0, x1, y1] = k.b;
        const bx = side === 'left' ? x0 : x1, nx = side === 'left' ? 0 : 1920;
        return [lerp(bx, nx, u), lerp(lerp(y0, y1, v), lerp(0, 1080, v), u)];
      },
      wallQuad(side, u0, v0, u1, v1, fill, o) {
        k.poly([k.onWall(side, u0, v0), k.onWall(side, u1, v0), k.onWall(side, u1, v1), k.onWall(side, u0, v1)], fill, o);
      },
      /* tábuas do piso convergindo para o ponto de fuga */
      onFloor(fn) {
        const [x0, , x1, y1] = k.b, id = 'sth-' + label + '-floor-' + (++gradientId), outer = g;
        element('path', { d: 'M0 1080H1920L' + x1 + ' ' + y1 + 'H' + x0 + 'Z' }, element('clipPath', { id }, defs));
        g = element('g', { 'clip-path': 'url(#' + id + ')' }, outer);
        fn();
        g = outer;
      },
      boards(y, color, step, o) {
        k.onFloor(() => { for (let x = -2400; x < 4320; x += step) k.line('M' + x + ' 1080L' + lerp(x, VP[0], (1080 - y) / (1080 - VP[1])) + ' ' + y, color, 3, o === undefined ? 0.35 : o); });
      },
      tiles(y, color, step) {
        k.boards(y, color, step, 0.3);
        k.onFloor(() => { let row = 30; for (let yy = y + 24; yy < 1080; yy += row) { k.line('M0 ' + yy + 'H1920', color, 3, 0.3); row *= 1.28; } });
      },
      /* objetos pendurados nas paredes laterais, já em perspectiva */
      wallDoor(side, u0, u1, c) {
        k.wallQuad(side, u0 - 0.015, 0.17, u1 + 0.015, 1, tone(c, 1.25));
        k.wallQuad(side, u0, 0.2, u1, 1, c);
        k.wallQuad(side, lerp(u0, u1, 0.14), 0.27, lerp(u0, u1, 0.86), 0.56, tone(c, 0.86));
        k.wallQuad(side, lerp(u0, u1, 0.14), 0.62, lerp(u0, u1, 0.86), 0.93, tone(c, 0.86));
        const h = k.onWall(side, lerp(u0, u1, 0.1), 0.6);
        k.oval(h[0], h[1], 7, 10, '#e2b24f');
      },
      wallWindow(side, u0, u1, v0, v1) {
        k.wallQuad(side, u0 - 0.02, v0 - 0.03, u1 + 0.02, v1 + 0.03, '#f4f2ec');
        k.wallQuad(side, u0, v0, u1, v1, '#a9dcf0');
        k.wallQuad(side, lerp(u0, u1, 0.47), v0, lerp(u0, u1, 0.53), v1, '#f4f2ec');
        k.wallQuad(side, u0, lerp(v0, v1, 0.47), u1, lerp(v0, v1, 0.53), '#f4f2ec');
      },
      wallArt(side, u0, u1, v0, v1, c) {
        k.wallQuad(side, u0 - 0.012, v0 - 0.02, u1 + 0.012, v1 + 0.02, '#5e4630');
        k.wallQuad(side, u0, v0, u1, v1, c);
      },
      wallShelf(side, u0, u1, v, c) {
        k.wallQuad(side, u0, v, u1, v + 0.018, c || '#8a5a30');
        k.wallQuad(side, u0, v + 0.018, u1, v + 0.05, '#000', 0.1);
      },
      wallBase(side, c) { k.wallQuad(side, 0, 0.93, 1, 1, c); },
      sky(x, y, w, h, day) {
        k.rect(x, y, w, h, k.grad(day === 'dusk' ? [['#ffb37a'], ['#f4d6b0']] : [['#8fd0ee'], ['#dff3fa']]));
      },
      city(x, y, w, h) {
        const c = tone('#9fb8c9', 1);
        for (let px = x; px < x + w;) { const bw = 40 + random() * 70, bh = h * (0.35 + random() * 0.6), rw = Math.min(bw, x + w - px); k.rect(px, y + h - bh, rw, bh, tone(c, 0.82 + random() * 0.26)); px += bw - 6; }
      },
      /* janela com caixilho, reflexo e cidade ao fundo */
      win(x, y, w, h, o) {
        const opt = Object.assign({ frame: '#f2f2ee', panes: 2, city: true }, o);
        k.rect(x - 12, y - 12, w + 24, h + 24, opt.frame);
        k.rect(x - 12, y + h + 12, w + 24, 12, tone(opt.frame, 0.78));
        k.sky(x, y, w, h, opt.day);
        if (opt.city) k.city(x, y + h * 0.3, w, h * 0.7);
        for (let i = 1; i < opt.panes; i++) k.rect(x + w * i / opt.panes - 5, y, 10, h, opt.frame);
        k.rect(x, y + h * 0.42, w, 8, opt.frame);
        k.poly([[x + w * 0.1, y + h], [x + w * 0.42, y], [x + w * 0.56, y], [x + w * 0.24, y + h]], '#fff', 0.26);
        k.poly([[x + w * 0.62, y + h], [x + w * 0.86, y], [x + w * 0.92, y], [x + w * 0.68, y + h]], '#fff', 0.2);
      },
      /* facho de luz da janela até o chão */
      shaft(pts, o) { k.poly(pts, k.grad([['#fff4d2', 0, o === undefined ? 0.34 : o], ['#fff4d2', 1, 0]])); },
      shadow(cx, cy, rx, ry, o) { k.oval(cx, cy, rx, ry, '#000', o === undefined ? 0.16 : o); },
      books(x, y, w, h) {
        const colors = ['#b5472f', '#d9863a', '#3f6f7d', '#6a7f4a', '#7a3f55', '#e2b24f', '#3c4a6b', '#a4593a', '#d6c6a8'];
        for (let px = x; px < x + w - 6;) {
          const bw = 11 + random() * 13, bh = h * (0.72 + random() * 0.26), c = k.pick(colors);
          if (random() < 0.09) { px += bw; continue; }
          k.rect(px, y + h - bh, bw - 1, bh, c);
          k.rect(px, y + h - bh, 3, bh, tone(c, 1.2), 0, 0.7);
          k.rect(px + 2, y + h - bh * 0.72, bw - 5, 4, tone(c, 1.45), 0, 0.8);
          px += bw;
        }
      },
      shelfUnit(x, y, w, h, wood, rows) {
        k.box(x, y, w, h, wood, 0.06);
        const n = rows || 4, ih = (h - 30) / n;
        for (let i = 0; i < n; i++) {
          const yy = y + 15 + i * ih;
          k.rect(x + 14, yy, w - 28, ih - 12, tone(wood, 0.45));
          k.books(x + 20, yy + 8, w - 40, ih - 22);
          k.rect(x + 14, yy, w - 28, 10, '#000', 0, 0.22);
        }
      },
      leaf(x, y, a, s, c) {
        const r = a * Math.PI / 180, tx = x + Math.cos(r) * s, ty = y + Math.sin(r) * s, nx = -Math.sin(r) * s * 0.26, ny = Math.cos(r) * s * 0.26;
        k.path('M' + x + ' ' + y + 'Q' + ((x + tx) / 2 + nx) + ' ' + ((y + ty) / 2 + ny) + ' ' + tx + ' ' + ty + 'Q' + ((x + tx) / 2 - nx) + ' ' + ((y + ty) / 2 - ny) + ' ' + x + ' ' + y + 'Z', c);
      },
      plant(x, y, s) {
        const z = s || 1;
        k.shadow(x, y + 66 * z, 66 * z, 12 * z);
        for (let i = 0; i < 11; i++) k.leaf(x, y, -160 + i * 14 + k.random() * 8, (90 + k.random() * 70) * z, i % 2 ? '#3f8f5e' : '#2f7a50');
        k.poly([[x - 40 * z, y - 4], [x + 40 * z, y - 4], [x + 30 * z, y + 66 * z], [x - 30 * z, y + 66 * z]], '#c4683f');
        k.poly([[x + 8 * z, y - 4], [x + 40 * z, y - 4], [x + 30 * z, y + 66 * z], [x + 8 * z, y + 66 * z]], '#a55430');
        k.rect(x - 44 * z, y - 12 * z, 88 * z, 14 * z, '#d67a4e', 4);
      },
      frame(x, y, w, h, c) {
        k.rect(x + 5, y + 7, w, h, '#000', 2, 0.14);
        k.rect(x, y, w, h, tone('#5e4630', 1));
        k.rect(x + 8, y + 8, w - 16, h - 16, '#f1ece2');
        k.rect(x + 18, y + 18, w - 36, h - 36, c || '#7fa8b0');
        k.path('M' + (x + 18) + ' ' + (y + h - 18) + 'l' + (w - 36) * 0.4 + ' ' + -(h - 36) * 0.5 + 'l' + (w - 36) * 0.25 + ' ' + (h - 36) * 0.3 + 'l' + (w - 36) * 0.15 + ' ' + -(h - 36) * 0.14 + 'l' + (w - 36) * 0.2 + ' ' + (h - 36) * 0.34 + 'Z', '#fff', 0.35);
      },
      lamp(x, y, s) {
        k.oval(x, y + 40, 260 * s, 200 * s, k.glow('#ffe9b0', 0.5));
        k.rect(x - 3, y - 200, 6, 170, '#3a3f4b');
        k.poly([[x - 56 * s, y + 20], [x + 56 * s, y + 20], [x + 28 * s, y - 40], [x - 28 * s, y - 40]], '#f4cf7a');
        k.poly([[x, y + 20], [x + 56 * s, y + 20], [x + 28 * s, y - 40], [x, y - 40]], '#e5b75c');
      },
      /* veladura final: afasta o fundo e deixa o elenco saltar */
      haze(c, o) { k.rect(0, 0, 1920, 1080, k.grad([[c || '#ffffff', 0, o === undefined ? 0.1 : o], [c || '#ffffff', 0.6, 0.04], ['#000000', 1, 0.12]])); }
    };
    return k;
  }

  const SCENES = {
    house_exterior: { label: 'Casa (exterior)', draw(k) {
      k.rect(0, 0, 1920, 1080, k.grad([['#7cc4ea'], ['#c6e8f2', 0.55], ['#f6efd2', 1]]));
      k.oval(1560, 180, 420, 300, k.glow('#fff6cf', 0.8));
      [[160, 150, 1.3], [1180, 90, 1], [620, 70, 0.8]].forEach(([x, y, s]) => { [0, 60, 130, 40].forEach((d, i) => k.oval(x + d * s, y + (i === 3 ? -22 : 0) * s, (70 - i * 6) * s, (30 + (i === 3 ? 16 : 0)) * s, '#fff', 0.85)); });
      k.path('M0 640Q300 520 620 610T1240 590T1920 620V760H0Z', '#9cc9a6');
      for (let i = 0; i < 26; i++) { const x = k.random() * 1920, s = 34 + k.random() * 46; k.oval(x, 640 + k.random() * 30, s, s * 1.1, k.pick(['#6fae7d', '#7cbb86', '#5f9f73'])); }
      k.rect(0, 690, 1920, 390, k.grad([['#7fc06a'], ['#5da552']]));
      for (let i = 0; i < 240; i++) { const y = 700 + k.random() * 370, x = k.random() * 1920, h = 6 + (y - 690) * 0.03; k.line('M' + x + ' ' + y + 'l' + (k.random() * 6 - 3) + ' ' + -h, '#4f9347', 2.5, 0.55); }
      /* casa */
      k.poly([[1250, 350], [1450, 410], [1450, 742], [1250, 760]], '#d9b98a');
      k.rect(470, 350, 780, 410, k.grad([['#f4dfb6'], ['#e7cb98']]));
      for (let y = 372; y < 760; y += 26) k.rect(470, y, 780, 2, '#c9a873', 0, 0.5);
      k.poly([[420, 362], [860, 96], [1300, 362]], '#a84a34');
      k.poly([[860, 96], [1300, 362], [1500, 420], [1060, 130]], '#8a3a29');
      for (let r = 1; r < 9; r++) { const y = 96 + r * 30, hw = r * 49; k.line('M' + (860 - hw) + ' ' + y + 'H' + (860 + hw), '#8f3d2c', 3, 0.7); for (let x = 860 - hw + (r % 2) * 24; x < 860 + hw; x += 50) k.line('M' + x + ' ' + y + 'v30', '#8f3d2c', 2.5, 0.5); }
      k.box(1040, 150, 76, 150, '#9a5340', 0.04);
      k.rect(430, 348, 860, 16, '#fff', 0, 0.9); k.rect(470, 364, 780, 14, '#000', 0, 0.12);
      k.win(540, 470, 170, 160, { city: false, panes: 2 }); k.win(1020, 470, 170, 160, { city: false, panes: 2 });
      [[540, 470], [1020, 470]].forEach(([x, y]) => { k.rect(x - 34, y - 12, 26, 184, '#3f7d8c'); k.rect(x + 178, y - 12, 26, 184, '#3f7d8c'); k.box(x - 20, y + 172, 210, 26, '#8a5a30', 0.03); for (let i = 0; i < 9; i++) k.oval(x - 8 + i * 24, y + 168, 16, 13, k.pick(['#e2574c', '#f4b41a', '#f28fa0', '#3f8f5e'])); });
      k.rect(780, 480, 160, 280, '#2a6f9c'); k.rect(796, 500, 54, 110, '#3b86b8'); k.rect(870, 500, 54, 110, '#3b86b8'); k.rect(796, 630, 54, 110, '#3b86b8'); k.rect(870, 630, 54, 110, '#3b86b8'); k.oval(925, 640, 7, 7, '#ffd23f');
      k.poly([[740, 760], [980, 760], [1010, 790], [710, 790]], '#c9c4ba'); k.poly([[760, 450], [960, 450], [990, 480], [730, 480]], '#a84a34');
      k.poly([[760, 790], [960, 790], [1180, 1080], [560, 1080]], k.grad([['#d6d0c4'], ['#bdb6a8']]));
      for (let y = 820, h = 26; y < 1080; y += h, h *= 1.25) k.line('M' + (760 - (y - 790) * 0.69) + ' ' + y + 'H' + (960 + (y - 790) * 0.76), '#a39c8e', 3, 0.6);
      for (let i = 0; i < 14; i++) { const x = 480 + i * 22; if (x < 770) k.oval(x, 766, 30, 34, k.pick(['#3f8f5e', '#4c9d68', '#357f52'])); const y = 1240 - i * 22; if (y > 960) k.oval(y, 766, 30, 34, k.pick(['#3f8f5e', '#4c9d68', '#357f52'])); }
      k.rect(1560, 470, 46, 300, '#7a5230'); k.rect(1584, 470, 22, 300, '#5f3f25');
      [[1582, 400, 150], [1480, 450, 100], [1680, 450, 104], [1582, 320, 110], [1500, 360, 84], [1670, 356, 84]].forEach(([x, y, r], i) => k.oval(x, y, r, r * 0.92, i % 2 ? '#3f8f5e' : '#2f7d52'));
      [[1540, 360, 60], [1640, 420, 50]].forEach(([x, y, r]) => k.oval(x, y, r, r * 0.8, '#57a872', 0.8));
      k.shadow(1600, 790, 240, 26, 0.2);
      for (let x = 0; x < 430; x += 40) { k.rect(x, 700, 24, 90, '#fbf8ef'); k.poly([[x, 700], [x + 12, 684], [x + 24, 700]], '#fbf8ef'); }
      k.rect(0, 722, 430, 10, '#efe9db'); k.rect(0, 760, 430, 10, '#efe9db');
      for (let x = 1320; x < 1500; x += 40) { k.rect(x, 700, 24, 90, '#fbf8ef'); k.poly([[x, 700], [x + 12, 684], [x + 24, 700]], '#fbf8ef'); }
      k.haze('#ffffff', 0.1);
    }, front(k) { for (let i = 0; i < 16; i++) k.leaf(40 + i * 8, 1090, -120 + i * 5, 150 + k.random() * 60, i % 2 ? '#2f7a50' : '#3f8f5e'); } },

    living_room: { label: 'Sala', draw(k) {
      k.room({ wall: '#e9d2a9', floor: '#a9784c', ceiling: '#f6ead2' }, [240, 90, 1680, 640]);
      k.boards(650, '#7d5533', 120);
      k.wallBase('left', '#f4ead6'); k.wallBase('right', '#f4ead6'); k.wallDoor('left', 0.2, 0.62, '#b98a5c'); k.wallWindow('right', 0.25, 0.6, 0.22, 0.68); k.wallArt('right', 0.68, 0.84, 0.28, 0.52, '#c98a5e');
      k.rect(0, 0, 1920, 1080, k.grad([['#fff0c4', 0, 0.12], ['#7a4a2a', 1, 0.14]]));
      k.win(340, 170, 420, 320, { panes: 3 });
      k.path('M300 150Q350 380 300 560H392Q372 340 420 150Z', '#b5472f'); k.path('M800 150Q750 380 800 560H708Q728 340 680 150Z', '#b5472f'); k.path('M300 150Q322 360 300 560H330Q338 340 350 150Z', '#8f3524'); k.rect(280, 138, 540, 16, '#6b3f22', 6);
      k.shaft([[380, 500], [740, 500], [1000, 1080], [300, 1080]], 0.3);
      k.shelfUnit(1420, 130, 250, 510, '#7a4d2c', 5);
      k.frame(860, 180, 170, 130, '#7fa8b0'); k.frame(1050, 150, 120, 160, '#c98a5e'); k.frame(1190, 200, 150, 110, '#8fb07f');
      k.box(1000, 590, 400, 60, '#6b4226', 0.05); k.rect(1040, 400, 320, 190, '#20232c', 6); k.rect(1052, 412, 296, 166, k.grad([['#3d6f8f'], ['#7fc8e0']])); k.poly([[1100, 578], [1240, 412], [1300, 412], [1160, 578]], '#fff', 0.1); k.rect(1180, 588, 40, 8, '#14161c');
      k.shadow(960, 800, 520, 44, 0.16);
      k.box(540, 500, 760, 230, '#3f7d8c', 0.06, { top: '#5aa0b0' }); for (let x = 560; x < 1290; x += 250) k.rect(x, 520, 236, 120, '#4a93a5', 18); k.rect(520, 640, 800, 110, '#357080', 18); k.rect(540, 640, 760, 26, '#4a93a5', 12);
      k.rect(490, 590, 80, 180, '#2f6675', 20); k.rect(1270, 590, 80, 180, '#2f6675', 20);
      [[640, 560, '#e9b44c'], [1160, 556, '#d9604f'], [1080, 566, '#f3ead7']].forEach(([x, y, c]) => { k.path('M' + (x - 50) + ' ' + (y + 60) + 'L' + (x - 40) + ' ' + y + 'L' + (x + 40) + ' ' + (y - 8) + 'L' + (x + 50) + ' ' + (y + 54) + 'Z', c); });
      k.oval(960, 900, 640, 90, '#b5472f'); k.oval(960, 900, 590, 78, '#d9604f'); k.oval(960, 900, 480, 58, '#e5b37a'); k.oval(960, 900, 380, 44, '#d9604f');
      k.lamp(150, 420, 1.1); k.rect(146, 440, 8, 320, '#3a3f4b'); k.oval(150, 760, 50, 12, '#2a2d38');
      k.plant(1760, 640, 1.1);
      k.haze('#fff3d8', 0.1);
    }, front(k) { k.box(-30, 950, 300, 150, '#7a4d2c', 0.02, { top: '#96663e' }); k.rect(70, 900, 70, 54, '#f3ead7', 8); k.line('M140 914q32 8 0 28', '#f3ead7', 8); k.rect(160, 932, 90, 18, '#d9604f', 3); k.rect(166, 918, 80, 16, '#3f8d84', 3); } },

    kitchen: { label: 'Cozinha', draw(k) {
      k.room({ wall: '#dcebe8', floor: '#c7ad88', ceiling: '#f2f6f4' }, [200, 80, 1720, 640]);
      k.tiles(650, '#a18a68', 150);
      k.wallDoor('left', 0.25, 0.62, '#3f8d84'); k.wallArt('right', 0.3, 0.46, 0.24, 0.5, '#f4efe2'); k.wallShelf('right', 0.52, 0.86, 0.5, '#a5764a'); [0.58, 0.68, 0.78].forEach((u, i) => { const q = k.onWall('right', u, 0.42); k.rect(q[0] - 14, q[1], 28, 44, ['#d9604f', '#e2b24f', '#3f8f5e'][i], 5); }); k.wallBase('left', '#c9dad6'); k.wallBase('right', '#c9dad6');
      for (let y = 396; y < 540; y += 24) for (let x = 200 + (y % 48 ? 0 : 24); x < 1420; x += 48) k.rect(x, y, 46, 22, k.pick(['#f4f8f6', '#eef4f1', '#e7f0ec']));
      for (let x = 230; x < 1400; x += 232) { k.box(x, 110, 226, 260, '#f1e4cd', 0.05, { top: '#f7ecd9' }); k.rect(x + 14, 124, 96, 232, '#f7ecd9', 4); k.rect(x + 118, 124, 96, 232, '#f7ecd9', 4); k.rect(x + 98, 300, 6, 40, '#8f97a3', 3); k.rect(x + 122, 300, 6, 40, '#8f97a3', 3); }
      k.rect(200, 370, 1220, 14, '#000', 0, 0.14);
      k.win(720, 400, 300, 130, { panes: 2, city: false }); k.oval(870, 470, 300, 160, k.glow('#fff6d8', 0.5));
      [[300, 462, '#d9604f'], [370, 470, '#e2b24f'], [440, 466, '#3f8f5e'], [1090, 466, '#3c4a6b'], [1160, 472, '#d9863a'], [1240, 470, '#7a3f55']].forEach(([x, y, c]) => { k.rect(x, y, 44, 68, c, 8); k.rect(x + 4, y - 10, 36, 12, tone(c, 0.7), 4); k.rect(x + 8, y + 18, 28, 26, '#fff', 3, 0.7); });
      k.box(200, 540, 1220, 28, '#6f6252', 0.02, { top: '#8b7c6a' });
      for (let x = 210; x < 1410; x += 200) { k.rect(x, 568, 194, 170, k.grad([['#3f8d84'], ['#2f7a72']])); k.rect(x + 10, 578, 86, 150, '#46978e', 3); k.rect(x + 100, 578, 86, 150, '#46978e', 3); k.rect(x + 80, 600, 5, 40, '#c8d0d6', 2); k.rect(x + 110, 600, 5, 40, '#c8d0d6', 2); }
      k.rect(200, 738, 1220, 12, '#1f4f4a');
      k.rect(1000, 524, 240, 18, '#3a3f4b', 3); [[1040, 520], [1120, 520], [1200, 520]].forEach(([x, y]) => k.oval(x, y, 24, 5, '#1f2229'));
      k.rect(1012, 568, 216, 170, '#2a2d38', 4); k.rect(1030, 610, 180, 110, '#14161c', 4); k.rect(1040, 620, 160, 60, '#3a3f4b', 3, 0.7); k.rect(1040, 584, 160, 8, '#8f97a3', 3);
      k.rect(1000, 150, 240, 80, '#b9c1c9'); k.poly([[970, 370], [1270, 370], [1240, 230], [1000, 230]], k.grad([['#c8d0d6'], ['#a6afb8']]));
      k.oval(1060, 490, 44, 12, '#b5472f'); k.rect(1020, 462, 80, 30, '#c8523a', 6); k.line('M1045 450q10 -24 0 -46M1075 452q10 -24 0 -46', '#fff', 5, 0.5);
      k.box(1470, 150, 250, 590, '#d3dbe2', 0.06, { top: '#e4eaef' }); k.rect(1470, 150, 250, 590, k.grad([['#e4eaef'], ['#c2ccd4']], [0, 0, 1, 0])); k.rect(1470, 360, 250, 6, '#8f97a3'); k.rect(1494, 240, 12, 90, '#8f97a3', 4); k.rect(1494, 400, 12, 130, '#8f97a3', 4);
      [[1560, 190, '#e9b44c', 40, 40], [1610, 204, '#d9604f', 70, 34], [1560, 250, '#3f8d84', 90, 48], [1600, 430, '#7fa8b0', 60, 70]].forEach(([x, y, c, w, h]) => k.rect(x, y, w, h, c, 3));
      k.poly([[1420, 1080], [1720, 740], [1470, 740], [1100, 1080]], '#fff', 0.05);
      k.shaft([[740, 540], [1000, 540], [1190, 1080], [600, 1080]], 0.22);
      k.haze('#ffffff', 0.09);
    }, front(k) { k.box(-60, 870, 330, 260, '#a5764a', 0.02, { top: '#c79a6c' }); k.oval(120, 870, 90, 16, '#f3ead7'); k.oval(120, 862, 60, 10, '#d9604f'); [[60, 850], [120, 840], [170, 852]].forEach(([x, y]) => k.oval(x, y, 18, 16, k.pick(['#e2574c', '#f4b41a', '#7fb35a']))); } },

    bedroom_kids: { label: 'Quarto dos filhos', draw(k) {
      k.room({ wall: '#bcd0ee', floor: '#b28f6a', ceiling: '#e3edf9', left: '#a9bfe2', right: '#9fb4d8' }, [230, 90, 1690, 640]);
      k.boards(650, '#8a6a48', 110);
      k.wallBase('left', '#eef3fb'); k.wallBase('right', '#eef3fb'); k.wallArt('left', 0.2, 0.42, 0.22, 0.52, '#ff8a1f'); k.wallArt('left', 0.52, 0.78, 0.26, 0.58, '#3f8d84'); k.wallDoor('right', 0.28, 0.66, '#f0e3cd');
      for (let i = 0; i < 30; i++) { const x = 240 + k.random() * 1400, y = 100 + k.random() * 180, s = 3 + k.random() * 3; k.oval(x, y, s, s, '#fff', 0.7); }
      k.win(1220, 170, 300, 300, { panes: 2, city: false, frame: '#ffffff' }); k.rect(1190, 150, 360, 14, '#8a5cd6', 6); k.path('M1190 160Q1210 340 1200 500H1250Q1240 320 1270 160Z', '#a97fe6'); k.path('M1550 160Q1530 340 1540 500H1490Q1500 320 1470 160Z', '#a97fe6');
      k.rect(300, 160, 150, 210, '#ff8a1f', 4); k.oval(375, 250, 50, 50, '#ffd23f'); k.rect(320, 330, 110, 14, '#fff', 3); k.rect(474, 190, 130, 180, '#8a5cd6', 4); k.line('M500 240h80M500 280h80M500 320h50', '#fff', 7); k.rect(620, 150, 190, 130, '#3f8d84', 4); k.path('M640 260l40 -60l40 40l30 -30l40 50Z', '#fff', 0.7);
      k.box(880, 170, 300, 26, '#a5764a', 0.04); k.books(900, 118, 200, 52); k.box(880, 290, 300, 26, '#a5764a', 0.04); [[910, 250, '#d9604f'], [980, 244, '#3f8f5e'], [1050, 250, '#ffd23f']].forEach(([x, y, c]) => k.oval(x, y + 12, 26, 28, c));
      k.box(860, 460, 460, 22, '#a5764a', 0.03, { top: '#c79a6c' }); k.rect(880, 482, 20, 160, '#7d5533'); k.rect(1280, 482, 20, 160, '#7d5533'); k.rect(1130, 482, 150, 130, '#8a5a30', 3); [492, 536, 580].forEach(y => { k.rect(1140, y, 130, 38, '#a5764a', 3); k.rect(1188, y + 14, 34, 7, '#e2b24f', 3); });
      k.rect(980, 340, 210, 120, '#20232c', 6); k.rect(992, 352, 186, 96, k.grad([['#2d6fa8'], ['#7fd8ff']])); k.line('M1006 372h90M1006 392h130M1006 412h70', '#fff', 6, 0.8); k.rect(1060, 460, 50, 8, '#14161c');
      k.box(280, 560, 500, 170, '#8a5a30', 0.05); k.rect(240, 480, 44, 280, '#7a4d2c', 8); k.rect(280, 540, 510, 90, k.grad([['#57a8b8'], ['#3f8d9e']]), 16); for (let x = 340; x < 780; x += 90) k.rect(x, 540, 44, 90, '#6fbbc9', 0, 0.45); k.rect(300, 510, 170, 66, '#fff', 22); k.rect(300, 548, 170, 26, '#000', 12, 0.08);
      k.oval(960, 900, 480, 66, '#f4c64f'); k.oval(960, 900, 400, 50, '#f7d87c');
      k.box(1560, 560, 110, 90, '#d9604f', 0.05); k.rect(1550, 548, 130, 18, '#b5472f', 3); k.oval(1600, 540, 30, 22, '#3f8d84');
      k.haze('#ffffff', 0.08);
    }, front(k) { [[120, 1020, '#d9604f'], [240, 1050, '#3f8d84']].forEach(([x, y, c]) => { k.rect(x, y, 120, 60, c, 6); k.rect(x, y, 120, 16, tone(c, 1.2), 6); }); } },

    bedroom_parents: { label: 'Quarto do casal', draw(k) {
      k.room({ wall: '#e5d4c6', floor: '#996f4e', ceiling: '#f6ece2', left: '#d6c3b3', right: '#cbb7a7' }, [230, 90, 1690, 640]);
      k.boards(650, '#7a5539', 120);
      k.wallBase('left', '#f6ece2'); k.wallBase('right', '#f6ece2'); k.wallDoor('left', 0.22, 0.62, '#a5764a'); k.wallArt('right', 0.3, 0.54, 0.26, 0.56, '#8fa6b8');
      for (let x = 240; x < 1680; x += 90) k.rect(x, 90, 2, 550, '#d2bfae', 0, 0.45);
      k.win(1380, 170, 240, 320, { panes: 2, city: false }); k.rect(1340, 150, 320, 12, '#6b4226', 6); k.path('M1340 156Q1370 360 1350 600H1414Q1400 330 1440 156Z', '#8fa6b8'); k.path('M1660 156Q1630 360 1650 600H1590Q1600 330 1560 156Z', '#8fa6b8');
      k.shaft([[1390, 500], [1610, 500], [1520, 1080], [1000, 1080]], 0.24);
      k.frame(560, 160, 300, 200, '#7fa8b0'); k.frame(880, 190, 130, 170, '#c98a5e'); k.frame(1030, 190, 130, 170, '#8fb07f');
      k.rect(420, 400, 860, 240, k.grad([['#7a4d2c'], ['#5e3a22']]), 10); for (let x = 440; x < 1260; x += 66) k.rect(x, 416, 54, 208, '#8a5a30', 4);
      k.box(380, 610, 940, 150, '#4f6d9e', 0.04, { top: '#6f8fc2' }); k.rect(380, 660, 940, 110, k.grad([['#46618f'], ['#3a5178']]), 8);
      k.rect(420, 540, 390, 110, '#fff', 26); k.rect(890, 540, 390, 110, '#fff', 26); k.rect(420, 610, 390, 40, '#000', 18, 0.07); k.rect(890, 610, 390, 40, '#000', 18, 0.07);
      k.rect(560, 582, 580, 90, '#d9863a', 18); k.rect(560, 650, 580, 22, '#b86f2c', 12);
      k.shadow(850, 800, 560, 36, 0.2);
      [[250, 'l'], [1330, 'r']].forEach(([x]) => { k.box(x, 600, 150, 160, '#6b4226', 0.05, { top: '#8a5a30' }); k.rect(x + 12, 616, 126, 60, '#7a4d2c', 3); k.rect(x + 12, 686, 126, 60, '#7a4d2c', 3); k.rect(x + 62, 642, 26, 6, '#e2b24f', 3); k.rect(x + 62, 712, 26, 6, '#e2b24f', 3); });
      k.lamp(325, 540, 0.9); k.rect(320, 560, 10, 40, '#3a3f4b'); k.oval(325, 598, 40, 8, '#2a2d38');
      k.books(1360, 572, 90, 28);
      k.oval(860, 930, 560, 70, '#c9a98a'); k.oval(860, 930, 500, 58, '#d9bfa2');
      k.haze('#fff3e2', 0.1);
    }, front(k) { k.plant(1810, 930, 1.5); } },

    garage: { label: 'Garagem', draw(k) {
      k.room({ wall: '#aeb4bd', floor: '#6f747d', ceiling: '#8d939c', left: '#9da3ac', right: '#8f959e' }, [200, 80, 1720, 640]);
      k.rect(0, 650, 1920, 430, k.grad([['#5f646d', 0, 0.5], ['#3a3e46', 1, 0.5]]));
      [[700, 860, 240, 30], [1260, 960, 300, 36]].forEach(([x, y, a, b]) => k.oval(x, y, a, b, '#2a2d33', 0.3));
      k.wallShelf('left', 0.15, 0.75, 0.42, '#6b4d32'); k.wallShelf('left', 0.15, 0.75, 0.66, '#6b4d32'); k.wallDoor('right', 0.3, 0.68, '#6f7680'); [0.25, 0.4, 0.56].forEach((u, i) => { const q = k.onWall('left', u, 0.3 + (i % 2) * 0.24); k.rect(q[0] - 26, q[1], 54, 60 + i * 8, ['#c8523a', '#3f7d8c', '#e2b24f'][i], 5); });
      for (let i = 0; i < 3; i++) { k.rect(420 + i * 420, 108, 220, 10, '#fff'); k.poly([[420 + i * 420, 118], [640 + i * 420, 118], [720 + i * 420, 640], [340 + i * 420, 640]], '#fff8d8', 0.06); }
      k.rect(1120, 150, 520, 490, k.grad([['#dfe4ea'], ['#b9c1ca']])); for (let y = 200; y < 640; y += 60) { k.rect(1120, y, 520, 3, '#8f97a3'); k.rect(1120, y + 3, 520, 6, '#fff', 0, 0.4); } k.rect(1100, 134, 560, 18, '#5e6773');
      [[1190, 210], [1320, 210], [1450, 210], [1580, 210]].forEach(([x, y]) => { k.rect(x, y - 44, 56, 34, '#9fd0e8'); });
      k.rect(230, 130, 620, 300, '#8d6a48', 4); for (let x = 240; x < 850; x += 15) for (let y = 142; y < 424; y += 15) k.oval(x, y, 1.6, 1.6, '#6b4d32');
      [[270, 170, 16, 110, '#c8523a'], [320, 170, 12, 130, '#8f97a3'], [364, 170, 22, 90, '#e2b24f'], [420, 170, 14, 150, '#c8523a'], [470, 170, 20, 100, '#3f7d8c'], [530, 170, 12, 120, '#8f97a3'], [580, 170, 26, 80, '#e2b24f'], [640, 170, 14, 140, '#3a3f4b'], [690, 170, 18, 110, '#c8523a'], [750, 170, 26, 90, '#8f97a3']].forEach(([x, y, w, h, c]) => { k.rect(x, y, w, h, c, 4); k.oval(x + w / 2, y - 6, 5, 5, '#3a3f4b'); });
      k.box(230, 500, 620, 30, '#a5764a', 0.05, { top: '#c79a6c' }); k.box(250, 530, 22, 150, '#6b4d32', 0.03); k.box(800, 530, 22, 150, '#6b4d32', 0.03);
      [[300, 454, 90, 46, '#c8523a'], [420, 470, 60, 30, '#3a3f4b'], [510, 440, 40, 60, '#e2b24f'], [580, 462, 110, 38, '#3f7d8c'], [720, 450, 70, 50, '#8f97a3']].forEach(([x, y, w, h, c]) => { k.rect(x, y, w, h, c, 4); k.rect(x, y, w, 8, tone(c, 1.2), 3); });
      [[300, 560], [440, 570], [580, 556]].forEach(([x, y]) => { k.rect(x, y, 100, 120, '#d9b98a', 3); k.rect(x, y + 50, 100, 12, '#c9a873'); });
      /* carro */
      k.shadow(1420, 780, 400, 34, 0.3);
      k.path('M1060 760Q1050 650 1140 630L1250 530Q1270 512 1300 512H1540Q1570 512 1590 530L1680 630Q1770 650 1760 760Z', k.grad([['#d9534a'], ['#a93a33']]));
      k.path('M1170 628L1262 544Q1272 534 1290 534H1400V628Z', '#a9dcf0'); k.path('M1420 534H1540Q1558 534 1570 546L1650 628H1420Z', '#a9dcf0'); k.poly([[1200 ,628],[1290,534],[1330,534],[1240,628]], '#fff', 0.3);
      k.rect(1060, 690, 700, 12, '#7f2a25'); [[1200, 760], [1620, 760]].forEach(([x, y]) => { k.oval(x, y, 62, 62, '#1f2229'); k.oval(x, y, 34, 34, '#c8d0d6'); k.oval(x, y, 12, 12, '#6f7680'); });
      k.haze('#ffffff', 0.05);
    }, front(k) { k.rect(-20, 960, 260, 150, '#c8523a', 8); k.rect(-20, 960, 260, 30, '#a33f2c', 8); k.rect(70, 930, 80, 34, '#7f8a96', 6); } },

    hospital: { label: 'Hospital', draw(k) {
      k.room({ wall: '#dcefec', floor: '#b8d3cf', ceiling: '#f3f8f7', left: '#cbe4e0', right: '#bfdbd6' }, [200, 80, 1720, 640]);
      k.rect(200, 500, 1520, 140, '#a9d6cf'); k.rect(200, 494, 1520, 8, '#7fbab0');
      k.tiles(650, '#9dbcb7', 180);
      k.wallQuad('left', 0, 0.76, 1, 1, '#a9d6cf'); k.wallQuad('right', 0, 0.76, 1, 1, '#a9d6cf'); k.wallDoor('left', 0.25, 0.66, '#d6dde4'); k.wallArt('right', 0.3, 0.5, 0.26, 0.5, '#f6f7f9'); k.wallArt('right', 0.58, 0.8, 0.3, 0.56, '#7fc1c9');
      for (let i = 0; i < 3; i++) { k.rect(430 + i * 420, 100, 240, 16, '#fff', 4); k.poly([[430 + i * 420, 116], [670 + i * 420, 116], [760 + i * 420, 640], [340 + i * 420, 640]], '#ffffff', 0.08); }
      k.win(250, 170, 300, 270, { panes: 2 });
      k.rect(610, 150, 170, 170, '#fff', 8); k.path('M672 180h46v44h44v46h-44v44h-46v-44h-44v-46h44Z', '#d9302f');
      k.rect(610, 340, 170, 110, '#f6f7f9', 4); k.line('M630 370h130M630 396h130M630 422h80', '#9dbcb7', 6);
      /* cortina */
      for (let x = 800; x < 1010; x += 34) k.path('M' + x + ' 130Q' + (x + 24) + ' 380 ' + x + ' 700H' + (x + 34) + 'Q' + (x + 50) + ' 380 ' + (x + 34) + ' 130Z', x % 68 ? '#8cc9d0' : '#79bcc4');
      k.rect(780, 120, 900, 8, '#8f97a3', 3);
      /* leito */
      k.shadow(1360, 800, 400, 30, 0.18);
      k.rect(1060, 470, 26, 300, '#8f97a3', 4); k.rect(1650, 590, 26, 180, '#8f97a3', 4);
      k.box(1060, 650, 620, 40, '#c8d0d6', 0.03, { top: '#dde3e8' }); k.rect(1070, 590, 600, 70, k.grad([['#fff'], ['#e4ecef']]), 12); k.rect(1090, 530, 210, 78, '#fff', 22); k.rect(1090, 580, 210, 28, '#000', 12, 0.06);
      k.rect(1300, 584, 370, 80, k.grad([['#7fc1c9'], ['#5fa8b2']]), 8);
      [[1100, 770], [1640, 770]].forEach(([x, y]) => { k.oval(x, y, 18, 18, '#3a3f4b'); k.oval(x, y, 7, 7, '#8f97a3'); });
      /* monitor e soro */
      k.rect(1500, 290, 200, 160, '#20232c', 8); k.rect(1512, 302, 176, 136, '#0f1f24', 4); k.line('M1520 370h34l14 -36l20 72l16 -36h76', '#3ddc97', 5); k.line('M1520 416h168', '#2c6f4f', 3); k.rect(1600, 450, 12, 30, '#8f97a3'); k.oval(1660, 318, 6, 6, '#3ddc97');
      k.rect(1760, 250, 10, 520, '#a6afb8', 4); k.rect(1730, 250, 70, 8, '#a6afb8', 3); k.rect(1730, 262, 40, 70, '#cdeaf2', 10, 0.9); k.line('M1750 332q-10 120 -120 230', '#a6afb8', 3); k.oval(1765, 772, 44, 10, '#6f7680');
      k.haze('#ffffff', 0.08);
    }, front(k) { k.rect(1650, 930, 320, 170, '#79bcc4', 10); k.rect(1650, 930, 320, 40, '#8cc9d0', 10); k.rect(1700, 900, 170, 30, '#f6f7f9', 4); } },

    school: { label: 'Escola', draw(k) {
      k.room({ wall: '#f1e4c1', floor: '#b6986f', ceiling: '#faf3df', left: '#e6d7b0', right: '#dccca4' }, [200, 80, 1720, 640]);
      k.boards(650, '#927652', 100);
      k.wallQuad('left', 0, 0.8, 1, 1, '#d9c79a'); k.wallQuad('right', 0, 0.8, 1, 1, '#d9c79a'); k.wallDoor('left', 0.25, 0.64, '#8a5a30'); k.wallArt('right', 0.25, 0.7, 0.2, 0.56, '#c9a873'); [[0.3, 0.26, '#fff'], [0.44, 0.38, '#ffd23f'], [0.56, 0.25, '#f28fa0']].forEach(([u, v, c]) => k.wallQuad('right', u, v, u + 0.09, v + 0.12, c));
      k.rect(200, 560, 1520, 80, '#d9c79a');
      for (let x = 210; x < 470; x += 86) { k.rect(x, 200, 80, 440, k.grad([['#3b86b8'], ['#2a6f9c']]), 3); k.rect(x + 16, 224, 48, 6, '#1f5a82'); k.rect(x + 16, 238, 48, 6, '#1f5a82'); k.rect(x + 62, 400, 8, 40, '#c8d0d6', 3); }
      k.rect(510, 130, 910, 370, '#8a5a30', 4); k.rect(524, 144, 882, 342, k.grad([['#2f6b52'], ['#275c46']]));
      k.line('M560 210h280M560 270h380M560 330h220', '#f4efe2', 8, 0.9); k.line('M1120 230v180M1040 320h170', '#f4efe2', 5, 0.8); k.line('M1050 390Q1120 200 1200 390', '#ffd23f', 5, 0.9);
      k.poly([[560, 470], [800, 200], [930, 200], [690, 470]], '#fff', 0.05);
      k.rect(524, 486, 882, 14, '#a5764a'); k.rect(620, 480, 50, 8, '#fff', 2); k.rect(700, 480, 30, 8, '#ffd23f', 2);
      k.oval(960, 110, 34, 34, '#fff'); k.oval(960, 110, 28, 28, '#f6f7f9'); k.line('M960 110v-20M960 110l14 8', '#3a3f4b', 4);
      k.win(1470, 170, 220, 320, { panes: 2, city: false });
      k.shelfUnit(1460, 500, 230, 140, '#a5764a', 1);
      [[300, 730], [760, 730], [1220, 730]].forEach(([x, y]) => { k.shadow(x + 180, y + 124, 200, 16, 0.16); k.box(x, y, 360, 22, '#c79a6c', 0.02, { top: '#dcb78c' }); k.rect(x + 20, y + 22, 320, 66, '#a5764a', 3); k.rect(x + 40, y + 88, 16, 44, '#5e6773'); k.rect(x + 304, y + 88, 16, 44, '#5e6773'); k.rect(x + 80, y - 12, 90, 12, '#d9604f', 3); k.rect(x + 200, y - 8, 60, 8, '#fff', 2); });
      k.haze('#ffffff', 0.08);
    }, front(k) { k.box(1540, 960, 460, 150, '#c79a6c', 0.02, { top: '#dcb78c' }); [[1600, 930, '#3b86b8'], [1700, 934, '#d9604f'], [1790, 926, '#3f8f5e']].forEach(([x, y, c]) => { k.rect(x, y, 80, 30, c, 3); k.rect(x, y + 22, 80, 8, '#fff', 0, 0.7); }); } },

    office: { label: 'Escritório', draw(k) {
      k.room({ wall: '#dfe4ec', floor: '#8c97a6', ceiling: '#eef1f5', left: '#cfd6e0', right: '#c5cdd8' }, [200, 80, 1720, 640]);
      k.boards(650, '#7a8594', 150, 0.25);
      k.wallBase('left', '#aab3c0'); k.wallBase('right', '#aab3c0'); k.wallDoor('left', 0.26, 0.66, '#5e6f86'); k.wallArt('right', 0.25, 0.46, 0.24, 0.5, '#3f8d84'); k.wallArt('right', 0.56, 0.84, 0.22, 0.56, '#c98a5e');
      k.win(250, 120, 1000, 460, { panes: 5, frame: '#3a4252' });
      for (let y = 136; y < 300; y += 24) k.rect(238, y, 1024, 14, '#3a4252', 0, 0.82);
      k.rect(238, 590, 1024, 50, '#c5cdd8');
      k.shaft([[300, 590], [1200, 590], [1380, 1080], [100, 1080]], 0.2);
      k.shelfUnit(1310, 110, 370, 530, '#8a4f2f', 5);
      /* mesas */
      k.shadow(600, 780, 380, 30, 0.18);
      k.box(270, 620, 680, 26, '#c79a6c', 0.03, { top: '#dcb78c' }); k.rect(300, 646, 16, 110, '#3a3f4b'); k.rect(900, 646, 16, 110, '#3a3f4b'); k.rect(690, 646, 180, 120, '#a5764a', 3); [658, 698, 734].forEach(y => { k.rect(700, y, 160, 30, '#b98a5c', 2); k.rect(762, y + 12, 36, 5, '#3a3f4b', 2); });
      k.rect(440, 460, 250, 150, '#20232c', 6); k.rect(452, 472, 226, 126, k.grad([['#3f6f94'], ['#6fbbd6']])); k.line('M466 566l40 -30l40 16l40 -44l40 22', '#ffd23f', 5); k.rect(540, 610, 50, 12, '#14161c');
      k.rect(320, 590, 90, 30, '#3a3f4b', 3); k.rect(740, 560, 46, 60, '#c8523a', 6); k.rect(748, 572, 30, 24, '#fff', 3, 0.7); k.rect(806, 596, 90, 24, '#f3ead7', 2); k.rect(806, 586, 90, 12, '#d6c6a8', 2);
      k.haze('#ffffff', 0.08);
    }, front(k) { k.plant(90, 900, 1.7); k.path('M1660 1090Q1680 900 1760 880H1920V1090Z', '#3a4252'); k.path('M1720 900Q1820 860 1920 880V960H1730Z', '#4a5468'); } },

    street: { label: 'Rua', draw(k) {
      k.rect(0, 0, 1920, 1080, k.grad([['#8fd0ee'], ['#e6f3f2', 0.62], ['#f6efd2', 1]]));
      k.oval(980, 500, 700, 420, k.glow('#fff4cf', 0.7));
      /* fundo: prédios distantes */
      for (let x = -20; x < 1940;) { const w = 80 + k.random() * 90, h = 200 + k.random() * 220; k.rect(x, 640 - h, w, h, tone('#a9c4d4', 0.9 + k.random() * 0.18)); x += w - 4; }
      /* quadras em perspectiva */
      const block = (x, y, w, c, floors) => {
        k.rect(x, y, w, 680 - y, k.grad([[tone(c, 1.06)], [c]]));
        k.rect(x, y - 12, w, 14, tone(c, 0.72));
        const wy = (680 - y - 130) / floors;
        for (let f = 0; f < floors; f++) for (let wx = x + 22; wx < x + w - 50; wx += 78) {
          const yy = y + 24 + f * wy, lit = k.random() < 0.3;
          k.rect(wx, yy, 50, wy - 22, lit ? '#f9e7a8' : '#6f93aa'); k.poly([[wx + 6, yy + wy - 22], [wx + 26, yy], [wx + 38, yy], [wx + 18, yy + wy - 22]], '#fff', 0.2); k.rect(wx - 4, yy + wy - 22, 58, 6, tone(c, 0.76));
        }
        const awn = k.pick(['#d9534a', '#3f8d84', '#e2b24f', '#4f6d9e']);
        k.rect(x + 12, 560, w - 24, 120, '#2a2d38'); k.rect(x + 20, 580, w * 0.42, 94, '#a9dcf0'); k.rect(x + w * 0.5, 580, w * 0.42 - 20, 94, '#a9dcf0');
        for (let i = 0; i < w - 24; i += 24) k.rect(x + 12 + i, 548, 24, 26, i % 48 ? tone(awn, 1.25) : awn);
        k.path('M' + (x + 12) + ' 574h' + (w - 24) + 'v8h-' + (w - 24) + 'Z', '#000', 0.2);
      };
      block(-30, 250, 320, '#b0533c', 5); block(280, 170, 340, '#d9a657', 6); block(1290, 190, 340, '#c9714a', 6); block(1620, 280, 330, '#7a6a9c', 4);
      block(620, 330, 300, '#4f6d9e', 4); block(1000, 300, 300, '#6a8f6a', 4);
      /* calçada e rua */
      k.rect(0, 680, 1920, 200, k.grad([['#d4cfc4'], ['#b9b3a7']]));
      for (let x = -600; x < 2500; x += 130) k.line('M' + x + ' 880L' + lerp(x, 960, 0.5) + ' 680', '#a39c8e', 3, 0.45);
      k.rect(0, 680, 1920, 6, '#fff', 0, 0.4);
      k.rect(0, 880, 1920, 16, '#8f8a80');
      k.rect(0, 896, 1920, 184, k.grad([['#565a63'], ['#3f434b']]));
      for (let x = -60; x < 1920; x += 260) k.rect(x, 985, 150, 12, '#f4efe2', 3);
      [[320, 640], [1600, 640]].forEach(([x, y]) => { k.rect(x - 8, y, 16, 240, '#5f3f25'); [[0, -60, 90], [-54, -30, 62], [54, -30, 62], [0, -130, 66]].forEach(([a, b, r], i) => k.oval(x + a, y + b, r, r * 0.9, i % 2 ? '#3f8f5e' : '#2f7d52')); k.shadow(x + 20, 882, 110, 12, 0.22); });
      k.rect(956, 440, 12, 440, '#3a3f4b'); k.rect(956, 440, 90, 8, '#3a3f4b'); k.oval(1044, 454, 26, 12, '#f9e7a8');
      k.rect(1490, 770, 60, 110, '#d9534a', 8); k.rect(1480, 760, 80, 16, '#a93a33', 6); k.rect(1500, 790, 40, 8, '#2a2d38');
      k.haze('#fff6dd', 0.09);
    } }
  };

  STH.Backdrops = {
    list() { return Object.keys(SCENES).map(id => ({ id, label: SCENES[id].label })); },
    /* Cenários de episódio, em arquivo próprio: entram depois dos oficiais e não mudam as sementes deles. */
    add(id, def) { SCENES[id] = def; return this; },
    draw(name, group, frontGroup) {
      if (!SCENES[name]) throw new Error('Cenário desconhecido "' + name + '". Use: ' + Object.keys(SCENES).join(', '));
      const seed = Object.keys(SCENES).indexOf(name) * 97 + 13;
      SCENES[name].draw(kit(group, seed, name));
      if (SCENES[name].front && frontGroup) SCENES[name].front(kit(frontGroup, seed + 1, name + '-front'));
    }
  };
})(typeof self !== 'undefined' ? self : this);
