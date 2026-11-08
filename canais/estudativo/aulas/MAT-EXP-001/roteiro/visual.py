"""Visual — Estudativo · MAT-EXP-001: função exponencial, lei e gráfico. Primeira aula da trilha Exponencial e Logaritmo.

Linguagem visual da trilha Exponencial e Logaritmo (as próximas aulas copiam daqui; herda a trilha Funções):
- x, expoente e entrada = índigo da matéria (ENT); y, saída e a base = tinta preta (SAI). Eixo x índigo, eixo y preto (eixos()).
- na fórmula, o expoente que é a entrada sai em índigo e o resto em preto: fx(c, [("f(x) = 2", SAI), ("^x", ENT)], ...).
  Um pedaço "^x" sozinho vira o expoente do pedaço anterior (lei() monta "f(x) = base^x").
- plano sempre na metade direita (P), texto ou tabela à esquerda; par (x, y) com o x índigo e o y preto (par()).
- tabela em pé x | f(x) (tabela()), com a coluna x índigo; a escada de dobras/metades são setas curvas com "×2" ou "÷2"
  numa pílula (seta_curva(), escada()), na lateral da coluna de saída ou numa linha de valores.
- curva crescente (base > 1) em índigo, curva decrescente (0 < base < 1) em preto; no palco escuro, CLARO e branco.
- o ponto (0, 1) sempre ganha anel(); "nunca encosta no eixo x" = faixa clara sobre o eixo (faixa_eixo()).
Peças locais: fx(), lei(), eixos(), par(), tabela(), seta_curva(), escada(), anel(), faixa_eixo(), pilha() da folha dobrada."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · y / saída / base
ARQUIVO_FINAL = "estudativo_MAT-EXP-001_funcao_exponencial_lei_e_grafico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "tabelameio", "base", "atalho", "questao", "fim"))
BR = "#FFFFFF"
P = E.Plano(1080, 150, 720, 780, -3, 3, -1, 9)       # 2^x e (1/2)^x
P2 = E.Plano(1080, 150, 720, 780, -1, 4, -9, 5)      # base negativa
P3 = E.Plano(1080, 150, 720, 780, -3, 3, -3, 8)      # o erro
f2 = lambda x: 2 ** x
fm = lambda x: 0.5 ** x
assert [f2(x) for x in (-2, -1, 0, 1, 2, 3)] == [0.25, 0.5, 1, 2, 4, 8] and 2 ** 10 == 1024
assert [fm(x) for x in (-2, -1, 0, 1, 2, 3)] == [4, 2, 1, 0.5, 0.25, 0.125]
assert [(-2) ** k for k in (1, 2, 3)] == [-2, 4, -8]
assert [3 ** k for k in (0, 1, 2)] == [1, 3, 9] and math.isclose(3 ** -1, 1 / 3) and math.isclose((1 / 3) ** 2, 1 / 9)


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
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    xs = []
    for (s, cor), wi in zip(partes, ws):
        xs.append(xx)
        if a > 0:
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


def eixos(c, t, P, tx, ty=None, tg=None, size=38, passo_y=1, tinta_x=None, tinta_y=None):
    """plano em etapas (o mesmo da trilha Funções): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    cx_, cy_ = tinta_x or ENT, tinta_y or SAI
    x, y, w, h = P.caixa
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in range(math.ceil(P.xmin), math.floor(P.xmax) + 1):
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in range(math.ceil(P.ymin), math.floor(P.ymax) + 1):
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, cx_, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", cx_, a))
        for i, v in enumerate(range(math.ceil(P.xmin), math.floor(P.xmax) + 1)):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, cx_, a, 4),
                centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, cy_, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", cy_, a))
        for i, v in enumerate(range(math.ceil(P.ymin), math.floor(P.ymax) + 1)):
            if v == 0 or v % passo_y:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, cy_, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


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


def tabela(c, t, x0, y0, xs, cols, tc, wc=170, hl=100, size=62, escuro=False, luz=None):
    """tabela em pé: coluna x (índigo) e cols = [(cabeçalho em partes de fx, valores, instante de cada valor)];
    luz(i) = destaque (0..1) da linha i. Devolve a função linha → y do centro."""
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    n = 1 + len(cols)
    ry = lambda i: y0 + 10 + hl * i + hl / 2
    a = ep(t, tc, 0.5)
    if a > 0:
        centro(c, "x", x0 + wc / 2, y0 - 34, 58, "i", ca, a)
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


# ---------------- a folha dobrada ----------------
CAMADA = 18


def pilha(c, cx, by, w, kf, a=1.0, hmax=700):
    """folha vista de lado depois de kf dobras: 2^kf camadas; acima de hmax, a pilha sai da tela"""
    if a <= 0:
        return
    h = CAMADA * 2 ** kf
    alto = min(h, hmax)
    x0, y1 = cx - w / 2, by
    y0 = by - alto
    M.rrect(c, x0, y0, w, alto, 6, BR, a)
    c.save()
    c.clipRect(skia.Rect.MakeLTRB(x0, y0, x0 + w, y1))
    yy = by - CAMADA
    while yy > y0 + 2:
        M.line(c, x0 + 6, yy, x0 + w - 6, yy, TINTA2, 0.55 * a, 2)
        yy -= CAMADA
    c.restore()
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x0 + w, y1), M.paint(TINTA, a, stroke=4))
    if h > hmax:  # passou do teto: some para cima
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y0 - 2), skia.Point(0, y0 + 160)],
                                                   [M.hexc(E.PAPEL, a), M.hexc(E.PAPEL, 0.0)]))
        c.drawRect(skia.Rect.MakeLTRB(x0 - 8, y0 - 4, x0 + w + 8, y0 + 160), g)
        M.arrow(c, cx, y0 + 120, cx, y0 - 60, COR, a * min(1, (h - hmax) / 200), 8, 26)


