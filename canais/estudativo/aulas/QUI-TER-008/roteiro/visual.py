"""Visual — Estudativo · QUI-TER-008: praticando energia e velocidade das reações (prática, 5 questões).

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha (QUI-TER-001) e da Cinética (QUI-TER-004). Cada questão tem a sua
cor de número na esfera turquesa no canto ("questão 1 de 5"); o enunciado fica no alto e a resolução embaixo, com o resultado na
esfera (azul para ΔH < 0, âmbar para ΔH > 0, turquesa para velocidade e ordem). As peças vêm das aulas TER-002 (linha_eq),
TER-003 (tab_lig), TER-004 (tabela, curva_pts) e TER-006 (marcas_eixo, seta_ea), copiadas aqui.
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
ARQUIVO_FINAL = "estudativo_QUI-TER-008_praticando_energia_velocidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR = Q.ELETRON, "#E8A317"

# as contas das cinco questões
assert 140 - 40 == 100 and 90 - 40 == 50 and 100 - 40 == 60
assert -394 + 2 * (-286) + 890 == -76
for eq in ("C + O2 -> CO2", "CH4 + 2 O2 -> CO2 + 2 H2O", "N2 + 3 H2 -> 2 NH3", "2 N2O5 -> 4 NO2 + O2", "2 NO + Cl2 -> 2 NOCl"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert 945 + 3 * 436 == 2253 and 6 * 391 == 2346 and 2253 - 2346 == -93 and 2253 - 3 * 391 == 1080
assert abs((1.2 - 0.8) / 5 - 0.08) < 1e-9 and abs(0.08 * 4 / 2 - 0.16) < 1e-9 and abs(0.08 / 2 - 0.04) < 1e-9
assert 12 / 3 == 4 == 2 ** 2 and 24 / 12 == 2 == 2 ** 1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def cab_q(c, t, t0, n):
    """'questão n' no alto, com a esfera do número"""
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, XE + 40, 130, 44, a=a), centro(c, str(n), XE + 40, 152, 54, "g", E.SOBRE, a),
                                     E.escreve(c, f"questão {n} de 5", XE + 110, 152, 52, "b", TINTA2, a)))


def dh_txt(c, v, x, y, size, a=1.0, align="right"):
    w1 = E.formula(None, "ΔH = ", 0, 0, size, a=0)
    num = ("+" if v > 0 else "−") + str(abs(v)) + " kJ"
    w2 = E.formula(None, num, 0, 0, size, a=0)
    x0 = x - w1 - w2 if align == "right" else x
    E.formula(c, "ΔH = ", x0, y, size, "g", TINTA2, a)
    E.formula(c, num, x0 + w1, y, size, "g", AZUL if v < 0 else AMBAR, a)


def linha_eq(c, t, t0, s, v, x, y, size, xdh, cores=None):
    Q.formula_em(c, t, t0, s, x, y, size, cores=cores)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: dh_txt(c, v, xdh, y, size * 0.9, a))


def marcas_eixo(c, t, t0, Y, vals, x, size=42):
    if Y is None:
        return
    for v in vals:
        E.foco(c, t, t0, 0.4, lambda a, v=v: (M.line(c, x - 14, Y(v), x + 14, Y(v), TINTA2, a, 4),
                                              E.formula(c, str(v), x - 26, Y(v) + size * 0.36, size, "g", TINTA2, a, "right")))


def seta_v(c, t, t0, Y, v0, v1, x, cor, rot=None, size=44):
    if Y is None or t < t0:
        return
    F.seta(c, x, Y(v0), x, Y(v1) + (6 if v1 > v0 else -6), cor, ep(t, t0, 0.4), 7, 24, ease_out(prog(t, t0, 0.6)))
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rot, x + 20, (Y(v0) + Y(v1)) / 2 + size * 0.36, size, "g", cor, a))


def tabela(c, t, t0, cab, linhas, x, y, wcols, dy=96, size=60, destaque=()):
    q = ep(t, t0, 0.4)
    if q <= 0:
        return [], []
    xs = [x + sum(wcols[:k]) + wcols[k] / 2 for k in range(len(wcols))]
    for k, s in enumerate(cab):
        Q.formula(c, s, xs[k], y, size * 0.8, TINTA2, q, "center")
    M.line(c, x, y + size * 0.4, x + sum(wcols), y + size * 0.4, TINTA2, 0.6 * q, 3)
    ys = []
    for i, lin in enumerate(linhas):
        yy = y + size * 0.4 + (i + 1) * dy - dy * 0.3
        ys.append(yy)
        if i in destaque:
            M.rrect(c, x - 10, yy - size * 0.95, sum(wcols) + 20, size * 1.3, 14, E.mix(E.COR, "#FFFFFF", 0.78), q)
        for k, s in enumerate(lin):
            E.foco(c, t, t0 + 0.3 + 0.2 * i + 0.05 * k, 0.4, lambda a, s=s, k=k, yy=yy: E.formula(c, s, xs[k], yy, size, "g", TINTA, a, "center"))
    return xs, ys


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("cinco", "g", 130, COR), ("questões", "g", 130)], XE, 330, passo=0.14)
    E.frase(c, t, C["s01.b"], ps("uma para cada ferramenta da trilha", "i", 66, TINTA2), XE, 460, passo=0.1)
    for k, s in enumerate(("diagrama", "Hess", "ligações", "velocidade", "ordem")):
        E.foco(c, t, C["s01.c"] + 0.3 * k, 0.4, lambda a, k=k, s=s: (E.bola(c, 260 + k * 340, 680, 60, a=a),
                                                                       centro(c, str(k + 1), 260 + k * 340, 706, 72, "g", E.SOBRE, a),
                                                                       centro(c, s, 260 + k * 340, 820, 50, "b", TINTA, a)))
    E.frase(c, t, C["s01.d"], ps("pause, tente, e só depois veja a resolução", "i", 60), W / 2, 990, "center", 0.1)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], ps("a caixa de ferramentas", "i", 76, TINTA2), XE, 170, passo=0.12)
    linhas = ((C["s02.b"], "ΔH = chegada − partida;  Ea = topo − reagentes"), (C["s02.c"], "Hess: inverteu, troca o sinal; multiplicou, multiplica"),
              (C["s02.d"], "ligações: ΔH = quebrar − formar"), (C["s02.e"], "v = Δ[ ] ÷ Δt;  a ordem sai da tabela"))
    for k, (tt, s) in enumerate(linhas):
        y = 340 + k * 170
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 40, y - 22, 40, a=a), centro(c, str(k + 1), XE + 40, y - 2, 48, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s: E.formula(c, s.replace("÷", "/"), XE + 100, y, 58, "g", TINTA, a))


# ---------------- questão 1: diagrama ----------------
GX, GY, GW, GH = 300, 300, 900, 560


def diag1(c, t, t0, cat=True, ea=None, dh=None):
    Y = Q.energia(c, t, t0, GX, GY, GW, GH, er=40, ep_=100, pico=140, cat=90 if cat else None, ea=ea, dh=dh, sinal=False)
    marcas_eixo(c, t, t0 + 0.4, Y, [40, 90, 100, 140], GX)
    return Y


def b_q1(c, t, C, b):
    cab_q(c, t, C["s03.a"], 1)
    Y = diag1(c, t, C["s03.b"] - 0.4, cat=t >= C["s03.e"])
    E.frase(c, t, C["s03.f"], ps("Ea sem catalisador?", "b", 44), 1440, 380, passo=0.08)
    E.frase(c, t, C["s03.f"] + 0.6, ps("Ea com catalisador?", "b", 44), 1440, 450, passo=0.08)
    E.frase(c, t, C["s03.f"] + 1.2, ps("ΔH? a vizinhança?", "b", 44), 1440, 520, passo=0.08)
    E.relogio(c, t, C["s04.a"], cx=1600, cy=740, r=100)


def b_r1(c, t, C, b):
    cab_q(c, t, C["s05"] - 0.6, 1)
    Y = diag1(c, t, C["s05"] - 0.6, ea=C["s05.a"], dh=C["s05.e"])
    seta_v(c, t, C["s05.c"], Y, 40, 90, GX + GW * 0.62, TINTA, "50")
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "sem: 140 − 40 = 100", 1430, 380, 44, "g", COR, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "com: 90 − 40 = 50", 1460, 470, 46, "g", TINTA, a))
    E.foco(c, t, C["s05.f"], 0.4, lambda a: E.formula(c, "ΔH = +60 kJ", 1520, 600, 52, "g", AMBAR, a))
    pilula_em(c, t, C["s05.g"], "endotérmica: a vizinhança esfria", 760, 1000, 48, AMBAR)
    pilula_em(c, t, C["s05.h"], "o catalisador só mudou o topo", 1520, 1000, 44, TINTA)


# ---------------- questão 2: Hess ----------------
E1, E2, E3 = "C + O2 -> CO2", "H2 + ½ O2 -> H2O(l)", "CH4 + 2 O2 -> CO2 + 2 H2O(l)"
QXH, XD = 270, 1800


def alvo2(c, t, t0, y):
    q = ep(t, t0, 0.5)
    if q > 0:
        E.caixa_pontilhada(c, QXH - 30, y - 90, 760, 130, q, E.COR, prog_=q)
    Q.formula_em(c, t, t0, "C + 2 H2 -> CH4", QXH, y, 84)


def b_q2(c, t, C, b):
    cab_q(c, t, C["s06.a"], 2)
    alvo2(c, t, C["s06.b"], 330)
    linha_eq(c, t, C["s06.c"], E1, -394, QXH, 500, 66, XD)
    linha_eq(c, t, C["s06.d"], E2, -286, QXH, 630, 66, XD)
    linha_eq(c, t, C["s06.e"], E3, -890, QXH, 760, 66, XD)
    E.relogio(c, t, C["s07.a"], cx=W / 2, cy=900, r=60)


def b_r2(c, t, C, b):
    cab_q(c, t, C["s08"] - 0.6, 2)
    alvo2(c, t, C["s08"] - 0.6, 330)
    linha_eq(c, t, C["s08"] - 0.6, E1, -394, QXH, 500, 66, XD, cores={"C": E.COR} if t >= C["s08.b"] else None)
    pilula_em(c, t, C["s08.b"] + 0.3, "fica", 190, 475, 38, TINTA)
    if t < C["s08.c"]:
        linha_eq(c, t, C["s08"] - 0.6, E2, -286, QXH, 630, 66, XD)
    else:
        E.foco(c, t, C["s08.c"], 0.4, lambda a: (Q.formula(c, "2 H2 + O2 -> 2 H2O(l)", QXH, 630, 66, cores={"coef": E.COR}, a=a)))
        pilula_em(c, t, C["s08.c"] + 0.2, "× 2", 190, 605, 38, E.COR)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: dh_txt(c, -572, XD, 630, 68, a))
    if t < C["s08.e"]:
        linha_eq(c, t, C["s08"] - 0.6, E3, -890, QXH, 760, 66, XD)
    else:
        E.foco(c, t, C["s08.e"], 0.4, lambda a: Q.formula(c, "CO2 + 2 H2O(l) -> CH4 + 2 O2", QXH, 760, 66, cores={"CH4": E.COR}, a=a))
        pilula_em(c, t, C["s08.e"] + 0.2, "invertida", 150, 735, 32, AMBAR)
        E.foco(c, t, C["s08.f"], 0.4, lambda a: dh_txt(c, 890, XD, 760, 68, a))
    if t >= C["s09.a"]:
        q = ep(t, C["s09.a"], 0.4)
        M.line(c, QXH, 830, XD, 830, TINTA, q, 5)
        pilula_em(c, t, C["s09.a"], "CO₂, H₂O e O₂ se cancelam", 760, 900, 42, TINTA2)
    E.formula_em(c, t, C["s09.b"], "−394 − 572 + 890 =", 1500, 1010, 66, "g", TINTA2, "right")
    bola_txt(c, t, C["s09.c"], "−76", 1620, 985, 80, 56, AZUL)
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1715, 1010, 50, "g", TINTA, a))


# ---------------- questão 3: energia de ligação ----------------
LIG = (("tripla N–N", 945), ("H–H", 436), ("N–H", 391))


def tab3(c, t, t0, x, y, size=54, dest=()):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    w = size * 9.0
    M.rrect(c, x, y, w, size * 1.6 + len(LIG) * size * 1.55, 24, "#FFFFFF", q, shadow=True)
    E.escreve(c, "kJ/mol", x + w - size * 0.4 - E.larg("kJ/mol", "i", size * 0.7), y + size * 0.95, size * 0.7, "i", TINTA2, q)
    for k, (ch, v) in enumerate(LIG):
        yy = y + size * 1.2 + (k + 1) * size * 1.55 - size * 0.4
        cor = E.COR if ch in dest else TINTA
        E.foco(c, t, t0 + 0.2 + 0.3 * k, 0.4, lambda a, ch=ch, v=v, yy=yy, cor=cor: (E.formula(c, ch, x + size * 0.6, yy, size, "g", cor, a),
                                                                                    E.formula(c, str(v), x + w - size * 0.6, yy, size, "g", cor, a, "right")))


def b_q3(c, t, C, b):
    cab_q(c, t, C["s10.a"], 3)
    Q.formula_em(c, t, C["s10.b"], "N2 + 3 H2 -> 2 NH3", XE, 340, 96)
    Q.molecula(c, t, C["s10.b"] + 0.4, "N2", 320, 520, 100)
    Q.molecula(c, t, C["s10.b"] + 0.7, "NH3", 760, 520, 100)
    tab3(c, t, C["s10.c"] - 0.2, 1250, 240)
    E.frase(c, t, C["s10.f"], ps("calcule o", "i", 70) + [("ΔH", "g", 66, COR)], XE, 760, passo=0.12)
    E.relogio(c, t, C["s11.a"], cx=1500, cy=760, r=90)


def b_r3(c, t, C, b):
    cab_q(c, t, C["s12"] - 0.6, 3)
    Q.formula(c, "N2 + 3 H2 -> 2 NH3", XE, 300, 84)
    tab3(c, t, C["s12"] - 0.6, 1330, 200, 48, dest=("tripla N–N", "H–H") if t < C["s12.d"] else ("N–H",))
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.escreve(c, "quebrar", XE, 470, 62, "g", AMBAR, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "945 + 3 × 436 = 945 + 1308", XE + 290, 470, 62, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "= 2253", XE + 290, 560, 62, "g", AMBAR, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "formar", XE, 700, 62, "g", AZUL, a))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.formula(c, "2 amônias × 3 N–H = 6 ligações", XE + 290, 700, 56, "g", TINTA2, a))
    E.foco(c, t, C["s12.f"], 0.4, lambda a: E.formula(c, "6 × 391 = 2346", XE + 290, 790, 62, "g", AZUL, a))
    E.formula_em(c, t, C["s13.a"], "ΔH = 2253 − 2346 =", 1380, 960, 70, "g", TINTA2, "right")
    bola_txt(c, t, C["s13.b"], "−93", 1510, 935, 80, 56, AZUL)
    E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1605, 960, 50, "g", TINTA, a))
    if t >= C["s13.c"]:
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "3 ligações? +1080: sinal errado", XE, 1040, 46, "g", ERRADO, a))


# ---------------- questão 4: velocidade num gráfico ----------------
from functools import lru_cache


def plano4(c, t, t0):
    P = E.plano(c, t, t0, 300, 300, 700, 560, 0, 10, 0, 1.4, passo=5, passo_y=0.4, marcas_x=[0, 5, 10], marcas_y=[0.4, 0.8, 1.2],
                nomes=("", ""), size=40)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, "[N₂O₅] (mol/L)", 330, 270, 44, "b", TINTA2, a), E.escreve(c, "tempo (min)", 760, 950, 46, "i", TINTA2, a)))
    return P


def f4(x):
    assert True
    return 0.6 + 0.6 * math.exp(-math.log(3) / 5 * x)   # 1,2 em 0 min e 0,8 em 5 min


def b_q4(c, t, C, b):
    cab_q(c, t, C["s14.a"], 4)
    Q.formula_em(c, t, C["s14.b"], "2 N2O5 -> 4 NO2 + O2", 1180, 220, 64)
    P = plano4(c, t, C["s14.c"] - 0.3)
    E.curva(c, t, C["s14.c"], P, f4, 0, 10, d=1.2, cor=TINTA)
    E.ponto(c, t, C["s14.c"] + 1.0, P, 0, 1.2, cor=TINTA, r=12)
    E.ponto(c, t, C["s14.c"] + 1.3, P, 5, 0.8, guias=True, cor=E.COR, r=12)
    E.frase(c, t, C["s14.d"], [("1", "g", 48, COR)] + ps("consumo do", "b", 48) + [("N₂O₅", "g", 48)], 1250, 480, passo=0.08)
    E.frase(c, t, C["s14.e"], [("2", "g", 48, COR)] + ps("formação do", "b", 48) + [("NO₂", "g", 48)], 1250, 570, passo=0.08)
    E.frase(c, t, C["s14.f"], [("3", "g", 48, COR)] + ps("a da reação", "b", 48), 1250, 660, passo=0.08)
    E.relogio(c, t, C["s15.a"], cx=1560, cy=830, r=70)


def b_r4(c, t, C, b):
    cab_q(c, t, C["s16"] - 0.6, 4)
    Q.formula(c, "2 N2O5 -> 4 NO2 + O2", 1180, 220, 64, cores={"coef": E.COR})
    P = plano4(c, t, C["s16"] - 0.6)
    E.curva(c, t, C["s16"] - 0.6, P, f4, 0, 10, d=0.1, cor=TINTA)
    E.ponto(c, t, C["s16"] - 0.6, P, 5, 0.8, guias=True, cor=E.COR, r=12)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.formula(c, "f{1,2 − 0,8}{5} =", 1520, 420, 60, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s16.c"], "0,08", 1630, 400, 70, 46)
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.formula(c, "NO₂: 0,08 × f{4}{2} =", 1520, 620, 60, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s16.e"], "0,16", 1630, 600, 70, 46)
    E.foco(c, t, C["s16.f"], 0.4, lambda a: E.formula(c, "reação: f{0,08}{2} =", 1520, 820, 60, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s16.g"], "0,04", 1630, 800, 70, 46)
    E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: E.escreve(c, "mol/L por minuto", 1250, 1020, 46, "i", TINTA2, a))


# ---------------- questão 5: ordem ----------------
T5 = [("1", "0,1", "0,1", "3"), ("2", "0,2", "0,1", "12"), ("3", "0,2", "0,2", "24")]


def b_q5(c, t, C, b):
    cab_q(c, t, C["s17.a"], 5)
    Q.formula_em(c, t, C["s17.b"], "2 NO + Cl2 -> 2 NOCl", 1100, 150, 64)
    tabela(c, t, C["s17.b"] + 0.4, ("exp.", "[NO]", "[Cl2]", "v"), T5, 200, 330, (180, 260, 260, 220), dy=130, size=62,
           destaque=(0, 1) if C["s17.c"] <= t < C["s17.d"] else (1, 2) if t >= C["s17.d"] else ())
    E.frase(c, t, C["s17.e"], ps("a lei da velocidade?", "b", 52), 1250, 450, passo=0.08)
    E.frase(c, t, C["s17.f"], ps("e o k, se esquentar?", "b", 52), 1250, 550, passo=0.08)
    E.relogio(c, t, C["s18.a"], cx=1560, cy=800, r=90)


def b_r5(c, t, C, b):
    cab_q(c, t, C["s19"] - 0.6, 5)
    xs, ys = tabela(c, t, C["s19"] - 0.6, ("exp.", "[NO]", "[Cl2]", "v"), T5, 200, 330, (180, 260, 260, 220), dy=130, size=62,
                    destaque=(0, 1) if t < C["s19.c"] else (1, 2) if t < C["s19.e"] else ())
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.formula(c, "NO × 2 → v × 4: ordem 2", 1180, 400, 54, "g", TINTA, a))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.formula(c, "Cl₂ × 2 → v × 2: ordem 1", 1180, 500, 54, "g", TINTA, a))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: Q.formula(c, "v = k · [NO]^{2} · [Cl2]", 1150, 660, 62, TINTA, a, cores={"carga": E.COR}))
    pilula_em(c, t, C["s19.f"], "esquentou: mais colisões efetivas", 1440, 820, 44, E.COR)
    pilula_em(c, t, C["s19.g"], "o k aumenta", 1440, 920, 50, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s21"]:
        E.frase(c, t, C["s20.a"], ps("acertou três das cinco?", "i", 80), W / 2, 400, "center", 0.12)
        E.frase(c, t, C["s20.a"] + 1.4, [("a trilha está no lugar", "g", 80, COR)], W / 2, 540, "center")
        E.frase(c, t, C["s20.b"], ps("errou alguma? volte na aula daquela ferramenta", "i", 60, TINTA2), W / 2, 740, "center", 0.1)
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("trilha", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("equilíbrio", "g", 120, COR), ("químico", "g", 120)], XE, 420)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: Q.formula(c, "N2O4 <=> 2 NO2", XE, 590, 90, TINTA, a))
    E.frase(c, t, C["s21.b"] + 1.0, ps("ida e volta ao mesmo tempo", "i", 60, TINTA2), XE, 700, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
assert abs(f4(5) - 0.8) < 1e-9 and abs(f4(0) - 1.2) < 1e-9
