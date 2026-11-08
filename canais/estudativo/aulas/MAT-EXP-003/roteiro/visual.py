"""Visual — Estudativo · MAT-EXP-003: tempo de duplicação e meia-vida.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, t, expoente e entrada em índigo (ENT); saída e base
em preto (SAI); fx() pinta só o expoente de índigo ("_0" = índice embaixo, como em Q zero); plano à direita e texto/tabela à esquerda;
escada de setas curvas com "×2" ou "÷2" ao lado da tabela ou por cima de uma linha de valores (saltos()).
Nesta aula: barra do remédio (dose()) no gancho; tabela t | mg com a escada ÷2 e o plano horas x mg; linha de dobras da colônia;
a fórmula Q = Q₀ · 2^(t/T) com o expoente t/T em índigo e a caixa pontilhada marcando "quantas vezes dobrou"."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / t / expoente / entrada · y / saída / base
ARQUIVO_FINAL = "estudativo_MAT-EXP-003_tempo_de_duplicacao_e_meia_vida.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("meiavida", "dobra", "formula", "atalho", "questao", "fim"))
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






def linha_valores(c, t, xs, vals, ts, y, size=70, cor=TINTA):
    """valores lado a lado, cada um no seu instante"""
    for X, s, t0 in zip(xs, vals, ts):
        E.foco(c, t, t0, 0.4, lambda a, X=X, s=s: E.formula(c, s, X, y, size, "g", cor, a, "center"), sobe=6)


def saltos(c, t, xs, y, rots, ts, cor=None, size=34, bojo=46, folga=20):
    """setas curvas por cima de uma linha de valores, cada uma com a sua pílula"""
    for i, (rot, t0) in enumerate(zip(rots, ts)):
        seta_curva(c, t, t0, (xs[i] + folga, y), (xs[i + 1] - folga, y), bojo, rot, cor=cor, size=size)


# ---------------- números desta aula ----------------
PQ = E.Plano(1080, 150, 720, 780, 0, 24, 0, 80)     # remédio: horas x miligramas
remedio = lambda h: 80 * 0.5 ** (h / 6)
assert [remedio(h) for h in (0, 6, 12, 18)] == [80, 40, 20, 10] and 80 * 0.5 ** 3 == 10
assert 500 * 2 ** 3 == 4000 and 120 / 20 == 6 and 500 * 2 ** 6 == 32000 and 18 / 6 == 3
assert 200 / 20 == 10 and 500 * 2 ** 10 == 512000 and 2 ** 10 == 1024
assert 160 * 0.5 ** 4 == 10 and 160 / 2 ** 5 == 5 and 5 * 5 == 25
LEI2 = [("Q = Q", SAI), ("_0", SAI), (" · 2", SAI), ("^{t/T}", ENT)]
LEIM = [("Q = Q", SAI), ("_0", SAI), (" · ", SAI), ("(f{1}{2})", COR), ("^{t/T}", ENT)]


def dose(c, x, y, mg, a=1.0, cor=None, escala=11, h=64):
    """barra do remédio: comprimento proporcional aos miligramas"""
    if a <= 0 or mg <= 0:
        return
    M.rrect(c, x, y - h / 2, mg * escala, h, 14, cor or COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    X0, Y0 = XE, 520

    def cena():
        E.frase(c, t, C["s01.a"], [("80", "g", 120, COR), ("mg", "i", 90)], XE, 300)
        E.frase(c, t, C["s01.b"], [("a", "i", 66), ("cada", "i", 66), ("6", "g", 72), ("horas:", "i", 66), ("metade", "g", 72, COR),
                                   ("sai", "i", 66)], 760, 300)
        # o jeito errado: tira 40, tira 40
        mg = 80 - 40 * ease_io(prog(t, C["s01.c"] + 0.3, 0.6)) - 40 * ease_io(prog(t, C["s01.c"] + 1.4, 0.6))
        dose(c, X0, Y0, mg, ep(t, C["s01.a"], 0.5), ERRADO if t >= C["s01.c"] else COR)
        E.foco(c, t, C["s01.c"], 0.4, lambda a: fx(c, [("80 − 40 − 40 = 0", ERRADO)], XE, 700, 84, a))
        E.frase(c, t, C["s01.d"], [("12", "g", 90, ERRADO), ("h:", "i", 84), ("acabou?", "g", 96, ERRADO)], XE, 880)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return

    def cena2():
        E.frase(c, t, C["s02"], ps("mas, de verdade:", "i", 72), XE, 230)
        for i, (mg, h, t0) in enumerate(((80, "0 h", C["s02"]), (40, "6 h", C["s02"] + 0.8), (20, "12 h", C["s02.a"]))):
            y = 380 + 170 * i
            E.foco(c, t, t0, 0.5, lambda a, mg=mg, h=h, y=y, i=i: (
                E.escreve(c, h, XE, y + 20, 56, "b", TINTA2, a), dose(c, XE + 200, y, mg, a, CERTO if i == 2 else COR),
                E.escreve(c, f"{mg} mg", XE + 230 + mg * 11, y + 22, 64, "g", CERTO if i == 2 else TINTA, a)))
    E.saida(c, t, C["s02.b"] - 0.1, cena2)
    if t < C["s02.b"]:
        return
    tb, te = C["s02.b"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("quanto", "i", 100), ("resta", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 2.2, [("quanto", "i", 100), ("cresce", "g", 110, COR)], XE, 620)
    E.frase(c, t, tb + 3.2, [("metades", "g", 80), ("e", "i", 76), ("dobras", "g", 80)], XE, 790)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("uma", "i", 84, TINTA, C["s03"] + 0.6), ("coisa", "g", 80, COR, C["s03"] + 0.8)], W / 2, 260, "center")
    E.frase(c, t, C["s03.a"], [("o", "i", 90), ("crescimento", "i", 90), ("que", "i", 90), ("multiplica", "g", 96, COR)], W / 2, 520, "center")
    E.foco(c, t, C["s03.b"], 0.5, lambda a: fx(c, [("Q = Q", SAI), ("_0", SAI), (" · fator", COR), ("^t", ENT)], W / 2, 760, 140, a, "center"))


# ---------------- meia-vida ----------------
TQ = (0, 6, 12, 18)
VQ = ("80", "40", "20", "10")


def b_meiavida(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("cair", "i", 96), ("pela", "i", 96), ("metade", "g", 100)], W / 2, 330, "center")
        E.frase(c, t, C["s04.b"], [("meia-vida", "g", 200, COR)], W / 2, 600, "center")
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "remédio: 6 horas", W / 2, 800, 70, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return

    def s05():
        eixos(c, t, PQ, C["s05"], C["s05"], C["s05"], passo_x=6, passo_y=20, nomes=("t (h)", "mg"))
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "metade do que sobrou", 500, 200, 50, "g", a=a))
        tv = [C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]]
        tabela(c, t, XE, 380, TQ, [([("mg", SAI)], VQ, tv)], C["s05.a"] + 0.6, 170, 104, nome_x="t (h)")
        ry = lambda i: 380 + 10 + 104 * i + 52
        escada(c, t, [tv[1] - 0.4, tv[2] - 0.4, tv[3] - 0.4], [(XE + 340 + 14, ry(i)) for i in range(4)], 42, "÷2", cor=COR)
        for i, h in enumerate(TQ):
            E.ponto(c, t, tv[i], PQ, h, remedio(h), cor=COR, r=15)
        E.curva(c, t, C["s05.e"] + 1.2, PQ, remedio, 0, 24, d=1.2, cor=COR)
        if t >= C["s05.e"] + 2.4:
            anel(c, t, C["s05.e"] + 2.4, *PQ(12, 20), CERTO)
            anel(c, t, C["s05.e"] + 3.2, *PQ(12, 20), CERTO)
        E.foco(c, t, C["s05.e"] + 2.4, 0.4, lambda a: E.pilula(c, "12 h: 20 mg, não zero", 760, 900, 44, "g", fundo=CERTO, a=a))
        faixa_eixo(c, PQ, 0, 24, ep(t, C["s05.e"] + 4.6, 0.5))
        E.foco(c, t, C["s05.e"] + 4.6, 0.4, lambda a: (centro(c, "nunca chega a zero", PQ.x(16), PQ.y(30), 44, "b", COR, a),
                                                       M.arrow(c, PQ.x(17), PQ.y(27), PQ.x(21), PQ.y(6), COR, a, 5, 18)))
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("em conta", "i", 72), XE, 220)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: (E.escreve(c, "cada meia-vida:", XE, 380, 70, "i", TINTA, a),
                                             fx(c, [("× f{1}{2}", COR)], XE + 560, 380, 96, a)))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: fx(c, [("80 · ", SAI), ("(f{1}{2})", COR), ("^3", ENT)], XE, 600, 120, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: fx(c, [("= 80 · f{1}{8}", SAI)], XE + 560, 600, 120, a))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: fx(c, [("= 80 ÷ 8 = 10 mg", COR)], XE + 60, 860, 120, a))


# ---------------- duplicação ----------------
XD = [300, 650, 1000, 1350]


def b_dobra(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("tempo", "g", 90, COR), ("de", "i", 84), ("duplicação", "g", 90, COR)], XE, 230)
    E.frase(c, t, C["s07.a"] + 1.4, ps("o tempo que leva para dobrar", "i", 56, TINTA2), XE, 320)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "500 bactérias", 360, 450, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "dobra a cada 20 min", 900, 450, 50, "g", a=a))
    ts = [C["s07.b"], C["s08.a"] + 0.6, C["s08.a"] + 1.2, C["s08.a"] + 1.8]
    linha_valores(c, t, XD, ["500", "1.000", "2.000", "4.000"], ts, 680, 76)
    linha_valores(c, t, XD, ["0 min", "20 min", "40 min", "60 min"], ts, 750, 40, TINTA2)
    saltos(c, t, XD, 600, ["×2", "×2", "×2"], [x - 0.3 for x in ts[1:]], cor=COR, bojo=48, folga=50)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.pilula(c, "60 ÷ 20 = 3 dobras", 1480, 450, 50, "g", fundo=ENT, a=a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: fx(c, [("500 · 2", SAI), ("^3", ENT)], XE, 930, 96, a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: fx(c, [("= 500 · 8 = 4.000", COR)], XE + 360, 930, 96, a))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    w, xs, ws = fx(c, LEI2, W / 2, 0, 140, 0, "center")
    E.foco(c, t, C["s09.a"], 0.6, lambda a: fx(c, LEI2, W / 2, 290, 140, a, "center"))
    xe = xs[3] + ws[3] / 2

    def s09():
        for k, partes, y in (("s09.b", [("Q", SAI), ("_0", SAI), (": quantidade inicial", TINTA2)], 500),
                             ("s09.c", [("t", ENT), (": tempo que passou", TINTA2)], 610),
                             ("s09.d", [("T", ENT), (": tempo de uma duplicação", TINTA2)], 720)):
            E.foco(c, t, C[k], 0.5, lambda a, partes=partes, y=y: fx(c, partes, 520, y, 60, a, est="b"))
        q = ep(t, C["s09.e"], 0.4)
        if q > 0:
            E.caixa_pontilhada(c, xe - 70, 120, 140, 110, q, COR)
        E.foco(c, t, C["s09.e"] + 0.3, 0.5, lambda a: (M.arrow(c, xe + 150, 352, xe + 20, 250, COR, a, 5, 18),
                                                       E.pilula(c, "quantas vezes dobrou", 1560, 390, 50, "g", a=a)))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t:
        def s10():
            linhas = (("s10.a", [("2 h = 120 min", SAI)]), ("s10.b", [("120 ÷ 20 = 6", SAI)]),
                      ("s10.c", [("2", SAI), ("^6", ENT), (" = 64", SAI)]), ("s10.d", [("500 · 64 = 32.000", COR)]))
            for i, (k, partes) in enumerate(linhas):
                E.foco(c, t, C[k], 0.5, lambda a, partes=partes, i=i: fx(c, partes, 520, 470 + 130 * i, 84, a))
            E.foco(c, t, C["s10.d"] + 0.8, 0.4, lambda a: E.pilula(c, "bactérias", 1400, 830, 46, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11.a"], 0.6, lambda a: fx(c, LEIM, W / 2, 560, 140, a, "center"))
    E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: E.pilula(c, "meia-vida", 330, 520, 46, "g", a=a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: fx(c, [("T", ENT), (" = a meia-vida", TINTA2)], W / 2, 740, 64, a, "center", est="b"))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: fx(c, [("remédio: 18 ÷ 6 = 3 metades", COR)], W / 2, 900, 76, a, "center"))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("o", "i", 76), ("erro:", "i", 76)], XE, 230)
    E.frase(c, t, C["s12.a"], [("misturar", "g", 84, ERRADO), ("unidades", "g", 84, ERRADO)], XE + 260, 230)
    E.foco(c, t, C["s12.a"] + 1.4, 0.5, lambda a: (E.pilula(c, "2 horas", 400, 360, 50, "g", fundo=TINTA, a=a),
                                                   E.pilula(c, "dobra a cada 20 min", 830, 360, 50, "g", fundo=TINTA, a=a)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: fx(c, [("2 ÷ 20 = 0,1", ERRADO)], XE, 540, 110, a))
    E.frase(c, t, C["s12.c"], [("0,1", "g", 84, ERRADO), ("de", "i", 76), ("dobra?", "g", 84, ERRADO)], XE + 760, 540)
    if t >= C["s13"]:
        E.risco(c, XE - 10, 515, XE + 1250, 495, t, C["s13"], ERRADO, 10)
    E.frase(c, t, C["s13.a"], [("mesma", "g", 84, COR), ("unidade", "g", 84, COR)], XE, 720)
    E.foco(c, t, C["s13.a"] + 1.2, 0.5, lambda a: fx(c, [("2 h = 120 min", SAI)], XE + 760, 720, 84, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: fx(c, [("120 ÷ 20 = 6 dobras", CERTO)], XE, 900, 110, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.foco(c, t, C["s14.a"], 0.5, lambda a: fx(c, [("10 dobras ≈ ×1.000", BR)], XE, 340, 120, a))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: fx(c, [("200 min ÷ 20 = 10 dobras", CLARO)], XE, 520, 76, a))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: fx(c, [("500  →  ≈ 500.000", BR)], XE, 650, 90, a))
        E.foco(c, t, C["s14.d"], 0.5, lambda a: fx(c, [("10 meias-vidas ≈ ÷1.000", BR)], XE, 830, 90, a))
        E.foco(c, t, C["s14.d"] + 2.0, 0.5, lambda a: fx(c, [("1.000 mg  →  ≈ 1 mg", CLARO)], XE, 950, 76, a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], ps("por que funciona", "i", 70, CLARO), XE, 220)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: fx(c, [("2", BR), ("^{10}", CLARO), (" = 1.024 ≈ 1.000", BR)], XE, 470, 130, a))
    E.frase(c, t, C["s15.a"] + 4.0, ps("prova pede o valor exato?", "i", 64, CLARO), XE, 700)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: fx(c, [("500 · 1.024 = 512.000", BR)], XE, 860, 110, a))


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16"] + 1.0, ps("material inventado", "i", 52, TINTA2), XE + 520, 200)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.pilula(c, "meia-vida: 5 anos", 470, 360, 56, "g", a=a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "amostra: 160 g", 1120, 360, 56, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s16.c"], [("1)", "g", 76, COR), ("quanto", "i", 76), ("resta", "g", 80), ("em", "i", 76), ("20", "g", 80),
                               ("anos?", "i", 76)], XE, 580)
    E.frase(c, t, C["s16.d"], [("2)", "g", 76, COR), ("quando", "i", 76), ("restam", "i", 76), ("5", "g", 80), ("g?", "g", 80)], XE, 730)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=760, r=80)


XR = [230, 500, 770, 1040, 1310, 1580]


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s18.a"], 0.5, lambda a: fx(c, [("20 ÷ 5 = 4 meias-vidas", SAI)], XE, 230, 72, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: fx(c, [("(f{1}{2})", COR), ("^4", ENT), (" = f{1}{16}", SAI)], XE, 370, 72, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: (fx(c, [("160 ÷ 16 = 10 g", CERTO)], 1000, 370, 72, a),
                                             E.selo(c, 1720, 345, 40, True, a)))
    ts = [C["s19.a"] + 0.5 * i for i in range(6)]
    linha_valores(c, t, XR, ["160", "80", "40", "20", "10", "5"], ts, 650, 76)
    saltos(c, t, XR, 570, ["÷2"] * 5, [x - 0.2 for x in ts[1:]], cor=COR, bojo=40, folga=44)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "5 meias-vidas", 560, 800, 52, "g", a=a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: (fx(c, [("5 · 5 = 25 anos", CERTO)], 960, 825, 84, a),
                                             E.selo(c, 1720, 795, 40, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", lambda a, y: E.frase(c, t, -99, [("tempo", "i", 72), ("÷", "g", 76, COR), ("tempo", "i", 72), ("de", "i", 72),
                                                            ("dobrar", "g", 76), ("ou", "i", 72), ("de", "i", 72), ("cair", "i", 72),
                                                            ("à", "i", 72), ("metade", "g", 76)], 400, y)),
                 ("s20.b", lambda a, y: (E.frase(c, t, -99, [("esse", "i", 76), ("número", "i", 76), ("vai", "i", 76), ("no", "i", 76),
                                                             ("expoente", "g", 84, COR)], 400, y),
                                         fx(c, LEI2, 400, y + 150, 84, a))))
        for i, (k, fn) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21"] + 2.4, [("equação", "g", 120, COR), ("exponencial", "g", 120, COR)], XE, 420)
    E.foco(c, t, C["s21.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^{x+1}", ENT), (" = 32", SAI)], XE, 640, 130, a))
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "tudo na mesma base", XE + 300, 820, 54, "g", a=a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, meiavida=b_meiavida, dobra=b_dobra, formula=b_formula, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
