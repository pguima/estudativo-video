"""Visual — Estudativo · MAT-EQU-008: equação com letra dos dois lados.
A balança é E.balanca; o que vai nos pratos (caixas x, pesos de 1 kg e a etiqueta −2) é a peça local carga(). As contas ficam na
coluna da direita ou numa coluna central, uma linha por passo, no tempo da fala. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-008_equacao_letra_dos_dois_lados.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ordem", "lados", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 * 4 + 3 == 11 and 11 - 3 == 8 and 8 / 2 == 4
assert 5 * 5 - 2 == 23 == 3 * 5 + 8 and 8 + 2 == 10 and 10 / 2 == 5 and 3 - 5 == -2
assert 11 / 2 == 5.5 and 4 + 3 == 7 and 4 + 3 / 2 == 11 / 2
assert 7 * 6 - 4 == 38 == 3 * 6 + 20 and 7 - 3 == 4 and 20 + 4 == 24 and 24 / 4 == 6


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


P, P2, GG, S, S2 = 44, 50, 22, 66, 76  # peso, passo dos pesos, folga entre grupos, caixa, passo das caixas


def peso(c, x, y, a=1.0, cor=TINTA):
    """peso de 1 kg; (x, y) = canto de baixo à esquerda"""
    M.rrect(c, x, y - P, P, P, 8, cor, a)
    centro(c, "1", x + P / 2, y - 12, 28, "g", BR, a)


def caixa(c, x, y, a=1.0, cor=None):
    """caixa de peso desconhecido x; (x, y) = canto de baixo à esquerda"""
    M.rrect(c, x, y - S, S, S, 10, cor or E.COR, a)
    centro(c, "x", x + S / 2, y - 20, 50, "g", BR, a)


def carga(nc=0, n=0, bcols=3, cols=4, grupos=1, sai_c=0, sai_cp=0.0, sai_n=0, sai=0.0, menos=0, menos_a=1.0, destaque=0.0, a=1.0, ap=None):
    """o que vai num prato: nc caixas (em bcols colunas), n pesos (em grupos) e a etiqueta "− menos".
    As últimas sai_c caixas sobem e somem com sai_cp; os últimos sai_n pesos com sai. destaque apaga a 2ª metade (dividir por 2).
    ap(i) = alfa do peso i (entrada um a um)."""
    def fn(c, x, y):
        if a <= 0:
            return
        bc = min(bcols, nc) if nc else 0
        wb = bc * S2 - (S2 - S) if nc else 0
        per = n // grupos if n else 0
        gc = min(cols, per) if per else 0
        wg = gc * P2 - (P2 - P) if gc else 0
        ww = grupos * wg + (grupos - 1) * GG if n else 0
        wm = E.larg(f"− {menos}", "g", 44) + 40 if menos else 0
        partes = [w for w in (wb, ww, wm) if w]
        tot = sum(partes) + 24 * (len(partes) - 1)
        x0 = x - tot / 2
        base = y + 18
        xx = x0
        for i in range(nc):
            r, k = divmod(i, bc)
            px, py = xx + k * S2, base - r * S2
            al = a * (1 - 0.7 * destaque if i >= nc / 2 else 1.0)
            if i >= nc - sai_c:
                py -= 90 * ease_io(sai_cp)
                al *= 1 - sai_cp
            if al > 0:
                caixa(c, px, py, al)
        if nc:
            xx += wb + 24
        for i in range(n):
            g, k = divmod(i, per)
            px = xx + g * (wg + GG) + (k % gc) * P2
            py = base - (k // gc) * P2
            al = a * (1 - 0.7 * destaque if g >= grupos / 2 and grupos > 1 else 1.0) * (ap(i) if ap else 1.0)
            if i >= n - sai_n:
                py -= 90 * ease_io(sai)
                al *= 1 - sai
            if al > 0:
                peso(c, px, py, al)
        if n:
            xx += ww + 24
        if menos and menos_a > 0:
            E.pilula(c, f"− {menos}", xx + wm / 2, base - 34, 44, "g", fundo=ERRADO, cor=BR, a=a * menos_a)
    return fn


def entra(t, t0, n, d=0.05):
    """alfa do peso i, que entra um depois do outro a partir de t0"""
    return lambda i: ep(t, t0 + i * d, 0.25)


BX, BY, BL = 590, 600, 580  # balança das cenas com conta à direita
RX = 1450  # centro da coluna das contas


def balanca(c, t, t0, esq, dir_, inclina=0.0, cx=BX, cy=BY, larg=BL):
    E.foco(c, t, t0, 0.6, lambda a: E.balanca(c, cx, cy, esq, dir_, inclina, a, larg_braco=larg), blur=8)


def rotulo(c, t, t0, s, cx, y=790, cor=None, est="i"):
    E.frase(c, t, t0, ps(s, est, 54 if est == "i" else 46, cor or COR), cx, y, "center", 0.08)


def realce(c, t, t0, x, y, w, size, cor=None):
    """fundo leve atrás de um trecho já escrito"""
    q = ep(t, t0, 0.3)
    if q > 0:
        M.rrect(c, x - size * 0.12, y - size * 0.9, w + size * 0.24, size * 1.15, size * 0.18, cor or E.COR, 0.14 * q)


def eq_linha(c, t, partes, cx, y, size):
    """equação em partes [(texto, cor, t0)], centrada; devolve os x e as larguras"""
    xs = E.linha(c, t, [(s, "g", size, cor, t0) for s, cor, t0 in partes], cx, y, "center")
    return xs, [E.larg(s, "g", size) for s, _, _ in partes]


def eq_f(c, t, partes, cx, y, size):
    """como eq_linha, mas cada parte é uma fórmula (aceita f{2x}{2})"""
    ws = [E.formula(c, s, 0, 0, size, a=0) for s, _, _ in partes]
    gap = size * 0.26
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for (s, cor, t0), w in zip(partes, ws):
        xs.append(x)
        E.formula_em(c, t, t0, s, x, y, size, "g", cor)
        x += w + gap
    return xs, ws


def bola_res(c, t, t0, s, cx, cy, r=140, size=84):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, a=a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def num(c, t, t0, n, x, y, r=40):
    """número de passo numa esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x, y, r, a=a), centro(c, str(n), x, y + r * 0.42, r * 1.2, "g", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        size, y = 170, 430
        partes = [("5x", "g", size, TINTA, ka), ("−", "g", size, TINTA, ka + 0.8), ("2", "g", size, TINTA, ka + 1.1),
                  ("=", "g", size, TINTA, ka + 1.8), ("3x", "g", size, TINTA, ka + 2.0), ("+", "g", size, TINTA, ka + 2.7), ("8", "g", size, TINTA, ka + 2.9)]
        _, xs = E._arranjo(partes, W / 2, "center")
        for i in (0, 4):
            realce(c, t, kb + 0.3 * (i > 0), xs[i], y, E.larg(partes[i][0], "g", size), size)
        E.linha(c, t, partes, W / 2, y, "center")
        for i in (0, 4):
            E.foco(c, t, kb + 0.3 * (i > 0), 0.4, lambda a, i=i: E.escreve(c, partes[i][0], xs[i], y, size, "g", COR, a))
        E.frase(c, t, kb + 0.4, [("x", "g", 80, COR)] + ps("dos dois lados do igual", "i", 80), W / 2, 640, "center", 0.1)
        E.frase(c, t, kc - 0.6, ps("a regra é", "i", 84) + [("a mesma da balança", "g", 84, COR)], W / 2, 860, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), [("resolver", "g", 110, COR)] + ps("equações", "i", 100), XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), ps("de", "i", 90) + [("vários passos", "g", 96, COR)], XE, 600, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("com", "i", 80) + [("x", "g", 84, COR)] + ps("de um lado ou dos dois", "i", 80), XE, 730, passo=0.1)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "fazer o mesmo", "nos dois lados da balança"), ("s03.c", "juntar termos semelhantes", "5x − 3x = 2x"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.6, ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 960, 820, "left", 0.12)


