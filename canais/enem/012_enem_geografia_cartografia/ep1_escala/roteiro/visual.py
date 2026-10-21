"""Visual — Cartografia, Episódio 1: Escala (aula para iniciantes, tema claro).
Cores com função: azul = definição · âmbar = atenção/armadilha · verde = atalho/dica · vermelho = erro.
"""
import math
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

ASSETS = Path(__file__).parent.parent / "assets" / "ia"
POSTER = (454, 155, 1087, 505)  # pôster em branco na sala_de_aula.png (px da imagem 1536x1024)

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep1_escala.mp4"
CARD_R = (140, 150, 1640, 690)
SEA = "#DBEAFE"
LAND = "#86C18A"
LAND2 = "#5FA463"
PIZZA = "#FCD34D"
CRUST = "#D97706"

AFRICA = [(0.30, 0.00), (0.55, 0.02), (0.70, 0.10), (0.95, 0.22), (1.00, 0.32), (0.85, 0.45), (0.80, 0.60), (0.68, 0.80),
          (0.55, 1.00), (0.45, 0.95), (0.38, 0.72), (0.32, 0.55), (0.10, 0.45), (0.00, 0.30), (0.05, 0.12)]
BRASIL = [(0.35, 0.0), (0.55, 0.05), (0.75, 0.12), (1.0, 0.28), (0.95, 0.40), (0.85, 0.55), (0.75, 0.72), (0.62, 0.85),
          (0.50, 1.0), (0.42, 0.88), (0.45, 0.72), (0.30, 0.62), (0.20, 0.50), (0.0, 0.42), (0.05, 0.25), (0.20, 0.15)]
EUROPA = [(0.1, 0.3), (0.3, 0.05), (0.55, 0.0), (0.8, 0.1), (1.0, 0.35), (0.85, 0.7), (0.6, 0.95), (0.35, 1.0), (0.15, 0.75), (0.0, 0.55)]


# ======================================================================
# utilidades de desenho
# ======================================================================

def clip_rect(c, x, y, w, h, r=28):
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), True)


def blob(c, pts, x, y, w, h, col, a, stroke=None):
    if a <= 0:
        return
    p = skia.Path()
    P = [(x + u * w, y + v * h) for u, v in pts]
    p.moveTo(*P[0])
    for i in range(1, len(P)):
        p.quadTo(P[i - 1][0], P[i - 1][1], (P[i - 1][0] + P[i][0]) / 2, (P[i - 1][1] + P[i][1]) / 2)
    p.quadTo(P[-1][0], P[-1][1], (P[-1][0] + P[0][0]) / 2, (P[-1][1] + P[0][1]) / 2)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint(stroke or LAND2, a, stroke=3))


def world_map(c, x, y, w, h, a):
    """mapa-múndi com contornos reais (Natural Earth), preenchendo o retângulo"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, SEA, a)
    mapas.draw_world(c, (x + 6, y + 6, w - 12, h - 12), a, frame=False, radius=12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK2, a, stroke=3))


REGIAO = [(0.05, 0.35), (0.2, 0.1), (0.45, 0.05), (0.62, 0.15), (0.85, 0.08), (1.0, 0.3), (0.92, 0.55), (0.98, 0.8), (0.75, 0.95),
          (0.5, 0.88), (0.3, 1.0), (0.12, 0.85), (0.0, 0.6)]


def regiao(c, x, y, w, h, a):
    """terra genérica para mapas regionais (de propósito, não é um país real)"""
    blob(c, REGIAO, x, y, w, h, LAND, a)


def brasil(c, x, y, w, h, a):
    mapas.draw_country(c, "Brazil", (x, y, w, h), a)


@lru_cache(None)
def _img(nome):
    return skia.Image.open(str(ASSETS / nome))


def photo(c, nome, x, y, w, h, a, r=28):
    """ilustração (IA) cobrindo o retângulo; devolve a função que leva px da imagem para a tela"""
    im = _img(nome)
    s = max(w / im.width(), h / im.height())
    ox, oy = x + (w - im.width() * s) / 2, y + (h - im.height() * s) / 2
    if a > 0:
        c.save()
        c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), True)
        p = skia.Paint(AntiAlias=True); p.setAlphaf(clamp(a))
        c.drawImageRect(im, skia.Rect.MakeXYWH(ox, oy, im.width() * s, im.height() * s), skia.SamplingOptions(skia.FilterMode.kLinear), p)
        c.restore()
    return lambda px, py: (ox + px * s, oy + py * s)


def bairro(c, x, y, w, h, a, cols=5, rows=4):
    """ruas e quarteirões com casinhas (zoom aproximado)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, "#9CA3AF", a)
    gw, gh = w / cols, h / rows
    for i in range(cols):
        for j in range(rows):
            bx, by = x + i * gw + 8, y + j * gh + 8
            rrect(c, bx, by, gw - 16, gh - 16, 6, "#F3F4F6", a)
            for q in range(3):
                c.drawRect(skia.Rect.MakeXYWH(bx + 6 + q * (gw - 28) / 3, by + 6, (gw - 40) / 3, (gh - 28) / 2), paint("#F59E0B", a * 0.75))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(INK2, a, stroke=3))


