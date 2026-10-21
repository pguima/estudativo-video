"""Visual do vídeo 002 — Candle Range Theory (modo escuro).
Cada bloco é uma função draw(c, t, C, B): t = tempo global, C = cues globais ("cena.cue"), B = bloco.
"""
import math
import numpy as np
import skia
import motor
motor.set_theme("escuro")
from motor import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "candle_range_theory_PTBR.mp4"

# ======================================================================
# dados
# ======================================================================

def K(o, c, h=None, l=None):
    h = max(o, c) + 0.3 if h is None else h
    l = min(o, c) - 0.3 if l is None else l
    return [o, h, l, c]


def walk(seed, p0, p1, n, vol=0.8, wick=0.4, lo=-1e9, hi=1e9):
    rng = np.random.default_rng(seed)
    path = np.cumsum(rng.normal(0, vol, n))
    path -= np.arange(1, n + 1) / n * path[-1]
    closes = p0 + (p1 - p0) * np.arange(1, n + 1) / n + path
    out, o = [], p0
    for cl in closes:
        cl = float(np.clip(cl, lo + 0.3, hi - 0.3))
        h = min(max(o, cl) + abs(rng.normal(0, wick)), hi)
        l = max(min(o, cl) - abs(rng.normal(0, wick)), lo)
        out.append([o, h, l, cl]); o = cl
    out[-1][3] = p1
    out[-1][1] = max(out[-1][1], p1); out[-1][2] = min(out[-1][2], p1)
    return out


PDH = 60.0

# --- hook: diário forte, depois venda contra que nunca volta
HK = walk(5, 50, 56.5, 9, lo=47, hi=58.5) + [K(56.5, 58.6), K(58.6, 61.4, h=61.8), K(61.4, 60.7, h=61.9, l=60.3)] + \
    [K(60.7, 62.9, l=60.5), K(62.9, 64.6), K(64.6, 66.8, h=67.2), K(66.8, 68.0)]
HK_SELL = 11

# --- reversão (cenas 11-14)
RV = walk(11, 50, 56.0, 12, lo=46, hi=58.5)
RV_U1 = len(RV); RV += [K(56.0, 57.5), K(57.5, 59.6), K(59.6, 61.8, h=62.4, l=59.4)]
RV_HI = len(RV) - 1
RV += [K(61.8, 61.2, h=62.0, l=60.8)]
RV_CF = len(RV); RV += [K(61.2, 55.2, h=61.5, l=54.9)]
RV += walk(12, 55.2, 41.0, 8, hi=56, lo=39.8, vol=0.7) + [K(41.0, 39.7, l=39.4), K(39.7, 40.5)]
RV_HIT = len(RV) - 2
RV_T = dict(entry=55.2, sl=62.8, tp=40.0, cisd=56.0)

# --- falha (cenas 16-19) — painel direito
FL = walk(21, 52, 57, 6, lo=50, hi=58.5) + [K(57, 58.6), K(58.6, 61.2, h=61.6), K(61.2, 63.4, h=63.9)]
FL_BC = len(FL); FL += [K(63.4, 62.3, h=63.6, l=60.4)]
FL += [K(62.3, 64.5), K(64.5, 66.2, h=66.6)]
# painel esquerdo (reversão que funcionou)
FO = walk(22, 52, 57, 6, lo=50, hi=58.5) + [K(57, 58.6), K(58.6, 61.2, h=61.6), K(61.2, 63.4, h=63.9)]
FO_BC = len(FO); FO += [K(63.4, 56.2, h=63.6, l=55.9)]
FO += [K(56.2, 54.4), K(54.4, 52.6)]

# --- continuação (cenas 20-24)
CT = walk(31, 52, 58, 8, lo=49, hi=59.5)
CT_C1 = len(CT)
CT += [K(58, 60.6, h=61.0, l=57.7), K(60.6, 64.2, h=64.6, l=60.4), K(64.2, 65.6, h=66.2, l=62.6)]
CT += [K(65.6, 64.9, h=66.0, l=64.2), K(64.9, 65.4, h=65.8, l=64.6)]
CT_R1 = len(CT); CT += [K(65.4, 64.0, h=65.6), K(64.0, 62.5, h=64.2, l=61.9)]
CT_CF = len(CT); CT += [K(62.5, 65.7, h=65.9, l=62.3)]
CT += walk(32, 65.7, 73.6, 6, lo=64.5, hi=74.0, vol=0.6) + [K(73.6, 74.3, h=74.6)]
CT_HIT = len(CT) - 1
CT += [K(74.3, 73.8)]
CT_T = dict(entry=65.7, sl=61.6, tp=73.9, cisd=65.4, fvg=(CT_C1, 61.0, 62.6), low=61.9)

# --- exemplo 1
E1 = walk(41, 50, 56.8, 10, hi=57.5, lo=46)
E1_C1 = len(E1)
E1 += [K(56.8, 56.2, h=57.3, l=55.9), K(56.2, 60.9, h=61.3, l=56.0), K(60.9, 62.0, h=62.6, l=58.8)]
E1_X = len(E1); E1 += [K(62.0, 59.6, h=62.3, l=59.2)]
E1 += [K(59.6, 60.3, h=60.7, l=59.3)]
E1_R1 = len(E1); E1 += [K(60.3, 59.0, h=60.5, l=58.6), K(59.0, 58.2, h=59.3, l=57.5)]
E1_CF = len(E1); E1 += [K(58.2, 60.8, h=61.1, l=57.9)]
E1 += walk(42, 60.8, 67.6, 6, lo=59.5, hi=68.0, vol=0.6) + [K(67.6, 68.3, h=68.5)]
E1_HIT = len(E1) - 1
E1 += [K(68.3, 67.9)]
E1_T = dict(entry=60.8, sl=57.2, tp=68.0, cisd_bear=56.2, cisd_bull=60.3, fvg=(E1_C1, 57.3, 58.8), low=57.5)
E1_D = walk(43, 40, 47, 8, vol=1.6, wick=1.0) + [K(47, 45.5), K(45.5, 44.2), K(44.2, 43.0, l=42.2), K(43.0, 49.8, h=50.3, l=42.6)]

# --- exemplo 2
E2 = walk(51, 48, 55.5, 10, hi=57, lo=44.5)
E2_U1 = len(E2); E2 += [K(55.5, 57.8, h=58.1), K(57.8, 61.0, h=61.5, l=57.6)]
E2_WK = len(E2); E2 += [K(61.0, 59.7, h=61.3, l=55.2)]
E2_NH = len(E2); E2 += [K(59.7, 62.3, h=62.8, l=59.5)]
E2_CF = len(E2); E2 += [K(62.3, 58.4, h=62.5, l=58.0)]
E2 += walk(52, 58.4, 49.6, 6, hi=59.0, lo=48.6, vol=0.6) + [K(49.6, 48.9, l=48.7)]
E2_HIT = len(E2) - 1
E2 += [K(48.9, 49.4)]
E2_T = dict(entry=58.4, sl=63.1, tp=49.0, cisd1=55.5, cisd2=59.7, pdl=44.0)
E2_D = walk(53, 38, 45, 8, vol=1.5, wick=1.0) + [K(45, 47.5, h=48.2, l=44.4), K(47.5, 46.6, h=48.0), K(46.6, 52.4, h=52.8, l=46.2)]

