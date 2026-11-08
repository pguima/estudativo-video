"""Visual — Estudativo · MAT-POL-012: praticando simetrias (cinco situações). Última aula da trilha Polígonos e Círculo.
Aula de prática no molde da MAT-POL-009 / MAT-ANG-009: selo de progresso "situação n de 5", figura à esquerda, pergunta embaixo à
direita e relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta aparece na coluna da direita.
Linguagem do plano (MAT-FUN-001, MAT-POL-011): eixo x em índigo, eixo y em tinta; par com o x em índigo e o y em preto; o eixo que
serve de espelho brilha (espelho()); a bandeirinha (mastro + pano índigo; o verso do pano, mais claro, quando está espelhada).
Linguagem da simetria (MAT-POL-010): eixos tracejados na cor da matéria; a folha que dobra em camadas e abre (folha()).
O relógio é o da MAT-ANG-001 (mostrador(), ponteiros()); no espelho, o ponteiro vira para o outro lado do eixo do 12 ao 6.
Peças locais: marca(), pergunta(), eixos(), par(), espelho(), bandeira(), folha(), mostrador(), ponteiros(), ps(), fcen(), bola_txt().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-POL-012_praticando_simetrias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
VERSO = E.mix(E.COR, "#FFFFFF", 0.55)
PAPEL_F, PAPEL_V, FURO = "#FFFFFF", "#E4E4EE", "#2A2A33"
assert (-1, 1) == (-1, 1) and (-4, 1) == (-4, 1) and (-1, 3) == (-1, 3)
assert (-2, 5) == (-2, 5) and (-5, -2) == (-5, -2) and 12 - 2 == 10
assert 180 - 90 == 90 and 90 // 2 == 45 and 45 + 45 == 90 and 2 + 2 == 4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def marca(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso (como na MAT-POL-009)"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=1500, y0=860):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * 100, "center", 0.12)
    E.relogio(c, t, rel, X, 430, 180)


def eixos(c, t, P, t0, size=32):
    """plano da MAT-FUN-001: grade, eixo x índigo e eixo y preto, com os números"""
    if t < t0:
        return
    x, y, w, h = P.caixa
    q = ep(t, t0, 0.8)
    for v in range(int(P.xmin), int(P.xmax) + 1):
        M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
    for v in range(int(P.ymin), int(P.ymax) + 1):
        M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 40, P.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 40, SAI, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (E.escreve(c, "x", x + w + 16, P.oy + 56, 54, "i", ENT, a),
                                           E.escreve(c, "y", P.ox + 20, y - 14, 54, "i", SAI, a)))
    for v in range(int(P.xmin), int(P.xmax) + 1):
        if v != 0:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, v=v: (M.line(c, P.x(v), P.oy - 9, P.x(v), P.oy + 9, ENT, a, 4),
                                                       centro(c, E._num(v), P.x(v), P.oy + 12 + size, size, "b", TINTA2, a)), sobe=6)
    for v in range(int(P.ymin), int(P.ymax) + 1):
        if v != 0:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, v=v: (M.line(c, P.ox - 9, P.y(v), P.ox + 9, P.y(v), SAI, a, 4),
                                                       E.escreve(c, E._num(v), P.ox - 16 - E.larg(E._num(v), "b", size), P.y(v) + size * 0.36,
                                                                 size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def espelho(c, t, t0, P, qual, t1=None, cor="#7CC4F5"):
    q = ep(t, t0, 0.5) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
    if q <= 0:
        return
    x, y, w, h = P.caixa
    if qual == "y":
        ret = skia.Rect.MakeXYWH(P.ox - 10, y - 20, 20, h + 40)
        a0, a1 = skia.Point(P.ox - 10, 0), skia.Point(P.ox + 10, 0)
    else:
        ret = skia.Rect.MakeXYWH(x - 20, P.oy - 10, w + 40, 20)
        a0, a1 = skia.Point(0, P.oy - 10), skia.Point(0, P.oy + 10)
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeLinear([a0, a1], [M.hexc(cor, 0.85 * q), M.hexc("#E8F6FF", 0.95 * q), M.hexc(cor, 0.85 * q)]))
    c.drawRect(ret, g)


def poli(c, pts, cor, a=1.0, alfa=0.25, larg=5, borda=TINTA, dash=False):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    if alfa > 0:
        c.drawPath(path, M.paint(cor, alfa * a))
    pa = M.paint(borda, a, stroke=larg); pa.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pa.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
    c.drawPath(path, pa)


BAND = [(0, 0), (0, 2), (1.5, 1.5), (0, 1)]   # pé do mastro, alto, ponta do pano, pé do pano (em unidades da malha)


def bandeira(c, P, f, a=1.0, verso=False, rotulo=None, t=0, t0=0):
    """bandeirinha: f leva os pontos de BAND para valores do plano"""
    if a <= 0:
        return
    pts = [P(*f(*q)) for q in BAND]
    path = skia.Path(); path.addPoly([pts[1], pts[2], pts[3]], True)
    c.drawPath(path, M.paint(VERSO if verso else E.COR, a))
    pa = M.paint(E.mix(E.COR, "#000000", 0.25), a, stroke=3); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pa)
    M.line(c, *pts[0], *pts[1], TINTA, a, 9)
    c.drawCircle(*pts[1], 10, M.paint(TINTA, a))


def hora(cx, cy, rr, h):
    a = math.radians(h * 30)
    return cx + rr * math.sin(a), cy - rr * math.cos(a)


def mostrador(c, cx, cy, r, a=1.0, numeros=(12, 3, 6, 9), size=None, fundo="#FFFFFF"):
    """mostrador da MAT-ANG-001: disco, 12 tracinhos e os números"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.16 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawCircle(cx + 6, cy + 12, r, s)
    c.drawCircle(cx, cy, r, M.paint(fundo, a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=max(4, r * 0.025)))
    for h in range(12):
        forte = h % 3 == 0
        M.line(c, *hora(cx, cy, r * (0.84 if forte else 0.89), h), *hora(cx, cy, r * 0.95, h), TINTA, a, max(3, r * (0.024 if forte else 0.012)))
    size = size or r * 0.17
    for n in numeros:
        x, y = hora(cx, cy, r * 0.70, n % 12)
        centro(c, str(n), x, y + size * 0.36, size, "g", TINTA, a)


