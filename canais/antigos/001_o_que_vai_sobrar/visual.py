"""Animação completa do piloto "O Que Vai Sobrar de Nós Daqui a 10.000 Anos?" (21 cenas, ~10 min).
Tempos: audio/tempos.json (cenas e cues casados com as palavras da narração). Peças: _ferramentas/antigos.py.
Cenas 01 e 02 vêm do teste_abertura.py. Cada cena é uma função sNN(c, t, q, tg):
t = tempo local da cena, q = cues (tempo local), tg = tempo global (para a boca da Lume e animações contínuas).

python visual.py --preview 03 5.0 [06 20 ...]   → saida/prev_<cena>_<t>.png
python visual.py --render [--partes 4]           → saida/piloto_mudo.mp4 (em paralelo)
VIDEO_LANG=en python visual.py ...               → versão em inglês (audio_en/, saida_en/, roteiro/textos_en.py)
"""
import sys, json, math, random, wave, subprocess
from pathlib import Path
import numpy as np
import skia
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
sys.path.insert(0, str(AQUI.parent / "visual"))
sys.path.insert(0, str(AQUI))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals())  # VIDEO_LANG=en: textos da tela em inglês, audio_en/ e saida_en/
from antigos import *  # noqa: E402,F403
from antigos import _meia_lua  # noqa: E402
from estudo import mundo, CENTRAL  # noqa: E402
import teste_abertura as abre  # noqa: E402

TEMPOS = json.loads((lingua.audio(AQUI) / "tempos.json").read_text())
CENAS = TEMPOS["scenes"]
TOTAL = TEMPOS["total"]
TR = 0.45  # transição (dissolve) entre cenas


def _env():
    with wave.open(str(lingua.audio(AQUI) / "narracao.wav")) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)
    hop = sr // FPS
    n = len(x) // hop
    rms = np.sqrt((x[: n * hop].reshape(n, hop) ** 2).mean(1) + 1e-9)
    rms = np.clip(rms / np.percentile(rms, 95) * 1.1 - 0.12, 0, 1)
    return np.convolve(rms, [0.25, 0.5, 0.25], mode="same")


ENV = _env()


def fala(tg):
    i = int(tg * FPS)
    return float(ENV[i]) * 0.85 if 0 <= i < len(ENV) else 0.0


def L(c, x, y, s, tg, **kw):
    """a Lume viva, falando com a narração"""
    lume(c, x, y, s, lume_viva(tg, kw, fala(tg)))


def blend(c, a, fa, fb):
    """dissolve entre duas partes da cena (a: 0 = só fa, 1 = só fb)"""
    a = clamp(a)
    if a < 1:
        fa()
    if a > 0:
        if a < 1:
            c.saveLayerAlpha(None, int(255 * a))
        fb()
        if a < 1:
            c.restore()


def fase(t, t0, d=0.5):
    return ease_io(prog(t, t0 - d / 2, d))


def chao(c, y=1000, cor="#4a52b8"):
    c.drawRect(skia.Rect.MakeLTRB(0, y, W, H), paint(cor))
    c.drawRect(skia.Rect.MakeLTRB(0, y, W, y + 8), paint("#8a93ff"))


def ceu(c, a="#7ec8ff", b="#ffd9e8"):
    fundo(c, a, b)


def nuvens(c, t, y=180, a=0.9, seed=2):
    rnd = random.Random(seed)
    for k in range(6):
        x = (rnd.uniform(0, W) + t * rnd.uniform(6, 16)) % (W + 400) - 200
        yy = y + rnd.uniform(-60, 60)
        s = rnd.uniform(0.7, 1.3)
        for dx, dy, r in ((0, 0, 50), (50, -18, 40), (95, 2, 44), (-45, 8, 34)):
            c.drawCircle(x + dx * s, yy + dy * s, r * s, paint("#ffffff", a))


# =====================================================================
# 03 · ESTRANHAMENTO: 8 bilhões e a balança
# =====================================================================
def _ceu_de_coisas(c, t, t0, seed=5):
    if t < t0:
        return
    rnd = random.Random(seed)
    nomes = ["carro", "celular", "garrafa", "predio", "carro", "garrafa", "celular"]
    n = int(min(46, (t - t0) * 10))
    for i in range(n):
        x, y = rnd.uniform(80, W - 80), rnd.uniform(70, 330)
        icone(c, nomes[i % len(nomes)], x, y + 6 * math.sin(t * 2 + i), 0.55, FESTA[i % 5], prog(t, t0 + i / 10, 0.4))


