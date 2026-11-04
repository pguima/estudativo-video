"""Cena-teste de estilo "ilustração vetorial com brilho" (tipo documentário animado):
célula saudável se divide -> mutação -> célula com câncer se divide sem parar.

    python3 cena.py --still 3.0,9.5,13.5      # quadros de conferência em stills/
    python3 cena.py --video --jobs 4          # final/teste_celula_cancer.mp4
"""
import argparse
import math
import random
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import skia

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
import motor  # noqa: E402

W, H, FPS = 1920, 1080, 30
DUR = 15.0


# ---------------- utilidades ----------------
def col(h, a=1.0):
    return motor.hexc(h, a)


def mixc(c1, c2, f):
    return motor.mix(c1, c2, max(0.0, min(1.0, f)))


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def seg(t, t0, t1):
    return ease((t - t0) / (t1 - t0))


def smooth_path(pts):
    """Curva fechada suave (Catmull-Rom -> Bézier cúbica)."""
    n = len(pts)
    p = skia.Path()
    p.moveTo(*pts[0])
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        p.cubicTo(*c1, *c2, *p2)
    p.close()
    return p


def blob(cx, cy, r, t, seed, amp=0.035, n=40, sx=1.0, sy=1.0, rot=0.0):
    """Contorno orgânico que 'respira'."""
    rnd = random.Random(seed)
    harm = [(k, amp * rnd.uniform(0.5, 1.2), rnd.uniform(0, 6.28), rnd.uniform(0.6, 1.4)) for k in (2, 3, 5)]
    pts = []
    cr, sr = math.cos(rot), math.sin(rot)
    for i in range(n):
        th = 2 * math.pi * i / n
        rr = r * (1 + sum(a * math.sin(k * th + ph + w * t) for k, a, ph, w in harm))
        x, y = math.cos(th) * rr * sx, math.sin(th) * rr * sy
        pts.append((cx + x * cr - y * sr, cy + x * sr + y * cr))
    return smooth_path(pts)


def glow(c, x, y, r, color, a, sigma=None):
    p = skia.Paint(AntiAlias=True, Color=col(color, a))
    p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, sigma or r * 0.45))
    p.setBlendMode(skia.BlendMode.kScreen)
    c.drawCircle(x, y, r, p)


def fill(c, path, color, a=1.0):
    c.drawPath(path, skia.Paint(AntiAlias=True, Color=col(color, a)))


def shifted(path, dx, dy, s=1.0, cx=0.0, cy=0.0):
    m = skia.Matrix()
    m.setTranslate(dx, dy)
    if s != 1.0:
        m.preScale(s, s, cx, cy)
    out = skia.Path(path)
    out.transform(m)
    return out


# ---------------- paletas ----------------
SAUDAVEL = dict(dark="#1E4FB8", main="#3A93F2", light="#9BE7FF",
                nuc_dark="#16307E", nuc="#2B5BD0", nuc_light="#6FA2FF", glow="#3A93F2", core=None)
CANCER = dict(dark="#8E1257", main="#E2337E", light="#FF9BCB",
              nuc_dark="#C2185B", nuc="#FF5A3C", nuc_light="#FFE066", glow="#FF2E88", core="#FFE680")
FUNDO = ("#140C3A", "#07061A")


TEAL = dict(dark="#14649A", main="#2FB2E0", light="#A6F3FF", nuc_dark="#123F84", nuc="#2367C8",
            nuc_light="#74C4FF", glow="#2FB2E0", core=None)
ANIL = dict(dark="#2A3AA8", main="#4F7BEA", light="#B4CCFF", nuc_dark="#1D237A", nuc="#3446B8",
            nuc_light="#8D9DFF", glow="#4F7BEA", core=None)


def tom_pal(v):
    alvo = TEAL if v > 0 else ANIL
    return {k: (mixc(SAUDAVEL[k], alvo[k], abs(v)) if SAUDAVEL[k] else None) for k in SAUDAVEL}


