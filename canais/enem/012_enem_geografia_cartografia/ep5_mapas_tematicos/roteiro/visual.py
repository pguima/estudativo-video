"""Visual — Cartografia, Episódio 5: Mapas temáticos e anamorfoses (aula para iniciantes, tema claro).
Cores com função: azul = definição · âmbar = atenção/armadilha · verde = atalho/dica · vermelho = erro.
A anamorfose é um "mapa de balões": cada país real (Natural Earth) é inflado/murchado em torno do próprio centro,
na proporção (dado do país ÷ média mundial por área). Não é um cartograma exato: é a analogia dos balões, com dados reais.
"""
import json
import math
from functools import lru_cache
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa
import mapas

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia_ep5_mapas_tematicos.mp4"
CARD_R = (140, 150, 1640, 690)
MAP = (220, 190, 1480, 600)
LAT = (-58, 84)
RAIN = ["#EFF6FF", "#BFDBFE", "#60A5FA", "#1D4ED8"]


# ======================================================================
# países e balões
# ======================================================================

@lru_cache(None)
def paises():
    gj = json.loads((mapas.DADOS / "ne_110m_admin_0_countries.geojson").read_text(encoding="utf-8"))
    out = []
    for f in gj["features"]:
        p = f["properties"]
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        rings = [[tuple(q[:2]) for q in poly[0]] for poly in polys]
        area = 0.0
        for r in rings:
            un, prev = [], None
            for x, y in r:                      # desenrola o salto de 180° (Rússia, Fiji...)
                if prev is not None:
                    while x - prev > 180:
                        x -= 360
                    while x - prev < -180:
                        x += 360
                un.append((x, y)); prev = x
            ra = 0.0
            for (x0, y0), (x1, y1) in zip(un, un[1:] + un[:1]):
                ra += (x0 - x1) * (math.sin(math.radians(y0)) + math.sin(math.radians(y1)))
            area += abs(ra) / 2                # área equivalente (proporcional à área real na esfera)
        if p.get("CONTINENT") == "Antarctica" or area < 0.5:
            continue
        out.append(dict(nome=p.get("NAME"), rings=rings, area=area, pop=max(p.get("POP_EST") or 0, 1),
                        pib=max(p.get("GDP_MD") or 0, 1)))
    return out


@lru_cache(None)
def fator(chave):
    ps = paises()
    tot_a = sum(p["area"] for p in ps)
    tot_v = sum(p[chave] for p in ps)
    return {p["nome"]: max(0.3, min(3.2, math.sqrt((p[chave] / tot_v) / (p["area"] / tot_a)))) for p in ps}


def centro(rings, rect):
    big = max(rings, key=len)
    pts = [mapas.to_xy(rect, q, lat=LAT) for q in big]
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)


def balao_map(c, rect, a, k, chave="pop", destaque=()):
    """mapa-múndi com cada país inflado (k=1) ou no tamanho normal (k=0)"""
    if a <= 0:
        return
    fx, fy, fw, fh = mapas.world_frame(rect, "equi", (-180, 180), LAT)
    rrect(c, fx, fy, fw, fh, 18, mapas.SEA, a)
    F = fator(chave)
    ps = sorted(paises(), key=lambda p: -p["area"])
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, fy, fw, fh), 18, 18), True)
    for p in ps:
        s = lerp(1.0, F[p["nome"]], k)
        cx, cy = centro(p["rings"], rect)
        if s > 1.05:
            col = mix(mapas.LAND, "#F59E0B", clamp((s - 1) / 1.5) * k)
        elif s < 0.95:
            col = mix(mapas.LAND, "#93C5FD", clamp((1 - s) / 0.6) * k)
        else:
            col = mapas.LAND
        if p["nome"] in destaque:
            col = mix(col, "#E5484D", 0.6)
        c.save(); c.translate(cx, cy); c.scale(s, s); c.translate(-cx, -cy)
        mapas.draw_rings_on(c, p["rings"], rect, a, col, mapas.COAST, lat=LAT)
        c.restore()
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, fy, fw, fh), 18, 18), paint(INK2, a, stroke=3))


