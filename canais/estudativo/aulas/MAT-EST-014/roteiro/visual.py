"""Visual — Estudativo · MAT-EST-014: quartis e percentis.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e das fichas de MAT-EST-011 (notas(): a lista em
fichas, a ficha da mediana acesa, colchetes de metade). Conta da vez à direita, resposta na esfera, atalho no palco escuro.
Novo nesta aula (para copiar nas próximas, e base do boxplot de MAT-EST-015):
- CORTE = TRAÇO VERTICAL TRACEJADO entre as fichas, com a pílula Q1, Q2 ou Q3 em cima (corte()).
- OS QUATRO PEDAÇOS = BARRA DIVIDIDA em quatro faixas iguais com "≈ 25%" (quartos()).
- RÉGUA DOS QUARTIS = E.reta de 0 a 10 com Q1 = 4, Q2 = 6 e Q3 = 8 marcados e a faixa pintada (faixa()) até o corte da vez.
- PERCENTIL = E.reta de 0 a 100% com a faixa pintada até o percentil.
- MULTIDÃO = GRADE DE BOLINHAS (multidao()): os que ficaram acima acesos na cor da matéria.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-014_quartis_e_percentis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quartis", "percentil", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
NOTAS = [2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10]
QUEST = [6, 9, 3, 10, 6, 7, 5, 8]
assert NOTAS == sorted(NOTAS) and (11 + 1) / 2 == 6 and NOTAS[5] == 6 and NOTAS[2] == 4 and NOTAS[8] == 8
_q = sorted(QUEST)
assert _q == [3, 5, 6, 6, 7, 8, 9, 10] and (_q[3] + _q[4]) / 2 == 6.5 and (_q[1] + _q[2]) / 2 == 5.5 and (_q[5] + _q[6]) / 2 == 8.5
assert 100 - 90 == 10 and 2000 * 10 // 100 == 200


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→≈") else est, size * (0.92 if any(ch in w for ch in "%²³→≈") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


def notas(c, t, t0, vals, cx, y, size=76, passo=None, t_ordem=None, acesas=None, d=1.0, d_ent=0.1, apaga=None):
    """lista de fichas numa linha (a mesma de MAT-EST-011). t_ordem: cada ficha anda em arco até o seu lugar em ordem.
    acesas = {índice original: [(t, cor), ...]}; apaga = {índice: t} desbota a ficha. Devolve slot(k) = x da k-ésima casa"""
    n = len(vals)
    passo = passo or size * 2.3
    x0 = cx - passo * (n - 1) / 2
    ordem = sorted(range(n), key=lambda i: (vals[i], i))
    lugar = {i: k for k, i in enumerate(ordem)}
    q = ease_io(prog(t, t_ordem, d)) if t_ordem is not None else 0.0
    for i, v in enumerate(vals):
        xa, xb = x0 + passo * i, x0 + passo * lugar[i]
        px = lerp(xa, xb, q)
        py = y - (1 if xb > xa else -1) * size * 1.6 * math.sin(math.pi * q) * (0 if xa == xb else 1)
        cor = None
        for ti, cc in (acesas or {}).get(i, []):
            if t >= ti:
                cor = cc
        al = 1 - 0.65 * ep(t, apaga[i], 0.4) if apaga and i in apaga else 1.0
        E.foco(c, t, t0 + d_ent * i, 0.4, lambda a, s=E._num(v), px=px, py=py, cor=cor, al=al: ficha(c, s, px, py, size, a * al, cor), sobe=10)
    return lambda k: x0 + passo * k


def metades(c, t, t0, x0, x1, x2, x3, y, rot1="metade", rot2="metade", cor=None, size=46):
    """colchetes embaixo das fichas, com o rótulo de cada lado (os de MAT-EST-011); x2 = None faz só o primeiro"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    for xa, xb, s in ((x0, x1, rot1), (x2, x3, rot2)):
        if xa is None:
            continue
        E.chave(c, xa, xb, y, cor or TINTA2, p, 26, 5)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, xa=xa, xb=xb, s=s: centro(c, s, (xa + xb) / 2, y + 26 + size * 1.25, size, "i", cor or TINTA2, a))


