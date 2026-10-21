"""Visual do vídeo 001 — Fair Value Gap (estilo claro/minimalista).
Cada bloco é uma função draw(c, t, C, B): t = tempo global (s), C = cues globais ("cena.cue"), B = bloco.
"""
import math
import numpy as np
import skia
from motor import *  # noqa

MARCA = ""  # marca d'água opcional (ex.: "@seucanal")
ARQUIVO_FINAL = "fair_value_gap_PTBR.mp4"

# ======================================================================
# Construção dos candles
# ======================================================================

def K(o, c, h=None, l=None):
    h = max(o, c) + 0.35 if h is None else h
    l = min(o, c) - 0.35 if l is None else l
    return [o, h, l, c]


def walk(seed, p0, p1, n, vol=0.9, wick=0.45, lo=-1e9, hi=1e9):
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
    out[-1][3] = p1 if lo < p1 < hi else out[-1][3]
    return out


def mirror(ks, S=None):
    m = [[100 - o, 100 - l, 100 - h, 100 - c] for o, h, l, c in ks]
    if S is None:
        return m
    S2 = dict(S); S2["dir"] = -S["dir"]
    for k in ("liq_p", "sweep_p", "bos_p", "entry", "sl", "tp", "touch_p", "close_p"):
        if k in S2:
            S2[k] = 100 - S2[k]
    S2["liq_marks"] = [(i, 100 - p) for i, p in S["liq_marks"]]
    i0, a, b = S["fvg"]; S2["fvg"] = (i0, 100 - a, 100 - b)
    return m, S2


def build_ny(seed):
    k = []
    k += walk(seed, 80, 71, 9, vol=1.0)
    k += [K(71, 73.5, h=74.0), K(73.5, 74.6, h=75.5, l=72.9)]
    tp_i0 = len(k) - 1
    k += [K(74.6, 72.0, h=75.0)]
    k += walk(seed + 2, 72, 60, 8, hi=74.5)
    k += walk(seed + 3, 60, 47, 8, hi=61, lo=44)
    k += [K(47, 44.5, l=44.0), K(44.5, 41.2, l=40.0)]; eq1 = len(k) - 1
    k += [K(41.2, 43.4, l=40.6), K(43.4, 45.6), K(45.6, 47.3, h=48.2)]; sh = len(k) - 1
    k += [K(47.3, 45.0, h=47.8), K(45, 42.8), K(42.8, 41.0, l=40.05)]; eq2 = len(k) - 1
    k += [K(41.0, 42.3, l=40.5)]
    sw = len(k); k += [K(42.3, 41.2, h=42.6, l=38.3)]
    d1 = len(k); k += [K(41.2, 44.6, h=45.0, l=40.9), K(44.6, 49.8, h=50.2, l=44.3), K(49.8, 52.4, h=53.0, l=47.4)]
    k += [K(52.4, 51.2, h=53.3, l=50.7), K(51.2, 49.3, l=48.9), K(49.3, 48.1, h=49.6, l=47.3), K(48.1, 47.0, h=48.4, l=46.15)]
    touch = len(k) - 1
    k += [K(47.0, 49.6, l=46.6)]
    k += walk(seed + 4, 49.6, 74.0, 13, vol=0.9, lo=47.5, hi=75.3)
    k += [K(74.0, 75.2, h=75.9, l=73.4)]; hit = len(k) - 1
    k += [K(75.2, 74.4, h=75.6)]
    k += walk(seed + 5, 74.4, 72.5, 3, hi=75.4)
    S = dict(dir=1, liq_p=40.0, liq_i0=eq1, liq_i1=sw + 1, liq_marks=[(eq1, 40.0), (eq2, 40.05)],
             sweep_i=sw, sweep_p=38.3, close_p=41.2, struct_i=sh, bos_p=48.2, bos_i1=d1 + 2, disp=[d1, d1 + 1, d1 + 2],
             fvg=(d1, 45.0, 47.4), touch_i=touch, touch_p=46.15, entry=46.2, sl=37.8, tp=75.5, tp_i0=tp_i0,
             trade_end=hit + 1, hit_i=hit, zone_end=touch)
    return k, S


def build_multi(seed=31):
    k = []
    k += walk(seed, 64, 70, 5, vol=0.7)
    k += [K(70, 71.4, h=72.0, l=69.6)]; tp_i0 = len(k) - 1
    k += walk(seed + 1, 71.4, 52, 10, hi=71.6)
    k += walk(seed + 2, 52, 44, 6, hi=53, lo=41)
    k += [K(44, 46.5), K(46.5, 49.2, h=50.0)]; sh = len(k) - 1
    k += [K(49.2, 46.8, h=49.6), K(46.8, 43.0), K(43.0, 39.6, l=38.0)]; low = len(k) - 1
    k += [K(39.6, 41.5, l=39.2), K(41.5, 40.0, h=42.0, l=39.0)]
    sw = len(k); k += [K(40.0, 38.8, h=40.3, l=36.3)]
    c1 = len(k)
    k += [K(38.8, 40.6, h=41.0, l=38.5), K(40.6, 44.0, h=44.5, l=40.3), K(44.0, 45.0, h=45.6, l=43.5)]
    c4 = len(k)
    k += [K(45.0, 46.6, h=47.2, l=44.6), K(46.6, 52.0, h=52.4, l=46.3), K(52.0, 54.2, h=54.8, l=49.6)]
    k += [K(54.2, 53.0, h=54.9, l=52.6), K(53.0, 51.2, l=50.8), K(51.2, 49.5, l=49.1), K(49.5, 48.9, h=49.9, l=48.35)]
    touch = len(k) - 1
    k += [K(48.9, 51.5, l=48.6)]
    k += walk(seed + 3, 51.5, 70.8, 10, lo=49.5, hi=71.8)
    k += [K(70.8, 72.3, h=72.6, l=70.2)]; hit = len(k) - 1
    k += walk(seed + 4, 72.3, 71.0, 2, hi=72.5)
    S = dict(dir=1, liq_p=38.0, liq_i0=low, liq_i1=sw + 1, liq_marks=[(low, 38.0)],
             sweep_i=sw, sweep_p=36.3, close_p=38.8, struct_i=sh, bos_p=50.0, bos_i1=c4 + 2, disp=[c1, c1 + 1, c1 + 2, c4, c4 + 1, c4 + 2],
             fvg=(c4, 47.2, 49.6), fvg1=(c1, 41.0, 43.5), touch_i=touch, touch_p=48.35, entry=48.4, sl=35.8, tp=72.0,
             tp_i0=tp_i0, trade_end=hit + 1, hit_i=hit, zone_end=touch)
    return k, S


def build_erro1(seed=41):
    k = []
    k += walk(seed, 47, 45.5, 3, vol=0.6, lo=45.0, hi=49)
    k += [K(45.5, 45.0, l=44.5)]; cons_low = len(k) - 1
    k += walk(seed + 1, 45.0, 47.0, 4, vol=0.6, lo=45.2, hi=48.5)
    c1 = len(k)
    k += [K(47, 49.5, h=49.9, l=46.7), K(49.5, 53.2, h=53.6, l=49.3), K(53.2, 55.2, h=55.6, l=51.8)]
    k += [K(55.2, 56.4, h=57.0, l=54.8)]; sh_top = len(k) - 1
    k += [K(56.4, 54.6), K(54.6, 52.9, l=52.5), K(52.9, 52.2, h=53.1, l=51.75)]; touch1 = len(k) - 1
    k += [K(52.2, 50.1, l=49.7), K(50.1, 48.5, l=48.2)]; stop1 = len(k) - 1
    k += [K(48.5, 49.8, h=50.5, l=48.1)]; sh = len(k) - 1
    k += [K(49.8, 47.6, h=50.1), K(47.6, 45.8, l=45.4), K(45.8, 46.4, l=45.2)]
    sw = len(k); k += [K(46.4, 45.1, h=46.7, l=43.7)]
    d1 = len(k); k += [K(45.1, 47.9, h=48.3, l=44.9), K(47.9, 51.8, h=52.2, l=47.6), K(51.8, 53.4, h=53.9, l=49.9)]
    k += [K(53.4, 52.3, l=51.9), K(52.3, 50.8, l=50.4), K(50.8, 50.0, h=51.1, l=49.05)]; touch = len(k) - 1
    k += [K(50.0, 52.4, l=49.6)]
    k += walk(seed + 2, 52.4, 56.4, 4, vol=0.5, lo=50.8, hi=56.9)
    k += [K(56.4, 57.6, h=58.0, l=56.0)]; hit = len(k) - 1
    k += walk(seed + 3, 57.6, 57.0, 2, hi=58.0, vol=0.4)
    W1 = dict(dir=1, fvg=(c1, 49.9, 51.8), touch_i=touch1, touch_p=51.75, entry=51.8, sl=48.8, tp=None,
              trade_end=stop1 + 1, zone_end=touch1, stop_i=stop1, cons=(0, c1 - 1))
    S = dict(dir=1, liq_p=44.5, liq_i0=cons_low, liq_i1=sw + 1, liq_marks=[(cons_low, 44.5)],
             sweep_i=sw, sweep_p=43.7, close_p=45.1, struct_i=sh, bos_p=50.5, bos_i1=d1 + 2, disp=[d1, d1 + 1, d1 + 2],
             fvg=(d1, 48.3, 49.9), touch_i=touch, touch_p=49.05, entry=49.1, sl=43.2, tp=57.0, tp_i0=sh_top,
             trade_end=hit + 1, hit_i=hit, zone_end=touch)
    return k, W1, S


