"""Cenário do Park Anything 002: rua de centro comercial com meio-fio, calçada, fachadas de lojas low-poly, árvores e
postes; dois sedãs estacionados (B na frente da vaga, C atrás) e a limusine preta esticada (28 pés), com janelas
escuras em fila, friso cromado, faróis e lanternas. Mundo em metros: X leste, Y norte, meio-fio em y = 0, a rua
para o norte (y > 0), a calçada e as lojas para o sul (y < 0). Motor 3D: 001/roteiro/mundo3d.py."""
import math
from functools import lru_cache
import numpy as np
import skia
import baliza as BZ
from mundo3d import rotz, tom
from motor import paint, hexc

ASFALTO = "#4A5058"
CALCADA = "#B9BCB8"
MEIOFIO = "#D3D5D0"
GRAMA = "#88C46F"
AMARELO, LARANJA = "#F2B705", "#FF7A1A"
LIMO = "#17191D"
CROMO = "#D7DCE2"
PNEU = "#1E2125"
CORES_LOJA = ("#C46A4A", "#E2C48A", "#6C8FB3", "#9A7BB0", "#D9A05B", "#7FAF8F", "#B85C66", "#A9B4BF")


# ---------------------------------------------------------------- rua
def montar_rua(cena, t=0.0, vaga_k=0.0):
    cena.chao([(-400, -400), (400, -400), (400, 400), (-400, 400)], GRAMA)
    cena.chao([(-140, 0), (140, 0), (140, 14), (-140, 14)], ASFALTO)
    cena.chao([(-140, -4.2), (140, -4.2), (140, 0), (-140, 0)], CALCADA)
    cena.chao([(-140, 14), (140, 14), (140, 18), (-140, 18)], CALCADA)
    for gx in np.arange(-140, 140, 2.0):          # juntas da calçada
        cena.chao([(gx - 0.02, -4.2), (gx + 0.02, -4.2), (gx + 0.02, -0.25), (gx - 0.02, -0.25)], tom(CALCADA, 0.88), 0.8, z=0.003)
    # faixa central (amarela dupla) e linha da faixa de estacionamento
    for yy in (6.95, 7.15):
        cena.chao([(-140, yy - 0.06), (140, yy - 0.06), (140, yy + 0.06), (-140, yy + 0.06)], AMARELO, 0.95, z=0.005)
    for gx in np.arange(-140, 140, 6.0):
        cena.chao([(gx, 2.42), (gx + 3.0, 2.42), (gx + 3.0, 2.54), (gx, 2.54)], "#F2F2EE", 0.8, z=0.005)
    # vaga em destaque
    if vaga_k > 0:
        xB, S = BZ.XB, BZ.VAGA
        pulse = 0.55 + 0.45 * math.sin(t * 4)
        cena.chao([(xB - S, 0.1), (xB, 0.1), (xB, 2.35), (xB - S, 2.35)], AMARELO, 0.22 * vaga_k * pulse, z=0.006)
    # meio-fio (degrau de 15 cm)
    cena.caixa((0, -0.15, 0.075), (280, 0.3, 0.15), 0, MEIOFIO, ao=0.15, sombra=False, camada=0)
    cena.caixa((0, 14.15, 0.075), (280, 0.3, 0.15), 0, MEIOFIO, ao=0.15, sombra=False, camada=0)
    # lojas ao sul e ao norte
    for i, (x0, w, h, cor) in enumerate(_lojas()):
        _loja(cena, x0, w, h, cor, sul=True)
    for i, (x0, w, h, cor) in enumerate(_lojas(9)):
        _loja(cena, x0, w, h, cor, sul=False)
    for x in np.arange(-60, 61, 12.0):
        _arvore(cena, x + 5, -2.6)
        _poste(cena, x, -0.9)


@lru_cache(None)
def _lojas(seed=4):
    rng = np.random.default_rng(seed)
    out, x = [], -90.0
    while x < 90:
        w = float(rng.choice([8.0, 10.0, 12.0, 14.0]))
        h = float(rng.uniform(7.5, 14))
        out.append((x, w, h, CORES_LOJA[int(rng.integers(len(CORES_LOJA)))]))
        x += w
    return tuple(out)


