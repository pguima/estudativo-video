"""Visual — Estudativo · MAT-EST-013: qual medida usar (média, mediana ou moda).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): cada categoria com a sua cor de E._paleta (aqui as
faixas de salário: 2.000, 2.500, 3.000 e o diretor), conta da vez à direita, resposta na esfera, atalho no palco escuro.
Pessoas da fila como em MAT-EST-011 (pessoa()).
Novo nesta aula (para copiar nas próximas):
- COLUNAS DA FILA (salarios()): os dez salários em ordem, uma coluna por pessoa, com a posição (1 a 10) embaixo. A escala
  se ajusta quando um valor cresce (a coluna do diretor vai de 21 para 41 mil e as outras encolhem).
- MÉDIA = LINHA TRACEJADA na altura da média, que sobe quando o valor da ponta cresce (linha_media()).
- MEDIANA = CAIXA PONTILHADA nas colunas do meio (5ª e 6ª), que não se mexe.
- QUANDO USAR = TRÊS CARTÕES (cartao()), um por medida, com um desenho: gangorra (média), fila (mediana), camisas (moda).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-013_qual_medida_usar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("salarios", "quando", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(4)                       # 2.000, 2.500, 3.000, diretor
SAL = [2.0] * 4 + [2.5] * 3 + [3.0] * 2 + [21.0]   # em mil reais, já em ordem
FAIXA = [0] * 4 + [1] * 3 + [2] * 2 + [3]
assert sum(SAL) == 42.5 and sum(SAL) / 10 == 4.25 and SAL[4] == SAL[5] == 2.5 and sum(1 for v in SAL if v <= 3) == 9
assert (sum(SAL) - 21 + 41) / 10 == 6.25 and 6.25 - 4.25 == 2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def pessoa(c, cx, base, h, cor, a=1.0):
    """uma pessoa de altura h (cabeça e corpo), em pé na linha base (a mesma de MAT-EST-011)"""
    if a <= 0:
        return
    r = h * 0.14
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    M.rrect(c, cx - h * 0.17, base - h + 2.25 * r, h * 0.34, h - 2.25 * r, h * 0.12, cor, a)


def camisa(c, cx, cy, s, a=1.0, cor=None):
    """camisa (a mesma de MAT-EST-001, sem número)"""
    if a <= 0:
        return
    k = s / 100
    p = skia.Path()
    pts = [(-40, -60), (-15, -70), (0, -58), (15, -70), (40, -60), (75, -30), (55, -5), (40, -18), (40, 70), (-40, 70), (-40, -18), (-55, -5), (-75, -30)]
    p.moveTo(cx + pts[0][0] * k, cy + pts[0][1] * k)
    for px, py in pts[1:]:
        p.lineTo(cx + px * k, cy + py * k)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))


def saco(c, cx, base, r, a=1.0, cor=None):
    """saco de dinheiro com R$"""
    if a <= 0 or r <= 0:
        return
    cor = cor or E.COR
    c.drawCircle(cx, base - r, r, M.paint(cor, a))
    p = skia.Path()
    p.moveTo(cx - r * 0.35, base - 1.85 * r); p.lineTo(cx + r * 0.35, base - 1.85 * r); p.lineTo(cx + r * 0.2, base - 2.3 * r)
    p.lineTo(cx - r * 0.2, base - 2.3 * r); p.close()
    c.drawPath(p, M.paint(cor, a))
    centro(c, "R$", cx, base - r + r * 0.3, r * 0.8, "g", E.SOBRE, a)


# ================= colunas da fila (copiar nas próximas aulas) =================
GX, GY, GW, GH = 190, 330, 1060, 560   # caixa das colunas: x, y do topo, largura, altura


def escala(t, t_cresce):
    return lerp(23.0, 43.0, ease_io(prog(t, t_cresce, 1.2))) if t_cresce is not None else 23.0


def py_(v, vmax):
    return GY + GH - v / vmax * GH


def px_(i):
    return GX + GW * (i + 0.5) / 10


def salarios(c, t, ts, t_cresce=None, risca=None, size=40, apaga=None):
    """as dez colunas (mil reais) em ordem; ts = instante de cada coluna; t_cresce = o diretor vai de 21 para 41 mil;
    risca = instante em que a coluna do diretor ganha o X vermelho"""
    vmax = escala(t, t_cresce)
    dirv = lerp(21.0, 41.0, ease_io(prog(t, t_cresce, 1.2))) if t_cresce is not None else 21.0
    bw = GW / 10 * 0.62
    p0 = ep(t, min(ts), 0.5)
    if p0 > 0:
        M.line(c, GX - 20, GY + GH, GX + GW + 20, GY + GH, TINTA, p0, 5)
        E.foco(c, t, min(ts), 0.4, lambda a: E.escreve(c, "salário (mil R$)", GX - 20, GY - 40, 40, "i", TINTA2, a))
    for i, v in enumerate(SAL):
        v = dirv if i == 9 else v
        q = ease_io(prog(t, ts[i], 0.6))
        if q <= 0:
            continue
        x, top = px_(i), lerp(GY + GH, py_(v, vmax), q)
        M.rrect(c, x - bw / 2, top, bw, GY + GH - top, 8, CATS[FAIXA[i]], 1.0)
        c.drawRect(skia.Rect.MakeXYWH(x - bw / 2, GY + GH - 8, bw, 8), M.paint(CATS[FAIXA[i]]))
        E.foco(c, t, ts[i] + 0.3, 0.4, lambda a, i=i, v=v, top=top: centro(c, E._num(round(v, 1)), px_(i), top - 16, size, "g", TINTA, a), sobe=6)
        E.foco(c, t, ts[i], 0.4, lambda a, i=i: centro(c, f"{i + 1}º", px_(i), GY + GH + 50, 34, "b", TINTA2, a), sobe=6)
    if risca is not None and t >= risca:
        x = px_(9)
        E.risco(c, x - 60, GY + 40, x + 60, GY + GH - 20, t, risca, largura=12)
        E.risco(c, x + 60, GY + 40, x - 60, GY + GH - 20, t, risca + 0.2, largura=12)


def linha_media(c, t, t0, v, t_sobe=None, v2=None, rotulo=True):
    """a média: linha tracejada na altura v (sobe para v2 em t_sobe), com a pílula do valor à direita"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    vmax = escala(t, t_sobe)
    vv = lerp(v, v2, ease_io(prog(t, t_sobe, 1.2))) if t_sobe is not None else v
    y = py_(vv, vmax)
    M.line(c, GX - 20, y, lerp(GX - 20, GX + GW + 20, p), y, ERRADO, 1, 5, dash=E.TRACO)
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, f"média: {E._num(round(vv, 2))} mil", px_(7), y - 44, 38, "g", fundo=ERRADO, a=a))