def build_erro2(seed=51):
    k = []
    k += walk(seed, 70, 58, 9, hi=71)
    k += walk(seed + 1, 58, 51, 5, hi=59, lo=49)
    k += [K(51, 49.2, l=48.0)]; low1 = len(k) - 1
    k += [K(49.2, 51.4, l=48.8), K(51.4, 53.0, h=53.5)]; sh1 = len(k) - 1
    k += [K(53, 51.2, h=53.3), K(51.2, 49.6, l=48.9)]
    sw1 = len(k); k += [K(49.6, 48.7, h=50.0, l=46.9)]
    d1 = len(k); k += [K(48.7, 51.6, h=52.0, l=48.4), K(51.6, 55.0, h=55.4, l=51.3), K(55.0, 56.6, h=57.2, l=53.4)]
    top = len(k) - 1
    k += [K(56.6, 55.6, h=57.0, l=55.2), K(55.6, 51.0, h=55.9, l=50.5)]; fail = len(k) - 1
    k += [K(51.0, 49.3, l=48.9), K(49.3, 46.9, l=46.5), K(46.9, 45.3, l=44.8)]; low2 = len(k) - 1
    k += [K(45.3, 46.6, l=45.0), K(46.6, 47.9, h=48.4)]; sh2 = len(k) - 1
    k += [K(47.9, 46.4, h=48.1), K(46.4, 45.6, l=45.2)]
    sw2 = len(k); k += [K(45.6, 45.4, h=46.0, l=43.9)]
    e1 = len(k); k += [K(45.4, 48.0, h=48.5, l=45.1), K(48.0, 51.6, h=52.0, l=47.7), K(51.6, 53.2, h=53.7, l=49.7)]
    k += [K(53.2, 52.1, l=51.7), K(52.1, 50.5, l=50.1), K(50.5, 49.8, h=50.8, l=49.05)]; touch = len(k) - 1
    k += [K(49.8, 52.6, l=49.4)]
    k += walk(seed + 2, 52.6, 56.5, 4, vol=0.5, lo=51, hi=57.0)
    k += [K(56.5, 57.7, h=58.1, l=56.1)]; hit = len(k) - 1
    k += walk(seed + 3, 57.7, 57.0, 2, hi=58.0, vol=0.4)
    F = dict(dir=1, liq_p=48.0, liq_i0=low1, liq_i1=sw1 + 1, liq_marks=[(low1, 48.0)],
             sweep_i=sw1, sweep_p=46.9, close_p=48.7, struct_i=sh1, bos_p=53.5, bos_i1=d1 + 2, disp=[d1, d1 + 1, d1 + 2],
             fvg=(d1, 52.0, 53.4), fail_i=fail, entry=52.7, sl=46.4, zone_end=fail, naive_stop=low2)
    S = dict(dir=1, liq_p=44.8, liq_i0=low2, liq_i1=sw2 + 1, liq_marks=[(low2, 44.8)],
             sweep_i=sw2, sweep_p=43.9, close_p=45.4, struct_i=sh2, bos_p=48.4, bos_i1=e1 + 2, disp=[e1, e1 + 1, e1 + 2],
             fvg=(e1, 48.5, 49.7), touch_i=touch, touch_p=49.05, entry=49.1, sl=43.4, tp=57.2, tp_i0=top,
             trade_end=hit + 1, hit_i=hit, zone_end=touch)
    return k, F, S


# ---------------- dados ----------------
NY_K, NY_S = build_ny(7)
_lk, _ls = build_ny(19)
LDN_K, LDN_S = mirror(_lk, _ls)
MU_K, MU_S = build_multi()
E1_K, E1_W, E1_S = build_erro1()
E2_K, E2_F, E2_S = build_erro2()

HOOK_K = (walk(61, 40, 44, 6, vol=0.6, lo=39, hi=45) +
          [K(44, 46.5, h=46.9, l=43.7), K(46.5, 50.5, h=50.9, l=46.3), K(50.5, 52.2, h=52.7, l=48.6), K(52.2, 53.4, h=53.9)] +
          [K(53.4, 51.6), K(51.6, 49.9, l=49.4), K(49.9, 48.9, h=50.2, l=48.55)] +
          [K(48.9, 46.9, l=46.5), K(46.9, 45.6, l=45.1)] +
          [K(45.6, 47.8, l=45.3), K(47.8, 51.5, h=51.9)] + walk(62, 51.5, 63, 9, lo=50.5, hi=64, vol=0.6))
HOOK = dict(fvg=(6, 46.9, 48.6), touch=13, entry=48.6, sl=45.6, stop=15, n=len(HOOK_K))

ALTA_K = (walk(71, 44, 45, 6, vol=0.5, lo=43, hi=46.5) +
          [K(45, 46.8, h=47.2, l=44.6), K(46.8, 51.5, h=51.9, l=46.6), K(51.5, 53.2, h=53.6, l=49.4)] +
          [K(53.2, 54.4, h=54.9), K(54.4, 53.1), K(53.1, 51.2), K(51.2, 49.6, h=51.4, l=48.4), K(49.6, 52.5, l=49.2), K(52.5, 55.0)])
ALTA = dict(fvg=(6, 47.2, 49.4), touch=13)
BAIXA_K = mirror(walk(72, 44, 45, 6, vol=0.5, lo=43, hi=46.5) + ALTA_K[6:])

DEF_K = [K(43, 44.2), K(44.2, 43.6), K(43.6, 44.8),
         K(44.8, 46.4, h=47.0, l=44.3), K(46.4, 53.2, h=53.6, l=46.1), K(53.2, 55.0, h=55.6, l=49.6),
         K(55, 56.2, h=56.7), K(56.2, 54.4), K(54.4, 52.2), K(52.2, 50.0, h=52.4, l=48.6), K(50, 53.5, l=49.7), K(53.5, 57, h=57.4)]

CE_K = [K(40, 42.6), K(42.6, 41.2), K(41.2, 40.2), K(40.2, 41.0, l=38.9),
        K(41, 43.0, h=43.5, l=40.6), K(43, 49.5, h=50, l=42.8), K(49.5, 51.5, h=52.4, l=46.5), K(51.5, 53.6, h=54.2, l=51.1)]

FAL_K = [K(42, 43.5), K(43.5, 42.8), K(42.8, 44),
         K(44, 45.8, h=46.2, l=43.6), K(45.8, 50.5, h=50.9, l=45.6), K(50.5, 51.8, h=52.4, l=48.6),
         K(51.8, 51.0, h=52.6, l=50.6), K(51.0, 45.2, h=51.4, l=44.7), K(45.2, 44.1, h=46.0, l=43.4), K(44.1, 42.5, h=44.6)]

_fk, _fs = build_ny(23)
_c0 = _fs["liq_i0"] - 7
FIL_K = _fk[_c0:_fs["disp"][2] + 3]
FIL_S = {k: (v - _c0 if isinstance(v, int) and k.endswith(("_i", "_i0", "_i1")) else v) for k, v in _fs.items()}
FIL_S["disp"] = [d - _c0 for d in _fs["disp"]]
FIL_S["fvg"] = (_fs["fvg"][0] - _c0, _fs["fvg"][1], _fs["fvg"][2])
FIL_S["liq_marks"] = [(i - _c0, p) for i, p in _fs["liq_marks"]]

# ======================================================================
# Utilidades de cena
# ======================================================================
CARD_R = (140, 150, 1640, 690)
CH_R = (210, 205, 1270, 580)
XLAB = CH_R[0] + CH_R[2] + 18


def chart_card(c, a=1.0, rect=CARD_R):
    card(c, *rect, a=a)


def reveal(t, sched):
    """sched = [(t, count, dur), ...] -> nº de candles visíveis (float)"""
    n = sched[0][1]
    for tt, cnt, d in sched[1:]:
        if t >= tt:
            n = lerp(n, cnt, ease_io(prog(t, tt, d)) if d > 0 else 1.0)
    return n


def camera(t, keys):
    """keys = [(t, (v0, v1, pmin, pmax), dur), ...] -> vista interpolada"""
    v = keys[0][1]
    for tt, tgt, d in keys[1:]:
        if t >= tt:
            f = ease_io(prog(t, tt, d)) if d > 0 else 1.0
            v = tuple(lerp(a, b, f) for a, b in zip(v, tgt))
    return v


