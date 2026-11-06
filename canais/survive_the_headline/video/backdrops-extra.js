/*!
 * Cenários novos do vídeo: pregão, canteiro do data center, supermercado e fundos
 * de cor chapada com raios, no espírito das thumbnails.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const { element } = STH.SVGRenderer;
  const text = (k, x, y, s, size, fill, anchor) => {
    const t = element('text', { x, y, fill, 'font-family': 'Anton', 'font-size': size, 'text-anchor': anchor || 'middle', 'letter-spacing': 1 }, k.rect(0, 0, 0, 0, 'none').parentNode);
    t.textContent = s; return t;
  };

  const rays = (a, b, c) => ({ label: 'Raios', draw(k) {
    k.rect(0, 0, 1920, 1080, a);
    for (let i = 0; i < 16; i++) {
      const p = i / 16 * Math.PI * 2, q = (i + 0.5) / 16 * Math.PI * 2;
      k.poly([[960, 520], [960 + Math.cos(p) * 1500, 520 + Math.sin(p) * 1500], [960 + Math.cos(q) * 1500, 520 + Math.sin(q) * 1500]], b);
    }
    k.oval(960, 500, 760, 520, k.glow(c, 0.75));
    k.rect(0, 948, 1920, 132, '#000', 0, 0.2);
    k.rect(0, 0, 1920, 1080, k.grad([['#000', 0, 0.22], ['#000', 0.35, 0], ['#000', 0.75, 0], ['#000', 1, 0.34]]));
  } });
  STH.Backdrops.add('void_red', rays('#b81f2c', '#cf2c36', '#ff8a4a'));
  STH.Backdrops.add('void_blue', rays('#1b3fa8', '#2450c4', '#47d2ff'));
  STH.Backdrops.add('void_amber', rays('#d9730d', '#ea8a14', '#ffe08a'));
  STH.Backdrops.add('void_night', rays('#141a3c', '#1b2350', '#6a55d8'));
  STH.Backdrops.add('void_green', rays('#0f7a53', '#149066', '#9dffc9'));

  STH.Backdrops.add('trading_floor', { label: 'Pregão', draw(k) {
    k.room({ wall: '#141c33', ceiling: '#0d1324', floor: '#222b45', left: '#101730', right: '#0e142a' }, [180, 70, 1740, 650]);
    k.boards(650, '#3a4768', 150, 0.3);
    for (let r = 0; r < 3; r++) for (let c = 0; c < 6; c++) {
      const x = 215 + c * 252, y = 96 + r * 158;
      k.rect(x - 6, y - 6, 240, 146, '#050814', 8);
      k.rect(x, y, 228, 134, '#0d1a33');
      let py = y + 28, d = 'M' + (x + 8) + ' ' + py;
      for (let i = 1; i <= 16; i++) { py = Math.min(y + 124, py + (k.random() - 0.22) * 16); d += 'L' + (x + 8 + i * 13) + ' ' + py; }
      k.line(d, '#ff4048', 4);
      k.rect(x + 8, y + 8, 62, 12, '#ff4048', 3, 0.85);
    }
    k.rect(180, 590, 1560, 54, '#07090f');
    let tx = 200;
    ['CHIPS ▼21%', 'CLOUD ▼14%', 'NASDAQ ▼9%', 'S&P ▼6%'].forEach(s => { text(k, tx, 630, s, 36, '#ff5a5a', 'start'); tx += 310; });
    k.oval(960, 360, 1000, 420, k.glow('#ff3040', 0.22));
    k.haze('#2b3c6e', 0.05);
  }, front(k) {
    [[-20, 800, 560], [1380, 800, 560]].forEach(([x, y, w]) => { k.rect(x, y, w, 300, '#1a2238', 10); k.rect(x, y, w, 26, '#2b3656', 10); });
    [[130, 690], [1560, 690]].forEach(([x, y]) => { k.rect(x, y, 230, 120, '#04070e', 8); k.rect(x + 10, y + 10, 210, 96, '#2a0d17'); k.line('M' + (x + 20) + ' ' + (y + 28) + 'l50 8l40 26l40 -6l60 36', '#ff4048', 5); });
  } });

  const site = closed => ({ label: 'Data center', draw(k) {
    k.rect(0, 0, 1920, 1080, k.grad([['#8fd0ee'], ['#e6f3f2', 0.7], ['#f6efd2', 1]]));
    k.oval(1500, 200, 520, 300, k.glow('#fff4cf', 0.8));
    k.path('M0 600Q300 480 640 580T1300 560T1920 590V760H0Z', '#9fbf9f');
    k.rect(230, 250, 1500, 500, k.grad([['#d8dee6'], ['#aab4c0']]));
    for (let x = 230; x < 1730; x += 100) k.rect(x, 250, 4, 500, '#8f9aa8', 0, 0.5);
    k.rect(230, 250, 1500, 56, '#7f8a98');
    for (let i = 0; i < 9; i++) { const x = 270 + i * 160; k.rect(x, 200, 120, 52, '#c2c9d2', 4); k.oval(x + 60, 212, 48, 8, '#59636f'); }
    for (let r = 0; r < 4; r++) k.rect(300, 360 + r * 62, 1360, 20, '#5e6875', 2, 0.55);
    k.rect(860, 590, 240, 160, '#49525e'); k.rect(868, 598, 112, 152, '#39414c'); k.rect(980, 598, 112, 152, '#343b45');
    text(k, 980, 296, 'PROJECT ATLAS · AI COMPUTE CAMPUS', 40, '#fff');
    if (!closed) {
      k.rect(1740, 90, 18, 660, '#e2a728'); k.rect(1200, 96, 760, 16, '#e2a728'); k.rect(1320, 112, 4, 260, '#333'); k.rect(1296, 370, 52, 26, '#555');
      k.line('M1749 96L1600 106M1749 96L1880 106', '#333', 3);
    }
    k.rect(0, 745, 1920, 335, k.grad([['#a68a64'], ['#8a7050']]));
    for (let i = 0; i < 26; i++) k.oval(k.random() * 1920, 780 + k.random() * 280, 30 + k.random() * 50, 6 + k.random() * 7, '#7a6244', 0.55);
    [[140, 860], [1660, 880]].forEach(([x, y]) => { k.oval(x, y + 10, 92, 12, '#000', 0.2); k.oval(x, y - 44, 76, 62, '#7a4d2c'); k.oval(x, y - 44, 40, 32, '#5a3820'); k.oval(x, y - 44, 18, 15, '#b9733f'); });
    if (closed) {
      for (let x = -20; x < 1960; x += 240) k.rect(x, 520, 10, 340, '#70788a');
      for (let i = -60; i < 120; i++) { k.line('M' + (i * 24) + ' 530l310 320', '#6c7586', 2, 0.55); k.line('M' + (i * 24 + 310) + ' 530l-310 320', '#6c7586', 2, 0.55); }
      k.rect(0, 526, 1920, 8, '#70788a'); k.rect(1090, 590, 330, 170, '#c8232c', 8); k.rect(1100, 600, 310, 150, '#fff', 4);
      text(k, 1255, 668, 'SITE CLOSED', 62, '#c8232c'); text(k, 1255, 722, 'NO ENTRY · NO DELIVERIES', 28, '#222');
      k.rect(1020, 650, 60, 60, '#e2a728', 8); k.line('M1034 650v-22a16 16 0 0 1 32 0v22', '#555', 9);
    }
    k.haze('#fff6dd', 0.06);
  } });
  STH.Backdrops.add('datacenter_site', site(false));
  STH.Backdrops.add('datacenter_closed', site(true));

  /* Telejornal fictício: nenhum canal real, sempre com a marca de simulação */
  STH.Backdrops.add('news_desk', { label: 'Telejornal', draw(k) {
    k.rect(0, 0, 1920, 1080, k.grad([['#0c1730'], ['#16264d', 0.6], ['#0b1224', 1]]));
    for (let i = 0; i < 14; i++) k.rect(i * 150 - 40, 0, 70, 760, '#1d3268', 0, 0.28);
    k.rect(300, 110, 1320, 500, '#07101f', 14); k.rect(316, 126, 1288, 468, k.grad([['#3a1220'], ['#1b1030']]));
    let py = 190, d = 'M340 ' + py;
    for (let i = 1; i <= 24; i++) { py = Math.min(560, py + (k.random() - 0.2) * 34); d += 'L' + (340 + i * 52) + ' ' + py; }
    k.line(d, '#ff4048', 9);
    text(k, 960, 182, 'MARKET CORRECTION?', 62, '#fff');
  }, front(k) {
    k.rect(420, 790, 1080, 300, k.grad([['#1b2c57'], ['#101a36']]), 14); k.rect(420, 790, 1080, 20, '#39c6f0', 8);
    text(k, 960, 900, 'SIMULATED NEWS', 74, '#fff');
  } });

  STH.Backdrops.add('supermarket', { label: 'Supermercado', draw(k) {
    k.room({ wall: '#eef1ee', ceiling: '#fafbf7', floor: '#d9dbd4', left: '#e6e8e4', right: '#dfe2dd' }, [640, 200, 1280, 640]);
    k.tiles(640, '#a9ada5', 190);
    const colors = ['#d9534a', '#e2b24f', '#3f8d84', '#4f6d9e', '#f09a3e', '#7fb35a', '#c05b8a'];
    ['left', 'right'].forEach(side => {
      k.wallQuad(side, 0, 0.02, 1, 1, '#c3c9c7');
      for (let r = 0; r < 5; r++) {
        const v0 = 0.06 + r * 0.185, v1 = v0 + 0.155;
        k.wallQuad(side, 0, v0, 1, v1, '#5b626b');
        for (let c = 0; c < 22; c++) k.wallQuad(side, c / 22 + 0.003, v0 + 0.04 + k.random() * 0.03, (c + 1) / 22 - 0.005, v1, k.pick(colors));
        k.wallQuad(side, 0, v1, 1, v1 + 0.024, '#f6f7f4');
      }
    });
    k.rect(660, 215, 600, 415, '#d7dbd6');
    for (let c = 0; c < 8; c++) { k.rect(668 + c * 75, 240, 66, 380, '#c9d6df', 2); k.rect(668 + c * 75, 240, 66, 12, '#fff', 2); [0, 1, 2, 3].forEach(r => k.rect(676 + c * 75, 270 + r * 86, 50, 60, colors[(c + r) % 7], 4)); }
    k.rect(790, 86, 340, 72, '#c8232c', 8); text(k, 960, 142, 'AISLE 7', 56, '#fff');
    k.haze('#ffffff', 0.08);
  } });
})(typeof self !== 'undefined' ? self : this);
