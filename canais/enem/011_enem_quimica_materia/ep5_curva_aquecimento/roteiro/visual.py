"""Visual — Matéria, Substâncias e Misturas, Episódio 5: A curva de aquecimento (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha/faixa · verde = patamar/atalho · vermelho = erro.
Reaproveita peças do ep. 1 (V: béquer, chama, termômetro…) e do ep. 4 (V4: cubos de gelo).
Peças próprias deste episódio:
- grafico(): temperatura × tempo desenhado até uma fração; patamares (trechos deitados) em verde, faixas em âmbar.
- experimento(): béquer no fogo com gelo derretendo, água fervendo e termômetro que "trava" nos patamares,
  sincronizado com o gráfico sendo desenhado em tempo real.
- pedágio: a cabine com cancela pousada sobre o patamar.
"""
import importlib.util
import json
import math
import random
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_BASE = Path(__file__).resolve().parents[2]


def _load(nome, rel):
    spec = importlib.util.spec_from_file_location(nome, _BASE / rel / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V = _load("visual_quimica_ep1", "ep1_materia_e_substancias")
V4 = _load("visual_quimica_ep4", "ep4_fases_componentes")

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep5_curva_aquecimento.mp4"
CARD_R = (140, 150, 1640, 690)
WATER = "#7FB2F0"
DARK_AMBER = "#B07A00"

# curvas normalizadas (x = tempo 0..1, y = temperatura 0..1)
PURA = [(0, 0.08), (0.18, 0.3), (0.4, 0.3), (0.58, 0.72), (0.8, 0.72), (0.96, 0.92)]
COMUM = [(0, 0.08), (0.18, 0.26), (0.4, 0.38), (0.58, 0.66), (0.8, 0.8), (0.96, 0.95)]
EUT = [(0, 0.08), (0.18, 0.3), (0.4, 0.3), (0.58, 0.66), (0.8, 0.8), (0.96, 0.95)]
AZEO = [(0, 0.08), (0.18, 0.26), (0.4, 0.38), (0.58, 0.72), (0.8, 0.72), (0.96, 0.92)]


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


def keyframes(t, ks):
    """ks = [(instante, valor)] crescentes -> valor interpolado"""
    if t <= ks[0][0]:
        return ks[0][1]
    for (t0, v0), (t1, v1) in zip(ks, ks[1:]):
        if t <= t1:
            return lerp(v0, v1, (t - t0) / max(1e-6, t1 - t0))
    return ks[-1][1]


def y_at(pts, x):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return lerp(y0, y1, (x - x0) / max(1e-6, x1 - x0))
    return pts[-1][1]


# ======================================================================
# gráfico temperatura × tempo
# ======================================================================

def eixos(c, x, y, w, h, a, xl="tempo", yl="temperatura", size=24):
    if a <= 0:
        return
    arrow(c, x, y + h, x + w + 20, y + h, INK2, a, 4, 14)
    arrow(c, x, y + h, x, y - 20, INK2, a, 4, 14)
    text(c, xl, x + w, y + h + 40, size, "bold", INK2, a, align="right")
    text(c, yl, x + 14, y - 8, size, "bold", INK2, a, align="left")


def grafico(c, x, y, w, h, a, pts, frac=1.0, col=INK, marcas=(), size=24, eixo=True, destaque=True, larg=6, xl="tempo", yl="temperatura"):
    """marcas = [(yfrac, rótulo, cor)] linhas tracejadas horizontais (PF, PE…)"""
    if a <= 0:
        return
    if eixo:
        eixos(c, x, y, w, h, a, xl, yl, size)
    for yf, lab, mc in marcas:
        yy = y + h * (1 - yf)
        line(c, x, yy, x + w, yy, mc, a * 0.7, 2, dash=[8, 8])
        text_mid(c, lab, x - 12, yy, size * 0.9, "black", mc, a, align="right")
    X = lambda u: x + w * u
    Y = lambda v: y + h * (1 - v)
    p = skia.Path()
    p.moveTo(X(pts[0][0]), Y(pts[0][1]))
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if frac <= x0:
            break
        u = min(1.0, (frac - x0) / (x1 - x0))
        p.lineTo(X(lerp(x0, x1, u)), Y(lerp(y0, y1, u)))
    c.drawPath(p, paint(col, a, stroke=larg, cap_round=True))
    if destaque:
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if frac <= x0:
                break
            u = min(1.0, (frac - x0) / (x1 - x0))
            xe = lerp(x0, x1, u)
            if abs(y1 - y0) < 1e-6:          # patamar
                line(c, X(x0), Y(y0), X(xe), Y(y0), GREEN, a, larg * 1.9)
            elif 0.05 < (y1 - y0) / (x1 - x0) < 0.9:   # faixa (sobe devagar)
                line(c, X(x0), Y(y0), X(xe), Y(lerp(y0, y1, u)), AMBER, a, larg * 1.6)


def patamar_rotulo(c, x, y, w, h, pts, k, s, a, col=GREEN, dy=-34, size=22):
    """rótulo sobre o k-ésimo trecho de pts"""
    if a <= 0:
        return
    (x0, y0), (x1, y1) = pts[k], pts[k + 1]
    cx = x + w * (x0 + x1) / 2
    cy = y + h * (1 - (y0 + y1) / 2)
    pill(c, s, cx, cy + dy, col, size=size, fg=INK if col == AMBER else None, a=a, anchor="center", bounds=(0, 1920))


def cabine(c, cx, by, a, aberta=0.0, s=1.0):
    """cabine de pedágio com cancela (aberta 0..1)"""
    if a <= 0:
        return
    rrect(c, cx - 26 * s, by - 70 * s, 52 * s, 70 * s, 6 * s, "#FFFFFF", a, shadow=True, stroke=3, stroke_color=INK2)
    rrect(c, cx - 34 * s, by - 84 * s, 68 * s, 16 * s, 5 * s, RED, a)
    rrect(c, cx - 16 * s, by - 58 * s, 32 * s, 22 * s, 4 * s, "#CFE6FA", a)
    ang = -80 * ease_io(aberta)
    c.save(); c.translate(cx + 26 * s, by - 30 * s); c.rotate(ang)
    for k in range(5):
        rrect(c, k * 18 * s, -5 * s, 18 * s, 10 * s, 2, RED if k % 2 == 0 else "#FFFFFF", a)
    c.restore()


# ======================================================================
# o experimento (béquer no fogo)
# ======================================================================

def experimento(c, cx, by, a, xprog, t, pts=PURA, termo_x=None):
    """béquer com gelo → água → fervura, sincronizado com a posição xprog no gráfico"""
    if a <= 0:
        return
    w, h = 300, 300
    x0 = cx - w / 2
    gelo = 1 - clamp((xprog - 0.18) / 0.22)          # derrete no 1º patamar
    vapor = clamp((xprog - 0.58) / 0.22)              # ferve no 2º patamar
    nivel = 0.55 - 0.32 * vapor
    V.bequer(c, x0, by - h, w, h, a, WATER, nivel * (1 - 0.35 * gelo) + 0.12 * gelo * 0)
    rnd = random.Random(4)
    if gelo > 0:
        for k in range(5):
            s = 70 * (0.35 + 0.65 * gelo)
            cxk = x0 + 50 + k * 50 + (k % 2) * 10
            V4.cubo(c, cxk, by - h * 0.32 - (k % 2) * 40, s, a, (k * 13) % 20 - 10)
    if 0.56 < xprog < 0.82:
        for k in range(14):
            ph = (t * 0.9 + k / 14) % 1.0
            xx = x0 + 30 + rnd.uniform(0, w - 60)
            c.drawCircle(xx, by - 14 - ph * h * nivel, 6, paint("#FFFFFF", a * (1 - ph)))
        for k in range(3):
            ph = (t * 0.4 + k / 3) % 1.0
            c.drawCircle(cx - 60 + k * 60, by - h - 20 - ph * 90, 26 + ph * 20, paint("#C9D6E3", a * 0.5 * (1 - ph)))
    V.chama(c, cx, by + 120, a, 0.75)
    # termômetro
    tx = termo_x if termo_x is not None else cx + w / 2 + 70
    V.termometro(c, tx, by - h - 40, a, h + 20, 0.08 + 0.85 * y_at(pts, xprog), RED)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def relogio(c, cx, cy, r, a, t):
    V4.relogio(c, cx, cy, r, a, t)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "CURVA DE AQUECIMENTO · EPISÓDIO 5", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    for k, s in enumerate(("laboratório", "análise química")):
        x = 330 + k * 300
        text_mid(c, s, x, 260, 30, "bold", INK2, aa)
        strike(c, x - 110, 260, x + 110, 260, aa, RED, ease_io(prog(t, C["01.a"] + 0.4 * k, 0.4)))
    ab = ep(t, C["01.b"], 0.5)
    V.termometro(c, 380, 360, ab, 300, 0.55, RED)
    relogio(c, 600, 520, 100, ab, t)
    ac = ep(t, C["01.c"], 0.5)
    f = ease_io(prog(t, C["01.c"], 2.6))
    grafico(c, 1000, 280, 560, 380, ac, PURA, f, INK, (), 24)
    pill(c, "é puro?", 1280, 220, BLUE, size=30, a=ac, anchor="center", bounds=(0, 1920))
    pill(c, "o item mais cobrado do assunto", 1280, 790, AMBER, size=28, fg=INK, a=ep(t, C["01.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI RECONHECER", GREEN)
    items = [("PURA", PURA, GREEN), ("COMUM", COMUM, INK2), ("EUTÉTICA", EUT, BLUE), ("AZEOTRÓPICA", AZEO, PURPLE)]
    for k, (s, pts, col) in enumerate(items):
        a, dy = rise(t, C["02.b"] + 0.5 * k)
        if a <= 0:
            continue
        x = 180 + k * 400
        card(c, x, 220 + dy, 360, 460, a)
        grafico(c, x + 50, 280 + dy, 270, 260, a, pts, 1.0, INK, (), 18, larg=5)
        text(c, s, x + 180, 640 + dy, 32, "black", col, a)


def b_prereq(c, t, C, B):
    if t < C["04"] - 0.2:
        head(c, t, B["start"], "LEMBRETE 1", "FUSÃO E EBULIÇÃO", BLUE)
        card(c, *CARD_R)
        for k, (cue, s, sub, kind) in enumerate((("03.a", "FUSÃO", "sólido → líquido", "gelo"), ("03.b", "EBULIÇÃO", "líquido → gás", "ferve"))):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            x = 560 + k * 800
            if kind == "gelo":
                s_ = 1 - 0.5 * ease_io(prog(t, C[cue], 3))
                V4.cubo(c, x, 420 + dy, 160 * s_, a, -6)
                rrect(c, x - 140, 520 + dy, 280, 20 * (2 - s_), 10, WATER, a * 0.7)
            else:
                experimento(c, x, 540 + dy, a, 0.7, t, PURA, termo_x=x + 240)
            V.defbox(c, s, sub, x, 740, a, w=460)
        return
    if t < C["05"] - 0.2:
        head(c, t, C["04"], "LEMBRETE 2", "COMO LER O GRÁFICO", BLUE)
        card(c, *CARD_R)
        aa = ep(t, C["04.a"], 0.5)
        x, y, w, h = 420, 230, 900, 460
        if aa > 0:
            arrow(c, x, y + h, x + w + 20, y + h, BLUE, aa, 5, 16)
            text(c, "TEMPO", x + w, y + h + 50, 30, "black", BLUE, aa, align="right")
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            arrow(c, x, y + h, x, y - 20, RED, ab, 5, 16)
            text(c, "TEMPERATURA", x + 20, y - 10, 30, "black", RED, ab, align="left")
        ac = ep(t, C["04.c"], 0.5)
        if ac > 0:
            pts = [(0, 0.1), (0.35, 0.55), (0.75, 0.55)]
            grafico(c, x, y, w, h, ac, pts, ease_io(prog(t, C["04.c"], 2.0)) * 0.75, INK, (), eixo=False)
            text(c, "subindo: esquentando", x + 200, y + 360, 26, "black", INK, ac, align="left")
            text(c, "deitada: parada", x + w * 0.55, y + h * 0.45 - 40, 26, "black", GREEN, ep(t, C["04.c"] + 1.6, 0.4))
        return
    head(c, t, C["05"], "LEMBRETE 3", "NÚMEROS NEGATIVOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05.t"], 0.5)
    x0, y0, hh = 960, 220, 520
    if a0 > 0:
        line(c, x0, y0, x0, y0 + hh, INK2, a0, 6)
        for v, lab, col in ((25, "25 °C", RED), (0, "0", INK2), (-114, "−114 °C", BLUE)):
            yy = y0 + hh * (1 - (v + 130) / 170)
            line(c, x0 - 30, yy, x0 + 30, yy, col, a0, 4)
            text_mid(c, lab, x0 + 50, yy, 34, "black", col, a0 * ep(t, C["05.a"] if v != 0 else C["05.t"], 0.4), align="left")
    pill(c, "mais negativo = MAIS EMBAIXO = mais frio", 520, 480, GREEN, size=28, a=ep(t, C["05.b"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco a: PF, PE e estado físico
# ======================================================================

def b_pfpe(c, t, C, B):
    head(c, t, B["start"], "PONTO DE FUSÃO", "E PONTO DE EBULIÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    V4.cubo(c, 420, 380, 140, aa, -5)
    text(c, "0 °C", 420, 520, 56, "black", BLUE, aa)
    V.defbox(c, "PONTO DE FUSÃO (PF)", "onde o sólido vira líquido", 420, 690, ep(t, C["06.a"] + 1.4, 0.5), w=560)
    ab = ep(t, C["06.b"], 0.5)
    experimento(c, 1180, 470, ab, 0.7, t, PURA, termo_x=1420)
    text(c, "100 °C", 1180, 600, 56, "black", RED, ab)
    V.defbox(c, "PONTO DE EBULIÇÃO (PE)", "onde o líquido vira gás", 1180, 730, ep(t, C["06.b"] + 2.0, 0.5), w=600)


def regua(c, x, y, h, a, pf, pe, lo, hi, temp=None, t=0.0, cues=None, w=60, rotulos=True, size=28):
    """régua vertical de temperatura com faixas sólido / líquido / gás"""
    if a <= 0:
        return
    Y = lambda v: y + h * (1 - (v - lo) / (hi - lo))
    ks = cues or (0, 0, 0)
    for k, (v0, v1, col, lab) in enumerate(((lo, pf, "#9AC1E8", "SÓLIDO"), (pf, pe, WATER, "LÍQUIDO"), (pe, hi, "#E3E7EC", "GÁS"))):
        ak = a * (ep(t, ks[k], 0.4) if cues else 1.0)
        if ak <= 0:
            continue
        rrect(c, x, Y(v1), w, Y(v0) - Y(v1), 6, col, ak)
        if rotulos:
            text_mid(c, lab, x + w + 20, (Y(v0) + Y(v1)) / 2, size, "black", INK if k != 2 else INK2, ak, align="left")
    for v, lab in ((pf, "PF"), (pe, "PE")):
        line(c, x - 14, Y(v), x + w + 6, Y(v), INK, a, 3)
        text_mid(c, lab, x - 22, Y(v), size * 0.85, "black", INK, a, align="right")
    if temp is not None:
        yy = Y(temp)
        line(c, x - 40, yy, x + w + 10, yy, RED, a, 5)
        c.drawCircle(x - 44, yy, 9, paint(RED, a))


def b_regua(c, t, C, B):
    head(c, t, B["start"], "PF E PE DECIDEM", "O ESTADO FÍSICO", PURPLE)
    card(c, *CARD_R)
    ab = ep(t, C["07.b"], 0.5)
    regua(c, 420, 210, 560, ab, 0, 100, -60, 160, None, t, (C["07.c"], C["07.d"], C["07.e"]), w=90, size=34)
    rows = [("07.c", "abaixo do PF", "SÓLIDO"), ("07.d", "entre PF e PE", "LÍQUIDO"), ("07.e", "acima do PE", "GASOSO")]
    for k, (cue, s1, s2) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 640 - k * 190 + dy
        text(c, s1, 980, y, 40, "black", INK, a, align="left")
        text(c, "→ " + s2, 1300, y, 40, "black", PURPLE, a, align="left")


def b_mercurio(c, t, C, B):
    head(c, t, B["start"], "O MERCÚRIO", "O METAL LÍQUIDO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["08.t"], 0.5)
    V.termometro(c, 360, 260, a0, 420, 0.5, "#B8BCC2")
    text(c, "mercúrio", 360, 790, 32, "black", INK, a0)
    aa = ep(t, C["08.a"], 0.5)
    ab = ep(t, C["08.b"], 0.5)
    regua(c, 780, 220, 520, max(aa, ab), -39, 357, -120, 450, 25 if t >= C["08.c"] else None, t, w=80, size=30)
    text(c, "PF = −39 °C", 1180, 640, 40, "black", BLUE, aa, align="left")
    text(c, "PE = 357 °C", 1180, 320, 40, "black", RED, ab, align="left")
    ac = ep(t, C["08.c"], 0.5)
    text(c, "25 °C → LÍQUIDO", 1180, 500, 44, "black", RED, ac, align="left")
    pill(c, "único metal líquido no ambiente", 1360, 760, GREEN, size=28, a=ep(t, C["08.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco b: a curva da substância pura (animação principal)
# ======================================================================

def xprog_pura(t, C):
    return keyframes(t, [(C["09.b"], 0.0), (WT(C, "10", "zero") + 0.3, 0.18), (C["11.c"] + 1.4, 0.40),
                         (WT(C, "12", "cem") + 0.3, 0.58), (C["12.c"] + 1.8, 0.80), (C["12.d"] + 0.6, 0.96)])


GX, GY, GW, GH = 830, 200, 850, 450


def b_curva(c, t, C, B):
    head(c, t, B["start"], "A CURVA DE AQUECIMENTO", "DA SUBSTÂNCIA PURA", BLUE)
    card(c, 140, 150, 600, 690)
    card(c, 760, 150, 1020, 690)
    xp = xprog_pura(t, C)
    experimento(c, 400, 640, ep(t, C["09.a"], 0.5), xp, t)
    a_g = ep(t, C["09.b"], 0.5)
    marcas = []
    if t > WT(C, "10", "zero") - 0.3:
        marcas.append((0.3, "0 °C", BLUE))
    if t > WT(C, "12", "cem") - 0.3:
        marcas.append((0.72, "100 °C", RED))
    grafico(c, GX, GY, GW, GH, a_g, PURA, xp, INK, marcas, 24)
    if a_g > 0:   # ponto atual
        c.drawCircle(GX + GW * xp, GY + GH * (1 - y_at(PURA, xp)), 11, paint(RED, a_g))
    V.defbox(c, "CURVA DE AQUECIMENTO", "temperatura × tempo enquanto esquenta", 1270, 790, ep(t, C["09.c"], 0.5) * (1 - ep(t, C["10.b"], 0.4)), w=760)
    ab = ep(t, C["10.b"], 0.5) * (1 - ep(t, C["11.c"] + 1.0, 0.4))
    pill(c, "TRAVOU", 400 + 220, 260, GREEN, size=28, a=ab, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["10.d"], 0.5) * (1 - ep(t, C["11.t"], 0.4))
    V.defbox(c, "PATAMAR", "temperatura parada enquanto muda de estado", 1270, 790, ad, w=760)
    # pedágio sobre os patamares
    a11 = ep(t, C["11.t"], 0.5)
    if a11 > 0:
        cabine(c, GX + GW * 0.29, GY + GH * (1 - 0.3) - 10, a11, prog(t, C["11.c"], 0.8))
        pill(c, "o material \"paga\" a mudança", 1270, 790, GREEN, size=26, a=a11 * ep(t, C["11.a"], 0.4) * (1 - ep(t, C["12.t"], 0.4)), anchor="center", bounds=(0, 1920))
    a12 = ep(t, C["12.b"], 0.5)
    if a12 > 0:
        cabine(c, GX + GW * 0.69, GY + GH * (1 - 0.72) - 10, a12, prog(t, C["12.c"], 0.8))
    patamar_rotulo(c, GX, GY, GW, GH, PURA, 1, "PF", ep(t, C["12.d"], 0.5), GREEN, 40)
    patamar_rotulo(c, GX, GY, GW, GH, PURA, 3, "PE", ep(t, C["12.d"], 0.5), GREEN, 40)
    regra(c, "PURA = 2 PATAMARES", 1270, 790, ep(t, C["12.d"], 0.5), 32, PURPLE, w=560)


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    V.regra(c, s, cx, cy, a, size, col, w)


# ======================================================================
# bloco c: mistura comum
# ======================================================================

def b_comum(c, t, C, B):
    head(c, t, B["start"], "E UMA MISTURA?", "ÁGUA COM SAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["13.t"], 0.5)
    grafico(c, 420, 220, 1000, 500, a0 * 0.25, PURA, 1.0, LIGHT, (), 24, destaque=False)
    text(c, "pura (para comparar)", 1420, 230, 22, "bold", LIGHT, a0, align="right")
    f = ease_io(prog(t, C["13.a"], 3.4))
    grafico(c, 420, 220, 1000, 500, a0, COMUM, f, INK, (), 24, eixo=False)
    ac = ep(t, C["13.c"], 0.5)
    patamar_rotulo(c, 420, 220, 1000, 500, COMUM, 1, "faixa", ac, AMBER, -40)
    patamar_rotulo(c, 420, 220, 1000, 500, COMUM, 3, "faixa", ac, AMBER, -40)
    pill(c, "cada componente muda numa temperatura diferente", 920, 790, INK2, size=26, a=ac * (1 - ep(t, C["13.d"], 0.4)), anchor="center", bounds=(0, 1920))
    regra(c, "MISTURA COMUM = NENHUM PATAMAR", 920, 790, ep(t, C["13.d"], 0.5), 30, PURPLE, w=760)


RITUAL = ["conte os PATAMARES", "ONDE estão? fusão ou ebulição", "CLASSIFIQUE"]


def ritual(c, t, x, y, w, a, cues=None, dy=120, ativo=None, size=34):
    if a <= 0:
        return
    card(c, x, y, w, dy * 3 + 70, a)
    text(c, "RITUAL DO GRÁFICO", x + 36, y + 52, 24, "black", PURPLE, a, align="left")
    for k, s in enumerate(RITUAL):
        ak = a * (ep(t, cues[k], 0.45) if cues else 1.0)
        if ak <= 0:
            continue
        yy = y + 76 + k * dy
        if ativo == k:
            rrect(c, x + 14, yy, w - 28, dy - 14, 16, PURPLE, ak * 0.12)
        badge_num(c, k + 1, x + 60, yy + (dy - 14) / 2, ak, 24, bg=PURPLE)
        text_mid(c, s, x + 104, yy + (dy - 14) / 2, size, "black", INK, ak, align="left")


def b_ritual(c, t, C, B):
    head(c, t, B["start"], "O RITUAL", "TODO GRÁFICO, 3 PASSOS", PURPLE)
    cues = [C["14.a"], C["14.b"], C["14.c"]]
    k = None
    for i, cu in enumerate(cues):
        if t >= cu:
            k = i
    ritual(c, t, 160, 200, 860, ep(t, C["14.t"], 0.5), cues, ativo=k, dy=150)
    card(c, 1060, 200, 700, 520, ep(t, C["14.t"], 0.5))
    grafico(c, 1140, 270, 560, 360, ep(t, C["14.t"], 0.5), PURA, 1.0, INK, (), 20)
    a1 = ep(t, C["14.a"], 0.4)
    for kk in (1, 3):
        badge_num(c, "12"[kk // 2], 1140 + 560 * (PURA[kk][0] + PURA[kk + 1][0]) / 2, 270 + 360 * (1 - PURA[kk][1]) - 34, a1, 18, bg=GREEN)
    patamar_rotulo(c, 1140, 270, 560, 360, PURA, 1, "fusão", ep(t, C["14.b"], 0.4), BLUE, 40, 20)
    patamar_rotulo(c, 1140, 270, 560, 360, PURA, 3, "ebulição", ep(t, C["14.b"], 0.4), RED, 40, 20)
    pill(c, "→ PURA", 1410, 680, PURPLE, size=28, a=ep(t, C["14.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d: o limite do gráfico
# ======================================================================

def b_limite(c, t, C, B):
    head(c, t, B["start"], "O LIMITE", "DO GRÁFICO", AMBER)
    card(c, *CARD_R)
    for k, (f, nome, tipo) in enumerate((("H2O", "água pura", "COMPOSTA"), ("O2", "gás oxigênio", "SIMPLES"))):
        a, dy = rise(t, C["15.a"] + 0.6 * k)
        if a <= 0:
            continue
        x = 200 + k * 560
        grafico(c, x + 40, 240 + dy, 400, 270, a, PURA, 1.0, INK, (), 18, larg=5)
        V.formula(c, f, x + 260, 600 + dy, 70, a, lit=ep(t, C["15.b"], 0.5) * V.n_el(f))
        text(c, nome, x + 260, 680 + dy, 28, "bold", INK2, a)
        text(c, tipo, x + 260, 730 + dy, 30, "black", PURPLE, ep(t, C["15.b"], 0.5))
    text_mid(c, "=", 720, 380, 90, "black", AMBER, ep(t, C["15.a"] + 1.0, 0.4))
    ac = ep(t, C["15.c"], 0.5)
    regra(c, "o gráfico separa PURO de MISTURA", 1500, 330, ac, 24, PURPLE)
    pill(c, "simples ou composta?", 1500, 470, AMBER, size=26, fg=INK, a=ep(t, C["15.d"], 0.5), anchor="center", bounds=(0, 1920))
    pill(c, "→ só a FÓRMULA (ep. 1)", 1500, 540, GREEN, size=26, a=ep(t, C["15.d"] + 1.2, 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco e-f: eutética e azeotrópica
# ======================================================================

def ferro_solda(c, cx, cy, a, t):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-25)
    rrect(c, -240, -22, 200, 44, 18, "#3A3A3C", a)
    rrect(c, -50, -10, 140, 20, 8, "#B8BCC2", a)
    p = skia.Path(); p.moveTo(90, -10); p.lineTo(140, 0); p.lineTo(90, 10); p.close()
    c.drawPath(p, paint("#8C9096", a))
    c.restore()
    line(c, cx - 120, cy + 120, cx + 200, cy + 120, "#C77B43", a, 10)
    line(c, cx - 120, cy + 140, cx + 200, cy + 140, "#C77B43", a, 10)
    c.drawCircle(cx + 140, cy + 128, 22 + 3 * math.sin(t * 3), paint("#B8BCC2", a))


def b_solda(c, t, C, B):
    head(c, t, B["start"], "AS MISTURAS", "QUE ENGANAM", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    ferro_solda(c, 520, 380, aa, t)
    V.defbox(c, "SOLDA", "metal derretido para grudar fios", 520, 680, aa, w=560)
    ab = ep(t, C["16.b"], 0.5)
    V.defbox(c, "LIGA", "uma mistura de metais", 1260, 300, ab, w=460)
    if ab > 0:
        f = ease_io(prog(t, C["16.b"] + 1.0, 1.0))
        rrect(c, 1000, 450, 520 * 0.63 * f, 80, 10, "#A7ADB4", ab)
        rrect(c, 1000 + 520 * 0.63, 450, 520 * 0.37 * f, 80, 10, "#5A5D62", ab * f)
        text_mid(c, "63% estanho", 1000 + 520 * 0.315, 490, 26, "black", INK, ab * f)
        text_mid(c, "37% chumbo", 1000 + 520 * 0.815, 490, 22, "black", "#FFFFFF", ab * f)


def b_eutetica(c, t, C, B):
    head(c, t, B["start"], "A SOLDA", "MISTURA EUTÉTICA", BLUE)
    card(c, *CARD_R)
    xp = keyframes(t, [(C["17.t"], 0), (C["17.a"] + 2.0, 0.42), (C["17.b"] + 2.0, 0.96)])
    grafico(c, 380, 230, 900, 430, 1.0, EUT, xp, INK, [(0.3, "183 °C", BLUE)] if t > C["17.a"] else [], 24)
    patamar_rotulo(c, 380, 230, 900, 430, EUT, 1, "funde certinho", ep(t, C["17.a"] + 1.4, 0.4), GREEN, -40)
    patamar_rotulo(c, 380, 230, 900, 430, EUT, 3, "ferve em faixa", ep(t, C["17.b"] + 1.4, 0.4), AMBER, -40)
    V.defbox(c, "MISTURA EUTÉTICA", "patamar só na FUSÃO", 1530, 755, ep(t, C["17.c"], 0.5), w=440)


def garrafa_alcool(c, cx, cy, a):
    if a <= 0:
        return
    rrect(c, cx - 60, cy - 110, 120, 230, 24, "#E9F2FB", a, shadow=True, stroke=3, stroke_color="#9AC1E8")
    rrect(c, cx - 24, cy - 160, 48, 56, 10, "#E9F2FB", a, stroke=3, stroke_color="#9AC1E8")
    rrect(c, cx - 30, cy - 182, 60, 26, 6, RED, a)
    rrect(c, cx - 60, cy - 30, 120, 80, 4, "#FFFFFF", a)
    text_mid(c, "ÁLCOOL", cx, cy - 6, 20, "black", BLUE, a)
    text_mid(c, "96%", cx, cy + 24, 26, "black", RED, a)


def b_azeotropica(c, t, C, B):
    head(c, t, B["start"], "O ÁLCOOL 96%", "MISTURA AZEOTRÓPICA", BLUE)
    card(c, *CARD_R)
    garrafa_alcool(c, 300, 450, ep(t, C["18.t"], 0.5))
    text(c, "álcool + água", 300, 650, 28, "black", INK2, ep(t, C["18.a"], 0.5))
    xp = keyframes(t, [(C["18.a"], 0), (C["18.a"] + 2.4, 0.42), (C["18.b"] + 2.4, 0.96)])
    grafico(c, 560, 230, 820, 430, ep(t, C["18.a"], 0.5), AZEO, xp, INK, [(0.72, "≈ 78 °C", RED)] if t > C["18.b"] else [], 24)
    patamar_rotulo(c, 560, 230, 820, 430, AZEO, 1, "derrete em faixa", ep(t, C["18.a"] + 1.6, 0.4), AMBER, -40)
    patamar_rotulo(c, 560, 230, 820, 430, AZEO, 3, "ferve certinho", ep(t, C["18.b"] + 1.4, 0.4), GREEN, -40)
    V.defbox(c, "MISTURA AZEOTRÓPICA", "patamar só na EBULIÇÃO", 1530, 755, ep(t, C["18.c"], 0.5), w=440)


def b_confundir(c, t, C, B):
    head(c, t, B["start"], "COMO NÃO", "TROCAR OS NOMES", GREEN)
    for k, (cue, verbo, nome, desenho, pts) in enumerate((("19.a", "FUNDE", "EUTÉTICA", "solda", EUT), ("19.b", "FERVE", "AZEOTRÓPICA", "alcool", AZEO))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 800
        card(c, x, 190 + dy, 760, 470, a)
        if desenho == "solda":
            c.save(); c.translate(x + 190, 340 + dy); c.scale(0.55, 0.55); ferro_solda(c, 0, 0, a, t); c.restore()
        else:
            c.save(); c.translate(x + 190, 380 + dy); c.scale(0.7, 0.7); garrafa_alcool(c, 0, 0, a); c.restore()
        grafico(c, x + 400, 250 + dy, 300, 220, a, pts, 1.0, INK, (), 16, larg=4)
        text(c, f"{'a solda' if k == 0 else 'o álcool'} {verbo} certinho", x + 380, 560 + dy, 40, "black", INK, a)
        text(c, "→ " + nome, x + 380, 620 + dy, 44, "black", GREEN, a)
    regra(c, "só a PURA para nas DUAS cabines", W / 2, 760, ep(t, C["19.c"], 0.5), 32, PURPLE, w=900)


QUATRO = [("PURA", PURA, "2 patamares", "20.a"), ("EUTÉTICA", EUT, "só na fusão", "20.b"),
          ("AZEOTRÓPICA", AZEO, "só na ebulição", "20.c"), ("COMUM", COMUM, "nenhum", "20.d")]


def b_quatro(c, t, C, B):
    head(c, t, B["start"], "AS QUATRO CURVAS", "LADO A LADO", PURPLE)
    for k, (nome, pts, sub, cue) in enumerate(QUATRO):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 180 + (k % 2) * 800, 175 + (k // 2) * 330 + dy
        card(c, x, y, 760, 310, a)
        grafico(c, x + 70, y + 40, 360, 220, a, pts, ease_io(prog(t, C[cue], 1.4)), INK, (), 16, larg=5)
        text(c, nome, x + 480, y + 140, 40, "black", INK, a, align="left")
        text(c, sub, x + 480, y + 190, 30, "bold", GREEN if k < 3 else INK2, a, align="left")


def b_alcool(c, t, C, B):
    head(c, t, B["start"], "CONSEQUÊNCIA PRÁTICA", "O ÁLCOOL PARA EM 96%", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.5)
    garrafa_alcool(c, 420, 470, a0)
    pill(c, "destilação simples = ferver e recolher o vapor", 960, 220, BLUE, size=26, a=a0, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        for k in range(4):
            ph = (t * 0.5 + k / 4) % 1.0
            c.drawCircle(700 + ph * 500, 420 - math.sin(ph * math.pi) * 90, 30, paint("#C9D6E3", ab * (1 - ph * 0.6)))
        text(c, "vapor: 96%", 950, 300, 36, "black", INK, ab)
        garrafa_alcool(c, 1380, 470, ab)
        text(c, "líquido 96% → vapor 96%", 960, 700, 36, "black", PURPLE, ab)
    pill(c, "destilação: vídeo próprio", 960, 790, GREEN, size=24, a=ep(t, C["21.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Dois patamares: puro. Nenhum: mistura comum.",
          "Um patamar só: eutética se for na fusão,",
          "O gráfico não diz se é simples ou composta."]


def b_recap(c, t, C, B):
    sid = "22" if B["start"] < C["34"] - 1 else "34"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    ys = [300, 450, 640]
    for k, (cue, col) in enumerate((("a", GREEN), ("b", PURPLE), ("c", AMBER))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = ys[k] + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        text(c, FRASES[k], 290, y, 44, "black", INK, a, align="left")
        if k == 1:
            text(c, "azeotrópica se for na ebulição.", 290, y + 62, 44, "black", INK, a, align="left")


def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "UM PATAMAR PROVA QUE É PURO?", RED)

    def ex(c, k, x, y, cw, a):
        if k == 2:
            grafico(c, x + 90, y + 400, 320, 130, a, EUT, 1.0, INK, (), 14, larg=4)
    V.erro_tiles(c, t, [(C["23.a"], "O ERRO", ["!1 patamar só", "!prova que é puro"], RED),
                        (C["23.b"], "POR QUE PARECE CERTO", ["o patamar é a marca", "da substância pura"], AMBER),
                        (C["23.c"], "A CORREÇÃO", ["eutética e azeotrópica", "também têm um", "!PURO PRECISA DE 2"], GREEN)], ex)


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "A CURVA DIZ SIMPLES OU COMPOSTA?", RED)
    V.erro_tiles(c, t, [(C["24.a"], "O ERRO", ["!a curva mostra", "!simples ou composta"], RED),
                        (C["24.b"], "POR QUE PARECE CERTO", ["ela já mostrou", "se é puro"], AMBER),
                        (C["24.c"], "A CORREÇÃO", ["H₂O e O₂: curvas", "do mesmo tipo", "!SÓ A FÓRMULA"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "TROCAR OS NOMES", RED)
    V.erro_tiles(c, t, [(C["25.a"], "O ERRO", ["!trocar eutética", "!e azeotrópica"], RED),
                        (C["25.b"], "POR QUE PARECE CERTO", ["nomes estranhos e", "um patamar só"], AMBER),
                        (C["25.c"], "A CORREÇÃO", ["solda FUNDE certinho", "álcool FERVE certinho", "!EUTÉ · AZEO"], GREEN)])


def b_erro4(c, t, C, B):
    head(c, t, B["start"], "ERRO 4", "O SINAL DE MENOS", RED)

    def ex(c, k, x, y, cw, a):
        if k == 2:
            regua(c, x + cw / 2 - 30, y + 380, 160, a, -219, -183, -260, 60, 25, w=50, rotulos=False, size=18)
    V.erro_tiles(c, t, [(C["26.a"], "O ERRO", ["!errar o estado", "!por um sinal"], RED),
                        (C["26.b"], "POR QUE PARECE CERTO", ["183 parece", "maior que 25"], AMBER),
                        (C["26.c"], "A CORREÇÃO", ["−183 é muito", "mais frio", "!DESENHE A RÉGUA"], GREEN)], ex)


# ======================================================================
# questões 8, 2 e 6
# ======================================================================

def alternativas(c, t, C, y0, alts, alt_cues, correta, cue_ok, xs, size=27):
    aok = ep(t, C[cue_ok], 0.5)
    for k, s in enumerate(alts):
        L = "ABCDE"[k]
        a, d = rise(t, C[alt_cues[k]])
        y = y0 + k * 56 + d
        ok = L == correta
        if ok and aok > 0:
            rrect(c, 170, y - 38, 700, 54, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
        x_cue, why = xs.get(L, (None, ""))
        ax = ep(t, C[x_cue], 0.4) if x_cue else 0
        text(c, s, 245, y, size, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 240, y - 10, 250 + text_w(s, "black", size), y - 10, ax, RED, ax)
            text(c, why, 860, y - 2, 20, "black", RED, ax, align="right")


TAB8 = [("Etanol", -114, 78, "28.s1", True), ("Cloreto de sódio", 801, 1413, "28.s2", False),
        ("Oxigênio", -219, -183, "28.s3", False), ("Mercúrio", -39, 357, "28.s4", True)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8", "ESTADO FÍSICO PELA TABELA", BLUE)
    card(c, 140, 160, 760, 660)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    ae = ep(t, C["27.e2"], 0.5)
    text(c, "Substância", 190, 270, 24, "black", INK2, ae, align="left")
    text(c, "PF (°C)", 600, 270, 24, "black", INK2, ae, align="right")
    text(c, "PE (°C)", 800, 270, 24, "black", INK2, ae, align="right")
    for k, (nome, pf, pe, _, _) in enumerate(TAB8):
        ak = ae * ep(t, C["27.e2"] + 1.6 * k, 0.4)
        y = 312 + k * 40
        text(c, nome, 190, y, 26, "black", INK, ak, align="left")
        text(c, f"{pf}".replace("-", "−"), 600, y, 26, "black", INK, ak, align="right")
        text(c, f"{pe}".replace("-", "−").replace("1413", "1 413"), 800, y, 26, "black", INK, ak, align="right")
    text(c, "A 25 °C, quantas estão líquidas?", 180, 500, 26, "black", INK2, ep(t, C["27.e3"], 0.5), align="left")
    alternativas(c, t, C, 560, ["0", "1", "2", "3", "4"], ["27.a", "27.b", "27.c", "27.d", "27.e"], "C", "28.ok",
                 {"D": ("29.xd", "errou o sinal do O₂"), "B": ("29.xb", "esqueceu o mercúrio"),
                  "A": ("29.xa", "ignorou a régua"), "E": ("29.xa", "ignorou a régua")})
    V.pause_badge(c, 1170, 440, ep(t, C["27.p"], 0.5) * (1 - prog(t, C["28.t"] - 0.3, 0.4)))
    ar = ep(t, C["28.t"], 0.5)
    if ar > 0:
        card(c, 940, 160, 840, 660, ar)
        text(c, "a régua de cada uma (linha vermelha = 25 °C)", 1360, 210, 22, "bold", INK2, ar)
        for k, (nome, pf, pe, cue, liq) in enumerate(TAB8):
            ak = ar * ep(t, C[cue], 0.4)
            x = 1010 + k * 200
            lo, hi = min(pf, 25) - 60, max(pe, 25) + 60
            regua(c, x + 30, 260, 400, ak, pf, pe, lo, hi, 25, w=56, rotulos=False, size=20)
            text(c, nome.split()[0], x + 58, 710, 22, "black", INK, ak)
            text(c, "LÍQUIDO" if liq else ("sólido" if pf > 25 else "gasoso"), x + 58, 750, 22, "black", GREEN if liq else INK2, ak)


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2", "DOIS PATAMARES", BLUE)
    card(c, 140, 160, 760, 660)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    for k, (cue, s) in enumerate((("30.e1", "Amostra aquecida sem parar."), ("30.e2", "Constante a 80 °C na fusão"),
                                  ("30.e2", "e a 218 °C na ebulição."), ("30.e3", "A amostra é:"))):
        text(c, s, 180, 280 + k * 42, 27, "black", INK if k < 3 else INK2, ep(t, C[cue] + (0.8 if k == 2 else 0), 0.5), align="left")
    alternativas(c, t, C, 500, ["substância pura", "mistura comum", "mistura eutética", "mistura azeotrópica", "substância simples"],
                 ["30.a", "30.b", "30.c", "30.d", "30.e"], "A", "31.ok",
                 {"C": ("31.xc", "só na fusão"), "D": ("31.xd", "só na ebulição"), "B": ("31.xb", "nenhum patamar"),
                  "E": ("31.xe", "ARMADILHA: a curva não diz")})
    V.pause_badge(c, 1170, 440, ep(t, C["30.p"], 0.5) * (1 - prog(t, C["31.t"] - 0.3, 0.4)))
    ar = ep(t, C["31.t"], 0.5)
    if ar > 0:
        card(c, 940, 160, 840, 660, ar)
        grafico(c, 1060, 240, 640, 380, ar, PURA, 1.0, INK, [(0.3, "80 °C", BLUE), (0.72, "218 °C", RED)], 22)
        for kk, cue in ((1, "31.r1"), (3, "31.r1")):
            badge_num(c, "1" if kk == 1 else "2", 1060 + 640 * (PURA[kk][0] + PURA[kk + 1][0]) / 2, 240 + 380 * (1 - PURA[kk][1]) - 34,
                      ar * ep(t, C[cue] + (0.6 if kk == 3 else 0), 0.3), 18, bg=GREEN)
        ritual(c, t, 1000, 640, 720, 0, None)
        pill(c, "2 patamares → PURA", 1380, 720, PURPLE, size=28, a=ar * ep(t, C["31.r3"], 0.5), anchor="center", bounds=(0, 1920))


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6", "A LIGA DE SOLDA", BLUE)
    card(c, 140, 160, 760, 660)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    for k, (cue, s) in enumerate((("32.e1", "Liga de solda: funde a 183 °C,"), ("32.e1", "temperatura constante,"),
                                  ("32.e2", "mas ferve numa faixa."), ("32.e3", "Ela é:"))):
        text(c, s, 180, 280 + k * 42, 27, "black", INK if k < 3 else INK2, ep(t, C[cue], 0.5), align="left")
    alternativas(c, t, C, 500, ["substância pura simples", "substância pura composta", "mistura eutética", "mistura azeotrópica",
                                "mistura comum"], ["32.a", "32.b", "32.c", "32.d", "32.e"], "C", "33.ok",
                 {"A": ("33.xa", "teria 2 patamares"), "B": ("33.xa", "teria 2 patamares"),
                  "D": ("33.xd", "patamar na ebulição"), "E": ("33.xe", "nenhum patamar")})
    V.pause_badge(c, 1170, 440, ep(t, C["32.p"], 0.5) * (1 - prog(t, C["33.t"] - 0.3, 0.4)))
    ar = ep(t, C["33.t"], 0.5)
    if ar > 0:
        card(c, 940, 160, 840, 660, ar)
        grafico(c, 1060, 240, 640, 380, ar, EUT, 1.0, INK, [(0.3, "183 °C", BLUE)], 22)
        badge_num(c, "1", 1060 + 640 * (EUT[1][0] + EUT[2][0]) / 2, 240 + 380 * (1 - EUT[1][1]) - 34, ar * ep(t, C["33.r1"], 0.3), 18, bg=GREEN)
        patamar_rotulo(c, 1060, 240, 640, 380, EUT, 1, "fusão", ar * ep(t, C["33.r2"], 0.4), BLUE, 40, 20)
        pill(c, "funde certinho → EUTÉTICA", 1380, 720, PURPLE, size=28, a=ar * ep(t, C["33.r3"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "ÚLTIMO EPISÓDIO", "REVISÃO DA SÉRIE", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["35.t"], 0.5)
    pecas = [("simples × composta", "ep. 1"), ("alotropia", "ep. 2"), ("misturas", "ep. 3"), ("fases e componentes", "ep. 4"), ("curva de aquecimento", "ep. 5")]
    for k, (s, e) in enumerate(pecas):
        ak = a0 * ep(t, C["35.t"] + 0.25 * k, 0.4)
        x = 300 + k * 330
        rrect(c, x - 140, 230, 280, 120, 18, BLUE, ak * 0.10)
        text_mid(c, s, x, 280, 22, "black", INK, ak)
        text_mid(c, e, x, 318, 20, "bold", INK2, ak)
    items = [("35.a", "um roteiro de 3 perguntas", PURPLE), ("35.b", "caçar as pegadinhas", AMBER), ("35.c", "questões novas", GREEN)]
    for k, (cue, s, col) in enumerate(items):
        a, dy = rise(t, C[cue])
        pill(c, s, W / 2, 460 + k * 100 + dy, col, size=32, fg=INK if col == AMBER else None, a=a, anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["36.like"], C["36.sub"], C["36.bell"], C["36.com"], C["36.bye"], "Você já conhecia a mistura eutética?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, pfpe=b_pfpe, regua=b_regua, mercurio=b_mercurio,
              curva=b_curva, comum=b_comum, ritual=b_ritual, limite=b_limite, solda=b_solda, eutetica=b_eutetica,
              azeotropica=b_azeotropica, confundir=b_confundir, quatro=b_quatro, alcool=b_alcool, recap=b_recap,
              erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, erro4=b_erro4, q8=b_q8, q2=b_q2, q6=b_q6,
              ponte=b_ponte, cta=b_cta)