def folha(c, x, y, w, h, p1=0.0, p2=0.0, recortes=(), a=1.0, vinco=0.0):
    """a folha da MAT-POL-010, com duas dobras: p1 = metade da direita sobre a esquerda; p2 = metade de baixo sobre a de cima.
    recortes = [(pontos, alfa_tracejado, alfa_cheio)] no quarto de cima à esquerda; cada pedaço desenha a sua cópia espelhada"""
    if a <= 0:
        return
    X1, Y1 = x + w / 2, y + h / 2
    c1, c2 = math.cos(math.pi * p1), math.cos(math.pi * p2)
    s1 = c1 if abs(c1) > 1e-3 else 1e-3
    s2 = c2 if abs(c2) > 1e-3 else 1e-3
    pecas = sorted(((i, j) for j in (0, 1) for i in (0, 1)), key=lambda q: (q[1] == 1 and p2 > 0.5) * 2 + (q[0] == 1 and p1 > 0.5))
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    for i, j in pecas:
        rx, ry = x + i * w / 2, y + j * h / 2
        c.save()
        if j == 1:
            c.translate(0, Y1); c.scale(1, s2); c.translate(0, -Y1)
        if i == 1:
            c.translate(X1, 0); c.scale(s1, 1); c.translate(-X1, 0)
        verso = (i == 1 and c1 < 0) != (j == 1 and c2 < 0)
        ret = skia.Rect.MakeXYWH(rx, ry, w / 2, h / 2)
        sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10))
        sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.drawRect(ret.makeOffset(4, 8), sombra)
        c.drawRect(ret, M.paint(PAPEL_V if verso else PAPEL_F))
        c.save(); c.clipRect(ret)
        mx = (lambda px: px) if i == 0 else (lambda px: 2 * X1 - px)
        my = (lambda py: py) if j == 0 else (lambda py: 2 * Y1 - py)
        for pts, ad, af in recortes:
            path = skia.Path(); path.addPoly([(mx(px), my(py)) for px, py in pts], True)
            if af > 0:
                c.drawPath(path, M.paint(E.COR, af))
            if ad > 0:
                pd = M.paint(TINTA, ad, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
                c.drawPath(path, pd)
        c.restore()
        for seg in ((rx, ry, rx + w / 2, ry) if j == 0 else None, (rx, ry + h / 2, rx + w / 2, ry + h / 2) if j == 1 else None,
                    (rx, ry, rx, ry + h / 2) if i == 0 else None, (rx + w / 2, ry, rx + w / 2, ry + h / 2) if i == 1 else None):
            if seg:
                M.line(c, *seg, TINTA2, 1.0, 3)
        if vinco > 0:
            if i == 0:
                M.line(c, rx + w / 2, ry, rx + w / 2, ry + h / 2, E.COR, vinco, 4, dash=[14, 10])
            if j == 0:
                M.line(c, rx, ry + h / 2, rx + w / 2, ry + h / 2, E.COR, vinco, 4, dash=[14, 10])
        c.restore()
    if a < 1:
        c.restore()


def eixo(c, t, t0, P, Q, cor=None, ext=50, larg=5, d=0.5, a=1.0):
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    A, B = (P[0] - ux * ext, P[1] - uy * ext), (Q[0] + ux * ext, Q[1] + uy * ext)
    M.line(c, *A, *B, cor or E.COR, a, larg, dash=[18, 12], progress=ease_io(prog(t, t0, d)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 1.0, ps("de simetria", "i", 80), XE, 480, passo=0.12)
    E.frase(c, t, a_ + 1.8, ps("criadas para esta aula", "i", 70, TINTA2), XE, 580, passo=0.12)
    for i, (s, cx, ti) in enumerate((("pause", 440, b_), ("resolva", 960, b_ + 0.9), ("confira", 1480, b_ + 2.0))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.6), ps("errar aqui", "i", 62) + [("ensina", "g", 66, COR)], W / 2, 980, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84, COR), XE, 220, passo=0.12)
    itens = (("a", "eixos de simetria"), ("b", "dobraduras"), ("c", "translação, reflexão e rotação"))
    for i, (k, s) in enumerate(itens):
        y = 420 + i * 190
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 40, y - 28, 46, 54, p))
        E.frase(c, t, ti + 0.1, [(s, "g", 70)], XE + 120, y)
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 60), XE, 980, passo=0.1)