DAILY = walk(61, 40, 46, 7, vol=1.6, wick=1.0) + [K(46, 44.3), K(44.3, 51.6, h=52.1, l=43.9)]

# ======================================================================
# utilidades
# ======================================================================
CARD_R = (140, 150, 1640, 690)
CH_R = (210, 205, 1270, 580)
XLAB = CH_R[0] + CH_R[2] + 18


def reveal(t, sched):
    n = sched[0][1]
    for tt, cnt, d in sched[1:]:
        if t >= tt:
            n = lerp(n, cnt, ease_io(prog(t, tt, d)) if d > 0 else 1.0)
    return n


def fw(t, t_in, t_out=1e9, d_in=0.45, d_out=0.4):
    return ep(t, t_in, d_in) * (1 - prog(t, t_out, d_out))


def level(c, ch, p, label, color, a, x0=None, x1=None, dash=(12, 8), width=2.5, lab_x=None, anchor="left", prog_=1.0,
          above=True, size=20):
    if a <= 0:
        return
    x0 = ch.x0 if x0 is None else x0
    x1 = ch.x0 + ch.w if x1 is None else x1
    hline(c, x0, x1, ch.y(p), color, a, width, dash, progress=prog_)
    if label:
        pill(c, label, x0 + 6 if lab_x is None else lab_x, ch.y(p) + (-26 if above else 26), color, size=size, a=a,
             anchor=anchor)


def body_box(c, ch, i, color, a, pad=7):
    if a <= 0:
        return
    o, h, l, cl = ch.k[i]
    r = skia.Rect.MakeLTRB(ch.xl(i) - pad, ch.y(max(o, cl)) - pad, ch.xr(i) + pad, ch.y(min(o, cl)) + pad)
    c.drawRRect(skia.RRect.MakeRectXY(r, 8, 8), paint(color, a, stroke=3))


def trade(c, t, ch, i0, i1, T, ev, labels=True, boxes=True):
    """caixas de risco/retorno + etiquetas. ev: sl, tp, hit, en"""
    right = ch.x0 + ch.w
    xa, xb = ch.xl(i0), min(ch.xr(i1), right)
    a = ep(t, ev.get("sl", 1e9), 0.5) if boxes else 0
    if a > 0:
        ya, yb = sorted((ch.y(T["entry"]), ch.y(T["sl"])))
        c.drawRect(skia.Rect.MakeLTRB(xa, ya, lerp(xa, xb, a), yb), paint(RED, 0.18 * a))
    a = ep(t, ev.get("tp", 1e9), 0.5) if boxes else 0
    if a > 0:
        ya, yb = sorted((ch.y(T["entry"]), ch.y(T["tp"])))
        c.drawRect(skia.Rect.MakeLTRB(xa, ya, lerp(xa, xb, a), yb), paint(GREEN, 0.16 * a + 0.12 * ep(t, ev.get("hit", 1e9), 0.4)))
    if not labels:
        return
    a = fw(t, ev.get("en", 1e9))
    hline(c, xa, xb, ch.y(T["entry"]), INK, a, 2, (8, 6))
    pill(c, "ENTRADA", XLAB, ch.y(T["entry"]), INK, size=22, a=a)
    pill(c, "STOP", XLAB, ch.y(T["sl"]), RED, size=22, a=ep(t, ev.get("sl", 1e9), 0.4))
    pill(c, "ALVO 2R", XLAB, ch.y(T["tp"]), GREEN, size=22, a=ep(t, ev.get("tp", 1e9), 0.4) * (1 - ep(t, ev.get("hit", 1e9), 0.3)))
    ah = ep(t, ev.get("hit", 1e9), 0.45)
    pill(c, "+2R", XLAB, ch.y(T["tp"]), GREEN, size=26, a=ah)
    up = T["tp"] > T["entry"]
    pill(c, "ALVO ATINGIDO", (xa + xb) / 2, ch.y(T["tp"]) + (-46 if up else 46), GREEN, size=24, a=ah, anchor="center")


def daily_card(c, t, t0, ks, rect, a_mark=0.0, label="DIÁRIO", t_out=1e9):
    a = fw(t, t0, t_out)
    if a <= 0:
        return None
    c.saveLayerAlpha(None, int(a * 255))
    x, y, w, h = rect
    card(c, x, y, w, h)
    pill(c, label, x + 24, y + 34, BLUE, size=20, bounds=(0, 1920))
    ch = Chart(ks, (x + 40, y + 70, w - 80, h - 100), max_body=60)
    ch.draw(c, len(ks))
    i = len(ks) - 1
    body_box(c, ch, i, GREEN, a_mark, 9)
    c.restore()
    return ch


def cursor(c, x, y, a, press=0.0):
    if a <= 0:
        return
    s = 1 - 0.15 * press
    c.save(); c.translate(x, y); c.scale(1.6 * s, 1.6 * s)
    p = skia.Path()
    pts = [(0, 0), (0, 22), (6, 17), (10, 26), (14, 24), (10, 15.5), (17, 15.5)]
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint("#11151B", a, stroke=1.6))
    c.restore()


# ======================================================================
# BLOCOS
# ======================================================================

def b_hook(c, t, C, B):
    title_chip(c, "O ERRO MAIS CARO", "DO TRADER", t, B["start"] + 0.1, RED)
    # diário à esquerda
    daily_card(c, t, B["start"] + 0.2, DAILY, (140, 150, 470, 690), a_mark=ep(t, C["01.a"], 0.5))
    # 1h à direita
    a0 = ep(t, C["01.b"] - 0.6, 0.5)
    if a0 <= 0:
        return
    c.saveLayerAlpha(None, int(a0 * 255))
    card(c, 650, 150, 1130, 690)
    pill(c, "1 HORA", 674, 184, BLUE, size=20, bounds=(0, 1920))
    ch = Chart(HK, (700, 230, 860, 560), max_body=40)
    n = reveal(t, [(0, 9, 0), (C["01.b"], 11, 1.2), (C["01.c"], 12, 0.8), (C["01.e"], len(HK), 2.4)])
    level(c, ch, PDH, "MÁXIMA DO DIA ANTERIOR", AMBER, ep(t, C["01.b"] - 0.3, 0.5), size=19)
    ch.draw(c, n)
    a = ep(t, C["01.d"], 0.4)
    if a > 0:
        ch.ring(c, HK_SELL, HK[HK_SELL][3], RED, a, 20)
        pill(c, "VENDA", ch.x(HK_SELL), ch.y(HK[HK_SELL][2]) + 44, RED, size=21, a=a, anchor="center")
    ae = ep(t, C["01.e"] + 1.6, 0.5)
    pill(c, "NUNCA VOLTOU", ch.x(len(HK) - 2), ch.y(69.5), RED, size=22, a=ae, anchor="center")
    c.restore()
    # mudar de opinião
    af = fw(t, C["02.f"], 1e9)
    if af > 0:
        osc = math.sin((t - C["02.f"]) * 2.4)
        pill(c, "VENDER?", 760, 790, RED, size=30, a=af * (0.45 + 0.55 * max(0, osc)), anchor="center")
        pill(c, "COMPRAR?", 1560, 790, GREEN, size=30, a=af * (0.45 + 0.55 * max(0, -osc)), anchor="center")


