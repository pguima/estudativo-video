"""Visual — Razão, Proporção e Regra de Três, Episódio 1: Razão (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, fichas, alternativas, erro_cards...).
Peças deste episódio: copo(), boneco(), ônibus, ícones das taxas e a seta do "para".
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
_s = importlib.util.spec_from_file_location("comum021", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_razao_ep1_razao.mp4"
CARD_R = K.CARD_R
SUCO = "#F08A24"
AGUA = "#7CC3EA"
PE = "#E8743B"      # pessoas em pé
SENT = "#3E7BFA"    # pessoas sentadas
MULHER = "#D9468F"


# ======================================================================
# peças do episódio
# ======================================================================

def copo(c, x, y, w, h, col, a=1.0, nivel=0.85):
    """copo (trapézio) com líquido; (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    inset = w * 0.12
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w - inset, y + h); p.lineTo(x + inset, y + h); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    top = y + h * (1 - nivel)
    k = (top - y) / h
    q = skia.Path()
    q.moveTo(x + inset * k, top); q.lineTo(x + w - inset * k, top); q.lineTo(x + w - inset, y + h); q.lineTo(x + inset, y + h); q.close()
    c.drawPath(q, paint(col, a * 0.9))
    c.drawPath(p, paint(INK2, a, stroke=4, cap_round=True))


def boneco(c, cx, cy, s, col, a=1.0):
    """bonequinho: cabeça + corpo arredondado; (cx, cy) = centro do corpo; s = altura total"""
    if a <= 0:
        return
    r = s * 0.17
    c.drawCircle(cx, cy - s * 0.30, r, paint(col, a))
    rrect(c, cx - s * 0.22, cy - s * 0.10, s * 0.44, s * 0.48, s * 0.18, col, a)


