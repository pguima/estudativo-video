"""Visual — Park Anything 001 (1920x1080, inglês): How to Back a Tractor-Trailer into a Loading Dock.
O mundo 3D (mundo3d.py + cenario.py) é contínuo e fica em BACKGROUND(c, t): câmera com planos encadeados (passagens
suaves ou corte escondido pela cortina de faixas amarelas e pretas), conjunto movido pela trajetória física de
manobra.py. Os blocos desenham só a interface: etiqueta do passo, cartões de instrução (amarelo e preto, a assinatura
do canal), volante com a "mão embaixo", medidor do ângulo do engate, anotações presas em pontos 3D e o mascote-cone."""
import json
import math
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import skia

import motor
from motor import clamp, ease_io, ease_out, ep, prog, paint, hexc
import manobra as MB
import cenario as CN
from mundo3d import Camera, Cena, linha3d, tom

ARQUIVO_FINAL = "park_anything_001_tractor_trailer_loading_dock.mp4"
MARCA = ""
SOM = None   # som próprio: som/mixar.py

PROJ = Path(__file__).resolve().parents[1]
AMARELO, PRETO, LARANJA, BRANCO = CN.AMARELO, "#16181C", CN.LARANJA, "#FFFFFF"
VERDE, VERMELHO = "#2FBF71", "#E5484D"
FONTES = Path(motor.__file__).parent / "fontes"


@lru_cache(None)
def _tf(nome):
    arq = {"display": FONTES / "antigos" / "Rubik-Black.ttf", "bold": FONTES / "inter" / "extras" / "ttf" / "Inter-Bold.ttf",
           "semi": FONTES / "inter" / "extras" / "ttf" / "Inter-SemiBold.ttf",
           "black": FONTES / "inter" / "extras" / "ttf" / "Inter-Black.ttf"}[nome]
    return skia.Typeface.MakeFromFile(str(arq))


def fnt(nome, size):
    f = skia.Font(_tf(nome), size)
    f.setEdging(skia.Font.Edging.kSubpixelAntiAlias)
    f.setSubpixel(True)
    return f


def txt(c, s, x, y, size, nome="bold", cor=BRANCO, a=1.0, align="left", track=0.0):
    """y = centro vertical (pela altura das maiúsculas)"""
    if a <= 0:
        return 0
    f = fnt(nome, size)
    w = f.measureText(s) + track * max(0, len(s) - 1)
    x0 = x - (w / 2 if align == "center" else w if align == "right" else 0)
    yb = y + size * 0.36
    if track:
        for ch in s:
            c.drawString(ch, x0, yb, f, paint(cor, a))
            x0 += f.measureText(ch) + track
    else:
        c.drawString(s, x0, yb, f, paint(cor, a))
    return w


def tw(s, size, nome="bold", track=0.0):
    return fnt(nome, size).measureText(s) + track * max(0, len(s) - 1)


# ---------------------------------------------------------------- tempos (cues)
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


def K(nome):
    return _C()[nome]


# ---------------------------------------------------------------- linha do tempo do conjunto
LTOT = None


def _segmentos():
    """(t0, t1, valor0, valor1) para s (distância da manobra) e dx (deslocamento à frente, só no preparo)"""
    L = MB.comprimento()
    S = [
        (K("01.c") + 0.4, K("01.c") + 4.6, 0.0, L),                 # prévia rápida: a manobra inteira
        (K("02") - 0.01, K("02"), L, 0.0),                           # (cortina) volta ao início
        (K("02.c") + 1.2, K("02.d") + 1.8, 0.0, 4.5),                # mão para a esquerda → carreta para a esquerda
        (K("03") - 0.01, K("03"), 4.5, 0.0),                         # (cortina)
        (K("04.c") - 0.2, K("04.end") + 0.2, 0.0, 6.0),             # vira para a doca (engate ~33°)
        (K("05.a") + 0.2, K("05.c") + 2.2, 6.0, 12.8),               # chega a 45° e contraesterça
        (K("06.a"), K("06.end") + 0.1, 12.8, 25.8),                  # segue a carreta
        (K("07.a") + 0.2, K("07.b") + 1.8, 25.8, 29.6),              # alinha
        (K("07.c"), K("07.end") + 0.2, 29.6, 31.8),                  # ré reta
        (K("08.b") + 0.6, K("08.b") + 3.4, 31.8, 28.8),              # pull-up (para a frente)
        (K("08.c") + 0.2, K("08.c") + 3.0, 28.8, 31.8),              # e volta
        (K("09.c"), K("09.d") + 2.8, 31.8, L),                       # encosta devagar
        (K("10") - 0.01, K("10"), L, 0.0),                           # (cortina) recapitulação
        (K("10.b") + 0.3, K("10.g") + 1.4, 0.0, L),
    ]
    DX = [
        (K("03") - 0.01, K("03"), 0.0, -46.0),
        (K("03.a") + 0.2, K("03.d") + 1.4, -46.0, 0.0),
    ]
    return S, DX


def _avalia(segs, t, v0):
    v = v0
    for t0, t1, a, b in segs:
        if t >= t1:
            v = b
        elif t >= t0:
            u = (t - t0) / max(1e-6, t1 - t0)
            v = a + (b - a) * ease_io(u)
            break
        else:
            break
    return v


