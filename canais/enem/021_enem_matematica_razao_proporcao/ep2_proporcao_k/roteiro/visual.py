"""Visual — Razão, Proporção e Regra de Três, Episódio 2: Proporção e o truque do k (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019: expr com frações, atalho, alternativas, erro_cards...).
Peças deste episódio: receita (ovos e xícaras), pontas e miolo em X, pacotinhos de k.
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
ARQUIVO_FINAL = "enem_matematica_razao_ep2_proporcao_k.mp4"
CARD_R = K.CARD_R
GEMA = "#F2B233"
CASCA = "#FFF4DC"
XIC = "#6FA8DC"
CAIXA = "#C98B4B"
PONTA = AMBER
MIOLO = BLUE


# ======================================================================
# peças do episódio
# ======================================================================

def ovo(c, x, y, r, a):
    if a <= 0:
        return
    rect = skia.Rect.MakeXYWH(x - r * 0.78, y - r, r * 1.56, r * 2)
    c.drawOval(rect.makeOffset(3, 5), paint("#000000", 0.08 * a))
    c.drawOval(rect, paint(CASCA, a))
    c.drawOval(rect, paint("#E3C98F", a, stroke=3))
    c.drawCircle(x - r * 0.25, y - r * 0.4, r * 0.18, paint("#FFFFFF", 0.8 * a))


def xicara(c, x, y, s, a):
    """xícara de farinha centrada em (x, y), largura s"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - s / 2, y - s * 0.35); p.lineTo(x + s / 2, y - s * 0.35)
    p.lineTo(x + s * 0.38, y + s * 0.35); p.lineTo(x - s * 0.38, y + s * 0.35); p.close()
    c.drawPath(p, paint(XIC, a))
    c.drawCircle(x + s * 0.5, y - s * 0.02, s * 0.17, paint(XIC, a, stroke=s * 0.07))
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.46, y - s * 0.46, s * 0.92, s * 0.22), paint("#FFFFFF", a))
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.46, y - s * 0.46, s * 0.92, s * 0.22), paint("#D9D9D4", a, stroke=2))


def receita(c, cx, cy, n_ov, n_xi, a, titulo, col=BLUE, w=600, h=330, prog_=1.0):
    """cartão de receita: ovos em cima, xícaras embaixo (prog_ revela os itens)"""
    if a <= 0:
        return
    card(c, cx - w / 2, cy - h / 2, w, h, a)
    text(c, titulo, cx, cy - h / 2 + 46, 28, "black", col, a)
    tot = n_ov + n_xi
    for i in range(n_ov):
        ai = a * clamp(prog_ * tot - i)
        ovo(c, cx - (n_ov - 1) * 42 + i * 84, cy - 30, 30, ai)
    for i in range(n_xi):
        ai = a * clamp(prog_ * tot - n_ov - i)
        xicara(c, cx - (n_xi - 1) * 46 + i * 92, cy + 80, 66, ai)


def fx(c, num, den, cx, cy, size, a, cn=None, cd=None):
    """fração empilhada; devolve os centros do numerador e do denominador (para as setas em X)"""
    fr(c, num, den, cx, cy, size, INK, a, num_col=cn, den_col=cd)
    return (cx, cy - size * 0.52), (cx, cy + size * 0.62)


def diag(c, p0, p1, col, a, enc=0.2, w=8, meio=0.4):
    """diagonal entre dois algarismos em DOIS traços que apontam para o centro (o "=" fica livre no meio)"""
    if a <= 0:
        return
    pe = paint(col, 0.9, stroke=w, cap_round=True)
    for u0, u1 in ((enc, meio), (1 - enc, 1 - meio)):
        u = lerp(u0, u1, a)
        c.drawLine(lerp(p0[0], p1[0], u0), lerp(p0[1], p1[1], u0), lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u), pe)


def proporcao_x(c, t, a, l, r, cx, cy, size, ap=0.0, am=0.0, cores=None):
    """a/b = c/d empilhada com as diagonais: ap = pontas (âmbar), am = miolo (azul)"""
    cores = cores or {}
    gap = size * 1.9
    nl, dl = fx(c, l[0], l[1], cx - gap, cy, size, a, cores.get("a"), cores.get("b"))
    nr, dr = fx(c, r[0], r[1], cx + gap, cy, size, a, cores.get("c"), cores.get("d"))
    diag(c, nl, dr, PONTA, ap)
    diag(c, dl, nr, MIOLO, am)
    igual(c, cx, cy, size, a)
    return nl, dl, nr, dr


