"""Visual — Cartografia, Episódio 2: Coordenadas geográficas e orientação (aula para iniciantes, tema claro).
Cores com função: azul = definição · âmbar = atenção/armadilha · verde = atalho/dica · vermelho = erro.
Mapas e globo com dados reais (_ferramentas/mapas.py).
"""
import math
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep2_coordenadas_orientacao.mp4"
CARD_R = (140, 150, 1640, 690)
SEA = "#DBEAFE"
NORTE_C, SUL_C = "#DBEAFE", "#DCFCE7"
WORLD = (220, 200, 1480, 560)   # retângulo padrão do mapa-múndi


# ======================================================================
# utilidades
# ======================================================================

def spin(t, t0, speed=12.0, base=-50.0):
    """longitude central de um globo girando devagar"""
    return base + speed * (t - t0)


def arc(c, cx, cy, r, start, sweep, col, a, w=4):
    if a > 0:
        c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), start, sweep, False, paint(col, a, stroke=w))


def wedge(c, cx, cy, r, start, sweep, col, a):
    if a > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), start, sweep, False); p.close()
        c.drawPath(p, paint(col, a))


def phone(c, x, y, w, h, a):
    rrect(c, x, y, w, h, 48, INK, a, shadow=True)
    return x + 20, y + 56, w - 40, h - 112


def badge_row(c, t, rows, x, y0, dy, size=46):
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
            text(c, ln, x + cw / 2, y + 250 + j * 58, 36, "black", INK, a)


def alts(c, t, C, items, x, y0, dy, size=32, ok_cue=None, why_x=None):
    """alternativas: items = [(letra, texto, cue_aparece, cue_elimina, motivo)]"""
    aok = ep(t, C[ok_cue], 0.5) if ok_cue else 0
    for k, (L, s, cue_in, cue_x, why) in enumerate(items):
        a, d = rise(t, C[cue_in])
        y = y0 + k * dy + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, x - 40, y - size * 1.05, (why_x or 1720) - x + 60, size * 1.9, 14, GREEN, 0.15 * aok)
        badge_num(c, L, x, y - size * 0.32, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, x + 44, y, size, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, x + 40, y - size * 0.3, x + 50 + text_w(s, "black", size), y - size * 0.3, ax, RED, ax)
            if why and why_x:
                text(c, why, why_x, y, 24, "black", RED, ax, align="right")


def pause_badge(c, t, C, cue_on, cue_off, x=1380, y=180):
    ap = ep(t, C[cue_on], 0.5) * (1 - prog(t, C[cue_off] - 0.3, 0.4))
    if ap > 0:
        rrect(c, x, y, 350, 100, 24, AMBER, ap, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x + 30, y + 24, 14, 52), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 56, y + 24, 14, 52), paint(INK, ap))
        text_mid(c, "PAUSE E TENTE", x + 215, y + 50, 30, "black", INK, ap)


def lat_axis(c, x, ytop, ybot, lat_top, lat_bot, a):
    """eixo vertical de latitudes (norte em cima), com o Equador destacado; devolve Y(lat)"""
    Y = lambda L: ytop + (lat_top - L) / (lat_top - lat_bot) * (ybot - ytop)
    line(c, x, ytop, x, ybot, INK2, a, 5)
    for L in range(int(lat_bot), int(lat_top) + 1, 5):
        line(c, x - 12, Y(L), x + 12, Y(L), INK2, a, 3)
        lab = "0°" if L == 0 else f"{abs(L)}° {'N' if L > 0 else 'S'}"
        text(c, lab, x - 26, Y(L) + 9, 24, "bold", BLUE if L == 0 else GRAY, a, align="right")
    hline(c, x - 160, x + 420, Y(0), BLUE, a, 4, (14, 10))
    text(c, "Equador", x + 430, Y(0) + 9, 26, "black", BLUE, a, align="left")
    return Y


def grid_coords(c, gx, gy, gw, gh, a, lons=(60, 50, 40, 30), lats=(0, 10, 20, 30)):
    """grade simples de latitude (sul) e longitude (oeste); devolve (X(lon), Y(lat))"""
    X = lambda lon: gx + (lons[0] - lon) / (lons[0] - lons[-1]) * gw
    Y = lambda lat: gy + (lat - lats[0]) / (lats[-1] - lats[0]) * gh
    for lon in lons:
        line(c, X(lon), gy, X(lon), gy + gh, LINE, a, 2)
        text(c, f"{lon}° O", X(lon), gy + gh + 40, 24, "bold", GRAY, a)
    for lat in lats:
        line(c, gx, Y(lat), gx + gw, Y(lat), LINE, a, 2)
        text(c, f"{lat}° S" if lat else "0°", gx - 14, Y(lat) + 8, 24, "bold", GRAY, a, align="right")
    return X, Y


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    st = B["start"]
    a0 = ep(t, st + 0.2, 0.6)
    sx, sy, sw, sh = phone(c, 760, 170, 400, 620, a0)
    if a0 > 0:
        c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(sx, sy, sw, sh), 20, 20), True)
        mapas.draw_world(c, (sx - 120, sy - 40, sw + 240, sh + 80), a0, lon=(-58, -35), lat=(-33, -12), frame=False, radius=0,
                         arquivo="ne_50m_land.geojson")
        c.restore()
    aa = ep(t, C["01.a"], 0.4)
    px, py = sx + sw * 0.62, sy + sh * 0.62
    if aa > 0:
        c.drawCircle(px, py, 30 + 10 * math.sin(t * 4), paint(BLUE, aa * 0.25))
        c.drawCircle(px, py, 14, paint(BLUE, aa)); c.drawCircle(px, py, 14, paint("#FFFFFF", aa, stroke=4))
    pill(c, "VOCÊ", px, py - 50, BLUE, size=24, a=aa, anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    pill(c, "23° S", 470, 420, BLUE, size=54, a=ab, anchor="center")
    pill(c, "46° O", 1450, 420, BLUE, size=54, a=ep(t, C["01.b"] + 0.4, 0.5), anchor="center")
    text(c, "só 2 números", 960, 860, 40, "black", INK, ab)
    text_mid(c, "?", 470, 560, 90, "black", AMBER, ep(t, C["01.c"], 0.5))
    text_mid(c, "?", 1450, 560, 90, "black", AMBER, ep(t, C["01.c"], 0.5))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Localizar qualquer\nponto da Terra", C["02.a"], BLUE), ("2", "Calcular a\ndistância", C["02.b"], GREEN),
                     ("3", "Descobrir\na direção", C["02.c"], PURPLE)], cw=440, chh=400, title_size=36)