def label_pais(c, nome, txt, rect, k, chave, col, a, dy=0):
    p = next(q for q in paises() if q["nome"] == nome)
    cx, cy = centro(p["rings"], rect)
    pill(c, txt, cx, cy + dy, col, size=24, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# mapa temático inventado (estado fictício em hexágonos)
# ======================================================================

HEX = [((0, 0), 3), ((1, 0), 2), ((2, 0), 1), ((0, 1), 3), ((1, 1), 2), ((2, 1), 1), ((3, 1), 0),
       ((0, 2), 3), ((1, 2), 3), ((2, 2), 2), ((3, 2), 1), ((1, 3), 2), ((2, 3), 1)]


def hexagon(c, cx, cy, r, fill, a, stroke="#FFFFFF", w=4):
    p = skia.Path()
    for k in range(6):
        ang = math.radians(60 * k + 30)
        (p.moveTo if k == 0 else p.lineTo)(cx + r * math.cos(ang), cy + r * math.sin(ang))
    p.close()
    if fill:
        c.drawPath(p, paint(fill, a))
    c.drawPath(p, paint(stroke, a, stroke=w))


def estado(c, x, y, r, a, cores=None, valores=None, hi=None):
    """desenha o estado fictício; cores: função(classe)->cor; devolve centros"""
    cen = []
    for (q, rr), cl in HEX:
        cx = x + q * r * math.sqrt(3) + (rr % 2) * r * math.sqrt(3) / 2
        cy = y + rr * r * 1.5
        col = cores(cl) if cores else RAIN[cl]
        hexagon(c, cx, cy, r, col, a)
        cen.append((cx, cy, cl))
    if hi is not None and a > 0:
        for cx, cy, cl in cen:
            if cl == hi:
                hexagon(c, cx, cy, r - 4, None, a, stroke="#E5484D", w=7)
    return cen


def legenda_box(c, x, y, a, itens, titulo, hi=None):
    rrect(c, x, y, 330, 60 + 52 * len(itens), 14, "#FFFFFF", a, shadow=True)
    text(c, titulo, x + 20, y + 40, 24, "black", INK, a, align="left")
    for k, (col, lab) in enumerate(itens):
        yy = y + 60 + k * 52
        rrect(c, x + 20, yy, 44, 34, 6, col, a)
        if a > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + 20, yy, 44, 34), paint(INK2, a * 0.4, stroke=2))
        text(c, lab, x + 80, yy + 26, 24, "bold", INK, a, align="left")
    if hi is not None and a > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 6, y - 6, 342, 72 + 52 * len(itens)), 18, 18),
                    paint(AMBER, a * (0.6 + 0.4 * math.sin(hi * 6)), stroke=6))


def norte(c, x, y, a):
    arrow(c, x, y + 40, x, y - 30, INK, a, 5, 18)
    text(c, "N", x, y - 44, 30, "black", INK, a)


def escala_barra(c, x, y, a, lab="0 — 100 km"):
    if a <= 0:
        return
    for k in range(2):
        c.drawRect(skia.Rect.MakeXYWH(x + k * 80, y, 80, 12), paint(INK if k == 0 else "#FFFFFF", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, 160, 12), paint(INK, a, stroke=2))
    text(c, lab, x + 80, y + 40, 22, "bold", INK2, a)


# ======================================================================
# utilidades de aula
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


