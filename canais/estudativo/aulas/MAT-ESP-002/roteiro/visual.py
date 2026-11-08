"""Visual — Estudativo · MAT-ESP-002: planificações, montar e desmontar sólidos.
Mesma linguagem da MAT-ESP-001 (sólidos do kit, elemento da vez na cor da matéria, a 2ª família em cinza, resposta na esfera).

PEÇA NOVA DA TRILHA: Molde, a planificação que DOBRA DE VERDADE (as próximas aulas copiam a classe daqui).
- O molde fica deitado no chão. faces = {nome: [(u, w), ...]} em px, u para a direita e w para baixo, como se desenha no papel.
  pais = {nome: (pai, i, graus)}: a face gira na sua aresta i (de pts[i] a pts[i+1]), que é a mesma aresta do pai.
- dobra = 0 (aberto) a 1 (montado), um número ou um dict por face: a faixa dobra antes das abas, por exemplo.
- A câmera camera(k) vai do molde visto de cima (k = 0: o desenho do papel, sem distorção) até o sólido de cima e de lado (k = 1).
- As faces são de papel (opacas, sombreadas pela luz) e o número de cada uma fica no centro dela. Cores da vez: cores = {face: cor}
  (a 1ª família em COR, a 2ª em CINZA2 = TINTA2 clareado, porque a face é opaca) e contornos = {face: cor} para a 3ª.
Outras peças locais: rotulo_lata() (o retângulo do rótulo com as tampas), leque() (setor do cone), quadrados() (fila do atalho).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-002_planificacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("molde", "cubo", "cilindro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
PI = 3
assert 2 * PI * 3 == 18 and 18 == 3 * 6 and 2 * PI * 5 == 30 and 3 * 10 == 30 and 90 + 90 == 180


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


# ================= Molde: a planificação que dobra =================
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


def cruz_cubo(s):
    """o molde em cruz: faixa 1 a 4 em pé (1 em cima), aba 5 à esquerda do 2 e aba 6 à direita do 2. A face 2 é o chão"""
    h = s / 2
    F = {"1": ret(-h, -h - s, s, s), "2": ret(-h, -h, s, s), "3": ret(-h, h, s, s), "4": ret(-h, h + s, s, s),
         "5": ret(-h - s, -h, s, s), "6": ret(h, -h, s, s)}
    P = {"1": ("2", 2, 90), "3": ("2", 0, 90), "4": ("3", 0, 90), "5": ("2", 1, 90), "6": ("2", 3, 90)}
    return Molde(F, P)


def molde_questao(s):
    """o molde da questão: faixa 1 a 4 em pé, aba 5 à esquerda do 1 e aba 6 à direita do 3"""
    h = s / 2
    F = {"1": ret(-h, -h - s, s, s), "2": ret(-h, -h, s, s), "3": ret(-h, h, s, s), "4": ret(-h, h + s, s, s),
         "5": ret(-h - s, -h - s, s, s), "6": ret(h, h, s, s)}
    P = {"1": ("2", 2, 90), "3": ("2", 0, 90), "4": ("3", 0, 90), "5": ("1", 1, 90), "6": ("3", 3, 90)}
    return Molde(F, P)


def caixa_sapato(a, b, h):
    """a caixa: fundo a x b no chão; frente e trás a x h; tampa presa atrás; lados h x b"""
    F = {"fundo": ret(-a / 2, -b / 2, a, b), "frente": ret(-a / 2, b / 2, a, h), "tras": ret(-a / 2, -b / 2 - h, a, h),
         "tampa": ret(-a / 2, -b / 2 - h - b, a, b), "esq": ret(-a / 2 - h, -b / 2, h, b), "dir": ret(a / 2, -b / 2, h, b)}
    P = {"frente": ("fundo", 0, 90), "tras": ("fundo", 2, 90), "tampa": ("tras", 2, 90), "esq": ("fundo", 1, 90), "dir": ("fundo", 3, 90)}
    return Molde(F, P)


def prisma_tri(s, L):
    """prisma de base triangular: três retângulos s x L lado a lado e um triângulo em cada ponta do do meio"""
    hh = s * math.sqrt(3) / 2
    F = {"r1": ret(-1.5 * s, -L / 2, s, L), "r2": ret(-s / 2, -L / 2, s, L), "r3": ret(s / 2, -L / 2, s, L),
         "t1": [(-s / 2, -L / 2), (s / 2, -L / 2), (0, -L / 2 - hh)], "t2": [(s / 2, L / 2), (-s / 2, L / 2), (0, L / 2 + hh)]}
    P = {"r1": ("r2", 1, 120), "r3": ("r2", 3, 120), "t1": ("r2", 0, 90), "t2": ("r2", 0, 90)}
    return Molde(F, P)


def piramide_q(s, hl):
    """pirâmide quadrangular: quadrado s x s e um triângulo de altura hl em cada lado; dobra até as pontas se encontrarem"""
    h = s / 2
    gr = 180 - math.degrees(math.acos(h / hl))  # gira mais de 90°: a ponta passa para dentro
    F = {"base": ret(-h, -h, s, s),
         "a": [(-h, -h), (h, -h), (0, -h - hl)], "b": [(h, -h), (h, h), (h + hl, 0)],
         "c": [(h, h), (-h, h), (0, h + hl)], "d": [(-h, h), (-h, -h), (-h - hl, 0)]}
    P = {k: ("base", 0, gr) for k in "abcd"}
    return Molde(F, P)


CRUZ = cruz_cubo(170)
QUEST = molde_questao(130)
CAIXA = caixa_sapato(340, 210, 150)
PTRI = prisma_tri(210, 340)
PIRQ = piramide_q(240, 240)


def rotulo_lata(c, t, x, y, w, h, r, pw=1.0, a=1.0, cor=None, tampas=1.0, cor_r=None):
    """o rótulo da lata: retângulo w x h que se desenrola da esquerda (pw = 0..1) e as duas tampas de raio r, em cima e embaixo"""
    if a <= 0:
        return
    cx = x + w * 0.16
    for cy in (y - r, y + h + r):
        if tampas > 0:
            k = ease_back(min(1, tampas))
            c.drawCircle(cx, cy, r * k, M.paint(E.mix(E.COR, "#FFFFFF", 0.78), a))
            c.drawCircle(cx, cy, r * k, M.paint(TINTA, a, stroke=5))
    if pw > 0:
        ww = w * ease_io(pw)
        c.drawRect(skia.Rect.MakeXYWH(x, y, ww, h), M.paint(cor_r or E.mix(E.COR, "#FFFFFF", 0.65), a))
        c.drawRect(skia.Rect.MakeXYWH(x, y, ww, h), M.paint(TINTA, a, stroke=5))


def leque(c, cx, cy, R, ini, varre, a=1.0, cor=None, p=1.0):
    """setor de círculo (a lateral do cone aberta): ângulos da tela, em graus"""
    if a <= 0 or p <= 0:
        return
    path = skia.Path()
    path.moveTo(cx, cy)
    path.arcTo(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), ini, varre * ease_io(p), False)
    path.close()
    c.drawPath(path, M.paint(cor or E.mix(E.COR, "#FFFFFF", 0.65), a))
    c.drawPath(path, M.paint(TINTA, a, stroke=5))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        abre = ease_io(prog(t, a1 + 0.8, max(1.0, b1 - a1 - 0.8)))
        k = 1 - abre
        E.foco(c, t, a1, 0.6, lambda q: CAIXA.desenha(c, t, 1 - abre, k, 560, lerp(600, 760, k), q,
                                                     cores={"frente": E.COR, "tras": CINZA2} if t >= d1 else None))
        E.frase(c, t, a1 + 0.2, ps("desmonte uma", "i", 76) + [("caixa", "g", 80, COR)], 1050, 260, "left", 0.12)
        E.frase(c, t, b1, [("figura plana", "g", 80, COR)], 1050, 400, "left", 0.12)
        E.frase(c, t, b1 + 0.6, ps("feita de retângulos", "i", 70), 1050, 490, "left", 0.12)
        E.frase(c, t, c1, ps("que", "i", 84) + [("sólido", "g", 88, COR)] + ps("ela monta?", "i", 84), 1050, 680, "left", 0.12)
        E.frase(c, t, d1, ps("qual face fica", "i", 70), 1050, 830, "left", 0.12)
        E.frase(c, t, d1 + 0.5, ps("de frente para qual?", "i", 70), 1050, 920, "left", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("montar", "g", 110, COR)] + ps("e", "i", 100), XE, 500, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), [("desmontar", "g", 110, COR)], XE, 630, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("sólidos de cabeça", "i", 90), XE, 760, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "do cubo", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 880
    itens = (("s03.b", "prisma: 2 bases + retângulos", "pirâmide: 1 base + triângulos"), ("s03.c", "a volta da circunferência:", "C = 2πr"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 54 if i == 0 else 70, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 680, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 940, "left", 0.12)


# ---------------- o que é planificação ----------------
def b_molde(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6 = C["s06.a"], C["s06.b"]
    X = 1080

    def caixa():
        abre = ease_io(prog(t, b4, 1.6))
        k = 1 - abre
        nomes = ("frente", "tampa", "dir", "tras", "esq", "fundo")
        pisca = {n: math.sin(math.pi * min(1, prog(t, c4 + 0.35 * i, 0.7))) for i, n in enumerate(nomes)} if t >= c4 else None
        CAIXA.desenha(c, t, 1 - abre, k, 560, lerp(640, 760, k), ep(t, C["s04"], 0.5), pisca=pisca)
        E.frase(c, t, a4, [("planificação:", "g", 84, COR)], X, 290)
        E.frase(c, t, a4 + 0.6, ps("o sólido aberto no plano", "i", 66), X, 380, "left", 0.1)
        E.frase(c, t, b4, ps("o molde que você", "i", 66), X, 530, "left", 0.1)
        E.frase(c, t, b4 + 0.6, [("recorta, dobra e cola", "g", 62)], X, 620, "left", 0.1)
        E.frase(c, t, c4, ps("cada face vira", "i", 66) + [("uma figura", "g", 66, COR)], X, 780, "left", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, caixa)

    def prisma():
        monta = ease_io(prog(t, c5 + 0.3, 1.8))
        cores = {"t1": E.COR, "t2": E.COR} if t >= b5 else None
        ta = {n: a5 + 0.15 * i for i, n in enumerate(("r2", "r1", "r3", "t1", "t2"))}
        PTRI.desenha(c, t, monta, monta, 560, lerp(560, 700, monta), ta=ta, cores=cores)
        E.frase(c, t, a5, ps("olhe as", "i", 76) + [("formas", "g", 80, COR)], X, 260, "left", 0.12)
        E.frase(c, t, b5, [("2 figuras iguais", "g", 66, COR)], X, 400, "left", 0.1)
        E.frase(c, t, b5 + 0.6, ps("+ retângulos =", "i", 66) + [("prisma", "g", 66)], X, 490, "left", 0.1)
        E.frase(c, t, lerp(b5, c5, 0.55), ps("as iguais são as", "i", 60, TINTA2) + [("bases", "g", 60, COR)], X, 590, "left", 0.1)
        E.frase(c, t, c5, ps("2 triângulos + 3 retângulos", "i", 60), X, 750, "left", 0.1)
        E.frase(c, t, c5 + 0.8, [("prisma de base triangular", "g", 60, COR)], X, 840, "left", 0.1)
    fase(c, t, C["s05"], C["s06"] - 0.1, prisma)
    if t < C["s06"] - 0.1:
        return
    fecha = ease_io(prog(t, lerp(a6, b6, 0.45), 1.8))
    ta = {n: a6 + 0.15 * i for i, n in enumerate(("base", "a", "b", "c", "d"))}
    PIRQ.desenha(c, t, fecha, fecha, 560, lerp(560, 720, fecha), ta=ta, cores={"base": E.COR} if t >= b6 else None)
    E.frase(c, t, a6, [("1 figura só", "g", 70, COR)], X, 280, "left", 0.1)
    E.frase(c, t, a6 + 0.6, ps("cercada de", "i", 66) + [("triângulos", "g", 66)], X, 370, "left", 0.1)
    E.frase(c, t, lerp(a6, b6, 0.45), ps("que se encontram num ponto", "i", 60, TINTA2), X, 460, "left", 0.1)
    E.frase(c, t, lerp(a6, b6, 0.75), ps("=", "i", 70) + [("pirâmide", "g", 76, COR)], X, 570, "left", 0.1)
    E.frase(c, t, b6, ps("quadrado + 4 triângulos", "i", 60), X, 740, "left", 0.1)
    E.frase(c, t, b6 + 0.8, [("pirâmide quadrangular", "g", 60, COR)], X, 830, "left", 0.1)


# ---------------- o cubo ----------------
ORDEM_CRUZ = ("1", "2", "3", "4", "5", "6")
OX, OY = 560, 470


def b_cubo(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    X = 1080

    def monta():
        faixa = ease_io(prog(t, d7 + 0.2, 1.8))
        abas = ease_io(prog(t, e7 + 0.2, 1.4))
        dobra = {"1": faixa, "3": faixa, "4": faixa, "5": abas, "6": abas}
        cam = ease_io(prog(t, d7, 1.2))
        cores = {}
        if b7 <= t < d7:
            cores.update({n: E.COR for n in "1234"})
        if c7 <= t < d7:
            cores.update({"5": CINZA2, "6": CINZA2})
        ta = {n: a7 + 0.12 * i for i, n in enumerate(ORDEM_CRUZ)}
        fase(c, t, C["s07"], a7 - 0.2, lambda: E.cubo(c, t, C["s07"], OX - 170, 760, 300))
        CRUZ.desenha(c, t, dobra, cam, OX, lerp(OY, 690, cam), ta=ta, cores=cores or None)
        E.frase(c, t, C["s07"] + 0.2, ps("o cubo:", "i", 70) + [("6 quadrados", "g", 70)], X, 230, "left", 0.1)
        E.frase(c, t, a7, ps("o molde em", "i", 76) + [("cruz", "g", 84, COR)], X, 360, "left", 0.1)
        E.frase(c, t, b7, [("faixa", "g", 66, COR)] + ps("de 4 quadrados", "i", 64), X, 490, "left", 0.1)
        E.frase(c, t, c7, [("1 aba", "g", 66)] + ps("de cada lado", "i", 64), X, 580, "left", 0.1)
        E.frase(c, t, d7, ps("a faixa dá a volta:", "i", 64) + [("4 faces", "g", 66, COR)], X, 740, "left", 0.1)
        E.frase(c, t, e7, ps("as abas", "i", 64) + [("fecham as pontas", "g", 62)], X, 840, "left", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, monta)
    if t < C["s08"] - 0.1:
        return

    # de novo aberto: numerar e achar os pares
    cores, contornos = {}, {}
    if t >= b8:
        cores.update({"1": E.COR, "3": E.COR})
    if t >= c8:
        cores.update({"2": CINZA2, "4": CINZA2})
    if t >= e8:
        contornos.update({"5": E.COR, "6": E.COR})
    tn = {"1": a8, "2": a8 + 0.3, "3": a8 + 0.6, "4": a8 + 0.9, "5": d8, "6": d8 + 0.3}
    CRUZ.desenha(c, t, 0, 0, OX, OY, ep(t, C["s08"], 0.4), cores=cores, contornos=contornos, nums={n: n for n in ORDEM_CRUZ}, tn=tn, size=70)
    E.frase(c, t, C["s08"] + 0.2, ps("qual fica de", "i", 70) + [("frente?", "g", 74, COR)], X, 230, "left", 0.1)
    E.frase(c, t, a8, ps("numere a faixa de cima para baixo", "i", 52, TINTA2), X, 330, "left", 0.08)
    for i, (tk, s_, cor) in enumerate(((b8, "1 e 3", COR), (c8, "2 e 4", CINZA2), (e8, "5 e 6", COR))):
        y = 500 + 150 * i
        E.foco(c, t, tk, 0.5, lambda a, y=y, cor=cor, i=i: (E.bola(c, X + 50, y - 30, 42, cor, a) if i < 2 else
                                                            c.drawCircle(X + 50, y - 30, 38, M.paint(cor, a, stroke=10))))
        E.frase(c, t, tk, [(s_, "g", 84, cor)] + ps("de frente", "i", 66), X + 130, y, "left", 0.1)
    E.frase(c, t, d8, ps("abas: pontas opostas", "i", 56, TINTA2), X + 130, 870, "left", 0.1)


# ---------------- cilindro e cone ----------------
NX, NY, NW, NH, NR = 700, 380, 540, 300, 86   # rótulo: x, y, largura (2πr), altura e raio da tampa


def b_cilindro(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12, d12 = (C[f"s12.{k}"] for k in "abcd")
    X = 1560

    def lata():
        E.foco(c, t, a9, 0.5, lambda q: E.cilindro(c, t, a9, 330, 820, 150, 400))
        E.foco(c, t, a9 + 0.3, 0.4, lambda q: centro(c, "lata = cilindro", 330, 960, 52, "i", TINTA2, q))
        tamp = prog(t, b9, 0.5)
        rotulo_lata(c, t, NX, NY, NW, NH, NR, prog(t, c9, 1.4), 1.0, tampas=tamp)
        E.foco(c, t, b9 + 0.3, 0.4, lambda q: E.escreve(c, "2 tampas", NX + NW * 0.16 + NR + 24, NY - NR + 16, 48, "i", TINTA2, q))
        E.foco(c, t, c9 + 1.0, 0.4, lambda q: centro(c, "rótulo", NX + NW / 2, NY + NH / 2 + 20, 64, "g", COR, q))
        # altura
        if t >= a10:
            p = ep(t, a10, 0.5)
            M.line(c, NX - 36, NY, NX - 36, NY + NH, COR, p, 6, progress=p)
            E.foco(c, t, a10 + 0.2, 0.4, lambda q: E.escreve(c, "h", NX - 92, NY + NH / 2 + 20, 64, "g", COR, q))
        # a volta da tampa = a largura do rótulo
        if t >= b10:
            p = ease_io(prog(t, b10, 2.0))
            cx, cy = NX + NW * 0.16, NY - NR
            c.drawArc(skia.Rect.MakeXYWH(cx - NR, cy - NR, 2 * NR, 2 * NR), 90, 360 * p, False, M.paint(E.COR, 1, stroke=12, cap_round=True))
            M.line(c, NX, NY + NH, NX + NW * p, NY + NH, E.COR, 1, 12)
        if t >= c10:
            E.chave(c, NX, NX + NW, NY + NH + 30, COR, ep(t, c10, 0.5), 26)
            E.foco(c, t, c10 + 0.3, 0.4, lambda q: centro(c, "2πr" if t < c11 else "2πr = 18 cm", NX + NW * 0.68, NY + NH + 130, 64, "g", COR, q))
            cx, cy = NX + NW * 0.16, NY - NR
            M.line(c, cx, cy, cx + NR, cy, TINTA, ep(t, c10 + 0.6, 0.4), 5)
            E.foco(c, t, c10 + 0.6, 0.4, lambda q: E.escreve(c, "r", cx + NR / 2 - 10, cy - 14, 46, "g", TINTA, q))
        E.frase(c, t, a10, ps("altura =", "i", 60) + [("altura da lata", "g", 56)], X, 260, "center", 0.1)
        E.frase(c, t, b10, ps("largura =", "i", 60) + [("a volta", "g", 56, COR)], X, 380, "center", 0.1)
        E.frase(c, t, c10 + 0.6, ps("r = raio da tampa", "i", 56, TINTA2), X, 470, "center", 0.1)
        # a lata do exemplo
        E.frase(c, t, a11, ps("raio", "i", 56) + [("3 cm", "g", 60)], X, 610, "center", 0.12)
        E.frase(c, t, a11 + 0.6, ps("altura", "i", 56) + [("10 cm", "g", 60)], X, 690, "center", 0.12)
        E.foco(c, t, a11 + 1.2, 0.4, lambda q: centro(c, "π = 3", X, 770, 56, "g", TINTA2, q))
        fcen(c, t, b11, "2 × 3 × 3 = 18", X, 870, 76)
        E.foco(c, t, c11, 0.5, lambda q: E.pilula(c, "18 cm × 10 cm", X, 980, 60, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s09"], C["s12"] - 0.1, lata)
    if t < C["s12"] - 0.1:
        return

    # cone e esfera
    E.cone(c, t, C["s12"], 300, 600, 120, 300)
    E.foco(c, t, a12, 0.5, lambda q: (c.drawCircle(760, 760, 80, M.paint(E.mix(E.COR, "#FFFFFF", 0.78), q)),
                                      c.drawCircle(760, 760, 80, M.paint(TINTA, q, stroke=5))))
    gr = 360 * 80 / 230
    leque(c, 760, 450, 230, 90 - gr / 2, gr, 1.0, p=prog(t, b12, 1.0))
    E.frase(c, t, a12, ps("base:", "i", 56) + [("círculo", "g", 56)], 300, 800, "center", 0.1)
    E.frase(c, t, b12 + 0.4, ps("lateral:", "i", 56) + [("leque", "g", 56, COR)], 300, 890, "center", 0.1)
    E.esfera(c, t, c12, 1450, 520, 200)
    E.frase(c, t, c12 + 0.3, [("esfera:", "g", 62, COR)] + ps("não tem", "i", 62), 1450, 830, "center", 0.1)
    E.frase(c, t, c12 + 0.9, ps("planificação", "i", 62), 1450, 910, "center", 0.1)
    E.frase(c, t, d12, ps("casca de laranja:", "i", 52, TINTA2) + [("rasga ou enruga", "g", 52, ERRADO)], 1450, 1010, "center", 0.1)
    E.foco(c, t, d12 + 0.6, 0.5, lambda q: E.selo(c, 1660, 360, 64 * ease_back(prog(t, d12 + 0.6, 0.5)), False, q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    cx, cy, R = 470, 600, 220
    E.frase(c, t, C["s13"] + 0.2, [("o erro", "g", 80, ERRADO)] + ps("comum", "i", 80), W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s13"] + 0.3, 0.5, lambda q: (c.drawCircle(cx, cy, R, M.paint(E.mix(E.COR, "#FFFFFF", 0.82), q)),
                                                 c.drawCircle(cx, cy, R, M.paint(TINTA, q, stroke=6))))
    E.foco(c, t, C["s13"] + 0.6, 0.4, lambda q: centro(c, "a tampa", cx, cy + R + 80, 52, "i", TINTA2, q))
    if t >= b13:
        p = ep(t, b13, 0.5)
        M.line(c, cx - R, cy, cx + R, cy, ERRADO, p, 7, progress=p)
        E.foco(c, t, b13 + 0.3, 0.4, lambda q: centro(c, "6 cm", cx, cy - 26, 56, "g", ERRADO, q))
    # o rótulo errado cobre 6 de 18: um terço da volta
    if t >= c13:
        p = ease_io(prog(t, c13, 0.9))
        E.arco(c, cx, cy, R + 34, -90, 120 * p, ERRADO, 16)
        if t >= c13 + 0.9 and t < d13:
            pt = M.paint(TINTA2, 0.6, stroke=6)
            pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
            c.drawArc(skia.Rect.MakeXYWH(cx - R - 34, cy - R - 34, 2 * R + 68, 2 * R + 68), 30, 240, False, pt)
    if t >= d13:
        E.arco(c, cx, cy, R + 34, 30, 240 * ease_io(prog(t, d13, 1.0)), CERTO, 16)
    X0, Y0, U, HH = 900, 330, 30, 300
    E.frase(c, t, a13, ps("rótulo", "i", 62) + [("=", "g", 62)] + ps("largura da lata?", "i", 62), 1350, 290, "center", 0.1)
    p = ep(t, b13 + 0.6, 0.5)
    if p > 0:
        c.drawRect(skia.Rect.MakeXYWH(X0, Y0 + 60, 6 * U, HH), M.paint(ERRADO, 0.18 * p))
        c.drawRect(skia.Rect.MakeXYWH(X0, Y0 + 60, 6 * U, HH), M.paint(ERRADO, p, stroke=6))
        E.foco(c, t, b13 + 0.8, 0.4, lambda q: centro(c, "6 × 10", X0 + 3 * U, Y0 + 60 + HH + 70, 52, "g", ERRADO, q))
    if t >= d13:
        k = ease_io(prog(t, d13 + 0.3, 1.0))
        x1 = X0 + 6 * U + 40
        c.drawRect(skia.Rect.MakeXYWH(x1, Y0 + 60, 18 * U * k, HH), M.paint(CERTO, 0.18))
        c.drawRect(skia.Rect.MakeXYWH(x1, Y0 + 60, 18 * U * k, HH), M.paint(CERTO, 1, stroke=6))
        E.foco(c, t, d13 + 1.0, 0.4, lambda q: centro(c, "18 × 10", x1 + 9 * U, Y0 + 60 + HH + 70, 52, "g", CERTO, q))
    E.frase(c, t, c13, ps("não cobre", "i", 62) + [("nem metade", "g", 62, ERRADO)], 1350, 880, "center", 0.1)
    E.frase(c, t, d13 + 0.6, [("18 cm", "g", 66, CERTO)] + ps("= o triplo de", "i", 62) + [("6", "g", 66)], 1350, 990, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def quadrados(c, t, t0, x0, y, s, nums, cores=None, a=1.0):
    """fila de quadrados com números, no palco"""
    for i, n in enumerate(nums):
        q = ep(t, t0 + 0.12 * i, 0.4) * a
        if q <= 0:
            continue
        x = x0 + i * s
        cor = (cores or {}).get(n)
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(cor or "#FFFFFF", q * (0.9 if cor else 0.08)))
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(BR, q, stroke=5))
        centro(c, n, x + s / 2, y + s / 2 + 30, 84, "g", BR, q)


def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15, d15, e15 = (C[f"s15.{k}"] for k in "abcde")

    def fila():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho do cubo", "i", 76, CLARO), W / 2, 200, "center", 0.12)
        E.frase(c, t, a14, [("pula uma", "g", 150, BR)], W / 2, 380, "center")
        s, x0, y = 190, W / 2 - 2 * 190, 560
        cores = {}
        if t >= c14:
            cores.update({"1": E.COR, "3": E.COR})
        if t >= lerp(c14, C["s14.end"], 0.5):
            cores.update({"2": TINTA2, "4": TINTA2})
        quadrados(c, t, b14, x0, y, s, ("1", "2", "3", "4"), cores)
        E.salto(c, t, c14, x0 + s / 2, x0 + 2.5 * s, y - 10, 130, CLARO, None)
        E.salto(c, t, lerp(c14, C["s14.end"], 0.5), x0 + 1.5 * s, x0 + 3.5 * s, y + s + 10, -130, BR, None)
        E.frase(c, t, b14 + 0.4, ps("a oposta vem logo depois da vizinha", "i", 60, CLARO), W / 2, 1000, "center", 0.1)
    fase(c, t, C["s14"], C["s15"] - 0.1, fila)
    if t < C["s15"] - 0.1:
        return

    def dobras():
        E.frase(c, t, a15, ps("cada dobra:", "i", 76, CLARO) + [("90°", "g", 84, BR)], W / 2, 220, "center", 0.12)
        # vista de lado: a fila 1-2-3 dobra nas duas pontas do 2
        L, cy = 260, 780
        th = math.radians(90 * ease_io(prog(t, a15 + 0.4, 1.4)))
        A, B = (W / 2 - L / 2, cy), (W / 2 + L / 2, cy)
        P1 = (A[0] - L * math.cos(th), cy - L * math.sin(th))
        P3 = (B[0] + L * math.cos(th), cy - L * math.sin(th))
        for (p0, p1), cor, n in (((A, B), TINTA2, "2"), ((P1, A), E.COR, "1"), ((B, P3), E.COR, "3")):
            M.line(c, *p0, *p1, CLARO if cor == E.COR else "#8E8CA8", 1, 22)
            mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            centro(c, n, mx + (-60 if n == "1" else 60 if n == "3" else 0), my + (70 if n == "2" else 0) + 22, 64, "g", BR)
        for V_, s_ in ((A, 1), (B, -1)):
            k = ep(t, a15 + 1.6, 0.4)
            if k > 0:
                q = 34
                path = skia.Path(); path.moveTo(V_[0] + s_ * q, V_[1]); path.lineTo(V_[0] + s_ * q, V_[1] - q); path.lineTo(V_[0], V_[1] - q)
                c.drawPath(path, M.paint(BR, k, stroke=4))
        fcen(c, t, b15, "90° + 90° = 180°", W / 2, 400, 90, BR)
        if t >= c15:
            k = ep(t, c15, 0.5)
            yy = cy - L * 0.55
            M.arrow(c, A[0] - 10, yy, A[0] + 90, yy, CLARO, k, 6, 18, k)
            M.arrow(c, B[0] + 10, yy, B[0] - 90, yy, CLARO, k, 6, 18, k)
            E.frase(c, t, c15 + 0.2, ps("o 1 fica virado para o 3", "i", 64, CLARO), W / 2, 1000, "center", 0.1)
    fase(c, t, C["s15"], d15 - 0.1, dobras)
    if t < d15 - 0.1:
        return
    E.frase(c, t, d15, ps("abas em alturas diferentes:", "i", 66, CLARO) + [("não serve", "g", 66, BR)], W / 2, 220, "center", 0.1)
    s, ox, oy = 120, 760, 420
    for n, (i, j) in {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3), "5": (-1, 0), "6": (1, 2)}.items():
        q = ep(t, d15 + 0.3, 0.5)
        x, y = ox + i * s - s / 2, oy + j * s - s / 2
        dest = n in "56" and t >= e15
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(E.COR if dest else BR, q * (0.9 if dest else 0.08)))
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(BR, q, stroke=5))
        centro(c, n, x + s / 2, y + s / 2 + 24, 64, "g", BR, q)
    E.frase(c, t, e15, ps("faixa de 4:", "i", 64, CLARO), 1380, 520, "center", 0.1)
    E.frase(c, t, e15 + 0.5, [("aba esquerda", "g", 60, BR)], 1380, 610, "center", 0.1)
    E.frase(c, t, e15 + 0.9, ps("de frente para a", "i", 60, CLARO), 1380, 690, "center", 0.1)
    E.frase(c, t, e15 + 1.3, [("aba direita", "g", 60, BR)], 1380, 770, "center", 0.1)


# ---------------- questão ----------------
QX, QY = 1450, 470


def b_questao(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    ta = {"1": a16, "2": a16 + 0.2, "3": a16 + 0.4, "4": a16 + 0.6, "5": b16, "6": c16}
    E.saida(c, t, C["s18.a"] - 0.1, lambda: QUEST.desenha(c, t, 0, 0, QX, QY, ta=ta, nums={n: n for n in "123456"}, tn=ta, size=60))

    def dados():
        E.frase(c, t, a16, ps("faixa de 4 em pé:", "i", 66) + [("1 a 4", "g", 66, COR)], XE, 360, "left", 0.1)
        E.frase(c, t, b16, [("5", "g", 70, COR)] + ps("à esquerda do 1", "i", 66), XE, 480, "left", 0.1)
        E.frase(c, t, c16, [("6", "g", 70, COR)] + ps("à direita do 3", "i", 66), XE, 600, "left", 0.1)
    fase(c, t, C["s16"], a17 - 0.1, dados)
    E.frase(c, t, a17, ps("de frente para o", "i", 76) + [("2?", "g", 84, COR)], XE, 380, "left", 0.1)
    E.frase(c, t, b17, ps("e para o", "i", 76) + [("5?", "g", 84, COR)], XE, 520, "left", 0.1)
    E.frase(c, t, c17, ps("rótulo de uma lata", "i", 66), XE, 700, "left", 0.1)
    E.frase(c, t, c17 + 0.8, [("r = 5 cm", "g", 66, COR)] + ps("e", "i", 64) + [("π = 3:", "g", 66)], XE, 800, "left", 0.1)
    E.frase(c, t, c17 + 1.6, ps("qual a", "i", 66) + [("largura?", "g", 70, COR)], XE, 900, "left", 0.1)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19 = C["s19.a"], C["s19.b"]
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    a21, b21 = C["s21.a"], C["s21.b"]
    X = 1350
    ox, oy = 600, 480

    def cubo():
        cores = {}
        if t >= b19:
            cores.update({"2": E.COR, "4": E.COR})
        if t >= a20:
            cores.update({"5": CINZA2, "6": CINZA2})
        monta = ease_io(prog(t, b20, 2.0))
        cam = ease_io(prog(t, b20, 1.2))
        QUEST.desenha(c, t, monta, cam, ox, lerp(oy, 700, cam), ep(t, C["s19"], 0.4), cores=cores, nums={n: n for n in "123456"}, size=60)
        if C["s19"] <= t < b20:
            p = ease_io(prog(t, a19, 0.8))
            if p > 0:
                cx_, y0, y1 = ox - 65, oy, oy + 2 * 130
                path = skia.Path(); path.moveTo(cx_, y0)
                path.cubicTo(cx_ - 200, y0 + 20, cx_ - 200, y1 - 20, cx_, y1)
                me = skia.PathMeasure(path, False)
                seg = skia.Path(); me.getSegment(0, me.getLength() * p, seg, True)
                c.drawPath(seg, M.paint(E.COR, 1, stroke=8, cap_round=True))
        E.frase(c, t, a19, ps("pula o 3", "i", 70), X, 300, "center", 0.1)
        E.frase(c, t, b19, [("2", "g", 90, COR)] + ps("de frente para o", "i", 70) + [("4", "g", 90, COR)], X, 430, "center", 0.1)
        E.frase(c, t, a20, [("5", "g", 74)] + ps("à esquerda,", "i", 64) + [("6", "g", 74)] + ps("à direita", "i", 64), X, 600, "center", 0.1)
        E.frase(c, t, b20, ps("cada um fecha uma ponta", "i", 62, TINTA2), X, 710, "center", 0.1)
        E.frase(c, t, c20, [("5", "g", 90)] + ps("de frente para o", "i", 70) + [("6", "g", 90)], X, 850, "center", 0.1)
    fase(c, t, C["s19"], C["s21"] - 0.1, cubo)
    if t < C["s21"] - 0.1:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("o rótulo da lata de", "i", 76) + [("r = 5 cm", "g", 80, COR)], W / 2, 240, "center", 0.12)
    fcen(c, t, a21, "2 × 3 × 5 = 30", W / 2, 470, 120)
    E.foco(c, t, a21 + 0.8, 0.4, lambda q: centro(c, "cm de largura", W / 2, 560, 60, "i", TINTA2, q))
    E.frase(c, t, b21 - 0.4, ps("pelo triplo do diâmetro:", "i", 62, TINTA2), W / 2, 700, "center", 0.1)
    fcen(c, t, b21, "3 × 10 = 30", W / 2 - 80, 840, 110, COR)
    E.foco(c, t, b21 + 1.0, 0.5, lambda q: E.selo(c, W / 2 + 330, 805, 80 * ease_back(prog(t, b21 + 1.0, 0.5)), True, q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", ps("as formas do molde dizem", "i", 70) + [("o sólido", "g", 70, COR)]),
                 ("s22.b", ps("no cubo,", "i", 70) + [("pula uma", "g", 76, COR)]),
                 ("s22.c", ps("lateral do cilindro:", "i", 70) + [("2πr de largura", "g", 70, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 360, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3, d3 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a3, [("Vistas", "g", 130, COR)], XE, 420)
    E.frase(c, t, a3 + 0.5, ps("de frente e de cima", "i", 72), XE, 530, passo=0.1)
    E.frase(c, t, b3, ps("a sombra de cada sólido", "i", 72), XE, 660, passo=0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c3 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c3 + 0.2, 0.4))
    E.frase(c, t, d3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, molde=b_molde, cubo=b_cubo, cilindro=b_cilindro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
