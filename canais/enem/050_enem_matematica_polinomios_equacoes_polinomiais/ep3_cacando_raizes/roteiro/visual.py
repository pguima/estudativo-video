"""Visual — Polinômios e Equações Polinomiais, Episódio 3: caçando raízes (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: chave() e molho() (o molho de chaves das candidatas; a que gira fica verde), fechadura() (a porta
P(x) = 0 que abre), esteira() (o dispositivo de Briot-Ruffini preenchido casa a casa), predio() (os andares do polinômio,
que perde o de cima), espelho() (a raiz e o fator dos dois lados de um espelho, com o sinal invertido).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum050", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_polinomios_ep3_cacando_raizes.mp4"
CARD_R = K.CARD_R
OURO = "#D4A93A"
OURO_D = "#A9822A"


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


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def chave(c, cx, cy, rot, a, col=None, giro=0.0, size=28, w=150):
    """chave deitada: argola à esquerda com o rótulo, haste e dentes; giro 0 → 1 gira a chave (só a argola tomba)"""
    if a <= 0:
        return
    col = col or OURO
    c.save()
    c.translate(cx, cy)
    c.rotate(-90 * giro)
    r = 34
    c.drawCircle(-w / 2 + r, 0, r, paint(col, a))
    c.drawCircle(-w / 2 + r, 0, r, paint(mix(col, "#000000", 0.25), a, stroke=3))
    rrect(c, -w / 2 + 2 * r - 6, -8, w - 2 * r + 6, 16, 6, col, a)
    for k in range(2):
        rrect(c, w / 2 - 34 + k * 18, 6, 12, 20, 3, col, a)
    c.restore()
    ftext(c, rot, cx - w / 2 + r, cy + size * 0.36, size, "black", INK, a)


def molho(c, cx, cy, rots, a, testadas=(), ok=None, giro=0.0, raio=230, size=28):
    """o molho: argola central e as chaves em leque; testadas = índices já testados (cinza riscado), ok = a que girou"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, 46, paint(GRAY, a, stroke=10))
    n = len(rots)
    for k, rot in enumerate(rots):
        ang = math.radians(200 + 140 * k / max(1, n - 1))
        kx, ky = cx + raio * math.cos(ang), cy + raio * math.sin(ang) * 0.75
        line(c, cx, cy, kx, ky, GRAY, a * 0.6, 3)
        if k == ok:
            col = GREEN
        elif k in testadas:
            col = "#C9C6BD"
        else:
            col = OURO
        chave(c, kx, ky, rot, a, col, giro if k == ok else 0.0, size)


