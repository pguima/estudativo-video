"""Cenário e veículos do Park Anything 001: centro de distribuição com 7 docas, pátio de concreto com faixas amarelas,
gramado com árvores low-poly, e o conjunto cavalo (cabine azul-cobalto) + carreta baú de 53 pés (branca, com faixa
refletiva vermelha e branca, portas traseiras, lanternas, pés de apoio e o logo do canal na lateral).
Medidas reais: doca a 1,2 m (48 pol.) do chão, portas de 2,75 × 3,05 m (9 × 10 pés), docas a 4,2 m de centro a centro,
carreta 16,15 × 2,6 × 4,1 m."""
import math
from functools import lru_cache
import numpy as np
import skia
import manobra as MB
from mundo3d import Cena, Camera, rotz, decalque, linha3d, tom
from motor import paint, hexc

# paleta do canal: céu azul-claro, asfalto grafite, laranja de cone, amarelo de sinalização
CEU_ALTO, CEU_BAIXO = "#8FD0F5", "#D8F0FB"
ASFALTO = "#4A5058"
CONCRETO = "#9AA0A6"
GRAMA = "#88C46F"
FACHADA = "#E6E1D8"
FACHADA_BASE = "#BDB7AD"
PORTA = "#C9CED6"
SELO = "#22252A"
AMARELO = "#F2B705"
LARANJA = "#FF7A1A"
CABINE = "#2F5BD3"
CROMO = "#D7DCE2"
PNEU = "#1E2125"
CARRETA = "#F3F5F7"

DOCAS_X = [-12.6, -8.4, -4.2, 0.0, 4.2, 8.4, 12.6]
NUM_ALVO = 4
PORTA_L, PORTA_H, DOCA_H = 2.75, 3.05, 1.2
PREDIO = (-34.0, 34.0, 0.0, 26.0, 10.5)     # x0, x1, y0, y1, altura


def _fonte(size, peso="black"):
    from pathlib import Path
    base = Path(__file__).resolve().parents[4] / "_ferramentas" / "fontes"
    arq = {"black": base / "antigos" / "Rubik-Black.ttf", "bold": base / "inter" / "extras" / "ttf" / "Inter-Bold.ttf"}[peso]
    f = skia.Font(skia.Typeface.MakeFromFile(str(arq)), size)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


@lru_cache(None)
def img_logo():
    """logo da lateral da carreta: cone + PARK ANYTHING (fundo transparente)"""
    w, h = 1700, 260
    s = skia.Surface(w, h)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    cone_icone(c, 120, 140, 1.7)
    f = _fonte(150)
    c.drawString("PARK", 240, 190, f, paint("#1C2126"))
    wpark = f.measureText("PARK ")
    c.drawString("ANYTHING", 240 + wpark, 190, f, paint(LARANJA))
    return s.makeImageSnapshot()


@lru_cache(None)
def img_numero(n, alvo=False):
    w, h = 220, 220
    s = skia.Surface(w, h)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(10, 10, 200, 200), 26, 26), paint(AMARELO if alvo else "#2A2E35"))
    f = _fonte(150)
    tw = f.measureText(str(n))
    c.drawString(str(n), 110 - tw / 2, 165, f, paint("#16181C" if alvo else "#FFFFFF"))
    return s.makeImageSnapshot()


def cone_icone(c, x, y, k=1.0, olhos=False, t=0.0, a=1.0):
    """o cone do canal (2D): corpo laranja, faixas brancas, base escura; olhos opcionais (mascote)"""
    c.save()
    c.translate(x, y)
    c.scale(k, k)
    base = skia.Path()
    base.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-46, 40, 92, 16), 6, 6))
    c.drawPath(base, paint("#2B2F36", a))
    corpo = skia.Path()
    corpo.moveTo(-8, -62)
    corpo.lineTo(8, -62)
    corpo.lineTo(34, 42)
    corpo.lineTo(-34, 42)
    corpo.close()
    c.drawPath(corpo, paint(LARANJA, a))
    for y0, y1 in ((-30, -16), (2, 18)):
        f0, f1 = (y0 + 62) / 104, (y1 + 62) / 104
        b = skia.Path()
        b.moveTo(-8 - 26 * f0, y0)
        b.lineTo(8 + 26 * f0, y0)
        b.lineTo(8 + 26 * f1, y1)
        b.lineTo(-8 - 26 * f1, y1)
        b.close()
        c.drawPath(b, paint("#FFFFFF", a))
    if olhos:
        pisca = 1.0
        ph = (t % 4.2)
        if ph < 0.14:
            pisca = max(0.12, abs(ph - 0.07) / 0.07)
        for ex in (-9, 9):
            c.drawOval(skia.Rect.MakeXYWH(ex - 6.5, -12 - 8 * pisca, 13, 16 * pisca), paint("#FFFFFF", a))
            c.drawCircle(ex + 1.5, -11, 3.6 * pisca, paint("#16181C", a))
    c.restore()