def checklist(c, t, cues, x, y, dy, a_all=1.0, done=()):
    itens = ["Título e fonte", "Legenda", "Escala", "Orientação e projeção"]
    for k, (s, tc) in enumerate(zip(itens, cues)):
        a, d = rise(t, tc)
        a *= a_all
        yy = y + k * dy + d
        rrect(c, x, yy - 32, 500, 64, 16, "#FFFFFF", a, shadow=True)
        ok = k in done
        if ok:
            check_icon(c, x + 40, yy, 20, a, GREEN)
        else:
            badge_num(c, k + 1, x + 40, yy, a, 20, bg=BLUE)
        text_mid(c, s, x + 80, yy, 32, "black", GREEN if ok else INK, a, align="left")


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    a0 = ep(t, B["start"] + 0.2, 0.6)
    k = ease_io(ep(t, C["01.a"], 2.5))
    balao_map(c, MAP, a0, k)
    label_pais(c, "Canada", "Canadá quase some", MAP, k, "pop", BLUE, ep(t, C["01.a"] + 1.0, 0.5), dy=-30)
    label_pais(c, "India", "Índia gigante", MAP, k, "pop", RED, ep(t, C["01.b"], 0.5), dy=10)
    pill(c, "tamanho = número de PESSOAS", W / 2, 150, AMBER, size=30, a=ep(t, B["start"] + 0.6, 0.5), anchor="center")
    pill(c, "cai no ENEM", W / 2, 830, GREEN, size=30, a=ep(t, C["01.c"], 0.5), anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Ler qualquer\nmapa em\n4 passos", C["02.a"], BLUE),
                     ("2", "Não confundir\nanamorfose\ncom projeção", C["02.b"], PURPLE)], cw=520, chh=420, title_size=40)


