"""Visual — Função Modular e Funções por Partes, Episódio 3: módulo é distância (o gráfico em V e o rebatimento) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: linha() (texto com cor por trecho), Plano (eixos com escala própria; curva() desenha y = f(x) aos
poucos; ponto()), reta_num() (reta numérica com marcas e pontos), boneco() (bonequinho que caminha na régua),
regua_k() (a régua horizontal y = k com os cortes de |x² − 4| contados), contador() (chip com o número de cortes).
Expressões com barras de módulo vão como TEXTO (ftext): o expr do 019 trata o "−" como operador e afastaria o sinal.
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
import math
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
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_modular_ep3_modulo_distancia.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else (cx - sum(ws) if align == "right" else cx)
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def t1(c, s, cx, cy, size, a, col=None, peso="black", align="center"):
    """uma expressão/texto de uma cor só, centrado verticalmente em cy"""
    return linha(c, [(s, col or INK)], cx, cy, size, a, peso, align)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def ease_out(u):
    return 1 - (1 - clamp(u)) ** 3


def fmt(v):
    s = f"{v:g}".replace(".", ",")
    return s.replace("-", "−")


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, grade=True, rot=("x", "y")):
        if a <= 0:
            return
        if grade:
            for v in xt:
                line(c, s.px(v), s.y0, s.px(v), s.y0 + s.h, GRADE, a, 2)
            for v in yt:
                line(c, s.x0, s.py(v), s.x0 + s.w, s.py(v), GRADE, a, 2)
        oy = s.py(0) if s.yr[0] <= 0 <= s.yr[1] else s.y0 + s.h
        ox = s.px(0) if s.xr[0] <= 0 <= s.xr[1] else s.x0
        arrow(c, s.x0, oy, s.x0 + s.w + 24, oy, INK2, a, 3, 12)
        arrow(c, ox, s.y0 + s.h, ox, s.y0 - 22, INK2, a, 3, 12)
        text(c, rot[0], s.x0 + s.w + 22, oy + 36, 24, "black", GRAY, a)
        text(c, rot[1], ox - 22, s.y0 - 6, 24, "black", GRAY, a, align="right")
        for v in xt:
            if v == 0:
                continue
            text(c, fmt(v), s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v == 0:
                continue
            text(c, fmt(v), ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def _clip(s, c):
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))

    def curva(s, c, a, f, col, u=1.0, width=7, xa=None, xb=None, n=240, dash=None):
        """y = f(x) de xa a xb (recortada no retângulo); u = fração já desenhada"""
        if a <= 0 or u <= 0:
            return
        xa = s.xr[0] if xa is None else xa
        xb = s.xr[1] if xb is None else xb
        xe = xa + (xb - xa) * clamp(u)
        s._clip(c)
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xe - xa) * k / n
            y = max(min(f(x), s.yr[1] + 6), s.yr[0] - 6)
            (path.moveTo if k == 0 else path.lineTo)(s.px(x), s.py(y))
        pt = paint(col, a, stroke=width, cap_round=True)
        if dash:
            pt.setPathEffect(skia.DashPathEffect.Make(list(dash), 0))
        c.drawPath(path, pt)
        c.restore()

    def ponto(s, c, x, y, col, a, rot_=None, dx=18, dy=-30, size=22, r=9, anchor="left"):
        if a <= 0:
            return
        c.drawCircle(s.px(x), s.py(y), r + 3, paint("#FFFFFF", a))
        c.drawCircle(s.px(x), s.py(y), r, paint(col, a))
        if rot_:
            pill(c, rot_, s.px(x) + dx, s.py(y) + dy, col, size=size, a=a, anchor=anchor, bounds=(0, 1920))

    def hreta(s, c, y, col, a, width=5, dash=(16, 10)):
        if a <= 0:
            return
        line(c, s.x0, s.py(y), s.x0 + s.w, s.py(y), col, a, width, dash=dash)


def reta_num(c, x0, x1, y, vmin, vmax, a, rotulos=True, size=26, passo=1):
    """reta numérica com marcas inteiras; devolve a função valor → x"""
    px = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    if a <= 0:
        return px
    arrow(c, x0 - 30, y, x1 + 40, y, INK2, a, 4, 14)
    v = vmin
    while v <= vmax + 1e-9:
        big = abs(v) < 1e-9
        line(c, px(v), y - (16 if big else 10), px(v), y + (16 if big else 10), INK if big else INK2, a, 4 if big else 3)
        if rotulos:
            text(c, fmt(v), px(v), y + 46, size, "black" if big else "bold", INK if big else INK2, a)
        v += passo
    return px


def boneco(c, x, ybase, col, a, s=1.0, passo=0.0):
    """bonequinho em pé com os pés em ybase; passo (0–1, cíclico) mexe as pernas"""
    if a <= 0:
        return
    ph = math.sin(passo * math.pi * 2) * 14 * s
    hip = ybase - 46 * s
    neck = ybase - 98 * s
    c.drawCircle(x, neck - 20 * s, 18 * s, paint(col, a))
    line(c, x, neck, x, hip, col, a, 9 * s)
    line(c, x, hip, x - 14 * s + ph, ybase, col, a, 9 * s)
    line(c, x, hip, x + 14 * s - ph, ybase, col, a, 9 * s)
    line(c, x, neck + 12 * s, x - 22 * s - ph * 0.6, neck + 44 * s, col, a, 8 * s)
    line(c, x, neck + 12 * s, x + 22 * s + ph * 0.6, neck + 44 * s, col, a, 8 * s)


def contador(c, n, cx, cy, a, col=None, rot_="cortes", size=64):
    """chip grande com um número (passos, cortes)"""
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, cx - 110, cy - 70, 220, 140, 26, mix("#FFFFFF", col, 0.14), a)
    text_mid(c, str(n), cx, cy - 12, size, "black", col, a)
    text(c, rot_, cx, cy + 50, 24, "black", INK2, a)


def g(x):
    return abs(x * x - 4)


def cortes(k):
    """pontos onde |x² − 4| = k (sem repetição, em ordem)"""
    if k < 0:
        return []
    out = set()
    for q in (4 + k, 4 - k):
        if q > 0:
            out |= {math.sqrt(q), -math.sqrt(q)}
        elif q == 0:
            out.add(0.0)
    return sorted(out)


def regua_k(c, P, k, a, col=None):
    """a régua horizontal y = k sobre o gráfico de |x² − 4|, com os cortes marcados"""
    if a <= 0:
        return 0
    col = col or AMBER
    line(c, P.x0 - 10, P.py(k), P.x0 + P.w + 10, P.py(k), col, a, 6)
    pill(c, f"y = {fmt(round(k, 1))}", P.x0 + P.w + 14, P.py(k), col, size=22, a=a, anchor="left", bounds=(0, 1920))
    xs = cortes(k)
    for x in xs:
        if P.xr[0] <= x <= P.xr[1]:
            P.ponto(c, x, k, RED, a, r=11)
    return len(xs)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO MODULAR · EPISÓDIO 3", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 230, 1440, 170, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("|−3|", BLUE), ("  +  ", INK2), ("|3|", BLUE), ("   =   ", INK2), ("6", GREEN)], W / 2, 315, 96, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 240, 440, 1440, 170, 26, "#FFFFFF", ab, shadow=True)
        linha(c, [("|−3 + 3|", PURPLE), ("   =   ", INK2), ("0", RED)], W / 2, 525, 96, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 680, acc, "MESMAS BARRINHAS · RESULTADOS DIFERENTES", AMBER, -2, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        P = Plano(1380, 690, 300, 140, (-2.2, 2.2), (-0.2, 2.2))
        P.curva(c, ad, abs, GREEN, u=ep(t, C["01.d"] + 0.3, 1.2), width=8)
        pill(c, "um V de presente", 1160, 780, GREEN, size=26, a=ad, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO MODULAR · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de FUNÇÃO MODULAR E FUNÇÕES POR PARTES", W / 2, 240, BLUE, size=28, a=a0,
             anchor="center")
    itens = [("02.a", "CALCULAR", "módulos", BLUE), ("02.b", "ACHAR O VÉRTICE", "de qualquer V", PURPLE),
             ("02.c", "CONTAR SOLUÇÕES", "no gráfico rebatido", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 330, 480, 340, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 240, 330, 480, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 580, 38, "black", col, ak)
        text(c, sub, x, 635, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 230, 720, 560, 24, "#FFFFFF", aa, shadow=True)
        pill(c, "série de Operações", 560, 270, BLUE, size=22, a=aa, anchor="center")
        reta_num(c, 260, 860, 420, -5, 5, aa, size=22)
        rrect(c, 260, 360, 300, 50, 12, mix("#FFFFFF", RED, 0.12), aa * 0.9)
        text(c, "negativos", 410, 395, 24, "black", RED, aa)
        t1(c, "−(−7) = 7", 560, 620, 72, ep(t, C["03.a"] + 2.5, 0.5), PURPLE)
        text(c, "menos com menos dá mais", 560, 720, 28, "bold", INK2, ep(t, C["03.a"] + 2.5, 0.5))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 720, 560, 24, "#FFFFFF", ab, shadow=True)
        pill(c, "série de Função quadrática", 1360, 270, PURPLE, size=22, a=ab, anchor="center")
        P = Plano(1120, 330, 480, 360, (-3.2, 3.2), (-4.8, 5.4))
        P.eixos(c, ab, xt=(), yt=(), grade=False)
        P.curva(c, ab, lambda x: x * x - 4, PURPLE, u=ep(t, C["03.b"] + 0.4, 1.4), width=6)
        a2 = ep(t, C["03.b"] + 4.0, 0.4)
        P.ponto(c, -2, 0, BLUE, a2, "−2", dx=-60, dy=-34, size=20)
        P.ponto(c, 2, 0, BLUE, a2, "2", dx=16, dy=-34, size=20)
        P.ponto(c, 0, -4, AMBER, ep(t, C["03.b"] + 6.5, 0.4), "vértice (0, −4)", dx=20, dy=6, size=20)
        t1(c, "y = x² − 4", 1360, 740, 44, ab, PURPLE)


# ======================================================================
# concreto · bloco a — definição
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA RÉGUA NO CHÃO", "DISTÂNCIA NÃO TEM SINAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.4)
    px = reta_num(c, 260, 1660, 520, -5, 5, a0, size=28)
    aa = ep(t, C["04.a"], 0.5)
    ab_t = C["04.b"]
    u = ease_io(clamp((t - ab_t - 0.4) / 2.6)) if t > ab_t else 0.0
    if aa > 0:
        for k, (v0, col) in enumerate(((-3, BLUE), (3, PURPLE))):
            x = px(v0 * (1 - 0.88 * u))
            boneco(c, x, 500, col, aa, 1.0, passo=u * 3 if 0 < u < 1 else 0)
            text(c, fmt(v0), px(v0), 300, 40, "black", col, aa)
            n = min(3, int(u * 3 + 1e-6))
            contador(c, n, 360 + k * 1200, 690, ep(t, ab_t, 0.5), col, "passos", 60)
        if u > 0:
            line(c, px(-3), 330, px(-3 * (1 - 0.88 * u)), 330, BLUE, aa, 6, dash=(12, 8))
            line(c, px(3), 330, px(3 * (1 - 0.88 * u)), 330, PURPLE, aa, 6, dash=(12, 8))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 640, 620, 640, 150, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("−4 °C", BLUE), ("  →  ", INK2), ("9 °C", RED)], 960, 665, 40, acc)
        linha(c, [("andou ", INK2), ("13 graus", GREEN)], 960, 730, 40, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "DISTÂNCIA NÃO TEM SINAL", W / 2, 215, ad, 36, BLUE)


def b_definicao(c, t, C, B):
    sid = which(t, C, ["05", "06"])
    head_seq(c, t, C, [("05", "O MÓDULO", "DISTÂNCIA ATÉ O ZERO", BLUE), ("06", "A REGRA ESCRITA", "O MÓDULO APAGA O SINAL",
                                                                        PURPLE)])
    card(c, *CARD_R)
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            defin(c, "RETA NUMÉRICA", "os números em ordem, com o zero no meio", 240, 200, 1440, aa, BLUE, 30)
            defin(c, "MÓDULO (VALOR ABSOLUTO)", "a distância do número até o zero", 240, 290, 1440,
                  ep(t, C["05.a"] + 2.2, 0.5), BLUE, 30)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            px = reta_num(c, 420, 1500, 560, -4, 4, ab, size=26)
            line(c, px(-3), 500, px(0), 500, BLUE, ab, 8)
            text(c, "3", (px(-3) + px(0)) / 2, 480, 34, "black", BLUE, ab)
            c.drawCircle(px(-3), 560, 13, paint(BLUE, ab))
            t1(c, "|−3| = 3", W / 2, 690, 80, ab, BLUE)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            regra(c, "MÓDULO É DISTÂNCIA: NUNCA É NEGATIVO", W / 2, 790, acc, 36)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 210, 1440, 120, 22, mix("#FFFFFF", PURPLE, 0.08), aa)
        linha(c, [("|x| = x", PURPLE), (",   se x ≥ 0", INK2)], W / 2, 270, 60, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 240, 360, 1440, 120, 22, mix("#FFFFFF", PURPLE, 0.08), ab)
        linha(c, [("|x| = −x", PURPLE), (",   se x < 0", INK2)], W / 2, 420, 60, ab)
        a2 = ep(t, C["06.b"] + 2.2, 0.5)
        if a2 > 0:
            rrect(c, 520, 530, 880, 130, 22, "#FFFFFF", a2, shadow=True)
            linha(c, [("|−7| = ", INK), ("−(−7)", AMBER), (" = 7", GREEN)], W / 2, 595, 66, a2)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        regra(c, "O −x DE UM NEGATIVO É POSITIVO", W / 2, 760, acc, 36, GREEN)


# ======================================================================
# bloco b — distância entre dois pontos · tabela · atalho
# ======================================================================

def b_dist(c, t, C, B):
    head(c, t, B["start"], "DISTÂNCIA ENTRE DOIS PONTOS", "O MÓDULO DA DIFERENÇA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 620, 200, 680, 120, 24, mix("#FFFFFF", PURPLE, 0.10), aa)
        linha(c, [("distância = ", INK2), ("|a − b|", PURPLE)], W / 2, 260, 56, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        px = reta_num(c, 340, 1580, 470, -3, 5, ab, size=26)
        for v, col in ((-2, BLUE), (4, PURPLE)):
            c.drawCircle(px(v), 470, 15, paint(col, ab))
        u = ease_out(ep(t, C["07.b"] + 0.6, 1.2))
        line(c, px(-2), 400, px(-2) + (px(4) - px(-2)) * u, 400, GREEN, ab, 8)
        text(c, "6", (px(-2) + px(4)) / 2, 380, 40, "black", GREEN, ab * u)
        a1 = ep(t, C["07.b"] + 1.5, 0.4)
        a2 = ep(t, C["07.b"] + 5.0, 0.4)
        rrect(c, 300, 590, 620, 110, 20, "#FFFFFF", a1, shadow=True)
        linha(c, [("|4 − (−2)| = ", INK), ("6", GREEN)], 610, 645, 48, a1)
        rrect(c, 1000, 590, 620, 110, 20, "#FFFFFF", a2, shadow=True)
        linha(c, [("|−2 − 4| = |−6| = ", INK), ("6", GREEN)], 1310, 645, 48, a2)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 785, acc, "A ORDEM NÃO IMPORTA", GREEN, -2, 32)


TAB = [("08.a", "|5 − 9|", "−4", "4"), ("08.b", "|9 − 5|", "4", "4"), ("08.c", "|−3| + |3|", "3 + 3", "6"),
       ("08.d", "|−3 + 3|", "0", "0")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "VAMOS TREINAR", "PRIMEIRO A CONTA DE DENTRO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    x0, y0, cw, rh = 320, 200, (440, 400, 300), 120
    if a0 > 0:
        rrect(c, x0, y0, sum(cw), 80, 18, mix("#FFFFFF", PURPLE, 0.12), a0)
        for k, s_ in enumerate(("expressão", "dentro / partes", "valor")):
            text(c, s_, x0 + sum(cw[:k]) + cw[k] / 2, y0 + 52, 28, "black", PURPLE, a0)
    for j, (cue, ex, de, va) in enumerate(TAB):
        aj, d = rise(t, C[cue])
        if aj <= 0:
            continue
        y = y0 + 100 + j * (rh + 10) + d
        rrect(c, x0, y, sum(cw), rh, 18, "#FFFFFF", aj, shadow=True)
        t1(c, ex, x0 + cw[0] / 2, y + rh / 2, 50, aj, INK)
        t1(c, de, x0 + cw[0] + cw[1] / 2, y + rh / 2, 46, ep(t, C[cue] + 1.2, 0.4), AMBER)
        t1(c, va, x0 + cw[0] + cw[1] + cw[2] / 2, y + rh / 2, 60, ep(t, C[cue] + 2.2, 0.4), GREEN)
    if ep(t, C["08.d"] + 4.0, 0.4) > 0:
        selo(c, 1560, 760, ep(t, C["08.d"] + 4.0, 0.4), "O GANCHO, RESOLVIDO", BLUE, -5, 26)


def b_atalho_dentro(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "MÓDULO SEM ERRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    K.atalho(c, 240, 200, 1440, 140, "ATALHO", ["1º a conta de DENTRO  ·  2º tire o sinal"], a0, 40)
    passos = [("09.a", "CONTA DE DENTRO", "|5 − 9|  →  |−4|", BLUE), ("09.b", "TIRE O SINAL", "|−4|  →  4", GREEN)]
    for k, (cue, tit, ex, col) in enumerate(passos):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 320, 400 + d, 640, 300, 26, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 470 + d, ak, 34, bg=col)
        text(c, tit, x, 570 + d, 38, "black", col, ak)
        t1(c, ex, x, 640 + d, 46, ak, INK)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 790, acc, "NESSA ORDEM, SEMPRE", GREEN, -2, 30)


# ======================================================================
# bloco c — armadilhas com letra
# ======================================================================

def b_letra(c, t, C, B):
    head(c, t, B["start"], "E COM LETRA?", "O MÓDULO NÃO TIRA O MENOS DE UMA LETRA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 210, 740, 420, 24, "#FFFFFF", aa, shadow=True)
        t1(c, "|−x| = x ?", 570, 290, 64, aa, AMBER)
        pill(c, "teste: x = −5", 570, 370, INK2, size=26, a=aa, anchor="center")
        t1(c, "|−(−5)| = |5| = 5", 570, 460, 46, ep(t, C["10.a"] + 2.0, 0.4), INK)
        a3 = ep(t, C["10.a"] + 4.5, 0.4)
        linha(c, [("5 é ", INK2), ("−x", RED), (", não x", INK2)], 570, 560, 44, a3)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 660, 740, 130, 24, mix("#FFFFFF", GREEN, 0.14), ab)
        t1(c, "|−x| = |x|", 570, 725, 64, ab, GREEN)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 210, 740, 580, 24, "#FFFFFF", acc, shadow=True)
        pill(c, "série de Potenciação", 1350, 250, PURPLE, size=22, a=acc, anchor="center")
        t1(c, "√(x²) = |x|", 1350, 380, 76, acc, GREEN)
        pill(c, "x = −5", 1350, 480, INK2, size=26, a=acc, anchor="center")
        t1(c, "√((−5)²) = √25 = 5", 1350, 580, 46, ep(t, C["10.c"] + 2.5, 0.4), INK)
        selo(c, 1350, 700, ep(t, C["10.c"] + 3.5, 0.4), "NÃO −5", RED, -4, 30)


# ======================================================================
# bloco d — a função |x| · bloco e — deslocamentos · bloco f — vértice
# ======================================================================

PTS_V = [(-2, 2), (-1, 1), (0, 0), (1, 1), (2, 2)]


def b_funcao_v(c, t, C, B):
    head(c, t, B["start"], "A FUNÇÃO f(x) = |x|", "O GRÁFICO EM V", BLUE)
    card(c, *CARD_R)
    P = Plano(260, 210, 760, 560, (-3, 3), (-0.8, 3.2))
    a0 = ep(t, C["11"], 0.4)
    P.eixos(c, a0, xt=(-2, -1, 1, 2), yt=(1, 2, 3))
    aa_t = C["11.a"] + 1.8
    for k, (x, y) in enumerate(PTS_V):
        ak = ep(t, aa_t + 0.9 * k, 0.3)
        P.ponto(c, x, y, BLUE, ak, None)
        if ak > 0:
            rrect(c, 1110, 220 + k * 64, 560, 56, 14, "#FFFFFF", ak, shadow=True)
            linha(c, [(f"x = {fmt(x)}", INK), ("   →   ", GRAY), (f"|x| = {fmt(y)}", BLUE)], 1390, 248 + k * 64, 30, ak)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        P.curva(c, ab, abs, BLUE, u=ep(t, C["11.b"], 1.2), width=8)
        P.ponto(c, 0, 0, AMBER, ep(t, C["11.b"] + 1.5, 0.4), "vértice", dx=20, dy=26, size=22)
        defin(c, "VÉRTICE", "onde o gráfico muda de direção", 1110, 560, 600, ep(t, C["11.b"] + 1.5, 0.4), AMBER, 24)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        pill(c, "y = x", P.px(2.2), P.py(2.6), GREEN, size=24, a=acc, anchor="left", bounds=(0, 1920))
        pill(c, "y = −x", P.px(-2.2), P.py(2.6), PURPLE, size=24, a=acc, anchor="right", bounds=(0, 1920))
        regra(c, "DUAS LEIS, UM GRÁFICO SÓ", 1410, 720, ep(t, C["11.c"] + 2.5, 0.4), 30, GREEN)


def b_desloc(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "DESLOCAMENTOS", "O SINAL ENGANA", AMBER), ("13", "O NÚMERO DE FORA", "SOBE, FECHA, VIRA",
                                                                          PURPLE)])
    card(c, *CARD_R)
    P = Plano(220, 210, 860, 580, (-4.5, 5.5), (-3.2, 4.2))
    a0 = ep(t, C[sid], 0.4)
    P.eixos(c, a0, xt=(-4, -2, 2, 3, 4), yt=(-2, 1, 2, 3))
    P.curva(c, a0 * 0.35, abs, GRAY, width=6)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            defin(c, "DESLOCAMENTO", "o gráfico muda de lugar", 1120, 220, 600, aa, BLUE, 24)
            text(c, "sem mudar de forma", 1420, 340, 26, "bold", INK2, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            u = ease_io(clamp((t - C["12.b"] - 1.0) / 2.0))
            P.curva(c, ab, lambda x: abs(x - 3 * u), BLUE, width=8)
            P.ponto(c, 3 * u, 0, BLUE, ab, None)
            if u > 0.98:
                P.ponto(c, 3, 0, BLUE, ab, "(3, 0)", dx=16, dy=30, size=22)
            arrow(c, P.px(0), P.py(-0.8), P.px(3 * u) + 1, P.py(-0.8), GREEN, ab * (u > 0.05), 6, 18)
            rrect(c, 1120, 400, 600, 150, 22, "#FFFFFF", ab, shadow=True)
            t1(c, "y = |x − 3|", 1420, 450, 46, ab, BLUE)
            linha(c, [("zera em x = 3  →  ", INK2), ("DIREITA", GREEN)], 1420, 510, 30, ep(t, C["12.b"] + 1.0, 0.4))
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            P.curva(c, acc, lambda x: abs(x + 2), PURPLE, width=8)
            P.ponto(c, -2, 0, PURPLE, acc, "(−2, 0)", dx=-120, dy=30, size=22)
            rrect(c, 1120, 590, 600, 150, 22, "#FFFFFF", acc, shadow=True)
            t1(c, "y = |x + 2|", 1420, 640, 46, acc, PURPLE)
            linha(c, [("zera em x = −2  →  ", INK2), ("ESQUERDA", PURPLE)], 1420, 700, 30, acc)
        return
    rows = [("13.a", "y = |x| + 1", "sobe 1", lambda x: abs(x) + 1, GREEN),
            ("13.b", "y = 2|x|", "V mais fechado", lambda x: 2 * abs(x), BLUE),
            ("13.c", "y = −|x|", "de cabeça para baixo", lambda x: -abs(x), RED)]
    for k, (cue, ex, sub, f, col) in enumerate(rows):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        P.curva(c, ak, f, col, u=ep(t, C[cue], 1.0), width=7)
        y = 230 + k * 190 + d
        rrect(c, 1120, y, 600, 160, 22, "#FFFFFF", ak, shadow=True)
        t1(c, ex, 1420, y + 55, 46, ak, col)
        text(c, sub, 1420, y + 125, 28, "bold", INK2, ak)


def b_vertice(c, t, C, B):
    head(c, t, B["start"], "ONDE FICA O VÉRTICE?", "y = |x − a| + b", PURPLE)
    card(c, *CARD_R)
    P = Plano(240, 220, 760, 560, (-1, 6), (-0.8, 5.2))
    a0 = ep(t, C["14"], 0.4)
    P.eixos(c, a0, xt=(), yt=(), grade=False)
    if a0 > 0:
        P.curva(c, a0, lambda x: abs(x - 3) + 1.5, PURPLE, u=ep(t, C["14"], 1.2), width=8)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        P.ponto(c, 3, 1.5, AMBER, aa, "(a, b)", dx=20, dy=34, size=24)
        line(c, P.px(3), P.py(0), P.px(3), P.py(1.5), AMBER, aa, 3, dash=(10, 8))
        line(c, P.px(0), P.py(1.5), P.px(3), P.py(1.5), AMBER, aa, 3, dash=(10, 8))
        text(c, "a", P.px(3), P.py(0) + 40, 30, "black", AMBER, aa)
        text(c, "b", P.px(0) - 18, P.py(1.5) + 10, 30, "black", AMBER, aa, align="right")
        rrect(c, 1080, 220, 640, 200, 24, mix("#FFFFFF", PURPLE, 0.08), aa)
        t1(c, "vértice (a, b)", 1400, 280, 54, aa, PURPLE)
        linha(c, [("a", AMBER), (": zera o de dentro  ·  ", INK2), ("b", AMBER), (": o de fora", INK2)], 1400, 360, 28,
              aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        defin(c, "PONTO DE MÍNIMO", "o ponto mais baixo", 1080, 460, 640, ab, BLUE, 26)
        text(c, "y nunca fica abaixo de b", 1400, 590, 30, "black", INK2, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        line(c, P.px(-0.6), P.py(1.5), P.px(-0.6), P.py(5.0), GREEN, acc, 10)
        c.drawCircle(P.px(-0.6), P.py(1.5), 12, paint(GREEN, acc))
        rrect(c, 1080, 640, 640, 130, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        linha(c, [("IMAGEM: ", GREEN), ("[b, +∞[", INK)], 1400, 705, 48, acc)


def b_atalho_vert(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "VÉRTICE EM DOIS SEGUNDOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    K.atalho(c, 240, 200, 1440, 140, "ATALHO", ["zere o de DENTRO → x  ·  número de FORA → y"], a0, 38)
    aa = ep(t, C["15.a"], 0.5)
    ab = ep(t, C["15.b"], 0.5)
    if aa > 0:
        rrect(c, 340, 420, 1240, 170, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("y = |", INK), ("x − 5", BLUE), ("|", INK), (" + 2", PURPLE)], W / 2, 505, 84, aa)
        text(c, "x = 5", 870, 640, 34, "black", BLUE, aa)
        if ab > 0:
            text(c, "y = 2", 1210, 640, 34, "black", PURPLE, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 760, acc, "VÉRTICE (5, 2)", GREEN, -3, 40)


# ======================================================================
# bloco g — o rebatimento · bloco h — contar soluções · atalho
# ======================================================================

def b_rebate(c, t, C, B):
    sid = which(t, C, ["16", "17"])
    head_seq(c, t, C, [("16", "O GRÁFICO DE |f(x)|", "UM ESPELHO NO CHÃO", PURPLE),
                       ("17", "REBATENDO A PARÁBOLA", "y = |x² − 4|", PURPLE)])
    card(c, *CARD_R)
    if sid == "16":
        P = Plano(240, 220, 820, 560, (-1, 6.5), (-3.6, 4))
        a0 = ep(t, C["16"], 0.4)
        P.eixos(c, a0, xt=(1, 3, 5), yt=())
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            rrect(c, P.x0, P.py(0) - 6, P.w, 12, 6, mix("#FFFFFF", BLUE, 0.6), aa)
            pill(c, "espelho no chão", P.x0 + P.w - 10, P.py(0) + 40, BLUE, size=22, a=aa, anchor="right",
                 bounds=(0, 1920))
        ab = ep(t, C["16.b"], 0.5)
        u = ease_io(clamp((t - C["16.c"] - 0.8) / 1.8)) if t > C["16.c"] else 0.0
        f = lambda x: x - 3
        P.curva(c, a0, f, GRAY if u > 0 else INK2, width=5, dash=(14, 10) if u > 0 else None)
        if ab > 0:
            P.curva(c, ab, f, GREEN, xa=3, xb=6.5, width=8)
            rrect(c, 1100, 230, 620, 130, 22, mix("#FFFFFF", GREEN, 0.14), ab)
            text_mid(c, "ACIMA DO EIXO: FICA", 1410, 295, 36, "black", GREEN, ab)
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            P.curva(c, acc, lambda x: f(x) + (abs(f(x)) - f(x)) * u, PURPLE, xa=-1, xb=3, width=8)
            rrect(c, 1100, 390, 620, 130, 22, mix("#FFFFFF", PURPLE, 0.12), acc)
            text_mid(c, "ABAIXO: REBATE PARA CIMA", 1410, 455, 34, "black", PURPLE, acc)
            a2 = ep(t, C["16.c"] + 2.8, 0.4)
            P.ponto(c, 0, -3, RED, a2, "−3", dx=18, dy=8, size=20)
            P.ponto(c, 0, 3, GREEN, a2, "3", dx=18, dy=-30, size=20)
            arrow(c, P.px(0) + 40, P.py(-2.6), P.px(0) + 40, P.py(2.6), PURPLE, a2, 5, 16)
            rrect(c, 1100, 560, 620, 180, 22, "#FFFFFF", a2, shadow=True)
            defin(c, "REBATER", "espelhar no eixo x", 1120, 580, 580, a2, PURPLE, 26)
            text(c, "altura −3  →  altura 3", 1410, 715, 32, "black", INK, a2)
        return
    P = Plano(260, 220, 820, 580, (-3.2, 3.2), (-4.8, 5.4))
    a0 = ep(t, C["17"], 0.4)
    P.eixos(c, a0, xt=(-1, 1), yt=(-2, 2))
    f = lambda x: x * x - 4
    u = ease_io(clamp((t - C["17.a"] - 2.2) / 2.0)) if t > C["17.a"] else 0.0
    P.curva(c, a0, f, PURPLE if u == 0 else GRAY, width=7 if u == 0 else 4, dash=None if u == 0 else (14, 10))
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        if u == 0:
            P.curva(c, aa, f, RED, xa=-2, xb=2, width=9)
        rrect(c, 1120, 230, 600, 120, 22, mix("#FFFFFF", RED, 0.10), aa)
        text_mid(c, "negativa entre −2 e 2", 1420, 290, 32, "black", RED, aa)
        if u > 0:
            P.curva(c, aa, lambda x: f(x) + (abs(f(x)) - f(x)) * u, GREEN, xa=-2, xb=2, width=9)
    P.curva(c, a0 * (u > 0), f, PURPLE, xa=-3.2, xb=-2, width=7)
    P.curva(c, a0 * (u > 0), f, PURPLE, xa=2, xb=3.2, width=7)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        P.ponto(c, 0, -4, GRAY, ab, "(0, −4)", dx=20, dy=8, size=20)
        P.ponto(c, 0, 4, GREEN, ab, "(0, 4)", dx=20, dy=-34, size=22)
        rrect(c, 1120, 380, 600, 200, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("(0, −4)", GRAY), ("  →  ", INK2), ("(0, 4)", GREEN)], 1420, 430, 40, ab)
        defin(c, "MÁXIMO LOCAL", "o mais alto daquele pedaço", 1140, 480, 560, ab, GREEN, 22)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        P.ponto(c, -2, 0, BLUE, acc, "−2", dx=-62, dy=-34, size=20)
        P.ponto(c, 2, 0, BLUE, acc, "2", dx=16, dy=-34, size=20)
        rrect(c, 1120, 620, 600, 140, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text_mid(c, "raízes paradas: |0| = 0", 1420, 690, 34, "black", BLUE, acc)


def _plano_g():
    return Plano(260, 220, 820, 580, (-3.3, 3.3), (-1.6, 6.2))


KS18 = [("18.a", -1.0, 0.0), ("18.a", 0.0, 3.2), ("18.b", 1.0, 0.0), ("18.c", 4.0, 0.0), ("18.d", 5.0, 0.0)]


def b_contar(c, t, C, B):
    head(c, t, B["start"], "QUANTAS SOLUÇÕES?", "|x² − 4| = k", GREEN)
    card(c, *CARD_R)
    P = _plano_g()
    a0 = ep(t, C["18"], 0.4)
    P.eixos(c, a0, xt=(-2, -1, 1, 2), yt=(1, 2, 3, 4, 5))
    P.curva(c, a0, g, PURPLE, width=7)
    # a régua: posição atual = último k já chamado
    ks = [(C[cue] + dt, k) for cue, k, dt in KS18]
    cur = None
    for t0, k in ks:
        if t >= t0:
            cur = (t0, k)
    if cur is None:
        return
    # transição suave entre um k e o seguinte
    idx = ks.index(cur)
    k_prev = ks[idx - 1][1] if idx > 0 else cur[1]
    u = ease_io(clamp((t - cur[0]) / 0.8))
    k = k_prev + (cur[1] - k_prev) * u
    if k < 0:
        line(c, P.x0 - 10, P.py(-1), P.x0 + P.w + 10, P.py(-1), AMBER, a0, 6)
        pill(c, "k < 0", P.x0 + P.w + 14, P.py(-1), AMBER, size=22, a=a0, anchor="left", bounds=(0, 1920))
        n = 0
    else:
        n = regua_k(c, P, k, a0)
    if u >= 0.999:
        contador(c, n, 1400, 330, a0, GREEN, "cortes", 80)
    tab = [(-1.0, "k < 0", "0"), (0.0, "k = 0", "2"), (1.0, "0 < k < 4", "4"), (4.0, "k = 4", "3"), (5.0, "k > 4", "2")]
    for j, (kv, rot_, nn) in enumerate(tab):
        tj = next(t0 for t0, kk in ks if kk == kv)
        aj = ep(t, tj + 0.8, 0.4)
        if aj <= 0:
            continue
        y = 450 + j * 66
        rrect(c, 1160, y, 480, 56, 14, "#FFFFFF", aj, shadow=True)
        linha(c, [(rot_, INK), ("   →   ", GRAY), (nn, GREEN)], 1400, y + 28, 30, aj)


def b_atalho_conta(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONTAR SEM CONTA NENHUMA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["19"], 0.4)
    K.atalho(c, 240, 200, 1440, 120, "ATALHO", ["cada corte é uma solução"], a0, 38)
    passos = [("19.a", "DESENHE", "o gráfico rebatido", PURPLE), ("19.b", "PASSE A RÉGUA", "na altura pedida", AMBER),
              ("19.c", "CONTE", "os cortes", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(passos):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 380 + d, 480, 380, 26, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 460 + d, ak, 36, bg=col)
        text(c, tit, x, 580 + d, 40, "black", col, ak)
        text(c, sub, x, 640 + d, 28, "bold", INK2, ak)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("20", "SUA VEZ", "PAUSE E TENTE", GREEN), ("21", "VAMOS JUNTOS", "ZERE O DE DENTRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["20.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 210, 760, 220, 24, "#FFFFFF", aa, shadow=True)
        t1(c, "y = |x + 1| − 3", 580, 290, 60, aa, INK)
        text(c, "1 · onde fica o VÉRTICE?", 580, 375, 30, "black", PURPLE, aa)
        text(c, "2 · onde CORTA o eixo x?", 580, 415, 30, "black", BLUE, ep(t, C["20.b"], 0.5))
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 1.9, 1360, 500)
        return
    P = Plano(1060, 220, 640, 560, (-5.5, 3.5), (-3.8, 2.6))
    a1 = ep(t, C["21.a"], 0.4)
    P.eixos(c, ep(t, C["21"], 0.4), xt=(-4, -1, 2), yt=(-3, 1))
    if a1 > 0:
        t1(c, "x + 1 = 0  →  x = −1", 580, 500, 40, a1, PURPLE)
        t1(c, "de fora: −3", 580, 560, 40, ep(t, C["21.a"] + 1.8, 0.4), PURPLE)
        a2 = ep(t, C["21.a"] + 3.0, 0.4)
        rrect(c, 330, 600, 500, 80, 18, mix("#FFFFFF", AMBER, 0.18), a2)
        t1(c, "vértice (−1, −3)", 580, 640, 42, a2, AMBER)
        P.curva(c, a1, lambda x: abs(x + 1) - 3, PURPLE, u=ep(t, C["21.a"], 1.4), width=7)
        P.ponto(c, -1, -3, AMBER, a2, "(−1, −3)", dx=18, dy=8, size=20)
    ab = ep(t, C["21.b"], 0.4)
    if ab > 0:
        t1(c, "|x + 1| = 3", 580, 730, 44, ab, BLUE)
        text(c, "a 3 passos do −1", 580, 795, 28, "black", INK2, ep(t, C["21.b"] + 2.0, 0.4))
        a3 = ep(t, C["21.b"] + 2.0, 0.4)
        line(c, P.px(-1), P.py(0.9), P.px(2), P.py(0.9), GREEN, a3, 5)
        line(c, P.px(-1), P.py(0.9), P.px(-4), P.py(0.9), GREEN, a3, 5)
        text(c, "3", P.px(0.5), P.py(1.2), 26, "black", GREEN, a3)
        text(c, "3", P.px(-2.5), P.py(1.2), 26, "black", GREEN, a3)
    acc = ep(t, C["21.c"], 0.4)
    if acc > 0:
        P.ponto(c, 2, 0, GREEN, acc, "2", dx=14, dy=30, size=22)
        P.ponto(c, -4, 0, GREEN, ep(t, C["21.c"] + 1.4, 0.4), "−4", dx=-60, dy=30, size=22)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Módulo é distância: nunca é negativo.",
          "O vértice mora onde o de dentro zera.",
          "|f(x)|: acima fica, abaixo rebate."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 56, "black", INK, a, 1360, 64)


ERROS = [("|x − 3| leva o V 3 para a ESQUERDA",
          "o “menos” lembra a esquerda da reta",
          "o vértice mora onde o de dentro zera: x = 3, à DIREITA"),
         ("|a + b| = |a| + |b| SEMPRE",
          "com dois positivos funciona",
          "|−3 + 3| = 0, mas |−3| + |3| = 6: com sinais diferentes, não vale"),
         ("√(x²) = x",
          "a raiz desfaz o quadrado",
          "com x = −5: √25 = 5, e não −5. O certo é √(x²) = |x|")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# questão 3 (eu faço)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720, x=190):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, x, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS3 = [("A", "(2, −1);  x = 1 e x = 3", "", GREEN), ("B", "(−2, −1);  x = −3 e x = −1", "leu −2 como esquerda", RED),
         ("C", "(2, 1);  não há valores", "trocou o sinal do −1", RED),
         ("D", "(−2, 1);  x = 1 e x = 3", "vértice errado nos 2 sinais", RED),
         ("E", "(2, −1);  x = −1 e x = 3", "x − 2 = −1 dá x = 1", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "LENDO O GRÁFICO EM V", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 700, 30, C["27.ok"], "A", cues_in, cues_x, gap=34)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    if t < C["27"]:
        if a0 > 0:
            yend = _enunciado(c, [("Um engenheiro modela o perfil de uma calha pela função", INK)], a0, 250, 30)
            t1(c, "f(x) = |x − 2| − 1", 550, yend + 30, 52, a0, BLUE)
            _enunciado(c, [("em metros. O ponto mais baixo do gráfico e os valores de x em que f(x) = 0 são, "
                            "respectivamente,", INK)], a0, yend + 120, 30)
        pause_timer(c, t, C["26.end"] - 1.9, 860, 720)
        return
    y0 = 206
    a1 = ep(t, C["27"], 0.4)
    rrect(c, 170, y0, 780, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    P = Plano(560, 250, 340, 300, (-0.6, 4.6), (-1.6, 2.4))
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        P.eixos(c, aa, xt=(1, 2, 3), yt=(-1, 1), grade=False, size=20)
        P.curva(c, aa, lambda x: abs(x - 2) - 1, BLUE, u=ep(t, C["27.a"], 1.2), width=6)
        t1(c, "x − 2 = 0 → x = 2", 360, y0 + 70, 34, aa, PURPLE)
        t1(c, "de fora: −1", 360, y0 + 130, 34, ep(t, C["27.a"] + 1.6, 0.4), PURPLE)
        a2 = ep(t, C["27.a"] + 3.0, 0.4)
        rrect(c, 200, y0 + 175, 330, 70, 16, mix("#FFFFFF", AMBER, 0.18), a2)
        t1(c, "vértice (2, −1)", 365, y0 + 210, 34, a2, AMBER)
        P.ponto(c, 2, -1, AMBER, a2, None)
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        t1(c, "|x − 2| = 1", 560, y0 + 390, 44, ab, BLUE)
        text(c, "a 1 passo do 2", 560, y0 + 445, 28, "black", INK2, ep(t, C["27.b"] + 1.6, 0.4))
        a3 = ep(t, C["27.b"] + 2.4, 0.4)
        P.ponto(c, 1, 0, GREEN, a3, "1", dx=-44, dy=28, size=20)
        P.ponto(c, 3, 0, GREEN, a3, "3", dx=14, dy=28, size=20)
        t1(c, "x = 1  ou  x = 3", 560, y0 + 510, 44, a3, GREEN)
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        rrect(c, 230, y0 + 555, 660, 70, 16, mix("#FFFFFF", GREEN, 0.12), acc)
        t1(c, "f(1) = |−1| − 1 = 0   ·   f(3) = |1| − 1 = 0", 560, y0 + 590, 28, acc, INK)


# ======================================================================
# questão 6 (você faz)
# ======================================================================

ALTS6 = [("A", "nenhuma", "só com número negativo", RED), ("B", "uma", "só √7, sem ± e sem o outro caso", RED),
         ("C", "duas", "só o caso = 3", RED), ("D", "três", "seria g(x) = 4", RED), ("E", "quatro", "", GREEN)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "CONTAR SOLUÇÕES NO GRÁFICO REBATIDO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS6, 1200, 250, 520, 34, C["31.ok"], "E", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
         align="left")
    if t < C["30"]:
        if a0 > 0:
            yend = _enunciado(c, [("O gráfico de", INK)], a0, 250, 30, 900)
            t1(c, "g(x) = |x² − 4|", 560, yend + 26, 54, a0, PURPLE)
            yend = _enunciado(c, [("é obtido a partir da parábola y = x² − 4, refletindo para cima o trecho que fica "
                                   "abaixo do eixo x. A quantidade de números reais x tais que g(x) = 3 é", INK)], a0,
                              yend + 110, 30, 900)
        pause_timer(c, t, C["29.end"] - 1.9, 560, 720)
        return
    if t < C["31"]:
        aa = ep(t, C["30.a"], 0.4)
        rrect(c, 170, 206, 960, 624, 18, "#FFFFFF", ep(t, C["30"], 0.4), shadow=True)
        if aa > 0:
            linha(c, [("|x² − 4| = 3  →  dentro = ", INK), ("3", BLUE), (" ou ", INK2), ("−3", PURPLE)], 650, 270, 40,
                  aa)
        ab = ep(t, C["30.b"], 0.4)
        if ab > 0:
            rrect(c, 210, 340, 420, 300, 22, mix("#FFFFFF", BLUE, 0.08), ab)
            t1(c, "x² − 4 = 3", 420, 400, 40, ab, BLUE)
            t1(c, "x² = 7", 420, 480, 40, ep(t, C["30.b"] + 1.6, 0.4), INK)
            t1(c, "x = ±√7", 420, 570, 48, ep(t, C["30.b"] + 2.6, 0.4), GREEN)
        acc = ep(t, C["30.c"], 0.4)
        if acc > 0:
            rrect(c, 670, 340, 420, 300, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
            t1(c, "x² − 4 = −3", 880, 400, 40, acc, PURPLE)
            t1(c, "x² = 1", 880, 480, 40, ep(t, C["30.c"] + 1.4, 0.4), INK)
            t1(c, "x = ±1", 880, 570, 48, ep(t, C["30.c"] + 2.4, 0.4), GREEN)
            a4 = ep(t, C["30.c"] + 3.6, 0.4)
            rrect(c, 420, 680, 460, 100, 20, mix("#FFFFFF", GREEN, 0.16), a4)
            t1(c, "4 soluções", 650, 730, 50, a4, GREEN)
        return
    P = Plano(250, 230, 800, 560, (-3.3, 3.3), (-1.0, 5.8))
    a1 = ep(t, C["31"], 0.4)
    P.eixos(c, a1, xt=(-2, -1, 1, 2), yt=(3, 4))
    P.curva(c, a1, g, PURPLE, width=7)
    aa = ep(t, C["31.a"], 0.4)
    if aa > 0:
        P.ponto(c, 0, 4, AMBER, aa, "topo (0, 4)", dx=18, dy=-34, size=20)
        line(c, P.x0 - 10, P.py(3), P.x0 + P.w + 10, P.py(3), AMBER, ep(t, C["31.a"] + 1.8, 0.4), 6)
        pill(c, "y = 3", P.x0 + P.w + 14, P.py(3), AMBER, size=22, a=ep(t, C["31.a"] + 1.8, 0.4), anchor="left",
             bounds=(0, 1920))
    ab = ep(t, C["31.b"], 0.4)
    if ab > 0:
        for k, x in enumerate((-1, 1, -math.sqrt(7), math.sqrt(7))):
            P.ponto(c, x, 3, RED, ep(t, C["31.b"] + 0.6 * k, 0.3), r=12)
        text(c, "≈ −2,65", P.px(-math.sqrt(7)), P.py(3) + 50, 22, "black", INK2, ab)
        text(c, "≈ 2,65", P.px(math.sqrt(7)), P.py(3) + 50, 22, "black", INK2, ab)
    acc = ep(t, C["31.c"], 0.4)
    if acc > 0:
        contador(c, 4, 470, 330, acc, GREEN, "cortes", 70)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "EQUAÇÕES MODULARES E TOLERÂNCIA", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 640, 300, 26, "#FFFFFF", aa, shadow=True)
        rrect(c, 430, 290, 300, 200, 24, mix("#FFFFFF", AMBER, 0.45), aa)
        text_mid(c, "CAFÉ", 580, 360, 50, "black", INK, aa)
        text_mid(c, "500 g", 580, 430, 46, "black", INK, aa)
        pill(c, "± 8 g no máximo", 580, 580, AMBER, size=26, a=aa, anchor="center")
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        rrect(c, 980, 240, 700, 140, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        t1(c, "|  ?  |  ≤  ?", 1330, 310, 64, ab, PURPLE)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 410, 700, 140, 24, mix("#FFFFFF", BLUE, 0.10), acc)
        linha(c, [("|x| = 5", BLUE), ("  →  2 respostas?", INK2)], 1330, 480, 50, acc)
    pill(c, "ep. 4 · equações e inequações modulares", W / 2, 760, PURPLE, size=26, a=ep(t, C["34.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Em que outra situação o que importa é a distância, e não o sinal?", canal="no Estudativo",
        anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              dist=b_dist, tabela=b_tabela, atalho_dentro=b_atalho_dentro, letra=b_letra, funcao_v=b_funcao_v,
              desloc=b_desloc, vertice=b_vertice, atalho_vert=b_atalho_vert, rebate=b_rebate, contar=b_contar,
              atalho_conta=b_atalho_conta, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q6=b_q6,
              ponte=b_ponte, cta=b_cta)
