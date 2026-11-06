/*!
 * Gráficos do vídeo. Cada função devolve { el, update(t, dur) }.
 * update é função pura do tempo do plano, então qualquer plano pode ser
 * renderizado sozinho e em qualquer ordem.
 */
(function (root) {
  'use strict';
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, k) => a + (b - a) * k;
  const out = k => 1 - Math.pow(1 - clamp(k), 3);
  const back = k => { const c = 1.9, x = clamp(k) - 1; return 1 + (c + 1) * x * x * x + c * x * x; };
  const prog = (t, start, dur) => clamp((t - start) / dur);
  const money = v => (v < 0 ? '-' : '') + '$' + Math.round(Math.abs(v)).toLocaleString('en-US');
  const div = (html, cls) => { const d = document.createElement('div'); if (cls) d.className = cls; d.innerHTML = html; return d; };
  /* entrada: sobe e aparece */
  const pop = (el, t, start, o) => {
    const k = back(prog(t, start, (o && o.dur) || 0.34));
    el.style.opacity = t < start ? 0 : clamp((t - start) / 0.12);
    el.style.transform = (o && o.base ? o.base + ' ' : '') + 'translateY(' + lerp(26, 0, k) + 'px) scale(' + lerp(0.92, 1, k) + ')';
  };

  const G = {};

  /* Manchete simulada: nunca imita um veículo real */
  G.headline = ({ kicker, title, sub }) => {
    const el = div(`<div class="abs" style="left:190px;top:280px;width:1540px;background:#f6f1e4;color:#121722;border-radius:12px;box-shadow:0 22px 0 rgba(0,0,0,.35);padding:34px 56px 44px">
      <div style="display:flex;justify-content:space-between;border-bottom:6px solid #121722;padding-bottom:12px;margin-bottom:22px">
      <span style="font:400 34px Anton;letter-spacing:.06em;color:#c8232c">${kicker}</span><span style="font:800 21px Inter;letter-spacing:.08em;align-self:center">SIMULATED HEADLINE · NOT A REAL NEWS REPORT</span></div>
      <div style="font:400 112px/1.04 Anton">${title}</div><div style="font:500 34px/1.3 Inter;margin-top:20px;color:#3a4252">${sub}</div></div>`, 'full');
    const c = el.firstChild;
    return { el, update(t) { pop(c, t, 0.05, { dur: 0.4 }); } };
  };

  /* Número gigante */
  G.big = ({ n, label, sub, color, source, count }) => {
    const el = div(`<div class="abs" style="left:0;right:0;top:170px;text-align:center"><div class="n" style="font:400 300px/1 Anton;color:${color || 'var(--red)'}"></div>
      <div class="h1 l" style="margin-top:6px">${label}</div><div class="s" style="font:500 36px/1.3 Inter;color:#c4d0e6;margin:14px auto 0;width:1200px">${sub || ''}</div></div>${source ? `<div class="src" style="left:60px;bottom:150px">Source: ${source}</div>` : ''}`, 'full');
    const a = el.querySelector('.n'), l = el.querySelector('.l'), s = el.querySelector('.s');
    return { el, update(t) {
      a.textContent = count ? count.fmt(lerp(count.from, count.to, out(prog(t, 0.1, 1.1)))) : n;
      pop(a, t, 0.05); pop(l, t, 0.4); pop(s, t, 0.7);
    } };
  };

  /* Linha neon que desaba */
  G.chart = ({ title, pts, color, tag, from, to, fmt, sideRight, source }) => {
    const w = 1300, h = 470;
    const xy = pts.map((v, i) => [i / (pts.length - 1) * w, h - clamp(v) * h]);
    const d = 'M' + xy.map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join('L');
    const c = color || '#ff3b3b';
    const grid = [0, 1, 2, 3, 4].map(i => `<path d="M0 ${i * h / 4}H${w}" stroke="#2c3d5e" stroke-width="2"/>`).join('');
    const el = div(`<div class="abs" style="left:56px;top:124px"><div class="h1" style="font-size:66px">${title}</div></div>
      <div class="abs v" style="right:80px;top:112px;text-align:right"><div class="num" style="font:400 92px/1 Anton;color:${c}"></div><div class="tag" style="font:400 34px Anton;letter-spacing:.05em;color:#fff">${tag || ''}</div></div>
      <svg class="abs" style="left:120px;top:280px;overflow:visible" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${grid}
      <path class="g" d="${d}" fill="none" stroke="${c}" stroke-opacity=".25" stroke-width="26" stroke-linejoin="round" stroke-linecap="round"/>
      <path class="l" d="${d}" fill="none" stroke="${c}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
      <circle class="dot" r="15" fill="#fff" stroke="${c}" stroke-width="7"/></svg>${source ? `<div class="src" style="left:56px;bottom:150px">${source}</div>` : ''}`, 'full');
    const ls = el.querySelectorAll('path.g,path.l'), dot = el.querySelector('.dot'), num = el.querySelector('.num');
    const L = ls[1].getTotalLength(), span = 0.72;
    ls.forEach(p => { p.style.strokeDasharray = L; });
    return { el, update(t, dur) {
      const k = out(prog(t, 0.2, dur * span));
      ls.forEach(p => { p.style.strokeDashoffset = L * (1 - k); });
      const q = ls[1].getPointAtLength(L * k);
      dot.setAttribute('cx', q.x); dot.setAttribute('cy', q.y);
      num.textContent = (fmt || money)(lerp(from, to, k));
    } };
  };

  /* Celular grande à direita, app do banco ou e-mail */
  G.phone = ({ title, balance, from, rows, alert, side }) => {
    const left = side === 'left' ? 200 : 1000;
    const el = div(`<div class="abs ph" style="left:${left}px;top:150px;width:420px;height:660px;background:#0a0f19;border-radius:52px;padding:18px;box-shadow:0 0 0 7px #2d3850,0 20px 0 7px rgba(0,0,0,.3)">
      <div style="background:#f4f6fa;height:100%;border-radius:36px;overflow:hidden;color:#121722">
      <div style="background:#c8232c;color:#fff;padding:30px 24px 22px"><div style="font:400 29px Anton;letter-spacing:.05em">${title}</div><div class="bal" style="font:400 66px/1.12 Anton;margin-top:4px"></div></div>
      ${alert ? `<div class="al" style="background:#ffb627;font:800 22px/1.25 Inter;padding:13px 20px">${alert}</div>` : ''}
      <div>${rows.map(r => `<div class="r" style="display:flex;justify-content:space-between;padding:21px 20px;border-bottom:2px solid #dde2eb;font:700 25px/1.2 Inter"><span>${r[0]}</span><span style="color:${r[2] || '#c8232c'};white-space:nowrap;margin-left:10px">${r[1]}</span></div>`).join('')}</div></div></div>`);
    const ph = el.querySelector('.ph'), bal = el.querySelector('.bal'), rs = el.querySelectorAll('.r');
    return { el, update(t) {
      pop(ph, t, 0, { dur: 0.42 });
      bal.textContent = typeof balance === 'string' ? balance : money(lerp(from === undefined ? balance : from, balance, out(prog(t, 0.5, 1.3))));
      rs.forEach((r, i) => { r.style.opacity = prog(t, 0.7 + i * 0.32, 0.25); });
    } };
  };

  /* O círculo do dinheiro */
  G.loop = o => {
    const stopped = o && o.stopped;
    const cx = 960, cy = 512, R = 248;
    const nodes = [['CHIP MAKER', -90, '#39c6f0'], ['AI LAB', 30, '#b78cff'], ['CLOUD / DATA CENTERS', 150, '#ffb627']];
    const pos = a => [cx + Math.cos(a * Math.PI / 180) * R, cy + Math.sin(a * Math.PI / 180) * R];
    const labels = ['INVESTS', 'RENTS COMPUTE', 'BUYS CHIPS'];
    const el = div(`<div class="abs h1" style="left:0;right:0;text-align:center;top:108px;font-size:56px">EVERYONE REPORTS GROWTH</div>
      <svg class="abs" style="left:0;top:0" width="1920" height="1080"><circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#2f4470" stroke-width="16" stroke-dasharray="4 26" stroke-linecap="round"/>
      <g class="coins">${[0, 1, 2, 3, 4, 5, 6, 7].map(() => '<g><circle r="24" fill="#ffd34d" stroke="#8a6200" stroke-width="5"/><text y="12" text-anchor="middle" font-family="Anton" font-size="33" fill="#8a6200">$</text></g>').join('')}</g></svg>
      ${nodes.map(([n, a, c], i) => { const [x, y] = pos(a); return `<div class="nd abs" style="left:${x - 165}px;top:${y - 56}px;width:330px;height:112px;background:${c};color:#0d1422;border:6px solid #0a101c;border-radius:18px;display:flex;align-items:center;justify-content:center;text-align:center;font:400 ${n.length > 12 ? 31 : 42}px/1.08 Anton">${n}</div>`; }).join('')}
      ${labels.map((n, i) => { const [x, y] = pos(-30 + i * 120); return `<div class="lb abs" style="left:${x - 130 + (i === 2 ? -105 : i === 0 ? 105 : 0)}px;top:${y - 22 + (i === 1 ? 20 : 0)}px;width:260px;text-align:center;font:400 32px Anton;letter-spacing:.05em;color:#fff">${n}</div>`; }).join('')}`, 'full');
    const title = el.querySelector('.h1'), coins = el.querySelectorAll('.coins > g'), nd = el.querySelectorAll('.nd'), lb = el.querySelectorAll('.lb');
    return { el, nodes: nd, update(t, dur) {
      nd.forEach((n, i) => pop(n, t, stopped ? 0 : 0.2 + i * 0.45));
      lb.forEach((n, i) => pop(n, t, stopped ? 0 : 0.9 + i * 0.45));
      coins.forEach((c, i) => { const run = stopped ? 30 * (1 - Math.pow(1 - clamp(t / 2.4), 3)) : t * 62; const [x, y] = pos(run + i * 45 - 90); c.setAttribute('transform', 'translate(' + x + ' ' + y + ')'); c.style.opacity = stopped ? 1 - prog(t, 2.4, 1.4) * 0.75 : prog(t, 1.4, 0.4); });
      if (stopped) { title.textContent = 'THE CIRCLE STOPS'; title.style.color = t > 2.4 ? '#ff3b3b' : '#fff'; }
    } };
  };

  /* Barras horizontais */
  G.bars = ({ title, items, source }) => {
    const el = div(`<div class="abs h1" style="left:80px;top:122px;width:1620px;font-size:62px">${title}</div>
      ${items.map((it, i) => `<div class="abs it" style="left:80px;top:${236 + i * 136}px;width:1700px"><div style="font:400 37px Anton;letter-spacing:.03em;margin-bottom:6px">${it.label}</div><div style="display:flex;align-items:center"><div class="b" style="height:58px;background:${it.color};border-radius:9px;width:0"></div><div class="v" style="font:400 56px Anton;margin-left:22px;color:${it.color}">${it.display}</div></div></div>`).join('')}
      ${source ? `<div class="src" style="left:80px;bottom:150px">Source: ${source}</div>` : ''}`, 'full');
    const its = el.querySelectorAll('.it');
    return { el, update(t) {
      its.forEach((d, i) => { const st = 0.4 + i * 0.6; d.querySelector('.b').style.width = out(prog(t, st, 0.9)) * items[i].v * 1320 + 'px'; d.style.opacity = prog(t, st - 0.1, 0.2); d.querySelector('.v').style.opacity = prog(t, st + 0.5, 0.3); });
    } };
  };

  /* Recibo em papel: entradas, saídas e saldo */
  G.ledger = ({ title, rows, total, totalColor }) => {
    const el = div(`<div class="abs ppr" style="left:560px;top:94px;width:800px;background:#f6f1e4;color:#121722;padding:26px 44px 28px;border-radius:8px;box-shadow:0 18px 0 rgba(0,0,0,.35)">
      <div class="h2" style="border-bottom:5px dashed #121722;padding-bottom:12px;margin-bottom:9px;font-size:50px">${title}</div>
      ${rows.map(r => `<div class="r" style="display:flex;justify-content:space-between;font:700 35px/1.62 Inter"><span>${r[0]}</span><span style="color:${r[2] || '#121722'}">${r[1]}</span></div>`).join('')}
      <div class="tt" style="display:flex;justify-content:space-between;border-top:5px solid #121722;margin-top:9px;padding-top:9px;font:400 58px Anton;color:${totalColor || '#c8232c'}"><span>${total[0]}</span><span>${total[1]}</span></div></div>`, 'full');
    const p = el.querySelector('.ppr'), rs = el.querySelectorAll('.r'), tt = el.querySelector('.tt');
    return { el, update(t, dur) {
      pop(p, t, 0, { dur: 0.4 });
      rs.forEach((r, i) => { r.style.opacity = prog(t, 0.5 + i * dur * 0.09, 0.2); });
      tt.style.opacity = prog(t, dur * 0.68, 0.2);
    } };
  };

  /* Ondas de choque da bolha */
  G.ripple = ({ rings }) => {
    const n = rings.length, cx = 960, cy = 512, base = 96, step = 72;
    const el = div(`<svg class="abs" style="left:0;top:0" width="1920" height="1080">${rings.map((r, i) => `<circle class="rg" cx="${cx}" cy="${cy}" r="${base + (n - i) * step}" fill="${r.color}"/>`).join('')}
      <circle class="core" cx="${cx}" cy="${cy}" r="${base}" fill="#ff3b3b" stroke="#0a101c" stroke-width="6"/></svg>
      <div class="abs" style="left:${cx - 90}px;top:${cy - 44}px;width:180px;text-align:center;font:400 40px/1.08 Anton">AI<br>BUBBLE</div>
      ${rings.map((r, i) => `<div class="tg abs" style="left:${i % 2 ? 1400 : 96}px;top:${190 + Math.floor(i / 2) * 208 + (i % 2 ? 48 : 0)}px;width:420px;font:400 44px/1.06 Anton;color:${r.color}"><span style="font:500 25px/1.3 Inter;color:#b9c8e2;display:block">WAVE ${i + 1}</span>${r.label}</div>`).join('')}`, 'full');
    const rg = Array.from(el.querySelectorAll('.rg')).reverse(), tg = el.querySelectorAll('.tg');
    return { el, update(t, dur) {
      rg.forEach((c, i) => {
        const st = 0.5 + i * (dur - 2.4) / n, k = out(prog(t, st, 0.8));
        c.setAttribute('r', base + k * (i + 1) * step); c.style.opacity = t < st ? 0 : 0.86;
        pop(tg[i], t, st + 0.2);
      });
    } };
  };

  /* Escolha A ou B */
  G.choice = ({ a, b, pick }) => {
    const box = (x, c, l, h) => `<div class="abs ch" style="left:${x}px;top:150px;width:810px;height:610px;background:${c};border:7px solid #0a101c;border-radius:24px;padding:24px 40px;box-shadow:0 14px 0 rgba(0,0,0,.3)"><div style="font:400 150px/1 Anton">${l}</div><div class="h1" style="font-size:62px;margin:6px 0 16px">${h.title}</div><div style="font:700 34px/1.34 Inter">${h.lines.join('<br>')}</div></div>`;
    const el = div(box(120, '#1e6fd9', 'A', a) + box(990, '#d9861a', 'B', b) + `<div class="abs" style="left:880px;top:390px;width:160px;height:160px;line-height:145px;text-align:center;background:#0d1422;border:7px solid #fff;border-radius:50%;font:400 70px/145px Anton">OR</div>`, 'full');
    const cs = el.querySelectorAll('.ch');
    return { el, update(t) {
      pop(cs[0], t, 0.1); pop(cs[1], t, pick === 'b' ? 0 : 0.5);
      if (pick !== 'b') cs[1].style.opacity = Math.min(+cs[1].style.opacity, 0.32);
    } };
  };

  /* Veredito: nota de 0 a 100 e balanço final */
  G.verdict = ({ score, label, rows }) => {
    const R = 186, C = 2 * Math.PI * R;
    const el = div(`<div class="abs h1" style="left:120px;top:118px;font-size:64px">SURVIVAL SCORE</div>
      <svg class="abs" style="left:120px;top:200px" width="480" height="480"><circle cx="240" cy="240" r="${R}" fill="none" stroke="#26344e" stroke-width="46"/><circle class="arc" cx="240" cy="240" r="${R}" fill="none" stroke="#ffb627" stroke-width="46" stroke-linecap="round" stroke-dasharray="${C}" transform="rotate(-90 240 240)"/></svg>
      <div class="abs n" style="left:120px;top:300px;width:480px;text-align:center;font:400 170px/1 Anton"></div>
      <div class="abs" style="left:120px;top:486px;width:480px;text-align:center;font:400 36px Anton;color:#9db0cf">OUT OF 100</div>
      <div class="abs lb" style="left:120px;top:698px;width:480px;text-align:center;font:400 44px Anton;color:#ffb627">${label}</div>
      ${rows.map((r, i) => `<div class="abs rw" style="left:700px;top:${196 + i * 92}px;width:1100px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px solid #2c3d5e;padding-bottom:10px;font:700 37px Inter"><span>${r[0]}</span><span style="font:400 50px Anton;color:${r[2]}">${r[1]}</span></div>`).join('')}`, 'full');
    const arc = el.querySelector('.arc'), n = el.querySelector('.n'), rw = el.querySelectorAll('.rw'), lb = el.querySelector('.lb');
    return { el, update(t, dur) {
      const k = out(prog(t, 0.3, 2.2));
      arc.setAttribute('stroke-dashoffset', C * (1 - k * score / 100));
      n.textContent = Math.round(k * score);
      lb.style.opacity = prog(t, 2.5, 0.3);
      rw.forEach((r, i) => pop(r, t, 1 + i * (dur - 3) / rows.length));
    } };
  };

  /* Três atitudes para hoje */
  G.actions = ({ items }) => {
    const el = div(`<div class="abs h1" style="left:120px;top:116px;font-size:62px">3 THINGS TO DO TODAY</div>
      ${items.map((it, i) => `<div class="abs a" style="left:120px;top:${212 + i * 186}px;width:1680px;display:flex;align-items:center;background:var(--paper);color:#121722;border-radius:16px;padding:18px 34px;box-shadow:0 10px 0 rgba(0,0,0,.3)"><div style="font:400 112px/1 Anton;color:#c8232c;width:112px">${i + 1}</div><div><div style="font:400 50px/1.1 Anton">${it[0]}</div><div style="font:500 30px/1.3 Inter;margin-top:4px">${it[1]}</div></div></div>`).join('')}`, 'full');
    const a = el.querySelectorAll('.a');
    return { el, update(t, dur) { a.forEach((d, i) => pop(d, t, 0.3 + i * dur * 0.3)); } };
  };

  /* Tela final */
  G.end = ({ next }) => {
    const box = (x, y, h) => `<div class="abs" style="left:${x}px;top:${y}px;width:690px;height:388px;background:#0a101c;border:6px solid #fff;border-radius:14px;display:flex;align-items:center;justify-content:center;text-align:center;font:400 42px/1.2 Anton;padding:30px">${h}</div>`;
    const el = div(`<div class="abs" style="left:120px;top:150px;width:800px"><div style="font:400 120px/1.02 Anton">SURVIVE<br>THE <span style="color:#ff3b3b">HEADLINE</span></div>
      <div style="font:700 36px/1.34 Inter;margin-top:26px;color:#d6e0f2">Every headline has a next 30 days.<br>We live them first.</div>
      <div class="abs" style="left:0;top:470px;background:#c8232c;font:400 42px Anton;padding:14px 30px;border-radius:12px">SUBSCRIBE</div></div>` + box(1090, 150, next) + box(1090, 566, 'THE RIVERA FILES<br>PLAYLIST'), 'full');
    return { el, update() {} };
  };

  /* Cartão de tempo entre os blocos */
  G.timecard = (big, small) => {
    const el = div(`<div class="abs" style="inset:0;background:#0b0f1a"></div><div class="abs st" style="left:-40px;right:-40px;top:424px;height:232px;background:#c8232c;transform:rotate(-2deg)"></div>
      <div class="abs t" style="left:0;right:0;top:396px;text-align:center;font:400 250px/1.15 Anton">${big}</div>
      <div class="abs s" style="left:0;right:0;top:716px;text-align:center;font:400 60px Anton;letter-spacing:.14em;color:#ffb627">${small || ''}</div>`);
    const tt = el.querySelector('.t'), ss = el.querySelector('.s'), st = el.querySelector('.st');
    return { el, update(t) {
      const k = out(prog(t, 0, 0.2));
      tt.style.transform = 'scale(' + lerp(1.55, 1, k) + ')'; tt.style.opacity = k;
      st.style.transform = 'rotate(-2deg) scaleX(' + out(prog(t, 0, 0.28)) + ')';
      ss.style.opacity = prog(t, 0.3, 0.2);
    } };
  };

  /* Abertura com o nome do canal */
  G.logo = () => {
    const el = div(`<div class="abs" style="inset:0;background:#0b0f1a"></div>
      <div class="abs w1" style="left:0;right:0;top:296px;text-align:center;font:400 210px/1 Anton">SURVIVE THE</div>
      <div class="abs st" style="left:306px;width:1308px;top:520px;height:232px;background:#c8232c"></div>
      <div class="abs w2" style="left:0;right:0;top:526px;text-align:center;font:400 210px/1.05 Anton">HEADLINE</div>`);
    const a = el.querySelector('.w1'), b = el.querySelector('.w2'), s = el.querySelector('.st');
    return { el, update(t) { pop(a, t, 0.1); s.style.transform = 'scaleX(' + out(prog(t, 0.3, 0.3)) + ')'; b.style.opacity = prog(t, 0.45, 0.15); } };
  };

  root.G = G;
  root.GfxUtil = { clamp, lerp, out, prog, money };
})(typeof self !== 'undefined' ? self : this);