# ---------------------------------------------------------------- mundo fixo
def montar_mundo(cena, t, alvo_k=0.0):
    x0, x1, y0, y1, hz = PREDIO
    # chão: gramado enorme, pátio de asfalto, pátio de concreto em frente às docas, calçada
    cena.chao([(-400, -400), (400, -400), (400, 400), (-400, 400)], GRAMA)
    cena.chao([(-60, -70), (60, -70), (60, y1 + 6), (-60, y1 + 6)], ASFALTO)
    cena.chao([(x0 + 2, -24), (x1 - 2, -24), (x1 - 2, 0.0), (x0 + 2, 0.0)], CONCRETO)
    # juntas do concreto
    for gx in np.arange(x0 + 2, x1 - 1, 6.0):
        cena.chao([(gx - 0.04, -24), (gx + 0.04, -24), (gx + 0.04, 0), (gx - 0.04, 0)], tom(CONCRETO, 0.86), 0.7, z=0.003)
    for gy in np.arange(-24, 0, 6.0):
        cena.chao([(x0 + 2, gy - 0.04), (x1 - 2, gy - 0.04), (x1 - 2, gy + 0.04), (x0 + 2, gy + 0.04)], tom(CONCRETO, 0.86), 0.7, z=0.003)
    # faixas amarelas entre as docas (guias de ré) e faixa de rolamento
    for i in range(len(DOCAS_X) + 1):
        gx = (DOCAS_X[0] - 2.1) + 4.2 * i
        cena.chao([(gx - 0.09, -17), (gx + 0.09, -17), (gx + 0.09, -0.4), (gx - 0.09, -0.4)], AMARELO, 0.95, z=0.006)
    for gx in np.arange(-56, 58, 6.0):
        cena.chao([(gx, -44.1), (gx + 3, -44.1), (gx + 3, -43.9), (gx, -43.9)], "#F2F2EE", 0.85, z=0.006)
    # meio-fio + canteiros
    for (a, b, cc, d) in ((-60, -72, 60, -70), ):
        cena.chao([(a, b), (cc, b), (cc, d), (a, d)], "#C9CBC7")
    # prédio
    fach = {"topo": "#C7C2B8", "frente": FACHADA, "tras": FACHADA, "esq": FACHADA, "dir": FACHADA}
    cena.caixa(((x0 + x1) / 2, (y0 + y1) / 2, hz / 2), (x1 - x0, y1 - y0, hz), 0, FACHADA, cores=fach, ao=0.08,
               deco={"dir": _deco_fachada(t, alvo_k)}, camada=0)
    cena.caixa(((x0 + x1) / 2, (y0 + y1) / 2, hz + 0.35), (x1 - x0 + 0.4, y1 - y0 + 0.4, 0.7), 0, "#AFA99F", ao=0.0, camada=0)
    # para-choques de borracha e selos das docas (volumes pequenos que saem da parede)
    for i, dx in enumerate(DOCAS_X):
        for sx in (-1, 1):
            cena.caixa((dx + sx * 0.95, -0.06, DOCA_H - 0.35), (0.28, 0.12, 0.42), 0, "#16181B", ao=0.0, sombra=False, camada=1)
            cena.caixa((dx + sx * (PORTA_L / 2 + 0.22), -0.2, DOCA_H + PORTA_H / 2), (0.32, 0.4, PORTA_H + 0.3), 0, SELO, ao=0.1,
                       sombra=False, camada=1)
        cena.caixa((dx, -0.2, DOCA_H + PORTA_H + 0.3), (PORTA_L + 0.76, 0.4, 0.42), 0, SELO, ao=0.0, sombra=False, camada=1)
    # árvores low-poly ao sul e nas laterais
    for (tx, ty, k) in _arvores():
        _arvore(cena, tx, ty, k)


@lru_cache(None)
def _arvores():
    rng = np.random.default_rng(7)
    pts = []
    for x in np.arange(-70, 72, 9.0):
        pts.append((x + rng.uniform(-2, 2), -80 + rng.uniform(-3, 3), rng.uniform(0.8, 1.25)))
    for y in np.arange(-60, 30, 10.0):
        for sx in (-1, 1):
            pts.append((sx * (68 + rng.uniform(-2, 2)), y + rng.uniform(-3, 3), rng.uniform(0.8, 1.2)))
    return tuple(pts)


