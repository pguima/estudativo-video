"""Visual — Cartografia, Episódio 4: Curvas de nível, perfil topográfico e declividade (aula para iniciantes, tema claro).
Cores com função: azul = definição · âmbar = atenção/armadilha · verde = atalho/dica · vermelho = erro.
O morro é um "bolo de camadas" (4 fatias de 100 m): visto de lado vira 3D; visto de cima vira as curvas de nível.
"""
import math
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep4_curvas_de_nivel.mp4"
CARD_R = (140, 150, 1640, 690)
BROWN = "#A16207"
RIVER = "#0EA5E9"
LAYER = ["#D9F99D", "#A3E635", "#65A30D", "#3F6212"]
SIDE = ["#BEF264", "#84CC16", "#4D7C0F", "#365314"]
# anéis do morro em coordenadas do plano (u para leste, v para o sul): (oeste, leste, meia-altura em v)
# lado oeste com anéis colados (íngreme), lado leste com anéis espaçados (suave)
RINGS = [(-330 + 45 * k, 330 - 80 * k, 210 - 45 * k) for k in range(4)]
SUMMIT = (-120, 0)


# ======================================================================
# o morro
# ======================================================================

def ring_rect(k, X0, Y0, S, tilt, lift, vs=1.0):
    w, e, hv = RINGS[k]
    hv *= vs
    uc, ru = (w + e) / 2, (e - w) / 2
    cx, cy = X0 + uc * S, Y0 - lift
    return skia.Rect.MakeLTRB(cx - ru * S, cy - hv * S * tilt, cx + ru * S, cy + hv * S * tilt)


def mountain(c, X0, Y0, S, a, tilt=1.0, gap=0.0, zh=70, labels=False, outline=None, fill=True, hi=None, vs=1.0):
    """tilt 1 = visto de cima (curvas de nível); tilt baixo = visto de lado (fatias empilhadas)."""
    if a <= 0:
        return
    side = 1 - tilt
    for k in range(4):
        lift = (zh * k + gap * k) * S * side
        thick = zh * S * side
        r = ring_rect(k, X0, Y0, S, tilt, lift, vs)
        if fill and thick > 0.5:
            wall = skia.Path()
            wall.addOval(skia.Rect.MakeLTRB(r.left(), r.top() + thick, r.right(), r.bottom() + thick))
            c.drawRect(skia.Rect.MakeLTRB(r.left(), r.centerY(), r.right(), r.centerY() + thick), paint(SIDE[k], a))
            c.drawPath(wall, paint(SIDE[k], a))
        if fill:
            c.drawOval(r, paint(LAYER[k], a * (1 - 0.75 * tilt) if tilt > 0.9 else a))
        col = outline or BROWN
        c.drawOval(r, paint((hi or {}).get(k, col), a, stroke=5 if tilt > 0.9 else 3))
        if labels:
            w, e, hv = RINGS[k]
            text_mid(c, str(100 * (k + 1)), X0 + e * S - 8, Y0 - lift - 14, 24, "black", BROWN, a, align="right")
    if tilt > 0.9:
        text_mid(c, "▲", X0 + SUMMIT[0] * S, Y0 + SUMMIT[1] * S, 30, "black", INK, a)


def u2x(u, X0, S):
    return X0 + u * S


# ======================================================================
# utilidades
# ======================================================================

def badge_row(c, t, rows, x, y0, dy, size=44):
    for k, (tc, s, col) in enumerate(rows):
        a, d = rise(t, tc)
        y = y0 + k * dy + d
        badge_num(c, k + 1, x, y - size * 0.36, a, 30, bg=col)
        text(c, s, x + 56, y, size, "black", INK, a, align="left")


def erro_tiles(c, t, items):
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
            text(c, ln, x + cw / 2, y + 250 + j * 58, 34, "black", INK, a)


def pause_badge(c, t, C, cue_on, cue_off, x=1390, y=170):
    ap = ep(t, C[cue_on], 0.5) * (1 - prog(t, C[cue_off] - 0.3, 0.4))
    if ap > 0:
        rrect(c, x, y, 340, 96, 24, AMBER, ap, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x + 28, y + 22, 14, 52), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 54, y + 22, 14, 52), paint(INK, ap))
        text_mid(c, "PAUSE E TENTE", x + 210, y + 48, 30, "black", INK, ap)


