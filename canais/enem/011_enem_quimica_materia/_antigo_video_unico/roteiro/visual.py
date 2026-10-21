"""Visual do vídeo 011 — ENEM Química: Matéria, substâncias puras e misturas (tema claro)."""
import math
import random
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_substancias_misturas.mp4"
CARD_R = (140, 150, 1640, 690)
SKY = "#0EA5E9"
WATER = "#7DD3FC"
OIL = "#FCD34D"
SAND = "#D6B98C"
BRONZE = "#B7793E"
OXY = "#E5484D"


# ======================================================================
# utilidades
# ======================================================================

def clip_rect(c, x, y, w, h, r=28):
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), True)


def poly_path(pts):
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    return p


def draw_partial(c, path, frac, col, a, w=7):
    """desenha a fração [0,1] do comprimento do caminho"""
    if a <= 0 or frac <= 0:
        return
    meas = skia.PathMeasure(path, False)
    L = meas.getLength()
    seg = skia.Path()
    meas.getSegment(0, L * clamp(frac), seg, True)
    pp = paint(col, a, stroke=w, cap_round=True)
    pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(seg, pp)


def axes(c, x, y, w, h, a, xl="tempo", yl="T"):
    vec_ = lambda x0, y0, x1, y1: arrow(c, x0, y0, x1, y1, INK, a, 4, 16)
    vec_(x, y + h, x + w + 20, y + h)
    vec_(x, y + h, x, y - 20)
    text(c, yl, x - 30, y + 6, 32, "black", INK, a, align="right")
    text(c, xl, x + w, y + h + 46, 28, "bold", GRAY, a, align="right")


def to_px(x, y, w, h, pts):
    return [(x + u * w, y + h - v * h) for u, v in pts]


PURE = [(0, 0.06), (0.2, 0.36), (0.42, 0.36), (0.6, 0.72), (0.84, 0.72), (1.0, 0.96)]
MIX = [(0, 0.06), (0.18, 0.3), (0.42, 0.44), (0.58, 0.66), (0.82, 0.8), (1.0, 0.97)]


def seg_frac(pts, k):
    """fração do comprimento até o vértice k (k pode ser fracionário)"""
    L = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1)]
    tot = sum(L)
    i = int(k)
    acc = sum(L[:i]) + (L[i] * (k - i) if i < len(L) else 0)
    return acc / tot


def beaker(c, x, y, w, h, a, layers=(), dots=None):
    """béquer: layers = [(fração_altura, cor, alfa)] de baixo para cima"""
    if a <= 0:
        return
    clip_rect(c, x, y, w, h, 30)
    yy = y + h
    for fr, col, al in layers:
        hh = h * fr
        c.drawRect(skia.Rect.MakeXYWH(x, yy - hh, w, hh), paint(col, a * al))
        yy -= hh
    if dots:
        dots(c)
    c.restore()
    p = skia.Path()
    p.moveTo(x - 14, y); p.lineTo(x, y + 10); p.lineTo(x, y + h - 30)
    p.quadTo(x, y + h, x + 30, y + h); p.lineTo(x + w - 30, y + h); p.quadTo(x + w, y + h, x + w, y + h - 30)
    p.lineTo(x + w, y + 10); p.lineTo(x + w + 14, y)
    c.drawPath(p, paint(INK2, a, stroke=6))


def atom(c, x, y, r, col, a, lab=""):
    if a <= 0:
        return
    c.drawCircle(x, y, r, paint(col, a))
    c.drawCircle(x - r * 0.3, y - r * 0.3, r * 0.3, paint("#FFFFFF", a * 0.35))
    if lab:
        text_mid(c, lab, x, y, r * 0.9, "black", "#FFFFFF", a)


def node(c, s, cx, cy, col, a, size=30):
    if a <= 0:
        return
    w = text_w(s, "black", size) + 56
    rrect(c, cx - w / 2, cy - 36, w, 72, 18, col, a, shadow=True)
    text_mid(c, s, cx, cy, size, "black", "#FFFFFF", a)


def hexgrid(c, x0, y0, cols, rows, s, col, a, w=3, skew=0.0, sy=1.0):
    """malha hexagonal (grafite/grafeno); skew/sy dão perspectiva"""
    if a <= 0:
        return
    pp = paint(col, a, stroke=w)
    for r in range(rows):
        for q in range(cols):
            cx = x0 + q * s * 1.5
            cy = y0 + (r * s * math.sqrt(3) + (q % 2) * s * math.sqrt(3) / 2) * sy
            pts = []
            for k in range(6):
                ang = math.radians(60 * k)
                px, py = cx + s * math.cos(ang), cy + s * math.sin(ang) * sy
                pts.append((px + skew * (py - y0), py))
            p = poly_path(pts); p.close()
            c.drawPath(p, pp)