def _loja(cena, x0, w, h, cor, sul=True):
    prof = 14.0
    yf = -4.2 if sul else 18.0                    # linha da fachada
    yc = yf - prof / 2 if sul else yf + prof / 2
    face = "dir" if not sul else "esq"            # a fachada que olha para a rua
    cena.caixa((x0 + w / 2, yc, h / 2), (w, prof, h), 0, cor, ao=0.12, camada=0,
               cores={"topo": tom(cor, 0.85)}, deco={face: _fachada(w, h, cor)})


def _fachada(w, h, cor):
    def deco(c, P, face):
        def poly(pts, col, a=1.0):
            p = skia.Path()
            p.moveTo(*pts[0])
            for q in pts[1:]:
                p.lineTo(*q)
            p.close()
            c.drawPath(p, paint(col, a))

        def q(u0, u1, v0, v1):
            return [P(u0, v1), P(u1, v1), P(u1, v0), P(u0, v0)]
        # vitrine e toldo no térreo, janelas acima, cornija
        poly(q(0.06, 0.94, 0.02, 3.0 / h), "#2C3A48")
        poly(q(0.08, 0.92, 0.05, 2.8 / h), "#7FA3BF", 0.85)
        poly(q(0.03, 0.97, 3.0 / h, 3.6 / h), tom(cor, 0.7))
        n = max(2, int(w / 3.2))
        andares = int((h - 4.2) / 3.0)
        for a in range(andares):
            v0 = (4.3 + a * 3.0) / h
            for k in range(n):
                u0 = 0.08 + k * (0.84 / n)
                poly(q(u0 + 0.02, u0 + 0.84 / n - 0.06, v0, v0 + 1.6 / h), "#3E5468")
        poly(q(0, 1, 1 - 0.5 / h, 1), tom(cor, 0.78))
    return deco


def _arvore(cena, x, y):
    cena.caixa((x, y, 1.3), (0.35, 0.35, 2.6), 0.2, "#7A5A3C", ao=0.1)
    cena.caixa((x, y, 3.6), (2.6, 2.6, 2.4), 0.5 + x * 0.07, "#3E9A4A", ao=0.15)
    cena.caixa((x, y, 5.0), (1.7, 1.7, 1.2), 0.2 + x * 0.07, "#4DAF57", ao=0.1)


def _poste(cena, x, y):
    cena.caixa((x, y, 2.6), (0.16, 0.16, 5.2), 0, "#3A3F47", ao=0.0)
    cena.caixa((x, y + 0.6, 5.15), (0.3, 1.3, 0.14), 0, "#3A3F47", ao=0.0)
    cena.caixa((x, y + 1.15, 5.05), (0.4, 0.3, 0.1), 0, "#FFF3C4", ao=0.0, sombra=False)


# ---------------------------------------------------------------- veículos
def _roda(cena, R, O, x, y, raio=0.36, larg=0.26, yaw=0.0):
    cena.cilindro((x, y, raio), raio, larg, yaw, PNEU, R=R, O=O, n=12, cor_tampa="#2A2E33", vies=1.5)
    sgn = 1 if y > 0 else -1
    cena.cilindro((x, y + sgn * (larg / 2 + 0.01), raio), raio * 0.55, 0.02, yaw, "#C3C9D1", R=R, O=O, n=10, vies=1.5)


def sedan(cena, x0, y0, cor, frente_leste=True):
    """sedã de 4,9 × 1,85 m com o canto traseiro-direito em (x0, y0) (estacionado, virado para leste)"""
    L, Wd = BZ.CARRO
    cx, cy = x0 + L / 2, y0 + Wd / 2
    R, O = rotz(0.0 if frente_leste else math.pi), np.array([cx, cy, 0.0])
    cxb = lambda *a, **k: cena.caixa(*a, R=R, O=O, **k)
    cxb((0, 0, 0.62), (L, Wd, 0.62), 0, cor, ao=0.2, cores={"topo": tom(cor, 1.05)})
    cxb((-0.25, 0, 1.18), (2.5, Wd - 0.18, 0.55), 0, tom(cor, 0.9), ao=0.1, deco={"esq": _vidro_sedan, "dir": _vidro_sedan,
                                                                                    "frente": _vidro_cheio, "tras": _vidro_cheio})
    cxb((L / 2 + 0.02, 0, 0.58), (0.06, Wd - 0.3, 0.2), 0, CROMO, ao=0.0, sombra=False)
    for sx in (-1, 1):
        cxb((L / 2 - 0.02, sx * 0.7, 0.75), (0.05, 0.3, 0.14), 0, "#FFF3C4", ao=0.0, sombra=False)
        cxb((-L / 2 + 0.02, sx * 0.7, 0.75), (0.05, 0.3, 0.14), 0, "#D3262E", ao=0.0, sombra=False)
    for x in (-1.45, 1.45):
        for sy in (-1, 1):
            _roda(cena, R, O, x, sy * 0.82)