def fade_win(t, t_in, t_out=1e9, d_in=0.45, d_out=0.4):
    return ep(t, t_in, d_in) * (1 - prog(t, t_out, d_out))


def clip_card(c, rect=CARD_R):
    x, y, w, h = rect
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), True)


def kz_band(c, ch, i0, i1, a, label):
    if a <= 0:
        return
    x0, x1 = ch.xl(i0) - 10, ch.xr(i1) + 10
    rrect(c, x0, ch.y0 - 30, x1 - x0, ch.h + 34, 10, BLUE, a * 0.08)
    pill(c, label, (x0 + x1) / 2, ch.y0 + ch.h + 4, BLUE, size=22, a=a, anchor="center")


# ======================================================================
# História de operação (varrida -> deslocamento -> BOS -> FVG -> entrada -> alvo)
# ======================================================================

def story(c, t, ch, S, E, L, nvis, fade=1.0, cfn=None, afn=None, draw_candles=True, parts=("under", "candles", "over")):
    """E = eventos -> tempo. L = textos. Desenha camadas na ordem certa."""
    d = S["dir"]
    g = lambda k: E.get(k, 1e9)
    Y = lambda p, off=0: ch.y(p) + off * d
    right = ch.rx + ch.w
    ti = S.get("touch_i"); te = S.get("trade_end")
    i0, pa, pb = S["fvg"]
    ptop, pbot = (max(pa, pb), min(pa, pb))
    pmid = (pa + pb) / 2
    fv = fade if "under" in parts else 0.0

    # kill zone
    if "kz" in E:
        kz_band(c, ch, S["sweep_i"] - 3, S["hit_i"] + 1, ep(t, g("kz"), 0.6) * fv, L.get("kz", ""))

    # caixas da operação
    if ti is not None:
        xa, xb = ch.xl(ti), min(ch.xr(te), right)
        a = ep(t, g("sl"), 0.5) * fv
        if a > 0:
            ya, yb = sorted((ch.y(S["entry"]), ch.y(S["sl"])))
            col = RED
            boost = 0.0
            if "slhit" in E:
                boost = 0.25 * ep(t, g("slhit"), 0.3)
            c.drawRect(skia.Rect.MakeLTRB(xa, ya, lerp(xa, xb, a), yb), paint(col, 0.13 * a + boost * fv))
        a = ep(t, g("tp"), 0.5) * fv
        if a > 0 and S.get("tp") is not None:
            ya, yb = sorted((ch.y(S["entry"]), ch.y(S["tp"])))
            boost = 0.12 * ep(t, g("hit"), 0.4)
            c.drawRect(skia.Rect.MakeLTRB(xa, ya, lerp(xa, xb, a), yb), paint(GREEN, 0.12 * a + boost * fv))

    # FVG
    a = ep(t, g("fvg"), 0.7) * fv
    zone_col = AMBER
    if "fail" in E:
        zone_col = mix(AMBER, RED, ep(t, g("fail"), 0.4))
    if a > 0:
        ch.zone(c, i0, ch.n - 1, pa, pb, zone_col, a=a, progress=ep(t, g("fvg"), 0.9),
                ext=right - ch.xr(ch.n - 1))
    # liquidez
    if "liq" in E:
        a = ep(t, g("liq"), 0.6) * fv
        ch.level(c, S["liq_i0"], S["liq_i1"], S["liq_p"], AMBER, a, progress=a, width=3)
    # BOS
    a = ep(t, g("bos"), 0.6) * fv
    if a > 0:
        ch.level(c, S["struct_i"], S["bos_i1"], S["bos_p"], INK2, a, progress=a, width=2.5)
    # alvo (liquidez acima/abaixo)
    a = ep(t, g("tp"), 0.6) * fv
    if a > 0 and S.get("tp") is not None:
        ch.level(c, S["tp_i0"], te, S["tp"], AMBER, a, progress=a, width=3)
    # CE
    a = ep(t, g("ce"), 0.5) * fv
    if a > 0:
        hline(c, ch.xl(i0), right, ch.y(pmid), GREEN, a, 2.5, (12, 8), progress=a)

    # candles
    if draw_candles and "candles" in parts:
        ch.draw(c, nvis, color_fn=cfn, alpha_fn=afn)

    fv = fade if "over" in parts else 0.0
    # destaques de pavio
    if "w1" in E:
        ch.wick_glow(c, i0, "h" if d == 1 else "l", BLUE, fade_win(t, g("w1"), g("w1") + 5.0) * fv)
        ch.wick_glow(c, i0 + 2, "l" if d == 1 else "h", BLUE, fade_win(t, g("w3"), g("w1") + 5.0) * fv)

    # medição (colchete)
    if "m" in E:
        a = fade_win(t, g("m"), g("m") + 4.5) * fv
        if a > 0:
            x = right - 30
            y1, y2 = ch.y(ptop), ch.y(pbot)
            line(c, x, y1, x, lerp(y1, y2, ep(t, g("m"), 0.6)), INK, a, 3)
            line(c, x - 10, y1, x + 10, y1, INK, a, 3); line(c, x - 10, y2, x + 10, y2, INK, a * ep(t, g("m") + 0.5, 0.2), 3)

    # anéis
    if "sw" in E:
        a = fade_win(t, g("sw") + 0.4, g("sw") + 6) * fv
        ch.ring(c, S["sweep_i"], S["sweep_p"], RED, a, 18)
    if ti is not None and "tc" in E:
        a = fade_win(t, g("tc"), g("tc") + 4) * fv
        ch.ring(c, ti, S["touch_p"], GREEN if S.get("tp") else INK, a, 18)

    # deslocamento numerado
    for n, (ev, idx) in enumerate(zip(("d1", "d2", "d3", "d4", "d5", "d6"), S.get("disp", []))):
        if ev in E:
            a = fade_win(t, g(ev), g("bos") + 2.5, 0.35) * fv
            o, h, l, cl = ch.k[idx]
            badge_num(c, n + 1, ch.x(idx) + ch.bw / 2 + 24, ch.y((o + cl) / 2), a, 17)

    # ---------- etiquetas ----------
    if "liq" in E:
        a = fade_win(t, g("liq") + 0.3, g("liqout")) * fv
        if L.get("liq_below"):
            pill(c, L["liq"], ch.xl(S["liq_i0"]), Y(S["liq_p"], 32), AMBER, size=22, a=a)
        else:
            pill(c, L["liq"], ch.xl(S["liq_i0"]) - 16, ch.y(S["liq_p"]), AMBER, size=22, a=a, anchor="right")
    if "sw" in E:
        a = fade_win(t, g("lab"), g("lab") + 9) * fv
        pill(c, L.get("sweep", "LIQUIDEZ VARRIDA"), ch.x(S["sweep_i"]), Y(S["sweep_p"], 44), RED, size=22, a=a, anchor="center")
    if "cl" in E:
        a = fade_win(t, g("cl"), g("cl") + 5) * fv
        pill(c, L.get("close", "FECHOU DE VOLTA"), ch.x(S["sweep_i"]), Y(S["sweep_p"], 92), INK, size=20, a=a, anchor="center")
    if "bos" in E:
        a = fade_win(t, g("bos") + 0.3, g("bos") + 9) * fv
        pill(c, L.get("bos", "QUEBRA DE ESTRUTURA"), ch.x(S["struct_i"]), Y(S["bos_p"], -34), INK2, size=22, a=a, anchor="center")
    yz = ch.y(pmid)
    a_f = fade_win(t, g("fvg") + 0.4, min(g("ce"), g("lg"))) * fv
    pill(c, L.get("fvg", "FVG"), XLAB, yz, AMBER, size=24, a=a_f)
    a_ce = fade_win(t, g("ce"), g("en") if "en" in E else g("lg")) * fv
    pill(c, "CE 50%", XLAB, yz, GREEN, size=24, a=a_ce)
    a_en = fade_win(t, g("en") if "en" in E else g("lg"), 1e9) * fv
    if a_en > 0 and S.get("entry") is not None:
        pill(c, L.get("entry", "ENTRADA"), XLAB, ch.y(S["entry"]), INK, size=24, a=a_en)
    if ti is not None:
        a = fade_win(t, g("lg"), 1e9) * fv
        lg_txt = L.get("lg", "COMPRA" if d == 1 else "VENDA")
        pill(c, lg_txt, ch.x(ti), Y(S["touch_p"], 46), GREEN if d == 1 else RED, size=23, a=a, anchor="center")
        a = fade_win(t, g("sl"), g("slhit")) * fv
        pill(c, "STOP", XLAB, ch.y(S["sl"]), RED, size=24, a=a)
        if "slhit" in E:
            a = ep(t, g("slhit"), 0.4) * fv
            pill(c, "STOP ATINGIDO", XLAB, ch.y(S["sl"]), RED, size=24, a=a)
        if S.get("tp") is not None:
            a = fade_win(t, g("tp"), g("hit")) * fv
            pill(c, "ALVO", XLAB, ch.y(S["tp"]), GREEN, size=24, a=a)
            a = fade_win(t, g("tp") + 0.3, 1e9) * fv
            pill(c, L.get("tp", "LIQUIDEZ ACIMA DA MÁXIMA"), ch.xl(S["tp_i0"]), Y(S["tp"], -30), AMBER, size=22, a=a)
            a = ep(t, g("hit"), 0.45) * fv
            if a > 0:
                rr = abs(S["tp"] - S["entry"]) / abs(S["entry"] - S["sl"])
                pill(c, f"+{rr:.1f}R".replace(".", ","), XLAB, ch.y(S["tp"]), GREEN, size=26, a=a)
                pill(c, "ALVO ATINGIDO", (ch.xl(ti) + ch.xr(te)) / 2, Y(S["tp"], -44), GREEN, size=25, a=a, anchor="center")


