"""Visual — Estudativo · QUI-TER-004: velocidade média de uma reação. Primeira aula do módulo Cinética química.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho da QUI-MIS-001) e a da trilha (cabeçalho da QUI-TER-001).
LINGUAGEM VISUAL DA CINÉTICA (QUI-TER-004 a 008 copiam daqui):
- TABELA DE TEMPO (tabela): cabeçalho em itálico cinza, valores na grotesca; a linha da vez ganha fundo turquesa claro;
  a diferença entre duas linhas aparece à direita com uma chave e "−0,3" em TINTA2.
- GRÁFICO CONCENTRAÇÃO × TEMPO: E.plano sem grade forte; REAGENTE em tinta (curva que desce), PRODUTO na cor da matéria
  (curva que sobe). Leitura de ponto com E.ponto(guias=True). O intervalo Δt é uma chave embaixo do eixo.
- VELOCIDADE: fórmula "v = Δ[ ] / Δt" com E.formula (fração f{}{}); o resultado sai na esfera com a unidade ao lado
  ("mol/L·min"). Concentração sempre entre colchetes, com Q.formula ("[H2O2]").
- Velocidade de cada substância ao lado da equação, embaixo de cada espécie (Q.sob_termos), na cor da espécie.
Peças candidatas ao kit: tabela (tabela de dados com linha destacada), curva_pts (curva suave por pontos de tabela).
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
ARQUIVO_FINAL = "estudativo_QUI-TER-004_velocidade_media_reacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "tabela", "grafico", "coef", "atalho", "questao", "fim"))
BR = "#FFFFFF"

TEMPO = (0, 10, 20, 30)
H2O2 = (0.80, 0.50, 0.30, 0.20)
O2 = (0.00, 0.15, 0.25, 0.30)
# as contas da aula
assert all(abs((H2O2[0] - H2O2[k]) / 2 - O2[k]) < 1e-9 for k in range(4))   # O₂ formado = metade do H₂O₂ gasto
assert abs((0.80 - 0.50) / 10 - 0.03) < 1e-9 and abs((0.50 - 0.30) / 10 - 0.02) < 1e-9 and abs((0.30 - 0.20) / 10 - 0.01) < 1e-9
assert abs(0.15 / 10 - 0.015) < 1e-9 and abs(0.03 / 2 - 0.015) < 1e-9 and abs(0.2 / 20 - 0.01) < 1e-9
assert abs(0.4 / 5 - 0.08) < 1e-9 and abs(0.08 * 3 / 2 - 0.12) < 1e-9 and abs(0.08 / 2 - 0.04) < 1e-9
assert Q.lados("2 H2O2 -> 2 H2O + O2")[0] == Q.lados("2 H2O2 -> 2 H2O + O2")[1]
assert Q.lados("N2 + 3 H2 -> 2 NH3")[0] == Q.lados("N2 + 3 H2 -> 2 NH3")[1]


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


def vir(v, casas=2):
    """0.8 → '0,80'"""
    return f"{v:.{casas}f}".replace(".", ",")


def tabela(c, t, t0, cab, linhas, x, y, wcols, dy=96, size=60, tl=None, destaque=None, escuro=False):
    """tabela de dados: cab = textos do cabeçalho (Q.formula), linhas = listas de textos; tl = instante de cada linha;
    destaque = índice da linha com fundo turquesa claro. Devolve o y da linha de base de cada linha"""
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.4)
    if q <= 0:
        return []
    xs = [x + sum(wcols[:k]) + wcols[k] / 2 for k in range(len(wcols))]
    for k, s in enumerate(cab):
        Q.formula(c, s, xs[k], y, size * 0.8, TINTA2 if not escuro else CLARO, q, "center")
    M.line(c, x, y + size * 0.4, x + sum(wcols), y + size * 0.4, TINTA2, 0.6 * q, 3)
    ys = []
    for i, lin in enumerate(linhas):
        yy = y + size * 0.4 + (i + 1) * dy - dy * 0.3
        ys.append(yy)
        ti = tl[i] if tl else t0 + 0.3 + 0.2 * i
        if destaque is not None and i in (destaque if isinstance(destaque, tuple) else (destaque,)):
            M.rrect(c, x - 10, yy - size * 0.95, sum(wcols) + 20, size * 1.3, 14, E.mix(E.COR, "#FFFFFF", 0.78), ep(t, ti, 0.3))
        for k, s in enumerate(lin):
            E.foco(c, t, ti + 0.05 * k, 0.4, lambda a, s=s, k=k, yy=yy: E.formula(c, s, xs[k], yy, size, "g", tinta, a, "center"))
    return ys


def curva_pts(pts):
    """função suave (Catmull-Rom) que passa pelos pontos (x, y) de uma tabela"""
    def f(x):
        if x <= pts[0][0]:
            return pts[0][1]
        for i in range(len(pts) - 1):
            x0, x1 = pts[i][0], pts[i + 1][0]
            if x <= x1:
                u = (x - x0) / (x1 - x0)
                p0 = pts[max(i - 1, 0)][1]; p1 = pts[i][1]; p2 = pts[i + 1][1]; p3 = pts[min(i + 2, len(pts) - 1)][1]
                return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)
        return pts[-1][1]
    return f


FV = "v = f{Δ[ ]}{Δt}"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.bequer(c, t, C["s01.a"], 1450, 900, 340, 400, 0.7, Q.AGUA, graduacao=False, rotulo=None)
        E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: Q.formula(c, "H2O2", 1450, 620, 80, TINTA, a, "center"))
        for k in range(10):  # bolhas de O₂ subindo, primeiro muitas, depois poucas
            ritmo = 1.0 if t < C["s01.c"] else max(0.25, 1 - 0.5 * (t - C["s01.c"]))
            if k / 10 > ritmo:
                continue
            ph = ((t * 0.5 + k * 0.37) % 1.0)
            if t > C["s01.a"] + 0.8:
                c.drawCircle(1340 + (k * 47 % 220), 880 - ph * 240, 9, M.paint(TINTA2, 0.6 * (1 - ph), stroke=3))
        E.frase(c, t, C["s01.a"], ps("a água oxigenada vira", "i", 66), XE, 250, passo=0.1)
        Q.formula_em(c, t, C["s01.a"] + 1.0, "2 H2O2 -> 2 H2O + O2", XE, 390, 80)
        E.frase(c, t, C["s01.b"], ps("não no mesmo ritmo:", "i", 66), XE, 560, passo=0.1)
        E.frase(c, t, C["s01.c"], [("rápido", "g", 66, COR)] + ps("no começo,", "i", 66) + [("devagar", "g", 66)] + ps("depois", "i", 66), XE, 660, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("como medir a", "i", 70) + [("rapidez?", "g", 66, COR)], XE, 850, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], [("velocidade", "g", 110, COR), ("média", "g", 110)], XE, 300, passo=0.14)
    E.foco(c, t, C["s02.a"] + 1.0, 0.4, lambda a: E.formula(c, "mol/L por minuto", XE, 410, 60, "g", TINTA2, a))
    lista(c, t, [(C["s02.b"], [("de", "i", 74), ("uma", "i", 74), ("tabela", "g", 70)]),
                 (C["s02.c"], [("de", "i", 74), ("um", "i", 74), ("gráfico", "g", 70)])], XE, 600, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 220, passo=0.12)
    lista(c, t, [(C["s03.a"], [("concentração", "g", 64, COR)] + ps("em mol por litro", "i", 68)),
                 (C["s03.b"], [("velocidade média", "g", 64, COR)] + ps("= quanto mudou, dividido pelo tempo", "b", 56, TINTA2))], XE, 400, 200)
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "f{180 km}{2 h} = 90 km/h", XE + 110, 830, 80, "g", TINTA, a))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("na reação, o que muda é a", "i", 70) + [("concentração", "g", 66, COR)], XE, 220, passo=0.1)
            # partículas: reagente (tinta) sumindo, produto (turquesa) aparecendo
            k = ep(t, C["s04.b"], 4.0)
            Q.bequer(c, t, C["s04"], W / 2, 860, 420, 440, 0.75, Q.AGUA, graduacao=False,
                     particulas=dict(n=50, estado="liquido", tipos=[("#3A3B40", 1 - 0.8 * k), (E.COR, 0.05 + 0.8 * k)], r=12, semente=3))
            E.foco(c, t, C["s04.b"], 0.4, lambda a: (E.bola(c, 420, 560, 22, "#3A3B40", a), E.escreve(c, "reagente some", 460, 575, 52, "i", TINTA, a)))
            E.foco(c, t, C["s04.c"], 0.4, lambda a: (E.bola(c, 1360, 560, 22, E.COR, a), E.escreve(c, "produto aparece", 1400, 575, 52, "i", COR, a)))
            E.frase(c, t, C["s04.d"], ps("quanto mudou, dividido pelo tempo", "b", 60), W / 2, 1000, "center", 0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    E.frase(c, t, C["s05.a"], ps("concentração entre", "i", 70) + [("colchetes", "g", 66, COR)], XE, 220, passo=0.12)
    Q.formula_em(c, t, C["s05.b"], "[H2O2]", XE, 400, 130, cores={"carga": E.COR})
    E.foco(c, t, C["s05.b"] + 0.6, 0.4, lambda a: E.escreve(c, "concentração da água oxigenada", XE + 520, 390, 56, "i", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, FV, W / 2, 680, 130, "g", TINTA, a, "center"))
    E.foco(c, t, C["s05.c"] + 0.8, 0.4, lambda a: (E.escreve(c, "Δ = variação", 1240, 620, 50, "b", COR, a)))
    pilula_em(c, t, C["s05.d"], "sempre positiva: quanto mudou, sem sinal", W / 2, 920, 50, E.COR)


# ---------------- tabela ----------------
TX, TY = 170, 290


def tab_h2o2(c, t, t0, tl=None, destaque=None):
    return tabela(c, t, t0, ("tempo (min)", "[H2O2] (mol/L)"), [[str(TEMPO[k]), vir(H2O2[k])] for k in range(4)], TX, TY, (300, 400),
                  dy=125, size=60, tl=tl, destaque=destaque)


def b_tabela(c, t, C, b):
    dest = (0, 1) if C["s07"] <= t < C["s08"] else (1, 2) if C["s08"] <= t < C["s08.c"] else (2, 3) if C["s08.c"] <= t < C["s08.d"] else None
    ys = tab_h2o2(c, t, C["s06"], tl=[C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]], destaque=dest)
    if not ys:
        return
    xr = TX + 700 + 30
    for k, (tt, v, cor) in enumerate(((C["s07.b"], "−0,30", TINTA2), (C["s08.a"], "−0,20", TINTA2), (C["s08.c"], "−0,10", TINTA2))):
        if t >= tt:
            q = ep(t, tt, 0.4)
            M.line(c, xr, ys[k] - 20, xr + 30, ys[k] - 20, TINTA2, q, 4)
            M.line(c, xr + 30, ys[k] - 20, xr + 30, ys[k + 1] - 20, TINTA2, q, 4)
            M.line(c, xr, ys[k + 1] - 20, xr + 30, ys[k + 1] - 20, TINTA2, q, 4)
            E.foco(c, t, tt, 0.4, lambda a, k=k, v=v: E.formula(c, v, xr + 60, (ys[k] + ys[k + 1]) / 2 - 2, 52, "g", TINTA2, a))
    # as contas à direita
    xc = 1180
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "v = f{0,30}{10} =", xc, 420, 76, "g", TINTA, a))
    wv = E.formula(None, "v = f{0,30}{10} =", 0, 0, 76, a=0)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "0,030", xc + wv + 20, 420, 76, "g", COR, a))
    E.foco(c, t, C["s07.d"] + 0.4, 0.4, lambda a: E.escreve(c, "mol/L por minuto", xc, 500, 46, "i", TINTA2, a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "10 a 20 min: 0,020", xc, 640, 66, "g", TINTA, a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "20 a 30 min: 0,010", xc, 750, 66, "g", TINTA, a))
    if t >= C["s08.d"]:
        pilula_em(c, t, C["s08.d"] + 0.3, "a velocidade cai", 1500, 880, 52, TINTA)


# ---------------- gráfico ----------------
def plano_g(c, t, t0, d=0.6):
    return E.plano(c, t, t0, 300, 220, 900, 640, 0, 30, 0, 0.9, passo=10, passo_y=0.3, marcas_x=[0, 10, 20, 30],
                   marcas_y=[0.3, 0.6, 0.9], nomes=("", ""), size=40, d=d)


def b_grafico(c, t, C, b):
    P = plano_g(c, t, C["s09.b"] - 0.3)
    fr = curva_pts(list(zip(TEMPO, H2O2)))
    fp = curva_pts(list(zip(TEMPO, O2)))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "tempo (min)", 960, 960, 50, "i", TINTA2, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "concentração (mol/L)", 330, 180, 50, "i", TINTA2, a))
    E.curva(c, t, C["s09.d"], P, fr, 0, 30, d=1.4, cor=TINTA, rotulo=None)
    E.foco(c, t, C["s09.d"] + 1.0, 0.4, lambda a: Q.formula(c, "H2O2", P.x(30) + 30, P.y(0.2) + 16, 50, TINTA, a))
    E.curva(c, t, C["s09.e"], P, fp, 0, 30, d=1.4, cor=E.COR, rotulo=None)
    E.foco(c, t, C["s09.e"] + 1.0, 0.4, lambda a: Q.formula(c, "O2", P.x(30) + 30, P.y(0.3) - 20, 50, COR, a))
    for k in range(4):
        if t >= C["s09.e"] + 1.2:
            E.ponto(c, t, C["s09.e"] + 1.2 + 0.1 * k, P, TEMPO[k], O2[k], cor=E.COR, r=10)
        if t >= C["s09.d"] + 1.2:
            E.ponto(c, t, C["s09.d"] + 1.2 + 0.1 * k, P, TEMPO[k], H2O2[k], cor=TINTA, r=10)
    E.frase(c, t, C["s09.f"], ps("leia 2 pontos", "b", 52) , 1400, 330, passo=0.1)
    E.frase(c, t, C["s09.f"] + 0.8, ps("dividido pelo tempo", "b", 52, COR), 1400, 410, passo=0.1)
    if t >= C["s10.a"]:
        E.ponto(c, t, C["s10.b"], P, 10, 0.15, guias=True, valores=False, cor=E.COR, r=14)
        E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: E.formula(c, "0,15", P.ox - 20, P.y(0.15) + 14, 40, "g", COR, a, "right"))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "f{0,15}{10} = 0,015", 1400, 600, 72, "g", COR, a))
        pilula_em(c, t, C["s10.d"], "metade de 0,030", 1600, 740, 50, TINTA)


# ---------------- coeficientes ----------------
EQ = "2 H2O2 -> 2 H2O + O2"


def b_coef(c, t, C, b):
    cs = Q.equacao(c, t, C["s11.a"], EQ, W / 2, 280, 110, tl=[C["s11.a"] + 0.25 * k for k in range(5)], cores={"coef": E.COR})
    for k, s_ in enumerate(("0,030", "0,030", "0,015")):
        E.foco(c, t, C["s11.c"] + 0.3 * k, 0.4, lambda a, k=k, s_=s_: (E.formula(c, s_, cs[k], 420, 60, "g", TINTA, a, "center")))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "a cada 2 que somem, nasce 1", 560, 560, 56, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "mol/L por minuto", cs[2] + 120, 425, 40, "i", TINTA2, a))
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "v da reação = f{v da substância}{coeficiente}", W / 2, 740, 76, "g", TINTA, a, "center"))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "f{0,030}{2} =", 820, 940, 76, "g", TINTA2, a, "right"))
    bola_txt(c, t, C["s12.c"], "0,015", 960, 912, 96, 52)
    pilula_em(c, t, C["s12.d"], "o mesmo para todas", 1380, 912, 50, TINTA)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    tab_h2o2(c, t, C["s13"] - 0.4, destaque=(1, 2))
    E.frase(c, t, C["s13.a"], [("cuidado:", "g", 66, ERRADO)] + ps("divida pelo intervalo", "i", 70), XE, 160, passo=0.1)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "queda: 0,20", 1000, 400, 70, "g", TINTA, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "f{0,20}{20} = 0,010", 1000, 560, 76, "g", ERRADO, a))
    if t >= C["s13.c"] + 0.8:
        E.risco(c, 990, 580, 1600, 480, t, C["s13.c"] + 0.8, largura=10)
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.formula(c, "20 − 10 = 10 min", 1000, 700, 66, "g", TINTA2, a))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "f{0,20}{10} = 0,020", 1000, 870, 76, "g", COR, a))
    E.foco(c, t, C["s13.e"] + 0.4, 0.4, lambda a: E.selo(c, 1700, 840, 44, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14.a"], ps("achou uma, achou", "i", 72, CLARO) + [("todas", "g", 68, BR)], W / 2, 170, "center", 0.12)
            E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "v(quero) = v(tenho) × f{coef. quero}{coef. tenho}", W / 2, 360, 72, "g", BR, a, "center"))
            Q.formula_em(c, t, C["s14.c"], EQ, W / 2, 560, 90, align="center", cores={"coef": E.CLARO}, escuro=True)
            E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "O₂: 0,030 × f{1}{2} = 0,015", W / 2, 740, 76, "g", CLARO, a, "center"))
            E.foco(c, t, C["s14.f"], 0.5, lambda a: E.formula(c, "f{mol/L}{min} = mol/L por minuto", W / 2, 940, 66, "g", BR, a, "center"))
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("a equação balanceada fixa a", "i", 70, CLARO) + [("proporção", "g", 66, BR)], W / 2, 360, "center", 0.12)
    E.frase(c, t, C["s15.b"], [("sem balancear,", "g", 66, ERRADO)] + ps("não vale", "i", 70, CLARO), W / 2, 560, "center", 0.12)
    pilula_em(c, t, C["s15.c"], "balanceie antes", W / 2, 720, 60, E.COR)


# ---------------- questão ----------------
EQN = "N2 + 3 H2 -> 2 NH3"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 150)
    Q.formula_em(c, t, C["s16.a"], EQN, XE, 320, 100)
    E.foco(c, t, C["s16.a"] + 0.6, 0.4, lambda a: E.escreve(c, "a produção da amônia", XE, 410, 50, "i", TINTA2, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "[NH₃]: 0 → 0,4 mol/L em 5 min", XE, 540, 70, "g", TINTA, a))
    E.frase(c, t, C["s16.c"], [("1", "g", 56, COR)] + ps("velocidade de formação da amônia?", "i", 58), XE, 700, passo=0.08)
    E.frase(c, t, C["s16.d"], [("2", "g", 56, COR)] + ps("de consumo do", "i", 58) + [("H₂?", "g", 54)], XE, 800, passo=0.08)
    E.frase(c, t, C["s16.d"] + 1.4, [("3", "g", 56, COR)] + ps("e a da reação?", "i", 58), XE, 900, passo=0.08)
    E.relogio(c, t, C["s17.a"], cx=1550, cy=640, r=150)


def b_resposta(c, t, C, b):
    cs = Q.centros(EQN, W / 2, 240, 100, "center")
    Q.formula(c, EQN, W / 2, 240, 100, align="center", cores={"coef": E.COR})
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "v(NH₃) = f{0,4}{5} =", 900, 450, 76, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s18.b"], "0,08", 1030, 425, 84, 56)
    E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: E.escreve(c, "mol/L por minuto", 1140, 450, 48, "i", TINTA2, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "coeficientes: H₂ 3, NH₃ 2", 300, 620, 62, "g", TINTA2, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "v(H₂) = 0,08 × f{3}{2} =", 900, 780, 76, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s18.e"], "0,12", 1030, 755, 84, 56)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "v(reação) = f{0,08}{2} =", 900, 960, 70, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s19.c"], "0,04", 1030, 937, 76, 50)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, FV, W / 2, 420, 130, "g", TINTA, a, "center"))
        E.frase(c, t, C["s20.b"], ps("os", "i", 70) + [("coeficientes", "g", 66, COR)] + ps("ligam as substâncias", "i", 70), W / 2, 720, "center", 0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("colisões", "g", 110, COR), ("e", "i", 110), ("fatores", "g", 110)], XE, 420)
    E.frase(c, t, C["s21.b"], ps("o comprimido em pó", "i", 64, TINTA2), XE, 560, passo=0.1)
    E.frase(c, t, C["s21.c"], ps("e a geladeira", "i", 64, TINTA2), XE, 650, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 825, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, tabela=b_tabela, grafico=b_grafico, coef=b_coef, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
