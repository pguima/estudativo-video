"""Visual — Estudativo · MAT-FUN-015: praticando função afim (quatro situações).

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-013 e 014: retas A em índigo e B em preto; custo preto e receita índigo; lucro verde e prejuízo vermelho; a reta
que compensa ganha um traço verde largo por baixo. Nesta aula: Δx é uma chave índigo deitada e Δy uma chave preta em pé (degrau());
no atalho, a escada que anda para trás até o eixo y. Cada situação abre com a esfera numerada (num_situacao()).
Peças locais: eixos(), par(), anel(), marca_ponto(), caixa_f(), destaca(), barra_vertical(), degrau(), caixa_dagua()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
REC, CUS = COR, TINTA  # receita · custo
ARQUIVO_FINAL = "estudativo_MAT-FUN-015_praticando_funcao_afim.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "fim"))
BR = "#FFFFFF"

caixa = lambda x: 500 - 20 * x
reta2 = lambda x: 3 * x + 1
loc_a = lambda x: 100 + 0.5 * x
loc_b = lambda x: 60 + x
custo = lambda x: 600 + 2 * x
receita = lambda x: 5 * x
assert caixa(0) == 500 and caixa(25) == 0 and 500 / 20 == 25
assert reta2(2) == 7 and reta2(5) == 16 and (16 - 7) / (5 - 2) == 3 and reta2(10) == 31 and 7 - 2 * 3 == 1
assert loc_a(80) == loc_b(80) == 140 and loc_a(120) == 160 and loc_b(120) == 180 and loc_b(0) < loc_a(0)
assert 600 / 3 == 200 and receita(200) == custo(200) == 1000 and 3 * 150 - 600 == -150 and receita(150) == 750 and custo(150) == 900


def mil(v):
    s = f"{abs(int(round(v))):,}".replace(",", ".")
    return ("−" if v < 0 else "") + s


PL = (1080, 190, 700, 700)
P1 = E.Plano(*PL, 0, 31, 0, 600)
M1 = ([5, 10, 15, 20, 25, 30], [100, 200, 300, 400, 500, 600])
P2 = E.Plano(*PL, 0, 11, 0, 35)
M2 = (list(range(1, 11)), [5, 10, 15, 20, 25, 30, 35])
P3 = E.Plano(*PL, 0, 145, 0, 215)
M3 = ([20, 40, 60, 80, 100, 120, 140], [20 * i for i in range(1, 11)])
P4 = E.Plano(*PL, 0, 265, 0, 1400)
M4 = ([50, 100, 150, 200, 250], [200 * i for i in range(1, 8)])


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
    """plano em etapas (o da MAT-FUN-001), com marcas escolhidas: grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
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
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                rot and (rx is None or v in rx) and centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
        if rot:
            E.foco(c, t, tx + 0.2, 0.4, lambda a: E.escreve(c, "0", P.ox - 16 - E.larg("0", "b", size), P.oy + 14 + size, size, "b", TINTA2, a))
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(my):
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


def caixa_f(c, s, x, y, size, fundo, a, align="left"):
    """fórmula branca numa caixa cheia (resultado)"""
    w = larg_f(s, size)
    x0 = x - w / 2 if align == "center" else x
    M.rrect(c, x0 - 40, y - size * 1.0, w + 80, size * 1.45, 40, fundo, a)
    E.formula(c, s, x0, y, size, "g", BR, a)


def destaca(c, t, t0, P, f, a, b, cor, largura=26, alfa=0.35):
    q = ep(t, t0, 0.4)
    if q > 0:
        c.saveLayerAlpha(None, int(255 * alfa * q))
        E.curva(c, t, t0, P, f, a, b, d=0.7, cor=cor, largura=largura)
        c.restore()


