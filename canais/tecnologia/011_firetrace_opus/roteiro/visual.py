"""Visual do vídeo Tecnologia 011 — FireTrace, protótipo de análise de incêndios feito com o Claude Opus 5.5. Tema 'tech'.
Só motion graphics próprios. NENHUM quadro ou trecho do vídeo original (direito autoral): a interface do FireTrace aparece
apenas como RECRIAÇÃO desenhada aqui (relevo procedural, perímetro, gráficos, câmera térmica sintética), sempre com o
selo RECRIAÇÃO ILUSTRATIVA e o crédito "Original: @DilumSanjaya no X". Sem logo do X: só o texto "post no X"."""
import math
from contextlib import contextmanager
from functools import lru_cache
import numpy as np
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

# neste Linux não há Consolas: a fonte mono do tech.py não carrega. Usa DejaVu Sans Mono (como no 009/010).
motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

tech.SERIE = "TECH//011 · FIRETRACE"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_011_firetrace_opus.mp4"
# som padrão do canal (_ferramentas/som_tech.py); aqui só os efeitos que fogem do "pop" de cada cue
SOM = dict(sfx={
    "01.a": "glitch", "01.c": "data", "01.d": "alert", "01.e": "impact",
    "02.a": "notif", "02.b": "typing@+0.1", "02.e": "notif",
    "03.s": "lock", "04.c": "data", "05.a": "data", "05.e": "data", "05.f": "alert",
    "06.d": "data", "06.e": "data", "06.f": "whoosh",
    "07.a": "deny", "07.b": "glitch",
    "08.b": "data", "09.c": "data", "09.f": "alert",
    "10.a": "data", "10.c": "alert",
    "11.a": "deny", "11.b": "deny", "11.c": "lock", "11.d": "lock",
    "12.a": "alert", "12.b": "alert", "12.c": "alert", "12.d": "alert",
    "13.a": "confirm", "13.b": "confirm", "13.c": "confirm", "13.d": "confirm", "13.e": "confirm"})
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

# paleta quente da RECRIAÇÃO (lembra o original claro creme + laranja/vermelho)
PAPER = "#FBF7F0"
CREAM = "#F1E8D9"
LINEW = "#E0D3BF"
TXT = "#2A211B"
TXT2 = "#7D6F62"
ORG = "#E2582A"
RED = "#C9361F"
AMB = "#E89A2E"
GRN = "#4E7A3A"


# ---------------------------------------------------------------- utilidades
def fade(t, t0, t1, d=0.5, d_out=0.4):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def rise(t, t0, d=0.5, dy=24):
    a = ep(t, t0, d)
    return a, (1 - a) * dy


@contextmanager
def cam(c, t, B, z0=1.0, z1=1.04, px=0.0, py=0.0, cx=W / 2, cy=H / 2):
    u = clamp((t - B["start"]) / max(1.0, B["end"] - B["start"]))
    u = u * u * (3 - 2 * u)
    z = lerp(z0, z1, u)
    c.save()
    c.translate(cx + px * u, cy + py * u)
    c.scale(z, z)
    c.translate(-cx, -cy)
    try:
        yield
    finally:
        c.restore()


def wrap(s, peso, size, maxw):
    words, lines, cur = s.split(" "), [], ""  # split(" "): não quebra no espaço rígido (\u00a0)
    for w in words:
        tst = (cur + " " + w).strip()
        if cur and text_w(tst, peso, size) > maxw:
            lines.append(cur); cur = w
        else:
            cur = tst
    if cur:
        lines.append(cur)
    return lines


def para(c, s, x, y, size, peso, col, a, maxw, lh=None, align="left"):
    lh = lh or size * 1.3
    ls = wrap(s, peso, size, maxw)
    for i, ln in enumerate(ls):
        text(c, ln, x, y + i * lh, size, peso, col, a, align=align)
    return len(ls) * lh


def fonte(c, s, a, y=880):
    text(c, s, W - 150, y, 20, "mono", DIM, a, align="right")


def selo(c, a, x=W - 150, y=192, credito=True):
    """selo obrigatório em toda recriação da interface + crédito do original"""
    if a <= 0:
        return
    x0, _ = chip(c, "RECRIAÇÃO ILUSTRATIVA", x, y, GOLD, a, anchor="right", size=20, filled=True)
    if credito:
        text(c, "Original: @DilumSanjaya no X", x0 - 20, y + 8, 20, "mono", INK2, a, align="right")


def clip_rr(c, x, y, w, h, r):
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), skia.ClipOp.kIntersect, True)


# ---------------------------------------------------------------- relevo procedural (desenhado aqui)
NX, NY = 72, 46


def _hfield(u, v):
    """altura 0..1 (u: esquerda→direita, v: fundo→frente)"""
    ridge = np.exp(-((u - 0.62 + 0.35 * (v - 0.5)) / 0.16) ** 2)          # crista principal (fundo-frente)
    ridge2 = 0.6 * np.exp(-((v - 0.32 - 0.25 * u) / 0.10) ** 2)            # crista transversal
    far = 0.55 * (1 - v) ** 2
    n1 = 0.10 * np.sin(9 * u + 2.0) * np.sin(7 * v + 1.0)
    n2 = 0.05 * np.sin(23 * u + 5 * v) * np.sin(19 * v - 3 * u + 0.5)
    n3 = 0.025 * np.sin(53 * u + 1.3) * np.sin(47 * v + 0.7)
    return np.clip(0.18 + 0.42 * ridge + 0.25 * ridge2 + far + n1 + n2 + n3, 0, 1.3)


_U, _V = np.meshgrid(np.linspace(0, 1, NX + 1), np.linspace(0, 1, NY + 1))
HF = _hfield(_U, _V)  # [NY+1, NX+1]


def height_at(u, v):
    x, y = clamp(u) * NX, clamp(v) * NY
    i, j = min(int(x), NX - 1), min(int(y), NY - 1)
    fx, fy = x - i, y - j
    h00, h10, h01, h11 = HF[j, i], HF[j, i + 1], HF[j + 1, i], HF[j + 1, i + 1]
    return (h00 * (1 - fx) + h10 * fx) * (1 - fy) + (h01 * (1 - fx) + h11 * fx) * fy


def proj(u, v, w, h, hgt=None):
    """(u,v) do terreno → (x,y) local numa vista oblíqua de largura w, altura h"""
    hgt = height_at(u, v) if hgt is None else hgt
    s = lerp(0.62, 1.0, v)
    x = w / 2 + (u - 0.5) * w * 1.22 * s
    y = h * 0.28 + v * h * 0.92 - hgt * h * 0.38 * s
    return x, y


def _rgb(hx):
    return np.array([int(hx[1:3], 16), int(hx[3:5], 16), int(hx[5:7], 16)], float)


@lru_cache(None)
def terrain_img(w, h, dark=False):
    """imagem do relevo low-poly em tons quentes (ou noturno, para a câmera de perseguição)"""
    w, h = int(w), int(h)
    surf = skia.Surface(w, h)
    c = surf.getCanvas()
    sky = skia.Paint(AntiAlias=True)
    sky.setShader(skia.GradientShader.MakeLinear(points=[(0, 0), (0, h * 0.5)],
                                                 colors=[hexc("#DCD6CB"), hexc("#EFE6D6")]))
    c.drawRect(skia.Rect.MakeWH(w, h), sky)
    low, high, tree = _rgb("#B98F5B"), _rgb("#EBD9B4"), "#46603A"
    for j in range(NY):
        for i in range(NX):
            u0, u1, v0, v1 = i / NX, (i + 1) / NX, j / NY, (j + 1) / NY
            hs = [HF[j, i], HF[j, i + 1], HF[j + 1, i + 1], HF[j + 1, i]]
            pts = [proj(u0, v0, w, h, hs[0]), proj(u1, v0, w, h, hs[1]), proj(u1, v1, w, h, hs[2]), proj(u0, v1, w, h, hs[3])]
            dhdu = (hs[1] + hs[2] - hs[0] - hs[3]) / 2 * NX / 10
            dhdv = (hs[2] + hs[3] - hs[0] - hs[1]) / 2 * NY / 10
            shade = clamp(0.92 - 0.55 * dhdu - 0.35 * dhdv, 0.45, 1.15)
            hm = clamp(sum(hs) / 4 / 1.0)
            col = (low * (1 - hm) + high * hm) * shade
            col = np.clip(col, 0, 255)
            p = skia.Path()
            p.moveTo(*pts[0]); [p.lineTo(*q) for q in pts[1:]]; p.close()
            c.drawPath(p, skia.Paint(AntiAlias=True, Color=skia.Color(int(col[0]), int(col[1]), int(col[2]))))
            if hash01(i * 131 + j, 3) < 0.30 + 0.25 * (1 - hm):
                cx = sum(q[0] for q in pts) / 4 + (hash01(i, j) - 0.5) * 6
                cy = sum(q[1] for q in pts) / 4
                r = lerp(1.6, 3.6, v0)
                c.drawCircle(cx, cy - r, r, paint(tree, 0.85))
    if dark:
        c.drawRect(skia.Rect.MakeWH(w, h), paint("#0B0F1A", 0.35))
    return surf.makeImageSnapshot()


