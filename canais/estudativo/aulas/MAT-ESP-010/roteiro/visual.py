"""Visual — Estudativo · MAT-ESP-010: praticando sólidos, prismas e cilindros (4 situações inéditas).
Mesma linguagem da trilha (MAT-ESP-001 a 009): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
faces gêmeas em par índigo/cinza, resposta na esfera. Estrutura das aulas de prática (MAT-ANG-019): a pílula "situação n de 4"
com os pontos de progresso (situacao()), o enunciado com a figura e o relógio de pausa.
- Situação 1: o molde do cilindro (rotulo_lata(), de MAT-ESP-002) e a lata montada ao lado.
- Situação 2: o molde do prisma de base 3-4-5 que DOBRA DE VERDADE (Molde, de MAT-ESP-002): bases em COR, retângulos em CINZA2.
- Situação 3: as vistas (de cima, um círculo; de frente, um retângulo) que viram o cilindro.
- Situação 4: o reservatório com a água subindo (agua(), de MAT-ESP-005), a cota marca() e a bomba (torneira(), de MAT-ESP-009).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-010_praticando_solidos_prismas_e_cilindros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
PI = 3
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cilindro
assert 2 * PI * 4 == 24 and PI * 4 ** 2 == 48 and 48 * 15 == 720
assert 3 * 4 / 2 == 6 and 6 * 10 == 60 and 2 * 6 == 12 and 3 + 4 + 5 == 12 and 12 * 10 == 120 and 120 + 12 == 132 and 3 ** 2 + 4 ** 2 == 5 ** 2
assert PI * 1 ** 2 == 3 and abs(3 * 1.2 - 3.6) < 1e-9 and round(3.6 * 1000) == 3600 and round(PI * 2 ** 2 * 1.2 * 1000) == 14400 and 14400 == 4 * 3600
assert 4 * 2 * 0.5 == 4 and 4 * 1000 / 40 == 100 and 100 == 60 + 40


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




# ================= peças desta aula =================
def situacao(c, t, t0, n):
    """situação n de 4, com quatro pontos de progresso (como na MAT-ANG-019)"""
    s = f"situação {n} de 4"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(4):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def rotulo_lata(c, t, x, y, w, h, r, pw=1.0, a=1.0, tampas=1.0, cor_r=None, cor_t=None):
    """o molde da lata (de MAT-ESP-002): retângulo w x h e as duas tampas de raio r encostadas no lado de cima e no de baixo"""
    if a <= 0:
        return
    cx = x + w * 0.16
    for cy in (y - r, y + h + r):
        if tampas > 0:
            k = ease_back(min(1, tampas))
            c.drawCircle(cx, cy, r * k, M.paint(cor_t or E.mix(E.COR, "#FFFFFF", 0.78), a))
            c.drawCircle(cx, cy, r * k, M.paint(TINTA, a, stroke=5))
    if pw > 0:
        ww = w * ease_io(pw)
        c.drawRect(skia.Rect.MakeXYWH(x, y, ww, h), M.paint(cor_r or E.mix(E.COR, "#FFFFFF", 0.65), a))
        c.drawRect(skia.Rect.MakeXYWH(x, y, ww, h), M.paint(TINTA, a, stroke=5))


def marca(c, t, t0, x, y0, y1, rot, cor=None, size=52, a=1.0):
    """cota vertical de y0 (embaixo) até y1 (em cima), com a medida à direita"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    yy = lerp(y0, y1, p)
    M.line(c, x, y0, x, yy, cor, a, 5)
    for y_ in (y0, yy):
        M.line(c, x - 14, y_, x + 14, y_, cor, a, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda q: E.escreve(c, rot, x + 26, (y0 + y1) / 2 + size * 0.36, size, "g", cor, q * a))


