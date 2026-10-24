"""Visual — Sistemas de Equações Lineares, Episódio 2: o método da adição e quando a pergunta já é a soma (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: nota() (nota fiscal da lanchonete), sacola() (a sacola com as duas compras), sistema() (duas
equações em COLUNAS: x embaixo de x, y embaixo de y), laco() (o "× 3" que abraça a equação inteira), traco() (a linha da
soma/subtração com o resultado), m().
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
_s = importlib.util.spec_from_file_location("comum037", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_sistemas_ep2_metodo_adicao.mp4"
CARD_R = K.CARD_R
COLS = (0, 150, 290, 420, 540)          # centros das colunas: termo x · sinal · termo y · = · total


def m(c, s, cx, cy, size, a=1.0, hl=None, align="center", col=None):
    """linha matemática (expr) de uma cor, com destaques por token: hl = {índice: cor}"""
    n = len(s.split())
    cores = {i: col or INK for i in range(n)}
    cores.update(hl or {})
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def defin(c, termo, s, y, a, w=1400, x=None):
    """faixa azul de definição: TERMO + frase"""
    if a <= 0:
        return
    x = W / 2 - w / 2 if x is None else x
    boxed(c, x, y - 50, w, 100, BLUE, a, 0.08)
    pill(c, termo, x + 24, y, BLUE, size=26, a=a)
    tw = text_w(termo, "bold", 26) + 70
    para(c, s, x + 24 + tw, y + 12, 32, "bold", INK, a, w - tw - 60)


# ======================================================================
# peças do episódio
# ======================================================================

def sanduiche(c, x, y, s, a):
    if a <= 0:
        return
    rrect(c, x - s / 2, y - s * 0.30, s, s * 0.26, s * 0.13, "#E2A55B", a)
    rrect(c, x - s * 0.52, y - s * 0.05, s * 1.04, s * 0.10, s * 0.05, "#6BB36B", a)
    rrect(c, x - s * 0.5, y + s * 0.05, s, s * 0.08, s * 0.04, "#C0533F", a)
    rrect(c, x - s / 2, y + s * 0.13, s, s * 0.18, s * 0.08, "#E2A55B", a)


def suco(c, x, y, s, a):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - s * 0.30, y - s * 0.40); p.lineTo(x + s * 0.30, y - s * 0.40)
    p.lineTo(x + s * 0.22, y + s * 0.40); p.lineTo(x - s * 0.22, y + s * 0.40); p.close()
    c.drawPath(p, paint("#F2A33A", a))
    c.drawPath(p, paint(INK2, a, stroke=3))
    line(c, x + s * 0.08, y - s * 0.40, x + s * 0.22, y - s * 0.68, "#D9534F", a, 5)


def itens(c, x, y, ns, nj, s, a):
    """ns sanduíches e nj sucos em fila, a partir de x"""
    for k in range(ns):
        sanduiche(c, x + k * s * 1.2, y, s, a)
    for k in range(nj):
        suco(c, x + (ns + k) * s * 1.2 + s * 0.2, y, s, a)


def nota(c, x, y, ns, nj, total, a, w=380, cor=None):
    """nota fiscal: canto serrilhado, itens desenhados e o total"""
    if a <= 0:
        return
    h = 270
    rrect(c, x, y, w, h, 6, "#FFFFFF", a, shadow=True)
    p = skia.Path()
    for k in range(int(w / 20) + 1):
        xx = x + k * 20
        (p.moveTo if k == 0 else p.lineTo)(xx, y + h)
        p.lineTo(xx + 10, y + h + 12)
    c.drawPath(p, paint("#FFFFFF", a))
    text(c, "NOTA FISCAL", x + w / 2, y + 44, 22, "black", GRAY, a, tracking=3)
    line(c, x + 24, y + 62, x + w - 24, y + 62, LIGHT, a, 2, dash=(8, 6))
    itens(c, x + 60, y + 120, ns, nj, 48, a)
    text(c, f"{ns} sanduíche{'s' if ns > 1 else ''} + {nj} suco{'s' if nj > 1 else ''}", x + w / 2, y + 190, 26, "bold",
         INK2, a)
    text(c, total, x + w / 2, y + 245, 40, "black", cor or INK, a)


def sacola(c, cx, cy, a, cheia=1.0, total="R$ 57,00", col=PURPLE):
    """sacola de papel com 3 sanduíches + 3 sucos e o total"""
    if a <= 0:
        return
    w, h = 520, 330
    x, y = cx - w / 2, cy - h / 2
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w - 24, y + h); p.lineTo(x + 24, y + h); p.close()
    c.drawPath(p, paint("#E9D7B4", a))
    c.drawPath(p, paint("#B99B66", a, stroke=4))
    for dx in (0.3, 0.7):
        ar = skia.Path(); ar.addArc(skia.Rect.MakeXYWH(x + w * dx - 50, y - 60, 100, 110), 180, 180)
        c.drawPath(ar, paint("#B99B66", a, stroke=7))
    itens(c, x + 70, y + 110, 3, 3, 56, a * cheia)
    text(c, "3 sanduíches + 3 sucos", cx, y + 220, 30, "black", INK, a * cheia)
    text(c, total, cx, y + 290, 52, "black", col, a * cheia)


def termos(eq):
    """'3x + 2y = 16' → ['3x', '+', '2y', '=', '16'] (5 colunas)"""
    return eq.split()


def sistema(c, x0, y0, eqs, size, a, cores=None, alfas=None, dy=None, col_x=COLS, chave=True):
    """equações alinhadas em colunas; cores = {(linha, coluna): cor}; devolve o y da última linha"""
    if a <= 0:
        return y0
    dy = dy or size * 1.55
    if chave:
        ab = a * (alfas[0] if alfas else 1)
        ytop, ybot = y0 - size * 0.7, y0 + dy * (min(2, len(eqs)) - 1) + size * 0.7
        p = skia.Path()
        xm = x0 - 70
        p.moveTo(xm + 20, ytop); p.quadTo(xm, ytop, xm, ytop + 30); p.lineTo(xm, (ytop + ybot) / 2 - 18)
        p.quadTo(xm, (ytop + ybot) / 2, xm - 18, (ytop + ybot) / 2); p.quadTo(xm, (ytop + ybot) / 2, xm, (ytop + ybot) / 2 + 18)
        p.lineTo(xm, ybot - 30); p.quadTo(xm, ybot, xm + 20, ybot)
        if len(eqs) >= 2:
            c.drawPath(p, paint(INK2, ab, stroke=4))
    for i, eq in enumerate(eqs):
        ai = a * (alfas[i] if alfas else 1)
        if ai <= 0:
            continue
        for j, tk in enumerate(termos(eq)):
            col = (cores or {}).get((i, j), INK)
            m(c, tk, x0 + col_x[j], y0 + i * dy, size, ai, col=col)
    return y0 + (len(eqs) - 1) * dy


def traco(c, x0, y, a, sinal="+", col=INK, col_x=COLS):
    """linha da soma (ou subtração) embaixo das equações, com o sinal à esquerda"""
    if a <= 0:
        return
    line(c, x0 - 60, y, x0 + col_x[-1] + 90, y, col, a, 4)
    text_mid(c, sinal, x0 - 110, y - 50, 56, "black", col, a)


def laco(c, x, y, w, h, a, rot="× 3", col=PURPLE, u=1.0):
    """o laço do multiplicador: contorno que abraça a equação inteira (u = progresso do contorno)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w * u, h), 26, 26)
    c.drawRRect(r, paint(col, a * 0.9, stroke=5))
    pill(c, rot, x - 16, y + h / 2, col, size=34, a=a, anchor="right", bounds=(0, 1920))


