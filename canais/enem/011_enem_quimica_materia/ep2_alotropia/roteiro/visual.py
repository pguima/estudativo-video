"""Visual — Matéria, Substâncias e Misturas, Episódio 2: Alotropia (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita as peças do ep. 1 (bolinhas por elemento, fórmulas que acendem, cartões de erro) via V.
Peça própria deste episódio:
- Carbono3D: os MESMOS átomos de carbono (bolinhas cinza) se reorganizam entre estados 3D:
  diamante (rede rígida, cada átomo preso a 4) → grafite (folhas hexagonais empilhadas) → grafeno (uma folha) → nanotubo.
"""
import importlib.util
import json
import math
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_EP1 = Path(__file__).resolve().parents[2] / "ep1_materia_e_substancias" / "roteiro" / "visual.py"
_spec = importlib.util.spec_from_file_location("visual_quimica_ep1", _EP1)
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep2_alotropia.mp4"
CARD_R = (140, 150, 1640, 690)
CGRAY = V.EL["C"]


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# carbono em 3D: estados e projeção
# ======================================================================

LAYER_GAP = 3.0
LX, LZ = 4.4, 4.9


def _honeycomb():
    """retalho retangular de folha hexagonal (ligação = 1), centrado num hexágono"""
    s3 = math.sqrt(3)
    pts = []
    for i in range(-10, 11):
        for j in range(-10, 11):
            ox, oz = i * s3 + j * s3 / 2, j * 1.5
            pts.append((ox, oz)); pts.append((ox, oz + 1.0))
    cx, cz = s3 / 2, 0.5
    out = [(x - cx, z - cz) for x, z in pts if abs(x - cx) <= LX and abs(z - cz) <= LZ]
    out.sort(key=lambda p: (round(p[1], 3), p[0]))
    return out


@lru_cache(None)
def _sheet():
    return _honeycomb()


N_LAYER = len(_honeycomb())
N_AT = N_LAYER * 3


@lru_cache(None)
def st_grafite():
    out = []
    sh = _sheet()
    for L in range(3):
        dz = 1.0 if L == 1 else 0.0
        for x, z in sh:
            out.append((x, (1 - L) * LAYER_GAP, z + dz))
    return out


@lru_cache(None)
def st_diamante():
    a = 4 / math.sqrt(3)            # ligação = 1
    base = [(0, 0, 0), (0, .5, .5), (.5, 0, .5), (.5, .5, 0)]
    pts = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for k in range(-3, 4):
                for bx, by, bz in base:
                    for d in (0, .25):
                        pts.append(((i + bx + d) * a, (j + by + d) * a, (k + bz + d) * a))
    c0 = (0.125 * a, 0.125 * a, 0.125 * a)
    pts.sort(key=lambda p: max(abs(p[0] - c0[0]), abs(p[1] - c0[1]) * 1.25, abs(p[2] - c0[2])) + 0.05 * (
        (p[0] - c0[0]) ** 2 + (p[1] - c0[1]) ** 2 + (p[2] - c0[2]) ** 2) ** 0.5)
    sel = pts[:N_AT]
    return [(x - c0[0], y - c0[1], z - c0[2]) for x, y, z in sel]


@lru_cache(None)
def _ordem():
    """associa cada átomo do diamante a uma posição no grafite (camadas por altura; dentro da camada, por ângulo)"""
    d, g = st_diamante(), st_grafite()
    di = sorted(range(N_AT), key=lambda i: -d[i][1])
    gi = sorted(range(N_AT), key=lambda i: -g[i][1])
    perm = [0] * N_AT
    for L in range(3):
        ds = di[L * N_LAYER:(L + 1) * N_LAYER]
        gs = gi[L * N_LAYER:(L + 1) * N_LAYER]
        ds.sort(key=lambda i: math.atan2(d[i][2], d[i][0]) + 0.02 * math.hypot(d[i][0], d[i][2]))
        gs.sort(key=lambda i: math.atan2(g[i][2], g[i][0]) + 0.02 * math.hypot(g[i][0], g[i][2]))
        for a_, b_ in zip(ds, gs):
            perm[a_] = b_
    return perm


def st_diamante_ordenado():
    """diamante na MESMA numeração do grafite (átomo k do diamante vira o átomo k do grafite)"""
    d = st_diamante()
    out = [None] * N_AT
    for i, k in enumerate(_ordem()):
        out[k] = d[i]
    return out


def st_rolo(f, R=1.9):
    """camada de cima enrolando: f=0 folha plana, f=1 tubo"""
    sh = _sheet()
    zs = [z for _, z in sh]
    z0 = (max(zs) + min(zs)) / 2
    W_ = max(zs) - min(zs) + 1.5
    out = []
    for x, z in sh:
        u = z - z0
        if f < 1e-3:
            out.append((x, 0.0, u)); continue
        Rf = W_ / (2 * math.pi * f)
        th = u / Rf
        out.append((x, Rf * (1 - math.cos(th)) - Rf * f, Rf * math.sin(th)))
    return out


def _bonds(pts, lim=1.18):
    out = []
    for i in range(len(pts)):
        xi, yi, zi = pts[i]
        for j in range(i + 1, len(pts)):
            xj, yj, zj = pts[j]
            dd = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
            if dd < lim * lim:
                out.append((i, j))
    return out


@lru_cache(None)
def bonds_diamante():
    return _bonds(st_diamante_ordenado())


@lru_cache(None)
def bonds_grafite():
    return _bonds(st_grafite())


@lru_cache(None)
def bonds_folha():
    return _bonds([(x, 0.0, z) for x, z in _sheet()])


def proj(p, cx, cy, s, yaw, pitch=18, D=40.0):
    x, y, z = p
    cy_, sy = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    x, z = x * cy_ + z * sy, -x * sy + z * cy_
    cp, sp = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    y, z = y * cp - z * sp, y * sp + z * cp
    k = D / (D - z)
    return cx + x * s * k, cy - y * s * k, z, k


def ball(c, x, y, r, a, col=CGRAY, glow=0.0, dim=0.0):
    if a <= 0:
        return
    if glow > 0:
        c.drawCircle(x, y, r * 1.6, paint(AMBER, a * glow * 0.4))
    cc = mix(col, "#FFFFFF", dim * 0.55)
    c.drawCircle(x, y, r, paint(cc, a))
    g = skia.GradientShader.MakeRadial(skia.Point(x - r * 0.35, y - r * 0.4), r * 1.1,
                                       [skia.Color4f(1, 1, 1, 0.5 * a), skia.Color4f(1, 1, 1, 0)])
    p = skia.Paint(AntiAlias=True); p.setShader(g)
    c.drawCircle(x, y, r, p)
    c.drawCircle(x, y, r, paint(mix(cc, "#000000", 0.35), a, stroke=max(1.2, r * 0.08)))