def _balanca(c, t, q):
    fundo(c, "#ff8fb1", "#ffc56b")
    k = ease_io(prog(t, q["c"], q["d"] - q["c"]))
    ang = lerp(0.20, 0.0, k) + 0.012 * math.sin(t * 3) * (1 - prog(t, q["d"], 1.0))
    cx, cy, L_ = 960, 520, 820
    # pé e base
    c.drawPath(poly([(cx - 30, cy), (cx + 30, cy), (cx + 70, 940), (cx - 70, 940)]), paint("#2e47c9"))
    c.drawRRect(rr(cx - 220, 930, 440, 30, 12), paint("#1f3196"))
    ex, ey = math.cos(ang) * L_ / 2, math.sin(ang) * L_ / 2
    pts = [(cx - ex, cy - ey), (cx + ex, cy + ey)]
    c.drawLine(*pts[0], *pts[1], paint("#2e47c9", stroke=22))
    c.drawCircle(cx, cy, 26, paint(AMBER))
    n_hum = int(lerp(1, 9, k))
    for lado, (px, py) in enumerate(pts):
        c.drawLine(px, py, px - 110, py + 170, paint(INK, 0.6, stroke=3))
        c.drawLine(px, py, px + 110, py + 170, paint(INK, 0.6, stroke=3))
        c.drawPath(poly([(px - 150, py + 170), (px + 150, py + 170), (px + 110, py + 205), (px - 110, py + 205)]),
                   paint("#ffffff"))
        if lado == 0:  # o que os humanos fabricaram
            nomes = ["predio", "carro", "celular", "garrafa", "predio", "carro", "predio", "celular", "carro"]
            for i in range(n_hum):
                ix, iy = px - 100 + (i % 4) * 66, py + 140 - (i // 4) * 62
                icone(c, nomes[i], ix, iy, 0.62, FESTA[i % 5], 1.0)
            rotulo(c, "PRÉDIOS · ESTRADAS · MÁQUINAS", px, py + 250, "#2e47c9", ep(t, q["c"] + 1.5, 0.4), size=24)
        else:  # tudo o que é vivo
            for i, nm in enumerate(["arvore", "arvore", "pessoa", "frango", "arvore", "pessoa", "arvore", "frango"]):
                ix, iy = px - 100 + (i % 4) * 66, py + 140 - (i // 4) * 62
                icone(c, nm, ix, iy, 0.62, FESTA[i % 5], 1.0)
            rotulo(c, "TODOS OS SERES VIVOS", px, py + 250, "#17a99a", ep(t, q["c"] + 1.5, 0.4), size=24)
    ano = int(lerp(1900, 2020, k))
    titulo(c, str(ano), cx, 190, 120 if t < q["d"] else 150, "#ffffff" if t < q["d"] else AMBER, 1.0)
    rotulo(c, "PESO IGUAL", cx, 300, CYAN, ep(t, q["d"] + 0.4, 0.4), size=36)
    fonte(c, "Elhacham et al., Nature, 2020", ep(t, q["c"], 0.5))


def s03(c, t, q, tg):
    def cidade():
        cidade_quente(c, tg)
        chao(c)
        _ceu_de_coisas(c, t, q["b"])
        titulo(c, "8 BILHÕES", W / 2, 170, 120, AMBER, prog(t, q["a"] + 2.8, 0.6))
        L(c, 300, 1030, 1.4, tg, look=(0.7, -0.6), brow=0.6, arm_r=1.4 * ep(t, 3.0, 0.4))
    blend(c, fase(t, q["c"], 0.8), cidade, lambda: _balanca(c, t, q))


# =====================================================================
# 04 · ARQUIVOS DIGITAIS QUE SE PERDEM
# =====================================================================
def _estante(c, t, q):
    fundo(c, "#ffb3c8", "#ffd99a")
    c.drawRRect(rr(330, 200, 1260, 700, 18), paint("#8a4b2f"))
    for k in range(3):
        y = 300 + k * 220
        c.drawRect(skia.Rect.MakeLTRB(350, y - 80, 1570, y + 110), paint("#b7683f"))
        c.drawRect(skia.Rect.MakeLTRB(350, y + 110, 1570, y + 128), paint("#6a3520"))
    tipos = ["foto", "carta", "livro", "musica"]
    rnd = random.Random(3)
    itens = []
    for k in range(3):
        for i in range(8):
            itens.append((430 + i * 150 + rnd.uniform(-10, 10), 330 + k * 220, tipos[(i + k) % 4], k * 8 + i))
    for x, y, tp, i in itens:
        a_in = prog(t, q["a"] + 0.3 + i * 0.05, 0.4)
        vira = prog(t, q["c"] + 0.2 + i * 0.03, 0.4)        # vira arquivo digital
        some = prog(t, q["c"] + 2.0 + i * 0.22, 0.5)        # perde-se
        if some >= 1:
            continue
        if vira < 1:
            icone(c, tp, x, y, 0.95, FESTA[i % 5], a_in * (1 - vira))
        if vira > 0:
            nm = "duvida" if some > 0.3 else "arquivo"
            icone(c, nm, x, y, 0.9, FESTA[i % 5] if nm == "duvida" else SKY, vira * (1 - some))
    for k, nome in enumerate(["FOTOS", "CARTAS", "LIVROS", "MÚSICAS"]):
        rotulo(c, nome, 520 + k * 290, 150, FESTA[k], ep(t, q["b"] + 2.0 + k * 0.6, 0.35) * (1 - prog(t, q["c"], 0.4)), size=30)
    rotulo(c, "A CADA TROCA DE MÁQUINA, UM POUCO SE PERDE", W / 2, 990, CORAL, ep(t, q["c"] + 2.5, 0.4), size=30)


def _citacao(c, t, q):
    fundo(c, "#1d2f8f", "#111b5c")
    estrelas(c, t, 9, 60, 0.4)
    text(c, "“", 300, 420, 260, "display", 800, AMBER, ep(t, q["d"], 0.4))
    titulo(c, "uma idade das", W / 2, 470, 96, BONE, prog(t, q["d"] + 3.0, 0.5))
    titulo(c, "trevas digital", W / 2, 590, 110, AMBER, prog(t, q["d"] + 3.4, 0.5))
    a = ep(t, q["d"] + 0.3, 0.5)
    text(c, "— VINT CERF, UM DOS CRIADORES DA INTERNET · 2015", W / 2, 720, 26, "mono", 500, DUST, a, "center", tracking=0.08)
    fonte(c, "NPR, 13/02/2015", a)


def terminal(c, x, y, t, msg="ARQUIVO ILEGÍVEL", a=1.0):
    c.drawRRect(rr(x - 140, y - 20, 280, 220, 14), paint("#2c45b8"))
    c.drawRRect(rr(x - 160, y - 210, 320, 200, 16), paint("#0c1550"))
    c.drawRRect(rr(x - 145, y - 195, 290, 170, 10), paint("#070c38"))
    pis = 0.75 + 0.25 * (math.sin(t * 9) > -0.6)
    text(c, msg, x, y - 100, 26, "mono", 500, CORAL, a * pis, "center")
    for k in range(4):
        c.drawRect(skia.Rect.MakeXYWH(x - 120 + k * 64, y - 70, 40, 6), paint(CORAL, 0.35 * a))
    glow(c, x, y - 110, 200, CORAL, 0.18 * a)


def _museu_chao(c, t, q, tg):
    c.save()
    camera(c, 960, 560, 1.15)
    mundo(c, tg, dict(titulo_a=0.0))
    terminal(c, 1360, 880, tg)
    p = ep(t, q["e"] + 3.6, 0.5)
    L(c, 1120, 900, 1.3, tg, face=1, look=(lerp(0.8, 0.2, p), lerp(-0.2, 0.9, p)), arm_r=lerp(1.6, 0.6, p), brow=0.4)
    c.restore()
    rotulo(c, "PELO QUE FICA NO CHÃO", W / 2, 140, AMBER, ep(t, q["e"] + 4.0, 0.4), size=40)


def s04(c, t, q, tg):
    if t < q["e"] - 0.3:
        blend(c, fase(t, q["d"], 0.7), lambda: _estante(c, t, q), lambda: _citacao(c, t, q))
    else:
        blend(c, fase(t, q["e"], 0.6), lambda: _citacao(c, t, q), lambda: _museu_chao(c, t, q, tg))


# =====================================================================
# 05 · ATRAVESSAR O VIDRO E AVANÇAR O RELÓGIO
# =====================================================================
def s05(c, t, q, tg):
    if t < 1.15:  # entra na vitrine
        z = lerp(1.15, 9.0, ease_io(prog(t, 0, 1.15)) ** 1.6)
        c.save()
        camera(c, 960, lerp(560, 480, prog(t, 0, 1.15)), z)
        mundo(c, tg, dict(titulo_a=0.0))
        c.restore()
    else:
        cidade_quente(c, tg, luzes=0.12, transito=0.0, cinza=0.35)
        chao(c)
        # dia e noite passando cada vez mais rápido
        if t > q["c"]:
            v = (t - q["c"]) * (3 + 6 * prog(t, q["c"], 3))
            c.drawRect(skia.Rect.MakeWH(W, H), paint("#0a1240", 0.35 * (0.5 + 0.5 * math.sin(v * 3))))
        vel = prog(t, q["b"], 4)
        ang = (t - q["b"]) * (1 + 40 * vel ** 2) if t > q["b"] else 0
        relogio(c, W / 2, 330, 170, ang, ep(t, q["b"], 0.5), vel, t)
        for k, (cue, s_) in enumerate((("c", "CEM ANOS"), ("d", "MIL ANOS"), ("e", "DEZ MIL ANOS"))):
            prox = ["d", "e", None][k]
            a = prog(t, q[cue], 0.35) * (1 - (prog(t, q[prox], 0.2) if prox else 0))
            titulo(c, s_, W / 2, 620, 110, AMBER, a)
        L(c, 300, 1030, 1.3, tg, look=(0.6, -0.8), brow=0.7, o_mouth=t > q["e"], mouth=0.6 if t > q["e"] else 0)
    flash = 1 - abs(t - 1.15) / 0.3
    if flash > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#ffffff", flash))


# =====================================================================
# 06 · CEM ANOS: metrô, concreto armado, Roma
# =====================================================================
def _tunel(c, t, q):
    camadas(c, 0, 0, W, H, ["#3a63e0", "#d9844a", "#c8673a", "#a94f2e", "#8f3f28"], seed=4, alturas=[2.4, 1, 1.2, 1.4, 1.6])
    # rua e prédios em cima
    c.drawRect(skia.Rect.MakeLTRB(0, 300, W, 330), paint("#26307e"))
    rnd = random.Random(8)
    x = 0
    while x < W:
        bw, bh = rnd.uniform(90, 160), rnd.uniform(80, 240)
        c.drawRect(skia.Rect.MakeLTRB(x, 300 - bh, x + bw - 10, 300), paint(rnd.choice(RECON["predios"])))
        x += bw
    # túnel
    tun = skia.Path()
    tun.moveTo(300, 920)
    tun.lineTo(300, 600)
    tun.arcTo(skia.Rect.MakeLTRB(300, 420, 1620, 780), 180, 180, False)
    tun.lineTo(1620, 920)
    tun.close()
    c.drawPath(tun, paint("#1c2a7a"))
    c.save()
    c.clipPath(tun, doAntiAlias=True)
    for k in range(10):
        c.drawLine(300 + k * 140, 480, 300 + k * 140, 920, paint("#26368f", stroke=4))
    c.drawRect(skia.Rect.MakeLTRB(300, 880, 1620, 920), paint("#3a3f9a"))
    for xr in (700, 1220):
        c.drawRect(skia.Rect.MakeLTRB(xr - 120, 866, xr + 120, 874), paint("#9fb4ff"))
    # gotas vazando pelas paredes
    for k in range(14):
        ph = (t * 0.9 + k * 0.37) % 1.0
        gx = 340 + (k * 97) % 1240
        c.drawCircle(gx, 520 + ph * 360, 6, paint(SKY, 0.9 * (1 - ph)))
    # bombas
    para = prog(t, q["a0"] + 9.0, 0.6)
    for bx in (420, 1500):
        c.drawRRect(rr(bx - 60, 780, 120, 100, 12), paint("#3a52c4"))
        c.save()
        c.translate(bx, 830)
        c.rotate((t * 400) * (1 - para) + 400 * q["a0"] * 0)
        for k in range(3):
            c.rotate(120)
            c.drawOval(oval(0, -18, 9, 18), paint(AMBER))
        c.restore()
        icone(c, "xis", bx, 760, 0.7, None, ep(t, q["a0"] + 9.0, 0.3))
    # água subindo depois que as bombas param
    nivel = lerp(915, 640, ease_io(prog(t, q["a0"] + 9.5, q["a"] - q["a0"] - 9.5)))
    agua = skia.Rect.MakeLTRB(300, nivel + 6 * math.sin(t * 2), 1620, 930)
    c.drawRect(agua, paint(SKY, 0.65))
    c.drawRect(skia.Rect.MakeLTRB(300, agua.top(), 1620, agua.top() + 6), paint("#ffffff", 0.6))
    c.restore()
    c.drawPath(tun, paint("#0c1550", stroke=10))
    rotulo(c, "METRÔ DE NOVA YORK", W / 2, 400, CORAL, ep(t, q["a0"] + 1.4, 0.4), size=34)
    rotulo(c, "~50 MILHÕES DE LITROS POR DIA", W / 2, 990, SKY, ep(t, q["a0"] + 4.5, 0.4), size=36)
    fonte(c, "MTA · NY1, jul/2026", ep(t, q["a0"] + 4.5, 0.4))


def _pilar(c, t, q):
    fundo(c, "#7ec8ff", "#c9d6ff")
    x0, x1, y0, y1 = 640, 1280, 140, 1000
    racha = prog(t, q["b"] + 1.2, 2.0)
    ferr = ease_io(prog(t, q["b"] + 3.0, q["c"] - q["b"]))
    quebra = ease_out(prog(t, q["c"] + 5.0, 1.6))
    rnd = random.Random(2)
    # pedaços do concreto (voam quando quebra)
    pedacos = [(x0, y0, 960, 560), (960, y0, x1, 560), (x0, 560, 960, y1), (960, 560, x1, y1)]
    for k, (a0, b0, a1, b1) in enumerate(pedacos):
        dx = (-1 if a0 < 960 else 1) * 110 * quebra
        dy = (-1 if b0 < 560 else 1) * 50 * quebra
        c.save()
        c.translate(dx, dy)
        c.rotate((-1) ** k * 4 * quebra, (a0 + a1) / 2, (b0 + b1) / 2)
        c.drawRect(skia.Rect.MakeLTRB(a0, b0, a1, b1), paint("#cfd3e6"))
        rr_ = random.Random(k)
        for _ in range(40):
            c.drawCircle(rr_.uniform(a0 + 8, a1 - 8), rr_.uniform(b0 + 8, b1 - 8), rr_.uniform(3, 9), paint("#a9b0cc"))
        c.restore()
    # barras de aço (incham com a ferrugem)
    for bx in (740, 880, 1040, 1180):
        w = 26 * (1 + 0.9 * ferr)
        cor = mix("#7d8bb0", "#e0742c", ferr)
        c.drawRRect(rr(bx - w / 2, y0 + 30, w, y1 - y0 - 60, w / 2), paint(cor))
        if ferr > 0.1:
            for k in range(8):
                yy = y0 + 80 + k * 100
                c.drawCircle(bx + rnd.uniform(-w / 3, w / 3), yy, w * 0.35, paint("#b9531c", 0.8 * ferr))
    # rachadura e água entrando
    if racha > 0:
        pts = [(x1, 240), (1180, 300), (1120, 290), (1040, 380), (980, 360), (900, 470), (860, 600), (780, 700)]
        n = max(2, int(len(pts) * racha))
        c.drawPath(poly(pts[:n], close=False), paint("#2a2f5a", stroke=6))
        for k in range(6):
            ph = (t * 0.8 + k / 6) % 1
            i = int(ph * (n - 1))
            if i < n - 1:
                (ax, ay), (bx2, by2) = pts[i], pts[i + 1]
                f = ph * (n - 1) - i
                c.drawCircle(lerp(ax, bx2, f), lerp(ay, by2, f), 7, paint(SKY))
    # trincas saindo das barras
    if ferr > 0.5:
        for bx in (740, 880, 1040, 1180):
            for k in range(4):
                yy = y0 + 150 + k * 200
                ln = 70 * (ferr - 0.5) * 2
                c.drawLine(bx, yy, bx + (ln if k % 2 else -ln), yy - ln * 0.6, paint("#2a2f5a", stroke=4))
    rotulo(c, "CONCRETO ARMADO", W / 2, 80, "#2e47c9", ep(t, q["a"] + 2.0, 0.4), size=36)
    rotulo(c, "BARRAS DE AÇO", 380, 560, "#7d8bb0", ep(t, q["b"] + 0.3, 0.4) * (1 - ferr), size=30)
    rotulo(c, "FERRUGEM OCUPA MAIS ESPAÇO", 360, 700, CORAL, ep(t, q["c"] + 0.4, 0.4), size=30)


def _desaba(c, t, q):
    fundo(c, "#ffb38a", "#ffe0b0")
    c.drawCircle(1500, 300, 90, paint("#fff6d6"))
    rnd = random.Random(4)
    for k in range(10):
        x = 100 + k * 175
        bw, bh = rnd.uniform(110, 150), rnd.uniform(300, 560)
        t0 = q["d"] + 0.3 + k * 0.35
        u = ease_io(prog(t, t0, 1.6))
        cor = mix(rnd.choice(RECON["predios"]), "#8a8fb0", 0.55)
        c.save()
        c.translate(x + bw / 2, 900)
        c.rotate((1 if k % 2 else -1) * 14 * u)
        c.translate(0, bh * 0.55 * u)
        c.drawRect(skia.Rect.MakeLTRB(-bw / 2, -bh, bw / 2, 0), paint(cor))
        for yy in range(int(-bh + 20), -10, 30):
            for xx in range(int(-bw / 2 + 14), int(bw / 2 - 20), 26):
                c.drawRect(skia.Rect.MakeXYWH(xx, yy, 12, 16), paint("#3a3f6a", 0.6))
        c.restore()
        if 0 < u < 1:
            for j in range(5):
                c.drawCircle(x + bw / 2 + rnd.uniform(-80, 80), 900 - rnd.uniform(0, 60) - 80 * u, 30 + 40 * u,
                             paint("#e9d7c8", 0.55 * (1 - u)))
    c.drawRect(skia.Rect.MakeLTRB(0, 900, W, H), paint("#b98a6a"))
    for k in range(18):
        c.drawCircle(60 + k * 110, 905, rnd.uniform(20, 40), paint("#9a7458"))
    rotulo(c, "PONTES · VIADUTOS · ARRANHA-CÉUS", W / 2, 120, "#2e47c9", ep(t, q["d"] + 0.3, 0.4), size=34)


def templo(c, cx, base, s=1.0, cor="#fff1d6"):
    c.save()
    c.translate(cx, base)
    c.scale(s, s)
    c.drawPath(_meia_lua(0, -330, 230), paint(mix(cor, "#c9a77a", 0.25)))
    c.drawRect(skia.Rect.MakeLTRB(-300, -60, 300, 0), paint(mix(cor, "#c9a77a", 0.3)))
    for k in range(8):
        x = -270 + k * 77
        c.drawRect(skia.Rect.MakeLTRB(x - 18, -300, x + 18, -60), paint(cor))
        c.drawRect(skia.Rect.MakeLTRB(x - 10, -300, x - 4, -60), paint("#ffffff", 0.5))
    c.drawRect(skia.Rect.MakeLTRB(-310, -330, 310, -300), paint(cor))
    c.drawPath(poly([(-320, -330), (320, -330), (0, -450)]), paint(mix(cor, "#c9a77a", 0.15)))
    c.restore()


def _roma(c, t, q, tg):
    ceu(c, "#7ec8ff", "#ffe6b0")
    nuvens(c, t, 160)
    c.drawRect(skia.Rect.MakeLTRB(0, 860, W, H), paint("#6ec26e"))
    templo(c, 1180, 880, 1.15)
    rnd = random.Random(7)
    for k in range(7):  # entulho com mato
        x = 120 + k * 90
        c.drawCircle(x, 880, rnd.uniform(40, 80), paint("#9aa0b8"))
        arvore(c, x + 20, 870, 0.7, "#3fd17a", 1.0)
    L(c, 600, 1000, 1.3, tg, look=(0.9, -0.6), brow=0.7, smile=0.9)
    rotulo(c, "~2.000 ANOS DE PÉ", 1180, 260, AMBER, ep(t, q["e"] + 3.5, 0.4), size=38)
    rotulo(c, "CONCRETO SEM AÇO POR DENTRO", 1180, 340, CYAN, ep(t, q["e"] + 2.0, 0.4), size=30)
    fonte(c, "Ex.: Panteão de Roma, c. 125 d.C.", ep(t, q["e"] + 2.0, 0.4))


def s06(c, t, q, tg):
    if t < q["a"] + 0.4:
        blend(c, fase(t, q["a"], 0.7), lambda: _tunel(c, t, q), lambda: _pilar(c, t, q))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.7), lambda: _pilar(c, t, q), lambda: _desaba(c, t, q))
    else:
        blend(c, fase(t, q["e"], 0.7), lambda: _desaba(c, t, q), lambda: _roma(c, t, q, tg))
    titulo(c, "100 ANOS", 200, 90, 48, "#ffffff", 1.0 if t > 0.3 else prog(t, 0, 0.3), align="left")


# =====================================================================
# 07 · MIL ANOS: morros, Svalbard, o que foi jogado fora
# =====================================================================
def morros(c, t, verde=1.0, y0=600):
    cores = ["#8fe39a", "#3fd17a", "#27b066", "#1f8f55"]
    rnd = random.Random(3)
    for k, cor in enumerate(cores):
        base = y0 + k * 110
        p = skia.Path()
        p.moveTo(0, H)
        for i in range(0, W + 120, 120):
            p.lineTo(i, base - 90 * math.sin(i / 300 + k * 1.7) - 40 * math.sin(i / 120 + k))
        p.lineTo(W, H)
        p.close()
        c.drawPath(p, paint(cor))
        for j in range(9):
            x = rnd.uniform(0, W)
            yy = base - 90 * math.sin(x / 300 + k * 1.7) - 40 * math.sin(x / 120 + k) + 12
            if rnd.random() < 0.25:
                c.drawRect(skia.Rect.MakeLTRB(x - 14, yy - 60, x + 14, yy + 10), paint("#9aa0b8"))
            arvore(c, x, yy + 6, 0.6 + 0.2 * k, mix(cor, "#ffffff", 0.1), verde)


def _morros(c, t, q, tg):
    ceu(c, "#62b8ff", "#d6f0ff")
    nuvens(c, t, 170)
    morros(c, t, ep(t, 0.2, 1.5))
    titulo(c, "1.000 ANOS", W / 2, 200, 120, AMBER, prog(t, q["a"] + 0.2, 0.5))
    rotulo(c, "AS CIDADES VIRARAM MORROS COM MATO", W / 2, 300, "#17a99a", ep(t, q["a"] + 1.4, 0.4), size=30)


