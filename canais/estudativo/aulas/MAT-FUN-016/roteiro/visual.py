"""Visual — Estudativo · MAT-FUN-016: função quadrática, a parábola.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Nesta aula: na lei, o a (que decide a boca) é índigo e o c (o corte no eixo y, uma saída) é preto pesado; o b fica cinza. A parábola
de a > 0 é índigo e a virada (a < 0) é preta. O corte no eixo y ganha o círculo fixo de marca_ponto(). Chaves sob a lei apontam a, b e c
(lei() desenha a lei por partes e devolve onde cada parte começa e termina).
Peças locais: eixos(), par(), anel(), marca_ponto(), tabela(), lei(), sob_parte(), mini()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
CA, CB, CC = COR, TINTA2, TINTA  # cores de a, b e c
ARQUIVO_FINAL = "estudativo_MAT-FUN-016_funcao_quadratica_a_parabola.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "tabela", "concavidade", "corte", "atalho", "questao", "fim"))
BR = "#FFFFFF"

f = lambda x: x * x - 4 * x + 3
g = lambda x: -x * x + 4 * x - 3
erro = lambda x: 3 - x * x
q1 = lambda x: -2 * x * x + 8 * x - 6
q2 = lambda x: 4 - x + 2 * x * x
XS = (0, 1, 2, 3, 4)
assert [f(x) for x in XS] == [3, 0, -1, 0, 3] and [g(x) for x in XS] == [-3, 0, 1, 0, -3]
assert 1 - 4 + 3 == 0 and 4 - 8 + 3 == -1 and 10 ** 2 == 100 and -4 * 10 == -40 and (0 - 1) * (0 - 3) == 3
assert q1(0) == -6 and q2(0) == 4

PL = (1080, 190, 700, 700)
P = E.Plano(*PL, -1.5, 5.5, -4, 4)
MP = ([-1, 0, 1, 2, 3, 4, 5], [-4, -3, -2, -1, 0, 1, 2, 3, 4])
PQ = E.Plano(*PL, -2, 5, -8, 8)
MQ = ([-2, -1, 0, 1, 2, 3, 4, 5], [-8, -6, -4, -2, 0, 2, 4, 6, 8])

LEI_F = [("f(x) = ", TINTA), ("x^2", CA), (" − 4x", CB), (" + 3", CC)]
LEI_G = [("f(x) = ", TINTA), ("−x^2", CA), (" + 4x", CB), (" − 3", CC)]


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


def plano(c, t, t0):
    eixos(c, t, P, t0, tg=t0, marcas=MP, size=36)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        pos = lei_em(c, t, C["s01.a"], LEI_F, W / 2, 260, 130, "center")
        sorri = lambda x: 0.6 * x * x - 1.8
        triste = lambda x: -0.6 * x * x + 1.8
        mini(c, t, C["s01.b"], 330, 470, 420, 340, sorri, -2.4, 2.4, COR)
        mini(c, t, C["s01.b"] + 0.8, 870, 470, 420, 340, triste, -2.4, 2.4, TINTA)
        E.foco(c, t, C["s01.b"] + 0.5, 0.4, lambda a: centro(c, "sorriso?", 540, 900, 52, "i", COR, a))
        E.foco(c, t, C["s01.b"] + 1.3, 0.4, lambda a: centro(c, "cara triste?", 1080, 900, 52, "i", TINTA, a))
        Q = E.plano(c, t, C["s01.c"], 1430, 470, 340, 340, -3, 3, -3, 3, grade=False, rotulos=False, size=30, d=0.5)
        if t >= C["s01.c"] + 0.4:
            q = ep(t, C["s01.c"] + 0.4, 0.4)
            M.line(c, Q.ox, Q.caixa[1], Q.ox, Q.caixa[1] + Q.caixa[3], SAI, 0.25 * q, 24)
            E.pilula(c, "?", Q.ox + 60, Q.y(1.5), 44, "g", fundo=SAI, a=q)
        E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: centro(c, "corta o y onde?", 1600, 900, 52, "i", SAI, a))
        tf = C["s02"] - 2.4
        sob_parte(c, t, tf, pos, 1, 260, "a", CA, 56)
        sob_parte(c, t, tf + 0.3, pos, 3, 260, "c", CC, 56, apara=larg_f(" + ", 130))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.6, [("a,", "g", 120, CA), ("b", "g", 120, CB), ("e", "i", 110), ("c", "g", 120, CC)], XE, 460)
        E.frase(c, t, C["s02.a"] + 3.4, ps("para onde a", "i", 90), XE, 600)
        E.frase(c, t, C["s02.a"] + 4.0, [("parábola", "g", 110, COR), ("abre", "i", 100)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.a", "a, b e c com o sinal junto:", lambda a, y: (lei(c, [("2x^2", CA), (" − 3x", CB), (" + 1 = 0", CC)], x + 44, y, 64, a),
                                                                  E.formula(c, "b = −3", x + 520, y, 56, "g", CB, a))),
             ("s03.b", "gráfico pela tabela:", lambda a, y: (E.escreve(c, "x", x + 44, y, 64, "g", ENT, a),
                                                            E.escreve(c, "→  y  →  ponto", x + 100, y, 64, "g", TINTA, a))))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.a"], 0.4))


# ---------------- a lei ----------------
LEI_GERAL = [("f(x) = ", TINTA), ("ax^2", CA), (" + bx", CB), (" + c", CC)]


def b_lei(c, t, C, b):
    def s04():
        lei_em(c, t, C["s04.a"], LEI_GERAL, W / 2, 260, 130, "center")
        E.frase(c, t, C["s04.b"], [("função", "g", 110, COR), ("quadrática", "g", 110, COR)], W / 2, 450, "center")
        E.foco(c, t, C["s04.b"] + 1.0, 0.4, lambda a: E.pilula(c, "a ≠ 0", W / 2, 560, 52, "g", fundo=CA, a=a))
        E.frase(c, t, C["s04.b"] + 2.6, [("a", "g", 64, CA), ("=", "g", 64), ("0:", "g", 64), ("o", "i", 64), ("x²", "g", 64), ("some", "i", 64, ERRADO)],
                W / 2, 670, "center")
        E.foco(c, t, C["s04.c"] - 1.6, 0.4, lambda a: E.formula(c, "equação: ax^2 + bx + c = 0", W / 2, 800, 64, "g", TINTA2, a, "center"))
        E.frase(c, t, C["s04.c"], [("função:", "i", 64), ("cada", "i", 64), ("x,", "g", 70, ENT), ("uma", "i", 64), ("saída", "g", 64)], W / 2, 920, "center")
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    pos = lei_em(c, t, C["s05.a"], LEI_F, W / 2, 420, 150, "center")
    sob_parte(c, t, C["s05.b"], pos, 1, 420, "a = 1", CA, 60)
    E.foco(c, t, C["s05.b"] - 1.6, 0.4, lambda a: E.escreve(c, "1", pos[1][0] - 46, 330, 70, "g", CA, 0.6 * a))
    sob_parte(c, t, C["s05.c"], pos, 2, 420, "b = −4", CB, 60)
    sob_parte(c, t, C["s05.d"], pos, 3, 420, "c = 3", CC, 60, apara=larg_f(" + ", 150))
    E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: E.pilula(c, "com o sinal junto", W / 2, 780, 46, "g", fundo=TINTA2, a=a))


# ---------------- tabela e gráfico ----------------
TX, TY = 220, 300


def tab(c, t, fn, tc, tl, destaque=None):
    linhas = [(E._num(x), E._num(fn(x))) for x in XS]
    tabela(c, t, TX, TY, ["x", "f(x)"], [ENT, SAI], linhas, tc, [[tc, ti] for ti in tl], wc=180, hl=84, size=58, destaque=destaque)


def b_tabela(c, t, C, b):
    plano(c, t, C["s06"])
    ks = ("s06.a", "s06.b", "s06.c", "s06.d", "s06.e")
    E.foco(c, t, C["s06"], 0.4, lambda a: lei(c, LEI_F, XE, 170, 66, a))
    tab(c, t, f, C["s06"] + 0.3, [C[k] for k in ks])
    contas = (("s06.b", "s06.c", "f(1) = 1 − 4 + 3 = 0"), ("s06.c", "s06.d", "f(2) = 4 − 8 + 3 = −1"))
    for k0, k1, s in contas:
        if t >= C[k0]:
            E.saida(c, t, C[k1] - 0.1, lambda s=s, k0=k0: fml(c, t, C[k0], s, XE, 860, 58, TINTA))
    if t < C["s07"]:
        return
    for i, xv in enumerate(XS):
        E.ponto(c, t, C["s07"] + 0.4 * i, P, xv, f(xv), cor=COR, r=15)
    E.curva(c, t, C["s07.a"] - 0.6, P, f, -0.6, 4.6, d=1.4, cor=COR)
    E.foco(c, t, C["s07.a"] + 0.4, 0.4, lambda a: E.escreve(c, "o U", XE, 870, 60, "i", COR, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "parábola", 1430, 220, 60, "g", fundo=COR, a=a))


# ---------------- concavidade ----------------
def b_concavidade(c, t, C, b):
    plano(c, t, C["s08"] - 3)
    E.curva(c, t, C["s08"] - 3, P, f, -0.6, 4.6, d=0.05, cor=COR)
    for i, xv in enumerate(XS):
        E.ponto(c, t, C["s08.c"] + 0.3 * i, P, xv, g(xv), cor=TINTA, r=14)
    E.curva(c, t, C["s08.d"], P, g, -0.6, 4.6, d=1.2, cor=TINTA)

    def s08():
        pos = lei_em(c, t, C["s08.a"], LEI_G, XE, 260, 84)
        sob_parte(c, t, C["s08.b"], pos, 1, 260, "a = −1", CA, 52)
        E.frase(c, t, C["s08.c"], [("x:", "g", 54, ENT), ("0", "g", 58, ENT), ("1", "g", 58, ENT), ("2", "g", 58, ENT), ("3", "g", 58, ENT), ("4", "g", 58, ENT)],
                XE, 520, passo=0.12)
        E.frase(c, t, C["s08.c"] + 0.3, [("y:", "g", 54), ("−3", "g", 58), ("0", "g", 58), ("1", "g", 58), ("0", "g", 58), ("−3", "g", 58)], XE, 610, passo=0.3)
        E.frase(c, t, C["s08.d"], [("de", "i", 64), ("cabeça", "g", 64, TINTA), ("para", "i", 64), ("baixo", "g", 64, TINTA)], XE, 790)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"] + 0.4:
        def s09():
            E.frase(c, t, C["s09"], [("quem", "i", 72), ("decide:", "i", 72), ("o", "i", 72), ("sinal", "g", 72), ("do", "i", 72), ("a", "g", 80, CA)], XE, 230)
            E.frase(c, t, C["s09.a"], [("a", "g", 76, CA), (">", "g", 76, CA), ("0:", "g", 76, CA), ("abre", "i", 70), ("para", "i", 70), ("cima", "g", 70, COR)], XE, 390)
            E.foco(c, t, C["s09.a"] + 1.0, 0.4, lambda a: E.escreve(c, "sorriso", XE + 100, 470, 52, "i", COR, a))
            E.frase(c, t, C["s09.b"], [("a", "g", 76, CA), ("<", "g", 76, CA), ("0:", "g", 76, CA), ("abre", "i", 70), ("para", "i", 70), ("baixo", "g", 70)], XE, 600)
            E.foco(c, t, C["s09.b"] + 1.0, 0.4, lambda a: E.escreve(c, "cara triste", XE + 100, 680, 52, "i", TINTA, a))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "concavidade", XE + 280, 840, 66, "g", fundo=COR, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
    for k, fn, cor in (("s09.a", f, COR), ("s09.b", g, TINTA)):
        q = ep(t, C[k], 0.3) * (1 - ep(t, C[k] + 3.0, 0.5))
        if q > 0:
            c.saveLayerAlpha(None, int(80 * q))
            E.curva(c, t, 0, P, fn, -0.6, 4.6, d=0.01, cor=cor, largura=26)
            c.restore()
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"], [("por", "i", 72), ("que", "i", 72), ("o", "i", 72), ("a?", "g", 80, CA)], XE, 230)
    E.frase(c, t, C["s10.a"], ps("longe do zero, o", "i", 54) + [("x²", "g", 54, CA)] + ps("cresce muito mais", "i", 54), XE, 340, passo=0.1)
    E.foco(c, t, C["s10.a"] + 2.4, 0.4, lambda a: E.formula(c, "x = 10:", XE, 460, 64, "g", ENT, a))
    E.foco(c, t, C["s10.a"] + 3.0, 0.4, lambda a: E.formula(c, "x^2 = 100", XE + 280, 460, 64, "g", CA, a))
    E.foco(c, t, C["s10.a"] + 5.0, 0.4, lambda a: E.formula(c, "−4x = −40", XE + 280, 560, 64, "g", CB, a))
    E.frase(c, t, C["s10.b"] - 1.0, [("nas", "i", 64), ("pontas,", "i", 64), ("manda", "i", 64)], XE, 720)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "a · x^2", XE + 520, 720, 76, "g", CA, a))
    E.foco(c, t, C["s10.b"] + 2.0, 0.4, lambda a: E.pilula(c, "sinal do a: pontas sobem ou descem", XE + 400, 850, 40, "g", fundo=TINTA2, a=a))
    p = ep(t, C["s10.b"] + 1.0, 0.6)
    if p > 0:
        for xv in (-0.75, 4.75):
            M.arrow(c, *P(xv, 2.4), *P(xv, 3.8), COR, p, 6, 20, p)
            M.arrow(c, *P(xv, -2.4), *P(xv, -3.8), TINTA, p, 6, 20, p)


# ---------------- corte no eixo y ----------------
def b_corte(c, t, C, b):
    plano(c, t, C["s11"] - 3)
    E.curva(c, t, C["s11"] - 3, P, f, -0.6, 4.6, d=0.05, cor=COR)
    E.curva(c, t, C["s11"] - 3, P, g, -0.6, 4.6, d=0.05, cor=TINTA)
    q = ep(t, C["s11.a"], 0.4) * (1 - ep(t, C["s12"], 0.5))
    if q > 0:
        x, y, w, h = P.caixa
        M.line(c, P.ox, y + h + 10, P.ox, y - 20, SAI, 0.2 * q, 30)
    if t >= C["s12.a"]:
        marca_ponto(c, t, C["s12.a"], *P(0, 3), COR, 24)
        E.foco(c, t, C["s12.a"] + 0.3, 0.4, lambda a: par(c, "0", "3", P.x(0) + 34, P.y(3) - 22, 46, a))
    if t >= C["s12.b"]:
        marca_ponto(c, t, C["s12.b"], *P(0, -3), TINTA, 24)
        E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: par(c, "0", "−3", P.x(0) + 34, P.y(-3) + 60, 46, a))

    def s11():
        E.frase(c, t, C["s11"], [("onde", "i", 72), ("cruza", "i", 72), ("o", "i", 72), ("eixo", "i", 72), ("y?", "g", 80)], XE, 230)
        E.frase(c, t, C["s11.a"], [("no", "i", 64), ("eixo", "i", 64), ("y,", "g", 70), ("x", "g", 70, ENT), ("=", "g", 70, ENT), ("0", "g", 70, ENT)], XE, 360)
        fml(c, t, C["s11.b"], "f(0) = a · 0 + b · 0 + c", XE, 500, 64, TINTA)
        E.foco(c, t, C["s11.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 570, 420, 150, 40, CC, a), E.formula(c, "f(0) = c", XE + 190, 680, 84, "g", BR, a, "center")))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.foco(c, t, C["s12"], 0.4, lambda a: E.formula(c, "f(0) = c", XE, 230, 66, "g", CC, a))
    pf = lei_em(c, t, C["s12"] + 0.3, LEI_F, XE, 380, 70)
    sob_parte(c, t, C["s12.a"] - 0.4, pf, 3, 380, "c = 3", CC, 46, apara=larg_f(" + ", 70))
    par_em(c, t, C["s12.a"], "0", "3", XE + 660, 380, 60)
    pg = lei_em(c, t, C["s12.b"] - 1.4, LEI_G, XE, 650, 70)
    sob_parte(c, t, C["s12.b"] - 0.4, pg, 3, 650, "c = −3", CC, 46, apara=larg_f(" ", 70))
    par_em(c, t, C["s12.b"], "0", "−3", XE + 660, 650, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    PE = E.Plano(*PL, -3, 3, -2, 4)
    eixos(c, t, PE, C["s13"], tg=C["s13"], marcas=([-3, -2, -1, 0, 1, 2, 3], [-2, -1, 0, 1, 2, 3, 4]), size=36)
    E.frase(c, t, C["s13.a"], [("o", "i", 72), ("erro:", "i", 72), ("o", "i", 72), ("primeiro", "g", 72, ERRADO), ("número", "g", 72, ERRADO)], XE, 230)
    partes = [("f(x) = ", TINTA), ("3", TINTA), (" − x^2", CA)]
    pos = lei_em(c, t, C["s13.b"], partes, XE, 420, 110)
    if t >= C["s13.b"] + 0.8:
        x0, x1 = pos[1]
        q = ease_out(prog(t, C["s13.b"] + 0.8, 0.5))
        E.arco(c, (x0 + x1) / 2, 380, 62, -90, 360 * q, ERRADO, 6)

    def errado():
        E.foco(c, t, C["s13.b"] + 2.4, 0.4, lambda a: E.pilula(c, "abre para cima?", XE + 230, 560, 50, "g", fundo=ERRADO, a=a))
        sorri = lambda x: x * x - 1
        E.curva(c, t, C["s13.b"] + 2.6, PE, sorri, -2.2, 2.2, d=0.8, cor=ERRADO, tracejada=True)
    E.saida(c, t, C["s13.c"] - 0.1, errado)
    sob_parte(c, t, C["s13.c"], pos, 2, 420, "a = −1", CA, 56, apara=larg_f(" ", 110))
    E.curva(c, t, C["s13.c"] + 1.0, PE, erro, -2.3, 2.3, d=1.0, cor=TINTA)
    E.frase(c, t, C["s13.c"] + 1.2, [("abre", "i", 70), ("para", "i", 70), ("baixo", "g", 70, CERTO)], XE, 700)
    E.frase(c, t, C["s13.end"] - 3.2, [("o", "i", 60, TINTA2), ("U", "g", 62), ("de", "i", 60, TINTA2), ("cabeça", "i", 60, TINTA2), ("para", "i", 60, TINTA2),
                                       ("baixo", "i", 60, TINTA2)], XE, 820)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 180)
        E.frase(c, t, C["s14.a"], [("a", "i", 80, CLARO), ("parábola", "g", 84, BR), ("em", "i", 80, CLARO), ("2", "g", 84, BR), ("segundos", "i", 80, CLARO)], XE, 300)
        E.frase(c, t, C["s14.b"], [("sinal", "i", 72, CLARO), ("do", "i", 72, CLARO), ("a", "g", 80, BR), ("→", "g", 72, CLARO), ("a", "i", 72, CLARO), ("boca", "g", 76, BR)], XE, 440)
        E.frase(c, t, C["s14.c"], [("c", "g", 80, BR), ("→", "g", 72, CLARO), ("o", "i", 72, CLARO), ("corte", "g", 76, BR), ("no", "i", 72, CLARO), ("eixo", "i", 72, CLARO),
                                   ("y", "g", 80, BR)], XE, 560)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: lei(c, [("x^2", BR), (" − 4x", CLARO), (" + 3", BR)], XE, 720, 80, a))
        E.frase(c, t, C["s14.d"] + 1.0, [("a", "g", 66, BR), (">", "g", 66, BR), ("0:", "g", 66, BR), ("sorriso,", "i", 66, CLARO), ("corta", "i", 66, CLARO), ("no", "i", 66, CLARO),
                                         ("3", "g", 70, "#FFD500")], XE, 840)
        Q = E.plano(c, t, C["s14.a"], 1140, 260, 600, 600, -1.5, 5.5, -2, 4, marcas_x=[1, 2, 3, 4, 5], marcas_y=[-1, 1, 2, 3, 4], escuro=True)
        E.curva(c, t, C["s14.b"] + 0.5, Q, f, -0.6, 4.6, d=1.0, cor=CLARO)
        if t >= C["s14.c"] + 0.5:
            marca_ponto(c, t, C["s14.c"] + 0.5, *Q(0, 3), "#FFD500", 22)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("f(0)", "g", 70, BR), ("apaga", "i", 68, CLARO), ("tudo", "i", 68, CLARO), ("menos", "i", 68, CLARO), ("o", "i", 68, CLARO), ("c", "g", 76, BR)], XE, 230)
    E.frase(c, t, C["s15.a"] - 1.4, [("não", "g", 70, ERRADO), ("compensa:", "i", 70, CLARO), ("lei", "i", 70, CLARO), ("em", "i", 70, CLARO), ("produto", "g", 70, BR)], XE, 400)
    fml(c, t, C["s15.a"], "f(x) = (x − 1)(x − 3)", XE, 540, 90, BR)
    E.frase(c, t, C["s15.a"] + 2.4, ps("o c não aparece escrito", "i", 60, CLARO), XE, 650, passo=0.1)
    E.foco(c, t, C["s15.b"], 0.6, lambda a: (M.rrect(c, XE - 20, 730, 1020, 160, 40, CERTO, a),
                                             E.formula(c, "f(0) = (−1) · (−3) = 3", XE + 490, 845, 80, "g", BR, a, "center")))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "f(x) = −2x^2 + 8x − 6", XE, 380, 90, "g", TINTA, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "g(x) = 4 − x + 2x^2", XE, 530, 90, "g", TINTA, a))
    E.frase(c, t, C["s16.c"], [("a,", "g", 66, CA), ("b", "g", 66, CB), ("e", "i", 62), ("c?", "g", 66, CC)], XE, 700)
    E.frase(c, t, C["s16.c"] + 1.8, [("abre", "i", 62), ("para", "i", 62), ("onde?", "g", 64, COR)], XE + 380, 700)
    E.frase(c, t, C["s16.c"] + 3.6, [("corta", "i", 62), ("o", "i", 62), ("eixo", "i", 62), ("y", "g", 66), ("onde?", "g", 64, COR)], XE, 810)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eixos(c, t, PQ, C["s18"], tg=C["s18"], marcas=MQ, size=34, ry=[-6, -4, -2, 2, 4, 6, 8])
    E.curva(c, t, C["s18.b"], PQ, q1, -0.25, 4.25, d=1.0, cor=TINTA)
    if t >= C["s18.c"]:
        marca_ponto(c, t, C["s18.c"], *PQ(0, -6), TINTA, 22)
        E.foco(c, t, C["s18.c"] + 0.3, 0.4, lambda a: par(c, "0", "−6", PQ.x(0) + 34, PQ.y(-6) + 50, 44, a))

    def s18():
        pos = lei_em(c, t, C["s18"], [("f(x) = ", TINTA), ("−2x^2", CA), (" + 8x", CB), (" − 6", CC)], XE, 260, 80)
        sob_parte(c, t, C["s18.a"], pos, 1, 260, "a = −2", CA, 44)
        sob_parte(c, t, C["s18.a"] + 0.8, pos, 2, 260, "b = 8", CB, 44, apara=larg_f(" + ", 80))
        sob_parte(c, t, C["s18.a"] + 1.6, pos, 3, 260, "c = −6", CC, 44, apara=larg_f(" ", 80))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.pilula(c, "a < 0: abre para baixo", XE + 300, 560, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s18.c"], [("corta", "i", 64), ("em", "i", 64)], XE, 720)
        par_em(c, t, C["s18.c"] + 0.3, "0", "−6", XE + 260, 720, 72)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.curva(c, t, C["s19.d"], PQ, q2, -1.3, 1.85, d=1.0, cor=COR)
    if t >= C["s19.e"]:
        marca_ponto(c, t, C["s19.e"], *PQ(0, 4), COR, 22)
        E.foco(c, t, C["s19.e"] + 0.3, 0.4, lambda a: par(c, "0", "4", PQ.x(0) + 34, PQ.y(4) + 74, 44, a))
    E.foco(c, t, C["s19"], 0.5, lambda a: lei(c, [("g(x) = ", TINTA), ("4", CC), (" − x", CB), (" + 2x^2", CA)], XE, 240, 76, a))
    E.frase(c, t, C["s19"] + 0.4, [("a", "i", 54, TINTA2), ("ordem", "i", 54, TINTA2), ("está", "i", 54, TINTA2), ("trocada", "g", 54, ERRADO)], XE, 330)
    fml(c, t, C["s19.a"], "a = 2", XE, 470, 76, CA)
    E.foco(c, t, C["s19.a"] + 0.3, 0.4, lambda a: E.escreve(c, "(o do x²)", XE + 250, 470, 44, "b", TINTA2, a))
    fml(c, t, C["s19.b"], "b = −1", XE, 580, 76, CB)
    fml(c, t, C["s19.c"], "c = 4", XE, 690, 76, CC)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "a > 0: abre para cima", XE + 290, 820, 50, "g", fundo=COR, a=a))
    E.frase(c, t, C["s19.e"], [("corta", "i", 62), ("em", "i", 62)], XE, 950)
    par_em(c, t, C["s19.e"] + 0.3, "0", "4", XE + 250, 950, 66)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("sinal", "i", 84), ("do", "i", 84), ("a:", "g", 90, CA), ("para", "i", 84), ("onde", "i", 84), ("abre", "g", 84)]),
                 ("s20.b", [("o", "i", 84), ("c:", "g", 90, CC), ("onde", "i", 84), ("corta", "i", 84), ("o", "i", 84), ("eixo", "i", 84), ("y", "g", 90)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s21.a"], [("onde", "i", 96), ("corta", "i", 96), ("o", "i", 96), ("eixo", "i", 96), ("x", "g", 120, ENT)], XE, 460)
    E.frase(c, t, C["s21.b"], [("o", "i", 64, TINTA2), ("1", "g", 70, ENT), ("e", "i", 64, TINTA2), ("o", "i", 64, TINTA2), ("3", "g", 70, ENT), ("desta", "i", 64, TINTA2),
                               ("parábola", "i", 64, TINTA2)], XE, 590)
    E.frase(c, t, C["s21.c"], [("e", "i", 64, TINTA2), ("as", "i", 64, TINTA2), ("que", "i", 64, TINTA2), ("nem", "g", 64, ERRADO), ("encostam", "i", 64, TINTA2)], XE, 690)
    Q = E.Plano(1280, 530, 380, 230, -1, 5, -1.5, 3.5)
    E.plano(c, t, C["s21.a"], 1280, 530, 380, 230, -1, 5, -1.5, 3.5, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, C["s21.a"] + 0.3, Q, f, -0.5, 4.5, d=1.0, cor=COR, largura=8)
    for xv in (1, 3):
        if t >= C["s21.b"]:
            marca_ponto(c, t, C["s21.b"] + 0.3 * (xv == 3), *Q(xv, 0), ENT, 16)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, tabela=b_tabela, concavidade=b_concavidade, corte=b_corte, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