def carbono(c, pts, cx, cy, s, a=1.0, yaw=30.0, pitch=18, bonds=(), bond_a=1.0, r=0.22, glow=None, bond_col="#9A9AA0",
            bond_w=0.11, extra_bonds=(), alphas=None, dim=None):
    """desenha os átomos (ordenados por profundidade) e as ligações; extra_bonds = [(i, j, cor, alpha)]"""
    if a <= 0:
        return
    P = [proj(p, cx, cy, s, yaw, pitch) for p in pts]
    if bond_a > 0:
        for i, j in bonds:
            ai = a * bond_a * (min(alphas[i], alphas[j]) if alphas else 1.0)
            if ai > 0.01:
                (x0, y0, z0, k0), (x1, y1, z1, k1) = P[i], P[j]
                line(c, x0, y0, x1, y1, bond_col, ai, s * bond_w * (k0 + k1) / 2)
    for i, j, col, ab in extra_bonds:
        (x0, y0, _, k0), (x1, y1, _, k1) = P[i], P[j]
        line(c, x0, y0, x1, y1, col, a * ab, s * bond_w * 1.6 * (k0 + k1) / 2)
    order = sorted(range(len(P)), key=lambda i: P[i][2])
    for i in order:
        x, y, z, k = P[i]
        ai = a * (alphas[i] if alphas else 1.0)
        fog = clamp((-z) / 14) * 0.35
        ball(c, x, y, s * r * k, ai, CGRAY, glow(i) if glow else 0.0, (dim[i] if dim else 0) + fog)


def lerp3(p, q, f):
    return [(lerp(a[0], b[0], f), lerp(a[1], b[1], f), lerp(a[2], b[2], f)) for a, b in zip(p, q)]


def morph(f):
    """diamante → grafite, com um "sopro" para os átomos se soltarem no meio do caminho"""
    d, g = st_diamante_ordenado(), st_grafite()
    e = ease_io(f)
    out = []
    for k, (a_, b_) in enumerate(zip(d, g)):
        bump = math.sin(math.pi * e) * 0.9
        x, y, z = lerp(a_[0], b_[0], e), lerp(a_[1], b_[1], e), lerp(a_[2], b_[2], e)
        L = math.hypot(x, z) + 1e-6
        out.append((x + x / L * bump, y, z + z / L * bump))
    return out


def centro_diamante():
    """átomo mais central do diamante e seus 4 vizinhos (para destacar o trepa-trepa)"""
    d = st_diamante_ordenado()
    i0 = min(range(N_AT), key=lambda i: d[i][0] ** 2 + d[i][1] ** 2 + d[i][2] ** 2)
    viz = [j for a_, b_ in bonds_diamante() for j in ((b_,) if a_ == i0 else (a_,) if b_ == i0 else ())]
    return i0, viz


# ======================================================================
# peças auxiliares
# ======================================================================

def trepa(c, cx, cy, a, s=1.0):
    """trepa-trepa de parquinho em perspectiva"""
    if a <= 0:
        return
    col = "#E8A317"
    n = 3
    def P(i, j, k):
        return cx + (i - j) * 46 * s, cy - k * 60 * s + (i + j) * 24 * s
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                x, y = P(i, j, k)
                if i < n:
                    x2, y2 = P(i + 1, j, k); line(c, x, y, x2, y2, col, a, 5 * s)
                if j < n:
                    x2, y2 = P(i, j + 1, k); line(c, x, y, x2, y2, "#3B6CF6", a, 5 * s)
                if k < n:
                    x2, y2 = P(i, j, k + 1); line(c, x, y, x2, y2, "#E5484D", a, 5 * s)
                c.drawCircle(x, y, 6 * s, paint(INK2, a))


def baralho(c, cx, cy, a, s=1.0, desliza=0.0, n=6):
    if a <= 0:
        return
    for k in range(n):
        off = desliza * (n - 1 - k) * 18 * s
        x, y = cx - 110 * s + off + k * 3 * s, cy - k * 12 * s
        rrect(c, x, y, 220 * s, 140 * s, 12 * s, "#FFFFFF", a, shadow=True, stroke=2.5, stroke_color=LIGHT)
        rrect(c, x + 12 * s, y + 12 * s, 196 * s, 116 * s, 8 * s, "#E5484D" if k == n - 1 else "#F4F4F2", a * (0.9 if k == n - 1 else 1))


def fulereno(c, cx, cy, r, a, yaw=0.0):
    """bola de carbonos (60 pontos numa esfera) com ligações curtas"""
    if a <= 0:
        return
    pts = _fib_sphere(60)
    R = 3.2
    P3 = [(x * R, y * R, z * R) for x, y, z in pts]
    carbono(c, P3, cx, cy, r / R, a, yaw=yaw, pitch=15, bonds=_bonds(P3, 1.62), r=0.26, bond_w=0.1)


@lru_cache(None)
def _fib_sphere(n):
    out = []
    g = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        y = 1 - 2 * (i + 0.5) / n
        rr = math.sqrt(1 - y * y)
        th = g * i
        out.append((math.cos(th) * rr, y, math.sin(th) * rr))
    return out


def mini(c, kind, cx, cy, s, a, t=0.0):
    """miniatura rotativa de cada forma do carbono"""
    yaw = 20 + t * 12
    if kind == "diamante":
        carbono(c, st_diamante_ordenado(), cx, cy, s, a, yaw, bonds=bonds_diamante())
    elif kind == "grafite":
        carbono(c, st_grafite(), cx, cy, s, a, yaw, 16, bonds=bonds_grafite())
    elif kind == "grafeno":
        carbono(c, [(x, 0.0, z) for x, z in _sheet()], cx, cy, s, a, yaw, pitch=35, bonds=bonds_folha())
    elif kind == "nanotubo":
        carbono(c, st_rolo(1.0), cx, cy, s, a, yaw + 60, pitch=20, bonds=_bonds(st_rolo(1.0), 1.25))
    elif kind == "fulereno":
        fulereno(c, cx, cy, s * 3.0, a, yaw)


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    V.regra(c, s, cx, cy, a, size, col, w)


def estrutura(c, t, t0, y=815):
    """o fecho de cada alótropo"""
    regra(c, "A ESTRUTURA DECIDE A PROPRIEDADE", W / 2, y, ep(t, t0, 0.5), 34, PURPLE, w=900)


