"""Visual — Estudativo · QUI-TER-003: energia de ligação.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho da QUI-MIS-001) e a da trilha Termoquímica e Cinética (cabeçalho da QUI-TER-001):
ΔH < 0 em azul (Q.ELETRON), ΔH > 0 em âmbar. Nesta aula: QUEBRAR ligação = energia que entra, em ÂMBAR, com sinal +;
FORMAR ligação = energia que sai, em AZUL, com sinal −. A molécula se desfaz com Q.molecula(separa=...) e se refaz com os
mesmos átomos. A TABELA de energias de ligação é um cartão branco à direita (tab_lig), com a ligação da vez na cor da matéria.
Peças candidatas ao kit: tab_lig (tabela de energias de ligação), conta_lig (linha "quebrar"/"formar" com o total).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Termoquímica e Cinética")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-TER-003_energia_de_ligacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quebra", "exemplo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR, CALOR = Q.ELETRON, "#E8A317", "#E8590C"

# as contas da aula (energias em kJ/mol)
LIG = {"H–H": 436, "Cl–Cl": 243, "H–Cl": 431, "C–H": 413, "C–Cl": 328, "O=O": 498, "C=O": 799, "O–H": 463}
assert LIG["H–H"] + LIG["Cl–Cl"] == 679 and 2 * LIG["H–Cl"] == 862 and 679 - 862 == -183
assert 679 - 431 == 248
assert LIG["C–H"] + LIG["Cl–Cl"] == 656 and LIG["C–Cl"] + LIG["H–Cl"] == 759 and 656 - 759 == -103
assert 4 * 413 == 1652 and 2 * 498 == 996 and 1652 + 996 == 2648
assert 2 * 799 == 1598 and 4 * 463 == 1852 and 1598 + 1852 == 3450 and 2648 - 3450 == -802
assert Q.lados("H2 + Cl2 -> 2 HCl")[0] == Q.lados("H2 + Cl2 -> 2 HCl")[1]
assert Q.lados("CH4 + 2 O2 -> CO2 + 2 H2O")[0] == Q.lados("CH4 + 2 O2 -> CO2 + 2 H2O")[1]
assert Q.lados("CH4 + Cl2 -> CH3Cl + HCl")[0] == Q.lados("CH4 + Cl2 -> CH3Cl + HCl")[1]


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
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def chama(c, cx, cy, s, t, a=1.0):
    """chama: base em (cx, cy)"""
    if a <= 0:
        return
    for k, (dx, esc) in enumerate(((-0.55, 0.75), (0.0, 1.0), (0.55, 0.75))):
        f = 1 + 0.07 * math.sin(t * 9 + k * 2)
        x0, hh, ww = cx + dx * s, s * esc * f, s * 0.32 * esc
        for cor, kk in (("#F59F00", 1.0), ("#FFE066", 0.62)):
            pth = skia.Path()
            pth.moveTo(x0, cy - hh * kk)
            pth.cubicTo(x0 + ww * kk * 1.2, cy - hh * kk * 0.45, x0 + ww * kk, cy, x0, cy)
            pth.cubicTo(x0 - ww * kk, cy, x0 - ww * kk * 1.2, cy - hh * kk * 0.45, x0, cy - hh * kk)
            c.drawPath(pth, M.paint(cor, a))


def tab_lig(c, t, t0, chaves, x, y, size=50, dy=None, destaque=(), escuro=False, d=0.15):
    """cartão com as energias de ligação (kJ/mol); destaque = ligações na cor da matéria"""
    dy = dy or size * 1.55
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    w, h = size * 7.2, dy * len(chaves) + size * 1.6
    M.rrect(c, x, y, w, h, 24, "#FFFFFF" if not escuro else "#1C1D24", q, shadow=not escuro)
    tinta = BR if escuro else TINTA
    E.escreve(c, "kJ/mol", x + w - size * 0.4 - E.larg("kJ/mol", "i", size * 0.7), y + size * 0.95, size * 0.7, "i", TINTA2 if not escuro else CLARO, q)
    for k, ch in enumerate(chaves):
        yy = y + size * 1.2 + (k + 1) * dy - dy * 0.25
        cor = (E.COR if not escuro else E.CLARO) if ch in destaque else tinta
        E.foco(c, t, t0 + 0.2 + d * k, 0.4, lambda a, ch=ch, yy=yy, cor=cor: (
            E.formula(c, ch, x + size * 0.6, yy, size, "g", cor, a),
            E.formula(c, str(LIG[ch]), x + w - size * 0.6, yy, size, "g", cor, a, "right")))


def conta_lig(c, t, t0, rotulo, conta, total, x, y, size, cor, tt=None, escuro=False):
    """linha 'quebrar: 436 + 243 = 679' com o rótulo na cor (âmbar para quebrar, azul para formar)"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, rotulo, x, y, size, "g", cor, a))
    xr = x + E.larg(rotulo + "  ", "g", size)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, conta, xr, y, size, "g", BR if escuro else TINTA, a))
    if total is not None:
        wc = E.formula(None, conta, 0, 0, size, a=0)
        E.foco(c, t, tt if tt is not None else t0 + 0.8, 0.4, lambda a: E.formula(c, "= " + total, xr + wc + size * 0.3, y, size, "g", cor, a))


