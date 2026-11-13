"""Visual — Estudativo · QUI-SOL-009: congelar mais tarde, contar as partículas.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a das propriedades coligativas (cabeçalho de
QUI-SOL-008/roteiro/visual.py). Íons com a cor do elemento (Q.atomo: Na roxo, Cl verde, Ca do kit) e a carga ao lado; açúcar =
bolinha âmbar inteira. Contar partículas = a unidade se parte na água (dissolve) e cada pedaço ganha um número.
Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-009_crioscopia_contar_particulas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("congelar", "anti", "contar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AGUA_P = "#7CC4EA"
ACUCAR = "#E8A317"
GELO = "#DDF1FB"

# partículas por fórmula e as contas da aula
PART = {"açúcar": 1, "NaCl": 2, "CaCl2": 3, "glicose": 1}
assert sum(Q.contar("NaCl").values()) == 2 and Q.contar("CaCl2") == {"Ca": 1, "Cl": 2}
assert round(0.1 * PART["açúcar"], 9) == 0.1 and round(0.1 * PART["NaCl"], 9) == 0.2 and round(0.1 * PART["CaCl2"], 9) == 0.3
assert round(0.3 * 1, 9) == round(0.1 * 3, 9)
Q_ = dict(A=0.25 * 1, B=0.1 * 2, C=0.1 * 3)
assert sorted(Q_, key=Q_.get) == ["B", "A", "C"]


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


def particula(c, x, y, r, cor, a=1.0):
    c.drawCircle(x, y, r, M.paint(cor, a))
    c.drawCircle(x, y, r, M.paint(M.mix(cor, "#000000", 0.35), 0.6 * a, stroke=2))


def acucar(c, x, y, r, a=1.0):
    """molécula de açúcar: bolinha âmbar com um anel claro, inteira"""
    particula(c, x, y, r, ACUCAR, a)
    c.drawCircle(x, y, r * 0.5, M.paint("#FFFFFF", 0.6 * a, stroke=3))


def ion(c, x, y, r, s, carga, a=1.0):
    Q.atomo(c, x, y, r, s, a)
    E.escreve(c, carga, x + r * 0.75, y - r * 0.6, r * 0.9, "g", TINTA, a)


def unidade(c, t, t0, formula, cx, cy, r=34, abre=None, num=None, a=1.0):
    """uma unidade de soluto: NaCl, CaCl2 ou açúcar; abre = instante em que os íons se separam; num = instante dos números"""
    if a <= 0 or t < t0:
        return 0
    q = ep(t, t0, 0.4) * a
    s = ease_io(prog(t, abre, 0.8)) if abre is not None else 0.0
    if formula == "açúcar":
        pts = [((cx, cy), None)]
        acucar(c, cx, cy, r * 1.15, q)
    elif formula == "NaCl":
        d = lerp(r * 1.6, r * 3.4, s)
        pts = [((cx - d / 2, cy), ("Na", "+")), ((cx + d / 2, cy), ("Cl", "−"))]
    else:
        d = lerp(r * 1.6, r * 3.4, s)
        pts = [((cx, cy), ("Ca", "2+")), ((cx - d, cy + lerp(0, 40, s)), ("Cl", "−")), ((cx + d, cy + lerp(0, 40, s)), ("Cl", "−"))]
    for (x, y), el in pts:
        if el:
            ion(c, x, y, r, el[0], el[1] if s > 0.5 else "", q)
    if num is not None and t >= num:
        for k, ((x, y), _) in enumerate(pts):
            E.foco(c, t, num + 0.2 * k, 0.3, lambda a_, x=x, y=y, k=k: (E.bola(c, x, y + r + 40, 22, TINTA, a_),
                                                                         centro(c, str(k + 1), x, y + r + 52, 30, "g", BR, a_)))
    return len(pts)


def copo(c, t, t0, cx, yb, w, h, a=1.0):
    Q.bequer(c, t, t0, cx, yb, w, h, 0.8, Q.AGUA, graduacao=False)


def gelo_rede(c, t, x, y, cols, lins, dx, impurezas=(), desarruma=0.0, a=1.0, r=16):
    """partículas de água arrumadas em fileiras (gelo); impurezas = posições (i, j) de soluto que entortam a vizinhança"""
    rnd = random.Random(7)
    for j in range(lins):
        for i in range(cols):
            if (i, j) in impurezas:
                continue
            perto = min((abs(i - a_) + abs(j - b_) for a_, b_ in impurezas), default=99)
            k = desarruma * (1.0 if perto <= 1 else 0.35 if perto == 2 else 0.0)
            ox, oy = (rnd.random() - 0.5) * 24 * k + 3 * math.sin(t * 3 + i + j) * k, (rnd.random() - 0.5) * 24 * k
            particula(c, x + i * dx + ox, y + j * dx + oy, r, AGUA_P, a)
    for (i, j) in impurezas:
        particula(c, x + i * dx, y + j * dx, r * 1.3, E.COR, a)


def termometro(c, x, y, h, nivel, cor="#2E86AB", a=1.0, valor=None):
    if a <= 0:
        return
    M.rrect(c, x - 14, y - h, 28, h, 14, "#FFFFFF", a, stroke=3, stroke_color=TINTA2)
    M.rrect(c, x - 7, y - 10 - (h - 30) * nivel, 14, (h - 30) * nivel + 10, 7, cor, a)
    c.drawCircle(x, y + 6, 24, M.paint(cor, a))
    c.drawCircle(x, y + 6, 24, M.paint(TINTA2, a, stroke=3))
    if valor:
        E.pilula(c, valor, x, y - h - 40, 40, "g", fundo=TINTA, a=a)


def radiador(c, cx, cy, w, h, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 16, "#5B6470", a)
    for k in range(9):
        xx = cx - w / 2 + 30 + k * (w - 60) / 8
        M.line(c, xx, cy - h / 2 + 20, xx, cy + h / 2 - 20, "#9AA0A8", a, 6)
    M.rrect(c, cx - 40, cy - h / 2 - 50, 80, 50, 12, "#3A3B42", a)


# ---------------- gancho ----------------
GX = (420, 960, 1500)
GN = (("açúcar", "açúcar"), ("sal de cozinha", "NaCl"), ("cloreto de cálcio", "CaCl2"))


def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("três copos com", "i", 66) + [("0,1 mol/L", "g", 62, COR)], W / 2, 180, "center", 0.12)
        for k, (nome, f) in enumerate(GN):
            cx = GX[k]
            ti = C["s01.c"] + 0.5 * k
            copo(c, t, ti, cx, 760, 300, 340)
            unidade(c, t, ti + 0.2, f, cx, 600, 40, abre=ti + 0.6)
            rotulo(c, t, ti + 0.3, nome, cx, 840, 46, TINTA, "b")
            if f != "açúcar":
                E.foco(c, t, ti + 0.4, 0.4, lambda a, f=f, cx=cx: Q.formula(c, f, cx, 900, 48, TINTA2, a, "center"))
        # gelo: o de açúcar congela primeiro, o de cloreto de cálcio por último
        for k, ti in ((0, C["s01.d"]), (2, C["s01.e"])):
            q = ep(t, ti, 0.8)
            if q > 0:
                cx = GX[k]
                M.rrect(c, cx - 140, 760 - 340 * 0.8, 280, 340 * 0.8 - 6, 12, GELO, 0.75 * q)
                pilula_em(c, t, ti + 0.3, "1º a congelar" if k == 0 else "último", cx, 360, 44, E.COR if k == 0 else TINTA)
        E.frase(c, t, C["s01.f"], ps("mesma concentração,", "i", 62) + [("efeitos diferentes", "g", 58, COR)], W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("o", "i", 74), ("anticongelante", "g", 70, COR)]),
                 (C["s02.c"], [("contar", "g", 70, COR), ("partículas", "i", 74), ("e", "i", 74), ("ordenar", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("soluto", "g", 62, COR)] + ps("baixa a pressão de vapor:", "i", 62), XE, 300, passo=0.1)
    E.frase(c, t, C["s03.a"] + 1.8, ps("ferve mais quente", "i", 62), XE + 60, 390, passo=0.1)
    E.frase(c, t, C["s03.b"], ps("depende de", "i", 62) + [("quantas", "g", 58, COR)] + ps("partículas:", "i", 62) + [("coligativo", "g", 58, COR)], XE, 530, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("na água, um sal se separa em", "i", 62) + [("íons", "g", 58, COR)], XE, 680, passo=0.1)
    unidade(c, t, C["s03.c"] + 0.3, "NaCl", 640, 860, 50, abre=C["s03.d"])
    E.foco(c, t, C["s03.d"] + 0.3, 0.4, lambda a: Q.formula(c, "NaCl -> Na^+ + Cl^-", 1400, 880, 80, TINTA, a, "center"))
    rotulo(c, t, C["s03.d"] + 0.6, "sódio e cloreto", 1400, 980, 48, TINTA2)


# ---------------- crioscopia ----------------
def b_congelar(c, t, C, b):
    if t < C["s05"]:
        imp = ((2, 1), (5, 3)) if t >= C["s04.b"] else ()
        q_imp = ep(t, C["s04.b"], 0.4)
        E.foco(c, t, C["s04.a"], 0.6, lambda a: gelo_rede(c, t, 1060, 320, 8, 6, 90, imp, ep(t, C["s04.c"], 0.8), a))
        E.frase(c, t, C["s04.a"], ps("para congelar, a água se", "i", 58), XE, 280, passo=0.1)
        E.frase(c, t, C["s04.a"] + 1.4, [("arruma", "g", 62, COR)] + ps("em fileiras", "i", 62), XE, 370, passo=0.1)
        E.frase(c, t, C["s04.b"], ps("o", "i", 62) + [("soluto", "g", 58, COR)] + ps("fica no caminho", "i", 62), XE, 520, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("e", "i", 62) + [("atrapalha", "g", 58, ERRADO)] + ps("a arrumação", "i", 62), XE, 620, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("é preciso", "i", 62) + [("esfriar mais", "g", 58, COR)], XE, 780, passo=0.1)
        return
    E.foco(c, t, C["s05.a"], 0.5, lambda a: termometro(c, 1500, 860, 520, 0.25, "#2E86AB", a, "abaixo de 0 °C"))
    E.frase(c, t, C["s05.a"], ps("a solução congela", "i", 66) + [("abaixo de 0 °C", "g", 62, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s05.b"], [("crioscopia", "g", 120, COR)], XE, 520)
    rotulo(c, t, C["s05.b"] + 0.8, "a descida do ponto de congelamento", XE + 420, 610, 48)
    E.frase(c, t, C["s05.c"], ps("também", "i", 62) + [("coligativa:", "g", 58, COR)], XE, 760, passo=0.1)
    E.frase(c, t, C["s05.c"] + 1.4, ps("mais partículas, mais frio", "i", 62), XE, 850, passo=0.1)


# ---------------- anticongelante ----------------
def b_anti(c, t, C, b):
    if t < C["s07"]:
        E.foco(c, t, C["s06.a"], 0.6, lambda a: radiador(c, 1400, 600, 520, 380, a))
        E.frase(c, t, C["s06.a"], ps("o", "i", 70) + [("anticongelante", "g", 70, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s06.a"] + 1.0, ps("do radiador do carro", "i", 58, TINTA2), XE, 350, passo=0.1)
        E.frase(c, t, C["s06.b"], ps("meio a meio com a água:", "i", 58), XE, 500, passo=0.1)
        E.foco(c, t, C["s06.b"] + 1.6, 0.5, lambda a: E.formula(c, "congela ≈ −35 °C", XE, 610, 74, "g", "#2E86AB", a))
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "ferve > 100 °C", XE, 730, 74, "g", ERRADO, a))
        pilula_em(c, t, C["s06.d"], "protege no frio e no calor", XE + 380, 860, 50, E.COR)
        return
    E.frase(c, t, C["s07.a"], ps("sal na estrada com", "i", 66) + [("neve", "g", 62, COR)], XE, 280, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("a água salgada só congela", "i", 58), XE, 420, passo=0.1)
    E.frase(c, t, C["s07.b"] + 1.4, [("bem abaixo de 0 °C", "g", 58, COR)], XE, 510)
    E.frase(c, t, C["s07.c"], ps("e o gelo", "i", 62) + [("derrete", "g", 58, COR)], XE, 660, passo=0.1)
    # estrada com gelo derretendo
    q = ep(t, C["s07.a"], 0.5)
    if q > 0:
        M.rrect(c, 1000, 760, 820, 140, 20, "#3A3B42", q)
        for k in range(6):
            M.rrect(c, 1040 + k * 135, 822, 70, 14, 7, "#F2C94C", q)
        derrete = ep(t, C["s07.c"], 1.4)
        M.rrect(c, 1020, 740, 780, 50, 22, GELO, q * (1 - 0.8 * derrete))
        rnd = random.Random(3)
        for k in range(26):
            u = prog(t, C["s07.a"] + 0.4 + 0.04 * k, 0.6)
            if u > 0:
                x = 1040 + rnd.random() * 740
                c.drawCircle(x, lerp(420, 738, u * u), 8, M.paint(BR, q))
                c.drawCircle(x, lerp(420, 738, u * u), 8, M.paint(TINTA2, q, stroke=2))


# ---------------- contar as partículas ----------------
CX = (380, 960, 1540)


def b_contar(c, t, C, b):
    E.frase(c, t, C["s08.a"] - 0.6, ps("o segredo:", "i", 64, TINTA2) + [("contar", "g", 64, COR), ("as", "i", 66), ("partículas", "i", 66)], W / 2, 170, "center", 0.12)
    dados = ((C["s08.b"], "açúcar", None, C["s08.c"] + 0.6, C["s08.d"], "0,1 × 1 = 0,1"),
             (C["s09.a"], "NaCl", C["s09.a"] + 0.4, C["s09.b"] + 0.3, C["s09.c"], "0,1 × 2 = 0,2"),
             (C["s10.a"], "CaCl2", C["s10.a"] + 0.4, C["s10.b"] + 0.3, C["s10.c"], "0,1 × 3 = 0,3"))
    for k, (ti, f, abre, num, tc, conta) in enumerate(dados):
        cx = CX[k]
        copo(c, t, ti - 0.2, cx, 640, 380, 360)
        unidade(c, t, ti, f, cx, 470, 36, abre=abre, num=num)
        E.foco(c, t, ti + 0.2, 0.4, lambda a, f=f, cx=cx: (centro(c, "açúcar", cx, 730, 52, "b", TINTA, a) if f == "açúcar" else Q.formula(c, f, cx, 735, 56, TINTA, a, "center")))
        E.foco(c, t, tc, 0.5, lambda a, cx=cx, conta=conta: E.formula(c, conta, cx, 850, 56, "g", COR, a, "center"))
        rotulo(c, t, tc + 0.6, "mol/L de partículas", cx, 920, 38, TINTA2, "b")
    if t >= C["s11"]:
        p = ep(t, C["s11.a"], 0.5)
        M.arrow(c, CX[0], 990, CX[2], 990, E.COR, p, 6, 24, ease_io(p))
        E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: centro(c, "mais partículas, maior efeito", W / 2, 1050, 44, "b", COR, a))
        pilula_em(c, t, C["s11.b"], "congela mais frio", CX[2], 300, 42, TINTA)
        pilula_em(c, t, C["s11.d"], "congela primeiro", CX[0], 300, 42, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("mesma concentração, mesmo efeito?", "i", 60), XE + 440, 190, passo=0.1)

    def errado():
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "0,1 = 0,1 = 0,1: congelam juntos", XE, 380, 70, "g", ERRADO, a))
        if t >= C["s12.b"] + 2.2:
            E.risco(c, XE - 10, 400, XE + 1160, 320, t, C["s12.b"] + 2.2, largura=12)
    errado()
    E.frase(c, t, C["s12.c"], ps("a concentração conta as", "i", 62) + [("unidades", "g", 58)], XE, 560, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("quem decide: as", "i", 62) + [("partículas soltas", "g", 58, COR)], XE, 680, passo=0.1)
    for k, (f, n) in enumerate((("açúcar", 1), ("NaCl", 2), ("CaCl2", 3))):
        x = XE + 120 + k * 520
        unidade(c, t, C["s12.d"] + 0.4 + 0.3 * k, f, x, 870, 30, abre=C["s12.d"] + 0.5 + 0.3 * k)
        E.foco(c, t, C["s12.d"] + 0.9 + 0.3 * k, 0.4, lambda a, x=x, n=n: E.pilula(c, f"{n}", x + 200, 860, 50, "g", fundo=E.COR, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 160, "center", 0.12)
            E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "concentração × partículas", W / 2, 340, 100, "g", BR, a, "center"))
            E.frase(c, t, C["s13.b"], ps("o maior resultado tem o", "i", 62, CLARO) + [("maior efeito", "g", 58, BR)], W / 2, 480, "center", 0.1)
            E.frase(c, t, C["s13.c"], ps("congela mais frio, ferve mais quente", "i", 56, CLARO), W / 2, 570, "center", 0.1)
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "0,3 açúcar: 0,3 × 1", 560, 760, 70, "g", BR, a, "center"))
            E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "0,1 CaCl₂: 0,1 × 3", 1360, 760, 70, "g", BR, a, "center"))
            bola_txt(c, t, C["s13.f"], "0,3", 560, 900, 70, 60)
            bola_txt(c, t, C["s13.f"] + 0.2, "0,3", 1360, 900, 70, 60)
            E.foco(c, t, C["s13.f"] + 0.4, 0.4, lambda a: centro(c, "=", W / 2, 925, 110, "g", E.CLARO, a))
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque o efeito só olha", "i", 62, CLARO), W / 2, 320, "center", 0.1)
    E.frase(c, t, C["s14.a"] + 1.8, [("a quantidade de partículas", "g", 62, BR)], W / 2, 420, "center")
    E.frase(c, t, C["s14.b"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("ácidos fracos soltam só parte dos íons", "i", 60, CLARO), W / 2, 640, "center", 0.1)
    pilula_em(c, t, C["s14.b"] + 3.0, "a fração que se separa: outra aula", W / 2, 780, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    itens = ((C["s15.a"], "A", "glicose (açúcar)", "0,25 mol/L"), (C["s15.b"], "B", "sal de cozinha", "0,1 mol/L"), (C["s15.c"], "C", "cloreto de cálcio", "0,1 mol/L"))
    for k, (ti, l, nome, conc) in enumerate(itens):
        y = 340 + k * 130
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 44, a=a), centro(c, l, XE + 40, y - 2, 54, "g", BR, a)))
        E.frase(c, t, ti + 0.1, ps(nome, "i", 62) + [(conc, "g", 58, COR)], XE + 110, y, passo=0.08)
    E.frase(c, t, C["s15.d"], ps("ordem: da que congela", "i", 60) + [("primeiro", "g", 56, COR)], XE, 820, passo=0.08)
    E.frase(c, t, C["s15.d"] + 1.6, ps("à que congela", "i", 60) + [("por último", "g", 56, COR)], XE, 910, passo=0.08)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.6, lambda a: E.simbolo(c, 1520, 560, 180 * a, giro=6 * math.sin(t * 0.5)), blur=0)
    else:
        E.relogio(c, t, C["s16.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("conte as partículas", "i", 62, TINTA2), XE, 170, passo=0.1)
    itens = ((C["s17.a"], "A", "0,25 × 1 = 0,25"), (C["s17.b"], "B", "0,1 × 2 = 0,2"), (C["s17.c"], "C", "0,1 × 3 = 0,3"))
    for k, (ti, l, conta) in enumerate(itens):
        y = 320 + k * 140
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 44, a=a), centro(c, l, XE + 40, y - 2, 54, "g", BR, a)))
        E.formula_em(c, t, ti + 0.2, conta, XE + 120, y, 72, "g", TINTA)
    E.frase(c, t, C["s18.a"], ps("menos partículas: congela primeiro", "i", 58), XE, 790, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "B → A → C", 1140, 470, 110, "g", COR, a))
    E.foco(c, t, C["s18.b"] + 0.6, 0.4, lambda a: E.selo(c, 1780, 430, 50, True, a))
    rotulo(c, t, C["s18.c"], "a glicose tinha a maior concentração,", 1420, 640, 42, TINTA, "b")
    rotulo(c, t, C["s18.d"], "mas o sal ficou com menos partículas", 1420, 710, 42, COR, "b")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("soluto:", "g", 66), ("congela", "i", 70), ("abaixo", "g", 66, COR), ("de", "i", 70), ("0", "g", 66), ("°C", "g", 66)]),
                 ("s19.b", [("concentração", "g", 66), ("×", "g", 66, TINTA2), ("partículas", "g", 66, COR)]),
                 ("s19.c", [("maior", "i", 70), ("resultado,", "i", 70), ("maior", "g", 66), ("efeito", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("osmose", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], ps("o sal que conserva a carne", "i", 60), XE, 560, passo=0.1)
    E.frase(c, t, C["s20.c"], ps("tirar o sal da água do mar", "i", 60), XE, 660, passo=0.1)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, congelar=b_congelar, anti=b_anti, contar=b_contar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
