"""Visual — Juros Compostos e Montante, Episódio 1: juros sobre juros e a fórmula M = C · (1 + i)ᵗ (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, fila...).
Peças deste episódio: bola() (a bola de neve com ×1,1 a cada volta), barra_juros() (os juros do mês: a parte que vem do
capital em verde e a parte que NASCE dos juros anteriores em âmbar), tabela() (seção 02 montada mês a mês),
pot() (texto com expoente pequeno, para o "t" da fórmula), linha(), etiqueta().
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
_s = importlib.util.spec_from_file_location("comum029", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_compostos_ep1_juros_sobre_juros.mp4"
CARD_R = K.CARD_R
NEVE = "#DCEBF7"
NEVE2 = "#9CC3E4"

COR = dict(C=BLUE, i=PURPLE, t=AMBER, J=GREEN, M=RED)


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


def pot(c, base, exp, cx, cy, size, a, col_b=None, col_e=None, align="center"):
    """base com expoente pequeno (ex.: 'M = C · (1 + i)' com 't'); base pode ser lista de (texto, cor)"""
    partes = base if isinstance(base, list) else [(base, col_b or INK)]
    wb = sum(ftext_w(s_, "black", size) for s_, _ in partes)
    we = ftext_w(exp, "black", size * 0.6)
    if a <= 0:
        return wb + we
    x0 = cx - (wb + we) / 2 if align == "center" else cx
    linha(c, partes, x0, cy, size, a, align="left")
    ftext(c, exp, x0 + wb + 4, cy - size * 0.18, size * 0.6, "black", col_e or AMBER, a, align="left")
    return wb + we


def formula(c, cx, cy, size, a):
    """M = C · (1 + i)ᵗ com cada letra na sua cor; devolve (x do '(1 + i)', x do fim do parêntese, largura)"""
    partes = [("M", RED), (" = ", INK), ("C", BLUE), (" · (1 + ", INK), ("i", PURPLE), (")", INK)]
    w = pot(c, partes, "t", cx, cy, size, a)
    x0 = cx - w / 2
    xa = x0 + ftext_w("M = C · ", "black", size)
    xb = x0 + ftext_w("M = C · (1 + i)", "black", size)
    return xa, xb, w


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def etiqueta(c, letra, valor, cx, cy, a, size=36):
    """cartão com a letra (C, i, t, J ou M) em cima e o valor com unidade embaixo"""
    if a <= 0:
        return
    col = COR[letra]
    w = max(ftext_w(valor, "black", size) + 60, 150)
    rrect(c, cx - w / 2, cy - 60, w, 130, 18, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - 60, w, 50, 18, col, a * 0.16)
    text_mid(c, letra, cx, cy - 35, 34, "black", col, a)
    fmid(c, valor, cx, cy + 32, size, "black", INK, a)


def bola(c, cx, cy, r, a, rot=0.0):
    """bola de neve com textura girando"""
    if a <= 0:
        return
    c.drawCircle(cx + r * 0.08, cy + r * 0.1, r, paint("#000000", a * 0.10))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(NEVE2, a, stroke=max(3, r * 0.05)))
    for k in range(5):
        ang = rot + k * 2 * math.pi / 5
        c.drawCircle(cx + r * 0.55 * math.cos(ang), cy + r * 0.55 * math.sin(ang), r * 0.14, paint(NEVE, a))
    c.drawCircle(cx - r * 0.3, cy - r * 0.35, r * 0.18, paint("#FFFFFF", a * 0.9))


def bola_rampa(c, t, t0, x0, y0, x1, y1, a, voltas=4, dur=4.0, r0=34, k=1.1):
    """a bola de neve descendo a rampa: a cada volta cresce ×1,1 (visualmente exagerado) e aparece o rótulo"""
    if a <= 0:
        return
    line(c, x0 - 40, y0 + r0 + 6, x1 + 80, y1 + r0 * 2.6 + 6, NEVE2, a, 8)
    u = clamp((t - t0) / dur)
    n = int(u * voltas)
    for j in range(1, voltas + 1):
        f = j / voltas
        xx = lerp(x0, x1, f)
        yy = lerp(y0, y1, f)
        aj = a * ep(t, t0 + dur * f - 0.2, 0.3)
        if aj > 0:
            pill(c, "× 1,1", xx, yy - 40 - r0 * (1.3 ** j) * 2, BLUE, size=24, a=aj, anchor="center")
    rr = r0 * (1.3 ** (u * voltas))
    xx = lerp(x0, x1, u)
    yy = lerp(y0, y1, u) + (r0 - rr) * -1 + 0 * n
    bola(c, xx, yy - rr + r0, rr, a, rot=u * 9)


def fichas(c, x, cy, itens, a, size, sep=None, gap=30):
    """fichas de fatores com largura pelo texto: itens = [(texto, cor)]"""
    if a <= 0:
        return 0
    xx = x
    for k, (s_, col) in enumerate(itens):
        w = ftext_w(s_, "black", size) + size * 0.9
        rrect(c, xx, cy - size * 0.9, w, size * 1.8, 14, mix("#FFFFFF", col, 0.14), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, cy - size * 0.9, w, size * 1.8), 14, 14), paint(col, a, stroke=3))
        fmid(c, s_, xx + w / 2, cy, size, "black", col, a)
        xx += w
        if sep and k < len(itens) - 1:
            fmid(c, sep, xx + gap / 2, cy, size, "black", INK, a)
        xx += gap
    return xx - gap - x


def barra_juros(c, x, base, val, a, esc=1.6, w=86, extra_a=1.0, rot=True, simples=False):
    """barra dos juros de um mês: até 100 vem do capital (verde); o que passa de 100 nasceu dos juros anteriores (âmbar)"""
    if a <= 0:
        return
    h100 = 100 * esc
    rrect(c, x, base - h100, w, h100, 8, GREEN if not simples else BLUE, a * 0.85)
    ex = val - 100
    if ex > 0:
        hx = ex * esc * extra_a
        rrect(c, x, base - h100 - hx - 4, w, hx, 8, AMBER, a)
    if rot:
        s = f"{val:.2f}".replace(".", ",").replace(",00", "")
        fmid(c, s, x + w / 2, base - h100 - max(ex, 0) * esc - 30, 28, "black", INK, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS COMPOSTOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 220, 1200, 110, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("R$ 1.000,00", BLUE), ("  ·  ", GRAY), ("10% ao mês", PURPLE), ("  ·  ", GRAY), ("4 meses", AMBER)],
              W / 2, 275, 54, aa)
    base = 800
    ab = ep(t, C["01.b"], 0.6)
    if ab > 0:
        h = 1400 * 0.19 * ab
        rrect(c, 520, base - h, 240, h, 14, BLUE, 0.85)
        text(c, "JUROS SIMPLES", 640, base + 46, 28, "black", BLUE, ab)
        fmid(c, "R$ 1.400,00", 640, base - h - 40, 44, "black", INK, ab)
    acc = ep(t, C["01.c"], 0.6)
    if acc > 0:
        h1 = 1400 * 0.19 * acc
        h2 = 64.1 * 0.19 * 3.0 * ep(t, C["01.e"], 0.6)
        rrect(c, 1160, base - h1, 240, h1, 14, GREEN, 0.85)
        if h2 > 0:
            rrect(c, 1160, base - h1 - h2 - 4, 240, h2, 10, AMBER, 1)
        text(c, "JUROS COMPOSTOS", 1280, base + 46, 28, "black", GREEN, acc)
        fmid(c, "R$ 1.464,10", 1280, base - h1 - h2 - 40, 44, "black", INK, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "os MESMOS 10%", W / 2, 520, PURPLE, size=30, a=ad, anchor="center")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, 1580, 440, ae, "+ R$ 64,10", AMBER, -6, 40)
        text(c, "juros que passaram", 1580, 530, 26, "black", AMBER, ae)
        text(c, "a render juros", 1580, 566, 26, "black", AMBER, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular QUALQUER montante em juros compostos", "M = C · (1 + i)ᵗ"),
            ("02.b", "encadear taxas diferentes sem somar porcentagens", "+10%, +20%, −25%  →  multiplique os fatores")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        if j == 0:
            pot(c, [("M = C · (1 + i)", GRAY)], "t", 360, y + 50, 36, a, col_e=GRAY, align="left")
        else:
            ftext(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    cols = [("03.a", "JUROS SIMPLES", BLUE), ("03.b", "PORCENTAGEM", PURPLE), ("03.c", "POTENCIAÇÃO", AMBER)]
    for k, (cue, tit, col) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 520
        rrect(c, x, 250 + d, 480, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250 + d, 480, 66, 24, col, a * 0.16)
        text(c, "da série de " + tit.title() if False else tit, x + 240, 295 + d, 28, "black", col, a)
        if k == 0:
            for j, (L, s) in enumerate((("C", "capital: o começo"), ("J", "juros: o acréscimo"), ("M", "montante: o total"))):
                text_mid(c, L, x + 70, 400 + j * 100 + d, 54, "black", COR[L], a)
                text(c, s, x + 120, 412 + j * 100 + d, 30, "bold", INK2, a, align="left")
        elif k == 1:
            linha(c, [("+10%", AMBER), ("  →  ", GRAY), ("× 1,10", PURPLE)], x + 240, 420 + d, 46, a)
            text(c, "dois aumentos seguidos:", x + 240, 530 + d, 26, "bold", GRAY, a)
            text(c, "MULTIPLICAM os fatores", x + 240, 580 + d, 30, "black", PURPLE, a)
        else:
            linha(c, [("1,1³", AMBER)], x + 240, 420 + d, 64, a)
            fmid(c, "= 1,1 · 1,1 · 1,1", x + 240, 530 + d, 38, "black", INK, a)
            text(c, "multiplicação repetida", x + 240, 610 + d, 26, "bold", GRAY, a)


def cartao(c, cx, cy, s, a):
    if a <= 0:
        return
    rrect(c, cx - 150, cy - 95, 300, 190, 20, PURPLE, a, shadow=True)
    rrect(c, cx - 110, cy - 45, 60, 44, 8, "#F2C94C", a)
    text(c, "•••• 4321", cx, cy + 60, 26, "black", "#FFFFFF", a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "CRESCE SOZINHO?", "DÍVIDA E POUPANÇA", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"] - 1.5, 0.5)
    if a1 > 0:
        cartao(c, 400, 360, "", a1)
        for j, v in enumerate(("R$ 500", "R$ 550", "R$ 605")):
            fmid(c, v, 680, 290 + j * 75, 40 + j * 6, "black", RED, a1 * ep(t, C["04.a"] + j * 1.0, 0.4))
        text(c, "a dívida do cartão", 400, 520, 28, "black", INK2, a1)
    a2 = ep(t, C["04.b"], 0.5)
    if a2 > 0:
        rrect(c, 980, 250, 260, 220, 30, mix("#FFFFFF", GREEN, 0.14), a2)
        text_mid(c, "$", 1110, 360, 110, "black", GREEN, a2)
        text(c, "a poupança", 1110, 520, 28, "black", INK2, a2)
        text(c, "rende sobre o que JÁ rendeu", 1500, 370, 28, "black", GREEN, a2)
    a3 = ep(t, C["04.c"], 0.5)
    if a3 > 0:
        bola_rampa(c, t, C["04.c"] + 0.4, 300, 700, 980, 725, a3, voltas=4, dur=5.0, r0=24)
        regra(c, "BOLA DE NEVE: neve sobre a neve que já tinha", 1420, 760, a3, 24, BLUE)


# ======================================================================
# bloco a — a definição
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "JUROS COMPOSTOS", "O QUE MUDA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 230, 1400, 90, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text_mid(c, "SALDO = quanto você tem na conta naquele momento", W / 2, 275, 36, "black", BLUE, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 400, 420, 200, 24, "#FFFFFF", ab, shadow=True)
        text(c, "SALDO DO MÊS ANTERIOR", 510, 450, 24, "black", GRAY, ab)
        fmid(c, "R$ 1.100,00", 510, 510, 46, "black", INK, ab)
        text(c, "(já com os juros)", 510, 570, 24, "bold", AMBER, ab)
        arrow(c, 740, 500, 960, 500, PURPLE, ab, 6, 20)
        text(c, "× 10%", 850, 470, 30, "black", PURPLE, ab)
        rrect(c, 980, 420, 300, 160, 24, mix("#FFFFFF", GREEN, 0.14), ab)
        text(c, "JUROS DO MÊS", 1130, 470, 24, "black", GRAY, ab)
        fmid(c, "R$ 110,00", 1130, 525, 46, "black", GREEN, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        p = skia.Path(); p.moveTo(1130, 590); p.cubicTo(1130, 720, 520, 720, 510, 612)
        c.drawPath(p, paint(GREEN, acc, stroke=6))
        arrow(c, 514, 640, 510, 610, GREEN, acc, 6, 18)
        text(c, "entra no saldo e passa a render", 820, 715, 28, "black", GREEN, acc)
        regra(c, "CAPITALIZAR = incorporar os juros ao saldo", W / 2, 800, acc, 34, BLUE)


# ======================================================================
# bloco b — a tabela, mês a mês
# ======================================================================

LIN = [("1", "100", "1.100", 100.0, "1.100"), ("2", "100", "1.200", 110.0, "1.210"),
       ("3", "100", "1.300", 121.0, "1.331"), ("4", "100", "1.400", 133.10, "1.464,10")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "MÊS A MÊS", "R$ 1.000,00 A 10% AO MÊS", BLUE)
    card(c, *CARD_R)
    xs = [230, 440, 680, 960, 1240]
    hdr = ["mês", "juros simples", "saldo simples", "juros compostos", "saldo composto"]
    a0 = ep(t, B["start"], 0.5)
    for x, h_ in zip(xs, hdr):
        col = BLUE if "simples" in h_ else (GREEN if "compostos" in h_ or "composto" in h_ else GRAY)
        text(c, h_, x, 250, 24, "black", col, a0)
    line(c, 160, 272, 1380, 272, "#E2E2DE", a0, 3)
    cues = [C["06.a"], C["06.b"], C["07.a"], C["07.b"]]
    simp_a = ep(t, C["07.c"], 0.5)
    for k, (m, js, ss, jc, sc) in enumerate(LIN):
        a = ep(t, cues[k], 0.5)
        if a <= 0:
            continue
        y = 330 + k * 92
        fmid(c, m, xs[0], y, 36, "black", INK, a)
        fmid(c, js, xs[1], y, 36, "black", BLUE, a * max(simp_a, 0.35))
        fmid(c, ss, xs[2], y, 36, "black", BLUE, a * max(simp_a, 0.35))
        fmid(c, f"{jc:.2f}".replace(".", ",").replace(",00", ""), xs[3], y, 36, "black", GREEN, a)
        fmid(c, sc, xs[4], y, 36, "black", INK, a)
    # as barras dos juros compostos: o pedaço âmbar nasce dos juros anteriores
    for k, (_, _, _, jc, _) in enumerate(LIN):
        a = ep(t, cues[k] + 0.6, 0.5)
        barra_juros(c, 1440 + k * 76, 720, jc, a, esc=2.4, w=62, rot=False)
    a1 = ep(t, cues[0] + 0.6, 0.5)
    if a1 > 0:
        text(c, "juros compostos", 1590, 760, 22, "black", GREEN, a1)
        rrect(c, 1470, 782, 18, 18, 4, AMBER, ep(t, cues[1] + 0.8, 0.4))
        text(c, "nasceu dos juros", 1500, 798, 20, "bold", AMBER, ep(t, cues[1] + 0.8, 0.4), align="left")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "sempre 10%, mas de um saldo CADA VEZ MAIOR", 770, 720, PURPLE, size=28, a=ad, anchor="center")


# ======================================================================
# bloco c — onde nasce a diferença
# ======================================================================

def b_diferenca(c, t, C, B):
    head(c, t, B["start"], "ONDE NASCE A DIFERENÇA?", "JUROS DE CADA MÊS", BLUE)
    card(c, *CARD_R)
    base = 700
    dif = ["0", "10", "21", "33,10"]
    cues = [C["08.a"], C["08.b"], C["08.c"], C["08.c"] + 1.2]
    for k, (_, _, _, jc, _) in enumerate(LIN):
        a = ep(t, cues[k], 0.5)
        if a <= 0:
            continue
        x = 330 + k * 340
        barra_juros(c, x, base, 100, a, esc=2.4, w=110, simples=True)
        barra_juros(c, x + 130, base, jc, a, esc=2.4, w=110)
        text(c, f"mês {k + 1}", x + 120, base + 44, 28, "black", GRAY, a)
        if k == 0:
            selo(c, x + 120, 330, a, "EMPATE", GRAY, -4, 26)
        else:
            pill(c, f"+ {dif[k]}", x + 185, 300, AMBER, size=26, a=a, anchor="center")
    a0 = ep(t, C["08.a"], 0.5)
    if a0 > 0:
        rrect(c, 330, 790, 26, 26, 6, BLUE, a0 * 0.85)
        text(c, "simples", 370, 812, 24, "black", BLUE, a0, align="left")
        rrect(c, 520, 790, 26, 26, 6, GREEN, a0 * 0.85)
        text(c, "compostos", 560, 812, 24, "black", GREEN, a0, align="left")
    ac = ep(t, C["08.c"] + 2.4, 0.5)
    if ac > 0:
        bola(c, 1680, 300, 46, ac, rot=t)
        text(c, "bola de neve", 1680, 380, 22, "black", BLUE, ac)


# ======================================================================
# bloco d — a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head_seq(c, t, C, [("09", "PULANDO A TABELA", "CADA MÊS: × 1,1", PURPLE),
                       ("10", "A FÓRMULA DO MONTANTE", "T MULTIPLICAÇÕES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        vals = ["1.000", "1.100", "1.210"]
        for k, v in enumerate(vals):
            a = ep(t, C["09.b"] + k * 1.6, 0.4) if k else ep(t, C["09.a"], 0.4)
            x = 420 + k * 540
            if a <= 0:
                continue
            rrect(c, x - 150, 330, 300, 120, 22, "#FFFFFF", a, shadow=True)
            fmid(c, v, x, 390, 52, "black", INK, a)
            if k:
                arrow(c, x - 400, 390, x - 170, 390, PURPLE, a, 5, 18)
                text(c, "× 1,1", x - 285, 360, 34, "black", PURPLE, a)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            rrect(c, 460, 560, 1000, 150, 28, mix("#FFFFFF", PURPLE, 0.10), acc)
            linha(c, [("cada período: ", INK), ("× (1 + ", PURPLE), ("i", PURPLE), (")", PURPLE)], W / 2, 610, 56, acc)
            text(c, "pense em FATORES, não em porcentagens somadas", W / 2, 690, 28, "black", INK2, acc)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        linha(c, [("C", BLUE), (" · (1 + i) · (1 + i) · ... · (1 + i)", INK)], W / 2, 300, 50, aa)
        wq = ftext_w("C · (1 + i) · (1 + i) · ... · (1 + i)", "black", 50)
        x0 = W / 2 - wq / 2 + ftext_w("C · ", "black", 50)
        x1 = W / 2 + wq / 2
        line(c, x0, 350, x1, 350, AMBER, aa, 4)
        line(c, x0, 340, x0, 350, AMBER, aa, 4); line(c, x1, 340, x1, 350, AMBER, aa, 4)
        text(c, "t vezes", (x0 + x1) / 2, 395, 30, "black", AMBER, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 450, 800, 150, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
        xa, xb, w = formula(c, W / 2, 525, 84, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        xa, xb, w = formula(c, W / 2, 525, 84, 0)
        ex = W / 2 + w / 2 - 14
        arrow(c, 1420, 520, ex + 16, 505, AMBER, acc, 5, 16)
        text(c, "EXPOENTE", 1430, 512, 30, "black", AMBER, acc, align="left")
        text(c, "quantas vezes o", 1430, 552, 22, "bold", INK2, acc, align="left")
        text(c, "fator foi aplicado", 1430, 580, 22, "bold", INK2, acc, align="left")
        pill(c, "3 anos  =  3 multiplicações  =  expoente 3", W / 2, 740, AMBER, size=30, a=ep(t, C["10.c"] + 2.0, 0.4),
             anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        xa, xb, w = formula(c, W / 2, 525, 84, 0)
        line(c, xa, 610, W / 2 + w / 2, 610, PURPLE, ad, 5)
        text(c, "FATOR DE CAPITALIZAÇÃO", (xa + W / 2 + w / 2) / 2, 650, 26, "black", PURPLE, ad)


# ======================================================================
# bloco e — os juros por diferença
# ======================================================================

def b_jdif(c, t, C, B):
    head(c, t, B["start"], "E SÓ OS JUROS?", "POR DIFERENÇA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        selo(c, W / 2, 330, aa, "NÃO EXISTE FÓRMULA DIRETA DOS JUROS", AMBER, -2, 34)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        text(c, "1º  calcule o montante", W / 2, 470, 34, "black", INK2, ab)
        rrect(c, 610, 540, 700, 150, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
        linha(c, [("J", GREEN), (" = ", INK), ("M", RED), (" − ", INK), ("C", BLUE)], W / 2, 615, 90, ab)
        text(c, "2º  tire o capital", W / 2, 760, 34, "black", INK2, ab)


# ======================================================================
# bloco f — o exemplo do material
# ======================================================================

def b_exemplo(c, t, C, B):
    head_seq(c, t, C, [("12", "EXEMPLO COMPLETO", "O FATOR DE UM MÊS", PURPLE), ("13", "PASSO A PASSO", "1,02³", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    etiqueta(c, "C", "R$ 5.000,00", 560, 300, aa)
    etiqueta(c, "i", "2% a.m.", 960, 300, ep(t, C["12.a"] + 1.4, 0.4))
    etiqueta(c, "t", "3 meses", 1360, 300, ep(t, C["12.a"] + 3.0, 0.4))
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("1 mês:  +2%  →  ", INK), ("× 1,02", PURPLE)], W / 2, 500, 60, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            fichas(c, 560, 650, [("1,02", PURPLE)] * 3, acc, 54, sep="·")
            linha(c, [("= 1,02³", AMBER)], 1380, 650, 60, acc)
        return
    linha(c, [("1,02 · 1,02 = ", INK), ("1,0404", PURPLE)], 620, 470, 46, ep(t, C["13.a"], 0.4))
    linha(c, [("1,0404 · 1,02 = ", INK), ("1,061208", PURPLE)], 620, 550, 46, ep(t, C["13.b"], 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        linha(c, [("M = 5.000 · 1,061208 = ", INK), ("R$ 5.306,04", RED)], 620, 640, 40, acc)
        linha(c, [("J = 5.306,04 − 5.000 = ", INK), ("R$ 306,04", GREEN)], 620, 720, 40, ep(t, C["13.c"] + 3.6, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 1240, 450, 430, 300, 24, "#FFFFFF", ad, shadow=True)
        text(c, "em juros simples", 1455, 500, 26, "black", BLUE, ad)
        fmid(c, "J = R$ 300,00", 1455, 560, 40, "black", BLUE, ad)
        selo(c, 1455, 660, ep(t, C["13.d"] + 2.2, 0.4), "+ R$ 6,04", AMBER, -4, 36)
        text(c, "juros sobre os juros", 1455, 730, 22, "black", AMBER, ep(t, C["13.d"] + 2.2, 0.4))


# ======================================================================
# atalho — multiplicar o fator sem calculadora
# ======================================================================

def b_atalho(c, t, C, B):
    head(c, t, B["start"], "SEM CALCULADORA", "MULTIPLICAR O FATOR", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 240, 1320, 150, "ATALHO", ["× 1,1  =  o número  +  o décimo dele"], aa, 40)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("1,21", INK), ("  +  ", GRAY), ("0,121", GREEN), ("  =  ", GRAY), ("1,331", PURPLE)], W / 2, 480, 64, ab)
        text(c, "(1,1² · 1,1 = 1,1³)", W / 2, 550, 28, "bold", GRAY, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.atalho(c, 300, 620, 1320, 150, "E O × 1,02?", ["o número  +  2% dele:  5.000 + 100 = 5.100"], acc, 36)


# ======================================================================
# bloco g — taxa e tempo no mesmo período
# ======================================================================

def b_unidade(c, t, C, B):
    head(c, t, B["start"], "TAXA AO ANO, PRAZO EM MESES?", "O MESMO PERÍODO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        regra(c, "i  e  t  no MESMO período (como nos juros simples)", W / 2, 320, aa, 38)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("12% a.a.", PURPLE), ("  ÷ 12  →  ", INK), ("1% a.m.", RED)], W / 2, 490, 60, ab)
        strike(c, 560, 490, 1360, 470, ab, RED, ep(t, C["15.b"] + 0.8, 0.5))
        selo(c, W / 2, 590, ep(t, C["15.b"] + 1.0, 0.4), "EM COMPOSTOS, NÃO FUNCIONA", AMBER, -3, 34)
        pill(c, "série própria: TAXAS EQUIVALENTES", W / 2, 680, PURPLE, size=28, a=ep(t, C["15.b"] + 3.0, 0.4),
             anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        conferido(c, "nas questões deste assunto, a taxa já vem no período certo", 420, 790, acc, True, 30)


# ======================================================================
# bloco h — taxas diferentes em sequência
# ======================================================================

def b_sequencia(c, t, C, B):
    head(c, t, B["start"], "TAXAS DIFERENTES?", "MULTIPLIQUE OS FATORES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        regra(c, "um fator por período  ·  multiplique todos", W / 2, 300, aa, 38)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, (p_, f_) in enumerate((("+5%", "1,05"), ("+10%", "1,10"))):
            x = 560 + k * 420
            text(c, p_, x, 420, 34, "black", AMBER, ab)
            rrect(c, x - 120, 450, 240, 110, 20, mix("#FFFFFF", PURPLE, 0.12), ab)
            fmid(c, f_, x, 505, 54, "black", PURPLE, ab)
        text_mid(c, "·", 770, 505, 60, "black", INK, ab)
        linha(c, [("=  1,155", PURPLE)], 1340, 505, 60, ep(t, C["16.b"] + 2.4, 0.4))
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("aumento de ", INK), ("15,5%", GREEN)], 800, 680, 56, acc)
        fmid(c, "15%", 1300, 680, 56, "black", RED, acc)
        strike(c, 1230, 690, 1370, 670, acc, RED, ep(t, C["16.c"] + 0.6, 0.4))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "FATOR, POTÊNCIA, DIFERENÇA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    etiqueta(c, "C", "R$ 2.000,00", 560, 300, aa)
    etiqueta(c, "i", "10% a.m.", 960, 300, aa)
    etiqueta(c, "t", "2 meses", 1360, 300, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("M = ?", RED), ("     ", INK), ("J = ?", GREEN)], W / 2, 450, 56, ab * (1 - ep(t, C["18"], 0.3)))
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 600)
    if t < C["18"]:
        return
    linha(c, [("fator 1,1  →  1,1² = ", INK), ("1,21", PURPLE)], W / 2, 450, 46, ep(t, C["18.a"], 0.4))
    linha(c, [("M = 2.000 · 1,21 = ", INK), ("R$ 2.420,00", RED)], W / 2, 540, 48, ep(t, C["18.b"], 0.4))
    linha(c, [("J = 2.420 − 2.000 = ", INK), ("R$ 420,00", GREEN)], W / 2, 630, 48, ep(t, C["18.c"], 0.4))
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        linha(c, [("em simples: R$ 400,00", BLUE), ("   ·   ", GRAY), ("+ R$ 20,00 de juros sobre juros", AMBER)], W / 2,
              735, 32, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Juros compostos: juros sobre juros, como bola de neve.",
          "Cada período multiplica o saldo por 1 + i.",
          "Os juros saem por diferença: montante menos capital."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Usar C · (1 + i · t) no regime composto: R$ 5.300,00 em vez de R$ 5.306,04",
          "você acabou de aprender essa fórmula nos juros simples", "“compostos” no enunciado pede POTÊNCIA"),
         ("Somar as taxas: 10% por 2 anos = 20%", "10 + 10 é mesmo 20",
          "1,1² = 1,21 → 21% em 2 anos"),
         ("Responder o montante quando pedem os juros (R$ 5.306,04 × R$ 306,04)",
          "a fórmula entrega o montante, e ele está nas alternativas", "“quanto rendeu?” → J = M − C"),
         ("Contar um período a mais: 3 anos virando expoente 4", "do ano 0 ao ano 3 há quatro números",
          "o expoente conta MULTIPLICAÇÕES: 3 anos, expoente 3")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


# ======================================================================
# questão 1 (eu faço) e questão 5 (você faz)
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


ALTS1 = [("A", "R$ 3.310,00", "só os juros", RED), ("B", "R$ 13.000,00", "montante simples", RED),
         ("C", "R$ 13.310,00", "", GREEN), ("D", "R$ 14.000,00", "simples de 4 anos", RED),
         ("E", "R$ 14.641,00", "expoente 4", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "MONTANTE EM TRÊS ANOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Uma pessoa aplicou R$ 10.000,00 a juros compostos de 10% ao ano. Sem novos depósitos nem "
                           "retiradas, o saldo ao final de 3 anos será de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["25.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        linha(c, [("1 ano: +10%  →  ", INK), ("× 1,1", PURPLE)], 540, y0 + 55, 32, ep(t, C["25"], 0.4))
        linha(c, [("1,1 → 1,21 → ", INK), ("1,331", PURPLE), ("  (1,1³)", AMBER)], 540, y0 + 125, 32, ep(t, C["25.a"], 0.4))
        linha(c, [("M = 10.000 · 1,331 = ", INK), ("R$ 13.310,00", RED)], 540, y0 + 195, 30, ep(t, C["25.b"], 0.4))
        pill(c, "pede o SALDO = montante", 540, y0 + 265, RED, size=24, a=ep(t, C["25.c"], 0.4), anchor="center")


ALTS5 = [("A", "perda de 1%", "", GREEN), ("B", "ganho de 5%", "somou as taxas", RED),
         ("C", "ganho de 1%", "errou o sinal", RED), ("D", "ganho de 30%", "só os ganhos", RED),
         ("E", "resultado nulo", "“quase se anulam”", RED)]


def b_q5(c, t, C, B):
    head_seq(c, t, C, [("27", "QUESTÃO 5 · VOCÊ FAZ", "TAXAS EM SEQUÊNCIA", GREEN),
                       ("28", "CONFERINDO", "UM FATOR POR MÊS", GREEN), ("29", "AS ARMADILHAS", "QUESTÃO 5", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Um investimento de risco rendeu 10% no primeiro mês e 20% no segundo, mas teve perda de 25% "
                           "no terceiro. Em relação ao valor investido no início, ao final do terceiro mês o investidor "
                           "teve", INK)], a0, 240, 27)
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 44, C["28.ok"], "A", cues_in, cues_x, gap=34)
    if t < C["28"]:
        ab = ep(t, C["27.b"], 0.4)
        if ab > 0:
            pill(c, "escreva o FATOR de cada mês", 540, yend + 60, GREEN, size=26, a=ab, anchor="center")
        pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 200)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["28"], 0.4))
    aa = ep(t, C["28.a"], 0.4)
    if aa > 0:
        fichas(c, 230, y0 + 70, [("1,10", GREEN), ("1,20", GREEN), ("0,75", RED)], aa, 36, sep="·")
    linha(c, [("1,10 · 1,20 = ", INK), ("1,32", PURPLE), ("  (já conhece)", GRAY)], 540, y0 + 160, 30, ep(t, C["28.b"], 0.4))
    linha(c, [("1,32 · 0,75 = ", INK), ("0,99", PURPLE)], 540, y0 + 225, 34, ep(t, C["28.c"], 0.4))
    pill(c, "99% do início → PERDA de 1%", 540, y0 + 290, GREEN, size=24, a=ep(t, C["28.d"], 0.4), anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SIMPLES × COMPOSTOS", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        text(c, "compostos SEMPRE rendem mais que simples?", W / 2, 320, 56, "black", INK, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 470, ab, "ERRADO!", RED, -5, 70)
        text(c, "existe um prazo em que os SIMPLES ganham", W / 2, 610, 44, "black", BLUE, ep(t, C["31.b"] + 1.0, 0.4))
    pill(c, "ep. 2 · reta e curva", W / 2, 790, PURPLE, size=30, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já somou taxas que deviam ser multiplicadas?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              tabela=b_tabela, diferenca=b_diferenca, formula=b_formula, jdif=b_jdif, exemplo=b_exemplo,
              atalho=b_atalho, unidade=b_unidade, sequencia=b_sequencia, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q1=b_q1, q5=b_q5, ponte=b_ponte, cta=b_cta)