def tiles(c, t, items, y, h=230, cw=480, gap=60):
    x0 = W / 2 - (len(items) * cw + (len(items) - 1) * gap) / 2
    for k, (tc, fn) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, y + dy, cw, h, a)
        fn(c, x, y + dy, cw, h, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    card(c, *CARD_R)
    x, y, w, h = 300, 230, 960, 500
    aa = ep(t, C["01.a"], 0.5)
    axes(c, x, y, w, h, aa)
    pts = to_px(x, y, w, h, PURE)
    path = poly_path(pts)
    k = 0.0
    for i, cue in enumerate(("01.b", "01.c", "01.d", "01.e")):
        k += ep(t, C[cue], 1.2 if i % 2 == 0 else 1.6)
    k += ep(t, C["01.e"] + 1.4, 0.8)
    draw_partial(c, path, seg_frac(PURE, k), BLUE, 1, 8)
    for i, cue in ((1, "01.c"), (3, "01.e")):
        a = ep(t, C[cue] + 0.6, 0.4)
        (x0, y0), (x1, _) = pts[i], pts[i + 1]
        pill(c, "T constante", (x0 + x1) / 2, y0 - 40, AMBER, size=22, a=a, anchor="center", bounds=(0, 1920))
    af = ep(t, C["01.f"], 0.5)
    pill(c, "PURO", 1490, 380, GREEN, size=40, a=af, anchor="center", bounds=(0, 1920))
    text(c, "ou", 1490, 470, 34, "black", GRAY, af)
    pill(c, "MISTURA?", 1490, 540, PURPLE, size=40, a=af, anchor="center", bounds=(0, 1920))
    pill(c, "a mais cobrada do assunto", 1490, 680, RED, size=28, a=ep(t, C["01.g"], 0.5), anchor="center", bounds=(0, 1920))


def b_enem(c, t, C, B):
    head(c, t, B["start"], "NO ENEM", "QUATRO FORMAS DE APARECER", BLUE)
    cards_row(c, t, [("1", "Curva de\naquecimento", C["02.a"], RED), ("2", "Fases e\ncomponentes", C["02.b"], BLUE),
                     ("3", "Materiais do\ndia a dia", C["02.c"], AMBER), ("4", "Alotropia\n(carbono)", C["02.d"], PURPLE)],
              cw=370, chh=400, title_size=36)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "MATÉRIA, SUBSTÂNCIAS E MISTURAS")
    cards_row(c, t, [("1", "Pura ou\nmistura?", C["03.a"], GREEN), ("2", "Fases e\ncomponentes", C["03.b"], BLUE),
                     ("3", "Curva de\naquecimento", C["03.c"], RED), ("4", "Alotropia", C["03.d"], PURPLE)],
              cw=370, chh=400, title_size=38)


# ======================================================================
# matéria e propriedades
# ======================================================================

