"""Visual — Estudativo · QUI-CAL-001: massa atômica e massa molecular. Primeira aula do módulo Cálculos Químicos.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho da QUI-MIS-001 (fórmula sempre em Q.formula, átomo na cor CPK, palco só no
atalho, erro com risco/selo). Acrescenta a LINGUAGEM DA TRILHA "MOL, ESTEQUIOMETRIA E GASES" (vale de QUI-CAL-001 a 009):
- CASA DA TABELA (casa): quadrado branco com borda turquesa, Z pequeno no canto, símbolo grande, nome em itálico e a MASSA
  ATÔMICA embaixo, em COR_TEXTO. É de onde sai todo número de massa: mostre a casa na primeira vez que a massa aparece.
- LINHA DE MASSA (conta): bolinha do elemento + "6 × 12 =" em tinta + parcial na cor da matéria; as linhas se empilham e a
  soma fica embaixo de um traço; o total vai na esfera turquesa (bola_txt). Unidade (u, g, g/mol, mol) sempre escrita.
- MOL = pacote: a ponte do mol (QUI-CAL-002) liga gramas ← → mol ← → moléculas; o mol fica no meio, na esfera turquesa.
- EQUAÇÃO com linhas embaixo (Q.sob_termos): mols na 1ª linha, massas (coef × M) na 2ª, dado/xis em cima, em COR.
- Resultado certo da questão = esfera verde (CERTO); leitura errada = vermelho + risco.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar.
Peça candidata ao kit quimica.py: casa() (casa da tabela com a massa) e conta() (linha n × massa = parcial)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-001_massa_atomica_molecular.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("unidade", "tabela", "molecular", "atalho", "questao", "fim"))
BR = "#FFFFFF"

MA = {"H": 1, "C": 12, "N": 14, "O": 16, "Cl": 35.5}


def massa(f):
    return sum(MA[el] * n for el, n in Q.contar(f).items())


# todas as contas da aula
assert massa("H2O") == 18 and massa("CO2") == 44 and massa("Cl2") == 71
assert Q.contar("C6H12O6") == {"C": 6, "H": 12, "O": 6} and massa("C6H12O6") == 180 == 72 + 12 + 96
assert massa("CH2O") == 30 and 30 * 6 == 180 and 12 + 1 + 16 == 29
assert massa("C2H6O") == 46 == 24 + 6 + 16
assert (3 * 35 + 37) / 4 == 35.5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    tinta = E.SOBRE if cor is None else BR
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def conta(c, t, t0, el, txt, res, x, y, size=72, tr=None, cor_res=None, escuro=False):
    """linha de massa: bolinha do elemento + "6 × 12 =" + parcial na cor da matéria (tr = instante do parcial)"""
    r = size * 0.42
    if el:
        Q.atomo_em(c, t, t0, x + r, y - size * 0.34, r, el, escuro=escuro)
        x += 2 * r + size * 0.4
    E.formula_em(c, t, t0 + 0.1, txt, x, y, size, "g", BR if escuro else TINTA)
    w = E.formula(None, txt, 0, 0, size, a=0)
    if res:
        E.formula_em(c, t, tr if tr is not None else t0 + 0.6, res, x + w + size * 0.3, y, size, "g", cor_res or (E.CLARO if escuro else COR))
    return x + w


def casa(c, cx, cy, s, el, z, m, a=1.0, cor_m=None):
    """casa do elemento na tabela periódica: Z no canto, símbolo, nome e a massa atômica embaixo"""
    if a <= 0:
        return
    w, h = s, s * 1.15
    x, y = cx - w / 2, cy - h / 2
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), s * 0.08, s * 0.08)
    c.drawRRect(rr, M.paint("#FFFFFF", a))
    c.drawRRect(rr, M.paint(E.COR, a, stroke=max(3, s * 0.025)))
    E.escreve(c, str(z), x + s * 0.09, y + s * 0.19, s * 0.14, "b", TINTA2, a)
    centro(c, el, cx, cy + s * 0.1, s * 0.42, "g", TINTA, a)
    centro(c, Q.NOMES[el], cx, cy + s * 0.28, s * 0.12, "i", TINTA2, a)
    centro(c, m, cx, cy + s * 0.5, s * 0.17, "g", cor_m or COR, a)


def casa_em(c, t, t0, cx, cy, s, el, z, m, cor_m=None):
    E.foco(c, t, t0, 0.5, lambda a: casa(c, cx, cy, s, el, z, m, a, cor_m))


def soma_vertical(c, t, tl, nums, tot, xd, y0, size, tt, cor_tot=None):
    """conta armada de somar, alinhada à direita em xd; tt = instante do traço e do total"""
    dy = size * 1.15
    for i, (n, ti) in enumerate(zip(nums, tl)):
        E.foco(c, t, ti, 0.4, lambda a, n=n, i=i: E.formula(c, n, xd, y0 + i * dy, size, "g", TINTA, a, "right"))
    E.foco(c, t, tl[1] if len(tl) > 1 else tl[0], 0.4, lambda a: E.formula(c, "+", xd - size * 2.6, y0 + dy * (len(nums) - 1), size, "g", TINTA2, a))
    p = ep(t, tt, 0.4)
    yl = y0 + (len(nums) - 1) * dy + size * 0.35
    if p > 0:
        M.line(c, xd - size * 2.8, yl, xd + size * 0.2, yl, TINTA, p, 5, progress=ease_out(prog(t, tt, 0.4)))
    return yl


def chip(c, s, cx, cy, size, fundo=None, a=1.0, escuro=True):
    """fórmula química dentro de uma pílula do tamanho dela"""
    if a <= 0:
        return
    w = Q.formula(None, s, 0, 0, size) + size * 0.9
    M.rrect(c, cx - w / 2, cy - size * 0.8, w, size * 1.6, size * 0.8, fundo or E.COR, a)
    Q.formula(c, s, cx, cy + size * 0.36, size, BR, a, "center", escuro=escuro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.formula_em(c, t, C["s01.a"], "C6H12O6", XE, 470, 230, cores={"indice": E.COR} if t >= C["s01.d"] else None)
        E.frase(c, t, C["s01.a"] + 1.2, ps("a glicose, o açúcar do sangue", "i", 64, TINTA2), XE, 590, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("massa", "i", 80), 1280, 300)
        E.foco(c, t, C["s01.b"] + 0.4, 0.5, lambda a: E.escreve(c, "180", 1270, 560, 260, "g", COR, a))
        pilula_em(c, t, C["s01.c"], "180 o quê?", 1500, 700, 60, TINTA)
        if t >= C["s01.d"]:
            E.frase(c, t, C["s01.d"], ps("e como chegar nele em", "i", 70) + [("segundos?", "g", 66, COR)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("massa", "g", 70), ("atômica", "g", 70, COR)]),
                 (C["s02.c"], [("massa", "g", 70), ("de", "i", 74), ("qualquer", "i", 74), ("molécula", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("três coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [400, 640, 880]
    for i, k in enumerate(("s03.b", "s03.c", "s03.d")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    # 1: o índice
    E.frase(c, t, C["s03.b"] + 0.1, ps("ler o índice", "i", 70), XE + 110, y[0])
    Q.formula_em(c, t, C["s03.b"] + 0.5, "H2O", XE + 560, y[0] + 10, 120, cores={"indice": E.COR})
    E.frase(c, t, C["s03.b"] + 1.4, [("2", "g", 60, COR), ("H,", "g", 60), ("1", "g", 60, COR), ("O", "g", 60)], XE + 860, y[0], passo=0.15)
    # 2: a tabela
    E.frase(c, t, C["s03.c"] + 0.1, ps("achar o elemento na tabela", "i", 70), XE + 110, y[1])
    Q.tabela(c, t, C["s03.c"] + 0.4, 1150, 500, 30, numeros=False, destaque=("O",), d=0.9)
    # 3: decimais
    E.frase(c, t, C["s03.d"] + 0.1, ps("multiplicar decimais", "i", 70), XE + 110, y[2])
    E.formula_em(c, t, C["s03.d"] + 0.8, "2 × 35,5 = 71", XE + 760, y[2] + 4, 76, "g", TINTA)


# ---------------- a unidade u ----------------
def nucleo(c, t, t0, cx, cy, r, um=None):
    """núcleo do carbono 12: 6 prótons (turquesa) e 6 nêutrons (cinza) que pulam; um = instante em que um deles se destaca"""
    pts = []
    for k in range(12):
        ang = k * 2.4
        rr = r * 0.62 * math.sqrt((k + 0.5) / 12)
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    for k, (x, y) in enumerate(pts):
        q = ease_back(prog(t, t0 + 0.06 * k, 0.4))
        if q > 0:
            E.bola(c, x, y, r * 0.24 * q, E.COR if k % 2 == 0 else Q.NEUTRON)
    if um is not None and t >= um:
        x, y = pts[0]
        q = ep(t, um, 0.4)
        c.drawCircle(x, y, r * 0.32, M.paint(TINTA, q, stroke=5))
    return pts


def b_unidade(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("leve demais para a balança", "i", 76), XE, 200, passo=0.12)
            E.frase(c, t, C["s04.a"], ps("um átomo de hidrogênio, em gramas:", "i", 60, TINTA2), XE, 330, passo=0.1)
            E.foco(c, t, C["s04.a"] + 0.8, 0.6, lambda a: E.escreve(c, "0," + "0" * 23 + "167 g", XE, 450, 58, "g", TINTA, a))
            p = ep(t, C["s04.a"] + 2.0, 0.5)
            if p > 0:
                x0 = XE + E.larg("0,", "g", 58)
                E.chave(c, x0, x0 + E.larg("0" * 23, "g", 58), 480, E.COR, p, 24)
            pilula_em(c, t, C["s04.a"] + 2.3, "23 zeros", XE + 520, 560, 46, E.COR)
        E.saida(c, t, C["s04.b"] - 0.1, s04)
        if t < C["s04.b"]:
            return
        E.frase(c, t, C["s04.b"], ps("uma régua própria:", "i", 76), XE, 230, passo=0.12)
        E.frase(c, t, C["s04.b"] + 1.0, ps("unidade de massa atômica", "i", 64, TINTA2), XE, 330, passo=0.1)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.escreve(c, "u", XE, 640, 300, "g", COR, a))
        # o carbono 12 dividido em doze
        nucleo(c, t, C["s04.d"], 1380, 560, 300, um=C["s04.d"] + 2.0)
        E.foco(c, t, C["s04.d"] + 0.6, 0.4, lambda a: centro(c, "carbono 12: 6 prótons + 6 nêutrons", 1380, 960, 44, "i", TINTA2, a))
        E.foco(c, t, C["s04.d"] + 1.6, 0.5, lambda a: (E.formula(c, "1 u =", XE + 300, 600, 80, "g", TINTA, a),
                                                      E.fracao(c, "1", "12", XE + 590, 572, 70, COR, a)))
        E.foco(c, t, C["s04.d"] + 2.2, 0.4, lambda a: E.escreve(c, "do carbono 12", XE + 300, 720, 58, "i", TINTA2, a))
        return
    # s05: próton e nêutron ≈ 1 u
    E.frase(c, t, C["s05.a"], ps("cada próton e cada nêutron", "i", 70), XE, 200, passo=0.12)
    E.foco(c, t, C["s05.a"] + 0.6, 0.4, lambda a: (E.bola(c, XE + 50, 300, 34, E.COR, a), E.bola(c, XE + 140, 300, 34, Q.NEUTRON, a),
                                                  E.formula(c, "≈ 1 u", XE + 210, 322, 70, "g", COR, a)))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (E.bola(c, XE + 700, 300, 14, Q.ELETRON, a), E.escreve(c, "elétron", XE + 740, 320, 60, "i", TINTA2, a), E.formula(c, "≈ 0", XE + 940, 320, 60, "g", TINTA2, a)))
    # hidrogênio e oxigênio
    for k, (el, z, n, m, tk) in enumerate((("H", 1, 0, "≈ 1 u", "s05.c"), ("O", 8, 8, "≈ 16 u", "s05.d"))):
        x = 560 + 820 * k
        Q.atomo_em(c, t, C[tk], x, 620, 110 if el == "O" else 80, el)
        E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, z=z, n=n, x=x: centro(c, f"{z} próton{'s' if z > 1 else ''}" + (f" + {n} nêutrons" if n else ""), x, 820, 50, "i", TINTA2, a))
        E.foco(c, t, C[tk] + 0.8, 0.5, lambda a, m=m, x=x: centro(c, m, x, 950, 100, "g", COR, a))


# ---------------- a massa na tabela ----------------
def b_tabela(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("a massa atômica vem na", "i", 70), XE, 200, passo=0.12)
        E.frase(c, t, C["s06.a"] + 1.1, [("casa do elemento", "g", 66, COR)], XE + 760, 200)
        Q.tabela(c, t, C["s06.a"] + 0.2, 1080, 330, 40, numeros=False, destaque=("C", "Cl"), d=0.9)
        casa_em(c, t, C["s06.b"], 400, 640, 300, "C", 6, "12")
        casa_em(c, t, C["s06.c"], 800, 640, 300, "Cl", 17, "35,5")
        if t >= C["s06.c"] + 0.5:
            q = ep(t, C["s06.c"] + 0.5, 0.4)
            c.drawCircle(800, 640 + 300 * 0.45, 96, M.paint(E.COR, q, stroke=6))
        return
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], [("por que", "i", 80), ("meio?", "g", 76, COR)], XE, 200, passo=0.12)
            E.frase(c, t, C["s07.a"], ps("o cloro é uma mistura de", "i", 64) + [("isótopos", "g", 60, COR)], XE, 310, passo=0.1)
            for k in range(4):
                x = 360 + k * 260
                tk = C["s07.b"] + 0.2 * k if k < 3 else C["s07.c"]
                Q.atomo_em(c, t, tk, x, 540, 78 if k < 3 else 86, "Cl")
                E.foco(c, t, tk + 0.3, 0.4, lambda a, k=k, x=x: centro(c, "35" if k < 3 else "37", x, 700, 72, "g", TINTA if k < 3 else COR, a))
            E.foco(c, t, C["s07.b"] + 1.2, 0.4, lambda a: centro(c, "3 em cada 4", 620, 790, 50, "i", TINTA2, a))
            E.foco(c, t, C["s07.c"] + 0.8, 0.4, lambda a: centro(c, "1 em cada 4", 1140, 790, 50, "i", TINTA2, a))
            # a reta de 35 a 37, com o 35,5 puxado para o 35
            x0, x1, yr = 1350, 1780, 560
            p = ep(t, C["s07.d"], 0.5)
            if p > 0:
                M.line(c, x0, yr, x1, yr, TINTA, p, 5, progress=ease_out(prog(t, C["s07.d"], 0.5)))
                for v, xx in ((35, x0), (36, (x0 + x1) / 2), (37, x1)):
                    M.line(c, xx, yr - 18, xx, yr + 18, TINTA, p, 4)
                    centro(c, str(v), xx, yr + 70, 46, "b", TINTA2, p)
            xm = lerp(x0, x1, 0.25)
            q = ease_back(prog(t, C["s07.d"] + 0.8, 0.5))
            if q > 0:
                E.bola(c, xm, yr, 22 * q)
                pilula_em(c, t, C["s07.d"] + 1.0, "35,5", xm, yr - 90, 54, E.COR)
            E.foco(c, t, C["s07.d"] + 1.6, 0.4, lambda a: centro(c, "mais perto do 35: a maioria", 1565, 720, 44, "i", TINTA2, a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    # s08: os valores da prova
    E.frase(c, t, C["s08.a"], ps("na prova, os valores vêm", "i", 76), XE, 230, passo=0.12)
    E.frase(c, t, C["s08.a"] + 1.4, [("no enunciado", "g", 72, COR)], XE + 920, 230)
    for k, (el, z, m, tk) in enumerate((("H", 1, "1", "s08.b"), ("C", 6, "12", "s08.c"), ("O", 8, "16", "s08.d"))):
        casa_em(c, t, C[tk], 560 + k * 400, 640, 300, el, z, m)


# ---------------- massa molecular ----------------
def b_molecular(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("massa molecular", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("soma de todos os átomos", "i", 72), XE, 190, passo=0.12)
        Q.formula_em(c, t, C["s09.b"], "H2O", XE, 400, 170, cores={"indice": E.COR})
        Q.molecula(c, t, C["s09.b"] + 0.3, "H2O", 1460, 470, 170, passo=0.15)
        conta(c, t, C["s09.c"], "H", "2 × 1 =", "2", XE, 600, 76)
        conta(c, t, C["s09.d"], "O", "", "16", XE, 730, 76, tr=C["s09.d"])
        p = ep(t, C["s09.e"], 0.4)
        if p > 0:
            M.line(c, XE, 790, XE + 560, 790, TINTA, p, 5, progress=ease_out(prog(t, C["s09.e"], 0.4)))
        E.formula_em(c, t, C["s09.e"] + 0.2, "2 + 16 =", XE, 900, 76, "g", TINTA2)
        bola_txt(c, t, C["s09.e"] + 0.7, "18 u", XE + 520, 875, 92, 62)
        return

    def co2():
        E.frase(c, t, C["s10.a"], [("o índice", "g", 70, COR)] + ps("manda multiplicar", "i", 76), XE, 190, passo=0.12)
        Q.formula_em(c, t, C["s10.b"], "CO2", XE, 400, 170, cores={"indice": E.COR})
        Q.molecula(c, t, C["s10.b"] + 0.3, "CO2", 1460, 420, 150, passo=0.15)
        conta(c, t, C["s10.c"], "C", "", "12", XE, 600, 76, tr=C["s10.c"])
        conta(c, t, C["s10.d"], "O", "2 × 16 =", "32", XE, 730, 76)
        p = ep(t, C["s10.e"], 0.4)
        if p > 0:
            M.line(c, XE, 790, XE + 560, 790, TINTA, p, 5, progress=ease_out(prog(t, C["s10.e"], 0.4)))
        E.formula_em(c, t, C["s10.e"] + 0.2, "12 + 32 =", XE, 900, 76, "g", TINTA2)
        bola_txt(c, t, C["s10.e"] + 0.7, "44 u", XE + 560, 875, 92, 62)
    E.saida(c, t, C["s10.f"] - 0.1, co2)
    if t < C["s10.f"]:
        return
    E.frase(c, t, C["s10.f"], ps("com decimal é igual", "i", 80), XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s10.f"] + 0.6, "Cl2", XE, 480, 200, cores={"indice": E.COR})
    Q.molecula(c, t, C["s10.f"] + 0.8, "Cl2", 1420, 440, 170, passo=0.2)
    E.foco(c, t, C["s10.f"] + 0.8, 0.4, lambda a: E.escreve(c, "o gás cloro", XE + 10, 580, 56, "i", TINTA2, a))
    conta(c, t, C["s10.f"] + 1.6, "Cl", "2 × 35,5 =", "", XE, 800, 84)
    bola_txt(c, t, C["s10.f"] + 2.8, "71 u", XE + 840, 772, 100, 66)


# ---------------- glicose ----------------
def b_glicose(c, t, C, b):
    cores = None
    for k, el in (("s11.c", "C"), ("s11.d", "H"), ("s11.e", "O")):
        if C[k] <= t < C[k] + 2.2:
            cores = {el: E.COR}
    if t >= C["s12"]:
        cores = {"indice": E.COR}
    Q.formula_em(c, t, C["s11.a"], "C6H12O6", XE, 270, 170, cores=cores)
    E.frase(c, t, C["s11.b"], ps("quantos átomos × massa de um", "i", 56, TINTA2), XE, 380, passo=0.1)
    ys = [520, 650, 780]
    for (k, el, txt, res), y in zip((("s11.c", "C", "6 × 12 =", "72"), ("s11.d", "H", "12 × 1 =", "12"), ("s11.e", "O", "6 × 16 =", "96")), ys):
        conta(c, t, C[k], el, txt, res, XE, y, 78, tr=C[k] + 1.2)
    # a soma armada à direita
    yt = soma_vertical(c, t, [C["s12.a"], C["s12.a"] + 0.4, C["s12.a"] + 0.8], ["72", "12", "96"], "180", 1560, 470, 96, C["s12.a"] + 1.4)
    bola_txt(c, t, C["s12.b"], "180 u", 1460, yt + 150, 120, 76)
    pilula_em(c, t, C["s12.c"], "o 180 do começo", 1050, yt + 150, 46, TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("esquecer o índice", "i", 72), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s13.a"] + 0.4, "C6H12O6", XE, 420, 170, cores={"indice": E.COR} if t >= C["s13.d"] else None)

    def errado():
        E.formula_em(c, t, C["s13.b"], "12 + 1 + 16 = 29", XE, 640, 96, "g", ERRADO)
        if t >= C["s13.b"] + 1.4:
            E.risco(c, XE - 20, 660, XE + 840, 570, t, C["s13.b"] + 1.4, largura=12)
        for k, el in enumerate(("C", "H", "O")):
            Q.atomo_em(c, t, C["s13.c"] + 0.2 * k, 1240 + 170 * k, 600, 62 if el != "H" else 48, el)
        E.foco(c, t, C["s13.c"] + 0.7, 0.4, lambda a: centro(c, "um de cada: não é a glicose", 1410, 740, 48, "i", ERRADO, a))
    E.saida(c, t, C["s13.d"] - 0.1, errado)
    if t >= C["s13.d"]:
        G = Q.grupos("C6H12O6", XE, 420, 170)
        for g in G:
            q = ep(t, C["s13.d"] + 0.2 * g["i"], 0.4)
            if q > 0:
                E.caixa_pontilhada(c, g["x0"] - 10, g["topo"] - 10, g["x1"] - g["x0"] + 20, g["base"] - g["topo"] + 20, q, E.COR, prog_=q)
        E.frase(c, t, C["s13.d"] + 0.6, ps("cada índice", "i", 76) + [("multiplica", "g", 70, COR)] + ps("a massa do seu elemento", "i", 76), XE, 700, passo=0.12)
        E.foco(c, t, C["s13.d"] + 1.6, 0.5, lambda a: E.formula(c, "6 × 12   12 × 1   6 × 16", XE, 860, 76, "g", TINTA2, a))
        E.foco(c, t, C["s13.d"] + 2.0, 0.4, lambda a: E.selo(c, XE + 1180, 834, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        Q.formula_em(c, t, C["s14.a"], "C6H12O6", W / 2, 470, 210, align="center", cores={"indice": E.CLARO}, escuro=True)
        G = [g for g in Q.grupos("C6H12O6", W / 2, 470, 210, "center") if g["tipo"] == "el"]
        for k, g in enumerate(G):
            pilula_em(c, t, C["s14.b"] + 0.3 * k, "÷ 6", g["x1"] - 30, 590, 44, E.COR)
        E.frase(c, t, C["s14.c"], ps("a glicose é", "i", 70, CLARO), W / 2 - 520, 830, "left", 0.12)
        E.formula_em(c, t, C["s14.c"] + 0.6, "6 ×", W / 2 - 80, 840, 110, "g", E.CLARO)
        Q.formula_em(c, t, C["s14.c"] + 0.8, "CH2O", W / 2 + 130, 840, 110, escuro=True)
        return

    def s15a():
        Q.formula_em(c, t, C["s15"], "CH2O", XE, 300, 150, escuro=True, cores={"indice": E.CLARO})
        E.formula_em(c, t, C["s15.a"] + 0.4, "12 + 2 + 16 = 30", XE + 470, 290, 80, "g", BR)
        E.formula_em(c, t, C["s15.b"], "30 × 6 =", XE + 470, 440, 80, "g", BR)
        bola_txt(c, t, C["s15.b"] + 0.6, "180 u", XE + 1040, 412, 92, 62)
        # as seis cópias do pedaço
        for k in range(6):
            x = XE + 90 + k * 270
            E.foco(c, t, C["s15.c"] + 0.15 * k, 0.4, lambda a, x=x: chip(c, "CH2O", x, 640, 56, "#24303A", a))
        E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: centro(c, "seis cópias do mesmo pedaço", W / 2, 760, 50, "i", E.CLARO, a))
    E.saida(c, t, C["s15.d"] - 0.1, s15a)
    if t < C["s15.d"]:
        return
    E.frase(c, t, C["s15.d"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("nada divide todos os índices", "i", 70, CLARO), W / 2, 300, "center", 0.12)
    Q.formula_em(c, t, C["s15.d"] + 1.0, "C2H6O", W / 2, 560, 180, align="center", escuro=True, cores={"indice": E.CLARO})
    E.foco(c, t, C["s15.d"] + 1.8, 0.4, lambda a: centro(c, "2, 6 e 1: faça a linha de cada elemento", W / 2, 700, 52, "i", E.CLARO, a))
    pilula_em(c, t, C["s15.e"], "o nome do pedaço: outra aula", W / 2, 860, 48, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16"] + 1.0, ps("o etanol, o álcool do posto", "i", 62, TINTA2), XE, 290, passo=0.1)
    Q.formula_em(c, t, C["s16.a"], "C2H6O", XE, 480, 170)
    for k, (el, z, m) in enumerate((("C", 6, "12"), ("H", 1, "1"), ("O", 8, "16"))):
        casa_em(c, t, C["s16.b"] + 0.3 * k, XE + 100 + k * 230, 690, 180, el, z, m)
    E.frase(c, t, C["s16.c"], ps("qual é a", "i", 64) + [("massa molecular?", "g", 60, COR)], XE, 920, passo=0.1)
    if t < C["s17"]:
        Q.molecula(c, t, C["s16.a"] + 0.4, "C2H6O", 1450, 520, 150, passo=0.12)
    else:
        E.relogio(c, t, C["s17.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cores = {"C": E.COR} if C["s18.a"] <= t < C["s18.b"] else {"H": E.COR} if C["s18.b"] <= t < C["s18.c"] else {"O": E.COR} if C["s18.c"] <= t < C["s18.d"] else None
    Q.formula_em(c, t, C["s18"], "C2H6O", XE, 260, 160, cores=cores)
    ys = [450, 580, 710]
    for (k, el, txt, res), y in zip((("s18.a", "C", "2 × 12 =", "24"), ("s18.b", "H", "6 × 1 =", "6"), ("s18.c", "O", "", "16")), ys):
        conta(c, t, C[k], el, txt, res, XE, y, 76, tr=C[k] + (1.0 if txt else 0.3))
    yt = soma_vertical(c, t, [C["s18.d"], C["s18.d"] + 0.4, C["s18.d"] + 0.8], ["24", "6", "16"], "46", 1500, 430, 92, C["s18.d"] + 1.3)
    bola_txt(c, t, C["s18.e"], "46 u", 1410, yt + 140, 110, 72, CERTO)

    def erro():
        E.foco(c, t, C["s18.f"], 0.5, lambda a: (E.formula(c, "12 + 1 + 16 = 29", XE, 920, 66, "g", ERRADO, a),
                                                 E.escreve(c, "sem os índices", XE + 620, 915, 52, "i", ERRADO, a)))
        if t >= C["s18.f"] + 0.7:
            E.risco(c, XE - 10, 935, XE + 560, 870, t, C["s18.f"] + 0.7, largura=9)
    if t >= C["s18.f"]:
        erro()


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s19.a", [("massa atômica", "g", 66), ("=", "g", 66, TINTA2)] + ps("na tabela, em u", "i", 70)),
                 ("s19.b", [("massa molecular", "g", 66), ("=", "g", 66, TINTA2)] + ps("soma de todos os átomos", "i", 70)),
                 ("s19.c", [("índice", "g", 66), ("=", "g", 66, TINTA2)] + ps("multiplica a massa", "i", 70)))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.foco(c, t, C["s20"] + 0.8, 0.5, lambda a: E.formula(c, "18 u", XE, 470, 130, "g", TINTA, a))
    E.foco(c, t, C["s20.a"], 0.5, lambda a: (E.formula(c, "→", XE + 360, 470, 130, "g", TINTA2, a), E.formula(c, "18 g", XE + 560, 470, 130, "g", COR, a)))
    E.frase(c, t, C["s20.b"], [("o", "i", 110), ("mol", "g", 120, COR)], XE, 680)
    E.frase(c, t, C["s20.b"] + 0.8, ps("a dúzia da Química", "i", 70, TINTA2), XE, 800, passo=0.1)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, unidade=b_unidade, tabela=b_tabela, molecular=b_molecular, glicose=b_glicose,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
