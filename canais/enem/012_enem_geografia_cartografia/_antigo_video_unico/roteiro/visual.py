"""Visual do vídeo 012 — ENEM Geografia: Cartografia (tema claro)."""
import math
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_geografia_cartografia.mp4"
CARD_R = (140, 150, 1640, 690)
SKY = "#0EA5E9"
LAND = "#86C18A"
LAND2 = "#5FA463"
SEA = "#DBEAFE"
ICE = "#CBD5E1"

# contornos estilizados (coordenadas normalizadas 0–1)
AFRICA = [(0.30, 0.00), (0.55, 0.02), (0.70, 0.10), (0.95, 0.22), (1.00, 0.32), (0.85, 0.45), (0.80, 0.60), (0.68, 0.80),
          (0.55, 1.00), (0.45, 0.95), (0.38, 0.72), (0.32, 0.55), (0.10, 0.45), (0.00, 0.30), (0.05, 0.12)]
GREENLAND = [(0.35, 0.0), (0.75, 0.02), (1.0, 0.15), (0.85, 0.40), (0.70, 0.65), (0.50, 1.0), (0.35, 0.80), (0.20, 0.55),
             (0.0, 0.35), (0.10, 0.12)]
BRASIL = [(0.35, 0.0), (0.55, 0.05), (0.75, 0.12), (1.0, 0.28), (0.95, 0.40), (0.85, 0.55), (0.75, 0.72), (0.62, 0.85),
          (0.50, 1.0), (0.42, 0.88), (0.45, 0.72), (0.30, 0.62), (0.20, 0.50), (0.0, 0.42), (0.05, 0.25), (0.20, 0.15)]
EUROPA = [(0.1, 0.3), (0.3, 0.05), (0.55, 0.0), (0.8, 0.1), (1.0, 0.35), (0.85, 0.7), (0.6, 0.95), (0.35, 1.0), (0.15, 0.75), (0.0, 0.55)]


# ======================================================================
# utilidades
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
        mx, my = (P[i - 1][0] + P[i][0]) / 2, (P[i - 1][1] + P[i][1]) / 2
        p.quadTo(P[i - 1][0], P[i - 1][1], mx, my)
    p.quadTo(P[-1][0], P[-1][1], (P[-1][0] + P[0][0]) / 2, (P[-1][1] + P[0][1]) / 2)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint(stroke or LAND2, a, stroke=3))


def oval(c, cx, cy, rx, ry, col, a, w=3, dash=None, fill=None):
    if a <= 0:
        return
    r = skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry)
    if fill:
        c.drawOval(r, paint(fill, a))
    p = paint(col, a, stroke=w)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawOval(r, p)


def arc(c, cx, cy, r, start, sweep, col, a, w=4):
    if a > 0:
        c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), start, sweep, False, paint(col, a, stroke=w))