def b_materia(c, t, C, B):
    head(c, t, B["start"], "MATÉRIA", "TEM MASSA E OCUPA ESPAÇO", BLUE)
    text(c, "matéria = tudo o que tem MASSA e ocupa LUGAR no espaço", W / 2, 225, 38, "black", INK, ep(t, C["04.t"], 0.5))
    for k, (cue, tt, items, pl, col) in enumerate((
            ("04.g", "PROPRIEDADES GERAIS", ["massa", "volume", "inércia", "impenetrabilidade"], ("valem para TODA matéria", GRAY), GRAY),
            ("04.e", "PROPRIEDADES ESPECÍFICAS", ["ponto de fusão", "ponto de ebulição", "densidade", "solubilidade"],
             ("a IMPRESSÃO DIGITAL da substância", GREEN), GREEN))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 280 + dy
        card(c, x, y, 700, 500, a)
        text(c, tt, x + 350, y + 70, 34, "black", col, a)
        for j, s in enumerate(items):
            text(c, s, x + 350, y + 150 + j * 62, 36, "bold", INK, a * ep(t, C[cue] + 0.3 + 0.25 * j, 0.3))
        pill(c, pl[0], x + 350, y + 435, pl[1], size=26, a=a * ep(t, C[cue] + 1.5, 0.4), anchor="center", bounds=(0, 1920))


def b_estado(c, t, C, B):
    head(c, t, B["start"], "O ESTADO FÍSICO", "O PF E O PE DECIDEM", BLUE)
    card(c, *CARD_R)
    x0, x1, y = 260, 1660, 430
    xf, xe = 700, 1220
    at = ep(t, C["05.t"], 0.5)
    for (a_, b_), col, cue, lab in (((x0, xf), BLUE, "05.s", "SÓLIDO"), ((xf, xe), SKY, "05.l", "LÍQUIDO"),
                                    ((xe, x1), AMBER, "05.g", "GASOSO")):
        a = ep(t, C[cue], 0.5)
        rrect(c, a_, y - 50, b_ - a_, 100, 0, col, 0.25 * a)
        text_mid(c, lab, (a_ + b_) / 2, y, 40, "black", col, a)
    arrow(c, x0, y + 90, x1 + 20, y + 90, INK, at, 4, 16)
    text(c, "temperatura", x1, y + 140, 28, "bold", GRAY, at, align="right")
    for xx, lab in ((xf, "PF"), (xe, "PE")):
        line(c, xx, y - 80, xx, y + 100, INK, at, 4)
        pill(c, lab, xx, y - 105, INK, size=28, a=at, anchor="center", bounds=(0, 1920))
    ah = ep(t, C["05.h"], 0.5)
    text(c, "−39 °C", xf, y + 190, 34, "black", INK2, ah)
    text(c, "357 °C", xe, y + 190, 34, "black", INK2, ah)
    xm = xf + (25 + 39) / (357 + 39) * (xe - xf)
    if ah > 0:
        c.drawCircle(xm, y + 90, 16, paint(RED, ah))
    pill(c, "mercúrio a 25 °C: LÍQUIDO", xm + 40, y + 260, RED, size=30, a=ah, bounds=(0, 1920))


# ======================================================================
# pura x mistura
# ======================================================================

def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "TRÊS PERGUNTAS", "CLASSIFICAM QUALQUER MATERIAL", GREEN)
    card(c, *CARD_R)
    at, aa, ab, ac = (ep(t, C[k], 0.5) for k in ("06.t", "06.a", "06.b", "06.c"))
    R, P, M = (960, 230), (560, 410), (1360, 410)
    for (p, q), a in (((R, P), aa), ((R, M), aa), ((P, (400, 600)), ab), ((P, (720, 600)), ab), ((M, (1200, 600)), ac),
                      ((M, (1520, 600)), ac)):
        line(c, p[0], p[1] + 36, q[0], q[1] - 36, LIGHT, a, 4)
    node(c, "MATÉRIA", *R, INK, at)
    node(c, "SUBSTÂNCIA PURA", *P, GREEN, aa)
    node(c, "MISTURA", *M, PURPLE, aa)
    pill(c, "1 ou + substâncias?", 960, 330, AMBER, size=24, a=aa, anchor="center")
    node(c, "SIMPLES", 400, 600, GREEN, ab, 28)
    node(c, "COMPOSTA", 720, 600, GREEN, ab, 28)
    pill(c, "1 ou + elementos?", 560, 510, AMBER, size=22, a=ab, anchor="center")
    text(c, "O₂ · Fe", 400, 700, 32, "black", INK2, ab)
    text(c, "H₂O · NaCl", 720, 700, 32, "black", INK2, ab)
    node(c, "HOMOGÊNEA", 1200, 600, PURPLE, ac, 28)
    node(c, "HETEROGÊNEA", 1520, 600, PURPLE, ac, 28)
    pill(c, "quantas fases?", 1360, 510, AMBER, size=22, a=ac, anchor="center")
    text(c, "1 fase: ar · aço", 1200, 700, 30, "black", INK2, ac)
    text(c, "2+: granito", 1520, 700, 30, "black", INK2, ac)


def b_simples(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIA PURA", "SIMPLES OU COMPOSTA?", GREEN)
    for k, (cue, tt, f, sub, col) in enumerate((("07.a", "SIMPLES", "O₂ · N₂ · Fe", "um único ELEMENTO", GREEN),
                                                ("07.b", "COMPOSTA", "H₂O · CO₂ · NaCl", "dois ou mais elementos", BLUE))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 180 + dy
        card(c, x, y, 700, 330, a)
        text(c, tt, x + 350, y + 70, 36, "black", col, a)
        text(c, f, x + 350, y + 190, 66, "black", INK, a)
        text(c, sub, x + 350, y + 270, 32, "bold", INK2, a)
    ac = ep(t, C["07.c"], 0.5)
    atom(c, 370, 660, 46, OXY, ac, "O"); atom(c, 450, 660, 46, OXY, ac, "O")
    text(c, "O₂: 2 átomos, 1 elemento", 530, 674, 34, "black", INK, ac, align="left")
    for k in range(8):
        ang = 2 * math.pi * k / 8 + t * 0.3
        atom(c, 1150 + 80 * math.cos(ang), 660 + 80 * math.sin(ang), 24, AMBER, ac * ep(t, C["07.c"] + 1.0, 0.5))
    text_mid(c, "S₈", 1150, 660, 40, "black", INK, ac * ep(t, C["07.c"] + 1.0, 0.5))
    text(c, "8 átomos, 1 elemento", 1270, 674, 34, "black", INK, ac * ep(t, C["07.c"] + 1.0, 0.5), align="left")
    pill(c, "conte ELEMENTOS, nunca átomos", W / 2, 800, AMBER, size=30, a=ep(t, C["07.d"], 0.5), anchor="center")


def b_q_simples(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "QUANTAS SÃO SIMPLES?", BLUE)
    items = [("O₂", True), ("O₃", True), ("H₂O", False), ("NaCl", False), ("N₂", True), ("CO₂", False), ("Fe", True)]
    cw, ch, gap = 330, 170, 30
    for k, (f, simp) in enumerate(items):
        row, col_ = (0, k) if k < 4 else (1, k - 4)
        n = 4 if row == 0 else 3
        x0 = W / 2 - (n * cw + (n - 1) * gap) / 2
        a, dy = rise(t, C["08.e"] + 0.55 * k)
        if a <= 0:
            continue
        x, y = x0 + col_ * (cw + gap), 180 + row * (ch + 30) + dy
        card(c, x, y, cw, ch, a)
        b = ep(t, C["08.s"] + (0.25 * k if simp else 0.6), 0.4)
        if simp and b > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, cw, ch), 28, 28), paint(GREEN, b, stroke=6))
        text_mid(c, f, x + cw / 2, y + 70, 60, "black", INK, a)
        pill(c, "simples" if simp else "composta", x + cw / 2, y + 138, GREEN if simp else GRAY, size=22, a=a * b,
             anchor="center", bounds=(0, 1920))
    result_box(c, "4 substâncias simples", W / 2, 640, 50, ep(t, C["08.r"], 0.5), GREEN)
    pill(c, "tirou O₂ e N₂ por terem 2 átomos? marcou 2: ERRADO", W / 2, 765, RED, size=28, a=ep(t, C["08.x"], 0.5),
         anchor="center")