def energia_seta(c, t, t0, x, y0, y1, cor, a=1.0, rotulo=None, size=50):
    p = ep(t, t0, 0.4)
    if p > 0:
        F.seta(c, x, y0, x, y0 + (y1 - y0) * ease_out(prog(t, t0, 0.6)), cor, p * a, 7, 24)
        if rotulo:
            E.foco(c, t, t0 + 0.2, 0.4, lambda aa: E.formula(c, rotulo, x + 30, (y0 + y1) / 2 + size * 0.36, size, "g", cor, aa * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        sep = 0.7 * ease_io(prog(t, C["s01.b"], 1.2))
        Q.molecula(c, t, C["s01.a"], "H2", 560, 470, 170, separa=sep)
        E.frase(c, t, C["s01.a"], ps("separar os átomos do", "i", 64), XE, 230, passo=0.1)
        Q.formula_em(c, t, C["s01.a"] + 1.0, "H2", XE + 640, 245, 90)
        if t >= C["s01.b"]:
            energia_seta(c, t, C["s01.b"], 560, 760, 620, AMBAR)
            pilula_em(c, t, C["s01.b"] + 0.3, "gasta energia", 560, 830, 52, AMBAR)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: chama(c, 1450, 700, 200, t, a))
        E.frase(c, t, C["s01.c"], ps("mas a queima do hidrogênio", "i", 60), 1100, 230, passo=0.1)
        E.frase(c, t, C["s01.c"] + 1.2, [("sobra", "g", 60, AZUL)] + ps("energia", "i", 64), 1100, 320, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("de onde vem essa", "i", 70) + [("energia?", "g", 66, COR)], W / 2, 990, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("a resposta está nas", "i", 80) + [("ligações", "g", 76, COR)], XE, 300, passo=0.12)
    lista(c, t, [(C["s02.b"], [("calcular", "g", 70), ("o", "i", 74), ("ΔH", "g", 70, COR)]),
                 (C["s02.c"], [("só", "i", 74), ("com", "i", 74), ("a", "i", 74), ("tabela", "g", 70), ("de", "i", 74), ("ligações", "g", 70)])], XE, 520, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.foco(c, t, C["s03.a"], 0.5, lambda a: (E.formula(c, "ΔH < 0", XE, 260, 90, "g", AZUL, a), E.escreve(c, "libera", XE + 380, 255, 64, "i", TINTA2, a)))
    E.foco(c, t, C["s03.a"] + 0.8, 0.5, lambda a: (E.formula(c, "ΔH > 0", XE + 760, 260, 90, "g", AMBAR, a), E.escreve(c, "absorve", XE + 1140, 255, 64, "i", TINTA2, a)))
    for k, (tt, mol, nome) in enumerate(((C["s03.b"], "H2", "simples"), (C["s03.c"], "O2", "dupla"), (C["s03.d"], "N2", "tripla"))):
        x = 420 + k * 540
        Q.molecula(c, t, tt, mol, x, 560, 150, passo=0.15)
        Q.formula_em(c, t, tt + 0.3, mol, x, 760, 90, align="center")
        E.foco(c, t, tt + 0.4, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 880, 66, "g", COR, a))


# ---------------- quebrar e formar ----------------
def b_quebra(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("uma ligação é como dois", "i", 70) + [("ímãs grudados", "g", 64, COR)], XE, 200, passo=0.1)
            sep = 0.8 * ease_io(prog(t, C["s04.b"], 1.0)) * (1 - ease_io(prog(t, C["s04.d"], 0.8)))
            Q.molecula(c, t, C["s04"], "H2", W / 2, 520, 230, separa=sep)
            if C["s04.b"] <= t < C["s04.d"]:
                energia_seta(c, t, C["s04.b"], W / 2, 360, 450, AMBAR)
            E.foco(c, t, C["s04.c"], 0.5, lambda a: (E.escreve(c, "quebrar", XE, 820, 90, "g", AMBAR, a), E.escreve(c, "absorve: +", XE, 920, 60, "b", TINTA2, a)))
            if t >= C["s04.d"] + 0.6:
                for k in range(6):
                    ang = k * 60 + t * 40
                    x0, y0 = W / 2 + 150 * math.cos(math.radians(ang)), 520 + 150 * math.sin(math.radians(ang))
                    x1, y1 = W / 2 + 260 * math.cos(math.radians(ang)), 520 + 260 * math.sin(math.radians(ang))
                    M.line(c, x0, y0, x0 + (x1 - x0) * ep(t, C["s04.d"] + 0.6, 0.5), y0 + (y1 - y0) * ep(t, C["s04.d"] + 0.6, 0.5), AZUL, 1, 6)
            E.foco(c, t, C["s04.e"], 0.5, lambda a: (E.escreve(c, "formar", 1350, 820, 90, "g", AZUL, a), E.escreve(c, "libera: −", 1350, 920, 60, "b", TINTA2, a)))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("energia de ligação", "g", 80, COR)], XE, 220)
            E.frase(c, t, C["s05.a"] + 0.9, ps("quanto custa quebrar uma ligação", "i", 64, TINTA2), XE, 320, passo=0.1)
            Q.molecula(c, t, C["s05.b"], "H2", 600, 560, 170)
            E.foco(c, t, C["s05.b"] + 0.3, 0.5, lambda a: (E.formula(c, "H–H: 436 kJ/mol", 900, 580, 90, "g", TINTA, a)))
            pilula_em(c, t, C["s05.c"], "mol: um pacote de partículas, outra aula", 960, 760, 44, TINTA2, "b")
            E.frase(c, t, C["s05.c"] + 1.6, ps("a tabela vem pronta na questão", "i", 60), W / 2, 870, "center", 0.1)
            E.frase(c, t, C["s05.d"], ps("formar a mesma ligação libera os mesmos", "i", 60) + [("436", "g", 56, AZUL)], W / 2, 990, "center", 0.1)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06.a"], ps("toda reação", "i", 70) + [("quebra", "g", 66, AMBAR)] + ps("as ligações dos reagentes", "i", 70), XE, 230, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("e", "i", 70) + [("forma", "g", 66, AZUL)] + ps("as dos produtos", "i", 70), XE, 340, passo=0.1)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "ΔH = quebrar − formar", W / 2, 560, 120, "g", TINTA, a, "center"))
    E.foco(c, t, C["s06.c"] + 0.8, 0.4, lambda a: (centro(c, "o que se gasta", 760, 660, 50, "i", AMBAR, a), centro(c, "o que se libera", 1420, 660, 50, "i", AZUL, a)))
    E.frase(c, t, C["s06.d"], ps("formar liberou mais?", "i", 66) + [("sobra energia:", "g", 60), ("exotérmica", "g", 60, AZUL)], W / 2, 860, "center", 0.1)