# ---------------- dois passos: a ordem ----------------
def b_ordem(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    xa, xb, xc, yc = 360, 900, 1500, 470

    def cadeia():
        fcen(c, t, a4, "2x + 3 = 11", W / 2, 210, 140)
        E.frase(c, t, lerp(a4, b4, 0.45), ps("o x passou por", "i", 70) + [("duas contas", "g", 70, COR)], W / 2, 330, "center", 0.1)
        fcen(c, t, b4 - 0.5, "x", xa, yc + 36, 110)
        E.ponte(c, t, b4, xa + 80, xb - 110, yc, "× 2", None, 56)
        fcen(c, t, b4 + 0.4, "2x", xb, yc + 36, 110)
        E.ponte(c, t, c4, xb + 110, xc - 210, yc, "+ 3", None, 56)
        fcen(c, t, c4 + 0.4, "2x + 3", xc, yc + 36, 110)
        # desfazer: o caminho de volta, na ordem contrária
        E.ponte(c, t, d5, xc - 210, xb + 110, yc + 160, "− 3", None, 56)
        E.ponte(c, t, d5 + 0.4, xb - 110, xa + 80, yc + 160, "÷ 2", TINTA2, 56)

        def veste():
            E.frase(c, t, a5, ps("desfaça na", "i", 76) + [("ordem contrária", "g", 76, COR)], W / 2, 720, "center", 0.12)
            E.frase(c, t, b5, ps("põe:", "i", 68, TINTA2) + [("meia,", "g", 68)] + ps("depois", "i", 68) + [("sapato", "g", 68)], W / 2, 840, "center", 0.1)
            E.frase(c, t, c5, ps("tira:", "i", 68, TINTA2) + [("sapato,", "g", 68, COR)] + ps("depois", "i", 68) + [("meia", "g", 68, COR)], W / 2, 950, "center", 0.1)
        E.saida(c, t, d5 - 0.3, veste)
        E.frase(c, t, d5 - 0.1, ps("o último a entrar,", "i", 76) + [("+ 3,", "g", 80, COR)] + ps("sai primeiro", "i", 76), W / 2, 860, "center", 0.12)
    E.saida(c, t, C["s06"] - 0.1, cadeia)
    if t < C["s06"]:
        return

    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    cx, size = 760, 96
    fcen(c, t, C["s06"] + 0.1, "2x + 3 = 11", cx, 180, 110)
    num(c, t, a6, 1, 200, 300)
    E.frase(c, t, a6 + 0.6, ps("subtraia", "i", 60) + [("3", "g", 60, COR)] + ps("de cada lado", "i", 60), 270, 320, "left", 0.1)
    xs, ws = eq_linha(c, t, [("2x + 3", TINTA, a6 + 1.6), ("− 3", COR, a6 + 2.2), ("=", TINTA, a6 + 2.5), ("11", TINTA, a6 + 2.5), ("− 3", COR, a6 + 2.8)], cx, 440, size)
    if t >= b6:
        realce(c, t, b6, xs[3], 440, xs[4] + ws[4] - xs[3], size)
    fcen(c, t, c6, "2x = 8", cx, 560, size, COR)
    num(c, t, a7, 2, 200, 660)
    E.frase(c, t, a7 + 0.6, ps("divida cada lado por", "i", 60) + [("2", "g", 60, COR)], 270, 680, "left", 0.1)
    xs, ws = eq_linha(c, t, [("2x", TINTA, a7 + 1.6), ("÷ 2", COR, a7 + 2.0), ("=", TINTA, a7 + 2.3), ("8", TINTA, a7 + 2.3), ("÷ 2", COR, a7 + 2.6)], cx, 800, size)
    if t >= b7:
        realce(c, t, b7, xs[3], 800, xs[4] + ws[4] - xs[3], size)
    bola_res(c, t, c7, "x = 4", 1560, 470, 150, 90)
    fcen(c, t, d7, "2 × 4 + 3 = 11", 1520, 820, 84, CERTO)
    E.foco(c, t, C["s07.end"] - 1.0, 0.5, lambda a: E.selo(c, 1560, 930, 44, True, a))


# ---------------- x dos dois lados ----------------
def b_lados(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def tirar():
        sp = ep(t, a9 + 0.6, 0.8)
        esq = carga(nc=5 if t >= b8 + 1.4 else 0, sai_c=3, sai_cp=sp, menos=2, menos_a=ep(t, a8 + 1.0, 0.5))
        dir_ = carga(nc=3 if t >= b8 + 2.8 else 0, n=8, sai_c=3, sai_cp=sp, ap=entra(t, a8 + 2.5, 8))
        balanca(c, t, a8, esq, dir_)
        E.saida(c, t, a9 + 0.5, lambda: (rotulo(c, t, b8 + 1.4, "5 caixas", BX - BL / 2, 800),
                                         rotulo(c, t, b8 + 2.8, "3 caixas e 8 pesos", BX + BL / 2, 800)))
        rotulo(c, t, b9, "2 caixas", BX - BL / 2, 800)
        rotulo(c, t, b9 + 1.2, "nenhuma caixa", BX + BL / 2, 800)
        E.frase(c, t, c8, ps("caixas", "i", 66) + [("num prato só", "g", 66, COR)], BX, 960, "center", 0.1)
        fcen(c, t, a8 + 0.2, "5x − 2 = 3x + 8", RX, 250, 90)
        xs, ws = E._arranjo([(s, "g", 90) for s in ("5x − 2", "=", "3x + 8")], RX, "center")[1], None
        E.foco(c, t, a9, 0.5, lambda a: (E.pilula(c, "− 3x", xs[0] + 120, 340, 50, "g", a=a, cor=E.SOBRE),
                                         E.pilula(c, "− 3x", xs[2] + 150, 340, 50, "g", a=a, cor=E.SOBRE)))
        E.frase(c, t, b9, ps("sobram", "i", 60) + [("2 caixas", "g", 60, COR)] + ps("à esquerda", "i", 60), RX, 470, "center", 0.1)
        fcen(c, t, c9, "5x − 3x = 2x", RX, 600, 84, TINTA2)
        fcen(c, t, d9, "2x − 2 = 8", RX, 760, 110, COR)
    E.saida(c, t, C["s10"] - 0.1, tirar)

    # por que tirar 3x, e não 5x?
    s10, e10 = C["s10"], C["s10.end"]
    a0, b0 = C["s10.a"], C["s10.b"]
    T = lambda f: lerp(s10, e10, f)
    if s10 - 0.1 <= t:
        def porque():
            E.frase(c, t, s10 + 0.3, ps("por que tirar", "i", 80) + [("3x", "g", 84, COR)] + ps("e não", "i", 80) + [("5x?", "g", 84, ERRADO)], W / 2, 170, "center", 0.12)
            xl, xr = 520, 1400
            E.frase(c, t, T(0.16), ps("tirando", "i", 66) + [("5x", "g", 70, ERRADO)], xl, 320, "center", 0.1)
            fcen(c, t, T(0.28), "3x − 5x", xl, 470, 100)
            fcen(c, t, T(0.39), "= −2x", xl, 610, 100, ERRADO)
            E.frase(c, t, T(0.46), ps("caixas negativas?", "g", 58, ERRADO), xl, 740, "center", 0.1)
            E.frase(c, t, T(0.5), ps("a balança nem mostra", "i", 58), xl, 820, "center", 0.08)
            E.foco(c, t, T(0.48), 0.5, lambda a: E.selo(c, xl + 260, 590, 44, False, a))
            E.frase(c, t, T(0.64), ps("tirando", "i", 66) + [("3x", "g", 70, CERTO)], xr, 320, "center", 0.1)
            E.frase(c, t, a0, ps("a letra fica no lado", "i", 58), xr, 450, "center", 0.08)
            E.frase(c, t, a0 + 0.4, ps("que tinha mais x", "g", 58, COR), xr, 530, "center", 0.08)
            fcen(c, t, b0, "2x", xr, 680, 110, CERTO)
            E.frase(c, t, b0 + 0.6, ps("positivo", "g", 58, CERTO), xr, 780, "center")
            E.foco(c, t, b0 + 0.6, 0.5, lambda a: E.selo(c, xr + 160, 640, 44, True, a))
            E.frase(c, t, T(0.93), ps("você foge do", "i", 76) + [("sinal de menos", "g", 76, COR)], W / 2, 970, "center", 0.12)
        E.saida(c, t, C["s11"] - 0.1, porque)

    # 2x − 2 = 8 até x = 5
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    if C["s11"] - 0.1 <= t:
        def resolve():
            esq = carga(nc=2, bcols=2, menos=2, menos_a=1 - ep(t, a1 + 1.4, 0.6), destaque=ep(t, c1 + 0.8, 0.6))
            dir_ = carga(n=10 if t >= a1 + 1.4 else 8, cols=3 if t >= a1 + 1.4 else 4, grupos=2 if t >= a1 + 1.4 else 1,
                         destaque=ep(t, c1 + 0.8, 0.6), ap=(lambda i: 1.0 if i < 8 else ep(t, a1 + 1.4 + (i - 8) * 0.1, 0.3)))
            balanca(c, t, C["s11"], esq, dir_)
            rotulo(c, t, a1 + 1.6, "− 2 sai, + 2 do outro lado", BX, 960, TINTA2)
            fcen(c, t, C["s11"] + 0.2, "2x − 2 = 8", RX, 250, 100)
            eq_linha(c, t, [("2x − 2", TINTA, a1), ("+ 2", COR, a1 + 0.4), ("=", TINTA, a1 + 0.7), ("8", TINTA, a1 + 0.7), ("+ 2", COR, a1 + 1.0)], RX, 400, 84)
            fcen(c, t, b1, "2x = 10", RX, 530, 96, COR)
            eq_linha(c, t, [("2x", TINTA, c1), ("÷ 2", COR, c1 + 0.4), ("=", TINTA, c1 + 0.7), ("10", TINTA, c1 + 0.7), ("÷ 2", COR, c1 + 1.0)], RX, 670, 84)
            bola_res(c, t, d1, "x = 5", RX, 840, 120, 76)
        E.saida(c, t, C["s12"] - 0.1, resolve)

    # conferência nos dois lados
    if t >= C["s12"]:
        a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
        E.frase(c, t, C["s12"] + 0.2, ps("conferindo com", "i", 80) + [("x = 5", "g", 84, COR)], W / 2, 170, "center", 0.12)
        xl, xr = 520, 1400
        E.frase(c, t, C["s12"] + 0.6, ps("lado esquerdo", "i", 64, TINTA2), xl, 320, "center", 0.1)
        fcen(c, t, a2, "5 × 5 − 2", xl, 470, 100)
        fcen(c, t, lerp(a2, b2, 0.4), "= 25 − 2", xl, 600, 100)
        fcen(c, t, lerp(a2, b2, 0.62), "= 23", xl, 730, 110, COR)
        E.frase(c, t, lerp(a2, b2, 0.75), ps("lado direito", "i", 64, TINTA2), xr, 320, "center", 0.1)
        fcen(c, t, b2, "3 × 5 + 8", xr, 470, 100)
        fcen(c, t, lerp(b2, c2, 0.3), "= 15 + 8", xr, 600, 100)
        fcen(c, t, lerp(b2, c2, 0.6), "= 23", xr, 730, 110, COR)
        fcen(c, t, c2, "23 = 23", W / 2 - 50, 920, 120, CERTO)
        E.foco(c, t, c2 + 2.4, 0.5, lambda a: E.selo(c, W / 2 + 270, 880, 54, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4, c4, d4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]

    def um():
        E.frase(c, t, C["s13"] + 0.3, ps("o erro mais comum:", "i", 80) + [("dividir primeiro", "g", 80, ERRADO)], W / 2, 170, "center", 0.11)
        fcen(c, t, C["s13"] + 1.6, "2x + 3 = 11", W / 2, 330, 120)
        eq_f(c, t, [("f{2x}{2}", ERRADO, a3 + 0.3), ("+ 3", TINTA, a3 + 0.3), ("=", TINTA, a3 + 0.3), ("f{11}{2}", ERRADO, a3 + 1.4)], W / 2, 540, 110)
        E.frase(c, t, a3 + 1.0, ps("só o 2x e o 11", "i", 58, ERRADO), W / 2, 690, "center", 0.08)
        fcen(c, t, b3, "x + 3 = 5,5", W / 2, 830, 120, ERRADO)
        E.frase(c, t, c3, ps("toda conta", "i", 70) + [("sai errada", "g", 70, ERRADO)], W / 2, 980, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, um)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("teste com o", "i", 80) + [("4", "g", 84, COR)] + ps("que já conferiu", "i", 80), W / 2, 170, "center", 0.12)
    xs, ws = eq_linha(c, t, [("4 + 3 = 7", TINTA, a4), ("≠ 5,5", ERRADO, b4)], W / 2 - 40, 340, 120)
    E.foco(c, t, b4 + 0.4, 0.5, lambda a: E.selo(c, xs[1] + ws[1] + 80, 300, 50, False, a))
    E.frase(c, t, c4 - 0.2, ps("dividir até vale, mas", "i", 66) + [("o 3 também", "g", 66, COR)], W / 2, 520, "center", 0.1)
    eq_f(c, t, [("f{2x}{2}", TINTA, c4 + 0.4), ("+", TINTA, c4 + 0.4), ("f{3}{2}", COR, c4 + 0.8), ("=", TINTA, c4 + 0.4), ("f{11}{2}", TINTA, c4 + 0.4)], W / 2, 690, 100)
    E.frase(c, t, d4, ps("tire primeiro", "i", 84) + [("o número sem letra", "g", 84, COR)], W / 2, 940, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5 = C["s15.a"], C["s15.b"]
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7, d7 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]

    def frase_pop():
        E.frase(c, t, C["s15"] + 0.3, ps("agora, o atalho", "i", 76, CLARO), W / 2, 200, "center", 0.11)
        E.frase(c, t, a5, ps("passa para o outro lado", "g", 100, BR), W / 2, 420, "center", 0.12)
        E.frase(c, t, a5 + 1.2, ps("trocando o sinal", "g", 100, BR), W / 2, 550, "center", 0.12)
        E.frase(c, t, b5, ps("é", "i", 84, CLARO) + [("a balança", "g", 90, BR)] + ps("escrita mais rápido", "i", 84, CLARO), W / 2, 800, "center", 0.12)
    E.saida(c, t, C["s16"] - 0.1, frase_pop)

    if C["s16"] - 0.1 <= t:
        def pulo():
            t0 = C["s16"] + 0.3
            E.frase(c, t, t0, ps("subtraia 3 de cada lado", "i", 70, CLARO), W / 2, 170, "center", 0.1)
            size = 120
            xs, ws = eq_linha(c, t, [("2x", BR, t0), ("+ 3", BR, t0), ("− 3", CLARO, t0 + 2.8), ("=", BR, t0), ("11", BR, t0), ("− 3", CLARO, t0 + 2.8)], W / 2, 380, size)
            if t >= a6:
                E.risco(c, xs[1] - 10, 330, xs[2] + ws[2] + 10, 330, t, a6, ERRADO, 10)
                E.frase(c, t, a6 + 0.2, ps("sumiu", "i", 56, CLARO), xs[1] + (xs[2] + ws[2] - xs[1]) / 2, 480, "center")
            if t >= b6:
                realce(c, t, b6, xs[5], 380, ws[5], size, CLARO)
                E.frase(c, t, b6 + 0.2, ps("apareceu", "i", 56, CLARO), xs[5] + ws[5] / 2, 480, "center")
            # o mesmo, escrito mais rápido
            y2 = 830
            xs2, ws2 = eq_linha(c, t, [("2x", BR, c6 - 0.4), ("+ 3", CINZA, c6 - 0.4), ("=", BR, c6 - 0.4), ("11", BR, c6 - 0.4), ("− 3", BR, c6 + 0.6)], W / 2, y2, size)
            E.salto(c, t, c6, xs2[1] + ws2[1] / 2, xs2[4] + ws2[4] / 2, y2 - 120, 100, CLARO, "pulou o igual", size=50)
        E.saida(c, t, C["s17"] - 0.1, pulo)

    if t >= C["s17"]:
        E.frase(c, t, C["s17"] + 0.2, [("cuidado:", "g", 76, BR)] + ps("só para o que", "i", 76, CLARO) + [("soma ou subtrai", "g", 76, BR)], W / 2, 180, "center", 0.11)
        E.frase(c, t, a7 + 2.0, ps("com letra ou sem", "i", 60, CLARO), W / 2, 270, "center", 0.1)
        E.frase(c, t, b7 - 1.6, ps("o número que multiplica", "i", 72, CLARO) + [("passa dividindo", "g", 76, BR)], W / 2, 410, "center", 0.1)
        E.frase(c, t, b7 + 1.0, ps("e não vira menos", "i", 60, CLARO), W / 2, 490, "center", 0.1)
        fcen(c, t, lerp(b7, c7, 0.6), "2x = 10", 620, 680, 110, BR)
        E.foco(c, t, c7, 0.5, lambda a: E.formula(c, "x = f{10}{2} = 5", 1300, 680, 110, "g", CLARO, a, "center"))
        E.frase(c, t, d7, ps("na dúvida,", "i", 76, CLARO) + [("faça a conta nos dois lados", "g", 76, BR)], W / 2, 930, "center", 0.11)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s18.a"] - 0.9, ps("resolva", "i", 80), XE, 340, passo=0.1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "7x − 4 = 3x + 20", XE, 540, 128, "g", COR, a))
    E.frase(c, t, C["s18.b"], ps("quanto vale", "i", 90) + [("x?", "g", 96, COR)], XE, 760, passo=0.12)
    E.relogio(c, t, C["s19.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc, kd = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    cx = 820

    def resolve():
        fcen(c, t, C["s20"] + 0.2, "7x − 4 = 3x + 20", cx, 190, 100)
        E.frase(c, t, C["s20"] + 1.2, ps("deixe o x no lado com", "i", 60) + [("mais x", "g", 60, COR)], cx, 300, "center", 0.09)
        linhas = ((ka, "− 3x", kb, "4x − 4 = 20"), (kc, "+ 4", kc + 2.1, "4x = 24"), (kd, "÷ 4", kd + 2.0, "x = 6"))
        for i, (k0, op, k1, r) in enumerate(linhas):
            y = 450 + i * 170
            E.foco(c, t, k0, 0.5, lambda a, op=op, y=y: E.pilula(c, op, 300, y - 36, 60, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, k0 + 0.3, ps("nos dois lados", "i", 46, TINTA2), 300, y + 50, "center", 0.06)
            fcen(c, t, k1, r, cx + 100, y, 100, COR if i == 2 else None)
        bola_res(c, t, kd + 2.6, "x = 6", 1600, 620, 150, 90)
    E.saida(c, t, C["s21"] - 0.1, resolve)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, [("conferindo", "i", 84, COR)], W / 2, 170, "center")
    fcen(c, t, a1, "7 × 6 − 4", 560, 380, 100)
    fcen(c, t, lerp(a1, b1, 0.3), "= 42 − 4", 560, 510, 100)
    fcen(c, t, lerp(a1, b1, 0.6), "= 38", 560, 640, 110, COR)
    fcen(c, t, b1, "3 × 6 + 20", 1360, 380, 100)
    fcen(c, t, lerp(b1, c1, 0.45), "= 18 + 20", 1360, 510, 100)
    fcen(c, t, lerp(b1, c1, 0.8), "= 38", 1360, 640, 110, COR)
    fcen(c, t, c1 - 0.6, "38 = 38", W / 2 - 50, 860, 120, CERTO)
    E.foco(c, t, c1, 0.5, lambda a: E.selo(c, W / 2 + 270, 820, 54, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "junte o x no lado que tem mais"), ("s22.b", "tire o número sem letra"),
                                    ("s22.c", "divida pelo número que multiplica a letra"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 240, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 72)], 330, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a3 - 0.2, ps("equação com", "i", 100) + [("parênteses", "g", 110, COR)], XE, 390, passo=0.14)
    E.frase(c, t, b3, ps("e uma equação que", "i", 72) + [("nenhum número resolve", "g", 72, COR)], XE, 530, passo=0.09)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ordem=b_ordem, lados=b_lados, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
