"""Visual — Estudativo · MAT-EXP-002: crescimento e decaimento, somar ou multiplicar.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, t, expoente e entrada em índigo (ENT); saída e base
em preto (SAI); fx() pinta só o expoente de índigo; plano à direita e texto/tabela à esquerda; tabela em pé com a escada de setas
curvas (×fator) na lateral; o modelo afim em preto, o exponencial na cor da matéria.
Nesta aula: valores em linha com saltos por cima (linha_valores(), saltos()); plano da população em mil (PM, 50 anos) com a reta
afim tracejada atrás da curva exponencial; plano do carro em mil reais (PC, 10 anos); o teste da tabela = escada preta (subtrair)
e escada índigo (dividir) ao lado da mesma tabela."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / t / expoente / entrada · y / saída / base
ARQUIVO_FINAL = "estudativo_MAT-EXP-002_crescimento_e_decaimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("somar", "carro", "teste", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def fx(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """fórmula em pedaços de cor: partes = [(escrita de E.formula, cor)]; "^x" sozinho é o expoente do pedaço anterior.
    Devolve (largura, [x de cada pedaço], [largura de cada pedaço])."""
    sub = lambda s: s.startswith("_") and len(s) > 1  # "_0" = índice embaixo, como em P zero
    ws = [E.larg(s[1:], est, size * 0.6) + size * 0.06 if sub(s) else E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    xs = []
    for (s, cor), wi in zip(partes, ws):
        xs.append(xx)
        if a > 0:
            if sub(s):
                E.escreve(c, s[1:], xx, y + size * 0.2, size * 0.6, est, cor, a)
            else:
                E.formula(c, s, xx, y, size, est, cor, a)
        xx += wi
    return w, xs, ws


def fx_em(c, t, t0, partes, x, y, size, align="left", d=0.5):
    E.foco(c, t, t0, d, lambda a: fx(c, partes, x, y, size, a, align))


def lei(base, e="x", nome=True, cb=None, ce=None):
    """f(x) = base^x com o x em índigo"""
    cb, ce = cb or SAI, ce or ENT
    pre = [("f(", cb), ("x", ce), (") = ", cb)] if nome else []
    return pre + [(base, cb), ("^" + e, ce)]


def eixos(c, t, P, tx, ty=None, tg=None, size=38, passo_x=1, passo_y=1, nomes=("x", "y"), fmt=None):
    """plano em etapas (o mesmo da trilha Funções): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty;
    marcas de passo_x em passo_x e de passo_y em passo_y; nomes = rótulos dos eixos; fmt = valor -> texto"""
    ty = tx if ty is None else ty
    fmt = fmt or E._num
    x, y, w, h = P.caixa
    xs = [v for v in E._marcas(P.xmin, P.xmax, passo_x)]
    ys = [v for v in E._marcas(P.ymin, P.ymax, passo_y)]
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in xs:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in ys:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, nomes[0], x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(xs):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                centro(c, fmt(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, nomes[1], P.ox + 22, y - 18, 56, "i", SAI, a))
        for i, v in enumerate(ys):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                E.escreve(c, fmt(v), P.ox - 20 - E.larg(fmt(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas; xv/yv aceitam a escrita de E.formula"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = [("(", cy_ if cores else TINTA), (xv, cx_), (", ", cy_ if cores else TINTA), (yv, cy_), (")", cy_ if cores else TINTA)]
    return fx(c, partes, x, y, size, a, align, est)[0]


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anel(c, t, t0, X, Y, cor=None):
    """anel que se abre num ponto: chama a atenção para ele"""
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def celula(c, s, cx, cy, size, cor, a):
    """valor centrado na casa (cx, cy): número ou fração (f{1}{2})"""
    if "f{" in s:
        E.formula(c, s, cx, cy + size * 0.25, size * 0.92, "g", cor, a, "center")
    else:
        E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def tabela(c, t, x0, y0, xs, cols, tc, wc=170, hl=100, size=62, escuro=False, luz=None, nome_x="x"):
    """tabela em pé: coluna x (índigo) e cols = [(cabeçalho em partes de fx, valores, instante de cada valor)];
    luz(i) = destaque (0..1) da linha i. Devolve a função linha → y do centro."""
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    n = 1 + len(cols)
    ry = lambda i: y0 + 10 + hl * i + hl / 2
    a = ep(t, tc, 0.5)
    if a > 0:
        centro(c, nome_x, x0 + wc / 2, y0 - 34, 58, "i", ca, a)
        for j, (cab, _, _) in enumerate(cols):
            fx(c, cab, x0 + wc * (j + 1.5), y0 - 34, 52, a, "center")
        M.line(c, x0, y0, x0 + n * wc, y0, tinta, a, 4)
        for j in range(1, n):
            M.line(c, x0 + wc * j, y0, x0 + wc * j, y0 + hl * len(xs) + 10, tinta, a, 4)
    for i, xv in enumerate(xs):
        cy = ry(i)
        if luz is not None:
            q = luz(i)
            if q > 0:
                M.rrect(c, x0 - 8, cy - hl / 2 + 4, n * wc + 16, hl - 8, 14, CLARO if escuro else COR, (0.22 if escuro else 0.14) * q)
        E.foco(c, t, tc + 0.3 + 0.1 * i, 0.4, lambda q, xv=xv, cy=cy: celula(c, E._num(xv), x0 + wc / 2, cy, size, ca, q), sobe=6)
        for j, (_, vals, tv) in enumerate(cols):
            if tv[i] is not None:
                E.foco(c, t, tv[i], 0.4, lambda q, s=vals[i], j=j, cy=cy: celula(c, s, x0 + wc * (j + 1.5), cy, size, tinta, q), sobe=6)
    return ry


def seta_curva(c, t, t0, A, B, bojo, rot=None, cor=None, size=36, d=0.5, escuro=False, largura=5):
    """seta curva de A até B (pixels), barriga de `bojo` px para a esquerda de quem anda de A para B; rot numa pílula no meio"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or (CLARO if escuro else COR)
    (x0, y0), (x1, y1) = A, B
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    nx, ny = dy / n, -dx / n
    qx, qy = (x0 + x1) / 2 + nx * bojo, (y0 + y1) / 2 + ny * bojo
    pt = lambda s: ((1 - s) ** 2 * x0 + 2 * (1 - s) * s * qx + s * s * x1, (1 - s) ** 2 * y0 + 2 * (1 - s) * s * qy + s * s * y1)
    path = skia.Path()
    path.moveTo(x0, y0)
    for i in range(1, 31):
        path.lineTo(*pt(p * i / 30))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.9:
        ex, ey = pt(1.0)
        ux, uy = ex - qx, ey - qy
        k = math.hypot(ux, uy) or 1.0
        ux, uy = ux / k, uy / k
        tri = skia.Path()
        tri.moveTo(ex + ux * 6, ey + uy * 6)
        tri.lineTo(ex - ux * 20 - uy * 12, ey - uy * 20 + ux * 12)
        tri.lineTo(ex - ux * 20 + uy * 12, ey - uy * 20 - ux * 12)
        tri.close()
        c.drawPath(tri, M.paint(cor, ep(t, t0 + d * 0.9, 0.15)))
    if rot:
        mx, my = pt(0.5)
        w = E.larg(rot, "g", size) + size * 1.1
        s = 1 if bojo >= 0 else -1
        off = abs(nx) * (w / 2 + 6) + abs(ny) * (size * 0.8 + 6)
        E.foco(c, t, t0 + d * 0.5, 0.4, lambda a: E.pilula(c, rot, mx + s * nx * off, my + s * ny * off, size, "g",
                                                          fundo=cor, cor="#07070F" if escuro else E.SOBRE, a=a), sobe=6)