# ---------------------------------------------------------------- incêndio simulado (perímetro em forma de gota)
IGN = (0.24, 0.76)
HEAD = (0.70, 0.18)


def _center(s):
    # leve curva no eixo de avanço
    u = lerp(IGN[0], HEAD[0], s) + 0.05 * math.sin(s * math.pi)
    v = lerp(IGN[1], HEAD[1], s)
    return u, v


def fire_poly(p, n=48):
    """contorno (u,v) da área queimada quando o fogo percorreu a fração p do eixo"""
    p = max(p, 0.02)
    left, right = [], []
    for k in range(n + 1):
        s = p * k / n
        cu, cv = _center(s)
        du, dv = HEAD[0] - IGN[0] + 0.05 * math.pi * math.cos(s * math.pi), HEAD[1] - IGN[1]
        L = math.hypot(du, dv)
        nu, nv = -dv / L, du / L
        r = (0.025 + 0.11 * (s / p) ** 0.6 * p) * (1 + 0.18 * math.sin(31 * s + 1.0) + 0.1 * math.sin(73 * s))
        rl = r * (1.15 + 0.2 * math.sin(11 * s))
        left.append((cu + nu * rl, cv + nv * rl))
        right.append((cu - nu * r * 0.9, cv - nv * r * 0.9))
    hu, hv = _center(p)
    rh = 0.025 + 0.11 * p
    ang0 = math.atan2(left[-1][1] - hv, left[-1][0] - hu)
    ang1 = math.atan2(right[-1][1] - hv, right[-1][0] - hu)
    arc = []
    pu, pv = _center(max(0.0, p - 0.02))
    af = math.atan2(hv - pv, hu - pu)
    d1 = (ang1 - ang0) % (2 * math.pi)
    best = None
    for da_ in (d1, d1 - 2 * math.pi):
        mid = ang0 + da_ / 2
        err = abs(math.atan2(math.sin(mid - af), math.cos(mid - af)))
        if best is None or err < best[0]:
            best = (err, da_)
    da = best[1]
    for k in range(1, 12):
        an = ang0 + da * k / 12
        arc.append((hu + rh * 0.9 * math.cos(an), hv + rh * 0.9 * math.sin(an)))
    tail = []
    iu, iv = _center(0)
    for k in range(1, 8):
        an = math.atan2(right[0][1] - iv, right[0][0] - iu) + math.pi * k / 8
        tail.append((iu + 0.03 * math.cos(an), iv + 0.03 * math.sin(an)))
    return left + arc + right[::-1] + tail


MARCAS = [(0.0, "Ignição · 14 ago, 14:26"), (0.27, "14 ago, 18:00"), (0.52, "15 ago, 00:00"), (0.76, "15 ago, 06:00"),
          (1.0, "15 ago, 12:00")]


def draw_fire(c, ox, oy, w, h, p, a, t, marks=True, size=17):
    if a <= 0:
        return
    poly = [proj(u, v, w, h) for u, v in fire_poly(p)]
    path = skia.Path()
    path.moveTo(ox + poly[0][0], oy + poly[0][1])
    for x, y in poly[1:]:
        path.lineTo(ox + x, oy + y)
    path.close()
    c.drawPath(path, paint(RED, 0.42 * a))
    c.drawPath(path, blur_paint(ORG, 0.6 * a, 6, stroke=6))
    c.drawPath(path, paint("#FF8A3D", 0.95 * a, stroke=2.4))
    # frente ativa piscando
    hu, hv = _center(p)
    hx, hy = proj(hu, hv, w, h)
    fl = 0.6 + 0.4 * math.sin(t * 9)
    c.drawCircle(ox + hx, oy + hy, 12, blur_paint("#FFB347", 0.8 * a * fl, 8))
    if not marks:
        return
    # eixo com marcas de hora
    pts = [proj(*_center(p * k / 30), w, h) for k in range(31)]
    pa = paint("#FFD27A", 0.9 * a, stroke=2.2)
    pa.setPathEffect(skia.DashPathEffect.Make([7, 5], 0))
    pp = skia.Path(); pp.moveTo(ox + pts[0][0], oy + pts[0][1]); [pp.lineTo(ox + x, oy + y) for x, y in pts[1:]]
    c.drawPath(pp, pa)
    for s, lab in MARCAS:
        if s > p + 0.001:
            continue
        x, y = proj(*_center(s), w, h)
        am = a * clamp((p - s) * 12 + 1)
        c.drawCircle(ox + x, oy + y, 6, paint("#FFFFFF", am))
        c.drawCircle(ox + x, oy + y, 6, paint(ORG, am, stroke=2.5))
        tw = text_w(lab, "semibold", size) + 18
        bx, by = ox + x + 12, oy + y - 34
        rrect(c, bx, by, tw, size + 12, 6, "#2A211B", 0.85 * am)
        text(c, lab, bx + 9, by + size + 2, size, "semibold", "#FFFFFF", am, align="left")


def map_view(c, x, y, w, h, a, t, p_fire=0.0, fire_a=1.0, marks=True, dark=False, r=10):
    if a <= 0:
        return
    c.save()
    clip_rr(c, x, y, w, h, r)
    pa = skia.Paint(AntiAlias=True)
    pa.setAlphaf(a)
    c.drawImage(terrain_img(int(w), int(h), dark), x, y, skia.SamplingOptions(skia.FilterMode.kLinear), pa)
    if p_fire > 0:
        draw_fire(c, x, y, w, h, p_fire, a * fire_a, t, marks)
    c.restore()


# ---------------------------------------------------------------- câmera térmica sintética (paleta "ironbow")
IRON = [(0.0, "#05030F"), (0.22, "#2E0B5E"), (0.45, "#8E1F6E"), (0.62, "#D9452B"), (0.78, "#F59B26"), (0.9, "#FBE36A"),
        (1.0, "#FFFFF4")]


@lru_cache(None)
def thermal_img(w, h, seed=0):
    yy, xx = np.mgrid[0:h, 0:w] / np.array([h, w], float)[:, None, None]
    f = 0.30 + 0.12 * np.sin(6 * xx + 1 + seed) * np.sin(5 * yy + 2) + 0.05 * np.sin(31 * xx + 17 * yy)
    f += 0.04 * np.sin(57 * xx - 11 * yy + seed)
    # mancha quente irregular (ponto quente)
    cx, cy = 0.56, 0.48
    ang = np.arctan2(yy - cy, (xx - cx) * w / h)
    rr = np.hypot((xx - cx) * w / h, yy - cy) / (0.20 * (1 + 0.25 * np.sin(3 * ang + 1) + 0.12 * np.sin(7 * ang)))
    f += 0.75 * np.exp(-rr ** 2 * 1.4)
    f = np.clip(f, 0, 1)
    xs = [p for p, _ in IRON]
    out = np.zeros((h, w, 4), np.uint8)
    for k in range(3):
        out[..., k] = np.interp(f, xs, [_rgb(col)[k] for _, col in IRON]).astype(np.uint8)
    out[..., 3] = 255
    return skia.Image.fromarray(out)


def thermal_cam(c, x, y, w, h, a, t, drone="FT-02 Harrier", show_hot=True):
    if a <= 0:
        return
    c.save()
    clip_rr(c, x, y, w, h, 8)
    pa = skia.Paint(AntiAlias=True); pa.setAlphaf(a)
    c.drawImage(thermal_img(int(w), int(h)), x, y, skia.SamplingOptions(skia.FilterMode.kLinear), pa)
    hud = "#E8F7FF"
    m = 22
    for bx, by, dx, dy in ((x + m, y + m, 1, 1), (x + w - m, y + m, -1, 1), (x + m, y + h - m, 1, -1), (x + w - m, y + h - m, -1, -1)):
        c.drawLine(bx, by, bx + dx * 26, by, paint(hud, a, stroke=2)); c.drawLine(bx, by, bx, by + dy * 26, paint(hud, a, stroke=2))
    blink = 0.5 + 0.5 * math.sin(t * 5)
    c.drawCircle(x + m + 14, y + m + 26, 6, paint("#FF3B3B", a * blink))
    text(c, "REC  IR · IRONBOW", x + m + 28, y + m + 32, 17, "monob", hud, a, align="left")
    text(c, drone, x + m + 8, y + m + 56, 17, "mono", hud, a, align="left")
    text(c, "ALT 580 ft   GS 22 kt", x + m + 8, y + h - m - 34, 17, "mono", hud, a, align="left")
    text(c, "34°20' N  117°55' W", x + m + 8, y + h - m - 10, 17, "mono", hud, a, align="left")
    text(c, "BAT 73%", x + w - m - 8, y + h - m - 34, 17, "mono", hud, a, align="right")
    text(c, "ZOOM 1.0x", x + w - m - 8, y + h - m - 10, 17, "mono", hud, a, align="right")
    # retícula
    cx, cy = x + w * 0.56, y + h * 0.48
    c.drawLine(cx - 30, cy, cx - 10, cy, paint(hud, a, stroke=2)); c.drawLine(cx + 10, cy, cx + 30, cy, paint(hud, a, stroke=2))
    c.drawLine(cx, cy - 30, cx, cy - 10, paint(hud, a, stroke=2)); c.drawLine(cx, cy + 10, cx, cy + 30, paint(hud, a, stroke=2))
    if show_hot:
        k = 0.5 + 0.5 * math.sin(t * 6)
        c.drawRect(skia.Rect.MakeXYWH(cx - 70, cy - 60, 140, 120), paint("#FF3B3B", a * (0.6 + 0.4 * k), stroke=3))
        rrect(c, cx - 70, cy - 98, 196, 32, 4, "#FF3B3B", a)
        text(c, "HOT SPOT · 983 °C", cx - 62, cy - 75, 17, "monob", "#FFFFFF", a, align="left")
    c.restore()


