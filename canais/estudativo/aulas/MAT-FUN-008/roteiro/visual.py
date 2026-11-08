"""Visual — Estudativo · MAT-FUN-008: praticando o que é função (fórmula, tabelas, domínio e gráfico).

Linguagem visual da trilha Funções (MAT-FUN-001 a 007): entrada / x em índigo (ENT), saída / y em preto (SAI); eixo x índigo, eixo y preto;
par (x, y) com o x índigo e o y preto; plano na metade direita e texto à esquerda.
Nesta aula (prática), a pergunta da trilha "é o x ou o y?" vira uma etiqueta: pílula índigo "entrada · x" ou pílula preta "saída · y"
(etiqueta()) colada no número dado. Tabelas de duas colunas (tabela2(), a mesma da MAT-FUN-002): a linha culpada ganha faixa vermelha.
Teste da reta vertical num V: régua tracejada preta e anel verde no único toque (regua(), toque(), os mesmos da MAT-FUN-006).
Domínio na reta: E.reta + E.intervalo (MAT-FUN-005). Gráfico do reservatório: eixos(), guia(), anda(), barra() da MAT-FUN-007;
a reta y = 6 é um tracejado preto deitado.
Peças locais: mista(), etiqueta(), tabela2(), faixa(), regua(), toque(), eixos(), par(), anda(), guia(), anel(), marca_eixo(), barra(), titulo()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-008_praticando_o_que_e_funcao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"

# contas da aula
C_ = lambda n: 20 + 0.5 * n
assert C_(100) == 70 and 0.5 * 100 == 50 and 45 - 20 == 25 and 25 / 0.5 == 50 and C_(50) == 45
TAB_A = [(1, 5), (2, 5), (3, 7), (4, 9)]
TAB_B = [(1, 2), (1, 4), (2, 6), (3, 8)]
assert len({x for x, _ in TAB_A}) == 4 and len({x for x, _ in TAB_B}) == 3
V = lambda x: abs(x - 1) - 1


def agua(x):
    """reservatório: trechos retos por (0, 4), (4, 8), (10, 2), (12, 3)"""
    pts = [(0, 4), (4, 8), (10, 2), (12, 3)]
    if x < 0 or x > 12:
        return None
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


assert agua(2) == 6 and agua(6) == 6 and agua(4) == 8 and agua(10) == 2
assert max(agua(i / 10) for i in range(121)) == 8 and min(agua(i / 10) for i in range(121)) == 2
PR = E.Plano(1080, 210, 720, 660, -0.8, 12.8, -0.8, 9.5)
RX, RY = list(range(0, 13, 2)), list(range(0, 9, 2))


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


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """texto numa linha com uma cor por parte (a mesma da MAT-FUN-003)"""
    ws = [E.larg(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += w
    return sum(ws)


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))


def etiqueta(c, t, t0, qual, cx, cy, size=44):
    """a pergunta da trilha respondida: pílula índigo "entrada · x" ou preta "saída · y" """
    s, cor = ("entrada · x", ENT) if qual == "x" else ("saída · y", SAI)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor, a=a))


def titulo(c, t, t0, n, resto=None, x=XE, y=170):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(n), x + 40, y - 6, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, [("situação", "i", 72), (str(n), "g", 72, COR)] + (resto or []), x + 110, y)


def tabela2(c, t, t0, linhas, x, y, cab=("x", "y"), wc=150, hl=84, size=60, tl=None):
    """tabela de duas colunas, x / entrada (índigo) | y / saída (preto) (a mesma da MAT-FUN-002)"""
    a = ep(t, t0, 0.5)
    n = len(linhas)
    if a > 0:
        centro(c, cab[0], x + wc / 2, y - 24, 54, "i", ENT, a)
        centro(c, cab[1], x + wc * 1.5, y - 24, 54, "i", SAI, a)
        M.line(c, x, y, x + 2 * wc, y, TINTA, a, 4)
        M.line(c, x + wc, y, x + wc, y + hl * n + 10, TINTA, a, 4)
    caixas = []
    for i, (e, s) in enumerate(linhas):
        ry = y + 10 + hl * i
        caixas.append((x - 10, ry, 2 * wc + 20, hl))
        ti = tl[i] if tl else t0 + 0.3 + 0.15 * i
        E.foco(c, t, ti, 0.4, lambda q, e=e, s=s, ry=ry: (
            centro(c, E._num(e), x + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
            centro(c, E._num(s), x + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)
    return caixas


def faixa(c, cx, cor, a):
    if a > 0:
        x, y, w, h = cx
        M.rrect(c, x, y + 4, w, h - 8, 14, cor, 0.18 * a)


def regua(c, P, xv, a=1.0, cor=TINTA, largura=6):
    """a régua do teste: reta vertical tracejada de borda a borda do plano (MAT-FUN-006)"""
    if a <= 0:
        return
    x, y, w, h = P.caixa
    X = P.x(xv)
    M.line(c, X, y - 10, X, y + h + 10, cor, a, largura, dash=[18, 12])


def toque(c, P, xv, yv, cor, a=1.0, r=22):
    if a <= 0:
        return
    X, Y = P(xv, yv)
    c.drawCircle(X, Y, r, M.paint(cor, 0.25 * a))
    c.drawCircle(X, Y, r, M.paint(cor, a, stroke=5))
    c.drawCircle(X, Y, 8, M.paint(cor, a))


def eixos(c, t, P, tx, ty=None, tg=None, mx=RX, my=RY, nx="hora", ny="mil L", size=36):
    """plano em etapas (MAT-FUN-001/006/007): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 10 - E.larg(nx, "i", 46), P.oy - 22, 46, "i", ENT, a))
        for i, v in enumerate(mx):
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                centro(c, E._num(v), X + (14 if v == 0 else 0), P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", SAI, a))
        for i, v in enumerate(my):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10):
    p = ease_io(prog(t, t0, d))
    if p > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, 1.0, largura, 30, p)


