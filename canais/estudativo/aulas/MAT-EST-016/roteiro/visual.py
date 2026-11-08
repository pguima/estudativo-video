"""Visual — Estudativo · MAT-EST-016: desvio médio, variância e desvio padrão.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): tabela que entra coluna a coluna (quadro()), com a
coluna da vez na cor da matéria; conta da vez à direita; resposta na esfera; atalho no palco escuro; fichas para a lista de dados.
Novo nesta aula (para copiar nas próximas):
- DADOS NA RETA = BOLINHAS EMPILHADAS (pontos()): cada valor é uma bolinha sobre a E.reta; valor repetido empilha.
  A média é um fio tracejado vertical com o rótulo em cima (media_fio()).
- DESVIO = SETA da média até o valor (desvio_seta()), com o desvio com sinal em cima; DISTÂNCIA = chave sem sinal.
- DUAS TURMAS (turmas()): duas retas, uma embaixo da outra, com a mesma média; a dispersão se vê no espalhamento.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-016_desvio_medio_variancia_e_desvio_padrao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("desvio", "variancia", "padrao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
TA, TB = [3, 4, 4, 5], [0, 2, 6, 8]          # as duas turmas de média 4
TEMPOS = [2, 4, 5, 6, 8]                       # a questão
assert sum(TA) / 4 == 4 == sum(TB) / 4 and sum([2, 4, 6]) == 12 and 12 / 3 == 4
assert abs(math.sqrt(sum((v - 4) ** 2 for v in TA) / 4) - 0.71) < 0.01 and abs(math.sqrt(sum((v - 4) ** 2 for v in TB) / 4) - 3.16) < 0.01
assert abs(8 / 3 - 2.67) < 0.01 and round(1.6 ** 2, 2) == 2.56 and round(1.7 ** 2, 2) == 2.89 and 2.67 - 2.56 < 2.89 - 2.67
assert sum(TEMPOS) == 25 and sum(abs(v - 5) for v in TEMPOS) == 8 and sum((v - 5) ** 2 for v in TEMPOS) == 20 and 20 / 5 == 4


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


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna (de MAT-EST-001)"""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: E.formula(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a, "center"))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc: centro(c, s, cx, yy, size, "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 and not s[0].isdigit() else "g", cc[0] if cc else TINTA, a))
    return bases


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


def fichas(c, t, t0, itens, x, y, w, size=44, gap=22, passo=0.06):
    """lista de dados em grade de fichas, da esquerda para a direita. itens = [texto]"""
    cx, cy = x, y
    h = size * 1.55
    for i, s in enumerate(itens):
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px = cx + wi / 2
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, cy=cy: ficha(c, s, px, cy, size, a), sobe=8)
        cx += wi + gap


# ================= peças novas da Estatística (dispersão) =================
def pontos(c, t, ts, vx, y, vals, cor=None, r=24, passo=56, desloc=0.0):
    """os dados como bolinhas sobre a reta (y = a linha da reta); valor repetido empilha.
    ts = instante de cada bolinha (ou um só); desloc soma um valor a todos (as bolinhas andam)"""
    ts = ts if isinstance(ts, (list, tuple)) else [ts + 0.12 * i for i in range(len(vals))]
    vistos = {}
    for i, v in enumerate(vals):
        k = vistos.get(v, 0)
        vistos[v] = k + 1
        q = ease_back(prog(t, ts[i], 0.45))
        if q > 0:
            cx, cy = vx(v + desloc), y - r - 8 - k * passo
            c.drawCircle(cx, cy, r * q, M.paint(cor or E.COR))