def b_misturas(c, t, C, B):
    head(c, t, B["start"], "MISTURAS", "HOMOGÊNEA OU HETEROGÊNEA?", PURPLE)
    for k, (cue, tt, sub, ex, layers, col) in enumerate((
            ("09.a", "HOMOGÊNEA", "uma única fase (solução)", ["ar", "água com sal", "aço (solução sólida)"],
             [(0.75, WATER, 0.7)], GREEN),
            ("09.b", "HETEROGÊNEA", "duas ou mais fases", ["água e óleo", "granito"],
             [(0.45, WATER, 0.8), (0.3, OIL, 0.9)], RED))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 180 + dy
        card(c, x, y, 700, 470, a)
        text(c, tt, x + 350, y + 64, 38, "black", col, a)
        text(c, sub, x + 350, y + 110, 28, "bold", INK2, a)
        beaker(c, x + 60, y + 160, 230, 260, a, layers)
        for j, s in enumerate(ex):
            text(c, "• " + s, x + 340, y + 220 + j * 64, 34, "black", INK, a * ep(t, C[cue] + 0.6 + 0.5 * j, 0.3), align="left")
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        c.drawCircle(330, 745, 46, paint("#FFF7ED", ac)); c.drawCircle(330, 745, 46, paint(INK2, ac, stroke=4))
        rnd = random.Random(3)
        for _ in range(14):
            c.drawCircle(330 + rnd.uniform(-30, 30), 745 + rnd.uniform(-30, 30), 6, paint(OIL, ac))
    pill(c, "leite e sangue: parecem uniformes, mas são HETEROGÊNEOS", 400, 745, RED, size=28, a=ac, bounds=(0, 1920))


def b_gases(c, t, C, B):
    head(c, t, B["start"], "REGRA DE OURO", "TODA MISTURA DE GASES É HOMOGÊNEA", AMBER)
    aa = ep(t, C["10.a"], 0.5)
    x, y, w, h = 200, 190, 640, 560
    card(c, x, y, w, h, aa)
    if aa > 0:
        clip_rect(c, x + 30, y + 30, w - 60, h - 160, 20)
        rnd = random.Random(7)
        for k in range(46):
            px0, py0 = rnd.uniform(0, 1), rnd.uniform(0, 1)
            vx, vy = rnd.uniform(-0.12, 0.12), rnd.uniform(-0.12, 0.12)
            px = abs(((px0 + vx * t) % 2) - 1)
            py = abs(((py0 + vy * t) % 2) - 1)
            c.drawCircle(x + 50 + px * (w - 100), y + 50 + py * (h - 200), 11, paint(BLUE if k % 2 else OXY, aa * 0.85))
        c.restore()
        text(c, "gases se misturam: UMA fase só", x + w / 2, y + h - 60, 32, "black", INK, aa)
    for k, (cue, tt, sub, col) in enumerate((("10.b", "AR = MISTURA", "78% N₂ · 21% O₂ · 1% outros", PURPLE),
                                             ("10.c", "ÁGUA MINERAL = MISTURA", "tem sais dissolvidos · só a destilada ≈ pura", BLUE))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        yy = 190 + k * 290 + dy
        card(c, 900, yy, 820, 250, a)
        text(c, tt, 1310, yy + 100, 46, "black", col, a)
        text(c, sub, 1310, yy + 170, 30, "bold", INK2, a)


# ======================================================================
# fases e componentes
# ======================================================================

def b_fases(c, t, C, B):
    head(c, t, B["start"], "FASE x COMPONENTE", "DOIS NÚMEROS DIFERENTES", RED)
    for k, (cue, tt, sub, how, col) in enumerate((("11.f", "FASE", "cada porção com aspecto UNIFORME", "conte o que você VÊ", BLUE),
                                                  ("11.c", "COMPONENTE", "cada SUBSTÂNCIA presente", "conte as SUBSTÂNCIAS", PURPLE))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 190 + dy
        card(c, x, y, 700, 480, a)
        text(c, tt, x + 350, y + 110, 72, "black", col, a)
        text(c, sub, x + 350, y + 220, 32, "bold", INK, a)
        pill(c, how, x + 350, y + 360, col, size=32, a=a, anchor="center", bounds=(0, 1920))
    pill(c, "a prova adora pedir os DOIS", W / 2, 765, RED, size=32, a=ep(t, C["11.x"], 0.5), anchor="center")


def b_gelo(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO", "ÁGUA E TRÊS CUBOS DE GELO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    bx, by, bw, bh = 300, 250, 460, 500

    def cubes(c):
        for k in range(3):
            cx = bx + 70 + k * 130 + 8 * math.sin(t * 1.2 + k)
            rrect(c, cx, by + 130 + 6 * math.sin(t * 1.5 + k * 2), 100, 86, 14, "#F8FAFC", aa)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx, by + 130 + 6 * math.sin(t * 1.5 + k * 2), 100, 86), 14, 14),
                        paint("#94A3B8", aa, stroke=3))
    beaker(c, bx, by, bw, bh, aa, [(0.72, WATER, 0.75)], cubes)
    ax = ep(t, C["12.x"], 0.5)
    if ax > 0:
        pd = paint(RED, ax, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx + 50, by + 112, 400, 126), 20, 20), pd)
    ac = ep(t, C["12.c"], 0.5)
    text(c, "COMPONENTES", 1300, 300, 34, "black", PURPLE, ac)
    text(c, "1", 1300, 400, 100, "black", PURPLE, ac)
    text(c, "só H₂O", 1300, 450, 30, "bold", INK2, ac)
    af = ep(t, C["12.f"], 0.5)
    text(c, "FASES", 1300, 540, 34, "black", BLUE, af)
    text(c, "2", 1300, 640, 100, "black", BLUE, af)
    text(c, "líquido + sólido", 1300, 690, 30, "bold", INK2, af)
    pill(c, "3 cubos = UMA fase (mesma substância, mesmo estado)", W / 2, 800, RED, size=26, a=ax, anchor="center")