def b_mapa(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    text(c, "CANDLE RANGE THEORY", W / 2, 215, 46, "black", INK, a0, tracking=2)
    text(c, "a análise na ordem certa", W / 2, 262, 28, "medium", GRAY, a0)
    items = [("1", "Candle diário", "define o viés", BLUE, "03.a"), ("2", "Reversão", "sempre primeiro", RED, "03.b"),
             ("3", "Continuação", "só se a reversão falhar", GREEN, "03.c")]
    cw, chh, gap = 440, 330, 60
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (n, l1, l2, col, cue) in enumerate(items):
        a = ep(t, C[cue], 0.55)
        x = x0 + k * (cw + gap)
        if k:
            arrow(c, x - gap + 8, 300 + chh / 2, x - 8, 300 + chh / 2, LIGHT, a, 4, 14, progress=a)
        if a <= 0:
            continue
        y = 300 + (1 - a) * 30
        card(c, x, y, cw, chh, a)
        badge_num(c, n, x + cw / 2, y + 90, a, 42, bg=col)
        text(c, l1, x + cw / 2, y + 205, 44, "extrabold", INK, a)
        text(c, l2, x + cw / 2, y + 255, 28, "medium", GRAY, a)
    ad = ep(t, C["03.d"], 0.5)
    for k, (s, col) in enumerate((("ENTRADA", INK), ("STOP", RED), ("ALVO 2R", GREEN))):
        pill(c, s, W / 2 + (k - 1) * 240, 720, col, size=28, a=ad, anchor="center", bounds=(0, 1920))


def mini_candle(c, x, y_top, y_bot, o, h, l, cl, scale, col, a=1.0, bw=90):
    """desenha um candle isolado. preços em unidades arbitrárias -> y por escala"""
    Y = lambda p: y_bot - (p - l) * scale
    c.drawLine(x, Y(h), x, Y(l), paint(col, a, stroke=4))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - bw / 2, Y(max(o, cl)), x + bw / 2, Y(min(o, cl))), 6, 6),
                paint(col, a))
    return Y


def b_range(c, t, C, B):
    title_chip(c, "O QUE É", "CANDLE RANGE THEORY", t, B["start"] + 0.1, BLUE)
    split = ep(t, C["05.n"], 0.8)
    card(c, 140, 150, 1640, 690)
    # candle principal
    cx = lerp(W / 2, 470, split)
    o, h, l, cl = 42, 64, 38, 60
    sc = 400 / (h - l)
    ybot = 740
    Y = lambda p: ybot - (p - l) * sc
    abox = ep(t, C["04.box"], 0.6)
    if abox > 0:
        rrect(c, cx - 150, Y(h), 300, Y(l) - Y(h), 8, BLUE, abox * 0.14 * (1 - split))
    xr_end = lerp(cx + 150, 1700, split)
    ahi = ep(t, C["04.hi"], 0.5); alo = ep(t, C["04.lo"], 0.5)
    hline(c, cx - 150, xr_end, Y(h), AMBER, ahi, 3, (12, 8), progress=ahi)
    hline(c, cx - 150, xr_end, Y(l), AMBER, alo, 3, (12, 8), progress=alo)
    mini_candle(c, cx, 0, ybot, o, h, l, cl, sc, GREEN, ep(t, C["04.a"] - 0.3, 0.5), bw=110)
    pill(c, "MÁXIMA", cx - 170, Y(h), AMBER, size=24, a=ahi * (1 - split), anchor="right")
    pill(c, "MÍNIMA", cx - 170, Y(l), AMBER, size=24, a=alo * (1 - split), anchor="right")
    pill(c, "RANGE", cx + 170, (Y(h) + Y(l)) / 2, BLUE, size=26, a=abox * (1 - split))
    if split <= 0:
        return
    # dois cenários
    for k, (cue, lab, col, kind) in enumerate((("05.r", "REVERSÃO", RED, "rev"), ("05.cn", "CONTINUAÇÃO", GREEN, "cont"))):
        a = ep(t, C[cue], 0.6)
        if a <= 0:
            continue
        x = 900 + k * 480
        if kind == "rev":
            mini_candle(c, x, 0, ybot, 59, 68, 47, 50, sc, RED, a, bw=100)
            arrow(c, x + 80, Y(66), x + 80, Y(52), RED, a, 5, 18, progress=ep(t, C[cue] + 0.3, 0.7))
        else:
            mini_candle(c, x, 0, ybot, 60, 72.5, 58.5, 71.5, sc, GREEN, a, bw=100)
            arrow(c, x + 80, Y(63), x + 80, Y(71.5), GREEN, a, 5, 18, progress=ep(t, C[cue] + 0.3, 0.7))
        pill(c, lab, x, 230, col, size=26, a=a, anchor="center")
    aq = ep(t, C["05.q"], 0.5)
    pill(c, "QUAL DAS DUAS VOCÊ PODE OPERAR?", W / 2, 800, INK, size=28, a=aq, anchor="center")