def media_fio(c, t, t0, x, y0, y1, rotulo, cor=None, size=46, escuro=False):
    """a média: fio tracejado vertical de y0 (em cima) a y1, com o rótulo em cima"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    tinta = cor or (BR if escuro else TINTA)
    M.line(c, x, y1, x, lerp(y1, y0, p), tinta, 1, 4, dash=E.TRACO)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, x, y0 - 16, size, "b", tinta, a), sobe=6)


def desvio_seta(c, t, t0, x0, x1, y, rotulo, cor=None, size=52):
    """o desvio: seta da média (x0) até o valor (x1), com o desvio com sinal em cima"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    M.arrow(c, x0, y, x1, y, cor or COR, 1, 6, 20, p)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rotulo, (x0 + x1) / 2, y - 26, size, "g", cor or COR, a), sobe=6)


def turmas(c, t, t0, ta, tb, ya, yb, x0, x1, rot=True):
    """as duas turmas de média 4: notas de 0 a 8 em duas retas, a turma A em cima"""
    vx = None
    for nome, vals, ti, y in (("turma A", TA, ta, ya), ("turma B", TB, tb, yb)):
        vx = E.reta(c, t, t0, x0, x1, y, 0, 8, list(range(9)), size=40)
        if rot:
            E.foco(c, t, t0 + 0.2, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE - 40, y - 20, 50, "i", TINTA2, a))
        pontos(c, t, ti, vx, y, vals, r=22, passo=50)
    return vx


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        def tit():
            E.frase(c, t, a1, ps("duas turmas, mesma", "i", 72) + [("média: 4", "g", 78, COR)], W / 2, 190, "center", 0.1)
        E.saida(c, t, d1 - 0.1, tit)
        E.frase(c, t, d1, ps("a média", "i", 72) + [("não enxerga", "g", 78, ERRADO)] + ps("a diferença", "i", 72), W / 2, 190, "center", 0.1)
        vx = turmas(c, t, a1, b1, c1, 520, 860, 480, 1480)
        media_fio(c, t, d1, vx(4), 330, 880, "média 4")
        E.foco(c, t, b1 + 0.6, 0.4, lambda a: E.pilula(c, "coladas no 4", 1680, 450, 46, "g", fundo=TINTA2, a=a))
        E.foco(c, t, c1 + 0.6, 0.4, lambda a: E.pilula(c, "de 0 a 8", 1680, 790, 46, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 260, passo=0.14)
        for i, s in enumerate(("desvio médio", "variância", "desvio padrão")):
            E.frase(c, t, tb + 0.9 * i, [(f"{i + 1}.", "g", 70, TINTA2), (s, "g", 92, COR)], XE, 430 + i * 150, passo=0.1)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "a média:", "soma ÷ quantidade"), ("s03.c", "a raiz quadrada, de fração e não exata:", "r{f{9}{16}} = f{3}{4}     r{8} ≈ 2,8"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 74, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 40, y + 180, 60, "g", COR)
    alvo = [250 + i * 290 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 900, "left", 0.1)


# ---------------- o desvio ----------------
RX0, RX1, RY = 360, 1560, 860          # a reta de 0 a 8 dos blocos desvio e desvio médio
VX = lambda v: RX0 + v * (RX1 - RX0) / 8


def reta3(c, t, t0, tp, tm, rotulo="média 4", topo=660):
    """a reta com 2, 4 e 6 e o fio da média"""
    E.reta(c, t, t0, RX0, RX1, RY, 0, 8, list(range(9)), size=42)
    pontos(c, t, tp, VX, RY, [2, 4, 6])
    media_fio(c, t, tm, VX(4), topo, RY, rotulo)