# ---------------------------------------------------------------- ícones desenhados
def ic_drone(c, cx, cy, s, col, a, t=0.0):
    k = s * 0.36
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        c.drawLine(cx, cy, cx + dx * k, cy + dy * k, paint(col, a, stroke=s * 0.08, cap_round=True))
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.17, paint(col, a, stroke=s * 0.06))
        ang = t * 30 + dx * dy
        c.drawLine(cx + dx * k - s * 0.15 * math.cos(ang), cy + dy * k - s * 0.15 * math.sin(ang),
                   cx + dx * k + s * 0.15 * math.cos(ang), cy + dy * k + s * 0.15 * math.sin(ang), paint(col, 0.7 * a, stroke=2))
    c.drawRect(skia.Rect.MakeXYWH(cx - s * 0.12, cy - s * 0.12, s * 0.24, s * 0.24), paint(col, a))


def ic_plane(c, cx, cy, s, col, a, ang=0.0):
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = skia.Path()
    p.moveTo(0, -s * 0.5); p.lineTo(s * 0.07, -s * 0.38); p.lineTo(s * 0.07, -s * 0.1); p.lineTo(s * 0.5, s * 0.1)
    p.lineTo(s * 0.5, s * 0.2); p.lineTo(s * 0.07, s * 0.08); p.lineTo(s * 0.06, s * 0.34); p.lineTo(s * 0.2, s * 0.45)
    p.lineTo(s * 0.2, s * 0.52); p.lineTo(0, s * 0.46); p.lineTo(-s * 0.2, s * 0.52); p.lineTo(-s * 0.2, s * 0.45)
    p.lineTo(-s * 0.06, s * 0.34); p.lineTo(-s * 0.07, s * 0.08); p.lineTo(-s * 0.5, s * 0.2); p.lineTo(-s * 0.5, s * 0.1)
    p.lineTo(-s * 0.07, -s * 0.1); p.lineTo(-s * 0.07, -s * 0.38); p.close()
    c.drawPath(p, paint(col, a))
    c.restore()


def ic_sat(c, cx, cy, s, col, a):
    c.save(); c.translate(cx, cy); c.rotate(-30)
    c.drawRect(skia.Rect.MakeXYWH(-s * 0.13, -s * 0.13, s * 0.26, s * 0.26), paint(col, a))
    for d in (-1, 1):
        x0 = d * s * 0.2
        rect = skia.Rect.MakeXYWH(min(x0, x0 + d * s * 0.3), -s * 0.1, s * 0.3, s * 0.2)
        c.drawRect(rect, paint(col, a, stroke=s * 0.04))
        c.drawLine(rect.left() + s * 0.1, -s * 0.1, rect.left() + s * 0.1, s * 0.1, paint(col, a, stroke=s * 0.025))
        c.drawLine(rect.left() + s * 0.2, -s * 0.1, rect.left() + s * 0.2, s * 0.1, paint(col, a, stroke=s * 0.025))
        c.drawLine(d * s * 0.13, 0, x0, 0, paint(col, a, stroke=s * 0.04))
    c.restore()
    for k in range(3):
        r = s * (0.35 + 0.12 * k)
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(cx - r, cy + s * 0.15 - r, 2 * r, 2 * r), 60, 60)
        c.drawPath(p, paint(col, a * (0.8 - 0.2 * k), stroke=s * 0.035))


def ic_warn(c, cx, cy, s, col, a):
    p = skia.Path(); p.moveTo(cx, cy - s * 0.48); p.lineTo(cx + s * 0.52, cy + s * 0.42); p.lineTo(cx - s * 0.52, cy + s * 0.42)
    p.close()
    pp = paint(col, a, stroke=s * 0.08); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    c.drawLine(cx, cy - s * 0.15, cx, cy + s * 0.12, paint(col, a, stroke=s * 0.09, cap_round=True))
    c.drawCircle(cx, cy + s * 0.27, s * 0.055, paint(col, a))


def ic_flame(c, cx, cy, s, col, a):
    p = skia.Path()
    p.moveTo(cx, cy - s * 0.5)
    p.cubicTo(cx + s * 0.1, cy - s * 0.2, cx + s * 0.42, cy - s * 0.05, cx + s * 0.32, cy + s * 0.25)
    p.cubicTo(cx + s * 0.25, cy + s * 0.48, cx - s * 0.25, cy + s * 0.48, cx - s * 0.32, cy + s * 0.25)
    p.cubicTo(cx - s * 0.4, cy, cx - s * 0.1, cy - s * 0.15, cx, cy - s * 0.5)
    p.close()
    c.drawPath(p, paint(col, a))
    q = skia.Path()
    q.moveTo(cx, cy - s * 0.05)
    q.cubicTo(cx + s * 0.18, cy + s * 0.1, cx + s * 0.16, cy + s * 0.38, cx, cy + s * 0.38)
    q.cubicTo(cx - s * 0.16, cy + s * 0.38, cx - s * 0.18, cy + s * 0.15, cx, cy - s * 0.05)
    c.drawPath(q, paint("#FFF1C2", a))


def ic_clock(c, cx, cy, r, col, a, t):
    c.drawCircle(cx, cy, r, paint(col, a, stroke=r * 0.1))
    for k in range(12):
        an = k * math.pi / 6
        c.drawLine(cx + r * 0.78 * math.cos(an), cy + r * 0.78 * math.sin(an), cx + r * 0.9 * math.cos(an),
                   cy + r * 0.9 * math.sin(an), paint(col, a, stroke=r * 0.05))
    an = t * 2.0 - math.pi / 2
    c.drawLine(cx, cy, cx + r * 0.65 * math.cos(an), cy + r * 0.65 * math.sin(an), paint(INK, a, stroke=r * 0.08, cap_round=True))
    an2 = t * 0.17 - math.pi / 2
    c.drawLine(cx, cy, cx + r * 0.42 * math.cos(an2), cy + r * 0.42 * math.sin(an2), paint(INK, a, stroke=r * 0.1, cap_round=True))
    c.drawCircle(cx, cy, r * 0.08, paint(col, a))


# ---------------------------------------------------------------- moldura da RECRIAÇÃO (interface clara, quente)
MX, MY, MW, MH = 150, 222, 1620, 650


def mock_frame(c, a, tab="Incidente"):
    """janela creme do FireTrace recriado. Retorna (x, y, w, h) da área útil abaixo da barra."""
    if a <= 0:
        return MX + 12, MY + 58, MW - 24, MH - 70
    panel(c, MX, MY, MW, MH, a, ORG, k=18, fill=0.9, glow=True)
    x, y, w, h = MX + 12, MY + 12, MW - 24, MH - 24
    rrect(c, x, y, w, h, 8, CREAM, a)
    rrect(c, x, y, w, 44, 8, PAPER, a)
    c.drawLine(x, y + 44, x + w, y + 44, paint(LINEW, a, stroke=1.5))
    # "logo": duas montanhas laranja (desenho genérico)
    p = skia.Path(); p.moveTo(x + 16, y + 32); p.lineTo(x + 28, y + 14); p.lineTo(x + 36, y + 24); p.lineTo(x + 42, y + 16)
    p.lineTo(x + 54, y + 32); p.close()
    c.drawPath(p, paint(ORG, a))
    xx = x + 64
    xx += text(c, "FireTrace", xx, y + 30, 21, "bold", TXT, a, align="left") + 18
    xx += text(c, "Wildfire Forensic Analysis", xx, y + 29, 16, "medium", TXT2, a, align="left") + 30
    xx += text(c, "Ridgeview Incident", xx, y + 29, 17, "bold", TXT, a, align="left") + 18
    xx += text(c, "San Gabriel Mountains, CA", xx, y + 29, 16, "medium", TXT2, a, align="left") + 26
    text(c, "14–18 ago 2024", xx, y + 29, 16, "medium", TXT2, a, align="left")
    tx = x + w - 20
    for lab in ("Recursos", "Drones", "Incidente")[::-1][::-1]:
        pass
    for lab in ("Recursos", "Drones", "Incidente"):
        tw = text_w(lab, "semibold", 16) + 26
        tx -= tw
        on = lab == tab
        if on:
            rrect(c, tx, y + 8, tw, 28, 6, "#FFE3D3", a)
        text(c, lab, tx + 13, y + 28, 16, "semibold", ORG if on else TXT2, a, align="left")
        tx -= 8
    return x, y + 44, w, h - 44


def side_card(c, x, y, w, h, a, title=None):
    rrect(c, x, y, w, h, 8, PAPER, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 8, 8), paint(LINEW, a, stroke=1.2))
    if title:
        text(c, title, x + 16, y + 30, 17, "bold", TXT, a, align="left")