def story_events(C, sid, mapping):
    """mapping: nome_evento -> 'cue' (na cena sid) ou 'outra.cue'."""
    E = {}
    for ev, cue in mapping.items():
        key = cue if "." in cue else f"{sid}.{cue}"
        v = C[key]
        if v < 1e8:
            E[ev] = v
    return E


# ======================================================================
# BLOCOS
# ======================================================================

def b_hook(c, t, C, B):
    title_chip(c, "NINGUÉM TE CONTA ISSO", "SOBRE FAIR VALUE GAPS", t, B["start"] + 0.1, AMBER)
    chart_card(c)
    ch = Chart(HOOK_K, (260, 205, 1180, 590), max_body=40)
    a, b = C["01.a"], C["01.b"]
    n = reveal(t, [(0, 9, 0), (B["start"], 9, 0), (B["start"] + 0.3, 11, 1.2), (a, 14, 1.4), (b, 16, 1.0), (b + 1.6, HOOK["n"], 3.2)])
    i0, p0, p1 = HOOK["fvg"]
    ch.zone(c, i0, HOOK["n"] - 1, p0, p1, AMBER, ep(t, B["start"] + 0.9, 0.6), progress=ep(t, B["start"] + 0.9, 1.0))
    xa, xb = ch.xl(HOOK["touch"]), ch.xr(HOOK["stop"] + 1)
    sa = ep(t, a + 1.0, 0.5)
    if sa > 0:
        c.drawRect(skia.Rect.MakeLTRB(xa, ch.y(HOOK["entry"]), lerp(xa, xb, sa), ch.y(HOOK["sl"])), paint(RED, 0.13 * sa + 0.2 * ep(t, b + 0.9, 0.3)))
    ch.draw(c, n)
    pill(c, "ENTRADA NO TOQUE", ch.xl(HOOK["touch"]) - 16, ch.y(HOOK["entry"]), INK, size=23, a=ep(t, a + 1.2, 0.4), anchor="right")
    pill(c, "STOP", ch.xr(HOOK["stop"] + 1) + 14, ch.y(HOOK["sl"]), RED, size=23, a=ep(t, b + 0.9, 0.4))
    aa = ep(t, b + 3.0, 0.6)
    arrow(c, ch.x(HOOK["stop"] + 3), ch.y(47), ch.x(HOOK["n"] - 2), ch.y(61), GREEN, aa, 5, 20, progress=ep(t, b + 3.0, 1.2))
    pill(c, "O MOVIMENTO VEIO DEPOIS", ch.x(HOOK["n"] - 7), ch.y(63.5), GREEN, size=23, a=ep(t, b + 3.8, 0.5), anchor="center")


def target_icon(c, cx, cy, r, a):
    for k, col in ((1.0, RED), (0.68, "#FFFFFF"), (0.4, RED)):
        c.drawCircle(cx, cy, r * k, paint(col, a))


