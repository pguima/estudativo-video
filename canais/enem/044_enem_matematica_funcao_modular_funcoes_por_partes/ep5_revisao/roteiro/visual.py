"""Visual — Função Modular e Funções por Partes, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): prédio de andares · escada de caixinhas · V na reta ·
elástico da tolerância.
Ícones de área (area_icone()): gota · raio · celular · relógio · termômetro · estrada · régua · barras · moeda · globo.
Q2 ("qual gráfico"): as alternativas são 5 mini gráficos (mini_graf()).
Cores com função: azul = definição · roxo = regra, fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum044", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_modular_ep5_revisao.mp4"
CARD_R = K.CARD_R
AGUA = "#9CCFE6"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 30', '5 GB', '1 h', '−18 °C' nem '1 000'"""
    s = re.sub(r"(?<=R\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\d) (?=(GB|kWh|km|min|mm|h|°C|reais|vezes|%)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


def fit(c, s, x, y, size, maxw, peso, col, a, align="left"):
    """texto numa linha só, encolhendo até caber em maxw"""
    s = nb(s)
    while ftw(s, size, peso) > maxw and size > 18:
        size -= 1
    ftext(c, s, x, y, size, peso, col, a, align=align)
    return size


def _quebra(s, size, maxw, peso="black"):
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and ftw(tst, size, peso) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    return out + ([cur] if cur else [])


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """quebra de linha que respeita os espaços rígidos de nb()"""
    s = nb(s)
    lh = lh or size * 1.32
    out = _quebra(s, size, maxw, peso)
    if a > 0:
        for k, ln in enumerate(out):
            text(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def predio_ic(c, a):
    """ep1: o prédio de andares; o 3º andar aceso"""
    rrect(c, -130, -190, 260, 380, 16, "#FFFFFF", a, shadow=True)
    for k in range(3):
        y = 100 - k * 110
        col = AMBER if k == 2 else mix("#FFFFFF", BLUE, 0.25)
        rrect(c, -105, y - 40, 210, 90, 10, col, a)
        ftext(c, f"{k + 1}º", -80, y + 20, 34, "black", INK if k == 2 else INK2, a, align="left")
    arrow(c, 170, 150, 170, -110, PURPLE, a, 8, 22)


def escada_ic(c, a):
    """ep2: a escada de caixinhas do progressivo"""
    for k, col in enumerate((mix("#FFFFFF", INK2, 0.3), BLUE, PURPLE)):
        h = 110 + k * 80
        rrect(c, -200 + k * 135, 170 - h, 125, h, 12, col, a, shadow=True)
        ftext(c, ("0%", "10%", "20%")[k], -137 + k * 135, 150, 30, "black", "#FFFFFF", a, align="center")


def v_ic(c, a):
    """ep3: o V na reta, com o vértice onde o de dentro zera"""
    rrect(c, -200, -170, 400, 340, 22, "#FFFFFF", a, shadow=True)
    line(c, -170, 110, 170, 110, INK2, a, 5)
    p = skia.Path(); p.moveTo(-150, -130); p.lineTo(40, 110); p.lineTo(170, -60)
    c.drawPath(p, paint(PURPLE, a, stroke=10))
    c.drawCircle(40, 110, 14, paint(AMBER, a))
    ftext(c, "3", 40, 160, 32, "black", INK, a, align="center")


def elastico_ic(c, a):
    """ep4: o elástico da tolerância, preso no centro, estica k para cada lado"""
    line(c, -210, 40, 210, 40, INK2, a, 5)
    p = skia.Path(); p.moveTo(-150, 40); p.quadTo(-75, -50, 0, 40); p.quadTo(75, -50, 150, 40)
    c.drawPath(p, paint(GREEN, a, stroke=9))
    for x in (-150, 150):
        c.drawCircle(x, 40, 16, paint(GREEN, a))
    c.drawCircle(0, 40, 18, paint(PURPLE, a))
    arrow(c, -20, 110, -150, 110, AMBER, a, 6, 16)
    arrow(c, 20, 110, 150, 110, AMBER, a, 6, 16)
    ftext(c, "± k", 0, 170, 38, "black", AMBER, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (predio_ic, escada_ic, v_ic, elastico_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def gota(c, a):
    p = skia.Path(); p.moveTo(0, -160); p.quadTo(120, 10, 100, 60); p.quadTo(60, 150, 0, 150)
    p.quadTo(-60, 150, -100, 60); p.quadTo(-120, 10, 0, -160); p.close()
    c.drawPath(p, paint(AGUA, a))
    c.drawPath(p, paint(mix(AGUA, INK, 0.4), a, stroke=6))
    c.drawCircle(-35, 60, 18, paint("#FFFFFF", a * 0.8))


def raio(c, a):
    p = skia.Path(); p.moveTo(30, -170); p.lineTo(-90, 20); p.lineTo(-5, 20); p.lineTo(-40, 170); p.lineTo(90, -30)
    p.lineTo(5, -30); p.close()
    c.drawPath(p, paint(AMBER, a))
    c.drawPath(p, paint(mix(AMBER, INK, 0.4), a, stroke=6))


def celular(c, a):
    rrect(c, -95, -170, 190, 340, 26, INK, a, shadow=True)
    rrect(c, -78, -140, 156, 260, 10, mix("#FFFFFF", BLUE, 0.2), a)
    for k in range(4):
        rrect(c, -55 + k * 30, 60 - k * 35, 22, 30 + k * 35, 4, BLUE, a)
    c.drawCircle(0, 145, 10, paint(LIGHT, a))


def relogio(c, a):
    c.drawCircle(0, 0, 140, paint("#FFFFFF", a))
    c.drawCircle(0, 0, 140, paint(INK2, a, stroke=10))
    for k in range(12):
        ang = math.radians(k * 30)
        line(c, 115 * math.sin(ang), -115 * math.cos(ang), 128 * math.sin(ang), -128 * math.cos(ang), INK2, a, 5)
    line(c, 0, 0, 0, -95, INK, a, 10)
    line(c, 0, 0, 70, 30, INK, a, 8)
    c.drawCircle(0, 0, 12, paint(RED, a))


def termometro(c, a):
    rrect(c, -35, -170, 70, 260, 35, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-35, -170, 70, 260), 35, 35), paint(INK2, a, stroke=6))
    c.drawCircle(0, 115, 60, paint(BLUE, a))
    rrect(c, -14, -60, 28, 160, 14, BLUE, a)
    for k in range(4):
        line(c, 40, -130 + k * 45, 70, -130 + k * 45, INK2, a, 5)


def estrada(c, a):
    p = skia.Path(); p.moveTo(-60, -170); p.lineTo(60, -170); p.lineTo(170, 170); p.lineTo(-170, 170); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", INK2, 0.55), a))
    for k in range(4):
        y = -150 + k * 85
        rrect(c, -6 - k * 2, y, 12 + k * 4, 45, 4, "#FFFFFF", a)
    rrect(c, 60, -120, 120, 70, 10, GREEN, a)
    ftext(c, "km 30", 120, -72, 30, "black", "#FFFFFF", a, align="center")


def regua(c, a):
    c.save(); c.rotate(-20)
    rrect(c, -190, -50, 380, 100, 10, AMBER, a, shadow=True)
    for k in range(13):
        h = 40 if k % 2 == 0 else 22
        line(c, -170 + k * 28, -50, -170 + k * 28, -50 + h, INK, a, 4)
    c.restore()


def barras(c, a):
    rrect(c, -170, -150, 340, 300, 16, "#FFFFFF", a)
    line(c, -140, 0, 150, 0, INK2, a, 4, dash=[12, 10])
    for k, h in enumerate((-80, 60, -40, 100, -60)):
        x = -125 + k * 55
        y0, y1 = (h, 0) if h < 0 else (0, h)
        rrect(c, x, min(y0, y1) if h < 0 else 0, 38, abs(h), 6, BLUE if h < 0 else PURPLE, a)
    ftext(c, "| desvio |", 0, 140, 30, "black", INK, a, align="center")


def moeda(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 30, 90, "black", "#FFFFFF", a, align="center")


def globo(c, a):
    c.drawCircle(0, 0, 140, paint(mix("#FFFFFF", AGUA, 0.8), a))
    c.drawCircle(0, 0, 140, paint(INK2, a, stroke=7))
    p = skia.Path(); p.moveTo(-60, -110); p.quadTo(10, -60, -30, -10); p.quadTo(-90, 20, -60, 80); p.lineTo(-120, 40)
    p.quadTo(-140, -40, -60, -110); p.close()
    c.drawPath(p, paint(GREEN, a))
    p = skia.Path(); p.moveTo(40, -50); p.lineTo(130, -30); p.quadTo(120, 60, 60, 110); p.quadTo(20, 30, 40, -50); p.close()
    c.drawPath(p, paint(GREEN, a))


AREA_F = (gota, raio, celular, relogio, termometro, estrada, regua, barras, moeda, globo)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# mini gráficos da Q2 (consumo 0–10 GB × conta R$ 0–90)
# ======================================================================

GRAF = {
    "A": ("reta", [(0, 0), (10, 60)]),
    "B": ("reta", [(0, 30), (10, 90)]),
    "C": ("salto", [[(0, 30), (5, 30)], [(5, 60), (10, 90)]]),
    "D": ("escada", None),
    "E": ("reta", [(0, 30), (5, 30), (10, 60)]),
}


def mini_graf(c, L, x, y, w, h, a, marca=0.0):
    """mini gráfico da alternativa L em (x, y, w, h); marca > 0 desenha os pontos de teste (2, 30) e (8, 48)"""
    if a <= 0:
        return
    ox, oy = x + 34, y + h - 26
    gw, gh = w - 54, h - 48
    X = lambda v: ox + gw * v / 10
    Y = lambda v: oy - gh * v / 90
    line(c, ox, oy, ox + gw + 6, oy, INK2, a, 3)
    line(c, ox, oy, ox, oy - gh - 6, INK2, a, 3)
    ftext(c, "30", ox - 6, Y(30) + 7, 18, "bold", GRAY, a, align="right")
    line(c, X(5), oy - 6, X(5), oy + 6, INK2, a, 3)
    ftext(c, "5", X(5), oy + 22, 18, "bold", GRAY, a, align="center")
    kind, pts = GRAF[L]
    pen = paint(PURPLE, a, stroke=6)
    if kind == "reta":
        p = skia.Path(); p.moveTo(X(pts[0][0]), Y(pts[0][1]))
        for u, v in pts[1:]:
            p.lineTo(X(u), Y(v))
        c.drawPath(p, pen)
    elif kind == "salto":
        for seg in pts:
            p = skia.Path(); p.moveTo(X(seg[0][0]), Y(seg[0][1])); p.lineTo(X(seg[1][0]), Y(seg[1][1]))
            c.drawPath(p, pen)
        c.drawCircle(X(5), Y(30), 6, paint(PURPLE, a))
        c.drawCircle(X(5), Y(60), 6, paint("#FFFFFF", a)); c.drawCircle(X(5), Y(60), 6, paint(PURPLE, a, stroke=3))
    else:
        p = skia.Path(); p.moveTo(X(0), Y(30)); p.lineTo(X(5), Y(30))
        c.drawPath(p, pen)
        for k in range(5):
            v = 30 + 6 * (k + 1)
            p = skia.Path(); p.moveTo(X(5 + k), Y(v)); p.lineTo(X(6 + k), Y(v))
            c.drawPath(p, pen)
    if marca > 0:
        for u, v in ((2, 30), (8, 48)):
            c.drawCircle(X(u), Y(v), 9, paint(GREEN, marca))
            c.drawCircle(X(u), Y(v), 9, paint("#FFFFFF", marca, stroke=3))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    a0 = ep(t, C["01.a"], 0.5)
    if a0 > 0:
        rrect(c, 560, 200, 800, 110, 55, "#FFFFFF", a0, shadow=True)
        s = "“função modular”"
        text_mid(c, s, W / 2, 255, 52, "black", INK2, a0)
        strike(c, W / 2 - ftw(s, 52) / 2 - 10, 258, W / 2 + ftw(s, 52) / 2 + 10, 258, ep(t, C["01.a"] + 1.4, 0.4), RED)
    for k, (s, ic, col) in enumerate((("CONTA DE ÁGUA", 0, BLUE), ("ESTACIONAMENTO", 3, PURPLE),
                                      ("TOLERÂNCIA DE 2 mm", 6, AMBER))):
        a, d = rise(t, C["01.b"] + 0.7 * k)
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 350 + d, 480, 300, 26, mix("#F7F7F5", col, 0.12), a)
        area_icone(c, ic, x, 470 + d, 0.48, a)
        fit(c, s, x, 615 + d, 38, 440, "black", col, a, align="center")
        arrow(c, x, 660 + d, 960, 705, INK2, a * ep(t, C["01.c"], 0.4) * 0.7, 4, 12)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 510, 710, 900, 100, 50, mix("#FFFFFF", PURPLE, 0.14), ac, shadow=True)
        text_mid(c, "A FUNÇÃO POR TRÁS DO TEXTO", W / 2, 760, 46, "black", PURPLE, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 330, 760, AMBER, ad, 26)
        chip(c, "5 QUESTÕES NOVAS", 1590, 760, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 26)