def area_chart(c, x, y, w, h, a, title, vals, col=ORG, upto=1.0, unit=""):
    side_card(c, x, y, w, h, a)
    text(c, title, x + 14, y + 26, 15, "semibold", TXT, a, align="left")
    if unit:
        text(c, unit, x + w - 14, y + 26, 14, "medium", TXT2, a, align="right")
    px, py, pw, ph = x + 14, y + 40, w - 28, h - 54
    n = len(vals)
    m = max(vals) * 1.1
    k = max(2, int(n * clamp(upto)))
    pts = [(px + i / (n - 1) * pw, py + ph - vals[i] / m * ph) for i in range(k)]
    p = skia.Path(); p.moveTo(pts[0][0], py + ph)
    for q in pts:
        p.lineTo(*q)
    p.lineTo(pts[-1][0], py + ph); p.close()
    c.drawPath(p, paint(col, 0.25 * a))
    pl = skia.Path(); pl.moveTo(*pts[0]); [pl.lineTo(*q) for q in pts[1:]]
    c.drawPath(pl, paint(col, a, stroke=2.2))
    c.drawLine(px, py + ph, px + pw, py + ph, paint(LINEW, a, stroke=1.2))
    c.drawCircle(*pts[-1], 4, paint(col, a))


def serie(n, fn):
    return [fn(i / (n - 1)) for i in range(n)]


AREA = serie(40, lambda u: 12480 / (1 + math.exp(-10 * (u - 0.35))))
ROS = serie(40, lambda u: 2 + 30 * math.exp(-((u - 0.12) / 0.05) ** 2) + 22 * math.exp(-((u - 0.3) / 0.06) ** 2)
            + 6 * abs(math.sin(u * 23)))
ELEV = serie(40, lambda u: 900 + 900 * u + 180 * math.sin(u * 9) + 90 * math.sin(u * 23))
RETARD = serie(40, lambda u: 312000 * (u ** 1.3) + 9000 * math.sin(u * 30) * u)
LINHA = serie(40, lambda u: 1111 / (1 + math.exp(-12 * (u - 0.25))))
PESS = serie(40, lambda u: 67 if u > 0.18 else 4)

EVENTOS = [(0.03, "Ignição (est.)", "14 ago, 14:26", RED), (0.07, "Crescimento rápido", "14 ago, 16:50", ORG),
           (0.24, "Foco secundário (prov.)", "15 ago, 03:12", AMB), (0.39, "Fogo cruza a crista", "15 ago, 17:48", ORG),
           (0.97, "Contenção (est.)", "18 ago, 11:20", GRN)]


def timeline(c, x, y, w, h, a, pos, t, ev_a=1.0):
    side_card(c, x, y, w, h, a)
    text(c, "Linha do tempo", x + 16, y + 28, 16, "bold", TXT, a, align="left")
    # play
    c.drawCircle(x + 34, y + 62, 16, paint(TXT, a))
    p = skia.Path(); p.moveTo(x + 29, y + 53); p.lineTo(x + 42, y + 62); p.lineTo(x + 29, y + 71); p.close()
    c.drawPath(p, paint(PAPER, a))
    tx0, tx1, ty = x + 70, x + w - 24, y + 62
    c.drawLine(tx0, ty, tx1, ty, paint(LINEW, a, stroke=4, cap_round=True))
    c.drawLine(tx0, ty, lerp(tx0, tx1, pos), ty, paint(ORG, a, stroke=4, cap_round=True))
    for d in range(5):
        xx = lerp(tx0, tx1, d / 4.6)
        text(c, f"{14 + d} ago", xx, ty + 30, 13, "medium", TXT2, a, align="left")
    for f, _, _, col in EVENTOS:
        c.drawCircle(lerp(tx0, tx1, f), ty, 5, paint(col, a * ev_a))
    sx = lerp(tx0, tx1, pos)
    c.drawCircle(sx, ty, 9, paint("#FFFFFF", a)); c.drawCircle(sx, ty, 9, paint(ORG, a, stroke=3))


# ======================================================================  01 — GANCHO
DRONES_UV = [(0.36, 0.62), (0.52, 0.42), (0.44, 0.30), (0.70, 0.55), (0.28, 0.40), (0.62, 0.70)]


def b_gancho(c, t, C, B):
    with cam(c, t, B, 1.0, 1.06):
        ta, tb, tc, td, te = C["01.a"], C["01.b"], C["01.c"], C["01.d"], C["01.e"]
        a0 = ep(t, ta, 0.7)
        dimm = ep(t, te, 0.6)
        x, y, w, h = 150, 205, 1620, 670
        if a0 > 0:
            panel(c, x, y, w, h, a0, ORG, k=20, fill=0.9)
            pf = 0.05 + 0.95 * ep(t, tb, 4.5)
            map_view(c, x + 10, y + 10, w - 20, h - 20, a0, t, pf if t >= tb else 0.0, marks=True)
            # drones
            ad = ep(t, tc, 0.6)
            if ad > 0:
                for k, (u, v) in enumerate(DRONES_UV):
                    ak = ad * ep(t, tc + 0.15 * k, 0.4)
                    px, py = proj(u + 0.02 * math.sin(t * 0.9 + k), v + 0.02 * math.cos(t * 0.9 + k), w - 20, h - 20)
                    gx, gy = x + 10 + px, y + 10 + py - 70
                    c.drawLine(gx, gy, gx, gy + 70, paint("#FFFFFF", 0.4 * ak, stroke=1.5))
                    c.drawCircle(gx, gy, 24, blur_paint(CYAN, 0.4 * ak, 10))
                    c.drawCircle(gx, gy, 20, paint("#0B1426", 0.85 * ak))
                    ic_drone(c, gx, gy, 28, CYAN, ak, t)
                    chip(c, f"FT-0{k + 1}", gx + 28, gy, CYAN, ak, size=15, filled=True)
            ath = ep(t, td, 0.6)
            if ath > 0:
                tw, th = 600, 340
                thermal_cam(c, x + w - tw - 40, y + 40 + (1 - ath) * 20, tw, th, ath, t)
            selo(c, a0, x + w, y - 26)
            if dimm > 0:
                c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint("#03050B", 0.72 * dimm))
        if dimm > 0:
            s = 1 + 0.04 * (1 - dimm)
            glow_text(c, "FIRETRACE", W / 2, 520, 170 * s, "black", INK, dimm, glow=0.3)
            glow_line(c, W / 2 - 480, 568, W / 2 + 480, 568, ORG, dimm, 4, progress=ep(t, te + 0.3, 0.9))
            text(c, "um protótipo · não um produto", W / 2, 640, 40, "mono", "#FFB37A", ep(t, te + 0.6, 0.6))
            chip(c, "FEITO COM CLAUDE OPUS 5.5 · SEGUNDO O AUTOR", W / 2, 730, CYAN, ep(t, te + 1.6, 0.5), anchor="center",
                 size=26, filled=True)


# ======================================================================  02 — O POST
def b_post(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "O POST · 08/10/2026", "QUEM, QUANDO E O QUE DIZ", CYAN)
        a0 = ep(t, C["02.t"], 0.6)
        x, y, w, h = 150, 225, 960, 650
        if a0 > 0:
            panel(c, x, y, w, h, a0, CYAN, label="post no X · recriação do cartão")
            # avatar genérico com iniciais
            c.drawCircle(x + 80, y + 85, 40, paint(VIOLET, a0))
            text_mid(c, "DS", x + 80, y + 85, 30, "black", "#03050B", a0)
            text(c, "Dilum Sanjaya", x + 140, y + 78, 32, "black", INK, a0, align="left")
            text(c, "@DilumSanjaya", x + 140, y + 112, 22, "mono", INK2, a0, align="left")
            aa = ep(t, C["02.a"], 0.5)
            chip(c, "8 OUT 2026", x + w - 40, y + 85, CYAN, aa, anchor="right", size=22)
            ab = ep(t, C["02.b"], 0.5)
            if ab > 0:
                yy = y + 185
                yy += para(c, "Played around with an idea for a wildfire analysis tool", x + 50, yy, 29, "bold", INK,
                           ab, w - 100, 38) + 10
                yy += para(c, "Visualizes wildfire progression over time, tracks hot spots with drones and monitors "
                              "firefighting efforts", x + 50, yy, 29, "bold", INK, ab, w - 100, 38) + 10
                ac = ep(t, C["02.c"], 0.5)
                tw = text(c, "Made with Opus 5.5", x + 50, yy, 29, "bold", INK, ab, align="left")
                if ac > 0:
                    c.drawRect(skia.Rect.MakeXYWH(x + 44, yy - 30, (tw + 12) * ac, 40), paint(CYAN, 0.25 * ac))
                    c.drawLine(x + 44, yy + 10, x + 44 + (tw + 12) * ac, yy + 10, paint(CYAN, ac, stroke=3))
                yy += 50
                c.drawLine(x + 50, yy - 10, x + w - 50, yy - 10, paint(CYAN, 0.25 * ab, stroke=1.5))
                text(c, "tradução:", x + 50, yy + 20, 19, "mono", DIM, ab, align="left")
                para(c, "“Brinquei com uma ideia de ferramenta de análise de incêndios florestais. Mostra o avanço do "
                        "fogo ao longo do tempo, rastreia pontos quentes com drones e acompanha o combate. Feito com o "
                        "Opus 5.5.”", x + 50, yy + 52, 23, "medium", INK2, ab, w - 100, 31)
            ad = ep(t, C["02.d"], 0.5)
            if ad > 0:
                yb = y + h - 50
                chip(c, "VÍDEO 1:55 · SEM ÁUDIO", x + 50, yb, MAGENTA, ad, size=20)
                text(c, "2.284 curtidas · 98 respostas", x + w - 40, yb + 8, 21, "mono", INK2, ad, align="right")
        # linha do tempo à direita
        ax = 1190
        items = [("22/09/2026", "Anthropic lança o Opus 5.5", VIOLET, C["02.t"] + 0.6),
                 ("08/10/2026", "Dilum posta o FireTrace", CYAN, C["02.a"]),
                 ("16/10/2026", "@claudeai destaca o projeto", LIME, C["02.e"])]
        for k, (d, s, col, t0) in enumerate(items):
            a, dy = rise(t, t0)
            if a <= 0:
                continue
            yy = 300 + k * 200 + dy
            if k:
                link(c, ax + 20, yy - 200 + 30, ax + 20, yy - 30, items[k - 1][2], a, t, pulses=2)
            c.drawCircle(ax + 20, yy, 16, blur_paint(col, 0.6 * a, 8)); c.drawCircle(ax + 20, yy, 12, paint(col, a))
            text(c, d, ax + 60, yy - 6, 26, "monob", col, a, align="left")
            text(c, s, ax + 60, yy + 30, 26, "bold", INK, a, align="left")
        ae = ep(t, C["02.e"] + 0.6, 0.5)
        if ae > 0:
            text(c, "“Six projects from the last few weeks", ax + 60, 760, 20, "mono", INK2, ae, align="left")
            text(c, "that caught our attention”", ax + 60, 788, 20, "mono", INK2, ae, align="left")
            text(c, "1º da lista · post no X de @claudeai", ax + 60, 824, 20, "mono", DIM, ae, align="left")