def b_promessa(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    text(c, "AO FINAL DESTE VÍDEO, VOCÊ VAI SABER:", W / 2, 230, 34, "extrabold", INK, a0, tracking=1)
    items = [("Quais FVGs", "operar", "check", C["02.a"]), ("Exatamente", "onde entrar", "target", C["02.b"]),
             ("Quais deles", "ignorar", "x", C["02.c"])]
    cw, chh, gap = 440, 380, 60
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (l1, l2, ic, tc) in enumerate(items):
        a = ep(t, tc, 0.55)
        if a <= 0:
            continue
        x = x0 + k * (cw + gap); y = 300 + (1 - a) * 40
        card(c, x, y, cw, chh, a)
        cx, cy = x + cw / 2, y + 130
        if ic == "check":
            check_icon(c, cx, cy, 58, a, GREEN)
        elif ic == "x":
            check_icon(c, cx, cy, 58, a, RED, "x")
        else:
            s = 0.5 + 0.5 * ease_back(a)
            target_icon(c, cx, cy, 58 * s, a)
        text(c, l1, cx, y + 260, 34, "medium", GRAY, a)
        text(c, l2, cx, y + 312, 44, "extrabold", INK, a)


def b_definicao(c, t, C, B):
    # cenas 03, 04, 05, 06
    s3, s5, s6 = C["03"], C["05"], C["06"]
    title_chip(c, "FAIR VALUE GAP", "(FVG)", t, C["03.a"] - 0.2, AMBER, t_out=s5 - 0.2)
    title_chip(c, "AS CORES", "NÃO IMPORTAM", t, s5, RED, t_out=s6 - 0.2)
    title_chip(c, "POR QUE ISSO", "É IMPORTANTE?", t, s6, BLUE)
    chart_card(c)
    # câmera: começa centrada nos 6 primeiros, depois abre para todos
    pan = ep(t, C["06.b"] - 0.2, 1.6)
    v0, v1 = lerp(-2.5, -0.5, pan), lerp(8.5, 12.5, pan)
    rect = (300, 215, 1150, 560)
    ch = Chart(DEF_K, rect, pmin=40.5, pmax=59, max_body=78)
    ch.step = rect[2] / (v1 - v0)
    ch.bw = min(ch.step * 0.56, 78)
    ch.x0 = rect[0] - v0 * ch.step
    ch.n = len(DEF_K)
    n = reveal(t, [(0, 3, 0), (C["03.a"] - 0.3, 6, 1.4), (C["06.b"], 12, 4.0)])
    clip_card(c)
    # cores neutras na cena 5
    col_t = ep(t, C["05.col"], 0.5) * (1 - ep(t, s6 - 0.3, 0.5))
    alt = {3: RED, 4: GREEN, 5: RED}
    cfn = (lambda i: mix(GREEN if DEF_K[i][3] >= DEF_K[i][0] else RED, alt[i], col_t) if i in alt else
           (GREEN if DEF_K[i][3] >= DEF_K[i][0] else RED))
    afn = lambda i: 1.0 if i in (3, 4, 5) or t < C["03.c1"] or t > s6 else 0.35 + 0.65 * (1 - ep(t, C["03.c1"], 0.5))
    zone_a = ep(t, C["04.gap"], 0.6)
    right = rect[0] + rect[2]
    ch.zone(c, 3, 3, 47.0, 49.6, AMBER, zone_a, progress=zone_a, ext=lerp(ch.xr(5), right, 1.0) - ch.xr(3))
    ch.draw(c, n, color_fn=cfn, alpha_fn=afn)
    w_t = fade_win(t, C["04.w1"], C["04.gap"] + 1.5)
    w_t2 = fade_win(t, C["05.wk"], C["06"] - 0.3)
    ch.wick_glow(c, 3, "h", BLUE, max(w_t, w_t2))
    ch.wick_glow(c, 5, "l", BLUE, max(fade_win(t, C["04.w3"], C["04.gap"] + 1.5), w_t2))
    for k, (i, cue) in enumerate(((3, "03.c1"), (4, "03.c2"), (5, "03.c3"))):
        a = fade_win(t, C[cue], s6 + 0.5)
        badge_num(c, k + 1, ch.x(i), ch.y(DEF_K[i][1]) - 44, a, 22)
    c.restore()
    # etiquetas
    ya = ch.y(48.3)
    pill(c, "FVG", ch.xr(5) + 34, ya, AMBER, size=26, a=ep(t, C["04.gap"] + 0.4, 0.4) * (1 - ep(t, s6 - 0.2, 0.4)))
    pill(c, "LACUNA DE VALOR JUSTO", ch.xr(5) + 120, ya, INK, size=24, a=fade_win(t, C["04.pt"], s5))
    pill(c, "PAVIO DO CANDLE 1", ch.xl(3) - 16, ch.y(DEF_K[3][1]), BLUE, size=22, a=fade_win(t, C["04.w1"] + 0.2, C["04.gap"] + 1.5), anchor="right")
    pill(c, "PAVIO DO CANDLE 3", ch.xr(5) + 16, ch.y(DEF_K[5][2]) + 6, BLUE, size=22, a=fade_win(t, C["04.w3"] + 0.2, C["04.gap"] + 0.3))
    pill(c, "SÓ OS PAVIOS IMPORTAM", ch.xr(5) + 34, ch.y(52), BLUE, size=24, a=fade_win(t, C["05.wk"], s6 - 0.3))
    # cena 6
    a = fade_win(t, C["06.a"], C["06.b"] + 0.5)
    o, h, l, cl = DEF_K[4]
    arrow(c, ch.xl(4) - 30, ch.y(o), ch.xl(4) - 30, ch.y(cl), INK, a, 5, 18, progress=ep(t, C["06.a"], 0.9))
    pill(c, "UMA SÓ DIREÇÃO", ch.xl(4) - 50, ch.y((o + cl) / 2), INK, size=23, a=a, anchor="right")
    pill(c, "PREÇO VOLTA PARA REEQUILIBRAR", ch.x(9), ch.y(48.6) + 52, BLUE, size=23,
         a=fade_win(t, C["06.b"] + 2.6, C["06.c"] + 0.2), anchor="center")
    pill(c, "ÁREA DE ENTRADA", ch.x(9), ch.y(48.6) + 52, GREEN, size=24, a=ep(t, C["06.c"] + 0.2, 0.4), anchor="center")
    ch.ring(c, 9, 48.6, GREEN, fade_win(t, C["06.b"] + 2.8, 1e9), 20)


def _simple_dir(c, t, C, B, ks, sid, label2, col2, bear=False):
    title_chip(c, "FVG", label2, t, B["start"] + 0.1, col2)
    chart_card(c)
    ch = Chart(ks, (330, 230, 1100, 540), max_body=50)
    a, b = C[f"{sid}.a"], C[f"{sid}.b"]
    n = reveal(t, [(0, 6, 0), (B["start"] + 0.2, 6, 0), (a - 0.4, 10, 1.6), (b, len(ks), 2.4)])
    i0, p0, p1 = ALTA["fvg"]
    if bear:
        p0, p1 = 100 - p0, 100 - p1
    za = ep(t, a + 0.9, 0.6)
    ch.zone(c, i0, len(ks) - 1, p0, p1, AMBER, za, progress=za)
    ch.draw(c, n)
    zmid = ch.y((p0 + p1) / 2)
    pill(c, "GAP ABAIXO" if not bear else "GAP ACIMA", ch.xr(len(ks) - 1) + 20, zmid, AMBER, size=24, a=ep(t, a + 1.3, 0.4))
    tch = ALTA["touch"]
    pp = ks[tch][2] if not bear else ks[tch][1]
    ch.ring(c, tch, pp, GREEN if not bear else RED, ep(t, b + 1.6, 0.4), 20)
    pill(c, "O PREÇO VOLTA AO GAP", ch.x(tch), ch.y(pp) + (56 if not bear else -56), INK, size=23, a=ep(t, b + 1.9, 0.4), anchor="center")


def b_alta(c, t, C, B):
    _simple_dir(c, t, C, B, ALTA_K, "07", "DE ALTA", GREEN)


def b_baixa(c, t, C, B):
    _simple_dir(c, t, C, B, BAIXA_K, "08", "DE BAIXA", RED, bear=True)


def b_filtro(c, t, C, B):
    title_chip(c, "NEM TODO FVG", "VALE A PENA", t, C["09.t"] - 0.3, AMBER)
    # cartão do checklist (esquerda)
    lc = (140, 150, 520, 690)
    rc = (700, 150, 1080, 690)
    a_l = ep(t, C["09"] + 3.5, 0.6)
    card(c, *lc, a=a_l)
    text(c, "OPERE SÓ DEPOIS DE:", lc[0] + 50, lc[1] + 90, 26, "extrabold", AMBER, a_l, align="left", tracking=0.6)
    items = [("Varrida de liquidez", "10.s"), ("Deslocamento", "11.d"), ("Quebra de estrutura", "12.b")]
    for k, (s, cue) in enumerate(items):
        a = ep(t, C[cue], 0.5) * a_l
        y = lc[1] + 190 + k * 110
        badge_num(c, k + 1, lc[0] + 78, y, a, 26, bg=INK)
        text(c, s, lc[0] + 128, y + 12, 32, "semibold", INK, a, align="left")
        check_icon(c, lc[0] + 460, y, 18, ep(t, C[cue] + 1.0, 0.4) if True else 0, GREEN)
    a_ok = ep(t, C["12.ok"], 0.5) * a_l
    if a_ok > 0:
        rrect(c, lc[0] + 40, lc[1] + 545, lc[2] - 80, 92, 18, GREEN, a_ok * 0.12)
        text_mid(c, "Esse é o FVG", lc[0] + lc[2] / 2, lc[1] + 574, 26, "semibold", GREEN, a_ok)
        text_mid(c, "que você opera", lc[0] + lc[2] / 2, lc[1] + 610, 26, "extrabold", GREEN, a_ok)
    # gráfico (direita)
    a_r = ep(t, C["09"] + 0.2, 0.6)
    card(c, *rc, a=a_r)
    ch = Chart(FIL_K, (rc[0] + 210, rc[1] + 90, rc[2] - 300, rc[3] - 170), max_body=36)
    S = FIL_S
    sw = S["sweep_i"]
    n = reveal(t, [(0, sw, 0), (C["10.s"] + 0.6, sw + 1, 1.0), (C["11.d"], sw + 4, 2.2), (C["12.f"], len(FIL_K), 1.0)])
    if a_r <= 0:
        return
    c.saveLayerAlpha(None, int(a_r * 255))
    i0, p0, p1 = S["fvg"]
    za = ep(t, C["12.f"], 0.6)
    ch.zone(c, i0, len(FIL_K) - 1, p0, p1, AMBER, za, progress=za, ext=30)
    la = ep(t, C["10.s"], 0.6)
    ch.level(c, S["liq_i0"], sw + 1, S["liq_p"], AMBER, la, progress=la, width=3)
    ba = ep(t, C["12.b"], 0.6)
    ch.level(c, S["struct_i"], S["bos_i1"], S["bos_p"], INK2, ba, progress=ba)
    ch.draw(c, n)
    ch.ring(c, sw, S["sweep_p"], RED, ep(t, C["10.s"] + 1.4, 0.4), 16)
    pill(c, "VARRIDA", ch.x(sw), ch.y(S["sweep_p"]) + 40, RED, size=22, a=ep(t, C["10.s"] + 1.5, 0.4), anchor="center")
    for k, idx in enumerate(S["disp"]):
        o, h, l, cl = FIL_K[idx]
        badge_num(c, k + 1, ch.x(idx) + ch.bw / 2 + 20, ch.y((o + cl) / 2), ep(t, C["11.d"] + 0.5 + k * 0.6, 0.35), 15)
    pill(c, "QUEBRA DE ESTRUTURA", ch.x(S["struct_i"]), ch.y(S["bos_p"]) - 32, INK2, size=21, a=ep(t, C["12.b"] + 0.3, 0.4), anchor="center")
    pill(c, "FVG", ch.xr(len(FIL_K) - 1) + 40, ch.y((p0 + p1) / 2), AMBER, size=23, a=ep(t, C["12.f"] + 0.4, 0.4))
    check_icon(c, ch.xr(len(FIL_K) - 1) + 120, ch.y((p0 + p1) / 2), 18, ep(t, C["12.ok"], 0.4), GREEN)
    c.restore()


def b_ce(c, t, C, B):
    title_chip(c, "CONSEQUENT", "ENCROACHMENT (CE)", t, C["13.ce"] - 0.3, GREEN)
    chart_card(c)
    ch = Chart(CE_K, (300, 215, 700, 560), pmin=37.5, pmax=56, max_body=66)
    n = reveal(t, [(0, 8, 0)])
    p_bot, p_top = 43.5, 46.5
    mid = (p_bot + p_top) / 2
    right = 1330
    za = ep(t, B["start"] + 0.2, 0.7)
    ch.zone(c, 4, 7, p_bot, p_top, AMBER, za, progress=za, ext=right - ch.xr(7))
    ch.draw(c, n)
    a = ep(t, C["13.ce"], 0.6)
    hline(c, ch.xl(4), right, ch.y(mid), GREEN, a, 3, (14, 9), progress=a)
    # linhas de borda
    at = ep(t, C["14.top"], 0.5); ab = ep(t, C["14.bot"], 0.5)
    hline(c, ch.xl(4), right, ch.y(p_top), RED, at, 3, progress=at)
    hline(c, ch.xl(4), right, ch.y(p_bot), AMBER, ab, 3, progress=ab)
    xl = right + 16
    dim = lambda t0: 1 - 0.55 * ep(t, C["14.mid"], 0.5) if t0 else 1
    pill(c, "CEDO DEMAIS", xl, ch.y(p_top) - 26, RED, size=23, a=at * dim(1))
    pill(c, "CE 50%", xl, ch.y(mid), GREEN, size=25, a=a)
    pill(c, "MUITAS VEZES NÃO CHEGA", xl, ch.y(p_bot) + 26, AMBER, size=23, a=ab * dim(1))
    pill(c, "50%", ch.xl(4) - 16, ch.y(mid), INK, size=23, a=ep(t, C["13.pct"], 0.4), anchor="right")
    am = ep(t, C["14.mid"], 0.5)
    check_icon(c, xl - 26, ch.y(mid), 16, am, GREEN)
    pill(c, "EQUILÍBRIO", xl + 138, ch.y(mid), INK, size=23, a=am)


def b_falha(c, t, C, B):
    title_chip(c, "O GAP", "FALHOU", t, C["15.f"] - 0.2, RED)
    chart_card(c)
    ch = Chart(FAL_K, (380, 215, 900, 560), pmin=40, pmax=55, max_body=60)
    st = B["start"]
    n = reveal(t, [(0, 6, 0), (st + 2.0, 7, 0.8), (st + 3.2, 8, 1.4), (C["15.i"] + 0.5, 10, 1.5)])
    p0, p1 = 46.2, 48.6
    right = 1520
    fa = ep(t, C["15.f"], 0.5)
    za = ep(t, st + 0.3, 0.6)
    ch.zone(c, 3, 9, p0, p1, mix(AMBER, RED, fa), za, progress=za, ext=right - ch.xr(9))
    ch.draw(c, n)
    # corpo que fechou através
    i = 7
    o, h, l, cl = FAL_K[i]
    ab = ep(t, st + 4.6, 0.5)
    if ab > 0:
        rrect(c, ch.xl(i) - 8, ch.y(o) - 8, ch.bw + 16, ch.y(cl) - ch.y(o) + 16, 10, RED, 0, stroke=None)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(ch.xl(i) - 8, ch.y(o) - 8, ch.xr(i) + 8, ch.y(cl) + 8), 10, 10),
                    paint(INK, ab, stroke=3))
    pill(c, "CORPO FECHOU ABAIXO DO GAP", ch.xr(i) + 24, ch.y(cl), INK, size=23, a=ab)
    pill(c, "FVG", right + 14, ch.y((p0 + p1) / 2), AMBER, size=24, a=za * (1 - fa))
    pill(c, "FALHOU", right + 14, ch.y((p0 + p1) / 2), RED, size=24, a=fa * (1 - ep(t, C["15.i"], 0.4)))
    pill(c, "IFVG", right + 14, ch.y((p0 + p1) / 2), RED, size=24, a=ep(t, C["15.i"], 0.4))
    ai = ep(t, C["15.i"] + 0.4, 0.5)
    if ai > 0:
        text(c, "Inversion Fair Value Gap", W / 2, 765, 30, "extrabold", RED, ai)
        text(c, "o gap inverte de função", W / 2, 805, 26, "medium", GRAY, ai)