def b_diario(c, t, C, B):
    s7, s8, s9 = C["07"], C["08"], C["09"]
    title_chip(c, "PASSO 1", "O CANDLE DIÁRIO", t, B["start"] + 0.1, BLUE)
    # cena 6: um candle grande
    a6 = fw(t, C["06.t"], s7 - 0.2)
    if a6 > 0:
        card(c, 610, 150, 700, 690, a6)
        mini_candle(c, W / 2, 0, 760, 42, 61, 40, 60, 540 / 21, GREEN, a6, bw=150)
        pill(c, "FECHADO", W / 2, 190, GREEN, size=24, a=a6 * ep(t, C["06.d"], 0.4), anchor="center")
    # cena 7: forte x fraco
    a7 = fw(t, s7, s8 - 0.2)
    if a7 > 0:
        for k, (lab, ok) in enumerate((("FORTE", True), ("FRACO", False))):
            x = 300 + k * 700
            aa = a7 * (ep(t, C["07.f"], 0.5) if ok else ep(t, C["07.w"], 0.5))
            if aa <= 0:
                continue
            card(c, x, 170, 620, 640, aa)
            if ok:
                mini_candle(c, x + 310, 0, 700, 42, 61, 40, 60, 440 / 21, GREEN, aa, bw=130)
                pill(c, "corpo perto da máxima", x + 310, 760, GREEN, size=22, a=aa, anchor="center")
            else:
                mini_candle(c, x + 310, 0, 700, 49.5, 61, 40, 50.6, 440 / 21, GREEN, aa, bw=130)
                pill(c, "indo e voltando o dia todo", x + 310, 760, GRAY, size=22, a=aa, anchor="center")
            check_icon(c, x + 80, 240, 30, aa, GREEN if ok else RED, "check" if ok else "x")
            text(c, lab, x + 130, 254, 40, "black", GREEN if ok else RED, aa, align="left")
    # cena 8: viés != comprador
    a8 = fw(t, C["08.b"], s9 - 0.2)
    if a8 > 0:
        card(c, 460, 200, 1000, 560, a8)
        text(c, "VIÉS DE ALTA", W / 2, 360, 92, "black", GREEN, a8)
        text(c, "para o dia seguinte", W / 2, 420, 34, "medium", GRAY, a8)
        ax = ep(t, C["08.x"], 0.5) * a8
        if ax > 0:
            text(c, "≠", W / 2, 560, 90, "black", INK, ax)
            text(c, "COMPRADOR", W / 2, 680, 70, "black", RED, ax)
    # cena 9: regras
    a9 = ep(t, s9, 0.5)
    if a9 > 0:
        card(c, 300, 180, 1320, 620, a9)
        rows = [("09.r1", "1", "Continuação: só a favor do diário (compra)", GREEN),
                ("09.r2", "2", "Mas a primeira opção é sempre a REVERSÃO", RED),
                ("09.inv", "3", "Diário forte de baixa: mesmo modelo, invertido", BLUE)]
        for k, (cue, n, s, col) in enumerate(rows):
            a = ep(t, C[cue], 0.5) * a9
            y = 320 + k * 160
            badge_num(c, n, 400, y, a, 38, bg=col)
            text(c, s, 470 + (1 - a) * 20, y + 15, 42, "bold", INK, a, align="left")


def b_niveis(c, t, C, B):
    title_chip(c, "MARQUE O", "RANGE DO DIA ANTERIOR", t, B["start"] + 0.1, AMBER)
    card(c, *CARD_R)
    ch = Chart(DAILY, (260, 230, 1000, 560), max_body=70)
    pill(c, "DIÁRIO", 170, 190, BLUE, size=22, bounds=(0, 1920))
    i = len(DAILY) - 1
    o, h, l, cl = DAILY[i]
    az = ep(t, C["10.z"], 0.6)
    if az > 0:
        c.drawRect(skia.Rect.MakeLTRB(ch.xl(i), ch.y(h), ch.x0 + ch.w + 200, ch.y(l)), paint(AMBER, 0.08 * az))
    ch.draw(c, len(DAILY))
    am, al = ep(t, C["10.m"], 0.6), ep(t, C["10.l"], 0.6)
    hline(c, ch.xl(i), 1700, ch.y(h), AMBER, am, 3, (12, 8), progress=am)
    hline(c, ch.xl(i), 1700, ch.y(l), AMBER, al, 3, (12, 8), progress=al)
    pill(c, "MÁXIMA DO DIA ANTERIOR (PDH)", 1700, ch.y(h) - 30, AMBER, size=22, a=am, anchor="right")
    pill(c, "MÍNIMA DO DIA ANTERIOR (PDL)", 1700, ch.y(l) + 30, AMBER, size=22, a=al, anchor="right")
    pill(c, "RANGE DE TRABALHO", 1500, (ch.y(h) + ch.y(l)) / 2, INK, size=24, a=az, anchor="center")
    ag = ep(t, C["10.g"], 0.5)
    pill(c, "PRÓXIMO: GRÁFICO DE 1 HORA  →", W / 2, 800, BLUE, size=26, a=ag, anchor="center")


def b_reversao(c, t, C, B):
    title_chip(c, "PASSO 2", "A REVERSÃO VEM PRIMEIRO", t, B["start"] + 0.1, RED)
    card(c, *CARD_R)
    pill(c, "1 HORA", 170, 190, BLUE, size=22, bounds=(0, 1920))
    ch = Chart(RV, CH_R, pmin=37, pmax=65)
    n = reveal(t, [(0, RV_U1, 0), (C["11.run"] - 0.4, RV_HI + 2, 2.2), (C["12.c1"] - 0.2, RV_CF + 1, 0.9),
                   (C["14.tr"] + 4.5, RV_HIT + 1, 2.4), (C["14.tr"] + 7.2, len(RV), 0.6)])
    clip = c.save()
    T = RV_T
    ev = dict(en=C["14.tr"], sl=C["14.tr"] + 1.4, tp=C["14.tr"] + 2.6, hit=C["14.tr"] + 7.0)
    trade(c, t, ch, RV_CF + 1, RV_HIT + 1, T, ev, labels=False)
    level(c, ch, PDH, "MÁXIMA DO DIA ANTERIOR", AMBER, ep(t, B["start"] + 0.4, 0.6), size=20)
    # linha do CISD
    alv = ep(t, C["13.lv"], 0.6)
    level(c, ch, T["cisd"], None, RED, alv, x0=ch.xl(RV_U1), x1=ch.x0 + ch.w, prog_=alv)
    ch.draw(c, n)
    # candles que fizeram a máxima
    ab = fw(t, C["13.lv"], C["14.ok"])
    if ab > 0:
        x0, x1 = ch.xl(RV_U1) - 8, ch.xr(RV_HI) + 8
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, ch.y(62.6), x1, ch.y(55.6)), 10, 10), paint(GREEN, ab, stroke=2.5))
    pill(c, "PREÇO TOMOU A MÁXIMA", ch.x(RV_HI), ch.y(62.4) - 36, AMBER, size=20, a=fw(t, C["11.run"] + 1.0, C["12.c1"]), anchor="center")
    body_box(c, ch, RV_CF, INK, fw(t, C["12.c1"] + 0.6, C["14.tr"]))
    pill(c, "CORPO FECHOU DE VOLTA NO RANGE", ch.xr(RV_CF) + 20, ch.y(57.5), INK, size=20, a=fw(t, C["12.c1"] + 0.8, C["13.lv"]))
    pill(c, "CISD (abertura do 1º candle de alta)", ch.xl(RV_U1) - 14, ch.y(T["cisd"]) + 28, RED, size=19, a=alv, anchor="right")
    pill(c, "FECHOU ABAIXO DO CISD", ch.xr(RV_CF) + 20, ch.y(55.2) + 30, RED, size=20, a=fw(t, C["13.cl"], C["14.tr"]))
    aok = fw(t, C["14.ok"], 1e9)
    pill(c, "REVERSÃO CONFIRMADA", ch.x(RV_CF), 250, RED, size=24, a=aok, anchor="center")
    c.restoreToCount(clip)
    trade(c, t, ch, RV_CF + 1, RV_HIT + 1, T, ev, boxes=False)


