"""Visual — Estudativo · MAT-EXP-007: praticando a função exponencial.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, t, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta só o expoente de índigo ("_0" = índice embaixo); contas à esquerda, gráfico à direita quando ajuda.
Como em MAT-EXP-004 a 006: eqn() alinha cada linha pelo sinal, caixa_base() contorna as bases iguais, iguala() faz os expoentes
descerem, apelido() marca a potência que se repete, pinta()/E.intervalo mostram a solução na reta e saltos() faz a escada ×2 ou ÷2.
Nesta aula: quatro situações, cada uma com cartão de enunciado (situacao()), relógio de pausa e resposta; o erro da conta apressada
riscado em vermelho; o atalho das dobras no palco escuro."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / t / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-007_praticando_funcao_exponencial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
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




# ---------------- peças desta aula ----------------
def situacao(c, t, t0, n, titulo="situação"):
    """cabeçalho do enunciado: esfera com o número e a palavra situação"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 180, 56, a=a),
                                     E.escreve(c, str(n), XE + 50 - E.larg(str(n), "g", 64) / 2, 203, 64, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [(w, "i", 76) for w in titulo.split()], XE + 140, 205)


def numero_item(c, t, t0, n, x, y, r=46):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x, y - 26, r, a=a),
                                     E.escreve(c, str(n), x - E.larg(str(n), "g", r * 1.1) / 2, y - 26 + r * 0.4, r * 1.1, "g", BR, a)))


def pausa(c, t, C, k):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx=1560, cy=560, r=110)


def risca(c, t, t0, x0, x1, y, cor=ERRADO):
    if t >= t0:
        E.risco(c, x0, y + 6, x1, y - 4, t, t0, cor, 10)


