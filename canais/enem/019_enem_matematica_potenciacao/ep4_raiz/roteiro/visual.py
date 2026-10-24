"""Visual — Potenciação e Radiciação, Episódio 4: Raiz, a operação que desfaz a potência (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências/raízes no expr, atalho, selo_teste...).
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep4_raiz.mp4"
CARD_R = K.CARD_R
PISO = "#E9DDC7"
PISO_L = "#CDBB9B"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


def curva(c, x1, y1, x2, y2, bend, col, a, w=5, rotulo=None, rsize=30, rcol=None):
    """seta curva (quadrática) de (x1,y1) a (x2,y2); bend > 0 sobe, < 0 desce; rótulo no meio da curva"""
    if a <= 0:
        return
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - bend
    p = skia.Path(); p.moveTo(x1, y1); p.quadTo(mx, my, x2, y2)
    pe = paint(col, a, stroke=w, cap_round=True)
    c.drawPath(p, pe)
    ang = math.atan2(y2 - my, x2 - mx)
    for s_ in (-1, 1):
        c.drawLine(x2, y2, x2 - 18 * math.cos(ang + s_ * 0.5), y2 - 18 * math.sin(ang + s_ * 0.5), pe)
    if rotulo:
        ftext(c, rotulo, mx, (y1 + y2) / 2 - bend / 2 + (-14 if bend > 0 else 34), rsize, "black", rcol or col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A REGRA QUE NÃO EXISTE", RED)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "√{9+16} = √{9} + √{16} ?", W / 2, 280, 84, aa)
    ac, ad = ep(t, C["01.c"], 0.5), ep(t, C["01.d"], 0.5)
    if ac > 0:
        card(c, 230, 400, 660, 300, ac)
        text(c, "um lado", 560, 450, 28, "black", GRAY, ac)
        expr(c, "√{9+16} = √{25} = 5", 560, 560, 54, ac, cores={4: BLUE})
    if ad > 0:
        card(c, 1030, 400, 660, 300, ad)
        text(c, "o outro lado", 1360, 450, 28, "black", GRAY, ad)
        expr(c, "√{9} + √{16} = 3 + 4 = 7", 1360, 560, 54, ad, cores={6: AMBER})
    ae = ep(t, C["01.e"], 0.5)
    fmid(c, "≠", W / 2, 550, 110, "black", RED, ae)
    selo(c, W / 2, 780, ae, "ESSA REGRA NÃO EXISTE", RED, -3, 38)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "quando uma raiz EXISTE", "e quando não existe"), ("02.b", "como ela trata os NEGATIVOS", "o detalhe do módulo"),
            ("02.c", "quais regras valem DE VERDADE", "e a que não existe")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 280 + j * 165 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 52, 30, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "DO EPISÓDIO 1", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "POTÊNCIA = a base vezes ela mesma", 560, 260, 32, "black", BLUE, aa)
    expr(c, "5^2 = 5 · 5 = 25", 560, 420, 64, aa, cores={6: GREEN})
    expr(c, "2^3 = 2 · 2 · 2 = 8", 560, 590, 64, ep(t, C["03.a"] + 2.0, 0.5), cores={8: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    text(c, "BASE NEGATIVA", 1360, 260, 32, "black", BLUE, ab)
    expr(c, "(-5)^2 = 25", 1360, 420, 64, ab, cores={2: GREEN})
    chip(c, "expoente PAR → +", 1360, 500, GREEN, ab, 28)
    acc = ep(t, C["03.c"], 0.5)
    expr(c, "(-2)^3 = -8", 1360, 620, 64, acc, cores={2: RED})
    chip(c, "expoente ÍMPAR → −", 1360, 700, RED, acc, 28)


# ======================================================================
# blocos A/B — ida e volta, pela geometria
# ======================================================================

def piso(c, x, y, lado, n, a, lit=1.0):
    """piso quadrado de n × n lajotas, canto superior esquerdo (x, y)"""
    if a <= 0:
        return
    s = lado / n
    for i in range(n):
        for j in range(n):
            k = i * n + j
            al = a * clamp(lit * n * n - k)
            if al <= 0:
                continue
            rrect(c, x + j * s + 2, y + i * s + 2, s - 4, s - 4, 4, PISO, al)
    c.drawRect(skia.Rect.MakeXYWH(x, y, lado, lado), paint(PISO_L, a, stroke=5))


def b_piso(c, t, C, B):
    frame(c, t, B["start"], "UM PISO QUADRADO", "QUANTO MEDE O LADO?", BLUE)
    a0 = ep(t, C["04"], 0.5)
    x, y, L = 300, 230, 470
    piso(c, x, y, L, 9, a0, prog(t, C["04"], 1.6))
    text_mid(c, "81 m²", x + L / 2, y + L / 2, 64, "black", INK, a0 * 0.9)
    # lado
    ac = ep(t, C["04.c"], 0.5)
    line(c, x, y + L + 40, x + L, y + L + 40, BLUE, a0, 4)
    for xx in (x, x + L):
        line(c, xx, y + L + 28, xx, y + L + 52, BLUE, a0, 4)
    text(c, "lado = ?", x + L / 2, y + L + 95, 36, "black", BLUE, a0 * (1 - ac))
    text(c, "lado = 9 m", x + L / 2, y + L + 95, 36, "black", GREEN, ac)
    aa = ep(t, C["04.a"], 0.5)
    text(c, "área do quadrado", 1300, 280, 30, "black", GRAY, aa)
    text(c, "lado · lado = lado²", 1300, 345, 46, "black", PURPLE, aa)
    ab = ep(t, C["04.b"], 0.5)
    expr(c, "? · ? = 81", 1300, 480, 72, ab * (1 - ac))
    expr(c, "9 · 9 = 81", 1300, 480, 72, ac, cores={0: GREEN, 2: GREEN})
    ad = ep(t, C["04.d"], 0.5)
    chip(c, "o lado mede 9 metros", 1300, 640, GREEN, ad, 34)


def b_idavolta(c, t, C, B):
    frame(c, t, B["start"], "IDA E VOLTA", "A RAIZ DESFAZ A POTÊNCIA", PURPLE)
    a0 = ep(t, C["05"], 0.5)
    xa, xb, y = 560, 1360, 470
    for x, s in ((xa, "9"), (xb, "81")):
        c.drawCircle(x, y, 110, paint("#FFFFFF", a0))
        c.drawCircle(x, y, 110, paint(LIGHT, a0, stroke=5))
        text_mid(c, s, x, y, 100, "black", INK, a0)
    aa = ep(t, C["05.a"], 0.6)
    curva(c, xa + 90, y - 110, xb - 90, y - 110, 130, PURPLE, aa, 6, "IDA: elevar ao quadrado", 34)
    ftext(c, "9^2 = 81", W / 2, 250, 36, "black", PURPLE, aa)
    ab = ep(t, C["05.b"], 0.6)
    curva(c, xb - 90, y + 110, xa + 90, y + 110, -130, GREEN, ab, 6, "VOLTA: ?", 34)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, W / 2 - 130, y - 45, 260, 90, 22, "#FFFFFF", acc, shadow=True)
        text_mid(c, "RAIZ", W / 2, y, 52, "black", GREEN, acc)
    pill(c, "RAIZ = a operação que DESFAZ a potência", W / 2, 790, BLUE, size=32, a=ep(t, C["05.d"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_nomes(c, t, C, B):
    head_seq(c, t, C, [("06", "COMO SE ESCREVE", "OS NOMES DAS PARTES", BLUE), ("07", "NO GERAL", "IDA E VOLTA LADO A LADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        size = 230
        cx, cy = 820, 470
        w = K.math_w("√{81}", size)
        x0 = cx - w / 2
        a0 = ep(t, C["06"], 0.5)
        expr(c, "√{81}", cx, cy, size, a0, cores={0: INK})
        ad = ep(t, C["06.d"], 0.5)
        # índice 2 "fantasma"
        ac = ep(t, C["06.c"], 0.5)
        if ac > 0:
            fmid(c, "2", x0 + 8, cy - 105, 70, "black", PURPLE, ac * (1 - 0.65 * ad))
            if ad > 0:
                strike(c, x0 - 17, cy - 105, x0 + 33, cy - 105, ad, RED, ad)
            arrow(c, x0 - 160, cy - 200, x0 + 10, cy - 120, PURPLE, ac, 5, 16, progress=ac)
            text(c, "ÍNDICE", x0 - 190, cy - 230, 34, "black", PURPLE, ac)
            text(c, "qual potência desfaz", x0 - 190, cy - 192, 24, "bold", INK2, ac)
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            arrow(c, x0 - 150, cy + 200, x0 + 50, cy + 70, BLUE, aa, 5, 16, progress=aa)
            text(c, "RADICAL", x0 - 170, cy + 250, 34, "black", BLUE, aa)
            text(c, "o sinal da raiz", x0 - 170, cy + 288, 24, "bold", INK2, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            rrect(c, x0 + w * 0.42, cy - 105, w * 0.6, 210, 24, BLUE, 0.10 * ab)
            arrow(c, x0 + w + 200, cy - 160, x0 + w + 20, cy - 60, BLUE, ab, 5, 16, progress=ab)
            text(c, "RADICANDO", x0 + w + 260, cy - 200, 34, "black", BLUE, ab)
            text(c, "o número de dentro", x0 + w + 260, cy - 162, 24, "bold", INK2, ab)
        if ad > 0:
            chip(c, "índice 2 = RAIZ QUADRADA (o 2 nem se escreve)", W / 2, 760, BLUE, ad, 30)
        ae = ep(t, C["06.e"], 0.5)
        expr(c, "= 9", cx + w / 2 + 170, cy, 150, ae, cores={1: GREEN})
        return
    a0 = ep(t, C["07.a"], 0.5)
    ab = ep(t, C["07.b"], 0.5)
    expr(c, "√[n]{a} = b", 620, 400, 120, a0, cores={0: GREEN, 1: INK, 2: INK})
    expr(c, "b^n = a", 1340, 400, 120, ab, cores={0: PURPLE, 1: INK, 2: INK})
    acc = ep(t, C["07.c"], 0.5)
    fmid(c, "⟺", W / 2 + 20, 400, 100, "black", AMBER, acc)
    chip(c, "⟺ = uma vale EXATAMENTE QUANDO a outra vale", W / 2, 600, AMBER, acc, 30)
    text(c, "VOLTA (raiz)", 620, 520, 32, "black", GREEN, a0)
    text(c, "IDA (potência)", 1340, 520, 32, "black", PURPLE, ab)
    ad = ep(t, C["07.d"], 0.5)
    expr(c, "√{81} = 9 ⟺ 9^2 = 81", W / 2, 730, 54, ad, cores={0: GREEN, 1: GREEN, 2: GREEN, 4: PURPLE, 5: PURPLE, 6: PURPLE})


def cubo(c, cx, cy, s, a, col=None, aresta_lbl=None, la=1.0):
    """cubo em perspectiva cavaleira: face da frente de lado s centrada em (cx, cy)"""
    if a <= 0:
        return
    col = col or BLUE
    d = s * 0.42
    x0, y0 = cx - s / 2, cy - s / 2 + d / 2
    front = skia.Path(); front.addRect(skia.Rect.MakeXYWH(x0, y0, s, s))
    top = skia.Path(); top.moveTo(x0, y0); top.lineTo(x0 + d, y0 - d); top.lineTo(x0 + s + d, y0 - d); top.lineTo(x0 + s, y0); top.close()
    side = skia.Path(); side.moveTo(x0 + s, y0); side.lineTo(x0 + s + d, y0 - d); side.lineTo(x0 + s + d, y0 + s - d)
    side.lineTo(x0 + s, y0 + s); side.close()
    c.drawPath(front, paint(mix("#FFFFFF", col, 0.18), a))
    c.drawPath(top, paint(mix("#FFFFFF", col, 0.32), a))
    c.drawPath(side, paint(mix("#FFFFFF", col, 0.45), a))
    for p in (front, top, side):
        c.drawPath(p, paint(col, a, stroke=4))
    if aresta_lbl:
        line(c, x0, y0 + s + 34, x0 + s, y0 + s + 34, AMBER, a * la, 4)
        for xx in (x0, x0 + s):
            line(c, xx, y0 + s + 22, xx, y0 + s + 46, AMBER, a * la, 4)
        text(c, aresta_lbl, x0 + s / 2, y0 + s + 90, 34, "black", AMBER, a * la)


def b_cubo(c, t, C, B):
    frame(c, t, B["start"], "E SE O ÍNDICE FOR 3?", "RAIZ CÚBICA", BLUE)
    a0 = ep(t, C["08.a"], 0.5)
    acc = ep(t, C["08.c"], 0.5)
    cubo(c, 500, 450, 280, a0, BLUE, None)
    text_mid(c, "8 L", 500, 480, 64, "black", INK, a0)
    if a0 > 0:
        lbl = "aresta = ?" if acc < 0.5 else "aresta = 2 dm"
        x0, y0 = 500 - 140, 450 - 140 + 280 * 0.21
        line(c, x0, y0 + 314, x0 + 280, y0 + 314, AMBER, a0, 4)
        for xx in (x0, x0 + 280):
            line(c, xx, y0 + 302, xx, y0 + 326, AMBER, a0, 4)
        text(c, lbl, 500, y0 + 370, 34, "black", GREEN if acc >= 0.5 else AMBER, a0)
        text(c, "(1 litro = um cubo de 10 cm de aresta)", 500, y0 + 410, 22, "bold", GRAY, a0 * acc)
    ab = ep(t, C["08.b"], 0.5)
    text(c, "volume do cubo", 1300, 260, 30, "black", GRAY, ab)
    text(c, "aresta · aresta · aresta = aresta³", 1300, 320, 36, "black", PURPLE, ab)
    expr(c, "?^3 = 8", 1300, 440, 72, ab * (1 - acc))
    expr(c, "2^3 = 8", 1300, 440, 72, acc, cores={0: GREEN})
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        boxed(c, 1010, 520, 580, 130, PURPLE, ad, 0.08)
        expr(c, "√[3]{8} = 2", 1300, 585, 72, ad, cores={0: PURPLE, 2: GREEN})
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        text(c, "quadrado → lado = raiz QUADRADA", 1300, 720, 28, "black", BLUE, ae)
        text(c, "cubo → aresta = raiz CÚBICA", 1300, 770, 28, "black", BLUE, ae)


def b_confere(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "CONFIRA ELEVANDO DE VOLTA", GREEN)
    aa = ep(t, C["09.a"], 0.5)
    boxed(c, 260, 210, 1400, 560, GREEN, aa, 0.06)
    text(c, "ATALHO", W / 2, 260, 24, "black", GREEN, aa, tracking=2)
    text(c, "confira elevando de volta", W / 2, 320, 46, "black", INK, aa)
    for k, (cue, volta, ida) in enumerate((("09.b", "√{81} = 9", "9^2 = 81"), ("09.c", "√[3]{8} = 2", "2^3 = 8"))):
        a = ep(t, C[cue], 0.5)
        y = 450 + k * 150
        expr(c, volta, 620, y, 66, a, cores={0: GREEN})
        arrow(c, 820, y, 1060, y, LIGHT, a, 5, 16, progress=a)
        expr(c, ida, 1260, y, 66, ep(t, C[cue] + 1.5, 0.4), cores={0: PURPLE})
        check_icon(c, 1460, y - 10, 30, ep(t, C[cue] + 2.4, 0.4), GREEN)
    text(c, "a volta sempre se confere com a ida", W / 2, 730, 32, "bold", INK2, ep(t, C["09.d"], 0.5))


# ======================================================================
# bloco C — quando a raiz existe
# ======================================================================

def b_existe(c, t, C, B):
    head_seq(c, t, C, [("10", "RAIZ DE MENOS QUATRO?", "QUEM, AO QUADRADO, DÁ −4?", AMBER),
                       ("11", "NÚMEROS REAIS", "TODOS OS NÚMEROS DA RETA", BLUE),
                       ("12", "E A RAIZ CÚBICA DE −8?", "ÍNDICE ÍMPAR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12"])
    if sid == "10":
        a0 = ep(t, C["10"], 0.5)
        expr(c, "√{-4} = ?", W / 2, 270, 100, a0)
        for k, (cue, s, cx) in enumerate((("10.b", "2^2 = 2 · 2 = 4", 560), ("10.c", "(-2)^2 = (-2) · (-2) = 4", 1360))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            card(c, cx - 360, 380, 720, 190, a)
            expr(c, s, cx, 450, 52, a, cores={len(s.split()) - 1: GREEN})
            text(c, "positivo", cx, 530, 28, "black", GREEN, a)
        ad = ep(t, C["10.d"], 0.5)
        text(c, "nenhum número AO QUADRADO dá negativo", W / 2, 650, 38, "black", INK, ad)
        selo(c, W / 2, 750, ep(t, C["10.e"], 0.5), "√−4 NÃO EXISTE nos números reais", RED, -3, 36)
        return
    if sid == "11":
        a0 = ep(t, C["11.a"], 0.5)
        x0, x1, y = 260, 1660, 450
        val = lambda v: lerp(x0, x1, (v + 5) / 10)
        line(c, x0 - 30, y, x1 + 30, y, INK2, a0, 5)
        for v in range(-4, 5):
            line(c, val(v), y - 12, val(v), y + 12, INK2, a0, 3)
            text(c, str(v).replace("-", "−"), val(v), y + 52, 26, "bold", GRAY, a0)
        marcas = [(-3, "−3", "inteiro", BLUE), (-0.5, "−0,5", "decimal", AMBER), (1.5, "3/2", "fração", PURPLE),
                  (3.7, "3,7", "decimal", AMBER)]
        for k, (v, s, tipo, col) in enumerate(marcas):
            a = ep(t, C["11.a"] + 0.5 + 0.4 * k, 0.4)
            c.drawCircle(val(v), y, 14, paint(col, a))
            expr(c, s, val(v), y - 80, 40, a, cores={0: col})
            text(c, tipo, val(v), y - 130, 22, "black", col, a)
        chip(c, "inteiros · frações · decimais · positivos e negativos", W / 2, 620, BLUE, ep(t, C["11.b"], 0.5), 30)
        ac = ep(t, C["11.c"], 0.5)
        if ac > 0:
            ftext(c, "nenhum ponto da reta é √−4", W / 2, 740, 38, "black", RED, ac)
        return
    a0 = ep(t, C["12"], 0.5)
    expr(c, "√[3]{-8} = ?", W / 2, 270, 100, a0)
    ab = ep(t, C["12.b"], 0.5)
    expr(c, "(-2) · (-2) · (-2) = -8", W / 2, 430, 64, ab, cores={6: RED})
    chip(c, "expoente ÍMPAR conserva o sinal", W / 2, 540, PURPLE, ep(t, C["12.c"], 0.5), 32)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        boxed(c, 640, 610, 640, 150, GREEN, ad, 0.08)
        expr(c, "√[3]{-8} = -2", W / 2, 670, 72, ad, cores={2: GREEN})
        text(c, "existe, e é negativa", W / 2, 740, 26, "black", GREEN, ad)


TABELA = [("13.a", "Par", "Positivo", "Existe", "√{16} = 4", GREEN), ("13.b", "Par", "Negativo", "NÃO existe", "√{-4}", RED),
          ("13.c", "Ímpar", "Positivo", "Existe", "√[3]{8} = 2", GREEN),
          ("13.d", "Ímpar", "Negativo", "Existe, negativa", "√[3]{-8} = -2", PURPLE)]


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "QUANDO A RAIZ EXISTE", "NOS NÚMEROS REAIS", PURPLE)
    a0 = ep(t, C["13"], 0.5)
    cols = [330, 600, 930, 1320]
    for x, s in zip(cols, ("ÍNDICE", "RADICANDO", "NOS REAIS", "EXEMPLO")):
        text(c, s, x, 240, 24, "black", GRAY, a0, tracking=1)
    line(c, 200, 262, 1720, 262, "#E6E6E2", a0, 3)
    for k, (cue, i_, r_, e_, ex, col) in enumerate(TABELA):
        a = ep(t, C[cue], 0.45)
        if a <= 0:
            continue
        y = 320 + k * 82
        rrect(c, 200, y - 36, 1520, 72, 14, mix("#FFFFFF", col, 0.07), a)
        text_mid(c, i_, cols[0], y, 32, "black", INK, a)
        text_mid(c, r_, cols[1], y, 32, "black", INK, a)
        text_mid(c, e_, cols[2], y, 32, "black", col, a)
        expr(c, ex, cols[3], y, 40, a)
        if col == RED:
            check_icon(c, cols[3] + 110, y - 8, 22, a, RED, "x")
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        K.atalho(c, 300, 650, 1320, 170, "ATALHO",
                 ["índice PAR com negativo dentro: não existe  ·  índice ÍMPAR: copie o sinal"], ae, 30)


# ======================================================================
# bloco D — a sutileza do módulo
# ======================================================================

def b_modulo(c, t, C, B):
    head_seq(c, t, C, [("14", "A SUTILEZA", "RAIZ DE (−5)²", AMBER), ("15", "POR QUÊ?", "DOIS PONTOS DE PARTIDA, UM DESTINO", PURPLE),
                       ("16", "MÓDULO", "O VALOR SEM SINAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    if sid == "14":
        a0 = ep(t, C["14.a"], 0.5)
        expr(c, "√{(-5)^2} = ?", W / 2, 280, 100, a0)
        ab = ep(t, C["14.b"], 0.5)
        acc = ep(t, C["14.c"], 0.5)
        if ab > 0:
            boxed(c, 300, 400, 560, 150, AMBER, ab, 0.10)
            pill(c, "PARECE...", 340, 420, AMBER, size=24, a=ab, bounds=(0, 1920))
            expr(c, "= -5 ?", 580, 495, 64, ab * (1 - 0.6 * acc), cores={1: AMBER})
            if acc > 0:
                strike(c, 470, 495, 700, 495, acc, RED, acc)
        expr(c, "(-5)^2 = 25", 1340, 440, 64, acc, cores={2: INK})
        ad = ep(t, C["14.d"], 0.5)
        expr(c, "√{25} = 5", 1340, 580, 72, ad, cores={2: GREEN})
        chip(c, "POSITIVO!", 1340, 700, GREEN, ep(t, C["14.d"] + 1.0, 0.4), 34)
        return
    if sid == "15":
        a0 = ep(t, C["15.a"], 0.5)
        xl, xr = 520, 1400
        ym, yp, y25 = 300, 620, 460
        for s, y, col in (("−5", ym, RED), ("+5", yp, GREEN)):
            c.drawCircle(xl, y, 80, paint("#FFFFFF", a0)); c.drawCircle(xl, y, 80, paint(LIGHT, a0, stroke=5))
            text_mid(c, s, xl, y, 64, "black", col, a0)
        c.drawCircle(xr, y25, 95, paint("#FFFFFF", a0)); c.drawCircle(xr, y25, 95, paint(LIGHT, a0, stroke=5))
        text_mid(c, "25", xr, y25, 72, "black", INK, a0)
        arrow(c, xl + 90, ym + 20, xr - 100, y25 - 30, PURPLE, a0, 5, 16, progress=a0)
        arrow(c, xl + 90, yp - 20, xr - 100, y25 + 30, PURPLE, ep(t, C["15.a"] + 2.5, 0.5), 5, 16,
              progress=ep(t, C["15.a"] + 2.5, 0.5))
        text(c, "IDA: ao quadrado", 960, 330, 30, "black", PURPLE, a0)
        ab = ep(t, C["15.b"], 0.6)
        curva(c, xr - 60, y25 + 90, xl + 80, yp + 40, -120, GREEN, ab, 6, "VOLTA: um destino só", 30)
        chip(c, "√ devolve só o valor SEM SINAL", W / 2, 800, GREEN, ep(t, C["15.c"], 0.5), 30)
        return
    a0 = ep(t, C["16.a"], 0.5)
    x0, x1, y = 300, 1620, 400
    val = lambda v: lerp(x0, x1, (v + 6) / 12)
    line(c, x0 - 20, y, x1 + 20, y, INK2, a0, 5)
    for v in range(-6, 7):
        line(c, val(v), y - 12, val(v), y + 12, INK2, a0, 3)
        text(c, str(v).replace("-", "−"), val(v), y + 50, 24, "bold", GRAY, a0)
    if a0 > 0:
        for v, col in ((-5, RED), (5, GREEN)):
            c.drawCircle(val(v), y, 15, paint(col, a0))
        for v in (-5, 5):
            yy = y - 60
            line(c, val(v), yy, val(0), yy, BLUE, a0, 5)
            text(c, "distância 5", (val(v) + val(0)) / 2, yy - 20, 26, "black", BLUE, a0)
    ab = ep(t, C["16.b"], 0.5)
    expr(c, "|-5| = 5", 640, 560, 64, ab, cores={2: BLUE})
    expr(c, "|5| = 5", 1280, 560, 64, ab, cores={2: BLUE})
    text(c, "módulo = entre duas barrinhas em pé", W / 2, 640, 26, "bold", INK2, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        boxed(c, 560, 680, 800, 130, PURPLE, acc, 0.08)
        expr(c, "√{a^2} = |a|", W / 2, 745, 72, acc, cores={0: PURPLE, 2: PURPLE})
        text(c, "e não simplesmente a", 1390, 755, 26, "black", RED, acc, align="left")


def b_impar_sinal(c, t, C, B):
    frame(c, t, B["start"], "E NO ÍNDICE ÍMPAR?", "O SINAL VOLTA", PURPLE)
    aa = ep(t, C["17.a"], 0.5)
    expr(c, "√[3]{(-2)^3} = √[3]{-8} = -2", W / 2, 320, 84, aa, cores={4: GREEN})
    ab = ep(t, C["17.b"], 0.5)
    chip(c, "índice ímpar: SEM módulo", W / 2, 470, PURPLE, ab, 34)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 560, 1200, 220, "ATALHO", ["índice PAR: TIRA o sinal", "índice ÍMPAR: MANTÉM o sinal"], acc, 38)


# ======================================================================
# bloco E — propriedades que valem
# ======================================================================

def b_produto(c, t, C, B):
    head_seq(c, t, C, [("18", "RAIZ DE UM PRODUTO", "VALE?", PURPLE), ("19", "RAIZ DE UM QUOCIENTE", "VALE?", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    if sid == "18":
        chip(c, "PRODUTO = resultado de uma multiplicação", W / 2, 230, BLUE, ep(t, C["18.a"], 0.5), 28)
        ab, acc = ep(t, C["18.b"], 0.5), ep(t, C["18.c"], 0.5)
        expr(c, "√{4·9} = √{36} = 6", 560, 400, 62, ab, cores={4: GREEN})
        expr(c, "√{4} · √{9} = 2 · 3 = 6", 1360, 400, 62, acc, cores={8: GREEN})
        fmid(c, "=", W / 2, 400, 80, "black", GREEN, acc)
        K.selo_teste(c, 1500, 520, acc, ok=True, s="TESTE COM 4 E 9: CONFERE")
        ad = ep(t, C["18.d"], 0.5)
        if ad > 0:
            boxed(c, 560, 620, 800, 140, PURPLE, ad, 0.08)
            expr(c, "√{a·b} = √{a} · √{b}", W / 2, 690, 66, ad, cores=mono("√{a·b} = √{a} · √{b}", PURPLE))
        return
    aa, ab = ep(t, C["19.a"], 0.5), ep(t, C["19.b"], 0.5)
    expr(c, "√{100/4} = √{25} = 5", 560, 400, 58, aa, cores={4: GREEN})
    expr(c, "√{100}/√{4} = 10/2 = 5", 1360, 400, 58, ab, cores={4: GREEN})
    fmid(c, "=", W / 2, 400, 80, "black", GREEN, ab)
    K.selo_teste(c, 1500, 520, ab, ok=True, s="TESTE: CONFERE")
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        boxed(c, 560, 620, 800, 160, PURPLE, acc, 0.08)
        expr(c, "√{a/b} = √{a}/√{b}", W / 2, 700, 62, acc, cores=mono("√{a/b} = √{a}/√{b}", PURPLE))
        text(c, "QUOCIENTE = resultado de uma divisão", W / 2, 810, 24, "black", BLUE, acc)


def b_ida_volta2(c, t, C, B):
    frame(c, t, B["start"], "RAIZ E DEPOIS O QUADRADO", "UMA DESFAZ A OUTRA", PURPLE)
    aa = ep(t, C["20.a"], 0.5)
    expr(c, "(√{7})^2 = ?", W / 2, 300, 110, aa)
    ab = ep(t, C["20.b"], 0.6)
    xa, xb, xc_, y = 500, 960, 1420, 520
    if ab > 0:
        for x, s in ((xa, "7"), (xb, "√{7}"), (xc_, "7")):
            c.drawCircle(x, y, 85, paint("#FFFFFF", ab)); c.drawCircle(x, y, 85, paint(LIGHT, ab, stroke=5))
            expr(c, s, x, y, 60, ab)
        curva(c, xa + 80, y - 40, xb - 80, y - 40, 70, GREEN, ab, 5, "VOLTA (√)", 26)
        curva(c, xb + 80, y - 40, xc_ - 80, y - 40, 70, PURPLE, ep(t, C["20.b"] + 1.2, 0.5), 5, "IDA (²)", 26)
    acc = ep(t, C["20.c"], 0.5)
    chip(c, "sobra o 7", xc_, 650, GREEN, acc, 32)
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        boxed(c, 660, 700, 600, 110, PURPLE, ad, 0.08)
        expr(c, "(√{a})^2 = a", W / 2, 755, 60, ad, cores=mono("(√{a})^2 = a", PURPLE))


def b_raiz_raiz(c, t, C, B):
    frame(c, t, B["start"], "RAIZ DENTRO DE RAIZ", "MULTIPLIQUE OS ÍNDICES", PURPLE)
    aa = ep(t, C["21.a"], 0.5)
    expr(c, "√{√[3]{64}}", 440, 300, 110, aa)
    ab, acc = ep(t, C["21.b"], 0.5), ep(t, C["21.c"], 0.5)
    text(c, "o caminho longo", 440, 430, 26, "black", GRAY, ab)
    expr(c, "√[3]{64} = 4", 440, 510, 54, ab, cores={2: INK})
    text(c, "porque 4³ = 64", 440, 570, 24, "bold", INK2, ab)
    expr(c, "√{4} = 2", 440, 660, 54, acc, cores={2: GREEN})
    line(c, 820, 230, 820, 800, "#E6E6E2", ab, 3)
    ad, ae = ep(t, C["21.d"], 0.5), ep(t, C["21.e"], 0.5)
    if ad > 0:
        K.atalho(c, 900, 220, 780, 300, "ATALHO", ["multiplique os índices", ("m", "2 · 3 = 6")], ad, 40)
    if ae > 0:
        expr(c, "√{√[3]{64}} = √[6]{64} = 2", 1290, 620, 60, ae, cores={2: PURPLE, 4: GREEN})
        text(c, "porque 2⁶ = 64 · num passo só", 1290, 720, 28, "black", INK2, ae)


def b_dividir_indice(c, t, C, B):
    frame(c, t, B["start"], "DÁ PARA ENCOLHER O ÍNDICE?", "DIVIDA ÍNDICE E EXPOENTE", PURPLE)
    aa, ab = ep(t, C["22.a"], 0.5), ep(t, C["22.b"], 0.5)
    expr(c, "√[4]{4} = √[4]{2^2}", 640, 300, 96, aa, alfas={1: ab, 2: ab}, cores={2: INK})
    acc, ad, ae = ep(t, C["22.c"], 0.5), ep(t, C["22.d"], 0.5), ep(t, C["22.e"], 0.5)
    if acc > 0:
        chip(c, "÷ 2 no índice E no expoente", 1460, 250, AMBER, acc, 30)
    if ad > 0:
        text(c, "índice 4 ÷ 2 = 2", 1460, 335, 32, "black", PURPLE, ad)
        text(c, "expoente 2 ÷ 2 = 1", 1460, 380, 32, "black", PURPLE, ad)
    expr(c, "= √{2}", 1080, 300, 96, ae, cores={1: GREEN})
    af = ep(t, C["22.f"], 0.5)
    if af > 0:
        card(c, 300, 500, 1320, 180, af)
        text(c, "confira com conta exata", W / 2, 545, 24, "black", GRAY, af)
        expr(c, "√[4]{16} = 2", 700, 615, 58, af, cores={2: GREEN})
        fmid(c, "e", W / 2, 615, 40, "black", GRAY, af)
        expr(c, "√{4} = 2", 1220, 615, 58, af, cores={2: GREEN})
        K.atalho(c, 300, 700, 1320, 120, "ATALHO", ["divida índice e expoente pelo MESMO número: o valor não muda"], af, 30)


def b_soma(c, t, C, B):
    frame(c, t, B["start"], "E A SOMA?", "A PROPRIEDADE QUE NÃO EXISTE", RED)
    aa, ab = ep(t, C["23.a"], 0.5), ep(t, C["23.b"], 0.5)
    expr(c, "√{9+16} = √{25} = 5", 560, 290, 60, aa, cores={4: BLUE})
    expr(c, "√{9} + √{16} = 3 + 4 = 7", 1360, 290, 60, ab, cores={6: AMBER})
    acc = ep(t, C["23.c"], 0.5)
    fmid(c, "≠", W / 2, 290, 90, "black", RED, acc)
    K.selo_teste(c, 1470, 372, acc, ok=False, s="TESTE COM 9 E 16: NÃO CONFERE")
    ad = ep(t, C["23.d"], 0.5)
    if ad > 0:
        boxed(c, 460, 470, 1000, 125, RED, ad, 0.07)
        expr(c, "√{a+b} ≠ √{a} + √{b}", W / 2, 525, 64, ad, cores=mono("√{a+b} ≠ √{a} + √{b}", RED))
        text(c, "nem na subtração", W / 2, 630, 26, "black", RED, ad)
    ae = ep(t, C["23.e"], 0.5)
    if ae > 0:
        K.atalho(c, 360, 670, 1200, 145, "ATALHO", ["na dúvida, teste com números de raiz exata (9 e 16)"], ae, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Raiz desfaz a potência.", "Raiz de índice par devolve sempre o positivo.",
          "A raiz se distribui no produto e na divisão, nunca na soma."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["24", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "24" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("√(a + b) = √a + √b", "com a multiplicação funciona", "teste: √(9 + 16) = 5, e não 3 + 4 = 7"),
         ("√(a²) = a  (esquecer o módulo)", "a raiz desfaz o quadrado", "com −5: √25 = 5, positivo → √(a²) = |a|"),
         ("√−4 = −2", "a raiz cúbica de −8 é −2", "(−2)² = +4: raiz QUADRADA de negativo não existe nos reais")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["25", "26", "27"], ERROS)


# ======================================================================
# Questão 8 do material
# ======================================================================

ALTS = [("A", "= -14", "esqueceu o módulo: √x² = x", RED), ("B", "= -7", "fez só a 2ª parte", RED), ("C", "= 0", "", GREEN),
        ("D", "= 7", "fez só a 1ª parte", RED), ("E", "= 14", "tirou o sinal das duas", RED)]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ÍNDICE PAR E ÍNDICE ÍMPAR", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    text(c, "Para x = −7, o valor de", 190, 250, 36, "black", INK, a0, align="left")
    expr(c, "√{x^2} + √[3]{x^3}", 190, 340, 60, a0, align="left")
    text(c, "é", 600, 352, 36, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["30.xa"], "B": C["30.xb"], "D": C["30.xd"], "E": C["30.xe"]}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS, 960, 200, 720, 42, C["29.ok"], "C", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["28.end"] - 1.9, 470, 620)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 410, 740, 390, 18, "#FFFFFF", ra, shadow=True)
        ax = ep(t, C["29.x"], 0.4)
        chip(c, "x = −7 (um número escondido)", 540, 450, BLUE, ax, 26)
        aa = ep(t, C["29.a"], 0.4)
        text(c, "PAR → sem sinal", 540, 510, 22, "black", GREEN, aa)
        expr(c, "√{(-7)^2} = √{49} = 7", 540, 560, 40, aa, cores={4: GREEN})
        ab = ep(t, C["29.b"], 0.4)
        text(c, "ÍMPAR → conserva o sinal", 540, 625, 22, "black", PURPLE, ab)
        expr(c, "√[3]{(-7)^3} = √[3]{-343} = -7", 540, 675, 36, ab, cores={4: PURPLE})
        expr(c, "7 + (-7) = 0", 540, 755, 44, ep(t, C["29.c"], 0.4), cores={4: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SIMPLIFICAR RADICAIS", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    for k, s in enumerate(("√{50}", "5√{2}", "√{25·2}")):
        a = aa * ep(t, C["32.a"] + 1.0 * k, 0.4)
        x = 480 + k * 480
        card(c, x - 190, 260, 380, 220, a)
        expr(c, s, x, 370, 80, a)
    chip(c, "o MESMO número, três jeitos", W / 2, 560, BLUE, ep(t, C["32.b"], 0.5), 34)
    text(c, "a prova quer o MAIS SIMPLES", W / 2, 650, 36, "black", AMBER, ep(t, C["32.c"], 0.5))
    pill(c, "ep. 5 · simplificar radicais", W / 2, 770, PURPLE, size=32, a=ep(t, C["32.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Você achava que √(9 + 16) dava 7?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, piso=b_piso, idavolta=b_idavolta, nomes=b_nomes, cubo=b_cubo,
              confere=b_confere, existe=b_existe, tabela=b_tabela, modulo=b_modulo, impar_sinal=b_impar_sinal,
              produto=b_produto, ida_volta2=b_ida_volta2, raiz_raiz=b_raiz_raiz, dividir_indice=b_dividir_indice, soma=b_soma,
              recap=b_recap, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
