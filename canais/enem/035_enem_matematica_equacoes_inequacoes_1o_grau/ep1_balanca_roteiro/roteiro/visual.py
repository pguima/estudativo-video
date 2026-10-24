"""Visual — Equações e Inequações do 1º Grau, Episódio 1: a equação como balança e o roteiro de resolução (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: balanca() (balança de feira com 3 sacos e 4 pesinhos; os pesinhos saem dos dois pratos e os pratos se
dividem em 3, com o ponteiro sempre no meio), passos() (as linhas da conta com a operação feita "nos dois pratos" ao lado),
prova() (a prova real: substitui e mostra se a balança fecha).
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
_s = importlib.util.spec_from_file_location("comum035", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacoes_ep1_balanca_roteiro.mp4"
CARD_R = K.CARD_R
SACO = "#C9A06A"
SACO2 = "#A97F48"
FERRO = "#8C939C"
MADEIRA = "#7A5A3A"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]. Devolve [(x_ini, largura)] de cada trecho."""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    pos = []
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        pos.append((x, w_))
        x += w_
    return pos


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def saco(c, cx, by, s, a, rot="x", col=None):
    """saco de feira apoiado em by (base), largura ~ s"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.42, by)
    p.cubicTo(cx - s * 0.62, by - s * 0.55, cx - s * 0.38, by - s * 0.95, cx - s * 0.18, by - s * 1.02)
    p.lineTo(cx + s * 0.18, by - s * 1.02)
    p.cubicTo(cx + s * 0.38, by - s * 0.95, cx + s * 0.62, by - s * 0.55, cx + s * 0.42, by)
    p.close()
    c.drawPath(p, paint(col or SACO, a))
    c.drawPath(p, paint(SACO2, a, stroke=3))
    # amarração
    rrect(c, cx - s * 0.22, by - s * 1.16, s * 0.44, s * 0.16, s * 0.06, SACO2, a)
    fmid(c, rot, cx, by - s * 0.45, s * 0.46, "black", "#FFFFFF", a)


def pesinho(c, cx, by, s, a, rot="1 kg"):
    """peso de ferro (trapézio) apoiado em by"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.5, by); p.lineTo(cx - s * 0.36, by - s * 0.62)
    p.lineTo(cx + s * 0.36, by - s * 0.62); p.lineTo(cx + s * 0.5, by); p.close()
    c.drawPath(p, paint(FERRO, a))
    rrect(c, cx - s * 0.14, by - s * 0.8, s * 0.28, s * 0.2, s * 0.08, FERRO, a)
    fmid(c, rot, cx, by - s * 0.3, s * 0.26, "black", "#FFFFFF", a)


def bloco_kg(c, cx, by, w, h, a, rot, col=None):
    if a <= 0:
        return
    rrect(c, cx - w / 2, by - h, w, h, 10, col or "#5C6672", a, shadow=True)
    fmid(c, rot, cx, by - h / 2, min(h * 0.42, w * 0.3), "black", "#FFFFFF", a)


