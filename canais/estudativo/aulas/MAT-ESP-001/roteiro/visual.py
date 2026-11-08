"""Visual — Estudativo · MAT-ESP-001: sólidos, poliedros e relação de Euler. Primeira aula de Geometria Espacial.

LINGUAGEM VISUAL DA GEOMETRIA ESPACIAL (as próximas aulas da trilha copiam daqui; ela continua a da Geometria Plana, MAT-ANG-001):
- Sólidos sempre com as peças do kit (E.cubo, E.paralelepipedo, E.prisma, E.piramide, E.cilindro, E.cone, E.esfera):
  arestas em tinta preta (TINTA), arestas escondidas tracejadas, corpo translúcido na cor da matéria.
  Poliedro em perspectiva cavaleira (frente de verdade, fundo subindo para a direita); corpo redondo visto de cima e de lado.
- As peças devolvem os vértices na tela (pts). No paralelepípedo e no cubo: 0..3 = frente (embaixo esq, embaixo dir,
  em cima dir, em cima esq) e 4..7 = fundo na mesma ordem; o vértice 4 é o escondido. No prisma: 0..n−1 = base de baixo,
  n..2n−1 = de cima. Na pirâmide: 0..n−1 = base, n = o vértice de cima.
- O ELEMENTO DA VEZ ganha a cor da matéria por cima do sólido: face = polígono pintado (face()), aresta = traço grosso
  (aresta()), vértice = bolinha que salta (vertice()). Contagem = bolinhas numeradas 1, 2, 3... (numera()), na ordem da fala.
- Duas faces que dividem uma aresta: a 1ª em COR, a 2ª em cinza (TINTA2), como as famílias de ângulos da Geometria Plana.
- Aresta escondida que a fala aponta: o mesmo tracejado, grosso e na cor da matéria.
- Contagens e fórmulas na grotesca (V, A, F); resposta final numa esfera (bola), como no resto do curso.
- Objeto do dia a dia vira o sólido do kit com o nome embaixo (caixa de sapato = paralelepípedo, lata = cilindro...).
- Sólido que muda de lugar ou de grupo desliza (lerp da posição), não some e reaparece.
Peças locais desta aula: face(), aresta(), vertice(), numera(), dado() (cubo com as pintas, por na_face()), icosaedro()
(poliedro de 20 faces triangulares, montado com E._solido) e folha() (folha de papel, a mesma de MAT-ANG-001).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import itertools
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-001_solidos_poliedros_e_euler.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grupos", "partes", "euler", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 8 - 12 + 6 == 2 and 5 - 8 + 5 == 2 and 6 * 4 == 24 and 24 // 2 == 12 and 20 * 3 == 60 and 60 // 2 == 30
assert 12 - 30 + 20 == 2 and 2 + 6 == 8 and 6 * 2 == 12 and 12 - 18 + 8 == 2 and 2 * 6 + 6 * 4 == 36 and 36 // 2 == 18


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def fase(c, t, t0, t1, fn):
    """desenha fn de t0 até t1 e some desfocando"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def alfa(c, a, fn):
    """desenha fn com transparência a (para sólidos que esperam a vez)"""
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint()
    p.setAlphaf(a)
    c.saveLayer(None, p)
    fn()
    c.restore()


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


# ---------------- peças da Geometria Espacial ----------------
def face(c, pts, idx, a=1.0, cor=None, alfa_=0.42):
    """a face da vez, pintada por cima do sólido"""
    if a <= 0:
        return
    p = skia.Path()
    p.addPoly([pts[i] for i in idx], True)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.45, tracejada=False, a=1.0):
    """a aresta da vez: traço grosso na cor da matéria que corre de P até Q"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    """o vértice da vez: bolinha que salta"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


def numera(c, t, ts, pts, idx, G, size=42, cor=None, r=13, a=1.0, n0=1):
    """contagem: bolinha em cada vértice de idx e o número dele, por fora do sólido (G = centro do sólido na tela)"""
    for k, (i, ti) in enumerate(zip(idx, ts)):
        P = pts[i]
        vertice(c, t, ti, P, r, cor, a)
        E.foco(c, t, ti, 0.35, lambda q, P=P, k=k: E._cola(c, str(n0 + k), P[0], P[1], P[0] - G[0], P[1] - G[1], 16, size, "b",
                                                            cor or COR, q * a))


def centro_pts(pts):
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)


