"""Visual — Estudativo · QUI-SOL-004: concentração em mol/L.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py). A concentração em mol/L aparece como M (M = n/V), a letra da vez em E.COR_TEXTO; a ponte
g/L ⇄ mol/L é sempre a mesma figura: duas pílulas com "÷ massa molar" indo e "× massa molar" voltando. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-004_concentracao_mol_por_litro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("porque", "exemplo", "ponte", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
MM = dict(H=1, C=12, O=16, Na=23, Cl=35.5)
assert MM["Na"] + MM["O"] + MM["H"] == 40 and MM["Na"] + MM["Cl"] == 58.5
assert 6 * MM["C"] + 12 * MM["H"] + 6 * MM["O"] == 180
assert 40 / 40 == 1 and 1 / 2 == 0.5 and (40 / 2) / 40 == 0.5
assert round(0.2 * 0.5, 9) == 0.1 and round(0.1 * 180, 9) == 18
assert 9 / 0.25 == 36 and 36 / 180 == 0.2 and round(9 / 180, 9) == 0.05 and round(0.05 / 0.25, 9) == 0.2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, "i", cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def frac_letras(c, x, y, esq, cima, baixo, size, cores=(TINTA, TINTA, TINTA), a=1.0, escuro=False):
    """fórmula 'esq = cima/baixo' com cor própria em cada letra; (x, y) = linha de base. Candidata ao kit"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    E.escreve(c, esq, x, y, size, "g", cores[0], a)
    xe = x + E.larg(esq, "g", size) + size * 0.2
    E.escreve(c, "=", xe, y, size, "g", TINTA2 if not escuro else CLARO, a)
    xf = xe + E.larg("=", "g", size) + size * 0.25
    wf = max(E.larg(cima, "g", size * 0.85), E.larg(baixo, "g", size * 0.85)) + size * 0.3
    centro(c, cima, xf + wf / 2, y - size * 0.48, size * 0.85, "g", cores[1], a)
    centro(c, baixo, xf + wf / 2, y + size * 0.62, size * 0.85, "g", cores[2], a)
    bh = max(5, size * 0.07)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xf, y - size * 0.33, wf, bh), bh / 2, bh / 2), M.paint(tinta, a))


def unidade(c, atomos, x, y, r, a=1.0):
    """uma 'unidade' de soluto: bolinhas encostadas (NaOH = Na, O, H)"""
    for k, s in enumerate(atomos):
        Q.atomo(c, x + k * r * 1.55, y, r * (Q.RAIO.get(s, 1.0) / 1.0), s, a)