# ---------------- situação 1: qual movimento ----------------
PG = E.Plano(170, 210, 1020, 600, 0, 17, 0, 10)      # malha sem eixos, 60 px por quadradinho
ORIG = (2, 5)
F_ORIG = lambda x, y: (ORIG[0] + x, ORIG[1] + y)
F_A = lambda x, y: (5 + x, 6 + y)                     # translação
F_B = lambda x, y: (12 - x, 5 + y)                    # reflexão: pano para a esquerda
F_C = lambda x, y: (16 - y, 2 + x)                    # rotação de 90° ao contrário do relógio, em volta do pé do mastro


def malha(c, t, t0):
    if t < t0:
        return
    q = ep(t, t0, 0.6)
    x, y, w, h = PG.caixa
    for v in range(18):
        M.line(c, PG.x(v), y, PG.x(v), y + h, FIO, q, 2)
    for v in range(11):
        M.line(c, x, PG.y(v), x + w, PG.y(v), FIO, q, 2)


def q1_fig(c, t, t0, tc):
    malha(c, t, t0)
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: bandeira(c, PG, F_ORIG, a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, "original", PG.x(2.6), PG.y(4.3), 40, "b", TINTA2, a))
    for k, (f, s, verso, pos) in enumerate(((F_A, "A", False, (5.3, 9.1)), (F_B, "B", True, (11.6, 8.1)), (F_C, "C", False, (14.8, 4.6)))):
        ti = tc + 0.4 * k
        E.foco(c, t, ti, 0.5, lambda a, f=f, verso=verso: bandeira(c, PG, f, a, verso))
        E.foco(c, t, ti + 0.2, 0.4, lambda a, s=s, pos=pos: num_bola(c, s, *PG(*pos), 30, 38, a))


def b_questao1(c, t, C, b):
    a3, b3, c3 = C["s03.a"], C["s03.b"], C["s03.c"]
    marca(c, t, a3, 1)
    q1_fig(c, t, a3 + 0.3, b3)
    pergunta(c, t, [(c3, ps("que", "i", 60) + [("movimento", "g", 64, COR)] + ps("levou", "i", 60)),
                    (c3 + 0.8, ps("a original até", "i", 60) + [("A, B e C?", "g", 64, COR)])], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C["s05." + k] for k in "abcde")
    X = 1500
    q1_fig(c, t, C["s05"] - 1.5, C["s05"] - 1.5)
    if t >= a5:  # A: a seta da translação
        M.arrow(c, *PG(2.2, 6.2), *PG(4.6, 7.2), CERTO, ep(t, a5, 0.3), 6, 22, ease_io(prog(t, a5, 0.6)))
    if t >= c5:  # B: o espelho entre a original e B
        eixo(c, t, c5, PG(7, 4.4), PG(7, 7.8), CERTO, ext=10)
    if t >= e5:  # C: o giro
        r = 70
        cx, cy = PG(16, 2)
        ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
        c.drawArc(ret, -90, -90 * ease_io(prog(t, e5, 0.6)), False, M.paint(CERTO, 1, stroke=6, cap_round=True))
    E.frase(c, t, a5, [("A:", "g", 64, COR), ("translação", "g", 64, CERTO)], X, 260, "center", 0.12)
    E.frase(c, t, a5 + 0.6, ps("mesmo jeito, outro lugar", "i", 50, TINTA2), X, 340, "center", 0.1)
    E.frase(c, t, b5, [("B:", "g", 64, COR)] + ps("pano virado", "i", 56), X, 480, "center", 0.12)
    E.frase(c, t, c5, ps("do avesso:", "i", 56) + [("reflexão", "g", 64, CERTO)], X, 570, "center", 0.12)
    E.frase(c, t, d5, [("C:", "g", 64, COR)] + ps("deitada", "i", 56), X, 720, "center", 0.12)
    E.frase(c, t, e5, ps("sobre a mesa:", "i", 56) + [("rotação", "g", 64, CERTO)], X, 810, "center", 0.12)


