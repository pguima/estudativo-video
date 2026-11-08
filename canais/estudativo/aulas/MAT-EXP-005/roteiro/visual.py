"""Visual — Estudativo · MAT-EXP-005: inequação exponencial.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; plano à direita e contas à esquerda.
Como em MAT-EXP-004: eqn() alinha cada linha pelo sinal (agora com op = ">", "<", "≥", "≤"), caixa_base()/caixa_frac() contornam as
bases iguais e iguala() faz os expoentes descerem. Nesta aula: quando o sinal vira, ele entra na cor da matéria e ganha um anel;
pinta() mostra a solução na reta (bolinha aberta/fechada e faixa com seta); no gráfico, a linha y = 8 tracejada e a região da curva
acima dela pintada com E.area."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-005_inequacao_exponencial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sobe", "desce", "erro", "atalho", "questao", "fim"))
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






# ---------------- inequações: o sinal alinhado, os expoentes que descem e a reta ----------------
def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, op="=", cor_op=SAI):
    """equação ou inequação com o sinal (op) centrado em xi: esq e dir_ em partes de fx. Devolve (xs, ws) de cada lado"""
    gap = size * 0.28
    wi = E.larg(op, "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, op, xi - wi / 2, y, size, "g", cor_op, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def eqn_em(c, t, t0, esq, dir_, y, size, xi=W / 2, op="=", cor_op=SAI, d=0.5):
    E.foco(c, t, t0, d, lambda a: eqn(c, esq, dir_, y, size, a, xi, op, cor_op))


def desce(c, t, t0, s, de, para, cor=None, d=0.9):
    """o expoente sai do lugar (de = (x, y, tamanho)) e desce até a nova linha (para = (x, y, tamanho)); some ao chegar"""
    p = prog(t, t0, d)
    if p <= 0 or p >= 1:
        return
    e = ease_io(p)
    E.formula(c, s, lerp(de[0], para[0], e), lerp(de[1], para[1], e), lerp(de[2], para[2], e), "g", cor or ENT, 1.0)


def iguala(c, t, t0, linha_de, size_de, k_esq, k_dir, y_de, esq_novo, dir_novo, y_para, size_para, xi=W / 2, d=0.9, op="=", cor_op=SAI):
    """os dois expoentes descem da linha de cima e viram esq_novo (op) dir_novo; com op diferente, o sinal entra na cor cor_op"""
    (le, ld) = linha_de
    (pe, pd) = eqn(c, esq_novo, dir_novo, y_para, size_para, 0, xi, op)
    xe0, xd0 = le[0][k_esq] + size_de * 0.02, ld[0][k_dir] + size_de * 0.02
    ye0 = y_de - size_de * 0.42
    desce(c, t, t0, "".join(s for s, _ in esq_novo), (xe0, ye0, size_de * 0.58), (pe[0][0], y_para, size_para), d=d)
    desce(c, t, t0, "".join(s for s, _ in dir_novo), (xd0, ye0, size_de * 0.58), (pd[0][0], y_para, size_para), d=d)
    if t >= t0 + d - 0.05:
        eqn(c, esq_novo, dir_novo, y_para, size_para, 1.0, xi, op, cor_op)


def caixa_base(c, lado, k, y, size, a, cor=None):
    """contorno na base (pedaço k) de um lado: mostra que as bases são iguais"""
    if a <= 0:
        return
    xs, ws = lado
    x0, w = xs[k] - size * 0.06, ws[k] + size * 0.06
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - size * 0.82, w, size * 1.0), 16, 16)
    c.drawRRect(r, M.paint(cor or COR, a, stroke=5))


def caixa_frac(c, lado, k, y, size, a, cor=None):
    """contorno numa base em fração (dois andares)"""
    if a <= 0:
        return
    xs, ws = lado
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[k] - size * 0.04, y - size * 1.12, ws[k] + size * 0.02, size * 1.62), 16, 16)
    c.drawRRect(r, M.paint(cor or COR, a, stroke=5))


def nota(c, t, t0, txt, x, y, size=46, fundo=None, cor="#FFFFFF"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, cor=cor, a=a), sobe=6)


def pinta(c, t, tb, tp, vx, y, v, lado, fecha, xa, xb, cor=None, r=17):
    """solução na reta: bolinha em v no instante tb (cheia se fecha) e a faixa que pinta para o lado (+1 direita, −1 esquerda) em tp,
    até a ponta da reta (xa..xb, em pixels), com seta"""
    cor = cor or COR
    X = vx(v)
    p = ease_out(prog(t, tp, 0.8))
    if p > 0:
        fim = xb if lado > 0 else xa
        xm = lerp(X, fim, p)
        M.line(c, X, y, xm, y, cor, 1.0, 12, cap_round=False)
        if p > 0.98:
            M.line(c, fim, y, fim - 26 * lado, y - 18, cor, 1.0, 8)
            M.line(c, fim, y, fim - 26 * lado, y + 18, cor, 1.0, 8)
    q = ep(t, tb, 0.3)
    if q > 0:
        k = ease_back(prog(t, tb, 0.45))
        c.drawCircle(X, y, r * k, M.paint(cor if fecha else E.PAPEL, q))
        c.drawCircle(X, y, r * k, M.paint(cor, q, stroke=6))


def reta_sol(c, t, t0, x0, x1, y, vmin, vmax, size=44):
    return E.reta(c, t, t0, x0, x1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=size)


HALF = "(f{1}{2})"
assert 2 ** 3 == 8 and 0.5 ** -3 == 8 and 0.5 ** -4 == 16 and 0.5 ** 0 == 1 and 2 ** -2 == 0.25 and 2 ** 0 == 1
assert 3 ** 3 == 27 and abs(0.2 ** -2 - 25) < 1e-9 and abs((1 / 3) ** 2 - 1 / 9) < 1e-12


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        eqn_em(c, t, C["s01.a"], [(HALF, SAI), ("^x", ENT)], [("8", SAI)], 300, 150, op=">")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (eqn(c, [("x", ERRADO)], [("−3", ERRADO)], 520, 100, a, 560, ">", ERRADO),
                                                 E.escreve(c, "iguala as bases e...", 820, 515, 54, "i", TINTA2, a)))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (fx(c, [("teste x = 0:  ", TINTA2), (HALF, SAI), ("^0", ENT), (" = 1", SAI)], XE, 720, 72, a),
                                                 fx(c, [("1 > 8?  não", ERRADO)], 1100, 720, 72, a)))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (fx(c, [("mas 0 > −3", SAI)], XE, 900, 84, a),
                                                 E.pilula(c, "algo deu errado", 1150, 875, 54, "g", fundo=ERRADO, a=a)))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("inequação", "g", 110), ("exponencial", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 3.6, [("quando", "i", 90), ("o", "i", 90), ("sinal", "g", 100, COR), ("vira", "g", 100, COR)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("2", SAI), ("^x", ENT), (" = 2", SAI), ("^5", ENT), ("  →  x = 5", SAI)], 430, y, 90, a),
                                     E.escreve(c, "igualar as bases", 1180, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (E.escreve(c, "base > 1 sobe", 430, y, 76, "g", COR, a),
                                     E.escreve(c, "0 < base < 1 desce", 980, y, 76, "g", TINTA, a))),
             ("s03.c", lambda a, y: (fx(c, [("x > 3", SAI)], 430, y, 90, a),
                                     E.escreve(c, "inequação, com a bolinha na reta", 800, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- base maior que 1 ----------------
XL = 560                          # o sinal das contas à esquerda
PS = E.Plano(1120, 170, 680, 700, -1, 5, -2, 18)
PD = E.Plano(1120, 170, 680, 700, -5, 1, -2, 18)


def b_sobe(c, t, C, b):
    S = 100
    eqn_em(c, t, C["s04.a"], [("2", SAI), ("^x", ENT)], [("8", SAI)], 260, S, XL, ">")
    nota(c, t, C["s04.b"], "8 = 2³", 900, 230, 44, fundo=TINTA)
    l2 = eqn(c, [("2", SAI), ("^x", ENT)], [("2", SAI), ("^3", ENT)], 430, S, 0, XL, ">")
    eqn_em(c, t, C["s04.c"], [("2", SAI), ("^x", ENT)], [("2", SAI), ("^3", ENT)], 430, S, XL, ">")
    q = ep(t, C["s04.c"] + 0.8, 0.4)
    caixa_base(c, l2[0], 0, 430, S, q)
    caixa_base(c, l2[1], 0, 430, S, q)
    if t < C["s05"]:
        return
    eixos(c, t, PS, C["s05"], C["s05"], C["s05"], passo_y=4)
    E.curva(c, t, C["s05.a"] - 0.6, PS, lambda x: 2 ** x, -1, 4.17, d=1.2, cor=COR, rotulo="2^x", em=(3.3, 15.5))
    nota(c, t, C["s05.a"], "base 2 > 1: sempre sobe", 1460, 960, 40)
    iguala(c, t, C["s05.b"], l2, S, 1, 1, 430, [("x", ENT)], [("3", ENT)], 600, S, XL, op=">")
    nota(c, t, C["s05.b"] + 0.9, "o sinal se mantém", 930, 570, 40, fundo=CERTO)
    vx = reta_sol(c, t, C["s05.c"] - 0.6, 200, 920, 820, 0, 6)
    pinta(c, t, C["s05.c"], C["s05.d"], vx, 820, 3, 1, False, 160, 980)
    E.foco(c, t, C["s05.c"] + 0.8, 0.4, lambda a: fx(c, [("2³ = 8, e 8 não é > 8", TINTA2)], 200, 960, 44, a, est="b"))
    # o gráfico
    q = ep(t, C["s06.a"], 0.6)
    if q > 0:
        M.line(c, PS.x(-1), PS.y(8), PS.x(5), PS.y(8), SAI, 0.8, 4, dash=E.TRACO, progress=q)
        E.foco(c, t, C["s06.a"] + 0.3, 0.3, lambda a: E.escreve(c, "y = 8", PS.x(-0.9), PS.y(8) - 16, 40, "b", SAI, a))
    E.area(c, t, C["s06.b"], PS, lambda x: 2 ** x, 3, 4.17, g=lambda x: 8, alfa=0.3)
    if t >= C["s06.b"]:
        M.line(c, PS.x(3), PS.y(8), PS.x(3), PS.oy, ENT, 0.9, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s06.b"], 0.5)))
        anel(c, t, C["s06.b"], *PS(3, 8))


# ---------------- base entre 0 e 1 ----------------
def b_desce(c, t, C, b):
    S = 96

    def contas():
        eqn_em(c, t, C["s07.a"], [(HALF, SAI), ("^x", ENT)], [("8", SAI)], 260, S, XL, ">")
        E.saida(c, t, C["s08.c"] - 0.1, lambda: nota(c, t, C["s07.b"], "(1/2)⁻³ = 1 ÷ 1/8 = 8", 560, 620, 40, fundo=TINTA))
        l2 = eqn(c, [(HALF, SAI), ("^x", ENT)], [(HALF, SAI), ("^{−3}", ENT)], 450, S, 0, XL, ">")
        eqn_em(c, t, C["s07.c"], [(HALF, SAI), ("^x", ENT)], [(HALF, SAI), ("^{−3}", ENT)], 450, S, XL, ">")
        q = ep(t, C["s07.c"] + 0.8, 0.4)
        caixa_frac(c, l2[0], 0, 450, S, q)
        caixa_frac(c, l2[1], 0, 450, S, q)
        iguala(c, t, C["s08.c"], l2, S, 1, 1, 450, [("x", ENT)], [("−3", ENT)], 640, S, XL, op="<", cor_op=COR)
        nota(c, t, C["s08.c"] + 0.9, "o sinal vira", 900, 610, 40)
        if t >= C["s08.c"] + 0.9:
            E.foco(c, t, C["s08.c"] + 0.9, 0.4, lambda a: c.drawCircle(XL, 640 - S * 0.35, S * 0.55, M.paint(COR, a, stroke=5)))
        vx = reta_sol(c, t, C["s08.c"] + 0.6, 200, 920, 840, -6, 0)
        pinta(c, t, C["s08.c"] + 1.2, C["s08.c"] + 1.8, vx, 840, -3, -1, False, 160, 980)
        E.frase(c, t, C["s08.b"], [("expoente", "i", 52), ("menor", "g", 56, ENT), ("→", "g", 52), ("resultado", "i", 52), ("maior", "g", 56)],
                XE, 980)
    E.saida(c, t, C["s10"] - 0.1, contas)

    def grafico():
        eixos(c, t, PD, C["s08"], C["s08"], C["s08"], passo_y=4)
        E.curva(c, t, C["s08.a"] - 0.6, PD, lambda x: 0.5 ** x, -4.17, 1, d=1.2, cor=TINTA, rotulo=HALF + "^x", em=(-2.3, 14))
        E.saida(c, t, C["s09.b"] - 0.1, lambda: nota(c, t, C["s08.a"], "base 1/2: sempre desce", 1460, 960, 40, fundo=TINTA))
        q = ep(t, C["s09.a"], 0.6)
        if q > 0:
            M.line(c, PD.x(-5), PD.y(8), PD.x(1), PD.y(8), SAI, 0.8, 4, dash=E.TRACO, progress=q)
            E.foco(c, t, C["s09.a"] + 0.3, 0.3, lambda a: E.escreve(c, "y = 8", PD.x(0.1), PD.y(8) - 16, 40, "b", SAI, a))
        E.area(c, t, C["s09.a"] + 0.6, PD, lambda x: 0.5 ** x, -4.17, -3, g=lambda x: 8, alfa=0.3)
        if t >= C["s09.a"] + 0.6:
            M.line(c, PD.x(-3), PD.y(8), PD.x(-3), PD.oy, ENT, 0.9, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s09.a"] + 0.6, 0.5)))
        E.ponto(c, t, C["s09.b"], PD, -4, 16, cor=CERTO, r=15)
        E.foco(c, t, C["s09.b"], 0.5, lambda a: (fx(c, [(HALF, SAI), ("^{−4}", ENT), (" = 16 > 8", CERTO)], 1150, 1010, 56, a),
                                                 E.selo(c, 1690, 990, 30, True, a)))
        E.foco(c, t, C["s09.b"] + 2.6, 0.4, lambda a: E.pilula(c, "o 0 fica de fora", PD.x(0) - 30, PD.y(4), 36, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s10"] - 0.1, grafico)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"], ps("a regra, depois de igualar as bases:", "i", 66), XE, 260)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: (fx(c, [("base > 1", COR)], XE, 520, 110, a),
                                             E.pilula(c, "mantém o sinal", 1200, 485, 64, "g", fundo=CERTO, a=a)))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (fx(c, [("0 < base < 1", TINTA)], XE, 780, 110, a),
                                             E.pilula(c, "vira o sinal", 1200, 745, 64, "g", a=a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    S = 96
    E.frase(c, t, C["s11"], [("o", "i", 72), ("erro", "i", 72), ("oposto:", "i", 72)], XE, 200)
    E.frase(c, t, C["s11.a"], [("virar", "g", 76, ERRADO), ("sem", "i", 72), ("precisar", "g", 76, ERRADO)], XE + 480, 200)
    eqn_em(c, t, C["s11.b"], [("2", SAI), ("^x", ENT)], [("f{1}{4}", SAI)], 380, S, XL, "<")
    nota(c, t, C["s11.c"], "1/4 = 2⁻²", 900, 350, 44, fundo=TINTA)
    eqn_em(c, t, C["s11.c"] + 0.4, [("2", SAI), ("^x", ENT)], [("2", SAI), ("^{−2}", ENT)], 560, S, XL, "<")
    E.saida(c, t, C["s12.b"] - 0.1, lambda: E.foco(c, t, C["s11.d"], 0.5, lambda a: (
        eqn(c, [("x", ERRADO)], [("−2", ERRADO)], 740, S, a, XL, ">", ERRADO), E.selo(c, XL + 330, 710, 40, False, a))))
    nota(c, t, C["s12.a"], "a base é 2 > 1: o sinal fica", 1420, 560, 44, fundo=CERTO)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (eqn(c, [("x", CERTO)], [("−2", CERTO)], 740, S, a, XL, "<", CERTO),
                                             E.selo(c, XL + 330, 710, 40, True, a)))
    vx = reta_sol(c, t, C["s12.b"] + 0.4, 200, 920, 900, -4, 2)
    pinta(c, t, C["s12.b"] + 0.8, C["s12.b"] + 1.4, vx, 900, -2, -1, False, 160, 980, CERTO)
    E.foco(c, t, C["s12.c"] - 1.4, 0.5, lambda a: fx(c, [("x = 0:  2", SAI), ("^0", ENT), (" = 1", SAI)], 1150, 820, 64, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: fx(c, [("1 < f{1}{4}?  não", ERRADO)], 1150, 950, 64, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    HB = [(HALF, BR)]

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s13.a"], [("fuja", "g", 110, BR), ("da", "i", 100, BR), ("base", "i", 100, BR), ("fração", "g", 110, BR)], XE + 540, 190)
        E.foco(c, t, C["s13.a"] + 1.6, 0.5, lambda a: fx(c, [("f{1}{2} = 2", BR), ("^{−1}", CLARO)], XE, 400, 96, a))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: fx(c, [(HALF, BR), ("^x", CLARO), (" = 2", BR), ("^{−x}", CLARO)], 820, 400, 96, a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: (fx(c, [("2", BR), ("^{−x}", CLARO), (" > 2", BR), ("^3", CLARO)], XE, 620, 96, a),
                                                 fx(c, [("→  −x > 3", BR)], 760, 620, 96, a)))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (fx(c, [("· (−1):  x < −3", BR)], XE, 840, 110, a),
                                                 E.pilula(c, "vira, como numa inequação comum", 1380, 810, 40, "g", fundo=CLARO, cor="#07070F", a=a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("a base 2 nunca vira o sinal", "i", 66, CLARO), XE, 220)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.pilula(c, "a virada vem do menos do expoente", 700, 360, 50, "g", fundo=BR, cor="#07070F", a=a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (fx(c, [("(f{1}{3})", BR), ("^x", CLARO), (" < f{1}{9} = (f{1}{3})", BR), ("^2", CLARO)], XE, 640, 100, a),
                                             E.escreve(c, "já está na base fração", 1180, 625, 54, "i", CLARO, a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: fx(c, [("vire direto:  x > 2", BR)], XE, 880, 110, a))


# ---------------- questão e resposta ----------------
XA_, XB_ = 520, 1400


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15"] + 1.6, ps("bolinha aberta ou fechada?", "i", 56, TINTA2), XE + 520, 200)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "1)", XE, 460, 76, "g", COR, a),
                                             eqn(c, [("3", SAI), ("^{x+1}", ENT)], [("27", SAI)], 460, 130, a, 720, "≥")))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "2)", XE, 740, 76, "g", COR, a),
                                             eqn(c, [("(f{1}{5})", SAI), ("^x", ENT)], [("25", SAI)], 740, 130, a, 720, "≥")))
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=560, r=110)


def b_resposta(c, t, C, b):
    S = 72
    E.foco(c, t, C["s17"], 0.4, lambda a: (E.escreve(c, "1)", 90, 230, 60, "g", COR, a),
                                           eqn(c, [("3", SAI), ("^{x+1}", ENT)], [("27", SAI)], 230, S, a, XA_, "≥")))
    l2 = eqn(c, [("3", SAI), ("^{x+1}", ENT)], [("3", SAI), ("^3", ENT)], 380, S, 0, XA_, "≥")
    eqn_em(c, t, C["s17.a"], [("3", SAI), ("^{x+1}", ENT)], [("3", SAI), ("^3", ENT)], 380, S, XA_, "≥")
    nota(c, t, C["s17.a"] + 1.4, "base 3 > 1: o sinal fica", XA_, 120, 36, fundo=CERTO)
    iguala(c, t, C["s17.b"], l2, S, 1, 1, 380, [("x + 1", ENT)], [("3", ENT)], 530, S, XA_, op="≥")
    E.foco(c, t, C["s17.c"], 0.5, lambda a: eqn(c, [("x", ENT)], [("2", CERTO)], 680, S + 10, a, XA_, "≥", CERTO))
    vx1 = reta_sol(c, t, C["s17.d"] - 0.4, 180, 820, 860, -1, 5, 38)
    pinta(c, t, C["s17.d"], C["s17.d"] + 0.8, vx1, 860, 2, 1, True, 140, 870)
    E.foco(c, t, C["s17.d"] + 0.4, 0.4, lambda a: E.escreve(c, "fechada: o 2 entra", 180, 1000, 40, "b", TINTA2, a))
    # a segunda
    F5 = "(f{1}{5})"
    E.foco(c, t, C["s18"], 0.4, lambda a: (E.escreve(c, "2)", 980, 230, 60, "g", COR, a),
                                           eqn(c, [(F5, SAI), ("^x", ENT)], [("25", SAI)], 230, S, a, XB_, "≥")))
    l3 = eqn(c, [(F5, SAI), ("^x", ENT)], [(F5, SAI), ("^{−2}", ENT)], 400, S, 0, XB_, "≥")
    eqn_em(c, t, C["s18.a"], [(F5, SAI), ("^x", ENT)], [(F5, SAI), ("^{−2}", ENT)], 400, S, XB_, "≥")
    nota(c, t, C["s18.b"], "base 1/5: vira o sinal", XB_, 120, 36)
    iguala(c, t, C["s18.c"] - 0.6, l3, S, 1, 1, 400, [("x", ENT)], [("−2", ENT)], 580, S + 10, XB_, op="≤", cor_op=COR)
    vx2 = reta_sol(c, t, C["s18.c"] - 0.2, 1080, 1720, 760, -5, 1, 38)
    pinta(c, t, C["s18.c"] + 0.4, C["s18.c"] + 1.2, vx2, 760, -2, -1, True, 1040, 1770)
    E.foco(c, t, C["s18.d"] - 1.8, 0.5, lambda a: fx(c, [("x = 0:  ", SAI), (F5, SAI), ("^0", ENT), (" = 1", SAI)], 1040, 940, 52, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: (fx(c, [("1 < 25: o 0 fica de fora", CERTO)], 1040, 1030, 46, a),
                                             E.selo(c, 1750, 1015, 30, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s19.a", [("iguale", "g", 84), ("as", "i", 80), ("bases", "g", 84)]),
                 ("s19.b", [("base > 1", "g", 84, COR), ("mantém", "i", 80), ("o", "i", 80), ("sinal", "g", 84)]),
                 ("s19.c", [("0 < base < 1", "g", 84), ("vira", "i", 80), ("o", "i", 80), ("sinal", "g", 84, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s20"] + 1.2, [("troca", "g", 120, COR), ("de", "i", 110), ("variável", "g", 120, COR)], XE, 420)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: fx(c, [("4", SAI), ("^x", ENT), (" − 6 · 2", SAI), ("^x", ENT), (" + 8 = 0", SAI)], XE, 610, 90, a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: fx(c, [("chame 2", COR), ("^x", ENT), (" de y", COR)], XE, 790, 80, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sobe=b_sobe, desce=b_desce, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
