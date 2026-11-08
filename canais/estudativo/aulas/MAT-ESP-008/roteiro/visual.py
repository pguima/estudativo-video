"""Visual — Estudativo · MAT-ESP-008: cilindro, área e volume.
Mesma linguagem da trilha (MAT-ESP-001 a 007): sólidos do kit (E.cilindro) com a metade de trás da base tracejada, o elemento
da vez na cor da matéria, resposta na esfera.
- Tampa e fundo pintados em COR (tampa()), a lateral curva em CINZA2 (lateral()); o raio e a altura saem das peças do kit.
- VOLUME = discos empilhados (discos()): as camadas com a forma da base, como as fatias do prisma em MAT-ESP-007.
- ÁREA = a lata aberta como um molde: as duas tampas e o rótulo que desenrola num retângulo de largura 2πr (rotulo_lata(),
  copiado de MAT-ESP-002), com a área escrita em cada parte.
- DOBRAR O RAIO = o fundo visto de cima: o círculo de raio 10 com o de raio 5 dentro (fundos()).
- π = 3 em toda a aula, como no roteiro.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-008_cilindro_area_e_volume.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cilindro", "volume", "dobro", "area", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
PI = 3
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cilindro
assert 5 ** 2 == 25 and PI * 25 == 75 and 75 * 10 == 750 and PI * 10 ** 2 == 300 and 300 == 4 * 75
assert 2 * PI * 5 == 30 and 30 * 10 == 300 and 2 * 75 == 150 and 300 + 150 == 450 and PI * 100 * 10 == 3000 and 3000 == 4 * 750
assert 5 + 10 == 15 and 30 * 15 == 450 and 4 ** 2 == 16 and PI * 16 == 48 and 48 * 10 == 480
assert 2 * PI * 4 == 24 and 4 + 10 == 14 and 24 * 14 == 336 and 24 * 10 == 240 and 2 * 48 == 96 and 240 + 96 == 336


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




# ================= peças desta aula =================
def alfa(c, a, fn):
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def topo(cy, h):
    """o centro da tampa na tela, para um E.cilindro de base em (cx, cy) e altura h px"""
    return cy - h * COS


def tampa(c, cx, cy, r, a=1.0, cor=None, alfa_=0.55):
    """um círculo da base (tampa ou fundo) pintado: a elipse em (cx, cy)"""
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))


def lateral(c, cx, cy, r, h, a=1.0, cor=None, alfa_=0.5):
    """a lateral curva pintada por cima do E.cilindro"""
    if a <= 0:
        return
    ry, ct = r * SEN, topo(cy, h)
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor or CINZA2, alfa_ * a))


def discos(c, t, ts, cx, cy, r, hs, gap=18):
    """o cilindro em camadas: cada disco tem a forma da base e entra caindo no instante ts[i]"""
    for i, ti in enumerate(ts):
        q = ep(t, ti, 0.4)
        if q > 0:
            y = cy - i * (hs + gap) * COS - (1 - ease_io(q)) * 40
            alfa(c, q, lambda y=y, ti=ti: E.cilindro(c, t, ti - 0.3, cx, y, r, hs, d=0.5))


def diametro(c, t, t0, cx, cy, r, rot, size=52, cor=None):
    """o diâmetro atravessando a tampa, com a medida em cima"""
    p = ease_io(prog(t, t0, 0.5))
    if p > 0:
        M.line(c, cx - r, cy, cx + r, cy, cor or ERRADO, 1, 7, progress=p)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, cx, cy - r * SEN - 20, size, "g", cor or ERRADO, a))


def rotulo_lata(c, t, x, y, w, h, r, pw=1.0, a=1.0, cor=None, tampas=1.0, cor_r=None, cor_t=None):
    """a lata aberta (de MAT-ESP-002): retângulo w x h que se desenrola da esquerda (pw = 0..1) e as duas tampas de raio r"""
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


def fundos(c, t, t0, t1, cx, cy, s, a=1.0):
    """o fundo visto de cima: o círculo de raio 5 (t0) e, por fora, o de raio 10 (t1); s = px por cm"""
    q1 = ease_back(prog(t, t1, 0.6))
    if q1 > 0:
        c.drawCircle(cx, cy, 10 * s * q1, M.paint(E.COR, 0.22 * a))
        c.drawCircle(cx, cy, 10 * s * q1, M.paint(TINTA, a, stroke=5))
        M.line(c, cx, cy, cx + 10 * s * q1, cy, E.COR, a, 6)
        E.foco(c, t, t1 + 0.4, 0.4, lambda q: centro(c, "10", cx + 7.5 * s, cy - 16, 50, "g", COR, q * a))
    q0 = ease_back(prog(t, t0, 0.5))
    if q0 > 0:
        c.drawCircle(cx, cy - 5 * s, 5 * s * q0, M.paint(TINTA2, 0.35 * a))
        c.drawCircle(cx, cy - 5 * s, 5 * s * q0, M.paint(TINTA, a, stroke=4))
        M.line(c, cx, cy - 5 * s, cx + 5 * s * q0, cy - 5 * s, TINTA, a, 4)
        E.foco(c, t, t0 + 0.3, 0.4, lambda q: centro(c, "5", cx + 2.5 * s, cy - 5 * s - 14, 44, "g", TINTA, q * a))


LX, LY, LR, LH = 330, 900, 100, 200   # a lata: raio 5, altura 10 (20 px por cm)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.cilindro(c, t, a1, LX, LY, LR, LH, "5", "10", size=50)
        E.frase(c, t, a1 + 0.3, ps("uma", "i", 72) + [("lata", "g", 76, COR)], 120, 200, "left", 0.1)
        E.foco(c, t, a1 + 0.8, 0.4, lambda q: centro(c, "raio 5, altura 10", LX, LY + 110, 44, "i", TINTA2, q))
        E.cilindro(c, t, b1, 800, LY, LR, 2 * LH)
        E.foco(c, t, b1 + 0.6, 0.4, lambda q: centro(c, "altura × 2", 800, LY + 110, 50, "g", TINTA, q))
        bola_txt(c, t, b1 + 1.0, "2 ×", 800, 240, 80, 60)
        E.cilindro(c, t, c1, 1450, LY, 2 * LR, LH)
        E.foco(c, t, c1 + 0.6, 0.4, lambda q: centro(c, "raio × 2", 1450, LY + 140, 50, "g", COR, q))
        bola_txt(c, t, d1, "4 ×", 1450, 420, 120, 84)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("quanto cabe", "g", 104, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), ps("num cilindro", "i", 90), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("e quanto", "i", 90) + [("material", "g", 104, COR)], XE, 740, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "prisma: volume =", "área da base × altura"), ("s03.c", "área do círculo:", "A = πr^2"),
             ("s03.d", "volta da circunferência:", "C = 2πr"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 80, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 162, 60, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- o que é cilindro ----------------
def b_cilindro(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    cx, cy, r, h = 520, 900, 210, 520
    ct = topo(cy, h)
    E.cilindro(c, t, a4, cx, cy, r, h)
    tampa(c, cx, cy, r, ep(t, b4 + 0.4, 0.4), alfa_=0.35)
    tampa(c, cx, ct, r, ep(t, b4, 0.4))
    lateral(c, cx, cy, r, h, ep(t, c4, 0.5), alfa_=0.55)
    if t >= d4:
        aresta(c, t, d4, (cx, ct), (cx, cy), largura=7, tracejada=True)
        E.foco(c, t, d4 + 0.4, 0.4, lambda a: E.escreve(c, "altura", cx + r + 24, (ct + cy) / 2 + 18, 54, "g", COR, a))
    X = 1060
    E.frase(c, t, a4, [("cilindro", "g", 96, COR)], X, 240, "left", 0.1)
    E.frase(c, t, a4 + 0.7, ps("um prisma de base", "i", 58) + [("redonda", "g", 60)], X, 330, "left", 0.1)
    E.frase(c, t, b4, [("2 círculos iguais:", "g", 60, COR)], X, 470, "left", 0.1)
    E.frase(c, t, b4 + 0.7, ps("a tampa e o fundo", "i", 56), X, 550, "left", 0.1)
    E.frase(c, t, c4, ps("ligados por uma", "i", 58) + [("lateral curva", "g", 60, TINTA2)], X, 680, "left", 0.1)
    E.frase(c, t, lerp(c4, d4, 0.45), ps("lata, cano, caixa-d'água redonda", "i", 50, TINTA2), X, 770, "left", 0.08)
    E.frase(c, t, d4, [("altura", "g", 60, COR)] + ps("= distância", "i", 56), X, 900, "left", 0.1)
    E.frase(c, t, d4 + 0.6, ps("entre a tampa e o fundo", "i", 56), X, 980, "left", 0.1)


# ---------------- volume ----------------
def b_volume(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    X = 1300

    def formula():
        discos(c, t, [a5 + 0.35 * i for i in range(5)], 450, 920, 200, 70)
        E.frase(c, t, C["s05"] + 0.2, ps("a ideia do", "i", 66) + [("prisma", "g", 70, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a5, ps("camadas com a", "i", 58) + [("forma da base", "g", 60, COR)], X, 320, "center", 0.1)
        E.frase(c, t, b5, ps("volume = área da base × altura", "i", 58), X, 460, "center", 0.1)
        E.frase(c, t, b5 + 1.4, ps("a base é um", "i", 58) + [("círculo", "g", 60, COR)], X, 545, "center", 0.1)
        fcen(c, t, c5, "V = πr² · h", X, 720, 130, COR)
        E.frase(c, t, d5, [("r", "g", 64, COR)] + ps("= raio da tampa", "i", 58), X, 870, "center", 0.1)
        E.frase(c, t, e5, [("h", "g", 64, COR)] + ps("= altura", "i", 58), X, 960, "center", 0.1)
    fase(c, t, C["s05"], C["s06"] - 0.1, formula)
    if t < C["s06"] - 0.1:
        return
    E.cilindro(c, t, C["s06"], LX + 60, LY, 1.5 * LR, 1.5 * LH, "5 cm", "10 cm", size=52)
    tampa(c, LX + 60, LY, 1.5 * LR, ep(t, c6, 0.5), alfa_=0.6)

    def lata():
        fcen(c, t, a6, "π = 3", X, 230, 76, COR)
        fcen(c, t, b6, "5² = 25", X, 380, 80)
        fcen(c, t, c6, "3 × 25 = 75 cm²", X, 520, 80)
        E.frase(c, t, c6 + 1.0, ps("o fundo", "i", 54, TINTA2), X, 600, "center", 0.1)
        fcen(c, t, d6, "75 × 10", X - 230, 820, 80)
        bola_txt(c, t, d6 + 0.6, "750 cm³", X + 190, 800, 140, 58)
    fase(c, t, C["s06"], C["s07"] - 0.1, lata)
    if t < C["s07"] - 0.1:
        return
    fcen(c, t, a7, "1 cm³ = 1 mL", X, 260, 100, COR)
    bola_txt(c, t, b7, "750 mL", X, 520, 150, 70)
    E.foco(c, t, c7, 0.5, lambda q: E.barra_fatias(c, X - 330, 760, 660, 110, 4, 3, E.COR, q))
    E.frase(c, t, c7 + 0.4, [("¾", "g", 70, COR)] + ps("de litro", "i", 62), X, 970, "center", 0.1)


# ---------------- o dobro e o quádruplo ----------------
def b_dobro(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    E.frase(c, t, C["s08"] + 0.2, ps("e o começo da aula?", "i", 70), W / 2, 180, "center", 0.1)
    # dobrar a altura: uma lata em cima da outra
    x, y = 330, 900
    E.cilindro(c, t, a8 - 0.5, x, y, LR, LH)
    q = ep(t, a8 + 0.3, 0.6)
    if q > 0:
        yy = y - LH * COS - (1 - ease_io(q)) * 80
        alfa(c, q, lambda: E.cilindro(c, t, a8 - 0.3, x, yy, LR, LH))
    E.foco(c, t, a8 + 0.5, 0.4, lambda a: (E.escreve(c, "10", x + LR + 20, y - LH * COS / 2 + 18, 50, "g", TINTA2, a),
                                          E.escreve(c, "10", x + LR + 20, y - 1.5 * LH * COS + 18, 50, "g", TINTA2, a)))
    E.frase(c, t, a8 + 0.8, [("20", "g", 60, COR)] + ps("camadas, não 10", "i", 52), x, 300, "center", 0.1)
    E.foco(c, t, a8 + 1.6, 0.4, lambda a: centro(c, "o dobro", x, 1040, 58, "g", COR, a))
    # dobrar o raio: o fundo visto de cima
    fx, fy, s = 1050, 600, 26
    fundos(c, t, b8 - 0.3, b8 + 0.3, fx, fy, s)
    X = 1640
    fcen(c, t, b8 - 0.1, "3 × 5² = 75", X, 420, 64, TINTA2)
    fcen(c, t, b8 + 0.8, "3 × 10² = 300", X, 540, 64, COR)
    fcen(c, t, c8, "300 = 4 × 75", X, 700, 72)
    E.foco(c, t, d8, 0.5, lambda a: E.pilula(c, "o raio entra ao quadrado", fx, 960, 48, "g", a=a, cor=E.SOBRE))
    bola_txt(c, t, c8 + 0.6, "4 ×", X, 860, 80, 56)


# ---------------- área ----------------
RX, RY, RW, RH, RR = 280, 470, 540, 180, 90   # a lata aberta: 30 x 10 e tampas de raio 5 (18 px por cm)


def b_area(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2 = C["s12.a"], C["s12.b"]
    X = 1320
    # a lata fecha (some) e abre no molde
    E.saida(c, t, a9 + 0.6, lambda: E.cilindro(c, t, C["s09"], 430, 760, 140, 280))
    tam = ep(t, a9 + 0.6, 0.5)
    rotulo_lata(c, t, RX, RY, RW, RH, RR, pw=prog(t, c9, 1.2), a=1.0 if t >= a9 + 0.6 else 0.0, tampas=tam,
                cor_t=E.mix(E.COR, "#FFFFFF", 0.45) if t >= b9 else None, cor_r=E.mix(TINTA2, "#FFFFFF", 0.72) if t >= c9 else None)
    cxT = RX + RW * 0.16
    if t >= a0:
        aresta(c, t, a0, (RX - 24, RY + RH), (RX - 24, RY), largura=8)
        E.foco(c, t, a0 + 0.3, 0.4, lambda q: E.escreve(c, "10", RX - 110, RY + RH / 2 + 18, 54, "g", COR, q))
    if t >= b0:
        aresta(c, t, b0, (RX, RY + RH + 26), (RX + RW, RY + RH + 26), largura=8)
        rot = "30" if t >= c0 + 0.6 else "2πr"
        E.foco(c, t, b0 + 0.3, 0.4, lambda q: E.formula(c, rot, RX + RW * 0.62, RY + RH + 90, 54, "g", COR, q, "center"))
    # as áreas escritas em cada parte
    E.foco(c, t, a1 + 0.3, 0.4, lambda q: centro(c, "300", RX + RW * 0.58, RY + RH / 2 + 22, 64, "g", TINTA, q))
    for k, cy in enumerate((RY - RR, RY + RH + RR)):
        E.foco(c, t, b1 + 0.3 + 0.2 * k, 0.4, lambda q, cy=cy: centro(c, "75", cxT, cy + 18, 52, "g", BR, q))

    def partes():
        E.frase(c, t, a9, ps("abra a lata:", "i", 66), X, 230, "center", 0.1)
        E.frase(c, t, b9, [("2 círculos,", "g", 66, COR)] + ps("tampa e fundo", "i", 60), X, 370, "center", 0.1)
        E.frase(c, t, c9, ps("e a", "i", 60) + [("lateral:", "g", 64, TINTA2)] + ps("um retângulo", "i", 60), X, 490, "center", 0.1)
    fase(c, t, C["s09"], C["s10"] - 0.1, partes)

    def largura():
        E.frase(c, t, a0, ps("altura do retângulo =", "i", 56) + [("10", "g", 62, COR)], X, 230, "center", 0.1)
        E.frase(c, t, b0, ps("largura = a volta:", "i", 56) + [("2πr", "g", 62, COR)], X, 360, "center", 0.1)
        E.frase(c, t, b0 + 1.2, ps("a lateral dava a volta na tampa", "i", 48, TINTA2), X, 440, "center", 0.08)
        fcen(c, t, c0, "2 × 3 × 5 = 30 cm", X, 600, 76)
    fase(c, t, C["s10"], C["s11"] - 0.1, largura)

    def soma():
        fcen(c, t, a1, "lateral: 30 × 10 = 300", X, 240, 64)
        fcen(c, t, b1, "tampa e fundo: 2 × 75 = 150", X, 370, 64, COR)
        fcen(c, t, c1, "300 + 150", X - 200, 590, 72)
        bola_txt(c, t, c1 + 0.6, "450 cm²", X + 200, 580, 130, 52)
    fase(c, t, C["s11"], C["s12"] - 0.1, soma)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"] + 0.2, ps("na fórmula:", "i", 62), X, 240, "center", 0.1)
    fcen(c, t, a2, "A = 2πr^2", X - 150, 420, 92, COR)
    E.frase(c, t, a2 + 0.6, ps("as duas bases", "i", 50, COR), X - 150, 500, "center", 0.1)
    fcen(c, t, b2, "+ 2πrh", X + 200, 420, 92, TINTA2)
    E.frase(c, t, b2 + 0.6, ps("a lateral", "i", 50, TINTA2), X + 200, 500, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    cx, cy, r, h = 420, 900, 200, 400
    E.frase(c, t, C["s13"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 180, "center", 0.1)
    E.frase(c, t, a3, ps("usar o", "i", 62) + [("diâmetro", "g", 66, ERRADO)] + ps("no lugar do", "i", 62) + [("raio", "g", 66, COR)],
            W / 2, 280, "center", 0.1)
    E.cilindro(c, t, b3, cx, cy, r, h, None, "10 cm", size=52)
    diametro(c, t, b3 + 0.5, cx, topo(cy, h), r, "10 cm de diâmetro", 46)
    X = 1300
    fcen(c, t, c3, "3 × 10² × 10 = 3.000", X, 470, 76, ERRADO)
    E.frase(c, t, d3, [("4 vezes", "g", 66, ERRADO)] + ps("o certo", "i", 62), X, 590, "center", 0.1)
    if t >= e3:
        ct = topo(cy, h)
        aresta(c, t, e3, (cx, ct), (cx + r, ct), largura=10)
    fcen(c, t, e3, "10 ÷ 2 = 5", X, 770, 84, COR)
    E.foco(c, t, e3 + 0.8, 0.5, lambda q: E.pilula(c, "raio 5", X, 920, 66, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("atalho da", "i", 70, CLARO) + [("área total", "g", 74, BR)], W / 2, 200, "center", 0.1)
        fcen(c, t, a4, "A = 2πr · (r + h)", W / 2, 400, 120, BR)
        fcen(c, t, b4, "2 × 3 × 5 = 30", 620, 620, 76, CLARO)
        fcen(c, t, c4, "5 + 10 = 15", 1300, 620, 76, CLARO)
        fcen(c, t, d4, "30 × 15", 760, 850, 84, BR)
        bola_txt(c, t, d4 + 0.6, "450", 1220, 830, 110, 70)
        E.frase(c, t, lerp(d4, C["s14.end"], 0.5), ps("duas contas pequenas", "i", 54, CLARO), 1220, 1010, "center", 0.1)
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("funciona porque", "i", 66, CLARO), W / 2, 200, "center", 0.1)
    s1, s2 = "2πr · r", "2πr · h"
    fcen(c, t, a5 - 0.6, s1 + " + " + s2, W / 2, 380, 110, BR)
    if t >= a5:
        wt = E.formula(None, s1 + " + " + s2, 0, 0, 110, "g", a=0)
        w1 = E.formula(None, "2πr", 0, 0, 110, "g", a=0)
        x0 = W / 2 - wt / 2
        x2 = x0 + wt - E.formula(None, s2, 0, 0, 110, "g", a=0)
        for k, xx in enumerate((x0, x2)):
            p = ep(t, a5 + 0.3 * k, 0.4)
            E.caixa_pontilhada(c, xx - 16, 270, w1 + 32, 140, p, CLARO, prog_=p)
    E.frase(c, t, b5, ps("o", "i", 60, CLARO) + [("fator comum", "g", 64, BR)] + ps("em evidência", "i", 60, CLARO), W / 2, 540, "center", 0.1)
    fcen(c, t, b5 + 0.8, "= 2πr · (r + h)", W / 2, 670, 90, CLARO)
    E.foco(c, t, c5, 0.5, lambda a: E.selo(c, 400, 830, 46, False, a))
    E.frase(c, t, c5 + 0.1, ps("copo ou lata sem tampa:", "i", 56, CLARO) + [("1 círculo só", "g", 60, BR)], 470, 852, "left", 0.1)
    E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "some as partes uma a uma", W / 2, 990, 56, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a6, ps("lata:", "i", 66) + [("raio 4 cm", "g", 66, COR)], XE, 340, passo=0.1)
    E.frase(c, t, b6, ps("altura", "i", 66) + [("10 cm", "g", 66, COR)], XE, 450, passo=0.1)
    E.frase(c, t, c6, [("π = 3", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, d6, [("1)", "g", 64, COR)] + ps("quantos mL cabem?", "i", 66), XE, 720, passo=0.1)
    E.frase(c, t, e6, [("2)", "g", 64, COR)] + ps("quanto metal, com tampa e fundo?", "i", 62), XE, 830, passo=0.1)

    def lata():
        E.cilindro(c, t, a6, 1450, 880, 160, 400)
        E.cilindro(c, t, 1e9, 1450, 880, 160, 400, "4 cm", None, size=54, tm=a6 + 0.3)
        E.cilindro(c, t, 1e9, 1450, 880, 160, 400, None, "10 cm", size=54, tm=b6)
    E.saida(c, t, C["s17.a"] - 0.1, lata)
    E.relogio(c, t, C["s17.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    X = 1260
    E.cilindro(c, t, C["s18"], 330, 900, 160, 400, "4", "10", size=52)

    def volume():
        E.frase(c, t, C["s18"] + 0.2, [("1)", "g", 64, COR)] + ps("quanto cabe", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a8, "4² = 16", X, 360, 80)
        fcen(c, t, b8, "3 × 16 = 48 cm²", X, 500, 80)
        fcen(c, t, c8, "48 × 10 = 480 cm³", X, 650, 80, COR)
        bola_txt(c, t, d8, "480 mL", X, 860, 140, 64)
    fase(c, t, C["s18"], C["s19"] - 0.1, volume)

    def metal():
        E.frase(c, t, C["s19"] + 0.2, [("2)", "g", 64, COR)] + ps("metal, pelo atalho", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a9, "2 × 3 × 4 = 24", X, 360, 80)
        fcen(c, t, b9, "4 + 10 = 14", X, 500, 80)
        fcen(c, t, c9, "24 × 14", X - 200, 720, 80)
        bola_txt(c, t, c9 + 0.6, "336 cm²", X + 200, 700, 140, 56)
    fase(c, t, C["s19"], C["s20"] - 0.1, metal)
    if t < C["s20"] - 0.1:
        return
    E.frase(c, t, C["s20"] + 0.2, ps("conferindo pelas partes", "i", 66), X, 200, "center", 0.1)
    fcen(c, t, a0, "lateral: 24 × 10 = 240", X, 360, 72)
    fcen(c, t, b0, "tampa e fundo: 2 × 48 = 96", X, 500, 72)
    fcen(c, t, c0, "240 + 96 = 336", X, 680, 84, COR)
    E.foco(c, t, c0 + 0.8, 0.5, lambda a: E.selo(c, X - 120, 860, 60, True, a))
    E.frase(c, t, c0 + 1.0, [("bateu", "g", 72, CERTO)], X - 30, 885, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s21.a", ps("volume =", "i", 66), "πr² · h"),
                 ("s21.b", ps("área = 2 círculos + retângulo de largura", "i", 60), "2πr"))
        for i, (k, l1, f_) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            wl = E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
            E.formula_em(c, t, C[k] + 0.8, f_, 350 + wl + 24, y, 68, "g", COR)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s22"] + 0.8, [("encher", "g", 120, COR)] + ps("a caixa-d'água", "i", 96), XE, 420)
    E.frase(c, t, a2, ps("quanto o", "i", 64) + [("nível sobe", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, b2, ps("em quanto", "i", 64) + [("tempo", "g", 66, COR)] + ps("ela enche", "i", 64), XE, 660, passo=0.1)
    E.cilindro(c, t, C["s22"] + 0.8, 1560, 860, 120, 200)
    lateral(c, 1560, 860, 120, 200 * ease_io(prog(t, a2, 2.0)), 1.0, E.COR, 0.35)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c2 + 0.2, 0.4))
    E.frase(c, t, d2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cilindro=b_cilindro, volume=b_volume, dobro=b_dobro, area=b_area,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
