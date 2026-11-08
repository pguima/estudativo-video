"""Visual — Estudativo · MAT-ESP-013: cone, geratriz, área e volume.
Mesma linguagem da trilha (MAT-ESP-001 a 012): sólidos do kit (E.cone, E.cilindro) com a metade de trás da base tracejada,
o elemento da vez na cor da matéria, a 2ª família em cinza, resposta na esfera.
- O CONE DESPEJA NO CILINDRO (gancho e volume): o cone cheio (lateral_cone() pintada) esvazia e a água do cilindro (agua())
  sobe um terço por vez, como a areia da pirâmide na caixa em MAT-ESP-011.
- O CORTE (geratriz): o triângulo retângulo dentro do cone (vértice, centro da base e a borda da direita), pintado na cor da
  matéria; catetos (altura e raio) em cinza grosso, hipotenusa (geratriz) em COR grosso, quadradinho no centro da base.
- O MOLDE DO CONE (leque): o círculo da base e o leque (setor de 216°, a lateral aberta, peça leque() de MAT-ESP-002), na
  escala certa (raio 3 e geratriz 5). A borda curva do leque e a volta da base acendem juntas; o resto do círculo de raio 5
  aparece tracejado para comparar.
- π fica escrito (12π, 15π) até o atalho; no atalho e na questão, π = 3.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-013_cone_geratriz_area_e_volume.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cone", "volume", "leque", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cone e E.cilindro
assert 3 ** 2 + 4 ** 2 == 25 and 5 ** 2 == 25 and 9 * 4 == 36 and 36 // 3 == 12
assert 2 * 3 == 6 and 2 * 5 == 10 and 3 * 25 // 5 == 15 and 15 == 3 * 5 and 15 + 9 == 24 and 360 * 3 // 5 == 216
assert 6 * 8 == 48 and 6 ** 2 + 8 ** 2 == 10 ** 2 and 6 * 10 == 60 and 12 * 3 == 36
assert 5 ** 2 + 12 ** 2 == 13 ** 2 and 5 * 13 == 65 and 65 * 3 == 195 and 25 * 12 == 300 and 300 == 100 * 3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, √ ou π vai na grotesca: a serifada não tem esses sinais)"""
    out = []
    for w in txt.split():
        g = any(ch in w for ch in "²³√π")
        out.append((w, "g" if g else est, size * (0.92 if g and est != "g" else 1), cor))
    return out


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


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


def alfa(c, a, fn):
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    """o vértice da vez: bolinha que salta (de MAT-ESP-001)"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


# ================= peças desta aula =================
def pontos_cone(cx, cy, r, h):
    """V = vértice, O = centro da base, P = borda da direita, L = borda da esquerda (na tela)"""
    return (cx, cy - h * COS), (cx, cy), (cx + r, cy), (cx - r, cy)


def tampa(c, cx, cy, r, a=1.0, cor=None, alfa_=0.55):
    """o círculo da base pintado: a elipse em (cx, cy)"""
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))


def lateral_cone(c, cx, cy, r, h, a=1.0, cor=None, alfa_=0.5):
    """a lateral do E.cone pintada por cima (a mesma silhueta da peça do kit)"""
    if a <= 0:
        return
    ry, hy = r * SEN, h * COS
    yt = -ry * ry / hy
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    at = math.degrees(math.atan2(yt / ry, xt / r))
    p = skia.Path()
    p.moveTo(cx, cy - hy); p.lineTo(cx - xt, cy + yt)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - at, -(180 - 2 * at), False)
    p.close()
    c.drawPath(p, M.paint(cor or CINZA2, alfa_ * a))


def agua(c, cx, cy, r, h, nivel, a=1.0):
    """a água dentro do E.cilindro até a fração nivel da altura: corpo e superfície"""
    if nivel <= 0 or a <= 0:
        return
    ry, hy = r * SEN, h * nivel * COS
    ct = cy - hy
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(E.COR, 0.38 * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(E.COR, 0.3 * a))
    pt = M.paint(E.COR, a, stroke=3)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)


def despeja(c, t, t_ini, t_fim, cone, cil, rotulos=None):
    """o cone cheio esvazia 3 vezes no cilindro; cone = (cx, cy, r, h), cil = (cx, cy, r, h). rotulos = (x, y0, dy) dos 1×, 2×, 3×"""
    T = max(0.8, (t_fim - t_ini) / 3)
    nivel, cheia = 0.0, 0.0
    for k in range(3):
        u = prog(t, t_ini + k * T, T)
        if u <= 0:
            break
        cheia = min(1.0, u * 2.5) if u < 0.5 else 1 - ease_io((u - 0.5) * 2)
        nivel = (k + ease_io(max(0.0, (u - 0.5) * 2))) / 3
        if u >= 1:
            cheia = 0.0
    lateral_cone(c, *cone, cheia, E.COR, 0.6)
    agua(c, *cil, nivel)
    if rotulos:
        x, y0, dy = rotulos
        for k in range(3):
            tk = t_ini + (k + 1) * T - 0.2
            E.foco(c, t, tk, 0.3, lambda q, k=k: (E.bola(c, x, y0 + dy * k, 40, a=q), centro(c, f"{k + 1}×", x, y0 + dy * k + 16, 44, "g", E.SOBRE, q)))


def leque(c, cx, cy, R, ini, varre, a=1.0, cor=None, p=1.0, borda=None):
    """setor de círculo (a lateral do cone aberta, de MAT-ESP-002): ângulos da tela, em graus. borda = 0..1 acende o arco"""
    if a <= 0 or p <= 0:
        return
    rc = skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R)
    path = skia.Path()
    path.moveTo(cx, cy)
    path.arcTo(rc, ini, varre * ease_io(p), False)
    path.close()
    c.drawPath(path, M.paint(cor or E.mix(E.COR, "#FFFFFF", 0.65), a))
    pt = M.paint(TINTA, a, stroke=5)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pt)
    if borda:
        c.drawArc(rc, ini, varre * ease_io(borda), False, M.paint(E.COR, a, stroke=14, cap_round=True))


def disco(c, cx, cy, r, a=1.0, cor=None, borda=None, ini=90):
    """o círculo da base do molde; borda = 0..1 acende a volta"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(cor or E.mix(E.COR, "#FFFFFF", 0.78), a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=5))
    if borda:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, 360 * ease_io(borda), False, M.paint(E.COR, a, stroke=14, cap_round=True))