# ================= peças dos quartis (copiar nas próximas aulas) =================
def corte(c, t, t0, x, y0, y1, rot=None, cor=None, size=44, escuro=False):
    """um corte: traço vertical tracejado de y0 a y1, com a pílula do nome em cima"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    k = cor or E.COR
    M.line(c, x, y0, x, lerp(y0, y1, p), k, 1, 5, dash=E.TRACO)
    if rot:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.pilula(c, rot, x, y0 - size * 0.9, size, "g", fundo=k, cor=E.SOBRE if not escuro else "#07070F", a=a))


def quartos(c, t, t0, x, y, w, h, t_cortes, t_pct=None, rotulos=("Q1", "Q2", "Q3"), t_rot=None):
    """a barra dos dados em quatro pedaços: t_cortes = instante de cada corte (Q1, Q2, Q3); t_pct = "≈ 25%" em cada pedaço"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w * p, h), 18, 18)
    c.drawRRect(r, M.paint(E.mix(E.COR, PAPEL, 0.78)))
    c.drawRRect(r, M.paint(E.COR, 1, stroke=4))
    for k, tc in enumerate(t_cortes):
        if tc is None:
            continue
        xc = x + w * (k + 1) / 4
        q = ep(t, tc, 0.4)
        if q > 0:
            M.line(c, xc, y - 20, xc, lerp(y - 20, y + h + 20, q), TINTA, 1, 6)
        if t_rot is not None:
            E.foco(c, t, t_rot + 0.3 * k, 0.4, lambda a, xc=xc, k=k: E.pilula(c, rotulos[k], xc, y - 70, 46, "g", a=a, cor=E.SOBRE))
    if t_pct is not None:
        for k in range(4):
            E.foco(c, t, t_pct + 0.15 * k, 0.4, lambda a, k=k: centro(c, "≈ 25%", x + w * (k + 0.5) / 4, y + h / 2 + 18, 50, "g", COR, a))