@lru_cache(None)
def _tabela():
    """s, dx e esterço exibido (suavizado) para cada quadro"""
    S, DX = _segmentos()
    fps = motor.FPS
    n = int((K("total") + 2) * fps) + 2
    ts = np.arange(n) / fps
    s = np.array([_avalia(S, t, 0.0) for t in ts])
    dx = np.array([_avalia(DX, t, 0.0) for t in ts])
    d_alvo = np.array([MB.estado(v)["d"] for v in s])
    vel = np.gradient(s, ts)
    # o volante: parado, sem movimento, o motorista já vira (passo 2); em movimento para a frente, rodas retas
    d_show = np.zeros(n)
    dv = 0.0
    t_vira = K("04.b") + 0.4
    for i, t in enumerate(ts):
        alvo = d_alvo[i]
        if vel[i] < -0.05:                           # pull-up: para a frente, rodas retas
            alvo = 0.0
        if abs(vel[i]) < 0.02 and s[i] < 0.3 and t >= t_vira and t < K("05"):
            alvo = MB.estado(0.3)["d"]                # vira o volante antes de sair (passo 2)
        if abs(vel[i]) < 0.02 and s[i] < 0.3 and (t < t_vira or t >= K("10")):
            alvo = 0.0 if not (K("02.c") + 0.4 <= t < K("03")) else MB.estado(0.3)["d"]
        rate = math.radians(55) / fps
        dv += max(-rate, min(rate, alvo - dv))
        d_show[i] = dv
    return ts, s, dx, d_show, vel


def rig(t):
    ts, s, dx, d_show, vel = _tabela()
    i = min(len(ts) - 1, max(0, int(round(t * motor.FPS))))
    p = MB.estado(float(s[i]))
    p["dshow"] = float(d_show[i])
    p["dx"] = float(dx[i])
    p["vel"] = float(vel[i])
    return p


# ---------------------------------------------------------------- câmera
def _mid(p):
    hx = p["hx"] + p["dx"]
    tx, ty = CN.traseira_carreta(p, p["dx"])
    return np.array([(hx + tx) / 2, (p["hy"] + ty) / 2])


def _loc(p, lx, ly, lz, quem="cavalo"):
    th = p["th1"] if quem == "cavalo" else p["th2"]
    c, s = math.cos(th), math.sin(th)
    return np.array([p["hx"] + p["dx"] + c * lx - s * ly, p["hy"] + s * lx + c * ly, lz])


def _planos():
    """(início, nome, função(t, pose) → (olho, alvo, fov), corte?)"""
    def lateral(t, p):
        u = ease_io(prog(t, 0, K("01.b") + 0.5))
        x2 = p["x2"] + p["dx"]
        return (x2 - 4 + 16 * u, -45, 4.0 + 1.5 * u), (x2 + 5 + 12 * u, -28, 2.6), 44

    def porta(t, p):
        u = prog(t, K("01.b"), 6)
        return (9 - 2 * u, -19 + 3 * u, 5.5), (0, -0.5, 2.4), 40

    def prevista(t, p):
        u = prog(t, K("01.c"), 8)
        a = math.radians(-118 + 30 * u)
        return (6 + 58 * math.cos(a), -16 + 58 * math.sin(a), 44 - 6 * u), (5, -14, 0), 40

    def titulo(t, p):
        u = prog(t, K("01.d"), 5)
        return (-10 + 6 * u, -40, 9 + 4 * u), (0, -6, 3), 46

    def topo(t, p):
        tx, ty = CN.traseira_carreta(MB.estado(0.0))
        u = prog(t, K("02"), 14)
        return (tx - 24 + 3 * u, ty - 1.5, 17 - 2 * u), (tx + 10, ty + 1.5, 0), 46

    def chase(t, p):
        h = _loc(p, -30, 16, 0)
        a = _loc(p, 6, 0, 0)
        return (h[0], h[1] - 3, 15), (a[0] + 6, a[1] + 10, 1.5), 50

    def janela(t, p):
        e = _loc(p, 3.9, 2.4, 3.3)
        tx, ty = CN.traseira_carreta(p, p["dx"])
        return tuple(e), (tx + 4, ty + 5.5, 1.4), 58

    def preparo(t, p):
        u = prog(t, K("03.d"), 7)
        return (8 + 4 * u, -66, 34), (6, -18, 0), 42

    def aereo(t, p):
        u = prog(t, K("04"), 15)
        return (-20 + 6 * u, -66, 30 + 4 * u), (6 - 2 * u, -20, 0), 42

    def engate(t, p):
        hx, hy = p["hx"] + p["dx"], p["hy"]
        return (hx - 2, hy - 7, 24), (hx - 2, hy + 1, 0), 44

    def segue(t, p):
        m = _mid(p)
        u = prog(t, K("06"), 14)
        a = math.radians(-150 + 50 * u)
        return (m[0] + 30 * math.cos(a), m[1] + 30 * math.sin(a), 22), (m[0], m[1], 0), 44

    def reto(t, p):
        u = prog(t, K("07"), 9)
        return (5 + 3 * u, -44 + 4 * u, 13), (0, -6, 1.5), 42

    def pullup(t, p):
        return (20, -24, 7), (0, -14, 1.8), 44

    def goal(t, p):
        u = prog(t, K("09"), 6)
        return (-9 + 2 * u, -19, 5.5), (0, -6, 1.6), 46

    def fresta(t, p):
        u = prog(t, K("09.c"), 7)
        return (8.5 - 1.0 * u, -10 + 1.0 * u, 3.0), (-0.5, -1.2, 1.4), 46

    def resumo(t, p):
        return (1, -27, 64), (1, -13.5, 0), 40

    def final(t, p):
        u = prog(t, K("11"), 14)
        a = math.radians(-60 + 14 * u)
        return (34 * math.cos(a), -6 + 34 * math.sin(a), 16 + 6 * u), (0, -10, 2), 42

    return [
        (0.0, lateral, True), (K("01.b") - 0.1, porta, False), (K("01.c") + 0.2, prevista, False),
        (K("01.d") + 0.6, titulo, False),
        (K("02"), topo, True), (K("03"), chase, True), (K("03.c") - 0.2, janela, False), (K("03.d") + 0.2, preparo, False),
        (K("04"), aereo, False), (K("05"), engate, False), (K("06"), segue, False), (K("07"), reto, False),
        (K("08.b"), pullup, False), (K("09"), goal, False), (K("09.c") - 0.3, fresta, False),
        (K("10"), resumo, True), (K("11"), final, False),
    ]


