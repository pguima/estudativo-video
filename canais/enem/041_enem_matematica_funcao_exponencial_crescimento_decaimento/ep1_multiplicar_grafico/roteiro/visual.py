"""Visual — Função Exponencial, Episódio 1: multiplicar em vez de somar, a função exponencial e seu gráfico (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: Plano (eixos com escala própria; curva() desenha y = f(x) aos poucos), escadas() (degraus +2 ao lado
de degraus ×2), tabela() (linha de x e linha de f(x) com as setas ×base / ÷base entre as colunas), parede() (a assíntota
tracejada como parede invisível), linha() (texto com cor por trecho).
Cores com função: azul = definição / base · roxo = regra / expoente · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum041", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_exponencial_ep1_multiplicar_grafico.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"
TEAL = "#0E8C8C"


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


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


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

    def curva(s, c, a, f, col, u=1.0, width=7, xa=None, xb=None, n=160):
        """y = f(x) de xa a xb (recortada no retângulo); u = fração já desenhada"""
        if a <= 0 or u <= 0:
            return
        xa = s.xr[0] if xa is None else xa
        xb = s.xr[1] if xb is None else xb
        xe = xa + (xb - xa) * clamp(u)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xe - xa) * k / n
            y = max(min(f(x), s.yr[1] * 3), s.yr[0] - 5)
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


def parede(c, P, y, a, rot_="parede invisível", col=None, rx=None):
    """a assíntota horizontal y = y0 como uma faixa tracejada"""
    if a <= 0:
        return
    col = col or AMBER
    rrect(c, P.x0, P.py(y) - 9, P.w, 18, 9, col, a * 0.16)
    line(c, P.x0, P.py(y), P.x0 + P.w, P.py(y), col, a, 4, dash=(16, 10))
    if rot_:
        pill(c, rot_, rx if rx is not None else P.x0 + P.w - 10, P.py(y) - 34, col, size=22, a=a, anchor="right",
             bounds=(0, 1920))


def tabela(c, x, y, xs, linhas, a, cw=150, rh=86, setas=None, prog=None):
    """tabela: linha de x e, abaixo, as linhas [(rótulo, [valores], cor, alfas_por_coluna)].
    setas = (linha, rótulo da direita, rótulo da esquerda, a_dir, a_esq): setas curvas entre as colunas."""
    if a <= 0:
        return
    n = len(xs)
    lw = 190
    tw = lw + n * cw
    rrect(c, x, y, tw, rh * (1 + len(linhas)), 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, tw, rh, 18, mix("#FFFFFF", INK, 0.06), a)
    text_mid(c, "x", x + lw / 2, y + rh / 2, 34, "black", INK, a)
    for k, v in enumerate(xs):
        text_mid(c, v, x + lw + cw * (k + 0.5), y + rh / 2, 34, "black", INK, a)
    for j, (rot_, vals, col, alfas) in enumerate(linhas):
        yy = y + rh * (j + 1)
        line(c, x + 14, yy, x + tw - 14, yy, LIGHT, a, 2)
        mx(c, rot_, x + lw / 2, yy + rh / 2, 34, a, col)
        for k, v in enumerate(vals):
            ak = a * (alfas[k] if alfas else 1.0)
            if ak > 0 and v:
                mx(c, v, x + lw + cw * (k + 0.5), yy + rh / 2, 34, ak, col)
    line(c, x + lw, y + 10, x + lw, y + rh * (1 + len(linhas)) - 10, LIGHT, a, 2)
    if setas:
        j, sd, se, ad, ae = setas
        yy = y + rh * (j + 1)
        for k in range(n - 1):
            xa_, xb_ = x + lw + cw * (k + 0.5), x + lw + cw * (k + 1.5)
            if ad > 0:
                _arco(c, xa_ + 20, xb_ - 20, yy + rh + 6, 30, GREEN, ad, down=True)
                text(c, sd, (xa_ + xb_) / 2, yy + rh + 70, 28, "black", GREEN, ad)
            if ae > 0:
                _arco(c, xb_ - 20, xa_ + 20, y - 6, 30, PURPLE, ae, down=False)
                text(c, se, (xa_ + xb_) / 2, y - 46, 28, "black", PURPLE, ae)


def _arco(c, x0, x1, y, h, col, a, down=True):
    """seta curva de x0 a x1, abaulada para baixo (down) ou para cima"""
    sgn = 1 if down else -1
    path = skia.Path()
    path.moveTo(x0, y)
    path.quadTo((x0 + x1) / 2, y + sgn * h, x1, y)
    c.drawPath(path, paint(col, a, stroke=4, cap_round=True))
    ang = math.atan2(-sgn * h, (x1 - x0) / 2)
    for d in (2.6, -2.6):
        line(c, x1, y, x1 - 14 * math.cos(ang + d * 0.25 + (0 if x1 > x0 else math.pi)),
             y - 14 * math.sin(ang + d * 0.25 + (0 if x1 > x0 else math.pi)), col, a, 4)


def escadas(c, a, n_soma, n_mult, base=700, esc=15, larg=100):
    """degraus iguais (+2) à esquerda e degraus que dobram (×2) à direita; n_* = quantos degraus já apareceram (float)"""
    if a <= 0:
        return
    for lado, n_, vals, col, x0, rot_ in (("soma", n_soma, [1 + 2 * k for k in range(8)], BLUE, 180, "+2"),
                                          ("mult", n_mult, [2 ** k for k in range(8)], PURPLE, 1040, "×2")):
        line(c, x0 - 20, base, x0 + 8 * larg + 20, base, INK2, a, 4)
        for k, v in enumerate(vals):
            u = clamp(n_ - k)
            if u <= 0:
                break
            h = v * esc * ease_out(u)
            top = base - h
            rrect(c, x0 + k * larg + 4, top, larg - 8, h, 10, mix("#FFFFFF", col, 0.35 + 0.05 * k), a)
            if top > 150:
                text(c, f"{v}", x0 + k * larg + larg / 2, top - 14, 30, "black", col, a * u)
            if k > 0 and u > 0.6 and top > 190:
                text(c, rot_, x0 + k * larg, top - 60, 22, "black", GRAY, a * (u - 0.6) / 0.4)


def ease_out(u):
    return 1 - (1 - clamp(u)) ** 3


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO EXPONENCIAL · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    # barras da mesada: semana 0..10, alturas 2^n (semana 10 = 560 px)
    nb = clamp((t - C["01.a"]) / max(0.1, C["01.c"] - C["01.a"])) * 11
    x0, base = 230, 740
    if aa > 0:
        line(c, x0 - 10, base, x0 + 11 * 78, base, INK2, aa, 4)
        for k in range(11):
            u = clamp(nb - k)
            if u <= 0:
                break
            h = max(4, 500 * 2 ** k / 1024) * ease_out(u)
            rrect(c, x0 + k * 78 + 6, base - h, 64, h, 8, mix("#FFFFFF", GREEN, 0.25 + 0.06 * k), aa)
            text(c, str(k), x0 + k * 78 + 38, base + 36, 22, "bold", GRAY, aa * u)
        text(c, "semana", x0 - 20, base + 36, 22, "bold", GRAY, aa, align="right")
        rrect(c, 1180, 230, 520, 120, 22, "#FFFFFF", aa, shadow=True)
        linha(c, [("R$ 1", GREEN), (" · dobra toda semana", INK2)], 1440, 290, 36, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1180, 380, 520, 140, 22, mix("#FFFFFF", GREEN, 0.10), ab)
        text(c, "10 semanas", 1440, 430, 30, "bold", INK2, ab)
        text(c, "R$ 1.024", 1440, 495, 56, "black", GREEN, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1180, 550, 520, 170, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "20 semanas", 1440, 600, 30, "bold", INK2, acc)
        mx(c, "2^{20} =", 1290, 670, 48, acc, PURPLE)
        text(c, "1 048 576", 1560, 690, 50, "black", PURPLE, acc)
        selo(c, 560, 300, acc, "MAIS DE R$ 1 MILHÃO", PURPLE, -5, 30)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "SOMAR NUNCA FARIA ISSO · MULTIPLICAR FAZ", W / 2, 850, ad, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO EXPONENCIAL · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de FUNÇÃO EXPONENCIAL", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "RECONHECER", "uma função exponencial", BLUE), ("02.b", "AS RESTRIÇÕES", "por que a base tem regras",
                                                                       PURPLE),
             ("02.c", "O GRÁFICO", "desenhar sem decorar", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a0 = ep(t, C["03"], 0.4)
    if a0 > 0:
        pill(c, "série de Potenciação e radiciação", 260, 230, BLUE, size=22, a=a0, bounds=(0, 1920))
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 280, 680, 200, 24, "#FFFFFF", aa, shadow=True)
        mx(c, "a^0 = 1", 580, 360, 80, aa, BLUE)
        text(c, "qualquer base diferente de zero", 580, 450, 26, "bold", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 240, 510, 680, 260, 24, "#FFFFFF", ab, shadow=True)
        K.expr(c, "2^{-2} = 1/2^2 = 1/4", 580, 620, 60, ab, cores={0: PURPLE, 4: GREEN})
        text(c, "expoente negativo INVERTE", 580, 735, 28, "black", PURPLE, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "série de Conceito de função", 1020, 230, BLUE, size=22, a=acc, bounds=(0, 1920))
        rrect(c, 1180, 360, 360, 260, 30, mix("#FFFFFF", BLUE, 0.12), acc, shadow=True)
        text_mid(c, "f", 1360, 490, 110, "black", BLUE, acc)
        arrow(c, 1030, 490, 1160, 490, INK2, acc, 6, 18)
        arrow(c, 1560, 490, 1690, 490, INK2, acc, 6, 18)
        text(c, "entra x", 1095, 455, 28, "black", INK, acc)
        text(c, "sai y", 1625, 455, 28, "black", INK, acc)


# ======================================================================
# concreto e bloco a — somar × multiplicar
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    rows = [("04.a", "MESADA", ["1", "2", "4", "8"], "×2", GREEN), ("04.b", "BOATO", ["1", "3", "9", "27"], "×3", PURPLE)]
    for k, (cue, nome, vals, op, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 220 + k * 170 + d
        rrect(c, 220, y, 1480, 140, 22, "#FFFFFF", a, shadow=True)
        text(c, nome, 260, y + 86, 40, "black", col, a, align="left")
        for j, v in enumerate(vals):
            xx = 700 + j * 230
            u = ep(t, C[cue] + 0.6 + 0.5 * j, 0.3)
            chip(c, v, xx, y + 70, col, a * u, size=40, w=130)
            if j > 0:
                text(c, op, xx - 115, y + 40, 24, "black", GRAY, a * u)
    acc, d = rise(t, C["04.c"])
    if acc > 0:
        y = 560 + d
        rrect(c, 220, y, 1480, 140, 22, "#FFFFFF", acc, shadow=True)
        text(c, "CAFÉ", 260, y + 86, 40, "black", RED, acc, align="left")
        P = Plano(700, y + 22, 700, 96, (0, 10), (0, 1))
        P.curva(c, acc, lambda x: 0.95 * 0.72 ** x, RED, u=ep(t, C["04.c"], 1.6), width=6)
        text(c, "rápido no começo,", 1460, y + 62, 24, "bold", INK2, acc, align="left")
        text(c, "devagar depois", 1460, y + 98, 24, "bold", INK2, acc, align="left")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "CADA PASSO MULTIPLICA PELO MESMO NÚMERO", W / 2, 790, ad, 36)


def b_escadas(c, t, C, B):
    head(c, t, B["start"], "SOMAR × MULTIPLICAR", "DUAS ESCADAS", PURPLE)
    aa = ep(t, C["05.a"], 0.5)
    ab = ep(t, C["05.b"], 0.5)
    n_s = clamp((t - C["05.a"]) / 3.0) * 8 if t >= C["05.a"] else 0
    n_m = 0.0
    if t >= C["05.b"]:
        n_m = min(5.0, (t - C["05.b"]) / 0.7)
    if t >= C["05.d"]:
        n_m = 5 + (t - C["05.d"]) / 0.6
    escadas(c, max(aa, ab), n_s, n_m)
    if aa > 0:
        pill(c, "FUNÇÃO AFIM · soma sempre o mesmo", 180, 745, BLUE, size=26, a=aa, bounds=(0, 1920))
    if ab > 0:
        pill(c, "EXPONENCIAL · multiplica sempre pelo mesmo", 1040, 745, PURPLE, size=26, a=ab, bounds=(0, 1920))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        defin(c, "FATOR", "o número que multiplica a cada passo", 540, 800, 840, acc, PURPLE, 28)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 230, ad, "SAIU DA TELA!", RED, 6, 30)


# ======================================================================
# bloco b — definição · bloco c — restrições
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "A FUNÇÃO EXPONENCIAL", "DEFINIÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 220, 1000, 220, 30, mix("#FFFFFF", BLUE, 0.08), aa)
        K.expr(c, "f(x) = a^x", W / 2, 330, 120, aa, cores={0: INK, 1: INK, 2: BLUE})
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        arrow(c, 980, 470, 1000, 380, BLUE, ab, 5, 16)
        pill(c, "BASE: o número que se multiplica", 900, 500, BLUE, size=26, a=ab, anchor="right", bounds=(0, 1920))
        ab2 = ep(t, C["06.b"] + 2.2, 0.4)
        arrow(c, 1110, 470, 1080, 290, PURPLE, ab2, 5, 16)
        pill(c, "EXPOENTE: quantas vezes", 1120, 500, PURPLE, size=26, a=ab2, bounds=(0, 1920))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        selo(c, 1520, 250, acc, "x NO EXPOENTE", PURPLE, 6, 28)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        for k, (s_, sub, col, ok) in enumerate((("2^x", "x no EXPOENTE → exponencial", GREEN, True),
                                                ("x^2", "x na BASE → NÃO é exponencial", RED, False))):
            x = 560 + k * 800
            rrect(c, x - 340, 600, 680, 200, 24, "#FFFFFF", ad, shadow=True)
            mx(c, s_, x - 180, 700, 80, ad, col)
            check_icon(c, x + 250, 660, 26, ad, col, "check" if ok else "x")
            text(c, sub, x + 40, 760, 24, "black", col, ad)
    elif acc > 0:
        regra(c, "A VARIÁVEL ESTÁ NO EXPOENTE", W / 2, 680, acc, 40)


def b_restricoes(c, t, C, B):
    head(c, t, B["start"], "AS REGRAS DA BASE", "POR QUE ELAS EXISTEM", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 560, 200, 800, 120, 24, mix("#FFFFFF", PURPLE, 0.10), aa)
        mx(c, "a > 0 e a ≠ 1", W / 2, 260, 62, aa, PURPLE)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 360, 740, 440, 24, "#FFFFFF", ab, shadow=True)
        text(c, "BASE 1", 570, 420, 34, "black", INK, ab)
        mx(c, "1^x = 1", 570, 490, 56, ab, INK)
        P = Plano(290, 560, 560, 160, (-2, 4), (0, 3))
        P.eixos(c, ab, xt=(), yt=(), grade=False)
        P.curva(c, ab, lambda x: 1, INK, u=ep(t, C["07.b"] + 1.0, 1.0), width=6)
        text(c, "parada: CONSTANTE", 570, 775, 28, "black", AMBER, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 360, 740, 440, 24, "#FFFFFF", acc, shadow=True)
        text(c, "BASE NEGATIVA", 1350, 420, 34, "black", INK, acc)
        K.expr(c, "(-4)^{1/2} = √{-4}", 1350, 510, 56, acc, cores={0: RED, 2: RED})
        check_icon(c, 1350, 610, 30, acc, RED, "x")
        text(c, "não é número real", 1350, 680, 30, "black", RED, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        P = Plano(1100, 700, 500, 80, (0, 10), (0, 1))
        for k in range(11):
            if k % 2 == 0:
                P.ponto(c, k, 0.5, RED, ad, None, r=7)
            else:
                c.drawCircle(P.px(k), P.py(0.5), 8, paint(RED, ad * 0.6, stroke=3))
        text(c, "cheia de buracos", 1350, 775, 26, "black", RED, ad)


# ======================================================================
# bloco d — as tabelas · atalho
# ======================================================================

XS = ["−2", "−1", "0", "1", "2", "3"]
V2 = ["1/4", "1/2", "1", "2", "4", "8"]
VM = ["4", "2", "1", "1/2", "1/4", "1/8"]


def _alfas_tab(t, t0, t_dir, t_esq, ncol=6, zero=2):
    """alfas por coluna: primeiro o zero, depois a direita (uma a uma), depois a esquerda"""
    al = [0.0] * ncol
    al[zero] = ep(t, t0, 0.4)
    for j, k in enumerate(range(zero + 1, ncol)):
        al[k] = ep(t, t_dir + 0.9 + 0.55 * j, 0.3)
    for j, k in enumerate(range(zero - 1, -1, -1)):
        al[k] = ep(t, t_esq + 1.0 + 0.6 * j, 0.3)
    return al


def b_tabela(c, t, C, B):
    sid = which(t, C, ["08", "09"])
    head_seq(c, t, C, [("08", "A TABELA DE 2ˣ", "COLUNA A COLUNA", BLUE), ("09", "E COM BASE 1/2?", "A MESMA LISTA",
                                                                                      PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["08.a"], 0.5)
    al2 = _alfas_tab(t, C["08.b"], C["08.c"], C["08.d"])
    linhas = [("2^x", V2, BLUE, al2)]
    if sid == "09":
        linhas.append(("(1/2)^x", VM, PURPLE, _alfas_tab(t, C["09.a"], C["09.b"], C["09.c"])))
    x0 = (W - (190 + 6 * 150)) / 2
    y0 = 320
    if sid == "08":
        tabela(c, x0, y0, XS, linhas, a0, setas=(0, "×2", "÷2", ep(t, C["08.c"], 0.4), ep(t, C["08.d"], 0.4)))
    else:
        tabela(c, x0, y0, XS, linhas, a0, setas=(1, "× 1/2", "", ep(t, C["09.b"], 0.4), 0))
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            regra(c, "A MESMA LISTA, DE TRÁS PARA A FRENTE", W / 2, 780, ad, 34, PURPLE)
            arrow(c, x0 + 190 + 5.5 * 150, y0 + 3 * 86 + 100, x0 + 190 + 0.5 * 150, y0 + 3 * 86 + 100, PURPLE, ad, 4, 16)


def b_atalho_tab(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "MONTE QUALQUER TABELA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["comece pelo 1 · direita × base · esquerda ÷ base"], a0, 38)
    xs = ["−2", "−1", "0", "1", "2"]
    v10 = ["1/100", "1/10", "1", "10", "100"]
    al = [0.0] * 5
    al[2] = ep(t, C["10.a"], 0.4)
    al[3] = ep(t, C["10.b"] + 0.8, 0.3)
    al[4] = ep(t, C["10.b"] + 1.4, 0.3)
    al[1] = ep(t, C["10.c"] + 0.8, 0.3)
    al[0] = ep(t, C["10.c"] + 1.4, 0.3)
    x0 = (W - (190 + 5 * 150)) / 2
    tabela(c, x0, 470, xs, [("10^x", v10, GREEN, al)], ep(t, C["10.a"], 0.4),
           setas=(0, "×10", "÷10", ep(t, C["10.b"], 0.4), ep(t, C["10.c"], 0.4)))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        pill(c, "nenhuma potência calculada", W / 2, 790, GREEN, size=28, a=ad, anchor="center")


# ======================================================================
# bloco e — sempre positivo
# ======================================================================

def b_positivo(c, t, C, B):
    head(c, t, B["start"], "SEMPRE POSITIVO", "A IMAGEM", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    x0 = (W - (190 + 6 * 150)) / 2
    tabela(c, x0, 210, XS, [("2^x", V2, BLUE, None), ("(1/2)^x", VM, PURPLE, None)], a0)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, x0 + 190, 296, 6 * 150, 172, 14, GREEN, aa * 0.14)
        selo(c, 1640, 250, aa, "NENHUM NEGATIVO", GREEN, 6, 24)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("positivo × positivo = ", INK2), ("positivo", GREEN)], W / 2, 545, 34, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        defin(c, "IMAGEM", "os valores que SAEM da função", 300, 600, 820, acc, BLUE, 28)
        # reta numérica com bolinha aberta no zero
        xa, xb, yy = 1180, 1680, 640
        line(c, xa, yy, xb, yy, INK2, acc, 4)
        line(c, xa + 80, yy, xb, yy, GREEN, acc, 10)
        arrow(c, xb - 30, yy, xb + 10, yy, GREEN, acc, 10, 22)
        c.drawCircle(xa + 80, yy, 13, paint("#FFFFFF", acc))
        c.drawCircle(xa + 80, yy, 13, paint(GREEN, acc, stroke=5))
        text(c, "0", xa + 80, yy + 46, 26, "black", INK, acc)
        mx(c, "]0, +∞[", W / 2, 760, 60, acc, GREEN)
        text(c, "todos os números maiores que zero", W / 2, 822, 26, "bold", INK2, acc)


# ======================================================================
# bloco f — o gráfico · atalho
# ======================================================================

def _plano_graf():
    return Plano(300, 210, 780, 590, (-3, 3.5), (-0.5, 8.5))


def b_grafico(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "O GRÁFICO DE 2ˣ", "PONTO A PONTO", BLUE), ("13", "O GRÁFICO DE (1/2)ˣ", "O ESPELHO",
                                                                                 PURPLE)])
    card(c, *CARD_R)
    P = _plano_graf()
    a0 = ep(t, C["12"], 0.4)
    P.eixos(c, a0, xt=range(-3, 4), yt=range(2, 9, 2))
    pts = [(-2, 0.25), (-1, 0.5), (0, 1), (1, 2), (2, 4), (3, 8)]
    for k, (x, y) in enumerate(pts):
        P.ponto(c, x, y, BLUE, ep(t, C["12.a"] + 0.4 * k, 0.3))
    P.curva(c, ep(t, C["12.b"], 0.4), lambda x: 2 ** x, BLUE, u=ep(t, C["12.b"], 1.6))
    pill(c, "2ˣ", P.px(2.6), P.py(6.2), BLUE, size=26, a=ep(t, C["12.b"] + 1.6, 0.4), anchor="right", bounds=(0, 1920))
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 1160, 230, 520, 150, 22, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "CRESCENTE", 1420, 290, 40, "black", BLUE, ab)
        text(c, "x aumenta → y aumenta", 1420, 345, 26, "bold", INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0 and sid == "12":
        c.drawCircle(P.px(-2.6), P.py(0.17), 34, paint(AMBER, acc * 0.5, stroke=4))
        pill(c, "gruda no eixo x, sem tocar", P.px(-2.2), P.py(1.4), AMBER, size=22, a=acc, bounds=(0, 1920))
    if sid == "12":
        return
    ptm = [(-3, 8), (-2, 4), (-1, 2), (0, 1), (1, 0.5), (2, 0.25), (3, 0.125)]
    for k, (x, y) in enumerate(ptm):
        P.ponto(c, x, y, PURPLE, ep(t, C["13.a"] + 0.3 * k, 0.3))
    P.curva(c, ep(t, C["13.a"], 0.4), lambda x: 0.5 ** x, PURPLE, u=ep(t, C["13.a"] + 1.0, 1.6))
    pill(c, "(1/2)ˣ", P.px(-2.6), P.py(6.2), PURPLE, size=26, a=ep(t, C["13.a"] + 2.4, 0.4), bounds=(0, 1920))
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 1160, 400, 520, 150, 22, mix("#FFFFFF", PURPLE, 0.10), aa)
        text(c, "DECRESCENTE", 1420, 460, 40, "black", PURPLE, aa)
        text(c, "x aumenta → y diminui", 1420, 515, 26, "bold", INK2, aa)
    ab2 = ep(t, C["13.b"], 0.5)
    if ab2 > 0:
        pulse = 0.5 + 0.5 * math.sin((t - C["13.b"]) * 6)
        c.drawCircle(P.px(0), P.py(1), 22 + 8 * pulse, paint(GREEN, ab2 * 0.35))
        P.ponto(c, 0, 1, GREEN, ab2, "(0, 1)", dx=26, dy=-46, size=24, r=11)
        mx(c, "a^0 = 1", 1420, 620, 48, ab2, GREEN)
    acc2 = ep(t, C["13.c"], 0.5)
    if acc2 > 0:
        line(c, P.px(0), P.y0, P.px(0), P.y0 + P.h, GREEN, acc2 * 0.6, 8, dash=(14, 10))
        rrect(c, 1160, 680, 520, 110, 22, "#FFFFFF", acc2, shadow=True)
        K.expr(c, "(1/2)^x = 2^{-x}", 1420, 735, 46, acc2, cores={0: PURPLE, 2: BLUE})
        pill(c, "ESPELHO no eixo y", P.px(0) + 16, P.y0 + 30, GREEN, size=22, a=acc2, bounds=(0, 1920))


def b_atalho_graf(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TRÊS PONTOS BASTAM", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.4)
    K.atalho(c, 1000, 200, 680, 150, "ATALHO", ["x = −1, 0 e 1"], a0, 44)
    aa = ep(t, C["14.a"], 0.5)
    P = Plano(300, 230, 560, 520, (-2, 2), (-0.3, 4))
    P.eixos(c, aa, xt=(-1, 1), yt=(1, 3))
    for k, (x, y) in enumerate(((-1, 1 / 3), (0, 1), (1, 3))):
        P.ponto(c, x, y, BLUE, ep(t, C["14.a"] + 0.5 * k, 0.3))
    for k, (x, y) in enumerate(((-1, 3), (1, 1 / 3))):
        P.ponto(c, x, y, PURPLE, ep(t, C["14.b"] + 2.4 + 0.4 * k, 0.3))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 390, 680, 120, 22, mix("#FFFFFF", BLUE, 0.10), ab)
        linha(c, [("base > 1  →  direita MAIS ALTA: ", INK), ("sobe", BLUE)], 1340, 450, 30, ab)
        ab2 = ep(t, C["14.b"] + 2.4, 0.4)
        rrect(c, 1000, 530, 680, 120, 22, mix("#FFFFFF", PURPLE, 0.10), ab2)
        linha(c, [("0 < base < 1  →  MAIS BAIXA: ", INK), ("desce", PURPLE)], 1340, 590, 30, ab2)
    acc = ep(t, C["14.c"], 0.5)
    P.curva(c, acc, lambda x: 3 ** x, BLUE, u=ep(t, C["14.c"], 1.2), width=6)
    P.curva(c, acc, lambda x: (1 / 3) ** x, PURPLE, u=ep(t, C["14.c"], 1.2), width=6)
    if acc > 0:
        pill(c, "ligue com uma curva suave", 1340, 720, GREEN, size=26, a=acc, anchor="center")


# ======================================================================
# bloco g — assíntota, coeficiente · atalho
# ======================================================================

def b_assintota(c, t, C, B):
    head(c, t, B["start"], "A ASSÍNTOTA", "UMA PAREDE INVISÍVEL", AMBER)
    card(c, *CARD_R)
    P = Plano(260, 230, 900, 520, (-1, 7), (-0.3, 2.2))
    a0 = ep(t, C["15"], 0.4)
    P.eixos(c, a0, xt=range(1, 8), yt=(1, 2))
    P.curva(c, a0, lambda x: 0.5 ** x, PURPLE, u=ep(t, C["15"], 1.4))
    aa = ep(t, C["15.a"], 0.5)
    parede(c, P, 0, aa, "y = 0")
    if aa > 0:
        defin(c, "ASSÍNTOTA", "a curva chega perto, sem tocar", 1200, 230, 500, aa, AMBER, 22)
        text(c, "NUNCA", 1450, 380, 70, "black", RED, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        selo(c, P.px(5.5), P.py(0) - 110, ab, "PAREDE INVISÍVEL", AMBER, -4, 28)
        for k, v in enumerate(("1/2", "1/4", "1/8", "1/16")):
            ak = ep(t, C["15.b"] + 1.6 + 0.5 * k, 0.3)
            mx(c, v, 1300 + (k % 2) * 220, 500 + (k // 2) * 120, 50, ak, PURPLE)
        ak = ep(t, C["15.b"] + 4.2, 0.4)
        if ak > 0:
            linha(c, [("encolhe · ", INK2), ("nunca vira 0", RED)], 1410, 760, 32, ak)


def b_coef(c, t, C, B):
    head(c, t, B["start"], "OUTROS NÚMEROS JUNTO", "COEFICIENTE E DESLOCAMENTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    P = Plano(260, 270, 520, 470, (-2, 2), (-0.5, 12))
    P.eixos(c, aa, xt=(-1, 1), yt=(1, 5, 10))
    P.curva(c, aa * 0.5, lambda x: 2 ** x, LIGHT, width=5)
    P.curva(c, aa, lambda x: 5 * 2 ** x, BLUE, u=ep(t, C["16.a"] + 1.0, 1.2))
    P.ponto(c, 0, 5, BLUE, ep(t, C["16.a"] + 2.2, 0.4), "(0, 5)", dx=24, dy=34)
    P.ponto(c, 0, 1, GRAY, ep(t, C["16.a"] + 2.6, 0.4), "(0, 1)", dx=24, dy=30, size=18, r=7)
    if aa > 0:
        defin(c, "COEFICIENTE", "o número que multiplica a potência", 200, 190, 760, aa, BLUE, 22)
        K.expr(c, "5 · 2^x", 520, 790, 46, aa, cores={0: BLUE, 2: INK})
    ab = ep(t, C["16.b"], 0.5)
    Q = Plano(1060, 270, 600, 450, (0, 6), (0, 100))
    Q.eixos(c, ab, xt=range(1, 7), yt=(22, 50, 92), rot=("t", "T"))
    if ab > 0:
        K.expr(c, "T = 22 + 70 · 0,5^t", 1360, 220, 44, ab, cores={0: INK, 2: AMBER, 4: INK, 6: PURPLE})
        pill(c, "sopa · cozinha a 22 °C", 1360, 800, INK2, size=24, a=ab, anchor="center")
    Q.curva(c, ab, lambda x: 22 + 70 * 0.5 ** x, RED, u=ep(t, C["16.b"] + 2.6, 2.2))
    acc = ep(t, C["16.c"], 0.5)
    parede(c, Q, 22, acc, "T = 22", rx=Q.x0 + Q.w - 10)
    if acc > 0:
        selo(c, 1460, 410, acc, "A PAREDE SUBIU", AMBER, -4, 26)


def b_atalho_ass(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ACHE A PAREDE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["17"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["tempo grande: apague a potência"], a0, 40)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        linha(c, [("base entre 0 e 1", PURPLE), ("  ·  tempo crescendo", INK2)], W / 2, 410, 34, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0 or aa > 0:
        al = 1 - 0.75 * ab
        K.expr(c, "T = 22 + 70 · 0,5^t", W / 2, 540, 80, max(aa, ab), cores={0: INK, 2: AMBER, 4: INK, 6: PURPLE},
               alfas={3: al, 4: al, 5: al, 6: al})
        if ab > 0:
            w_ = K.math_w("T = 22 + 70 · 0,5^t", 80)
            xs = W / 2 - w_ / 2 + K.math_w("T = 22 +", 80) + 18
            strike(c, xs, 540, W / 2 + w_ / 2, 540, ab, RED)
            pill(c, "≈ 0", W / 2 + w_ / 2 - 120, 620, RED, size=28, a=ab, anchor="center")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        c.drawCircle(W / 2 - K.math_w("T = 22 + 70 · 0,5^t", 80) / 2 + K.math_w("T =", 80) + 70, 540, 70,
                     paint(GREEN, acc, stroke=6))
        regra(c, "O NÚMERO SOMADO SOZINHO = ASSÍNTOTA", W / 2, 740, acc, 36, GREEN)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "COMECE PELO 1", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    xs = ["−2", "−1", "0", "1", "2"]
    v3 = ["1/9", "1/3", "1", "3", "9"]
    x0 = (W - (190 + 5 * 150)) / 2
    if t < C["19"]:
        tabela(c, x0, 290, xs, [("3^x", ["?"] * 5, AMBER, None)], aa)
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            pill(c, "comece pelo 1 · direita × 3 · esquerda ÷ 3", W / 2, 560, GREEN, size=28, a=ab, anchor="center")
        pause_timer(c, t, C["18.end"] - 1.9, W / 2, 700)
        return
    al = [0.0] * 5
    al[2] = ep(t, C["19.a"], 0.4)
    al[3] = ep(t, C["19.b"] + 0.9, 0.3)
    al[4] = ep(t, C["19.b"] + 1.6, 0.3)
    al[1] = ep(t, C["19.c"] + 1.0, 0.3)
    al[0] = ep(t, C["19.c"] + 1.8, 0.3)
    tabela(c, x0, 290, xs, [("3^x", v3, BLUE, al)], 1.0,
           setas=(0, "×3", "÷3", ep(t, C["19.b"], 0.4), ep(t, C["19.c"], 0.4)))
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 640, 1000, 150, 22, mix("#FFFFFF", GREEN, 0.10), ad)
        linha(c, [("nenhum negativo  ·  base 3 > 1  →  ", INK), ("SOBE", BLUE)], W / 2, 715, 38, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Na exponencial, cada passo multiplica pelo mesmo fator.",
          "Base maior que 1 sobe; base entre 0 e 1 desce; todas passam por (0, 1).",
          "A exponencial nunca chega a zero: ela só se aproxima da assíntota."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("2⁻³ = −8",
          "o sinal de menos está ali, e a gente leva ele para o resultado",
          "expoente negativo é um 'vire de cabeça para baixo': 2⁻³ = 1/8, positivo"),
         ("Achar que a curva ENCOSTA no eixo x em algum momento",
          "no desenho, ela fica tão colada que parece tocar",
          "a metade de um positivo ainda é positiva: a parede é invisível e nunca é tocada")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22"], ERROS)


# ======================================================================
# questão 9 (nós fazemos)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS9 = [("A", "25 °C.", "", GREEN), ("B", "40 °C.", "subtraiu: 65 − 25", RED),
         ("C", "65 °C.", "diferença inicial", RED), ("D", "77 °C.", "depois de 1 minuto", RED),
         ("E", "90 °C.", "temperatura inicial", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · NÓS FAZEMOS", "O CAFÉ NA SALA CLIMATIZADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 260, 680, 38, C["24.ok"], "A", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    if t < C["24"]:
        yend = _enunciado(c, [("Uma xícara de café é deixada sobre a mesa de uma sala climatizada. Sua temperatura, em "
                               "graus Celsius, t minutos depois, é modelada por", INK)], a0, 236, 28)
        K.expr(c, "T(t) = 25 + 65 · 0,8^t", 540, yend + 30, 46, a0, cores={2: AMBER, 4: BLUE, 6: PURPLE})
        _enunciado(c, [("De acordo com esse modelo, à medida que o tempo passa, a temperatura do café se aproxima de",
                        INK)], a0, yend + 120, 28)
        pause_timer(c, t, C["23.end"] - 1.9, 540, 760)
        return
    y0 = 206
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["24"], 0.4), shadow=True)
    a1 = ep(t, C["24"], 0.4)
    K.expr(c, "T(t) = 25 + 65 · 0,8^t", 540, y0 + 50, 42, a1, cores={2: AMBER, 4: BLUE, 6: PURPLE})
    aa = ep(t, C["24.a"], 0.4)
    if aa > 0:
        pill(c, "base 0,8: entre 0 e 1 → ENCOLHE", 540, y0 + 110, PURPLE, size=24, a=aa, anchor="center",
             bounds=(170, 910))
        for k, (e_, v, h) in enumerate((("0,8^1", "0,8", 140), ("0,8^2", "0,64", 112), ("0,8^3", "0,512", 90))):
            ak = ep(t, C["24.a"] + 2.0 + 0.9 * k, 0.3)
            x = 290 + k * 250
            rrect(c, x - 50, y0 + 320 - h, 100, h, 10, mix("#FFFFFF", PURPLE, 0.35), ak)
            mx(c, e_, x, y0 + 355, 30, ak, INK2)
            text(c, v, x, y0 + 408, 32, "black", PURPLE, ak)
    ab = ep(t, C["24.b"], 0.4)
    if ab > 0:
        linha(c, [("65 · 0,8^t  →  ", INK2), ("quase 0", RED)], 540, y0 + 465, 34, ab)
    acc = ep(t, C["24.c"], 0.4)
    if acc > 0:
        rrect(c, 200, y0 + 510, 680, 100, 18, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("sobra  T → ", INK), ("25 °C", GREEN), ("  (a assíntota)", INK2)], 540, y0 + 560, 36, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUAL É O FATOR?", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 640, 180, 24, "#FFFFFF", aa, shadow=True)
        text(c, "CARRO", 580, 300, 28, "black", BLUE, aa)
        text(c, "R$ 60.000,00", 580, 380, 56, "black", BLUE, aa)
        ab0 = ep(t, C["27.a"] + 1.6, 0.5)
        rrect(c, 1020, 240, 640, 180, 24, "#FFFFFF", ab0, shadow=True)
        text(c, "PERDE POR ANO", 1340, 300, 28, "black", RED, ab0)
        text(c, "15%", 1340, 380, 64, "black", RED, ab0)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 470, 1200, 200, 26, mix("#FFFFFF", AMBER, 0.20), ab)
        text(c, "o preço do ano seguinte:", W / 2, 530, 32, "bold", INK2, ab)
        text_mid(c, "× 0,15  ou  × 0,85 ?", W / 2, 610, 64, "black", INK, ab)
    pill(c, "ep. 2 · o modelo Q₀ · aᵗ: da frase do enunciado ao fator", W / 2, 760, PURPLE, size=26,
         a=ep(t, C["27.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"],
        "Onde mais você já viu algo crescer multiplicando?", canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, escadas=b_escadas,
              definicao=b_definicao, restricoes=b_restricoes, tabela=b_tabela, atalho_tab=b_atalho_tab,
              positivo=b_positivo, grafico=b_grafico, atalho_graf=b_atalho_graf, assintota=b_assintota, coef=b_coef,
              atalho_ass=b_atalho_ass, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q9=b_q9, ponte=b_ponte,
              cta=b_cta)