def b_desvio(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    reta3(c, t, C["s04"], [a4, a4 + 0.8, a4 + 1.6], c4 + 0.6)

    def um():
        E.frase(c, t, a4, ps("só", "i", 72) + [("3 valores:", "g", 78, COR)] + ps("2, 4 e 6", "i", 72), W / 2, 200, "center", 0.1)
        fcen(c, t, b4, "2 + 4 + 6 = 12", W / 2, 360, 84)
        fcen(c, t, c4, "12 ÷ 3 = 4", W / 2, 490, 84, COR)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    # as setas dos desvios ficam até o fim do bloco
    desvio_seta(c, t, b5, VX(4), VX(2) + 30, 740, "−2")
    E.foco(c, t, c5, 0.4, lambda a: centro(c, "0", VX(4) + 46, 812, 52, "g", COR, a), sobe=6)
    desvio_seta(c, t, d5, VX(4), VX(6) - 30, 740, "+2")

    def dois():
        E.frase(c, t, a5, [("desvio", "g", 80, COR)] + ps("= valor − média", "i", 72), W / 2, 200, "center", 0.1)
        fcen(c, t, b5, "2 − 4 = −2", 520, 400, 66)
        fcen(c, t, c5, "4 − 4 = 0", W / 2, 400, 66)
        fcen(c, t, d5, "6 − 4 = 2", 1400, 400, 66)
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("a média dos desvios?", "i", 66), W / 2, 190, "center", 0.1)
    fcen(c, t, a6, "−2 + 0 + 2 = 0", W / 2, 330, 84)
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "sempre dá 0", W / 2, 440, 56, "g", fundo=ERRADO, a=a))
    E.frase(c, t, c6, ps("o que", "i", 56) + [("sobra", "g", 60, COR)] + ps("num valor cobre o que", "i", 56) + [("falta", "g", 60, COR)] + ps("no outro", "i", 56),
            W / 2, 545, "center", 0.08)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "o sinal precisa sumir", 760, 1010, 52, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, lerp(d6, C["s06.end"], 0.55), [("2 jeitos", "g", 60, COR)], 1240, 1030, "left")


# ---------------- desvio médio ----------------
def distancias(c, t, ts, y=700):
    """as distâncias até a média: chaves sem sinal sobre a reta"""
    for (x0, x1, s), ti in zip(((VX(2), VX(4), "2"), (VX(4), VX(4), "0"), (VX(4), VX(6), "2")), ts):
        if x1 > x0:
            p = ep(t, ti, 0.5)
            if p > 0:
                E.chave(c, x0 + 6, x1 - 6, y, COR, p, h=-24)
        E.foco(c, t, ti + 0.2, 0.4, lambda a, x0=x0, x1=x1, s=s: centro(c, s, (x0 + x1) / 2, y - 40 - (30 if x0 == x1 else 0), 60, "g", COR, a), sobe=6)