def ponte_unidades(c, t, t0, cx, y, size=70, escuro=False, t_volta=None):
    """g/L ⇄ mol/L: ÷ massa molar indo, × massa molar voltando"""
    fundo2 = "#3A3B42" if escuro else TINTA
    pilula_em(c, t, t0, "g/L", cx - 420, y, size, fundo2)
    pilula_em(c, t, t0 + 0.3, "mol/L", cx + 420, y, size, E.COR)
    p = ep(t, t0 + 0.4, 0.5)
    seta = E.CLARO if escuro else E.COR
    txt = BR if escuro else TINTA
    if p > 0:
        M.arrow(c, cx - 280, y - 40, cx + 260, y - 40, seta, p, 6, 24, ease_io(p))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: centro(c, "÷ massa molar", cx, y - 70, 46, "b", txt, a))
    if t_volta is not None:
        q = ep(t, t_volta, 0.5)
        if q > 0:
            M.arrow(c, cx + 260, y + 50, cx - 280, y + 50, seta, q, 6, 24, ease_io(q))
            E.foco(c, t, t_volta + 0.2, 0.4, lambda a: centro(c, "× massa molar", cx, y + 110, 46, "b", txt, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("dois frascos de", "i", 70, TINTA2) + [("1 litro", "g", 66)], XE, 190, passo=0.12)
        for k, (ti, f, g, x) in enumerate(((C["s01.b"], "NaOH", "40 g", 560), (C["s01.c"], "NaCl", "58,5 g", 1360))):
            Q.bequer(c, t, ti, x, 760, 340, 380, 0.75, Q.AGUA, particulas=dict(n=24, estado="liquido", tipos=[(E.COR, 1.0)], r=8, semente=3 + k))
            E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, g=g: centro(c, g, x, 870, 80, "g", COR, a))
            E.foco(c, t, ti + 0.4, 0.4, lambda a, x=x, f=f: Q.formula(c, f, x, 950, 60, TINTA2, a, "center"))
        rotulo(c, t, C["s01.b"] + 0.6, "soda cáustica", 560, 330, 46)
        rotulo(c, t, C["s01.c"] + 0.6, "sal de cozinha", 1360, 330, 46)
        E.frase(c, t, C["s01.d"], [("qual", "i", 66), ("tem", "i", 66), ("mais", "g", 62, COR), ("soluto?", "i", 66)], W / 2, 1050, "center", 0.12)

        def mol():
            E.foco(c, t, C["s01.e"] + 0.4, 0.4, lambda a: centro(c, "=", W / 2, 640, 150, "g", TINTA2, a))
            pilula_em(c, t, C["s01.e"] + 0.8, "1 mol", 560, 580, 60, E.COR)
            pilula_em(c, t, C["s01.e"] + 1.0, "1 mol", 1360, 580, 60, E.COR)
        mol()
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("concentração", "i", 74), ("em", "i", 74), ("mol/L", "g", 70, COR)]),
                 (C["s02.c"], [("g/L", "g", 70), ("→", "g", 70, TINTA2), ("mol/L", "g", 70, COR), ("numa", "i", 74), ("divisão", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("1 mol", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("um pacote com sempre o mesmo número de partículas", "i", 56), XE, 300, passo=0.08)
    E.frase(c, t, C["s03.b"], [("massa molar", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("gramas de 1 mol", "i", 62), XE, 430, passo=0.1)
    pilula_em(c, t, C["s03.b"] + 1.2, "g/mol", 1420, 410, 50, TINTA)
    E.formula_em(c, t, C["s03.c"], "mols = f{massa}{massa molar}", XE, 640, 84, "g", TINTA)
    E.formula_em(c, t, C["s03.d"], "C = f{m}{V}", XE, 870, 84, "g", TINTA)
    rotulo(c, t, C["s03.d"] + 0.6, "concentração comum, em g/L", XE + 760, 870, 50)


# ---------------- por que mol ----------------
def b_porque(c, t, C, b):
    E.frase(c, t, C["s04"], ps("por que contar em", "i", 76) + [("mol?", "g", 72, COR)], XE, 190, passo=0.12)
    E.frase(c, t, C["s04.a"], ps("as reações acontecem", "i", 60) + [("partícula com partícula", "g", 56, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s04.b"], [("o", "i", 64), ("grama", "g", 60), ("engana", "g", 60, ERRADO)], XE, 400, passo=0.12)
    if t >= C["s04.c"]:
        inc = 0.55 * ease_io(prog(t, C["s04.c"] + 0.6, 1.0))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.balanca(c, W / 2, 770, lambda cc, x, y: unidade(cc, ("Na", "O", "H"), x - 60, y - 30, 36, a),
                                                          lambda cc, x, y: unidade(cc, ("Na", "Cl"), x - 40, y - 30, 36, a), inc, a, 80, 820))
        rotulo(c, t, C["s04.c"] + 0.4, "1 unidade de soda", 420, 930, 44, TINTA)
        rotulo(c, t, C["s04.c"] + 0.6, "1 unidade de sal", 1500, 930, 44, TINTA)
    E.foco(c, t, C["s04.e"], 0.5, lambda a: (E.formula(c, "1 mol = 40 g", 420, 1040, 60, "g", COR, a, "center"),
                                             E.formula(c, "1 mol = 58,5 g", 1500, 1040, 60, "g", COR, a, "center")))
    rotulo(c, t, C["s04.d"], "mesmo número de unidades, pesos diferentes", 1300, 400, 44, TINTA)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    cores = (COR if t >= C["s05.a"] else TINTA, COR if t >= C["s05.b"] else TINTA, COR if t >= C["s05.b"] + 1.2 else TINTA)
    E.foco(c, t, C["s05"], 0.5, lambda a: frac_letras(c, 260, 500, "M", "n", "V", 200, cores, a))
    E.frase(c, t, C["s05.a"], ps("mols de soluto em cada", "i", 60) + [("litro", "g", 58, COR)], 1000, 300, passo=0.1)
    for k, (ti, l, nome, un) in enumerate(((C["s05.b"], "n", "número de mols do soluto", "mol"), (C["s05.b"] + 1.2, "V", "volume da solução", "L"))):
        y = 440 + k * 120
        E.foco(c, t, ti, 0.5, lambda a, l=l, y=y: E.escreve(c, l, 1000, y, 76, "g", COR, a))
        E.frase(c, t, ti + 0.2, ps(nome, "i", 56), 1090, y, passo=0.08)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "M maiúsculo ≠ m da massa", 560, 760, 50, "b", fundo=TINTA, a=a))
    pilula_em(c, t, C["s05.c"] + 0.6, "mol/L", 1100, 760, 60, E.COR)
    E.frase(c, t, C["s05.d"], ps("também chamada de", "i", 60, TINTA2) + [("concentração molar", "g", 56), ("ou", "i", 60, TINTA2), ("molaridade", "g", 56)], XE, 940, passo=0.1)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("40 g", "g", 70, COR), ("de", "i", 74), ("soda", "i", 74)], XE, 200, passo=0.12)
    E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: Q.formula(c, "NaOH", XE + 470, 200, 70, TINTA, a))
    E.frase(c, t, C["s06.a"] + 1.4, ps("em", "i", 74) + [("2 L", "g", 70, COR)], XE + 760, 200, passo=0.12)
    if t < C["s07"]:
        Q.inventario(c, t, C["s06.b"], [("Na", 1), ("O", 1), ("H", 1)], XE + 10, 360, 60, tl=[C["s06.b"], C["s06.b"] + 0.9, C["s06.b"] + 1.7], nomes=True)
        for k, v in enumerate(("23", "16", "1")):
            E.foco(c, t, C["s06.b"] + 0.3 + 0.8 * k, 0.4, lambda a, k=k, v=v: E.escreve(c, f"{v} g/mol", XE + 620, 382 + k * 110, 60, "g", TINTA2, a))
        E.formula_em(c, t, C["s06.c"] - 0.6, "23 + 16 + 1 =", XE + 10, 780, 80, "g", TINTA2)
        bola_txt(c, t, C["s06.c"], "40 g/mol", XE + 840, 752, 130, 46)
        Q.bequer(c, t, C["s06.a"], 1560, 900, 360, 460, 0.8, Q.AGUA, particulas=dict(n=30, estado="liquido", tipos=[(E.COR, 1.0)], r=8))
        rotulo(c, t, C["s06.a"] + 0.4, "2 L de solução", 1560, 980, 46, TINTA)
        return
    E.frase(c, t, C["s07.a"], [("1", "g", 58, COR), ("gramas", "i", 62), ("→", "g", 58, TINTA2), ("mols", "i", 62)], XE, 380, passo=0.12)
    E.formula_em(c, t, C["s07.b"], "f{40 g}{40 g/mol} = 1 mol", XE + 60, 540, 84, "g", TINTA)
    E.frase(c, t, C["s07.c"], [("2", "g", 58, COR), ("mols", "i", 62), ("→", "g", 58, TINTA2), ("mol/L", "g", 58)], XE, 720, passo=0.12)
    E.formula_em(c, t, C["s07.d"], "M = f{1 mol}{2 L} =", XE + 60, 880, 84, "g", TINTA)
    bola_txt(c, t, C["s07.d"] + 1.2, "0,5 mol/L", XE + 900, 850, 130, 44)


# ---------------- ponte g/L → mol/L ----------------
def b_ponte(c, t, C, b):
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], ps("já tem em", "i", 70) + [("g/L?", "g", 66, COR)], XE, 200, passo=0.12)
            E.formula_em(c, t, C["s08.b"], "f{40 g}{2 L} = 20 g/L", XE, 360, 84, "g", TINTA)
            ponte_unidades(c, t, C["s08.c"], W / 2, 640, 66)
            E.formula_em(c, t, C["s08.d"], "f{20}{40} = 0,5 mol/L", XE, 900, 84, "g", TINTA)
            pilula_em(c, t, C["s08.e"], "o mesmo resultado, numa conta só", 1400, 870, 46, E.COR, "b")
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09.a"], ps("o caminho de volta:", "i", 66) + [("multiplicar", "g", 62, COR)], XE, 200, passo=0.12)
    E.frase(c, t, C["s09.a"] + 1.4, [("0,5 L", "g", 60)] + ps("de glicose a", "i", 64) + [("0,2 mol/L", "g", 60, COR)], XE, 300, passo=0.1)
    E.formula_em(c, t, C["s09.b"], "0,2 × 0,5 = 0,1 mol", XE, 470, 84, "g", TINTA)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: (Q.formula(c, "C6H12O6", XE, 620, 70, TINTA2, a), E.escreve(c, "= 180 g/mol", XE + 400, 620, 66, "g", TINTA2, a)))
    E.formula_em(c, t, C["s09.d"], "0,1 × 180 =", XE, 800, 84, "g", TINTA2)
    bola_txt(c, t, C["s09.d"] + 0.8, "18 g", XE + 620, 775, 90, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("massa ÷ volume não é mol/L", "i", 64), XE + 440, 190, passo=0.1)
    E.formula_em(c, t, C["s10.b"], "f{40 g}{2 L} = 20", XE, 430, 100, "g", TINTA)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.escreve(c, "mol/L", XE + 720, 430, 100, "g", ERRADO, a))
    if t >= C["s10.c"] + 1.0:
        E.risco(c, XE + 700, 450, XE + 1040, 360, t, C["s10.c"] + 1.0, largura=12)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.escreve(c, "g/L", XE + 1080, 430, 100, "g", CERTO, a))
    E.frase(c, t, C["s10.e"], ps("faltou passar pela", "i", 66) + [("massa molar", "g", 62, COR)], XE, 680, passo=0.12)
    E.formula_em(c, t, C["s10.e"] + 1.4, "f{20}{40} = 0,5 mol/L", XE, 880, 90, "g", COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        ponte_unidades(c, t, C["s11.a"], W / 2, 450, 90, escuro=True, t_volta=C["s11.b"])
        E.frase(c, t, C["s11.c"], ps("confira pelas unidades:", "i", 56, CLARO), W / 2, 760, "center", 0.1)
        E.foco(c, t, C["s11.c"] + 1.2, 0.5, lambda a: E.formula(c, "f{g}{g/mol} = mol", W / 2, 920, 90, "g", BR, a, "center"))
        return
    E.frase(c, t, C["s12.a"], ps("dividir pela massa molar", "i", 64, CLARO) + [("troca gramas por mols", "g", 60, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s12.a"] + 2.2, ps("e o litro continua embaixo", "i", 64, CLARO), W / 2, 400, "center", 0.1)
    E.frase(c, t, C["s12.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("a questão pede só os mols", "i", 66, CLARO), W / 2, 620, "center", 0.12)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "mols = f{massa}{massa molar}", W / 2, 820, 90, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s13.a"], [("9 g", "g", 62, COR)] + ps("de glicose em", "i", 66) + [("250 mL", "g", 62, COR)], XE, 330, passo=0.1)
    E.foco(c, t, C["s13.a"] + 0.8, 0.4, lambda a: Q.formula(c, "C6H12O6", XE, 440, 70, TINTA2, a))
    E.frase(c, t, C["s13.b"], ps("massa molar:", "i", 64) + [("180 g/mol", "g", 62)], XE, 580, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("qual é a concentração em", "i", 64) + [("mol/L?", "g", 62, COR)], XE, 760, passo=0.1)
    if t < C["s14"]:
        E.foco(c, t, C["s13.a"], 0.6, lambda a: E.simbolo(c, 1520, 540, 200 * a, giro=6 * math.sin(t * 0.5)), blur=0)
    else:
        E.relogio(c, t, C["s14.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s15.a"], "250 mL ÷ 1000 = 0,25 L", XE, 230, 76, "g", TINTA)
    E.formula_em(c, t, C["s15.b"], "f{9 g}{0,25 L} = 36 g/L", XE, 410, 80, "g", TINTA)
    E.formula_em(c, t, C["s15.c"], "f{36}{180} =", XE, 610, 80, "g", TINTA2)
    bola_txt(c, t, C["s15.d"], "0,2 mol/L", XE + 530, 585, 125, 42, CERTO)
    E.frase(c, t, C["s16.a"], ps("pelo outro caminho:", "i", 56, TINTA2), 1120, 230, passo=0.1)
    E.formula_em(c, t, C["s16.a"] + 0.6, "f{9}{180} = 0,05 mol", 1120, 410, 72, "g", TINTA)
    E.formula_em(c, t, C["s16.b"], "f{0,05}{0,25} = 0,2 mol/L", 1120, 610, 72, "g", TINTA)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.selo(c, 1800, 585, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s17.a"], 0.5, lambda a: (E.bola(c, 300, 374, 52, a=a), centro(c, "1", 300, 396, 60, "g", BR, a)))
        E.foco(c, t, C["s17.a"] + 0.2, 0.5, lambda a: frac_letras(c, 400, 420, "M", "n", "V", 110, (COR, TINTA, TINTA), a))
        rotulo(c, t, C["s17.a"] + 0.6, "mols ÷ litros de solução", 1200, 420, 54)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.bola(c, 300, 674, 52, a=a), centro(c, "2", 300, 696, 60, "g", BR, a)))
        E.foco(c, t, C["s17.b"] + 0.2, 0.5, lambda a: E.formula(c, "f{g/L}{massa molar} = mol/L", 400, 720, 84, "g", TINTA, a))
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("diluição", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s18.b"], [("e", "i", 90), ("mistura", "g", 100, COR)], XE, 530)
    E.foco(c, t, C["s18.b"] + 1.0, 0.5, lambda a: E.formula(c, "C₁V₁ = C₂V₂", XE, 700, 90, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, porque=b_porque, formula=b_formula, exemplo=b_exemplo, ponte=b_ponte,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