def na_face(c, O, U, V, fn):
    """desenha fn() no quadrado (0..1, 0..1) levado à face: O = canto (0, 0), U = canto (1, 0), V = canto (0, 1)"""
    m = skia.Matrix.MakeAll(U[0] - O[0], V[0] - O[0], O[0], U[1] - O[1], V[1] - O[1], O[1], 0, 0, 1)
    c.save()
    c.concat(m)
    fn()
    c.restore()


PINTAS = {1: ((0.5, 0.5),), 3: ((0.25, 0.25), (0.5, 0.5), (0.75, 0.75)),
          5: ((0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75))}


def dado(c, t, t0, x, y, a, **kw):
    """o dado: E.cubo com as pintas (5 na frente, 1 em cima, 3 do lado). Devolve os vértices na tela"""
    pts = E.cubo(c, t, t0, x, y, a, **kw)
    q = ep(t, t0 + 0.7, 0.5)
    if q > 0:
        tinta = M.paint(TINTA, q)
        for (O, U, V), n in (((pts[3], pts[2], pts[0]), 5), ((pts[7], pts[6], pts[3]), 1), ((pts[2], pts[6], pts[1]), 3)):
            na_face(c, O, U, V, lambda n=n: [c.drawOval(skia.Rect.MakeXYWH(u - 0.075, v - 0.075, 0.15, 0.15), tinta) for u, v in PINTAS[n]])
    return pts


