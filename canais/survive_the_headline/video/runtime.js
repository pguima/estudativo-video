/*!
 * Runtime do episódio: transforma a lista de planos de episode.js em quadros.
 *
 * Cada plano é autônomo: prepare(i) monta a cena, frame(t) desenha o instante t.
 * O painel é calculado a partir de todos os planos anteriores, então um plano
 * pode ser renderizado sozinho, em qualquer processo, e sair idêntico.
 *
 * Sem voz, a duração vem da contagem de palavras. Com voz, episodes/<ep>/voz.js
 * (gerado por video/alinhar.py) traz a duração medida e o tempo de cada palavra.
 */
(function (root) {
  'use strict';
  const { clamp, lerp, out, prog, money } = root.GfxUtil;
  const $ = id => document.getElementById(id);
  const PACE = 2.45;                    // palavras por segundo da narração estimada
  const SPEAKER = { dan: ['DAN', '#7fc4ff'], mia: ['MIA', '#6fe3c1'], leo: ['LEO', '#ffb627'], bea: ['BEA', '#ff9ccb'] };
  const MOOD = { day: null, dusk: ['#ff9a5a', 0.2], night: ['#1c2a66', 0.56], dark: ['#0d1538', 0.72], tense: ['#7a1f2a', 0.2] };
  const ROWS = [['cash', 'CASH'], ['food', 'FOOD'], ['power', 'POWER'], ['stress', 'STRESS'], ['health', 'HEALTH']];
  const HEALTH = { OK: 1, TIRED: 0.6, LOW: 0.3 };

  let gradeBase = 0, shots = [], scene, cur = null, cast = {}, extras = [], plate = null, lastT = 0, fired = 0, showCaps = true;

  function words(s) { return s ? s.trim().split(/\s+/).length : 0; }

  /* Monta durações e tempo global de cada plano */
  function layout() {
    let at = 0;
    shots.forEach((s, i) => {
      s.i = i;
      const v = root.EP_VOZ && root.EP_VOZ[s.id];
      if (s.card) s.dur = s.dur || 1.7;
      if (v) { s.dur = v.d + (s.hold || 0); if (v.wt) s.wt = v.wt; }
      if (!s.dur) s.dur = Math.max(2.4, words(s.n) / PACE + 0.55) + (s.hold || 0);
      s.dur = Math.round(s.dur * 30) / 30;   /* quadro inteiro: o som usa este mesmo início */
      s.start = at; at += s.dur;
    });
    /* troca de lugar pede transição; mesmo cenário fica no corte seco */
    shots.forEach((s, i) => {
      const n = shots[i + 1];
      if (!n || s.card || n.card || s.tout === false) return;
      const here = s.bg || 'gfx', there = n.bg || 'gfx';
      if (here === there && s.bg) return;
      const kind = here === 'gfx' || there === 'gfx' ? 'zoom' : 'whip';
      s.tout = s.tout || kind; n.tin = n.tin || kind;
    });
    return at;
  }

  /* Estado do painel no instante t do plano i: histórico + mudanças do plano */
  function hudAt(i, t) {
    const v = Object.assign({}, EP.hudStart), prev = Object.assign({}, EP.hudStart), when = {};
    let on = false, deltas = [];
    for (let k = 0; k <= i; k++) {
      const s = shots[k];
      if (s.hudOn) on = true;
      if (!s.hud) continue;
      const fraction = s.hudAt === undefined ? 0.45 : s.hudAt, at = s.dur * fraction;
      if (k < i || t >= at) {
        Object.keys(s.hud).forEach(key => {
          prev[key] = v[key]; v[key] = s.hud[key]; when[key] = k === i ? t - at : 99;
          if (k === i && key === 'cash') deltas.push({ d: s.hud.cash - prev.cash, age: t - at });
        });
      }
    }
    return { v, prev, when, on, deltas };
  }

  function drawHud(h) {
    const el = $('hud');
    el.style.display = h.on ? 'block' : 'none';
    if (!h.on) return;
    if (!el.firstChild) {
      el.innerHTML = '<div class="ttl">SURVIVAL PANEL</div>' + ROWS.map(([k, l]) => `<div class="row" id="r-${k}"><label>${l}</label><div class="bar"><i></i></div><div class="val"></div></div>`).join('') + '<div class="delta" id="delta"></div>';
    }
    let punch = 0;
    ROWS.forEach(([key]) => {
      const age = h.when[key] === undefined ? 99 : h.when[key], k = out(clamp(age / 0.8));
      const row = $('r-' + key), bar = row.querySelector('i'), val = row.querySelector('.val');
      const a = h.prev[key], b = h.v[key];
      let ratio, text;
      if (key === 'cash') { const x = lerp(a, b, k); ratio = x / 7000; text = money(x); }
      else if (key === 'food') { const x = lerp(a, b, k); ratio = x / 14; text = Math.round(x) + ' DAYS'; }
      else if (key === 'power') { const x = lerp(a, b, k); ratio = x / 100; text = Math.round(x) + '%'; }
      else if (key === 'stress') { const x = lerp(a, b, k); ratio = x / 100; text = Math.round(x) + '/100'; }
      else { ratio = HEALTH[b]; text = b; }
      ratio = clamp(ratio);
      const danger = key === 'stress' ? ratio : 1 - ratio;
      bar.style.width = ratio * 100 + '%';
      val.textContent = text;
      bar.style.background = danger > 0.66 ? '#ff3b3b' : danger > 0.4 ? '#ffb627' : '#35d07f';
      val.style.color = danger > 0.66 ? '#ff6a6a' : '#fff';
      const flash = age < 1.5 ? 1 - age / 1.5 : 0;
      punch = Math.max(punch, age < 0.5 ? 1 - age / 0.5 : 0);
      row.style.background = flash ? 'rgba(255,59,59,' + flash * 0.42 + ')' : 'transparent';
    });
    el.style.transform = 'scale(' + (1 + punch * 0.1) + ')';
    const dl = $('delta'), last = h.deltas[h.deltas.length - 1];
    if (last && last.d && last.age < 2.4) {
      dl.style.display = 'block'; dl.style.bottom = '150px';
      dl.textContent = (last.d > 0 ? '+' : '-') + money(Math.abs(last.d));
      dl.style.color = last.d > 0 ? '#35d07f' : '#ff5a5a';
      dl.style.opacity = last.age > 2 ? 1 - (last.age - 2) / 0.4 : clamp(last.age / 0.1);
    } else dl.style.display = 'none';
  }

  /* Legenda palavra a palavra, em blocos de até 10 palavras */
  function buildCap(s) {
    const box = $('cap');
    box.innerHTML = '';
    box.style.display = 'none';
    s.chunks = [];
    if (!s.n || !showCaps) return;
    const list = s.n.trim().split(/\s+/), total = list.reduce((a, w) => a + w.length + 2, 0), span = s.dur - 0.45 - (s.hold || 0);
    let at = 0.2, chunk = [];
    list.forEach((w, i) => {
      const d = span * (w.length + 2) / total;
      chunk.push({ w, at, end: at + d }); at += d;
      const stop = /[.?!,:]$/.test(w) && chunk.length >= 4;
      if (chunk.length >= 10 || stop || i === list.length - 1) { s.chunks.push(chunk); chunk = []; }
    });
  }
  function drawCap(s, t) {
    const box = $('cap');
    if (!s.chunks || !s.chunks.length) { box.style.display = 'none'; return; }
    let c = s.chunks.find(ch => t < ch[ch.length - 1].end);
    if (!c) c = s.chunks[s.chunks.length - 1];
    if (t > c[c.length - 1].end + 0.5 || t < 0.15) { box.style.display = 'none'; return; }
    box.style.display = 'block';
    if (box._c !== c) {
      box._c = c;
      const who = s.who && SPEAKER[s.who];
      box.innerHTML = '<div class="box">' + (who ? `<span class="who" style="color:${who[1]}">${who[0]}</span>` : '') + c.map(x => `<span class="w">${x.w}</span> `).join('') + '</div>';
    }
    box.querySelectorAll('.w').forEach((el, i) => el.classList.toggle('on', t >= c[i].at));
  }

  const SCENE_FLOOR = 948;
  /* profundidade: 0 no chão do elenco, 1 no fundo da sala, negativo perto da lente */
  const depthAt = d => ({ y: SCENE_FLOOR - 250 * d, k: d >= 0 ? 1 - 0.47 * d : 1 - d * 1.1 });

  function setDepth(c, a) {
    const d = a.d || 0, { y, k } = depthAt(d), h = a.h || 1, g = a.girth || 1, x0 = c.x0;
    c.wrap.setAttribute('transform', 'translate(' + x0 + ' ' + y + ') scale(' + (k * h * g) + ' ' + (k * h) + ') translate(' + (-x0) + ' ' + (-SCENE_FLOOR) + ')');
    c.wrap.style.filter = a.blur ? 'blur(' + a.blur + 'px)' : a.sil ? 'brightness(0)' : '';
  }

  function wrapDepth(c, a, x) {
    const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    c.slot.parentNode.insertBefore(g, c.slot); g.appendChild(c.slot);
    c.wrap = g; c.x0 = x;
    setDepth(c, a);
  }

  async function addActor(id, name, a, seed, spec) {
    const o = { id, x: a.x, direction: a.dir || 'front', animation: a.anim || 'idle', seed };
    if (a.pose) o.pose = a.pose;
    if (a.expr) o.expression = a.expr;
    const look = a.outfit || (spec && spec.outfit);
    if (look) o.outfit = look;
    const c = await scene.add(name, o);
    if (a.acc) Object.keys(a.acc).forEach(k => { if (k in c.accessories) c.setAccessory(k, a.acc[k]); });
    if (spec) root.Extras.dress(c, spec);
    wrapDepth(c, a, a.x);
    return c;
  }

  /* Coloca figurantes e elenco em ordem de profundidade */
  async function mountCast(s, i) {
    cast = {}; extras = [];
    const crowd = (s.crowd || []).map((e, n) => Object.assign({ n }, e)).sort((a, b) => (b.d || 0) - (a.d || 0));
    const addExtra = async e => {
      const spec = root.Extras.ensure(e.role, e.v === undefined ? e.n : e.v), cfg = CharacterEngine.config(spec.name);
      /* cada corpo tem suas poses: quem não tem a pedida usa a mais próxima */
      const ALT = { hands_on_head: ['worried', 'thinking', 'shrugging'], working: ['using_laptop', 'thinking', 'explaining'], worried: ['hands_on_head', 'thinking'], thinking: ['arms_crossed', 'standing'], using_phone: ['standing'], comforting: ['standing'] };
      if (e.pose && !cfg.POSES[e.pose]) e = Object.assign({}, e, { pose: (ALT[e.pose] || []).find(p => cfg.POSES[p]) || 'standing' });
      if (e.expr && !cfg.EXPRESSIONS[e.expr]) e = Object.assign({}, e, { expr: 'neutral' });
      const c = await addActor('x' + e.n, spec.name, Object.assign({}, e, { h: spec.height, girth: spec.girth }), 101 + i * 7 + e.n, spec);
      extras.push({ c, e });
    };
    for (const e of crowd.filter(x => (x.d || 0) > 0)) await addExtra(e);
    for (const name of Object.keys(s.cast || {})) cast[name] = await addActor(name, name, s.cast[name], 11 + i * 3);
    for (const e of crowd.filter(x => (x.d || 0) <= 0)) await addExtra(e);
  }

  function fire(s, t) {
    while (fired < s.beats.length && s.beats[fired][0] <= t) { s.beats[fired][1](cast, Player); fired += 1; }
  }

  async function prepare(i) {
    const s = shots[i];
    cur = s; lastT = 0; fired = 0; s.lastCut = null;
    $('fx').innerHTML = ''; $('flash').style.opacity = 0; $('vig').style.opacity = 0;
    $('barT').style.transform = $('barB').style.transform = 'scaleY(0)';
    $('world').style.transform = 'none'; $('world').style.filter = 'none'; $('card').style.transform = 'none';
    $('tela').style.transform = 'none';
    if (s.cast0) s.cast = JSON.parse(JSON.stringify(s.cast0)); else if (s.cast) s.cast0 = JSON.parse(JSON.stringify(s.cast));
    $('gfx').innerHTML = ''; $('card').innerHTML = ''; $('card').style.display = 'none';
    s.mount = null;
    const hudOn = hudAt(i, 0).on;
    if (s.card) {
      const g = s.card();
      $('card').style.display = 'block'; $('card').appendChild(g.el); s.mount = g;
      $('sim').style.display = 'none'; $('clock').style.display = 'none'; $('hud').style.display = 'none';
      $('cap').style.display = 'none';
      s.chunks = [];
      return { dur: s.dur };
    }
    $('sim').style.display = 'block';
    scene.clear();
    Array.from(scene.stage.children).forEach(n => n.remove());
    if (s.bg && scene.background !== s.bg) scene.setBackground(s.bg);
    Array.from(scene.front.querySelectorAll('[data-prop]')).forEach(n => n.remove());
    Array.from(scene.back.querySelectorAll('[data-crowd]')).forEach(n => n.remove());
    plate = s.plate ? root.Extras.silhouettes(scene.back, s.plate) : null;
    await mountCast(s, i);
    if (s.prop) EP.props[s.prop](scene.front);
    s.cast = s.cast || {};
    root.Camera.build(s);
    root.Camera.mountStamps(s);
    s.beats = (s.at || []).map(b => [typeof b[0] === 'string' ? root.Camera.when(s, b[0]) : b[0] <= 1 && !b[2] ? b[0] * s.dur : b[0], b[1]]).sort((a, b) => a[0] - b[0]);
    if (s.who && cast[s.who]) {
      const c = cast[s.who];
      s.beats.unshift([0.15, () => { c.speak(s.n, s.dur - 0.5); }]);
    }
    if (s.gfx) { const g = s.gfx(); $('gfx').appendChild(g.el); s.mount = g; }
    setMood(s.mood);
    const clockText = EP.clockFor(i, shots);
    $('clock').style.display = clockText ? 'flex' : 'none';
    if (clockText) { $('clock').children[0].textContent = clockText[0]; $('clock').children[1].textContent = clockText[1]; }
    $('hud').style.display = hudOn && !s.clean ? 'block' : 'none';
    if (s.clean) $('clock').style.display = 'none';
    buildCap(s);
    s.full = !!s.gfx && !s.bg;
    $('tela').style.visibility = s.full ? 'hidden' : 'visible';
    $('gfx').style.transform = 'none';
    scene.back.style.filter = '';
    applyCamera(s, 0);
    return { dur: s.dur };
  }

  function applyCamera(s, t) {
    const Camera = root.Camera, stress = hudAt(s.i, t).v.stress || 0, c = Camera.state(s, t, stress);
    if (s.full) Camera.applyGfx(c); else Camera.applyScene(scene, c);
    /* tomada nova: troca lugar, pose e luz no instante do corte */
    const cut = c.cut;
    if (cut !== s.lastCut) {
      s.lastCut = cut;
      if (cut.place) Object.keys(cut.place).forEach(n => {
        s.cast[n] = Object.assign({}, s.cast[n], cut.place[n]);
        const who = cast[n], a = s.cast[n];
        if (!who) return;
        if (cut.place[n].x !== undefined) { who.moveTo(a.x); who.x0 = a.x; }
        if (cut.place[n].dir) who.setDirection(cut.place[n].dir, { duration: 0 });
        setDepth(who, a);
      });
      if (cut.pose) Object.keys(cut.pose).forEach(n => cast[n] && cast[n].setPose(cut.pose[n], { duration: 0 }));
      if (cut.expr) Object.keys(cut.expr).forEach(n => cast[n] && cast[n].setExpression(cut.expr[n], { duration: 0 }));
      if (cut.mood !== undefined) setMood(cut.mood);
    }
    /* desfoque de fundo só em plano fechado */
    const dof = !s.full && c.z >= 1.45 && s.dof !== false ? Math.min(4.5, (c.z - 1.25) * 2.6) : 0;
    scene.back.style.filter = dof ? 'blur(' + dof.toFixed(1) + 'px)' : '';
    $('vig').style.opacity = clamp(0.12 + Math.pow(stress / 100, 2) * 0.62 + (s.vig || 0)).toFixed(3);
    const flick = s.flicker && Math.sin(t * 37) * Math.sin(t * 13 + 1) > 0.55 ? s.flicker : 0;
    $('grade').style.opacity = clamp(gradeBase + flick).toFixed(3);
    Camera.transition(s, t);
    Camera.effects(s, t);
  }

  function setMood(name) {
    const mood = MOOD[name || 'day'];
    $('grade').style.background = mood ? mood[0] : 'none';
    gradeBase = mood ? mood[1] : 0;
    $('grade').style.opacity = gradeBase;
    $('grade').style.mixBlendMode = name === 'dusk' || name === 'tense' ? 'normal' : 'multiply';
  }

  /* Cartão de dia: bate na tela com tranco */
  function cardFx(t) {
    const k = clamp(t / 0.3), j = (1 - k) * 20;
    $('card').style.transform = 'translate(' + (Math.sin(t * 90) * j).toFixed(1) + 'px,' + (Math.cos(t * 71) * j).toFixed(1) + 'px) scale(' + (1 + (1 - k) * (1 - k) * 0.2 + t * 0.03).toFixed(3) + ')';
  }

  function frame(t) {
    const s = cur;
    if (s.mount) s.mount.update(t, s.dur);
    if (s.card) { cardFx(t); return; }
    fire(s, t);
    const dt = (t - lastT) * 1000;
    lastT = t;
    (s.walks || []).forEach(w => {
      const k = prog(t, w.from || 0, w.dur || s.dur);
      cast[w.who].moveTo(lerp(s.cast[w.who].x, w.to, k));
    });
    extras.forEach(({ c, e }) => {
      if (e.to !== undefined) c.moveTo(lerp(e.x, e.to, prog(t, e.from || 0, e.dur || s.dur)));
    });
    if (plate) plate.update(t);
    if (dt >= 0) scene.tick(dt);
    applyCamera(s, t);
    if (!s.clean) drawHud(hudAt(s.i, t));
    drawCap(s, t);
  }

  async function boot() {
    const q = new URLSearchParams(location.search);
    showCaps = q.get('caps') !== '0';
    CharacterEngine.configure({ basePath: '../characters/' });
    scene = CharacterEngine.createScene('#tela', { autoStart: false });
    shots = EP.shots;
    const total = layout();
    await document.fonts.load('40px Anton');
    await document.fonts.load('700 40px Inter');
    await document.fonts.load('500 40px Inter');
    await document.fonts.load('800 40px Inter');
    await document.fonts.ready;
    root.playerReady = { count: shots.length, total };
  }

  root.Player = { boot, prepare, frame,
    info: () => shots.map(s => ({ i: s.i, id: s.id, dur: s.dur, start: s.start, n: s.n || '', who: s.who || '', day: s.day || '',
      bg: s.bg || '', card: !!s.card, gfx: !!s.gfx, tin: s.tin || '', tout: s.tout || '', mood: s.mood || '', hudAt: s.hud ? (s.hudAt === undefined ? 0.45 : s.hudAt) * s.dur : -1,
      hud: s.hud || null, stress: hudAt(s.i, s.dur).v.stress || 0,
      hits: (s.hits || []).map(h => ({ t: root.Camera.when(s, h.at), stamp: h.stamp || '', flash: !!h.flash, shake: h.shake || 0, punch: h.punch || 0 })) })) };
})(typeof self !== 'undefined' ? self : this);
