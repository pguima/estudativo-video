"""Visual — Estudativo · MAT-ESP-018: volume pelo nível da água.
Mesma linguagem da trilha (MAT-ESP-001 a 017): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
a 2ª família em cinza, resposta na esfera.
- ÁGUA SUBINDO (copiada de MAT-ESP-005/009): agua() no aquário (E.paralelepipedo transparente) e agua_cil() no copo (E.cilindro);
  o nível que a fala cita ganha a cota marca() à direita. A CAMADA que subiu (camada()) é o prisma pintado na cor da matéria,
  com o fundo pintado (piso()): é ela que mede o volume do objeto.
- A PEDRA (pedra()): um contorno irregular cinza que afunda até o fundo; a bolinha do copo é uma E.esfera que cai.
- ERRO: a cota da altura final inteira (22) em vermelho; só a faixa de 2 cm em verde.
- ATALHO (palco): o copo em traço branco (copo_br()) com o espaço vazio pintado (144) contra a bolinha (108) e duas (216).
- π = 3 no copo, como no roteiro.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-018_volume_pelo_nivel_da_agua.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "copo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cilindro
KX, KY = 0.394, -0.308  # a profundidade na perspectiva cavaleira (a mesma de E.paralelepipedo)
assert 40 * 25 == 1000 and 22 - 20 == 2 and 1000 * 2 == 2000 and 1000 * 22 == 22000
assert 3 * 4 ** 2 == 48 and 4 * 3 ** 3 == 108 and 108 / 48 == 2.25 and 12 + 2.25 == 14.25 and 14.25 < 15
assert 48 * (15 - 12) == 144 and 108 < 144 and 2 * 108 == 216 and 216 > 144
assert 50 * 30 == 1500 and 27 - 25 == 2 and 1500 * 2 == 3000 and 3000 // 3 == 1000
assert 1500 * (30 - 27) == 4500 and 4 * 1000 <= 4500 and 5 * 1000 > 4500


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, √, π ou ° vai na grotesca)"""
    out = []
    for w in txt.split():
        g = any(ch in w for ch in "²³√π°")
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


# ================= peças desta aula (água: de MAT-ESP-005 e MAT-ESP-009) =================
def piso(c, x, y, w, d, a=1.0, cor=None):
    """o fundo da caixa pintado (a área da base)"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    p = skia.Path(); p.addPoly([(x, y), (x + w, y), (x + w + dx, y + dy), (x + dx, y + dy)], True)
    c.drawPath(p, M.paint(cor or E.COR, 0.35 * a))


def agua(c, x, y, w, d, h, nivel, a=1.0, n0=0.0, cor=None, alfa=1.0):
    """água de n0 até a fração nivel da altura h, dentro da caixa"""
    if a <= 0 or nivel <= n0:
        return
    dx, dy = KX * d, KY * d
    h0, hh = h * n0, h * nivel
    cor = cor or E.mix(E.COR, "#FFFFFF", 0.45)
    for pts, al in (([(x + w, y - h0), (x + w + dx, y + dy - h0), (x + w + dx, y + dy - hh), (x + w, y - hh)], 0.42),
                    ([(x, y - hh), (x + w, y - hh), (x + w + dx, y - hh + dy), (x + dx, y - hh + dy)], 0.55),
                    ([(x, y - h0), (x + w, y - h0), (x + w, y - hh), (x, y - hh)], 0.38)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(cor, al * a * alfa))


def camada(c, x, y, w, d, h, n0, n1, a=1.0, cor=None):
    """a camada que subiu (de n0 a n1): um prisma pintado forte"""
    agua(c, x, y, w, d, h, n1, a, n0, cor or E.COR, 1.2)


def agua_cil(c, cx, cy, r, h, nivel, a=1.0, n0=0.0, cor=None, alfa=1.0):
    """água de n0 até a fração nivel da altura h (px) dentro de um E.cilindro de base em (cx, cy)"""
    if a <= 0 or nivel <= n0:
        return
    ry, ct, cb = r * SEN, cy - h * nivel * COS, cy - h * n0 * COS
    cor = cor or E.mix(E.COR, "#FFFFFF", 0.45)
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cb)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cb - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor, 0.45 * a * alfa))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(cor, 0.6 * a * alfa))


def marca(c, t, t0, x, y0, y1, rot, cor=None, size=52, a=1.0):
    """cota vertical de y0 (embaixo) até y1 (em cima), com a medida à direita (de MAT-ESP-009)"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    yy = lerp(y0, y1, p)
    M.line(c, x, y0, x, yy, cor, a, 5)
    for y_ in (y0, yy):
        M.line(c, x - 14, y_, x + 14, y_, cor, a, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda q: E.escreve(c, rot, x + 26, (y0 + y1) / 2 + size * 0.36, size, "g", cor, q * a))


