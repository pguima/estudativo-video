/* Artes do canal, com os mesmos personagens dos vídeos. ?art=avatar|banner|marca|logo [&guia=1] */
(async () => {
  const q = new URLSearchParams(location.search), art = q.get('art') || 'banner', A = document.getElementById('art');
  const size = (w, h) => { A.style.width = w + 'px'; A.style.height = h + 'px'; };
  const div = (css, html, cls) => { const d = document.createElement('div'); if (cls) d.className = cls; d.style.cssText = css; if (html) d.innerHTML = html; A.appendChild(d); return d; };
  const svg = (w, h, inner, css) => div('position:absolute;left:0;top:0;' + (css || ''), `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="display:block">${inner}</svg>`);
  /* contorno de adesivo: um filtro só, sobre a área visível (filtro na caixa gigante derruba o navegador) */
  const sticker = (r, cor, clip) => {
    const id = 'st' + r, w = div('position:absolute;inset:0;overflow:hidden;filter:url(#' + id + ');' + (clip ? 'clip-path:' + clip : ''));
    div('position:absolute;width:0;height:0', `<svg width="0" height="0"><filter id="${id}" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feMorphology in="SourceAlpha" operator="dilate" radius="${r}" result="d"/><feFlood flood-color="${cor}"/><feComposite in2="d" operator="in" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge></filter></svg>`);
    return w;
  };
  /* cx = centro do personagem; base = onde pisa; s = lado da caixa (300 = escala 1) */
  const who = async (name, o) => {
    const w = div(`left:${o.cx - o.s / 2}px;top:${o.base - o.s}px;width:${o.s}px;height:${o.s}px;${o.css || ''}`, '<div></div>', 'who');
    if (o.into) o.into.appendChild(w);
    const c = await CharacterEngine.load(name, { container: w.firstChild });
    if (o.outfit) c.setOutfit(o.outfit);
    c.setPose(o.pose); c.setExpression(o.expr); c.setDirection(o.dir || 'front');
    if (c.tick) for (let i = 0; i < 6; i++) c.tick(1000);
    if (o.look) { c.lookAt(o.look[0], o.look[1]); if (c.tick) c.tick(1000); }
    return c;
  };
  /* selo do relógio: mostrador com o tempo acabando */
  const dial = (cx, cy, r, opt = {}) => {
    const end = (opt.left === undefined ? 0.17 : opt.left) * 2 * Math.PI, ang = -Math.PI / 2 - end;
    const sx = cx + r * Math.cos(ang), sy = cy + r * Math.sin(ang);
    let t = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${opt.face || '#12307a'}"/>`;
    t += `<path d="M${cx} ${cy}L${cx} ${cy - r}A${r} ${r} 0 0 0 ${sx.toFixed(1)} ${sy.toFixed(1)}Z" fill="${opt.wedge || '#e8232c'}"/>`;
    for (let i = 0; i < 60; i++) {
      const a = i / 60 * 2 * Math.PI, big = i % 5 === 0, r1 = r * (big ? 0.84 : 0.91), r2 = r * 0.965;
      t += `<line x1="${(cx + r1 * Math.sin(a)).toFixed(1)}" y1="${(cy - r1 * Math.cos(a)).toFixed(1)}" x2="${(cx + r2 * Math.sin(a)).toFixed(1)}" y2="${(cy - r2 * Math.cos(a)).toFixed(1)}" stroke="#fff" stroke-opacity="${big ? 1 : 0.55}" stroke-width="${r * (big ? 0.026 : 0.012)}" stroke-linecap="round"/>`;
    }
    t += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${opt.rim || '#ffb627'}" stroke-width="${r * 0.075}"/>`;
    return t;
  };
  const logo = (x, y, k, extra) => div(`left:${x}px;top:${y}px;font-size:${k}px;${extra || ''}`, `<span class="l1" style="font-size:.62em">Survive the</span><span class="l2">Headline</span>`, 'logo');

  await document.fonts.load('40px Anton'); await document.fonts.load('800 40px Inter');

  if (art === 'avatar' || art === 'marca') {
    size(800, 800);
    const trans = art === 'marca';
    if (!trans) A.style.background = '#0d1422';
    svg(800, 800, dial(400, 400, trans ? 372 : 352, { left: 0.17 }));
    await who('biscuit', { cx: 400, base: 1040, s: 2500, pose: 'sitting', expr: 'scared', into: sticker(10, '#fff', trans ? 'circle(372px at 400px 400px);' : '') });
  }

  if (art === 'logo') {
    size(1500, 460);
    svg(1500, 460, dial(215, 230, 196, { left: 0.17 }));
    await who('biscuit', { cx: 215, base: 495, s: 1150, pose: 'sitting', expr: 'scared', into: sticker(6, '#fff', 'circle(196px at 215px 230px);') });
    logo(450, 58, 205);
  }

  if (art === 'banner') {
    size(2560, 1440);
    /* céu: azul frio à esquerda, incêndio laranja atrás da família */
    A.style.background = 'radial-gradient(900px 760px at 1600px 800px,#ffb627 0%,#ff7a18 34%,#d42a2a 60%,rgba(120,20,60,0) 100%),linear-gradient(100deg,#0b1a44 0%,#12307a 40%,#2a1b5e 75%,#3a1140 100%)';
    const rnd = (s => () => (s = (s * 16807) % 2147483647) / 2147483647)(4242);
    let b = '';
    /* grade e gráfico despencando */
    for (let x = 0; x <= 2560; x += 120) b += `<line x1="${x}" y1="0" x2="${x}" y2="1440" stroke="#39c6f0" stroke-opacity=".07" stroke-width="2"/>`;
    for (let y = 0; y <= 1440; y += 120) b += `<line x1="0" y1="${y}" x2="2560" y2="${y}" stroke="#39c6f0" stroke-opacity=".07" stroke-width="2"/>`;
    let d = 'M0 250';
    [[300, 215], [560, 280], [800, 205], [1000, 250], [1180, 170], [1330, 240], [1470, 215], [1610, 420], [1760, 380], [1960, 720], [2150, 680], [2380, 1010], [2560, 1120]].forEach(p => { d += `L${p[0]} ${p[1]}`; });
    b += `<path d="${d}" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="30" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="#ff3b3b" stroke-width="14" stroke-linejoin="round"/>`;
    /* bairro em silhueta */
    const rua = (base, cor, esc) => {
      let x = -60, s = '';
      while (x < 2620) {
        const w = (190 + rnd() * 150) * esc, h = (120 + rnd() * 70) * esc, r = (70 + rnd() * 50) * esc;
        s += `<path d="M${x} ${base}V${base - h}L${x + w / 2} ${base - h - r}L${x + w} ${base - h}V${base}Z" fill="${cor}"/>`;
        const cabe = base - h * .4 < 985, j1 = rnd() > 0.45, j2 = rnd() > 0.72;
        if (j1 && cabe) s += `<rect x="${x + w * .3}" y="${base - h * .72}" width="${w * .15}" height="${h * .32}" fill="#ffb627" fill-opacity=".85"/>`;
        if (j2 && cabe) s += `<rect x="${x + w * .58}" y="${base - h * .72}" width="${w * .15}" height="${h * .32}" fill="#ffb627" fill-opacity=".55"/>`;
        x += w + (rnd() * 70) * esc;
      }
      return s;
    };
    b += rua(1060, '#241646', 1.0) + rua(1130, '#140f30', 1.25);
    svg(2560, 1440, b);
    /* a família, na frente do fogo */
    const glow = 'filter:drop-shadow(0 0 14px rgba(255,190,90,.65));';
    await who('dan', { cx: 1490, base: 1260, s: 730, pose: 'hands_on_head', expr: 'shocked', css: glow });
    await who('mia', { cx: 1805, base: 1250, s: 690, pose: 'worried', expr: 'worried', dir: 'three-quarter-left', css: glow });
    await who('leo', { cx: 1692, base: 1215, s: 660, pose: 'using_phone', expr: 'shocked', css: glow });
    await who('bea', { cx: 1592, base: 1072, s: 680, pose: 'hands_on_cheeks', expr: 'scared', css: glow });
    /* muro do quintal: esconde as pernas e deixa os rostos na faixa do celular */
    let m = '<rect x="0" y="1012" width="2560" height="330" fill="#3b1f2e"/><rect x="0" y="992" width="2560" height="30" rx="4" fill="#6d3a43"/>';
    for (let y = 1022, r = 0; y < 1340; y += 40, r++) {
      m += `<line x1="0" y1="${y}" x2="2560" y2="${y}" stroke="#23121f" stroke-width="5"/>`;
      for (let x = r % 2 ? 60 : 0; x < 2560; x += 120) m += `<line x1="${x}" y1="${y}" x2="${x}" y2="${y + 40}" stroke="#23121f" stroke-width="5"/>`;
    }
    svg(2560, 1440, m);
    div('left:0;top:1102px;width:2560px;text-align:center;font:150px/1 Anton;letter-spacing:.03em;color:#f6f1e4;opacity:.93', 'NEW HEADLINE. <span style="color:#ffb627">SAME FAMILY.</span>', 'abs');
    await who('biscuit', { cx: 1362, base: 1002, s: 790, pose: 'sitting', expr: 'scared', dir: 'three-quarter-right', css: glow });
    /* marca e promessa */
    logo(668, 556, 118);
    div('left:670px;top:790px;font:800 33px/1.25 Inter;letter-spacing:.005em;text-shadow:0 3px 12px rgba(0,0,0,.6)', 'Every headline has a next 30 days.<br><span style="color:#ffb627">We live them first.</span>', 'abs');
    /* painel de sobrevivência, fora da área do celular */
    const row = (n, v, p, c) => `<div class="row"><span>${n}</span><span style="color:${c}">${v}</span><i><b style="width:${p}%;background:${c}"></b></i></div>`;
    div('left:2080px;top:548px;width:400px', '<h6>SURVIVAL PANEL</h6>' + row('CASH', '$212', 8, '#ff3b3b') + row('FOOD', '2 days', 16, '#ffb627') + row('POWER', '4%', 4, '#ff3b3b') + row('STRESS', '97', 97, '#ff3b3b'), 'panel');
    div('left:70px;top:590px;font-size:92px;transform:rotate(-3deg)', 'DAY 1', 'stamp');
    div('left:225px;top:712px;font-size:74px;transform:rotate(2deg)', 'HOUR 14', 'stamp');
    div('left:95px;top:812px;font-size:64px;transform:rotate(-2deg)', '3:14 AM', 'stamp');
    /* faixa que só a TV mostra */
    div('left:0;top:1330px;width:2560px;height:110px;background:#e8232c;font:800 44px/110px Inter;white-space:nowrap;text-align:center;letter-spacing:.02em', 'WHAT IF THE GRID GOES DOWN?&nbsp;&nbsp;·&nbsp;&nbsp;WHAT IF THE DOLLAR LOSES 40%?&nbsp;&nbsp;·&nbsp;&nbsp;SIMULATION BASED ON REAL DATA', 'abs');
    if (q.get('guia')) {
      div('left:662px;top:551px;width:1235px;height:338px;border-color:#35d07f;color:#35d07f', 'CELULAR 1235x338', 'guia');
      div('left:507px;top:508px;width:1546px;height:423px;border-color:#fff;color:#fff', 'TABLET 1546x423', 'guia');
      div('left:0;top:508px;width:2560px;height:423px;border-color:#39c6f0;color:#39c6f0', 'COMPUTADOR 2560x423', 'guia');
      div('left:0;top:0;width:2560px;height:1440px;border-color:#ffb627;color:#ffb627', 'TV 2560x1440', 'guia');
    }
  }
  window.ok = 1;
})().catch(e => { console.error(e); window.ok = 1; });
