"""Visual — Números Complexos, Episódio 2: as operações (soma, produto, conjugado, divisão e igualdade) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: cx_() (complexo com a parte REAL em azul e a IMAGINÁRIA em roxo), produtos() (os quatro produtos da
distributiva saindo como setas), pedagio() (a cancela: o termo com i² passa, vira −1 e pula para a coluna da parte real),
espelho() (o conjugado como reflexo: só a parte imaginária troca de sinal), andar() (a fração em dois andares que recebe o
espelho do denominador e fica com o andar de baixo real, selo verde "andar de baixo limpo"), frutas() (maçãs e bananas).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
Na tela, parte real = azul e parte imaginária = roxo.
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
_s = importlib.util.spec_from_file_location("comum051", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_complexos_ep2_operacoes.mp4"
CARD_R = K.CARD_R
RE, IM = BLUE, PURPLE


# ======================================================================
# peças do episódio
# ======================================================================

ZB = "z̄"   # z̄: a fonte não posiciona o macron combinante; o traço é desenhado à mão


def _w(s_, peso, size):
    return ftext_w(s_.replace(ZB, "z"), peso, size)


def _ftext_zb(c, s_, x, base, size, peso, col, a):
    """ftext que desenha z̄ como 'z' com um traço por cima"""
    for k, pedaco in enumerate(s_.split(ZB)):
        if k > 0:
            wz = ftext_w("z", peso, size)
            ftext(c, "z", x, base, size, peso, col, a, align="left")
            rrect(c, x + wz * 0.08, base - size * 0.78, wz * 0.84, max(3, size * 0.07), 2, col, a)
            x += wz
        if pedaco:
            ftext(c, pedaco, x, base, size, peso, col, a, align="left")
            x += ftext_w(pedaco, peso, size)


def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços; aceita z̄)"""
    if a <= 0:
        return 0
    ws = [_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        _ftext_zb(c, s_, x, cy + size * 0.36, size, peso, col or INK, a)
        x += w_
    return sum(ws)


def cx_(re, im, par=False):
    """partes coloridas de um complexo: cx_('2', '+ 3i') → [('2', azul), (' + 3i', roxo)]"""
    p = [(re, RE), (" " + im if re else im, IM)]
    return [("(", INK)] + p + [(")", INK)] if par else p


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


def chip(c, s, cx, cy, col, a, size=46):
    """um termo num cartãozinho colorido"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 44
    rrect(c, cx - w / 2, cy - size * 0.8, w, size * 1.6, 18, mix("#FFFFFF", col, 0.16), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.8, w, size * 1.6), 18, 18),
                paint(col, a, stroke=3))
    text_mid(c, s, cx, cy, size, "black", col, a)


def colunas(c, a, y0=420, h=330):
    """as duas colunas: REAL (azul) e IMAGINÁRIA (roxo)"""
    if a <= 0:
        return
    for x, s, col in ((300, "PARTE REAL", RE), (1020, "PARTE IMAGINÁRIA", IM)):
        rrect(c, x, y0, 600, h, 24, mix("#FFFFFF", col, 0.07), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y0, 600, h), 24, 24), paint(col, a * 0.6, stroke=3))
        text(c, s, x + 300, y0 + 48, 26, "black", col, a, tracking=2)


def cancela(c, cx, cy, a, aberta=0.0, sc=1.0):
    """cancela de pedágio pequena: cabine roxa com 'i² = −1' e a barra que levanta"""
    if a <= 0:
        return
    rrect(c, cx - 70 * sc, cy - 90 * sc, 140 * sc, 120 * sc, 14, PURPLE, a, shadow=True)
    text_mid(c, "i² = −1", cx, cy - 30 * sc, 30 * sc, "black", "#FFFFFF", a)
    c.save()
    c.translate(cx + 70 * sc, cy + 10 * sc)
    c.rotate(-70 * aberta)
    rrect(c, 0, -9 * sc, 200 * sc, 18 * sc, 9, RED, a)
    for k in range(3):
        rrect(c, (26 + k * 60) * sc, -9 * sc, 26 * sc, 18 * sc, 0, "#FFFFFF", a)
    c.restore()


def frutas(c, x, y, n, tipo, a, neg=False):
    """n frutas desenhadas (maçã = círculo vermelho, banana = arco amarelo); neg = contorno tracejado (dívida)"""
    if a <= 0:
        return
    for k in range(n):
        xx = x + k * 74
        if tipo == "maca":
            c.drawCircle(xx, y, 28, paint(RED, a * (0.35 if neg else 1)))
            rrect(c, xx - 3, y - 42, 6, 16, 3, "#6B4A2B", a)
        else:
            p = skia.Path()
            p.addArc(skia.Rect.MakeXYWH(xx - 30, y - 36, 60, 60), 20, 140)
            c.drawPath(p, paint(AMBER, a * (0.35 if neg else 1), stroke=14))


def andar(c, cx, cy, num, den, a, size=70, cores_num=None, cores_den=None):
    """fração em dois andares com o traço longo: num e den são listas de partes coloridas (linha)"""
    if a <= 0:
        return
    wn = sum(ftext_w(s_, "black", size) for s_, _ in num)
    wd = sum(ftext_w(s_, "black", size) for s_, _ in den)
    w = max(wn, wd) + 40
    linha(c, num, cx, cy - size * 0.72, size, a)
    rrect(c, cx - w / 2, cy - 4, w, 8, 4, INK, a)
    linha(c, den, cx, cy + size * 0.78, size, a)
    return w


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NÚMEROS COMPLEXOS · EPISÓDIO 2", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, cx_("2", "+ 3i", True) + [("  ·  ", INK)] + cx_("1", "− i", True), 960, 300, 84, aa)
        linha(c, [("= ", INK)] + cx_("5", "+ i"), 960, 430, 84, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 420, 540, 1080, 130, 24, mix("#FFFFFF", AMBER, 0.18), ab)
        linha(c, [("esqueceu que ", INK), ("i² = −1", PURPLE), ("  →  ", INK), ("−1 + i", RED)], 960, 605, 52, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1520, 760, acc, "ALTERNATIVA ESPERANDO", RED, -5, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "COMPLEXOS · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de NÚMEROS COMPLEXOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "+   ·   ÷", "somar, multiplicar e dividir", PURPLE), ("02.b", "z  e  " + ZB, "equações com o conjugado",
                                                                              GREEN)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 660 + k * 600
        rrect(c, x - 270, 340, 540, 340, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 270, 340, 540, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        linha(c, [(tit, col)], x, 568, 60, ak)
        text(c, sb, x, 645, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "QUATRO LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = (("03.a", "episódio 1", PURPLE, [("i² = −1", PURPLE)]),
             ("03.b", "Expressões algébricas", BLUE, [("(a + b)(c + d) → 4 produtos", INK)]),
             ("03.c", "Frações", AMBER, [("× o mesmo número em cima e embaixo: ", INK), ("não muda", GREEN)]),
             ("03.d", "Sistemas lineares", GREEN, [("2 equações · 2 incógnitas", INK)]))
    for k, (cue, rot, col, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 145 + d
        cartao(c, 260, y - 58, 1400, 116, a)
        pill(c, rot, 300, y - 58, col, size=22, a=a)
        linha(c, partes, 960, y + 6, 42, a)


# ======================================================================
# concreto — frutas com frutas
# ======================================================================

def b_frutas(c, t, C, B):
    head(c, t, B["start"], "FRUTAS COM FRUTAS", "MAÇÃ COM MAÇÃ, BANANA COM BANANA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    ac = ep(t, C["04.c"], 0.5)
    if aa > 0:
        fa = aa * (1 - 0.65 * ac)
        cartao(c, 240, 210, 640, 220, fa)
        frutas(c, 300, 280, 2, "maca", fa); frutas(c, 300, 380, 3, "banana", fa)
        text(c, "2 maçãs e 3 bananas", 560, 290, 30, "black", INK, fa, align="left")
        text_mid(c, "+", 960, 320, 80, "black", INK, fa)
        cartao(c, 1040, 210, 640, 220, fa)
        frutas(c, 1100, 280, 1, "maca", fa); frutas(c, 1100, 380, 5, "banana", fa, neg=True)
        text(c, "1 maçã e −5 bananas", 1260, 290, 30, "black", INK, fa, align="left")
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        linha(c, [("3 maçãs", RED), ("   e   ", INK), ("−2 bananas", AMBER)], 960, 520, 54, ab * (1 - 0.65 * ac))
    if ac > 0:
        rrect(c, 300, 600, 1320, 130, 24, mix("#FFFFFF", PURPLE, 0.10), ac)
        linha(c, cx_("2", "+ 3i", True) + [(" + ", INK)] + cx_("1", "− 5i", True) + [("  =  ", INK)] + cx_("3", "− 2i"),
              960, 665, 60, ac)
        pill(c, "banana → i", 1500, 590, PURPLE, size=26, a=ac, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pill(c, "PARTE REAL", 760, 790, RE, size=28, a=ad, anchor="center")
        pill(c, "PARTE IMAGINÁRIA (a do i)", 1180, 790, IM, size=28, a=ad, anchor="center")


# ======================================================================
# bloco a — subtração
# ======================================================================

def b_subtracao(c, t, C, B):
    head(c, t, B["start"], "SUBTRAÇÃO", "O MENOS ENTRA NAS DUAS PARTES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        linha(c, cx_("2", "+ 3i", True) + [("  −  ", RED)] + cx_("1", "− 5i", True), 960, 270, 72, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 360, 1200, 130, 24, mix("#FFFFFF", AMBER, 0.16), ab)
        linha(c, [("2 + 3i", INK), ("  − 1  ", RE), ("+ 5i", IM)], 960, 425, 64, ab)
        pill(c, "− (− 5i) = + 5i", 1480, 360, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        linha(c, [("2 − 1 = ", INK), ("1", RE), ("      3i + 5i = ", INK), ("8i", IM)], 960, 580, 50, acc)
        rrect(c, 610, 650, 700, 120, 24, mix("#FFFFFF", GREEN, 0.16), acc)
        linha(c, [("= ", INK)] + cx_("1", "+ 8i"), 960, 710, 66, acc)


def b_atalho_soma(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "SOMA E SUBTRAÇÃO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["06"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · TROQUE OS SINAIS ANTES", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, partes) in enumerate((("06.a", [("1. subtração? troque os sinais do 2º número", INK)]),
                                       ("06.b", [("2. some: ", INK), ("real com real", RE), (" · ", INK),
                                                 ("imaginária com imaginária", IM)]))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 400 + k * 190 + d
        rrect(c, 330, y - 60, 1260, 120, 22, "#FFFFFF", ak, shadow=True)
        linha(c, partes, 380, y, 40, ak, align="left")


# ======================================================================
# bloco b — multiplicação e o pedágio do i²
# ======================================================================

PROD = [("3", RE), ("− i", IM), ("+ 6i", IM), ("− 2i²", AMBER)]
PX = [430, 770, 1150, 1490]


def produtos(c, t, a, cues, y_top=250, y=440):
    """(1 + 2i)(3 − i): as quatro setas saindo de cada termo do 1º fator para cada termo do 2º, e os produtos"""
    if a <= 0:
        return
    linha(c, cx_("1", "+ 2i", True) + [("  ·  ", INK)] + cx_("3", "− i", True), 960, y_top, 76, a)
    for k, (s_, col) in enumerate(PROD):
        ak = ep(t, cues[k], 0.5) * a
        if ak <= 0:
            continue
        x1 = 690 if k < 2 else 830
        arrow(c, x1, y_top + 50, PX[k], y - 60, col, ak, 4, 14, progress=min(1, ak * 1.4))
        chip(c, s_, PX[k], y, col, ak, 50)


def b_mult(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICAÇÃO", "TODOS COM TODOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    q = C["07.c"]
    produtos(c, t, aa, [q, q + 1.2, C["07.d"], C["07.d"] + 1.4])
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        pill(c, "trate o i como um x", 960, 600, PURPLE, size=34, a=ab, anchor="center")
        text(c, "distributiva: 2 × 2 = 4 produtos", 960, 700, 32, "bold", INK2, ab)


def b_pedagio(c, t, C, B):
    head(c, t, B["start"], "O PEDÁGIO", "TODO i² VIRA −1 E MUDA DE TIME", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    linha(c, [("3", RE), ("  − i  ", IM), ("+ 6i", IM), ("  − 2i²", AMBER)], 960, 230, 60, a0)
    colunas(c, a0, 470, 300)
    pa, pb, pc = ep(t, C["08.a"], 0.6), ep(t, C["08.b"], 1.4), ep(t, C["08.c"], 0.5)
    cancela(c, 960, 380, a0 * (1 - pc), pa)
    chip(c, "3", 480, 620, RE, a0 * (1 - pc), 52)
    chip(c, "− i", 1180, 620, IM, a0 * (1 - pc), 52)
    chip(c, "+ 6i", 1420, 620, IM, a0 * (1 - pc), 52)
    # o −2i² anda até a cancela, vira +2 e pula para a coluna real
    if pb <= 0:
        chip(c, "− 2i²", 1180, 380, AMBER, a0 * (1 - pc), 46)
        if pa > 0:
            pill(c, "−2 · (−1) = +2", 1390, 300, AMBER, size=26, a=pa, anchor="center", bounds=(0, 1920))
    else:
        u = ease(pb) if "ease" in globals() else pb
        x = 1180 + (700 - 1180) * u
        yy = 380 + (620 - 380) * u
        chip(c, "+ 2", x, yy, RE, a0 * (1 - pc), 52)
        if pb < 1:
            pill(c, "muda de time", x, yy - 70, AMBER, size=24, a=a0, anchor="center", bounds=(0, 1920))
    if pc > 0:
        chip(c, "3 + 2 = 5", 600, 620, RE, pc, 52)
        chip(c, "−i + 6i = 5i", 1320, 620, IM, pc, 52)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 640, 760, 640, 80, 20, mix("#FFFFFF", GREEN, 0.20), ad)
        linha(c, [("= ", INK)] + cx_("5", "+ 5i"), 960, 800, 52, ad)


def b_atalho_mult(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O PRODUTO DIRETO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · (a + bi)(c + di)", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa, d = rise(t, C["09.a"])
    if aa > 0:
        rrect(c, 330, 310 + d, 1260, 110, 22, "#FFFFFF", aa, shadow=True)
        linha(c, [("parte real = ", RE), ("ac − bd", INK)], 960, 365 + d, 50, aa)
    ab, d = rise(t, C["09.b"])
    if ab > 0:
        rrect(c, 330, 450 + d, 1260, 110, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("parte imaginária = ", IM), ("ad + bc", INK)], 960, 505 + d, 50, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        linha(c, [("1·3 − 2·(−1) = ", INK), ("5", RE), ("      1·(−1) + 2·3 = ", INK), ("5", IM)], 960, 650, 40, acc)
        selo(c, 1480, 730, acc, "BATEU", GREEN, -5, 34)


# ======================================================================
# bloco c — o conjugado (o espelho)
# ======================================================================

def espelho(c, cx, y1, y2, a, re="3", im1="+ 4i", im2="− 4i", size=80, prog_=1.0):
    """o número em cima, a linha do espelho e o reflexo embaixo (só a parte imaginária troca de sinal)"""
    if a <= 0:
        return
    linha(c, cx_(re, im1), cx, y1, size, a)
    ym = (y1 + y2) / 2
    line(c, cx - 360, ym, cx + 360, ym, "#9FC6E8", a, 6, dash=[18, 12])
    text(c, "espelho", cx + 420, ym + 10, 26, "bold", BLUE, a, align="left")
    if prog_ > 0:
        linha(c, cx_(re, im2), cx, y2, size, a * prog_)


def b_conjugado(c, t, C, B):
    head(c, t, B["start"], "O CONJUGADO", "O ESPELHO DO NÚMERO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    defin(c, "CONJUGADO", "de a + bi é a − bi (troca SÓ o sinal da parte imaginária)", 260, 190, 1400, aa, BLUE, 29)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        defin(c, "z BARRA", "o nome do conjugado de z: um z com um tracinho em cima (z̄)", 260, 285, 1400, ab, BLUE, 29)
    acc = ep(t, C["10.c"], 0.5)
    ad = ep(t, C["10.d"], 0.5)
    espelho(c, 640, 450, 650, acc, prog_=ep(t, C["10.c"] + 1.6, 0.6), size=72)
    if acc > 0:
        pill(c, "conjugado", 640, 760, GREEN, size=28, a=ep(t, C["10.c"] + 1.6, 0.6), anchor="center")
    if ad > 0:
        cartao(c, 1300, 470, 380, 220, ad)
        linha(c, [("−3", RE), (" − 4i", IM)], 1490, 560, 60, ad)
        pill(c, "OPOSTO: troca tudo", 1490, 650, AMBER, size=24, a=ad, anchor="center", bounds=(0, 1920))
        selo(c, 1560, 760, ad, "NÃO É O CONJUGADO", RED, -5, 26)


def b_conj_prop(c, t, C, B):
    head(c, t, B["start"], "PARA QUE SERVE O ESPELHO", "z VEZES z BARRA É REAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, cx_("3", "+ 4i", True) + [("  ·  ", INK)] + cx_("3", "− 4i", True), 960, 250, 64, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("9 ", RE), ("− 12i + 12i", IM), (" − 16i²", AMBER), ("  =  9 + 16  =  ", INK), ("25", GREEN)], 960, 360,
              46, ab)
        pill(c, "número REAL", 1500, 440, GREEN, size=28, a=ab, anchor="center", bounds=(0, 1920))
    acc, d = rise(t, C["11.c"])
    if acc > 0:
        rrect(c, 360, 480 + d, 1200, 120, 24, mix("#FFFFFF", PURPLE, 0.14), acc)
        linha(c, [("z · z̄ = ", PURPLE), ("a² + b²", INK), ("   (real, nunca negativo)", INK2)], 960, 540 + d, 44, acc)
    ad, d = rise(t, C["11.d"])
    if ad > 0:
        cartao(c, 360, 640 + d, 1200, 120, ad)
        linha(c, [("z + z̄ = ", PURPLE), ("2a", INK), ("   →   3 + 3 = 6", RE)], 960, 700 + d, 44, ad)


# ======================================================================
# bloco d — a divisão (o andar de baixo limpo)
# ======================================================================

NUM = cx_("5", "+ 5i")
DEN = cx_("3", "− i")


def b_divisao(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head(c, t, B["start"] if sid == "12" else C["13"], "DIVISÃO",
         "LIMPE O i DO ANDAR DE BAIXO" if sid == "12" else "ANDAR POR ANDAR", PURPLE)
    card(c, *CARD_R)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        andar(c, 700, 420, NUM, DEN, aa, 78)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            pill(c, "i no andar de baixo", 700, 600, AMBER, size=30, a=ab, anchor="center")
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            text_mid(c, "×", 1020, 420, 70, "black", INK, acc)
            andar(c, 1260, 420, cx_("3", "+ i"), cx_("3", "+ i"), acc, 78)
            pill(c, "o ESPELHO do denominador", 1260, 600, GREEN, size=28, a=acc, anchor="center")
            text(c, "mesmo número em cima e embaixo: a fração não muda", 960, 740, 30, "bold", INK2,
                 ep(t, C["12.c"] + 2.5, 0.5))
        return
    # cena 13: as contas
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        pill(c, "EM CIMA", 300, 240, PURPLE, size=24, a=aa)
        linha(c, cx_("5", "+ 5i", True) + cx_("3", "+ i", True) + [("  =  15 + 5i + 15i + ", INK), ("5i²", AMBER)],
              960, 300, 46, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        cancela(c, 1600, 470, ab, ep(t, C["13.b"] + 0.6, 0.6), 0.8)
        linha(c, [("5i² = −5", AMBER), ("   →   ", INK)] + cx_("10", "+ 20i"), 1010, 400, 50, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        pill(c, "EMBAIXO", 300, 500, PURPLE, size=24, a=acc)
        linha(c, [("(3 − i)(3 + i)  =  9 + 1  =  ", INK), ("10", RE)], 960, 560, 46, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        selo(c, 1520, 600, ad, "ANDAR DE BAIXO LIMPO", GREEN, -5, 30)
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        andar(c, 720, 710, cx_("10", "+ 20i"), [("10", RE)], ae, 50)
        linha(c, [("=  ", INK)] + cx_("1", "+ 2i"), 1130, 710, 66, ae)


def b_divisao_conf(c, t, C, B):
    head(c, t, B["start"], "CONFIRA", "MULTIPLIQUE DE VOLTA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, cx_("1", "+ 2i", True) + [("  ·  ", INK)] + cx_("3", "− i", True), 960, 330, 76, aa)
        text(c, "resultado × denominador", 960, 440, 32, "bold", INK2, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 520, 800, 140, 26, mix("#FFFFFF", GREEN, 0.18), ab)
        linha(c, [("= ", INK)] + cx_("5", "+ 5i"), 960, 590, 80, ab)
        selo(c, 1500, 720, ab, "O NÚMERO DO COMEÇO", GREEN, -5, 30)


def b_atalho_div(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O ANDAR DE BAIXO DIRETO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · DIVISÃO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa, d = rise(t, C["15.a"])
    if aa > 0:
        rrect(c, 330, 330 + d, 1260, 130, 22, "#FFFFFF", aa, shadow=True)
        linha(c, [("(a − bi)(a + bi) = ", INK), ("a² + b²", GREEN), ("      3² + 1² = 10", RE)], 960, 395 + d, 44, aa)
    ab, d = rise(t, C["15.b"])
    if ab > 0:
        rrect(c, 330, 520 + d, 1260, 130, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("no fim: ", INK), ("resultado × denominador", GREEN), (" = número de cima", INK)], 960, 585 + d, 42, ab)


# ======================================================================
# bloco e — igualdade · bloco f — equações com z e z̄
# ======================================================================

def b_igualdade(c, t, C, B):
    head(c, t, B["start"], "IGUALDADE", "UMA EQUAÇÃO VALE POR DUAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    defin(c, "IGUALDADE", "a + bi = c + di  só se  a = c  e  b = d", 260, 200, 1400, aa, BLUE, 32)
    if aa > 0:
        linha(c, [("a", RE), (" + ", INK), ("b", IM), ("i  =  ", INK), ("c", RE), (" + ", INK), ("d", IM), ("i", INK)], 960,
              380, 80, aa)
        arrow(c, 820, 440, 760, 520, RE, ep(t, C["16.a"] + 2.0, 0.5), 4, 14)
        arrow(c, 1100, 440, 1160, 520, IM, ep(t, C["16.a"] + 2.0, 0.5), 4, 14)
        linha(c, [("a = c", RE)], 720, 570, 54, ep(t, C["16.a"] + 2.0, 0.5))
        linha(c, [("b = d", IM)], 1200, 570, 54, ep(t, C["16.a"] + 2.0, 0.5))
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        pill(c, "1 equação complexa = 2 equações reais", 960, 660, PURPLE, size=32, a=ab, anchor="center")
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        defin(c, "IMAGINÁRIO PURO", "parte real zero e imaginária não nula (ex.: 5i)", 260, 730, 1400, acc, BLUE, 29)


def b_igualdade_ex(c, t, C, B):
    head(c, t, B["start"], "REAL OU IMAGINÁRIO PURO?", "IGUALE AS PARTES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        linha(c, [("(a + 2i)(1 + i)  =  ", INK), ("(a − 2)", RE), (" + ", INK), ("(a + 2)i", IM)], 960, 270, 56, aa)
        text(c, "Exemplo do material (seção 05)", 190, 822, 18, "medium", GRAY, aa, align="left")
    for k, (cue, tit, conta, res, col) in enumerate((("17.b", "REAL", "a + 2 = 0", "a = −2", IM),
                                                     ("17.c", "IMAGINÁRIO PURO", "a − 2 = 0", "a = 2", RE))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 300 + k * 700
        cartao(c, x, 380 + d, 620, 360, ak)
        text(c, tit, x + 310, 450 + d, 38, "black", INK, ak)
        text(c, "some a parte " + ("imaginária" if k == 0 else "real"), x + 310, 510 + d, 28, "bold", col, ak)
        expr(c, conta, x + 310, 590 + d, 54, ak)
        chip(c, res, x + 310, 680 + d, GREEN, ak, 50)


def b_eq_z(c, t, C, B):
    head(c, t, B["start"], "EQUAÇÕES COM z E z BARRA", "TROQUE z POR a + bi", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        linha(c, [("z + 2z̄  =  ", INK)] + cx_("6", "+ i"), 960, 250, 66, aa)
        text(c, "Exemplo nosso", 190, 822, 18, "medium", GRAY, aa, align="left")
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        for x_, s_ in ((760, "z = a + bi"), (1160, ZB + " = a − bi")):
            rrect(c, x_ - 150, 318, 300, 64, 32, PURPLE, ab)
            linha(c, [(s_, "#FFFFFF")], x_, 350, 34, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        linha(c, [("a + bi + 2a − 2bi  =  ", INK), ("3a", RE), (" − bi", IM)], 960, 450, 52, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        cartao(c, 360, 520, 560, 140, ad)
        linha(c, [("3a = 6  →  ", INK), ("a = 2", RE)], 640, 590, 46, ad)
        cartao(c, 1000, 520, 560, 140, ad)
        linha(c, [("−b = 1  →  ", INK), ("b = −1", IM)], 1280, 590, 46, ad)
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        rrect(c, 660, 690, 600, 110, 24, mix("#FFFFFF", GREEN, 0.18), ae)
        linha(c, [("z = ", INK)] + cx_("2", "− i"), 960, 745, 62, ae)


def b_atalho_eq(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "UMA EQUAÇÃO VIRA DUAS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["19"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · z E z BARRA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, partes) in enumerate((("19.a", [("1. z → a + bi   ·   z̄ → a − bi", INK)]),
                                       ("19.b", [("2. separe: ", INK), ("real = real", RE), ("  ·  ", INK),
                                                 ("imaginária = imaginária", IM)]),
                                       ("19.c", [("3. confira: (2 − i) + 2(2 + i) = 6 + i", GREEN)]))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 360 + k * 150 + d
        rrect(c, 330, y - 55, 1260, 110, 22, "#FFFFFF", ak, shadow=True)
        linha(c, partes, 380, y, 38, ak, align="left")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("20", "SUA VEZ", "PAUSE E TENTE", GREEN), ("21", "VAMOS JUNTOS", "PRODUTO E CONJUGADO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["20.a"], 0.5)
    linha(c, [("1)  ", INK)] + cx_("4", "− i", True) + [("  ·  ", INK)] + cx_("2", "+ 3i", True), 960, 240, 60, aa)
    ab = ep(t, C["20.b"], 0.5)
    linha(c, [("2)  conjugado de  ", INK)] + cx_("−2", "+ 5i"), 960, 340, 54, ab)
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 1.9, 960, 580)
        return
    a1 = ep(t, C["21.a"], 0.5)
    if a1 > 0:
        for k, (s_, col) in enumerate((("8", RE), ("+ 12i", IM), ("− 2i", IM), ("− 3i²", AMBER))):
            chip(c, s_, 470 + k * 330, 470, col, ep(t, C["21.a"] + 0.9 * k, 0.4), 46)
    ab2 = ep(t, C["21.b"], 0.5)
    if ab2 > 0:
        pill(c, "−3i² = +3", 1460, 400, AMBER, size=26, a=ab2, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["21.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 560, 560, 110, 22, mix("#FFFFFF", GREEN, 0.18), acc)
        linha(c, cx_("11", "+ 10i"), 640, 615, 56, acc)
    ad = ep(t, C["21.d"], 0.5)
    if ad > 0:
        rrect(c, 1000, 560, 560, 110, 22, mix("#FFFFFF", GREEN, 0.18), ad)
        linha(c, cx_("−2", "− 5i"), 1280, 615, 56, ad)
        pill(c, "o real fica · o imaginário troca", 1280, 720, BLUE, size=24, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Trate i como letra e troque i² por −1 no fim.",
          "Conjugado: só a parte imaginária troca de sinal.",
          "Na divisão, multiplique em cima e embaixo pelo conjugado do denominador."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "35"])
    frame(c, t, B["start"] if sid == "22" else C["35"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 62)


ERROS = [("(2 + 3i)(1 − i) = 2 − 3i  (só real com real e imaginária com imaginária)",
          "na SOMA é assim: real com real, imaginária com imaginária",
          "no produto são 4 contas + o pedágio do i²: 5 + i."),
         ("(5 + 5i) ÷ (3 − i) = 5/3 + 5i/(−i)  (parte por parte)",
          "com denominador real funciona: (6 + 4i) ÷ 2 = 3 + 2i",
          "com i embaixo, limpe o andar de baixo primeiro: 1 + 2i."),
         ("conjugado de 3 + 4i = −3 − 4i",
          "\"conjugar\" soa como inverter tudo",
          "esse é o OPOSTO. O espelho troca só a parte imaginária: 3 − 4i.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# questões 2 (eu faço), 3 (nós fazemos) e 9 (você faz)
# ======================================================================

ALTS2 = [("A", "= 5 + i", "", GREEN), ("B", "= −1 + i", "usou i² = 1", RED), ("C", "= 2 − 3i", "só correspondentes", RED),
         ("D", "= 5 − i", "sinal dos termos em i", RED), ("E", "= 3 + 2i", "é a soma z + w", RED)]


def b_q2(c, t, C, B):
    sid = which(t, C, ["26", "27", "28"])
    heads = {"26": "O PRODUTO z · w", "27": "EU FAÇO", "28": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "26" else C[sid], "QUESTÃO 2 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS2, 1250, 240, 440, 38, C["27.ok"], "A", cues_in, cues_x, gap=30)
    a0 = ep(t, C["26.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        text(c, "circuitos:", 660, 250, 30, "bold", INK2, a0)
        linha(c, [("z = ", INK)] + cx_("2", "+ 3i") + [("     w = ", INK)] + cx_("1", "− i"), 660, 320, 44, a0)
        text(c, "z · w = ?", 660, 400, 40, "black", INK, a0)
    if sid == "26":
        return
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        linha(c, [("2", RE), (" − 2i + 3i", IM), (" − 3i²", AMBER)], 660, 490, 46, aa)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        pill(c, "−3i² = +3  →  parte real", 660, 570, AMBER, size=28, a=ab, anchor="center")
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        linha(c, [("real: 2 + 3 = ", INK), ("5", RE), ("    imag.: ", INK), ("i", IM)], 660, 650, 38, acc)
    ad = ep(t, C["27.d"], 0.5) * (1 - ep(t, C["28"], 0.4))
    if ad > 0:
        rrect(c, 460, 700, 400, 90, 18, mix("#FFFFFF", GREEN, 0.20), ad)
        linha(c, cx_("5", "+ i"), 660, 745, 52, ad)


ALTS3 = [("A", "= 2 + 4i", "esqueceu o ÷ 2", RED), ("B", "= 3 − i", "parte por parte", RED),
         ("C", "= 2 + i", "trocou as partes", RED), ("D", "= 1 + 4i", "÷ 2 só na real", RED), ("E", "= 1 + 2i", "", GREEN)]


def b_q3(c, t, C, B):
    sid = which(t, C, ["29", "30", "31"])
    heads = {"29": "DIVISÃO PELO CONJUGADO", "30": "NÓS FAZEMOS", "31": "AS ERRADAS"}
    head(c, t, B["start"] if sid == "29" else C[sid], "QUESTÃO 3 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS3, 1250, 240, 440, 38, C["30.ok"], "E", cues_in, cues_x, gap=30)
    a0 = ep(t, C["29.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        andar(c, 560, 320, cx_("3", "+ i"), cx_("1", "− i"), a0, 56)
        text(c, "= a + bi ?", 860, 340, 40, "black", INK2, a0, align="left")
    if sid == "29":
        ap = ep(t, C["29.p"], 0.5)
        if ap > 0:
            pill(c, "qual é o ESPELHO do denominador?", 660, 520, GREEN, size=30, a=ap, anchor="center")
        return
    a1 = ep(t, C["30"], 0.4)
    if a1 > 0:
        pill(c, "× (1 + i) em cima e embaixo", 660, 460, GREEN, size=28, a=a1, anchor="center")
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        linha(c, [("cima: 3 + 3i + i + i²  =  ", INK)] + cx_("2", "+ 4i"), 660, 540, 34, aa)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        linha(c, [("baixo: 1 + 1  =  ", INK), ("2", RE)], 660, 600, 34, ab)
    acc = ep(t, C["30.c"], 0.5) * (1 - ep(t, C["31"], 0.4))
    if acc > 0:
        rrect(c, 430, 640, 460, 80, 18, mix("#FFFFFF", GREEN, 0.20), acc)
        linha(c, [("÷ 2  →  ", INK)] + cx_("1", "+ 2i"), 660, 680, 44, acc)
    ad = ep(t, C["30.d"], 0.5) * (1 - ep(t, C["31"], 0.4))
    if ad > 0:
        pill(c, "confere: (1 + 2i)(1 − i) = 3 + i", 660, 760, GREEN, size=24, a=ad, anchor="center")


ALTS9 = [("A", "= 2 + 2i", "sinal de b", RED), ("B", "= 2 − {2/3}i", "tratou z barra como z", RED),
         ("C", "= 6 − {2/3}i", "conjugado −a + bi", RED), ("D", "= 3 − 2i", "só o 2z na real", RED),
         ("E", "= 2 − 2i", "", GREEN)]


def b_q9(c, t, C, B):
    sid = which(t, C, ["32", "33", "34"])
    heads = {"32": "VOCÊ FAZ", "33": "VAMOS CONFERIR", "34": "AS ERRADAS"}
    head(c, t, B["start"] if sid == "32" else C[sid], "QUESTÃO 9 · ESTILO ENEM", heads[sid], GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS9, 1250, 240, 440, 36, C["33.ok"], "E", cues_in, cues_x, gap=26)
    a0 = ep(t, C["32.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        linha(c, [(ZB + " = conjugado de z", INK2)], 660, 240, 30, a0, peso="bold")
        linha(c, [("2z + z̄  =  ", INK)] + cx_("6", "− 2i"), 660, 330, 56, a0)
        text(c, "z = ?", 660, 420, 40, "black", INK, a0)
    if sid == "32":
        pause_timer(c, t, C["32.end"] - 1.9, 660, 620)
        return
    aa = ep(t, C["33.a"], 0.5)
    if aa > 0:
        linha(c, [("z = a + bi    z̄ = a − bi", PURPLE)], 660, 500, 34, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        linha(c, [("2a + 2bi + a − bi  =  ", INK), ("3a", RE), (" + bi", IM)], 660, 565, 34, ab)
    acc = ep(t, C["33.c"], 0.5)
    if acc > 0:
        linha(c, [("3a = 6 → ", INK), ("a = 2", RE), ("    b = −2", IM)], 660, 630, 36, acc)
    ad = ep(t, C["33.d"], 0.5) * (1 - ep(t, C["34"], 0.4))
    if ad > 0:
        rrect(c, 430, 670, 460, 80, 18, mix("#FFFFFF", GREEN, 0.20), ad)
        linha(c, [("z = ", INK)] + cx_("2", "− 2i"), 660, 710, 44, ad)
    ae = ep(t, C["33.e"], 0.5) * (1 - ep(t, C["34"], 0.4))
    if ae > 0:
        pill(c, "confere: 4 − 4i + 2 + 2i = 6 − 2i", 660, 785, GREEN, size=24, a=ae, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O PLANO DE ARGAND-GAUSS", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    if aa > 0:
        ox, oy, u = 620, 720, 90
        line(c, ox - 80, oy, ox + 5 * u, oy, INK2, aa, 3)
        line(c, ox, oy + 60, ox, oy - 5 * u, INK2, aa, 3)
        text(c, "real", ox + 5 * u + 30, oy + 10, 24, "bold", RE, aa, align="left")
        text(c, "imaginário", ox + 10, oy - 5 * u - 20, 24, "bold", IM, aa, align="left")
        c.drawCircle(ox + 3 * u, oy - 4 * u, 14, paint(PURPLE, aa))
        linha(c, cx_("3", "+ 4i"), ox + 3 * u + 110, oy - 4 * u - 10, 40, aa)
    ab = ep(t, C["36.b"], 0.5)
    if ab > 0:
        line(c, 620, 720, 620 + 270, 720 - 360, AMBER, ab, 5, dash=[14, 10])
        pill(c, "distância = ?", 1340, 360, AMBER, size=34, a=ab, anchor="center")
    acc = ep(t, C["36.c"], 0.5)
    if acc > 0:
        pill(c, "× i  →  ?", 1340, 480, PURPLE, size=40, a=acc, anchor="center")
    ad = ep(t, C["36.d"], 0.5)
    if ad > 0:
        selo(c, 1340, 650, ad, "PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"],
        "Você já tinha caído no pedágio do i²?", canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, frutas=b_frutas, subtracao=b_subtracao,
              atalho_soma=b_atalho_soma, mult=b_mult, pedagio=b_pedagio, atalho_mult=b_atalho_mult,
              conjugado=b_conjugado, conj_prop=b_conj_prop, divisao=b_divisao, divisao_conf=b_divisao_conf,
              atalho_div=b_atalho_div, igualdade=b_igualdade, igualdade_ex=b_igualdade_ex, eq_z=b_eq_z,
              atalho_eq=b_atalho_eq, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q3=b_q3, q9=b_q9,
              ponte=b_ponte, cta=b_cta)