# ---------------- exemplos completos ----------------

def b_ny(c, t, C, B):
    S = NY_S
    title_chip(c, "SESSÃO DE NOVA YORK", "9:30 · HORÁRIO DE NY", t, C["16.s"] - 0.2, BLUE)
    chart_card(c)
    ch = Chart(NY_K, CH_R, pad_lo=0.16, pad_hi=0.08)
    sw, d1 = S["sweep_i"], S["disp"][0]
    ch.view(*camera(t, [(0, ch.full_view(), 0), (C["17.eq"] - 1.0, (sw - 13, sw + 15, 33.0, 57.5), 1.8),
                        (C["22.tp"] - 0.3, (5, len(NY_K) + 0.5, 33.0, 78.5), 1.8)]))
    n = reveal(t, [(0, 10, 0), (B["start"] + 0.3, 14, 2.0), (C["16.dn"], sw - 4, 2.6), (C["17.eq"] - 0.5, sw, 1.2),
                   (C["18.sw"], sw + 1, 1.3), (C["19.d1"] - 0.1, d1 + 1, 0.5), (C["19.d2"] - 0.1, d1 + 2, 0.5),
                   (C["19.d3"] - 0.1, d1 + 3, 0.5), (C["22.pb"], S["touch_i"], 2.6), (C["22.tc"] - 0.2, S["touch_i"] + 1, 0.5),
                   (C["23.run"] + 0.6, S["hit_i"] + 1, C["23.hit"] - C["23.run"] - 0.6), (C["23.hit"] + 0.6, len(NY_K), 1.0)])
    E = story_events(C, "", {"liq": "17.eq", "sw": "18.sw", "lab": "18.lab", "cl": "18.cl", "d1": "19.d1", "d2": "19.d2",
                              "d3": "19.d3", "bos": "19.bos", "fvg": "20.fvg", "w1": "20.w1", "w3": "20.w3", "m": "21.m",
                              "ce": "21.ce", "en": "21.en", "tc": "22.tc", "lg": "22.lg", "sl": "22.sl", "tp": "22.tp",
                              "hit": "23.hit", "kz": "25.kz"})
    L = dict(liq="LIQUIDEZ VENDEDORA (SSL)", tp="LIQUIDEZ COMPRADORA (BSL)", close="FECHOU DE VOLTA ACIMA",
             kz="KILL ZONE DE NOVA YORK · 7h–10h")
    clip_card(c)
    story(c, t, ch, S, E, L, n)
    c.restore()
    # mínimas iguais
    a = fade_win(t, C["17.eq"], C["18.lab"])
    for i, p in S["liq_marks"]:
        ch.ring(c, i, p, AMBER, a, 15)
    # distância até o stop
    a = fade_win(t, C["24.st"], C["25.kz"])
    if a > 0:
        lowest = min(k[2] for k in NY_K[S["touch_i"]:S["hit_i"] + 1])
        x = ch.x(S["touch_i"] + 3)
        line(c, x, ch.y(lowest) + 6, x, ch.y(S["sl"]) - 6, RED, a, 3, dash=(6, 6))
        pill(c, "LONGE DO STOP", x + 16, (ch.y(lowest) + ch.y(S["sl"])) / 2, RED, size=22, a=a)


def b_resumo(c, t, C, B):
    steps = [("Varrida", "26.s1", RED), ("Deslocamento", "26.s2", INK), ("Quebra de\nestrutura", "26.s3", INK),
             ("Fair Value\nGap", "26.s4", AMBER), ("Entrada\nno meio", "26.s5", GREEN)]
    cw, chh, gap = 300, 330, 44
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    y0 = 300
    text(c, "OS 5 PASSOS", W / 2, 220, 40, "extrabold", INK, ep(t, B["start"], 0.5), tracking=1)
    for k, (s, cue, col) in enumerate(steps):
        a = ep(t, C[cue] - 0.1, 0.5)
        x = x0 + k * (cw + gap)
        if k > 0:
            arrow(c, x - gap + 10, y0 + chh / 2, x - 10, y0 + chh / 2, LIGHT, a, 4, 12, progress=a)
        if a <= 0:
            continue
        y = y0 + (1 - a) * 30
        card(c, x, y, cw, chh, a)
        badge_num(c, k + 1, x + cw / 2, y + 90, a, 38, bg=col)
        lines = s.split("\n")
        for j, ln in enumerate(lines):
            text(c, ln, x + cw / 2, y + 225 + j * 46 - (len(lines) - 1) * 16, 36, "bold", INK, a)