def globe(c, cx, cy, r, a, lats=(-60, -30, 0, 30, 60), lons=(-60, -30, 30, 60)):
    """globo em vista frontal: paralelos são retas, meridianos são elipses"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(SEA, a))
    for L in lats:
        yy = cy - r * math.sin(math.radians(L))
        hw = r * math.cos(math.radians(L))
        line(c, cx - hw, yy, cx + hw, yy, "#93C5FD", a, 2)
    for L in lons:
        oval(c, cx, cy, r * abs(math.sin(math.radians(L))), r, "#93C5FD", a, 2)
    line(c, cx, cy - r, cx, cy + r, "#93C5FD", a, 2)
    c.drawCircle(cx, cy, r, paint(INK2, a, stroke=4))


def lat_line(c, cx, cy, r, L, col, a, w=6):
    yy = cy - r * math.sin(math.radians(L))
    hw = r * math.cos(math.radians(L))
    line(c, cx - hw, yy, cx + hw, yy, col, a, w)
    return yy, hw


def tiles(c, t, items, y, h=230, cw=480, gap=60):
    x0 = W / 2 - (len(items) * cw + (len(items) - 1) * gap) / 2
    for k, (tc, fn) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, y + dy, cw, h, a)
        fn(c, x, y + dy, cw, h, a)


def scale_bar(c, x, y, w, a, labels=("0", "5", "10 km")):
    if a <= 0:
        return
    for k in range(2):
        rrect(c, x + k * w / 2, y, w / 2, 14, 0, INK if k == 0 else "#FFFFFF", a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, 14), paint(INK, a, stroke=2))
    for k, s in enumerate(labels):
        text(c, s, x + k * w / 2, y + 44, 24, "bold", INK2, a)


def mini_map(c, x, y, w, h, a):
    """mapinha genérico: ilha, rio e cidade"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, SEA, a)
    blob(c, BRASIL, x + w * 0.12, y + h * 0.08, w * 0.7, h * 0.8, LAND, a)
    p = skia.Path(); p.moveTo(x + w * 0.3, y + h * 0.3)
    p.cubicTo(x + w * 0.45, y + h * 0.45, x + w * 0.4, y + h * 0.6, x + w * 0.6, y + h * 0.75)
    c.drawPath(p, paint(SKY, a, stroke=max(2, w / 120)))
    c.drawCircle(x + w * 0.55, y + h * 0.4, max(4, w / 60), paint(RED, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(INK2, a, stroke=3))


def contour_map(c, a, hi_tight=0.0, hi_wide=0.0):
    """morro com curvas de nível: lado oeste com curvas juntas, lado leste espaçadas"""
    cy = 500
    for k, lv in enumerate((100, 200, 300, 400)):
        cx, rx, ry = 560 - 45 * k, 300 - 70 * k, 200 - 50 * k
        oval(c, cx, cy, rx, ry, "#A16207", a, 4, fill="#FEF3C7" if k == 0 else None)
        text_mid(c, str(lv), cx + rx - 4, cy - 26, 24, "black", "#A16207", a, align="right")
    text_mid(c, "▲", 425, 500, 30, "black", INK, a)
    if hi_tight > 0:
        rrect(c, 240, 430, 110, 140, 16, RED, 0.15 * hi_tight)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(240, 430, 110, 140), 16, 16), paint(RED, hi_tight, stroke=4))
    if hi_wide > 0:
        rrect(c, 500, 430, 380, 140, 16, GREEN, 0.12 * hi_wide)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(500, 430, 380, 140), 16, 16), paint(GREEN, hi_wide, stroke=4))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    for k, (tt, gw, gh, aw, ah, al) in enumerate((("NO MAPA DA ESCOLA (Mercator)", 300, 300, 300, 320, aa),
                                                  ("NO TAMANHO REAL", 92, 92, 340, 360, ab))):
        if al <= 0:
            continue
        x = 200 + k * 820
        card(c, x, 180, 700, 560, al)
        text(c, tt, x + 350, 240, 32, "black", RED if k == 0 else GREEN, al)
        blob(c, GREENLAND, x + 60, 300 if k == 0 else 330, gw, gh, ICE, al, "#64748B")
        blob(c, AFRICA, x + 360 - (40 if k else 0), 300, aw, ah, LAND, al)
        text(c, "Groenlândia", x + 60 + gw / 2, 650 if k == 0 else 470, 28, "black", INK2, al)
        text(c, "África", x + 360 - (40 if k else 0) + aw / 2, 690, 28, "black", INK2, al)
    pill(c, "a África é 14 vezes MAIOR", 1370, 780, GREEN, size=30, a=ab, anchor="center")
    pill(c, "o mapa errou? NÃO: fez uma ESCOLHA", 550, 780, AMBER, size=30, a=ep(t, C["01.c"], 0.5), anchor="center")
    pill(c, "o ENEM quer saber se você percebe quando o mapa MENTE", W / 2, 120, RED, size=28, a=ep(t, C["01.d"], 0.5),
         anchor="center")


def b_enem(c, t, C, B):
    head(c, t, B["start"], "CARTOGRAFIA NO ENEM", "DOIS JEITOS DE APARECER", BLUE)
    data = [("02.a", "COMO CONTA", ["escala", "distância", "declividade"], BLUE),
            ("02.b", "LEITURA CRÍTICA", ["projeções", "quem pôs o norte em cima?", "o mapa mente?"], PURPLE)]
    items = []
    for cue, tt, lst, col in data:
        def fn(c, x, y, w, h, a, tt=tt, lst=lst, col=col):
            text(c, tt, x + w / 2, y + 90, 50, "black", col, a)
            for j, s in enumerate(lst):
                text(c, s, x + w / 2, y + 190 + j * 70, 38, "bold", INK, a)
        items.append((C[cue], fn))
    tiles(c, t, items, 200, h=470, cw=700, gap=80)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "GEOGRAFIA ENEM", "CARTOGRAFIA")
    cards_row(c, t, [("1", "Escala", C["03.a"], BLUE), ("2", "Coordenadas", C["03.b"], GREEN),
                     ("3", "Projeções", C["03.c"], PURPLE), ("4", "Curvas\nde nível", C["03.d"], AMBER)],
              cw=370, chh=400, title_size=40)


# ======================================================================
# escala
# ======================================================================