# ======================================================================  03 — TOUR: INCIDENTE
def b_incidente(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "TOUR · ABA INCIDENTE", "O QUE O PROTÓTIPO MOSTRA", ORG)
        ab = ep(t, C["03.s"], 0.5)
        selo(c, ab)
        a0 = ep(t, C["03.a"] - 0.2, 0.6)
        if a0 > 0:
            x, y, w, h = mock_frame(c, a0, "Incidente")
            mw = w - 420
            am = ep(t, C["03.a"], 0.7)  # mapa já aparece com a janela; {d} só destaca o 2D/3D
            # mapa
            if am > 0:
                pf = ep(t, C["03.e"], 6.0)
                map_view(c, x + 12, y + 12, mw, h - 24, am, t, pf if t >= C["03.e"] else 0.0)
                ad3 = ep(t, C["03.d"], 0.5)
                chip(c, "2D", x + mw - 90, y + h - 40, TXT2, ad3, size=16)
                chip(c, "3D", x + mw - 42, y + h - 40, ORG, ad3, size=16, filled=True)
            else:
                rrect(c, x + 12, y + 12, mw, h - 24, 10, "#E7DCCB", a0)
            # visão geral do incidente
            ao = ep(t, C["03.b"], 0.5)
            sx = x + mw + 26
            if ao > 0:
                side_card(c, sx, y + 12, 380, 330, ao, "Visão geral do incidente")
                rows = [("Nome", "Ridgeview Incident"), ("Local", "San Gabriel Mts., CA"), ("Início (est.)", "14 ago 2024, 14:26"),
                        ("Fim", "18 ago 2024, 11:20"), ("Área total", "12.480 acres"), ("Causa (prel.)", "em investigação")]
                for i, (k, v) in enumerate(rows):
                    yy = y + 80 + i * 42
                    text(c, k, sx + 16, yy, 16, "medium", TXT2, ao, align="left")
                    text(c, v, sx + 150, yy, 16, "semibold", TXT, ao, align="left")
            ac = ep(t, C["03.c"], 0.5)
            if ac > 0:
                side_card(c, sx, y + 360, 380, h - 372, ac)
                ic_warn(c, sx + 44, y + 420, 40, AMB, ac)
                text(c, "Parece um cenário", sx + 80, y + 412, 22, "bold", TXT, ac, align="left")
                text(c, "de demonstração", sx + 80, y + 440, 22, "bold", TXT, ac, align="left")
                para(c, "datas e números vêm da tela do vídeo; o autor não diz se são reais", sx + 20, y + 490, 16,
                     "medium", TXT2, ac, 340, 22)


# ======================================================================  04 — TOUR: LINHA DO TEMPO, GRÁFICOS, CAMADAS
CAMADAS = [("Relevo (3D)", True), ("Imagem aérea", True), ("Cicatriz da queimada", True), ("Propagação (modelada)", True),
           ("Probabilidade de ignição", True), ("Linhas de contenção", True)]


def b_tempo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "TOUR · TEMPO E DADOS", "TUDO NA MESMA TELA", ORG)
        selo(c, ep(t, B["start"], 0.5))
        a0 = ep(t, B["start"], 0.5)
        x, y, w, h = mock_frame(c, a0, "Incidente")
        mw = w - 420
        sx = x + mw + 26
        aa = ep(t, C["04.a"], 0.5)
        # posição do "play": anda durante a cena
        pos = 0.03 + 0.94 * clamp((t - C["04.a"]) / max(1, B["end"] - C["04.a"] - 0.5))
        mh = 250
        map_view(c, x + 12, y + 12, mw, mh, a0, t, 0.08 + 0.92 * min(1, pos / 0.45))
        if aa > 0:
            timeline(c, x + 12, y + mh + 24, mw, 96, aa, pos, t, ep(t, C["04.b"], 0.5))
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            # eventos-chave (lista)
            ex, ey = x + 12, y + mh + 132
            for i, (f, s, d, col) in enumerate(EVENTOS):
                ai = ab * ep(t, C["04.b"] + 0.5 + 0.45 * i, 0.4) * (1 - ep(t, C["04.c"], 0.4))
                if ai <= 0:
                    continue
                xx = ex + i * (mw / 5)
                side_card(c, xx, ey, mw / 5 - 10, 92, ai)
                c.drawCircle(xx + 20, ey + 26, 7, paint(col, ai))
                text(c, s, xx + 34, ey + 32, 15, "bold", TXT, ai, align="left")
                text(c, d, xx + 16, ey + 66, 15, "medium", TXT2, ai, align="left")
        acg = ep(t, C["04.c"], 0.5)
        if acg > 0:
            cw = (mw - 20) / 3
            ey = y + mh + 132
            for i, (tit, vals, col, un) in enumerate((("Área queimada", AREA, RED, "acres"), ("Velocidade de avanço", ROS, ORG, "ch/h"),
                                                      ("Perfil de elevação", ELEV, GRN, "ft"))):
                ai = acg * ep(t, C["04.c"] + 0.4 * i, 0.4)
                area_chart(c, x + 12 + i * (cw + 10), ey, cw, h - mh - 144, ai, tit, vals, col, upto=ep(t, C["04.c"] + 0.4 * i, 2.5), unit=un)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            side_card(c, sx, y + 12, 380, 330, ad, "Camadas")
            for i, (s, on) in enumerate(CAMADAS):
                ai = ad * ep(t, C["04.d"] + 0.3 + 0.35 * i, 0.3)
                yy = y + 70 + i * 44
                rrect(c, sx + 16, yy - 15, 20, 20, 4, ORG if on else LINEW, ai)
                if on:
                    pp = skia.Path(); pp.moveTo(sx + 20, yy - 5); pp.lineTo(sx + 25, yy); pp.lineTo(sx + 32, yy - 10)
                    c.drawPath(pp, paint("#FFFFFF", ai, stroke=2.5, cap_round=True))
                text(c, s, sx + 48, yy + 1, 16, "medium", TXT, ai, align="left")
                rrect(c, sx + 280, yy - 8, 80, 6, 3, LINEW, ai)
                rrect(c, sx + 280, yy - 8, 80 * (0.8 + 0.2 * hash01(i)), 6, 3, TXT, ai)
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            side_card(c, sx, y + 360, 380, h - 372, ae, "Clima e comportamento do fogo")
            for i, (k, v) in enumerate((("Vento", "16 km/h SO"), ("Temperatura", "29 °C"), ("Umidade", "22%"))):
                ai = ae * ep(t, C["04.e"] + 0.3 * (i + 1), 0.4)
                xx = sx + 16 + i * 120
                text(c, k, xx, y + 430, 15, "medium", TXT2, ai, align="left")
                text(c, v, xx, y + 462, 20, "bold", TXT, ai, align="left")
            text(c, "valores ilustrativos", sx + 16, y + h - 30, 14, "mono", TXT2, ae, align="left")


# ======================================================================  05 — TOUR: DRONES
FROTA = [("FT-01", "Kestrel", "mapeia o perímetro", "05.a"), ("FT-02", "Harrier", "circula a frente ativa", "05.b"),
         ("FT-03", "Swift", "vigia foco secundário", "05.c"), ("FT-04", "Osprey", "patrulha", "05.d"),
         ("FT-05", "Condor", "levantamento", "05.d"), ("FT-06", "Wren", "retransmite o sinal", "05.d")]


