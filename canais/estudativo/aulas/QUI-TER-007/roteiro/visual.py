"""Visual — Estudativo · QUI-TER-007: lei da velocidade e ordem de reação.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha (QUI-TER-001) e da Cinética (QUI-TER-004): tabela de experimentos
com a linha da vez em turquesa claro, concentrações em Q.formula entre colchetes, fórmula da lei em E.formula.
Nesta aula: a LEI DA VELOCIDADE fica no alto; o EXPOENTE (a ordem) é sempre na cor da matéria. A comparação entre dois
experimentos é uma seta curva entre as linhas da tabela com "× 2" no reagente que mudou e "× 4" na velocidade (fator_seta).
A potência que liga os fatores (2^ordem) entra numa pílula. Peça candidata ao kit: fator_seta (comparação de linhas de tabela).
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
ARQUIVO_FINAL = "estudativo_QUI-TER-007_lei_velocidade_ordem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "ordem", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

EXP = [(0.10, 0.10, 0.002), (0.20, 0.10, 0.004), (0.20, 0.20, 0.016)]
QX = [(0.1, 0.1, 2), (0.3, 0.1, 18), (0.3, 0.2, 18)]
# as contas da aula: a lei v = k[H2][NO]^2 com k = 2 reproduz a tabela; a da questão, v = k[X]^2 com k = 200
for h2, no, v in EXP:
    assert abs(2 * h2 * no ** 2 - v) < 1e-12
for x, y, v in QX:
    assert abs(200 * x ** 2 - v) < 1e-9
assert 2 ** 0 == 1 and 2 ** 1 == 2 and 2 ** 2 == 4 and 2 ** 3 == 8 and 3 ** 2 == 9 and 2 * 4 == 8
assert Q.lados("2 H2 + 2 NO -> N2 + 2 H2O")[0] == Q.lados("2 H2 + 2 NO -> N2 + 2 H2O")[1]


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


def vir(v):
    s = f"{v:g}" if v >= 1 else f"{v:.3f}".rstrip("0")
    if v < 1 and len(s.split(".")[1]) < 2:
        s = f"{v:.2f}"
    return s.replace(".", ",")


def tabela(c, t, t0, cab, linhas, x, y, wcols, dy=96, size=60, tl=None, destaque=(), escuro=False):
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.4)
    if q <= 0:
        return [], []
    xs = [x + sum(wcols[:k]) + wcols[k] / 2 for k in range(len(wcols))]
    for k, s in enumerate(cab):
        Q.formula(c, s, xs[k], y, size * 0.8, TINTA2 if not escuro else CLARO, q, "center")
    M.line(c, x, y + size * 0.4, x + sum(wcols), y + size * 0.4, TINTA2, 0.6 * q, 3)
    ys = []
    for i, lin in enumerate(linhas):
        yy = y + size * 0.4 + (i + 1) * dy - dy * 0.3
        ys.append(yy)
        ti = tl[i] if tl else t0 + 0.3 + 0.2 * i
        if i in destaque:
            M.rrect(c, x - 10, yy - size * 0.95, sum(wcols) + 20, size * 1.3, 14, E.mix(E.COR, "#FFFFFF", 0.78), ep(t, ti, 0.3))
        for k, s in enumerate(lin):
            E.foco(c, t, ti + 0.05 * k, 0.4, lambda a, s=s, k=k, yy=yy: E.formula(c, s, xs[k], yy, size, "g", tinta, a, "center"))
    return xs, ys


def fator_seta(c, t, t0, x, y0, y1, rot, cor=None, lado=1, size=50):
    """seta curva entre duas linhas da tabela, com o fator ("× 2") ao lado"""
    if t < t0:
        return
    cor = cor or E.COR
    p = ease_out(prog(t, t0, 0.6))
    pth = skia.Path()
    pth.moveTo(x, y0 - 20)
    pth.quadTo(x + lado * 80, (y0 + y1) / 2 - 20, x, y1 - 20)
    pt = M.paint(cor, p, stroke=6, cap_round=True)
    c.drawPath(pth, pt)
    M.arrow(c, x + lado * 20, y1 - 34, x, y1 - 20, cor, p, 6, 20)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, x + lado * 70, (y0 + y1) / 2, size, "g", cor, a, "left" if lado > 0 else "right"))


TAB_X, TAB_Y = 170, 360
COLS = (180, 300, 300, 420)


def tab_ex(c, t, t0, destaque=(), tl=None):
    linhas = [[str(i + 1), vir(h2), vir(no), vir(v)] for i, (h2, no, v) in enumerate(EXP)]
    return tabela(c, t, t0, ("exp.", "[H2]", "[NO]", "v (mol/L·s)"), linhas, TAB_X, TAB_Y, COLS, dy=130, size=62, tl=tl, destaque=destaque)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("dobrou a concentração de um reagente", "i", 64), XE, 230, passo=0.1)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.formula(c, "× 2", XE, 400, 120, "g", TINTA, a), E.formula(c, "→ v × 4", XE + 280, 400, 120, "g", COR, a)))
        E.frase(c, t, C["s01.c"], ps("dobrou o outro", "i", 64), XE, 560, passo=0.1)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.formula(c, "× 2", XE, 730, 120, "g", TINTA, a), E.formula(c, "→ v igual", XE + 280, 730, 120, "g", TINTA2, a)))
        E.frase(c, t, C["s01.e"], ps("a regra cabe numa", "i", 64) + [("tabela", "g", 60, COR)], XE, 920, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1640, 640, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], [("lei", "g", 110, COR), ("da", "i", 110), ("velocidade", "g", 110, COR)], XE, 300, passo=0.14)
    lista(c, t, [(C["s02.a"] + 1.0, [("escrever", "i", 74), ("a", "i", 74), ("lei", "g", 70)]),
                 (C["s02.b"], [("achar", "i", 74), ("a", "i", 74), ("ordem", "g", 70, COR), ("na", "i", 74), ("tabela", "g", 70)])], XE, 520, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "2^2 = 2 × 2 = 4", XE, 420, 100, "g", TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.escreve(c, "dobrou o lado: área × 4", XE, 600, 76, "g", COR, a))
    for k in range(4):
        E.foco(c, t, C["s03.b"] + 0.4, 0.4, lambda a, k=k: M.rrect(c, 1250 + (k % 2) * 160, 380 + (k // 2) * 160, 150, 150, 10, E.mix(E.COR, "#FFFFFF", 0.5 if k else 0.0), a))
    E.frase(c, t, C["s03.c"], ps("mais concentração, mais colisões", "i", 66, TINTA2), XE, 800, passo=0.1)


# ---------------- a lei ----------------
LEI_G = "v = k · [A]^{x} · [B]^{y}"


def b_lei(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s04.a"], ps("a velocidade depende das concentrações", "i", 66), XE, 200, passo=0.1)
        if t < C["s04.d"]:
            E.foco(c, t, C["s04.c"], 0.5, lambda a: Q.formula(c, "v = k", W / 2, 460, 140, TINTA, a, "center"))
        elif t < C["s04.e"]:
            E.foco(c, t, C["s04.d"], 0.3, lambda a: Q.formula(c, "v = k · [A] · [B]", W / 2, 460, 140, TINTA, a, "center"))
        else:
            Q.formula(c, "v = k · [A]^{x} · [B]^{y}", W / 2, 460, 140, TINTA, 1, "center", cores={"carga": E.COR})
        if t >= C["s05"]:
            E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "v: velocidade", XE, 680, 58, "b", TINTA, a))
            E.foco(c, t, C["s05.b"], 0.4, lambda a: E.escreve(c, "k: constante da reação, naquela temperatura", XE, 780, 58, "b", TINTA, a))
            pilula_em(c, t, C["s05.c"], "mudou a temperatura, muda o k", 1380, 900, 44, TINTA2)
            E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "x, y: as ordens", XE, 880, 58, "g", COR, a))
            E.foco(c, t, C["s05.e"], 0.4, lambda a: E.escreve(c, "quanto cada reagente pesa", XE, 960, 50, "i", TINTA2, a))
        return
    E.foco(c, t, C["s06"], 0.4, lambda a: E.formula(c, LEI_G, W / 2, 260, 100, "g", TINTA, a, "center"))
    E.frase(c, t, C["s06.b"], ps("a ordem vem do", "i", 72) + [("experimento", "g", 68, COR)], W / 2, 480, "center", 0.12)
    E.frase(c, t, C["s06.c"], [("não", "g", 68, ERRADO)] + ps("dos coeficientes da equação", "i", 72), W / 2, 600, "center", 0.12)
    if t >= C["s06.c"] + 1.6:
        E.risco(c, W / 2 - 480, 610, W / 2 + 480, 560, t, C["s06.c"] + 1.6, largura=8)
    pilula_em(c, t, C["s06.d"], "só a reação de uma batida só segue os coeficientes", W / 2, 800, 44, TINTA2)


# ---------------- como achar a ordem ----------------
def b_ordem(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("só um reagente muda, e ele", "i", 66) + [("dobra", "g", 62, COR)], XE, 210, passo=0.1)
        linhas = ((C["s07.b"], "v igual", "ordem 0"), (C["s07.c"], "v × 2", "ordem 1"), (C["s07.d"], "v × 4", "ordem 2"))
        for k, (tt, a1, a2) in enumerate(linhas):
            y = 420 + k * 170
            E.foco(c, t, tt, 0.4, lambda a, y=y, a1=a1: E.formula(c, "[A] × 2  →  " + a1, XE + 60, y, 80, "g", TINTA, a))
            E.foco(c, t, tt + 0.3, 0.4, lambda a, y=y, a2=a2: E.escreve(c, a2, 1250, y, 80, "g", COR, a))
        E.foco(c, t, C["s07.e"], 0.4, lambda a: E.escreve(c, "como a área do quadrado", 1250, 860, 50, "i", TINTA2, a))
        return
    E.frase(c, t, C["s08.a"], ps("por trás está a", "i", 70) + [("potência", "g", 66, COR)], XE, 210, passo=0.12)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "fator da v = 2^{ordem}", W / 2, 380, 100, "g", TINTA, a, "center"))
    for k, (tt, s) in enumerate(((C["s08.c"], "2^0 = 1"), (C["s08.d"], "2^1 = 2"), (C["s08.e"], "2^2 = 4"))):
        E.foco(c, t, tt, 0.5, lambda a, k=k, s=s: E.formula(c, s, 460 + k * 500, 640, 110, "g", COR, a, "center"))
        E.foco(c, t, tt + 0.3, 0.4, lambda a, k=k: centro(c, f"ordem {k}", 460 + k * 500, 760, 50, "b", TINTA2, a))


# ---------------- exemplo resolvido ----------------
EQ = "2 H2 + 2 NO -> N2 + 2 H2O"


def b_exemplo(c, t, C, b):
    Q.formula_em(c, t, C["s09.a"], EQ, W / 2, 200, 90, align="center")
    dest = (0, 1) if C["s10"] <= t < C["s11"] else (1, 2) if C["s11"] <= t < C["s12"] else ()
    xs, ys = tab_ex(c, t, C["s09.b"], destaque=dest)
    if not ys:
        return
    if C["s10.a"] <= t < C["s11"]:
        fator_seta(c, t, C["s10.a"], xs[1] + 90, ys[0], ys[1], "× 2")
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "igual", xs[2] + 80, (ys[0] + ys[1]) / 2, 40, "i", TINTA2, a))
        fator_seta(c, t, C["s10.d"], xs[3] + 150, ys[0], ys[1], "× 2")
        pilula_em(c, t, C["s10.e"], "ordem 1 no H₂", 1600, 900, 50, E.COR)
    if C["s11.a"] <= t < C["s12"]:
        fator_seta(c, t, C["s11.a"], xs[2] + 90, ys[1], ys[2], "× 2")
        fator_seta(c, t, C["s11.c"] - 0.4, xs[3] + 150, ys[1], ys[2], "× 4")
        pilula_em(c, t, C["s11.d"], "ordem 2 no NO", 1600, 900, 50, E.COR)
    if t >= C["s12"]:
        E.foco(c, t, C["s12.a"], 0.5, lambda a: Q.formula(c, "v = k · [H2]^{1} · [NO]^{2}", W / 2, 900, 90, TINTA, a, "center", cores={"carga": E.COR}))
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "1 + 2 = 3", 1500, 1010, 60, "g", TINTA2, a))
        pilula_em(c, t, C["s12.c"], "ordem total 3", 1000, 1010, 46, E.COR)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    Q.formula_em(c, t, C["s13.a"], EQ, XE, 340, 90, cores={"coef": E.COR})
    E.foco(c, t, C["s13.c"], 0.5, lambda a: Q.formula(c, "v = k · [H2]^{2} · [NO]^{2}", XE, 520, 90, ERRADO, a))
    if t >= C["s13.d"]:
        E.risco(c, XE - 10, 540, XE + 980, 460, t, C["s13.d"], largura=10)
    E.foco(c, t, C["s13.d"] + 0.3, 0.5, lambda a: Q.formula(c, "v = k · [H2]^{1} · [NO]^{2}", XE, 720, 90, TINTA, a, cores={"carga": E.COR}))
    E.foco(c, t, C["s13.d"] + 0.6, 0.4, lambda a: E.selo(c, XE + 1070, 690, 44, True, a))
    pilula_em(c, t, C["s13.e"], "quem manda é o experimento", W / 2, 900, 60, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho", "i", 72, CLARO), W / 2, 160, "center", 0.12)
            E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "fator da v = (fator da [ ])^{ordem}", W / 2, 340, 90, "g", BR, a, "center"))
            E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "× 2 → v × 8:  2^3, ordem 3", W / 2, 580, 86, "g", E.CLARO, a, "center"))
            E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "× 3 → v × 9:  3^2, ordem 2", W / 2, 760, 86, "g", E.CLARO, a, "center"))
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("e serve para prever", "i", 72, CLARO), W / 2, 180, "center", 0.12)
    E.foco(c, t, C["s15.a"] + 0.6, 0.5, lambda a: Q.formula(c, "v = k · [H2] · [NO]^{2}", W / 2, 340, 90, BR, a, "center", escuro=True))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.escreve(c, "dobrar os dois reagentes", 560, 500, 60, "b", BR, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "2 × 2^2 = 2 × 4", W / 2, 660, 90, "g", BR, a, "center"))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "v × 8", W / 2, 800, 110, "g", E.CLARO, a, "center"))
    E.frase(c, t, C["s15.e"], ps("a ordem diz o efeito antes de medir", "i", 60, CLARO), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def tab_q(c, t, t0, destaque=(), tl=None):
    linhas = [[str(i + 1), vir(x), vir(y), str(v)] for i, (x, y, v) in enumerate(QX)]
    return tabela(c, t, t0, ("exp.", "[X]", "[Y]", "v"), linhas, TAB_X, 330, COLS, dy=130, size=62, tl=tl, destaque=destaque)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 150)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "reagentes X e Y", XE + 520, 150, 56, "b", TINTA2, a))
    xs, ys = tab_q(c, t, C["s16.a"], tl=[C["s16.a"] + 0.4, C["s16.b"], C["s16.c"]])
    E.frase(c, t, C["s16.d"], ps("escreva a", "i", 70) + [("lei da velocidade", "g", 66, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s17.a"], cx=1560, cy=560, r=120)


def b_resposta(c, t, C, b):
    dest = (0, 1) if t < C["s18.d"] else (1, 2) if t < C["s19"] else ()
    xs, ys = tab_q(c, t, C["s18"] - 0.6, destaque=dest, tl=[C["s18"] - 0.6] * 3)
    if not ys:
        return
    if t < C["s18.d"]:
        fator_seta(c, t, C["s18.a"], xs[1] + 90, ys[0], ys[1], "× 3")
        fator_seta(c, t, C["s18.b"], xs[3] + 150, ys[0], ys[1], "× 9")
        E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "3^2 = 9: ordem 2", 1300, 900, 70, "g", COR, a))
    elif t < C["s19"]:
        fator_seta(c, t, C["s18.d"], xs[2] + 90, ys[1], ys[2], "× 2")
        E.foco(c, t, C["s18.d"] + 0.3, 0.4, lambda a: E.formula(c, "v igual", xs[3] + 240, (ys[1] + ys[2]) / 2, 50, "g", TINTA2, a))
        E.foco(c, t, C["s18.e"], 0.5, lambda a: E.formula(c, "2^0 = 1: ordem 0", 1300, 900, 70, "g", COR, a))
    else:
        E.foco(c, t, C["s19.a"], 0.5, lambda a: Q.formula(c, "v = k · [X]^{2}", W / 2, 920, 110, TINTA, a, "center", cores={"carga": E.COR}))
        pilula_em(c, t, C["s19.b"], "o Y some: elevado a zero dá 1", W / 2, 1030, 44, TINTA2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, LEI_G, W / 2, 440, 110, "g", TINTA, a, "center"))
        E.frase(c, t, C["s20.b"], ps("a ordem sai da", "i", 74) + [("tabela", "g", 70, COR)] + ps("nunca dos coeficientes", "i", 74), W / 2, 680, "center", 0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("praticando", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s21.b"], ps("ΔH, energia de ativação, velocidade e ordem", "b", 54, TINTA2), XE, 560, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, ordem=b_ordem, exemplo=b_exemplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