def b_pavio(c, t, C, B):
    title_chip(c, "REGRA DE OURO", "PAVIO NÃO É FECHAMENTO", t, B["start"] + 0.1, AMBER)
    for k, (cue, lab, ok) in enumerate((("15.wk", "SÓ PAVIO", False), ("15.bd", "CORPO FECHOU", True))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 260 + k * 720
        card(c, x, 170, 680, 620, a)
        sc = 22
        ly = 740 - (64 - 50) * sc
        cx = x + 340
        if ok:
            mini_candle(c, cx, 0, 740, 67, 68, 50, 55, sc, RED, a, bw=110)   # corpo fechou abaixo
        else:
            mini_candle(c, cx, 0, 740, 68.5, 70, 50, 65.5, sc, RED, a, bw=110)  # só o pavio abaixo
        hline(c, x + 40, x + 640, ly, AMBER, a, 3, (12, 8))
        pill(c, "MÁXIMA DO DIA ANTERIOR", x + 50, ly - 28, AMBER, size=18, a=a, bounds=(0, 1920))
        check_icon(c, x + 80, 230, 30, a, GREEN if ok else RED, "check" if ok else "x")
        text(c, lab, x + 130, 244, 36, "black", GREEN if ok else RED, a, align="left")
    an = ep(t, C["15.nc"], 0.5)
    pill(c, "SEM FECHAMENTO, SEM REVERSÃO", W / 2, 830, RED, size=28, a=an, anchor="center")


def _panel(c, t, ks, rect, n, a, i_bc, ok):
    x, y, w, h = rect
    card(c, x, y, w, h, a)
    if a <= 0:
        return None
    c.saveLayerAlpha(None, int(a * 255))
    ch = Chart(ks, (x + 50, y + 110, w - 100, h - 170), pmin=49, pmax=68, max_body=34)
    level(c, ch, PDH, None, AMBER, 1.0)
    ch.draw(c, n)
    c.restore()
    return ch


def b_falha(c, t, C, B):
    title_chip(c, "PASSO 3", "FECHOU DE VOLTA PARA DENTRO?", t, B["start"] + 0.1, AMBER, t_out=C["18.two"] - 0.2)
    title_chip(c, "DOIS FATOS", "AO MESMO TEMPO", t, C["18.two"], BLUE)
    dim = 1 - 0.75 * ep(t, C["18.two"], 0.5)
    # esquerda: funcionou
    al = ep(t, C["16.q"], 0.5) * dim
    chL = _panel(c, t, FO, (140, 160, 800, 640), reveal(t, [(0, FO_BC, 0), (C["16.l"], len(FO), 1.6)]), al, FO_BC, True)
    if chL:
        body_box(c, chL, FO_BC, GREEN, ep(t, C["16.l"] + 0.8, 0.4) * al)
        pill(c, "FECHOU DE VOLTA", 170, 205, GREEN, size=22, a=al, bounds=(0, 1920))
        pill(c, "→ REVERSÃO", 540, 760, GREEN, size=24, a=ep(t, C["16.l"] + 1.0, 0.4) * al, anchor="center", bounds=(0, 1920))
    # direita: falhou
    ar = ep(t, C["17.r"], 0.5) * dim
    chR = _panel(c, t, FL, (980, 160, 800, 640), reveal(t, [(0, FL_BC, 0), (C["17.bc"], FL_BC + 1, 0.8), (C["17.f"] + 0.6, len(FL), 1.4)]), ar, FL_BC, False)
    if chR:
        body_box(c, chR, FL_BC, RED, ep(t, C["17.ab"], 0.4) * ar)
        pill(c, "CORPO FICOU ACIMA", chR.xr(FL_BC) + 16, chR.y(62.8) + 46, RED, size=19, a=ep(t, C["17.ab"], 0.4) * ar,
             bounds=(0, 1920))
        pill(c, "FALHOU, FICOU ACIMA", 1010, 205, RED, size=22, a=ar, bounds=(0, 1920))
        pill(c, "→ CONTINUAÇÃO", 1380, 760, GREEN, size=24, a=ep(t, C["19.go"], 0.4) * ar / max(dim, 1e-3) if dim > 0 else 0,
             anchor="center", bounds=(0, 1920))
    # dois fatos
    a2 = fw(t, C["18.two"], 1e9)
    if a2 > 0:
        card(c, 460, 250, 1000, 470, a2)
        check_icon(c, 560, 380, 34, a2, GREEN)
        text(c, "O diário continua de ALTA", 620, 396, 46, "bold", INK, a2, align="left")
        check_icon(c, 560, 500, 34, ep(t, C["18.two"] + 1.6, 0.4) * a2, RED, "x")
        text(c, "A ideia de venda MORREU", 620, 516, 46, "bold", INK, ep(t, C["18.two"] + 1.6, 0.4) * a2, align="left")
        ag = ep(t, C["19.go"], 0.5) * a2
        pill(c, "AGORA SIM: PROCURE A CONTINUAÇÃO", W / 2, 640, GREEN, size=30, a=ag, anchor="center")


def b_continua(c, t, C, B):
    title_chip(c, "PASSO 4", "A CONTINUAÇÃO", t, B["start"] + 0.1, GREEN)
    card(c, *CARD_R)
    pill(c, "1 HORA", 170, 190, BLUE, size=22, bounds=(0, 1920))
    ch = Chart(CT, CH_R, pmin=49, pmax=76)
    T = CT_T
    n = reveal(t, [(0, CT_C1 + 4, 0), (C["20.pb"], CT_R1 + 2, 2.2), (C["21.lv"] + 2.2, CT_CF + 1, 0.8),
                   (C["24.s1"], CT_HIT + 1, 3.0), (C["24.s3"] + 1.0, len(CT), 0.5)])
    ev = dict(en=C["23.en"], sl=C["23.sl"], tp=C["23.tp"], hit=C["24.s1"] + 3.1)
    clip = c.save()
    trade(c, t, ch, CT_CF + 1, CT_HIT + 1, T, ev, labels=False)
    level(c, ch, PDH, "MÁXIMA DO DIA ANTERIOR", AMBER, ep(t, B["start"] + 0.3, 0.5), size=20)
    i0, p0, p1 = T["fvg"]
    af = ep(t, C["20.poi"], 0.6)
    ch.zone(c, i0, len(CT) - 1, p0, p1, AMBER, af, progress=af, fill=0.2)
    alv = ep(t, C["21.lv"], 0.6)
    level(c, ch, T["cisd"], None, GREEN, alv, x0=ch.xl(CT_R1), prog_=alv)
    ch.draw(c, n)
    pill(c, "FECHOU ACIMA DA MÁXIMA", ch.x(CT_C1 + 2), ch.y(66.2) - 34, GREEN, size=20, a=fw(t, C["20.a"], C["20.pb"] + 1), anchor="center")
    pill(c, "FVG", ch.xl(i0) - 14, ch.y((p0 + p1) / 2), AMBER, size=22, a=af, anchor="right")
    # candle aleatório "não"
    an = fw(t, C["21.nr"], C["21.lv"])
    if an > 0:
        ch.ring(c, 5, CT[5][3], RED, an, 18)
        pill(c, "QUALQUER CANDLE VERMELHO? NÃO", ch.x(5), ch.y(CT[5][2]) + 44, RED, size=20, a=an, anchor="center")
    pill(c, "CISD DE ALTA", ch.xl(CT_R1) - 14, ch.y(T["cisd"]), GREEN, size=20, a=alv, anchor="right")
    acb = ep(t, C["21.cb"], 0.5)
    if acb > 0:
        r = skia.Rect.MakeLTRB(ch.xl(CT_R1) - 8, ch.y(65.9), ch.xr(CT_CF) + 8, ch.y(T["low"]) + 6)
        c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), paint(BLUE, acb * 0.12))
        c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), paint(BLUE, acb, stroke=3))
        pill(c, "BLOCO DE CONTINUAÇÃO", ch.x(CT_R1 + 1), ch.y(T["low"]) + 46, BLUE, size=20, a=acb, anchor="center")
    pill(c, "A FAVOR DO DIÁRIO ✓", ch.x(CT_R1 + 1), ch.y(T["low"]) + 96, GREEN, size=20, a=fw(t, C["22.ag"], C["23.sl"]), anchor="center")
    c.restoreToCount(clip)
    trade(c, t, ch, CT_CF + 1, CT_HIT + 1, T, ev, boxes=False)
    for k, (cue, s, col) in enumerate((("24.s1", "STOP NA INVALIDAÇÃO", RED), ("24.s2", "ALVO FIXO: 2R", GREEN))):
        pill(c, s, 380 + k * 420, 800, col, size=22, a=fw(t, C[cue], 1e9), anchor="center", bounds=(0, 1920))