def pal_mix(f):
    out = {}
    for k in SAUDAVEL:
        a, b = SAUDAVEL[k], CANCER[k]
        if a is None or b is None:
            out[k] = b if f > 0.5 else a
        else:
            out[k] = mixc(a, b, f)
    return out


def draw_cell(c, path, cx, cy, r, t, seed, pal, heat=0.0, nuc_split=0.0, axis=0.0, nucleo=True):
    """Célula estilo vetor: sombra embaixo-direita, borda iluminada em cima-esquerda,
    núcleo com brilho próprio quando heat > 0."""
    if heat > 0:
        glow(c, cx, cy, r * 1.35, pal["glow"], 0.55 * heat)
    c.save()
    c.clipPath(path, doAntiAlias=True)
    fill(c, path, pal["dark"])
    fill(c, shifted(path, -0.09 * r, -0.11 * r), pal["light"])
    fill(c, shifted(path, -0.02 * r, -0.03 * r, 0.9, cx, cy), pal["main"])
    # organelas (pontinhos translúcidos)
    rnd = random.Random(seed * 7 + 1)
    for _ in range(6):
        ang, dist = rnd.uniform(0, 6.28), rnd.uniform(0.45, 0.72) * r
        ox = cx + math.cos(ang + 0.15 * math.sin(t * 0.7 + seed)) * dist
        oy = cy + math.sin(ang + 0.15 * math.sin(t * 0.7 + seed)) * dist
        c.drawCircle(ox, oy, r * rnd.uniform(0.05, 0.09), skia.Paint(AntiAlias=True, Color=col(pal["light"], 0.28)))
    if not nucleo:
        c.restore()
        return
    # núcleo(s)
    nr = r * 0.4
    ux, uy = math.cos(axis), math.sin(axis)
    sep = nr * 1.15 * ease(nuc_split)
    nucs = [(cx + 0.06 * r, cy + 0.05 * r)] if nuc_split <= 0 else \
        [(cx + 0.06 * r + ux * sep, cy + 0.05 * r + uy * sep), (cx + 0.06 * r - ux * sep, cy + 0.05 * r - uy * sep)]
    nrr = nr * (1 - 0.25 * ease(nuc_split))
    for j, (nx, ny) in enumerate(nucs):
        npath = blob(nx, ny, nrr, t * 1.3, seed * 13 + j, amp=0.05)
        if heat > 0:
            glow(c, nx, ny, nrr * 1.6, pal["nuc_light"], 0.8 * heat)
        fill(c, npath, pal["nuc_dark"])
        fill(c, shifted(npath, -0.12 * nrr, -0.12 * nrr), pal["nuc_light"] if heat <= 0 else pal["nuc"])
        fill(c, shifted(npath, -0.03 * nrr, -0.03 * nrr, 0.86, nx, ny), pal["nuc"])
        if heat > 0 and pal["core"]:
            # núcleo incandescente
            pc = skia.Paint(AntiAlias=True)
            pc.setShader(skia.GradientShader.MakeRadial(
                (nx - 0.1 * nrr, ny - 0.1 * nrr), nrr * 0.75,
                [col(pal["core"], heat), col(pal["nuc_light"], 0.85 * heat), col(pal["nuc"], 0)]))
            c.drawCircle(nx, ny, nrr * 0.9, pc)
        c.drawCircle(nx - 0.32 * nrr, ny - 0.34 * nrr, nrr * 0.14,
                     skia.Paint(AntiAlias=True, Color=col("#FFFFFF", 0.55)))
    c.restore()


# ---------------- mundo ----------------
R_H = 82          # célula saudável
R_C = 70          # célula com câncer
N_LEAF = 32
T_MUT = 8.3       # mutação
T_DIV = [9.4, 10.35, 11.15, 11.85, 12.45]   # gerações de divisão do tumor
DIV_D = 0.75      # duração de cada divisão
A_T0, A_T1 = 4.7, 6.8   # divisão normal (demonstração)


