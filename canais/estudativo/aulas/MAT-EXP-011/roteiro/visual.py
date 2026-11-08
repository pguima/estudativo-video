"""Visual — Estudativo · MAT-EXP-011: achar o expoente, equação exponencial com log.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, t, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; eqn() alinha cada linha pelo sinal (MAT-EXP-004 a 006).
Logaritmo como em MAT-EXP-008 a 010: log com a base pequena embaixo ("_2" no fx), logaritmando em preto, valor em índigo; os valores
dados pela prova ficam num cartão fixo no canto (dados()); a conferência "entre 7 e 8" sai numa reta com a bolinha (entre()).
Nesta aula: o t sai voando do expoente e pousa na frente do log (voa()), que é o passo que dá nome à aula; a divisão por decimal
mostra a pílula "ande 3 casas"; o erro de ler o expoente como multiplicação sai em vermelho; no palco, o capital C some na divisão."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # t / expoente / logaritmo · base / logaritmando / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-011_equacao_exponencial_com_log.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("isolar", "conta", "meses", "erro", "atalho", "questao", "fim"))
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


def dados(c, t, t0, itens, x=1430, y=150, size=50, escuro=False, ti=None):
    """os valores que a prova dá, num cartão fixo: itens = [(logaritmando, valor), ...]; ti = instante de cada item (senão, t0)"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    w = max(fx(c, lg(None, (n, SAI)) + [(" ≈ " + v, ENT)], 0, 0, size, 0)[0] for n, v in itens)
    M.rrect(c, x - 30, y - size * 1.2, w + 60, size * 1.6 * len(itens) + size * 0.6, 22, CLARO if escuro else COR, (0.2 if escuro else 0.08) * q)
    for i, (n, v) in enumerate(itens):
        E.foco(c, t, ti[i] if ti else t0, 0.5, lambda a, n=n, v=v, i=i: fx(c, lg(None, (n, BR if escuro else SAI)) + [(" ≈ " + v, CLARO if escuro else ENT)],
                                                                            x, y + i * size * 1.6, size, a), sobe=6)


def entre(c, t, t0, x0, x1, y, vmin, vmax, v, rot, cor=None):
    """reta curta com a bolinha do resultado entre duas marcas inteiras"""
    vx = E.reta(c, t, t0, x0, x1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=42)
    q = ep(t, t0 + 0.6, 0.4)
    if q > 0:
        k = ease_back(prog(t, t0 + 0.6, 0.45))
        c.drawCircle(vx(v), y, 17 * k, M.paint(cor or CERTO, q))
        E.foco(c, t, t0 + 0.8, 0.4, lambda a: centro(c, rot, vx(v), y - 40, 46, "g", cor or CERTO, a), sobe=6)
    return vx


def voa(c, t, t0, s, de, para, cor=None, d=0.9):
    """o expoente sai do alto e pousa na frente do log, num arco"""
    p = prog(t, t0, d)
    if p <= 0 or p >= 1:
        return
    e = ease_io(p)
    E.formula(c, s, lerp(de[0], para[0], e), lerp(de[1], para[1], e) - 90 * math.sin(math.pi * e), lerp(de[2], para[2], e), "g", cor or ENT, 1.0)


def pedacos(c, partes, xs, y, size, a, pular=()):
    """desenha cada pedaço de fx na posição já calculada, menos os índices de pular"""
    for i, ((s, cor), x) in enumerate(zip(partes, xs)):
        if i not in pular and a > 0:
            fx(c, [(s, cor)], x, y, size, a)