def faixa(c, vx, v0, v1, y, h, cor, a):
    """faixa pintada sobre a reta, de v0 a v1"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(vx(v0), y - h, vx(v1) - vx(v0), h), M.paint(cor, a))


def multidao(c, t, t0, cols, lins, x, y, passo, r, acima, t_acima, cor_base=None, d=0.8):
    """grade de bolinhas (pessoas); as `acima` primeiras de cima ficam na cor da matéria a partir de t_acima"""
    for j in range(lins):
        for i in range(cols):
            k = ease_back(prog(t, t0 + d * (j / max(1, lins - 1)) * 0.6 + 0.01 * i, 0.3))
            if k <= 0:
                continue
            n = j * cols + i
            dentro = n < acima and t >= t_acima
            q = ep(t, t_acima + 0.01 * n, 0.3) if dentro else 0
            cor = E.mix(cor_base or E.mix(CINZA, PAPEL, 0.4), E.COR, q)
            c.drawCircle(x + i * passo, y + j * passo, r * k, M.paint(cor))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        for k, (ti, l1, l2) in enumerate(((a1, "acertos", "62 de 100"), (b1, "posição", "percentil 90"))):
            x = 560 + 800 * k
            p = ep(t, ti, 0.5)
            if p > 0:
                M.rrect(c, x - 330, 300, 660, 420, 30, BR, p)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 330, 300, 660, 420), 30, 30), M.paint(FIO, p, stroke=3))
            E.foco(c, t, ti + 0.1, 0.4, lambda a, x=x, l1=l1: centro(c, l1, x, 400, 56, "i", TINTA2, a))
            E.foco(c, t, ti + 0.3, 0.4, lambda a, x=x, l2=l2: centro(c, l2, x, 560, 96, "g", COR, a))
        E.frase(c, t, b1 + 1.0, ps("foi mal ou foi bem?", "i", 64), W / 2, 200, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "foi muito bem", W / 2, 850, 72, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("os dados em", "i", 88) + [("4 partes", "g", 100, COR)], XE, 330, passo=0.14)
        E.frase(c, t, ta + 2.0, ps("os", "i", 88) + [("quartis", "g", 100, COR)], XE, 480, passo=0.14)
        quartos(c, t, ta + 1.0, XE, 600, 900, 110, [ta + 1.6, ta + 1.4, ta + 1.8])
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa:", XE + 175, 700, 120, "i", TINTA, a))
    E.frase(c, t, C["s03.a"] + 0.6, [("a mediana", "g", 90, COR)], XE, 860)
    x, w = 980, 820
    itens = (("s03.b", "ordene e pegue", "o meio"), ("s03.c", "a posição do meio:", "f{n + 1}{2}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 90, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 44, y + 190, 70, "g", COR)
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- quartis ----------------
FY = 470   # a linha das fichas


def b_quartis(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, a4, ps("a mediana corta em", "i", 66) + [("2 metades", "g", 72, COR)], W / 2, 200, "center", 0.1)
        E.frase(c, t, b4, ps("os quartis cortam em", "i", 66) + [("4 partes", "g", 72, COR)], W / 2, 300, "center", 0.1)
        quartos(c, t, a4, 260, 520, 1400, 150, [b4 + 0.3, a4 + 0.3, b4 + 0.5], t_pct=c4, t_rot=d4)
        E.foco(c, t, a4 + 0.5, 0.4, lambda a: (centro(c, "metade", 610, 760, 46, "i", TINTA2, a * (1 - ep(t, b4, 0.4))),
                                               centro(c, "metade", 1310, 760, 46, "i", TINTA2, a * (1 - ep(t, b4, 0.4)))))
        E.frase(c, t, d4 + 1.0, ps("3 cortes:", "i", 56) + [("1º, 2º e 3º quartil", "g", 60, COR)], W / 2, 860, "center", 0.08)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    # as onze notas, em ordem, até o fim do bloco
    ac = {5: [(c5, E.COR)], 2: [(c6, E.COR)], 8: [(e6, E.COR)]}
    apaga = {5: a6} if t < c7 - 0.5 else None
    slot = notas(c, t, a5, NOTAS, W / 2, FY, 64, 150, acesas=ac, d_ent=0.06, apaga=apaga)
    for k in range(11):
        E.foco(c, t, b5 + 0.04 * k, 0.4, lambda a, k=k: centro(c, f"{k + 1}º", slot(k), FY + 100, 34, "b", COR if k == 5 else TINTA2, a))
    corte(c, t, d5, slot(5), FY - 110, FY + 60, "Q2")
    corte(c, t, c6 + 0.3, slot(2), FY - 110, FY + 60, "Q1")
    corte(c, t, e6 + 0.3, slot(8), FY - 110, FY + 60, "Q3")

    def dois():
        E.frase(c, t, a5, ps("11 notas,", "i", 60) + [("já em ordem", "g", 64, COR)], W / 2, 190, "center", 0.1)
        fcen(c, t, b5, "posição: f{11 + 1}{2} = 6", 640, 760, 70)
        E.frase(c, t, c5, ps("o valor na 6ª posição:", "i", 54) + [("6", "g", 64, COR)], 1340, 760, "center", 0.08)
        E.frase(c, t, lerp(c5, d5, 0.4), ps("a mediana é o valor, não a posição", "i", 46, TINTA2), W / 2, 880, "center", 0.06)
        E.foco(c, t, d5, 0.4, lambda a: E.pilula(c, "mediana = 2º quartil = Q2", W / 2, 990, 50, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)

    def tres():
        E.frase(c, t, C["s06"] + 0.1, ps("o mesmo em", "i", 60) + [("cada metade", "g", 64, COR)], W / 2, 190, "center", 0.1)
        E.frase(c, t, a6, ps("ímpar: a mediana", "i", 46, TINTA2) + [("fica de fora", "g", 48, TINTA2)], W / 2, 260, "center", 0.06)
        metades(c, t, b6, slot(0) - 60, slot(4) + 60, None, None, FY + 150, "5 notas de baixo")
        metades(c, t, d6, slot(6) - 60, slot(10) + 60, None, None, FY + 150, "5 notas de cima")
        E.foco(c, t, c6, 0.4, lambda a: E.pilula(c, "Q1 = 4", slot(2), 830, 60, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, e6, 0.4, lambda a: E.pilula(c, "Q3 = 8", slot(8), 830, 60, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s06"], C["s07"] - 0.1, tres)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, a7, [("Q1", "g", 60, COR)] + ps("= mediana da metade de baixo", "i", 52), 520, 200, "center", 0.06)
    E.frase(c, t, b7, [("Q3", "g", 60, COR)] + ps("= mediana da metade de cima", "i", 52), 1400, 200, "center", 0.06)
    vx = E.reta(c, t, c7 - 0.4, 260, 1660, 800, 0, 10, list(range(0, 11)), size=40)
    for k, (tc, v, rot) in enumerate(((c7, 4, "≈ 1/4"), (d7, 8, "≈ 3/4"))):
        if t >= tc:
            a_ = ep(t, tc, 0.5) * (1 - ep(t, (d7, e7)[k], 0.4))
            faixa(c, vx, 0, v, 790, 60, E.mix(E.COR, PAPEL, 0.55), a_)
            E.foco(c, t, tc + 0.2, 0.4, lambda a, v=v, rot=rot, k=k: centro(c, "até Q" + ("1" if k == 0 else "3") + ": " + rot, vx(v / 2), 700, 46, "g", COR,
                                                                         a * (1 - ep(t, (d7, e7)[k], 0.4))))
    if t >= e7:
        faixa(c, vx, 4, 8, 790, 60, E.mix(E.COR, PAPEL, 0.55), ep(t, e7, 0.5))
        E.foco(c, t, e7 + 0.2, 0.4, lambda a: centro(c, "≈ metade do meio", vx(6), 700, 46, "g", COR, a))
    for v, rot in ((4, "Q1"), (6, "Q2"), (8, "Q3")):
        E.foco(c, t, c7, 0.4, lambda a, v=v: c.drawCircle(vx(v), 800, 14, M.paint(E.COR, a)))
    E.foco(c, t, lerp(e7, C["s07.end"], 0.25), 0.5, lambda a: E.pilula(c, "neste curso: a mediana de cada metade", W / 2, 950, 42, "g", fundo=TINTA2, a=a))
    E.frase(c, t, lerp(e7, C["s07.end"], 0.75), ps("se a prova ensinar outro jeito, siga a prova", "i", 42, TINTA2), W / 2, 1035, "center", 0.05)


# ---------------- percentil ----------------
def b_percentil(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    E.frase(c, t, a8, [("percentil", "g", 84, COR)] + ps("= a mesma ideia, em", "i", 66) + [("100 partes", "g", 72)], W / 2, 200, "center", 0.1)
    vx = E.reta(c, t, a8 + 0.6, 260, 1660, 600, 0, 100, [0, 25, 50, 75, 90, 100], fmt=lambda v: f"{v}%", size=40)
    if t >= b8:
        a_ = ep(t, b8, 0.6) * (1 - ep(t, a9, 0.4)) + ep(t, d9, 0.5)
        faixa(c, vx, 0, lerp(0, 90, ep(t, b8, 0.8)) if t < d9 else 90, 590, 70, E.mix(E.COR, PAPEL, 0.55), min(1, a_))
    corte(c, t, b8, vx(90), 470, 610, "P90")
    E.frase(c, t, b8 + 0.6, ps("≈ 90% dos dados", "i", 54) + [("abaixo ou iguais", "g", 56, COR)], vx(45), 760, "center", 0.08)
    for k, (ti, v, rot) in enumerate(((a9, 25, "P25 = Q1"), (b9, 50, "P50 = mediana"), (c9, 75, "P75 = Q3"))):
        corte(c, t, ti, vx(v), 470, 610, None, TINTA)
        E.foco(c, t, ti + 0.2, 0.4, lambda a, v=v, rot=rot: E.pilula(c, rot, vx(v), 380 - 0 * k, 40, "g", fundo=TINTA, a=a))
    E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "percentil 90: melhor ou igual a ≈ 90% dos candidatos", W / 2, 900, 48, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, C["s10"] + 0.2, [("erro comum:", "g", 64, ERRADO)], 560, 200, "center", 0.1)
    E.frase(c, t, a0, ps("percentil 90 =", "i", 54) + [("acertar 90%?", "g", 58, ERRADO)], 560, 330, "center", 0.08)
    E.foco(c, t, a0 + 1.4, 0.4, lambda a: E.selo(c, 560, 450, 44, False, a))
    E.frase(c, t, b0, ps("o percentil", "i", 54) + [("compara você", "g", 58, COR)], 560, 600, "center", 0.08)
    E.frase(c, t, b0 + 0.8, ps("com os outros", "i", 54), 560, 680, "center", 0.08)
    E.frase(c, t, c0, ps("62 acertos:", "i", 50) + [("acima de ≈ 90%", "g", 54, CERTO)], 560, 820, "center", 0.08)
    E.frase(c, t, lerp(c0, C["s10.end"], 0.6), ps("a prova é que foi difícil", "i", 46, TINTA2), 560, 900, "center", 0.06)
    multidao(c, t, b0, 10, 10, 1140, 300, 60, 20, 10, c0)
    E.foco(c, t, c0 + 0.6, 0.4, lambda a: E.escreve(c, "você está aqui em cima", 1140 - 20, 260, 40, "i", COR, a))
    E.foco(c, t, b0 + 0.6, 0.4, lambda a: centro(c, "100 candidatos", 1410, 960, 44, "i", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    X = 620

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("o atalho:", "i", 64, CLARO), X, 180, "center", 0.1)
        E.frase(c, t, a1, ps("quantos acima?", "i", 58, CLARO), X, 290, "center", 0.1)
        fcen(c, t, a1 + 0.6, "100 − percentil", X, 400, 80, BR)
        fcen(c, t, b1, "100 − 90 = 10", X, 540, 80, BR)
        E.frase(c, t, c1, ps("entre os", "i", 54, CLARO) + [("10% mais altos", "g", 58, BR)], X, 650, "center", 0.08)
        fcen(c, t, d1, "10% de 2.000 = 200", X, 800, 76, BR)
        E.frase(c, t, d1 + 1.0, ps("entre os ≈ 200 primeiros", "i", 50, CLARO), X, 900, "center", 0.08)
        multidao(c, t, d1 - 0.4, 40, 50, 1180, 220, 15, 5.2, 200, d1 + 0.8, cor_base="#3A3A4A")
        E.foco(c, t, d1, 0.4, lambda a: centro(c, "2.000 candidatos", 1472, 1000, 40, "i", CLARO, a))
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, a2, ps("funciona porque quem", "i", 60, CLARO) + [("não está abaixo,", "g", 64, BR)], W / 2, 330, "center", 0.1)
    E.frase(c, t, a2 + 1.2, [("está acima", "g", 72, BR)], W / 2, 430, "center", 0.1)
    E.frase(c, t, b2, ps("o resultado é sempre", "i", 60, CLARO) + [("aproximado", "g", 64, BR)], W / 2, 600, "center", 0.1)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "lista pequena ou notas iguais? conte na lista", W / 2, 780, 48, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a3, ps("as notas de", "i", 58) + [("8 alunos:", "g", 62, COR)], XE, 300, passo=0.1)
    notas(c, t, a3 + 0.3, QUEST, 820, 440, 70, 175, d_ent=0.06)
    E.frase(c, t, b3, [("1)", "g", 60, COR)] + ps("ache", "i", 60) + [("Q1, Q2 e Q3", "g", 64)], XE, 630, passo=0.1)
    E.frase(c, t, c3, [("2)", "g", 60, COR)] + ps("Bia tirou nota igual a", "i", 60) + [("Q3", "g", 64)], XE, 750, passo=0.1)
    E.frase(c, t, c3 + 1.8, ps("o que isso diz sobre ela?", "i", 56), XE + 70, 840, passo=0.08)
    E.relogio(c, t, C["s14.a"], 1600, 700, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    ordem = sorted(range(8), key=lambda i: (QUEST[i], i))
    ac = {ordem[3]: [(b5, E.COR), (a6 - 0.3, None)], ordem[4]: [(b5, E.COR), (a6 - 0.3, None)],
          ordem[1]: [(a6 - 0.3, E.COR)], ordem[2]: [(a6 - 0.3, E.COR)], ordem[5]: [(b6 - 0.3, E.COR)], ordem[6]: [(b6 - 0.3, E.COR)]}
    slot = notas(c, t, C["s15"], QUEST, W / 2, 330, 70, 190, t_ordem=a5, acesas=ac, d_ent=0.0)
    E.foco(c, t, a5, 0.4, lambda a: E.escreve(c, "em ordem", XE - 60, 220, 48, "i", TINTA2, a))
    corte(c, t, b5 + 0.6, (slot(3) + slot(4)) / 2, 230, 400, "Q2")
    corte(c, t, a6, (slot(1) + slot(2)) / 2, 230, 400, "Q1")
    corte(c, t, b6, (slot(5) + slot(6)) / 2, 230, 400, "Q3")
    metades(c, t, c5, slot(0) - 60, slot(3) + 50, slot(4) - 50, slot(7) + 60, 410, "4 notas", "4 notas")

    def um():
        fcen(c, t, b5, "Q2 = (6 + 7) ÷ 2 = 6,5", W / 2, 640, 72, COR)
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    fcen(c, t, C["s16"], "Q2 = 6,5", W / 2, 600, 56)
    fcen(c, t, a6, "Q1 = (5 + 6) ÷ 2 = 5,5", 560, 700, 60, COR)
    fcen(c, t, b6, "Q3 = (8 + 9) ÷ 2 = 8,5", 1360, 700, 60, COR)
    E.frase(c, t, c6, ps("Bia:", "i", 56) + [("≈ 75%", "g", 60, COR)] + ps("tiraram nota igual ou menor", "i", 56), W / 2, 850, "center", 0.08)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "entre os 25% mais altos", W / 2, 970, 56, "g", a=a, cor=E.SOBRE))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", [("quartis:", "g", 66, COR)] + ps("medianas das metades", "i", 62)),
                 ("s17.b", [("percentil:", "g", 66, COR)] + ps("quantos ficaram abaixo de você", "i", 62)))
        for i, (k, partes) in enumerate(itens):
            y = 460 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
        E.frase(c, t, C["s17.b"] + 1.6, ps("não quanto você acertou", "i", 52, TINTA2), 290, 750, "left", 0.08)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a0, b0, c0, d0 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("o boxplot", "g", 120, COR)], XE, 420)
    E.frase(c, t, b0, ps("mínimo, quartis, máximo e", "i", 54) + [("amplitude", "g", 58, COR)], XE, 560, passo=0.08)
    E.frase(c, t, b0 + 1.6, ps("e duas turmas comparadas de uma olhada", "i", 50, TINTA2), XE, 650, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quartis=b_quartis, percentil=b_percentil, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