def dobras(t, C):
    """quantas dobras já foram feitas (contínuo)"""
    b, k = C["s01.b"], C["s01.c"]
    return (ease_io(prog(t, b - 0.4, 0.6)) + ease_io(prog(t, b + 0.9, 0.5)) + ease_io(prog(t, b + 1.6, 0.5))
            + 7 * ease_io(prog(t, k + 0.3, 1.8)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        kf = dobras(t, C)
        a = ep(t, C["s01.a"], 0.5)
        pilha(c, 1450, 850, 380, kf, a, hmax=640)
        n = int(round(2 ** kf))
        if a > 0 and t < C["s01.d"]:
            txt = "1 folha" if n == 1 else f"{n} camadas"
            centro(c, txt, 1450, 930, 52, "b", TINTA, a)
        E.foco(c, t, C["s01.d"], 0.5, lambda q: (
            M.rrect(c, 1450 - 250, 880, 500, 96, 48, COR, q),
            centro(c, "1.024 camadas", 1450, 947, 56, "g", BR, q)), sobe=6)
        E.frase(c, t, C["s01.a"], [("dobre", "g", 96, COR), ("a", "i", 90), ("folha", "i", 90)], XE, 300)
        E.frase(c, t, C["s01.a"] + 0.8, [("ao", "i", 90), ("meio", "i", 90)], XE, 410)
        E.frase(c, t, C["s01.b"], [("a", "i", 76), ("espessura", "i", 76)], XE, 560)
        E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda q: E.pilula(c, "×2", XE + 560, 538, 66, "g", a=q))
        E.frase(c, t, C["s01.c"], [("10", "g", 96, COR), ("dobras", "i", 90)], XE, 720)
        E.frase(c, t, C["s01.d"], [("1.024", "g", 130, COR), ("vezes", "i", 84)], XE, 880)
        E.frase(c, t, C["s01.d"] + 0.8, ps("mais grossa", "i", 70, TINTA2), XE, 970)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return

    def cena2():
        w, xs, ws = fx(c, lei("2", nome=False), 0, 0, 300, 0)
        x0 = 560 - w / 2
        E.foco(c, t, C["s02"] + 0.2, 0.6, lambda a: fx(c, lei("2", nome=False), x0, 640, 300, a))
        ex = xs[1] - xs[0] + x0 + ws[1] / 2
        p = ep(t, C["s02.a"], 0.6)
        if p > 0:
            M.arrow(c, ex + 260, 300, ex + 60, 440, COR, p, 7, 24, p)
            c.drawCircle(ex, 470, 90, M.paint(COR, p * pulso(t, C["s02.a"], 2.5), stroke=6))
        E.frase(c, t, C["s02.a"], [("o", "i", 72), ("x", "g", 84, ENT), ("mora", "i", 72)], ex + 270, 260)
        E.frase(c, t, C["s02.a"] + 0.6, [("no", "i", 72), ("expoente", "g", 76, COR)], ex + 270, 350)
        E.frase(c, t, C["s02.a"] + 1.2, [("10", "g", 70, ENT), ("dobras:", "i", 66), ("2", "g", 70)], 1180, 800)
        E.foco(c, t, C["s02.a"] + 1.8, 0.5, lambda a: fx(c, [("2", SAI), ("^{10}", ENT), (" = 1.024", SAI)], 1180, 920, 84, a))
    E.saida(c, t, C["s02.b"] - 0.1, cena2)
    if t < C["s02.b"]:
        return
    tb, te = C["s02.b"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.2, [("o", "i", 120), ("gráfico", "g", 130, COR)], XE, 470)
    E.frase(c, t, tb + 2.8, [("sobe", "g", 100), ("ou", "i", 96), ("desce", "g", 100)], XE, 640)
    p = ep(t, tb + 3.4, 0.5)
    if p > 0:
        M.arrow(c, XE + 10, 760, XE + 130, 680, COR, p, 8, 26, p)
        M.arrow(c, XE + 400, 680, XE + 520, 760, TINTA, p, 8, 26, p)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (E.escreve(c, "gráfico:", 430, y, 90, "g", COR, a),
                                     E.escreve(c, "tabela, pontos e curva", 860, y, 66, "i", TINTA, a))),
             ("s03.b", lambda a, y: (fx(c, [("2", SAI), ("^{−1}", ENT), (" = f{1}{2}", SAI)], 430, y, 100, a),
                                     E.escreve(c, "expoente negativo vira fração", 860, y, 60, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("9", SAI), ("^{1/2}", ENT), (" = r{9}", SAI)], 430, y, 100, a),
                                     E.escreve(c, "expoente em fração vira raiz", 860, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    E.foco(c, t, C["s04.a"], 0.5, lambda a: fx(c, [("espessura = 2", SAI), ("^{nº de dobras}", ENT)], W / 2, 260, 100, a, "center"))
    partes = lei("2")
    w, xs, ws = fx(c, partes, W / 2, 0, 210, 0, "center")
    E.foco(c, t, C["s04.b"], 0.6, lambda a: fx(c, partes, W / 2, 590, 210, a, "center"))
    E.foco(c, t, C["s04.b"] - 1.2, 0.5, lambda a: E.pilula(c, "x = nº de dobras", W / 2, 362, 46, "g", fundo=ENT, a=a))
    bx = xs[3] + ws[3] / 2 - 0.02 * 210
    ex = xs[4] + ws[4] / 2
    for k, X, Yt, px, rot, fundo in (("s04.c", bx, 630, bx - 210, "a base: fixa", TINTA), ("s04.d", ex, 530, ex + 170, "o expoente: a entrada", ENT)):
        p = ep(t, C[k], 0.5)
        if p > 0:
            M.arrow(c, X + (px - X) * 0.25, 745, X, Yt, fundo, p, 6, 22, p)
        E.foco(c, t, C[k] + 0.2, 0.4, lambda a, px=px, rot=rot, fundo=fundo: E.pilula(c, rot, px, 790, 48, "g", fundo=fundo, a=a), sobe=6)
    E.frase(c, t, C["s04.e"], [("função", "g", 110, COR), ("exponencial", "g", 110, COR)], W / 2, 980, "center")


# ---------------- tabelas ----------------
XS = (-2, -1, 0, 1, 2, 3)
TX, TY, TW, TL = XE, 330, 170, 104
V2 = ("f{1}{4}", "f{1}{2}", "1", "2", "4", "8")
VM = ("4", "2", "1", "f{1}{2}", "f{1}{4}", "f{1}{8}")


def luz_de(t, C, ks, fim):
    """destaque da linha i entre a fala dela (ks[i]) e a próxima"""
    def luz(i):
        k = ks[i]
        if k is None:
            return 0.0
        nxt = [v for v in ks if v is not None and v > k]
        t1 = min(nxt) if nxt else fim
        return ep(t, k, 0.3) * (1 - ep(t, t1 - 0.2, 0.3))
    return luz


def contas(c, t, C, itens, x=880, y1=480, y2=730, size=130):
    """a conta da vez, à direita: itens = [(k0, k1, partes da conta, partes do resultado, atraso do resultado)]"""
    for k0, k1, l1, l2, dr in itens:
        def d(k0=k0, l1=l1, l2=l2, dr=dr):
            fx_em(c, t, C[k0], l1, x, y1, size)
            fx_em(c, t, C[k0] + dr, l2, x + 60, y2, size)
        if t >= C[k0]:
            if k1:
                E.saida(c, t, C[k1] - 0.1, d)
            else:
                d()


def b_tabela2(c, t, C, b):
    fx_em(c, t, C["s05"], lei("2"), XE, 160, 80)
    tv = [C["s06.b"] + 1.2, C["s06.a"] + 1.2, C["s05.a"] + 1.0, C["s05.b"] + 1.0, C["s05.c"] + 0.8, C["s05.d"] + 0.8]
    luz = luz_de(t, C, [C["s06.b"], C["s06.a"], C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]], C["s06.end"])
    tabela(c, t, TX, TY, XS, [(lei("2", nome=False), V2, tv)], C["s05"] + 0.8, TW, TL, luz=luz)
    contas(c, t, C, [("s05.a", "s05.b", [("2", SAI), ("^0", ENT)], [("= 1", COR)], 1.0),
                     ("s05.b", "s05.c", [("2", SAI), ("^1", ENT)], [("= 2", COR)], 1.0),
                     ("s05.c", "s05.d", [("2", SAI), ("^2", ENT), (" = 2 · 2", SAI)], [("= 4", COR)], 0.8),
                     ("s05.d", "s06", [("2", SAI), ("^3", ENT), (" = 2 · 2 · 2", SAI)], [("= 8", COR)], 0.8),
                     ("s06.a", "s06.b", [("2", SAI), ("^{−1}", ENT), (" = f{1}{2^1}", SAI)], [("= f{1}{2}", COR)], 1.2),
                     ("s06.b", None, [("2", SAI), ("^{−2}", ENT), (" = f{1}{2^2}", SAI)], [("= f{1}{4}", COR)], 1.2)])
    E.saida(c, t, C["s06.a"] - 0.1, lambda: E.frase(c, t, C["s06"], [("expoente", "i", 66), ("negativo", "g", 66, ENT), ("vira", "i", 66),
                                                                     ("fração", "g", 66, COR)], 880, 340))


def b_tabelameio(c, t, C, b):
    E.saida(c, t, C["s09.a"] - 0.1, lambda: fx_em(c, t, C["s09"] - 0.6, lei("2"), XE, 160, 80))
    fx_em(c, t, C["s09.a"], lei("(f{1}{2})"), XE, 160, 80)
    E.saida(c, t, C["s09.b"] - 0.1, lambda: (
        E.frase(c, t, C["s09"] + 0.3, [("troque", "i", 84), ("a", "i", 84), ("base", "g", 90)], 880, 420),
        E.foco(c, t, C["s09.a"], 0.5, lambda a: fx(c, [("2  →  f{1}{2}", COR)], 880, 640, 130, a))))
    tv = [C["s10.c"] + 1.0, C["s10.b"] + 0.4, C["s09.b"] + 1.0, C["s09.c"] + 0.8, C["s09.d"] + 0.8, C["s09.e"] + 0.8]
    luz = luz_de(t, C, [C["s10.c"], C["s10.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]], C["s10.end"])
    tabela(c, t, TX, TY, XS, [(lei("(f{1}{2})", nome=False), VM, tv)], C["s09.a"] + 0.5, TW, TL, luz=luz)
    m = "(f{1}{2})"
    contas(c, t, C, [("s09.b", "s09.c", [(m, SAI), ("^0", ENT)], [("= 1", COR)], 1.0),
                     ("s09.c", "s09.d", [(m, SAI), ("^1", ENT)], [("= f{1}{2}", COR)], 0.8),
                     ("s09.d", "s09.e", [(m, SAI), ("^2", ENT), (" = f{1}{2} · f{1}{2}", SAI)], [("= f{1}{4}", COR)], 0.8),
                     ("s09.e", "s10", [(m, SAI), ("^3", ENT)], [("= f{1}{8}", COR)], 0.8),
                     ("s10.a", "s10.c", [(m, SAI), ("^{−1}", ENT), (" = 1 ÷ f{1}{2}", SAI)], [("= 1 · 2 = 2", COR)], C["s10.b"] - C["s10.a"]),
                     ("s10.c", None, [(m, SAI), ("^{−2}", ENT), (" = 2 · 2", SAI)], [("= 4", COR)], 1.0)], size=116)
    E.saida(c, t, C["s10.a"] - 0.1, lambda: (
        E.frase(c, t, C["s10"], [("e", "i", 66), ("com", "i", 66), ("x", "g", 72, ENT), ("negativo?", "g", 66, ENT)], 880, 340),
        E.frase(c, t, C["s10"] + 1.6, [("vira", "i", 60), ("fração", "g", 60, COR), ("com", "i", 60), ("1", "g", 60), ("em", "i", 60), ("cima", "i", 60)], 880, 460)))


# ---------------- gráficos ----------------
def pontos(c, t, t0, f, cor, passo=0.25, r=15):
    for i, xv in enumerate(XS):
        E.ponto(c, t, t0 + passo * i, P, xv, f(xv), cor=cor, r=r)


def degraus(c, t, t0, rot, cor, sentido=1, dt=0.6):
    """escada na lateral da tabela: das linhas x = 0 até x = 3"""
    ry = lambda i: TY + 10 + TL * i + TL / 2
    X = TX + 2 * TW + 14
    pts = [(X, ry(i)) for i in (2, 3, 4, 5)]
    escada(c, t, [t0 + dt * i for i in range(3)], pts, 42, rot, cor=cor)


def tabela_peq(c, t, t0, vals, base, luz=None):
    tabela(c, t, TX, TY, XS, [(lei(base, nome=False), vals, [t0] * 6)], t0, TW, TL, luz=luz)


def b_grafico2(c, t, C, b):
    eixos(c, t, P, C["s07"], C["s07"], C["s07"])
    fx_em(c, t, C["s07"] - 2, lei("2"), XE, 160, 80)

    def tab():
        tabela_peq(c, t, C["s07"] - 2, V2, "2")
        degraus(c, t, C["s07.b"], "×2", COR)
    E.saida(c, t, C["s08.a"] - 0.1, tab)
    pontos(c, t, C["s07"] + 0.6, f2, COR)
    E.ponto(c, t, C["s08.a"] + 2.0, P, -3, 1 / 8, cor=COR, r=15)
    E.curva(c, t, C["s07.a"], P, f2, -3, 3.12, d=1.6, cor=COR)
    q = pulso(t, C["s07.b"], 3.0)
    if q > 0:  # os degraus no gráfico: cada passo para a direita dobra a altura
        for xv in (0, 1, 2, 3):
            M.line(c, P.x(xv), P.oy, P.x(xv), P.y(f2(xv)), COR, 0.35 * q, 10)
    E.saida(c, t, C["s08.a"] - 0.1, lambda: E.foco(c, t, C["s07.c"], 0.5, lambda a: (E.pilula(c, "crescente", 830, 300, 56, "g", a=a),
                                                                                    M.arrow(c, 720, 470, 940, 380, COR, a, 8, 26))))
    if t >= C["s07.d"]:
        anel(c, t, C["s07.d"], *P(0, 1))
        anel(c, t, C["s07.d"] + 0.8, *P(0, 1))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: par(c, "0", "1", *P(-1.4, 1.9), 52, a, "center"))
    E.saida(c, t, C["s08.a"] - 0.1, lambda: fx_em(c, t, C["s07.d"] + 1.2, [("2", SAI), ("^0", ENT), (" = 1", SAI)], 700, 620, 76))
    if t < C["s08"]:
        return
    # para a esquerda: metades
    vals = ("1", "f{1}{2}", "f{1}{4}", "f{1}{8}")
    xs = [230, 430, 630, 830]
    for i, (s, X) in enumerate(zip(vals, xs)):
        E.foco(c, t, C["s08.a"] + 0.7 * i, 0.4, lambda a, s=s, X=X: celula(c, s, X, 380, 80, COR if i else SAI, a))
    escada(c, t, [C["s08.a"] + 0.7 * i + 0.2 for i in range(3)], [(X + 30, 300) for X in xs], 40, "÷2", cor=COR, size=32)
    faixa_eixo(c, P, -3, 0, ep(t, C["s08.b"], 0.5))
    E.frase(c, t, C["s08.b"], ps("cada vez mais perto", "i", 64), XE, 560)
    E.frase(c, t, C["s08.b"] + 1.0, [("do", "i", 64), ("eixo", "i", 64), ("x", "g", 72, ENT)], XE, 650)
    E.frase(c, t, C["s08.c"], [("nunca", "g", 90, COR), ("encosta", "g", 90, COR)], XE, 790)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" > 0", COR)], XE, 950, 110, a))
    E.frase(c, t, C["s08.d"] + 0.8, ps("nunca zero nem negativo", "i", 46, TINTA2), XE + 330, 935)


