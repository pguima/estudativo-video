"""Visual — Park Anything 002 (1920x1080, inglês): How to Parallel Park a Limousine.
Mesmo sistema do 001: mundo 3D contínuo em BACKGROUND(c, t) (motor 001/roteiro/mundo3d.py, cenário rua.py), câmera
em planos encadeados, cortina de faixas para os cortes, e os componentes de interface do 001 (placas amarelas e
pretas, etiqueta do passo, volante com a mão embaixo, mascote-cone), carregados de 001/roteiro/visual.py como
biblioteca. A limusine segue a trajetória física de baliza.py: a tentativa "de carro" (bate no meio-fio) e a versão
para limusine (~4 pés de folga, ~20°, vaga de ~41 pés)."""
import importlib.util
import json
import math
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
import skia

AQUI = Path(__file__).resolve().parent
P001 = AQUI.parents[1] / "001_tractor_trailer_loading_dock" / "roteiro"
sys.path[:0] = [str(AQUI), str(P001)]

import motor  # noqa: E402
from motor import clamp, ease_io, ease_out, ep, prog, paint, hexc  # noqa: E402
import baliza as BZ  # noqa: E402
import rua  # noqa: E402
from mundo3d import Camera, Cena, linha3d  # noqa: E402


def _lib():
    spec = importlib.util.spec_from_file_location("pa001_visual", P001 / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B1 = _lib()
txt, tw, fnt, etiqueta, faixas, cartao, chip_passo, volante = (B1.txt, B1.tw, B1.fnt, B1.etiqueta, B1.faixas, B1.cartao,
                                                               B1.chip_passo, B1.volante)
cortina, mascote, seta_chao, ponto_tela = B1.cortina, B1.mascote, B1.seta_chao, B1.ponto_tela
AMARELO, PRETO, LARANJA, BRANCO, VERDE, VERMELHO = B1.AMARELO, B1.PRETO, B1.LARANJA, B1.BRANCO, B1.VERDE, B1.VERMELHO

ARQUIVO_FINAL = "park_anything_002_parallel_park_limousine.mp4"
MARCA = ""
SOM = None   # som próprio: som/mixar.py

PROJ = AQUI.parent
PE = 0.3048


# ---------------------------------------------------------------- tempos
@lru_cache(None)
def _C():
    tempos = json.loads((PROJ / "audio" / "tempos.json").read_text(encoding="utf-8"))
    C = {}
    for s in tempos["scenes"]:
        C[s["id"]] = s["start"]
        C[s["id"] + ".end"] = s["start"] + s["dur"]
        for k, v in s["cues"].items():
            C[f"{s['id']}.{k}"] = s["start"] + v
    C["total"] = tempos["total"]
    return C


def K(n):
    return _C()[n]


# ---------------------------------------------------------------- linha do tempo da limusine
def _rotas():
    return BZ.limo()[0], BZ.falha()[0]


def _marcos():
    rl, _ = _rotas()
    return {f: BZ.marco(rl, f) for f in "ABCD"} | {"fim": rl[-1][5]}


def _segmentos():
    """(t0, t1, v0, v1) de s e de dx; e os intervalos em que vale a rota da falha"""
    M = _marcos()
    Lf = _rotas()[1][-1][5]
    S = [
        (K("01.c") + 0.4, K("01.c") + 4.4, 0.0, M["fim"]),
        (K("02") - 0.01, K("02"), M["fim"], 0.0),
        (K("03.a") + 0.3, K("03.c") + 0.25, 0.0, Lf),
        (K("05") - 0.01, K("05"), Lf, 0.0),
        (K("06.b") + 0.3, K("06.d") + 1.8, 0.0, M["B"]),
        (K("07.a") + 0.4, K("07.b") + 2.4, M["B"], M["C"]),
        (K("08.a") + 0.4, K("08.b") + 1.4, M["C"], M["D"]),
        (K("09.a") + 0.5, K("09.b") + 0.6, M["D"], M["fim"]),
        (K("11") - 0.01, K("11"), M["fim"], 0.0),
        (K("11.b") + 0.2, K("11.f") + 1.4, 0.0, M["fim"]),
    ]
    DX = [
        (0.0, 0.01, 0.0, -30.0),
        (0.3, K("01.b") + 0.6, -30.0, 0.0),
        (K("05") - 0.01, K("05"), 0.0, -26.0),
        (K("05.a") + 0.1, K("05.c") + 0.8, -26.0, 0.0),
    ]
    falha = [(K("02"), K("05"))]
    return S, DX, falha


def _avalia(segs, t, v0):
    v = v0
    for t0, t1, a, b in segs:
        if t >= t1:
            v = b
        elif t >= t0:
            v = a + (b - a) * ease_io((t - t0) / max(1e-6, t1 - t0))
            break
        else:
            break
    return v


@lru_cache(None)
def _tabela():
    S, DX, FALHA = _segmentos()
    fps = motor.FPS
    n = int((K("total") + 2) * fps) + 2
    ts = np.arange(n) / fps
    s = np.array([_avalia(S, t, 0.0) for t in ts])
    dx = np.array([_avalia(DX, t, 0.0) for t in ts])
    rl, rf = _rotas()
    modo = np.array([any(a <= t < b for a, b in FALHA) for t in ts])
    d_alvo = np.array([BZ.pose(rf if m else rl, v)["d"] for v, m in zip(s, modo)])
    vel = np.gradient(s, ts)
    d_show = np.zeros(n)
    dv = 0.0
    for i in range(n):
        alvo = d_alvo[i] if abs(vel[i]) > 0.02 else (d_alvo[i] if s[i] > 0.05 else 0.0)
        rate = math.radians(60) / fps
        dv += max(-rate, min(rate, alvo - dv))
        if abs(s[i] - (s[i - 1] if i else 0)) > 1.0:   # corte (cortina): pula direto
            dv = alvo
        d_show[i] = dv
    return ts, s, dx, d_show, vel, modo


def limo(t):
    ts, s, dx, d_show, vel, modo = _tabela()
    i = min(len(ts) - 1, max(0, int(round(t * motor.FPS))))
    rl, rf = _rotas()
    p = BZ.pose(rf if modo[i] else rl, float(s[i]))
    p.update(dx=float(dx[i]), dshow=float(d_show[i]), vel=float(vel[i]), falha=bool(modo[i]))
    p["x"] += p["dx"]
    return p


# ---------------------------------------------------------------- câmera
def _planos():
    xm = BZ.XB - BZ.VAGA / 2          # meio da vaga

    def chega(t, p):
        u = ease_io(prog(t, 0, K("01.b") + 0.6))
        return (p["x"] - 10 + 6 * u, 14.5, 3.0 + 2 * u), (p["x"] + 4, 2.5, 1.0), 46

    def vaga(t, p):
        u = prog(t, K("01.b"), 6)
        return (xm + 7 - 3 * u, 16.5, 13 + 2 * u), (xm, 0.8, 0), 42

    def previa(t, p):
        u = prog(t, K("01.c"), 6)
        a = math.radians(70 + 30 * u)
        return (xm + 26 * math.cos(a), 1 + 14 * math.sin(a), 22), (xm + 1, 1.2, 0), 44

    def titulo(t, p):
        u = prog(t, K("01.d"), 5)
        return (xm + 12 - 4 * u, 16.5, 5 + 2 * u), (xm - 2, 1.5, 1.2), 48

    def regra(t, p):
        u = prog(t, K("02"), 12)
        return (xm + 2 + 2 * u, 12.5, 30), (xm + 2, 1.0, 0), 44

    def falha(t, p):
        u = prog(t, K("03"), 6)
        return (xm + 6, 14.5 - 1.5 * u, 9), (xm + 1, 1.5, 0.4), 46

    def porque(t, p):
        return (xm + 14, 9, 52), (xm + 14, 8, 0), 44

    def chega2(t, p):
        return (p["x"] - 4, 16.5, 9.5), (p["x"] + 6, 2.0, 0.5), 46

    def passo2(t, p):
        u = prog(t, K("06"), 10)
        return (xm + 10 + 4 * u, 16.5, 16), (xm + 2, 2.5, 0), 44

    def passo3(t, p):
        return (BZ.XB + 7, 15.5, 7.5), (BZ.XB - 3, 1.5, 0.6), 46

    def passo4(t, p):
        u = prog(t, K("08"), 8)
        return (xm - 9 + 3 * u, 16, 11), (xm + 1, 1.2, 0), 46

    def passo5(t, p):
        return (xm - 13, 12, 7), (xm, 1.2, 0.4), 46

    def espaco(t, p):
        return (xm, 6.5, 34), (xm, 1.2, 0), 42

    def resumo(t, p):
        return (xm + 2, 9.5, 38), (xm + 2, 2.2, 0), 42

    def final(t, p):
        u = prog(t, K("12"), 13)
        a = math.radians(60 + 25 * u)
        return (xm + 22 * math.cos(a), 1 + 15 * math.sin(a), 10 + 4 * u), (xm, 1.2, 0.6), 44

    return [(0.0, chega, True), (K("01.b") - 0.2, vaga, False), (K("01.c") + 0.2, previa, False),
            (K("01.d") + 0.4, titulo, False), (K("02"), regra, True), (K("03"), falha, False), (K("04"), porque, False),
            (K("05"), chega2, True), (K("06"), passo2, False), (K("07"), passo3, False), (K("08"), passo4, False),
            (K("09"), passo5, False), (K("10"), espaco, False), (K("11"), resumo, True), (K("12"), final, False)]


@lru_cache(None)
def PLANOS():
    return _planos()


_TREME = {}


def camera(t, p):
    pl = PLANOS()
    i = max(k for k in range(len(pl)) if pl[k][0] <= t) if t >= pl[0][0] else 0
    t0, fn, corte = pl[i]
    e1, a1, f1 = fn(t, p)
    if i > 0 and not corte:
        u = ease_io(prog(t, t0, 1.5))
        if u < 1:
            e0, a0, f0 = pl[i - 1][1](t, p)
            e1 = tuple(np.array(e0) * (1 - u) + np.array(e1) * u)
            a1 = tuple(np.array(a0) * (1 - u) + np.array(a1) * u)
            f1 = f0 * (1 - u) + f1 * u
    # tremida na batida
    tb = K("03.c") + 0.25
    if tb <= t < tb + 0.6:
        k = (1 - (t - tb) / 0.6) * 0.35
        e1 = (e1[0] + k * math.sin(t * 90), e1[1] + k * math.cos(t * 77), e1[2] + k * 0.5 * math.sin(t * 63))
    return Camera(e1, a1, f1)


# ---------------------------------------------------------------- mundo
_ULT = {}


def BACKGROUND(c, t):
    p = limo(t)
    cam = camera(t, p)
    _ULT.update(cam=cam, p=p, t=t)
    B1._ceu(c)
    cena = Cena(cam)
    vk = ep(t, K("01.b"), 0.5) * (1 - ep(t, K("01.c") + 0.4, 0.4)) + ep(t, K("10"), 0.5) * (1 - ep(t, K("11"), 0.3))
    rua.montar_rua(cena, t, vaga_k=vk)
    rua.estacionados(cena)
    rua.limusine(cena, p["x"], p["y"], p["th"], p["dshow"])
    cena.sobre_chao.append(lambda cc, cm: _chao(cc, cm, t, p))
    cena.desenhar(c)
    B1._haze(c)
    # flash vermelho na batida
    tb = K("03.c") + 0.25
    if tb <= t < tb + 0.7:
        c.drawRect(skia.Rect.MakeWH(1920, 1080), paint(VERMELHO, 0.35 * (1 - (t - tb) / 0.7)))


def _canto(rota, sv, idx):
    q = BZ.pose(rota, sv)
    return BZ.cantos(q["x"], q["y"], q["th"])[idx]


def _chao(c, cam, t, p):
    rl, rf = _rotas()
    M = _marcos()
    xB = BZ.XB
    # prévia: o caminho da traseira
    k = ep(t, K("01.c") + 0.2, 0.6) * (1 - ep(t, K("01.d") + 0.6, 0.4))
    if k > 0:
        pts = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in
               ((_canto(rl, v, 0), _canto(rl, v, 1)) for v in np.linspace(0, M["C"] + 2.5, 50))]
        seta_chao(c, cam, pts, a=k, k=ep(t, K("01.c") + 0.2, 3.6), larg=0.7)
    # regra: 31 pés a partir do carro da frente (mínimo da Califórnia) e o comprimento da limusine
    k = ep(t, K("02.c"), 0.4) * (1 - ep(t, K("03"), 0.4))
    if k > 0:
        x31 = xB - (BZ.COMP + 0.914)
        y = 0.6
        linha3d(c, cam, [(x31, y, 0.03), (xB, y, 0.03)], AMARELO, 8, k)
        for xx in (x31, xB):
            linha3d(c, cam, [(xx, y - 0.6, 0.03), (xx, y + 0.6, 0.03)], AMARELO, 8, k)
        q = ponto_tela(cam, ((x31 + xB) / 2, y, 0.05))
        if q is not None:
            etiqueta(c, "31 FT  (28 + 3)", q[0], q[1] + 50, 38, AMARELO, PRETO, k)
    # falha: rastro da quina traseira até o meio-fio
    if K("03") <= t < K("05"):
        kk = ep(t, K("04.d"), 0.4)
        if kk > 0:
            pts = [_canto(rf, v, 0) for v in np.linspace(0, rf[-1][5], 40)]
            linha3d(c, cam, [(x, y, 0.04) for x, y in pts], VERMELHO, 8, kk)
    # por quê: os dois círculos de giro (mesmo esterço; raio no eixo traseiro = entre-eixos / tan)
    k = ep(t, K("04.b") + 0.3, 0.5) * (1 - ep(t, K("05") - 0.3, 0.3))
    if k > 0:
        cx0, cy0 = BZ.XB - BZ.VAGA / 2 + 14, 8.5
        r_carro = 2.99 / math.tan(BZ.DMAX)
        r_limo = BZ.EE / math.tan(BZ.DMAX)
        for r, cor, kk, nome in ((r_carro, BRANCO, k, "CAR"), (r_limo, LARANJA, k * ep(t, K("04.c"), 0.5), "LIMO")):
            if kk <= 0:
                continue
            circ = [(cx0 + r * math.cos(a), cy0 + r * math.sin(a), 0.05) for a in np.linspace(0, 2 * math.pi, 90)]
            linha3d(c, cam, circ, cor, 10, kk)
            q = ponto_tela(cam, (cx0 - r, cy0, 0.05) if nome == "LIMO" else (cx0, cy0 - r, 0.05))
            if q is not None:
                etiqueta(c, nome, q[0], q[1], 40, cor if cor != BRANCO else "#FFFFFF", PRETO, kk)
    # passo 1: 4 pés ao lado do carro da frente
    k = ep(t, K("05.b") + 0.8, 0.4) * (1 - ep(t, K("06"), 0.3))
    if k > 0:
        x = xB + 1.5
        y0, y1 = BZ.Y_CARRO + BZ.CARRO[1], BZ.Y_CARRO + BZ.CARRO[1] + BZ.METODO["folga"]
        linha3d(c, cam, [(x, y0, 0.03), (x, y1, 0.03)], AMARELO, 9, k)
        q = ponto_tela(cam, (x + 1.2, (y0 + y1) / 2, 0.05))
        if q is not None:
            etiqueta(c, "4 FT", q[0], q[1], 40, AMARELO, PRETO, k)
    k = ep(t, K("05.c") + 0.4, 0.4) * (1 - ep(t, K("06"), 0.3))
    if k > 0:
        linha3d(c, cam, [(xB, -0.1, 0.03), (xB, 6.6, 0.03)], BRANCO, 5, k, dash=[16, 12])
    # passo 2: o nariz sai para a faixa (trajetória da quina dianteira esquerda)
    k = ep(t, K("06.c"), 0.4) * (1 - ep(t, K("07"), 0.4))
    if k > 0:
        pts = [_canto(rl, v, 2) for v in np.linspace(0, M["B"], 30)]
        linha3d(c, cam, [(x, y, 0.04) for x, y in pts], LARANJA, 9, k)
    # passo 3: linha do para-choque de B
    k = ep(t, K("07.b"), 0.4) * (1 - ep(t, K("08"), 0.4))
    if k > 0:
        linha3d(c, cam, [(xB, -0.1, 0.03), (xB, 6.0, 0.03)], AMARELO, 6, k, dash=[18, 12])
    # passo 5: distância ao meio-fio
    k = ep(t, K("09.b"), 0.4) * (1 - ep(t, K("10"), 0.4))
    if k > 0:
        x = p["x"] + 2.5
        y1 = min(q[1] for q in BZ.cantos(p["x"], p["y"], p["th"]))
        linha3d(c, cam, [(x, 0.0, 0.05), (x, y1, 0.05)], VERDE, 8, k)
    # espaço necessário: ~40 pés
    k = ep(t, K("10.a") + 0.5, 0.5) * (1 - ep(t, K("11"), 0.3))
    if k > 0:
        xa, xb = xB - BZ.VAGA, xB
        y = 3.2
        linha3d(c, cam, [(xa, y, 0.03), (xb, y, 0.03)], AMARELO, 9, k)
        for xx in (xa, xb):
            linha3d(c, cam, [(xx, y - 0.6, 0.03), (xx, y + 0.6, 0.03)], AMARELO, 9, k)
        q = ponto_tela(cam, ((xa + xb) / 2, y + 1.2, 0.05))
        if q is not None:
            etiqueta(c, "~40 FT", q[0], q[1], 56, AMARELO, PRETO, k)
    # recapitulação
    k = ep(t, K("11.a"), 0.4) * (1 - ep(t, K("12"), 0.4))
    if k > 0:
        pts = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in
               ((_canto(rl, v, 0), _canto(rl, v, 1)) for v in np.linspace(0, M["C"] + 3, 50))]
        seta_chao(c, cam, pts, a=0.55 * k, larg=0.5)


