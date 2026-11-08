"""Visual — Estudativo · MAT-ESP-004: retas e planos no espaço.
Mesma linguagem da MAT-ESP-001 (sólidos do kit, elemento da vez por cima do sólido, resposta na esfera).

POSIÇÃO DE RETAS NA CAIXA (as próximas aulas copiam daqui):
- A caixa é sempre E.paralelepipedo; os vértices vêm de pts (0..3 frente: embaixo esq, embaixo dir, em cima dir, em cima esq;
  4..7 o fundo na mesma ordem; o 4 é o escondido).
- A aresta ESCOLHIDA fica na cor da matéria, grossa. A aresta comparada fica em tinta preta, grossa (tracejada se escondida).
- Reta = aresta esticada: estica() prolonga as duas pontas com tracejado fino. Direção = setinha sobre a aresta (seta_dir()).
- Plano = paralelogramo translúcido maior que a face (plano_face()), com borda tracejada: a folha sem bordas.
- Ângulo reto no espaço = quadradinho desenhado nas duas direções das arestas (reto()), como na Geometria Plana.
- No palco do atalho: escolhida em branco, paralelas em lilás (CLARO), concorrentes em cor da matéria clara, reversas em cinza.
Peças locais: aresta(), estica(), seta_dir(), plano_face(), reto(), caixa().
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-004_retas_e_planos_no_espaco.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("plano", "posicoes", "perpendicular", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA_R = "#8E8CA8"
LILAS = E.mix(E.COR, "#FFFFFF", 0.3)
# a caixa: as 12 arestas e a conferência do atalho (3 paralelas, 4 concorrentes, 4 reversas da aresta 0-1)
ARESTAS = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
PARAL, CONC, REV = ((3, 2), (7, 6), (4, 5)), ((0, 3), (0, 4), (1, 2), (1, 5)), ((3, 7), (2, 6), (4, 7), (5, 6))
assert len(PARAL) + len(CONC) + len(REV) == 11 and all(0 in e or 1 in e for e in CONC) and not any(0 in e or 1 in e for e in PARAL + REV)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


# ---------------- peças de retas e planos ----------------
def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.45, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def estica(c, t, t0, P, Q, k=0.9, cor=None, a=1.0):
    """a reta da aresta: prolonga as duas pontas em k vezes o comprimento, tracejado"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0 or a <= 0:
        return
    dx, dy = Q[0] - P[0], Q[1] - P[1]
    M.line(c, *Q, Q[0] + dx * k, Q[1] + dy * k, cor or TINTA2, 0.8 * a, 4, dash=[12, 10], progress=p)
    M.line(c, *P, P[0] - dx * k, P[1] - dy * k, cor or TINTA2, 0.8 * a, 4, dash=[12, 10], progress=p)