def build_world():
    rnd = random.Random(7)
    sp = 188
    cells = []
    row = 0
    for y in np.arange(-1250, 1251, sp * 0.866):
        for x in np.arange(-1900, 1901, sp):
            xx = x + (sp / 2 if row % 2 else 0) + rnd.uniform(-16, 16)
            yy = y + rnd.uniform(-14, 14)
            cells.append(dict(x=xx, y=yy, r=R_H * rnd.uniform(0.9, 1.06), seed=len(cells) + 3,
                              rot=rnd.uniform(0, 6.28), sx=rnd.uniform(0.96, 1.07),
                              tom=rnd.choice([0.0, 0.0, 0.0, 0.35, 0.6, -0.4])))
        row += 1
    # célula que vira câncer: a mais próxima da origem; a que se divide normalmente: perto de (-430, -60)
    foco = min(cells, key=lambda q: q["x"] ** 2 + q["y"] ** 2)
    cells.remove(foco)
    for q in cells:
        q["x"] -= foco["x"]
        q["y"] -= foco["y"]
    demo = min(cells, key=lambda q: (q["x"] + 470) ** 2 + (q["y"] + 40) ** 2)
    cells.remove(demo)

    # tumor: posições finais em girassol, árvore binária por cortes alternados
    golden = math.pi * (3 - math.sqrt(5))
    d = 2 * R_C * 0.93
    leaves = [(d * 0.53 * math.sqrt(i + 0.5) * math.cos(i * golden),
               d * 0.53 * math.sqrt(i + 0.5) * math.sin(i * golden)) for i in range(N_LEAF)]

    def node(pts, gen, seed):
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        nd = dict(x=cx, y=cy, gen=gen, seed=seed, kids=[])
        if len(pts) > 1:
            ang = rnd.uniform(0, math.pi) if gen == 0 else rnd.uniform(0, math.pi)
            ux, uy = math.cos(ang), math.sin(ang)
            pts = sorted(pts, key=lambda p: p[0] * ux + p[1] * uy)
            h = len(pts) // 2
            nd["t"] = T_DIV[gen] + rnd.uniform(-0.12, 0.18)
            nd["kids"] = [node(pts[:h], gen + 1, seed * 2 + 1), node(pts[h:], gen + 1, seed * 2 + 2)]
        return nd

    tumor = node(leaves, 0, 1)

    rb = random.Random(11)
    bokeh = [dict(x=rb.uniform(-2600, 2600), y=rb.uniform(-1600, 1600), r=rb.uniform(90, 230),
                  c=rb.choice(["#3A2A8F", "#5B2BA0", "#1F3E9E", "#7A2A8F"]), a=rb.uniform(0.25, 0.5),
                  ph=rb.uniform(0, 6.28)) for _ in range(46)]
    motes = [dict(x=rb.uniform(-2200, 2200), y=rb.uniform(-1400, 1400), r=rb.uniform(2.5, 7),
                  vx=rb.uniform(-14, 14), vy=rb.uniform(-10, 6), ph=rb.uniform(0, 6.28),
                  c=rb.choice(["#9BE7FF", "#C9B6FF", "#FF9BCB"])) for _ in range(170)]
    front = [dict(x=rb.uniform(-1600, 1600), y=rb.uniform(-900, 900), r=rb.uniform(120, 220),
                  c=rb.choice(["#5B2BA0", "#2B4FC0"]), ph=rb.uniform(0, 6.28)) for _ in range(5)]
    return dict(cells=cells, demo=demo, tumor=tumor, bokeh=bokeh, motes=motes, front=front)


WORLD = build_world()


def tumor_cells(t):
    """Lista (x, y, r, seed, split_info) das células do tumor vivas em t (posições sem escala)."""
    out = []

    def walk(nd, px, py, born, parent_path_seed):
        # posição: nasce no centroide do pai e escorrega até o próprio
        f = ease_out((t - born) / DIV_D) if born is not None else 1.0
        x = px + (nd["x"] - px) * f
        y = py + (nd["y"] - py) * f
        if nd["kids"] and t >= nd["t"]:
            for k in nd["kids"]:
                walk(k, x, y, nd["t"], nd["seed"])
            return
        out.append(dict(x=x, y=y, seed=nd["seed"], born=born, pseed=parent_path_seed,
                        next=nd.get("t") if nd["kids"] else None, axis=_axis(nd)))

    walk(WORLD["tumor"], 0.0, 0.0, None, 0)
    return out


