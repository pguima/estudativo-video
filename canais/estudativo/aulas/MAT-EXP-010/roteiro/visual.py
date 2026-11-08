"""Visual — Estudativo · MAT-EXP-010: usar log 2, log 3 e mudança de base.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; eqn() alinha cada linha pelo sinal (MAT-EXP-004 a 006).
Logaritmo como em MAT-EXP-008 e 009: log() monta "log₂ 5" com a base pequena embaixo ("_2" no fx), logaritmando em preto e o valor
do logaritmo em índigo; mao_dupla() é a seta potência ↔ log; a operação que muda de nome sai na cor da matéria; regra() põe a
fórmula numa faixa com a pílula do nome (aqui, a mudança de base, log₂ 5 = log 5 / log 2).
Nesta aula: os valores dados (log 2 ≈ 0,30 e log 3 ≈ 0,48) ficam em cartões fixos no canto (dados()); cada conta substitui o log
pelo valor; a conferência "entre 1 e 2" sai numa reta com a bolinha do resultado (entre()); o erro de subtrair sai em vermelho."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / logaritmo · base / logaritmando / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-010_log_2_log_3_e_mudanca_de_base.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("valores", "cinco", "base", "erro", "atalho", "questao", "fim"))
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

def apelido(c, t, t0, partes, x, y, size, nome="y", cor=None):
    """caixa pontilhada em volta da potência que se repete (partes de fx) e a etiqueta com o apelido embaixo"""
    w, _, _ = fx(c, partes, 0, 0, size, 0)
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    E.caixa_pontilhada(c, x - size * 0.12, y - size * 1.12, w + size * 0.24, size * 1.38, q, cor or COR, ease_io(q))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, f"= {nome}", x + w / 2, y + size * 0.62, size * 0.42, "g", fundo=cor or COR, a=a), sobe=6)

def linha_valores(c, t, xs, vals, ts, y, size=70, cor=TINTA):
    """valores lado a lado, cada um no seu instante"""
    for X, s, t0 in zip(xs, vals, ts):
        E.foco(c, t, t0, 0.4, lambda a, X=X, s=s: E.formula(c, s, X, y, size, "g", cor, a, "center"), sobe=6)


def saltos(c, t, xs, y, rots, ts, cor=None, size=34, bojo=46, folga=20):
    """setas curvas por cima de uma linha de valores, cada uma com a sua pílula"""
    for i, (rot, t0) in enumerate(zip(rots, ts)):
        seta_curva(c, t, t0, (xs[i] + folga, y), (xs[i + 1] - folga, y), bojo, rot, cor=cor, size=size)




# ---------------- o logaritmo: base pequena embaixo, rótulos e a seta de mão dupla ----------------
def log(b, n, r=None, cb=None, cn=None, cr=None, op=" = ", co=None):
    """partes de fx para log_b n (= r): base pequena embaixo, logaritmando em preto, logaritmo em índigo (é um expoente).
    b = None ou "" para a base 10 escondida; n aceita a escrita de E.formula ("(x − 1)", "f{1}{8}")"""
    p = [("log", SAI)]
    if b:
        p.append(("_" + str(b), cb or SAI))
    if not str(n).startswith("("):
        p.append((" ", SAI))
    else:
        p.append(("", SAI))
    p.append((str(n), cn or SAI))
    if r is not None:
        p += [(op, co or SAI), (str(r), cr or ENT)]
    return p


def pot(b, e, r=None, cb=None, ce=None, cr=None, op=" = "):
    """partes de fx para b^e (= r), com o expoente em índigo; separa base, expoente e resultado para as setas"""
    p = [(str(b), cb or SAI), ("^" + ("{" + str(e) + "}" if len(str(e)) > 1 else str(e)), ce or ENT)]
    if r is not None:
        p += [(op, SAI), (str(r), cr or SAI)]
    return p


def centro_de(xs, ws, k):
    return xs[k] + ws[k] / 2


def rotulos(c, t, ts, xs, ws, y, size, itens, cor=None, tam=44):
    """etiquetas embaixo das peças: itens = [(índice da peça, texto, profundidade 1 ou 2)], uma em cada instante de ts"""
    for t0, (k, txt, prof) in zip(ts, itens):
        X = centro_de(xs, ws, k)
        topo = y + size * (0.42 if k == 1 else 0.16)
        yb = y + size * 0.35 + 90 * prof
        q = ep(t, t0, 0.4)
        if q > 0:
            M.line(c, X, topo, X, lerp(topo, yb - tam * 0.95, ease_io(q)), cor or TINTA2, q, 3)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, X=X, txt=txt, yb=yb: centro(c, txt, X, yb, tam, "i", cor or TINTA2, a), sobe=6)


def ponta(c, x, y, ux, uy, cor, a, k=1.0):
    tri = skia.Path()
    tri.moveTo(x + ux * 6 * k, y + uy * 6 * k)
    tri.lineTo(x - ux * 22 * k - uy * 13 * k, y - uy * 22 * k + ux * 13 * k)
    tri.lineTo(x - ux * 22 * k + uy * 13 * k, y - uy * 22 * k - ux * 13 * k)
    tri.close()
    c.drawPath(tri, M.paint(cor, a))


def mao_dupla(c, t, t0, x0, y0, x1, y1, rot="lê como", cor=None, size=38, d=0.6, escuro=False):
    """seta de mão dupla entre o log e a potência: cresce do meio para as pontas, com a pílula no meio"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or (CLARO if escuro else COR)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ax, ay = lerp(mx, x0, p), lerp(my, y0, p)
    bx, by = lerp(mx, x1, p), lerp(my, y1, p)
    M.line(c, ax, ay, bx, by, cor, 1.0, 6)
    n = math.hypot(x1 - x0, y1 - y0) or 1.0
    ux, uy = (x1 - x0) / n, (y1 - y0) / n
    q = ep(t, t0 + d * 0.8, 0.2)
    ponta(c, bx, by, ux, uy, cor, q)
    ponta(c, ax, ay, -ux, -uy, cor, q)
    if rot:
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda a: E.pilula(c, rot, mx + (0 if abs(ux) > abs(uy) else size * 3.2),
                                                         my - (size * 1.1 if abs(ux) > abs(uy) else 0), size, "g", fundo=cor,
                                                         cor="#07070F" if escuro else E.SOBRE, a=a), sobe=6)