def alt_list(c, t, C, items, x, y0, dy, ok_cue, size=28, xmax=1760):
    """alternativas com o motivo da eliminação embaixo: items = [(letra, texto, cue_in, cue_x, motivo)]"""
    aok = ep(t, C[ok_cue], 0.5)
    for k, (L, s, cue_in, cue_x, why) in enumerate(items):
        a, d = rise(t, C[cue_in])
        y = y0 + k * dy + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, x - 40, y - 36, xmax - x + 20, dy - 12, 14, GREEN, 0.15 * aok)
        badge_num(c, L, x, y - 10, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, x + 40, y, size, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, x + 36, y - 10, x + 46 + text_w(s, "black", size), y - 10, ax, RED, ax)
            text(c, why, x + 40, y + 30, 21, "black", RED, ax, align="left")


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.2, 0.6)
    rrect(c, 230, 220, 760, 560, 10, "#FFFBEB", a0)
    c.drawRect(skia.Rect.MakeXYWH(230, 220, 760, 560), paint(INK2, a0, stroke=3)) if a0 > 0 else None
    mountain(c, 640, 500, 1.0, a0, labels=True)
    pill(c, "um papel PLANO", 610, 200, INK, size=24, a=ep(t, C["01.a"], 0.5), anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    hx, hy = u2x(-300, 640, 1.0), 500
    if ab > 0:
        rrect(c, hx - 22, hy - 18, 44, 34, 4, "#FFFFFF", ab); c.drawRect(skia.Rect.MakeXYWH(hx - 22, hy - 18, 44, 34), paint(INK, ab, stroke=3))
        p = skia.Path(); p.moveTo(hx - 30, hy - 18); p.lineTo(hx, hy - 44); p.lineTo(hx + 30, hy - 18); p.close(); c.drawPath(p, paint(RED, ab))
        c.drawCircle(hx, hy - 5, 60, paint(RED, ab * (0.5 + 0.5 * math.sin(t * 5)), stroke=5))
    pill(c, "PERIGOSO?", 1360, 380, RED, size=44, a=ab, anchor="center")
    pill(c, "Defesa Civil faz isso todo dia", 1360, 520, BLUE, size=30, a=ep(t, C["01.c"], 0.5), anchor="center")
    pill(c, "hoje: você também", 1360, 640, GREEN, size=30, a=ep(t, C["01.d"], 0.5), anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Ler o relevo\nnum mapa", C["02.a"], BLUE), ("2", "Achar morros\ne vales", C["02.b"], GREEN),
                     ("3", "Calcular a\ninclinação", C["02.c"], PURPLE)], cw=440, chh=400, title_size=38)
    pill(c, "ENCOSTA = o lado em rampa de um morro", W / 2, 760, BLUE, size=30, a=ep(t, C["02.c"] + 1.5, 0.5), anchor="center")