assert abs(1.1 ** 7 - 1.95) < 0.005 and abs(1.1 ** 8 - 2.14) < 0.005 and abs(math.log10(1.1) - 0.041) < 0.001 and abs(300 / 41 - 7.3) < 0.05
assert abs(math.log10(1.02) - 0.0086) < 0.0001 and abs(3000 / 86 - 35) < 0.2 and abs(2 / 1.1 - 1.8) < 0.02 and abs(1000 * 1.1 ** 2 - 1210) < 1e-6
assert abs(math.log10(1.03) - 0.013) < 0.0005 and abs(480 / 13 - 37) < 0.1 and 15000 / 5000 == 3 and 2000 / 1000 == 2
CAIXA_1 = [("2", "0,30"), ("1,1", "0,041")]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        E.frase(c, t, C["s01.a"], [("R$ 1.000", "g", 96), ("a", "i", 80), ("10%", "g", 96, COR), ("ao", "i", 80), ("ano", "i", 80)], XE, 230)
        E.frase(c, t, C["s01.b"], [("em", "i", 76), ("quantos", "i", 76), ("anos", "g", 84, ENT), ("viram", "i", 76), ("R$ 2.000?", "g", 84)], XE, 380)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: fx(c, [("1,1", SAI), ("^7", ENT), (" ≈ 1,95", SAI)], XE, 590, 96, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: fx(c, [("1,1", SAI), ("^8", ENT), (" ≈ 2,14", SAI)], XE, 770, 96, a))
        vx = E.reta(c, t, C["s01.c"] + 0.8, 1100, 1760, 690, 6, 9, [6, 7, 8, 9], E._num, size=44)
        if t >= C["s01.d"] + 1.6:
            q = ep(t, C["s01.d"] + 1.6, 0.5)
            M.line(c, vx(7), 690, vx(8), 690, ERRADO, q, 12)
            E.foco(c, t, C["s01.d"] + 1.8, 0.4, lambda a: centro(c, "?", (vx(7) + vx(8)) / 2, 640, 80, "g", ERRADO, a))
        E.foco(c, t, C["s01.d"] + 2.4, 0.5, lambda a: E.pilula(c, "dobra entre 7 e 8, mas onde?", W / 2, 960, 56, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("achar", "g", 110), ("o", "i", 100), ("expoente", "g", 110, COR)], XE, 470)
    E.foco(c, t, C["s02.b"], 0.5, lambda a: fx(c, [("t ≈ 7,3", ENT), (" anos", TINTA2)], XE, 660, 110, a))
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("M = C · fator", SAI), ("^t", ENT)], 430, y, 90, a),
                                     E.escreve(c, "juros compostos", 1150, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, lg(None, ("a", SAI), ("^n", ENT)) + [(" = ", SAI), ("n", ENT), (" · ", SAI)] + lg(None, ("a", SAI)), 430, y, 90, a),
                                     E.escreve(c, "o expoente sai na frente", 1150, y, 60, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("0,30 ÷ 0,041 = 300 ÷ 41", SAI)], 430, y, 80, a),
                                     E.escreve(c, "dividir por decimal", 1400, y, 54, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        numero_item(c, t, C[k], i + 1, 300, y)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- montar e isolar ----------------
XI = 760
P11 = [("1,1", SAI), ("^t", ENT)]


def b_isolar(c, t, C, b):
    S = 92
    eqn_em(c, t, C["s04.a"], [("1.000 · ", SAI)] + P11, [("2.000", SAI)], 230, S, XI)
    nota(c, t, C["s04.b"], "÷ 1.000 dos dois lados", 1480, 200, 40, fundo=TINTA)
    nota(c, t, C["s04.b"] + 0.6, "isole a potência", 1480, 290, 40)
    eqn_em(c, t, C["s04.c"], P11, [("2", SAI)], 400, S, XI)
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "2 não é potência de 1,1", 1430, 380, 40, "g", fundo=ERRADO, a=a))
    L3 = lg(None, ("1,1", SAI), ("^t", ENT))
    l3 = eqn(c, L3, lg(None, ("2", SAI)), 570, S, 0, XI)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (pedacos(c, L3, l3[0][0], 570, S, a, pular=(len(L3) - 1,)),
                                             E.escreve(c, "=", XI - E.larg("=", "g", S) / 2, 570, S, "g", SAI, a),
                                             fx(c, lg(None, ("2", SAI)), l3[1][0][0], 570, S, a)))
    xt = l3[0][0][-1]
    tvoo = C["s06.a"]
    if t < tvoo + 0.1:
        E.foco(c, t, C["s05.b"], 0.5, lambda a: fx(c, [("^t", ENT)], xt, 570, S, a))
    nota(c, t, C["s05.b"] + 0.4, "log dos dois lados", 1480, 545, 40, fundo=TINTA)
    E.foco(c, t, C["s05.b"] + 1.6, 0.4, lambda a: E.escreve(c, "números iguais têm logs iguais", 1260, 640, 40, "i", TINTA2, a))
    L4 = [("t", ENT), (" · ", SAI)] + lg(None, ("1,1", SAI))
    l4 = eqn(c, L4, lg(None, ("2", SAI)), 750, S, 0, XI)
    voa(c, t, tvoo, "t", (xt + 2, 570 - S * 0.42, S * 0.58), (l4[0][0][0], 750, S))
    if t >= tvoo:
        q = ep(t, tvoo + 0.3, 0.5)
        pedacos(c, L4, l4[0][0], 750, S, q, pular=(0,))
        if t >= tvoo + 0.9:
            fx(c, L4[:1], l4[0][0][0], 750, S, 1.0)
        E.foco(c, t, tvoo + 0.3, 0.5, lambda a: (E.escreve(c, "=", XI - E.larg("=", "g", S) / 2, 750, S, "g", SAI, a),
                                                 fx(c, lg(None, ("2", SAI)), l4[1][0][0], 750, S, a)))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: eqn(c, [("t", ENT)], [("f{log 2}{log 1,1}", SAI)], 940, S, a, XI))
    nota(c, t, C["s06.b"] + 0.3, "÷ log 1,1", 1480, 910, 40, fundo=TINTA)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "o t desceu do expoente", 1430, 750, 44, "g", a=a))


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    S = 96
    E.foco(c, t, C["s07"], 0.4, lambda a: fx(c, [("t = ", ENT), ("f{log 2}{log 1,1}", SAI)], XE, 260, 84, a))
    dados(c, t, C["s07.a"], CAIXA_1, ti=[C["s07.a"], C["s07.b"]])
    E.foco(c, t, C["s07.b"] + 0.4, 0.4, lambda a: E.escreve(c, "a prova dá", 1440, 370, 40, "i", TINTA2, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: fx(c, [("t = ", ENT), ("f{0,30}{0,041}", SAI)], XE, 520, S, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: fx(c, [("= f{300}{41}", SAI)], XE + 470, 520, S, a))
    nota(c, t, C["s07.d"], "ande 3 casas", XE + 590, 345, 40, fundo=TINTA)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: fx(c, [("≈ 7,3 anos", CERTO)], XE + 800, 520, S, a))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: fx(c, [("1,1", SAI), ("^7", ENT), (" ≈ 1,95  <  2  <  2,14 ≈ 1,1", SAI), ("^8", ENT)], XE, 760, 70, a))
    entre(c, t, C["s08.a"] + 0.4, 1300, 1780, 760, 6, 9, 7.3, "7,3")
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.pilula(c, "o log mostra o ponto certo", W / 2, 950, 56, "g", a=a))