def igual(c, cx, cy, size, a):
    """sinal de igual com fundo branco, para continuar legível com as diagonais por trás"""
    if a <= 0:
        return
    fmid(c, "=", cx, cy + size * 0.06, size * 0.9, "black", INK, a)


def pacote(c, x, y, s, col, a, abre=0.0, valor=None, vsize=34):
    """pacotinho fechado (laço) centrado em (x, y); abre = 0..1 levanta a tampa e mostra o valor"""
    if a <= 0:
        return
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    w, h = s * sc, s * 0.8 * sc
    rrect(c, x - w / 2, y - h / 2, w, h, 10, col, a, shadow=True)
    lid = h * 0.28
    dy = -abre * s * 0.45
    rrect(c, x - w / 2 - 6, y - h / 2 - lid * 0.5 + dy, w + 12, lid, 8, mix(col, "#000000", 0.12), a)
    line(c, x, y - h / 2 + 8, x, y + h / 2, "#FFFFFF", a * 0.85, 6)
    line(c, x, y - h / 2 - lid * 0.5 + dy, x, y - h / 2 + lid * 0.5 + dy, "#FFFFFF", a * 0.85, 6)
    if abre > 0 and valor:
        text_mid(c, valor, x, y - h / 2 - s * 0.1 + dy * 0.2, vsize, "black", GREEN, a * clamp(abre * 1.6))


def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROPORÇÃO E O TRUQUE DO k", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "toda REGRA DE TRÊS", W / 2, 250, 44, "black", INK, aa)
    proporcao_x(c, t, aa, ("2", "3"), ("x", "12"), W / 2, 380, 90, ap=ep(t, C["01.a"] + 1.0, 0.6),
                am=ep(t, C["01.a"] + 1.4, 0.6))
    ab = ep(t, C["01.b"], 0.5)
    chip(c, "funciona por causa de 1 PROPRIEDADE", 640, 650, PURPLE, ab, 34)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k in range(3):
            pacote(c, 1200 + k * 110, 650, 84, CAIXA, acc * ep(t, C["01.c"] + 0.2 * k, 0.4))
        text(c, "+ um TRUQUE de uma linha", 1310, 770, 32, "black", GREEN, acc)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "por que a regra de três funciona", "a propriedade das pontas e do miolo"),
            ("02.b", "dividir qualquer valor numa razão", "com pacotinhos de k")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "RAZÃO = comparar dividindo", 560, 260, 34, "black", BLUE, aa)
        text(c, "2 para 3", 560, 420, 64, "black", INK, aa)
        fmid(c, "↓", 560, 500, 50, "black", GRAY, aa)
        expr(c, "2/3", 560, 620, 90, ep(t, C["03.a"] + 1.0, 0.5), cores={0: BLUE})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "EQUIVALENTES = o mesmo pedaço", 1360, 260, 34, "black", BLUE, ab)
        for k, (n, s, lab) in enumerate([(2, 1, "1/2"), (4, 2, "2/4"), (6, 3, "3/6")]):
            a = ab * ep(t, C["03.c"] + 0.5 * k, 0.4)
            x = 1140 + k * 220
            K.pizza(c, x, 470, 88, n, s, a)
            expr(c, lab, x, 640, 50, a, cores={0: INK})
        chip(c, "a mesma metade", 1360, 770, GREEN, ep(t, C["03.c"] + 1.6, 0.5), 30)


# ======================================================================
# bloco A — a receita: proporção
# ======================================================================