def pizza(c, cx, cy, r, n, a, hi=0.0, hi_col=GREEN):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(PIZZA, a))
    c.drawCircle(cx, cy, r, paint(CRUST, a, stroke=10))
    for k in range(n):
        ang = -90 + 360 * k / n
        line(c, cx, cy, cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)), CRUST, a, 3)
    if hi > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 / n, False); p.close()
        c.drawPath(p, paint(hi_col, a * 0.55 * hi))
        c.drawPath(p, paint(hi_col, a * hi, stroke=6))


def scale_bar(c, x, y, w, a, labels=("0", "5", "10 km"), size=22):
    if a <= 0:
        return
    for k in range(2):
        c.drawRect(skia.Rect.MakeXYWH(x + k * w / 2, y, w / 2, 14), paint(INK if k == 0 else "#FFFFFF", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, 14), paint(INK, a, stroke=2))
    for k, s in enumerate(labels):
        text(c, s, x + k * w / 2, y + 40, size, "bold", INK2, a)


def mini_map(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, SEA, a)
    regiao(c, x + w * 0.08, y + h * 0.08, w * 0.84, h * 0.84, a)
    p = skia.Path(); p.moveTo(x + w * 0.3, y + h * 0.3)
    p.cubicTo(x + w * 0.45, y + h * 0.45, x + w * 0.4, y + h * 0.6, x + w * 0.6, y + h * 0.75)
    c.drawPath(p, paint("#0EA5E9", a, stroke=max(2, w / 120)))
    c.drawCircle(x + w * 0.55, y + h * 0.4, max(4, w / 60), paint(RED, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(INK2, a, stroke=3))


def ruler(c, x, y, length_px, units, a, label_every=1):
    """régua com marcações de 0 a 'units' centímetros"""
    if a <= 0 or length_px <= 4:
        return
    rrect(c, x - 10, y - 8, length_px + 20, 54, 8, "#FDE68A", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, y - 8, length_px + 20, 54), 8, 8), paint(CRUST, a, stroke=2))
    step = length_px / units
    for k in range(units + 1):
        line(c, x + k * step, y - 8, x + k * step, y + 14, INK, a, 2)
        if k % label_every == 0:
            text(c, str(k), x + k * step, y + 38, 20, "bold", INK, a)


def zeros_cut(c, t, lead, x, y, size, a, t0, unit=" cm"):
    """escreve lead + 00000 e risca os cinco zeros, um a um"""
    if a <= 0:
        return x
    text(c, lead, x, y, size, "black", INK, a, align="left")
    x += text_w(lead, "black", size)
    for k in range(5):
        w = text_w("0", "black", size)
        text(c, "0", x, y, size, "black", RED, a, align="left")
        strike(c, x - 4, y - size * 0.15, x + w + 4, y - size * 0.75, a, RED, ep(t, t0 + 0.25 * k, 0.3))
        x += w
    text(c, unit, x, y, size * 0.7, "black", INK, a, align="left")
    return x + text_w(unit, "black", size * 0.7)


def badge_row(c, t, rows, x, y0, dy, size=40):
    """linhas numeradas: rows = [(cue_time, texto, cor)]"""
    for k, (tc, s, col) in enumerate(rows):
        a, d = rise(t, tc)
        y = y0 + k * dy + d
        badge_num(c, k + 1, x, y - size * 0.36, a, 30, bg=col)
        text(c, s, x + 56, y, size, "black", INK, a, align="left")


def erro_tiles(c, t, items):
    """três passos do erro: (cue_time, título, linhas, cor)"""
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (tc, tt, lines, col) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x, y = x0 + k * (cw + gap), 200 + dy
        card(c, x, y, cw, 500, a)
        rrect(c, x, y, cw, 70, 28, col, a * 0.15)
        text_mid(c, tt, x + cw / 2, y + 38, 30, "black", col, a)
        if k == 0:
            check_icon(c, x + cw / 2, y + 140, 30, a, RED, "x")
        elif k == 2:
            check_icon(c, x + cw / 2, y + 140, 30, a, GREEN)
        else:
            text_mid(c, "?", x + cw / 2, y + 140, 70, "black", AMBER, a)
        for j, ln in enumerate(lines):
            text(c, ln, x + cw / 2, y + 250 + j * 58, 36, "black", INK, a)


def globe(c, cx, cy, r, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(SEA, a))
    for L in (-60, -30, 0, 30, 60):
        yy = cy - r * math.sin(math.radians(L)); hw = r * math.cos(math.radians(L))
        line(c, cx - hw, yy, cx + hw, yy, "#93C5FD", a, 2)
    for L in (-60, -30, 30, 60):
        rx = r * abs(math.sin(math.radians(L)))
        c.drawOval(skia.Rect.MakeLTRB(cx - rx, cy - r, cx + rx, cy + r), paint("#93C5FD", a, stroke=2))
    line(c, cx, cy - r, cx, cy + r, "#93C5FD", a, 2)
    c.drawCircle(cx, cy, r, paint(INK2, a, stroke=4))


# ======================================================================
# gancho e promessa
# ======================================================================