def b_graficomeio(c, t, C, b):
    eixos(c, t, P, C["s11"] - 2, C["s11"] - 2, C["s11"] - 2)
    m = "(f{1}{2})"
    E.saida(c, t, C["s12"] - 0.1, lambda: fx_em(c, t, C["s11"] - 2, lei(m), XE, 160, 80))

    def tab():
        tabela_peq(c, t, C["s11"] - 2, VM, m)
        degraus(c, t, C["s11.b"], "÷2", TINTA)
    E.saida(c, t, C["s12"] - 0.1, tab)
    pontos(c, t, C["s11"] - 1.5, fm, TINTA, 0.12)
    E.curva(c, t, C["s11.a"], P, fm, -3.12, 3, d=1.4, cor=TINTA)
    q = pulso(t, C["s11.b"], 3.0)
    if q > 0:
        for xv in (0, 1, 2, 3):
            M.line(c, P.x(xv), P.oy, P.x(xv), P.y(fm(xv)), TINTA, 0.3 * q, 10)
    E.saida(c, t, C["s12"] - 0.1, lambda: E.foco(c, t, C["s11.c"], 0.5, lambda a: (
        E.pilula(c, "decrescente", 830, 300, 56, "g", fundo=TINTA, a=a), M.arrow(c, 720, 380, 940, 470, TINTA, a, 8, 26))))
    if t >= C["s11.d"]:
        anel(c, t, C["s11.d"], *P(0, 1), TINTA)
    E.saida(c, t, C["s12"] - 0.1, lambda: E.foco(c, t, C["s11.d"], 0.5, lambda a: par(c, "0", "1", *P(1.4, 1.9), 52, a, "center")))
    faixa_eixo(c, P, 0, 3, ep(t, C["s11.d"] + 2.6, 0.5) * (1 - ep(t, C["s12"], 0.5)), TINTA)
    if t < C["s12"]:
        return
    # quem decide é a base
    E.curva(c, t, C["s12.a"], P, f2, -3, 3.12, d=1.0, cor=COR)
    E.frase(c, t, C["s12"], [("quem", "i", 84), ("decide", "i", 84), ("é", "i", 84), ("a", "i", 84), ("base", "g", 96)], XE, 260)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: fx(c, [("base > 1", COR)], XE, 470, 100, a))
    E.frase(c, t, C["s12.a"] + 0.6, [("sobe", "g", 90, COR)], XE + 520, 470)
    E.foco(c, t, C["s12.a"] + 0.8, 0.5, lambda a: M.arrow(c, XE + 760, 480, XE + 860, 400, COR, a, 8, 24))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: fx(c, [("0 < base < 1", TINTA)], XE, 680, 100, a))
    E.frase(c, t, C["s12.b"] + 0.6, [("desce", "g", 90)], XE + 30, 810)
    E.foco(c, t, C["s12.b"] + 0.8, 0.5, lambda a: M.arrow(c, XE + 330, 740, XE + 430, 820, TINTA, a, 8, 24))
    for k, f, cor, em in (("s12.a", f2, COR, (2.2, 7.2)), ("s12.b", fm, TINTA, (-2.2, 7.2))):
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, f=f, cor=cor, em=em: fx(c, [("2" if f is f2 else m, cor), ("^x", ENT)], *P(*em), 60, a, "center"))


