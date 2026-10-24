"""Visual — Notação Científica e Ordem de Grandeza, Episódio 3: Somar em notação científica e comparar grandezas
(iniciantes, tema claro). Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, frações,
alternativas, erro_cards, atalho...). Peças deste episódio: notas de dinheiro, gangorra, Terra com Luas.
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
_s = importlib.util.spec_from_file_location("comum020", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep3_somar_comparar.mp4"
CARD_R = K.CARD_R
NOTA100 = "#4F7FD1"
NOTA10 = "#E0763F"
TERRA = "#3D86C6"
TERRA2 = "#4FAE6A"
LUA = "#B9B7B0"


def mono(n, col):
    return {i: col for i in range(n)}


def mline(c, partes, x, y, size, a, col=None):
    """linha mista: partes = [str | ('m', expr)], desenhadas em sequência; y = linha de base do texto"""
    col = col or INK
    for p in partes:
        if isinstance(p, tuple):
            w = K.math_w(p[1], size)
            K.mdraw(c, p[1], x, y - size * 0.36, size, col, a)
            x += w
        else:
            text(c, p, x, y, size, "black", col, a, align="left")
            x += text_w(p, "black", size)
    return x


# ======================================================================
# peças do episódio
# ======================================================================

def nota(c, x, y, w, h, valor, col, a, fill=1.0, rot=0.0):
    """nota de dinheiro (x, y = canto); fill < 1 desenha só a fração colorida da nota (o resto tracejado)"""
    if a <= 0:
        return
    c.save()
    if rot:
        c.translate(x + w / 2, y + h / 2); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    if fill < 1:
        rrect(c, x, y, w, h, 10, "#FFFFFF", a * 0.9)
        pe = paint(col, a * 0.7, stroke=3)
        pe.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), pe)
        c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w * fill, h))
        rrect(c, x, y, w, h, 10, col, a)
        c.restore()
    else:
        rrect(c, x, y, w, h, 10, col, a, shadow=True)
        rrect(c, x + 8, y + 8, w - 16, h - 16, 6, "#FFFFFF", a * 0.18)
        c.drawCircle(x + w * 0.78, y + h / 2, h * 0.26, paint("#FFFFFF", a * 0.35))
    if fill >= 1:
        text_mid(c, valor, x + w * 0.38, y + h / 2, h * 0.36, "black", "#FFFFFF", a)
    c.restore()


def gangorra(c, cx, cy, incl, a, esq, dir_, col_esq=None, col_dir=None, size=40, larg=560):
    """gangorra: incl > 0 abaixa a esquerda. esq/dir_ = expressões nas pontas (expr)"""
    if a <= 0:
        return
    col_esq, col_dir = col_esq or BLUE, col_dir or PURPLE
    p = skia.Path(); p.moveTo(cx, cy); p.lineTo(cx - 34, cy + 60); p.lineTo(cx + 34, cy + 60); p.close()
    c.drawPath(p, paint(INK2, a))
    ang = math.radians(10 * incl)
    dx, dy = math.cos(ang) * larg / 2, math.sin(ang) * larg / 2
    line(c, cx - dx, cy + dy, cx + dx, cy - dy, INK, a, 12, cap_round=True)
    for sx, sy, s, col in ((cx - dx, cy + dy, esq, col_esq), (cx + dx, cy - dy, dir_, col_dir)):
        w = K.math_w(s, size) + 40
        rrect(c, sx - w / 2, sy - 92, w, 76, 16, "#FFFFFF", a, shadow=True)
        expr(c, s, sx, sy - 54, size, a, cores=mono(8, col))


def terra(c, cx, cy, r, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(TERRA, a))
    for (ox, oy, rr) in ((-0.35, -0.25, 0.32), (0.3, 0.2, 0.28), (0.05, -0.55, 0.18), (-0.2, 0.45, 0.2)):
        c.drawCircle(cx + ox * r, cy + oy * r, rr * r, paint(TERRA2, a * 0.9))
    c.drawCircle(cx, cy, r, paint(INK, a * 0.25, stroke=3))


def lua(c, cx, cy, r, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(LUA, a))
    c.drawCircle(cx - r * 0.3, cy - r * 0.2, r * 0.22, paint("#9E9C95", a))
    c.drawCircle(cx + r * 0.25, cy + r * 0.3, r * 0.15, paint("#9E9C95", a))


def luas_na_terra(c, cx, cy, r, n, a, rl=14):
    """n Luas pequenas preenchendo o disco da Terra (grade dentro do círculo)"""
    pos = []
    step = rl * 2.25
    k = int(r / step) + 1
    for j in range(-k, k + 1):
        for i in range(-k, k + 1):
            x, y = cx + i * step + (step / 2 if j % 2 else 0), cy + j * step * 0.9
            if (x - cx) ** 2 + (y - cy) ** 2 <= (r - rl) ** 2:
                pos.append((x, y))
    pos.sort(key=lambda p: (p[1], p[0]))
    for (x, y) in pos[:n]:
        lua(c, x, y, rl, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "SOMAR: A QUE DERRUBA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "3·10^5 + 8·10^4 = ?", W / 2, 300, 110, aa)
    ad = ep(t, C["01.d"], 0.5)
    for k, (cue, s) in enumerate((("01.b", "11·10^9"), ("01.c", "11·10^5"))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 640 + k * 640
        card(c, x - 230, 440, 460, 190, a)
        text(c, "metade responde", x, 485, 26, "bold", GRAY, a)
        expr(c, s, x, 565, 76, a, cores=mono(3, AMBER if ad <= 0 else RED))
        if ad > 0:
            strike(c, x - 160, 565, x + 160, 565, ad, RED, ad)
    selo(c, W / 2, 700, ad, "AS DUAS ERRARAM", RED, -3, 40)
    pill(c, "quem ESTUDOU  ×  quem DECOROU", W / 2, 800, PURPLE, size=32, a=ep(t, C["01.e"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "somar em notação científica", "sem errar, com notas de dinheiro"),
            ("02.b", "dividir ou subtrair?", "o que cada comparação pede")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 34, a, GREEN)
        text(c, s, 390, y, 52, "black", INK, a, align="left")
        text(c, sub, 390, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "DO EPISÓDIO PASSADO", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "A GANGORRA", 560, 250, 32, "black", BLUE, aa)
    incl = ep(t, C["03.a"] + 0.6, 0.8)
    gangorra(c, 560, 470, incl, aa, "8 → 0,8", "10^4 → 10^5", col_esq=BLUE, col_dir=PURPLE, size=36, larg=600)
    text(c, "número da frente ÷ 10", 330, 600, 24, "bold", BLUE, aa)
    text(c, "expoente + 1", 800, 600, 24, "bold", PURPLE, aa)
    ab = ep(t, C["03.b"], 0.5)
    expr(c, "8·10^4 = 0,8·10^5", 560, 690, 50, ab, cores={2: GREEN})
    chip(c, "mesmo valor", 560, 780, GREEN, ab, 28)
    line(c, 1050, 230, 1050, 800, "#E6E6E2", aa, 3)
    acc = ep(t, C["03.c"], 0.5)
    text(c, "DIVIDIR", 1370, 250, 32, "black", PURPLE, acc)
    expr(c, "6·10^5/2·10^3", 1370, 420, 62, acc)
    expr(c, "= 3·10^2", 1370, 570, 62, acc, cores={1: GREEN})
    text(c, "divide a frente · SUBTRAI os expoentes", 1370, 690, 28, "bold", INK2, acc)


# ======================================================================
# notas de valores diferentes
# ======================================================================

def b_notas(c, t, C, B):
    head_seq(c, t, C, [("04", "COMEÇANDO PELO DINHEIRO", "NOTAS DIFERENTES", BLUE), ("05", "COM MEDIDAS", "É IGUAL", BLUE),
                       ("06", "E NA NOTAÇÃO?", "10⁵ E 10⁴ SÃO NOTAS DIFERENTES", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        for k in range(3):
            nota(c, 220 + k * 34, 230 + k * 40, 300, 130, "R$ 100", NOTA100, ep(t, C["04.a"] + 0.25 * k, 0.4))
        text(c, "3 notas de R$ 100", 380, 480, 30, "black", NOTA100, aa)
        for k in range(8):
            nota(c, 680 + (k % 4) * 150, 230 + (k // 4) * 110, 136, 92, "10", NOTA10, ep(t, C["04.b"] + 0.15 * k, 0.3))
        text(c, "8 notas de R$ 10", 970, 480, 30, "black", NOTA10, ep(t, C["04.b"], 0.5))
        acc = ep(t, C["04.c"], 0.5)
        ad = ep(t, C["04.d"], 0.4)
        if acc > 0:
            boxed(c, 1340, 230, 340, 230, AMBER, acc, 0.10)
            text(c, "11 notas", 1510, 320, 44, "black", INK, acc)
            text(c, "de R$ 100?", 1510, 380, 44, "black", INK, acc)
            if ad > 0:
                check_icon(c, 1650, 250, 30, ad, RED, "x")
                strike(c, 1380, 345, 1640, 345, ad, RED, ad)
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            rrect(c, 460, 580, 1000, 150, 22, "#FFFFFF", ae, shadow=True)
            ftext(c, "R$ 300 + R$ 80 = R$ 380", W / 2, 680, 64, "black", GREEN, ae)
        return
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        # réguas
        x0, y0 = 300, 300
        rrect(c, x0, y0, 800, 70, 10, "#F3D9A4", aa, shadow=True)
        for i in range(9):
            line(c, x0 + i * 100, y0, x0 + i * 100, y0 + (30 if i % 2 == 0 else 18), INK2, aa, 3)
        text(c, "2 m", x0 + 400, y0 + 110, 30, "black", INK, aa)
        rrect(c, x0 + 830, y0, 200, 70, 10, "#F3D9A4", aa, shadow=True)
        text(c, "50 cm", x0 + 930, y0 + 110, 30, "black", INK, aa)
        expr(c, "2 m + 50 cm ≠ 52 m", 960, 540, 60, aa, cores={5: RED, 6: RED, 7: RED})
        ab = ep(t, C["05.b"], 0.5)
        expr(c, "50 cm = 0,5 m", 960, 650, 50, ab, cores={3: BLUE, 4: BLUE})
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 710, 710, 500, 90, 18, "#FFFFFF", acc, shadow=True)
            text_mid(c, "2,5 m", 960, 755, 56, "black", GREEN, acc)
        return
    # 06
    aa, ab = ep(t, C["06.a"], 0.5), ep(t, C["06.b"], 0.5)
    nota(c, 330, 260, 460, 200, "100 mil", NOTA100, aa)
    expr(c, "10^5 = 100 mil", 560, 540, 54, aa, cores={0: NOTA100})
    nota(c, 1130, 260, 460, 200, "10 mil", NOTA10, ab)
    expr(c, "10^4 = 10 mil", 1360, 540, 54, ab, cores={0: NOTA10})
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        boxed(c, 460, 650, 1000, 110, AMBER, acc, 0.10)
        text_mid(c, "NOTAS DE VALORES DIFERENTES", W / 2, 705, 46, "black", INK, acc)


# ======================================================================
# a condição
# ======================================================================

def b_condicao(c, t, C, B):
    frame(c, t, B["start"], "A REGRA", "SÓ COM O MESMO EXPOENTE", PURPLE)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 220, 1320, 120, PURPLE, aa, 0.08)
        text_mid(c, "somar ou subtrair: só com o MESMO expoente", W / 2, 280, 46, "black", INK, aa)
    expr(c, "3·10^5 + 8·10^4", W / 2, 440, 80, aa)
    if aa > 0:
        ftext(c, "expoentes diferentes: 5 ≠ 4", W / 2, 540, 32, "black", RED, aa)
    ab = ep(t, C["07.b"], 0.5)
    chip(c, "iguale PRIMEIRO", W / 2, 600, AMBER, ab, 34)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 650, 1320, 110, BLUE, acc, 0.08)
        text(c, "IGUALAR OS EXPOENTES", W / 2, 690, 24, "black", BLUE, acc, tracking=2)
        text(c, "reescrever um número com o mesmo expoente do outro, SEM mudar o valor", W / 2, 738, 32, "black", INK, acc)
    pill(c, "= trocar tudo pela MESMA nota", W / 2, 800, GREEN, size=28, a=ep(t, C["07.d"], 0.5), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# como igualar
# ======================================================================

def b_igualar(c, t, C, B):
    head_seq(c, t, C, [("08", "COMO TROCAR AS NOTAS?", "A GANGORRA", BLUE), ("09", "O EXEMPLO COMPLETO", "TUDO NA MESMA NOTA", PURPLE),
                       ("10", "E O GANCHO?", "3 · 10⁵ + 8 · 10⁴", PURPLE), ("11", "ATALHO", "CONTE A DIFERENÇA DOS EXPOENTES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10", "11"])
    if sid == "08":
        a0 = ep(t, C["08"], 0.5)
        mv = ep(t, C["08.a"] + 0.6, 1.4)
        # 8 notas de 10 deslizam e viram 0,8 de uma nota de 100
        for k in range(8):
            sx, sy = 220 + (k % 4) * 140, 240 + (k // 4) * 100
            tx, ty = 270 + k * 34, 300
            x, y = lerp(sx, tx, mv), lerp(sy, ty, mv)
            nota(c, x, y, 128, 86, "10", NOTA10, a0 * (1 - ep(t, C["08.a"] + 2.0, 0.5)))
        an = ep(t, C["08.a"] + 2.0, 0.5)
        nota(c, 260, 260, 400, 170, "R$ 100", NOTA100, an, fill=lerp(0, 0.8, ep(t, C["08.a"] + 2.0, 0.8)))
        text(c, "R$ 80 = 0,8 de uma nota de R$ 100", 460, 490, 30, "black", NOTA100, an)
        ab, acc = ep(t, C["08.b"], 0.5), ep(t, C["08.c"], 0.5)
        gangorra(c, 1300, 400, ab, ab, "8 → 0,8", "10^4 → 10^5" if acc > 0 else "10^4", col_esq=BLUE, col_dir=PURPLE,
                 size=36, larg=600)
        text(c, "÷ 10", 1010, 500, 30, "black", BLUE, ab)
        text(c, "expoente + 1", 1600, 420, 30, "black", PURPLE, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            rrect(c, 460, 640, 1000, 130, 22, "#FFFFFF", ad, shadow=True)
            expr(c, "8·10^4 = 0,8·10^5", W / 2, 705, 64, ad, cores={2: GREEN})
        return
    if sid == "09":
        rows = [("09.a", "3·10^5", None), ("09.b", "8·10^4", "0,8·10^5"), ("09.c", "2·10^4", "0,2·10^5")]
        for k, (cue, s, conv) in enumerate(rows):
            a = ep(t, C["09.a"] + 0.6 * k, 0.4)
            y = 270 + k * 110
            if k > 0:
                fmid(c, "+", 330, y, 60, "black", INK2, a)
            expr(c, s, 520, y, 60, a, align="center")
            if conv:
                ac = ep(t, C[cue], 0.5)
                arrow(c, 700, y, 860, y, AMBER, ac, 5, 16, progress=ac)
                expr(c, conv, 1060, y, 60, ac, cores={0: GREEN})
            else:
                expr(c, s, 1060, y, 60, ep(t, C["09.b"], 0.5))
        ad = ep(t, C["09.d"], 0.5)
        line(c, 820, 590, 1300, 590, INK, ad, 4)
        expr(c, "3 + 0,8 + 0,2 = 4", 1060, 650, 52, ad, cores={6: GREEN})
        ae = ep(t, C["09.e"], 0.5)
        if ae > 0:
            rrect(c, 300, 600, 420, 120, 22, GREEN, 0.14 * ae)
            expr(c, "4·10^5", 510, 660, 72, ae, cores={0: GREEN})
        pill(c, "mesma nota: 10⁵", 1060, 800, PURPLE, size=28, a=ep(t, C["09.d"], 0.5), anchor="center", bounds=(0, 1920))
        return
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        expr(c, "3·10^5 + 0,8·10^5", W / 2, 320, 80, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            rrect(c, 560, 420, 800, 140, 24, GREEN, 0.14 * ab)
            expr(c, "= 3,8·10^5", W / 2, 490, 86, ab, cores={1: GREEN})
        acc = ep(t, C["10.c"], 0.5)
        expr(c, "300 mil + 80 mil = 380 mil", W / 2, 680, 54, acc, cores={6: GREEN, 7: GREEN})
        check_icon(c, 1560, 668, 30, acc, GREEN)
        return
    # 11 atalho
    a0 = ep(t, C["11.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 200, "ATALHO", ["a DIFERENÇA dos expoentes = quantas casas a vírgula anda"], a0, 40)
    ab = ep(t, C["11.b"], 0.5)
    expr(c, "10^4 → 10^5", 600, 520, 62, ab)
    text(c, "diferença 1 = 1 casa para a esquerda", 600, 610, 30, "bold", INK2, ab)
    # a vírgula andando: 8 → 0,8 (o zero da frente aparece quando a vírgula passa)
    acc = ep(t, C["11.b"] + 0.8, 0.5)
    if acc > 0:
        u = ep(t, C["11.b"] + 1.4, 1.0)
        x0, base, dw = 1150, 600, 110
        text(c, "0", x0, base, 130, "black", INK, acc * u)
        text(c, "8", x0 + dw, base, 130, "black", INK, acc)
        text(c, ",", lerp(x0 + 1.6 * dw, x0 + 0.55 * dw, u), base, 130, "black", AMBER, acc)
        if u > 0.05:
            p = skia.Path(); p.moveTo(x0 + 1.6 * dw, base + 30); p.quadTo(x0 + 1.07 * dw, base + 80, x0 + 0.55 * dw, base + 30)
            c.drawPath(p, paint(AMBER, acc * u, stroke=4, cap_round=True))
    ac2 = ep(t, C["11.c"], 0.5)
    pill(c, "8 vira 0,8", 1205, 740, GREEN, size=32, a=ac2, anchor="center", bounds=(0, 1920))


# ======================================================================
# a regra de bolso
# ======================================================================

def b_bolso(c, t, C, B):
    frame(c, t, B["start"], "POR QUE PELO MAIOR?", "A REGRA DE BOLSO", GREEN)
    aa = ep(t, C["12.a"], 0.5)
    text(c, "descendo o maior (dá certo, mas…)", 560, 240, 30, "black", AMBER, aa)
    expr(c, "3·10^5 = 30·10^4", 560, 330, 50, aa)
    expr(c, "30 + 8 = 38·10^4", 560, 430, 50, ep(t, C["12.a"] + 2.0, 0.5), cores={4: AMBER})
    ab = ep(t, C["12.b"], 0.5)
    selo(c, 560, 520, ab, "38 NÃO SERVE NA FRENTE", RED, -4, 26)
    expr(c, "mais uma gangorra: 3,8·10^5", 560, 620, 40, ab)
    line(c, 1050, 230, 1050, 800, "#E6E6E2", aa, 3)
    acc = ep(t, C["12.c"], 0.5)
    K.atalho(c, 1110, 230, 560, 240, "REGRA DE BOLSO", ["iguale sempre pelo", "MAIOR expoente"], acc, 40)
    ad = ep(t, C["12.d"], 0.5)
    expr(c, "0,8 + 0,2", 1390, 560, 56, ad, cores={0: GREEN, 2: GREEN})
    text(c, "menores que 1: soma de cabeça", 1390, 650, 28, "bold", INK2, ad)
    text(c, "e já sai na forma certa", 1390, 700, 28, "bold", INK2, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("14", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["13.a"], 0.5)
    expr(c, "5·10^3 + 2·10^2 = ?", W / 2, 290, 86, a0)
    if t < C["14"]:
        pause_timer(c, t, C["13.end"] - 1.9, W / 2, 560)
        return
    steps = [("14.a", "maior expoente: 3", None), ("14.b", "2·10^2 = 0,2·10^3", {2: GREEN}),
             ("14.c", "5 + 0,2 = 5,2 → 5,2·10^3", {6: GREEN})]
    for k, (cue, s, cor) in enumerate(steps):
        a = ep(t, C[cue], 0.5)
        y = 420 + k * 95
        if k == 0:
            text(c, s, W / 2, y + 14, 40, "black", PURPLE, a)
        else:
            expr(c, s, W / 2, y, 52, a, cores=cor)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 560, 700, 800, 90, 18, GREEN, 0.12 * ad)
        expr(c, "5000 + 200 = 5200", W / 2, 745, 46, ad, cores={4: GREEN})
        check_icon(c, 1320, 732, 26, ad, GREEN)


# ======================================================================
# comparar: quantas vezes · quanto
# ======================================================================

def b_vezes(c, t, C, B):
    head_seq(c, t, C, [("15", "COMPARAR", "QUANTAS LUAS CABEM NA TERRA?", BLUE), ("16", "QUANTAS VEZES MAIOR?", "É DIVISÃO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 210, 1320, 100, BLUE, aa, 0.08)
            text(c, "GRANDEZA = o que dá para medir: massa, distância, dinheiro", W / 2, 272, 34, "black", INK, aa)
        ab = ep(t, C["15.b"], 0.5)
        terra(c, 620, 560, 180, ab)
        lua(c, 950, 470, 50, ab)
        arrow(c, 920, 520, 820, 560, INK2, ab, 4, 14, progress=ab)
        text(c, "Terra", 620, 790, 30, "black", TERRA, ab)
        text(c, "Lua", 950, 560, 28, "black", INK2, ab)
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            text(c, "quanto sobra?", 1380, 450, 44, "black", INK2, acc)
            strike(c, 1240, 435, 1520, 435, ep(t, C["15.c"] + 0.6, 0.4), RED, acc)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            boxed(c, 1170, 540, 420, 160, PURPLE, ad, 0.10)
            text(c, "quantas VEZES?", 1380, 605, 40, "black", INK, ad)
            text(c, "→ DIVISÃO", 1380, 665, 40, "black", PURPLE, ad)
        return
    aa, ab = ep(t, C["16.a"], 0.5), ep(t, C["16.b"], 0.5)
    for k, (a, nome, s, w) in enumerate(((aa, "empresa 1", "6·10^5 reais", 760), (ab, "empresa 2", "2·10^3 reais", 30))):
        y = 240 + k * 110
        text(c, nome, 300, y + 52, 28, "black", INK2, a, align="left")
        rrect(c, 460, y + 10, w * ep(t, C["16.a" if k == 0 else "16.b"] + 0.2, 0.8), 64, 14, NOTA100 if k == 0 else NOTA10, a)
        expr(c, s, 1250 if k == 0 else 520, y + 42, 40, a, align="left")
    acc = ep(t, C["16.c"], 0.5)
    text(c, "quantas vezes a primeira é maior?", W / 2, 500, 36, "black", PURPLE, acc)
    ad, ae = ep(t, C["16.d"], 0.5), ep(t, C["16.e"], 0.5)
    expr(c, "6 ÷ 2 = 3", 640, 590, 50, ad, cores={4: GREEN})
    text(c, "a frente: divide", 640, 650, 26, "bold", INK2, ad)
    expr(c, "5 − 3 = 2", 1280, 590, 50, ae, cores={4: GREEN})
    text(c, "os expoentes: subtrai", 1280, 650, 26, "bold", INK2, ae)
    af = ep(t, C["16.f"], 0.5)
    if af > 0:
        rrect(c, 300, 690, 760, 80, 18, GREEN, 0.12 * af)
        ftext(c, "3 · 10^2 = 300 vezes", 680, 745, 46, "black", GREEN, af)
    ag = ep(t, C["16.g"], 0.5)
    if ag > 0:
        boxed(c, 1110, 690, 520, 80, BLUE, ag, 0.08)
        text_mid(c, "RAZÃO = divisão que compara", 1370, 730, 30, "black", BLUE, ag)


def b_quanto(c, t, C, B):
    head_seq(c, t, C, [("17", "QUANTO MAIOR?", "É SUBTRAÇÃO", PURPLE), ("18", "ATALHO", "OLHE A RESPOSTA QUE ELA QUER", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18"])
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 210, 1320, 100, BLUE, aa, 0.08)
            text(c, "DIFERENÇA = resultado da subtração, na MESMA unidade (reais)", W / 2, 272, 34, "black", INK, aa)
        ab = ep(t, C["17.b"], 0.5)
        expr(c, "6·10^5 − 2·10^3", W / 2, 400, 70, ab)
        chip(c, "iguale os expoentes ANTES", W / 2, 480, AMBER, ab, 30)
        acc = ep(t, C["17.c"], 0.5)
        expr(c, "2·10^3 = 0,02·10^5", 700, 590, 52, acc, cores={2: GREEN})
        text(c, "5 − 3 = 2 casas", 1340, 600, 32, "black", INK2, acc)
        ad = ep(t, C["17.d"], 0.5)
        if ad > 0:
            rrect(c, 420, 670, 1080, 110, 22, GREEN, 0.12 * ad)
            expr(c, "6 − 0,02 = 5,98 → 5,98·10^5 reais", W / 2, 725, 46, ad, cores={4: GREEN, 6: GREEN})
        return
    a0 = ep(t, C["18.a"], 0.5)
    K.atalho(c, 300, 220, 1320, 140, "ATALHO", ["olhe a RESPOSTA que a pergunta quer"], a0, 40)
    ab, acc = ep(t, C["18.b"], 0.5), ep(t, C["18.c"], 0.5)
    for k, (a, tit, sub, op, col) in enumerate(((ab, "em VEZES", "quantas vezes maior", "÷  DIVIDE", PURPLE),
                                               (acc, "na UNIDADE", "reais, quilos, metros", "−  SUBTRAI", BLUE))):
        if a <= 0:
            continue
        x = 640 + k * 640
        card(c, x - 270, 420, 540, 340, a)
        text(c, tit, x, 500, 46, "black", col, a)
        text(c, sub, x, 560, 30, "bold", INK2, a)
        text_mid(c, op, x, 670, 60, "black", col, a)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Para somar, primeiro o mesmo expoente.", "Iguale sempre pelo maior expoente.",
          "“Quantas vezes” divide; “quanto” subtrai."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1340, 60)


ERROS = [("3·10⁵ + 8·10⁴ + 2·10⁴ = 13·10⁵", "somar 3, 8 e 2 é uma conta normal",
          "notas diferentes: iguale primeiro → 4·10⁵"),
         ("somar os expoentes numa soma: 11·10⁹", "na multiplicação a gente soma expoentes, e a regra fica na cabeça",
          "somar expoentes só vale no PRODUTO; na adição, iguale primeiro"),
         ("“quantas vezes maior” com subtração", "a palavra “maior” lembra diferença",
          "“vezes” pede divisão: quantas Luas cabem na Terra"),
         ("8·10⁹ ÷ 2·10⁶ = “3 vezes maior”", "9 − 6 dá 3, e o 3 estava na conta",
          "o 3 é o EXPOENTE: 4·10³ = 4 000 vezes")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


# ======================================================================
# Questão 4 do material
# ======================================================================

ALTS4 = [("A", "= 1,3·10^4", "somou 13 e mexeu só na vírgula", RED), ("B", "= 1,3·10^{13}", "os dois erros juntos", RED),
         ("C", "= 4·10^5", "", GREEN), ("D", "= 4·10^{13}", "somou os expoentes", RED),
         ("E", "= 13·10^5", "somou sem igualar", RED)]


def _enunciado4(c, a):
    mline(c, ["Três municípios vizinhos têm,"], 190, 250, 34, a)
    mline(c, ["respectivamente, ", ("m", "3·10^5"), ", ", ("m", "8·10^4"), " e"], 190, 310, 34, a)
    mline(c, [("m", "2·10^4"), " habitantes. A população"], 190, 370, 34, a)
    mline(c, ["total da região é"], 190, 430, 34, a)


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · SOMA COM EXPOENTES DIFERENTES", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    _enunciado4(c, a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    if t >= C["24.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS4, 1000, 210, 680, 40, C["25.ok"], "C", cues_in, cues_x, gap=16)
    pause_timer(c, t, C["24.end"] - 1.9, 470, 620)
    if t >= C["25"]:
        ra = ep(t, C["25"], 0.4) * (1 - ep(t, C["26"], 0.4) * 0.0)
        rrect(c, 170, 470, 760, 340, 18, "#FFFFFF", ra, shadow=True)
        text(c, "mesmo expoente: o maior, 5", 550, 520, 28, "black", PURPLE, ep(t, C["25.a"], 0.4))
        expr(c, "8·10^4 = 0,8·10^5", 550, 585, 40, ep(t, C["25.b"], 0.4), cores={2: GREEN})
        expr(c, "2·10^4 = 0,2·10^5", 550, 655, 40, ep(t, C["25.c"], 0.4), cores={2: GREEN})
        expr(c, "3 + 0,8 + 0,2 = 4 → 4·10^5", 550, 730, 40, ep(t, C["25.d"], 0.4), cores={8: GREEN})
        text(c, "400 000 habitantes", 550, 795, 26, "black", GREEN, ep(t, C["25.e"], 0.4))


# ======================================================================
# Questão 7 do material
# ======================================================================

ALTS7 = [("A", "8 vezes", "multiplicou por 10, não por 100", RED), ("B", "80 vezes", "", GREEN),
         ("C", "800 vezes", "perdeu a vírgula do 0,8", RED), ("D", "2 vezes", "parou no 24 − 22", RED),
         ("E", "100 vezes", "olhou só os expoentes", RED)]


def _enunciado7(c, a, y0=250):
    mline(c, ["A massa da Terra é de aproximadamente"], 190, y0, 34, a)
    mline(c, [("m", "6·10^{24}"), " kg e a da Lua, ", ("m", "7,5·10^{22}"), " kg."], 190, y0 + 60, 34, a)
    mline(c, ["A massa da Terra é maior que a da Lua"], 190, y0 + 120, 34, a)
    mline(c, ["em cerca de"], 190, y0 + 180, 34, a)


def b_q7(c, t, C, B):
    sid = which(t, C, ["27", "28", "29", "30"])
    if sid in ("27", "30"):
        head(c, t, C[sid], "QUESTÃO · QUANTAS VEZES MAIOR", "PAUSE E TENTE" if sid == "27" else "E AS OUTRAS?", BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C["27.a"], 0.4) if sid == "27" else ep(t, C["30"], 0.4)
        _enunciado7(c, a0)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        cues_in = {L: (C[f"27.q{L.lower()}"] if sid == "27" else C["30"]) for L in "ABCDE"}
        cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
        ok = C["30"] if sid == "30" else 1e9
        if t >= cues_in["A"] - 0.3:
            K.alternativas(c, t, C, ALTS7, 1080, 230, 600, 44, ok, "B", cues_in, cues_x, gap=24)
        if sid == "27":
            pause_timer(c, t, C["27.end"] - 1.9, 470, 640)
        return
    if sid == "28":
        head(c, t, C["28"], "RESOLVENDO", "EM VEZES → DIVISÃO", PURPLE)
        card(c, *CARD_R)
        a0 = ep(t, C["28"], 0.4)
        expr(c, "6·10^{24}/7,5·10^{22}", 520, 300, 66, a0)
        aa = ep(t, C["28.a"], 0.4)
        expr(c, "6 ÷ 7,5 = 60 ÷ 75 = 0,8", 520, 450, 42, aa, cores={8: GREEN})
        ab = ep(t, C["28.b"], 0.4)
        expr(c, "24 − 22 = 2", 520, 540, 42, ab, cores={4: GREEN})
        acc = ep(t, C["28.c"], 0.4)
        expr(c, "0,8·10^2 = 0,8 · 100", 520, 640, 46, acc)
        ad = ep(t, C["28.d"], 0.4)
        if ad > 0:
            rrect(c, 300, 690, 440, 100, 20, GREEN, 0.14 * ad)
            text_mid(c, "= 80", 520, 740, 60, "black", GREEN, ad)
        # Terra enchendo de Luas, com contador
        ae = ep(t, C["28.c"], 0.5)
        terra(c, 1300, 480, 250, ae)
        nluas = int(round(80 * ep(t, C["28.c"] + 0.3, max(0.5, C["28.e"] - C["28.c"] - 0.3))))
        luas_na_terra(c, 1300, 480, 250, nluas, ae, rl=19)
        if ae > 0:
            rrect(c, 1530, 210, 150, 90, 18, "#FFFFFF", ae, shadow=True)
            text_mid(c, str(nluas), 1605, 255, 52, "black", GREEN if nluas >= 80 else INK, ae)
            text(c, "Luas", 1605, 330, 26, "black", INK2, ae)
        return
    # 29: conferência por ordem de grandeza
    head(c, t, C["29"], "CONFERINDO SEM CONTA", "ORDEM DE GRANDEZA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["29.a"], 0.5)
    expr(c, "10^{24} ÷ 10^{22} = 10^2", 560, 270, 54, aa, cores={4: GREEN})
    text(c, "diferença de 2 → umas 100 vezes", 560, 360, 30, "black", INK2, aa)
    ab = ep(t, C["29.b"], 0.5)
    expr(c, "6 < 7,5", 1400, 270, 60, ab, cores={0: AMBER, 1: AMBER, 2: AMBER})
    text(c, "o de cima é menor", 1400, 360, 30, "black", INK2, ab)
    acc = ep(t, C["29.c"], 0.5)
    x0, x1, y = 300, 1620, 560
    if acc > 0:
        line(c, x0, y, x1, y, INK2, acc, 5)
        for v in range(0, 101, 20):
            xv = lerp(x0, x1, v / 100)
            line(c, xv, y - 14, xv, y + 14, INK2, acc, 4)
            text(c, str(v), xv, y + 56, 28, "bold", INK2, acc)
        xc = lerp(x0, x1, 1.0)
        c.drawCircle(xc, y, 14, paint(PURPLE, acc))
        text(c, "100", xc, y - 40, 30, "black", PURPLE, acc)
        text(c, "um pouco abaixo de 100", lerp(x0, x1, 0.82), y - 100, 30, "black", AMBER, acc)
    ad = ep(t, C["29.d"], 0.5)
    if ad > 0:
        xv = lerp(x0, x1, 0.8)
        c.drawCircle(xv, y, 18, paint(GREEN, ad))
        rrect(c, xv - 230, 660, 460, 100, 20, GREEN, 0.14 * ad)
        text_mid(c, "80: coerente ✓", xv, 710, 44, "black", GREEN, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ORDEM DE GRANDEZA", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    expr(c, "7,2·10^5", W / 2, 320, 110, aa)
    text(c, "qual é a ESCALA?", W / 2, 440, 36, "black", INK2, aa)
    ab = ep(t, C["32.b"], 0.5)
    chip(c, "ORDEM DE GRANDEZA", W / 2, 520, BLUE, ab, 34)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        expr(c, "10^5 ?", W / 2, 640, 70, acc, cores={0: RED, 1: RED})
        selo(c, W / 2 + 330, 650, acc, "NÃO é o expoente escrito", RED, -5, 28)
    pill(c, "ep. 4 · ordem de grandeza e a conta de guardanapo", W / 2, 790, PURPLE, size=30, a=ep(t, C["32.d"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Você também somava os expoentes numa soma?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, notas=b_notas, condicao=b_condicao, igualar=b_igualar,
              bolso=b_bolso, exercicio=b_exercicio, vezes=b_vezes, quanto=b_quanto, recap=b_recap, erros=b_erros,
              q4=b_q4, q7=b_q7, ponte=b_ponte, cta=b_cta)