# ---------------------------------------------------------------- interface
def medidor_limo(c, cx, cy, r, ang, a):
    """ângulo da limusine com o meio-fio, com as marcas de 20° (limusine) e 45° (carro)"""
    if a <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r - 40, cy - r - 46, 2 * r + 80, r + 136), 22, 22),
                paint("#0E1116", 0.62 * a))
    ini = 180
    for a0, a1, cor in ((0, 25, VERDE), (25, 45, AMARELO), (45, 60, VERMELHO)):
        pth = skia.Path()
        pth.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini + a0 * 3, (a1 - a0) * 3)
        c.drawPath(pth, paint(cor, a, stroke=18))
    for v, rot in ((20, "LIMO"), (45, "CAR")):
        an = math.radians(ini + v * 3)
        c.drawLine(cx + (r - 22) * math.cos(an), cy + (r - 22) * math.sin(an), cx + (r + 12) * math.cos(an),
                   cy + (r + 12) * math.sin(an), paint(BRANCO, a, stroke=4))
        txt(c, rot, cx + (r + 34) * math.cos(an), cy + (r + 30) * math.sin(an), 16, "display", "#C9D1DC", a, "center")
    v = max(0, min(60, ang))
    an = math.radians(ini + v * 3)
    pp = paint(BRANCO, a, stroke=7)
    pp.setStrokeCap(skia.Paint.kRound_Cap)
    c.drawLine(cx, cy, cx + (r - 6) * math.cos(an), cy + (r - 6) * math.sin(an), pp)
    c.drawCircle(cx, cy, 11, paint(BRANCO, a))
    cor = VERDE if v < 25 else AMARELO if v < 45 else VERMELHO
    txt(c, f"{v:.0f}°", cx, cy + 46, 44, "display", cor, a, "center")
    txt(c, "ANGLE TO CURB", cx, cy - r - 22, 20, "display", "#C9D1DC", a, "center", track=2)


