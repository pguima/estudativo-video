"""Visual — Frações, Decimais e Dízimas, Episódio 3: As quatro operações com frações (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, barra, expr com frações empilhadas, reta, alternativas, erro_cards...).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
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
fr, expr, expr_w, pizza, barra, reta = K.fr, K.expr, K.expr_w, K.pizza, K.barra, K.reta
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep3_operacoes.mp4"
CARD_R = K.CARD_R
AGUA = "#5AA9E6"


def cfrac(c, num, den, cx, cy, size, a, col=None, cut_n=0.0, cut_d=0.0, new_n="", new_d=""):
    """fração empilhada com os termos 'cortados' (simplificação em cruz): risca o termo e escreve o novo em verde"""
    if a <= 0:
        return
    col = INK if col is None else col
    w = K.fr_w(num, den, size)
    ftext(c, num, cx, cy - size * 0.16, size, "black", mix(col, LIGHT, 0.7 * cut_n), a)
    line(c, cx - w / 2, cy + size * 0.06, cx + w / 2, cy + size * 0.06, col, a, max(3, size * 0.075), cap_round=True)
    ftext(c, den, cx, cy + size * 0.98, size, "black", mix(col, LIGHT, 0.7 * cut_d), a)
    hw = K.ftext_w(num, "black", size) / 2 + 10
    if cut_n > 0:
        strike(c, cx - hw, cy - size * 0.2, cx + hw, cy - size * 0.86, a, RED, cut_n)
        ftext(c, new_n, cx + hw + 6, cy - size * 0.66, size * 0.55, "black", GREEN, a * cut_n, align="left")
    hw = K.ftext_w(den, "black", size) / 2 + 10
    if cut_d > 0:
        strike(c, cx - hw, cy + size * 0.98, cx + hw, cy + size * 0.3, a, RED, cut_d)
        ftext(c, new_d, cx + hw + 6, cy + size * 1.12, size * 0.55, "black", GREEN, a * cut_d, align="left")


def copo(c, x, by, w, h, nivel, a, col=AGUA):
    """recipiente com fundo em by; nivel = fração cheia (0..1)"""
    if a <= 0:
        return
    rrect(c, x, by - h, w, h, 14, "#FFFFFF", a)
    if nivel > 0:
        rrect(c, x + 5, by - h * nivel, w - 10, h * nivel - 5, 10, col, a * 0.85)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, by - h, w, h), 14, 14), paint(INK2, a, stroke=5))


def atalho(c, s1, s2, cx, y, w, a):
    if a <= 0:
        return
    boxed(c, cx - w / 2, y, w, 130 if s2 else 90, GREEN, a, 0.08)
    text(c, "ATALHO", cx, y + 34, 22, "black", GREEN, a, tracking=2)
    fmid(c, s1, cx, y + 66, 32, "black", INK, a)
    if s2:
        fmid(c, s2, cx, y + 104, 32, "black", INK, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FRAÇÕES · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ac = ep(t, C["01.c"], 0.5)
    w = expr(c, "1/2 + 1/3 = 2/5", W / 2 - 40, 450, 130, aa, cores={4: mix(AMBER, RED, ac)})
    fmid(c, "?", W / 2 - 40 + w / 2 + 70, 430, 130, "black", mix(AMBER, RED, ac), aa * (1 - ac))
    ab = ep(t, C["01.b"], 0.5) * (1 - ep(t, C["01.d"], 0.4))
    fmid(c, "em cima: 1 + 1 = 2", W / 2, 230, 40, "black", AMBER, ab)
    fmid(c, "embaixo: 2 + 3 = 5", W / 2, 660, 40, "black", AMBER, ab)
    if ac > 0:
        strike(c, W / 2 - w / 2 - 70, 470, W / 2 + w / 2 + 10, 400, 1, RED, ac)
        selo(c, 1480, 290, ac, "ERRADO", RED, -8, 44)
    ad = ep(t, C["01.d"], 0.5)
    pizza(c, 420, 700, 90, 6, 5, ad, sel_col=GREEN)
    pill(c, "a prova: uma pizza, em 10 segundos", 1000, 720, BLUE, size=34, a=ad, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "fazer as QUATRO operações", "com frações"), ("02.b", "sem calculadora", "só com conta pequena"),
            ("02.c", "sem cair nas pegadinhas", "as alternativas que enganam")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + j * 170 + d
        check_icon(c, 260, y - 14, 32, a, GREEN)
        text(c, s, 320, y, 50, "black", INK, a, align="left")
        text(c, sub, 320, y + 52, 30, "bold", GRAY, a, align="left")
    for k, s in enumerate(("+", "−", "×", "÷")):
        a = ep(t, C["02.a"] + 0.5 + 0.25 * k, 0.4)
        x = 1260 + (k % 2) * 200
        y = 340 + (k // 2) * 200
        if a <= 0:
            continue
        rrect(c, x - 80, y - 80, 160, 160, 30, mix("#FFFFFF", PURPLE, 0.12), a)
        fmid(c, s, x, y, 110, "black", PURPLE, a)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    cols = [("03.a", 420, "MMC", PURPLE), ("03.b", 960, "SIMPLIFICAR", BLUE), ("03.c", 1500, "POTÊNCIA", PURPLE)]
    for cue, x, tit, col in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 245, 190, 490, 610, 24, mix("#FFFFFF", col, 0.06), a)
        text(c, tit, x, 250, 34, "black", col, a, tracking=1)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "“o reencontro”", 420, 300, 30, "bold", INK2, aa)
    for k, (s, d) in enumerate((("4, 8, 12", "tabuada do 4"), ("6, 12", "tabuada do 6"))):
        a = aa * ep(t, C["03.a"] + 0.6 + 0.5 * k, 0.4)
        text(c, d, 420, 390 + k * 130, 26, "bold", GRAY, a)
        text(c, s, 420, 440 + k * 130, 46, "black", INK, a)
    fmid(c, "MMC(4, 6) = 12", 420, 700, 44, "black", GREEN, aa * ep(t, C["03.a"] + 1.8, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    text(c, "episódio 1", 960, 300, 30, "bold", INK2, ab)
    expr(c, "6/12 = 1/2", 960, 470, 80, ab, cores={2: BLUE})
    para(c, "dividir em cima e embaixo pelo mesmo número", 960, 640, 30, "black", BLUE, ab, 420, align="center")
    acc = ep(t, C["03.c"], 0.5)
    text(c, "multiplicação repetida", 1500, 300, 30, "bold", INK2, acc)
    fmid(c, "2^3", 1500, 450, 110, "black", PURPLE, acc)
    fmid(c, "= 2 · 2 · 2 = 8", 1500, 620, 50, "black", INK, ep(t, C["03.c"] + 1.0, 0.4))


# ======================================================================
# bloco A — a prova da pizza
# ======================================================================

def b_prova(c, t, C, B):
    head_seq(c, t, C, [("04", "1/2 + 1/3 = 2/5?", "A PROVA DA PIZZA", AMBER), ("05", "QUANTO DÁ, ENTÃO?", "RECORTE EM 6 FATIAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    x0, x1, yr = 380, 1540, 700
    marcas = []
    if sid == "04":
        aa, ab = ep(t, C["04.a"], 0.5), ep(t, C["04.b"], 0.5)
        pizza(c, 330, 360, 120, 2, 1, aa)
        fr(c, "1", "2", 330, 520, 40, INK, aa)
        fmid(c, "+", 500, 360, 80, "black", INK, ab)
        pizza(c, 670, 360, 120, 3, 1, ab, sel_col=BLUE)
        fr(c, "1", "3", 670, 520, 40, INK, ab)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            pill(c, "MAIS que meia pizza", 500, 600, GREEN, size=30, a=acc, anchor="center", bounds=(0, 1920))
        ad = ep(t, C["04.d"], 0.5)
        pizza(c, 1420, 360, 140, 5, 2, ad, sel_col=RED)
        fr(c, "2", "5", 1420, 540, 40, RED, ad)
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            line(c, 1420, 200, 1420, 520, PURPLE, ae, 5, dash=(14, 10), progress=ae)
            text(c, "metade", 1420, 192, 26, "black", PURPLE, ae)
        marcas = [(0.4, "2/5", RED, ae)]
        reta(c, x0, x1, yr, ep(t, C["04.e"], 0.5), marcas)
        selo(c, 990, 400, ep(t, C["04.f"], 0.5), "NÃO PODE SER 2/5", RED, -6, 36)
        return
    # 05: recortando em sextos
    a0 = ep(t, C["05"], 0.4)
    cut = ep(t, C["05.a"], 0.9)
    n1, n2 = (6, 6) if cut > 0.5 else (2, 3)
    s1 = ep(t, C["05.b"], 0.4)
    s2 = ep(t, C["05.c"], 0.4)
    pizza(c, 330, 360, 120, n1, 3 if n1 == 6 else 1, a0)
    pizza(c, 670, 360, 120, n2, 2 if n2 == 6 else 1, a0, sel_col=BLUE)
    fmid(c, "+", 500, 360, 80, "black", INK, a0)
    fr(c, "1", "2", 330, 520, 40, INK, a0 * (1 - s1))
    fr(c, "3", "6", 330, 520, 40, MOLHO_(), s1)
    fr(c, "1", "3", 670, 520, 40, INK, a0 * (1 - s2))
    fr(c, "2", "6", 670, 520, 40, BLUE, s2)
    ad = ep(t, C["05.d"], 0.5)
    fmid(c, "=", 880, 360, 80, "black", INK, ad)
    pizza(c, 1110, 360, 140, 6, 5, ad, sel_col=GREEN)
    expr(c, "3/6 + 2/6 = 5/6", 1450, 360, 58, ad, cores={4: GREEN})
    ae = ep(t, C["05.e"], 0.5)
    reta(c, x0, x1, yr, a0, [(0.4, "2/5", RED, 0.35), (5 / 6, "5/6", GREEN, ae)])
    af = ep(t, C["05.f"], 0.5)
    pill(c, "teste rápido: compare com a METADE", 1450, 230, GREEN, size=28, a=af, anchor="center", bounds=(0, 1920))


def MOLHO_():
    return K.MOLHO


# ======================================================================
# bloco B — soma e subtração
# ======================================================================

VARAL = [("6", "4", "3", "2"), ("3", "2", "3", "2"), ("3", "1", "3", "3"), ("1", "1", "1", "")]


def b_soma(c, t, C, B):
    head_seq(c, t, C, [("06", "O SEGREDO DA SOMA", "MESMO TAMANHO DE FATIA", BLUE), ("07", "EU FAÇO", "1/6 + 1/4 + 1/3", PURPLE),
                       ("08", "ATALHO", "CONVERTER PARA DOZE AVOS", GREEN), ("09", "AGORA SIM", "SOMA SÓ EM CIMA", PURPLE),
                       ("10", "SUBTRAÇÃO", "IGUALZINHA", PURPLE), ("11", "ATALHO PARA DUAS FRAÇÕES", "A BORBOLETA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08", "09", "10", "11"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.4)
        rc = ep(t, C["06.b"], 0.8)
        n1, n2 = (12, 12) if rc > 0.5 else (4, 3)
        pizza(c, 380, 430, 170, n1, 3 if n1 == 12 else 1, a0)
        pizza(c, 860, 430, 170, n2, 4 if n2 == 12 else 1, a0, sel_col=BLUE)
        fmid(c, "+", 620, 430, 80, "black", INK, a0)
        aa = ep(t, C["06.a"], 0.5) * (1 - rc)
        if aa > 0:
            boxed(c, 220, 650, 820, 100, AMBER, aa, 0.14)
            text_mid(c, "fatias de tamanhos diferentes: não dá para somar", 630, 700, 30, "black", INK, aa)
        text(c, "todas recortadas em 12", 620, 720, 34, "black", GREEN, rc)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            boxed(c, 1150, 260, 520, 240, BLUE, acc, 0.08)
            text(c, "DENOMINADOR COMUM", 1410, 310, 28, "black", BLUE, acc, tracking=1)
            para(c, "o mesmo número embaixo de todas as frações", 1410, 370, 32, "bold", INK, acc, 440, align="center")
        add = ep(t, C["06.d"], 0.5)
        chip(c, "quem acha: o MMC", 1410, 600, PURPLE, add, 40)
        return
    if sid == "07":
        expr(c, "1/6 + 1/4 + 1/3", 560, 270, 80, ep(t, C["07.a"], 0.5))
        ab = ep(t, C["07.b"], 0.5)
        rc = ep(t, C["07.e"], 0.9)
        for k, n in enumerate((6, 4, 3)):
            a = ab * ep(t, C["07.b"] + 0.4 * k, 0.4)
            nn = 12 if rc > 0.5 else n
            pizza(c, 300 + k * 260, 530, 105, nn, 12 // n if nn == 12 else 1, a, sel_col=(MOLHO_(), BLUE, GREEN)[k])
            text(c, f"em {n}" if nn != 12 else "em 12", 300 + k * 260, 690, 30, "black", GREEN if nn == 12 else INK2, a)
        acc = ep(t, C["07.c"], 0.5)
        fmid(c, "MMC(6, 4, 3) = ?", 1380, 230, 44, "black", PURPLE, acc * (1 - ep(t, C["07.e"], 0.4)))
        ad = ep(t, C["07.d"], 0.5)
        for k, row in enumerate(VARAL):
            a = ad * ep(t, C["07.d"] + 0.9 * k, 0.3)
            y = 330 + k * 82
            for j in range(3):
                text(c, row[j], 1190 + j * 90, y, 46, "black", INK, a, align="right")
            if row[3]:
                line(c, 1390, y - 46, 1390, y + 24, INK2, a, 4)
                text(c, row[3], 1420, y, 46, "black", GREEN, a, align="left")
        ae = ep(t, C["07.e"], 0.5)
        fmid(c, "MMC = 2 · 2 · 3 = 12", 1310, 230, 44, "black", GREEN, ae)
        pill(c, "o varal da série do MMC", 1310, 720, GREEN, size=26, a=ad, anchor="center", bounds=(0, 1920))
        return
    if sid == "08":
        atalho(c, "divide pelo de BAIXO, multiplica pelo de CIMA", "", W / 2, 190, 900, ep(t, C["08.a"], 0.5))
        rows = [("08.b", "1", "6", "2", MOLHO_()), ("08.c", "1", "4", "3", BLUE), ("08.d", "1", "3", "4", GREEN)]
        for k, (cue, n_, d_, r_, col) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            x = 420 + k * 540
            if a <= 0:
                continue
            q = 12 // int(d_)
            expr(c, f"{n_}/{d_} = {r_}/12", x, 400, 76, a, cores={2: col})
            fmid(c, f"12 ÷ {d_} = {q}", x, 560, 40, "black", INK2, a)
            fmid(c, f"{q} · {n_} = {r_}", x, 620, 40, "black", col, ep(t, C[cue] + 1.2, 0.4))
            pizza(c, x, 740, 70, 12, int(r_), ep(t, C[cue] + 1.4, 0.4), sel_col=col, sombra=False)
        return
    if sid == "09":
        a0 = ep(t, C["09"], 0.5)
        expr(c, "2/12 + 3/12 + 4/12", 620, 290, 76, a0)
        aa = ep(t, C["09.a"], 0.5)
        expr(c, "= 9/12", 620, 450, 76, aa, cores={1: PURPLE})
        pizza(c, 1420, 400, 170, 12, 9, aa, sel_col=PURPLE)
        ab = ep(t, C["09.b"], 0.5)
        expr(c, "9/12 = 3/4", 620, 590, 76, ab, cores={2: GREEN})
        fmid(c, "÷ 3", 440, 590, 36, "black", GREEN, ab)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            boxed(c, 1080, 640, 660, 140, AMBER, acc, 0.14)
            text_mid(c, "o 12 NÃO se soma", 1410, 685, 34, "black", INK, acc)
            text_mid(c, "ele é só o tamanho da fatia", 1410, 735, 30, "bold", INK2, acc)
        return
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        expr(c, "3/4 − 1/6", 560, 270, 80, aa)
        fmid(c, "MMC(4, 6) = 12", 560, 400, 44, "black", PURPLE, ep(t, C["10.b"], 0.5))
        acc = ep(t, C["10.c"], 0.5)
        expr(c, "9/12 − 2/12", 560, 540, 76, acc)
        ad = ep(t, C["10.d"], 0.5)
        expr(c, "= 7/12", 560, 690, 76, ad, cores={1: GREEN})
        gone = {7, 8} if ad > 0.5 else set()
        pizza(c, 1300, 450, 190, 12, set(range(9)) - gone, ep(t, C["10.c"], 0.5), sel_col=PURPLE, gone=gone)
        pill(c, "7 e 12 sem divisor comum: já simplificada", 1300, 730, GREEN, size=28, a=ep(t, C["10.e"], 0.5),
             anchor="center", bounds=(0, 1920))
        return
    # 11: a borboleta
    aa = ep(t, C["11.a"], 0.5)
    s = 120
    xl, xr, cy = 560, 860, 420
    fr(c, "1", "2", xl, cy, s, INK, aa)
    fr(c, "1", "3", xr, cy, s, INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    yn, yd = cy - s * 0.52, cy + s * 0.62
    if ab > 0:
        line(c, xl + 40, yn + 10, xr - 40, yd - 10, GREEN, ab, 6, progress=ab)
        line(c, xl + 40, yd - 10, xr - 40, yn + 10, PURPLE, ab, 6, progress=ep(t, C["11.b"] + 1.0, 0.5))
    if aa > 0:
        c.drawCircle((xl + xr) / 2, cy + s * 0.05, 40, paint("#FFFFFF", aa))
    fmid(c, "+", (xl + xr) / 2, cy + s * 0.05, 80, "black", INK, aa)
    fmid(c, "em cima: 1 · 3 + 2 · 1 = 5", 1350, 330, 40, "black", INK, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        arrow(c, xl, yd + 90, xr, yd + 90, AMBER, acc, 5, 16, progress=acc)
    fmid(c, "embaixo: 2 · 3 = 6", 1350, 440, 40, "black", AMBER, acc)
    ad = ep(t, C["11.d"], 0.5)
    expr(c, "1/2 + 1/3 = 5/6", 1350, 600, 70, ad, cores={4: GREEN})
    pill(c, "só para DUAS frações · sem procurar MMC", 710, 740, GREEN, size=26, a=ep(t, C["11.a"], 0.5), anchor="center",
         bounds=(0, 1920))
    pill(c, "depois, confira se simplifica", 1350, 740, BLUE, size=26, a=ep(t, C["11.e"], 0.5), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# bloco C — multiplicação
# ======================================================================

def b_mult(c, t, C, B):
    head_seq(c, t, C, [("12", "MULTIPLICAR", "METADE DE UM TERÇO", PURPLE), ("13", "A REGRA", "CIMA × CIMA, BAIXO × BAIXO", PURPLE),
                       ("14", "ATALHO", "SIMPLIFICAR EM CRUZ", GREEN), ("15", "E SEM CORTAR?", "NÚMEROS ENORMES", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14", "15"])
    if sid == "12":
        aa = ep(t, C["12"], 0.5)
        ab = ep(t, C["12.b"], 0.5)
        acc = ep(t, C["12.c"], 0.5)
        sel = {0, 3} if ab > 0.5 else set()
        sel2 = {0} if acc > 0.5 else set()
        barra(c, 260, 260, 600, 400, 3, 2, sel - sel2, aa, sel2=sel2, sel2_col=GREEN)
        if ab > 0:
            text(c, "1/3 da barra = 1 coluna", 560, 730, 32, "black", AMBER, ab)
        text(c, "metade do 1/3: 1 quadradinho", 560, 790, 32, "black", GREEN, acc)
        ad = ep(t, C["12.d"], 0.5)
        fmid(c, "1 de 6", 1350, 300, 50, "black", INK2, ad)
        fr(c, "1", "6", 1350, 410, 100, GREEN, ad)
        ae = ep(t, C["12.e"], 0.5)
        expr(c, "1/2 de 1/3 = 1/2 · 1/3", 1350, 640, 52, ae, cores={1: AMBER, 4: PURPLE})
        pill(c, "o “de” é vezes (episódio 1)", 1350, 760, PURPLE, size=26, a=ae, anchor="center", bounds=(0, 1920))
        return
    if sid == "13":
        a0 = ep(t, C["13"], 0.5)
        hn, hd = ep(t, C["13.a"], 0.4), ep(t, C["13.b"], 0.4)
        s = 120
        xs = (620, 920, 1300)
        if hn > 0:
            rrect(c, 520, 280, 880, 130, 22, MOLHO_(), 0.14 * hn)
        if hd > 0:
            rrect(c, 520, 425, 880, 130, 22, BLUE, 0.12 * hd)
        fr(c, "1", "2", xs[0], 420, s, INK, a0)
        fmid(c, "·", 770, 440, 90, "black", INK, a0)
        fr(c, "1", "3", xs[1], 420, s, INK, a0)
        ac_ = ep(t, C["13.c"], 0.5)
        fmid(c, "=", 1110, 440, 90, "black", INK, ac_)
        fr(c, "1", "6", xs[2], 420, s, GREEN, ac_)
        text(c, "numerador × numerador", 1560, 365, 28, "black", "#C9532A", hn)
        text(c, "denominador × denominador", 1560, 510, 28, "black", BLUE, hd)
        pill(c, "NÃO precisa de denominador comum", 760, 680, BLUE, size=30, a=ep(t, C["13.d"], 0.5), anchor="center",
             bounds=(0, 1920))
        ae = ep(t, C["13.e"], 0.5)
        if ae > 0:
            boxed(c, 1180, 620, 440, 150, GREEN, ae, 0.08)
            text(c, "número inteiro?", 1400, 660, 26, "black", GREEN, ae)
            expr(c, "3 = 3/1", 1400, 725, 50, ae, cores={2: GREEN})
        return
    if sid == "14":
        pill(c, "SIMPLIFICAR EM CRUZ = dividir um de cima e um de baixo, em diagonal, pelo mesmo número", W / 2, 215, BLUE,
             size=24, a=ep(t, C["14.a"], 0.5), anchor="center", bounds=(0, 1920))
        ab = ep(t, C["14.b"], 0.5)
        s = 130
        xl, xr, cy = 480, 800, 440
        c48 = ep(t, C["14.c"], 0.6)
        c39 = ep(t, C["14.d"], 0.6)
        cfrac(c, "4", "9", xl, cy, s, ab, cut_n=c48, cut_d=c39, new_n="1", new_d="3")
        fmid(c, "·", (xl + xr) / 2, cy + 20, 90, "black", INK, ab)
        cfrac(c, "3", "8", xr, cy, s, ab, cut_n=c39, cut_d=c48, new_n="1", new_d="2")
        yn, yd = cy - s * 0.52, cy + s * 0.62
        if c48 > 0:
            line(c, xl + 50, yn + 14, xr - 50, yd - 14, GREEN, ab * c48, 6, dash=(16, 10), progress=c48)
            fmid(c, "4 e 8: ÷ 4", 1120, 330, 36, "black", GREEN, c48)
        if c39 > 0:
            line(c, xl + 50, yd - 14, xr - 50, yn + 14, GREEN, ab * c39, 6, dash=(16, 10), progress=c39)
            fmid(c, "3 e 9: ÷ 3", 1120, 400, 36, "black", GREEN, c39)
        ae = ep(t, C["14.e"], 0.5)
        expr(c, "1/3 · 1/2 = 1/6", 1350, 600, 70, ae, cores={4: GREEN})
        return
    # 15 sem cortar
    aa = ep(t, C["15.a"], 0.5)
    expr(c, "4/9 · 3/8 = 12/72", 560, 330, 72, aa, cores={4: AMBER})
    fmid(c, "4 · 3 = 12    9 · 8 = 72", 560, 470, 34, "bold", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    fmid(c, "ainda teria de simplificar...", 560, 560, 34, "black", AMBER, ab)
    acc = ep(t, C["15.c"], 0.5)
    expr(c, "12/72 = 1/6", 560, 680, 62, acc, cores={2: GREEN})
    if acc > 0:
        boxed(c, 1080, 260, 580, 300, GREEN, acc, 0.06)
        text(c, "cortando antes", 1370, 310, 28, "black", GREEN, acc)
        expr(c, "1/3 · 1/2 = 1/6", 1370, 430, 60, acc, cores={4: GREEN})
        text(c, "mesmo resultado, números pequenos", 1370, 530, 24, "bold", INK2, acc)
    regra(c, "corte antes, multiplique depois", 1370, 690, ep(t, C["15.d"], 0.5), 34, GREEN)


# ======================================================================
# bloco D — divisão
# ======================================================================

def b_div(c, t, C, B):
    head_seq(c, t, C, [("16", "DIVIDIR", "QUANTAS VEZES CABE?", BLUE), ("17", "MAS POR QUE", "INVERTER?", PURPLE),
                       ("18", "A REGRA", "CONSERVA, INVERTE, MULTIPLICA", PURPLE), ("19", "QUANTOS COPOS CABEM?", "3/4 ÷ 2/5", BLUE),
                       ("20", "ATALHO", "CORTE DEPOIS DE INVERTER", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17", "18", "19", "20"])
    if sid == "16":
        aa = ep(t, C["16"], 0.5)
        ab = ep(t, C["16.b"], 0.5)
        sel = {0, 1} if ab > 0.6 else ({0} if ab > 0.3 else set())
        pizza(c, 520, 460, 220, 2, sel, aa, sel_col=BLUE, pull=0.8 * ab, cut=ab)
        badge_num(c, 1, 640, 330, ab, 30, bg=BLUE)
        badge_num(c, 2, 400, 600, ep(t, C["16.b"] + 0.5, 0.4), 30, bg=BLUE)
        text(c, "quantas METADES cabem na pizza inteira?", 1250, 300, 32, "black", INK, aa)
        acc = ep(t, C["16.c"], 0.5)
        expr(c, "1 ÷ 1/2 = 2", 1250, 470, 90, acc, cores={4: GREEN})
        pill(c, "o resultado ficou MAIOR, e está certo", 1250, 660, AMBER, size=30, a=ep(t, C["16.d"], 0.5), anchor="center",
             bounds=(0, 1920))
        return
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        pizza(c, 300, 360, 100, 2, {0, 1}, aa, sel_col=BLUE, pull=0.6)
        text(c, "1 pizza = 2 meios", 300, 520, 30, "black", INK2, aa)
        ab = ep(t, C["17.b"], 0.5)
        for k in range(3):
            pizza(c, 700 + k * 230, 360, 100, 2, {0, 1}, ab * ep(t, C["17.b"] + 0.25 * k, 0.3), sel_col=BLUE, pull=0.6)
        text(c, "3 pizzas = 6 meios", 930, 520, 30, "black", INK2, ab)
        acc = ep(t, C["17.c"], 0.5)
        expr(c, "÷ 1/2 = × 2", 560, 680, 72, acc, cores={0: BLUE, 1: BLUE, 3: GREEN, 4: GREEN})
        ad = ep(t, C["17.d"], 0.5)
        if ad > 0:
            fr(c, "1", "2", 1260, 640, 70, BLUE, ad)
            arrow(c, 1320, 670, 1440, 670, LIGHT, ad, 5, 16, progress=ad)
            fr(c, "2", "1", 1500, 640, 70, GREEN, ep(t, C["17.d"] + 0.8, 0.4))
            text(c, "de cabeça para baixo", 1380, 800, 26, "black", GREEN, ad)
        selo(c, 1520, 350, ep(t, C["17.e"], 0.5), "POR ISSO INVERTE", PURPLE, -6, 30)
        return
    if sid == "18":
        steps = [("18.a", "1", "CONSERVA", "a primeira", BLUE), ("18.b", "2", "INVERTE", "a segunda", AMBER),
                 ("18.c", "3", "MULTIPLICA", "cima × cima, baixo × baixo", PURPLE)]
        for k, (cue, n_, s, sub, col) in enumerate(steps):
            a, d = rise(t, C[cue])
            x = 420 + k * 540
            if a <= 0:
                continue
            rrect(c, x - 240, 220 + d, 480, 280, 24, mix("#FFFFFF", col, 0.10), a)
            badge_num(c, n_, x, 270 + d, a, 28, bg=col)
            text(c, s, x, 380 + d, 50, "black", col, a)
            text(c, sub, x, 440 + d, 28, "bold", INK2, a)
        ad = ep(t, C["18.d"], 0.5)
        if ad > 0:
            boxed(c, 300, 560, 1320, 220, BLUE, ad, 0.06)
            text(c, "INVERSO = trocar o de cima com o de baixo", 960, 610, 32, "black", BLUE, ad)
            expr(c, "2/5 → 5/2", 960, 700, 66, ad, cores={2: AMBER})
        return
    if sid == "19":
        a0 = ep(t, C["19"], 0.5)
        copo(c, 240, 760, 220, 480, 0.75, a0)
        text(c, "3/4 de litro", 350, 810, 28, "black", INK2, a0)
        ae = ep(t, C["19.e"], 0.5)
        hc = 480 * 0.4
        copo(c, 540, 760, 140, hc, 1.0 if ae > 0.3 else 0.0, a0)
        copo(c, 720, 760, 140, hc, 7 / 8 if ae > 0.6 else 0.0, ae)
        text(c, "copo de 2/5", 610, 540, 26, "black", INK2, a0)
        text(c, "1 copo e 7/8", 700, 810, 28, "black", GREEN, ae)
        X = 1280
        expr(c, "3/4 ÷ 2/5", X, 270, 72, ep(t, C["19.a"], 0.5))
        ab = ep(t, C["19.b"], 0.5)
        expr(c, "= 3/4 · 5/2", X, 410, 72, ab, cores={1: BLUE, 3: AMBER})
        if ab > 0:
            text(c, "conserva", X - 40, 520, 22, "black", BLUE, ab)
            text(c, "inverte", X + 150, 520, 22, "black", AMBER, ab)
        acc = ep(t, C["19.c"], 0.5)
        fmid(c, "3 · 5 = 15    4 · 2 = 8", X, 580, 36, "bold", INK2, acc)
        ad = ep(t, C["19.d"], 0.5)
        expr(c, "= 15/8 = 1|7/8", X, 700, 72, ad, cores={1: GREEN, 3: GREEN}, alfas={2: ae, 3: ae})
        pill(c, "quase 2 copos: faz sentido!", X, 800, GREEN, size=26, a=ep(t, C["19.e"] + 1.5, 0.4), anchor="center",
             bounds=(0, 1920))
        return
    # 20 atalho
    aa = ep(t, C["20.a"], 0.5)
    expr(c, "4/9 ÷ 2/3 = 4/9 · 3/2", 960, 260, 64, aa, cores={5: AMBER})
    ab = ep(t, C["20.b"], 0.5)
    s = 110
    cut = ep(t, C["20.b"] + 0.8, 0.6)
    cfrac(c, "4", "9", 560, 470, s, ab, cut_n=cut, cut_d=cut, new_n="2", new_d="3")
    fmid(c, "·", 720, 490, 80, "black", INK, ab)
    cfrac(c, "3", "2", 880, 470, s, ab, cut_n=cut, cut_d=cut, new_n="1", new_d="1")
    expr(c, "= 2/3 · 1/1 = 2/3", 1350, 520, 64, ep(t, C["20.b"] + 2.2, 0.5), cores={4: GREEN})
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        boxed(c, 420, 680, 1080, 110, RED, acc, 0.10)
        check_icon(c, 490, 735, 26, acc, RED, "x")
        text_mid(c, "NUNCA corte antes de inverter", 1000, 735, 38, "black", RED, acc)


# ======================================================================
# bloco E — potência
# ======================================================================

def b_potencia(c, t, C, B):
    head_seq(c, t, C, [("21", "POTÊNCIA DE FRAÇÃO", "O EXPOENTE VAI NOS DOIS", PURPLE),
                       ("22", "ATALHO", "CIMA E BAIXO SEPARADOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["21", "22"])
    if sid == "21":
        aa = ep(t, C["21.a"], 0.5)
        expr(c, "(2/3)^3", 460, 470, 150, aa)
        ab = ep(t, C["21.b"], 0.5)
        if ab > 0:
            arrow(c, 700, 360, 900, 330, PURPLE, ab, 5, 16, progress=ab)
            arrow(c, 700, 420, 900, 520, PURPLE, ab, 5, 16, progress=ep(t, C["21.b"] + 0.4, 0.4))
            text(c, "expoente = o numerozinho no alto", 460, 720, 28, "black", BLUE, ab)
        fmid(c, "2^3 = 2 · 2 · 2 = 8", 1300, 320, 54, "black", INK, ep(t, C["21.c"], 0.5))
        fmid(c, "3^3 = 3 · 3 · 3 = 27", 1300, 500, 54, "black", INK, ep(t, C["21.d"], 0.5))
        ae = ep(t, C["21.e"], 0.5)
        expr(c, "(2/3)^3 = 8/27", 1300, 680, 70, ae, cores={2: GREEN})
        return
    aa = ep(t, C["22.a"], 0.5)
    fmid(c, "em cima: 2^3 = 8", 600, 250, 40, "black", PURPLE, aa)
    fmid(c, "embaixo: 3^3 = 27", 1320, 250, 40, "black", PURPLE, ep(t, C["22.a"] + 0.6, 0.4))
    ab = ep(t, C["22.b"], 0.5)
    pill(c, "fração menor que 1, elevada a uma potência: fica MENOR", W / 2, 350, GREEN, size=28, a=ab, anchor="center",
         bounds=(0, 1920))
    acc = ep(t, C["22.c"], 0.5)
    x0, x1, yr = 380, 1540, 560
    reta(c, x0, x1, yr, acc, [(2 / 3, "2/3", PURPLE, acc), (8 / 27, "8/27", GREEN, ep(t, C["22.c"] + 1.0, 0.4))])
    if acc > 0:
        xt = lerp(x0, x1, 1 / 3)
        line(c, xt, yr - 18, xt, yr + 18, GRAY, acc, 4)
        fr(c, 1, 3, xt, yr + 74, 28, GRAY, acc)
    ad = ep(t, C["22.d"], 0.5)
    if ad > 0:
        boxed(c, 380, 690, 1160, 120, AMBER, ad, 0.14)
        text(c, "PEGADINHA", 520, 760, 26, "black", AMBER, ad, tracking=1)
        expr(c, "2^3/3 = 8/3", 900, 750, 52, ad, cores={0: RED, 2: RED})
        text(c, "maior que 2!", 1300, 762, 32, "black", RED, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("23", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("24", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    a1, a2 = ep(t, C["23.a"], 0.5), ep(t, C["23.b"], 0.5)
    for k, (a, s) in enumerate(((a1, "2/3 + 1/4"), (a2, "5/6 ÷ 1/3"))):
        x = 560 + k * 800
        if a <= 0:
            continue
        rrect(c, x - 330, 210, 660, 240, 24, "#F7F7F5", a)
        text(c, "1ª CONTA" if k == 0 else "2ª CONTA", x, 260, 24, "black", GRAY, a, tracking=1)
        expr(c, s + " = ?", x, 370, 72, a)
    pause_timer(c, t, C["23.end"] - 1.9, W / 2, 560)
    if t >= C["24"]:
        ra = ep(t, C["24.a"], 0.5)
        fmid(c, "MMC(3, 4) = 12", 560, 510, 34, "black", PURPLE, ra)
        expr(c, "8/12 + 3/12", 560, 610, 52, ra)
        expr(c, "= 11/12", 560, 730, 60, ep(t, C["24.b"], 0.5), cores={1: GREEN})
        rc = ep(t, C["24.c"], 0.5)
        expr(c, "5/6 · 3/1", 1360, 560, 52, rc, cores={2: AMBER})
        expr(c, "= 15/6 = 5/2", 1360, 690, 60, ep(t, C["24.d"], 0.5), cores={3: GREEN})
        pill(c, "5/2 = 2,5: o 1/3 cabe duas vezes e meia", 1360, 795, GREEN, size=24, a=ep(t, C["24.e"], 0.5),
             anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Somar e subtrair: mesmo denominador antes, pelo MMC.", "Multiplicar: corte em cruz antes, multiplique depois.",
          "Dividir: conserva a primeira, inverte a segunda."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["25", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "25" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Somar em cima com em cima e embaixo com embaixo: 1/2 + 1/3 = 2/5", "na multiplicação é exatamente assim",
          "na soma, primeiro o mesmo tamanho de fatia: o MMC (1/2 + 1/3 = 5/6)"),
         ("Na divisão, inverter a PRIMEIRA fração", "você lembra que tem que inverter alguma coisa",
          "a primeira se conserva: quem inverte é a segunda"),
         ("Multiplicar sem simplificar e se perder em números enormes", "a resposta até sai igual",
          "número grande é conta errada esperando para acontecer: corte em cruz antes")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["26", "27", "28"], ERROS)


# ======================================================================
# questão 9
# ======================================================================

ALTS = [("A", "= 1/6", "só a turma A", RED), ("B", "= 1/4", "", GREEN), ("C", "= 1/3", "só a turma C", RED),
        ("D", "= 3/4", "é o que já foi ARRECADADO", AMBER), ("E", "= 1/13", "13 = 6 + 4 + 3: somou os denominadores", RED)]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A CAMPANHA DAS TRÊS TURMAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.5)
    rows = [("29.a", "Três turmas participaram de uma campanha de arrecadação."),
            ("29.b", "A turma A arrecadou 1/6 da meta, a turma B arrecadou 1/4 e a turma C, 1/3."),
            ("29.c", "Que fração da meta ainda falta arrecadar?")]
    y = 240
    for cue, s in rows:
        a = ep(t, C[cue], 0.4)
        y += para(c, s, 190, y, 30, "black" if cue != "29.c" else "bold", INK if cue != "29.c" else BLUE, a, 580, 38) + 14
    text(c, "Questão do material de estudo, no estilo ENEM.", 190, 830, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"30.{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["32.xa"], "C": C["32.xa"] + 0.4, "D": C["32.xd"], "E": C["32.xe"]}
    if t >= C["30"] - 0.3:
        K.alternativas(c, t, C, ALTS, 870, 205, 820, 42, C["31.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["30.end"] - 1.9, 470, 720)
    ra = ep(t, C["31.a"], 0.4) * (1 - ep(t, C["32"], 0.4))
    if ra > 0:
        rrect(c, 170, 540, 620, 268, 18, "#FFFFFF", ra, shadow=True)
        text(c, "arrecadado", 480, 580, 22, "black", GRAY, ra)
        expr(c, "2/12 + 3/12 + 4/12 = 3/4", 480, 640, 38, ep(t, C["31.b"], 0.4), cores={6: PURPLE})
        text(c, "falta", 480, 715, 22, "black", GRAY, ep(t, C["31.c"], 0.4))
        expr(c, "1 − 3/4 = 1/4", 480, 770, 44, ep(t, C["31.d"], 0.4), cores={4: GREEN})
    result_box(c, "Letra B", 470, 690, 50, ep(t, C["32"], 0.5), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A ARMADILHA DO “DO RESTANTE”", AMBER)
    aa = ep(t, C["34.a"], 0.5)
    pizza(c, 460, 470, 190, 3, {0}, aa, gone={0} if t > C["34.b"] else None)
    fr(c, "1", "3", 460, 720, 40, INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        selo(c, 1220, 420, ab, "“DO RESTANTE”", AMBER, -5, 64)
        text(c, "duas palavras que derrubam quase todo mundo", 1220, 580, 32, "black", INK2, ab)
    pill(c, "ep. 4 · a armadilha do “do restante”", 1220, 720, PURPLE, size=32, a=ep(t, C["34.c"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Você já tinha caído no 1/2 + 1/3 = 2/5?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, prova=b_prova, soma=b_soma, mult=b_mult, div=b_div,
              potencia=b_potencia, exercicio=b_exercicio, recap=b_recap, erros=b_erros, questao=b_questao, ponte=b_ponte,
              cta=b_cta)