def _arvore(cena, x, y, k):
    cena.caixa((x, y, 1.2 * k), (0.45 * k, 0.45 * k, 2.4 * k), 0.3, "#7A5A3C", ao=0.1)
    cena.caixa((x, y, 3.8 * k), (3.0 * k, 3.0 * k, 3.0 * k), 0.6 + x * 0.1, "#3E9A4A", ao=0.15)
    cena.caixa((x, y, 5.4 * k), (2.0 * k, 2.0 * k, 1.6 * k), 0.2 + x * 0.1, "#4DAF57", ao=0.1)


def _deco_fachada(t, alvo_k):
    """desenha na face sul do prédio: rodapé, portas de enrolar, números e luminárias"""
    x0, x1, y0, y1, hz = PREDIO

    def deco(c, Pf, face):
        def P(u, v):    # u em metros (x do mundo), v em metros a partir do chão
            return Pf((u - x0) / (x1 - x0), v / hz)

        def quad_m(ua, ub, va, vb):
            return [P(ua, vb), P(ub, vb), P(ub, va), P(ua, va)]

        def poly(pts, cor, a=1.0):
            p = skia.Path()
            p.moveTo(*pts[0])
            for z in pts[1:]:
                p.lineTo(*z)
            p.close()
            c.drawPath(p, paint(cor, a))
        for px in np.arange(x0 + 6.0, x1, 6.0):     # juntas dos painéis de concreto
            p0, p1 = P(px, DOCA_H), P(px, hz - 0.6)
            c.drawLine(*p0, *p1, paint("#CFC9BE", 1, stroke=max(1.0, np.linalg.norm(p1 - p0) / 260)))
        poly(quad_m(x0, x1, 0, DOCA_H), FACHADA_BASE)
        poly(quad_m(x0, x1, DOCA_H - 0.08, DOCA_H), "#A39D93")
        for i, dx in enumerate(DOCAS_X):
            alvo = i == NUM_ALVO - 1
            poly(quad_m(dx - PORTA_L / 2, dx + PORTA_L / 2, DOCA_H, DOCA_H + PORTA_H), PORTA)
            for k in range(1, 12):     # gomos da porta de enrolar
                v = DOCA_H + PORTA_H * k / 12
                p0, p1 = P(dx - PORTA_L / 2, v), P(dx + PORTA_L / 2, v)
                c.drawLine(*p0, *p1, paint("#9EA6B1", 0.9, stroke=max(1.0, np.linalg.norm(p1 - p0) / 220)))
            # placa com número
            img = img_numero(i + 1, alvo)
            decalque(c, img, quad_m(dx - 0.45, dx + 0.45, DOCA_H + PORTA_H + 0.75, DOCA_H + PORTA_H + 1.65))
            if alvo and alvo_k > 0:
                pulse = 0.5 + 0.5 * math.sin(t * 4)
                pts = quad_m(dx - PORTA_L / 2 - 0.1, dx + PORTA_L / 2 + 0.1, DOCA_H - 0.05, DOCA_H + PORTA_H + 0.05)
                p = skia.Path()
                p.moveTo(*pts[0])
                for z in pts[1:]:
                    p.lineTo(*z)
                p.close()
                st = paint(AMARELO, alvo_k * (0.55 + 0.45 * pulse), stroke=6)
                c.drawPath(p, st)
            # luminária
            poly(quad_m(dx - 0.25, dx + 0.25, DOCA_H + PORTA_H + 2.1, DOCA_H + PORTA_H + 2.3), "#3A3F47")
        # faixa de topo
        poly(quad_m(x0, x1, hz - 0.6, hz), "#D2CCC1")
    return deco


# ---------------------------------------------------------------- veículos
def _roda(cena, R, O, x, y, raio, larg, yaw=0.0, sombra=False):
    cena.cilindro((x, y, raio), raio, larg, yaw, PNEU, R=R, O=O, n=12, cor_tampa="#2A2E33", sombra=sombra)
    # cubo cromado
    sgn = 1 if y > 0 else -1
    cena.cilindro((x, y + sgn * (larg / 2 + 0.01), raio), raio * 0.45, 0.02, yaw, "#B8BEC6", R=R, O=O, n=10)