def escada(c, t, ts, pts, bojo, rot, **kw):
    """setas curvas entre pontos vizinhos (pixels), uma em cada instante de ts: a escada das dobras (×2) ou metades (÷2)"""
    for t0, A, B in zip(ts, pts, pts[1:]):
        seta_curva(c, t, t0, A, B, bojo, rot, **kw)


def faixa_eixo(c, P, x0, x1, q, cor=None):
    """faixa clara sobre o eixo x, de x0 a x1 (valores): a curva chega perto e nunca encosta"""
    if q > 0:
        M.line(c, P.x(x0), P.oy, P.x(x1), P.oy, cor or COR, 0.18 * q, 34)




# ---------------- números desta aula ----------------
def mil(v):
    """10000 -> "10.000"; 36450 -> "36.450\""""
    return f"{int(round(v)):,}".replace(",", ".")


def vg(v):
    """1.03 -> "1,03\""""
    return E._num(v)


def linha_valores(c, t, xs, vals, ts, y, size=70, cor=TINTA):
    """valores lado a lado, cada um no seu instante"""
    for X, s, t0 in zip(xs, vals, ts):
        E.foco(c, t, t0, 0.4, lambda a, X=X, s=s: E.formula(c, s, X, y, size, "g", cor, a, "center"), sobe=6)