def _axis(nd):
    if not nd["kids"]:
        return 0.0
    a, b = nd["kids"]
    return math.atan2(b["y"] - a["y"], b["x"] - a["x"])


def n_eff(t):
    n = 1.0
    gen_t = [T_DIV[g] for g in range(len(T_DIV))]
    for g, tg in enumerate(gen_t):
        n += (2 ** g) * ease((t - tg) / (DIV_D + 0.3))
    return n


def push(x, y, cx, cy, area_r):
    """Empurra (x,y) radialmente como se um disco de raio area_r fosse inserido em (cx,cy)."""
    if area_r <= 0:
        return x, y
    dx, dy = x - cx, y - cy
    d = math.hypot(dx, dy) + 1e-6
    nd = math.sqrt(d * d + area_r * area_r)
    return cx + dx / d * nd, cy + dy / d * nd


def relax(P0, R, rt, it=24):
    """Separa células sobrepostas, mantém todas fora do tumor (raio rt) e puxa cada uma de leve
    para a posição empurrada. Determinístico: mesmo t -> mesmo resultado."""
    near = np.hypot(P0[:, 0], P0[:, 1]) < rt + 900
    P = P0[near].copy()
    r = R[near] * 0.97
    tgt = P.copy()
    for _ in range(it):
        d = P[:, None, :] - P[None, :, :]
        dist = np.sqrt((d ** 2).sum(-1)) + np.eye(len(P)) * 1e9
        ov = np.clip((r[:, None] + r[None, :]) - dist, 0, None)
        P += (d / dist[..., None] * ov[..., None] * 0.25).sum(1)
        rad = np.hypot(P[:, 0], P[:, 1]) + 1e-6
        lim = rt * 0.86 + r * 0.8
        out = np.clip(lim - rad, 0, None)
        P += P / rad[:, None] * out[:, None]
        P += (tgt - P) * 0.06
    res = P0.copy()
    res[near] = P
    return res


# ---------------- câmera ----------------
def camera(t):
    """(centro_x, centro_y, zoom) em coordenadas de mundo."""
    keys = [  # t, cx, cy, zoom
        (0.0, 60, 30, 0.92),
        (3.9, -20, 0, 1.02),
        (5.0, -400, -40, 1.32),
        (7.2, -380, -40, 1.36),
        (8.2, -40, 0, 1.38),
        (10.0, 0, 0, 1.22),
        (12.6, 0, 0, 0.74),
        (15.0, 0, 0, 0.66),
    ]
    for (t0, x0, y0, z0), (t1, x1, y1, z1) in zip(keys, keys[1:]):
        if t <= t1:
            f = ease((t - t0) / (t1 - t0))
            # zoom interpolado em log, mais natural
            z = math.exp(math.log(z0) + (math.log(z1) - math.log(z0)) * f)
            return x0 + (x1 - x0) * f, y0 + (y1 - y0) * f, z
    return keys[-1][1], keys[-1][2], keys[-1][3]


def layer(c, cam, parallax):
    cx, cy, z = cam
    zz = 1 + (z - 1) * parallax
    c.save()
    c.translate(W / 2, H / 2)
    c.scale(zz, zz)
    c.translate(-cx * parallax, -cy * parallax)
    return zz


def visible(x, y, r, cam, par=1.0, margin=1.25):
    cx, cy, z = cam
    zz = 1 + (z - 1) * par
    sx = (x - cx * par) * zz
    sy = (y - cy * par) * zz
    return abs(sx) < W / 2 + r * zz * margin and abs(sy) < H / 2 + r * zz * margin


