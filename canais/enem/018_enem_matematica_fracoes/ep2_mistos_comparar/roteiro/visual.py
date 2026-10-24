"""Visual — Frações, Decimais e Dízimas, Episódio 2: Números mistos e qual fração é maior (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, expr com frações empilhadas e mistos "2|3/4", reta, alternativas, erro_cards...).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w, pizza = K.fr, K.expr, K.expr_w, K.pizza
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep2_mistos_comparar.mp4"
CARD_R = K.CARD_R
FARINHA = "#F1E7CF"


def xicara(c, x, y, cheio, a, w=120, h=150):
    """xícara de medida (x, y = canto superior esquerdo); cheio = 0..1"""
    if a <= 0:
        return
    c.drawCircle(x + w + 4, y + h * 0.45, 30, paint(INK2, a, stroke=8))
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    if cheio > 0:
        hh = (h - 16) * cheio
        rrect(c, x + 8, y + h - 8 - hh, w - 16, hh, 12, FARINHA, a)
        if cheio < 1:
            line(c, x + 8, y + h - 8 - hh, x + w - 8, y + h - 8 - hh, "#C9A86A", a, 3)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK2, a, stroke=5))


def fatia(c, cx, cy, r, j, a, col=None):
    """uma fatia de quarto solta (j = posição 0..3 na pizza, a partir do topo)"""
    if a <= 0:
        return
    a0 = -90 + j * 90
    c.drawPath(K._wedge(cx, cy, r, a0, a0 + 90), paint("#D9A55B", a))
    c.drawPath(K._wedge(cx, cy, r * 0.88, a0, a0 + 90), paint(col or K.MOLHO, a))


def misto(c, inteiro, num, den, cx, cy, size, a, cols=(INK, INK, INK)):
    """número misto grande com cores separadas (inteiro, numerador, denominador); devolve as posições (xi, xf)"""
    wi = ftext_w_(inteiro, size * 1.15)
    wf = K.fr_w(num, den, size * 0.8)
    x0 = cx - (wi + 10 + wf) / 2
    xi, xf = x0 + wi / 2, x0 + wi + 10 + wf / 2
    fmid(c, inteiro, xi, cy, size * 1.15, "black", cols[0], a)
    fr(c, num, den, xf, cy - size * 0.38, size * 0.8, INK, a, num_col=cols[1], den_col=cols[2])
    return xi, xf


def ftext_w_(s, size):
    return K.ftext_w(s, "black", size)


def tipos_chips(c, t, C, ativo):
    """a fileira dos 4 tipos, acumulando ao longo do bloco"""
    itens = [("04", "PRÓPRIA  < 1"), ("05", "IMPRÓPRIA  > 1"), ("06", "APARENTE  = inteiro"), ("07", "MISTA  = inteiro + fração")]
    for k, (sid, lab) in enumerate(itens):
        a = ep(t, C[f"{sid}.c"] if sid != "07" else C["07.a"], 0.4)
        if a <= 0:
            continue
        x = 330 + k * 420
        chip(c, lab, x, 780, BLUE if sid == ativo else GRAY, a, 26, fill=sid == ativo, w=380)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MISTOS E QUAL É MAIOR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ac = ep(t, C["01.c"], 0.5)
    fr(c, "3", "7", 640, 380, 140, mix(INK, AMBER, ep(t, C["01.b"], 0.4) * (1 - ac)), aa)
    fmid(c, "ou", W / 2, 380, 60, "black", GRAY, aa)
    fr(c, "3", "5", 1280, 380, 140, mix(INK, GREEN, ac), aa)
    ab = ep(t, C["01.b"], 0.5)
    pill(c, "“porque 7 é maior que 5”", 640, 560, AMBER, size=30, a=ab * (1 - ac), anchor="center", bounds=(0, 1920))
    if ac > 0:
        strike(c, 560, 380, 720, 380, ac, RED, ac)
        check_icon(c, 1430, 300, 34, ac, GREEN)
        selo(c, W / 2, 595, ac, "É EXATAMENTE O CONTRÁRIO", RED, -4, 34)
    ad = ep(t, C["01.d"], 0.5)
    pizza(c, 640, 730, 80, 7, 3, ad, pull=0.5)
    pizza(c, 1280, 730, 80, 5, 3, ad, pull=0.5)
    text(c, "com uma pizza", W / 2, 744, 34, "black", INK2, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "operar com NÚMEROS MISTOS sem errar"), ("02.b", "colocar qualquer lista de frações EM ORDEM")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
    a, d = rise(t, C["02.a"] + 0.6)
    expr(c, "2|3/4 = 11/4", 560, 400 + d, 56, a, cores={2: PURPLE})
    a, d = rise(t, C["02.b"] + 0.6)
    expr(c, "3/5 < 5/8 < 7/11", 620, 600 + d, 56, a, cores={1: GREEN, 3: GREEN})
    pill(c, "cada palavra nova, explicada", 1380, 760, BLUE, size=32, a=ep(t, C["02.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pizza(c, 380, 430, 150, 4, 3, aa, pull=0.4)
        fr(c, "3", "4", 700, 430, 100, INK, aa, num_col="#C9532A", den_col=BLUE)
        text(c, "quantas você pegou", 780, 375, 28, "black", "#C9532A", aa, align="left")
        text(c, "em quantas fatias", 780, 505, 28, "black", BLUE, aa, align="left")
        text(c, "EPISÓDIO 1", 540, 680, 26, "black", GRAY, aa, tracking=2)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        line(c, 1100, 220, 1100, 780, LINE, ab, 3)
        # 11 bolinhas: dois grupos de 4 e sobram 3
        g = ep(t, C["03.c"], 0.6)
        for i in range(11):
            grupo, k = divmod(i, 4)
            x0, y0 = 1180 + (i % 6) * 70, 290 + (i // 6) * 70
            x1, y1 = 1190 + grupo * 170 + (k % 2) * 60, 270 + (k // 2) * 60
            col = AMBER if grupo == 2 and g > 0.5 else BLUE
            c.drawCircle(lerp(x0, x1, g), lerp(y0, y1, g), 22, paint(col, ab))
        if g > 0:
            for grupo in range(2):
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1150 + grupo * 170, 230, 140, 140), 20, 20),
                            paint(BLUE, g, stroke=4))
        expr(c, "11 ÷ 4 = 2", 1440, 480, 60, ab, cores={4: BLUE})
        expr(c, "2 · 4 = 8 , sobram 3", 1440, 580, 44, ep(t, C["03.c"], 0.5), cores={6: AMBER})
        pill(c, "RESTO = o que sobra da divisão", 1440, 690, BLUE, size=30, a=ep(t, C["03.d"], 0.5), anchor="center",
             bounds=(0, 1920))


# ======================================================================
# bloco A — os quatro tipos
# ======================================================================

def b_tipos(c, t, C, B):
    head_seq(c, t, C, [("04", "MAIS OU MENOS QUE 1?", "FRAÇÃO PRÓPRIA", BLUE), ("05", "7 FATIAS DE UMA PIZZA DE 4?", "FRAÇÃO IMPRÓPRIA", BLUE),
                       ("06", "UM INTEIRO DISFARÇADO", "FRAÇÃO APARENTE", BLUE), ("07", "INTEIRO + PEDAÇO", "NÚMERO MISTO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06", "07"])
    tipos_chips(c, t, C, sid)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "04":
        a0 = ep(t, q("t"), 0.5)
        for k, ch in enumerate((1, 1, 0.75)):
            xicara(c, 230 + k * 190, 300, ch * ep(t, q("t") + 0.4 + 0.4 * k, 0.6), a0 * ep(t, q("t") + 0.3 * k, 0.3))
        text(c, "2 xícaras e 3/4", 430, 540, 38, "black", INK, a0)
        aa = ep(t, q("a"), 0.4)
        pill(c, "MAIS que 1 xícara", 430, 595, GREEN, size=30, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, q("b"), 0.5)
        if ab > 0:
            line(c, 820, 230, 820, 680, LINE, ab, 3)
            pizza(c, 1080, 420, 150, 4, 3, ab, pull=0.4)
            fr(c, "3", "4", 1420, 420, 110, INK, ab, num_col=mix(INK, BLUE, ep(t, q("b") + 1.0, 0.4)))
            text(c, "3 < 4", 1420, 620, 40, "black", BLUE, ep(t, q("b") + 1.0, 0.4))
        regra(c, "PRÓPRIA: numerador menor · vale menos que 1", W / 2, 680, ep(t, q("c"), 0.5), 32, BLUE)
    elif sid == "05":
        a0 = ep(t, q("t"), 0.5)
        fr(c, "7", "4", 1450, 420, 120, INK, a0, num_col=mix(INK, BLUE, ep(t, q("a"), 0.4)))
        text(c, "7 > 4", 1450, 640, 40, "black", BLUE, ep(t, q("a"), 0.4))
        ab = ep(t, q("b"), 0.5)
        pizza(c, 420, 420, 150, 4, 4, a0)
        pizza(c, 820, 420, 150, 4, 3, ab, gone={3})
        text(c, "4 fatias", 420, 630, 30, "bold", INK2, a0)
        text(c, "+ 3 de outra pizza", 820, 630, 30, "bold", INK2, ab)
        regra(c, "IMPRÓPRIA: numerador maior · vale mais que 1", W / 2, 690, ep(t, q("c"), 0.5), 32, BLUE)
    elif sid == "06":
        a0 = ep(t, q("t"), 0.5)
        fr(c, "8", "4", 1250, 420, 120, INK, a0)
        aa = ep(t, q("a"), 0.5)
        pizza(c, 380, 420, 140, 4, 4, aa)
        pizza(c, 740, 420, 140, 4, 4, ep(t, q("a") + 0.5, 0.5))
        fmid(c, "= 2", 1450, 420, 90, "black", GREEN, ep(t, q("a") + 1.2, 0.5))
        text(c, "duas pizzas inteiras", 560, 620, 32, "bold", INK2, aa)
        text(c, "8 está na tabuada do 4:  4 · 2 = 8", 1350, 620, 30, "black", INK2, ep(t, q("c"), 0.5))
        regra(c, "APARENTE: um inteiro disfarçado", W / 2, 690, ep(t, q("b"), 0.5), 32, BLUE)
    else:
        a0 = ep(t, q("t"), 0.5)
        for k, (n, s_) in enumerate(((4, 4), (4, 4), (4, 3))):
            pizza(c, 330 + k * 270, 400, 110, n, s_, a0 * ep(t, q("t") + 0.3 * k, 0.3), gone={3} if k == 2 else None)
        aa, ab = ep(t, q("a"), 0.5), ep(t, q("b"), 0.5)
        misto(c, "2", "3", "4", 1380, 420, 150, max(aa, a0 * 0.4), (mix(INK, PURPLE, aa), mix(INK, BLUE, ab), mix(INK, BLUE, ab)))
        text(c, "parte inteira", 1250, 620, 28, "black", PURPLE, aa)
        text(c, "parte fracionária", 1520, 620, 28, "black", BLUE, ab)
        text(c, "dois inteiros e três quartos", W / 2, 700, 40, "black", INK, ep(t, q("c"), 0.5))


# ======================================================================
# bloco B — misto → impróprio
# ======================================================================

def b_mista(c, t, C, B):
    head_seq(c, t, C, [("08", "2 3/4 SÃO QUANTOS QUARTOS?", "CONTANDO TUDO EM FATIAS", PURPLE),
                       ("09", "A REGRA", "MISTO → IMPRÓPRIO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        a0 = ep(t, C["08.t"], 0.5)
        misto(c, "2", "3", "4", 1460, 300, 90, a0)
        fmid(c, "= ?", 1460, 420, 60, "black", AMBER, a0 * (1 - ep(t, C["08.e"], 0.4)))
        aa = ep(t, C["08.a"], 0.5)
        cut = ep(t, C["08.b"], 0.8)
        for k in range(3):
            pizza(c, 300 + k * 300, 400, 130, 4, 4 if k < 2 else 3, aa * ep(t, C["08.a"] + 0.3 * k, 0.3),
                  cut=cut if k < 2 else 1, gone={3} if k == 2 else None)
        ac = ep(t, C["08.c"], 0.5)
        text(c, "4", 300, 600, 44, "black", PURPLE, ac)
        text(c, "+ 4", 600, 600, 44, "black", PURPLE, ac)
        text(c, "= 8", 450, 670, 44, "black", PURPLE, ep(t, C["08.c"] + 0.8, 0.4))
        ad = ep(t, C["08.d"], 0.5)
        text(c, "+ 3", 900, 600, 44, "black", AMBER, ad)
        text(c, "11 fatias de quarto", 600, 770, 40, "black", INK, ep(t, C["08.d"] + 0.8, 0.4))
        ae = ep(t, C["08.e"], 0.5)
        fmid(c, "=", 1460, 430, 60, "black", GREEN, ae)
        fr(c, "11", "4", 1460, 560, 110, GREEN, ae)
        return
    aa = ep(t, C["09.a"], 0.5)
    regra(c, "inteiro × denominador + numerador", W / 2, 240, aa, 38)
    text(c, "o denominador continua o mesmo", W / 2, 330, 30, "bold", INK2, ep(t, C["09.a"] + 1.4, 0.4))
    ab = ep(t, C["09.b"], 0.5)
    expr(c, "2 · 4 = 8", 480, 450, 56, ab)
    expr(c, "8 + 3 = 11", 480, 560, 56, ep(t, C["09.b"] + 1.2, 0.4))
    expr(c, "2|3/4 = 11/4", 480, 690, 60, ep(t, C["09.b"] + 2.2, 0.4), cores={2: GREEN})
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        boxed(c, 900, 390, 760, 420, GREEN, ac, 0.06)
        text(c, "ATALHO · A VOLTA DA FERRADURA", 1280, 440, 26, "black", GREEN, ac, tracking=2)
        xi, xf = misto(c, "2", "3", "4", 1280, 640, 140, ac)
        ad = ep(t, C["09.d"], 0.6)
        if ad > 0:
            yd, yi, yn = 760, 640, 520
            arrow(c, xf - 10, yd, xi + 30, yi + 70, GREEN, ad, 6, 18, progress=clamp(ad * 2))
            fmid(c, "×", xi - 75, 700, 48, "black", GREEN, clamp(ad * 2))
            arrow(c, xi + 30, yi - 80, xf - 30, yn + 10, GREEN, ad, 6, 18, progress=clamp(ad * 2 - 1))
            fmid(c, "+", xi - 75, 560, 52, "black", GREEN, clamp(ad * 2 - 1))
            text(c, "começa embaixo · multiplica · sobe somando", 1280, 790, 24, "black", GREEN, ad)


# ======================================================================
# bloco C — impróprio → misto
# ======================================================================

def b_impropria(c, t, C, B):
    frame(c, t, B["start"], "O CAMINHO DE VOLTA", "IMPRÓPRIO → MISTO", PURPLE)
    a0 = ep(t, C["10.t"], 0.5)
    fr(c, "11", "4", 1400, 300, 80, INK, a0 * (1 - ep(t, C["10.c"], 0.4)))
    aa = ep(t, C["10.a"], 0.5)
    g = ep(t, C["10.a"] + 0.6, 1.4)
    for i in range(11):
        grupo, j = divmod(i, 4)
        x0, y0 = 220 + i * 80, 300
        x1, y1 = 300 + grupo * 300, 420
        r = lerp(50, 120, g)
        col = AMBER if grupo == 2 and t > C["10.b"] else K.MOLHO
        fatia(c, lerp(x0, x1, g), lerp(y0, y1, g), r, j, aa * ep(t, C["10.a"] + 0.06 * i, 0.3), col)
    ab = ep(t, C["10.b"], 0.5)
    text(c, "1 pizza", 300, 610, 32, "black", BLUE, ab)
    text(c, "2 pizzas", 600, 610, 32, "black", BLUE, ab)
    text(c, "sobram 3", 900, 610, 32, "black", AMBER, ab)
    ac = ep(t, C["10.c"], 0.5)
    expr(c, "11 ÷ 4 = 2 , resto 3", 1400, 290, 52, ac, cores={4: BLUE, 7: AMBER})
    ad, ae, af = ep(t, C["10.d"], 0.5), ep(t, C["10.e"], 0.5), ep(t, C["10.f"], 0.5)
    pill(c, "QUOCIENTE (resultado da divisão) → inteiro", 1400, 370, BLUE, size=26, a=ad, anchor="center", bounds=(0, 1920))
    pill(c, "RESTO → numerador", 1400, 435, AMBER, size=26, a=ae, anchor="center", bounds=(0, 1920))
    misto(c, "2", "3", "4", 1400, 680, 130, max(ad, ae) * 0.999,
          (mix(INK, BLUE, ad), mix(INK, AMBER, ae), mix(INK, GREEN, af)))
    pill(c, "ATALHO: o denominador nunca muda", 600, 720, GREEN, size=30, a=af, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco D — a regra de ouro
# ======================================================================

def b_ouro(c, t, C, B):
    frame(c, t, B["start"], "A REGRA DE OURO", "NUNCA OPERE COM O MISTO", PURPLE)
    regra(c, "converta para imprópria ANTES de qualquer conta", W / 2, 240, ep(t, C["11.t"], 0.5), 36)
    passos = [("11.a", "1. converta para imprópria"), ("11.b", "2. faça a conta"), ("11.c", "3. volte para misto (se pedir)")]
    for k, (cue, s) in enumerate(passos):
        a = ep(t, C[cue], 0.5)
        x = 400 + k * 560
        chip(c, s, x, 380, PURPLE, a, 30, w=470)
        if k:
            arrow(c, x - 300, 380, x - 250, 380, LIGHT, a, 5, 14)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        boxed(c, 220, 480, 700, 300, GREEN, ad, 0.06)
        text(c, "NA SOMA: até funciona", 570, 530, 30, "black", GREEN, ad)
        expr(c, "1|1/4 + 2|1/4 = 3|2/4", 570, 650, 48, ad)
        check_icon(c, 570, 740, 22, ad, GREEN)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        boxed(c, 1000, 480, 700, 300, RED, ae, 0.06)
        text(c, "NA × E NA ÷: quebra feio", 1350, 530, 30, "black", RED, ae)
        expr(c, "2|3/4 · 3 ≠ 6|3/4", 1350, 650, 48, ae, cores={3: RED})
        check_icon(c, 1350, 740, 22, ae, RED, "x")


# ======================================================================
# blocos E e F — mesmo denominador / mesmo numerador
# ======================================================================

def b_mesmo_den(c, t, C, B):
    frame(c, t, B["start"], "5/7 OU 3/7?", "MESMO DENOMINADOR", PURPLE)
    aa = ep(t, C["12.a"], 0.5)
    pizza(c, 560, 400, 160, 7, 5, max(aa, ep(t, C["12.t"], 0.5)), pull=0.4)
    pizza(c, 1360, 400, 160, 7, 3, max(aa, ep(t, C["12.t"], 0.5)), pull=0.4)
    a0 = ep(t, C["12.t"], 0.5)
    ab = ep(t, C["12.b"], 0.5)
    fr(c, "5", "7", 560, 650, 70, mix(INK, GREEN, ab), a0, den_col=mix(INK, BLUE, aa))
    fr(c, "3", "7", 1360, 650, 70, INK, a0, den_col=mix(INK, BLUE, aa))
    text(c, "fatias do mesmo tamanho", W / 2, 420, 28, "black", BLUE, aa)
    fmid(c, ">", W / 2, 650, 90, "black", GREEN, ab)
    regra(c, "mesmo denominador: o MAIOR numerador vence", W / 2, 792, ep(t, C["12.c"], 0.5), 32)


def pessoas(c, cx, y, n, col, a, s=0.55):
    if a <= 0:
        return
    step = 56 * s / 0.55
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * step
        c.drawCircle(x, y - 120 * s, 30 * s, paint(col, a))
        rrect(c, x - 42 * s, y - 82 * s, 84 * s, 82 * s, 30 * s, col, a)


def b_mesmo_num(c, t, C, B):
    head_seq(c, t, C, [("13", "3/5 OU 3/7?", "MESMO NUMERADOR", PURPLE), ("14", "POR QUE O 7 ENGANA?", "MESMO NUMERADOR", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        a0 = ep(t, C["13.t"], 0.5)
        pull = ep(t, C["13.e"], 0.6)
        ab, ac = ep(t, C["13.b"], 0.5), ep(t, C["13.c"], 0.5)
        pizza(c, 560, 430, 170, 5, 3, a0, pull=pull)
        pizza(c, 1360, 430, 170, 7, 3, a0, pull=pull)
        text(c, "3 fatias", 560, 220, 30, "black", "#C9532A", ep(t, C["13.a"], 0.4))
        text(c, "3 fatias", 1360, 220, 30, "black", "#C9532A", ep(t, C["13.a"], 0.4))
        pessoas(c, 560, 700, 5, BLUE, ab)
        pessoas(c, 1360, 700, 7, BLUE, ac)
        text(c, "5 pessoas", 560, 740, 30, "black", BLUE, ab)
        text(c, "7 pessoas", 1360, 740, 30, "black", BLUE, ac)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            boxed(c, 760, 380, 400, 120, AMBER, ad, 0.12)
            text_mid(c, "mais gente →", W / 2, 420, 30, "black", INK, ad)
            text_mid(c, "fatia MENOR", W / 2, 462, 30, "black", INK, ad)
        af = ep(t, C["13.f"], 0.5)
        if af > 0:
            rrect(c, 760, 560, 400, 150, 22, "#FFFFFF", af, shadow=True)
            expr(c, "3/5 > 3/7", W / 2, 645, 64, af, cores={0: GREEN})
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 230, 660, 200, AMBER, aa, 0.12)
        fmid(c, "7 > 5", 550, 300, 64, "black", AMBER, aa)
        text(c, "no dia a dia: número maior = coisa maior", 550, 390, 26, "bold", INK2, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 470, 660, 200, BLUE, ab, 0.08)
        para(c, "o DENOMINADOR conta em quantos pedaços o inteiro foi cortado", 260, 535, 32, "black", BLUE, ab, 590, 42)
    pizza(c, 1150, 430, 120, 5, 3, ep(t, C["14"], 0.5), pull=0.4, label="3/5")
    pizza(c, 1500, 430, 120, 7, 3, ep(t, C["14"], 0.5), pull=0.4, label="3/7")
    regra(c, "mesmo numerador: denominador MENOR, pedaço MAIOR", W / 2, 765, ep(t, C["14.c"], 0.5), 34)


# ======================================================================
# bloco G — produto cruzado
# ======================================================================

def b_cruzado(c, t, C, B):
    frame(c, t, B["start"], "3/5 OU 5/8?", "O PRODUTO CRUZADO", PURPLE)
    a0 = ep(t, C["15.t"], 0.5)
    fr(c, "3", "5", 700, 380, 120, INK, a0)
    fr(c, "5", "8", 1220, 380, 120, INK, a0)
    aa = ep(t, C["15.a"], 0.5)
    pill(c, "PRODUTO CRUZADO = multiplicar em X", W / 2, 215, PURPLE, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab, ac = ep(t, C["15.b"], 0.5), ep(t, C["15.c"], 0.5)
    line(c, 760, 310, 1150, 450, PURPLE, ab, 6, progress=ab)
    line(c, 1160, 310, 770, 450, AMBER, ac, 6, progress=ac)
    fmid(c, "3 · 8 = 24", 700, 600, 54, "black", PURPLE, ab)
    fmid(c, "5 · 5 = 25", 1220, 600, 54, "black", AMBER, ac)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        fmid(c, "<", W / 2, 600, 64, "black", GREEN, ad)
        rrect(c, 1080, 270, 280, 230, 22, GREEN, 0.12 * ad)
        check_icon(c, 1380, 280, 26, ad, GREEN)
        text(c, "25 é maior → 5/8 vence", W / 2, 690, 38, "black", GREEN, ad)
    pill(c, "ATALHO: cada produto fica do lado do numerador que você usou", W / 2, 785, GREEN, size=28,
         a=ep(t, C["15.e"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco H — três ou mais: decimal
# ======================================================================

def b_decimal(c, t, C, B):
    frame(c, t, B["start"], "TRÊS OU MAIS FRAÇÕES?", "TRANSFORME EM DECIMAL", PURPLE)
    regra(c, "numerador ÷ denominador", 560, 250, ep(t, C["16.b"], 0.5), 34)
    pill(c, "o caminho mais seguro", 560, 340, GREEN, size=26, a=ep(t, C["16.a"], 0.5), anchor="center", bounds=(0, 1920))
    rows = [("16.c", "3/4 = 0,75"), ("16.d", "2/3 ≈ 0,667"), ("16.e", "5/8 = 0,625")]
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        expr(c, s, 560, 460 + k * 120 + d, 54, a, cores={2: PURPLE})
    af = ep(t, C["16.f"], 0.5)
    if af > 0:
        line(c, 1000, 230, 1000, 790, LINE, af, 3)
        text(c, "ORDEM DECRESCENTE", 1340, 270, 30, "black", BLUE, af, tracking=1)
        text(c, "do maior para o menor", 1340, 315, 26, "bold", INK2, af)
        for k, (s, v) in enumerate((("3/4", "0,75"), ("2/3", "0,667"), ("5/8", "0,625"))):
            a = af * ep(t, C["16.f"] + 1.2 + 0.5 * k, 0.4)
            expr(c, s, 1220, 410 + k * 95, 50, a)
            text(c, v, 1420, 422 + k * 95, 36, "black", PURPLE, a)
        arrow(c, 1580, 380, 1580, 610, BLUE, af, 5, 16, progress=af)
    ag = ep(t, C["16.g"], 0.5)
    pill(c, "CRESCENTE = do menor para o maior", 1340, 740, BLUE, size=28, a=ag, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco I — a metade como régua
# ======================================================================

def b_metade(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "COMPARE COM A METADE", GREEN)
    a0 = ep(t, C["17.t"], 0.5)
    aa = ep(t, C["17.a"], 0.5)
    text(c, "a fração passou da metade da pizza?", W / 2, 250, 38, "black", GREEN, aa)
    pizza(c, 300, 480, 90, 2, 1, a0, sel_col=GREEN)
    ab, ac, ad = ep(t, C["17.b"], 0.5), ep(t, C["17.c"], 0.5), ep(t, C["17.d"], 0.5)
    K.reta(c, 480, 1640, 480, a0, marcas=[(7 / 16, "7/16", RED, ac), (9 / 16, "9/16", GREEN, ad)])
    text(c, "metade de 16 = 8", W / 2 + 100, 345, 32, "black", PURPLE, ab * (1 - ac))
    if ac > 0:
        text(c, "7 < 8", 760, 640, 44, "black", RED, ac)
        text(c, "não chegou na metade", 760, 690, 28, "bold", INK2, ac)
    if ad > 0:
        text(c, "9 > 8", 1360, 640, 44, "black", GREEN, ad)
        text(c, "passou da metade", 1360, 690, 28, "bold", INK2, ad)
    pill(c, "sem fazer conta nenhuma · elimina alternativas na hora", W / 2, 785, GREEN, size=28,
         a=ep(t, C["17.e"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Misto vira impróprio antes de qualquer conta.", "Mesmo numerador: denominador menor, pedaço maior.",
          "Três ou mais frações: transforme em decimal."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Multiplicar só o inteiro: “2 e 3/4” vezes 3 virar “6 e 3/4”", "o inteiro é a parte que salta aos olhos",
          "o 3/4 também é multiplicado: converta para imprópria antes (dá 33/4)"),
         ("Achar 3/7 maior que 3/5 porque 7 é maior que 5", "número maior costuma ser coisa maior",
          "o denominador é em quantas fatias a pizza foi cortada: mais fatias, fatias menores"),
         ("Comparar “no olho” frações muito próximas", "elas parecem quase iguais",
          "quando estão perto, o olho erra: transforme em decimal e compare")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões (textos exatamente como no material; conferidos por script)
# ======================================================================

Q6_ENUNC = ["Uma receita de bolo leva", "2|3/4 xícaras de farinha.",
            "Para preparar três receitas iguais, quantas xícaras de farinha serão necessárias?"]
Q6_ALTS = [("A", "= 6|3/4", "multiplicou só o inteiro", AMBER), ("B", "= 7|1/2", "não sai de conta certa", RED),
           ("C", "= 8|1/4", "", GREEN), ("D", "= 8|3/4", "copiou o 3/4 do enunciado", RED),
           ("E", "= 9", "não sai de conta certa", RED)]

Q2_INTRO = "Quatro candidatos acertaram as seguintes frações de uma prova:"
Q2_NOMES = [("Ana", "5/8", "0,625"), ("Bruno", "3/5", "0,600"), ("Carla", "7/10", "0,700"), ("Diego", "2/3", "≈ 0,667")]
Q2_PERG = "Qual é a ordem decrescente de acertos?"
Q2_ALTS = [("A", "Carla, Diego, Ana, Bruno", "", GREEN), ("B", "Carla, Ana, Diego, Bruno", "troca Ana e Diego", RED),
           ("C", "Diego, Carla, Ana, Bruno", "Diego na frente de Carla", RED),
           ("D", "Bruno, Ana, Diego, Carla", "é a ordem CRESCENTE", AMBER), ("E", "Ana, Carla, Diego, Bruno", "Ana em primeiro", RED)]

TI_INTRO = "Três marcas de tinta informam o rendimento por lata em relação a uma parede padrão:"
TI_LINHAS = [("a marca X cobre 3/5 da parede,", "0,600"), ("a marca Y cobre 5/8", "0,625"), ("e a marca Z cobre 7/11.", "≈ 0,636")]
TI_PERG = "Qual é a ordem decrescente de rendimento?"
TI_ALTS = [("A", "X, Y, Z", "é a ordem CRESCENTE", AMBER), ("B", "Y, X, Z", "comparou no olho", RED), ("C", "Z, Y, X", "", GREEN),
           ("D", "Z, X, Y", "comparou no olho", RED), ("E", "Y, Z, X", "comparou no olho", RED)]


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("22", "QUESTÃO · EU FAÇO", "A RECEITA DE BOLO", BLUE), ("23", "RESOLVENDO", "MISTO VIRA IMPRÓPRIO", PURPLE),
                       ("24", "E A ARMADILHA?", "A LETRA A", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    y = 250
    y += para(c, Q6_ENUNC[0], 190, y, 32, "black", INK, a0, 600, 40) + 6
    expr(c, Q6_ENUNC[1], 190, y + 6, 32, a0, align="left", cores={0: PURPLE})
    y += 70
    para(c, Q6_ENUNC[2], 190, y, 32, "bold", BLUE, ep(t, C["22.b"], 0.4), 600, 40)
    text(c, "Questão do material de estudo (seção 12)", 190, 830, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.{k}"] for L, k in zip("ABCDE", "cdefg")}
    cues_x = {"A": C["24.xa"], "B": C["24.xb"], "D": C["24.xd"], "E": C["24.xe"]}
    K.alternativas(c, t, C, Q6_ALTS, 870, 205, 820, 42, C["23.ok"], "C", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["22.end"] - 1.9, 470, 680)
    ra = ep(t, C["23.a"], 0.4) * (1 - ep(t, C["24"], 0.4))
    if ra > 0:
        rrect(c, 170, 470, 600, 345, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "2|3/4 = 11/4", 470, 530, 38, ep(t, C["23.a"], 0.4) * ra, cores={2: GREEN})
        expr(c, "11/4 · 3 = 33/4", 470, 615, 38, ep(t, C["23.b"], 0.4) * ra, cores={4: GREEN})
        expr(c, "33 ÷ 4 = 8 , resto 1", 470, 695, 38, ep(t, C["23.c"], 0.4) * ra)
        expr(c, "→ 8|1/4", 470, 775, 42, ep(t, C["23.d"], 0.4) * ra, cores={1: GREEN})
    result_box(c, "Letra C", 470, 660, 50, ep(t, C["24"], 0.5), GREEN)
    pill(c, "33/4 é EXATAMENTE 8 e 1/4", 470, 770, GREEN, size=26, a=ep(t, C["24.xe"], 0.5), anchor="center", bounds=(0, 1920))


def _lista_nomes(c, t, C, y, dec_cue, dec_a):
    for k, (nome, f, dec) in enumerate(Q2_NOMES):
        yy = y + k * 78
        a = ep(t, C["25.b"] + 0.5 * k, 0.4)
        text(c, nome, 190, yy + 12, 34, "black", INK, a, align="left")
        n_, d_ = f.split("/")
        fr(c, n_, d_, 360, yy, 32, PURPLE, a)
        da = dec_a * ep(t, C[f"27.{'abcd'[k]}"], 0.4)
        text(c, ("= " + dec) if not dec.startswith("≈") else dec, 420, yy + 12, 34, "black", GREEN, da, align="left")


def b_q2(c, t, C, B):
    head_seq(c, t, C, [("25", "QUESTÃO · NÓS FAZEMOS", "QUEM ACERTOU MAIS?", BLUE), ("26", "DICA ANTES DE PAUSAR", "SÃO 4 FRAÇÕES", GREEN),
                       ("27", "RESOLVENDO", "TUDO EM DECIMAL", PURPLE), ("28", "E AS OUTRAS?", "POR QUE ESTÃO ERRADAS", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    y = 240 + para(c, Q2_INTRO, 190, 240, 30, "black", INK, a0, 620, 38) + 40
    _lista_nomes(c, t, C, y, "27", ep(t, C["27.a"], 0.4))
    para(c, Q2_PERG, 190, y + 4 * 78 + 10, 30, "bold", BLUE, ep(t, C["25.c"], 0.4), 620, 38)
    text(c, "Questão do material de estudo (seção 12)", 190, 830, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.{k}"] for L, k in zip("ABCDE", "defgh")}
    cues_x = {"B": C["28.xb"], "C": C["28.xc"], "D": C["28.xd"], "E": C["28.xe"]}
    K.alternativas(c, t, C, Q2_ALTS, 870, 215, 820, 38, C["27.ok"], "A", cues_in, cues_x, gap=14)
    at = ep(t, C["26.t"], 0.5) * (1 - ep(t, C["27"], 0.4))
    pill(c, "DICA: 4 frações → qual o caminho mais seguro?", 1280, 640, GREEN, size=28, a=at, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["26.end"] - 1.9, 1280, 740)
    ae = ep(t, C["27.e"], 0.5)
    expr(c, "0,700 > 0,667 > 0,625 > 0,600", 1280, 640, 38, ae, cores={0: GREEN})
    result_box(c, "Letra A", 1280, 725, 46, ep(t, C["27.ok"], 0.5), GREEN)
    pill(c, "as 4 estão entre 0,6 e 0,7: no olho, não daria", 1280, 805, AMBER, size=26, a=ep(t, C["28.x"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_tintas(c, t, C, B):
    head_seq(c, t, C, [("29", "QUESTÃO · VOCÊ FAZ", "AS TRÊS TINTAS", BLUE), ("30", "VAMOS CONFERIR", "TRÊS FRAÇÕES: DECIMAL", PURPLE),
                       ("31", "REPARE", "TODAS PERTO DE 0,6", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    y = 240 + para(c, TI_INTRO, 190, 240, 30, "black", INK, a0, 620, 38) + 40
    for k, (s, dec) in enumerate(TI_LINHAS):
        yy = y + k * 78
        a = ep(t, C["29.b"] + 0.9 * k, 0.4)
        toks = s.rstrip(".").split()
        w_ = expr(c, " ".join(toks), 190, yy, 34, a, align="left", cores={[i for i, x in enumerate(toks) if "/" in x][0]: PURPLE})
        if s.endswith("."):
            fmid(c, ".", 190 + w_ + 8, yy, 34, "black", INK, a)
        text(c, dec if dec.startswith("≈") else "= " + dec, 190 + w_ + 24, yy + 12, 32, "black", GREEN,
             ep(t, C[f"30.{'abc'[k]}"], 0.4), align="left")
    para(c, TI_PERG, 190, y + 3 * 78 + 10, 30, "bold", BLUE, ep(t, C["29.c"], 0.4), 620, 38)
    text(c, "Questão extra da série (estilo ENEM)", 190, 830, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.{k}"] for L, k in zip("ABCDE", "defgh")}
    cues_x = {"A": C["31.xa"], "B": C["31.xb"], "D": C["31.xb"] + 0.3, "E": C["31.xb"] + 0.6}
    K.alternativas(c, t, C, TI_ALTS, 1060, 215, 630, 42, C["30.ok"], "C", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["29.end"] - 1.9, 1375, 700)
    ad = ep(t, C["30.d"], 0.5)
    expr(c, "0,636 > 0,625 > 0,600", 1375, 640, 40, ad, cores={0: GREEN})
    result_box(c, "Letra C", 1375, 725, 46, ep(t, C["30.ok"], 0.5), GREEN)
    pill(c, "todas perto de 0,6: é preciso dividir de fato", 1375, 805, AMBER, size=26, a=ep(t, C["31.a"], 0.5),
         anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS QUATRO OPERAÇÕES", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    for k, (s, col) in enumerate((("LER", BLUE), ("COMPARAR", GREEN))):
        check_icon(c, 330, 300 + k * 110, 30, aa, col)
        text(c, s, 380, 314 + k * 110, 48, "black", INK, aa, align="left")
    ab = ep(t, C["33.b"], 0.5)
    text(c, "agora: fazer contas com elas", 1260, 280, 40, "black", PURPLE, ab)
    for k, s in enumerate(("+", "−", "×", "÷")):
        a = ep(t, C["33.c"] + 0.45 * k, 0.4)
        chip(c, s, 900 + k * 240, 450, PURPLE, a, 80, w=170)
    expr(c, "1/2 + 1/3 = ?", 1260, 620, 60, ab)
    pill(c, "ep. 3 · as quatro operações com frações", W / 2, 780, PURPLE, size=32, a=ep(t, C["33.d"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Você acertou a questão das tintas?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, tipos=b_tipos, mista=b_mista, impropria=b_impropria,
              ouro=b_ouro, mesmo_den=b_mesmo_den, mesmo_num=b_mesmo_num, cruzado=b_cruzado, decimal=b_decimal,
              metade=b_metade, recap=b_recap, erros=b_erros, q6=b_q6, q2=b_q2, tintas=b_tintas, ponte=b_ponte, cta=b_cta)
