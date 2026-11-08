"""Visual — Estudativo · MAT-FUN-014: custo, receita e lucro; o ponto de equilíbrio.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Nesta aula: a receita R(x) é sempre índigo e o custo C(x) sempre preto, nas fórmulas e nas retas; o lucro é verde e o prejuízo é
vermelho, também como região pintada entre as retas (E.area). Dinheiro com ponto de milhar ("2.000"). Nos planos de telefone,
A em índigo e B em preto (como na MAT-FUN-013), e a reta que compensa ganha um traço verde largo por baixo.
Peças locais: eixos() com marcas e formato, par(), anel(), marca_ponto(), sob() (chave com rótulo sob um trecho de fórmula),
barra_vertical() (a distância entre as retas num x)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
REC, CUS = COR, TINTA  # receita · custo
ARQUIVO_FINAL = "estudativo_MAT-FUN-014_custo_receita_lucro_ponto_de_equilibrio.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("custo", "equilibrio", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"

custo = lambda x: 2000 + 30 * x
receita = lambda x: 50 * x
lucro = lambda x: receita(x) - custo(x)
plano_a = lambda x: 40 + 0.5 * x
plano_b = lambda x: 20 + x
custo_d = lambda x: 900 + 4 * x
receita_d = lambda x: 10 * x
assert lucro(50) == -1000 and 50 * 20 == 1000 and 20 * 50 - 2000 == -1000
assert receita(100) == custo(100) == 5000 and 2000 / 20 == 100
assert plano_a(40) == plano_b(40) == 60 and plano_b(0) < plano_a(0)
assert receita(120) == 6000 and custo(120) == 5600 and lucro(120) == 400
assert 900 / 6 == 150 and (600 + 900) / 6 == 250 and receita_d(250) == 2500 and custo_d(250) == 1900 and receita_d(250) - custo_d(250) == 600


def mil(v):
    """dinheiro com ponto de milhar: 2000 → "2.000", −1000 → "−1.000" """
    s = f"{abs(int(round(v))):,}".replace(",", ".")
    return ("−" if v < 0 else "") + s


PL = (1080, 190, 700, 700)
PG = E.Plano(*PL, 0, 170, 0, 8500)  # fábrica
MG = ([20 * i for i in range(1, 9)], [1000 * i for i in range(1, 9)])
PP = E.Plano(*PL, 0, 85, 0, 105)  # planos de telefone
MP = ([10 * i for i in range(1, 9)], [20, 40, 60, 80, 100])
PD = E.Plano(*PL, 0, 310, 0, 3600)  # doceira
MD = ([50, 100, 150, 200, 250, 300], [500 * i for i in range(1, 8)])


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
    """plano em etapas (o da MAT-FUN-001), com marcas escolhidas: grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty.
    rx / ry = só estes valores ganham número (os outros, só o traço)"""
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


def sob(c, t, t0, s, antes, trecho, x, y, size, rotulo, cor, align="left", h=24, rs=46):
    """chave sob um trecho de uma fórmula escrita em (x, y): antes = o texto que vem antes do trecho"""
    w = larg_f(s, size)
    x0 = (x - w / 2 if align == "center" else x) + larg_f(antes, size)
    x1 = x0 + larg_f(trecho, size)
    p = ep(t, t0, 0.5)
    if p > 0:
        E.chave(c, x0, x1, y + 30, cor, p, h, 5)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, (x0 + x1) / 2, y + 30 + h + rs + 10, rs, "i", cor, a))


def reta_nome(c, t, t0, P, f, xv, nome, cor, lado=-1, size=46):
    """nome da reta perto do fim dela (lado −1 = acima)"""
    E.foco(c, t, t0, 0.4, lambda a: E.formula(c, nome, P.x(xv), P.y(f(xv)) + (-28 if lado < 0 else 64), size, "g", cor, a, "right"))


def barra_vertical(c, P, xv, y0, y1, cor, a, w=18):
    """faixa em pé no x, de y0 a y1 (valores)"""
    if a <= 0:
        return
    X = P.x(xv)
    c.drawRect(skia.Rect.MakeLTRB(X - w / 2, P.y(max(y0, y1)), X + w / 2, P.y(min(y0, y1))), M.paint(cor, 0.85 * a))


def caixa_f(c, s, x, y, size, fundo, a, align="left"):
    """fórmula branca numa caixa cheia (resultado); x, y como em E.formula"""
    w = larg_f(s, size)
    x0 = x - w / 2 if align == "center" else x
    M.rrect(c, x0 - 40, y - size * 1.0, w + 80, size * 1.45, 40, fundo, a)
    E.formula(c, s, x0, y, size, "g", BR, a)


def destaca(c, t, t0, P, f, a, b, cor, largura=26, alfa=0.35, t1=None):
    """traço largo e claro por baixo de uma reta (a reta que compensa)"""
    q = ep(t, t0, 0.4) * (1 - (ep(t, t1, 0.4) if t1 else 0))
    if q > 0:
        c.saveLayerAlpha(None, int(255 * alfa * q))
        E.curva(c, t, t0, P, f, a, b, d=0.7, cor=cor, largura=largura)
        c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01"], [("uma", "i", 76), ("pequena", "i", 76), ("fábrica", "g", 76)], W / 2, 190, "center")
        E.frase(c, t, C["s01.a"], [("vende", "i", 80), ("por", "i", 80), ("R$", "g", 96, REC), ("50", "g", 96, REC)], 330, 380)
        E.frase(c, t, C["s01.b"], [("gasta", "i", 80), ("R$", "g", 96, CUS), ("30", "g", 96, CUS)], 1120, 380)
        E.frase(c, t, C["s01.b"] + 1.4, [("sobram", "i", 76), ("R$", "g", 84, CERTO), ("20", "g", 84, CERTO), ("por", "i", 76), ("peça", "i", 76)],
                W / 2, 540, "center")
        E.frase(c, t, C["s01.b"] + 3.0, [("50", "g", 76, ENT), ("peças:", "i", 76), ("lucro", "i", 76), ("de", "i", 76), ("R$", "g", 76),
                                         ("1.000?", "g", 76)], W / 2, 680, "center")
        if t >= C["s01.c"]:
            E.risco(c, 560, 700, 1360, 620, t, C["s01.c"], largura=14)
        E.foco(c, t, C["s01.c"] + 0.5, 0.5, lambda a: E.pilula(c, "prejuízo de R$ 1.000", W / 2, 860, 70, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("custo", "g", 110, CUS), ("e", "i", 100), ("receita", "g", 110, REC)], XE, 460)
        E.frase(c, t, C["s02.a"] + 3.0, [("o", "i", 90), ("ponto", "i", 90), ("de", "i", 90)], XE, 600)
        E.frase(c, t, C["s02.a"] + 3.4, [("equilíbrio", "g", 120, COR)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.a", "o empate de dois planos:", lambda a, y: E.formula(c, "40 + 0,5x = 20 + x", x + 44, y, 70, "g", TINTA, a)),
             ("s03.b", "valor inicial e taxa de variação:", lambda a, y: E.formula(c, "f(x) = 40 + 0,5x", x + 44, y, 70, "g", COR, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.a"], 0.4))


# ---------------- custo ----------------
FC = "C(x) = 2.000 + 30x"


def b_custo(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("o que faltou no gancho?", "i", 80), XE, 220)
        E.frase(c, t, C["s04.a"], [("aluguel", "g", 84), ("e", "i", 84), ("máquinas", "g", 84)], XE, 380)
        E.frase(c, t, C["s04.b"], [("R$", "g", 130, CUS), ("2.000", "g", 130, CUS), ("por", "i", 90), ("mês", "i", 90)], XE, 560)
        E.frase(c, t, C["s04.b"] + 1.0, ps("mesmo sem fazer peça nenhuma", "i", 62, TINTA2), XE, 660, passo=0.1)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "custo fixo", XE + 230, 800, 70, "g", fundo=CUS, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("+", "g", 90, CUS), ("R$", "g", 90, CUS), ("30", "g", 90, CUS), ("por", "i", 84), ("peça", "i", 84)], XE, 240)
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "custo por peça", 1130, 210, 56, "g", fundo=CUS, a=a))
    fml(c, t, C["s05.b"], FC, W / 2, 620, 140, CUS, "center")
    E.foco(c, t, C["s05.b"] - 0.4, 0.4, lambda a: E.escreve(c, "x = peças no mês", XE, 380, 58, "i", ENT, a))
    sob(c, t, C["s05.c"], FC, "C(x) = ", "2.000", W / 2, 620, 140, "valor inicial", CUS, "center", rs=54)
    sob(c, t, C["s05.d"], FC, "C(x) = 2.000 + ", "30", W / 2, 620, 140, "taxa: +30 por peça", COR, "center", rs=54)


# ---------------- receita ----------------
FR = "R(x) = 50x"


def b_receita(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("receita:", "g", 84, REC), ("o", "i", 84), ("dinheiro", "i", 84), ("que", "i", 84), ("entra", "g", 84)], XE, 240)
    E.frase(c, t, C["s06.a"] + 1.4, ps("com as vendas", "i", 84), XE, 340)
    E.frase(c, t, C["s06.b"] - 1.0, [("R$", "g", 76, REC), ("50", "g", 76, REC), ("por", "i", 72), ("peça", "i", 72), ("vendida", "i", 72)], XE, 480)
    fml(c, t, C["s06.b"], FR, W / 2, 700, 150, REC, "center")
    sob(c, t, C["s06.c"] + 0.8, FR, "R(x) = ", "50", W / 2, 700, 150, "começa no zero", REC, "center", rs=54)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "R(0) = 0", 1350, 480, 76, "g", TINTA2, a))


# ---------------- lucro ----------------
def b_lucro(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07.a"], [("lucro", "g", 84, CERTO), ("=", "g", 84), ("o", "i", 84), ("que", "i", 84), ("entra", "g", 84, REC),
                                   ("−", "g", 84), ("o", "i", 84), ("que", "i", 84), ("sai", "g", 84, CUS)], W / 2, 200, "center")
        fml(c, t, C["s07.b"], "L(x) = R(x) − C(x)", W / 2, 330, 100, TINTA, "center")
        fml(c, t, C["s07.b"] + 2.4, "L(x) = 50x − (2.000 + 30x)", W / 2, 480, 90, TINTA, "center")
        E.foco(c, t, C["s07.c"] - 1.6, 0.4, lambda a: E.pilula(c, "o menos troca os sinais", W / 2, 565, 40, "g", fundo=ERRADO, a=a))
        fml(c, t, C["s07.c"] - 1.6, "L(x) = 50x − 2.000 − 30x", W / 2, 700, 90, TINTA2, "center")
        E.foco(c, t, C["s07.c"], 0.6, lambda a: caixa_f(c, "L(x) = 20x − 2.000", W / 2, 900, 100, CERTO, a, "center"))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.foco(c, t, C["s08"], 0.5, lambda a: E.formula(c, "L(x) = 20x − 2.000", W / 2, 230, 96, "g", CERTO, a, "center"))
    E.frase(c, t, C["s08"] + 0.3, [("com", "i", 72), ("50", "g", 76, ENT), ("peças", "i", 72)], W / 2, 360, "center")
    fml(c, t, C["s08.a"], "20 · 50 = 1.000", W / 2, 520, 100, TINTA, "center")
    fml(c, t, C["s08.b"], "1.000 − 2.000 = −1.000", W / 2, 680, 100, ERRADO, "center")
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "lucro negativo = prejuízo", W / 2, 840, 64, "g", fundo=ERRADO, a=a))


# ---------------- equilíbrio ----------------
def b_equilibrio(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], ps("quando para de perder?", "i", 80), XE, 220)
        E.frase(c, t, C["s09.a"], [("receita", "g", 96, REC), ("=", "g", 96), ("custo", "g", 96, CUS)], XE, 380)
        E.frase(c, t, C["s09.b"], [("ponto", "i", 110), ("de", "i", 110), ("equilíbrio", "g", 110, COR)], XE, 560)
        E.foco(c, t, C["s09.b"] + 1.2, 0.4, lambda a: E.pilula(c, "o empate dos dois planos", 1350, 660, 48, "g", fundo=TINTA2, a=a))
    E.saida(c, t, C["s09.c"] - 0.1, s09)
    xf = 400
    E.foco(c, t, C["s09.c"], 0.5, lambda a: (E.formula(c, "50x", xf, 260, 110, "g", REC, a, "right"),
                                             E.formula(c, " = ", xf, 260, 110, "g", TINTA, a),
                                             E.formula(c, "2.000 + 30x", xf + larg_f(" = ", 110), 260, 110, "g", CUS, a)))
    E.foco(c, t, C["s10.a"] - 0.8, 0.4, lambda a: E.pilula(c, "− 30x dos dois lados", 1450, 225, 44, "g", fundo=TINTA2, a=a))
    fml(c, t, C["s10.a"], "20x = 2.000", xf - larg_f("20x", 110), 410, 110, TINTA)
    E.foco(c, t, C["s10.b"] - 0.6, 0.4, lambda a: E.pilula(c, "÷ 20", 1100, 375, 44, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s10.b"], 0.6, lambda a: caixa_f(c, "x = 100 peças", xf - larg_f("x", 110), 575, 100, CERTO, a))
    fml(c, t, C["s10.c"], "R(100) = 50 · 100 = 5.000", XE, 740, 80, REC)
    fml(c, t, C["s10.d"], "C(100) = 2.000 + 3.000 = 5.000", XE, 860, 80, CUS)
    E.foco(c, t, C["s10.end"] - 1.2, 0.5, lambda a: E.pilula(c, "lucro zero", 1580, 800, 56, "g", fundo=CERTO, a=a))


# ---------------- gráfico ----------------
def retas_fab(c, t, tc, tr, d=1.0, nomes=None):
    E.curva(c, t, tc, PG, custo, 0, 170, d=d, cor=CUS)
    E.curva(c, t, tr, PG, receita, 0, 170, d=d, cor=REC)
    if nomes is not None:
        E.foco(c, t, tc + d * 0.8 if nomes is True else nomes, 0.4, lambda a: E.pilula(c, "custo", *PG(150, 5100), 40, "g", fundo=CUS, a=a))
        E.foco(c, t, tr + d * 0.8 if nomes is True else nomes, 0.4, lambda a: E.pilula(c, "receita", *PG(118, 7500), 40, "g", fundo=REC, a=a))


def plano_fab(c, t, t0, ry=(2000, 4000, 5000, 6000, 8000)):
    eixos(c, t, PG, t0, tg=t0, marcas=MG, size=34, rx=[40, 80, 100, 120, 160], ry=None, fmt=mil)


def b_grafico(c, t, C, b):
    plano_fab(c, t, C["s11"])
    retas_fab(c, t, C["s11.a"], C["s11.a"] + 0.4, nomes=True)
    if t >= C["s11.b"]:
        marca_ponto(c, t, C["s11.b"], *PG(0, 2000), CUS, 22)
    if t >= C["s11.c"]:
        marca_ponto(c, t, C["s11.c"], PG.ox, PG.oy, REC, 22)
    E.area(c, t, C["s12.a"], PG, custo, 0, 100, receita, cor=ERRADO, alfa=0.28, d=1.0)
    E.area(c, t, C["s12.b"], PG, receita, 100, 170, custo, cor=CERTO, alfa=0.3, d=1.0)
    E.ponto(c, t, C["s11.d"], PG, 100, 5000, guias=True, cor=COR, r=17)
    E.foco(c, t, C["s11.d"] + 0.3, 0.4, lambda a: (M.rrect(c, PG.x(100) - 300, PG.y(5000) - 80, 280, 62, 14, "#F4F3EF", 0.95 * a),
                                                   par(c, "100", "5.000", PG.x(100) - 26, PG.y(5000) - 32, 44, a, "right")))
    E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: centro(c, "prejuízo", PG.x(45), PG.y(1500) + 14, 44, "g", ERRADO, a))
    E.foco(c, t, C["s12.b"] + 0.4, 0.4, lambda a: centro(c, "lucro", PG.x(150), PG.y(5600), 44, "g", CERTO, a))

    def s11():
        E.frase(c, t, C["s11.a"], [("duas", "i", 80), ("retas", "g", 80)], XE, 230)
        E.frase(c, t, C["s11.b"], [("custo:", "g", 66, CUS), ("começa", "i", 66), ("no", "i", 66), ("2.000", "g", 66, CUS)], XE, 360)
        E.frase(c, t, C["s11.c"], [("receita:", "g", 66, REC), ("começa", "i", 66), ("no", "i", 66), ("0", "g", 66, REC)], XE, 460)
        E.frase(c, t, C["s11.c"] + 1.6, [("e", "i", 66), ("sobe", "i", 66), ("mais", "g", 66, REC), ("rápido", "g", 66, REC)], XE, 550)
        E.frase(c, t, C["s11.d"], [("cruzam", "i", 66), ("em", "i", 66)], XE, 700)
        E.foco(c, t, C["s11.d"] + 0.3, 0.5, lambda a: par(c, "100", "5.000", XE + 300, 700, 72, a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("antes:", "i", 70), ("custo", "g", 70, CUS), ("por", "i", 70), ("cima", "i", 70)], XE, 260)
    E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: E.pilula(c, "prejuízo", XE + 140, 350, 48, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s12.b"], [("depois:", "i", 70), ("receita", "g", 70, REC), ("por", "i", 70), ("cima", "i", 70)], XE, 500)
    E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: E.pilula(c, "lucro", XE + 100, 590, 48, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s12.c"], [("a", "i", 70), ("reta", "i", 70), ("de", "i", 70), ("cima", "g", 70, COR)], XE, 760)
    E.frase(c, t, C["s12.c"] + 0.8, [("vale", "i", 70), ("mais", "g", 70, COR), ("naquele", "i", 70), ("x", "g", 76, ENT)], XE, 860)


# ---------------- planos ----------------
def b_planos(c, t, C, b):
    eixos(c, t, PP, C["s13"], tg=C["s13"], marcas=MP, size=36)
    E.curva(c, t, C["s13.a"], PP, plano_a, 0, 85, d=1.0, cor=COR)
    E.curva(c, t, C["s13.b"], PP, plano_b, 0, 85, d=1.0, cor=TINTA)
    E.foco(c, t, C["s13.a"] + 0.8, 0.4, lambda a: E.pilula(c, "A", *PP(78, 88), 44, "g", fundo=COR, a=a))
    E.foco(c, t, C["s13.b"] + 0.8, 0.4, lambda a: E.pilula(c, "B", *PP(68, 99), 44, "g", fundo=TINTA, a=a))
    menor = lambda x: min(plano_a(x), plano_b(x))
    destaca(c, t, C["s13.d"] + 0.8, PP, plano_b, 0, 40, CERTO)
    destaca(c, t, C["s13.e"], PP, plano_a, 40, 85, CERTO)
    E.ponto(c, t, C["s13.c"], PP, 40, 60, guias=True, cor=TINTA, r=17)
    E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: par(c, "40", "60", PP.x(40) + 30, PP.y(60) + 70, 44, a))
    E.frase(c, t, C["s13"], [("dois", "i", 70), ("planos", "g", 70), ("de", "i", 70), ("telefone", "i", 70)], XE, 210)
    E.foco(c, t, C["s13"] + 1.0, 0.4, lambda a: E.escreve(c, "x = minutos", XE, 300, 54, "i", ENT, a))
    fml(c, t, C["s13.a"], "A: 40 + 0,5x", XE, 420, 80, COR)
    fml(c, t, C["s13.b"], "B: 20 + x", XE, 530, 80, TINTA)
    E.frase(c, t, C["s13.d"], [("pagar", "i", 66), ("menos:", "i", 66), ("a", "i", 66), ("reta", "i", 66), ("de", "i", 66), ("baixo", "g", 66, CERTO)],
            XE, 680)
    E.frase(c, t, C["s13.d"] + 1.6, [("até", "i", 66), ("40", "g", 66, ENT), ("min:", "i", 66), ("B", "g", 72)], XE, 790)
    E.frase(c, t, C["s13.e"], [("depois:", "i", 66), ("A", "g", 72, COR)], XE + 470, 790)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_fab(c, t, C["s14"] - 3)
    retas_fab(c, t, C["s14"] - 3, C["s14"] - 3, d=0.05, nomes=C["s14"] - 3)
    a1 = ep(t, C["s14.b"], 0.5)
    if a1 > 0:
        M.line(c, PG.x(120), PG.oy, PG.x(120), PG.y(6000), REC, a1, 4, dash=E.TRACO)
    E.ponto(c, t, C["s14.b"], PG, 120, 6000, cor=REC, r=15)
    E.ponto(c, t, C["s14.c"], PG, 120, 5600, cor=CUS, r=15)
    barra_vertical(c, PG, 120, 5600, 6000, CERTO, ep(t, C["s14.d"], 0.4), 30)
    E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.pilula(c, "400", PG.x(120) - 80, PG.y(6500), 40, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s14.a"], [("receita", "g", 80, REC), ("≠", "g", 80, ERRADO), ("lucro", "g", 80, CERTO)], XE, 220)
    fml(c, t, C["s14.b"], "R(120) = 6.000", XE, 360, 80, REC)

    def diz():
        E.frase(c, t, C["s14.b"] + 1.2, [("lucrou", "i", 68, ERRADO), ("6.000?", "g", 68, ERRADO)], XE, 470)
        if t >= C["s14.b"] + 2.4:
            E.risco(c, XE - 10, 480, XE + 420, 420, t, C["s14.b"] + 2.4, largura=10)
    diz()
    fml(c, t, C["s14.c"], "C(120) = 2.000 + 3.600", XE, 620, 64, CUS)
    fml(c, t, C["s14.c"] + 1.6, "= 5.600", XE + 240, 710, 64, CUS)
    E.foco(c, t, C["s14.d"], 0.6, lambda a: caixa_f(c, "L = 6.000 − 5.600 = 400", XE + 20, 890, 70, CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 72, CLARO), W / 2, 170, "center")
        E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "f{custo fixo}{sobra por peça}", W / 2, 390, 100, "g", BR, a, "center"))
        fml(c, t, C["s15.b"], "50 − 30 = 20", W / 2, 640, 100, CLARO, "center")
        E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "f{2.000}{20} = 100 peças", W / 2, 900, 110, "g", BR, a, "center"))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return

    def pago():
        E.frase(c, t, C["s16.a"], [("cada", "i", 76, CLARO), ("peça", "i", 76, CLARO), ("paga", "g", 76, BR), ("R$", "g", 76, BR), ("20", "g", 76, BR),
                                   ("do", "i", 76, CLARO), ("fixo", "g", 76, BR)], W / 2, 230, "center")
        x, y, w, h = 260, 380, 1400, 120
        a = ep(t, C["s16.a"] + 0.3, 0.5)
        if a > 0:
            M.rrect(c, x, y, w, h, 20, CLARO, 0.15 * a)
            f = ease_io(prog(t, C["s16.a"] + 0.8, 3.0))
            M.rrect(c, x, y, max(1, w * f), h, 20, CERTO, a)
            M.rrect(c, x, y, w, h, 20, BR, a * 0.0)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), M.paint(BR, a, stroke=4))
            n = int(round(100 * f))
            centro(c, f"{n} peças", x + w / 2, y + h + 90, 70, "g", BR, a)
            centro(c, f"R$ {mil(20 * n)} de R$ 2.000", x + w / 2, y + h + 180, 56, "i", CLARO, a)
    E.saida(c, t, C["s16.b"] - 0.1, pago)
    if t < C["s16.b"]:
        return
    E.frase(c, t, C["s16.b"], [("não", "g", 76, ERRADO), ("compensa:", "i", 76, CLARO)], W / 2, 290, "center")
    E.frase(c, t, C["s16.b"] + 0.8, [("preço", "g", 76, BR), ("ou", "i", 76, CLARO), ("custo", "g", 76, BR), ("que", "i", 76, CLARO), ("mudam", "i", 76, CLARO)],
            W / 2, 420, "center")
    E.frase(c, t, C["s16.b"] + 2.4, ps("desconto para quem compra muito", "i", 64, CLARO), W / 2, 540, "center", passo=0.1)
    E.foco(c, t, C["s16.end"] - 1.6, 0.5, lambda a: E.pilula(c, "monte as funções e iguale", W / 2, 760, 60, "g", fundo=CERTO, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 70, COR), XE, 180)
    E.foco(c, t, C["s17"] + 1.0, 0.4, lambda a: E.escreve(c, "(valores inventados)", XE + 480, 180, 46, "i", TINTA2, a))
    E.frase(c, t, C["s17.a"] - 1.6, [("uma", "i", 72), ("doceira", "g", 72)], XE, 300)
    E.frase(c, t, C["s17.a"], [("custo", "i", 68), ("fixo:", "i", 68), ("R$", "g", 72, CUS), ("900", "g", 72, CUS), ("por", "i", 68), ("mês", "i", 68)], XE, 420)
    E.frase(c, t, C["s17.b"], [("gasta", "i", 68), ("R$", "g", 72, CUS), ("4", "g", 72, CUS), ("por", "i", 68), ("bolo", "i", 68)], XE, 520)
    E.frase(c, t, C["s17.c"], [("vende", "i", 68), ("por", "i", 68), ("R$", "g", 72, REC), ("10", "g", 72, REC)], XE, 620)
    E.frase(c, t, C["s17.d"], [("1)", "g", 68, COR), ("ponto", "i", 68), ("de", "i", 68), ("equilíbrio?", "g", 68, COR)], XE, 780)
    E.frase(c, t, C["s17.d"] + 2.2, [("2)", "g", 68, COR), ("quantos", "i", 68), ("bolos", "i", 68), ("para", "i", 68), ("lucrar", "i", 68),
                                     ("R$", "g", 68, CERTO), ("600?", "g", 68, CERTO)], XE, 880)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1500, cy=460, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eixos(c, t, PD, C["s19"], tg=C["s19"], marcas=MD, size=34, fmt=mil, ry=[500, 1000, 1500, 2000, 2500, 3000, 3500])
    E.curva(c, t, C["s19.a"], PD, custo_d, 0, 310, d=1.0, cor=CUS)
    E.curva(c, t, C["s19.b"], PD, receita_d, 0, 310, d=1.0, cor=REC)
    E.foco(c, t, C["s19.a"] + 0.8, 0.4, lambda a: E.pilula(c, "custo", *PD(287, 1200), 40, "g", fundo=CUS, a=a))
    E.foco(c, t, C["s19.b"] + 0.8, 0.4, lambda a: E.pilula(c, "receita", *PD(200, 3100), 40, "g", fundo=REC, a=a))
    E.ponto(c, t, C["s19.d"] + 0.5, PD, 150, 1500, guias=True, cor=COR, r=16)

    def s19():
        fml(c, t, C["s19.a"], "C(x) = 900 + 4x", XE, 260, 80, CUS)
        fml(c, t, C["s19.b"], "R(x) = 10x", XE, 380, 80, REC)
        fml(c, t, C["s19.c"], "L(x) = 6x − 900", XE, 500, 80, CERTO)
        E.foco(c, t, C["s19.d"] - 1.4, 0.4, lambda a: E.pilula(c, "sobram R$ 6 por bolo", XE + 250, 620, 44, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s19.d"], 0.6, lambda a: caixa_f(c, "f{900}{6} = 150 bolos", XE + 20, 815, 80, CERTO, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20"], 0.4, lambda a: E.formula(c, "equilíbrio: 150 bolos", XE, 200, 54, "g", CERTO, a))
    fml(c, t, C["s20.a"], "6x − 900 = 600", XE, 330, 84, TINTA)
    E.foco(c, t, C["s20.b"] - 0.8, 0.4, lambda a: E.pilula(c, "+ 900", 730, 395, 40, "g", fundo=TINTA2, a=a))
    fml(c, t, C["s20.b"], "6x = 1.500", XE, 470, 84, TINTA)
    fml(c, t, C["s20.c"], "x = 250 bolos", XE, 600, 90, COR)
    fml(c, t, C["s20.c"] + 1.6, "R = 2.500", XE, 730, 68, REC)
    fml(c, t, C["s20.c"] + 3.2, "C = 900 + 1.000 = 1.900", XE, 830, 68, CUS)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "sobram R$ 600: bateu", XE + 260, 950, 54, "g", fundo=CERTO, a=a))
    a1 = ep(t, C["s20.c"], 0.5)
    if a1 > 0:
        M.line(c, PD.x(250), PD.oy, PD.x(250), PD.y(2500), ENT, a1, 4, dash=E.TRACO)
    E.ponto(c, t, C["s20.c"] + 1.6, PD, 250, 2500, cor=REC, r=15)
    E.ponto(c, t, C["s20.c"] + 3.2, PD, 250, 1900, cor=CUS, r=15)
    barra_vertical(c, PD, 250, 1900, 2500, CERTO, ep(t, C["s20.d"], 0.4), 30)
    E.foco(c, t, C["s20.d"] + 0.3, 0.4, lambda a: E.pilula(c, "600", PD.x(250) - 90, PD.y(2200), 40, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("lucro", "g", 84, CERTO), ("=", "g", 84), ("receita", "g", 84, REC), ("−", "g", 84), ("custo", "g", 84, CUS)]),
                 ("s21.b", [("equilíbrio:", "g", 84, COR), ("onde", "i", 84), ("as", "i", 84), ("retas", "i", 84), ("se", "i", 84), ("cruzam", "g", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s22"] + 1.0, [("praticando", "g", 130, COR)], XE, 460)
    E.frase(c, t, C["s22"] + 1.4, [("função", "i", 100), ("afim", "g", 100, COR)], XE, 580)
    E.frase(c, t, C["s22.a"], ps("lei, coeficientes e duas retas", "i", 60, TINTA2), XE, 700, passo=0.1)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, custo=b_custo, receita=b_receita, lucro=b_lucro, equilibrio=b_equilibrio,
              grafico=b_grafico, planos=b_planos, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