def cavalo(cena, hx, hy, th1, d, cor=CABINE, alfa=1.0, sombra=True):
    """cavalo mecânico: origem no eixo traseiro (= quinta roda), x para a frente"""
    R, O = rotz(th1), np.array([hx, hy, 0.0])
    cx = lambda *a, **k: cena.caixa(*a, R=R, O=O, alfa=alfa, **{"sombra": sombra, **k})
    cx((2.35, 0, 0.75), (7.1, 1.0, 0.35), 0, "#2B2F35", ao=0.0, sombra=False)                  # chassi
    cx((5.45, 0, 1.55), (2.1, 2.3, 1.1), 0, cor, ao=0.2,
       cores={"topo": tom(cor, 1.08)})                                                           # capô
    cx((3.55, 0, 2.15), (1.9, 2.5, 2.3), 0, cor, ao=0.25,
       deco={"frente": _parabrisa, "esq": _janela(True), "dir": _janela(False)})                             # cabine
    cx((3.55, 0, 3.4), (1.7, 2.3, 0.22), 0, tom(cor, 0.9), ao=0.0)                             # teto
    cx((6.58, 0, 0.75), (0.2, 2.45, 0.42), 0, CROMO, ao=0.0)                                   # para-choque
    cx((6.5, 0, 1.55), (0.06, 1.2, 0.7), 0, "#9CA3AD", ao=0.0, sombra=False)                   # grade
    for sy in (-1, 1):
        cx((6.49, sy * 0.85, 1.2), (0.05, 0.4, 0.18), 0, "#FFF3C4", ao=0.0, sombra=False)       # faróis
        cx((1.95, sy * 1.12, 0.85), (1.2, 0.36, 0.55), 0, CROMO, ao=0.1)                       # tanques
        cx((2.55, sy * 1.05, 2.6), (0.16, 0.16, 3.0), 0, CROMO, ao=0.0)                         # escapamentos
        cx((4.35, sy * 1.6, 2.6), (0.1, 0.16, 0.7), 0, "#1D2026", ao=0.0)                       # retrovisores
        cx((0.0, sy * 0.95, 1.12), (2.6, 0.65, 0.12), 0, "#1D2026", ao=0.0, sombra=False)       # para-lamas
    cx((0.15, 0, 1.12), (1.2, 1.4, 0.1), 0, "#15171A", ao=0.0, sombra=False)                    # quinta roda
    for x in (-0.65, 0.65):
        for sy in (-1, 1):
            _roda(cena, R, O, x, sy * 0.92, 0.52, 0.62)
    for sy in (-1, 1):
        _roda(cena, R, O, 5.2, sy * 1.0, 0.52, 0.34, yaw=d)


def _parabrisa(c, P, face):
    pts = [P(0.08, 0.55), P(0.92, 0.55), P(0.94, 0.93), P(0.06, 0.93)]
    p = skia.Path()
    p.moveTo(*pts[0])
    for z in pts[1:]:
        p.lineTo(*z)
    p.close()
    sh = skia.GradientShader.MakeLinear([skia.Point(*pts[3]), skia.Point(*pts[0])], [hexc("#9FD3F2"), hexc("#2C4A66")])
    pp = paint("#2C4A66")
    pp.setShader(sh)
    c.drawPath(p, pp)


def _janela(frente_no_inicio):
    """janela lateral da cabine, na metade da frente (na face esq a frente fica em u = 0; na dir, em u = 1)"""
    def deco(c, P, face):
        u0, u1 = (0.08, 0.55) if frente_no_inicio else (0.45, 0.92)
        pts = [P(u0, 0.55), P(u1, 0.55), P(u1, 0.9), P(u0, 0.9)]
        p = skia.Path()
        p.moveTo(*pts[0])
        for z in pts[1:]:
            p.lineTo(*z)
        p.close()
        c.drawPath(p, paint("#2C4A66", 0.92))
    return deco


