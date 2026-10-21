"""Visual — Cartografia, Episódio 3: Projeções cartográficas (aula para iniciantes, tema claro).
Cores com função: azul = definição · âmbar = atenção/armadilha · verde = atalho/dica · vermelho = erro.
Mapas com dados reais e projeções calculadas de verdade (_ferramentas/mapas.py).
"""
import math
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep3_projecoes.mp4"
CARD_R = (140, 150, 1640, 690)
ORANGE, PEEL = "#FB923C", "#EA580C"
MLAT = (-58, 80)                  # recorte de latitudes para a Mercator
MAP = (200, 175, 1520, 640)       # retângulo padrão de mapa grande


# ======================================================================
# utilidades
# ======================================================================

def clip(c, rect, r=18):
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(*rect), r, r), True)


def merc(c, rect, a, **kw):
    mapas.draw_world(c, rect, a, proj="mercator", lat=MLAT, **kw)
    return mapas.world_frame(rect, "mercator", (-180, 180), MLAT)


def on_merc(c, rings, rect, a, fill, stroke):
    fr = mapas.world_frame(rect, "mercator", (-180, 180), MLAT)
    clip(c, fr)
    mapas.draw_rings_on(c, rings, rect, a, fill, stroke, proj="mercator", lat=MLAT)
    c.restore()


def gore(c, x, top, bot, w, col, a, stroke=None):
    """gomo de casca (lente) vertical"""
    if a <= 0:
        return
    mid = (top + bot) / 2
    p = skia.Path(); p.moveTo(x, top)
    p.quadTo(x + w, mid, x, bot); p.quadTo(x - w, mid, x, top); p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint(stroke or PEEL, a, stroke=3))


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
            text(c, ln, x + cw / 2, y + 250 + j * 58, 36, "black", INK, a)


def mini_globe_surface(c, cx, cy, r, kind, a):
    """globo pequeno com a superfície de projeção encostada; a linha de contato em verde"""
    mapas.draw_globe(c, cx, cy, r, a, lon0=-20, lat0=0 if kind == "cil" else 20, grat_lats=(), grat_lons=())
    if kind == "cil":
        line(c, cx - r, cy - r * 1.25, cx - r, cy + r * 1.25, PURPLE, a, 4)
        line(c, cx + r, cy - r * 1.25, cx + r, cy + r * 1.25, PURPLE, a, 4)
        for yy in (cy - r * 1.25, cy + r * 1.25):
            c.drawOval(skia.Rect.MakeLTRB(cx - r, yy - 16, cx + r, yy + 16), paint(PURPLE, a, stroke=3))
        mapas.globe_line(c, cx, cy, r, GREEN, a, 6, -20, 0, lat=0)
    elif kind == "con":
        y45 = mapas.globe_xy(0, 45, cx, cy, r, -20, 20)[1]
        hw = r * math.cos(math.radians(45))
        apex = (cx, y45 - hw * 1.2)
        for s in (-1, 1):
            line(c, *apex, cx + s * hw * 1.7, y45 + hw * 0.85, PURPLE, a, 4)
        mapas.globe_line(c, cx, cy, r, GREEN, a, 6, -20, 20, lat=45)
    else:
        top = mapas.globe_xy(0, 90, cx, cy, r, -20, 20)
        line(c, cx - r * 1.1, top[1] - 6, cx + r * 1.1, top[1] - 6, PURPLE, a, 5)
        c.drawCircle(top[0], top[1], 10, paint(GREEN, a))


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    a0 = ep(t, B["start"] + 0.2, 0.6)
    merc(c, MAP, a0)
    ga, fa = ep(t, C["01.a"], 0.5), ep(t, C["01.b"], 0.5)
    on_merc(c, mapas._country_rings("Greenland"), MAP, ga, "#F59E0B", "#B45309")
    on_merc(c, mapas.continent_rings("Africa"), MAP, fa, "#F59E0B", "#B45309")
    gx, gy = mapas.to_xy(MAP, (-42, 72), "mercator", lat=MLAT)
    ax, ay = mapas.to_xy(MAP, (20, 5), "mercator", lat=MLAT)
    pill(c, "Groenlândia", gx, gy, INK, size=26, a=ga, anchor="center")
    pill(c, "África", ax, ay, INK, size=26, a=fa, anchor="center")
    pill(c, "mesmo tamanho?", W / 2, 140, AMBER, size=32, a=ep(t, C["01.c"], 0.5), anchor="center")
    pill(c, "a África é 14× MAIOR", ax + 40, ay + 120, RED, size=34, a=ep(t, C["01.d"], 0.5), anchor="center")
    text_mid(c, "?", 1640, 300, 110, "black", RED, ep(t, C["01.e"], 0.5))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Entender por que\nnenhum mapa\né perfeito", C["02.a"], BLUE),
                     ("2", "Reconhecer os\ntipos de projeção", C["02.b"], GREEN),
                     ("3", "Ver a política\npor trás do mapa", C["02.c"], PURPLE)], cw=440, chh=420, title_size=34)