# ---------------- exemplo resolvido ----------------
EQ = "H2 + Cl2 -> 2 HCl"


def b_exemplo(c, t, C, b):
    cs = Q.equacao(c, t, C["s07.a"], EQ, 620, 220, 100, tl=[C["s07.a"] + 0.25 * k for k in range(4)])
    sep = 0.35 * ease_io(prog(t, C["s08.a"], 1.0))
    Q.molecula(c, t, C["s07.a"] + 0.3, "H2", cs[0], 380, 90, separa=sep)
    Q.molecula(c, t, C["s07.a"] + 0.5, "Cl2", cs[1], 380, 90, separa=sep)
    for j in range(2):
        Q.molecula(c, t, C["s07.a"] + 0.7 + 0.2 * j, "HCl", cs[2] - 120 + 240 * j, 380, 70)
    dest = ("H–H", "Cl–Cl") if C["s08.a"] <= t < C["s08.d"] else ("H–Cl",) if C["s08.d"] <= t < C["s09"] else ()
    tab_lig(c, t, C["s07.b"], ("H–H", "Cl–Cl", "H–Cl"), 1360, 140, 54, destaque=dest, d=1.0)
    conta_lig(c, t, C["s08.a"], "quebrar", "436 + 243", "679", XE, 600, 70, AMBAR, tt=C["s08.c"])
    conta_lig(c, t, C["s08.d"], "formar", "2 × 431", "862", XE, 730, 70, AZUL, tt=C["s08.f"])
    E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.escreve(c, "duas ligações H–Cl", 1100, 725, 46, "b", TINTA2, a))
    E.formula_em(c, t, C["s09.a"], "ΔH = 679 − 862 =", 1180, 900, 80, "g", TINTA2, "right")
    bola_txt(c, t, C["s09.b"], "−183", 1330, 872, 98, 64, AZUL)
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1445, 900, 60, "g", TINTA, a))
    pilula_em(c, t, C["s09.c"], "formar liberou mais", 1560, 1010, 44, AZUL)
    pilula_em(c, t, C["s09.d"], "é a energia do foguete", 1560, 820, 44, TINTA)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 200)
            E.frase(c, t, C["s10.a"], ps("esquecer o", "i", 70) + [("coeficiente", "g", 66, ERRADO)], XE + 470, 200, passo=0.1)
            Q.formula_em(c, t, C["s10.a"] + 0.6, EQ, XE, 380, 100, cores={"coef": E.COR})
            E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "679 − 431 =", XE, 560, 90, "g", ERRADO, a))
            E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "+248", XE + 560, 560, 90, "g", ERRADO, a))
            E.foco(c, t, C["s10.d"], 0.5, lambda a: E.escreve(c, "endotérmica? sinal trocado", XE + 900, 550, 54, "i", ERRADO, a))
            if t >= C["s10.d"] + 0.6:
                E.risco(c, XE - 10, 580, XE + 800, 490, t, C["s10.d"] + 0.6, largura=10)
            E.frase(c, t, C["s10.e"], ps("conte", "i", 70) + [("todas", "g", 66, COR)] + ps("as ligações, molécula por molécula", "i", 70), XE, 780, passo=0.1)
            for j in range(2):
                Q.molecula(c, t, C["s10.e"] + 0.6 + 0.3 * j, "HCl", 760 + 400 * j, 920, 90)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], ps("a ligação", "i", 70) + [("dupla", "g", 66, COR)] + ps("tem valor próprio", "i", 70), XE, 220, passo=0.1)
    Q.molecula(c, t, C["s11.b"], "O2", 520, 520, 160)
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: (centro(c, "O=O", 520, 700, 80, "g", TINTA, a), centro(c, "uma dupla", 520, 790, 56, "i", COR, a)))
    Q.molecula(c, t, C["s11.c"], "CO2", 1300, 520, 160)
    E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: (centro(c, "O=C=O", 1300, 700, 80, "g", TINTA, a), centro(c, "duas duplas", 1300, 790, 56, "i", COR, a)))
    pilula_em(c, t, C["s11.d"], "desenhe a estrutura antes de contar", W / 2, 940, 54, E.COR)