def b_ex1(c, t, C, B):
    title_chip(c, "EXEMPLO 1", "CONTINUAÇÃO", t, B["start"] + 0.1, GREEN)
    # diário
    sw = ep(t, C["26.h1"] - 0.3, 0.6)
    if sw < 1:
        c.saveLayerAlpha(None, int((1 - sw) * 255))
        card(c, *CARD_R)
        pill(c, "DIÁRIO", 170, 190, BLUE, size=22, bounds=(0, 1920))
        chd = Chart(E1_D, (300, 220, 1100, 560), max_body=60)
        chd.draw(c, len(E1_D))
        i = len(E1_D) - 1
        ad = ep(t, C["25.d"], 0.5)
        body_box(c, chd, i, GREEN, ad, 9)
        x0 = chd.xl(i - 3) - 8
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, chd.y(47.6), chd.xr(i - 1) + 8, chd.y(42.0)), 10, 10),
                    paint(RED, ad, stroke=2.5))
        pill(c, "3 CANDLES DE BAIXA", (x0 + chd.xr(i - 1)) / 2, chd.y(42.0) + 36, RED, size=20, a=ad, anchor="center")
        pill(c, "VIÉS DE ALTA", chd.xr(i) + 30, chd.y(49.8), GREEN, size=26, a=ep(t, C["25.b"], 0.5))
        c.restore()
    if sw <= 0:
        return
    c.saveLayerAlpha(None, int(sw * 255))
    card(c, *CARD_R)
    pill(c, "1 HORA", 170, 190, BLUE, size=22, bounds=(0, 1920))
    ch = Chart(E1, CH_R, pmin=46, pmax=70)
    T = E1_T
    n = reveal(t, [(0, E1_C1, 0), (C["26.run"] - 0.3, E1_X, 1.6), (C["27.in"] - 0.2, E1_X + 1, 0.8),
                   (C["28.fl"], E1_R1 + 2, 2.0), (C["28.cisd"], E1_CF + 1, 0.8),
                   (C["29.run"] + 0.4, E1_HIT + 1, C["29.hit"] - C["29.run"] - 0.4), (C["29.hit"] + 0.6, len(E1), 0.5)])
    ev = dict(en=C["29.en"], sl=C["29.sl"], tp=C["29.tp"], hit=C["29.hit"])
    clip = c.save()
    trade(c, t, ch, E1_CF + 1, E1_HIT + 1, T, ev, labels=False)
    level(c, ch, PDH, "MÁXIMA DO DIA ANTERIOR", AMBER, ep(t, C["26.h1"], 0.6), size=20)
    i0, p0, p1 = T["fvg"]
    af = ep(t, C["28.fvg"], 0.6)
    ch.zone(c, i0, len(E1) - 1, p0, p1, AMBER, af, progress=af, fill=0.2)
    acb = fw(t, C["27.cl"] - 0.6, C["28.fl"] + 1.0)
    level(c, ch, T["cisd_bear"], "CISD DE BAIXA", RED, acb, x0=ch.xl(E1_C1 + 1), above=False, size=19)
    alv = ep(t, C["28.cisd"], 0.5)
    level(c, ch, T["cisd_bull"], None, GREEN, alv, x0=ch.xl(E1_R1), prog_=alv)
    ch.draw(c, n)
    pill(c, "TOMOU A MÁXIMA", ch.x(E1_C1 + 2), ch.y(62.6) - 34, AMBER, size=20, a=fw(t, C["26.run"] + 0.8, C["27.no"]), anchor="center")
    body_box(c, ch, E1_X, INK, fw(t, C["27.in"] + 0.5, C["28.fl"]))
    pill(c, "FECHOU DE VOLTA...", ch.xr(E1_X) + 20, ch.y(60.8), INK, size=20, a=fw(t, C["27.in"] + 0.6, C["28.fl"]))
    pill(c, "...MAS SEM CISD = SEM OPERAÇÃO", ch.xr(E1_X) + 20, ch.y(60.8) + 46, RED, size=20, a=fw(t, C["27.no"], C["28.fl"]))
    pill(c, "REVERSÃO FALHOU", ch.x(E1_X + 1), 250, RED, size=22, a=fw(t, C["28.fl"], C["28.cisd"]), anchor="center")
    pill(c, "FVG", ch.xl(i0) - 14, ch.y((p0 + p1) / 2), AMBER, size=22, a=af, anchor="right")
    pill(c, "CISD DE ALTA", ch.xr(E1_CF) + 18, ch.y(T["cisd_bull"]) - 30, GREEN, size=19, a=fw(t, C["28.cisd"] + 0.4, C["29.en"]))
    ab = ep(t, C["28.cb"], 0.5)
    if ab > 0:
        r = skia.Rect.MakeLTRB(ch.xl(E1_R1) - 8, ch.y(61.2), ch.xr(E1_CF) + 8, ch.y(T["low"]) + 6)
        c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), paint(BLUE, ab * 0.12))
        c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), paint(BLUE, ab, stroke=3))
        pill(c, "BLOCO DE CONTINUAÇÃO", ch.x(E1_R1 + 1), ch.y(T["low"]) + 46, BLUE, size=20, a=ab, anchor="center")
    c.restoreToCount(clip)
    trade(c, t, ch, E1_CF + 1, E1_HIT + 1, T, ev, boxes=False)
    c.restore()