# ---------------- por que a base é positiva e diferente de 1 ----------------
def lagrange(pts):
    def f(x):
        s = 0.0
        for i, (xi, yi) in enumerate(pts):
            p = yi
            for j, (xj, _) in enumerate(pts):
                if j != i:
                    p *= (x - xj) / (xi - xj)
            s += p
        return s
    return f


def b_base(c, t, C, b):
    def s13():
        eixos(c, t, P, C["s13"], C["s13"], C["s13"])
        E.frase(c, t, C["s13.a"], [("e", "i", 90), ("base", "g", 100), ("1?", "g", 110, COR)], XE, 300)
        E.foco(c, t, C["s13.a"] + 1.4, 0.5, lambda a: fx(c, [("1", SAI), ("^x", ENT), (" = 1", SAI)], XE, 470, 120, a))
        E.frase(c, t, C["s13.a"] + 2.4, ps("sempre", "i", 60, TINTA2), XE + 500, 450)
        E.curva(c, t, C["s13.b"], P, lambda x: 1, -3, 3, d=1.0, cor=COR, rotulo="y = 1", em=(2.0, 1.8))
        E.frase(c, t, C["s13.b"], [("reta", "g", 84), ("deitada", "g", 84)], XE, 640)
        E.frase(c, t, C["s13.b"] + 2.2, ps("não sobe nem desce", "i", 64), XE, 770)
        E.frase(c, t, C["s13.b"] + 3.6, [("não", "g", 76, ERRADO), ("é", "i", 72), ("exponencial", "g", 76, ERRADO)], XE, 890)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if C["s14"] <= t:
        def s14():
            eixos(c, t, P2, C["s14"], C["s14"], C["s14"], passo_y=2)
            E.frase(c, t, C["s14"], [("e", "i", 90), ("base", "g", 100), ("negativa?", "g", 100, COR)], XE, 260)
            E.foco(c, t, C["s14.a"], 0.5, lambda a: fx(c, [("(−2)", SAI), ("^{1/2}", ENT)], XE, 420, 110, a))
            E.foco(c, t, C["s14.b"], 0.5, lambda a: fx(c, [("= r{−2}", ERRADO)], XE + 330, 420, 110, a))
            E.frase(c, t, C["s14.b"] + 1.0, ps("não está na reta", "i", 52, ERRADO), XE + 330, 510)
            pts = [(1, -2), (2, 4), (3, -8)]
            for i, (xv, yv) in enumerate(pts):
                ti = C["s14.c"] + 0.9 * i
                E.foco(c, t, ti, 0.5, lambda a, xv=xv, yv=yv, i=i: fx(c, [("(−2)", SAI), (f"^{xv}", ENT), (f" = {E._num(yv)}", ERRADO)],
                                                                    XE, 650 + 110 * i, 84, a))
                E.ponto(c, t, ti, P2, xv, yv, cor=ERRADO, r=16)
                if i:
                    (x0, y0), (x1, y1) = P2(*pts[i - 1]), P2(xv, yv)
                    M.line(c, x0, y0, x1, y1, ERRADO, 0.7, 5, dash=E.TRACO, progress=ease_io(prog(t, ti, 0.5)))
            E.foco(c, t, C["s14.c"] + 2.8, 0.5, lambda a: E.pilula(c, "não sai curva", 1660, 400, 50, "g", fundo=ERRADO, a=a))
        E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.foco(c, t, C["s15.a"], 0.5, lambda a: fx(c, [("0", SAI), ("^{−1}", ENT), (" = f{1}{0}", SAI)], W / 2 - 120, 400, 150, a, "center"))
    E.foco(c, t, C["s15.a"] + 1.2, 0.5, lambda a: E.selo(c, W / 2 + 320, 350, 70, False, a))
    E.frase(c, t, C["s15.a"] + 1.4, ps("dividir por zero não existe", "i", 56, TINTA2), W / 2, 540, "center")
    E.frase(c, t, C["s15.b"], [("base", "g", 110), (">", "g", 110, COR), ("0", "g", 110, COR), ("e", "i", 100), ("base", "g", 110),
                               ("≠", "g", 110, COR), ("1", "g", 110, COR)], W / 2, 800, "center")
    E.foco(c, t, C["s15.b"] + 1.4, 0.4, lambda a: E.pilula(c, "positiva e diferente de 1", W / 2, 940, 50, "g", a=a))