def saltos(c, t, xs, y, rots, ts, cor=None, size=34, bojo=46):
    """setas curvas por cima de uma linha de valores, cada uma com a sua pílula"""
    for i, (rot, t0) in enumerate(zip(rots, ts)):
        seta_curva(c, t, t0, (xs[i] + 20, y), (xs[i + 1] - 20, y), bojo, rot, cor=cor, size=size)


PM = E.Plano(1080, 150, 720, 780, 0, 50, 0, 50)     # população em mil, 50 anos
PC = E.Plano(1080, 150, 720, 780, 0, 10, 0, 50)     # carro em mil reais, 10 anos
afim = lambda t: 10 + 0.3 * t
expo = lambda t: 10 * 1.03 ** t
carro = lambda t: 50 * 0.9 ** t
assert 10000 + 300 * 50 == 25000 and 43000 < 10000 * 1.03 ** 50 < 44000
assert round(10000 * 1.03) == 10300 and round(10000 * 1.03 ** 2) == 10609
assert [round(50000 * 0.9 ** k) for k in range(4)] == [50000, 45000, 40500, 36450] and round(50000 * 0.9 ** 10) in range(17400, 17450)
assert [round(1000 * 1.1 ** k) for k in range(4)] == [1000, 1100, 1210, 1331]
assert [round(100 * 1.3 ** k, 1) for k in range(4)] == [100, 130, 169, 219.7]


def plano_pop(c, t, t0):
    eixos(c, t, PM, t0, t0, t0, passo_x=10, passo_y=10, nomes=("t", "P (mil)"))


def plano_carro(c, t, t0):
    eixos(c, t, PC, t0, t0, t0, passo_x=2, passo_y=10, nomes=("t", "V (mil R$)"))


# ---------------- gancho ----------------
def cidade(c, t, cx, nome, cor, ta, tb, rot, td, t2, v2):
    E.foco(c, t, ta - 1.2, 0.5, lambda a: E.pilula(c, nome, cx, 250, 50, "g", fundo=cor, a=a))
    E.frase(c, t, ta, [("10.000", "g", 120)], cx, 440, "center")
    E.foco(c, t, tb, 0.5, lambda a: E.pilula(c, rot, cx, 540, 50, "g", fundo=cor, cor=BR, a=a))
    E.foco(c, t, td, 0.5, lambda a: (centro(c, "1 ano", cx, 690, 48, "i", TINTA2, a), centro(c, "10.300", cx, 790, 96, "g", TINTA, a)))
    if t2 is not None:
        E.foco(c, t, t2, 0.5, lambda a: (centro(c, "50 anos", cx, 900, 48, "i", TINTA2, a), centro(c, v2, cx, 1000, 96, "g", cor, a)))