def chip(c, rot, titulo, t0, t1, t):
    """etiqueta do passo (como a do 001, com o rótulo da esquerda livre)"""
    k = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.3))
    if k <= 0:
        return
    x, y = 70 - (1 - ease_out(prog(t, t0, 0.5))) * 80, 84
    w1 = tw(rot, 34, "display") + 44
    w2 = tw(titulo, 40, "black") + 52
    h = 74
    sh = paint("#000000", 0.35 * k)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 6, w1 + w2, h), 12, 12), sh)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w1 + w2, h), 12, 12), paint(PRETO, 0.92 * k))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w1, h), 12, 12), paint(AMARELO, k))
    c.drawRect(skia.Rect.MakeXYWH(x + w1 - 12, y, 12, h), paint(AMARELO, k))
    txt(c, rot, x + w1 / 2, y + h / 2, 34, "display", PRETO, k, "center")
    txt(c, titulo, x + w1 + 26, y + h / 2, 40, "black", BRANCO, k)


def hud(c, t, t0, t1, seta=0.0):
    k = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.4))
    if k <= 0:
        return
    p = _ULT["p"]
    volante(c, 190, 860, 110, p["dshow"], k, mao=False, seta=seta)
    medidor_limo(c, 1600, 900, 110, math.degrees(p["th"]), k)


