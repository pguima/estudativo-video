"""Animação do vídeo 02 "Por Que os Antigos Não Conseguiam Parar de Olhar?" (18 cenas, ~9 min).
Tempos: audio/tempos.json (cenas e cues casados com as palavras da narração). Peças: _ferramentas/antigos.py.
Cada cena é uma função sNN(c, t, q, tg): t = tempo local da cena, q = cues (tempo local), tg = tempo global.

python visual.py --preview 03 5.0 [06 20 ...]   → saida/prev_<cena>_<t>.png
python visual.py --render [--partes 4]           → saida/video_mudo.mp4 (em paralelo)
"""
import sys, json, math, random, wave, subprocess
from pathlib import Path
import numpy as np
import skia
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
sys.path.insert(0, str(AQUI.parent / "visual"))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals())
from antigos import *  # noqa: E402,F403
from estudo import LATERAIS, peca_lateral  # noqa: E402

TEMPOS = json.loads((lingua.audio(AQUI) / "tempos.json").read_text())
CENAS = TEMPOS["scenes"]
TOTAL = TEMPOS["total"]
TR = 0.45  # transição (dissolve) entre cenas
AZUL_TELA = "#4cc9ff"


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


def partes(c, t, q, lista):
    """lista = [(cue_de_entrada, função), ...]: troca de parte com dissolve em cada cue"""
    k = 0
    for i in range(1, len(lista)):
        if t >= q[lista[i][0]] - 0.3:
            k = i
    if k == 0:
        lista[0][1]()
        return
    blend(c, fase(t, q[lista[k][0]], 0.6), lista[k - 1][1], lista[k][1])


def chao(c, y=1000, cor="#4a52b8"):
    c.drawRect(skia.Rect.MakeLTRB(0, y, W, H), paint(cor))
    c.drawRect(skia.Rect.MakeLTRB(0, y, W, y + 8), paint("#8a93ff"))


def maquina(s, k):
    return s[: int(len(s) * clamp(k))]


def citacao(c, linhas, x, y, size, a_list, cor=BONE, destaque=AMBER):
    """linhas de citação centralizadas; a_list = progresso de cada linha"""
    for i, (s_, a) in enumerate(zip(linhas, a_list)):
        titulo(c, s_, x, y + i * size * 1.18, size, destaque if i == len(linhas) - 1 else cor, a)


# =====================================================================
# O CELULAR ACESO (peça 002 e reconstituições)
# =====================================================================
APPS = [CORAL, AMBER, SKY, CYAN, PINK, "#7be36b", "#ff9f43", "#3a63e0"]


def tela_apps(c, x, y, w, h, t, badge=0.0, feed=0.0, a=1.0):
    """conteúdo da tela: grade de apps (feed=0) ou feed rolando (feed=1)"""
    c.save()
    c.clipRRect(rr(x, y, w, h, 10), doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), linear(x, y, x, y + h, ["#3fb8ff", "#2e47c9"], a=a))
    if feed < 1:
        al = a * (1 - feed)
        ic = w / 4.2
        for r_ in range(5):
            for k in range(3):
                cx, cy = x + w * (0.2 + k * 0.3), y + h * 0.13 + r_ * ic * 1.25
                c.drawRRect(rr(cx - ic / 2, cy - ic / 2, ic, ic, ic * 0.28), paint(APPS[(r_ * 3 + k) % 8], al))
        if badge > 0:
            bx, by = x + w * 0.2 + ic / 2, y + h * 0.13 - ic / 2
            r = ic * 0.3 * pop(badge)
            c.drawCircle(bx, by, r, paint("#ff2d55", al))
            text(c, "3", bx, by + r * 0.42, r * 1.25, "display", 800, "#ffffff", al * clamp(badge * 2), "center")
    if feed > 0:
        off = (t * h * 0.35) % (h * 0.42)
        for k in range(-1, 4):
            yy = y + k * h * 0.42 - off + h * 0.04
            c.drawRRect(rr(x + w * 0.08, yy, w * 0.84, h * 0.36, 8), paint("#ffffff", 0.9 * a * feed))
            c.drawRRect(rr(x + w * 0.12, yy + h * 0.03, w * 0.76, h * 0.2, 6), paint(APPS[(k + 9) % 8], a * feed))
            c.drawRect(skia.Rect.MakeXYWH(x + w * 0.12, yy + h * 0.26, w * 0.5, h * 0.025), paint(INK, 0.4 * a * feed))
    c.restore()


def celular_aceso(c, cx, cy, s=1.0, t=0.0, tela=1.0, badge=0.0, feed=0.0, ang=0.0, a=1.0):
    """celular em pé (cx, cy = centro), tela 0 = apagada, 1 = acesa"""
    if a <= 0:
        return
    c.save()
    c.translate(cx, cy)
    c.rotate(ang)
    c.scale(s, s)
    w, h = 120, 236
    if tela > 0:
        glow(c, 0, 0, 260, AZUL_TELA, 0.5 * tela * a)
    c.drawRRect(rr(-w / 2 + 8, -h / 2 + 10, w, h, 20), paint(INK, 0.45 * a, blur=8))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 20), paint("#1c232c", a))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 20), paint("#c9d3d6", 0.9 * a, stroke=4))
    c.drawRRect(rr(-w / 2 + 8, -h / 2 + 10, w - 16, h - 20, 12), paint("#141b24", a))
    if tela > 0:
        c.saveLayerAlpha(None, int(255 * clamp(tela) * a))
        tela_apps(c, -w / 2 + 8, -h / 2 + 10, w - 16, h - 20, t, badge, feed)
        c.restore()
    c.drawRRect(rr(-14, -h / 2 + 4, 28, 5, 2), paint("#0b0f14", a))
    c.drawPath(poly([(-w / 2 + 10, -h / 2 + 12), (-w / 2 + 50, -h / 2 + 12), (-w / 2 + 10, -h / 2 + 90)]), paint("#ffffff", 0.07 * a))
    c.restore()


def peca_002(c, cx, base, t, tela=1.0, luz=1.0, badge=0.0):
    """o celular aceso num suporte de acrílico (base = topo do pedestal)"""
    c.drawPath(poly([(cx - 50, base), (cx + 50, base), (cx + 30, base - 40), (cx - 30, base - 40)]), paint("#cfe6ff", 0.35 * luz))
    celular_aceso(c, cx, base - 150, 0.95, t, tela, badge)
    c.drawOval(oval(cx, base - 2, 90, 10), paint(AZUL_TELA, 0.35 * tela, blur=10))


def mundo2(c, t, st):
    """o salão com a peça 002 na vitrine central (mesmo salão do piloto)"""
    salao(c, t, titulo="ALA 02 · O QUE PRENDIA OS OLHOS", titulo_a=st.get("titulo_a", 1.0))
    luz_salao = st.get("salao", 1.0)
    for v in LATERAIS:
        holofote(c, v["cx"], 72, v["top"], 40, v["w"] * 1.1, 0.75 * luz_salao)
        pedestal(c, v["cx"], v["top"], v["w"] + 30, 200, None, 0.75 * luz_salao)
        peca_lateral(c, v["obj"], v["cx"], v["top"] - 6)
        vitrine_vidro(c, v["cx"], v["top"], v["w"], v["h"], t)
    if luz_salao < 1:
        c.drawRect(skia.Rect.MakeLTRB(0, 0, W, H + 400), paint("#0a1240", 0.82 * (1 - luz_salao)))
    cx, top, w, h = 960, 640, 340, 300
    luz = st.get("luz", 1.0)
    holofote(c, cx, 72, top, 50, w * 1.25, luz)
    pedestal(c, cx, top, w + 40, 230, "PEÇA Nº 002 · c. 2026 d.C.", luz)
    peca_002(c, cx, top - 4, t, st.get("tela", 1.0), luz, st.get("badge", 0.0))
    vitrine_vidro(c, cx, top, w, h, t)
    poeira(c, t, (cx - 170, 90, cx + 170, top), 46, seed=2, a=0.55 * luz, zoom=st.get("zoom", 1))
    if luz_salao > 0:
        for i, lv in enumerate(LATERAIS):
            poeira(c, t, (lv["cx"] - 110, 90, lv["cx"] + 110, lv["top"]), 18, seed=10 + i, a=0.4 * luz_salao)


def antigo(c, x, y, s, t, roupa=CORAL, pele=PELE[0], cabelo="#3a2416", luz=1.0, olhar=1, a=1.0):
    """um Antigo de pé olhando o celular aceso na mão (rosto iluminado de baixo)"""
    if a <= 0:
        return
    pessoa(c, x, y, s, roupa, pele, braco=1.25, a=a, cabelo=cabelo, olhar=olhar)
    hx, hy = x + olhar * (16 + 50 * math.sin(1.25)) * s, y + (-112 + 50 * math.cos(1.25)) * s
    glow(c, x + olhar * 6 * s, y - 140 * s, 60 * s, AZUL_TELA, 0.55 * luz * a)
    celular_aceso(c, hx + olhar * 4 * s, hy - 10 * s, 0.17 * s, t, luz, ang=-20 * olhar, a=a)


# =====================================================================
# 01 · 02 · ABERTURA: a vitrine 002 acende e o salão aparece
# =====================================================================
def s01(c, t, q, tg):
    if t < 0.35:
        luz = 0.0
    elif t < 0.9:
        luz = [0, 0.7, 0.15, 0.9, 0.4, 1.0][min(5, int((t - 0.35) / 0.09))]
    else:
        luz = 1.0
    tela = ep(t, q["c"] + 0.2, 0.25)
    if q["c"] + 0.2 < t < q["c"] + 0.6:  # pisca ao ligar
        tela *= 0.5 + 0.5 * (int(t * 30) % 2)
    zoom = lerp(2.4, 2.9, prog(t, 0, q["d"] + 4))
    c.save()
    camera(c, 960, 500, zoom)
    mundo2(c, tg, dict(luz=luz, salao=0.0, tela=tela, zoom=zoom))
    rotulo(c, "VIDRO E METAL", 850, 400, SKY, ep(t, q["b"] + 0.3, 0.35) * (1 - prog(t, q["c"] - 0.2, 0.3)), size=12)
    rotulo(c, "ACESA", 1060, 420, AMBER, ep(t, q["c"] + 0.6, 0.35) * (1 - prog(t, q["d"] - 0.2, 0.3)), size=13)
    c.restore()
    if t > q["d"]:
        a = ep(t, q["d"] + 0.4, 0.4)
        rotulo(c, "A UM PALMO DO ROSTO", W / 2, 920, CORAL, a, size=34)
    vinheta(c, 0.85)
    if t < 0.3:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", 1 - t / 0.3))