def b_drones(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "TOUR · ABA DRONES", "SEIS DE SEIS NO AR", CYAN)
        a0 = ep(t, B["start"], 0.5)
        selo(c, a0)
        x, y, w, h = mock_frame(c, a0, "Drones")
        mw = w - 420
        sx = x + mw + 26
        map_view(c, x + 12, y + 12, mw, h - 24, a0, t, 0.62, marks=False)
        cur = max([k for k, f in enumerate(FROTA) if t >= C[f[3]]] or [-1])
        if cur >= 3:
            cur = 1  # depois da lista, volta o foco para o FT-02 (câmera)
        # drones no mapa
        for k, (u, v) in enumerate(DRONES_UV):
            ak = a0 * ep(t, C[FROTA[k][3]] if k < 4 else C["05.d"] + 0.3 * (k - 3), 0.5)
            if ak <= 0:
                continue
            ang = t * 0.8 + k
            px, py = proj(u + 0.03 * math.cos(ang), v + 0.03 * math.sin(ang), mw, h - 24)
            gx, gy = x + 12 + px, y + 12 + py - 50
            col = CYAN if k != cur else ORG
            c.drawCircle(gx, gy, 22, paint("#0B1426", 0.85 * ak))
            ic_drone(c, gx, gy, 26, col, ak, t)
            chip(c, FROTA[k][0], gx + 26, gy, col, ak, size=14, filled=True)
        # frota (lista)
        side_card(c, sx, y + 12, 380, 330, a0, "Frota de drones")
        text(c, "6 de 6 no ar", sx + 364, y + 42, 15, "semibold", ORG, ep(t, C["05.t"], 0.5), align="right")
        for k, (cod, nome, fun, cue) in enumerate(FROTA):
            ak = a0 * ep(t, C[cue] + (0.3 * (k - 3) if k >= 3 else 0), 0.4)
            if ak <= 0:
                continue
            yy = y + 82 + k * 44
            if k == cur:
                rrect(c, sx + 8, yy - 26, 364, 38, 6, "#FFE3D3", ak)
            ic_drone(c, sx + 30, yy - 7, 22, ORG if k == cur else TXT2, ak, t)
            text(c, f"{cod} {nome}", sx + 52, yy, 16, "bold", TXT, ak, align="left")
            text(c, fun, sx + 200, yy, 15, "medium", TXT2, ak, align="left")
        # câmera IR
        ae = ep(t, C["05.e"], 0.6)
        if ae > 0:
            thermal_cam(c, x + mw - 640, y + 30, 620, 360, ae, t, show_hot=t >= C["05.f"])
            # telemetria (cartão)
            side_card(c, sx, y + 360, 380, h - 372, ae, "FT-02 Harrier · telemetria")
            for i, (k, v) in enumerate((("Altitude", "580 ft"), ("Velocidade", "22 kt"), ("Bateria", "73%"))):
                xx = sx + 16 + i * 120
                text(c, k, xx, y + 430, 15, "medium", TXT2, ae, align="left")
                text(c, v, xx, y + 462, 22, "bold", TXT, ae, align="left")
        af = ep(t, C["05.f"], 0.5)
        if af > 0:
            rrect(c, sx + 16, y + 490, 348, 40, 6, "#FFE3D3", af)
            c.drawCircle(sx + 36, y + 510, 7, paint(RED, af))
            text(c, "Hot spot · 983 °C", sx + 52, y + 516, 17, "bold", TXT, af, align="left")
            text(c, "04:00", sx + 350, y + 516, 15, "medium", TXT2, af, align="right")


# ======================================================================  06 — TOUR: RECURSOS
RECURSOS = [("AERONAVES", None, "06.a"), ("T-910", "DC-10 · avião-tanque", "06.a"), ("T-131", "C-130Q · avião-tanque", "06.a"),
            ("T-162", "RJ85 · avião-tanque", "06.a"), ("H-743", "S-64 Air-Crane · helicóptero", "06.b"),
            ("H-531", "Bell 205 · helicóptero", "06.b"), ("AA-52", "King Air · coordenação aérea", "06.b"),
            ("EM SOLO", None, "06.c"), ("E-31/32/45", "caminhões", "06.c"), ("WT-12", "caminhão-tanque", "06.c"),
            ("C-7 · C-14", "equipes em solo", "06.c"), ("DZ-4", "trator", "06.c")]
LOG = [("T-910", "9.400 gal retardante", "17:14"), ("H-531", "324 gal água", "17:32"), ("T-131", "4.000 gal retardante", "17:53"),
       ("H-743", "2.650 gal água", "18:08")]


def b_recursos(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "TOUR · ABA RECURSOS", "13 UNIDADES EM CAMPO", GOLD)
        a0 = ep(t, B["start"], 0.5)
        selo(c, a0)
        x, y, w, h = mock_frame(c, a0, "Recursos")
        mw = w - 420
        sx = x + mw + 26
        mh = 330
        af = ep(t, C["06.f"], 0.6)
        map_view(c, x + 12, y + 12, mw, mh, a0, t, 0.85, marks=False)
        # rota do avião sobre o mapa
        pts = [proj(lerp(0.15, 0.85, k / 20), 0.55 - 0.25 * math.sin(k / 20 * math.pi), mw, mh) for k in range(21)]
        ap = ep(t, C["06.a"], 0.6)
        if ap > 0:
            c.save(); clip_rr(c, x + 12, y + 12, mw, mh, 10)
            pa = paint("#FFFFFF", 0.7 * ap, stroke=2); pa.setPathEffect(skia.DashPathEffect.Make([8, 6], -t * 30))
            pp = skia.Path(); pp.moveTo(x + 12 + pts[0][0], y + 12 + pts[0][1] - 60)
            for px, py in pts[1:]:
                pp.lineTo(x + 12 + px, y + 12 + py - 60)
            c.drawPath(pp, pa)
            u = ((t - C["06.a"]) * 0.08) % 1.0
            i = min(19, int(u * 20)); f = u * 20 - i
            px = lerp(pts[i][0], pts[i + 1][0], f); py = lerp(pts[i][1], pts[i + 1][1], f)
            ang = math.degrees(math.atan2(pts[i + 1][1] - pts[i][1], pts[i + 1][0] - pts[i][0])) + 90
            ic_plane(c, x + 12 + px, y + 12 + py - 60, 46, "#FFFFFF", ap, ang)
            chip(c, "T-910", x + 12 + px + 30, y + 12 + py - 60, ORG, ap, size=14, filled=True)
            c.restore()
        if af > 0:
            # câmera de perseguição: quadro escurecido com o avião grande
            cx0, cy0, cw0, ch0 = x + 12 + mw - 470, y + 24, 450, 250
            c.save(); clip_rr(c, cx0, cy0, cw0, ch0, 8)
            pa = skia.Paint(AntiAlias=True); pa.setAlphaf(af)
            c.save(); c.translate(cx0 - 200, cy0 - 60); c.scale(1.6, 1.6)
            c.drawImage(terrain_img(int(mw), int(mh)), 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear), pa)
            c.restore()
            c.drawRect(skia.Rect.MakeXYWH(cx0, cy0, cw0, ch0), paint("#000000", 0.25 * af))
            ic_plane(c, cx0 + cw0 / 2, cy0 + ch0 / 2 + 6 * math.sin(t * 2), 140, "#F4F1EA", af, 80)
            c.restore()
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx0, cy0, cw0, ch0), 8, 8), paint(ORG, af, stroke=3))
            chip(c, "PERSEGUIÇÃO", cx0 + 14, cy0 + 26, ORG, af, size=15, filled=True)
            chip(c, "CABINE", cx0 + 170, cy0 + 26, TXT2, af, size=15)
        # gráficos e registro
        ad = ep(t, C["06.d"], 0.5)
        ey = y + mh + 24
        eh = h - mh - 36
        if ad > 0:
            side_card(c, x + 12, ey, 400, eh, ad, "Registro de lançamentos")
            for i, (u_, s, hh) in enumerate(LOG):
                ai = ad * ep(t, C["06.d"] + 0.3 * i, 0.3)
                yy = ey + 66 + i * 44
                c.drawCircle(x + 34, yy - 6, 6, paint(RED if "ret" in s else "#3B7BD9", ai))
                text(c, f"{u_} · {s}", x + 50, yy, 16, "semibold", TXT, ai, align="left")
                text(c, hh, x + 396, yy, 15, "medium", TXT2, ai, align="right")
        ae = ep(t, C["06.e"], 0.5)
        if ae > 0:
            cw = (mw - 420) / 3
            for i, (tit, vals, col, un) in enumerate((("Retardante lançado", RETARD, RED, "gal"),
                                                      ("Linha construída", LINHA, TXT, "chains"),
                                                      ("Pessoal em campo", PESS, GRN, "pessoas"))):
                ai = ae * ep(t, C["06.e"] + 0.4 * i, 0.4)
                area_chart(c, x + 422 + i * (cw + 10) - 10 * i + 10 * i, ey, cw - 6, eh, ai, tit, vals, col,
                           upto=ep(t, C["06.e"] + 0.4 * i, 2.5), unit=un)
        # lista de recursos
        side_card(c, sx, y + 12, 380, h - 24, a0)
        text(c, "Recursos", sx + 16, y + 42, 17, "bold", TXT, a0, align="left")
        text(c, "13 unidades", sx + 364, y + 42, 15, "semibold", ORG, ep(t, C["06.t"], 0.5), align="right")
        yy = y + 80
        for nm, desc, cue in RECURSOS:
            ai = a0 * ep(t, C[cue], 0.4)
            if desc is None:
                text(c, nm, sx + 16, yy, 13, "bold", TXT2, ai, align="left", tracking=1)
                yy += 30
                continue
            text(c, nm, sx + 16, yy, 15, "bold", TXT, ai, align="left")
            text(c, desc, sx + 150, yy, 15, "medium", TXT2, ai, align="left")
            yy += 36


