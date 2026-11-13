"""Visual — Estudativo · QUI-SOL-006: titulação.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py). Montagem da titulação: bureta (peça desta aula, candidata ao kit) em cima, com a base; erlenmeyer
embaixo com o ácido e a fenolftaleína: incolor (Q.AGUA) até a viragem, rosa (ROSA) depois, com Q.muda_cor. A conta da titulação
é sempre a mesma linha: H do ácido · M · V (lado do ácido) = OH da base · M · V (lado da base). Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-006_titulacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("montagem", "conta", "dois", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ROSA = "#F06292"
BASE = "#DCEFF7"

# as contas da aula
assert Q.lados("HCl + NaOH -> NaCl + H2O")[0] == Q.lados("HCl + NaOH -> NaCl + H2O")[1]
assert Q.lados("H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O")[0] == Q.lados("H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O")[1]
assert round(0.1 * 25, 9) == 2.5 and 2.5 / 20 == 0.125
assert round(0.1 * 20, 9) == 2 and 2 / 2 == 1 and 1 / 10 == 0.1 and round(0.1 * 20 / 10, 9) == 0.2
assert round(1 * 0.1 * 20, 9) == 2 and 2 / (2 * 10) == 0.1
assert round(0.5 * 16, 9) == 8 and 8 / 10 == 0.8 and 8 / (4 * 10) == 0.2


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


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, est, cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def bureta(c, x, ytop, h, nivel, cor=BASE, a=1.0, aberta=False, escuro=False):
    """bureta: tubo fino graduado, com torneira e ponta; nivel 0..1 = quanto de base ainda há. Candidata ao kit"""
    if a <= 0:
        return
    w = 56
    vidro = Q.VIDRO if not escuro else "#B8BCC8"
    yb = ytop + h
    M.rrect(c, x - w / 2, ytop, w, h, 10, "#FFFFFF" if not escuro else "#2A2C36", 0.5 * a)
    hl = (h - 20) * nivel
    if hl > 0:
        M.rrect(c, x - w / 2 + 6, yb - 10 - hl, w - 12, hl, 6, cor, 0.95 * a)
    for k in range(1, 10):
        yy = ytop + h * k / 10
        M.line(c, x - w / 2 + 6, yy, x - w / 2 + (24 if k % 2 else 32), yy, vidro, 0.7 * a, 2.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, ytop, w, h), 10, 10), M.paint(vidro, a, stroke=4))
    # torneira e ponta
    M.rrect(c, x - 10, yb, 20, 40, 4, vidro, a)
    c.save(); c.translate(x, yb + 22); c.rotate(0 if aberta else 90)
    M.rrect(c, -46, -9, 92, 18, 9, E.COR, a)
    c.restore()
    p = skia.Path(); p.moveTo(x - 8, yb + 40); p.lineTo(x - 3, yb + 90); p.lineTo(x + 3, yb + 90); p.lineTo(x + 8, yb + 40); p.close()
    c.drawPath(p, M.paint(vidro, a))
    # suporte
    M.line(c, x + 140, ytop - 20, x + 140, yb + 520, "#9AA0A8", a, 10)
    M.line(c, x + 140, ytop + 60, x + w / 2, ytop + 60, "#9AA0A8", a, 8)


def montagem(c, t, t0, cx, ytop, tv=None, tg=None, ng=6, nivel_b=None, rot=True, h=420, d_vira=0.5, escala=1.0):
    """bureta + erlenmeyer. tv = instante da viragem (fica rosa); tg = início das gotas"""
    E.foco(c, t, t0, 0.5, lambda a: bureta(c, cx, ytop, h, 0.9 if nivel_b is None else nivel_b, BASE, a, aberta=tg is not None and t >= tg))
    cor = Q.AGUA if tv is None else Q.muda_cor(t, tv, Q.AGUA, ROSA, d_vira)
    yb = ytop + h + 90 + 320
    Q.erlenmeyer(c, t, t0 + 0.2, cx, yb, 300, 300, 0.4, cor)
    if tg is not None:
        Q.gotas(c, t, tg, cx, ytop + h + 92, yb - 120, ng, BASE if t < (tv or 1e9) else ROSA, 0.5, 11)
    if rot:
        rotulo(c, t, t0 + 0.6, "bureta", cx - 160, ytop + h * 0.45, 44, TINTA, "b")
        rotulo(c, t, t0 + 0.8, "erlenmeyer", cx - 260, yb - 40, 44, TINTA, "b")
    return yb


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        montagem(c, t, C["s01.a"], 1400, 120, tv=C["s01.d"] + 0.3, tg=C["s01.c"], ng=10, nivel_b=lerp(0.9, 0.6, ease_io(prog(t, C["s01.c"], 5))), rot=False)
        E.frase(c, t, C["s01.a"], ps("quanto ácido tem no", "i", 70) + [("vinagre?", "g", 66, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.8, ps("não existe régua de ácido", "i", 58, TINTA2), XE, 360, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("pingue uma base,", "i", 66) + [("gota a gota", "g", 62, COR)], XE, 540, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("até a", "i", 66) + [("cor mudar", "g", 62, ROSA)], XE, 650, passo=0.12)
        E.frase(c, t, C["s01.e"], ps("o volume gasto", "i", 66) + [("conta a resposta", "g", 62, COR)], XE, 820, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("a", "i", 74), ("conta", "g", 70, COR), ("da", "i", 74), ("titulação", "i", 74)]),
                 (C["s02.c"], [("ácidos", "i", 74), ("com", "i", 74), ("2", "g", 70, COR), ("hidrogênios", "i", 74)]),
                 (C["s02.d"], [("o", "i", 74), ("ponto", "g", 70), ("de", "i", 74), ("viragem", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    Q.equacao(c, t, C["s03.a"], "HCl + NaOH -> NaCl + H2O", XE + 560, 330, 80, align="center")
    rotulo(c, t, C["s03.a"] + 1.4, "ácido + base → sal + água: neutralização", XE + 560, 420, 44, TINTA2, "b")
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.formula(c, "mols = M · V", XE, 600, 90, "g", COR, a))
    rotulo(c, t, C["s03.b"] + 0.6, "V em litros", XE + 700, 595, 48)
    E.frase(c, t, C["s03.c"], [("fenolftaleína:", "g", 60)], XE, 820, passo=0.1)
    for k, (cor, s, x) in enumerate(((Q.AGUA, "ácido: incolor", 720), (ROSA, "base: rosa", 1240))):
        Q.tubo(c, t, C["s03.c"] + 0.5 + 0.4 * k, x, 1000, 80, 260, 0.6, cor)
        rotulo(c, t, C["s03.c"] + 0.7 + 0.4 * k, s, x + 200, 920, 48, TINTA, "b")


# ---------------- a montagem ----------------
def b_montagem(c, t, C, b):
    cx, ytop = 1380, 110
    tg = C["s05.a"]
    tv = C["s05.c"] + 0.4
    nivel = lerp(0.9, 0.55, ease_io(prog(t, tg, max(0.1, tv - tg))))
    montagem(c, t, C["s04.b"], cx, ytop, tv=tv if t >= C["s05"] else None, tg=tg if t >= C["s05"] else None, ng=14, nivel_b=nivel, rot=True)
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("titular", "g", 90, COR)], XE, 230)
            E.frase(c, t, C["s04.a"] + 0.6, ps("descobrir a concentração", "i", 58), XE, 320, passo=0.1)
            E.frase(c, t, C["s04.a"] + 1.8, ps("com uma solução que você conhece", "i", 58), XE, 400, passo=0.1)
            E.frase(c, t, C["s04.b"], [("embaixo:", "i", 60, TINTA2), ("o", "i", 62), ("ácido", "g", 60, COR)], XE, 560, passo=0.1)
            E.frase(c, t, C["s04.c"], ps("+ gotas de fenolftaleína", "i", 56), XE + 40, 640, passo=0.1)
            E.frase(c, t, C["s04.d"], [("em", "i", 60, TINTA2), ("cima:", "i", 60, TINTA2), ("a", "i", 62), ("bureta", "g", 60)], XE, 800, passo=0.1)
            E.frase(c, t, C["s04.e"], ps("com a", "i", 58) + [("base conhecida", "g", 56, COR)], XE + 40, 880, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("abra a torneira", "i", 66), XE, 230, passo=0.12)
            E.frase(c, t, C["s05.b"], ps("sobra ácido:", "i", 60) + [("incolor", "g", 58)], XE, 380, passo=0.1)
            E.frase(c, t, C["s05.c"], ps("o ácido acabou:", "i", 60) + [("rosa", "g", 58, ROSA)], XE, 490, passo=0.1)
            E.frase(c, t, C["s05.d"], [("ponto", "g", 90, COR), ("de", "i", 90), ("viragem", "g", 90, COR)], XE, 680, passo=0.15)
            rotulo(c, t, C["s05.d"] + 1.2, "o instante em que a cor muda", XE + 360, 770, 48)
            pilula_em(c, t, C["s05.d"] + 2.6, "feche e leia o volume gasto", XE + 380, 900, 46, TINTA, "b")
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06.a"], [("ponto", "g", 80, COR), ("de", "i", 80), ("equivalência", "g", 80, COR)], XE, 300, passo=0.15)
    E.frase(c, t, C["s06.a"] + 1.4, ps("ácido e base se igualam, sem sobra", "i", 58), XE, 400, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("com o indicador certo,", "i", 58, TINTA2), XE, 620, passo=0.1)
    E.frase(c, t, C["s06.b"] + 1.2, ps("a cor vira", "i", 66) + [("praticamente nele", "g", 60, COR)], XE, 720, passo=0.1)


# ---------------- a conta 1:1 ----------------
def b_conta(c, t, C, b):
    Q.equacao(c, t, C["s07.a"], "HCl + NaOH -> NaCl + H2O", W / 2, 220, 90, cores={0: E.COR, 2: E.COR})
    if t >= C["s07.b"]:
        x = Q.centros("HCl + NaOH -> NaCl + H2O", W / 2, 220, 90)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: (centro(c, "1", x[0], 320, 70, "g", COR, a), centro(c, "1", x[1], 320, 70, "g", COR, a)))
    rotulo(c, t, C["s07.c"], "cada partícula de ácido gasta uma de base", W / 2, 410, 46, TINTA)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "mols de ácido = mols de base", W / 2, 520, 72, "g", TINTA, a, "center"))
    E.saida(c, t, C["s08.b"] - 0.1, lambda: E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "mols = M · V", W / 2, 680, 80, "g", TINTA2, a, "center")))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "M ácido · V ácido", W / 2 - 60, 680, 80, "g", COR, a, "right"))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "= M base · V base", W / 2 - 20, 680, 80, "g", TINTA, a))
    if t >= C["s09"]:
        E.formula_em(c, t, C["s09.a"], "M ácido · 20 = 0,1 · 25", W / 2, 830, 76, "g", TINTA, "center")
        E.formula_em(c, t, C["s09.b"], "0,1 · 25 = 2,5", 360, 990, 66, "g", TINTA2)
        E.formula_em(c, t, C["s09.c"], "f{2,5}{20} =", 900, 990, 66, "g", TINTA2)
        bola_txt(c, t, C["s09.d"], "0,125 mol/L", 1330, 948, 120, 38, CERTO)
        rotulo(c, t, C["s09.e"], "mL dos dois lados", 1650, 830, 40, TINTA, "b")


# ---------------- proporção 1:2 ----------------
def b_dois(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("e o", "i", 76) + [("ácido sulfúrico?", "g", 72, COR)], XE, 230, passo=0.12)
        Q.formula_em(c, t, C["s10.a"] + 0.8, "H2SO4", XE + 40, 420, 150, cores={"H": E.COR} if t >= C["s10.b"] else None)
        rotulo(c, t, C["s10.b"] + 0.3, "2 hidrogênios que saem", XE + 280, 520, 50, COR, "b")
        Q.equacao(c, t, C["s10.c"], "H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O", W / 2, 720, 84, cores={"coef": E.COR})
        if t >= C["s10.d"]:
            x = Q.centros("H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O", W / 2, 720, 84)
            E.foco(c, t, C["s10.d"], 0.4, lambda a: (centro(c, "1", x[0], 830, 70, "g", COR, a), centro(c, "2", x[1], 830, 70, "g", COR, a)))
        pilula_em(c, t, C["s10.e"], "proporção 1 : 2", W / 2, 950, 60, E.COR)
        return
    E.frase(c, t, C["s11.a"], [("10 mL", "g", 62, COR)] + ps("de ácido sulfúrico gastaram", "i", 62) + [("20 mL", "g", 62, COR)] + ps("de soda", "i", 62), XE, 200, passo=0.1)
    rotulo(c, t, C["s11.a"] + 1.6, "soda com 0,1 mol/L", XE + 260, 280, 48, TINTA, "b")
    E.formula_em(c, t, C["s11.b"], "soda: 0,1 × 20 = 2", XE, 440, 84, "g", TINTA)
    E.formula_em(c, t, C["s11.c"], "ácido: metade de 2 = 1", XE, 600, 84, "g", COR)
    E.formula_em(c, t, C["s11.d"], "f{1}{10 mL} =", XE, 790, 84, "g", TINTA2)
    bola_txt(c, t, C["s11.e"], "0,1 mol/L", XE + 560, 765, 115, 42, CERTO)
    for k in range(2):
        Q.atomo_em(c, t, C["s11.c"] + 0.3 + 0.2 * k, 1480 + 120 * k, 520, 40, "Na")
    rotulo(c, t, C["s11.c"] + 0.5, "2 de soda para 1 de ácido", 1540, 640, 44, TINTA, "b")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("um para um em tudo", "i", 64), XE + 440, 190, passo=0.1)
    E.formula_em(c, t, C["s12.b"], "f{0,1 × 20}{10} = 0,2 mol/L", XE, 430, 100, "g", ERRADO)
    if t >= C["s12.c"] + 0.4:
        E.risco(c, XE - 10, 460, XE + 1080, 330, t, C["s12.c"] + 0.4, largura=12)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.escreve(c, "o dobro do certo: 0,1", XE, 650, 80, "g", TINTA, a))
    E.frase(c, t, C["s12.e"], ps("escreva a", "i", 66) + [("equação balanceada", "g", 62, COR)] + ps("antes", "i", 66), XE, 840, passo=0.12)
    Q.formula_em(c, t, C["s12.e"] + 1.0, "H2SO4 + 2 NaOH", XE, 960, 76, cores={"coef": E.COR})


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s13.a"], ps("conte os", "i", 64, CLARO) + [("H", "g", 60, BR)] + ps("que saem do ácido", "i", 64, CLARO), XE, 280, passo=0.1)
            E.frase(c, t, C["s13.b"], ps("e as hidroxilas,", "i", 64, CLARO) + [("OH", "g", 60, BR)] + ps(", da base", "i", 64, CLARO), XE, 370, passo=0.1)
            E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "H · M · V", W / 2 - 40, 560, 110, "g", E.CLARO, a, "right"))
            rotulo(c, t, C["s13.c"] + 0.4, "lado do ácido", W / 2 - 300, 640, 44, CLARO, "b")
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "= OH · M · V", W / 2, 560, 110, "g", BR, a))
            rotulo(c, t, C["s13.d"] + 0.4, "lado da base", W / 2 + 330, 640, 44, CLARO, "b")
            E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "2 · M · 10 = 1 · 0,1 · 20", W / 2, 800, 80, "g", BR, a, "center"))
            E.foco(c, t, C["s13.f"], 0.5, lambda a: E.formula(c, "20 · M = 2 → M = 0,1 mol/L", W / 2, 940, 80, "g", E.CLARO, a, "center"))
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque cada", "i", 62, CLARO) + [("H", "g", 58, BR)] + ps("encontra um", "i", 62, CLARO) + [("OH", "g", 58, BR)] + ps("e vira água", "i", 62, CLARO), W / 2, 230, "center", 0.1)
    Q.equacao(c, t, C["s14.a"] + 1.6, "H^+ + OH^- -> H2O", W / 2, 380, 90, escuro=True)
    E.frase(c, t, C["s14.b"], [("cuidado:", "g", 60, ERRADO)] + ps("nem todo hidrogênio sai", "i", 64, CLARO), W / 2, 560, "center", 0.12)
    Q.formula_em(c, t, C["s14.c"], "CH3COOH", W / 2, 760, 130, align="center", escuro=True)
    if t >= C["s14.d"]:
        g = Q.grupos("CH3COOH", W / 2, 760, 130, "center")[-1]
        q = ep(t, C["s14.d"], 0.4)
        E.caixa_pontilhada(c, g["x0"] - 12, g["topo"] - 12, g["x1"] - g["x0"] + 24, g["base"] - g["topo"] + 24, q, E.CLARO, prog_=q)
    rotulo(c, t, C["s14.c"] + 0.4, "4 hidrogênios", W / 2 - 330, 860, 46, CLARO, "b")
    rotulo(c, t, C["s14.d"], "só 1 se solta", W / 2 + 330, 860, 46, BR, "b")
    pilula_em(c, t, C["s14.d"] + 1.2, "conte só os que saem", W / 2, 980, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], [("10 mL", "g", 60, COR)] + ps("de vinagre, com fenolftaleína", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("gastaram", "i", 62) + [("16 mL", "g", 60, COR)] + ps("de soda com", "i", 62) + [("0,5 mol/L", "g", 60, COR)], XE, 420, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("até ficar", "i", 62) + [("rosa", "g", 60, ROSA)], XE, 520, passo=0.1)
    E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: (E.escreve(c, "ácido acético:", XE, 650, 56, "i", TINTA2, a), Q.formula(c, "CH3COOH", XE + 360, 650, 60, TINTA, a)))
    E.frase(c, t, C["s15.d"], ps("concentração em", "i", 64) + [("mol/L?", "g", 60, COR)], XE, 800, passo=0.1)
    if t < C["s16"]:
        montagem(c, t, C["s15.a"], 1500, 120, tv=C["s15.c"] + 0.2, tg=C["s15.b"], ng=8, nivel_b=0.6, rot=False)
    else:
        E.relogio(c, t, C["s16.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17.a"], ps("o ácido acético solta", "i", 62) + [("1 H;", "g", 58, COR)] + ps("a soda tem", "i", 62) + [("1 OH", "g", 58, COR)], XE, 220, passo=0.1)
    pilula_em(c, t, C["s17.b"], "1 para 1", XE + 200, 320, 52, E.COR)
    E.formula_em(c, t, C["s17.c"], "0,5 × 16 = 8", XE, 480, 90, "g", TINTA)
    E.formula_em(c, t, C["s17.d"], "f{8}{10} =", XE, 680, 90, "g", TINTA2)
    bola_txt(c, t, C["s17.e"], "0,8 mol/L", XE + 470, 652, 115, 42, CERTO)

    if t >= C["s17.f"]:
        E.foco(c, t, C["s17.f"], 0.5, lambda a: (E.formula(c, "f{8}{4 × 10} = 0,2", 1180, 900, 66, "g", ERRADO, a),
                                                 E.escreve(c, "contou os 4 H", 1180, 1010, 46, "i", ERRADO, a)))
        if t >= C["s17.f"] + 1.2:
            E.risco(c, 1160, 930, 1660, 840, t, C["s17.f"] + 1.2, largura=10)
    if t < C["s17.f"]:
        E.saida(c, t, C["s17.f"] - 0.1, lambda: montagem(c, t, C["s17"] - 0.3, 1500, 60, tv=C["s17"] - 0.4, nivel_b=0.6, rot=False, h=300))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("a", "i", 70), ("base", "g", 66), ("conhecida", "g", 66, COR), ("descobre", "i", 70), ("o", "i", 70), ("ácido", "g", 66)]),
                 ("s18.b", [("a", "i", 70), ("cor", "g", 66, ROSA), ("vira", "i", 70), ("no", "i", 70), ("ponto", "g", 66), ("de", "i", 70), ("viragem", "g", 66)]),
                 ("s18.c", [("H", "g", 66, COR), ("do", "i", 70), ("ácido", "i", 70), ("e", "i", 70), ("OH", "g", 66, COR), ("da", "i", 70), ("base", "i", 70), ("entram", "i", 70), ("na", "i", 70), ("conta", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("praticando", "g", 110, COR)], XE, 400)
    for k, s in enumerate(("rótulos", "laudos", "curvas", "diluição", "titulação")):
        pilula_em(c, t, C["s19.b"] + 0.3 * k, s, XE + 120 + (k % 3) * 300, 560 + (k // 3) * 110, 50, TINTA)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, montagem=b_montagem, conta=b_conta, dois=b_dois, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