def folha(c, x, y, w, h, a=1.0):
    """folha de papel com sombra"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 12, w, h), s)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#FFFFFF", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(CINZA, a, stroke=2))


def icosaedro(c, t, t0, cx, cy, r, d=1.6, **kw):
    """poliedro de 20 faces triangulares (o do atalho), com o centro em (cx, cy)"""
    f = (1 + 5 ** 0.5) / 2
    V = []
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            V += [(0, s1, s2 * f), (s1, s2 * f, 0), (s2 * f, 0, s1)]
    k = r / math.sqrt(1 + f * f)
    V = [(x * k, y * k, z * k) for x, y, z in V]
    F = [tri for tri in itertools.combinations(range(12), 3)
         if all(abs(math.dist(V[i], V[j]) - 2 * k) < 1e-6 for i, j in itertools.combinations(tri, 2))]
    assert len(F) == 20
    return E._solido(c, t, t0, V, F, E._vista_alta(-18, 14), cx, cy, d=d, **kw)


TOPO, BAIXO, PE = ((3, 2), (2, 6), (6, 7), (7, 3)), ((0, 1), (1, 5), (5, 4), (4, 0)), ((0, 3), (1, 2), (5, 6), (4, 7))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        pts = dado(c, t, a1, 260, 860, 420)
        # 8 pontas e as dobras, na fala
        tp, td = lerp(a1, b1, 0.3), lerp(a1, b1, 0.5)
        for k, i in enumerate((3, 2, 6, 7, 0, 1, 5, 4)):
            vertice(c, t, tp + 0.08 * k, pts[i], 14)
        for k, (i, j) in enumerate(TOPO + PE + BAIXO):
            aresta(c, t, td + 0.07 * k, pts[i], pts[j], largura=9, tracejada=4 in (i, j))
        E.frase(c, t, a1 + 0.5, [("6", "g", 120, COR), ("faces", "i", 100)], 1080, 300, "left", 0.15)
        E.frase(c, t, tp, [("8", "g", 120, COR), ("pontas", "i", 100)], 1080, 450, "left", 0.15)
        E.frase(c, t, td, [("?", "g", 120, COR), ("dobras", "i", 100)], 1080, 600, "left", 0.15)
        E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "sem contar nenhuma", 1390, 740, 58, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, c1, [("1", "g", 80, COR)] + ps("conta,", "i", 76) + [("3", "g", 80, COR)] + ps("números", "i", 76), 1390, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("separar", "g", 104, COR)] + ps("os sólidos", "i", 96), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), [("contar", "g", 104, COR)] + ps("faces,", "i", 96), XE, 600, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.75), ps("arestas e vértices", "i", 96), XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 880
    itens = (("s03.b", "polígono:", "figura plana e fechada"), ("s03.c", "nas diagonais,", "cada uma entrou 2 vezes"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 680, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 940, "left", 0.12)


# ---------------- dois grupos ----------------
def b_grupos(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")

    # 1) plana x sólido
    def plana():
        E.frase(c, t, C["s04"] + 0.2, [("plana:", "g", 80)] + ps("cabe na folha", "i", 76), 170, 200, "left", 0.12)
        E.foco(c, t, C["s04"] + 0.4, 0.5, lambda a: folha(c, 200, 330, 560, 560, a))
        E.regular(c, t, C["s04"] + 0.8, 5, 480, 630, 170, preenche=0.3)
        E.frase(c, t, a4, [("sólido:", "g", 80, COR)] + ps("ocupa espaço", "i", 76), 1010, 200, "left", 0.12)
        E.paralelepipedo(c, t, a4 + 0.3, 1160, 880, 360, 360, 360, ("comprimento", "largura", "altura"), size=50, tm=lerp(a4, b4, 0.4))
    fase(c, t, C["s04"], b4 - 0.1, plana)
    if t < b4 - 0.1:
        return

    # 2) três objetos; depois cada um desliza para o seu grupo
    m1 = ease_io(prog(t, a5, 1.0))   # a caixa vai para os poliedros, a lata e a bola esperam do outro lado
    vez_c, vez_b = ep(t, b6, 0.4), ep(t, d6, 0.4)
    espera = 1 - 0.7 * m1
    E.paralelepipedo(c, t, b4, lerp(170, 560, m1), lerp(840, 880, m1), lerp(420, 300, m1), lerp(220, 160, m1), lerp(200, 150, m1))
    alfa(c, espera + (1 - espera) * vez_c, lambda: E.cilindro(c, t, c4, lerp(980, 1130, m1), lerp(860, 900, m1), lerp(150, 95, m1), lerp(330, 230, m1)))
    rola = 70 * math.sin(math.pi * 2 * ep(t, e6 + 0.3, 1.6))
    alfa(c, espera + (1 - espera) * vez_b, lambda: E.esfera(c, t, d4, lerp(1560, 1710, m1) + rola, lerp(680, 790, m1), lerp(190, 120, m1)))

    def nomes():
        for s, x, tk in (("caixa de sapato", 380, b4), ("lata", 980, c4), ("bola", 1560, d4)):
            E.foco(c, t, tk + 0.3, 0.4, lambda a, s=s, x=x: centro(c, s, x, 990, 60, "i", TINTA, a))
    fase(c, t, b4, a5 - 0.1, nomes)
    if t < a5 - 0.1:
        return

    # 3) os dois grupos
    E.foco(c, t, a5, 0.5, lambda a: M.line(c, 960, 170, 960, 1010, TINTA2, a * 0.6, 3, dash=E.TRACO))
    E.frase(c, t, a5, [("poliedro", "g", 92, COR)], 480, 230, "center")
    E.frase(c, t, a5 + 0.6, ps("só faces planas", "i", 66), 480, 320, "center", 0.12)
    dado(c, t, b5, 150, 880, 250)
    E.foco(c, t, b5 + 0.3, 0.4, lambda a: (centro(c, "dado", 300, 980, 50, "i", TINTA2, a), centro(c, "caixa", 740, 980, 50, "i", TINTA2, a)))
    E.frase(c, t, a6, [("corpo redondo", "g", 92, COR)], 1440, 230, "center")
    E.frase(c, t, a6 + 0.8, ps("tem parte curva", "i", 66), 1440, 320, "center", 0.12)
    E.cone(c, t, c6, 1420, 900, 105, 270)
    for s, x, tk in (("cilindro", 1130, b6), ("cone", 1420, c6), ("esfera", 1710, d6)):
        E.foco(c, t, tk + 0.2, 0.4, lambda a, s=s, x=x: centro(c, s, x, 990, 50, "g", TINTA, a))
    E.frase(c, t, e6, [("rola", "g", 66, COR)] + ps("na mesa", "i", 66), 1440, 450, "center", 0.12)


# ---------------- prisma e pirâmide ----------------
def b_tipos(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")

    def prismas():
        E.frase(c, t, a7, [("prisma:", "g", 92, COR)] + ps("2 bases iguais", "i", 84), W / 2, 200, "center", 0.12)
        E.frase(c, t, lerp(a7, b7, 0.55), ps("ligadas por", "i", 70) + [("retângulos", "g", 70)], W / 2, 300, "center", 0.12)
        pts = E.prisma(c, t, a7, 380, 800, 5, 170, 320)
        q = ep(t, a7 + 0.8, 0.5)
        face(c, pts, range(5), q)
        face(c, pts, range(5, 10), q)
        i = max(range(5), key=lambda i: pts[i][1] + pts[(i + 1) % 5][1])  # o retângulo da frente
        face(c, pts, (i, (i + 1) % 5, 5 + (i + 1) % 5, 5 + i), ep(t, lerp(a7, b7, 0.6), 0.5), TINTA2, 0.16)
        E.foco(c, t, a7 + 0.4, 0.4, lambda a: centro(c, "prisma", 380, 960, 52, "g", COR, a))
        E.paralelepipedo(c, t, b7, 690, 860, 330, 180, 220)
        E.foco(c, t, b7 + 0.4, 0.4, lambda a: (centro(c, "paralelepípedo", 925, 960, 52, "g", COR, a), centro(c, "(bloco)", 925, 1020, 48, "i", TINTA2, a)))
        cp = E.cubo(c, t, c7, 1340, 860, 290)
        face(c, cp, (0, 1, 2, 3), ep(t, c7 + 0.8, 0.5), alfa_=0.3)
        E.foco(c, t, c7 + 0.4, 0.4, lambda a: (centro(c, "cubo", 1540, 960, 52, "g", COR, a), centro(c, "faces quadradas", 1540, 1020, 48, "i", TINTA2, a)))
    fase(c, t, C["s07"], C["s08"] - 0.1, prismas)
    if t < C["s08"] - 0.1:
        return

    pts = E.piramide(c, t, a8, 520, 800, 4, 240, 420)
    face(c, pts, range(4), ep(t, a8 + 0.8, 0.5))
    if t >= b8:
        pulsa = 1 + 0.6 * math.sin(min(1, prog(t, b8, 0.9)) * math.pi)
        vertice(c, t, b8, pts[4], 15 * pulsa)
        for i in range(4):
            aresta(c, t, b8 + 0.1 * i, pts[i], pts[4], largura=8, tracejada=False, a=1 - ep(t, c8, 0.4))

    def texto():
        E.frase(c, t, a8, [("pirâmide:", "g", 92, COR)] + ps("1 base só", "i", 84), 1000, 330, "left", 0.12)
        E.frase(c, t, lerp(a8, b8, 0.6), ps("o resto:", "i", 70) + [("triângulos", "g", 70)], 1000, 470, "left", 0.12)
        E.frase(c, t, b8, ps("que se encontram", "i", 70), 1000, 570, "left", 0.12)
        E.frase(c, t, b8 + 0.6, ps("num", "i", 70) + [("ponto", "g", 70, COR)], 1000, 670, "left", 0.12)
    fase(c, t, a8, c8 - 0.1, texto)
    if t >= c8 - 0.1:
        E.frase(c, t, c8, ps("a base dá o", "i", 84) + [("sobrenome", "g", 84, COR)], 1300, 250, "center", 0.12)
        E.foco(c, t, d8, 0.4, lambda a: (centro(c, "quadrangular", 520, 990, 60, "g", COR, a), centro(c, "base quadrada", 520, 1050, 44, "i", TINTA2, a)))
        pt3 = E.piramide(c, t, e8 - 0.2, 1400, 820, 3, 210, 330, giro=20)
        face(c, pt3, range(3), ep(t, e8 + 0.6, 0.5))
        E.foco(c, t, e8, 0.4, lambda a: (centro(c, "triangular", 1400, 990, 60, "g", COR, a), centro(c, "base triangular", 1400, 1050, 44, "i", TINTA2, a)))


# ---------------- partes do poliedro ----------------
CX0, CY0, CA = 230, 890, 440


def b_partes(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    pts = E.cubo(c, t, a9, CX0, CY0, CA)
    G = centro_pts(pts)
    X = 1060

    def partes():
        face(c, pts, (0, 1, 2, 3), ep(t, b9, 0.5))
        aresta(c, t, c9, pts[3], pts[2], largura=15)
        face(c, pts, (3, 2, 6, 7), ep(t, c9, 0.5), TINTA2, 0.16)
        if t >= d9:
            pulsa = 1 + 0.6 * math.sin(min(1, prog(t, d9, 0.9)) * math.pi)
            vertice(c, t, d9, pts[2], 17 * pulsa)
        E.frase(c, t, b9, [("face", "g", 100, COR)], X, 290)
        E.frase(c, t, b9 + 0.4, ps("cada polígono da casca", "i", 62), X, 370, "left", 0.1)
        E.frase(c, t, c9, [("aresta", "g", 100, COR)], X, 530)
        E.frase(c, t, c9 + 0.4, ps("encontro de 2 faces: a dobra", "i", 62), X, 610, "left", 0.1)
        E.frase(c, t, d9, [("vértice", "g", 100, COR)], X, 770)
        E.frase(c, t, d9 + 0.4, ps("a ponta", "i", 62), X, 850, "left", 0.1)
    fase(c, t, C["s09"], C["s10"] - 0.1, partes)

    def perspectiva():
        E.frase(c, t, a10, ps("em", "i", 84) + [("perspectiva", "g", 92, COR)], X, 360, "left", 0.12)
        E.frase(c, t, a10 + 0.6, ps("como numa foto", "i", 70), X, 460, "left", 0.12)
        for k, (i, j) in enumerate(((4, 5), (4, 7), (4, 0))):
            aresta(c, t, b10 + 0.2 * k, pts[i], pts[j], largura=11, tracejada=True)
        E.frase(c, t, b10, ps("escondidas:", "i", 70) + [("tracejadas", "g", 76, COR)], X, 650, "left", 0.12)
        E.frase(c, t, lerp(b10, C["s10.end"], 0.55), ps("contam igual", "i", 70), X, 760, "left", 0.12)
    fase(c, t, C["s10"], C["s11"] - 0.1, perspectiva)
    if t < C["s11"] - 0.1:
        return

    # contagem: 8 vértices, 12 arestas, 6 faces
    ordem = (3, 2, 6, 7, 0, 1, 5, 4)
    E.saida(c, t, b11 - 0.1, lambda: numera(c, t, [a11 + 0.18 * k + (0.4 if k >= 4 else 0) for k in range(8)], pts, ordem, G))
    for g_, (grupo, f0) in enumerate(((TOPO, 0.0), (BAIXO, 0.3), (PE, 0.6))):
        tg = lerp(b11, c11, f0)
        for k, (i, j) in enumerate(grupo):
            aresta(c, t, tg + 0.1 * k, pts[i], pts[j], largura=10, tracejada=4 in (i, j), a=1 - ep(t, c11, 0.4))
    for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5))):
        face(c, pts, idx, ep(t, c11 + 0.2 * k, 0.4), alfa_=0.3)
    fcen(c, t, a11 + 0.4, "V = 8", X + 220, 330, 110)
    E.frase(c, t, a11 + 1.0, ps("4 em cima + 4 embaixo", "i", 52, TINTA2), X + 220, 410, "center", 0.08)
    fcen(c, t, b11 + 0.3, "A = 12", X + 220, 600, 110)
    E.frase(c, t, lerp(b11, c11, 0.7), ps("4 + 4 + 4 em pé", "i", 52, TINTA2), X + 220, 680, "center", 0.08)
    fcen(c, t, c11 + 0.2, "F = 6", X + 220, 870, 110)


# ---------------- relação de Euler ----------------
def b_euler(c, t, C, b):
    a12, b12 = C["s12.a"], C["s12.b"]
    X = 1260

    def cubo():
        E.cubo(c, t, C["s12"] - 1.0, 200, 840, 360)
        E.foco(c, t, C["s12"], 0.4, lambda a: centro(c, "V = 8    A = 12    F = 6", X, 290, 64, "g", TINTA2, a))
        E.frase(c, t, a12, ps("vértices − arestas + faces", "i", 64), X, 450, "center", 0.12)
        fcen(c, t, a12 + 1.2, "V − A + F", X, 590, 120, COR)
        fcen(c, t, b12, "8 − 12 + 6 =", X - 60, 790, 110)
        bola_txt(c, t, b12 + 1.0, "2", X + 380, 755, 95, 110)
    fase(c, t, C["s12"], C["s13"] - 0.1, cubo)
    if C["s13"] - 0.1 <= t < C["s14"] + 0.3:
        E.saida(c, t, C["s14"] - 0.1, lambda: piramide_euler(c, t, C))
    if t >= C["s14"] - 0.1:
        relacao(c, t, C)


def piramide_euler(c, t, C):
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    X = 1260
    pts = E.piramide(c, t, C["s13"], 470, 860, 4, 250, 460)
    G = centro_pts(pts)
    numera(c, t, [a13 + 0.2 * k for k in range(4)] + [a13 + 1.2], pts, (0, 1, 2, 3, 4), G, a=1 - ep(t, b13, 0.4))
    for k in range(4):
        aresta(c, t, b13 + 0.12 * k, pts[k], pts[(k + 1) % 4], largura=10, a=1 - ep(t, c13, 0.4))
        aresta(c, t, b13 + 1.2 + 0.12 * k, pts[k], pts[4], largura=10, a=1 - ep(t, c13, 0.4))
    face(c, pts, range(4), ep(t, c13, 0.4), alfa_=0.35)
    for k in range(4):
        face(c, pts, (k, (k + 1) % 4, 4), ep(t, c13 + 0.6 + 0.15 * k, 0.4), TINTA2, 0.1)
    x0 = 1000
    for y, tk, s, nota in ((290, a13, "V = 5", "4 + 1"), (450, b13, "A = 8", "4 + 4"), (610, c13, "F = 5", "1 + 4")):
        E.foco(c, t, tk + 0.3, 0.5, lambda a, y=y, s=s: E.formula(c, s, x0, y, 100, "g", TINTA, a))
        E.foco(c, t, tk + 1.0, 0.5, lambda a, y=y, nota=nota: E.escreve(c, nota, x0 + 360, y - 8, 60, "i", TINTA2, a))
    fcen(c, t, d13, "5 − 8 + 5 =", X - 40, 820, 110)
    bola_txt(c, t, d13 + 1.0, "2", X + 380, 785, 95, 110)


def relacao(c, t, C):
    a14, b14, c14, d14, e14, f14 = (C[f"s14.{k}"] for k in "abcdef")
    a15, b15, c15, d15 = (C[f"s15.{k}"] for k in "abcd")

    def formula():
        E.frase(c, t, a14, ps("relação de", "i", 92) + [("Euler", "g", 100, COR)], W / 2, 220, "center", 0.12)
        size = 170
        partes = [("V", c14), ("−", b14), ("A", d14), ("+", b14), ("F", e14), ("=", b14), ("2", b14)]
        xs = E.linha(c, t, [(s, "g", size, COR if (s in "VAF" and t >= tk) else TINTA, b14 if s in "VAF" else b14 + 0.1)
                            for s, tk in partes], W / 2, 490, "center")
        for (s, tk), x in zip(partes, xs):
            if s in "VAF":
                nome = {"V": "vértices", "A": "arestas", "F": "faces"}[s]
                E.foco(c, t, tk, 0.4, lambda a, x=x, s=s, nome=nome: centro(c, nome, x + E.larg(s, "g", size) / 2, 610, 56, "i", COR, a))
        E.foco(c, t, f14, 0.5, lambda a: E.pilula(c, "poliedros convexos", W / 2, 790, 70, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, f14 + 0.8, ps("sem nenhuma parte afundada", "i", 62, TINTA2), W / 2, 930, "center", 0.1)
    fase(c, t, C["s14"], C["s15"] - 0.1, formula)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("achar o número que", "i", 76) + [("falta", "g", 80, COR)], W / 2, 200, "center", 0.12)
    E.foco(c, t, a15, 0.5, lambda a: centro(c, "V = 8      F = 6      A = ?", 760, 340, 76, "g", TINTA2, a))
    fcen(c, t, b15, "8 − A + 6 = 2", 760, 500, 120)
    fcen(c, t, c15, "14 − A = 2", 760, 660, 120)
    bola_txt(c, t, d15, "A = 12", 760, 870, 145, 72)
    dado(c, t, d15 + 0.2, 1380, 920, 260)
    E.frase(c, t, d15 + 0.8, ps("as dobras do dado", "i", 58, TINTA2), 1560, 500, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    pts = E.cubo(c, t, C["s16"], 200, 900, 420)
    X = 1330
    E.frase(c, t, C["s16"] + 0.2, [("o erro", "g", 80, ERRADO)] + ps("mais comum", "i", 80), W / 2, 170, "center", 0.12)
    # face por face: cada face acende com os 4 lados
    for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5))):
        face(c, pts, idx, ep(t, a16 + 0.4 * k, 0.4) * (1 - ep(t, c16, 0.4)), ERRADO, 0.18)
    E.frase(c, t, a16, ps("contar", "i", 72) + [("face por face", "g", 72, ERRADO)], X, 330, "center", 0.12)
    E.frase(c, t, lerp(a16, b16, 0.5), ps("6 faces de 4 lados", "i", 66), X, 450, "center", 0.12)
    fcen(c, t, b16, "6 × 4 = 24", X, 600, 110, ERRADO)
    # a dobra é de duas faces
    face(c, pts, (0, 1, 2, 3), ep(t, c16, 0.4), alfa_=0.4)
    face(c, pts, (3, 2, 6, 7), ep(t, c16 + 0.3, 0.4), TINTA2, 0.16)
    aresta(c, t, c16 + 0.5, pts[3], pts[2], largura=15)
    E.frase(c, t, c16, [("1 aresta", "g", 72, COR)] + ps("= dobra de", "i", 70) + [("2 faces", "g", 72)], X, 760, "center", 0.12)
    mx, my = (pts[3][0] + pts[2][0]) / 2, (pts[3][1] + pts[2][1]) / 2
    for k, (dy, cor) in enumerate(((60, E.COR), (-60, TINTA2))):
        tk = d16 + 0.5 * k
        E.foco(c, t, tk, 0.4, lambda a, dy=dy, cor=cor, k=k: (E.bola(c, mx, my + dy, 34, cor, a), centro(c, str(k + 1), mx, my + dy + 15, 42, "g", BR, a)))
    E.frase(c, t, d16 + 0.3, ps("contou", "i", 66) + [("2 vezes", "g", 70, ERRADO)], X, 880, "center", 0.12)
    E.frase(c, t, e16, [("24", "g", 84, ERRADO), ("=", "g", 84), ("2 × 12", "g", 84, CERTO)], X, 1010, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a17, b17, c17, d17 = (C[f"s17.{k}"] for k in "abcd")
    a18, b18, c18, d18, e18 = (C[f"s18.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, C["s17"] + 0.2, ps("o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.foco(c, t, a17, 0.5, lambda a: E.formula(c, "A = f{soma dos lados}{2}", W / 2, 330, 84, "g", BR, a, "center"))
        icosaedro(c, t, b17, 500, 720, 270, escuro=True)
        E.frase(c, t, b17 + 0.2, [("20", "g", 96, BR)] + ps("faces", "i", 90, CLARO), 1350, 560, "center", 0.12)
        E.frase(c, t, b17 + 0.8, ps("todas", "i", 76, CLARO) + [("triângulos", "g", 80, BR)], 1350, 660, "center", 0.12)
        fcen(c, t, c17, "20 × 3 = 60 lados", 1350, 820, 92, BR)
        fcen(c, t, d17, "60 ÷ 2 = 30", 1260, 970, 110, CLARO)
        E.foco(c, t, d17 + 0.6, 0.5, lambda a: E.escreve(c, "arestas", 1600, 960, 66, "i", BR, a))
    fase(c, t, C["s17"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return

    def porque():
        E.frase(c, t, a18, ps("cada aresta é lado de", "i", 80, CLARO) + [("2 faces", "g", 84, BR)], W / 2, 240, "center", 0.12)
        A, B = (960, 380), (960, 760)
        for k, (P, cor) in enumerate((((620, 570), CLARO), ((1300, 570), BR))):
            q = ep(t, a18 + 0.4 + 0.3 * k, 0.5)
            if q > 0:
                p = skia.Path(); p.addPoly([A, B, P], True)
                c.drawPath(p, M.paint(cor, 0.22 * q))
                c.drawPath(p, M.paint(BR, q, stroke=6))
        aresta(c, t, a18 + 1.2, A, B, CLARO, 15)
        E.frase(c, t, lerp(a18, b18, 0.55), ps("como a diagonal com", "i", 64, CLARO) + [("2 pontas", "g", 66, BR)], W / 2, 910, "center", 0.1)
    fase(c, t, a18, b18 - 0.1, porque)

    def quando():
        E.frase(c, t, b18, ps("não sabe a forma", "i", 90, BR), W / 2, 380, "center", 0.12)
        E.frase(c, t, b18 + 0.7, ps("das faces?", "i", 90, BR), W / 2, 490, "center", 0.12)
        E.frase(c, t, c18, ps("use", "i", 110, CLARO) + [("Euler", "g", 130, BR)], W / 2, 720, "center", 0.12)
    fase(c, t, b18, d18 - 0.1, quando)
    if t >= d18 - 0.1:
        E.frase(c, t, d18, ps("atalho", "i", 76, CLARO) + [("+", "g", 76, BR)] + ps("Euler", "i", 76, CLARO), W / 2, 250, "center", 0.12)
        fcen(c, t, d18 + 0.2, "V − 30 + 20 = 2", W / 2, 520, 130, BR)
        bola_txt(c, t, e18, "V = 12", W / 2, 760, 150, 84)
        E.foco(c, t, e18 + 0.6, 0.5, lambda a: centro(c, "vértices", W / 2, 990, 66, "i", CLARO, a))


# ---------------- questão ----------------
PX, PY = 1520, 820


def b_questao(c, t, C, b):
    a19, b19, c19, d19 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a19, ps("caixa de presente:", "i", 70), XE, 340, passo=0.1)
    E.frase(c, t, a19 + 0.8, [("prisma", "g", 76)] + ps("de base", "i", 70) + [("hexagonal", "g", 76, COR)], XE, 440, passo=0.1)
    E.frase(c, t, b19, ps("quantas", "i", 80) + [("faces?", "g", 86, COR)], XE, 620, passo=0.12)
    E.frase(c, t, c19, ps("quantos", "i", 80) + [("vértices?", "g", 86, COR)], XE, 750, passo=0.12)
    E.frase(c, t, d19, ps("e, por Euler,", "i", 80) + [("arestas?", "g", 86, COR)], XE, 880, passo=0.12)

    def caixa():
        pts = E.prisma(c, t, a19, PX, PY, 6, 210, 360)
        q = ep(t, a19 + 1.0, 0.5)
        face(c, pts, range(6), q, alfa_=0.3)
        face(c, pts, range(6, 12), q, alfa_=0.3)
    E.saida(c, t, C["s20.a"] - 0.1, caixa)
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
    a22, b22, c22, d22, e22 = (C[f"s22.{k}"] for k in "abcde")
    pts = E.prisma(c, t, C["s21"], 480, 830, 6, 220, 400)
    G = centro_pts(pts)
    face(c, pts, range(6, 12), ep(t, a21, 0.4), alfa_=0.4)
    face(c, pts, range(6), ep(t, a21 + 0.6, 0.4), alfa_=0.4)
    for k in range(6):
        face(c, pts, (k, (k + 1) % 6, 6 + (k + 1) % 6, 6 + k), ep(t, lerp(a21, b21, 0.5) + 0.12 * k, 0.4), TINTA2, 0.08)
    some = 1 - ep(t, C["s22"], 0.4)
    numera(c, t, [c21 + 0.15 * k for k in range(6)], pts, range(6, 12), G, size=44, r=13, a=some)
    for k in range(6):
        vertice(c, t, c21 + 1.2 + 0.1 * k, pts[k], 13, TINTA2, some)
    E.foco(c, t, c21 + 1.2, 0.4, lambda a: centro(c, "× 2", 480, 1050, 56, "g", TINTA2, a * some))
    X = 1330
    E.frase(c, t, a21 + 0.3, ps("2 bases + 1 retângulo por lado", "i", 56, TINTA2), X, 140, "center", 0.1)
    fcen(c, t, b21, "F = 2 + 6 = 8", X, 260, 92)
    fcen(c, t, c21 + 0.3, "V = 6 × 2 = 12", X, 380, 92)

    def euler():
        fcen(c, t, a22, "12 − A + 8 = 2", X, 530, 96)
        fcen(c, t, b22, "20 − A = 2", X, 660, 96)
    fase(c, t, C["s22"], d22 - 0.1, euler)
    bola_txt(c, t, c22, "A = 18", 1170, 885, 135, 64)
    if t >= d22 - 0.1:
        E.frase(c, t, d22, ps("conferindo pelo atalho", "i", 60, TINTA2), X, 500, "center", 0.1)
        fcen(c, t, d22 + 0.6, "12 + 24 = 36 lados", X, 600, 80)
        fcen(c, t, e22, "36 ÷ 2 = 18", X, 700, 88, COR)
        E.foco(c, t, e22 + 1.4, 0.5, lambda a: E.selo(c, 1530, 885, 90 * ease_back(prog(t, e22 + 1.4, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s23.a", ps("poliedro:", "i", 76) + [("faces planas", "g", 76)], ps("corpo redondo:", "i", 76) + [("parte curva", "g", 76)]),
                 ("s23.b", ps("nos poliedros,", "i", 76) + [("V − A + F = 2", "g", 84, COR)], None))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 300
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 60, a=a), centro(c, str(i + 1), 300, y - 7, 68, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 400, y, "left", 0.12)
            if l2:
                E.frase(c, t, C[k] + 1.2, l2, 400, y + 100, "left", 0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a4, b4, c4, d4 = (C[f"s24.{k}"] for k in "abcd")
    E.frase(c, t, C["s24"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a4, [("Planificações", "g", 130, COR)], XE, 420)
    E.frase(c, t, a4 + 0.6, ps("desmontar e abrir no papel", "i", 72), XE, 530, passo=0.1)
    E.frase(c, t, b4, ps("qual face fica de frente", "i", 72), XE, 660, passo=0.1)
    E.frase(c, t, b4 + 0.8, ps("para qual", "i", 72), XE, 750, passo=0.1)
    molde_cruz(c, t, a4 + 0.4, 1390, 520, 84)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c4 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c4 + 0.2, 0.4))
    E.frase(c, t, d4, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


def molde_cruz(c, t, t0, x, y, s):
    """o molde do cubo em cruz (prévia da próxima aula): seis quadrados que entram um a um"""
    for k, (i, j) in enumerate(((1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3))):
        q = ep(t, t0 + 0.12 * k, 0.4)
        if q > 0:
            r = skia.Rect.MakeXYWH(x + i * s, y + j * s, s, s)
            c.drawRect(r, M.paint(E.COR, 0.25 * q))
            c.drawRect(r, M.paint(TINTA, q, stroke=5))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grupos=b_grupos, tipos=b_tipos, partes=b_partes, euler=b_euler,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