def b_ex2(c, t, C, B):
    title_chip(c, "EXEMPLO 2", "REVERSÃO", t, B["start"] + 0.1, RED)
    sw = ep(t, C["30.m"] + 1.6, 0.6)
    if sw < 1:
        c.saveLayerAlpha(None, int((1 - sw) * 255))
        card(c, *CARD_R)
        pill(c, "DIÁRIO", 170, 190, BLUE, size=22, bounds=(0, 1920))
        chd = Chart(E2_D, (300, 220, 1100, 560), max_body=60)
        chd.draw(c, len(E2_D))
        i = len(E2_D) - 1
        ad = ep(t, C["30.d"], 0.5)
        body_box(c, chd, i, GREEN, ad, 9)
        hline(c, chd.xl(i - 1), chd.xr(i) + 40, chd.y(E2_D[i - 1][1]), GRAY, ad, 2, (8, 6))
        pill(c, "FECHOU ACIMA DA MÁXIMA ANTERIOR", chd.xr(i) + 30, chd.y(E2_D[i - 1][1]), GREEN, size=19, a=ad)
        am = ep(t, C["30.m"], 0.5)
        hline(c, chd.xl(i), 1700, chd.y(E2_D[i][1]), AMBER, am, 3, (12, 8), progress=am)
        hline(c, chd.xl(i), 1700, chd.y(E2_D[i][2]), AMBER, am, 3, (12, 8), progress=am)
        c.restore()
    if sw <= 0:
        return
    c.saveLayerAlpha(None, int(sw * 255))
    card(c, *CARD_R)
    pill(c, "1 HORA", 170, 190, BLUE, size=22, bounds=(0, 1920))
    ch = Chart(E2, CH_R, pmin=42, pmax=65)
    T = E2_T
    n = reveal(t, [(0, E2_U1, 0), (C["31.run"] - 0.3, E2_WK, 1.2), (C["31.wk"] - 0.3, E2_WK + 1, 0.8),
                   (C["32.nh"] - 0.2, E2_NH + 1, 0.8), (C["32.cl"] - 0.2, E2_CF + 1, 0.8),
                   (C["34.run"] + 0.4, E2_HIT + 1, C["34.hit"] - C["34.run"] - 0.4), (C["34.hit"] + 0.6, len(E2), 0.5)])
    ev = dict(en=C["34.en"], sl=C["34.sl"], tp=C["34.tp"], hit=C["34.hit"])
    clip = c.save()
    trade(c, t, ch, E2_CF + 1, E2_HIT + 1, T, ev, labels=False)
    level(c, ch, PDH, "MÁXIMA DO DIA ANTERIOR", AMBER, ep(t, B["start"] + 2.0, 0.6), size=20)
    level(c, ch, T["pdl"], "MÍNIMA DO DIA ANTERIOR", AMBER, ep(t, B["start"] + 2.0, 0.6), above=False, size=20)
    a1 = fw(t, C["31.lv"], C["32.nl"])
    level(c, ch, T["cisd1"], None, RED, a1, x0=ch.xl(E2_U1), prog_=ep(t, C["31.lv"], 0.6))
    a2 = ep(t, C["32.nl"], 0.6)
    level(c, ch, T["cisd2"], None, RED, a2, x0=ch.xl(E2_NH), prog_=a2)
    ch.draw(c, n)
    pill(c, "CISD", ch.xl(E2_U1) - 14, ch.y(T["cisd1"]), RED, size=19, a=a1, anchor="right")
    ap = fw(t, C["31.wk"] + 0.3, C["32.nh"])
    ch.ring(c, E2_WK, E2[E2_WK][2], AMBER, ap, 16)
    pill(c, "SÓ PAVIO — ESPERE", ch.x(E2_WK), ch.y(E2[E2_WK][2]) + 42, AMBER, size=20, a=ap, anchor="center")
    pill(c, "NOVA MÁXIMA (1 candle)", ch.x(E2_NH), ch.y(62.8) - 36, INK, size=19, a=fw(t, C["32.nh"] + 0.4, C["33.q1"]), anchor="center")
    pill(c, "NOVO CISD", ch.xl(E2_NH) - 14, ch.y(T["cisd2"]) - 26, RED, size=19, a=a2, anchor="right")
    body_box(c, ch, E2_CF, RED, fw(t, C["32.cl"] + 0.5, C["34.en"]))
    # perguntas
    for k, cue in enumerate(("33.q1", "33.q2")):
        a = fw(t, C[cue], C["34.en"])
        txt = ("Tomou a máxima do dia anterior?", "CISD de baixa, de volta no range?")[k]
        y = 560 + k * 60
        pill(c, txt, 1060, y, INK, size=22, a=a, bounds=(0, 1920))
        check_icon(c, 1060 + text_w(txt, "bold", 22) + 60, y, 20, ep(t, C[cue] + 1.0, 0.3) * a, GREEN)
    pill(c, "VENDA VÁLIDA", ch.x(E2_CF), 250, RED, size=24, a=fw(t, C["33.ok"], C["34.hit"]), anchor="center")
    apdl = fw(t, C["35.pdl"], 1e9)
    if apdl > 0:
        arrow(c, ch.x(E2_HIT + 1), ch.y(48.4), ch.x(E2_HIT + 1), ch.y(T["pdl"]) - 10, AMBER, apdl, 4, 16,
              progress=ep(t, C["35.pdl"], 0.8))
        pill(c, "PRÓXIMO ALVO NATURAL", ch.x(E2_HIT + 1) + 24, ch.y(46.2), AMBER, size=19, a=apdl)
    pill(c, "SIMPLES: PEGUE OS 2R", W / 2, 800, GREEN, size=24, a=fw(t, C["35.simple"], 1e9), anchor="center", bounds=(0, 1920))
    c.restoreToCount(clip)
    trade(c, t, ch, E2_CF + 1, E2_HIT + 1, T, ev, boxes=False)
    c.restore()