def b_altitude(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 1", "ALTITUDE", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["03.a"], 0.5)
    rrect(c, 200, 620, 1520, 200, 0, "#BAE6FD", a)
    hline(c, 200, 1720, 620, RIVER, a, 4)
    text(c, "nível do mar = 0 m", 240, 680, 30, "black", RIVER, a, align="left")
    p = skia.Path(); p.moveTo(900, 620); p.cubicTo(1050, 620, 1150, 300, 1250, 300); p.cubicTo(1350, 300, 1450, 620, 1600, 620); p.close()
    c.drawPath(p, paint("#86C18A", ep(t, C["03.c"], 0.5)))
    ac = ep(t, C["03.c"], 0.5)
    arrow(c, 1250, 620, 1250, 310, RED, ac, 5, 18); arrow(c, 1250, 310, 1250, 620, RED, ac, 5, 18)
    pill(c, "300 m de altitude", 1280, 450, RED, size=28, a=ac, bounds=(0, 1920))
    pill(c, "praia ≈ 0 m", 450, 560, INK, size=26, a=ep(t, C["03.b"], 0.5), anchor="center")
    pill(c, "ALTITUDE = altura em relação ao nível do mar", W / 2, 230, BLUE, size=30, a=a, anchor="center")


def b_escala(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 2", "A ESCALA (EPISÓDIO 1)", BLUE)
    card(c, *CARD_R)
    text(c, "1 : 50 000", W / 2, 320, 100, "black", INK, ep(t, C["04.a"], 0.5))
    text(c, "1 cm = 50 000 cm", W / 2, 450, 56, "black", INK2, ep(t, C["04.b"], 0.5))
    text(c, "corte 5 zeros: 0,5 km", W / 2, 560, 50, "black", GREEN, ep(t, C["04.c"], 0.5))
    result_box(c, "1 cm = 500 m", W / 2, 690, 60, ep(t, C["04.d"], 0.5), GREEN)


def b_porcento(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 3", "PORCENTAGEM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    text(c, "20% = 20 em cada 100", W / 2, 300, 70, "black", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    x0, y0, L = 460, 720, 1000
    p = skia.Path(); p.moveTo(x0, y0); p.lineTo(x0 + L, y0); p.lineTo(x0 + L, y0 - L * 0.2); p.close()
    c.drawPath(p, paint("#D6D3D1", ab)); c.drawPath(p, paint(INK2, ab, stroke=4))
    text(c, "100 m para a frente", x0 + L / 2, y0 + 50, 32, "black", INK2, ab)
    text(c, "sobe 20 m", x0 + L + 20, y0 - L * 0.1 + 10, 32, "black", RED, ab, align="left")


# ======================================================================
# bloco a: o que é curva de nível
# ======================================================================

def b_fatias(c, t, C, B):
    head(c, t, B["start"], "COMO DESENHAR UM MORRO", "NUMA FOLHA PLANA?", AMBER)
    card(c, *CARD_R)
    X0, Y0, S = 700, 640, 1.0
    rise_cam = ease_io(ep(t, C["07.d"], 2.2))
    tilt = lerp(0.32, 1.0, rise_cam)
    gap = 30 * ep(t, C["06.b"], 1.0) * (1 - rise_cam)
    Yc = lerp(Y0, 495, rise_cam)
    mountain(c, X0, Yc, S, ep(t, C["06.a"], 0.6), tilt=tilt, gap=gap, labels=False)
    ab = ep(t, C["06.b"], 0.5) * (1 - rise_cam)
    for k in range(4):
        y = Yc - (70 * k + gap * k) * (1 - tilt) - 6
        text(c, f"{100 * (k + 1)} m", u2x(RINGS[k][1], X0, S) + 30, y, 28, "black", BROWN, ab * ep(t, C["06.b"] + 0.3 * k, 0.4), align="left")
    pill(c, "fatias de MESMA altura", 1440, 260, AMBER, size=26, a=ab, anchor="center")
    pill(c, "cada corte deixa uma BORDA", 1440, 340, INK, size=24, a=ep(t, C["06.c"], 0.5) * (1 - rise_cam), anchor="center")
    pill(c, "visto de CIMA", 1440, 260, PURPLE, size=28, a=ep(t, C["07.d"] + 1.2, 0.5), anchor="center")
    if rise_cam > 0.95:
        mountain(c, X0, Yc, S, ep(t, C["07.e"], 0.5), labels=True, fill=False)
    pill(c, "CURVA DE NÍVEL = linha de MESMA altitude", 1360, 700, BLUE, size=28, a=ep(t, C["07.f"], 0.5), anchor="center")
    pill(c, "também chamada de ISOÍPSA", 1360, 780, BLUE, size=24, a=ep(t, C["07.f"] + 2.5, 0.5), anchor="center")


def b_equidistancia(c, t, C, B):
    head(c, t, B["start"], "EQUIDISTÂNCIA", "A ALTURA DE CADA DEGRAU", BLUE)
    card(c, *CARD_R)
    X0, Y0 = 640, 520
    mountain(c, X0, Y0, 1.0, 1, labels=True)
    aa = ep(t, C["08.a"], 0.5)
    pill(c, "EQUIDISTÂNCIA = diferença de altura entre curvas vizinhas", 1300, 300, BLUE, size=24, a=aa, anchor="center",
         bounds=(0, 1920))
    ab = ep(t, C["08.b"], 0.5)
    text(c, "100 → 200 → 300 → 400", 1300, 420, 44, "black", BROWN, ab)
    text(c, "sempre 100 m", 1300, 480, 36, "black", GREEN, ab)
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "DESNÍVEL = diferença de altura entre 2 pontos", 1300, 620, BLUE, size=24, a=ac, anchor="center", bounds=(0, 1920))
    text(c, "ex.: de 100 a 400 m → desnível de 300 m", 1300, 700, 28, "black", INK2, ac)


# ======================================================================
# bloco b: a escada (próximas x espaçadas)
# ======================================================================

def stairs(c, x, y, tread, rise_h, n, col, a):
    p = skia.Path(); p.moveTo(x, y)
    for k in range(n):
        p.lineTo(x + k * tread, y - (k + 1) * rise_h); p.lineTo(x + (k + 1) * tread, y - (k + 1) * rise_h)
    p.lineTo(x + n * tread, y); p.close()
    c.drawPath(p, paint(col, a * 0.35)); c.drawPath(p, paint(col, a, stroke=4))


def b_escada(c, t, C, B):
    head(c, t, B["start"], "PENSE NUMA ESCADA", "TODO DEGRAU TEM A MESMA ALTURA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    pill(c, "todo degrau: MESMA altura", W / 2, 220, INK, size=28, a=aa, anchor="center")
    ab = ep(t, C["09.b"], 0.5)
    stairs(c, 260, 660, 50, 80, 5, RED, ab)
    for k in range(5):
        line(c, 260 + k * 50, 720, 260 + k * 50, 760, RED, ab, 4)
    text(c, "vista de cima: colados", 385, 800, 26, "black", RED, ab)
    pill(c, "ÍNGREME", 385, 280, RED, size=32, a=ab, anchor="center")
    ac = ep(t, C["09.c"], 0.5)
    stairs(c, 900, 660, 160, 80, 5, GREEN, ac)
    for k in range(5):
        line(c, 900 + k * 160, 720, 900 + k * 160, 760, GREEN, ac, 4)
    text(c, "vista de cima: espaçados", 1300, 800, 26, "black", GREEN, ac)
    pill(c, "RAMPA SUAVE", 1300, 280, GREEN, size=32, a=ac, anchor="center")


def b_declive(c, t, C, B):
    head(c, t, B["start"], "AS CURVAS SÃO OS DEGRAUS", "PRÓXIMAS x ESPAÇADAS", PURPLE)
    card(c, *CARD_R)
    X0, Y0 = 760, 500
    aa, ab = ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5)
    mountain(c, X0, Y0, 1.2, 1, labels=True)
    rrect(c, u2x(-340, X0, 1.2) - 20, 420, 190, 160, 18, RED, 0.15 * aa)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(u2x(-340, X0, 1.2) - 20, 420, 190, 160), 18, 18), paint(RED, aa, stroke=5)) if aa > 0 else None
    pill(c, "PRÓXIMAS: declive FORTE", 300, 300, RED, size=26, a=aa, anchor="center", bounds=(0, 1920))
    rrect(c, u2x(90, X0, 1.2), 420, 330, 160, 18, GREEN, 0.15 * ab)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(u2x(90, X0, 1.2), 420, 330, 160), 18, 18), paint(GREEN, ab, stroke=5)) if ab > 0 else None
    pill(c, "ESPAÇADAS: declive SUAVE", 1450, 300, GREEN, size=26, a=ab, anchor="center", bounds=(0, 1920))
    pill(c, "DECLIVE = inclinação do terreno", W / 2, 800, BLUE, size=28, a=ep(t, C["10.c"], 0.5), anchor="center")