def nivel_linha(c, x, y, w, d, yy, rot, cor=None, a=1.0, size=48):
    """o risco de um nível na parede da frente e no fundo, com o valor à esquerda"""
    if a <= 0:
        return
    M.line(c, x - 30, yy, x + w, yy, cor or TINTA2, a, 3, dash=E.TRACO)
    E._cola(c, rot, x - 30, yy, -1, 0, 10, size, "g", cor or TINTA2, a)


_PEDRA = [(1.0, 0.0), (0.78, 0.55), (0.25, 0.82), (-0.42, 0.7), (-0.95, 0.28), (-0.88, -0.35), (-0.4, -0.75), (0.3, -0.68), (0.82, -0.42)]


def pedra(c, cx, cy, s, a=1.0, cor=None):
    """a pedra torta: contorno irregular arredondado, de raio s"""
    if a <= 0:
        return
    pts = [(cx + s * u, cy + s * v * 0.72) for u, v in _PEDRA]
    p = skia.Path()
    n = len(pts)
    m = [((pts[i][0] + pts[(i + 1) % n][0]) / 2, (pts[i][1] + pts[(i + 1) % n][1]) / 2) for i in range(n)]
    p.moveTo(*m[-1])
    for i in range(n):
        p.quadTo(pts[i][0], pts[i][1], m[i][0], m[i][1])
    p.close()
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx - s * 0.3, cy - s * 0.3), s * 1.4,
                [M.hexc(E.mix(cor or TINTA2, "#FFFFFF", 0.55), a), M.hexc(cor or TINTA2, a)], [0.0, 1.0]))
    c.drawPath(p, g)
    pt = M.paint(TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def no_fundo(x, y, w, d, s, k=0.5):
    """onde a pedra (de raio s) assenta no fundo da caixa, na fração k da largura"""
    return x + w * k + KX * d * 0.5, y + KY * d * 0.5 - s * 0.6


def copo_br(c, cx, cy, r, h, a=1.0, cor=BR):
    """o copo em traço branco (para o palco escuro)"""
    if a <= 0:
        return
    ry, ct = r * SEN, cy - h * COS
    pt = M.paint(cor, a, stroke=6)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False, pt)
    tr = M.paint(cor, 0.5 * a, stroke=4); tr.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, 180, False, tr)
    M.line(c, cx - r, cy, cx - r, ct, cor, a, 6); M.line(c, cx + r, cy, cx + r, ct, cor, a, 6)


# ---------------- gancho ----------------
AX, AY, AW, AD, AH = 160, 920, 520, 325, 390   # o aquário: 40 x 25 cm de fundo e 30 de altura (13 px por cm)