# ---------------- atalho (palco) ----------------
EQA = "CH4 + Cl2 -> CH3Cl + HCl"


def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho:", "i", 72, CLARO) + [("só as ligações que mudam", "g", 66, BR)], W / 2, 150, "center", 0.12)
    if t < C["s13"]:
        E.frase(c, t, C["s12.b"], ps("ligação igual dos dois lados se cancela", "i", 62, CLARO), W / 2, 250, "center", 0.1)
    Q.equacao(c, t, C["s12.c"], EQA, W / 2, 420, 96, tl=[C["s12.c"] + 0.25 * k for k in range(5)], escuro=True)
    if C["s12.d"] <= t < C["s13"]:
        pilula_em(c, t, C["s12.d"], "3 C–H não mudam", W / 2, 540, 54, TINTA2)
    conta_lig(c, t, C["s12.e"], "quebra", "C–H + Cl–Cl", None, 300, 680, 64, AMBAR, escuro=True)
    conta_lig(c, t, C["s12.f"], "forma", "C–Cl + H–Cl", None, 300, 800, 64, AZUL, escuro=True)
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.formula(c, "413 + 243 = 656", 1150, 680, 64, "g", BR, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "328 + 431 = 759", 1150, 800, 64, "g", BR, a))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: (E.formula(c, "ΔH = 656 − 759 = −103 kJ", W / 2, 940, 80, "g", CLARO, a, "center")))
    if t >= C["s13.f"]:
        pilula_em(c, t, C["s13.f"], "quebrar e formar a mesma ligação se anulam", W / 2, 250, 46, E.COR)
    if t >= C["s13.g"]:
        pilula_em(c, t, C["s13.g"], "simples virou dupla? entra na conta", W / 2, 1035, 40, TINTA2)