# ---------------- erro ----------------
ERRO = lagrange([(-1, -2), (0, 1), (1, 2), (2, 4)])


def b_erro(c, t, C, b):
    eixos(c, t, P3, C["s16"], C["s16"], C["s16"])
    E.frase(c, t, C["s16"], [("o", "i", 76), ("erro:", "i", 76), ("expoente", "g", 72, ENT), ("negativo", "g", 72, ENT)], XE, 250)
    E.frase(c, t, C["s16"] + 1.4, [("→", "g", 72, ERRADO), ("saída", "i", 72), ("negativa", "g", 72, ERRADO)], XE, 350)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: fx(c, [("2", ERRADO), ("^{−1}", ERRADO), (" = −2", ERRADO)], XE, 520, 110, a))
    if t >= C["s17.a"]:
        E.risco(c, XE - 10, 490, XE + 520, 470, t, C["s17.a"], ERRADO, 10)

    def errado():
        E.ponto(c, t, C["s16.a"] + 0.6, P3, -1, -2, cor=ERRADO, r=16)
        E.curva(c, t, C["s16.b"], P3, ERRO, -1.25, 2.3, d=1.4, cor=ERRADO, tracejada=True)
    E.saida(c, t, C["s17.a"] + 0.6, errado)
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^{−1}", ENT), (" = f{1}{2}", CERTO)], XE, 700, 110, a))
    E.frase(c, t, C["s17.a"] + 1.4, ps("positivo", "g", 60, CERTO), XE + 420, 680)
    E.ponto(c, t, C["s17.a"] + 0.4, P3, -1, 0.5, cor=CERTO, r=16)
    E.foco(c, t, C["s17.a"] + 0.6, 0.4, lambda a: par(c, "−1", "f{1}{2}", *P3(-1.9, 1.5), 48, a, "center"))
    E.curva(c, t, C["s17.b"], P3, f2, -3, 3, d=1.2, cor=COR)
    q = ep(t, C["s17.b"] + 0.6, 0.5)
    if q > 0:
        x, y, w, h = P3.caixa
        c.drawRect(skia.Rect.MakeLTRB(x, P3.oy + 4, x + w, y + h), M.paint(ERRADO, 0.10 * q))
        centro(c, "nunca aqui", P3.x(1.5), P3.y(-1.9), 46, "b", ERRADO, q)
    E.frase(c, t, C["s17.b"], [("sempre", "g", 76, COR), ("acima", "i", 72), ("do", "i", 72), ("eixo", "i", 72), ("x", "g", 80, ENT)], XE, 900)


