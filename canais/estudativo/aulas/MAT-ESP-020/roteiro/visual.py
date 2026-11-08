"""Visual — Estudativo · MAT-ESP-020: razão entre volumes de sólidos semelhantes.
Mesma linguagem da trilha (MAT-ESP-001 a 019): sólidos do kit (E.cubo, E.paralelepipedo, E.cone), arestas escondidas e metade
de trás das bases tracejadas, o elemento da vez na cor da matéria, a 2ª família em cinza, resposta na esfera.
- O CUBO DOBRADO (oito()): o cubo de aresta 2 com as linhas que o dividem em 8 cubinhos nas três faces visíveis, e o "2" que
  acende em cada direção (frente, lado, cima), na ordem da fala.
- A TAÇA (taca()): cone de ponta para baixo, com haste e pé, desenhado aqui; o suco é o cone pequeno pintado na cor da
  matéria, que sobe até a fração da altura dita na fala. É a mesma peça no gancho, na explicação, no erro e na resposta.
- O CORTE NA METADE (b_corte): o cone de cima pintado na cor da matéria, o tronco em cinza; ao lado, o corte de lado com
  os dois triângulos semelhantes (o pequeno na cor da matéria dentro do grande).
- k fica escrito como letra (k, k², k³); a fala diz "cá".
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-020_razao_entre_volumes_de_solidos_semelhantes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cubo", "regra", "cone", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cone
assert 2 * 2 * 2 == 8 and 2 * 3 * 4 == 24 and 4 * 6 * 8 == 192 and 192 // 24 == 8 and 3 ** 3 == 27
assert 9 * 4 // 3 == 12 and 36 * 8 == 288 and 288 // 3 == 96 and 96 == 8 * 12 and 96 - 12 == 84 and 400 // 8 == 50
assert 4 ** 3 == 64 and 250 * 8 == 2000 and 270 // 27 == 10 and abs(1.26 ** 3 - 2) < 0.01


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, π ou → vai na grotesca: a serifada não tem esses sinais)"""
    return [(w, "g" if any(ch in w for ch in "²³√π→") else est, size * (0.92 if any(ch in w for ch in "²³√π→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def mid(P, Q):
    return (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2


# ================= peças desta aula =================
def oito(c, t, t0, x, y, a, tl, t2=(None, None, None), cor_l=None):
    """o cubo de aresta a (px) dividido em 8 cubinhos: as linhas entram em tl; os "2" de frente, lado e cima em t2"""
    pts = E.cubo(c, t, t0, x, y, a, preenche=0.16)
    p = ease_io(prog(t, tl, 0.6))
    if p > 0:
        for P, Q in ((mid(pts[0], pts[1]), mid(pts[3], pts[2])), (mid(pts[0], pts[3]), mid(pts[1], pts[2])),
                     (mid(pts[3], pts[2]), mid(pts[7], pts[6])), (mid(pts[3], pts[7]), mid(pts[2], pts[6])),
                     (mid(pts[1], pts[2]), mid(pts[5], pts[6])), (mid(pts[1], pts[5]), mid(pts[2], pts[6]))):
            M.line(c, *P, *Q, cor_l or TINTA2, 1, 4, progress=p)
    lados = ((pts[0], pts[1], (0, 1)), (pts[1], pts[5], (1, 0.3)), (pts[0], pts[3], (-1, 0)))
    for (P, Q, n), ti in zip(lados, t2):
        if ti is None:
            continue
        q = ease_io(prog(t, ti, 0.4))
        if q > 0:
            M.line(c, *P, *Q, E.COR, 1, 10, progress=q)
        m = mid(P, Q)
        E.foco(c, t, ti + 0.1, 0.4, lambda a, m=m, n=n: E._cola(c, "2", m[0], m[1], n[0], n[1], 20, 64, "g", COR, a))
    return pts


def taca(c, t, t0, cx, ty, r, h, f=0.0, tf=None, cor=None, rot=None, tr=None):
    """taça em forma de cone, de ponta para baixo: a boca é a elipse em (cx, ty), a ponta fica h px abaixo.
    O suco (cone pintado) sobe até a fração f da altura a partir de tf"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    ry = r * SEN
    ax, ay = cx, ty + h
    # corpo de vidro bem claro
    corpo = skia.Path(); corpo.moveTo(cx - r, ty); corpo.lineTo(ax, ay); corpo.lineTo(cx + r, ty); corpo.close()
    c.drawPath(corpo, M.paint(E.COR, 0.06 * p))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ty - ry, 2 * r, 2 * ry), M.paint(E.COR, 0.05 * p))
    # o suco
    fl = f * (ease_io(prog(t, tf, 0.9)) if tf is not None else 1.0)
    if fl > 0.002:
        yl, rl = ay - fl * h, r * fl
        suco = skia.Path(); suco.moveTo(cx - rl, yl); suco.lineTo(ax, ay); suco.lineTo(cx + rl, yl); suco.close()
        c.drawPath(suco, M.paint(cor or E.COR, 0.62 * p))
        c.drawOval(skia.Rect.MakeXYWH(cx - rl, yl - rl * SEN, 2 * rl, 2 * rl * SEN), M.paint(E.mix(cor or E.COR, "#FFFFFF", 0.4), 0.9 * p))
        c.drawOval(skia.Rect.MakeXYWH(cx - rl, yl - rl * SEN, 2 * rl, 2 * rl * SEN), M.paint(cor or E.COR, p, stroke=3))
    # contorno: boca, lados, haste e pé
    E._elipse(c, cx, ty, r, ry, 180, 360 * p, TINTA, 1.0, 6)
    M.line(c, cx - r, ty, ax, ay, TINTA, 1, 6, progress=p)
    M.line(c, cx + r, ty, ax, ay, TINTA, 1, 6, progress=p)
    hs = 0.22 * h
    M.line(c, ax, ay, ax, ay + hs, TINTA, 1, 8, progress=p)
    E._elipse(c, ax, ay + hs, 0.45 * r, 0.45 * r * SEN, 180, 360 * p, TINTA, 1.0, 6)
    if rot:
        E.foco(c, t, tr if tr is not None else t0 + 0.6, 0.4, lambda a: centro(c, rot, cx, ty - ry - 30, 54, "g", COR, a))


def regua(c, t, t0, x, y0, y1, rot, cor=None, size=46, lado=1):
    """cota vertical de y0 a y1 em x, com o rótulo ao lado"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    k = cor or E.COR
    M.line(c, x, y0, x, lerp(y0, y1, p), k, 1, 5)
    for yy in (y0, y1):
        M.line(c, x - 14, yy, x + 14, yy, k, p, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, rot, x + 24 if lado > 0 else x - 24 - E.larg(rot, "g", size), (y0 + y1) / 2 + size * 0.35,
                                                   size, "g", k if cor != TINTA2 else TINTA2, a))


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


# ---------------- gancho ----------------
TX, TY, TR, TH = 560, 300, 250, 520   # a taça grande


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        taca(c, t, a1, TX, TY, TR, TH, 0.5, b1)
        regua(c, t, b1 + 0.6, TX + TR + 60, TY + TH / 2, TY + TH, "metade da altura", TINTA2, 44)
        X = 1450
        E.frase(c, t, a1 + 0.4, ps("taça em", "i", 66) + [("cone", "g", 72, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b1 + 1.2, ps("meio cheia?", "i", 92), X, 470, "center", 0.12)
        E.foco(c, t, c1 - 0.6, 0.4, lambda q: centro(c, "não!", X, 600, 80, "g", ERRADO, q))
        bola_txt(c, t, c1, "f{1}{8}", X, 820, 140, 90)
        E.frase(c, t, c1 + 0.8, ps("do que cabe", "i", 54, TINTA2), X, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("comparar volumes", "g", 96, COR)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 2.4, ps("de sólidos ampliados", "i", 84), XE, 550, passo=0.14)
        E.frase(c, t, ta + 3.4, ps("sem calcular cada um", "i", 84), XE, 670, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 920
    itens = (("s03.b", "semelhantes: todas as medidas", "× k  (a razão)"), ("s03.c", "a área fica", "× k²"),
             ("s03.d", "volume do cone:", "f{πr^2 · h}{3}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 80, "left", 0.1)
        if "f{" in l2:
            E.formula_em(c, t, C[k] + 0.5, l2, x + w - 60, y + 128, 62, "g", COR, "right")
        else:
            E.formula_em(c, t, C[k] + 0.5, l2, x + 44, y + 162, 62, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.75), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 1000, "left", 0.1)


# ---------------- dobrar o cubo ----------------
def b_cubo(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    # o cubinho de 1 cm e o cubo de 2 cm
    E.cubo(c, t, b4, 200, 820, 150, "1 cm", size=48)
    passos = (d4, d4 + 1.1, d4 + 2.2)
    oito(c, t, c4, 540, 900, 380, d4 - 0.4 if t < e4 else d4 - 0.4, passos)
    if t >= c4:
        E.foco(c, t, c4 + 0.5, 0.4, lambda a: E.escreve(c, "2 cm", 540, 990, 50, "g", TINTA2, a) if t < d4 else None)
    X = 1460

    def um():
        E.frase(c, t, a4, [("semelhantes:", "g", 76, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a4 + 0.8, ps("mesma forma, tamanhos diferentes", "i", 50), X, 300, "center", 0.08)
        E.frase(c, t, c4, ps("dobre a aresta:", "i", 60) + [("2 cm", "g", 64, COR)], X, 440, "center", 0.1)
        E.frase(c, t, c4 + 1.2, ps("quantos cubinhos cabem?", "i", 58), X, 540, "center", 0.1)
        fcen(c, t, e4, "2 × 2 × 2", X - 140, 790, 84)
        bola_txt(c, t, e4 + 0.6, "8", X + 200, 770, 110, 110)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, ps("o volume usa", "i", 60) + [("3 medidas", "g", 66, COR)], X, 230, "center", 0.1)
    E.frase(c, t, a5 + 0.9, ps("comprimento, largura e altura", "i", 50, TINTA2), X, 320, "center", 0.08)
    E.frase(c, t, b5, ps("cada uma", "i", 60) + [("× 2", "g", 66, COR)], X, 470, "center", 0.1)
    fcen(c, t, c5, "volume × 2³ = 8", X, 680, 92, COR)


# ---------------- qualquer sólido: o bloco ----------------
def b_bloco(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, a6, ps("vale para", "i", 70) + [("qualquer sólido", "g", 74, COR)], W / 2, 170, "center", 0.1)
    s = 46   # px por cm
    E.paralelepipedo(c, t, b6, 170, 880, 2 * s, 3 * s, 4 * s, ("2", "3", "4"), size=46)
    E.paralelepipedo(c, t, c6, 560, 960, 4 * s, 6 * s, 8 * s, ("4", "6", "8"), size=52, cor=E.COR, preenche=0.2)
    X = 1440
    fcen(c, t, b6 + 0.8, "2 × 3 × 4 = 24 cm³", X, 380, 70, TINTA2)
    fcen(c, t, c6 + 1.4, "4 × 6 × 8 = 192 cm³", X, 520, 70, COR)
    fcen(c, t, d6, "192 ÷ 24", X - 170, 760, 84)
    bola_txt(c, t, d6 + 0.6, "8", X + 190, 740, 110, 110)
    E.frase(c, t, d6 + 1.2, ps("medidas × 2,", "i", 54) + [("volume × 8", "g", 58, COR)], X, 950, "center", 0.1)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s07.{k}"] for k in "abcdef")
    E.frase(c, t, a7, ps("razão de semelhança", "i", 62), 560, 220, "center", 0.1)
    fcen(c, t, a7 + 0.6, "k", 560, 400, 160, COR)
    E.frase(c, t, b7, ps("razão entre os volumes", "i", 62), 560, 560, "center", 0.1)
    fcen(c, t, b7 + 0.6, "k³", 560, 740, 160, COR)
    E.frase(c, t, b7 + 1.6, ps("a escala ao cubo da maquete", "i", 46, TINTA2), 560, 860, "center", 0.08)
    x, w, hh = 1050, 760, 150
    linhas = ((c7, "comprimento", "× k"), (d7, "área", "× k²"), (e7, "volume", "× k³"))
    for i, (ti, nome, fator) in enumerate(linhas):
        y = 150 + i * 180
        p = ep(t, ti, 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, COR if i == 2 else None, prog_=p)
        E.frase(c, t, ti + 0.1, ps(nome, "i", 64), x + 44, y + 98, "left", 0.1)
        E.formula_em(c, t, ti + 0.4, fator, x + w - 44, y + 104, 80, "g", COR if i == 2 else TINTA, "right")
    E.frase(c, t, f7 - 1.6, ps("medidas", "i", 60) + [("× 3", "g", 66)], x + w / 2, 780, "center", 0.1)
    fcen(c, t, f7, "volume × 3³ = 27", x + w / 2, 920, 80, COR)


# ---------------- o cone ----------------
def b_cone(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    s = 50
    E.cone(c, t, C["s08"], 260, 900, 3 * s, 4 * s, "3", "4", size=50, tm=a8)
    E.foco(c, t, b8, 0.4, lambda a: E.formula(c, "12π", 260, 1010, 64, "g", TINTA2, a, "center"))
    E.cone(c, t, c8 - 0.4, 740, 900, 6 * s, 8 * s, "6", "8", size=56, tm=c8, cor=E.COR, preenche=0.6)
    X = 1460
    fcen(c, t, C["s08"] + 0.2, "f{πr^2 · h}{3}", X, 230, 70, TINTA2)
    fcen(c, t, d8, "6² = 36", X, 410, 72)
    fcen(c, t, d8 + 1.6, "36 × 8 = 288", X, 530, 72)
    fcen(c, t, d8 + 3.2, "288 ÷ 3 = 96π", X, 650, 72, COR)
    fcen(c, t, e8, "96 = 8 × 12", X - 100, 870, 80)
    bola_txt(c, t, e8 + 0.6, "8 ×", X + 260, 850, 90, 70)


# ---------------- o corte na metade ----------------
KX, KY, KR, KH = 470, 940, 300, 600   # o cone grande (raio 6, altura 8)


def b_corte(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    hy = KH * COS
    ym = KY - hy / 2
    q_tr = ep(t, c0, 0.6)
    if q_tr > 0:
        tronco = skia.Op(lateral_cone(KX, KY, KR, KH), lateral_cone(KX, ym, KR / 2, KH / 2), skia.PathOp.kDifference_PathOp)
        if tronco is not None:
            c.drawPath(tronco, M.paint(TINTA2, 0.28 * q_tr))
    E.cone(c, t, C["s09"], KX, KY, KR, KH, preenche=0.18)
    q = ep(t, b9, 0.6)
    if q > 0:
        c.drawPath(lateral_cone(KX, ym, KR / 2, KH / 2), M.paint(E.COR, 0.6 * q))
    if t >= a9:
        p = ease_io(prog(t, a9, 0.6))
        E._elipse(c, KX, ym, KR / 2, KR / 2 * SEN, 180, 360 * p, E.COR, 1, 7)
        M.line(c, KX - KR * 0.85, ym, KX + KR * 0.85, ym, E.COR, 0.8 * p, 4, dash=E.TRACO)
        E.foco(c, t, a9 + 0.4, 0.4, lambda a: E.escreve(c, "metade da altura", KX + KR * 0.6, ym - 24, 42, "g", COR, a))
    E.foco(c, t, b9 + 0.4, 0.4, lambda a: E.escreve(c, "cone menor", KX - KR - 40, ym - hy / 4 + 10, 44, "i", COR, a) if t < c0 else None)
    E.foco(c, t, c0 + 0.3, 0.4, lambda a: centro(c, "tronco", KX, KY - hy * 0.3, 56, "g", TINTA, a))

    def lado():
        # o corte de lado: triângulo grande (raio 6, altura 8) e o de cima (raio 3, altura 4)
        k = 42
        vx, vy = 1360, 230
        A, B = (vx - 6 * k, vy + 8 * k), (vx + 6 * k, vy + 8 * k)
        a_, b_ = (vx - 3 * k, vy + 4 * k), (vx + 3 * k, vy + 4 * k)
        p = ease_io(prog(t, c9, 0.7))
        if p > 0:
            tri = skia.Path(); tri.addPoly([(vx, vy), A, B], True)
            c.drawPath(tri, M.paint(TINTA2, 0.12 * p))
            pt = M.paint(TINTA, p, stroke=6); c.drawPath(tri, pt)
            pq = ease_io(prog(t, c9 + 0.5, 0.6))
            if pq > 0:
                tr2 = skia.Path(); tr2.addPoly([(vx, vy), a_, b_], True)
                c.drawPath(tr2, M.paint(E.COR, 0.55 * pq))
                c.drawPath(tr2, M.paint(E.COR, pq, stroke=6))
            M.line(c, vx, vy, vx, B[1], TINTA2, p, 4, dash=E.TRACO)
        regua(c, t, c9 + 1.0, B[0] + 50, vy, B[1], "8", TINTA2, 52)
        E.foco(c, t, c9 + 1.2, 0.4, lambda a: centro(c, "6", (vx + B[0]) / 2, B[1] + 66, 52, "g", TINTA2, a))
        regua(c, t, d9, a_[0] - 50, vy, a_[1], "4", None, 52, -1)
        E.foco(c, t, d9 + 0.6, 0.4, lambda a: centro(c, "3", (vx + b_[0]) / 2, a_[1] - 14, 52, "g", COR, a))
        E.frase(c, t, c9 + 0.4, ps("dois triângulos", "i", 56) + [("semelhantes", "g", 58, COR)], 1360, 880, "center", 0.1)
        E.frase(c, t, d9 + 0.3, ps("altura e raio", "i", 52) + [("pela metade", "g", 56, COR)], 1360, 990, "center", 0.1)
    fase(c, t, C["s09"], C["s10"] - 0.1, lado)
    if t < C["s10"] - 0.1:
        return
    X = 1420
    E.frase(c, t, C["s10"] + 0.2, ps("é o cone de", "i", 60) + [("12π", "g", 64, COR)], X, 200, "center", 0.1)
    fcen(c, t, a0, "(f{1}{2})³ = f{1}{8}", X, 390, 96, COR)
    E.frase(c, t, b0, ps("em cima:", "i", 60) + [("1/8", "g", 66, COR)] + ps("do volume", "i", 60), X, 560, "center", 0.1)
    E.frase(c, t, c0, [("tronco", "g", 64)] + ps("de cone: a parte larga", "i", 56), X, 690, "center", 0.1)
    E.frase(c, t, d0, ps("fica com", "i", 60) + [("7/8", "g", 66)], X, 810, "center", 0.1)
    fcen(c, t, d0 + 1.0, "96π − 12π = 84π", X, 950, 72)


# ---------------- a taça ----------------
def b_taca(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    taca(c, t, C["s11"], TX, TY, TR, TH, 0.5, None, rot="400 mL" if t >= c1 else None, tr=c1)
    if t >= a1:
        p = ease_io(prog(t, a1, 0.5))
        rl = TR / 2
        yl = TY + TH / 2
        pt = M.paint(E.COR, p, stroke=8)
        tri = skia.Path(); tri.addPoly([(TX - rl, yl), (TX, TY + TH), (TX + rl, yl)], True)
        c.drawPath(tri, pt)
    regua(c, t, a1 + 0.3, TX + TR + 60, TY, TY + TH, "altura da taça", TINTA2, 42)
    regua(c, t, a1 + 0.8, TX - TR - 60, TY + TH / 2, TY + TH, "metade", None, 46, -1)
    X = 1450
    E.frase(c, t, C["s11"] + 0.2, ps("e a taça do começo?", "i", 64), X, 210, "center", 0.1)
    E.frase(c, t, a1, ps("o suco é um", "i", 58) + [("cone", "g", 64, COR)], X, 340, "center", 0.1)
    E.frase(c, t, a1 + 1.0, ps("com metade da altura:", "i", 54), X, 420, "center", 0.1)
    fcen(c, t, b1, "(f{1}{2})³ = f{1}{8}", X, 590, 84, COR)
    fcen(c, t, d1, "400 ÷ 8", X - 170, 860, 80)
    bola_txt(c, t, d1 + 0.6, "50 mL", X + 190, 840, 120, 58)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    taca(c, t, C["s12"], TX, TY + 40, TR, TH, 0.5, None)
    if t >= c2:
        p = ep(t, c2, 0.5)
        E.caixa_pontilhada(c, TX - TR / 2 - 30, TY + 40 + TH / 2 - 40, TR + 60, TH / 2 + 80, p, ERRADO, prog_=p)
        E.foco(c, t, c2 + 0.3, 0.4, lambda a: E.escreve(c, "a ponta,", 120, TY + 40 + TH * 0.7, 46, "g", ERRADO, a))
        E.foco(c, t, c2 + 0.5, 0.4, lambda a: E.escreve(c, "estreita", 120, TY + 40 + TH * 0.7 + 56, 46, "g", ERRADO, a))
    X = 1440
    E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a2, ps("metade da altura =", "i", 56), X, 310, "center", 0.1)
    E.frase(c, t, a2 + 1.0, ps("metade do volume?", "i", 56), X, 390, "center", 0.1)
    fcen(c, t, b2, "200 mL", X, 560, 100, ERRADO)
    if t >= b2 + 0.8:
        E.risco(c, X - 180, 590, X + 180, 480, t, b2 + 0.8, largura=12)
    E.frase(c, t, d2, ps("o suco encolhe nas", "i", 56) + [("3 medidas", "g", 60, COR)], X, 760, "center", 0.1)
    E.foco(c, t, d2 + 1.2, 0.5, lambda a: E.pilula(c, "certo: 50 mL", X, 900, 62, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def cubinhos(c, x, y, n, s, a, cor=None):
    """n x n x n em perspectiva simples: a frente n x n e a profundidade sugerida por uma faixa"""
    if a <= 0:
        return
    L = n * s
    d = 0.4 * L
    fr = skia.Rect.MakeXYWH(x, y - L, L, L)
    top = skia.Path(); top.addPoly([(x, y - L), (x + d * 0.8, y - L - d * 0.6), (x + L + d * 0.8, y - L - d * 0.6), (x + L, y - L)], True)
    lado = skia.Path(); lado.addPoly([(x + L, y), (x + L, y - L), (x + L + d * 0.8, y - L - d * 0.6), (x + L + d * 0.8, y - d * 0.6)], True)
    c.drawRect(fr, M.paint(cor or E.COR, 0.85 * a))
    c.drawPath(top, M.paint(E.mix(cor or E.COR, BR, 0.35), 0.85 * a))
    c.drawPath(lado, M.paint(E.mix(cor or E.COR, "#000000", 0.25), 0.85 * a))
    for i in range(1, n):
        M.line(c, x + i * s, y, x + i * s, y - L, BR, 0.5 * a, 2)
        M.line(c, x, y - i * s, x + L, y - i * s, BR, 0.5 * a, 2)
    for pth in (top, lado):
        c.drawPath(pth, M.paint(BR, a, stroke=3))
    c.drawRect(fr, M.paint(BR, a, stroke=3))


def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho, para voltar:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a3, ps("decore os", "i", 76, CLARO) + [("cubos", "g", 82, BR)], W / 2, 270, "center", 0.1)
        xs = (230, 470, 760, 1110, 1520)
        for i, n in enumerate((1, 2, 3, 4, 5)):
            ti = b3 + 0.85 * i
            s = 30
            E.foco(c, t, ti, 0.4, lambda q, i=i, n=n: cubinhos(c, xs[i], 640, n, s, q))
            E.foco(c, t, ti + 0.1, 0.4, lambda q, i=i, n=n: E.formula(c, f"{n}^3", xs[i] + n * s / 2 + 6, 740, 52, "g", CLARO, q, "center"))
            E.foco(c, t, ti + 0.2, 0.4, lambda q, i=i, n=n: centro(c, str(n ** 3), xs[i] + n * s / 2 + 6, 850, 84, "g", BR, q))
        E.frase(c, t, c3, ps("volume", "i", 60, CLARO) + [("× 64", "g", 66, BR)], 620, 990, "center", 0.1)
        E.frase(c, t, d3, [("→", "g", 60, CLARO)] + ps("medidas", "i", 60, CLARO) + [("× 4", "g", 66, BR)], 1180, 990, "center", 0.1)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 64, CLARO), W / 2, 180, "center", 0.1)
    fcen(c, t, a4, "volume: k · k · k", W / 2, 330, 96, BR)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 360, 500, 50, False, a))
    E.frase(c, t, b4 + 0.1, ps("não compensa: volume", "i", 62, CLARO) + [("× 2", "g", 68, BR)], 440, 525, "left", 0.1)
    fcen(c, t, c4, "1³ = 1     2³ = 8", W / 2, 680, 84, CLARO)
    E.frase(c, t, c4 + 2.0, ps("nenhum inteiro ao cubo dá 2", "i", 54, CLARO), W / 2, 780, "center", 0.1)
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "medidas × 1,26 (uns 26%)", W / 2, 920, 62, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, ps("pote:", "i", 62) + [("250 mL", "g", 66, COR)], XE, 300, passo=0.1)
    E.frase(c, t, b5, ps("pote semelhante:", "i", 58) + [("medidas × 2", "g", 62, COR)], XE, 400, passo=0.1)
    E.frase(c, t, c5, [("1)", "g", 62, COR)] + ps("quanto cabe no novo?", "i", 62), XE, 520, passo=0.1)
    E.frase(c, t, d5, ps("taça em cone, cheia:", "i", 58) + [("270 mL", "g", 62, COR)], XE, 680, passo=0.1)
    E.frase(c, t, e5, [("2)", "g", 62, COR)] + ps("suco até", "i", 62) + [("1/3", "g", 66, COR)] + ps("da altura?", "i", 62), XE, 800, passo=0.1)

    def figs():
        E.cilindro(c, t, a5, 1300, 540, 60, 110)
        E.cilindro(c, t, b5, 1560, 540, 120, 220, preenche=0.6)
        taca(c, t, d5, 1450, 690, 160, 220, 1 / 3, e5 + 0.3)
    E.saida(c, t, C["s16.a"] - 0.1, figs)
    E.relogio(c, t, C["s16.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    X = 1300

    def pote():
        E.cilindro(c, t, C["s17"], 220, 880, 80, 150, None, "250 mL", size=40)
        E.cilindro(c, t, C["s17"] + 0.3, 690, 880, 160, 300, preenche=0.6)
        E.frase(c, t, C["s17"] + 0.2, [("1)", "g", 64, COR)] + ps("o pote", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a7, "k = 2,  2³ = 8", X, 380, 80)
        fcen(c, t, b7, "250 × 8 = 2.000 mL", X, 540, 80, COR)
        bola_txt(c, t, c7, "2 litros", X, 790, 150, 58)
    fase(c, t, C["s17"], C["s18"] - 0.1, pote)
    if t < C["s18"] - 0.1:
        return
    taca(c, t, C["s18"], 470, 260, 260, 560, 1 / 3, C["s18"] + 0.4, rot="270 mL cheia", tr=C["s18"] + 0.6)
    regua(c, t, a8, 470 + 260 + 50, 260 + 560 * 2 / 3, 260 + 560, "1/3", None, 52)
    E.frase(c, t, C["s18"] + 0.2, [("2)", "g", 64, COR)] + ps("a taça", "i", 66), X, 200, "center", 0.1)
    fcen(c, t, a8, "k = f{1}{3}", X, 380, 84)
    fcen(c, t, b8, "(f{1}{3})³ = f{1}{27}", X, 560, 84, COR)
    fcen(c, t, c8, "270 ÷ 27", X - 180, 790, 80)
    bola_txt(c, t, c8 + 0.6, "10 mL", X + 200, 770, 120, 56)
    E.frase(c, t, d8, [("1/3", "g", 56, COR)] + ps("da altura, só", "i", 54) + [("10 mL", "g", 56, COR)], X, 990, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", ps("medidas", "i", 72) + [("× k", "g", 76, COR)]),
                 ("s19.b", ps("volume", "i", 72) + [("× k³", "g", 76, COR)]),
                 ("s19.c", ps("metade da altura do cone:", "i", 64) + [("1/8", "g", 72, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 25, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 390, y, "left", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0, f0 = (C[f"s20.{k}"] for k in "abcdef")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("praticar", "g", 120, COR)] + ps("o módulo", "i", 96), XE, 410)
    E.frase(c, t, b0, ps("sólidos compostos e a água que sobe", "i", 56), XE, 560, passo=0.1)
    E.frase(c, t, c0, ps("sólidos encaixados", "i", 56), XE, 650, passo=0.1)
    E.frase(c, t, d0, ps("volumes ampliados", "i", 56), XE, 740, passo=0.1)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, e0 + 0.2, 0.4))
    E.frase(c, t, f0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cubo=b_cubo, bloco=b_bloco, regra=b_regra, cone=b_cone, corte=b_corte,
              taca=b_taca, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
