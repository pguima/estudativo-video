"""Visual — Estudativo · MAT-EXP-012: equações logarítmicas.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; eqn() alinha cada linha pelo sinal (MAT-EXP-004 a 006).
Logaritmo como em MAT-EXP-008 a 011: log com a base pequena embaixo ("_2" no fx), logaritmando em preto, valor em índigo;
mao_dupla() é a seta "lê como" entre o log e a potência.
Nesta aula: o filtro da condição de existência. pinta() (de MAT-EXP-005) marca na reta a faixa permitida, com bolinha aberta;
cada raiz cai na reta como um ponto: verde com "fica" se está dentro da faixa, vermelho riscado com "descarte" se está fora.
Na condição dupla, cada condição é uma faixa sobre a reta e a faixa final, na cor da matéria, é o trecho em que as duas valem."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / logaritmo · base / logaritmando / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-012_equacoes_logaritmicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("simples", "produto", "filtro", "erro", "atalho", "questao", "fim"))
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


def risca(c, t, t0, x0, x1, y, cor=ERRADO):
    if t >= t0:
        E.risco(c, x0, y + 6, x1, y - 4, t, t0, cor, 10)


def raiz(c, t, t0, vx, y, v, ok, rot=None, size=40):
    """a raiz cai na reta: ponto verde (fica) ou vermelho com x (descarte), com a etiqueta em cima"""
    q = ep(t, t0, 0.3)
    if q <= 0:
        return
    k = ease_back(prog(t, t0, 0.45))
    X = vx(v)
    E.selo(c, X, y, 26 * k, ok, q)
    if rot:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.pilula(c, rot, X, y - 70, size, "g", fundo=CERTO if ok else ERRADO, a=a), sobe=6)


EQ = lg(None, ("x", ENT)) + [(" + ", SAI)] + lg(None, ("(x − 3)", ENT), esp=False) + [(" = 1", SAI)]
EQ_Q = lg(3, ("(x + 1)", ENT), esp=False) + [(" + ", SAI)] + lg(3, ("(x − 1)", ENT), esp=False) + [(" = 1", SAI)]
assert 2 ** 3 == 8 == 9 - 1 and 5 * (5 - 3) == 10 and (-2) * (-2 - 3) == 10 and 9 + 40 == 49 and (3 + 7) / 2 == 5 and (3 - 7) / 2 == -2
assert 2 * 6.5 - 3 == 10 and 6.5 * 3.5 == 22.75 and (2 + 1) * (2 - 1) == 3 and 2 ** 2 - 1 == 3 and 3 ** 1 == 3
assert abs(math.log10(5) + math.log10(2) - 1) < 1e-12 and abs(math.log(3, 3) + math.log(1, 3) - 1) < 1e-12


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        fx_em(c, t, C["s01.a"], EQ, W / 2, 330, 110, "center")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: fx(c, [("x = 5", ENT)], 560, 600, 120, a))
        E.foco(c, t, C["s01.b"] + 0.8, 0.5, lambda a: fx(c, [("x = −2", ENT if t < C["s01.c"] else ERRADO)], 1100, 600, 120, a))
        risca(c, t, C["s01.c"] + 0.4, 1090, 1480, 560)
        E.foco(c, t, C["s01.c"] + 0.4, 0.4, lambda a: E.pilula(c, "falsa", 1290, 700, 56, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s01.c"] + 2.0, 0.5, lambda a: E.pilula(c, "quem não confere, marca a errada", W / 2, 900, 58, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("o", "i", 100), ("x", "g", 110, ENT), ("dentro", "g", 110), ("do", "i", 100), ("log", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 3.6, [("descartar", "g", 96, ERRADO), ("a", "i", 90), ("raiz", "i", 90), ("falsa", "g", 96)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 80, TINTA, C["s03"]), ("precisa", "i", 80, TINTA, C["s03"] + 0.2), ("de", "i", 80, TINTA, C["s03"] + 0.4),
                   ("4", "g", 88, COR, C["s03"] + 0.6), ("coisas", "i", 80, TINTA, C["s03"] + 0.8)], W / 2, 200, "center")
    itens = (("s03.a", lambda a, y: (fx(c, log(2, 8, 3) + [("  ⇔  ", COR)] + pot(2, 3, 8), 430, y, 76, a),
                                     E.escreve(c, "ler como potência", 1250, y, 52, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, lg(None, ("a", SAI)) + [(" existe se a > 0", COR)], 430, y, 76, a),
                                     E.escreve(c, "condição de existência", 1250, y, 52, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, lg(None, ("a", SAI)) + [(" + ", COR)] + lg(None, ("b", SAI)) + [(" = log(a · b)", SAI)], 430, y, 76, a),
                                     E.escreve(c, "vezes dentro, mais fora", 1250, y, 52, "i", TINTA2, a))),
             ("s03.d", lambda a, y: (fx(c, [("x − 1 > 0      x² − 3x − 10 = 0", SAI)], 430, y, 70, a),
                                     E.escreve(c, "inequação e 2º grau", 1250, y, 52, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 390 + i * 175
        numero_item(c, t, C[k], i + 1, 300, y + 4, 50)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- primeiro exemplo ----------------
def b_simples(c, t, C, b):
    S = 96
    L = lg(2, ("(x − 1)", ENT), esp=False) + [(" = 3", SAI)]
    fx_em(c, t, C["s04.a"], L, XE, 230, 110)
    nota(c, t, C["s04.b"], "condição: logaritmando > 0", 1350, 200, 44)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: fx(c, [("x − 1 > 0", COR)], XE, 420, S, a))
    E.foco(c, t, C["s04.d"], 0.5, lambda a: fx(c, [("x > 1", COR)], XE, 570, S, a))
    vx = E.reta(c, t, C["s04.d"] - 0.3, 240, 1000, 860, 0, 10, list(range(0, 11)), E._num, size=38)
    pinta(c, t, C["s04.d"] + 0.2, C["s04.d"] + 0.6, vx, 860, 1, 1, False, 200, 1060)
    # a potência, à direita
    E.foco(c, t, C["s05.a"], 0.5, lambda a: (fx(c, [("2", SAI), ("^3", ENT), (" = x − 1", SAI)], 1150, 420, S, a),
                                             E.escreve(c, "lê como potência", 1150, 320, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: fx(c, [("8 = x − 1", SAI)], 1150, 570, S, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: fx(c, [("x = 9", ENT)], 1150, 720, S + 10, a))
    raiz(c, t, C["s05.d"], vx, 860, 9, True, "passa")
    E.foco(c, t, C["s05.e"], 0.5, lambda a: (fx(c, [("9 − 1 = 8:  ", SAI)] + log(2, 8, 3), 1150, 960, 64, a), E.selo(c, 1800, 935, 30, True, a)))


# ---------------- segundo exemplo ----------------
def faixa(c, t, t0, vx, y, v, cor, rot, x1=1800):
    """condição sobre a reta: bolinha aberta em v e a faixa até a ponta, com o nome à esquerda"""
    pinta(c, t, t0, t0 + 0.3, vx, y, v, 1, False, 0, x1, cor=cor, r=14)
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, rot, vx(-3) - 20 - E.larg(rot, "g", 40), y + 14, 40, "g", cor, a))


def b_produto(c, t, C, b):
    S = 84
    E.foco(c, t, C["s06"], 0.4, lambda a: fx(c, EQ, XE, 200, 90, a))

    def s06():
        E.foco(c, t, C["s06.a"], 0.5, lambda a: fx(c, lg(None, ("x", ENT)) + [(":  x > 0", SAI)], XE, 380, S, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: fx(c, lg(None, ("(x − 3)", ENT), esp=False) + [(":  x − 3 > 0  →  x > 3", SAI)], XE, 520, S, a))
        vx = E.reta(c, t, C["s06.a"] - 0.2, 600, 1700, 880, -3, 7, list(range(-3, 8)), E._num, size=38)
        faixa(c, t, C["s06.a"] + 0.3, vx, 720, 0, TINTA2, "x > 0")
        faixa(c, t, C["s06.b"] + 0.3, vx, 790, 3, TINTA2, "x > 3")
        pinta(c, t, C["s06.c"], C["s06.c"] + 0.3, vx, 880, 3, 1, False, 560, 1760)
        E.foco(c, t, C["s06.c"] + 0.4, 0.4, lambda a: E.pilula(c, "as duas: x > 3", 360, 880, 44, "g", a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    nota(c, t, C["s07"], "condição: x > 3", 1550, 175, 40)
    XI = 780
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.pilula(c, "soma de logs = log do produto", 1460, 340, 40, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: eqn(c, lg(None, ("[x · (x − 3)]", ENT), esp=False), [("1", SAI)], 340, S, a, XI))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: eqn(c, [("10", SAI), ("^1", ENT)], [("x · (x − 3)", ENT)], 480, S, a, XI))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: eqn(c, [("x² − 3x", ENT)], [("10", SAI)], 620, S, a, XI))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: eqn(c, [("x² − 3x − 10", ENT)], [("0", SAI)], 760, S, a, XI))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: fx(c, [("Δ = 9 + 40 = 49", SAI)], 1280, 620, 72, a))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: fx(c, [("r{49} = 7", SAI)], 1280, 760, 72, a))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: fx(c, [("x = f{3 + 7}{2} = ", SAI), ("5", ENT)], XE, 940, 72, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: fx(c, [("x = f{3 − 7}{2} = ", SAI), ("−2", ENT)], 960, 940, 72, a))


# ---------------- o filtro ----------------
def b_filtro(c, t, C, b):
    E.foco(c, t, C["s10"], 0.4, lambda a: fx(c, EQ, XE, 200, 80, a))
    E.frase(c, t, C["s10"], [("falta", "i", 60, TINTA2), ("o", "i", 60, TINTA2), ("filtro", "g", 66, COR)], 1300, 200)

    def s10():
        vx = E.reta(c, t, C["s10"], 300, 1620, 460, -4, 7, list(range(-4, 8)), E._num, size=40)
        pinta(c, t, C["s10"] + 0.3, C["s10"] + 0.7, vx, 460, 3, 1, False, 260, 1680)
        E.foco(c, t, C["s10"] + 0.6, 0.4, lambda a: E.escreve(c, "x > 3", vx(3) + 30, 420, 44, "g", COR, a))
        raiz(c, t, C["s10.a"], vx, 460, 5, True, "fica")
        raiz(c, t, C["s10.b"], vx, 460, -2, False, "descarte")
        E.foco(c, t, C["s10.c"], 0.5, lambda a: (fx(c, lg(None, ("(−2)", ERRADO), esp=False), XE, 700, 84, a),
                                                 E.escreve(c, "nem existe", XE + 330, 690, 56, "g", ERRADO, a)))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "x = 5", 1450, 680, 80, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: (fx(c, lg(None, ("5", SAI)) + [(" + ", SAI)] + lg(None, ("2", SAI)) + [(" = ", SAI)] + lg(None, ("10", SAI)) +
                                                    [(" = 1", ENT)], XE, 880, 80, a), E.selo(c, 1290, 850, 36, True, a)))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("por que a raiz falsa apareceu?", "i", 64, TINTA2), XE, 330)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (fx(c, [("x = −2:  (−2) · (−5) = 10", SAI)], XE, 480, 80, a),
                                             E.escreve(c, "juntos, o log existe", 1250, 470, 52, "i", CERTO, a)))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (fx(c, lg(None, ("(−2)", ERRADO), esp=False) + [("   e   ", SAI)] + lg(None, ("(−5)", ERRADO), esp=False), XE, 640, 80, a),
                                             E.escreve(c, "separados, nenhum existe", 1050, 630, 52, "g", ERRADO, a)))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "condição na equação original, antes de juntar", W / 2, 860, 52, "g", a=a))


# ---------------- o método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("o", "i", 90), ("método:", "i", 90), ("4", "g", 110, COR), ("passos", "g", 100)], XE, 220)
    for i, (k, txt) in enumerate(zip(("s12.b", "s12.c", "s12.d", "s12.e"), ("condição de existência", "junte num log só",
                                                                            "leia como potência e resolva", "passe as raízes pelo filtro"))):
        y = 400 + i * 160
        numero_item(c, t, C[k], i + 1, 300, y + 4, 52)
        E.frase(c, t, C[k] + 0.1, [(w, "g" if j == 0 else "i", 70) for j, w in enumerate(txt.split())], 400, y)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    S = 84
    E.frase(c, t, C["s13.a"], [("outro", "i", 72), ("erro:", "i", 72), ("juntar", "g", 80, ERRADO), ("somando", "g", 80, ERRADO), ("dentro", "i", 72)], XE, 200)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: fx(c, lg(None, ("(x + x − 3)", ERRADO), esp=False) + [(" = ", SAI)] + lg(None, ("(2x − 3)", ERRADO), esp=False) +
                                               [(" = 1", SAI)], XE, 370, S, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: fx(c, [("2x − 3 = 10", ERRADO)], XE, 520, S, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: fx(c, [("x = 6,5 ?", ERRADO)], 800, 520, S, a))
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (fx(c, [("6,5 · 3,5 = 22,75", SAI), ("  ≠ 10", ERRADO)], XE, 690, S, a), E.selo(c, 1220, 660, 40, False, a)))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "soma de logs vira produto dentro, não soma", W / 2, 880, 54, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
ALT = (("A", "−2"), ("B", "0"), ("C", "3"), ("D", "5"))
ALT2 = (("A", "4"), ("B", "5"), ("C", "6"), ("D", "8"))


def alternativas(c, t, t0, alts, y, corta=None, tc=None, fica=None, tf=None):
    for i, (L, v) in enumerate(alts):
        X = XE + 20 + i * 400
        E.foco(c, t, t0 + 0.2 * i, 0.4, lambda a, L=L, v=v, X=X: (E.escreve(c, f"({L})", X, y, 70, "b", CLARO, a),
                                                                   E.escreve(c, v, X + 110, y, 80, "g", BR, a)), sobe=6)
        if corta and corta(v) and t >= tc:
            E.risco(c, X - 10, y - 20, X + 250, y - 40, t, tc + 0.15 * i, ERRADO, 9)
        if fica and v == fica and t >= tf:
            q = ep(t, tf, 0.4)
            c.drawCircle(X + 120 + E.larg(v, "g", 80) / 2, y - 30, 80, M.paint(CERTO, q, stroke=7))


def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora o atalho:", "i", 66, CLARO), XE, 190)
        E.frase(c, t, C["s15.a"], [("filtre", "g", 110, CLARO), ("as", "i", 100, BR), ("alternativas", "g", 110, BR)], XE, 340)
        E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "condição: x > 3", 560, 500, 56, "g", fundo=CLARO, cor="#07070F", a=a))
        alternativas(c, t, C["s15.b"] + 0.6, ALT, 720, lambda v: float(v.replace("−", "-")) <= 3, C["s15.c"], "5", C["s15.d"])
        E.foco(c, t, C["s15.d"] + 0.3, 0.4, lambda a: E.pilula(c, "sobra uma só", 1450, 900, 56, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("toda", "i", 80, CLARO), ("resposta", "g", 88, BR), ("passa", "i", 80, CLARO), ("na", "i", 80, CLARO),
                               ("condição", "g", 88, BR)], XE, 280)
    alternativas(c, t, C["s16.b"], ALT2, 560)
    E.foco(c, t, C["s16.b"] + 1.0, 0.4, lambda a: E.escreve(c, "todas > 3: o filtro não decide", XE, 690, 56, "i", CLARO, a))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "resolva a equação", 760, 880, 62, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    fx_em(c, t, C["s17.a"], EQ_Q, XE, 480, 100)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.escreve(c, "cada parêntese inteiro dentro do seu log", XE, 600, 50, "i", TINTA2, a))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1560, cy=820, r=95)


def b_resposta(c, t, C, b):
    S = 84
    E.foco(c, t, C["s19"], 0.4, lambda a: fx(c, EQ_Q, XE, 200, 72, a))

    def s19():
        E.foco(c, t, C["s19.a"], 0.5, lambda a: fx(c, [("x + 1 > 0   e   x − 1 > 0", COR)], XE, 380, S, a))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: fx(c, [("x > 1", COR)], XE, 530, S + 10, a))
        vx = E.reta(c, t, C["s19.b"] - 0.2, 900, 1700, 530, -3, 4, list(range(-3, 5)), E._num, size=38)
        pinta(c, t, C["s19.b"] + 0.2, C["s19.b"] + 0.5, vx, 530, 1, 1, False, 860, 1760)
        E.foco(c, t, C["s19.c"], 0.5, lambda a: fx(c, [("(x + 1) · (x − 1) = 3", ENT), ("^1", ENT), (" = 3", SAI)], XE, 760, S, a))
        E.foco(c, t, C["s19.c"] + 0.4, 0.4, lambda a: E.pilula(c, "um log só, lido como potência", 1400, 880, 40, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    nota(c, t, C["s20"], "condição: x > 1", 1550, 175, 40)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: fx(c, [("x² − 1 = 3", ENT)], XE, 380, S, a))
    E.foco(c, t, C["s20.a"] + 0.4, 0.4, lambda a: E.escreve(c, "soma vezes diferença", XE + 520, 370, 44, "i", TINTA2, a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: fx(c, [("x² = 4", ENT)], XE, 530, S, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: fx(c, [("x = 2  ou  x = −2", ENT)], XE, 680, S, a))
    if t >= C["s20.d"]:
        x0 = XE + fx(c, [("x = 2  ou  ", ENT)], 0, 0, S, 0)[0]
        risca(c, t, C["s20.d"], x0 - 10, x0 + fx(c, [("x = −2", ENT)], 0, 0, S, 0)[0] + 10, 655)
    nota(c, t, C["s20.d"] + 0.3, "−2 não passa no filtro", XE + 900, 650, 40, fundo=ERRADO)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: E.pilula(c, "x = 2", 470, 850, 80, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s21.a"], 0.5, lambda a: fx(c, log(3, 3, 1), 1000, 800, 72, a))
    E.foco(c, t, C["s21.b"], 0.5, lambda a: fx(c, log(3, 1, 0), 1000, 940, 72, a))
    E.foco(c, t, C["s21.b"] + 1.2, 0.5, lambda a: (fx(c, [("1 + 0 = 1", SAI)], 1420, 870, 72, a), E.selo(c, 1790, 845, 30, True, a)))


# ---------------- fechamento ----------------
P23 = E.Plano(1300, 330, 500, 500, -2, 6, -2, 6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", [("condição", "g", 80, COR), ("de", "i", 76), ("existência", "g", 80, COR), ("primeiro", "i", 76)]),
                 ("s22.b", [("junte", "g", 80), ("num", "i", 76), ("log", "g", 80), ("só", "i", 76), ("e", "i", 76), ("leia", "g", 80), ("como", "i", 76),
                            ("potência", "i", 76)]),
                 ("s22.c", [("descarte", "g", 80, ERRADO), ("quem", "i", 76), ("não", "i", 76), ("passar", "i", 76), ("no", "i", 76), ("filtro", "g", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            numero_item(c, t, C[k], i + 1, 300, y)
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 230)
    E.frase(c, t, C["s23.a"], [("função", "g", 108, COR), ("logarítmica", "g", 108)], XE, 400)
    if t >= C["s23.b"] - 0.4:
        eixos(c, t, P23, C["s23.b"] - 0.4, C["s23.b"] - 0.4, C["s23.b"] - 0.4, passo_x=2, passo_y=2, size=32)
        q = ep(t, C["s23.b"] - 0.2, 0.5)
        if q > 0:
            M.line(c, P23.x(-2), P23.y(-2), P23.x(6), P23.y(6), CINZA, q, 3, dash=E.TRACO)
        E.curva(c, t, C["s23.b"], P23, lambda x: 2 ** x, -2, 2.58, d=0.8, cor=TINTA2, rotulo="2^x", em=(1.4, 5.2))
        E.curva(c, t, C["s23.b"] + 0.8, P23, lambda x: math.log2(x), 0.25, 6, d=0.8, cor=COR)
        E.foco(c, t, C["s23.b"] + 1.6, 0.4, lambda a: fx(c, lg(2, ("x", ENT)), P23.x(3.6), P23.y(1.0), 44, a))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: fx(c, lg(2, ("x", ENT)) + [(" > 3", SAI)], XE, 600, 110, a))
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 640, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(980, 780, p), lerp(1000, 825, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, simples=b_simples, produto=b_produto, filtro=b_filtro, metodo=b_metodo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