def carreta(cena, hx, hy, th2, alfa=1.0, sombra=True):
    """carreta baú de 53 pés: origem no pino-rei, x para a frente"""
    R, O = rotz(th2), np.array([hx, hy, 0.0])
    cx = lambda *a, **k: cena.caixa(*a, R=R, O=O, alfa=alfa, **{"sombra": sombra, **k})
    comp = MB.KP_FRENTE + MB.L2 + MB.TRAS
    xc = MB.KP_FRENTE - comp / 2
    cx((xc, 0, 2.68), (comp, MB.LARG, 2.85), 0, CARRETA, ao=0.12,
       cores={"topo": "#E9ECEF"}, deco={"esq": _lateral_carreta, "dir": _lateral_carreta, "tras": _traseira})
    cx((xc, 0, 1.18), (comp - 0.4, MB.LARG - 0.25, 0.14), 0, "#3A3F46", ao=0.0, sombra=False)    # assoalho/longarina
    for sy in (-1, 1):
        cx((-1.9, sy * 0.85, 0.6), (0.18, 0.18, 1.1), 0, "#41464D", ao=0.0, sombra=False)       # pés de apoio
        cx((-1.9, sy * 0.85, 0.06), (0.4, 0.3, 0.1), 0, "#41464D", ao=0.0, sombra=False)
    cx((-(MB.L2 + MB.TRAS) + 0.2, 0, 0.62), (0.15, MB.LARG - 0.3, 0.14), 0, "#C0262D", ao=0.0, sombra=False)  # para-choque traseiro
    cx((-MB.L2, 0, 1.05), (2.6, MB.LARG - 0.1, 0.12), 0, "#1D2026", ao=0.0, sombra=False)
    for x in (-MB.L2 - 0.65, -MB.L2 + 0.65):
        for sy in (-1, 1):
            _roda(cena, R, O, x, sy * 0.95, 0.52, 0.62)


def _lateral_carreta(c, P, face):
    # nervuras verticais
    n = 22
    for k in range(1, n):
        p0, p1 = P(k / n, 0.02), P(k / n, 0.98)
        c.drawLine(*p0, *p1, paint("#C9CED5", 0.8, stroke=max(0.6, np.linalg.norm(p1 - p0) / 140)))
    # faixa refletiva vermelha e branca (fita DOT-C2) ao longo da base
    m = 26
    for k in range(m):
        u0, u1 = k / m, (k + 0.5) / m
        pts = [P(u0, 0.03), P(u1, 0.03), P(u1, 0.08), P(u0, 0.08)]
        p = skia.Path()
        p.moveTo(*pts[0])
        for z in pts[1:]:
            p.lineTo(*z)
        p.close()
        c.drawPath(p, paint("#D3262E" if k % 2 == 0 else "#FFFFFF"))
    # logo: na face, u vai da traseira para a frente (ou ao contrário); mantém a leitura da esquerda para a direita
    img = img_logo()
    a, b = 0.24, 0.76
    va, vb = 0.38, 0.66
    decalque(c, img, [P(a, vb), P(b, vb), P(b, va), P(a, va)])


def _traseira(c, P, face):
    def poly(pts, cor, a=1.0, st=None):
        p = skia.Path()
        p.moveTo(*pts[0])
        for z in pts[1:]:
            p.lineTo(*z)
        p.close()
        c.drawPath(p, paint(cor, a, stroke=st))
    poly([P(0.03, 0.04), P(0.97, 0.04), P(0.97, 0.97), P(0.03, 0.97)], "#E2E6EA")
    esc = np.linalg.norm(P(1, 0) - P(0, 0)) / 300
    c.drawLine(*P(0.5, 0.04), *P(0.5, 0.97), paint("#8E96A0", 1, stroke=max(1, 3 * esc)))
    for u in (0.2, 0.36, 0.64, 0.8):
        c.drawLine(*P(u, 0.06), *P(u, 0.95), paint("#AEB5BE", 1, stroke=max(1, 4 * esc)))
    for u0 in (0.03, 0.86):
        poly([P(u0, 0.06), P(u0 + 0.11, 0.06), P(u0 + 0.11, 0.13), P(u0, 0.13)], "#E0242C")
    for k in range(10):
        u0 = 0.03 + k * 0.094
        poly([P(u0, 0.0), P(u0 + 0.047, 0.0), P(u0 + 0.047, 0.03), P(u0, 0.03)], "#D3262E" if k % 2 == 0 else "#FFFFFF")


def conjunto(cena, pose, dx=0.0, alfa=1.0, cor=CABINE, sombra=True):
    hx, hy = pose["hx"] + dx, pose["hy"]
    carreta(cena, hx, hy, pose["th2"], alfa=alfa, sombra=sombra)
    cavalo(cena, hx, hy, pose["th1"], pose.get("dshow", pose["d"]), cor=cor, alfa=alfa, sombra=sombra)


def traseira_carreta(pose, dx=0.0):
    """centro da traseira da carreta no chão"""
    return (pose["x2"] + dx - MB.TRAS * math.cos(pose["th2"]), pose["y2"] - MB.TRAS * math.sin(pose["th2"]))