def flash(c, x, y, w, h, t, t0, a=1.0, col=None):
    f = ep(t, t0, 0.25) * (1 - ep(t, t0 + 1.2, 0.6)) * a
    if f > 0:
        rrect(c, x - w / 2, y - h / 2, w, h, 14, col or AMBER, 0.28 * f)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "SISTEMAS · O MÉTODO DA ADIÇÃO", PURPLE)
    nota(c, 260, 240, 2, 1, "R$ 31,00", ep(t, C["01.a"], 0.5))
    nota(c, 720, 240, 1, 2, "R$ 26,00", ep(t, C["01.b"], 0.5))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1200, 250, 520, 250, 26, "#FFFFFF", acc, shadow=True)
        sanduiche(c, 1340, 330, 70, acc)
        text_mid(c, "+", 1440, 330, 60, "black", INK2, acc)
        suco(c, 1540, 330, 70, acc)
        text(c, "juntos: quanto?", 1460, 450, 40, "black", BLUE, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "R$ 19,00", 1460, 640, GREEN, ad, 70)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        rrect(c, 260, 640, 840, 160, 22, mix("#FFFFFF", AMBER, 0.10), ae)
        text(c, "sem o preço do sanduíche", 680, 700, 36, "black", INK, ae)
        text(c, "e sem o preço do suco", 680, 760, 36, "black", INK, ae)
        selo(c, 1000, 640, ae, "?", AMBER, 8, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver sistemas pela adição", "3x + 2y = 16  e  5x - 2y = 16   →   8x = 32"),
            ("02.b", "reconhecer quando a pergunta sai somando", "x + y = ?   →   some antes de tudo")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 240 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        m(c, sub, 360, y + 90, 38, a, align="left", col=PURPLE)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE DO EPISÓDIO 1", "EM 20 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 250, 1400, 250, 26, "#FFFFFF", aa, shadow=True)
        text(c, "SISTEMA = duas equações que valem ao mesmo tempo", W / 2, 320, 36, "black", BLUE, aa)
        text(c, "quantidade × valor = total", W / 2, 420, 50, "black", PURPLE, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 560, 1400, 200, 26, mix("#FFFFFF", GREEN, 0.10), ab)
        check_icon(c, 420, 650, 34, ab, GREEN)
        text(c, "a resposta tem que BATER NAS DUAS", 1000, 665, 46, "black", GREEN, ab)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS NOTAS, UMA SACOLA", "JUNTE AS COMPRAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    ub = ep(t, C["04.b"], 1.2)          # as notas deslizam para o centro e somem dentro da sacola
    if aa > 0:
        fade = 1 - ep(t, C["04.c"], 0.5)
        nota(c, 200 + 330 * ub, 230 + 80 * ub, 2, 1, "R$ 31,00", aa * fade, 340)
        nota(c, 1380 - 330 * ub, 230 + 80 * ub, 1, 2, "R$ 26,00", aa * fade, 340)
        if ub > 0 and fade > 0:
            text_mid(c, "+", W / 2, 400, 90, "black", PURPLE, ub * fade)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        sacola(c, W / 2 - 250, 560, acc, ep(t, C["04.d"], 0.5))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        m(c, "31 + 26 = 57", W / 2 - 250, 300, 48, ad, hl={4: PURPLE})
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        rrect(c, 1180, 400, 470, 320, 26, mix("#FFFFFF", GREEN, 0.10), ae)
        text(c, "3 combos = R$ 57,00", 1415, 470, 34, "black", INK, ae)
        u = ep(t, C["04.e"] + 2.2, 0.6)
        m(c, "57 ÷ 3 = 19", 1415, 570, 54, u, hl={4: GREEN})
        text(c, "1 sanduíche + 1 suco", 1415, 660, 30, "black", GREEN, u)