# ======================================================================
# blocos c, d, e: morro x depressão, vale, nunca se cruzam
# ======================================================================

def rings_simple(c, cx, cy, labels, col, a):
    for k, lab in enumerate(labels):
        rx, ry = 240 - 55 * k, 170 - 38 * k
        c.drawOval(skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry), paint(col, a, stroke=4))
        text_mid(c, lab, cx + rx - 6, cy - 16, 22, "black", col, a, align="right")


def b_morro(c, t, C, B):
    head(c, t, B["start"], "ANÉIS FECHADOS", "MORRO OU DEPRESSÃO?", BLUE)
    card(c, *CARD_R)
    aa, ab = ep(t, C["11.a"], 0.5), ep(t, C["11.b"], 0.5)
    rings_simple(c, 540, 470, ["100", "200", "300", "400"], BROWN, aa)
    text_mid(c, "▲", 540, 470, 34, "black", INK, ab)
    pill(c, "números CRESCEM para dentro", 540, 700, BROWN, size=26, a=aa, anchor="center")
    pill(c, "MORRO", 540, 770, GREEN, size=34, a=ab, anchor="center")
    ac, ad = ep(t, C["11.c"], 0.5), ep(t, C["11.d"], 0.5)
    rings_simple(c, 1380, 470, ["400", "300", "200", "100"], RIVER, ac)
    pill(c, "números DIMINUEM para dentro", 1380, 700, RIVER, size=26, a=ac, anchor="center")
    pill(c, "DEPRESSÃO (um buraco)", 1380, 770, AMBER, size=34, a=ad, anchor="center")


def b_vale(c, t, C, B):
    head(c, t, B["start"], "ONDE PASSA O RIO?", "O VALE", BLUE)
    card(c, *CARD_R)
    cx = 720
    aa = ep(t, C["12.a"], 0.5)
    ab = ep(t, C["12.b"], 0.5)
    for k, lab in enumerate(("100", "200", "300", "400")):
        y = 720 - k * 130
        a = ab * ep(t, C["12.b"] + 0.3 * k, 0.4)
        p = skia.Path(); p.moveTo(cx - 420, y - 60); p.quadTo(cx - 60, y - 40, cx, y - 150); p.quadTo(cx + 60, y - 40, cx + 420, y - 60)
        c.drawPath(p, paint(BROWN, a, stroke=4))
        text_mid(c, lab, cx + 440, y - 60, 24, "black", BROWN, a, align="left")
    ac = ep(t, C["12.c"], 0.5)
    arrow(c, cx + 120, 300, cx + 20, 230, AMBER, ac, 5, 18)
    pill(c, "a ponta do V aponta para os números MAIORES", cx + 280, 330, AMBER, size=22, a=ac, bounds=(0, 1920))
    ad = ep(t, C["12.d"], 0.5)
    river = skia.Path(); river.moveTo(cx, 200); river.cubicTo(cx + 10, 400, cx - 10, 600, cx, 830)
    if ad > 0:
        meas = skia.PathMeasure(river, False); seg = skia.Path(); meas.getSegment(0, meas.getLength() * ad, seg, True)
        c.drawPath(seg, paint(RIVER, 1, stroke=10, cap_round=True))
    pill(c, "VALE = parte baixa entre morros", 1460, 230, BLUE, size=24, a=aa, anchor="center")
    pill(c, "o rio corre no meio do V", 1460, 500, RIVER, size=26, a=ad, anchor="center")
    ae, af = ep(t, C["13.e"], 0.5), ep(t, C["13.f"], 0.5)
    pill(c, "MONTANTE: rio acima (nascente)", 1460, 620, BLUE, size=24, a=ae, anchor="center")
    pill(c, "JUSANTE: rio abaixo", 1460, 720, BLUE, size=24, a=af, anchor="center")
    arrow(c, cx - 60, 780, cx - 60, 820, RIVER, af, 5, 16)