# ---------------- o método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("o", "i", 90), ("método:", "i", 90), ("3", "g", 110, COR), ("passos", "g", 100)], XE, 230)
    itens = (("s09.b", "isole a potência", [("1,1", SAI), ("^t", ENT), (" = 2", SAI)]),
             ("s09.c", "tire o log de cada lado", [("t", ENT), (" · log 1,1 = log 2", SAI)]),
             ("s09.d", "divida", [("t = ", ENT), ("f{log 2}{log 1,1}", SAI)]))
    for i, (k, txt, f) in enumerate(itens):
        y = 430 + i * 200
        numero_item(c, t, C[k], i + 1, 300, y + 4, 52)
        E.frase(c, t, C[k] + 0.1, [(w, "g" if j == 0 else "i", 70) for j, w in enumerate(txt.split())], 400, y)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, f=f, y=y: fx(c, f, 1200, y, 72, a))


# ---------------- em meses ----------------
def b_meses(c, t, C, b):
    S = 96
    E.frase(c, t, C["s10"], ps("e em meses?", "i", 72, TINTA2), XE, 200)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: fx(c, [("2% ao mês  →  × 1,02", SAI)], XE, 350, 84, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (fx(c, [("1,02", SAI), ("^t", ENT), (" = 2", SAI)], XE, 520, S, a),
                                             E.escreve(c, "t em meses", 700, 510, 50, "i", TINTA2, a)))
    dados(c, t, C["s10.c"], [("2", "0,30"), ("1,02", "0,0086")], ti=[C["s10.c"] - 1.2, C["s10.c"]])
    E.foco(c, t, C["s11.a"], 0.5, lambda a: fx(c, [("t = ", ENT), ("f{0,30}{0,0086}", SAI)], XE, 760, S, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: fx(c, [("= f{3.000}{86}", SAI)], XE + 560, 760, S, a))
    nota(c, t, C["s11.b"], "ande 4 casas", XE + 720, 590, 40, fundo=TINTA)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: fx(c, [("≈ 35 meses", CERTO)], XE + 1000, 760, S, a))
    E.foco(c, t, C["s11.c"] + 1.4, 0.4, lambda a: E.pilula(c, "quase 3 anos", 1450, 920, 50, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("o", "i", 72), ("erro:", "i", 72), ("ler", "i", 72), ("o", "i", 72), ("expoente", "g", 80, ERRADO), ("como", "i", 72),
                               ("vezes", "g", 80, ERRADO)], XE, 200)
    E.foco(c, t, C["s12.a"] + 2.0, 0.5, lambda a: fx(c, [("1,1 · t = 2", ERRADO)], XE, 380, 96, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (fx(c, [("t = 2 ÷ 1,1 ≈ 1,8 anos ?", ERRADO)], XE, 540, 96, a), E.selo(c, 1420, 510, 40, False, a)))
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: fx(c, [("em 2 anos:  1.000 · 1,1", SAI), ("^2", ENT), (" = 1.210", SAI)], XE, 720, 80, a))
    E.foco(c, t, C["s13.a"] + 2.4, 0.4, lambda a: E.escreve(c, "longe de 2.000", 1300, 710, 60, "g", ERRADO, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "o t está no expoente: sai com log", W / 2, 920, 58, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora o atalho:", "i", 66, CLARO), XE, 190)
        E.frase(c, t, C["s14.a"], [("o", "i", 100, BR), ("capital", "g", 110, CLARO), ("não", "g", 110, BR), ("importa", "g", 110, BR)], XE, 340)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "dobrar:", XE, 540, 60, "i", CLARO, a),
                                                 fx(c, [("t = ", CLARO), ("f{log 2}{log fator}", BR)], 520, 540, 84, a)))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.escreve(c, "triplicar:", XE, 760, 60, "i", CLARO, a),
                                                 fx(c, [("t = ", CLARO), ("f{log 3}{log fator}", BR)], 520, 760, 84, a)))
        if t >= C["s14.d"]:
            for y in (540, 760):
                E.caixa_pontilhada(c, 622, y - 22, 296, 96, ep(t, C["s14.d"], 0.4), CLARO, ease_io(ep(t, C["s14.d"], 0.5)))
        E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.pilula(c, "só muda o de baixo", 1350, 660, 50, "g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, C["s14.e"], 0.5, lambda a: E.pilula(c, "R$ 1.000 ou R$ 1.000.000: o mesmo tempo", W / 2, 990, 52, "g", fundo=BR, cor="#07070F", a=a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.foco(c, t, C["s15.a"] - 1.6, 0.5, lambda a: fx(c, [("C", CLARO), (" · 1,1", BR), ("^t", CLARO), (" = 2 · ", BR), ("C", CLARO)], XE, 300, 100, a))
    if t >= C["s15.a"]:
        for x0 in (XE - 6, XE + fx(c, [("C · 1,1", BR), ("^t", CLARO), (" = 2 · ", BR)], 0, 0, 100, 0)[0] - 6):
            E.risco(c, x0, 300, x0 + 82, 230, t, C["s15.a"], CLARO, 9)
    E.foco(c, t, C["s15.a"] + 0.5, 0.5, lambda a: fx(c, [("1,1", BR), ("^t", CLARO), (" = 2", BR)], 1000, 300, 100, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (fx(c, [("1,1", BR), ("^7", CLARO), (" ≈ 1,95     1,1", BR), ("^8", CLARO), (" ≈ 2,14", BR)], XE, 560, 84, a),
                                             E.escreve(c, "a prova deu a tabela", XE, 660, 54, "i", CLARO, a)))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "passa do dobro no 8º ano: basta olhar", 860, 850, 54, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
CAIXA_Q = [("3", "0,48"), ("1,03", "0,013")]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("R$ 5.000", "g", 90), ("a", "i", 80), ("3%", "g", 90, COR), ("ao", "i", 80), ("mês", "i", 80)], XE, 360)
    E.foco(c, t, C["s16.a"] + 2.6, 0.4, lambda a: E.escreve(c, "(taxa alta, só de exemplo)", XE, 440, 44, "i", TINTA2, a))
    E.frase(c, t, C["s16.b"], [("em", "i", 76), ("quantos", "i", 76), ("meses", "g", 84, ENT), ("viram", "i", 76), ("R$ 15.000?", "g", 84)], XE, 590)
    dados(c, t, C["s16.c"], CAIXA_Q, XE + 30, 780, 54, ti=[C["s16.c"], C["s16.d"]])
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=790, r=95)