def _svalbard(c, t, q, tg):
    fundo(c, "#13206b", "#3a63e0")
    estrelas(c, t, 6, 90, 0.6, (0, 0, W, 500))
    for k, cor in enumerate(["#3ee6c8", "#ff7eb6"]):  # aurora
        p = skia.Path()
        p.moveTo(0, 220 + k * 60)
        for i in range(0, W + 60, 60):
            p.lineTo(i, 220 + k * 60 + 50 * math.sin(i / 200 + t * 0.6 + k))
        c.drawPath(p, paint(cor, 0.45, stroke=40, blur=18))
    c.drawPath(poly([(200, H), (760, 380), (1000, 470), (1240, 330), (1800, H)]), paint("#e8f0ff"))
    c.drawPath(poly([(760, 380), (860, 470), (700, 520)]), paint("#c3d2ff"))
    c.drawRRect(rr(900, 760, 170, 200, 16), paint("#26307e"))
    glow(c, 985, 860, 160, AMBER, 0.6)
    c.drawRect(skia.Rect.MakeLTRB(910, 770, 1060, 960), paint(AMBER, 0.35))
    rotulo(c, "SVALBARD · ÁRTICO", 985, 690, SKY, ep(t, q["c"] + 0.4, 0.4), size=32)


def _filmes(c, t, q, tg):
    fundo(c, "#26307e", "#13206b")
    for k in range(3):
        y = 330 + k * 230
        c.drawRect(skia.Rect.MakeLTRB(300, y + 70, 1620, y + 86), paint("#9fb4ff"))
        for i in range(8):
            icone(c, "filme", 380 + i * 165, y + 20, 1.2, None, prog(t, q["c"] + 3.0 + (k * 8 + i) * 0.03, 0.35))
    rotulo(c, "DADOS GRAVADOS EM FILME FOTOGRÁFICO", W / 2, 150, CYAN, ep(t, q["c"] + 3.4, 0.4), size=34)
    rotulo(c, "PROJETADO PARA ~1.000 ANOS", W / 2, 1000, AMBER, ep(t, q["c"] + 4.5, 0.4), size=36)
    fonte(c, "Arctic World Archive (Piql)", ep(t, q["c"] + 4.5, 0.4))


def _descer(c, t, q, tg):
    y = -380 * ease_io(prog(t, q["d"] + 0.5, q["e"] - q["d"]))
    c.save()
    c.translate(0, y)
    ceu(c, "#62b8ff", "#d6f0ff")
    c.drawRect(skia.Rect.MakeLTRB(0, 520, W, 560), paint("#3fd17a"))
    camadas(c, 0, 560, W, H + 420, ["#c8673a", "#a94f2e", "#8f3f28", "#6b3442"], seed=9)
    # bolsão de lixo
    k = ep(t, q["e"], 0.6)
    rnd = random.Random(1)
    lixo = skia.Path()
    lixo.addOval(oval(W / 2, 1150, 620 * k + 1, 200 * k + 1))
    c.drawPath(lixo, paint("#5a2f45"))
    c.save()
    c.clipPath(lixo, doAntiAlias=True)
    for _ in range(260):
        c.drawRect(skia.Rect.MakeXYWH(rnd.uniform(300, 1620), rnd.uniform(950, 1350), rnd.uniform(14, 40), rnd.uniform(8, 24)),
                   paint(rnd.choice(FESTA + ["#ffffff"])))
    c.restore()
    L(c, 520, 530, 1.1, tg, look=(0.3, 1.0), brow=0.5, arm_r=0.9)
    c.restore()
    rotulo(c, "O QUE ELES JOGARAM FORA", W / 2, 1010, CORAL, ep(t, q["e"] + 0.4, 0.4), size=40)


def s07(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.7), lambda: _morros(c, t, q, tg), lambda: _svalbard(c, t, q, tg))
    elif t < q["c"] + 3.4:
        blend(c, fase(t, q["c"] + 3.0, 0.7), lambda: _svalbard(c, t, q, tg), lambda: _filmes(c, t, q, tg))
    else:
        blend(c, fase(t, q["d"], 0.7), lambda: _filmes(c, t, q, tg), lambda: _descer(c, t, q, tg))


# =====================================================================
# 08 · O ATERRO (Garbage Project)
# =====================================================================
def _aterro_corte(c, t, q, tg, aperto=0.0):
    ceu(c, "#7ec8ff", "#ffe0f0")
    nuvens(c, t, 120)
    topo = 380
    morro = skia.Path()
    morro.moveTo(0, 620)
    morro.cubicTo(400, topo, 1500, topo, W, 620)
    morro.lineTo(W, H)
    morro.lineTo(0, H)
    morro.close()
    c.drawPath(morro, paint("#3fd17a"))
    c.save()
    c.clipPath(morro, doAntiAlias=True)
    c.translate(0, H)
    c.scale(1, 1 - 0.12 * aperto)
    c.translate(0, -H)
    sobe = ease_out(prog(t, q["a"], 2.5))
    rnd = random.Random(12)
    y = H
    k = 0
    while y > topo + 30:
        h = 70 if k % 2 == 0 else 26
        yy = y - h
        if yy < lerp(H, topo, sobe):
            break
        if k % 2 == 0:  # camada de lixo
            c.drawRect(skia.Rect.MakeLTRB(0, yy, W, y), paint("#6b3442"))
            for _ in range(70):
                c.drawRect(skia.Rect.MakeXYWH(rnd.uniform(0, W), rnd.uniform(yy + 4, y - 14), rnd.uniform(12, 34), rnd.uniform(6, 14)),
                           paint(rnd.choice(FESTA + ["#ffffff", "#9fb4ff"])))
        else:  # terra por cima
            c.drawRect(skia.Rect.MakeLTRB(0, yy, W, y), paint("#a94f2e"))
        y = yy
        k += 1
    c.restore()
    c.drawPath(morro, paint("#2e9a5a", stroke=10))


def _escavadores(c, t, q, tg):
    _aterro_corte(c, t, q, tg)
    a = ep(t, q["b"], 0.6)
    # sonda perfurando
    fx = 960
    prof = 380 + 420 * ease_io(prog(t, q["b"] + 1.0, 6))
    c.drawRect(skia.Rect.MakeLTRB(fx - 60, 250, fx + 60, 270), paint("#2e47c9", a))
    c.drawPath(poly([(fx - 60, 270), (fx - 20, 430), (fx + 20, 430), (fx + 60, 270)], close=False), paint("#2e47c9", a, stroke=8))
    c.drawRect(skia.Rect.MakeLTRB(fx - 10, 260, fx + 10, prof), paint("#c9d0ff", a))
    for yy in range(270, int(prof), 26):
        off = (t * 120) % 26
        c.drawLine(fx - 10, yy + off, fx + 10, yy + off - 8, paint("#7d8bb0", a, stroke=3))
    pessoa(c, 760, 440, 1.0, AMBER, PELE[0], capacete="#ffd84a", braco=1.2, a=a, olhar=1)
    pessoa(c, 1170, 440, 1.0, CORAL, PELE[2], capacete="#ffd84a", braco=0.5, a=a, olhar=-1)
    rotulo(c, "WILLIAM RATHJE", 760, 170, CORAL, ep(t, q["b"] + 1.5, 0.4), size=30)
    rotulo(c, "UNIVERSIDADE DO ARIZONA · ANOS 1980", 1180, 170, "#2e47c9", ep(t, q["b"] + 3.0, 0.4), size=26)
    fonte(c, "Garbage Project · Univ. do Arizona", ep(t, q["b"] + 1.5, 0.4))


def jornal(c, cx, cy, s=1.0, a=1.0):
    c.save()
    c.translate(cx, cy)
    c.scale(s * pop(a), s * pop(a))
    c.rotate(-4)
    c.drawRect(skia.Rect.MakeLTRB(-260, -330, 266, 344), paint(INK, 0.3))
    c.drawRect(skia.Rect.MakeLTRB(-270, -340, 260, 330), paint("#f3e2b8"))
    c.drawRect(skia.Rect.MakeLTRB(-240, -310, 230, -250), paint("#3a2c18"))
    c.drawRect(skia.Rect.MakeLTRB(-240, -230, 230, -224), paint("#3a2c18"))
    rnd = random.Random(2)
    for col in range(3):
        for k in range(18):
            w = rnd.uniform(80, 140)
            c.drawRect(skia.Rect.MakeXYWH(-240 + col * 160, -200 + k * 26, w, 9), paint("#5a4a30", 0.75))
    c.drawRect(skia.Rect.MakeLTRB(-80, -200, 70, -60), paint("#c9b48a"))
    c.drawPath(poly([(160, 330), (260, 230), (260, 330)]), paint("#e2c98f"))
    c.restore()


def cachorro_quente(c, cx, cy, s=1.0, a=1.0):
    c.save()
    c.translate(cx, cy)
    c.scale(s * pop(a), s * pop(a))
    c.drawRRect(rr(-250, -30, 500, 110, 55), paint("#e0a35a"))
    c.drawRRect(rr(-270, -60, 540, 70, 35), paint(CORAL))
    p = skia.Path()
    p.moveTo(-220, -30)
    for k in range(12):
        p.lineTo(-220 + k * 40 + 20, -50 if k % 2 == 0 else -20)
    c.drawPath(p, paint(AMBER, stroke=10))
    c.drawRRect(rr(-250, 0, 500, 100, 50), paint("#f0b86a"))
    c.drawOval(oval(-120, 50, 60, 12), paint("#ffffff", 0.25))
    c.restore()


def _achados(c, t, q, tg):
    fundo(c, "#ffd99a", "#ffb3c8")
    if t < q["d"] - 0.2:
        jornal(c, W / 2, 560, 1.0, prog(t, q["c"], 0.5))
        rotulo(c, "JORNAIS DE DÉCADAS ANTES: AINDA DÁ PARA LER", W / 2, 990, "#2e47c9", ep(t, q["c"] + 1.2, 0.4), size=32)
    else:
        cachorro_quente(c, W / 2, 520, 1.1, prog(t, q["d"], 0.5))
        rotulo(c, "~15 ANOS ENTERRADO", W / 2, 260, CORAL, ep(t, q["d"] + 1.6, 0.4), size=40)
        rotulo(c, "AINDA COM CARA DE CACHORRO-QUENTE", W / 2, 780, "#2e47c9", ep(t, q["d"] + 3.5, 0.4), size=32)
        L(c, 1650, 1020, 1.1, tg, face=-1, look=(0.9, -0.4), o_mouth=True, mouth=0.7, brow_y=1.0)


def _aperto(c, t, q, tg):
    _aterro_corte(c, t, q, tg, ease_io(prog(t, q["e"] + 0.3, 1.5)))
    rotulo(c, "SECO E APERTADO", W / 2, 160, AMBER, ep(t, q["e"] + 0.5, 0.4), size=40)
    rotulo(c, "QUASE NADA APODRECE", W / 2, 250, CORAL, ep(t, q["e"] + 2.0, 0.4), size=34)


def s08(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lambda: (_aterro_corte(c, t, q, tg),
                                               rotulo(c, "ATERRO", W / 2, 200, CORAL, ep(t, q["a"] + 1.2, 0.4), size=48)),
              lambda: _escavadores(c, t, q, tg))
    elif t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _escavadores(c, t, q, tg), lambda: _achados(c, t, q, tg))
    else:
        blend(c, fase(t, q["e"], 0.6), lambda: _achados(c, t, q, tg), lambda: _aperto(c, t, q, tg))


# =====================================================================
# 09 · CACOS DE CERÂMICA
# =====================================================================
def caco(c, x, y, s, cor="#d9844a", ang=0, seed=0):
    rnd = random.Random(seed)
    pts = [(math.cos(k * 2.1 + rnd.uniform(0, 0.6)) * rnd.uniform(18, 34), math.sin(k * 2.1 + rnd.uniform(0, 0.6)) * rnd.uniform(14, 28))
           for k in range(5)]
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(s, s)
    c.drawPath(poly(pts), paint(cor))
    c.drawPath(poly(pts), paint(mix(cor, INK, 0.3), stroke=2))
    c.drawLine(-14, -4, 10, -8, paint("#ffffff", 0.35, stroke=3))
    c.restore()


def _escavacao(c, t, q, tg):
    fundo(c, "#c8673a", "#8f3f28")
    c.drawRect(skia.Rect.MakeLTRB(0, 0, W, 170), paint("#3fd17a"))
    for k in range(5):
        c.drawLine(360 + k * 300, 170, 360 + k * 300, H, paint("#ffffff", 0.5, stroke=2))
    for k in range(3):
        c.drawLine(0, 420 + k * 230, W, 420 + k * 230, paint("#ffffff", 0.5, stroke=2))
    rnd = random.Random(4)
    for i in range(28):
        caco(c, rnd.uniform(150, W - 150), rnd.uniform(260, 1020), 1.6 * pop(prog(t, q["b"] + i * 0.05, 0.4)),
             rnd.choice(["#d9844a", "#e8a36a", "#c4693a", "#ffffff"]), rnd.uniform(0, 360), i)
    rotulo(c, "O ACHADO MAIS COMUM", W / 2, 90, "#2e47c9", ep(t, q["a"] + 2.5, 0.4), size=34)
    rotulo(c, "CACOS DE CERÂMICA", W / 2, 560, AMBER, ep(t, q["b"] + 0.3, 0.4), size=56)