def b_gancho(c, t, Cc, B):
    ta, tb, tc, td = (K(f"01.{k}") for k in "abcd")
    p = _ULT["p"]
    cam = _ULT["cam"]
    k = ep(t, ta + 0.8, 0.5) * (1 - ep(t, tb - 0.2, 0.3))
    if k > 0:
        a = BZ.cantos(p["x"], p["y"], p["th"])
        xa, xb = a[1][0], a[2][0]
        y, z = a[1][1] + 0.05, 1.9
        linha3d(c, cam, [(xa, y, z), (xb, y, z)], AMARELO, 7, k)
        for xx in (xa, xb):
            linha3d(c, cam, [(xx, y, z - 0.3), (xx, y, z + 0.3)], AMARELO, 7, k)
        q = ponto_tela(cam, ((xa + xb) / 2, y, z))
        if q is not None:
            etiqueta(c, "28 FT", q[0], q[1] - 50, 54, AMARELO, PRETO, k * ep(t, ta + 1.2, 0.3))
    B1._ULT.update(cam=cam)
    B1.ancorado(c, "THE SPACE", (BZ.XB - BZ.VAGA / 2, 1.2, 1.4), a=ep(t, tb + 0.5, 0.4) * (1 - ep(t, tc, 0.3)), size=40, dy=-90)
    cartao(c, "IN ONE GO?", tc + 1.2, td - 0.1, t, y=150, size=64)
    kt = ep(t, td + 0.4, 0.5)
    if kt > 0:
        y = 470
        g = skia.Paint()
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(960, y + 60), 900, [hexc("#0B0F17", 0.62 * kt), hexc("#0B0F17", 0.0)]))
        c.drawRect(skia.Rect.MakeWH(1920, 1080), g)
        sl = (1 - ease_out(prog(t, td + 0.4, 0.6))) * 80
        c.save(); c.translate(0, sl)
        etiqueta(c, "PARK ANYTHING", 960, y - 150, 40, PRETO, AMARELO, kt)
        for j, linha in enumerate(("HOW TO PARALLEL PARK", "A LIMOUSINE")):
            kj = ep(t, td + 0.55 + 0.15 * j, 0.4)
            txt(c, linha, 960, y + j * 112, 96, "display", BRANCO, kj, "center")
        cartao(c, "IS THIS EVEN POSSIBLE?", td + 1.0, 99999, t, y=y + 250, size=50)
        c.restore()