@lru_cache(None)
def PLANOS():
    return _planos()


def camera(t, p):
    pl = PLANOS()
    i = max(k for k in range(len(pl)) if pl[k][0] <= t) if t >= pl[0][0] else 0
    t0, fn, corte = pl[i]
    e1, a1, f1 = fn(t, p)
    if i > 0 and not corte:
        u = ease_io(prog(t, t0, 1.6))
        if u < 1:
            e0, a0, f0 = pl[i - 1][1](t, p)
            e1 = tuple(np.array(e0) * (1 - u) + np.array(e1) * u)
            a1 = tuple(np.array(a0) * (1 - u) + np.array(a1) * u)
            f1 = f0 * (1 - u) + f1 * u
    return Camera(e1, a1, f1)


# ---------------------------------------------------------------- mundo + anotações 3D
_ULT = {}


def _ceu(c):
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 0), skia.Point(0, 1080)],
                                               [hexc(CN.CEU_ALTO), hexc(CN.CEU_BAIXO)]))
    c.drawRect(skia.Rect.MakeWH(1920, 1080), p)


def _haze(c):
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 0), skia.Point(0, 420)],
                                               [hexc(CN.CEU_BAIXO, 0.30), hexc(CN.CEU_BAIXO, 0.0)]))
    c.drawRect(skia.Rect.MakeWH(1920, 420), p)
    v = skia.Paint()
    v.setShader(skia.GradientShader.MakeRadial(skia.Point(960, 560), 1250, [hexc("#000000", 0.0), hexc("#0B1020", 0.30)],
                                               [0.55, 1.0]))
    c.drawRect(skia.Rect.MakeWH(1920, 1080), v)


def seta_chao(c, cam, pts, cor=LARANJA, larg=0.9, a=1.0, k=1.0, z=0.03):
    """a seta grossa do canal, pintada no chão: pts (n, 2) em metros; k = quanto já foi desenhado"""
    pts = np.asarray(pts, float)
    if a <= 0 or len(pts) < 2:
        return
    seg = np.hypot(*np.diff(pts, axis=0).T)
    acc = np.concatenate([[0], np.cumsum(seg)])
    L = acc[-1] * clamp(k)
    if L < 0.5:
        return
    n = max(2, int(np.searchsorted(acc, L)))
    P = pts[:n].copy()
    P = np.vstack([P, np.interp(L, acc, pts[:, 0]) * np.array([1, 0]) + np.interp(L, acc, pts[:, 1]) * np.array([0, 1])])
    d = P[-1] - P[-2]
    d = d / (np.linalg.norm(d) + 1e-9)
    nrm = np.array([-d[1], d[0]])
    corpo = P[:-1].tolist() + [(P[-1] - d * larg * 1.4).tolist()]
    # faixa como polígono (largura em metros)
    esq, dir_ = [], []
    for j in range(len(corpo)):
        q = np.array(corpo[j])
        if j < len(corpo) - 1:
            dd = np.array(corpo[j + 1]) - q
        else:
            dd = q - np.array(corpo[j - 1])
        dd = dd / (np.linalg.norm(dd) + 1e-9)
        nn = np.array([-dd[1], dd[0]])
        esq.append(q + nn * larg / 2)
        dir_.append(q - nn * larg / 2)
    poly = esq + dir_[::-1]
    ponta = [P[-1] - d * larg * 1.5 + nrm * larg * 1.15, P[-1] + d * 0.2, P[-1] - d * larg * 1.5 - nrm * larg * 1.15]
    for forma in (poly, ponta):
        Q = np.column_stack([np.array(forma), np.full(len(forma), z)])
        Pc = cam.cam(Q)
        if (Pc[:, 2] < 0.4).any():
            continue
        xy = cam.tela(Pc)
        path = skia.Path()
        path.moveTo(*xy[0])
        for q in xy[1:]:
            path.lineTo(*q)
        path.close()
        sh = paint("#000000", 0.25 * a)
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 6))
        c.save(); c.translate(0, 4); c.drawPath(path, sh); c.restore()
        c.drawPath(path, paint(cor, a))


def caminho_traseira(s0, s1, n=80):
    out = []
    for v in np.linspace(s0, s1, n):
        p = MB.estado(v)
        out.append(CN.traseira_carreta(p))
    return np.array(out)


def ponto_tela(cam, P):
    Pc = cam.cam(np.atleast_2d(P))
    if Pc[0, 2] < 0.5:
        return None
    return cam.tela(Pc)[0]