def b_prereq(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITOS", "EPISÓDIOS 3 E 1", BLUE)
    aa, ab = ep(t, C["03.a"], 0.5), ep(t, C["03.b"], 0.5)
    card(c, 200, 190, 700, 600, aa)
    if aa > 0:
        mapas.draw_world(c, (240, 260, 620, 330), aa, proj="peters")
    text(c, "EQUIVALENTE (ep. 3)", 550, 650, 36, "black", GREEN, aa)
    text(c, "mantém as ÁREAS reais", 550, 710, 30, "black", INK2, aa)
    card(c, 1020, 190, 700, 600, ab)
    text(c, "1 : 100 000", 1370, 420, 80, "black", INK, ab)
    text(c, "ESCALA (ep. 1)", 1370, 650, 36, "black", BLUE, ab)
    text(c, "quanto o mundo encolheu", 1370, 710, 30, "black", INK2, ab)


# ======================================================================
# bloco a: mapa temático
# ======================================================================

def b_previsao(c, t, C, B):
    head(c, t, B["start"], "TRÊS MAPAS DO DIA A DIA", "O QUE ELES TÊM EM COMUM?", BLUE)
    data = [("04.t", "previsão do tempo", "chuva"), ("04.a", "eleição", "voto"), ("04.b", "trânsito", "ruas paradas")]
    for k, (cue, nome, tema) in enumerate(data):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 520
        card(c, x, 190 + dy, 480, 560, a)
        R = (x + 30, 250 + dy, 420, 380)
        mapas.draw_world(c, R, a, lon=(-75, -33), lat=(-35, 6), arquivo="ne_50m_land.geojson")
        mapas.draw_country_on(c, "Brazil", R, a, fill="#86C18A", stroke="#5FA463", lon=(-75, -33), lat=(-35, 6))
        if k == 0:
            for cx, cy, rr in ((x + 260, 360, 90), (x + 300, 470, 60)):
                c.drawCircle(cx, cy + dy, rr, paint("#3B82F6", a * 0.45))
        elif k == 1:
            for cx, cy, col in ((x + 220, 340, RED), (x + 320, 420, BLUE), (x + 260, 520, RED), (x + 200, 440, BLUE)):
                c.drawCircle(cx, cy + dy, 34, paint(col, a * 0.6))
        else:
            for k2 in range(5):
                line(c, x + 120 + k2 * 50, 330 + dy, x + 160 + k2 * 50, 560 + dy, RED if k2 % 2 else AMBER, a, 7)
        text(c, nome, x + 240, 690 + dy, 34, "black", INK, a)
        text(c, tema, x + 240, 730 + dy, 28, "bold", INK2, a)
    pill(c, "têm algo em comum", W / 2, 820, AMBER, size=28, a=ep(t, C["04.c"], 0.5), anchor="center")


def b_tematico(c, t, C, B):
    head(c, t, B["start"], "MAPA TEMÁTICO", "UM ASSUNTO SOBRE O MAPA", BLUE)
    card(c, *CARD_R)
    R = (240, 230, 560, 520)
    lon, lat = (-75, -33), (-35, 6)
    at = ep(t, C["05.t"], 0.5)
    mapas.draw_world(c, R, at, lon=lon, lat=lat, arquivo="ne_50m_land.geojson")
    ab = ep(t, C["05.b"], 0.5)
    pill(c, "BASE CARTOGRÁFICA = o mapa de fundo", 520, 210, BLUE, size=24, a=ab, anchor="center")
    aa = ep(t, C["05.a"], 0.8)
    mapas.draw_country_on(c, "Brazil", R, aa, fill="#60A5FA", stroke="#1D4ED8", lon=lon, lat=lat)
    arrow(c, 860, 490, 990, 490, INK2, aa, 6, 22)
    ac = ep(t, C["05.c"], 0.5)
    pill(c, "MAPA TEMÁTICO = base + um ASSUNTO", 1340, 420, BLUE, size=28, a=ac, anchor="center")
    ad = ep(t, C["05.d"], 0.5)
    for k, s in enumerate(("clima", "população", "desmatamento", "votos")):
        pill(c, s, 1150 + (k % 2) * 300, 540 + (k // 2) * 80, PURPLE, size=26, a=ad * ep(t, C["05.d"] + 0.3 * k, 0.4), anchor="center")
    ae = ep(t, C["05b.e"], 0.5)
    pill(c, "o território é o MESMO; muda o tema", 1340, 720, AMBER, size=26, a=ae, anchor="center")
    pill(c, "1ª pergunta: QUAL É O TEMA?", 1340, 800, GREEN, size=28, a=ep(t, C["05b.f"], 0.5), anchor="center")


# ======================================================================
# bloco b: a legenda
# ======================================================================

def b_legenda(c, t, C, B):
    head(c, t, B["start"], "A LEGENDA", "PARTE DO MAPA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    estado(c, 380, 330, 70, 1)
    legenda_box(c, 1100, 300, aa, [(RAIN[0], "pouca chuva"), (RAIN[1], ""), (RAIN[2], ""), (RAIN[3], "muita chuva")], "Chuva por ano",
                hi=t if aa > 0.5 else None)
    pill(c, "LEGENDA = explica cada cor e símbolo", 1265, 230, BLUE, size=24, a=aa, anchor="center")
    pill(c, "sem legenda, as cores não dizem nada", 1265, 760, AMBER, size=26, a=ep(t, C["06.b"], 0.5), anchor="center")


def b_tipos(c, t, C, B):
    head(c, t, B["start"], "TRÊS JEITOS DE PINTAR", "UM TEMA", BLUE)
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    clima = ["#FCD34D", "#86EFAC", "#C4B5FD", "#FCA5A5"]
    for k, (cue, nome, sub, col) in enumerate((("07.a", "GRADAÇÃO", "claro → escuro = quantidade", BLUE),
                                              ("08.b", "CORES DIFERENTES", "categorias sem ordem", PURPLE),
                                              ("08.c", "SÍMBOLOS PROPORCIONAIS", "bolinha cresce com o total", GREEN))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 190 + dy, cw, 600, a)
        text(c, nome, x + cw / 2, 250 + dy, 32, "black", col, a)
        if k == 0:
            estado(c, x + 110, 340 + dy, 46, a)
        elif k == 1:
            estado(c, x + 110, 340 + dy, 46, a, cores=lambda cl: clima[cl])
        else:
            cen = estado(c, x + 110, 340 + dy, 46, a, cores=lambda cl: "#E5E7EB")
            for j, (cx, cy, cl) in enumerate(cen[::2]):
                c.drawCircle(cx, cy, 8 + 7 * cl, paint(GREEN, a * 0.75))
        text(c, sub, x + cw / 2, 720 + dy, 28, "black", INK2, a)


# ======================================================================
# bloco c: anamorfose (balões)
# ======================================================================

def b_balao(c, t, C, B):
    head(c, t, B["start"], "UM MAPA DE BALÕES", "", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    data = [("09.c", 1.6, "#F59E0B", "muita gente: INCHA"), ("09.d", 0.55, "#93C5FD", "pouca gente: MURCHA")]
    for k, (cue, s_end, col, lab) in enumerate(data):
        x = 560 + k * 800
        s = lerp(1.0, s_end, ease_io(ep(t, C[cue], 1.2)))
        r = 110 * s
        line(c, x, 640, x, 520 + r * 0.2, INK2, aa, 3)
        if aa > 0:
            c.drawOval(skia.Rect.MakeLTRB(x - r, 450 - r * 1.15, x + r, 450 + r * 0.9), paint(col if s != 1 else mapas.LAND, aa))
            c.drawOval(skia.Rect.MakeLTRB(x - r, 450 - r * 1.15, x + r, 450 + r * 0.9), paint(INK2, aa, stroke=3))
        rrect(c, x - 40, 640, 80, 24, 6, INK2, aa)
        pill(c, lab, x, 740, col, size=28, a=ep(t, C[cue], 0.5), anchor="center")
    pill(c, "cada país = um balão PRESO no seu lugar", W / 2, 210, INK, size=28, a=aa, anchor="center")
    pill(c, "enche conforme um NÚMERO", W / 2, 280, BLUE, size=26, a=ep(t, C["09.b"], 0.5), anchor="center")


def b_morph(c, t, C, B):
    head(c, t, B["start"], "ANAMORFOSE DE POPULAÇÃO", "DADOS REAIS", AMBER)
    k = ease_io(ep(t, C["10.t"] + 0.6, 3.0))
    balao_map(c, MAP, 1, k, destaque=("Brazil",) if t >= C["11b.g"] else ())
    aa, ab = ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5)
    label_pais(c, "India", "Índia", MAP, k, "pop", RED, aa, dy=10)
    label_pais(c, "China", "China", MAP, k, "pop", RED, aa, dy=-20)
    label_pais(c, "Canada", "Canadá", MAP, k, "pop", BLUE, ab)
    label_pais(c, "Russia", "Rússia", MAP, k, "pop", BLUE, ab)
    label_pais(c, "Australia", "Austrália", MAP, k, "pop", BLUE, ab)
    pill(c, "ANAMORFOSE (cartograma) = tamanho é um DADO", W / 2, 150, BLUE, size=28, a=fw(t, C["11.c"], C["11b.g"] - 0.2), anchor="center")
    pill(c, "a POSIÇÃO continua a mesma", 560, 840, GREEN, size=26, a=fw(t, C["11.e"], C["11b.g"] - 0.2), anchor="center")
    pill(c, "as formas deformam DE PROPÓSITO", 1360, 840, AMBER, size=26, a=fw(t, C["11.f"], C["11b.g"] - 0.2), anchor="center")
    ag = ep(t, C["11b.g"], 0.5)
    label_pais(c, "Brazil", "Brasil: +200 milhões", MAP, k, "pop", INK, ag, dy=-60)
    pill(c, "muito território → até ENCOLHE um pouco", W / 2, 840, AMBER, size=28, a=ep(t, C["11b.h"], 0.5), anchor="center")


def b_pib(c, t, C, B):
    head(c, t, B["start"], "OUTRO DADO", "PIB", AMBER)
    k = ease_io(ep(t, C["12.b"], 2.5))
    balao_map(c, MAP, 1, k, chave="pib")
    pill(c, "PIB = tudo o que um país produz em 1 ano", W / 2, 150, BLUE, size=28, a=ep(t, C["12.a"], 0.5), anchor="center")
    label_pais(c, "United States of America", "EUA incha", MAP, k, "pib", RED, ep(t, C["12.b"] + 1.0, 0.5), dy=-40)
    label_pais(c, "Dem. Rep. Congo", "África murcha", MAP, k, "pib", BLUE, ep(t, C["12.c"], 0.5))
    pill(c, "a anamorfose mostra a DESIGUALDADE", W / 2, 840, GREEN, size=30, a=ep(t, C["12.d"], 0.5), anchor="center")


# ======================================================================
# recapitulação (meio e fim)
# ======================================================================

def b_recap(c, t, C, B):
    sid = "13" if B["start"] < C["26"] - 1 else "26"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    badge_row(c, t, [(C[sid + ".a"], "A resposta costuma estar na LEGENDA", BLUE),
                     (C[sid + ".b"], "Anamorfose: tamanho é DADO, não território", AMBER),
                     (C[sid + ".c"], "Projeção mantém · anamorfose distorce", PURPLE)], 220, 330, 160, 42)


# ======================================================================
# bloco d: anamorfose não é projeção
# ======================================================================

def b_naoproj(c, t, C, B):
    head(c, t, B["start"], "ANAMORFOSE É PROJEÇÃO?", "NÃO", RED)
    aa = ep(t, C["14.a"], 0.5)
    for k, (cue, tt, sub, col) in enumerate((("14.b", "PROJEÇÃO", "TENTA manter a realidade", BLUE),
                                              ("14.c", "ANAMORFOSE", "ABANDONA a área real", AMBER))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 820
        card(c, x, 190 + dy, 700, 560, a)
        text(c, tt, x + 350, 250 + dy, 40, "black", col, a)
        R = (x + 40, 290 + dy, 620, 300)
        if k == 0:
            mapas.draw_world(c, R, a, proj="peters")
        else:
            balao_map(c, R, a, 1.0)
        text(c, sub, x + 350, 680 + dy, 32, "black", INK, a)
    check_icon(c, W / 2, 470, 30, aa * (1 - ep(t, C["14.b"], 0.4)), RED, "x")
    pill(c, "área = PIB ou população?  → anamorfose", W / 2, 830, GREEN, size=28, a=ep(t, C["14.d"], 0.5), anchor="center")


# ======================================================================
# bloco e: roteiro de leitura e aplicação
# ======================================================================

def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "COMO LER QUALQUER MAPA", "4 PASSOS", GREEN)
    card(c, *CARD_R)
    checklist(c, t, [C["15.a"], C["15.b"], C["16.c"], C["16.d"]], 300, 300, 120)
    pill(c, "a resposta costuma estar AQUI", 1080, 420, AMBER, size=26, a=ep(t, C["15.b"] + 1.5, 0.5))
    notes = [("15.a", "o quê, e de quando"), ("16.c", "grande ou pequena?"), ("16.d", "onde fica o norte?")]
    for cue, s in notes:
        yy = {"15.a": 300, "16.c": 540, "16.d": 660}[cue]
        text(c, s, 1080, yy + 10, 28, "black", INK2, ep(t, C[cue] + 0.6, 0.4), align="left")


def b_aplica(c, t, C, B):
    head(c, t, B["start"], "APLICANDO OS 4 PASSOS", "NUM MAPA INVENTADO", GREEN)
    card(c, 140, 150, 980, 690)
    a0 = ep(t, C["17.t"], 0.5)
    ta = ep(t, C["17.a"], 0.5)
    text(c, "Chuva por ano — estado fictício", 630, 215, 30, "black", INK, a0)
    text(c, "Fonte: dados inventados, 2025", 630, 250, 22, "bold", GRAY, a0)
    if ta > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(320, 180, 620, 90), 14, 14), paint(AMBER, ta * fw(t, C["17.a"], C["17.b"] - 0.2), stroke=5))
    hi = 3 if t >= C["18.c"] else None
    estado(c, 250, 380, 62, a0, hi=hi)
    lb = fw(t, C["17.b"], C["18.d"] - 0.2)
    legenda_box(c, 800, 330, a0, [(RAIN[0], "menos chuva"), (RAIN[1], ""), (RAIN[2], ""), (RAIN[3], "mais chuva")], "Legenda",
                hi=t if lb > 0.5 else None)
    pill(c, "litoral: chove MAIS", 420, 790, RED, size=24, a=ep(t, C["18.c"], 0.5), anchor="center")
    ad = ep(t, C["18.d"], 0.5)
    escala_barra(c, 860, 650, a0)
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(840, 630, 200, 80), 14, 14), paint(AMBER, ad * fw(t, C["18.d"], C["18.e"] - 0.2), stroke=5))
    norte(c, 1040, 740, a0)
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        c.drawCircle(1040, 720, 56, paint(AMBER, ae * fw(t, C["18.e"], C["18.f"] - 0.2), stroke=5))
    done = tuple(k for k, cue in enumerate(("17.b", "18.c", "18.e", "18.f")) if t >= C[cue])
    checklist(c, t, [C["17.t"]] * 4, 1180, 300, 110, done=done)
    pill(c, "mapa lido, sem adivinhar", 1430, 790, GREEN, size=28, a=ep(t, C["18.f"], 0.5), anchor="center")


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "ANAMORFOSE = PROJEÇÃO EQUIVALENTE?", RED)
    erro_tiles(c, t, [(C["19.a"], "O ERRO", ["anamorfose =", "projeção equivalente"], RED),
                      (C["19.b"], "POR QUE PARECE CERTO", ["as duas falam", "de ÁREA"], AMBER),
                      (C["19.c"], "A CORREÇÃO", ["equivalente MANTÉM", "a área; anamorfose", "TROCA por um dado"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "MAIOR NA ANAMORFOSE = MAIS TERRITÓRIO?", RED)
    erro_tiles(c, t, [(C["20.a"], "O ERRO", ["país maior =", "mais território"], RED),
                      (C["20.b"], "POR QUE PARECE CERTO", ["no mapa comum", "é assim"], AMBER),
                      (C["20.c"], "A CORREÇÃO", ["o tamanho é o DADO:", "Índia grande pela", "POPULAÇÃO"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "IGNORAR A LEGENDA", RED)
    erro_tiles(c, t, [(C["21.a"], "O ERRO", ["adivinhar", "pelas cores"], RED),
                      (C["21.b"], "POR QUE PARECE CERTO", ["vermelho parece", "ruim; verde, bom"], AMBER),
                      (C["21.c"], "A CORREÇÃO", ["cada mapa escolhe", "as cores: quem", "manda é a LEGENDA"], GREEN)])


# ======================================================================
# questão e dica
# ======================================================================

ALTS = [("A", "anamorfose: a área expressa um dado, não o território", "23.a", None, ""),
        ("B", "projeção equivalente: mantém as áreas reais", "23.b", "24.b", "na equivalente, Canadá e Rússia seriam ENORMES"),
        ("C", "projeção conforme: preserva as formas", "23.c", "24.c", "não explica a Índia (perto do Equador) crescer"),
        ("D", "escala grande: mais detalhe nos populosos", "23.d", "24.d", "o mapa-múndi inteiro tem escala PEQUENA"),
        ("E", "projeção azimutal equidistante", "23.e", "25.e", "distância a partir de um ponto ≠ população")]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "O MAPA DA POPULAÇÃO", BLUE)
    card(c, *CARD_R)
    text(c, "Área de cada país proporcional ao número de habitantes.", 200, 230, 32, "black", INK, ep(t, C["22.e1"], 0.5), align="left")
    text(c, "Índia e China enormes; Canadá, Rússia e Austrália estreitos; mesma posição.", 200, 280, 28, "black", INK2,
         ep(t, C["22.e2"], 0.5), align="left")
    aok = ep(t, C["25.a"], 0.5)
    for k, (L, s, cue_in, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[cue_in])
        y = 380 + k * 90 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 190, y - 36, 1540, 76, 14, GREEN, 0.15 * aok)
        badge_num(c, L, 230, y - 10, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 275, y, 30, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 270, y - 10, 280 + text_w(s, "black", 30), y - 10, ax, RED, ax)
            text(c, why, 275, y + 30, 21, "black", RED, ax, align="left")
    ap = ep(t, C["23.p"], 0.5) * (1 - prog(t, C["24.t"] - 0.3, 0.4))
    if ap > 0:
        rrect(c, 1390, 300, 340, 96, 24, AMBER, ap, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(1418, 322, 14, 52), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(1444, 322, 14, 52), paint(INK, ap))
        text_mid(c, "PAUSE E TENTE", 1600, 348, 30, "black", INK, ap)
    pill(c, "RESPOSTA: A · o tamanho é o dado", 1500, 230, GREEN, size=24, a=ep(t, C["25.x"], 0.5), anchor="center", bounds=(0, 1920))


def b_dica(c, t, C, B):
    head(c, t, B["start"], "DICA DE PROVA", "PALAVRA-CHAVE: PROPORCIONAL", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["25b.a"], 0.5)
    text(c, "\"tamanho PROPORCIONAL a ...\"", W / 2, 300, 56, "black", INK, aa)
    text(c, "população · PIB · emissões", W / 2, 370, 34, "black", INK2, aa)
    ab = ep(t, C["25b.b"], 0.5)
    for k in range(3):
        x = 700 + k * 260
        r = 50 + 20 * math.sin(t * 2 + k)
        if ab > 0:
            c.drawOval(skia.Rect.MakeLTRB(x - r, 520 - r, x + r, 520 + r * 0.8), paint(("#F59E0B", "#93C5FD", "#86C18A")[k], ab))
            line(c, x, 520 + r * 0.8, x, 640, INK2, ab, 3)
    pill(c, "= ANAMORFOSE", W / 2, 700, AMBER, size=36, a=ep(t, C["25b.c"], 0.5), anchor="center")
    pill(c, "\"áreas REAIS\" = projeção equivalente", W / 2, 790, BLUE, size=28, a=ep(t, C["25b.d"], 0.5), anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO E PEGADINHAS", PURPLE)
    card(c, *CARD_R)
    itens = [("1", "Escala"), ("2", "Coordenadas"), ("3", "Projeções"), ("4", "Curvas de nível"), ("5", "Mapas temáticos")]
    at = ep(t, C["27.t"], 0.5)
    for k, (n, s) in enumerate(itens):
        x = 260 + k * 300
        a = at * ep(t, C["27.t"] + 0.3 * k, 0.4)
        badge_num(c, n, x + 60, 360, a, 36, bg=BLUE)
        text(c, s, x + 60, 450, 28, "black", INK, a)
        check_icon(c, x + 60, 520, 20, a, GREEN)
    pill(c, "EPISÓDIO 6: tudo junto + pegadinhas + questões", W / 2, 680, PURPLE, size=32, a=ep(t, C["27.a"], 0.5), anchor="center")
    pill(c, "caçar as PEGADINHAS", W / 2, 770, AMBER, size=28, a=ep(t, C["27.b"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Que dado você poria num mapa de balões?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, previsao=b_previsao, tematico=b_tematico, legenda=b_legenda,
              tipos=b_tipos, balao=b_balao, morph=b_morph, pib=b_pib, recap=b_recap, naoproj=b_naoproj, roteiro=b_roteiro,
              aplica=b_aplica, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, questao=b_questao, dica=b_dica, ponte=b_ponte,
              cta=b_cta)
