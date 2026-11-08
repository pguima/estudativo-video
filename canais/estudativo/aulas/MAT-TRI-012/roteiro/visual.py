"""Visual — Estudativo · MAT-TRI-012: fenômenos periódicos (maré h(t) = 5 + 2 cos(πt/6): máx 7 m, mín 3 m, período 12 h;
roda-gigante h(t) = 12 + 10 cos(πt/3): 22 m, 2 m, 6 min).
Segue MAT-TRI-011 e MAT-TRI-014: eixo do tempo t (a entrada) em índigo e eixo da altura h em preto; a onda do cosseno em petróleo;
as letras com a cor e a marca da MAT-TRI-014:
    nível médio (o número somado, á) = âmbar, com a LINHA DO MEIO tracejada
    o número da frente (bê) = índigo, com a seta da amplitude
    o de dentro do parêntese e o período (cê) = magenta, com o colchete do período
Água do porto em petróleo claro, com uma régua de maré em metros; a roda-gigante em tinta, com a cadeira na cor da matéria.
Resposta na pílula; erro em vermelho, certo em verde; atalho no palco escuro.
A figura não mente: a régua e o gráfico usam as alturas da fórmula (3, 5 e 7 m; 2, 12 e 22 m), a onda passa pelos pontos ditos
e a roda tem o centro a 12 m e raio de 10 m na mesma escala da régua.
Peças locais: cf() (fórmula com cores por parte), mare() (formula da maré colorida), porto() (água, régua, barco), eixos(),
curva_a(), periodo(), meio(), roda(), resp(). Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-012_fenomenos_periodicos_mares_e_ondas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "periodo", "quando", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
ADJ, ADJ_ESC = "#0E9AA7", "#3CC7D3"
LA, LB, LC = AMBAR, E.COR, "#C0187C"
LA_ESC, LB_ESC, LC_ESC = "#FFB020", CLARO, "#FF6FB5"
ENT, SAI = E.COR, TINTA
AGUA = "#7FD3DA"
PI = math.pi
cos = math.cos
h_mare = lambda t: 5 + 2 * cos(PI * t / 6)
h_roda = lambda t: 12 + 10 * cos(PI * t / 3)
assert h_mare(0) == 7 and abs(h_mare(6) - 3) < 1e-12 and abs(h_mare(12) - 7) < 1e-12 and abs(h_mare(18) - 3) < 1e-12
assert h_roda(0) == 22 and abs(h_roda(3) - 2) < 1e-12 and abs(h_roda(6) - 22) < 1e-12 and 22 - 2 == 20 and 2 * 3 == 6 and 2 * 6 == 12
assert abs(2 * PI * 5 / 5 - 2 * PI) < 1e-12 and 2 * 12 == 24


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
    """fórmula numa linha com partes coloridas; devolve o x do centro de cada parte"""
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    centros = []
    for (s, cor), wi in zip(partes, ws):
        if a > 0 and c is not None:
            E.formula(c, s, xx, y, size, est, cor, a)
        centros.append(xx + wi / 2)
        xx += wi
    return centros


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=66, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = sum(_w(s, size) for s, _ in partes) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def mare(tinta=TINTA, esc=False, a_="5", b_="2", n="6"):
    la, lb, lc = (LA_ESC, LB_ESC, LC_ESC) if esc else (LA, LB, LC)
    return [("h(t) = ", tinta), (a_, la), (" + ", tinta), (b_, lb), (" · cos(", tinta), (f"f{{πt}}{{{n}}}", lc), (")", tinta)]


# ---------------- o porto ----------------
PX0, PX1, PBASE, PK = 1200, 1800, 960, 70   # água de PX0 a PX1, fundo em PBASE, 70 px por metro


def porto(c, t, t0, nivel, marcas=(), a=1.0, barco=True):
    """água no nível (metros), régua de maré de 0 a 8 m à esquerda da água, cais e um barco que boia"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.6) * a
    topo = PBASE - nivel * PK
    # a água, com ondinhas
    path = skia.Path(); path.moveTo(PX0, PBASE)
    for i in range(61):
        X = PX0 + (PX1 - PX0) * i / 60
        path.lineTo(X, topo + 6 * math.sin(i * 0.7 + t * 3))
    path.lineTo(PX1, PBASE); path.close()
    c.drawPath(path, M.paint(AGUA, 0.55 * q))
    M.line(c, PX0, PBASE, PX1, PBASE, TINTA, q, 5)
    # o cais: pilares e o deck acima da maré alta
    for X in (PX0 + 40, PX0 + 170):
        M.line(c, X, PBASE, X, PBASE - 8.6 * PK, TINTA2, q, 12, cap_round=False)
    M.rrect(c, PX0 - 10, PBASE - 8.8 * PK, 240, 22, 6, TINTA, q)
    # a régua de maré
    xr = PX0 - 40
    M.line(c, xr, PBASE, xr, PBASE - 8 * PK, TINTA, q, 5)
    for m in range(0, 9):
        Y = PBASE - m * PK
        M.line(c, xr - (22 if m % 2 == 0 else 12), Y, xr, Y, TINTA, q, 4)
    for m in (0, 2, 4, 6, 8):
        E.escreve(c, str(m), xr - 34 - E.larg(str(m), "b", 40), PBASE - m * PK + 14, 40, "b", TINTA, q)
    E.escreve(c, "m", xr - 30, PBASE - 8 * PK - 30, 40, "i", TINTA2, q)
    if barco:
        bx = PX0 + 400
        by = topo + 6 * math.sin(10 * 0.7 + t * 3)
        hull = skia.Path(); hull.moveTo(bx - 110, by - 26); hull.lineTo(bx + 120, by - 26); hull.lineTo(bx + 80, by + 22); hull.lineTo(bx - 80, by + 22); hull.close()
        c.drawPath(hull, M.paint(E.COR, q))
        M.line(c, bx - 10, by - 26, bx - 10, by - 150, TINTA, q, 6)
        vela = skia.Path(); vela.moveTo(bx - 4, by - 145); vela.lineTo(bx + 80, by - 40); vela.lineTo(bx - 4, by - 40); vela.close()
        c.drawPath(vela, M.paint(BR, q)); c.drawPath(vela, M.paint(TINTA, q, stroke=3))