def _compara(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    cols = [("MADEIRA", "APODRECE", "xis"), ("METAL", "ENFERRUJA", "xis"), ("BARRO COZIDO", "FICA", "check")]
    quebra = ep(t, q["c"] + 5.0, 0.6)
    for k, (nome, verbo, ok) in enumerate(cols):
        x = 420 + k * 540
        a = ep(t, q["c"] + k * 1.2, 0.4)
        c.drawRRect(rr(x - 220, 220, 440, 640, 30), paint("#ffffff", 0.75 * a))
        if k == 0:
            c.drawRRect(rr(x - 140, 420, 280, 100, 50), paint("#a0643a", a))
            c.drawCircle(x + 140, 470, 50, paint("#c88a5a", a))
            for j in range(4):
                c.drawCircle(x - 80 + j * 50, 470, 8, paint("#5a3a20", a * prog(t, q["c"] + 1, 1)))
        elif k == 1:
            c.drawRRect(rr(x - 150, 440, 300, 60, 10), paint(mix("#9fb4ff", "#e0742c", prog(t, q["c"] + 2, 1.5)), a))
        else:
            if quebra < 1:
                vaso = poly([(x - 70, 380), (x + 70, 380), (x + 100, 470), (x + 60, 560), (x - 60, 560), (x - 100, 470)])
                c.save()
                c.translate(0, 0)
                c.drawPath(vaso, paint("#d9844a", a * (1 - quebra)))
                c.restore()
            if quebra > 0:
                for j in range(6):
                    caco(c, x - 80 + j * 32, lerp(470, 600, quebra) + (j % 2) * 20, 1.3, "#d9844a", j * 50, j)
        text(c, nome, x, 700, 38, "display", 800, INK, a, "center")
        icone(c, ok, x, 790, 0.9, None, ep(t, q["c"] + k * 1.2 + 0.6, 0.3))
        text(c, verbo, x, 300, 30, "mono", 500, "#2e47c9", a, "center")
    rotulo(c, "POTE QUEBRADO VAI DIRETO PARA O LIXO", W / 2, 960, CORAL, ep(t, q["c"] + 5.4, 0.4), size=32)


def _lab(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    c.drawRRect(rr(160, 620, 1600, 60, 12), paint("#4a66e0"))
    c.drawRect(skia.Rect.MakeLTRB(160, 680, 1760, 720), paint("#2c45b8"))
    for k, (nm, rot) in enumerate((("xicara", "XÍCARA"), ("azulejo", "AZULEJO"), ("privada", "PRIVADA"))):
        x = 480 + k * 480
        a = prog(t, q["d"] + 2.2 + k * 1.0, 0.4)
        glow(c, x, 500, 200, AMBER, 0.3 * a)
        icone(c, nm, x, 500, 2.0, AMBER, a)
        c.drawLine(x - 40, 420, x + 30, 580, paint("#1f3196", a, stroke=6))
        rotulo(c, rot, x, 780, FESTA[k], ep(t, q["d"] + 2.4 + k * 1.0, 0.3), size=34)
    titulo(c, "DAQUI A 10.000 ANOS", W / 2, 200, 64, BONE, prog(t, q["d"] + 0.3, 0.5))


def _privadas(c, t, q, tg):
    fundo(c, "#ffb3c8", "#ffd99a")
    n = int(min(60, (t - q["e"]) * 22))
    for i in range(n):
        x, y = 140 + (i % 12) * 150, 170 + (i // 12) * 190
        icone(c, "privada", x, y, 1.05, None, prog(t, q["e"] + i / 22, 0.3))
    L(c, 330, 1060, 1.5, tg, lid=0.45, smile=1.0, brow_y=0.5, cheek=0.8, squash=0.05 * math.sin(tg * 14))
    titulo(c, "MUITAS, MUITAS PRIVADAS", 1150, 1010, 64, "#2e47c9", prog(t, q["e"] + 0.5, 0.5))


def s09(c, t, q, tg):
    if t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _escavacao(c, t, q, tg), lambda: _compara(c, t, q, tg))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _compara(c, t, q, tg), lambda: _lab(c, t, q, tg))
    else:
        blend(c, fase(t, q["e"], 0.5), lambda: _lab(c, t, q, tg), lambda: _privadas(c, t, q, tg))


# =====================================================================
# 10 · DEZ MIL ANOS: o monte Rushmore
# =====================================================================
def rosto(c, x, y, s, cor):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    c.drawOval(oval(0, 0, 70, 100), paint(mix(cor, "#ffffff", 0.12)))
    c.drawOval(oval(-26, -20, 16, 8), paint(mix(cor, INK, 0.35)))
    c.drawOval(oval(26, -20, 16, 8), paint(mix(cor, INK, 0.35)))
    c.drawLine(-44, -40, -10, -36, paint(mix(cor, INK, 0.3), stroke=6))
    c.drawLine(10, -36, 44, -40, paint(mix(cor, INK, 0.3), stroke=6))
    c.drawPath(poly([(0, -24), (12, 22), (-8, 24)]), paint(mix(cor, INK, 0.25)))
    c.drawLine(-22, 50, 22, 50, paint(mix(cor, INK, 0.35), stroke=6))
    c.drawOval(oval(30, 10, 30, 70), paint(INK, 0.12))
    c.restore()


def _rushmore(c, t, q, tg):
    ceu(c, "#62b8ff", "#ffe0f0")
    nuvens(c, t, 140)
    rocha_ = "#a7a2c8"
    c.drawPath(poly([(240, H), (420, 330), (700, 220), (1100, 200), (1450, 300), (1700, H)]), paint(rocha_))
    c.drawPath(poly([(1100, 200), (1450, 300), (1700, H), (1300, H)]), paint(mix(rocha_, INK, 0.15)))
    for k in range(4):
        rosto(c, 640 + k * 200, 470 + (k % 2) * 30, 1.05, rocha_)
    rnd = random.Random(5)
    cresce = ep(t, q["b"], 4)
    for k in range(40):
        x = rnd.uniform(0, W)
        arvore(c, x, H - rnd.uniform(0, 160), rnd.uniform(1.2, 2.0), rnd.choice(["#27b066", "#3fd17a", "#1f8f55"]),
               prog(cresce, k / 40, 0.2))
    # folhas caindo
    for k in range(12):
        ph = (t * 0.15 + k / 12) % 1
        c.drawOval(oval(300 + (k * 137) % 1300 + 40 * math.sin(t + k), 150 + ph * 900, 9, 5), paint("#3fd17a", 0.9 * (1 - ph)))
    rotulo(c, "MONTE RUSHMORE · EUA", 960, 120, "#2e47c9", ep(t, q["b"] + 0.5, 0.4), size=34)
    # régua
    a = ep(t, q["c"], 0.5)
    if a > 0:
        c.drawRRect(rr(1640, 300, 90, 500, 10), paint(AMBER, a))
        for k in range(21):
            c.drawLine(1640, 310 + k * 24, 1640 + (40 if k % 5 == 0 else 22), 310 + k * 24, paint(INK, a, stroke=3))
        c.drawRect(skia.Rect.MakeLTRB(1640, 310, 1730, 334), paint(CORAL, a))
        rotulo(c, "≈ 2,5 cm A CADA 10.000 ANOS", 1380, 880, CORAL, ep(t, q["c"] + 1.0, 0.4), size=34)
        fonte(c, "Serviço Nacional de Parques dos EUA", a)
    L(c, 260, 1060, 1.2, tg, look=(0.8, -0.9), brow=0.5, smile=0.5)


def s10(c, t, q, tg):
    def rel():
        fundo(c, "#1d2f8f", "#111b5c")
        estrelas(c, t, 3, 80, 0.5)
        relogio(c, W / 2, 470, 230, t * 9, 1.0, 1.0, t)
        titulo(c, "10.000 ANOS", W / 2, 880, 120, AMBER, prog(t, q["a"] + 0.2, 0.5))
    blend(c, fase(t, q["b"], 0.7), rel, lambda: _rushmore(c, t, q, tg))


# =====================================================================
# 11 · PLÁSTICO E PLASTIGLOMERADO
# =====================================================================
def _montanha(c, t, q, tg):
    fundo(c, "#7ec8ff", "#ffe0f0")
    h = lerp(40, 560, ease_out(prog(t, q["a"] + 0.5, 6)))
    rnd = random.Random(11)
    base = 980
    for i in range(int(h * 0.9)):
        u = rnd.random()
        x = W / 2 + (rnd.random() * 2 - 1) * (700 * (1 - u * 0.7))
        y = base - h * u * (1 - abs(x - W / 2) / 900) - 10
        nm = rnd.choice(["garrafa", "garrafa", "celular", "garrafa"])
        icone(c, nm, x, y, 0.45, rnd.choice(FESTA + ["#9fe3ff"]), 1.0)
    c.drawRect(skia.Rect.MakeLTRB(0, base, W, H), paint("#4a52b8"))
    titulo(c, "8,3 BILHÕES DE TONELADAS", W / 2, 160, 84, "#2e47c9", prog(t, q["a"] + 3.2, 0.5))
    rotulo(c, "DE PLÁSTICO, ATÉ 2015", W / 2, 250, CORAL, ep(t, q["a"] + 4.2, 0.4), size=34)
    fonte(c, "Geyer, Jambeck & Law, Science Advances, 2017", ep(t, q["a"] + 3.2, 0.4))


def _pizza(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    k = ease_out(prog(t, q["b"] + 0.3, 1.6))
    fatias = [(0.79, CORAL, "79% ATERROS E NATUREZA"), (0.12, AMBER, "12% QUEIMADO"), (0.09, CYAN, "9% RECICLADO")]
    ang = -90
    cx, cy, r = 700, 560, 300
    for i, (f, cor, nome) in enumerate(fatias):
        sw = 360 * f * k
        p = skia.Path()
        p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), ang, sw, False)
        p.close()
        c.drawPath(p, paint(cor))
        ang += 360 * f * k
        rotulo(c, nome, 1380, 400 + i * 130, cor, ep(t, q["b"] + 1.0 + i * 0.5, 0.4), size=36)
    c.drawCircle(cx, cy, r * 0.5, paint("#1a2a85"))
    titulo(c, "DO LIXO DE PLÁSTICO", W / 2, 140, 56, BONE, prog(t, q["b"], 0.5))


def _quebra(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    u = prog(t, q["c"] + 1.5, 4)
    rnd = random.Random(1)
    n = int(1 + 60 * u ** 1.5)
    s = lerp(3.0, 0.35, u ** 0.7)
    for i in range(n):
        ang = rnd.uniform(0, 2 * math.pi)
        d = rnd.uniform(0, 520) * u
        caco(c, W / 2 + math.cos(ang) * d, 540 + math.sin(ang) * d * 0.6, s, rnd.choice(["#9fe3ff", CORAL, "#3a7bd5", AMBER]),
             rnd.uniform(0, 360), i)
    rotulo(c, "SÓ SE QUEBRA EM PEDAÇOS CADA VEZ MENORES", W / 2, 980, "#2e47c9", ep(t, q["c"] + 2.0, 0.4), size=32)
    titulo(c, "VIRA PEDRA", W / 2, 180, 110, CORAL, prog(t, q["d"] + 0.2, 0.5))


def fogueira(c, x, y, t, s=1.0):
    for k in range(3):
        c.drawRRect(rr(x - 70 * s + k * 10, y - 10 * s - k * 6, 140 * s, 18 * s, 9), paint("#8a4b2f"))
    for k, (cor, r) in enumerate(((CORAL, 60), (AMBER, 42), ("#fff1a8", 24))):
        h = r * (1.6 + 0.2 * math.sin(t * 9 + k))
        c.drawPath(poly([(x - r * s, y - 10), (x + r * s, y - 10), (x + 6 * math.sin(t * 7 + k), y - 10 - h * s)]), paint(cor))
    glow(c, x, y - 60 * s, 220 * s, AMBER, 0.5)


def plastiglomerado(c, x, y, s=1.0, a=1.0):
    c.save()
    c.translate(x, y)
    c.scale(s * pop(a), s * pop(a))
    p = poly([(-120, -40), (-60, -90), (40, -86), (120, -40), (110, 50), (20, 80), (-90, 66), (-130, 20)])
    c.drawPath(p, paint("#4a3f5a"))
    c.save()
    c.clipPath(p, doAntiAlias=True)
    rnd = random.Random(3)
    for _ in range(30):
        c.drawOval(oval(rnd.uniform(-120, 120), rnd.uniform(-90, 80), rnd.uniform(8, 26), rnd.uniform(5, 14)),
                   paint(rnd.choice([CORAL, SKY, AMBER, CYAN, "#ffffff", "#e8d6bf"])))
    c.drawOval(oval(-30, -60, 70, 24), paint("#ffffff", 0.18))
    c.restore()
    c.drawPath(p, paint("#2a2238", stroke=4))
    c.restore()


def _praia(c, t, q, tg):
    ceu(c, "#62b8ff", "#ffd9e8")
    c.drawRect(skia.Rect.MakeLTRB(0, 520, W, 640), paint("#17a99a"))
    for k in range(6):
        c.drawLine(0, 540 + k * 18, W, 540 + k * 18 + 6 * math.sin(t + k), paint("#ffffff", 0.25, stroke=3))
    c.drawRect(skia.Rect.MakeLTRB(0, 630, W, H), paint("#f2c98a"))
    rnd = random.Random(6)
    for _ in range(30):
        c.drawCircle(rnd.uniform(0, W), rnd.uniform(680, 1060), rnd.uniform(4, 9), paint("#ffffff", 0.7))
    for x in (150, 1600, 1780):
        c.drawOval(oval(x, 760, 90, 50), paint("#2a2238"))
    fogueira(c, 980, 800, t)
    derr = prog(t, q["e"] + 3.0, 4)
    if t < q["f"]:
        icone(c, "garrafa", 980, 700 + 30 * derr, 1.2 * (1 - 0.6 * derr), "#9fe3ff", 1 - derr * 0.7)
    plastiglomerado(c, 980, 880, 1.3, prog(t, q["f"] - 0.2, 0.6))
    rotulo(c, "PRAIA DO HAVAÍ · 2014", W / 2, 140, "#2e47c9", ep(t, q["e"] + 1.2, 0.4), size=34)
    for k, s_ in enumerate(["PLÁSTICO DERRETIDO", "AREIA", "CONCHAS", "LAVA"]):
        rotulo(c, s_, 380 + k * 390, 250, FESTA[k], ep(t, q["e"] + 3.6 + k * 0.6, 0.3) * (1 - prog(t, q["f"], 0.3)), size=28)
    rotulo(c, "PLASTIGLOMERADO", W / 2, 260, CORAL, ep(t, q["f"] + 0.2, 0.4), size=52)
    fonte(c, "Corcoran, Moore & Jazvac, GSA Today, 2014", ep(t, q["f"], 0.4))
    L(c, 420, 1040, 1.3, tg, look=(0.9, -0.2), brow=0.6, arm_r=1.2 * ep(t, q["f"], 0.5))


def _afunda(c, t, q, tg):
    fundo(c, "#17a99a", "#0f6e70")
    lim = camadas(c, 0, 380, W, H, ["#f2c98a", "#e0b070", "#c8945a", "#a87448", "#8a5a38"], seed=3)
    y = lerp(330, 900, ease_io(prog(t, q["g"] + 1.0, 5)))
    plastiglomerado(c, W / 2, y, 1.0, 1.0)
    rotulo(c, "MAIS PESADO", 420, 200, AMBER, ep(t, q["g"] + 0.2, 0.3), size=34)
    rotulo(c, "AFUNDA", W / 2, 200, SKY, ep(t, q["g"] + 2.0, 0.3), size=34)
    rotulo(c, "VIRA REGISTRO DAS ROCHAS", 1480, 200, CORAL, ep(t, q["g"] + 3.4, 0.3), size=34)


def s11(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lambda: _montanha(c, t, q, tg), lambda: _pizza(c, t, q, tg))
    elif t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _pizza(c, t, q, tg), lambda: _quebra(c, t, q, tg))
    elif t < q["e"] + 0.4:
        blend(c, fase(t, q["e"], 0.6), lambda: _quebra(c, t, q, tg), lambda: _praia(c, t, q, tg))
    else:
        blend(c, fase(t, q["g"], 0.6), lambda: _praia(c, t, q, tg), lambda: _afunda(c, t, q, tg))