def corte(c, t, t0, V, O, P, a=1.0, tc=None, th=None, rots=None, tr=None, size=58):
    """o triângulo do corte: pintado em t0; catetos (altura OV e raio OP) em cinza grosso em tc; hipotenusa VP em COR em th.
    rots = (raio, altura, geratriz) e tr = instantes de cada rótulo"""
    q = ep(t, t0, 0.5) * a
    if q > 0:
        p = skia.Path(); p.addPoly([V, O, P], True)
        c.drawPath(p, M.paint(E.COR, 0.28 * q))
        M.line(c, *V, *O, TINTA, q, 5, dash=E.TRACO)
        M.line(c, *O, *P, TINTA, q, 5, dash=E.TRACO)
        reto(c, O, P, V, 30, q)
    if tc is not None:
        aresta(c, t, tc, O, V, TINTA2, 11, a=a)
        aresta(c, t, tc + 0.3, O, P, TINTA2, 11, a=a)
    if th is not None:
        aresta(c, t, th, V, P, None, 13, a=a)
    if rots and tr:
        for s, (A, B, n), ti in zip(rots, ((O, P, (0, 1)), (O, V, (-1, 0)), (V, P, (1, -0.35))), tr):
            if s:
                E.foco(c, t, ti, 0.4, lambda q, s=s, A=A, B=B, n=n: E._cola(c, s, (A[0] + B[0]) / 2, (A[1] + B[1]) / 2, n[0], n[1], 18, size, "g",
                                                                            COR if B == P and A == V else TINTA, q * a))