def balanca(c, cx, cy, a, tira=0.0, divide=0.0, rot_dir=None, n_pesos=4, esc=1.0):
    """balança de feira equilibrada. Pivô em (cx, cy). Prato da esquerda: 3 sacos + n_pesos pesinhos; da direita: bloco de 15 kg
    + n_pesos pesinhos (total 19 kg). tira (0→1): os pesinhos sobem e somem dos DOIS pratos. divide (0→1): cada prato se
    divide em 3 partes iguais (1 saco · 5 kg). O ponteiro fica sempre no meio."""
    if a <= 0:
        return
    e = esc
    half = 400 * e
    # base e coluna
    rrect(c, cx - 150 * e, cy + 330 * e, 300 * e, 34 * e, 12 * e, MADEIRA, a)
    rrect(c, cx - 16 * e, cy, 32 * e, 336 * e, 10 * e, MADEIRA, a)
    # mostrador e ponteiro (sempre no meio)
    c.drawCircle(cx, cy - 64 * e, 70 * e, paint("#FFFFFF", a))
    c.drawCircle(cx, cy - 64 * e, 70 * e, paint(INK2, a, stroke=4 * e))
    for k in (-2, -1, 0, 1, 2):
        ang = math.radians(-90 + k * 28)
        x1, y1 = cx + 52 * e * math.cos(ang), cy - 64 * e + 52 * e * math.sin(ang)
        x2, y2 = cx + 64 * e * math.cos(ang), cy - 64 * e + 64 * e * math.sin(ang)
        line(c, x1, y1, x2, y2, GREEN if k == 0 else GRAY, a, 4 * e if k == 0 else 2 * e)
    line(c, cx, cy - 64 * e, cx, cy - 120 * e, RED, a, 6 * e)
    c.drawCircle(cx, cy - 64 * e, 9 * e, paint(INK, a))
    # travessão
    rrect(c, cx - half, cy - 10 * e, 2 * half, 20 * e, 10 * e, MADEIRA, a)
    c.drawCircle(cx, cy, 16 * e, paint(INK, a))
    py = cy + 210 * e
    pw = 330 * e
    for sx in (-1, 1):
        xx = cx + sx * half
        line(c, xx, cy, xx - pw * 0.42, py, INK2, a, 2.5 * e)
        line(c, xx, cy, xx + pw * 0.42, py, INK2, a, 2.5 * e)
        c.drawOval(skia.Rect.MakeXYWH(xx - pw / 2, py - 12 * e, pw, 26 * e), paint("#B9BEC4", a))
        c.drawOval(skia.Rect.MakeXYWH(xx - pw / 2, py - 12 * e, pw, 26 * e), paint(INK2, a, stroke=2.5 * e))
    by = py - 8 * e
    up = 160 * e * ease_io(clamp(tira))
    ap = a * (1 - clamp(tira * 1.25))
    dv = ease_io(clamp(divide))
    xl, xr = cx - half, cx + half
    # prato da esquerda: 3 sacos (afastam-se ao dividir) e os pesinhos à direita deles
    for k in range(3):
        sx = xl - 92 * e + k * 74 * e + (k - 1) * 36 * e * dv
        saco(c, sx, by, 78 * e, a, "x", mix(SACO, "#9BD7A8", 0.0 if k else 0.8 * dv))
    for k in range(n_pesos):
        pesinho(c, xl + 82 * e + (k % 2) * 46 * e, by - (k // 2) * 46 * e - up, 44 * e, ap)
    # prato da direita: bloco de 15 kg que vira 3 de 5 kg, mais os pesinhos
    if dv < 0.5:
        bloco_kg(c, xr - 50 * e, by, 170 * e, 120 * e, a * (1 - dv * 2), "15 kg")
    if dv > 0:
        for k in range(3):
            bx = xr - 50 * e + (k - 1) * (56 * e + 34 * e * dv)
            bloco_kg(c, bx, by, 54 * e, 120 * e, a * clamp(dv * 2), "5", GREEN if k == 0 else None)
    for k in range(n_pesos):
        pesinho(c, xr + 82 * e + (k % 2) * 46 * e, by - (k // 2) * 46 * e - up, 44 * e, ap)
    # rótulos totais
    rl = "3x + 4" if tira < 0.5 else ("3x" if dv < 0.5 else "x")
    rr = rot_dir or ("19 kg" if tira < 0.5 else ("15 kg" if dv < 0.5 else "5 kg"))
    pill(c, rl, xl, py + 70 * e, BLUE, size=int(30 * e), a=a, anchor="center")
    pill(c, rr, xr, py + 70 * e, INK, size=int(30 * e), a=a, anchor="center")
    if dv > 0:
        for xx in (xl, xr):
            for k in (-1, 1):
                x_ = xx + k * 52 * e * (0.6 + 0.4 * dv) + (20 * e if xx == xr else -10 * e)
                for yy in range(int(by - 150 * e), int(by), int(16 * e)):
                    line(c, x_, yy, x_, yy + 8 * e, PURPLE, a * dv, 3)


def passos(c, t, rows, x, y0, size, dy, a_mult=1.0, xnota=None):
    """linhas da conta: rows = [(instante, expr, nota_dos_dois_pratos, cor_da_nota)]"""
    xnota = xnota or 1660
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        a *= a_mult
        if a <= 0:
            continue
        y = y0 + k * dy + d
        expr(c, ex, x, y, size, a, align="left")
        if nota:
            pill(c, nota, xnota, y, col or PURPLE, size=24, a=a, anchor="right", bounds=(0, 1920))


def prova(c, s, x, y, a, ok=True, size=30):
    """a prova real: substitui e diz se a balança fecha"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 160
    rrect(c, x, y - 40, w, 80, 22, mix("#FFFFFF", GREEN if ok else RED, 0.12), a)
    text(c, "PROVA REAL", x + 22, y - 12, 16, "black", GREEN if ok else RED, a, align="left", tracking=2)
    conferido(c, s, x + 22, y + 26, a, ok, size * 0.8)


def mini_balanca(c, cx, cy, a, ok=True, s=1.0):
    """ícone: balança reta (fecha) ou torta (não fecha)"""
    if a <= 0:
        return
    ang = 0 if ok else -14
    rrect(c, cx - 6 * s, cy, 12 * s, 70 * s, 4 * s, MADEIRA, a)
    rrect(c, cx - 40 * s, cy + 66 * s, 80 * s, 12 * s, 4 * s, MADEIRA, a)
    c.save(); c.translate(cx, cy); c.rotate(ang)
    rrect(c, -80 * s, -5 * s, 160 * s, 10 * s, 5 * s, GREEN if ok else RED, a)
    for sx in (-1, 1):
        c.drawOval(skia.Rect.MakeXYWH(sx * 80 * s - 30 * s, 26 * s, 60 * s, 12 * s), paint(GREEN if ok else RED, a))
        line(c, sx * 80 * s, 0, sx * 80 * s - 24 * s, 30 * s, INK2, a, 2)
        line(c, sx * 80 * s, 0, sx * 80 * s + 24 * s, 30 * s, INK2, a, 2)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÕES DO 1º GRAU", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "5(x-2) - 3(x-4) = 18", W / 2, 330, 96, aa, cores={2: AMBER})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 330, 470, 520, 150, 26, mix("#FFFFFF", GREEN, 0.14), ab)
        check_icon(c, 400, 528, 40, ab, GREEN)
        expr(c, "x = 8", 650, 545, 90, ab, cores={2: GREEN})
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1070, 470, 520, 150, 26, mix("#FFFFFF", RED, 0.12), acc)
        check_icon(c, 1140, 528, 40, acc, RED, "x")
        expr(c, "x = 20", 1390, 545, 90, acc, cores={2: RED})
        pill(c, "1 sinal errado · e está nas alternativas", 1330, 670, AMBER, size=26, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        for k in range(5):
            badge_num(c, k + 1, 700 + k * 130, 790, ep(t, C["01.d"] + 0.25 * k, 0.3), 30, bg=PURPLE)
        text(c, "ROTEIRO EM 5 PASSOS", W / 2, 880, 34, "black", PURPLE, ad, tracking=2)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver qualquer equação do 1º grau", "3x + 4 = 19  →  x = 5"),
            ("02.b", "com parênteses e frações", "5(x − 2) − 3(x − 4) = 18  ·  x/2 − (x − 4)/3 = 3"),
            ("02.c", "saber quando não tem solução ou tem infinitas", "0x = −1  ·  0x = 0")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "O ESPELHO", 560, 280, 34, "black", PURPLE, aa)
        text(c, "série de Expressões Algébricas", 560, 324, 24, "bold", GRAY, aa)
        text(c, "o menos antes do parêntese vira TODOS os sinais", 560, 400, 24, "bold", INK2, aa)
        expr(c, "-(x-4)", 560, 520, 76, ep(t, C["03.a"] + 1.5, 0.4), cores={0: RED})
        expr(c, "= -x + 4", 560, 650, 76, ep(t, C["03.a"] + 3.5, 0.4), cores={1: PURPLE, 3: PURPLE})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "O MMC", 1360, 280, 34, "black", BLUE, ab)
        text(c, "série de Frações", 1360, 324, 24, "bold", GRAY, ab)
        text(c, "o menor múltiplo comum dos denominadores", 1360, 400, 24, "bold", INK2, ab)
        a2 = ep(t, C["03.b"] + 2.0, 0.4)
        ftext(c, "múltiplos de 2:  2 · 4 · 6 · 8", 1360, 500, 36, "black", INK, a2)
        ftext(c, "múltiplos de 3:  3 · 6 · 9", 1360, 570, 36, "black", INK, a2)
        a3 = ep(t, C["03.b"] + 3.6, 0.4)
        if a3 > 0:
            rrect(c, 1200, 610, 320, 90, 22, mix("#FFFFFF", GREEN, 0.16), a3)
            fmid(c, "MMC = 6", 1360, 655, 50, "black", GREEN, a3)
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: a balança
# ======================================================================

def b_balanca(c, t, C, B):
    head(c, t, B["start"], "UMA BALANÇA DE FEIRA", "EQUILIBRADA", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    ab = ep(t, C["04.b"], 0.5)
    tira = ep(t, C["04.d"] + 1.0, 1.6)
    divide = ep(t, C["04.e"] + 1.0, 1.6)
    balanca(c, W / 2, 330, aa, tira, divide, None if ab > 0 else "?")
    acc = ep(t, C["04.c"], 0.5) * (1 - ep(t, C["04.d"], 0.4))
    if acc > 0:
        selo(c, W / 2, 790, acc, "QUANTO PESA CADA SACO?", AMBER, -2, 40)
    ad = ep(t, C["04.d"], 0.5) * (1 - ep(t, C["04.e"], 0.4))
    if ad > 0:
        pill(c, "− 4 kg NOS DOIS PRATOS", W / 2, 790, PURPLE, size=34, a=ad, anchor="center")
    ae = ep(t, C["04.e"], 0.5) * (1 - ep(t, C["04.f"], 0.4))
    if ae > 0:
        pill(c, "÷ 3 NOS DOIS PRATOS", W / 2, 790, PURPLE, size=34, a=ae, anchor="center")
    af = ep(t, C["04.f"], 0.5)
    if af > 0:
        pill(c, "1 saco = 5 kg · e o ponteiro nunca saiu do meio", W / 2, 790, GREEN, size=34, a=af, anchor="center")


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "A BALANÇA VIRA EQUAÇÃO", "EQUAÇÃO · INCÓGNITA · RAIZ", BLUE),
                       ("06", "EQUAÇÃO DO 1º GRAU", "ax + b = 0", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        balanca(c, 480, 340, aa, 0, 0, esc=0.55)
        expr(c, "3x + 4 = 19", 1240, 330, 100, aa, cores={0: RED})
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            rrect(c, 900, 430, 700, 90, 20, mix("#FFFFFF", BLUE, 0.10), ab)
            linha(c, [("EQUAÇÃO", BLUE), (": igualdade com um valor escondido", INK)], 1250, 475, 30, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 900, 545, 700, 90, 20, mix("#FFFFFF", BLUE, 0.10), acc)
            linha(c, [("INCÓGNITA", BLUE), (": o valor escondido (o x)", INK)], 1250, 590, 30, acc)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            rrect(c, 900, 660, 700, 110, 20, mix("#FFFFFF", GREEN, 0.14), ad)
            linha(c, [("RAIZ", BLUE), (" ou ", INK), ("SOLUÇÃO", BLUE), (": deixa a igualdade verdadeira", INK)], 1250, 695,
                  28, ad)
            expr(c, "x = 5", 1250, 745, 44, ad, cores={2: GREEN})
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "o x aparece sozinho, sem estar ao quadrado", W / 2, 260, 30, "bold", GRAY, aa)
        expr(c, "ax + b = 0", 760, 400, 110, aa, cores={0: PURPLE, 2: PURPLE})
        pill(c, "a ≠ 0", 1260, 400, AMBER, size=40, a=aa, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 470, 800, 170, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "RAIZ", 680, 565, 30, "black", PURPLE, ab)
        expr(c, "x = -b/a", 1020, 555, 80, ab, cores={2: PURPLE})
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        expr(c, "3x - 15 = 0", 620, 730, 58, acc)
        expr(c, "→ x = -(-15)/3 = 5", 1200, 730, 58, acc, cores={4: GREEN})
        pill(c, "o mesmo saco", 1560, 800, GREEN, size=24, a=acc, anchor="center")


# ======================================================================
# bloco b — a balança na conta
# ======================================================================

def b_naconta(c, t, C, B):
    head(c, t, B["start"], "A BALANÇA NA CONTA", "LINHA POR LINHA", PURPLE)
    card(c, *CARD_R)
    balanca(c, 1380, 300, ep(t, C["07"], 0.5), ep(t, C["07.b"] + 0.4, 1.2), ep(t, C["07.c"] + 0.4, 1.2), esc=0.5)
    rows = [(C["07.a"], "3x + 4 = 19", "", None),
            (C["07.b"], "3x = 15", "− 4 nos dois lados", PURPLE),
            (C["07.c"], "x = 5", "÷ 3 nos dois lados", PURPLE)]
    passos(c, t, rows, 240, 300, 80, 150, xnota=960)
    prova(c, "3 · 5 + 4 = 19  ·  a balança fecha", 240, 760, ep(t, C["07.d"], 0.5))


# ======================================================================
# bloco c — os dois princípios e o apelido
# ======================================================================

def b_principios(c, t, C, B):
    head_seq(c, t, C, [("08", "O QUE PODE NA BALANÇA", "DOIS PRINCÍPIOS", PURPLE),
                       ("09", "ATALHO", "“PASSAR PARA O OUTRO LADO”", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        rows = [("08.a", "PRINCÍPIO ADITIVO", "somar ou subtrair o MESMO número dos dois lados", "+ 7  e  + 7"),
                ("08.b", "PRINCÍPIO MULTIPLICATIVO", "multiplicar ou dividir os dois lados pelo MESMO número ≠ 0",
                 "÷ 3  e  ÷ 3")]
        for k, (cue, tit, s, ex) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 240 + k * 240
            rrect(c, 220, y, 1480, 200, 24, "#FFFFFF", a, shadow=True)
            rrect(c, 220, y, 14, 200, 7, PURPLE, a)
            text(c, tit, 270, y + 62, 34, "black", PURPLE, a, align="left")
            para(c, s, 270, y + 120, 32, "bold", INK2, a, 1000, 40)
            pill(c, ex, 1620, y + 100, GREEN, size=34, a=a, anchor="right")
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            regra(c, "todo o resto é APELIDO dessas duas regras", W / 2, 770, acc, 34)
        return
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 220, 220, 1480, 200, "O APELIDO", ["o que SOMA passa SUBTRAINDO", "o que MULTIPLICA passa DIVIDINDO"], aa, 34)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 470, ab, "QUEM PASSA DIVIDINDO LEVA O PRÓPRIO SINAL", AMBER, -1, 30)
    acc = ep(t, C["09.c"], 0.5)
    expr(c, "-2x = 10", 600, 620, 76, acc, cores={0: RED})
    expr(c, "→ x = 10/(-2) = -5", 1180, 620, 76, ep(t, C["09.c"] + 2.0, 0.4), cores={4: RED, 6: GREEN})
    prova(c, "−2 · (−5) = 10  ·  fecha", 600, 770, ep(t, C["09.d"], 0.5))


# ======================================================================
# bloco d — o roteiro
# ======================================================================

ROTEIRO = [("10.a", "DENOMINADORES", "multiplique tudo pelo MMC"),
           ("10.b", "PARÊNTESES", "distributiva, cuidando do sinal"),
           ("10.c", "SEPARE", "x de um lado, números do outro"),
           ("10.d", "REDUZA E DIVIDA", "pelo número que multiplica o x"),
           ("10.e", "CONFIRA", "substitua na equação do começo")]


def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "O ROTEIRO", "5 PASSOS, SEMPRE NA MESMA ORDEM", PURPLE)
    card(c, *CARD_R)
    for k, (cue, tit, s) in enumerate(ROTEIRO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 112 + d
        col = GREEN if k == 4 else PURPLE
        rrect(c, 260, y - 46, 1400, 92, 20, mix("#FFFFFF", col, 0.08), a)
        badge_num(c, k + 1, 320, y, a, 30, bg=col)
        text(c, tit, 390, y + 14, 40, "black", col, a, align="left")
        text(c, s, 1620, y + 12, 30, "bold", INK2, a, align="right")


# ======================================================================
# bloco e — com parênteses
# ======================================================================

def b_parenteses(c, t, C, B):
    head_seq(c, t, C, [("11", "COM PARÊNTESES", "ATENÇÃO AO −3 · (−4)", PURPLE), ("12", "A PROVA REAL", "A BALANÇA FECHA?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    a0 = ep(t, C["11.a"], 0.5)
    expr(c, "5(x-2) - 3(x-4) = 18", W / 2, 250, 66, a0, cores={2: RED})
    if sid == "11":
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            linha(c, [("5x − 10", BLUE)], 620, 390, 60, ab)
            pill(c, "5 · x  e  5 · (−2)", 620, 460, BLUE, size=24, a=ab, anchor="center")
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            linha(c, [("− 3x ", RED), ("+ 12", GREEN)], 1260, 390, 60, acc)
            pill(c, "(−3) · (−4) = +12", 1260, 460, AMBER, size=26, a=acc, anchor="center")
        rows = [(C["11.d"], "2x + 2 = 18", "juntando", BLUE),
                (C["11.d"] + 3.2, "2x = 16", "− 2 nos dois lados", PURPLE),
                (C["11.d"] + 5.4, "x = 8", "÷ 2 nos dois lados", PURPLE)]
        passos(c, t, rows, 560, 560, 56, 90, xnota=1620)
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        prova(c, "5 · (8 − 2) − 3 · (8 − 4) = 30 − 12 = 18", 300, 380, aa)
        mini_balanca(c, 1520, 340, aa, True)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 470, 1400, 140, 22, mix("#FFFFFF", RED, 0.07), ab)
        linha(c, [("5x − 10 ", INK), ("− 3x − 12", RED), (" = 18", INK), ("   →   x = 20", RED)], W / 2, 540, 50, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        prova(c, "5 · 18 − 3 · 16 = 42  ≠ 18", 300, 720, acc, False)
        mini_balanca(c, 1520, 680, acc, False)
        pill(c, "a balança não fecha", 1520, 800, RED, size=24, a=acc, anchor="center")


# ======================================================================
# bloco f — com frações (o parêntese disfarçado)
# ======================================================================

def b_fracoes(c, t, C, B):
    head_seq(c, t, C, [("13", "COM FRAÇÕES", "PASSO 1: O MMC", PURPLE), ("14", "O ESPELHO NO NUMERADOR", "x = 10", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    a0 = ep(t, C["13.a"], 0.5)
    expr(c, "x/2 - x-4/3 = 3", W / 2, 270, 80, a0)
    if sid == "13":
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            pill(c, "MMC(2, 3) = 6 · multiplique TUDO por 6", W / 2, 400, GREEN, size=30, a=ab, anchor="center")
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            linha(c, [("6 · x/2 = ", INK), ("3x", BLUE)], 560, 510, 46, acc)
            linha(c, [("6 · 3 = ", INK), ("18", BLUE)], 1360, 510, 46, acc)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            # o traço vira parêntese
            m = ep(t, C["13.d"] + 2.6, 1.0)
            rrect(c, 360, 590, 1200, 200, 24, mix("#FFFFFF", AMBER, 0.12), ad)
            expr(c, "- x-4/3", 700, 690, 76, ad * (1 - m), cores={0: RED})
            expr(c, "- (x-4)/3", 700, 690, 76, ad * m, cores={0: RED, 1: AMBER})
            arrow(c, 900, 690, 1020, 690, INK, ad, 5, 16)
            expr(c, "- 2(x-4)", 1250, 690, 76, ep(t, C["13.d"] + 4.4, 0.5), cores={0: RED, 1: AMBER})
            text(c, "o traço é um parêntese disfarçado", W / 2, 820, 28, "black", AMBER, ad)
        return
    expr(c, "3x - 2(x-4) = 18", W / 2, 380, 64, a0, cores={2: AMBER})
    rows = [(C["14.a"], "3x - 2x + 8 = 18", "(−2) · (−4) = +8", AMBER),
            (C["14.b"], "x + 8 = 18", "juntando", BLUE),
            (C["14.b"] + 2.4, "x = 10", "− 8 nos dois lados", PURPLE)]
    passos(c, t, rows, 400, 480, 54, 80, xnota=1620)
    acc = ep(t, C["14.c"], 0.5) * (1 - ep(t, C["14.d"], 0.4))
    prova(c, "10/2 − 6/3 = 5 − 2 = 3  ·  fecha", 400, 760, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 715, 1200, 100, 22, mix("#FFFFFF", RED, 0.08), ad)
        linha(c, [("esqueceu o parêntese: 3x − 2x ", INK), ("− 8", RED), (" = 18  →  ", INK), ("x = 26", RED)], W / 2, 765,
              40, ad)


# ======================================================================
# bloco g — quando o x some
# ======================================================================

def b_xsome(c, t, C, B):
    head_seq(c, t, C, [("15", "O X SUMIU", "NENHUMA SOLUÇÃO", RED), ("16", "O X SUMIU DE NOVO", "INFINITAS SOLUÇÕES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        rows = [(C["15.a"], "2(x+3) = 2x + 5", "", None), (C["15.a"] + 3.0, "2x + 6 = 2x + 5", "parênteses", BLUE),
                (C["15.b"], "0x = -1", "− 2x nos dois lados", PURPLE)]
        passos(c, t, rows, 300, 280, 66, 120, xnota=1120)
        ab = ep(t, C["15.b"] + 2.5, 0.5)
        if ab > 0:
            linha(c, [("ou seja: ", GRAY), ("6 = 5", RED)], 560, 680, 56, ab)
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            mini_balanca(c, 1420, 380, acc, False, 1.4)
            rrect(c, 1200, 560, 440, 120, 22, mix("#FFFFFF", RED, 0.12), acc)
            text(c, "NENHUMA", 1420, 610, 40, "black", RED, acc)
            text(c, "SOLUÇÃO", 1420, 656, 30, "black", RED, acc)
            text(c, "falso para qualquer x", 1420, 730, 24, "bold", GRAY, acc)
        return
    rows = [(C["16.a"], "3(x-2) = 3x - 6", "", None), (C["16.a"] + 3.0, "3x - 6 = 3x - 6", "parênteses", BLUE),
            (C["16.b"], "0x = 0", "− 3x nos dois lados", PURPLE)]
    passos(c, t, rows, 300, 270, 62, 105, xnota=1120)
    acc = ep(t, C["16.c"], 0.5) * (1 - ep(t, C["16.d"], 0.4))
    if acc > 0:
        mini_balanca(c, 1420, 330, acc, True, 1.4)
        rrect(c, 1200, 500, 440, 120, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        text(c, "INFINITAS", 1420, 550, 40, "black", GREEN, acc)
        text(c, "IDENTIDADE", 1420, 596, 26, "black", BLUE, acc)
        text(c, "vale para todo x", 1420, 670, 24, "bold", GRAY, acc)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        K.atalho(c, 260, 570, 1400, 230, "ATALHO · O X SUMIU? LEIA O QUE SOBROU",
                 ["número = outro número (falso)  →  NENHUMA", "0 = 0 (sempre verdade)  →  INFINITAS"], ad, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "COM O ROTEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    text(c, "RESOLVA", W / 2, 240, 28, "black", GRAY, aa * (1 - ep(t, C["18"], 0.3)), tracking=2)
    expr(c, "4(x-1) - 2(x-5) = 12", W / 2, 330, 72, aa, cores={2: RED})
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t < C["18"]:
        return
    ab = ep(t, C["18.a"], 0.5)
    if ab > 0:
        linha(c, [("4x − 4", BLUE)], 620, 450, 54, ab)
        linha(c, [("− 2x ", RED), ("+ 10", GREEN)], 1260, 450, 54, ep(t, C["18.a"] + 2.4, 0.4))
        pill(c, "espelho: (−2) · (−5) = +10", 1260, 515, AMBER, size=24, a=ep(t, C["18.a"] + 2.4, 0.4), anchor="center")
    rows = [(C["18.b"], "2x + 6 = 12", "juntando", BLUE), (C["18.b"] + 2.6, "2x = 6", "− 6 nos dois lados", PURPLE),
            (C["18.b"] + 3.8, "x = 3", "÷ 2 nos dois lados", PURPLE)]
    passos(c, t, rows, 560, 590, 48, 66, xnota=1620)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        rrect(c, 160, 560, 360, 230, 22, mix("#FFFFFF", GREEN, 0.12), acc)
        text(c, "PROVA REAL", 340, 600, 18, "black", GREEN, acc, tracking=2)
        text(c, "4 · 2 = 8", 340, 650, 30, "black", INK, acc)
        text(c, "−2 · (−2) = +4", 340, 700, 30, "black", INK, acc)
        conferido(c, "8 + 4 = 12", 220, 760, acc, True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O que se faz num prato se faz no outro.",
          "O que multiplica passa dividindo, com o próprio sinal.",
          "O traço da fração é um parêntese disfarçado."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("−3(x − 4) = −3x − 12", "o −4 já tinha sinal de menos, parece que ele fica",
          "menos vezes menos dá MAIS: −3x + 12"),
         ("x/2 − (x − 4)/3 = 3  →  3x − 2x − 8 = 18", "o menos parece encostado só no x",
          "o traço é um parêntese disfarçado: o menos atinge o numerador inteiro"),
         ("−2x = 10  →  x = 5", "“passar para o outro lado” parece sempre trocar o sinal",
          "trocar sinal é só para quem soma; quem multiplica passa dividindo com o próprio sinal: x = −5"),
         ("1/3 + 1/4 = 2/7", "é só somar em cima e somar embaixo",
          "fração se soma pelo MMC: 4/12 + 3/12 = 7/12")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


# ======================================================================
# questão 6 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS6 = [("A", "os preços se igualam em uma entrega de 12 km", "12 do parêntese", RED),
         ("B", "os preços se igualam em uma entrega de 4 km", "R$ 4 virou 4 km", RED),
         ("C", "A é mais barata em qualquer entrega, por R$ 4,00", "inverteu", RED),
         ("D", "B é mais barata em qualquer entrega, por R$ 4,00", "", GREEN),
         ("E", "B é mais barata só nas entregas de até 12 km", "não se cruzam", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · EU FAÇO, VOCÊ CONFERE", "DUAS EMPRESAS DE FRETE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4) * (1 - ep(t, C["25"], 0.4))
    yend = _enunciado(c, [("Duas empresas de frete calculam o preço, em reais, de uma entrega de x quilômetros. A empresa A "
                           "cobra 40 + 3x; a empresa B cobra 3(x + 12). Comparando as duas, conclui-se que", INK)], a0, 250,
                      30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS6, 1000, 240, 680, 30, C["25.ok"], "D", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 110)
    if t >= C["25"]:
        ap = ep(t, C["25"], 0.4)
        _painel(c, ap)
        text(c, "A: 40 + 3x     B: 3(x + 12)", 550, 285, 30, "black", GRAY, ap)
        rows = [(C["25.a"], "B = 3x + 36", "", None),
                (C["25.b"], "40 + 3x = 3x + 36", "", None),
                (C["25.c"], "0x = -4", "", None)]
        passos(c, t, rows, 240, 370, 46, 80)
        acc = ep(t, C["25.c"] + 2.4, 0.4)
        if acc > 0:
            pill(c, "o x sumiu e sobrou algo falso: NUNCA se igualam", 550, 590, RED, size=20, a=acc, anchor="center")
        ad = ep(t, C["25.d"], 0.4)
        if ad > 0:
            linha(c, [("40 − 36 = ", INK), ("R$ 4,00", GREEN), (" a menos em B", INK)], 550, 650, 32, ad)
        ae = ep(t, C["25.e"], 0.4)
        if ae > 0:
            rrect(c, 200, 690, 700, 120, 18, mix("#FFFFFF", GREEN, 0.10), ae)
            text(c, "10 km: A = 70 · B = 66", 550, 735, 26, "black", INK2, ae)
            text(c, "100 km: A = 340 · B = 336", 550, 785, 26, "black", INK2, ae)
    af = ep(t, C["26.f"], 0.5)
    if af > 0:
        pill(c, "volta em Sistemas Lineares: RETAS PARALELAS", 1340, 820, PURPLE, size=24, a=af, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MONTAR A EQUAÇÃO", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        mini_balanca(c, 420, 330, aa, True, 1.2)
        text(c, "resolver: a parte fácil", 420, 520, 34, "black", GREEN, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        rrect(c, 760, 260, 1000, 260, 26, "#FFFFFF", ab, shadow=True)
        para(c, "“daqui a 4 anos, o pai terá o triplo da idade do filho”", 810, 340, 40, "black", INK, ab, 900, 52)
        expr(c, "→ ? = ?", 1260, 470, 56, ab, cores={1: AMBER, 3: AMBER})
    pill(c, "ep. 2 · montar a equação a partir do texto", W / 2, 700, PURPLE, size=32, a=ep(t, C["28.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Qual desses 4 erros você já cometeu?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, balanca=b_balanca, definicao=b_definicao,
              naconta=b_naconta, principios=b_principios, roteiro=b_roteiro, parenteses=b_parenteses, fracoes=b_fracoes,
              xsome=b_xsome, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, ponte=b_ponte, cta=b_cta)