def b_prelat(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 1", "LATITUDE (EPISÓDIO 2)", BLUE)
    card(c, *CARD_R)
    cx, cy, r = 560, 495, 270
    mapas.draw_globe(c, cx, cy, r, ep(t, C["03.a"], 0.5), lon0=-30, lat0=0, grat_lats=(0,), grat_lons=())
    ab, ac = ep(t, C["03.b"], 0.5), ep(t, C["03.c"], 0.5)
    for L in (60, -60):
        mapas.globe_line(c, cx, cy, r, RED, ab, 7, -30, 0, lat=L)
    for L in (15, -15):
        mapas.globe_line(c, cx, cy, r, GREEN, ac, 7, -30, 0, lat=L)
    pill(c, "LATITUDE = quanto acima ou abaixo do Equador", 1290, 320, BLUE, size=26, a=ep(t, C["03.a"], 0.5), anchor="center")
    pill(c, "ALTA latitude = perto dos POLOS", 1290, 470, RED, size=30, a=ab, anchor="center")
    pill(c, "BAIXA latitude = perto do EQUADOR", 1290, 600, GREEN, size=30, a=ac, anchor="center")


def b_preforma(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO 2", "ÁREA x FORMA", BLUE)
    card(c, *CARD_R)
    aa, ab, ac = (ep(t, C[k], 0.5) for k in ("04.a", "04.b", "04.c"))
    rrect(c, 300, 300, 240, 240, 8, BLUE, 0.85 * ac)
    rrect(c, 680, 360, 480, 120, 8, GREEN, 0.85 * ac)
    text(c, "mesma ÁREA", 730, 640, 40, "black", INK, ac)
    text(c, "formas DIFERENTES", 730, 700, 34, "black", AMBER, ac)
    pill(c, "ÁREA = o TAMANHO", 1460, 360, BLUE, size=34, a=aa, anchor="center")
    pill(c, "FORMA = o CONTORNO", 1460, 500, PURPLE, size=34, a=ab, anchor="center")


# ======================================================================
# bloco a: o problema (casca de laranja)
# ======================================================================

def b_laranja(c, t, C, B):
    head(c, t, B["start"], "DÁ PARA DESENHAR A TERRA", "NUMA FOLHA SEM ERRAR?", AMBER)
    card(c, *CARD_R)
    a0 = ep(t, C["05.t"], 0.5) * (1 - 0.7 * ep(t, C["05.b"], 0.5))
    if a0 > 0:
        c.drawCircle(400, 480, 180, paint(ORANGE, a0)); c.drawCircle(400, 480, 180, paint(PEEL, a0, stroke=5))
        for k in range(8):
            ang = math.radians(k * 22.5)
            c.drawOval(skia.Rect.MakeLTRB(400 - 180 * abs(math.cos(ang)), 300, 400 + 180 * abs(math.cos(ang)), 660),
                       paint(PEEL, a0 * 0.4, stroke=2))
    aa = ep(t, C["05.a"], 0.5)
    pill(c, "descasque inteira", 400, 720, INK, size=26, a=aa * (1 - ep(t, C["05.b"], 0.4)), anchor="center")
    ab = ep(t, C["05.b"], 1.0)
    x0, step = 760, 110
    spread = lerp(0, 18, ep(t, C["05.c"], 0.8))
    stretch = ep(t, C["05.d"], 0.8)
    for k in range(9):
        x = x0 + k * (step + spread * (1 - stretch))
        w = lerp(48, 60, stretch)
        gore(c, x, lerp(480, 300, ab), lerp(480, 660, ab), w * ab, ORANGE, ab)
    if stretch > 0:
        rrect(c, x0 - 4, 300, 8 * step + 8, 360, 4, ORANGE, stretch * 0.75)
        for yy in (330, 630):
            arrow(c, x0 + 4 * step, yy, x0 + 4 * step - 400 * stretch, yy, AMBER, stretch, 5, 18)
            arrow(c, x0 + 4 * step, yy, x0 + 4 * step + 400 * stretch, yy, AMBER, stretch, 5, 18)
    ac = ep(t, C["05.c"], 0.4) * (1 - stretch)
    for k in range(8):
        xx = x0 + k * (step + spread) + step / 2 + spread / 2
        line(c, xx - 12, 330, xx + 12, 370, RED, ac, 4); line(c, xx - 12, 590, xx + 12, 630, RED, ac, 4)
    pill(c, "RASGA", 1200, 240, RED, size=40, a=ac, anchor="center")
    pill(c, "ou ESTICA", 1200, 240, AMBER, size=40, a=stretch, anchor="center")


def b_projecao(c, t, C, B):
    head(c, t, B["start"], "PROJEÇÃO", "", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    mapas.draw_globe(c, 430, 495, 230, aa, lon0=-30, lat0=10)
    arrow(c, 700, 495, 860, 495, BLUE, aa, 7, 26)
    merc(c, (900, 330, 760, 330), aa)
    pill(c, "PROJEÇÃO = jeito de passar a Terra para o papel", W / 2, 230, BLUE, size=28, a=aa, anchor="center")
    pill(c, "toda projeção ESTICA em algum lugar", 1280, 720, AMBER, size=28, a=ep(t, C["06.b"], 0.5), anchor="center")
    pill(c, "a diferença é ONDE", 1280, 790, GREEN, size=28, a=ep(t, C["06.c"], 0.5), anchor="center")


# ======================================================================
# bloco b: as três superfícies
# ======================================================================

def b_lampada(c, t, C, B):
    head(c, t, B["start"], "COMO SE FAZ UMA PROJEÇÃO?", "A SOMBRA DO GLOBO", BLUE)
    card(c, *CARD_R)
    cx, cy, r = 620, 500, 230
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        c.drawCircle(cx, cy, r, paint("#E0F2FE", aa * 0.6)); c.drawCircle(cx, cy, r, paint(INK2, aa, stroke=4))
        for L in (-60, -30, 0, 30, 60):
            yy = cy - r * math.sin(math.radians(L))
            line(c, cx - r * math.cos(math.radians(L)), yy, cx + r * math.cos(math.radians(L)), yy, "#60A5FA", aa, 3)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        c.drawCircle(cx, cy, 70 + 6 * math.sin(t * 6), paint("#FDE047", ab * 0.35))
        c.drawCircle(cx, cy, 22, paint("#FACC15", ab))
    ac = ep(t, C["07.c"], 0.5)
    px = cx + r
    rrect(c, px, 170, 30, 660, 4, "#FFFFFF", ac)
    if ac > 0:
        c.drawRect(skia.Rect.MakeXYWH(px, 170, 30, 660), paint(INK2, ac, stroke=3))
    for L in (-60, -30, 0, 30, 60):
        hy = cy - r * math.tan(math.radians(L))
        if 175 < hy < 825:
            line(c, cx, cy, px, hy, "#FACC15", ac * 0.8, 2)
            c.drawCircle(px + 15, hy, 9, paint("#60A5FA", ac))
    pill(c, "lâmpada dentro do globo", 300, 230, AMBER, size=26, a=ab, anchor="center")
    pill(c, "as linhas viram SOMBRA no papel", 1280, 420, BLUE, size=28, a=ac, anchor="center")
    pill(c, "o papel pode ser enrolado de 3 jeitos", 1280, 560, PURPLE, size=28, a=ep(t, C["07.d"], 0.5), anchor="center")


def b_superficies(c, t, C, B):
    head(c, t, B["start"], "AS TRÊS SUPERFÍCIES", "TUBO · CHAPÉU · FOLHA", PURPLE)
    cw, gap, y = 500, 40, 180
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    data = [("08.c", "cil", "CILÍNDRICA", "toca: o EQUADOR", "mapa-múndi"),
            ("09.k", "con", "CÔNICA", "toca: um PARALELO", "latitudes médias"),
            ("10.z", "azi", "AZIMUTAL (plana)", "toca: um PONTO", "regiões polares · ONU")]
    for k, (cue, kind, nome, toca, uso) in enumerate(data):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, y + dy, cw, 610, a)
        text(c, nome, x + cw / 2, y + dy + 60, 38, "black", PURPLE, a)
        mini_globe_surface(c, x + cw / 2, y + dy + 250, 120, kind, a)
        pill(c, toca, x + cw / 2, y + dy + 450, GREEN, size=26, a=a, anchor="center", bounds=(0, 1920))
        text(c, uso, x + cw / 2, y + dy + 530, 30, "black", INK2, a)


def b_toque(c, t, C, B):
    head(c, t, B["start"], "ONDE O MAPA ERRA MENOS?", "ONDE O PAPEL ENCOSTA", GREEN)
    at = ep(t, C["11.t"], 0.5)
    merc(c, MAP, at)
    aa = ep(t, C["11.a"], 0.5)
    x0, y0 = mapas.to_xy(MAP, (-180, 0), "mercator", lat=MLAT); x1, _ = mapas.to_xy(MAP, (180, 0), "mercator", lat=MLAT)
    line(c, x0, y0, x1, y0, GREEN, aa, 7)
    pill(c, "toque: erro MÍNIMO", x0 + 20, y0 - 34, GREEN, size=26, a=aa, bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    for k, la in enumerate((0, 30, 50, 65, -30, -50)):
        mapas.tissot(c, MAP, (150, la), 5, ab * ep(t, C["11.b"] + 0.3 * k, 0.4), RED, proj="mercator", lat=MLAT)
    pill(c, "mais longe do toque = MAIS distorção", W / 2, 840, RED, size=30, a=ep(t, C["11.c"], 0.5), anchor="center")
    text(c, "círculos do MESMO tamanho real", 1450, 160, 26, "black", RED, ab)


# ======================================================================
# bloco c: o que cada projeção conserva
# ======================================================================

def _ic_conforme(c, x, y, a):
    for k, s in enumerate((40, 52, 70, 96)):
        rrect(c, x + k * 80, y + 110 - s, s, s, 4, BLUE, a * 0.85)


def _ic_equivalente(c, x, y, a):
    ws = (52, 64, 82, 108)
    for k, w in enumerate(ws):
        h = 52 * 52 / w
        rrect(c, x + sum(ws[:k]) + 10 * k, y + 110 - h, w, h, 4, GREEN, a * 0.85)


def _ic_equidistante(c, x, y, a):
    cx, cy = x + 170, y + 60
    for k in range(8):
        ang = k * math.pi / 4
        line(c, cx, cy, cx + 80 * math.cos(ang), cy + 80 * math.sin(ang), PURPLE, a, 4)
        c.drawCircle(cx + 80 * math.cos(ang), cy + 80 * math.sin(ang), 8, paint(PURPLE, a))
    c.drawCircle(cx, cy, 12, paint(INK, a))


def _ic_afilatica(c, x, y, a):
    for k, (w, h) in enumerate(((56, 56), (64, 54), (74, 56), (88, 60))):
        rrect(c, x + k * 82, y + 110 - h, w, h, 10, AMBER, a * 0.85)


def b_conserva(c, t, C, B):
    head(c, t, B["start"], "O QUE VOCÊ PROTEGE?", "CADA PROJEÇÃO ESCOLHE", BLUE)
    a12 = fw(t, C["12.t"], C["13.c"] - 0.2)
    pill(c, "proteger a FORMA", 700, 450, BLUE, size=40, a=a12 * ep(t, C["12.a"], 0.5), anchor="center")
    text(c, "ou", 960, 465, 40, "black", GRAY, a12 * ep(t, C["12.a"], 0.5))
    pill(c, "proteger a ÁREA", 1220, 450, GREEN, size=40, a=a12 * ep(t, C["12.a"], 0.5), anchor="center")
    data = [("13.c", "13.c2", "CONFORME", "guarda: FORMA", "estraga: ÁREA", BLUE, _ic_conforme),
            ("14.e", "14.e2", "EQUIVALENTE", "guarda: ÁREA", "estraga: FORMA", GREEN, _ic_equivalente),
            ("15.d", "15.d", "EQUIDISTANTE", "guarda: DISTÂNCIA", "a partir de 1 ponto", PURPLE, _ic_equidistante),
            ("15.f", "15.f", "AFILÁTICA", "um pouco de TUDO", "erro total pequeno", AMBER, _ic_afilatica)]
    cw, gap = 390, 20
    x0 = W / 2 - (4 * cw + 3 * gap) / 2
    for k, (cue, cue2, nome, g, e, col, ic) in enumerate(data):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = x0 + k * (cw + gap), 200 + dy
        card(c, x, y, cw, 560, a)
        text(c, nome, x + cw / 2, y + 70, 38, "black", col, a)
        ic(c, x + 30, y + 130, a)
        text(c, g, x + cw / 2, y + 360, 32, "black", INK, a)
        text(c, e, x + cw / 2, y + 420, 28, "bold", RED if "estraga" in e else INK2, a * ep(t, C[cue2], 0.5))


def b_regra(c, t, C, B):
    head(c, t, B["start"], "REGRA DE OURO", "", RED)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    text(c, "FORMA  +  ÁREA", W / 2, 380, 110, "black", INK, aa)
    check_icon(c, W / 2, 500, 50, aa, RED, "x")
    text(c, "ao mesmo tempo: IMPOSSÍVEL", W / 2, 640, 50, "black", RED, aa)
    pill(c, "contorno perfeito → o TAMANHO estica", W / 2, 760, AMBER, size=30, a=ep(t, C["16.c"], 0.5), anchor="center")


# ======================================================================
# recapitulação (meio e fim)
# ======================================================================

def b_recap(c, t, C, B):
    sid = "17" if B["start"] < C["33"] - 1 else "33"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    badge_row(c, t, [(C[sid + ".a"], "Todo mapa DISTORCE alguma coisa", BLUE),
                     (C[sid + ".b"], "Conforme: FORMA · Equivalente: ÁREA · nunca as 2", GREEN),
                     (C[sid + ".c"], "Mercator infla os POLOS · Peters: áreas certas", PURPLE)], 220, 330, 160, 40)


# ======================================================================
# bloco d: Mercator
# ======================================================================

def b_mercator(c, t, C, B):
    head(c, t, B["start"], "MERCATOR (1569)", "CILÍNDRICA E CONFORME", BLUE)
    s19, s20 = C["19.c"], C["20.g"]
    aA = fw(t, B["start"], s19 - 0.2)
    if aA > 0:
        R = (200, 200, 1000, 560)
        merc(c, R, aA)
        p0 = mapas.to_xy(R, (-75, 38), "mercator", lat=MLAT); p1 = mapas.to_xy(R, (-5, 52), "mercator", lat=MLAT)
        arrow(c, *p0, *p1, RED, aA * ep(t, C["18.b"], 0.5), 6, 22, progress=ep(t, C["18.b"], 1.5))
        pill(c, "rumo constante = linha RETA", (p0[0] + p1[0]) / 2, p0[1] - 60, RED, size=24, a=aA * ep(t, C["18.b"], 0.5),
             anchor="center")
        pill(c, "CILÍNDRICA + CONFORME", 1470, 380, BLUE, size=30, a=aA * ep(t, C["18.a"], 0.5), anchor="center")
        pill(c, "feita para NAVEGAR", 1470, 520, GREEN, size=30, a=aA * ep(t, C["18.t"], 0.5), anchor="center")
    aB = fw(t, s19, s20 - 0.2)
    if aB > 0:
        card(c, *CARD_R, a=aB)
        mapas.draw_globe(c, 470, 500, 250, aB * ep(t, C["19.d"], 0.5), lon0=0, lat0=25, grat_lats=(60,), grat_lons=tuple(range(-180, 180, 20)))
        p, q = mapas.globe_xy(-10, 60, 470, 500, 250, 0, 25), mapas.globe_xy(10, 60, 470, 500, 250, 0, 25)
        line(c, p[0], p[1], q[0], q[1], RED, aB * ep(t, C["19.d"], 0.5), 8)
        pill(c, "no globo: os meridianos SE ENCONTRAM", 470, 200, INK, size=24, a=aB * ep(t, C["19.d"], 0.5), anchor="center")
        ae = aB * ep(t, C["19.e"], 0.5)
        gx, gy, gw, gh = 1000, 260, 640, 460
        for k in range(9):
            line(c, gx + k * gw / 8, gy, gx + k * gw / 8, gy + gh, "#93C5FD", ae, 3)
        for k in range(5):
            line(c, gx, gy + k * gh / 4, gx + gw, gy + k * gh / 4, "#93C5FD", ae, 2)
        pill(c, "no mapa: retas PARALELAS", gx + gw / 2, 200, INK, size=24, a=ae, anchor="center")
        af = aB * ep(t, C["19.f"], 0.5)
        rrect(c, gx + 3 * gw / 8, gy + 40, gw / 4, 60, 0, RED, 0.35 * af)
        arrow(c, gx + gw / 2, gy + 130, gx + gw / 2 - 200, gy + 130, AMBER, af, 6, 22)
        arrow(c, gx + gw / 2, gy + 130, gx + gw / 2 + 200, gy + 130, AMBER, af, 6, 22)
        pill(c, "perto dos polos: ESTICA para os lados", gx + gw / 2, gy + gh + 60, AMBER, size=26, a=af, anchor="center")
    aC = ep(t, s20, 0.5)
    if aC > 0:
        card(c, *CARD_R, a=aC)
        data = [(0, "× 1"), (30, "× 1,3"), (45, "× 2"), (60, "× 4"), (70, "× 8,5")]
        x, base = 260, 620
        for lat, lab in data:
            s = 44 / math.cos(math.radians(lat))
            hi = lat >= 60
            a = aC * ep(t, C["20.h"] + (0.6 if lat == 60 else 0), 0.5) if hi else aC
            if lat == 70:
                a = aC * ep(t, C["20.j"], 0.5)
            rrect(c, x, base - s, s, s, 6, RED if hi else BLUE, a * 0.85)
            text(c, f"{lat}°", x + s / 2, base + 50, 32, "black", INK2, a)
            text(c, lab, x + s / 2, base - s - 20, 32, "black", RED if hi else INK, a)
            x += s + 60
        text(c, "a MESMA área de verdade, desenhada em cada latitude", 900, 730, 28, "bold", GRAY, aC)
        ah = ep(t, C["20.h"], 0.5)
        text(c, "a 60°: largura × 2", 1460, 340, 40, "black", AMBER, ah)
        text(c, "altura × 2", 1460, 400, 40, "black", AMBER, ah)
        result_box(c, "área × 4", 1460, 520, 56, ep(t, C["20.i"], 0.5), RED)


def b_truesize(c, t, C, B):
    head(c, t, B["start"], "O TAMANHO DE VERDADE", "ARRASTANDO A GROENLÂNDIA", RED)
    at = ep(t, C["21.t"], 0.5)
    merc(c, MAP, at)
    on_merc(c, mapas.continent_rings("Africa"), MAP, at * 0.9, "#CBD5E1", "#64748B")
    f = ease_io(clamp((t - C["21.a"]) / max(1.0, C["21.b"] - C["21.a"] + 0.4)))
    rings = mapas.moved_rings("Greenland", (22, 4), f)
    on_merc(c, rings, MAP, at, "#F59E0B", "#B45309")
    cx, cy = mapas.to_xy(MAP, (lerp(-41, 22, f), lerp(73, 4, f)), "mercator", lat=MLAT)
    pill(c, "Groenlândia", cx, cy - 70 - 40 * (1 - f), INK, size=24, a=at, anchor="center")
    pill(c, "em ALTA latitude: inflada", 520, 840, AMBER, size=26, a=at * (1 - ep(t, C["21.b"], 0.4)), anchor="center")
    pill(c, "ENCOLHE!", W / 2, 840, RED, size=36, a=ep(t, C["21.b"], 0.5), anchor="center")
    pill(c, "Groenlândia ≈ 2,2 mi km² · África ≈ 30 mi km²", 1350, 840, INK, size=24, a=ep(t, C["21.c"], 0.5), anchor="center")


# ======================================================================
# bloco e: Peters e comparação
# ======================================================================

def b_peters(c, t, C, B):
    head(c, t, B["start"], "PETERS (anos 1970)", "CILÍNDRICA E EQUIVALENTE", GREEN)
    R = (420, 175, 1080, 640)
    at = ep(t, C["22.t"], 0.5)
    mapas.draw_world(c, R, at, proj="peters")
    pill(c, "EQUIVALENTE: áreas REAIS", 260, 380, GREEN, size=26, a=ep(t, C["22.a"], 0.5), anchor="center")
    pill(c, "África grande · Europa menor", 260, 480, INK, size=22, a=ep(t, C["22.b"], 0.5), anchor="center")
    ac = ep(t, C["22.c"], 0.5)
    for k, la in enumerate((0, 35, 60, -35)):
        mapas.tissot(c, R, (110, la), 6, ac, RED, proj="peters")
    pill(c, "formas ESTICADAS", 1660, 420, RED, size=26, a=ac, anchor="center")


def b_lado(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO", "", PURPLE)
    for k, (cue, proj, nome, ok, err) in enumerate((("23.a", "mercator", "MERCATOR", "forma ✓", "área ✗"),
                                                    ("23.b", "peters", "PETERS", "área ✓", "forma ✗"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 160 + k * 820
        card(c, x, 170 + dy, 780, 620, a)
        text(c, nome, x + 390, 230 + dy, 40, "black", BLUE if k == 0 else GREEN, a)
        if proj == "mercator":
            mapas.draw_world(c, (x + 40, 260 + dy, 700, 400), a, proj="mercator", lat=MLAT)
        else:
            mapas.draw_world(c, (x + 40, 260 + dy, 700, 400), a, proj="peters")
        pill(c, ok, x + 260, 720 + dy, GREEN, size=30, a=a, anchor="center", bounds=(0, 1920))
        pill(c, err, x + 520, 720 + dy, RED, size=30, a=a, anchor="center", bounds=(0, 1920))
    pill(c, "nenhuma é o mapa CERTO: cada uma serve para uma coisa", W / 2, 840, AMBER, size=28, a=ep(t, C["23.c"], 0.5),
         anchor="center")


# ======================================================================
# bloco f: a política dos mapas
# ======================================================================

def b_politica(c, t, C, B):
    head(c, t, B["start"], "QUEM DECIDIU?", "A POLÍTICA DOS MAPAS", PURPLE)
    at = ep(t, C["24.t"], 0.5)
    merc(c, MAP, at)
    ex, ey = mapas.to_xy(MAP, (10, 50), "mercator", lat=MLAT)
    if at > 0:
        c.drawCircle(ex, ey, 70 + 6 * math.sin(t * 4), paint(AMBER, at, stroke=6))
    pill(c, "Europa no CENTRO", ex, ey - 100, AMBER, size=26, a=at, anchor="center")
    pill(c, "norte EM CIMA", 330, 230, AMBER, size=26, a=at, anchor="center")
    pill(c, "são CONVENÇÕES (combinados), não fatos", W / 2, 840, BLUE, size=28, a=fw(t, C["24.a"], C["24.c"] - 0.2), anchor="center")
    pill(c, "países ricos do norte AUMENTADOS", 1450, 260, RED, size=26, a=ep(t, C["24.b"], 0.5), anchor="center")
    pill(c, "EUROCENTRISMO = ver o mundo com a Europa no centro", W / 2, 840, BLUE, size=28, a=ep(t, C["24.c"], 0.5),
         anchor="center")


def b_sulcima(c, t, C, B):
    head(c, t, B["start"], "SUL EM CIMA", "ESTÁ ERRADO?", GREEN)
    at = ep(t, C["25.t"], 0.5)
    rot = 180 * ease_io(ep(t, C["25.t"] + 0.6, 1.6))
    R = (300, 215, 1320, 580)
    c.save(); c.translate(W / 2, 505); c.rotate(rot); c.translate(-W / 2, -505)
    merc(c, R, at)
    c.restore()
    pill(c, "tão correto quanto o tradicional", W / 2, 172, GREEN, size=30, a=ep(t, C["25.a"], 0.5), anchor="center")
    pill(c, "no espaço não existe EM CIMA", 520, 850, BLUE, size=26, a=ep(t, C["25.b"], 0.5), anchor="center")
    pill(c, "todo mapa é uma ESCOLHA", 1400, 850, AMBER, size=28, a=ep(t, C["25.c"], 0.5), anchor="center")


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "A MERCATOR MOSTRA AS ÁREAS REAIS?", RED)
    erro_tiles(c, t, [(C["26.a"], "O ERRO", ["Mercator mostra", "as áreas reais"], RED),
                      (C["26.b"], "POR QUE PARECE CERTO", ["é o mapa que", "a gente vê", "a vida inteira"], AMBER),
                      (C["26.c"], "A CORREÇÃO", ["é CONFORME:", "guarda a forma e", "INFLA os polos"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "A PETERS PRESERVA AS FORMAS?", RED)
    erro_tiles(c, t, [(C["27.a"], "O ERRO", ["Peters preserva", "as formas"], RED),
                      (C["27.b"], "POR QUE PARECE CERTO", ["é a projeção", "\"mais justa\""], AMBER),
                      (C["27.c"], "A CORREÇÃO", ["é EQUIVALENTE:", "acerta a área e", "ESTICA as formas"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "DISTORÇÃO MAIOR ONDE TOCA?", RED)
    erro_tiles(c, t, [(C["28.a"], "O ERRO", ["distorção maior", "onde o cilindro", "toca o globo"], RED),
                      (C["28.b"], "POR QUE PARECE CERTO", ["é ali que", "\"acontece\"", "a projeção"], AMBER),
                      (C["28.c"], "A CORREÇÃO", ["onde toca:", "distorção MENOR", "cresce longe dali"], GREEN)])


# ======================================================================
# questão estilo ENEM
# ======================================================================

ALTS = [("A", "equivalente: preserva as formas, reduz áreas no Equador", "30.a", "31.a", "equivalente guarda a ÁREA, não a forma"),
        ("B", "azimutal no Polo Norte: amplia perto do contato", "30.b", "31.b", "perto do contato a distorção é MENOR"),
        ("C", "cilíndrica: exagera no Equador, onde toca o globo", "30.c", "31.c", "onde toca, o erro é MENOR"),
        ("D", "cônica: fiel nas latitudes médias", "30.d", "32.d", "não é o mapa-múndi escolar"),
        ("E", "cilíndrica CONFORME: preserva formas, infla rumo aos polos", "30.e", None, "")]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "A GROENLÂNDIA DO MAPA ESCOLAR", BLUE)
    card(c, *CARD_R)
    text(c, "No mapa escolar, a Groenlândia parece do tamanho da África,", 200, 230, 32, "black", INK, ep(t, C["29.e1"], 0.5), align="left")
    text(c, "que é 14 vezes maior. Isso acontece porque a projeção é...", 200, 280, 32, "black", INK, ep(t, C["29.e2"], 0.5), align="left")
    aok = ep(t, C["32.e"], 0.5)
    for k, (L, s, cue_in, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[cue_in])
        y = 370 + k * 88 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 190, y - 36, 1540, 72, 14, GREEN, 0.15 * aok)
        badge_num(c, L, 230, y - 10, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 275, y, 30, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 270, y - 10, 280 + text_w(s, "black", 30), y - 10, ax, RED, ax)
            text(c, why, 1720, y + 4, 22, "black", RED, ax, align="right")
    ap = ep(t, C["30.p"], 0.5) * (1 - prog(t, C["31.t"] - 0.3, 0.4))
    if ap > 0:
        rrect(c, 1390, 170, 340, 96, 24, AMBER, ap, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(1418, 192, 14, 52), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(1444, 192, 14, 52), paint(INK, ap))
        text_mid(c, "PAUSE E TENTE", 1600, 218, 30, "black", INK, ap)
    pill(c, "RESPOSTA: E · a Mercator", 1560, 230, GREEN, size=26, a=ep(t, C["32.x"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CURVAS DE NÍVEL", PURPLE)
    card(c, *CARD_R)
    at = ep(t, C["34.t"], 0.5)
    rrect(c, 260, 360, 640, 260, 8, "#FFFFFF", at)
    if at > 0:
        c.drawRect(skia.Rect.MakeXYWH(260, 360, 640, 260), paint(INK2, at, stroke=3))
    text(c, "mapa plano", 580, 680, 30, "black", INK2, at)
    aa = ep(t, C["34.a"], 0.5)
    p = skia.Path(); p.moveTo(1000, 700)
    p.cubicTo(1120, 700, 1180, 330, 1300, 330); p.cubicTo(1400, 330, 1420, 520, 1500, 520); p.cubicTo(1580, 520, 1620, 700, 1700, 700)
    p.close()
    if aa > 0:
        c.drawPath(p, paint("#86C18A", aa)); c.drawPath(p, paint("#5FA463", aa, stroke=4))
    ab = ep(t, C["34.b"], 0.5)
    for k, y in enumerate((620, 540, 460, 380)):
        hline(c, 1000, 1700, y, "#A16207", ab * ep(t, C["34.b"] + 0.3 * k, 0.4), 3, (12, 8))
    pill(c, "como mostrar ALTURA no papel?", 1350, 250, AMBER, size=28, a=ab, anchor="center")
    pill(c, "EPISÓDIO 4: CURVAS DE NÍVEL", W / 2, 800, PURPLE, size=34, a=ep(t, C["34.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Achava a Groenlândia do tamanho da África?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prelat=b_prelat, preforma=b_preforma, laranja=b_laranja, projecao=b_projecao,
              lampada=b_lampada, superficies=b_superficies, toque=b_toque, conserva=b_conserva, regra=b_regra, recap=b_recap,
              mercator=b_mercator, truesize=b_truesize, peters=b_peters, lado=b_lado, politica=b_politica, sulcima=b_sulcima,
              erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, questao=b_questao, ponte=b_ponte, cta=b_cta)