def nivel_marca(c, t, t0, m, rot, cor, a=1.0, tracejada=False):
    """traço horizontal na altura m da régua, atravessando a água, com o rótulo à direita"""
    if t < t0 or a <= 0:
        return
    Y = PBASE - m * PK
    q = ep(t, t0, 0.5) * a
    M.line(c, PX0 - 60, Y, PX1, Y, cor, q, 5, dash=E.TRACO if tracejada else None, progress=ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.3, 0.4, lambda b: E.formula(c, rot, PX1 + 16, Y + 16, 46, "g", cor, b * a))


# ---------------- gráfico ----------------
def eixos(c, t, P, tx, marcas, ys, nome_x="t (h)", nome_y="h (m)", tl=None, escuro=False, size=46):
    if t < tx:
        return
    x, y, w, h = P.caixa
    tinta = BR if escuro else SAI
    ent = CLARO if escuro else ENT
    q = ep(t, tx, 0.8) * (0.25 if escuro else 1)
    for v in marcas:
        M.line(c, P.x(v), y, P.x(v), y + h, CLARO if escuro else FIO, q, 2)
    for v in ys:
        M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ent, 1.0, 6, 24, ep(t, tx, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, tinta, 1.0, 6, 24, ep(t, tx, 0.7))
    E.foco(c, t, tx + 0.5, 0.4, lambda b: (E.escreve(c, nome_x, x + w - E.larg(nome_x, "i", 46) + 30, P.oy - 24, 46, "i", ent, b),
                                           E.escreve(c, nome_y, P.ox - 24 - E.larg(nome_y, "i", 46), y - 10, 46, "i", tinta, b)))
    tl = tx + 0.3 if tl is None else tl
    for v in marcas:
        X = P.x(v)
        E.foco(c, t, tl, 0.4, lambda b, X=X, v=v: (M.line(c, X, P.oy - 10, X, P.oy + 10, ent, b, 4),
                                                   v != 0 and centro(c, E._num(v), X, P.oy + 14 + size, size, "b", ent, b)), sobe=4)
    for v in ys:
        Y = P.y(v)
        s = E._num(v)
        E.foco(c, t, tl, 0.4, lambda b, Y=Y, s=s: (M.line(c, P.ox - 10, Y, P.ox + 10, Y, tinta, b, 4),
                                                   E.escreve(c, s, P.ox - 22 - E.larg(s, "b", size), Y + size * 0.36, size, "b", tinta, b)))