def s02(c, t, q, tg):
    u = ease_io(prog(t, 0.0, 2.6))
    zoom = lerp(2.9, 1.0, u)
    salao_luz = ease_io(prog(t, 0.4, 1.8))
    c.save()
    camera(c, 960, lerp(500, 560, u), zoom)
    mundo2(c, tg, dict(salao=salao_luz, zoom=zoom, titulo_a=1 - prog(t, q["c"] + 1.5, 0.5)))
    te0 = q["a"] + 0.6
    if t > te0:
        te = t - te0
        d = 1.5
        k = clamp(te / d)
        x = lerp(-180, 640, ease_out(k) if k < 1 else 1)
        salto = 0.0 if k >= 1 else abs(math.sin(k * math.pi * 3)) * 70 * (1 - k * 0.5)
        p = dict(face=1, look=(0.3, 0.0), smile=0.7)
        p["squash"] = (-0.08 if salto > 20 else 0.0) + 0.12 * mola(t, te0 + d, 2.6, 5.0)
        p["sway"] = 0.5 * mola(t, te0 + d, 1.8, 2.5) - (0.35 if salto > 20 else 0)
        if q["b"] <= t < q["b"] + 1.6:
            a = ep(t, q["b"], 0.25) * (1 - prog(t, q["b"] + 1.3, 0.3))
            p["arm_r"] = lerp(0.15, 2.6 + 0.3 * math.sin((t - q["b"]) * 14), a)
            p["smile"] = 1.0
        if t >= q["c"] - 0.4:
            a = ep(t, q["c"] - 0.4, 0.5)
            p["look"] = (lerp(0.3, 1.0, a), lerp(0, -0.35, a))
            p["arm_r"] = lerp(0.15, 2.0, a)
            p["brow"] = 0.6 * a
            p["tilt"] = 0.06 * a
        lume(c, x, 880 - salto, 1.25, lume_viva(tg, p, fala(tg)))
    c.restore()
    logo(c, W / 2, 175, 0.72, ep(t, q["c"] + 1.6, 0.8))
    vinheta(c, lerp(0.85, 0.6, u))


# =====================================================================
# 03 · BILHÕES DE ROSTOS ACESOS
# =====================================================================
MULTIDAO = [(170, 1.05, CORAL, 0), (380, 0.95, SKY, 2), (600, 1.1, AMBER, 1), (820, 1.0, PINK, 3), (1040, 1.08, CYAN, 4),
            (1260, 0.97, "#7be36b", 0), (1480, 1.1, CORAL, 2), (1700, 1.0, SKY, 1)]


def _rua(c, t, q, tg, n=8, conta=True):
    cidade_quente(c, tg, luzes=0.8)
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#2a1a6e", 0.25))
    for i, (x, s, cor, pl) in enumerate(MULTIDAO[:n]):
        a = ep(t, 0.2 + i * 0.12, 0.4)
        antigo(c, x, 1010 + (i % 2) * 30, s * 1.6, tg, cor, PELE[pl], olhar=1 if i % 3 else -1, a=a)
    if conta:
        k = ease_out(prog(t, q["a"] + 0.5, 2.5))
        n_ = 5.78 * k
        titulo(c, f"{n_:.2f}".replace(".", ",") + " BILHÕES", W / 2, 190, 110, AMBER, prog(t, q["a"] + 0.3, 0.5))
        rotulo(c, "USAVAM CELULAR", W / 2, 280, CYAN, ep(t, q["a"] + 2.8, 0.4), size=34)
        fonte(c, "DataReportal / GSMA Intelligence, 2026", ep(t, q["a"] + 0.5, 0.5))


def _relogio24(c, t, q, tg):
    fundo(c, "#1d2f8f", "#111b5c")
    estrelas(c, tg, 9, 50, 0.35)
    cx, cy, r = 760, 560, 320
    c.drawCircle(cx, cy, r + 16, paint(VAULT))
    c.drawCircle(cx, cy, r, paint("#fff6e8"))
    # horas acordado (16 h) em faixa clara ao redor
    acordado = ep(t, q["c"], 0.8)
    if acordado > 0:
        c.drawArc(skia.Rect.MakeLTRB(cx - r - 30, cy - r - 30, cx + r + 30, cy + r + 30), -90 + 7 * 15, 16 * 15 * acordado,
                  False, paint(AMBER, 0.9, stroke=14))
        text(c, "ACORDADO ~16 H", cx + r + 60, cy - r + 40, 26, "mono", 500, AMBER, acordado)
    k = ease_io(prog(t, q["b"] + 0.4, 2.2))
    ang = 360 * (6 + 38 / 60) / 24 * k
    pie = skia.Path()
    pie.moveTo(cx, cy)
    pie.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, ang, False)
    pie.close()
    c.drawPath(pie, paint(AZUL_TELA))
    for h_ in range(24):
        an = math.radians(h_ * 15 - 90)
        c.drawLine(cx + math.cos(an) * (r - 6), cy + math.sin(an) * (r - 6), cx + math.cos(an) * (r - 26),
                   cy + math.sin(an) * (r - 26), paint(INK, 0.6, stroke=4 if h_ % 6 == 0 else 2))
    c.drawCircle(cx, cy, 14, paint(INK))
    hh = (6 + 38 / 60) * k
    mins = int(round(hh * 60))
    titulo(c, f"{mins // 60} H {mins % 60:02d} MIN", 1440, 470, 92, AZUL_TELA, prog(t, q["b"] + 0.2, 0.5))
    text(c, "POR DIA NA INTERNET", 1440, 560, 34, "display", 700, BONE, ep(t, q["b"] + 0.6, 0.4), "center")
    text(c, "(MÉDIA DOS ADULTOS CONECTADOS)", 1440, 610, 22, "mono", 500, DUST, ep(t, q["b"] + 0.9, 0.4), "center")
    rotulo(c, "MAIS DE 1/3 DO DIA ACORDADO", 1440, 760, CORAL, ep(t, q["c"] + 1.2, 0.4), size=36)
    fonte(c, "DataReportal / GWI, Digital 2025", ep(t, q["b"], 0.5))


def _postura(c, t, q, tg):
    cidade_quente(c, tg, luzes=0.6, transito=0.4)
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#1a1050", 0.45))
    x, y, s = 860, 1180, 4.2
    antigo(c, x, y, s, tg, CORAL, PELE[1])
    rotulo(c, "PESCOÇO DOBRADO", 1380, 380, AMBER, ep(t, q["d"] + 1.6, 0.4), size=36)
    rotulo(c, "LUZ DE BAIXO PARA CIMA", 1380, 470, AZUL_TELA, ep(t, q["d"] + 2.6, 0.4), size=36)
    L(c, 1640, 1040, 1.3, tg, face=-1, look=(-0.9, -0.5), brow=0.6)


def s03(c, t, q, tg):
    partes(c, t, q, [("a", lambda: _rua(c, t, q, tg)), ("b", lambda: _relogio24(c, t, q, tg)),
                     ("d", lambda: _postura(c, t, q, tg))])


# =====================================================================
# 04 · VIBRAÇÃO FANTASMA
# =====================================================================
def ondas(c, x, y, t, a=1.0, cor=CORAL):
    for k in range(3):
        u = ((t * 2.2 + k / 3) % 1)
        c.drawCircle(x, y, 20 + u * 70, paint(cor, a * (1 - u) * 0.9, stroke=5))


def _fantasma(c, t, q, tg, fim=False):
    fundo(c, "#ffb3c8", "#ffd99a")
    chao(c, 960, "#e8879f")
    # mesa com o celular apagado
    c.drawRRect(rr(1180, 700, 520, 30, 8), paint("#8a4b2f"))
    c.drawRect(skia.Rect.MakeLTRB(1220, 730, 1240, 960), paint("#6a3520"))
    c.drawRect(skia.Rect.MakeLTRB(1640, 730, 1660, 960), paint("#6a3520"))
    celular_aceso(c, 1440, 676, 0.3, tg, 0.0, ang=90)
    pessoa(c, 700, 960, 3.2, SKY, PELE[2], cabelo="#1e1410")
    bx, by = 700 + 20 * 3.2, 960 - 62 * 3.2
    vib = t > q["a"] + 0.8
    if vib:
        ondas(c, bx, by, tg, 1.0 if not fim else 0.8)
        if fim:
            c.drawRRect(rr(bx - 26, by - 46, 52, 92, 10), paint(CORAL, 0.7, stroke=4))
    rotulo(c, "BZZZ?", bx + 170, by - 120, CORAL, ep(t, q["a"] + 1.0, 0.4) if not fim else 1.0, size=40)
    rotulo(c, "O CELULAR ESTÁ NA MESA", 1440, 600, INK, ep(t, q["a"] + 2.0, 0.4) if not fim else 0, size=28, fg=BONE)
    if fim:
        titulo(c, "VIBRAÇÃO FANTASMA", W / 2, 200, 100, "#ffffff", prog(t, q["d"] + 0.2, 0.5))
    L(c, 1820, 1040, 1.1, tg, face=-1, look=(-0.9, -0.3), brow=0.7, o_mouth=t > q["a"] + 1.0, mouth=0.3)