def b_regra(c, t, Cc, B):
    ta, tb, tc = (K(f"02.{k}") for k in "abc")
    chip(c, "THE RULE", "SPACE FOR A CAR", ta + 0.3, B["end"], t)
    k = ep(t, tb + 0.4, 0.4) * (1 - ep(t, B["end"], 0.3))
    if k > 0:
        cartao(c, "SPACE = VEHICLE + 3 FT", tb + 0.4, B["end"] + 0.2, t, y=960, size=52)
        txt(c, "California Driver's Handbook", 960, 1038, 26, "semi", "#E9ECEE", k, "center")


def b_falha(c, t, Cc, B):
    ta, tb, tc = (K(f"03.{k}") for k in "abc")
    chip(c, "TRY IT", "THE CAR METHOD", ta + 0.1, B["end"], t)
    hud(c, t, ta + 0.2, B["end"] + 0.4, seta=ep(t, ta + 0.6, 0.4) * (1 - ep(t, tb, 0.4)))
    cartao(c, "2 FT · FULL LOCK · 45°", ta + 0.6, tb, t, y=215, size=50)
    k = ep(t, tc + 0.25, 0.15) * (1 - ep(t, B["end"] + 0.3, 0.3))
    if k > 0:
        c.save(); c.translate(960, 300); c.rotate(-6)
        etiqueta(c, "CURB!", 0, 0, 110 * (1 + 0.3 * (1 - ep(t, tc + 0.25, 0.25))), VERMELHO, BRANCO, k)
        c.restore()