def guia(c, t, t0, P, xv, yv, eixo, cor=None, d=0.6, largura=5):
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    X, Y = P(xv, yv)
    if eixo == "x":
        M.line(c, X, Y, X, P.oy, cor or ENT, 1.0, largura, dash=E.TRACO, progress=q)
    else:
        M.line(c, X, Y, P.ox, Y, cor or SAI, 1.0, largura, dash=E.TRACO, progress=q)


def anel(c, t, t0, P, xv, yv, cor=SAI, r=24, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, *P(xv, yv), r, -90, 360 * q, cor, largura)


def marca_eixo(c, t, t0, P, v, eixo, cor, size=44):
    s = E._num(v)
    if eixo == "x":
        cx, cy = P.x(v), P.oy + 37
    else:
        cx, cy = P.ox - 20 - E.larg(s, "b", 36) / 2, P.y(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor, a=a), sobe=0)


def barra(c, t, t0, P, a_, b_, cor, d=0.8, larg=14, r=15):
    """trecho em pé no eixo y (a imagem), bolinhas cheias nas pontas (MAT-FUN-007)"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    y0, y1 = P.y(a_), P.y(b_)
    M.line(c, P.ox, y0, P.ox, lerp(y0, y1, p), cor, 1.0, larg)
    q = ep(t, t0 + d * 0.6, 0.3)
    for Y in (y0, y1):
        c.drawCircle(P.ox, Y, r, M.paint(cor, q))


def resultado(c, t, t0, s, cx, cy, r=100):
    """resposta final na esfera da matéria"""
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k)
        size = r * (0.62 if len(s) <= 4 else 0.46)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 140, COR), ("situações", "i", 110)], XE, 300)
    E.frase(c, t, C["s01.a"] + 1.0, ps("criadas para esta aula", "i", 56, TINTA2), XE, 390, passo=0.1)
    itens = (("s01.b", "fórmula", "C(n)"), ("s01.c", "tabelas", "x | y"), ("s01.d", "domínio", "r{x − 5}"), ("s01.e", "gráfico", None))
    for i, (k, nome, desenho) in enumerate(itens):
        cx = 330 + i * 420
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, cx - 170, 500, 340, 320, p, prog_=p)
        E.foco(c, t, C[k], 0.5, lambda a, cx=cx, i=i: (E.bola(c, cx, 500, 34, a=a), centro(c, str(i + 1), cx, 516, 42, "g", BR, a)), sobe=0)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 780, 56, "g", COR, a))
        if desenho:
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, cx=cx, d_=desenho: E.formula(c, d_, cx, 660, 72, "g", TINTA, a, "center"))
        else:
            q = ep(t, C[k] + 0.3, 0.5)
            if q > 0:
                pts = [(cx - 110, 700), (cx - 40, 590), (cx + 30, 650), (cx + 110, 570)]
                for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                    M.line(c, x0, y0, x1, y1, TINTA, q, 8, cap_round=True)
    E.foco(c, t, C["s01.f"], 0.5, lambda a: E.pilula(c, "pause e resolva antes da resposta", W / 2, 940, 50, "g", fundo=COR, a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], [("antes", "i", 84), ("de", "i", 84), ("cada", "i", 84), ("conta,", "i", 84)], XE, 260)
    E.frase(c, t, C["s02.a"], [("1", "g", 110, COR), ("pergunta", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s02.b"], [("o", "i", 72), ("número", "i", 72), ("que", "i", 72), ("eu", "i", 72), ("tenho", "i", 72), ("é", "i", 72)], XE, 560)
    E.foco(c, t, C["s02.b"] + 1.0, 0.5, lambda a: (E.bola(c, 520, 760, 120, ENT, a), centro(c, "x", 520, 795, 110, "g", BR, a),
                                                  centro(c, "a entrada", 520, 950, 56, "g", ENT, a)))
    E.foco(c, t, C["s02.c"], 0.5, lambda a: centro(c, "ou", 860, 790, 90, "i", TINTA2, a))
    E.foco(c, t, C["s02.c"] + 0.3, 0.5, lambda a: (E.bola(c, 1200, 760, 120, SAI, a), centro(c, "y", 1200, 790, 110, "g", BR, a),
                                                  centro(c, "a saída", 1200, 950, 56, "g", SAI, a)))
    E.foco(c, t, C["s02.c"] + 1.6, 0.5, lambda a: E.formula(c, "?", 1620, 820, 300, "g", COR, a, "center"))


# ---------------- situação 1: fórmula ----------------
FORM = [("C(", SAI), ("n", ENT), (") = 20 + 0,5", TINTA), ("n", ENT)]


def b_questao1(c, t, C, b):
    titulo(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.b"], [("R$", "g", 64), ("20", "g", 64), ("fixos", "i", 64), ("+", "g", 64, TINTA2), ("R$", "g", 64), ("0,50", "g", 64),
                               ("por", "i", 64), ("cópia", "i", 64)], XE, 300)
    mista_em(c, t, C["s03.c"], FORM, XE, 470, 120)
    E.foco(c, t, C["s03.c"] + 1.0, 0.5, lambda a: mista(c, [("n", ENT), (" = número de cópias", TINTA2)], XE, 560, 52, a, est="i"))
    E.frase(c, t, C["s03.d"], [("a)", "g", 66, COR), ("100", "g", 70), ("cópias", "i", 68), ("custam?", "i", 68)], XE, 680)
    E.frase(c, t, C["s03.e"], [("b)", "g", 66, COR), ("com", "i", 68), ("R$", "g", 70), ("45,", "g", 70), ("quantas", "i", 68), ("cópias?", "i", 68)], XE, 810)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1560, cy=720, r=80)


def b_resposta1(c, t, C, b):
    mista(c, FORM, XE, 190, 84, ep(t, C["s05"] - 2, 0.3))

    def s05():
        E.frase(c, t, C["s05"], [("a)", "g", 64, COR), ("100", "g", 70, ENT), ("cópias", "i", 64)], XE, 340)
        etiqueta(c, t, C["s05.a"], "x", XE + 600, 318)
        fml(c, t, C["s05.b"], "C(100) = 20 + 0,5 · 100", XE, 500, 88)
        fml(c, t, C["s05.b"] + 1.2, "0,5 · 100 = 50", XE + 80, 630, 72, TINTA2)
        fml(c, t, C["s05.c"], "= 20 + 50 = 70", XE + 330, 800, 96)
        resultado(c, t, C["s05.c"] + 0.8, "R$ 70", 1560, 720, 140)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return

    def s06():
        E.frase(c, t, C["s06"], [("b)", "g", 64, COR), ("R$", "g", 70, SAI), ("45", "g", 70, SAI)], XE, 340)
        etiqueta(c, t, C["s06.a"], "y", XE + 520, 318)
        E.frase(c, t, C["s06.a"] + 1.0, ps("caminho de volta", "i", 56, TINTA2), XE + 760, 340, passo=0.1)
        fml(c, t, C["s06.b"], "20 + 0,5n = 45", XE, 500, 96)
        fml(c, t, C["s06.c"], "0,5n = 25", XE + 230, 650, 96)
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "−20 dos dois lados", 1140, 620, 44, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s06.d"], "n = 50", XE + 400, 800, 96, ENT)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "÷ 0,5", 1040, 770, 44, "g", fundo=TINTA2, a=a))
        resultado(c, t, C["s06.d"] + 0.8, "50", 1640, 820, 110)
        E.foco(c, t, C["s06.d"] + 1.0, 0.4, lambda a: centro(c, "cópias", 1640, 990, 56, "g", COR, a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], [("atalho", "g", 66, COR)], XE, 330)
    E.frase(c, t, C["s07.a"], [("0,5", "g", 80), ("=", "g", 80, TINTA2), ("metade", "g", 80, COR)], XE, 460)
    E.frase(c, t, C["s07.b"], [("metade", "i", 64), ("de", "i", 64), ("n", "g", 70, ENT), ("=", "g", 64), ("25", "g", 70), ("→", "g", 64, TINTA2),
                               ("n", "g", 70, ENT), ("=", "g", 64), ("50", "g", 76, ENT)], XE, 590)
    fml(c, t, C["s07.c"], "C(50) = 20 + 25 = 45", XE, 730, 72)
    E.foco(c, t, C["s07.c"] + 1.4, 0.4, lambda a: E.selo(c, XE + 860, 705, 36, True, a))
    E.frase(c, t, C["s07.d"], [("n", "g", 64, ERRADO), ("=", "g", 64, ERRADO), ("45?", "g", 64, ERRADO), ("daria", "i", 62), ("um", "i", 62),
                               ("preço,", "g", 62), ("não", "i", 62), ("cópias", "g", 62, ENT)], XE, 880)
    E.foco(c, t, C["s07.d"] + 0.4, 0.4, lambda a: E.selo(c, XE + 1180, 855, 36, False, a))


# ---------------- situação 2: é função? ----------------
TX_A, TX_B, TY = 200, 690, 400
PV = E.Plano(1260, 380, 480, 420, -3, 3, -1.6, 2.6)


def v_plano(c, t, t0, d=0.8):
    E.plano(c, t, t0, *PV.caixa, PV.xmin, PV.xmax, PV.ymin, PV.ymax, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, t0 + 0.3, PV, V, -1.6, 3, d=d, largura=8)


def paineis(c, t, ta, tb, tv, rapido=False):
    """as três situações lado a lado: tabela A, tabela B e o V"""
    E.foco(c, t, ta, 0.4, lambda a: centro(c, "A", TX_A + 150, TY - 110, 70, "g", COR, a))
    E.foco(c, t, tb, 0.4, lambda a: centro(c, "B", TX_B + 150, TY - 110, 70, "g", COR, a))
    E.foco(c, t, tv, 0.4, lambda a: centro(c, "C", PV.caixa[0] + PV.caixa[2] / 2, TY - 110, 70, "g", COR, a))
    passo = 0.0 if rapido else 0.3
    ca = tabela2(c, t, ta, TAB_A, TX_A, TY, tl=[ta + 0.3 + passo * i for i in range(4)])
    cb = tabela2(c, t, tb, TAB_B, TX_B, TY, tl=[tb + 0.3 + passo * i for i in range(4)])
    v_plano(c, t, tv, 0.1 if rapido else 0.9)
    return ca, cb


def b_questao2(c, t, C, b):
    titulo(c, t, C["s08.a"], 2, [("é", "i", 72), ("função?", "g", 72, COR)])
    paineis(c, t, C["s08.b"], C["s08.c"], C["s08.d"])
    if t >= C["s09"]:
        E.relogio(c, t, C["s09.a"], cx=W / 2, cy=880, r=56)


def pilula_sob(c, t, t0, cx, ok):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "é função" if ok else "não é função", cx, 930, 50, "g", fundo=CERTO if ok else ERRADO, a=a))


def b_resposta2(c, t, C, b):
    ca, cb = paineis(c, t, C["s10"] - 2, C["s10"] - 2, C["s10"] - 2, rapido=True)
    E.frase(c, t, C["s10.a"], [("cada", "i", 64), ("entrada,", "g", 64, ENT), ("uma", "i", 64), ("saída", "g", 64), ("só", "i", 64)], W / 2, 170, "center")
    # tabela A: o 5 repetido é saída
    for i in (0, 1):
        x, y, w, h = ca[i]
        q = ease_out(prog(t, C["s10.b"] + 0.3 * i, 0.5))
        if q > 0:
            E.arco(c, TX_A + 150 * 1.5, y + h / 2, 40, -90, 360 * q, SAI, 6)
    E.frase(c, t, C["s10.c"], [("x", "g", 48, ENT), ("diferentes,", "i", 46)], TX_A, 800)
    E.frase(c, t, C["s10.c"] + 0.5, [("mesmo", "i", 46), ("y:", "g", 48), ("pode", "g", 48, CERTO)], TX_A, 860)
    pilula_sob(c, t, C["s10.d"], TX_A + 150, True)
    # tabela B: o 1 com duas saídas
    for i in (0, 1):
        faixa(c, cb[i], ERRADO, ep(t, C["s11.a"] + 0.3 * i, 0.4))
    E.frase(c, t, C["s11.a"] + 0.8, [("1", "g", 50, ENT), ("→", "g", 50, TINTA2), ("2", "g", 50, ERRADO), ("e", "i", 48), ("4", "g", 50, ERRADO)], TX_B + 60, 830)
    pilula_sob(c, t, C["s11.b"], TX_B + 150, False)
    # o V: régua em pé
    if t >= C["s11.c"]:
        a = ep(t, C["s11.c"], 0.4)
        xv = lerp(-1.4, 2.6, ease_io(prog(t, C["s11.c"] + 0.3, 3.0)))
        xv = lerp(xv, 1.0, ease_io(prog(t, C["s11.e"] - 0.6, 0.8)))
        regua(c, PV, xv, a)
        toque(c, PV, xv, V(xv), CERTO, ep(t, C["s11.d"], 0.3) * a, 18)
    E.frase(c, t, C["s11.d"], [("toca", "i", 50), ("1", "g", 54, CERTO), ("vez", "i", 50)], PV.caixa[0] + PV.caixa[2] / 2, 860, "center")
    pilula_sob(c, t, C["s11.e"], PV.caixa[0] + PV.caixa[2] / 2, True)
    if t >= C["s11.e"]:
        E.foco(c, t, C["s11.e"] + 0.2, 0.4, lambda a: E.escreve(c, "a ponta também", PV.x(1) + 40, PV.y(V(1)) + 20, 40, "i", TINTA2, a))


# ---------------- situação 3: domínio ----------------
F = "f(x) = r{x − 5}"
G = "g(x) = f{1}{x + 2}"


def b_questao3(c, t, C, b):
    titulo(c, t, C["s12.a"], 3, [("domínio", "g", 72, ENT)])
    fml(c, t, C["s12.b"], F, XE, 380, 110)
    E.frase(c, t, C["s12.c"], [("domínio", "i", 64), ("como", "i", 64), ("intervalo?", "g", 64, ENT)], XE + 900, 360)
    fml(c, t, C["s12.d"], G, XE, 690, 110)
    E.frase(c, t, C["s12.d"] + 0.8, [("que", "i", 64), ("número", "i", 64), ("fica", "i", 64), ("fora?", "g", 64, ERRADO)], XE + 900, 650)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=W / 2, cy=880, r=56)


def b_resposta3(c, t, C, b):
    def s14():
        fml(c, t, C["s14"] - 2, F, XE, 200, 90)
        E.frase(c, t, C["s14.a"], [("raiz", "i", 60), ("de", "i", 60), ("negativo:", "g", 60, ERRADO), ("não", "i", 60), ("existe", "i", 60), ("na", "i", 60),
                                   ("reta", "i", 60)], XE, 330)
        E.frase(c, t, C["s14.b"], [("dentro", "i", 60), ("da", "i", 60), ("raiz:", "i", 60), ("zero", "g", 60), ("ou", "i", 60), ("positivo", "g", 60)], XE, 430)
        fml(c, t, C["s14.c"], "x − 5 ≥ 0", XE, 580, 96)
        fml(c, t, C["s14.d"], "x ≥ 5", XE + 700, 580, 96, ENT)
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.pilula(c, "+5 dos dois lados", XE + 820, 660, 40, "g", fundo=TINTA2, a=a))
        vx = E.reta(c, t, C["s14.e"] - 0.4, 260, 1640, 800, 0, 10, list(range(0, 11)), E._num, size=46)
        E.intervalo(c, t, C["s14.e"], vx, 800, 5, None, fecha_ini=True)
        fml(c, t, C["s14.e"] + 0.6, "D = [5, +∞[", 1180, 600, 88, ENT)
        if t >= C["s15.a"]:
            X = vx(4)
            c.drawCircle(X, 800, 15, M.paint(ERRADO, ep(t, C["s15.a"], 0.3)))
            E.foco(c, t, C["s15.a"], 0.4, lambda a: E.formula(c, "x = 4: r{4 − 5} = r{−1}", XE, 1000, 64, "g", ERRADO, a))
            E.foco(c, t, C["s15.a"] + 0.6, 0.4, lambda a: E.selo(c, XE + 820, 975, 34, False, a))
    E.saida(c, t, C["s15.b"] - 0.1, s14)
    if t < C["s15.b"]:
        return
    fml(c, t, C["s15.b"], G, XE, 260, 100)
    E.frase(c, t, C["s15.b"] + 0.4, [("não", "g", 64, ERRADO), ("se", "i", 64), ("divide", "i", 64), ("por", "i", 64), ("zero", "g", 64)], 900, 240)
    fml(c, t, C["s15.c"], "x + 2 = 0", XE, 480, 92)
    fml(c, t, C["s15.c"] + 0.8, "x = −2", XE + 620, 480, 92, ERRADO)
    vx = E.reta(c, t, C["s15.d"] - 0.4, 260, 1640, 720, -6, 4, list(range(-6, 5)), E._num, size=46)
    E.intervalo(c, t, C["s15.d"], vx, 720, None, -2)
    E.intervalo(c, t, C["s15.d"] + 0.3, vx, 720, -2, None)
    E.foco(c, t, C["s15.d"] + 0.4, 0.4, lambda a: E.pilula(c, "−2 fica fora", 1440, 920, 56, "g", fundo=ERRADO, a=a))
    fml(c, t, C["s15.d"] + 0.8, "x ≠ −2", XE, 940, 92, ENT)


# ---------------- situação 4: gráfico ----------------
def reservatorio(c, t, t0, d=1.4):
    eixos(c, t, PR, t0, t0, t0)
    E.curva(c, t, t0 + 0.3, PR, agua, 0, 12, d=d)
    for xv in (0, 12):
        k = ease_back(prog(t, t0 + 0.3 + d, 0.4))
        if k > 0:
            c.drawCircle(*PR(xv, agua(xv)), 11 * k, M.paint(COR))


def b_questao4(c, t, C, b):
    titulo(c, t, C["s16.a"], 4)
    reservatorio(c, t, C["s16.b"])
    E.frase(c, t, C["s16.b"], [("água", "g", 66), ("em", "i", 62), ("mil", "i", 62), ("litros", "i", 62)], XE, 300)
    E.frase(c, t, C["s16.c"], [("das", "i", 62), ("0", "g", 66, ENT), ("às", "i", 62), ("12", "g", 66, ENT), ("h", "g", 66, ENT)], XE, 390)
    perguntas = (("s16.d", "1", [("maior", "i", 58), ("volume?", "g", 58)]),
                 ("s16.e", "2", [("6", "g", 60), ("mil", "i", 58), ("L:", "i", 58), ("quando?", "g", 58, ENT)]),
                 ("s16.f", "3", [("imagem?", "g", 58)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 540 + i * 120
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=780, cy=860, r=56)


def b_resposta4(c, t, C, b):
    reservatorio(c, t, C["s18"] - 3, 0.1)

    def s18():
        E.ponto(c, t, C["s18.a"], PR, 4, 8, cor=COR, r=17)
        anel(c, t, C["s18.a"] + 0.2, PR, 4, 8, COR, 32)
        E.foco(c, t, C["s18.a"], 0.5, lambda a: par(c, "4", "8", XE, 300, 96, a))
        E.foco(c, t, C["s18.a"] + 0.3, 0.4, lambda a: par(c, "4", "8", PR.x(4) + 30, PR.y(8) - 10, 40, a))
        E.frase(c, t, C["s18.b"], [("volume", "i", 64), ("=", "g", 64), ("o", "i", 64), ("y", "g", 70)], XE, 460)
        etiqueta(c, t, C["s18.b"] + 0.4, "y", XE + 600, 438)
        guia(c, t, C["s18.c"], PR, 4, 8, "y")
        marca_eixo(c, t, C["s18.c"] + 0.4, PR, 8, "y", SAI)
        guia(c, t, C["s18.c"] + 0.8, PR, 4, 8, "x")
        marca_eixo(c, t, C["s18.c"] + 1.2, PR, 4, "x", ENT)
        E.frase(c, t, C["s18.c"], [("8", "g", 90), ("mil", "g", 70), ("litros", "g", 70)], XE, 640)
        E.frase(c, t, C["s18.c"] + 1.0, [("às", "i", 66), ("4", "g", 76, ENT), ("h", "g", 70, ENT)], XE, 760)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return

    def s19():
        E.frase(c, t, C["s19.a"], [("6", "g", 80), ("mil", "i", 70), ("=", "g", 70), ("o", "i", 70), ("y", "g", 80)], XE, 270)
        etiqueta(c, t, C["s19.a"] + 0.6, "y", XE + 640, 248)
        E.frase(c, t, C["s19.a"] + 1.2, [("quer", "i", 60), ("o", "i", 60), ("x", "g", 66, ENT)], XE, 370)
        marca_eixo(c, t, C["s19.b"], PR, 6, "y", SAI)
        q = ep(t, C["s19.b"] + 0.4, 0.5)
        if q > 0:
            x, y, w, h = PR.caixa
            M.line(c, PR.ox, PR.y(6), x + w + 10, PR.y(6), SAI, 0.6 * q, 5, dash=[18, 12])
        anda(c, t, C["s19.b"], PR, (0, 6), (1.75, 6), SAI, d=0.7)
        E.frase(c, t, C["s19.b"], [("saia", "i", 60), ("do", "i", 60), ("6", "g", 66), ("e", "i", 60), ("vá", "i", 60), ("de", "i", 60), ("lado", "g", 60)], XE, 480)
        E.frase(c, t, C["s19.c"], [("encontra", "i", 60), ("a", "i", 60), ("curva", "i", 60), ("2", "g", 70, COR), ("vezes", "g", 62, COR)], XE, 580)
        for k, xv, txt in (("s19.d", 2, "subindo"), ("s19.e", 6, "descendo")):
            anel(c, t, C[k], PR, xv, 6, COR, 28)
            E.ponto(c, t, C[k], PR, xv, 6, cor=COR, r=14)
            guia(c, t, C[k] + 0.2, PR, xv, 6, "x")
            marca_eixo(c, t, C[k] + 0.6, PR, xv, "x", ENT)
        E.frase(c, t, C["s19.d"], [("às", "i", 62), ("2", "g", 72, ENT), ("h,", "g", 66, ENT), ("subindo", "i", 62, CERTO)], XE, 720)
        E.frase(c, t, C["s19.e"], [("às", "i", 62), ("6", "g", 72, ENT), ("h,", "g", 66, ENT), ("descendo", "i", 62, ERRADO)], XE, 820)
        E.frase(c, t, C["s19.f"], [("parar", "i", 54, ERRADO), ("no", "i", 54, ERRADO), ("1º:", "g", 54, ERRADO), ("metade", "g", 54), ("da", "i", 54),
                                   ("resposta", "i", 54)], XE, 940)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], [("imagem:", "g", 70), ("a", "i", 66), ("sombra", "g", 66, COR), ("no", "i", 66), ("y", "g", 70)], XE, 290)
    for i in range(0, 25):
        xv = i / 2
        q = ease_io(prog(t, C["s20.a"] + 0.05 * i, 0.4))
        if q > 0:
            X, Y = PR(xv, agua(xv))
            M.line(c, X, Y, PR.ox, Y, SAI, 0.2, 3, progress=q)
    E.ponto(c, t, C["s20.b"], PR, 10, 2, cor=COR, r=15)
    guia(c, t, C["s20.b"] + 0.2, PR, 10, 2, "y")
    E.frase(c, t, C["s20.b"], [("mais", "i", 62), ("baixo:", "i", 62), ("2,", "g", 70), ("às", "i", 62), ("10", "g", 70, ENT), ("h", "g", 66, ENT)], XE, 440)
    E.ponto(c, t, C["s20.c"], PR, 4, 8, cor=COR, r=15)
    guia(c, t, C["s20.c"] + 0.2, PR, 4, 8, "y")
    E.frase(c, t, C["s20.c"], [("mais", "i", 62), ("alto:", "i", 62), ("8", "g", 70)], XE, 560)
    barra(c, t, C["s20.d"], PR, 2, 8, SAI)
    fml(c, t, C["s20.d"], "Im = [2, 8]", XE, 760, 110)


# ---------------- fechamento ----------------
PA = E.Plano(1180, 460, 560, 420, -1, 6, -1, 6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("o", "i", 76), ("número", "i", 76), ("dado", "i", 76), ("é", "i", 76), ("o", "i", 76), ("x", "g", 84, ENT), ("ou", "i", 76), ("o", "i", 76),
                            ("y?", "g", 84)]),
                 ("s21.b", [("conta", "g", 76), ("no", "i", 76), ("sentido", "i", 76), ("certo", "g", 76, COR)]),
                 ("s21.c", [("confira", "g", 76, CERTO), ("na", "i", 76), ("fórmula", "i", 76), ("ou", "i", 76), ("no", "i", 76), ("gráfico", "i", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s22.a"], [("função", "g", 120, COR), ("afim", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s22.b"], [("a", "i", 64), ("lei", "i", 64), ("do", "i", 64), ("táxi", "g", 66)], XE, 540)
    E.frase(c, t, C["s22.c"], [("uma", "i", 64), ("reta,", "g", 66, COR), ("com", "i", 64), ("2", "g", 70, COR), ("pontos", "i", 64)], XE, 650)
    if t >= C["s22.c"]:
        E.plano(c, t, C["s22.c"], *PA.caixa, PA.xmin, PA.xmax, PA.ymin, PA.ymax, grade=False, rotulos=False, size=30, d=0.5)
        E.reta_pontos(c, t, C["s22.c"] + 0.4, PA, (1, 2), (4, 5))
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(560, 325, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