# ======================================================================  07 — COMO SE CONSTRÓI (hipótese)
NAO_CONTOU = [("tempo gasto", "07.a"), ("pedidos (prompts)", "07.a"), ("bibliotecas", "07.a"), ("código / demo", "07.a")]
LAYERS = [("DADOS", "perímetros por hora · drones · retardante", "num protótipo: simulados", "07.c", VIOLET),
          ("MAPA 3D", "relevo a partir de um modelo de elevação", "tipicamente WebGL (ex.: three.js)", "07.d", CYAN),
          ("LINHA DO TEMPO", "relógio que controla tudo", "play · arrastar · eventos", "07.e", MAGENTA),
          ("PAINÉIS", "gráficos · listas · câmera", "componentes de interface", "07.f", LIME)]


def b_camadas(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "COMO SE CONSTRÓI", "AS CAMADAS DE UM APP ASSIM", VIOLET)
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            panel(c, 150, 250, 520, 600, aa, ROSE, label="o que ele não contou")
            for i, (s, cue) in enumerate(NAO_CONTOU):
                ai = aa * ep(t, C["07.a"] + 0.6 + 0.5 * i, 0.4)
                yy = 360 + i * 110
                c.drawCircle(220, yy - 10, 26, paint(ROSE, 0.15 * ai)); c.drawCircle(220, yy - 10, 26, paint(ROSE, ai, stroke=2.5))
                text_mid(c, "?", 220, yy - 10, 32, "black", ROSE, ai)
                text(c, s, 270, yy, 32, "bold", INK, ai, align="left")
            text(c, "nada disso foi publicado", 410, 815, 22, "mono", ROSE, ep(t, C["07.a"] + 2.6, 0.5))
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            chip(c, "HIPÓTESE · COMO APPS ASSIM COSTUMAM SER FEITOS", 1770, 215, GOLD, ab, anchor="right", size=20, filled=True)
        # pilha de camadas (de baixo para cima)
        for i, (nm, d1, d2, cue, col) in enumerate(LAYERS):
            a, dy = rise(t, C[cue], 0.6, 40)
            if a <= 0:
                continue
            yy = 740 - i * 140 + dy
            x0, wl = 730, 1040
            # placa em perspectiva
            p = skia.Path()
            p.moveTo(x0 + 40, yy - 40); p.lineTo(x0 + wl, yy - 40); p.lineTo(x0 + wl - 40, yy + 60); p.lineTo(x0, yy + 60); p.close()
            c.drawPath(p, blur_paint(col, 0.25 * a, 18))
            c.drawPath(p, paint(PANEL, 0.92 * a))
            c.drawPath(p, paint(col, a, stroke=2.5))
            glow_text(c, nm, x0 + 60, yy + 22, 36, "black", col, a, align="left", glow=0.35)
            text(c, d1, x0 + 440, yy + 6, 23, "bold", INK, a, align="left")
            text(c, d2, x0 + 440, yy + 38, 20, "mono", INK2, a, align="left")
            if i:
                link(c, x0 + wl / 2, yy + 100, x0 + wl / 2, yy + 62, LAYERS[i - 1][4], a, t, pulses=2)


# ======================================================================  08 — UM RELÓGIO SÓ
SYNC = [("PERÍMETRO NO MAPA", "08.c", ORG, (470, 380)), ("DRONES", "08.d", CYAN, (1450, 380)),
        ("GRÁFICOS", "08.e", LIME, (470, 700)), ("EVENTOS", "08.e", MAGENTA, (1450, 700))]


def b_relogio(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "O SEGREDO", "UM RELÓGIO SÓ", CYAN)
        aa = ep(t, C["08.a"], 0.6)
        cx, cy = W / 2, 540
        tb = C["08.b"]
        sl = 0.15 + 0.85 * (1 - abs(((t - tb) / 5.0) % 2 - 1)) if t > tb else 0.15
        if aa > 0:
            node(c, cx, cy, 120, None, None, CYAN, aa, t)
            ic_clock(c, cx, cy, 62, CYAN, aa, t if t > tb else 0)
            # slider
            ab = ep(t, tb, 0.5)
            if ab > 0:
                x0, x1, yy = cx - 260, cx + 260, cy + 190
                c.drawLine(x0, yy, x1, yy, paint(DIM, ab, stroke=5, cap_round=True))
                c.drawLine(x0, yy, lerp(x0, x1, sl), yy, paint(CYAN, ab, stroke=5, cap_round=True))
                c.drawCircle(lerp(x0, x1, sl), yy, 14, paint(INK, ab))
                text(c, "arraste a linha do tempo", cx, yy + 50, 24, "mono", INK2, ab)
        for nm, cue, col, (nx, ny) in SYNC:
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            link(c, cx + (nx - cx) * 0.22, cy + (ny - cy) * 0.22, nx + (cx - nx) * 0.3, ny + (cy - ny) * 0.3, col, a, t, pulses=3)
            panel(c, nx - 210, ny - 95, 420, 190, a, col, k=16, fill=0.9)
            text(c, nm, nx, ny - 50, 24, "monob", col, a)
            # mini-visual que muda com o slider
            if nm.startswith("PER"):
                pts = fire_poly(max(0.05, sl))
                fx = lambda u: nx - 180 + (u - 0.15) / 0.7 * 360
                fy = lambda v: ny - 25 + (v - 0.1) / 0.8 * 115
                p = skia.Path(); p.moveTo(fx(pts[0][0]), fy(pts[0][1]))
                for u, v in pts[1:]:
                    p.lineTo(fx(u), fy(v))
                p.close()
                c.drawPath(p, paint(RED, 0.5 * a)); c.drawPath(p, paint(ORG, a, stroke=2))
            elif nm == "DRONES":
                for k in range(6):
                    ang = sl * 6 + k
                    ic_drone(c, nx - 150 + k * 60, ny + 20 + 18 * math.sin(ang), 26, col, a, t)
            elif nm == "GRÁFICOS":
                n = len(AREA)
                k = max(2, int(n * sl))
                p = skia.Path(); p.moveTo(nx - 160, ny + 70)
                for i in range(k):
                    p.lineTo(nx - 160 + i / (n - 1) * 320, ny + 70 - AREA[i] / 12480 * 100)
                p.lineTo(nx - 160 + (k - 1) / (n - 1) * 320, ny + 70); p.close()
                c.drawPath(p, paint(col, 0.3 * a))
            else:
                for i, (f, s, d, cc) in enumerate(EVENTOS[:3]):
                    on = sl >= f * 2
                    text(c, ("> " if on else "  ") + s, nx - 170, ny - 4 + i * 30, 19, "mono", INK if on else DIM, a, align="left")
        af = ep(t, C["08.f"], 0.5)
        if af > 0:
            chip(c, "MUITAS PEÇAS CONVERSANDO ENTRE SI", cx, 255, GOLD, af, anchor="center", size=22, filled=True)


# ======================================================================  09 — OPUS 5.5
OPUS = [("09.a", "LANÇADO", "22 de setembro de 2026", CYAN),
        ("09.b", "NÍVEL", "do Claude Fable 5.1 na maior parte do trabalho", VIOLET),
        ("09.c", "CUSTO", "cerca de 40% menor que o do Opus 5", LIME),
        ("09.d", "DESTAQUE", "tarefas longas e extensas", MAGENTA),
        ("09.e", "TESTE DE JOGO", "maior nota em gráficos e acabamento", GOLD)]


def b_opus(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "O MODELO", "CLAUDE OPUS 5.5", VIOLET)
        a0 = ep(t, C["09.t"], 0.6)
        if a0 > 0:
            node(c, 400, 470, 150, None, None, VIOLET, a0, t)
            glow_text(c, "OPUS", 400, 465, 64, "black", VIOLET, a0, glow=0.5)
            glow_text(c, "5.5", 400, 530, 56, "black", INK, a0, glow=0.3)
            text(c, "segundo a Anthropic", 400, 690, 24, "mono", INK2, a0)
        for i, (cue, k, v, col) in enumerate(OPUS):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 240 + i * 100 + dy
            panel(c, 700, y, 1070, 86, a, col, k=12, fill=0.85, glow=False)
            text(c, k, 735, y + 54, 22, "monob", col, a, align="left")
            text(c, v, 960, y + 55, 28, "bold", INK, a, align="left")
        af = ep(t, C["09.f"], 0.5)
        if af > 0:
            panel(c, 150, 760, 1620, 90, af, GOLD, k=12, fill=0.9)
            ic_warn(c, 210, 805, 44, GOLD, af)
            text(c, "o vídeo não mostra: quantas tentativas · quanto ajuste manual", 260, 815, 30, "bold", INK, af, align="left")
        fonte(c, "anthropic.com/news/claude-opus-5-5 · 22/09/2026", ep(t, C["09.a"], 0.5), 885)