def queda(t, t0, y0, y1, d=0.8):
    """a pedra cai de y0 até y1"""
    q = prog(t, t0, d)
    return lerp(y0, y1, q * q)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def torta():
        E.foco(c, t, a1, 0.6, lambda q: pedra(c, 480, 560, 230, q))
        E.frase(c, t, a1 + 0.3, ps("uma pedra", "i", 70) + [("toda torta", "g", 76, COR)], 1000, 300, "left", 0.1)
        E.frase(c, t, lerp(a1, b1, 0.5), ps("não é cubo, cilindro, esfera", "i", 56, TINTA2), 1000, 420, "left", 0.08)
        E.frase(c, t, b1, [("nenhuma fórmula", "g", 70, ERRADO)] + ps("serve", "i", 64), 1000, 560, "left", 0.1)
        E.foco(c, t, b1 + 0.6, 0.4, lambda q: E.selo(c, 930, 538, 40, False, q))
    fase(c, t, C["s01"], c1 - 0.1, torta)
    if t >= c1 - 0.1:
        s = 70
        px, py = no_fundo(AX, AY, AW, AD, s)
        E.paralelepipedo(c, t, c1 - 0.3, AX, AY, AW, AD, AH, preenche=0.04)
        yy = queda(t, c1 + 0.4, AY - AH - 120, py)
        sobe = ease_io(prog(t, c1 + 1.0, 0.8))
        pedra(c, px, yy, s, ep(t, c1 + 0.3, 0.3))
        agua(c, AX, AY, AW, AD, AH, 0.55 + 0.1 * sobe, ep(t, c1, 0.4))
        if sobe > 0:
            camada(c, AX, AY, AW, AD, AH, 0.55, 0.55 + 0.1 * sobe)
        E.frase(c, t, c1, ps("mergulhe num aquário:", "i", 60), 1100, 360, "left", 0.1)
        E.frase(c, t, c1 + 1.0, ps("a água", "i", 66) + [("sobe", "g", 72, COR)], 1100, 480, "left", 0.1)
        E.frase(c, t, c1 + 2.0, ps("a subida conta", "i", 60) + [("o volume", "g", 64, COR)], 1100, 620, "left", 0.1)


def gancho_s02(c, t, C):
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, lerp(ta, tb, 0.2), [("medir o volume", "g", 96, COR)], XE, 450, passo=0.14)
    E.frase(c, t, lerp(ta, tb, 0.4), ps("de qualquer objeto", "i", 84), XE, 570, passo=0.14)
    E.frase(c, t, lerp(ta, tb, 0.65), ps("e prever se", "i", 84) + [("transborda", "g", 92, COR)], XE, 700, passo=0.14)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


def b_gancho_todo(c, t, C, b):
    E.saida(c, t, C["s02"] - 0.1, lambda: b_gancho(c, t, C, b))
    if t >= C["s02"]:
        gancho_s02(c, t, C)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "prisma e cilindro:", "V = área da base × altura"), ("s03.c", "o nível sobe:", "f{volume}{área do fundo}"),
             ("s03.d", "1 cm³ = 1 mL", "1.000 cm³ = 1 L"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 180 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 76, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 172, 56, "g", COR)
    alvo = [180 + i * 250 + 180 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1010, "left", 0.12)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    s = 80
    px, py = no_fundo(AX, AY, AW, AD, s)
    E.paralelepipedo(c, t, C["s04"] - 0.6, AX, AY, AW, AD, AH, preenche=0.04)
    yy = queda(t, a4 + 0.3, AY - AH - 140, py, 1.0)
    pedra(c, px, yy, s, ep(t, a4, 0.3))
    sobe = ease_io(prog(t, b4, 1.0))
    n0, n1 = 0.45, 0.45 + 0.13 * sobe
    agua(c, AX, AY, AW, AD, AH, n1)
    if t >= c4:
        camada(c, AX, AY, AW, AD, AH, n0, n1, ep(t, c4, 0.5))
    piso(c, AX, AY, AW, AD, ep(t, a5 + 0.4, 0.5) * (1 - ep(t, c5, 0.4)))
    if t >= b4:
        for k in (0.2, 0.8):
            x = AX + AW * k
            p = ep(t, b4, 0.4) * (1 - ep(t, c4 + 0.5, 0.4))
            if p > 0:
                M.arrow(c, x, AY - AH * n0 + 10, x, AY - AH * n0 - 70, E.COR, p, 6, 20, ease_io(prog(t, b4, 0.5)))
    if t >= c4:
        marca(c, t, c4 + 0.3, AX + AW + KX * AD + 40, AY + KY * AD - AH * n0, AY + KY * AD - AH * (0.58), "subiu", E.COR, 46)
    X = 1420

    def porque():
        E.frase(c, t, C["s04"] + 0.1, ps("por que a água sobe?", "i", 62), X, 230, "center", 0.1)
        E.frase(c, t, a4, ps("pedra e água não cabem", "i", 56), X, 360, "center", 0.1)
        E.frase(c, t, a4 + 0.9, [("no mesmo lugar", "g", 62, COR)], X, 440, "center", 0.1)
        E.frase(c, t, b4, ps("a pedra", "i", 58) + [("empurra", "g", 62, COR)] + ps("a água para cima", "i", 58), X, 580, "center", 0.1)
        E.frase(c, t, c4, ps("água empurrada =", "i", 58) + [("volume da pedra", "g", 62, COR)], X, 720, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, porque)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, ps("a camada tem a forma do fundo:", "i", 54), X, 230, "center", 0.1)
    E.frase(c, t, a5 + 1.0, [("um prisma", "g", 66, COR)], X, 320, "center", 0.1)
    fcen(c, t, b5, "V pedra = área do fundo × subida", X, 470, 56, COR)
    E.foco(c, t, c5, 0.5, lambda q: E.pilula(c, "objeto inteiro dentro da água", X, 640, 52, "g", a=q, cor=E.SOBRE))
    E.frase(c, t, c5 + 1.4, ps("se ele boia, só a parte de baixo", "i", 50, TINTA2), X, 760, "center", 0.08)
    E.frase(c, t, c5 + 2.2, ps("empurra água", "i", 50, TINTA2), X, 830, "center", 0.08)