def b_cruzam(c, t, C, B):
    head(c, t, B["start"], "PODEM SE CRUZAR?", "NUNCA", RED)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    p1 = skia.Path(); p1.moveTo(240, 650); p1.cubicTo(450, 300, 650, 300, 860, 400)
    p2 = skia.Path(); p2.moveTo(240, 360); p2.cubicTo(450, 620, 650, 640, 860, 560)
    c.drawPath(p1, paint(BROWN, aa, stroke=5)); c.drawPath(p2, paint(BROWN, aa, stroke=5))
    text(c, "100 m", 870, 410, 28, "black", BROWN, aa, align="left"); text(c, "200 m", 870, 570, 28, "black", BROWN, aa, align="left")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        c.drawCircle(505, 470, 18, paint(RED, ab))
    pill(c, "100 m E 200 m ao mesmo tempo?!", 505, 250, RED, size=26, a=ab, anchor="center")
    check_icon(c, 505, 760, 34, ep(t, C["14.c"], 0.5), RED, "x")
    ad = ep(t, C["14.d"], 0.5)
    rrect(c, 1200, 260, 120, 520, 6, "#A8A29E", ad)
    for k in range(4):
        line(c, 1180, 320 + k * 120, 1330 + k * 60, 320 + k * 120, BROWN, ad, 4)
        line(c, 1330 + k * 60, 320 + k * 120, 1600, 320 + k * 120 + 60, BROWN, ad, 4)
    pill(c, "paredão: podem ENCOSTAR", 1420, 230, AMBER, size=26, a=ad, anchor="center")
    pill(c, "cruzar: NUNCA", 1420, 800, RED, size=30, a=ad, anchor="center")


# ======================================================================
# recapitulação (meio e fim)
# ======================================================================

def b_recap(c, t, C, B):
    sid = "15" if B["start"] < C["32"] - 1 else "32"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    badge_row(c, t, [(C[sid + ".a"], "Curva de nível: pontos de MESMA altitude", BLUE),
                     (C[sid + ".b"], "Curvas PRÓXIMAS = terreno ÍNGREME", RED),
                     (C[sid + ".c"], "Declividade = desnível ÷ distância × 100", GREEN)], 220, 330, 160, 42)
    text(c, "(na MESMA unidade)", 276, 700, 34, "black", AMBER, ep(t, C[sid + ".c"] + 1.5, 0.5), align="left")


# ======================================================================
# bloco f: perfil topográfico
# ======================================================================