def seta_dir(c, t, t0, P, Q, cor=None, a=1.0, off=(0, 0)):
    """setinha que mostra a direção da aresta, desenhada ao lado dela"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    mx, my = (P[0] + Q[0]) / 2 + off[0], (P[1] + Q[1]) / 2 + off[1]
    dx, dy = Q[0] - P[0], Q[1] - P[1]
    n = math.hypot(dx, dy) or 1
    ux, uy = dx / n, dy / n
    M.arrow(c, mx - ux * 60, my - uy * 60, mx + ux * 60, my + uy * 60, cor or E.COR, q, 7, 22)


def plano_face(c, pts, idx, a=1.0, cor=None, k=0.45):
    """o plano da face idx: paralelogramo translúcido maior que a face, com borda tracejada (folha sem bordas)"""
    if a <= 0:
        return
    A, B, D = pts[idx[0]], pts[idx[1]], pts[idx[3]]
    u = (B[0] - A[0], B[1] - A[1])
    v = (D[0] - A[0], D[1] - A[1])
    O = (A[0] - u[0] * k - v[0] * k, A[1] - u[1] * k - v[1] * k)
    s = 1 + 2 * k
    P = [O, (O[0] + u[0] * s, O[1] + u[1] * s), (O[0] + u[0] * s + v[0] * s, O[1] + u[1] * s + v[1] * s), (O[0] + v[0] * s, O[1] + v[1] * s)]
    path = skia.Path(); path.addPoly(P, True)
    c.drawPath(path, M.paint(cor or E.COR, 0.13 * a))
    pt = M.paint(cor or E.COR, 0.5 * a, stroke=3)
    pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(path, pt)


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


def caixa(c, t, t0, x=280, y=860, a=560, b=320, h=320, **kw):
    """a caixa de sapato da aula; devolve os vértices"""
    return E.paralelepipedo(c, t, t0, x, y, a, b, h, **kw)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, a1, ps("nunca se encontram =", "i", 70) + [("paralelas?", "g", 74, COR)], W / 2, 190, "center", 0.1)
        def papel():
            E.foco(c, t, a1 + 0.3, 0.5, lambda q: (c.drawRect(skia.Rect.MakeXYWH(160, 330, 640, 460), M.paint("#FFFFFF", q)),
                                                    c.drawRect(skia.Rect.MakeXYWH(160, 330, 640, 460), M.paint(CINZA, q, stroke=2))))
            for k, y in enumerate((470, 650)):
                p = ease_io(prog(t, a1 + 0.6 + 0.3 * k, 0.6))
                if p > 0:
                    M.line(c, 200, y, 760, y, E.COR if k == 0 else TINTA, 1, 10, progress=p)
            E.foco(c, t, a1 + 1.4, 0.4, lambda q: centro(c, "no papel: sim", 480, 880, 56, "g", CERTO, q))
        papel()
        pts = caixa(c, t, b1, 1060, 820, 480, 280, 300)
        aresta(c, t, b1 + 0.8, pts[0], pts[1])
        aresta(c, t, b1 + 1.1, pts[4], pts[7], TINTA, tracejada=True)
        E.foco(c, t, b1 + 0.6, 0.4, lambda q: centro(c, "na caixa: nem sempre", 1400, 950, 56, "g", ERRADO, q))
        E.foco(c, t, c1, 0.5, lambda q: E.pilula(c, "um 3º tipo de reta", 1400, 330, 60, "g", a=q, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("2 arestas", "g", 104, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("de uma caixa:", "i", 90), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("dizer a", "i", 90) + [("posição", "g", 98, COR)], XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 880
    itens = (("s03.b", "no papel, se cruzam: concorrentes", "ângulo reto: perpendiculares"), ("s03.c", "aresta:", "encontro de 2 faces"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 54, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 680, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 940, "left", 0.12)


# ---------------- o plano ----------------
def b_plano(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")

    def folha():
        k = ease_io(prog(t, b4, 1.6))
        cx, cy = 560, 620
        w, h, sk = lerp(360, 760, k), lerp(200, 380, k), lerp(110, 220, k)
        P = [(cx - w / 2 + sk / 2, cy - h / 2), (cx + w / 2 + sk / 2, cy - h / 2), (cx + w / 2 - sk / 2, cy + h / 2), (cx - w / 2 - sk / 2, cy + h / 2)]
        q = ep(t, a4, 0.5)
        if q > 0:
            path = skia.Path(); path.addPoly(P, True)
            c.drawPath(path, M.paint(E.COR, 0.16 * q))
            pt = M.paint(E.COR, 0.6 * q, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
            c.drawPath(path, pt)
            for (x0, y0), (x1, y1) in ((P[0], P[1]), (P[1], P[2]), (P[2], P[3]), (P[3], P[0])):
                mx, my = (x0 + x1) / 2, (y0 + y1) / 2
                ux, uy = mx - cx, my - cy
                n = math.hypot(ux, uy) or 1
                M.arrow(c, mx, my, mx + ux / n * 70, my + uy / n * 70, E.COR, ep(t, b4 + 0.4, 0.4), 5, 18)
        E.frase(c, t, a4, [("o plano", "g", 92, COR)], 1120, 300)
        E.frase(c, t, b4, ps("uma folha", "i", 70) + [("sem bordas", "g", 70)], 1120, 430, "left", 0.1)
        E.frase(c, t, b4 + 0.9, ps("para todos os lados", "i", 64, TINTA2), 1120, 520, "left", 0.1)
        for k_, s_ in enumerate(("o chão", "uma parede", "o tampo da mesa")):
            E.frase(c, t, c4 + 0.5 * k_, [("•", "g", 60, COR)] + ps(s_, "i", 62), 1120, 680 + 80 * k_, "left", 0.1)
    fase(c, t, C["s04"], d4 - 0.1, folha)
    if t < d4 - 0.1:
        return
    pts = caixa(c, t, d4, 380, 820, 440, 260, 280)
    for k, idx in enumerate(((0, 1, 2, 3), (3, 2, 6, 7), (1, 5, 6, 2))):
        plano_face(c, pts, idx, ep(t, d4 + 0.8 + 0.5 * k, 0.5), k=0.35)
    E.frase(c, t, d4 + 0.3, ps("cada face", "i", 70) + [("num plano", "g", 74, COR)], 1360, 300, "center", 0.1)


# ---------------- paralelas, concorrentes e reversas ----------------
X = 1140


def b_posicoes(c, t, C, b):
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    pts = caixa(c, t, a5)
    # a escolhida fica o bloco inteiro
    E.frase(c, t, C["s05"] + 0.2, ps("uma caixa de sapato", "i", 66), 580, 200, "center", 0.1)

    # paralelas
    def par():
        plano_face(c, pts, (0, 1, 2, 3), ep(t, c6, 0.5), k=0.25)
        aresta(c, t, a6, pts[3], pts[2], TINTA)
        seta_dir(c, t, b6, pts[0], pts[1], off=(0, 50))
        seta_dir(c, t, b6 + 0.2, pts[3], pts[2], TINTA, off=(0, -50))
        E.frase(c, t, a6, ps("frente, em cima:", "i", 62), X, 300, "left", 0.1)
        E.frase(c, t, a6 + 0.8, [("nunca encontra", "g", 62)], X, 380, "left", 0.1)
        E.frase(c, t, b6, ps("mesma direção", "i", 62), X, 500, "left", 0.1)
        E.frase(c, t, c6, ps("mesmo plano: a face da frente", "i", 54, TINTA2), X, 590, "left", 0.1)
        E.foco(c, t, d6, 0.5, lambda q: E.pilula(c, "paralelas", 1460, 790, 90, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s06"], C["s07"] - 0.1, par)

    # concorrentes e perpendiculares
    def conc():
        aresta(c, t, a7, pts[1], pts[2], TINTA)
        if t >= b7:
            k = ease_back(prog(t, b7, 0.4))
            c.drawCircle(*pts[1], 18 * k, M.paint(E.COR))
        if t >= c7:
            reto(c, pts[1], pts[0], pts[2], 40, ep(t, c7, 0.4), E.COR)
        E.frase(c, t, a7, ps("em pé, na frente à direita:", "i", 58), X, 330, "left", 0.1)
        E.frase(c, t, a7 + 1.0, [("toca na ponta", "g", 62)], X, 420, "left", 0.1)
        E.foco(c, t, b7, 0.5, lambda q: E.pilula(c, "concorrentes", 1460, 620, 84, "g", a=q, cor=E.SOBRE))
        E.frase(c, t, c7, ps("canto reto:", "i", 62) + [("perpendiculares", "g", 62, COR)], 1460, 860, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, conc)

    # reversas
    if t >= C["s08"] - 0.1:
        aresta(c, t, a8, pts[4], pts[7], TINTA, tracejada=True)
        estica(c, t, b8, pts[0], pts[1], 0.35)
        estica(c, t, b8 + 0.3, pts[4], pts[7], 0.6)
        seta_dir(c, t, c8, pts[0], pts[1], off=(0, 50))
        seta_dir(c, t, c8 + 0.3, pts[4], pts[7], TINTA, off=(-50, 0))

        def tres():
            E.frase(c, t, a8, ps("em pé, no fundo à esquerda", "i", 58), X, 330, "left", 0.1)
            E.frase(c, t, b8, [("nunca encontra,", "g", 62)], X, 430, "left", 0.1)
            E.frase(c, t, b8 + 0.7, ps("mesmo esticando", "i", 58, TINTA2), X, 510, "left", 0.1)
            E.frase(c, t, c8, ps("uma vai para o lado,", "i", 62), X, 640, "left", 0.1)
            E.frase(c, t, c8 + 0.8, ps("a outra sobe", "i", 62), X, 720, "left", 0.1)
        fase(c, t, C["s08"], C["s09"] - 0.1, tres)
        if t >= C["s09"] - 0.1:
            E.foco(c, t, a9, 0.5, lambda q: E.pilula(c, "reversas", 1460, 320, 90, "g", a=q, cor=E.SOBRE))
            E.frase(c, t, b9, ps("não se cruzam", "i", 62), 1460, 480, "center", 0.1)
            E.frase(c, t, b9 + 0.8, ps("e não estão no", "i", 62) + [("mesmo plano", "g", 62, COR)], 1460, 560, "center", 0.1)
            # a folha que tenta passar pelas duas: a da frente tem a escolhida, mas a de trás fica fora
            plano_face(c, pts, (0, 1, 2, 3), ep(t, c9, 0.5) * (1 - ep(t, d9, 0.4)), k=0.2)
            E.foco(c, t, c9 + 0.5, 0.5, lambda q: E.selo(c, 1460, 740, 70 * ease_back(prog(t, c9 + 0.5, 0.5)), False, q))
            E.frase(c, t, c9 + 0.3, ps("nenhuma folha passa pelas duas", "i", 52, TINTA2), 1460, 870, "center", 0.08)
            E.frase(c, t, d9, ps("só existe", "i", 66) + [("no espaço", "g", 66, COR)], 1460, 990, "center", 0.1)
    aresta(c, t, b5, pts[0], pts[1])
    E.foco(c, t, b5 + 0.3, 0.4, lambda q: centro(c, "a escolhida", (pts[0][0] + pts[1][0]) / 2, pts[0][1] + 125, 52, "g", COR, q))
    if t < C["s06"]:
        E.frase(c, t, b5, ps("a da frente, embaixo,", "i", 62), X, 420, "left", 0.1)
        E.frase(c, t, b5 + 0.8, [("deitada", "g", 62, COR)], X, 510, "left", 0.1)


# ---------------- reta perpendicular a um plano ----------------
def b_perpendicular(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def na_caixa():
        pts = caixa(c, t, C["s10"])
        plano_face(c, pts, (0, 1, 5, 4), ep(t, a0, 0.5), k=0.3)
        aresta(c, t, a0, pts[1], pts[2])
        aresta(c, t, c0, pts[0], pts[1], TINTA, 10)
        aresta(c, t, c0 + 0.3, pts[1], pts[5], TINTA, 10)
        reto(c, pts[1], pts[2], pts[0], 40, ep(t, c0 + 0.5, 0.4), E.COR)
        reto(c, pts[1], pts[2], pts[5], 40, ep(t, c0 + 0.8, 0.4), E.COR)
        # mais retas do chão pelo pé
        if t >= b1:
            for k, (dx, dy) in enumerate(((-1, -0.35), (-0.7, -0.8), (0.4, -1))):
                P = pts[1]
                p = ease_io(prog(t, b1 + 0.2 * k, 0.6))
                M.line(c, P[0] - dx * 130, P[1] - dy * 130 * 0.45, P[0] + dx * 180, P[1] + dy * 180 * 0.45, TINTA2, 0.8, 4, dash=[12, 10], progress=p)
        def txt10():
            E.frase(c, t, a0, ps("a aresta em pé chega ao chão", "i", 56), X, 330, "left", 0.1)
            E.frase(c, t, b0, ps("como", "i", 58) + [("um poste na calçada", "g", 54)], X, 430, "left", 0.1)
            E.frase(c, t, c0, [("ângulo reto", "g", 62, COR)] + ps("com as 2", "i", 62), X, 560, "left", 0.1)
            E.frase(c, t, c0 + 0.8, ps("arestas do chão no pé dela", "i", 56, TINTA2), X, 640, "left", 0.1)
        fase(c, t, C["s10"], C["s11"] - 0.1, txt10)
        if t >= C["s11"] - 0.1:
            E.frase(c, t, a1, [("perpendicular", "g", 74, COR)], X, 330)
            E.frase(c, t, a1 + 0.6, ps("ao plano do chão", "i", 66), X, 420, "left", 0.1)
            E.frase(c, t, b1, ps("90° com toda reta do chão", "i", 56, TINTA2), X, 530, "left", 0.1)
            E.frase(c, t, b1 + 0.8, ps("que passa pelo pé", "i", 56, TINTA2), X, 600, "left", 0.1)
            E.frase(c, t, c1, ps("para testar:", "i", 62) + [("bastam 2", "g", 62, COR)], X, 740, "left", 0.1)
            E.frase(c, t, c1 + 0.8, ps("que se cruzam no pé", "i", 56, TINTA2), X, 820, "left", 0.1)
            E.foco(c, t, d1, 0.5, lambda q: E.selo(c, X + 40, 960, 44 * ease_back(prog(t, d1, 0.5)), True, q))
            E.frase(c, t, d1 + 0.2, [("perpendicular ao plano", "g", 56, CERTO)], X + 110, 980, "left", 0.1)
    fase(c, t, C["s10"], C["s12"] - 0.1, na_caixa)
    if t < C["s12"] - 0.1:
        return
    # o poste torto
    F = (620, 760)
    dz = (0.394 / 0.5, -0.308 / 0.5)  # direção do fundo (unitária na tela, aprox.)
    n = math.hypot(*dz)
    dz = (dz[0] / n, dz[1] / n)
    q = ep(t, C["s12"], 0.5)
    if q > 0:
        L1, L2 = 360, 260
        calc = [(F[0] - L1 - dz[0] * L2, F[1] - dz[1] * L2), (F[0] + L1 - dz[0] * L2, F[1] - dz[1] * L2),
                (F[0] + L1 + dz[0] * L2, F[1] + dz[1] * L2), (F[0] - L1 + dz[0] * L2, F[1] + dz[1] * L2)]
        path = skia.Path(); path.addPoly(calc, True)
        c.drawPath(path, M.paint(CINZA, 0.35 * q))
        c.drawPath(path, M.paint(TINTA2, 0.6 * q, stroke=3))
    E.foco(c, t, C["s12"] + 0.3, 0.4, lambda q_: E.escreve(c, "calçada", F[0] - 330, F[1] + 230, 46, "i", TINTA2, q_))
    tilt = 140 * ease_io(prog(t, a2, 0.8))
    top = (F[0] - dz[0] * tilt, F[1] - 380 - dz[1] * tilt)   # inclina para a frente (para quem olha)
    M.line(c, *F, *top, TINTA, ep(t, a2 - 0.3, 0.4), 16)
    c.drawCircle(*F, 12 * ep(t, a2 - 0.3, 0.4), M.paint(TINTA))
    if t >= b2:
        p = ease_io(prog(t, b2, 0.6))
        M.line(c, F[0] - 330, F[1], F[0] + 330, F[1], E.COR, 1, 7, progress=p)
        reto(c, F, top, (F[0] + 100, F[1]), 40, ep(t, b2 + 0.5, 0.4), CERTO)
    if t >= c2:
        p = ease_io(prog(t, c2, 0.6))
        A, B = (F[0] + dz[0] * 240, F[1] + dz[1] * 240), (F[0] - dz[0] * 240, F[1] - dz[1] * 240)
        M.line(c, *A, *B, ERRADO, 1, 7, progress=p)
        E.angulo(c, t, c2 + 0.5, F, B, top, None, r=70, cor=ERRADO)
    E.frase(c, t, a2, ps("um poste", "i", 66) + [("torto", "g", 70, COR)], 1520, 300, "center", 0.1)
    E.frase(c, t, b2, ps("com a linha de lado:", "i", 56) + [("90°", "g", 60, CERTO)], 1520, 470, "center", 0.1)
    E.frase(c, t, c2, ps("com a de frente:", "i", 56) + [("não", "g", 60, ERRADO)], 1520, 580, "center", 0.1)
    E.frase(c, t, d2, ps("uma reta só", "i", 62) + [("não garante", "g", 62, ERRADO)], 1520, 1000, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, [("o erro", "g", 80, ERRADO)] + ps("comum", "i", 80), W / 2, 170, "center", 0.12)
    pts = caixa(c, t, C["s13"], 240, 880, 520, 300, 300)
    aresta(c, t, b3, pts[0], pts[1])
    aresta(c, t, b3 + 0.3, pts[4], pts[7], TINTA, tracejada=True)
    estica(c, t, b3 + 0.6, pts[0], pts[1], 0.3)
    estica(c, t, b3 + 0.8, pts[4], pts[7], 0.5)
    seta_dir(c, t, c3, pts[0], pts[1], off=(0, 50))
    seta_dir(c, t, c3 + 0.3, pts[4], pts[7], TINTA, off=(-50, 0))
    E.frase(c, t, a3, ps("não se encontram =", "i", 62) + [("paralelas?", "g", 62, ERRADO)], 1370, 330, "center", 0.1)
    if t >= b3:
        E.risco(c, 1450, 360, 1700, 280, t, b3 + 1.0, largura=8)
    E.frase(c, t, b3, ps("nunca se encontram...", "i", 58), 1370, 470, "center", 0.1)
    E.frase(c, t, c3, ps("...mas uma vai para o lado e a outra sobe", "i", 50, TINTA2), 1370, 560, "center", 0.08)
    E.frase(c, t, d3, [("paralelas", "g", 66, COR)] + ps("=", "i", 62), 1370, 720, "center", 0.1)
    E.frase(c, t, d3 + 0.6, ps("não se cruzam", "i", 62) + [("+", "g", 62)], 1370, 810, "center", 0.1)
    E.frase(c, t, d3 + 1.2, [("mesmo plano", "g", 66, COR)], 1370, 900, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def caixinha(c, t, t0, s, cx, cy, size=60, cor=BR, fundo=None, w=None):
    """cartão do fluxograma no palco"""
    a = ep(t, t0, 0.4)
    if a <= 0:
        return
    w = w or E.larg(s, "g", size) + 80
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.95, w, size * 1.6), 26, 26)
    c.drawRRect(r, M.paint(fundo or "#FFFFFF", a * (1 if fundo else 0.08)))
    c.drawRRect(r, M.paint(cor, a, stroke=4))
    centro(c, s, cx, cy + size * 0.12, size, "g", cor if not fundo else E.SOBRE, a)


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def fluxo():
        E.frase(c, t, a4, ps("o atalho:", "i", 76, CLARO) + [("2 perguntas", "g", 80, BR)], W / 2, 180, "center", 0.12)
        caixinha(c, t, b4, "1. se cruzam, esticando?", 640, 360, 54)
        M.arrow(c, 1080, 340, 1260, 340, CLARO, ep(t, b4 + 0.5, 0.4), 6, 20, ep(t, b4 + 0.5, 0.4))
        E.foco(c, t, b4 + 0.5, 0.4, lambda q: E.escreve(c, "sim", 1120, 310, 40, "i", CLARO, q))
        caixinha(c, t, b4 + 0.7, "concorrentes", 1520, 360, 56, BR, E.COR)
        M.arrow(c, 640, 430, 640, 560, CLARO, ep(t, c4, 0.4), 6, 20, ep(t, c4, 0.4))
        E.foco(c, t, c4, 0.4, lambda q: E.escreve(c, "não", 660, 515, 40, "i", CLARO, q))
        caixinha(c, t, c4 + 0.2, "2. mesma direção?", 640, 650, 54)
        M.arrow(c, 980, 630, 1260, 630, CLARO, ep(t, c4 + 0.8, 0.4), 6, 20, ep(t, c4 + 0.8, 0.4))
        E.foco(c, t, c4 + 0.8, 0.4, lambda q: E.escreve(c, "sim", 1080, 600, 40, "i", CLARO, q))
        caixinha(c, t, c4 + 1.0, "paralelas", 1520, 650, 56, BR, E.COR)
        M.arrow(c, 640, 720, 640, 850, CLARO, ep(t, d4, 0.4), 6, 20, ep(t, d4, 0.4))
        E.foco(c, t, d4, 0.4, lambda q: E.escreve(c, "não", 660, 805, 40, "i", CLARO, q))
        caixinha(c, t, d4 + 0.4, "reversas", 640, 940, 60, BR, E.COR)
    fase(c, t, C["s14"], C["s15"] - 0.1, fluxo)

    def conta():
        # a caixa fica apagada; cada grupo acende na sua vez e depois baixa
        pt = skia.Paint(); pt.setAlphaf(0.35)
        c.saveLayer(None, pt)
        pts = caixa(c, t, C["s15"], 220, 860, 520, 300, 300, escuro=True)
        c.restore()
        aresta(c, t, C["s15"] + 0.4, pts[0], pts[1], BR, 16)
        vez = lambda t0, t1: 1.0 if t < t1 else 0.4
        for grupo, tg, t1, cor in ((PARAL, b5, c5, LILAS), (CONC, c5, d5, CLARO), (REV, d5, 1e9, CINZA_R)):
            for k, (i, j) in enumerate(grupo):
                aresta(c, t, tg + 0.2 * k, pts[i], pts[j], cor, 12, tracejada=4 in (i, j), a=vez(tg, t1))
        E.frase(c, t, a5, ps("cada aresta da caixa tem", "i", 64, CLARO), 1360, 250, "center", 0.1)
        for k, (tk, n, s_, cor) in enumerate(((b5, "3", "paralelas", LILAS), (c5, "4", "concorrentes", CLARO), (d5, "4", "reversas", CINZA_R))):
            y = 420 + 150 * k
            E.foco(c, t, tk, 0.4, lambda q, y=y, cor=cor: c.drawRect(skia.Rect.MakeXYWH(1080, y - 30, 60, 14), M.paint(cor, q)))
            E.frase(c, t, tk, [(n, "g", 84, BR)] + ps(s_, "i", 70, cor), 1170, y, "left", 0.1)
        E.frase(c, t, b5 + 0.4, ps("as 3 da mesma direção", "i", 44, CINZA_R), 1170, 470, "left", 0.08)
        E.frase(c, t, c5 + 0.4, ps("2 em cada ponta", "i", 44, CINZA_R), 1170, 620, "left", 0.08)
        E.frase(c, t, d5 + 0.4, ps("o que sobra das 11", "i", 44, CINZA_R), 1170, 770, "left", 0.08)
        E.formula_em(c, t, d5 + 1.0, "3 + 4 + 4 = 11", 1360, 940, 70, "g", BR, "center")
    fase(c, t, C["s15"], C["s16"] - 0.1, conta)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, a6, ps("a caixa só tem", "i", 70, CLARO) + [("3 direções", "g", 74, BR)], W / 2, 200, "center", 0.12)
    O = (560, 760)
    for k, ((dx, dy), s_) in enumerate((((380, 0), "lado"), ((250, -195), "fundo"), ((0, -360), "cima"))):
        q = ep(t, a6 + 0.4 + 0.3 * k, 0.5)
        M.arrow(c, *O, O[0] + dx, O[1] + dy, CLARO, q, 8, 24, q)
        E.foco(c, t, a6 + 0.6 + 0.3 * k, 0.4, lambda q_, dx=dx, dy=dy, s_=s_: centro(c, s_, O[0] + dx * 1.18, O[1] + dy * 1.18 + (56 if dy == 0 else 0), 52, "g", BR, q_))
    E.frase(c, t, a6 + 1.6, ps("4 arestas em cada", "i", 56, CLARO), 640, 900, "center", 0.1)
    E.piramide(c, t, b6, 1440, 760, 4, 200, 360, escuro=True)
    E.frase(c, t, b6, ps("na pirâmide:", "i", 60, CLARO) + [("não vale", "g", 60, BR)], 1440, 330, "center", 0.1)
    E.frase(c, t, c6, ps("use as", "i", 60, CLARO) + [("2 perguntas", "g", 60, BR)], 1440, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a7, ps("a escolhida:", "i", 64) + [("em pé, frente esquerda", "g", 58, COR)], XE, 330, passo=0.1)
    itens = ((b7, "1", "cima, no fundo, deitada"), (c7, "2", "em pé, fundo direita"), (d7, "3", "cima, lado esquerdo"))
    for k, (tk, n, s_) in enumerate(itens):
        y = 500 + 140 * k
        E.foco(c, t, tk, 0.5, lambda q, y=y, n=n: (E.bola(c, XE + 40, y - 22, 44, TINTA, q), centro(c, n, XE + 40, y, 54, "g", BR, q)))
        E.frase(c, t, tk + 0.1, ps(s_, "i", 60), XE + 110, y, "left", 0.1)
    E.frase(c, t, d7 + 1.0, ps("qual a posição de cada uma?", "i", 60, TINTA2), XE, 960, passo=0.1)

    def cx_():
        pts = caixa(c, t, C["s17"], 1130, 800, 440, 260, 280)
        aresta(c, t, a7, pts[0], pts[3])
        for tk, (i, j), n in ((b7, (7, 6), "1"), (c7, (5, 6), "2"), (d7, (3, 7), "3")):
            aresta(c, t, tk, pts[i], pts[j], TINTA, 11)
            mx, my = (pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2
            off = {"1": (0, -50), "2": (55, 0), "3": (-45, -40)}[n]
            E.foco(c, t, tk + 0.2, 0.4, lambda q, mx=mx, my=my, n=n, off=off: (E.bola(c, mx + off[0], my + off[1], 30, TINTA, q),
                                                                                centro(c, n, mx + off[0], my + off[1] + 14, 38, "g", BR, q)))
    E.saida(c, t, C["s18.a"] - 0.1, cx_)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9 = C["s19.a"], C["s19.b"]
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    pts = caixa(c, t, C["s19"], 220, 860, 520, 300, 320)
    aresta(c, t, C["s19"] + 0.4, pts[0], pts[3])
    vez = 1 if t < a0 else 2 if t < d0 else 3
    i, j = {1: (7, 6), 2: (5, 6), 3: (3, 7)}[vez]
    tk = {1: a9, 2: a0, 3: d0}[vez]
    aresta(c, t, tk, pts[i], pts[j], TINTA, 13)
    if vez == 1:
        seta_dir(c, t, a9 + 0.6, pts[0], pts[3], off=(-50, 0))
        seta_dir(c, t, a9 + 0.8, pts[7], pts[6], TINTA, off=(0, -50))
    if vez == 2:
        seta_dir(c, t, b0, pts[0], pts[3], off=(-50, 0))
        seta_dir(c, t, b0 + 0.2, pts[5], pts[6], TINTA, off=(50, 0))
    mx, my = (pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2
    off = {1: (-150, -45), 2: (55, 0), 3: (-45, -40)}[vez]
    E.foco(c, t, tk + 0.2, 0.4, lambda q: (E.bola(c, mx + off[0], my + off[1], 30, TINTA, q), centro(c, str(vez), mx + off[0], my + off[1] + 14, 38, "g", BR, q)))
    if vez == 3 and t >= e0:
        reto(c, pts[3], pts[0], pts[7], 40, ep(t, e0, 0.4), E.COR)
        c.drawCircle(*pts[3], 16 * ease_back(prog(t, d0 + 0.5, 0.4)), M.paint(E.COR))
    X0 = 1080
    for k, (tk_, n, s_, cor) in enumerate(((b9, "1", "reversas", TINTA), (c0, "2", "paralelas", TINTA), (e0, "3", "concorrentes", TINTA))):
        y = 330 + 200 * k
        E.foco(c, t, {0: a9, 1: a0, 2: d0}[k], 0.5, lambda q, y=y, n=n: (E.bola(c, X0 + 40, y - 22, 44, TINTA, q), centro(c, n, X0 + 40, y, 54, "g", BR, q)))
        E.foco(c, t, tk_, 0.5, lambda q, y=y, s_=s_: E.pilula(c, s_, X0 + 360, y - 22, 64, "g", a=q, cor=E.SOBRE))
        motivo = ("não toca; uma vai para o lado, a outra sobe", "não toca, mas sobe na mesma direção", "encosta no topo da escolhida")[k]
        E.frase(c, t, {0: a9 + 0.6, 1: a0 + 0.6, 2: d0 + 0.6}[k], ps(motivo, "i", 40, TINTA2), X0 + 100, y + 60, "left", 0.06)
    E.frase(c, t, e0 + 0.6, ps("e", "i", 58) + [("perpendiculares", "g", 58, COR)], X0 + 360, 860, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s21.a", ps("se cruzam:", "i", 66) + [("concorrentes", "g", 66, COR)]),
                 ("s21.b", ps("mesma direção:", "i", 66) + [("paralelas", "g", 66, COR)]),
                 ("s21.c", ps("nenhum dos casos:", "i", 66) + [("reversas", "g", 66, COR)]),
                 ("s21.d", ps("perpendicular ao plano:", "i", 60) + [("90° com 2 retas no pé", "g", 58, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 360 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a2, [("Volume", "g", 130, COR)], XE, 420)
    E.frase(c, t, a2 + 0.5, ps("do cubo e do bloco", "i", 76), XE, 530, passo=0.1)
    E.frase(c, t, b2, ps("quantos litros cabem em", "i", 62, TINTA2), XE, 660, passo=0.1)
    E.frase(c, t, b2 + 1.0, [("2 m × 1,5 m × 1 m", "g", 62)], XE, 750, passo=0.1)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c2 + 0.2, 0.4))
    E.frase(c, t, d2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, plano=b_plano, posicoes=b_posicoes, perpendicular=b_perpendicular, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