def P4(c, cx, cy, r, a, col):
    pts = [(0, -1.2), (-1.2, 0.6), (1.2, 0.6), (0.15, -0.05)]
    for i in range(4):
        for j in range(i + 1, 4):
            line(c, cx + pts[i][0] * r, cy + pts[i][1] * r, cx + pts[j][0] * r, cy + pts[j][1] * r, "#B8B8BC", a, r * 0.22)
    for k in (3, 0, 1, 2):
        ball(c, cx + pts[k][0] * r, cy + pts[k][1] * r, r * 0.55, a, col)


def cadeia(c, cx, cy, r, a, col, n=7):
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * r * 1.3
        y = cy + (r * 0.5 if k % 2 else -r * 0.5)
        if k:
            line(c, x - r * 1.3, cy + (r * 0.5 if (k - 1) % 2 else -r * 0.5), x, y, "#B8B8BC", a, r * 0.22)
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * r * 1.3
        y = cy + (r * 0.5 if k % 2 else -r * 0.5)
        ball(c, x, y, r * 0.52, a, col)


def cristal(c, cx, cy, a, s=1.0, agulha=False):
    col = V.EL["S"]
    if a <= 0:
        return
    if agulha:
        pts = [(-30, -110), (30, -110), (40, 100), (-20, 120), (-40, 90)]
        top = [(-30, -110), (30, -110), (10, -140)]
    else:
        pts = [(0, -110), (90, 0), (0, 110), (-90, 0)]
        top = None
    p = skia.Path(); p.moveTo(cx + pts[0][0] * s, cy + pts[0][1] * s)
    for x, y in pts[1:]:
        p.lineTo(cx + x * s, cy + y * s)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint("#B88A00", a, stroke=4))
    if not agulha:
        line(c, cx - 90 * s, cy, cx + 90 * s, cy, "#B88A00", a * 0.6, 3)
        line(c, cx, cy - 110 * s, cx, cy + 110 * s, "#B88A00", a * 0.6, 3)
    else:
        q = skia.Path(); q.moveTo(cx + top[0][0] * s, cy + top[0][1] * s)
        for x, y in top[1:]:
            q.lineTo(cx + x * s, cy + y * s)
        q.close()
        c.drawPath(q, paint(mix(col, "#FFFFFF", 0.3), a))
        c.drawPath(q, paint("#B88A00", a, stroke=4))