def BACKGROUND(c, t):
    p = rig(t)
    cam = camera(t, p)
    _ULT.update(cam=cam, p=p, t=t)
    _ceu(c)
    cena = Cena(cam)
    alvo_k = ep(t, K("01.b"), 0.5) * (1 - ep(t, K("02"), 0.3)) + ep(t, K("03.d"), 0.5) * (1 - ep(t, K("06"), 0.6))
    CN.montar_mundo(cena, t, alvo_k=alvo_k)
    if K("05.d") <= t < K("06"):   # fantasma: o que seria o "L" fechado (jackknife)
        kj = ep(t, K("05.d") + 0.2, 0.6) * (1 - ep(t, K("06") - 0.4, 0.4))
        if kj > 0:
            pj = dict(p)
            pj["th1"] = p["th2"] + math.radians(45 + 42 * ease_out(prog(t, K("05.d") + 0.2, 1.4)))
            pj["dshow"] = math.radians(40)
            CN.cavalo(cena, p["hx"] + p["dx"], p["hy"], pj["th1"], pj["dshow"], cor=VERMELHO, alfa=0.45 * kj, sombra=False)
    CN.conjunto(cena, p, dx=p["dx"])
    cena.sobre_chao.append(lambda cc, cm: _sobre_chao(cc, cm, t, p))
    cena.desenhar(c)
    _haze(c)


def _sobre_chao(c, cam, t, p):
    """setas e marcas pintadas no chão (debaixo dos veículos)"""
    L = MB.comprimento()
    # prévia (gancho): o caminho da traseira
    k = ep(t, K("01.c") + 0.1, 1.2) * (1 - ep(t, K("01.d") + 0.8, 0.5))
    if k > 0:
        seta_chao(c, cam, caminho_traseira(0, L), a=k * 0.95, k=ep(t, K("01.c") + 0.1, 3.8))
    # regra: a traseira vai para a esquerda (norte)
    k = ep(t, K("02.d") - 0.2, 0.4) * (1 - ep(t, K("03") - 0.3, 0.3))
    if k > 0:
        tx, ty = CN.traseira_carreta(p, p["dx"])
        seta_chao(c, cam, [(tx - 1.5, ty + 1.8), (tx - 1.5, ty + 8.5)], a=k, k=ep(t, K("02.d") - 0.2, 0.8), larg=1.1)
    # preparo: dirigindo para leste, doca à esquerda
    k = ep(t, K("03.b"), 0.4) * (1 - ep(t, K("03.c") - 0.3, 0.3))
    if k > 0:
        seta_chao(c, cam, [(-30, -23.5), (24, -23.5)], a=k, k=ep(t, K("03.b"), 1.6), larg=1.0)
    # sobra para girar: da porta até a traseira da carreta
    k = ep(t, K("03.d") + 1.4, 0.4) * (1 - ep(t, K("04.c"), 0.4))
    if k > 0:
        tx, ty = CN.traseira_carreta(p, p["dx"])
        y = ty + 2.4
        linha3d(c, cam, [(0, -1, 0.03), (0, y, 0.03)], AMARELO, 5, k, dash=[18, 12])
        linha3d(c, cam, [(0, y, 0.03), (tx, y, 0.03)], AMARELO, 8, k)
        for xx in (0, tx):
            linha3d(c, cam, [(xx, y - 1.0, 0.03), (xx, y + 1.0, 0.03)], AMARELO, 8, k)
    # passo 2 em diante: o caminho planejado da traseira até a porta
    k = ep(t, K("04.d"), 0.5) * (1 - ep(t, K("08"), 0.5))
    if k > 0:
        s0 = p["s"]
        if L - s0 > 1.0:
            seta_chao(c, cam, caminho_traseira(s0, L), a=0.9 * k, k=ep(t, K("04.d"), 1.4), larg=0.75)
    # 45°: arco no chão entre o cavalo e a carreta
    k = ep(t, K("05.b"), 0.4) * (1 - ep(t, K("06.b"), 0.4))
    if k > 0:
        hx, hy = p["hx"] + p["dx"], p["hy"]
        a_tr, a_ca = p["th2"], p["th1"]      # eixo da carreta prolongado à frente do engate × rumo do cavalo
        R = 5.0
        linha3d(c, cam, [(hx, hy, 0.04), (hx + 9 * math.cos(a_tr), hy + 9 * math.sin(a_tr), 0.04)], BRANCO, 4, 0.8 * k,
                dash=[14, 10])
        arco = [(hx + R * math.cos(a), hy + R * math.sin(a), 0.05) for a in np.linspace(a_tr, a_ca, 30)]
        phi = abs(math.degrees(p["phi"]))
        cor = VERDE if phi < 35 else AMARELO if phi < 46 else VERMELHO
        linha3d(c, cam, arco, cor, 10, k)
        am = (a_tr + a_ca) / 2
        q = ponto_tela(cam, (hx + (R + 2.6) * math.cos(am), hy + (R + 2.6) * math.sin(am), 0.1))
        if q is not None:
            etiqueta(c, f"{phi:.0f}°", q[0], q[1], 46, cor, PRETO, k)
    # recapitulação: caminho inteiro com os marcos de cada passo
    if t >= K("10"):
        kk = ep(t, K("10.a"), 0.5) * (1 - ep(t, K("11"), 0.5))
        if kk > 0:
            seta_chao(c, cam, caminho_traseira(0, L), a=0.55 * kk, larg=0.6)


# ---------------------------------------------------------------- componentes de interface
def etiqueta(c, s, cx, cy, size, bg=AMARELO, fg=PRETO, a=1.0, nome="display"):
    if a <= 0:
        return
    w = tw(s, size, nome) + size * 0.9
    h = size * 1.45
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h * 0.22, h * 0.22)
    sh = paint("#000000", 0.35 * a)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, paint(bg, a))
    txt(c, s, cx, cy, size, nome, fg, a, "center")