def _vidro_sedan(c, P, face):
    for u0, u1 in ((0.1, 0.47), (0.53, 0.9)):
        pts = [P(u0, 0.15), P(u1, 0.15), P(u1, 0.85), P(u0, 0.85)]
        p = skia.Path()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, paint("#2C4A66", 0.92))


def _vidro_cheio(c, P, face):
    pts = [P(0.08, 0.12), P(0.92, 0.12), P(0.92, 0.88), P(0.08, 0.88)]
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    sh = skia.GradientShader.MakeLinear([skia.Point(*pts[3]), skia.Point(*pts[0])], [hexc("#9FD3F2"), hexc("#2C4A66")])
    pp = paint("#2C4A66")
    pp.setShader(sh)
    c.drawPath(p, pp)


def limusine(cena, x, y, th, d, cor=LIMO, alfa=1.0, sombra=True):
    """limusine esticada: origem no eixo traseiro, x para a frente"""
    R, O = rotz(th), np.array([x, y, 0.0])
    cx = lambda *a, **k: cena.caixa(*a, R=R, O=O, alfa=alfa, **{"sombra": sombra, **k})
    xa, xb = -BZ.BALANCO_TRAS, BZ.EE + BZ.BALANCO_FRENTE
    xm = (xa + xb) / 2
    cx((xm, 0, 0.66), (BZ.COMP, BZ.LARG, 0.66), 0, cor, ao=0.15, cores={"topo": "#2B2F36"})
    # cabine longa (do para-brisa até o vidro traseiro)
    cx((xm - 0.35, 0, 1.25), (BZ.COMP - 2.9, BZ.LARG - 0.14, 0.55), 0, "#23262C", ao=0.05,
       cores={"topo": "#33373F"}, deco={"esq": _janelas_limo(True), "dir": _janelas_limo(False),
                                            "frente": _vidro_cheio, "tras": _vidro_cheio})
    for sy in (-1, 1):                                                                                 # frisos
        cx((xm, sy * (BZ.LARG / 2 + 0.01), 0.9), (BZ.COMP - 0.3, 0.02, 0.05), 0, CROMO, ao=0.0, sombra=False)
    cx((xb + 0.02, 0, 0.62), (0.06, BZ.LARG - 0.25, 0.22), 0, CROMO, ao=0.0, sombra=False)         # grade
    for sy in (-1, 1):
        cx((xb + 0.01, sy * 0.75, 0.78), (0.05, 0.32, 0.14), 0, "#FFF3C4", ao=0.0, sombra=False)
        cx((xa - 0.01, sy * 0.75, 0.8), (0.05, 0.32, 0.16), 0, "#E0242C", ao=0.0, sombra=False)
        cx((BZ.EE - 0.9, sy * 1.06, 1.15), (0.1, 0.14, 0.14), 0, "#2B2F36", ao=0.0, sombra=False)  # retrovisor
    for xx in (0.0,):
        for sy in (-1, 1):
            _roda(cena, R, O, xx, sy * 0.85)
    for sy in (-1, 1):
        _roda(cena, R, O, BZ.EE, sy * 0.85, yaw=d)


def _janelas_limo(esq):
    """fila de janelas escuras; na face esq a frente fica em u = 0, na dir em u = 1"""
    def deco(c, P, face):
        n = 6
        for k in range(n):
            u0 = 0.06 + k * 0.88 / n
            u1 = u0 + 0.88 / n - 0.025
            if not esq:
                u0, u1 = 1 - u1, 1 - u0
            pts = [P(u0, 0.14), P(u1, 0.14), P(u1, 0.86), P(u0, 0.86)]
            p = skia.Path()
            p.moveTo(*pts[0])
            for q in pts[1:]:
                p.lineTo(*q)
            p.close()
            c.drawPath(p, paint("#0B0D10", 0.95))
            c.drawLine(*P(u0, 0.8), *P(u0 + (u1 - u0) * 0.4, 0.8), paint("#6C7A8A", 0.5, stroke=2))
    return deco


def estacionados(cena):
    rB, rC = BZ.carros()
    sedan(cena, rB[0], rB[1], "#C0392B")
    sedan(cena, rC[0], rC[1], "#2E8B8B")