COBRA = [("02.a", "TARIFA POR FAIXAS", "água · energia · frete · celular", BLUE, 1),
         ("02.b", "QUAL GRÁFICO?", "trechos fixos · saltos · inclinações", PURPLE, 2),
         ("02.c", "TOLERÂNCIA", "|x − 50| ≤ 2", AMBER, 6),
         ("02.d", "DISTÂNCIA NA RETA", "quanto falta · quanto passou", GREEN, 5)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO FORMAS", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 250 + d, 380, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 30, "black", col, a, 340, 38, align="center")
        area_icone(c, ic, x, 560 + d, 0.42, a)
        if k == 2:
            fit(c, sub, x, 710 + d, 40, 340, "black", AMBER, a, align="center")
        else:
            para(c, nb(sub), x, 690 + d, 26, "bold", INK2, a, 340, 32, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DUAS HABILIDADES", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate((("03.a", "DESCUBRA A FAIXA ANTES", "a lei certa depende da entrada", PURPLE, 0),
                                                  ("03.b", "CADA PARTE NA SUA FAIXA", "não o valor todo na taxa da última", GREEN, 1))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 290
        rrect(c, 200, y + d, 1520, 250, 26, mix("#F7F7F5", col, 0.10), a, shadow=True)
        badge_num(c, k + 1, 280, y + 125 + d, a, 36, bg=col)
        icone(c, ic, 470, y + 125 + d, 0.48, a)
        fit(c, tit, 640, y + 115 + d, 54, 1040, "black", col, a)
        fit(c, sub, 640, y + 180 + d, 34, 1040, "bold", INK2, a)


INDICE = [("EP. 1", "o prédio de andares · cada faixa parte de onde a anterior parou · hora ou fração é catraca"),
          ("EP. 2", "a escada de caixinhas · “excedente” é o alarme · a parcela a deduzir é o troco"),
          ("EP. 3", "módulo é distância · o vértice mora onde o de dentro zera · o espelho no chão"),
          ("EP. 4", "menor fica entre, maior fica fora · o elástico preso no centro")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 360, 380, 1200, 160, 30, "#FFFFFF", aq, shadow=True)
        text_mid(c, "1º passo numa função por partes?", W / 2, 460, 54, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 2.2, 1500, 640, a=aq)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 358 + k * 400
        y = 210
        rrect(c, x - 190, y, 380, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 190, y, 380, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 170, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.58, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para(c, nb(ln), x, yy, 26, "black", INK if on_ else INK2, a, 330, 32, align="center") + 10


ONDE = [("06.a", "FÍSICA", 5, "vai 3 km, volta 3 km", "deslocamento 0 · percurso 6 km · erro x ± Δx", BLUE),
        ("06.b", "ESTATÍSTICA", 7, "desvio médio absoluto", "o módulo impede que os desvios se anulem", PURPLE),
        ("07.c", "FINANCEIRA", 8, "imposto progressivo", "cada parte na sua alíquota", GREEN),
        ("07.d", "GEOGRAFIA", 4, "|9 − (−4)| = 13 °C", "amplitude térmica", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "O MESMO MÓDULO, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 220 + d, 380, 600, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 30, "black", col, a, 360, 36, align="center")
        area_icone(c, ic, x, 450 + d, 0.42, a)
        fit(c, lei_, x, 630 + d, 32, 340, "black", INK, a, align="center")
        para(c, nb(res), x, 680 + d, 25, "bold", INK2, a, 340, 31, align="center")


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    a, d = rise(t, C["08.a"])
    if a > 0:
        rrect(c, 120, 230 + d, 1000, 600, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, 1, 190, 300 + d, a, 34, bg=GREEN)
        fit(c, "LOCALIZE A FAIXA ANTES DE CALCULAR", 250, 315 + d, 40, 840, "black", GREEN, a)
        # a conta de água: o 26 com a etiqueta da linha que ele usa
        rrect(c, 170, 380 + d, 900, 260, 18, "#FFFFFF", a, shadow=True)
        regras = [("40", "se 0 ≤ x ≤ 10"), ("40 + 6(x − 10)", "se 10 < x ≤ 20"), ("100 + 9(x − 20)", "se x > 20")]
        for j, (lei_, cond) in enumerate(regras):
            acesa = j == 2 and ep(t, C["08.a"] + 2.5, 0.4) > 0
            col = PURPLE if acesa else INK2
            fit(c, lei_, 210, 440 + j * 70 + d, 34, 420, "black", col, a)
            fit(c, cond, 660, 440 + j * 70 + d, 32, 380, "bold", col, a)
        ae = ep(t, C["08.a"] + 2.5, 0.4) * a
        if ae > 0:
            pill(c, "x = 26 → 3ª linha", 620, 690 + d, PURPLE, size=30, a=ae, anchor="center")
        a2 = ep(t, C["08.a2"], 0.4) * a
        if a2 > 0:
            selo(c, 620, 790 + d, a2, "FRONTEIRA: CONFIRA O ≤", AMBER, -2, 32)
    for k, (cue, n, tit, sub) in enumerate((("09.b", "2", "TESTE DOIS PONTOS", "um de cada faixa | horizontal = fixo · salto = mudou a regra"),
                                            ("09.c", "3", "MÓDULO = DISTÂNCIA", "desenhe a reta | confira substituindo"))):
        ak, dk = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 310
        rrect(c, 1160, y + dk, 600, 290, 24, mix("#F7F7F5", GREEN, 0.10), ak)
        badge_num(c, n, 1230, y + 60 + dk, ak, 30, bg=GREEN)
        fit(c, tit, 1285, y + 74 + dk, 36, 450, "black", GREEN, ak)
        yy = y + 150 + dk
        for ln in sub.split(" | "):
            yy += para(c, nb(ln), 1460, yy, 28, "bold", INK, ak, 540, 34, align="center") + 8


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["10.t"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["10.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["10.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["10.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone do episódio)
VF = [
    ("distância até o zero", "|x| = 5 ⇒ x = 5", False, "o 5 está ali, pronto",
     "dois pontos estão a 5 do zero", "x = 5 ou x = −5", 2),
    ("distância nunca é negativa", "|x| = −3 não tem solução", True, "dá vontade de escrever ± 3",
     "módulo nunca é negativo", "conjunto vazio", 2),
    ("menor fica entre", "|x| < 4 ⇒ x < ± 4", False, "imita a equação",
     "“menor que” fica entre", "−4 < x < 4", 3),
    ("onde o de dentro zera", "|x − 3|: o V vai 3 para a esquerda", False, "o “menos” parece “para trás”",
     "o vértice está onde x − 3 = 0", "x = 3 · direita", 2),
    ("módulo da soma", "|a + b| = |a| + |b| sempre", False, "funciona com dois positivos",
     "|−3 + 3| = 0, mas |−3| + |3| = 6", "só com o mesmo sinal", 2),
    ("raiz do quadrado", "√(x²) = |x|", True, "a raiz parece desfazer o quadrado",
     "teste −5: √25 = 5, positivo", "√(x²) = |x|", 2),
    ("a escada de caixinhas", "progressivo: última alíquota sobre tudo", False, "a tabela mostra a faixa onde o lucro parou",
     "cada fatia paga a taxa da sua caixinha", "faixa por faixa", 1),
    ("o prédio de andares", "primeiro a faixa, depois a lei", True, "a 1ª linha está bem ali",
     "o andar decide a regra · na fronteira, o ≤", "faixa → lei", 0),
    ("a catraca", "R$ 5/h ou fração: 2 h 20 min = R$ 11,67", False, "a conta proporcional parece justa",
     "começou a hora, pagou inteira", "3 h = R$ 15,00", 0),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 410, 0.55, a0)
    text(c, ctx.upper(), 960, 300, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    s = nb(conta)
    sz = 50
    while ftw(s, sz) > 760 and sz > 38:
        sz -= 2
    lines = [s] if ftw(s, sz) <= 760 else _quebra(s, sz, 760)
    riscos = []
    for j, ln in enumerate(lines):
        yj = 410 + (j - (len(lines) - 1) / 2) * (sz + 12)
        fmid(c, ln, 960, yj, sz, "black", INK, a0)
        riscos.append((ftw(ln, sz), yj + 4))
    if ar > 0 and not ver:
        for w, yl in riscos:
            strike(c, 960 - w / 2 - 10, yl, 960 + w / 2 + 10, yl, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        fit(c, engana, 640 if ver else 520, 552, 34, 1020 if ver else 1140, "bold", INK2, ae)
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = _quebra(nb(regra_), 30, 820)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 725 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1420, 735, 48, 520, "black", GREEN, ag, align="center")


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["20.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["20.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["20.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    if ab > 0:
        rrect(c, W / 2 - 520, 700, 1040, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "ache a faixa ou a distância · resolva · confira", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="QUANTO VEM NA CONTA?", area="ENERGIA PROGRESSIVA", ic=1, ok="C",
               enun=[("a", "Até 100 kWh: R$ 0,50 por kWh. De 100 a 200: R$ 0,80 por kWh excedente. Acima de 200: "
                           "R$ 1,10 por kWh excedente.", False),
                     ("b", "Quanto paga quem consome 250 kWh?", True)],
               alts=[("A", "R$ 125,00", "1ª taxa sobre tudo", RED), ("B", "R$ 170,00", "esqueceu a 3ª faixa", AMBER),
                     ("C", "R$ 185,00", "", GREEN), ("D", "R$ 215,00", "pulou a faixa do meio", AMBER),
                     ("E", "R$ 275,00", "última taxa sobre tudo", RED)],
               passos=[("d", "“excedente” → progressivo"), ("a", "100 · 0,50 = 50"), ("a", "100 · 0,80 = 80"),
                       ("a", "50 · 1,10 = 55"), ("a", "50 + 80 + 55 = R$ 185")],
               confere=None),
    "q3": dict(ids=("25", "26"), titulo="HORA OU FRAÇÃO", area="ALUGUEL DE BICICLETA", ic=3, ok="D",
               enun=[("a", "R$ 8,00 pela 1ª meia hora e R$ 3,00 por meia hora adicional ou fração.", False),
                     ("b", "Quanto paga quem usa por 1 h 50 min?", True)],
               alts=[("A", "R$ 12,00", "esqueceu a 1ª tarifa", RED), ("B", "R$ 14,00", "ignorou a fração", AMBER),
                     ("C", "R$ 16,00", "fração proporcional", AMBER), ("D", "R$ 17,00", "", GREEN),
                     ("E", "R$ 20,00", "4 meias horas adicionais", RED)],
               passos=[("d", "1 h 50 min = 110 min"), ("d", "110 − 30 = 80 min"), ("a", "80 = 30 + 30 + 20 → 3 adicionais"),
                       ("a", "8 + 3 · 3 = R$ 17")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="O ELÁSTICO DA CÂMARA FRIA", area="TOLERÂNCIA", ic=4, ok="A",
               enun=[("a", "Uma câmara fria deve ficar a no máximo 1,5 °C de −18 °C.", False),
                     ("b", "As temperaturas T permitidas são:", True)],
               alts=[("A", "−19,5 ≤ T ≤ −16,5", "", GREEN), ("B", "16,5 ≤ T ≤ 19,5", "errou o sinal do centro", RED),
                     ("C", "−18,75 ≤ T ≤ −17,25", "dividiu a tolerância por 2", AMBER),
                     ("D", "−19,5 < T < −16,5", "tirou as pontas", AMBER),
                     ("E", "T ≤ −19,5 ou T ≥ −16,5", "pegou o “fora”", RED)],
               passos=[("d", "centro −18 · estica 1,5"), ("d", "|T + 18| ≤ 1,5"), ("a", "−19,5 ≤ T ≤ −16,5")],
               confere=("a", "“no máximo” inclui as pontas")),
    "q5": dict(ids=("29", "30"), titulo="ONDE ESTÁ O ENTREGADOR?", area="DISTÂNCIA NA RETA", ic=5, ok="B",
               enun=[("a", "Numa avenida retilínea, um entregador está a 7 km do km 30.", False),
                     ("b", "Em que quilômetro ele pode estar?", True)],
               alts=[("A", "só no km 37", "esqueceu um lado", AMBER), ("B", "no km 23 ou no km 37", "", GREEN),
                     ("C", "só no km 23", "esqueceu um lado", AMBER), ("D", "no km 23 ou no km 30", "o centro não é resposta", RED),
                     ("E", "no km −23 ou no km 37", "errou o sinal", RED)],
               passos=[("d", "|x − 30| = 7"), ("a", "30 − 7 = 23  ·  30 + 7 = 37")],
               confere=("v", "|23 − 30| = 7 · |37 − 30| = 7")),
}


def reta_q5(c, x0, y0, w, a, prog):
    """a avenida: o km 30 no centro e os dois pontos a 7 km"""
    if a <= 0:
        return
    X = lambda v: x0 + w * (v - 18) / 24
    line(c, X(18), y0, X(42), y0, INK2, a, 5)
    for v in (20, 25, 30, 35, 40):
        line(c, X(v), y0 - 10, X(v), y0 + 10, INK2, a, 3)
    c.drawCircle(X(30), y0, 13, paint(PURPLE, a))
    ftext(c, "30", X(30), y0 + 46, 28, "black", PURPLE, a, align="center")
    if prog > 0:
        for v in (23, 37):
            arrow(c, X(30), y0 - 30, X(30) + (X(v) - X(30)) * prog, y0 - 30, GREEN, a, 5, 14)
            if prog > 0.95:
                c.drawCircle(X(v), y0, 13, paint(GREEN, a))
                ftext(c, str(v), X(v), y0 + 46, 28, "black", GREEN, a, align="center")
        ftext(c, "7", (X(30) + X(23)) / 2, y0 - 46, 26, "black", GREEN, a * prog, align="center")
        ftext(c, "7", (X(30) + X(37)) / 2, y0 - 46, 26, "black", GREEN, a * prog, align="center")


def elastico_q4(c, x0, y0, w, a, prog):
    """o elástico preso em −18, esticado 1,5 para cada lado"""
    if a <= 0:
        return
    X = lambda v: x0 + w * (v + 21) / 6
    line(c, X(-21), y0, X(-15), y0, INK2, a, 5)
    for v in (-20, -19, -18, -17, -16):
        line(c, X(v), y0 - 10, X(v), y0 + 10, INK2, a, 3)
    e = 1.5 * prog
    if prog > 0:
        rrect(c, X(-18 - e), y0 - 12, X(-18 + e) - X(-18 - e), 24, 12, GREEN, a * 0.6)
        for v in (-18 - e, -18 + e):
            c.drawCircle(X(v), y0, 12, paint(GREEN, a))
    c.drawCircle(X(-18), y0, 13, paint(PURPLE, a))
    ftext(c, "−18", X(-18), y0 + 46, 26, "black", PURPLE, a, align="center")
    if prog > 0.95:
        ftext(c, "−19,5", X(-19.5), y0 - 28, 24, "black", GREEN, a, align="center")
        ftext(c, "−16,5", X(-16.5), y0 - 28, 24, "black", GREEN, a, align="center")


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · {d['area']}", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, [(L, nb(s), w, col) for L, s, w, col in d["alts"]],
                       880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, d["ic"], 770, 222, 0.26, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 290
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 66
            if nome == "q5":
                reta_q5(c, 200, yy + 70, 600, sol, ep(t, C[f"{s2}.a"], 1.0))
                yy += 130
            if nome == "q4":
                elastico_q4(c, 200, yy + 60, 600, sol, ep(t, C[f"{s2}.d"] + 0.4, 1.2))
                yy += 110
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"] + 1.6, 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 760, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


Q2_WHY = {"A": "sai da origem: f(2) = 12", "B": "sobe desde o zero: f(2) = 42", "C": "salto: cobrou a franquia de novo",
          "D": "escada: o texto não diz “ou fração”"}


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 DE 5 · QUAL GRÁFICO?", "O PLANO COM FRANQUIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23"], 0.5)
    pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
    text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
    sol = ep(t, C["24"], 0.5)
    area_icone(c, 2, 770, 222, 0.26, a0 * (1 - sol))
    y = 280
    for cue, s, dest in (("a", "Plano de celular: R$ 30,00 com 5 GB de franquia e R$ 6,00 por GB excedente.", False),
                         ("b", "Qual gráfico representa a conta (R$) em função do consumo (GB)?", True)):
        a = ep(t, C[f"23.{cue}"], 0.4) * (1 - sol)
        y += para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40) + 18
    pause_timer(c, t, C["23.end"] - 1.9, 720, 760)
    if sol > 0:
        passos = [("d", "f(2) = 30 (dentro da franquia)"), ("d", "f(8) = 30 + 3 · 6 = 48"),
                  ("xd", "sem “ou fração”: o meio é reta"), ("ok", "horizontal até 5, depois sobe, sem salto")]
        yy = 300
        for j, (cue, s) in enumerate(passos):
            a = ep(t, C[f"24.{cue}"] + (1.6 if j == 1 else 0), 0.4) * sol
            fit(c, s, 180, yy + 14, 32, 640, "black", GREEN if j == 3 else INK, a)
            yy += 74
        result_box(c, "Letra E", 490, 690, 38, ep(t, C["24.ok"], 0.5), GREEN)
    aok = ep(t, C["24.ok"], 0.5)
    pos = {"A": (880, 225), "B": (1170, 225), "C": (1460, 225), "D": (1025, 520), "E": (1315, 520)}
    for L, (x, yb) in pos.items():
        a, dd = rise(t, C[f"23.l{L.lower()}"])
        if a <= 0:
            continue
        ok = L == "E"
        ax = ep(t, C[f"24.x{L.lower()}"], 0.4) if not ok else 0
        col = mix("#FFFFFF", GREEN, 0.18 * aok) if ok else "#FFFFFF"
        rrect(c, x, yb + dd, 270, 270, 18, col, a, shadow=True)
        if ok and aok > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, yb + dd, 270, 270), 18, 18), paint(GREEN, aok, stroke=6))
        badge_num(c, L, x + 30, yb + 30 + dd, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
        mini_graf(c, L, x + 10, yb + 50 + dd, 250, 200, a * (1 - 0.5 * ax), marca=ep(t, C["24.d"] + 2.2, 0.4) * sol)
        if ax > 0:
            check_icon(c, x + 240, yb + 30 + dd, 18, ax, RED, "x")
            rrect(c, x + 6, yb + 226 + dd, 258, 38, 8, "#FFFFFF", ax * 0.92)
            fit(c, Q2_WHY[L], x + 135, yb + 254 + dd, 20, 250, "bold", RED, ax, align="center")


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["tarifa: parte fixa + excedente", "a faixa antes da lei", "“hora ou fração”: para cima"]),
         ("31.c", "EP. 2", 1, ["progressivo faixa por faixa", "parcela a deduzir"]),
         ("32.a", "EP. 3", 2, ["|a − b| = distância", "V de |x − a| + b", "|f(x)|: rebate o de baixo"]),
         ("32.b", "EP. 4", 3, ["|A| = k: dois casos", "≤ entre · > fora", "tolerância → |x − a| ≤ k"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 210), (150, 480), (990, 210), (990, 480)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 55, y0 + 130, 0.24, a)
        for j, it in enumerate(itens):
            yy = y0 + 40 + j * 62
            rrect(c, x + 150, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 198, yy + 10, 28, 580, "bold", INK, a)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        boxed(c, 560, 760, 800, 90, AMBER, ac, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 805, 34, "black", INK, ac)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["33.a"], 0.5)
    ab = ep(t, C["33.b"], 0.5)
    ac = ep(t, C["33.c"], 0.5)
    for i in range(25):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 18
        x, y = 200 + k * 82, 230 + r_ * 90
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 66, 72, 12, col, a)
        if ac > 0 and i < 10:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 80), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "25 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "18 acertos", 1450, 400, 46, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 580, 1520, 180, BLUE, ac, 0.08)
        for k, ic in enumerate((0, 1, 2)):
            area_icone(c, ic, 290 + k * 110, 670, 0.22, ac)
        text_mid(c, "10 DE TARIFAS OU GRÁFICO POR PARTES", 1100, 640, 42, "black", BLUE, ac)
        text_mid(c, "água · energia · celular · estacionamento", 1100, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função composta", W / 2, 350, 76, "black", PURPLE, aa)
    text(c, "e função inversa", W / 2, 420, 40, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.6)
    if ab > 0:
        for k, (s, col) in enumerate((("x", INK2), ("g", BLUE), ("f", PURPLE), ("f(g(x))", GREEN))):
            x = 520 + k * 300
            if k < 3:
                rrect(c, x - 90, 520, 180, 130, 22, mix("#FFFFFF", col, 0.16) if k else "#FFFFFF", ab, shadow=True)
            fmid(c, s, x, 585, 60 if k < 3 else 50, "black", col, ab)
            if k < 3:
                arrow(c, x + 100, 585, x + 195, 585, INK2, ab * ep(t, C["34.b"] + 0.5 * k, 0.4), 5, 14)
        fit(c, "uma dentro da outra", W / 2, 700, 34, 900, "bold", INK2, ab, align="center")
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        arrow(c, 1420, 760, 520, 760, AMBER, ac, 6, 18)
        selo(c, W / 2, 800, ac, "E DESFEITAS", AMBER, -3, 34)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=b_q2,
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
