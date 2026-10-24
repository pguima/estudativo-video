"""Visual — Função Logarítmica, Episódio 1: o espelho da exponencial (gráfico, domínio e sinal) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: lrow() (linha com "log" e a base em subscrito, junto com expr e texto), Plano (eixos com escala
própria; curva() desenha y = f(x) aos poucos; param() desenha uma curva paramétrica — usada na DOBRA de 2ˣ sobre y = x),
reta() (reta numérica com faixas, bolinhas abertas/fechadas e buracos), porta() (a porta do log, aberta só para positivos),
escada_log() (degraus de mesma altura e largura crescente: 1, 10, 100, 1 000), tabela() (colunas x e y).
Cores com função: azul = definição / base · roxo = regra · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum043", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmica_ep1_espelho_grafico.mp4"
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
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências, frações)"""
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def _pw(p, size):
    k = p[0]
    if k == "log":
        w = ftext_w("log", "black", size)
        return w + (ftext_w(p[1], "black", size * 0.58) + size * 0.04 if p[1] else 0)
    if k == "m":
        return K.math_w(p[1], size)
    return ftext_w(p[1], "black", size)


def lrow(c, partes, cx, cy, size, a, align="center", gap=None):
    """linha com logs: partes = [("log", base, cor[, cor_base]), ("m", expr, cor), ("t", texto, cor)].
    A base vai em subscrito; base "" = log decimal. Devolve a largura."""
    gap = size * 0.26 if gap is None else gap
    ws = [_pw(p, size) for p in partes]
    total = sum(ws) + gap * (len(partes) - 1)
    if a <= 0:
        return total
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    for p, w_ in zip(partes, ws):
        col = p[2] if len(p) > 2 and p[2] else INK
        if p[0] == "log":
            ftext(c, "log", x, cy + size * 0.36, size, "black", col, a, align="left")
            if p[1]:
                cb = p[3] if len(p) > 3 else col
                ftext(c, p[1], x + ftext_w("log", "black", size) + size * 0.04, cy + size * 0.62, size * 0.58, "black",
                      cb, a, align="left")
        elif p[0] == "m":
            mx(c, p[1], x, cy, size, a, col, align="left")
        else:
            ftext(c, p[1], x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_ + gap
    return total


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def ease_out(u):
    return 1 - (1 - clamp(u)) ** 3


def lg(b, x):
    return math.log(x) / math.log(b)


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, grade=True, rot=("x", "y"), fmt=None):
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
        f = fmt or (lambda v: f"{v:g}".replace(".", ",").replace("-", "−"))
        for v in xt:
            if v == 0:
                continue
            text(c, f(v), s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v == 0:
                continue
            text(c, f(v), ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def _clip(s, c):
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))

    def curva(s, c, a, f, col, u=1.0, width=7, xa=None, xb=None, n=200):
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
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))
        c.restore()

    def param(s, c, a, fxy, s0, s1, col, width=7, n=240):
        """curva paramétrica (x(s), y(s)) para s de s0 a s1"""
        if a <= 0:
            return
        s._clip(c)
        path = skia.Path()
        for k in range(n + 1):
            x, y = fxy(s0 + (s1 - s0) * k / n)
            x = max(min(x, s.xr[1] + 6), s.xr[0] - 6)
            y = max(min(y, s.yr[1] + 6), s.yr[0] - 6)
            (path.moveTo if k == 0 else path.lineTo)(s.px(x), s.py(y))
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))
        c.restore()

    def ponto(s, c, x, y, col, a, rot_=None, dx=18, dy=-30, size=22, r=9):
        if a <= 0:
            return
        c.drawCircle(s.px(x), s.py(y), r + 3, paint("#FFFFFF", a))
        c.drawCircle(s.px(x), s.py(y), r, paint(col, a))
        if rot_:
            pill(c, rot_, s.px(x) + dx, s.py(y) + dy, col, size=size, a=a, bounds=(0, 1920))


def _bola(c, x, y, col, a, aberta, r=13):
    c.drawCircle(x, y, r, paint("#FFFFFF", a))
    if aberta:
        c.drawCircle(x, y, r, paint(col, a, stroke=5))
    else:
        c.drawCircle(x, y, r, paint(col, a))


def reta(c, x0, x1, y, vmin, vmax, a, marcas=(), faixas=(), buracos=(), size=26):
    """reta numérica: marcas = [(valor, rótulo)]; faixas = [(va, vb, cor, ponta_a, ponta_b)] com va/vb = None para ±∞ e
    ponta = 'o' (aberta), 'f' (fechada) ou None; buracos = [(valor, cor)] (bolinha aberta no meio da faixa)."""
    if a <= 0:
        return
    px = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    line(c, x0 - 20, y, x1 + 20, y, INK2, a, 4)
    for v, lab in marcas:
        line(c, px(v), y - 12, px(v), y + 12, INK2, a, 3)
        text(c, lab, px(v), y + 50, size, "black", INK, a)
    for va, vb, col, pa, pb in faixas:
        xa = px(va) if va is not None else x0 - 20
        xb = px(vb) if vb is not None else x1 + 20
        line(c, xa, y, xb, y, col, a, 11)
        if va is None:
            arrow(c, xa + 30, y, xa - 14, y, col, a, 11, 22)
        if vb is None:
            arrow(c, xb - 30, y, xb + 14, y, col, a, 11, 22)
        if va is not None and pa:
            _bola(c, xa, y, col, a, pa == "o")
        if vb is not None and pb:
            _bola(c, xb, y, col, a, pb == "o")
    for v, col in buracos:
        _bola(c, px(v), y, col, a, True)


