"""Visual — Função Afim, Episódio 2: o coeficiente angular (taxa), o linear (valor inicial) e o zero (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra, fr...).
Peças deste episódio: vela() (vela com chama e altura), cronometro() (relógio com o tempo decorrido), tabela() (linhas x/y
com as setas de diferença entre colunas), tanque() (tanque com nível de água), carro() (carro com etiqueta de preço),
camera() (a "foto no instante zero"), linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = b / definição · roxo = a, a taxa / regra · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum039", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_afim_ep2_taxa_valor_inicial_zero.mp4"
CARD_R = K.CARD_R
CERA = "#F6E7C8"
AGUA = "#5AA9E6"


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


def vela(c, x, ybase, a, alt_cm, px=20, rotulo=None, col_rot=None, chama=True, fantasma=False):
    """vela de pé com base em ybase; alt_cm em cm (px por cm). rotulo embaixo."""
    if a <= 0:
        return
    h = max(alt_cm, 0) * px
    if fantasma:
        c.drawRect(skia.Rect.MakeXYWH(x - 45, ybase - h, 90, h), paint(GRAY, a * 0.7, stroke=3))
    elif h > 0:
        rrect(c, x - 45, ybase - h, 90, h, 10, CERA, a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x - 45, ybase - h, 90, h), paint("#D9C59A", a, stroke=3))
    rrect(c, x - 80, ybase, 160, 18, 8, "#8A909C", a)
    if chama and h > 0 and not fantasma:
        line(c, x, ybase - h, x, ybase - h - 20, INK, a, 4)
        p = skia.Path()
        top = ybase - h - 68
        p.moveTo(x, top); p.quadTo(x + 22, top + 34, x, top + 46); p.quadTo(x - 22, top + 34, x, top)
        c.drawPath(p, paint("#FFB020", a))
    if rotulo:
        ftext(c, rotulo, x, ybase + 62, 34, "black", col_rot or INK, a)


def cronometro(c, cx, cy, r, a, minutos, rotulo=None, col=None):
    """relógio: ponteiro na fração de hora; rotulo (ex.: '10 min') abaixo"""
    if a <= 0:
        return
    col = col or INK
    c.drawCircle(cx, cy, r + 6, paint(col, a * 0.15))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(col, a, stroke=5))
    for k in range(12):
        ang = math.radians(k * 30 - 90)
        line(c, cx + math.cos(ang) * r * 0.82, cy + math.sin(ang) * r * 0.82, cx + math.cos(ang) * r * 0.94,
             cy + math.sin(ang) * r * 0.94, INK2, a, 3)
    ang = math.radians((minutos % 60) / 60 * 360 - 90)
    line(c, cx, cy, cx + math.cos(ang) * r * 0.75, cy + math.sin(ang) * r * 0.75, col, a, 6)
    c.drawCircle(cx, cy, 7, paint(col, a))
    if rotulo:
        ftext(c, rotulo, cx, cy + r + 48, 32, "black", col, a)


def tabela(c, x0, y0, xs, ys, a, cw=170, rh=86, rot_x="x", rot_y="y", diffs=None, a_diff=0.0, col_diff=None,
           hl=None, a_hl=0.0, diff_y0=None):
    """tabela de 2 linhas (x em cima, y embaixo). diffs = textos entre colunas (setas abaixo). hl = colunas destacadas."""
    if a <= 0:
        return
    n = len(xs)
    lw = 230
    W_ = lw + n * cw
    rrect(c, x0, y0, W_, rh * 2, 18, "#FFFFFF", a, shadow=True)
    rrect(c, x0, y0, lw, rh * 2, 18, mix("#FFFFFF", BLUE, 0.10), a)
    line(c, x0, y0 + rh, x0 + W_, y0 + rh, LIGHT, a, 3)
    ftext(c, rot_x, x0 + lw / 2, y0 + rh / 2 + 12, 30, "black", INK2, a)
    ftext(c, rot_y, x0 + lw / 2, y0 + rh * 1.5 + 12, 30, "black", INK2, a)
    for k in range(n):
        cx = x0 + lw + cw * (k + 0.5)
        if hl and k in hl and a_hl > 0:
            rrect(c, cx - cw / 2 + 6, y0 + 6, cw - 12, rh * 2 - 12, 14, AMBER, 0.18 * a * a_hl)
        line(c, cx - cw / 2, y0, cx - cw / 2, y0 + rh * 2, LIGHT, a, 2)
        ftext(c, xs[k], cx, y0 + rh / 2 + 14, 40, "black", INK, a)
        ftext(c, ys[k], cx, y0 + rh * 1.5 + 14, 40, "black", INK, a)
    if diffs and a_diff > 0:
        col = col_diff or PURPLE
        yd = diff_y0 if diff_y0 is not None else y0 + rh * 2 + 50
        for k, d in enumerate(diffs):
            if not d:
                continue
            ad = a * clamp(a_diff * len(diffs) - k)
            if ad <= 0:
                continue
            xa = x0 + lw + cw * (k + 0.5)
            xb = x0 + lw + cw * (k + 1.5)
            p = skia.Path()
            p.moveTo(xa, y0 + rh * 2 + 6); p.quadTo((xa + xb) / 2, yd + 10, xb, y0 + rh * 2 + 6)
            c.drawPath(p, paint(col, ad, stroke=4))
            ftext(c, d, (xa + xb) / 2, yd + 40, 32, "black", col, ad)
    return x0 + lw, cw


def tanque(c, x, y, w, h, a, nivel=1.0, marcas=True, rotulo=None):
    """tanque visto de frente; nivel 0..1"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 16, "#FFFFFF", a, shadow=True)
    hn = h * clamp(nivel)
    if hn > 2:
        rrect(c, x + 6, y + h - hn, w - 12, hn - 6, 10, AGUA, a * 0.75)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), paint(INK2, a, stroke=5))
    if marcas:
        for k in range(1, 5):
            yy = y + h * k / 5
            line(c, x + w - 34, yy, x + w - 6, yy, INK2, a, 3)
    if rotulo:
        ftext(c, rotulo, x + w / 2, y + h + 50, 32, "black", INK, a)


