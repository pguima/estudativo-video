"""Visual — Estudativo · MAT-TRI-011: gráficos de seno, cosseno e tangente (período 2π, imagem [−1, 1]; tangente com galhos,
período π; y = 3 sen x com imagem [−3, 3] e período 2π).
Duas linguagens juntas:
- Trigonometria (MAT-TRI-001, 007, 008): o seno é a altura (âmbar, OPO), o cosseno a largura (petróleo, ADJ); no ciclo, o raio em tinta
  e o arco do ângulo na cor da matéria. Por isso a ONDA DO SENO é âmbar e a DO COSSENO é petróleo; a tangente sai em índigo.
- Funções (MAT-FUN-001 e 007): o eixo x (a entrada, o ângulo) em índigo e o eixo y (a saída) em preto; imagem = barra preta em pé
  sobre o eixo y (bolinha cheia = entra); o eixo x é marcado em radianos, com os graus embaixo, numa régua abaixo do gráfico.
- Período = colchete sobre um pedaço da onda, com o trecho repintado mais grosso. Assíntota = linha tracejada que a curva não toca.
Resposta na pílula; erro em vermelho, certo em verde; atalho no palco escuro.
A figura não mente: as curvas são sen, cos e tg de verdade; o ponto do gancho gira e a altura dele desenha a onda ao lado.
Peças locais: eixos() (régua de radianos e graus), curva_a() (curva com transparência), barra_y() (imagem), periodo(), ciclo_gira(),
tabela() (os 5 pontos fáceis), resp(). Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-011_graficos_de_seno_cosseno_e_tangente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("seno", "cosseno", "tangente", "vezes3", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
OPO, ADJ, ADJ_ESC = AMBAR, "#0E9AA7", "#3CC7D3"
TGC = E.COR                # a tangente
ENT, SAI = E.COR, TINTA    # eixo x (ângulo) e eixo y (valor)
PI = math.pi
sen, cos, tg = math.sin, math.cos, math.tan
assert abs(sen(PI / 2) - 1) < 1e-12 and abs(sen(3 * PI / 2) + 1) < 1e-12 and abs(cos(PI) + 1) < 1e-12 and 2 * cos(PI) == -2
assert 3 * 1 == 3 and 3 * -1 == -3 and abs(3 * 2 * PI - 6 * PI) < 1e-12

MARCAS = [(0, "0", "0°"), (PI / 2, "f{π}{2}", "90°"), (PI, "π", "180°"), (3 * PI / 2, "f{3π}{2}", "270°"), (2 * PI, "2π", "360°")]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: [(texto, cor), ...]; y = linha de base. Devolve a largura"""
    w = sum(_w(s, size, est) for s, _ in partes)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for s, cor in partes:
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += _w(s, size, est)
    return w


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=70, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size, 0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def eixos(c, t, P, tx, ty=None, tl=None, marcas=MARCAS, graus=True, ys=(1, -1), extra=(), escuro=False, a=1.0, size=50, grade=True):
    """eixo x (ângulo) em índigo em tx, eixo y (valor) em preto em ty; régua de radianos (e graus) embaixo do gráfico, cada marca
    no seu instante tl[i] (ou todas em tl). extra = posições com traço e grade, sem rótulo"""
    if a <= 0 or t < tx:
        return
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    tinta = BR if escuro else SAI
    ent = CLARO if escuro else ENT
    lay = a < 1
    if lay:
        pt = skia.Paint(); pt.setAlphaf(a); c.saveLayer(None, pt)
    todas = [m[0] for m in marcas] + list(extra)
    if grade:
        q = ep(t, tx, 0.8) * (0.25 if escuro else 1)
        for v in todas:
            M.line(c, P.x(v), y, P.x(v), y + h, CLARO if escuro else FIO, q, 2)
        for v in ys:
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ent, 1.0, 6, 24, ep(t, tx, 0.7))
    E.foco(c, t, tx + 0.5, 0.4, lambda b: E.escreve(c, "x", x + w + 24, P.oy + 52, 50, "i", ent, b))
    for v in todas:
        X = P.x(v)
        E.foco(c, t, tx + 0.3, 0.4, lambda b, X=X: M.line(c, X, P.oy - 10, X, P.oy + 10, ent, b, 4), sobe=4)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, tinta, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda b: E.escreve(c, "y", P.ox + 22, y - 10, 50, "i", tinta, b))
        for v in ys:
            Y = P.y(v)
            s = E._num(v).replace("-", "−")
            E.foco(c, t, ty + 0.3, 0.4, lambda b, Y=Y, s=s: (M.line(c, P.ox - 10, Y, P.ox + 10, Y, tinta, b, 4),
                                                            E.escreve(c, s, P.ox - 22 - E.larg(s, "b", size), Y + size * 0.36, size, "b", tinta, b)))
    if tl is not None:
        tls = tl if isinstance(tl, (list, tuple)) else [tl + 0.08 * i for i in range(len(marcas))]
        for (v, rad, gr), tt in zip(marcas, tls):
            X = P.x(v)
            E.foco(c, t, tt, 0.4, lambda b, X=X, rad=rad, gr=gr: (
                E.formula(c, rad, X, y + h + 62, size, "g", ent, b, "center"),
                graus and centro(c, gr, X, y + h + 128, size * 0.8, "b", CINZA if not escuro else CLARO, b)))
    if lay:
        c.restore()