# =====================================================================
# 12 · A ERA DO FRANGO
# =====================================================================
def robo(c, x, y, s, t, a=1.0):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    c.drawRRect(rr(-40, -16, 80, 20, 10), paint("#3a52c4", a))
    c.drawRRect(rr(-34, -90, 68, 74, 14), paint("#e8ecff", a))
    c.drawRRect(rr(-24, -78, 48, 26, 8), paint("#1f3196", a))
    c.drawCircle(-10, -65, 5, paint(CYAN, a))
    c.drawCircle(10, -65, 5, paint(CYAN, a))
    c.save()
    c.translate(34, -50)
    c.rotate(30 + 20 * math.sin(t * 5))
    c.drawRRect(rr(-4, 0, 8, 50, 4), paint("#9fb4ff", a))
    c.drawRect(skia.Rect.MakeLTRB(-10, 46, 10, 58), paint(AMBER, a))
    c.restore()
    c.restore()


def _museu12(c, t, q, tg):
    c.save()
    camera(c, 800, 620, 1.35)
    mundo(c, tg, dict(titulo_a=0.0))
    L(c, 640, 880, 1.3, tg, look=(0.2, 0.0), brow=0.9, brow_y=0.7, arm_r=1.5)
    c.restore()


def _escava12(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    camadas(c, 0, 360, W, H, ["#c8673a", "#e88d4c", "#a94f2e", "#dc7a4a", "#8f3f28"], seed=5)
    rnd = random.Random(9)
    for i in range(40):
        icone(c, "osso", rnd.uniform(120, W - 120), rnd.uniform(470, 1040), rnd.uniform(0.6, 1.0), None,
              prog(t, q["b"] + 1.0 + i * 0.06, 0.3))
    for k, x in enumerate((420, 1500)):
        robo(c, x, 360, 1.3, t + k)
    titulo(c, "10.000 ANOS NO FUTURO", W / 2, 180, 60, BONE, prog(t, q["b"], 0.5))
    if t > q["c"] - 0.2:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.6 * ep(t, q["c"] - 0.2, 0.4)))
        glow(c, W / 2, 560, 360, AMBER, 0.5 * ep(t, q["c"], 0.4))
        icone(c, "osso", W / 2, 560, 4.0, None, prog(t, q["c"] - 0.1, 0.5))
        rotulo(c, "OSSO DE FRANGO", W / 2, 830, AMBER, ep(t, q["c"] + 0.5, 0.4), size=52)


def esqueleto_frango(c, x, y, s, a=1.0, cor=BONE):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    p = paint(cor, a, stroke=10)
    c.drawOval(oval(0, 0, 90, 60), paint(cor, a, stroke=10))
    for k in range(5):
        c.drawLine(-60 + k * 30, -40, -55 + k * 30, 40, paint(cor, a, stroke=7))
    c.drawLine(70, -30, 110, -90, p)
    c.drawCircle(120, -110, 26, paint(cor, a, stroke=9))
    c.drawPath(poly([(144, -112), (172, -104), (144, -96)]), paint(cor, a))
    for lx in (-20, 30):
        c.drawLine(lx, 55, lx - 6, 130, p)
        c.drawLine(lx - 6, 130, lx + 20, 160, p)
    c.drawLine(-90, -10, -140, -40, p)
    c.restore()


def _compara12(c, t, q, tg):
    fundo(c, "#ffd99a", "#ffb3c8")
    if t < q["e"] + 0.3:
        sai = 1 - prog(t, q["e"] - 0.2, 0.4)
        glow(c, W / 2, 560, 320, AMBER, 0.4 * sai)
        icone(c, "frango", W / 2, 560, 5.0 * (0.3 + 0.7 * sai), None, prog(t, q["d"] + 0.2, 0.5) * sai)
        rotulo(c, "UM ANIMAL NOVO", W / 2, 900, CORAL, ep(t, q["d"] + 4.0, 0.4) * sai, size=44)
    a1 = ep(t, q["e"], 0.5)
    a2 = ep(t, q["e"] + 1.0, 0.5)
    esqueleto_frango(c, 520, 620, 1.0, a1, "#2e47c9")
    esqueleto_frango(c, 1260, 560, 2.0, a2, CORAL)
    rotulo(c, "IDADE MÉDIA", 520, 880, "#2e47c9", a1, size=32)
    rotulo(c, "FRANGO DOS ANTIGOS", 1260, 930, CORAL, a2, size=32)
    rotulo(c, "PELO MENOS 2× MAIOR", 1260, 180, AMBER, ep(t, q["e"] + 2.0, 0.4), size=40)
    rotulo(c, "2018 · PESQUISADORES BRITÂNICOS", W / 2, 90, "#17a99a", ep(t, q["d"] + 0.3, 0.4), size=30)
    fonte(c, "Bennett et al., Royal Society Open Science, 2018", ep(t, q["d"], 0.4))


def _bilhoes(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    n = int(min(120, (t - q["f"]) * 60))
    for i in range(n):
        icone(c, "frango", 110 + (i % 15) * 122, 330 + (i // 15) * 92, 0.8, None, prog(t, q["f"] + i / 60, 0.25))
    titulo(c, "≈ 23 BILHÕES", W / 2, 170, 110, AMBER, prog(t, q["f"] + 0.3, 0.5))
    rotulo(c, "VIVOS AO MESMO TEMPO", W / 2, 260, CORAL, ep(t, q["f"] + 1.2, 0.4), size=34)
    if t > q["g"]:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.55 * ep(t, q["g"], 0.4)))
        carimbo(c, "A ERA DO FRANGO", W / 2, 560, AMBER, prog(t, q["g"] + 1.2, 0.8), size=96)
        L(c, 1680, 1060, 1.2, tg, face=-1, brow=1.0, brow_y=0.9, look=(0.6, -0.4), smile=0.3)
    fonte(c, "Univ. de Leicester, 2018 (comunicado)", ep(t, q["f"], 0.4))


def s12(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lambda: _museu12(c, t, q, tg), lambda: _escava12(c, t, q, tg))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _escava12(c, t, q, tg), lambda: _compara12(c, t, q, tg))
    else:
        blend(c, fase(t, q["f"], 0.6), lambda: _compara12(c, t, q, tg), lambda: _bilhoes(c, t, q, tg))


# =====================================================================
# 13 · PLUTÔNIO E O ANTROPOCENO
# =====================================================================
def cogumelo(c, x, y, s, a):
    if a <= 0:
        return
    k = ease_out(clamp(a))
    c.save()
    c.translate(x, y)
    c.scale(s * k, s * k)
    c.drawRect(skia.Rect.MakeLTRB(-8, -50, 8, 0), paint("#ffd59a", 1 - 0.5 * clamp(a - 1)))
    for dx, r in ((-22, 22), (0, 30), (22, 22)):
        c.drawCircle(dx, -60, r, paint(AMBER, 1 - 0.5 * clamp(a - 1)))
    c.restore()


def _lago_corte(c, t, q, tg, brilho=1.0):
    ceu(c, "#7ec8ff", "#d6f0ff")
    c.drawRect(skia.Rect.MakeLTRB(0, 300, W, 330), paint("#3fd17a"))
    c.drawRect(skia.Rect.MakeLTRB(0, 330, W, 560), paint("#3a9be0"))
    lim = camadas(c, 0, 560, W, H, ["#c8945a", "#a87448", "#8a5a38", "#6b3442"], seed=8)
    y = 700
    a = ep(t, q["c"] + 1.5, 1.5)
    c.drawRect(skia.Rect.MakeLTRB(0, y, W, y + 14), paint(AMBER, a))
    c.drawRect(skia.Rect.MakeLTRB(0, y - 10, W, y + 24), paint(AMBER, 0.35 * a * brilho, blur=10))
    return a


def _globo13(c, t, q, tg):
    fundo(c, "#111b5c", "#070c38")
    estrelas(c, t, 2, 140, 0.7)
    globo(c, W / 2, 560, 330, t * 8)
    for k, (dx, dy) in enumerate(((-150, -120), (90, -230), (200, 60), (-60, 180), (-250, 40), (40, 20))):
        cogumelo(c, W / 2 + dx, 560 + dy, 1.0, prog(t, q["b"] + 0.8 + k * 0.5, 1.2))
    rnd = random.Random(2)
    sp = prog(t, q["b"] + 3.0, 4)
    for i in range(int(160 * sp)):
        ang = rnd.uniform(0, 2 * math.pi) + t * 0.3
        r = 360 + rnd.uniform(0, 70)
        c.drawCircle(W / 2 + math.cos(ang) * r, 560 + math.sin(ang) * r * 0.9, 3.5, paint(AMBER, 0.8))
    rotulo(c, "ANOS 1950 · TESTES DE BOMBAS ATÔMICAS", W / 2, 120, CORAL, ep(t, q["b"] + 0.5, 0.4), size=34)
    rotulo(c, "PLUTÔNIO NO PLANETA INTEIRO", W / 2, 1000, AMBER, ep(t, q["b"] + 3.5, 0.4), size=34)
    fonte(c, "Hancock et al., 2014 · Bulletin of the Atomic Scientists", ep(t, q["b"] + 3.5, 0.4))


def _chuva(c, t, q, tg):
    _lago_corte(c, t, q, tg)
    for k in range(60):
        ph = (t * 1.4 + k / 60) % 1
        x = (k * 61) % W
        c.drawLine(x, ph * 560, x - 6, ph * 560 + 24, paint(AMBER if k % 3 == 0 else "#ffffff", 0.8, stroke=3))
    rotulo(c, "UMA CAMADA FINA, NO MUNDO TODO", W / 2, 150, "#2e47c9", ep(t, q["c"] + 2.0, 0.4), size=34)


def _meia_vida(c, t, q, tg):
    _lago_corte(c, t, q, tg, 0.6 + 0.4 * math.sin(t * 4))
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.5))
    titulo(c, "PLUTÔNIO-239", W / 2, 260, 80, AMBER, prog(t, q["d"] + 0.2, 0.5))
    k = ease_io(prog(t, q["d"] + 1.0, 3))
    c.drawRRect(rr(460, 380, 1000, 70, 35), paint("#1f3196"))
    c.drawRRect(rr(460, 380, 1000 * (1 - 0.5 * k), 70, 35), paint(AMBER))
    rotulo(c, "METADE DA RADIOATIVIDADE EM ~24.100 ANOS", W / 2, 540, CORAL, ep(t, q["d"] + 2.5, 0.4), size=34)
    rotulo(c, "10.000 ANOS DEPOIS: CONTINUA LÁ", W / 2, 900, CYAN, ep(t, q["e"], 0.4), size=40)


def _crawford(c, t, q, tg):
    fundo(c, "#3fd17a", "#27b066")
    rnd = random.Random(4)
    for _ in range(60):
        arvore(c, rnd.uniform(0, W), rnd.uniform(100, H), 0.9, rnd.choice(["#1f8f55", "#27b066", "#8fe39a"]))
    c.drawOval(oval(W / 2, 560, 360, 230), paint("#3a9be0"))
    c.drawOval(oval(W / 2, 560, 360, 230), paint("#ffffff", 0.5, stroke=6))
    a = prog(t, q["f"] + 0.5, 0.5)
    py = 560 - 60 - 40 * (1 - pop(a))
    c.drawCircle(W / 2, py - 40, 34, paint(CORAL, clamp(a * 2)))
    c.drawPath(poly([(W / 2 - 30, py - 26), (W / 2 + 30, py - 26), (W / 2, py + 20)]), paint(CORAL, clamp(a * 2)))
    c.drawCircle(W / 2, py - 40, 13, paint("#ffffff", clamp(a * 2)))
    rotulo(c, "LAGO CRAWFORD · CANADÁ", W / 2, 860, "#2e47c9", ep(t, q["f"] + 1.0, 0.4), size=36)
    titulo(c, "ANTROPOCENO?", W / 2, 200, 100, "#ffffff", prog(t, q["f"] + 4.5, 0.5))
    if t > q["g"]:
        carimbo(c, "REJEITADO · 2024", W / 2, 560, CORAL, prog(t, q["g"] + 0.8, 0.8), size=80)
        L(c, 1680, 1060, 1.2, tg, face=-1, brow=-0.6, lid=0.3, smile=-0.2, look=(0.5, -0.3), arm_l=1.2, arm_r=1.2)
    fonte(c, "Working Group on the Anthropocene · IUGS, 2024", ep(t, q["f"] + 1.0, 0.4))