def b_gancho(c, t, C, b):
    def cena():
        M.line(c, W / 2, 220, W / 2, 1020, FIO, ep(t, C["s01.a"], 0.5), 4)
        cidade(c, t, 560, "cidade 1", TINTA, C["s01.a"], C["s01.b"], "+300 por ano", C["s01.d"], C["s02.a"] if t >= C["s02"] else None, "25.000")
        cidade(c, t, 1360, "cidade 2", COR, C["s01.a"], C["s01.c"], "+3% ao ano", C["s01.d"], C["s02.b"] if t >= C["s02"] else None, "mais de 43 mil")
        E.saida(c, t, C["s02"] - 0.1, lambda: E.frase(c, t, C["s01.d"] + 1.6, ps("parece a mesma coisa", "i", 56, TINTA2), W / 2, 160, "center"))
    E.saida(c, t, C["s02.c"] - 0.1, cena)
    if t < C["s02.c"]:
        return
    tb, te = C["s02.c"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("somar", "g", 120), ("ou", "i", 110)], XE, 470)
    E.frase(c, t, tb + 1.8, [("multiplicar?", "g", 120, COR)], XE, 610)
    E.frase(c, t, tb + 3.0, [("a", "i", 80), ("lei", "g", 84), ("de", "i", 80), ("cada", "i", 80), ("uma", "i", 80)], XE, 780)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (E.escreve(c, "função afim:", 430, y, 84, "g", COR, a),
                                     E.escreve(c, "muda sempre o mesmo valor", 1000, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, [("+15% → ×1,15", SAI)], 430, y, 84, a),
                                     fx(c, [("−20% → ×0,8", SAI)], 1060, y, 84, a))),
             ("s03.c", lambda a, y: (E.escreve(c, "exponencial:", 430, y, 84, "g", COR, a),
                                     fx(c, lei("2"), 1000, y, 96, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- somar: afim ----------------
XL = [270, 520, 770]


def b_somar(c, t, C, b):
    plano_pop(c, t, C["s04"])
    E.frase(c, t, C["s04"], [("cidade", "i", 64), ("1", "g", 70)], XE, 190)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: E.pilula(c, "+300 por ano", 600, 168, 46, "g", fundo=TINTA, a=a))
    tv = [C["s04.b"], C["s04.b"] + 0.9, C["s04.b"] + 1.9]
    linha_valores(c, t, XL, ["10.000", "10.300", "10.600"], tv, 470, 60)
    linha_valores(c, t, XL, ["ano 0", "ano 1", "ano 2"], tv, 540, 40, TINTA2)
    saltos(c, t, XL, 390, ["+300", "+300"], [tv[1] - 0.3, tv[2] - 0.3], cor=TINTA, bojo=50)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: fx(c, [("P = 10.000 + 300 · ", SAI), ("t", ENT)], XE, 720, 76, a))
    E.frase(c, t, C["s04.c"] + 2.0, [("t", "g", 52, ENT), ("em", "i", 52, TINTA2), ("anos", "i", 52, TINTA2)], XE, 810)
    E.curva(c, t, C["s04.d"], PM, afim, 0, 50, d=1.0, cor=TINTA)
    E.frase(c, t, C["s04.d"], [("uma", "i", 76), ("reta", "g", 84)], XE, 950)
    E.foco(c, t, C["s04.d"] + 0.8, 0.4, lambda a: centro(c, "afim", PM.x(40), PM.y(afim(40)) + 60, 46, "b", TINTA, a))


# ---------------- multiplicar: exponencial ----------------
def contas_dir(c, t, itens, x=1000, y1=520, y2=660, size=84):
    for t0, t1, l1, l2, dr in itens:
        def d(t0=t0, l1=l1, l2=l2, dr=dr):
            fx_em(c, t, t0, l1, x, y1, size)
            fx_em(c, t, t0 + dr, l2, x + 40, y2, size)
        if t >= t0:
            if t1:
                E.saida(c, t, t1 - 0.1, d)
            else:
                d()


TT = (0, 1, 2)


def b_multiplicar(c, t, C, b):
    E.saida(c, t, C["s07"] - 0.1, lambda: (
        E.frase(c, t, C["s05"], [("cidade", "i", 64), ("2", "g", 70, COR)], XE, 190),
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "+3% do que já existe", 720, 168, 46, "g", a=a))))

    def tab():
        tv = [C["s05"] + 0.4, C["s05.c"] + 2.4, C["s05.d"] + 3.0]
        tabela(c, t, XE, 330, TT, [([("P", SAI)], ["10.000", "10.300", "10.609"], tv)], C["s05"] + 0.3, 220, 110, size=56, nome_x="t")
        ry = lambda i: 330 + 10 + 110 * i + 55
        escada(c, t, [C["s05.c"] + 0.6, C["s05.d"] + 0.6], [(XE + 440 + 14, ry(i)) for i in range(3)], 46, "×1,03", cor=COR)
        if t >= C["s06.a"]:
            for i, (rot, t0) in enumerate((("+300", C["s06.a"]), ("+309", C["s06.a"] + 1.0))):
                E.foco(c, t, t0, 0.4, lambda a, i=i, rot=rot: E.pilula(c, rot, XE + 720, ry(i) + 55, 42, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s07"] - 0.1, tab)
    E.saida(c, t, C["s06"] - 0.1, lambda: (
        E.foco(c, t, C["s05.b"], 0.5, lambda a: fx(c, [("+3%  →  ×1,03", COR)], 1000, 360, 96, a)),
        contas_dir(c, t, [(C["s05.c"], C["s05.d"], [("10.000 · 1,03", SAI)], [("= 10.300", COR)], 2.4),
                          (C["s05.d"], None, [("10.300 · 1,03", SAI)], [("= 10.609", COR)], 3.0)])))
    if C["s06"] <= t < C["s07"]:
        E.frase(c, t, C["s06"], ps("3% de um número maior", "i", 60), 1000, 360)
        E.frase(c, t, C["s06.a"] + 1.6, [("o", "i", 66), ("salto", "g", 70), ("cresce", "g", 70, COR)], 1000, 470)
        E.foco(c, t, C["s06.b"] - 2.4, 0.5, lambda a: fx(c, [("1,03 · 1,03 · … · 1,03", SAI)], 1000, 700, 64, a))
        q = ep(t, C["s06.b"] - 1.8, 0.4)
        if q > 0:
            E.chave(c, 1000, 1000 + fx(c, [("1,03 · 1,03 · … · 1,03", SAI)], 0, 0, 64, 0)[0], 730, TINTA2, q, 20, 5)
            fx(c, [("t", ENT), (" vezes", TINTA2)], 1240, 800, 50, q)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: fx(c, [("= 1,03", COR), ("^t", ENT)], 1000, 930, 110, a))
    if t < C["s07"]:
        return
    # a lei
    plano_pop(c, t, C["s07"])
    E.curva(c, t, C["s07"], PM, afim, 0, 50, d=0.1, cor=TINTA2, tracejada=True)
    E.foco(c, t, C["s07"], 0.4, lambda a: centro(c, "afim", PM.x(40), PM.y(afim(40)) + 60, 46, "b", TINTA2, a))
    lei_ = [("P = P", SAI), ("_0", SAI), (" · 1,03", COR), ("^t", ENT)]
    w, xs, ws = fx(c, lei_, XE, 0, 110, 0)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: fx(c, lei_, XE, 320, 110, a))
    for k, partes, y in (("s07.b", [("P", SAI), (": população no ano ", TINTA2), ("t", ENT)], 590),
                         ("s07.c", [("P", SAI), ("_0", SAI), (": população do começo (", TINTA2), ("t", ENT), (" = 0)", TINTA2)], 680)):
        E.foco(c, t, C[k], 0.5, lambda a, partes=partes, y=y: fx(c, partes, XE, y, 48, a, est="b"))
    xb = xs[2] + ws[2] / 2 + 20
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (E.pilula(c, "fator na base", xb, 450, 44, "g", fundo=COR, a=a),
                                             M.arrow(c, xb, 418, xb, 350, COR, a, 5, 18)))
    xt = xs[3] + ws[3] / 2
    E.foco(c, t, C["s07.d"] + 1.2, 0.5, lambda a: (E.pilula(c, "tempo no expoente", xt - 60, 170, 44, "g", fundo=ENT, a=a),
                                                   M.arrow(c, xt, 205, xt, 236, ENT, a, 5, 16)))
    E.curva(c, t, C["s07.e"], PM, expo, 0, 50, d=1.4, cor=COR)
    E.foco(c, t, C["s07.e"] + 1.2, 0.4, lambda a: centro(c, "exponencial", PM.x(36), PM.y(expo(48)) - 10, 46, "b", COR, a))
    E.frase(c, t, C["s07.e"], [("base", "i", 70), ("1,03", "g", 76, COR), (">", "g", 76), ("1:", "g", 76), ("sobe", "g", 80, COR)], XE, 960)


