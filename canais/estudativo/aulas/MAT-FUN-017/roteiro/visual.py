"""Visual — Estudativo · MAT-FUN-017: raízes, onde a parábola corta o eixo x.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016: na lei, o a em índigo, o b em cinza e o c em preto; parábola de a > 0 índigo, de a < 0 preta; o corte no eixo y
ganha o círculo fixo de marca_ponto(). Nesta aula: as raízes são círculos índigo no eixo x (o x é índigo); o Δ fica sempre numa
pílula (verde > 0, cinza = 0, vermelho < 0). Os três casos lado a lado em minis (caso()), com a faixa do eixo x acesa.
Peças locais: eixos(), par(), anel(), marca_ponto(), lei(), sob_parte(), mini(), caso(), raiz()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
CA, CB, CC = COR, TINTA2, TINTA  # cores de a, b e c
ARQUIVO_FINAL = "estudativo_MAT-FUN-017_raizes_onde_a_parabola_corta_o_eixo_x.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "exemplo", "casos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

f = lambda x: x * x - 4 * x + 3
f4 = lambda x: x * x - 4 * x + 4
f5 = lambda x: x * x - 4 * x + 5
h = lambda x: x * x + 2 * x - 8
q1 = lambda x: x * x - 6 * x + 8
q2 = lambda x: -x * x + 2 * x - 1
assert 16 - 12 == 4 and (4 + 2) / 2 == 3 and (4 - 2) / 2 == 1 and f(1) == f(3) == 0 and f(0) == 3
assert 16 - 16 == 0 and 4 / 2 == 2 and f4(2) == 0 and 16 - 20 == -4 and f5(0) == 5 and f5(2) == 1 and min(f5(x / 10) for x in range(-50, 90)) > 0
assert h(-4) == h(2) == 0 and h(0) == -8
assert 36 - 32 == 4 and (6 + 2) / 2 == 4 and (6 - 2) / 2 == 2 and q1(2) == q1(4) == 0
assert 2 ** 2 - 4 * (-1) * (-1) == 0 and -2 / -2 == 1 and q2(1) == 0

PL = (1080, 190, 700, 700)
P = E.Plano(*PL, -1.5, 5.5, -2, 5)
MP = ([-1, 0, 1, 2, 3, 4, 5], [-2, -1, 0, 1, 2, 3, 4, 5])
PQ = E.Plano(*PL, -1.5, 5.5, -5, 9)
MQ = ([-1, 0, 1, 2, 3, 4, 5], [-4, -2, 0, 2, 4, 6, 8])
LEI_F = [("f(x) = ", TINTA), ("x^2", CA), (" − 4x", CB), (" + 3", CC)]
AMARELO = "#FFD500"
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




def plano(c, t, t0, P_=None, marcas=None):
    eixos(c, t, P_ or P, t0, tg=t0, marcas=marcas or MP, size=36)


def raiz(c, t, t0, P_, xv, rot=True, cor=None, size=42, lado=1):
    """raiz: círculo no eixo x, com o par (x, 0) acima do eixo, para dentro do intervalo entre as raízes (lado = +1 direita, −1 esquerda)"""
    if t < t0:
        return
    marca_ponto(c, t, t0, P_.x(xv), P_.oy, cor or ENT, 20)
    if rot:
        def rot_(a):
            w = par(None, E._num(xv), "0", 0, 0, size, 0)
            x0 = P_.x(xv) + 24 if lado > 0 else P_.x(xv) - 24 - w
            M.rrect(c, x0 - 10, P_.oy - 32 - size * 0.95, w + 20, size * 1.3, 12, "#F4F3EF", 0.92 * a)
            par(c, E._num(xv), "0", x0, P_.oy - 32, size, a)
        E.foco(c, t, t0 + 0.3, 0.4, rot_)


def faixa_x(c, P_, q, cor=ENT, larg=24):
    """faixa acesa sobre o eixo x"""
    if q > 0:
        x, y, w, h_ = P_.caixa
        M.line(c, x - 10, P_.oy, x + w + 20, P_.oy, cor, 0.22 * q, larg)


def delta(c, s, cx, cy, size, fundo, a):
    E.pilula(c, s, cx, cy, size, "g", fundo=fundo, a=a)


# ---------------- gancho ----------------
CASOS = ((f, CERTO, "Δ > 0"), (f4, TINTA2, "Δ = 0"), (f5, ERRADO, "Δ < 0"))
CX = (130, 720, 1310)


def caso(c, t, t0, i, fn, cor=None, y=290, w=480, h_=420, d=0.9, ymin=-2, ymax=5, neg=None, tn=None):
    """mini-plano de um caso, de x = −0,5 até 4,5 (eixos sem números), com a curva fn"""
    Q = E.plano(c, t, t0, CX[i], y, w, h_, -0.5, 4.5, ymin, ymax, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, t0 + 0.3, Q, fn, -0.5, 4.5, d=d, largura=8, cor=cor or COR)
    if neg is not None:
        E.curva(c, t, tn, Q, neg, -0.5, 4.5, d=d, largura=8, cor=TINTA)
    return Q


def b_gancho(c, t, C, b):
    def cena1():
        Qs = [caso(c, t, C["s01.a"] + 0.4 * i, i, fn) for i, (fn, _, _) in enumerate(CASOS)]
        rots = ("corta 2 vezes", "só encosta", "nem chega perto")
        for i, Q in enumerate(Qs):
            E.foco(c, t, C["s01.a"] + 0.4 * i + 0.8, 0.4, lambda a, i=i: centro(c, rots[i], CX[i] + 240, 790, 54, "i", ERRADO if i == 2 else TINTA, a))
        faixa_x(c, Qs[2], ep(t, C["s01.b"], 0.4) * (1 - ep(t, C["s01.b"] + 2.0, 0.4)), ERRADO)
        for x_ in (1, 3):
            raiz(c, t, C["s01.a"] + 1.2, Qs[0], x_, rot=False)
        raiz(c, t, C["s01.a"] + 1.6, Qs[1], 2, rot=False)
        E.frase(c, t, C["s01.c"], [("uma", "i", 70), ("conta", "g", 70, COR), ("diz", "i", 70), ("qual", "i", 70), ("é", "i", 70), ("qual", "i", 70)], W / 2, 200, "center")
        E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: delta(c, "Δ", W / 2, 940, 70, COR, a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("onde", "i", 100), ("corta", "g", 110, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 2.4, [("o", "i", 100), ("eixo", "i", 100), ("x", "g", 120, ENT)], XE, 590)
        E.frase(c, t, C["s02.a"] + 4.2, [("+", "g", 90, COR), ("os", "i", 90), ("3", "g", 100), ("casos", "g", 100)], XE, 750)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.a", "Bhaskara, com o delta:", lambda a, y: (E.formula(c, "x = f{−b ± r{Δ}}{2a}", x + 44, y + 10, 62, "g", COR, a),
                                                               E.formula(c, "Δ = b^2 − 4ac", x + 450, y, 58, "g", TINTA, a))),
             ("s03.b", "a parábola:", lambda a, y: (E.escreve(c, "a: a boca", x + 44, y, 58, "g", CA, a),
                                                     E.escreve(c, "c: corte no y", x + 380, y, 58, "g", CC, a))))
    for i, (k, l1, fn) in enumerate(itens):
        y = 230 + i * 320
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 260, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 780, q), ep(t, C["s03.a"], 0.4))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    plano(c, t, C["s04"])
    E.curva(c, t, C["s04"] + 0.4, P, f, -0.5, 4.5, d=1.0, cor=COR)
    faixa_x(c, P, ep(t, C["s04.a"], 0.4) * (1 - ep(t, C["s04.c"], 0.5)))
    if t >= C["s04.d"]:
        for k, xv in enumerate((1, 3)):
            raiz(c, t, C["s04.d"] + 0.3 * k, P, xv, rot=False)
            E.foco(c, t, C["s04.d"] + 0.3 * k + 0.2, 0.4, lambda a, xv=xv: E.pilula(c, "?", P.x(xv), P.oy + 80, 40, "g", fundo=ENT, a=a))
    E.frase(c, t, C["s04.a"], [("no", "i", 70), ("eixo", "i", 70), ("x:", "g", 76, ENT), ("y", "g", 80), ("=", "g", 80), ("0", "g", 80)], XE, 250)
    fml(c, t, C["s04.b"], "f(x) = 0", XE, 410, 100, TINTA)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: lei(c, [("x^2", CA), (" − 4x", CB), (" + 3", CC), (" = 0", TINTA)], XE, 560, 84, a))
    E.foco(c, t, C["s04.c"] + 0.5, 0.4, lambda a: E.escreve(c, "equação do 2º grau", XE, 640, 50, "i", TINTA2, a))
    E.frase(c, t, C["s04.d"], [("as", "i", 66), ("soluções:", "i", 66)], XE, 780)
    E.foco(c, t, C["s04.d"] + 0.4, 0.5, lambda a: E.pilula(c, "raízes ou zeros", XE + 210, 880, 56, "g", fundo=ENT, a=a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    def calc():
        pos = lei_em(c, t, C["s05.a"], [("x^2", CA), (" − 4x", CB), (" + 3", CC), (" = 0", TINTA)], XE, 220, 76)
        E.foco(c, t, C["s05.a"] + 1.4, 0.4, lambda a: E.escreve(c, "a = 1   b = −4   c = 3", XE, 310, 50, "g", TINTA2, a))
        fml(c, t, C["s05.b"] - 2.2, "Δ = b^2 − 4ac", XE, 440, 70, TINTA)
        fml(c, t, C["s05.b"], "Δ = 16 − 12 = 4", XE, 550, 70, TINTA)
        fml(c, t, C["s05.b"] + 1.4, "r{4} = 2", XE + 640, 550, 64, TINTA2)
        fml(c, t, C["s05.c"] - 1.8, "−b = 4    2a = 2", XE, 650, 58, TINTA2)
        fml(c, t, C["s05.c"], "x = f{4 ± 2}{2}", XE, 820, 90, COR)
    E.saida(c, t, C["s07"] - 0.1, calc)
    plano(c, t, C["s05"])

    def velho():
        E.curva(c, t, C["s05"] + 0.3, P, f, -0.5, 4.5, d=0.8, cor=COR)
        fml(c, t, C["s06.a"], "f{6}{2} = 3", XE + 560, 700, 70, ENT)
        fml(c, t, C["s06.b"], "f{2}{2} = 1", XE + 560, 900, 70, ENT)
        raiz(c, t, C["s06.c"], P, 1, lado=-1)
        raiz(c, t, C["s06.d"], P, 3)
    E.saida(c, t, C["s07"] - 0.1, velho)
    if t < C["s07"]:
        return
    # s07: o desenho em três pontos e a boca
    E.frase(c, t, C["s07"], ps("desenhar sem tabela comprida", "i", 60), XE, 220, passo=0.1)
    E.frase(c, t, C["s07.a"], [("a", "g", 70, CA), (">", "g", 70, CA), ("0:", "g", 70, CA), ("abre", "i", 64), ("para", "i", 64), ("cima", "g", 64)], XE, 380)
    E.frase(c, t, C["s07.b"], [("c", "g", 70, CC), ("=", "g", 70), ("3:", "g", 70), ("corta", "i", 64), ("o", "i", 64), ("y", "g", 70), ("no", "i", 64), ("3", "g", 70)], XE, 500)
    E.frase(c, t, C["s07.c"], [("raízes:", "i", 64), ("1", "g", 70, ENT), ("e", "i", 64), ("3", "g", 70, ENT)], XE, 620)
    E.frase(c, t, C["s07.d"], [("3", "g", 70, COR), ("pontos", "i", 64), ("+", "g", 70), ("a", "i", 64), ("boca", "g", 64)], XE, 790)
    p = ep(t, C["s07.a"], 0.5) * (1 - ep(t, C["s07.d"], 0.4))
    if p > 0:
        for xv in (-0.6, 4.6):
            M.arrow(c, *P(xv, 2.6), *P(xv, 4.3), COR, p, 6, 20, p)
    if t >= C["s07.b"]:
        marca_ponto(c, t, C["s07.b"], *P(0, 3), CC, 22)
    raiz(c, t, C["s07.c"], P, 1, rot=False)
    raiz(c, t, C["s07.c"] + 0.3, P, 3, rot=False)
    E.curva(c, t, C["s07.d"], P, f, -0.5, 4.5, d=1.2, cor=COR)


# ---------------- os três casos ----------------
def b_casos(c, t, C, b):
    neg = t >= C["s11"]
    ymin, ymax = -5, 5
    linhas = (("s08", f, CERTO, "Δ > 0", "2 raízes", None, None),
              ("s09", f4, TINTA2, "Δ = 0", "1 raiz (dupla)", "x^2 − 4x + 4", "Δ = 16 − 16 = 0"),
              ("s10", f5, ERRADO, "Δ < 0", "nenhuma raiz real", "x^2 − 4x + 5", "Δ = 16 − 20 = −4"))
    for i, (s, fn, cor, dl, rot, lei_, conta) in enumerate(linhas):
        t0 = C[s + ".a"]
        if t < t0:
            continue
        E.foco(c, t, t0, 0.5, lambda a, i=i, dl=dl, cor=cor: delta(c, dl, CX[i] + 240, 200, 56, cor, a))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a, i=i, rot=rot: centro(c, rot, CX[i] + 240, 790, 48, "i", TINTA, a))
        tc = C[s + ".b"]
        negf = (lambda x, fn=fn: -fn(x))
        Q = caso(c, t, t0, i, fn, d=0.9, ymin=ymin, ymax=ymax, neg=negf if neg else None, tn=C["s11.a"] + 0.4 * i)
        if s == "s08":
            raiz(c, t, tc + 0.4, Q, 1, rot=False)
            raiz(c, t, tc + 0.7, Q, 3, rot=False)
        elif s == "s09":
            raiz(c, t, C["s09.d"] + 0.4, Q, 2, rot=False)
        else:
            faixa_x(c, Q, ep(t, tc, 0.4) * (1 - ep(t, C["s11"], 0.4)), ERRADO)
        if lei_ and not neg:
            E.foco(c, t, C[s + ".c"], 0.5, lambda a, i=i, lei_=lei_: E.formula(c, lei_, CX[i] + 240, 880, 48, "g", TINTA, a, "center"))
            E.foco(c, t, C[s + ".c"] + 1.4, 0.5, lambda a, i=i, conta=conta: E.formula(c, conta, CX[i] + 240, 960, 46, "g", TINTA2, a, "center"))
        if s == "s09" and not neg:
            E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "x = f{4}{2} = 2", CX[1] + 240, 1040, 40, "g", ENT, a, "center"))
        if s == "s10" and not neg:
            E.foco(c, t, C["s10.d"], 0.4, lambda a: E.pilula(c, "inteira acima do eixo", CX[2] + 240, 1035, 34, "g", fundo=COR, a=a))
    if t >= C["s08"] and t < C["s08.a"] + 0.6:
        E.frase(c, t, C["s08"], ps("e o delta conta mais", "i", 72), W / 2, 540, "center")
    if neg:
        E.frase(c, t, C["s11.a"], [("a", "g", 66, CA), ("<", "g", 66, CA), ("0:", "g", 66, CA), ("de", "i", 62), ("cabeça", "g", 62), ("para", "i", 62), ("baixo", "g", 62)],
                W / 2, 900, "center")
        E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "Δ < 0: inteira abaixo do eixo", W / 2, 1000, 40, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
P5 = E.Plano(*PL, -1.5, 5.5, -1, 6)
M5 = ([-1, 0, 1, 2, 3, 4, 5], [-1, 0, 1, 2, 3, 4, 5, 6])


def b_erro(c, t, C, b):
    plano(c, t, C["s12"], P5, M5)
    E.ponto(c, t, C["s12.b"], P5, 0, 5, cor=COR, r=16)
    E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: par(c, "0", "5", P5.x(0) + 30, P5.y(5) - 20, 44, a))
    E.ponto(c, t, C["s12.c"], P5, 2, 1, cor=COR, r=16)
    E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: par(c, "2", "1", P5.x(2), P5.y(1) + 74, 44, a, "center"))
    E.curva(c, t, C["s12.c"] + 1.2, P5, f5, -0.4, 4.4, d=1.2, cor=COR)
    faixa_x(c, P5, ep(t, C["s12.d"], 0.4), ERRADO)
    fml(c, t, C["s12"] + 0.2, "f(x) = x^2 − 4x + 5", XE, 220, 64, TINTA)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: delta(c, "Δ < 0", XE + 100, 330, 50, ERRADO, a))
    E.frase(c, t, C["s12.a"] + 0.6, [("a", "i", 64, ERRADO), ("parábola", "g", 64, ERRADO), ("não", "i", 64, ERRADO), ("existe?", "g", 64, ERRADO)], XE + 240, 350)
    if t >= C["s12.b"] - 0.4:
        E.risco(c, XE + 230, 365, XE + 830, 300, t, C["s12.b"] - 0.4, largura=10)
    fml(c, t, C["s12.b"], "f(0) = 5", XE, 500, 72, TINTA)
    fml(c, t, C["s12.c"], "f(2) = 4 − 8 + 5 = 1", XE, 620, 72, TINTA)
    E.frase(c, t, C["s12.c"] + 1.6, [("os", "i", 64), ("pontos", "g", 64, CERTO), ("estão", "i", 64), ("lá", "i", 64)], XE, 740)
    E.frase(c, t, C["s12.d"], [("não", "i", 64), ("existe:", "i", 64), ("o", "i", 64), ("toque", "g", 64, ERRADO), ("no", "i", 64), ("eixo", "i", 64), ("x", "g", 70, ENT)], XE, 880)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    Q = E.plano(c, t, C["s13.b"], 1120, 230, 640, 640, -5.5, 3.5, -10, 6, marcas_x=[-5, -4, -3, -2, -1, 1, 2, 3], marcas_y=[-8, -6, -4, -2, 2, 4, 6],
                passo_y=2, escuro=True)
    if t >= C["s14.a"]:
        p = ep(t, C["s14.a"], 0.5) * (1 - ep(t, C["s14.c"], 0.4))
        if p > 0:
            for xv in (-5.2, 3.2):
                M.arrow(c, *Q(xv, 1.0), *Q(xv, 4.5), CLARO, p, 6, 20, p)
    if t >= C["s14.b"]:
        marca_ponto(c, t, C["s14.b"], *Q(0, -8), AMARELO, 22)
        E.foco(c, t, C["s14.b"] + 0.3, 0.4, lambda a: par(c, "0", "−8", Q.x(0) + 30, Q.y(-8) + 16, 42, a, cores=(CLARO, BR)))
    E.curva(c, t, C["s14.c"], Q, h, -5.3, 3.3, d=1.4, cor=CLARO)
    if t >= C["s14.c"] + 1.2:
        for k, xv in enumerate((-4, 2)):
            marca_ponto(c, t, C["s14.c"] + 1.2 + 0.3 * k, Q.x(xv), Q.oy, AMARELO, 20)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), XE, 200)
        E.frase(c, t, C["s13.a"], [("a", "g", 80, BR), ("e", "i", 72, CLARO), ("c", "g", 80, BR), ("com", "i", 72, CLARO), ("sinais", "i", 72, CLARO)], XE, 350)
        E.frase(c, t, C["s13.a"] + 1.0, [("contrários:", "g", 76, AMARELO)], XE, 460)
        E.frase(c, t, C["s13.a"] + 2.0, [("corta", "i", 70, CLARO), ("em", "i", 70, CLARO), ("2", "g", 76, BR), ("pontos", "g", 72, BR)], XE, 570)
        pos = lei_em(c, t, C["s13.b"], [("x^2", BR), (" + 2x", CLARO), (" − 8", BR)], XE, 760, 90)
        sob_parte(c, t, C["s13.b"] + 1.0, pos, 0, 760, "a > 0", BR, 46)
        sob_parte(c, t, C["s13.b"] + 1.6, pos, 2, 760, "c < 0", AMARELO, 46, apara=larg_f(" ", 90))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("olhe o desenho", "i", 70, CLARO), XE, 200)
    E.frase(c, t, C["s14.a"], [("a", "g", 70, BR), (">", "g", 70, BR), ("0:", "g", 70, BR), ("abre", "i", 64, CLARO), ("para", "i", 64, CLARO), ("cima", "g", 64, BR)], XE, 330)
    E.frase(c, t, C["s14.b"], [("c", "g", 70, AMARELO), ("<", "g", 70, AMARELO), ("0:", "g", 70, AMARELO), ("cruza", "i", 64, CLARO), ("o", "i", 64, CLARO), ("y", "g", 70, BR),
                               ("embaixo", "g", 64, BR)], XE, 440)
    E.frase(c, t, C["s14.c"], [("tem", "i", 64, CLARO), ("de", "i", 64, CLARO), ("cruzar", "i", 64, CLARO), ("o", "i", 64, CLARO), ("eixo", "i", 64, CLARO), ("x", "g", 70, BR)], XE, 580)
    E.frase(c, t, C["s14.c"] + 1.0, [("2", "g", 76, AMARELO), ("vezes", "g", 70, AMARELO)], XE, 680)
    E.frase(c, t, C["s14.d"], [("sinais", "i", 64, CLARO), ("iguais:", "i", 64, CLARO), ("calcule", "i", 64, CLARO), ("o", "i", 64, CLARO), ("Δ", "g", 76, BR)], XE, 860)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "f(x) = x^2 − 6x + 8", XE, 380, 86, "g", TINTA, a))
    E.frase(c, t, C["s15.a"] + 2.0, [("onde", "i", 60), ("corta", "i", 60), ("o", "i", 60), ("eixo", "i", 60), ("x?", "g", 66, ENT)], XE + 60, 480)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "g(x) = −x^2 + 2x − 1", XE, 640, 86, "g", TINTA, a))
    E.frase(c, t, C["s15.c"], [("corta,", "g", 62, CERTO), ("encosta", "g", 62, TINTA2), ("ou", "i", 60), ("não", "g", 62, ERRADO), ("toca?", "g", 62, ERRADO)], XE + 60, 740)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    plano(c, t, C["s17"], PQ, MQ)
    def graf17():
        E.curva(c, t, C["s17.c"], PQ, q1, 0.6, 5.4, d=1.0, cor=COR)
        raiz(c, t, C["s17.c"] + 0.3, PQ, 2, lado=-1)
        raiz(c, t, C["s17.c"] + 0.6, PQ, 4)
    E.saida(c, t, C["s18"] - 0.1, graf17)

    def s17():
        fml(c, t, C["s17"], "f(x) = x^2 − 6x + 8", XE, 220, 66, TINTA)
        fml(c, t, C["s17.a"], "Δ = 36 − 32 = 4", XE, 370, 72, TINTA)
        fml(c, t, C["s17.b"] - 1.6, "x = f{6 ± 2}{2}", XE, 540, 76, COR)
        E.foco(c, t, C["s17.b"], 0.4, lambda a: E.formula(c, "x = 4  ou  x = 2", XE, 700, 76, "g", ENT, a))
        E.frase(c, t, C["s17.c"], [("corta", "i", 64), ("no", "i", 64), ("2", "g", 70, ENT), ("e", "i", 64), ("no", "i", 64), ("4", "g", 70, ENT)], XE, 850)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.curva(c, t, C["s18.d"], PQ, q2, -1.2, 3.2, d=1.0, cor=TINTA)
    if t >= C["s18.d"] + 0.6:
        marca_ponto(c, t, C["s18.d"] + 0.6, PQ.x(1), PQ.oy, ENT, 20)
        E.foco(c, t, C["s18.d"] + 0.9, 0.4, lambda a: par(c, "1", "0", PQ.x(1) + 30, PQ.oy - 30, 42, a))
    pos = lei_em(c, t, C["s18"], [("g(x) = ", TINTA), ("−x^2", CA), (" + 2x", CB), (" − 1", CC)], XE, 220, 70)
    sob_parte(c, t, C["s18"] + 0.6, pos, 1, 220, "a = −1", CA, 42)
    sob_parte(c, t, C["s18"] + 1.6, pos, 3, 220, "c = −1", CC, 42, apara=larg_f(" ", 70))
    E.foco(c, t, C["s18.a"] - 1.6, 0.4, lambda a: E.pilula(c, "sinais iguais: o atalho não decide", XE + 330, 380, 36, "g", fundo=TINTA2, a=a))
    fml(c, t, C["s18.a"], "Δ = 2^2 − 4 · (−1) · (−1)", XE, 510, 66, TINTA)
    fml(c, t, C["s18.b"], "Δ = 4 − 4 = 0", XE, 620, 72, TINTA)
    E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: delta(c, "Δ = 0", XE + 640, 600, 44, TINTA2, a))
    fml(c, t, C["s18.c"], "x = f{−2}{−2} = 1", XE, 790, 72, ENT)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "abre para baixo e encosta em (1, 0)", XE + 380, 930, 38, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("raiz:", "g", 80, ENT), ("onde", "i", 80), ("a", "i", 80), ("parábola", "i", 80), ("toca", "g", 80), ("o", "i", 80), ("eixo", "i", 80), ("x", "g", 86, ENT)]),
                 ("s19.b", [("sinal", "i", 80), ("do", "i", 80), ("Δ:", "g", 86, COR), ("corta,", "g", 80, CERTO), ("encosta", "g", 80, TINTA2), ("ou", "i", 80), ("não", "g", 80, ERRADO),
                            ("toca", "g", 80, ERRADO)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 220, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 220 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s20.a"], [("o", "i", 120), ("vértice", "g", 140, COR)], XE, 470)
    E.frase(c, t, C["s20.a"] + 1.0, ps("onde a parábola faz a curva", "i", 60, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s20.b"], [("no", "i", 60, TINTA2), ("meio", "g", 64), ("do", "i", 60, TINTA2), ("1", "g", 64, ENT), ("e", "i", 60, TINTA2), ("do", "i", 60, TINTA2), ("3", "g", 64, ENT)], XE, 680)
    Q = E.Plano(1280, 530, 380, 230, -1, 5, -1.5, 3.5)
    E.plano(c, t, C["s20.a"], 1280, 530, 380, 230, -1, 5, -1.5, 3.5, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, C["s20.a"] + 0.3, Q, f, -0.5, 4.5, d=1.0, cor=COR, largura=8)
    if t >= C["s20.b"]:
        for xv in (1, 3):
            marca_ponto(c, t, C["s20.b"], *Q(xv, 0), ENT, 14)
        a_ = ep(t, C["s20.b"] + 0.4, 0.5)
        M.line(c, Q.x(2), Q.y(3.3), Q.x(2), Q.y(-1), TINTA, a_, 4, dash=E.TRACO)
        E.ponto(c, t, C["s20.b"] + 0.6, Q, 2, -1, cor=AMARELO, r=14)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, exemplo=b_exemplo, casos=b_casos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