# ---------------- situação 2: refletir no eixo y ----------------
PQ = E.Plano(200, 200, 640, 640, -5, 5, -5, 5)
TRI = [(1, 1), (4, 1), (1, 3)]


def b_questao2(c, t, C, b):
    a6, b6, c6, d6, e6 = (C["s06." + k] for k in "abcde")
    marca(c, t, a6, 2)
    eixos(c, t, PQ, a6 + 0.2)
    if t >= d6 + 0.3:
        poli(c, [PQ(*p) for p in TRI], E.COR, ep(t, d6 + 0.3, 0.4), 0.25)
    for (x, y), ti, lado in zip(TRI, (b6, c6, d6), ((-1, 1), (1, 1), (-1, -1))):
        E.ponto(c, t, ti, PQ, x, y, None, r=12)
    espelho(c, t, e6, PQ, "y")
    pergunta(c, t, [(b6, ps("triângulo", "i", 58) + [("(1, 1), (4, 1), (1, 3)", "g", 56)]),
                    (e6, ps("refletido no", "i", 60) + [("eixo y?", "g", 64, COR)])], C["s07.a"])


def b_resposta2(c, t, C, b):
    a8, b8, c8, d8, e8 = (C["s08." + k] for k in "abcde")
    X = 1400
    t0 = C["s08"] - 1.5
    eixos(c, t, PQ, t0)
    espelho(c, t, t0, PQ, "y")
    poli(c, [PQ(*p) for p in TRI], E.COR, 1.0, 0.25)
    for (x, y) in TRI:
        c.drawCircle(*PQ(x, y), 11, M.paint(E.COR))
    for (x, y), ti in zip(TRI, (b8, c8, d8)):
        if t >= ti:
            M.line(c, *PQ(x, y), *PQ(-x, y), TINTA2, ep(t, ti, 0.3) * 0.8, 4, dash=[12, 9])
        E.ponto(c, t, ti + 0.2, PQ, -x, y, None, cor=CERTO, r=12)
    if t >= e8:
        poli(c, [PQ(-x, y) for x, y in TRI], VERSO, ep(t, e8, 0.4), 0.8)
    E.frase(c, t, a8, [("eixo y", "g", 66, SAI)] + ps("em pé:", "i", 60), X, 240, "center", 0.12)
    E.frase(c, t, a8 + 0.7, ps("muda o sinal do", "i", 58) + [("x", "g", 68, ENT)], X, 330, "center", 0.12)
    for k, (ti, xv, yv) in enumerate(((b8, "−1", "1"), (c8, "−4", "1"), (d8, "−1", "3"))):
        E.foco(c, t, ti, 0.5, lambda a, xv=xv, yv=yv, k=k: par(c, xv, yv, X, 480 + k * 110, 84, a, "center"))
    E.frase(c, t, e8, ps("aponta para a", "i", 58) + [("esquerda", "g", 64, COR)], X, 860, "center", 0.12)
    E.frase(c, t, e8 + 0.8, [("espelhado", "g", 70, CERTO)], X, 960, "center")


# ---------------- situação 3: meia volta ----------------
PR = E.Plano(200, 200, 640, 640, -6, 6, -6, 6)


def arco_giro(c, t, t0, P, g0, g1, r, cor, d=0.8):
    """arco de giro em volta da origem, de g0 a g1 (graus, anti-horário)"""
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    O = P(0, 0)
    rr = r * (P.x(1) - P.x(0))
    ret = skia.Rect.MakeXYWH(O[0] - rr, O[1] - rr, 2 * rr, 2 * rr)
    c.drawArc(ret, -g0, -(g1 - g0) * q, False, M.paint(cor, 1, stroke=5, cap_round=True))