# ---------------- carro: decaimento ----------------
TC = (0, 1, 2, 3)
VC = ["50.000", "45.000", "40.500", "36.450"]


def tab_carro(c, t, t0, tv=None, luz=None):
    tabela(c, t, XE, 330, TC, [([("V", SAI)], VC, tv or [t0] * 4)], t0, 230, 110, size=56, luz=luz, nome_x="t")
    return lambda i: 330 + 10 + 110 * i + 55


def b_carro(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], ps("no caminho contrário", "i", 76), W / 2, 260, "center")
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.pilula(c, "carro: R$ 50.000", W / 2, 440, 70, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s08.a"] + 1.4, [("perde", "i", 76), ("10%", "g", 84, ERRADO), ("por", "i", 76), ("ano", "i", 76)], W / 2, 620, "center")
        E.foco(c, t, C["s08.b"], 0.5, lambda a: fx(c, [("−10%  →  ×0,9", COR)], W / 2, 860, 130, a, "center"))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    plano_carro(c, t, C["s09"])
    tv = [C["s09"], C["s09.a"] + 2.6, C["s09.b"] + 2.8, C["s09.c"] + 0.4]
    E.saida(c, t, C["s09.d"] - 0.1, lambda: fx_em(c, t, C["s09"], [("fator 0,9", COR)], XE, 190, 70))
    ry = tab_carro(c, t, C["s09"], tv)
    escada(c, t, [tv[1] - 0.6, tv[2] - 0.6, tv[3] - 0.3], [(XE + 460 + 14, ry(i)) for i in range(4)], 46, "×0,9", cor=COR)
    for i in range(4):
        E.ponto(c, t, tv[i], PC, i, carro(i), cor=TINTA, r=14)
    contas_dir(c, t, [(C["s09.a"], C["s09.b"], [("50.000 · 0,9", SAI)], [("= 45.000", COR)], 2.6),
                      (C["s09.b"], C["s09.c"], [("45.000 · 0,9", SAI)], [("= 40.500", COR)], 2.8)], x=XE, y1=880, y2=970, size=60)
    E.saida(c, t, C["s09.d"] - 0.1, lambda: E.foco(c, t, C["s09.c"], 0.5, lambda a: fx(c, [("3 anos: 36.450", COR)], XE, 900, 60, a)))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: fx(c, [("V = 50.000 · 0,9", SAI), ("^t", ENT)], XE, 190, 80, a))
    E.curva(c, t, C["s09.e"], PC, carro, 0, 10, d=1.4, cor=TINTA)
    E.foco(c, t, C["s09.e"] + 0.6, 0.5, lambda a: E.pilula(c, "decaimento", XE + 200, 900, 52, "g", fundo=TINTA, a=a))