# ---------------- atalho (palco escuro) ----------------
PA = (1120, 200, 680, 680, -3, 3, -1, 5)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s18():
        Pk = E.plano(c, t, C["s18.a"] + 0.4, *PA, escuro=True)
        E.frase(c, t, C["s18"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s18.a"], [("o", "i", 110, BR), ("espelho", "g", 120, BR)], XE + 540, 190)
        # a linha de valores: x, 2^x e (1/2)^x
        cols = [500, 620, 740, 860, 980]
        xs = (-2, -1, 0, 1, 2)
        linhas = (("x", [E._num(v) for v in xs], 420, CLARO, C["s18.b"] - 0.4),
                  ("2^x", ("f{1}{4}", "f{1}{2}", "1", "2", "4"), 560, CLARO, C["s18.b"] - 0.2),
                  ("(f{1}{2})^x", ("4", "2", "1", "f{1}{2}", "f{1}{4}"), 720, BR, C["s18.b"] + 1.2))
        for nome, vals, y, cor, t0 in linhas:
            E.foco(c, t, t0, 0.4, lambda a, nome=nome, y=y, cor=cor: E.formula(c, nome, 400, y + 20, 56, "g", cor, a, "right"))
            for j, (X, s) in enumerate(zip(cols, vals)):
                E.foco(c, t, t0 + 0.08 * j, 0.4, lambda a, X=X, s=s, y=y, cor=cor: celula(c, s, X, y, 56, cor, a), sobe=6)
        E.foco(c, t, C["s18.b"] - 0.4, 0.4, lambda a: M.line(c, 440, 640, 1040, 640, CLARO, 0.3 * a, 2))
        E.foco(c, t, C["s18.b"] + 1.6, 0.4, lambda a: E.pilula(c, "o x com o sinal trocado", 740, 850, 40, "g", fundo=CLARO, cor="#07070F", a=a))
        # o 4 de cada linha
        for k, X, y, cor, xv in (("s18.c", cols[4], 560, CLARO, 2), ("s18.d", cols[0], 720, BR, -2)):
            if t >= C[k]:
                q = ep(t, C[k], 0.4)
                c.drawCircle(X, y, 52, M.paint(cor, q, stroke=5))
            E.ponto(c, t, C[k] + 0.3, Pk, xv, 4, cor=cor, r=16)
        seta_curva(c, t, C["s18.d"] + 0.6, (Pk.x(2) - 20, Pk.y(4) - 20), (Pk.x(-2) + 20, Pk.y(4) - 20), 60, cor=CLARO, escuro=True)
        x, y, w, h = PA[:4]
        q = pulso(t, C["s18.e"], 3.0)
        if q > 0:
            M.line(c, Pk.ox, y - 30, Pk.ox, y + h + 10, CLARO, 0.35 * q, 26)
        E.curva(c, t, C["s18.e"], Pk, f2, -3, 2.32, d=1.0, cor=CLARO, rotulo="2^x", em=(1.3, 4.6))
        E.curva(c, t, C["s18.e"] + 1.0, Pk, fm, -2.32, 3, d=1.0, cor=BR, rotulo="(f{1}{2})^x", em=(-1.3, 4.6))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: fx(c, [("f{1}{2} = 2", BR), ("^{−1}", CLARO)], W / 2, 300, 120, a, "center"))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: fx(c, [("(f{1}{2})", BR), ("^x", CLARO), (" = (2", BR), ("^{−1}", CLARO), (")", BR), ("^x", CLARO),
                                                   (" = 2", BR), ("^{−x}", CLARO)], W / 2, 540, 120, a, "center"))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: (fx(c, [("3  e  f{1}{3}", BR)], 560, 760, 96, a, "right"),
                                             E.pilula(c, "inversos: tem espelho", 960, 735, 50, "g", fundo=CERTO, a=a)))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: (fx(c, [("3  e  f{1}{2}", BR)], 560, 940, 96, a, "right"),
                                             E.pilula(c, "sem espelho: monte a tabela", 1020, 915, 50, "g", fundo=ERRADO, a=a)))