def terra_ozonio(c, x, y, w, h, a, t, t0):
    """céu com a camada de ozônio barrando os raios UV"""
    if a <= 0:
        return
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), True)
    g = skia.GradientShader.MakeLinear([skia.Point(x, y), skia.Point(x, y + h)],
                                       [skia.Color4f(0.10, 0.16, 0.38, a), skia.Color4f(0.55, 0.75, 0.98, a)])
    p = skia.Paint(AntiAlias=True); p.setShader(g)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), p)
    gx, gy = x + w / 2, y + h + 900
    c.drawCircle(gx, gy, 1000, paint("#2E9E5B", a))
    c.drawCircle(gx, gy, 1110, paint("#7FD3F7", a * 0.45, stroke=40))
    text(c, "camada de ozônio (O₃)", x + w - 30, y + 150, 26, "black", "#FFFFFF", a, align="right")
    c.drawCircle(x + 90, y + 80, 44, paint("#FFD54A", a))
    for k in range(4):
        ph = ((t - t0) * 0.6 + k * 0.25) % 1.0
        x0, y0 = x + 140 + k * 60, y + 100
        x1, y1 = x0 + 120, y0 + 120
        f = min(ph * 1.6, 1.0)
        xe, ye = lerp(x0, x1, f), lerp(y0, y1, f)
        line(c, x0, y0, xe, ye, "#C084FC", a * (1 - ph * 0.6), 6)
        if f >= 1:
            check_icon(c, x1, y1 + 4, 14, a * (1 - ph), RED, "x")
    text(c, "raios UV", x + 210, y + 90, 22, "black", "#E9D5FF", a)
    c.restore()


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "ALOTROPIA · EPISÓDIO 2", BLUE)
    aa, dy = rise(t, C["01.a"])
    card(c, 200, 190 + dy, 620, 520, aa)
    V.diamante(c, 510, 380 + dy, aa, 1.2)
    text(c, "DIAMANTE", 510, 560 + dy, 40, "black", INK, aa)
    text(c, "o mais duro", 510, 610 + dy, 30, "bold", INK2, aa)
    ab, dy2 = rise(t, C["01.b"])
    card(c, 1100, 190 + dy2, 620, 520, ab)
    V.lapis(c, 1410, 380 + dy2, ab, 1.1)
    text(c, "GRAFITE", 1410, 560 + dy2, 40, "black", INK, ab)
    text(c, "um dos mais moles", 1410, 610 + dy2, 30, "bold", INK2, ab)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        V.peca(c, W / 2, 440, 70, "C", ac)
        arrow(c, 880, 440, 840, 440, INK2, ac, 4, 14)
        arrow(c, 1040, 440, 1080, 440, INK2, ac, 4, 14)
        text(c, "carbono puro", W / 2, 560, 32, "black", INK, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        line(c, 330, 670, 330 + 360 * ease_io(prog(t, C["01.d"], 0.8)), 650, "#5BA6D6", ad, 4)
        text(c, "corta vidro", 510, 690, 24, "bold", "#5BA6D6", ad)
        line(c, 1250, 670, 1250 + 320 * ease_io(prog(t, C["01.d"] + 1.0, 0.8)), 668, INK, ad, 8)
        text(c, "solta no papel", 1410, 700, 24, "bold", INK2, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        s_ = 0.8 + 0.2 * ease_back(ae)
        c.save(); c.translate(W / 2, 800); c.scale(s_, s_)
        rrect(c, -170, -46, 340, 92, 24, AMBER, ae, shadow=True)
        text_mid(c, "COMO?", 0, 0, 50, "black", INK, ae)
        c.restore()


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    for k, (cue, titulo) in enumerate((("02.a", "ENTENDER O QUE\nÉ ALOTROPIA"), ("02.b", "RECONHECER OS\nALÓTROPOS DO ENEM"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 600 + k * 720
        card(c, x - 320, 200 + dy, 640, 540, a)
        if k == 0:
            mini(c, "diamante", x - 140, 400 + dy, 19, a, t)
            mini(c, "grafite", x + 140, 400 + dy, 19, a, t)
        else:
            for j, kd in enumerate(("grafeno", "nanotubo", "fulereno")):
                mini(c, kd, x - 200 + j * 200, 430 + dy, 14, a * ep(t, C[cue] + 0.3 * j, 0.4), t)
            V.mol(c, "O3", x, 285 + dy, 20, a)
        for j, ln in enumerate(titulo.split("\n")):
            text(c, ln, x, 610 + dy + j * 54, 44, "black", INK, a)


def b_prereq(c, t, C, B):
    head(c, t, B["start"], "LEMBRETE DO EPISÓDIO 1", "SUBSTÂNCIA SIMPLES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    for k, e in enumerate(("O", "N", "S")):
        V.brick(c, 260 + k * 160, 300, 130, 84, V.EL[e], aa * ep(t, C["03.a"] + 0.2 * k, 0.4))
    text(c, "peça = átomo · cor = elemento", 480, 450, 30, "black", INK2, aa)
    V.defbox(c, "SIMPLES = 1 cor só", "um único elemento", 480, 610, ep(t, C["03.b"], 0.5), w=600)
    for k, (cue, f, m) in enumerate((("03.d", "O2", "O2"), ("03.e", "O3", "O3"))):
        a = ep(t, C[cue], 0.5)
        x = 1100 + k * 360
        V.mol(c, m, x, 330, 42, a, ease_io(prog(t, C[cue], 0.9)))
        V.formula(c, f, x, 500, 110, a)
        text(c, f"{2 + k} peças de oxigênio", x, 610, 28, "black", V.eltxt("O"), a)
    pill(c, "o número pequeno conta as peças", 1280, 720, BLUE, size=26, a=ep(t, C["03.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco a: definição
# ======================================================================

PREDIO = [(0, k) for k in range(5)] + [(1, k) for k in range(5)]
CARRO = [(-1.5, 0), (-0.5, 0), (0.5, 0), (1.5, 0), (-2.5, 0), (2.5, 0), (-1, 1), (0, 1), (1, 1), (-0.0, 2)]


def pecas_cinza(c, cx, by, f, a):
    """10 peças cinza: f=0 prédio, f=1 carrinho"""
    bw, bh = 110, 66
    for k in range(10):
        (px, py), (qx, qy) = PREDIO[k], CARRO[k]
        e = ease_io(clamp(f * 1.4 - k * 0.04))
        hop = math.sin(math.pi * e) * 90
        x = cx + lerp((px - 0.5) * bw, qx * bw, e) - bw / 2
        y = by - lerp(py, qy, e) * bh - bh - hop
        V.brick(c, x, y, bw - 6, bh - 6, "#8E8E93", a)
    if f > 0.95:
        aw = ep(f, 0.95, 0.05) * a
        for dx in (-200, 200):
            c.drawCircle(cx + dx, by + 10, 34, paint(INK, aw))
            c.drawCircle(cx + dx, by + 10, 14, paint("#B8B8BC", aw))


def b_def(c, t, C, B):
    head(c, t, B["start"], "O MESMO ELEMENTO", "SUBSTÂNCIAS DIFERENTES?", BLUE)
    card(c, *CARD_R)
    if t < C["05"] - 0.2:
        aa = ep(t, C["04.a"], 0.5)
        f = ease_io(prog(t, C["04.c"], 1.6))
        pecas_cinza(c, 620, 700, f, aa)
        text(c, "PRÉDIO" if f < 0.5 else "CARRINHO", 620, 780, 34, "black", INK, ep(t, C["04.b"], 0.4))
        ad = ep(t, C["04.d"], 0.5)
        regra(c, "mesmas peças", 1300, 330, ad, 36, BLUE, w=520)
        regra(c, "montagem diferente", 1300, 460, ep(t, C["04.d"] + 0.8, 0.5), 36, BLUE, w=520)
        regra(c, "MUDA A MONTAGEM, MUDA TUDO", 1300, 620, ep(t, C["04.d"] + 1.6, 0.5), 32, PURPLE, w=620)
        return
    a0 = ep(t, C["05"], 0.5)
    for k, f in enumerate((0.0, 1.0)):
        x = 330 + k * 480
        c.save(); c.translate(x, 600); c.scale(0.58, 0.58)
        pecas_cinza(c, 0, 0, f, a0)
        c.restore()
        pill(c, "ALÓTROPO", x, 680, BLUE, size=24, a=ep(t, C["05.b"] + 0.5 * k, 0.5), anchor="center", bounds=(0, 1920))
    V.defbox(c, "ALOTROPIA", "1 elemento → várias substâncias simples", 1420, 330, ep(t, C["05.a"], 0.5), w=560)
    V.defbox(c, "ALÓTROPO", "cada uma dessas substâncias", 1420, 540, ep(t, C["05.b"], 0.5), w=560)
    text(c, "mesmas peças cinza → 2 alótropos", 570, 780, 30, "black", INK2, ep(t, C["05.c"], 0.5))


# ======================================================================
# bloco b: oxigênio
# ======================================================================

def b_oxigenio(c, t, C, B):
    head(c, t, B["start"], "OXIGÊNIO", "O₂ × O₃", BLUE)
    aa, dy = rise(t, C["06.a"])
    card(c, 200, 190 + dy, 700, 560, aa)
    if aa > 0:
        text(c, "NO SEU PULMÃO", 550, 250 + dy, 28, "black", INK2, aa)
        V.mol(c, "O2", 550, 420 + dy, 70, aa, ease_io(prog(t, C["06.a"], 0.9)))
        V.formula(c, "O2", 550, 610 + dy, 110, aa)
        text(c, "gás oxigênio", 550, 710 + dy, 30, "black", INK, aa)
    ab, dy2 = rise(t, C["06.b"])
    card(c, 1020, 190 + dy2, 700, 560, ab)
    if ab > 0:
        text(c, "A 20–30 KM DE ALTURA", 1370, 250 + dy2, 28, "black", INK2, ab)
        ac = ep(t, C["06.c"], 0.5)
        V.mol(c, "O3", 1370, 420 + dy2, 62, ac, ease_io(prog(t, C["06.c"], 0.9)))
        V.formula(c, "O3", 1370, 610 + dy2, 110, ac)
        text(c, "?", 1370, 470 + dy2, 120, "black", LIGHT, ab * (1 - ac))
    V.defbox(c, "OZÔNIO = O₃", "", 1370, 820, ep(t, C["06.d"], 0.5), w=460)


def b_atomicidade(c, t, C, B):
    head(c, t, B["start"], "O QUE MUDOU?", "ATOMICIDADE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["07.t"], 0.5)
    for k, (m, n) in enumerate((("O2", 2), ("O3", 3))):
        x = 470 + k * 500
        V.mol(c, m, x, 330, 60, a0)
        ac = ep(t, C["07.a"] + 0.6 * k, 0.4)
        badge_num(c, n, x, 470, ac, 40, bg=BLUE)
        text(c, "peças", x, 540, 28, "black", INK2, ac)
        text(c, f"atomicidade {n}", x, 610, 34, "black", BLUE, ep(t, C["07.c"] + 0.8 * k, 0.4))
    text_mid(c, "≠", 720, 330, 90, "black", INK2, ep(t, C["07.a"], 0.5))
    V.defbox(c, "ATOMICIDADE", "nº de átomos na molécula", 1430, 340, ep(t, C["07.b"], 0.5), w=460)
    regra(c, "mudou a atomicidade → mudou a substância", W / 2, 740, ep(t, C["07.d"], 0.5), 34, PURPLE, w=1100)


def b_ozonio(c, t, C, B):
    head(c, t, B["start"], "MESMO ELEMENTO", "PROPRIEDADES OPOSTAS", BLUE)
    aa = ep(t, C["08.a"], 0.5)
    terra_ozonio(c, 160, 180, 760, 560, aa, t, C["08.a"])
    if aa > 0:
        pill(c, "PROTEGE", 540, 700, GREEN, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab, dy = rise(t, C["08.b"])
    card(c, 1000, 180 + dy, 760, 560, ab)
    if ab > 0:
        text(c, "NO NÍVEL DO CHÃO", 1380, 240 + dy, 28, "black", INK2, ab)
        for k in range(6):   # fumaça
            c.drawCircle(1180 + k * 80, 380 + dy + 20 * math.sin(k + t), 60, paint("#9AA3AD", ab * 0.35))
        V.mol(c, "O3", 1380, 380 + dy, 46, ab)
        pill(c, "TÓXICO: irrita olhos e pulmões", 1380, 520 + dy, AMBER, size=28, fg=INK, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["08.c"], 0.5)
    if ac > 0:
        V.formula(c, "O2", 1230, 640, 70, ac)
        check_icon(c, 1300, 640, 22, ac, GREEN)
        text(c, "respira", 1230, 710, 24, "bold", INK2, ac)
        V.formula(c, "O3", 1530, 640, 70, ac)
        check_icon(c, 1600, 640, 22, ac, RED, "x")
        text(c, "não", 1530, 710, 24, "bold", INK2, ac)
    estrutura(c, t, C["08.d"])


# ======================================================================
# bloco c: carbono (a animação principal)
# ======================================================================

def b_carbono(c, t, C, B):
    head(c, t, B["start"], "CARBONO", "O CAMPEÃO DO ENEM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    V.diamante(c, 360, 420, aa, 0.9)
    text(c, "diamante", 360, 560, 30, "black", INK, aa)
    V.lapis(c, 360, 690, aa, 0.6)
    text(c, "grafite", 360, 790, 30, "black", INK, aa)
    text(c, "= só carbono", 650, 600, 34, "black", INK, aa)
    ab = ep(t, C["09.b"], 0.5)
    build = ease_io(prog(t, C["09.b"], 2.0))
    if ab > 0:
        n = int(N_AT * build) + 1
        al = [clamp(build * N_AT - i) for i in range(N_AT)]
        carbono(c, st_diamante_ordenado(), 1220, 380, 34, ab, 25 + (t - C["09.b"]) * 10, bonds=bonds_diamante(),
                bond_a=build, alphas=al)
        pill(c, "ARRANJO = jeito de organizar", 1220, 610, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
    V.defbox(c, "RETÍCULO", "arranjo que se repete organizado", 1220, 735, ep(t, C["09.c"], 0.5), w=640)


def b_diamante(c, t, C, B):
    head(c, t, B["start"], "DIAMANTE", "UM TREPA-TREPA DE CARBONO", BLUE)
    card(c, 140, 150, 1000, 610)
    i0, viz = centro_diamante()
    hb = ep(t, C["10.b"], 0.5)
    ex = [(i0, j, AMBER, hb) for j in viz]
    glow = (lambda i: hb if i == i0 or i in viz else 0.0)
    carbono(c, st_diamante_ordenado(), 640, 430, 47, 1.0, 25 + (t - B["start"]) * 9, bonds=bonds_diamante(),
            extra_bonds=ex, glow=glow)
    pill(c, "cada átomo preso a outros 4", 640, 718, AMBER, size=28, fg=INK, a=hb, anchor="center", bounds=(0, 1920))
    aa, dy = rise(t, C["10.a"])
    card(c, 1180, 150 + dy, 580, 470, aa)
    trepa(c, 1470, 380 + dy, aa, 0.95)
    text(c, "trepa-trepa", 1470, 585 + dy, 30, "black", INK, aa)
    ac = ep(t, C["10.c"], 0.5)
    pill(c, "rede 3D rígida", 1470, 668, BLUE, size=28, a=ac, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["10.d"], 0.5)
    pill(c, "o mais DURO da natureza", 1470, 735, INK2, size=26, a=ad, anchor="center", bounds=(0, 1920))
    estrutura(c, t, C["10.e"])


def b_grafite(c, t, C, B):
    head(c, t, B["start"], "GRAFITE", "UM BARALHO DE CARBONO", BLUE)
    card(c, 140, 150, 1000, 610)
    f = prog(t, C["11.a"], 3.0)
    yaw = 25 + (t - B["start"]) * 6
    pitch = lerp(18, 13, ease_io(f))
    pts = morph(f)
    ac = ep(t, C["11.c"], 0.5)
    ad = ep(t, C["11.d"], 0.5)
    bonds_a = clamp(f * 3 - 2)
    carbono(c, pts, 640, 440, 40, 1.0, yaw, pitch, bonds=bonds_diamante(), bond_a=(1 - clamp(f * 3)))
    if bonds_a > 0:
        carbono(c, pts, 640, 440, 40, 1.0, yaw, pitch, bonds=bonds_grafite(), bond_a=bonds_a,
                bond_col=mix("#9A9AA0", GREEN, ac))
    if ad > 0:
        g = st_grafite()
        for L in range(2):
            for k in range(0, N_LAYER, 7):
                i, j = L * N_LAYER + k, (L + 1) * N_LAYER + k
                (x0, y0, _, _), (x1, y1, _, _) = proj(g[i], 640, 440, 40, yaw, pitch), proj(g[j], 640, 440, 40, yaw, pitch)
                line(c, x0, y0, x1, y1, RED, ad * 0.8, 3, dash=[6, 8])
    pill(c, "folhas de 6 lados (favo de mel)", 640, 718, BLUE, size=28, a=ep(t, C["11.a"] + 2.5, 0.5), anchor="center", bounds=(0, 1920))
    ab, dy = rise(t, C["11.b"])
    card(c, 1180, 150 + dy, 580, 420, ab)
    baralho(c, 1470, 380 + dy, ab, 0.95)
    text(c, "baralho de cartas", 1470, 530 + dy, 30, "black", INK, ab)
    pill(c, "dentro da folha: bem presas", 1470, 640, GREEN, size=26, a=ac, anchor="center", bounds=(0, 1920))
    pill(c, "entre as folhas: mal presas", 1470, 720, RED, size=26, a=ad, anchor="center", bounds=(0, 1920))


def lapis_escrevendo(c, tx, ty, a, ang=55):
    """lápis com a ponta em (tx, ty), corpo subindo para a direita"""
    if a <= 0:
        return
    c.save(); c.translate(tx, ty); c.rotate(-ang)
    p = skia.Path(); p.moveTo(0, 0); p.lineTo(70, -24); p.lineTo(70, 24); p.close()
    c.drawPath(p, paint("#E9C9A0", a))
    p = skia.Path(); p.moveTo(0, 0); p.lineTo(24, -8); p.lineTo(24, 8); p.close()
    c.drawPath(p, paint("#3A3A3C", a))
    rrect(c, 70, -24, 260, 48, 6, "#F2C230", a)
    rrect(c, 318, -24, 14, 48, 2, "#B8B8BC", a)
    rrect(c, 330, -24, 44, 48, 6, "#F49AB0", a)
    c.restore()


def b_lapis(c, t, C, B):
    head(c, t, B["start"], "POR QUE O LÁPIS ESCREVE?", "AS FOLHAS ESCORREGAM", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["12.t"], 0.5)
    mv = ease_io(prog(t, C["12.a"], 4.0))
    # lado direito: lápis riscando o papel
    py = 600
    rrect(c, 900, py, 800, 36, 8, "#FFFDF5", a0, stroke=2, stroke_color=LIGHT)
    text(c, "papel", 930, py + 76, 26, "bold", INK2, a0, align="left")
    px = lerp(960, 1620, mv)
    if mv > 0:
        rrect(c, 960, py - 5, px - 960, 9, 4, "#4A4A4E", a0 * 0.85)
    lapis_escrevendo(c, px, py - 4, a0)
    # lupa na ponta
    c.drawCircle(px, py - 4, 26, paint(BLUE, a0 * ep(t, C["12.a"], 0.5), stroke=4))
    line(c, px - 22, py - 20, 760, 300, BLUE, a0 * ep(t, C["12.a"], 0.5) * 0.6, 3, dash=[8, 8])
    # zoom (vista de lado): folhas de carbono escorregando
    zx, zy, zr = 520, 470, 250
    az = ep(t, C["12.t"] + 0.3, 0.5)
    if az > 0:
        c.save()
        c.clipPath(skia.Path.Circle(zx, zy, zr), doAntiAlias=True)
        rrect(c, zx - zr, zy - zr, 2 * zr, 2 * zr, 0, "#FFFFFF", az)
        rrect(c, zx - zr, zy + 170, 2 * zr, 90, 0, "#FFFDF5", az)
        n_f, sp = 6, 30
        for k in range(n_f):
            yk = zy + 150 - k * 52
            # a folha de baixo fica no papel (anda para a esquerda); as de cima andam menos
            off = -(mv * 900) * (1 - k / (n_f - 1)) ** 1.5
            for j in range(-12, 13):
                xk = zx + ((j * sp + off) % (sp * 25)) - sp * 12.5
                ball(c, xk, yk, 11, az, CGRAY)
                if j < 12:
                    line(c, xk + 11, yk, xk + sp - 11, yk, GREEN, az * 0.7, 3)
            if k < n_f - 1:
                for j in range(-6, 7, 2):
                    xk = zx + j * sp * 2
                    line(c, xk, yk - 14, xk, yk - 38, RED, az * 0.5, 2, dash=[3, 4])
        c.restore()
        c.drawCircle(zx, zy, zr, paint(BLUE, az, stroke=5))
        pill(c, "ZOOM NA PONTA", zx, zy - zr + 6, BLUE, size=22, a=az, anchor="center", bounds=(0, 1920))
    pill(c, "folhas escorregam", 1290, 300, BLUE, size=28, a=ep(t, C["12.a"] + 0.6, 0.5), anchor="center", bounds=(0, 1920))
    pill(c, "as que ficam no papel = o traço", 1290, 380, INK2, size=26, a=ep(t, C["12.b"], 0.5), anchor="center", bounds=(0, 1920))
    pill(c, "grafite = MACIO", 1290, 730, GREEN, size=28, a=ep(t, C["12.c"], 0.5), anchor="center", bounds=(0, 1920))
    estrutura(c, t, C["12.d"])


# ======================================================================
# bloco d: grafeno, nanotubo, fulereno, nanotecnologia
# ======================================================================

def b_grafeno(c, t, C, B):
    head(c, t, B["start"], "UMA CARTA SÓ", "GRAFENO", BLUE)
    card(c, 140, 150, 1000, 610)
    f = ease_io(prog(t, C["13.t"] + 0.4, 2.2))
    g = st_grafite()
    pts = [(x, y + (f * 2.2 if i < N_LAYER else -f * 1.5), z) for i, (x, y, z) in enumerate(g)]
    al = [1.0 if i < N_LAYER else 1 - f for i in range(N_AT)]
    yaw = 25 + (t - B["start"]) * 6
    pitch = lerp(13, 40, f)
    carbono(c, pts, 640, lerp(440, 500, f), lerp(40, 46, f), 1.0, yaw, pitch, bonds=bonds_grafite(), alphas=al)
    aa = ep(t, C["13.a"], 0.5)
    pill(c, "espessura de 1 átomo", 640, 718, BLUE, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab, dy = rise(t, C["13.t"])
    card(c, 1180, 150 + dy, 580, 400, ab)
    if ab > 0:
        baralho(c, 1400, 420 + dy, ab * (1 - 0.5 * f), 0.8, n=5)
        rrect(c, 1500, lerp(330, 250, f) + dy, 180, 115, 10, "#FFFFFF", ab, shadow=True, stroke=2.5, stroke_color=LIGHT)
        rrect(c, 1510, lerp(340, 260, f) + dy, 160, 95, 6, "#E5484D", ab * 0.9)
        text(c, "1 carta = grafeno", 1470, 515 + dy, 28, "black", INK, ab)
    V.defbox(c, "GRAFENO", "uma única folha de carbono", 1470, 640, ep(t, C["13.b"], 0.5), w=560)
    pill(c, "quase transparente · muito resistente", 1470, 770, INK2, size=24, a=ep(t, C["13.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_nanotubo(c, t, C, B):
    head(c, t, B["start"], "A CARTA ENROLADA", "NANOTUBO", BLUE)
    card(c, 140, 150, 1000, 690)
    f = ease_io(prog(t, C["14.t"] + 0.5, 2.6))
    pts = st_rolo(f)
    yaw = lerp(25, 75, f) + (t - B["start"]) * 3
    carbono(c, pts, 640, 430, lerp(46, 52, f), 1.0, yaw, lerp(40, 18, f), bonds=bonds_folha())
    V.defbox(c, "NANOTUBO", "folha de grafeno enrolada em tubo", 640, 740, ep(t, C["14.a"], 0.5), w=760)
    ab, dy = rise(t, C["14.b"])
    card(c, 1180, 150 + dy, 580, 690, ab)
    if ab > 0:
        fulereno(c, 1470, 380 + dy, 130, ab, (t - C["14.b"]) * 25)
        text(c, "FULERENO", 1470, 590 + dy, 40, "black", INK, ab)
        text(c, "formato de bola de futebol", 1470, 640 + dy, 28, "bold", INK2, ab)
        pill(c, "só o nome", 1470, 740 + dy, GREEN, size=26, a=ep(t, C["14.b"] + 1.5, 0.5), anchor="center", bounds=(0, 1920))


def b_nanotec(c, t, C, B):
    head(c, t, B["start"], "POR QUE CAI NO ENEM?", "NANOTECNOLOGIA", BLUE)
    card(c, *CARD_R)
    V.defbox(c, "NANOTECNOLOGIA", "tecnologia com coisas do tamanho de átomos", W / 2, 240, ep(t, C["15.a"], 0.5), w=900)
    ab = ep(t, C["15.b"], 0.5)
    pill(c, "materiais leves e resistentes", 640, 380, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
    acn = ep(t, C["15.c"], 0.5)
    pill(c, "CONDUTIVIDADE = deixar a eletricidade passar", 1280, 380, BLUE, size=28, a=acn, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["15.d"], 0.5)
    kinds = ["diamante", "grafite", "grafeno", "nanotubo", "fulereno"]
    for k, kd in enumerate(kinds):
        a = ad * ep(t, C["15.d"] + 0.45 * k, 0.4)
        x = 320 + k * 320
        mini(c, kd, x, 540, 19, a, t)
        text(c, kd, x, 670, 28, "black", INK, a)
    pill(c, "tudo CARBONO PURO", W / 2, 735, GREEN, size=28, a=ep(t, C["15.d"] + 2.6, 0.5), anchor="center", bounds=(0, 1920))
    estrutura(c, t, C["15.e"])


# ======================================================================
# bloco e: fósforo e enxofre
# ======================================================================

def b_outros(c, t, C, B):
    head(c, t, B["start"], "OUTROS ALÓTROPOS", "SÓ PARA RECONHECER", BLUE)
    ab, dy = rise(t, C["16.b"])
    card(c, 160, 190 + dy, 780, 540, ab)
    if ab > 0:
        text(c, "FÓSFORO", 550, 250 + dy, 34, "black", V.eltxt("P"), ab)
        P4(c, 380, 420 + dy, 60, ab, "#F6EBD9")
        cadeia(c, 720, 420 + dy, 46, ab, "#C0392B", 5)
        text(c, "branco", 380, 580 + dy, 32, "black", INK, ab)
        text(c, "vermelho", 720, 580 + dy, 32, "black", "#C0392B", ab)
    ac, dy2 = rise(t, C["16.c"])
    card(c, 980, 190 + dy2, 780, 540, ac)
    if ac > 0:
        text(c, "ENXOFRE", 1370, 250 + dy2, 34, "black", V.eltxt("S"), ac)
        cristal(c, 1180, 420 + dy2, ac, 0.9)
        cristal(c, 1560, 420 + dy2, ac, 0.9, agulha=True)
        text(c, "rômbico", 1180, 580 + dy2, 32, "black", INK, ac)
        text(c, "monoclínico", 1560, 580 + dy2, 32, "black", INK, ac)
        text(c, "duas formas de cristal", 1370, 660 + dy2, 26, "bold", INK2, ac)
    regra(c, "viu esses nomes → É ALOTROPIA", W / 2, 810, ep(t, C["16.d"], 0.5), 34, GREEN, w=800)


# ======================================================================
# bloco f: substâncias diferentes
# ======================================================================

def b_diferentes(c, t, C, B):
    head(c, t, B["start"], "ALÓTROPOS SÃO", "SUBSTÂNCIAS DIFERENTES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["17.t"], 0.5)
    V.mol(c, "O2", 380, 320, 46, a0)
    V.mol(c, "O3", 760, 320, 42, a0)
    mini(c, "diamante", 1160, 330, 17, a0, t)
    mini(c, "grafite", 1540, 330, 17, a0, t)
    aa = ep(t, C["17.a"], 0.5)
    for x in (570, 1350):
        text_mid(c, "≠", x, 320, 90, "black", PURPLE, aa)
    pill(c, "versões da mesma?", 960, 470, AMBER, size=28, fg=INK, a=a0 * (1 - aa), anchor="center", bounds=(0, 1920))
    regra(c, "mesmo elemento, substâncias DIFERENTES", W / 2, 520, ep(t, C["17.c"], 0.5), 34, PURPLE, w=1000)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        for k, f in enumerate(("O2", "O3", "C")):
            V.formula(c, f, 620 + k * 340, 680, 80, ad, lit=ep(t, C["17.d"] + 0.4 * k, 0.4))
            text(c, "SIMPLES", 620 + k * 340, 770, 26, "black", PURPLE, ad)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Alotropia: um elemento, várias substâncias simples.",
          "Muda o arranjo ou o número de átomos, muda a substância.",
          "A estrutura decide a propriedade."]


def b_recap(c, t, C, B):
    sid = "18" if B["start"] < C["26"] - 1 else "26"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", BLUE), ("b", GREEN), ("c", PURPLE))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        text(c, FRASES[k], 290, y, 46, "black", INK, a, align="left")


def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "\"O₂ E O₃ SÃO A MESMA\"", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            V.mol(c, "O2", x + cw / 2 - 100, y + 470, 26, a)
            V.mol(c, "O3", x + cw / 2 + 90, y + 470, 24, a)
    V.erro_tiles(c, t, [(C["19.a"], "O ERRO", ["!O₂ e O₃ são", "!a mesma"], RED),
                        (C["19.b"], "POR QUE PARECE CERTO", ["os dois são", "oxigênio, com a", "mesma letra O"], AMBER),
                        (C["19.c"], "A CORREÇÃO", ["atomicidade e", "propriedades ≠", "!DIFERENTES"], GREEN)], extra)


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "\"É POR CAUSA DE IMPUREZAS\"", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            mini(c, "diamante", x + cw / 2 - 110, y + 470, 12, a, t)
            mini(c, "grafite", x + cw / 2 + 110, y + 470, 12, a, t)
    V.erro_tiles(c, t, [(C["20.a"], "O ERRO", ["!o grafite tem", "!impurezas"], RED),
                        (C["20.b"], "POR QUE PARECE CERTO", ["coisas parecidas", "e diferentes:", "a gente pensa", "em sujeira"], AMBER),
                        (C["20.c"], "A CORREÇÃO", ["os dois são", "carbono puro", "!o ARRANJO muda"], GREEN)], extra)


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "\"ALÓTROPO COMPOSTO\"", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            V.formula(c, "O3", x + cw / 2 - 90, y + 480, 60, a, lit=1)
            V.formula(c, "C", x + cw / 2 + 90, y + 480, 60, a, lit=1)
    V.erro_tiles(c, t, [(C["21.a"], "O ERRO", ["!algum alótropo", "!é composto"], RED),
                        (C["21.b"], "POR QUE PARECE CERTO", ["são substâncias", "diferentes, e O₃", "tem 3 átomos"], AMBER),
                        (C["21.c"], "A CORREÇÃO", ["conte as letras:", "1 letra só", "!sempre SIMPLES"], GREEN)], extra)


# ======================================================================
# questão 5
# ======================================================================

ALTS = [("A", "impurezas diferentes em cada um", "24.a", "o enunciado diz: só carbono"),
        ("B", "arranjo diferente dos átomos no retículo", None, ""),
        ("C", "o diamante é substância composta", "24.c", "1 letra: simples"),
        ("D", "diferença de massa atômica dos carbonos", "25.d", "as mesmas peças"),
        ("E", "misturas de elementos diferentes", "24.e", "1 elemento, puro")]
ALT_CUE = ["23.a", "23.b", "23.c", "23.d", "23.e"]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "GRAFITE × DIAMANTE", BLUE)
    card(c, 140, 160, 1060, 600)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    for k, (cue, s) in enumerate((("22.e1", "Grafite e diamante: SÓ átomos de carbono."),
                                  ("22.e2", "Diamante: o mais duro · grafite: macio, do lápis."),
                                  ("22.e3", "Essa diferença é explicada:"))):
        text(c, s, 180, 280 + k * 48, 30, "black", INK if k < 2 else INK2, ep(t, C[cue], 0.5), align="left")
    aok = ep(t, C["25.ok"], 0.5)
    for k, (L, s, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[ALT_CUE[k]])
        y = 450 + k * 60 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 170, y - 40, 1000, 58, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 21, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 245, y, 29, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 240, y - 10, 250 + text_w(s, "black", 29), y - 10, ax, RED, ax)
            text(c, why, 1160, y - 2, 22, "black", RED, ax, align="right")
    pause_ = ep(t, C["23.p"], 0.5) * (1 - prog(t, C["24.t"] - 0.3, 0.4))
    V.pause_badge(c, 1350, 420, pause_)
    ar = ep(t, C["24.t"], 0.5)
    card(c, 1240, 160, 540, 600, ar)
    if ar > 0:
        mini(c, "diamante", 1510, 290, 15, ar, t)
        text(c, "trepa-trepa", 1510, 410, 28, "black", INK, ar)
        mini(c, "grafite", 1510, 530, 15, ar, t)
        text(c, "baralho", 1510, 640, 28, "black", INK, ar)
        pill(c, "RESPOSTA: B", 1510, 710, GREEN, size=30, a=aok, anchor="center", bounds=(0, 1920))
    estrutura(c, t, C["25.x"])


# ======================================================================
# ponte e CTA
# ======================================================================

def garrafa(c, cx, cy, a):
    if a <= 0:
        return
    rrect(c, cx - 50, cy - 90, 100, 200, 26, "#CFE6FA", a, stroke=4, stroke_color="#7FB2F0")
    rrect(c, cx - 22, cy - 140, 44, 56, 10, "#CFE6FA", a, stroke=4, stroke_color="#7FB2F0")
    rrect(c, cx - 26, cy - 160, 52, 22, 6, "#3B6CF6", a)
    rrect(c, cx - 50, cy - 20, 100, 60, 4, "#FFFFFF", a)
    text_mid(c, "MINERAL", cx, cy + 10, 16, "black", "#3B6CF6", a)


def anel(c, cx, cy, a):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(cx - 90, cy - 60, 180, 120), paint("#E8B53A", a, stroke=22))
    c.drawOval(skia.Rect.MakeXYWH(cx - 90, cy - 60, 180, 120), paint("#B8860B", a, stroke=3))
    V.diamante(c, cx, cy - 80, a, 0.32)


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MISTURAS", PURPLE)
    card(c, *CARD_R)
    text(c, "até agora: só substâncias PURAS", W / 2, 240, 36, "black", INK, ep(t, C["27.t"], 0.5))
    items = [("27.b", "o ar"), ("27.c", "a água mineral"), ("27.d", "um anel de ouro")]
    for k, (cue, s) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 480 + k * 480
        if k == 0:
            V.bexiga(c, x, 430 + dy, a, 0.9, BLUE)
        elif k == 1:
            garrafa(c, x, 450 + dy, a)
        else:
            anel(c, x, 470 + dy, a)
        text(c, s, x, 640 + dy, 34, "black", INK, a)
        pill(c, "não é puro", x, 700 + dy, AMBER, size=24, fg=INK, a=a, anchor="center", bounds=(0, 1920))
    pill(c, "EPISÓDIO 3: MISTURAS", W / 2, 800, PURPLE, size=32, a=ep(t, C["27.e"], 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Você sabia que diamante e grafite eram a mesma coisa?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, **{"def": b_def}, oxigenio=b_oxigenio,
              atomicidade=b_atomicidade, ozonio=b_ozonio, carbono=b_carbono, diamante=b_diamante, grafite=b_grafite,
              lapis=b_lapis, grafeno=b_grafeno, nanotubo=b_nanotubo, nanotec=b_nanotec, outros=b_outros,
              diferentes=b_diferentes, recap=b_recap, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3,
              questao=b_questao, ponte=b_ponte, cta=b_cta)