def b_perfil(c, t, C, B):
    head(c, t, B["start"], "PERFIL TOPOGRÁFICO", "O MORRO VISTO DE LADO", BLUE)
    card(c, *CARD_R)
    X0, Y0, S = 860, 320, 1.3
    mountain(c, X0, Y0, S, 1, labels=True, fill=False, vs=0.45)
    xa, xb = u2x(-380, X0, S), u2x(380, X0, S)
    ab = ep(t, C["16.b"], 0.5)
    line(c, xa, Y0, xa + (xb - xa) * ep(t, C["16.b"], 1.0), Y0, RED, ab, 5)
    text_mid(c, "A", xa - 30, Y0, 36, "black", RED, ab); text_mid(c, "B", xb + 30, Y0, 36, "black", RED, ab)
    pill(c, "cortar o morro de A até B", 360, 220, INK, size=24, a=ep(t, C["16.a"], 0.5), anchor="center")
    gy0, gy1 = 800, 520            # base do gráfico (0 m) e topo (400 m)
    Hy = lambda m: gy0 - (gy0 - gy1) * m / 400
    ac = ep(t, C["16.c"], 0.5)
    line(c, xa, gy0, xb, gy0, INK2, ac, 3); line(c, xa, gy0, xa, gy1 - 20, INK2, ac, 3)
    for m in (100, 200, 300, 400):
        hline(c, xa, xb, Hy(m), LINE, ac, 2)
        text(c, f"{m}", xa - 12, Hy(m) + 8, 22, "bold", GRAY, ac, align="right")
    pts = []
    order = [(RINGS[k][0], k) for k in range(4)] + [(RINGS[k][1], k) for k in reversed(range(4))]
    for j, (u, k) in enumerate(order):
        x = u2x(u, X0, S)
        a = ac * ep(t, C["16.c"] + 0.35 * j, 0.4)
        if a > 0:
            c.drawCircle(x, Y0, 9, paint(RED, a))
            line(c, x, Y0 + 10, x, Hy(100 * (k + 1)), GRAY, a * 0.7, 2, dash=(8, 6))
            c.drawCircle(x, Hy(100 * (k + 1)), 9, paint(BROWN, a))
        pts.append((x, Hy(100 * (k + 1))))
    ad = ep(t, C["17.d"], 1.5)
    if ad > 0:
        prof = skia.Path(); prof.moveTo(xa, gy0)
        prof.lineTo(*pts[0])
        for k in range(1, 4):
            prof.lineTo(*pts[k])
        sx = u2x(SUMMIT[0], X0, S)
        prof.quadTo(sx, Hy(440), pts[4][0], pts[4][1])
        for p in pts[5:]:
            prof.lineTo(*p)
        prof.lineTo(xb, gy0)
        meas = skia.PathMeasure(prof, False); seg = skia.Path(); meas.getSegment(0, meas.getLength() * ad, seg, True)
        c.drawPath(seg, paint("#4D7C0F", 1, stroke=6, cap_round=True))
    pill(c, "PERFIL TOPOGRÁFICO = o morro visto de lado", 1450, 470, BLUE, size=22, a=ep(t, C["17.e"], 0.5), anchor="center",
         bounds=(0, 1920))
    af = ep(t, C["17.f"], 0.5)
    pill(c, "colado → EM PÉ", xa + 40, gy1 - 60, RED, size=22, a=af, bounds=(0, 1920))
    pill(c, "espaçado → DEITADO", xb - 40, gy1 + 40, GREEN, size=22, a=af, anchor="right", bounds=(0, 1920))


# ======================================================================
# blocos g e h: declividade e risco
# ======================================================================

def triangle(c, x0, y0, L, Hh, a, lab_h, lab_v):
    p = skia.Path(); p.moveTo(x0, y0); p.lineTo(x0 + L, y0); p.lineTo(x0 + L, y0 - Hh); p.close()
    c.drawPath(p, paint("#D6D3D1", a)); c.drawPath(p, paint(INK2, a, stroke=4))
    text(c, lab_h, x0 + L / 2, y0 + 48, 30, "black", BLUE, a)
    text(c, lab_v, x0 + L + 16, y0 - Hh / 2 + 10, 30, "black", RED, a, align="left")


