"""Baliza de limusine: o método de carro (manuais de Manitoba e da Califórnia) e a versão que funciona para uma limusine,
simulados com cinemática de bicicleta (eixo traseiro como referência, sem escorregamento).
Mundo em metros: X leste (sentido do trânsito), Y norte; meio-fio em y = 0, vagas em 0 < y < 2,4, faixa acima.

Limusine: Lincoln Town Car esticada 120 pol. (entre-eixos 117,7 + 120 = 237,7 pol. = 6,04 m), 28 pés (8,53 m).
Esterço máximo 30°: o diâmetro de giro do Town Car de série é dado como 12,8 (m) em fichas técnicas (entre-eixos de
2,99 m → ~28° na roda de fora, ~33° na de dentro); o esticamento não muda o esterço, só o entre-eixos.
Carros estacionados: sedãs de 4,9 × 1,85 m.

Fases (ré, salvo D): 0 ao lado do carro da frente (B), para-choques traseiros alinhados; A volante todo para o
meio-fio até o ângulo-alvo; B rodas retas até a quina dianteira direita passar o para-choque de B; C volante todo
para o outro lado até ficar paralela; D para a frente até centralizar entre B e C.
Resultado da varredura (folga lateral × ângulo × vaga): com 2 pés de folga e 45° a traseira bate no meio-fio; a
combinação mais curta que funciona é ~4 pés (1,25 m) de folga, 20° e uma vaga de ~40 pés (12,2 m)."""
import math
from functools import lru_cache
import numpy as np

COMP, LARG = 8.53, 2.0
EE = 6.04
BALANCO_TRAS = 1.45
BALANCO_FRENTE = COMP - EE - BALANCO_TRAS
DMAX = math.radians(30)
CARRO = (4.9, 1.85)
Y_CARRO = 0.25                 # carros estacionados a 25 cm do meio-fio
DS = 0.02

VAGA = 12.5                    # m (41 pés): um pouco acima do mínimo da simulação
METODO = dict(folga=1.25, ang=20, passa=0.3)     # a versão para limusine
CARRO_METODO = dict(folga=0.61, ang=45, passa=0.15)  # 2 pés, 45° (o jeito de carro)
XB = 0.0                       # traseira do carro da frente


def cantos(x, y, th):
    """quinas (x, y = eixo traseiro): tras-dir, tras-esq, frente-esq, frente-dir"""
    c, s = math.cos(th), math.sin(th)
    return [(x + c * lx - s * ly, y + s * lx + c * ly)
            for lx, ly in ((-BALANCO_TRAS, -LARG / 2), (-BALANCO_TRAS, LARG / 2), (EE + BALANCO_FRENTE, LARG / 2),
                           (EE + BALANCO_FRENTE, -LARG / 2))]


def mover(st, h, d):
    x, y, th = st
    return (x + h * math.cos(th), y + h * math.sin(th), th + h * math.tan(d) / EE)


def _sep(poly, rect):
    x0, y0, x1, y1 = rect
    R = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    for P in (poly, R):
        for i in range(len(P)):
            ax, ay = P[i]
            bx, by = P[(i + 1) % len(P)]
            nx, ny = by - ay, -(bx - ax)
            pa = [nx * px + ny * py for px, py in poly]
            pb = [nx * px + ny * py for px, py in R]
            if max(pa) < min(pb) or max(pb) < min(pa):
                return True
    return False


def carros(S=VAGA):
    """retângulos (x0, y0, x1, y1) do carro da frente (B) e do de trás (C)"""
    return ((XB, Y_CARRO, XB + CARRO[0], Y_CARRO + CARRO[1]), (XB - S - CARRO[0], Y_CARRO, XB - S, Y_CARRO + CARRO[1]))


def plano(S=VAGA, folga=1.25, ang=20, passa=0.3, parar_na_batida=True):
    """lista de passos (fase, x, y, th, d, s_acumulado) e o desfecho: dict(ok, batida, meiofio)"""
    rB, rC = carros(S)
    st = (XB + BALANCO_TRAS, Y_CARRO + CARRO[1] + folga + LARG / 2, 0.0)
    rota, s_ac = [("0", *st, 0.0, 0.0)], 0.0
    batida = None

    def bate(s):
        P = cantos(*s)
        if not _sep(P, rB):
            return "car"
        if not _sep(P, rC):
            return "car"
        if min(p[1] for p in P) < 0.02:
            return "curb"
        return None

    def anda(fase, dist, d, ate):
        nonlocal st, s_ac, batida
        for _ in range(int(abs(dist) / DS)):
            st = mover(st, math.copysign(DS, dist), d)
            s_ac += DS
            rota.append((fase, *st, d, s_ac))
            b = bate(st)
            if b and batida is None:
                batida = (b, len(rota) - 1)
                if parar_na_batida:
                    return True
            if ate(st):
                return False
        return False
    if anda("A", -40, -DMAX, lambda s: s[2] >= math.radians(ang)):
        return rota, dict(ok=False, batida=batida)
    if anda("B", -40, 0.0, lambda s: cantos(*s)[3][0] <= XB - passa):
        return rota, dict(ok=False, batida=batida)
    if anda("C", -40, DMAX, lambda s: s[2] <= 0.0):
        return rota, dict(ok=False, batida=batida)
    xc = XB - S / 2
    centro = lambda s: s[0] + math.cos(s[2]) * (EE + BALANCO_FRENTE - BALANCO_TRAS) / 2 >= xc
    if not centro(st):
        anda("D", 30, 0.0, centro)
    mf = min(p[1] for p in cantos(*st))
    return rota, dict(ok=batida is None and mf <= 0.46, batida=batida, meiofio=mf)


@lru_cache(None)
def limo():
    rota, r = plano(VAGA, **METODO)
    assert r["ok"], r
    return rota, r


@lru_cache(None)
def falha():
    """o jeito de carro: 2 pés de folga, 45°; para no instante em que a traseira bate no meio-fio"""
    rota, r = plano(VAGA, **CARRO_METODO)
    assert not r["ok"] and r["batida"], r
    return rota, r


def pose(rota, sv):
    """pose interpolada na distância percorrida sv"""
    S = np.array([p[5] for p in rota])
    i = int(np.clip(np.searchsorted(S, sv), 0, len(rota) - 1))
    f, x, y, th, d, s = rota[i]
    return dict(fase=f, x=x, y=y, th=th, d=d, s=s)


def marco(rota, fase):
    """distância em que a fase começa"""
    for p in rota:
        if p[0] == fase:
            return p[5]
    return rota[-1][5]


if __name__ == "__main__":
    rota, r = limo()
    print("limusine: vaga", VAGA, "m =", round(VAGA / 0.3048, 1), "pés; meio-fio", round(r["meiofio"], 2), "m; total", round(rota[-1][5], 1), "m")
    for f in "ABCD":
        print(" ", f, "começa em", round(marco(rota, f), 2))
    rf, rr = falha()
    print("jeito de carro: bateu no", rr["batida"][0], "após", round(rf[-1][5], 2), "m, ângulo", round(math.degrees(rf[-1][3]), 1))
    print("regra da Califórnia: limusine + 3 pés =", round((COMP + 0.914) / 0.3048, 1), "pés")
