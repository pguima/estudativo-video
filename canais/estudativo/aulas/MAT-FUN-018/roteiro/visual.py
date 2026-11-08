"""Visual — Estudativo · MAT-FUN-018: vértice da parábola.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016 e 017: na lei, o a em índigo, o b em cinza e o c em preto; parábola de a > 0 índigo, de a < 0 preta; raízes como
círculos índigo no eixo x. Nesta aula: o vértice é a esfera amarela (VERT) com anel; o eixo de simetria é a reta tracejada em pé;
os pares simétricos se ligam por uma ponte tracejada; a imagem é a faixa preta pintada sobre o eixo y (é saída), com a ponta
fechada (bolinha cheia) no y do vértice e a seta no infinito.
Peças locais: eixos(), par(), anel(), marca_ponto(), lei(), sob_parte(), raiz(), vertice(), eixo_sim(), faixa_imagem()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
CA, CB, CC = COR, TINTA2, TINTA  # cores de a, b e c
ARQUIVO_FINAL = "estudativo_MAT-FUN-018_vertice_da_parabola.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("simetria", "media", "formula", "imagem", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"

f = lambda x: x * x - 4 * x + 3
p15 = lambda x: (x - 1) * (x - 5)
q = lambda x: -x * x + 6 * x - 5
assert [f(x) for x in (0, 1, 2, 3, 4)] == [3, 0, -1, 0, 3] and (1 + 3) / 2 == 2 and 4 - 8 + 3 == -1 and 4 / 2 == 2
assert p15(1) == p15(5) == 0 and (1 + 5) / 2 == 3
assert -6 / -2 == 3 and q(3) == 4 and -9 + 18 - 5 == 4 and q(1) == 0 and q(5) == 0 and -25 + 30 - 5 == 0

PL = (1080, 190, 700, 700)
P = E.Plano(*PL, -1.5, 5.5, -2, 5)
MP = ([-1, 0, 1, 2, 3, 4, 5], [-2, -1, 0, 1, 2, 3, 4, 5])
PQ = E.Plano(*PL, -0.5, 6.5, -4, 6)
MQ = ([0, 1, 2, 3, 4, 5, 6], [-4, -2, 0, 2, 4, 6])
LEI_F = [("f(x) = ", TINTA), ("x^2", CA), (" − 4x", CB), (" + 3", CC)]
def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


def eixos(c, t, P, tx, ty=None, tg=None, marcas=None, size=38, rot=True, rx=None, ry=None, fmt=E._num):
    """plano em etapas (o da MAT-FUN-001): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    mx, my = marcas
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(mx):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                rot and (rx is None or v in rx) and centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(my):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                rot and (ry is None or v in ry) and E.escreve(c, fmt(v), P.ox - 20 - E.larg(fmt(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)),
                sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anel(c, t, t0, X, Y, cor=None, d=0.9):
    p = prog(t, t0, d)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def marca_ponto(c, t, t0, X, Y, cor, r=26):
    q = ease_back(prog(t, t0, 0.5))
    if q > 0:
        c.drawCircle(X, Y, r * q, M.paint(cor, 0.22))
        c.drawCircle(X, Y, r * q, M.paint(cor, 1.0, stroke=6))
    anel(c, t, t0, X, Y, cor)


def tabela(c, t, x, y, cab, cores, linhas, tc, tcel, wc=200, hl=86, size=60, destaque=None, cab_size=50):
    """tabela em pé: cab = cabeçalhos (escrita de fórmula), tcel[i][j] = instante de cada célula (None = vazia)"""
    n = len(cab)
    a = ep(t, tc, 0.5)
    if a > 0:
        for j, (h_, cor) in enumerate(zip(cab, cores)):
            E.formula(c, h_, x + wc * j + wc / 2, y - 24, cab_size, "b" if j else "g", cor, a, "center")
        M.line(c, x, y, x + n * wc, y, TINTA, a, 4)
        for j in range(1, n):
            M.line(c, x + wc * j, y, x + wc * j, y + hl * len(linhas) + 10, TINTA, a, 4)
    for i, row in enumerate(linhas):
        ry = y + 10 + hl * i
        if destaque is not None:
            q = destaque(i)
            if q > 0:
                M.rrect(c, x - 8, ry + 4, n * wc + 16, hl - 8, 14, COR, 0.14 * q)
        for j, v in enumerate(row):
            t0 = tcel[i][j]
            if t0 is None:
                continue
            E.foco(c, t, t0, 0.4, lambda q, v=v, j=j, ry=ry: centro(c, v, x + wc * j + wc / 2, ry + hl / 2 + size * 0.36, size, "g", cores[j], q), sobe=6)


def lei(c, partes, x, y, size, a=1.0, align="left"):
    """lei escrita por partes [(texto, cor)]; devolve [(x0, x1)] de cada parte"""
    w = sum(larg_f(s, size) for s, _ in partes)
    xx = x - w / 2 if align == "center" else x
    pos = []
    for s, cor in partes:
        lw = larg_f(s, size)
        if a > 0:
            E.formula(c, s, xx, y, size, "g", cor, a)
        pos.append((xx, xx + lw))
        xx += lw
    return pos


def lei_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: lei(c, partes, x, y, size, a, align))
    return lei(None, partes, x, y, size, 0, align)