def b_medio(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    reta3(c, t, C["s07"], C["s07"], C["s07"], "", 740)
    E.foco(c, t, C["s07"], 0.4, lambda a: centro(c, "média", VX(4), RY + 140, 40, "i", TINTA2, a))
    distancias(c, t, [c7, c7 + 0.8, c7 + 1.6])

    def um():
        E.frase(c, t, a7, [("1º jeito:", "g", 76, COR)] + ps("esquecer o sinal", "i", 72), W / 2, 200, "center", 0.1)
        E.frase(c, t, b7, ps("só a", "i", 60) + [("distância", "g", 64, COR)] + ps("até a média", "i", 60), W / 2, 330, "center", 0.1)
        E.frase(c, t, b7 + 1.2, ps("sempre positiva", "i", 56, TINTA2), W / 2, 420, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, [("desvio médio", "g", 76, COR)] + ps("= média das distâncias", "i", 66), W / 2, 190, "center", 0.1)
    fcen(c, t, b8, "2 + 0 + 2 = 4", 620, 340, 76)
    fcen(c, t, c8, "4 ÷ 3 = f{4}{3} ≈ 1,3", 620, 500, 76, COR)
    bola_txt(c, t, d8, "f{4}{3}", 1440, 410, 120, 76)
    E.frase(c, t, d8 + 0.4, ps("cada valor fica, em média,", "i", 46, TINTA2), 1440, 590, "center", 0.06)
    E.frase(c, t, d8 + 1.0, ps("a", "i", 46, TINTA2) + [("4/3", "g", 48, COR)] + ps("da média", "i", 46, TINTA2), 1440, 650, "center", 0.06)


# ---------------- variância ----------------
def tab_var(c, t, t0, tq, tsoma, x=150, y=420):
    cols = [("valor", 220, t0), ("desvio", 240, t0), ("desvio^2", 280, tq[0] - 0.3)]
    vez = lambda ti: COR
    linhas = [[("2", t0), ("−2", t0), ("4", tq[0], COR)],
              [("4", t0 + 0.1), ("0", t0 + 0.1), ("0", tq[1], COR)],
              [("6", t0 + 0.2), ("2", t0 + 0.2), ("4", tq[2], COR)]]
    total = [("soma", tsoma), ("", tsoma), ("8", tsoma, COR)] if tsoma is not None else None
    quadro(c, t, x, y, cols, linhas, total, size=62)


def b_variancia(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0, d0, e0, f0, g0 = (C[f"s10.{k}"] for k in "abcdefg")
    X = 1400

    def tab():
        tab_var(c, t, a9 + 0.4, [c9, d9, e9], b0)
    E.saida(c, t, d0 - 0.1, tab)

    def um():
        E.frase(c, t, a9, [("2º jeito:", "g", 76, COR)] + ps("elevar cada desvio", "i", 72) + [("ao quadrado", "g", 76, COR)], W / 2, 200, "center", 0.1)
        E.frase(c, t, b9, ps("negativo ao quadrado", "i", 54), X, 390, "center", 0.1)
        E.frase(c, t, b9 + 1.0, [("vira positivo", "g", 60, CERTO)], X, 460, "center", 0.1)
        fcen(c, t, c9, "(−2)^2 = 4", X, 610, 76)
        fcen(c, t, d9, "0^2 = 0", X, 730, 76)
        fcen(c, t, e9, "2^2 = 4", X, 850, 76)
    fase(c, t, C["s09"], C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return

    def dois():
        E.frase(c, t, a0, [("variância", "g", 80, COR)] + ps("= média dos quadrados", "i", 70), W / 2, 200, "center", 0.1)
        fcen(c, t, b0, "4 + 0 + 4 = 8", X, 480, 76)
        fcen(c, t, c0, "8 ÷ 3 = f{8}{3}", X, 660, 90, COR)
    fase(c, t, C["s10"], d0 - 0.1, dois)
    if t < d0 - 0.1:
        return
    E.frase(c, t, d0, ps("a receita da", "i", 70) + [("variância", "g", 76, COR)], W / 2, 190, "center", 0.1)
    passos = ((d0, "(valor − média)^2", "cada um"), (e0, "somados", ""), (f0, "÷ quantidade de valores", ""))
    for i, (ti, s, sub) in enumerate(passos):
        y = 360 + i * 150
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 50, a=a), centro(c, str(i + 1), 260, y - 4, 56, "g", E.SOBRE, a)))
        E.formula_em(c, t, ti + 0.1, s, 350, y, 70, "g", TINTA)
        if sub:
            E.foco(c, t, ti + 0.5, 0.4, lambda a, s=s, y=y, sub=sub: E.escreve(c, sub, 380 + E.formula(c, s, 0, 0, 70, "g", None, 0), y, 52, "i", TINTA2, a))
    E.foco(c, t, g0, 0.5, lambda a: E.caixa_pontilhada(c, 200, 790, 1520, 210, a, TINTA2))
    E.frase(c, t, g0 + 0.1, ps("dados de uma parte do grupo: alguns livros", "i", 48, TINTA2) + [("÷ (quantidade − 1)", "g", 50, TINTA2)], 240, 870, "left", 0.06)
    E.frase(c, t, lerp(g0, C["s10.end"], 0.62), ps("sem aviso na questão:", "i", 50) + [("÷ quantidade", "g", 54, COR)], 240, 960, "left", 0.08)