# ---------------- questão ----------------
XQ = (-1, 0, 1, 2)
V3 = ("f{1}{3}", "1", "3", "9")
V3M = ("3", "1", "f{1}{3}", "f{1}{9}")


def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: fx(c, lei("3"), XE, 320, 96, a))
    E.frase(c, t, C["s20.a"] + 1.4, [("x", "g", 64, ENT), ("de", "i", 60), ("−1", "g", 64, ENT), ("até", "i", 60), ("2", "g", 64, ENT)], XE, 420)
    E.frase(c, t, C["s20.b"], [("espelho", "g", 72, COR), ("→", "g", 72)], XE, 560)
    E.foco(c, t, C["s20.b"] + 0.6, 0.5, lambda a: fx(c, lei("(f{1}{3})"), XE + 440, 560, 84, a))
    E.frase(c, t, C["s20.c"], [("qual", "i", 72), ("cresce?", "g", 72, COR), ("qual", "i", 72), ("decresce?", "g", 72)], XE, 690)
    tabela(c, t, 1150, 330, XQ, [(lei("3", nome=False), ("?",) * 4, [C["s20.a"] + 1.6] * 4),
                                 (lei("(f{1}{3})", nome=False), ("?",) * 4, [C["s20.b"] + 1.0] * 4)], C["s20.a"] + 1.2, 190, 110)
    if t >= C["s21"]:
        E.relogio(c, t, C["s21.a"], cx=560, cy=850, r=66)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eixos(c, t, P, C["s22"], C["s22"], C["s22"])
    t1 = [C["s22.a"] + 1.2, C["s22.b"] + 1.0, C["s22.c"] + 0.8, C["s22.d"] + 0.8]
    t2 = [C["s23.a"] + 1.2, C["s23.b"] + 0.8, C["s23.c"] + 0.8, C["s23.d"] + 0.8]
    ks = [C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]]
    k2 = [C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]]

    def luz(i):
        a1 = ep(t, ks[i], 0.3) * (1 - ep(t, (ks[i + 1] if i < 3 else C["s23"]) - 0.2, 0.3))
        a2 = ep(t, k2[i], 0.3) * (1 - ep(t, (k2[i + 1] if i < 3 else C["s23.e"]) - 0.2, 0.3))
        return max(a1, a2)
    tabela(c, t, XE, 300, XQ, [(lei("3", nome=False), V3, t1), (lei("(f{1}{3})", nome=False), V3M, t2)], C["s22"], 190, 110, luz=luz)
    E.foco(c, t, C["s23"], 0.4, lambda a: E.pilula(c, "espelho: troque o sinal do x", XE + 285, 220 - 40, 40, "g", a=a))
    for i, xv in enumerate(XQ):
        E.ponto(c, t, t1[i], P, xv, 3.0 ** xv, cor=COR, r=15)
        E.ponto(c, t, t2[i], P, xv, (1 / 3) ** xv, cor=TINTA, r=15)
    E.curva(c, t, C["s23.e"], P, lambda x: 3.0 ** x, -3, 2.0, d=1.2, cor=COR, rotulo="3^x", em=(1.4, 8.2))
    E.curva(c, t, C["s23.f"], P, lambda x: (1 / 3) ** x, -2.0, 3, d=1.2, cor=TINTA, rotulo="(f{1}{3})^x", em=(-1.6, 8.0))
    E.foco(c, t, C["s23.e"], 0.5, lambda a: (fx(c, [("3 > 1", SAI)], XE, 860, 84, a),
                                             E.pilula(c, "cresce", XE + 400, 832, 54, "g", fundo=CERTO, a=a)))
    E.foco(c, t, C["s23.f"], 0.5, lambda a: (fx(c, [("f{1}{3} < 1", SAI)], XE, 990, 84, a),
                                             E.pilula(c, "decresce", XE + 420, 962, 54, "g", fundo=CERTO, a=a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s24.a", lambda a, y: (E.escreve(c, "o x no expoente:", 400, y, 80, "i", TINTA, a), fx(c, lei("2", nome=False), 900, y, 100, a))),
                 ("s24.b", lambda a, y: (E.frase(c, t, -99, [("base > 1", "g", 72, COR), ("sobe;", "i", 76)], 400, y),
                                         E.frase(c, t, -99, [("0 < base < 1", "g", 72), ("desce", "i", 76)], 1020, y))),
                 ("s24.c", lambda a, y: (E.escreve(c, "passa por", 400, y, 80, "i", TINTA, a), par(c, "0", "1", 760, y, 84, a),
                                         E.escreve(c, "e nunca toca o eixo x", 1040, y, 64, "i", TINTA2, a))))
        for i, (k, fn) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s25"] + 1.0, [("crescimento", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s25"] + 1.4, [("e", "i", 110), ("decaimento", "g", 120, COR)], XE, 540)
    E.foco(c, t, C["s25.a"], 0.5, lambda a: E.pilula(c, "população: +3% ao ano", XE + 330, 680, 50, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s25.b"], 0.5, lambda a: E.pilula(c, "carro: −10% ao ano", XE + 290, 800, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, tabela2=b_tabela2, grafico2=b_grafico2, tabelameio=b_tabelameio,
              graficomeio=b_graficomeio, base=b_base, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