def b_escala(c, t, C, B):
    head(c, t, B["start"], "ESCALA", "MAPA x TERRENO", BLUE)
    card(c, *CARD_R)
    at = ep(t, C["04.t"], 0.5)
    text(c, "1 : 100 000", W / 2, 300, 96, "black", BLUE, at)
    text(c, "mapa : terreno", W / 2, 350, 30, "bold", GRAY, at)
    aa = ep(t, C["04.a"], 0.5)
    text(c, "1 cm no mapa  =  100 000 cm  =  1 km", W / 2, 470, 50, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        x = 640
        text(c, "1", x, 620, 80, "black", INK, ab, align="left")
        x += text_w("1", "black", 80)
        for k in range(5):
            text(c, "0", x, 620, 80, "black", RED, ab, align="left")
            w = text_w("0", "black", 80)
            strike(c, x - 4, 610, x + w + 4, 560, ab, RED, ep(t, C["04.b"] + 0.4 + 0.2 * k, 0.3))
            x += w
        text(c, " cm", x, 620, 60, "black", INK, ab, align="left")
        arrow(c, 1130, 595, 1230, 595, GREEN, ab, 6, 22)
        text(c, "1 km", 1260, 620, 80, "black", GREEN, ab, align="left")
    pill(c, "corte CINCO zeros: cm → km", W / 2, 730, AMBER, size=30, a=ep(t, C["04.b"] + 1.6, 0.5), anchor="center")


def b_q_escala(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "DISTÂNCIA REAL", BLUE)
    stmt_card(c, t, [(C["05.e1"], "Escala 1 : 250 000"), (C["05.e2"], "No mapa: 8 cm"), (C["05.e2"] + 1.2, "Distância real?")], size=42)
    a = ep(t, C["05.s1"], 0.5)
    if a <= 0:
        return
    sol_card(c, a=a)
    text(c, "1 cm = 250 000 cm", 1330, 330, 52, "black", INK, a)
    text(c, "= 2,5 km", 1330, 420, 52, "black", BLUE, ep(t, C["05.s1"] + 1.2, 0.5))
    result_box(c, "8 × 2,5 = 20 km", 1330, 590, 60, ep(t, C["05.s2"], 0.5), GREEN)


def b_ampliado(c, t, C, B):
    head(c, t, B["start"], "MAPA AMPLIADO", "SÓ A ESCALA GRÁFICA SOBREVIVE", AMBER)
    card(c, *CARD_R)
    at = ep(t, C["06.t"], 0.5)
    mini_map(c, 250, 300, 340, 240, at)
    scale_bar(c, 270, 570, 160, at)
    text(c, "1 : 1 000 000", 420, 660, 36, "black", INK, at)
    text(c, "original", 420, 260, 30, "black", GRAY, at)
    f = ep(t, C["06.t"] + 1.0, 1.2)
    if f > 0:
        s = lerp(1, 2, f)
        mini_map(c, 760, 230, 340 * s * 0.85, 240 * s * 0.85, at)
        scale_bar(c, 780, 230 + 240 * s * 0.85 + 20, 160 * s * 0.85, at)
    text(c, "cópia 200%", 1250, 210, 30, "black", GRAY, f)
    ag = ep(t, C["06.g"], 0.5)
    check_icon(c, 1370, 650, 22, ag, GREEN)
    text(c, "barra cresceu junto:", 1402, 645, 26, "black", GREEN, ag, align="left")
    text(c, "continua CERTA", 1402, 680, 26, "black", GREEN, ag, align="left")
    an = ep(t, C["06.n"], 0.5)
    text(c, "1 : 1 000 000", 1560, 745, 32, "black", GRAY, an)
    strike(c, 1455, 735, 1665, 735, an, RED, ep(t, C["06.n"] + 0.3, 0.4))
    pill(c, "agora é 1 : 500 000", 1560, 800, RED, size=26, a=ep(t, C["06.n"] + 0.9, 0.4), anchor="center")
    pill(c, "por isso mapas DIGITAIS usam escala gráfica", 420, 780, BLUE, size=26, a=ep(t, C["06.d"], 0.5), anchor="center")


def b_grande(c, t, C, B):
    head(c, t, B["start"], "ESCALA GRANDE x PEQUENA", "A REGRA QUE PARECE INVERTIDA", AMBER)
    seq(c, [("FRAC", "1", "5 000", INK), (">", RED), ("FRAC", "1", "5 000 000", INK)], W / 2, 270, 60, ep(t, C["07.a"], 0.5))

    def grande(c, x, y, w, h, a):
        text(c, "1 : 5 000", x + w / 2, y + 60, 44, "black", INK, a)
        pill(c, "ESCALA GRANDE", x + w / 2, y + 110, GREEN, size=30, a=a, anchor="center", bounds=(0, 1920))
        for i in range(5):
            for j in range(3):
                rrect(c, x + 90 + i * 108, y + 160 + j * 72, 92, 56, 6, "#E5E7EB", a)
                for q in range(3):
                    c.drawRect(skia.Rect.MakeXYWH(x + 98 + i * 108 + q * 28, y + 168 + j * 72, 20, 18), paint("#F59E0B", a * 0.7))
        text(c, "área pequena · MUITO detalhe", x + w / 2, y + 420, 30, "black", INK2, a)

    def pequena(c, x, y, w, h, a):
        text(c, "1 : 5 000 000", x + w / 2, y + 60, 44, "black", INK, a)
        pill(c, "ESCALA PEQUENA", x + w / 2, y + 110, RED, size=30, a=a, anchor="center", bounds=(0, 1920))
        rrect(c, x + 120, y + 150, w - 240, 230, 14, SEA, a)
        blob(c, BRASIL, x + 240, y + 160, 220, 210, LAND, a)
        text(c, "área grande · POUCO detalhe", x + w / 2, y + 420, 30, "black", INK2, a)

    tiles(c, t, [(C["07.b"], grande), (C["07.c"], pequena)], 320, h=450, cw=720, gap=60)
    pill(c, "mapa-múndi de 2 metros = escala PEQUENA", W / 2, 815, RED, size=28, a=ep(t, C["07.d"], 0.5), anchor="center")


def b_q_bairro(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "BOCAS DE LOBO, RUA A RUA", BLUE)
    stmt_card(c, t, [(C["08.e1"], "Planejar rua a rua\num bairro"), (C["08.e2"], "Mapa A: 1 : 2 000"),
                     (C["08.e2"] + 1.2, "Mapa B: 1 : 2 000 000")], size=42)
    a = ep(t, C["08.s1"], 0.5)
    if a <= 0:
        return
    sol_card(c, a=a)
    text(c, "1 : 2 000 → 1 cm = 20 m", 1330, 320, 48, "black", INK, a)
    text(c, "cada rua aparece", 1330, 400, 36, "bold", INK2, a)
    result_box(c, "1 : 2 000 · escala GRANDE", 1330, 540, 50, ep(t, C["08.s2"], 0.5), GREEN)
    pill(c, "denominador maior NÃO é escala maior", 1330, 690, RED, size=28, a=ep(t, C["08.x"], 0.5), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# coordenadas
# ======================================================================

def b_coord(c, t, C, B):
    head(c, t, B["start"], "COORDENADAS", "LATITUDE E LONGITUDE", GREEN)
    card(c, *CARD_R)
    cx, cy, r = 520, 495, 290
    at = ep(t, C["09.t"], 0.5)
    globe(c, cx, cy, r, at)
    ap = ep(t, C["09.p"], 0.5)
    lat_line(c, cx, cy, r, 0, BLUE, ap)
    if ap > 0:
        ang = math.radians(40)
        P = (cx + r * math.cos(ang), cy - r * math.sin(ang))
        line(c, cx, cy, cx + r, cy, BLUE, ap, 3)
        line(c, cx, cy, *P, BLUE, ap, 3)
        arc(c, cx, cy, 90, -40, 40, BLUE, ap, 4)
        text(c, "40°", cx + 105, cy - 22, 28, "black", BLUE, ap, align="left")
        c.drawCircle(*P, 12, paint(RED, ap))
        pill(c, "Equador 0°", cx - r + 10, cy + 34, BLUE, size=22, a=ap, bounds=(0, 1920))
    am = ep(t, C["09.m"], 0.5)
    line(c, cx, cy - r, cx, cy + r, GREEN, am, 6)
    pill(c, "Greenwich 0°", cx, cy - r - 30, GREEN, size=22, a=am, anchor="center", bounds=(0, 1920))
    for k, (cue, tt, l1, l2, col) in enumerate((("09.p", "LATITUDE", "a partir do EQUADOR", "0° a 90° · Norte ou Sul", BLUE),
                                                ("09.m", "LONGITUDE", "a partir de GREENWICH", "0° a 180° · Leste ou Oeste", GREEN))):
        a, dy = rise(t, C[cue])
        y = 290 + k * 210 + dy
        text(c, tt, 900, y, 52, "black", col, a, align="left")
        text(c, l1, 900, y + 56, 34, "black", INK, a, align="left")
        text(c, l2, 900, y + 102, 32, "bold", INK2, a, align="left")
    pill(c, "são ÂNGULOS, não quilômetros", 1200, 765, AMBER, size=30, a=ep(t, C["09.x"], 0.5), anchor="center")


def b_linhas(c, t, C, B):
    head(c, t, B["start"], "AS LINHAS DA PROVA", "E O BRASIL NA REDE", GREEN)
    card(c, *CARD_R)
    cx, cy, r = 520, 495, 290
    globe(c, cx, cy, r, 1, lats=(), lons=(-60, -30, 30, 60))
    data = [("10.e", (0,), "Equador 0°", BLUE), ("10.tr", (23.45, -23.45), "Trópicos ≈ 23°", AMBER),
            ("10.cp", (66.55, -66.55), "Círculos polares ≈ 66°", PURPLE)]
    for cue, lats, lab, col in data:
        a = ep(t, C[cue], 0.5)
        for L in lats:
            yy, hw = lat_line(c, cx, cy, r, L, col, a, 5)
        yy, hw = lat_line(c, cx, cy, r, lats[0], col, 0)
        pill(c, lab, cx + hw + 16, yy, col, size=22, a=a, bounds=(0, 1920))
    ab = ep(t, C["10.b"], 0.5)
    bx, by, bw, bh = 1130, 230, 340, 450
    blob(c, BRASIL, bx, by, bw, bh, LAND, ab)
    for fr, lab, col in ((0.13, "Equador", BLUE), (0.73, "Trópico de Capricórnio", AMBER)):
        hline(c, bx - 60, 1680, by + bh * fr, col, ab, 5, (16, 10))
        text(c, lab, 1680, by + bh * fr + 32, 22, "black", col, ab, align="right")
    pill(c, "Brasil: todas as longitudes são OESTE", 1390, 760, GREEN, size=28, a=ep(t, C["10.o"], 0.5), anchor="center")


def b_meridiano(c, t, C, B):
    head(c, t, B["start"], "DISTÂNCIA NO MERIDIANO", "1° DE LATITUDE ≈ 111 km", GREEN)
    card(c, *CARD_R)
    cx, cy, r = 470, 495, 290
    globe(c, cx, cy, r, 1)
    lat_line(c, cx, cy, r, 0, BLUE, 1, 4)
    ac = ep(t, C["11.c"], 0.5)
    pA = (cx, cy + r * math.sin(math.radians(2)))
    pB = (cx, cy + r * math.sin(math.radians(22)))
    line(c, cx, cy - r, cx, cy + r, GREEN, ac, 5)
    if ac > 0:
        line(c, *pA, *pB, RED, ac, 10)
        for p, lab in ((pA, "A · 2° S"), (pB, "B · 22° S")):
            c.drawCircle(*p, 13, paint(RED, ac))
            text_mid(c, lab, p[0] + 26, p[1], 26, "black", RED, ac, align="left")
    aa = ep(t, C["11.a"], 0.5)
    text(c, "volta da Terra ≈ 40 000 km", 1240, 290, 42, "black", INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    text(c, "40 000 ÷ 360 ≈ 111 km por grau", 1240, 380, 42, "black", BLUE, ab)
    result_box(c, "20° × 111 ≈ 2 220 km", 1240, 520, 50, ep(t, C["11.c"] + 1.5, 0.5), GREEN)
    pill(c, "hemisférios diferentes: SOME (5° N e 15° S = 20°)", 1240, 680, AMBER, size=26, a=ep(t, C["11.d"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_direcao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "PARA QUE LADO ELE FOI?", BLUE)
    card(c, *CARD_R)
    gx, gy, gw, gh = 260, 230, 720, 520
    ae = ep(t, C["12.e"], 0.5)
    X = lambda lon: gx + (60 - lon) / 30 * gw
    Y = lambda lat: gy + lat / 30 * gh
    for lon in (60, 50, 40, 30):
        line(c, X(lon), gy, X(lon), gy + gh, LINE, ae, 2)
        text(c, f"{lon}° O", X(lon), gy + gh + 40, 24, "bold", GRAY, ae)
    for lat in (0, 10, 20, 30):
        line(c, gx, Y(lat), gx + gw, Y(lat), LINE, ae, 2)
        text(c, f"{lat}° S" if lat else "0°", gx - 14, Y(lat) + 8, 24, "bold", GRAY, ae, align="right")
    A, Bp = (X(50), Y(10)), (X(40), Y(20))
    if ae > 0:
        c.drawCircle(*A, 14, paint(BLUE, ae)); text_mid(c, "A", A[0] - 30, A[1], 30, "black", BLUE, ae)
        c.drawCircle(*Bp, 14, paint(RED, ae)); text_mid(c, "B", Bp[0] + 30, Bp[1], 30, "black", RED, ae)
    a1 = ep(t, C["12.s1"], 0.5)
    arrow(c, A[0], A[1], A[0], Bp[1], PURPLE, a1, 5, 18, progress=a1)
    pill(c, "mais ao SUL", A[0] - 20, (A[1] + Bp[1]) / 2, PURPLE, size=22, a=a1, anchor="right", bounds=(0, 1920))
    a2 = ep(t, C["12.s2"], 0.5)
    arrow(c, A[0], Bp[1], Bp[0], Bp[1], GREEN, a2, 5, 18, progress=a2)
    pill(c, "mais a LESTE", (A[0] + Bp[0]) / 2, Bp[1] + 40, GREEN, size=22, a=a2, anchor="center", bounds=(0, 1920))
    ar = ep(t, C["12.r"], 0.5)
    arrow(c, *A, *Bp, RED, ar, 6, 22, progress=ar)
    rx, ry = 1350, 420
    for ang, lab in ((90, "N"), (270, "S"), (0, "L"), (180, "O")):
        x2, y2 = rx + 120 * math.cos(math.radians(ang)), ry - 120 * math.sin(math.radians(ang))
        line(c, rx, ry, x2, y2, INK2, ae, 4)
        text_mid(c, lab, rx + 150 * math.cos(math.radians(ang)), ry - 150 * math.sin(math.radians(ang)), 32, "black", INK, ae)
    arrow(c, rx, ry, rx + 95, ry + 95, RED, ar, 7, 24)
    result_box(c, "SUDESTE", rx, 640, 56, ar, RED)
    pill(c, "40° O fica a LESTE de 50° O", rx, 760, AMBER, size=28, a=ep(t, C["12.x"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# projeções
# ======================================================================

def b_projecoes(c, t, C, B):
    head(c, t, B["start"], "PROJEÇÕES", "TODA PROJEÇÃO DISTORCE", PURPLE)
    pill(c, "achatar uma casca de laranja: ela RASGA", W / 2, 205, AMBER, size=28, a=ep(t, C["13.a"], 0.5), anchor="center")

    def cil(c, x, y, w, h, a):
        cx, cy, r = x + w / 2, y + 250, 105
        globe(c, cx, cy, r, a, lats=(), lons=(-45, 45))
        line(c, cx - r, cy - 140, cx - r, cy + 140, PURPLE, a, 4); line(c, cx + r, cy - 140, cx + r, cy + 140, PURPLE, a, 4)
        oval(c, cx, cy - 140, r, 22, PURPLE, a, 3); oval(c, cx, cy + 140, r, 22, PURPLE, a, 3, dash=(10, 8))
        lat_line(c, cx, cy, r, 0, GREEN, a, 6)
        text(c, "CILÍNDRICA", cx, y + 60, 38, "black", PURPLE, a)
        pill(c, "toca: o EQUADOR", cx, y + 440, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, "mapa-múndi", cx, y + 500, 28, "bold", INK2, a)

    def con(c, x, y, w, h, a):
        cx, cy, r = x + w / 2, y + 280, 105
        globe(c, cx, cy, r, a, lats=(), lons=(-45, 45))
        L = math.radians(45)
        tx, ty = r * math.cos(L), cy - r * math.sin(L)
        apex = (cx, ty - tx * math.tan(L))
        for sgn in (-1, 1):
            line(c, apex[0], apex[1], cx + sgn * tx * 1.6, ty + (tx * 0.6) * math.tan(L), PURPLE, a, 4)
        lat_line(c, cx, cy, r, 45, GREEN, a, 6)
        text(c, "CÔNICA", cx, y + 60, 38, "black", PURPLE, a)
        pill(c, "toca: um PARALELO", cx, y + 440, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, "latitudes médias", cx, y + 500, 28, "bold", INK2, a)

    def azi(c, x, y, w, h, a):
        cx, cy, r = x + w / 2, y + 280, 105
        globe(c, cx, cy, r, a, lats=(), lons=(-45, 45))
        line(c, cx - 170, cy - r, cx + 170, cy - r, PURPLE, a, 6)
        c.drawCircle(cx, cy - r, 12, paint(GREEN, a))
        text(c, "AZIMUTAL", cx, y + 60, 38, "black", PURPLE, a)
        pill(c, "toca: um PONTO", cx, y + 440, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, "polos · bandeira da ONU", cx, y + 500, 28, "bold", INK2, a)

    tiles(c, t, [(C["13.c"], cil), (C["13.k"], con), (C["13.z"], azi)], 245, h=530)
    pill(c, "distorção mínima onde a superfície TOCA", W / 2, 815, RED, size=28, a=ep(t, C["13.x"], 0.5), anchor="center")


def b_propriedade(c, t, C, B):
    head(c, t, B["start"], "O QUE A PROJEÇÃO PRESERVA", "FORMA OU ÁREA", PURPLE)

    def conf(c, x, y, w, h, a):
        text(c, "CONFORME", x + w / 2, y + 70, 48, "black", BLUE, a)
        text(c, "preserva ÂNGULOS e FORMAS", x + w / 2, y + 130, 32, "black", INK, a)
        text(c, "sacrifica as ÁREAS", x + w / 2, y + 175, 30, "bold", RED, a)
        yy = y + 440
        for k, s in enumerate((44, 52, 66, 92)):
            rrect(c, x + 120 + k * 130, yy - s, s, s, 6, BLUE, a * 0.8)
        text(c, "Equador  →  polo", x + w / 2, y + 490, 26, "bold", GRAY, a)

    def equi(c, x, y, w, h, a):
        text(c, "EQUIVALENTE", x + w / 2, y + 70, 48, "black", GREEN, a)
        text(c, "preserva as ÁREAS", x + w / 2, y + 130, 32, "black", INK, a)
        text(c, "deforma as FORMAS", x + w / 2, y + 175, 30, "bold", RED, a)
        yy = y + 440
        for k, (ww, hh) in enumerate(((60, 60), (75, 48), (100, 36), (140, 26))):
            rrect(c, x + 100 + sum((60, 75, 100, 140)[:k]) + 22 * k, yy - hh, ww, hh, 6, GREEN, a * 0.8)
        text(c, "mesma área, formas esticadas", x + w / 2, y + 490, 26, "bold", GRAY, a)

    tiles(c, t, [(C["14.a"], conf), (C["14.b"], equi)], 190, h=530, cw=720, gap=60)
    pill(c, "as duas ao mesmo tempo: IMPOSSÍVEL", W / 2, 790, RED, size=32, a=ep(t, C["14.x"], 0.5), anchor="center")


def b_mercator(c, t, C, B):
    head(c, t, B["start"], "MERCATOR (1569)", "CILÍNDRICA E CONFORME", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    gx, gy, gw, gh = 220, 240, 480, 420
    for k in range(7):
        line(c, gx + k * gw / 6, gy, gx + k * gw / 6, gy + gh, LINE, aa, 2)
    for k, fr in enumerate((0, 0.18, 0.33, 0.5, 0.7, 1.0)):
        line(c, gx, gy + gh * fr, gx + gw, gy + gh * fr, LINE, aa, 2)
    arrow(c, gx + 30, gy + gh - 30, gx + gw - 40, gy + 40, BLUE, aa, 6, 22, progress=ep(t, C["15.a"], 1.2))
    text(c, "rumo constante = linha RETA", gx + gw / 2, gy + gh + 50, 30, "black", BLUE, aa)
    ab = ep(t, C["15.b"], 0.5)
    data = [(0, 1, None), (30, 1.3, None), (45, 2, None), (60, 4, "15.c"), (70, 8.5, "15.d")]
    x = 820
    for lat, f, cue in data:
        s = 36 * math.sqrt(f)
        a = ab if cue is None else ep(t, C[cue], 0.5)
        hi = cue is not None and a > 0
        rrect(c, x, 620 - s, s, s, 6, RED if hi else BLUE, a * 0.85)
        text(c, f"{lat}°", x + s / 2, 670, 28, "black", INK2, a)
        text(c, f"× {f}".replace(".", ","), x + s / 2, 620 - s - 16, 28, "black", RED if hi else INK, a)
        x += s + 50
    text(c, "mesma área real, desenhada mais perto do polo", 1220, 730, 28, "bold", GRAY, ab)
    pill(c, "por isso a Groenlândia parece a África", W / 2, 800, RED, size=30, a=ep(t, C["15.e"], 0.5), anchor="center")


def b_peters(c, t, C, B):
    head(c, t, B["start"], "PETERS (anos 70)", "EQUIVALENTE E CRÍTICA", GREEN)
    at = ep(t, C["16.t"], 0.5)
    ad = ep(t, C["16.d"], 1.2)
    for k, (tt, eu, af, col) in enumerate((("MERCATOR", (150, 120), (200, 220), BLUE), ("PETERS", (120, 70), (160, 320), GREEN))):
        a = at if k == 0 else ep(t, C["16.a"], 0.5)
        if a <= 0:
            continue
        x, y = 200 + k * 820, 180
        card(c, x, y, 700, 560, a)
        text(c, tt, x + 350, y + 60, 40, "black", col, a)
        c.save()
        if k == 0 and ad > 0:
            c.translate(x + 350, y + 330); c.rotate(180 * ease_io(ad)); c.translate(-(x + 350), -(y + 330))
        rrect(c, x + 60, y + 100, 580, 440, 14, SEA, a)
        blob(c, EUROPA, x + 330 - eu[0] / 2, y + 120, eu[0], eu[1], LAND, a)
        blob(c, AFRICA, x + 350 - af[0] / 2, y + 130 + eu[1] + 20, af[0], af[1], LAND, a)
        c.restore()
    pill(c, "crítica a uma visão EUROCÊNTRICA", W / 2, 800, PURPLE, size=28, a=fw(t, C["16.b"], C["16.c"] - 0.2), anchor="center")
    pill(c, "centro e polo de cima são CONVENÇÕES", W / 2, 800, AMBER, size=28, a=fw(t, C["16.c"], C["16.d"] - 0.2), anchor="center")
    pill(c, "sul em cima: tão correto quanto o tradicional", W / 2, 800, GREEN, size=28, a=ep(t, C["16.d"] + 0.4, 0.5), anchor="center")


# ======================================================================
# curvas de nível
# ======================================================================

def b_curvas(c, t, C, B):
    head(c, t, B["start"], "CURVAS DE NÍVEL", "LEIA O RELEVO", AMBER)
    card(c, *CARD_R)
    contour_map(c, ep(t, C["17.a"], 0.5), ep(t, C["17.b"], 0.5), ep(t, C["17.c"], 0.5))
    rows = [("17.a", "mesma ALTITUDE em toda a linha", INK), ("17.b", "próximas → declive FORTE", RED),
            ("17.c", "espaçadas → declive SUAVE", GREEN), ("17.d", "fechadas, crescendo p/ dentro → MORRO", AMBER),
            ("17.x", "nunca se CRUZAM", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        text(c, s, 960, 270 + k * 105 + dy, 36, "black", col, a, align="left")


def b_trilhas(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "QUAL TRILHA É MAIS ÍNGREME?", BLUE)
    card(c, *CARD_R)
    ae = ep(t, C["18.e"], 0.5)
    contour_map(c, ae)
    p1 = skia.Path(); p1.moveTo(260, 500); p1.lineTo(410, 500)
    pp = paint(RED, ae, stroke=8, cap_round=True); c.drawPath(p1, pp)
    p2 = skia.Path(); p2.moveTo(860, 500); p2.cubicTo(760, 600, 600, 560, 440, 505)
    pd = paint(BLUE, ae, stroke=7, cap_round=True); pd.setPathEffect(skia.DashPathEffect.Make([18, 12], 0)); c.drawPath(p2, pd)
    text(c, "trilha 1", 250, 600, 30, "black", RED, ae)
    text(c, "trilha 2", 860, 610, 30, "black", BLUE, ae)
    pill(c, "mesmo DESNÍVEL: 100 → 400 m", 1330, 300, INK, size=30, a=ep(t, C["18.s1"], 0.5), anchor="center")
    pill(c, "muda a distância HORIZONTAL", 1330, 400, AMBER, size=30, a=ep(t, C["18.s2"], 0.5), anchor="center")
    result_box(c, "trilha 1: a mais íngreme", 1330, 560, 46, ep(t, C["18.r"], 0.5), RED)
    text(c, "curvas juntas = sobe tudo num caminho curto", 1330, 680, 28, "bold", INK2, ep(t, C["18.r"] + 1.0, 0.5))


def b_declividade(c, t, C, B):
    head(c, t, B["start"], "DECLIVIDADE", "DESNÍVEL SOBRE DISTÂNCIA", AMBER)
    card(c, *CARD_R)
    at = ep(t, C["19.t"], 0.5)
    seq(c, [("declividade =", INK), ("FRAC", "desnível", "distância horizontal", INK), ("× 100%", INK)], W / 2, 280, 50, at)
    rows = [("19.a", "4 cm × 50 000 = 200 000 cm = 2 000 m", BLUE), ("19.b", "600 m − 200 m = 400 m de desnível", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        text(c, s, 240, 430 + k * 90 + dy, 40, "black", col, a, align="left")
    result_box(c, "400 ÷ 2 000 = 20%", 560, 650, 54, ep(t, C["19.c"], 0.5), GREEN)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        p = skia.Path(); p.moveTo(1150, 720); p.lineTo(1650, 720); p.lineTo(1650, 400); p.close()
        c.drawPath(p, paint("#D6B98C", ad)); c.drawPath(p, paint("#A16207", ad, stroke=4))
        hx, hy = 1480, 610
        c.save(); c.translate(hx, hy); c.rotate(-32)
        rrect(c, -30, -50, 60, 50, 4, "#FFFFFF", ad); c.drawRect(skia.Rect.MakeXYWH(-30, -50, 60, 50), paint(INK, ad, stroke=3))
        tri = skia.Path(); tri.moveTo(-40, -50); tri.lineTo(0, -85); tri.lineTo(40, -50); tri.close()
        c.drawPath(tri, paint(RED, ad))
        c.restore()
    pill(c, "a partir de 30%: proibido lotear (risco)", 1400, 790, RED, size=26, a=ad, anchor="center", bounds=(0, 1920))


# ======================================================================
# anamorfose e leitura
# ======================================================================

def b_anamorfose(c, t, C, B):
    head(c, t, B["start"], "ANAMORFOSE", "O TAMANHO É UM DADO", PURPLE)
    card(c, *CARD_R)
    at = ep(t, C["20.t"], 0.5)
    aa, ab = ep(t, C["20.a"], 1.5), ep(t, C["20.b"], 1.5)
    k = 52
    paises = [("Canadá", (470, 340), 10, 0.4, ab, RED), ("Rússia", (1250, 300), 17, 1.4, ab, RED),
              ("China", (1270, 540), 9.6, 14, aa, GREEN), ("Índia", (1010, 650), 3.3, 14, aa, GREEN),
              ("Brasil", (620, 620), 8.5, 2.1, ab, BLUE), ("Austrália", (1530, 700), 7.7, 0.26, ab, BLUE)]
    for nome, (cx, cy), real, pop, f, col in paises:
        s = k * math.sqrt(lerp(real, pop, f))
        rrect(c, cx - s / 2, cy - s / 2, s, s, 10, col, at * 0.75)
        if s > 110:
            text_mid(c, nome, cx, cy, 26 if s > 150 else 22, "black", "#FFFFFF", at)
        else:
            text_mid(c, nome, cx, cy - s / 2 - 22, 22, "black", col, at)
    text(c, "área real", 260, 230, 28, "black", GRAY, at * (1 - aa), align="left")
    text(c, "tamanho = POPULAÇÃO", 260, 230, 30, "black", PURPLE, aa, align="left")
    pill(c, "não é projeção: distorce a área DE PROPÓSITO", W / 2, 800, RED, size=28, a=ep(t, C["20.x"], 0.5), anchor="center")


def b_leitura(c, t, C, B):
    head(c, t, B["start"], "COMO LER QUALQUER MAPA", "O ROTEIRO DA PROVA", BLUE)
    cards_row(c, t, [("1", "Título\ne fonte", C["21.a"], BLUE), ("2", "Legenda", C["21.b"], GREEN),
                     ("3", "Escala", C["21.c"], AMBER), ("4", "Orientação\ne projeção", C["21.d"], PURPLE)],
              cw=370, chh=400, title_size=38)
    pill(c, "a resposta costuma estar AQUI", 755, 720, GREEN, size=26, a=ep(t, C["21.b"] + 0.8, 0.4), anchor="center")


# ======================================================================
# fechamento
# ======================================================================

def b_erros(c, t, C, B):
    head(c, t, B["start"], "OS ERROS QUE", "MAIS CUSTAM PONTOS", RED)
    errors_list(c, t, [(C["22.e1"], "1 : 5 000 000 = escala grande", "é escala PEQUENA"),
                       (C["22.e2"], "numérica de mapa ampliado", "só a GRÁFICA vale"),
                       (C["22.e3"], "latitude a partir de Greenwich", "a partir do EQUADOR"),
                       (C["22.e4"], "Mercator mostra áreas reais", "ela INFLA os polos"),
                       (C["22.e5"], "curvas juntas = terreno plano", "juntas = ÍNGREME")])


def b_cta(c, t, C, B):
    cta(c, t, C["23.like"], C["23.sub"], C["23.bell"], C["23.com"], C["23.bye"], "Achava a Groenlândia do tamanho da África?")


BLOCKS = dict(hook=b_hook, enem=b_enem, mapa=b_mapa, escala=b_escala, q_escala=b_q_escala, ampliado=b_ampliado,
              grande=b_grande, q_bairro=b_q_bairro, coord=b_coord, linhas=b_linhas, meridiano=b_meridiano,
              direcao=b_direcao, projecoes=b_projecoes, propriedade=b_propriedade, mercator=b_mercator, peters=b_peters,
              curvas=b_curvas, trilhas=b_trilhas, declividade=b_declividade, anamorfose=b_anamorfose, leitura=b_leitura,
              erros=b_erros, cta=b_cta)