def b_ldn(c, t, C, B):
    S = LDN_S
    title_chip(c, "SESSÃO DE LONDRES", "3:00 · HORÁRIO DE NY", t, C["27.s"] - 0.2, PURPLE)
    chart_card(c)
    ch = Chart(LDN_K, CH_R, pad_lo=0.08, pad_hi=0.16)
    sw, d1 = S["sweep_i"], S["disp"][0]
    ch.view(*camera(t, [(0, ch.full_view(), 0), (C["27.oh"] - 1.0, (sw - 13, sw + 15, 42.5, 67.0), 1.8),
                        (C["30.tp"] - 0.3, (5, len(LDN_K) + 0.5, 21.5, 67.0), 1.8)]))
    n = reveal(t, [(0, 10, 0), (B["start"] + 0.3, 14, 2.0), (C["27.up"], sw - 4, 2.6), (C["27.oh"] - 0.4, sw, 1.2),
                   (C["28.sw"], sw + 1, 1.3), (C["29.d1"] - 0.1, d1 + 1, 0.5), (C["29.d2"] - 0.1, d1 + 3, 0.9),
                   (C["30.pb"], S["touch_i"], 2.4), (C["30.tc"] - 0.2, S["touch_i"] + 1, 0.5),
                   (C["31.run"] + 0.6, S["hit_i"] + 1, C["31.hit"] - C["31.run"] - 0.6), (C["31.hit"] + 0.6, len(LDN_K), 1.0)])
    E = story_events(C, "", {"liq": "27.bsl", "sw": "28.sw", "lab": "28.lab", "cl": "28.cl", "d1": "29.d1", "d2": "29.d2",
                              "bos": "29.bos", "fvg": "29.fvg", "m": "30.m", "ce": "30.ce", "tc": "30.tc", "lg": "30.sh",
                              "sl": "30.sl", "tp": "30.tp", "hit": "31.hit"})
    L = dict(liq="LIQUIDEZ COMPRADORA (BSL)", tp="LIQUIDEZ VENDEDORA (SSL)", close="FECHOU DE VOLTA ABAIXO",
             tp_dir="ABAIXO")
    L["tp"] = "LIQUIDEZ ABAIXO DA MÍNIMA"
    clip_card(c)
    story(c, t, ch, S, E, L, n)
    c.restore()
    a = fade_win(t, C["27.oh"], C["28.lab"])
    for i, p in S["liq_marks"]:
        ch.ring(c, i, p, AMBER, a, 15)
    i, p = S["liq_marks"][-1]
    pill(c, "MÁXIMA ANTIGA", ch.x(i), ch.y(p) - 44, INK, size=21, a=a, anchor="center")


def b_multi(c, t, C, B):
    S = MU_S
    title_chip(c, "MAIS DE UM FVG?", "QUAL OPERAR", t, B["start"] + 0.1, AMBER)
    chart_card(c)
    ch = Chart(MU_K, CH_R, pad_lo=0.16, pad_hi=0.08)
    sw, c1 = S["sweep_i"], S["disp"][0]
    ch.view(*camera(t, [(0, ch.full_view(), 0), (C["32.sw"] - 1.2, (sw - 12, sw + 17, 31.5, 58.0), 1.8),
                        (C["34.tp"] - 0.3, (3, len(MU_K) + 0.5, 31.5, 75.0), 1.8)]))
    n = reveal(t, [(0, sw - 2, 0), (B["start"] + 0.3, sw, 2.0), (C["32.sw"], sw + 1, 1.0), (C["32.run"], sw + 7, 2.6),
                   (C["34.pb"], S["touch_i"], 2.6), (C["34.tc"] - 0.2, S["touch_i"] + 1, 0.5),
                   (C["34.run"] + 0.5, S["hit_i"] + 1, C["34.hit"] - C["34.run"] - 0.5), (C["34.hit"] + 0.6, len(MU_K), 1.0)])
    E = story_events(C, "", {"sw": "32.sw", "lab": "32.sw", "fvg": "32.f2", "bos": "33.bk", "m": "34.m", "ce": "34.ce",
                              "tc": "34.tc", "lg": "34.lg", "sl": "34.sl", "tp": "34.tp", "hit": "34.hit"})
    E["lab"] = E.get("sw", 1e9) + 0.8
    L = dict(fvg="FVG 2", tp="LIQUIDEZ ACIMA DA MÁXIMA")
    clip_card(c)
    # FVG 1 (de baixo)
    i1, a1, b1 = S["fvg1"]
    fa = ep(t, C["32.f1"], 0.7)
    dimf = 1 - 0.6 * ep(t, C["33.l2"], 0.5)
    ch.zone(c, i1, len(MU_K) - 1, a1, b1, GRAY, fa * dimf, progress=fa, ext=ch.rx + ch.w - ch.xr(len(MU_K) - 1))
    story(c, t, ch, S, E, L, n)
    c.restore()
    pill(c, "FVG 1", XLAB, ch.y((a1 + b1) / 2), GRAY, size=24, a=fa * dimf)
    a = fade_win(t, C["33.l1"], C["33.l2"] + 1.5)
    pill(c, "ANTES DA QUEBRA", ch.x(i1 + 1), ch.y(b1) + 0, INK, size=21, a=a, anchor="right")
    a = fade_win(t, C["33.l2"], C["34.m"])
    pill(c, "NA QUEBRA DE ESTRUTURA", XLAB - 290, ch.y(S["fvg"][2]) - 34, GREEN, size=21, a=a)
    check_icon(c, XLAB + 112, ch.y((S["fvg"][1] + S["fvg"][2]) / 2), 16, fade_win(t, C["33.ok"], C["34.ce"]), GREEN)
    a = fade_win(t, C["32.f1"], C["33.bk"])
    if a > 0:
        text(c, "?", XLAB + 150, ch.y(46), 64, "black", AMBER, a)


def b_erro1(c, t, C, B):
    S, Wt = E1_S, E1_W
    title_chip(c, "O ERRO QUE MAIS", "ESTOPA TRADERS", t, B["start"] + 0.1, RED, t_out=C["37.ok"] - 0.2)
    title_chip(c, "A OPERAÇÃO", "CORRETA", t, C["37.ok"], GREEN)
    chart_card(c)
    ch = Chart(E1_K, CH_R, pad_lo=0.14, pad_hi=0.08)
    c1 = Wt["fvg"][0]
    n = reveal(t, [(0, c1, 0), (C["35.up"], c1 + 4, 1.6), (C["35.pb"], Wt["touch_i"] + 1, 1.4),
                   (C["35.lg"] + 0.5, Wt["stop_i"] + 1, 1.0), (C["37.ok"] + 0.4, S["sweep_i"], 2.4),
                   (C["37.sw"], S["sweep_i"] + 1, 0.8), (C["37.d"], S["sweep_i"] + 4, 1.4),
                   (C["37.ce"] + 0.4, S["touch_i"] + 1, 2.0),
                   (C["37.run"] + 0.5, S["hit_i"] + 1, C["37.hit"] - C["37.run"] - 0.5), (C["37.hit"] + 0.6, len(E1_K), 1.0)])
    Ew = story_events(C, "", {"fvg": "35.fvg", "lg": "35.lg", "sl": "35.lg", "slhit": "35.slh", "tc": "35.lg"})
    Ew["sl"] = Ew["lg"] + 0.3
    fade_w = 1 - ep(t, C["37.ok"], 0.6)
    E = story_events(C, "", {"liq": "37.sw", "sw": "37.sw", "lab": "37.lab", "d1": "37.d", "bos": "37.bos", "fvg": "37.fvg",
                              "ce": "37.ce", "lg": "37.lg", "sl": "37.sl", "tp": "37.tp", "hit": "37.hit", "tc": "37.lg"})
    E["d2"] = E.get("d1", 1e9) + 0.5; E["d3"] = E.get("d1", 1e9) + 1.0
    L = dict(liq="LIQUIDEZ VENDEDORA", entry="ENTRADA (CE)", liq_below=True)
    clip_card(c)
    # região antes do movimento (rewind)
    a = fade_win(t, C["36.ns"], C["37.ok"])
    if a > 0:
        x0, x1 = ch.xl(Wt["cons"][0]) - 10, ch.xr(Wt["cons"][1]) + 10
        rrect(c, x0, ch.y0 - 10, x1 - x0, ch.h + 20, 14, RED, a * 0.07)
    Lw = dict(entry="ENTRADA NA BORDA")
    story(c, t, ch, Wt, Ew, Lw, n, fade=fade_w, parts=("under",))
    story(c, t, ch, S, E, L, n)
    story(c, t, ch, Wt, Ew, Lw, n, fade=fade_w, parts=("over",))
    c.restore()
    pill(c, "SEM VARRIDA", (ch.xl(Wt["cons"][0]) + ch.xr(Wt["cons"][1])) / 2, ch.y0 + 20, RED, size=23, a=a, anchor="center")
    if a > 0:
        check_icon(c, (ch.xl(Wt["cons"][0]) + ch.xr(Wt["cons"][1])) / 2, ch.y0 + 80, 20, a, RED, "x")
    ar = fade_win(t, C["36.rw"], C["36.ns"] + 1.0)
    pill(c, "◀◀  VOLTANDO", W / 2, 200, INK, size=24, a=ar, anchor="center")
    ae = fade_win(t, C["36.ed"], C["37.ok"])
    ch.ring(c, Wt["touch_i"], Wt["entry"], RED, ae, 20)
    pill(c, "BORDA SUPERIOR — NÃO O MEIO", ch.x(Wt["touch_i"]) + 34, ch.y(Wt["entry"]) - 44, RED, size=22, a=ae)