def sob_parte(c, t, t0, pos, i, y, rot, cor, size=50, apara=0):
    """chave sob a parte i da lei (pos = o que lei() devolveu) com o rótulo embaixo; apara corta o sinal da esquerda"""
    x0, x1 = pos[i]
    x0 += apara
    p = ep(t, t0, 0.5)
    if p > 0:
        E.chave(c, x0 + 6, x1 - 2, y + 28, cor, p, 22, 5)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, (x0 + x1) / 2, y + 28 + 22 + size + 6, size, "g", cor, a, "center"))


def mini(c, t, t0, x, y, w, h, fn, a_, b_, cor, escuro=False, d=0.9, ymin=-3, ymax=3):
    """mini-gráfico sem números (E.plano sem grade nem rótulos) com a curva fn de a_ até b_"""
    Q = E.plano(c, t, t0, x, y, w, h, -3, 3, ymin, ymax, grade=False, rotulos=False, size=30, d=0.5, escuro=escuro)
    E.curva(c, t, t0 + 0.3, Q, fn, a_, b_, d=d, largura=8, cor=cor)
    return Q




def fsub(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """E.formula com índice no começo: "x_v = f{−b}{2a}" escreve x com o v pequeno embaixo"""
    if not s.startswith("x_"):
        return E.formula(c, s, x, y, size, estilo, cor, a, align)
    sub, rest = s[2], s[3:]
    wx, ws, wr = E.larg("x", estilo, size), E.larg(sub, estilo, size * 0.55), larg_f(rest, size)
    w = wx + ws + size * 0.06 + wr
    if a <= 0 or c is None:
        return w
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    E.escreve(c, "x", x0, y, size, estilo, cor or TINTA, a)
    E.escreve(c, sub, x0 + wx + size * 0.02, y + size * 0.2, size * 0.55, estilo, cor or TINTA, a)
    E.formula(c, rest, x0 + wx + ws + size * 0.06, y, size, estilo, cor or TINTA, a)
    return w


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fsub(c, s, x, y, size, "g", cor, a, align))


def plano(c, t, t0, P_=None, marcas=None):
    eixos(c, t, P_ or P, t0, tg=t0, marcas=marcas or MP, size=36)


def caixa_par(c, P_, xv, yv, X, Y, size, a, align="left"):
    """par com fundo de papel (legível sobre a grade e a curva)"""
    w = par(None, xv, yv, 0, 0, size, 0)
    x0 = X - w / 2 if align == "center" else X - w if align == "right" else X
    M.rrect(c, x0 - 10, Y - size * 0.95, w + 20, size * 1.3, 12, "#F4F3EF", 0.92 * a)
    par(c, xv, yv, x0, Y, size, a)


def raiz(c, t, t0, P_, xv, rot=True, size=42, lado=1):
    if t < t0:
        return
    marca_ponto(c, t, t0, P_.x(xv), P_.oy, ENT, 20)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, P_, E._num(xv), "0", P_.x(xv) + (24 if lado > 0 else -24), P_.oy - 32, size, a,
                                                          "left" if lado > 0 else "right"))