def faixas(c, x, y, w, h, a, k=1.0, passo=26, cor1=AMARELO, cor2=PRETO):
    """faixas diagonais de sinalização (amarelo e preto)"""
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(cor1, a))
    pth = skia.Path()
    for i in range(-int(h / (2 * passo)) - 3, int(w / passo) + 6):
        x0 = x + i * passo * 2
        pth.moveTo(x0, y + h)
        pth.lineTo(x0 + passo, y + h)
        pth.lineTo(x0 + passo + h, y)
        pth.lineTo(x0 + h, y)
        pth.close()
    c.drawPath(pth, paint(cor2, a))
    c.restore()


def cartao(c, linhas, t0, t1, t, y=930, x=960, size=54):
    """cartão de instrução: placa amarela com texto preto e borda de faixas; linhas = [(texto, cor_destaque|None)]"""
    k = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.25))
    if k <= 0:
        return
    s = linhas
    w = tw(s, size, "display") + 80
    h = size * 1.75
    sl = (1 - ease_out(prog(t, t0, 0.45))) * 60
    c.save()
    c.translate(0, sl)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, y - h / 2, w, h), 14, 14)
    sh = paint("#000000", 0.4 * k)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.save(); c.translate(0, 10); c.drawRRect(r, sh); c.restore()
    c.save()
    c.clipRRect(r, True)
    faixas(c, x - w / 2, y - h / 2, w, h, k, passo=18)
    inner = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2 + 12, y - h / 2 + 12, w - 24, h - 24), 8, 8)
    c.drawRRect(inner, paint(AMARELO, k))
    c.restore()
    txt(c, s, x, y, size, "display", PRETO, k, "center")
    c.restore()


def chip_passo(c, n, titulo, t0, t1, t):
    k = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.3))
    if k <= 0:
        return
    x, y = 70 - (1 - ease_out(prog(t, t0, 0.5))) * 80, 84
    rot = f"STEP {n}" if n else "THE RULE"
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


def volante(c, cx, cy, r, d, a, mao=True, seta=0.0):
    """volante visto de frente; d = esterço das rodas (rad, negativo = direita); mão na parte de baixo"""
    if a <= 0:
        return
    rot = -math.degrees(d) * 12.0
    bg = paint("#0E1116", 0.62 * a)
    c.drawCircle(cx, cy, r + 34, bg)
    c.save()
    c.translate(cx, cy)
    c.rotate(rot)
    aro = paint("#2B3038", a, stroke=r * 0.2)
    c.drawCircle(0, 0, r, aro)
    c.drawCircle(0, 0, r, paint("#454C57", a, stroke=r * 0.06))
    for ang in (90, 210, 330):
        p = paint("#2B3038", a, stroke=r * 0.13)
        p.setStrokeCap(skia.Paint.kRound_Cap)
        c.drawLine(0, 0, r * math.cos(math.radians(ang)) * 0.92, r * math.sin(math.radians(ang)) * 0.92, p)
    c.drawCircle(0, 0, r * 0.3, paint("#20242B", a))
    CN.cone_icone(c, 0, 4, r * 0.0042, a=a)
    c.drawRect(skia.Rect.MakeXYWH(-6, -r - r * 0.1, 12, r * 0.2), paint(AMARELO, a))     # marca do topo
    c.restore()
    if mao:
        # a mão fica embaixo (6 h); o deslocamento lateral acompanha o giro (limitado)
        u = max(-1, min(1, rot / 120))
        ang = math.radians(90 + 32 * u)
        hx, hy = cx + r * math.cos(ang), cy + r * math.sin(ang)
        c.drawCircle(hx, hy, r * 0.2, paint(AMARELO, a))
        c.drawCircle(hx, hy, r * 0.2, paint(PRETO, a, stroke=4))
        txt(c, "HAND", hx, hy + r * 0.38, 22, "display", AMARELO, a, "center")
    if abs(seta) > 0.01:
        # seta curva mostrando para onde a mão vai
        sgn = 1 if seta > 0 else -1       # seta > 0: a mão vai para a esquerda (sentido horário na tela)
        pth = skia.Path()
        rr = r + 58
        a0 = 90 - 10 * sgn
        pth.addArc(skia.Rect.MakeXYWH(cx - rr, cy - rr, 2 * rr, 2 * rr), a0, 50 * sgn)
        p = paint(LARANJA, a * abs(seta), stroke=14)
        p.setStrokeCap(skia.Paint.kRound_Cap)
        c.drawPath(pth, p)
        ae = math.radians(a0 + 50 * sgn)
        ex, ey = cx + rr * math.cos(ae), cy + rr * math.sin(ae)
        tx, ty = -math.sin(ae) * sgn, math.cos(ae) * sgn
        tri = skia.Path()
        tri.moveTo(ex + tx * 26, ey + ty * 26)
        tri.lineTo(ex - ty * 20, ey + tx * 20)
        tri.lineTo(ex + ty * 20, ey - tx * 20)
        tri.close()
        c.drawPath(tri, paint(LARANJA, a * abs(seta)))