# ---------------- legendas ----------------
LEGENDAS = [
    (0.5, 3.9, "Seu corpo é feito de trilhões de células."),
    (4.3, 7.6, "Elas só se dividem quando recebem o sinal certo."),
    (8.0, 11.0, "Mas mutações no DNA podem fazer uma célula ignorar esse sinal…"),
    (11.3, 14.8, "…e se dividir sem parar. É assim que começa um câncer."),
]


def legendas(c, t):
    band = skia.Paint()
    band.setShader(skia.GradientShader.MakeLinear([(0, H - 260), (0, H)],
                                                  [col("#05041A", 0), col("#05041A", 0.82)]))
    c.drawRect(skia.Rect(0, H - 260, W, H), band)
    for t0, t1, s in LEGENDAS:
        if t0 - 0.01 <= t <= t1:
            a = min(ease((t - t0) / 0.35), ease((t1 - t) / 0.35))
            dy = (1 - ease_out((t - t0) / 0.45)) * 14
            f = motor.font("semibold", 46)
            w = f.measureText(s)
            sh = skia.Paint(AntiAlias=True, Color=col("#000000", 0.9 * a))
            sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 7))
            c.drawString(s, W / 2 - w / 2, 985 + dy + 2, f, sh)
            c.drawString(s, W / 2 - w / 2, 985 + dy, f, skia.Paint(AntiAlias=True, Color=col("#FFFFFF", a)))


