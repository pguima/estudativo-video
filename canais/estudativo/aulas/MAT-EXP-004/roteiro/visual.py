"""Visual — Estudativo · MAT-EXP-004: equação exponencial, igualar as bases.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; plano à direita e texto à esquerda.
Nesta aula (modelo para as equações e inequações da trilha): eqn() alinha cada linha pelo "=" (xi); caixa_base() contorna as duas
bases iguais em índigo; iguala() faz os dois expoentes descerem da linha de cima e virarem a equação de baixo; trilho() mostra os três
passos do método no alto da tela e acende o da vez; selo verde na resposta conferida."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-004_equacao_exponencial_igualar_as_bases.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "metodo", "nove", "erro", "atalho", "questao", "fim"))
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






# ---------------- equações: o "=" alinhado e os expoentes que descem ----------------
def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, cor_igual=SAI):
    """equação com o "=" centrado em xi: esq e dir_ em partes de fx. Devolve (xs, ws) de cada lado, em pixels"""
    gap = size * 0.28
    wi = E.larg("=", "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, "=", xi - wi / 2, y, size, "g", cor_igual, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def eqn_em(c, t, t0, esq, dir_, y, size, xi=W / 2, d=0.5):
    E.foco(c, t, t0, d, lambda a: eqn(c, esq, dir_, y, size, a, xi))


def desce(c, t, t0, s, de, para, cor=None, d=0.9):
    """o expoente sai do lugar (de = (x, y, tamanho)) e desce até a nova linha (para = (x, y, tamanho)); some ao chegar"""
    p = prog(t, t0, d)
    if p <= 0 or p >= 1:
        return
    e = ease_io(p)
    x = lerp(de[0], para[0], e)
    y = lerp(de[1], para[1], e)
    sz = lerp(de[2], para[2], e)
    E.formula(c, s, x, y, sz, "g", cor or ENT, 1.0)


def iguala(c, t, t0, linha_de, size_de, k_esq, k_dir, y_de, esq_novo, dir_novo, y_para, size_para, xi=W / 2, d=0.9):
    """os dois expoentes (pedaço k_esq do lado esquerdo e k_dir do direito) descem e viram a equação esq_novo = dir_novo"""
    (le, ld) = linha_de
    (pe, pd) = eqn(c, esq_novo, dir_novo, y_para, size_para, 0, xi)
    xe0, xd0 = le[0][k_esq] + size_de * 0.02, ld[0][k_dir] + size_de * 0.02
    ye0 = y_de - size_de * 0.42
    txt_e = "".join(s for s, _ in esq_novo)
    txt_d = "".join(s for s, _ in dir_novo)
    desce(c, t, t0, txt_e, (xe0, ye0, size_de * 0.58), (pe[0][0], y_para, size_para), d=d)
    desce(c, t, t0, txt_d, (xd0, ye0, size_de * 0.58), (pd[0][0], y_para, size_para), d=d)
    if t >= t0 + d - 0.05:
        eqn(c, esq_novo, dir_novo, y_para, size_para, 1.0, xi)


def caixa_base(c, lado, k, y, size, a, cor=None):
    """contorno na base (pedaço k) de um lado: mostra que as bases são iguais"""
    if a <= 0:
        return
    xs, ws = lado
    x0, w = xs[k] - size * 0.06, ws[k] + size * 0.06
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - size * 0.82, w, size * 1.0), 16, 16)
    c.drawRRect(r, M.paint(cor or COR, a, stroke=5))


def nota(c, t, t0, txt, x, y, size=46, cor=None, fundo=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, a=a), sobe=6)


assert 2 ** 5 == 32 and 9 ** 1.5 == 27 and 3 ** 3 == 27 and 2 ** -3 == 1 / 8 and 9 ** 3 == 729
assert 4 ** (4 - 1) == 64 and abs(27 ** (2 / 3) - 9) < 1e-9 and 6 ** 2 == 36


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        eqn_em(c, t, C["s01.a"], [("9", SAI), ("^x", ENT)], [("27", SAI)], 330, 150)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (eqn(c, [("9", SAI), ("^1", ENT)], [("9", SAI)], 560, 90, a, 760),
                                                 E.escreve(c, "pouco", 1060, 555, 60, "i", TINTA2, a)))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (eqn(c, [("9", SAI), ("^2", ENT)], [("81", SAI)], 720, 90, a, 760),
                                                 E.escreve(c, "passou direto", 1060, 715, 60, "i", ERRADO, a)))
        E.frase(c, t, C["s01.c"] + 2.6, ps("nenhum inteiro serve", "i", 60, TINTA2), XE, 880)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "e a resposta sai exata", 1300, 860, 56, "g", a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("o", "i", 100), ("x", "g", 110, ENT), ("no", "i", 100), ("expoente", "g", 110)], XE, 470)
    E.frase(c, t, tb + 3.0, [("tudo", "i", 90), ("na", "i", 90), ("mesma", "g", 100, COR), ("base", "g", 100, COR)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("64 = 2", SAI), ("^6", ENT)], 430, y, 100, a),
                                     E.escreve(c, "número como potência", 900, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, [("(2", SAI), ("^3", ENT), (")", SAI), ("^4", ENT), (" = 2", SAI), ("^{12}", ENT)], 430, y, 100, a),
                                     E.escreve(c, "potência de potência", 900, y, 60, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("2x = 3  →  x = f{3}{2}", SAI)], 430, y, 90, a),
                                     E.escreve(c, "resolver equação", 1080, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- a ideia ----------------
P5 = E.Plano(1120, 170, 680, 740, -1, 6, -4, 36)


def b_ideia(c, t, C, b):
    def s04():
        l1 = eqn(c, [("2", SAI), ("^x", ENT)], [("32", SAI)], 330, 130, 0)
        eqn_em(c, t, C["s04.a"], [("2", SAI), ("^x", ENT)], [("32", SAI)], 330, 130)
        nota(c, t, C["s04.b"], "32 = 2 · 2 · 2 · 2 · 2 = 2⁵", 1540, 420, 40, fundo=TINTA)
        l2 = eqn(c, [("2", SAI), ("^x", ENT)], [("2", SAI), ("^5", ENT)], 560, 130, 0)
        eqn_em(c, t, C["s04.c"], [("2", SAI), ("^x", ENT)], [("2", SAI), ("^5", ENT)], 560, 130)
        q = ep(t, C["s04.c"] + 1.0, 0.4)
        caixa_base(c, l2[0], 0, 560, 130, q)
        caixa_base(c, l2[1], 0, 560, 130, q)
        nota(c, t, C["s04.c"] + 1.2, "mesma base", W / 2, 640, 44)
        iguala(c, t, C["s04.d"] - 0.6, l2, 130, 1, 1, 560, [("x", ENT)], [("5", ENT)], 840, 130)
        if t >= C["s04.d"] + 0.5:
            E.selo(c, 1240, 800, 46, True, ep(t, C["s04.d"] + 0.5, 0.4))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    eixos(c, t, P5, C["s05"], C["s05"], C["s05"], passo_y=8)
    E.foco(c, t, C["s05"], 0.4, lambda a: fx(c, lei("2"), XE, 190, 80, a))
    E.curva(c, t, C["s05.a"] - 0.8, P5, lambda x: 2 ** x, -1, 5.2, d=1.2, cor=COR)
    E.frase(c, t, C["s05.a"], [("sempre", "i", 76), ("sobe", "g", 84, COR)], XE, 360)
    E.frase(c, t, C["s05.b"], [("cada", "i", 64), ("saída", "g", 66)], XE, 500)
    E.frase(c, t, C["s05.b"] + 0.8, [("←", "g", 66), ("uma", "i", 64), ("entrada", "g", 66, ENT), ("só", "i", 64)], XE, 590)
    q = ep(t, C["s05.b"] + 1.4, 0.6)
    if q > 0:
        M.line(c, P5.x(-1), P5.y(32), P5.x(6), P5.y(32), SAI, 0.8, 4, dash=E.TRACO, progress=q)
    E.ponto(c, t, C["s05.c"] - 0.4, P5, 5, 32, cor=COR, r=16)
    if t >= C["s05.c"]:
        M.line(c, P5.x(5), P5.y(32), P5.x(5), P5.oy, ENT, 0.9, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s05.c"], 0.6)))
    E.foco(c, t, C["s05.c"] + 0.5, 0.4, lambda a: E.pilula(c, "5", P5.x(5), P5.oy + 50, 40, "g", fundo=ENT, a=a))
    E.frase(c, t, C["s05.c"], [("32", "g", 80), ("←", "g", 80), ("5", "g", 90, ENT)], XE, 760)
    E.frase(c, t, C["s05.c"] + 2.4, ps("base entre 0 e 1: sempre desce", "i", 50, TINTA2), XE, 900)
    E.frase(c, t, C["s05.c"] + 3.6, ps("vale o mesmo", "g", 50, TINTA2), XE, 970)


# ---------------- o método ----------------
PASSOS = ("mesma base", "iguale os expoentes", "resolva")


def trilho(c, t, t0, ativos):
    """os três passos no alto da tela; ativos = instante em que cada um acende"""
    x = XE
    for i, (txt, ta) in enumerate(zip(PASSOS, ativos)):
        q = ep(t, ta, 0.3) if ta is not None else 0
        rot = f"{i + 1}  {txt}"
        w = E.larg(rot, "g", 40) + 44

        def d(a, x=x, rot=rot, q=q, w=w):
            E.pilula(c, rot, x + w / 2, 150, 40, "g", fundo=E.mix(FIO, COR, q), cor=E.mix(TINTA2, BR, q), a=a)
        E.foco(c, t, t0, 0.4, d)
        x += w + 30


def b_metodo(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], [("o", "i", 90), ("método:", "i", 90), ("3", "g", 110, COR), ("passos", "g", 100)], XE, 260)
        for i, (k, txt) in enumerate(zip(("s06.b", "s06.c", "s06.d"), ("escreva cada lado na mesma base", "iguale os expoentes",
                                                                       "resolva a equação que sobrou"))):
            y = 470 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(w, "g" if j == 0 else "i", 72) for j, w in enumerate(txt.split())], 400, y)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    trilho(c, t, C["s07"], (C["s07.b"], C["s07.c"], C["s07.d"]))
    eqn_em(c, t, C["s07.a"], [("2", SAI), ("^{x+1}", ENT)], [("32", SAI)], 320, 110)
    l2 = eqn(c, [("2", SAI), ("^{x+1}", ENT)], [("2", SAI), ("^5", ENT)], 490, 110, 0)
    eqn_em(c, t, C["s07.b"], [("2", SAI), ("^{x+1}", ENT)], [("2", SAI), ("^5", ENT)], 490, 110)
    q = ep(t, C["s07.b"] + 0.8, 0.4)
    caixa_base(c, l2[0], 0, 490, 110, q)
    caixa_base(c, l2[1], 0, 490, 110, q)
    iguala(c, t, C["s07.c"], l2, 110, 1, 1, 490, [("x + 1", ENT)], [("5", ENT)], 660, 100)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: eqn(c, [("x", ENT)], [("5 − 1 = 4", COR)], 820, 100, a))
    E.foco(c, t, C["s07.e"], 0.5, lambda a: (fx(c, [("conferindo: 2", SAI), ("^{4+1}", ENT), (" = 2", SAI), ("^5", ENT), (" = 32", CERTO)], W / 2, 990, 64, a, "center"),
                                             E.selo(c, 1520, 970, 34, True, a)))


# ---------------- nove elevado a x ----------------
XI = 760


def b_nove(c, t, C, b):
    l1 = eqn(c, [("9", SAI), ("^x", ENT)], [("27", SAI)], 260, 120, 0, XI)
    eqn_em(c, t, C["s08.a"], [("9", SAI), ("^x", ENT)], [("27", SAI)], 260, 120, XI)

    def s08():
        E.frase(c, t, C["s08.a"] + 1.4, ps("27 não é potência inteira de 9", "i", 54, TINTA2), XE, 880)
        nota(c, t, C["s08.b"], "base 3", 1500, 230, 60)
        x9 = l1[0][0][0] + l1[0][1][0] / 2
        x27 = l1[1][0][0] + l1[1][1][0] / 2
        for k, X, txt in (("s08.c", x9, "3^2"), ("s08.d", x27, "3^3")):
            E.foco(c, t, C[k], 0.5, lambda a, X=X, txt=txt: (M.arrow(c, X, 290, X, 500, COR, a, 5, 18),
                                                            fx(c, [("3", SAI), (txt[1:], ENT)], X, 600, 90, a, "center")))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.saida(c, t, C["s09.b"] - 0.1, lambda: eqn_em(c, t, C["s09.a"], [("(3", SAI), ("^2", ENT), (")", SAI), ("^x", ENT)],
                                                   [("3", SAI), ("^3", ENT)], 430, 110, XI))
    l2 = eqn(c, [("3", SAI), ("^{2x}", ENT)], [("3", SAI), ("^3", ENT)], 430, 110, 0, XI)
    eqn_em(c, t, C["s09.b"], [("3", SAI), ("^{2x}", ENT)], [("3", SAI), ("^3", ENT)], 430, 110, XI)
    nota(c, t, C["s09.b"] + 0.3, "expoentes se multiplicam", 1500, 400, 40, fundo=TINTA)
    q = ep(t, C["s09.c"], 0.4)
    caixa_base(c, l2[0], 0, 430, 110, q)
    caixa_base(c, l2[1], 0, 430, 110, q)
    iguala(c, t, C["s09.d"] - 0.4, l2, 110, 1, 1, 430, [("2x", ENT)], [("3", ENT)], 610, 110, XI)
    E.foco(c, t, C["s09.e"], 0.5, lambda a: eqn(c, [("x", ENT)], [("f{3}{2} = 1,5", COR)], 800, 110, a, XI))
    # a conferência, à direita
    E.foco(c, t, C["s10"], 0.5, lambda a: fx(c, [("9", SAI), ("^{3/2}", ENT)], 1300, 640, 90, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: fx(c, [("r{9} = 3", SAI)], 1300, 780, 76, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (fx(c, [("3", SAI), ("^3", ENT), (" = 27", CERTO)], 1300, 910, 76, a),
                                             E.selo(c, 1700, 885, 40, True, a)))


# ---------------- fração do outro lado ----------------
def b_fracao(c, t, C, b):
    E.frase(c, t, C["s11"], ps("e se o outro lado for fração?", "i", 70), XE, 210)
    eqn_em(c, t, C["s11.a"], [("2", SAI), ("^x", ENT)], [("f{1}{8}", SAI)], 400, 120)
    E.foco(c, t, C["s11.a"] + 1.6, 0.5, lambda a: fx(c, [("f{1}{8} = f{1}{2^3}", SAI)], 1350, 400, 90, a))
    l2 = eqn(c, [("2", SAI), ("^x", ENT)], [("2", SAI), ("^{−3}", ENT)], 620, 120, 0)
    eqn_em(c, t, C["s11.b"], [("2", SAI), ("^x", ENT)], [("2", SAI), ("^{−3}", ENT)], 620, 120)
    iguala(c, t, C["s11.c"] - 0.6, l2, 120, 1, 1, 620, [("x", ENT)], [("−3", ENT)], 860, 120)
    if t >= C["s11.c"] + 0.4:
        E.selo(c, 1300, 820, 46, True, ep(t, C["s11.c"] + 0.4, 0.4))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("o", "i", 76), ("erro:", "i", 76)], XE, 220)
    E.frase(c, t, C["s12.a"], [("dividir", "g", 84, ERRADO), ("os", "i", 76), ("números", "g", 84, ERRADO)], XE + 260, 220)
    eqn_em(c, t, C["s12.a"] + 1.2, [("9", SAI), ("^x", ENT)], [("27", SAI)], 400, 110)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: fx(c, [("27 ÷ 9 = 3", ERRADO)], XE, 580, 96, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: fx(c, [("x = 3", ERRADO)], 900, 580, 96, a))
    if t >= C["s13.a"]:
        E.risco(c, XE - 10, 555, 1200, 540, t, C["s13.a"], ERRADO, 10)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: fx(c, [("9", SAI), ("^3", ENT), (" = 729", ERRADO), ("  ≠ 27", SAI)], XE, 760, 96, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "só sai igualando as bases", 1300, 920, 56, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s14.a"], [("desça", "i", 110, BR), ("até", "i", 110, BR), ("o", "i", 110, BR), ("primo", "g", 120, BR)], XE + 540, 190)
        linhas = (("9 = 3 · 3", 0), ("27 = 3 · 3 · 3", 1.0), ("4 = 2 · 2", 3.6), ("32 = 2 · 2 · 2 · 2 · 2", 4.6))
        for i, (s, dt) in enumerate(linhas):
            y = 390 + 130 * i
            E.foco(c, t, C["s14.b"] + dt, 0.5, lambda a, s=s, y=y: fx(c, [(s, BR)], XE, y, 76, a))
        for k, (y, rot) in enumerate(((455, "primo 3"), (715, "primo 2"))):
            E.foco(c, t, C["s14.b"] + (1.6 if k == 0 else 5.2), 0.4, lambda a, y=y, rot=rot: E.pilula(c, rot, 1300, y - 25, 50, "g", fundo=CLARO,
                                                                                                    cor="#07070F", a=a))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "um primo só = a base", 1300, 950, 56, "g", fundo=BR, cor="#07070F", a=a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return

    def s15():
        E.frase(c, t, C["s15.a"], ps("a fatoração mostra de que a base é feita", "i", 64, CLARO), XE, 220)
        E.foco(c, t, C["s15.b"], 0.5, lambda a: fx(c, [("6 = 2 · 3", BR)], XE, 400, 84, a))
        E.foco(c, t, C["s15.b"] + 1.8, 0.5, lambda a: fx(c, [("36 = 2 · 2 · 3 · 3 = 6", BR), ("^2", CLARO)], XE + 520, 400, 84, a))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: eqn(c, [("2", BR), ("^x", CLARO)], [("10", BR)], 640, 100, a, 560, BR))
        E.foco(c, t, C["s15.c"] + 1.6, 0.5, lambda a: (fx(c, [("10 = 2 · ", BR), ("5", ERRADO)], 900, 640, 84, a),
                                                       c.drawCircle(900 + fx(c, [("10 = 2 · ", BR)], 0, 0, 84, 0)[0] + 28, 610, 56,
                                                                    M.paint(ERRADO, a, stroke=5))))
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "pede logaritmo: outra aula", W / 2, 860, 56, "g", fundo=CLARO, cor="#07070F", a=a))
    s15()


# ---------------- questão e resposta ----------------
XA_, XB_ = 520, 1420


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.escreve(c, "1)", XE, 460, 76, "g", COR, a),
                                             eqn(c, [("4", SAI), ("^{x−1}", ENT)], [("64", SAI)], 460, 130, a, 700)))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.escreve(c, "2)", XE, 720, 76, "g", COR, a),
                                             eqn(c, [("27", SAI), ("^x", ENT)], [("9", SAI)], 720, 130, a, 700)))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=560, r=110)


def b_resposta(c, t, C, b):
    S = 72
    E.foco(c, t, C["s18"], 0.4, lambda a: (E.escreve(c, "1)", 90, 230, 60, "g", COR, a),
                                           eqn(c, [("4", SAI), ("^{x−1}", ENT)], [("64", SAI)], 230, S, a, XA_)))
    nota(c, t, C["s18"] + 1.0, "primo 2", XA_, 120, 38, fundo=TINTA)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: eqn(c, [("(2", SAI), ("^2", ENT), (")", SAI), ("^{x−1}", ENT)], [("2", SAI), ("^6", ENT)], 370, S, a, XA_))
    l3 = eqn(c, [("2", SAI), ("^{2(x−1)}", ENT)], [("2", SAI), ("^6", ENT)], 510, S, 0, XA_)
    eqn_em(c, t, C["s18.b"], [("2", SAI), ("^{2(x−1)}", ENT)], [("2", SAI), ("^6", ENT)], 510, S, XA_)
    iguala(c, t, C["s18.b"] + 3.6, l3, S, 1, 1, 510, [("2(x − 1)", ENT)], [("6", ENT)], 650, S, XA_)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: eqn(c, [("x − 1", ENT)], [("3", SAI)], 790, S, a, XA_))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: (eqn(c, [("x", ENT)], [("4", CERTO)], 930, S + 10, a, XA_), E.selo(c, XA_ + 200, 905, 34, True, a)))
    nota(c, t, C["s19.a"], "atalho: 64 = 4³  →  x − 1 = 3", XA_, 1030, 36)
    # a segunda
    E.foco(c, t, C["s20"], 0.4, lambda a: (E.escreve(c, "2)", 990, 230, 60, "g", COR, a),
                                           eqn(c, [("27", SAI), ("^x", ENT)], [("9", SAI)], 230, S, a, XB_)))
    nota(c, t, C["s20"] + 1.0, "primo 3", XB_, 120, 38, fundo=TINTA)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: eqn(c, [("(3", SAI), ("^3", ENT), (")", SAI), ("^x", ENT)], [("3", SAI), ("^2", ENT)], 370, S, a, XB_))
    l3b = eqn(c, [("3", SAI), ("^{3x}", ENT)], [("3", SAI), ("^2", ENT)], 510, S, 0, XB_)
    eqn_em(c, t, C["s20.b"], [("3", SAI), ("^{3x}", ENT)], [("3", SAI), ("^2", ENT)], 510, S, XB_)
    iguala(c, t, C["s20.c"] - 0.4, l3b, S, 1, 1, 510, [("3x", ENT)], [("2", ENT)], 650, S, XB_)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: (eqn(c, [("x", ENT)], [("f{2}{3}", CERTO)], 800, S + 10, a, XB_), E.selo(c, XB_ + 200, 775, 34, True, a)))
    E.foco(c, t, C["s20.e"], 0.5, lambda a: fx(c, [("r3{27} = 3,  3", SAI), ("^2", ENT), (" = 9", CERTO)], XB_ - 260, 960, 60, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        for i, (k, txt) in enumerate(zip(("s21.a", "s21.b", "s21.c"), ("mesma base dos dois lados", "expoentes iguais",
                                                                       "resolva a equação que sobra"))):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(w, "g" if j < 2 else "i", 80) for j, w in enumerate(txt.split())], 400, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s22"] + 1.2, [("inequação", "g", 120, COR), ("exponencial", "g", 120, COR)], XE, 420)
    E.foco(c, t, C["s22.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" > 8", SAI)], XE, 610, 100, a))
    E.foco(c, t, C["s22.a"] + 1.6, 0.5, lambda a: fx(c, [("(f{1}{2})", SAI), ("^x", ENT), (" > 8", SAI)], XE + 420, 610, 100, a))
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "quando o sinal vira?", XE + 300, 800, 54, "g", a=a))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, metodo=b_metodo, nove=b_nove, fracao=b_fracao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