def curva_a(c, t, t0, P, f, a_, b_, d=1.2, cor=None, alfa=1.0, largura=8):
    if alfa <= 0 or t < t0:
        return
    if alfa < 1:
        pt = skia.Paint(); pt.setAlphaf(alfa); c.saveLayer(None, pt)
    E.curva(c, t, t0, P, f, a_, b_, d=d, cor=cor, largura=largura)
    if alfa < 1:
        c.restore()


def periodo(c, t, t0, P, x0, x1, yv, rot, cor=LC, size=50, d=0.6):
    if t < t0:
        return
    Y = P.y(yv)
    E.chave(c, P.x(x0), P.x(x1), Y, cor, ease_out(prog(t, t0, d)), -26, 6)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda b: E.formula(c, rot, (P.x(x0) + P.x(x1)) / 2, Y - 46, size, "g", cor, b, "center"))


def meio(c, t, t0, P, yv, rot=None, cor=LA, size=44):
    if t < t0:
        return
    x, y, w, h = P.caixa
    M.line(c, x, P.y(yv), x + w, P.y(yv), cor, 1.0, 5, dash=E.TRACO, progress=ep(t, t0, 0.8))
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.formula(c, rot, x + w + 24, P.y(yv) + 16, size, "g", cor, b))


def ponto(c, t, t0, P, xv, yv, rot=None, cor=TINTA, dx=28, dy=-36, size=44, align="left"):
    E.ponto(c, t, t0, P, xv, yv, None, cor=cor, r=14)
    if rot:
        X, Y = P(xv, yv)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, X + dx, Y + dy + 16, size, "g", cor, a, align))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        nv = 5 + 2 * math.cos(2 * PI * (t - a1) / 6.0)  # a maré sobe e desce na tela
        porto(c, t, a1, nv)
        E.frase(c, t, a1 + 0.2, ps("a maré", "i", 80) + [("sobe e desce", "g", 86, ADJ)], XE, 300, passo=0.12)
        E.frase(c, t, a1 + 1.6, ps("sempre no mesmo", "i", 70) + [("ritmo", "g", 76)], XE, 410, passo=0.12)
        E.foco(c, t, b1, 0.5, lambda a: (M.arrow(c, XE + 20, 600, XE + 20, 520, CERTO, a, 7, 26, 1.0),
                                         E.escreve(c, "quando fica alta?", XE + 70, 580, 66, "g", TINTA, a)))
        E.foco(c, t, c1, 0.5, lambda a: (M.arrow(c, XE + 20, 680, XE + 20, 760, ERRADO, a, 7, 26, 1.0),
                                         E.escreve(c, "quando fica baixa?", XE + 70, 740, 66, "g", TINTA, a)))
        E.frase(c, t, c1 + 2.0, ps("uma fórmula com", "i", 60) + [("cosseno", "g", 66, ADJ)] + ps("responde", "i", 60), XE, 900, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 600, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula, no dia a dia:", "i", 70), XE, 280, passo=0.12)
        E.frase(c, t, ta + 2.0, [("máximo,", "g", 90, LB)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 2.6, [("mínimo", "g", 90, LB)], XE, 560, passo=0.14)
        E.frase(c, t, ta + 3.2, ps("e", "i", 80) + [("período", "g", 90, LC)], XE, 690, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 585, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 670, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa da", "i", 84), XE, 450, passo=0.14)
    E.frase(c, t, C["s03"] + 1.0, [("aula anterior", "g", 96, COR)], XE, 590, passo=0.14)
    x, w = 900, 920
    itens = (("s03.a", lambda a, y: cf(c, [("máximo = ", TINTA), ("a", LA), (" + ", TINTA), ("b", LB)], x + 44, y, 72, a)),
             ("s03.b", lambda a, y: cf(c, [("mínimo = ", TINTA), ("a", LA), (" − ", TINTA), ("b", LB)], x + 44, y, 72, a)),
             ("s03.c", lambda a, y: (E.escreve(c, "volta fecha quando", x + 44, y - 64, 48, "i", TINTA2, a),
                                     cf(c, [("o de dentro = 2π", LC)], x + 44, y + 10, 64, a))))
    for i, (k, fn) in enumerate(itens):
        y = 200 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y + 125))
    alvo = [C[k] for k, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(370, 610, q1), 850, q2), ep(t, C["s03.a"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), XE, 1000, "left", 0.12)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.2, ps("num porto", "i", 60) + [("imaginado", "g", 64)] + ps("para esta aula", "i", 60), W / 2, 200, "center", 0.1)
    E.foco(c, t, a4, 0.6, lambda a: cf(c, mare(), W / 2, 460, 130, a, "center"))
    xs = cf(None, mare(), W / 2, 460, 130, 0, "center")
    E.foco(c, t, b4, 0.5, lambda a: (M.arrow(c, xs[5] + 20, 700, xs[5] + 20, 590, ENT, a, 5, 20, 1.0),
                                     cf(c, [("t", ENT), (" = tempo, em horas, desde a meia-noite", TINTA)], 1780, 780, 54, a, "right")))
    E.foco(c, t, c4, 0.5, lambda a: (M.arrow(c, xs[0] - 40, 620, xs[0] - 40, 530, SAI, a, 5, 20, 1.0),
                                     cf(c, [("h(t)", SAI), (" = altura da água, em metros", TINTA)], XE, 700, 54, a)))