def b_questao3(c, t, C, b):
    a9, b9, c9, d9 = (C["s09." + k] for k in "abcd")
    marca(c, t, a9, 3)
    eixos(c, t, PR, a9 + 0.2)
    E.ponto(c, t, b9, PR, 5, 2, None, r=13)
    E.foco(c, t, b9 + 0.3, 0.4, lambda a: par(c, "5", "2", PR.x(5) - 90, PR.y(2) - 30, 44, a))
    if t >= c9:
        g0 = math.degrees(math.atan2(2, 5))
        arco_giro(c, t, c9, PR, g0 + 8, g0 + 55, math.hypot(5, 2), TINTA2, 0.8)
        if t >= c9 + 0.8:  # a ponta da seta: só o sentido, sem entregar onde para
            g = math.radians(g0 + 55)
            R_ = math.hypot(5, 2) * (PR.x(1) - PR.x(0))
            O = PR(0, 0)
            tip = (O[0] + R_ * math.cos(g), O[1] - R_ * math.sin(g))
            ux, uy = -math.sin(g), -math.cos(g)
            nx, ny = math.cos(g), -math.sin(g)
            for s_ in (-1, 1):
                M.line(c, *tip, tip[0] - ux * 22 + nx * 14 * s_, tip[1] - uy * 22 + ny * 14 * s_, TINTA2, 1, 5)
        k = ease_back(prog(t, c9, 0.4))
        if k > 0:
            c.drawCircle(*PR(0, 0), 13 * k, M.paint(E.COR))
    pergunta(c, t, [(c9, [("meia volta: 180°", "g", 64, COR)]), (d9, ps("em volta da origem:", "i", 60) + [("onde?", "g", 64, COR)])], C["s10.a"])


def b_resposta3(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    X = 1400
    t0 = C["s11"] - 1.5
    eixos(c, t, PR, t0)
    E.ponto(c, t, t0, PR, 5, 2, None, r=13)
    c.drawCircle(*PR(0, 0), 12, M.paint(E.COR))
    R = math.hypot(5, 2)
    g0 = math.degrees(math.atan2(2, 5))
    if t >= b11:
        arco_giro(c, t, b11, PR, g0, g0 + 90, R, E.COR)
        for P_ in ((5, 2), (-2, 5)):
            M.line(c, *PR(0, 0), *PR(*P_), TINTA2, ep(t, b11, 0.3) * 0.7, 3, dash=[10, 8])
    E.ponto(c, t, c11, PR, -2, 5, None, cor=TINTA2, r=13)
    E.foco(c, t, c11 + 0.3, 0.4, lambda a: par(c, "−2", "5", PR.x(-2) - 200, PR.y(5) - 24, 44, a))
    if t >= a12:
        arco_giro(c, t, a12, PR, g0 + 90, g0 + 180, R, CERTO)
        M.line(c, *PR(0, 0), *PR(-5, -2), TINTA2, ep(t, a12, 0.3) * 0.7, 3, dash=[10, 8])
    E.ponto(c, t, b12, PR, -5, -2, None, cor=CERTO, r=13)
    E.foco(c, t, b12 + 0.3, 0.4, lambda a: par(c, "−5", "−2", PR.x(-5) - 20, PR.y(-2) + 66, 44, a, cores=(CERTO, CERTO)))

    def um():
        E.frase(c, t, a11, [("180°", "g", 72, COR)] + ps("= 2 giros de 90°", "i", 60), X, 240, "center", 0.12)
        E.frase(c, t, b11, ps("1º giro: troca e muda o sinal do 1º", "i", 50), X, 400, "center", 0.08)
        E.foco(c, t, b11 + 1.0, 0.4, lambda a: (par(c, "5", "2", X - 330, 520, 80, a), E.escreve(c, "→", X - 50, 520, 80, "g", TINTA2, a)))
        E.foco(c, t, c11, 0.5, lambda a: par(c, "−2", "5", X + 50, 520, 80, a))
    E.saida(c, t, C["s12"] - 0.1, um)
    if t >= C["s12"]:
        E.frase(c, t, a12, ps("2º giro: troca", "i", 56), X, 240, "center", 0.1)
        E.foco(c, t, a12 + 0.6, 0.4, lambda a: (par(c, "−2", "5", X - 360, 350, 76, a), E.escreve(c, "→", X - 60, 350, 76, "g", TINTA2, a),
                                                par(c, "5", "−2", X + 40, 350, 76, a)))
        E.frase(c, t, lerp(a12, b12, 0.6), ps("muda o sinal do 1º", "i", 56), X, 470, "center", 0.1)
        E.foco(c, t, b12, 0.5, lambda a: par(c, "−5", "−2", X, 620, 110, a, "center", cores=(CERTO, CERTO)))
        E.foco(c, t, c12, 0.5, lambda a: E.pilula(c, "meia volta: os dois trocam de sinal", X, 800, 48, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, c12 + 0.6, 0.5, lambda a: (par(c, "5", "2", X - 300, 950, 80, a), E.escreve(c, "→", X - 40, 950, 80, "g", TINTA2, a),
                                                par(c, "−5", "−2", X + 60, 950, 80, a)))


# ---------------- situação 4: o relógio no espelho ----------------
def moldura(c, cx, cy, w, h, a=1.0):
    """moldura do espelho, com o vidro azulado e um reflexo em faixa"""
    if a <= 0:
        return
    ret = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30)
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - w / 2, cy - h / 2), skia.Point(cx + w / 2, cy + h / 2)],
                                                [M.hexc("#DDF0FC", a), M.hexc("#B9DDF4", a)]))
    c.drawRRect(ret, g)
    c.drawRRect(ret, M.paint("#8A8A90", a, stroke=14))