def s13(c, t, q, tg):
    def lupa():
        fundo(c, "#1f3196", "#111b5c")
        camadas(c, 0, 300, W, H, ["#c8945a", "#a87448", "#8a5a38", "#6b3442"], seed=8)
        c.drawRect(skia.Rect.MakeLTRB(0, 600, W, 612), paint(AMBER, 0.8))
        x = lerp(500, 1300, ease_io(prog(t, 0.5, 3)))
        c.drawCircle(x, 606, 150, paint("#cfe6ff", 0.25))
        c.drawCircle(x, 606, 150, paint("#ffffff", stroke=12))
        c.drawLine(x + 106, 712, x + 220, 830, paint("#ffffff", stroke=26))
        titulo(c, "UMA MARCA QUE NINGUÉM VAI DEIXAR PASSAR", W / 2, 180, 50, BONE, prog(t, 0.6, 0.5))
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lupa, lambda: _globo13(c, t, q, tg))
    elif t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _globo13(c, t, q, tg), lambda: _chuva(c, t, q, tg))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _chuva(c, t, q, tg), lambda: _meia_vida(c, t, q, tg))
    else:
        blend(c, fase(t, q["f"], 0.6), lambda: _meia_vida(c, t, q, tg), lambda: _crawford(c, t, q, tg))


# =====================================================================
# 14 · O AR PRESO NO GELO
# =====================================================================
CO2 = [(1750, 278), (1800, 282), (1850, 285), (1900, 296), (1950, 311), (1960, 317), (1970, 326), (1980, 339), (1990, 354),
       (2000, 369), (2010, 389), (2015, 401), (2020, 414), (2025, 430.5)]


def _antartida(c, t, q, tg):
    ceu(c, "#9fd6ff", "#ffffff")
    c.drawRect(skia.Rect.MakeLTRB(0, 640, W, H), paint("#eef6ff"))
    c.drawPath(poly([(0, 640), (500, 560), (900, 620), (1400, 540), (W, 640)]), paint("#dbeaff"))
    # sonda
    c.drawPath(poly([(1240, 640), (1320, 300), (1400, 640)], close=False), paint(CORAL, stroke=14))
    c.drawLine(1320, 300, 1320, 640, paint("#2e47c9", stroke=8))
    k = ep(t, q["b"], 1.5)
    # cilindro de gelo
    cx, cy = W / 2 - 200, 820
    c.drawRRect(rr(cx - 500 * k, cy - 70, 1000 * k + 1, 140, 70), paint("#cfeaff"))
    c.save()
    c.clipRRect(rr(cx - 500 * k, cy - 70, 1000 * k + 1, 140, 70), doAntiAlias=True)
    for j in range(14):
        c.drawLine(cx - 500 + j * 75, cy - 70, cx - 500 + j * 75, cy + 70, paint("#a9d4ff", stroke=3))
    rnd = random.Random(3)
    for _ in range(50):
        c.drawCircle(rnd.uniform(cx - 500, cx + 500), rnd.uniform(cy - 50, cy + 50) + 3 * math.sin(t * 2 + _),
                     rnd.uniform(4, 10), paint("#ffffff", 0.9, stroke=2))
    c.restore()
    titulo(c, "O AR", W / 2, 230, 140, "#2e47c9", prog(t, q["a"] + 0.3, 0.5))
    rotulo(c, "ANTÁRTIDA", 500, 400, SKY, ep(t, q["b"] + 0.3, 0.4), size=34)
    rotulo(c, "BOLHAS DO AR DE CADA ÉPOCA", W / 2 - 200, 990, "#2e47c9", ep(t, q["b"] + 2.0, 0.4), size=32)
    L(c, 1640, 1040, 1.2, tg, face=-1, look=(0.7, 0.2), brow=0.5)


def _grafico(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    x0, x1, y0, y1 = 260, 1660, 900, 220
    c.drawLine(x0, y0, x1, y0, paint(DUST, stroke=3))
    c.drawLine(x0, y0, x0, y1, paint(DUST, stroke=3))
    X = lambda ano: x0 + (ano - 1750) / (2025 - 1750) * (x1 - x0)
    Y = lambda ppm: y0 - (ppm - 260) / (440 - 260) * (y0 - y1)
    for ano in (1800, 1900, 2000):
        text(c, str(ano), X(ano), y0 + 44, 26, "mono", 500, DUST, 1, "center")
    for ppm in (280, 350, 430):
        c.drawLine(x0, Y(ppm), x1, Y(ppm), paint(LINE, 0.6, stroke=1.5))
        text(c, str(ppm), x0 - 20, Y(ppm) + 9, 24, "mono", 500, DUST, 1, "right")
    fim = lerp(1750, 1850, ep(t, q["c"], 1.0))
    if t > q["d"]:
        fim = lerp(1850, 2025, ease_io(prog(t, q["d"], 3.0)))
    pts = []
    for (a1, p1), (a2, p2) in zip(CO2, CO2[1:]):
        for k in range(10):
            ano = a1 + (a2 - a1) * k / 10
            if ano <= fim:
                pts.append((X(ano), Y(p1 + (p2 - p1) * k / 10)))
    if len(pts) > 1:
        c.drawPath(poly(pts, close=False), paint(CORAL, stroke=9))
        c.drawCircle(*pts[-1], 12, paint(AMBER))
        glow(c, *pts[-1], 80, AMBER, 0.5)
    rotulo(c, "~280 ppm ANTES DAS FÁBRICAS", 620, Y(280) - 60, CYAN, ep(t, q["c"] + 1.0, 0.4), size=30)
    rotulo(c, "430 ppm · MAIO DE 2025", 1340, 160, CORAL, ep(t, q["d"] + 2.6, 0.4), size=34)
    titulo(c, "GÁS CARBÔNICO NO AR", 660, 140, 48, BONE, prog(t, q["c"], 0.5))
    fonte(c, "NOAA · Mauna Loa · Scripps", ep(t, q["d"], 0.4))
    if t > q["e"]:
        rotulo(c, "A RESPIRAÇÃO DE UMA CIVILIZAÇÃO COM PRESSA", W / 2, 1000, AMBER, ep(t, q["e"] + 3.0, 0.4), size=32)


def s14(c, t, q, tg):
    blend(c, fase(t, q["c"], 0.6), lambda: _antartida(c, t, q, tg), lambda: _grafico(c, t, q, tg))


# =====================================================================
# 15 · O AVISO PARA O FUTURO
# =====================================================================
def _carta(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    estrelas(c, t, 5, 80, 0.5)
    u = ease_io(prog(t, 0.3, 3.5))
    x = lerp(200, 1700, u)
    y = 560 - 120 * math.sin(u * math.pi)
    for k in range(18):
        uu = max(0, u - k * 0.012)
        c.drawCircle(lerp(200, 1700, uu), 560 - 120 * math.sin(uu * math.pi), 9 - k * 0.4, paint(AMBER, 0.6 - k * 0.03))
    icone(c, "carta", x, y, 1.8, None, 1.0)
    titulo(c, "UMA MENSAGEM DE PROPÓSITO", W / 2, 200, 70, BONE, prog(t, 0.5, 0.5))
    rotulo(c, "PARA O FUTURO", W / 2, 900, AMBER, ep(t, 2.0, 0.4), size=40)


def _onkalo(c, t, q, tg):
    ceu(c, "#7ec8ff", "#d6f0ff")
    c.drawRect(skia.Rect.MakeLTRB(0, 250, W, 270), paint("#3fd17a"))
    for k in range(18):
        x = 50 + k * 110
        c.drawPath(poly([(x - 30, 255), (x, 170), (x + 30, 255)]), paint("#1f8f55"))
    camadas(c, 0, 270, W, H, ["#8a93c8", "#7a83b8", "#6a72a8", "#5a6298", "#4a5288"], seed=2)
    # poço e túneis
    c.drawRect(skia.Rect.MakeLTRB(930, 270, 990, 860), paint("#26307e"))
    c.drawRect(skia.Rect.MakeLTRB(400, 830, 1600, 890), paint("#26307e"))
    for x in range(450, 1600, 110):
        c.drawRect(skia.Rect.MakeLTRB(x, 890, x + 40, 960), paint("#26307e"))
    for k in range(3):
        ph = (t * 0.12 + k / 3) % 1
        icone(c, "capsula", 960, 300 + ph * 520, 0.55, None, 1.0)
    for i, x in enumerate(range(450, 1600, 110)):
        if prog(t, q["b"] + 1.0 + i * 0.25, 0.3) > 0:
            icone(c, "capsula", x + 20, 925, 0.4, None, prog(t, q["b"] + 1.0 + i * 0.25, 0.3))
    c.drawLine(1680, 270, 1680, 860, paint("#ffffff", stroke=3))
    rotulo(c, "~430 m", 1680, 560, AMBER, ep(t, q["b"] + 1.5, 0.4), size=30)
    rotulo(c, "LIXO NUCLEAR · CENTENAS DE METROS ABAIXO", W / 2, 80, "#2e47c9", ep(t, q["b"] + 0.5, 0.4), size=30)
    rotulo(c, "ONKALO · FINLÂNDIA", 520, 600, CORAL, ep(t, q["c"] + 1.0, 0.4), size=36)
    rotulo(c, "LICENÇA: OUTUBRO DE 2026", 520, 700, AMBER, ep(t, q["c"] + 3.0, 0.4), size=30)
    fonte(c, "Reuters/CP24, 22/10/2026 · Posiva", ep(t, q["c"] + 1.0, 0.4))


def _linguas(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    titulo(c, "Como avisar alguém daqui a", W / 2, 230, 64, BONE, prog(t, q["d"] + 0.2, 0.5))
    titulo(c, "milhares de anos?", W / 2, 320, 72, AMBER, prog(t, q["d"] + 0.6, 0.5))
    palavras = ["PERIGO", "DANGER", "PELIGRO", "VAARA", "GEFAHR", "PERICOLO", "GEVAAR", "TEHLIKE"]
    for i, w in enumerate(palavras):
        x, y = 260 + (i % 4) * 460, 560 + (i // 4) * 200
        some = prog(t, q["d"] + 4.0 + i * 0.25, 0.8)
        c.save()
        c.translate(x, y + 60 * some)
        text(c, w, 0, 0, 56, "display", 800, FESTA[i % 5], ep(t, q["d"] + 1.0 + i * 0.12, 0.3) * (1 - some), "center")
        c.restore()
    rotulo(c, "NENHUMA LÍNGUA DURA TANTO", W / 2, 990, CORAL, ep(t, q["d"] + 4.5, 0.4), size=34)


def espinhos(c, t, a=1.0):
    ceu(c, "#62b8ff", "#ffd9b0")
    c.drawRect(skia.Rect.MakeLTRB(0, 700, W, H), paint("#f0a860"))
    rnd = random.Random(8)
    for k in range(26):
        x, base = rnd.uniform(0, W), rnd.uniform(720, 1060)
        h, w = rnd.uniform(160, 420) * (base / 900), rnd.uniform(30, 60)
        ang = rnd.uniform(-18, 18)
        c.save()
        c.translate(x, base)
        c.rotate(ang)
        c.drawPath(poly([(-w, 0), (w, 0), (0, -h * pop(prog(a, k / 26, 0.2)))]), paint(mix("#5a4a6a", "#2a2238", base / 1100 - 0.4)))
        c.restore()


def placa(c, t, q, k1, k2):
    c.drawRRect(rr(360, 220, 1200, 640, 20), paint("#8a8fb0"))
    c.drawRRect(rr(380, 240, 1160, 600, 14), paint("#a3a8c8"))
    for i, (s_, k) in enumerate((("ESTE LUGAR NÃO É", k1), ("UM LUGAR DE HONRA.", k1), ("NADA DE VALOR", k2), ("ESTÁ AQUI.", k2))):
        n = int(len(s_) * clamp(k * 1.4 - (i % 2) * 0.4))
        text(c, s_[:n], 960, 380 + i * 110 + (40 if i > 1 else 0), 72, "display", 800, "#2a2f5a", 1.0, "center")


def _deserto(c, t, q, tg):
    espinhos(c, t, prog(t, q["e"], 2.5))
    rotulo(c, "NOVO MÉXICO · RELATÓRIO DE 1993", W / 2, 140, "#2e47c9", ep(t, q["e"] + 1.0, 0.4), size=34)
    fonte(c, "Sandia National Laboratories, SAND92-1382 (1993)", ep(t, q["e"] + 1.0, 0.4))
    if t > q["f"] - 0.2:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.45 * ep(t, q["f"] - 0.2, 0.4)))
        placa(c, t, q, prog(t, q["f"] + 2.0, 2.2), prog(t, q["f"] + 4.6, 1.8))


def _carta_futuro(c, t, q, tg):
    espinhos(c, t, 1.0)
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.45))
    placa(c, t, q, 1, 1)
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.25))
    L(c, 300, 1060, 1.4, tg, look=(0.9, -0.8), lid=0.25, smile=0.6, brow=0.3)
    rotulo(c, "UMA CARTA PARA O FUTURO: “NÃO CHEGUE PERTO”", 1150, 990, AMBER, ep(t, q["g"] + 2.5, 0.4), size=30)