def caixa_mediana(c, t, t0, rotulo=True):
    """a mediana: caixa pontilhada nas colunas 5 e 6, com a pílula embaixo"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    x0, x1 = px_(4) - 50, px_(5) + 50
    E.caixa_pontilhada(c, x0, GY + GH - 150, x1 - x0, 230, p, E.COR, prog_=p)
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, "mediana: 2,5 mil", (x0 + x1) / 2, GY + GH + 120, 38, "g", a=a, cor=E.SOBRE))


def cartao(c, t, t0, cx, titulo, a_=1.0):
    """o cartão de uma medida: retângulo branco com o nome em cima"""
    p = ep(t, t0, 0.5) * a_
    if p <= 0:
        return
    w, h, y = 540, 680, 290
    M.rrect(c, cx - w / 2, y, w, h, 28, BR, p)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y, w, h), 28, 28), M.paint(FIO, p, stroke=3))
    centro(c, titulo, cx, y + 90, 70, "g", COR, p)


def gangorra(c, cx, cy, a=1.0):
    """a média como ponto de equilíbrio"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy); p.lineTo(cx - 40, cy + 70); p.lineTo(cx + 40, cy + 70); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    M.line(c, cx - 200, cy - 6, cx + 200, cy - 6, TINTA, a, 10)
    for dx, r in ((-170, 26), (-120, 26), (140, 34)):
        c.drawCircle(cx + dx, cy - 6 - r - 5, r, M.paint(TINTA2, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, a1, 0.5, lambda a: E.pilula(c, "salário médio: R$ 4.250", W / 2, 200, 66, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, lerp(a1, b1, 0.6), ps("parece bom", "i", 54, TINTA2), W / 2, 310, "center", 0.08)
        for i in range(10):
            x = 300 + 145 * i
            dono = i == 9
            E.foco(c, t, b1 + 0.08 * i, 0.4, lambda a, x=x, dono=dono: (
                pessoa(c, x - 25, 820, 190 if dono else 170, TINTA2 if not dono else TINTA, a),
                saco(c, x + (120 if dono else 35), 820, 90 if dono else 26, a, CATS[3] if dono else E.COR)), sobe=20)
        E.frase(c, t, b1 + 1.0, [("9 de 10", "g", 66, COR)] + ps("ganham até R$ 3.000", "i", 60), W / 2, 450, "center", 0.1)
        E.frase(c, t, lerp(b1, c1, 0.6), ps("a conta está certa", "i", 50, TINTA2), W / 2, 920, "center", 0.08)
        E.frase(c, t, c1, ps("mas a média não era", "i", 56) + [("a medida certa", "g", 60, ERRADO)], W / 2, 1010, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("quando usar", "i", 88), XE, 410, passo=0.14)
        E.frase(c, t, ta + 2.2, [("média, mediana", "g", 96, COR)], XE, 540, passo=0.14)
        E.frase(c, t, ta + 3.0, ps("ou", "i", 88) + [("moda", "g", 96, COR)], XE, 670, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "medidas", XE + 240, 700, 110, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a média aritmética:", "soma ÷ quantidade"), ("s03.c", "a mediana:", "o valor do meio, em ordem"),
             ("s03.d", "a moda:", "o valor que mais aparece"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 200 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 74, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 40, y + 160, 56, "g", COR)
    alvo = [200 + i * 240 + 170 for i in range(3)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 1000, "left", 0.1)


# ---------------- os salários ----------------
def b_salarios(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    ts = [a4 + 0.1 * i for i in range(4)] + [b4 + 0.1 * i for i in range(3)] + [c4, c4 + 0.1, d4]
    salarios(c, t, ts, t_cresce=a7)
    linha_media(c, t, b5, 4.25, t_sobe=b7, v2=6.25)
    caixa_mediana(c, t, c5)
    if t >= d5:   # moda: as quatro de 2 mil
        p = ep(t, d5, 0.5) * (1 - ep(t, C["s06"], 0.4))
        if p > 0:
            E.caixa_pontilhada(c, px_(0) - 50, GY + GH - 110, px_(3) - px_(0) + 100, 150, p, CATS[0], prog_=p)
    X = 1590

    def um():
        for k, (ti, n, s, cor) in enumerate(((a4, "4", "R$ 2.000", CATS[0]), (b4, "3", "R$ 2.500", CATS[1]), (c4, "2", "R$ 3.000", CATS[2]))):
            E.foco(c, t, ti, 0.4, lambda a, k=k, cor=cor: c.drawCircle(1350, 372 + 120 * k, 20, M.paint(cor, a)))
            E.frase(c, t, ti, [(n, "g", 58, COR)] + ps("pessoas:", "i", 50) + [(s, "g", 52)], 1395, 390 + 120 * k, "left", 0.08)
        E.foco(c, t, d4, 0.4, lambda a: c.drawCircle(1350, 732, 20, M.paint(CATS[3], a)))
        E.frase(c, t, d4, ps("diretor:", "i", 50) + [("R$ 21.000", "g", 56, COR)], 1395, 750, "left", 0.08)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)

    def dois():
        fcen(c, t, a5, "soma: R$ 42.500", X, 360, 56)
        fcen(c, t, b5, "42.500 ÷ 10 = 4.250", X, 480, 52, ERRADO)
        E.frase(c, t, c5, ps("mediana:", "i", 54) + [("o 5º e o 6º", "g", 58, COR)], X, 620, "center", 0.08)
        fcen(c, t, c5 + 1.2, "R$ 2.500", X, 710, 66, COR)
        E.frase(c, t, d5, ps("moda:", "i", 54) + [("R$ 2.000", "g", 60, CATS[0])], X, 850, "center", 0.08)
        E.frase(c, t, d5 + 0.6, ps("o mais comum", "i", 46, TINTA2), X, 930, "center", 0.06)
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)

    def tres():
        E.frase(c, t, C["s06"] + 0.1, ps("por que a média", "i", 50) + [("ficou alta?", "g", 54)], X, 330, "center", 0.08)
        E.frase(c, t, a6, ps("ela", "i", 52) + [("soma todos", "g", 56, ERRADO)], X, 450, "center", 0.08)
        E.frase(c, t, b6, ps("o diretor entra inteiro", "i", 44), X, 550, "center", 0.08)
        E.frase(c, t, b6 + 0.8, ps("e", "i", 44) + [("puxa para cima", "g", 50, ERRADO)], X, 620, "center", 0.08)
        if t >= b6:
            y = py_(4.25, 23) - 20
            k = ep(t, b6 + 0.3, 0.6)
            M.arrow(c, px_(1), y + 10, px_(1), y - 120, ERRADO, k, 7, 20, k)
        E.frase(c, t, c6, ps("a mediana só olha", "i", 48) + [("a posição", "g", 52, COR)], X, 760, "center", 0.08)
        E.frase(c, t, c6 + 1.6, ps("o diretor é só mais um na ponta", "i", 40, TINTA2), X, 840, "center", 0.06)
    fase(c, t, C["s06"], C["s07"] - 0.1, tres)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, C["s07"] + 0.1, [("o teste", "g", 66, COR)], X, 320, "center")
    E.frase(c, t, a7, ps("diretor:", "i", 54) + [("R$ 41.000", "g", 60, COR)], X, 440, "center", 0.08)
    E.frase(c, t, b7, ps("média:", "i", 54) + [("R$ 6.250", "g", 60, ERRADO)], X, 580, "center", 0.08)
    E.frase(c, t, b7 + 1.0, ps("subiu R$ 2.000", "i", 46, ERRADO), X, 650, "center", 0.06)
    E.frase(c, t, c7, ps("mediana:", "i", 54) + [("R$ 2.500", "g", 60, COR)], X, 790, "center", 0.08)
    E.foco(c, t, c7 + 0.6, 0.4, lambda a: E.selo(c, X - 230, 880, 36, True, a))
    E.frase(c, t, c7 + 0.7, ps("o 5º e o 6º não mudaram", "i", 44, TINTA2), X - 180, 896, "left", 0.06)


# ---------------- quando usar ----------------
def b_quando(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0 = C["s10.a"], C["s10.b"]
    E.frase(c, t, C["s08"] + 0.1, ps("quando usar", "i", 70) + [("cada uma?", "g", 76, COR)], W / 2, 190, "center", 0.1)
    xs = (360, 960, 1560)
    # média
    cartao(c, t, a8, xs[0], "média")
    E.foco(c, t, a8 + 0.3, 0.5, lambda a: gangorra(c, xs[0], 540, a))
    E.frase(c, t, a8 + 0.5, ps("importa o", "i", 46) + [("total", "g", 50, COR)], xs[0], 690, "center", 0.06)
    fcen(c, t, b8, "média × quantidade = total", xs[0], 790, 40)
    E.frase(c, t, lerp(b8, C["s08.end"], 0.4), ps("sem valores fora do padrão", "i", 38, TINTA2), xs[0], 900, "center", 0.05)
    # mediana
    cartao(c, t, a9, xs[1], "mediana")
    for i, h in enumerate((100, 120, 140, 160, 180)):
        E.foco(c, t, a9 + 0.3 + 0.06 * i, 0.4, lambda a, i=i, h=h: pessoa(c, xs[1] - 180 + 90 * i, 600, h, E.COR if i == 2 else E.mix(TINTA2, PAPEL, 0.35), a))
    E.frase(c, t, a9 + 0.6, ps("valores", "i", 46) + [("extremos", "g", 50, COR)], xs[1], 690, "center", 0.06)
    E.frase(c, t, a9 + 1.6, ps("salário, imóvel, espera", "i", 38, TINTA2), xs[1], 760, "center", 0.05)
    E.frase(c, t, b9, ps("quem está", "i", 42) + [("no meio da fila", "g", 44, COR)], xs[1], 880, "center", 0.05)
    # moda
    cartao(c, t, a0, xs[2], "moda")
    for i, cor in enumerate((E.COR, CATS[1], E.COR, TINTA2, E.COR)):
        E.foco(c, t, a0 + 0.3 + 0.06 * i, 0.4, lambda a, i=i, cor=cor: camisa(c, xs[2] - 190 + 95 * i, 540, 58, a, cor))
    E.frase(c, t, a0 + 0.6, ps("o", "i", 46) + [("mais comum", "g", 50, COR)], xs[2], 690, "center", 0.06)
    E.frase(c, t, a0 + 1.6, ps("tamanho, sabor mais pedido", "i", 38, TINTA2), xs[2], 760, "center", 0.05)
    E.foco(c, t, b0, 0.4, lambda a: E.pilula(c, "a única para cor ou sabor", xs[2], 880, 34, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    ts = [C["s11"]] * 10
    salarios(c, t, ts, risca=a1 + 0.4)
    caixa_mediana(c, t, c1)
    X = 1590
    E.frase(c, t, C["s11"] + 0.1, [("erro comum:", "g", 64, ERRADO)], X, 320, "center")
    E.frase(c, t, a1, ps("jogar fora", "i", 54) + [("o diretor", "g", 58, ERRADO)], X, 440, "center", 0.08)
    E.frase(c, t, a1 + 1.0, ps("para a média ficar justa", "i", 46, TINTA2), X, 510, "center", 0.06)
    E.foco(c, t, b1 - 0.6, 0.4, lambda a: E.selo(c, X - 210, 610, 38, False, a))
    E.frase(c, t, b1, ps("é um", "i", 52) + [("dado real", "g", 56)], X + 30, 630, "center", 0.08)
    E.frase(c, t, c1, ps("a saída: a medida que", "i", 46), X, 760, "center", 0.06)
    E.frase(c, t, c1 + 0.6, [("não se deixa puxar", "g", 50, COR)], X, 830, "center", 0.06)
    E.foco(c, t, c1 + 1.0, 0.4, lambda a: E.pilula(c, "a mediana", X, 940, 56, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def comparar(c, t, t0, y, medx, medianx, rotulo):
    """duas pílulas na mesma linha: mediana e média, com a seta da mediana para a média"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "mediana", medianx, y, 46, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, "média", medx, y, 46, "g", fundo=BR, cor="#07070F", a=a))
    if t >= t0 + 0.5:
        k = ep(t, t0 + 0.5, 0.6)
        d = 1 if medx > medianx else -1
        M.arrow(c, medianx + d * 140, y, lerp(medianx + d * 140, medx - d * 120, k), y, BR, k, 6, 18, k)
    E.frase(c, t, t0 + 0.8, ps(rotulo, "i", 46, CLARO), (medx + medianx) / 2, y + 90, "center", 0.06)


def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4 = C["s14.a"], C["s14.b"]

    def um():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a2, ps("compare a", "i", 64, CLARO) + [("média", "g", 70, BR)] + ps("com a", "i", 64, CLARO) + [("mediana", "g", 70, BR)], W / 2, 270, "center", 0.1)
        comparar(c, t, b2, 440, 1400, 600, "bem acima: valor alto puxando para cima")
        comparar(c, t, c2, 680, 600, 1400, "bem abaixo: valor baixo puxando para baixo")
        E.frase(c, t, lerp(c2, C["s12.end"], 0.6), ps("diferença pequena não prova nada: olhe os dados", "i", 44, CLARO), W / 2, 920, "center", 0.05)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)

    def dois():
        E.frase(c, t, C["s13"] + 0.2, ps("as pistas do enunciado:", "i", 64, CLARO), W / 2, 190, "center", 0.1)
        for k, (ti, pista, med) in enumerate(((a3, "“metade ganha até”, “valor central”", "mediana"), (b3, "“mais comum”, “mais vendido”", "moda"),
                                              (c3, "“dividir o total igualmente”", "média"))):
            y = 370 + 190 * k
            E.frase(c, t, ti, ps(pista, "i", 52, CLARO), 1060, y, "right", 0.06)
            E.foco(c, t, ti + 0.5, 0.4, lambda a, y=y: M.arrow(c, 1100, y - 18, 1260, y - 18, BR, a, 6, 18, 1.0))
            E.foco(c, t, ti + 0.7, 0.4, lambda a, y=y, med=med: E.pilula(c, med, 1450, y - 18, 52, "g", fundo=BR, cor="#07070F", a=a))
    fase(c, t, C["s13"], C["s14"] - 0.1, dois)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.1, ps("a palavra é só pista", "i", 62, CLARO), W / 2, 230, "center", 0.1)
    E.frase(c, t, a4, ps("quem decide é", "i", 70, CLARO) + [("a situação", "g", 76, BR)], W / 2, 380, "center", 0.1)
    E.frase(c, t, b4, ps("eu preciso do...", "i", 56, CLARO), W / 2, 540, "center", 0.08)
    for k, (s, m) in enumerate((("total?", "média"), ("meio?", "mediana"), ("mais comum?", "moda"))):
        x = 520 + 440 * k
        E.foco(c, t, b4 + 0.5 + 0.4 * k, 0.5, lambda a, x=x, s=s, m=m, k=k: (E.bola(c, x, 740, 140 * ease_back(prog(t, b4 + 0.5 + 0.4 * k, 0.5)), a=a),
                                                                       centro(c, s, x, 755, 40 if len(s) < 8 else 32, "g", E.SOBRE, a),
                                                                       centro(c, m, x, 930, 50, "i", CLARO, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar:", "i", 72, COR) + ps("qual medida?", "i", 72), XE, 180, passo=0.12)
    E.frase(c, t, a5, [("1)", "g", 58, COR)] + ps("calçados: o", "i", 56) + [("número que mais sai", "g", 58)], XE, 330, passo=0.08)
    E.frase(c, t, b5, [("2)", "g", 58, COR)] + ps("o", "i", 56) + [("preço típico", "g", 58)] + ps("das casas do bairro", "i", 56), XE, 470, passo=0.08)
    E.frase(c, t, b5 + 1.6, ps("(o bairro tem uma mansão)", "i", 48, TINTA2), XE + 70, 545, passo=0.06)
    E.frase(c, t, c5, [("3)", "g", 58, COR)] + ps("o mesmo valor todo mês", "i", 56), XE, 690, passo=0.08)
    E.frase(c, t, c5 + 1.6, ps("para pagar", "i", 56) + [("a luz do ano inteiro", "g", 58)], XE + 70, 770, passo=0.08)
    E.relogio(c, t, C["s16.a"], 1600, 700, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7 = C["s17.a"], C["s17.b"]
    a8, b8 = C["s18.a"], C["s18.b"]
    linhas = ((a7, "1) calçados", "moda", "o número mais comum"),
              (b7, "2) casas com mansão", "mediana", "a mansão puxaria a média"),
              (a8, "3) luz do ano", "média", "o total ÷ 12 meses"))
    for k, (ti, caso, med, porque) in enumerate(linhas):
        y = 300 + 210 * k
        E.frase(c, t, ti, ps(caso, "i", 56), XE, y, passo=0.08)
        E.foco(c, t, ti + 0.4, 0.4, lambda a, y=y, med=med: E.pilula(c, med, 900, y - 18, 56, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, ti + 1.2, ps(porque, "i", 44, TINTA2), 1080, y, passo=0.06)
    fcen(c, t, b8, "valor por mês = f{total do ano}{12}", W / 2, 960, 60, COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("média:", "g", 70, COR)] + ps("sente cada valor", "i", 64)),
                 ("s19.b", [("mediana:", "g", 70, COR)] + ps("só sente a posição", "i", 64)),
                 ("s19.c", [("moda:", "g", 70, COR)] + ps("mostra o mais comum", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, ps("os dados em", "i", 70) + [("4 partes", "g", 84, COR)], XE, 390, passo=0.12)
    E.frase(c, t, b0, [("os quartis", "g", 110, COR)], XE, 540)
    E.frase(c, t, c0, ps("e o", "i", 60) + [("percentil 90", "g", 66, COR)] + ps("de uma prova", "i", 60), XE, 680, passo=0.1)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, salarios=b_salarios, quando=b_quando, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