# ---------------- quadro ----------------
def frame(t):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    cam = camera(t)

    # fundo
    bg = skia.Paint()
    bg.setShader(skia.GradientShader.MakeRadial((W * 0.45, H * 0.4), W * 0.85, [col(FUNDO[0]), col(FUNDO[1])]))
    c.drawRect(skia.Rect(0, 0, W, H), bg)

    # camada de fundo desfocada (bokeh)
    layer(c, cam, 0.45)
    for b in WORLD["bokeh"]:
        x = b["x"] + 30 * math.sin(t * 0.25 + b["ph"])
        y = b["y"] + 20 * math.cos(t * 0.2 + b["ph"])
        p = skia.Paint(AntiAlias=True, Color=col(b["c"], b["a"]))
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, b["r"] * 0.22))
        c.drawCircle(x, y, b["r"], p)
    c.restore()

    # ---- tecido ----
    zz = layer(c, cam, 1.0)
    na = n_eff(t)
    area_tumor = math.sqrt(max(0.0, na - 1) * (R_C * 1.12) ** 2 * 1.1)
    # divisão normal (demo)
    demo = WORLD["demo"]
    fdiv = seg(t, A_T0, A_T1)
    area_demo = math.sqrt(0.45 * fdiv) * R_H

    def place(x, y):
        x, y = push(x, y, demo["x"], demo["y"], area_demo)
        return push(x, y, 0.0, 0.0, area_tumor)

    # partículas do meio
    for m in WORLD["motes"]:
        x = m["x"] + m["vx"] * t
        y = m["y"] + m["vy"] * t + 8 * math.sin(t + m["ph"])
        if not visible(x, y, 10, cam):
            continue
        a = 0.35 + 0.25 * math.sin(t * 1.7 + m["ph"])
        c.drawCircle(x, y, m["r"], skia.Paint(AntiAlias=True, Color=col(m["c"], a)))

    # células saudáveis: empurrão radial + relaxamento (preenche os vãos em volta do tumor)
    cells_h = WORLD["cells"]
    P = np.array([place(q["x"], q["y"]) for q in cells_h])
    if area_tumor > 0:
        P = relax(P, np.array([q["r"] for q in cells_h]), area_tumor)
    for q, (x, y) in zip(cells_h, P):
        x += 4 * math.sin(t * 0.6 + q["seed"])
        y += 4 * math.cos(t * 0.5 + q["seed"] * 1.3)
        if not visible(x, y, q["r"], cam):
            continue
        # pressão do tumor: achata na direção radial, estica na tangencial
        dist = math.hypot(x, y)
        if area_tumor > 0 and dist < area_tumor + 3 * q["r"]:
            k = ease((area_tumor + 3 * q["r"] - dist) / (3 * q["r"])) * min(1.0, area_tumor / 200)
            path = blob(x, y, q["r"], t, q["seed"], sx=1 - 0.2 * k, sy=1 + 0.12 * k, rot=math.atan2(y, x))
        else:
            path = blob(x, y, q["r"], t, q["seed"], sx=q["sx"], rot=q["rot"])
        draw_cell(c, path, x, y, q["r"], t, q["seed"], tom_pal(q["tom"]))

    # divisão normal: uma célula vira duas (com sulco de clivagem)
    dx, dy = place(demo["x"], demo["y"])
    ang = -0.35
    ux, uy = math.cos(ang), math.sin(ang)
    if t < A_T0 + 0.9:
        f = seg(t, A_T0, A_T0 + 0.9)  # alonga e duplica o núcleo
        r = demo["r"]
        path = blob(dx, dy, r, t, demo["seed"], sx=1 + 0.18 * f, sy=1 - 0.1 * f, rot=ang)
        draw_cell(c, path, dx, dy, r, t, demo["seed"], SAUDAVEL, nuc_split=f, axis=ang)
    else:
        f = seg(t, A_T0 + 0.9, A_T1)
        rk = demo["r"] * (0.86 - 0.06 * f + 0.06 * seg(t, A_T1, A_T1 + 1.2))
        sep = demo["r"] * (0.42 + 0.48 * f)
        kids = [(dx + ux * sep, dy + uy * sep), (dx - ux * sep, dy - uy * sep)]
        paths = [blob(kx, ky, rk, t, demo["seed"] * 5 + i) for i, (kx, ky) in enumerate(kids)]
        if f < 0.97:
            u = skia.Op(paths[0], paths[1], skia.kUnion_PathOp)
            draw_cell(c, u, dx, dy, demo["r"] * 1.1, t, demo["seed"], SAUDAVEL, nucleo=False)
            # núcleos dos filhos por cima, dentro da forma unida
            c.save()
            c.clipPath(u, doAntiAlias=True)
            for i, (kx, ky) in enumerate(kids):
                _nucleo(c, kx, ky, rk, t, demo["seed"] * 5 + i, SAUDAVEL, 0.0)
            c.restore()
        else:
            for i, ((kx, ky), p) in enumerate(zip(kids, paths)):
                draw_cell(c, p, kx, ky, rk, t, demo["seed"] * 5 + i, SAUDAVEL)
    # brilho suave sinalizando a divisão "permitida"
    if A_T0 - 0.3 < t < A_T1 + 0.4:
        a = min(seg(t, A_T0 - 0.3, A_T0 + 0.3), 1 - seg(t, A_T1 - 0.2, A_T1 + 0.4))
        glow(c, dx, dy, demo["r"] * 2.0, "#7FE0FF", 0.22 * a)

    # tumor
    heat = seg(t, T_MUT, T_MUT + 0.9)
    pal = pal_mix(heat) if heat < 1 else CANCER
    if T_MUT - 0.2 < t < T_MUT + 0.8:  # clarão da mutação
        k = 1 - abs((t - T_MUT - 0.15) / 0.55)
        glow(c, 0, 0, R_C * 2.6, "#FFF2B0", 0.7 * max(0.0, k))
    scale = math.sqrt(max(na, 1) / N_LEAF)
    cells = tumor_cells(t)
    # tumor como um todo: brilho de fundo
    if heat > 0:
        glow(c, 0, 0, R_C * 1.2 + area_tumor * 0.95, "#FF2E88", 0.28 * heat, sigma=R_C + area_tumor * 0.4)
    r_root = R_H * (1 - heat) + R_C * heat
    for cl in sorted(cells, key=lambda q: q["y"]):
        x, y = cl["x"] * scale, cl["y"] * scale
        r = r_root if len(cells) == 1 else R_C
        jitter = 0.06 if heat > 0.5 else 0.035
        # perto da divisão: alonga; logo após nascer: forma unida com a irmã
        pre = 0.0
        if cl["next"] is not None:
            pre = seg(t, cl["next"] - 0.55, cl["next"])
        path = blob(x, y, r, t * 1.4, cl["seed"], amp=jitter, sx=1 + 0.15 * pre, sy=1 - 0.08 * pre, rot=cl["axis"])
        draw_cell(c, path, x, y, r, t * 1.4, cl["seed"], pal, heat=heat, nuc_split=pre, axis=cl["axis"])

    c.restore()

    # camada da frente: borrões passando perto da câmera
    layer(c, cam, 1.6)
    for b in WORLD["front"]:
        x = b["x"] + 60 * math.sin(t * 0.18 + b["ph"])
        y = b["y"] + 40 * math.cos(t * 0.15 + b["ph"])
        p = skia.Paint(AntiAlias=True, Color=col(b["c"], 0.22))
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, b["r"] * 0.35))
        c.drawCircle(x, y, b["r"], p)
    c.restore()

    # vinheta
    v = skia.Paint()
    v.setShader(skia.GradientShader.MakeRadial((W / 2, H / 2), W * 0.72,
                                               [col("#000000", 0), col("#000000", 0), col("#04030F", 0.75)],
                                               [0.0, 0.55, 1.0]))
    c.drawRect(skia.Rect(0, 0, W, H), v)

    legendas(c, t)
    # entrada e saída em preto
    fa = max(1 - t / 0.5, (t - (DUR - 0.5)) / 0.5, 0)
    if fa > 0:
        c.drawRect(skia.Rect(0, 0, W, H), skia.Paint(Color=col("#000000", min(fa, 1))))
    return surf.makeImageSnapshot()