def onibus(c, x, y, a, n_sent, n_pe, a_pe=1.0, hl_pe=0.0, hl_sent=0.0, s=34):
    """ônibus com n_sent sentados (grade) e n_pe em pé (fileira de cima); (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    w, h = 1000, 330
    rrect(c, x, y, w, h, 40, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 40, 40), paint("#D4D4CF", a, stroke=5))
    for k in range(6):
        rrect(c, x + 60 + k * 150, y + 30, 120, 70, 12, "#EAF3FB", a)
    for cx_ in (x + 190, x + w - 190):
        c.drawCircle(cx_, y + h, 42, paint(INK, a))
        c.drawCircle(cx_, y + h, 16, paint("#C9C9C4", a))
    # em pé: na frente das janelas
    for i in range(n_pe):
        boneco(c, x + 120 + i * 125, y + 82, s * 1.6, PE, a * a_pe)
    # sentados: 3 fileiras de 7
    for i in range(n_sent):
        r_, k = divmod(i, 7)
        boneco(c, x + 120 + k * 125, y + 160 + r_ * 52, s, SENT, a)


def seta_para(c, x_word, y_word, w_word, x_den, y_den, a, col=PURPLE):
    """sublinha a palavra que vem depois do 'para' e leva uma seta até o denominador"""
    if a <= 0:
        return
    line(c, x_word, y_word + 14, x_word + w_word * a, y_word + 14, col, 1.0, 6)
    if a > 0.5:
        u = (a - 0.5) / 0.5
        x0, y0 = x_word + w_word / 2, y_word + 24
        p = skia.Path(); p.moveTo(x0, y0)
        p.quadTo((x0 + x_den) / 2, max(y0, y_den) + 90, x0 + (x_den - x0) * u, y0 + (y_den - y0) * u)
        c.drawPath(p, paint(col, u, stroke=5, cap_round=True))
        if u > 0.95:
            ang = math.atan2(y_den - (max(y0, y_den) + 90), x_den - (x0 + x_den) / 2)
            for s_ in (-1, 1):
                c.drawLine(x_den, y_den, x_den - 18 * math.cos(ang + s_ * 0.5), y_den - 18 * math.sin(ang + s_ * 0.5),
                           paint(col, u, stroke=5, cap_round=True))


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ---------- ícones das taxas (desenhados em vetor) ----------

def ic_velocimetro(c, cx, cy, a):
    pe = paint(INK, a, stroke=7, cap_round=True)
    c.drawArc(skia.Rect.MakeXYWH(cx - 60, cy - 50, 120, 120), 180, 180, False, pe)
    for k in range(5):
        ang = math.pi + k * math.pi / 4
        c.drawLine(cx + 46 * math.cos(ang), cy + 10 + 46 * math.sin(ang), cx + 58 * math.cos(ang), cy + 10 + 58 * math.sin(ang),
                   paint(INK, a, stroke=4))
    ang = math.pi * 1.7
    c.drawLine(cx, cy + 10, cx + 44 * math.cos(ang), cy + 10 + 44 * math.sin(ang), paint(RED, a, stroke=6, cap_round=True))
    c.drawCircle(cx, cy + 10, 8, paint(INK, a))


def ic_balanca(c, cx, cy, a):
    pe = paint(INK, a, stroke=6, cap_round=True)
    c.drawLine(cx, cy - 45, cx, cy + 40, pe)
    c.drawLine(cx - 55, cy - 35, cx + 55, cy - 35, pe)
    c.drawLine(cx - 30, cy + 42, cx + 30, cy + 42, pe)
    for s_ in (-1, 1):
        x = cx + s_ * 55
        c.drawLine(x, cy - 35, x - 18, cy + 5, paint(INK, a, stroke=3)); c.drawLine(x, cy - 35, x + 18, cy + 5, paint(INK, a, stroke=3))
        c.drawArc(skia.Rect.MakeXYWH(x - 24, cy - 10, 48, 28), 0, 180, True, paint(AMBER, a))


def ic_mapa(c, cx, cy, a):
    pts = [(-60, -35), (-20, -48), (20, -35), (60, -48), (60, 40), (20, 52), (-20, 40), (-60, 52)]
    p = skia.Path(); p.moveTo(cx + pts[0][0], cy + pts[0][1])
    for x, y in pts[1:]:
        p.lineTo(cx + x, cy + y)
    p.close()
    c.drawPath(p, paint("#DDEFD9", a)); c.drawPath(p, paint(INK, a, stroke=4))
    c.drawLine(cx - 20, cy - 48, cx - 20, cy + 40, paint(INK, a * 0.6, stroke=3))
    c.drawLine(cx + 20, cy - 35, cx + 20, cy + 52, paint(INK, a * 0.6, stroke=3))
    c.drawCircle(cx + 5, cy - 8, 12, paint(RED, a)); c.drawCircle(cx + 5, cy - 8, 4, paint("#FFFFFF", a))


def ic_pessoas(c, cx, cy, a):
    for k, dx in enumerate((-38, 0, 38)):
        boneco(c, cx + dx, cy + (6 if k != 1 else -4), 64, [SENT, PE, MULHER][k], a)
    line(c, cx - 64, cy + 48, cx + 64, cy + 48, INK2, a, 4)


def ic_bomba(c, cx, cy, a):
    rrect(c, cx - 38, cy - 48, 60, 100, 10, GREEN, a)
    rrect(c, cx - 28, cy - 38, 40, 28, 6, "#FFFFFF", a)
    p = skia.Path(); p.moveTo(cx + 22, cy - 20); p.quadTo(cx + 55, cy - 20, cx + 50, cy + 20); p.lineTo(cx + 50, cy + 35)
    c.drawPath(p, paint(INK, a, stroke=5, cap_round=True))
    rrect(c, cx - 48, cy + 50, 80, 10, 4, INK, a)


def ic_torneira(c, cx, cy, a):
    rrect(c, cx - 60, cy - 30, 70, 26, 8, INK2, a)
    p = skia.Path(); p.moveTo(cx + 10, cy - 30); p.quadTo(cx + 45, cy - 30, cx + 45, cy + 5)
    c.drawPath(p, paint(INK2, a, stroke=22, cap_round=False))
    rrect(c, cx - 38, cy - 52, 26, 22, 6, INK, a)
    for k in range(3):
        c.drawCircle(cx + 45, cy + 26 + k * 18, 6 - k, paint(AGUA, a))


def ic_etiqueta(c, cx, cy, a):
    p = skia.Path(); p.moveTo(cx - 55, cy - 30); p.lineTo(cx + 30, cy - 30); p.lineTo(cx + 60, cy); p.lineTo(cx + 30, cy + 30)
    p.lineTo(cx - 55, cy + 30); p.close()
    c.drawPath(p, paint(AMBER, a)); c.drawCircle(cx + 32, cy, 7, paint("#FFFFFF", a))
    fmid(c, "R$", cx - 15, cy, 30, "black", "#FFFFFF", a)


# ======================================================================
# abertura
# ======================================================================

TEMAS = [("velocidade", "km/h"), ("escala", "1 : 50 000"), ("densidade", "g/cm³"), ("câmbio", "R$/US$"), ("consumo", "km/L")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "RAZÃO EM TODO LUGAR", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 190, 1000, 110, BLUE, aa, 0.08)
        text_mid(c, "UM único assunto para levar ao ENEM?", W / 2, 245, 42, "black", INK, aa)
    ac = ep(t, C["01.c"], 0.5)
    for k, (nome, u) in enumerate(TEMAS):
        a = ep(t, C["01.b"] + 0.45 * k, 0.4)
        if a <= 0:
            continue
        x = 300 + k * 330
        card(c, x - 145, 360, 290, 220, a)
        text(c, nome, x, 440, 34, "black", INK, a)
        ftext(c, u, x, 520, 38, "black", PURPLE, a * ac)
    if ac > 0:
        text(c, "tudo é RAZÃO: alguma coisa ÷ outra", W / 2, 650, 40, "black", PURPLE, ac)
    ad = ep(t, C["01.d"], 0.5)
    selo(c, W / 2, 770, ad, "REGRA DE TRÊS: A FERRAMENTA QUE MAIS RESOLVE", GREEN, -2, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "montar qualquer razão na ordem certa", "o que vem depois do “para” vai embaixo"),
            ("02.b", "achar as razões escondidas", "velocidade, densidade, preço por quilo…")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "DA SÉRIE DE FRAÇÕES", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "SIMPLIFICAR = ÷ em cima e embaixo pelo mesmo", 560, 260, 28, "black", BLUE, aa)
        expr(c, "6/8 = 3/4", 560, 450, 100, aa, cores={2: GREEN})
        chip(c, "÷ 2 nos dois", 560, 610, GREEN, aa, 30)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "O MESMO NÚMERO, TRÊS JEITOS", 1360, 260, 28, "black", BLUE, ab)
        expr(c, "3/4 = 0,75 = 75%", 1360, 450, 76, ab, cores={0: INK, 2: PURPLE, 4: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)


# ======================================================================
# bloco A — o suco e a definição
# ======================================================================

def b_suco(c, t, C, B):
    frame(c, t, B["start"], "A RECEITA DO SUCO", "1 PARA 3", BLUE)
    a0 = ep(t, C["04"], 0.5)
    copo(c, 260, 300, 150, 210, SUCO, a0)
    text(c, "concentrado", 335, 570, 30, "black", SUCO, a0)
    for k in range(3):
        copo(c, 560 + k * 190, 300, 150, 210, AGUA, ep(t, C["04"] + 0.3 + 0.25 * k, 0.4))
    text(c, "água", 845, 570, 30, "black", mix(AGUA, INK, 0.4), a0)
    fmid(c, "para", 485, 405, 30, "black", INK2, a0)
    aa = ep(t, C["04.a"], 0.5) * (1 - ep(t, C["04.b"], 0.4))
    fmid(c, "?", 1360, 400, 140, "black", AMBER, aa)
    ab = ep(t, C["04.b"], 0.5)
    chip(c, "COMPARA duas quantidades", 1360, 270, BLUE, ab, 32)
    acc = ep(t, C["04.c"], 0.5)
    expr(c, "1 ÷ 3 = 1/3", 1360, 420, 90, acc, cores={4: PURPLE})
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        boxed(c, 1010, 520, 700, 100, BLUE, ad, 0.08)
        text_mid(c, "RAZÃO = comparação por divisão", 1360, 570, 34, "black", BLUE, ad)
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        x0, x1 = 560, 1130
        line(c, x0, 620, x1, 620, GREEN, ae, 4)
        line(c, x0, 620, x0, 605, GREEN, ae, 4); line(c, x1, 620, x1, 605, GREEN, ae, 4)
        text(c, "o concentrado cabe 3 VEZES na água", 845, 680, 32, "black", GREEN, ae)


def b_definicao(c, t, C, B):
    frame(c, t, B["start"], "NO GERAL", "A RAZÃO ENTRE a E b", BLUE)
    a0 = ep(t, C["05"], 0.5)
    expr(c, "a/b", 700, 440, 220, a0, cores={0: PURPLE})
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 470, 690, 460, 90, AMBER, aa, 0.10)
        ftext(c, "b ≠ 0: não existe ÷ 0", 700, 748, 34, "black", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        arrow(c, 1080, 330, 790, 340, BLUE, ab, 5, 16, progress=ab)
        text(c, "ANTECEDENTE", 1300, 320, 40, "black", BLUE, ab)
        text(c, "vem antes · fica em cima", 1300, 370, 28, "bold", INK2, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        arrow(c, 1080, 560, 790, 545, PURPLE, acc, 5, 16, progress=acc)
        text(c, "CONSEQUENTE", 1300, 560, 40, "black", PURPLE, acc)
        text(c, "vem depois · fica embaixo", 1300, 610, 28, "bold", INK2, acc)


# ======================================================================
# bloco B — a ordem importa
# ======================================================================

def b_ordem(c, t, C, B):
    frame(c, t, B["start"], "A ORDEM IMPORTA?", "O “PARA” DECIDE", PURPLE)
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    text(c, "concentrado PARA água", 300, 300, 40, "black", INK, aa, align="left")
    expr(c, "= 1/3", 1100, 285, 70, aa, cores={1: PURPLE})
    text(c, "água PARA concentrado", 300, 470, 40, "black", INK, ab, align="left")
    expr(c, "= 3/1 = 3", 1100, 455, 70, ab, cores={3: AMBER})
    acc = ep(t, C["06.c"], 0.5)
    selo(c, 1520, 380, acc, "DIFERENTES!", RED, -6, 34)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        # a seta do "para" sobre a primeira linha: "água" vai para o denominador do 1/3
        xw = 300 + text_w("concentrado PARA ", "black", 40)
        seta_para(c, xw, 300, text_w("água", "black", 40), 1140, 315, ep(t, C["06.d"], 1.2))
        regra(c, "o que vem depois de “para” vai EMBAIXO", W / 2, 640, ad, 40)
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        text(c, "razão ENTRE a E b  =", 760, 775, 34, "black", INK2, ae, align="right")
        expr(c, "a/b", 830, 760, 54, ae, cores={0: PURPLE})
        text(c, "o primeiro em cima", 900, 775, 30, "bold", INK2, ae, align="left")


def b_onibus(c, t, C, B):
    head_seq(c, t, C, [("07", "NO ÔNIBUS", "EM PÉ PARA SENTADAS", BLUE), ("08", "MUDEI UMA PALAVRA", "EM PÉ PARA O TOTAL", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    a0 = ep(t, C["07"], 0.5)
    n_sent = 21 if t >= C["07.a"] else 0
    a_pe = ep(t, C["07.b"], 0.5)
    onibus(c, 200, 230, a0, n_sent, 7, a_pe, 1.0, 1.0)
    text(c, "21 sentadas", 450, 640, 32, "black", SENT, ep(t, C["07.a"], 0.4))
    text(c, "7 em pé", 900, 640, 32, "black", PE, a_pe)
    if sid == "07":
        acc = ep(t, C["07.c"], 0.5)
        text(c, "em pé PARA as sentadas", 1450, 290, 32, "black", INK, acc)
        ad = ep(t, C["07.d"], 0.5)
        expr(c, "7/21", 1450, 430, 96, ad, cores={0: INK})
        if ad > 0:
            text(c, "as sentadas vão embaixo", 1450, 545, 26, "bold", INK2, ad)
        ae = ep(t, C["07.e"], 0.5)
        expr(c, "= 1/3", 1450, 650, 80, ae, cores={1: PURPLE})
        text(c, "÷ 7 nos dois", 1450, 760, 26, "bold", GREEN, ae)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        line(c, 210, 690, 1190, 690, AMBER, aa, 5)
        line(c, 210, 690, 210, 670, AMBER, aa, 5); line(c, 1190, 690, 1190, 670, AMBER, aa, 5)
        expr(c, "total: 21 + 7 = 28", 700, 750, 40, aa, cores={4: AMBER})
    text(c, "em pé PARA O TOTAL", 1450, 290, 32, "black", AMBER, ep(t, C["08"], 0.5))
    ab = ep(t, C["08.b"], 0.5)
    expr(c, "7/28 = 1/4", 1450, 430, 80, ab, cores={2: AMBER})
    acc = ep(t, C["08.c"], 0.5)
    text(c, "mesmas pessoas, outra resposta", 1450, 540, 26, "bold", INK2, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1240, 580, 420, 200, "ATALHO", ["sublinhe o que vem", "depois do “para”:", "comparado com QUEM?"], ad, 28)


# ======================================================================
# bloco C — as quatro formas
# ======================================================================

FORMAS = [("09.a", "3/4", "fração"), ("09.b", "0,75", "decimal"), ("09.c", "75%", "porcentagem"), ("09.d", "3 : 4", "“três para quatro”")]


def b_formas(c, t, C, B):
    frame(c, t, B["start"], "A MESMA RAZÃO", "QUATRO JEITOS DE ESCREVER", BLUE)
    for k, (cue, s, nome) in enumerate(FORMAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 340 + k * 413
        card(c, x - 170, 260 + d, 340, 300, a)
        expr(c, s, x, 390 + d, 90, a, cores={0: [PURPLE, BLUE, GREEN, AMBER][k]})
        text(c, nome, x, 510 + d, 30, "black", INK2, a)
        if k > 0:
            fmid(c, "=", x - 206, 410, 60, "black", GRAY, a)
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        K.pizza(c, 560, 700, 90, 4, 3, ae)
        text(c, "as quatro dizem a MESMA coisa", 700, 715, 40, "black", PURPLE, ae, align="left")


# ======================================================================
# bloco D — número puro × taxa
# ======================================================================

def b_taxa(c, t, C, B):
    head_seq(c, t, C, [("10", "NÚMERO PURO OU TAXA?", "A UNIDADE DECIDE", BLUE), ("11", "A ETIQUETA DO MERCADO", "TAXA E VALOR UNITÁRIO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        text(c, "MESMA ESPÉCIE", 560, 250, 28, "black", BLUE, aa)
        for k in range(3):
            boneco(c, 440 + k * 60, 340, 70, PE, aa)
        for k in range(3):
            boneco(c, 440 + k * 60, 470, 70, SENT, aa)
        line(c, 380, 405, 740, 405, INK, aa, 5)
        text(c, "pessoas", 860, 355, 30, "black", INK2, aa, align="left")
        text(c, "pessoas", 860, 485, 30, "black", INK2, aa, align="left")
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            strike(c, 850, 345, 990, 345, ab, RED, ab); strike(c, 850, 475, 990, 475, ab, RED, ab)
            boxed(c, 300, 600, 520, 130, BLUE, ab, 0.08)
            text(c, "NÚMERO PURO", 560, 655, 36, "black", BLUE, ab)
            text(c, "sem unidade nenhuma", 560, 700, 26, "bold", INK2, ab)
        line(c, 1060, 230, 1060, 800, "#E6E6E2", ep(t, C["10.c"], 0.4), 3)
        acc = ep(t, C["10.c"], 0.5)
        text(c, "ESPÉCIES DIFERENTES", 1400, 250, 28, "black", PURPLE, acc)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            fr(c, "100 metros", "20 segundos", 1400, 410, 56, INK, ad)
        ae = ep(t, C["10.e"], 0.5)
        if ae > 0:
            ftext(c, "= 5 m/s", 1400, 590, 64, "black", PURPLE, ae)
            boxed(c, 1170, 640, 460, 110, PURPLE, ae, 0.08)
            text(c, "TAXA", 1400, 690, 36, "black", PURPLE, ae)
            text(c, "razão com unidade", 1400, 732, 26, "bold", INK2, ae)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        p = skia.Path(); x0, y0 = 250, 270
        p.moveTo(x0, y0); p.lineTo(x0 + 440, y0); p.lineTo(x0 + 540, y0 + 110); p.lineTo(x0 + 440, y0 + 220); p.lineTo(x0, y0 + 220); p.close()
        c.save(); c.translate(x0 + 270, y0 + 110); c.rotate(-4); c.translate(-(x0 + 270), -(y0 + 110))
        c.drawPath(p, paint(AMBER, aa)); c.drawCircle(x0 + 445, y0 + 110, 16, paint("#FFFFFF", aa))
        text(c, "CARNE", x0 + 210, y0 + 70, 30, "black", "#FFFFFF", aa)
        text(c, "R$ 30,00", x0 + 210, y0 + 140, 56, "black", "#FFFFFF", aa)
        text(c, "pacote de 2 kg", x0 + 210, y0 + 190, 28, "bold", "#FFFFFF", aa)
        c.restore()
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        fr(c, "R$ 30", "2 kg", 1180, 360, 70, INK, ab)
        ftext(c, "= R$ 15/kg", 1470, 380, 56, "black", GREEN, ab, align="left")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 560, 640, 150, BLUE, acc, 0.08)
        text(c, "VALOR UNITÁRIO", 620, 620, 36, "black", BLUE, acc)
        text(c, "quanto custa UMA unidade", 620, 668, 28, "bold", INK2, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1040, 540, 600, 200, "ATALHO", ["leia o “por” como", "“dividido por”: R$ ÷ kg"], ad, 32)


# ======================================================================
# bloco E — o passeio das taxas
# ======================================================================

PASSEIO = [("12.a", ic_velocimetro, "velocidade", "distância", "tempo", "km/h · m/s"),
           ("12.b", ic_balanca, "densidade", "massa", "volume", "g/cm³"),
           ("12.c", ic_mapa, "escala", "desenho", "real", "1 : n"),
           ("12.d", ic_pessoas, "dens. demográfica", "habitantes", "área", "hab/km²"),
           ("13.a", ic_bomba, "rendimento", "distância", "combustível", "km/L"),
           ("13.b", ic_torneira, "vazão", "volume", "tempo", "L/s"),
           ("13.c", ic_etiqueta, "custo unitário", "preço", "quantidade", "R$/kg")]


def b_passeio(c, t, C, B):
    frame(c, t, B["start"], "O PASSEIO DAS TAXAS", "TUDO É ALGO ÷ ALGO", PURPLE)
    for k, (cue, ic, nome, num, den, u) in enumerate(PASSEIO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        row, col = divmod(k, 4)
        x = W / 2 + (col - 1.5) * 395
        y = 200 + row * 300 + d
        card(c, x - 180, y, 360, 280, a)
        text(c, nome, x, y + 48, 28, "black", INK, a)
        ic(c, x - 100, y + 140, a)
        fr(c, num, den, x + 70, y + 140, 32, PURPLE, a)
        pill(c, u, x, y + 240, BLUE, size=22, a=a, anchor="center", bounds=(0, 1920))
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        x = W / 2 + 1.5 * 395
        boxed(c, x - 180, 540, 360, 200, AMBER, ae, 0.10)
        text(c, "converter unidades", x, 610, 28, "black", INK, ae)
        text(c, "e calcular escalas:", x, 650, 28, "black", INK, ae)
        text(c, "séries próprias", x, 700, 30, "black", AMBER, ae)
    ad = ep(t, C["13.d"], 0.5)
    pill(c, "a mesma cara: ALGUMA COISA ÷ OUTRA", W / 2, 830, PURPLE, size=28, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco F — razões encadeadas
# ======================================================================

def _elo(c, x, y, s, col, a):
    card(c, x - 150, y - 70, 300, 140, a)
    ftext(c, s, x, y + 16, 52, "black", col, a)


def b_encadeada(c, t, C, B):
    head_seq(c, t, C, [("14", "UMA RAZÃO NÃO BASTA", "RAZÕES ENCADEADAS", BLUE), ("15", "ATALHO", "SIGA AS UNIDADES", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.5)
    fa, fb = ep(t, C["14.a"], 0.5), ep(t, C["14.b"], 0.5)
    chip(c, "10 km por litro", 500, 250, BLUE, fa, 30)
    chip(c, "R$ 6 o litro", 960, 250, AMBER, fb, 30)
    chip(c, "viagem: 150 km?", 1420, 250, PURPLE, ep(t, C["14.c"], 0.5), 30)
    ad, ae = ep(t, C["14.d"], 0.5), ep(t, C["14.e"], 0.5)
    _elo(c, 360, 430, "150 km", INK, ep(t, C["14.c"], 0.5))
    if ad > 0:
        arrow(c, 520, 430, 800, 430, BLUE, ad, 5, 16, progress=ad)
        ftext(c, "÷ 10 km/L", 660, 390, 30, "black", BLUE, ad)
        _elo(c, 960, 430, "15 L", BLUE, ad)
    if ae > 0:
        arrow(c, 1120, 430, 1400, 430, AMBER, ae, 5, 16, progress=ae)
        ftext(c, "× R$ 6/L", 1260, 390, 30, "black", AMBER, ae)
        _elo(c, 1560, 430, "R$ 90", GREEN, ae)
    if t < C["15"]:
        text(c, "1ª etapa: os litros", 660, 560, 28, "bold", INK2, ad)
        text(c, "2ª etapa: o preço", 1260, 560, 28, "bold", INK2, ae)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 560, 1400, 250, GREEN, aa, 0.06)
        text(c, "ATALHO · SIGA AS UNIDADES", W / 2, 605, 24, "black", GREEN, aa, tracking=2)
        ftext(c, "km ÷ km/L  =  litros", W / 2, 670, 40, "black", INK, ep(t, C["15.b"], 0.5))
        ftext(c, "litros × R$/L  =  reais", W / 2, 735, 40, "black", INK, ep(t, C["15.c"], 0.5))
        text(c, "unidade final ≠ a pedida? falta uma etapa", W / 2, 790, 28, "black", AMBER, ep(t, C["15.d"], 0.5))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E ESCREVA", GREEN), ("17", "VAMOS CONFERIR", "PAUSE E ESCREVA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    for i in range(20):
        r_, k = divmod(i, 10)
        boneco(c, 230 + k * 62, 290 + r_ * 100, 70, MULHER, aa * ep(t, C["16.a"] + 0.03 * i, 0.3))
    for k in range(5):
        boneco(c, 230 + k * 62, 500, 70, SENT, aa * ep(t, C["16.a"] + 0.8 + 0.08 * k, 0.3))
    text(c, "20 mulheres", 1000, 310, 30, "black", MULHER, aa, align="left")
    text(c, "5 homens", 600, 510, 30, "black", SENT, aa, align="left")
    q = [("16.b", "homens PARA mulheres", "5/20 = 1/4", "17.a"), ("16.c", "mulheres PARA o total", "20/25 = 4/5", "17.b")]
    for j, (cue, s, r, rc) in enumerate(q):
        a = ep(t, C[cue], 0.5)
        y = 630 + j * 120
        text(c, f"{j + 1}.  {s}", 230, y, 34, "black", INK, a, align="left")
        if t >= C["17"]:
            ra = ep(t, C[rc], 0.5)
            expr(c, r, 1000, y - 12, 46, ra, cores={2: GREEN}, align="left")
    pause_timer(c, t, C["16.end"] - 1.9, 1500, 420)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Razão é comparar dividindo.", "O que vem depois de “para” vai embaixo.", "Taxa é razão com unidade."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1340, 58)


ERROS = [("Inverter a razão", "os mesmos dois números estão ali, e a gente escreve na ordem em que lê",
          "a ordem muda o valor: o que vem depois do “para” vai embaixo"),
         ("Usar o outro grupo quando a pergunta é “para o total”", "o outro grupo é o número que está escrito",
          "o total quase nunca está escrito: some os grupos e só depois divida"),
         ("Pular a 1ª etapa: km × preço do litro", "são os dois números grandes do enunciado",
          "km × R$/L não dá reais: primeiro os litros, depois o preço")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=34, w=640):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS1 = [("A", "= 2/3", "meninos para MENINAS", RED), ("B", "= 3/2", "invertida", RED), ("C", "= 2/5", "", GREEN),
         ("D", "= 3/5", "meninas para o total", RED), ("E", "= 5/2", "invertida", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · A ORDEM DOS TERMOS", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    _enunciado(c, [("Em uma turma há 18 meninas e 12 meninos.", INK),
                   ("A razão entre o número de meninos e o número total de alunos da turma é", INK)], a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    if t >= C["22.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS1, 980, 200, 700, 40, C["23.ok"], "C", cues_in, cues_x, gap=12)
    pause_timer(c, t, C["22.end"] - 1.9, 470, 640)
    if t >= C["23"]:
        ra = ep(t, C["23"], 0.4)
        rrect(c, 170, 470, 700, 330, 18, "#FFFFFF", ra, shadow=True)
        text(c, "meninos em cima · TOTAL embaixo", 520, 530, 28, "black", PURPLE, ep(t, C["23.a"], 0.4))
        expr(c, "total = 18 + 12 = 30", 520, 600, 40, ep(t, C["23.b"], 0.4), cores={6: AMBER})
        expr(c, "12/30 = 2/5", 520, 715, 60, ep(t, C["23.c"], 0.4), cores={2: GREEN}, alfas={1: ep(t, C["23.d"], 0.4), 2: ep(t, C["23.d"], 0.4)})


ALTS9 = [("A", "R$ 82,80", "dividiu km pelo preço", RED), ("B", "R$ 232,00", "", GREEN), ("C", "R$ 240,00", "arredondou o litro para R$ 6", RED),
         ("D", "R$ 696,00", "mais de R$ 1 por km", RED), ("E", "R$ 2 784,00", "pulou os litros", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · RAZÃO EM DUAS ETAPAS", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Um automóvel percorre, em média, 12 quilômetros com um litro de combustível, vendido a R$ 5,80 o litro.", INK),
                   ("O custo aproximado do combustível para uma viagem de 480 quilômetros será de", BLUE)], a0, 240, 30, 680)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 980, 220, 700, 38, C["26.ok"], "B", cues_in, cues_x, gap=16)
    pause_timer(c, t, C["25.end"] - 1.9, 470, 680)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 520, 720, 290, 18, "#FFFFFF", ra, shadow=True)
        ftext(c, "1ª: 480 km ÷ 12 km/L = 40 L", 530, 580, 34, "black", BLUE, ep(t, C["26.a"], 0.4))
        ftext(c, "2ª: 40 L × R$ 5,80 = R$ 232", 530, 650, 34, "black", GREEN, ep(t, C["26.b"], 0.4))
        acc = ep(t, C["26.c"], 0.4)
        ftext(c, "bom senso: ≈ R$ 0,50 por km", 530, 725, 28, "black", AMBER, acc)
        ftext(c, "500 km ≈ R$ 250 ✓", 530, 775, 28, "black", AMBER, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PROPORÇÃO", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        for j, (n_s, n_a) in enumerate(((1, 3), (2, 6))):
            x0 = 300 + j * 600
            for k in range(n_s):
                copo(c, x0 + k * 85, 290, 70, 110, SUCO, aa)
            for k in range(n_a):
                copo(c, x0 + (n_s + k) * 85 + 20, 290, 70, 110, AGUA, aa)
    ab = ep(t, C["29.b"], 0.5)
    expr(c, "1/3 = 2/6", W / 2, 540, 110, ab, cores={1: PURPLE})
    text(c, "duas razões IGUAIS = PROPORÇÃO", W / 2, 680, 36, "black", PURPLE, ab)
    pill(c, "ep. 2 · proporção e o truque do k", W / 2, 780, PURPLE, size=32, a=ep(t, C["29.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "Você já tinha invertido uma razão na prova?",
        canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, suco=b_suco, definicao=b_definicao, ordem=b_ordem,
              onibus=b_onibus, formas=b_formas, taxa=b_taxa, passeio=b_passeio, encadeada=b_encadeada,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q9=b_q9, ponte=b_ponte, cta=b_cta)