def vertice(c, t, t0, P_, xv, yv, rot=None, size=44, abaixo=True):
    """o vértice: esfera amarela com anel, e o par embaixo (ou em cima)"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        X, Y = P_(xv, yv)
        c.drawCircle(X, Y, 19 * k, M.paint(VERT))
        c.drawCircle(X, Y, 19 * k, M.paint(TINTA, 1.0, stroke=4))
        anel(c, t, t0, X, Y, VERT)
        if rot:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, P_, rot[0], rot[1], X, Y + (78 if abaixo else -36), size, a, "center"))


def eixo_sim(c, t, t0, P_, xv, cor=TINTA, a=1.0):
    p = ep(t, t0, 0.8)
    if p > 0 and a > 0:
        x, y, w, h_ = P_.caixa
        X = P_.x(xv)
        M.line(c, X, y + h_ + 10, X, lerp(y + h_ + 10, y - 20, p), cor, a, 5, dash=[18, 12])


def ponte_sim(c, t, t0, P_, x1, x2, yv, cor=COR):
    """dois pontos simétricos ligados por uma ponte tracejada"""
    p = ep(t, t0, 0.6)
    if p > 0:
        M.line(c, P_.x(x1), P_.y(yv), P_.x(x2), P_.y(yv), cor, 0.8, 4, dash=[12, 10], progress=p)
    for xv in (x1, x2):
        E.ponto(c, t, t0, P_, xv, yv, cor=cor, r=15)


def faixa_imagem(c, t, t0, P_, y0, para_cima=True, cor=SAI, a=1.0):
    """imagem como faixa sobre o eixo y: fechada em y0 (bolinha cheia) e indo até a borda com seta"""
    p = ease_io(prog(t, t0, 0.9))
    if p <= 0 or a <= 0:
        return
    x, y, w, h_ = P_.caixa
    Y0 = P_.y(y0)
    Yf = y - 30 if para_cima else y + h_ + 30
    Y1 = lerp(Y0, Yf, p)
    M.line(c, P_.ox, Y0, P_.ox, Y1, cor, 0.3 * a, 16)
    M.arrow(c, P_.ox + 28, Y0, P_.ox + 28, Y1, cor, a, 7, 22, 1.0)
    c.drawCircle(P_.ox + 28, Y0, 13, M.paint(cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano(c, t, C["s01"])
        lei_em(c, t, C["s01.a"], LEI_F, XE, 260, 90)
        E.curva(c, t, C["s01.a"] + 0.3, P, f, -0.5, 4.5, d=2.4, cor=COR)
        p = ep(t, C["s01.a"] + 0.4, 0.5) * (1 - ep(t, C["s01.c"], 0.4))
        if p > 0:
            M.arrow(c, *P(-0.1, 4.2), *P(0.9, 1.0), TINTA2, p, 6, 22, p)
            M.arrow(c, *P(3.1, 1.0), *P(4.1, 4.2), TINTA2, p * ep(t, C["s01.b"] + 0.6, 0.4), 6, 22, p)
        E.frase(c, t, C["s01.a"] + 0.5, [("desce,", "i", 70)], XE, 420)
        E.frase(c, t, C["s01.b"], [("faz", "i", 70), ("a", "i", 70), ("curva", "g", 70, COR)], XE + 240, 420)
        E.frase(c, t, C["s01.b"] + 0.8, [("e", "i", 70), ("sobe", "i", 70)], XE, 520)
        vertice(c, t, C["s01.c"], P, 2, -1)
        E.frase(c, t, C["s01.c"], [("o", "i", 110), ("vértice", "g", 120, COR)], XE, 700)
        E.frase(c, t, C["s01.c"] + 1.2, ps("altura máxima, lucro máximo, menor custo", "i", 44, TINTA2), XE, 790, passo=0.1)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "sem desenhar", XE + 200, 900, 50, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.2, [("o", "i", 100), ("vértice", "g", 120, COR)], XE, 460)
        E.frase(c, t, C["s02.a"] + 2.2, [("de", "i", 90), ("2", "g", 100), ("maneiras", "i", 90)], XE, 600)
        E.frase(c, t, C["s02.a"] + 3.4, [("+", "g", 90, COR), ("a", "i", 90), ("imagem", "g", 100)], XE, 750)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.a", "as raízes (corta o eixo x):", lambda a, y: (E.escreve(c, "x = 1  e  x = 3", x + 44, y, 66, "g", ENT, a))),
             ("s03.b", "a imagem, como intervalo:", lambda a, y: (E.escreve(c, "[0, +∞[", x + 44, y, 66, "g", SAI, a),
                                                                E.escreve(c, "as saídas", x + 340, y, 56, "i", TINTA2, a))))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q_ = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q_), ep(t, C["s03.a"], 0.4))


# ---------------- simetria ----------------
def tab_sim(c, t, t0, ta, tb, tc):
    """tabela deitada x | f(x), com os pares que se repetem ligados"""
    xs = (0, 1, 2, 3, 4)
    x0, w_ = XE + 120, 130
    y1, y2 = 330, 450
    a = ep(t, t0, 0.5)
    if a > 0:
        E.escreve(c, "x", XE, y1, 60, "g", ENT, a)
        E.formula(c, "f(x)", XE - 40, y2, 52, "g", SAI, a)
        M.line(c, XE - 40, (y1 + y2) / 2 - 22, x0 + w_ * 5, (y1 + y2) / 2 - 22, TINTA, a * 0.6, 3)
        for i, xv in enumerate(xs):
            centro(c, str(xv), x0 + w_ * i + w_ / 2, y1, 64, "g", ENT, a)
            centro(c, E._num(f(xv)), x0 + w_ * i + w_ / 2, y2, 64, "g", SAI, a)
    for k, (i, j, tk) in enumerate(((0, 4, ta), (1, 3, tb))):
        p = ep(t, tk, 0.6)
        if p > 0:
            xa, xb = x0 + w_ * i + w_ / 2, x0 + w_ * j + w_ / 2
            E.arco(c, (xa + xb) / 2, y2 + 30, (xb - xa) / 2, 0, 180 * p, COR, 5)
    p = ep(t, tc, 0.4)
    if p > 0:
        X = x0 + w_ * 2 + w_ / 2
        M.rrect(c, X - 50, y1 - 70, 100, y2 - y1 + 110, 20, VERT, 0.3 * p)


def b_simetria(c, t, C, b):
    plano(c, t, C["s04"])
    E.curva(c, t, C["s04"] + 0.3, P, f, -0.5, 4.5, d=1.0, cor=COR)
    E.frase(c, t, C["s04"], ps("olhe a tabela", "i", 70), XE, 200)
    tab_sim(c, t, C["s04"] + 0.4, C["s04.a"] + 0.6, C["s04.b"] + 0.6, C["s04.c"])
    ponte_sim(c, t, C["s04.a"], P, 0, 4, 3)
    ponte_sim(c, t, C["s04.b"], P, 1, 3, 0)
    E.frase(c, t, C["s04.c"], [("em", "i", 64), ("volta", "i", 64), ("do", "i", 64), ("2", "g", 70, ENT)], XE, 600)
    if t < C["s05"]:
        return
    eixo_sim(c, t, C["s05.b"], P, 2)
    vertice(c, t, C["s05.end"] - 2.0, P, 2, -1)
    p = ep(t, C["s05.b"] + 0.6, 0.5)
    if p > 0:
        for d_ in (1, -1):
            E.arco(c, P.x(2), P.y(4.3), 60, -90 + 40 * d_, 30 * d_ * p, TINTA2, 4)
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "simétrica", XE + 160, 730, 54, "g", fundo=COR, a=a))
    E.frase(c, t, C["s05.c"], [("eixo", "g", 70), ("de", "i", 66), ("simetria", "g", 70)], XE, 850)
    E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: E.formula(c, "x = 2", XE + 600, 850, 60, "g", ENT, a))


# ---------------- média das raízes ----------------
def b_media(c, t, C, b):
    plano(c, t, C["s06"] - 3)
    E.curva(c, t, C["s06"] - 3, P, f, -0.5, 4.5, d=0.05, cor=COR)
    eixo_sim(c, t, C["s06"] - 3, P, 2, a=0.6)
    raiz(c, t, C["s06.a"], P, 1, lado=-1)
    raiz(c, t, C["s06.a"] + 0.3, P, 3)
    def meio():
        p = ep(t, C["s06.c"] + 1.0, 0.6)
        if p > 0:
            E.chave(c, P.x(1), P.x(3), P.oy + 70, ENT, p, 22, 5)
            E.foco(c, t, C["s06.c"] + 1.2, 0.4, lambda a: E.pilula(c, "meio: 2", P.x(2), P.oy + 150, 40, "g", fundo=ENT, a=a))
    E.saida(c, t, C["s07"] - 0.1, meio)

    def s06():
        E.frase(c, t, C["s06.a"], [("x", "g", 76, ENT), ("do", "i", 70), ("vértice:", "i", 70), ("no", "i", 70), ("meio", "g", 70, COR)], XE, 220)
        E.frase(c, t, C["s06.a"] + 1.2, ps("das raízes", "i", 70), XE, 310)
        E.frase(c, t, C["s06.b"], [("média:", "g", 66), ("some", "i", 64), ("e", "i", 64), ("÷", "g", 66), ("2", "g", 66)], XE, 450)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: fsub(c, "x_v = f{1 + 3}{2} = f{4}{2} = 2", XE, 640, 80, "g", ENT, a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07"], 0.4, lambda a: E.formula(c, "x = 2", XE, 220, 70, "g", ENT, a))
    E.frase(c, t, C["s07"] + 0.4, [("e", "i", 66), ("o", "i", 66), ("y", "g", 70), ("do", "i", 66), ("vértice?", "i", 66)], XE + 260, 220)
    fml(c, t, C["s07.a"], "f(2) = 2^2 − 4 · 2 + 3", XE, 360, 72, TINTA)
    fml(c, t, C["s07.b"], "= 4 − 8 + 3 = −1", XE + 120, 470, 72, TINTA)
    vertice(c, t, C["s07.c"], P, 2, -1, ("2", "−1"))
    E.frase(c, t, C["s07.c"], [("vértice:", "i", 70)], XE, 630)
    E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: par(c, "2", "−1", XE + 270, 630, 76, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "a > 0: o mais baixo, o mínimo", XE + 340, 780, 46, "g", fundo=COR, a=a))


# ---------------- fórmula ----------------
def b_formula(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], [("e", "i", 80), ("sem", "i", 80), ("raízes?", "g", 80, ERRADO)], W / 2, 300, "center")
        E.foco(c, t, C["s08.a"], 0.6, lambda a: (M.rrect(c, W / 2 - 360, 460, 720, 260, 50, COR, a),
                                                 fsub(c, "x_v = f{−b}{2a}", W / 2, 630, 130, "g", BR, a, "center")))
        E.frase(c, t, C["s08.a"] - 1.6, ps("sempre funciona", "i", 60, TINTA2), W / 2, 850, "center")
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09"], ps("ela sai da Bhaskara", "i", 70), XE, 200)
            fml(c, t, C["s09.a"], "x_1 = f{−b + r{Δ}}{2a}", XE, 360, 76, TINTA)
            fml(c, t, C["s09.a"] + 1.2, "x_2 = f{−b − r{Δ}}{2a}", XE + 760, 360, 76, TINTA)
            E.foco(c, t, C["s09.b"] - 1.0, 0.4, lambda a: E.escreve(c, "some as duas:", XE, 540, 56, "i", TINTA2, a))
            fml(c, t, C["s09.b"], "soma = f{−2b}{2a}", XE + 400, 550, 72, TINTA)
            E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.pilula(c, "+√Δ e −√Δ se cancelam", XE + 1180, 525, 40, "g", fundo=ERRADO, a=a))
            E.foco(c, t, C["s09.c"] - 0.6, 0.4, lambda a: E.escreve(c, "÷ 2:", XE, 790, 60, "g", TINTA2, a))
            E.foco(c, t, C["s09.c"], 0.6, lambda a: (M.rrect(c, XE + 180, 670, 560, 200, 46, COR, a),
                                                     fsub(c, "x_v = f{−b}{2a}", XE + 460, 800, 100, "g", BR, a, "center")))
        E.saida(c, t, C["s09.c"] + 3.0, s09)
        # o c nem entra: a parábola sobe e desce e o vértice fica no mesmo x
        tc = C["s09.c"] + 3.4
        if t >= tc:
            E.frase(c, t, tc, [("o", "i", 70), ("c", "g", 80, CC), ("nem", "i", 70), ("entra", "g", 70, ERRADO)], XE, 230)
            fml(c, t, tc + 0.6, "x_v = f{−b}{2a}", XE, 400, 90, COR)
            E.frase(c, t, tc + 2.6, ps("mudar o c: sobe ou desce tudo", "i", 56), XE, 560, passo=0.1)
            E.frase(c, t, tc + 4.6, [("o", "i", 56), ("vértice", "g", 56, COR), ("fica", "i", 56), ("no", "i", 56), ("mesmo", "i", 56), ("x", "g", 62, ENT)], XE, 660)
            E.foco(c, t, C["s09.end"] - 2.6, 0.4, lambda a: E.pilula(c, "vale sem tocar o eixo x", XE + 300, 800, 46, "g", fundo=CERTO, a=a))
            plano(c, t, tc)
            sobe = 2.2 * ease_io(prog(t, tc + 2.6, 1.6)) * (1 - 0.5 * ease_io(prog(t, tc + 5.0, 1.4)))
            g = lambda x: f(x) + sobe
            E.curva(c, t, tc + 0.3, P, g, -0.5, 4.5, d=0.8, cor=COR)
            eixo_sim(c, t, tc + 1.0, P, 2, a=0.7)
            vertice(c, t, tc + 1.0, P, 2, -1 + sobe)
        return
    if t < C["s10"]:
        return
    pos = lei_em(c, t, C["s10"], LEI_F, XE, 220, 80)
    sob_parte(c, t, C["s10.a"], pos, 2, 220, "b = −4", CB, 44)
    fml(c, t, C["s10.a"] + 0.6, "−b = 4", XE, 450, 76, TINTA)
    fml(c, t, C["s10.b"], "2a = 2", XE + 400, 450, 76, CA)
    E.foco(c, t, C["s10.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 540, 640, 190, 46, COR, a),
                                             fsub(c, "x_v = f{4}{2} = 2", XE + 300, 670, 90, "g", BR, a, "center")))
    E.foco(c, t, C["s10.c"] + 1.2, 0.4, lambda a: E.pilula(c, "o mesmo 2 da média", XE + 300, 840, 50, "g", fundo=CERTO, a=a))
    plano(c, t, C["s10"])
    E.curva(c, t, C["s10"] + 0.3, P, f, -0.5, 4.5, d=0.8, cor=COR)
    eixo_sim(c, t, C["s10.c"], P, 2)
    vertice(c, t, C["s10.c"] + 0.6, P, 2, -1, ("2", "−1"))


# ---------------- imagem ----------------
def b_imagem(c, t, C, b):
    plano(c, t, C["s11"] - 3)

    def cima():
        E.curva(c, t, C["s11"] - 3, P, f, -0.5, 4.5, d=0.05, cor=COR)
        vertice(c, t, C["s11"] - 3, P, 2, -1, ("2", "−1"))
        M.line(c, P.x(2), P.y(-1), P.ox, P.y(-1), TINTA, ep(t, C["s11.a"], 0.5), 4, dash=E.TRACO)
        faixa_imagem(c, t, C["s11.b"], P, -1, True)
        E.frase(c, t, C["s11.a"], [("abre", "i", 66), ("para", "i", 66), ("cima", "g", 66, COR), ("a", "i", 66), ("partir", "i", 66), ("do", "i", 66),
                                   ("−1", "g", 72)], XE, 240)
        E.frase(c, t, C["s11.b"], [("saídas:", "i", 66), ("o", "i", 66), ("−1", "g", 72), ("e", "i", 66), ("acima", "g", 66)], XE, 370)
        E.foco(c, t, C["s11.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 450, 620, 170, 44, SAI, a),
                                                 E.formula(c, "Im = [−1, +∞[", XE + 290, 565, 84, "g", BR, a, "center")))
        E.foco(c, t, C["s11.c"] + 1.6, 0.4, lambda a: E.escreve(c, "fechado no −1: a função alcança", XE, 700, 48, "i", TINTA, a))
        E.foco(c, t, C["s11.c"] + 3.0, 0.4, lambda a: E.escreve(c, "aberto no infinito", XE, 780, 48, "i", TINTA2, a))
    E.saida(c, t, C["s12"] - 0.1, cima)
    if t < C["s12"]:
        return
    g = lambda x: -f(x)
    E.curva(c, t, C["s12"] + 0.2, P, g, -0.4, 4.4, d=1.0, cor=TINTA)
    E.frase(c, t, C["s12"], [("a", "g", 72, CA), ("<", "g", 72, CA), ("0:", "g", 72, CA), ("o", "i", 66), ("contrário", "g", 66)], XE, 240)
    vertice(c, t, C["s12.a"], P, 2, 1, ("2", "1"), abaixo=False)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.pilula(c, "o ponto mais alto: o máximo", XE + 330, 380, 46, "g", fundo=TINTA, a=a))
    M.line(c, P.x(2), P.y(1), P.ox, P.y(1), TINTA, ep(t, C["s12.b"], 0.5), 4, dash=E.TRACO)
    faixa_imagem(c, t, C["s12.b"], P, 1, False)
    E.foco(c, t, C["s12.b"] + 0.5, 0.6, lambda a: (M.rrect(c, XE - 20, 470, 680, 170, 44, SAI, a),
                                                   E.formula(c, "Im = ]−∞, 1]", XE + 320, 585, 84, "g", BR, a, "center")))
    E.foco(c, t, C["s12.b"] + 1.2, 0.4, lambda a: E.escreve(c, "até o y do vértice, fechado", XE, 720, 50, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s13"] - 3)
    E.curva(c, t, C["s13"] - 3, P, f, -0.5, 4.5, d=0.05, cor=COR)
    vertice(c, t, C["s13"] - 3, P, 2, -1, ("2", "−1"))
    E.frase(c, t, C["s13.a"], [("o", "i", 70), ("erro:", "i", 70), ("o", "i", 70), ("x", "g", 76, ERRADO), ("na", "i", 70), ("imagem", "g", 70, ERRADO)], XE, 230)

    def errado():
        E.foco(c, t, C["s13.a"] + 1.6, 0.5, lambda a: E.formula(c, "Im = [2, +∞[", XE, 380, 84, "g", ERRADO, a))
        if t >= C["s13.a"] + 3.4:
            E.risco(c, XE - 10, 390, XE + 480, 320, t, C["s13.a"] + 3.4, largura=10)
        faixa_imagem(c, t, C["s13.a"] + 1.8, P, 2, True, ERRADO, 0.9)
    E.saida(c, t, C["s13.b"], errado)
    E.frase(c, t, C["s13.b"], [("imagem", "i", 66), ("é", "i", 66), ("saída:", "i", 66), ("saída", "g", 66), ("é", "i", 66), ("y", "g", 76)], XE, 500)
    E.frase(c, t, C["s13.c"], [("o", "i", 64), ("2", "g", 72, ENT), ("diz", "i", 64), ("onde", "i", 64), ("a", "i", 64), ("curva", "i", 64), ("vira", "g", 64, ENT)], XE, 650)
    E.frase(c, t, C["s13.d"], [("o", "i", 64), ("−1", "g", 72), ("diz", "i", 64), ("até", "i", 64), ("onde", "i", 64), ("desce", "g", 64)], XE, 770)
    eixo_sim(c, t, C["s13.c"], P, 2, ENT)
    M.line(c, P.x(2), P.y(-1), P.ox, P.y(-1), TINTA, ep(t, C["s13.d"], 0.5), 4, dash=E.TRACO)
    faixa_imagem(c, t, C["s13.d"] + 0.4, P, -1, True, CERTO)
    E.foco(c, t, C["s13.d"] + 1.2, 0.4, lambda a: E.formula(c, "Im = [−1, +∞[", XE, 890, 72, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    Q = E.Plano(1120, 230, 640, 640, -0.5, 6.5, -5, 4, escuro=True)

    def graf():
        E.plano(c, t, C["s14.b"], 1120, 230, 640, 640, -0.5, 6.5, -5, 4, marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[-4, -3, -2, -1, 1, 2, 3, 4], escuro=True)
        E.curva(c, t, C["s14.c"] + 0.8, Q, p15, 0.2, 5.8, d=1.0, cor=CLARO)
        for k, xv in enumerate((1, 5)):
            if t >= C["s14.c"] + 0.3 * k:
                marca_ponto(c, t, C["s14.c"] + 0.3 * k, Q.x(xv), Q.oy, AMARELO, 20)
        if t >= C["s14.d"]:
            eixo_sim(c, t, C["s14.d"], Q, 3, CLARO)
            vertice(c, t, C["s14.d"] + 0.5, Q, 3, -4)
    E.saida(c, t, C["s15"] + 0.2, graf)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 200)
        E.frase(c, t, C["s14.a"], [("raízes", "g", 72, BR), ("de", "i", 68, CLARO), ("graça?", "i", 68, CLARO), ("use", "i", 68, CLARO), ("a", "i", 68, CLARO),
                                   ("média", "g", 72, AMARELO)], XE, 330)
        fml(c, t, C["s14.b"], "f(x) = (x − 1)(x − 5)", XE, 490, 86, BR)
        E.frase(c, t, C["s14.b"] + 2.4, ps("produto zero: um fator vale zero", "i", 52, CLARO), XE, 590, passo=0.1)
        E.frase(c, t, C["s14.c"], [("raízes:", "i", 66, CLARO), ("1", "g", 74, AMARELO), ("e", "i", 66, CLARO), ("5", "g", 74, AMARELO)], XE, 710)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: fsub(c, "x_v = f{1 + 5}{2} = 3", XE, 870, 86, "g", BR, a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("o", "i", 70, CLARO), ("vértice", "g", 72, BR), ("fica", "i", 70, CLARO), ("no", "i", 70, CLARO), ("meio", "g", 72, AMARELO),
                             ("das", "i", 70, CLARO), ("raízes", "i", 70, CLARO)], W / 2, 260, "center")
    E.frase(c, t, C["s15.a"], [("não", "g", 70, ERRADO), ("compensa:", "i", 70, CLARO), ("Δ", "g", 76, BR), ("<", "g", 76, BR), ("0", "g", 76, BR)], W / 2, 430, "center")
    E.frase(c, t, C["s15.a"] + 2.0, ps("ou raízes que não saem exatas", "i", 60, CLARO), W / 2, 540, "center", passo=0.1)
    E.foco(c, t, C["s15.b"], 0.6, lambda a: (M.rrect(c, W / 2 - 330, 650, 660, 230, 50, CERTO, a),
                                             fsub(c, "x_v = f{−b}{2a}", W / 2, 800, 110, "g", BR, a, "center")))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "f(x) = −x^2 + 6x − 5", XE, 400, 96, "g", TINTA, a))
    E.frase(c, t, C["s16.a"] + 2.2, [("1)", "g", 64, COR), ("o", "i", 64), ("vértice?", "g", 64, COR)], XE, 560)
    E.frase(c, t, C["s16.b"], [("2)", "g", 64, COR), ("mais", "i", 64), ("alto", "g", 64), ("ou", "i", 64), ("mais", "i", 64), ("baixo?", "g", 64)], XE, 670)
    E.frase(c, t, C["s16.b"] + 2.0, [("3)", "g", 64, COR), ("a", "i", 64), ("imagem?", "g", 64, COR)], XE, 780)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    plano(c, t, C["s18"], PQ, MQ)
    E.curva(c, t, C["s18"] + 0.3, PQ, q, 0, 6, d=1.0, cor=TINTA)

    def s18():
        pos = lei_em(c, t, C["s18"], [("f(x) = ", TINTA), ("−x^2", CA), (" + 6x", CB), (" − 5", CC)], XE, 220, 70)
        sob_parte(c, t, C["s18.a"], pos, 1, 220, "a = −1", CA, 40)
        sob_parte(c, t, C["s18.a"] + 0.6, pos, 2, 220, "b = 6", CB, 40, apara=larg_f(" + ", 70))
        fml(c, t, C["s18.b"] - 1.6, "−b = −6    2a = −2", XE, 410, 56, TINTA2)
        fml(c, t, C["s18.b"], "x_v = f{−6}{−2} = 3", XE, 540, 76, ENT)
        fml(c, t, C["s18.b"] + 2.4, "f(3) = −3^2 + 6 · 3 − 5", XE, 680, 64, TINTA)
        fml(c, t, C["s18.c"], "= −9 + 18 − 5", XE + 140, 780, 64, TINTA)
        fml(c, t, C["s18.d"], "= 4", XE + 560, 780, 70, SAI)
        E.frase(c, t, C["s18.e"], [("vértice:", "i", 64)], XE, 910)
        E.foco(c, t, C["s18.e"] + 0.3, 0.4, lambda a: par(c, "3", "4", XE + 250, 910, 70, a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    eixo_sim(c, t, C["s18.b"] + 0.4, PQ, 3, ENT, 0.7)
    vertice(c, t, C["s18.e"], PQ, 3, 4, ("3", "4"), abaixo=False)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.pilula(c, "a < 0: o mais alto, o máximo", XE + 320, 220, 46, "g", fundo=TINTA, a=a))
    M.line(c, PQ.x(3), PQ.y(4), PQ.ox, PQ.y(4), TINTA, ep(t, C["s19.b"], 0.5), 4, dash=E.TRACO)
    faixa_imagem(c, t, C["s19.b"], PQ, 4, False)
    E.foco(c, t, C["s19.b"], 0.6, lambda a: (M.rrect(c, XE - 20, 300, 600, 160, 44, SAI, a),
                                             E.formula(c, "Im = ]−∞, 4]", XE + 280, 410, 80, "g", BR, a, "center")))
    E.foco(c, t, C["s19.c"] - 10.4, 0.4, lambda a: E.formula(c, "f(1) = −1 + 6 − 5 = 0", XE, 580, 58, "g", TINTA2, a))
    E.foco(c, t, C["s19.c"] - 6.6, 0.4, lambda a: E.formula(c, "f(5) = −25 + 30 − 5 = 0", XE, 680, 58, "g", TINTA2, a))
    raiz(c, t, C["s19.c"], PQ, 1, rot=False)
    raiz(c, t, C["s19.c"] + 0.3, PQ, 5, rot=False)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "f{1 + 5}{2} = 3", XE, 840, 70, "g", ENT, a))
    E.foco(c, t, C["s19.c"] + 1.4, 0.4, lambda a: E.pilula(c, "bateu", XE + 560, 820, 50, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        x1 = 340 + E.larg("x do vértice:", "i", 76) + 30
        x2 = x1 + E.larg("média das raízes ou", "g", 56) + 30
        itens = (("s20.a", lambda a, y: (E.escreve(c, "x do vértice:", 340, y, 76, "i", ENT, a),
                                         E.escreve(c, "média das raízes ou", x1, y - 6, 56, "g", COR, a), E.formula(c, "f{−b}{2a}", x2, y, 76, "g", COR, a))),
                 ("s20.b", lambda a, y: (E.escreve(c, "a imagem começa ou termina no", 340, y, 64, "i", TINTA, a),
                                         E.escreve(c, "y do vértice", 340, y + 90, 76, "g", SAI, a))))
        for i, (k, fn) in enumerate(itens):
            y = 440 + i * 230
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s21"] + 1.0, [("máximo", "g", 120, COR), ("e", "i", 110), ("mínimo", "g", 120, COR)], XE, 460)
    E.frase(c, t, C["s21.a"], ps("altura máxima e lucro máximo", "i", 58, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s21.b"], [("o", "i", 62), ("x", "g", 70, ENT), ("ou", "i", 62), ("o", "i", 62), ("y", "g", 70), ("do", "i", 62), ("vértice?", "g", 62, COR)], XE, 690)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, simetria=b_simetria, media=b_media, formula=b_formula, imagem=b_imagem, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