def _pesquisa(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    cols, rows = 29, 10
    x0, y0, d = 360, 360, 42
    vira = ease_io(prog(t, q["c"], 2.0))
    for i in range(cols * rows):
        r_, k = divmod(i, cols)
        a = prog(t, q["b"] + 0.2 + i * 0.004, 0.3)
        sim = i < 258 and (i / 258) < vira  # 89% de 290 ≈ 258
        cor = CORAL if sim else "#2e47c9"
        c.drawCircle(x0 + k * d, y0 + r_ * d, 13 * pop(a), paint(cor, clamp(a * 2)))
    rotulo(c, "290 UNIVERSITÁRIOS · 2012", W / 2, 230, "#2e47c9", ep(t, q["b"] + 0.4, 0.4), size=36)
    titulo(c, "89%", W / 2, 900, 160, CORAL, prog(t, q["c"] + 0.4, 0.5))
    text(c, "JÁ SENTIRAM O CELULAR VIBRAR SEM VIBRAR", W / 2, 990, 30, "display", 700, INK, ep(t, q["c"] + 1.2, 0.4), "center")
    fonte(c, "Drouin, Kaiser & Miller, Computers in Human Behavior, 2012", ep(t, q["b"], 0.5))


def s04(c, t, q, tg):
    partes(c, t, q, [("a", lambda: _fantasma(c, t, q, tg)), ("b", lambda: _pesquisa(c, t, q, tg)),
                     ("d", lambda: _fantasma(c, t, q, tg, fim=True))])


# =====================================================================
# 05 · HERBERT SIMON: INFORMAÇÃO DEMAIS, ATENÇÃO DE MENOS
# =====================================================================
def ampulheta(c, cx, cy, s, cheio, a=1.0):
    c.save()
    c.translate(cx, cy)
    c.scale(s, s)
    c.drawRRect(rr(-110, -170, 220, 24, 8), paint("#8a4b2f", a))
    c.drawRRect(rr(-110, 146, 220, 24, 8), paint("#8a4b2f", a))
    vidro = poly([(-90, -146), (90, -146), (14, 0), (90, 146), (-90, 146), (-14, 0)])
    c.drawPath(vidro, paint("#d6f1fa", 0.35 * a))
    c.save()
    c.clipPath(vidro, doAntiAlias=True)
    topo = -146 + (1 - cheio) * 140
    c.drawRect(skia.Rect.MakeLTRB(-90, topo, 90, 0), paint(AMBER, a))
    c.drawRect(skia.Rect.MakeLTRB(-90, 146 - (1 - cheio) * 120, 90, 146), paint(AMBER, a))
    if 0.02 < cheio < 0.98:
        c.drawRect(skia.Rect.MakeLTRB(-3, 0, 3, 146), paint(AMBER, 0.8 * a))
    c.restore()
    c.drawPath(vidro, paint("#ffffff", 0.8 * a, stroke=4))
    c.restore()


def _simon(c, t, q, tg):
    fundo(c, "#1d2f8f", "#111b5c")
    estrelas(c, tg, 5, 50, 0.3)
    c.drawRRect(rr(560, 260, 800, 460, 24), paint("#ffe9c2"))
    c.drawRRect(rr(560, 260, 800, 460, 24), paint(AMBER, stroke=6))
    pessoa(c, 780, 640, 2.0, "#2e47c9", PELE[0], cabelo="#c9c9c9")
    text(c, "HERBERT SIMON", 1150, 430, 48, "display", 800, INK, 1, "center")
    text(c, "ECONOMISTA DOS ANTIGOS", 1150, 490, 24, "mono", 500, "#6a4a2a", 1, "center")
    text(c, "1971", 1150, 590, 80, "display", 800, CORAL, 1, "center")
    a = ep(t, q["a"] + 3.0, 0.5)
    text(c, "“A riqueza de informação cria uma pobreza de atenção.”", W / 2, 800, 40, "display", 700, BONE, a, "center")
    fonte(c, "Simon, 'Designing Organizations for an Information-Rich World', 1971", a)
    L(c, 300, 1030, 1.3, tg, look=(0.8, -0.6), brow=0.6, arm_r=1.6 * ep(t, 1.0, 0.4))


def _chuva(c, t, q, tg):
    fundo(c, "#ff8fb1", "#ffc56b")
    rnd = random.Random(4)
    nomes = ["foto", "carta", "livro", "musica", "arquivo", "celular", "foto", "carta"]
    dens = prog(t, q["b"] - 0.3, 3)
    for i in range(int(70 * dens) + 1):
        x = rnd.uniform(80, W - 80)
        vel = rnd.uniform(160, 300)
        y = (rnd.uniform(0, 1400) + vel * tg) % 1400 - 200
        icone(c, nomes[i % 8], x, y, 0.7, FESTA[i % 5], 0.9)
    pessoa(c, 620, 1000, 2.6, "#2e47c9", PELE[1])
    cheio = 1 - ease_io(prog(t, q["c"] - 0.3, 3.5))
    ampulheta(c, 1330, 560, 1.4, cheio, ep(t, q["c"] - 0.5, 0.5))
    rotulo(c, "INFORMAÇÃO: ABUNDANTE", 620, 160, "#2e47c9", ep(t, q["b"] + 0.3, 0.4), size=34)
    rotulo(c, "ATENÇÃO: ESCASSA", 1330, 880, CORAL, ep(t, q["c"] + 0.4, 0.4), size=40)


def s05(c, t, q, tg):
    partes(c, t, q, [("a", lambda: _simon(c, t, q, tg)), ("b", lambda: _chuva(c, t, q, tg))])


# =====================================================================
# 06 · A ATENÇÃO VIROU O PRODUTO
# =====================================================================
def moeda(c, x, y, s=1.0, a=1.0):
    c.drawCircle(x, y, 22 * s, paint("#e0a21e", a))
    c.drawCircle(x, y, 17 * s, paint(AMBER, a))
    text(c, "$", x, y + 9 * s, 26 * s, "display", 800, "#a8700e", a, "center")


def olho(c, x, y, s=1.0, a=1.0, look=0.0):
    c.drawOval(oval(x, y, 34 * s, 22 * s), paint("#ffffff", a))
    c.drawCircle(x + look * 10 * s, y, 13 * s, paint(SKY, a))
    c.drawCircle(x + look * 10 * s, y, 6 * s, paint(INK, a))


def _vitrine_loja(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    cx, cy = W / 2, 560
    celular_aceso(c, cx, cy, 2.6, tg, 1.0, feed=1.0)
    # anunciantes em volta, pagando por cada olhar
    lados = [(380, 330), (330, 620), (440, 880), (1540, 330), (1590, 620), (1480, 880)]
    for i, (x, y) in enumerate(lados):
        a = ep(t, q["b"] + 1.4 + i * 0.15, 0.4)
        c.drawRRect(rr(x - 90, y - 60, 180, 120, 16), paint(FESTA[i % 5], a))
        text(c, "ANÚNCIO", x, y + 10, 28, "display", 800, "#ffffff", a, "center")
        if t > q["b"] + 2.5:
            u = ((tg * 0.7 + i * 0.37) % 1)
            moeda(c, lerp(x, cx, u), lerp(y, cy, u), 0.9, a * (1 - u * 0.3))
    rotulo(c, "GRÁTIS", cx + 230, 220, CYAN, ep(t, q["b"] + 0.2, 0.4) * (1 - prog(t, q["c"] - 0.3, 0.3)), size=48)
    olho(c, cx, 560 - 360, 1.6, ep(t, q["a"] + 0.5, 0.4), math.sin(tg * 2))
    rotulo(c, "A ATENÇÃO VIROU O PRODUTO", cx, 1000, CORAL, ep(t, q["a"] + 0.8, 0.4), size=36)


def _pizza(c, t, q, tg):
    fundo(c, "#1d2f8f", "#111b5c")
    cx, cy, r = 720, 560, 300
    k = ease_io(prog(t, q["c"] + 0.3, 2.0))
    c.drawCircle(cx, cy, r, paint("#3a52c4"))
    pie = skia.Path()
    pie.moveTo(cx, cy)
    pie.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * 0.976 * k, False)
    pie.close()
    c.drawPath(pie, paint(AMBER))
    c.drawCircle(cx, cy, r * 0.45, paint("#16236e"))
    titulo(c, f"{97.6 * k:.1f}%".replace(".", ","), cx, cy + 30, 84, BONE, prog(t, q["c"] + 0.2, 0.5))
    text(c, "RECEITA DA META EM 2025", 1380, 440, 36, "display", 800, BONE, ep(t, q["c"] + 0.6, 0.4), "center")
    rotulo(c, "PUBLICIDADE", 1380, 540, AMBER, ep(t, q["c"] + 1.6, 0.4), size=44)
    text(c, "US$ 196 BI DE US$ 201 BI", 1380, 640, 30, "mono", 500, DUST, ep(t, q["c"] + 2.2, 0.4), "center")
    fonte(c, "Meta Platforms, Form 10-K 2025", ep(t, q["c"], 0.5))


def _contadores(c, t, q, tg):
    fundo(c, "#ff8fb1", "#ffc56b")
    k = prog(t, q["d"], 6.0)
    for i, (rot, cor, x) in enumerate((("TEMPO OLHANDO", "#2e47c9", 640), ("ANÚNCIOS VISTOS", CORAL, 1280))):
        h = 520 * ease_out(k)
        c.drawRRect(rr(x - 110, 900 - h, 220, h, 18), paint(cor))
        rotulo(c, rot, x, 960, cor, ep(t, q["d"] + 0.3 + i * 0.4, 0.4), size=32)
        valor = int(k * (120 if i == 0 else 47))
        titulo(c, (f"{valor} MIN" if i == 0 else f"{valor}"), x, 860 - h, 70, "#ffffff", prog(t, q["d"] + 0.3, 0.4))
    L(c, 960, 1040, 1.2, tg, look=(0.0, -0.8), brow=0.5)


def s06(c, t, q, tg):
    partes(c, t, q, [("a", lambda: _vitrine_loja(c, t, q, tg)), ("c", lambda: _pizza(c, t, q, tg)),
                     ("d", lambda: _contadores(c, t, q, tg))])


# =====================================================================
# 07 · A CAIXA DE SKINNER
# =====================================================================
def rato(c, x, y, s=1.0, t=0.0, aperta=0.0, dorme=0.0, a=1.0):
    """rato fofo de perfil (olhando para a direita); aperta = pata na alavanca (0..1); dorme = deitado de olhos fechados"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    c.rotate(-8 * aperta)
    cauda = skia.Path()
    cauda.moveTo(-60, 0)
    cauda.cubicTo(-110, -10, -120, -50, -150 + 10 * math.sin(t * 3), -40)
    c.drawPath(cauda, paint("#f0a8b8", stroke=6))
    c.drawOval(oval(0, -30 + 8 * dorme, 70, 40 - 8 * dorme), paint("#c9cfe6"))
    c.drawOval(oval(-10, -18 + 8 * dorme, 50, 22), paint("#e6e9f7"))
    c.drawCircle(56, -50 + 14 * dorme, 30, paint("#c9cfe6"))
    c.drawCircle(42, -82 + 14 * dorme, 18, paint("#c9cfe6"))
    c.drawCircle(42, -82 + 14 * dorme, 10, paint("#f0a8b8"))
    c.drawCircle(84, -46 + 14 * dorme, 7, paint("#f07a96"))
    if dorme > 0.5:
        c.drawLine(58, -54 + 14 * dorme, 72, -54 + 14 * dorme, paint(INK, stroke=3))
    else:
        c.drawCircle(64, -56, 6, paint(INK))
        c.drawCircle(66, -58, 2, paint("#ffffff"))
    for wx in (-1, 1):
        c.drawLine(84, -44 + 14 * dorme, 110, -44 + wx * 10 + 14 * dorme, paint(INK, 0.5, stroke=1.5))
    # patas (a da frente sobe para a alavanca)
    c.drawRRect(rr(30 + 20 * aperta, -14 - 40 * aperta, 14, 26, 7), paint("#b8bfdc"))
    c.drawRRect(rr(-40, -14, 14, 26, 7), paint("#b8bfdc"))
    c.restore()
    c.restore()


def caixa_skinner(c, cx, cy, t, modo, q, tg, a=1.0):
    """modo 'sempre': o rato come e vai dormir; 'asvezes': aperta sem parar"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawRRect(rr(cx - 330, cy - 230, 660, 440, 22), paint("#e8f3ff"))
    c.drawRRect(rr(cx - 330, cy - 230, 660, 440, 22), paint("#2e47c9", stroke=8))
    c.drawRect(skia.Rect.MakeLTRB(cx - 322, cy + 150, cx + 322, cy + 202), paint("#b7c6ef"))
    lx, ly = cx + 200, cy + 30
    c.drawRRect(rr(lx + 40, ly - 70, 70, 120, 10), paint("#8a93c8"))   # comedouro
    if modo == "sempre":
        u = t - q["c"]
        aperta = 1.0 if 0.3 < u < 0.9 else 0.0
        dorme = ep(t, q["c"] + 2.4, 0.6)
        x = lerp(cx - 40, cx - 120, dorme)
        prato = 1.0 if 0.9 < u < 2.4 else 0.0
        rotulo(c, "COMIDA TODA VEZ", cx, cy - 290, "#2e47c9", ep(t, q["c"], 0.4), size=30)
        if dorme > 0.5:
            for k in range(3):
                zz = ((tg * 0.6 + k / 3) % 1)
                text(c, "z", x + 60 + zz * 60, cy + 40 - zz * 120, 30 + k * 6, "display", 800, "#2e47c9", 1 - zz)
    else:
        u = t - q["d"]
        aperta = 0.5 + 0.5 * math.sin(u * 16) if u > 0.3 else 0.0
        dorme = 0.0
        x = cx - 40
        cai = (u > 0.3) and ((int(u * 2.7) % 4) == 2) and t < q["d"] + 5.2
        prato = 1.0 if cai else 0.0
        rotulo(c, "COMIDA ÀS VEZES ?", cx, cy - 290, CORAL, ep(t, q["d"], 0.4), size=30)
        if t > q["d"] + 5.4:
            rotulo(c, "A COMIDA ACABOU... E ELE CONTINUA", cx, cy + 270, CORAL, ep(t, q["d"] + 5.4, 0.4), size=24)
    c.save()
    c.translate(lx, ly)
    c.rotate(20 * aperta)
    c.drawRRect(rr(-80, -8, 90, 16, 6), paint(CORAL))
    c.restore()
    c.drawCircle(lx, ly, 10, paint(INK))
    if prato:
        c.drawCircle(lx + 75, ly + 40, 14, paint("#e0a21e"))
    rato(c, x, cy + 150, 1.2, tg, aperta, dorme)
    c.restore()


def estrela(c, x, y, r, cor, a=1.0, pontas=5):
    pts = []
    for k in range(pontas * 2):
        an = -math.pi / 2 + k * math.pi / pontas
        rr_ = r if k % 2 == 0 else r * 0.45
        pts.append((x + math.cos(an) * rr_, y + math.sin(an) * rr_))
    c.drawPath(poly(pts), paint(cor, a))


def raio(c, x, y, s, cor, a=1.0):
    c.drawPath(poly([(x + 6 * s, y - 40 * s), (x - 18 * s, y + 4 * s), (x - 2 * s, y + 4 * s), (x - 8 * s, y + 40 * s),
                     (x + 18 * s, y - 6 * s), (x + 2 * s, y - 6 * s)]), paint(cor, a))


def simbolo(c, k, x, y, size, cor):
    k %= 5
    if k == 0:
        text(c, "7", x, y + size * 0.36, size, "display", 800, cor, 1, "center")
    elif k == 1:
        estrela(c, x, y, size * 0.45, cor)
    elif k == 2:
        c.drawPath(poly([(x, y - size * 0.45), (x + size * 0.33, y), (x, y + size * 0.45), (x - size * 0.33, y)]), paint(cor))
    elif k == 3:
        c.drawCircle(x, y, size * 0.32, paint(cor))
    else:
        coracao(c, x, y, size * 0.28, cor)


def caca_niquel(c, cx, cy, t, a=1.0):
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawRRect(rr(cx - 300, cy - 260, 600, 520, 40), paint(CORAL))
    c.drawRRect(rr(cx - 300, cy - 260, 600, 120, 40), paint("#ff8fa0"))
    text(c, "777", cx, cy - 175, 60, "display", 800, AMBER, 1, "center")
    for k in range(3):
        x0 = cx - 230 + k * 160
        c.drawRRect(rr(x0, cy - 100, 140, 200, 16), paint("#ffffff"))
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(x0, cy - 100, 140, 200))
        off = (t * (9 + k * 2) * 100) % 100
        for i in range(-1, 3):
            sk = int(t * (9 + k * 2)) + i + k
            simbolo(c, sk, x0 + 70, cy + i * 100 - off - 30, 80, FESTA[sk % 5])
        c.restore()
    c.drawRRect(rr(cx + 300, cy - 200, 26, 220, 12), paint("#b8bfdc"))
    c.drawCircle(cx + 313, cy - 210 + 60 * (0.5 + 0.5 * math.sin(t * 5)), 30, paint(AMBER))
    c.restore()


