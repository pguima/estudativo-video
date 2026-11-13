"""Visual — Estudativo · QUI-ATO-004: prótons, nêutrons e elétrons; Z, A, íons e isótopos.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001). Nesta aula:
- PARTÍCULAS: próton = esfera turquesa com "+"; nêutron = esfera cinza lisa; elétron = esfera azul com "−".
  Núcleo = cacho de prótons e nêutrons (nucleo()); a contagem fica num quadro de três linhas (contagem()) com a bolinha,
  o nome e o número; a conta de apoio em cinza-tinta e o número final na cor da partícula.
- NOTAÇÃO DO ÁTOMO: Q.formula("^{23}_{11}Na^+"): número de massa em cima, número atômico embaixo, carga no alto à direita.
  A parte que a fala explica vai na cor da matéria.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-004_protons_neutrons_eletrons.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("particulas", "za", "ions", "isotopos", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEUTRON = "#8A8D96"

# contas da aula
assert 23 - 11 == 12 and 11 - 1 == 10
assert 35 - 17 == 18 and 17 + 1 == 18 and 17 - (-1) == 18
assert (13, 27 - 13, 13 - 3) == (13, 14, 10)
assert 3 - (-5) == 8
assert [12 - 6, 13 - 6, 14 - 6] == [6, 7, 8]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def particula(c, x, y, r, tipo, a=1.0):
    """p = próton (turquesa, +), n = nêutron (cinza), e = elétron (azul, −)"""
    if a <= 0 or r <= 0:
        return
    cor = {"p": E.COR, "n": NEUTRON, "e": Q.ELETRON}[tipo]
    E.bola(c, x, y, r, cor, a)
    w = max(3, r * 0.17)
    if tipo in "pe" and r >= 10:
        M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, w)
        if tipo == "p":
            M.line(c, x, y - r * 0.45, x, y + r * 0.45, BR, a, w)


def nucleo(c, t, t0, cx, cy, p, n, r=24, a=1.0, passo=0.04):
    """cacho de p prótons e n nêutrons, em espiral a partir do centro"""
    tot = p + n
    tipos = []
    for k in range(tot):     # alterna para misturar
        tipos.append("p" if (k % 2 == 0 and tipos.count("p") < p) or tipos.count("n") >= n else "n")
    for k in range(tot):
        g = k * 2.4
        d = r * 0.95 * math.sqrt(k)
        q = ease_back(prog(t, t0 + passo * k, 0.35)) if t0 is not None else 1
        particula(c, cx + d * math.cos(g), cy + d * math.sin(g), r * q, tipos[k], a)


def eletrons_volta(c, t, cx, cy, R, n, a=1.0, r=16, gira=0.5, some=()):
    """n elétrons numa órbita circular; os índices em some saem voando"""
    for k in range(n):
        g = math.tau * k / n + t * gira
        x, y = cx + R * math.cos(g), cy + R * math.sin(g)
        if k in some:
            continue
        particula(c, x, y, r, "e", a)


def contagem(c, t, linhas, x, y, dy=110, size=70):
    """linhas = [(t0, tipo, nome, valor, conta)]: bolinha, nome, número e a conta de apoio"""
    for i, (ti, tipo, nome, val, conta) in enumerate(linhas):
        yy = y + i * dy
        cor = {"p": COR, "n": TINTA, "e": Q.ELETRON}[tipo]
        E.foco(c, t, ti, 0.4, lambda a, yy=yy, tipo=tipo, nome=nome: (particula(c, x + 30, yy - 22, 28, tipo, a), E.escreve(c, nome, x + 80, yy, size * 0.8, "i", TINTA, a)))
        if conta:
            E.foco(c, t, ti + 0.3, 0.4, lambda a, yy=yy, conta=conta: E.formula(c, conta, x + 420, yy, size * 0.75, "g", TINTA2, a))
        wc = E.formula(None, conta, 0, 0, size * 0.75, "g", a=0) + 30 if conta else 0
        E.foco(c, t, ti + (0.7 if conta else 0.3), 0.4, lambda a, yy=yy, val=val, cor=cor, wc=wc: E.escreve(c, val, x + 420 + wc, yy, size, "g", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.formula_em(c, t, C["s01.a"], "^{23}Na^+", 360, 600, 300)
        E.frase(c, t, C["s01.a"] + 0.4, ps("sódio 23, carga um mais", "i", 56, TINTA2), 380, 760, passo=0.1)
        for k, (tp, nome) in enumerate((("p", "prótons"), ("n", "nêutrons"), ("e", "elétrons"))):
            y = 380 + k * 170
            E.foco(c, t, C["s01.b"] + 0.4 * k, 0.4, lambda a, y=y, tp=tp, nome=nome: (particula(c, 1180, y - 22, 34, tp, a), E.escreve(c, nome, 1250, y, 66, "i", TINTA, a),
                                                                                     centro(c, "?", 1700, y + 6, 100, "g", COR, a)))
        E.frase(c, t, C["s01.c"], ps("duas contas de", "i", 62) + [("menos", "g", 60, COR)], 1180, 960, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("contar as", "i", 70), ("partículas", "g", 66)]),
                 (C["s02.b"], [("dizer se são", "i", 70), ("isótopos", "g", 66, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula do ouro", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("núcleo", "g", 70, COR)] + ps("positivo e, em volta,", "i", 70) + [("eletrosfera", "g", 66, Q.ELETRON)], XE, 340, passo=0.12)
    E.foco(c, t, C["s03.a"] + 0.4, 0.5, lambda a: (E.bola(c, 1550, 330, 26, E.COR, a), c.drawCircle(1550, 330, 140, M.paint(Q.ELETRON, 0.1 * a))))
    E.frase(c, t, C["s03.b"], ps("da Matemática:", "i", 64, TINTA2), XE, 560, passo=0.12)
    E.frase(c, t, C["s03.b"] + 0.6, ps("subtrair um negativo é", "i", 70) + [("somar", "g", 66, COR)], XE, 660, passo=0.12)
    E.formula_em(c, t, C["s03.c"], "3 − (−5) = 8", XE, 860, 130, "g", TINTA)


# ---------------- as partículas ----------------
def b_particulas(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("dentro do", "i", 72) + [("núcleo", "g", 70, COR)], XE, 200, passo=0.12)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: particula(c, XE + 70, 360, 60, "p", a))
        E.frase(c, t, C["s04.a"] + 0.2, [("próton:", "g", 66, COR)] + ps("carga positiva", "i", 66), XE + 170, 385, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: particula(c, XE + 70, 540, 60, "n", a))
        E.frase(c, t, C["s04.b"] + 0.2, [("nêutron:", "g", 66)] + ps("sem carga, neutro", "i", 66), XE + 170, 565, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("quase a", "i", 64) + [("mesma massa", "g", 60)], XE, 760, passo=0.1)
        E.frase(c, t, C["s04.c"] + 1.4, ps("e quase toda a massa do átomo", "i", 60, TINTA2), XE, 850, passo=0.1)
        nucleo(c, t, C["s04.a"] + 0.3, 1480, 560, 6, 6, 40)
        return
    E.frase(c, t, C["s05.a"], ps("na eletrosfera:", "i", 66) + [("elétrons", "g", 64, Q.ELETRON)], XE, 220, passo=0.12)
    E.foco(c, t, C["s05.a"] + 0.3, 0.5, lambda a: particula(c, XE + 900, 200, 40, "e", a))
    E.frase(c, t, C["s05.b"], ps("quase", "i", 62) + [("2.000 vezes", "g", 60, COR)] + ps("mais leve que o próton", "i", 62), XE, 370, passo=0.1)
    nucleo(c, t, C["s05.c"], 1400, 760, 3, 3, 30)
    if t >= C["s05.c"]:
        q = ep(t, C["s05.c"], 0.5)
        c.drawCircle(1400, 760, 200, M.paint(TINTA2, 0.5 * q, stroke=3))
        eletrons_volta(c, t, 1400, 760, 200, 3, q)
    E.frase(c, t, C["s05.c"], ps("átomo neutro:", "i", 64), XE, 620, passo=0.1)
    E.frase(c, t, C["s05.c"] + 0.8, [("elétrons", "g", 60, Q.ELETRON), ("=", "g", 60, TINTA2), ("prótons", "g", 60, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s05.d"], ps("as cargas se cancelam", "i", 60, TINTA2), XE, 860, passo=0.1)


# ---------------- Z e A ----------------
NX, NY, NS = 1250, 560, 250


def b_za(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("número de prótons:", "i", 70), XE, 220, passo=0.12)
        E.frase(c, t, C["s06.a"] + 1.0, [("número atômico,", "g", 80, COR), ("Z", "g", 100, COR)], XE, 360, passo=0.15)
        E.frase(c, t, C["s06.b"], ps("a identidade do elemento", "i", 64, TINTA2), XE, 470, passo=0.1)
        for k, (ck, z, el) in enumerate((("s06.c", "11", "Na"), ("s06.d", "17", "Cl"))):
            y = 640 + k * 160
            E.foco(c, t, C[ck], 0.4, lambda a, y=y, z=z: (particula(c, XE + 40, y - 30, 30, "p", a), E.escreve(c, z + " prótons", XE + 100, y, 70, "g", TINTA, a)))
            E.foco(c, t, C[ck] + 0.5, 0.4, lambda a, y=y: M.arrow(c, XE + 520, y - 22, XE + 640, y - 22, E.COR, a, 5, 18))
            Q.formula_em(c, t, C[ck] + 0.6, el, XE + 680, y + 10, 110)
            E.foco(c, t, C[ck] + 0.8, 0.4, lambda a, y=y, el=el: E.escreve(c, Q.NOMES[el], XE + 870, y, 60, "i", TINTA2, a))
        E.frase(c, t, C["s06.e"], ps("mudou o número de prótons,", "i", 58) + [("mudou o elemento", "g", 56, COR)], XE, 1000, passo=0.1)
        nucleo(c, t, C["s06.c"] + 0.3, 1600, 640, 11, 0, 24) if C["s06.c"] <= t < C["s06.d"] else nucleo(c, t, C["s06.d"] + 0.3, 1600, 640, 17, 0, 22) if t >= C["s06.d"] else None
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("prótons + nêutrons:", "i", 66), XE, 210, passo=0.12)
        E.frase(c, t, C["s07.a"] + 1.0, [("número de massa,", "g", 70, TINTA), ("A", "g", 90, TINTA)], XE, 330, passo=0.15)
        E.frase(c, t, C["s07.b"], ps("os nêutrons, ao contrário:", "i", 62, TINTA2), XE, 470, passo=0.1)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "nêutrons = A − Z", XE + 300, 570, 72, "g", fundo=E.COR, a=a))
        Q.formula_em(c, t, C["s07.d"], "^{23}_{11}Na", NX, NY + 260, 260, cores={"Na": TINTA})
        E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: (M.arrow(c, NX - 150, NY + 80, NX - 20, NY + 80, TINTA, a, 5, 18), E.escreve(c, "A, no alto", 790, NY + 100, 54, "g", TINTA, a)))
        E.foco(c, t, C["s07.d"] + 1.4, 0.4, lambda a: (M.arrow(c, NX - 150, NY + 320, NX - 20, NY + 320, COR, a, 5, 18), E.escreve(c, "Z, embaixo", 790, NY + 340, 54, "g", COR, a)))
        return
    Q.formula_em(c, t, C["s08"], "^{23}_{11}Na", XE, 380, 200)
    E.frase(c, t, C["s08.a"], [("Z = 11", "g", 60, COR), ("A = 23", "g", 60)], XE, 520, passo=0.3)
    contagem(c, t, [(C["s08.b"], "p", "prótons", "11", ""), (C["s08.c"], "n", "nêutrons", "12", "23 − 11 ="), (C["s08.d"], "e", "elétrons", "11", "")], XE, 700)
    nucleo(c, t, C["s08.b"], 1500, 560, 11, 12, 24)
    if t >= C["s08.d"]:
        q = ep(t, C["s08.d"], 0.4)
        c.drawCircle(1500, 560, 300, M.paint(TINTA2, 0.5 * q, stroke=3))
        eletrons_volta(c, t, 1500, 560, 300, 11, q, 14)


# ---------------- íons ----------------
def b_ions(c, t, C, b):
    if t < C["s11"]:
        def s09():
            E.frase(c, t, C["s09.a"], ps("o átomo pode", "i", 70) + [("ganhar", "g", 66, Q.ELETRON)] + ps("ou", "i", 70) + [("perder", "g", 66, COR)] + ps("elétrons", "i", 70), XE, 220, passo=0.12)
            nucleo(c, t, C["s09"], 1450, 620, 6, 6, 26)
            some = (0,) if t >= C["s09.a"] + 1.0 else ()
            if t >= C["s09"]:
                c.drawCircle(1450, 620, 240, M.paint(TINTA2, 0.5, stroke=3))
                eletrons_volta(c, t, 1450, 620, 240, 6, 1, 16, some=some)
                if some:
                    u = ease_out(prog(t, C["s09.a"] + 1.0, 1.0))
                    particula(c, 1450 + 240 + 300 * u, 620 - 200 * u, 16, "e", 1 - ep(t, C["s09.a"] + 1.8, 0.4))
            E.frase(c, t, C["s09.b"], ps("o núcleo", "i", 66) + [("não muda", "g", 62, COR)], XE, 380, passo=0.1)
            E.frase(c, t, C["s09.c"], ps("as cargas não se cancelam", "i", 62), XE, 540, passo=0.1)
            E.frase(c, t, C["s09.d"], [("íon", "g", 150, COR)], XE, 760)
        E.saida(c, t, C["s10"] - 0.1, s09)
        if t < C["s10"]:
            return
        for k, (ck, ck2, perg, nome, cor, sinal) in enumerate((("s10.a", "s10.b", "perdeu elétrons?", "cátion", COR, "+"), ("s10.c", "s10.d", "ganhou elétrons?", "ânion", Q.ELETRON, "−"))):
            x = XE + k * 860
            E.frase(c, t, C[ck], ps(perg, "i", 66), x, 280, passo=0.1)
            E.frase(c, t, C[ck] + 0.8, ps("sobra", "i", 66) + [("positivo" if sinal == "+" else "negativo", "g", 62, cor)], x, 380, passo=0.1)
            E.frase(c, t, C[ck2], [(nome, "g", 120, cor)], x, 560)
        Q.formula_em(c, t, C["s10.e"], "Na^+", 560, 860, 150)
        Q.formula_em(c, t, C["s10.e"] + 0.3, "Cl^-", 1300, 860, 150)
        E.frase(c, t, C["s10.e"] + 0.6, ps("a carga diz quantos elétrons mudaram", "i", 54, TINTA2), W / 2, 1000, "center", 0.08)
        return
    if t < C["s12"]:
        Q.formula_em(c, t, C["s11.a"], "^{23}_{11}Na^+", XE, 380, 200, cores={"carga": E.COR})
        E.frase(c, t, C["s11.a"] + 0.8, ps("perdeu um elétron", "i", 60, TINTA2), XE + 660, 400, passo=0.1)
        contagem(c, t, [(C["s11.b"], "p", "prótons", "11", ""), (C["s11.c"], "n", "nêutrons", "12", ""), (C["s11.d"], "e", "elétrons", "10", "11 − 1 =")], XE, 600)
        nucleo(c, t, C["s11.b"], 1500, 560, 11, 12, 22)
        if t >= C["s11.b"]:
            c.drawCircle(1500, 560, 300, M.paint(TINTA2, 0.5, stroke=3))
            eletrons_volta(c, t, 1500, 560, 300, 11, 1, 14, some=(0,) if t >= C["s11.d"] else ())
        return
    Q.formula_em(c, t, C["s12.a"], "^{35}_{17}Cl^-", XE, 380, 200, cores={"carga": Q.ELETRON})
    E.frase(c, t, C["s12.a"] + 1.4, ps("Z do cloro: 17", "i", 60, TINTA2), XE + 520, 300, passo=0.1)
    contagem(c, t, [(C["s12.b"], "p", "prótons", "17", ""), (C["s12.c"], "n", "nêutrons", "18", "35 − 17 ="), (C["s12.d"], "e", "elétrons", "18", "17 + 1 =")], XE, 600)
    nucleo(c, t, C["s12.b"], 1500, 560, 17, 18, 20)
    if t >= C["s12.b"]:
        c.drawCircle(1500, 560, 300, M.paint(TINTA2, 0.5, stroke=3))
        eletrons_volta(c, t, 1500, 560, 300, 18 if t >= C["s12.d"] else 17, 1, 13)


# ---------------- isótopos ----------------
def b_isotopos(c, t, C, b):
    E.frase(c, t, C["s13.a"], ps("mesmo elemento, nêutrons diferentes:", "i", 62), XE, 190, passo=0.1)
    E.frase(c, t, C["s13.b"], [("isótopos", "g", 90, COR)], XE, 320)
    E.frase(c, t, C["s13.c"], [("mesmo Z,", "g", 56, COR)] + ps("número de massa diferente", "i", 58), XE + 470, 310, passo=0.1)
    for k, A in enumerate((12, 13, 14)):
        x = 400 + k * 560
        Q.formula_em(c, t, C["s13.d"] + 0.4 * k, "^{%d}_{6}C" % A, x - 110, 560, 150)
        nucleo(c, t, C["s13.d"] + 0.4 * k + 0.2, x, 760, 6, A - 6, 22)
        E.foco(c, t, C["s13.e"], 0.4, lambda a, x=x: (particula(c, x - 150, 940, 22, "p", a), E.escreve(c, "6", x - 115, 962, 60, "g", COR, a)))
        E.foco(c, t, C["s13.f"] + 0.3 * k, 0.4, lambda a, x=x, A=A: (particula(c, x + 40, 940, 22, "n", a), E.escreve(c, str(A - 6), x + 75, 962, 60, "g", TINTA, a)))
    if t >= C["s14"]:
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.pilula(c, "o mesmo elemento", 1500, 200, 54, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "muda só o número de nêutrons", 1450, 1040, 44, "b", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    Q.formula_em(c, t, C["s15.a"], "Na^+", XE, 450, 200, cores={"carga": E.COR})
    E.frase(c, t, C["s15.a"] + 0.4, ps("sinal de mais =", "i", 64) + [("ganhou elétron?", "g", 60, ERRADO)], XE + 520, 400, passo=0.1)
    if t >= C["s15.b"]:
        E.risco(c, XE + 900, 420, XE + 1380, 350, t, C["s15.b"], largura=12)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (particula(c, XE + 60, 640, 40, "e", a), E.escreve(c, "o elétron é negativo", XE + 130, 662, 66, "i", TINTA, a)))
    E.frase(c, t, C["s15.d"], [("perder", "g", 66, COR)] + ps("elétron deixa o saldo", "i", 66) + [("positivo", "g", 66, COR)], XE, 820, passo=0.1)
    E.foco(c, t, C["s15.d"] + 1.0, 0.4, lambda a: E.formula(c, "11 prótons − 10 elétrons = +1", XE, 950, 64, "g", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("o atalho para os elétrons", "i", 70, CLARO), W / 2, 170, "center", 0.12)
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.pilula(c, "elétrons = Z − carga", W / 2, 330, 90, "g", fundo=E.COR, a=a))
        Q.formula_em(c, t, C["s16.b"], "Na^+", 420, 600, 140, escuro=True)
        E.formula_em(c, t, C["s16.b"] + 0.6, "11 − 1 = 10", 720, 600, 100, "g", BR)
        Q.formula_em(c, t, C["s16.c"], "Cl^-", 420, 840, 140, escuro=True)
        E.formula_em(c, t, C["s16.c"] + 0.8, "17 − (−1) = 18", 720, 840, 100, "g", BR)
        E.foco(c, t, C["s16.c"] + 2.4, 0.4, lambda a: E.pilula(c, "menos com menos: soma", 1520, 950, 44, "b", fundo="#22232B", a=a))
        return
    E.frase(c, t, C["s17.a"], [("+1", "g", 70, E.CLARO)] + ps("= um elétron que", "i", 70, CLARO) + [("falta", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s17.b"], [("−1", "g", 70, "#8FB8FF")] + ps("= um elétron que", "i", 70, CLARO) + [("sobra", "g", 66, BR)], W / 2, 440, "center", 0.12)
    E.frase(c, t, C["s17.c"], [("não", "g", 64, ERRADO), ("compensa:", "i", 68, CLARO)] + ps("se perde no sinal?", "i", 68, CLARO), W / 2, 640, "center", 0.12)
    E.frase(c, t, C["s17.d"], ps("pense em", "i", 66, CLARO) + [("perdeu", "g", 62, BR)] + ps("ou", "i", 66, CLARO) + [("ganhou", "g", 62, BR)], W / 2, 780, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    Q.formula_em(c, t, C["s18.a"], "^{27}_{13}Al^{3+}", XE, 430, 190)
    E.frase(c, t, C["s18.a"] + 0.4, ps("alumínio: Z 13, A 27", "i", 54, TINTA2), XE + 560, 360, passo=0.08)
    E.frase(c, t, C["s18.b"], [("1", "g", 56, COR)] + ps("prótons, nêutrons e elétrons do íon?", "i", 60), XE, 620, passo=0.08)
    E.frase(c, t, C["s18.c"], [("2", "g", 56, COR)] + ps("um átomo de Z 14 e A 27", "i", 60), XE, 740, passo=0.08)
    E.frase(c, t, C["s18.c"] + 1.8, ps("é isótopo do alumínio?", "i", 60), XE + 50, 830, passo=0.08)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s21"]:
        Q.formula_em(c, t, C["s20"], "^{27}_{13}Al^{3+}", XE, 330, 170, cores={"carga": E.COR})
        contagem(c, t, [(C["s20.a"], "p", "prótons", "13", ""), (C["s20.b"], "n", "nêutrons", "14", "27 − 13 ="), (C["s20.c"], "e", "elétrons", "10", "13 − 3 =")], XE, 540)
        nucleo(c, t, C["s20.a"], 1520, 480, 13, 14, 22)
        if t >= C["s20.d"]:
            E.foco(c, t, C["s20.d"] + 0.2, 0.4, lambda a: E.selo(c, XE + 900, 740, 40, True, a))

        def erro():
            E.foco(c, t, C["s20.e"], 0.4, lambda a: E.formula(c, "13 + 3 = 16 ?", XE, 960, 64, "g", ERRADO, a))
            E.foco(c, t, C["s20.e"] + 0.4, 0.4, lambda a: E.escreve(c, "somou a carga: o erro do sinal de mais", XE + 470, 955, 50, "i", ERRADO, a))
            if t >= C["s20.e"] + 0.8:
                E.risco(c, XE - 10, 975, XE + 400, 915, t, C["s20.e"] + 0.8, largura=9)
        if t >= C["s20.e"]:
            erro()
        return
    E.frase(c, t, C["s21.a"], ps("e o átomo de", "i", 66) + [("Z 14", "g", 62, COR)] + ps("?", "i", 66), XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s21.a"] + 0.4, "^{27}_{13}Al", 420, 560, 180)
    Q.formula_em(c, t, C["s21.a"] + 0.8, "^{27}_{14}X", 1080, 560, 180)
    E.frase(c, t, C["s21.b"], [("mesmo A,", "g", 60), ("outro Z", "g", 60, ERRADO)], XE, 780, passo=0.15)
    E.frase(c, t, C["s21.c"], ps("outro número de prótons:", "i", 60) + [("outro elemento", "g", 58)], XE, 880, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "não é isótopo", 1500, 860, 60, "g", fundo=ERRADO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s22.a", "Z = prótons"), ("s22.b", "nêutrons = A − Z"), ("s22.c", "elétrons = Z − carga"), ("s22.d", "isótopos: mesmo Z"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.foco(c, t, C[k] + 0.1, 0.4, lambda a, y=y, s=s: E.formula(c, s, XE + 110, y, 70, "g", TINTA, a))
        Q.formula_em(c, t, C["s22.a"] + 0.5, "^{23}_{11}Na^+", 1300, 640, 220)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], ps("os 26 elétrons do", "i", 70) + [("ferro", "g", 70, COR)], XE, 390, passo=0.12)
    E.frase(c, t, C["s23.b"], [("diagrama de Pauling", "g", 70)], XE, 510)
    Q.pauling(c, t, C["s23.b"] + 0.3, XE + 40, 590, 46, setas=True)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, particulas=b_particulas, za=b_za, ions=b_ions, isotopos=b_isotopos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