def b_hook(c, t, C, B):
    st = B["start"]
    a0 = ep(t, st + 0.2, 0.6)
    card(c, 160, 190, 960, 520, a0)
    to = photo(c, "sala_de_aula.png", 160, 190, 960, 520, a0)
    (px0, py0), (px1, py1) = to(POSTER[0], POSTER[1]), to(POSTER[2], POSTER[3])
    rrect(c, px0, py0, px1 - px0, py1 - py0, 6, SEA, a0)
    mapas.draw_world(c, (px0 + 4, py0 + 4, px1 - px0 - 8, py1 - py0 - 8), a0 * ep(t, st + 0.6, 0.6), frame=False, radius=4)
    arrow(c, px0, py1 + 24, px1, py1 + 24, INK, a0, 4, 14)
    arrow(c, px1, py1 + 24, px0, py1 + 24, INK, a0, 4, 14)
    pill(c, "2 metros", (px0 + px1) / 2, py1 + 24, INK, size=26, a=a0, anchor="center")
    aa = ep(t, C["01.a"], 0.5)
    card(c, 1240, 300, 480, 340, aa)
    bairro(c, 1270, 330, 420, 280, aa)
    text(c, "só o bairro", 1480, 690, 30, "black", INK2, aa)
    pill(c, "qual tem a escala MAIOR?", W / 2, 790, BLUE, size=34, a=ep(t, C["01.b"], 0.5), anchor="center")
    pill(c, "pegadinha!", 640, 150, AMBER, size=32, a=ep(t, C["01.c"], 0.5), anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1240, 300, 480, 340), 28, 28), paint(GREEN, ad, stroke=8))
    pill(c, "escala MAIOR", 1480, 250, GREEN, size=32, a=ad, anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Ler a escala\nde qualquer mapa", C["02.a"], BLUE), ("2", "Descobrir a\ndistância real", C["02.b"], GREEN),
                     ("3", "Escolher o\nmapa certo", C["02.c"], PURPLE)], cw=440, chh=400, title_size=38)


# ======================================================================
# pré-requisitos relâmpago
# ======================================================================