def s15(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lambda: _carta(c, t, q, tg), lambda: _onkalo(c, t, q, tg))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _onkalo(c, t, q, tg), lambda: _linguas(c, t, q, tg))
    elif t < q["e"] + 0.4:
        blend(c, fase(t, q["e"], 0.6), lambda: _linguas(c, t, q, tg), lambda: _deserto(c, t, q, tg))
    else:
        blend(c, fase(t, q["g"], 0.8), lambda: _deserto(c, t, q, tg), lambda: _carta_futuro(c, t, q, tg))


# =====================================================================
# 16 · O ABISMO: um milhão de anos
# =====================================================================
ROCHAS = ["#5a6298", "#6a72a8", "#4a5288", "#7a83b8", "#5a6298", "#6a72a8", "#4a5288"]


def coluna(c, x0, y0, x1, y1, faixa_y, cor_faixa="#2a2238", h_faixa=10, seed=3, brilho=0.0):
    camadas(c, x0, y0, x1, y1, ROCHAS, seed=seed, onda=8)
    c.drawRect(skia.Rect.MakeLTRB(x0, faixa_y, x1, faixa_y + h_faixa), paint(cor_faixa))
    if brilho:
        c.drawRect(skia.Rect.MakeLTRB(x0, faixa_y - 8, x1, faixa_y + h_faixa + 8), paint(AMBER, 0.4 * brilho, blur=10))


def _retratos(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    for k, (nome, inst) in enumerate((("GAVIN SCHMIDT", "NASA"), ("ADAM FRANK", "UNIV. DE ROCHESTER"))):
        x = 620 + k * 680
        a = ep(t, q["c"] + 1.5 + k * 2.4, 0.5)
        c.drawRRect(rr(x - 220, 260, 440, 500, 30), paint("#2c45b8", a))
        pessoa(c, x, 700, 1.9, [CYAN, AMBER][k], PELE[k * 2], a=a, cabelo=["#3a2416", "#7a6a5a"][k])
        rotulo(c, nome, x, 820, FESTA[k], a, size=34)
        text(c, inst, x, 900, 26, "mono", 500, DUST, a, "center")
    rotulo(c, "2018", W / 2, 150, CORAL, ep(t, q["c"] + 0.3, 0.4), size=40)
    fonte(c, "Schmidt & Frank, International Journal of Astrobiology, 2018", ep(t, q["c"], 0.4))
    if t > q["d"] - 0.2:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.75 * ep(t, q["d"] - 0.2, 0.4)))
        titulo(c, "Se houvesse uma civilização industrial", W / 2, 420, 62, BONE, prog(t, q["d"], 0.5))
        titulo(c, "há milhões de anos, daria para perceber?", W / 2, 520, 62, AMBER, prog(t, q["d"] + 0.8, 0.5))
        titulo(c, "NÃO SERIA FÁCIL.", W / 2, 720, 100, CORAL, prog(t, q["e"] + 1.0, 0.5))


def _faixa(c, t, q, tg):
    fundo(c, "#111b5c", "#070c38")
    z = lerp(3.5, 1.0, ease_io(prog(t, q["b"] - 0.5, 4))) if t < q["c"] else 1.0
    c.save()
    c.translate(W / 2, 560)
    c.scale(z, z)
    c.translate(-W / 2, -560)
    coluna(c, 260, 100, 1660, 1020, 556, h_faixa=10)
    c.drawRect(skia.Rect.MakeLTRB(260, 566, 1660, 570), paint("#111b5c"))
    c.restore()
    rotulo(c, "AS CIDADES: ENTULHO PRENSADO", 560, 470, CORAL, ep(t, q["b"] + 0.5, 0.4), size=28)
    rotulo(c, "O PLÁSTICO: UMA LÂMINA ESCURA", 1360, 660, AMBER, ep(t, q["b"] + 2.5, 0.4), size=28)


def _parecidas(c, t, q, tg):
    fundo(c, "#111b5c", "#070c38")
    if t < q["g"] - 0.2:
        coluna(c, 260, 100, 1660, 1020, 556, h_faixa=14, brilho=0.6 + 0.4 * math.sin(t * 3))
        for k, s_ in enumerate(("MUDANÇA NO CARBONO", "RESTOS DE PLÁSTICO", "ELEMENTOS RAROS")):
            rotulo(c, s_, 520 + k * 440, 470 if k % 2 == 0 else 660, FESTA[k], ep(t, q["f"] + 1.5 + k * 1.2, 0.4), size=28)
    else:
        for k, (nome, cor) in enumerate((("EVENTO NATURAL", "#2a2238"), ("NÓS", "#2a2238"), ("EVENTO NATURAL", "#2a2238"))):
            x = 360 + k * 600
            a = ep(t, q["g"] + k * 0.4, 0.4)
            c.saveLayerAlpha(None, int(255 * a))
            coluna(c, x - 220, 160, x + 220, 960, 520 + k * 20, cor, 12, seed=k + 4)
            c.restore()
            rotulo(c, nome, x, 1010, CYAN if k == 1 else DUST, a, size=30)
        titulo(c, "DE LONGE, SE PARECEM", W / 2, 100, 54, BONE, prog(t, q["g"] + 1.5, 0.5))


def _final16(c, t, q, tg):
    fundo(c, "#070c38", "#070c38")
    titulo(c, "Oito bilhões de pessoas.", W / 2, 360, 76, BONE, prog(t, q["h"] + 0.1, 0.5))
    titulo(c, "Um século de pressa.", W / 2, 480, 76, BONE, prog(t, q["h"] + 1.8, 0.5))
    a = ep(t, q["h"] + 3.6, 1.0)
    c.drawRect(skia.Rect.MakeLTRB(0, 700, W * a, 712), paint(AMBER))
    c.drawRect(skia.Rect.MakeLTRB(0, 690, W * a, 722), paint(AMBER, 0.4, blur=12))
    titulo(c, "uma faixa fina de rocha diferente", W / 2, 830, 52, AMBER, prog(t, q["h"] + 4.6, 0.5))


def s16(c, t, q, tg):
    def mil():
        fundo(c, "#1d2f8f", "#070c38")
        estrelas(c, t, 7, 120, 0.6)
        relogio(c, W / 2, 470, 230, t * 25, 1.0, 1.0, t)
        titulo(c, "1.000.000 DE ANOS", W / 2, 880, 110, AMBER, prog(t, q["a"] + 1.4, 0.5))
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.7), mil, lambda: _faixa(c, t, q, tg))
    elif t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _faixa(c, t, q, tg), lambda: _retratos(c, t, q, tg))
    elif t < q["f"] + 0.4:
        blend(c, fase(t, q["f"], 0.6), lambda: _retratos(c, t, q, tg), lambda: _parecidas(c, t, q, tg))
    else:
        blend(c, fase(t, q["h"], 0.8), lambda: _parecidas(c, t, q, tg), lambda: _final16(c, t, q, tg))


# =====================================================================
# 17 · OS RASTROS MAIS LONGE
# =====================================================================
def _sobe(c, t, q, tg):
    fundo(c, "#070c38", "#1d2f8f")
    estrelas(c, t, 11, 200, 0.8)
    y = lerp(1150, 1700, ease_io(prog(t, 0, 3.5)))
    globo(c, W / 2, y, 700, t * 4)
    titulo(c, "LONGE DAQUI", W / 2, 300, 100, BONE, prog(t, q["a"] + 0.3, 0.5))


def _lua(c, t, q, tg):
    fundo(c, "#070c38", "#111b5c")
    estrelas(c, t, 12, 160, 0.8)
    globo(c, 1550, 220, 90, t * 4)
    c.drawPath(poly([(0, 640), (500, 600), (1000, 650), (1500, 590), (W, 630), (W, H), (0, H)]), paint("#b9bcd6"))
    rnd = random.Random(2)
    for _ in range(14):
        x, y, r = rnd.uniform(0, W), rnd.uniform(700, 1050), rnd.uniform(20, 70)
        c.drawOval(oval(x, y, r, r * 0.35), paint("#9a9dbb"))
    n = int(clamp(prog(t, q["b"] + 0.5, 2.5)) * 12)
    for k in range(n):
        x = 300 + k * 110
        y = 900 - k * 18 + (k % 2) * 30
        c.drawRRect(rr(x - 22, y - 12, 44, 24, 12), paint("#7a7d9b"))
        for j in range(4):
            c.drawLine(x - 16 + j * 10, y - 8, x - 16 + j * 10, y + 8, paint("#5a5d7b", stroke=3))
    rotulo(c, "PEGADAS NA LUA", W / 2, 150, SKY, ep(t, q["b"] + 0.3, 0.4), size=40)
    rotulo(c, "SEM VENTO NEM CHUVA: MILHÕES DE ANOS", W / 2, 250, AMBER, ep(t, q["b"] + 2.5, 0.4), size=32)
    fonte(c, "NASA · Lunar Reconnaissance Orbiter", ep(t, q["b"] + 0.5, 0.4))


def satelite(c, x, y, s, ang):
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(s, s)
    c.drawRect(skia.Rect.MakeLTRB(-60, -12, -16, 12), paint("#3a63e0"))
    c.drawRect(skia.Rect.MakeLTRB(16, -12, 60, 12), paint("#3a63e0"))
    c.drawRRect(rr(-16, -18, 32, 36, 4), paint("#c9d0ff"))
    c.restore()


def _cemiterio(c, t, q, tg):
    fundo(c, "#070c38", "#111b5c")
    estrelas(c, t, 13, 160, 0.8)
    globo(c, W / 2, 560, 170, t * 6)
    c.drawOval(oval(W / 2, 560, 620, 220), paint(DUST, 0.35, stroke=2))
    for k in range(9):
        ang = t * 0.08 + k * 2 * math.pi / 9
        x, y = W / 2 + math.cos(ang) * 620, 560 + math.sin(ang) * 220
        satelite(c, x, y, 0.8, k * 30 + t * 6)
    rotulo(c, "ÓRBITA CEMITÉRIO · ~36.000 km", W / 2, 140, CORAL, ep(t, q["c"] + 0.5, 0.4), size=36)
    rotulo(c, "SATÉLITES MORTOS GIRANDO POR MILHÕES DE ANOS", W / 2, 990, DUST, ep(t, q["c"] + 3.0, 0.4), size=28)


def _voyager(c, t, q, tg):
    fundo(c, "#070c38", "#111b5c")
    estrelas(c, t, 14, 220, 0.9)
    x = lerp(700, 1100, prog(t, q["d"], 9))
    c.save()
    c.translate(x, 540)
    c.rotate(-12)
    c.drawLine(0, 0, 360, 40, paint("#c9d0ff", stroke=6))
    c.drawLine(0, 0, -260, 120, paint("#c9d0ff", stroke=4))
    c.drawPath(_meia_lua(0, -90, 140), paint("#e8ecff"))
    c.drawRect(skia.Rect.MakeLTRB(-140, -92, 140, -84), paint("#c9d0ff"))
    c.drawRect(skia.Rect.MakeLTRB(-50, -84, 50, 20), paint("#9fa6d0"))
    glow(c, 60, -20, 90, AMBER, 0.6 + 0.3 * math.sin(t * 3))
    c.drawCircle(60, -20, 32, paint(AMBER))
    c.drawCircle(60, -20, 8, paint("#c98a1c"))
    c.restore()
    rotulo(c, "VOYAGER · DISCO DE OURO", W / 2, 140, AMBER, ep(t, q["d"] + 0.5, 0.4), size=38)
    rotulo(c, "FEITO PARA DURAR ~1 BILHÃO DE ANOS", W / 2, 990, CYAN, ep(t, q["d"] + 3.5, 0.4), size=32)
    fonte(c, "NASA/JPL", ep(t, q["d"] + 0.5, 0.4))


def _bolha(c, t, q, tg):
    fundo(c, "#070c38", "#111b5c")
    estrelas(c, t, 15, 220, 0.9)
    for k in range(6):
        r = ((t * 70 + k * 120) % 720)
        c.drawCircle(W / 2, 560, r, paint(CYAN, 0.55 * (1 - r / 720), stroke=4))
    globo(c, W / 2, 560, 40, t * 6)
    rotulo(c, "BOLHA DE RÁDIO", W / 2, 140, CYAN, ep(t, q["e"] + 0.5, 0.4), size=40)
    rotulo(c, "MAIS DE 100 ANOS-LUZ DE RAIO", W / 2, 990, AMBER, ep(t, q["e"] + 3.0, 0.4), size=34)
    fonte(c, "EarthSky", ep(t, q["e"] + 0.5, 0.4))


def s17(c, t, q, tg):
    if t < q["b"] + 0.4:
        blend(c, fase(t, q["b"], 0.6), lambda: _sobe(c, t, q, tg), lambda: _lua(c, t, q, tg))
    elif t < q["c"] + 0.4:
        blend(c, fase(t, q["c"], 0.6), lambda: _lua(c, t, q, tg), lambda: _cemiterio(c, t, q, tg))
    elif t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _cemiterio(c, t, q, tg), lambda: _voyager(c, t, q, tg))
    else:
        blend(c, fase(t, q["e"], 0.6), lambda: _voyager(c, t, q, tg), lambda: _bolha(c, t, q, tg))


# =====================================================================
# 18 · A VIRADA: a camada ainda não estava escrita
# =====================================================================
def _pagina(c, t, q, tg):
    fundo(c, "#1f3196", "#111b5c")
    coluna(c, 260, 100, 1660, 1020, 540, h_faixa=12)
    k = ease_io(prog(t, q["b"], 1.4))
    h = lerp(12, 300, k)
    c.drawRRect(rr(260, 546 - h / 2, 1400, h, 12), paint("#fff6e8", k ** 0.5))
    if k > 0.6:
        if int(t * 2) % 2 == 0:
            c.drawRect(skia.Rect.MakeLTRB(330, 500, 336, 590), paint(INK))
        titulo(c, "ainda não estava escrita", W / 2, 570, 72, "#2e47c9", prog(t, q["b"] + 1.0, 0.5), sombra=False)
    rotulo(c, "TODA CAMADA É UM REGISTRO DE ESCOLHAS", W / 2, 960, AMBER, ep(t, q["c"] + 0.4, 0.4), size=34)