def s07(c, t, q, tg):
    def pergunta():
        fundo(c, "#1d2f8f", "#111b5c")
        estrelas(c, tg, 3, 50, 0.3)
        titulo(c, "Como se prende", W / 2, 440, 100, BONE, prog(t, q["a"] + 0.2, 0.5))
        titulo(c, "a atenção de alguém?", W / 2, 560, 100, AMBER, prog(t, q["a"] + 0.6, 0.5))
        L(c, 300, 1030, 1.3, tg, look=(0.8, -0.6), brow=0.8)

    def caixas():
        fundo(c, "#7ec8ff", "#d6f0ff")
        rotulo(c, "B. F. SKINNER · PSICÓLOGO", W / 2, 110, "#2e47c9", ep(t, q["b"] + 0.4, 0.4), size=34)
        if t < q["c"] - 0.2:
            caixa_skinner(c, W / 2, 580, t, "sempre", dict(q, c=1e9), tg, ep(t, q["b"] + 0.2, 0.5))
        else:
            caixa_skinner(c, 500, 600, t, "sempre", q, tg)
            caixa_skinner(c, 1420, 600, t, "asvezes", q, tg, ep(t, q["d"] - 0.3, 0.5))
        fonte(c, "Skinner, Science and Human Behavior, 1953", ep(t, q["b"], 0.5))

    def maquina_apostas():
        fundo(c, "#ff8fb1", "#ffc56b")
        caca_niquel(c, 1100, 560, tg)
        caixa_skinner(c, 0, 0, t, "asvezes", q, tg, 0)  # (mantém o mesmo estado; não desenha)
        rotulo(c, "O MESMO TRUQUE", 1100, 960, "#2e47c9", ep(t, q["e"] + 0.8, 0.4), size=36)
        rato(c, 420, 900, 2.0, tg, 0.5 + 0.5 * math.sin(tg * 16))
    partes(c, t, q, [("a", pergunta), ("b", caixas), ("e", maquina_apostas)])


# =====================================================================
# 08 · DOPAMINA: O CÉREBRO REAGE À PROMESSA
# =====================================================================
def cerebro(c, cx, cy, s=1.0, flash=0.0, a=1.0):
    c.save()
    c.translate(cx, cy)
    c.scale(s, s)
    c.drawOval(oval(0, 0, 220, 160), paint("#ff9fc0", a))
    c.drawOval(oval(-40, -30, 150, 110), paint("#ffb3cf", a))
    dob = paint("#e0709a", a, stroke=7)
    for pts in ([(-160, -40), (-100, -80), (-40, -60), (20, -100)], [(-180, 30), (-110, 0), (-40, 30), (40, -10), (120, -50)],
                [(-120, 90), (-50, 60), (30, 90), (110, 50), (170, 10)], [(40, -110), (100, -80), (170, -90)]):
        p = skia.Path()
        p.moveTo(*pts[0])
        for k in range(1, len(pts)):
            p.quadTo(pts[k - 1][0] + 20, pts[k - 1][1] - 30, *pts[k])
        c.drawPath(p, dob)
    if flash > 0:
        glow(c, 30, 40, 200, AMBER, flash)
        c.drawCircle(30, 40, 24, paint("#ffffff", flash))
    c.restore()


