"""Visual — Estudativo · MAT-EXP-008: o que é logaritmo.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo; eqn() alinha cada linha pelo sinal, caixa_base() contorna as bases iguais,
iguala() faz os expoentes descerem (MAT-EXP-004 a 006).
Nesta aula entra o logaritmo, que é um expoente e por isso sai em índigo: log() monta "log₂ 8 = 3" com a base pequena embaixo
("_2" no fx), o logaritmando em preto e o logaritmo em índigo, como o expoente de 2³ = 8. rotulos() põe "base", "logaritmando" e
"logaritmo" embaixo de cada peça com um fio; mao_dupla() é a seta de mão dupla potência ↔ log, com a pílula "lê como"; na
leitura, seta_curva() leva cada peça do log à peça da potência (base → base, logaritmo → expoente, logaritmando → resultado).
A base 10 escondida aparece como um "10" fantasma numa caixa pontilhada; o logaritmo que não existe sai em vermelho, riscado,
com o gráfico de 2ˣ que nunca chega na linha y = −8."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / logaritmo · base / logaritmando / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-008_o_que_e_logaritmo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("definicao", "nove", "restricao", "erro", "atalho", "questao", "fim"))
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
    p += [(" ", SAI), (str(n), cn or SAI)]
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


def risca(c, t, t0, x0, x1, y, cor=ERRADO):
    if t >= t0:
        E.risco(c, x0, y + 6, x1, y - 4, t, t0, cor, 10)


assert 2 ** 3 == 8 and 10 ** 3 == 1000 and 9 ** 1.5 == 27 and 3 ** 2 == 9 and 3 ** 3 == 27 and 2 ** 0 == 1 and 5 ** 0 == 1
assert 8 / 2 == 4 and 2 ** 4 == 16 and 10 ** 2 == 100 and 10 ** 6 == 1000000 and abs(10 ** -3 - 0.001) < 1e-15
assert 4 ** 1.5 == 8 and abs(10 ** -2 - 0.01) < 1e-15 and 100 < 500 < 1000
XI = 960


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        S = 200
        w, xs, ws = fx(c, [("2", SAI), ("^?", ENT), (" = 8", SAI)], W / 2, 0, S, 0, "center")
        E.foco(c, t, C["s01.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^" + ("3" if t >= C["s01.b"] else "?"), ENT), (" = 8", SAI)],
                                                   xs[0], 470, S, a))
        if t >= C["s01.b"]:
            anel(c, t, C["s01.b"], xs[1] + 40, 470 - S * 0.55)
        E.frase(c, t, C["s01.b"] + 1.2, ps("você calculou um logaritmo", "i", 70, TINTA2), W / 2, 700, "center")
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "logaritmo é só um expoente", W / 2, 870, 64, "g", a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.4, [("ler", "g", 110), ("e", "i", 100), ("calcular", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 3.2, [("quando", "i", 90), ("o", "i", 90), ("log", "g", 96, COR), ("existe", "g", 96)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("2", SAI), ("^{−3}", ENT), (" = f{1}{8}", SAI)], 430, y + 10, 84, a),
                                     fx(c, [("9", SAI), ("^{1/2}", ENT), (" = 3", SAI)], 880, y, 84, a),
                                     E.escreve(c, "potência", 1300, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, [("9", SAI), ("^x", ENT), (" = 27  →  3", SAI), ("^{2x}", ENT), (" = 3", SAI), ("^3", ENT)], 430, y, 84, a),
                                     E.escreve(c, "igualar as bases", 1300, y, 60, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("2", SAI), ("^x", ENT), (" > 0", COR)], 430, y, 84, a),
                                     E.escreve(c, "nunca encosta no eixo x", 800, y, 60, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        numero_item(c, t, C[k], i + 1, 300, y)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- definição ----------------
L8 = log(2, 8, 3)
P8 = pot(2, 3, 8)


def b_definicao(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("o logaritmo responde:", "i", 66, TINTA2), XE, 200)
        E.frase(c, t, C["s04.a"], [("a", "i", 84), ("base", "g", 92), ("elevada", "i", 84), ("a", "i", 84), ("quê", "g", 92, COR),
                                   ("dá", "i", 84), ("esse", "i", 84), ("número?", "g", 92)], XE, 360)
        fx_em(c, t, C["s04.b"] - 2.2, P8, XE, 620, 130)
        mao_dupla(c, t, C["s04.b"] - 0.2, 760, 580, 1000, 580, rot=None)
        fx_em(c, t, C["s04.b"], L8, 1060, 620, 130)
        E.frase(c, t, C["s04.b"] + 0.6, ps("o logaritmo de 8 na base 2 é 3", "i", 60, TINTA2), XE, 860)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            S = 170
            w, xs, ws = fx(c, L8, W / 2, 0, S, 0, "center")
            E.frase(c, t, C["s05"], [("logaritmo", "i", 80)], W / 2, 220, "center")
            if t >= C["s05.a"]:
                xl = W / 2 - E.larg("logaritmo", "i", 80) / 2
                E.foco(c, t, C["s05.a"], 0.4, lambda a: M.line(c, xl, 240, xl + E.larg("log", "i", 80), 240, COR, a, 6))
            fx_em(c, t, C["s05.a"], L8[:1], xs[0], 520, S)
            fx_em(c, t, C["s05.b"], L8[1:2], xs[1], 520, S)
            fx_em(c, t, C["s05.c"], L8[2:4], xs[2], 520, S)
            fx_em(c, t, C["s05.d"], L8[4:], xs[4], 520, S)
            rotulos(c, t, [C["s05.b"] + 0.3, C["s05.c"] + 0.3, C["s05.d"] + 0.3], xs, ws, 520, S,
                    [(1, "base", 1), (3, "logaritmando", 2), (5, "logaritmo", 1)], tam=50)
            E.foco(c, t, C["s05.d"] + 1.6, 0.4, lambda a: E.pilula(c, "o expoente que faltava", 1450, 880, 46, "g", a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    S = 140
    E.frase(c, t, C["s06.a"], [("todo", "i", 66, TINTA2), ("log", "g", 72, COR), ("se", "i", 66, TINTA2), ("lê", "i", 66, TINTA2),
                               ("como", "i", 66, TINTA2), ("potência", "g", 72)], XE, 190)
    wl, xl, wsl = fx(c, L8, 0, 0, S, 0)
    wp, xp, wsp = fx(c, P8, 0, 0, S, 0)
    x0 = (W - (wl + 300 + wp)) / 2
    Y = 640
    _, xl, wsl = fx(c, L8, x0, 0, S, 0)
    _, xp, wsp = fx(c, P8, x0 + wl + 300, 0, S, 0)
    fx_em(c, t, C["s06.b"], L8, x0, Y, S)
    fx_em(c, t, C["s06.c"], P8, x0 + wl + 300, Y, S)
    mao_dupla(c, t, C["s06.c"] - 0.3, x0 + wl + 40, Y - 50, x0 + wl + 260, Y - 50, rot=None)
    E.foco(c, t, C["s06.c"] + 0.1, 0.4, lambda a: E.pilula(c, "lê como", x0 + wl + 150, Y + 20, 34, "g", a=a), sobe=6)
    # base embaixo; expoente e resultado por cima, um dentro do outro
    seta_curva(c, t, C["s06.d"], (centro_de(xl, wsl, 1), Y + 70), (centro_de(xp, wsp, 0), Y + 40), -110, "base", cor=TINTA, size=36)
    seta_curva(c, t, C["s06.e"], (centro_de(xl, wsl, 5), Y - S * 0.8), (centro_de(xp, wsp, 1), Y - S * 1.05), 50, "expoente", size=36)
    seta_curva(c, t, C["s06.f"], (centro_de(xl, wsl, 3), Y - S * 0.8), (centro_de(xp, wsp, 3), Y - S * 0.8), 380, "resultado", cor=TINTA, size=36)


# ---------------- base dez ----------------
def b_dez(c, t, C, b):
    S = 150
    E.frase(c, t, C["s07"], [("sem", "i", 76), ("base", "g", 84), ("escrita:", "i", 76), ("base", "i", 76), ("10", "g", 90, COR)], XE, 210)
    wlog = E.larg("log", "g", S)
    fx_em(c, t, C["s07.a"] - 0.2, [("log", SAI)], XE, 480, S)
    fantasma(c, t, C["s07.a"] + 0.6, XE + wlog + 20, 480, S)
    fx_em(c, t, C["s07.a"] - 0.2, [("1.000", SAI)], XE + wlog + E.larg("10", "g", S * 0.6) + 60, 480, S)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: fx(c, [("10", SAI), ("^?", ENT), (" = 1.000", SAI)], 1180, 480, 110, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: fx(c, [("10", SAI), ("^3", ENT), (" = 1.000", SAI)], 1180, 680, 110, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: fx(c, log(None, "1.000", 3), XE, 880, 130, a))
    E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.selo(c, 1060, 845, 40, True, a))


# ---------------- quando não sai de cabeça ----------------
def b_nove(c, t, C, b):
    S = 110
    L = log(9, 27, "x")
    fx_em(c, t, C["s08.a"], L, XE, 280, 120)
    mao_dupla(c, t, C["s08.b"] - 0.3, 830, 250, 1040, 250)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: fx(c, pot(9, "x", 27), 1100, 280, 120, a))
    E.foco(c, t, C["s08.b"] + 2.0, 0.4, lambda a: E.pilula(c, "equação exponencial", 1400, 400, 44, "g", fundo=TINTA, a=a))
    if t < C["s09"]:
        return
    nota(c, t, C["s09.a"], "9 = 3²   e   27 = 3³", 560, 450, 44, fundo=TINTA)
    X9 = 760
    l2 = eqn(c, pot(3, "2x"), pot(3, 3), 610, S, 0, X9)
    eqn_em(c, t, C["s09.b"], pot(3, "2x"), pot(3, 3), 610, S, X9)
    q = ep(t, C["s09.b"] + 0.8, 0.4)
    caixa_base(c, l2[0], 0, 610, S, q)
    caixa_base(c, l2[1], 0, 610, S, q)
    iguala(c, t, C["s09.c"], l2, S, 1, 1, 610, [("2x", ENT)], [("3", ENT)], 770, S, X9)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: eqn(c, [("x", ENT)], [("f{3}{2} = 1,5", COR)], 940, S, a, X9))
    E.foco(c, t, C["s09.d"] + 1.2, 0.5, lambda a: fx(c, log(9, 27, "1,5"), 1300, 770, 80, a))
    E.foco(c, t, C["s09.d"] + 2.4, 0.4, lambda a: E.pilula(c, "nem sempre é inteiro", 1530, 900, 44, "g", fundo=TINTA, a=a))


# ---------------- logaritmo de 1 e da própria base ----------------
def b_um(c, t, C, b):
    S = 100
    E.frase(c, t, C["s10.a"], [("log", "g", 84, COR), ("de", "i", 76), ("1", "g", 84), ("em", "i", 76), ("qualquer", "i", 76), ("base", "g", 84)],
            XE, 200)
    for i, (bb, X) in enumerate(((2, XE), (5, 760), (10, 1350))):
        p0 = pot(bb, 0, 1)
        E.foco(c, t, C["s10.b"] + 0.4 * i, 0.5, lambda a, p0=p0, X=X: fx(c, p0, X, 420, S, a))
        lg = log(bb if bb != 10 else None, 1, 0)
        E.foco(c, t, C["s10.c"] + 0.4 * i, 0.5, lambda a, lg=lg, X=X: fx(c, lg, X, 640, S, a))
    E.foco(c, t, C["s10.b"] + 1.6, 0.4, lambda a: E.escreve(c, "todo número diferente de zero, elevado a zero, dá 1", XE, 510, 44, "i", TINTA2, a))
    E.foco(c, t, C["s10.c"] + 1.4, 0.5, lambda a: E.pilula(c, "log de 1 = 0, sempre", W / 2, 775, 54, "g", a=a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: fx(c, log(2, 2, 1), XE, 950, S, a))
    mao_dupla(c, t, C["s10.d"] + 0.3, 720, 915, 960, 915, rot=None)
    E.foco(c, t, C["s10.d"] + 0.5, 0.5, lambda a: fx(c, pot(2, 1, 2), 1010, 950, S, a))
    E.foco(c, t, C["s10.d"] + 1.2, 0.4, lambda a: E.escreve(c, "a própria base dá 1", 1400, 940, 48, "i", TINTA2, a))


# ---------------- as restrições ----------------
P11 = E.Plano(1180, 170, 620, 760, -3, 3.4, -9, 10)


def b_restricao(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11"], ps("aceita qualquer número?", "i", 66, TINTA2), XE, 200)
        L = log(2, "(−8)", "?")
        fx_em(c, t, C["s11.a"], L, XE, 400, 110)
        E.foco(c, t, C["s11.a"] + 1.4, 0.5, lambda a: fx(c, pot(2, "?", "−8"), XE, 580, 110, a))
        eixos(c, t, P11, C["s11.b"] - 0.6, C["s11.b"] - 0.6, C["s11.b"] - 0.6, passo_y=4, size=34)
        E.curva(c, t, C["s11.b"] - 0.3, P11, lambda x: 2 ** x, -3, 3.3, d=0.8, cor=COR, rotulo="2^x", em=(1.5, 8.5))
        q = ep(t, C["s11.b"] + 0.4, 0.5)
        if q > 0:
            M.line(c, P11.x(-3), P11.y(-8), P11.x(3.4), P11.y(-8), ERRADO, 0.9, 5, dash=E.TRACO, progress=q)
            E.foco(c, t, C["s11.b"] + 0.7, 0.3, lambda a: E.escreve(c, "y = −8", P11.x(1.3), P11.y(-8) - 16, 40, "b", ERRADO, a))
        E.foco(c, t, C["s11.b"] + 0.6, 0.4, lambda a: fx(c, [("2", SAI), ("^x", ENT), (" > 0", COR)], XE, 760, 90, a))
        risca(c, t, C["s11.c"], XE - 10, XE + 760, 375)
        E.foco(c, t, C["s11.c"] + 0.2, 0.4, lambda a: E.pilula(c, "não existe", 540, 920, 56, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if C["s12"] <= t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12.a"], [("base", "g", 84), ("positiva", "g", 84, COR), ("e", "i", 76), ("diferente", "i", 76), ("de", "i", 76),
                                       ("1", "g", 84, COR)], XE, 200)
            E.foco(c, t, C["s12.b"], 0.5, lambda a: fx(c, [("1", SAI), ("^2", ENT), (" = 1     1", SAI), ("^5", ENT), (" = 1     1", SAI),
                                                           ("^{100}", ENT), (" = 1", SAI)], XE, 400, 90, a))
            E.foco(c, t, C["s12.c"], 0.5, lambda a: (fx(c, log(1, 5, "?"), XE, 620, 96, a), fx(c, [("→  1", SAI), ("^?", ENT), (" = 5", SAI)], 700, 620, 96, a),
                                                     E.escreve(c, "nenhum expoente", 1260, 610, 54, "g", ERRADO, a)))
            E.foco(c, t, C["s12.d"], 0.5, lambda a: (fx(c, log(1, 1, "?"), XE, 820, 96, a), fx(c, [("→  1", SAI), ("^?", ENT), (" = 1", SAI)], 700, 820, 96, a),
                                                     E.escreve(c, "qualquer expoente", 1260, 810, 54, "g", ERRADO, a)))
        E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    S = 150
    E.frase(c, t, C["s13.a"], [("condição", "g", 100, COR), ("de", "i", 90), ("existência", "g", 100, COR)], W / 2, 220, "center")
    L = log("b", "a")
    _, xs, ws = fx(c, L, W / 2, 0, S, 0, "center")
    fx_em(c, t, C["s13.a"] + 0.4, L, xs[0], 460, S)
    rotulos(c, t, [C["s13.c"], C["s13.b"]], xs, ws, 460, S, [(1, "base", 1), (3, "logaritmando", 2)], tam=46)
    E.foco(c, t, C["s13.b"] + 0.4, 0.5, lambda a: fx(c, [("a > 0", COR)], W / 2, 820, 90, a, "center"))
    E.foco(c, t, C["s13.c"] + 0.4, 0.5, lambda a: fx(c, [("b > 0  e  b ≠ 1", COR)], W / 2, 950, 90, a, "center"))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("o", "i", 72), ("erro:", "i", 72), ("dividir", "g", 84, ERRADO)], XE, 200)
    E.foco(c, t, C["s14.b"] - 0.6, 0.5, lambda a: fx(c, log(2, 8, "?"), XE, 380, 100, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: fx(c, [("8 ÷ 2 = 4 ?", ERRADO)], 900, 380, 100, a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (fx(c, [("2", SAI), ("^4", ENT), (" = 16", ERRADO), ("  ≠ 8", ERRADO)], 900, 560, 100, a),
                                             E.selo(c, 1580, 530, 40, False, a)))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "o logaritmo é um expoente", 560, 720, 52, "g", a=a))
    for i in range(3):
        E.foco(c, t, C["s14.d"] + 1.4 + 0.4 * i, 0.4, lambda a, i=i: (
            E.escreve(c, "2", XE + 30 + i * 150, 900, 110, "g", SAI, a),
            E.escreve(c, "·", XE + 115 + i * 150, 890, 90, "g", SAI, a) if i < 2 else None,
            centro(c, str(i + 1), XE + 62 + i * 150, 975, 44, "b", COR, a)), sobe=6)
    E.foco(c, t, C["s14.d"] + 2.8, 0.4, lambda a: E.escreve(c, "= 8", XE + 450, 900, 110, "g", SAI, a))
    E.foco(c, t, C["s14.e"], 0.5, lambda a: (E.escreve(c, "3 vezes", XE + 560, 975, 52, "i", COR, a),
                                             fx(c, log(2, 8, 3, cr=CERTO), 1150, 900, 100, a), E.selo(c, 1700, 865, 40, True, a)))


# ---------------- atalho (palco escuro) ----------------
def zeros(c, s, x, y, size, cor, cor_z, a):
    """número com os zeros (ou, com vírgula, as casas depois dela) na cor de destaque"""
    xx = x
    k = s.find(",")
    for i, ch in enumerate(s):
        E.escreve(c, ch, xx, y, size, "g", cor_z if (i > k if k >= 0 else ch == "0") else cor, a)
        xx += E.larg(ch, "g", size)
    return xx - x


def b_atalho(c, t, C, b):
    palco(c, t)
    def LG(n, r, a, x, y, s=96):
        w0 = fx(c, [("log ", BR)], x, y, s, a)[0]
        w1 = zeros(c, n, x + w0, y, s, BR, CLARO, a)
        fx(c, [(" = ", BR), (r, CLARO)], x + w0 + w1, y, s, a)

    def s15():
        E.frase(c, t, C["s15"], ps("o atalho da base 10:", "i", 66, CLARO), XE, 190)
        E.frase(c, t, C["s15.a"], [("conte", "g", 110, BR), ("os", "i", 100, BR), ("zeros", "g", 110, CLARO)], XE, 340)
        E.foco(c, t, C["s15.b"], 0.5, lambda a: LG("100", "2", a, XE, 520))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: LG("1.000.000", "6", a, XE, 680))
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "com vírgula: conte as casas e ponha o −", 1300, 830, 44, "g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, C["s15.e"], 0.5, lambda a: LG("0,001", "−3", a, XE, 960))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.foco(c, t, C["s16.a"], 0.5, lambda a: fx(c, [("10", BR), ("^3", CLARO), (" = 1.000", BR)], XE, 280, 100, a))
    E.foco(c, t, C["s16.a"] + 1.6, 0.5, lambda a: fx(c, [("10", BR), ("^{−3}", CLARO), (" = 0,001", BR)], 1000, 280, 100, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "só 1 seguido de zeros, ou 0,0...01", 760, 470, 52, "g", fundo=BR, cor="#07070F", a=a))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: fx(c, [("log 100 = 2  <  log 500  <  log 1.000 = 3", BR)], XE, 700, 72, a))
    E.foco(c, t, C["s16.c"] + 1.8, 0.5, lambda a: E.pilula(c, "entre 2 e 3: assunto de outra aula", 760, 880, 50, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    for k, letra, partes, y in (("s17.a", "a)", log(4, 8, "?"), 400), ("s17.b", "b)", log(None, "0,01", "?"), 590),
                                ("s17.c", "c)", log(3, "(−9)", "existe?", cr=TINTA2), 780)):
        E.foco(c, t, C[k], 0.5, lambda a, letra=letra, partes=partes, y=y: (E.escreve(c, letra, XE, y, 80, "g", COR, a),
                                                                             fx(c, partes, XE + 120, y, 100, a)))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1500, cy=560, r=110)


def b_resposta(c, t, C, b):
    def s19():
        E.foco(c, t, C["s19"], 0.4, lambda a: (E.escreve(c, "a)", XE, 220, 72, "g", COR, a), fx(c, log(4, 8, "?"), XE + 110, 220, 80, a)))
        S = 100
        eqn_em(c, t, C["s19.a"], pot(4, "x"), [("8", SAI)], 400, S, 760)
        nota(c, t, C["s19.a"] + 1.4, "base comum: 2", 1400, 370, 44, fundo=TINTA)
        l2 = eqn(c, pot(2, "2x"), pot(2, 3), 570, S, 0, 760)
        eqn_em(c, t, C["s19.b"], pot(2, "2x"), pot(2, 3), 570, S, 760)
        q = ep(t, C["s19.b"] + 0.8, 0.4)
        caixa_base(c, l2[0], 0, 570, S, q)
        caixa_base(c, l2[1], 0, 570, S, q)
        iguala(c, t, C["s19.c"], l2, S, 1, 1, 570, [("2x", ENT)], [("3", ENT)], 740, S, 760)
        E.foco(c, t, C["s19.c"] + 1.4, 0.5, lambda a: eqn(c, [("x", ENT)], [("f{3}{2} = 1,5", CERTO)], 910, S, a, 760))
        E.foco(c, t, C["s19.c"] + 1.8, 0.5, lambda a: fx(c, log(4, 8, "1,5", cr=CERTO), 1260, 900, 80, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20"], 0.4, lambda a: (E.escreve(c, "b)", XE, 220, 72, "g", COR, a), fx(c, log(None, "0,01", "?"), XE + 110, 220, 80, a)))
    E.foco(c, t, C["s20.a"], 0.5, lambda a: (E.escreve(c, "0", XE + 110, 400, 100, "g", SAI, a),
                                             zeros(c, ",01", XE + 110 + E.larg("0", "g", 100), 400, 100, SAI, COR, a),
                                             E.escreve(c, "2 casas", XE + 420, 390, 56, "i", TINTA2, a)))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: fx(c, log(None, "0,01", "−2", cr=CERTO), 900, 400, 100, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: (fx(c, [("10", SAI), ("^{−2}", ENT), (" = f{1}{100} = 0,01", SAI)], 900, 580, 90, a),
                                             E.selo(c, 1780, 550, 36, True, a)))
    E.foco(c, t, C["s20.d"], 0.4, lambda a: (E.escreve(c, "c)", XE, 820, 72, "g", COR, a), fx(c, log(3, "(−9)"), XE + 110, 820, 90, a),
                                             E.pilula(c, "não existe", 900, 795, 52, "g", fundo=ERRADO, a=a)))
    E.foco(c, t, C["s20.d"] + 1.2, 0.5, lambda a: fx(c, [("3", SAI), ("^x", ENT), (" > 0", COR), ("  sempre", TINTA2)], 1150, 820, 80, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", [("logaritmo", "g", 80, COR), ("é", "i", 76), ("o", "i", 76), ("expoente", "g", 80), ("que", "i", 76), ("falta", "i", 76)]),
                 ("s21.b", [("leia", "g", 80), ("como", "i", 76), ("potência", "g", 80)]),
                 ("s21.c", [("logaritmando", "g", 72), ("> 0;", "g", 72, COR), ("base", "g", 72), ("> 0", "g", 72, COR), ("e", "i", 68),
                            ("≠ 1", "g", 72, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            numero_item(c, t, C[k], i + 1, 300, y)
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
        E.foco(c, t, C["s21.b"] + 0.6, 0.5, lambda a: (fx(c, L8, 1080, 620, 64, a), fx(c, [("  ⇔  ", COR)] + P8, 1380, 620, 64, a)))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 230)
    E.frase(c, t, C["s22.a"], [("propriedades", "g", 110, COR), ("dos", "i", 100), ("logaritmos", "g", 110)], XE, 400)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "× vira +", 380, 580, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s22.b"] + 0.8, 0.5, lambda a: E.pilula(c, "÷ vira −", 700, 580, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: fx(c, [("log a", SAI), ("^3", ENT), (" = ", SAI), ("3", ENT), (" · log a", SAI)], XE, 780, 100, a))
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(920, 625, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, definicao=b_definicao, dez=b_dez, nove=b_nove, um=b_um, restricao=b_restricao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
