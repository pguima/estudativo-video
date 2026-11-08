"""Visual — Estudativo · MAT-ESP-019: sólidos inscritos e circunscritos.
Mesma linguagem da trilha (MAT-ESP-001 a 013): sólidos do kit (E.cubo, E.esfera, E.cilindro, E.cone), arestas escondidas e
metade de trás das bases tracejadas, o elemento da vez na cor da matéria, resposta na esfera.
- UM DENTRO DO OUTRO (bola_no_cubo(), cone_no_cilindro()): o de fora em traço e o de dentro pintado na cor da matéria; as
  arestas do cubo são redesenhadas por cima da bola, para ela ficar "dentro".
- A FRASE QUE LIGA AS MEDIDAS = o corte de frente (corte_q()): o quadrado com o círculo encostado, o diâmetro na cor da
  matéria por cima da aresta. O mesmo corte, com o círculo errado em vermelho, mostra o erro de usar a aresta como raio.
- O QUE SOBRA = a parte entre os dois sólidos pintada (sobra_cil()): a lateral do cilindro na cor da matéria e o cone recortado.
- π = 3 em toda a aula, como no roteiro.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-019_solidos_inscritos_e_circunscritos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conceito", "cone", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
PAPEL = "#F4F2EC"
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cone e E.cilindro
KC, KS = 0.5 * math.cos(math.radians(38)), 0.5 * math.sin(math.radians(38))  # a profundidade de E.cubo
assert 6 ** 3 == 216 and 3 ** 3 == 27 and 4 * 27 == 108 and 216 - 108 == 108 and 4 * 216 == 864 and 864 == 4 * 216
assert 2 ** 2 == 4 and 3 * 4 == 12 and 12 * 6 == 72 and 72 // 3 == 24 and 72 - 24 == 48 and 72 * 2 // 3 == 48
assert 3 ** 2 == 9 and 3 * 9 == 27 and 27 * 10 == 270 and 270 // 3 == 90 and 270 - 90 == 180 and 90 * 2 == 180


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³√π→") else est, size * (0.92 if any(ch in w for ch in "²³√π→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def alfa(c, a, fn):
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def ponto(c, t, t0, P, r=13, cor=None):
    k = ease_back(prog(t, t0, 0.35))
    if k > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR))


# ================= peças desta aula =================
def centro_cubo(x, y, a):
    """o centro do E.cubo na tela: (x, y) = canto de baixo à esquerda da frente, a = aresta em px"""
    return x + a / 2 + KC * a / 2, y - a / 2 - KS * a / 2


def bola_no_cubo(c, t, t0, x, y, a, tb=None, medida=None, size=52, cor_b=None):
    """o cubo de aresta a com a bola encostada nas seis faces (a bola entra em tb)"""
    tb = t0 + 0.6 if tb is None else tb
    E.cubo(c, t, t0, x, y, a, medida, size=size, preenche=0.06)
    cx, cy = centro_cubo(x, y, a)
    E.esfera(c, t, tb, cx, cy, a / 2, cor=cor_b, preenche=0.6)
    if t >= tb:
        E.cubo(c, t, t0, x, y, a, preenche=0.0)  # as arestas por cima: a bola fica dentro
    return cx, cy


def topo(cy, h):
    return cy - h * COS


def tampa(c, cx, cy, r, a=1.0, cor=None, alfa_=0.55):
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))


def lateral_cil(cx, cy, r, h):
    ry, ct = r * SEN, topo(cy, h)
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    return p


def lateral_cone(cx, cy, r, h):
    ry, hy = r * SEN, h * COS
    yt = -ry * ry / hy
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    at = math.degrees(math.atan2(yt / ry, xt / r))
    p = skia.Path()
    p.moveTo(cx, cy - hy); p.lineTo(cx - xt, cy + yt)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - at, -(180 - 2 * at), False)
    p.close()
    return p


def cone_no_cilindro(c, t, t0, cx, cy, r, h, tc=None, raio=None, altura=None, tm=None, size=52):
    """o cilindro em traço e o cone pintado dentro: base no fundo, ponta no centro da tampa (o cone entra em tc)"""
    tc = t0 + 0.6 if tc is None else tc
    E.cilindro(c, t, t0, cx, cy, r, h, raio, altura, preenche=0.12, size=size, tm=tm)
    E.cone(c, t, tc, cx, cy, r, h, preenche=0.75)


def sobra_cil(c, cx, cy, r, h, a):
    """o que sobra: o cilindro pintado, menos o cone"""
    if a <= 0:
        return
    p = lateral_cil(cx, cy, r, h)
    ct = topo(cy, h)
    p.addOval(skia.Rect.MakeXYWH(cx - r, ct - r * SEN, 2 * r, 2 * r * SEN))
    q = skia.Op(p, lateral_cone(cx, cy, r, h), skia.PathOp.kDifference_PathOp)
    if q is not None:
        c.drawPath(q, M.paint(E.COR, 0.42 * a))


def corte_q(c, t, t0, cx, cy, L, r=None, cor=None, a=1.0, tq=None, preenche=0.28):
    """o corte de frente: o quadrado de lado L (o cubo) e o círculo de raio r (a bola) no mesmo centro"""
    r = L / 2 if r is None else r
    p = ease_io(prog(t, t0, 0.7))
    if p > 0 and a > 0:
        path = skia.Path(); path.addRect(skia.Rect.MakeXYWH(cx - L / 2, cy - L / 2, L, L))
        c.drawRect(skia.Rect.MakeXYWH(cx - L / 2, cy - L / 2, L, L), M.paint(TINTA2, 0.06 * a))
        pt = M.paint(TINTA, a, stroke=6)
        pt.setPathEffect(skia.DashPathEffect.Make([4 * L * p + 1, 4 * L + 10], 0))
        c.drawPath(path, pt)
    tq = t0 + 0.5 if tq is None else tq
    q = ease_back(prog(t, tq, 0.6))
    if q > 0 and a > 0:
        c.drawCircle(cx, cy, r * q, M.paint(cor or E.COR, preenche * a))
        c.drawCircle(cx, cy, r * q, M.paint(cor or E.COR, a, stroke=6))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        bola_no_cubo(c, t, a1, 230, 920, 500, a1 + 0.9, "6 cm", 58)
        X = 1360
        E.frase(c, t, a1 + 0.3, ps("uma bola numa", "i", 70) + [("caixa cúbica", "g", 72, COR)], X, 240, "center", 0.1)
        E.frase(c, t, a1 + 1.5, ps("encostando em todas as paredes", "i", 54, TINTA2), X, 330, "center", 0.08)
        E.frase(c, t, b1, ps("quanto fica", "i", 92) + [("vazio?", "g", 96, COR)], X, 520, "center", 0.12)
        E.foco(c, t, c1, 0.4, lambda q: centro(c, "com π = 3", X, 690, 60, "g", TINTA2, q))
        bola_txt(c, t, c1 + 0.4, "metade", X, 860, 150, 74)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.2, ps("um sólido", "i", 88) + [("dentro", "g", 100, COR)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 1.8, ps("do outro", "i", 88), XE, 550, passo=0.14)
        E.frase(c, t, tb, ps("e", "i", 88) + [("o que sobra", "g", 100, COR)], XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 80), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w, hh, dy, y0 = 900, 920, 170, 205, 120
    itens = (("s03.b", "cubo:", "V = a³"), ("s03.c", "esfera:", "f{4πr^3}{3} → 4r^3  (π = 3)"),
             ("s03.d", "cone = um terço do cilindro:", "f{1}{3} · área do fundo · h"), ("s03.e", "o que sobra:", "de fora − de dentro"))
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 66, "left", 0.08)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 40, y + 140 if "f{" not in l2 else y + 124, 52, "g", COR)
    alvo = [y0 + i * dy + hh - 26 for i in range(4)]
    py = alvo[0]
    for i, k in enumerate(("s03.c", "s03.d", "s03.e")):
        py = lerp(py, alvo[i + 1], ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.e"], C["s03.end"], 0.8), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 1010, "left", 0.1)


# ---------------- inscrito e circunscrito ----------------
def b_conceito(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    x, y, a = 200, 900, 500
    cx, cy = bola_no_cubo(c, t, C["s04"], x, y, a, a4 + 0.3)
    # os seis pontos de contato, no meio de cada face
    toques = [(cx - a / 2, cy), (cx + a / 2, cy), (cx, cy - a / 2), (cx, cy + a / 2),
              (cx - KC * a / 2, cy + KS * a / 2), (cx + KC * a / 2, cy - KS * a / 2)]
    for i, P in enumerate(toques):
        ponto(c, t, b4 + 0.4 + 0.18 * i, P, 15)
    if t >= c4:
        E.cubo(c, t, c4, x, y, a, preenche=0.0, cor=TINTA2, largura=10)
    X = 1330
    E.frase(c, t, a4, [("inscrito", "g", 100, COR)], X, 220, "center", 0.1)
    E.frase(c, t, a4 + 0.6, ps("por dentro, encostando", "i", 56), X, 300, "center", 0.08)
    E.frase(c, t, b4, ps("a bola toca as", "i", 56) + [("6 faces", "g", 60, COR)], X, 410, "center", 0.1)
    E.frase(c, t, c4, ps("o cubo, por fora, é", "i", 56), X, 540, "center", 0.1)
    E.frase(c, t, c4 + 0.8, [("circunscrito", "g", 84, TINTA2)], X, 630, "center", 0.1)
    E.frase(c, t, d4, ps("o maior que cabe:", "i", 52) + [("inscrito", "g", 56, COR)], X, 790, "center", 0.1)
    E.frase(c, t, e4, ps("a menor caixa que guarda:", "i", 52) + [("circunscrita", "g", 56, TINTA2)], X, 900, "center", 0.1)


# ---------------- a bola no cubo ----------------
QX, QY, QL = 560, 560, 560   # o corte de frente: 6 cm = 560 px


def b_esfera(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    X = 1400

    def frase_():
        E.frase(c, t, a5, ps("a frase antes da conta:", "i", 58), X, 210, "center", 0.1)
        E.frase(c, t, a5 + 1.2, ps("qual medida de um", "i", 56), X, 300, "center", 0.1)
        E.frase(c, t, a5 + 2.0, ps("é igual a qual do outro", "i", 56), X, 380, "center", 0.1)
    fase(c, t, a5, b5 + 0.2, frase_)

    def secao():
        bola_no_cubo(c, t, C["s05"], 130, 760, 240, C["s05"] + 0.4)
        E.saida(c, t, b5, lambda: E.foco(c, t, C["s05"] + 0.2, 0.4, lambda q: centro(c, "de frente", 330, 840, 50, "i", TINTA2, q)))
        corte_q(c, t, b5, QX + 300, QY + 20, QL)
        # a aresta embaixo e o diâmetro por cima
        y_ar = QY + 20 + QL / 2 + 46
        if t >= c5:
            p = ease_io(prog(t, c5, 0.6))
            M.line(c, QX + 300 - QL / 2, QY + 20, QX + 300 - QL / 2 + QL * p, QY + 20, E.COR, 1, 10)
            M.line(c, QX + 300 - QL / 2, y_ar, QX + 300 - QL / 2 + QL * p, y_ar, TINTA, 1, 6)
            ra = "aresta = 6" if t >= a6 + 0.2 else "aresta"
            rd = "diâmetro = 6" if t >= a6 else "diâmetro"
            E.foco(c, t, c5 + 0.5, 0.4, lambda q: centro(c, ra, QX + 300, y_ar + 62, 52, "g" if t >= a6 + 0.2 else "i", TINTA, q))
            E.foco(c, t, c5 + 0.3, 0.4, lambda q: centro(c, rd, QX + 300, QY + 20 - 24, 54, "g", COR, q))
        E.frase(c, t, c5 + 0.4, [("diâmetro", "g", 76, COR)] + ps("da bola", "i", 66), 1500, 600, "center", 0.1)
        E.frase(c, t, c5 + 1.0, ps("=", "g", 80), 1500, 700, "center", 0.1)
        E.frase(c, t, c5 + 1.2, [("aresta", "g", 76)] + ps("do cubo", "i", 66), 1500, 800, "center", 0.1)
        # medidas
        if t >= b6:
            p = ease_io(prog(t, b6, 0.5))
            M.line(c, QX + 300, QY + 20 + 50, QX + 300 + QL / 2 * p, QY + 20 + 50, TINTA2, 1, 8)
            ponto(c, t, b6, (QX + 300, QY + 20 + 50), 10, TINTA)
            E.foco(c, t, b6 + 0.3, 0.4, lambda q: centro(c, "raio 3", QX + 300 + QL / 4, QY + 20 + 130, 56, "g", TINTA, q))
        fcen(c, t, b6 + 0.2, "6 ÷ 2 = 3", 1500, 940, 72, COR)
    fase(c, t, C["s05"], C["s07"] - 0.1, secao)
    if t < C["s07"] - 0.1:
        return
    bola_no_cubo(c, t, C["s07"], 160, 900, 520, C["s07"] + 0.5, "6 cm", 56)
    X = 1420

    def contas():
        fcen(c, t, a7, "cubo: 6 × 6 × 6 = 216 cm³", X, 230, 66)
        fcen(c, t, b7, "bola (π = 3): 4r^3", X, 400, 66, COR)
        fcen(c, t, c7, "3³ = 27", X, 540, 72, COR)
        fcen(c, t, d7, "4 × 27 = 108 cm³", X, 680, 76, COR)
    fase(c, t, C["s07"], C["s08"] - 0.1, contas)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, ps("sobra =", "i", 64) + [("fora − dentro", "g", 66, COR)], X, 220, "center", 0.1)
    fcen(c, t, b8, "216 − 108", X - 190, 420, 80)
    bola_txt(c, t, b8 + 0.7, "108 cm³", X + 230, 400, 130, 54)
    E.foco(c, t, c8, 0.5, lambda q: E.barra_fatias(c, X - 330, 580, 660, 110, 2, 1, E.COR, q))
    E.frase(c, t, c8 + 0.3, [("metade", "g", 72, COR)] + ps("fica vazia", "i", 64), X, 790, "center", 0.1)
    E.frase(c, t, d8, ps("com o π de verdade: a bola ocupa", "i", 46, TINTA2), X, 920, "center", 0.08)
    E.frase(c, t, d8 + 1.0, ps("um pouco mais que a metade", "i", 46, TINTA2), X, 990, "center", 0.08)


# ---------------- a bola por fora ----------------
def b_circunscrita(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    x, y, a = 400, 760, 420
    pts = E.cubo(c, t, C["s09"], x, y, a, preenche=0.10)
    cx, cy = centro_cubo(x, y, a)
    R = math.dist(pts[0], pts[6]) / 2
    q = ep(t, a9, 0.8)
    if q > 0:
        E.esfera(c, t, a9, cx, cy, R, preenche=0.18)
    for i in range(8):
        ponto(c, t, a9 + 0.8 + 0.1 * i, pts[i], 12)
    if t >= b9:
        M.line(c, *pts[0], *pts[6], E.COR, 1, 10, dash=E.TRACO, progress=ease_io(prog(t, b9, 0.7)))
    X = 1520
    E.frase(c, t, a9, ps("a bola", "i", 66) + [("por fora", "g", 72, COR)], X, 220, "center", 0.1)
    E.frase(c, t, a9 + 1.0, ps("encosta nos", "i", 56) + [("8 cantos", "g", 60, COR)], X, 310, "center", 0.1)
    E.frase(c, t, b9, [("diâmetro", "g", 66, COR)] + ps("=", "g", 66), X, 480, "center", 0.1)
    E.frase(c, t, b9 + 0.8, ps("diagonal do cubo", "i", 64), X, 570, "center", 0.1)
    bola_txt(c, t, c9, "a · √3", X, 790, 150, 74)
    E.frase(c, t, c9 + 0.5, ps("aresta vezes raiz de três", "i", 44, TINTA2), X, 1000, "center", 0.08)


# ---------------- cone no cilindro ----------------
CX, CY, CR, CH = 470, 920, 160, 480   # o cilindro de raio 2 e altura 6 (80 px por cm)


def b_cone(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2 = C["s12.a"], C["s12.b"]
    ct = topo(CY, CH)
    E.cilindro(c, t, a0, CX, CY, CR, CH, preenche=0.12)
    tampa(c, CX, CY, CR, ep(t, b0, 0.4) * (1 - ep(t, C["s11"], 0.4)), alfa_=0.6)
    if t >= c0:
        ponto(c, t, c0, (CX, ct), 15)
    if t >= c0 + 0.2:
        E.cone(c, t, c0 + 0.2, CX, CY, CR, CH, preenche=0.75)
    sobra_cil(c, CX, CY, CR, CH, ep(t, a2, 0.6))
    if t >= a1:
        E.cilindro(c, t, 1e9, CX, CY, CR, CH, "2", "6", preenche=0, size=58, tm=a1)
    X = 1300

    def frase_():
        E.frase(c, t, a0, ps("um", "i", 70) + [("cone", "g", 76, COR)] + ps("dentro de um", "i", 70) + [("cilindro", "g", 76)], X, 230, "center", 0.1)
        E.frase(c, t, b0, ps("base = o", "i", 58) + [("fundo", "g", 62, COR)], X, 400, "center", 0.1)
        E.frase(c, t, c0, ps("ponta no", "i", 58) + [("centro da tampa", "g", 62, COR)], X, 510, "center", 0.1)
        E.foco(c, t, d0, 0.5, lambda q: E.pilula(c, "mesmo raio e mesma altura", X, 720, 60, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s10"], C["s11"] - 0.1, frase_)

    def contas():
        E.frase(c, t, a1, ps("raio", "i", 58) + [("2 cm,", "g", 60, COR)] + ps("altura", "i", 58) + [("6 cm,", "g", 60, COR)] + [("π = 3", "g", 60)],
                X, 210, "center", 0.1)
        fcen(c, t, b1, "fundo: 2² = 4,  3 × 4 = 12 cm²", X, 380, 62)
        fcen(c, t, c1, "cilindro: 12 × 6 = 72 cm³", X, 530, 68)
        fcen(c, t, d1, "cone: 72 ÷ 3 = 24 cm³", X, 680, 68, COR)
    fase(c, t, C["s11"], C["s12"] - 0.1, contas)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"] + 0.1, ps("sobra", "i", 66), X, 230, "center", 0.1)
    fcen(c, t, a2, "72 − 24", X - 200, 450, 84)
    bola_txt(c, t, a2 + 0.8, "48 cm³", X + 200, 430, 130, 58)
    fcen(c, t, b2, "48 = f{2}{3} · 72", X, 760, 96, COR)
    E.frase(c, t, b2 + 0.8, [("dois terços", "g", 60, COR)] + ps("do cilindro", "i", 56), X, 920, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    E.frase(c, t, a3, ps("usar a", "i", 60) + [("aresta", "g", 64, ERRADO)] + ps("como", "i", 60) + [("raio", "g", 64, ERRADO)], W / 2, 260, "center", 0.1)
    qx, qy, L = 540, 660, 290   # 6 cm = 290 px: a bola errada (raio 6) é o dobro da caixa
    certo = t >= e3
    corte_q(c, t, C["s13"] + 0.3, qx, qy, L, r=L / 2, tq=1e9)
    if not certo:
        corte_q(c, t, a3 + 0.4, qx, qy, L, r=L, cor=ERRADO, tq=a3 + 0.5, preenche=0.14)
        if t >= a3 + 0.9:
            M.line(c, qx, qy, qx, qy - L * ease_io(prog(t, a3 + 0.9, 0.5)), ERRADO, 1, 7)
            ponto(c, t, a3 + 0.9, (qx, qy), 9, ERRADO)
            E.foco(c, t, a3 + 1.2, 0.4, lambda q: E.escreve(c, "raio 6?", qx + 24, qy - 0.6 * L, 52, "g", ERRADO, q))
    else:
        corte_q(c, t, -9, qx, qy, L, r=L / 2, tq=e3 + 0.2)
        if t >= e3 + 0.4:
            M.line(c, qx, qy, qx, qy - L / 2 * ease_io(prog(t, e3 + 0.4, 0.4)), E.COR, 1, 7)
            ponto(c, t, e3 + 0.4, (qx, qy), 9, TINTA)
        E.foco(c, t, e3 + 0.5, 0.4, lambda q: E.escreve(c, "raio 3", qx + L / 2 + 24, qy - L / 4 + 16, 52, "g", COR, q))
    E.foco(c, t, C["s13"] + 0.6, 0.4, lambda q: centro(c, "6", qx, qy + L / 2 + 60, 56, "g", TINTA, q))
    X = 1360
    fcen(c, t, b3, "4 × 6³", X, 440, 84, ERRADO)
    fcen(c, t, c3, "4 × 216 = 864", X, 580, 84, ERRADO)
    E.frase(c, t, d3, [("4 vezes", "g", 66, ERRADO)] + ps("a caixa inteira!", "i", 60), X, 710, "center", 0.1)
    fcen(c, t, e3, "6 ÷ 2 = 3", X, 870, 88, COR)
    E.frase(c, t, e3 + 0.6, [("aresta", "g", 56)] + ps("=", "g", 56) + [("diâmetro", "g", 56, COR)], X, 980, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def icone_cone(c, cx, cy, s, a):
    """o corte do cone no cilindro: o retângulo e o triângulo dentro, em traço branco"""
    if a <= 0:
        return
    w, h = 0.8 * s, 1.1 * s
    tri = skia.Path(); tri.moveTo(cx - w / 2, cy + h / 2); tri.lineTo(cx, cy - h / 2); tri.lineTo(cx + w / 2, cy + h / 2); tri.close()
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint(E.COR, 0.8 * a))
    c.drawPath(tri, M.paint("#0A0820", a))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint(BR, a, stroke=5))
    c.drawPath(tri, M.paint(BR, a, stroke=5))


def icone_bola(c, cx, cy, s, a):
    if a <= 0:
        return
    L = s
    c.drawRect(skia.Rect.MakeXYWH(cx - L / 2, cy - L / 2, L, L), M.paint(E.COR, 0.8 * a))
    c.drawCircle(cx, cy, L / 2, M.paint("#0A0820", a))
    c.drawRect(skia.Rect.MakeXYWH(cx - L / 2, cy - L / 2, L, L), M.paint(BR, a, stroke=5))
    c.drawCircle(cx, cy, L / 2, M.paint(BR, a, stroke=5))


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5, f5 = (C[f"s15.{k}"] for k in "abcdef")

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 70, CLARO), W / 2, 190, "center", 0.1)
        E.frase(c, t, a4, ps("decore a", "i", 76, CLARO) + [("fração que sobra", "g", 80, BR)], W / 2, 300, "center", 0.1)
        E.foco(c, t, b4, 0.5, lambda q: icone_cone(c, 560, 560, 230, q))
        E.foco(c, t, b4 + 0.3, 0.4, lambda q: centro(c, "cone no cilindro", 560, 760, 50, "b", CLARO, q))
        E.foco(c, t, b4 + 0.8, 0.4, lambda q: E.formula(c, "sobra f{2}{3}", 560, 900, 90, "g", BR, q, "center"))
        E.foco(c, t, c4, 0.5, lambda q: icone_bola(c, 1360, 560, 230, q))
        E.foco(c, t, c4 + 0.3, 0.4, lambda q: centro(c, "bola no cubo, π = 3", 1360, 760, 50, "b", CLARO, q))
        E.foco(c, t, c4 + 0.8, 0.4, lambda q: E.formula(c, "sobra f{1}{2}", 1360, 900, 90, "g", BR, q, "center"))
        E.foco(c, t, d4, 0.5, lambda q: E.pilula(c, "calcule o de fora e tire a fração", W / 2, 1010, 50, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.saida(c, t, e5 - 0.1, lambda: E.frase(c, t, C["s15"] + 0.2, ps("funciona porque", "i", 64, CLARO), W / 2, 170, "center", 0.1))
    E.frase(c, t, e5, ps("não compensa quando", "i", 64, CLARO), W / 2, 260, "center", 0.1)

    def porque():
        fcen(c, t, a5, "cone = f{1}{3} do cilindro", 520, 360, 66, BR)
        fcen(c, t, a5 + 1.0, "sobra 1 − f{1}{3} = f{2}{3}", 520, 540, 66, CLARO)
        fcen(c, t, b5, "r = f{a}{2}", 1400, 340, 76, BR)
        fcen(c, t, c5, "(f{a}{2})³ = f{a³}{8}", 1400, 530, 76, CLARO)
        fcen(c, t, d5, "4 · f{a³}{8} = f{a³}{2}", 1400, 720, 76, BR)
        E.foco(c, t, d5 + 0.6, 0.4, lambda q: centro(c, "metade do cubo", 1400, 830, 52, "i", CLARO, q))
    fase(c, t, C["s15"], e5 - 0.1, porque)
    if t < e5 - 0.1:
        return
    E.foco(c, t, e5, 0.5, lambda a: E.selo(c, 330, 420, 52, False, a))
    E.frase(c, t, e5 + 0.1, ps("cone", "i", 62, CLARO) + [("mais baixo", "g", 66, BR)] + ps("que o cilindro", "i", 62, CLARO), 420, 445, "left", 0.1)
    E.foco(c, t, e5 + 1.6, 0.5, lambda a: E.selo(c, 330, 600, 52, False, a))
    E.frase(c, t, e5 + 1.7, ps("a prova manda usar", "i", 62, CLARO) + [("π = 3,14", "g", 66, BR)], 420, 625, "left", 0.1)
    E.foco(c, t, f5, 0.5, lambda a: E.pilula(c, "faça as duas contas", W / 2, 850, 66, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a6, ps("peça de madeira:", "i", 62) + [("cilindro", "g", 64, COR)], XE, 330, passo=0.1)
    E.frase(c, t, a6 + 1.2, ps("raio", "i", 62) + [("3 cm,", "g", 64, COR)] + ps("altura", "i", 62) + [("10 cm", "g", 64, COR)], XE, 430, passo=0.1)
    E.frase(c, t, b6, ps("tira o", "i", 62) + [("maior cone", "g", 64, COR)], XE, 560, passo=0.1)
    E.frase(c, t, b6 + 1.0, ps("mesma base, mesma altura", "i", 56, TINTA2), XE, 650, passo=0.1)
    E.frase(c, t, c6, [("π = 3", "g", 64, COR)], XE, 770, passo=0.1)
    E.frase(c, t, d6, ps("quantos cm³ viram", "i", 70) + [("serragem?", "g", 74, COR)], XE, 920, passo=0.1)

    def peca():
        cone_no_cilindro(c, t, a6, 1500, 900, 150, 500, b6, "3 cm", "10 cm", a6 + 0.6, 54)
    E.saida(c, t, C["s17.a"] - 0.1, peca)
    E.relogio(c, t, C["s17.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    px, py, pr, ph = 380, 920, 150, 500
    cone_no_cilindro(c, t, C["s18"], px, py, pr, ph, C["s18"] + 0.4, "3", "10", C["s18"] + 0.8, 54)
    sobra_cil(c, px, py, pr, ph, ep(t, b9, 0.6))
    X = 1250

    def cil():
        E.foco(c, t, a8, 0.5, lambda q: E.pilula(c, "mesmo raio e mesma altura", X, 220, 54, "g", a=q, cor=E.SOBRE))
        fcen(c, t, b8, "fundo: 3² = 9,  3 × 9 = 27", X, 420, 68)
        fcen(c, t, c8, "cilindro: 27 × 10 = 270 cm³", X, 580, 68, COR)
    fase(c, t, C["s18"], C["s19"] - 0.1, cil)
    if t < C["s19"] - 0.1:
        return
    fcen(c, t, a9, "cone: 270 ÷ 3 = 90", X, 220, 68)
    fcen(c, t, b9, "270 − 90", X - 220, 420, 80)
    bola_txt(c, t, b9 + 0.7, "180 cm³", X + 220, 400, 130, 54)
    fcen(c, t, c9, "atalho: f{2}{3} de 270", X, 650, 72, COR)
    fcen(c, t, c9 + 1.2, "270 ÷ 3 = 90", X - 220, 830, 64)
    fcen(c, t, d9, "90 × 2 = 180", X + 230, 830, 64, COR)
    E.foco(c, t, d9 + 1.0, 0.5, lambda a: E.selo(c, X - 110, 970, 50, True, a))
    E.frase(c, t, d9 + 1.1, [("bateu", "g", 66, CERTO)], X - 40, 995, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s20.a", ps("a frase:", "i", 66) + [("qual medida = qual", "g", 70, COR)]),
                 ("s20.b", ps("depois:", "i", 66) + [("fora − dentro", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 25, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 390, y, "left", 0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a1, [("mesma forma,", "g", 100, COR)], XE, 400)
    E.frase(c, t, a1 + 0.8, ps("tamanhos diferentes", "i", 84), XE, 510)
    E.frase(c, t, b1, ps("medidas × 2 →", "i", 60) + [("volume × 8", "g", 64, COR)], XE, 650, passo=0.1)
    E.frase(c, t, c1, ps("a ponta do cone:", "i", 60) + [("1/8", "g", 64, COR)], XE, 750, passo=0.1)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conceito=b_conceito, esfera=b_esfera, circunscrita=b_circunscrita,
              cone=b_cone, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
