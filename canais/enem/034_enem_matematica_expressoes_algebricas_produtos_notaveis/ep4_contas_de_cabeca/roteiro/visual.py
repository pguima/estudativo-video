"""Visual — Expressões Algébricas e Produtos Notáveis, Episódio 4: contas de cabeça com produtos notáveis (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo...).
Peças deste episódio: alarme() (o alarme verde "ATALHO!" que acende quando aparece conta grande demais), reta_gemeos()
(reta numérica com o REDONDO no centro e os dois GÊMEOS saltando o mesmo número de passos para cada lado), coluna()
(conta empilhada com os zeros alinhados à direita), deposito() (as caixas de parafusos), barras_preco() (100 → 130 → 91),
linha() (texto numa linha com cor por trecho), m() (expr de uma cor).
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
_s = importlib.util.spec_from_file_location("comum034", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                 K.selo, K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_algebra_ep4_contas_de_cabeca.mp4"
CARD_R = K.CARD_R
BOX = "#C98A4B"     # caixas de papelão


def m(c, s, cx, cy, size, a=1.0, hl=None, align="center", col=None):
    """linha matemática (expr) de uma cor, com destaques por token: hl = {índice: cor}"""
    n = len(s.split())
    cores = {i: col or INK for i in range(n)}
    cores.update(hl or {})
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha (aceita ² e −), com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    tot = sum(ws)
    x = cx - tot / 2 if align == "center" else (cx - tot if align == "right" else cx)
    for (s_, col), w_ in zip(partes, ws):
        fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_
    return tot


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def defin(c, termo, s, y, a, w=1400):
    """faixa azul de definição: TERMO + frase"""
    if a <= 0:
        return
    x = W / 2 - w / 2
    boxed(c, x, y - 50, w, 100, BLUE, a, 0.08)
    pill(c, termo, x + 24, y, BLUE, size=26, a=a)
    tw = text_w(termo, "bold", 26) + 70
    para(c, s, x + 24 + tw, y + 12, 32, "bold", INK, a, w - tw - 60)


# ======================================================================
# peças do episódio
# ======================================================================

def alarme(c, cx, cy, a, t=0.0, size=34):
    """alarme verde "ATALHO!": luz giratória + faixa; pulsa com t"""
    if a <= 0:
        return
    pulse = 0.5 + 0.5 * math.sin(t * 7.0)
    h = size * 1.9
    w = text_w("ATALHO!", "black", size) + h * 1.5
    c.drawCircle(cx - w / 2 + h * 0.5, cy, h * 0.62 + 10 * pulse, paint(GREEN, a * 0.18))
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, GREEN, a, shadow=True)
    # a luz
    lx = cx - w / 2 + h * 0.5
    c.drawCircle(lx, cy, h * 0.32, paint("#FFFFFF", a))
    c.drawCircle(lx, cy, h * 0.2, paint(mix(GREEN, "#FFFFFF", 0.35 + 0.4 * pulse), a))
    for k in range(3):
        ang = math.radians(-50 + k * 50)
        r0, r1 = h * 0.42, h * 0.58
        line(c, lx + r0 * math.sin(ang) * 0.9, cy - h * 0.45 - 2, lx + r1 * math.sin(ang) * 1.3, cy - h * 0.62 - 6 * pulse,
             GREEN, a * (0.5 + 0.5 * pulse), 4)
    text_mid(c, "ATALHO!", cx + h * 0.38, cy, size, "black", "#FFFFFF", a)


def coluna(c, xr, y0, rows, size, alfas, lh=None, barra_antes=None, peso="black"):
    """conta empilhada, alinhada à direita (os zeros ficam um embaixo do outro). rows = [(texto, cor)];
    alfas = lista de opacidades por linha; barra_antes = índice da linha que ganha o traço de soma acima dela."""
    lh = lh or size * 1.35
    wmax = max(ftext_w(s_, peso, size) for s_, _ in rows)
    for k, ((s_, col), a) in enumerate(zip(rows, alfas)):
        if a <= 0:
            continue
        y = y0 + k * lh
        if barra_antes == k:
            line(c, xr - wmax - 20, y - lh * 0.55, xr + 10, y - lh * 0.55, INK2, a, 4)
        fmid(c, s_, xr, y, size, peso, col or INK, a, align="right")


def reta_gemeos(c, x0, x1, y, centro, passo, a, u=1.0, escala=None, rot=("", "", ""), size=44, col=GREEN, salto=True):
    """reta numérica: o REDONDO no meio (roxo) e os dois GÊMEOS (verde) a `passo` unidades para cada lado.
    u = 0..1 anima os saltos (os gêmeos saem do centro e vão até a posição); escala = quantas unidades cabem em cada
    metade da reta (padrão 2,5 × passo)."""
    if a <= 0:
        return
    escala = escala or passo * 2.5
    cx = (x0 + x1) / 2
    half = (x1 - x0) / 2
    X = lambda v: cx + half * (v - centro) / escala
    line(c, x0, y, x1, y, INK2, a, 5)
    for k in range(-int(escala), int(escala) + 1):
        if escala > 12 and k % max(1, int(escala // 6)):
            continue
        line(c, X(centro + k), y - 12, X(centro + k), y + 12, INK2, a * 0.6, 3)
    c.drawCircle(X(centro), y, 18, paint(PURPLE, a))
    ftext(c, rot[1] or f"{centro}", X(centro), y + 70, size, "black", PURPLE, a)
    uu = ease_io(clamp(u))
    for sgn, lab in ((-1, rot[0]), (1, rot[2])):
        xx = X(centro + sgn * passo * uu)
        if salto and uu > 0:
            # arco do salto
            p = skia.Path()
            n = 24
            for j in range(n + 1):
                f = j / n * uu
                px = X(centro + sgn * passo * f)
                py = y - 90 * math.sin(math.pi * f / max(uu, 1e-3)) * min(1.0, uu * 1.5)
                (p.moveTo if j == 0 else p.lineTo)(px, py)
            c.drawPath(p, paint(col, a * 0.7, stroke=4))
        c.drawCircle(xx, y, 15, paint(col, a))
        if uu > 0.95:
            ftext(c, lab, xx, y + 70, size, "black", col, a)
            ftext(c, f"{'−' if sgn < 0 else '+'}{passo}", (X(centro) + xx) / 2, y - 105, size * 0.8, "black", col, a)


def deposito(c, x, y, a, cols=9, rows=4, s=1.0, rot=True):
    """as caixas de parafusos empilhadas (grade), cada uma com '997'"""
    if a <= 0:
        return
    bw, bh, g = 92 * s, 70 * s, 10 * s
    for r_ in range(rows):
        for k in range(cols):
            xx = x + k * (bw + g)
            yy = y + r_ * (bh + g)
            rrect(c, xx, yy, bw, bh, 8, BOX, a)
            line(c, xx + bw / 2, yy, xx + bw / 2, yy + bh * 0.28, mix(BOX, "#000000", 0.25), a, 3)
            text_mid(c, "997", xx + bw / 2, yy + bh * 0.62, 24 * s, "black", "#FFFFFF", a)
    if rot:
        text(c, "1 003 caixas · 997 parafusos em cada", x + cols * (bw + g) / 2, y + rows * (bh + g) + 50, 32, "black",
             INK2, a)


def barras_preco(c, x, ybase, a, u=1.0):
    """três barras: R$ 100 → (+30%) R$ 130 → (−30%) R$ 91; u anima a sequência"""
    if a <= 0:
        return
    vals = [(100, "R$ 100", INK2), (130, "R$ 130", GREEN), (91, "R$ 91", RED)]
    sc = 2.6
    for k, (v, lab, col) in enumerate(vals):
        ak = a * ep(u * 3, k, 0.6)
        if ak <= 0:
            continue
        bx = x + k * 260
        h = v * sc
        rrect(c, bx, ybase - h, 170, h, 14, mix("#FFFFFF", col, 0.25), ak)
        text(c, lab, bx + 85, ybase - h - 20, 38, "black", col, ak)
        if k:
            arrow(c, bx - 80, ybase - 330, bx - 10, ybase - 330, INK2, ak, 4, 16)
            text(c, "+30%" if k == 1 else "−30%", bx - 45, ybase - 355, 28, "black", GREEN if k == 1 else RED, ak)
    line(c, x - 20, ybase, x + 2 * 260 + 190, ybase, INK2, a, 4)
    # linha tracejada do original
    if u > 0.9:
        hline(c, x - 20, x + 2 * 260 + 190, ybase - 100 * sc, GRAY, a, 3, dash=(14, 10))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "CONTAS DE CABEÇA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        fmid(c, "87² − 13² = ?", W / 2, 290, 96, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 390, 680, 380, GRAY, ab, 0.06)
        text(c, "CONTA DIRETA", 560, 440, 28, "black", GRAY, ab)
        coluna(c, 760, 530, [("7 569", INK2), ("− 169", INK2), ("7 400", INK2)], 58,
               [ab, ep(t, C["01.b"] + 1.4, 0.4), ep(t, C["01.c"] - 0.6, 0.4)], barra_antes=2)
        text(c, "dois quadrados e uma subtração", 560, 740, 26, "bold", GRAY, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        boxed(c, 1020, 390, 680, 380, GREEN, acc, 0.08)
        text(c, "PRODUTO NOTÁVEL", 1360, 440, 28, "black", GREEN, acc)
        fmid(c, "(87 + 13)(87 − 13)", 1360, 530, 48, "black", INK, acc)
        fmid(c, "100 · 74", 1360, 610, 58, "black", INK, ep(t, C["01.c"] + 2.0, 0.4))
        fmid(c, "= 7 400", 1360, 690, 64, "black", GREEN, ep(t, C["01.c"] + 3.6, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1360, 800, ad, "3 SEGUNDOS", GREEN, -4, 30)
        alarme(c, 1500, 290, ad, t)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    a, d = rise(t, C["02.a"])
    if a > 0:
        rrect(c, 260, 360 + d, 1400, 180, 24, mix("#FFFFFF", GREEN, 0.08), a, shadow=True)
        check_icon(c, 340, 450 + d, 30, a, GREEN)
        text_mid(c, "reconhecer NA HORA quando uma conta grande tem atalho", 400, 450 + d, 42, "black", INK, a,
                 align="left")
    alarme(c, W / 2, 680, ep(t, C["02.a"] + 2.5, 0.5), t, 40)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "3 LEMBRETES", "RÁPIDOS", GREEN)
    cards_ = [("03.a", "EPISÓDIO 2", ["(a+b)^2 = a^2 + 2ab + b^2", "(a-b)^2 = a^2 - 2ab + b^2"], "termo do meio: 2ab"),
              ("03.b", "EPISÓDIO 2", ["(a+b)(a-b) = a^2 - b^2"], "sem termo do meio"),
              ("03.c", "PORCENTAGEM", ["aumento: × (1 + p)", "desconto: × (1 − p)"], "fatores")]
    for k, (cue, tag, linhas, sub) in enumerate(cards_):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 530
        rrect(c, x, 260 + d, 500, 470, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, x + 250, 310 + d, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
        for j, s_ in enumerate(linhas):
            yy = 450 + d + j * 110 - (len(linhas) - 1) * 40
            if k < 2:
                m(c, s_, x + 250, yy, 34, a, col=PURPLE)
            else:
                fmid(c, s_, x + 250, yy, 40, "black", PURPLE, a)
        text(c, sub, x + 250, 680 + d, 28, "bold", GRAY, a)


# ======================================================================
# concreto e definições
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM DEPÓSITO", "CONTA DE PROVA?", BLUE)
    card(c, *CARD_R)
    deposito(c, 240, 260, ep(t, C["04.a"], 0.6))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        fmid(c, "1 003 × 997 = ?", 1450, 330, 64, "black", INK, ab)
        text(c, "sem calculadora?", 1450, 410, 34, "bold", GRAY, ab)
    alarme(c, 1450, 540, ep(t, C["04.c"], 0.5), t, 40)
    if t > C["04.c"]:
        text(c, "5 segundos", 1450, 640, 36, "black", GREEN, ep(t, C["04.c"], 0.5))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pill(c, "volta no fim · VOCÊ FAZ", 1450, 760, AMBER, size=30, a=ad, anchor="center", bounds=(0, 1920))


def b_defs(c, t, C, B):
    frame(c, t, B["start"], "DUAS PALAVRAS", "E UM ALARME", BLUE)
    defin(c, "NÚMERO REDONDO", "termina em zeros: 50 · 100 · 1 000", 300, ep(t, C["05.a"], 0.5))
    ab = ep(t, C["05.b"], 0.5)
    defin(c, "DISTÂNCIA ATÉ O REDONDO", "quantos passos faltam ou sobram", 440, ab)
    if ab > 0:
        reta_gemeos(c, 560, 1360, 620, 100, 2, ab, u=ep(t, C["05.b"] + 1.2, 1.0), escala=4, rot=("98", "100", "102"),
                    size=34, col=BLUE)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        alarme(c, 1560, 640, acc, t, 30)
        text(c, "conta grande demais", 1560, 740, 26, "black", GREEN, acc)
        text(c, "= produto notável escondido", 1560, 780, 26, "bold", INK2, acc)


# ======================================================================
# bloco a — quadrado perto do redondo
# ======================================================================

def b_quadrado(c, t, C, B):
    head_seq(c, t, C, [("06", "PERTO DO REDONDO", "101²", PURPLE),
                       ("07", "PERTO DO REDONDO", "998²", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "06":
        fmid(c, "101²", 470, 300, 110, "black", INK, ep(t, C["06.t"], 0.5))
        aa = ep(t, q("a"), 0.5)
        if aa > 0:
            fmid(c, "= (100 + 1)²", 470, 430, 60, "black", PURPLE, aa)
            text(c, "quadrado da soma", 470, 510, 30, "bold", GRAY, aa)
        rows = [("10 000", INK), ("+ 200", AMBER), ("+ 1", INK), ("10 201", GREEN)]
        coluna(c, 1500, 300, rows, 70, [ep(t, q("b"), 0.4), ep(t, q("c"), 0.4), ep(t, q("d"), 0.4), ep(t, q("e"), 0.4)],
               lh=110, barra_antes=3)
        for cue, s_, yy in (("b", "100²", 300), ("c", "2 · 100 · 1", 410), ("d", "1²", 520)):
            text(c, s_, 1000, yy + 12, 34, "bold", GRAY, ep(t, q(cue), 0.4), align="left")
        return
    fmid(c, "998²", 470, 300, 110, "black", INK, ep(t, C["07.t"], 0.5))
    aa = ep(t, q("a"), 0.5)
    if aa > 0:
        fmid(c, "= (1 000 − 2)²", 470, 430, 56, "black", PURPLE, aa)
        text(c, "quadrado da diferença", 470, 510, 30, "bold", GRAY, aa)
    rows = [("1 000 000", INK), ("− 4 000", RED), ("+ 4", GREEN), ("996 004", GREEN)]
    coluna(c, 1560, 280, rows, 64, [ep(t, q("b"), 0.4), ep(t, q("c"), 0.4), ep(t, q("d"), 0.4), ep(t, q("e"), 0.4)],
           lh=96, barra_antes=3)
    for cue, s_, yy in (("b", "1 000²", 280), ("c", "2 · 1 000 · 2", 376), ("d", "2²", 472)):
        text(c, s_, 960, yy + 12, 32, "bold", GRAY, ep(t, q(cue), 0.4), align="left")
    af = ep(t, q("f"), 0.5)
    if af > 0:
        K.atalho(c, 200, 600, 1520, 200, "ATALHO · PERTO DO REDONDO",
                 ["redondo² ± o dobro + passinho²"], af, 44)


# ======================================================================
# bloco b — gêmeos
# ======================================================================

def b_gemeos(c, t, C, B):
    head_seq(c, t, C, [("08", "OS GÊMEOS", "49 · 51", GREEN),
                       ("09", "SEM TERMO DO MEIO", "REDONDO² − PASSO²", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        fmid(c, "49 · 51 = ?", W / 2, 260, 72, "black", INK, ep(t, C["08.t"], 0.5))
        aa = ep(t, C["08.a"], 0.5)
        reta_gemeos(c, 340, 1580, 480, 50, 1, aa, u=ep(t, C["08.a"] + 0.6, 1.4), escala=3, rot=("49", "50", "51"))
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            selo(c, W / 2, 640, ab, "GÊMEOS: MESMA DISTÂNCIA DO REDONDO", GREEN, -2, 32)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            fmid(c, "(50 − 1)(50 + 1)", W / 2, 760, 56, "black", PURPLE, acc)
        return
    m(c, "(50-1)(50+1) = 50^2 - 1^2", W / 2, 290, 60, ep(t, C["09.t"], 0.5), hl={2: PURPLE, 3: PURPLE, 4: PURPLE})
    rows = [("2 500", INK), ("− 1", RED), ("2 499", GREEN)]
    coluna(c, 1100, 420, rows, 64, [ep(t, C["09.a"], 0.4), ep(t, C["09.b"], 0.4), ep(t, C["09.c"], 0.4)], lh=90,
           barra_antes=2)
    for cue, s_, yy in (("a", "50²", 420), ("b", "1²", 510)):
        text(c, s_, 700, yy + 12, 34, "bold", GRAY, ep(t, C[f"09.{cue}"], 0.4), align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1180, 400, 540, 260, "ATALHO · GÊMEOS", ["redondo²", "− passo²"], ad, 46)


# ======================================================================
# bloco c — diferença de dois quadrados
# ======================================================================

def b_difquad(c, t, C, B):
    head_seq(c, t, C, [("10", "DIFERENÇA DE QUADRADOS", "SOMA × DIFERENÇA", PURPLE),
                       ("11", "PARECE IMPOSSÍVEL?", "VIZINHOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        fmid(c, "87² − 13²", W / 2, 260, 80, "black", INK, ep(t, C["10.t"], 0.5))
        defin(c, "DIFERENÇA DE DOIS QUADRADOS", "um quadrado menos outro quadrado", 390, ep(t, C["10.a"], 0.5))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            regra(c, "a² − b² = (a + b)(a − b)", W / 2, 530, ab, 44)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            linha(c, [("87 + 13 = ", INK), ("100", GREEN)], 620, 670, 50, acc)
            linha(c, [("87 − 13 = ", INK), ("74", GREEN)], 1300, 670, 50, ep(t, C["10.c"] + 2.4, 0.4))
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            linha(c, [("100 · 74 = ", INK), ("7 400", GREEN)], W / 2, 780, 60, ad)
        return
    fmid(c, "2 025² − 2 024²", W / 2, 280, 84, "black", INK, ep(t, C["11.a"], 0.5))
    alarme(c, W / 2, 400, ep(t, C["11.b"], 0.5), t, 38)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("soma: 2 025 + 2 024 = ", INK), ("4 049", GREEN)], 640, 530, 40, acc)
        linha(c, [("diferença: 2 025 − 2 024 = ", INK), ("1", GREEN)], 1310, 530, 40, ep(t, C["11.c"] + 2.2, 0.4))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        linha(c, [("4 049 · 1 = ", INK), ("4 049", GREEN)], 600, 690, 56, ad)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1000, 600, 720, 200, "ATALHO · VIZINHOS", ["a diferença dos quadrados", "é a SOMA deles"], ae, 36)


# ======================================================================
# bloco d — conexão com Porcentagem
# ======================================================================

def b_porcent(c, t, C, B):
    head_seq(c, t, C, [("12", "CONEXÃO COM PORCENTAGEM", "+30% E −30%", PURPLE),
                       ("13", "LEMBRA DE PORCENTAGEM?", "DE ONDE VEM", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        barras_preco(c, 230, 760, aa, u=clamp((t - C["12.a"]) / 3.0) if t > C["12.a"] else 0)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("sobe: × ", INK), ("1,3", GREEN), ("    desce: × ", INK), ("0,7", RED)], 1330, 290, 40, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            fmid(c, "(1 + 0,3)(1 − 0,3)", 1330, 400, 50, "black", PURPLE, acc)
            text(c, "soma pela diferença", 1330, 460, 28, "bold", GRAY, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            linha(c, [("= 1 − 0,3² = 1 − 0,09 = ", INK), ("0,91", RED)], 1330, 560, 42, ad)
        ae = ep(t, C["12.e"], 0.5)
        if ae > 0:
            selo(c, 1330, 690, ae, "9% ABAIXO DO ORIGINAL", RED, -3, 36)
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        pill(c, "SÉRIE DE PORCENTAGEM", W / 2, 270, GREEN, size=28, a=aa, anchor="center", bounds=(0, 1920))
        linha(c, [("+20% e −20%  →  ", INK), ("−4%", RED)], W / 2, 370, 60, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("1,2 · 0,8 = 1 − 0,2² = 1 − ", INK), ("0,04", RED)], W / 2, 500, 54, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        regra(c, "(1 + p)(1 − p) = 1 − p²  →  perda de p²", W / 2, 660, acc, 44)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN),
                       ("15", "VAMOS JUNTOS", "GÊMEOS E REDONDO", GREEN)])
    card(c, *CARD_R)
    a1 = ep(t, C["14.a"], 0.5)
    a2 = ep(t, C["14.b"], 0.5)
    if t < C["15"]:
        fmid(c, "48 · 52 = ?", 620, 400, 80, "black", INK, a1)
        fmid(c, "103² = ?", 1300, 400, 80, "black", INK, a2)
        pause_timer(c, t, C["14.end"] - 1.9, W / 2, 640)
        return
    fmid(c, "48 · 52", 560, 250, 60, "black", INK, 1.0)
    fmid(c, "103²", 1360, 250, 60, "black", INK, 1.0)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        reta_gemeos(c, 260, 860, 450, 50, 2, aa, u=ep(t, C["15.a"] + 0.4, 1.2), escala=4, rot=("48", "50", "52"),
                    size=32)
        coluna(c, 640, 610, [("2 500", INK), ("− 4", RED), ("2 496", GREEN)], 52,
               [ep(t, C["15.a"] + 3.0, 0.4), ep(t, C["15.a"] + 3.8, 0.4), ep(t, C["15.a"] + 4.8, 0.4)], lh=74,
               barra_antes=2)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        fmid(c, "(100 + 3)²", 1360, 380, 48, "black", PURPLE, ab)
        coluna(c, 1500, 500, [("10 000", INK), ("+ 600", AMBER), ("+ 9", INK), ("10 609", GREEN)], 54,
               [ab, ep(t, C["15.b"] + 1.6, 0.4), ep(t, C["15.b"] + 2.6, 0.4), ep(t, C["15.b"] + 3.6, 0.4)], lh=80,
               barra_antes=3)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Gêmeos ao redor do redondo: redondo ao quadrado menos o passo ao quadrado.",
          "Diferença de quadrados vira soma vezes diferença.",
          "Conta grande demais é aviso de atalho."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "23"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 190 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("503 · 497 ≈ 250 000", "um sobe 3, o outro desce 3: parece que se compensam",
          "sobra o −3²: 250 000 − 9 = 249 991"),
         ("503 · 497 = 250 000 − 6", "2 · 3 = 6 parece o termo do meio do quadrado",
          "gêmeos não têm termo do meio: sai o passo², 9"),
         ("998² = 1 000 000 − 4 000 = 996 000", "é MENOS dois, então tudo parece ser de menos",
          "o passo² é sempre positivo: (−2)·(−2) = +4 → 996 004")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# questão 3 (você faz)
# ======================================================================

def _enunciado(c, s, a, y0=250, size=30, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS3 = [("A", "999 991", "", GREEN), ("B", "999 994", "subtraiu 6: termo do meio", RED),
         ("C", "999 997", "subtraiu só 3", RED), ("D", "1 000 000", "aproximou: ignorou o 3²", RED),
         ("E", "1 000 009", "trocou o sinal do 9", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "CONTA GRANDE SEM CALCULADORA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    yend = _enunciado(c, "Um depósito recebeu 1 003 caixas, cada uma com 997 parafusos. O número total de parafusos "
                      "recebidos é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["21"], 0.3)), align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1040, 250, 640, 40, C["21.ok"], "A", cues_in, cues_x, gap=40)
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 2.4, 540, 640, dur=2.1)
        return
    y0 = yend + 10
    ar = ep(t, C["21"], 0.4)
    rrect(c, 170, y0, 800, 830 - y0, 18, "#FFFFFF", ar, shadow=True)
    reta_gemeos(c, 230, 910, y0 + 120, 1000, 3, ep(t, C["21.a"], 0.4), u=ep(t, C["21.a"] + 1.5, 1.6), escala=5,
                rot=("997", "1 000", "1 003"), size=30)
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        linha(c, [("1 000² − 3² = 1 000 000 − 9", INK)], 570, y0 + 250, 34, ab)
    acc = ep(t, C["21.c"], 0.5)
    if acc > 0:
        linha(c, [("= ", INK), ("999 991", GREEN)], 570, y0 + 320, 46, acc)
    if t > C["22.c"]:
        text(c, "quase 1 000 × quase 1 000: pouco menos de 1 milhão", 570, min(y0 + 390, 810), 22, "bold", AMBER,
             ep(t, C["22.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DO ASSUNTO", PURPLE)
    itens = [("24.a", "juntamos tudo", "linguagem · produtos · fatoração · contas"),
             ("24.b", "caçamos as pegadinhas", "os erros que mais custam pontos"),
             ("24.c", "questões inéditas", "no formato do ENEM")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        sz = 34
        while text_w(s, "black", sz) > 440:
            sz -= 2
        text(c, s, x + 240, 480 + d, sz, "black", INK, a)
        sz2 = 24
        while text_w(sub, "bold", sz2) > 440:
            sz2 -= 1
        text(c, sub, x + 240, 540 + d, sz2, "bold", GRAY, a)
    pill(c, "ep. 5 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["24.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["25.like"], C["25.sub"], C["25.bell"], C["25.com"], C["25.bye"],
        "99² de cabeça: quanto dá?", canal="no Estudativo", anki=C["25.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, defs=b_defs, quadrado=b_quadrado,
              gemeos=b_gemeos, difquad=b_difquad, porcent=b_porcent, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q3=b_q3, ponte=b_ponte, cta=b_cta)