def medidor(c, cx, cy, r, phi_deg, a):
    """ângulo entre cavalo e carreta: 0–90°, verde até 35, amarelo até 45, vermelho depois"""
    if a <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r - 40, cy - r - 46, 2 * r + 80, r + 136), 22, 22),
                paint("#0E1116", 0.62 * a))
    ini = 180
    for a0, a1, cor in ((0, 35, VERDE), (35, 45, AMARELO), (45, 90, VERMELHO)):
        pth = skia.Path()
        pth.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini + a0 * 2, (a1 - a0) * 2)
        c.drawPath(pth, paint(cor, a, stroke=18))
    v = max(0, min(90, phi_deg))
    ang = math.radians(ini + v * 2)
    p = paint(BRANCO, a, stroke=7)
    p.setStrokeCap(skia.Paint.kRound_Cap)
    c.drawLine(cx, cy, cx + (r - 6) * math.cos(ang), cy + (r - 6) * math.sin(ang), p)
    c.drawCircle(cx, cy, 11, paint(BRANCO, a))
    cor = VERDE if v < 35 else AMARELO if v < 45.5 else VERMELHO
    txt(c, f"{v:.0f}°", cx, cy + 46, 44, "display", cor, a, "center")
    txt(c, "TRAILER ANGLE", cx, cy - r - 22, 20, "display", "#C9D1DC", a, "center", track=2)


def mascote(c, t, a=1.0):
    b = math.sin(t * 2.2) * 3
    CN.cone_icone(c, 1840, 1000 + b, 0.72, olhos=True, t=t, a=a)


def ancorado(c, s, P3, cor=AMARELO, fg=PRETO, a=1.0, size=34, dy=-90):
    cam = _ULT.get("cam")
    if cam is None or a <= 0:
        return
    q = ponto_tela(cam, P3)
    if q is None:
        return
    x, y = q
    p = paint(BRANCO, 0.9 * a, stroke=3)
    c.drawLine(x, y, x, y + dy + 26, p)
    c.drawCircle(x, y, 7, paint(BRANCO, a))
    etiqueta(c, s, x, y + dy, size, cor, fg, a)


def cortina(c, t, tc, d=0.7):
    """cortina de faixas amarelas e pretas que cobre a tela no instante tc (corte escondido)"""
    u = (t - (tc - d / 2)) / d
    if u <= 0 or u >= 1:
        return
    x = -2400 + 4800 * ease_io(u)
    c.save()
    c.translate(x, 0)
    c.skew(-0.35, 0)
    faixas(c, -1300, -40, 2600, 1160, 1.0, passo=60)
    c.drawRect(skia.Rect.MakeXYWH(-1300, -40, 60, 1160), paint(PRETO))
    c.drawRect(skia.Rect.MakeXYWH(1240, -40, 60, 1160), paint(PRETO))
    c.restore()


def hud_direcao(c, t, t0, t1, seta=0.0):
    k = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.4))
    if k <= 0:
        return
    p = _ULT["p"]
    volante(c, 190, 860, 110, p["dshow"], k, seta=seta)
    medidor(c, 1600, 900, 110, abs(math.degrees(p["phi"])), k)


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, Cc, B):
    ta, tb, tc, td = (K(f"01.{k}") for k in "abcd")
    p = _ULT["p"]
    # 53 ft ao longo da carreta
    k = ep(t, ta + 0.4, 0.5) * (1 - ep(t, tb - 0.2, 0.3))
    if k > 0:
        cam = _ULT["cam"]
        x2 = p["x2"] + p["dx"]
        xa, xb = x2 - MB.TRAS, x2 + MB.L2 + MB.KP_FRENTE
        y = p["y2"] - MB.LARG / 2 - 0.05
        kk = ep(t, ta + 0.4, 1.0)
        xm = (xa + xb) / 2
        linha3d(c, cam, [(xm - (xm - xa) * kk, y, 4.6), (xm + (xb - xm) * kk, y, 4.6)], AMARELO, 7, k)
        for xx in (xa, xb):
            linha3d(c, cam, [(xx, y, 4.25), (xx, y, 4.95)], AMARELO, 7, k * ep(t, ta + 1.2, 0.3))
        q = ponto_tela(cam, (xm, y, 4.6))
        if q is not None:
            etiqueta(c, "53 FT", q[0], q[1] - 46, 54, AMARELO, PRETO, k * ep(t, ta + 0.8, 0.3))
    ancorado(c, "DOOR 4", (0, -0.6, 4.7), a=ep(t, tb + 0.6, 0.4) * (1 - ep(t, tc, 0.3)), size=40, dy=-80)
    cartao(c, "BACKWARDS", tc + 1.6, td - 0.1, t, y=150, size=64)
    # título
    kt = ep(t, td + 0.4, 0.5)
    if kt > 0:
        y = 470
        sl = (1 - ease_out(prog(t, td + 0.4, 0.6))) * 80
        g = skia.Paint()
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(960, y + 60), 900, [hexc("#0B0F17", 0.62 * kt), hexc("#0B0F17", 0.0)]))
        c.drawRect(skia.Rect.MakeWH(1920, 1080), g)
        c.save(); c.translate(0, sl)
        etiqueta(c, "PARK ANYTHING", 960, y - 150, 40, PRETO, AMARELO, kt)
        for j, linha in enumerate(("HOW TO BACK A TRACTOR-TRAILER", "INTO A LOADING DOCK")):
            kj = ep(t, td + 0.55 + 0.15 * j, 0.4)
            sh = paint("#000000", 0.45 * kj)
            sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
            f = fnt("display", 92)
            w = f.measureText(linha)
            c.drawString(linha, 960 - w / 2, y + j * 112 + 33 + 6, f, sh)
            txt(c, linha, 960, y + j * 112, 92, "display", BRANCO, kj, "center")
        cartao(c, "STEP-BY-STEP", td + 1.0, 99999, t, y=y + 250, size=50)
        c.restore()