def b_erro2(c, t, C, B):
    F, S = E2_F, E2_S
    title_chip(c, "O SEGUNDO", "ERRO", t, B["start"] + 0.1, RED, t_out=C["40.sw"] - 0.3)
    title_chip(c, "ESPERE O", "PRÓXIMO SETUP", t, C["40.sw"] - 0.1, GREEN)
    chart_card(c)
    ch = Chart(E2_K, CH_R, pad_lo=0.14, pad_hi=0.08)
    ch.view(6, len(E2_K) + 0.5, 40.0, 63.0)
    sw1 = F["sweep_i"]
    n = reveal(t, [(0, sw1 - 1, 0), (C["38.sw"] - 0.2, sw1 + 1, 1.0), (C["38.d"], sw1 + 4, 1.4),
                   (C["38.bc"] - 0.2, F["fail_i"] + 1, 1.0), (C["39.st"] - 0.1, F["naive_stop"] + 1, 1.4),
                   (C["39.w"], S["sweep_i"], 2.0), (C["40.sw"], S["sweep_i"] + 1, 0.8), (C["40.d"], S["sweep_i"] + 4, 1.4),
                   (C["40.ce"] + 0.4, S["touch_i"] + 1, 2.0),
                   (C["40.run"] + 0.5, S["hit_i"] + 1, C["40.hit"] - C["40.run"] - 0.5), (C["40.hit"] + 0.6, len(E2_K), 1.0)])
    Ef = story_events(C, "", {"liq": "38.sw", "sw": "38.sw", "lab": "38.sw", "d1": "38.d", "bos": "38.bos", "fvg": "38.fvg",
                               "fail": "38.fail"})
    Ef["d2"] = Ef.get("d1", 1e9) + 0.5; Ef["d3"] = Ef.get("d1", 1e9) + 1.0
    Ef["lab"] = Ef.get("sw", 1e9) + 0.8
    Ef["liqout"] = C["39.w"]
    fade_f = 1 - ep(t, C["40.sw"] - 0.4, 0.6)
    E = story_events(C, "", {"liq": "39.w", "sw": "40.sw", "lab": "40.lab", "d1": "40.d", "bos": "40.bos", "fvg": "40.fvg",
                              "ce": "40.ce", "lg": "40.lg", "sl": "40.sl", "tp": "40.tp", "hit": "40.hit", "tc": "40.lg"})
    E["d2"] = E.get("d1", 1e9) + 0.5; E["d3"] = E.get("d1", 1e9) + 1.0
    E["liq"] = E.get("liq", 1e9) + 1.5
    clip_card(c)
    Lf = dict(liq="LIQUIDEZ", fvg="FVG")
    story(c, t, ch, F, Ef, Lf, n, fade=fade_f, parts=("under",))
    story(c, t, ch, S, E, dict(liq="NOVA LIQUIDEZ", entry="ENTRADA (CE)"), n)
    story(c, t, ch, F, Ef, Lf, n, fade=fade_f, parts=("over",))
    c.restore()
    i = F["fail_i"]
    o, h, l, cl = E2_K[i]
    ab = fade_win(t, C["38.bc"] + 0.3, C["40.sw"])
    if ab > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(ch.xl(i) - 7, ch.y(o) - 7, ch.xr(i) + 7, ch.y(cl) + 7), 8, 8),
                    paint(INK, ab, stroke=3))
    pill(c, "CORPO FECHOU ABAIXO", ch.xr(i) + 18, ch.y(cl) + 10, INK, size=21, a=fade_win(t, C["38.bc"] + 0.5, C["39.w"]))
    pill(c, "GAP FALHOU", XLAB, ch.y((F["fvg"][1] + F["fvg"][2]) / 2), RED, size=24, a=fade_win(t, C["38.fail"], C["40.sw"] - 0.3))
    # compra ingênua
    a = fade_win(t, C["39.st"] - 0.6, C["39.w"])
    if a > 0:
        ch.ring(c, i, F["entry"], INK, a, 16)
        pill(c, "COMPRA MESMO ASSIM", ch.xl(i) - 14, ch.y(F["entry"]), INK, size=21, a=a, anchor="right")
        a2 = fade_win(t, C["39.st"] + 0.9, C["39.w"])
        pill(c, "ESTOPADO", ch.x(F["naive_stop"]), ch.y(E2_K[F["naive_stop"]][2]) + 40, RED, size=22, a=a2, anchor="center")
    a = fade_win(t, C["39.rule"], C["39.w"] + 0.5)
    if a > 0:
        check_icon(c, XLAB + 40, ch.y(44), 26, a, RED, "x")
        text(c, "OPERAÇÃO", XLAB + 40, ch.y(44) + 64, 20, "extrabold", RED, a)
        text(c, "CANCELADA", XLAB + 40, ch.y(44) + 90, 20, "extrabold", RED, a)


def b_checklist(c, t, C, B):
    x, y, w, h = 460, 120, 1000, 700
    a0 = ep(t, B["start"], 0.6)
    card(c, x, y, w, h, a0)
    text(c, "O CHECKLIST", W / 2, y + 92, 40, "black", INK, a0, tracking=2)
    hline(c, x + 80, x + w - 80, y + 132, LINE, a0, 2)
    items = [("Liquidez varrida", "41.i1"), ("Deslocamento", "41.i2"), ("Quebra de estrutura", "41.i3"),
             ("FVG dentro desse movimento", "41.i4"), ("Entrada no CE · stop além da varrida", "41.i5")]
    for k, (s, cue) in enumerate(items):
        a = ep(t, C[cue] - 0.1, 0.5)
        yy = y + 205 + k * 88
        check_icon(c, x + 120, yy, 24, a, GREEN)
        text(c, s, x + 170 + (1 - a) * 20, yy + 13, 36, "semibold", INK, a, align="left")
    ax = ep(t, C["41.x"], 0.5)
    if ax > 0:
        rrect(c, x + 80, y + h - 118, w - 160, 84, 20, RED, ax * 0.1)
        check_icon(c, x + 150, y + h - 76, 22, ax, RED, "x")
        text_mid(c, "Faltou um?  Pule a operação.", x + w / 2 + 30, y + h - 76, 34, "extrabold", RED, ax)


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
    c.drawPath(p, paint(INK, a))
    c.drawPath(p, paint("#FFFFFF", a, stroke=1.6))
    c.restore()


def b_cta(c, t, C, B):
    like, sub, bell, com, bye = C["42.like"], C["42.sub"], C["42.bell"], C["42.com"], C["42.bye"]
    # cartões principais
    y = 240
    # LIKE
    a = ep(t, like - 0.2, 0.5)
    lx = 300
    card(c, lx, y, 340, 340, a, scale=1 + 0.06 * math.sin(math.pi * prog(t, like + 0.4, 0.5)))
    on = ep(t, like + 0.5, 0.3)
    icon(c, "", lx + 170, y + 150, 120, mix(INK, BLUE, on), a)
    text(c, "Curtir", lx + 170, y + 290, 36, "bold", mix(INK, BLUE, on), a)
    # INSCREVA-SE
    a = ep(t, sub - 0.2, 0.5)
    sx, sw_ = 720, 480
    card(c, sx, y, sw_, 340, a)
    if a > 0:
        done = ep(t, sub + 1.3, 0.3)
        press = math.sin(math.pi * prog(t, sub + 1.1, 0.35))
        bw, bh = 340 * (1 - 0.04 * press), 96 * (1 - 0.04 * press)
        bx, by = sx + sw_ / 2 - bw / 2, y + 130 - bh / 2
        rrect(c, bx, by, bw, bh, 48, mix(RED, "#E5E5EA", done), a, shadow=True)
        text_mid(c, "INSCREVA-SE", bx + bw / 2, by + bh / 2, 34, "extrabold", "#FFFFFF", a * (1 - done))
        text_mid(c, "INSCRITO  ✓", bx + bw / 2, by + bh / 2, 34, "extrabold", INK2, a * done)
        text(c, "no canal", sx + sw_ / 2, y + 290, 36, "bold", INK, a)
        # cursor
        ca = fade_win(t, sub + 0.2, bell + 0.4)
        mv = ep(t, sub + 0.2, 0.9)
        cursor(c, lerp(sx + sw_ + 140, bx + bw * 0.62, mv), lerp(y + 420, by + bh * 0.55, mv), ca, press)
    # SININHO
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
    # comentário
    a = fade_win(t, com, bye)
    if a > 0:
        yy = 640 + (1 - a) * 20
        card(c, 560, yy, 800, 130, a, r=36)
        icon(c, "", 650, yy + 65, 56, BLUE, a)
        text_mid(c, "Qual tema no próximo vídeo?", 1000, yy + 65, 38, "bold", INK, a)
    ab = ep(t, bye, 0.6)
    if ab > 0:
        text(c, "Bons trades!", W / 2, 760 + (1 - ab) * 20, 72, "black", INK, ab)


BLOCKS = dict(hook=b_hook, promessa=b_promessa, definicao=b_definicao, alta=b_alta, baixa=b_baixa, filtro=b_filtro,
              ce=b_ce, falha=b_falha, ny=b_ny, resumo=b_resumo, ldn=b_ldn, multi=b_multi, erro1=b_erro1,
              erro2=b_erro2, checklist=b_checklist, cta=b_cta)