def b_porque(c, t, Cc, B):
    ta, tb, tc, td = (K(f"04.{k}") for k in "abcd")
    cartao(c, "WHEELS 2× FARTHER APART = 2× WIDER CIRCLE", tb + 0.4, td - 0.1, t, y=980, size=44)
    cartao(c, "THE BACK END SWINGS TO THE CURB", td + 0.3, B["end"] + 0.2, t, y=980, size=48)


def b_passo1(c, t, Cc, B):
    ta, tb, tc = (K(f"05.{k}") for k in "abc")
    chip_passo(c, 1, "LINE UP, 4 FEET OUT", ta + 0.3, B["end"], t)
    cartao(c, "THE LIMO VERSION", ta + 0.1, tb - 0.1, t, y=215, size=56)
    cartao(c, "REAR BUMPERS EVEN", tc + 0.3, B["end"] + 0.3, t, y=980, size=50)


def b_passo2(c, t, Cc, B):
    ta, tb, tc, td = (K(f"06.{k}") for k in "abcd")
    chip_passo(c, 2, "BACK IN TO 20°", ta + 0.3, B["end"], t)
    hud(c, t, ta + 0.4, 1e9, seta=ep(t, tb + 0.2, 0.4) * (1 - ep(t, tc + 1.5, 0.4)))
    cartao(c, "CHECK MIRRORS + BLIND SPOT", ta + 0.8, tb - 0.1, t, y=215, size=48)
    cartao(c, "THE NOSE SWINGS OUT", tc + 0.2, td - 0.1, t, y=215, size=52)
    cartao(c, "20°, NOT 45°", td + 0.3, B["end"] + 0.2, t, y=215, size=60)