# ---------------- o teste da tabela ----------------
def b_teste(c, t, C, b):
    E.frase(c, t, C["s10"], ps("só uma tabela?", "i", 76), XE, 190)
    ry = tab_carro(c, t, C["s10"] - 0.5)
    X = XE + 460 + 14
    E.saida(c, t, C["s11"] - 0.1, lambda: escada(c, t, [C["s10.a"] + 0.3 + 0.5 * i for i in range(3)], [(X, ry(i)) for i in range(4)], 46,
                                                 None, cor=TINTA))
    for i, rot in enumerate(("−5.000", "−4.500", "−4.050")):
        E.saida(c, t, C["s11"] - 0.1, lambda i=i, rot=rot: E.foco(c, t, C["s10.a"] + 0.5 + 0.5 * i, 0.4, lambda a: E.pilula(
            c, rot, X + 150, (ry(i) + ry(i + 1)) / 2, 40, "g", fundo=TINTA, a=a)))
    escada(c, t, [C["s11.a"] + 0.3 + 0.5 * i for i in range(3)], [(X, ry(i)) for i in range(4)], 46, None, cor=COR)
    for i in range(3):
        E.foco(c, t, C["s11.a"] + 0.5 + 0.5 * i, 0.4, lambda a, i=i: E.pilula(c, "÷ = 0,9", X + 150, (ry(i) + ry(i + 1)) / 2, 40, "g", a=a))
    XR = 1040
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.pilula(c, "1º teste: subtraia", XR + 250, 330, 50, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s10.b"], [("sempre", "i", 60), ("igual?", "i", 60), ("afim", "g", 66)], XR, 460)
    E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: E.pilula(c, "soma", XR + 590, 440, 42, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.pilula(c, "2º teste: divida", XR + 230, 600, 50, "g", a=a))
    E.frase(c, t, C["s11.b"], [("sempre", "i", 60), ("igual?", "i", 60), ("exponencial", "g", 66, COR)], XR, 730)
    E.foco(c, t, C["s11.b"] + 1.4, 0.4, lambda a: E.pilula(c, "multiplica", XR + 400, 810, 42, "g", a=a))
    E.frase(c, t, C["s11.c"], [("o", "i", 60), ("número", "i", 60), ("=", "g", 60), ("o", "i", 60), ("fator", "g", 66, COR)], XR, 920)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: fx(c, [("45.000 ÷ 50.000 = 0,9", COR)], XE, 860, 64, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def s12():
        E.frase(c, t, C["s12"], ps("cuidado com este erro", "i", 72), W / 2, 230, "center")
        E.foco(c, t, C["s12.a"], 0.5, lambda a: fx(c, [("10 anos · 10% = 100%", ERRADO)], W / 2, 520, 110, a, "center"))
        E.foco(c, t, C["s12.b"], 0.5, lambda a: fx(c, [("vale R$ 0?", ERRADO)], W / 2, 760, 150, a, "center"))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    plano_carro(c, t, C["s13"])
    E.curva(c, t, C["s13.a"], PC, carro, 0, 10, d=2.0, cor=TINTA)
    E.frase(c, t, C["s13"], [("não", "g", 90, ERRADO)], XE, 250)
    E.frase(c, t, C["s13.a"], [("tira", "i", 66), ("10%", "g", 70, COR), ("do", "i", 66), ("que", "i", 66), ("sobrou", "g", 70)], XE, 400)
    E.ponto(c, t, C["s13.b"], PC, 10, carro(10), cor=CERTO, r=16, guias=True)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: fx(c, [("10 anos: ≈ R$ 17.400", CERTO)], XE, 580, 76, a))
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: centro(c, "≈ 17,4", PC.x(9), PC.y(carro(10)) - 40, 44, "b", CERTO, a))
    faixa_eixo(c, PC, 0, 10, ep(t, C["s13.c"], 0.5), TINTA)
    E.frase(c, t, C["s13.c"], [("nunca", "g", 84, COR), ("chega", "i", 76), ("a", "i", 76), ("zero", "g", 84)], XE, 780)