def porta(c, cx, cy, a, aberta=1.0, col=None):
    """a porta do log: moldura com 'log ( )' em cima e a folha da porta girando"""
    if a <= 0:
        return
    col = col or BLUE
    w, h = 220, 300
    rrect(c, cx - w / 2 - 16, cy - h / 2 - 16, w + 32, h + 32, 18, mix("#FFFFFF", col, 0.18), a)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 8, mix("#FFFFFF", INK, 0.06), a)
    ww = w * (1 - 0.72 * clamp(aberta))
    rrect(c, cx - w / 2, cy - h / 2, ww, h, 8, mix("#FFFFFF", col, 0.55), a)
    c.drawCircle(cx - w / 2 + ww - 22, cy, 8, paint(INK, a))
    lrow(c, [("log", "", col), ("t", "(   )", col)], cx, cy - h / 2 - 50, 40, a)


def escada_log(c, x0, base, a, n_on, alturas=95, larguras=(80, 200, 440, 760), rot=("1", "10", "100", "1 000")):
    """degraus de MESMA altura e largura crescente; n_on = quantos degraus já acenderam (float)"""
    if a <= 0:
        return
    x = x0
    line(c, x0 - 30, base, x0 + sum(larguras) + 60, base, INK2, a, 4)
    text(c, rot[0], x0, base + 46, 30, "black", INK, a)
    for k, w_ in enumerate(larguras[:-1]):
        u = clamp(n_on - k)
        top = base - alturas * (k + 1)
        col = mix("#FFFFFF", PURPLE, 0.25 + 0.15 * k)
        if u > 0:
            rrect(c, x, top, w_ * ease_out(u), alturas * (k + 1), 8, col, a)
            text(c, rot[k + 1], x + w_, base + 46, 30, "black", INK, a * u)
            text(c, f"log = {k + 1}", x + w_ - 12, top - 18, 26, "black", PURPLE, a * u, align="right")
            if k > 0:
                text(c, "× 10", x + w_ / 2, base + 92, 24, "black", GREEN, a * u)
        x += w_