# ---------------- máximo e mínimo ----------------
def b_altura(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    E.foco(c, t, C["s05"] - 0.2, 0.5, lambda a: cf(c, mare(), XE, 190, 76, a))
    nv = 5 + 2 * math.cos(2 * PI * (t - C["s05"]) / 6.0)
    porto(c, t, C["s05"] - 0.2, nv, barco=True)
    nivel_marca(c, t, a5, 7, "7 m", LB)
    nivel_marca(c, t, b5, 3, "3 m", LB)
    nivel_marca(c, t, c5, 5, "5 m", LA, tracejada=True)
    E.frase(c, t, C["s05"] + 0.2, ps("o cosseno vai de", "i", 54, TINTA2) + [("−1 a 1", "g", 58)], XE, 320, "left", 0.08)
    E.foco(c, t, a5, 0.5, lambda a: (E.escreve(c, "maré alta", XE, 470, 56, "i", TINTA, a),
                                     cf(c, [("5", LA), (" + ", TINTA), ("2", LB), (" = 7 m", TINTA)], XE + 300, 470, 72, a)))
    E.foco(c, t, b5, 0.5, lambda a: (E.escreve(c, "maré baixa", XE, 630, 56, "i", TINTA, a),
                                     cf(c, [("5", LA), (" − ", TINTA), ("2", LB), (" = 3 m", TINTA)], XE + 300, 630, 72, a)))
    E.frase(c, t, c5, [("5", "g", 66, LA)] + ps("= nível médio,", "i", 56) + [("o meio da onda", "g", 60, LA)], XE, 820, "left", 0.1)


# ---------------- período ----------------
def b_periodo(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    E.foco(c, t, C["s06"] - 0.2, 0.5, lambda a: cf(c, mare(), XE, 190, 76, a))
    E.frase(c, t, C["s06"] + 0.3, ps("de quantas em quantas", "i", 60) + [("horas?", "g", 66, LC)], 1150, 190, "left", 0.1)
    E.frase(c, t, a6, ps("quando", "i", 58) + [("o de dentro", "g", 62, LC)] + ps("chega a", "i", 58) + [("2π", "g", 62)], XE, 340, "left", 0.1)
    x0 = 620
    cf_em(c, t, b6, [("f{πt}{6}", LC), (" = 2π", TINTA)], x0, 520, 96)
    E.foco(c, t, c6, 0.4, lambda a: E.formula(c, "÷ π", x0 - 220, 680, 52, "b", TINTA2, a))
    cf_em(c, t, c6 + 0.3, [("f{t}{6} = 2", TINTA)], x0, 690, 96)
    E.foco(c, t, d6, 0.4, lambda a: E.formula(c, "× 6", x0 - 220, 850, 52, "b", TINTA2, a))
    cf_em(c, t, d6 + 0.3, [("t = 12", TINTA)], x0, 850, 96)
    resp(c, t, e6, [("período = 12 h", BR)], 1400, 690, 76, cor=LC)


# ---------------- quando ----------------
PQ = E.Plano(300, 330, 1400, 560, 0, 25.5, 0, 8.2)
TM = (0, 6, 12, 18, 24)


def b_quando(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    eixos(c, t, PQ, C["s07"] - 0.2, TM, (3, 5, 7))
    meio(c, t, e8 + 0.2, PQ, 5, "5 m")
    curva_a(c, t, e8, PQ, h_mare, 0, 24, d=2.0, cor=ADJ, largura=9)
    periodo(c, t, e8 + 1.4, PQ, 0, 12, 7.75, "12 h")
    ponto(c, t, b7, PQ, 0, 7, "meia-noite: 7 m", cor=LB, dx=30, dy=-34)
    ponto(c, t, c8, PQ, 6, 3, "6 h: 3 m", cor=LB, dx=0, dy=72, align="center")
    ponto(c, t, d8, PQ, 12, 7, "meio-dia: 7 m", cor=LB, dx=30, dy=-34)
    ponto(c, t, e8 + 0.8, PQ, 18, 3, None, cor=LB)
    ponto(c, t, e8 + 1.0, PQ, 24, 7, None, cor=LB)

    def sete():
        E.frase(c, t, C["s07"] + 0.2, ps("a que horas a maré é", "i", 56) + [("alta?", "g", 62, LB)], XE, 140, "left", 0.08)
        E.foco(c, t, a7, 0.5, lambda a: cf(c, [("cos = 1", ADJ), ("  quando o ângulo é ", TINTA), ("0", LC)], XE, 240, 56, a))
    E.saida(c, t, a8 - 0.2, sete)
    if t < a8 - 0.2:
        return

    def oito():
        E.foco(c, t, a8, 0.5, lambda a: cf(c, [("t = 6:  ", ENT), ("f{π · 6}{6} = π", LC)], XE, 170, 60, a))
        E.foco(c, t, b8, 0.5, lambda a: cf(c, [("cos π = −1", ADJ)], XE + 620, 170, 60, a))
    E.saida(c, t, e8 - 0.2, oito)
    if t >= e8 - 0.2:
        E.frase(c, t, e8, ps("a onda oscila entre", "i", 56) + [("3 e 7,", "g", 62, LB)] + ps("um pico a cada", "i", 56) + [("12 h", "g", 62, LC)],
                XE, 170, "left", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    eixos(c, t, PQ, C["s09"] - 0.3, TM, (3, 5, 7), tl=C["s09"] - 0.3)
    curva_a(c, t, C["s09"] - 0.3, PQ, h_mare, 0, 24, d=0.01, cor=ADJ, alfa=0.45, largura=7)
    if t >= b9:
        E.curva(c, t, b9, PQ, h_mare, 0, 6, d=0.8, cor=ERRADO, largura=13)
    if t >= d9:
        E.curva(c, t, d9, PQ, h_mare, 6, 12, d=0.8, cor=CERTO, largura=13)
    periodo(c, t, b9 + 0.4, PQ, 0, 6, 7.55, None, cor=ERRADO)
    periodo(c, t, e9, PQ, 0, 12, 8.05, None, cor=CERTO)
    E.frase(c, t, a9, ps("o erro: período =", "i", 58) + [("6,", "g", 64, ERRADO)] + ps("o número da fórmula", "i", 58), XE, 150, "left", 0.1)
    if t >= a9 + 2.5:
        x1 = XE + E._arranjo(ps("o erro: período =", "i", 58), XE, "left")[0] + 14
        E.risco(c, x1, 164, x1 + 70, 112, t, a9 + 2.5, ERRADO, 9)
    E.frase(c, t, b9, ps("em 6 h, o de dentro só chega a", "i", 52, TINTA2) + [("π", "g", 58, LC)], XE, 250, "left", 0.07)
    E.frase(c, t, c9, [("alta → baixa", "g", 54, ERRADO)], PQ.x(3), PQ.y(1.6), "center", 0.1)
    E.frase(c, t, d9, [("+ 6 h", "g", 54, CERTO)], PQ.x(9), PQ.y(1.6), "center", 0.1)
    resp(c, t, e9, [("período = 12 h", BR)], 1450, 220, 64, cor=CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")

    def dez():
        E.frase(c, t, C["s10"] + 0.1, ps("o atalho", "i", 66, CLARO), W / 2, 180, "center", 0.1)
        E.foco(c, t, a0, 0.5, lambda a: cf(c, [("dentro = ", CLARO), ("f{πt}{n}", LC_ESC)], W / 2 - 340, 400, 100, a, "center"))
        E.foco(c, t, b0, 0.5, lambda a: cf(c, [("→  período = ", BR), ("2n", AMBAR)], W / 2 + 360, 400, 100, a, "center"))
        E.foco(c, t, c0, 0.5, lambda a: cf(c, [("f{πt}{6}", LC_ESC), ("  →  ", CLARO), ("12", AMBAR)], W / 2, 650, 96, a, "center"))
        E.foco(c, t, d0, 0.5, lambda a: cf(c, [("f{πt}{12}", LC_ESC), ("  →  ", CLARO), ("24", AMBAR)], W / 2, 880, 96, a, "center"))
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, C["s11"] + 0.2, ps("funciona porque o", "i", 56, CLARO) + [("π", "g", 60, BR)] + ps("se corta dos dois lados", "i", 56, CLARO),
            W / 2, 170, "center", 0.08)
    E.foco(c, t, a1, 0.5, lambda a: cf(c, [("f{πt}{n}", LC_ESC), (" = 2π  →  ", BR), ("f{t}{n} = 2", BR), ("  →  t = 2n", AMBAR)], W / 2, 340, 80, a, "center"))
    E.foco(c, t, b1, 0.5, lambda a: E.selo(c, 330, 520, 38, False, a))
    E.frase(c, t, b1, ps("não serve com número", "i", 56, CLARO) + [("multiplicando o π", "g", 60, BR)], 390, 540, "left", 0.08)
    E.foco(c, t, c1, 0.5, lambda a: cf(c, [("f{2πt}{5}", LC_ESC)], 330, 750, 86, a))
    E.foco(c, t, d1, 0.5, lambda a: cf(c, [(" = 2π  →  ", BR), ("f{2t}{5} = 2", BR), ("  →  2t = 10", BR)], 330 + _w("f{2πt}{5}", 86), 750, 86, a))
    resp(c, t, e1, [("período = 5", BR)], W / 2, 940, 70, cor=LC)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.2, ps("hora de testar:", "i", 72, COR) + ps("roda-gigante", "i", 72), XE, 170, passo=0.12)
    E.foco(c, t, a2, 0.5, lambda a: cf(c, mare(a_="12", b_="10", n="3"), XE, 360, 92, a))
    E.frase(c, t, b2, [("t", "g", 58, ENT)] + ps("em minutos,", "i", 56) + [("h", "g", 58)] + ps("em metros", "i", 56), XE, 470, "left", 0.08)
    for i, (tt, partes) in enumerate(((c2, ps("altura", "i", 62) + [("máxima?", "g", 68, LB)]),
                                      (d2, ps("altura", "i", 62) + [("mínima?", "g", 68, LB)]),
                                      (e2, ps("tempo de", "i", 62) + [("uma volta?", "g", 68, LC)]))):
        y = 640 + i * 130
        E.foco(c, t, tt, 0.5, lambda a, y=y, i=i: centro(c, str(i + 1), XE + 30, y, 60, "g", COR, a))
        E.frase(c, t, tt, partes, XE + 100, y, "left", 0.1)
    E.relogio(c, t, C["s13.a"], 1520, 440, 170)


# ---------------- resposta ----------------
RCX, RCY, RK = 1520, 960 - 12 * 26, 26    # centro da roda a 12 m; 26 px por metro; chão em y = 960
RR = 10 * RK


def roda(c, t, t0, ang, cota=None, a=1.0):
    """roda-gigante: chão, torre, aro, raios e a cadeira no ângulo ang (graus, 0 = no alto, girando no sentido horário)"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.6) * a
    chao = RCY + 12 * RK
    M.line(c, RCX - 420, chao, RCX + 360, chao, TINTA, q, 5)
    for dx in (-150, 150):
        M.line(c, RCX, RCY, RCX + dx, chao, TINTA2, q, 8)
    c.drawCircle(RCX, RCY, RR, M.paint(TINTA, q, stroke=6))
    for k in range(8):
        th = math.radians(k * 45)
        M.line(c, RCX, RCY, RCX + RR * math.sin(th), RCY - RR * math.cos(th), TINTA2, q * 0.6, 3)
    c.drawCircle(RCX, RCY, 12, M.paint(TINTA, q))
    th = math.radians(ang)
    X, Y = RCX + RR * math.sin(th), RCY - RR * math.cos(th)
    M.rrect(c, X - 28, Y - 18, 56, 36, 10, E.COR, q)   # a cadeira, centrada no ponto do aro (a altura da fórmula)
    c.drawCircle(X, Y, 6, M.paint(BR, q))
    # régua: 0, 2, 12 e 22 m
    xr = RCX - 380
    M.line(c, xr, chao, xr, chao - 22 * RK, TINTA, q, 4)
    for m in (0, 2, 12, 22):
        Yr = chao - m * RK
        M.line(c, xr - 14, Yr, xr, Yr, TINTA, q, 4)
        E.escreve(c, str(m), xr - 24 - E.larg(str(m), "b", 40), Yr + 14, 40, "b", TINTA, q)
        M.line(c, xr, Yr, RCX - (RR if m == 12 else 0), Yr, FIO if m != 12 else LA, q, 3 if m != 12 else 4, dash=E.TRACO)
    E.escreve(c, "m", xr - 22, chao - 22 * RK - 30, 40, "i", TINTA2, q)
    return X, Y


def b_resposta(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    # a cadeira gira (uma volta a cada 8 s de vídeo) e para embaixo quando a fala chega em t = 3
    if t < b5:
        ang = 360 * ((t - C["s14"]) / 8.0)
    else:
        ang0 = 360 * ((b5 - C["s14"]) / 8.0)
        alvo = math.ceil((ang0 - 180) / 360) * 360 + 180
        ang = lerp(ang0, alvo, ease_io(prog(t, b5, 1.2)))
    roda(c, t, C["s14"], ang)
    if t >= a5:  # a altura da roda de ponta a ponta
        q = ep(t, a5, 0.6)
        xx = RCX + 40
        M.arrow(c, xx, RCY, xx, RCY - RR + 6, LB, q, 6, 22, 1.0)
        M.arrow(c, xx, RCY, xx, RCY + RR - 6, LB, q, 6, 22, 1.0)
        E.foco(c, t, a5 + 0.3, 0.4, lambda a: (M.rrect(c, xx + 12, RCY - 84, 130, 60, 14, E.PAPEL, 0.9 * a),
                                               E.formula(c, "20 m", xx + 20, RCY - 40, 46, "g", LB, a)))
    E.frase(c, t, C["s14"] + 0.1, ps("vamos lá", "i", 64, COR), XE, 170, "left", 0.1)
    E.foco(c, t, a4, 0.5, lambda a: cf(c, [("máx = ", TINTA), ("12", LA), (" + ", TINTA), ("10", LB), (" = 22 m", TINTA)], XE, 300, 66, a))
    E.foco(c, t, b4, 0.5, lambda a: cf(c, [("mín = ", TINTA), ("12", LA), (" − ", TINTA), ("10", LB), (" = 2 m", TINTA)], XE, 420, 66, a))
    E.foco(c, t, c4, 0.5, lambda a: cf(c, [("f{πt}{3}", LC), ("  →  período = 2 · 3 = 6 min", TINTA)], XE, 570, 56, a))
    resp(c, t, d4, [("1 volta a cada 6 min", BR)], XE + 300, 700, 56, cor=LC)
    E.foco(c, t, a5, 0.5, lambda a: cf(c, [("22 − 2 = 20 m", LB)], XE, 840, 60, a))
    E.foco(c, t, b5, 0.5, lambda a: cf(c, [("t = 3:  ", ENT), ("f{π · 3}{3} = π", LC)], XE + 450, 840, 60, a))
    E.frase(c, t, c5, ps("a cadeira no", "i", 50) + [("ponto mais baixo,", "g", 54, LB)] + ps("na metade da volta", "i", 50), XE, 1030, "left", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s16.a", ps("o número somado:", "i", 62) + [("nível médio", "g", 66, LA)]),
                 ("s16.b", [("máx = a + b,", "g", 66, LB), ("mín = a − b", "g", 66, LB)]),
                 ("s16.c", ps("período: quando", "i", 62) + [("o de dentro = 2π", "g", 66, LC)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, "left", 0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    a7, b7 = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s17"] + 0.2, ps("na próxima aula, você", "i", 70), XE, 200, passo=0.1)
    E.frase(c, t, a7, [("pratica o ciclo inteiro", "g", 84, COR)], XE, 320, passo=0.1)
    E.frase(c, t, b7, ps("radianos, sinais, relação fundamental e ondas", "i", 56), XE, 450, passo=0.08)
    E.frase(c, t, b7 + 2.0, ps("em questões no estilo da prova", "i", 56, TINTA2), XE, 540, passo=0.08)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, altura=b_altura, periodo=b_periodo, quando=b_quando,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