def b_fracao(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 1", "FRAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    frac(c, "1", "4", 560, 440, 170, INK, aa, "black")
    pizza(c, 1330, 470, 200, 4, aa, ep(t, C["03.a"] + 0.8, 0.5))
    ab = ep(t, C["03.b"], 0.5)
    arrow(c, 820, 650, 650, 560, BLUE, ab, 6, 22)
    pill(c, "DENOMINADOR = o número de baixo", 830, 680, BLUE, size=28, a=ab)
    text(c, "em quantos pedaços cortou", 830, 750, 28, "bold", BLUE, ab, align="left")


def b_pizza(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 2", "QUAL FRAÇÃO É MAIOR?", BLUE)
    card(c, *CARD_R)
    hc = ep(t, C["04.c"], 0.5)
    for cue, n, cx, lab_n in (("04.a", 4, 560, "4"), ("04.b", 12, 1360, "12")):
        a = ep(t, C[cue], 0.5)
        pizza(c, cx, 420, 190, n, a, 1.0, GREEN if n == 4 else AMBER)
        frac(c, "1", lab_n, cx, 690, 64, INK, a, "black")
    pill(c, "MAIOR", 560, 200, GREEN, size=32, a=hc, anchor="center")
    pill(c, "número de baixo MAIOR → pedaço MENOR", W / 2, 800, BLUE, size=30, a=ep(t, C["04.d"], 0.5), anchor="center")


def b_cmkm(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 3", "CENTÍMETRO → QUILÔMETRO", BLUE)
    card(c, *CARD_R)
    rows = [("05.a", "100 cm = 1 m"), ("05.b", "1 000 m = 1 km"), ("05.c", "1 km = 100 × 1 000 = 100 000 cm")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        text(c, s, W / 2, 300 + k * 120 + dy, 58, "black", INK, a)
    result_box(c, "guarde: 100 000", W / 2, 700, 54, ep(t, C["05.c"] + 2.0, 0.5), GREEN)


# ======================================================================
# bloco 1: o que é escala
# ======================================================================

def b_planta(c, t, C, B):
    head(c, t, B["start"], "O QUE É ESCALA?", "O MUNDO ENCOLHIDO", BLUE)
    aa = ep(t, C["06.a"], 0.5)
    # quarto de verdade
    card(c, 180, 190, 640, 360, aa)
    text(c, "de verdade", 500, 240, 30, "black", INK2, aa)
    rrect(c, 260, 280, 480, 220, 10, "#FDE68A", aa * 0.6)
    rrect(c, 290, 320, 160, 110, 10, "#93C5FD", aa)
    c.drawCircle(640, 360, 26, paint(INK2, aa)); rrect(c, 615, 390, 50, 90, 20, INK2, aa)
    ab = ep(t, C["06.b"], 0.5)
    arrow(c, 260, 520, 740, 520, RED, ab, 4, 14); arrow(c, 740, 520, 260, 520, RED, ab, 4, 14)
    pill(c, "3 m", 500, 520, RED, size=30, a=ab, anchor="center")
    # planta no papel
    card(c, 1000, 190, 720, 360, aa)
    text(c, "no papel (planta)", 1360, 240, 30, "black", INK2, aa)
    for (x, y, w, h) in ((1060, 280, 200, 220), (1260, 280, 180, 120), (1260, 400, 180, 100), (1440, 280, 220, 220)):
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(INK, aa, stroke=4))
    ac = ep(t, C["06.c"], 0.5)
    rrect(c, 1060, 280, 200, 220, 0, RED, 0.15 * ac)
    pill(c, "3 cm", 1160, 520, RED, size=30, a=ac, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    arrow(c, 830, 370, 990, 370, BLUE, ad, 6, 22, progress=ad)
    pill(c, "encolhido", 910, 320, BLUE, size=24, a=ad, anchor="center")
    # cena 07: as contas
    rows = [("07.a", "3 m = 300 cm", INK), ("07.b", "300 cm  →  3 cm", INK), ("07.c", "1 cm do desenho = 100 cm de verdade", INK)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        text(c, s, 260 + k * 0, 620 + k * 56 + dy, 36, "black", col, a, align="left")
    pill(c, "ESCALA = quantas vezes o mundo ENCOLHEU", 1340, 700, BLUE, size=30, a=ep(t, C["07.d"], 0.5), anchor="center")


def b_numerica(c, t, C, B):
    head(c, t, B["start"], "ESCALA NUMÉRICA", "COMO SE LÊ", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    sz = 170
    s_full = "1 : 100"
    x0 = W / 2 - text_w(s_full, "black", sz) / 2
    text(c, s_full, W / 2, 430, sz, "black", INK, aa)
    text(c, "“um para cem”", W / 2, 510, 36, "bold", GRAY, aa)
    x1 = x0 + text_w("1", "black", sz) / 2
    x2 = x0 + text_w("1 : ", "black", sz) + text_w("100", "black", sz) / 2
    ab = ep(t, C["08.b"], 0.5)
    arrow(c, x1, 560, x1 - 80, 650, BLUE, ab, 5, 18)
    pill(c, "MAPA", x1 - 80, 680, BLUE, size=34, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["08.c"], 0.5)
    arrow(c, x2, 560, x2 + 80, 650, GREEN, ac, 5, 18)
    pill(c, "MUNDO REAL", x2 + 80, 680, GREEN, size=34, a=ac, anchor="center", bounds=(0, 1920))
    pill(c, "ESCALA NUMÉRICA = escala escrita com números", W / 2, 800, BLUE, size=28, a=ep(t, C["08.d"], 0.5), anchor="center")


# ======================================================================
# bloco 2: centímetros em quilômetros
# ======================================================================

def b_cemmil(c, t, C, B):
    head(c, t, B["start"], "NUM MAPA DE CIDADE", "1 : 100 000", BLUE)
    card(c, *CARD_R)
    text(c, "1 : 100 000", W / 2, 320, 110, "black", INK, ep(t, C["09.a"], 0.5))
    text(c, "1 cm no mapa = 100 000 cm no chão", W / 2, 440, 48, "black", INK2, ep(t, C["09.b"], 0.5))
    pill(c, "100 000 cm?! ninguém pensa assim", W / 2, 530, AMBER, size=28, a=fw(t, C["09.c"], C["09.d"] - 0.1), anchor="center")
    ad = ep(t, C["09.d"], 0.5)
    result_box(c, "100 000 cm = 1 km", W / 2, 560, 58, ad, GREEN)
    text(c, "1 cm no mapa  →  1 km de verdade", W / 2, 720, 46, "black", INK, ep(t, C["09.d"] + 1.6, 0.5))


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CORTE CINCO ZEROS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    x = zeros_cut(c, t, "1", 560, 340, 90, aa, C["10.a"] + 0.8)
    arrow(c, x + 30, 310, x + 130, 310, GREEN, aa, 6, 22)
    text(c, "1 km", x + 160, 340, 90, "black", GREEN, aa, align="left")
    ab = ep(t, C["10.b"], 0.5)
    for k in range(5):
        badge_num(c, k + 1, 620 + k * 56, 400, ab * ep(t, C["10.b"] + 0.2 * k, 0.3), 20, bg=AMBER)
    text(c, "cem mil tem 5 zeros", 960, 410, 30, "black", AMBER, ab, align="left")
    ac = ep(t, C["10.c"], 0.5)
    text(c, "1 : 500 000", W / 2, 540, 70, "black", INK, ac)
    ad = ep(t, C["10.d"], 0.5)
    x = zeros_cut(c, t, "5", 640, 660, 76, ad, C["10.d"] + 0.3)
    arrow(c, x + 30, 634, x + 130, 634, GREEN, ad, 6, 22)
    text(c, "5 km", x + 160, 660, 76, "black", GREEN, ad, align="left")
    pill(c, "1 cm no mapa = 5 km", W / 2, 790, GREEN, size=32, a=ep(t, C["10.e"], 0.5), anchor="center")


# ======================================================================
# bloco 3: distância real
# ======================================================================

def b_conta(c, t, C, B):
    head(c, t, B["start"], "DISTÂNCIA REAL", "PASSO A PASSO", BLUE)
    card(c, *CARD_R)
    at = ep(t, C["11.t"], 0.5)
    rrect(c, 200, 220, 780, 460, 18, SEA, at)
    regiao(c, 250, 250, 700, 400, at)
    A, Bp = (480, 430), (770, 430)
    for p, lab in ((A, "A"), (Bp, "B")):
        if at > 0:
            c.drawCircle(*p, 14, paint(RED, at))
        text_mid(c, lab, p[0], p[1] - 40, 34, "black", RED, at)
    aa = ep(t, C["11.a"], 0.5)
    ruler(c, A[0], 470, (Bp[0] - A[0]) * ep(t, C["11.a"], 1.2), 8, aa)
    pill(c, "8 cm", 625, 570, INK, size=32, a=ep(t, C["11.a"] + 1.2, 0.4), anchor="center")
    text(c, "1 : 500 000", 590, 270, 36, "black", INK, at)
    ab = ep(t, C["11.b"], 0.5)
    text(c, "1 cm = 5 km", 1350, 290, 52, "black", GREEN, ab)
    ac = ep(t, C["11.c"], 0.5)
    for k in range(8):
        a = ac * ep(t, C["11.c"] + 0.15 * k, 0.3)
        rrect(c, 1040 + k * 80, 360, 68, 60, 10, BLUE, a)
        text_mid(c, "5", 1074 + k * 80, 390, 30, "black", "#FFFFFF", a)
    text(c, "8 pedaços de 5 km", 1350, 470, 34, "black", INK2, ac)
    text(c, "8 × 5", 1350, 580, 66, "black", INK, ep(t, C["11.d"], 0.5))
    result_box(c, "= 40 km", 1350, 690, 60, ep(t, C["11.e"], 0.5), GREEN)


# ======================================================================
# bloco 4: escala grande x pequena (âncora: o zoom)
# ======================================================================

def b_zoom(c, t, C, B):
    head(c, t, B["start"], "A ESCALA É O ZOOM", "DO MAPA", BLUE)
    px, py, pw, ph = 760, 180, 400, 600
    at = ep(t, C["12.t"], 0.5)
    rrect(c, px, py, pw, ph, 50, INK, at, shadow=True)
    sx, sy, sw, sh = px + 22, py + 60, pw - 44, ph - 120
    aa, ab = ep(t, C["12.a"], 0.6), ep(t, C["12.b"], 1.2)
    if at > 0:
        clip_rect(c, sx, sy, sw, sh, 20)
        c.drawRect(skia.Rect.MakeXYWH(sx, sy, sw, sh), paint(SEA, at))
        z = lerp(1.0, 0.25, ab)
        cx, cy = sx + sw / 2, sy + sh / 2
        bw, bh = sw * 1.6 * z, sh * 1.2 * z
        bairro(c, cx - bw / 2, cy - bh / 2, bw, bh, max(aa, 0.3) * (1 - ab * 0.9))
        brasil(c, sx + 20, sy + 40, sw - 40, sh - 100, ab)
        c.restore()
        for k, s in enumerate(("+", "−")):
            c.drawCircle(sx + sw - 34, sy + sh - 100 + k * 58, 24, paint("#FFFFFF", at))
            text_mid(c, s, sx + sw - 34, sy + sh - 100 + k * 58, 34, "black", INK, at)
    pill(c, "ZOOM APROXIMADO", 420, 360, GREEN, size=30, a=aa, anchor="center")
    text(c, "rua, casas, detalhes", 420, 430, 32, "black", INK2, aa)
    pill(c, "ZOOM AFASTADO", 1500, 360, PURPLE, size=30, a=ab, anchor="center")
    text(c, "o país inteiro", 1500, 430, 32, "black", INK2, ab)
    pill(c, "ESCALA = o ZOOM do mapa", W / 2, 815, BLUE, size=32, a=ep(t, C["12.c"], 0.5), anchor="center")


def b_grande(c, t, C, B):
    head(c, t, B["start"], "QUAL ESCALA É MAIOR?", "1 : 5 000 OU 1 : 5 000 000", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    text(c, "1 : 5 000", 560, 280, 66, "black", INK, aa)
    text(c, "1 : 5 000 000", 1360, 280, 66, "black", INK, aa)
    ab = ep(t, C["13.b"], 0.5)
    frac(c, "1", "5 000", 560, 390, 52, BLUE, ab, "black")
    frac(c, "1", "5 000 000", 1360, 390, 52, BLUE, ab, "black")
    ac = ep(t, C["13.c"], 0.5)
    pizza(c, 560, 600, 110, 24, ac, 1.0, GREEN)
    pizza(c, 1360, 600, 110, 90, ac, 1.0, RED)
    text(c, "pedaço maior", 560, 760, 30, "black", GREEN, ac)
    text(c, "pedaço menor", 1360, 760, 30, "black", RED, ac)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(330, 210, 460, 580), 28, 28), paint(GREEN, ad, stroke=7))
    pill(c, "escala MAIOR", 560, 190, GREEN, size=30, a=ad, anchor="center")


def b_regra(c, t, C, B):
    head(c, t, B["start"], "A REGRA", "QUE PARECE INVERTIDA", AMBER)
    for k, (cue, top, mid, zoom, desc, col, draw) in enumerate((
            ("14.a", "número de baixo PEQUENO", "ESCALA GRANDE", "zoom aproximado", "pouca área · muito detalhe", GREEN, "bairro"),
            ("14.b", "número de baixo GRANDE", "ESCALA PEQUENA", "zoom afastado", "muita área · pouco detalhe", PURPLE, "mundo"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 180 + dy
        card(c, x, y, 700, 600, a)
        text(c, top, x + 350, y + 60, 32, "black", INK2, a)
        arrow(c, x + 350, y + 80, x + 350, y + 120, col, a, 5, 16)
        text(c, mid, x + 350, y + 180, 54, "black", col, a)
        if draw == "bairro":
            bairro(c, x + 160, y + 220, 380, 220, a)
        else:
            world_map(c, x + 140, y + 220, 420, 220, a)
        pill(c, zoom, x + 350, y + 490, col, size=28, a=a, anchor="center", bounds=(0, 1920))
        text(c, desc, x + 350, y + 560, 30, "black", INK, a)


def b_usos(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "DO ZOOM APROXIMADO AO AFASTADO", BLUE)
    at = ep(t, C["15.t"], 0.5)
    arrow(c, 200, 770, 1720, 770, INK2, at, 5, 20)
    text(c, "zoom aproximado", 200, 815, 26, "black", GREEN, at, align="left")
    text(c, "zoom afastado", 1720, 815, 26, "black", PURPLE, at, align="right")

    def casa(c, x, y, w, h, a):
        text(c, "1 : 500", x + w / 2, y + 60, 44, "black", INK, a)
        for (rx, ry, rw, rh) in ((70, 110, 160, 150), (230, 110, 180, 90), (230, 200, 180, 60)):
            c.drawRect(skia.Rect.MakeXYWH(x + rx, y + ry, rw, rh), paint(INK, a, stroke=4))
        text(c, "planta de casa", x + w / 2, y + 320, 30, "black", INK2, a)
        pill(c, "escala GRANDE", x + w / 2, y + 380, GREEN, size=26, a=a, anchor="center", bounds=(0, 1920))

    def cidade(c, x, y, w, h, a):
        text(c, "1 : 50 000", x + w / 2, y + 60, 44, "black", INK, a)
        bairro(c, x + 70, y + 100, w - 140, 170, a, cols=9, rows=5)
        text(c, "mapa de cidade", x + w / 2, y + 320, 30, "black", INK2, a)
        pill(c, "escala MÉDIA", x + w / 2, y + 380, AMBER, size=26, a=a, anchor="center", bounds=(0, 1920))

    def mundo(c, x, y, w, h, a):
        text(c, "1 : 50 000 000", x + w / 2, y + 60, 44, "black", INK, a)
        world_map(c, x + 50, y + 100, w - 100, 170, a)
        text(c, "mapa-múndi", x + w / 2, y + 320, 30, "black", INK2, a)
        pill(c, "escala PEQUENA", x + w / 2, y + 380, PURPLE, size=26, a=a, anchor="center", bounds=(0, 1920))

    items = [(C["15.a"], casa), (C["15.b"], cidade), (C["15.c"], mundo)]
    x0 = W / 2 - (3 * 480 + 2 * 60) / 2
    for k, (tc, fn) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x = x0 + k * 540
        card(c, x, 190 + dy, 480, 430, a)
        fn(c, x, 190 + dy, 480, 430, a)


def b_parede(c, t, C, B):
    head(c, t, B["start"], "E O MAPA DA PAREDE?", "2 METROS DE LARGURA", AMBER)
    aa = ep(t, C["16.a"], 0.5)
    world_map(c, 200, 190, 1520, 470, aa)
    arrow(c, 200, 690, 1720, 690, INK2, aa, 4, 16); arrow(c, 1720, 690, 200, 690, INK2, aa, 4, 16)
    pill(c, "2 metros", W / 2, 690, INK, size=28, a=aa, anchor="center")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        c.drawRect(skia.Rect.MakeXYWH(820, 400, 20, 20), paint(RED, ab))
        c.drawRect(skia.Rect.MakeXYWH(820, 400, 20, 20), paint(INK, ab, stroke=2))
        arrow(c, 850, 410, 1010, 340, RED, ab, 4, 14)
    pill(c, "1 cm = centenas de km", 1020, 330, RED, size=28, a=ab, bounds=(0, 1920))
    pill(c, "zoom AFASTADO = escala PEQUENA", 560, 770, PURPLE, size=28, a=ep(t, C["16.c"], 0.5), anchor="center")
    pill(c, "o tamanho do PAPEL não importa", 1380, 770, AMBER, size=28, a=ep(t, C["16.d"], 0.5), anchor="center")


# ======================================================================
# recapitulação (meio e fim, as mesmas três frases)
# ======================================================================

def b_recap(c, t, C, B):
    sid = "17" if B["start"] < C["28"] - 1 else "28"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    rows = [(C[sid + ".a"], "Escala = quantas vezes o mundo ENCOLHEU", BLUE),
            (C[sid + ".b"], "cm → km: corte CINCO zeros", GREEN),
            (C[sid + ".c"], "GRANDE = zoom aproximado", PURPLE)]
    badge_row(c, t, rows, 260, 310, 150, 46)
    text(c, "PEQUENA = zoom afastado", 316, 520 + 150 - 0, 46, "black", INK, ep(t, C[sid + ".c"] + 1.4, 0.5), align="left")


# ======================================================================
# bloco 5: escala gráfica
# ======================================================================

def b_grafica(c, t, C, B):
    head(c, t, B["start"], "ESCALA GRÁFICA", "UMA RÉGUA NO MAPA", BLUE)
    card(c, *CARD_R)
    at = ep(t, C["18.t"], 0.5)
    mx, my, mw, mh = 200, 210, 920, 560
    bairro(c, mx, my, mw, mh, at, cols=8, rows=5)
    A, Bp = (mx + 270, my + 290), (mx + 270 + 3 * 130, my + 290)
    for p in (A, Bp):
        if at > 0:
            c.drawCircle(*p, 14, paint(RED, at))
    aa = ep(t, C["18.a"], 0.5)
    bw = 130
    rrect(c, mx + 20, my + mh - 90, bw + 100, 76, 12, "#FFFFFF", aa)
    scale_bar(c, mx + 50, my + mh - 74, bw, aa, ("0", "", "500 m"), 20)
    if aa > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(mx + 20, my + mh - 90, bw + 100, 76), 12, 12),
                    paint(BLUE, aa * (0.5 + 0.5 * math.sin(t * 4)), stroke=5))
    pill(c, "ESCALA GRÁFICA = régua desenhada no mapa", 1460, 300, BLUE, size=26, a=ep(t, C["18.b"], 0.5), anchor="center",
         bounds=(0, 1920))
    ac, ad = ep(t, C["18.c"], 0.5), C["18.d"]
    n = int((Bp[0] - A[0]) // bw)
    rrect(c, A[0] - 40, A[1] - 70, Bp[0] - A[0] + 80, 120, 16, "#FFFFFF", ac * 0.9)
    for p in (A, Bp):
        if at > 0:
            c.drawCircle(*p, 14, paint(RED, at))
    for k in range(n):
        a = ac * ep(t, ad + 0.6 * k, 0.4)
        f = ep(t, ad + 0.6 * k, 0.6)
        x = lerp(mx + 50, A[0] + k * bw, f); y = lerp(my + mh - 74, A[1] + 20, f)
        scale_bar(c, x, y, bw, a, ("", "", ""), 16)
        text(c, str(k + 1), A[0] + k * bw + bw / 2, A[1] - 20, 34, "black", AMBER, a)
    text(c, "quantas barrinhas cabem?", 1420, 450, 34, "black", INK, ac)
    text(c, "3 × 500 m = 1 500 m", 1420, 560, 44, "black", GREEN, ep(t, ad + 2.2, 0.5))


# ======================================================================
# bloco 6: mapa ampliado
# ======================================================================

def b_ampliado(c, t, C, B):
    head(c, t, B["start"], "MAPA AMPLIADO NO XEROX", "O DOBRO DO TAMANHO", AMBER)
    card(c, *CARD_R)
    photo(c, "xerox.png", *CARD_R, fw(t, B["start"], C["19.a"] + 0.2, 0.5, 0.6))
    at = ep(t, C["19.a"] - 0.3, 0.6)
    mini_map(c, 220, 300, 300, 210, at)
    scale_bar(c, 240, 530, 140, at)
    text(c, "1 : 1 000 000", 370, 620, 32, "black", INK, at)
    text(c, "original", 370, 270, 28, "black", GRAY, at)
    f = ep(t, C["19.a"], 1.2)
    s = lerp(1, 2, f) * 0.85
    if f > 0:
        mini_map(c, 600, 230, 300 * s, 210 * s, at)
    bfr = ep(t, C["19.b"], 1.0)
    bw = 140 * lerp(1, 2, min(f, 1)) * 0.85 if bfr > 0 else 0
    scale_bar(c, 620, 230 + 210 * s + 24, max(bw, 1), bfr)
    text(c, "cópia 2×", 600 + 300 * s / 2, 210, 28, "black", GRAY, f)
    check_icon(c, 640 + bw + 50, 230 + 210 * s + 32, 20, bfr, GREEN)
    text(c, "CERTA", 640 + bw + 80, 230 + 210 * s + 42, 28, "black", GREEN, bfr, align="left")
    ac = ep(t, C["19.c"], 0.5)
    text(c, "1 : 1 000 000", 860, 740, 34, "black", INK, ac)
    ad = ep(t, C["19.d"], 0.5)
    strike(c, 745, 730, 975, 730, ad, RED, ad)
    pill(c, "ERRADO", 990, 728, RED, size=26, a=ad, bounds=(0, 1920))
    # cena 20: por quê
    line(c, 1190, 210, 1190, 790, LINE, ep(t, C["20.a"], 0.5), 3)
    rows = [("20.a", "antes: 1 cm = 10 km", INK), ("20.b", "depois: 10 km = 2 cm", INK), ("20.c", "1 cm = 5 km", BLUE)]
    for k, (cue, s_, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        text(c, s_, 1460, 290 + k * 90 + dy, 40, "black", col, a)
    result_box(c, "1 : 500 000", 1460, 590, 52, ep(t, C["20.d"], 0.5), GREEN)
    pill(c, "o celular usa a BARRINHA", 1460, 730, GREEN, size=28, a=ep(t, C["20.e"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "DENOMINADOR GRANDE = ESCALA GRANDE?", RED)
    erro_tiles(c, t, [(C["21.a"], "O ERRO", ["1 : 5 000 000", "é escala grande"], RED),
                      (C["21.b"], "POR QUE PARECE CERTO", ["5 000 000 é", "um número ENORME"], AMBER),
                      (C["21.c"], "A CORREÇÃO", ["é o número de BAIXO:", "pedaço MENOR", "escala PEQUENA"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "ESQUECER DE CONVERTER", RED)
    erro_tiles(c, t, [(C["22.a"], "O ERRO", ["8 × 500 000", "= 4 000 000"], RED),
                      (C["22.b"] + 1.5, "POR QUE PARECE CERTO", ["a conta", "está certa"], AMBER),
                      (C["22.c"], "A CORREÇÃO", ["são CENTÍMETROS", "corte 5 zeros:", "40 km"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "CONFIAR NO NÚMERO DO MAPA AMPLIADO", RED)
    erro_tiles(c, t, [(C["23.a"], "O ERRO", ["usar o número", "do mapa ampliado"], RED),
                      (C["23.b"], "POR QUE PARECE CERTO", ["o número está", "IMPRESSO ali"], AMBER),
                      (C["23.c"], "A CORREÇÃO", ["vale para o", "tamanho ORIGINAL:", "use a BARRINHA"], GREEN)])


# ======================================================================
# questão estilo ENEM
# ======================================================================

ALTS = [("A", "1 : 2 000 000 · escala maior, mais detalhe", "26.a", "denominador grande ≠ escala grande"),
        ("B", "1 : 2 000 000 · mais área, mesmo detalhe", "26.b", "mais área = MENOS detalhe"),
        ("C", "1 : 2 000 · escala pequena", "27.c", "1 : 2 000 é escala GRANDE"),
        ("D", "1 : 2 000 · escala maior, mais detalhe", None, ""),
        ("E", "tanto faz: escala não muda o detalhe", "26.e", "mesmo motivo da B")]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "BOCAS DE LOBO, RUA POR RUA", BLUE)
    card(c, *CARD_R)
    text(c, "Planejar bocas de lobo, rua por rua, num bairro que alaga.", 210, 240, 34, "black", INK,
         ep(t, C["24.e1"], 0.5), align="left")
    text(c, "Mapas do mesmo tamanho: 1 : 2 000 e 1 : 2 000 000.", 210, 295, 34, "black", INK, ep(t, C["24.e2"], 0.5), align="left")
    text(c, "Qual é o mais adequado?", 210, 350, 34, "black", BLUE, ep(t, C["24.e3"], 0.5), align="left")
    keys = ["25.a", "25.b", "25.c", "25.d", "25.e"]
    ad = ep(t, C["27.d"], 0.5)
    for k, ((L, s, cue_x, why), key) in enumerate(zip(ALTS, keys)):
        a, dy = rise(t, C[key])
        y = 440 + k * 72 + dy
        ok = L == "D"
        hi = ad if ok else 0
        if hi > 0:
            rrect(c, 190, y - 34, 1540, 62, 14, GREEN, 0.15 * hi)
        badge_num(c, L, 230, y - 10, a, 24, bg=GREEN if hi > 0.5 else INK)
        text(c, s, 275, y, 32, "black", INK, a * (1 - 0.55 * (ep(t, C[cue_x], 0.4) if cue_x else 0)), align="left")
        if cue_x:
            ax = ep(t, C[cue_x], 0.4)
            strike(c, 270, y - 10, 270 + text_w(s, "black", 32) + 10, y - 10, ax, RED, ax)
            text(c, why, 1720, y, 26, "black", RED, ax, align="right")
    ap = ep(t, C["25.p"], 0.5) * (1 - prog(t, C["26.t"] - 0.3, 0.4))
    if ap > 0:
        rrect(c, 1380, 200, 350, 110, 24, AMBER, ap, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(1410, 228, 14, 54), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(1436, 228, 14, 54), paint(INK, ap))
        text_mid(c, "PAUSE E TENTE", 1595, 255, 30, "black", INK, ap)
    pill(c, "RESPOSTA: D · 1 cm = 20 m, cada rua aparece", 1300, 365, GREEN, size=26, a=ep(t, C["27.x"], 0.5), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "COORDENADAS GEOGRÁFICAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["29.a"], 0.5)
    globe(c, 600, 480, 260, aa)
    if aa > 0:
        P = (600 + 260 * math.cos(math.radians(40)) * 0.6, 480 - 260 * math.sin(math.radians(25)))
        c.drawCircle(*P, 16 + 3 * math.sin(t * 5), paint(RED, aa))
    text(c, "QUALQUER ponto da Terra", 1300, 400, 46, "black", INK, aa)
    text(c, "com só 2 números", 1300, 470, 40, "black", PURPLE, ep(t, C["29.a"] + 1.2, 0.5))
    pill(c, "COORDENADAS GEOGRÁFICAS", 1300, 590, PURPLE, size=34, a=ep(t, C["29.b"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "O mapa da parede tinha escala grande?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, fracao=b_fracao, pizza=b_pizza, cmkm=b_cmkm, planta=b_planta,
              numerica=b_numerica, cemmil=b_cemmil, atalho=b_atalho, conta=b_conta, zoom=b_zoom, grande=b_grande,
              regra=b_regra, usos=b_usos, parede=b_parede, recap=b_recap, grafica=b_grafica, ampliado=b_ampliado,
              erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, questao=b_questao, ponte=b_ponte, cta=b_cta)
