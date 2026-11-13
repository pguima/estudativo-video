"""Visual — Estudativo · QUI-ORG-001: o carbono e as fórmulas orgânicas. Primeira aula da Química Orgânica.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho da QUI-MIS-001 (turquesa, Q.formula, bolinhas CPK, palco só no atalho).
LINGUAGEM VISUAL DA ORGÂNICA (todas as aulas QUI-ORG-* copiam daqui; as peças marcadas [kit] são candidatas a quimica.py):
- CADEIA EM BASTÃO = Q.bastao em tinta (largura 7), escala 120 a 190, sempre com Q.zigzag(n) ou anel(6) desta aula. É a forma
  principal da trilha: a fórmula condensada fica em cima ou ao lado, menor. Heteroátomos escritos nas cores CPK (O vermelho,
  N azul, S amarelo-escuro, Cl verde), como o Q.bastao já faz.
- CARBONO ESCONDIDO: quando a aula conta ou numera carbonos, cada vértice ganha a bolinha turquesa numerada (Q.bastao(numeros=t)).
  O número da bolinha é o mesmo da numeração oficial quando a aula numera a cadeia.
- HIDROGÊNIO ESCONDIDO [kit]: hs() — rótulo "H₃", "H₂", "H" em cinza (TINTA2), por fora do vértice, do lado oposto aos vizinhos.
  Na hora em que a fala conta aquele carbono, o rótulo sai na cor da matéria (COR_TEXTO). Rótulo errado = vermelho + E.risco.
- LIGAÇÃO QUE CONTA [kit]: realce() — o traço ganha por cima uma faixa larga turquesa clara; a ligação dupla conta como duas faixas.
- CADEIA PRINCIPAL (QUI-ORG-004): realce() em todos os traços da maior fila; galhos ficam em tinta.
- GRUPO FUNCIONAL [kit] (módulo Funções, QUI-ORG-006+): halo() — mancha turquesa translúcida atrás dos átomos do grupo, com a
  pílula da função (E.pilula, fundo E.COR) ao lado. Um grupo por vez na cor da matéria; os já vistos ficam com halo cinza.
- FÓRMULA ESTRUTURAL completa = Q.lewis sem pares livres. CONDENSADA = cond() [kit]: grupos "CH3", "CH2", "OH" na grotesca,
  com traço "–" entre eles e galhos em cima/embaixo.
- NOME OFICIAL na tela (QUI-ORG-003+): nome() [kit] — peças do nome lado a lado, prefixo em COR_TEXTO, infixo em tinta,
  sufixo em cinza; cada peça com a legenda pequena embaixo ("carbonos", "ligação", "função").
- O "1" implícito, contas de H e a esfera de resposta seguem a QUI-MIS-001.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-001_carbono_formulas_organicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carbono", "formas", "contar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# contas da aula, refeitas pelo kit
assert Q.contar("C5H12") == {"C": 5, "H": 12} and 3 + 2 + 2 + 2 + 3 == 12 and 2 * 5 + 2 == 12
assert 2 + 1 + 2 + 3 == 8 and 2 * 4 + 2 - 2 == 8 and 3 + 2 + 2 + 3 == 10
assert Q.contar("CH3CH2OH") == Q.contar("C2H6O") and 2 * 2 + 2 == 6
assert 3 + 2 + 1 + 1 + 2 + 1 == 10 and 2 * 5 + 2 - 2 == 10 and Q.contar("CH3CH2CHCHCH2OH") == {"C": 5, "H": 10, "O": 1}


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (candidatas ao kit) ----------------
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
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def pts_tela(pts, cx, cy, esc):
    return [(cx + x * esc, cy + y * esc) for x, y in pts]


def anel(n=6, r=1.0, rot=90):
    return [(r * math.cos(math.radians(rot + 360 * k / n)), -r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]


def hs(c, t, t0, P, i, viz, n, size=50, cor=TINTA2, dist=None, a_max=1.0):
    """[kit] hidrogênios escondidos do vértice i: rótulo H₃/H₂/H por fora, do lado oposto aos vizinhos"""
    if n <= 0 or t < t0:
        return
    ux = uy = 0.0
    for j in viz:
        dx, dy = P[j][0] - P[i][0], P[j][1] - P[i][1]
        L = math.hypot(dx, dy) or 1
        ux, uy = ux + dx / L, uy + dy / L
    L = math.hypot(ux, uy)
    ux, uy = (-ux / L, -uy / L) if L > 0.2 else (0, -1)
    dist = dist or size * 1.15
    x, y = P[i][0] + ux * dist, P[i][1] + uy * dist
    s = "H" if n == 1 else f"H{n}"
    E.foco(c, t, t0, 0.4, lambda a: Q.formula(c, s, x, y + size * 0.36, size, cor, a * a_max, "center"), sobe=8)


def realce(c, t, t0, A, B, cor=None, d=0.4, largura=22, alfa=0.45):
    """[kit] faixa clara por cima de uma ligação do bastão (a ligação que conta, a cadeia principal)"""
    p = ease_io(prog(t, t0, d))
    if p > 0:
        M.line(c, A[0], A[1], B[0], B[1], cor or E.COR, alfa, largura, progress=p)


def halo(c, t, t0, pts, r=70, cor=None, alfa=0.25):
    """[kit] mancha translúcida atrás de um grupo funcional"""
    a = ep(t, t0, 0.5) * alfa
    if a <= 0:
        return
    lay = skia.Paint()
    lay.setAlphaf(a)
    lay.setImageFilter(skia.ImageFilters.Blur(r * 0.18, r * 0.18))
    c.saveLayer(None, lay)
    k = ease_back(prog(t, t0, 0.5))
    for x, y in pts:
        c.drawCircle(x, y, r * k, M.paint(cor or E.COR))
    c.restore()


def valencia(c, s, cx, cy, n, size=90, a=1.0, cor=None, comp=70):
    """símbolo com n tracinhos em volta: quantas ligações o átomo faz"""
    if a <= 0:
        return
    angs = {1: [0], 2: [0, 180], 3: [0, 120, 240], 4: [0, 90, 180, 270]}[n]
    r0 = size * 0.62
    for g in angs:
        ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
        M.line(c, cx + ux * r0, cy + uy * r0, cx + ux * (r0 + comp), cy + uy * (r0 + comp), cor or TINTA, a, 7)
    centro(c, s, cx, cy + size * 0.36, size, "g", Q.cor_el(s) if s in "ONS" else TINTA, a)


def estrela(c, cx, cy, ordens, a=1.0, size=80, comp=80):
    """um carbono com as ligações dadas (ordens = [1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1])"""
    if a <= 0:
        return
    angs = {4: [90, 0, 270, 180], 3: [180, 30, -30], 2: [180, 0]}[len(ordens)]
    r0 = size * 0.6
    for g, o in zip(angs, ordens):
        ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
        nx, ny = -uy, ux
        for k in {1: (0,), 2: (-0.5, 0.5), 3: (-1, 0, 1)}[o]:
            off = k * 16
            M.line(c, cx + ux * r0 + nx * off, cy + uy * r0 + ny * off, cx + ux * (r0 + comp) + nx * off, cy + uy * (r0 + comp) + ny * off,
                   TINTA, a, 7)
    centro(c, "C", cx, cy + size * 0.36, size, "g", TINTA, a)


def bastao_viz(n, ligs=None):
    ligs = ligs or [(i, i + 1) for i in range(n - 1)]
    v = {i: [] for i in range(n)}
    for i, j in ligs:
        v[i].append(j); v[j].append(i)
    return v


# ---------------- gancho ----------------
GX, GY, GE = W / 2 + 120, 560, 190
PENT = Q.zigzag(5)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        E.frase(c, t, a1, ps("este zigue-zague é uma", "i", 80) + [("molécula", "g", 76, COR)], XE, 190, passo=0.12)
        Q.bastao(c, t, a1 + 0.3, PENT, GX, GY, GE, d=1.2, numeros=b1 + 0.2, passo_n=0.18)
        P = pts_tela(PENT, GX, GY, GE)
        viz = bastao_viz(5)
        for i, n in enumerate((3, 2, 2, 2, 3)):
            hs(c, t, c1 + 0.2 + 0.15 * i, P, i, viz[i], n, 60, COR, dist=100)
        E.frase(c, t, b1, [("5", "g", 84, COR), ("carbonos", "i", 84)], XE, 870, passo=0.12)
        E.frase(c, t, c1, [("12", "g", 84, COR), ("hidrogênios", "i", 84), ("escondidos", "g", 76)], XE + 520, 870, passo=0.12)
        E.frase(c, t, d1, ps("onde eles estão?", "i", 80), W / 2, 1000, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 520, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("achar", "g", 70), ("cada", "i", 74), ("carbono", "g", 70, COR)]),
                 (C["s02.c"], [("contar", "g", 70), ("os", "i", 74), ("H", "g", 70, COR), ("escondidos", "i", 74)]),
                 (C["s02.d"], [("chegar", "g", 70), ("à", "i", 74), ("fórmula", "g", 70)]),
                 (C["s02.e"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 430, 160)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembra da", "i", 80) + [("estrutura de Lewis?", "g", 74, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("cada", "i", 70), ("traço", "g", 66), ("=", "g", 66, TINTA2)] + ps("um par de elétrons compartilhado", "i", 66), XE, 360, passo=0.1)
    linhas = ((C["s03.a"] + 0.6, 1, "simples"), (C["s03.b"], 2, "dupla"), (C["s03.c"], 3, "tripla"))
    for k, (ti, o, nome) in enumerate(linhas):
        y = 560 + k * 170
        Q.lewis(c, t, ti, [("C", 0, 0), ("C", 1.6, 0)], [(0, 1, o)], XE + 120, y, escala=150, size=96)
        E.frase(c, t, ti + 0.4, [(nome, "i", 72)], XE + 520, y + 26)
    E.foco(c, t, C["s03.c"] + 0.8, 0.6, lambda a: E.simbolo(c, 1550, 640, 170 * a, giro=-6 * math.sin(t * 0.5)), blur=0)
    E.foco(c, t, C["s03.c"] + 1.2, 0.4, lambda a: centro(c, "faltou a aula? procure no canal", 1550, 900, 44, "i", TINTA2, a))


# ---------------- o carbono ----------------
def b_carbono(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("a Química Orgânica estuda", "i", 76), XE, 240, passo=0.12)
            E.frase(c, t, C["s04.a"] + 1.2, [("os compostos do", "i", 84), ("carbono", "g", 110, COR)], XE, 400, passo=0.14)
            for k, (key, s) in enumerate((("s04.b", "combustível"), ("s04.c", "comida"), ("s04.d", "remédio"))):
                x = XE + 40 + [0, 360, 640][k]
                E.foco(c, t, C[key], 0.4, lambda a, s=s, x=x: E.pilula(c, s, x + (E.larg(s, "i", 54) + 60) / 2, 560, 54, "i", fundo=TINTA, a=a))
            E.frase(c, t, C["s04.e"] - 0.6, ps("tudo começa num número:", "i", 70, TINTA2), XE, 800, passo=0.1)
            E.foco(c, t, C["s04.e"] - 0.3, 0.6, lambda a: E.escreve(c, "4", 1380, 900, 560, "g", COR, a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05"], [("carbono:", "i", 80), ("Z = 6", "g", 76, COR)], XE, 230, passo=0.14)
            E.frase(c, t, C["s05.a"], [("2", "g", 76, TINTA2), ("na 1ª camada", "i", 70, TINTA2)], XE, 380, passo=0.12)
            E.frase(c, t, C["s05.b"], [("4", "g", 76, COR), ("na camada de valência", "i", 70)], XE, 490, passo=0.12)
            E.frase(c, t, C["s05.c"], ps("cada um faz uma ligação", "i", 70), XE, 640, passo=0.1)
            E.frase(c, t, C["s05.d"], [("sempre", "i", 84), ("4 ligações", "g", 90, COR)], XE, 820, passo=0.14)

            def atomo():
                Q.bohr(c, t, C["s05"] + 0.3, 1450, 520, camadas_=[2, 4], r0=120, dr=90, s="C", te=[C["s05.a"], C["s05.b"]])
            E.saida(c, t, C["s05.d"] - 0.2, atomo)
            if t >= C["s05.d"]:
                E.foco(c, t, C["s05.d"], 0.5, lambda a: valencia(c, "C", 1450, 540, 4, 150, a, comp=110))
                for k in range(4):
                    g = [0, 90, 180, 270][k]
                    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
                    E.foco(c, t, C["s05.d"] + 0.4 + 0.15 * k, 0.3, lambda a, ux=ux, uy=uy, k=k: (
                        E.bola(c, 1450 + ux * 250, 540 + uy * 250, 34, a=a), centro(c, str(k + 1), 1450 + ux * 250, 540 + uy * 250 + 16, 42, "g", E.SOBRE, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("e os vizinhos mais comuns?", "i", 76), XE, 220, passo=0.12)
            for k, (key, s, n) in enumerate((("s06.b", "H", 1), ("s06.c", "O", 2), ("s06.d", "N", 3), ("s06.d", "C", 4))):
                cx = 330 + k * 420
                ti = C[key] + (0.8 if s == "C" else 0)
                E.foco(c, t, ti, 0.5, lambda a, s=s, n=n, cx=cx: valencia(c, s, cx, 560, n, 120, a, comp=80))
                E.foco(c, t, ti + 0.3, 0.4, lambda a, n=n, cx=cx, s=s: (E.escreve(c, str(n), cx - 110, 860, 120, "g", COR, a),
                                                                       E.escreve(c, "ligação" if n == 1 else "ligações", cx - 10, 850, 46, "i", TINTA, a)))
            E.frase(c, t, lerp(C["s06.d"], C["s07"], 0.6), ps("guarde esses números", "i", 60, TINTA2), W / 2, 1000, "center", 0.1)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    # s07: os quatro jeitos de fazer quatro ligações
    E.frase(c, t, C["s07.a"], ps("as 4 ligações podem vir de", "i", 72) + [("jeitos diferentes", "g", 68, COR)], XE, 200, passo=0.1)
    jeitos = (("s07.b", [1, 1, 1, 1], "1 + 1 + 1 + 1"), ("s07.c", [2, 1, 1], "2 + 1 + 1"), ("s07.d", [2, 2], "2 + 2"), ("s07.e", [3, 1], "3 + 1"))
    for k, (key, ords, conta) in enumerate(jeitos):
        cx = 330 + k * 420
        E.foco(c, t, C[key], 0.5, lambda a, ords=ords, cx=cx: estrela(c, cx, 520, ords, a, 96, 90))
        E.foco(c, t, C["s07.f"] + 0.3 * k, 0.4, lambda a, conta=conta, cx=cx: E.formula(c, conta + " = 4", cx, 800, 54, "g", COR, a, "center"))
    E.frase(c, t, C["s07.f"] + 1.4, [("dupla", "g", 60), ("conta", "i", 64), ("2,", "g", 60, COR), ("tripla", "g", 60), ("conta", "i", 64), ("3", "g", 60, COR)],
            W / 2, 980, "center", 0.1)


# ---------------- três jeitos de escrever ----------------
ETANOL = ([("C", 0, 0), ("C", 1, 0), ("O", 2, 0), ("H", -1, 0), ("H", 0, -1), ("H", 0, 1), ("H", 1, -1), ("H", 1, 1), ("H", 3, 0)],
          [(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 6, 1), (1, 7, 1), (2, 8, 1)])


def cond(c, t, t0, partes, x, y, size, cores=None, passo=0.25, align="left", traco="–"):
    """[kit] fórmula condensada em fila: partes = ["CH3", "CH2", "OH"], com o traço entre os grupos. Devolve as caixas (x0, x1)"""
    cores = cores or {}
    ws = [Q.formula(None, p, 0, 0, size) for p in partes]
    wt = Q.formula(None, traco, 0, 0, size)
    tot = sum(ws) + wt * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x
    caixas = []
    for k, (p, w) in enumerate(zip(partes, ws)):
        cor = cores.get(k)
        E.foco(c, t, t0 + k * passo, 0.4, lambda a, p=p, xx=xx, cor=cor: Q.formula(c, p, xx, y, size, cor, a))
        caixas.append((xx, xx + w))
        xx += w
        if k < len(partes) - 1:
            E.foco(c, t, t0 + k * passo + 0.15, 0.4, lambda a, xx=xx: Q.formula(c, traco, xx, y, size, TINTA2, a))
            xx += wt
    return caixas


def b_formas(c, t, C, b):
    E.frase(c, t, C["s08"], ps("três jeitos de escrever", "i", 64, TINTA2), XE, 150, passo=0.1)
    Q.formula_em(c, t, C["s08.a"], "C2H6O", 1750, 150, 76, align="right")
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.b"], [("1", "g", 64, COR), ("estrutural:", "g", 64)] + ps("todos os átomos e traços", "i", 64), XE, 280, passo=0.1)
            pts = Q.lewis(c, t, C["s08.b"] + 0.4, *ETANOL, 760, 640, escala=150, size=96, passo=0.12)
            for k, (key, quais, r) in enumerate((("s08.c", (0, 1), 84), ("s08.d", (2,), 84), ("s08.e", (3, 4, 5, 6, 7, 8), 56))):
                fim_ = C[("s08.d", "s08.e", "s09")[k]] - 0.1
                for j, i in enumerate(quais):
                    q = ep(t, C[key] + 0.08 * j, 0.3) * (1 - ep(t, fim_, 0.3))
                    if q > 0:
                        c.drawCircle(pts[i][0], pts[i][1], r, M.paint(E.COR, q, stroke=6))
            for k, (key, s) in enumerate((("s08.c", "C: 4 traços"), ("s08.d", "O: 2 traços"), ("s08.e", "H: 1 traço"))):
                E.foco(c, t, C[key] + 0.3, 0.4, lambda a, s=s, k=k: E.formula(c, s, 1380, 540 + k * 110, 60, "g", COR if k == 0 else TINTA, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09"] + 0.3, [("2", "g", 64, COR), ("condensada", "g", 64)], XE, 280, passo=0.1)
            cx_ = cond(c, t, C["s09.a"], ["CH3", "CH2", "OH"], W / 2, 600, 190, align="center", passo=0.35)
            if t >= C["s09.b"]:
                for k in range(2):
                    x0, x1 = cx_[k]
                    q = ep(t, C["s09.b"] + 0.3 * k, 0.4)
                    E.caixa_pontilhada(c, x0 - 14, 430, x1 - x0 + 28, 230, q, E.COR, prog_=q)
                E.frase(c, t, C["s09.b"] + 0.5, ps("os H vão junto do seu carbono", "i", 62), W / 2, 790, "center", 0.1)
            E.frase(c, t, C["s09.c"], ps("só ficam os traços entre os grupos", "i", 62, TINTA2), W / 2, 900, "center", 0.1)
            if t >= C["s09.c"]:
                for k in range(2):
                    x = cx_[k][1] + Q.formula(None, "–", 0, 0, 190) / 2
                    q = ep(t, C["s09.c"] + 0.6 + 0.2 * k, 0.3)
                    c.drawCircle(x, 540, 46, M.paint(E.COR, q, stroke=6))
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    # s10: bastão do etanol
    E.frase(c, t, C["s10"] + 0.2, [("3", "g", 64, COR), ("em bastão", "g", 64)] + ps("a mais curta", "i", 64, TINTA2), XE, 280, passo=0.1)
    pts = Q.zigzag(3)
    bx, by, be = 1180, 600, 210
    Q.bastao(c, t, C["s10.a"], pts, bx, by, be, rotulos={2: "OH"}, d=0.9)
    P = pts_tela(pts, bx, by, be)
    for k, (i, s) in enumerate(((0, "ponta"), (1, "dobra"))):
        E.foco(c, t, C["s10.b"] + 0.5 * k, 0.4, lambda a, i=i: (E.bola(c, P[i][0], P[i][1], 30, a=a), centro(c, "C", P[i][0], P[i][1] + 14, 36, "g", E.SOBRE, a)))
        E.foco(c, t, C["s10.b"] + 0.5 * k + 0.2, 0.4, lambda a, i=i, s=s: centro(c, s + " = C", P[i][0], P[i][1] + (-80 if i == 0 else 120), 50, "i", COR, a))

    def escondidos():
        viz = bastao_viz(3)
        hs(c, t, C["s10.c"], P, 0, viz[0], 3, 58, TINTA2, dist=110)
        hs(c, t, C["s10.c"] + 0.2, P, 1, viz[1], 2, 58, TINTA2, dist=170)
    E.saida(c, t, C["s10.c"] + 1.6, escondidos)
    if C["s10.c"] + 0.4 <= t < C["s10.d"]:
        E.frase(c, t, C["s10.c"] + 0.4, ps("os H do carbono não aparecem", "i", 58, TINTA2), XE, 900, passo=0.1)
    halo(c, t, C["s10.d"], [P[2]], 90)
    E.frase(c, t, C["s10.d"], ps("os outros átomos são escritos,", "i", 58), XE, 900, passo=0.1)
    E.frase(c, t, C["s10.e"], ps("com os H deles", "i", 58) + [("OH", "g", 54, Q.cor_el("O"))], XE, 990, passo=0.1)


# ---------------- contar os hidrogênios ----------------
CX, CY, CE = 1250, 560, 190


def b_contar(c, t, C, b):
    P = pts_tela(PENT, CX, CY, CE)
    viz = bastao_viz(5)
    E.frase(c, t, C["s11"], ps("como achar os H escondidos?", "i", 70), XE, 180, passo=0.12)
    E.frase(c, t, C["s11.a"], [("use o", "i", 74), ("4", "g", 110, COR)], XE, 360, passo=0.12)
    E.formula_em(c, t, C["s11.b"], "4 − ligações", XE, 500, 76, "g", TINTA)
    E.formula_em(c, t, C["s11.c"], "= H", XE + E.formula(None, "4 − ligações ", 0, 0, 76, a=0), 500, 76, "g", COR)
    Q.bastao(c, t, C["s11"] + 0.3, PENT, CX, CY, CE, d=0.8)
    # a ponta: uma ligação; as dobras: duas
    realce(c, t, C["s12.a"], P[0], P[1]); realce(c, t, C["s12.a"] + 0.2, P[4], P[3])
    hs(c, t, C["s12.b"], P, 0, viz[0], 3, 64, COR); hs(c, t, C["s12.b"] + 0.2, P, 4, viz[4], 3, 64, COR)
    E.frase(c, t, C["s12.a"], [("ponta:", "i", 60), ("1 ligação", "g", 56)], XE, 660, passo=0.1)
    E.frase(c, t, C["s12.b"], [("→", "g", 56, TINTA2), ("3 H", "g", 56, COR)], XE + 520, 660, passo=0.1)
    for k, i in enumerate((1, 2, 3)):
        realce(c, t, C["s12.c"] + 0.15 * k, P[i - 1], P[i], alfa=0.3)
        realce(c, t, C["s12.c"] + 0.15 * k, P[i], P[i + 1], alfa=0.3)
        hs(c, t, C["s12.d"] + 0.15 * k, P, i, viz[i], 2, 64, COR)
    E.frase(c, t, C["s12.c"], [("dobra:", "i", 60), ("2 ligações", "g", 56)], XE, 760, passo=0.1)
    E.frase(c, t, C["s12.d"], [("→", "g", 56, TINTA2), ("2 H", "g", 56, COR)], XE + 520, 760, passo=0.1)
    E.formula_em(c, t, C["s13.a"], "3 + 2 + 2 + 2 + 3 =", 1300, 930, 70, "g", TINTA2, "right")
    bola_txt(c, t, C["s13.b"], "12", 1400, 905, 62, 64)
    E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: E.escreve(c, "H", 1490, 930, 70, "g", TINTA, a))
    Q.formula_em(c, t, C["s13.d"], "C5H12", XE, 960, 120, cores={"indice": E.COR})
    pilula_em(c, t, C["s13.e"], "pentano: está na gasolina", CX, 300, 46, TINTA, "b")
    E.foco(c, t, C["s13.c"], 0.4, lambda a: centro(c, "5 carbonos · fórmula molecular", XE + 260, 850, 44, "i", TINTA2, a))


# ---------------- com ligação dupla ----------------
BUT = Q.zigzag(4)
DX_, DY_, DE = 1460, 600, 190


def b_dupla(c, t, C, b):
    P = pts_tela(BUT, DX_, DY_, DE)
    viz = bastao_viz(4)
    E.frase(c, t, C["s14"], ps("e se houver uma", "i", 72) + [("dupla?", "g", 68, COR)], XE, 180, passo=0.12)
    Q.bastao(c, t, C["s14.a"], BUT, DX_, DY_, DE, duplas={(0, 1)}, d=0.8, numeros=C["s14.a"] + 1.0)
    linhas = (("s14.b", 0, "1º: só a dupla", "2", 2), ("s14.c", 1, "2º: dupla + simples", "3", 1), ("s14.d", 2, "3º: duas simples", "2", 2),
              ("s14.e", 3, "4º: a ponta", "1", 3))
    for k, (key, i, txt, nl, nh) in enumerate(linhas):
        y = 340 + k * 120
        E.frase(c, t, C[key], [(txt, "i", 54)], XE, y)
        E.foco(c, t, C[key] + 0.3, 0.4, lambda a, nl=nl, nh=nh, y=y: E.formula(c, f"{nl} lig. → {nh} H", XE + 520, y, 52, "g", COR, a))
        hs(c, t, C[key] + 0.3, P, i, viz[i], nh, 64, COR, dist=95)
    realce(c, t, C["s14.b"], P[0], P[1], largura=36)
    E.formula_em(c, t, C["s15.a"], "2 + 1 + 2 + 3 =", 1260, 940, 70, "g", TINTA2, "right")
    bola_txt(c, t, C["s15.a"] + 0.8, "8", 1350, 915, 56, 64)
    Q.formula_em(c, t, C["s15.b"], "C4H8", 1440, 965, 110, cores={"indice": E.COR})


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s16.a"], ps("a dupla vale só uma ligação?", "i", 66), XE + 450, 190, passo=0.1)
    P = pts_tela(BUT, 640, 560, 190)
    viz = bastao_viz(4)
    Q.bastao(c, t, C["s16"], BUT, 640, 560, 190, duplas={(0, 1)}, d=0.6)

    def errado():
        hs(c, t, C["s16.b"], P, 0, viz[0], 3, 62, ERRADO, dist=95)
        hs(c, t, C["s16.b"] + 0.5, P, 1, viz[1], 2, 62, ERRADO, dist=95)
        hs(c, t, C["s16.b"] + 0.8, P, 2, viz[2], 2, 62, TINTA2, dist=95)
        hs(c, t, C["s16.b"] + 0.9, P, 3, viz[3], 3, 62, TINTA2, dist=95)
        E.formula_em(c, t, C["s16.c"], "3 + 2 + 2 + 3 = 10", 640, 900, 70, "g", ERRADO, "center")
        if t >= C["s16.c"] + 0.8:
            E.risco(c, 360, 920, 920, 850, t, C["s16.c"] + 0.8, largura=10)
    E.saida(c, t, C["s17"] + 2.0, errado)
    # o carbono de cinco ligações, de perto
    zx, zy = 1440, 560
    if t >= C["s17.a"]:
        q = ep(t, C["s17.a"], 0.5)
        E.foco(c, t, C["s17.a"], 0.5, lambda a: estrela(c, zx, zy, [2, 1, 1], a, 110, 100))
        E.foco(c, t, C["s17.a"] + 0.3, 0.4, lambda a: (M.line(c, zx, zy - 66, zx, zy - 170, ERRADO, a, 7), centro(c, "H", zx, zy - 190, 80, "g", ERRADO, a)))
        for k, g in enumerate((30, -30)):
            ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
            E.foco(c, t, C["s17.a"] + 0.4 + 0.1 * k, 0.4, lambda a, ux=ux, uy=uy: centro(c, "H", zx + ux * 205, zy + uy * 205 + 28, 80, "g", TINTA, a))
        E.foco(c, t, C["s17.a"] + 1.0, 0.4, lambda a: E.formula(c, "2 + 1 + 1 + 1 = 5", zx, 870, 64, "g", ERRADO, a, "center"))
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.selo(c, zx + 330, zy - 40, 60, False, a))
        E.foco(c, t, C["s17.b"] + 0.3, 0.4, lambda a: centro(c, "não existe", zx + 330, zy + 80, 50, "i", ERRADO, a))
    if t >= C["s17.c"]:
        pilula_em(c, t, C["s17.c"], "traços + H = 4, em cada carbono", W / 2, 1000, 50, E.COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s19"]:
        def s18():
            E.frase(c, t, C["s18.a"], ps("o atalho para conferir o total", "i", 70, CLARO), W / 2, 160, "center", 0.12)
            E.frase(c, t, C["s18.b"], ps("cadeia aberta, só simples:", "i", 62, CLARO), XE, 300, passo=0.1)
            E.formula_em(c, t, C["s18.b"] + 1.2, "H = 2 × C + 2", W / 2, 470, 150, "g", BR, "center")
            E.formula_em(c, t, C["s18.c"], "5 C:  10 + 2 = 12", XE, 650, 76, "g", CLARO)
            E.frase(c, t, C["s18.d"], [("cada dupla:", "i", 62, CLARO), ("− 2 H", "g", 62, BR), ("·", "g", 62, CLARO), ("tripla:", "i", 62, CLARO), ("− 4 H", "g", 62, BR)],
                    XE, 790, passo=0.1)
            E.formula_em(c, t, C["s18.e"], "4 C + dupla:  8 + 2 − 2 =", XE, 940, 76, "g", CLARO)
            w = E.formula(None, "4 C + dupla:  8 + 2 − 2 =", 0, 0, 76, a=0)
            bola_txt(c, t, C["s18.e"] + 1.6, "8", XE + w + 80, 915, 56, 70)
        E.saida(c, t, C["s19"] - 0.1, s18)
        return
    E.frase(c, t, C["s19.a"], ps("a dupla usa uma ligação a mais de cada carbono", "i", 62, CLARO), W / 2, 180, "center", 0.1)

    def porque():
        P = pts_tela([(-0.6, 0), (0.6, 0)], W / 2 - 300, 420, 180)
        Q.bastao(c, t, C["s19.a"] + 0.6, [(-0.6, 0), (0.6, 0)], W / 2 - 300, 420, 180, duplas={(0, 1)}, d=0.5, escuro=True)
        for k, p in enumerate(P):
            E.foco(c, t, C["s19.a"] + 1.2 + 0.2 * k, 0.4, lambda a, p=p: E.formula(c, "− 1 H", p[0], p[1] - 70, 56, "g", E.CLARO, a, "center"))
        E.foco(c, t, C["s19.a"] + 1.8, 0.4, lambda a: E.formula(c, "= − 2 H", W / 2 + 120, 440, 76, "g", BR, a))
    E.saida(c, t, C["s19.d"] - 0.1, porque)
    E.frase(c, t, C["s19.b"], ps("o oxigênio não muda a conta:", "i", 60, CLARO), XE, 640, passo=0.1)
    Q.formula_em(c, t, C["s19.c"], "C2H6O", XE, 790, 110, cores={"indice": E.CLARO}, escuro=True)
    E.formula_em(c, t, C["s19.c"] + 0.6, "2 × 2 + 2 = 6", XE + 440, 790, 76, "g", BR)
    E.frase(c, t, C["s19.d"], [("não vale", "g", 60, ERRADO), ("com nitrogênio:", "i", 62, CLARO)] + ps("conte carbono por carbono", "i", 62, CLARO), XE, 960, passo=0.1)


# ---------------- questão ----------------
QPTS = Q.zigzag(6)
QX, QY, QE = 1300, 520, 160


def bastao_q(c, t, t0, numeros=None):
    Q.bastao(c, t, t0, QPTS, QX, QY, QE, duplas={(2, 3)}, rotulos={5: "OH"}, d=0.9, numeros=numeros, passo_n=0.25)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 180)
    bastao_q(c, t, C["s20.a"])
    E.frase(c, t, C["s20.a"] + 0.2, [("uma", "i", 62), ("dupla", "g", 58), ("e", "i", 62), ("OH", "g", 58, Q.cor_el("O")), ("na ponta", "i", 62)], XE, 330, passo=0.1)
    E.frase(c, t, C["s20.b"], ps("qual é a", "i", 76) + [("fórmula molecular?", "g", 70, COR)], XE, 820, passo=0.12)
    if t >= C["s21"]:
        E.relogio(c, t, C["s21.a"], cx=1600, cy=800, r=105)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = pts_tela(QPTS, QX, QY, QE)
    viz = bastao_viz(6)
    bastao_q(c, t, C["s22"] - 0.5, numeros=C["s22.a"])
    E.frase(c, t, C["s22.a"], ps("a ponta e as quatro dobras", "i", 60), XE, 200, passo=0.1)
    if t >= C["s22.b"]:
        q = ep(t, C["s22.b"], 0.4)
        c.drawCircle(P[5][0], P[5][1], 70, M.paint(TINTA2, q, stroke=5))
        E.foco(c, t, C["s22.b"] + 0.2, 0.4, lambda a: centro(c, "não é C", P[5][0], P[5][1] - 90, 44, "i", TINTA2, a))
    E.frase(c, t, C["s22.c"], [("5", "g", 64, COR), ("carbonos", "i", 66)], XE, 300, passo=0.12)
    nhs = (3, 2, 1, 1, 2)
    for k, n in enumerate(nhs):
        hs(c, t, C[f"s23.{'abcde'[k]}"], P, k, viz[k], n, 58, COR, dist=92)
    contas = ("3", "+ 2", "+ 1", "+ 1", "+ 2")
    x = XE
    for k, s in enumerate(contas):
        E.foco(c, t, C[f"s23.{'abcde'[k]}"] + 0.2, 0.4, lambda a, s=s, x=x: E.formula(c, s, x, 820, 64, "g", TINTA2, a))
        x += E.formula(None, s + " ", 0, 0, 64, a=0)
    if t >= C["s23.f"]:
        halo(c, t, C["s23.f"], [P[5]], 80)
        E.foco(c, t, C["s23.f"] + 0.3, 0.4, lambda a, x=x: E.formula(c, "+ 1", x, 820, 64, "g", COR, a))
        E.foco(c, t, C["s23.f"] + 0.3, 0.4, lambda a: centro(c, "o H do OH conta", P[5][0], P[5][1] + 120, 44, "i", COR, a))
    x2 = x + E.formula(None, "+ 1 ", 0, 0, 64, a=0)
    E.foco(c, t, C["s23.g"], 0.4, lambda a: E.formula(c, "= 10 H", x2, 820, 64, "g", TINTA, a))
    Q.formula_em(c, t, C["s23.h"], "C5H10O", XE, 990, 120, cores={"indice": E.COR})
    # pelo atalho
    E.foco(c, t, C["s24.a"], 0.4, lambda a: E.formula(c, "atalho: 10 + 2 = 12", 1100, 880, 56, "g", TINTA2, a))
    E.foco(c, t, C["s24.b"], 0.4, lambda a: E.formula(c, "− 2 da dupla = 10", 1100, 960, 56, "g", TINTA2, a))
    E.foco(c, t, C["s24.c"] + 0.5, 0.4, lambda a: E.selo(c, 1780, 920, 54, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        E.frase(c, t, C["s25.a"], [("o carbono faz", "i", 80), ("4 ligações", "g", 84, COR)], XE, 420, passo=0.12)
        E.frase(c, t, C["s25.b"], ps("no bastão, o que falta para 4", "i", 74), XE, 580, passo=0.1)
        E.frase(c, t, C["s25.b"] + 1.6, [("=", "g", 74, TINTA2), ("H escondidos", "g", 80, COR)], XE, 700, passo=0.12)
        Q.bastao(c, t, C["s25.b"], PENT, 1450, 900, 120, d=0.6)
        P = pts_tela(PENT, 1450, 900, 120)
        viz = bastao_viz(5)
        for i, n in enumerate((3, 2, 2, 2, 3)):
            hs(c, t, C["s25.b"] + 1.0 + 0.1 * i, P, i, viz[i], n, 44, COR, dist=60)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s26.a"], [("classificar", "g", 96, COR)], XE, 380)
    E.frase(c, t, C["s26.a"] + 0.5, [("carbonos", "i", 96), ("e", "i", 96), ("cadeias", "g", 96, COR)], XE, 500, passo=0.12)
    for k, (key, s) in enumerate((("s26.b", "aberta ou fechada"), ("s26.c", "ramificada"), ("s26.d", "insaturada"))):
        E.foco(c, t, C[key], 0.4, lambda a, s=s, k=k: E.pilula(c, s, XE + 30 + (E.larg(s, "i", 50) + 55) / 2, 640 + k * 100, 50, "i", fundo=TINTA, a=a))
    E.foco(c, t, C["s26.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s26.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s26.e"] + 0.2, 0.4))
    E.frase(c, t, C["s26.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carbono=b_carbono, formas=b_formas, contar=b_contar, dupla=b_dupla, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