def b_regra(c, t, Cc, B):
    ta, tb, tc, td = (K(f"02.{k}") for k in "abcd")
    chip_passo(c, 0, "HAND AT THE BOTTOM", ta + 0.3, B["end"], t)
    k = ep(t, tb, 0.5)
    p = _ULT["p"]
    if k > 0:
        u = ep(t, tc + 0.4, 0.8)
        volante(c, 1480, 600, 210, p["dshow"], k, seta=u * (1 - ep(t, B["end"] - 0.5, 0.3)))
    cartao(c, "HAND LEFT = TRAILER LEFT", td, B["end"] + 1, t, y=960, size=56)
    tx, ty = CN.traseira_carreta(p, p["dx"])
    ancorado(c, "TRAILER", (tx, ty, 4.2), a=ep(t, td + 0.2, 0.4), size=32, dy=-70)


def b_preparo(c, t, Cc, B):
    ta, tb, tc, td = (K(f"03.{k}") for k in "abcd")
    chip_passo(c, 1, "THE SETUP", ta + 0.3, B["end"], t)
    cartao(c, "DOCK ON YOUR LEFT", tb + 0.4, tc - 0.3, t)
    ancorado(c, "DRIVER'S SIDE", (-6, -0.5, 6.5), a=ep(t, tb + 1.2, 0.4) * (1 - ep(t, tc - 0.3, 0.3)), size=34)
    cartao(c, "SEE IT THROUGH YOUR WINDOW", tc + 0.6, td - 0.2, t)
    cartao(c, "ROOM TO SWING", td + 1.6, B["end"] + 0.2, t)


def b_virar(c, t, Cc, B):
    ta, tb, tc, td = (K(f"04.{k}") for k in "abcd")
    chip_passo(c, 2, "TURN TOWARD THE DOCK", ta + 0.3, B["end"], t)
    hud_direcao(c, t, ta + 0.6, 1e9, seta=ep(t, tb + 0.2, 0.4) * (1 - ep(t, tc + 2.5, 0.4)))
    cartao(c, "SLOW · LOWEST REVERSE GEAR", tc + 0.4, td - 0.2, t, y=110 + 900, size=46)


def b_angulo(c, t, Cc, B):
    ta, tb, tc, td = (K(f"05.{k}") for k in "abcd")
    chip_passo(c, 3, "WATCH THE ANGLE", ta + 0.3, B["end"], t)
    hud_direcao(c, t, B["start"] - 1, 1e9, seta=-ep(t, tc, 0.4) * (1 - ep(t, td, 0.4)))
    cartao(c, "COUNTER-STEER NEAR 45°", tc + 0.2, td - 0.1, t, size=52)
    k = ep(t, td + 0.4, 0.3) * (1 - ep(t, B["end"] - 0.2, 0.3))
    if k > 0:
        etiqueta(c, "JACKKNIFE!", 960, 190, 70, VERMELHO, BRANCO, k)


def b_seguir(c, t, Cc, B):
    ta, tb, tc, td = (K(f"06.{k}") for k in "abcd")
    chip_passo(c, 4, "FOLLOW THE TRAILER", ta + 0.3, B["end"], t)
    hud_direcao(c, t, B["start"] - 1, 1e9)
    cartao(c, "SMALL MOVES", tc + 0.2, td - 0.1, t)
    cartao(c, "FIX DRIFT EARLY", td + 1.0, B["end"] + 0.2, t)


def b_endireitar(c, t, Cc, B):
    ta, tb, tc = (K(f"07.{k}") for k in "abc")
    chip_passo(c, 5, "STRAIGHTEN OUT", ta + 0.3, B["end"], t)
    hud_direcao(c, t, B["start"] - 1, 1e9)
    cartao(c, "CENTER THE WHEEL", tb + 1.6, B["end"] + 0.2, t)


def b_pullup(c, t, Cc, B):
    ta, tb, tc, td = (K(f"08.{k}") for k in "abcd")
    hud_direcao(c, t, B["start"] - 1, B["end"])
    k = ep(t, tb, 0.25) * (1 - ep(t, tb + 0.9, 0.25))
    if k > 0:
        etiqueta(c, "STOP", 960, 210, 90, VERMELHO, BRANCO, k)
    cartao(c, "PULL-UP", tc + 0.1, td - 0.1, t, size=64)
    cartao(c, "PULL-UPS CAN COST POINTS", td + 0.6, B["end"] + 0.1, t, size=50)


def b_goal(c, t, Cc, B):
    ta, tb, tc, td = (K(f"09.{k}") for k in "abcd")
    chip_passo(c, 6, "GET OUT AND LOOK", ta + 0.3, B["end"], t)
    k = ep(t, tb + 0.6, 0.4) * (1 - ep(t, tc - 0.2, 0.3))
    if k > 0:
        letras = (("G", "GET"), ("O", "OUT"), ("A", "AND"), ("L", "LOOK"))
        for j, (le, pal) in enumerate(letras):
            kj = k * ep(t, tb + 0.6 + 0.22 * j, 0.3)
            x = 960 + (j - 1.5) * 250
            etiqueta(c, le, x, 470, 120, AMARELO, PRETO, kj)
            txt(c, pal, x, 600, 44, "display", BRANCO, kj, "center")
    # distância até a doca
    p = _ULT["p"]
    tx, ty = CN.traseira_carreta(p, p["dx"])
    gap = max(0.0, -ty - 0.0)
    kd = ep(t, tc + 0.6, 0.4) * (1 - ep(t, B["end"] - 0.1, 0.3))
    if kd > 0:
        ft = gap * 3.281
        cor = VERDE if gap < 0.6 else AMARELO
        etiqueta(c, f"{ft:.0f} FT" if ft >= 1.5 else f"{gap * 39.37:.0f} IN", 960, 170, 64, cor, PRETO, kd)
    ks = ep(t, td + 2.9, 0.25)
    if ks > 0 and t < B["end"] + 0.5:
        etiqueta(c, "STOP", 960, 300, 86, VERMELHO, BRANCO, ks * (1 - ep(t, B["end"], 0.3)))