def linha_tempo(c, t, t0, y, sinal, flash_em, rot, cor):
    """linha do tempo: [luz] .... [gota de suco]; o flash do neurônio fica em cima de onde ele dispara"""
    a = ep(t, t0, 0.4)
    c.drawLine(360, y, 1560, y, paint(INK, 0.5 * a, stroke=4))
    if sinal:
        c.drawCircle(620, y, 46, paint(AMBER, a))
        glow(c, 620, y, 120, AMBER, 0.5 * a * (0.5 + 0.5 * math.sin(t * 6)))
        text(c, "LUZ", 620, y + 100, 26, "display", 800, INK, a, "center")
    c.drawPath(poly([(1300, y - 50), (1330, y), (1300, y + 40), (1270, y)]), paint(SKY, a))
    text(c, "SUCO", 1300, y + 100, 26, "display", 800, INK, a, "center")
    fx = 620 if flash_em == "sinal" else 1300
    pis = ep(t, t0 + 1.0, 0.3)
    glow(c, fx, y - 120, 110, CORAL, 0.8 * pis)
    raio(c, fx, y - 120, 1.3, CORAL, pis)
    rotulo(c, rot, 960, y - 190, cor, a, size=26)


def s08(c, t, q, tg):
    def cerebro_cena():
        fundo(c, "#1d2f8f", "#111b5c")
        estrelas(c, tg, 2, 40, 0.3)
        cerebro(c, W / 2, 520, 1.5, 0.6 + 0.4 * math.sin(tg * 4) if t > q["a"] + 0.8 else 0)
        rotulo(c, "NEURÔNIOS DE DOPAMINA", W / 2, 860, PINK, ep(t, q["a"] + 1.0, 0.4), size=34)
        L(c, 300, 1030, 1.3, tg, look=(0.8, -0.6), brow=0.5)

    def linhas():
        fundo(c, "#d6f0ff", "#ffffff")
        rotulo(c, "WOLFRAM SCHULTZ · 1997 · MACACOS", W / 2, 110, "#2e47c9", ep(t, q["b"] + 0.3, 0.4), size=30)
        linha_tempo(c, t, q["b"] + 0.6, 380, False, "recompensa", "RECOMPENSA INESPERADA → DISPARA NO SUCO", CORAL)
        if t > q["c"] - 0.3:
            linha_tempo(c, t, q["c"], 760, True, "sinal", "A LUZ ANUNCIA O SUCO → DISPARA NA LUZ", "#2e47c9")
        fonte(c, "Schultz, Dayan & Montague, Science, 1997", ep(t, q["b"], 0.5))

    def promessa():
        fundo(c, "#ff8fb1", "#ffc56b")
        titulo(c, "O cérebro reagia", W / 2, 260, 90, "#ffffff", prog(t, q["d"] + 0.1, 0.5))
        titulo(c, "à promessa.", W / 2, 370, 110, "#2e47c9", prog(t, q["d"] + 0.6, 0.5))
        a = ep(t, q["e"], 0.4)
        celular_aceso(c, W / 2, 720, 1.25, tg, 1.0, badge=ep(t, q["e"] + 3.2, 0.3), a=a)
        if t > q["e"] + 1.0:
            ondas(c, W / 2 - 210, 640, tg, ep(t, q["e"] + 1.0, 0.3), "#2e47c9")
            icone(c, "musica", W / 2 - 340, 640, 1.0, "#2e47c9", ep(t, q["e"] + 1.0, 0.3))
        if t > q["e"] + 2.0:
            glow(c, W / 2 + 230, 600, 120, AMBER, 0.8 * (0.5 + 0.5 * math.sin(tg * 8)))
            c.drawCircle(W / 2 + 230, 600, 22, paint(AMBER))
        L(c, 1650, 1040, 1.2, tg, face=-1, look=(-0.8, -0.4), brow=0.6)
    partes(c, t, q, [("a", cerebro_cena), ("b", linhas), ("d", promessa)])


# =====================================================================
# 09 · PUXAR PARA ATUALIZAR E O BOTÃO DE CURTIR
# =====================================================================
def mao(c, x, y, s=1.0, a=1.0):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    c.drawRRect(rr(-30, 0, 60, 120, 28), paint(PELE[0], a))
    c.drawRRect(rr(-12, -70, 26, 90, 13), paint(PELE[0], a))
    c.drawRRect(rr(-8, -66, 18, 22, 8), paint("#ffe2cc", a))
    c.restore()


def coracao(c, cx, cy, r, cor=CORAL, a=1.0):
    p = skia.Path()
    p.moveTo(cx, cy + r)
    p.cubicTo(cx - r * 1.6, cy - r * 0.2, cx - r * 0.8, cy - r * 1.4, cx, cy - r * 0.5)
    p.cubicTo(cx + r * 0.8, cy - r * 1.4, cx + r * 1.6, cy - r * 0.2, cx, cy + r)
    c.drawPath(p, paint(cor, a))


def s09(c, t, q, tg):
    def lume_cena():
        c.save()
        camera(c, 960, 560, 1.25)
        mundo2(c, tg, dict(titulo_a=0.0))
        L(c, 640, 880, 1.3, tg, face=1, look=(0.9, -0.3), brow=0.4)
        c.restore()
        rotulo(c, "QUEM DESENHOU O RETÂNGULO", W / 2, 150, AMBER, ep(t, q["a"] + 0.8, 0.4), size=40)

    def puxar():
        fundo(c, "#7ec8ff", "#d6f0ff")
        cx, cy = 760, 560
        celular_aceso(c, cx, cy, 2.9, tg, 1.0, feed=1.0)
        u = (t - q["b"]) % 2.4
        puxa = ease_io(clamp(u / 0.6)) * (1 - ease_io(clamp((u - 1.4) / 0.4)))
        # rodinha de atualizar girando como a manivela
        c.drawCircle(cx, cy - 250 + 120 * puxa, 34 * puxa, paint("#ffffff", puxa))
        c.drawArc(skia.Rect.MakeLTRB(cx - 22, cy - 272 + 120 * puxa, cx + 22, cy - 228 + 120 * puxa), tg * 600, 270, False,
                  paint("#2e47c9", puxa, stroke=6))
        mao(c, cx + 40, cy - 200 + 220 * puxa, 1.6)
        rodada = int((t - q["b"]) / 2.4)
        if u > 1.0 and t > q["b"]:
            novo = rodada % 3 != 1
            rotulo(c, "NOVIDADE!" if novo else "NADA...", 1420, 420, CYAN if novo else "#8a93c8", ep(u, 1.0, 0.3), size=48)
        rotulo(c, "PUXAR PARA ATUALIZAR · 2009", 1420, 220, "#2e47c9", ep(t, q["b"] + 0.4, 0.4), size=32)
        text(c, "LOREN BRICHTER", 1420, 300, 30, "mono", 500, INK, ep(t, q["b"] + 0.8, 0.4), "center")
        rotulo(c, "“ISSO VICIA”, DISSE ELE", 1420, 640, CORAL, ep(t, q["c"] + 0.4, 0.4), size=36)
        fonte(c, "The Guardian, 2017", ep(t, q["c"], 0.5))

    def curtir():
        fundo(c, "#ff8fb1", "#ffc56b")
        k = (t - q["d"]) % 1.6
        r = 120 * (1 + 0.25 * math.exp(-k * 5) * math.sin(k * 30))
        coracao(c, W / 2, 470, r, "#ffffff")
        coracao(c, W / 2, 470, r * 0.88, CORAL)
        rnd = random.Random(int((t - q["d"]) / 1.6))
        for i in range(14):
            an = rnd.uniform(0, 6.28)
            d = 140 + 260 * ease_out(clamp(k / 0.8))
            c.drawCircle(W / 2 + math.cos(an) * d, 470 + math.sin(an) * d, 10 * (1 - clamp(k / 1.0)), paint(FESTA[i % 5]))
        rotulo(c, "JUSTIN ROSENSTEIN · BOTÃO DE CURTIR", W / 2, 160, "#2e47c9", ep(t, q["d"] + 0.3, 0.4), size=30)
        titulo(c, "“toques brilhantes", W / 2, 800, 80, "#ffffff", prog(t, q["d"] + 2.4, 0.5))
        titulo(c, "de pseudoprazer”", W / 2, 900, 80, "#2e47c9", prog(t, q["d"] + 3.0, 0.5))
        fonte(c, "The Guardian, 2017", ep(t, q["d"], 0.5))
    partes(c, t, q, [("a", lume_cena), ("b", puxar), ("d", curtir)])


# =====================================================================
# 10 · ROLAGEM INFINITA
# =====================================================================
def pagina(c, x, y, w, h, off, fim=True, a=1.0):
    c.save()
    c.clipRRect(rr(x, y, w, h, 14), doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint("#ffffff", a))
    for k in range(40):
        yy = y + 30 + k * 150 - off
        if fim and k >= 5:
            if k == 5:
                c.drawRRect(rr(x + w / 2 - 170, yy + 10, 340, 70, 35), paint("#2e47c9", a))
                text(c, "PRÓXIMA PÁGINA ›", x + w / 2, yy + 56, 28, "display", 800, "#ffffff", a, "center")
                text(c, "FIM", x + w / 2, yy + 160, 30, "mono", 500, "#8a93c8", a, "center")
            break
        c.drawRRect(rr(x + 30, yy, w - 60, 120, 12), paint(APPS[k % 8], 0.85 * a))
        c.drawRect(skia.Rect.MakeXYWH(x + 50, yy + 84, (w - 100) * 0.6, 12), paint("#ffffff", 0.7 * a))
    c.restore()
    c.drawRRect(rr(x, y, w, h, 14), paint(INK, a, stroke=6))