def b_bronze(c, t, C, B):
    head(c, t, B["start"], "FASES E COMPONENTES", "SÃO INDEPENDENTES", RED)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    bx, by, bw, bh = 280, 230, 480, 520

    def fill(c):
        rnd = random.Random(11)
        for _ in range(160):
            c.drawCircle(bx + rnd.uniform(0, bw), by + bh - rnd.uniform(0, 110), rnd.uniform(4, 8), paint("#A16207", aa * 0.5))
        rrect(c, bx + 150, by + bh - 190, 180, 90, 12, BRONZE, aa)
        text_mid(c, "bronze", bx + 240, by + bh - 145, 28, "black", "#FFFFFF", aa)
    beaker(c, bx, by, bw, bh, aa, [(0.22, SAND, 0.9), (0.55, WATER, 0.7)], fill)
    af = ep(t, C["13.f"], 0.5)
    text(c, "FASES: 3", 1330, 300, 56, "black", BLUE, af)
    for k, s in enumerate(("bronze (liga homogênea = 1 fase)", "água", "areia")):
        text(c, s, 1330, 360 + k * 44, 30, "bold", INK2, af * ep(t, C["13.f"] + 0.4 * k, 0.3))
    ac = ep(t, C["13.c"], 0.5)
    text(c, "COMPONENTES: 4", 1330, 560, 56, "black", PURPLE, ac)
    text(c, "cobre · estanho · água · areia", 1330, 620, 32, "bold", INK2, ac)
    result_box(c, "3 fases · 4 componentes", 1330, 740, 46, ep(t, C["13.x"], 0.5), RED)


# ======================================================================
# curva de aquecimento
# ======================================================================

def chart_card(c, x, y, title, col, a, pts, frac, labels=()):
    card(c, x, y, 780, 580, a)
    text(c, title, x + 390, y + 60, 34, "black", col, a)
    px, py, pw, ph = x + 100, y + 120, 620, 360
    axes(c, px, py, pw, ph, a)
    P = to_px(px, py, pw, ph, pts)
    draw_partial(c, poly_path(P), frac, col, a, 8)
    return P


