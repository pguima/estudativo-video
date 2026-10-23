"""Visual — Equação do 2º grau sem Bhaskara: Soma e Produto (Relações de Girard), episódio único (iniciantes, tema claro).
Quadro branco digital: cartão branco, contas construídas linha a linha, cada uma quando é dita.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha/sinais · verde = atalho/resposta · vermelho = erro.
Letras da forma geral sempre com a mesma cor: a = azul, b = laranja, c = verde-azulado.
Reaproveita a série 016 (Po-Shen Loh: fbox, fmid, regra, linhas, reta, gangorra, bhaskara_formula) e a 015/014/010 por ela.
Símbolos usados (², ₁, ₂, ×, ·, −, ≠, ✓, →) existem na Inter: nada cai em fonte reserva.
Peças próprias deste episódio:
- mrow(): linha matemática com frações empilhadas (−b sobre a) e cores por pedaço.
- tabela(): a tabela Números | Soma | Produto, linha por linha, com ✓/✗ e destaque da linha certa.
- contagem(): contagem regressiva de 10 s do desafio (sincronizada com a pausa do áudio).
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ROOT = Path(__file__).resolve().parents[3]          # canais/enem


def _load(nome, rel):
    sp = importlib.util.spec_from_file_location(nome, _ROOT / rel)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    return mod


V16 = _load("v016_ep1", "016_enem_matematica_po_shen_loh/ep1_metodo_po_shen_loh/roteiro/visual.py")
motor.set_theme("claro")

ftext, fmid, ftext_w, fbox, regra = V16.ftext, V16.fmid, V16.ftext_w, V16.fbox, V16.regra
pause_timer, which, para, frame, head_seq, boxed = V16.pause_timer, V16.which, V16.para, V16.frame, V16.head_seq, V16.boxed
linhas = V16.linhas

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_soma_produto_ep1.mp4"
CARD_R = (140, 150, 1640, 690)

CA, CB, CC = BLUE, "#F97316", "#0E9F9A"     # cores fixas das letras a, b, c


# ======================================================================
# peças
# ======================================================================

def _w(it, size):
    if it[0] == "f":
        return max(ftext_w(it[1], "black", size * 0.82), ftext_w(it[2], "black", size * 0.82)) + 22
    return ftext_w(it[1], "black", size)


def mrow(c, items, x, cy, size, a=1.0, align="left", col=None):
    """items: ("t", texto[, cor]) ou ("f", numerador, denominador[, cor]) — fração empilhada"""
    if a <= 0:
        return 0
    col = col or INK
    total = sum(_w(it, size) for it in items)
    xx = x - total / 2 if align == "center" else x - total if align == "right" else x
    for it in items:
        w = _w(it, size)
        if it[0] == "f":
            k = it[3] if len(it) > 3 else col
            s2 = size * 0.82
            fmid(c, it[1], xx + w / 2, cy - s2 * 0.62, s2, "black", k, a)
            line(c, xx + 4, cy, xx + w - 4, cy, k, a, max(3, size * 0.07), cap_round=False)
            fmid(c, it[2], xx + w / 2, cy + s2 * 0.66, s2, "black", k, a)
        else:
            fmid(c, it[1], xx, cy, size, "black", it[2] if len(it) > 2 else col, a, align="left")
        xx += w
    return total


def build(c, t, t0, parts, x, cy, size, col=None, step=0.35, align="center"):
    """equação montada pedaço por pedaço (parts = [(texto, cor)])"""
    total = sum(ftext_w(s, "black", size) for s, _ in parts)
    xx = x - total / 2 if align == "center" else x
    for k, (s, cc) in enumerate(parts):
        a, d = rise(t, t0 + k * step, 0.4)
        fmid(c, s, xx, cy + d * 0.6, size, "black", cc or col or INK, a, align="left")
        xx += ftext_w(s, "black", size)


def parts_x(parts, x, size, align="center"):
    """centro x de cada pedaço (para setas e destaques)"""
    total = sum(ftext_w(s, "black", size) for s, _ in parts)
    xx = x - total / 2 if align == "center" else x
    out = []
    for s, _ in parts:
        w = ftext_w(s, "black", size)
        out.append((xx, xx + w))
        xx += w
    return out


def hl_box(c, x0, x1, cy, size, col, a, pad=10):
    if a <= 0:
        return
    h = size * 1.35
    rrect(c, x0 - pad, cy - h / 2, x1 - x0 + 2 * pad, h, 14, col, 0.16 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - pad, cy - h / 2, x1 - x0 + 2 * pad, h), 14, 14),
                paint(col, a, stroke=3))


def tabela(c, t, C, x, y, widths, head_cue, rows, size=38, rh=84, heads=("NÚMEROS", "SOMA", "PRODUTO")):
    """rows = [dict(cells=[(cue, texto)], marks=[(cue, ok, col)], hl=cue|None)]"""
    ah = ep(t, C[head_cue], 0.5)
    if ah <= 0:
        return
    tw = sum(widths)
    hh = 64
    rrect(c, x, y, tw, hh, 16, INK, ah, shadow=True)
    xs = [x + sum(widths[:j]) for j in range(len(widths))]
    for j, hd in enumerate(heads):
        text_mid(c, hd, xs[j] + widths[j] / 2, y + hh / 2, 24, "black", "#FFFFFF", ah, tracking=2)
    for k, row in enumerate(rows):
        yy = y + hh + 10 + k * rh
        a_row = max(ep(t, C[cue], 0.4) for cue, _ in row["cells"])
        if row.get("hl"):
            ahl = ep(t, C[row["hl"]], 0.5)
            if ahl > 0:
                rrect(c, x - 10, yy + 4, tw + 20, rh - 8, 18, GREEN, 0.14 * ahl)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, yy + 4, tw + 20, rh - 8), 18, 18),
                            paint(GREEN, ahl, stroke=4))
        if a_row > 0:
            line(c, x, yy + rh, x + tw, yy + rh, LINE, a_row * ah, 2)
        tint = {}
        for cue, ok, j in row.get("marks", []):
            am = ep(t, C[cue], 0.4)
            tint[j] = (GREEN if ok else RED, am)
            check_icon(c, xs[j] + widths[j] - 34, yy + rh / 2, 20, am, GREEN if ok else RED, "check" if ok else "x")
        for j, (cue, s) in enumerate(row["cells"]):
            a, d = rise(t, C[cue])
            col = INK
            if j in tint:
                col = mix(INK, tint[j][0], tint[j][1])
            fmid(c, s, xs[j] + widths[j] / 2 - (14 if j in tint and tint[j][1] > 0 else 0), yy + rh / 2 + d * 0.5, size,
                 "black", col, a)


def contagem(c, t, t0, cx, cy, R=130, dur=10.0):
    """contagem regressiva grande: 10, 9, ..., 1 com anel que esvazia"""
    a = ep(t, t0, 0.3) * (1 - prog(t, t0 + dur, 0.35))
    if a <= 0:
        return
    el = clamp((t - t0) / dur)
    rem = dur * (1 - el)
    n = max(1, math.ceil(rem - 1e-6))
    c.drawCircle(cx, cy, R + 22, paint(AMBER, a * 0.14))
    c.drawCircle(cx, cy, R, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, R, paint(LIGHT, a, stroke=16))
    rect = skia.Rect.MakeLTRB(cx - R, cy - R, cx + R, cy + R)
    c.drawArc(rect, -90, 360 * (1 - el), False, paint(AMBER if n > 3 else RED, a, stroke=16, cap_round=True))
    frac_ = (rem % 1.0)
    pulse = 1 + 0.12 * ease_out(clamp((frac_ - 0.75) / 0.25)) if rem < dur - 0.05 else 1
    c.save(); c.translate(cx, cy); c.scale(pulse, pulse)
    text_mid(c, str(n), 0, 0, 140, "black", INK if n > 3 else RED, a)
    c.restore()
    text(c, "segundos", cx, cy + R + 56, 28, "black", GRAY, a)


def cronometro(c, cx, cy, r, a, ang=0.0):
    if a <= 0:
        return
    rrect(c, cx - 14, cy - r - 26, 28, 18, 5, INK, a)
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=7))
    for k in range(12):
        th = math.radians(k * 30)
        line(c, cx + math.sin(th) * r * 0.78, cy - math.cos(th) * r * 0.78, cx + math.sin(th) * r * 0.9,
             cy - math.cos(th) * r * 0.9, GRAY, a, 3)
    th = math.radians(ang)
    line(c, cx, cy, cx + math.sin(th) * r * 0.7, cy - math.cos(th) * r * 0.7, RED, a, 5)
    c.drawCircle(cx, cy, 7, paint(INK, a))


EQ = [("x²", None), (" − 5", None), ("x", None), (" + 6", None), (" = 0", None)]


# ======================================================================
# CENA 1 — introdução
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÃO DO 2º GRAU SEM BHASKARA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "fórmula de Bhaskara", 520, 290, 30, "black", GRAY, aa)
        V16.bhaskara_formula(c, 520, 420, aa, 44, GRAY)
        ax = ep(t, C["01.a"] + 1.6, 0.5)
        line(c, 330, 500, 720, 340, RED, ax, 8, progress=ax)
        pill(c, "SEM ela!", 520, 580, RED, size=30, a=ax, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["01.b"], 0.5)
    pill(c, "às vezes, só OLHANDO para os números", 520, 720, GREEN, size=28, a=ab, anchor="center", bounds=(0, 1920))
    if t >= C["01.c"]:
        build(c, t, C["01.c"], EQ, 1300, 340, 76)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        fmid(c, "x = ?    e    x = ?", 1300, 500, 50, "black", GRAY, ad)
        cronometro(c, 1300, 680, 82, ad, 360 * prog(t, C["01.d"], 3.0))
        text(c, "em segundos", 1300, 815, 30, "black", GREEN, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    text(c, "achar as raízes usando só DUAS operações:", W / 2, 270, 46, "black", INK, aa)
    for cue, x, sym, nome, col in (("02.b", 680, "+", "SOMA", BLUE), ("02.c", 1240, "×", "MULTIPLICAÇÃO", PURPLE)):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        rrect(c, x - 230, 340 + d, 460, 280, 30, mix("#FFFFFF", col, 0.10), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 230, 340 + d, 460, 280), 30, 30), paint(col, a, stroke=4))
        text_mid(c, sym, x, 440 + d, 130, "black", col, a)
        text_mid(c, nome, x, 565 + d, 40, "black", col, a)
    ad = ep(t, C["02.d"], 0.5)
    check_icon(c, 640, 735, 26, ad, GREEN)
    text_mid(c, "e entendendo POR QUE funciona", 990, 735, 40, "black", GREEN, ad)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE RÁPIDO", "EQUAÇÃO DO 2º GRAU E RAIZ", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    boxed(c, 220, 280, 860, 160, BLUE, aa, 0.07)
    text(c, "EQUAÇÃO DO 2º GRAU", 255, 325, 22, "black", BLUE, aa, align="left", tracking=2)
    text(c, "tem x², e nenhuma potência maior", 255, 393, 40, "black", INK, aa, align="left")
    fbox(c, "x² − 5x + 6 = 0", 1400, 360, 52, aa, INK)
    ab = ep(t, C["03.b"], 0.5)
    boxed(c, 220, 530, 860, 160, BLUE, ab, 0.07)
    text(c, "RAIZ", 255, 575, 22, "black", BLUE, ab, align="left", tracking=2)
    text(c, "o número que, no lugar do x, ZERA a conta", 255, 643, 36, "black", INK, ab, align="left")
    if ab > 0:
        fmid(c, "x = ?   →   conta = 0", 1400, 610, 44, "black", BLUE, ab)


# ======================================================================
# CENA 2 — entendendo a lógica
# ======================================================================

def caixinha(c, x, y, s, a, col, size=56):
    if a <= 0:
        return
    rrect(c, x - 60, y - 52, 120, 104, 18, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 60, y - 52, 120, 104), 18, 18), paint(col, a, stroke=4))
    fmid(c, s, x, y, size, "black", col, a)


def b_logica(c, t, C, B):
    frame(c, t, B["start"], "ENTENDENDO A LÓGICA", "DOIS NÚMEROS ESCONDIDOS", BLUE)
    size = 72
    px = parts_x(EQ, W / 2, size)
    if t >= C["04.a"]:
        build(c, t, C["04.a"], EQ, W / 2, 255, size)
    ad = ep(t, C["04.d"], 0.5)
    hl_box(c, px[1][0] + ftext_w(" ", "black", size), px[1][1] - 4, 255, size, AMBER, ad, pad=5)
    for cue, y, op, res, nome, col in (("04.b", 440, "+", "5", "SOMA", BLUE), ("04.c", 600, "×", "6", "PRODUTO", PURPLE)):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        pill(c, nome, 330, y + d, col, size=28, a=a, anchor="center", bounds=(0, 1920))
        caixinha(c, 560, y + d, "?", a, col)
        fmid(c, op, 680, y + d, 60, "black", INK, a)
        caixinha(c, 800, y + d, "?", a, col)
        fmid(c, "=", 920, y + d, 60, "black", INK, a)
        fmid(c, res, 1010, y + d, 72, "black", col, a)
    if ad > 0:
        arrow(c, (px[1][0] + px[1][1]) / 2 + 10, 305, 1000, 395, AMBER, ad, 4, 16, progress=ad)
        boxed(c, 1130, 400, 520, 150, AMBER, ad, 0.08)
        fmid(c, "na equação:  −5", 1390, 445, 36, "black", INK, ad)
        fmid(c, "na soma:  +5", 1390, 505, 36, "black", AMBER, ad)
    ae = ep(t, C["04.e"], 0.5)
    pill(c, "por que o sinal troca? já, já!", 1390, 630, AMBER, size=26, a=ae, anchor="center", bounds=(0, 1920))


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "TABELA DE PARES", "SOMA 5 · PRODUTO 6", BLUE)
    a0 = ep(t, C["05.t"], 0.5)
    pill(c, "soma = 5", 300, 230, BLUE, size=30, a=a0, bounds=(0, 1920))
    pill(c, "produto = 6", 520, 230, PURPLE, size=30, a=a0, bounds=(0, 1920))
    pill(c, "ATALHO: comece pelo PRODUTO", 1230, 230, GREEN, size=28, a=ep(t, C["05.a"], 0.5), bounds=(0, 1920))
    rows = [dict(cells=[("05.b", "1 e 6"), ("05.c", "1 + 6 = 7"), ("05.d", "1 × 6 = 6")],
                 marks=[("05.e", False, 1), ("05.e", True, 2)]),
            dict(cells=[("05.f", "2 e 3"), ("05.g", "2 + 3 = 5"), ("05.h", "2 × 3 = 6")],
                 marks=[("05.i", True, 1), ("05.i", True, 2)], hl="05.j")]
    tabela(c, t, C, 330, 300, (380, 440, 440), "05.t", rows, size=46, rh=110)
    ae = ep(t, C["05.e"], 0.4) * (1 - ep(t, C["05.f"], 0.3))
    pill(c, "7 ≠ 5: não serve", 1200, 625, RED, size=26, a=ae, anchor="center", bounds=(0, 1920))
    fbox(c, "os números: 2 e 3", W / 2, 690, 48, ep(t, C["05.j"], 0.5), GREEN)


def b_porque(c, t, C, B):
    frame(c, t, B["start"], "POR QUE 2 E 3?", "TESTANDO NA EQUAÇÃO", BLUE)
    fmid(c, "x² − 5x + 6 = 0", W / 2, 225, 44, "black", GRAY, ep(t, C["06.t"], 0.5))
    pill(c, "x = 2", 560, 310, AMBER, size=30, a=ep(t, C["06.a"], 0.4), anchor="center", bounds=(0, 1920))
    rows2 = [("06.a", "2² − 5 · 2 + 6", INK), ("06.b", "2² = 4", BLUE), ("06.c", "5 · 2 = 10", BLUE),
             ("06.d", "= 4 − 10 + 6", INK), ("06.e", "= −6 + 6 = 0  ✓", GREEN)]
    linhas(c, t, C, rows2, 560, 390, 42, 72, align="center")
    pill(c, "x = 3", 1360, 310, AMBER, size=30, a=ep(t, C["06.f"], 0.4), anchor="center", bounds=(0, 1920))
    rows3 = [("06.f", "3² − 5 · 3 + 6", INK), ("06.f", "3² = 9   ·   5 · 3 = 15", BLUE), ("06.g", "= 9 − 15 + 6", INK),
             ("06.g", "= 0  ✓", GREEN)]
    for k, (cue, s, col) in enumerate(rows3):
        a, d = rise(t, C[cue] + (1.0 if k == 1 else 0) + (1.2 if k == 3 else 0))
        fmid(c, s, 1360, 390 + k * 72 + d, 42, "black", col, a)
    line(c, W / 2, 300, W / 2, 720, LINE, ep(t, C["06.f"], 0.4), 3)
    fbox(c, "2 e 3 zeram a conta: são raízes!", W / 2, 775, 40, ep(t, C["06.h"], 0.5), GREEN)


FAT = [("(", None), ("x", None), (" − 2", None), (")", None), (" · ", None), ("(", None), ("x", None), (" − 3", None),
       (")", None), (" = 0", None)]


def b_fatoracao(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head_seq(c, t, C, [("07", "FATORAÇÃO", "MULTIPLICANDO OS PARÊNTESES", PURPLE),
                       ("08", "UMA MULTIPLICAÇÃO QUE DÁ ZERO", "AS SOLUÇÕES", GREEN)])
    card(c, *CARD_R)
    size = 70
    a0 = ep(t, C["07.a"], 0.5)
    fmid(c, "".join(s for s, _ in FAT), W / 2, 265, size, "black", INK, a0)
    px = parts_x(FAT, W / 2, size)
    cx = [(p[0] + p[1]) / 2 for p in px]
    # cada termo que entra na multiplicação: x(1), −2(2), x(6), −3(7)
    term = {1: cx[1], 2: (px[2][0] + 30 + px[2][1]) / 2, 6: cx[6], 7: (px[7][0] + 30 + px[7][1]) / 2}
    if sid == "07":
        steps = [("07.b", 1, 6, BLUE, "x · x = x²"), ("07.c", 1, 7, CB, "x · (−3) = −3x"),
                 ("07.d", 2, 6, CB, "(−2) · x = −2x"), ("07.f", 2, 7, CC, "(−2) · (−3) = +6")]
        for k, (cue, i, j, col, s) in enumerate(steps):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            # arco ligando os dois termos multiplicados
            nxt = steps[k + 1][0] if k + 1 < len(steps) else None
            act = a * (1 - (ep(t, C[nxt], 0.3) if nxt else 0))
            if act > 0:
                p = skia.Path()
                h = 50 + 18 * k
                p.moveTo(term[i], 215); p.cubicTo(term[i], 215 - h, term[j], 215 - h, term[j], 215)
                c.drawPath(p, paint(col, act, stroke=5, cap_round=True))
            y = 380 + k * 80 + d
            fmid(c, s, 560, y, 44, "black", col, a, align="center")
        ae = ep(t, C["07.e"], 0.5)
        if ae > 0:
            boxed(c, 1060, 455, 600, 110, CB, ae, 0.08)
            fmid(c, "−3x − 2x = −5x", 1360, 510, 46, "black", CB, ae)
        fbox(c, "x² − 5x + 6 = 0  ✓", 1360, 690, 50, ep(t, C["07.g"], 0.5), GREEN)
        pill(c, "voltou a nossa equação!", 1360, 790, GREEN, size=24, a=ep(t, C["07.g"] + 0.6, 0.4), anchor="center",
             bounds=(0, 1920))
        return
    regra(c, "produto = 0  →  um dos fatores é 0", W / 2, 390, ep(t, C["08.a"], 0.5), 40, PURPLE)
    for cue, x, s1, s2 in (("08.b", 560, "x − 2 = 0", "x = 2"), ("08.c", 1360, "x − 3 = 0", "x = 3")):
        a, d = rise(t, C[cue])
        fmid(c, s1, x - 90, 520 + d, 46, "black", INK, a)
        fmid(c, "→", x + 70, 520 + d, 46, "black", GRAY, a)
        fmid(c, s2, x + 170, 520 + d, 46, "black", GREEN, a)
    fbox(c, "soluções:  x = 2   e   x = 3", W / 2, 640, 46, ep(t, C["08.d"], 0.5), GREEN)
    pill(c, "5 = 2 + 3  (SOMA)", 640, 775, BLUE, size=30, a=ep(t, C["08.e"], 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "6 = 2 × 3  (PRODUTO)", 1280, 775, PURPLE, size=30, a=ep(t, C["08.f"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# CENA 3 — regra geral, Girard e a demonstração do sinal
# ======================================================================

GERAL = [("a", CA), ("x²", INK), (" + ", INK), ("b", CB), ("x", INK), (" + ", INK), ("c", CC), (" = 0", INK)]


def b_geral(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "A REGRA GERAL", "A FORMA ax² + bx + c = 0", PURPLE),
                       ("10", "IDENTIFICANDO", "a, b E c NA NOSSA EQUAÇÃO", BLUE)])
    card(c, *CARD_R)
    if sid == "09":
        size = 96
        if t >= C["09.a"]:
            build(c, t, C["09.a"], GERAL, W / 2, 290, size, step=0.25)
        px = parts_x(GERAL, W / 2, size)
        for cue, i, s, col, y in (("09.b", 0, "acompanha o x²", CA, 440), ("09.c", 3, "acompanha o x, COM o sinal", CB, 520),
                                  ("09.d", 6, "o número sozinho", CC, 440)):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            xm = (px[i][0] + px[i][1]) / 2
            arrow(c, xm, 360, xm, y - 34, col, a, 4, 14, progress=a)
            pill(c, s, xm, y, col, size=26, a=a, anchor="center", bounds=(160, 1760))
        ae = ep(t, C["09.e"], 0.5)
        boxed(c, 300, 620, 1320, 170, AMBER, ae, 0.08)
        text_mid(c, "a ≠ 0", 470, 705, 64, "black", AMBER, ae)
        af = ep(t, C["09.f"], 0.5)
        if af > 0:
            x0 = 1060 - ftext_w("se a = 0:   0x² + bx + c", "black", 40) / 2
            fmid(c, "se a = 0:   0x² + bx + c", x0, 680, 40, "black", INK2, af, align="left")
            xs0 = x0 + ftext_w("se a = 0:   ", "black", 40)
            strike(c, xs0 - 6, 680, xs0 + ftext_w("0x²", "black", 40) + 6, 680, af, RED, progress=ep(t, C["09.f"] + 0.6, 0.4))
            text_mid(c, "o x² some: não é mais do 2º grau", 1060, 745, 30, "black", RED, ep(t, C["09.f"] + 1.0, 0.4))
        return
    size = 96
    parts = [("x²", INK), (" − 5", CB), ("x", INK), (" + 6", CC), (" = 0", INK)]
    a0 = ep(t, C["10.t"], 0.5)
    total = sum(ftext_w(s, "black", size) for s, _ in parts)
    x0 = W / 2 - total / 2 + 40
    aa = ep(t, C["10.a"], 0.5)
    fmid(c, "1", x0 - 18, 290, size * 0.8, "black", mix("#FFFFFF", CA, 0.6), aa, align="right")
    xx = x0
    for s, col in parts:
        fmid(c, s, xx, 290, size, "black", col, a0, align="left")
        xx += ftext_w(s, "black", size)
    px = parts_x(parts, x0, size, align="left")
    items = [("10.a", x0 - 50, "a = 1", CA, "um escondido"), ("10.b", (px[1][0] + px[1][1]) / 2 + 10, "b = −5", CB, "com o sinal!"),
             ("10.c", (px[3][0] + px[3][1]) / 2 + 10, "c = 6", CC, "sozinho")]
    for cue, x, s, col, sub in items:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        arrow(c, x, 365, x, 470, col, a, 4, 14, progress=a)
        fbox(c, s, x, 540, 50, a, col)
        text(c, sub, x, 640, 28, "black", col, a)


def b_girard(c, t, C, B):
    frame(c, t, B["start"], "RELAÇÕES DE GIRARD", "SOMA E PRODUTO DAS RAÍZES", PURPLE)
    a0 = ep(t, C["11.t"], 0.5)
    text(c, "Albert Girard · matemático francês, século XVII", W / 2, 215, 28, "bold", GRAY, a0)
    for cue, x, nome, frac_ in (("11.a", 560, "SOMA", ("−b", "a")), ("11.b", 1360, "PRODUTO", ("c", "a"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        rrect(c, x - 330, 260 + d, 660, 200, 26, mix("#FFFFFF", PURPLE, 0.10), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 330, 260 + d, 660, 200), 26, 26), paint(PURPLE, a, stroke=4))
        text(c, nome + " DAS RAÍZES", x, 305 + d, 22, "black", PURPLE, a, tracking=2)
        lhs = "x₁ + x₂ = " if nome == "SOMA" else "x₁ · x₂ = "
        num = [("t", "−", PURPLE), ("t", "b", CB)] if nome == "SOMA" else [("t", "c", CC)]
        w_l = ftext_w(lhs, "black", 58)
        w_f = max(ftext_w(frac_[0], "black", 58 * 0.82), ftext_w("a", "black", 58 * 0.82)) + 22
        x_l = x - (w_l + w_f) / 2
        fmid(c, lhs, x_l, 390 + d, 58, "black", INK, a, align="left")
        xf = x_l + w_l
        s2 = 58 * 0.82
        nw = ftext_w(frac_[0], "black", s2)
        xn = xf + w_f / 2 - nw / 2
        for _, s, col in num:
            fmid(c, s, xn, 390 + d - s2 * 0.62, s2, "black", col, a, align="left")
            xn += ftext_w(s, "black", s2)
        line(c, xf + 4, 390 + d, xf + w_f - 4, 390 + d, PURPLE, a, 4, cap_round=False)
        fmid(c, "a", xf + w_f / 2, 390 + d + s2 * 0.66, s2, "black", CA, a)
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        mrow(c, [("f", "−(−5)", "1"), ("t", " = ", INK), ("t", "5", GREEN)], 560, 590, 52, ac, align="center")
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        mrow(c, [("f", "6", "1"), ("t", " = ", INK), ("t", "6", GREEN)], 1360, 590, 52, ad, align="center")
    pill(c, "menos com menos dá mais", 560, 700, AMBER, size=24, a=ep(t, C["11.c"] + 2.2, 0.4), anchor="center",
         bounds=(0, 1920))
    fbox(c, "soma 5 ✓    produto 6 ✓", W / 2, 785, 36, ep(t, C["11.d"] + 1.6, 0.5), GREEN)


def b_prova(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "POR QUE O SINAL TROCA?", "A DEMONSTRAÇÃO", PURPLE),
                       ("13", "COMPARANDO COM ax² + bx + c", "PEDAÇO POR PEDAÇO", PURPLE)])
    card(c, *CARD_R)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        pill(c, "raízes:  r  e  s", 230, 225, BLUE, size=30, a=aa, bounds=(0, 1920))
        fmid(c, "a · (x − r) · (x − s) = 0", 1100, 225, 50, "black", INK, ep(t, C["12.b"], 0.5))
        rows = [("12.c", "x · x = x²", BLUE), ("12.d", "x · (−s) = −sx      (−r) · x = −rx", CB),
                ("12.e", "−sx − rx = −(r + s)x", CB), ("12.f", "(−r) · (−s) = +rs", CC)]
        linhas(c, t, C, rows, 240, 340, 42, 76)
        ag = ep(t, C["12.g"], 0.5)
        if ag > 0:
            boxed(c, 220, 660, 1480, 140, PURPLE, ag, 0.08)
            text(c, "MULTIPLICANDO TUDO PELO a", 250, 692, 20, "black", PURPLE, ag, align="left", tracking=2)
            fmid(c, "ax²  −  a(r + s)x  +  a·r·s  =  0", W / 2, 750, 54, "black", INK, ag)
        return
    # cena 13: alinhar com a forma geral
    cols = [560, 760, 1010, 1220, 1330, 1500, 1670]
    r1 = ["ax²", "+", "b", "x", "+", "c", "= 0"]
    r2 = ["ax²", "−", "a(r + s)", "x", "+", "a·r·s", "= 0"]
    a0 = ep(t, C["13.t"], 0.5)
    for k, (s1, s2) in enumerate(zip(r1, r2)):
        col1 = CB if k == 2 else CC if k == 5 else INK
        fmid(c, s1, cols[k] - 200, 235, 48, "black", col1, a0)
        fmid(c, s2, cols[k] - 200, 315, 48, "black", INK, a0)
    aa = ep(t, C["13.a"], 0.5)
    hl_box(c, cols[1] - 200 - 25, cols[2] - 200 + 105, 315, 48, CB, aa)
    hl_box(c, cols[2] - 200 - 20, cols[2] - 200 + 20, 235, 48, CB, aa)
    ae = ep(t, C["13.e"], 0.5)
    hl_box(c, cols[5] - 200 - 70, cols[5] - 200 + 70, 315, 48, CC, ae)
    hl_box(c, cols[5] - 200 - 20, cols[5] - 200 + 20, 235, 48, CC, ae)
    line(c, 160, 385, 1760, 385, LINE, a0, 2)
    rows = [("13.a", "b = −a(r + s)", CB), ("13.b", "dividindo os dois lados por −a", GRAY)]
    linhas(c, t, C, rows, 240, 450, 44, 76)
    acf = ep(t, C["13.c"], 0.5)
    if acf > 0:
        mrow(c, [("t", "r + s = ", INK), ("t", "−", PURPLE), ("f", "b", "a", PURPLE)], 240, 640, 58, acf)
        boxed(c, 210, 575, 470, 130, PURPLE, acf, 0.06)
    ad = ep(t, C["13.d"], 0.5)
    pill(c, "o menos já estava em (x − r)(x − s)!", 445, 775, AMBER, size=26, a=ad, anchor="center", bounds=(0, 1920))
    rows2 = [("13.e", "c = a·r·s", CC), ("13.f", "dividindo os dois lados por a", GRAY)]
    linhas(c, t, C, rows2, 1060, 450, 44, 76)
    af = ep(t, C["13.f"] + 0.8, 0.5)
    if af > 0:
        mrow(c, [("t", "r · s = ", INK), ("f", "c", "a", PURPLE)], 1060, 640, 58, af)
        boxed(c, 1030, 575, 400, 130, PURPLE, af, 0.06)


def b_armadilha(c, t, C, B):
    frame(c, t, B["start"], "ARMADILHA", "O SINAL DA SOMA", AMBER)
    fmid(c, "x² − 5x + 6 = 0", W / 2, 230, 48, "black", INK, ep(t, C["14.t"], 0.5))
    aa = ep(t, C["14.a"], 0.5)
    check_icon(c, 300, 340, 34, aa, RED, "x")
    fmid(c, "“a soma é −5”", 360, 340, 46, "black", RED, aa, align="left")
    strike(c, 355, 340, 360 + ftext_w("“a soma é −5”", "black", 46), 340, ep(t, C["14.c"], 0.4), RED,
           progress=ep(t, C["14.c"], 0.4))
    ab = ep(t, C["14.b"], 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 450, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, "o −5 está ali, à vista", 300, 525, 40, "bold", INK2, ab, align="left")
    ac = ep(t, C["14.c"], 0.5)
    check_icon(c, 300, 670, 34, ac, GREEN)
    if ac > 0:
        mrow(c, [("t", "soma = ", GREEN), ("f", "−b", "a", GREEN), ("t", " = ", GREEN), ("f", "−(−5)", "1", GREEN),
                 ("t", " = +5", GREEN)], 360, 670, 50, ac)


# ======================================================================
# CENA 4 — exemplos progressivos
# ======================================================================

def coef_row(c, t, C, cue, a_, b_, c_, x, y, size=40, hl_b=None):
    a, d = rise(t, C[cue])
    if a <= 0:
        return
    xx = x
    for lab, val, col in (("a", a_, CA), ("b", b_, CB), ("c", c_, CC)):
        s = f"{lab} = {val}"
        fmid(c, s, xx, y + d, size, "black", col, a, align="left")
        xx += ftext_w(s, "black", size) + 46


def girard_rows(c, t, C, cue_s, cue_p, s_num, a_, s_res, p_num, p_res, x, y, size=44, dy=110):
    a1 = ep(t, C[cue_s], 0.5)
    if a1 > 0:
        mrow(c, [("t", "soma = ", INK), ("f", s_num, a_), ("t", " = ", INK), ("t", s_res, GREEN)], x, y, size, a1)
    a2 = ep(t, C[cue_p], 0.5)
    if a2 > 0:
        mrow(c, [("t", "produto = ", INK), ("f", p_num, a_), ("t", " = ", INK), ("t", p_res, GREEN)], x, y + dy, size, a2)


def b_ex1(c, t, C, B):
    frame(c, t, B["start"], "EXEMPLO 1", "x² − 7x + 12 = 0", BLUE)
    fbox(c, "x² − 7x + 12 = 0", 520, 240, 48, ep(t, C["15.a"], 0.5), INK)
    coef_row(c, t, C, "15.b", "1", "−7", "12", 200, 345, 38)
    girard_rows(c, t, C, "15.c", "15.d", "−(−7)", "1", "7", "12", "12", 200, 470)
    rows = [dict(cells=[("15.e", "1 e 12"), ("15.e", "13")], marks=[("15.e", False, 1)]),
            dict(cells=[("15.f", "2 e 6"), ("15.f", "8")], marks=[("15.f", False, 1)]),
            dict(cells=[("15.g", "3 e 4"), ("15.g", "7")], marks=[("15.g", True, 1)], hl="15.h")]
    pill(c, "produto 12  →  qual par soma 7?", 1300, 240, PURPLE, size=26, a=ep(t, C["15.e"], 0.4), anchor="center",
         bounds=(0, 1920))
    tabela(c, t, C, 1000, 300, (330, 270), "15.e", rows, size=44, rh=96, heads=("PAR (PRODUTO 12)", "SOMA"))
    fbox(c, "raízes:  3  e  4", W / 2, 760, 48, ep(t, C["15.h"], 0.5), GREEN)


def b_ex2(c, t, C, B):
    sid = which(t, C, ["16", "17"])
    head_seq(c, t, C, [("16", "EXEMPLO 2", "x² + 5x + 6 = 0", BLUE), ("17", "A REGRA DOS SINAIS", "PRODUTO E SOMA", AMBER)])
    card(c, *CARD_R)
    if sid == "16":
        fbox(c, "x² + 5x + 6 = 0", W / 2, 240, 52, ep(t, C["16.a"], 0.5), INK)
        ab = ep(t, C["16.b"], 0.5)
        coef_row(c, t, C, "16.b", "1", "+5", "6", 300, 350, 40)
        pill(c, "b POSITIVO!", 1180, 350, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
        girard_rows(c, t, C, "16.c", "16.d", "−5", "1", "−5", "6", "6", 300, 470)
        ae = ep(t, C["16.e"], 0.5)
        if ae > 0:
            boxed(c, 1050, 440, 600, 200, AMBER, ae, 0.08)
            fmid(c, "soma NEGATIVA", 1350, 495, 38, "black", AMBER, ae)
            fmid(c, "produto POSITIVO", 1350, 580, 38, "black", AMBER, ae)
            fmid(c, "sinais = ?", W / 2, 770, 54, "black", INK, ep(t, C["16.e"] + 1.6, 0.4))
        return
    a0 = ep(t, C["17.t"], 0.5)
    boxed(c, 190, 190, 900, 610, AMBER, a0, 0.06)
    text(c, "OLHE PRIMEIRO O PRODUTO", 230, 235, 22, "black", AMBER, a0, align="left", tracking=2)
    regras = [("17.a", "produto +", "→  MESMO sinal", "(+ +)  ou  (− −)"),
              ("17.b", "  e soma −", "→  os dois NEGATIVOS", "(soma + → os dois positivos)"),
              ("17.c", "produto −", "→  sinais OPOSTOS", "(+ −)")]
    for k, (cue, s1, s2, s3) in enumerate(regras):
        a, d = rise(t, C[cue])
        y = 320 + k * 165 + d
        fmid(c, s1, 230, y, 40, "black", INK, a, align="left")
        fmid(c, s2, 470, y, 40, "black", AMBER if k != 1 else RED, a, align="left")
        fmid(c, s3, 470, y + 56, 28, "bold", GRAY, a, align="left")
    ad = ep(t, C["17.d"], 0.5)
    fmid(c, "produto 6 (+) · soma −5 (−)", 1420, 260, 32, "black", INK2, ad)
    fmid(c, "os dois NEGATIVOS", 1420, 320, 40, "black", RED, ad)
    fbox(c, "−2  e  −3", 1420, 430, 54, ep(t, C["17.e"], 0.5), INK)
    rows = [("17.f", "(−2) + (−3) = −5  ✓", GREEN), ("17.g", "(−2) × (−3) = +6  ✓", GREEN)]
    linhas(c, t, C, rows, 1420, 540, 38, 70, align="center")
    fbox(c, "x = −2   e   x = −3", 1420, 740, 42, ep(t, C["17.h"], 0.5), GREEN)


def b_ex3(c, t, C, B):
    frame(c, t, B["start"], "EXEMPLO 3", "QUANDO a ≠ 1", BLUE)
    fbox(c, "2x² − 10x + 12 = 0", 560, 240, 50, ep(t, C["18.a"], 0.5), INK)
    coef_row(c, t, C, "18.b", "2", "−10", "12", 200, 350, 38)
    pill(c, "divida por a = 2", 1000, 350, AMBER, size=24, a=ep(t, C["18.b"] + 0.4, 0.4), anchor="center", bounds=(0, 1920))
    girard_rows(c, t, C, "18.c", "18.d", "−(−10)", "2", "5", "12", "6", 200, 475, 42, 115)
    ae = ep(t, C["18.e"], 0.5)
    pill(c, "soma 5 e produto 6: já conhecemos!", 520, 690, BLUE, size=26, a=ae, anchor="center", bounds=(0, 1920))
    fbox(c, "x = 2   e   x = 3", 520, 785, 42, ep(t, C["18.f"], 0.5), GREEN)
    ag = ep(t, C["18.g"], 0.5)
    if ag > 0:
        boxed(c, 1080, 420, 600, 380, GREEN, ag, 0.05)
        text(c, "CONFERINDO x = 2", 1380, 465, 22, "black", GREEN, ag, tracking=2)
    rows = [("18.g", "2 · 2² − 10 · 2 + 12", INK), ("18.g", "= 2 · 4 − 20 + 12", INK), ("18.g", "= 8 − 20 + 12", INK),
            ("18.g", "= 0  ✓", GREEN)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue] + [0, 2.2, 4.0, 5.6][k])
        fmid(c, s, 1380, 540 + k * 68 + d, 38, "black", col, a)


FRASES = ["A soma das raízes é menos b sobre a.", "O produto das raízes é c sobre a.",
          "Comece pelo produto e use a soma para escolher o par."]


def b_recap(c, t, C, B):
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR", PURPLE)
    forms = [[("t", "x₁ + x₂ = ", PURPLE), ("f", "−b", "a", PURPLE)], [("t", "x₁ · x₂ = ", PURPLE), ("f", "c", "a", PURPLE)],
             [("t", "produto → pares → a soma escolhe", GREEN)]]
    for k, s in enumerate(FRASES):
        cue = f"19.{'abc'[k]}"
        a, d = rise(t, C[cue])
        y = 270 + k * 185 + d
        badge_num(c, k + 1, 260, y, a, 36, bg=PURPLE if k < 2 else GREEN)
        text_mid(c, s, 330, y - 30, 42, "black", INK, a, align="left")
        mrow(c, forms[k], 330, y + 52, 50 if k < 2 else 36, ep(t, C[cue] + 0.6, 0.4))


# ======================================================================
# CENA 5 — desafio
# ======================================================================

def b_desafio(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "AGORA É SUA VEZ!", "O DESAFIO", GREEN), ("21", "RESPOSTA DO DESAFIO", "x² − 9x + 20 = 0", GREEN)])
    card(c, *CARD_R)
    if sid == "20":
        if t >= C["20.a"]:
            build(c, t, C["20.a"], [("x²", None), (" − 9x", None), (" + 20", None), (" = 0", None)], W / 2, 245, 70)
        for cue, y, op, res, nome, col in (("20.b", 400, "+", "9", "SOMA", BLUE), ("20.b", 540, "×", "20", "PRODUTO", PURPLE)):
            a, d = rise(t, C[cue] + (0 if nome == "SOMA" else 1.4))
            if a <= 0:
                continue
            pill(c, nome, 330, y + d, col, size=26, a=a, anchor="center", bounds=(0, 1920))
            caixinha(c, 520, y + d, "?", a, col, 50)
            fmid(c, op, 630, y + d, 56, "black", INK, a)
            caixinha(c, 740, y + d, "?", a, col, 50)
            fmid(c, "=", 850, y + d, 56, "black", INK, a)
            fmid(c, res, 900, y + d, 66, "black", col, a, align="left")
        ac = ep(t, C["20.c"], 0.4) * (1 - ep(t, C["20.cd"], 0.3))
        pill(c, "você tem 10 segundos", 1340, 470, AMBER, size=30, a=ac, anchor="center", bounds=(0, 1920))
        contagem(c, t, C["20.cd"], 1340, 470, R=140)
        text(c, "dica: comece pelo produto", 640, 720, 30, "black", GREEN, ep(t, C["20.cd"] + 2.0, 0.5))
        ar = ep(t, C["20.r"], 0.3)
        if ar > 0:
            s_ = 0.8 + 0.2 * ease_back(ar)
            c.save(); c.translate(1340, 470); c.scale(s_, s_)
            text_mid(c, "TEMPO!", 0, 0, 90, "black", RED, ar)
            c.restore()
        return
    aa = ep(t, C["21.a"], 0.5)
    if aa > 0:
        mrow(c, [("t", "soma = ", INK), ("f", "−(−9)", "1"), ("t", " = 9", GREEN)], 200, 260, 40, aa)
        mrow(c, [("t", "produto = ", INK), ("f", "20", "1"), ("t", " = 20", GREEN)], 200, 380, 40,
             ep(t, C["21.a"] + 2.4, 0.5))
    rows = [dict(cells=[("21.b", "1 e 20"), ("21.b", "21")], marks=[("21.b", False, 1)]),
            dict(cells=[("21.c", "2 e 10"), ("21.c", "12")], marks=[("21.c", False, 1)]),
            dict(cells=[("21.d", "4 e 5"), ("21.d", "9")], marks=[("21.d", True, 1)], hl="21.e")]
    tabela(c, t, C, 1000, 210, (330, 270), "21.b", rows, size=44, rh=92, heads=("PAR (PRODUTO 20)", "SOMA"))
    rows2 = [("21.e", "4 + 5 = 9  ✓", GREEN), ("21.f", "4 × 5 = 20  ✓", GREEN)]
    linhas(c, t, C, rows2, 200, 500, 42, 70)
    fbox(c, "x₁ = 4    x₂ = 5", 1165, 640, 54, ep(t, C["21.g"], 0.5), GREEN)
    pill(c, "resolvido DE CABEÇA!", 1165, 770, GREEN, size=30, a=ep(t, C["21.h"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# CENA 6 — encerramento
# ======================================================================

PASSOS = [("22.a", "Identifique a, b e c", "com os sinais!", BLUE),
          ("22.b", "Soma = −b/a", "", PURPLE),
          ("22.c", "Produto = c/a", "", PURPLE),
          ("22.d", "Procure 2 números que satisfaçam as duas", "comece pelo produto", GREEN),
          ("22.e", "Confira substituindo na equação original", "tem que dar 0", GREEN)]


def b_passos(c, t, C, B):
    frame(c, t, B["start"], "RECAPITULANDO", "O MÉTODO EM 5 PASSOS", PURPLE)
    for k, (cue, s, sub, col) in enumerate(PASSOS):
        a, d = rise(t, C[cue])
        y = 235 + k * 118 + d
        if a <= 0:
            continue
        rrect(c, 220, y - 48, 1480, 96, 22, mix("#FFFFFF", col, 0.08), a)
        badge_num(c, k + 1, 280, y, a, 30, bg=col)
        if k in (1, 2):
            items = [("t", "Soma = " if k == 1 else "Produto = ", col)]
            items += [("t", "−", col), ("f", "b", "a", col)] if k == 1 else [("f", "c", "a", col)]
            mrow(c, items, 340, y, 42, a)
        else:
            fmid(c, s, 340, y, 40, "black", INK, a, align="left")
            if sub:
                fmid(c, sub, 1670, y, 28, "black", col, a, align="right")


def b_fecho(c, t, C, B):
    frame(c, t, B["start"], "PARA LEVAR DESTA AULA", "SOMA E PRODUTO", BLUE)
    aa = ep(t, C["23.a"], 0.5)
    text(c, "Nem toda equação terá raízes fáceis de achar de cabeça.", W / 2, 235, 36, "bold", INK2, aa)
    ab = ep(t, C["23.b"], 0.5)
    text(c, "Mas quem entende soma e produto enxerga a matemática de outro jeito.", W / 2, 295, 36, "bold", INK2, ab)
    ac = ep(t, C["23.c"], 0.5)
    if ac > 0:
        boxed(c, 240, 330, 1440, 180, GREEN, ac, 0.07)
        text(c, "O segredo não é decorar fórmulas,", W / 2, 403, 50, "black", INK, ac)
        text(c, "mas compreender como os números se relacionam!", W / 2, 475, 50, "black", GREEN, ac)
    ad = ep(t, C["23.d"], 0.5)
    if ad > 0:
        pill(c, "PRÓXIMA AULA", 300, 590, PURPLE, size=24, a=ad, bounds=(0, 1920))
        text(c, "Método de Po-Shen Loh", 300, 670, 46, "black", INK, ad, align="left")
        text(c, "quando as raízes não são fáceis de achar de cabeça", 300, 720, 28, "bold", GRAY, ad, align="left")
        X = V16.reta(c, 1180, 1620, 760, 0, 8, ad)
        if X:
            V16.gangorra(c, X, 760, 4, 2, ad, show_val=0.0, h=100, s=1.0)


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"],
        "Quanto tempo você levou para resolver o desafio?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, logica=b_logica, tabela=b_tabela, porque=b_porque,
              fatoracao=b_fatoracao, geral=b_geral, girard=b_girard, prova=b_prova, armadilha=b_armadilha, ex1=b_ex1,
              ex2=b_ex2, ex3=b_ex3, recap=b_recap, desafio=b_desafio, passos=b_passos, fecho=b_fecho, cta=b_cta)