def s10(c, t, q, tg):
    fundo(c, "#7ec8ff", "#d6f0ff")
    x, y, w, h = 660, 140, 600, 820
    if t < q["c"] - 0.2:
        off = 470 * ease_io(prog(t, q["b"] + 0.4, 2.0))
        pagina(c, x, y, w, h, off, True)
        rotulo(c, "ANTES: A PÁGINA TINHA FIM", 1580, 300, "#2e47c9", ep(t, q["b"] + 0.4, 0.4), size=26)
        if t > q["b"] + 2.6:
            L(c, 1560, 900, 1.1, tg, face=-1, look=(-0.9, 0.0), brow=0.7, arm_l=1.4)
            rotulo(c, "MAIS?", 1560, 560, AMBER, ep(t, q["b"] + 2.8, 0.4), size=40)
    else:
        u = t - (q["c"] - 0.2)
        vel = 300 + 900 * prog(u, 0, 4)
        off = 470 + u * vel
        pagina(c, x, y, w, h, off % 600 + 300, False)
        # o fundo some: as bordas da página descem para um poço
        c.drawRect(skia.Rect.MakeLTRB(x, y + h - 120, x + w, y + h), linear(0, y + h - 120, 0, y + h, [("#070c38", 0), ("#070c38", 0.7)]))
        rotulo(c, "SEM FUNDO", 1580, 300, CORAL, ep(t, q["c"] + 1.5, 0.4), size=36)
        if t > q["d"]:
            rotulo(c, "AZA RASKIN SE ARREPENDEU", 1580, 420, "#2e47c9", ep(t, q["d"] + 0.6, 0.4), size=24)
    rotulo(c, "ROLAGEM INFINITA · 2006", 380, 300, AMBER, ep(t, q["a"] + 0.5, 0.4), size=30)
    text(c, "AZA RASKIN", 380, 380, 30, "mono", 500, INK, ep(t, q["a"] + 0.9, 0.4), "center")
    fonte(c, "Masters of Scale · BBC, 2018", ep(t, q["a"], 0.5))


# =====================================================================
# 11 · NOTIFICAÇÕES: A SEMANA BARULHENTA E A SILENCIOSA
# =====================================================================
def sino(c, x, y, s=1.0, cor=AMBER, a=1.0, ang=0.0, riscado=False):
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(s, s)
    p = skia.Path()
    p.moveTo(-34, 20)
    p.cubicTo(-30, -10, -30, -40, 0, -44)
    p.cubicTo(30, -40, 30, -10, 34, 20)
    p.close()
    c.drawPath(p, paint(cor, a))
    c.drawRRect(rr(-40, 16, 80, 10, 5), paint(cor, a))
    c.drawCircle(0, 32, 8, paint(cor, a))
    c.restore()
    if riscado:
        c.drawLine(x - 50 * s, y - 50 * s, x + 50 * s, y + 50 * s, paint(CORAL, a, stroke=10 * s))


def s11(c, t, q, tg):
    def chamando():
        fundo(c, "#1d2f8f", "#111b5c")
        celular_aceso(c, W / 2, 560, 2.2, tg, 1.0, badge=1.0, ang=6 * math.sin(tg * 40) * (0.5 + 0.5 * math.sin(tg * 2)))
        ondas(c, W / 2, 560, tg, 0.9, AMBER)
        sino(c, W / 2 + 330, 340, 1.5, AMBER, ep(t, q["a"] + 0.4, 0.4), 15 * math.sin(tg * 12))
        titulo(c, "Ele chamava.", W / 2, 960, 90, AMBER, prog(t, q["a"] + 1.8, 0.5))

    def semanas():
        fundo(c, "#d6f0ff", "#ffffff")
        for i, (x, rot, cor) in enumerate(((520, "SEMANA BARULHENTA", CORAL), (1400, "SEMANA SILENCIOSA", "#2e47c9"))):
            a = ep(t, q["b"] + 0.5 + i * 2.5, 0.5)
            c.drawRRect(rr(x - 380, 230, 760, 560, 28), paint(cor, 0.12 * a))
            c.drawRRect(rr(x - 380, 230, 760, 560, 28), paint(cor, a, stroke=6))
            rotulo(c, rot, x, 230, cor, a, size=32)
            if i == 0:
                pessoa(c, x - 120, 700, 2.0, CORAL, PELE[0], braco=1.25, a=a)
                celular_aceso(c, x - 120 + 66 * 2, 700 - 106 * 2, 0.35, tg, 1.0, badge=1.0, a=a)
                for k in range(4):
                    sino(c, x + 120 + (k % 2) * 110, 360 + k * 90, 0.7, AMBER, a * (0.5 + 0.5 * math.sin(tg * 9 + k)),
                         20 * math.sin(tg * 14 + k))
            else:
                pessoa(c, x - 120, 700, 2.0, "#2e47c9", PELE[2], a=a)
                c.drawRRect(rr(x + 40, 520, 240, 160, 12), paint("#8a4b2f", a))
                c.drawRRect(rr(x + 60, 540, 200, 24, 8), paint("#6a3520", a))
                celular_aceso(c, x + 160, 610, 0.3, tg, 0.0, ang=90, a=a)
                sino(c, x + 160, 380, 0.9, "#8a93c8", a, 0, True)
            # medidor de desatenção
            if t > q["c"] - 0.2:
                h = (130 if i == 0 else 60) * ease_out(prog(t, q["c"] + i * 0.5, 1.0))
                c.drawRRect(rr(x - 160, 830, 320, 36, 18), paint(cor, 0.2))
                c.drawRRect(rr(x - 160, 830, 320 * h / 130, 36, 18), paint(cor))
        text(c, "DESATENÇÃO", 960, 858, 26, "mono", 500, INK, ep(t, q["c"], 0.4), "center")
        rotulo(c, "MAIS DESATENÇÃO E AGITAÇÃO", 960, 960, CORAL, ep(t, q["c"] + 1.2, 0.4), size=30)
        text(c, "221 UNIVERSITÁRIOS · CANADÁ", 960, 160, 28, "mono", 500, INK, ep(t, q["b"] + 0.4, 0.4), "center")
        fonte(c, "Kushlev, Proulx & Dunn, CHI 2016", ep(t, q["b"], 0.5))

    def ambiente():
        fundo(c, "#ff8fb1", "#ffc56b")
        titulo(c, "Não era doença.", W / 2, 420, 100, "#ffffff", prog(t, q["d"] + 0.1, 0.5))
        titulo(c, "Era o ambiente.", W / 2, 560, 110, "#2e47c9", prog(t, q["d"] + 1.0, 0.5))
        L(c, W / 2, 1000, 1.3, tg, look=(0.0, -0.4), smile=0.8)
    partes(c, t, q, [("a", chamando), ("b", semanas), ("d", ambiente)])


# =====================================================================
# 12 · DOIS MINUTOS E MEIO → QUARENTA E SETE SEGUNDOS
# =====================================================================
def cronometro(c, cx, cy, r, seg, a=1.0, cor=CORAL):
    c.drawCircle(cx, cy, r + 10, paint(INK, a))
    c.drawCircle(cx, cy, r, paint("#ffffff", a))
    c.drawRRect(rr(cx - 18, cy - r - 44, 36, 30, 8), paint(INK, a))
    an = math.radians(seg / 60 * 360 - 90)
    c.drawLine(cx, cy, cx + math.cos(an) * r * 0.82, cy + math.sin(an) * r * 0.82, paint(cor, a, stroke=7))
    c.drawCircle(cx, cy, 9, paint(INK, a))
    m, s_ = divmod(int(seg), 60)
    text(c, f"{m}:{s_:02d}", cx, cy + r + 70, 52, "display", 800, INK, a, "center")


def janelas(c, x, y, w, h, k, cores, a=1.0):
    cor = cores[k % len(cores)]
    c.drawRRect(rr(x, y, w, h, 16), paint("#ffffff", a))
    c.drawRRect(rr(x, y, w, 46, 16), paint(cor, a))
    for i in range(4):
        c.drawRect(skia.Rect.MakeXYWH(x + 30, y + 80 + i * 48, w * (0.4 + 0.12 * ((k + i) % 4)), 18), paint(cor, 0.4 * a))


def s12(c, t, q, tg):
    def escritorio(seg, troca, rot, cor):
        fundo(c, "#7ec8ff", "#d6f0ff")
        c.drawRRect(rr(380, 230, 700, 470, 24), paint(INK))
        janelas(c, 410, 260, 640, 410, troca, [SKY, CORAL, AMBER, CYAN, PINK])
        c.drawRect(skia.Rect.MakeLTRB(690, 700, 770, 780), paint(INK))
        c.drawRRect(rr(580, 770, 300, 24, 10), paint(INK))
        cronometro(c, 1450, 470, 170, seg, 1.0, cor)
        rotulo(c, rot, 1450, 220, cor, 1, size=36)

    def intro():
        fundo(c, "#7ec8ff", "#d6f0ff")
        pessoa(c, 760, 1000, 2.6, "#2e47c9", PELE[0], braco=1.2)
        c.drawRRect(rr(880, 470, 520, 360, 20), paint(INK))
        janelas(c, 900, 490, 480, 300, int(tg) % 5, [SKY, CORAL, AMBER, CYAN, PINK])
        rotulo(c, "GLORIA MARK · PSICÓLOGA", W / 2, 150, "#2e47c9", ep(t, q["a"] + 0.4, 0.4), size=34)
        cronometro(c, 1600, 330, 90, (tg * 4) % 60, ep(t, q["a"] + 1.4, 0.4))
        fonte(c, "Gloria Mark, 'Attention Span', 2023", ep(t, q["a"], 0.5))

    def ano2004():
        u = max(0.0, t - q["b"] - 0.3)
        seg = min(150.0, u * 30)
        escritorio(seg, 0 if seg < 150 else 1, "2004", "#2e47c9")

    def hoje():
        u = max(0.0, t - q["c"] - 0.3)
        per = 47 / 30  # ~1,6 s por troca na tela (47 s acelerados)
        seg = (u % per) / per * 47
        escritorio(seg, int(u / per) + 2, "A PARTIR DE 2016", CORAL)
        rotulo(c, "~47 SEGUNDOS", 1450, 930, CORAL, ep(t, q["c"] + 1.6, 0.4), size=40)

    def pingue():
        fundo(c, "#ff8fb1", "#ffc56b")
        for i, x in enumerate((360, 960, 1560)):
            janelas(c, x - 230, 380, 460, 320, i, [SKY, CORAL, AMBER])
        u = (t - q["d"]) * 1.4
        k = int(u) % 4
        f = u % 1
        xs = [360, 960, 1560, 960]
        x = lerp(xs[k], xs[(k + 1) % 4], f)
        y = 330 - 220 * math.sin(f * math.pi)
        c.drawOval(oval(x, 760, 40 * (1 - 0.4 * math.sin(f * math.pi)), 10), paint(INK, 0.3))
        c.drawCircle(x, y, 34, paint("#ffffff"))
        c.drawCircle(x - 10, y - 10, 10, paint("#ffffff", 0.6))
        c.drawCircle(x, y, 34, paint("#f0a030", stroke=4))
        titulo(c, "Atenção de pingue-pongue", W / 2, 960, 80, "#2e47c9", prog(t, q["d"] + 1.2, 0.5))
    partes(c, t, q, [("a", intro), ("b", ano2004), ("c", hoje), ("d", pingue)])