def b_curva(c, t, C, B):
    head(c, t, B["start"], "CURVA DE AQUECIMENTO", "CONTE OS PATAMARES", RED)
    aa = ep(t, C["14.a"], 0.5)
    k = 5 * ep(t, C["14.a"], 3.0)
    P = chart_card(c, 160, 180, "SUBSTÂNCIA PURA", GREEN, aa, PURE, seg_frac(PURE, k))
    for i, cue, lab in ((1, "14.c", "fusão (PF)"), (3, "14.d", "ebulição (PE)")):
        a = ep(t, C[cue], 0.4)
        (x0, y0), (x1, _) = P[i], P[i + 1]
        line(c, x0, y0, x1, y0, AMBER, a, 12)
        pill(c, lab, (x0 + x1) / 2, y0 - 40, AMBER, size=24, a=a, anchor="center", bounds=(0, 1920))
    pill(c, "patamar: a energia vai para a MUDANÇA, T não sobe", W / 2, 805, AMBER, size=26,
         a=fw(t, C["14.b"], C["15.m"] - 0.2), anchor="center")
    am = ep(t, C["15.m"], 0.5)
    if am > 0:
        km = 5 * ep(t, C["15.m"], 3.0)
        chart_card(c, 980, 180, "MISTURA COMUM", PURPLE, am, MIX, seg_frac(MIX, km))
        text(c, "nenhum patamar: a temperatura VARIA", 1370, 752, 26, "black", PURPLE, ep(t, C["15.m"] + 2.5, 0.5))
    pill(c, "a curva NÃO diz se é simples ou composta", W / 2, 805, RED, size=28, a=ep(t, C["15.x"], 0.5), anchor="center")


def b_enganam(c, t, C, B):
    head(c, t, B["start"], "AS MISTURAS QUE", "ENGANAM O GRÁFICO", RED)
    card(c, *CARD_R)
    at = ep(t, C["16.t"], 0.5)
    cols = (("TIPO", 230, "left"), ("FUSÃO", 860, "center"), ("EBULIÇÃO", 1140, "center"), ("EXEMPLO", 1300, "left"))
    for s, x, al in cols:
        text(c, s, x, 240, 28, "black", GRAY, at, align=al)
    line(c, 200, 262, 1720, 262, LINE, at, 3)
    rows = [("16.e", "EUTÉTICA", True, False, "solda Sn-Pb · 183 °C", AMBER),
            ("16.a", "AZEOTRÓPICA", False, True, "álcool 96% · 78 °C", SKY),
            ("16.p", "SUBSTÂNCIA PURA", True, True, "água destilada", GREEN),
            ("16.p", "MISTURA COMUM", False, False, "água e sal", GRAY)]
    for k, (cue, nome, fu, eb, ex, col) in enumerate(rows):
        a, dy = rise(t, C[cue] + (0.8 if k == 3 else 0))
        y = 335 + k * 95 + dy
        text_mid(c, nome, 230, y, 38, "black", col, a, align="left")
        for ok, x in ((fu, 860), (eb, 1140)):
            if ok:
                check_icon(c, x - 85, y, 18, a, GREEN)
                text_mid(c, "constante", x + 18, y, 28, "black", GREEN, a)
            else:
                text_mid(c, "em faixa", x, y, 28, "bold", GRAY, a)
        text_mid(c, ex, 1300, y, 28, "bold", INK2, a, align="left")
    pill(c, "EUTÉTICA lembra FUNDIR · AZEOTRÓPICA lembra FERVER", W / 2, 765, AMBER, size=30,
         a=ep(t, C["16.m"], 0.5), anchor="center")


def b_q_solda(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "A LIGA DE SOLDA", BLUE)
    stmt_card(c, t, [(C["17.e1"], "Funde a 183 °C,\ntemperatura CONSTANTE"), (C["17.e2"], "Ferve em uma FAIXA"),
                     (C["17.e3"], "O que ela é?")], size=38)
    a2 = ep(t, C["17.e2"], 0.5)
    px, py, pw, ph = 230, 560, 540, 220
    axes(c, px, py, pw, ph, a2)
    E = [(0, 0.06), (0.25, 0.4), (0.5, 0.4), (1.0, 0.95)]
    P = to_px(px, py, pw, ph, E)
    draw_partial(c, poly_path(P), ep(t, C["17.e2"], 2.0), AMBER, a2, 7)
    a = ep(t, C["17.s1"], 0.5)
    if a <= 0:
        return
    sol_card(c, a=a)
    text(c, "1 patamar só, na FUSÃO", 1330, 320, 48, "black", INK, a)
    result_box(c, "MISTURA EUTÉTICA", 1330, 470, 58, ep(t, C["17.s2"], 0.5), GREEN)
    ax = ep(t, C["17.x"], 0.5)
    text(c, "2 patamares → substância pura", 1330, 620, 32, "bold", INK2, ax)
    text(c, "patamar na ebulição → azeotrópica", 1330, 680, 32, "bold", INK2, ep(t, C["17.x"] + 1.5, 0.5))