def torneira(c, t, t0, x, y, y_fim, vazao=None, a=1.0):
    """a bomba/torneira com a boca em (x, y) e o fio d'água caindo até y_fim; vazao = texto da pílula"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    M.rrect(c, x - 150, y - 46, 160, 30, 8, E.mix(TINTA2, "#FFFFFF", 0.3), q)
    M.rrect(c, x - 16, y - 46, 32, 46, 6, E.mix(TINTA2, "#FFFFFF", 0.3), q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 150, y - 46, 160, 30), 8, 8), M.paint(TINTA, q, stroke=3))
    f = ease_io(prog(t, t0 + 0.3, 0.5))
    if f > 0:
        c.drawRect(skia.Rect.MakeXYWH(x - 7, y, 14, (y_fim - y) * f), M.paint(E.mix(E.COR, "#FFFFFF", 0.35), 0.8 * q))
    if vazao:
        E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.pilula(c, vazao, x - 330, y - 30, 50, "g", a=b * a, cor=E.SOBRE))


def molde_345(s, L):
    """o prisma de base 3-4-5: retângulos 3, 4 e 5 (x L) lado a lado, o de 4 no chão, e um triângulo retângulo em cada ponta.
    O de 3 fica em pé (o ângulo reto); o de 5 é a hipotenusa e dobra até encostar no alto do de 3"""
    gr = 180 - math.degrees(math.atan2(3, 4))
    F = {"r1": ret(-5 * s, -L / 2, 3 * s, L), "r2": ret(-2 * s, -L / 2, 4 * s, L), "r3": ret(2 * s, -L / 2, 5 * s, L),
         "t1": [(-2 * s, -L / 2), (2 * s, -L / 2), (-2 * s, -L / 2 - 3 * s)], "t2": [(2 * s, L / 2), (-2 * s, L / 2), (-2 * s, L / 2 + 3 * s)]}
    P = {"r1": ("r2", 1, 90), "r3": ("r2", 3, gr), "t1": ("r2", 0, 90), "t2": ("r2", 0, 90)}
    return Molde(F, P)


MS, ML = 40, 400
M345 = molde_345(MS, ML)
OX, OY = 470, 560


def rotulos_345(c, t, ts, a=1.0):
    """as medidas do molde aberto: 3, 4 e 5 no triângulo de cima e 10 na altura dos retângulos (ts = instante de cada uma)"""
    s, L = MS, ML
    pos = ((ts[0], "3", OX - 2 * s - 34, OY - L / 2 - 1.5 * s + 18, "right"), (ts[1], "4", OX, OY - L / 2 + 44, "center"),
           (ts[2], "5", OX + 0.3 * s, OY - L / 2 - 1.9 * s, "left"), (ts[3], "10", OX + 7 * s + 20, OY + 18, "left"))
    for t0, s_, x, y, al in pos:
        if t0 is None:
            continue
        E.foco(c, t, t0, 0.4, lambda q, s_=s_, x=x, y=y, al=al: E.formula(c, s_, x, y, 50, "g", COR, q * a, al))


def pergunta(c, t, linhas, X=1350, y0=230, dy=100):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * dy, "center", 0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.frase(c, t, a1, [("4 situações", "g", 96, COR)], W / 2, 240, "center", 0.1)
    E.frase(c, t, a1 + 0.8, ps("com latas, caixas e reservatórios", "i", 64), W / 2, 340, "center", 0.1)
    xs = (330, 750, 1170, 1590)
    for k, x in enumerate(xs):
        tk = a1 + 1.4 + 0.35 * k
        E.foco(c, t, tk, 0.4, lambda q, k=k, x=x: (E.bola(c, x, 470, 34, a=q), centro(c, str(k + 1), x, 490, 46, "g", E.SOBRE, q)))
    rotulo_lata(c, t, 230, 620, 200, 110, 34, pw=prog(t, a1 + 1.4, 0.6), a=ep(t, a1 + 1.4, 0.3))
    alfa_on = ep(t, a1 + 1.75, 0.4)
    if alfa_on > 0:
        M345.desenha(c, t, 0, 0, 750, 690, alfa_on, zoom=0.4)
    E.cilindro(c, t, a1 + 2.1, 1170, 790, 110, 180)
    E.paralelepipedo(c, t, a1 + 2.45, 1460, 790, 230, 150, 140)
    agua(c, 1460, 790, 230, 150, 140, 0.4 * ease_io(prog(t, a1 + 3.0, 1.0)))
    E.foco(c, t, b1, 0.5, lambda q: E.pilula(c, "pause e resolva antes da resposta", W / 2, 960, 56, "g", a=q, cor=E.SOBRE))
    E.frase(c, t, lerp(b1, C["s01.end"], 0.6), ps("errar aqui não custa nada", "i", 52, TINTA2), W / 2, 1050, "center", 0.1)


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02"] + 0.6, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02"] + 0.75, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w = 960, 840
    itens = (("s02.a", "molde ou vista:", "descubra o sólido"), ("s02.b", "volume =", "área da base × altura"),
             ("s02.c", "área total =", "soma das faces"), ("s02.d", "1 m³ guarda", "1.000 litros"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 120 + i * 205
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 175, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 54), x + 40, y + 70, "left", 0.1)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 56, COR)], x + 40, y + 142)
    alvo = [120 + i * 205 + 150 for i in range(4)]
    ks = ("s02.b", "s02.c", "s02.d")
    yc = alvo[0]
    for j, k in enumerate(ks):
        yc = lerp(yc, alvo[j + 1], ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, yc, ep(t, C["s02.a"], 0.4))
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.7), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), x, 1010, "left", 0.12)


# ---------------- situação 1: o molde da lata ----------------
LX1, LY1, LW1, LH1, LR1 = 160, 470, 480, 300, 80   # retângulo 24 x 15 (20 px por cm) e tampas de raio 4


def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    situacao(c, t, a3, 1)
    rotulo_lata(c, t, LX1, LY1, LW1, LH1, LR1, pw=prog(t, c3, 0.8), a=1.0, tampas=ep(t, b3, 0.5))
    E.foco(c, t, c3 + 0.6, 0.4, lambda q: centro(c, "24 cm", LX1 + LW1 * 0.62, LY1 - 20, 52, "g", COR, q))
    E.foco(c, t, c3 + 0.9, 0.4, lambda q: E.escreve(c, "15 cm", LX1 + LW1 + 20, LY1 + LH1 / 2 + 18, 52, "g", COR, q))
    pergunta(c, t, [(b3, ps("molde:", "i", 60) + [("2 círculos iguais", "g", 60, COR)]),
                    (c3, ps("+", "i", 60) + [("retângulo 24 × 15 cm", "g", 60, COR)]),
                    (lerp(c3, d3, 0.6), ps("os círculos encostam no lado de 24", "i", 48, TINTA2)),
                    (d3, ps("que", "i", 60) + [("sólido?", "g", 64, COR)]),
                    (d3 + 1.2, ps("quantos", "i", 60) + [("mL", "g", 64, COR)] + ps("cabem?", "i", 60)),
                    (d3 + 2.6, [("π = 3", "g", 60, COR)])], X=1350, y0=200, dy=90)
    E.relogio(c, t, C["s04.a"], 1350, 840, 105)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    situacao(c, t, C["s05"], 1)
    rotulo_lata(c, t, LX1, LY1, LW1, LH1, LR1, a=1.0, cor_t=E.mix(E.COR, "#FFFFFF", 0.45) if t >= a5 else None)
    centro(c, "24 cm", LX1 + LW1 * 0.62, LY1 - 20, 52, "g", COR)
    E.escreve(c, "15 cm", LX1 + LW1 + 20, LY1 + LH1 / 2 + 18, 52, "g", COR)
    if t >= b5:
        aresta(c, t, b5, (LX1, LY1), (LX1 + LW1, LY1), largura=12)
    if t >= e5:
        aresta(c, t, e5, (LX1 + LW1, LY1), (LX1 + LW1, LY1 + LH1), largura=12)
    if t >= d5:
        cx = LX1 + LW1 * 0.16
        cy = LY1 + LH1 + LR1
        M.line(c, cx, cy, cx + LR1, cy, TINTA, 1, 5, progress=ease_io(prog(t, d5, 0.4)))
        E.foco(c, t, d5 + 0.3, 0.4, lambda q: centro(c, "4", cx + LR1 / 2, cy - 12, 44, "g", COR, q))
    X = 1360

    def raio():
        E.frase(c, t, a5, ps("monta um", "i", 62) + [("cilindro", "g", 66, COR)], X, 220, "center", 0.1)
        E.frase(c, t, b5, ps("o lado de 24 dá a volta:", "i", 56) + [("2πr", "g", 62, COR)], X, 340, "center", 0.1)
        fcen(c, t, c5, "2 × 3 × r = 6r = 24", X, 480, 70)
        fcen(c, t, d5, "r = 4", X - 200, 620, 80, COR)
        fcen(c, t, e5, "h = 15", X + 200, 620, 80, COR)
        E.cilindro(c, t, a5 + 0.3, X, 960, 120, 225)
    fase(c, t, C["s05"], C["s06"] - 0.1, raio)
    if t < C["s06"] - 0.1:
        return
    fcen(c, t, a6, "3 × 4² = 48", X, 240, 76)
    fcen(c, t, b6, "48 × 15 = 720 cm³", X, 380, 76)
    bola_txt(c, t, c6, "720 mL", X, 560, 120, 62)
    fcen(c, t, d6, "r = 24", X - 220, 820, 72, ERRADO)
    if t >= d6 + 0.6:
        E.risco(c, X - 360, 835, X - 80, 775, t, d6 + 0.6, largura=10)
    E.frase(c, t, d6 + 1.2, ps("24 é a", "i", 56) + [("volta inteira", "g", 58, COR)], X + 230, 815, "center", 0.1)


# ---------------- situação 2: o molde do prisma ----------------
def b_questao2(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    situacao(c, t, a7, 2)
    ta = {"t1": b7, "t2": b7 + 0.3, "r1": c7, "r2": c7 + 0.2, "r3": c7 + 0.4}
    M345.desenha(c, t, 0, 0, OX, OY, 1.0, ta=ta)
    rotulos_345(c, t, (b7 + 0.8, b7 + 1.0, b7 + 1.2, c7 + 0.8))
    pergunta(c, t, [(b7, [("2 triângulos retângulos", "g", 56, COR)]),
                    (b7 + 1.0, ps("catetos 3 e 4, hipotenusa 5", "i", 52)),
                    (c7, [("3 retângulos", "g", 56, COR)] + ps("de altura 10", "i", 54)),
                    (d7, [("1)", "g", 58, COR)] + ps("volume da peça?", "i", 58)),
                    (e7, [("2)", "g", 58, COR)] + ps("quanto papel?", "i", 58))], X=1360, y0=230, dy=100)
    E.relogio(c, t, C["s08.a"], 1360, 840, 105)


def b_resposta2(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    situacao(c, t, C["s09"], 2)
    X = 1360
    monta = ease_io(prog(t, a9, 1.6)) * (1 - ease_io(prog(t, C["s10"], 1.2)))
    cores = {"t1": E.COR, "t2": E.COR, "r1": CINZA2, "r2": CINZA2, "r3": CINZA2}
    nums = {"t1": "6", "t2": "6", "r1": "3 × 10", "r2": "4 × 10", "r3": "5 × 10"}
    tn = {"t1": a0, "t2": a0 + 0.3, "r1": c0, "r2": c0 + 0.3, "r3": c0 + 0.6}
    cont = {"t1": ERRADO, "t2": ERRADO} if t >= c1 else None
    M345.desenha(c, t, monta, monta, OX, lerp(OY, 700, monta), 1.0, cores=cores, contornos=cont, nums=nums if t >= C["s10"] else None,
                 tn=tn, size=36)
    if t < a9 + 0.2 or t >= C["s10"] + 1.2:
        rotulos_345(c, t, (C["s09"], C["s09"], C["s09"], C["s09"]), a=1 - ep(t, a9, 0.2) if t < C["s10"] else ep(t, C["s10"] + 1.2, 0.4))

    def volume():
        E.frase(c, t, a9, ps("é um", "i", 62) + [("prisma triangular", "g", 66, COR)], X, 220, "center", 0.1)
        E.frase(c, t, lerp(a9, b9, 0.5), ps("catetos = base e altura", "i", 54, TINTA2), X, 330, "center", 0.1)
        fcen(c, t, b9, "f{3 × 4}{2} = 6 cm²", X, 480, 76)
        fcen(c, t, c9, "6 × 10", X - 200, 700, 80)
        bola_txt(c, t, c9 + 0.6, "60 cm³", X + 200, 680, 120, 56)
    fase(c, t, C["s09"], C["s10"] - 0.1, volume)

    def papel():
        fcen(c, t, a0, "2 bases: 2 × 6 = 12", X, 220, 64, COR)
        E.frase(c, t, b0, ps("retângulos:", "i", 56) + [("perímetro × altura", "g", 58)], X, 350, "center", 0.1)
        fcen(c, t, c0, "3 + 4 + 5 = 12", X, 470, 68)
        fcen(c, t, d0, "12 × 10 = 120", X, 590, 68)
        fcen(c, t, e0, "120 + 12", X - 200, 790, 76)
        bola_txt(c, t, e0 + 0.6, "132 cm²", X + 200, 780, 125, 52)
    fase(c, t, C["s10"], C["s11"] - 0.1, papel)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, ps("os 3 retângulos têm a", "i", 56) + [("mesma altura", "g", 58, COR)], X, 230, "center", 0.1)
    s, h = 26, 260
    x0 = X - 12 * s / 2
    for k, (wq, n) in enumerate(((3, "3"), (4, "4"), (5, "5"))):
        q = ep(t, a1 + 0.4 + 0.2 * k, 0.4)
        if q > 0:
            xx = x0 + sum((3, 4, 5)[:k]) * s
            c.drawRect(skia.Rect.MakeXYWH(xx, 320, wq * s, h), M.paint(CINZA2, q))
            c.drawRect(skia.Rect.MakeXYWH(xx, 320, wq * s, h), M.paint(TINTA, q, stroke=4))
            centro(c, n, xx + wq * s / 2, 320 + h + 50, 46, "g", TINTA, q)
    E.frase(c, t, a1 + 1.4, ps("lado a lado:", "i", 54) + [("um retângulo só", "g", 56)], X, 720, "center", 0.1)
    E.frase(c, t, b1, ps("mas deixa", "i", 58) + [("as bases de fora", "g", 60, ERRADO)], X, 850, "center", 0.1)
    E.frase(c, t, c1, ps("parar no 120 =", "i", 56) + [("esquecer os 2 triângulos", "g", 56, ERRADO)], X, 960, "center", 0.1)


# ---------------- situação 3: as vistas ----------------
def vistas(c, t, t1, t2, a=1.0, dx=0.0):
    """de cima, o círculo de 2 m de diâmetro; de frente, o retângulo de 1,2 m de altura (100 px por metro... ×1,7)"""
    k = 170
    cx, cy = 360 + dx, 420
    q1 = ep(t, t1, 0.5) * a
    if q1 > 0:
        c.drawCircle(cx, cy, k * ease_back(min(1, prog(t, t1, 0.5))), M.paint(E.mix(E.COR, "#FFFFFF", 0.78), q1))
        c.drawCircle(cx, cy, k, M.paint(TINTA, q1, stroke=5))
        M.line(c, cx - k, cy, cx + k, cy, E.COR, q1, 6)
        centro(c, "2 m", cx, cy - 18, 52, "g", COR, q1)
        centro(c, "de cima", cx, cy + k + 60, 50, "i", TINTA2, q1)
    q2 = ep(t, t2, 0.5) * a
    if q2 > 0:
        x, y, w, h = cx - k, 720, 2 * k, 1.2 * k
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.mix(E.COR, "#FFFFFF", 0.78), q2))
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, q2, stroke=5))
        E.escreve(c, "1,2 m", x + w + 20, y + h / 2 + 18, 52, "g", COR, q2)
        centro(c, "de frente", cx, y + h + 60, 50, "i", TINTA2, q2)


def b_questao3(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    situacao(c, t, a2, 3)
    vistas(c, t, b2, c2)
    pergunta(c, t, [(a2 + 0.3, ps("uma", "i", 60) + [("caixa-d'água", "g", 64, COR)]),
                    (b2, ps("de cima: círculo de", "i", 56) + [("2 m de diâmetro", "g", 58, COR)]),
                    (c2, ps("de frente: retângulo de", "i", 56) + [("1,2 m", "g", 58, COR)]),
                    (d2, ps("quantos", "i", 62) + [("litros?", "g", 66, COR)]),
                    (d2 + 1.0, [("π = 3", "g", 60, COR)])], X=1300, y0=230, dy=100)
    E.relogio(c, t, C["s13.a"], 1300, 840, 105)


def b_resposta3(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    situacao(c, t, C["s14"], 3)
    E.saida(c, t, a4, lambda: vistas(c, t, -9, -9))
    cx, cy, r, h = 400, 900, 200, 240
    E.cilindro(c, t, a4, cx, cy, r, h, None, "1,2 m", size=52)
    if t >= b4:
        ct = cy - h * COS
        M.line(c, cx, ct, cx + r, ct, E.COR, 1, 8, progress=ease_io(prog(t, b4, 0.4)))
        E.foco(c, t, b4 + 0.3, 0.4, lambda q: centro(c, "1 m", cx + r / 2, ct - 18, 50, "g", COR, q))
    X = 1320
    E.frase(c, t, a4, ps("um", "i", 62) + [("cilindro em pé", "g", 66, COR)], X, 200, "center", 0.1)

    def certo():
        fcen(c, t, b4, "diâmetro 2 → raio 1", X, 330, 64)
        fcen(c, t, c4, "3 × 1² = 3 m²", X, 450, 68)
        fcen(c, t, d4, "3 × 1,2 = 3,6 m³", X, 570, 68)
        fcen(c, t, e4, "3,6 × 1.000", X - 200, 760, 70)
        bola_txt(c, t, e4 + 0.6, "3.600 L", X + 220, 750, 130, 52)
    fase(c, t, C["s14"], C["s15"] - 0.1, certo)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("com o diâmetro como raio:", "i", 58), X, 330, "center", 0.1)
    fcen(c, t, a5, "3 × 2² × 1,2 → 4 vezes", X, 460, 64, ERRADO)
    fcen(c, t, b5, "14.400 L", X, 600, 84, ERRADO)
    if t >= b5 + 0.6:
        E.risco(c, X - 190, 615, X + 190, 555, t, b5 + 0.6, largura=10)
    E.foco(c, t, c5, 0.5, lambda q: E.pilula(c, "raio = metade do diâmetro", X, 780, 60, "g", a=q, cor=E.SOBRE))


# ---------------- situação 4: o reservatório ----------------
RX, RY, RW, RD, RH = 240, 900, 520, 260, 300   # o reservatório: fundo 4 m x 2 m (130 px por metro), altura 2,3 m de desenho


def reservatorio(c, t, t0, tl=None, tm=None):
    E.paralelepipedo(c, t, t0, RX, RY, RW, RD, RH)
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda q: centro(c, "4 m", RX + RW / 2, RY + 64, 52, "g", COR, q))
        E.foco(c, t, (tm or tl) + 0.3, 0.4, lambda q: E.escreve(c, "2 m", RX + RW + KX * RD / 2 + 24, RY + KY * RD / 2 + 30, 52, "g", COR, q))


def b_questao4(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    situacao(c, t, a6, 4)
    reservatorio(c, t, a6, b6)
    torneira(c, t, c6, RX + RW / 2 + KX * RD / 2, 260, RY + KY * RD / 2, "40 L/min")
    if t >= d6:
        marca(c, t, d6 + 0.4, RX + RW + KX * RD + 40, RY + KY * RD, RY + KY * RD - 65, "50 cm", size=48)
    pergunta(c, t, [(a6 + 0.3, ps("reservatório em", "i", 60) + [("bloco", "g", 64, COR)]),
                    (b6, ps("fundo:", "i", 58) + [("4 m × 2 m", "g", 60, COR)]),
                    (c6, ps("bomba:", "i", 58) + [("40 L por minuto", "g", 60, COR)]),
                    (d6, ps("quanto tempo para o nível", "i", 56)),
                    (d6 + 1.0, ps("subir", "i", 60) + [("50 cm?", "g", 64, COR)])], X=1380, y0=230, dy=100)
    E.relogio(c, t, C["s17.a"], 1380, 840, 105)


def b_resposta4(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    situacao(c, t, C["s18"], 4)
    reservatorio(c, t, C["s18"] - 2, C["s18"] - 2)
    agua(c, RX, RY, RW, RD, RH, (65 / RH) * ease_io(prog(t, a8, 1.2)))
    if t >= b8:
        marca(c, t, b8, RX + RW + KX * RD + 40, RY + KY * RD, RY + KY * RD - 65, "0,5 m", size=48)
    X = 1380

    def volume():
        E.frase(c, t, a8, ps("a água forma uma", "i", 58) + [("camada em bloco", "g", 62, COR)], X, 220, "center", 0.1)
        fcen(c, t, b8, "50 cm = 0,5 m", X, 360, 70)
        fcen(c, t, c8, "4 × 2 × 0,5 = 4 m³", X, 500, 70)
        fcen(c, t, d8, "= 4.000 L", X, 640, 76, COR)
    fase(c, t, C["s18"], C["s19"] - 0.1, volume)
    if t < C["s19"] - 0.1:
        return
    fcen(c, t, a9, "4.000 ÷ 40 = 100 min", X, 230, 70)
    fcen(c, t, b9, "100 min = 60 + 40", X, 360, 70, TINTA2)
    bola_txt(c, t, c9, "1 h 40 min", X, 560, 140, 50)
    fcen(c, t, d9, "1,4 h", X, 810, 76, ERRADO)
    if t >= d9 + 0.5:
        E.risco(c, X - 110, 825, X + 110, 765, t, d9 + 0.5, largura=10)
    E.frase(c, t, d9 + 1.0, ps("o tempo anda de", "i", 54) + [("60 em 60", "g", 58, COR)], X, 930, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", ps("descubra o sólido pelo", "i", 62) + [("molde ou pela vista", "g", 62, COR)]),
                 ("s20.b", ps("ache o", "i", 62) + [("raio e a altura certos", "g", 62, COR)]),
                 ("s20.c", [("confira a unidade", "g", 62, COR)] + ps("antes de responder", "i", 62)))
        for i, (k, l1) in enumerate(itens):
            y = 400 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a1, [("Pirâmide", "g", 130, COR)], XE, 420)
    E.frase(c, t, b1, ps("o volume é", "i", 64) + [("1/3", "g", 70, COR)] + ps("do prisma", "i", 64), XE, 540, passo=0.1)
    E.frase(c, t, b1 + 1.0, ps("de mesma base e mesma altura", "i", 58), XE, 640, passo=0.1)
    E.prisma(c, t, b1 + 0.3, 1250, 820, 4, 140, 260)
    E.piramide(c, t, a1, 1600, 820, 4, 140, 260)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1040, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
