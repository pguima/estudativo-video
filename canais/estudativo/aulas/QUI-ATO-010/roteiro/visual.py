"""Visual — Estudativo · QUI-ATO-010: raio atômico.
Segue a linguagem visual da Química (QUI-MIS-001), a da trilha (QUI-ATO-001) e a do módulo Tabela periódica (QUI-ATO-008).
Nesta aula: TAMANHO DO ÁTOMO = esfera turquesa clara com o símbolo, em escala com o raio de verdade (raios em pm, de tabela);
a seta do raio é âmbar (cresce para baixo e para a esquerda). Íon ao lado do átomo, com a mesma escala.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-010_raio_atomico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("raio", "familia", "periodo", "ion", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#F2A33A"
ESFERA = E.mix(E.COR, "#FFFFFF", 0.55)
# raios atômicos aproximados (pm), só para a escala do desenho
RAIO = dict(Li=152, Na=186, K=227, Mg=160, Ca=197, Cs=265, Cl=99)
RAIO_ION = {"Na+": 102, "Ca2+": 100, "Cl-": 181}
assert RAIO["Mg"] < RAIO["Na"] < RAIO["K"] and RAIO["Mg"] < RAIO["Ca"] < RAIO["K"]
assert RAIO_ION["Na+"] < RAIO["Na"] and RAIO_ION["Cl-"] > RAIO["Cl"] and RAIO_ION["Ca2+"] < RAIO["Ca"]
P = Q._posicoes()
assert P["Li"][1:] == (2, 1) and P["Na"][1:] == (3, 1) and P["K"][1:] == (4, 1) and P["Mg"][1:] == (3, 2) and P["Ca"][1:] == (4, 2)


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


def esfera(c, t, t0, cx, cy, pm, rotulo, k=0.75, cor=None, sub=None):
    """átomo em escala: raio na tela = pm * k; rotulo dentro (fórmula)"""
    q = ease_back(prog(t, t0, 0.6))
    if q <= 0:
        return
    r = pm * k * q
    E.bola(c, cx, cy, r, cor or ESFERA)
    Q.formula(c, rotulo, cx, cy + r * 0.2, max(30, r * 0.55), TINTA, min(1, q), "center")
    if sub:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, sub, cx, cy + pm * k + 60, 44, "i", TINTA2, a))


def mini_tabela(c, t, t0, x, y, cel, destaque=(), seta=None, ts=None):
    Q.tabela(c, t, t0, x, y, cel, numeros=False, destaque=destaque)
    if seta and ts is not None and t >= ts:
        p = ease_io(prog(t, ts, 0.8))
        x0, y0, x1, y1 = seta
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), AMBAR, ep(t, ts, 0.3), 14, 40)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("magnésio:", "g", 66)] + ps("mais prótons e mais elétrons", "i", 62), XE, 240, passo=0.1)
        esfera(c, t, C["s01.a"] + 0.4, 1200, 560, RAIO["Na"], "Na", 1.2, sub="sódio, 11 prótons")
        esfera(c, t, C["s01.a"] + 0.8, 1620, 590, RAIO["Mg"], "Mg", 1.2, sub="magnésio, 12 prótons")
        E.frase(c, t, C["s01.b"], ps("e mesmo assim é", "i", 66) + [("menor", "g", 66, COR)], XE, 380, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("mais partículas, tamanho menor:", "i", 58, TINTA2), XE, 900, passo=0.08)
        E.frase(c, t, C["s01.c"] + 1.6, [("por quê?", "g", 76, COR)], XE, 1010)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("ordenar pelo", "i", 70), ("tamanho", "g", 66, COR)]),
                 (C["s02.b"], [("o", "i", 70), ("íon de sódio", "g", 66), ("e o átomo", "i", 70)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas anteriores", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("período", "g", 66, COR)] + ps("= número de camadas", "i", 70), XE, 340, passo=0.12)
    E.frase(c, t, C["s03.b"], [("família", "g", 66, COR)] + ps("= a coluna", "i", 70), XE, 460, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("opostas se atraem:", "i", 66) + [("o núcleo puxa os elétrons", "g", 60)], XE, 640, passo=0.12)
    Q.bohr(c, t, C["s03.c"] + 0.3, 1500, 400, (2, 8, 1), r0=70, dr=55, s="Na")


# ---------------- o raio ----------------
def b_raio(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("raio atômico", "g", 100, COR)], XE, 260)
    E.frase(c, t, C["s04.a"] + 1.2, ps("o tamanho do átomo", "i", 66), XE, 370, passo=0.12)
    cx, cy = 1350, 600
    Q.bohr(c, t, C["s04.a"] + 0.3, cx, cy, (2, 8, 1), r0=100, dr=80, s="Na")
    if t >= C["s04.b"]:
        p = ease_io(prog(t, C["s04.b"], 0.7))
        R = 100 + 2 * 80
        M.line(c, cx, cy, cx + R * p, cy, AMBAR, 1, 8)
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.escreve(c, "raio", cx + 70, cy - 20, 50, "g", AMBAR, a))
        E.frase(c, t, C["s04.b"], ps("do núcleo até a última camada", "i", 58), XE, 520, passo=0.1)
    E.frase(c, t, C["s04.c"], ps("última camada mais longe:", "i", 60) + [("átomo maior", "g", 58, COR)], XE, 900, passo=0.1)


# ---------------- na família ----------------
def b_familia(c, t, C, b):
    E.frase(c, t, C["s05"], ps("desça a", "i", 66) + [("família 1", "g", 64, COR)], XE, 190, passo=0.12)
    mini_tabela(c, t, C["s05"] + 0.2, XE, 300, 52, destaque=("Li", "Na", "K"), seta=(XE + 26, 380, XE + 26, 560), ts=C["s05.d"])
    for k, (el, cam, y) in enumerate((("Li", 2, 330), ("Na", 3, 560), ("K", 4, 850))):
        x = 1000 + k * 0
        Q.bohr(c, t, C["s05.a"] + 0.4 * k, 1200 + k * 250, 600, [2, 8, 8, 1][:cam - 1] + [1], r0=34, dr=30, s=el, r_e=7)
        E.foco(c, t, C["s05.c"] + 0.5 * k, 0.4, lambda a, k=k, cam=cam: centro(c, f"{cam} camadas", 1200 + k * 250, 860, 46, "g", COR, a))
    E.frase(c, t, C["s05.b"], ps("cada período a mais:", "i", 58) + [("uma camada a mais", "g", 56)], XE, 980, passo=0.1)
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "descendo a família, o raio aumenta", 1250, 200, 54, "g", fundo=AMBAR, a=a))


# ---------------- no período ----------------
def b_periodo(c, t, C, b):
    E.frase(c, t, C["s06"] + 0.2, ps("ande no", "i", 66) + [("3º período", "g", 64, COR)], XE, 190, passo=0.12)
    for k, (el, ck, nuc, pm) in enumerate((("Na", "s06.a", "11 prótons", RAIO["Na"]), ("Mg", "s06.a", "12 prótons", RAIO["Mg"]))):
        cx = 620 + k * 640
        aperta = ease_io(prog(t, C["s06.d"], 1.0)) if el == "Mg" else 0
        R = lerp(250, 215, aperta)
        q = ep(t, C[ck] + 0.4 * k, 0.5)
        if q > 0:
            for i, r in enumerate((R * 0.38, R * 0.7, R)):
                c.drawCircle(cx, 560, r, M.paint(TINTA2, 0.6 * q, stroke=3))
            E.bola(c, cx, 560, 46 if el == "Na" else 50, E.COR, q)
            centro(c, el, cx, 576, 40, "g", E.SOBRE, q)
            n_ult = 1 if el == "Na" else 2
            for j in range(n_ult):
                g = -1.2 + j * 2.4 + t * 0.3
                E.bola(c, cx + R * math.cos(g), 560 + R * math.sin(g), 14, Q.ELETRON, q)
            E.foco(c, t, C["s06.c"] if el == "Mg" else C["s06.b"], 0.4, lambda a, cx=cx, nuc=nuc: centro(c, nuc, cx, 880, 54, "g", COR, a))
        if el == "Mg" and t >= C["s06.d"]:
            for g in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
                x0, y0 = cx + 300 * math.cos(g), 560 + 300 * math.sin(g)
                M.arrow(c, x0, y0, cx + 240 * math.cos(g), 560 + 240 * math.sin(g), E.COR, ep(t, C["s06.d"], 0.3), 6, 18)
    E.frase(c, t, C["s06.b"], ps("as duas com", "i", 58, TINTA2) + [("3 camadas", "g", 56)], XE, 290, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("mais carga positiva", "i", 60) + [("puxa mais", "g", 58, COR)], W / 2, 980, "center", 0.1)
    E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "para a direita, o raio diminui", 1450, 200, 54, "g", fundo=AMBAR, a=a))


# ---------------- ordenar ----------------
def b_ordem(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("Na,", "g", 66), ("Mg", "g", 66), ("e", "i", 70), ("K", "g", 66)], XE, 190, passo=0.15)
    mini_tabela(c, t, C["s07"] + 0.2, XE, 280, 56, destaque=("Na", "Mg", "K"))
    E.frase(c, t, C["s07.b"], ps("Mg e Na: mesmo período", "i", 56), XE, 860, passo=0.08)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "Mg < Na", XE, 950, 64, "g", COR, a))
    E.frase(c, t, C["s07.d"], ps("Na e K: mesma família", "i", 56), XE + 700, 860, passo=0.08)
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.formula(c, "Na < K", XE + 700, 950, 64, "g", COR, a))
    if t >= C["s07.f"]:
        for k, el in enumerate(("Mg", "Na", "K")):
            esfera(c, t, C["s07.f"] + 0.3 * k, [1330, 1530, 1745][k], 640 - RAIO[el] * 0.55, RAIO[el], el, 0.55)
        E.foco(c, t, C["s07.f"] + 1.0, 0.4, lambda a: E.formula(c, "Mg < Na < K", 1540, 260, 80, "g", TINTA, a, "center"))


# ---------------- o íon ----------------
def b_ion(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("e o íon de sódio?", "i", 70), XE, 190, passo=0.12)
        sai = t >= C["s08.b"]
        if t < C["s08.c"]:
            Q.bohr(c, t, C["s08"] + 0.3, 600, 560, (2, 8, 1), r0=80, dr=70, s="Na")
            if t >= C["s08.a"]:
                q = ep(t, C["s08.a"], 0.4)
                c.drawCircle(600, 560, 80 + 140, M.paint(E.COR, q, stroke=8))
        else:
            some = 1 - ep(t, C["s08.c"], 0.8)
            Q.bohr(c, t, C["s08"] + 0.3, 600, 560, (2, 8), r0=80, dr=70, s="Na")
            if some > 0:
                c.drawCircle(600, 560, 220, M.paint(TINTA2, 0.6 * some, stroke=3))
        if sai:
            u = ease_out(prog(t, C["s08.b"], 1.2))
            E.bola(c, 600 + 220 + 400 * u, 560 - 160 * u, 16, Q.ELETRON, 1 - ep(t, C["s08.b"] + 1.2, 0.4))
        E.frase(c, t, C["s08.a"], ps("1 elétron só na camada 3", "i", 58), XE, 900, passo=0.1)
        E.frase(c, t, C["s08.c"], [("a camada 3 some", "g", 60, COR)], XE + 760, 900)
        E.frase(c, t, C["s08.d"], ps("sobram 2 camadas;", "i", 56, TINTA2), XE, 1010, passo=0.08)
        E.frase(c, t, C["s08.e"], ps("11 prótons puxam só 10 elétrons", "i", 56, TINTA2), XE + 480, 1010, passo=0.08)
        if t >= C["s08.f"]:
            esfera(c, t, C["s08.f"], 1300, 520, RAIO["Na"], "Na", 1.0, sub="átomo")
            esfera(c, t, C["s08.f"] + 0.3, 1650, 560, RAIO_ION["Na+"], "Na^+", 1.0, sub="íon, bem menor")
        return
    E.frase(c, t, C["s09.a"], ps("com o", "i", 70) + [("ânion", "g", 66, Q.ELETRON)] + ps(", o contrário", "i", 70), XE, 220, passo=0.12)
    E.frase(c, t, C["s09.b"], ps("os elétrons a mais se empurram", "i", 60), XE, 340, passo=0.1)
    esfera(c, t, C["s09.c"], 650, 680, RAIO["Cl"], "Cl", 1.2, sub="átomo")
    esfera(c, t, C["s09.c"] + 0.4, 1250, 680, RAIO_ION["Cl-"], "Cl^-", 1.2, cor=E.mix(Q.ELETRON, "#FFFFFF", 0.7), sub="íon, maior")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("o raio cresce junto com o Z?", "i", 66), XE, 310, passo=0.1)
    if t >= C["s10.c"] + 0.4:
        E.risco(c, XE, 325, XE + 830, 260, t, C["s10.c"] + 0.4, largura=12)
    esfera(c, t, C["s10.b"], 1150, 620, RAIO["Na"], "Na", 1.1, sub="Z = 11")
    esfera(c, t, C["s10.b"] + 0.4, 1600, 650, RAIO["Mg"], "Mg", 1.1, sub="Z = 12")
    E.frase(c, t, C["s10.c"], ps("Z maior,", "i", 62) + [("átomo menor", "g", 60, COR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s10.d"], ps("no mesmo período, mais prótons", "i", 58), XE, 700, passo=0.08)
    E.frase(c, t, C["s10.d"] + 1.6, ps("deixam o átomo", "i", 58) + [("menor", "g", 56, COR)], XE, 790, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("o atalho de prova", "i", 70, CLARO), W / 2, 150, "center", 0.12)
        Q.tabela(c, t, C["s11"] + 0.2, 430, 280, 60, numeros=False, escuro=True)
        if t >= C["s11.a"]:
            p = ease_io(prog(t, C["s11.a"], 1.0))
            M.arrow(c, 1300, 360, lerp(1300, 520, p), lerp(360, 700, p), AMBAR, 1, 18, 56)
        E.frase(c, t, C["s11.b"], ps("o raio cresce", "i", 64, CLARO) + [("para baixo e para a esquerda", "g", 60, BR)], W / 2, 830, "center", 0.1)
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "os maiores: Cs, Fr", 700, 960, 50, "g", fundo=AMBAR, a=a))
        return
    E.frase(c, t, C["s12.a"], [("descer", "g", 62, BR)] + ps("acrescenta camada", "i", 64, CLARO), W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s12.b"], [("ir para a direita", "g", 62, BR)] + ps("acrescenta prótons na mesma camada", "i", 62, CLARO), W / 2, 380, "center", 0.1)
    E.frase(c, t, C["s12.c"], [("não", "g", 62, ERRADO)] + ps("compensa: um átomo mais embaixo", "i", 62, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s12.d"], ps("e mais à direita que o outro", "i", 62, CLARO), W / 2, 660, "center", 0.1)
    E.frase(c, t, C["s12.e"], ps("as regras brigam:", "i", 62, CLARO) + [("precisa de mais informação", "g", 58, BR)], W / 2, 820, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s13.a"], [("1", "g", 56, COR)] + ps("ordene do menor para o maior raio:", "i", 58), XE, 320, passo=0.08)
    E.foco(c, t, C["s13.a"] + 1.8, 0.4, lambda a: E.formula(c, "Mg, Ca, K", XE + 60, 430, 84, "g", TINTA, a))
    E.frase(c, t, C["s13.b"], ps("Mg e Ca: família 2", "i", 56, TINTA2), XE, 540, passo=0.08)
    E.frase(c, t, C["s13.c"], ps("Ca e K: 4º período", "i", 56, TINTA2), XE, 630, passo=0.08)
    E.frase(c, t, C["s13.d"], [("2", "g", 56, COR)] + ps("quem é maior:", "i", 58), XE, 780, passo=0.08)
    Q.formula_em(c, t, C["s13.d"] + 1.2, "Ca", XE + 480, 790, 80)
    E.foco(c, t, C["s13.d"] + 1.4, 0.4, lambda a: E.escreve(c, "ou", XE + 610, 785, 60, "i", TINTA, a))
    Q.formula_em(c, t, C["s13.d"] + 1.8, "Ca^{2+}", XE + 690, 790, 80)
    if t < C["s14"]:
        mini_tabela(c, t, C["s13.b"], 1150, 300, 40, destaque=("Mg", "Ca", "K"))
    else:
        E.relogio(c, t, C["s14.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    mini_tabela(c, t, C["s15"], XE, 200, 54, destaque=("Mg", "Ca", "K"))
    E.frase(c, t, C["s15.a"], ps("Ca embaixo do Mg:", "i", 56), XE, 680, passo=0.08)
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.formula(c, "Mg < Ca", XE + 560, 680, 60, "g", COR, a))
    E.frase(c, t, C["s15.c"], ps("K à esquerda do Ca:", "i", 56), XE, 780, passo=0.08)
    E.foco(c, t, C["s15.d"], 0.4, lambda a: E.formula(c, "Ca < K", XE + 560, 780, 60, "g", COR, a))
    for k, el in enumerate(("Mg", "Ca", "K")):
        esfera(c, t, C["s15.e"] + 0.3 * k, [1310, 1500, 1730][k], 600 - RAIO[el] * 0.55, RAIO[el], el, 0.55)
    E.foco(c, t, C["s15.e"] + 0.8, 0.4, lambda a: E.formula(c, "Mg < Ca < K", 1510, 230, 80, "g", TINTA, a, "center"))
    if t >= C["s15.f"]:
        esfera(c, t, C["s15.f"], 1350, 880, RAIO["Ca"], "Ca", 0.6)
        esfera(c, t, C["s15.f"] + 0.3, 1600, 900, RAIO_ION["Ca2+"], "Ca^{2+}", 0.6)
        E.frase(c, t, C["s15.f"] + 0.3, ps("o átomo é maior: o íon perdeu a camada 4", "i", 54, TINTA2), XE, 960, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s16.a", [("descendo a família:", "i", 66), ("aumenta", "g", 62, AMBAR)]),
                 ("s16.b", [("para a direita no período:", "i", 66), ("diminui", "g", 62, AMBAR)]),
                 ("s16.c", [("cátion", "g", 62, COR), ("menor que o átomo", "i", 66)]),
                 ("s16.d", [("ânion", "g", 62, Q.ELETRON), ("maior que o átomo", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s17.a"], ps("ao contrário do raio:", "i", 70), XE, 400, passo=0.12)
    E.frase(c, t, C["s17.b"], [("energia de ionização", "g", 70, COR)], XE, 520)
    E.frase(c, t, C["s17.b"] + 0.8, [("e", "i", 74), ("eletronegatividade", "g", 70, COR)], XE, 640, passo=0.12)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, raio=b_raio, familia=b_familia, periodo=b_periodo, ordem=b_ordem, ion=b_ion,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