# ======================================================================
# alotropia
# ======================================================================

def b_alotropia(c, t, C, B):
    head(c, t, B["start"], "ALOTROPIA", "MESMO ELEMENTO, SUBSTÂNCIAS DIFERENTES", PURPLE)
    for k, (cue, f, nome, sub, col) in enumerate((("18.a", "O₂", "gás oxigênio", "o que a gente respira", BLUE),
                                                  ("18.b", "O₃", "ozônio", "protege a atmosfera · tóxico no solo", PURPLE))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x, y = 200 + k * 820, 190 + dy
        card(c, x, y, 700, 500, a)
        cx, cy = x + 350, y + 180
        if k == 0:
            atom(c, cx - 45, cy, 58, OXY, a, "O"); atom(c, cx + 45, cy, 58, OXY, a, "O")
        else:
            atom(c, cx - 95, cy + 40, 54, OXY, a, "O"); atom(c, cx, cy - 25, 54, OXY, a, "O"); atom(c, cx + 95, cy + 40, 54, OXY, a, "O")
        text(c, f, cx, y + 360, 64, "black", col, a)
        text(c, nome, cx, y + 410, 34, "black", INK, a)
        text(c, sub, cx, y + 455, 28, "bold", INK2, a)
    pill(c, "mesmo ELEMENTO, substâncias DIFERENTES", W / 2, 775, PURPLE, size=32, a=ep(t, C["18.c"], 0.5), anchor="center")


def b_carbono(c, t, C, B):
    head(c, t, B["start"], "OS ALÓTROPOS DO CARBONO", "A ESTRUTURA DECIDE", INK)

    def diamante(c, x, y, w, h, a):
        text(c, "DIAMANTE", x + w / 2, y + 60, 36, "black", SKY, a)
        nodes = []
        for i in range(5):
            for j in range(4):
                nodes.append((x + 70 + i * 85 + (j % 2) * 42, y + 120 + j * 62))
        for (x1, y1) in nodes:
            for (x2, y2) in nodes:
                d = math.hypot(x2 - x1, y2 - y1)
                if 0 < d < 80:
                    line(c, x1, y1, x2, y2, INK2, a * 0.7, 3)
        for p in nodes:
            c.drawCircle(*p, 10, paint(INK, a))
        text(c, "4 ligações por átomo", x + w / 2, y + 420, 28, "bold", INK2, a)
        pill(c, "DURÍSSIMO", x + w / 2, y + 480, SKY, size=28, a=a, anchor="center", bounds=(0, 1920))

    def grafite(c, x, y, w, h, a):
        text(c, "GRAFITE", x + w / 2, y + 60, 36, "black", INK2, a)
        for k in range(3):
            off = 18 * math.sin(t * 1.4 + k * 1.3) if t > C["19.g"] else 0
            hexgrid(c, x + 90 + off, y + 125 + k * 90, 7, 1, 22, INK2, a, 3, skew=0.9, sy=0.35)
        arrow(c, x + 60, y + 410, x + w - 60, y + 410, AMBER, a, 4, 16)
        text(c, "folhas que DESLIZAM", x + w / 2, y + 395, 28, "bold", INK2, a)
        pill(c, "MACIO · risca o papel", x + w / 2, y + 480, GRAY, size=28, a=a, anchor="center", bounds=(0, 1920))

    def grafeno(c, x, y, w, h, a):
        text(c, "GRAFENO e NANOTUBOS", x + w / 2, y + 60, 32, "black", GREEN, a)
        clip_rect(c, x + 30, y + 95, w - 60, 170, 12)
        hexgrid(c, x + 50, y + 110, 9, 3, 20, GREEN, a, 3)
        c.restore()
        rrect(c, x + 80, y + 300, w - 160, 80, 40, GREEN, a * 0.12)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 80, y + 300, w - 160, 80), 40, 40), paint(GREEN, a, stroke=4))
        for k in range(7):
            xx = x + 120 + k * 42
            line(c, xx, y + 302, xx + 20, y + 378, GREEN, a * 0.6, 3)
        text(c, "folha de 1 átomo · folha enrolada", x + w / 2, y + 420, 26, "bold", INK2, a)
        pill(c, "NANOTECNOLOGIA", x + w / 2, y + 480, GREEN, size=28, a=a, anchor="center", bounds=(0, 1920))

    tiles(c, t, [(C["19.d"], diamante), (C["19.g"], grafite), (C["19.n"], grafeno)], 175, h=530)
    pill(c, "mesmo carbono: a ESTRUTURA decide a propriedade", W / 2, 785, PURPLE, size=30, a=ep(t, C["19.x"], 0.5), anchor="center")