def barra_vertical(c, P, xv, y0, y1, cor, a, w=18):
    if a <= 0:
        return
    X = P.x(xv)
    c.drawRect(skia.Rect.MakeLTRB(X - w / 2, P.y(max(y0, y1)), X + w / 2, P.y(min(y0, y1))), M.paint(cor, 0.85 * a))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def num_situacao(c, t, t0, n, x=XE, y=200):
    """esfera com o número da situação e o título ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 46, y - 26, 46, a=a), centro(c, str(n), x + 46, y - 4, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("situação", "i", 72), (str(n), "g", 72, COR)], x + 120, y)


def chave_h(c, P, x0, x1, yv, rot, cor, a, size=44, abaixo=True):
    """Δx: chave deitada sob o trecho de x0 a x1, na altura yv"""
    if a <= 0:
        return
    Y = P.y(yv) + (16 if abaixo else -16)
    E.chave(c, P.x(x0), P.x(x1), Y, cor, a, 20 if abaixo else -20, 5)
    E.formula(c, rot, (P.x(x0) + P.x(x1)) / 2, Y + (64 if abaixo else -34), size, "g", cor, a, "center")


def chave_v(c, P, xv, y0, y1, rot, cor, a, size=44):
    """Δy: chave em pé à direita do trecho de y0 a y1, no x"""
    if a <= 0:
        return
    X = P.x(xv) + 16
    Y0, Y1 = P.y(y0), P.y(y1)
    for x0_, ya, x1_, yb in ((X, Y0, X + 20, Y0), (X + 20, Y0, X + 20, Y1), (X + 20, Y1, X, Y1)):
        M.line(c, x0_, ya, x1_, yb, cor, a, 5)
    E.formula(c, rot, X + 36, (Y0 + Y1) / 2 + size * 0.36, size, "g", cor, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 220, COR), ("situações", "i", 110)], XE, 400)
    E.frase(c, t, C["s01.a"] + 1.4, ps("com tudo da função afim", "i", 70, TINTA2), XE, 520, passo=0.12)
    for i in range(4):
        E.foco(c, t, C["s01.a"] + 0.5 + 0.2 * i, 0.4, lambda a, i=i: (E.bola(c, 1150 + 170 * i, 340, 62, a=a),
                                                                      centro(c, str(i + 1), 1150 + 170 * i, 366, 72, "g", BR, a)), blur=0)
    E.relogio(c, t, C["s01.b"], cx=1400, cy=640, r=110)
    E.frase(c, t, C["s01.b"] + 0.4, [("pause", "g", 80, COR), ("e", "i", 80), ("resolva", "g", 80)], XE, 700)
    E.frase(c, t, C["s01.b"] + 1.2, ps("antes de ver a resposta", "i", 70), XE, 800, passo=0.12)
    E.frase(c, t, C["s01.end"] - 3.0, [("errar", "i", 64, TINTA2), ("aqui", "i", 64, TINTA2), ("ensina", "g", 64, CERTO)], XE, 940)


# ---------------- o que vai usar ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], [("você", "i", 80), ("vai", "i", 80), ("usar", "g", 80, COR)], XE, 200)
    itens = (("s02.a", lambda a, x, y: E.formula(c, "f(x) = ax + b", x, y, 60, "g", COR, a)),
             ("s02.b", lambda a, x, y: (E.escreve(c, "b e", x, y, 56, "i", TINTA, a), E.formula(c, "a = f{Δy}{Δx}", x + 110, y, 56, "g", COR, a))),
             ("s02.c", lambda a, x, y: E.escreve(c, "o zero da função", x, y, 58, "g", TINTA, a)),
             ("s02.d", lambda a, x, y: E.escreve(c, "a lei por 2 pontos", x, y, 58, "g", TINTA, a)),
             ("s02.e", lambda a, x, y: E.escreve(c, "reta pela origem", x, y, 58, "g", TINTA, a)),
             ("s02.f", lambda a, x, y: E.escreve(c, "ponto de equilíbrio", x, y, 58, "g", TINTA, a)))
    for i, (k, fn) in enumerate(itens):
        col, lin = i % 2, i // 2
        x, y = XE + col * 820, 400 + lin * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, x=x, y=y: (E.bola(c, x + 40, y - 20, 40, a=a),
                                                          centro(c, str(i + 1), x + 40, y, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, x=x, y=y: fn(a, x + 110, y))


# ---------------- situação 1: caixa d'água ----------------
def caixa_dagua(c, t, t0, nivel, a=1.0, x=1260, y=280, w=400, h=480):
    """caixa d'água com o nível (0..1) e a torneira embaixo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 30, BR, a)
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * (1 - nivel), w, h * nivel), M.paint(COR, 0.85 * a))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(TINTA, a, stroke=6))
    M.line(c, x + w * 0.5, y + h, x + w * 0.5, y + h + 50, TINTA, a, 14)
    M.line(c, x + w * 0.5, y + h + 50, x + w * 0.5 + 70, y + h + 50, TINTA, a, 14)