# ---------------- a pedra do aquário ----------------
def aquario_20_22(c, t, t0, tc, sobe_t, a=1.0, cotas=True, cor_cam=None, cam_a=1.0):
    """o aquário do exemplo: água a 20 de 30 e, com a pedra, a 22. Devolve (n0, n1)"""
    s = 70
    px, py = no_fundo(AX, AY, AW, AD, s)
    E.paralelepipedo(c, t, t0, AX, AY, AW, AD, AH, ("40 cm", "25 cm", None), preenche=0.04, size=50, tm=t0 + 0.6)
    q = ep(t, tc, 0.4)
    yy = queda(t, tc, AY - AH - 120, py)
    pedra(c, px, yy, s, q)
    sobe = ease_io(prog(t, sobe_t, 0.8))
    n0, n1 = 20 / 30, 20 / 30 + 2 / 30 * sobe
    agua(c, AX, AY, AW, AD, AH, n1)
    if sobe > 0:
        camada(c, AX, AY, AW, AD, AH, n0, n1, cam_a, cor_cam)
    return n0, n1


def b_pedra(c, t, C, b):
    a6, b6, c6, d6, e6, f6 = (C[f"s06.{k}"] for k in "abcdef")
    n0, n1 = aquario_20_22(c, t, C["s06"] - 0.4, c6 - 0.6, c6 + 0.4)
    piso(c, AX, AY, AW, AD, ep(t, b6, 0.5) * (1 - ep(t, c6, 0.4)))
    xm = AX + AW + KX * AD + 40
    yb = AY + KY * AD
    if t >= c6:
        marca(c, t, c6, xm, yb, yb - AH * 20 / 30, "20", TINTA2, 48)
    if t >= d6:
        marca(c, t, d6, xm, yb - AH * 20 / 30, yb - AH * 22 / 30, "2", E.COR, 52)
    X = 1420
    E.frase(c, t, a6, ps("fundo de", "i", 58) + [("40 por 25 cm", "g", 62, COR)], X, 220, "center", 0.1)
    fcen(c, t, b6, "40 × 25 = 1.000 cm²", X, 350, 70)
    E.frase(c, t, c6, ps("a água vai de", "i", 58) + [("20", "g", 62)] + ps("para", "i", 58) + [("22 cm", "g", 62, COR)], X, 490, "center", 0.1)
    fcen(c, t, d6, "22 − 20 = 2 cm", X, 610, 70, COR)
    fcen(c, t, e6, "1.000 × 2 = 2.000 cm³", X, 750, 70)
    bola_txt(c, t, f6, "2 L", X, 910, 100, 76)


# ---------------- o copo: transborda? ----------------
CX, CY, CR, CH = 430, 960, 136, 510   # o copo: raio 4 e altura 15 (34 px por cm)