# ---------------- atalho (palco escuro) ----------------
XA = [560, 820, 1080, 1340]


def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s14.a"], [("olhe", "i", 110, BR), ("os", "i", 110, BR), ("saltos", "g", 120, BR)], XE + 540, 190)
        linha_valores(c, t, XA, ["100", "130", "160", "190"], [C["s14.b"] - 0.6] * 4, 470, 76, BR)
        saltos(c, t, XA, 390, ["+30", "+30", "+30"], [C["s14.b"] - 0.4 + 0.3 * i for i in range(3)], cor=CLARO, bojo=50)
        E.foco(c, t, C["s14.b"] + 0.6, 0.4, lambda a: E.pilula(c, "iguais: afim", 1680, 450, 46, "g", fundo=BR, cor="#07070F", a=a))
        linha_valores(c, t, XA, ["100", "130", "169", "219,7"], [C["s14.c"] - 0.6] * 4, 800, 76, BR)
        saltos(c, t, XA, 720, ["+30", "+39", "+50,7"], [C["s14.c"] - 0.4 + 0.3 * i for i in range(3)], cor=CLARO, bojo=50)
        E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: E.pilula(c, "crescem: divida", 1680, 780, 46, "g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, C["s14.c"] + 1.6, 0.4, lambda a: centro(c, "÷ = 1,3", 1680, 900, 52, "g", CLARO, a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], ps("por que funciona", "i", 70, CLARO), XE, 200)
    E.frase(c, t, C["s15.a"], [("afim:", "g", 76, BR), ("soma", "i", 72, CLARO), ("sempre", "i", 72, CLARO), ("o", "i", 72, CLARO),
                               ("mesmo", "g", 76, BR), ("valor", "i", 72, CLARO)], XE, 380)
    E.frase(c, t, C["s15.b"], [("exponencial:", "g", 76, BR), ("soma", "i", 72, CLARO), ("uma", "i", 72, CLARO), ("%", "g", 76, BR)], XE, 520)
    E.frase(c, t, C["s15.b"] + 1.2, [("de", "i", 72, CLARO), ("um", "i", 72, CLARO), ("valor", "i", 72, CLARO), ("que", "i", 72, CLARO),
                                     ("muda", "g", 76, BR)], XE + 160, 620)
    E.frase(c, t, C["s15.b"] + 3.0, ps("taxa pequena e números arredondados:", "i", 60, CLARO), XE, 790)
    E.frase(c, t, C["s15.b"] + 4.6, ps("os saltos parecem iguais", "i", 60, CLARO), XE, 870)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "faça a divisão", 1500, 830, 60, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
XQ = [560, 840, 1120, 1400]
YA, YB = 470, 760


def perfis(c, t, ta, tb, tc, tr=None):
    E.foco(c, t, ta, 0.4, lambda a: (E.escreve(c, "mês", XE, 300, 48, "i", ENT, a),
                                     [centro(c, str(i), X, 300, 52, "g", ENT, a) for i, X in enumerate(XQ)]))
    E.foco(c, t, tb[0], 0.4, lambda a: E.pilula(c, "A", 300, YA - 24, 56, "g", fundo=COR, a=a))
    E.foco(c, t, tc[0], 0.4, lambda a: E.pilula(c, "B", 300, YB - 24, 56, "g", fundo=TINTA, a=a))
    linha_valores(c, t, XQ, ["1.000", "1.100", "1.210", "1.331"], tb, YA, 70)
    linha_valores(c, t, XQ, ["1.000", "1.100", "1.200", "1.300"], tc, YB, 70)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s16.a"], [("começam", "i", 60), ("com", "i", 60), ("1.000", "g", 64), ("seguidores", "i", 60)], 900, 190)
    perfis(c, t, C["s16.a"] + 0.6, [C["s16.b"] + 0.7 * i for i in range(4)], [C["s16.c"] + 0.7 * i for i in range(4)])
    E.frase(c, t, C["s16.d"], [("qual", "i", 66), ("é", "i", 66), ("exponencial?", "g", 66, COR)], XE, 960)
    E.frase(c, t, C["s16.d"] + 1.4, [("a", "i", 66), ("lei", "g", 66), ("de", "i", 66), ("cada", "i", 66), ("um", "i", 66)], 1000, 960)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1700, cy=560, r=60)