def b_questao1(c, t, C, b):
    num_situacao(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.b"], [("caixa", "i", 70), ("d'água:", "i", 70), ("500", "g", 76, SAI), ("litros", "i", 70)], XE, 340)
    E.frase(c, t, C["s03.c"], [("perde", "i", 70), ("20", "g", 76, ERRADO), ("litros", "i", 70), ("por", "i", 70), ("hora", "i", 70, ENT)], XE, 450)
    E.frase(c, t, C["s03.d"], [("1)", "g", 64, COR), ("a", "i", 64), ("lei", "g", 64), ("do", "i", 64), ("volume?", "i", 64)], XE, 610)
    E.frase(c, t, C["s03.d"] + 1.6, [("2)", "g", 64, COR), ("sobe", "i", 64), ("ou", "i", 64), ("desce?", "g", 64)], XE, 700)
    E.frase(c, t, C["s03.d"] + 3.0, [("3)", "g", 64, COR), ("esvazia", "i", 64), ("em", "i", 64), ("quantas", "i", 64), ("horas?", "g", 64, ENT)], XE, 790)
    a = ep(t, C["s03.b"], 0.5)
    nivel = 1 - 0.18 * ep(t, C["s03.c"], 2.5)
    caixa_dagua(c, t, C["s03.b"], nivel, a)
    E.foco(c, t, C["s03.b"] + 0.3, 0.4, lambda q: centro(c, "500 L", 1460, 560, 80, "g", BR, q))
    if t >= C["s03.c"]:
        for k in range(3):
            p = ((t - C["s03.c"]) * 0.9 + k / 3) % 1
            c.drawCircle(1460 + 70, 830 + 120 * p, 9, M.paint(COR, (1 - p) * ep(t, C["s03.c"], 0.4)))
        E.foco(c, t, C["s03.c"], 0.4, lambda q: E.escreve(c, "−20 L por hora", 1580, 860, 44, "g", ERRADO, q))
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1070, cy=820, r=64)


def b_resposta1(c, t, C, b):
    eixos(c, t, P1, C["s05"], tg=C["s05"], marcas=M1, size=36)
    E.ponto(c, t, C["s05.a"], P1, 0, 500, cor=SAI, r=17)
    if t >= C["s05.a"]:
        anel(c, t, C["s05.a"], *P1(0, 500), SAI)
    E.curva(c, t, C["s05.c"], P1, caixa, 0, 25, d=1.2, cor=COR)
    if t >= C["s05.d"]:
        p = ep(t, C["s05.d"], 0.6)
        M.arrow(c, P1.x(6), P1.y(470), P1.x(14), P1.y(310), ERRADO, p, 7, 24, p)

    def s05():
        E.frase(c, t, C["s05.a"], [("valor", "i", 66), ("inicial:", "i", 66), ("b", "g", 70, COR), ("=", "g", 70), ("500", "g", 70)], XE, 230)
        E.frase(c, t, C["s05.b"], [("taxa:", "i", 66), ("a", "g", 70, COR), ("=", "g", 70), ("−20", "g", 70, ERRADO)], XE, 340)
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "a < 0: a reta desce", XE + 250, 680, 48, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s06"] - 0.1, s05)
    E.foco(c, t, C["s05.c"], 0.6, lambda a: caixa_f(c, "f(x) = 500 − 20x", XE + 20, lerp(520, 230, ease_io(prog(t, C["s06"], 0.6))), 80, COR, a))
    if t < C["s06"]:
        return
    E.ponto(c, t, C["s06.c"], P1, 25, 0, cor=CERTO, r=17)
    if t >= C["s06.c"]:
        marca_ponto(c, t, C["s06.c"], *P1(25, 0), CERTO, 24)
    E.area(c, t, C["s06.d"], P1, caixa, 0, 25, cor=CERTO, alfa=0.25, d=1.0)
    E.frase(c, t, C["s06.a"], [("vazia:", "i", 64), ("f(x)", "g", 64), ("=", "g", 64), ("0", "g", 64, CERTO)], XE, 380)
    fml(c, t, C["s06.a"] + 1.2, "500 − 20x = 0", XE, 490, 72, TINTA)
    fml(c, t, C["s06.b"], "20x = 500", XE, 600, 72, TINTA)
    fml(c, t, C["s06.c"], "x = 25 horas", XE, 720, 80, CERTO)
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "antes de 25: positiva, tem água", XE + 370, 850, 44, "g", fundo=CERTO, a=a))