def b_grau(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 1", "O QUE É GRAU", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    cx, cy, r = 360, 470, 150
    if aa > 0:
        c.drawCircle(cx, cy, r, paint("#FFFFFF", aa))
        c.drawCircle(cx, cy, r, paint(INK2, aa, stroke=5))
        for k in range(12):
            ang = math.radians(k * 30)
            line(c, cx + (r - 18) * math.cos(ang), cy + (r - 18) * math.sin(ang), cx + r * math.cos(ang), cy + r * math.sin(ang), INK2, aa, 3)
    sweep = 60 * ep(t, C["03.a"] + 0.5, 1.0)
    wedge(c, cx, cy, r - 30, -90, sweep, BLUE, aa * 0.25)
    line(c, cx, cy, cx, cy - r + 25, INK, aa, 8)
    ang = math.radians(-90 + sweep)
    line(c, cx, cy, cx + (r - 45) * math.cos(ang), cy + (r - 45) * math.sin(ang), INK, aa, 8)
    pill(c, "GRAU = medida de uma ABERTURA", cx, 700, BLUE, size=24, a=aa, anchor="center")
    for k, (cue, sw, lab, col) in enumerate((("03.b", 360, "volta inteira: 360°", GREEN), ("03.c", 180, "meia volta: 180°", PURPLE),
                                             ("03.d", 90, "um quarto: 90°", AMBER))):
        a = ep(t, C[cue], 0.5)
        x = 820 + k * 330
        if a > 0:
            c.drawCircle(x, 450, 110, paint(INK2, a, stroke=3))
            wedge(c, x, 450, 110, -90, sw * ep(t, C[cue], 1.0), col, a * 0.6)
            if sw == 90:
                c.drawRect(skia.Rect.MakeXYWH(x, 424, 26, 26), paint(INK, a, stroke=3))
        text(c, lab, x, 620, 30, "black", col, a)


def b_terra(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 2", "A TERRA GIRA EM UM EIXO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    cx, cy, r = 760, 495, 280
    mapas.draw_globe(c, cx, cy, r, aa, lon0=spin(t, B["start"], 25), lat0=12)
    top, bot = mapas.globe_xy(0, 90, cx, cy, r, 0, 12), mapas.globe_xy(0, -90, cx, cy, r, 0, 12)
    line(c, top[0], top[1] - 70, bot[0], bot[1] + 70, RED, aa, 5, dash=(14, 10))
    pill(c, "EIXO", cx + 40, top[1] - 80, RED, size=24, a=aa)
    arc(c, cx, top[1] - 40, 60, 200, 140, INK2, aa, 4)
    ab = ep(t, C["04.b"], 0.5)
    for (x, y, _), lab in ((top, "POLO NORTE"), (bot, "POLO SUL")):
        if ab > 0:
            c.drawCircle(x, y, 12, paint(BLUE, ab))
        pill(c, lab, x + 230, y, BLUE, size=28, a=ab, anchor="center")


# ======================================================================
# âncora: batalha naval
# ======================================================================

def b_batalha(c, t, C, B):
    head(c, t, B["start"], "LEMBRA DA BATALHA NAVAL?", "LINHA + COLUNA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    gx, gy, cs = 300, 230, 64
    for i in range(9):
        line(c, gx + i * cs, gy, gx + i * cs, gy + 8 * cs, "#93C5FD", aa, 2)
        line(c, gx, gy + i * cs, gx + 8 * cs, gy + i * cs, "#93C5FD", aa, 2)
    for k in range(8):
        text_mid(c, "ABCDEFGH"[k], gx - 30, gy + k * cs + cs / 2, 28, "black", INK2, aa)
        text_mid(c, str(k + 1), gx + k * cs + cs / 2, gy - 26, 28, "black", INK2, aa)
    ab = ep(t, C["05.b"], 0.5)
    rrect(c, gx, gy + cs, 8 * cs, cs, 0, BLUE, 0.15 * ab)
    rrect(c, gx + 4 * cs, gy, cs, 8 * cs, 0, GREEN, 0.15 * ab)
    ac = ep(t, C["05.c"], 0.5)
    if ac > 0:
        cx, cy = gx + 4.5 * cs, gy + 1.5 * cs
        for k in range(8):
            ang = k * math.pi / 4 + t
            line(c, cx, cy, cx + 40 * math.cos(ang) * ac, cy + 40 * math.sin(ang) * ac, AMBER, ac, 5)
        c.drawCircle(cx, cy, 18, paint(RED, ac))
    pill(c, "B 5", 1250, 360, PURPLE, size=80, a=ab, anchor="center")
    text(c, "linha B + coluna 5", 1250, 480, 34, "black", INK2, ab)
    text(c, "= UMA casinha exata", 1250, 540, 36, "black", GREEN, ac)
    pill(c, "a Terra tem um tabuleiro assim", 1250, 680, BLUE, size=28, a=ep(t, C["05.d"], 0.5), anchor="center")


# ======================================================================
# bloco a: paralelos e latitude
# ======================================================================

def b_equador(c, t, C, B):
    head(c, t, B["start"], "ONDE COMEÇA O TABULEIRO?", "O EQUADOR", BLUE)
    card(c, *CARD_R)
    cx, cy, r = 640, 495, 290
    lon0 = spin(t, B["start"], 10)
    mapas.draw_globe(c, cx, cy, r, 1, lon0=lon0, lat0=12, grat_lats=(), grat_lons=())
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        c.save(); clip = skia.Path(); clip.addCircle(cx, cy, r); c.clipPath(clip, skia.ClipOp.kIntersect, True)
        ey = mapas.globe_xy(lon0, 0, cx, cy, r, lon0, 12)[1]
        c.drawRect(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, ey), paint(BLUE, 0.12 * ac))
        c.drawRect(skia.Rect.MakeLTRB(cx - r, ey, cx + r, cy + r), paint(GREEN, 0.12 * ac))
        c.restore()
    mapas.globe_line(c, cx, cy, r, BLUE, ep(t, C["06.a"], 0.5), 8, lon0, 12, lat=0)
    pill(c, "EQUADOR", 1180, 470, BLUE, size=40, a=ep(t, C["06.b"], 0.5), anchor="center")
    text(c, "o meio da Terra", 1180, 540, 30, "black", INK2, ep(t, C["06.b"], 0.5))
    pill(c, "HEMISFÉRIO = metade da Terra", 1180, 630, BLUE, size=26, a=ac, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    text(c, "HEMISFÉRIO NORTE", cx, 260, 32, "black", BLUE, ad)
    text(c, "HEMISFÉRIO SUL", cx, 760, 32, "black", GREEN, ad)


def b_paralelos(c, t, C, B):
    head(c, t, B["start"], "AS LINHAS DO TABULEIRO", "PARALELOS", BLUE)
    card(c, *CARD_R)
    cx, cy, r = 640, 495, 290
    lon0 = spin(t, B["start"], 10)
    mapas.draw_globe(c, cx, cy, r, 1, lon0=lon0, lat0=12, grat_lats=(), grat_lons=())
    mapas.globe_line(c, cx, cy, r, BLUE, 1, 7, lon0, 12, lat=0)
    for k, L in enumerate((15, -15, 30, -30, 45, -45, 60, -60, 75, -75)):
        mapas.globe_line(c, cx, cy, r, PURPLE, ep(t, C["07.t"] + 0.35 * k, 0.4), 4, lon0, 12, lat=L)
    pill(c, "menores perto dos polos", 1180, 380, AMBER, size=26, a=ep(t, C["07.a"], 0.5), anchor="center")
    pill(c, "PARALELOS", 1180, 480, BLUE, size=44, a=ep(t, C["07.b"], 0.5), anchor="center")
    text(c, "paralelos ao Equador", 1180, 550, 30, "black", INK2, ep(t, C["07.b"], 0.5))
    pill(c, "= as LINHAS do tabuleiro", 1180, 640, PURPLE, size=28, a=ep(t, C["07.c"], 0.5), anchor="center")


def b_latitude(c, t, C, B):
    head(c, t, B["start"], "LATITUDE", "QUANTO ACIMA OU ABAIXO DO EQUADOR", BLUE)
    card(c, *CARD_R)
    cx, cy, r = 600, 495, 280
    at = ep(t, C["08.t"], 0.5)
    if at > 0:
        c.drawCircle(cx, cy, r, paint(SEA, at)); c.drawCircle(cx, cy, r, paint(INK2, at, stroke=4))
    line(c, cx - r - 30, cy, cx + r + 30, cy, BLUE, at, 5)
    line(c, cx, cy - r - 30, cx, cy + r + 30, GRAY, at, 3, dash=(12, 8))
    text(c, "Equador", cx + r + 40, cy + 10, 28, "black", BLUE, at, align="left")
    ab = ep(t, C["08.b"], 0.5)
    lat = 40 * ep(t, C["08.b"], 1.5) if t < C["09.e"] else 40
    ang = math.radians(lat)
    P = (cx + r * math.cos(ang), cy - r * math.sin(ang))
    if ab > 0:
        wedge(c, cx, cy, 120, -lat, lat, AMBER, ab * 0.35)
        line(c, cx, cy, P[0], P[1], AMBER, ab, 5)
        c.drawCircle(cx, cy, 8, paint(INK, ab))
        c.drawCircle(*P, 14, paint(RED, ab))
    text(c, f"{lat:.0f}°", cx + 150, cy - 30, 36, "black", AMBER, ab, align="left")
    pill(c, "medida no CENTRO da Terra", 1300, 300, BLUE, size=26, a=ab, anchor="center")
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "Equador = 0°", 1300, 400, BLUE, size=32, a=ac, anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    pill(c, "90° N", cx, cy - r - 60, INK, size=28, a=ad, anchor="center")
    pill(c, "90° S", cx, cy + r + 60, INK, size=28, a=ad, anchor="center")
    text(c, "polos = 90°", 1300, 500, 36, "black", INK, ad)
    ae = ep(t, C["09.e"], 0.5)
    pill(c, "40° N", P[0] + 80, P[1] - 30, RED, size=30, a=ae, bounds=(0, 1920))
    af = ep(t, C["09.f"], 0.5)
    pill(c, "N = norte", 1210, 620, BLUE, size=30, a=af, anchor="center")
    pill(c, "S = sul", 1420, 620, GREEN, size=30, a=af, anchor="center")
    text(c, "sem a letra, não dá", 1300, 700, 30, "black", AMBER, ep(t, C["09.f"] + 1.5, 0.5))


# ======================================================================
# bloco b: meridianos e longitude
# ======================================================================

def b_meridianos(c, t, C, B):
    head(c, t, B["start"], "AS COLUNAS DO TABULEIRO", "MERIDIANOS", GREEN)
    card(c, *CARD_R)
    cx, cy, r = 640, 495, 290
    lon0 = spin(t, B["start"], 12)
    mapas.draw_globe(c, cx, cy, r, 1, lon0=lon0, lat0=12, grat_lats=(0,), grat_lons=())
    for k, L in enumerate(range(-180, 180, 30)):
        mapas.globe_line(c, cx, cy, r, GREEN, ep(t, C["10.b"] + 0.25 * k, 0.4), 4, lon0, 12, lon=L)
    pill(c, "como gomos de laranja", 1180, 380, AMBER, size=26, a=ep(t, C["10.a"], 0.5), anchor="center")
    pill(c, "MERIDIANOS", 1180, 480, GREEN, size=44, a=ep(t, C["10.c"], 0.5), anchor="center")
    text(c, "de polo a polo", 1180, 550, 30, "black", INK2, ep(t, C["10.c"], 0.5))
    pill(c, "= as COLUNAS do tabuleiro", 1180, 640, GREEN, size=28, a=ep(t, C["10.c"] + 1.0, 0.5), anchor="center")


def b_greenwich(c, t, C, B):
    head(c, t, B["start"], "QUAL MERIDIANO É O ZERO?", "GREENWICH", GREEN)
    at = ep(t, C["11.t"], 0.5)
    mapas.draw_world(c, WORLD, at, graticule=True)
    aa = ep(t, C["11.a"], 0.5)
    x0, y0 = mapas.to_xy(WORLD, (-180, 0)); x1, _ = mapas.to_xy(WORLD, (180, 0))
    line(c, x0, y0, x1, y0, BLUE, aa, 6)
    pill(c, "Equador: meio natural", x0 + 140, y0 + 40, BLUE, size=24, a=aa, bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    text_mid(c, "?", 1600, 330, 80, "black", AMBER, ab * (1 - ep(t, C["11.c"], 0.4)))
    ac = ep(t, C["11.c"], 0.5)
    gx, gy0 = mapas.to_xy(WORLD, (0, 84)); _, gy1 = mapas.to_xy(WORLD, (0, -58))
    line(c, gx, gy0, gx, gy0 + (gy1 - gy0) * ep(t, C["11.c"], 1.0), GREEN, ac, 7)
    lx, ly = mapas.to_xy(WORLD, (0, 51.5))
    if ac > 0:
        c.drawCircle(lx, ly, 12, paint(RED, ac))
    pill(c, "Londres", lx + 24, ly - 30, RED, size=22, a=ac, bounds=(0, 1920))
    pill(c, "MERIDIANO DE GREENWICH = 0°", W / 2, 810, GREEN, size=32, a=ep(t, C["11.d"], 0.5), anchor="center")
    text(c, "um acordo entre os países", W / 2, 180, 30, "black", INK2, ac)


def b_longitude(c, t, C, B):
    head(c, t, B["start"], "LONGITUDE", "QUANTO À DIREITA OU À ESQUERDA DE GREENWICH", GREEN)
    at = ep(t, C["12.t"], 0.5)
    mapas.draw_world(c, WORLD, at, graticule=True)
    gx, gy0 = mapas.to_xy(WORLD, (0, 84)); _, gy1 = mapas.to_xy(WORLD, (0, -58))
    line(c, gx, gy0, gx, gy1, GREEN, at, 7)
    ab = ep(t, C["12.b"], 0.5)
    pill(c, "0°", gx, gy0 - 22, GREEN, size=28, a=ab, anchor="center")
    ac = ep(t, C["12.c"], 0.5)
    x0, _ = mapas.to_xy(WORLD, (-180, 0)); x1, _ = mapas.to_xy(WORLD, (180, 0))
    pill(c, "180°", x0 + 10, gy0 - 22, INK, size=26, a=ac, bounds=(0, 1920))
    pill(c, "180°", x1 - 10, gy0 - 22, INK, size=26, a=ac, anchor="right", bounds=(0, 1920))
    ad = ep(t, C["12.d"], 0.5)
    ym = (gy0 + gy1) / 2 + 160
    arrow(c, gx - 20, ym, gx - 520 * ad, ym, PURPLE, ad, 7, 26)
    arrow(c, gx + 20, ym, gx + 520 * ad, ym, AMBER, ad, 7, 26)
    pill(c, "OESTE (O)", gx - 300, ym - 50, PURPLE, size=30, a=ad, anchor="center")
    pill(c, "LESTE (L)", gx + 300, ym - 50, AMBER, size=30, a=ad, anchor="center")


def b_ancora(c, t, C, B):
    head(c, t, B["start"], "O TABULEIRO DA TERRA", "LINHA + COLUNA", PURPLE)
    at = ep(t, C["13.t"], 0.5)
    mapas.draw_world(c, WORLD, at, graticule=True)
    P = (-46.6, -23.5)
    px, py = mapas.to_xy(WORLD, P)
    aa = ep(t, C["13.a"], 0.5)
    x0, _ = mapas.to_xy(WORLD, (-180, 0)); x1, _ = mapas.to_xy(WORLD, (180, 0))
    line(c, x0, py, x1, py, BLUE, aa, 8)
    pill(c, "LINHA = latitude", x0 + 20, py - 34, BLUE, size=26, a=aa, bounds=(0, 1920))
    ab = ep(t, C["13.b"], 0.5)
    _, y0 = mapas.to_xy(WORLD, (0, 84)); _, y1 = mapas.to_xy(WORLD, (0, -58))
    line(c, px, y0, px, y1, GREEN, ab, 8)
    pill(c, "COLUNA = longitude", px + 20, y0 + 30, GREEN, size=26, a=ab, bounds=(0, 1920))
    ac = ep(t, C["13.c"], 0.5)
    if ac > 0:
        c.drawCircle(px, py, 18 + 4 * math.sin(t * 5), paint(RED, ac))
    pill(c, "23° S · 46° O = os 2 números do GPS", W / 2, 810, RED, size=30, a=ac, anchor="center")


# ======================================================================
# bloco c: por que 90 e 180
# ======================================================================

def b_porque(c, t, C, B):
    head(c, t, B["start"], "POR QUE 90° E 180°?", "", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    cx, cy, r = 520, 500, 230
    if aa > 0:
        c.drawCircle(cx, cy, r, paint(SEA, aa)); c.drawCircle(cx, cy, r, paint(INK2, aa, stroke=4))
    line(c, cx - r, cy, cx + r, cy, BLUE, aa, 4)
    wedge(c, cx, cy, r, -90 * ep(t, C["14.a"] + 0.4, 1.2), 90 * ep(t, C["14.a"] + 0.4, 1.2), AMBER, aa * 0.4)
    text(c, "Equador → polo", cx, cy + r + 50, 30, "black", INK2, aa)
    pill(c, "LATITUDE: 1/4 de volta = 90°", cx, 230, BLUE, size=28, a=aa, anchor="center")
    ab = ep(t, C["14.b"], 0.5)
    cx2 = 1300
    if ab > 0:
        c.drawCircle(cx2, cy, r, paint(SEA, ab)); c.drawCircle(cx2, cy, r, paint(INK2, ab, stroke=4))
        c.drawCircle(cx2, cy, 10, paint(INK, ab))
        text_mid(c, "PN", cx2 + 30, cy - 20, 22, "black", INK2, ab, align="left")
    line(c, cx2, cy, cx2, cy + r, GREEN, ab, 6)
    text(c, "Greenwich", cx2, cy + r + 40, 26, "black", GREEN, ab)
    acc = ep(t, C["14.c"], 1.2)
    wedge(c, cx2, cy, r - 20, 90, 180 * acc, PURPLE, ab * 0.35)
    wedge(c, cx2, cy, r - 20, 90, -180 * acc, AMBER, ab * 0.35)
    pill(c, "180° O", cx2 - 170, cy - 40, PURPLE, size=26, a=acc, anchor="center")
    pill(c, "180° L", cx2 + 170, cy - 40, AMBER, size=26, a=acc, anchor="center")
    pill(c, "LONGITUDE: meia volta para cada lado", cx2, 230, GREEN, size=28, a=ab, anchor="center")
    text(c, "vista de cima do Polo Norte", cx2, 805, 24, "bold", GRAY, ab)


# ======================================================================
# bloco d: linhas importantes e o Brasil
# ======================================================================

LINHAS = [(0, "Equador · 0°", BLUE, "15.a"), (23.45, "Trópico de Câncer", AMBER, "15.c"), (-23.45, "Trópico de Capricórnio", AMBER, "15.c"),
          (66.55, "Círculo Polar Ártico", PURPLE, "16.d"), (-66.55, "Círculo Polar Antártico", PURPLE, "16.d")]


def b_linhas(c, t, C, B):
    head(c, t, B["start"], "LINHAS COM NOME PRÓPRIO", "", BLUE)
    R = (200, 190, 1520, 620)
    lat = (-72, 84)
    mapas.draw_world(c, R, 1, lat=lat)
    for L, lab, col, cue in LINHAS:
        a = ep(t, C[cue], 0.5)
        x0, y = mapas.to_xy(R, (-180, L), lat=lat); x1, _ = mapas.to_xy(R, (180, L), lat=lat)
        line(c, x0, y, x0 + (x1 - x0) * a, y, col, a, 5, dash=None if L == 0 else (16, 10))
        pill(c, lab, x1 - 10, y - 26, col, size=22, a=a, anchor="right", bounds=(0, 1920))
    pill(c, "TRÓPICO = limite do Sol a pino ao meio-dia", 640, 840, AMBER, size=24, a=ep(t, C["15.b"], 0.5), anchor="center")
    pill(c, "CÍRCULO POLAR = 1 dia de 24 h de luz ou escuridão", 1290, 840, PURPLE, size=24, a=ep(t, C["16.d"] + 1.0, 0.5),
         anchor="center")


def b_brasil(c, t, C, B):
    head(c, t, B["start"], "E O BRASIL?", "NO TABULEIRO DA TERRA", GREEN)
    R = (260, 180, 860, 640)
    lon, lat = (-82, -28), (-36, 8)
    at = ep(t, C["17.t"], 0.5)
    mapas.draw_world(c, R, at, lon=lon, lat=lat, arquivo="ne_50m_land.geojson")
    mapas.draw_country_on(c, "Brazil", R, at, lon=lon, lat=lat)
    for L, lab, col, cue in ((0, "Equador", BLUE, "17.a"), (-23.45, "Trópico de Capricórnio", AMBER, "17.b")):
        a = ep(t, C[cue], 0.5)
        x0, y = mapas.to_xy(R, (lon[0], L), lon=lon, lat=lat); x1, _ = mapas.to_xy(R, (lon[1], L), lon=lon, lat=lat)
        line(c, x0, y, x1, y, col, a, 6, dash=(16, 10))
        pill(c, lab, x1 + 20, y, col, size=26, a=a, bounds=(0, 1920))
        text(c, ("AP · RR · AM · PA" if L == 0 else "SP · PR · MS"), x1 + 24, y + 56, 28, "black", col, ep(t, C[cue] + 0.8, 0.5), align="left")
    pill(c, "maior parte no hemisfério SUL", 1420, 500, GREEN, size=26, a=ep(t, C["17.c"], 0.5), anchor="center")
    pill(c, "todas as longitudes: OESTE", 1420, 760, PURPLE, size=28, a=ep(t, C["17.d"], 0.5), anchor="center")


# ======================================================================
# recapitulação (meio e fim)
# ======================================================================

def b_recap(c, t, C, B):
    sid = "18" if B["start"] < C["37"] - 1 else "37"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    badge_row(c, t, [(C[sid + ".a"], "Latitude: a partir do EQUADOR, até 90°", BLUE),
                     (C[sid + ".b"], "Longitude: a partir de GREENWICH, até 180°", GREEN),
                     (C[sid + ".c"], "1° de latitude ≈ 111 km", PURPLE)], 240, 330, 160, 46)


# ======================================================================
# bloco e: distância no meridiano
# ======================================================================

def b_km(c, t, C, B):
    head(c, t, B["start"], "QUANTO VALE 1 GRAU?", "EM QUILÔMETROS", GREEN)
    card(c, *CARD_R)
    cx, cy, r = 520, 500, 260
    mapas.draw_globe(c, cx, cy, r, 1, lon0=spin(t, B["start"], 15), lat0=0, grat_lats=(), grat_lons=())
    aa = ep(t, C["19.a"], 0.5)
    mapas.globe_line(c, cx, cy, r, RED, aa, 8, 0, 0, lat=0)
    pill(c, "volta ≈ 40 000 km", cx, cy + 50, RED, size=30, a=aa, anchor="center")
    ab = ep(t, C["19.b"], 0.5)
    text(c, "1 volta = 360°", 1300, 330, 48, "black", INK, ab)
    ac = ep(t, C["19.c"], 0.5)
    seq(c, [("FRAC", "40 000 km", "360", INK)], 1300, 480, 70, ac)
    result_box(c, "1° ≈ 111 km", 1300, 650, 62, ep(t, C["19.d"], 0.5), GREEN)


def b_subtrai(c, t, C, B):
    head(c, t, B["start"], "MESMO HEMISFÉRIO", "SUBTRAI", GREEN)
    card(c, *CARD_R)
    Y = lat_axis(c, 420, 200, 800, 10, -30, 1)
    for cue, L, lab in (("20.a", -2, "2° S"), ("20.b", -22, "22° S")):
        a = ep(t, C[cue], 0.4)
        if a > 0:
            c.drawCircle(420, Y(L), 16, paint(RED, a))
        pill(c, lab, 460, Y(L), RED, size=26, a=a, bounds=(0, 1920))
    ac = ep(t, C["20.c"], 0.5)
    line(c, 620, Y(-2), 620, Y(-2) + (Y(-22) - Y(-2)) * ac, AMBER, ac, 8)
    text(c, "22 − 2 = 20°", 660, (Y(-2) + Y(-22)) / 2 + 12, 44, "black", AMBER, ac, align="left")
    result_box(c, "20 × 111 = 2 220 km", 1360, 560, 50, ep(t, C["20.d"], 0.5), GREEN)
    pill(c, "os dois do MESMO lado do Equador", 1360, 400, BLUE, size=26, a=ac, anchor="center")


def b_soma(c, t, C, B):
    head(c, t, B["start"], "HEMISFÉRIOS DIFERENTES", "SOMA", AMBER)
    card(c, *CARD_R)
    Y = lat_axis(c, 420, 200, 800, 10, -20, 1)
    a0 = ep(t, C["21.a"], 0.4)
    for L, lab in ((5, "5° N"), (-15, "15° S")):
        if a0 > 0:
            c.drawCircle(420, Y(L), 16, paint(RED, a0))
        pill(c, lab, 460, Y(L), RED, size=26, a=a0, bounds=(0, 1920))
    ab = ep(t, C["21.b"], 0.5)
    line(c, 620, Y(5), 620, Y(5) + (Y(0) - Y(5)) * ab, PURPLE, ab, 8)
    text(c, "5°", 650, (Y(5) + Y(0)) / 2 + 12, 40, "black", PURPLE, ab, align="left")
    ac = ep(t, C["21.c"], 0.5)
    line(c, 620, Y(0), 620, Y(0) + (Y(-15) - Y(0)) * ac, AMBER, ac, 8)
    text(c, "+ 15°", 650, (Y(0) + Y(-15)) / 2 + 12, 40, "black", AMBER, ac, align="left")
    result_box(c, "5 + 15 = 20°", 1360, 560, 56, ep(t, C["21.d"], 0.5), GREEN)
    pill(c, "atravessou o Equador → SOMA", 1360, 400, AMBER, size=26, a=ep(t, C["21.d"], 0.5), anchor="center")


def b_lonnao(c, t, C, B):
    head(c, t, B["start"], "E A LONGITUDE?", "A CONTA NÃO VALE", RED)
    card(c, *CARD_R)
    cx, cy, r = 620, 495, 290
    mapas.draw_globe(c, cx, cy, r, 1, lon0=15, lat0=20, grat_lats=(), grat_lons=tuple(range(-180, 180, 15)))
    aa, ab = ep(t, C["22.a"], 0.5), ep(t, C["22.b"], 0.5)
    for L in (0, 30):
        mapas.globe_line(c, cx, cy, r, RED, ab, 6, 15, 20, lon=L)
    for lat, lab, col, a in ((0, "largo", GREEN, aa), (60, "apertado", AMBER, ab)):
        p0, p1 = mapas.globe_xy(0, lat, cx, cy, r, 15, 20), mapas.globe_xy(30, lat, cx, cy, r, 15, 20)
        line(c, p0[0], p0[1], p1[0], p1[1], col, a, 9)
        pill(c, lab, p1[0] + 20, p1[1], col, size=24, a=a, bounds=(0, 1920))
    pill(c, "no polo, 1° de longitude = ZERO", 1300, 480, RED, size=30, a=ep(t, C["22.c"], 0.5), anchor="center")
    text(c, "os meridianos se encontram", 1300, 560, 30, "black", INK2, ep(t, C["22.c"], 0.5))


# ======================================================================
# blocos f e g: rosa dos ventos e direção
# ======================================================================

def rosa(c, cx, cy, R, a_card, a_col, a_sub):
    for k in range(16):
        ang = math.radians(90 - k * 22.5)
        kind = 0 if k % 4 == 0 else 1 if k % 2 == 0 else 2
        a = (a_card, a_col, a_sub)[kind]
        if a <= 0:
            continue
        L = R * (1.0, 0.72, 0.5)[kind]
        w = (34, 26, 16)[kind]
        tip = (cx + L * math.cos(ang), cy - L * math.sin(ang))
        side = math.radians(90 - k * 22.5 + 90)
        p = skia.Path(); p.moveTo(*tip)
        p.lineTo(cx + w * math.cos(side), cy - w * math.sin(side)); p.lineTo(cx - w * math.cos(side), cy + w * math.sin(side)); p.close()
        c.drawPath(p, paint((BLUE, PURPLE, AMBER)[kind], a * 0.85))
        lab = ["N", "NNE", "NE", "ENE", "L", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"][k]
        text_mid(c, lab, cx + (L + 40) * math.cos(ang), cy - (L + 40) * math.sin(ang), (40, 28, 20)[kind], "black",
                 (INK, PURPLE, AMBER)[kind], a)


def b_rosa(c, t, C, B):
    head(c, t, B["start"], "ROSA DOS VENTOS", "PARA QUE LADO FICA?", PURPLE)
    card(c, *CARD_R)
    rosa(c, 620, 500, 260, ep(t, C["23.b"], 0.5), ep(t, C["23.c"], 0.5), ep(t, C["23.d"], 0.5))
    pill(c, "a estrela no canto dos mapas", 620, 200, INK, size=24, a=ep(t, C["23.a"], 0.5), anchor="center")
    rows = [("23.b", "CARDEAIS", "N · S · L · O", BLUE), ("23.c", "COLATERAIS", "NE · SE · SO · NO", PURPLE),
            ("23.d", "SUBCOLATERAIS", "NNE · ENE · ...", AMBER)]
    for k, (cue, tt, ex, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + k * 150 + d
        text(c, tt, 1080, y, 44, "black", col, a, align="left")
        text(c, ex, 1080, y + 50, 32, "bold", INK2, a, align="left")


def b_direcao(c, t, C, B):
    head(c, t, B["start"], "DIREÇÃO PELOS NÚMEROS", "LINHA E COLUNA SEPARADAS", PURPLE)
    card(c, *CARD_R)
    X, Y = grid_coords(c, 300, 230, 640, 480, 1)
    A = (X(50), Y(10))
    c.drawCircle(*A, 14, paint(INK, 1))
    aa = ep(t, C["24.a"], 0.5)
    arrow(c, A[0], A[1] + 20, A[0], Y(25), BLUE, aa, 6, 22, progress=aa)
    pill(c, "número SUL maior → mais ao SUL", A[0] + 20, Y(20), BLUE, size=24, a=aa, bounds=(0, 1920))
    ab = ep(t, C["24.b"], 0.5)
    arrow(c, A[0] + 20, A[1], X(32), A[1], GREEN, ab, 6, 22, progress=ab)
    pill(c, "número OESTE menor → mais a LESTE", X(45), A[1] - 40, GREEN, size=24, a=ab, bounds=(0, 1920))
    text(c, "Greenwich fica para lá →", 1300, 440, 34, "black", GREEN, ab)
    text(c, "(mais perto do 0°)", 1300, 490, 30, "bold", INK2, ab)


# ======================================================================
# bloco h: curiosidades
# ======================================================================

def b_sol(c, t, C, B):
    head(c, t, B["start"], "CURIOSIDADE", "O SOL NASCE NO LESTE?", AMBER)
    card(c, *CARD_R)
    hy = 640
    rrect(c, 200, hy, 1520, 190, 0, "#BBF7D0", 1)
    line(c, 200, hy, 1720, hy, INK2, 1, 3)
    for x, lab in ((560, "NE"), (960, "L"), (1360, "SE")):
        line(c, x, hy, x, hy + 30, INK2, 1, 3)
        text(c, lab, x, hy + 70, 36, "black", INK, 1)
    aa = ep(t, C["25.a"], 0.5)
    u = (t - C["25.a"]) % 5 / 5
    sy = lerp(hy, hy - 300, u)
    if aa > 0:
        c.drawCircle(960, sy, 46, paint("#FACC15", aa)); c.drawCircle(960, sy, 46, paint("#F59E0B", aa, stroke=4))
    pill(c, "EQUINÓCIO (março e setembro): no LESTE", 1390, 230, BLUE, size=26, a=aa, anchor="center")
    text(c, "dia e noite do mesmo tamanho", 1390, 290, 28, "black", INK2, aa)
    ab = ep(t, C["25.b"], 0.5)
    for x in (560, 1360):
        if ab > 0:
            c.drawCircle(x, hy - 60, 34, paint("#FACC15", ab * 0.8))
    pill(c, "no resto do ano: um pouco para NE ou SE", 1390, 400, AMBER, size=26, a=ab, anchor="center")


def b_bussola(c, t, C, B):
    head(c, t, B["start"], "CURIOSIDADE", "A BÚSSOLA E O POLO NORTE", AMBER)
    card(c, *CARD_R)
    cx, cy, r = 620, 500, 240
    aa = ep(t, C["26.a"], 0.5)
    if aa > 0:
        c.drawCircle(cx, cy, r, paint("#FFFFFF", aa)); c.drawCircle(cx, cy, r, paint(INK2, aa, stroke=8))
    line(c, cx, cy, cx, cy - r + 20, BLUE, aa, 5, dash=(14, 10))
    pill(c, "norte GEOGRÁFICO", cx, cy - r - 40, BLUE, size=26, a=aa, anchor="center")
    ang = math.radians(-14 + 2 * math.sin(t * 2))
    tip = (cx + (r - 30) * math.sin(ang), cy - (r - 30) * math.cos(ang))
    if aa > 0:
        p = skia.Path(); p.moveTo(*tip); p.lineTo(cx + 18 * math.cos(ang), cy + 18 * math.sin(ang))
        p.lineTo(cx - 18 * math.cos(ang), cy - 18 * math.sin(ang)); p.close()
        c.drawPath(p, paint(RED, aa))
        c.drawCircle(cx, cy, 14, paint(INK, aa))
    pill(c, "norte MAGNÉTICO", tip[0] - 40, tip[1] + 40, RED, size=26, a=aa, anchor="right", bounds=(0, 1920))
    ab = ep(t, C["26.b"], 0.5)
    arc(c, cx, cy, 150, -90, -14, AMBER, ab, 6)
    pill(c, "DECLINAÇÃO MAGNÉTICA", 1300, 400, BLUE, size=32, a=ab, anchor="center")
    text(c, "a diferença entre os dois nortes", 1300, 470, 30, "black", INK2, ab)
    pill(c, "muda com o tempo: o mapa de trilha traz o número", 1300, 620, AMBER, size=24, a=ep(t, C["26.c"], 0.5),
         anchor="center", bounds=(0, 1920))


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "LATITUDE A PARTIR DE GREENWICH", RED)
    erro_tiles(c, t, [(C["27.a"], "O ERRO", ["latitude a partir", "de Greenwich"], RED),
                      (C["27.b"], "POR QUE PARECE CERTO", ["Greenwich é o", "famoso ZERO"], AMBER),
                      (C["27.c"], "A CORREÇÃO", ["Greenwich: zero da", "LONGITUDE", "latitude: do EQUADOR"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "SUBTRAIR HEMISFÉRIOS DIFERENTES", RED)
    erro_tiles(c, t, [(C["28.a"], "O ERRO", ["5° N a 15° S:", "15 − 5 = 10°"], RED),
                      (C["28.b"], "POR QUE PARECE CERTO", ["diferença sempre", "é subtração"], AMBER),
                      (C["28.c"], "A CORREÇÃO", ["lados opostos", "do Equador:", "5 + 15 = 20°"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "40° O MAIS A OESTE QUE 50° O?", RED)
    erro_tiles(c, t, [(C["29.a"], "O ERRO", ["40° O fica mais", "a oeste que 50° O"], RED),
                      (C["29.b"], "POR QUE PARECE CERTO", ["a gente lê", "só o número"], AMBER),
                      (C["29.c"], "A CORREÇÃO", ["o número é a", "distância a Greenwich:", "40° O é mais a LESTE"], GREEN)])


# ======================================================================
# questões estilo ENEM
# ======================================================================

def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "DISTÂNCIA NO MERIDIANO", BLUE)
    card(c, *CARD_R)
    for k, (cue, s, col) in enumerate((("30.e1", "Povoados A e B no mesmo meridiano (50° O).", INK),
                                       ("30.e2", "A: 2° S · B: 22° S · 1° ≈ 111 km", INK),
                                       ("30.e3", "Qual a distância entre eles?", BLUE))):
        text(c, s, 210, 240 + k * 55, 34, "black", col, ep(t, C[cue], 0.5), align="left")
    items = [("A", "222 km", "31.a", "32.a", "usou só os 2° de A"), ("B", "1 110 km", "31.b", "32.b", "10° não é a diferença"),
             ("C", "2 220 km", "31.c", None, ""), ("D", "2 664 km", "31.d", "32.d", "somou: 24°"),
             ("E", "5 550 km", "31.e", "32.e", "usou a longitude")]
    alts(c, t, C, items, 240, 450, 72, 34, ok_cue="32.c", why_x=1720)
    pause_badge(c, t, C, "31.p", "32.t")
    pill(c, "mesmo hemisfério: 22 − 2 = 20° · 20 × 111", 1250, 380, GREEN, size=26, a=ep(t, C["32.t"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "PARA QUE LADO FICA?", BLUE)
    card(c, *CARD_R)
    text(c, "Sai de 10° S, 50° O e vai até 20° S, 40° O.", 210, 240, 34, "black", INK, ep(t, C["33.e1"], 0.5), align="left")
    text(c, "Para que lado fica o destino?", 210, 295, 34, "black", BLUE, ep(t, C["33.e3"], 0.5), align="left")
    ag = ep(t, C["35.t"], 0.5)
    X, Y = grid_coords(c, 300, 380, 520, 360, ag, lats=(0, 10, 20, 30))
    A, Bp = (X(50), Y(10)), (X(40), Y(20))
    if ag > 0:
        c.drawCircle(*A, 14, paint(INK, ag)); text_mid(c, "saída", A[0] - 20, A[1] - 30, 22, "black", INK, ag, align="right")
        c.drawCircle(*Bp, 14, paint(RED, ag)); text_mid(c, "destino", Bp[0] + 20, Bp[1] + 30, 22, "black", RED, ag, align="left")
    a1, a2, ar = ep(t, C["35.s1"], 0.5), ep(t, C["35.s2"], 0.5), ep(t, C["35.r"], 0.5)
    arrow(c, A[0], A[1] + 16, A[0], Bp[1], BLUE, a1, 5, 18, progress=a1)
    pill(c, "SUL", A[0] - 20, (A[1] + Bp[1]) / 2, BLUE, size=22, a=a1, anchor="right", bounds=(0, 1920))
    arrow(c, A[0], Bp[1], Bp[0] - 16, Bp[1], GREEN, a2, 5, 18, progress=a2)
    pill(c, "LESTE", (A[0] + Bp[0]) / 2, Bp[1] + 40, GREEN, size=22, a=a2, anchor="center", bounds=(0, 1920))
    arrow(c, A[0] + 10, A[1] + 10, Bp[0] - 12, Bp[1] - 12, RED, ar, 6, 22, progress=ar)
    items = [("A", "nordeste", "34.a", "36.a", "errou a latitude"), ("B", "noroeste", "34.b", "36.b", "errou os dois"),
             ("C", "sudoeste", "34.c", "36.c", "o erro do 40° O"), ("D", "sudeste", "34.d", None, ""),
             ("E", "leste", "34.e", "36.e", "esqueceu a latitude")]
    alts(c, t, C, items, 1060, 430, 72, 34, ok_cue="35.r", why_x=1730)
    pause_badge(c, t, C, "34.p", "35.t")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PROJEÇÕES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["38.a"], 0.5)
    mapas.draw_globe(c, 480, 500, 240, aa, lon0=spin(t, B["start"], 20), lat0=10)
    arrow(c, 760, 500, 900, 500, INK2, aa, 6, 22)
    ab = ep(t, C["38.b"], 0.5)
    mapas.draw_world(c, (940, 330, 680, 340), aa, proj="mercator", lat=(-58, 80))
    text_mid(c, "?", 830, 430, 70, "black", AMBER, aa * (1 - ab))
    pill(c, "não dá sem DISTORCER", 1280, 260, AMBER, size=30, a=ab, anchor="center")
    pill(c, "EPISÓDIO 3: PROJEÇÕES", W / 2, 800, PURPLE, size=34, a=ep(t, C["38.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["39.like"], C["39.sub"], C["39.bell"], C["39.com"], C["39.bye"], "Já caiu na do 40° oeste?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, grau=b_grau, terra=b_terra, batalha=b_batalha, equador=b_equador,
              paralelos=b_paralelos, latitude=b_latitude, meridianos=b_meridianos, greenwich=b_greenwich, longitude=b_longitude,
              ancora=b_ancora, porque=b_porque, linhas=b_linhas, brasil=b_brasil, recap=b_recap, km=b_km, subtrai=b_subtrai,
              soma=b_soma, lonnao=b_lonnao, rosa=b_rosa, direcao=b_direcao, sol=b_sol, bussola=b_bussola, erro1=b_erro1,
              erro2=b_erro2, erro3=b_erro3, q4=b_q4, q9=b_q9, ponte=b_ponte, cta=b_cta)
