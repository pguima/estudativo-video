/*!
 * CharacterEngine — API única para os cinco personagens e para as cenas.
 *
 *   const dan = await CharacterEngine.load('dan', { container: '#palco' });
 *   dan.setExpression('worried');
 *   dan.setPose('standing');
 *   dan.play('talking');
 *   dan.setDirection('left');
 *   dan.setVisible(true);
 *
 *   const cena = CharacterEngine.createScene('#tela', { background: 'kitchen' });
 *   const mia = await cena.add('mia', { x: 900 });
 *
 * Vídeo quadro a quadro (determinístico):
 *   const cena = CharacterEngine.createScene(el, { autoStart: false });
 *   cena.tick(1000 / 30);
 *   const svg = cena.toSVG();
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  const R = STH.SVGRenderer;
  const { Mixer, Eyes, VISEMES } = STH.ExpressionEngine;
  const { Layers, armState } = STH.AnimationEngine;
  const { HANDS } = STH.PoseController;
  const { LipSync, fromText } = STH.LipSyncEngine;
  const { clamp, lerp, lerpDict, ease, smooth, put, element, NS, VIEWBOX, FLOOR } = R;

  const DIRECTIONS = { front: 0, right: 1, left: -1, 'three-quarter-right': 0.5, 'three-quarter-left': -0.5 };
  const registry = {};
  const pending = {};
  let basePath = 'characters/';
  let instances = 0;

  /* Um relógio só para todo mundo: personagens da cena andam no mesmo quadro. */
  const clock = {
    items: new Set(), raf: null, last: null,
    add(c) { this.items.add(c); this.start(); },
    remove(c) { this.items.delete(c); },
    start() {
      if (this.raf !== null || typeof requestAnimationFrame === 'undefined') return;
      const loop = now => {
        if (this.last !== null) { const dt = Math.min(now - this.last, 50); this.items.forEach(c => c.tick(dt)); }
        this.last = now;
        this.raf = this.items.size ? requestAnimationFrame(loop) : null;
        if (this.raf === null) this.last = null;
      };
      this.raf = requestAnimationFrame(loop);
    }
  };

  class Character {
    constructor(name, cfg, target, options) {
      const opt = Object.assign({ expression: 'neutral', pose: cfg.defaultPose || 'standing', animation: 'idle', direction: cfg.defaultDirection || 'front', seed: cfg.seed || 7, autoStart: true }, options);
      this.name = name;
      this.cfg = cfg;
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      if (!this.host) throw new Error('CharacterEngine: destino não encontrado para ' + name + '.');
      instances += 1;
      this.prefix = opt.idPrefix || (name + (instances > 1 ? '-' + instances : ''));
      this.uid = this.prefix;
      this.random = R.rng(opt.seed);
      this.time = 0;
      this.turn = this._dir(opt.direction);
      this.turnFrom = this.turn; this.turnTo = this.turn; this.turnP = 1; this.turnDur = 1;
      this.poseMix = new Mixer(this._need(opt.pose, cfg.POSES, 'pose'));
      this.exprMix = new Mixer(this._need(opt.expression, cfg.EXPRESSIONS, 'expressão'));
      this.anims = new Layers(this._anim(opt.animation));
      this.breathing = true;
      this.eyes = new Eyes(this.random);
      this.talking = 0; this.talkTarget = 0;
      this.headTilt = 0; this.headTiltTarget = 0;
      this.arms = { r: armState(), l: armState() };
      this.viseme = { name: 'rest', w: 0, on: false, dur: 80 };
      this.hairSwing = 0; this.hairVel = 0;
      this.accessories = Object.assign({ shadow: true }, cfg.accessories);
      this.visible = true; this.alpha = 1;
      this.outfit = opt.outfit || cfg.defaultOutfit || 'main';
      this.hairStyle = opt.hair || (cfg.OUTFITS && cfg.OUTFITS[this.outfit] && cfg.OUTFITS[this.outfit].hair) || 'down';
      this.lips = new LipSync(this);
      this.position = { x: 0, y: 0 };
      if (cfg.init) cfg.init.call(this);
      this._build();
      this._applyScale(this.svg);
      this.tick(0);
      this.running = false;
      if (opt.autoStart) this.resume();
    }

    /* ---------- API unificada ---------- */
    setExpression(name, o) { this.exprMix.to(this._need(name, this.cfg.EXPRESSIONS, 'expressão'), this._ms(o, 260)); return this._after(); }
    setPose(name, o) { this.poseMix.to(this._need(name, this.cfg.POSES, 'pose'), this._ms(o, 480)); return this._after(); }
    play(name, o) {
      const n = (this.cfg.ALIASES && this.cfg.ALIASES[name]) || name;
      this.anims.set(this._anim(n), this._ms(o, 300));
      return this._after();
    }
    setAnimation(name, o) { return this.play(name, o); }
    setDirection(dir, o) { return this.setTurn(this._dir(dir), o); }
    /* Giro contínuo: -1 perfil esquerdo, 0 frente, 1 perfil direito. */
    setTurn(value, o) {
      const dur = this._ms(o, 420);
      this.turnTo = clamp(value, -1, 1);
      if (dur <= 0) { this.turn = this.turnTo; this.turnP = 1; } else { this.turnFrom = this.turn; this.turnP = 0; this.turnDur = dur; }
      return this._after();
    }
    setVisible(on, o) {
      this.visible = !!on;
      if (this._ms(o, 200) <= 0) this.alpha = on ? 1 : 0;
      return this._after();
    }
    /* true liga, false desliga, 'auto' devolve a decisão à pose. */
    setAccessory(name, on) {
      if (!(name in this.accessories)) throw new Error(this.name + ': acessório desconhecido "' + name + '". Use: ' + Object.keys(this.accessories).join(', '));
      this.accessories[name] = on === 'auto' ? 'auto' : !!on;
      return this._after();
    }
    setOutfit(name, o) {
      const table = this.cfg.OUTFITS || {};
      if (!table[name]) throw new Error(this.name + ': figurino desconhecido "' + name + '". Use: ' + Object.keys(table).join(', '));
      this.outfit = name;
      this.hairStyle = (o && o.hair) || table[name].hair || this.hairStyle;
      return this._after();
    }
    setHair(style) {
      const list = this.cfg.HAIR || ['down'];
      if (!list.includes(style)) throw new Error(this.name + ': penteado desconhecido "' + style + '". Use: ' + list.join(', '));
      this.hairStyle = style;
      return this._after();
    }
    /* Controla um braço sem depender da pose; null devolve à pose. */
    setArm(side, values) {
      const k = side === 'right' ? 'r' : side === 'left' ? 'l' : null;
      if (!k) throw new Error(this.name + ': braço desconhecido "' + side + '". Use: right, left');
      if (values && values.hand && !HANDS[values.hand]) throw new Error(this.name + ': mão desconhecida "' + values.hand + '". Use: ' + Object.keys(HANDS).join(', '));
      const a = this.arms[k];
      a.on = !!values;
      if (values) a.v = Object.assign({ shoulder: 0, elbow: 0, wrist: 0 }, values);
      return this._after();
    }
    /* Boca de fala: rest, A, E, I, O, U, M, F. null devolve a boca à expressão. */
    setViseme(name, o) {
      if (name !== null && !VISEMES[name]) throw new Error(this.name + ': visema desconhecido "' + name + '". Use: ' + Object.keys(VISEMES).join(', '));
      this.viseme.on = name !== null;
      if (name !== null) this.viseme.name = name;
      this.viseme.dur = this._ms(o, 80);
      if (this.viseme.dur <= 0) this.viseme.w = name !== null ? 1 : 0;
      return this._after();
    }
    /* Fala por uma linha do tempo de visemas, ou por texto como rascunho. */
    speak(lineOrText, seconds) {
      this.lips.play(typeof lineOrText === 'string' ? fromText(lineOrText, seconds || 2) : lineOrText);
      return this;
    }
    setHeadTilt(deg) { this.headTiltTarget = clamp(deg, -20, 20); return this._after(); }
    setBreathing(on) { this.breathing = !!on; return this; }
    setBlinking(on) { this.eyes.enabled = !!on; return this; }
    setTalking(on) { this.talkTarget = on ? 1 : 0; return this; }
    lookAt(x, y) { this.eyes.look = x === undefined ? null : { x: clamp(x, -1, 1), y: clamp(y || 0, -1, 1) }; return this._after(); }
    blink() { this.eyes.blink(); return this; }
    getState() {
      return {
        name: this.name, expression: this.exprMix.name, pose: this.poseMix.name, animation: this.animation, outfit: this.outfit, hair: this.hairStyle,
        direction: Object.keys(DIRECTIONS).find(k => DIRECTIONS[k] === this.turnTo) || 'custom', turn: this.turnTo,
        visible: this.visible, accessories: Object.assign({}, this.accessories)
      };
    }
    get animation() { return this.anims.current; }
    get expressions() { return Object.keys(this.cfg.EXPRESSIONS); }
    get poses() { return Object.keys(this.cfg.POSES); }
    get animations() { return ['none'].concat(Object.keys(this.cfg.ANIMATE)); }
    resume() { this.running = true; clock.add(this); return this; }
    pause() { this.running = false; clock.remove(this); return this; }
    toSVG() {
      const clone = this.svg.cloneNode(true);
      clone.setAttribute('xmlns', NS);
      clone.removeAttribute('class');
      return new XMLSerializer().serializeToString(clone);
    }
    destroy() { this.pause(); this.svg.remove(); }

    tick(dtMs) {
      const dt = dtMs / 1000;
      this.time += dt;
      this.poseMix.update(dtMs); this.exprMix.update(dtMs);
      if (this.turnP < 1) {
        this.turnP = clamp(this.turnP + dtMs / this.turnDur);
        this.turn = lerp(this.turnFrom, this.turnTo, ease(this.turnP));
      }
      this.anims.update(dtMs);
      this.lips.update(dt);
      this.talking = lerp(this.talking, this.talkTarget, clamp(dt * 12));
      this.headTilt = lerp(this.headTilt, this.headTiltTarget, clamp(dt * 10));
      ['r', 'l'].forEach(k => { const a = this.arms[k]; a.w = clamp(a.w + (a.on ? 1 : -1) * dtMs / 260); });
      const v = this.viseme;
      if (v.dur > 0) v.w = clamp(v.w + (v.on ? 1 : -1) * dtMs / v.dur);
      this.alpha += clamp((this.visible ? 1 : 0) - this.alpha, -dtMs / 200, dtMs / 200);
      this._render(this.eyes.blinkAmount(this.time, dt), dt);
      return this;
    }

    /* ---------- Serviços usados pelos rigs ---------- */
    applyAnimations(j, st) {
      const table = this.cfg.ANIMATE;
      this.anims.list.forEach(a => { if (table[a.name]) table[a.name](j, this.time, a.w, st); });
    }
    talkWeight() { return Math.max(this.animation === 'talk' ? 1 : this.talking, this.exprMix.name === 'talking' ? 1 : 0); }
    mouthFlap() {
      const w = this.talkWeight();
      if (w < 0.01) return 0;
      const t = this.time;
      return Math.abs(Math.sin(t * 13.1) * 0.6 + Math.sin(t * 7.3 + 1) * 0.4) * w;
    }
    faceFrame() {
      let e = this.exprMix.sample(n => this.cfg.EXPRESSIONS[n]);
      if (this.viseme.w > 0) e = lerpDict(e, Object.assign({}, e, VISEMES[this.viseme.name]), ease(this.viseme.w));
      return e;
    }
    _n(tag, attrs, parent, part, pivot) {
      const el = element(tag, attrs, parent);
      if (part) { el.setAttribute('data-part', part); el.setAttribute('id', this.prefix + '-' + part); }
      if (pivot) el.setAttribute('data-pivot', pivot.join(','));
      return el;
    }
    _applyScale(svg) {
      const s = this.cfg.scale || 1;
      const g = element('g', { transform: 'translate(0 ' + FLOOR + ') scale(' + s + ') translate(0 ' + -FLOOR + ')' });
      g.setAttribute('data-part', 'proportion');
      Array.from(svg.childNodes).forEach(n => { if (n.nodeName !== 'defs') g.appendChild(n); });
      svg.appendChild(g);
    }
    _need(name, table, label) {
      if (!table[name]) throw new Error(this.name + ': ' + label + ' desconhecida "' + name + '". Use: ' + Object.keys(table).join(', '));
      return name;
    }
    _anim(name) {
      if (name !== 'none' && !this.cfg.ANIMATE[name]) throw new Error(this.name + ': animação desconhecida "' + name + '". Use: none, ' + Object.keys(this.cfg.ANIMATE).join(', '));
      return name;
    }
    _dir(dir) {
      if (!(dir in DIRECTIONS)) throw new Error(this.name + ': direção desconhecida "' + dir + '". Use: ' + Object.keys(DIRECTIONS).join(', '));
      return DIRECTIONS[dir];
    }
    _ms(o, fallback) { return o && o.duration !== undefined ? o.duration : fallback; }
    _after() { if (!this.running) this.tick(0); return this; }
  }

  /* Uma classe por personagem, feita de Character + rig + partes próprias. */
  function classFor(name) {
    const cfg = registry[name];
    if (cfg.Class) return cfg.Class;
    const rig = STH.Rigs[cfg.rig](cfg);
    class Made extends Character {}
    Object.assign(Made.prototype, rig, cfg.methods ? cfg.methods(cfg) : {});
    cfg.Class = Made;
    return Made;
  }

  function loadConfig(name) {
    if (registry[name]) return Promise.resolve(registry[name]);
    if (pending[name]) return pending[name];
    pending[name] = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = basePath + name + '/config.js';
      s.onload = () => (registry[name] ? resolve(registry[name]) : reject(new Error('CharacterEngine: ' + name + ' não se registrou.')));
      s.onerror = () => reject(new Error('CharacterEngine: não encontrei ' + s.src));
      document.head.appendChild(s);
    });
    return pending[name];
  }

  /* ---------- Cenas: personagens e cenário em um único SVG ---------- */
  const SCENE_W = 1920, SCENE_H = 1080, SCENE_FLOOR = 948, UNIT = 0.86;
  class Scene {
    constructor(target, options) {
      const opt = Object.assign({ background: null, autoStart: true, floor: SCENE_FLOOR }, options);
      this.host = typeof target === 'string' ? document.querySelector(target) : target;
      this.opt = opt;
      this.svg = element('svg', { viewBox: '0 0 ' + SCENE_W + ' ' + SCENE_H, class: 'sth-scene', preserveAspectRatio: 'xMidYMid meet' }, this.host);
      this.back = element('g', {}, this.svg);
      this.stage = element('g', {}, this.svg);
      this.front = element('g', {}, this.svg);
      this.cast = {};
      if (opt.background) this.setBackground(opt.background);
    }
    setBackground(name) {
      [this.back, this.front].forEach(g => { while (g.firstChild) g.removeChild(g.firstChild); });
      this.background = name;
      if (name) STH.Backdrops.draw(name, this.back, this.front);
      return this;
    }
    /* x = centro do personagem em pixels da cena (0 a 1920). */
    async add(name, o) {
      const opt = Object.assign({ x: SCENE_W / 2, id: name }, o);
      await loadConfig(name);
      const Made = classFor(name);
      const w = 850 * UNIT, h = 860 * UNIT;
      const slot = element('svg', { x: opt.x - w / 2, y: this.opt.floor - 820 * UNIT, width: w, height: h, overflow: 'visible' }, this.stage);
      const c = new Made(name, registry[name], slot, Object.assign({ autoStart: this.opt.autoStart, idPrefix: 'scene-' + opt.id }, opt));
      c.slot = slot;
      c.moveTo = function (x) { slot.setAttribute('x', x - w / 2); return this; };
      this.cast[opt.id] = c;
      return c;
    }
    remove(id) { const c = this.cast[id]; if (c) { c.destroy(); c.slot.remove(); delete this.cast[id]; } return this; }
    clear() { Object.keys(this.cast).forEach(id => this.remove(id)); return this; }
    tick(dt) { Object.values(this.cast).forEach(c => c.tick(dt)); return this; }
    toSVG() {
      const clone = this.svg.cloneNode(true);
      clone.setAttribute('xmlns', NS);
      clone.removeAttribute('class');
      return new XMLSerializer().serializeToString(clone);
    }
    destroy() { this.clear(); this.svg.remove(); }
  }

  const CharacterEngine = {
    register(name, build) { registry[name] = build(STH); return this; },
    configure(o) { if (o.basePath) basePath = o.basePath; return this; },
    /* Sem container, o personagem nasce em um elemento próprio dentro do <body>. */
    async load(name, options) {
      await loadConfig(name);
      const opt = Object.assign({}, options);
      let target = opt.container;
      if (!target) { target = document.createElement('div'); target.className = 'sth-character'; document.body.appendChild(target); }
      const Made = classFor(name);
      return new Made(name, registry[name], target, opt);
    },
    /* O model.svg estático, para conferência; a animação vem do rig. */
    loadModel(name) { return R.loadSVG(basePath + name + '/model.svg'); },
    createScene(target, options) { return new Scene(target, options); },
    list() { return Object.keys(registry); },
    config(name) { return registry[name]; },
    SCENE: { width: SCENE_W, height: SCENE_H, floor: SCENE_FLOOR },
    DIRECTIONS: Object.keys(DIRECTIONS),
    VIEWBOX, smooth
  };

  root.CharacterEngine = STH.CharacterEngine = CharacterEngine;
  STH.Rigs = STH.Rigs || {};
})(typeof self !== 'undefined' ? self : this);