# ---------------- situação 2: dois pontos ----------------
def pontos2(c, t, tb, tc):
    E.ponto(c, t, tb, P2, 2, 7, guias=True, cor=COR, r=16)
    E.foco(c, t, tb + 0.3, 0.4, lambda a: par(c, "2", "7", P2.x(2) - 20, P2.y(7) - 24, 42, a, "right"))
    E.ponto(c, t, tc, P2, 5, 16, guias=True, cor=COR, r=16)
    E.foco(c, t, tc + 0.3, 0.4, lambda a: par(c, "5", "16", P2.x(5) - 20, P2.y(16) - 24, 42, a, "right"))


def b_questao2(c, t, C, b):
    eixos(c, t, P2, C["s07"], tg=C["s07"], marcas=M2, size=36)
    pontos2(c, t, C["s07.b"], C["s07.c"])
    num_situacao(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.b"], [("a", "i", 66), ("reta", "i", 66), ("passa", "i", 66), ("por", "i", 66)], XE, 330)
    par_em(c, t, C["s07.b"] + 0.4, "2", "7", XE, 440, 76)
    E.frase(c, t, C["s07.c"] - 0.3, [("e", "i", 66)], XE + 250, 440)
    par_em(c, t, C["s07.c"], "5", "16", XE + 320, 440, 76)
    E.frase(c, t, C["s07.d"], [("1)", "g", 64, COR), ("a", "i", 64), ("lei?", "g", 64)], XE, 600)
    E.foco(c, t, C["s07.d"] + 1.0, 0.4, lambda a: (E.escreve(c, "2)", XE, 690, 64, "g", COR, a), E.formula(c, "f(10)?", XE + 90, 690, 64, "g", TINTA, a)))
    E.frase(c, t, C["s07.d"] + 2.2, [("3)", "g", 64, COR), ("proporcionais?", "g", 64)], XE, 780)
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=860, cy=830, r=64)