# ======================================================================
# cotidiano
# ======================================================================

def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "MATERIAIS DO DIA A DIA", "PURO OU MISTURA?", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["20.a"], 0.5)
    text(c, "LIGAS = misturas homogêneas", 230, 250, 38, "black", PURPLE, aa, align="left")
    for k, (s, col) in enumerate((("AÇO  Fe + C", INK2), ("BRONZE  Cu + Sn", BRONZE), ("LATÃO  Cu + Zn", AMBER))):
        pill(c, s, 230 + k * 400, 320, col, size=30, a=ep(t, C["20.a"] + 0.5 * k, 0.4), bounds=(0, 1920))
    ab = ep(t, C["20.b"], 0.5)
    text(c, "OURO 18 QUILATES", 230, 440, 38, "black", AMBER, ab, align="left")
    for k in range(24):
        a = ep(t, C["20.b"] + 0.05 * k, 0.3)
        rrect(c, 230 + (k % 12) * 52, 470 + (k // 12) * 52, 44, 44, 8, "#EAB308" if k < 18 else "#9CA3AF", a)
    text(c, "18/24 = 75% de ouro  →  MISTURA", 900, 530, 40, "black", INK, ep(t, C["20.b"] + 2.5, 0.5), align="left")
    ac = ep(t, C["20.c"], 0.5)
    text(c, "SORO FISIOLÓGICO: água + NaCl 0,9%  →  mistura homogênea", 230, 680, 34, "black", BLUE, ac, align="left")


def b_q_materiais(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO", "QUAL É SUBSTÂNCIA PURA?", BLUE)
    items = [("água mineral", "s1", "tem sais · MISTURA"), ("ouro 18 k", "s2", "liga · MISTURA"), ("gás oxigênio (O₂)", "r", "SUBSTÂNCIA PURA"),
             ("ar filtrado", "s3", "gases misturados · MISTURA"), ("granito", "s4", "HETEROGÊNEO")]
    cw, ch, gap = 460, 190, 40
    for k, (nome, cue, st) in enumerate(items):
        row, cl = (0, k) if k < 3 else (1, k - 3)
        n = 3 if row == 0 else 2
        x0 = W / 2 - (n * cw + (n - 1) * gap) / 2
        a, dy = rise(t, C["21.e"] + 0.5 * k)
        if a <= 0:
            continue
        x, y = x0 + cl * (cw + gap), 190 + row * (ch + 40) + dy
        card(c, x, y, cw, ch, a)
        b = ep(t, C["21." + cue], 0.4)
        ok = cue == "r"
        if ok and b > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, cw, ch), 28, 28), paint(GREEN, b, stroke=7))
        text_mid(c, nome, x + cw / 2, y + 75, 40, "black", INK, a)
        pill(c, st, x + cw / 2, y + 145, GREEN if ok else GRAY, size=24, a=a * b, anchor="center", bounds=(0, 1920))
    result_box(c, "só o gás oxigênio", W / 2, 720, 50, ep(t, C["21.r"] + 0.8, 0.5), GREEN)


# ======================================================================
# fechamento
# ======================================================================

def b_estrategia(c, t, C, B):
    head(c, t, B["start"], "ESTRATÉGIA", "NA HORA DA PROVA", GREEN)
    cards_row(c, t, [("1", "3 perguntas\npara classificar", C["22.a"], GREEN), ("2", "Gráfico?\nconte os patamares", C["22.b"], RED),
                     ("3", "Sistema?\nconte 2 vezes", C["22.c"], BLUE)], cw=440, chh=400, title_size=36)


def b_erros(c, t, C, B):
    head(c, t, B["start"], "OS ERROS QUE", "MAIS CUSTAM PONTOS", RED)
    errors_list(c, t, [(C["23.e1"], "O₂ é composto (2 átomos)", "O₂ é SIMPLES"),
                       (C["23.e2"], "3 cubos de gelo = 4 fases", "são 2 fases"),
                       (C["23.e3"], "T constante = puro", "só com 2 patamares"),
                       (C["23.e4"], "ar e água mineral: puros", "são MISTURAS"),
                       (C["23.e5"], "curva: simples ou composta", "só pura ou mistura")])


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"], "Já caiu na dos cubos de gelo?")


BLOCKS = dict(hook=b_hook, enem=b_enem, mapa=b_mapa, materia=b_materia, estado=b_estado, roteiro=b_roteiro,
              simples=b_simples, q_simples=b_q_simples, misturas=b_misturas, gases=b_gases, fases=b_fases, gelo=b_gelo,
              bronze=b_bronze, curva=b_curva, enganam=b_enganam, q_solda=b_q_solda, alotropia=b_alotropia,
              carbono=b_carbono, cotidiano=b_cotidiano, q_materiais=b_q_materiais, estrategia=b_estrategia,
              erros=b_erros, cta=b_cta)