def brilho(c, cx, cy, w, h, a=1.0):
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30))
    path = skia.Path()
    path.addPoly([(cx - w / 2 + 40, cy + h / 2), (cx - w / 2 + 140, cy + h / 2), (cx + w / 2 - 40, cy - h / 2), (cx + w / 2 - 140, cy - h / 2)], True)
    c.drawPath(path, M.paint("#FFFFFF", 0.35 * a))
    c.restore()


def relogio_espelho(c, t, t0, cx, cy, r):
    a = ep(t, t0, 0.5)
    moldura(c, cx, cy, 2 * r + 120, 2 * r + 120, a)
    mostrador(c, cx, cy, r, a, numeros=())
    if a > 0:
        M.line(c, cx, cy, *hora(cx, cy, r * 0.62, 0), TINTA, a, max(5, r * 0.03))
        M.line(c, cx, cy, *hora(cx, cy, r * 0.42, 2), TINTA, a, max(7, r * 0.05))
        c.drawCircle(cx, cy, max(7, r * 0.045), M.paint(TINTA, a))
    brilho(c, cx, cy, 2 * r + 120, 2 * r + 120, a)


def b_questao4(c, t, C, b):
    a13, b13, c13, d13 = (C["s13." + k] for k in "abcd")
    marca(c, t, a13, 4)
    relogio_espelho(c, t, b13, 560, 540, 260)
    E.foco(c, t, b13 + 0.3, 0.4, lambda a: centro(c, "espelho", 560, 980, 56, "i", TINTA2, a))
    pergunta(c, t, [(c13, ps("no espelho:", "i", 60) + [("2 h", "g", 70, COR)]),
                    (d13, ps("que horas", "i", 60) + [("são de verdade?", "g", 64, COR)])], C["s14.a"])


def b_resposta4(c, t, C, b):
    a15, b15, c15, d15, e15, f15 = (C["s15." + k] for k in "abcdef")
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    X = 1450
    cx, cy, r = 560, 560, 320
    mostrador(c, cx, cy, r, ep(t, C["s15"] - 1.0, 0.5), numeros=range(1, 13), size=50)
    eixo(c, t, a15, (cx, cy - r), (cx, cy + r), ext=50, larg=6)
    if b15 <= t < c15 + 1:
        for h in (0, 6):
            k = 1 + 0.4 * math.sin(math.pi * M.clamp(prog(t, b15, 0.8)))
            x, y = hora(cx, cy, r * 0.70, h)
            c.drawCircle(x, y, 44 * k, M.paint(E.COR, 0.25))
    if t >= c15:  # direita e esquerda trocam
        for h in (2, 3, 4):
            x1, y1 = hora(cx, cy, r * 0.70, h)
            x2, y2 = hora(cx, cy, r * 0.70, 12 - h)
            M.line(c, x1 - 30, y1, x2 + 30, y2, TINTA2, ep(t, c15 + 0.1 * (h - 2), 0.3) * 0.7, 3, dash=[10, 8])
    # pares do outro lado, no atalho
    if t >= c16:
        for h in (1, 5):
            x1, y1 = hora(cx, cy, r * 0.70, h)
            x2, y2 = hora(cx, cy, r * 0.70, 12 - h)
            M.line(c, x1 - 30, y1, x2 + 30, y2, CERTO, ep(t, c16 + 0.2 * (h > 1), 0.3) * 0.8, 4, dash=[10, 8])
    # o ponteiro das horas: no 2, depois espelhado até o 10
    q = ease_io(prog(t, e15, 1.0))
    tx, ty = hora(cx, cy, r * 0.42, 2)
    tip = (cx + (tx - cx) * math.cos(math.pi * q), ty)
    M.line(c, cx, cy, *hora(cx, cy, r * 0.62, 0), TINTA, 1, 9)
    M.line(c, cx, cy, *tip, E.COR if t >= d15 else TINTA, 1, 14)
    c.drawCircle(cx, cy, 14, M.paint(TINTA))
    if t >= e15:
        M.line(c, cx, cy, tx, ty, TINTA2, 0.5 * (1 - ep(t, e15 + 1.4, 0.4)), 8, dash=[10, 8])

    def um():
        E.frase(c, t, a15, ps("eixo:", "i", 60) + [("do 12 ao 6", "g", 66, COR)], X, 240, "center", 0.12)
        E.frase(c, t, b15, ps("12 e 6", "g", 60) + ps("ficam no lugar", "i", 56), X, 360, "center", 0.12)
        E.frase(c, t, c15, [("direita", "g", 62)] + ps("troca com", "i", 56) + [("esquerda", "g", 62)], X, 480, "center", 0.12)
        E.frase(c, t, d15, ps("no espelho:", "i", 56) + [("2 à direita", "g", 62, COR)], X, 620, "center", 0.12)
        E.frase(c, t, e15, ps("de verdade:", "i", 56) + [("2 à esquerda", "g", 62, COR)], X, 730, "center", 0.12)
        bola_txt(c, t, f15, "10 h", X, 880, 100, 70, CERTO)
    E.saida(c, t, C["s16"] - 0.1, um)
    if t >= C["s16"]:
        E.frase(c, t, a16, ps("hora cheia:", "i", 60) + [("12 − espelho", "g", 64, COR)], X, 260, "center", 0.12)
        fcen(c, t, b16, "12 − 2 = 10", X, 420, 96, CERTO)
        E.frase(c, t, c16, ps("cada hora troca com a do", "i", 52), X, 580, "center", 0.1)
        E.frase(c, t, c16 + 0.8, [("outro lado", "g", 62, CERTO)] + ps("do eixo", "i", 52), X, 660, "center", 0.12)
        E.foco(c, t, d16, 0.5, lambda a: E.pilula(c, "com minutos, a conta muda", X, 830, 52, "g", fundo=ERRADO, a=a))