# =====================================================================
# 13 · O ABISMO: ELES SABIAM
# =====================================================================
def cartao_citacao(c, linhas, autor, fonte_txt, a, cor=AMBER):
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.drawRRect(rr(260, 230, 1400, 560, 30), paint("#0c1550", 0.92))
    c.drawRRect(rr(260, 230, 1400, 560, 30), paint(cor, stroke=5))
    text(c, "“", 330, 400, 200, "display", 800, cor, 1)
    for i, s_ in enumerate(linhas):
        text(c, s_, W / 2, 420 + i * 90, 64, "display", 800, BONE if i < len(linhas) - 1 else cor, 1, "center")
    text(c, autor, W / 2, 740, 28, "mono", 500, DUST, 1, "center", tracking=0.06)
    c.restore()
    fonte(c, fonte_txt, a)


def s13(c, t, q, tg):
    def museu():
        z = lerp(1.15, 1.4, ease_io(prog(t, 0, 6)))
        c.save()
        camera(c, 860, 600, z)
        mundo2(c, tg, dict(titulo_a=0.0, luz=0.7, salao=0.55))
        L(c, 640, 880, 1.3, tg, face=1, look=(0.9, -0.3), brow=-0.3)
        c.restore()
        vinheta(c, 0.8)

    def jobs():
        museu()
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.5))
        cartao_citacao(c, ["Eles ainda não usaram.", "Nós limitamos quanta tecnologia", "nossos filhos usam em casa."],
                       "— STEVE JOBS, CHEFE DA APPLE, SOBRE O iPAD (FIM DE 2010)", "The New York Times, 2014",
                       ep(t, q["b"] + 0.4, 0.5))

    def harris():
        museu()
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.5))
        cartao_citacao(c, ["Todas as nossas mentes", "podem ser sequestradas."],
                       "— TRISTAN HARRIS, EX-FUNCIONÁRIO DO GOOGLE", "The Guardian, 2017", 1.0, CORAL)

    def alvo():
        fundo(c, "#111b5c", "#070c38")
        # o celular visto de trás: do outro lado, um placar subindo
        celular_aceso(c, 560, 470, 2.0, tg, 1.0, feed=1.0)
        k = prog(t, q["e"], 12)
        c.drawRRect(rr(980, 230, 760, 420, 26), paint("#0c1550"))
        c.drawRRect(rr(980, 230, 760, 420, 26), paint(CORAL, stroke=5))
        text(c, "TEMPO OLHANDO", 1360, 320, 40, "display", 800, CORAL, 1, "center")
        horas = 6 + 38 / 60 + k * 2
        text(c, f"{int(horas)}:{int(horas % 1 * 60):02d}:{int(tg * 60) % 60:02d}", 1360, 480, 110, "mono", 500, BONE, 1, "center")
        for i in range(8):
            c.drawRect(skia.Rect.MakeXYWH(1030 + i * 85, 625, 60, -20 - 20 * ((i + int(tg * 3)) % 4)), paint(AMBER, 0.7))
        titulo(c, "Não eram fracos. Eram o alvo.", W / 2, 920, 84, AMBER, prog(t, q["e"] + 0.8, 0.5))
    partes(c, t, q, [("a", museu), ("b", jobs), ("d", harris), ("e", alvo)])


# =====================================================================
# 14 · A VIRADA: QUATRO SEMANAS SEM FACEBOOK
# =====================================================================
def calendario(c, cx, cy, folha, a=1.0):
    c.drawRRect(rr(cx - 150, cy - 160, 300, 320, 20), paint("#ffffff", a))
    c.drawRRect(rr(cx - 150, cy - 160, 300, 80, 20), paint(CORAL, a))
    text(c, "SEMANA", cx, cy - 106, 30, "display", 800, "#ffffff", a, "center")
    text(c, str(folha), cx, cy + 90, 150, "display", 800, INK, a, "center")


def mesa_familia(c, t, a=1.0):
    for i, (x, cor, pl, cab) in enumerate(((560, CORAL, 0, "#3a2416"), (780, SKY, 3, "#1e1410"), (1140, AMBER, 1, "#6a3a1a"),
                                          (1360, CYAN, 2, "#2a1a10"))):
        pessoa(c, x, 880, 2.1 if i != 1 else 1.6, cor, PELE[pl], cabelo=cab, braco=0.4 + 0.3 * math.sin(t * 2 + i),
               a=a, olhar=1 if x < 960 else -1)
    c.drawRRect(rr(440, 690, 1040, 40, 12), paint("#8a4b2f", a))
    for lx in (480, 1420):
        c.drawRect(skia.Rect.MakeLTRB(lx, 730, lx + 24, 900), paint("#6a3520", a))
    for k in range(4):
        c.drawOval(oval(640 + k * 210, 684, 50, 12), paint("#ffffff", a))
        c.drawOval(oval(640 + k * 210, 680, 30, 7), paint(FESTA[k], a))


def s14(c, t, q, tg):
    def lume_luz():
        c.save()
        camera(c, 860, 600, 1.3)
        mundo2(c, tg, dict(titulo_a=0.0, luz=lerp(0.7, 1.0, ep(t, 0.5, 2.0)), salao=lerp(0.55, 1.0, ep(t, 0.5, 2.0))))
        L(c, 640, 880, 1.3, tg, face=1, look=(0.9, -0.4), smile=0.9, brow=0.5, arm_r=2.0 * ep(t, q["a"] + 2.0, 0.5))
        c.restore()
        rotulo(c, "A SAÍDA", W / 2, 150, CYAN, ep(t, q["a"] + 2.2, 0.4), size=44)

    def desativa():
        fundo(c, "#7ec8ff", "#d6f0ff")
        celular_aceso(c, 620, 560, 2.2, tg, 1.0 - 0.8 * ep(t, q["b"] + 2.2, 0.4))
        rotulo(c, "DESATIVAR CONTA", 620, 560, CORAL, ep(t, q["b"] + 1.2, 0.4), size=30)
        if t > q["b"] + 2.0:
            icone(c, "check", 620, 720, 1.4, None, prog(t, q["b"] + 2.0, 0.4))
        folha = 1 + min(3, int(max(0.0, t - q["b"] - 2.8) / 0.7))
        calendario(c, 1350, 540, folha, ep(t, q["b"] + 2.6, 0.4))
        rotulo(c, "4 SEMANAS · PAGOS PARA SAIR", 1350, 820, "#2e47c9", ep(t, q["b"] + 3.6, 0.4), size=28)
        fonte(c, "Allcott et al., American Economic Review, 2020", ep(t, q["b"], 0.5))

    def familia():
        fundo(c, "#ff8fb1", "#ffc56b")
        mesa_familia(c, tg)
        rotulo(c, "MAIS TEMPO COM FAMÍLIA E AMIGOS", W / 2, 180, "#2e47c9", ep(t, q["c"] + 0.4, 0.4), size=34)
        rotulo(c, "BEM-ESTAR: UM POUCO MELHOR", W / 2, 280, CYAN, ep(t, q["c"] + 2.6, 0.4), size=30)

    def depois():
        fundo(c, "#d6f0ff", "#ffffff")
        for i, (rot, h, cor) in enumerate((("ANTES", 420, "#8a93c8"), ("DEPOIS DO EXPERIMENTO", 260, CYAN))):
            x = 720 + i * 480
            hh = h * ease_out(prog(t, q["d"] + 0.3 + i * 0.6, 0.8))
            c.drawRRect(rr(x - 100, 860 - hh, 200, hh, 16), paint(cor))
            rotulo(c, rot, x, 920, cor if i else "#2e47c9", ep(t, q["d"] + 0.3 + i * 0.6, 0.4), size=26)
        text(c, "USO DO FACEBOOK", W / 2, 260, 44, "display", 800, INK, ep(t, q["d"], 0.4), "center")
        L(c, 1620, 1040, 1.2, tg, face=-1, look=(-0.8, -0.4), smile=1.0)
    partes(c, t, q, [("a", lume_luz), ("b", desativa), ("c", familia), ("d", depois)])