def fantasma(c, t, t0, x, y, size, txt="10", cor=None):
    """a base escondida: um "10" pequeno na caixa pontilhada, onde a base ficaria"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    s = size * 0.6
    w = E.larg(txt, "g", s)
    E.caixa_pontilhada(c, x - 6, y + size * 0.2 - s * 0.8, w + 12, s * 1.0, q, cor or COR, ease_io(q))
    E.escreve(c, txt, x, y + size * 0.2, s, "g", cor or COR, q)


# ---------------- peças desta aula ----------------
def numero_item(c, t, t0, n, x, y, r=56):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x, y - 30, r, a=a),
                                     E.escreve(c, str(n), x - E.larg(str(n), "g", r * 1.14) / 2, y - 30 + r * 0.41, r * 1.14, "g", BR, a)))


def lg(b, *partes, esp=True):
    """'log_b' seguido das partes (texto, cor); b None = base 10 escondida"""
    p = [("log", SAI)]
    if b:
        p.append(("_" + str(b), SAI))
    if esp:
        p.append((" ", SAI))
    return p + list(partes)


def regra(c, t, t0, partes, nome, y, size=110, escuro=False, topo=1.1, alto=1.75):
    """a fórmula numa faixa clara, centrada, com a pílula do nome em cima (topo/alto em múltiplos de size; maiores com fração)"""
    w, _, _ = fx(c, partes, W / 2, y, size, 0, "center")
    q = ep(t, t0, 0.5)
    if q > 0:
        M.rrect(c, W / 2 - w / 2 - 50, y - size * topo, w + 100, size * alto, 28, CLARO if escuro else COR, (0.18 if escuro else 0.1) * q)
    fx_em(c, t, t0, partes, W / 2, y, size, "center")
    if nome:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, nome, W / 2, y - size * 1.1, size * 0.4, "g",
                                                       fundo=CLARO if escuro else COR, cor="#07070F" if escuro else E.SOBRE, a=a), sobe=6)


def dados(c, t, t0, x=1450, y=150):
    """os valores que a prova dá, num cartão fixo no canto"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x - 30, y - 60, 420, 170, 22, COR, 0.08 * q)
    fx(c, lg(None, ("2", SAI)) + [(" ≈ 0,30", ENT)], x, y, 54, q)
    fx(c, lg(None, ("3", SAI)) + [(" ≈ 0,48", ENT)], x, y + 80, 54, q)