# ---------------- situação 5: a dobradura ----------------
FX, FY, FL = 200, 210, 640          # folha quadrada
FU = 80                             # 1 cm = 80 px
X1, Y1 = FX + FL / 2, FY + FL / 2
CORTE = [(X1, Y1), (X1 - 2 * FU, Y1), (X1, Y1 - 2 * FU)]


def b_questao5(c, t, C, b):
    a17, b17, c17, d17, e17, f17 = (C["s17." + k] for k in "abcdef")
    marca(c, t, a17, 5)
    p1 = ease_io(prog(t, b17, 0.8))
    p2 = ease_io(prog(t, c17, 0.8))
    ad = ep(t, d17, 0.3)
    folha(c, FX, FY, FL, FL, p1, p2, recortes=[(CORTE, ad, 0.0)], a=ep(t, a17, 0.4))
    if t >= d17:  # o canto das dobras
        k = 1 + 0.4 * math.sin(math.pi * M.clamp(prog(t, d17, 0.8)))
        c.drawCircle(X1, Y1, 12 * k, M.paint(E.COR))
    E.foco(c, t, e17, 0.4, lambda a: (E._cola(c, "2 cm", X1 - FU, Y1, 0, 1, 14, 46, "b", COR, a),
                                      E._cola(c, "2 cm", X1, Y1 - FU, 1, 0, 14, 46, "b", COR, a)))
    pergunta(c, t, [(d17, ps("triângulo no", "i", 58) + [("canto das dobras", "g", 60, COR)]),
                    (f17, ps("que figura?", "i", 60) + [("quantos eixos?", "g", 64, COR)])], C["s18.a"])