def node(c, x, y, w, h, s, a, col=None, sub=None):
    if a <= 0:
        return
    card(c, x, y + (1 - a) * 16, w, h, a, r=20)
    if col:
        rrect(c, x, y + (1 - a) * 16, 8, h, 4, col, a)
    yy = y + (1 - a) * 16
    if sub:
        text_mid(c, s, x + w / 2, yy + h / 2 - 16, 30, "bold", INK, a)
        text_mid(c, sub, x + w / 2, yy + h / 2 + 22, 22, "medium", GRAY, a)
    else:
        text_mid(c, s, x + w / 2, yy + h / 2, 30, "bold", INK, a)


def b_fluxo(c, t, C, B):
    title_chip(c, "RESUMO", "O FLUXO COMPLETO", t, B["start"] + 0.1, BLUE)
    a1, a2, a3 = ep(t, C["36.s1"], 0.5), ep(t, C["36.s2"], 0.5), ep(t, C["36.s3"], 0.5)
    node(c, 150, 170, 500, 110, "Diário forte", a1, BLUE, "define o viés")
    arrow(c, 660, 225, 700, 225, LIGHT, a2, 4, 12, progress=a2)
    node(c, 710, 170, 500, 110, "Marque PDH e PDL", a2, AMBER, "range do dia anterior")
    arrow(c, 1220, 225, 1260, 225, LIGHT, a3, 4, 12, progress=a3)
    node(c, 1270, 170, 500, 110, "1H toma um lado", a3, AMBER, "máxima ou mínima")
    aq = ep(t, C["37.q"], 0.5)
    arrow(c, W / 2, 300, W / 2, 360, LIGHT, aq, 4, 12, progress=aq)
    node(c, 560, 370, 800, 110, "Fechou de volta no range + CISD?", aq, INK)
    ay = ep(t, C["37.y"], 0.5)
    arrow(c, 700, 490, 520, 560, GREEN, ay, 4, 14, progress=ay)
    pill(c, "SIM", 590, 520, GREEN, size=20, a=ay, anchor="center", bounds=(0, 1920))
    node(c, 160, 570, 640, 150, "REVERSÃO", ay, RED, "stop acima/abaixo do pavio · alvo 2R")
    an = ep(t, C["37.n"], 0.5)
    arrow(c, 1220, 490, 1400, 560, RED, an, 4, 14, progress=an)
    pill(c, "NÃO", 1330, 520, RED, size=20, a=an, anchor="center", bounds=(0, 1920))
    node(c, 1120, 570, 640, 150, "CONTINUAÇÃO", ep(t, C["37.c"], 0.5), GREEN, "FVG/swing · CISD a favor · alvo 2R")
    ak = ep(t, C["38.k"], 0.5)
    pill(c, "SAIBA EM QUAL OPERAÇÃO VOCÊ ESTÁ AUTORIZADO A ESTAR", W / 2, 800, INK, size=26, a=ak, anchor="center")


def b_cta(c, t, C, B):
    like, sub, bell, com, bye = C["39.like"], C["39.sub"], C["39.bell"], C["39.com"], C["39.bye"]
    y = 240
    a = ep(t, like - 0.2, 0.5)
    lx = 300
    card(c, lx, y, 340, 340, a, scale=1 + 0.06 * math.sin(math.pi * prog(t, like + 0.4, 0.5)))
    onl = ep(t, like + 0.5, 0.3)
    icon(c, "", lx + 170, y + 150, 120, mix(INK, BLUE, onl), a)
    text(c, "Curtir", lx + 170, y + 290, 36, "bold", mix(INK, BLUE, onl), a)
    a = ep(t, sub - 0.2, 0.5)
    sx, sw_ = 720, 480
    card(c, sx, y, sw_, 340, a)
    if a > 0:
        done = ep(t, sub + 1.3, 0.3)
        press = math.sin(math.pi * prog(t, sub + 1.1, 0.35))
        bw, bh = 340 * (1 - 0.04 * press), 96 * (1 - 0.04 * press)
        bx, by = sx + sw_ / 2 - bw / 2, y + 130 - bh / 2
        rrect(c, bx, by, bw, bh, 48, mix(RED, "#30363D", done), a, shadow=True)
        text_mid(c, "INSCREVA-SE", bx + bw / 2, by + bh / 2, 34, "extrabold", "#FFFFFF", a * (1 - done))
        text_mid(c, "INSCRITO  ✓", bx + bw / 2, by + bh / 2, 34, "extrabold", INK2, a * done)
        text(c, "no canal", sx + sw_ / 2, y + 290, 36, "bold", INK, a)
        ca = fw(t, sub + 0.2, bell + 0.4)
        mv = ep(t, sub + 0.2, 0.9)
        cursor(c, lerp(sx + sw_ + 140, bx + bw * 0.62, mv), lerp(y + 420, by + bh * 0.55, mv), ca, press)
    a = ep(t, bell - 0.2, 0.5)
    bxx = 1280
    card(c, bxx, y, 340, 340, a)
    if a > 0:
        ring = prog(t, bell + 0.4, 1.4)
        ang = 18 * math.sin(ring * math.pi * 6) * (1 - ring)
        c.save(); c.translate(bxx + 170, y + 90); c.rotate(ang); c.translate(-(bxx + 170), -(y + 90))
        icon(c, "", bxx + 170, y + 150, 120, mix(INK, AMBER, ep(t, bell + 0.4, 0.3)), a)
        c.restore()
        text(c, "Ativar o sininho", bxx + 170, y + 290, 34, "bold", INK, a)
    a = fw(t, com, bye)
    if a > 0:
        yy = 640 + (1 - a) * 20
        card(c, 460, yy, 1000, 130, a, r=36)
        icon(c, "", 550, yy + 65, 56, BLUE, a)
        text_mid(c, "Reversão ou continuação?", 1010, yy + 65, 38, "bold", INK, a)
    ab = ep(t, bye, 0.6)
    if ab > 0:
        text(c, "Bons trades!", W / 2, 760 + (1 - ab) * 20, 72, "black", INK, ab)


BLOCKS = dict(hook=b_hook, mapa=b_mapa, range=b_range, diario=b_diario, niveis=b_niveis, reversao=b_reversao,
              pavio=b_pavio, falha=b_falha, continua=b_continua, ex1=b_ex1, ex2=b_ex2, fluxo=b_fluxo, cta=b_cta)