def carro(c, cx, cy, s, a, preco=None, col_preco=None):
    """carrinho simples de lado; s = escala (~1 → 260 px)"""
    if a <= 0:
        return
    w = 260 * s
    rrect(c, cx - w / 2, cy - 40 * s, w, 70 * s, 22 * s, "#4F7CAC", a, shadow=True)
    rrect(c, cx - w * 0.28, cy - 90 * s, w * 0.52, 60 * s, 20 * s, "#6C95C2", a)
    rrect(c, cx - w * 0.22, cy - 80 * s, w * 0.18, 40 * s, 8 * s, "#DDEBF7", a)
    rrect(c, cx + w * 0.01, cy - 80 * s, w * 0.18, 40 * s, 8 * s, "#DDEBF7", a)
    for dx in (-0.3, 0.3):
        c.drawCircle(cx + w * dx, cy + 34 * s, 30 * s, paint("#2B2F37", a))
        c.drawCircle(cx + w * dx, cy + 34 * s, 12 * s, paint("#C9CDD4", a))
    if preco:
        pill(c, preco, cx, cy - 140 * s, col_preco or INK, size=int(26 * s + 4), a=a, anchor="center")


def camera(c, cx, cy, s, a, col=None):
    """câmera fotográfica: a 'foto no instante zero'"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, cx - 90 * s, cy - 55 * s, 180 * s, 115 * s, 20 * s, col, a, shadow=True)
    rrect(c, cx - 40 * s, cy - 78 * s, 80 * s, 30 * s, 8 * s, col, a)
    c.drawCircle(cx, cy + 4 * s, 38 * s, paint("#FFFFFF", a))
    c.drawCircle(cx, cy + 4 * s, 26 * s, paint(mix(col, "#000000", 0.3), a))
    c.drawCircle(cx + 62 * s, cy - 32 * s, 8 * s, paint("#FFD166", a))


def rebobina(c, cx, cy, a, col=None, size=60):
    """símbolo ◄◄ desenhado (não depende da fonte)"""
    if a <= 0:
        return
    col = col or BLUE
    for k in range(2):
        x = cx - size * 0.1 + k * size * 0.55 - size * 0.45
        p = skia.Path()
        p.moveTo(x, cy); p.lineTo(x + size * 0.55, cy - size * 0.4); p.lineTo(x + size * 0.55, cy + size * 0.4); p.close()
        c.drawPath(p, paint(col, a))


def eixos(c, x0, y0, w, h, a, ox=None, oy=None):
    """eixos simples: origem (ox, oy)"""
    ox = x0 + 40 if ox is None else ox
    oy = y0 + h - 40 if oy is None else oy
    line(c, x0, oy, x0 + w, oy, INK2, a, 3)
    line(c, ox, y0, ox, y0 + h, INK2, a, 3)
    ftext(c, "x", x0 + w - 6, oy + 36, 26, "black", INK2, a)
    ftext(c, "y", ox - 26, y0 + 22, 26, "black", INK2, a)
    return ox, oy


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO AFIM · EPISÓDIO 2", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    vela(c, 420, 760, aa, 17, 22, "17 cm")
    cronometro(c, 720, 380, 80, aa, 10, "10 min depois de acesa")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        chip(c, "perde 0,2 cm por minuto", 720, 610, PURPLE, ab, 30)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 250, 660, 190, 24, mix("#FFFFFF", AMBER, 0.22), acc)
        text(c, "A CONTA APRESSADA", 1350, 305, 30, "black", AMBER, acc)
        linha(c, [("17 ÷ 0,2 = ", INK), ("85 min", AMBER)], 1350, 380, 56, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        strike(c, 1180, 380, 1560, 380, ep(t, C["01.d"], 0.4), RED, 1)
        selo(c, 1350, 520, ad, "CONTAVA DESDE QUE FOI ACESA", RED, -4, 30)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        rrect(c, 1020, 610, 660, 170, 24, mix("#FFFFFF", BLUE, 0.12), ae)
        rebobina(c, 1110, 695, ae, BLUE, 64)
        text(c, "VOLTAR O FILME", 1400, 680, 40, "black", BLUE, ae)
        text(c, "até o zero", 1400, 730, 30, "bold", INK2, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO AFIM · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de FUNÇÃO AFIM", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "A TAXA", "de dois dados quaisquer", PURPLE), ("02.b", "O VALOR INICIAL", "mesmo escondido", BLUE),
             ("02.c", "QUANDO ACABA?", "com uma conta", GREEN)]
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
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        y = 340 + d1
        rrect(c, 260, y - 90, 1400, 180, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "episódio 1", 300, y - 90, BLUE, size=22, a=a1)
        linha(c, [("f(x) = ", INK), ("a", PURPLE), ("x + ", INK), ("b", BLUE)], 700, y + 10, 60, a1)
        linha(c, [("a", PURPLE), (" = taxa   ·   ", INK2), ("b", BLUE), (" = valor inicial", INK2)], 1250, y + 10, 38, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        y = 600 + d2
        rrect(c, 260, y - 90, 1400, 180, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "série de Equações do 1º grau", 300, y - 90, BLUE, size=22, a=a2)
        linha(c, [("3x − 12 = 0", INK), ("  →  3x = 12  →  ", INK2), ("x = 4", GREEN)], 960, y + 10, 54, a2)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    xs = (450, 960, 1470)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, xs[0] - 230, 210, 460, 470, 24, "#FFFFFF", aa, shadow=True)
        nv = 1 - 0.5 * clamp((t - C["04.a"]) / 6)
        tanque(c, xs[0] - 110, 260, 220, 300, aa, nv)
        text(c, "TANQUE · 500 L", xs[0], 620, 32, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, xs[1] - 230, 210, 460, 470, 24, "#FFFFFF", ab, shadow=True)
        alt = 13 - 4 * clamp((t - C["04.b"]) / 6)
        vela(c, xs[1], 560, ab, alt, 18)
        text(c, "VELA ACESA", xs[1], 620, 32, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, xs[2] - 230, 210, 460, 470, 24, "#FFFFFF", acc, shadow=True)
        carro(c, xs[2], 470, 1.1, acc, "valor ↓ a cada ano", RED)
        text(c, "DEPRECIAÇÃO", xs[2], 620, 32, "black", INK, acc)
        text(c, "perda de valor com o tempo", xs[2], 660, 24, "bold", INK2, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "ALGO DIMINUI SEMPRE NO MESMO RITMO", W / 2, 760, ad, 38)


# ======================================================================
# bloco a — a taxa de variação
# ======================================================================

def b_delta(c, t, C, B):
    head(c, t, B["start"], "COMO MEDIR O RITMO?", "A TAXA DE VARIAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 210, 640, 330, 26, mix("#FFFFFF", BLUE, 0.10), aa)
        ftext(c, "Δ", 380, 420, 200, "black", BLUE, aa)
        text(c, "DELTA", 650, 300, 40, "black", BLUE, aa)
        text(c, "= VARIAÇÃO", 650, 360, 34, "black", INK, aa)
        text(c, "final − inicial", 650, 430, 30, "bold", INK2, ep(t, C["05.a"] + 2.6, 0.4))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        # escadinha: x +1 → y muda a
        x0, y0 = 1000, 470
        for k in range(3):
            ak = ab * ep(t, C["05.b"] + 0.4 + k * 0.6, 0.3)
            xa, ya = x0 + k * 190, y0 - k * 80
            line(c, xa, ya, xa + 190, ya, INK2, ak, 5)
            line(c, xa + 190, ya, xa + 190, ya - 80, PURPLE, ak, 6)
            ftext(c, "+1", xa + 95, ya + 40, 28, "black", INK2, ak)
            ftext(c, "a", xa + 220, ya - 30, 36, "black", PURPLE, ak)
        text(c, "x anda 1  →  y muda a", 1290, 540, 32, "black", INK, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        K.boxed(c, 220, 600, 1480, 150, BLUE, acc, 0.08)
        linha(c, [("a", PURPLE), (" = COEFICIENTE ANGULAR", BLUE)], 960, 650, 40, acc)
        text(c, "ou TAXA DE VARIAÇÃO: quanto a saída muda por unidade de entrada", 960, 715, 28, "bold", INK2, acc)


def b_formula(c, t, C, B):
    head(c, t, B["start"], "COM DOIS PONTOS", "A FÓRMULA DA TAXA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        K.boxed(c, 330, 210, 1260, 230, PURPLE, aa, 0.08)
        ftext(c, "a =", 560, 345, 80, "black", PURPLE, aa, align="right")
        K.fr(c, "Δy", "Δx", 680, 325, 76, INK, aa)
        ftext(c, "=", 820, 345, 70, "black", INK, aa)
        ab0 = ep(t, C["06.a"] + 2.4, 0.4)
        K.fr(c, "y₂ − y₁", "x₂ − x₁", 1130, 325, 62, INK, ab0)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 330, 480, 1260, 120, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("quanto a ", INK2), ("SAÍDA", PURPLE), (" andou  ÷  quanto a ", INK2), ("ENTRADA", BLUE),
                  (" andou", INK2)], 960, 540, 38, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        text(c, "UNIDADE: unidade de y POR unidade de x", 960, 670, 30, "black", INK, acc)
        for k, s_ in enumerate(("L/h", "cm/min", "R$/ano")):
            chip(c, s_, 660 + k * 300, 755, PURPLE, ep(t, C["06.c"] + 1.0 + k * 0.7, 0.3), 36)


# ======================================================================
# bloco b — a tabela do tanque
# ======================================================================

def b_tanque(c, t, C, B):
    head(c, t, B["start"], "O TANQUE", "DIFERENÇAS CONSTANTES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    ab = prog(t, C["07.b"], 2.2)
    tabela(c, 260, 220, ["0", "1", "2", "3", "4"], ["500", "440", "380", "320", "260"], aa, cw=200,
           rot_x="x (horas)", rot_y="y (litros)", diffs=["−60"] * 4, a_diff=ab)
    nv = 1 - 0.48 * clamp((t - C["07.a"]) / 8)
    tanque(c, 1550, 210, 150, 210, aa, nv, rotulo=None)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 520, 680, 160, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        linha(c, [("a = ", INK), ("−60 L/h", PURPLE)], 600, 580, 54, acc)
        text(c, "com MENOS: o tanque diminui", 600, 650, 26, "bold", INK2, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 520, 680, 160, 22, mix("#FFFFFF", BLUE, 0.10), ad)
        linha(c, [("b = ", INK), ("500 L", BLUE)], 1320, 570, 44, ad)
        linha(c, [("y = ", INK), ("500", BLUE), (" − ", INK), ("60", PURPLE), ("x", INK)], 1320, 640, 50,
              ep(t, C["07.d"] + 1.6, 0.4))


def b_irregular(c, t, C, B):
    head(c, t, B["start"], "E SE AS HORAS PULAREM?", "x ESPAÇADO IRREGULAR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    ab = ep(t, C["08.b"], 0.5)
    tabela(c, 330, 230, ["0", "1", "3"], ["500", "440", "320"], aa, cw=260, rot_x="x (horas)", rot_y="y (litros)",
           hl=[1, 2], a_hl=ab)
    if ab > 0:
        rrect(c, 1290, 230, 360, 80, 18, mix("#FFFFFF", PURPLE, 0.12), ab)
        linha(c, [("Δy = ", INK), ("−120 L", PURPLE)], 1470, 270, 36, ab)
        ab2 = ep(t, C["08.b"] + 1.8, 0.4)
        rrect(c, 1290, 330, 360, 80, 18, mix("#FFFFFF", BLUE, 0.12), ab2)
        linha(c, [("Δx = ", INK), ("2 h", BLUE)], 1470, 370, 36, ab2)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        K.boxed(c, 460, 520, 1000, 220, PURPLE, acc, 0.08)
        ftext(c, "a =", 700, 650, 64, "black", PURPLE, acc, align="right")
        K.fr(c, "−120 L", "2 h", 860, 630, 58, INK, acc)
        linha(c, [("= ", INK), ("−60 L/h", PURPLE)], 1170, 630, 60, ep(t, C["08.c"] + 1.6, 0.4))


# ======================================================================
# bloco c — a ordem
# ======================================================================

def b_ordem(c, t, C, B):
    head(c, t, B["start"], "A ORDEM IMPORTA?", "Δy SOBRE Δx · MESMOS PONTOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        regra(c, "Δy SOBRE Δx, NESSA ORDEM E COM OS MESMOS PONTOS", W / 2, 250, aa, 34)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 340, 760, 330, 24, mix("#FFFFFF", RED, 0.06), ab, shadow=True)
        K.fr(c, "380 − 500", "0 − 2", 560, 490, 56, INK, ab, num_col=INK, den_col=RED)
        linha(c, [("= ", INK), ("+60", RED)], 880, 490, 64, ep(t, C["09.b"] + 2.6, 0.4))
        text(c, "em cima: 2º − 1º   ·   embaixo: 1º − 2º", 680, 630, 26, "bold", RED, ep(t, C["09.b"] + 1.4, 0.4))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        tanque(c, 1250, 340, 200, 260, acc, 0.55 + 0.35 * clamp((t - C["09.c"]) / 1.5), marcas=True)
        selo(c, 1350, 680, acc, "O TANQUE ENCHERIA?", AMBER, -4, 30)
        if t > C["09.c"] + 2.2:
            selo(c, 1350, 770, ep(t, C["09.c"] + 2.2, 0.4), "O SINAL VIROU", RED, 3, 30)


def b_pontos(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "SEGUNDO MENOS PRIMEIRO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 130, "ATALHO", ["escreva os DOIS PONTOS antes de tudo"], aa, 40)
    if aa > 0:
        a1 = ep(t, C["10.a"] + 1.4, 0.4)
        linha(c, [("1º: ", INK2), ("(0, 500)", BLUE)], 560, 400, 44, a1)
        linha(c, [("2º: ", INK2), ("(2, 380)", PURPLE)], 1360, 400, 44, ep(t, C["10.a"] + 2.0, 0.4))
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        K.fr(c, "380 − 500", "2 − 0", 860, 560, 54, INK, ab, num_col=PURPLE, den_col=PURPLE)
        linha(c, [("= ", INK), ("−60", GREEN)], 1120, 560, 60, ep(t, C["10.b"] + 2.0, 0.4))
        text(c, "2º − 1º em cima E embaixo", 960, 690, 28, "bold", INK2, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        pill(c, "diminui → taxa NEGATIVA", W / 2, 775, GREEN, size=32, a=acc, anchor="center")


# ======================================================================
# bloco d — o coeficiente linear e voltar o filme
# ======================================================================

def b_linear(c, t, C, B):
    head(c, t, B["start"], "E O b?", "O COEFICIENTE LINEAR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 130, 24, "#FFFFFF", aa, shadow=True)
        linha(c, [("x = 0:   f(0) = ", INK), ("a", PURPLE), (" · 0 + ", INK), ("b", BLUE), ("  =  ", INK), ("b", BLUE)],
              960, 275, 56, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        K.boxed(c, 260, 380, 820, 220, BLUE, ab, 0.08)
        linha(c, [("b", BLUE), (" = COEFICIENTE LINEAR", BLUE)], 670, 440, 40, ab)
        text(c, "o valor da função no início", 670, 510, 30, "bold", INK2, ab)
        a2 = ep(t, C["11.b"] + 2.4, 0.4)
        ox, oy = eixos(c, 1180, 380, 460, 300, a2, ox=1260, oy=640)
        if a2 > 0:
            line(c, ox, 520, 1620, 420, PURPLE, a2, 5)
            c.drawCircle(ox, 520, 12, paint(BLUE, a2))
            ftext(c, "(0, b)", ox + 70, 560, 28, "black", BLUE, a2)
            pill(c, "ep. 3", 1600, 640, GRAY, size=22, a=a2, anchor="right", bounds=(0, 1920))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        camera(c, 520, 720, 0.8, acc)
        text(c, "o b é a FOTO NO INSTANTE ZERO", 1060, 735, 40, "black", BLUE, acc)


def b_filme(c, t, C, B):
    head(c, t, B["start"], "A TABELA NÃO COMEÇA NO ZERO?", "VOLTE O FILME", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 100, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        rebobina(c, 360, 260, aa, BLUE, 52)
        text(c, "começou aos 10 min? volte o filme ATÉ O ZERO", 1000, 272, 34, "black", BLUE, aa)
    ab = ep(t, C["12.b"], 0.5)
    tc = C["12.c"]
    rew = ep(t, tc + 0.4, 1.6) if t >= tc else 0.0
    alt = 14 + 2 * rew
    mins = 5 - 5 * rew
    if ab > 0:
        vela(c, 560, 760, ab, alt, 20)
        if rew > 0:
            vela(c, 560, 760, ab * 0.9, 14, 20, chama=False, fantasma=True)
        cronometro(c, 900, 470, 74, ab, mins, f"{mins:.0f} min".replace(".", ","))
        chip(c, "perde 0,4 cm/min", 900, 650, PURPLE, ab, 30)
        ftext(c, f"{alt:.0f} cm" if rew in (0, 1) else f"{alt:.1f} cm".replace(".", ","), 380, 560, 44, "black",
              BLUE if rew >= 1 else INK, ab, align="right")
    acc = ep(t, tc, 0.5)
    if acc > 0:
        rrect(c, 1120, 380, 520, 140, 22, "#FFFFFF", acc, shadow=True)
        rebobina(c, 1200, 450, acc, BLUE, 44)
        linha(c, [("5 min: ", INK), ("+ 2 cm", BLUE)], 1420, 450, 40, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        linha(c, [("14 + 2 = ", INK), ("16 cm", BLUE)], 1380, 600, 56, ad)
        selo(c, 1380, 720, ad, "ESTE É O b", GREEN, -4, 36)


def b_voltar(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "VOLTAR O FILME EM 1 LINHA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 170, "ATALHO", ["b = valor medido + o que se perdeu até ali"], aa, 42)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 420, 1400, 150, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("perdeu: ", INK2), ("0,4", PURPLE), (" cm/min · ", INK2), ("5", INK), (" min = ", INK2), ("2 cm", PURPLE)],
              960, 470, 40, ab)
        linha(c, [("b = 14 + 2 = ", INK), ("16 cm", BLUE)], 960, 530, 40, ep(t, C["13.b"] + 2.0, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        pill(c, "se CRESCESSE: tire o que ganhou", W / 2, 680, AMBER, size=32, a=acc, anchor="center")


# ======================================================================
# blocos e e f — o zero
# ======================================================================

def b_zero(c, t, C, B):
    head(c, t, B["start"], "QUANDO O y CHEGA A ZERO?", "O ZERO DA FUNÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        K.boxed(c, 260, 210, 1400, 130, BLUE, aa, 0.08)
        text(c, "ZERO ou RAIZ: o x que faz a função dar ZERO", 960, 290, 38, "black", BLUE, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 380, 820, 300, 24, "#FFFFFF", ab, shadow=True)
        linha(c, [("a", PURPLE), ("x + ", INK), ("b", BLUE), (" = 0", INK)], 670, 450, 54, ab)
        linha(c, [("a", PURPLE), ("x = −", INK), ("b", BLUE)], 670, 530, 46, ep(t, C["14.b"] + 1.6, 0.4))
        a3 = ep(t, C["14.b"] + 3.0, 0.4)
        if a3 > 0:
            ftext(c, "x =", 600, 640, 50, "black", INK, a3, align="right")
            K.fr(c, "−b", "a", 680, 620, 50, INK, a3, num_col=BLUE, den_col=PURPLE)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 1120, 380, 540, 300, 24, mix("#FFFFFF", GREEN, 0.10), acc, shadow=True)
        linha(c, [("2x − 6 = 0", INK)], 1390, 450, 46, acc)
        linha(c, [("2x = 6", INK2)], 1390, 530, 40, ep(t, C["14.c"] + 1.0, 0.4))
        linha(c, [("x = 3", GREEN)], 1390, 615, 56, ep(t, C["14.c"] + 1.8, 0.4))


def b_seca(c, t, C, B):
    head(c, t, B["start"], "QUANDO O TANQUE SECA?", "y = 500 − 60x", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    nv = 1 - clamp((t - C["15.a"]) / 7)
    tanque(c, 300, 230, 260, 420, aa, nv, rotulo=f"{max(0, 500 * nv):.0f} L")
    if aa > 0:
        linha(c, [("500", BLUE), (" − ", INK), ("60", PURPLE), ("x = 0", INK)], 1150, 280, 56, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        ftext(c, "x =", 960, 420, 52, "black", INK, ab, align="right")
        K.fr(c, "500", "60", 1050, 400, 52, INK, ab)
        linha(c, [("≈ ", INK), ("8,3 h", PURPLE)], 1260, 400, 56, ep(t, C["15.b"] + 1.4, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 760, 560, 380, 120, 22, mix("#FFFFFF", RED, 0.08), acc)
        text_mid(c, "8 h 30 min", 950, 620, 44, "black", RED, acc)
        strike(c, 790, 620, 1110, 620, ep(t, C["15.c"] + 0.8, 0.4), RED, 1)
        a2 = ep(t, C["15.c"] + 1.8, 0.4)
        rrect(c, 1180, 560, 440, 120, 22, mix("#FFFFFF", GREEN, 0.14), a2)
        text_mid(c, "8 h 20 min", 1400, 620, 48, "black", GREEN, a2)


def b_horas(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DECIMAL DE HORA → MINUTOS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO", ["depois da vírgula é FRAÇÃO DE HORA: × 60"], aa, 40)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        cx, cy, r = 560, 590, 150
        c.drawCircle(cx, cy, r, paint("#FFFFFF", ab))
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 120 * ep(t, C["16.b"], 1.2), False); p.close()
        c.drawPath(p, paint(GREEN, ab * 0.5))
        c.drawCircle(cx, cy, r, paint(INK, ab, stroke=5))
        text(c, "1/3 de hora", cx, cy + r + 50, 30, "black", GREEN, ab)
        linha(c, [("0,3 h ≈ 1/3 h", INK)], 1200, 470, 48, ab)
        linha(c, [("1/3 · 60 = ", INK), ("20 min", GREEN)], 1200, 570, 56, ep(t, C["16.b"] + 1.6, 0.4))
        pill(c, "a hora tem 60 min, não 100", 1200, 690, AMBER, size=30, a=ep(t, C["16.b"] + 3.2, 0.4), anchor="center")


def b_nome(c, t, C, B):
    head(c, t, B["start"], "NA PROVA", "O ZERO TEM NOME", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    for k, s_ in enumerate(("a vela ACABA", "o tanque SECA", "a dívida ZERA")):
        chip(c, s_, 470 + k * 490, 260, BLUE, aa * ep(t, C["17.a"] + 0.5 + k * 0.7, 0.3), 34)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        regra(c, "“QUANDO ACABA?” → ZERO DA FUNÇÃO", W / 2, 380, ab, 38)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 460, 900, 200, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("16", BLUE), (" − ", INK), ("0,4", PURPLE), ("t = 0", INK)], 710, 520, 46, acc)
        linha(c, [("t = 16 ÷ 0,4 = ", INK), ("40 min", GREEN)], 710, 600, 46, ep(t, C["17.c"] + 1.6, 0.4))
        alt = 16 * (1 - clamp((t - C["17.c"] - 1.6) / 2.5))
        vela(c, 1400, 650, acc, alt, 11, chama=alt > 0.2)
        if alt <= 0.2:
            selo(c, 1400, 560, ep(t, C["17.c"] + 4.1, 0.4), "ACABOU · 40 min", GREEN, -4, 30)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        K.boxed(c, 260, 700, 1400, 100, BLUE, ad, 0.08)
        text(c, "EXTRAPOLAR: usar a lei além dos dados, supondo que o ritmo continua", 960, 762, 28, "black", BLUE, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "O x PULA DE 2 EM 2", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    resol = t >= C["19"]
    ad = ep(t, C["19.a"], 0.5) if resol else 0
    tabela(c, 420, 210, ["0", "2", "4", "6"], ["30", "26", "22", "18"], aa, cw=200, diffs=["−4"] * 3, a_diff=ad,
           diff_y0=None)
    if resol and ad > 0:
        for k in range(3):
            ak = ad * clamp(ad * 3 - k)
            xa = 850 + k * 200
            ftext(c, "+2", xa, 196, 26, "black", BLUE, ak)
    ab = ep(t, C["18.b"], 0.5)
    if not resol:
        if ab > 0:
            for k, s_ in enumerate(("TAXA = ?", "b = ?", "ZERO = ?")):
                chip(c, s_, 560 + k * 400, 560, AMBER, ab * ep(t, C["18.b"] + k * 0.6, 0.3), 40)
        pause_timer(c, t, C["18.end"] - 1.9, 960, 730)
        return
    if ad > 0:
        ftext(c, "a =", 430, 600, 46, "black", PURPLE, ad, align="right")
        K.fr(c, "−4", "2", 500, 580, 46, INK, ad, den_col=BLUE)
        linha(c, [("= ", INK), ("−2", PURPLE)], 620, 580, 50, ep(t, C["19.a"] + 2.4, 0.4))
    a_b = ep(t, C["19.b"], 0.5)
    if a_b > 0:
        linha(c, [("b = ", INK), ("30", BLUE)], 960, 580, 50, a_b)
        camera(c, 960, 690, 0.55, a_b)
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("30 − 2x = 0", INK)], 1420, 540, 42, acc)
        linha(c, [("x = ", INK), ("15", GREEN)], 1420, 620, 54, ep(t, C["19.c"] + 1.4, 0.4))
    a_d = ep(t, C["19.d"], 0.5)
    if a_d > 0:
        pill(c, "taxa −4 (esqueceu o pulo do x)  →  7,5", 1420, 740, RED, size=24, a=a_d, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa é Δy sobre Δx, com unidade e com sinal.",
          "b é o valor no instante zero, não o primeiro dado da tabela.",
          "“Quando acaba?” pede o zero: ax + b = 0."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Fração invertida: Δx/Δy = 2 ÷ (−120) ≈ −0,017", "as duas dividem as diferenças",
          "taxa = SAÍDA sobre ENTRADA: −120 ÷ 2 = −60 L/h"),
         ("O primeiro dado da tabela como b: 14 cm aos 5 min", "é o primeiro número que aparece",
          "b é a foto do ZERO: volte o filme → 16 cm"),
         ("Confundir o zero com o b", "os dois têm “zero” na história",
          "b = y quando x = 0 (500 L) · zero = x que zera o y (8 h 20 min)"),
         ("Taxa com “+” no que diminui: y = 500 + 60x", "o texto diz “perde 60” e anotamos só o número",
          "em 2 h teria 620 L! O certo: y = 500 − 60x"),
         ("Esquecer o tempo que já passou: 14 ÷ 0,4 = 35 min", "a conta acha quanto FALTA",
          "desde que foi acesa: 16 ÷ 0,4 = 40 min")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24", "25"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _fonte(c, t, C, a0, prox):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[prox], 0.3)),
         align="left")


ALTS3 = [("A", "1,25 h do início do vazamento.", "proporção 400/1 600", RED),
         ("B", "4 h do início do vazamento.", "1 600 ÷ 400: L com h", RED),
         ("C", "15 h do início do vazamento.", "contou da 5ª hora", RED),
         ("D", "20 h do início do vazamento.", "", GREEN),
         ("E", "25 h do início do vazamento.", "tempo para ESVAZIAR", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "RESERVATÓRIO COM VAZAMENTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    yend = _enunciado(c, [("Um reservatório tinha 2 000 litros de água quando começou um vazamento de vazão constante. "
                           "Cinco horas depois, restavam 1 600 litros. Se nada for feito, o reservatório terá 400 litros "
                           "após", INK)], a0, 236, 28)
    _fonte(c, t, C, a0, "27")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 34, C["27.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["27"]:
        pause_timer(c, t, C["26.end"] - 1.9, 540, yend + 120)
        return
    y0 = 206
    _painel(c, y0, ep(t, C["27"], 0.4))
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        linha(c, [("(0, ", INK), ("2 000", BLUE), (")   (5, 1 600)", INK)], 540, y0 + 60, 34, aa)
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        ftext(c, "a =", 330, y0 + 175, 38, "black", PURPLE, ab, align="right")
        K.fr(c, "1 600 − 2 000", "5 − 0", 500, y0 + 160, 34, INK, ab)
        linha(c, [("= ", INK), ("−80 L/h", PURPLE)], 760, y0 + 160, 36, ep(t, C["27.b"] + 1.8, 0.4))
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        linha(c, [("2 000", BLUE), (" − ", INK), ("80", PURPLE), ("t = 400", INK)], 540, y0 + 290, 38, acc)
        linha(c, [("80t = 1 600  →  ", INK), ("t = 20 h", GREEN)], 540, y0 + 360, 38, ep(t, C["27.c"] + 2.0, 0.4))
    ad = ep(t, C["27.d"], 0.4)
    if ad > 0:
        check_icon(c, 250, y0 + 450, 20, ad, GREEN)
        linha(c, [("t = 5: 2 000 − 400 = 1 600 · bate", GREEN)], 290, y0 + 452, 26, ad, align="left")
        tanque(c, 680, y0 + 490, 160, 110, ad, 0.2, marcas=False)
        ftext(c, "400 L", 760, y0 + 470, 26, "black", INK, ad)


ALTS8 = [("A", "R$ 6.000,00.", "a perda POR ANO", RED), ("B", "R$ 12.000,00.", "5 anos em vez de 4", RED),
         ("C", "R$ 18.000,00.", "", GREEN), ("D", "R$ 24.000,00.", "60 000 − 2 · 18 000", RED),
         ("E", "cerca de R$ 26.000,00.", "queda em % (exponencial)", AMBER)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · NÓS FAZEMOS", "DEPRECIAÇÃO LINEAR", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    yend = _enunciado(c, [("Um carro comprado por R$ 60.000,00 passou a valer R$ 42.000,00 três anos depois. Suponha que o "
                           "valor do carro diminua linearmente com o tempo. Sete anos após a compra, ele valerá", INK)],
                      a0, 236, 28)
    _fonte(c, t, C, a0, "30")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 260, 680, 36, C["30.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["30"]:
        pause_timer(c, t, C["29.end"] - 1.9, 540, yend + 120)
        carro(c, 540, yend + 330, 0.8, a0, "R$ 60.000 → R$ 42.000", INK)
        return
    y0 = 206
    _painel(c, y0, ep(t, C["30"], 0.4))
    a_t = ep(t, C["30"], 0.4)
    if a_t > 0:
        linha(c, [("(0, ", INK), ("60 000", BLUE), (")   (3, 42 000)", INK)], 540, y0 + 60, 32, a_t)
    aa = ep(t, C["30.a"], 0.4)
    if aa > 0:
        ftext(c, "a =", 330, y0 + 175, 38, "black", PURPLE, aa, align="right")
        K.fr(c, "−18 000", "3", 460, y0 + 160, 36, INK, aa)
        linha(c, [("= ", INK), ("−6 000 R$/ano", PURPLE)], 720, y0 + 160, 32, ep(t, C["30.a"] + 1.8, 0.4))
    ab = ep(t, C["30.b"], 0.4)
    if ab > 0:
        linha(c, [("V(7) = ", INK), ("60 000", BLUE), (" − ", INK), ("6 000", PURPLE), (" · 7", INK)], 540, y0 + 290, 34, ab)
        linha(c, [("= 60 000 − 42 000 = ", INK), ("18 000", GREEN)], 540, y0 + 360, 34, ep(t, C["30.b"] + 2.0, 0.4))
    acc = ep(t, C["30.c"], 0.4)
    if acc > 0:
        check_icon(c, 250, y0 + 450, 20, acc, GREEN)
        linha(c, [("V(3) = 60 000 − 18 000 = 42 000 · bate", GREEN)], 290, y0 + 452, 26, acc, align="left")


ALTS1 = [("A", "47,5 min.", "19 ÷ 0,4: taxa errada", RED), ("B", "65 min.", "13 ÷ 0,2: falta após 30 min", RED),
         ("C", "85 min.", "17 ÷ 0,2: falta após 10 min", RED), ("D", "95 min.", "", GREEN),
         ("E", "105 min.", "começou em 21 cm", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · VOCÊ FAZ", "A VELA QUE DERRETE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    yend = _enunciado(c, [("Uma vela foi acesa e passou a diminuir de altura a uma taxa constante. Dez minutos depois de "
                           "acesa, ela media 17 cm; trinta minutos depois de acesa, media 13 cm. Mantido esse ritmo, o "
                           "tempo total, contado a partir do momento em que foi acesa, até a vela se consumir por "
                           "completo é de", INK)], a0, 236, 26)
    _fonte(c, t, C, a0, "33")
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1000, 260, 680, 38, C["33.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["33"]:
        pause_timer(c, t, C["32.end"] - 1.9, 540, yend + 110)
        return
    y0 = 206
    _painel(c, y0, ep(t, C["33"], 0.4))
    # a vela: 17 aos 10 → 13 aos 30 → rebobina a 19 (t = 0) → some em 95
    ta, tb, tc, td = C["33.a"], C["33.b"], C["33.c"], C["33.d"]
    if t < tb:
        u = ep(t, ta + 0.8, 1.6)
        alt, mins = 17 - 4 * u, 10 + 20 * u
    elif t < tc:
        u = ep(t, tb + 0.3, 1.6)
        alt, mins = 13 + 6 * u, 30 - 30 * u
    else:
        u = ep(t, tc + 1.2, 3.0)
        alt, mins = 19 - 19 * u, 95 * u
    xv = 770
    vela(c, xv, 780, ep(t, C["33"], 0.4), alt, 14, chama=alt > 0.3)
    cronometro(c, xv, 270, 52, ep(t, C["33"], 0.4), mins, f"{mins:.0f} min")
    ftext(c, f"{alt:.0f} cm", xv, 780 - alt * 14 - 92, 30, "black", BLUE if (tb <= t < tc and u >= 1) else INK,
          ep(t, C["33"], 0.4) * (1 if alt > 0.3 else 0))
    aa = ep(t, ta, 0.4)
    if aa > 0:
        linha(c, [("(10, 17)  (30, 13)", INK)], 410, y0 + 60, 30, aa)
        ftext(c, "a =", 280, y0 + 165, 34, "black", PURPLE, aa, align="right")
        K.fr(c, "13 − 17", "30 − 10", 380, y0 + 150, 30, INK, aa)
        linha(c, [("= −0,2", PURPLE)], 540, y0 + 150, 32, ep(t, ta + 2.0, 0.4))
        text(c, "cm/min", 540, y0 + 200, 22, "black", PURPLE, ep(t, ta + 2.0, 0.4))
    ab = ep(t, tb, 0.4)
    if ab > 0:
        rebobina(c, 230, y0 + 280, ab, BLUE, 34)
        linha(c, [("b = 17 + 0,2 · 10 = ", INK), ("19", BLUE)], 270, y0 + 280, 28, ab, align="left")
        selo(c, 410, y0 + 345, ep(t, tb + 2.6, 0.4), "ESTE É O b", GREEN, -4, 24)
    acc = ep(t, tc, 0.4)
    if acc > 0:
        linha(c, [("19", BLUE), (" − ", INK), ("0,2", PURPLE), ("t = 0", INK)], 410, y0 + 440, 34, acc)
        linha(c, [("t = ", INK), ("95 min", GREEN)], 410, y0 + 510, 42, ep(t, tc + 1.6, 0.4))
    ad = ep(t, td, 0.4)
    if ad > 0:
        check_icon(c, 220, y0 + 590, 18, ad, GREEN)
        linha(c, [("t = 30: 19 − 6 = 13 · bate", GREEN)], 250, y0 + 592, 24, ad, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O GRÁFICO", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    if aa > 0:
        ox, oy = eixos(c, 300, 230, 620, 520, aa, ox=500, oy=520)
        u = 70
        c.drawCircle(ox, oy + 3 * u, 14, paint(BLUE, aa))
        ftext(c, "(0, −3)", ox - 30, oy + 3 * u + 10, 30, "black", BLUE, aa, align="right")
        a2 = ep(t, C["36.a"] + 1.6, 0.4)
        c.drawCircle(ox + 2 * u, oy - u, 14, paint(PURPLE, a2))
        ftext(c, "(2, 1)", ox + 2 * u + 30, oy - u - 20, 30, "black", PURPLE, a2, align="left")
        linha(c, [("lei = ", INK), ("?", AMBER)], 1340, 330, 70, ep(t, C["36.a"] + 2.6, 0.4))
    ab = ep(t, C["36.b"], 0.5)
    if ab > 0:
        rrect(c, 1080, 430, 520, 170, 24, mix("#FFFFFF", AMBER, 0.25), ab)
        text(c, "só de olhar:", 1340, 495, 30, "bold", INK2, ab)
        text(c, "SOBE ou DESCE?", 1340, 560, 44, "black", AMBER, ab)
    pill(c, "ep. 3 · o gráfico e a lei por dois pontos", 1340, 700, PURPLE, size=26, a=ep(t, C["36.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"],
        "O que na sua casa tem uma “hora em que acaba”?", canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, delta=b_delta, formula=b_formula,
              tanque=b_tanque, irregular=b_irregular, ordem=b_ordem, pontos=b_pontos, linear=b_linear, filme=b_filme,
              voltar=b_voltar, zero=b_zero, seca=b_seca, horas=b_horas, nome=b_nome, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, q8=b_q8, q1=b_q1, ponte=b_ponte, cta=b_cta)
