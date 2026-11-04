"""Manobra do vídeo: ré em 90° de cavalo + semirreboque de 53 pés para a doca, pelo lado do motorista.
Mundo em metros: X leste, Y norte, Z para cima. Prédio em y > 0, para-choques da doca na linha y = 0, porta-alvo em x = 0.

Cinemática inversa (quinta roda sobre o eixo traseiro do cavalo): desenha-se o caminho do eixo da carreta (reta → curva
com entrada e saída suaves → reta para dentro da porta) e daí sai tudo o que é fisicamente obrigatório:
o engate H = eixo2 + L2·(cos th2, sin th2); o cavalo aponta para o lado oposto ao movimento de H (de ré);
o esterço sai de tan(d) = L1·(dth1/dt) / v. O ângulo do engate phi = th1 − th2 chega a ~45° no meio da curva.
O caminho é parametrizado pela distância s percorrida pelo eixo da carreta; estado(s) devolve a pose completa."""
import math
from functools import lru_cache
import numpy as np

L1 = 5.2       # entre-eixos do cavalo
L2 = 12.2      # pino-rei → centro do tandem da carreta
KP_FRENTE = 1.0                  # pino-rei → frente da carreta
TRAS = 2.95                      # centro do tandem → traseira da carreta (16,15 m no total = 53 pés)
LARG = 2.6                       # largura (102 polegadas)
PHI_MAX = math.radians(45)       # pico do ângulo do engate
RAMPA = 7.0                      # m de entrada/saída da curva (clotoide)
RETA_FIM = 9.0                   # m de ré reta até a doca
RETA_INI = 1.5                   # m de ré reta antes de começar a curva
FIM_Y = -0.25                    # traseira da carreta para aqui
DS = 0.02


@lru_cache(None)
def caminho():
    """amostras (s, x2, y2, th2) do eixo da carreta, de ré, do ponto de partida até a doca"""
    km = math.tan(PHI_MAX) / L2
    giro = math.pi / 2
    # rampa sobe (ângulo km·R/2), plato, rampa desce (km·R/2): plato = (giro − km·R)/km
    plato = (giro - km * RAMPA) / km
    ks, s = [], 0.0
    total = RETA_INI + 2 * RAMPA + plato + RETA_FIM
    while s <= total + 1e-9:
        u = s - RETA_INI
        if u < 0:
            k = 0
        elif u < RAMPA:
            k = km * u / RAMPA
        elif u < RAMPA + plato:
            k = km
        elif u < 2 * RAMPA + plato:
            k = km * (2 * RAMPA + plato - u) / RAMPA
        else:
            k = 0
        ks.append(k)
        s += DS
    ks = np.array(ks)
    psi = math.pi - np.concatenate([[0], np.cumsum((ks[1:] + ks[:-1]) / 2 * DS)])   # direção de ré: oeste → norte
    psi[-1 * int(RETA_FIM / DS):] = math.pi / 2
    x = np.concatenate([[0], np.cumsum(np.cos(psi[:-1]) * DS)])
    y = np.concatenate([[0], np.cumsum(np.sin(psi[:-1]) * DS)])
    th2 = psi - math.pi
    # encaixe: no fim, eixo em x = 0 e traseira em FIM_Y
    x += -x[-1]
    y += (FIM_Y - TRAS) - y[-1]
    sarr = np.arange(len(x)) * DS
    return sarr, x, y, th2


@lru_cache(None)
def poses():
    """(s, x2, y2, th2, hx, hy, th1, phi, d) ao longo do caminho"""
    s, x2, y2, th2 = caminho()
    hx, hy = x2 + L2 * np.cos(th2), y2 + L2 * np.sin(th2)
    dhx, dhy = np.gradient(hx, s), np.gradient(hy, s)
    th1 = np.unwrap(np.arctan2(-dhy, -dhx))                 # de ré: o cavalo aponta contra o movimento do engate
    phi = th1 - th2
    vh = np.hypot(dhx, dhy)                                  # m de engate por m de carreta
    w1 = np.gradient(th1, s)
    d = np.arctan(L1 * w1 / -np.maximum(vh, 1e-6))
    return s, x2, y2, th2, hx, hy, th1, phi, d


def estado(sv):
    """pose interpolada na distância sv (0 = parado no início da ré)"""
    P = poses()
    s = P[0]
    sv = min(max(sv, 0.0), s[-1])
    return {k: float(np.interp(sv, s, a)) for k, a in zip(("s", "x2", "y2", "th2", "hx", "hy", "th1", "phi", "d"), P)}


def comprimento():
    return float(poses()[0][-1])


def s_onde(cond):
    """primeiro s em que cond(pose) vale"""
    P = poses()
    for i in range(len(P[0])):
        if cond({k: P[j][i] for j, k in enumerate(("s", "x2", "y2", "th2", "hx", "hy", "th1", "phi", "d"))}):
            return float(P[0][i])
    return None


if __name__ == "__main__":
    s, x2, y2, th2, hx, hy, th1, phi, d = poses()
    print("comprimento", round(s[-1], 1), "m · início eixo2", round(x2[0], 2), round(y2[0], 2), "· engate", round(hx[0], 2))
    print("phi máx", round(math.degrees(phi.max()), 1), "· esterço mín/máx", round(math.degrees(d.min()), 1), round(math.degrees(d.max()), 1))
    print("fim: eixo2", round(x2[-1], 2), round(y2[-1], 2), "th2", round(math.degrees(th2[-1]), 1), "th1", round(math.degrees(th1[-1]), 1))
    for i in range(0, len(s), 100):
        print(f"s {s[i]:5.1f}  eixo2 ({x2[i]:6.1f},{y2[i]:6.1f})  th2 {math.degrees(th2[i]):6.1f}  th1 {math.degrees(th1[i]):6.1f}"
              f"  phi {math.degrees(phi[i]):5.1f}  d {math.degrees(d[i]):6.1f}")
