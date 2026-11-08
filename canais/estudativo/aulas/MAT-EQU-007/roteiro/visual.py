"""Visual — Estudativo · MAT-EQU-007: o que é equação, fazer o mesmo nos dois lados.
A balança é E.balanca; o que vai nos pratos (caixas x e pesos de 1 kg) é a peça local carga(). As equações ficam na coluna da direita,
uma linha por passo, no tempo da fala. Todo instante vem de C[...]."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-007_o_que_e_equacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("testar", "balanca", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 * 4 + 1 == 9 and 2 * 3 + 1 == 7 and 12 - 7 == 5 and 5 + 7 == 12 and 12 / 3 == 4 and 3 * 4 == 12
assert 5 * 4 == 20 and 20 / 4 == 5 and 3 * 9 == 27 and 9 + 6 == 15 and 15 - 6 == 9 and 3 - 6 == -3
assert [2 * v + 1 for v in (3, 4, 5, 6)] == [7, 9, 11, 13]


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


P, P2, GG, S = 54, 60, 22, 100  # peso, passo dos pesos, folga entre grupos, caixa


def peso(c, x, y, a=1.0, cor=TINTA):
    """peso de 1 kg; (x, y) = canto de baixo à esquerda"""
    M.rrect(c, x, y - P, P, P, 8, cor, a)
    centro(c, "1", x + P / 2, y - 15, 34, "g", BR, a)


def caixa(c, x, y, a=1.0, cor=None, quartos=None):
    """caixa de peso desconhecido x; (x, y) = canto de baixo à esquerda. quartos = (cheios 0..4, contorno 0..1): caixa em 4 fatias"""
    cor = cor or E.COR
    if quartos is None:
        M.rrect(c, x, y - S, S, S, 12, cor, a)
        centro(c, "x", x + S / 2, y - 28, 70, "g", BR, a)
        return
    cheios, cont = quartos
    q = S / 4
    if cont > 0:
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - S, S, S), 12, 12)
        c.drawRRect(rr, M.paint(E.COR, a * cont, stroke=4))
    for i in range(4):
        f = E.clamp(cheios - i)
        if f > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + i * q, y - S, q, S), M.paint(cor, a * f))
    for i in range(1, 4):
        if cont > 0 or i < cheios:
            M.line(c, x + i * q, y - S + 4, x + i * q, y - 4, BR if i < cheios else E.COR, a * max(cont, 1.0 if i < cheios else 0), 3)


def carga(nc=0, n=0, cols=6, grupos=1, sai_n=0, sai=0.0, div=0.0, destaque=0.0, quartos=None, a=1.0, ap=None):
    """o que vai num prato: nc caixas x e n pesos (em grupos lado a lado). Os últimos sai_n pesos sobem e somem com sai 0..1.
    div 0..1 traça as divisões entre caixas e entre grupos; destaque 0..1 apaga tudo menos a 1ª caixa e o 1º grupo.
    ap(i) = alfa do peso i (entrada um a um)."""
    def fn(c, x, y):
        if a <= 0:
            return
        per = n // grupos if n else 0
        gc = min(cols, per) if per else 0
        wg = gc * P2 - (P2 - P) if gc else 0
        ww = grupos * wg + (grupos - 1) * GG if n else 0
        wb = nc * (S + 14) - 14 if nc else 0
        tot = wb + ww + (30 if nc and n else 0)
        x0 = x - tot / 2
        base = y + 18
        apaga = lambda i: 1 - 0.7 * destaque if i > 0 else 1.0
        for i in range(nc):
            caixa(c, x0 + i * (S + 14), base, a * apaga(i), quartos=quartos)
            if div > 0 and i > 0:
                lx = x0 + i * (S + 14) - 7
                M.line(c, lx, base + 6, lx, base - (S + 30) * div, E.COR, a, 5, dash=[10, 8])
        xp = x0 + wb + (30 if nc and n else 0)
        for i in range(n):
            g, k = divmod(i, per)
            px = xp + g * (wg + GG) + (k % gc) * P2
            py = base - (k // gc) * P2
            al = a * apaga(g) * (ap(i) if ap else 1.0)
            if i >= n - sai_n:
                py -= 90 * ease_io(sai)
                al *= 1 - sai
            if al > 0:
                peso(c, px, py, al)
        if div > 0 and grupos > 1:
            alto = -(-per // gc) * P2 + 26
            for g in range(1, grupos):
                lx = xp + g * (wg + GG) - GG / 2
                M.line(c, lx, base + 6, lx, base - alto * div, E.COR, a, 5, dash=[10, 8])
    return fn


def entra(t, t0, n, d=0.06):
    """alfa do peso i, que entra um depois do outro a partir de t0"""
    return lambda i: ep(t, t0 + i * d, 0.25)


BX, BY, BL = 600, 600, 560  # balança das cenas com equação à direita
RX = 1460  # centro da coluna das equações


def balanca(c, t, t0, esq, dir_, inclina=0.0, cx=BX, cy=BY, larg=BL):
    E.foco(c, t, t0, 0.6, lambda a: E.balanca(c, cx, cy, esq, dir_, inclina, a, larg_braco=larg), blur=8)


def rotulo(c, t, t0, s, cx, y=790, cor=None, t1=None, est="i"):
    fn = lambda: E.frase(c, t, t0, ps(s, est, 54 if est == "i" else 46, cor or COR), cx, y, "center", 0.08)
    if t1 is None:
        fn()
    else:
        E.saida(c, t, t1, fn)


def realce(c, t, t0, x, y, w, size, cor=None):
    """fundo leve atrás de um trecho já escrito"""
    q = ep(t, t0, 0.3)
    if q > 0:
        M.rrect(c, x - size * 0.12, y - size * 0.9, w + size * 0.24, size * 1.15, size * 0.18, cor or E.COR, 0.14 * q)


def eq_linha(c, t, partes, cx, y, size):
    """equação em partes [(texto, cor, t0)], centrada; devolve os x"""
    return E.linha(c, t, [(s, "g", size, cor, t0) for s, cor, t0 in partes], cx, y, "center")


def eq_f(c, t, partes, cx, y, size):
    """como eq_linha, mas cada parte é uma fórmula (aceita f{x}{4})"""
    ws = [E.formula(c, s, 0, 0, size, a=0) for s, _, _ in partes]
    gap = size * 0.26
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for (s, cor, t0), w in zip(partes, ws):
        xs.append(x)
        E.formula_em(c, t, t0, s, x, y, size, "g", cor)
        x += w + gap
    return xs


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        eq_linha(c, t, [("2x", TINTA, ka), ("+", TINTA, ka + 0.9), ("1", TINTA, ka + 1.1), ("=", TINTA, ka + 1.5), ("9", TINTA, ka + 2.0)], W / 2, 400, 210)
        E.frase(c, t, kb - 0.8, ps("alguém diz:", "i", 80), W / 2, 590, "center", 0.12)
        eq_linha(c, t, [("x", COR, kb), ("=", COR, kb + 0.2), ("4", COR, kb + 0.4), ("?", TINTA, kb + 1.2)], W / 2, 760, 150)
        E.linha(c, t, [("em", "i", 76, TINTA, lerp(kb, kc, 0.62)), ("5 segundos,", "g", 76, COR, lerp(kb, kc, 0.72)),
                       ("sem resolver nada", "i", 82, TINTA, kc)], W / 2, 930, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), [("conferir", "g", 110, COR)] + ps("e", "i", 100) + [("resolver", "g", 110, COR)], XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.75), ps("equações", "i", 90), XE, 600, passo=0.1)
        E.frase(c, t, tb - 0.3, ps("com uma", "i", 90) + [("balança", "g", 96, COR)], XE, 730, passo=0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "trocar a letra por um número", "e fazer a conta"), ("s03.c", "multiplicar e dividir", "com sinal de menos"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.c"] + 3.1, ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 960, 820, "left", 0.12)


# ---------------- o que é equação e como testar ----------------
def b_testar(c, t, C, b):
    def oque():
        ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, C["s04"] + 0.3, ps("o que é uma", "i", 84) + [("equação?", "g", 84, COR)], W / 2, 170, "center", 0.12)
        size, y = 200, 460
        t0 = ka - 0.6
        cx_ = lambda tt: COR if t >= tt else TINTA
        partes = [("2x", "g", size, TINTA, t0), ("+", "g", size, TINTA, t0 + 0.1), ("1", "g", size, TINTA, t0 + 0.2),
                  ("=", "g", size, cx_(ka), t0 + 0.3), ("9", "g", size, TINTA, t0 + 0.4)]
        _, xs = E._arranjo(partes, W / 2, "center")
        realce(c, t, ka, xs[3], y, E.larg("=", "g", size), size)
        xx = xs[0] + E.larg("2", "g", size) + E.APERTO["g"] * size
        realce(c, t, kb, xx, y, E.larg("x", "g", size), size)
        E.linha(c, t, partes, W / 2, y, "center")
        if t >= kb:
            E.foco(c, t, kb, 0.4, lambda a: E.escreve(c, "x", xx, y, size, "g", COR, a))
        E.frase(c, t, ka + 0.2, ps("sinal de", "i", 56) + [("igual", "g", 56, COR)], xs[3] + E.larg("=", "g", size) / 2, y + 110, "center", 0.08)
        E.frase(c, t, kb + 0.2, ps("a", "i", 60) + [("letra", "g", 60, COR)] + ps("guarda o número que você não conhece", "i", 60), W / 2, y + 200, "center", 0.07)
        fcen(c, t, kc, "2x = 2 × x", W / 2, 810, 120, COR)
        E.frase(c, t, kd - 0.6, ps("resolver é achar", "i", 70) + [("o número que deixa os lados iguais", "g", 64, COR)], W / 2, 970, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, oque)
    if t < C["s05"]:
        return

    # testar o 4 e o 3
    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    fcen(c, t, C["s05"] + 0.2, "2x + 1 = 9", W / 2, 180, 120)
    xl, xr = 540, 1380
    E.foco(c, t, C["s05"] + 0.4, 0.5, lambda a: E.pilula(c, "x = 4", xl, 300, 72, "g", a=a, cor=E.SOBRE))
    E.expressao(c, t, [("2 × 4 + 1", "2 × 4", b5), ("8 + 1", "8 + 1", c5), ("9", None)], [b5 + 0.9, c5 + 1.0], xl, 480, 104, empilha=120, t0=a5)
    E.foco(c, t, d5, 0.5, lambda a: E.formula(c, "9 = 9", xl, 860, 120, "g", CERTO, a, "center"))
    E.foco(c, t, e5, 0.5, lambda a: E.selo(c, xl + 250, 820, 54, True, a))
    E.foco(c, t, C["s06"] + 0.5, 0.5, lambda a: E.pilula(c, "x = 3", xr, 300, 72, "g", a=a, cor=E.SOBRE))
    E.expressao(c, t, [("2 × 3 + 1", "2 × 3", a6), ("6 + 1", "6 + 1", a6 + 1.5), ("7", None)], [a6 + 1.0, a6 + 2.6], xr, 480, 104, empilha=120, t0=a6)
    E.foco(c, t, b6, 0.5, lambda a: E.formula(c, "7 ≠ 9", xr, 860, 120, "g", ERRADO, a, "center"))
    E.foco(c, t, c6, 0.5, lambda a: E.selo(c, xr + 250, 820, 54, False, a))
    E.frase(c, t, d6, ps("esse teste é", "i", 66) + [("conferir substituindo", "g", 66, COR)], W / 2, 1000, "center", 0.1)


# ---------------- a balança ----------------
def b_balanca(c, t, C, b):
    ka, kb = C["s07.a"], C["s07.b"]
    a8, b8 = C["s08.a"], C["s08.b"]
    cx, cy, lb = W / 2, 640, 760
    t_tira1, t_tira2 = b8 + 0.4, lerp(b8, C["s08.end"], 0.25)  # "Tirou um peso" / "Tire o mesmo peso do outro"
    s1, s2 = ep(t, t_tira1, 0.6), ep(t, t_tira2, 0.6)
    inc = 0.8 * ease_io(prog(t, t_tira1 + 0.2, 0.6)) * (1 - ease_io(prog(t, t_tira2 + 0.2, 0.6)))
    E.foco(c, t, ka, 0.6, lambda a: E.balanca(c, cx, cy, carga(n=3, cols=3, sai_n=1, sai=s1), carga(n=3, cols=3, sai_n=1, sai=s2), inc, a, larg_braco=lb), blur=8)
    E.saida(c, t, a8 - 0.2, lambda: E.frase(c, t, C["s07"] + 0.2, ps("como achar o número", "i", 84) + [("sem chutar?", "g", 84, COR)], W / 2, 170, "center", 0.12))
    E.saida(c, t, a8 - 0.2, lambda: (E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "=", cx, 290, 90, "g", a=a, cor=E.SOBRE)),
                                     E.frase(c, t, kb + 0.3, ps("o igual é", "i", 70) + [("o equilíbrio", "g", 70, COR)], cx - 90, 312, "right", 0.1),
                                     E.frase(c, t, lerp(kb, C["s07.end"], 0.4), ps("esquerda pesa o mesmo que direita", "i", 66), W / 2, 1000, "center", 0.08)))
    if t >= a8 - 0.2:
        E.frase(c, t, a8, ps("faça", "i", 96) + [("o mesmo", "g", 96, COR)] + ps("nos dois lados", "i", 96), W / 2, 180, "center", 0.12)
        E.saida(c, t, t_tira2 + 0.9, lambda: E.frase(c, t, t_tira1, ps("tirou um peso?", "i", 70, ERRADO), cx - lb / 2, 1000, "center", 0.1))
        E.frase(c, t, t_tira2, ps("tire o mesmo do outro", "i", 70, CERTO), cx + lb / 2, 1000, "center", 0.1)
        E.foco(c, t, lerp(b8, C["s08.end"], 0.62), 0.5, lambda a: E.pilula(c, "a regra de todas as equações", cx, 300, 60, "g", a=a, cor=E.SOBRE))


# ---------------- x + 7 = 12 ----------------
def b_somar(c, t, C, b):
    ka, kb, kc, kd = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    s1, s2 = ep(t, a0 + 0.3, 0.8), ep(t, b0 + 0.3, 0.8)
    inc = 0.7 * ease_io(prog(t, a0 + 0.6, 0.6)) * (1 - ease_io(prog(t, b0 + 0.6, 0.6)))
    esq = carga(nc=1 if t >= kb else 0, n=7 if t >= kc else 0, cols=4, sai_n=7, sai=s1, ap=entra(t, kc, 7))
    dir_ = carga(n=12 if t >= kd else 0, cols=6, sai_n=7, sai=s2, ap=entra(t, kd, 12, 0.05))
    balanca(c, t, ka - 0.2, esq, dir_, inc)
    rotulo(c, t, kb + 0.2, "a caixa é o x", BX - BL / 2 - 20, t1=c0)
    rotulo(c, t, kc + 0.3, "7 pesos de 1 kg", BX - BL / 2 - 60, 862, TINTA2, t1=a0)
    rotulo(c, t, kd + 0.2, "12 pesos", BX + BL / 2, t1=b0)
    fcen(c, t, ka, "x + 7 = 12", RX, 260, 120)
    eq_linha(c, t, [("x + 7", TINTA, a0 - 0.2), ("− 7", COR, a0), ("=", TINTA, b0 - 0.2), ("12", TINTA, b0 - 0.2), ("− 7", COR, b0)], RX, 440, 84)
    E.foco(c, t, c0, 0.5, lambda a: (E.bola(c, RX, 590, 135, a=a), E.formula(c, "x = 5", RX, 622, 86, "g", E.SOBRE, a, "center")))
    fcen(c, t, d0, "5 + 7 = 12", RX - 60, 850, 100, CERTO)
    E.foco(c, t, lerp(d0, C["s10.end"], 0.6), 0.5, lambda a: E.selo(c, RX + 250, 815, 48, True, a))


# ---------------- 3x = 12 ----------------
def b_vezes(c, t, C, b):
    ka, kb, kc, kd, ke, kf, kg = (C[f"s11.{k}"] for k in "abcdefg")
    td = lerp(kd, ke, 0.55)  # "três partes iguais": fica só uma parte
    esq = carga(nc=3 if t >= kb else 0, div=ep(t, kd, 0.8), destaque=ep(t, td, 0.6))
    dir_ = carga(n=12 if t >= kc else 0, cols=2, grupos=3, div=ep(t, kd + 0.3, 0.8), destaque=ep(t, td, 0.6), ap=entra(t, kc, 12, 0.05))
    balanca(c, t, ka - 0.2, esq, dir_)
    rotulo(c, t, kb + 0.3, "3 caixas", BX - BL / 2)
    rotulo(c, t, kc + 0.3, "12 pesos", BX + BL / 2)
    E.frase(c, t, td, ps("cada parte:", "i", 60) + [("1 caixa e 4 pesos", "g", 60, COR)], BX, 960, "center", 0.1)
    fcen(c, t, ka, "3x = 12", RX, 260, 120)
    eq_linha(c, t, [("3x", TINTA, kd), ("÷ 3", COR, kd + 0.3), ("=", TINTA, kd + 0.6), ("12", TINTA, kd + 0.6), ("÷ 3", COR, kd + 0.9)], RX, 440, 84)
    if t >= ke:
        xs = E._arranjo([(s, "g", 84) for s in ("3x", "÷ 3", "=", "12", "÷ 3")], RX, "center")[1]
        realce(c, t, ke, xs[3], 440, xs[4] + E.larg("÷ 3", "g", 84) - xs[3], 84)
    E.foco(c, t, kf, 0.5, lambda a: (E.bola(c, RX, 590, 135, a=a), E.formula(c, "x = 4", RX, 622, 86, "g", E.SOBRE, a, "center")))
    fcen(c, t, kg, "3 × 4 = 12", RX - 60, 850, 100, CERTO)
    E.foco(c, t, kg + 1.2, 0.5, lambda a: E.selo(c, RX + 250, 815, 48, True, a))


# ---------------- x/4 = 5 ----------------
def b_dividir(c, t, C, b):
    ka, kb, kc, kd, ke, kf, kg = (C[f"s12.{k}"] for k in "abcdefg")
    cheios = 1 + 3 * ease_io(prog(t, ke + 0.3, 0.8))
    cont = ep(t, kd, 0.6)
    esq = carga(nc=1, quartos=(cheios, cont))
    n = 20 if t >= ke + 0.3 else 5
    dir_ = carga(n=n, cols=5, ap=(lambda i: 1.0 if i < 5 else ep(t, ke + 0.3 + (i - 5) * 0.05, 0.25)))
    balanca(c, t, kc - 0.2, esq, dir_)
    E.saida(c, t, kd, lambda: rotulo(c, t, kc + 0.2, "1/4 da caixa", BX - BL / 2))
    rotulo(c, t, kd + 0.2, "4 pedaços: a caixa", BX - BL / 2 - 20)
    E.saida(c, t, ke + 0.3, lambda: rotulo(c, t, kc + 0.5, "5 kg", BX + BL / 2))
    rotulo(c, t, ke + 1.0, "4 × 5 = 20 kg", BX + BL / 2, est="g")
    fcen(c, t, ka, "f{x}{4} = 5", RX, 270, 120)
    E.saida(c, t, ke - 0.2, lambda: E.frase(c, t, kb, [("x ÷ 4", "g", 84, COR)] + ps("x dividido por 4", "i", 56), RX, 450, "center", 0.12))
    if t >= ke - 0.2:
        eq_f(c, t, [("f{x}{4}", TINTA, ke), ("× 4", COR, ke + 0.3), ("=", TINTA, ke + 0.6), ("5", TINTA, ke + 0.6), ("× 4", COR, ke + 0.9)], RX, 450, 84)
    E.foco(c, t, kf, 0.5, lambda a: (E.bola(c, RX, 610, 135, a=a), E.formula(c, "x = 20", RX, 640, 76, "g", E.SOBRE, a, "center")))
    fcen(c, t, kg, "20 ÷ 4 = 5", RX - 60, 860, 100, CERTO)
    E.foco(c, t, kg + 1.4, 0.5, lambda a: E.selo(c, RX + 260, 825, 48, True, a))


# ---------------- o padrão ----------------
def b_padrao(c, t, C, b):
    E.frase(c, t, C["s13"] + 0.2, ps("repare no", "i", 84) + [("padrão", "g", 84, COR)], W / 2, 160, "center", 0.12)
    linhas = (("s13.a", "x + 7", "número somando", "subtraia"), ("s13.b", "3x", "número multiplicando", "divida"),
              ("s13.c", "f{x}{4}", "número dividindo", "multiplique"), ("s13.d", "x − 6", "número subtraindo", "some"))
    for i, (k, f, l, r) in enumerate(linhas):
        y = 320 + i * 150
        fcen(c, t, C[k], f, 340, y, 84)
        E.frase(c, t, C[k] + 0.1, ps(l, "i", 64), 520, y, "left", 0.08)
        if t >= C[k] + 0.5:
            M.arrow(c, 1110, y - 22, 1230, y - 22, TINTA2, ep(t, C[k] + 0.5, 0.3), 5, 16, ep(t, C[k] + 0.5, 0.4))
        E.frase(c, t, C[k] + 0.7, [(r, "g", 80, COR)], 1270, y)
    E.frase(c, t, C["s13.e"], ps("sempre", "i", 96) + [("nos dois lados", "g", 96, COR)], W / 2, 950, "center", 0.14)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def um():
        E.frase(c, t, ka - 0.4, ps("o erro:", "i", 84) + [("a conta errada", "g", 84, ERRADO)] + ps("para tirar o número", "i", 84), W / 2, 170, "center", 0.11)
        fcen(c, t, lerp(ka, kb, 0.6), "3x = 12", W / 2, 400, 140)
        eq_linha(c, t, [("3x", TINTA, kb), ("− 3", ERRADO, kb + 0.2), ("=", TINTA, kb + 0.5), ("12", TINTA, kb + 0.5), ("− 3", ERRADO, kb + 0.8)], W / 2, 610, 120)
        fcen(c, t, kc, "x = 9", W / 2, 840, 150, ERRADO)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("o 3", "i", 84) + [("não está somando", "g", 84, ERRADO)], W / 2, 170, "center", 0.12)
    E.foco(c, t, a5, 0.5, lambda a: E.formula(c, "3x = 3 × x", W / 2, 380, 130, "g", TINTA, a, "center"))
    E.frase(c, t, a5 + 0.3, ps("ele", "i", 66) + [("multiplica", "g", 66, COR)] + ps("o x", "i", 66), W / 2, 480, "center", 0.1)
    xs = eq_linha(c, t, [("3 × 9", TINTA, b5), ("=", TINTA, b5 + 0.4), ("27", ERRADO, b5 + 0.9), ("≠ 12", ERRADO, c5)], W / 2 - 60, 680, 130)
    E.foco(c, t, c5 + 0.3, 0.5, lambda a: E.selo(c, W / 2 + 470, 635, 56, False, a))
    E.frase(c, t, d5, ps("esse número", "i", 84) + [("soma", "g", 84, COR)] + ps("ou", "i", 84) + [("multiplica?", "g", 84, COR)], W / 2, 900, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]

    def regra():
        E.frase(c, t, C["s16"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("em questão com alternativas,", "i", 80, CLARO), W / 2, 270, "center", 0.1)
        E.frase(c, t, lerp(ka, kb, 0.35), [("teste as alternativas", "g", 96, BR)], W / 2, 390, "center")
        E.foco(c, t, kb - 0.4, 0.5, lambda a: E.formula(c, "2x + 1 = 9", W / 2, 540, 110, "g", CLARO, a, "center"))
        for i, v in enumerate((3, 4, 5, 6)):
            x = 480 + i * 320
            ti = kb + 0.4 + i * 0.5
            ok = v == 4
            E.foco(c, t, ti, 0.5, lambda a, v=v, x=x, i=i: E.pilula(c, f"{'ABCD'[i]})  {v}", x, 680, 66, "g", a=a, cor=E.SOBRE))
            E.foco(c, t, ti + 0.3, 0.5, lambda a, v=v, x=x, ok=ok: E.formula(c, f"→ {2 * v + 1}", x, 820, 76, "g", (CERTO if ok and t >= kc else BR) if ok else CLARO, a, "center"))
            if ok:
                E.foco(c, t, kc + 0.3, 0.5, lambda a, x=x: E.selo(c, x + 130, 800, 40, True, a))
        E.frase(c, t, kc, ps("qual deixa", "i", 76, CLARO) + [("os lados iguais?", "g", 76, BR)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s17"] - 0.1, regra)
    if t < C["s17"]:
        return
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, a7, [("conferir", "g", 110, BR)] + ps("é mais rápido que", "i", 96, CLARO) + [("resolver", "g", 110, BR)], W / 2, 260, "center", 0.14)
    E.frase(c, t, lerp(a7, b7, 0.5), ps("como o 4 do começo", "i", 70, CLARO), W / 2, 370, "center", 0.1)
    E.foco(c, t, b7, 0.5, lambda a: E.selo(c, 300, 545, 56, False, a))
    E.frase(c, t, b7 + 0.1, ps("não compensa com números", "i", 62, CLARO) + [("grandes", "g", 62, BR)] + ps("ou", "i", 62, CLARO) + [("quebrados", "g", 62, BR)], 390, 570, "left", 0.09)
    for i, s in enumerate(("1.248", "f{17}{3}", "2,375")):
        E.foco(c, t, lerp(b7, c7, 0.55) + i * 0.25, 0.5, lambda a, s=s, i=i: E.formula(c, s, 560 + i * 330, 720, 80, "g", CLARO, a, "center"))
    E.frase(c, t, c7, ps("aí,", "i", 96, CLARO) + [("use a balança", "g", 96, BR)], 820, 930, "center", 0.12)

    def mini(a):
        c.save(); c.translate(1500, 880); c.scale(0.42, 0.42)
        E.balanca(c, 0, 0, "", "", 0, a, larg_braco=560, escuro=True)
        c.restore()
    E.foco(c, t, c7 + 0.3, 0.6, mini, blur=6)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s18.a"] - 0.8, ps("resolva", "i", 80), XE, 340, passo=0.1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "x − 6 = 9", XE, 560, 190, "g", COR, a))
    E.frase(c, t, C["s18.b"], ps("quanto vale", "i", 90) + [("x?", "g", 96, COR)], XE, 760, passo=0.12)
    E.relogio(c, t, C["s19.a"], 1490, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s20.{k}"] for k in "abcde")
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    cx = 760
    neg = lerp(ke, C["s20.end"], 0.18)  # "Na balança, não dá para desenhar um peso negativo"
    regra = lerp(ke, C["s20.end"], 0.52)  # "mas a regra não muda"

    def resolve():
        fcen(c, t, C["s20"] + 0.2, "x − 6 = 9", cx, 190, 110)
        E.frase(c, t, ka - 0.2, ps("o 6 está", "i", 64) + [("subtraindo:", "g", 64, COR)] + ps("some 6", "i", 64), cx, 320, "center", 0.1)
        xs = eq_linha(c, t, [("x − 6", TINTA, kb - 0.3), ("+ 6", COR, kb), ("=", TINTA, kb + 0.3), ("9", TINTA, kb + 0.3), ("+ 6", COR, kb + 0.6)], cx, 480, 116)
        E.frase(c, t, kc, ps("−6 + 6 = 0", "g", 60, TINTA2), xs[1] - 40, 600, "center", 0.05)
        E.frase(c, t, kd, ps("9 + 6 = 15", "g", 60, TINTA2), xs[4] - 10, 600, "center", 0.05)
        E.foco(c, t, ke, 0.5, lambda a: (E.bola(c, 1560, 450, 170, a=a), E.formula(c, "x = 15", 1560, 490, 104, "g", E.SOBRE, a, "center")))
        E.frase(c, t, neg, ps("peso negativo não cabe na balança,", "i", 64), W / 2, 790, "center", 0.07)
        E.frase(c, t, regra, ps("mas a regra vale igual:", "i", 70) + [("o mesmo nos dois lados", "g", 70, COR)], W / 2, 920, "center", 0.09)
    E.saida(c, t, C["s21"] - 0.1, resolve)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, [("conferindo", "i", 84, COR)], W / 2, 170, "center")
    fcen(c, t, a1, "15 − 6 = 9", W / 2 - 60, 350, 120, CERTO)
    E.foco(c, t, a1 + 1.6, 0.5, lambda a: E.selo(c, W / 2 + 290, 310, 54, True, a))
    E.frase(c, t, b1 - 0.9, ps("quem subtraiu 6 achou", "i", 70), W / 2 - 80, 560, "center", 0.09)
    E.foco(c, t, b1, 0.5, lambda a: E.formula(c, "x = 3", W / 2 + 390, 560, 90, "g", ERRADO, a, "center"))
    xs = eq_linha(c, t, [("3 − 6", TINTA, c1 - 0.6), ("=", TINTA, c1), ("−3", ERRADO, c1 + 0.4), ("≠ 9", ERRADO, c1 + 1.5)], W / 2 - 60, 780, 120)
    E.foco(c, t, c1 + 1.8, 0.5, lambda a: E.selo(c, W / 2 + 500, 740, 54, False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "equação é uma balança"), ("s22.b", "faça o mesmo nos dois lados"), ("s22.c", "confira substituindo"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 350, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a3, [("mais de um passo", "g", 110, COR)], XE, 390, passo=0.14)
    E.frase(c, t, b3, ps("e", "i", 84) + [("x", "g", 90, COR)] + ps("nos dois pratos da balança", "i", 84), XE, 530, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, testar=b_testar, balanca=b_balanca, somar=b_somar, vezes=b_vezes, dividir=b_dividir,
              padrao=b_padrao, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