# ---------------- questão ----------------
EQQ = "CH4 + 2 O2 -> CO2 + 2 H2O"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 150)
    Q.formula_em(c, t, C["s14.a"], EQQ, XE, 320, 90)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "tudo gás", XE, 410, 54, "i", TINTA2, a))
    tab_lig(c, t, C["s14.c"], ("C–H", "O=O", "C=O", "O–H"), 1260, 420, 54, d=0.3)
    E.frase(c, t, C["s14.d"], ps("quanto vale o", "i", 70) + [("ΔH?", "g", 66, COR)], XE, 560, passo=0.12)
    E.relogio(c, t, C["s15.a"], cx=560, cy=780, r=110)


def b_resposta(c, t, C, b):
    Q.formula(c, EQQ, XE, 200, 84)
    tab_lig(c, t, C["s16"] - 0.8, ("C–H", "O=O", "C=O", "O–H"), 1360, 260, 48, d=0.0,
            destaque=("C–H", "O=O") if t < C["s16.d"] else ("C=O", "O–H") if t < C["s17"] else ())
    conta_lig(c, t, C["s16.a"], "quebrar", "4 × 413 + 2 × 498", None, XE, 400, 62, AMBAR)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.formula(c, "= 1652 + 996", XE + 300, 490, 62, "g", TINTA2, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "= 2648", XE + 760, 490, 62, "g", AMBAR, a))
    conta_lig(c, t, C["s16.d"], "formar", "2 × 799 + 4 × 463", None, XE, 640, 62, AZUL)
    E.foco(c, t, C["s16.e"], 0.4, lambda a: E.formula(c, "= 1598 + 1852", XE + 300, 730, 62, "g", TINTA2, a))
    E.foco(c, t, C["s16.f"], 0.4, lambda a: E.formula(c, "= 3450", XE + 760, 730, 62, "g", AZUL, a))
    E.formula_em(c, t, C["s17.a"], "ΔH = 2648 − 3450 =", 1180, 920, 76, "g", TINTA2, "right")
    bola_txt(c, t, C["s17.b"], "−802", 1330, 892, 98, 64, AZUL)
    E.foco(c, t, C["s17.b"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1445, 920, 60, "g", TINTA, a))
    pilula_em(c, t, C["s17.c"], "exotérmica, como toda queima", 1560, 1030, 44, AZUL)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s18.a"], [("quebrar", "g", 80, AMBAR), ("gasta,", "i", 84), ("formar", "g", 80, AZUL), ("libera", "i", 84)], W / 2, 380, "center", 0.14)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "ΔH = quebrar − formar", W / 2, 580, 110, "g", TINTA, a, "center"))
        E.frase(c, t, C["s18.c"], ps("conte cada ligação, com os", "i", 66) + [("coeficientes", "g", 62, COR)], W / 2, 780, "center", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], ps("não quanto, mas", "i", 80, TINTA2) + [("com que rapidez", "g", 76, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s19.b"], [("velocidade", "g", 110, COR), ("média", "g", 110)], XE, 560)
    E.foco(c, t, C["s19.b"] + 0.6, 0.5, lambda a: E.formula(c, "mol/L por minuto", XE, 680, 60, "g", TINTA2, a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 825, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quebra=b_quebra, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