HALF = "(f{1}{2})"
maquina = lambda a: 80 * 0.8 ** a
assert abs(0.8 ** 2 - 0.64) < 1e-12 and abs(maquina(2) - 51.2) < 1e-9 and 80 * 0.6 == 48 and 64 * 0.2 == 12.8 and 80 * 0.8 == 64
assert [200 * 0.5 ** k for k in range(4)] == [200, 100, 50, 25] and 12 / 4 == 3 and 25 / 200 == 1 / 8 == 0.5 ** 3
assert 3200 / 100 == 32 == 2 ** 5 and 5 * 3 == 15 and [100 * 2 ** k for k in range(6)][-1] == 3200 and 100 * 2 ** 10 == 102400
assert 1 + 3 == 4 and 1 * 3 == 3 and 3 ** 0 == 1 and 1 - 4 + 3 == 0 and 9 - 12 + 3 == 0


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 140, COR), ("situações", "g", 120)], W / 2, 290, "center")
    E.frase(c, t, C["s01.a"] + 1.0, ps("criadas para esta aula", "i", 64, TINTA2), W / 2, 400, "center")
    for i, nome in enumerate(("máquina", "remédio", "colônia", "equação")):
        X = 420 + i * 360
        t0 = C["s01.a"] + 1.4 + 0.25 * i
        E.foco(c, t, t0, 0.5, lambda a, i=i, X=X: (E.bola(c, X, 560, 62, a=a),
                                                   centro(c, str(i + 1), X, 585, 70, "g", BR, a)))
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, X=X, nome=nome: centro(c, nome, X, 700, 56, "i", TINTA, a), sobe=6)
    for i, (nome, X) in enumerate((("crescimento", 600), ("meia-vida", 960), ("equação", 1320))):
        E.foco(c, t, C["s01.b"] + 0.45 * i, 0.4, lambda a, nome=nome, X=X: E.pilula(c, nome, X, 820, 50, "g", fundo=TINTA, a=a), sobe=6)
    E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "pause e resolva antes da resposta", W / 2, 960, 56, "g", a=a))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 80, TINTA, C["s02"]), ("vai", "i", 80, TINTA, C["s02"] + 0.2), ("usar", "i", 80, TINTA, C["s02"] + 0.4),
                   ("4", "g", 88, COR, C["s02"] + 0.6), ("ferramentas", "i", 80, TINTA, C["s02"] + 0.8)], W / 2, 200, "center")
    itens = (("s02.a", lambda a, y: (fx(c, [("Q = Q", SAI), ("_0", SAI), (" · fator", COR), ("^t", ENT)], 430, y, 84, a),
                                     E.escreve(c, "fator na base, tempo no expoente", 1050, y, 50, "i", TINTA2, a))),
             ("s02.b", lambda a, y: (fx(c, [("t ÷ T", ENT)], 430, y, 84, a),
                                     E.escreve(c, "quantas meias-vidas ou dobras", 1050, y, 50, "i", TINTA2, a))),
             ("s02.c", lambda a, y: (fx(c, [("2", SAI), ("^x", ENT), (" = 2", SAI), ("^5", ENT), ("  →  x = 5", SAI)], 430, y, 84, a),
                                     E.escreve(c, "igualar as bases", 1050, y, 50, "i", TINTA2, a))),
             ("s02.d", lambda a, y: (fx(c, [("3", SAI), ("^x", ENT), (" = y", COR)], 430, y, 84, a),
                                     E.escreve(c, "o apelido", 1050, y, 50, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 400 + i * 175
        numero_item(c, t, C[k], i + 1, 300, y + 4, 50)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- situação 1: a máquina ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.b"], [("máquina", "i", 76), ("de", "i", 76), ("R$ 80.000", "g", 92)], XE, 380)
    E.frase(c, t, C["s03.c"], [("perde", "i", 76), ("20%", "g", 92, ERRADO), ("ao", "i", 76), ("ano", "i", 76)], XE, 510)
    E.frase(c, t, C["s03.d"], [("a)", "g", 64, COR), ("a", "i", 60), ("lei", "g", 64), ("do", "i", 60), ("valor;", "i", 60), ("cresce", "g", 64),
                               ("ou", "i", 60), ("decresce?", "g", 64)], XE, 700)
    E.frase(c, t, C["s03.e"], [("b)", "g", 64, COR), ("o", "i", 60), ("valor", "i", 60), ("depois", "i", 60), ("de", "i", 60),
                               ("2", "g", 64), ("anos", "i", 60)], XE, 830)
    pausa(c, t, C, "s04")


PV = E.Plano(1250, 220, 560, 560, 0, 5, 0, 80)


def b_resposta1(c, t, C, b):
    def contas():
        E.foco(c, t, C["s05.a"], 0.5, lambda a: fx(c, [("− 20%  →  × 0,8", SAI)], XE, 230, 84, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: fx(c, [("V = 80.000 · 0,8", SAI), ("^t", ENT)], XE, 420, 96, a))
        nota(c, t, C["s05.b"] + 1.6, "t em anos", 920, 500, 38, fundo=TINTA)
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "0 < 0,8 < 1: decresce", 500, 580, 48, "g", a=a))
        E.foco(c, t, C["s06.a"], 0.5, lambda a: fx(c, [("0,8", SAI), ("^2", ENT), (" = 0,64", SAI)], XE, 760, 84, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: fx(c, [("80.000 · 0,64 = ", SAI), ("51.200", CERTO)], XE, 920, 80, a))
        E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: E.selo(c, 1140, 895, 34, True, a))
        eixos(c, t, PV, C["s05.b"], C["s05.b"], C["s05.b"], passo_y=20, nomes=("t", "V (mil)"))
        E.curva(c, t, C["s05.c"] - 0.4, PV, maquina, 0, 5, d=1.2, cor=COR, rotulo="80 · 0,8^t", em=(3.3, 50))
        E.ponto(c, t, C["s06.b"], PV, 2, 51.2, guias=True, cor=CERTO, r=14)
        E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: fx(c, [("51,2", CERTO)], PV.x(2) - 120, PV.y(51.2) - 22, 44, a))
    E.saida(c, t, C["s07"] - 0.1, contas)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("cuidado com a conta apressada", "i", 66, TINTA2), XE, 190)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: fx(c, [("20% + 20% = 40%", ERRADO)], XE, 340, 84, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: fx(c, [("80.000 − 40% = 48.000", ERRADO)], XE, 480, 84, a))
    risca(c, t, C["s07.b"] + 1.4, XE - 10, XE + 1010, 452)
    nota(c, t, C["s07.b"] + 1.4, "errado", 1330, 455, 46, fundo=ERRADO)
    XS = [360, 960, 1560]
    linha_valores(c, t, XS, ["80.000", "64.000", "51.200"], [C["s07.c"] - 0.6, C["s07.c"], C["s07.c"] + 1.6], 800, 84)
    saltos(c, t, XS, 700, ["− 20% de 80.000", "− 20% de 64.000"], [C["s07.c"] - 0.4, C["s07.c"] + 1.0], cor=COR, size=34, bojo=50, folga=150)
    E.foco(c, t, C["s07.c"] + 2.0, 0.4, lambda a: E.selo(c, 1810, 770, 34, True, a))
    E.foco(c, t, C["s07.c"] + 1.2, 0.4, lambda a: E.escreve(c, "a cada ano, 20% do que sobrou", 960 - 430, 940, 52, "i", TINTA2, a))


# ---------------- situação 2: o remédio ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s08.a"], 2)
    E.frase(c, t, C["s08.b"], [("200", "g", 92, COR), ("mg", "i", 76), ("de", "i", 76), ("remédio", "i", 76)], XE, 380)
    E.frase(c, t, C["s08.c"], [("meia-vida:", "i", 76), ("4", "g", 92, COR), ("horas", "i", 76)], XE, 510)
    E.frase(c, t, C["s08.d"], [("a)", "g", 64, COR), ("quanto", "i", 60), ("resta", "g", 64), ("em", "i", 60), ("12", "g", 64), ("horas?", "i", 60)],
            XE, 700)
    E.frase(c, t, C["s08.e"], [("b)", "g", 64, COR), ("por", "i", 60), ("quanto", "i", 60), ("tempo", "i", 60), ("restam", "i", 60),
                               ("mais", "g", 64), ("de", "i", 60), ("25", "g", 64), ("mg?", "i", 60)], XE, 830)
    pausa(c, t, C, "s09")


XL2 = 800


def b_resposta2(c, t, C, b):
    def parte1():
        E.foco(c, t, C["s10.a"], 0.5, lambda a: fx(c, [("12 ÷ 4 = 3", SAI), (" meias-vidas", TINTA2)], XE, 230, 84, a))
        XS = [330, 710, 1090, 1470]
        ts = [C["s10.b"] + 0.5 * i for i in range(4)]
        linha_valores(c, t, XS, ["200", "100", "50", "25"], ts, 520, 96)
        saltos(c, t, XS, 420, ["÷2"] * 3, [x - 0.2 for x in ts[1:]], cor=COR, bojo=44, folga=80)
        E.foco(c, t, ts[-1] + 0.3, 0.4, lambda a: E.pilula(c, "25 mg", 1470, 620, 46, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: fx(c, [("Q = 200 · ", SAI), (HALF, SAI), ("^{t/4}", ENT)], W / 2, 860, 120, a, "center"))
    E.saida(c, t, C["s11"] - 0.1, parte1)
    if t < C["s11"]:
        return
    S = 84
    L = [(HALF, SAI), ("^{t/4}", ENT)]
    eqn_em(c, t, C["s11.a"], [("200 · ", SAI)] + L, [("25", SAI)], 250, S, XL2, ">")
    nota(c, t, C["s11.b"], "÷ 200 nos dois lados", 1450, 225, 38, fundo=TINTA)
    eqn_em(c, t, C["s11.b"] + 0.3, L, [("f{25}{200}", SAI)], 420, S, XL2, ">")
    l2 = eqn(c, L, [("f{25}{200}", SAI)], 420, S, 0, XL2, ">")
    E.foco(c, t, C["s11.c"], 0.5, lambda a: fx(c, [(" = f{1}{8}", SAI)], l2[1][0][0] + l2[1][1][0] + 10, 420, S, a))
    l3 = eqn(c, L, [(HALF, SAI), ("^3", ENT)], 590, S, 0, XL2, ">")
    eqn_em(c, t, C["s11.d"], L, [(HALF, SAI), ("^3", ENT)], 590, S, XL2, ">")
    if t < C["s12"]:
        return
    nota(c, t, C["s12.a"], "base 1/2: o sinal vira", 1450, 560, 38)
    iguala(c, t, C["s12.b"], l3, S, 1, 1, 590, [("f{t}{4}", ENT)], [("3", ENT)], 770, S, XL2, op="<", cor_op=COR)
    if t >= C["s12.b"] + 0.9:
        E.foco(c, t, C["s12.b"] + 0.9, 0.4, lambda a: c.drawCircle(XL2, 770 - S * 0.33, S * 0.46, M.paint(COR, a, stroke=5)))
    eqn_em(c, t, C["s12.c"], [("t", ENT)], [("12", ENT)], 920, S, XL2, "<", COR)
    vx = E.reta(c, t, C["s12.d"] - 0.4, 1260, 1780, 830, 0, 16, [0, 4, 8, 12, 16], E._num, size=40)
    E.intervalo(c, t, C["s12.d"], vx, 830, 0, 12, fecha_ini=True, fecha_fim=False)
    E.foco(c, t, C["s12.d"] + 0.5, 0.4, lambda a: E.pilula(c, "as primeiras 12 horas", 1520, 990, 42, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s12.d"] - 0.2, 0.4, lambda a: E.escreve(c, "horas", 1790, 790, 40, "i", TINTA2, a))
    E.foco(c, t, C["s12.d"] + 2.6, 0.4, lambda a: E.escreve(c, "na hora 12: 25 mg", 1300, 720, 44, "i", TINTA2, a))


# ---------------- situação 3: a colônia ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s13.a"], 3)
    E.frase(c, t, C["s13.b"], [("100", "g", 92, COR), ("bactérias", "i", 76)], XE, 380)
    E.frase(c, t, C["s13.c"], [("dobra", "g", 84), ("a", "i", 76), ("cada", "i", 76), ("3", "g", 92, COR), ("horas", "i", 76)], XE, 510)
    E.frase(c, t, C["s13.d"], [("em", "i", 64), ("quantas", "i", 64), ("horas", "g", 68), ("chega", "i", 64), ("a", "i", 64),
                               ("3.200?", "g", 72, COR)], XE, 720)
    pausa(c, t, C, "s14")


XI3 = 900


def b_resposta3(c, t, C, b):
    S = 100
    P = [("2", SAI), ("^{t/3}", ENT)]
    eqn_em(c, t, C["s15.a"], [("100 · ", SAI)] + P, [("3.200", SAI)], 260, S, XI3)
    nota(c, t, C["s15.b"], "÷ 100", 1500, 230, 40, fundo=TINTA)
    eqn_em(c, t, C["s15.b"] + 0.3, P, [("32", SAI)], 430, S, XI3)
    l3 = eqn(c, P, [("2", SAI), ("^5", ENT)], 600, S, 0, XI3)
    eqn_em(c, t, C["s15.c"], P, [("2", SAI), ("^5", ENT)], 600, S, XI3)
    q = ep(t, C["s15.c"] + 0.8, 0.4)
    caixa_base(c, l3[0], 0, 600, S, q)
    caixa_base(c, l3[1], 0, 600, S, q)
    iguala(c, t, C["s16.a"], l3, S, 1, 1, 600, [("f{t}{3}", ENT)], [("5", ENT)], 790, S, XI3)
    nota(c, t, C["s16.b"], "× 3", 1300, 760, 40, fundo=TINTA)
    E.foco(c, t, C["s16.b"] + 0.3, 0.5, lambda a: (eqn(c, [("t", ENT)], [("15 h", CERTO)], 960, S, a, XI3), E.selo(c, 1300, 925, 36, True, a)))


# ---------------- atalho (palco escuro) ----------------
XD = [230, 530, 830, 1130, 1430, 1730]


def b_atalho(c, t, C, b):
    palco(c, t)

    def s17():
        E.frase(c, t, C["s17"], ps("o atalho:", "i", 70, CLARO), XE, 190)
        E.frase(c, t, C["s17.a"], [("conte", "g", 110, BR), ("as", "i", 100, BR), ("dobras", "g", 110, BR)], XE, 340)
        ts = [C["s17.b"] + 0.5 * i for i in range(6)]
        linha_valores(c, t, XD, ["100", "200", "400", "800", "1.600", "3.200"], ts, 600, 70, BR)
        saltos(c, t, XD, 510, ["×2"] * 5, [x - 0.2 for x in ts[1:]], cor=CLARO, bojo=40, folga=60)
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "5 dobras", 560, 790, 60, "g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, C["s17.d"], 0.5, lambda a: fx(c, [("5 · 3 = ", BR), ("15 h", CLARO)], 960, 815, 100, a))
        if t >= C["s18.a"]:
            for i, X in enumerate(XD):
                E.foco(c, t, C["s18.a"] + 0.15 * i, 0.4, lambda a, i=i, X=X: fx(c, [("2", BR), ("^" + str(i), CLARO)], X, 690, 56, a, "center"), sobe=6)
    E.saida(c, t, C["s18.b"] - 1.8, s17)
    if t < C["s18.b"] - 1.8:
        return
    E.frase(c, t, C["s18.b"] - 1.7, [("não", "g", 80, BR), ("compensa", "i", 74, CLARO), ("com", "i", 74, CLARO), ("muitas", "g", 80, BR),
                                     ("dobras", "g", 80, BR)], XE, 220)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: fx(c, [("100  →  102.400", BR)], XE, 430, 100, a))
    E.foco(c, t, C["s18.b"] + 1.4, 0.5, lambda a: E.pilula(c, "10 linhas de conta", 1300, 400, 52, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: fx(c, [("2", BR), ("^{t/3}", CLARO), (" = 1.024 = 2", BR), ("^{10}", CLARO)], XE, 660, 100, a))
    E.foco(c, t, C["s18.c"] + 0.4, 0.4, lambda a: E.pilula(c, "iguale as bases", 560, 820, 56, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- situação 4: a troca de variável ----------------
EQ4 = [("9", SAI), ("^x", ENT), (" − 4 · 3", SAI), ("^x", ENT), (" + 3 = 0", SAI)]


def b_questao4(c, t, C, b):
    situacao(c, t, C["s19.a"], 4, "última situação")
    fx_em(c, t, C["s19.b"], EQ4, XE, 560, 110)
    pausa(c, t, C, "s20")


def b_resposta4(c, t, C, b):
    S = 96

    def tela1():
        w, xs, ws = fx(c, EQ4, XE, 0, S, 0)
        fx_em(c, t, C["s21"], EQ4, XE, 230, S)
        apelido(c, t, C["s21.b"], [("3", SAI), ("^x", ENT)], xs[2] + E.larg(" − 4 · ", "g", S) + S * 0.02 * 3, 230, S)
        E.foco(c, t, C["s21.a"], 0.5, lambda a: fx(c, [("9", SAI), ("^x", ENT), (" = (3", SAI), ("^x", ENT), (")", SAI), ("^2", ENT),
                                                       (" = y²", COR)], XE, 470, 84, a))
        E.foco(c, t, C["s21.c"], 0.5, lambda a: fx(c, [("y² − 4y + 3 = 0", COR)], XE, 630, 96, a))
        E.foco(c, t, C["s22.a"], 0.5, lambda a: (fx(c, [("y = 1  ou  y = 3", COR)], XE, 800, 90, a),
                                                 E.escreve(c, "soma 4, produto 3", XE + 80, 890, 46, "i", TINTA2, a)))
        E.foco(c, t, C["s22.b"], 0.5, lambda a: fx(c, [("3", SAI), ("^x", ENT), (" = 3  →  ", SAI), ("x = 1", ENT)], 1130, 470, 84, a))
        E.foco(c, t, C["s22.c"], 0.5, lambda a: fx(c, [("3", SAI), ("^x", ENT), (" = 1 = 3", SAI), ("^0", ENT)], 1130, 630, 84, a))
        E.foco(c, t, C["s22.d"], 0.5, lambda a: fx(c, [("→  ", SAI), ("x = 0", ENT)], 1300, 790, 84, a))
        nota(c, t, C["s22.d"] + 0.3, "expoente zero dá 1", 1500, 900, 38, fundo=TINTA)
    E.saida(c, t, C["s23"] - 0.1, tela1)
    if t < C["s23"]:
        return
    E.foco(c, t, C["s23.a"], 0.5, lambda a: fx(c, [("y = 1 > 0   e   y = 3 > 0", SAI)], XE, 250, 84, a))
    nota(c, t, C["s23.a"] + 1.0, "nenhuma raiz se descarta", 1450, 230, 42, fundo=CERTO)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: (fx(c, [("x = 0:  ", ENT), ("1 − 4 + 3 = 0", SAI)], XE, 480, 84, a), E.selo(c, 1000, 455, 36, True, a)))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: (fx(c, [("x = 1:  ", ENT), ("9 − 12 + 3 = 0", SAI)], XE, 650, 84, a), E.selo(c, 1000, 625, 36, True, a)))
    E.foco(c, t, C["s23.c"] + 2.2, 0.5, lambda a: E.pilula(c, "x = 0  ou  x = 1", W / 2, 870, 70, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s24.a", [("o", "i", 72), ("fator", "g", 76, COR), ("na", "i", 72), ("base,", "i", 72), ("o", "i", 72), ("tempo", "g", 76, ENT),
                            ("no", "i", 72), ("expoente", "i", 72)]),
                 ("s24.b", [("iguale", "g", 76), ("as", "i", 72), ("bases", "i", 72), ("para", "i", 72), ("achar", "i", 72), ("o", "i", 72),
                            ("expoente", "g", 76, COR)]),
                 ("s24.c", [("confira", "g", 76, CERTO), ("se", "i", 72), ("a", "i", 72), ("resposta", "i", 72), ("faz", "i", 72), ("sentido", "g", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            numero_item(c, t, C[k], i + 1, 300, y + 4, 56)
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 230)
    E.foco(c, t, C["s25.a"], 0.5, lambda a: fx(c, [("2", SAI), ("^?", ENT), (" = 8", SAI)], XE, 420, 120, a))
    E.frase(c, t, C["s25.b"], [("logaritmo", "g", 130, COR)], XE, 610)
    E.foco(c, t, C["s25.b"] + 1.2, 0.5, lambda a: fx(c, [("log", SAI), ("_2", SAI), (" 8 = ", SAI), ("3", ENT), ("   ⇔   2", SAI), ("^3", ENT),
                                                         (" = 8", SAI)], XE, 790, 90, a))
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(790, 495, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