def b_resumo(c, t, Cc, B):
    ks = [K(f"10.{k}") for k in "bcdefg"]
    itens = ("DOCK ON THE DRIVER'S SIDE", "TURN TOWARD THE DOCK", "COUNTER-STEER NEAR 45°", "FOLLOW THE TRAILER",
             "STRAIGHTEN OUT", "GET OUT AND LOOK")
    k0 = ep(t, K("10.a"), 0.4) * (1 - ep(t, B["end"] - 0.3, 0.3))
    if k0 <= 0:
        return
    x, y0 = 70, 210
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 24, y0 - 70, 700, 6 * 104 + 100), 22, 22), paint("#0E1116", 0.68 * k0))
    txt(c, "RECAP", x, y0 - 22, 34, "display", AMARELO, k0, track=3)
    for j, (s, t0) in enumerate(zip(itens, ks)):
        kj = k0 * ep(t, t0, 0.3)
        y = y0 + 50 + j * 104
        ativo = t0 <= t < (ks[j + 1] if j + 1 < len(ks) else 1e9)
        c.drawCircle(x + 26, y, 26, paint(AMARELO if ativo else "#3A414C", kj))
        txt(c, str(j + 1), x + 26, y, 30, "display", PRETO if ativo else BRANCO, kj, "center")
        txt(c, s, x + 70, y, 32, "black", BRANCO if ativo else "#C9D1DC", kj)


def b_final(c, t, Cc, B):
    ta, tb, tc = (K(f"11.{k}") for k in "abc")
    k = ep(t, ta, 0.5)
    if k <= 0:
        return
    c.drawRect(skia.Rect.MakeWH(1920, 1080), paint("#0B0F17", 0.62 * k))
    # próximo vídeo
    x, y, w, h = 160, 250, 900, 520
    sl = (1 - ease_out(prog(t, ta, 0.6))) * 90
    c.save(); c.translate(-sl, 0)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
    c.drawRRect(r, paint("#F7F9FB", k))
    c.save(); c.clipRRect(r, True)
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y), skia.Point(0, y + h)], [hexc(CN.CEU_ALTO), hexc(CN.CEU_BAIXO)]))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h * 0.62), p)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.62, w, h * 0.38), paint(CN.ASFALTO, k))
    _limo(c, x + w / 2, y + h * 0.62, k)
    c.restore()
    etiqueta(c, "NEXT", x + 110, y + 60, 40, PRETO, AMARELO, k)
    txt(c, "PARALLEL PARKING", x + 40, y + h + 60, 62, "display", BRANCO, k)
    txt(c, "A LIMOUSINE", x + 40, y + h + 130, 62, "display", AMARELO, k)
    c.restore()
    # comentário + inscrição
    kb = ep(t, tb, 0.5)
    if kb > 0:
        etiqueta(c, "TRUCK DRIVER?", 1440, 330, 50, AMARELO, PRETO, kb)
        txt(c, "Tell us what we missed", 1440, 420, 40, "bold", BRANCO, kb, "center")
        txt(c, "in the comments", 1440, 470, 40, "bold", BRANCO, kb, "center")
    kc = ep(t, tc, 0.5)
    if kc > 0:
        pulse = 1 + 0.035 * math.sin(t * 5)
        c.save(); c.translate(1440, 640); c.scale(pulse, pulse)
        etiqueta(c, "SUBSCRIBE", 0, 0, 56, VERMELHO, BRANCO, kc, nome="display")
        c.restore()
        CN.cone_icone(c, 1440, 840, 1.25, olhos=True, t=t, a=kc)


def _limo(c, cx, cy, a):
    """limusine estilizada vista de lado (cartão do próximo vídeo)"""
    w, h = 640, 96
    body = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h - 30, w, h), 30, 30)
    c.drawRRect(body, paint("#15181D", a))
    top = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 120, cy - h - 80, w - 250, 70), 26, 26)
    c.drawRRect(top, paint("#15181D", a))
    for i in range(6):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 140 + i * 62, cy - h - 68, 50, 46), 8, 8), paint("#6C8BA8", a))
    for wx in (cx - w / 2 + 100, cx + w / 2 - 100):
        c.drawCircle(wx, cy - 30, 40, paint("#0A0B0D", a))
        c.drawCircle(wx, cy - 30, 18, paint("#9AA3AD", a))
    p = skia.Path()
    p.moveTo(cx + w / 2 + 30, cy + 40)
    p.quadTo(cx, cy + 120, cx - w / 2 - 10, cy + 30)
    pp = paint(LARANJA, a, stroke=16)
    pp.setStrokeCap(skia.Paint.kRound_Cap)
    c.drawPath(p, pp)


def OVERLAY(c, t):
    mascote(c, t, 1.0 * (1 - ep(t, K("11.c"), 0.3)))
    for tc in (K("02"), K("03"), K("10")):
        cortina(c, t, tc)


BLOCKS = dict(gancho=b_gancho, regra=b_regra, preparo=b_preparo, virar=b_virar, angulo=b_angulo, seguir=b_seguir,
              endireitar=b_endireitar, pullup=b_pullup, goal=b_goal, resumo=b_resumo, final=b_final)


def CAPTION(c, scene, t):
    pass