# ---------------- gancho ----------------
PX, BX, GY, GR, GH = 470, 1050, 900, 170, 440   # o cone e o cilindro do gancho


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.cilindro(c, t, a1, BX, GY, GR, GH)
        E.foco(c, t, a1 + 0.6, 0.4, lambda q: centro(c, "cilindro", BX, GY + 130, 54, "g", TINTA, q))
        E.cone(c, t, b1, PX, GY, GR, GH)
        E.foco(c, t, b1 + 0.6, 0.4, lambda q: centro(c, "cone", PX, GY + 130, 54, "g", COR, q))
        E.frase(c, t, b1 + 0.8, ps("mesma", "i", 64) + [("boca", "g", 68, COR)] + ps("e mesma", "i", 64) + [("altura", "g", 68, COR)],
                W / 2, 200, "center", 0.1)
        despeja(c, t, b1 + 2.2, c1, (PX, GY, GR, GH), (BX, GY, GR, GH), (1560, 420, 130))
        E.frase(c, t, c1, [("3 vezes", "g", 80, COR)], 1560, 880, "center", 0.1)
        E.frase(c, t, c1 + 0.5, ps("certinho", "i", 60), 1560, 970, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), ps("a", "i", 90) + [("geratriz", "g", 104, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("o", "i", 90) + [("volume", "g", 104, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("e a", "i", 90) + [("área lateral", "g", 104, COR)], XE, 730, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "área do círculo:", "A = πr^2"), ("s03.c", "pirâmide =", "f{1}{3} do prisma"),
             ("s03.d", "triângulo em pé na pirâmide:", "Pitágoras"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 80, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 166, 60, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- o que é cone (e o corte) ----------------
KX, KY, KR, KH = 500, 900, 240, 600   # o cone grande: raio 3 e altura 4 (80 px por unidade; a altura na tela encurta)


def b_cone(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    V, O, P, L = pontos_cone(KX, KY, KR, KH)
    E.cone(c, t, a4, KX, KY, KR, KH)
    tampa(c, KX, KY, KR, ep(t, b4, 0.4), alfa_=0.5)
    lateral_cone(c, KX, KY, KR, KH, ep(t, c4, 0.5) * (1 - 0.6 * ep(t, a5, 0.4)), alfa_=0.6)
    if t >= d4:
        pulsa = 1 + 0.6 * math.sin(min(1, prog(t, d4, 0.9)) * math.pi)
        vertice(c, t, d4, V, 15 * pulsa)
        E.foco(c, t, d4 + 0.2, 0.4, lambda q: E._cola(c, "vértice", *V, -1, -0.2, 26, 50, "g", COR, q))
    # a altura (tracejada, por dentro) e a geratriz (inclinada, pela lateral)
    if t >= a5:
        aresta(c, t, a5, V, O, TINTA2, 8, tracejada=True)
        reto(c, O, P, V, 30, ep(t, a5 + 0.4, 0.3))
        E.foco(c, t, a5 + 0.4, 0.4, lambda q: E._cola(c, "altura", O[0], lerp(O[1], V[1], 0.22), 1, 0, 16, 46, "g", TINTA2, q))
    if t >= b5:
        aresta(c, t, b5, V, P, None, 12)
        E.foco(c, t, b5 + 0.4, 0.4, lambda q: E._cola(c, "geratriz", (V[0] + P[0]) / 2, (V[1] + P[1]) / 2, 1, -0.3, 22, 54, "g", COR, q))
    X = 1060

    def que_e():
        E.frase(c, t, a4, [("cone", "g", 96, COR)], X, 240, "left", 0.1)
        E.frase(c, t, b4, ps("base:", "i", 60) + [("um círculo", "g", 62, COR)], X, 380, "left", 0.1)
        E.frase(c, t, c4, ps("lateral curva que", "i", 58) + [("afina", "g", 60, TINTA2)], X, 500, "left", 0.1)
        E.frase(c, t, d4, ps("até um ponto: o", "i", 58) + [("vértice", "g", 60, COR)], X, 600, "left", 0.1)
        E.frase(c, t, lerp(d4, C["s04.end"], 0.3), ps("casquinha, funil, chapéu de festa", "i", 50, TINTA2), X, 740, "left", 0.08)
    fase(c, t, C["s04"], C["s05"] - 0.1, que_e)

    def partes():
        E.frase(c, t, a5, [("altura:", "g", 62, TINTA2)] + ps("em pé, por dentro", "i", 58), X, 300, "left", 0.1)
        E.frase(c, t, a5 + 0.8, ps("do vértice ao centro da base", "i", 48, TINTA2), X, 380, "left", 0.08)
        E.frase(c, t, b5, [("geratriz:", "g", 62, COR)] + ps("inclinada, pela lateral", "i", 58), X, 520, "left", 0.1)
        E.frase(c, t, b5 + 0.8, ps("do vértice à borda da base", "i", 48, TINTA2), X, 600, "left", 0.08)
        E.frase(c, t, lerp(b5, c5, 0.6), ps("como a", "i", 52) + [("apótema", "g", 54)] + ps("da pirâmide", "i", 52), X, 740, "left", 0.08)
        E.frase(c, t, c5, [("geratriz", "g", 66, COR)] + ps("é mais comprida", "i", 60), X, 870, "left", 0.1)
        E.frase(c, t, c5 + 0.6, ps("que a", "i", 60) + [("altura", "g", 66, TINTA2)], X, 960, "left", 0.1)
    fase(c, t, C["s05"], C["s06"] - 0.1, partes)


def b_geratriz(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7, e7, f7 = (C[f"s07.{k}"] for k in "abcdef")
    V, O, P, L = pontos_cone(KX, KY, KR, KH)
    E.cone(c, t, C["s06"] - 1.0, KX, KY, KR, KH)
    # o plano do corte: uma faixa tracejada que desce de cima a baixo
    q = ease_io(prog(t, C["s06"] + 0.2, 1.0))
    if 0 < q and t < a6 + 0.6:
        y = lerp(V[1] - 60, KY + 80, q)
        M.line(c, KX - KR - 60, y, KX + KR + 60, y, E.COR, 1 - ep(t, a6 + 0.2, 0.4), 4, dash=E.TRACO)
    corte(c, t, a6, V, O, P, tc=b6, th=c6, rots=("3", "4", "5"), tr=(a7, a7 + 0.5, e7 + 0.4), size=64)
    X = 1380

    def nomes():
        E.frase(c, t, C["s06"] + 0.1, ps("corte ao meio", "i", 70), X, 240, "center", 0.1)
        E.frase(c, t, a6, [("triângulo retângulo", "g", 70, COR)], X, 380, "center", 0.1)
        E.frase(c, t, b6, [("catetos:", "g", 62, TINTA2)] + ps("altura e raio", "i", 60), X, 540, "center", 0.1)
        E.frase(c, t, c6, [("hipotenusa:", "g", 62, COR)] + ps("a geratriz", "i", 60), X, 680, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, nomes)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, a7, ps("raio", "i", 60) + [("3,", "g", 66, COR)] + ps("altura", "i", 60) + [("4", "g", 66, COR)], X, 220, "center", 0.1)
    fcen(c, t, b7, "3² = 9", X - 200, 380, 80)
    fcen(c, t, c7, "4² = 16", X + 200, 380, 80)
    fcen(c, t, d7, "9 + 16 = 25", X, 540, 84)
    fcen(c, t, e7, "r{25} = 5", X - 120, 720, 92, COR)
    bola_txt(c, t, e7 + 0.6, "g = 5", X + 230, 690, 100, 54)
    E.foco(c, t, f7, 0.5, lambda q: E.pilula(c, "terno 3, 4 e 5", X, 920, 62, "g", a=q, cor=E.SOBRE))


# ---------------- volume ----------------
def b_volume(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]

    def terco():
        E.frase(c, t, a8, ps("o mesmo que a", "i", 60) + [("pirâmide", "g", 64)] + ps("faz com o", "i", 60) + [("prisma", "g", 64)],
                W / 2, 200, "center", 0.1)
        E.prisma(c, t, a8 + 0.3, 330, 620, 4, 120, 250, preenche=0.1)
        E.piramide(c, t, a8 + 0.5, 330, 620, 4, 120, 250)
        E.foco(c, t, a8 + 1.2, 0.4, lambda q: E.formula(c, "pirâmide = f{1}{3} do prisma", 330, 760, 46, "g", TINTA2, q, "center"))
        E.cilindro(c, t, b8, 1000, 860, 170, 430, preenche=0.3)
        E.cone(c, t, b8 + 0.2, 1500, 860, 170, 430)
        E.foco(c, t, b8 + 0.6, 0.4, lambda q: (centro(c, "cilindro", 1000, 990, 50, "g", TINTA, q), centro(c, "cone", 1500, 990, 50, "g", COR, q)))
        E.foco(c, t, b8 + 0.8, 0.4, lambda q: E.formula(c, "cone = f{1}{3} do cilindro", 1250, 330, 70, "g", COR, q, "center"))
        despeja(c, t, c8, C["s09"] - 0.4, (1500, 860, 170, 430), (1000, 860, 170, 430), (1250, 500, 120))
    fase(c, t, C["s08"], C["s09"] - 0.1, terco)
    if t < C["s09"] - 0.1:
        return
    E.cone(c, t, C["s09"], KX - 80, KY, KR, KH)
    V, O, P, L = pontos_cone(KX - 80, KY, KR, KH)
    tampa(c, KX - 80, KY, KR, ep(t, b9, 0.4), alfa_=0.6)
    if t >= b9:
        aresta(c, t, b9 + 0.6, O, P, TINTA, 7)
        rr = "r = 3" if t >= C["s10"] else "r"
        E.foco(c, t, b9 + 0.8, 0.4, lambda q: E._cola(c, rr, (O[0] + P[0]) / 2, O[1], 0, -1, 10, 56, "g", TINTA, q))
    if t >= c9:
        aresta(c, t, c9, V, O, TINTA2, 8, tracejada=True)
        hh = "h = 4" if t >= C["s10"] else "h"
        E.foco(c, t, c9 + 0.3, 0.4, lambda q: E._cola(c, hh, O[0], lerp(O[1], V[1], 0.32), 1, 0, 16, 56, "g", TINTA2, q))
    X = 1300

    def formula():
        fcen(c, t, a9, "V = f{πr² · h}{3}", X, 400, 130, COR)
        E.frase(c, t, b9, [("πr²", "g", 62, COR)] + ps("= área da base", "i", 58), X, 640, "center", 0.1)
        E.frase(c, t, b9 + 1.0, [("r", "g", 62, COR)] + ps("= raio da base", "i", 58), X, 740, "center", 0.1)
        E.frase(c, t, c9, [("h", "g", 62, COR)] + ps("= altura", "i", 58), X, 860, "center", 0.1)
    fase(c, t, C["s09"], C["s10"] - 0.1, formula)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.1, ps("raio", "i", 58) + [("3,", "g", 62, COR)] + ps("altura", "i", 58) + [("4", "g", 62, COR)], X, 220, "center", 0.1)
    fcen(c, t, a0, "base: π · 3² = 9π", X, 390, 80)
    fcen(c, t, b0, "9π × 4 = 36π", X, 550, 80, TINTA2)
    E.frase(c, t, b0 + 0.8, ps("o cilindro", "i", 52, TINTA2), X, 630, "center", 0.1)
    fcen(c, t, c0, "36π ÷ 3", X - 180, 840, 84)
    bola_txt(c, t, c0 + 0.6, "12π", X + 220, 815, 120, 80)


# ---------------- área lateral: o leque ----------------
S = 58                        # px por unidade no molde
LCX, LCY = 560, 352           # centro do leque
LR_, BR_ = 5 * S, 3 * S       # raio do leque (geratriz 5) e da base (raio 3)
VARRE = 360 * 3 / 5           # 216°
INI = 90 - VARRE / 2          # o leque aberto para baixo, simétrico
DCX, DCY = LCX, LCY + LR_ + BR_   # o círculo da base encostado no meio da borda


def molde(c, t, t0, tp, a=1.0, borda=None):
    """o cone aberto: círculo da base (t0) e leque que se abre (tp); borda = 0..1 acende a volta da base e a borda do leque"""
    E.foco(c, t, t0, 0.5, lambda q: disco(c, DCX, DCY, BR_, q * a, borda=borda, ini=-90))
    leque(c, LCX, LCY, LR_, INI, VARRE, a, p=prog(t, tp, 1.2), borda=borda)


def b_leque(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.saida(c, t, a1 + 0.3, lambda: E.cone(c, t, C["s11"] - 0.5, 560, 760, 190, 500))
    borda = prog(t, d1, 1.6) if t >= d1 else None
    molde(c, t, a1 + 0.4, b1 - 0.6, borda=borda)
    if t >= c1:
        ang = math.radians(INI)
        Q = (LCX + LR_ * math.cos(ang), LCY + LR_ * math.sin(ang))
        aresta(c, t, c1, (LCX, LCY), Q, None, 10)
        E.foco(c, t, c1 + 0.3, 0.4, lambda q: E._cola(c, "5", (LCX + Q[0]) / 2, (LCY + Q[1]) / 2, 0, -1, 10, 60, "g", COR, q))
        vertice(c, t, c1, (LCX, LCY), 12, TINTA)
    if t >= a2:
        aresta(c, t, a2, (DCX, DCY), (DCX + BR_, DCY), TINTA, 6)
        E.foco(c, t, a2 + 0.3, 0.4, lambda q: E._cola(c, "3", DCX + BR_ / 2, DCY, 0, -1, 8, 52, "g", TINTA, q))
    # o resto do círculo de raio 5, tracejado
    q = ease_io(prog(t, b2, 1.0))
    if q > 0:
        pt = M.paint(TINTA2, 1.0, stroke=5, cap_round=True)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawArc(skia.Rect.MakeXYWH(LCX - LR_, LCY - LR_, 2 * LR_, 2 * LR_), INI, -(360 - VARRE) * q, False, pt)
    X = 1380

    def abre():
        E.frase(c, t, a1, ps("abra o cone", "i", 66), X, 220, "center", 0.1)
        E.frase(c, t, b1, ps("lateral =", "i", 62) + [("leque", "g", 66, COR)], X, 350, "center", 0.1)
        E.frase(c, t, b1 + 0.6, ps("um setor de círculo", "i", 50, TINTA2), X, 430, "center", 0.08)
        E.frase(c, t, c1, ps("raio do leque =", "i", 58) + [("geratriz 5", "g", 62, COR)], X, 580, "center", 0.1)
        E.frase(c, t, d1, ps("borda do leque =", "i", 58) + [("volta da base", "g", 62, COR)], X, 730, "center", 0.1)
        E.frase(c, t, d1 + 1.0, ps("ela contornava o círculo de baixo", "i", 48, TINTA2), X, 810, "center", 0.08)
    fase(c, t, C["s11"], C["s12"] - 0.1, abre)

    def fracao():
        fcen(c, t, a2, "volta da base: 2π · 3 = 6π", X, 260, 64, COR)
        fcen(c, t, b2, "raio 5 inteiro: 2π · 5 = 10π", X, 420, 64, TINTA2)
        fcen(c, t, c2, "f{6π}{10π} = f{3}{5}", X, 680, 110)
        E.frase(c, t, c2 + 0.8, ps("do círculo de raio 5", "i", 54), X, 850, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, fracao)
    if t < C["s13"] - 0.1:
        return
    E.foco(c, t, b3 + 0.6, 0.4, lambda q: centro(c, "15π", LCX, LCY + LR_ * 0.62, 70, "g", COR, q))
    tr, tf = lerp(b3, c3, 0.15), lerp(b3, c3, 0.55)

    def conta():
        E.frase(c, t, C["s13"] + 0.1, ps("no setor, a área acompanha a borda", "i", 50, TINTA2), X, 200, "center", 0.08)
        fcen(c, t, a3, "círculo de raio 5: π · 5² = 25π", X, 340, 60)
        fcen(c, t, b3, "f{3}{5} · 25π", X - 170, 520, 80)
        bola_txt(c, t, b3 + 0.6, "15π", X + 200, 495, 100, 70)
        fcen(c, t, tr, "15 = 3 · 5", X, 730, 80, COR)
        E.frase(c, t, tr + 0.8, [("raio", "g", 56)] + ps("vezes", "i", 54) + [("geratriz", "g", 56, COR)], X, 820, "center", 0.1)
        E.frase(c, t, tf, ps("fração do leque =", "i", 52, TINTA2), X - 50, 960, "center", 0.1)
        fcen(c, t, tf + 0.7, "f{r}{g}", X + 175, 978, 66, TINTA2)
    fase(c, t, C["s13"], c3 - 0.1, conta)
    if t < c3 - 0.1:
        return
    fcen(c, t, c3, "π · r · g", X, 300, 90)
    fcen(c, t, d3, "área lateral = πrg", X, 480, 96, COR)
    fcen(c, t, e3, "15π + 9π", X - 180, 760, 84)
    E.frase(c, t, e3 + 0.5, ps("lateral + base", "i", 46, TINTA2), X - 180, 840, "center", 0.08)
    bola_txt(c, t, e3 + 0.8, "24π", X + 220, 735, 110, 74)
    E.frase(c, t, e3 + 1.2, [("área total", "g", 54, COR)], X + 220, 910, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")
    cx, cy, r, h = 440, 920, 210, 560   # raio 6, altura 8 (35 px por unidade)
    V, O, P, L = pontos_cone(cx, cy, r, h)
    E.frase(c, t, C["s14"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 180, "center", 0.1)
    E.frase(c, t, a4, ps("usar a", "i", 62) + [("altura", "g", 66, ERRADO)] + ps("no lugar da", "i", 62) + [("geratriz", "g", 66, COR)],
            W / 2, 280, "center", 0.1)
    E.cone(c, t, b4, cx, cy, r, h)
    corte(c, t, b4 + 0.6, V, O, P, a=ep(t, d4, 0.4))
    if t >= b4:
        aresta(c, t, b4 + 0.5, V, O, ERRADO if t >= c4 else TINTA2, 8, tracejada=True)
        reto(c, O, P, V, 28, ep(t, b4 + 0.8, 0.3))
        E.foco(c, t, b4 + 0.6, 0.4, lambda q: (E._cola(c, "8", O[0], lerp(O[1], V[1], 0.42), -1, 0, 16, 58, "g", ERRADO if t >= c4 else TINTA, q),
                                               E._cola(c, "6", (O[0] + P[0]) / 2, O[1] + 16, 0, 1, 10, 58, "g", TINTA, q)))
        aresta(c, t, b4 + 0.9, O, P, TINTA, 6)
    if t >= d4:
        aresta(c, t, d4, V, P, None, 12)
        E.foco(c, t, d4 + 0.4, 0.4, lambda q: E._cola(c, "10", (V[0] + P[0]) / 2, (V[1] + P[1]) / 2, 1, -0.3, 20, 62, "g", COR, q))
    X = 1300
    fcen(c, t, c4, "π · 6 · 8 = 48π", X, 440, 80, ERRADO)
    E.foco(c, t, c4 + 0.8, 0.5, lambda q: E.selo(c, X + 360, 410, 44, False, q))
    E.frase(c, t, d4, ps("terno", "i", 58) + [("6, 8 e 10:", "g", 62, COR)] + ps("geratriz", "i", 58) + [("10", "g", 62, COR)], X, 600, "center", 0.1)
    fcen(c, t, e4, "π · 6 · 10", X - 180, 780, 80)
    bola_txt(c, t, e4 + 0.6, "60π", X + 220, 755, 100, 68)
    E.foco(c, t, f4, 0.5, lambda q: E.pilula(c, "altura → volume", X - 250, 960, 46, "g", a=q, cor=E.SOBRE, fundo=TINTA2))
    E.foco(c, t, f4 + 0.6, 0.5, lambda q: E.pilula(c, "geratriz → lateral", X + 250, 960, 46, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def um():
        E.frase(c, t, C["s15"] + 0.2, ps("atalho do", "i", 70, CLARO) + [("volume", "g", 74, BR)], W / 2, 190, "center", 0.1)
        fcen(c, t, a5, "π = 3", W / 2, 330, 90, CLARO)
        # V = 3 · r² · h ÷ 3, com os dois 3 riscados
        size, y = 120, 530
        partes = ("V = ", "3", " · r² · h ÷ ", "3")
        ws = [E.formula(None, s_, 0, 0, size, "g", a=0) for s_ in partes]
        x = W / 2 - sum(ws) / 2
        xs = []
        for w_ in ws:
            xs.append(x); x += w_
        E.foco(c, t, a5 + 0.4, 0.5, lambda q: [E.formula(c, s_, xx, y, size, "g", BR if k in (0, 2) else CLARO, q) for k, (s_, xx) in enumerate(zip(partes, xs))])
        if t >= b5:
            for k in (1, 3):
                E.risco(c, xs[k] - 8, y + 10, xs[k] + ws[k] + 8, y - size * 0.8, t, b5 + 0.3 * (k == 3), ERRADO, 10)
        fcen(c, t, c5, "V = r² · h", W / 2, 720, 120, BR)
        fcen(c, t, d5, "9 × 4", 720, 920, 90, CLARO)
        bola_txt(c, t, d5 + 0.6, "36", 1060, 890, 90, 76)
        fcen(c, t, e5, "12 × 3 = 36", 1460, 920, 76, CLARO)
        E.foco(c, t, e5 + 0.7, 0.5, lambda q: E.selo(c, 1460, 1010, 36, True, q))
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, C["s16"] + 0.2, ps("funciona porque", "i", 66, CLARO), W / 2, 220, "center", 0.1)
    fcen(c, t, a6, "× 3  e  ÷ 3  se desfazem", W / 2, 400, 96, BR)
    E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 380, 610, 46, False, a))
    E.frase(c, t, b6 + 0.1, ps("não compensa se a prova quer", "i", 54, CLARO), 450, 632, "left", 0.1)
    E.frase(c, t, b6 + 0.9, [("12π", "g", 64, BR)] + ps("escrito", "i", 56, CLARO) + ps("ou", "i", 56, CLARO) + [("π = 3,14", "g", 64, BR)],
            450, 750, "left", 0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "aí, faça a conta inteira", W / 2, 940, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
QX, QY, QR, QH = 1420, 920, 190, 560   # o chapéu: raio 5, altura 12


def b_questao(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s17"] + 1.2, ps("chapéu de festa:", "i", 62) + [("cone", "g", 66, COR)], XE, 320, passo=0.1)
    E.frase(c, t, a7, ps("raio", "i", 62) + [("5 cm", "g", 66, COR)], XE, 430, passo=0.1)
    E.frase(c, t, b7, ps("altura", "i", 62) + [("12 cm", "g", 66, COR)], XE, 530, passo=0.1)
    E.frase(c, t, c7, [("π = 3", "g", 66, COR)], XE, 630, passo=0.1)
    E.frase(c, t, d7, [("1)", "g", 62, COR)] + ps("quanto papel na lateral?", "i", 62), XE, 780, passo=0.1)
    E.frase(c, t, e7, [("2)", "g", 62, COR)] + ps("quantos cm³ cabem dentro?", "i", 62), XE, 890, passo=0.1)

    def chapeu():
        E.cone(c, t, C["s17"] + 1.0, QX, QY, QR, QH)
        V, O, P, L = pontos_cone(QX, QY, QR, QH)
        if t >= a7:
            aresta(c, t, a7, O, P, TINTA, 6)
            E.foco(c, t, a7 + 0.3, 0.4, lambda q: E._cola(c, "5 cm", (O[0] + P[0]) / 2, O[1] + QR * SEN, 0, 1, 8, 54, "g", COR, q))
        if t >= b7:
            aresta(c, t, b7, V, O, TINTA2, 6, tracejada=True)
            xc = QX + QR + 50
            aresta(c, t, b7, (xc, O[1]), (xc, V[1]), TINTA, 4)
            for yy in (O[1], V[1]):
                M.line(c, xc - 14, yy, xc + 14, yy, TINTA, ep(t, b7, 0.3), 4)
            E.foco(c, t, b7 + 0.3, 0.4, lambda q: E._cola(c, "12 cm", xc, (O[1] + V[1]) / 2, 1, 0, 16, 54, "g", COR, q))
    E.saida(c, t, C["s18.a"] - 0.1, chapeu)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    cx, cy, r, h = 380, 930, 200, 560
    V, O, P, L = pontos_cone(cx, cy, r, h)
    E.cone(c, t, C["s19"], cx, cy, r, h)
    corte(c, t, C["s19"] + 0.5, V, O, P)
    E.foco(c, t, C["s19"] + 0.8, 0.4, lambda q: (E._cola(c, "12", O[0], lerp(O[1], V[1], 0.42), -1, 0, 16, 58, "g", TINTA, q),
                                                 E._cola(c, "5", (O[0] + P[0]) / 2, O[1] + 16, 0, 1, 10, 58, "g", TINTA, q)))
    if t >= b9:
        aresta(c, t, b9, V, P, None, 12, a=1 - 0.7 * ep(t, c0, 0.4) * (1 - ep(t, d0, 0.4)))
        E.foco(c, t, b9 + 0.3, 0.4, lambda q: E._cola(c, "13", (V[0] + P[0]) / 2, (V[1] + P[1]) / 2, 1, -0.3, 20, 62, "g", COR, q))
    if t >= c0:
        aresta(c, t, c0, V, O, TINTA2, 12, a=1 - ep(t, d0, 0.4))
    X = 1240

    def lateral():
        E.frase(c, t, C["s19"] + 0.2, [("1)", "g", 64, COR)] + ps("primeiro a geratriz", "i", 62), X, 200, "center", 0.1)
        E.foco(c, t, a9, 0.5, lambda q: E.pilula(c, "terno 5, 12 e 13", X, 330, 58, "g", a=q, cor=E.SOBRE))
        fcen(c, t, b9, "g = 13", X, 490, 84, COR)
        fcen(c, t, c9, "π · 5 · 13 = 65π", X, 650, 80)
        fcen(c, t, d9, "65 × 3", X - 200, 860, 80)
        bola_txt(c, t, d9 + 0.6, "195 cm²", X + 200, 835, 135, 54)
    fase(c, t, C["s19"], C["s20"] - 0.1, lateral)
    if t < C["s20"] - 0.1:
        return
    E.frase(c, t, C["s20"] + 0.2, [("2)", "g", 64, COR)] + ps("volume, pelo atalho", "i", 62), X, 200, "center", 0.1)
    fcen(c, t, a0, "5² = 25", X, 360, 80)
    fcen(c, t, b0, "25 × 12", X - 200, 560, 80)
    bola_txt(c, t, b0 + 0.6, "300 cm³", X + 200, 535, 135, 54)
    E.foco(c, t, c0, 0.5, lambda q: E.pilula(c, "altura 12 → volume", X, 780, 56, "g", a=q, cor=E.SOBRE, fundo=TINTA2))
    E.foco(c, t, d0, 0.5, lambda q: E.pilula(c, "geratriz 13 → lateral", X, 910, 56, "g", a=q, cor=E.SOBRE))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s21.a", ps("geratriz:", "i", 66), "Pitágoras"), ("s21.b", ps("volume:", "i", 66), "f{1}{3} do cilindro"),
                 ("s21.c", ps("lateral:", "i", 66), "πrg"))
        for i, (k, l1, f_) in enumerate(itens):
            y = 440 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 460, y - 25, 52, a=a), centro(c, str(i + 1), 460, y - 4, 60, "g", E.SOBRE, a)))
            wl = E.frase(c, t, C[k] + 0.1, l1, 550, y, "left", 0.12)
            E.formula_em(c, t, C[k] + 0.5, f_, 550 + wl + 24, y, 74, "g", COR)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2, e2 = (C[f"s22.{k}"] for k in "abcde")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a2, ps("a", "i", 96) + [("esfera", "g", 120, COR)], XE, 420)
    E.frase(c, t, b2, [("área", "g", 66, COR)] + ps("e", "i", 64) + [("volume", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, c2, ps("reservatório de raio", "i", 60) + [("3 m", "g", 64, COR)], XE, 660, passo=0.1)
    E.esfera(c, t, a2, 1560, 640, 190, "3 m", size=52, tm=c2)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 290, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(560, 315, p), ep(t, d2 + 0.2, 0.4))
    E.frase(c, t, e2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cone=b_cone, geratriz=b_geratriz, volume=b_volume, leque=b_leque,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