def b_resposta(c, t, C, b):
    dados(c, t, C["s18"], CAIXA_Q)
    S = 90
    XR = 700
    eqn_em(c, t, C["s18.a"], [("5.000 · 1,03", SAI), ("^t", ENT)], [("15.000", SAI)], 250, S, XR)
    eqn_em(c, t, C["s18.b"], [("1,03", SAI), ("^t", ENT)], [("3", SAI)], 400, S, XR)
    nota(c, t, C["s18.b"] + 0.3, "÷ 5.000", 1250, 370, 40, fundo=TINTA)
    eqn_em(c, t, C["s18.c"], [("t", ENT)], [("f{log 3}{log 1,03}", SAI)], 590, S, XR)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: fx(c, [("= f{0,48}{0,013}", SAI)], XR + 340, 590, S, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: eqn(c, [], [("f{480}{13}", SAI)], 830, S, a, XR))
    nota(c, t, C["s19.b"], "ande 3 casas", 420, 805, 40, fundo=TINTA)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: (fx(c, [("≈ 37 meses", CERTO)], XR + 260, 860, S, a), E.selo(c, 1600, 830, 38, True, a)))
    E.foco(c, t, C["s19.c"] + 1.4, 0.4, lambda a: E.escreve(c, "pouco mais de 3 anos", XR + 260, 950, 48, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", [("isole", "g", 80, COR), ("a", "i", 76), ("potência", "i", 76)]),
                 ("s20.b", [("tire", "g", 80), ("o", "i", 76), ("log", "g", 80, COR), ("de", "i", 76), ("cada", "i", 76), ("lado", "i", 76)]),
                 ("s20.c", [("divida", "g", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            numero_item(c, t, C[k], i + 1, 300, y)
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula:", "i", 84), ("o", "i", 84), ("x", "g", 96, ENT), ("dentro", "g", 96), ("do", "i", 84),
                             ("log", "g", 96, COR)], XE, 230)
    E.foco(c, t, C["s21.a"], 0.5, lambda a: fx(c, lg(2, ("(x − 1)", SAI), esp=False) + [(" = 3", ENT)], XE, 440, 120, a))
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "raiz falsa: descarte", XE + 310, 620, 56, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, isolar=b_isolar, conta=b_conta, metodo=b_metodo, meses=b_meses, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