def entre(c, t, t0, x0, x1, y, vmin, vmax, v, rot, cor=None):
    """reta curta com a bolinha do resultado entre duas marcas inteiras"""
    vx = E.reta(c, t, t0, x0, x1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=42)
    q = ep(t, t0 + 0.6, 0.4)
    if q > 0:
        k = ease_back(prog(t, t0 + 0.6, 0.45))
        c.drawCircle(vx(v), y, 17 * k, M.paint(cor or CERTO, q))
        E.foco(c, t, t0 + 0.8, 0.4, lambda a: centro(c, rot, vx(v), y - 40, 46, "g", cor or CERTO, a), sobe=6)
    return vx


MAIS, MENOS = (" + ", COR), (" − ", COR)
L2, L3 = 0.30, 0.48
assert abs(3 * L2 + 2 * L3 - 1.86) < 1e-9 and 72 == 8 * 9 == 2 ** 3 * 3 ** 2 and abs(1 - L2 - 0.70) < 1e-9 and 10 < 72 < 100
assert abs(0.70 / 0.30 - 2.333) < 1e-3 and 2 ** 2 < 5 < 2 ** 3 and abs(0.70 - 0.30 - 0.40) < 1e-9 and 2 ** 0.4 < 2
assert abs(0.70 + 1 - 1.70) < 1e-9 and 15 == 3 * 5 and abs(0.48 + 0.70 - 1.18) < 1e-9 and abs(0.48 / 0.30 - 1.6) < 1e-9 and 2 < 3 < 4
assert abs(math.log10(72) - 1.857) < 1e-3 and abs(math.log(5, 2) - 2.32) < 1e-2 and abs(10 ** 0.30 - 2) < 0.01


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: fx(c, lg(None, ("72", SAI)) + [(" = ?", ENT)], W / 2, 380, 170, a, "center"))
        E.frase(c, t, C["s01.a"] + 1.6, ps("sem calculadora", "i", 64, TINTA2), W / 2, 520, "center")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "log 2 ≈ 0,30", 700, 690, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.b"] + 0.4, 0.5, lambda a: E.pilula(c, "log 3 ≈ 0,48", 1220, 690, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: fx(c, lg(None, ("72", SAI)) + [(" ≈ 1,86", CERTO)], W / 2, 900, 110, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("log", "g", 110), ("2", "g", 110, COR), ("e", "i", 100), ("log", "g", 110), ("3", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 4.0, [("trocar", "g", 96), ("a", "i", 90), ("base", "g", 96, COR)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("2", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (E.pilula(c, "× vira +", 560, y - 25, 50, "g", fundo=TINTA, a=a),
                                     E.pilula(c, "÷ vira −", 860, y - 25, 50, "g", fundo=TINTA, a=a),
                                     E.pilula(c, "expoente vai para a frente", 1340, y - 25, 50, "g", fundo=TINTA, a=a))),
             ("s03.b", lambda a, y: (fx(c, lg(None, ("1.000", SAI)) + [(" = 3", ENT)], 430, y, 90, a),
                                     E.escreve(c, "a base 10 escondida", 1050, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 480 + i * 240
        numero_item(c, t, C[k], i + 1, 300, y)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- os valores ----------------
def b_valores(c, t, C, b):
    E.frase(c, t, C["s04"], ps("os valores, na base 10:", "i", 70, TINTA2), XE, 200)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: fx(c, lg(None, ("2", SAI)) + [(" ≈ 0,30", ENT)], XE, 420, 130, a))
    E.foco(c, t, C["s04.b"], 0.5, lambda a: fx(c, lg(None, ("3", SAI)) + [(" ≈ 0,48", ENT)], XE, 640, 130, a))
    mao_dupla(c, t, C["s04.c"] - 0.2, 950, 380, 1130, 380, rot=None)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: fx(c, [("10", SAI), ("^{0,30}", ENT), (" ≈ 2", SAI)], 1190, 420, 110, a))
    E.foco(c, t, C["s04.c"] + 2.4, 0.5, lambda a: E.pilula(c, "aproximações: o enunciado costuma dar", W / 2, 880, 54, "g", a=a))


# ---------------- log 72 ----------------
def b_setenta(c, t, C, b):
    dados(c, t, C["s05"])
    S = 96
    E.foco(c, t, C["s05.a"], 0.5, lambda a: fx(c, [("72", SAI)], XE, 260, S, a))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: fx(c, [(" = 8 · 9", SAI)], XE + E.larg("72", "g", S), 260, S, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: fx(c, [(" = 2", SAI), ("^3", ENT), (" · 3", SAI), ("^2", ENT)], XE + E.larg("72 = 8 · 9", "g", S) + 20, 260, S, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: fx(c, lg(None, ("72", SAI)) + [(" = ", SAI), ("3", COR), (" · ", SAI)] + lg(None, ("2", SAI)) + [MAIS, ("2", COR),
                                                (" · ", SAI)] + lg(None, ("3", SAI)), XE, 430, S, a))
    E.foco(c, t, C["s06.a"], 0.5, lambda a: fx(c, [("3 · 0,30 = ", SAI), ("0,90", ENT)], XE, 600, 84, a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: fx(c, [("2 · 0,48 = ", SAI), ("0,96", ENT)], XE, 740, 84, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: fx(c, lg(None, ("72", SAI)) + [(" ≈ 0,90 + 0,96 = ", SAI), ("1,86", CERTO)], XE, 910, 76, a))
    E.foco(c, t, C["s06.d"] - 2.6, 0.5, lambda a: fx(c, [("10 < 72 < 100", SAI)], 1260, 620, 70, a))
    entre(c, t, C["s06.d"], 1260, 1720, 800, 0, 3, 1.86, "1,86")


# ---------------- log 5 ----------------
def b_cinco(c, t, C, b):
    dados(c, t, C["s07"])
    S = 100
    E.foco(c, t, C["s07.a"], 0.5, lambda a: fx(c, lg(None, ("5", SAI)) + [(" = ?", ENT)], XE, 280, S, a))
    E.foco(c, t, C["s07.a"] + 1.4, 0.4, lambda a: E.escreve(c, "5 é primo, e não é 2 nem 3", XE, 380, 50, "i", TINTA2, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: fx(c, [("5 = f{10}{2}", SAI)], 1000, 300, S, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: fx(c, lg(None, ("5", SAI)) + [(" = ", SAI)] + lg(None, ("10", SAI)) + [MENOS] + lg(None, ("2", SAI)), XE, 580, S, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "log 10 = 1", 1500, 550, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.e"], 0.5, lambda a: fx(c, [("= 1 − 0,30 = ", SAI), ("0,70", CERTO)], XE + E.larg("log 5 ", "g", S), 780, S, a))


# ---------------- mudança de base ----------------
MB = lg(2, ("5", SAI)) + [(" = ", SAI), ("f{log 5}{log 2}", COR)]


def b_base(c, t, C, b):
    def s08():
        dados(c, t, C["s08"])
        E.foco(c, t, C["s08.a"], 0.5, lambda a: fx(c, lg(2, ("5", SAI)) + [(" = ?", ENT)], XE, 300, 110, a))
        E.foco(c, t, C["s08.a"] + 1.6, 0.4, lambda a: E.escreve(c, "a prova só deu a base 10", XE, 410, 54, "i", TINTA2, a))
        regra(c, t, C["s08.c"], MB, None, 720, 120, topo=1.45, alto=2.2)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "mudança de base", W / 2, 720 - 174, 48, "g", a=a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "em cima e embaixo, base 10", W / 2, 950, 50, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            S = 100
            E.frase(c, t, C["s09"], ps("de onde vem?", "i", 72, TINTA2), XE, 200)
            XI = 760
            E.foco(c, t, C["s09.a"], 0.5, lambda a: eqn(c, pot(2, "x"), [("5", SAI)], 360, S, a, XI))
            E.foco(c, t, C["s09.a"] + 0.4, 0.4, lambda a: fx(c, lg(2, ("5", SAI)) + [(" = x", ENT)], 1250, 360, 70, a))
            E.foco(c, t, C["s09.b"], 0.5, lambda a: eqn(c, lg(None, ("2", SAI), ("^x", ENT)), lg(None, ("5", SAI)), 530, S, a, XI))
            E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.pilula(c, "log dos dois lados", 1450, 500, 44, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: eqn(c, [("x", ENT), (" · ", SAI)] + lg(None, ("2", SAI)), lg(None, ("5", SAI)), 700, S, a, XI))
            E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: E.pilula(c, "o expoente sai na frente", 1450, 670, 44, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s09.d"], 0.5, lambda a: eqn(c, [("x", ENT)], [("f{log 5}{log 2}", COR)], 900, S, a, XI))
            E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.pilula(c, "÷ log 2", 1450, 870, 44, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    dados(c, t, C["s10"] - 0.3)
    E.foco(c, t, C["s10"], 0.4, lambda a: fx(c, MB, XE, 250, 80, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: fx(c, [("= f{0,70}{0,30}", SAI)], XE + 470, 470, 100, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: fx(c, [("= f{70}{30}", SAI)], XE + 870, 470, 100, a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: fx(c, [("≈ 2,33", CERTO)], XE + 1170, 470, 100, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: fx(c, [("2", SAI), ("^2", ENT), (" = 4  <  5  <  8 = 2", SAI), ("^3", ENT)], XE, 720, 90, a))
    vx = entre(c, t, C["s10.e"], 1180, 1700, 880, 1, 4, 2.33, "2,33")
    E.foco(c, t, C["s10.e"] + 1.4, 0.4, lambda a: E.selo(c, 1800, 860, 34, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("o", "i", 72), ("erro:", "i", 72), ("trocar", "g", 80, ERRADO), ("÷", "g", 84, ERRADO), ("por", "i", 72), ("−", "g", 84, ERRADO)],
            XE, 200)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (fx(c, lg(2, ("5", SAI)) + [(" = 0,70 − 0,30 = 0,40", ERRADO)], XE, 380, 96, a),
                                             E.selo(c, 1500, 350, 40, False, a)))
    if t < C["s12"]:
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (fx(c, [("2", SAI), ("^{0,40}", ERRADO), (" < 2", SAI), ("^1", ENT), (" = 2", SAI)], XE, 560, 90, a),
                                             E.escreve(c, "longe de 5", 900, 550, 60, "g", ERRADO, a)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (fx(c, lg(None, ("(f{a}{b})", SAI), esp=False) + [(" = ", SAI)] + lg(None, ("a", SAI)) + [MENOS] +
                                                lg(None, ("b", SAI)), XE, 760, 80, a),
                                             E.escreve(c, "÷ dentro do log", 1050, 750, 54, "i", TINTA2, a)))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (fx(c, MB, XE, 940, 80, a), E.escreve(c, "um log ÷ o outro", 1050, 930, 54, "g", CERTO, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora o atalho:", "i", 66, CLARO), XE, 190)
        E.frase(c, t, C["s13.a"], [("2", "g", 110, CLARO), ("e", "i", 100, BR), ("5", "g", 110, CLARO), ("fecham", "i", 100, BR), ("10", "g", 110, BR)], XE, 340)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: fx(c, [("log 2 + log 5 = ", BR), ("1", CLARO)], XE, 520, 96, a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: fx(c, [("log 5 = 1 − log 2 = ", BR), ("0,70", CLARO)], XE, 690, 96, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: fx(c, [("log 50 = log 5 + 1 = ", BR), ("1,70", CLARO)], XE, 860, 96, a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14.a"], 0.5, lambda a: fx(c, [("2 · 5 = 10   e   log 10 = ", BR), ("1", CLARO)], XE, 300, 90, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (fx(c, [("log 7 = ?", BR)], XE, 560, 110, a),
                                             E.escreve(c, "não sai de 2, 3 e 10", 700, 550, 60, "i", CLARO, a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "a prova precisa dar o valor", 760, 780, 60, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    dados(c, t, C["s15.a"], XE + 30, 330)
    for k, letra, partes, y in (("s15.b", "a)", lg(None, ("15", SAI)), 640), ("s15.c", "b)", lg(2, ("3", SAI)), 820)):
        E.foco(c, t, C[k], 0.5, lambda a, letra=letra, partes=partes, y=y: (E.escreve(c, letra, XE, y, 80, "g", COR, a),
                                                                             fx(c, partes, XE + 120, y, 110, a)))
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=560, r=110)


def b_resposta(c, t, C, b):
    dados(c, t, C["s17"])
    S = 90

    def s17():
        E.foco(c, t, C["s17"], 0.4, lambda a: (E.escreve(c, "a)", XE, 230, 72, "g", COR, a), fx(c, lg(None, ("15", SAI)), XE + 110, 230, 80, a)))
        E.foco(c, t, C["s17.a"], 0.5, lambda a: fx(c, [("15 = 3 · 5", SAI)], 750, 230, 80, a))
        E.foco(c, t, C["s17.b"], 0.5, lambda a: fx(c, [("= ", SAI)] + lg(None, ("3", SAI)) + [MAIS] + lg(None, ("5", SAI)), XE + 110, 420, S, a))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: fx(c, lg(None, ("5", SAI)) + [(" = 1 − 0,30 = ", SAI), ("0,70", ENT)], XE + 110, 600, 80, a))
        E.foco(c, t, C["s17.d"], 0.5, lambda a: (fx(c, [("= 0,48 + 0,70 = ", SAI), ("1,18", CERTO)], XE + 110, 790, S, a),
                                                 E.selo(c, 1200, 760, 36, True, a)))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.foco(c, t, C["s18"], 0.4, lambda a: (E.escreve(c, "b)", XE, 230, 72, "g", COR, a), fx(c, lg(2, ("3", SAI)), XE + 110, 230, 80, a)))
    E.foco(c, t, C["s18.a"], 0.5, lambda a: fx(c, [("= f{log 3}{log 2} = f{0,48}{0,30}", SAI)], XE + 110, 450, S, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: fx(c, [("= f{48}{30} = ", SAI), ("1,6", CERTO)], XE + 110, 680, S, a))
    E.foco(c, t, C["s18.c"] - 2.0, 0.5, lambda a: fx(c, [("2 < 3 < 4", SAI)], 1180, 680, 70, a))
    entre(c, t, C["s18.c"], 1180, 1700, 860, 0, 3, 1.6, "1,6")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s19.a", [("fatore", "g", 80), ("e", "i", 76), ("use", "i", 76), ("log 2", "g", 80, COR), ("e", "i", 76), ("log 3", "g", 80, COR)]),
                 ("s19.b", [("5", "g", 80), ("=", "g", 80), ("10 ÷ 2:", "g", 80, COR), ("log 5 = 1 − log 2", "g", 70)]),
                 ("s19.c", [("trocar", "g", 80), ("a", "i", 76), ("base:", "i", 76), ("um", "i", 76), ("log", "g", 80), ("÷", "g", 80, COR), ("o", "i", 76),
                            ("outro", "i", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            numero_item(c, t, C[k], i + 1, 300, y)
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 230)
    E.frase(c, t, C["s20.a"], [("em", "i", 80), ("quanto", "i", 80), ("tempo", "g", 88, COR), ("o", "i", 80), ("dinheiro", "i", 80), ("dobra?", "g", 88)],
            XE, 410)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: fx(c, [("1,1", SAI), ("^t", ENT), (" = 2", SAI)], XE, 640, 140, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 640, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 665, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, valores=b_valores, setenta=b_setenta, cinco=b_cinco, base=b_base, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