def b_resposta2(c, t, C, b):
    eixos(c, t, P2, C["s09"] - 3, tg=C["s09"] - 3, marcas=M2, size=36)
    pontos2(c, t, C["s09"] - 3, C["s09"] - 3)
    chave_v(c, P2, 5, 7, 16, "Δy = 9", SAI, ep(t, C["s09.a"], 0.5) * (1 - ep(t, C["s10"], 0.4)))
    if C["s09.a"] <= t < C["s10"] + 0.4:
        M.line(c, P2.x(2), P2.y(7), P2.x(5), P2.y(7), TINTA2, ep(t, C["s09.a"], 0.4) * (1 - ep(t, C["s10"], 0.4)), 4, dash=E.TRACO)
    chave_h(c, P2, 2, 5, 7, "Δx = 3", ENT, ep(t, C["s09.b"], 0.5) * (1 - ep(t, C["s10"], 0.4)))

    def s09():
        fml(c, t, C["s09"] + 0.4, "a = f{Δy}{Δx}", XE, 260, 80, COR)
        fml(c, t, C["s09.a"], "Δy = 16 − 7 = 9", XE, 420, 72, SAI)
        fml(c, t, C["s09.b"], "Δx = 5 − 2 = 3", XE, 540, 72, ENT)
        fml(c, t, C["s09.c"], "a = f{9}{3} = 3", XE, 710, 84, COR)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.curva(c, t, C["s10.c"], P2, reta2, 0, 11, d=1.2, cor=COR)
    E.ponto(c, t, C["s10.b"], P2, 0, 1, cor=SAI, r=16)
    E.ponto(c, t, C["s10.d"] + 0.4, P2, 10, 31, guias=True, cor=COR, r=16)
    E.foco(c, t, C["s10.d"] + 0.7, 0.4, lambda a: par(c, "10", "31", P2.x(10) - 24, P2.y(31) - 26, 42, a, "right"))

    def s10():
        E.foco(c, t, C["s10"], 0.4, lambda a: E.formula(c, "a = 3", XE, 230, 64, "g", COR, a))
        E.foco(c, t, C["s10"] + 0.8, 0.4, lambda a: E.pilula(c, "troque (2, 7) na fórmula", XE + 560, 210, 40, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s10.a"], "3 · 2 + b = 7", XE, 360, 72, TINTA)
        fml(c, t, C["s10.b"], "6 + b = 7  →  b = 1", XE, 480, 72, TINTA)
        fml(c, t, C["s10.d"], "f(10) = 30 + 1 = 31", XE, 820, 72, TINTA)
    E.saida(c, t, C["s11"] - 0.1, s10)
    E.foco(c, t, C["s10.c"], 0.6, lambda a: caixa_f(c, "f(x) = 3x + 1", XE + 20, 660, 84, COR, a))
    if t < C["s11"]:
        return
    if t >= C["s11.b"]:
        marca_ponto(c, t, C["s11.b"], P2.ox, P2.oy, ERRADO, 22)
    E.frase(c, t, C["s11.a"], [("b", "g", 80, COR), ("=", "g", 80), ("1", "g", 80), ("≠", "g", 80, ERRADO), ("0", "g", 80)], XE, 300)
    E.frase(c, t, C["s11.b"], ps("não passa pela origem", "i", 66), XE, 430, passo=0.12)
    E.foco(c, t, C["s11.b"] + 0.8, 0.4, lambda a: E.pilula(c, "não é proporcional", XE + 280, 870, 54, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    Q = E.plano(c, t, C["s12"], 1100, 220, 640, 640, 0, 6.4, 0, 20, marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[4, 7, 10, 13, 16, 19],
                passo_y=3, escuro=True)
    E.curva(c, t, C["s12"] + 0.3, Q, reta2, 0, 6.3, d=0.8, cor=CLARO)
    for xv, yv in ((2, 7), (5, 16)):
        E.ponto(c, t, C["s12"] + 0.5, Q, xv, yv, cor=BR, r=15)
    E.foco(c, t, C["s12"] + 0.8, 0.4, lambda a: par(c, "2", "7", Q.x(2) + 26, Q.y(7) + 18, 44, a, cores=(CLARO, BR)))
    # a escada para trás: de x = 2 até x = 0, dois degraus de −3
    for k in range(2):
        x0, x1 = 2 - k, 1 - k
        y0, y1 = reta2(x0), reta2(x1)
        t0 = C["s12.b"] + 0.7 * k
        p = ep(t, t0, 0.4)
        if p > 0:
            M.line(c, Q.x(x0), Q.y(y0), lerp(Q.x(x0), Q.x(x1), p), Q.y(y0), "#FFD500", 1.0, 6)
        p2 = ep(t, t0 + 0.4, 0.4)
        if p2 > 0:
            M.line(c, Q.x(x1), Q.y(y0), Q.x(x1), lerp(Q.y(y0), Q.y(y1), p2), "#FFD500", 1.0, 6)
        E.foco(c, t, C["s12.c"] + 0.3 * k, 0.4, lambda a, x1=x1, y0=y0, y1=y1: E.escreve(c, "−3", Q.x(x1) - 14 - E.larg("−3", "g", 44), (Q.y(y0) + Q.y(y1)) / 2 + 16, 44, "g", "#FFD500", a))
    if t >= C["s12.d"]:
        E.ponto(c, t, C["s12.d"], Q, 0, 1, cor="#FFD500", r=17)
        anel(c, t, C["s12.d"], *Q(0, 1), "#FFD500")

    def s12():
        E.frase(c, t, C["s12"], ps("atalho para o b", "i", 72, CLARO), XE, 200)
        E.frase(c, t, C["s12.a"], [("ande", "i", 70, CLARO), ("para", "i", 70, CLARO), ("trás", "g", 70, BR)], XE, 340)
        E.frase(c, t, C["s12.a"] + 1.0, [("até", "i", 70, CLARO), ("x", "g", 76, BR), ("=", "g", 76, BR), ("0", "g", 76, BR)], XE, 440)
        E.frase(c, t, C["s12.b"], [("2", "g", 76, BR), ("passos", "i", 70, CLARO)], XE, 590)
        E.frase(c, t, C["s12.c"], [("cada", "i", 70, CLARO), ("passo:", "i", 70, CLARO), ("−3", "g", 76, "#FFD500")], XE, 690)
        E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "7 − 6 = 1 → b = 1", XE, 850, 90, "g", BR, a))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("b", "g", 76, BR), ("=", "g", 76, BR), ("valor", "i", 70, CLARO), ("no", "i", 70, CLARO), ("x", "g", 76, BR), ("=", "g", 76, BR), ("0", "g", 76, BR)], XE, 260)
    E.frase(c, t, C["s13.a"] + 1.8, [("a", "g", 76, BR), ("=", "g", 76, BR), ("quanto", "i", 66, CLARO), ("muda", "i", 66, CLARO), ("a", "i", 66, CLARO), ("cada", "i", 66, CLARO),
                                     ("passo", "i", 66, CLARO)], XE, 370)
    E.frase(c, t, C["s13.b"], [("não", "g", 70, ERRADO), ("compensa:", "i", 70, CLARO)], XE, 540)
    E.frase(c, t, C["s13.b"] + 0.8, [("ponto", "i", 66, CLARO), ("em", "i", 66, CLARO), ("x", "g", 70, BR), ("=", "g", 70, BR), ("50", "g", 70, BR)], XE, 640)
    E.frase(c, t, C["s13.b"] + 1.8, [("50", "g", 66, BR), ("passos", "i", 66, CLARO), ("para", "i", 66, CLARO), ("trás", "i", 66, CLARO)], XE, 730)
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "troque o ponto na fórmula", XE + 330, 870, 48, "g", fundo=CERTO, a=a))