def b_resposta5(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    X = 1450
    t0 = C["s19"] - 1.5
    p1 = 1 - ease_io(prog(t, b19 + 0.5, 0.7))
    p2 = 1 - ease_io(prog(t, b19, 0.6))
    folha(c, FX, FY, FL, FL, p1, p2, recortes=[(CORTE, 0.0, 1.0)], vinco=ep(t, b19 + 1.2, 0.4), a=1.0)
    if a19 <= t < b19 + 0.4:
        k = 1 + 0.4 * math.sin(math.pi * M.clamp(prog(t, a19, 0.8)))
        c.drawCircle(X1, Y1, 16 * k, M.paint(CERTO))
    Q = [(X1 - 2 * FU, Y1), (X1, Y1 - 2 * FU), (X1 + 2 * FU, Y1), (X1, Y1 + 2 * FU)]
    if t >= c19:  # a figura junta: um quadrado em pé sobre uma ponta
        poli(c, Q, E.COR, ep(t, c19, 0.4), 0.0, 6, TINTA)
    if t >= a20:  # um dos triângulos
        poli(c, [(X1, Y1), (X1 + 2 * FU, Y1), (X1, Y1 - 2 * FU)], CERTO, ep(t, a20, 0.4) * (1 - ep(t, b20, 0.4)), 0.5, 4, TINTA)
        E.angulo(c, t, a20 + 0.3, (X1, Y1), (X1 + 2 * FU, Y1), (X1, Y1 - 2 * FU), r=26, reto=True, cor=BR)
    if t >= c20:  # de ponta a ponta: 2 + 2
        M.line(c, X1 - 2 * FU, Y1, X1 + 2 * FU, Y1, CLARO, ep(t, c20, 0.3), 9)
        E.foco(c, t, c20, 0.4, lambda a: centro(c, "4 cm", X1, Y1 + 2 * FU + 70, 60, "g", COR, a))
    if t >= d20:
        for k, (P, Q_) in enumerate((((X1, Y1 - 3 * FU), (X1, Y1 + 3 * FU)), ((X1 - 3 * FU, Y1), (X1 + 3 * FU, Y1)),
                                     ((X1 - 2 * FU, Y1 - 2 * FU), (X1 + 2 * FU, Y1 + 2 * FU)), ((X1 - 2 * FU, Y1 + 2 * FU), (X1 + 2 * FU, Y1 - 2 * FU)))):
            eixo(c, t, d20 + 0.2 * k, P, Q_, CERTO if k < 2 else E.COR, ext=10, larg=5)

    def um():
        E.frase(c, t, a19, ps("canto das dobras =", "i", 56) + [("centro", "g", 62, CERTO)], X, 260, "center", 0.12)
        E.frase(c, t, b19, [("4 triângulos", "g", 70, COR)] + ps("iguais", "i", 60), X, 420, "center", 0.12)
        E.frase(c, t, c19, ps("encostam nas dobras:", "i", 56), X, 580, "center", 0.12)
        E.frase(c, t, c19 + 0.7, [("uma figura só", "g", 68, COR)], X, 680, "center")
    E.saida(c, t, C["s20"] - 0.1, um)
    if t >= C["s20"]:
        E.frase(c, t, a20, ps("canto reto e lados de 2:", "i", 54), X, 200, "center", 0.1)
        fcen(c, t, a20 + 1.0, "180 − 90 = 90", X, 300, 64)
        fcen(c, t, lerp(a20, b20, 0.4), "90 ÷ 2 = 45°", X, 400, 64)
        fcen(c, t, lerp(a20, b20, 0.75), "45 + 45 = 90°", X, 500, 64, COR)
        E.frase(c, t, b20, [("quadrado", "g", 70, COR)] + ps("em pé numa ponta", "i", 54), X, 630, "center", 0.12)
        fcen(c, t, c20, "2 + 2 = 4 cm", X, 750, 70)
        bola_txt(c, t, d20, "4", X - 130, 900, 80, 90, CERTO)
        E.frase(c, t, d20 + 0.3, [("eixos", "g", 70, CERTO)], X - 20, 925, "left")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", "dobra", "é espelho"), ("s21.b", "em pé: sinal do x;", "deitado: do y"), ("s21.c", "reconhecer:", "gire ou vire do avesso"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 66, COR), (l2, "i", 68)], 350, y, "left", 0.2)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("trilha", "i", 70) + [("fechada!", "g", 76, CERTO)], XE, 230, passo=0.12)
    E.frase(c, t, C["s22"] + 1.5, ps("próxima aula", "i", 70), XE, 340)
    E.frase(c, t, C["s22.a"], [("Áreas e", "g", 110, COR)], XE, 470)
    E.frase(c, t, C["s22.a"] + 0.4, [("perímetros", "g", 110, COR)], XE, 590)
    # o terreno de 20 m por 35 m e a cerca em volta
    if t >= C["s22.b"]:
        x, y, w, h = 300, 660, 560, 320
        q = ease_io(prog(t, C["s22.b"], 1.2))
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(CERTO, 0.12 * ep(t, C["s22.b"], 0.4)))
        E._contorno(c, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], q, E.COR, 8)
        E.foco(c, t, C["s22.b"] + 0.6, 0.4, lambda a: (centro(c, "35 m", x + w / 2, y + h + 64, 54, "g", TINTA, a),
                                                        E.escreve(c, "20 m", x + w + 20, y + h / 2 + 18, 54, "g", TINTA, a)))
        E.foco(c, t, C["s22.b"] + 1.2, 0.4, lambda a: centro(c, "cerca?", x + w / 2, y + h / 2 + 22, 64, "g", COR, a))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1450, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