def _sliders(c, t, q, tg):
    fundo(c, "#7ec8ff", "#ffd9e8")
    falas = [q["d"], q["d"] + 2.0, q["d"] + 4.0]
    for k, nome in enumerate(("PLÁSTICO", "CARBONO", "BOMBAS")):
        y = 330 + k * 220
        a = ep(t, q["d"] + k * 2.0 - 0.3, 0.4)
        c.drawRRect(rr(560, y - 14, 900, 28, 14), paint("#ffffff", a))
        text(c, nome, 520, y + 14, 44, "display", 800, "#2e47c9", a, "right")
        text(c, "MENOS", 600, y + 70, 22, "mono", 500, "#2e47c9", a * 0.8)
        text(c, "MAIS", 1420, y + 70, 22, "mono", 500, "#2e47c9", a * 0.8, "right")
        osc = 0.75 + 0.2 * math.sin((t - falas[k]) * 3.2) if t < q["e"] else 0.75
        desce = ease_io(prog(t, q["e"] + k * 0.4, 1.2))
        pos = lerp(osc, 0.15, desce)
        kx = 560 + 900 * pos
        c.drawCircle(kx, y, 34, paint(mix(CORAL, CYAN, desce), a))
        c.drawCircle(kx, y, 34, paint("#ffffff", a, stroke=5))
    L(c, 1700, 1060, 1.2, tg, face=-1, look=(0.8, -0.6), arm_r=2.0, smile=0.9)
    titulo(c, "E ELES COMEÇARAM A ESCOLHER", W / 2, 1000, 50, "#2e47c9", prog(t, q["e"], 0.5))


def _ozonio(c, t, q, tg):
    fundo(c, "#070c38", "#111b5c")
    estrelas(c, t, 16, 160, 0.8)
    globo(c, W / 2, 560, 300, 40 + t * 3)
    fecha = ease_io(prog(t, q["e2"] + 9.0, 5))
    buraco = lerp(70, 0, fecha)
    anel = skia.Path()
    anel.addArc(skia.Rect.MakeLTRB(W / 2 - 345, 215, W / 2 + 345, 905), 90 + buraco / 2, 360 - buraco)
    c.drawPath(anel, paint(CYAN, 0.45, stroke=36, cap_round=False))
    if buraco > 1:
        rotulo(c, "BURACO", W / 2 + 300, 880, CORAL, (1 - fecha) * ep(t, q["e2"] + 4.0, 0.4), size=26)
    rotulo(c, "CAMADA DE OZÔNIO", W / 2, 150, CYAN, ep(t, q["e2"] + 2.5, 0.4), size=38)
    rotulo(c, "PROTOCOLO DE MONTREAL · 1987", W / 2, 990, AMBER, ep(t, q["e2"] + 7.0, 0.4), size=36)
    rotulo(c, "A CAMADA COMEÇOU A SE RECUPERAR", 1500, 560, CYAN, ep(t, q["e2"] + 11.5, 0.4), size=26)
    fonte(c, "ONU/UNEP, avaliação científica do ozônio, 2023", ep(t, q["e2"] + 7.0, 0.4))


def _acoes(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    if t < q["g"] - 0.2:
        icone(c, "filme", 560, 480, 2.4, None, prog(t, q["f"] + 0.3, 0.5))
        rotulo(c, "ARQUIVOS PARA SÉCULOS", 560, 760, "#2e47c9", ep(t, q["f"] + 0.6, 0.4), size=32)
        ph = prog(t, q["f"] + 2.5, 4)
        c.drawRect(skia.Rect.MakeLTRB(1310, 260, 1410, 700), paint("#26307e", ep(t, q["f"] + 2.3, 0.4)))
        icone(c, "capsula", 1360, lerp(320, 620, ph), 1.0, None, prog(t, q["f"] + 2.3, 0.4))
        rotulo(c, "LIXO PERIGOSO BEM FUNDO", 1360, 760, CORAL, ep(t, q["f"] + 2.8, 0.4), size=32)
    else:
        camadas(c, 0, 600, W, H, ["#c8945a", "#a87448", "#8a5a38", "#6b3442"], seed=8)
        c.drawRect(skia.Rect.MakeLTRB(1000, 560, 1060, 1000), paint("#cfeaff"))
        for k in range(10):
            c.drawLine(1000, 600 + k * 40, 1030, 600 + k * 40, paint(INK, stroke=3))
        pessoa(c, 820, 600, 1.4, CYAN, PELE[3], braco=1.4)
        rotulo(c, "MEDIR O QUE FICA NO CHÃO", W / 2, 160, "#2e47c9", ep(t, q["g"] + 0.3, 0.4), size=36)
        rotulo(c, "PARA PODER MUDAR", W / 2, 260, AMBER, ep(t, q["g"] + 2.0, 0.4), size=36)


def s18(c, t, q, tg):
    if t < q["d"] + 0.4:
        blend(c, fase(t, q["d"], 0.6), lambda: _pagina(c, t, q, tg), lambda: _sliders(c, t, q, tg))
    elif t < q["e2"] + 0.4:
        blend(c, fase(t, q["e2"], 0.6), lambda: _sliders(c, t, q, tg), lambda: _ozonio(c, t, q, tg))
    else:
        blend(c, fase(t, q["f"], 0.6), lambda: _ozonio(c, t, q, tg), lambda: _acoes(c, t, q, tg))


# =====================================================================
# 19 · DE VOLTA AO MUSEU · 20 · A ETIQUETA · 21 · A PRÓXIMA PEÇA
# =====================================================================
def s19(c, t, q, tg):
    z = lerp(1.2, 1.7, ease_io(prog(t, 0, 14)))
    c.save()
    camera(c, 830, 600, z)
    mundo(c, tg, dict(titulo_a=0.0, luz=1.0))
    glow(c, CENTRAL["cx"], 480, 380, AMBER, 0.35 * ep(t, q["b"], 3))
    L(c, 680, 880, 1.3, tg, face=1, look=(1.0, -0.4), lid=0.25, smile=0.9, cheek=0.7, tilt=0.05)
    c.restore()
    titulo(c, "decidir o que ia sobrar", W / 2, 150, 70, AMBER, prog(t, q["c"] + 2.2, 0.6))


def maquina(s, k):
    return s[: int(len(s) * clamp(k))]


def s20(c, t, q, tg):
    c.save()
    camera(c, 960, 560, 1.3)
    mundo(c, tg, dict(titulo_a=0.0))
    L(c, 640, 880, 1.25, tg, face=1, look=(0.9, -0.2), smile=0.7, arm_r=lerp(0.2, 2.2, ep(t, 0.4, 0.6)) * (1 - prog(t, 2.0, 0.5)))
    c.restore()
    a = ep(t, q["a"] + 1.2, 0.6)
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.55 * a))
    c.save()
    c.translate(W / 2, 560 + 60 * (1 - a))
    c.rotate(-1.5)
    c.drawRRect(rr(-620, -380, 1240, 760, 10), paint(INK, 0.4 * a))
    c.drawRRect(rr(-630, -390, 1240, 760, 10), paint("#ffe9c2", a))
    c.drawRect(skia.Rect.MakeLTRB(-630, 350, 610, 370), paint("#e2b97a", a))
    linhas = [("PEÇA Nº 001", q["a"] + 1.8, 34, 800),
              ("Retângulo de vidro e metal.", q["b"], 40, 500),
              ("Século 21 d.C.", q["b"] + 1.6, 40, 500),
              ("Os Antigos guardavam o mundo inteiro aqui dentro.", q["c"], 34, 500),
              ("Não sobrou nada aqui dentro.", q["c"] + 2.6, 34, 500),
              ("Sobrou o que eles fizeram lá fora.", q["d"], 44, 500)]
    for i, (s_, t0, size, w_) in enumerate(linhas):
        k = prog(t, t0, len(s_) * 0.045)
        y = -280 + [0, 110, 170, 300, 360, 470][i]
        cor = "#3a2c18" if i < 5 else "#b5381e"
        text(c, maquina(s_, k), -560, y, size, "mono", 500 if w_ < 800 else 500, cor, a)
    c.restore()


def s21(c, t, q, tg):
    pan = ease_io(prog(t, 0.2, 3.0))
    c.save()
    camera(c, lerp(960, 1590, pan), 560, lerp(1.2, 1.7, pan))
    mundo(c, tg, dict(titulo_a=0.0))
    # pano cobrindo a próxima vitrine (desenhado por cima da lateral direita)
    vx, top = 1590, 610
    pano = skia.Path()
    pano.moveTo(vx - 135, top + 20)
    pano.cubicTo(vx - 150, top - 120, vx - 110, top - 230, vx, top - 225)
    pano.cubicTo(vx + 110, top - 230, vx + 150, top - 120, vx + 135, top + 20)
    for k in range(6):
        pano.lineTo(vx + 135 - k * 54, top + 20 + (12 if k % 2 else 0))
    pano.close()
    pulsa = 0.6 + 0.4 * math.sin(tg * 2.5)
    glow(c, vx, top - 100, 220, CYAN, 0.45 * pulsa)
    c.drawPath(pano, paint(CORAL))
    c.drawPath(pano, paint("#d94a5e", stroke=4))
    c.drawRRect(rr(vx - 30, top - 150, 60, 104, 10), paint(CYAN, 0.35 * pulsa))
    x = lerp(1300, 1430, ep(t, 0.6, 2.0))
    L(c, x, 880, 1.05, tg, face=1, look=(0.8, -0.5), brow=0.7, arm_r=1.6 * ep(t, 2.6, 0.5))
    c.restore()
    rotulo(c, "PRÓXIMA PEÇA · Nº 002", W / 2, 120, AMBER, ep(t, q["a"] + 1.0, 0.4), size=40)
    if t > q["b"] - 0.2:
        a = ep(t, q["b"] - 0.2, 0.5)
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.6 * a))
        titulo(c, "Que objeto da sua casa", W / 2, 430, 80, BONE, prog(t, q["b"] + 0.6, 0.5))
        titulo(c, "deveria entrar no museu?", W / 2, 540, 80, AMBER, prog(t, q["b"] + 1.0, 0.5))
        rotulo(c, "ESCREVE NOS COMENTÁRIOS", W / 2, 700, CYAN, ep(t, q["c"] + 0.2, 0.4), size=40)
    fim = TOTAL - (CENAS[-1]["start"])
    logo(c, W / 2, 900, 0.7, ep(t, fim - 3.5, 0.8))
    if t > fim - 1.0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", prog(t, fim - 1.0, 1.0)))


# =====================================================================
# QUADRO
# =====================================================================
FUNCS = {"03": s03, "04": s04, "05": s05, "06": s06, "07": s07, "08": s08, "09": s09, "10": s10, "11": s11, "12": s12,
         "13": s13, "14": s14, "15": s15, "16": s16, "17": s17, "18": s18, "19": s19, "20": s20, "21": s21}


def cena_em(tg):
    for i, s in enumerate(CENAS):
        if s["start"] <= tg < s["end"]:
            return i
    return len(CENAS) - 1


def desenha(c, i, tg):
    s = CENAS[i]
    if s["id"] in ("01", "02"):
        abre.quadro(c, tg, fecha=False)
        return
    c.save()
    FUNCS[s["id"]](c, tg - s["start"], s["cues"], tg)
    c.restore()


def quadro(c, tg):
    i = cena_em(tg)
    s = CENAS[i]
    tl = tg - s["start"]
    if i > 0 and tl < TR and s["id"] != "02":
        desenha(c, i - 1, tg)
        c.saveLayerAlpha(None, int(255 * ease_io(tl / TR)))
        desenha(c, i, tg)
        c.restore()
    else:
        desenha(c, i, tg)


def render(i0, i1, saida):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                           "-pix_fmt", "yuv420p", str(saida)], stdin=subprocess.PIPE)
    for f in range(i0, i1):
        c.clear(hexc(INK))
        quadro(c, f / FPS)
        ff.stdin.write(surf.makeImageSnapshot().toarray(colorType=skia.kRGBA_8888_ColorType).tobytes())
        if (f - i0) % 600 == 0:
            print(f"{saida.name}: {f - i0}/{i1 - i0}", flush=True)
    ff.stdin.close()
    ff.wait()


def main():
    out = lingua.saida(AQUI)
    out.mkdir(exist_ok=True)
    a = sys.argv[1:]
    if a and a[0] == "--preview":
        surf = skia.Surface(W, H)
        c = surf.getCanvas()
        pares = a[1:]
        for k in range(0, len(pares), 2):
            sid, tl = pares[k], float(pares[k + 1])
            s = next(x for x in CENAS if x["id"] == sid)
            c.clear(hexc(INK))
            quadro(c, s["start"] + tl)
            surf.makeImageSnapshot().save(str(out / f"prev_{sid}_{tl}.png"), skia.kPNG)
        return
    if a and a[0] == "--parte":  # --parte k n
        k, n = int(a[1]), int(a[2])
        tot = int(TOTAL * FPS)
        i0, i1 = tot * k // n, tot * (k + 1) // n
        render(i0, i1, out / f"parte_{k:02d}.mp4")
        return
    if a and a[0] == "--render":
        n = int(a[a.index("--partes") + 1]) if "--partes" in a else 4
        procs = [subprocess.Popen([sys.executable, __file__, "--parte", str(k), str(n)]) for k in range(n)]
        for p in procs:
            p.wait()
        lst = out / "partes.txt"
        lst.write_text("".join(f"file 'parte_{k:02d}.mp4'\n" for k in range(n)))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                        str(out / "piloto_mudo.mp4")], check=True)
        print("ok", out / "piloto_mudo.mp4")


if __name__ == "__main__":
    main()
