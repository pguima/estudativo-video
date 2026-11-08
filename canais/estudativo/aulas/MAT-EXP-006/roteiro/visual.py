"""Visual — Estudativo · MAT-EXP-006: equação exponencial com troca de variável.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; contas à esquerda, gráfico à direita quando ajuda.
Nesta aula: o apelido. apelido() põe a caixa pontilhada em volta da potência que se repete (2ˣ) e a etiqueta "= y" embaixo; toda conta
em y sai na cor da matéria (Y); a raiz que não volta é riscada em vermelho com a pílula "descarte"; no gráfico de 3ˣ, a linha y = 3
(verde) corta a curva e a linha y = −1 (vermelha) nunca é tocada."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-006_equacao_exponencial_troca_de_variavel.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quadrado", "apelido", "descarte", "erro", "atalho", "questao", "fim"))
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






# ---------------- equações e o apelido ----------------
def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, op="=", cor_op=SAI):
    """equação com o sinal centrado em xi: esq e dir_ em partes de fx. Devolve (xs, ws) de cada lado"""
    gap = size * 0.28
    wi = E.larg(op, "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, op, xi - wi / 2, y, size, "g", cor_op, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def linha(c, t, t0, partes, x, y, size, align="left"):
    fx_em(c, t, t0, partes, x, y, size, align)


def nota(c, t, t0, txt, x, y, size=46, fundo=None, cor="#FFFFFF"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, cor=cor, a=a), sobe=6)


def apelido(c, t, t0, partes, x, y, size, nome="y", cor=None):
    """caixa pontilhada em volta da potência que se repete (partes de fx) e a etiqueta com o apelido embaixo"""
    w, _, _ = fx(c, partes, 0, 0, size, 0)
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    E.caixa_pontilhada(c, x - size * 0.12, y - size * 1.12, w + size * 0.24, size * 1.38, q, cor or COR, ease_io(q))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, f"= {nome}", x + w / 2, y + size * 0.62, size * 0.42, "g", fundo=cor or COR, a=a), sobe=6)


Y = COR  # o apelido y aparece na cor da matéria, como o atalho que ele é
P2X = lambda s="x": [("2", SAI), ("^" + s, ENT)]
EQ1 = [("4", SAI), ("^x", ENT), (" − 6 · 2", SAI), ("^x", ENT), (" + 8 = 0", SAI)]
P6 = E.Plano(1180, 330, 600, 560, -2, 2, -2, 6)
assert 4 ** 3 == 64 == (2 ** 3) ** 2 and 2 + 4 == 6 and 2 * 4 == 8 and 4 - 12 + 8 == 0 and 16 - 24 + 8 == 0
assert 3 + (-1) == 2 and 3 * (-1) == -3 and 4 ** 4 == 256 and 6 * 2 ** 4 == 96 and 256 - 96 + 8 == 168
assert 2 ** 4 + 2 ** 3 == 24 and 3 * 8 == 24 and 2 ** 5 == 32 and 4 + (-1) == 3 and 4 * (-1) == -4 and 16 - 12 - 4 == 0


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        linha(c, t, C["s01.a"], EQ1, W / 2, 330, 120, "center")
        E.foco(c, t, C["s01.a"] + 2.0, 0.4, lambda a: E.pilula(c, "3 termos", W / 2, 470, 44, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.b"], [("igualar", "i", 70), ("as", "i", 70), ("bases", "i", 70), ("não", "g", 76, ERRADO), ("resolve", "g", 76, ERRADO)],
                W / 2, 620, "center")
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "um apelido", 640, 800, 56, "g", a=a))
        E.foco(c, t, C["s01.c"] + 1.4, 0.5, lambda a: fx(c, [("→  y² − 6y + 8 = 0", Y)], 900, 825, 84, a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("troca", "g", 110, COR), ("de", "i", 100), ("variável", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 3.2, [("sem", "i", 90), ("pular", "g", 96), ("passo", "g", 96)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("2", SAI), ("^x", ENT), (" = 2", SAI), ("^5", ENT), ("  →  x = 5", SAI)], 430, y, 90, a),
                                     E.escreve(c, "igualar as bases", 1180, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, [("y² − 7y + 12 = 0  →  3 e 4", SAI)], 430, y, 76, a),
                                     E.escreve(c, "soma e produto", 1330, y, 56, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("2", SAI), ("^x", ENT), (" > 0", COR)], 430, y, 90, a),
                                     E.escreve(c, "nunca zero nem negativo", 760, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- o quadrado escondido ----------------
def b_quadrado(c, t, C, b):
    S = 100
    E.frase(c, t, C["s04"], [("o", "i", 72), ("segredo", "i", 72), ("está", "i", 72), ("no", "i", 72), ("4", "g", 84, COR)], XE, 200)
    linha(c, t, C["s04.a"], [("4 = 2", SAI), ("^2", ENT)], XE, 360, S)
    linha(c, t, C["s04.b"], [("4", SAI), ("^x", ENT), (" = (2", SAI), ("^2", ENT), (")", SAI), ("^x", ENT)], XE, 520, S)
    linha(c, t, C["s04.c"], [("= 2", SAI), ("^{2x}", ENT)], XE + 150, 670, S)
    nota(c, t, C["s04.c"] + 0.4, "potência de potência: multiplica", 900, 640, 36, fundo=TINTA)
    linha(c, t, C["s05.a"], [("= 2", SAI), ("^{x · 2}", ENT), (" = (2", SAI), ("^x", ENT), (")", SAI), ("^2", ENT)], XE + 150, 820, S)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "4ˣ é o quadrado de 2ˣ", 640, 960, 52, "g", a=a))
    # a conferência, à direita
    E.foco(c, t, C["s06"], 0.4, lambda a: E.pilula(c, "x = 3", 1450, 360, 46, "g", fundo=ENT, a=a))
    linha(c, t, C["s06.a"], [("4", SAI), ("^3", ENT), (" = 64", SAI)], 1300, 520, 84)
    linha(c, t, C["s06.b"], [("2", SAI), ("^3", ENT), (" = 8", SAI)], 1300, 670, 84)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (fx(c, [("8", SAI), ("^2", ENT), (" = 64", CERTO)], 1300, 820, 84, a), E.selo(c, 1720, 790, 36, True, a)))


# ---------------- o apelido ----------------
def b_apelido(c, t, C, b):
    S = 110
    w, xs, ws = fx(c, EQ1, W / 2, 0, S, 0, "center")
    linha(c, t, C["s07"], EQ1, W / 2, 300, S, "center")
    apelido(c, t, C["s07.a"], P2X(), xs[2] + E.larg(" − 6 · ", "g", S) + S * 0.02 * 3, 300, S)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: fx(c, [("4", SAI), ("^x", ENT), (" = (2", SAI), ("^x", ENT), (")", SAI), ("^2", ENT), (" = y²", Y)],
                                               XE, 540, 84, a))
    E.foco(c, t, C["s07.c"], 0.6, lambda a: fx(c, [("y² − 6y + 8 = 0", Y)], W / 2, 720, 120, a, "center"))

    def s08():
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.pilula(c, "soma 6 · produto 8", 1300, 540, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s08.a"] + 2.0, 0.4, lambda a: fx(c, [("1 e 8: soma 9", TINTA2)], 1130, 900, 60, a))
        E.foco(c, t, C["s08.b"], 0.4, lambda a: (fx(c, [("2 e 4: soma 6", CERTO)], 1130, 1000, 60, a), E.selo(c, 1660, 980, 30, True, a)))
    s08()
    E.foco(c, t, C["s08.c"], 0.5, lambda a: fx(c, [("y = 2  ou  y = 4", COR)], XE, 950, 90, a))


# ---------------- a volta para o x ----------------
def b_volta(c, t, C, b):
    E.frase(c, t, C["s09"], [("a", "i", 72), ("pergunta", "i", 72), ("é", "i", 72), ("o", "i", 72), ("x", "g", 84, ENT)], XE, 200)
    E.foco(c, t, C["s09"] + 1.6, 0.4, lambda a: fx(c, [("y = 2  ou  y = 4", COR)], 1000, 200, 64, a))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" = 2  →  ", SAI), ("x = 1", ENT)], XE, 380, 100, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" = 4 = 2", SAI), ("^2", ENT), ("  →  ", SAI), ("x = 2", ENT)], XE, 540, 100, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: (fx(c, [("x = 1:  4 − 12 + 8 = 0", SAI)], XE, 740, 76, a), E.selo(c, 1180, 715, 34, True, a)))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (fx(c, [("x = 2:  16 − 24 + 8 = 0", SAI)], XE, 880, 76, a), E.selo(c, 1180, 855, 34, True, a)))
    E.foco(c, t, C["s10.b"] + 2.6, 0.5, lambda a: E.pilula(c, "x = 1 e x = 2", 1550, 800, 56, "g", fundo=CERTO, a=a))


def b_metodo(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("o", "i", 90), ("método:", "i", 90), ("4", "g", 110, COR), ("passos", "g", 100)], XE, 230)
    for i, (k, txt) in enumerate(zip(("s11.b", "s11.c", "s11.d", "s11.e"), ("ache a potência que se repete", "dê o apelido:",
                                                                            "resolva em y", "volte para o x"))):
        y = 410 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 52, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 60) / 2, y - 8, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(w, "g" if j == 0 else "i", 70) for j, w in enumerate(txt.split())], 400, y)
        if k == "s11.c":
            E.foco(c, t, C[k] + 0.7, 0.4, lambda a, y=y: fx(c, P2X() + [(" = y", Y)], 900, y, 76, a))


# ---------------- a raiz que não volta ----------------
EQ2 = [("9", SAI), ("^x", ENT), (" − 2 · 3", SAI), ("^x", ENT), (" − 3 = 0", SAI)]


def b_descarte(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("às", "i", 66), ("vezes,", "i", 66), ("uma", "i", 66), ("raiz", "g", 72), ("não", "g", 72, ERRADO), ("volta", "g", 72, ERRADO)],
            XE, 190)
    linha(c, t, C["s12.b"], EQ2, XE, 340, 96)
    E.saida(c, t, C["s12.c"] - 1.3, lambda: nota(c, t, C["s12.b"] + 3.4, "9ˣ = (3ˣ)²", 960, 455, 40, fundo=TINTA))
    nota(c, t, C["s12.c"] - 1.2, "3ˣ = y", 960, 455, 40)
    linha(c, t, C["s12.c"], [("y² − 2y − 3 = 0", Y)], XE, 480, 90)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: fx(c, [("y = 3  ou  y = −1", COR)], XE, 620, 84, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (fx(c, [("3", SAI), ("^x", ENT), (" = 3  →  x = 1", CERTO)], XE, 760, 84, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: fx(c, [("3", SAI), ("^x", ENT), (" = −1", ERRADO)], XE, 900, 84, a))
    E.foco(c, t, C["s13.c"] + 1.6, 0.4, lambda a: E.escreve(c, "nunca dá negativo", XE + 420, 895, 50, "i", ERRADO, a))
    if t >= C["s13.d"]:
        E.risco(c, XE - 10, 875, XE + 380, 865, t, C["s13.d"], ERRADO, 10)
    nota(c, t, C["s13.d"], "descarte", XE + 120, 985, 44, fundo=ERRADO)
    E.foco(c, t, C["s13.d"] + 1.4, 0.5, lambda a: E.pilula(c, "resposta: só x = 1", 1500, 1000, 50, "g", fundo=CERTO, a=a))
    # o gráfico de 3^x: corta y = 3, nunca chega em y = −1
    if t >= C["s13.b"] - 0.6:
        eixos(c, t, P6, C["s13.b"] - 0.6, C["s13.b"] - 0.6, C["s13.b"] - 0.6, passo_y=2)
        E.curva(c, t, C["s13.b"] - 0.3, P6, lambda x: 3 ** x, -2, 1.63, d=0.8, cor=COR, rotulo="3^x", em=(1.0, 5.2))
        for yv, cor, t0 in ((3, CERTO, C["s13.b"]), (-1, ERRADO, C["s13.c"])):
            q = ep(t, t0, 0.5)
            if q > 0:
                M.line(c, P6.x(-2), P6.y(yv), P6.x(2), P6.y(yv), cor, 0.9, 5, dash=E.TRACO, progress=q)
        E.ponto(c, t, C["s13.b"] + 0.5, P6, 1, 3, cor=CERTO, r=14)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("o", "i", 72), ("erro:", "i", 72)], XE, 200)
    E.frase(c, t, C["s14.a"], [("parar", "g", 80, ERRADO), ("no", "i", 72), ("y", "g", 84, ERRADO)], XE + 230, 200)
    E.foco(c, t, C["s14"], 0.4, lambda a: fx(c, EQ1, 1150, 200, 52, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: fx(c, [("x = 2  ou  x = 4 ?", ERRADO)], XE, 360, 90, a))
    E.foco(c, t, C["s14.b"] + 2.6, 0.4, lambda a: E.pilula(c, "teste x = 4", 1180, 330, 44, "g", fundo=TINTA, a=a))
    linha(c, t, C["s14.c"], [("4", SAI), ("^4", ENT), (" = 256", SAI)], XE, 520, 80)
    linha(c, t, C["s14.d"], [("6 · 2", SAI), ("^4", ENT), (" = 96", SAI)], XE + 600, 520, 80)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (fx(c, [("256 − 96 + 8 = 168", SAI), ("  ≠ 0", ERRADO)], XE, 690, 90, a),
                                             E.selo(c, 1350, 660, 40, False, a)))
    E.frase(c, t, C["s15.a"] + 3.4, ps("o x = 2 aparece por coincidência; o x = 1 ficou de fora", "i", 50, TINTA2), XE, 820)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "y é o apelido, não a resposta", W / 2, 960, 56, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s16.a"], [("separe", "g", 100, BR), ("a", "i", 90, BR), ("soma", "g", 100, BR), ("do", "i", 90, BR), ("expoente", "i", 90, BR)],
                XE, 360)
        E.foco(c, t, C["s16.b"], 0.5, lambda a: fx(c, [("2", BR), ("^{x+1}", CLARO), (" = 2", BR), ("^x", CLARO), (" · 2", BR), ("^1", CLARO),
                                                       (" = 2 · 2", BR), ("^x", CLARO)], XE, 640, 110, a))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if C["s17"] <= t:
        def s17():
            E.foco(c, t, C["s17.a"], 0.5, lambda a: fx(c, [("2", BR), ("^{x+1}", CLARO), (" + 2", BR), ("^x", CLARO), (" = 24", BR)], XE, 260, 100, a))
            E.foco(c, t, C["s17.b"], 0.5, lambda a: fx(c, [("2y + y = 24", BR)], XE, 460, 100, a))
            E.foco(c, t, C["s17.b"] - 1.4, 0.4, lambda a: E.pilula(c, "2ˣ = y", 1300, 230, 44, "g", fundo=CLARO, cor="#07070F", a=a))
            E.foco(c, t, C["s17.c"], 0.5, lambda a: fx(c, [("3y = 24  →  y = 8", BR)], XE, 640, 100, a))
            E.foco(c, t, C["s17.d"], 0.5, lambda a: fx(c, [("2", BR), ("^x", CLARO), (" = 8 = 2", BR), ("^3", CLARO), ("  →  x = 3", BR)], XE, 840, 110, a))
        E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.foco(c, t, C["s18.a"], 0.5, lambda a: fx(c, [("2", BR), ("^a", CLARO), (" · 2", BR), ("^b", CLARO), (" = 2", BR), ("^{a+b}", CLARO)], XE, 320, 110, a))
    E.frase(c, t, C["s18.a"] + 2.0, ps("e o caminho de volta separa", "i", 60, CLARO), XE, 450)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: (fx(c, [("2", BR), ("^{x+1}", CLARO), (" = 32", BR)], XE, 680, 100, a),
                                             E.escreve(c, "uma potência só", 820, 670, 56, "i", CLARO, a)))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "iguale as bases direto: x + 1 = 5", 820, 880, 54, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
EQ3 = [("4", SAI), ("^x", ENT), (" − 3 · 2", SAI), ("^x", ENT), (" − 4 = 0", SAI)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    linha(c, t, C["s19.a"], EQ3, XE, 480, 120)
    if t >= C["s20"]:
        E.relogio(c, t, C["s20.a"], cx=1500, cy=760, r=110)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s21"], 0.4, lambda a: fx(c, EQ3, XE, 200, 72, a))
    nota(c, t, C["s21.a"], "2ˣ = y", 1150, 175, 40)
    linha(c, t, C["s21.b"], [("y² − 3y − 4 = 0", Y)], XE, 350, 90)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: (fx(c, [("y = 4  ou  y = −1", COR)], XE, 490, 84, a),
                                             E.escreve(c, "produto −4, soma 3", 1050, 485, 50, "i", TINTA2, a)))
    E.foco(c, t, C["s22.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" = 4  →  x = 2", CERTO)], XE, 640, 84, a))
    E.foco(c, t, C["s22.b"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" = −1", ERRADO)], XE, 780, 84, a))
    if t >= C["s22.b"] + 1.0:
        E.risco(c, XE - 10, 755, XE + 380, 745, t, C["s22.b"] + 1.0, ERRADO, 10)
    nota(c, t, C["s22.b"] + 1.0, "descarte", XE + 560, 760, 44, fundo=ERRADO)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: (fx(c, [("x = 2", CERTO)], 1300, 700, 130, a), E.selo(c, 1720, 650, 44, True, a)))
    E.foco(c, t, C["s22.d"], 0.5, lambda a: fx(c, [("16 − 12 − 4 = 0", SAI)], XE, 940, 76, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s23.a", [("apelide", "g", 80, COR), ("a", "i", 76), ("potência", "i", 76), ("que", "i", 76), ("se", "i", 76), ("repete", "i", 76)]),
                 ("s23.b", [("resolva", "g", 80), ("em", "i", 76), ("y", "g", 84, COR)]),
                 ("s23.c", [("volte", "g", 80), ("para", "i", 76), ("o", "i", 76), ("x", "g", 84, ENT), ("e", "i", 76), ("descarte", "g", 80, ERRADO),
                            ("zero", "i", 76), ("ou", "i", 76), ("negativo", "i", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s24"] + 1.0, [("praticando", "g", 120, COR)], XE, 420)
    E.foco(c, t, C["s24.a"], 0.5, lambda a: E.pilula(c, "crescimento e meia-vida", XE + 330, 600, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.pilula(c, "equações exponenciais", XE + 310, 740, 56, "g", a=a))
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quadrado=b_quadrado, apelido=b_apelido, volta=b_volta, metodo=b_metodo,
              descarte=b_descarte, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