# =====================================================================
# 15 · NOVAS REGRAS: BRASIL E AUSTRÁLIA
# =====================================================================
def s15(c, t, q, tg):
    def mapa():
        fundo(c, "#1d2f8f", "#111b5c")
        estrelas(c, tg, 6, 80, 0.4)
        rot = lerp(60, 60, 0) if t < q["c"] else lerp(60, -150, ease_io(prog(t, q["c"], 1.6)))
        globo(c, W / 2, 560, 330, rot)
        # Brasil (~ -50, -10) e Austrália (~ 135, -25)
        for lon, lat, cue, rot_, sub in ((-50, -10, "b", "BRASIL · JAN 2025", "CELULAR RESTRITO NAS ESCOLAS, ATÉ NO RECREIO"),
                                         (135, -25, "c", "AUSTRÁLIA · DEZ 2025", "MENORES DE 16 SEM CONTA NAS REDES")):
            lo, la = math.radians(lon + rot), math.radians(lat)
            if math.cos(la) * math.cos(lo) <= 0.1:
                continue
            x, y = W / 2 + 330 * math.cos(la) * math.sin(lo), 560 - 330 * math.sin(la)
            a = ep(t, q[cue] + 0.5, 0.4)
            glow(c, x, y, 80, AMBER, 0.8 * a)
            c.drawCircle(x, y, 16 * pop(a), paint(AMBER))
            rotulo(c, rot_, W / 2, 140, AMBER if cue == "b" else CYAN, a, size=40)
            text(c, sub, W / 2, 230, 30, "display", 700, BONE, ep(t, q[cue] + 1.2, 0.4), "center")
        fontes_ = "Lei 15.100/2025 · Agência Senado" if t < q["c"] else "Online Safety Amendment (Social Media Minimum Age) Act"
        fonte(c, fontes_, ep(t, q["b"], 0.5))
        L(c, 300, 1030, 1.2, tg, look=(0.8, -0.6), brow=0.5)

    def patio():
        fundo(c, "#7ec8ff", "#d6f0ff")
        c.drawRect(skia.Rect.MakeLTRB(0, 700, W, H), paint("#3fd17a"))
        c.drawRect(skia.Rect.MakeLTRB(0, 700, W, 712), paint("#7be36b"))
        for i, x in enumerate((360, 620, 900, 1240, 1520)):
            pulo = abs(math.sin(tg * 3 + i)) * 40 if i % 2 == 0 else 0
            pessoa(c, x, 900 - pulo, 1.4, FESTA[i % 5], PELE[i % 5], braco=1.0 + 0.8 * math.sin(tg * 4 + i))
        bx = 1060 + 260 * math.sin(tg * 1.7)
        c.drawCircle(bx, 620 - abs(math.sin(tg * 3.4)) * 200, 28, paint("#ffffff"))
        titulo(c, "Redesenhando o ambiente", W / 2, 230, 90, "#2e47c9", prog(t, q["d"] + 1.6, 0.5))
    partes(c, t, q, [("a", mapa), ("d", patio)])


# =====================================================================
# 16 · QUEM DECIDE QUANDO ELE CHAMA
# =====================================================================
def s16(c, t, q, tg):
    def silencio():
        fundo(c, "#d6f0ff", "#ffffff")
        k = ease_io(prog(t, q["a"] + 2.5, 1.2))
        c.drawRRect(rr(1100, 640, 560, 280, 20), paint("#8a4b2f"))
        c.drawRRect(rr(1130, 600 - 0, 500, 60, 14), paint("#a85a35"))
        celular_aceso(c, lerp(700, 1380, k), lerp(520, 640, k), lerp(1.8, 0.6, k), tg, 1 - k, ang=lerp(0, 90, k))
        sino(c, 700, 200, 1.4, "#8a93c8", ep(t, q["a"] + 1.0, 0.4), 0, True)
        rotulo(c, "SILENCIAR", 960, 200, "#2e47c9", ep(t, q["a"] + 1.0, 0.4), size=34)
        rotulo(c, "LONGE DA MÃO", 1380, 520, CORAL, ep(t, q["a"] + 3.0, 0.4), size=34)
        fonte(c, "Kushlev et al., CHI 2016", ep(t, q["a"], 0.5))

    def ferramenta():
        fundo(c, "#ff8fb1", "#ffc56b")
        celular_aceso(c, W / 2, 560, 2.6, tg, 1.0)
        # o que o retângulo guardava de bom
        for i, (nome, x, y) in enumerate((("foto", 520, 360), ("musica", 1400, 360), ("carta", 520, 760), ("pessoa", 1400, 760))):
            a = ep(t, q["b"] + 1.6 + i * 0.6, 0.4)
            c.drawCircle(x, y, 90 * pop(a), paint("#ffffff", 0.85 * a))
            icone(c, nome, x, y, 1.3, FESTA[i % 5], a)
        rotulo(c, "MAPAS · MÚSICAS · VOZES", W / 2, 990, "#2e47c9", ep(t, q["b"] + 2.0, 0.4), size=34)

    def quem():
        fundo(c, "#1d2f8f", "#111b5c")
        celular_aceso(c, 620, 560, 1.8, tg, 1.0, badge=1.0)
        mao(c, 620, 860, 2.0)
        titulo(c, "Quem decide", 1300, 480, 90, BONE, prog(t, q["c"] + 0.2, 0.5))
        titulo(c, "quando ele chama?", 1300, 590, 90, AMBER, prog(t, q["c"] + 0.7, 0.5))
        L(c, 1300, 980, 1.2, tg, look=(0.0, -0.4), smile=0.9, arm_r=1.8 * ep(t, q["d"], 0.5))
        rotulo(c, "OS ANTIGOS PODIAM TOMAR DE VOLTA", 1300, 760, CYAN, ep(t, q["d"] + 0.8, 0.4), size=30)
    partes(c, t, q, [("a", silencio), ("b", ferramenta), ("c", quem)])


# =====================================================================
# 17 · A ETIQUETA · 18 · A PRÓXIMA PEÇA
# =====================================================================
def s17(c, t, q, tg):
    c.save()
    camera(c, 960, 560, 1.3)
    mundo2(c, tg, dict(titulo_a=0.0, tela=1 - ep(t, q["a"] + 0.6, 0.5)))
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
    linhas = [("PEÇA Nº 002", q["a"] + 1.8, 34),
              ("Retângulo brilhante.", q["b"], 40),
              ("Século 21 d.C.", q["b"] + 1.4, 40),
              ("Foi desenhado para nunca acabar.", q["c"], 40),
              ("Os Antigos aprenderam a pôr um fim.", q["d"], 44)]
    for i, (s_, t0, size) in enumerate(linhas):
        k = prog(t, t0, len(s_) * 0.045)
        y = -280 + [0, 110, 170, 320, 450][i]
        cor = "#3a2c18" if i < 4 else "#b5381e"
        text(c, maquina(s_, k), -560, y, size, "mono", 500, cor, a)
    c.restore()


def nota_dinheiro(c, cx, cy, s, a=1.0):
    c.save()
    c.translate(cx, cy)
    c.rotate(-8)
    c.scale(s, s)
    c.drawRRect(rr(-110, -52, 220, 104, 10), paint("#3fd17a", a))
    c.drawRRect(rr(-100, -42, 200, 84, 8), paint("#ffffff", 0.35 * a, stroke=3))
    c.drawCircle(0, 0, 28, paint("#ffffff", 0.4 * a))
    c.restore()


def s18(c, t, q, tg):
    pan = ease_io(prog(t, 0.2, 3.0))
    c.save()
    camera(c, lerp(960, 1590, pan), 560, lerp(1.2, 1.7, pan))
    mundo2(c, tg, dict(titulo_a=0.0, tela=0.0))
    vx, top = 1590, 610
    pano = skia.Path()
    pano.moveTo(vx - 135, top + 20)
    pano.cubicTo(vx - 150, top - 120, vx - 110, top - 230, vx, top - 225)
    pano.cubicTo(vx + 110, top - 230, vx + 150, top - 120, vx + 135, top + 20)
    for k in range(6):
        pano.lineTo(vx + 135 - k * 54, top + 20 + (12 if k % 2 else 0))
    pano.close()
    pulsa = 0.6 + 0.4 * math.sin(tg * 2.5)
    glow(c, vx, top - 100, 220, "#3fd17a", 0.4 * pulsa)
    c.drawPath(pano, paint(CORAL))
    c.drawPath(pano, paint("#d94a5e", stroke=4))
    c.saveLayerAlpha(None, int(255 * 0.35 * pulsa))
    nota_dinheiro(c, vx, top - 110, 0.55)
    c.restore()
    x = lerp(1300, 1430, ep(t, 0.6, 2.0))
    L(c, x, 880, 1.05, tg, face=1, look=(0.8, -0.5), brow=0.7, arm_r=1.6 * ep(t, 2.6, 0.5))
    c.restore()
    rotulo(c, "PRÓXIMA PEÇA · Nº 003", W / 2, 120, AMBER, ep(t, q["a"] + 1.0, 0.4), size=40)
    if t > q["b"] - 0.2:
        a = ep(t, q["b"] - 0.2, 0.5)
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#070c38", 0.6 * a))
        titulo(c, "Quanto tempo de tela o seu", W / 2, 430, 80, BONE, prog(t, q["b"] + 0.6, 0.5))
        titulo(c, "celular marcou ontem?", W / 2, 540, 80, AMBER, prog(t, q["b"] + 1.0, 0.5))
        rotulo(c, "CONTA NOS COMENTÁRIOS", W / 2, 700, CYAN, ep(t, q["c"] + 0.2, 0.4), size=40)
    fim = TOTAL - (CENAS[-1]["start"])
    logo(c, W / 2, 900, 0.7, ep(t, fim - 3.5, 0.8))
    if t > fim - 1.0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", prog(t, fim - 1.0, 1.0)))


# =====================================================================
# QUADRO
# =====================================================================
FUNCS = {f"{k:02d}": globals()[f"s{k:02d}"] for k in range(1, 19)}


def cena_em(tg):
    for i, s in enumerate(CENAS):
        if s["start"] <= tg < s["end"]:
            return i
    return len(CENAS) - 1


def desenha(c, i, tg):
    s = CENAS[i]
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
                        str(out / "video_mudo.mp4")], check=True)
        print("ok", out / "video_mudo.mp4")


if __name__ == "__main__":
    main()