# ---------------- desvio padrão ----------------
def b_padrao(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, ps("a variância", "i", 72) + [("muda a unidade", "g", 78, ERRADO)], W / 2, 200, "center", 0.1)
        E.frase(c, t, b1, ps("dados em", "i", 64) + [("metros", "g", 70)], 560, 400, "center", 0.1)
        E.frase(c, t, b1 + 1.2, ps("quadrados em", "i", 64) + [("metros²", "g", 70, ERRADO)], 1360, 400, "center", 0.1)
        E.foco(c, t, b1 + 0.9, 0.4, lambda a: M.arrow(c, 860, 380, 990, 380, TINTA2, a, 5, 18))
        E.frase(c, t, c1, ps("de volta à unidade:", "i", 60) + [("tire a raiz", "g", 66, COR)], W / 2, 590, "center", 0.1)
        E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "desvio padrão", 640, 800, 72, "g", a=a, cor=E.SOBRE))
        E.formula_em(c, t, d1 + 0.4, "= r{variância}", 1000, 826, 90, "g", COR)
    fase(c, t, C["s11"], C["s12"] - 0.1, um)

    def dois():
        E.formula_em(c, t, a2, "r{f{8}{3}}", 520, 420, 150, "g", COR)
        E.frase(c, t, a2 + 1.4, ps("não é exata:", "i", 52, TINTA2) + [("cerque", "g", 56)], 520, 610, "center", 0.1)
        X = 1330
        fcen(c, t, b2, "8 ÷ 3 ≈ 2,67", X, 270, 72)
        fcen(c, t, c2, "1,6^2 = 2,56", X, 400, 72)
        fcen(c, t, d2, "1,7^2 = 2,89", X, 520, 72)
        vx = E.reta(c, t, b2, 900, 1760, 760, 2.5, 2.95, [2.56, 2.67, 2.89], fmt=lambda v: f"{v:.2f}".replace(".", ","), size=44,
                    tm=[c2, b2 + 0.4, d2])
        E.foco(c, t, b2 + 0.4, 0.4, lambda a: c.drawCircle(vx(2.67), 760, 16, M.paint(ERRADO, a)))
        te = lerp(d2, e2, 0.7)
        p1, p2 = ep(t, te, 0.5), ep(t, te + 0.4, 0.5)
        if p1 > 0:
            E.chave(c, vx(2.56) + 6, vx(2.67) - 6, 700, COR, p1, h=-22)
        if p2 > 0:
            E.chave(c, vx(2.67) + 6, vx(2.89) - 6, 700, TINTA2, p2, h=-22)
        E.foco(c, t, te, 0.4, lambda a: centro(c, "mais perto", vx(2.56) + 20, 650, 40, "b", COR, a))
        bola_txt(c, t, e2, "≈ 1,6", 520, 830, 130, 74)
        E.frase(c, t, e2 + 0.4, [("desvio padrão", "g", 50, COR)], 520, 1030, "center")
    fase(c, t, C["s12"], C["s13"] - 0.1, dois)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, C["s13"] + 0.2, ps("e as turmas do começo?", "i", 66), W / 2, 180, "center", 0.1)
    turmas(c, t, C["s13"], C["s13"], C["s13"], 440, 780, 480, 1380)
    E.foco(c, t, a3, 0.5, lambda a: E.pilula(c, "DP ≈ 0,7", 1660, 400, 56, "g", fundo=TINTA2, a=a))
    E.frase(c, t, a3 + 0.5, ps("pequeno", "i", 48, TINTA2), 1660, 500, "center")
    E.foco(c, t, b3, 0.5, lambda a: E.pilula(c, "DP ≈ 3,2", 1660, 740, 56, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, b3 + 0.5, [("grande", "g", 52, COR)], 1660, 840, "center")
    E.frase(c, t, c3, ps("maior desvio padrão =", "i", 56) + [("mais espalhados", "g", 60, COR)], W / 2, 280, "center", 0.08)
    E.frase(c, t, d3, ps("todos iguais, como 4, 4, 4, 4 →", "i", 54) + [("DP = 0", "g", 58, COR)], W / 2, 1000, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    E.frase(c, t, C["s14"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    X = 600
    fcen(c, t, a4, "(−2)^2 = −4", X, 360, 96, ERRADO)
    fcen(c, t, b4, "−4 + 0 + 4 = 0", X, 520, 80, TINTA)
    fcen(c, t, c4, "variância = 0 ?", X, 670, 80, ERRADO)
    if t >= e4:
        E.risco(c, X + 20, 380, X + 300, 290, t, e4, largura=12)
    X2 = 1440
    E.frase(c, t, d4, [("impossível:", "g", 62, ERRADO)], X2, 360, "center", 0.1)
    E.frase(c, t, d4 + 0.7, ps("os valores são diferentes", "i", 50), X2, 440, "center", 0.08)
    for i, s in enumerate(("2", "4", "6")):
        E.foco(c, t, d4 + 1.2 + 0.2 * i, 0.4, lambda a, s=s, i=i: ficha(c, s, X2 - 160 + 160 * i, 560, 56, a), sobe=10)
    fcen(c, t, e4, "(−2) · (−2) = 4", W / 2, 880, 96, CERTO)
    E.foco(c, t, e4 + 0.8, 0.5, lambda a: E.selo(c, W / 2 + 470, 850, 44, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6, f6 = (C[f"s16.{k}"] for k in "abcdef")

    def um():
        E.frase(c, t, C["s15"] + 0.2, ps("o atalho:", "i", 60, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a5, [("+1 ponto", "g", 80, BR)] + ps("na nota de todo mundo", "i", 66, CLARO), W / 2, 270, "center", 0.1)
        E.frase(c, t, b5, ps("desvio padrão:", "i", 62, CLARO) + [("não muda", "g", 72, BR)], W / 2, 400, "center", 0.1)
        x0, x1, y = 360, 1560, 830
        vx = E.reta(c, t, a5, x0, x1, y, 0, 8, list(range(9)), escuro=True, size=42)
        k = ease_io(prog(t, c5, 1.2))
        pontos(c, t, a5 + 0.4, vx, y, [2, 4, 6], cor=CLARO, desloc=k)
        xm = vx(4 + k)
        M.line(c, xm, y, xm, 560, BR, ep(t, a5 + 0.6, 0.5), 4, dash=E.TRACO)
        E.foco(c, t, a5 + 0.6, 0.4, lambda a: centro(c, "média " + ("5" if k > 0.5 else "4"), xm, 540, 44, "b", BR, a))
        if t >= d5:
            for v, s in ((2, "−2"), (6, "+2")):
                p = ep(t, d5, 0.5)
                M.arrow(c, xm, 710, vx(v + k) + (30 if v < 4 else -30), 710, BR, 1, 6, 20, p)
                E.foco(c, t, d5 + 0.3, 0.4, lambda a, v=v, s=s: centro(c, s, (xm + vx(v + k)) / 2, 684, 52, "g", BR, a), sobe=6)
            E.foco(c, t, d5 + 0.3, 0.4, lambda a: centro(c, "0", xm + 44, 770, 52, "g", BR, a), sobe=6)
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, a6, [("× 2", "g", 84, BR)] + ps("em todas as notas", "i", 66, CLARO), W / 2, 190, "center", 0.1)
    E.frase(c, t, b6, ps("desvio padrão", "i", 64, CLARO) + [("× 2", "g", 72, BR)], 560, 350, "center", 0.1)
    E.frase(c, t, c6, ps("variância", "i", 64, CLARO) + [("× 4", "g", 72, BR)], 1360, 350, "center", 0.1)
    fcen(c, t, c6 + 1.4, "(2 · desvio)^2 = 4 · desvio^2", 1360, 480, 54, CLARO)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "só depende da distância até a média", W / 2, 640, 56, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, e6, 0.5, lambda a: E.selo(c, 520, 820, 44, False, a))
    E.frase(c, t, e6 + 0.1, ps("só alguns valores mudam?", "i", 60, CLARO), 600, 842, "left", 0.1)
    E.frase(c, t, f6, [("refaça a conta", "g", 66, BR)], 600, 950, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a7, ps("tempos de espera de 5 clientes", "i", 56) + [("(min)", "g", 54)], XE, 290, passo=0.08)
    fichas(c, t, a7 + 1.0, ["2", "4", "5", "6", "8"], XE, 390, 900, size=60, gap=30, passo=0.12)
    for i, (ti, s) in enumerate(((b7, "a média"), (c7, "o desvio médio"), (d7, "a variância"), (e7, "o desvio padrão"))):
        E.frase(c, t, ti, [(f"{i + 1})", "g", 58, COR)] + ps(s, "i", 58), XE, 560 + i * 110, passo=0.1)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    t0 = C["s19"]
    cols = [("tempo", 200, t0), ("desvio", 220, c9 - 0.3), ("distância", 250, d9 - 0.3), ("desvio^2", 230, a0 - 0.3)]
    des = ["−3", "−1", "0", "1", "3"]
    dis = ["3", "1", "0", "1", "3"]
    qua = ["9", "1", "0", "1", "9"]
    linhas = [[(str(v), t0 + 0.2 + 0.1 * i), (des[i], c9 + 0.5 * i), (dis[i], d9 - 0.2 + 0.1 * i), (qua[i], a0 + 0.5 * i, COR)]
              for i, v in enumerate(TEMPOS)]
    total = [("25", a9), ("", a9), ("8", d9 + 0.5), ("20", b0, COR)]
    quadro(c, t, 110, 330, cols, linhas, total, size=52)
    X = 1460

    def um():
        fcen(c, t, a9, "2 + 4 + 5 + 6 + 8 = 25", X, 280, 56)
        fcen(c, t, b9, "25 ÷ 5 = 5 min", X, 390, 62, COR)
        E.frase(c, t, b9 + 0.6, ps("a média", "i", 44, TINTA2), X, 450, "center")
        E.frase(c, t, c9, ps("desvio = tempo − 5", "i", 52), X, 570, "center", 0.08)
        fcen(c, t, d9, "3 + 1 + 0 + 1 + 3 = 8", X, 690, 56)
        fcen(c, t, e9, "8 ÷ 5 = 1,6 min", X, 810, 64, COR)
        E.frase(c, t, e9 + 0.6, ps("o desvio médio", "i", 44, TINTA2), X, 870, "center")
    fase(c, t, C["s19"], C["s20"] - 0.1, um)
    if t < C["s20"] - 0.1:
        return
    fcen(c, t, b0, "9 + 1 + 0 + 1 + 9 = 20", X, 280, 56)
    fcen(c, t, c0, "20 ÷ 5 = 4", X, 400, 66, COR)
    E.frase(c, t, c0 + 0.6, ps("a variância", "i", 44, TINTA2), X, 460, "center")
    fcen(c, t, d0, "r{4} = 2", X, 600, 76)
    bola_txt(c, t, e0, "2 min", X, 790, 120, 64)
    E.frase(c, t, e0 + 0.4, ps("o desvio padrão", "i", 44, TINTA2), X, 970, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("desvio médio", "g", 66, COR)] + ps("= média das distâncias", "i", 60)),
                 ("s21.b", [("variância", "g", 66, COR)] + ps("= média dos quadrados dos desvios", "i", 60)),
                 ("s21.c", [("desvio padrão", "g", 66, COR)] + ps("= raiz da variância", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s22.{k}"] for k in "abcde")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("interpretar", "g", 100, COR)] + ps("esses números", "i", 80), XE, 410)
    E.frase(c, t, b0, ps("qual atleta é", "i", 56) + [("mais regular?", "g", 60, COR)], XE, 540, passo=0.08)
    E.frase(c, t, c0, [("coeficiente de variação", "g", 64, COR)], XE, 660, passo=0.08)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, desvio=b_desvio, medio=b_medio, variancia=b_variancia, padrao=b_padrao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
