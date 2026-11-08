"""Visual — Estudativo · MAT-FUN-013: função linear e grandezas proporcionais.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Nesta aula: a reta do feijão (y = 8x) em índigo, que passa pela origem; a reta do táxi (P = 5 + 2,5d) em preto, que corta o eixo y
no 5. A origem, quando decide a resposta, ganha um anel (verde: passa; vermelho: não passa). As barras empilhadas do táxi mostram a
bandeirada (preto) que fica e a parte dos quilômetros (índigo) que dobra.
Peças locais: eixos() com marcas escolhidas, par(), tabela(), anel(), pilha()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
ARQUIVO_FINAL = "estudativo_MAT-FUN-013_funcao_linear_e_grandezas_proporcionais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("feijao", "grafico", "taxi", "atalho", "questao", "fim"))
BR = "#FFFFFF"

feijao = lambda x: 8 * x
taxi = lambda x: 5 + 2.5 * x
reta_a = lambda x: 12 * x
reta_b = lambda x: 20 + 8 * x
assert [feijao(x) for x in (0, 1, 2, 3)] == [0, 8, 16, 24] and 16 / 2 == 8 and 24 / 3 == 8
assert taxi(0) == 5 and taxi(2) == 10 and taxi(4) == 15 and 10 / 2 == 5 and 15 / 4 == 3.75
assert reta_a(5) == 60 and reta_b(0) == 20 and reta_b(5) == 60 and reta_b(10) == 100 and 60 / 5 == 12 and 100 / 10 == 10
assert 80 / 10 == 8 and 96 / 12 == 8

PL = (1080, 190, 700, 700)
PF = E.Plano(*PL, 0, 4.4, 0, 35)  # feijão
MF = ([1, 2, 3, 4], [8, 16, 24, 32])
PT = E.Plano(*PL, 0, 6.5, 0, 21)  # táxi
MT = ([1, 2, 3, 4, 5, 6], [5, 10, 15, 20])
PQ = E.Plano(*PL, 0, 11, 0, 130)  # questão
MQ = (list(range(1, 11)), [20, 40, 60, 80, 100, 120])


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


def eixos(c, t, P, tx, ty=None, tg=None, marcas=None, size=38, rot=True, esp=4, rx=None):
    """plano em etapas (o da MAT-FUN-001), com marcas escolhidas: grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty.
    rx = só estes valores de x ganham número (os outros, só o traço)"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    mx, my = marcas or (list(range(int(P.xmin), int(P.xmax) + 1)), list(range(int(P.ymin), int(P.ymax) + 1)))
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, esp + 2, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(mx):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                rot and (rx is None or v in rx) and centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
        if rot:
            E.foco(c, t, tx + 0.2, 0.4, lambda a: E.escreve(c, "0", P.ox - 16 - E.larg("0", "b", size), P.oy + 14 + size, size, "b", TINTA2, a))
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, esp + 2, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(my):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                rot and E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas"""
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
    """anel que se abre num ponto: chama a atenção para ele"""
    p = prog(t, t0, d)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def marca_ponto(c, t, t0, X, Y, cor, r=26):
    """círculo fixo em volta de um ponto (a origem que decide)"""
    q = ease_back(prog(t, t0, 0.5))
    if q > 0:
        c.drawCircle(X, Y, r * q, M.paint(cor, 0.22))
        c.drawCircle(X, Y, r * q, M.paint(cor, 1.0, stroke=6))
    anel(c, t, t0, X, Y, cor)


def tabela(c, t, x, y, cab, cores, linhas, tc, tcel, wc=200, hl=92, size=64, destaque=None, cab_size=50):
    """tabela em pé: cab = cabeçalhos, linhas = textos, tcel[i][j] = instante de cada célula (None = vazia)"""
    n = len(cab)
    a = ep(t, tc, 0.5)
    if a > 0:
        for j, (h_, cor) in enumerate(zip(cab, cores)):
            centro(c, h_, x + wc * j + wc / 2, y - 24, cab_size, "i", cor, a)
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


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def reta_volta(c, t, t0, P, f, x0, x1, cor=COR, d=1.0, largura=7):
    """reta desenhada da direita (x1) para a esquerda (x0): a reta "prolongada para trás" """
    p = ease_io(prog(t, t0, d))
    if p > 0:
        (ax, ay), (bx, by) = P(x1, f(x1)), P(x0, f(x0))
        M.line(c, ax, ay, lerp(ax, bx, p), lerp(ay, by, p), cor, 1.0, largura)


def pilha(c, P, xv, fixo, total, a, w=72):
    """barra em pé no x: a parte fixa (preta) embaixo e o resto (índigo) em cima, com os valores dentro"""
    if a <= 0:
        return
    X = P.x(xv)
    y0, y1, y2 = P.oy, P.y(fixo), P.y(total)
    c.drawRect(skia.Rect.MakeLTRB(X - w / 2, y1, X + w / 2, y0), M.paint(TINTA, 0.85 * a))
    c.drawRect(skia.Rect.MakeLTRB(X - w / 2, y2, X + w / 2, y1), M.paint(COR, 0.85 * a))
    centro(c, E._num(fixo), X, (y0 + y1) / 2 + 15, 40, "g", BR, a)
    centro(c, E._num(total - fixo), X, (y1 + y2) / 2 + 15, 40, "g", BR, a)


# ---------------- gancho ----------------
Q1 = E.Plano(250, 300, 560, 480, 0, 4.4, 0, 35)
Q2 = E.Plano(1110, 300, 560, 480, 0, 6.5, 0, 21)


def b_gancho(c, t, C, b):
    def cena1():
        eixos(c, t, Q1, C["s01.a"], marcas=MF, rot=False)
        eixos(c, t, Q2, C["s01.a"] + 0.2, marcas=MT, rot=False)
        E.curva(c, t, C["s01.b"], Q1, feijao, 0, 4.4, d=1.0, largura=8)
        E.curva(c, t, C["s01.b"] + 0.3, Q2, taxi, 0, 6.5, d=1.0, largura=8, cor=TINTA)
        E.frase(c, t, C["s01.b"] + 1.6, [("feijão", "g", 72, COR)], 530, 920, "center")
        E.frase(c, t, C["s01.b"] + 3.4, [("táxi", "g", 72)], 1390, 920, "center")
        if t >= C["s01.c"]:
            for Q in (Q1, Q2):
                q = ep(t, C["s01.c"] + 0.3, 0.4)
                c.drawCircle(Q.ox, Q.oy, 26, M.paint(COR, q, stroke=6))
                for k in range(3):
                    anel(c, t, C["s01.c"] + 0.3 + 0.9 * k, Q.ox, Q.oy)
            E.frase(c, t, C["s01.c"], [("só", "i", 72), ("uma", "i", 72), ("é", "i", 72), ("proporcional", "g", 72, COR)], W / 2, 180, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.2, [("proporção", "g", 120, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.6, ps("no gráfico", "i", 96), XE, 570)
        E.frase(c, t, C["s02.a"] + 2.6, [("e", "i", 90), ("o", "i", 90), ("número", "g", 96), ("que", "i", 90), ("liga", "i", 90)], XE, 730)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.a", "função afim, gráfico reta:", lambda a, y: E.formula(c, "f(x) = ax + b", x + 44, y, 76, "g", COR, a)),
             ("s03.b", "o teste do dobro:", lambda a, y: (E.escreve(c, "dobra e dobra:", x + 44, y, 62, "g", TINTA, a),
                                                       E.escreve(c, "direta", x + 520, y, 62, "g", CERTO, a))))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.a"], 0.4))


# ---------------- feijão ----------------
TX, TY = 300, 330


def tab_feijao(c, t, tc, tl, destaque=None, extra=None):
    """quilos | reais, com o 0 na primeira linha (que só entra quando a fala chega nele)"""
    linhas = [("0", "0"), ("1", "8"), ("2", "16"), ("3", "24")]
    cab, cores = ["quilos", "reais"], [ENT, SAI]
    tcel = [[ti, ti] for ti in tl]
    if extra:
        cab.append("y ÷ x"); cores.append(CERTO)
        for i, v in enumerate(extra):
            linhas[i] = linhas[i] + (v[0],)
            tcel[i].append(v[1])
    tabela(c, t, TX, TY, cab, cores, linhas, tc, tcel, wc=210, destaque=destaque)


def b_feijao(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], [("feijão:", "g", 80, COR), ("R$", "g", 80), ("8", "g", 80), ("o", "i", 80), ("quilo", "i", 80)], XE, 190)
        destaque = lambda i: pulso(t, C["s04.d"], 2.6) if i == 0 else 0
        tab_feijao(c, t, C["s04.a"] - 0.3, (C["s04.d"], C["s04.a"], C["s04.b"], C["s04.c"]), destaque)
        E.frase(c, t, C["s04.d"] + 0.8, [("não", "i", 70), ("leva", "i", 70), ("nada,", "i", 70)], 1020, 450)
        E.frase(c, t, C["s04.d"] + 1.6, [("não", "i", 70), ("paga", "g", 70, COR), ("nada", "g", 70, COR)], 1020, 550)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    tab_feijao(c, t, C["s05"] - 2, [C["s05"] - 2] * 4)
    fml(c, t, C["s05.a"], "y = 8x", 1020, 450, 150, COR)
    E.frase(c, t, C["s05.a"] + 1.0, [("8", "g", 64, COR), ("vezes", "i", 64), ("os", "i", 64), ("quilos", "i", 64, ENT)], 1020, 560)
    fml(c, t, C["s05.b"], "y = 8x + 0", 1020, 770, 96, TINTA)
    q = ep(t, C["s05.b"] + 0.5, 0.4)
    if q > 0:
        w0 = E.formula(None, "y = 8x ", 1020, 770, 96, "g", a=0)
        w1 = E.formula(None, "+ 0", 0, 0, 96, "g", a=0)
        E.caixa_pontilhada(c, 1020 + w0 - 2, 680, w1 + 30, 120, q, ERRADO, q)
    E.foco(c, t, C["s05.b"] + 0.9, 0.4, lambda a: E.pilula(c, "b = 0: sem parte fixa", 1340, 880, 46, "g", fundo=TINTA, a=a))


# ---------------- função linear ----------------
def b_linear(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06"], [("afim", "g", 80), ("com", "i", 80), ("b", "g", 80, COR), ("=", "g", 80, COR), ("0", "g", 80, COR)], XE, 220)
        E.frase(c, t, C["s06.a"], [("função", "g", 150, COR), ("linear", "g", 150, COR)], XE, 420)
        fml(c, t, C["s06.b"], "y = kx", XE, 640, 170, TINTA)
        E.frase(c, t, C["s06.b"] + 1.2, [("k:", "g", 66, COR), ("um", "i", 66), ("número", "i", 66), ("fixo", "g", 66)], 900, 610)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.bola(c, 470, 860, 110, a=a), centro(c, "k = 8", 470, 885, 70, "g", BR, a)))
        E.frase(c, t, C["s06.c"] + 0.6, [("o", "i", 70), ("preço", "g", 70), ("de", "i", 70), ("1", "g", 70, ENT), ("quilo", "i", 70, ENT)], 640, 885)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return

    def topo():
        E.frase(c, t, C["s07.a"], [("linear", "g", 84, COR), ("=", "g", 84), ("diretamente", "i", 84), ("proporcional", "i", 84)], W / 2, 220, "center")
        fml(c, t, C["s07.b"] - 1.0, "x → 2x", W / 2, 470, 120, ENT, "center")
        fml(c, t, C["s07.b"], "k · 2x = 2 · kx", W / 2, 680, 120, TINTA, "center")
        E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.pilula(c, "o dobro do resultado", W / 2, 840, 54, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s07.c"] - 0.2, topo)
    if t < C["s07.c"] - 0.2:
        return
    destaque = lambda i: (ep(t, C["s07.c"], 0.3) * (1 - ep(t, C["s07.d"] - 0.2, 0.3)) if i == 2 else
                          ep(t, C["s07.d"], 0.3) * (1 - ep(t, C["s07.e"] - 0.2, 0.3)) if i == 3 else 0)
    t0 = C["s07.c"] - 0.2
    tab_feijao(c, t, t0, [t0] * 4, destaque, extra=[("", None), ("8", C["s07.e"]), ("8", C["s07.c"] + 0.6), ("8", C["s07.d"] + 0.6)])
    fml(c, t, C["s07.c"], "16 ÷ 2 = 8", 1080, 470, 96, TINTA)
    fml(c, t, C["s07.d"], "24 ÷ 3 = 8", 1080, 620, 96, TINTA)
    E.foco(c, t, C["s07.e"], 0.6, lambda a: (E.bola(c, 1200, 820, 90, a=a), centro(c, "k", 1200, 848, 96, "g", BR, a)))
    E.frase(c, t, C["s07.e"] + 0.5, [("constante", "g", 60, COR)], 1320, 810)
    E.frase(c, t, C["s07.e"] + 0.8, [("de", "i", 60), ("proporcionalidade", "i", 60)], 1320, 880)


# ---------------- gráfico ----------------
PTS_F = ((1, 8), (2, 16), (3, 24))


def b_grafico(c, t, C, b):
    eixos(c, t, PF, C["s08"], tg=C["s08"], marcas=MF)
    for k, (xv, yv) in zip(("s08.a", "s08.b", "s08.c"), PTS_F):
        E.ponto(c, t, C[k], PF, xv, yv, guias=True, cor=COR, r=16)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, xv=xv, yv=yv: par(c, str(xv), str(yv), PF.x(xv) - 24, PF.y(yv) - 26, 44, a, "right"))
    reta_volta(c, t, C["s08.d"], PF, feijao, 0, 4.3, d=1.2)
    if t >= C["s08.d"] + 1.0:
        marca_ponto(c, t, C["s08.d"] + 1.0, PF.ox, PF.oy, CERTO)
    E.frase(c, t, C["s08"], [("vamos", "i", 76), ("ao", "i", 76), ("gráfico", "g", 76, COR)], XE, 230)
    xx = XE
    for k, (xv, yv) in zip(("s08.a", "s08.b", "s08.c"), PTS_F):
        par_em(c, t, C[k], str(xv), str(yv), xx, 370, 68)
        xx += par(None, str(xv), str(yv), 0, 0, 68, 0) + 40

    def s08():
        E.frase(c, t, C["s08.d"], [("passa", "i", 80), ("pela", "i", 80)], XE, 560)
        E.frase(c, t, C["s08.d"] + 0.6, [("origem", "g", 110, CERTO)], XE, 690)
        par_em(c, t, C["s08.d"] + 1.0, "0", "0", XE + 500, 690, 76)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    fml(c, t, C["s09.a"], "x = 0", XE, 560, 84, ENT)
    fml(c, t, C["s09.a"] + 0.4, "k · 0 = 0", XE + 340, 560, 84, TINTA)
    E.frase(c, t, C["s09.b"], [("toda", "i", 76), ("linear:", "g", 76, COR)], XE, 720)
    E.frase(c, t, C["s09.b"] + 0.6, [("reta", "g", 76), ("pela", "i", 76), ("origem", "g", 76, CERTO)], XE, 830)


# ---------------- táxi ----------------
def b_taxi(c, t, C, b):
    eixos(c, t, PT, C["s10"], tg=C["s10"], marcas=MT)
    E.curva(c, t, C["s10.c"], PT, taxi, 0, 6.5, d=1.2, cor=TINTA)
    E.ponto(c, t, C["s10.b"], PT, 0, 5, cor=TINTA, r=17)
    if t >= C["s10.b"]:
        anel(c, t, C["s10.b"], *PT(0, 5), TINTA)
    if t >= C["s10.c"] + 0.8:
        marca_ponto(c, t, C["s10.c"] + 0.8, PT.ox, PT.oy, ERRADO, 22)
        anel(c, t, C["s10.c"] + 1.2, *PT(0, 5), TINTA)

    def s10():
        E.frase(c, t, C["s10"], [("o", "i", 76), ("táxi", "g", 80)], XE, 220)
        fml(c, t, C["s10.a"], "P = 5 + 2,5d", XE, 360, 100, TINTA)
        E.frase(c, t, C["s10.a"] + 2.0, [("b", "g", 70, COR), ("=", "g", 70), ("5:", "g", 70), ("a", "i", 70), ("bandeirada", "g", 70)], XE, 480)
        E.frase(c, t, C["s10.b"], [("0", "g", 70, ENT), ("km", "i", 70, ENT), ("→", "g", 70, TINTA2), ("R$", "g", 70), ("5", "g", 70)], XE, 620)
        E.frase(c, t, C["s10.c"], [("corta", "i", 70), ("o", "i", 70), ("eixo", "i", 70), ("y", "g", 80), ("no", "i", 70), ("5", "g", 80)], XE, 760)
        E.frase(c, t, C["s10.c"] + 0.8, [("acima", "g", 66, ERRADO), ("da", "i", 66), ("origem", "i", 66)], XE, 860)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.ponto(c, t, C["s11.a"], PT, 2, 10, guias=True, cor=COR, r=16)
    E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: par(c, "2", "10", PT.x(2) - 24, PT.y(10) - 26, 44, a, "right"))
    E.ponto(c, t, C["s11.b"], PT, 4, 15, guias=True, cor=COR, r=16)
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: par(c, "4", "15", PT.x(4) - 24, PT.y(15) - 26, 44, a, "right"))
    # o que seria proporcional: 20, fantasma vermelho
    tf = C["s11.b"] + 1.6
    if t >= tf:
        q = ep(t, tf, 0.4) * (1 - ep(t, C["s11.c"] - 0.2, 0.4))
        if q > 0:
            X, Y = PT(4, 20)
            c.drawCircle(X, Y, 16, M.paint(ERRADO, q, stroke=5))
            E.escreve(c, "20?", X + 26, Y + 16, 46, "g", ERRADO, q)
    qp = ep(t, C["s11.c"], 0.5)
    pilha(c, PT, 2, 5, 10, qp)
    pilha(c, PT, 4, 5, 15, ep(t, C["s11.c"] + 0.5, 0.5))
    E.frase(c, t, C["s11"], ps("o teste do dobro", "i", 72), XE, 220)
    E.frase(c, t, C["s11.a"], [("2", "g", 76, ENT), ("km", "i", 76, ENT), ("→", "g", 76, TINTA2), ("R$", "g", 76), ("10", "g", 76)], XE, 360)
    E.frase(c, t, C["s11.b"], [("4", "g", 76, ENT), ("km", "i", 76, ENT), ("→", "g", 76, TINTA2), ("R$", "g", 76), ("15", "g", 76)], XE, 470)
    E.saida(c, t, C["s11.c"] - 0.2, lambda: E.frase(c, t, tf, [("proporcional:", "i", 66, ERRADO), ("R$", "g", 66, ERRADO), ("20", "g", 66, ERRADO)], XE, 580))
    E.frase(c, t, C["s11.c"], [("km:", "i", 66, COR), ("5", "g", 66, COR), ("→", "g", 66, TINTA2), ("10", "g", 66, COR), ("dobrou", "g", 60, COR)], XE, 600)
    E.frase(c, t, C["s11.c"] + 0.8, [("bandeirada:", "i", 66), ("5", "g", 66), ("→", "g", 66, TINTA2), ("5", "g", 66)], XE, 700)
    E.foco(c, t, C["s11.end"] - 2.6, 0.5, lambda a: E.pilula(c, "não é proporcional", XE + 330, 840, 56, "g", fundo=ERRADO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    eixos(c, t, PT, C["s12"] - 3, tg=C["s12"] - 3, marcas=MT)
    E.curva(c, t, C["s12"] - 3, PT, taxi, 0, 6.5, d=0.05, cor=TINTA)
    E.ponto(c, t, C["s12.b"], PT, 2, 10, cor=COR, r=16)
    E.ponto(c, t, C["s12.c"], PT, 4, 15, cor=COR, r=16)
    E.frase(c, t, C["s12.a"], [("toda", "i", 76), ("reta", "i", 76), ("que", "i", 76), ("sobe", "g", 76, ERRADO)], XE, 230)
    E.frase(c, t, C["s12.a"] + 0.8, [("é", "i", 76), ("proporcional?", "g", 76, ERRADO)], XE, 330)
    if t >= C["s12.a"] + 1.4:
        E.risco(c, XE - 10, 350, XE + 720, 190, t, C["s12.a"] + 1.4, largura=12)
    fml(c, t, C["s12.b"], "10 ÷ 2 = 5", XE, 490, 90, TINTA)
    fml(c, t, C["s12.c"], "15 ÷ 4 = 3,75", XE, 610, 90, TINTA)
    E.foco(c, t, C["s12.d"] - 1.4, 0.4, lambda a: E.pilula(c, "mudou", 850, 580, 44, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s12.d"], [("subir", "i", 72), ("não", "g", 72, ERRADO), ("basta", "i", 72)], XE, 770)
    E.frase(c, t, C["s12.d"] + 0.8, [("precisa", "i", 72), ("passar", "i", 72), ("pela", "i", 72), ("origem", "g", 72, CERTO)], XE, 870)
    if t >= C["s12.d"] + 0.8:
        marca_ponto(c, t, C["s12.d"] + 0.8, PT.ox, PT.oy, CERTO, 22)
        E.curva(c, t, C["s12.d"] + 1.2, PT, lambda x: 5 * x, 0, 4.1, d=0.9, cor=CERTO, tracejada=True, largura=6)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 72, CLARO), XE, 180)
        E.frase(c, t, C["s13.a"], [("reta", "i", 76, CLARO), ("pela", "i", 76, CLARO), ("origem:", "g", 76, BR)], XE, 330)
        E.frase(c, t, C["s13.a"] + 1.4, [("1", "g", 90, BR), ("ponto", "i", 76, CLARO), ("dá", "i", 76, CLARO), ("o", "i", 76, CLARO), ("k", "g", 90, BR)], XE, 440)
        fml(c, t, C["s13.b"], "k = f{y}{x}", XE, 640, 150, BR)
        fml(c, t, C["s13.c"] + 0.8, "k = f{24}{3} = 8", XE, 900, 110, CLARO)
        Q = E.plano(c, t, C["s13.a"], 1100, 220, 640, 640, 0, 4.4, 0, 35, marcas_x=[1, 2, 3, 4], marcas_y=[8, 16, 24, 32], passo_y=8, escuro=True)
        E.curva(c, t, C["s13.a"] + 0.5, Q, feijao, 0, 4.4, d=1.0, cor=CLARO)
        c.drawCircle(Q.ox, Q.oy, 22 * ep(t, C["s13.a"] + 1.2, 0.4), M.paint(CERTO, 1.0, stroke=6))
        E.ponto(c, t, C["s13.c"], Q, 3, 24, guias=True, cor=BR, r=17)
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: par(c, "3", "24", Q.x(3) - 24, Q.y(24) - 26, 46, a, "right", (CLARO, BR)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return

    def s14a():
        fml(c, t, C["s14.a"], "y = k · x", XE, 300, 110, BR)
        E.foco(c, t, C["s14.a"] + 1.2, 0.4, lambda a: E.escreve(c, "→", XE + 520, 290, 100, "g", CLARO, a))
        fml(c, t, C["s14.a"] + 1.6, "f{y}{x} = k", XE + 660, 300, 110, BR)
    E.saida(c, t, C["s14.b"] - 0.1, s14a)
    if t < C["s14.b"]:
        return
    E.frase(c, t, C["s14.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 72, CLARO)], XE, 230)
    E.frase(c, t, C["s14.b"] + 0.7, [("eixos", "i", 72, CLARO), ("longe", "g", 72, BR), ("do", "i", 72, CLARO), ("zero", "g", 72, BR)], XE, 330)
    Q = E.plano(c, t, C["s14.b"] + 0.4, 1100, 220, 640, 640, 9, 14.4, 70, 116, marcas_x=[10, 11, 12, 13, 14], marcas_y=[80, 90, 100, 110],
                passo_y=10, escuro=True)
    E.curva(c, t, C["s14.b"] + 1.0, Q, feijao, 9, 14.4, d=1.0, cor=CLARO)
    E.foco(c, t, C["s14.b"] + 1.4, 0.4, lambda a: centro(c, "sem a origem (0, 0)", 1440, 1000, 52, "i", ERRADO, a))
    E.frase(c, t, C["s14.c"], [("divida", "i", 72, CLARO), ("em", "i", 72, CLARO), ("2", "g", 80, BR), ("pontos", "g", 72, BR)], XE, 480)
    E.ponto(c, t, C["s14.c"] + 0.3, Q, 10, 80, guias=True, cor=BR, r=16)
    E.ponto(c, t, C["s14.c"] + 0.9, Q, 12, 96, guias=True, cor=BR, r=16)
    fml(c, t, C["s14.c"] + 0.4, "80 ÷ 10 = 8", XE, 620, 84, CLARO)
    fml(c, t, C["s14.c"] + 1.0, "96 ÷ 12 = 8", XE, 740, 84, CLARO)
    E.foco(c, t, C["s14.end"] - 1.6, 0.5, lambda a: E.pilula(c, "mesmo número: proporcional", XE + 390, 870, 50, "g", fundo=CERTO, a=a))


# ---------------- questão ----------------
def retas_q(c, t, ta, tb, d=1.0):
    E.curva(c, t, ta, PQ, reta_a, 0, 10.8, d=d, cor=COR)
    E.curva(c, t, tb, PQ, reta_b, 0, 11, d=d, cor=TINTA)
    E.foco(c, t, ta + d * 0.8, 0.4, lambda a: E.pilula(c, "A", *PQ(9.3, 123), 46, "g", fundo=COR, a=a))
    E.foco(c, t, tb + d * 0.8, 0.4, lambda a: E.pilula(c, "B", *PQ(10.3, 90), 46, "g", fundo=TINTA, a=a))


def b_questao(c, t, C, b):
    eixos(c, t, PQ, C["s15"], tg=C["s15"], marcas=MQ, size=34, rx=[2, 4, 5, 6, 8, 10])
    retas_q(c, t, C["s15.a"], C["s15.a"] + 0.4)
    E.ponto(c, t, C["s15.b"], PQ, 5, 60, guias=True, cor=COR, r=17)
    E.foco(c, t, C["s15.b"] + 0.3, 0.4, lambda a: par(c, "5", "60", PQ.x(5) + 30, PQ.y(60) + 60, 44, a))
    if t >= C["s15.b"]:
        anel(c, t, C["s15.b"] - 0.2, PQ.ox, PQ.oy)
    E.ponto(c, t, C["s15.c"], PQ, 0, 20, cor=TINTA, r=17)
    if t >= C["s15.c"]:
        anel(c, t, C["s15.c"], *PQ(0, 20), TINTA)
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 66, COR), XE, 190)
    E.frase(c, t, C["s15.b"] - 1.2, [("A:", "g", 66, COR), ("origem", "i", 64), ("e", "i", 64)], XE, 320)
    par_em(c, t, C["s15.b"], "5", "60", XE + 430, 320, 66)
    E.frase(c, t, C["s15.c"] - 0.6, [("B:", "g", 66), ("corta", "i", 64), ("o", "i", 64), ("y", "g", 66), ("no", "i", 64), ("20", "g", 66)], XE, 430)
    E.frase(c, t, C["s15.c"] + 0.9, [("e", "i", 64), ("passa", "i", 64), ("por", "i", 64)], XE + 90, 530)
    par_em(c, t, C["s15.c"] + 1.3, "5", "60", XE + 500, 530, 66)
    E.frase(c, t, C["s15.d"], [("qual", "i", 76), ("é", "i", 76), ("proporcional?", "g", 72, COR)], XE, 680)
    E.frase(c, t, C["s15.d"] + 1.5, [("o", "i", 70), ("k", "g", 76, COR), ("e", "i", 70), ("a", "i", 70), ("lei?", "g", 72, COR)], XE, 780)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=820, cy=860, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eixos(c, t, PQ, C["s17"] - 3, tg=C["s17"] - 3, marcas=MQ, size=34, rx=[2, 4, 5, 6, 8, 10])
    retas_q(c, t, C["s17"] - 3, C["s17"] - 3, d=0.05)
    E.ponto(c, t, C["s17"] - 3, PQ, 5, 60, cor=COR, r=17)
    E.ponto(c, t, C["s17"] - 3, PQ, 0, 20, cor=TINTA, r=17)
    if t < C["s18"]:
        q = ep(t, C["s17"], 0.4)
        if q > 0:
            c.saveLayerAlpha(None, int(70 * q)); E.curva(c, t, 0, PQ, reta_a, 0, 10.8, d=0.01, cor=COR, largura=24); c.restore()
        if t >= C["s17.a"]:
            marca_ponto(c, t, C["s17.a"], PQ.ox, PQ.oy, CERTO, 22)
        E.frase(c, t, C["s17"], [("reta", "i", 76), ("A", "g", 80, COR)], XE, 220)
        E.foco(c, t, C["s17.a"], 0.5, lambda a: E.pilula(c, "proporcional", 600, 195, 44, "g", fundo=CERTO, a=a))
        fml(c, t, C["s17.b"], "k = f{60}{5} = 12", XE, 470, 110, TINTA)
        E.foco(c, t, C["s17.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 620, 640, 190, 40, CERTO, a),
                                                 E.formula(c, "y = 12x", XE + 300, 750, 120, "g", BR, a, "center")))
        return
    # a reta B
    q = ep(t, C["s18"], 0.4)
    if q > 0:
        c.saveLayerAlpha(None, int(70 * q)); E.curva(c, t, 0, PQ, reta_b, 0, 11, d=0.01, cor=TINTA, largura=24); c.restore()
    if t >= C["s18.a"]:
        marca_ponto(c, t, C["s18.a"], PQ.ox, PQ.oy, ERRADO, 22)
    E.frase(c, t, C["s18"], [("reta", "i", 76), ("B", "g", 80)], XE, 220)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.pilula(c, "não é proporcional", 640, 195, 44, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s18.b"] - 1.0, [("armadilha:", "g", 64, ERRADO)], XE, 360)
    if t >= C["s18.b"]:
        anel(c, t, C["s18.b"], *PQ(5, 60))
    fml(c, t, C["s18.b"] + 0.4, "f{60}{5} = 12", XE, 500, 96, TINTA)
    E.ponto(c, t, C["s18.c"], PQ, 10, 100, guias=True, cor=TINTA, r=17)
    E.foco(c, t, C["s18.c"] + 0.3, 0.4, lambda a: (M.rrect(c, PQ.x(10) - 230, PQ.y(100) - 82, 216, 64, 14, "#F4F3EF", 0.95 * a),
                                                    par(c, "10", "100", PQ.x(10) - 24, PQ.y(100) - 34, 44, a, "right")))
    fml(c, t, C["s18.c"] + 0.8, "f{100}{10} = 10", XE, 680, 96, ERRADO)
    E.frase(c, t, C["s18.d"], [("fora", "i", 70), ("da", "i", 70), ("origem,", "g", 70, ERRADO)], XE, 850)
    E.frase(c, t, C["s18.d"] + 0.8, [("1", "g", 76, ERRADO), ("ponto", "i", 70), ("só", "i", 70), ("engana", "g", 70, ERRADO)], XE, 950)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", lambda a, y: E.escreve(c, "reta pela origem: proporcional", 400, y, 84, "g", TINTA, a)),
                 ("s19.b", lambda a, y: E.formula(c, "k = f{y}{x}", 400, y + 10, 100, "g", COR, a)))
        for i, (k, fn) in enumerate(itens):
            y = 450 + i * 240
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s20.a"], [("custo", "g", 130, COR), ("e", "i", 120), ("receita", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s20.b"], ps("quantas peças vender", "i", 66, TINTA2), XE, 600, passo=0.1)
    E.frase(c, t, C["s20.b"] + 1.0, [("para", "i", 66), ("sair", "i", 66), ("do", "i", 66), ("prejuízo", "g", 66, ERRADO)], XE, 690)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, feijao=b_feijao, linear=b_linear, grafico=b_grafico, taxi=b_taxi, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