def b_resposta(c, t, C, b):
    t0 = C["s18"] - 2
    perfis(c, t, t0, [t0] * 4, [t0] * 4)
    saltos(c, t, XQ, YB - 80, ["+100"] * 3, [C["s18.a"] + 0.3 * i for i in range(3)], cor=TINTA, bojo=44)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: (fx(c, [("S = 1.000 + 100 · ", SAI), ("t", ENT)], XQ[0] - 40, YB + 130, 64, a),
                                             E.pilula(c, "afim", 1440, YB + 108, 44, "g", fundo=TINTA, a=a)))
    saltos(c, t, XQ, YA - 80, ["+100", "+110", "+121"], [C["s19.a"] + 0.7 * i for i in range(3)], cor=COR, bojo=44)
    E.saida(c, t, C["s19.d"] - 0.1, lambda: (
        fx_em(c, t, C["s19.b"], [("1.100 ÷ 1.000 = 1,1", COR)], XQ[0] - 40, 960, 60),
        fx_em(c, t, C["s19.c"], [("1.210 ÷ 1.100 = 1,1", COR)], 1180, 960, 60)))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "×1,1 = +10% ao mês", 1500, 190, 46, "g", a=a))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: (fx(c, [("S = 1.000 · 1,1", SAI), ("^t", ENT)], XQ[0] - 40, 990, 70, a),
                                             E.pilula(c, "exponencial", 1260, 965, 44, "g", a=a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", lambda a, y: E.frase(c, t, -99, [("somar", "g", 84), ("o", "i", 80), ("mesmo", "i", 80), ("valor:", "i", 80),
                                                            ("afim", "g", 84)], 400, y)),
                 ("s20.b", lambda a, y: (E.frase(c, t, -99, [("multiplicar", "g", 72, COR), ("pelo", "i", 68), ("mesmo", "i", 68), ("fator:", "i", 68),
                                                             ("exponencial", "g", 72, COR)], 400, y),
                                         fx(c, [("P = P", SAI), ("_0", SAI), (" · fator", COR), ("^t", ENT)], 400, y + 130, 76, a))))
        for i, (k, fn) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21.a"], [("dobrar", "g", 120, COR), ("e", "i", 110)], XE, 410)
    E.frase(c, t, C["s21.a"] + 0.6, [("meia-vida", "g", 120, COR)], XE, 540)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "remédio: 3 meias-vidas", XE + 340, 680, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s21.b"] + 2.4, 0.5, lambda a: E.pilula(c, "bactérias: dobram a cada 20 min", XE + 440, 800, 50, "g", a=a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, somar=b_somar, multiplicar=b_multiplicar, carro=b_carro, teste=b_teste,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