def tabela(c, x, y, cols, linhas, a, cw=150, rh=86, lw=180, alfas=None):
    """tabela: cabeçalho (rótulos das linhas à esquerda) e valores. linhas = [(rótulo_expr, [valores], cor)]"""
    if a <= 0:
        return
    n = len(linhas[0][1])
    tw = lw + n * cw
    rrect(c, x, y, tw, rh * len(linhas), 18, "#FFFFFF", a, shadow=True)
    for j, (rot_, vals, col) in enumerate(linhas):
        yy = y + rh * j
        if j > 0:
            line(c, x + 14, yy, x + tw - 14, yy, LIGHT, a, 2)
        if isinstance(rot_, tuple):
            lrow(c, [rot_], x + lw / 2, yy + rh / 2, 34, a)
        else:
            mx(c, rot_, x + lw / 2, yy + rh / 2, 34, a, col)
        for k, v in enumerate(vals):
            ak = a * (alfas[j][k] if alfas else 1.0)
            if ak > 0:
                mx(c, v, x + lw + cw * (k + 0.5), yy + rh / 2, 34, ak, col)
    line(c, x + lw, y + 10, x + lw, y + rh * len(linhas) - 10, LIGHT, a, 2)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO LOGARÍTMICA · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 180, 220, 760, 140, 24, mix("#FFFFFF", BLUE, 0.10), aa)
        lrow(c, [("m", "P(t) = 20 ·", INK), ("log", "", BLUE), ("m", "t", BLUE)], 560, 290, 64, aa)
        pill(c, "t = horas de treino", 560, 395, INK2, size=24, a=aa, anchor="center")
    P = Plano(1060, 250, 620, 480, (0, 1100), (0, 70))
    P.eixos(c, aa, xt=(100, 200, 1000), yt=(20, 40, 60), rot=("h", "pts"))
    P.curva(c, aa, lambda x: 20 * math.log10(max(x, 1e-3)), BLUE, u=ep(t, C["01.a"] + 0.6, 2.2), xa=1, xb=1100)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        P.ponto(c, 100, 40, BLUE, ab, "100 h → 40", dx=-16, dy=-44)
        rrect(c, 180, 450, 760, 110, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("100 horas  →  ", INK2), ("40 pontos", BLUE)], 560, 505, 42, ab)
    acc = ep(t, C["01.c"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    if acc > 0:
        rrect(c, 180, 590, 760, 110, 22, mix("#FFFFFF", AMBER, 0.18), acc)
        linha(c, [("60 pontos  →  ", INK2), ("200 horas?", AMBER)], 560, 645, 42, acc)
        line(c, P.px(200), P.py(0), P.px(200), P.py(60), AMBER, acc * (1 - ad), 4, dash=(12, 8))
        pill(c, "200 h?", P.px(200) + 10, P.py(62), AMBER, size=22, a=acc * (1 - ad), bounds=(0, 1920))
        if ad > 0:
            strike(c, 640, 645, 900, 645, ad, RED)
    if ad > 0:
        P.ponto(c, 1000, 60, GREEN, ad, "1 000 h → 60", dx=-20, dy=-46, size=22)
        rrect(c, 180, 730, 760, 110, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("NÃO: ", RED), ("1 000 horas", GREEN)], 560, 785, 46, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, 1380, 800, ae, "A CARA DO LOGARITMO", PURPLE, -4, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO LOGARÍTMICA · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de FUNÇÃO LOGARÍTMICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "O GRÁFICO", "desenhar o log", BLUE), ("02.b", "A BASE", "ler num gráfico", PURPLE),
             ("02.c", "O DOMÍNIO", "o que pode entrar", AMBER), ("02.d", "INEQUAÇÕES", "logarítmicas", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 330, 380, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 190, 330, 380, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 38, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    cards = [("03.a", "série de Logaritmos", BLUE), ("03.b", "série de Função exponencial", PURPLE),
             ("03.c", "série de Conceito de função", GREEN)]
    for k, (cue, rot_, col) in enumerate(cards):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 140 + k * 560
        rrect(c, x, 250, 520, 560, 24, "#FFFFFF", ak, shadow=True)
        pill(c, rot_, x + 260, 290, col, size=22, a=ak, anchor="center")
        if k == 0:
            lrow(c, [("log", "b", INK, BLUE), ("m", "a = x", INK)], x + 260, 420, 60, ak)
            text(c, "⇔", x + 260, 510, 54, "black", PURPLE, ak)
            mx(c, "b^x = a", x + 260, 590, 64, ak, PURPLE)
            text(c, "b > 0  e  b ≠ 1", x + 260, 720, 32, "black", BLUE, ak)
        elif k == 1:
            P = Plano(x + 70, 360, 380, 330, (-3, 3), (-0.4, 6))
            P.eixos(c, ak, xt=(-2, 2), yt=(1, 4), grade=False)
            P.curva(c, ak, lambda v: 2 ** v, PURPLE, u=ep(t, C[cue] + 0.5, 1.2), width=6)
            line(c, P.x0, P.py(0) - 1, P.x0 + P.w, P.py(0) - 1, AMBER, ak, 4, dash=(14, 9))
            P.ponto(c, 0, 1, PURPLE, ak, "(0, 1)", dx=20, dy=-36, size=20)
            text(c, "assíntota: y = 0", x + 260, 760, 28, "black", AMBER, ak)
        else:
            rrect(c, x + 150, 420, 220, 200, 26, mix("#FFFFFF", GREEN, 0.14), ak)
            text_mid(c, "f", x + 260, 520, 90, "black", GREEN, ak)
            arrow(c, x + 40, 520, x + 140, 520, INK2, ak, 5, 16)
            text(c, "entra", x + 90, 490, 24, "black", INK, ak)
            text(c, "DOMÍNIO", x + 260, 700, 38, "black", GREEN, ak)
            text(c, "os valores que podem entrar", x + 260, 750, 26, "bold", INK2, ak)


# ======================================================================
# concreto e bloco a — definição
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TREINANDO PARA A PROVA", "CADA HORA RENDE MENOS", BLUE)
    card(c, *CARD_R)
    rows = [("04.a", "1 → 10 h", "+ 9 h", 9, "+20 pontos"), ("04.b", "10 → 100 h", "+ 90 h", 90, "+20 pontos")]
    for k, (cue, rot_, mais, horas, pts) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 200 + d
        text(c, rot_, 230, y + 60, 36, "black", INK, a, align="left")
        u = ep(t, C[cue] + 0.6, 1.4)
        w_ = 1100 * horas / 90 * ease_out(u)
        rrect(c, 520, y + 20, max(w_, 6), 80, 14, mix("#FFFFFF", BLUE if k == 0 else AMBER, 0.45), a)
        text(c, mais, 520 + max(w_, 6) + 16, y + 74, 30, "black", BLUE if k == 0 else AMBER, a * u, align="left")
        pill(c, pts, 520, y + 132, GREEN, size=26, a=a * u, bounds=(0, 1920))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        linha(c, [("mesmos ", INK2), ("+20 pontos", GREEN), (", esforço ", INK2), ("10 vezes maior", RED)], W / 2,
              690, 38, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "ESSE JEITO DE CRESCER: LOGARITMO", W / 2, 800, ad, 38)


def b_definicao(c, t, C, B):
    head(c, t, B["start"], "A FUNÇÃO LOGARÍTMICA", "DEFINIÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 200, 1000, 200, 30, mix("#FFFFFF", BLUE, 0.08), aa)
        lrow(c, [("m", "f(x) =", INK), ("log", "b", INK, BLUE), ("m", "x", INK)], W / 2, 300, 110, aa)
        pill(c, "b > 0  e  b ≠ 1", 520, 430, BLUE, size=28, a=aa, bounds=(0, 1920))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        pill(c, "x > 0", 1260, 430, PURPLE, size=28, a=ab, bounds=(0, 1920))
        rrect(c, 200, 510, 740, 290, 24, "#FFFFFF", ab, shadow=True)
        text(c, "DOMÍNIO · o que entra", 570, 560, 30, "black", PURPLE, ab)
        reta(c, 280, 860, 650, -2, 6, ab, marcas=[(0, "0")], faixas=[(0, None, PURPLE, "o", None)])
        mx(c, "]0, +∞[", 570, 760, 52, ab, PURPLE)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 510, 740, 290, 24, "#FFFFFF", acc, shadow=True)
        text(c, "IMAGEM · o que sai", 1350, 560, 30, "black", GREEN, acc)
        reta(c, 1060, 1640, 650, -3, 3, acc, marcas=[(0, "0")], faixas=[(None, None, GREEN, None, None)])
        text(c, "todos os reais", 1350, 770, 44, "black", GREEN, acc)


# ======================================================================
# bloco b — o espelho · atalho
# ======================================================================

def _plano_esp():
    return Plano(250, 210, 600, 600, (-2.5, 9), (-2.5, 9))


def b_espelho(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    head_seq(c, t, C, [("06", "DE ONDE VEM O LOG?", "ELE DESFAZ A EXPONENCIAL", BLUE),
                       ("07", "DOBRE A FOLHA", "O ESPELHO NA RETA y = x", PURPLE)])
    card(c, *CARD_R)
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 240, 600, 200, 26, mix("#FFFFFF", PURPLE, 0.10), aa)
            mx(c, "2^3 = 8", 560, 340, 96, aa, PURPLE)
            rrect(c, 1060, 240, 600, 200, 26, mix("#FFFFFF", BLUE, 0.10), ep(t, C["06.a"] + 1.4, 0.5))
            lrow(c, [("log", "2", BLUE), ("m", "8 = 3", BLUE)], 1360, 340, 90, ep(t, C["06.a"] + 1.4, 0.5))
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            arrow(c, 880, 300, 1040, 300, GREEN, ab, 6, 18)
            arrow(c, 1040, 380, 880, 380, GREEN, ab, 6, 18)
            text(c, "desfaz", 960, 270, 26, "black", GREEN, ab)
            defin(c, "FUNÇÕES INVERSAS", "uma desfaz o que a outra faz", 360, 520, 1200, ab, BLUE, 32)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            pill(c, "série própria: Função composta e inversa", W / 2, 680, INK2, size=26, a=acc, anchor="center")
            regra(c, "AQUI, SÓ O DESENHO", W / 2, 790, acc, 36)
        return
    P = _plano_esp()
    a0 = ep(t, C["07"], 0.4)
    P.eixos(c, a0, xt=(1, 2, 4, 8), yt=(1, 2, 4, 8))
    line(c, P.px(-2.5), P.py(-2.5), P.px(9), P.py(9), GRAY, a0, 3, dash=(14, 10))
    pill(c, "y = x", P.px(8.2), P.py(8.9), GRAY, size=22, a=a0, anchor="right", bounds=(0, 1920))
    u = ease_out(ep(t, C["07.a"], 2.4))
    if u > 0 and u < 1:
        P.param(c, a0 * 0.3, lambda s: (s, 2 ** s), -2.5, 3.3, PURPLE, width=5)
    P.param(c, a0, lambda s: (s + (2 ** s - s) * u, 2 ** s + (s - 2 ** s) * u), -2.5, 3.3,
            mix(PURPLE, BLUE, u), width=7)
    if u < 0.5:
        pill(c, "y = 2ˣ", P.px(3.1), P.py(7.6), PURPLE, size=24, a=a0 * (1 - 2 * u), anchor="right", bounds=(0, 1920))
    else:
        lrow(c, [("m", "y =", BLUE), ("log", "2", BLUE), ("m", "x", BLUE)], P.px(7.4), P.py(2.4), 32, a0 * (2 * u - 1))
    pts = [((0, 1), "(0, 1)", "(1, 0)"), ((1, 2), "(1, 2)", "(2, 1)"), ((3, 8), "(3, 8)", "(8, 3)")]
    for k, ((xa, ya), r0, r1) in enumerate(pts):
        P.ponto(c, xa + (ya - xa) * u, ya + (xa - ya) * u, mix(PURPLE, BLUE, u), a0)
        ak = ep(t, C["07.b"] + 1.3 * k, 0.4)
        if ak > 0:
            P.ponto(c, xa, ya, PURPLE, ak * 0.45, r=7)
            line(c, P.px(xa), P.py(ya), P.px(ya), P.py(xa), GREEN, ak * 0.7, 3, dash=(8, 6))
            y_r = 250 + k * 110
            rrect(c, 1000, y_r, 680, 90, 18, "#FFFFFF", ak, shadow=True)
            linha(c, [(r0, PURPLE), ("   →   ", GRAY), (r1, BLUE)], 1340, y_r + 45, 40, ak)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        ang = ease_out(ep(t, C["07.c"] + 0.8, 1.6)) * math.pi / 2
        L = 12
        x1, y1 = -L * math.cos(ang) * 0.2, -L * math.sin(ang) * 0.2
        x2, y2 = L * math.cos(ang), L * math.sin(ang)
        P._clip(c)
        line(c, P.px(x1), P.py(y1), P.px(x2), P.py(y2), AMBER, acc, 6, dash=(16, 10))
        c.restore()
        defin(c, "ASSÍNTOTA VERTICAL", "reta em pé, a curva não toca", 1000, 600, 680, acc, AMBER, 24)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        linha(c, [("domínio ", PURPLE), ("⇄", GREEN), (" imagem", GREEN), ("  trocam de papel", INK2)], 1340, 740, 32, ad)


def b_atalho_esp(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DESENHE O LOG SEM CALCULAR LOG", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    K.atalho(c, 240, 200, 1440, 140, "ATALHO", ["tabela da exponencial  →  troque as colunas"], a0, 38)
    aa = ep(t, C["08.a"], 0.5)
    xs = ["−1", "0", "1", "2", "3"]
    ys = ["1/2", "1", "2", "4", "8"]
    tabela(c, 330, 400, [], [("x", xs, INK), ("2^x", ys, PURPLE)], aa, cw=200)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        tabela(c, 330, 620, [], [("x", ys, BLUE), (("log", "2", BLUE), xs, BLUE)], ab, cw=200)
        arrow(c, 260, 480, 260, 680, GREEN, ab, 5, 16)
        text(c, "troca", 250, 600, 24, "black", GREEN, ab, align="right")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        selo(c, 1600, 800, acc, "NENHUM LOG CALCULADO", GREEN, -4, 24)


# ======================================================================
# bloco c — o gráfico · atalho da base
# ======================================================================

def _plano_graf():
    return Plano(280, 220, 760, 580, (-0.6, 8.6), (-3.4, 3.4))


def b_grafico(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "O GRÁFICO", "SOBE OU DESCE", BLUE), ("10", "OS DOIS PONTOS DE SEMPRE", "(1, 0) E (b, 1)",
                                                                       GREEN)])
    card(c, *CARD_R)
    P = _plano_graf()
    a0 = ep(t, C["09"], 0.4)
    P.eixos(c, a0, xt=(1, 2, 4, 8), yt=(-3, -2, -1, 1, 2, 3))
    aa = ep(t, C["09.a"], 0.5)
    P.curva(c, aa, lambda x: lg(2, max(x, 1e-4)), BLUE, u=ep(t, C["09.a"], 1.6), xa=0.01, xb=8.6)
    if aa > 0:
        rrect(c, 1120, 230, 560, 150, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        lrow(c, [("t", "base 2 > 1 →", INK), ("t", "CRESCENTE", BLUE)], 1400, 285, 32, aa)
        text(c, "x aumenta → y aumenta", 1400, 345, 26, "bold", INK2, aa)
    ab = ep(t, C["09.b"], 0.5)
    P.curva(c, ab, lambda x: lg(0.5, max(x, 1e-4)), PURPLE, u=ep(t, C["09.b"], 1.6), xa=0.01, xb=8.6)
    if ab > 0:
        rrect(c, 1120, 400, 560, 150, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
        lrow(c, [("t", "base 1/2 →", INK), ("t", "DECRESCENTE", PURPLE)], 1400, 455, 32, ab)
        text(c, "x aumenta → y diminui", 1400, 515, 26, "bold", INK2, ab)
        lrow(c, [("log", "2", BLUE), ("m", "x", BLUE)], P.px(7.9), P.py(2.5), 30, aa, align="right")
        lrow(c, [("log", "1/2", PURPLE), ("m", "x", PURPLE)], P.px(7.9), P.py(-2.5), 30, ab, align="right")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0 and sid == "09":
        rrect(c, P.px(0) - 8, P.y0, 16, P.h, 8, AMBER, acc * 0.25)
        pill(c, "colada no eixo y, sem tocar", P.px(0) + 24, P.y0 + 40, AMBER, size=22, a=acc, bounds=(0, 1920))
    if sid == "09":
        return
    a1 = ep(t, C["10.a"], 0.5)
    if a1 > 0:
        pulse = 0.5 + 0.5 * math.sin((t - C["10.a"]) * 6)
        c.drawCircle(P.px(1), P.py(0), 22 + 8 * pulse, paint(GREEN, a1 * 0.35))
        P.ponto(c, 1, 0, GREEN, a1, "(1, 0)", dx=22, dy=40, size=24, r=11)
        rrect(c, 1120, 580, 560, 90, 18, "#FFFFFF", a1, shadow=True)
        lrow(c, [("log", "b", INK, BLUE), ("m", "1 = 0", GREEN)], 1400, 625, 46, a1)
    a2 = ep(t, C["10.b"], 0.5)
    if a2 > 0:
        P.ponto(c, 2, 1, BLUE, a2, "(2, 1)", dx=20, dy=-36, size=22, r=10)
        P.ponto(c, 0.5, 1, PURPLE, a2, "(1/2, 1)", dx=20, dy=-36, size=22, r=10)
        rrect(c, 1120, 690, 560, 90, 18, "#FFFFFF", a2, shadow=True)
        lrow(c, [("log", "b", INK, BLUE), ("m", "b = 1", GREEN)], 1400, 735, 46, a2)
    a3 = ep(t, C["10.c"], 0.5)
    if a3 > 0:
        line(c, P.x0, P.py(0), P.x0 + P.w, P.py(0), GREEN, a3 * 0.7, 8, dash=(14, 10))
        rrect(c, 1120, 230, 560, 320, 22, "#FFFFFF", a3, shadow=True)
        lrow(c, [("log", "1/2", PURPLE), ("m", "x =", INK), ("m", "−", RED), ("log", "2", BLUE), ("m", "x", BLUE)],
             1400, 330, 46, a3)
        text(c, "ESPELHO no eixo x", 1400, 450, 34, "black", GREEN, a3)


def b_atalho_base(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "LEIA A BASE NO GRÁFICO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    K.atalho(c, 1000, 200, 680, 200, "ATALHO", ["procure a ALTURA 1", "o x desse ponto = a base"], a0, 36)
    P = Plano(280, 230, 620, 540, (-0.4, 6.5), (-2.4, 2.4))
    P.eixos(c, a0, xt=(1, 2, 3, 4, 5, 6), yt=(-2, -1, 1, 2))
    P.curva(c, a0, lambda x: lg(3, max(x, 1e-4)), BLUE, u=ep(t, C["11"], 1.4), xa=0.01, xb=6.5)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        line(c, P.x0, P.py(1), P.px(3), P.py(1), GREEN, aa, 5, dash=(14, 9))
        pill(c, "altura 1", P.x0 + 10, P.py(1) - 34, GREEN, size=22, a=aa, bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        arrow(c, P.px(3), P.py(1), P.px(3), P.py(0) - 6, GREEN, ab, 5, 16)
        P.ponto(c, 3, 1, GREEN, ab, "(3, 1)", dx=20, dy=-40, size=24, r=11)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 470, 680, 200, 24, mix("#FFFFFF", BLUE, 0.10), acc)
        text(c, "passa por (3, 1)", 1340, 540, 34, "black", INK2, acc)
        linha(c, [("base = ", INK), ("3", BLUE)], 1340, 615, 56, acc)
        lrow(c, [("m", "y =", BLUE), ("log", "3", BLUE), ("m", "x", BLUE)], 1340, 740, 44, acc)


# ======================================================================
# bloco d — o sinal
# ======================================================================

def b_sinal(c, t, C, B):
    head(c, t, B["start"], "O SINAL DO LOG", "QUANDO DÁ NEGATIVO?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        defin(c, "SINAL", "onde a função é positiva e onde é negativa", 380, 200, 1160, aa, BLUE, 28)
    for k, (cue, b, rot_, col, ex, ex_partes) in enumerate((
            ("12.b", 10, "base > 1", BLUE, "−2", [("log", "", BLUE), ("m", "0,01 = −2", RED)]),
            ("12.c", 0.5, "0 < base < 1", PURPLE, "−3", [("log", "0,5", PURPLE), ("m", "8 = −3", RED)]))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x0 = 200 + k * 790
        rrect(c, x0, 300, 740, 520, 24, "#FFFFFF", ak, shadow=True)
        pill(c, rot_, x0 + 370, 340, col, size=26, a=ak, anchor="center")
        P = Plano(x0 + 70, 390, 600, 270, (-0.3, 4.5), (-2.2, 2.2))
        f = (lambda x, b=b: lg(b, max(x, 1e-4)))
        neg_esq = b > 1
        rrect(c, P.px(0), P.y0, P.px(1) - P.px(0), P.h, 6, RED if neg_esq else GREEN, ak * 0.12)
        rrect(c, P.px(1), P.y0, P.x0 + P.w - P.px(1), P.h, 6, GREEN if neg_esq else RED, ak * 0.12)
        P.eixos(c, ak, xt=(1,), yt=(), grade=False)
        P.curva(c, ak, f, col, u=ep(t, C[cue], 1.2), xa=0.01, xb=4.5, width=6)
        text(c, "−" if neg_esq else "+", P.px(0.5), P.y0 + 40, 44, "black", RED if neg_esq else GREEN, ak)
        text(c, "+" if neg_esq else "−", P.px(2.8), P.y0 + 40, 44, "black", GREEN if neg_esq else RED, ak)
        ae = ep(t, C[cue] + 3.0, 0.5)
        lrow(c, ex_partes, x0 + 370, 740, 44, ae)
    ab = ep(t, C["12.c"], 0.5)
    if ab > 0:
        selo(c, 1640, 300, ab, "O CONTRÁRIO", PURPLE, 6, 24)


# ======================================================================
# bloco e — retorno decrescente
# ======================================================================

def b_escada(c, t, C, B):
    head(c, t, B["start"], "RETORNO DECRESCENTE", "DEGRAUS IGUAIS, CAMINHOS CADA VEZ MAIORES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["13.a"], 0.5)
    n_on = 0.0
    if t >= C["13.a"]:
        n_on = min(3.0, (t - C["13.a"]) / 1.6)
    escada_log(c, 300, 640, a0, n_on)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        regra(c, "PARA O LOG SUBIR 1, x É MULTIPLICADO POR 10", W / 2, 260, ab, 34)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 770, 1320, 80, 18, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("40 pontos = 100 h", BLUE), ("     ·     ", GRAY), ("60 pontos = 1 000 h", GREEN)], W / 2, 810,
              34, acc)


# ======================================================================
# bloco f — domínio · atalho
# ======================================================================

def b_dominio(c, t, C, B):
    sid = which(t, C, ["14", "15"])
    head_seq(c, t, C, [("14", "O QUE PODE ENTRAR?", "A PORTA DO LOG", AMBER), ("15", "MAIS DOIS DOMÍNIOS",
                                                                               "x² E x NA BASE", AMBER)])
    card(c, *CARD_R)
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        porta(c, 430, 500, aa, aberta=ep(t, C["14.a"] + 0.6, 0.8), col=BLUE)
        if aa > 0:
            for k, (v, ok) in enumerate((("5", True), ("0", False), ("−2", False))):
                ak = ep(t, C["14.a"] + 1.4 + 0.8 * k, 0.4)
                y = 360 + k * 110
                chip(c, v, 720, y, GREEN if ok else RED, ak, size=40, w=120)
                check_icon(c, 830, y, 22, ak, GREEN if ok else RED, "check" if ok else "x")
            text(c, "só número estritamente positivo", 430, 760, 26, "black", BLUE, aa)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            rrect(c, 980, 250, 700, 120, 22, "#FFFFFF", ab, shadow=True)
            lrow(c, [("log", "", INK), ("t", "(2x − 6)", INK)], 1330, 310, 54, ab)
            rrect(c, 980, 400, 700, 110, 22, mix("#FFFFFF", PURPLE, 0.12), ab)
            mx(c, "2x − 6 > 0", 1330, 455, 54, ab, PURPLE)
            pill(c, "escreva PRIMEIRO", 1660, 400, PURPLE, size=20, a=ab, anchor="right", bounds=(0, 1920))
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            mx(c, "2x > 6", 1330, 560, 50, acc, INK)
            mx(c, "x > 3", 1330, 640, 64, ep(t, C["14.c"] + 1.0, 0.4), GREEN)
            reta(c, 1050, 1610, 750, 0, 6, ep(t, C["14.c"] + 1.4, 0.4), marcas=[(3, "3")],
                 faixas=[(3, None, GREEN, "o", None)])
        return
    rows = [("15.a", [("log", "", INK), ("t", "(x² − 9)", INK)], "x² > 9"),
            ("15.b", [("log", "x", INK, AMBER), ("t", "(5 − x)", INK)], "5 − x > 0 · x > 0 · x ≠ 1")]
    for k, (cue, partes, cond) in enumerate(rows):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 220 + k * 300
        rrect(c, 200, y, 1520, 270, 24, "#FFFFFF", ak, shadow=True)
        lrow(c, partes, 420, y + 70, 50, ak)
        text(c, cond, 1060, y + 84, 36, "black", PURPLE, ak)
    aa = ep(t, C["15.a"] + 3.5, 0.5)
    if aa > 0:
        reta(c, 320, 1100, 380, -6, 6, aa, marcas=[(-3, "−3"), (0, "0"), (3, "3")],
             faixas=[(None, -3, GREEN, None, "o"), (3, None, GREEN, "o", None)])
        linha(c, [("x < −3", GREEN), ("  ou  ", INK2), ("x > 3", GREEN)], 1400, 390, 40, aa)
    az = ep(t, C["15.a"] + 7.5, 0.5)
    if az > 0:
        pill(c, "teste o 0:  0² − 9 = −9  ✗", 1400, 460, RED, size=24, a=az, anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        reta(c, 320, 1100, 680, -1, 6, acc, marcas=[(0, "0"), (1, "1"), (5, "5")],
             faixas=[(0, 5, GREEN, "o", "o")], buracos=[(1, GREEN)])
        linha(c, [("0 < x < 5", GREEN), (" e ", INK2), ("x ≠ 1", AMBER)], 1400, 690, 40, acc)


def b_atalho_dom(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DOMÍNIO SEM ERRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["16"], 0.4)
    K.atalho(c, 240, 200, 1440, 140, "ATALHO", ["ANTES de qualquer conta: escreva  > 0"], a0, 38)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 400, 620, 260, 24, "#FFFFFF", aa, shadow=True)
        text(c, "o que está DENTRO do log", 610, 460, 28, "black", INK2, aa)
        text_mid(c, "(    ) > 0", 610, 570, 80, "black", PURPLE, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 400, 620, 260, 24, "#FFFFFF", ab, shadow=True)
        text(c, "tem x NA BASE?", 1310, 460, 28, "black", INK2, ab)
        mx(c, "base > 0", 1310, 540, 52, ab, AMBER)
        mx(c, "base ≠ 1", 1310, 610, 52, ab, AMBER)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        regra(c, "SÓ DEPOIS RESOLVA", W / 2, 760, acc, 38, GREEN)


# ======================================================================
# bloco g — inequações · atalho
# ======================================================================

def b_ineq(c, t, C, B):
    sid = which(t, C, ["17", "18"])
    head_seq(c, t, C, [("17", "INEQUAÇÃO LOGARÍTMICA", "BASE MAIOR QUE 1: MANTÉM", BLUE),
                       ("18", "BASE ENTRE 0 E 1", "INVERTE O SENTIDO", AMBER)])
    card(c, *CARD_R)
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            defin(c, "INEQUAÇÃO LOGARÍTMICA", "um log comparado com > ou <", 330, 200, 1260, aa, BLUE, 30)
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            lrow(c, [("log", "2", INK, BLUE), ("m", "x > 3", INK)], 560, 380, 70, ab)
            pill(c, "base 2 > 1 → MANTÉM", 560, 470, BLUE, size=26, a=ab, anchor="center")
            mx(c, "x > 2^3", 560, 580, 64, ep(t, C["17.b"] + 3.0, 0.4), INK)
            mx(c, "x > 8", 560, 690, 76, ep(t, C["17.b"] + 5.0, 0.4), GREEN)
        acc = ep(t, C["17.c"], 0.5)
        if acc > 0:
            rrect(c, 1000, 330, 680, 420, 24, "#FFFFFF", acc, shadow=True)
            reta(c, 1080, 1600, 500, 0, 12, acc, marcas=[(0, "0"), (8, "8")], faixas=[(8, None, GREEN, "o", None)])
            text(c, "todo x > 8 já é positivo", 1340, 640, 30, "black", GREEN, acc)
            check_icon(c, 1340, 700, 24, acc, GREEN, "check")
        return
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        lrow(c, [("log", "0,5", INK, PURPLE), ("m", "x > 2", INK)], 560, 270, 64, aa)
        pill(c, "base 0,5 < 1 → INVERTE", 560, 360, AMBER, size=26, a=aa, anchor="center")
        a2 = ep(t, C["18.a"] + 4.0, 0.4)
        K.expr(c, "x < 0,5^2", 560, 470, 64, a2, cores={0: INK, 1: RED, 2: INK})
        if a2 > 0:
            selo(c, 830, 420, a2, "VIROU", RED, 6, 22)
        mx(c, "x < 0,25", 560, 580, 70, ep(t, C["18.a"] + 6.5, 0.4), AMBER)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 680, 380, 24, "#FFFFFF", ab, shadow=True)
        porta(c, 1200, 430, ab * 0.9, aberta=0.0, col=RED)
        text(c, "fechada para", 1500, 400, 28, "black", INK2, ab)
        text(c, "0 e negativos", 1500, 450, 32, "black", RED, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        reta(c, 300, 900, 700, -0.15, 0.45, acc, marcas=[(0, "0"), (0.25, "0,25")],
             faixas=[(0, 0.25, GREEN, "o", "o")])
        rrect(c, 1000, 650, 680, 110, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        mx(c, "0 < x < 0,25", 1340, 705, 60, acc, GREEN)


def b_atalho_ineq(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "INEQUAÇÃO EM 4 PASSOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["19"], 0.4)
    K.atalho(c, 240, 200, 1440, 120, "ATALHO", ["sempre na mesma ordem"], a0, 36)
    passos = [("19.a", "DOMÍNIO", "o de dentro > 0", BLUE), ("19.b", "TIRE O LOG", "base elevada ao número", PURPLE),
              ("19.c", "BASE < 1?", "vire o sinal", AMBER), ("19.d", "CRUZE", "com o domínio", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(passos):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 380 + d, 380, 380, 26, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 460 + d, ak, 36, bg=col)
        text(c, tit, x, 580 + d, 38, "black", col, ak)
        text(c, sub, x, 640 + d, 26, "bold", INK2, ak)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("20", "SUA VEZ", "PAUSE E TENTE", GREEN), ("21", "VAMOS JUNTOS", "DOMÍNIO PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["20.a"], 0.5)
    ab = ep(t, C["20.b"], 0.5)
    if aa > 0:
        rrect(c, 200, 220, 740, 160, 24, "#FFFFFF", aa, shadow=True)
        text(c, "1 · DOMÍNIO DE", 570, 265, 26, "black", BLUE, aa)
        lrow(c, [("m", "f(x) =", INK), ("log", "", INK), ("t", "(3x − 12)", INK)], 570, 330, 50, aa)
    if ab > 0:
        rrect(c, 980, 220, 740, 160, 24, "#FFFFFF", ab, shadow=True)
        text(c, "2 · RESOLVA", 1350, 265, 26, "black", PURPLE, ab)
        lrow(c, [("log", "3", INK, PURPLE), ("m", "x < 2", INK)], 1350, 330, 54, ab)
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 1.9, W / 2, 620)
        return
    a1 = ep(t, C["21.a"], 0.4)
    if a1 > 0:
        mx(c, "3x − 12 > 0", 570, 450, 48, a1, PURPLE)
        mx(c, "3x > 12", 570, 530, 44, ep(t, C["21.a"] + 2.0, 0.4), INK)
        mx(c, "x > 4", 570, 620, 64, ep(t, C["21.a"] + 3.4, 0.4), GREEN)
        reta(c, 280, 860, 740, 0, 8, ep(t, C["21.a"] + 3.4, 0.4), marcas=[(4, "4")], faixas=[(4, None, GREEN, "o", None)])
    a2 = ep(t, C["21.b"], 0.4)
    if a2 > 0:
        pill(c, "base 3 > 1 → MANTÉM", 1350, 440, BLUE, size=24, a=a2, anchor="center")
        mx(c, "x < 3^2 = 9", 1350, 530, 52, ep(t, C["21.b"] + 3.0, 0.4), INK)
    a3 = ep(t, C["21.c"], 0.4)
    if a3 > 0:
        reta(c, 1060, 1640, 650, -1, 11, a3, marcas=[(0, "0"), (9, "9")], faixas=[(0, 9, GREEN, "o", "o")])
        rrect(c, 1050, 720, 600, 100, 22, mix("#FFFFFF", GREEN, 0.14), ep(t, C["21.c"] + 2.0, 0.4))
        mx(c, "0 < x < 9", 1350, 770, 56, ep(t, C["21.c"] + 2.0, 0.4), GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Log e exponencial são espelhos na reta y = x.",
          "Toda função logarítmica passa por (1, 0) e por (b, 1).",
          "Dentro do log, só número estritamente positivo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 60)


ERROS = [("Domínio de log(2x − 6): x ≥ 3",
          "o 3 resolve a conta do zero",
          "com x = 3 sobra log 0, que não existe: o certo é x > 3"),
         ("log na base 0,5 de x > 2  ⇒  x > 0,25",
          "com base 2 ou 10, o sinal fica onde está",
          "base menor que 1 inverte: o certo é 0 < x < 0,25"),
         ("“O logaritmo cresce cada vez mais rápido”",
          "a curva sobe para sempre, sem teto",
          "cada degrau custa 10 vezes mais x: cresce cada vez mais devagar")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# questão 7 (nós fazemos)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS7 = [("A", "−5", "x = −b: mas x > 0", RED), ("B", "0,04", "usou 25 como base", RED),
         ("C", "0,2", "", GREEN), ("D", "0,5", "usou o 2 como base", RED),
         ("E", "5", "é onde f(x) = 1", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · NÓS FAZEMOS", "LER A BASE NO GRÁFICO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 40, C["27.ok"], "C", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    if t < C["27"]:
        y = 236
        if a0 > 0:
            lrow(c, [("t", "O gráfico de", INK), ("m", "f(x) =", INK), ("log", "b", INK, BLUE), ("m", "x,", INK)], 190, y,
                 34, a0, align="left")
            yend = _enunciado(c, [("com b > 0 e b ≠ 1, passa pelo ponto (25, 2). O valor de x para o qual f(x) = −1 é",
                                   INK)], a0, y + 60, 28)
            P = Plano(260, yend + 10, 520, 220, (-2, 32), (-1.6, 3))
            P.eixos(c, a0, xt=(25,), yt=(2,), grade=False, size=20)
            P.curva(c, a0, lambda x: lg(5, max(x, 1e-4)), BLUE, xa=0.05, xb=32, width=5)
            P.ponto(c, 25, 2, AMBER, a0, "(25, 2)", dx=-130, dy=-36, size=20)
        pause_timer(c, t, C["26.end"] - 1.9, 860, 700)
        return
    y0 = 206
    a1 = ep(t, C["27"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        lrow(c, [("log", "b", INK, BLUE), ("m", "25 = 2", INK)], 540, y0 + 60, 50, aa)
        mx(c, "b^2 = 25", 540, y0 + 150, 56, ep(t, C["27.a"] + 3.0, 0.4), PURPLE)
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        linha(c, [("b = 5", GREEN), ("   (−5 não: a base é positiva)", INK2)], 540, y0 + 240, 30, ab)
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        lrow(c, [("log", "5", INK, GREEN), ("m", "x = −1", INK)], 540, y0 + 330, 50, acc)
        mx(c, "x = 5^{-1} = 1/5", 540, y0 + 430, 50, ep(t, C["27.c"] + 3.0, 0.4), PURPLE)
        rrect(c, 260, y0 + 500, 560, 90, 18, mix("#FFFFFF", GREEN, 0.14), ep(t, C["27.c"] + 4.5, 0.4))
        mx(c, "x = 0,2", 540, y0 + 545, 56, ep(t, C["27.c"] + 4.5, 0.4), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANTAS VEZES MAIS ÁCIDO?", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        for k, (nome, ph, col) in enumerate((("SUCO", "pH 3", AMBER), ("ÁGUA DA CHUVA", "pH 6", BLUE))):
            ak = ep(t, C["30.a"] + 1.4 * k, 0.5)
            x = 580 + k * 760
            rrect(c, x - 320, 240, 640, 200, 24, "#FFFFFF", ak, shadow=True)
            text(c, nome, x, 300, 30, "black", col, ak)
            text(c, ph, x, 390, 70, "black", col, ak)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 480, 1200, 200, 26, mix("#FFFFFF", AMBER, 0.20), ab)
        text(c, "o suco é quantas vezes mais ácido?", W / 2, 540, 32, "bold", INK2, ab)
        text_mid(c, "2×  ·  3×  ·  1 000× ?", W / 2, 620, 64, "black", INK, ab)
    pill(c, "ep. 2 · escalas logarítmicas e o pH", W / 2, 760, PURPLE, size=26, a=ep(t, C["30.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Em que outra situação mais esforço rende cada vez menos?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              espelho=b_espelho, atalho_esp=b_atalho_esp, grafico=b_grafico, atalho_base=b_atalho_base, sinal=b_sinal,
              escada=b_escada, dominio=b_dominio, atalho_dom=b_atalho_dom, ineq=b_ineq, atalho_ineq=b_atalho_ineq,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q7=b_q7, ponte=b_ponte, cta=b_cta)