def _nucleo(c, nx, ny, r, t, seed, pal, heat):
    nrr = r * 0.4
    npath = blob(nx + 0.06 * r, ny + 0.05 * r, nrr, t * 1.3, seed * 13, amp=0.05)
    fill(c, npath, pal["nuc_dark"])
    fill(c, shifted(npath, -0.12 * nrr, -0.12 * nrr), pal["nuc_light"])
    fill(c, shifted(npath, -0.03 * nrr, -0.03 * nrr, 0.86, nx + 0.06 * r, ny + 0.05 * r), pal["nuc"])
    c.drawCircle(nx - 0.26 * nrr, ny - 0.28 * nrr, nrr * 0.14, skia.Paint(AntiAlias=True, Color=col("#FFFFFF", 0.55)))


# ---------------- saída ----------------
def render_chunk(args):
    i0, i1, out = args
    proc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
                             "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                             "-crf", "16", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(i0, i1):
        img = frame(i / FPS)
        proc.stdin.write(img.toarray(colorType=skia.kRGBA_8888_ColorType).tobytes())
    proc.stdin.close()
    proc.wait()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--still")
    ap.add_argument("--video", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    if a.still:
        (AQUI / "stills").mkdir(exist_ok=True)
        for s in a.still.split(","):
            frame(float(s)).save(str(AQUI / "stills" / f"t{float(s):05.2f}.png"), skia.kPNG)
        return
    if a.video:
        tmp = AQUI / "tmp"
        tmp.mkdir(exist_ok=True)
        (AQUI / "final").mkdir(exist_ok=True)
        n = int(DUR * FPS)
        step = math.ceil(n / a.jobs)
        chunks = [(i, min(i + step, n), str(tmp / f"parte_{k}.mp4")) for k, i in enumerate(range(0, n, step))]
        with Pool(a.jobs) as p:
            outs = p.map(render_chunk, chunks)
        lst = tmp / "lista.txt"
        lst.write_text("".join(f"file '{o}'\n" for o in outs))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", "-movflags", "+faststart", str(AQUI / "final" / "teste_celula_cancer.mp4")],
                       check=True)


if __name__ == "__main__":
    main()