def b_passo3(c, t, Cc, B):
    ta, tb = K("07.a"), K("07.b")
    chip_passo(c, 3, "STRAIGHTEN AND BACK", ta + 0.3, B["end"], t)
    hud(c, t, B["start"] - 1, 1e9)
    cartao(c, "FRONT CORNER PAST THEIR BUMPER", tb + 0.2, B["end"] + 0.2, t, y=215, size=48)


def b_passo4(c, t, Cc, B):
    ta, tb = K("08.a"), K("08.b")
    chip_passo(c, 4, "SWING THE OTHER WAY", ta + 0.3, B["end"], t)
    hud(c, t, B["start"] - 1, 1e9, seta=-ep(t, ta + 0.4, 0.4) * (1 - ep(t, tb + 1.0, 0.4)))
    cartao(c, "UNTIL IT'S STRAIGHT", tb + 0.2, B["end"] + 0.2, t, y=215, size=56)


def b_passo5(c, t, Cc, B):
    ta, tb = K("09.a"), K("09.b")
    chip_passo(c, 5, "PULL FORWARD, CENTER", ta + 0.3, B["end"], t)
    hud(c, t, B["start"] - 1, B["end"])
    k = ep(t, tb + 0.3, 0.4) * (1 - ep(t, B["end"], 0.3))
    if k > 0:
        p = _ULT["p"]
        mf = min(q[1] for q in BZ.cantos(p["x"], p["y"], p["th"]))
        etiqueta(c, f"{mf * 39.37:.0f} IN FROM THE CURB", 960, 215, 52, VERDE, PRETO, k)
        txt(c, "max 18 in · California Driver's Handbook", 960, 285, 26, "semi", "#FFFFFF", k, "center")


def b_espaco(c, t, Cc, B):
    ta, tb, tc = (K(f"10.{k}") for k in "abc")
    chip(c, "SPACE", "HOW MUCH DOES IT NEED?", ta + 0.3, B["end"], t)
    k = ep(t, tb, 0.4) * (1 - ep(t, B["end"], 0.3))
    if k > 0:
        etiqueta(c, "28 FT LIMO + 12 FT", 960, 960, 52, AMARELO, PRETO, k)
    k2 = ep(t, ta + 0.6, 0.4) * (1 - ep(t, B["end"], 0.3))
    if k2 > 0:
        txt(c, "in our simulation", 960, 1035, 26, "semi", "#FFFFFF", k2, "center")


def b_resumo(c, t, Cc, B):
    ks = [K(f"11.{k}") for k in "bcdef"]
    itens = ("4 FT OUT, BUMPERS EVEN", "BACK IN TO 20°", "STRAIGHTEN", "SWING THE OTHER WAY", "PULL FORWARD")
    k0 = ep(t, K("11.a"), 0.4) * (1 - ep(t, B["end"] - 0.3, 0.3))
    if k0 <= 0:
        return
    x, y0 = 70, 210
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 24, y0 - 70, 640, 5 * 104 + 100), 22, 22), paint("#0E1116", 0.68 * k0))
    txt(c, "RECAP", x, y0 - 22, 34, "display", AMARELO, k0, track=3)
    for j, (s, t0) in enumerate(zip(itens, ks)):
        kj = k0 * ep(t, t0, 0.3)
        y = y0 + 50 + j * 104
        ativo = t0 <= t < (ks[j + 1] if j + 1 < len(ks) else 1e9)
        c.drawCircle(x + 26, y, 26, paint(AMARELO if ativo else "#3A414C", kj))
        txt(c, str(j + 1), x + 26, y, 30, "display", PRETO if ativo else BRANCO, kj, "center")
        txt(c, s, x + 70, y, 32, "black", BRANCO if ativo else "#C9D1DC", kj)