# ---------------- situação 3: locadoras ----------------
def retas_loc(c, t, ta, tb, d=1.0):
    E.curva(c, t, ta, P3, loc_a, 0, 145, d=d, cor=COR)
    E.curva(c, t, tb, P3, loc_b, 0, 145, d=d, cor=TINTA)
    E.foco(c, t, ta + d * 0.8, 0.4, lambda a: E.pilula(c, "A", *P3(12, 125), 44, "g", fundo=COR, a=a))
    E.foco(c, t, tb + d * 0.8, 0.4, lambda a: E.pilula(c, "B", *P3(30, 60), 44, "g", fundo=TINTA, a=a))


def plano3(c, t, t0):
    eixos(c, t, P3, t0, tg=t0, marcas=M3, size=34, ry=[40, 80, 120, 140, 160, 200])


def b_questao3(c, t, C, b):
    plano3(c, t, C["s14"])
    retas_loc(c, t, C["s14.b"], C["s14.c"])
    num_situacao(c, t, C["s14.a"], 3)
    E.frase(c, t, C["s14.a"] + 1.4, [("aluguel", "i", 62), ("de", "i", 62), ("carro", "i", 62), ("·", "g", 62, TINTA2), ("x", "g", 66, ENT), ("=", "g", 66, ENT),
                                     ("km", "i", 62, ENT)], XE, 310)
    fml(c, t, C["s14.b"], "A: 100 + 0,5x", XE, 440, 76, COR)
    fml(c, t, C["s14.c"], "B: 60 + x", XE, 560, 76, TINTA)
    E.frase(c, t, C["s14.d"], [("viagem", "i", 66), ("de", "i", 66), ("120", "g", 70, ENT), ("km:", "i", 66)], XE, 720)
    E.frase(c, t, C["s14.d"] + 1.6, [("qual", "i", 66), ("compensa?", "g", 66, COR)], XE, 810)
    a = ep(t, C["s14.d"] + 0.6, 0.5)
    if a > 0:
        M.line(c, P3.x(120), P3.oy, P3.x(120), P3.caixa[1], ENT, a, 4, dash=E.TRACO)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=860, cy=830, r=64)