def b_receita(c, t, C, B):
    head_seq(c, t, C, [("04", "UMA RECEITA DE BOLO", "E UM BOLO MAIOR", BLUE), ("05", "O NOME DISSO", "PROPORÇÃO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        a0 = ep(t, C["04"], 0.5)
        receita(c, 560, 420, 2, 3, a0, "RECEITA", BLUE, prog_=ep(t, C["04"], 1.6))
        text(c, "2 ovos  :  3 xícaras", 560, 640, 38, "black", INK, a0)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            arrow(c, 880, 420, 1000, 420, AMBER, ab, 6, 18, progress=ab)
            fmid(c, "× 2", 940, 380, 34, "black", AMBER, ab)
        receita(c, 1360, 420, 4, 6, ab, "RECEITA DA FESTA", BLUE, w=700, prog_=ep(t, C["04.b"], 1.6))
        text(c, "4 ovos  :  6 xícaras", 1360, 640, 38, "black", INK, ab)
        ac = ep(t, C["04.c"], 0.5)
        selo(c, W / 2, 718, ac, "A MESMA RECEITA", GREEN, -3, 38)
        text(c, "ovos : farinha continua 2 para 3", W / 2, 818, 28, "bold", INK2, ep(t, C["04.d"], 0.5))
        return
    a0 = ep(t, C["05.a"], 0.5)
    expr(c, "2/3 = 4/6", W / 2, 300, 110, a0, cores={0: BLUE, 2: BLUE})
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        boxed(c, 460, 450, 1000, 96, BLUE, ab, 0.08)
        text_mid(c, "PROPORÇÃO = igualdade entre duas razões", W / 2, 498, 38, "black", BLUE, ab)
    acc = ep(t, C["05.c"], 0.5)
    expr(c, "a/b = c/d", W / 2, 640, 80, acc, cores={0: PURPLE, 2: PURPLE})
    regra(c, "a mesma receita em tamanhos diferentes", W / 2, 790, ep(t, C["05.d"], 0.5), 32, GREEN)


# ======================================================================
# bloco B — pontas e miolo
# ======================================================================

LIN = ["a", ":", "b", "=", "c", ":", "d"]


def b_pontas(c, t, C, B):
    frame(c, t, B["start"], "QUEM ESTÁ NAS PONTAS?", "EXTREMOS E MEIOS", BLUE)
    aa = ep(t, C["06.a"], 0.5)
    ab, ac = ep(t, C["06.b"], 0.5), ep(t, C["06.c"], 0.5)
    xs = [560 + k * 135 for k in range(7)]
    y = 380
    for k, s in enumerate(LIN):
        col = INK
        if k in (0, 6):
            col = mix(INK, PONTA, ab)
        if k in (2, 4):
            col = mix(INK, MIOLO, ac)
        if k in (0, 6) and ab > 0:
            rrect(c, xs[k] - 55, y - 75, 110, 130, 20, PONTA, 0.14 * ab)
        if k in (2, 4) and ac > 0:
            rrect(c, xs[k] - 55, y - 75, 110, 130, 20, MIOLO, 0.14 * ac)
        fmid(c, s, xs[k], y, 110, "black", col, aa)
    text(c, "“a está para b, assim como c está para d”", W / 2, 520, 30, "bold", INK2, aa)
    if ab > 0:
        text(c, "PONTAS = EXTREMOS", 560 + 405, 630, 40, "black", PONTA, ab)
        text(c, "o a e o d", 560 + 405, 680, 28, "bold", INK2, ab)
    if ac > 0:
        text(c, "MIOLO = MEIOS", 560 + 405, 750, 40, "black", MIOLO, ac)
        text(c, "o b e o c", 560 + 405, 798, 28, "bold", INK2, ac)


# ======================================================================
# bloco C — a propriedade fundamental
# ======================================================================

def b_fundamental(c, t, C, B):
    head_seq(c, t, C, [("07", "A PROPRIEDADE", "QUE FAZ TUDO FUNCIONAR", PURPLE), ("08", "PRODUTO CRUZADO", "ACHANDO O NÚMERO QUE FALTA", PURPLE),
                       ("09", "ATALHO", "O NÚMERO QUE FALTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    if sid == "07":
        a0 = ep(t, C["07"], 0.5)
        aa, ab = ep(t, C["07.a"], 0.6), ep(t, C["07.b"], 0.6)
        proporcao_x(c, t, a0, ("2", "3"), ("4", "6"), 560, 400, 120, ap=aa, am=ab,
                    cores={"a": mix(INK, PONTA, aa), "d": mix(INK, PONTA, aa), "b": mix(INK, MIOLO, ab), "c": mix(INK, MIOLO, ab)})
        expr(c, "2 · 6 = 12", 1300, 320, 64, aa, cores={4: PONTA})
        text(c, "pontas", 1300, 380, 28, "black", PONTA, aa)
        expr(c, "3 · 4 = 12", 1300, 500, 64, ab, cores={4: MIOLO})
        text(c, "miolo", 1300, 560, 28, "black", MIOLO, ab)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            boxed(c, 560, 640, 800, 110, PURPLE, ad, 0.08)
            expr(c, "a · d = b · c", W / 2, 695, 64, ad, cores={i: PURPLE for i in range(7)})
        chip(c, "PROPRIEDADE FUNDAMENTAL", W / 2, 800, PURPLE, ep(t, C["07.e"], 0.5), 30)
        return
    if sid == "08":
        a0 = ep(t, C["08"], 0.5)
        aa = ep(t, C["08.a"], 0.5)
        dmode = t >= C["08.d"] - 0.1
        if not dmode:
            proporcao_x(c, t, a0, ("2", "3"), ("4", "6"), W / 2, 380, 120, ap=a0, am=a0)
            if aa > 0:
                boxed(c, 460, 640, 1000, 96, BLUE, aa, 0.08)
                text_mid(c, "PRODUTO CRUZADO = multiplicar em diagonal", W / 2, 688, 36, "black", BLUE, aa)
            text(c, "e por que a regra de três funciona?", W / 2, 800, 32, "black", AMBER, ep(t, C["08.b"], 0.5))
            return
        ad = ep(t, C["08.d"], 0.5)
        ae, af = ep(t, C["08.e"], 0.6), ep(t, C["08.f"], 0.5)
        proporcao_x(c, t, ad, ("2", "3"), ("x", "12"), 560, 400, 120, ap=ae, am=ae,
                    cores={"c": RED})
        chip(c, "x = o número que falta", 560, 720, RED, ad, 28)
        expr(c, "2 · 12 = 24", 1300, 300, 58, ae, cores={4: PONTA})
        expr(c, "3 · x", 1300, 420, 58, ae, cores={0: MIOLO, 1: MIOLO, 2: MIOLO})
        expr(c, "3x = 24", 1300, 560, 64, af)
        expr(c, "x = 8", 1300, 690, 80, ep(t, C["08.f"] + 1.2, 0.5), cores={2: GREEN})
        return
    # 09 atalho
    a0 = ep(t, C["09"], 0.5)
    nl, dl, nr, dr = proporcao_x(c, t, a0, ("2", "3"), ("x", "12"), 520, 420, 120, cores={"c": RED})
    aa, ab = ep(t, C["09.a"], 0.5), ep(t, C["09.b"], 0.5)
    diag(c, nl, dr, GREEN, aa, w=9)
    diag(c, dl, nr, AMBER, ab, w=9)
    if aa > 0:
        K.atalho(c, 960, 200, 760, 400, "ATALHO", ["multiplique a diagonal COMPLETA", "divida pelo número", "da diagonal do x"], aa, 34)
    acc = ep(t, C["09.c"], 0.5)
    expr(c, "x = 2 · 12 / 3", 1340, 680, 50, acc)
    expr(c, "= 24/3 = 8", 1340, 770, 50, ep(t, C["09.c"] + 1.2, 0.5), cores={3: GREEN})
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        text(c, "8 ovos : 12 xícaras", 520, 720, 36, "black", GREEN, ad)
        text(c, "a receita × 4", 520, 776, 28, "bold", INK2, ad)


# ======================================================================
# bloco D — inverter as duas
# ======================================================================

def b_inverter(c, t, C, B):
    frame(c, t, B["start"], "E SE VIRAR DE CABEÇA PARA BAIXO?", "AS DUAS OU SÓ UMA", PURPLE)
    a0 = ep(t, C["10"], 0.5)
    expr(c, "2/3 = 4/6", W / 2, 230, 60, a0 * (1 - 0.5 * ep(t, C["10.a"], 0.4)) * (1 - ep(t, C["10.f"], 0.3)))
    aa, ab = ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5)
    text(c, "vire AS DUAS", 560, 330, 34, "black", GREEN, aa)
    proporcao_x(c, t, aa, ("3", "2"), ("6", "4"), 560, 450, 100, ap=ab, am=ab)
    expr(c, "3 · 4 = 12   2 · 6 = 12", 560, 700, 40, ab)
    if ab > 0:
        check_icon(c, 560, 780, 32, ab, GREEN)
    line(c, 960, 300, 960, 820, "#E6E6E2", ep(t, C["10.c"], 0.4), 3)
    acc, ad = ep(t, C["10.c"], 0.5), ep(t, C["10.d"], 0.5)
    text(c, "vire SÓ UMA", 1360, 330, 34, "black", RED, acc)
    proporcao_x(c, t, acc, ("3", "2"), ("4", "6"), 1360, 450, 100, ap=ad, am=ad)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        rrect(c, 1270, 440, 180, 130, 16, "#FFFFFF", ae * 0.85)
        fmid(c, "≠", 1360, 506, 100, "black", RED, ae)
    expr(c, "3 · 6 = 18   2 · 4 = 8", 1360, 700, 40, ad, cores={4: RED, 9: RED})
    if ae > 0:
        check_icon(c, 1360, 780, 32, ae, RED, "x")
    regra(c, "inverteu? inverta AS DUAS", W / 2, 230, ep(t, C["10.f"], 0.5), 34)


# ======================================================================
# bloco E — soma dos antecedentes
# ======================================================================

def b_soma(c, t, C, B):
    frame(c, t, B["start"], "JUNTE AS DUAS RECEITAS", "A MESMA PROPORÇÃO", PURPLE)
    a0 = ep(t, C["11"], 0.5)
    aa = ep(t, C["11.a"], 0.5)
    receita(c, 420, 340, 2, 3, a0 * (1 - 0.3 * aa), "2 : 3", BLUE, w=440, h=300)
    fmid(c, "+", 700, 340, 70, "black", INK2, a0)
    receita(c, 1050, 340, 4, 6, a0 * (1 - 0.3 * aa), "4 : 6", BLUE, w=560, h=300)
    if aa > 0:
        arrow(c, 1360, 340, 1440, 340, AMBER, aa, 6, 18, progress=aa)
        rrect(c, 1450, 220, 300, 250, 28, mix("#FFFFFF", AMBER, 0.12), aa, shadow=True)
        text(c, "a tigela", 1600, 260, 26, "black", AMBER, aa)
        expr(c, "2 + 4 = 6", 1600, 340, 40, aa, cores={4: INK})
        text(c, "ovos", 1600, 380, 24, "bold", INK2, aa)
        ab = ep(t, C["11.b"], 0.5)
        expr(c, "3 + 6 = 9", 1600, 430, 40, ab)
        text(c, "xícaras", 1600, 462, 24, "bold", INK2, ab)
    acc = ep(t, C["11.c"], 0.5)
    expr(c, "(2+4)/(3+6) = 6/9 = 2/3", W / 2, 600, 70, acc, cores={2: GREEN, 4: GREEN})
    ad = ep(t, C["11.d"], 0.5)
    regra(c, "somar os de cima e somar os de baixo MANTÉM a proporção", W / 2, 760, ad, 32)


# ======================================================================
# bloco F — os pacotinhos de k
# ======================================================================

def _linha_pacotes(c, t, x0, y, n, a, abre, valor, col=CAIXA, s=100, gap=124, ins=None):
    for i in range(n):
        ai = a * (ep(t, ins + 0.25 * i, 0.4) if ins is not None else 1.0)
        pacote(c, x0 + i * gap, y, s, col, ai, abre, valor)


def b_pacotes(c, t, C, B):
    head_seq(c, t, C, [("12", "DUAS SÓCIAS, R$ 10 000", "RAZÃO 2 PARA 3", BLUE), ("13", "ABRA OS PACOTINHOS", "O TAMANHO DE CADA UM: k", PURPLE),
                       ("14", "TRÊS PARTES?", "FUNCIONA DO MESMO JEITO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    if sid in ("12", "13"):
        a0 = ep(t, C["12"], 0.5)
        chip(c, "lucro: R$ 10 000", W / 2, 230, INK2, a0, 34)
        ab = ep(t, C["12.b"], 0.5)
        abre = ep(t, C["13.a"], 0.6) if sid == "13" else 0.0
        abre2 = ep(t, C["13.b"], 0.6) if sid == "13" else 0.0
        text(c, "ANA", 360, 410, 40, "black", BLUE, ab)
        _linha_pacotes(c, t, 520, 400, 2, ab, abre, "2 000", ins=C["12.b"] + 0.3)
        text(c, "BIA", 360, 590, 40, "black", PURPLE, ab)
        _linha_pacotes(c, t, 520, 580, 3, ab, abre2, "2 000", col=mix(CAIXA, PURPLE, 0.25), ins=C["12.b"] + 1.0)
        if sid == "12":
            acc = ep(t, C["12.c"], 0.5)
            if acc > 0:
                boxed(c, 1080, 330, 600, 330, AMBER, acc, 0.08)
                text(c, "2 + 3 = 5 pacotinhos", 1380, 410, 40, "black", INK, acc)
            ad = ep(t, C["12.d"], 0.5)
            linha(c, [("10 000 ÷ 5 = ", INK), ("2 000", GREEN)], 1380, 520, 46, ad)
            text(c, "cada pacotinho", 1380, 600, 30, "bold", INK2, ad)
            return
        expr(c, "= 4 000", 920, 410, 50, ep(t, C["13.a"] + 0.6, 0.5), cores={1: GREEN, 2: GREEN})
        expr(c, "= 6 000", 1040, 590, 50, ep(t, C["13.b"] + 0.6, 0.5), cores={1: GREEN, 2: GREEN})
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            boxed(c, 1240, 330, 480, 120, BLUE, acc, 0.08)
            text(c, "k = o tamanho de cada pacotinho", 1480, 380, 26, "black", BLUE, acc)
            text(c, "CONSTANTE: um número que não muda", 1480, 425, 22, "bold", INK2, acc)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            rrect(c, 300, 690, 1320, 110, 20, "#FFFFFF", ad, shadow=True)
            linha(c, [("2k + 3k = 10 000  →  5k = 10 000  →  ", INK), ("k = 2 000", GREEN)], W / 2, 745, 40, ad)
        return
    # 14 três partes
    a0 = ep(t, C["14.a"], 0.5)
    text(c, "60 balas na razão 1 : 2 : 3", W / 2, 230, 40, "black", INK, a0)
    nomes = ["1º irmão", "2º irmão", "3º irmão"]
    cols = [BLUE, PURPLE, AMBER]
    ab = ep(t, C["14.b"], 0.5)
    abre = ep(t, C["14.d"], 0.6)
    for k in range(3):
        y = 340 + k * 140
        text(c, nomes[k], 300, y + 12, 30, "black", cols[k], ab, align="left")
        _linha_pacotes(c, t, 520, y, k + 1, ab, abre, "10", col=mix(CAIXA, cols[k], 0.2), s=80, gap=100,
                       ins=C["14.b"] + 0.5 * k)
        expr(c, f"= {10 * (k + 1)}", 900, y, 46, ep(t, C["14.d"] + 0.5 * k, 0.5), cores={1: GREEN})
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 1100, 300, 560, 200, 22, "#FFFFFF", acc, shadow=True)
        text(c, "1 + 2 + 3 = 6 pacotinhos", 1380, 365, 34, "black", INK, acc)
        expr(c, "60 ÷ 6 = 10 = k", 1380, 440, 46, acc, cores={4: GREEN})
    ae = ep(t, C["14.e"], 0.5)
    K.atalho(c, 300, 700, 1320, 130, "ATALHO",
             ["some os números da razão  →  divida o total  →  multiplique"], ae, 34)


# ======================================================================
# bloco G — proporção contínua
# ======================================================================

def b_continua(c, t, C, B):
    frame(c, t, B["start"], "UM CASO ESPECIAL", "PROPORÇÃO CONTÍNUA", BLUE)
    aa, ab = ep(t, C["15.a"], 0.5), ep(t, C["15.b"], 0.5)
    ad = ep(t, C["15.d"], 0.6)
    proporcao_x(c, t, aa, ("2", "4"), ("4", "8"), 560, 380, 120, ap=ad, am=ad,
                cores={"b": mix(INK, MIOLO, ab), "c": mix(INK, MIOLO, ab)})
    chip(c, "o miolo repete o mesmo número", 560, 680, MIOLO, ab, 28)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        boxed(c, 1050, 230, 620, 96, BLUE, acc, 0.08)
        text_mid(c, "PROPORÇÃO CONTÍNUA", 1360, 278, 36, "black", BLUE, acc)
    expr(c, "2 · 8 = 16", 1360, 410, 54, ad, cores={4: PONTA})
    expr(c, "4 · 4 = 16", 1360, 500, 54, ad, cores={4: MIOLO})
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        rrect(c, 1050, 570, 620, 210, 22, "#FFFFFF", ae, shadow=True)
        expr(c, "4^2 = 2 · 8", 1360, 630, 54, ae, cores={0: PURPLE})
        text(c, "4 = MÉDIA GEOMÉTRICA de 2 e 8", 1360, 712, 28, "black", PURPLE, ae)
        text(c, "ao quadrado, dá o produto das pontas", 1360, 756, 24, "bold", INK2, ae)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E RESOLVA", GREEN), ("17", "VAMOS CONFERIR", "PAUSE E RESOLVA", GREEN)])
    card(c, *CARD_R)
    conf = t >= C["17"]
    for k, cue in enumerate(["16.a", "16.b"]):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 200, 24, "#F7F7F5", a)
        text(c, f"{k + 1}ª CONTA", x, 245, 22, "black", GRAY, a, tracking=1)
        if k == 0:
            expr(c, "x/12 = 5/4", x, 320, 70, a, cores={0: RED})
        else:
            text_mid(c, "90 na razão 2 para 7", x, 320, 50, "black", INK, a)
    if conf:
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            expr(c, "4 · x = 12 · 5 = 60", 560, 500, 46, aa)
            expr(c, "x = 60 ÷ 4 = 15", 560, 610, 54, ep(t, C["17.a"] + 2.5, 0.5), cores={6: GREEN})
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            text(c, "2 + 7 = 9 pacotinhos", 1360, 500, 36, "black", INK, ab)
            expr(c, "90 ÷ 9 = 10 = k", 1360, 590, 46, ab, cores={4: GREEN})
        acc = ep(t, C["17.c"], 0.5)
        if acc > 0:
            for i in range(9):
                col = mix(CAIXA, BLUE, 0.25) if i < 2 else mix(CAIXA, PURPLE, 0.25)
                pacote(c, 1030 + i * 80 + (30 if i >= 2 else 0), 690, 60, col, acc * ep(t, C["17.c"] + 0.08 * i, 0.3))
            expr(c, "20   e   70", 1220, 795, 50, acc, cores={0: GREEN, 2: GREEN})
        text(c, "20 + 70 = 90 ✓", 1560, 808, 30, "black", GREEN, ep(t, C["17.d"], 0.5))
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 620)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Proporção é a mesma receita em tamanhos diferentes.", "Pontas vezes pontas = miolo vezes miolo.",
          "Razão e soma? Pacotinhos de k."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("Inverter só UMA das razões", "as duas frações continuam ali, com os mesmos números",
          "virou uma? vire AS DUAS: 3/2 = 6/4"),
         ("Dividir em partes IGUAIS, ignorando a razão", "dividir ao meio é o jeito mais comum de repartir",
          "razão 2 para 3 = 2 pacotinhos para um, 3 para o outro"),
         ("Responder a parte MENOR quando pedem a MAIOR", "a primeira parte calculada já aparece nas alternativas",
          "antes de marcar, releia: QUAL parte a questão quer?")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# Questão 7 do material
# ======================================================================

ALTS = [("A", "R$ 24 000,00", "a parte MENOR", RED), ("B", "R$ 32 000,00", "partes iguais", RED),
        ("C", "R$ 38 400,00", "3/5 do total: são 3 de 8", RED), ("D", "R$ 40 000,00", "", GREEN),
        ("E", "R$ 48 000,00", "48 000 : 16 000 = 3 : 1", RED)]
ENUN = "Dois sócios dividiram um lucro de R$ 64 000,00 na razão de 3 para 5. O sócio que recebeu a maior parte ficou com"


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · RAZÃO COM SOMA CONHECIDA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    para(c, ENUN, 190, 240, 34, "black", INK, a0, 650, 46)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["24.xa"], "B": C["24.xb"], "C": C["24.xc"], "E": C["24.xe"]}
    if t >= C["22.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS, 920, 200, 780, 40, C["23.ok"], "D", cues_in, cues_x, gap=16)
    pause_timer(c, t, C["22.end"] - 1.9, 470, 640)
    if t >= C["23"]:
        ra = ep(t, C["23"], 0.4)
        rrect(c, 170, 470, 700, 330, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["23.a"], 0.4)
        for i in range(8):
            col = mix(CAIXA, BLUE, 0.25) if i < 3 else mix(CAIXA, PURPLE, 0.25)
            pacote(c, 230 + i * 78 + (24 if i >= 3 else 0), 540, 56, col, aa * ep(t, C["23.a"] + 0.1 * i, 0.3),
                   ep(t, C["23.b"] + 0.3, 0.5), "8 mil", 22)
        linha(c, [("8k = 64 000  →  ", INK), ("k = 8 000", GREEN)], 520, 640, 34, ep(t, C["23.b"], 0.4))
        linha(c, [("3k = 24 000   ·   5k = ", INK), ("40 000", GREEN)], 520, 730, 34, ep(t, C["23.c"], 0.4))


def b_conferir(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "CONFIRA ANTES DE MARCAR", GREEN)
    a0 = ep(t, C["25"], 0.5)
    text(c, "dividiu um total numa razão? dois testes:", W / 2, 240, 38, "black", INK, a0)
    aa = ep(t, C["25.a"], 0.5)
    if aa > 0:
        badge_num(c, 1, 300, 380, aa, 30, bg=GREEN)
        text(c, "somam o total?", 360, 392, 40, "black", INK, aa, align="left")
        linha(c, [("24 000 + 40 000 = ", INK), ("64 000", GREEN)], 1150, 380, 46, aa)
        check_icon(c, 1720, 375, 28, ep(t, C["25.a"] + 2.5, 0.4), GREEN)
    ab = ep(t, C["25.b"], 0.5)
    if ab > 0:
        badge_num(c, 2, 300, 540, ab, 30, bg=GREEN)
        text(c, "estão na razão?", 360, 552, 40, "black", INK, ab, align="left")
        linha(c, [("24 000 ÷ 8 000 = ", INK), ("3", GREEN), ("   ·   40 000 ÷ 8 000 = ", INK), ("5", GREEN)], 1150, 540, 40, ab)
        check_icon(c, 1720, 535, 28, ep(t, C["25.b"] + 2.5, 0.4), GREEN)
    selo(c, W / 2, 740, ep(t, C["25.c"], 0.5), "PASSOU NOS DOIS? PODE MARCAR", GREEN, -3, 34)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DIRETA OU INVERSA?", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    text(c, "antes de qualquer regra de três: uma DECISÃO", W / 2, 260, 40, "black", INK, aa)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        for k, (nome, col, cresce) in enumerate([("DIRETA", GREEN, True), ("INVERSA", PURPLE, False)]):
            x = 640 + k * 640
            text(c, nome, x, 360, 44, "black", col, ab)
            g = ep(t, C["27.b"] + 0.5, 1.2)
            h1 = 120 + 120 * g
            h2 = 120 + 120 * g if cresce else 240 - 120 * g
            rrect(c, x - 130, 660 - h1, 100, h1, 12, col, ab)
            rrect(c, x + 30, 660 - h2, 100, h2, 12, mix(col, "#FFFFFF", 0.35), ab)
    pill(c, "ep. 3 · direta ou inversa? e a regra de três simples", W / 2, 770, PURPLE, size=30,
         a=ep(t, C["27.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Você já conhecia o truque dos pacotinhos?",
        canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, receita=b_receita, pontas=b_pontas, fundamental=b_fundamental,
              inverter=b_inverter, soma=b_soma, pacotes=b_pacotes, continua=b_continua, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, questao=b_questao, conferir=b_conferir, ponte=b_ponte, cta=b_cta)