def b_final(c, t, Cc, B):
    ta, tb, tc = (K(f"12.{k}") for k in "abc")
    k = ep(t, ta, 0.5)
    if k <= 0:
        return
    c.drawRect(skia.Rect.MakeWH(1920, 1080), paint("#0B0F17", 0.62 * k))
    x, y, w, h = 160, 250, 900, 520
    sl = (1 - ease_out(prog(t, ta, 0.6))) * 90
    c.save(); c.translate(-sl, 0)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
    c.drawRRect(r, paint("#F7F9FB", k))
    c.save(); c.clipRRect(r, True)
    pg = skia.Paint()
    pg.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y), skia.Point(0, y + h)], [hexc("#8FD0F5"), hexc("#D8F0FB")]))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h * 0.5), pg)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.5, w, h * 0.5), paint("#2F7FC1", k))      # água
    pth = skia.Path()                                                                     # rampa
    pth.moveTo(x, y + h * 0.42); pth.lineTo(x + w * 0.55, y + h * 0.42); pth.lineTo(x + w * 0.8, y + h); pth.lineTo(x, y + h)
    pth.close()
    c.drawPath(pth, paint("#8A9097", k))
    _barco(c, x + w * 0.42, y + h * 0.48, k)
    c.restore()
    etiqueta(c, "NEXT", x + 110, y + 60, 40, PRETO, AMARELO, k)
    txt(c, "BACKING A BOAT TRAILER", x + 40, y + h + 60, 62, "display", BRANCO, k)
    txt(c, "DOWN A RAMP", x + 40, y + h + 130, 62, "display", AMARELO, k)
    c.restore()
    kb = ep(t, tb, 0.5)
    if kb > 0:
        etiqueta(c, "CHAUFFEUR?", 1440, 330, 50, AMARELO, PRETO, kb)
        txt(c, "Tell us your secret", 1440, 420, 40, "bold", BRANCO, kb, "center")
        txt(c, "in the comments", 1440, 470, 40, "bold", BRANCO, kb, "center")
    kc = ep(t, tc, 0.5)
    if kc > 0:
        pulse = 1 + 0.035 * math.sin(t * 5)
        c.save(); c.translate(1440, 640); c.scale(pulse, pulse)
        etiqueta(c, "SUBSCRIBE", 0, 0, 56, VERMELHO, BRANCO, kc)
        c.restore()
        B1.CN.cone_icone(c, 1440, 840, 1.25, olhos=True, t=t, a=kc)


def _barco(c, cx, cy, a):
    """carro + carretinha + barco descendo a rampa (cartão do próximo vídeo)"""
    c.save(); c.translate(cx, cy); c.rotate(24)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-250, -40, 230, 60), 14, 14), paint("#2F5BD3", a))   # carro
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-210, -80, 130, 46), 12, 12), paint("#2F5BD3", a))
    c.drawLine(-20, 10, 40, 10, paint("#3A3F47", a, stroke=8))
    bote = skia.Path()
    bote.moveTo(30, -50); bote.lineTo(300, -50); bote.lineTo(270, 10); bote.lineTo(60, 10); bote.close()
    c.drawPath(bote, paint("#FFFFFF", a))
    c.drawRect(skia.Rect.MakeXYWH(40, -50, 260, 12), paint(LARANJA, a))
    for wx in (-200, -60, 150):
        c.drawCircle(wx, 22, 22, paint("#16181C", a))
    c.restore()


def OVERLAY(c, t):
    mascote(c, t, 1.0 * (1 - ep(t, K("12.c"), 0.3)))
    for tc in (K("02"), K("05"), K("11")):
        cortina(c, t, tc)


BLOCKS = dict(gancho=b_gancho, regra=b_regra, falha=b_falha, porque=b_porque, passo1=b_passo1, passo2=b_passo2,
              passo3=b_passo3, passo4=b_passo4, passo5=b_passo5, espaco=b_espaco, resumo=b_resumo, final=b_final)


def CAPTION(c, scene, t):
    pass