def b_resposta3(c, t, C, b):
    plano3(c, t, C["s16"] - 3)
    retas_loc(c, t, C["s16"] - 3, C["s16"] - 3, d=0.05)
    E.ponto(c, t, C["s16.d"], P3, 80, 140, guias=True, cor=TINTA, r=17)
    E.foco(c, t, C["s16.d"] + 0.3, 0.4, lambda a: (M.rrect(c, P3.x(80) - 230, P3.y(140) - 82, 214, 62, 14, "#F4F3EF", 0.95 * a),
                                                   par(c, "80", "140", P3.x(80) - 24, P3.y(140) - 34, 44, a, "right")))

    def s16():
        fml(c, t, C["s16.a"], "100 + 0,5x = 60 + x", XE, 260, 76, TINTA)
        E.foco(c, t, C["s16.b"] - 1.2, 0.4, lambda a: E.pilula(c, "− 0,5x e − 60", XE + 160, 340, 38, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s16.b"], "40 = 0,5x", XE, 450, 76, TINTA)
        E.foco(c, t, C["s16.c"] - 0.6, 0.4, lambda a: E.pilula(c, "dobrando", XE + 560, 425, 38, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s16.c"], "x = 80 km", XE, 580, 80, ENT)
        E.frase(c, t, C["s16.d"], [("cruzam", "i", 64), ("em", "i", 64)], XE, 730)
        par_em(c, t, C["s16.d"] + 0.3, "80", "140", XE + 300, 730, 70)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    destaca(c, t, C["s17"] + 0.3, P3, loc_b, 0, 80, CERTO)
    destaca(c, t, C["s17.a"], P3, loc_a, 80, 145, CERTO)
    a = ep(t, C["s17.b"] - 0.4, 0.5)
    if a > 0:
        M.line(c, P3.x(120), P3.oy, P3.x(120), P3.y(195), ENT, a, 4, dash=E.TRACO)
    E.ponto(c, t, C["s17.c"], P3, 120, 160, cor=COR, r=15)
    E.ponto(c, t, C["s17.d"], P3, 120, 180, cor=TINTA, r=15)
    barra_vertical(c, P3, 120, 160, 180, ERRADO, ep(t, C["s17.e"], 0.4), 26)
    E.foco(c, t, C["s17.e"] + 0.3, 0.4, lambda a: E.pilula(c, "+ R$ 20", *P3(100, 190), 38, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s17"] + 0.2, [("até", "i", 62), ("80", "g", 66, ENT), ("km:", "i", 62), ("B", "g", 66), ("embaixo", "i", 62)], XE, 240)
    E.frase(c, t, C["s17.a"], [("depois:", "i", 62), ("A", "g", 66, COR), ("embaixo", "i", 62)], XE, 330)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.pilula(c, "120 km: compensa A", XE + 300, 450, 52, "g", fundo=CERTO, a=a))
    fml(c, t, C["s17.c"], "A: 100 + 60 = 160", XE, 600, 70, COR)
    fml(c, t, C["s17.d"], "B: 60 + 120 = 180", XE, 710, 70, TINTA)
    E.frase(c, t, C["s17.e"], [("só", "i", 60), ("a", "i", 60), ("parte", "i", 60), ("fixa:", "i", 60), ("R$", "g", 64, ERRADO), ("20", "g", 64, ERRADO),
                               ("a", "i", 60), ("mais", "g", 60, ERRADO)], XE, 860)


# ---------------- situação 4: pipoca ----------------
def b_questao4(c, t, C, b):
    num_situacao(c, t, C["s18.a"], 4)
    E.frase(c, t, C["s18.a"] + 0.6, [("um", "i", 72), ("carrinho", "i", 72), ("de", "i", 72), ("pipoca", "g", 72)], XE + 520, 200)
    E.frase(c, t, C["s18.b"], [("custo", "i", 68), ("fixo:", "i", 68), ("R$", "g", 72, CUS), ("600", "g", 72, CUS), ("por", "i", 68), ("mês", "i", 68)], XE, 400)
    E.frase(c, t, C["s18.c"], [("faz", "i", 68), ("por", "i", 68), ("R$", "g", 72, CUS), ("2", "g", 72, CUS), ("o", "i", 68), ("saquinho", "i", 68)], XE, 500)
    E.frase(c, t, C["s18.d"], [("vende", "i", 68), ("por", "i", 68), ("R$", "g", 72, REC), ("5", "g", 72, REC)], XE, 600)
    E.frase(c, t, C["s18.e"], [("1)", "g", 64, COR), ("ponto", "i", 64), ("de", "i", 64), ("equilíbrio?", "g", 64, COR)], XE, 770)
    E.frase(c, t, C["s18.e"] + 2.0, [("2)", "g", 64, COR), ("150", "g", 64, ENT), ("saquinhos:", "i", 64), ("lucro", "g", 64, CERTO), ("ou", "i", 64),
                                     ("prejuízo?", "g", 64, ERRADO)], XE, 870)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=1500, cy=460, r=180)


def b_resposta4(c, t, C, b):
    eixos(c, t, P4, C["s20"], tg=C["s20"], marcas=M4, size=34, fmt=mil)
    E.curva(c, t, C["s20"] + 0.3, P4, custo, 0, 265, d=1.0, cor=CUS)
    E.curva(c, t, C["s20"] + 0.6, P4, receita, 0, 265, d=1.0, cor=REC)
    E.foco(c, t, C["s20"] + 1.2, 0.4, lambda a: (E.pilula(c, "receita", *P4(170, 1250), 40, "g", fundo=REC, a=a),
                                                 E.pilula(c, "custo", *P4(235, 800), 40, "g", fundo=CUS, a=a)))
    E.ponto(c, t, C["s20.b"] + 0.4, P4, 200, 1000, guias=True, cor=COR, r=16)

    def s20():
        fml(c, t, C["s20.a"], "5 − 2 = 3 por saquinho", XE, 260, 64, TINTA)
        E.foco(c, t, C["s20.b"], 0.6, lambda a: caixa_f(c, "f{600}{3} = 200 saquinhos", XE + 20, 440, 70, CERTO, a))
        fml(c, t, C["s20.c"], "L(x) = 3x − 600", XE, 640, 76, CERTO)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21"], 0.4, lambda a: E.formula(c, "L(x) = 3x − 600", XE, 230, 60, "g", CERTO, a))
    fml(c, t, C["s21.a"], "3 · 150 = 450", XE, 380, 76, TINTA)
    fml(c, t, C["s21.b"], "450 − 600 = −150", XE, 510, 76, ERRADO)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "prejuízo", XE + 140, 640, 60, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s21.d"], [("150", "g", 66, ENT), ("ainda", "i", 64), ("não", "i", 64), ("chegou", "i", 64), ("em", "i", 64), ("200", "g", 66, ENT)], XE, 800)
    a = ep(t, C["s21.a"], 0.5)
    if a > 0:
        M.line(c, P4.x(150), P4.oy, P4.x(150), P4.y(900), ENT, a, 4, dash=E.TRACO)
    E.ponto(c, t, C["s21.a"] + 0.3, P4, 150, 750, cor=REC, r=14)
    E.ponto(c, t, C["s21.a"] + 0.6, P4, 150, 900, cor=CUS, r=14)
    barra_vertical(c, P4, 150, 750, 900, ERRADO, ep(t, C["s21.b"], 0.4), 26)
    E.foco(c, t, C["s21.b"] + 0.3, 0.4, lambda a: E.pilula(c, "−150", P4.x(150) - 90, P4.y(825), 38, "g", fundo=ERRADO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s22.a", [("b:", "g", 76, COR), ("onde", "i", 76), ("a", "i", 76), ("reta", "i", 76), ("começa", "g", 76)]),
                 ("s22.b", [("a:", "g", 76, COR), ("quanto", "i", 76), ("sobe", "i", 76), ("ou", "i", 76), ("desce", "i", 76), ("a", "i", 76), ("cada", "i", 76),
                            ("passo", "g", 76)]),
                 ("s22.c", [("no", "i", 76), ("gráfico,", "i", 76), ("a", "i", 76), ("reta", "i", 76), ("de", "i", 76), ("cima", "g", 76, COR), ("vale", "i", 76),
                            ("mais", "g", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 52, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 60) / 2, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 330, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.foco(c, t, C["s23.a"], 0.5, lambda a: E.formula(c, "x^2", XE, 480, 150, "g", COR, a))
    E.frase(c, t, C["s23.b"], [("a", "i", 120), ("parábola", "g", 130, COR)], XE + 260, 480)
    E.frase(c, t, C["s23.c"], ps("para onde abre e onde corta o eixo y", "i", 56, TINTA2), XE, 610, passo=0.1)
    Q = E.Plano(1250, 560, 420, 300, -3, 3, -1, 4)
    E.curva(c, t, C["s23.b"] + 0.3, Q, lambda x: x * x * 0.5, -2.7, 2.7, d=1.0, cor=COR, largura=9)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