def curva_a(c, t, t0, P, f, a_, b_, d=1.2, cor=None, alfa=1.0, largura=8, tracejada=False):
    if alfa <= 0 or t < t0:
        return
    if alfa < 1:
        pt = skia.Paint(); pt.setAlphaf(alfa); c.saveLayer(None, pt)
    E.curva(c, t, t0, P, f, a_, b_, d=d, cor=cor, largura=largura, tracejada=tracejada)
    if alfa < 1:
        c.restore()


def barra_y(c, t, t0, P, a_, b_, cor=SAI, d=0.8, larg=14, r=15, fundo=None, setas=False):
    """imagem: o trecho do eixo y ocupado pela onda (bolinha cheia = entra); setas=True = sem fim nos dois sentidos"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    fundo = fundo or E.PAPEL
    y0, y1 = P.y(a_), P.y(b_)
    m = (y0 + y1) / 2
    M.line(c, P.ox, lerp(m, y0, p), P.ox, lerp(m, y1, p), cor, 0.85, larg)
    q = ep(t, t0 + d * 0.6, 0.3)
    if setas:
        for Y, s in ((y0, 1), (y1, -1)):
            M.arrow(c, P.ox, Y - s * 30, P.ox, Y + s * 6, cor, q, larg, 34, 1.0)
        return
    for Y in (y0, y1):
        c.drawCircle(P.ox, Y, r, M.paint(cor, q))


def periodo(c, t, t0, P, x0, x1, yv, rot, cor=None, size=54, f=None, cor_f=None, d=0.6):
    """colchete acima da onda de x0 a x1 (na altura yv), com o rótulo; f repinta o trecho mais grosso"""
    if t < t0:
        return
    cor = cor or COR
    p = ease_out(prog(t, t0, d))
    if f is not None:
        E.curva(c, t, t0, P, f, x0, x1, d=0.01, cor=cor_f or cor, largura=15)
    Y = P.y(yv)
    E.chave(c, P.x(x0), P.x(x1), Y, cor, p, -26, 6)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rot, (P.x(x0) + P.x(x1)) / 2, Y - 50, size, "g", cor, a, "center"))


def tabela(c, t, ts, pares, x0, y, passo_x, size=50, cor=OPO):
    """os pontos fáceis numa linha: "0° → 0", cada um no seu instante"""
    for i, ((g, v), tt) in enumerate(zip(pares, ts)):
        X = x0 + i * passo_x
        E.foco(c, t, tt, 0.4, lambda a, X=X, g=g, v=v: cf(c, [(g, TINTA), (" → ", TINTA2), (v, cor)], X, y, size, a, "center"))


def pt_c(cx, cy, r, ang):
    return cx + r * math.cos(ang), cy - r * math.sin(ang)


def ciclo_gira(c, t, t0, cx, cy, r, ang, escuro=False):
    """ciclo com o ponto no ângulo ang (radianos), o raio, o arco percorrido (na volta atual) e a altura (seno) em âmbar"""
    if t < t0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6)
    M.arrow(c, cx - r - 50, cy, cx + r + 60, cy, tinta, q, 4, 18, q)
    M.arrow(c, cx, cy + r + 50, cx, cy - r - 60, tinta, q, 4, 18, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    if t < t0 + 0.9:
        return
    k = ep(t, t0 + 0.9, 0.4)
    resto = math.degrees(ang) % 360
    if resto > 0.5:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -resto, False, M.paint(E.COR, k * 0.5, stroke=9, cap_round=True))
    X, Y = pt_c(cx, cy, r, ang)
    M.line(c, cx, cy, X, Y, tinta, k, 5)
    M.line(c, X, cy, X, Y, OPO, k, 12, cap_round=False)
    c.drawCircle(X, Y, 14 * k, M.paint(E.COR))
    c.drawCircle(X, Y, 14 * k, M.paint(BR, k, stroke=3))
    return X, Y


# ---------------- gancho ----------------
GCX, GCY, GCR = 330, 560, 175
PG = E.Plano(700, GCY - 1.3 * GCR, 1040, 2.6 * GCR, 0, 4 * PI, -1.3, 1.3)  # 1 unidade de y = o raio do ciclo


def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]

    def um():
        dur = max(4.0, b1 - a1 - 0.4)
        ang = 4 * PI * ease_io(prog(t, a1 + 0.9, dur)) if t >= a1 + 0.9 else 0.0
        eixos(c, t, PG, a1 + 0.3, tl=None, marcas=[], ys=(), grade=False)
        r = ciclo_gira(c, t, a1, GCX, GCY, GCR, ang)
        if t >= a1 + 0.9 and r:
            X, Y = r
            curva_a(c, t, a1 + 0.9, PG, sen, 0, max(ang, 1e-3), d=0.001, cor=OPO, largura=9)
            Xw, Yw = PG(ang, sen(ang))
            M.line(c, X, Y, Xw, Yw, TINTA2, 0.6, 3, dash=E.TRACO)
            c.drawCircle(Xw, Yw, 12, M.paint(OPO))
        E.frase(c, t, lerp(a1, b1, 0.3), ps("acompanhe só", "i", 64) + [("a altura", "g", 70, OPO)], XE, 200, "left", 0.1)
        E.frase(c, t, b1, ps("a altura vira", "i", 64) + [("uma onda", "g", 76, OPO)], XE, 930, "left", 0.1)
        E.foco(c, t, b1 + 1.4, 0.5, lambda a: E.formula(c, "y = sen x", 1300, 200, 80, "g", OPO, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 640, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula, a onda", "i", 76), XE, 260, passo=0.12)
        E.frase(c, t, ta + 1.6, ps("do", "i", 76) + [("seno,", "g", 86, OPO)] + ps("do", "i", 76) + [("cosseno", "g", 86, ADJ)], XE, 400, passo=0.14)
        E.frase(c, t, ta + 2.6, ps("e da", "i", 76) + [("tangente", "g", 86, TGC)], XE, 530, passo=0.14)
        E.frase(c, t, tb, [("período", "g", 80, COR)] + ps("e", "i", 72) + [("imagem", "g", 80)], XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 625, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 710, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 860, 960
    itens = (("s03.b", "no ciclo:",
              lambda a, y: cf(c, [("sen", OPO), (" = altura (vertical),  ", TINTA), ("cos", ADJ), (" no horizontal", TINTA)], x + 44, y, 46, a)),
             ("s03.c", "num gráfico, a imagem:",
              lambda a, y: cf(c, [("a sombra da curva no eixo y", COR)], x + 44, y, 56, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 260 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, fn=fn, y=y: fn(a, y + 168))
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 730, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 860, 960, "left", 0.12)


# ---------------- o gráfico principal (seno, cosseno, tangente, vezes 3) ----------------
GX, GY, GW, GH = 230, 330, 1460, 500
P1 = E.Plano(GX, GY, GW, GH, -PI, 3 * PI, -1.6, 1.6)
EXTRA = (-PI, -PI / 2, 5 * PI / 2, 3 * PI)


def b_seno(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    tl = [c4 + 1.0 + 0.7 * i for i in range(5)]
    eixos(c, t, P1, a4, b4, tl, extra=EXTRA)
    # os cinco pontos fáceis
    pontos = [(0, 0, a5), (PI / 2, 1, b5), (PI, 0, c5), (3 * PI / 2, -1, d5), (2 * PI, 0, e5)]
    for xv, yv, tt in pontos:
        E.ponto(c, t, tt, P1, xv, yv, None, cor=OPO, r=15)
    # a curva: uma volta, depois para os dois lados
    curva_a(c, t, a6, P1, sen, 0, 2 * PI, d=2.6, cor=OPO, largura=9)
    curva_a(c, t, c6, P1, sen, 2 * PI, 3 * PI, d=1.2, cor=OPO, largura=9)
    if t >= c6:  # o lado esquerdo cresce do zero para a esquerda
        p = ease_io(prog(t, c6, 1.2))
        if p > 0:
            E.curva(c, t, c6 - 5, P1, sen, -PI * p, 0, d=0.01, cor=OPO, largura=9)
    periodo(c, t, a7, P1, 0, 2 * PI, 1.42, "2π  (360°)" if t >= b7 else None, f=sen, cor_f=OPO)
    barra_y(c, t, c7, P1, -1, 1)

    def topo4():
        E.frase(c, t, a4, ps("o ângulo no", "i", 60) + [("eixo x", "g", 64, ENT)], XE, 140, "left", 0.1)
        E.frase(c, t, b4, ps("o seno dele no", "i", 60) + [("eixo y", "g", 64, SAI)], XE, 230, "left", 0.1)
        E.frase(c, t, c4, ps("na prova,", "i", 56) + [("em radianos", "g", 60, COR)], 1150, 140, "left", 0.1)
        E.foco(c, t, c4 + 1.0, 0.4, lambda a: cf(c, [("90° = f{π}{2}", COR), ("    volta = 2π", COR)], 1150, 240, 50, a))
    E.saida(c, t, a5 - 0.2, topo4)
    if a5 - 0.2 <= t:
        def topo5():
            E.frase(c, t, a5 - 0.1, ps("os pontos fáceis do ciclo", "i", 56, TINTA2), W / 2, 120, "center", 0.08)
            tabela(c, t, [a5, b5, c5, d5, e5], [("0°", "0"), ("90°", "1"), ("180°", "0"), ("270°", "−1"), ("360°", "0")], 360, 225, 300)
        E.saida(c, t, a6 - 0.2, topo5)
    if a6 - 0.2 <= t:
        def topo6():
            E.frase(c, t, a6, ps("sai do 0, sobe até 1, desce até −1, volta ao 0", "i", 54), W / 2, 150, "center", 0.07)
            E.frase(c, t, b6, ps("depois de uma volta, os mesmos pontos:", "i", 50, TINTA2) + [("390° → 30°", "g", 54, COR)], W / 2, 240, "center", 0.07)
        E.saida(c, t, c6 + 0.2, topo6)
    if c6 + 0.2 <= t:
        def topo6b():
            E.frase(c, t, c6 + 0.2, ps("o desenho", "i", 64) + [("se repete para sempre", "g", 68, OPO)], W / 2, 180, "center", 0.1)
        E.saida(c, t, a7 - 0.2, topo6b)
    if a7 - 0.2 <= t:
        E.frase(c, t, a7, ps("o pedaço que se repete:", "i", 58) + [("o período", "g", 64, COR)], XE, 150, "left", 0.1)
        E.frase(c, t, c7, ps("imagem: de", "i", 58) + [("−1 a 1", "g", 64, SAI)], 1200, 150, "left", 0.1)


def b_cosseno(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    eixos(c, t, P1, C["s08"] - 0.3, tl=C["s08"] - 0.3, extra=EXTRA)
    curva_a(c, t, C["s08"] - 0.3, P1, sen, -PI, 3 * PI, d=0.01, cor=OPO, alfa=0.25 * ep(t, C["s08"] - 0.3, 0.6), largura=7)
    pontos = [(0, 1, a8), (PI / 2, 0, b8), (PI, -1, c8), (3 * PI / 2, 0, d8), (2 * PI, 1, e8)]
    for xv, yv, tt in pontos:
        E.ponto(c, t, tt, P1, xv, yv, None, cor=ADJ, r=15)
    curva_a(c, t, a9, P1, cos, -PI, 3 * PI, d=2.2, cor=ADJ, largura=9)
    periodo(c, t, b9, P1, 0, 2 * PI, 1.42, "2π", f=cos, cor_f=ADJ)
    barra_y(c, t, c9, P1, -1, 1)

    def topo8():
        E.frase(c, t, C["s08"] + 0.1, [("cosseno", "g", 60, ADJ)] + ps("nos pontos fáceis", "i", 56, TINTA2), W / 2, 120, "center", 0.08)
        tabela(c, t, [a8, b8, c8, d8, e8], [("0°", "1"), ("90°", "0"), ("180°", "−1"), ("270°", "0"), ("360°", "1")], 360, 225, 300, cor=ADJ)
    E.saida(c, t, a9 - 0.2, topo8)
    if a9 - 0.2 <= t:
        E.frase(c, t, a9, ps("a mesma onda,", "i", 60) + [("começa no alto", "g", 66, ADJ)], W / 2, 150, "center", 0.1)
        E.frase(c, t, b9, ps("período", "i", 54) + [("2π,", "g", 58, COR)] + ps("imagem de", "i", 54) + [("−1 a 1", "g", 58, SAI)], W / 2, 245, "center", 0.1)


PT = E.Plano(GX, GY, GW, GH, -PI, 3 * PI, -3.4, 3.4)


def b_tangente(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    eixos(c, t, PT, C["s10"] - 0.3, tl=C["s10"] - 0.3, extra=EXTRA, ys=(2, -2))
    # 90°: o cosseno é zero
    if t >= b0:
        q = ep(t, b0, 0.5) * (1 - ep(t, b1 - 0.2, 0.3))
        X = PT.x(PI / 2)
        M.line(c, X, GY, X, GY + GH, ERRADO, q, 5, dash=E.TRACO)
        E.foco(c, t, b0 + 0.3, 0.4, lambda a: E.formula(c, "cos 90° = 0", X + 20, GY + 40, 46, "g", ERRADO, a * (1 - ep(t, b1 - 0.2, 0.3))))
    # o galho do meio, depois todos
    curva_a(c, t, c0, PT, tg, -PI / 2 + 0.001, PI / 2 - 0.001, d=1.4, cor=TGC, largura=8)
    for k in (-1, 1, 2):
        curva_a(c, t, a1 + 0.3 * (k + 1), PT, tg, k * PI - PI / 2 + 0.001, k * PI + PI / 2 - 0.001, d=1.0, cor=TGC, largura=8)
    for xv in (-PI / 2, PI / 2, 3 * PI / 2, 5 * PI / 2):
        if t >= b1:
            M.line(c, PT.x(xv), GY, PT.x(xv), GY + GH, TINTA2, 0.85, 4, dash=E.TRACO, progress=ep(t, b1, 0.6))
    barra_y(c, t, c1, PT, -3.3, 3.3, setas=True)
    periodo(c, t, d1, PT, PI / 2, 3 * PI / 2, 3.15, "π  (180°)", f=None)

    def topo10():
        E.frase(c, t, C["s10"] + 0.1, [("tangente:", "g", 60, TGC)] + ps("diferente", "i", 56), XE, 150, "left", 0.1)
        E.foco(c, t, a0, 0.5, lambda a: cf(c, [("tg x = ", TGC), ("sen x", OPO), (" ÷ ", TINTA), ("cos x", ADJ)], XE, 245, 58, a))
        E.frase(c, t, b0 + 0.6, ps("÷ 0 não existe", "i", 56, ERRADO), 1060, 150, "left", 0.08)
        E.frase(c, t, c0, ps("perto dali,", "i", 56) + [("dispara", "g", 60, TGC)], 1060, 245, "left", 0.1)
    E.saida(c, t, a1 - 0.2, topo10)
    if t < a1 - 0.2:
        return

    def topo11():
        E.frase(c, t, a1, [("vários galhos", "g", 64, TGC)], XE, 150, "left", 0.1)
        E.frase(c, t, b1, ps("linhas", "i", 56) + [("tracejadas:", "g", 60)] + ps("a curva nunca toca", "i", 56), XE, 245, "left", 0.1)
        E.frase(c, t, c1, ps("imagem:", "i", 58) + [("todos os reais", "g", 64, SAI)], 1150, 150, "left", 0.1)
    E.saida(c, t, d1 - 0.2, topo11)
    if t >= d1 - 0.2:
        E.frase(c, t, d1, ps("repete a cada meia volta:", "i", 58) + [("período π", "g", 64, COR)], XE, 150, "left", 0.1)
        E.frase(c, t, d1 + 3.0, ps("do outro lado do ciclo, sen e cos trocam de sinal juntos:", "i", 46, TINTA2), XE, 240, "left", 0.06)
        E.foco(c, t, d1 + 5.0, 0.4, lambda a: E.formula(c, "(−) ÷ (−) = +", 1500, 245, 54, "g", TINTA, a))


P3 = E.Plano(GX, GY, GW, GH, -PI, 3 * PI, -3.6, 3.6)


def b_vezes3(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    eixos(c, t, P3, C["s12"] - 0.3, tl=C["s12"] - 0.3, extra=EXTRA, ys=(3, -3))
    curva_a(c, t, C["s12"], P3, sen, -PI, 3 * PI, d=1.2, cor=OPO, alfa=1 - 0.7 * ep(t, c2, 0.5), largura=8)
    if t >= c2:  # a onda estica: cada altura vezes k, de 1 até 3
        k = 1 + 2 * ease_io(prog(t, c2 + 0.3, 1.6))
        E.curva(c, t, c2 - 5, P3, lambda x: k * sen(x), -PI, 3 * PI, d=0.01, cor=COR, largura=10)
        for xv, s in ((PI / 2, 1), (3 * PI / 2, -1), (-PI / 2, -1), (5 * PI / 2, 1)):
            q = ep(t, c2 + 0.3, 0.4) * (1 - ep(t, C["s13"] - 0.3, 0.4))
            if q > 0:
                M.arrow(c, P3.x(xv), P3.y(s), P3.x(xv), P3.y(3 * s), TINTA2, q, 5, 20, ease_io(prog(t, c2 + 0.3, 1.6)))
        lab = ((PI / 2, 3, "1 → 3", c2 + 1.6), (3 * PI / 2, -3, "−1 → −3", c2 + 3.0), (PI, 0, "0 → 0", c2 + 4.4))
        for xv, yv, s, tt in lab:
            dy = -40 if yv > 0 else 16 if yv < 0 else -30
            dx = 90 if yv == 0 else 190 if yv < 0 else 0
            E.foco(c, t, tt, 0.4, lambda a, xv=xv, yv=yv, s=s, dy=dy, dx=dx: cf(c, [(s, COR)], P3.x(xv) + dx, P3.y(yv) + dy, 44,
                                                                        a * (1 - ep(t, C["s13"] - 0.3, 0.4)), "center"))
    barra_y(c, t, b3, P3, -3, 3)
    periodo(c, t, c3, P3, 0, 2 * PI, 3.45, "2π", f=None)

    def topo12():
        E.frase(c, t, a2, ps("multiplicado por", "i", 58) + [("3", "g", 66, COR)], XE, 150, "left", 0.1)
        E.foco(c, t, b2, 0.5, lambda a: E.formula(c, "y = 3 · sen x", XE, 250, 66, "g", COR, a))
        E.frase(c, t, c2, ps("cada altura", "i", 58) + [("triplica", "g", 64, COR)], 1150, 200, "left", 0.1)
    E.saida(c, t, C["s13"] - 0.2, topo12)
    if t >= C["s13"] - 0.2:
        E.frase(c, t, a3, [("mais alta,", "g", 62, COR)] + ps("mas não mais larga", "i", 58), XE, 150, "left", 0.1)
        E.frase(c, t, b3, ps("imagem:", "i", 56) + [("de −3 a 3", "g", 62, SAI)], XE, 250, "left", 0.1)
        E.frase(c, t, c3, ps("período:", "i", 56) + [("continua 2π", "g", 62, COR)], 1150, 250, "left", 0.1)


# ---------------- erro ----------------
PE = E.Plano(1080, 330, 690, 460, -0.3, 2 * PI + 0.4, -3.6, 3.6)


def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    x = XE
    eixos(c, t, PE, C["s14"] - 0.2, tl=C["s14"] - 0.2, marcas=[(PI, "π", ""), (2 * PI, "2π", "")], graus=False, ys=(3, -3), size=40)
    curva_a(c, t, C["s14"], PE, lambda v: 3 * sen(v), -0.3, 2 * PI + 0.4, d=1.0, cor=COR, largura=8)
    periodo(c, t, e4, PE, 0, 2 * PI, 3.4, "2π", cor=CERTO)
    E.frase(c, t, a4, ps("o erro: achar que o", "i", 60) + [("3", "g", 66, ERRADO)] + ps("mexe no período", "i", 60), x, 190, "left", 0.1)
    E.foco(c, t, b4, 0.5, lambda a: E.formula(c, "3 · 2π = 6π", x, 380, 96, "g", ERRADO, a))
    if t >= b4 + 1.4:
        E.risco(c, x - 10, 400, x + _w("3 · 2π = 6π", 96) + 10, 320, t, b4 + 1.4, ERRADO, 10)
    E.frase(c, t, c4, ps("o 3 multiplica", "i", 58) + [("a saída", "g", 64, SAI)] + ps("(a altura)", "i", 54, TINTA2), x, 560, "left", 0.1)
    E.frase(c, t, d4, [("a entrada", "g", 64, ENT)] + ps("(o ângulo)", "i", 54, TINTA2) + ps("não muda", "i", 58), x, 690, "left", 0.1)
    resp(c, t, e4, "período = 2π", x + 300, 880, 70, cor=CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def quinze():
        E.frase(c, t, C["s15"] + 0.1, ps("o atalho", "i", 66, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a5, ps("o número positivo da frente dá", "i", 60, CLARO) + [("a imagem", "g", 66, BR)], W / 2, 310, "center", 0.1)
        E.foco(c, t, a5 + 1.6, 0.5, lambda a: cf(c, [("y = k · sen x", BR), ("   →   ", CLARO), ("[−k, k]", AMBAR)], W / 2, 470, 84, a, "center"))
        E.frase(c, t, b5, ps("do", "i", 56, CLARO) + [("oposto", "g", 60, BR)] + ps("dele até", "i", 56, CLARO) + [("ele", "g", 60, BR)], W / 2, 590, "center", 0.1)
        E.foco(c, t, c5, 0.5, lambda a: E.formula(c, "y = 5 · cos x", W / 2 - 330, 800, 92, "g", BR, a, "center"))
        E.foco(c, t, d5, 0.5, lambda a: E.formula(c, "→   de −5 a 5", W / 2 + 330, 800, 92, "g", AMBAR, a, "center"))
    E.saida(c, t, C["s16"] - 0.1, quinze)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, a6, ps("sen e cos nunca passam de", "i", 56, CLARO) + [("1", "g", 62, BR)] + ps("nem ficam abaixo de", "i", 56, CLARO) + [("−1", "g", 62, BR)],
            W / 2, 190, "center", 0.08)
    E.foco(c, t, a6 + 3.5, 0.5, lambda a: cf(c, [("−1 · 5 = −5", AMBAR), ("        ", BR), ("1 · 5 = 5", AMBAR)], W / 2, 330, 80, a, "center"))
    E.frase(c, t, a6 + 4.6, ps("as duas pontas, vezes o número", "i", 50, CLARO), W / 2, 420, "center", 0.07)
    E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 560, 580, 40, False, a))
    E.frase(c, t, b6, ps("não serve para a", "i", 58, CLARO) + [("tangente:", "g", 62, BR)] + ps("não tem teto", "i", 58, CLARO), 630, 600, "left", 0.1)
    E.frase(c, t, c6, ps("número somado ou dentro do parêntese:", "i", 54, CLARO), W / 2, 760, "center", 0.08)
    E.foco(c, t, c6 + 1.2, 0.5, lambda a: cf(c, [("y = 1 + 2 · cos x", BR), ("        ", BR), ("y = cos(2x)", BR)], W / 2, 880, 70, a, "center"))
    E.frase(c, t, c6 + 2.4, ps("a onda muda de outro jeito", "i", 50, CLARO), W / 2, 980, "center", 0.07)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.foco(c, t, a7, 0.5, lambda a: E.formula(c, "y = 2 · cos x", XE, 380, 110, "g", TINTA, a))
    for i, (tt, partes) in enumerate(((b7, ps("qual é o", "i", 64) + [("período?", "g", 70, COR)]),
                                      (c7, ps("qual é a", "i", 64) + [("imagem?", "g", 70, SAI)]))):
        y = 560 + i * 140
        E.foco(c, t, tt, 0.5, lambda a, y=y, i=i: centro(c, str(i + 1), XE + 30, y, 60, "g", COR, a))
        E.frase(c, t, tt, partes, XE + 100, y, "left", 0.1)
    E.foco(c, t, d7, 0.5, lambda a: centro(c, "3", XE + 30, 840, 60, "g", COR, a))
    E.frase(c, t, d7, ps("y quando", "i", 64) + [("x = π", "g", 70, ENT)] + ps("(180°)?", "i", 60, TINTA2), XE + 100, 840, "left", 0.1)
    E.relogio(c, t, C["s18.a"], 1520, 440, 170)


# ---------------- resposta ----------------
PR = E.Plano(1000, 300, 740, 480, -0.3, 2 * PI + 0.4, -2.7, 2.7)


def b_resposta(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    eixos(c, t, PR, C["s19"], tl=C["s19"] + 0.2, marcas=[(PI / 2, "f{π}{2}", ""), (PI, "π", "180°"), (3 * PI / 2, "f{3π}{2}", ""), (2 * PI, "2π", "")],
          ys=(2, -2), size=46)
    curva_a(c, t, C["s19"] + 0.4, PR, lambda v: 2 * cos(v), -0.3, 2 * PI + 0.4, d=1.2, cor=ADJ, largura=8)
    periodo(c, t, a9, PR, 0, 2 * PI, 2.45, "2π", f=None)
    barra_y(c, t, b9, PR, -2, 2)
    if t >= c9:
        X = PR.x(PI)
        M.line(c, X, PR.oy, X, PR.y(-2), TINTA2, 0.7 * ep(t, c9, 0.4), 4, dash=E.TRACO, progress=ep(t, c9, 0.6))
    E.ponto(c, t, e9, PR, PI, -2, "(π, −2)", cor=COR, lado=(1, 0.2), size=46)
    E.frase(c, t, C["s19"] + 0.1, ps("vamos lá", "i", 64, COR), XE, 170, "left", 0.1)
    E.frase(c, t, a9, ps("o 2 só mexe na altura:", "i", 54, TINTA2), XE, 280, "left", 0.07)
    resp(c, t, a9 + 0.5, [("período = 2π", BR)], XE + 260, 380, 62)
    resp(c, t, b9, [("imagem: de −2 a 2", BR)], XE + 330, 530, 62, cor=TINTA)
    E.foco(c, t, c9, 0.5, lambda a: cf(c, [("cos π", ADJ), (" = −1", TINTA)], XE, 710, 72, a))
    E.foco(c, t, d9, 0.5, lambda a: cf(c, [("y = 2 · (−1) = −2", TINTA)], XE, 840, 72, a))
    E.frase(c, t, e9, [("o ponto mais baixo", "g", 62, COR)], XE, 960, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", ps("sen e cos:", "i", 60) + [("período 2π,", "g", 64, COR), ("imagem [−1, 1]", "g", 64)]),
                 ("s20.b", ps("tangente:", "i", 60) + [("galhos,", "g", 64, TGC), ("período π", "g", 64, COR)]),
                 ("s20.c", ps("o número na frente:", "i", 60) + [("só a altura", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula, você", "i", 70), XE, 200, passo=0.1)
    E.frase(c, t, a1, [("mexe na onda", "g", 84, COR)] + ps("de 3 jeitos", "i", 70), XE, 320, passo=0.1)
    E.frase(c, t, b1, [("sobe,", "g", 66, COR), ("estica", "g", 66, COR)] + ps("e", "i", 60) + [("aperta", "g", 66, COR)], XE, 450, passo=0.12)
    E.foco(c, t, c1, 0.5, lambda a: E.formula(c, "y = 1 + 2 · cos(2x)", XE, 590, 80, "g", COR, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, seno=b_seno, cosseno=b_cosseno, tangente=b_tangente, vezes3=b_vezes3,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