# ======================================================================
# bloco a — coeficientes opostos
# ======================================================================

def b_opostos(c, t, C, B):
    head_seq(c, t, C, [("05", "MÉTODO DA ADIÇÃO", "SOMAR AS EQUAÇÕES", BLUE),
                       ("06", "COEFICIENTES OPOSTOS", "+2 E −2 SE ANULAM", PURPLE),
                       ("07", "COEFICIENTES OPOSTOS", "SOME LADO COM LADO", PURPLE),
                       ("08", "ATALHO", "OLHE A COLUNA ANTES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07", "08"])
    if sid == "05":
        defin(c, "MÉTODO DA ADIÇÃO", "somar as duas equações, lado com lado", 250, ep(t, C["05.a"], 0.5))
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            nota(c, 300, 340, 2, 1, "R$ 31,00", ab, 330)
            text_mid(c, "+", 720, 480, 80, "black", PURPLE, ab)
            nota(c, 780, 340, 1, 2, "R$ 26,00", ab, 330)
            text_mid(c, "=", 1180, 480, 80, "black", PURPLE, ab)
            rrect(c, 1250, 360, 380, 240, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
            text(c, "comprado + comprado", 1440, 440, 28, "black", INK, ab)
            text(c, "pago + pago", 1440, 520, 34, "black", PURPLE, ab)
        defin(c, "ELIMINAR UMA INCÓGNITA", "fazer uma das letras desaparecer da conta", 760, ep(t, C["05.c"], 0.5))
        return
    if sid in ("06", "07"):
        x0 = 520
        alf = [ep(t, C["06.a"], 0.5), ep(t, C["06.a"] + 1.8, 0.5)]
        cores = {}
        if t >= C["06.c"]:
            cores = {(0, 1): AMBER, (0, 2): AMBER, (1, 1): AMBER, (1, 2): AMBER}
        sistema(c, x0, 300, ["3x + 2y = 16", "5x - 2y = 16"], 64, 1.0, cores, alfas=alf)
        if sid == "06":
            ab = ep(t, C["06.b"], 0.5)
            if ab > 0:
                defin(c, "COEFICIENTE", "o número que multiplica a letra (o 3 de 3x)", 560, ab * (1 - ep(t, C["06.c"], 0.4)), 1300)
            acc = ep(t, C["06.c"], 0.5)
            if acc > 0:
                pill(c, "COEFICIENTES OPOSTOS: mesmo número, sinais contrários", W / 2, 560, PURPLE, size=28, a=acc,
                     anchor="center")
            ad = ep(t, C["06.d"], 0.5)
            if ad > 0:
                u = ep(t, C["06.d"] + 0.6, 1.2)
                chip(c, "+2y", 760 + 160 * u, 700, GREEN, ad * (1 - u), 46)
                chip(c, "−2y", 1160 - 160 * u, 700, RED, ad * (1 - u), 46)
                text(c, "0", W / 2, 720, 70, "black", PURPLE, ad * u)
                text(c, "o y some", W / 2, 790, 32, "black", PURPLE, ad * u)
            return
        ya = ep(t, C["07.a"], 0.5)
        traco(c, x0, 300 + 64 * 1.55 + 60, ya)
        if ya > 0:
            m(c, "8x", x0 + COLS[0], 300 + 64 * 1.55 * 2 + 20, 64, ya, col=PURPLE)
            m(c, "0", x0 + COLS[2], 300 + 64 * 1.55 * 2 + 20, 64, ya * 0.5, col=GRAY)
            m(c, "=", x0 + COLS[3], 300 + 64 * 1.55 * 2 + 20, 64, ya)
            m(c, "32", x0 + COLS[4], 300 + 64 * 1.55 * 2 + 20, 64, ya, col=PURPLE)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            chip(c, "x = 4", 1420, 320, GREEN, ab, 54)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            m(c, "12 + 2y = 16", 1420, 470, 42, acc)
            chip(c, "y = 2", 1420, 570, GREEN, acc, 54)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            m(c, "5·4 - 2·2 = 20 - 4 = 16", 1240, 760, 40, ad)
            conferido(c, "bateu", 1560, 780, ep(t, C["07.ok"], 0.4), True, 32)
        return
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 150, "ATALHO · OLHE A COLUNA ANTES", ["x embaixo de x · y embaixo de y"], aa, 38)
    for k, (cue, s, eqs, sinal, col) in enumerate((("08.b", "sinais OPOSTOS → SOME", ["3x + 2y = 16", "5x - 2y = 16"], "+",
                                                    GREEN),
                                                   ("08.c", "números IGUAIS → SUBTRAIA", ["6x + 9y = 36", "6x + 4y = 26"],
                                                    "−", PURPLE))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 420 + k * 720
        rrect(c, x - 170, 420, 660, 380, 24, mix("#FFFFFF", col, 0.08), a)
        text(c, s, x + 160, 480, 32, "black", col, a)
        hl = {(0, 2): col, (1, 2): col, (1, 1): col, (0, 1): col} if k == 0 else {(0, 0): col, (1, 0): col}
        sistema(c, x, 580, eqs, 44, a, hl, col_x=(0, 100, 190, 280, 360), chave=False)
        traco(c, x, 700, a, sinal, col, col_x=(0, 100, 190, 280, 360))
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        pill(c, "nos dois casos, a letra SOME", W / 2, 840, GREEN, size=28, a=ad, anchor="center")


# ======================================================================
# bloco b — multiplicando antes
# ======================================================================

def b_multiplicar(c, t, C, B):
    head_seq(c, t, C, [("09", "NENHUMA COLUNA SE ANULA?", "MULTIPLIQUE ANTES", PURPLE),
                       ("10", "MULTIPLICANDO ANTES", "IGUALE O x E SUBTRAIA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    x0 = 560
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        sistema(c, x0, 290, ["2x + 3y = 12", "3x + 2y = 13"], 62, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            check_icon(c, 1420, 300, 28, ab, RED, "x")
            text(c, "somar não apaga nada", 1470, 312, 30, "black", RED, ab, align="left")
            defin(c, "MULTIPLICAR A EQUAÇÃO", "multiplicar TODOS os termos pelo mesmo número", 500, ab, 1300)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            nota(c, 420, 565, 2, 3, "R$ 12,00", acc, 380)
            pill(c, "× 3", 900, 690, PURPLE, size=40, a=acc, anchor="center")
            arrow(c, 960, 690, 1080, 690, PURPLE, acc, 5, 18)
            rrect(c, 1100, 590, 560, 200, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
            text(c, "6 sanduíches + 9 sucos", 1380, 660, 34, "black", PURPLE, acc)
            text(c, "pago × 3 = R$ 36,00", 1380, 740, 38, "black", INK, acc)
        return
    aa = ep(t, C["10.a"], 0.5)
    ab = ep(t, C["10.b"], 0.5)
    eq1 = "6x + 9y = 36" if aa > 0.5 else "2x + 3y = 12"
    eq2 = "6x + 4y = 26" if ab > 0.5 else "3x + 2y = 13"
    cores = {(0, 4): PURPLE} if aa > 0.5 else {}
    if ab > 0.5:
        cores.update({(1, 4): PURPLE})
    if t >= C["10.c"]:
        cores.update({(0, 0): GREEN, (1, 0): GREEN})
    sistema(c, x0, 280, [eq1, eq2], 60, 1.0, cores)
    laco(c, x0 - 70, 280 - 50, 680, 100, aa, "× 3", PURPLE, ep(t, C["10.a"], 0.9))
    laco(c, x0 - 70, 280 + 93 - 50, 680, 100, ab, "× 2", PURPLE, ep(t, C["10.b"], 0.9))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        yl = 280 + 93 + 70
        traco(c, x0, yl, acc, "−", PURPLE)
        m(c, "0", x0 + COLS[0], yl + 60, 60, acc * 0.5, col=GRAY)
        m(c, "5y", x0 + COLS[2], yl + 60, 60, acc, col=PURPLE)
        m(c, "=", x0 + COLS[3], yl + 60, 60, acc)
        m(c, "10", x0 + COLS[4], yl + 60, 60, acc, col=PURPLE)
        chip(c, "y = 2", 1440, 320, GREEN, ep(t, C["10.c"] + 3.0, 0.4), 52)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        m(c, "2x + 6 = 12", 1440, 450, 40, ad)
        chip(c, "x = 3", 1440, 540, GREEN, ad, 52)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        m(c, "3·3 + 2·2 = 9 + 4 = 13", 1150, 760, 40, ae)
        conferido(c, "bateu", 1500, 780, ep(t, C["10.ok"], 0.4), True, 32)


# ======================================================================
# bloco c — a equação inteira
# ======================================================================

def b_inteira(c, t, C, B):
    head_seq(c, t, C, [("11", "MULTIPLIQUE A EQUAÇÃO INTEIRA", "O LAÇO VAI ATÉ O FIM", PURPLE),
                       ("12", "ATALHO", "MULTIPLIQUE CRUZADO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        x0 = 640
        aa = ep(t, C["11.a"], 0.5)
        sistema(c, x0, 300, ["2x + 3y = 12"], 70, aa, chave=False)
        laco(c, x0 - 80, 245, 720, 110, aa, "× 3", PURPLE, ep(t, C["11.a"] + 0.3, 1.4))
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            arrow(c, x0, 370, x0, 440, PURPLE, ab, 4, 14)
            arrow(c, x0 + COLS[2], 370, x0 + COLS[2], 440, PURPLE, ab, 4, 14)
            m(c, "6x", x0 + COLS[0], 500, 70, ab, col=PURPLE)
            m(c, "+", x0 + COLS[1], 500, 70, ab)
            m(c, "9y", x0 + COLS[2], 500, 70, ab, col=PURPLE)
            m(c, "=", x0 + COLS[3], 500, 70, ab)
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            arrow(c, x0 + COLS[4], 370, x0 + COLS[4], 440, PURPLE, acc, 4, 14)
            m(c, "36", x0 + COLS[4], 500, 70, acc, col=GREEN)
            flash(c, x0 + COLS[4], 500, 150, 100, t, C["11.c"] + 0.3, col=GREEN)
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            m(c, "6x + 9y = 12", 700, 690, 50, ad, col=RED)
            strike(c, 560, 690, 840, 690, ad, RED, ad)
            text(c, "quem compra 3 vezes PAGA 3 vezes", 1290, 702, 34, "black", PURPLE, ad)
        return
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 150, "ATALHO · MULTIPLIQUE CRUZADO", ["cada equação × o coeficiente DA OUTRA"], aa, 38)
    ab = ep(t, C["12.a"] + 0.3, 0.5)
    if ab > 0:
        x0 = 620
        sistema(c, x0, 480, ["2x + 3y = 12", "3x + 2y = 13"], 54, ab, {(0, 0): AMBER, (1, 0): AMBER})
        u = ep(t, C["12.b"], 0.8)
        if u > 0:
            pill(c, "× 3", x0 + 720, 480, GREEN, size=34, a=u)
            pill(c, "× 2", x0 + 720, 480 + 84, GREEN, size=34, a=u)
            arrow(c, x0 + 30, 545, x0 + 700, 495, GREEN, u * 0.7, 3, 12)
            arrow(c, x0 + 30, 505, x0 + 700, 555, GREEN, u * 0.7, 3, 12)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        chip(c, "6x  e  6x", W / 2, 760, GREEN, acc, 48)


# ======================================================================
# bloco d — a pergunta é a soma
# ======================================================================

def b_soma(c, t, C, B):
    head_seq(c, t, C, [("13", "ÀS VEZES A PERGUNTA É A SOMA", "x + y EM UMA LINHA", GREEN),
                       ("14", "ATALHO", "COEFICIENTES TROCADOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    x0 = 560
    if sid == "13":
        sistema(c, x0, 280, ["2x + 3y = 12", "3x + 2y = 13"], 60, ep(t, C["13"], 0.5))
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            chip(c, "x + y = ?", 1460, 300, BLUE, aa, 50)
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            traco(c, x0, 280 + 93 + 66, ab, "+", GREEN)
            text(c, "sem multiplicar nada", 1460, 410, 28, "black", GREEN, ab)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            yl = 280 + 93 + 130
            m(c, "5x", x0 + COLS[0], yl, 60, acc, col=GREEN)
            m(c, "+", x0 + COLS[1], yl, 60, acc)
            m(c, "5y", x0 + COLS[2], yl, 60, acc, col=GREEN)
            m(c, "=", x0 + COLS[3], yl, 60, acc)
            m(c, "25", x0 + COLS[4], yl, 60, acc, col=GREEN)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            rrect(c, 520, 600, 880, 170, 24, mix("#FFFFFF", GREEN, 0.12), ad)
            m(c, "x + y = 25/5 = 5", W / 2, 685, 58, ad, hl={6: GREEN})
        ae = ep(t, C["13.e"], 0.5)
        if ae > 0:
            conferido(c, "3 + 2 = 5", 1460, 560, ae, True, 34)
        return
    aa = ep(t, C["14.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 150, "ATALHO · COEFICIENTES TROCADOS", ["2 e 3 numa · 3 e 2 na outra → SOME"], aa, 38)
    if aa > 0:
        sistema(c, 560, 480, ["2x + 3y = 12", "3x + 2y = 13"], 54, aa,
                {(0, 0): GREEN, (0, 2): AMBER, (1, 0): AMBER, (1, 2): GREEN})
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        m(c, "5x + 5y = 25", 1440, 520, 50, ab, hl={0: GREEN, 2: GREEN})
        text(c, "o mesmo coeficiente", 1440, 600, 28, "black", GREEN, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pill(c, "às vezes a SACOLA já é a resposta", W / 2, 760, GREEN, size=32, a=acc, anchor="center")


# ======================================================================
# bloco e — qual método
# ======================================================================

def b_escolha(c, t, C, B):
    head(c, t, B["start"], "SUBSTITUIÇÃO OU ADIÇÃO?", "COMO ESCOLHER", PURPLE)
    card(c, *CARD_R)
    cards = [("15.a", "letra sozinha (coeficiente 1)", "x + 2y = 11", "SUBSTITUIÇÃO", BLUE, {0: BLUE}),
             ("15.b", "opostos ou fáceis de igualar", "+2y  e  -2y", "ADIÇÃO", PURPLE, {0: PURPLE, 3: PURPLE}),
             ("15.c", "a pergunta é x + y", "x + y = ?", "SOME ANTES DE TUDO", GREEN, {0: GREEN, 2: GREEN})]
    for k, (cue, cond, ex, met, col, hl) in enumerate(cards):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 230 + k * 500
        rrect(c, x, 240, 460, 520, 24, mix("#FFFFFF", col, 0.08), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 240, 460, 520), 24, 24), paint(col, a, stroke=3))
        para(c, cond, x + 30, 320, 32, "black", INK, a, 400)
        m(c, ex, x + 230, 470, 48, a, hl=hl)
        arrow(c, x + 230, 540, x + 230, 600, col, a, 4, 14)
        chip(c, met, x + 230, 670, col, a, 32 if len(met) < 14 else 26)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "COLUNA · SOMA · CONFERÊNCIA", GREEN)])
    card(c, *CARD_R)
    x0 = 520
    aa = ep(t, C["16.a"], 0.5)
    cores = {(0, 1): AMBER, (0, 2): AMBER, (1, 1): AMBER, (1, 2): AMBER} if t >= C["17.a"] else {}
    sistema(c, x0, 280, ["x + 2y = 11", "3x - 2y = 1"], 60, aa, cores)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 1440, 330)
        return
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        yl = 280 + 93 + 66
        traco(c, x0, yl, ab, "+", GREEN)
        for j, s in enumerate(("4x", "", "0", "=", "12")):
            if s:
                m(c, s, x0 + COLS[j], yl + 64, 60, ab * (0.5 if s == "0" else 1), col=GRAY if s == "0" else PURPLE)
        chip(c, "x = 3", 1440, 300, GREEN, ab, 52)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        m(c, "3 + 2y = 11", 1440, 430, 40, acc)
        chip(c, "y = 4", 1440, 520, GREEN, acc, 52)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        m(c, "3·3 - 2·4 = 9 - 8 = 1", 1060, 740, 42, ad)
        conferido(c, "bateu", 1420, 760, ep(t, C["17.ok"], 0.4), True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Some as equações para uma incógnita sumir.",
          "Multiplicou? Multiplique a equação inteira.",
          "Antes de resolver, olhe o que foi pedido."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("2x + 3y = 12 vezes 3 → 6x + 9y = 12", "o olho fica nas letras, e o lado direito é esquecido",
          "o laço vai até o fim: 6x + 9y = 36 · com o 12, sairia y = −2,8 (preço negativo!)"),
         ("pediu pão + café e você achou cada preço (R$ 3,50 e R$ 2,50)", "achar cada preço é o caminho de sempre",
          "some as duas notas: 4 pães + 4 cafés = R$ 24,00 → um de cada = R$ 6,00"),
         ("6x + 9y e 6x + 4y somados: 12x + 13y = 62", "o método se chama ADIÇÃO",
          "coeficientes IGUAIS pedem SUBTRAÇÃO: sobra 5y = 10")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questão 4 do material (eu faço)
# ======================================================================

ALTS4 = [("A", "10 kg", "usou 40 − 30 como quantidade", RED), ("B", "20 kg", "", GREEN),
         ("C", "30 kg", "meio a meio: preço médio R$ 37,50", RED), ("D", "40 kg", "é o café CARO", RED),
         ("E", "50 kg", "60 − 10", RED)]
ENUN4 = ("Um comerciante mistura um café de R$ 30,00 o quilograma com outro de R$ 45,00 o quilograma e obtém 60 kg de um "
         "blend que vende a R$ 40,00 o quilograma, sem ganho nem perda em relação ao custo dos cafés. A quantidade usada "
         "do café mais barato foi de")


def enunciado(c, s, a, y=230, maxw=720, size=26, fim=None):
    yy = y
    for ln in K.wrap(s, "black", size, maxw):
        ftext(c, ln, 190, yy, size, "black", INK, a, align="left")
        yy += size + 12
    return yy


def b_q4(c, t, C, B):
    head_seq(c, t, C, [("22", "QUESTÃO 4 · EU FAÇO", "MISTURA DE CAFÉS", BLUE), ("23", "QUESTÃO 4 · EU FAÇO", "AS ETIQUETAS",
                                                                               BLUE),
                       ("24", "QUESTÃO 4 · EU FAÇO", "PELA ADIÇÃO", PURPLE), ("25", "QUESTÃO 4 · EU FAÇO",
                                                                             "CONFERE E RESPONDE", GREEN),
                       ("26", "QUESTÃO 4", "AS ALTERNATIVAS ERRADAS", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["22", "23", "24", "25", "26"])
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    if sid == "22" or sid == "26":
        a0 = ep(t, C["22.a"], 0.4)
        enunciado(c, ENUN4, a0)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        K.alternativas(c, t, C, ALTS4, 1000, 260, 680, 40, C["25.b"], "B", cues_in, cues_x, gap=34)
        return
    # resolução: alternativas encolhidas à direita, contas à esquerda
    K.alternativas(c, t, C, ALTS4, 1240, 250, 420, 30, C["25.b"], "B", cues_in, cues_x, gap=26)
    x0 = 330
    ca = (0, 120, 290, 430, 600)
    aa = ep(t, C["23.a"], 0.5)
    if aa > 0:
        pill(c, "a = café barato (kg)", 190, 240, BLUE, size=24, a=aa)
        pill(c, "b = café caro (kg)", 560, 240, AMBER, size=24, a=aa)
    alf = [ep(t, C["23.b"], 0.5), ep(t, C["23.c"], 0.5)]
    e1 = "30a + 30b = 1800" if t >= C["24.a"] + 0.6 else "a + b = 60"
    sistema(c, x0, 350, [e1, "30a + 45b = 2400"], 48, 1.0, {(0, 4): PURPLE} if t >= C["24.a"] + 0.6 else {}, alfas=alf,
            col_x=ca)
    if sid == "23":
        acc = ep(t, C["23.c"], 0.5)
        if acc > 0:
            text(c, "40 · 60 = 2 400 (o blend todo)", x0 + 300, 520, 28, "black", INK2, acc)
        return
    if sid == "24":
        laco(c, x0 - 60, 350 - 42, 770, 84, ep(t, C["24.a"], 0.5), "× 30", PURPLE, ep(t, C["24.a"], 0.9))
        ab = ep(t, C["24.b"], 0.5)
        if ab > 0:
            traco(c, x0, 350 + 75 + 56, ab, "−", PURPLE, ca)
        acc = ep(t, C["24.c"], 0.5)
        if acc > 0:
            m(c, "15b = 600", x0 + 300, 540, 48, acc, col=PURPLE)
            chip(c, "b = 40", 400, 650, AMBER, acc, 44)
            chip(c, "a = 60 − 40 = 20", 820, 650, BLUE, ep(t, C["24.c"] + 2.5, 0.4), 40)
        ad = ep(t, C["24.d"], 0.5)
        if ad > 0:
            text(c, "substituição (ep. 1): 30a + 45(60 − a) = 2 400 → 15a = 300", 620, 770, 26, "black", INK2, ad)
        return
    aa = ep(t, C["25.a"], 0.5)
    if aa > 0:
        m(c, "20·30 + 40·45 = 600 + 1800 = 2400", 620, 540, 38, aa)
        conferido(c, "bateu", 520, 620, ep(t, C["25.ok"], 0.4), True, 32)
    ab = ep(t, C["25.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 680, 800, 110, 22, mix("#FFFFFF", GREEN, 0.12), ab)
        text(c, "pediu o BARATO: a = 20 kg", 620, 748, 40, "black", GREEN, ab)


# ======================================================================
# questão 7 do material (você faz)
# ======================================================================

ALTS7 = [("A", "R$ 7,00", "é o suco", RED), ("B", "R$ 12,00", "é o sanduíche", RED), ("C", "R$ 19,00", "", GREEN),
         ("D", "R$ 28,50", "57 ÷ 2", RED), ("E", "R$ 57,00", "a sacola: 3 de cada", RED)]
ENUN7 = ("Em uma lanchonete, dois sanduíches e um suco custam R$ 31,00, e um sanduíche e dois sucos custam R$ 26,00. "
         "Todos os sanduíches têm o mesmo preço, assim como os sucos. Quanto custam, juntos, um sanduíche e um suco?")


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("27", "QUESTÃO 7 · VOCÊ FAZ", "COMBO DE LANCHONETE", GREEN),
                       ("28", "QUESTÃO 7 · CONFERINDO", "A PERGUNTA É A SOMA", GREEN),
                       ("29", "QUESTÃO 7", "AS ALTERNATIVAS ERRADAS", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["27", "28", "29"])
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    if sid in ("27", "29"):
        a0 = ep(t, C["27.a"], 0.4)
        yy = enunciado(c, ENUN7, a0)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 40, C["28.ok"], "C", cues_in, cues_x, gap=34)
        if sid == "27":
            pause_timer(c, t, C["27.p"] + 0.1, 540, min(yy + 120, 720))
        return
    K.alternativas(c, t, C, ALTS7, 1240, 250, 420, 30, C["28.ok"], "C", cues_in, cues_x, gap=26)
    x0 = 330
    ca = (0, 120, 250, 370, 520)
    sistema(c, x0, 320, ["2S + J = 31", "S + 2J = 26"], 50, 1.0, col_x=ca)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        traco(c, x0, 320 + 78 + 56, aa, "+", GREEN, ca)
        m(c, "3S + 3J = 57", x0 + 260, 520, 50, aa, col=GREEN)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 565, 820, 135, 22, mix("#FFFFFF", GREEN, 0.12), ab)
        m(c, "S + J = 57/3 = 19", 630, 630, 48, ab, hl={6: GREEN})
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        text(c, "subtraindo: S − J = 5  →  S = 12, J = 7", 630, 735, 30, "black", INK2, acc)
    ad = ep(t, C["28.d"], 0.5)
    if ad > 0:
        conferido(c, "2·12 + 7 = 31", 440, 805, ad, True, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS TRÊS POSIÇÕES DE DUAS RETAS", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        rrect(c, 610, 250, 700, 180, 30, "#FFFFFF", aa, shadow=True)
        m(c, "0 = 2", W / 2, 340, 110, aa, col=RED)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        chip(c, "você errou?", 650, 560, AMBER, ab, 44)
        chip(c, "ou o sistema está dizendo algo?", 1250, 560, BLUE, ab, 40)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        for k, (dx, inc) in enumerate(((-420, (0.6, -0.6)), (0, (0.35, 0.35)), (420, (0.4, 0.4)))):
            x = W / 2 + dx
            line(c, x - 130, 760 - 130 * inc[0], x + 130, 760 + 130 * inc[0], PURPLE, acc, 5)
            off = 0 if k != 1 else 40
            line(c, x - 130, 760 - 130 * inc[1] + off, x + 130, 760 + 130 * inc[1] + off, BLUE, acc, 5)
        text(c, "ep. 3", W / 2 + 720, 770, 30, "black", PURPLE, acc)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Já resolveu um sistema inteiro quando a pergunta era só a soma?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, opostos=b_opostos,
              multiplicar=b_multiplicar, inteira=b_inteira, soma=b_soma, escolha=b_escolha, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q4=b_q4, q7=b_q7, ponte=b_ponte, cta=b_cta)