def fechadura(c, cx, cy, s, a, aberta=0.0, w=420, h=300):
    """a porta P(x) = 0: abre (aberta 0 → 1) e acende verde"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 24, mix("#FFFFFF", GREEN if aberta > 0.5 else INK2, 0.10), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 24, 24),
                paint(GREEN if aberta > 0.5 else INK2, a, stroke=4))
    c.drawCircle(cx, cy - 20, 30, paint(INK if aberta < 0.5 else GREEN, a))
    rrect(c, cx - 12, cy - 10, 24, 60, 8, INK if aberta < 0.5 else GREEN, a)
    expr(c, s, cx, cy + h / 2 - 50, 34, a)
    if aberta > 0:
        pill(c, "ABRIU!", cx, cy - h / 2 - 10, GREEN, size=28, a=aberta, anchor="center", bounds=(0, 1920))


def esteira(c, x, y, coefs, raiz, res, a, prog=99, cw=150, ch=100, size=44, destaque_zero=False):
    """dispositivo de Briot-Ruffini: raiz à esquerda; linha 1 = coeficientes; linha 2 = resultados (prog = quantas casas já
    preenchidas). A última casa é o resto (verde se 0)."""
    if a <= 0:
        return
    n = len(coefs)
    rrect(c, x - 20, y - 20, cw * (n + 1) + 40, ch * 2 + 40, 22, "#FFFFFF", a, shadow=True)
    line(c, x + cw, y, x + cw, y + ch * 2, INK, a, 4)
    line(c, x + cw, y + ch, x + cw * (n + 1), y + ch, INK, a, 4)
    expr(c, raiz, x + cw / 2, y + ch / 2, size, a, cores={0: PURPLE})
    for k, cf in enumerate(coefs):
        cx = x + cw * (k + 1.5)
        col = AMBER if (destaque_zero and cf == "0") else INK
        expr(c, cf, cx, y + ch / 2, size, a, cores={0: col})
    for k, r in enumerate(res):
        if k >= prog:
            break
        cx = x + cw * (k + 1.5)
        resto = k == n - 1
        if resto:
            rrect(c, cx - cw / 2 + 10, y + ch + 10, cw - 20, ch - 20, 16, mix("#FFFFFF", GREEN, 0.25), a)
        expr(c, r, cx, y + ch * 1.5, size, a, cores={0: GREEN if resto else BLUE})
    if prog >= n:
        text(c, "resto", x + cw * (n + 0.5), y + ch * 2 + 44, 24, "bold", GREEN, a)


def predio(c, x, ybase, andares, a, cai=0.0, w=260, h=80, col=None):
    """prédio de baixo para cima: andares = rótulos; cai 0 → 1 faz o andar de cima subir e sumir"""
    if a <= 0:
        return
    col = col or PURPLE
    rrect(c, x - 20, ybase - 4, w + 40, 12, 6, INK2, a)
    n = len(andares)
    for k, rot in enumerate(andares):
        y = ybase - (k + 1) * h
        topo = k == n - 1
        aa = a * (1 - cai) if topo else a
        dy = -60 * cai if topo else 0
        if aa <= 0:
            continue
        rrect(c, x, y + 4 + dy, w, h - 8, 14, mix("#FFFFFF", col, 0.30) if topo else "#FFFFFF", aa, shadow=True)
        expr(c, rot, x + w / 2, y + h / 2 + dy, 38, aa, cores={0: col if topo else INK2})
    text(c, f"GRAU {n - 1 if cai < 0.5 else n - 2}", x + w / 2, ybase + 56, 34, "black", col, a)


def espelho(c, cx, cy, esq, dir_, a, prog=1.0, size=60):
    """raiz à esquerda, espelho no meio, fator à direita (aparece com prog)"""
    if a <= 0:
        return
    rrect(c, cx - 8, cy - 130, 16, 260, 8, mix("#FFFFFF", BLUE, 0.5), a)
    c.drawRect(skia.Rect.MakeXYWH(cx - 8, cy - 130, 16, 260), paint(BLUE, a, stroke=3))
    text(c, "RAIZ", cx - 300, cy - 90, 26, "black", INK2, a, tracking=2)
    text(c, "FATOR", cx + 300, cy - 90, 26, "black", INK2, a, tracking=2)
    expr(c, esq, cx - 300, cy + 10, size, a, cores={0: RED})
    if prog > 0:
        expr(c, dir_, cx + 300, cy + 10, size, a * prog, cores={0: GREEN})
        arrow(c, cx - 150, cy + 10, cx + 150, cy + 10, BLUE, a * prog, 4, 14)


RAIZES_G = ["±1", "±2", "±3", "±6"]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POLINÔMIOS · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 200, 640, 120, 22, mix("#FFFFFF", RED, 0.10), aa)
        text_mid(c, "\"Bhaskara do 3º grau\"", 620, 260, 42, "black", INK, aa)
        selo(c, 1010, 205, aa, "NÃO NA PROVA", RED, 8, 26)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        expr(c, "x^3 − 2x^2 − 5x + 6 = 0", 960, 420, 80, ab, cores={0: PURPLE})
        pill(c, "em 1 minuto", 1530, 230, GREEN, size=34, a=ab, anchor="center")
    for k, (cue, s, col) in enumerate((("01.c", "teste uma CHAVE", OURO_D), ("01.d", "baixe um GRAU", PURPLE),
                                        ("01.e", "termine com BHASKARA", BLUE))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 240, 560 + d, 480, 150, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x - 190, 635 + d, ak, 30, bg=col)
        text_mid(c, s, x + 30, 635 + d, 34, "black", col, ak)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "POLINÔMIOS · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de POLINÔMIOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "TODAS AS RAÍZES", "grau 3, coeficientes inteiros", PURPLE),
             ("02.b", "FORMA FATORADA", "sem errar sinal", GREEN)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 320, 340, 640, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 320, 340, 640, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 46, "black", col, ak)
        text(c, sb, x, 625, 30, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Episódio 2", 300, y - 75, BLUE, size=22, a=a)
        expr(c, "P(a) = 0  →  a é raiz", 640, y, 46, a)
        text_mid(c, "Briot-Ruffini divide por (x − a)", 1250, y, 34, "bold", INK2, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Equação do 2º grau", 300, y - 75, PURPLE, size=22, a=a)
        text_mid(c, "Bhaskara · soma e produto", 640, y, 36, "black", INK, a)
        expr(c, "a(x−x1)(x−x2)", 1250, y, 50, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Divisibilidade", 300, y - 75, GREEN, size=22, a=a)
        text_mid(c, "divisores de 6:  1, 2, 3, 6", 960, y, 46, "black", INK, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O LUCRO QUE ZERA", "E O MOLHO DE CHAVES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    fa = ep(t, C["04.c"], 0.5)
    if a0 > 0:
        # gráfico do lucro que zera
        x0, y0, w, h = 260, 260, 640, 420
        ax = a0 * (1 - 0.6 * fa)
        line(c, x0, y0 + h / 2, x0 + w, y0 + h / 2, INK2, ax, 3)
        line(c, x0, y0, x0, y0 + h, INK2, ax, 3)
        p = skia.Path()
        for i in range(101):
            u = 0.55 + i / 100 * 3.0
            v = (u - 1) * (u - 2) * (u - 3)
            px, py = x0 + u / 4 * w, y0 + h / 2 - v * 110
            p.moveTo(px, py) if i == 0 else p.lineTo(px, py)
        c.drawPath(p, paint(PURPLE, ax, stroke=6))
        text(c, "lucro", x0 + 20, y0 - 14, 26, "bold", INK2, ax, align="left")
        text(c, "produção", x0 + w - 10, y0 + h / 2 + 44, 26, "bold", INK2, ax, align="right")
        aa = ep(t, C["04.a"], 0.5) * (1 - 0.6 * fa)
        for u in (1, 2, 3):
            c.drawCircle(x0 + u / 4 * w, y0 + h / 2, 14, paint(RED, aa))
        if aa > 0:
            pill(c, "lucro ZERO", x0 + w / 2, y0 + h + 40, RED, size=28, a=aa, anchor="center")
    ab = ep(t, C["04.b"], 0.5) * (1 - fa)
    if ab > 0:
        cartao(c, 1000, 330, 640, 160, ab)
        text_mid(c, "zeros = RAÍZES", 1320, 410, 52, "black", PURPLE, ab)
    if fa > 0:
        molho(c, 1300, 520, RAIZES_G, fa, size=26, raio=220)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            pill(c, "teste uma por uma", 1300, 790, OURO_D, size=30, a=ad, anchor="center")


# ======================================================================
# bloco a — teorema fundamental · bloco b — forma fatorada
# ======================================================================

def b_tfa(c, t, C, B):
    head(c, t, B["start"], "QUANTAS RAÍZES?", "O TEOREMA FUNDAMENTAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "EQUAÇÃO POLINOMIAL", "um polinômio igual a zero", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        regra(c, "grau n  →  exatamente n raízes", 960, 380, ab, 52, PURPLE)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        for k in range(3):
            c.drawCircle(760 + k * 200, 540, 54, paint(mix("#FFFFFF", PURPLE, 0.25), acc))
            text_mid(c, f"r{k + 1}", 760 + k * 200, 540, 40, "black", PURPLE, acc)
        text(c, "grau 3 → 3 raízes", 960, 650, 38, "black", INK, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        pill(c, "algumas REAIS · outras COMPLEXAS (com i, próxima série)", 960, 750, BLUE, size=30, a=ad, anchor="center")


def b_fatorada(c, t, C, B):
    head(c, t, B["start"], "A FORMA FATORADA", "AS RAÍZES MONTAM O POLINÔMIO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    defin(c, "FORMA FATORADA", "o polinômio como multiplicação · cada pedaço é um FATOR", 260, 200, 1400, aa, BLUE, 30)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        for k, r in enumerate(("−2", "1", "3")):
            pill(c, r, 760 + k * 200, 360, RED, size=44, a=ab, anchor="center")
        text(c, "raízes", 560, 372, 30, "bold", INK2, ab, align="right")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        expr(c, "(x+2)(x−1)(x−3)", 960, 500, 72, acc, cores={0: GREEN})
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        arrow(c, 960, 560, 960, 610, PURPLE, ad, 5, 16)
        rrect(c, 460, 630, 1000, 120, 22, mix("#FFFFFF", PURPLE, 0.14), ad)
        expr(c, "x^3 − 2x^2 − 5x + 6", 960, 690, 60, ad, cores={0: PURPLE})
        pill(c, "o do gancho", 1560, 690, AMBER, size=26, a=ad, anchor="center")


def b_espelho(c, t, C, B):
    head(c, t, B["start"], "O ESPELHO", "RAIZ E FATOR TÊM SINAIS OPOSTOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    ab = ep(t, C["07.b"], 0.5)
    if ab <= 0:
        espelho(c, 960, 430, "−2", "(x+2)", aa, ep(t, C["07.a"] + 1.2, 0.6))
    else:
        espelho(c, 960, 430, "3", "(x−3)", ab, ep(t, C["07.b"] + 1.0, 0.6))
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "o sinal INVERTE no espelho", 960, 650, acc, 42, PURPLE)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "x + 2 = 0  só quando  x = −2", 960, 760, GREEN, size=32, a=ad, anchor="center")


def b_dominante(c, t, C, B):
    head(c, t, B["start"], "FALTA UMA PEÇA", "O COEFICIENTE DOMINANTE", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        expr(c, "2x^2 − 2", 960, 280, 80, aa, cores={0: AMBER})
        text(c, "raízes:  1  e  −1", 960, 400, 40, "black", INK2, aa)
    ab = ep(t, C["08.b"], 0.5)
    acc = ep(t, C["08.c"], 0.5)
    if ab > 0:
        cartao(c, 300, 460, 600, 150, ab)
        expr(c, "(x−1)(x+1)", 600, 535, 56, ab * (1 - 0.5 * acc))
        if acc > 0:
            strike(c, 400, 535, 800, 535, acc, RED, acc)
    if acc > 0:
        cartao(c, 1020, 460, 600, 150, acc, GREEN, True)
        expr(c, "2(x−1)(x+1)", 1320, 535, 56, acc, cores={0: GREEN})
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        regra(c, "P(x) = a(x − r1)(x − r2)...  ·  a = dominante", 960, 720, ad, 36, PURPLE)


def b_atalho_espelho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TROQUE O SINAL E CONFIRA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · O ESPELHO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, s1, s2) in enumerate((("09.a", "raiz −2", "fator (x + 2)"),
                                        ("09.b", "x = −2 em (x + 2)", "−2 + 2 = 0  ✓"),
                                        ("09.c", "o número da frente", "vai antes dos fatores"))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 360 + k * 140 + d
        rrect(c, 340, y - 55, 1240, 110, 22, "#FFFFFF", ak, shadow=True)
        text(c, s1, 400, y + 14, 40, "black", INK, ak, align="left")
        text(c, s2, 1520, y + 14, 40, "black", GREEN, ak, align="right")


# ======================================================================
# bloco c — multiplicidade · bloco d — candidatas
# ======================================================================

def b_multiplicidade(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICIDADE", "RAIZ QUE APARECE DUAS VEZES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    ab = ep(t, C["10.b"], 0.5)
    if aa > 0:
        expr(c, "(x+1)^2(x−3)", 960, 280, 84, aa, cores={0: PURPLE} if ab > 0 else None)
    if ab > 0:
        for k in range(2):
            cartao(c, 470 + k * 340, 400, 300, 120, ab, PURPLE, True)
            expr(c, "(x+1)", 620 + k * 340, 460, 52, ab, cores={0: PURPLE})
        cartao(c, 1150, 400, 300, 120, ab)
        expr(c, "(x−3)", 1300, 460, 52, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        pill(c, "−1: RAIZ DUPLA", 790, 580, PURPLE, size=32, a=acc, anchor="center")
        pill(c, "3: RAIZ SIMPLES", 1300, 580, BLUE, size=32, a=acc, anchor="center")
        defin(c, "MULTIPLICIDADE", "quantas vezes a raiz aparece", 260, 640, 1400, acc, BLUE, 30)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        text(c, "3 raízes contadas · 2 valores diferentes", 960, 790, 36, "black", INK, ad)


def b_candidatas(c, t, C, B):
    head(c, t, B["start"], "AS CANDIDATAS", "QUAIS CHAVES TESTAR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    ab = ep(t, C["11.b"], 0.5)
    defin(c, "RAIZ RACIONAL", "inteiro ou fração · CANDIDATA: pode ser raiz", 260, 200, 1400, aa * (1 - ab), BLUE, 30)
    if ab > 0:
        rrect(c, 360, 200, 1200, 220, 26, mix("#FFFFFF", PURPLE, 0.12), ab)
        expr(c, "candidata = p/q", 700, 310, 66, ab, cores={2: PURPLE})
        text(c, "p divide o termo independente", 1050, 290, 32, "black", INK, ab, align="left")
        text(c, "q divide o coeficiente dominante", 1050, 360, 32, "black", INK, ab, align="left")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        pill(c, "exemplo: termo 4 · dominante 3", 960, 470, AMBER, size=28, a=acc, anchor="center")
        cands = ["±1", "±2", "±4", "±1/3", "±2/3", "±4/3"]
        for k, s in enumerate(cands):
            x = 420 + k * 216
            rrect(c, x - 95, 520, 190, 120, 20, "#FFFFFF", acc, shadow=True)
            expr(c, s, x, 580, 46, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        regra(c, "dominante 1 → só os INTEIROS que dividem o termo independente", 960, 730, ad, 32, PURPLE)


# ======================================================================
# bloco e — o roteiro de 4 passos · bloco f — atalhos de teste
# ======================================================================

def b_passo1(c, t, C, B):
    head(c, t, B["start"], "PASSOS 1 E 2", "AS CHAVES E O TESTE", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    expr(c, "P(x) = x^3 − 2x^2 − 5x + 6", 960, 230, 54, a0)
    aa = ep(t, C["12.a"], 0.5)
    giro = ep(t, C["12.c"], 0.8)
    ok = 0 if t >= C["12.b"] + 3.0 else None
    molho(c, 620, 640, ["1", "−1", "2", "−2", "3", "−3", "6", "−6"], aa, ok=ok, giro=giro, raio=330, size=24)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        cartao(c, 1060, 330, 600, 140, ab)
        expr(c, "P(1) = 1 − 2 − 5 + 6", 1360, 380, 40, ab)
        text(c, "= 0", 1360, 450, 44, "black", GREEN, ab)
        fechadura(c, 1360, 680, "P(x) = 0", ab, giro, h=240)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        pill(c, "1 é RAIZ", 620, 790, GREEN, size=40, a=acc, anchor="center")


def b_passo3(c, t, C, B):
    head(c, t, B["start"], "PASSO 3", "DERRUBAR UM ANDAR", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["13"], 0.4)
    aa = ep(t, C["13.a"], 0.5)
    t0 = C["13.b"]
    prog = sum(1 for dt in (0.0, 2.2, 5.0, 7.8) if t >= t0 + dt)
    esteira(c, 260, 300, ["1", "−2", "−5", "6"], "1", ["1", "−1", "−6", "0"], aa, prog, cw=150, ch=100)
    cai = ep(t, C["13.c"] + 2.0, 1.0)
    predio(c, 1280, 720, ["x^0", "x", "x^2", "x^3"], a0, cai, w=280, h=100)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 620, 880, 110, 22, mix("#FFFFFF", PURPLE, 0.14), acc)
        expr(c, "x^2 − x − 6", 670, 675, 58, acc, cores={0: PURPLE})


def b_passo4(c, t, C, B):
    head(c, t, B["start"], "PASSO 4", "TERMINAR NO 2º GRAU", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.4)
    expr(c, "x^2 − x − 6 = 0", 960, 240, 64, a0)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        pill(c, "soma 1", 760, 340, BLUE, size=32, a=aa, anchor="center")
        pill(c, "produto −6", 1160, 340, BLUE, size=32, a=aa, anchor="center")
        text(c, "3  e  −2", 960, 440, 60, "black", GREEN, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        cartao(c, 260, 500, 680, 150, ab)
        expr(c, "P(3) = 27 − 18 − 15 + 6", 600, 550, 36, ab)
        text(c, "= 0 ✓", 600, 620, 40, "black", GREEN, ab)
        ab2 = ep(t, C["14.b"] + 4.5, 0.5)
        if ab2 > 0:
            cartao(c, 980, 500, 680, 150, ab2)
            expr(c, "P(−2) = −8 − 8 + 10 + 6", 1320, 550, 36, ab2)
            text(c, "= 0 ✓", 1320, 620, 40, "black", GREEN, ab2)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        regra(c, "S = { −2, 1, 3 }", 960, 740, acc, 56, PURPLE)


def b_atalho_testes(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUAL CHAVE TESTAR PRIMEIRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · TESTE O 1 E O −1", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, q, r) in enumerate((("15.a", "x = 1", "some os coeficientes"),
                                      ("15.b", "x = −1", "troque o sinal dos termos de grau ÍMPAR"))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 360 + k * 150 + d
        rrect(c, 340, y - 55, 1240, 110, 22, "#FFFFFF", ak, shadow=True)
        pill(c, q, 420, y, GREEN, size=40, a=ak, anchor="left", bounds=(0, 1920))
        text(c, r, 1520, y + 14, 36, "black", INK, ak, align="right")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        expr(c, "P(−1) = −1 − 2 + 5 + 6 = 8", 960, 690, 46, acc, cores={8: RED})
        pill(c, "−1 NÃO é raiz", 960, 760, RED, size=28, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "O ZERO NA ESTEIRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    expr(c, "x^3 − 7x + 6 = 0", 960, 240, 72, aa)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 960, 520)
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        expr(c, "1 + 0 − 7 + 6 = 0", 960, 340, 46, a1, cores={2: AMBER, 6: GREEN})
    ab = ep(t, C["17.b"], 0.5)
    t0 = C["17.c"]
    prog = sum(1 for dt in (0.0, 1.0, 2.0, 3.0) if t >= t0 + dt)
    esteira(c, 380, 420, ["1", "0", "−7", "6"], "1", ["1", "1", "−6", "0"], ab, prog, cw=140, ch=90, size=40,
            destaque_zero=True)
    if ab > 0:
        pill(c, "sem x²: entra um ZERO", 1500, 420, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 680, 1200, 110, 22, mix("#FFFFFF", PURPLE, 0.14), ad)
        linha(c, [("x² + x − 6 → 2 e −3   ·   ", INK), ("S = {−3, 1, 2}", PURPLE)], 960, 735, 40, ad)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Raiz e fator têm sinais opostos.",
          "Candidatas: divisores do termo independente sobre divisores do dominante.",
          "Achou uma raiz, Briot-Ruffini derruba um grau."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "27"])
    frame(c, t, B["start"] if sid == "18" else C["27"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("a raiz −2 virar o fator (x − 2)",
          "a gente copia o número que viu, com o mesmo sinal",
          "x − 2 só zera em x = 2. O fator certo é (x + 2)."),
         ("2x² − 2 escrito como (x − 1)(x + 1)",
          "as raízes 1 e −1 estão certas",
          "esse produto dá x² − 1. Falta o 2 na frente: 2(x − 1)(x + 1).")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20"], ERROS)


# ======================================================================
# questão 3 (eu faço) e questão 7 (você faz)
# ======================================================================

ALTS3 = [("A", "2 e 3", "", GREEN), ("B", "−2 e −3", "trocou os sinais", RED),
         ("C", "5 e 6", "leu os coeficientes", RED), ("D", "1 e 6", "errou: −7", RED),
         ("E", "−1 e 6", "sinal do 6", RED)]


def b_q3(c, t, C, B):
    sid = which(t, C, ["21", "22", "23"])
    heads = {"21": "O LUCRO DA FÁBRICA", "22": "EU FAÇO", "23": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "21" else C[sid], "QUESTÃO 3 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1240, 250, 480, 34, C["22.ok"], "A", cues_in, cues_x, gap=30)
    a0 = ep(t, C["21.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "21":
        if a0 > 0:
            expr(c, "L(x) = x^3 − 6x^2 + 11x − 6", 680, 320, 50, a0, cores={0: PURPLE})
            text(c, "x em centenas · 0 ≤ x ≤ 4 · L em milhares de R$", 680, 410, 26, "bold", INK2, a0)
        ab = ep(t, C["21.b"], 0.5)
        if ab > 0:
            cartao(c, 260, 480, 840, 140, ab)
            text_mid(c, "L(1) = 0  ·  os OUTROS zeros?", 680, 550, 40, "black", INK, ab)
        return
    if sid == "22":
        aa = ep(t, C["22.a"], 0.5)
        t0 = C["22.b"]
        prog = sum(1 for dt in (0.0, 1.0, 2.6, 4.2) if t >= t0 + dt)
        esteira(c, 230, 230, ["1", "−6", "11", "−6"], "1", ["1", "−5", "6", "0"], aa, prog, cw=170, ch=95, size=42)
        acc = ep(t, C["22.c"], 0.5)
        if acc > 0:
            rrect(c, 200, 520, 960, 110, 22, mix("#FFFFFF", PURPLE, 0.14), acc)
            linha(c, [("x² − 5x + 6 → ", INK), ("2 e 3", GREEN)], 680, 575, 44, acc)
        ad = ep(t, C["22.d"], 0.5)
        if ad > 0:
            linha(c, [("L(2) = 8 − 24 + 22 − 6 = ", INK), ("0", GREEN)], 680, 680, 32, ad)
            linha(c, [("L(3) = 27 − 54 + 33 − 6 = ", INK), ("0", GREEN)], 680, 740, 32, ad)
        return
    # 23: armadilhas — a esteira certa como referência
    esteira(c, 230, 300, ["1", "−6", "11", "−6"], "1", ["1", "−5", "6", "0"], ep(t, C["23"], 0.4), 4, cw=170, ch=95,
            size=42)
    axd = ep(t, C["23.xd"], 0.5)
    if axd > 0:
        selo(c, 680, 620, axd, "1 · 1 − 6 = −5, não −7", AMBER, -3, 30)


ALTS7 = [("A", "{−2, −1/2, 1}", "trocou os sinais", RED), ("B", "{−1, 2}", "só inteiros", RED),
         ("C", "{−2, −1, 1, 2}", "não testou", RED), ("D", "{1/2, 1, 2}", "1 não é raiz", RED),
         ("E", "{−1, 1/2, 2}", "", GREEN)]


def b_q7(c, t, C, B):
    sid = which(t, C, ["24", "25", "26"])
    heads = {"24": "VOCÊ FAZ", "25": "VAMOS CONFERIR", "26": "AS OUTRAS"}
    head(c, t, B["start"] if sid == "24" else C[sid], "QUESTÃO 7 · ESTILO ENEM", heads[sid], GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS7, 1220, 250, 500, 34, C["25.ok"], "E", cues_in, cues_x, gap=30)
    a0 = ep(t, C["24.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "2x^3 − 3x^2 − 3x + 2 = 0", 680, 260, 50, a0, cores={0: PURPLE})
    if sid == "24":
        if a0 > 0:
            text(c, "conjunto solução = ?", 680, 360, 40, "black", INK, a0)
        pause_timer(c, t, C["24.end"] - 1.9, 680, 560)
        return
    if sid == "25":
        aa = ep(t, C["25.a"], 0.5)
        if aa > 0:
            linha(c, [("candidatas: ", INK2), ("±1, ±2, ±1/2", OURO_D)], 680, 340, 38, aa)
        ab = ep(t, C["25.b"], 0.5)
        if ab > 0:
            linha(c, [("P(1) = ", INK), ("−2", RED), ("     P(−1) = ", INK), ("0", GREEN)], 680, 420, 38, ab)
        acc = ep(t, C["25.c"], 0.5)
        t0 = C["25.c"]
        prog = sum(1 for dt in (0.6, 1.4, 2.2, 3.0) if t >= t0 + dt)
        esteira(c, 270, 480, ["2", "−3", "−3", "2"], "−1", ["2", "−5", "2", "0"], acc, prog, cw=150, ch=80, size=38)
        ad = ep(t, C["25.d"], 0.5)
        if ad > 0:
            rrect(c, 200, 700, 960, 90, 20, mix("#FFFFFF", PURPLE, 0.14), ad)
            linha(c, [("Δ = 9 · (5 ± 3)/4 → ", INK), ("2 e 1/2", GREEN)], 680, 745, 36, ad)
        return
    # 26: as outras — a fechadura com as chaves que giraram
    a6 = ep(t, C["26"], 0.4)
    molho(c, 680, 640, ["−1", "1/2", "2", "1", "−2"], a6, testadas=(3, 4), ok=None, raio=260, size=24)
    if a6 > 0:
        pill(c, "giram: −1, 1/2 e 2", 680, 360, GREEN, size=32, a=a6, anchor="center")
        axc = ep(t, C["26.xc"], 0.5)
        if axc > 0:
            pill(c, "P(1) = −2 · P(−2) = −20", 680, 780, RED, size=28, a=axc, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "GIRARD E GRÁFICOS", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        # bloco retangular
        x0, y0, L, H, P = 360, 330, 360, 220, 160
        dx, dy = P * 0.62, -P * 0.42
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, L, H), paint(mix("#FFFFFF", BLUE, 0.25), aa))
        p = skia.Path(); p.moveTo(x0, y0); p.lineTo(x0 + dx, y0 + dy); p.lineTo(x0 + L + dx, y0 + dy); p.lineTo(x0 + L, y0)
        p.close(); c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.40), aa))
        p2 = skia.Path(); p2.moveTo(x0 + L, y0); p2.lineTo(x0 + L + dx, y0 + dy); p2.lineTo(x0 + L + dx, y0 + dy + H)
        p2.lineTo(x0 + L, y0 + H); p2.close(); c.drawPath(p2, paint(mix("#FFFFFF", BLUE, 0.55), aa))
        for s_, px, py in (("?", x0 + L / 2, y0 + H + 44), ("?", x0 - 34, y0 + H / 2 + 14), ("?", x0 + L + dx / 2 + 30,
                                                                                               y0 + dy / 2 - 10)):
            text(c, s_, px, py, 44, "black", RED, aa)
        expr(c, "2x^3 − 14x^2 + 28x − 16 = 0", 1240, 380, 44, aa, cores={0: PURPLE})
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        text(c, "volume = ?   sem achar nenhuma aresta", 1240, 520, 38, "black", INK, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        selo(c, 1240, 680, acc, "DÁ. PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Qual chave você testa primeiro?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, tfa=b_tfa, fatorada=b_fatorada,
              espelho=b_espelho, dominante=b_dominante, atalho_espelho=b_atalho_espelho,
              multiplicidade=b_multiplicidade, candidatas=b_candidatas, passo1=b_passo1, passo3=b_passo3,
              passo4=b_passo4, atalho_testes=b_atalho_testes, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q3=b_q3, q7=b_q7, ponte=b_ponte, cta=b_cta)