def copo(c, t, t0, n_agua, tb=None, bola_y=None, a=1.0):
    E.cilindro(c, t, t0, CX, CY, CR, CH, preenche=0.12)
    agua_cil(c, CX, CY, CR, CH, n_agua, a)
    if tb is not None and bola_y is not None:
        q = ep(t, tb, 0.3)
        if q > 0:
            pa = skia.Paint(); pa.setAlphaf(q)
            c.saveLayer(None, pa); E.esfera(c, 1e9, 0, CX, bola_y, 3 * 34, inclina=22); c.restore()


def b_copo(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    yb = CY - 3 * 34 * COS - 3 * 34 + 20     # a bolinha assentada no fundo
    by = queda(t, d8 - 0.6, CY - CH * COS - 140, yb, 0.7) if t >= d7 else None   # a bolinha espera em cima e cai na subida
    sobe = ease_io(prog(t, d8, 1.0))
    n = 12 / 15 + 2.25 / 15 * sobe
    copo(c, t, C["s07"], n * ep(t, c7, 0.6) if t < C["s08"] else n, d7 + 0.3, by)
    if sobe > 0:
        agua_cil(c, CX, CY, CR, CH, n, 1.0, 12 / 15, E.COR, 1.2)
    xm = CX + CR + 40
    yl = lambda h: CY - CH * h / 15 * COS
    if t >= b7:
        aresta_cota = ep(t, b7, 0.4)
        M.line(c, CX, yl(15), CX + CR, yl(15), TINTA, aresta_cota, 5)
        E.foco(c, t, b7 + 0.2, 0.4, lambda q: E._cola(c, "4", CX + CR / 2, yl(15), 0, -1, 8, 50, "g", TINTA, q))
        marca(c, t, b7 + 0.5, xm + 200, CY, yl(15), "15", TINTA2, 48)
    if t >= c7:
        marca(c, t, c7, xm, CY, yl(12), "12", TINTA2, 48)
    if t >= e8:
        marca(c, t, e8, xm, yl(12), yl(14.25), "", E.COR, 48)
        E.foco(c, t, e8 + 0.3, 0.4, lambda q: E.escreve(c, "14,25", xm + 26, yl(14.25) + 6, 50, "g", COR, q))
    X = 1360

    def enunciado():
        E.frase(c, t, a7, ps("vai", "i", 66) + [("transbordar?", "g", 72, COR)], X, 220, "center", 0.1)
        E.frase(c, t, b7, ps("copo: raio", "i", 58) + [("4 cm,", "g", 62, COR)] + ps("altura", "i", 58) + [("15 cm", "g", 62, COR)], X, 360, "center", 0.1)
        E.frase(c, t, c7, ps("água até", "i", 58) + [("12 cm", "g", 62, COR)], X, 470, "center", 0.1)
        E.frase(c, t, d7, ps("bolinha maciça de", "i", 58) + [("raio 3 cm", "g", 62, COR)], X, 580, "center", 0.1)
        E.frase(c, t, e7, [("π = 3", "g", 64, COR)], X, 690, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, enunciado)
    if t < C["s08"] - 0.1:
        return
    fcen(c, t, a8, "fundo: 3 × 4² = 48 cm²", X, 220, 64)
    fcen(c, t, b8, "bolinha: 4r^3", X, 340, 64, TINTA2)
    fcen(c, t, lerp(b8, c8, 0.35), "4 × 3³ = 108 cm³", X, 450, 64)
    fcen(c, t, c8, "108 ÷ 48 = 2,25", X, 590, 76, COR)
    E.frase(c, t, d8, ps("a água sobe", "i", 58) + [("2,25 cm", "g", 62, COR)], X, 700, "center", 0.1)
    fcen(c, t, e8, "12 + 2,25 = 14,25", X, 820, 76)
    E.foco(c, t, f8, 0.5, lambda q: E.selo(c, X - 270, 945, 44, True, q))
    E.frase(c, t, f8 + 0.1, [("14,25 < 15:", "g", 58, CERTO)] + ps("não transborda", "i", 56), X - 200, 968, "left", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    errado = 1 - ep(t, d9, 0.4)
    aquario_20_22(c, t, C["s09"] - 1.0, -1e9, -1e9, cor_cam=CERTO if t >= d9 else E.COR, cam_a=0.6 + 0.4 * ep(t, d9, 0.4))
    xm = AX + AW + KX * AD + 40
    yb = AY + KY * AD
    if t >= b9:
        marca(c, t, b9, xm, yb, yb - AH * 22 / 30, "22", ERRADO, 52, a=errado)
    if t >= d9:
        marca(c, t, d9, xm + 30, yb - AH * 20 / 30, yb - AH * 22 / 30, "2", CERTO, 52)
    X = 1420
    E.frase(c, t, C["s09"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a9, ps("usar a", "i", 58) + [("altura final", "g", 62, ERRADO)], X, 310, "center", 0.1)
    E.frase(c, t, a9 + 0.8, ps("no lugar da", "i", 58) + [("subida", "g", 62, CERTO)], X, 400, "center", 0.1)
    fcen(c, t, b9, "1.000 × 22 = 22.000", X, 540, 74, ERRADO)
    E.frase(c, t, c9, [("22 L?", "g", 70, ERRADO)], X - 80, 670, "center", 0.1)
    E.foco(c, t, c9 + 0.5, 0.5, lambda q: E.selo(c, X + 80, 645, 40, False, q))
    E.frase(c, t, lerp(c9, d9, 0.5), ps("isso é a água junto com a pedra", "i", 48, TINTA2), X, 770, "center", 0.08)
    E.frase(c, t, d9, ps("só a", "i", 58) + [("subida", "g", 62, CERTO)] + ps("é a pedra", "i", 58), X, 880, "center", 0.1)
    E.foco(c, t, e9, 0.5, lambda q: E.pilula(c, "altura final − altura inicial", X, 990, 52, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a0, b0, c0, d0, e0, f0 = (C[f"s10.{k}"] for k in "abcdef")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    cx, cy, r, h = 420, 960, 136, 510
    yl = lambda hh: cy - h * hh / 15 * COS
    copo_br(c, cx, cy, r, h, ep(t, C["s10"], 0.5))
    agua_cil(c, cx, cy, r, h, 12 / 15, ep(t, C["s10"], 0.5), cor=E.mix(E.COR, "#FFFFFF", 0.3), alfa=0.9)
    if t >= b0:
        q = ep(t, b0, 0.5)
        agua_cil(c, cx, cy, r, h, 1.0, q, 12 / 15, "#FFD500", 0.7)
        x = cx + r + 40
        M.line(c, x, yl(12), x, yl(15), CLARO, q, 4)
        for y in (yl(12), yl(15)):
            M.line(c, x - 12, y, x + 12, y, CLARO, q, 4)
        E.foco(c, t, b0 + 0.3, 0.4, lambda k: E._cola(c, "3", x, (yl(12) + yl(15)) / 2, 1, 0, 14, 56, "g", BR, k))
    X = 1260

    def um():
        E.frase(c, t, C["s10"] + 0.2, ps("atalho:", "i", 66, CLARO) + [("transborda?", "g", 72, BR)], X, 200, "center", 0.1)
        E.frase(c, t, a0, [("compare volumes,", "g", 62, BR)] + ps("sem dividir", "i", 58, CLARO), X, 310, "center", 0.1)
        E.frase(c, t, b0, ps("espaço vazio: cilindro de", "i", 56, CLARO) + [("3 cm", "g", 60, BR)], X, 430, "center", 0.1)
        fcen(c, t, c0, "48 × 3 = 144", X, 560, 84, "#FFD500")
        fcen(c, t, d0, "bolinha: 108 < 144", X - 60, 700, 70, BR)
        E.foco(c, t, d0 + 0.6, 0.5, lambda q: E.selo(c, X + 330, 678, 40, True, q))
        E.frase(c, t, d0 + 0.8, [("cabe", "g", 60, CERTO)], X + 390, 700, "left", 0.1)
        fcen(c, t, e0, "2 bolinhas: 216 > 144", X - 60, 840, 70, BR)
        E.foco(c, t, f0, 0.5, lambda q: E.selo(c, X + 360, 818, 40, False, q))
        E.frase(c, t, f0 + 0.2, [("transborda", "g", 56, ERRADO)], X + 210, 940, "left", 0.1)
    fase(c, t, C["s10"], C["s11"] - 0.1, um)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, C["s11"] + 0.1, ps("funciona porque", "i", 62, CLARO), X, 220, "center", 0.1)
    E.frase(c, t, a1, [("espaço vazio", "g", 66, BR)] + ps("= o que ainda cabe", "i", 60, CLARO), X, 350, "center", 0.1)
    E.frase(c, t, b1, ps("se o objeto cabe nele,", "i", 56, CLARO), X, 470, "center", 0.1)
    E.frase(c, t, b1 + 0.8, ps("a água não passa da", "i", 56, CLARO) + [("borda", "g", 60, BR)], X, 550, "center", 0.1)
    E.foco(c, t, c1, 0.5, lambda a: E.selo(c, 900, 700, 44, False, a))
    E.frase(c, t, c1 + 0.1, ps("a prova pede a", "i", 56, CLARO) + [("altura nova?", "g", 60, BR)], 970, 722, "left", 0.1)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "divida pela área do fundo", X, 900, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
QX, QY, QW, QD, QH = 1060, 900, 500, 300, 300   # o aquário da questão: 50 x 30 x 30 (10 px por cm)


def aquario_q(c, t, t0, td, n_sobe, a=1.0, medidas=True, tm=None, qx=QX):
    E.paralelepipedo(c, t, t0, qx, QY, QW, QD, QH, ("50 cm", "30 cm", "30 cm") if medidas else (None, None, None),
                     preenche=0.04, size=46, tm=tm)
    for k, kk in enumerate((0.25, 0.5, 0.75)):
        s = 40
        px, py = no_fundo(qx, QY, QW, QD, s, kk)
        if t >= td:
            yy = queda(t, td + 0.3 * k, QY - QH - 100, py, 0.7)
            pedra(c, px, yy, s, ep(t, td + 0.3 * k, 0.3))
    n0 = 25 / 30
    agua(c, qx, QY, QW, QD, QH, n0 + 2 / 30 * n_sobe, a)
    return n0


def b_questao(c, t, C, b):
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    E.frase(c, t, C["s12"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a2, ps("aquário: fundo", "i", 56) + [("50 × 30 cm", "g", 60, COR)], XE, 320, passo=0.1)
    E.frase(c, t, b2, ps("altura", "i", 56) + [("30 cm", "g", 60, COR)], XE, 410, passo=0.1)
    E.frase(c, t, c2, ps("água a", "i", 56) + [("25 cm", "g", 60, COR)], XE, 500, passo=0.1)
    E.frase(c, t, d2, [("3 pedras", "g", 60, COR)] + ps("iguais: sobe para", "i", 56) + [("27", "g", 60, COR)], XE, 590, passo=0.1)
    E.frase(c, t, e2, [("1)", "g", 58, COR)] + ps("volume de cada pedra?", "i", 58), XE, 720, passo=0.1)
    E.frase(c, t, f2, [("2)", "g", 58, COR)] + ps("quantas pedras ainda cabem", "i", 58), XE, 820, passo=0.1)
    E.frase(c, t, f2 + 1.0, ps("sem transbordar?", "i", 58), XE + 70, 900, passo=0.1)

    def fig():
        aquario_q(c, t, a2, d2, ease_io(prog(t, d2 + 1.0, 0.8)), ep(t, c2, 0.5), tm=a2 + 0.6)
    E.saida(c, t, C["s13.a"] - 0.1, fig)
    E.relogio(c, t, C["s13.a"], 1440, 560, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    qx = 160
    n0 = aquario_q(c, t, C["s14"], -1e9, 1.0, qx=qx)
    piso(c, qx, QY, QW, QD, ep(t, a4, 0.5) * (1 - ep(t, b4, 0.4)))
    camada(c, qx, QY, QW, QD, QH, n0, 27 / 30, ep(t, b4, 0.5))
    xm = qx + QW + KX * QD + 40
    yb = QY + KY * QD
    if t >= b4:
        marca(c, t, b4, xm, yb - QH * 25 / 30, yb - QH * 27 / 30, "2", E.COR, 48, a=1 - ep(t, a5, 0.4))
    if t >= a5:
        qv = ep(t, b5, 0.5)
        agua(c, qx, QY, QW, QD, QH, 1.0, qv, 27 / 30, "#FFD500", 1.3)
        marca(c, t, a5, xm, yb - QH * 27 / 30, yb - QH, "3", TINTA, 48)
    X = 1400

    def cada():
        fcen(c, t, a4, "fundo: 50 × 30 = 1.500 cm²", X, 220, 62)
        fcen(c, t, b4, "subida: 27 − 25 = 2", X, 340, 66)
        fcen(c, t, c4, "1.500 × 2 = 3.000 cm³", X, 470, 66)
        E.frase(c, t, c4 + 1.0, ps("as 3 pedras", "i", 52, TINTA2), X, 550, "center", 0.1)
        fcen(c, t, d4, "3.000 ÷ 3 = 1.000 cm³", X, 680, 66, COR)
        bola_txt(c, t, e4, "1 L", X - 160, 870, 95, 72)
        E.frase(c, t, e4 + 0.4, ps("cada pedra", "i", 58), X - 30, 892, "left", 0.1)
    fase(c, t, C["s14"], C["s15"] - 0.1, cada)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.1, [("2)", "g", 60, COR)] + ps("pelo atalho", "i", 60), X, 210, "center", 0.1)
    fcen(c, t, a5, "faltam 30 − 27 = 3 cm", X, 330, 64)
    fcen(c, t, b5, "1.500 × 3 = 4.500 cm³ vazios", X, 450, 60)
    fcen(c, t, c5, "4 pedras: 4.000 ≤ 4.500", X - 60, 590, 62)
    E.foco(c, t, c5 + 0.6, 0.5, lambda q: E.selo(c, X + 370, 568, 38, True, q))
    fcen(c, t, d5, "5 pedras: 5.000 > 4.500", X - 60, 710, 62, ERRADO)
    E.foco(c, t, d5 + 0.6, 0.5, lambda q: E.selo(c, X + 370, 688, 38, False, q))
    bola_txt(c, t, e5, "+4", X - 140, 880, 95, 80)
    E.frase(c, t, e5 + 0.4, ps("mais 4 pedras", "i", 60), X - 20, 902, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s16.a", ps("volume do objeto =", "i", 62) + [("área do fundo × subida", "g", 62, COR)]),
                 ("s16.b", ps("transborda? compare com o", "i", 62) + [("espaço vazio", "g", 62, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 480 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 25, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 390, y, "left", 0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    E.frase(c, t, C["s17"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s17"] + 0.8, ps("um sólido", "i", 92) + [("dentro", "g", 110, COR)] + ps("do outro", "i", 92), XE, 410)
    E.frase(c, t, a7, ps("esfera no cubo de aresta 6:", "i", 56) + [("raio 3", "g", 60, COR)], XE, 540, passo=0.1)
    E.frase(c, t, b7, [("cone", "g", 60, COR)] + ps("dentro do", "i", 56) + [("cilindro", "g", 60, COR)], XE, 640, passo=0.1)
    E.frase(c, t, c7, ps("e o", "i", 60) + [("volume que sobra", "g", 64, COR)], XE, 760, passo=0.1)
    pts = E.cubo(c, t, a7, 1260, 900, 260)
    E.esfera(c, t, a7 + 0.5, 1260 + 130 + 0.5 * 0.394 * 260, 900 - 130 - 0.5 * 0.308 * 260, 130, inclina=18)
    E.cilindro(c, t, b7, 1700, 900, 110, 280, preenche=0.15)
    E.cone(c, t, b7 + 0.4, 1700, 900, 110, 280)
    E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d7 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(560, 355, p), ep(t, d7 + 0.2, 0.4))
    E.frase(c, t, e7, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1040, "center")


BLOCKS = dict(gancho=b_gancho_todo, lembrete=b_lembrete, ideia=b_ideia, pedra=b_pedra, copo=b_copo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