def b_declividade(c, t, C, B):
    head(c, t, B["start"], "DECLIVIDADE", "A INCLINAÇÃO EM NÚMERO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    pill(c, "DECLIVIDADE = inclinação em porcentagem", W / 2, 220, BLUE, size=28, a=aa, anchor="center")
    ab = ep(t, C["18.b"], 0.5)
    seq(c, [("declividade =", INK), ("FRAC", "desnível", "distância horizontal", INK)], 820, 400, 52, ab)
    ac = ep(t, C["18.c"], 0.5)
    text(c, "× 100%", 1390, 400, 52, "black", INK, ac, align="left")
    triangle(c, 400, 720, 700, 180, ab, "distância horizontal", "desnível")
    pill(c, "MESMA unidade: metro com metro", 1450, 790, AMBER, size=26, a=ep(t, C["18.d"], 0.5), anchor="center")


def b_conta(c, t, C, B):
    head(c, t, B["start"], "VAMOS CALCULAR", "PASSO A PASSO", GREEN)
    card(c, *CARD_R)
    rows = [("19.a", "1 : 50 000 · 4 cm no mapa", INK), ("19.b", "4 × 500 m = 2 000 m", BLUE),
            ("19.c", "curvas de 200 m e 600 m", INK), ("19.d", "600 − 200 = 400 m de desnível", RED)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        text(c, s, 230, 280 + k * 90 + d, 40, "black", col, a, align="left")
    ae = ep(t, C["20.e"], 0.5)
    seq(c, [("FRAC", "400 m", "2 000 m", INK), ("= 0,2", INK)], 1350, 360, 56, ae)
    result_box(c, "0,2 × 100 = 20%", 1350, 530, 54, ep(t, C["20.f"], 0.5), GREEN)
    ag = ep(t, C["20.g"], 0.5)
    triangle(c, 1120, 760, 420, 84, ag, "100 m", "20 m")


def b_risco(c, t, C, B):
    head(c, t, B["start"], "POR QUE IMPORTA", "RISCO DE DESLIZAMENTO", RED)
    card(c, *CARD_R)
    aa = ep(t, C["21.a"], 0.5)
    p = skia.Path(); p.moveTo(220, 800); p.lineTo(900, 800); p.lineTo(900, 330); p.close()
    c.drawPath(p, paint("#D6B98C", aa)); c.drawPath(p, paint(BROWN, aa, stroke=4))
    for k, (hx, hy) in enumerate(((560, 640), (700, 550), (820, 470))):
        c.save(); c.translate(hx, hy); c.rotate(-34)
        rrect(c, -26, -40, 52, 40, 4, "#FFFFFF", aa); c.drawRect(skia.Rect.MakeXYWH(-26, -40, 52, 40), paint(INK, aa, stroke=3)) if aa > 0 else None
        tri = skia.Path(); tri.moveTo(-34, -40); tri.lineTo(0, -70); tri.lineTo(34, -40); tri.close(); c.drawPath(tri, paint(RED, aa))
        c.restore()
    for k in range(14):
        xx = 260 + ((k * 97 + t * 260) % 640); yy = 200 + ((k * 53 + t * 420) % 300)
        line(c, xx, yy, xx - 10, yy + 28, RIVER, aa * 0.7, 3)
    ab = ep(t, C["21.b"], 0.5)
    pill(c, "Lei 6.766/1979", 1340, 300, BLUE, size=34, a=ab, anchor="center")
    ac = ep(t, C["21.c"], 0.5)
    result_box(c, "≥ 30%: proibido lotear", 1340, 450, 46, ac, RED)
    text(c, "salvo exigências específicas", 1340, 540, 28, "black", INK2, ac)
    pill(c, "a conta da Defesa Civil", 1340, 680, GREEN, size=30, a=ep(t, C["21.d"], 0.5), anchor="center")


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "CURVAS PRÓXIMAS = PLANO?", RED)
    erro_tiles(c, t, [(C["22.a"], "O ERRO", ["curvas próximas", "= terreno plano"], RED),
                      (C["22.b"], "POR QUE PARECE CERTO", ["linhas juntinhas", "parecem \"tranquilas\""], AMBER),
                      (C["22.c"], "A CORREÇÃO", ["degraus colados:", "escada ÍNGREME"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "ALTITUDE NO LUGAR DO DESNÍVEL", RED)
    erro_tiles(c, t, [(C["23.a"], "O ERRO", ["usar 600 m", "(o ponto mais alto)"], RED),
                      (C["23.b"], "POR QUE PARECE CERTO", ["é o número que", "aparece no mapa"], AMBER),
                      (C["23.c"], "A CORREÇÃO", ["o quanto SUBIU:", "600 − 200 = 400 m"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "METRO DIVIDIDO POR CENTÍMETRO", RED)
    erro_tiles(c, t, [(C["24.a"], "O ERRO", ["400 m ÷ 4 cm"], RED),
                      (C["24.b"], "POR QUE PARECE CERTO", ["os números já", "estão prontos"], AMBER),
                      (C["24.c"], "A CORREÇÃO", ["converta antes:", "4 cm = 2 000 m"], GREEN)])


def b_erro4(c, t, C, B):
    head(c, t, B["start"], "ERRO 4", "CURVAS QUE SE CRUZAM", RED)
    erro_tiles(c, t, [(C["25.a"], "O ERRO", ["curvas de nível", "podem se cruzar"], RED),
                      (C["25.b"], "POR QUE PARECE CERTO", ["no desenho são", "só linhas"], AMBER),
                      (C["25.c"], "A CORREÇÃO", ["cada linha é uma", "altitude: um ponto", "não tem duas"], GREEN)])


# ======================================================================
# questões estilo ENEM
# ======================================================================

def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "DUAS TRILHAS ATÉ O CUME", BLUE)
    card(c, *CARD_R)
    X0, Y0, S = 470, 490, 0.85
    ae = ep(t, C["26.e1"], 0.5)
    mountain(c, X0, Y0, S, ae, labels=True, fill=False)
    sx, sy = u2x(SUMMIT[0], X0, S), Y0
    a1 = ep(t, C["26.e2"], 0.5)
    w0 = u2x(RINGS[0][0], X0, S)
    line(c, w0, Y0, sx - 14, sy, RED, a1, 6)
    pill(c, "trilha 1", w0 - 10, Y0 + 50, RED, size=22, a=a1, anchor="center", bounds=(0, 1920))
    a2 = ep(t, C["26.e3"], 0.5)
    e0 = u2x(RINGS[0][1], X0, S)
    p = skia.Path(); p.moveTo(e0, Y0); p.cubicTo(e0 - 80, Y0 + 90, sx + 140, Y0 + 70, sx + 14, sy)
    pd = paint(BLUE, a2, stroke=6); pd.setPathEffect(skia.DashPathEffect.Make([16, 10], 0)); c.drawPath(p, pd)
    pill(c, "trilha 2", e0, Y0 + 60, BLUE, size=22, a=a2, anchor="center", bounds=(0, 1920))
    text(c, "equidistância: 100 m · N ↑", X0, 790, 24, "black", GRAY, ae)
    items = [("A", "trilha 2 mais íngreme: curvas mais largas", "27.a", "28.a", "curvas largas = terreno SUAVE"),
             ("B", "mesma inclinação: mesmo desnível", "27.b", "28.b", "inclinação depende da DISTÂNCIA também"),
             ("C", "trilha 2 vence desnível maior: é mais longa", "27.c", "28.c", "as duas sobem de 100 m ao cume"),
             ("D", "oeste mais suave: curvas próximas", "27.d", "28.d", "curvas próximas = ÍNGREME"),
             ("E", "trilha 1 mais íngreme: mesmo desnível, menos distância", "27.e", None, "")]
    alt_list(c, t, C, items, 880, 250, 112, "28.e", 26)
    pause_badge(c, t, C, "27.p", "28.t", x=1400, y=700)


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "A DECLIVIDADE DA ENCOSTA", BLUE)
    card(c, *CARD_R)
    for k, (cue, s) in enumerate((("29.e1", "Carta 1 : 50 000"), ("29.e2", "Curvas de 200 m e 600 m"), ("29.e3", "4 cm entre os pontos · declividade?"))):
        text(c, s, 210, 240 + k * 52, 34, "black", INK if k < 2 else BLUE, ep(t, C[cue], 0.5), align="left")
    items = [("A", "0,2%", "30.a", "31.a", "dividiu metro por centímetro"), ("B", "2%", "30.b", "31.b", "errou a conversão: 20 000 m"),
             ("C", "20%", "30.c", None, ""), ("D", "30%", "30.d", "31.d", "usou 600 m, não o desnível"),
             ("E", "200%", "30.e", "31.e", "usou só 200 m de distância")]
    alt_list(c, t, C, items, 250, 440, 84, "31.c", 32, xmax=900)
    at = ep(t, C["31.t"], 0.5)
    rrect(c, 1010, 420, 700, 360, 20, GREEN, 0.08 * at)
    for k, s in enumerate(("4 × 500 m = 2 000 m", "600 − 200 = 400 m", "400 ÷ 2 000 × 100")):
        text(c, s, 1360, 490 + k * 80, 40, "black", INK, at * ep(t, C["31.t"] + 0.8 * k, 0.4))
    result_box(c, "= 20%", 1360, 720, 52, ep(t, C["31.t"] + 2.6, 0.5), GREEN)
    pause_badge(c, t, C, "30.p", "31.t")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MAPAS TEMÁTICOS E ANAMORFOSES", PURPLE)
    R = (260, 200, 1400, 560)
    at = ep(t, C["33.t"], 0.5)
    mapas.draw_world(c, R, at)
    g = ep(t, C["33.a"], 2.0)
    for nome, col in (("India", AMBER), ("China", RED)):
        rings = mapas._country_rings(nome)
        pts = [mapas.to_xy(R, p) for r in rings for p in r]
        cx, cy = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
        s = 1 + 1.4 * g
        c.save(); c.translate(cx, cy); c.scale(s, s); c.translate(-cx, -cy)
        mapas.draw_country_on(c, nome, R, at, fill=col, stroke=INK2)
        c.restore()
    pill(c, "e se o tamanho fosse a POPULAÇÃO?", W / 2, 800, AMBER, size=30, a=ep(t, C["33.a"], 0.5), anchor="center")
    pill(c, "EPISÓDIO 5: MAPAS TEMÁTICOS E ANAMORFOSES", W / 2, 860, PURPLE, size=28, a=ep(t, C["33.b"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "A sua rua tem mais de 30%?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, altitude=b_altitude, escala=b_escala, porcento=b_porcento, fatias=b_fatias,
              equidistancia=b_equidistancia, escada=b_escada, declive=b_declive, morro=b_morro, vale=b_vale, cruzam=b_cruzam,
              recap=b_recap, perfil=b_perfil, declividade=b_declividade, conta=b_conta, risco=b_risco, erro1=b_erro1,
              erro2=b_erro2, erro3=b_erro3, erro4=b_erro4, q7=b_q7, q8=b_q8, ponte=b_ponte, cta=b_cta)