# ======================================================================  10 — MUNDO REAL
REAL = [("10.a", "SATÉLITE", "NASA FIRMS", "focos de fogo ativo por satélite em até 3\u00a0h após a observação", CYAN, "sat"),
        ("10.b", "AVIÃO IR", "voos noturnos (EUA)", "perímetro de calor atualizado 1 vez a cada 24\u00a0h (NIROPS)", VIOLET, "plane"),
        ("10.c", "DRONE TÉRMICO", "através da fumaça", "foco de 5\u00a0x\u00a05\u00a0cm a ~800\u00a0m, segundo o Forest Service", ORG, "drone"),
        ("10.d", "BRASIL", "INPE · Queimadas", "200+ imagens de satélite por dia para achar focos de calor", LIME, "flame")]


def b_real(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "O MUNDO REAL", "COMO SE ACOMPANHA UM INCÊNDIO", LIME)
        for i, (cue, k, s1, s2, col, ic) in enumerate(REAL):
            a, dy = rise(t, C[cue], 0.6, 30)
            if a <= 0:
                continue
            x, y, w, h = 150 + i * 412, 250 + dy, 388, 580
            panel(c, x, y, w, h, a, col, k=18, label=k)
            cx, cy = x + w / 2, y + 170
            c.drawCircle(cx, cy, 86, blur_paint(col, 0.25 * a, 20))
            c.drawCircle(cx, cy, 80, paint(PANEL, a)); c.drawCircle(cx, cy, 80, paint(col, a, stroke=3))
            if ic == "sat":
                ic_sat(c, cx, cy - 10, 120, col, a)
            elif ic == "plane":
                c.drawCircle(cx + 36, cy - 36, 16, paint(INK2, 0.8 * a))
                c.drawCircle(cx + 44, cy - 42, 14, paint(PANEL, a))
                ic_plane(c, cx - 6, cy + 6, 96, col, a, 60)
            elif ic == "drone":
                ic_drone(c, cx, cy, 100, col, a, t)
            else:
                ic_flame(c, cx, cy, 110, col, a)
            text(c, s1, cx, y + 330, 30, "black", INK, a)
            para(c, s2, x + 34, y + 390, 25, "medium", INK2, a, w - 68, 34, align="left")
        fonte(c, "NASA Earthdata · USDA Forest Service · INPE — links na descrição", ep(t, C["10.a"], 0.5), 885)


# ======================================================================  11 — PROTÓTIPO × SISTEMA REAL
COMP = [("11.a", "DADOS", "de demonstração", "sensores, satélites, equipes"),
        ("11.b", "ATRASO", "não importa", "minutos contam"),
        ("11.c", "VALIDAÇÃO", "nenhuma mostrada", "testes em campo"),
        ("11.d", "RESPONSÁVEL", "não se aplica", "equipe que responde pelas decisões")]


def b_compara(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "A DISTÂNCIA", "PROTÓTIPO × SISTEMA REAL", GOLD)
        a0 = ep(t, C["11.t"] + 0.5, 0.6)
        if a0 > 0:
            panel(c, 560, 230, 560, 620, a0, ORG, label="protótipo (vídeo)")
            panel(c, 1170, 230, 600, 620, a0, LIME, label="sistema real")
        for i, (cue, k, p1, p2) in enumerate(COMP):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 330 + i * 130 + dy
            text(c, k, 150, y + 10, 30, "monob", GOLD, a, align="left")
            check_icon(c, 610, y, 20, a, ROSE, kind="x")
            text(c, p1, 645, y + 11, 30, "bold", INK2, a, align="left")
            check_icon(c, 1220, y, 20, a, LIME)
            for j, ln in enumerate(wrap(p2, "bold", 30, 500)):
                text(c, ln, 1255, y + 11 + j * 36, 30, "bold", INK, a, align="left")


# ======================================================================  12 — LIMITES / CUIDADOS
LIM = [("12.a", "só existe em vídeo", "sem código, sem demo para testar"),
       ("12.b", "dados reais ou simulados?", "o autor não diz"),
       ("12.c", "“feito com Opus 5.5”", "é a palavra dele · intervenção manual desconhecida"),
       ("12.d", "destaque da @claudeai", "é vitrine, não avaliação independente")]


def b_limites(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "CUIDADOS", "O QUE O POST NÃO PROVA", GOLD)
        for i, (cue, s, sub) in enumerate(LIM):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 245 + i * 150 + dy
            panel(c, 150, y, 1620, 126, a, GOLD, k=14, fill=0.85, glow=False)
            ic_warn(c, 230, y + 63, 64, GOLD, a)
            text(c, s, 310, y + 56, 36, "black", INK, a, align="left")
            text(c, sub, 310, y + 98, 26, "mono", INK2, a, align="left")
        fonte(c, "verificado em dilum.dev e no post em 23/10/2026", ep(t, C["12.a"], 0.5), 880)


# ======================================================================  13 — RESUMO
RES = [("13.a", "protótipo de análise de incêndios · Dilum Sanjaya · 08/10/2026", CYAN),
       ("13.b", "mapa 3D + linha do tempo + drones + recursos, sincronizados", ORG),
       ("13.c", "“feito com Opus 5.5”, mas sem mostrar como", VIOLET),
       ("13.d", "o mundo real já usa satélites, aviões e drones com dados validados", LIME),
       ("13.e", "ótima ideia ilustrada, não uma ferramenta pronta", GOLD)]


def b_resumo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "RESUMO", "FIRETRACE EM 5 PONTOS", CYAN)
        for i, (cue, s, col) in enumerate(RES):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 245 + i * 120 + dy
            panel(c, 150, y, 1620, 100, a, col, k=14, fill=0.85, glow=False)
            check_icon(c, 220, y + 50, 26, a, col)
            fs = 34 if text_w(s, "bold", 34) < 1420 else 30
            text(c, s, 280, y + 62, fs, "bold", INK, a, align="left")


# ======================================================================  CTA + FONTES
def b_cta(c, t, C, B):
    head(c, t, B["start"], "TECH//011", "OBRIGADO POR ASSISTIR", CYAN)
    cta(c, t, C["14.like"], C["14.sub"], C["14.bell"], C["14.com"], C["14.bye"],
        "Que ferramenta você tentaria criar com uma IA dessas?")


FONTES = [
    ("Dilum Sanjaya (X)", "post original · x.com/DilumSanjaya/status/2108241054298415258", "08/10/2026"),
    ("Claude (X, oficial)", "Six projects... · x.com/claudeai/status/2111177834127601902", "16/10/2026"),
    ("Anthropic", "Introducing Claude Opus 5.5 · anthropic.com/news/claude-opus-5-5", "22/09/2026"),
    ("P. Pillitteri", "Claude revela protótipo sobre incêndios florestais (análise)", "17/10/2026"),
    ("NASA Earthdata", "FIRMS · earthdata.nasa.gov/data/tools/firms", "acesso 23/10"),
    ("USFS / NIFC", "Fire Imaging Technologies Users Guide (NIROPS) · nifc.gov", "fev/2020"),
    ("USDA Forest Service", "Mechanized birds: wildland firefighting drone intelligence", "03/10/2022"),
    ("INPE", "Programa Queimadas · perguntas frequentes · data.inpe.br/queimadas", "acesso 23/10"),
]


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "CRÉDITOS", "FONTES", CYAN)
    a0 = ep(t, B["start"] + 0.2, 0.6)
    panel(c, 150, 230, 1620, 600, a0, CYAN, label="consultadas em 23/10/2026")
    for i, (v, tit, d) in enumerate(FONTES):
        a = ep(t, B["start"] + 0.4 + 0.12 * i, 0.4)
        y = 300 + i * 62
        text(c, v, 200, y, 26, "extrabold", CYAN, a, align="left")
        tt = tit if text_w(tit, "medium", 24) < 1000 else wrap(tit, "medium", 24, 960)[0] + "…"
        text(c, tt, 520, y, 24, "medium", INK, a, align="left")
        text(c, d, 1720, y, 24, "mono", INK2, a, align="right")
    ab = ep(t, B["start"] + 1.8, 0.6)
    text(c, "interface do FireTrace: recriação ilustrativa nossa · nenhum quadro do vídeo original · narração com voz sintética (IA)",
         W / 2, 870, 20, "mono", DIM, ab)


BLOCKS = dict(gancho=b_gancho, post=b_post, incidente=b_incidente, tempo=b_tempo, drones=b_drones, recursos=b_recursos,
              camadas=b_camadas, relogio=b_relogio, opus=b_opus, real=b_real, compara=b_compara, limites=b_limites,
              resumo=b_resumo, cta=b_cta, fontes=b_fontes)
