"""Visual — Estudativo · MAT-ESP-007: prisma, área e volume.
Mesma linguagem da trilha (MAT-ESP-001 a 006): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
faces gêmeas em par índigo/cinza, resposta na esfera.
- A EMBALAGEM = prisma triangular deitado (prisma_deitado(), montado com E._solido na perspectiva cavaleira de E.paralelepipedo):
  a ponta de frente, em verdadeira grandeza, e o comprimento para trás. A base da vez (a ponta) fica pintada na cor da matéria.
- O bloco em volta dela (os 240 errados) é o contorno arame() de MAT-ESP-005, com as arestas de trás tracejadas.
- VOLUME = camadas: os cubinhos de MAT-ESP-005 (enche) no bloco e fatias com a forma da base (fatias()) no prisma.
- ÁREA TOTAL = a embalagem que se abre no plano (Molde de MAT-ESP-002): bases em COR, retângulos em CINZA2, a área escrita em cada face.
- O atalho (palco escuro): os três retângulos deslizam lado a lado e viram uma faixa só, tão comprida quanto o contorno da base.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-007_prisma_area_e_volume.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("prisma", "volume", "triangular", "hexagonal", "area", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
R3 = 3 ** 0.5
assert 6 * 4 * 10 == 240 and 6 * 4 == 24 and 24 / 2 == 12 and 12 * 10 == 120 and 240 == 2 * 120
assert (4 / 2) ** 2 == 4 and 6 * 4 == 24 and 24 * 10 == 240 and round(240 * 1.7) == 408
assert 3 ** 2 + 4 ** 2 == 25 and 25 ** 0.5 == 5 and 2 * 12 == 24 and 5 * 10 + 5 * 10 + 6 * 10 == 160 and 24 + 160 == 184
assert 5 + 5 + 6 == 16 and 16 * 10 == 160
assert (2 / 2) ** 2 == 1 and 6 * 1 == 6 and 6 * 5 == 30 and 2 * 6 == 12 and 6 * 2 == 12 and 12 * 5 == 60 and round(60 + 12 * R3) == 81


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)



# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³√") else est, size * (0.92 if any(ch in w for ch in "²³√") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def face(c, pts, idx, a=1.0, cor=None, alfa_=0.42):
    if a <= 0:
        return
    p = skia.Path(); p.addPoly([pts[i] for i in idx], True)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def reto(c, P, A, B, k=34, a=1.0, cor=None):
    """quadradinho de ângulo reto no vértice P, nas direções de P→A e P→B"""
    if a <= 0:
        return
    def un(Q):
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy) or 1
        return dx / n * k, dy / n * k
    u, v = un(A), un(B)
    path = skia.Path()
    path.moveTo(P[0] + u[0], P[1] + u[1]); path.lineTo(P[0] + u[0] + v[0], P[1] + u[1] + v[1]); path.lineTo(P[0] + v[0], P[1] + v[1])
    c.drawPath(path, M.paint(cor or TINTA, a, stroke=4))


def rotulo(c, t, t0, s, P, Q, n, size=56, cor=None, gap=20):
    """rótulo de um segmento PQ, afastado na direção n"""
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, n[0], n[1], gap, size, "g", cor or COR, a))


# ================= Molde: a planificação que dobra (copiada de MAT-ESP-002) =================
def _rot(P, A, u, th):
    """gira P em torno do eixo que passa por A na direção u (unitária)"""
    c_, s_ = math.cos(th), math.sin(th)
    p = (P[0] - A[0], P[1] - A[1], P[2] - A[2])
    cr = (u[1] * p[2] - u[2] * p[1], u[2] * p[0] - u[0] * p[2], u[0] * p[1] - u[1] * p[0])
    d = u[0] * p[0] + u[1] * p[1] + u[2] * p[2]
    return tuple(A[k] + p[k] * c_ + cr[k] * s_ + u[k] * d * (1 - c_) for k in range(3))


def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


LUZ = (-0.35 / 1.0, 0.85, 0.4)


def camera(k):
    """k = 0: o molde visto de cima; k = 1: de cima e de lado"""
    k = ease_io(min(1.0, max(0.0, k)))
    return E._vista_alta(lerp(0, -28, k), lerp(89.9, 34, k))


class Molde:
    def __init__(s, faces, pais):
        s.f = {n: [(u, 0.0, w) for u, w in pts] for n, pts in faces.items()}
        s.pais = pais
        s.h = {}
        for n, (pai, i, gr) in pais.items():
            P = s.f[n]
            A, B = P[i], P[(i + 1) % len(P)]
            assert any(math.dist(A, q) < 1e-6 for q in s.f[pai]) and any(math.dist(B, q) < 1e-6 for q in s.f[pai]), (n, pai)
            L = math.dist(A, B)
            u = tuple((B[k] - A[k]) / L for k in range(3))
            g = tuple(sum(q[k] for q in P) / len(P) for k in range(3))
            sg = 1 if _rot(g, A, u, 0.2)[1] > 0 else -1  # sempre dobra para cima
            s.h[n] = (A, u, sg * math.radians(gr))

    def pontos(s, n, dobra):
        P, k = s.f[n], n
        while k in s.pais:
            A, u, th = s.h[k]
            f = dobra.get(k, 0.0) if isinstance(dobra, dict) else dobra
            if f:
                P = [_rot(q, A, u, th * f) for q in P]
            k = s.pais[k][0]
        return P

    def desenha(s, c, t, dobra, cam, ox, oy, a=1.0, ta=None, cores=None, contornos=None, nums=None, tn=None, size=64, pisca=None, zoom=None):
        """ta = {face: instante em que entra}; nums = {face: texto}; tn = {face: instante do número}; pisca = {face: 0..1}.
        zoom = escala em volta de (ox, oy); sem ela, o sólido montado cresce 40% (visto de lado ele parece menor)"""
        R, U, v = camera(cam) if isinstance(cam, (int, float)) else cam
        z = zoom if zoom is not None else (1 + 0.4 * ease_io(min(1.0, max(0.0, cam))) if isinstance(cam, (int, float)) else 1.0)
        R, U = tuple(x * z for x in R), tuple(x * z for x in U)
        itens = []
        for n in s.f:
            P = s.pontos(n, dobra)
            g = tuple(sum(q[k] for q in P) / len(P) for k in range(3))
            itens.append((_dot(g, v), n, P, g))
        itens.sort()
        for _, n, P, g in itens:
            af = a * (ep(t, ta[n], 0.4) if ta and n in ta else 1.0)
            if af <= 0:
                continue
            pts = [E._proj(q, R, U, ox, oy) for q in P]
            nn = _cruz(_sub(P[1], P[0]), _sub(P[2], P[0]))
            nl = math.sqrt(_dot(nn, nn)) or 1
            nn = tuple(x / nl for x in nn)
            luz = abs(_dot(nn, LUZ)) / math.sqrt(_dot(LUZ, LUZ))
            base = (cores or {}).get(n) or E.mix(E.COR, "#FFFFFF", 0.82)
            if pisca and pisca.get(n, 0) > 0:
                base = E.mix(base, E.COR, 0.7 * pisca[n])
            fill = E.mix(base, "#000000", 0.2 * (1 - luz))
            path = skia.Path()
            path.addPoly(pts, True)
            c.drawPath(path, M.paint(fill, af))
            pt = M.paint(TINTA, af, stroke=5)
            pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(path, pt)
            if contornos and n in contornos:
                c.save(); c.clipPath(path, skia.ClipOp.kIntersect, True)
                c.drawPath(path, M.paint(contornos[n], af, stroke=22))
                c.restore()
            if nums and n in nums:
                vis = min(1.0, max(0.0, abs(_dot(nn, v)) * 3 - 0.3))
                q = af * vis * (ep(t, tn[n], 0.35) if tn and n in tn else 1.0)
                gx, gy = E._proj(g, R, U, ox, oy)
                cor_n = BR if (cores and n in cores) else (contornos[n] if contornos and n in contornos else TINTA)
                if q > 0:
                    centro(c, nums[n], gx, gy + size * 0.36, size, "g", cor_n, q)


def ret(x, w, lx, lw):
    """retângulo (u, w, largura, altura) no sentido horário"""
    return [(x, w), (x + lx, w), (x + lx, w + lw), (x, w + lw)]


# ---------------- cubinhos ----------------
KX, KY = 0.394, -0.308  # a profundidade na perspectiva cavaleira (a mesma de E.paralelepipedo)


def cubinho(c, x, y, s, a=1.0, cor=None):
    """cubinho cheio de aresta s: (x, y) = canto de baixo à esquerda da face da frente"""
    if a <= 0:
        return
    cor = cor or E.COR
    dx, dy = KX * s, KY * s
    br = M.paint("#FFFFFF", 0.9 * a, stroke=2)

    def poli(pts, tinta):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta, a)); c.drawPath(p, br)
    poli([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(cor, "#FFFFFF", 0.35))
    poli([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(cor, "#000000", 0.25))
    poli([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], cor)


def enche(c, t, cols, fil, cam, x, y, s, tf, a=1.0, cor=None):
    """cubinhos de aresta s enchendo uma caixa cols x fil x cam: tf(camada, fileira) = instante da fileira (None = não entra).
    (x, y) = canto de baixo à esquerda da frente; a fileira 0 é a da FRENTE. cor(i, j, k) pode trocar a cor de um cubinho"""
    if a <= 0:
        return
    for k in range(cam):
        for j in reversed(range(fil)):  # do fundo para a frente
            t0 = tf(k, j)
            if t0 is None:
                continue
            for i in range(cols):
                q = ep(t, t0 + 0.08 * i, 0.35)
                if q <= 0:
                    continue
                cx = x + i * s + KX * s * j
                cy = y - k * s + KY * s * j - (1 - ease_io(q)) * 40
                cubinho(c, cx, cy, s, a * q, cor(i, j, k) if callable(cor) else cor)


def arame(c, x, y, w, d, h, a=1.0, cor=None):
    """contorno de uma caixa w x d x h (px) na mesma perspectiva, com as arestas de trás tracejadas"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    pt = M.paint(cor or TINTA, a, stroke=4)
    tr = M.paint(cor or TINTA2, 0.7 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
    c.drawLine(x, y, x + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + w + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + dx, y + dy - h, tr)
    for (x0, y0, x1, y1) in ((x, y, x + w, y), (x + w, y, x + w, y - h), (x + w, y - h, x, y - h), (x, y - h, x, y),
                             (x, y - h, x + dx, y - h + dy), (x + w, y - h, x + w + dx, y - h + dy), (x + w, y, x + w + dx, y + dy),
                             (x + dx, y - h + dy, x + w + dx, y - h + dy), (x + w + dx, y - h + dy, x + w + dx, y + dy)):
        c.drawLine(x0, y0, x1, y1, pt)


def piso(c, x, y, w, d, a=1.0, cor=None, grade=None):
    """o fundo da caixa pintado (a área da base); grade = (colunas, fileiras) desenha os quadradinhos de 1 m²"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    p = skia.Path(); p.addPoly([(x, y), (x + w, y), (x + w + dx, y + dy), (x + dx, y + dy)], True)
    c.drawPath(p, M.paint(cor or E.COR, 0.35 * a))
    if grade:
        n, m = grade
        for i in range(1, n):
            M.line(c, x + w * i / n, y, x + w * i / n + dx, y + dy, "#FFFFFF", a, 3)
        for j in range(1, m):
            M.line(c, x + dx * j / m, y + dy * j / m, x + w + dx * j / m, y + dy * j / m, "#FFFFFF", a, 3)


def agua(c, x, y, w, d, h, nivel, a=1.0):
    """água até a fração nivel da altura h, dentro da caixa"""
    if a <= 0 or nivel <= 0:
        return
    dx, dy = KX * d, KY * d
    hh = h * nivel
    cor = E.mix(E.COR, "#FFFFFF", 0.45)
    for pts, al in (([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + dy - hh), (x + w, y - hh)], 0.42),
                    ([(x, y - hh), (x + w, y - hh), (x + w + dx, y - hh + dy), (x + dx, y - hh + dy)], 0.55),
                    ([(x, y), (x + w, y), (x + w, y - hh), (x, y - hh)], 0.38)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(cor, al * a))



# ================= peças desta aula =================
def alfa(c, a, fn):
    """desenha fn com transparência a"""
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def meio(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


def prisma_deitado(c, t, t0, x, y, b, hh, L, d=1.0, **kw):
    """o prisma triangular deitado: a ponta (triângulo isósceles de base b e altura hh, px) de frente, em verdadeira grandeza,
    e o comprimento L (px) para trás, na perspectiva cavaleira de E.paralelepipedo. (x, y) = canto de baixo à esquerda da ponta.
    pts: 0, 1, 2 = a ponta da frente (embaixo esq, embaixo dir, topo); 3, 4, 5 = a de trás, na mesma ordem"""
    V = [(0, 0, 0), (b, 0, 0), (b / 2, hh, 0), (0, 0, L), (b, 0, L), (b / 2, hh, L)]
    F = [(0, 1, 2), (3, 4, 5), (0, 1, 4, 3), (1, 2, 5, 4), (2, 0, 3, 5)]
    return E._solido(c, t, t0, V, F, E._vista_obliqua(), x, y, kw.pop("cor", None), kw.pop("preenche", 0.14), d=d, **kw)


def medidas_emb(c, t, pts, tb, th, tl, size=50, base="6 cm", alt="4 cm", comp="10 cm"):
    """as medidas da embalagem: base da ponta, altura da ponta (tracejada, no meio) e comprimento"""
    if tb is not None:
        E._medida_aresta(c, t, tb, pts[0], pts[1], base, (0, 1), size)
    if th is not None:
        pe = meio(pts[0], pts[1])
        E.segmento(c, t, th, pts[2], pe, None, cor=TINTA2, pontas=False, tracejado=True, largura=5)
        E.foco(c, t, th + 0.3, 0.4, lambda a: E._cola(c, alt, pe[0], lerp(pe[1], pts[2][1], 0.24), 1, 0, 12, size * 0.9, "b", COR, a))
    if tl is not None:
        E._medida_aresta(c, t, tl, pts[1], pts[4], comp, (1, 0.35), size)


def medidas_prisma(c, t, pts, n, ta, th, aresta_, altura, size=50):
    """rótulos do E.prisma em instantes separados: aresta da base (na frente) e altura (aresta lateral da direita)"""
    if ta is not None:
        i_fr = max(range(n), key=lambda i: pts[i][1] + pts[(i + 1) % n][1])
        E._medida_aresta(c, t, ta, pts[i_fr], pts[(i_fr + 1) % n], aresta_, (0, 1), size)
    if th is not None:
        i_dir = max(range(n), key=lambda i: pts[i][0])
        E._medida_aresta(c, t, th, pts[i_dir], pts[n + i_dir], altura, (1, 0), size)


def fatias(c, t, ts, cx, cy, n, r, hs, vista=(-24, 22)):
    """o prisma em camadas: cada fatia tem a forma da base e entra caindo no instante ts[i]"""
    R, U, _ = E._vista_alta(*vista)
    for i, ti in enumerate(ts):
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        ox, oy = E._proj((0, i * (hs + 22), 0), R, U, cx, cy)
        alfa(c, q, lambda ox=ox, oy=oy, ti=ti: E.prisma(c, t, ti - 0.3, ox, oy - (1 - ease_io(q)) * 40, n, r, hs, d=0.5, vista=vista, preenche=0.2))


def hexagono(c, t, t0, cx, cy, r, tt=None, lado=None, pinta=(), a=1.0):
    """hexágono regular de lado deitado embaixo; tt = instante dos 6 cortes do centro aos vértices; pinta = triângulos em COR"""
    pts = E.regular(c, t, t0, 6, cx, cy, r, lado=lado, preenche=0.08)
    if tt is not None:
        for k in range(6):
            q = ep(t, tt + 0.08 * k, 0.4)
            if k in pinta and q > 0:
                p = skia.Path(); p.addPoly([(cx, cy), pts[k], pts[(k + 1) % 6]], True)
                c.drawPath(p, M.paint(E.COR, 0.45 * q * a))
            M.line(c, cx, cy, *pts[k], TINTA, a, 4, progress=ease_io(prog(t, tt + 0.08 * k, 0.4)))
    return pts


def molde_emb(s, L):
    """a embalagem aberta: retângulos 5, 6 e 5 (x L) lado a lado e as duas pontas (triângulo de base 6 e altura 4) no do meio.
    O retângulo do meio (6) é o chão; os de 5 dobram até se encontrarem no alto"""
    gr = 180 - math.degrees(math.atan2(4, 3))
    F = {"r1": ret(-3 * s - 5 * s, -L / 2, 5 * s, L), "r2": ret(-3 * s, -L / 2, 6 * s, L), "r3": ret(3 * s, -L / 2, 5 * s, L),
         "t1": [(-3 * s, -L / 2), (3 * s, -L / 2), (0, -L / 2 - 4 * s)], "t2": [(3 * s, L / 2), (-3 * s, L / 2), (0, L / 2 + 4 * s)]}
    P = {"r1": ("r2", 1, gr), "r3": ("r2", 3, gr), "t1": ("r2", 0, 90), "t2": ("r2", 0, 90)}
    return Molde(F, P)


EMB = molde_emb(36, 360)
OX, OY = 470, 560
EX, EY, EB, EH, EL = 150, 830, 360, 240, 600   # a embalagem: 6 x 4 x 10 cm, 60 px por cm


def embalagem(c, t, t0, pinta=None, d=1.0):
    pts = prisma_deitado(c, t, t0, EX, EY, EB, EH, EL, d=d)
    if pinta is not None:
        face(c, pts, (0, 1, 2), pinta, alfa_=0.5)
    return pts


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s01.{k}"] for k in "abcde")

    def um():
        pts = embalagem(c, t, a1, ep(t, b1, 0.5))
        medidas_emb(c, t, pts, b1 + 0.2, b1 + 0.6, c1)
        arame(c, EX, EY, EB, EL, EH, ep(t, d1, 0.5), ERRADO)
        X = 1020
        E.frase(c, t, a1 + 0.2, ps("embalagem em", "i", 70) + [("prisma", "g", 76, COR)], X, 250, "left", 0.1)
        E.frase(c, t, a1 + 1.0, ps("deitada", "i", 70), X, 340, "left", 0.1)
        E.frase(c, t, b1, ps("ponta: triângulo", "i", 60, TINTA2), X, 470, "left", 0.1)
        E.frase(c, t, d1, ps("multiplicar tudo?", "i", 66), X, 620, "left", 0.1)
        fcen(c, t, d1 + 0.6, "6 × 4 × 10 = 240", X + 360, 740, 80, ERRADO)
        if t >= e1:
            E.risco(c, X, 760, X + 720, 690, t, e1, largura=10)
        E.frase(c, t, e1 + 0.3, ps("é o", "i", 70) + [("dobro", "g", 76, ERRADO)] + ps("do certo", "i", 70), X, 880, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("volume", "g", 110, COR)] + ps("e", "i", 100), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), [("área", "g", 110, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("de um prisma", "i", 90), XE, 720, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "bloco: volume =", "área da base × altura", 0), ("s03.c", "área do triângulo:", "A = f{base × altura}{2}", 1),
             ("s03.d", "hexágono regular =", "6 triângulos equiláteros", 0))
    for i, (k, l1, l2, fr_) in enumerate(itens):
        y = 170 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 76, "left", 0.1)
        if fr_:
            E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 158, 58, "g", COR)
        else:
            E.frase(c, t, C[k] + 0.4, [(l2, "g", 56, COR)], x + 44, y + 160)
    alvo = [190 + i * 250 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- o que é prisma ----------------
def lateral_frente(pts, n, cy):
    """as faces laterais de um E.prisma que ficam de frente para quem olha"""
    return [i for i in range(n) if (pts[i][1] + pts[(i + 1) % n][1]) / 2 > cy]


def b_prisma(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    X = 1060

    def um():
        n, cx, cy = 5, 520, 860
        pts = E.prisma(c, t, a4, cx, cy, n, 230, 420)
        if t >= b4:
            q = ep(t, b4, 0.5)
            face(c, pts, list(range(n)), q, alfa_=0.35)
            face(c, pts, list(range(n, 2 * n)), q, alfa_=0.5)
        if t >= c4:
            for k, i in enumerate(lateral_frente(pts, n, cy)):
                face(c, pts, (i, (i + 1) % n, n + (i + 1) % n, n + i), ep(t, c4 + 0.25 * k, 0.4), CINZA2, 0.5)
        if t >= d4:
            g0 = (sum(p[0] for p in pts[:n]) / n, sum(p[1] for p in pts[:n]) / n)
            g1 = (sum(p[0] for p in pts[n:]) / n, sum(p[1] for p in pts[n:]) / n)
            aresta(c, t, d4, g1, g0, largura=7, tracejada=True)
            xd = max(p[0] for p in pts) + 24
            E.foco(c, t, d4 + 0.4, 0.4, lambda a: E.escreve(c, "altura", xd, lerp(g0[1], g1[1], 0.5) + 18, 52, "g", COR, a))
        E.frase(c, t, a4, [("prisma", "g", 96, COR)], X, 250, "left", 0.1)
        E.frase(c, t, b4, [("2 bases iguais,", "g", 62, COR)], X, 400, "left", 0.1)
        E.frase(c, t, b4 + 0.7, ps("uma de frente para a outra", "i", 54), X, 480, "left", 0.1)
        E.frase(c, t, c4, ps("ligadas por", "i", 58) + [("retângulos", "g", 62)], X, 610, "left", 0.1)
        E.frase(c, t, c4 + 0.7, ps("as faces laterais", "i", 54, TINTA2), X, 690, "left", 0.1)
        E.frase(c, t, d4, [("altura", "g", 62, COR)] + ps("= distância", "i", 58), X, 820, "left", 0.1)
        E.frase(c, t, d4 + 0.6, ps("entre as duas bases", "i", 58), X, 900, "left", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, C["s05"] + 0.2, ps("o nome vem da", "i", 76) + [("base", "g", 80, COR)], W / 2, 210, "center", 0.1)
    pt3 = E.prisma(c, t, a5 - 0.3, 360, 800, 3, 170, 300)
    if t >= a5:
        face(c, pt3, (3, 4, 5), ep(t, a5 + 0.3, 0.4), alfa_=0.6)
    E.foco(c, t, a5 + 0.4, 0.4, lambda q: (centro(c, "triangular", 360, 940, 58, "g", COR, q)))
    pt6 = E.prisma(c, t, b5 - 0.3, 960, 800, 6, 160, 300)
    if t >= b5:
        face(c, pt6, list(range(6, 12)), ep(t, b5 + 0.3, 0.4), alfa_=0.6)
    E.foco(c, t, b5 + 0.4, 0.4, lambda q: (centro(c, "hexagonal", 960, 940, 58, "g", COR, q)))
    ptb = E.paralelepipedo(c, t, c5 - 0.3, 1400, 800, 300, 260, 240)
    if t >= c5:
        face(c, ptb, (3, 2, 6, 7), ep(t, c5 + 0.3, 0.4), alfa_=0.6)
    E.foco(c, t, c5 + 0.4, 0.4, lambda q: (centro(c, "retangular", 1600, 940, 58, "g", COR, q),
                                           centro(c, "o bloco", 1600, 1000, 46, "i", TINTA2, q)))


# ---------------- volume ----------------
def b_volume(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def camadas():
        x, y, s = 170, 880, 100
        w, d, h = 4 * s, 3 * s, 2 * s
        arame(c, x, y, w, d, h, ep(t, C["s06"], 0.5))
        piso(c, x, y, w, d, ep(t, a6, 0.5) * (1 - ep(t, b6 + 0.6, 0.4)), grade=(4, 3))
        enche(c, t, 4, 3, 2, x, y, s, lambda k, j: (b6 + 0.15 * (2 - j)) if k == 0 else (c6 + 0.15 * (2 - j)))
        E.frase(c, t, a6, [("área do fundo", "g", 58, COR)], 120, 260, "left", 0.1)
        E.frase(c, t, b6, ps("= cubinhos da 1ª camada", "i", 54), 120, 340, "left", 0.1)
        E.frase(c, t, c6, [("altura", "g", 58, COR)] + ps("= nº de camadas", "i", 54), 120, 450, "left", 0.1)
        fatias(c, t, [d6 + 0.4 * i for i in range(3)], 1420, 880, 3, 200, 80)
        E.frase(c, t, d6, ps("no prisma, cada camada", "i", 54), 1420, 260, "center", 0.1)
        E.frase(c, t, d6 + 0.7, ps("tem a", "i", 58) + [("forma da base", "g", 60, COR)], 1420, 340, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, camadas)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, C["s07"] + 0.2, ps("a regra do bloco vale para", "i", 66) + [("todo prisma", "g", 70, COR)], W / 2, 200, "center", 0.1)
    E.frase(c, t, a7, [("volume", "g", 92, COR)] + ps("=", "i", 84) + [("área da base", "g", 84)] + ps("× altura", "i", 84), W / 2, 370, "center", 0.12)
    E.frase(c, t, b7, ps("só muda", "i", 62) + [("a forma da base", "g", 64, COR)], W / 2, 520, "center", 0.1)
    E.regular(c, t, c7, 3, 500, 790, 170, preenche=0.3)
    E.regular(c, t, c7 + 0.5, 6, 960, 790, 160, preenche=0.3)
    E.poligono(c, t, c7 + 1.0, [(1300, 900), (1560, 900), (1620, 760), (1470, 640), (1330, 720)], preenche=0.3)
    for k, (s_, x_) in enumerate((("triângulo", 500), ("hexágono", 960), ("o que for", 1460))):
        E.foco(c, t, c7 + 0.5 * k + 0.4, 0.4, lambda q, s_=s_, x_=x_: centro(c, s_, x_, 1010, 52, "i", TINTA2, q))
    E.foco(c, t, lerp(c7, C["s07.end"], 0.6), 0.5, lambda q: E.pilula(c, "1º: a área da base", 1500, 520, 52, "g", a=q, cor=E.SOBRE))


# ---------------- prisma triangular ----------------
def b_triangular(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    pts = embalagem(c, t, C["s08"], ep(t, a8, 0.5))
    medidas_emb(c, t, pts, C["s08"] + 0.8, C["s08"] + 1.0, C["s08"] + 1.2)
    X = 1360

    def volume():
        E.frase(c, t, a8, ps("base =", "i", 62) + [("o triângulo da ponta", "g", 62, COR)], X, 230, "center", 0.1)
        fcen(c, t, b8, "6 × 4 = 24", X, 370, 80)
        fcen(c, t, c8, "24 ÷ 2 = 12 cm²", X, 490, 80, COR)
        aresta(c, t, d8, pts[1], pts[4], largura=12)
        E.frase(c, t, d8, ps("deitada: a altura vai", "i", 56) + [("de ponta a ponta", "g", 56)], X, 640, "center", 0.1)
        fcen(c, t, d8 + 0.8, "altura = 10 cm", X, 730, 66, TINTA2)
        fcen(c, t, e8, "12 × 10", X - 230, 900, 80)
        bola_txt(c, t, e8 + 0.6, "120 cm³", X + 170, 880, 130, 56)
    fase(c, t, C["s08"], C["s09"] - 0.1, volume)
    if t < C["s09"] - 0.1:
        return
    arame(c, EX, EY, EB, EL, EH, ep(t, a9, 0.5), TINTA2)
    if t >= c9:
        q = ep(t, c9, 0.5)
        for tri in ((pts[0], (EX, EY - EH), pts[2]), (pts[1], (EX + EB, EY - EH), pts[2])):
            p = skia.Path(); p.addPoly(list(tri), True)
            c.drawPath(p, M.paint(TINTA2, 0.35 * q))
    E.frase(c, t, C["s09"] + 0.2, ps("e os", "i", 66) + [("240?", "g", 72, ERRADO)], X, 230, "center", 0.1)
    fcen(c, t, a9, "6 × 4 × 10 = 240", X, 380, 72, TINTA2)
    E.frase(c, t, a9 + 0.6, ps("é o", "i", 56, TINTA2) + [("bloco em volta", "g", 58)], X, 460, "center", 0.1)
    E.frase(c, t, b9, ps("faltou o", "i", 62) + [("÷ 2", "g", 70, ERRADO)] + ps("do triângulo", "i", 62), X, 610, "center", 0.1)
    E.frase(c, t, c9, ps("o prisma é", "i", 66) + [("metade do bloco", "g", 66, COR)], X, 770, "center", 0.1)
    fcen(c, t, c9 + 0.8, "240 ÷ 2 = 120", X, 900, 76)


# ---------------- prisma hexagonal ----------------
HX, HY = 1000, 560


def b_hexagonal(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    pts = E.prisma(c, t, C["s10"] + 0.2, 330, 900, 6, 150, 400)
    if t >= c0:
        face(c, pts, list(range(6, 12)), ep(t, c0, 0.5), alfa_=0.5)
    medidas_prisma(c, t, pts, 6, a0, b0, "4 cm", "10 cm", 52)
    E.frase(c, t, C["s10"] + 0.2, ps("prisma", "i", 70) + [("hexagonal", "g", 74, COR)], 120, 200, "left", 0.1)

    def base():
        hexagono(c, t, c0 - 0.2, HX, HY, 200, tt=c0 + 0.3, lado="4", pinta=(0,) if t >= d0 else ())
        E.foco(c, t, c0 + 0.8, 0.4, lambda q: centro(c, "6 triângulos equiláteros", HX, 870, 50, "i", TINTA2, q))
        X2 = 1590
        fcen(c, t, lerp(c0, d0, 0.45), "A = (f{ℓ}{2})² · r{3}", X2, 300, 64, COR)
        E.frase(c, t, lerp(c0, d0, 0.45) + 0.6, ps("atalho da metade do lado", "i", 42, TINTA2), X2, 380, "center", 0.08)
        fcen(c, t, d0, "f{4}{2} = 2", X2, 530, 68)
        fcen(c, t, d0 + 1.2, "2² = 4", X2, 660, 68)
        E.frase(c, t, e0, ps("cada triângulo:", "i", 54), X2, 790, "center", 0.1)
        fcen(c, t, e0 + 0.4, "4r{3}", X2, 900, 90, COR)
    fase(c, t, C["s10"], C["s11"] - 0.1, base)
    if t < C["s11"] - 0.1:
        return
    X = 1220
    fcen(c, t, a1, "6 × 4r{3} = 24r{3} cm²", X, 300, 76)
    E.frase(c, t, a1 + 1.0, ps("a área da base", "i", 52, TINTA2), X, 380, "center", 0.1)
    fcen(c, t, b1, "24r{3} × 10 = 240r{3} cm³", X, 540, 76, COR)
    fcen(c, t, c1 - 1.2, "r{3} ≈ 1,7", X, 700, 64, TINTA2)
    bola_txt(c, t, c1, "≈ 408 cm³", X, 880, 140, 54)


# ---------------- área total ----------------
NUMS = {"t1": "12", "t2": "12", "r1": "5 × 10", "r2": "6 × 10", "r3": "5 × 10"}


def b_area(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3 = C["s13.a"], C["s13.b"]
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    X = 1340
    abre = ease_io(prog(t, a2, 1.8))
    k = 1 - abre
    cores = {}
    if t >= b2:
        cores.update({"t1": E.COR, "t2": E.COR})
    for i, n in enumerate(("r1", "r2", "r3")):
        if t >= c2 + 0.3 * i:
            cores[n] = CINZA2
    tn = {"t1": a4, "t2": a4 + 0.3, "r1": b4, "r3": c4, "r2": d4}
    EMB.desenha(c, t, 1 - abre, k, OX, lerp(OY, 700, k), ep(t, C["s12"], 0.5), cores=cores or None, nums=NUMS, tn=tn, size=40)

    def abrir():
        E.frase(c, t, a2, ps("abra a embalagem:", "i", 66), X, 260, "center", 0.1)
        E.frase(c, t, b2, [("2 triângulos", "g", 70, COR)] + ps("das pontas", "i", 62), X, 420, "center", 0.1)
        E.frase(c, t, c2, [("3 retângulos,", "g", 70, TINTA2)] + ps("um por lado", "i", 62), X, 540, "center", 0.1)
        E.frase(c, t, d2, [("área total", "g", 70, COR)] + ps("=", "i", 66), X, 720, "center", 0.1)
        E.frase(c, t, d2 + 0.6, ps("a soma de todas as faces", "i", 62), X, 810, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, abrir)

    def lado():
        A, B, P = (1050, 780), (1650, 780), (1350, 380)
        E.frase(c, t, C["s13"] + 0.2, ps("lados inclinados", "i", 60) + [("iguais", "g", 64, COR)], X, 220, "center", 0.1)
        E.triangulo(c, t, C["s13"] + 0.2, A, B, P, vertices=None, lados=("6", "5", "5"), preenche=0.18,
                    tl=[C["s13"] + 0.8, a3, a3 + 0.2], size=58)
        pe = meio(A, B)
        E.segmento(c, t, C["s13"] + 1.4, P, pe, None, cor=TINTA2, pontas=False, tracejado=True, largura=5)
        reto(c, pe, B, P, a=ep(t, C["s13"] + 1.8, 0.3))
        E.foco(c, t, C["s13"] + 1.8, 0.4, lambda q: E._cola(c, "4", pe[0], lerp(pe[1], P[1], 0.45), 1, 0, 14, 54, "g", TINTA2, q))
        th = lerp(a3, b3, 0.4)
        aresta(c, t, th, A, pe, largura=10)
        E.foco(c, t, th + 0.2, 0.4, lambda q: centro(c, "3", lerp(A[0], pe[0], 0.5), pe[1] - 24, 50, "g", COR, q))
        fcen(c, t, b3, "3² + 4² = 25", 1350 - 200, 960, 64)
        fcen(c, t, b3 + 1.6, "r{25} = 5", 1350 + 250, 960, 64, COR)
    fase(c, t, C["s13"], C["s14"] - 0.1, lado)
    if t < C["s14"] - 0.1:
        return
    fcen(c, t, a4, "bases: 2 × 12 = 24", X, 240, 64, COR)
    E.frase(c, t, b4, ps("laterais:", "i", 58), X - 380, 400, "left", 0.1)
    for kk, (tk, s_) in enumerate(((b4, "5 × 10 = 50"), (c4, "+ 5 × 10 = 50"), (d4, "+ 6 × 10 = 60"))):
        E.formula_em(c, t, tk + 0.2, s_, X + 300, 400 + 90 * kk, 56, "g", TINTA, "right")
    fcen(c, t, lerp(d4, e4, 0.6), "= 160", X + 160, 680, 60, TINTA2)
    fcen(c, t, e4, "24 + 160", X - 160, 860, 74)
    bola_txt(c, t, e4 + 0.7, "184 cm²", X + 240, 860, 130, 52)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    X = 1340
    pisca = {n: math.sin(math.pi * min(1, prog(t, c5 + 0.4 * i, 0.8))) for i, n in enumerate(("t1", "t2"))} if t >= c5 else None
    cont = {"t1": ERRADO, "t2": ERRADO} if a5 <= t < c5 else None
    EMB.desenha(c, t, 0, 0, OX, OY, ep(t, C["s15"], 0.5), cores={"r1": CINZA2, "r2": CINZA2, "r3": CINZA2, **({"t1": E.COR, "t2": E.COR} if t >= c5 else {})},
                contornos=cont, pisca=pisca, nums=NUMS, size=40)
    E.frase(c, t, C["s15"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 230, "center", 0.1)
    E.frase(c, t, a5, ps("esquecer as", "i", 66) + [("bases", "g", 70, ERRADO)], X, 330, "center", 0.1)
    E.frase(c, t, b5, ps("só os retângulos:", "i", 58), X, 480, "center", 0.1)
    fcen(c, t, b5 + 0.6, "160 cm²", X, 590, 80, ERRADO)
    if t >= b5 + 1.2:
        E.risco(c, X - 170, 605, X + 170, 545, t, b5 + 1.2, largura=10)
    E.frase(c, t, c5, [("2 pontas", "g", 66, COR)] + ps("para fechar", "i", 62), X, 740, "center", 0.1)
    E.foco(c, t, d5, 0.5, lambda q: E.pilula(c, "prisma: sempre 2 bases", X, 900, 62, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s16"] + 0.2, ps("atalho da", "i", 70, CLARO) + [("área lateral", "g", 74, BR)], W / 2, 200, "center", 0.1)
        E.frase(c, t, a6, [("perímetro da base", "g", 80, BR)] + ps("× altura", "i", 80, CLARO), W / 2, 360, "center", 0.12)
        E.triangulo(c, t, a6 + 0.4, (220, 900), (580, 900), (400, 660), vertices=None, lados=("6", "5", "5"), escuro=True, preenche=0.25,
                    tl=[b6 + 0.4, b6, b6 + 0.2], size=56)
        fcen(c, t, b6, "5 + 5 + 6 = 16", 1150, 620, 84, BR)
        fcen(c, t, c6, "16 × 10 = 160", 1000, 830, 84, CLARO)
        bola_txt(c, t, c6 + 0.8, "160", 1560, 820, 110, 70)
        E.frase(c, t, lerp(c6, C["s16.end"], 0.6), ps("uma conta só", "i", 56, CLARO), 1560, 1000, "center", 0.1)
    fase(c, t, C["s16"], C["s17"] - 0.1, um)
    if t < C["s17"] - 0.1:
        return
    s, y0, hh = 34, 300, 340
    larg = (5 * s, 5 * s, 6 * s)
    junta = ease_io(prog(t, b7, 1.0))
    total = sum(larg)
    x_j = W / 2 - total / 2
    x_s = W / 2 - (total + 2 * 90) / 2
    xx_j, xx_s = x_j, x_s
    cores = (CLARO, CLARO, CLARO)
    for i, w_ in enumerate(larg):
        q = ep(t, a7 + 0.2 * i, 0.4)
        x = lerp(xx_s, xx_j, junta)
        xx_s += w_ + 90
        xx_j += w_
        if q <= 0:
            continue
        sem = i == 2 and t >= d7
        r = skia.Rect.MakeXYWH(x, y0, w_, hh)
        if not sem:
            c.drawRect(r, M.paint(E.COR, 0.55 * q))
            c.drawRect(r, M.paint(BR, q, stroke=4))
        else:
            pt = M.paint(ERRADO, q, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
            c.drawRect(r, pt)
            E.foco(c, t, d7 + 0.3, 0.4, lambda a, x=x, w_=w_: centro(c, "sem papel", x + w_ / 2, y0 + hh / 2 + 15, 40, "g", ERRADO, a))
        E.foco(c, t, a7 + 0.2 * i + 0.2, 0.4, lambda a, x=x, w_=w_, i=i: centro(c, ("5", "5", "6")[i], x + w_ / 2, y0 + hh + 60, 52, "g", BR, a))
    E.foco(c, t, a7 + 0.6, 0.4, lambda a: E._cola(c, "10", lerp(x_s, x_j, junta), y0 + hh / 2, -1, 0, 18, 56, "g", CLARO, a))
    E.frase(c, t, a7, ps("todos têm a", "i", 60, CLARO) + [("altura do prisma", "g", 62, BR)], W / 2, 210, "center", 0.1)
    if t >= b7 + 0.8:
        E.chave(c, x_j, x_j + total, y0 + hh + 100, CLARO, ep(t, b7 + 0.8, 0.5), h=22)
        E.foco(c, t, b7 + 1.0, 0.4, lambda a: centro(c, "16 = o contorno da base", W / 2, y0 + hh + 190, 56, "g", BR, a))
    E.frase(c, t, c7, ps("não inclui as bases:", "i", 58, CLARO) + [("some as 2 no fim", "g", 60, BR)], W / 2, 900, "center", 0.1)

    def calha():
        E.frase(c, t, d7, ps("calha aberta em cima:", "i", 58, CLARO) + [("tire o lado sem papel", "g", 60, ERRADO)], W / 2, 1000, "center", 0.1)
    calha()


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a8, ps("peça de madeira:", "i", 64) + [("prisma hexagonal", "g", 64, COR)], XE, 340, passo=0.1)
    E.frase(c, t, b8, ps("lado da base", "i", 64) + [("2 cm", "g", 66, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c8, ps("altura", "i", 64) + [("5 cm", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, d8, [("1)", "g", 64, COR)] + ps("volume?", "i", 70), XE, 720, passo=0.1)
    E.frase(c, t, e8, [("2)", "g", 64, COR)] + ps("área total?", "i", 70), XE, 830, passo=0.1)
    E.frase(c, t, e8 + 1.0, ps("pode deixar o", "i", 52, TINTA2) + [("√3", "g", 52, TINTA2)], XE, 950, passo=0.1)

    def peca():
        pts = E.prisma(c, t, a8, 1450, 860, 6, 170, 425)
        medidas_prisma(c, t, pts, 6, b8, c8, "2 cm", "5 cm", 54)
    E.saida(c, t, C["s19.a"] - 0.1, peca)
    E.relogio(c, t, C["s19.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    X = 1260

    def volume():
        hexagono(c, t, C["s20"] + 0.2, 420, 560, 210, tt=C["s20"] + 0.6, lado="2", pinta=tuple(range(6)) if t >= c0 else (0,) if t >= b0 else ())
        E.frase(c, t, C["s20"] + 0.2, [("1)", "g", 64, COR)] + ps("volume", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a0, "f{2}{2} = 1    1² = 1", X, 340, 70)
        E.frase(c, t, b0, ps("cada triângulo:", "i", 56), X - 120, 480, "center", 0.1)
        fcen(c, t, b0 + 0.5, "r{3}", X + 190, 480, 70, COR)
        fcen(c, t, c0, "base: 6r{3}", X, 620, 70)
        fcen(c, t, d0, "6r{3} × 5", X - 220, 830, 74)
        bola_txt(c, t, d0 + 0.7, "30r{3} cm³", X + 230, 820, 150, 54)
    fase(c, t, C["s20"], C["s21"] - 0.1, volume)
    if t < C["s21"] - 0.1:
        return
    E.frase(c, t, C["s21"] + 0.2, [("2)", "g", 64, COR)] + ps("área total", "i", 66), W / 2, 200, "center", 0.1)
    fcen(c, t, a1, "2 bases: 2 × 6r{3} = 12r{3}", W / 2, 340, 70)
    fcen(c, t, b1, "perímetro: 6 × 2 = 12", W / 2, 470, 70, TINTA2)
    fcen(c, t, c1, "laterais: 12 × 5 = 60", W / 2, 600, 70)
    bola_txt(c, t, d1, "60 + 12r{3} cm²", W / 2 - 160, 860, 195, 46)
    E.frase(c, t, e1, ps("perto de", "i", 60) + [("80 cm²", "g", 64, COR)], W / 2 + 120, 880, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s22.a", ps("volume =", "i", 66) + [("área da base × altura", "g", 64, COR)]),
                 ("s22.b", ps("área total =", "i", 66) + [("2 bases + laterais", "g", 64, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3, d3 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a3, [("Cilindro", "g", 130, COR)], XE, 420)
    E.frase(c, t, b3, ps("a lata de", "i", 64) + [("raio 5", "g", 66, COR)] + ps("e", "i", 64) + [("altura 10", "g", 66, COR)], XE, 540, passo=0.1)
    E.frase(c, t, b3 + 1.2, ps("quanto cabe e quanto metal gasta", "i", 58), XE, 640, passo=0.1)
    E.cilindro(c, t, a3, 1560, 800, 100, 200)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c3 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c3 + 0.2, 0.4))
    E.frase(c, t, d3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], 1500, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, prisma=b_prisma, volume=b_volume, triangular=b_triangular, hexagonal=b_hexagonal,
              area=b_area, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
