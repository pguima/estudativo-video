"""Visual — Estudativo · MAT-EST-018: praticando médias, mediana, moda e dispersão (5 situações).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e da dispersão de MAT-EST-016/017: lista de dados
em fichas que acendem quando são usadas; dados como bolinhas sobre a reta (pontos()) com a média e a mediana em fios
tracejados (media_fio()); tabela que entra coluna a coluna (quadro()); cartão de grupo (cartao(), de MAT-EST-017);
conta da vez à direita ou embaixo; resposta na esfera; cada situação abre com a pílula "situação n" e fecha no relógio.
Novo nesta aula (para copiar nas próximas):
- BOXPLOT (boxplot()): a escala é uma E.reta só com os cinco números (mín., Q1, mediana, Q3, máx.); bigodes e caixa
  entram em ordem; quartos() escreve "25%" sobre cada pedaço e acende os pedaços pedidos na cor da matéria.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-018_praticando_medias_mediana_moda_e_dispersao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
TEMPOS = [10, 15, 15, 15, 20, 25, 30, 35, 105]
CARLA, DORA = [8, 10, 10, 12], [4, 10, 10, 16]
BOX = (8, 12, 15, 18, 26)
assert sum(TEMPOS) == 270 and 270 / 9 == 30 and sorted(TEMPOS)[4] == 20 and TEMPOS.count(15) == 3 and sum(v <= 30 for v in TEMPOS) == 7
assert (6 * 3 + 8.5 * 2) / 5 == 7 and 7 * 5 == 35 and 35 - 18 == 17 and 17 / 2 == 8.5
assert 26 - 8 == 18 and 18 - 12 == 6
assert sum(CARLA) == sum(DORA) == 40 and sum((v - 10) ** 2 for v in CARLA) == 8 and sum((v - 10) ** 2 for v in DORA) == 72
assert round(1.4 ** 2, 2) == 1.96 and round(4.2 ** 2, 2) == 17.64 and 30 / 200 == 0.15 and 10 / 50 == 0.2


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




def fichas_ac(c, t, t0, itens, x, y, w, size=50, gap=24, passo=0.06, acende=None):
    """lista de dados em fichas; acende(i) -> cor da ficha (ou None). Devolve os centros"""
    cx, cy, cs = x, y, []
    h = size * 1.55
    for i, s in enumerate(itens):
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px = cx + wi / 2
        cor = acende(i) if acende else None
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, cy=cy, cor=cor: ficha(c, s, px, cy, size, a, cor), sobe=8)
        cs.append((px, cy))
        cx += wi + gap
    return cs


def pontos(c, t, ts, vx, y, vals, cor=None, r=24, passo=56, cores=None):
    """os dados como bolinhas sobre a reta (y = a linha da reta); valor repetido empilha (de MAT-EST-016)"""
    ts = ts if isinstance(ts, (list, tuple)) else [ts + 0.12 * i for i in range(len(vals))]
    vistos = {}
    for i, v in enumerate(vals):
        k = vistos.get(v, 0)
        vistos[v] = k + 1
        q = ease_back(prog(t, ts[i], 0.45))
        if q > 0:
            c.drawCircle(vx(v), y - r - 8 - k * passo, r * q, M.paint((cores(i) if cores else None) or cor or E.COR))


def media_fio(c, t, t0, x, y0, y1, rotulo, cor=None, size=44, dx=0):
    """a média: fio tracejado vertical de y0 (em cima) a y1, com o rótulo em cima (de MAT-EST-016)"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.line(c, x, y1, x, lerp(y1, y0, p), cor or TINTA, 1, 4, dash=E.TRACO)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, x + dx, y0 - 14, size, "b", cor or TINTA, a), sobe=6)


def cartao(c, t, t0, x, y, w, h, titulo, linhas, cor=None):
    """um grupo: caixa pontilhada com o nome em cima e uma linha por medida (de MAT-EST-017)"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: centro(c, titulo, x + w / 2, y + 80, 62, "g", cor or COR, a))
    for i, (partes, ti) in enumerate(linhas):
        E.frase(c, t, ti, partes, x + w / 2, y + 160 + i * 74, "center", 0.08)


def boxplot(c, t, t0, x0, x1, y, cinco, vmin, vmax, alto=120, d=0.5):
    """boxplot sobre uma escala só com os cinco números; y = linha da escala. Bigodes, caixa e mediana entram em ordem.
    Devolve vx"""
    vx = E.reta(c, t, t0, x0, x1, y, vmin, vmax, list(cinco), size=46, tm=[t0 + 0.2 + 0.15 * i for i in range(5)])
    mn, q1, md, q3, mx = cinco
    yc = y - 60 - alto / 2
    p = ep(t, t0 + 0.6, d)
    if p > 0:
        M.line(c, vx(mn), yc, lerp(vx(mn), vx(q1), p), yc, TINTA, 1, 5)
        M.line(c, vx(mx), yc, lerp(vx(mx), vx(q3), p), yc, TINTA, 1, 5)
        for v in (mn, mx):
            M.line(c, vx(v), yc - alto * 0.25, vx(v), yc + alto * 0.25, TINTA, p, 5)
    q = ep(t, t0 + 0.6 + d, d)
    if q > 0:
        r = skia.Rect.MakeXYWH(vx(q1), yc - alto / 2, (vx(q3) - vx(q1)) * q, alto)
        c.drawRect(r, M.paint(E.mix(E.COR, PAPEL, 0.8), q))
        c.drawRect(r, M.paint(TINTA, q, stroke=5))
    k = ep(t, t0 + 0.6 + 2 * d, 0.4)
    if k > 0:
        M.line(c, vx(md), yc - alto / 2, vx(md), yc + alto / 2, E.COR, k, 9)
    for v in cinco:   # guias até a escala
        M.line(c, vx(v), yc + alto / 2 if q1 <= v <= q3 else yc + alto * 0.25, vx(v), y - 6, FIO, ep(t, t0 + 1.5, 0.4), 3, dash=E.TRACO)
    return vx


def quartos(c, t, t0, vx, cinco, y, acesos=(), ta=None, size=44):
    """'25%' sobre cada um dos 4 pedaços; os índices de acesos ficam na cor da matéria a partir de ta"""
    for i in range(4):
        a_, b_ = vx(cinco[i]), vx(cinco[i + 1])
        aceso = i in acesos and ta is not None and t >= ta
        cor = COR if aceso else TINTA2
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda a, a_=a_, b_=b_, cor=cor: centro(c, "25%", (a_ + b_) / 2, y, size, "g", cor, a), sobe=6)
        if aceso:
            E.chave(c, a_ + 6, b_ - 6, y + 22, COR, ep(t, ta + 0.15 * i, 0.4), h=22)


def situacao(c, t, t0, n, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"situação {n}" if n != 5 else "última situação", XE + 180, 140, 54, "g", a=a, cor=E.SOBRE))


def relogio(c, t, C, k):
    E.relogio(c, t, C[k], cx=1600, cy=600, r=160)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.frase(c, t, a1, [("5", "g", 160, COR)] + ps("situações", "i", 110), XE, 360, passo=0.14)
    E.frase(c, t, a1 + 1.6, ps("com", "i", 66) + [("todas as medidas", "g", 72, COR)] + ps("do módulo", "i", 66), XE, 490, passo=0.1)
    for i in range(5):
        x = 260 + i * 160
        E.foco(c, t, a1 + 2.4 + 0.15 * i, 0.5, lambda a, i=i, x=x: (E.bola(c, x, 640, 56, a=a), centro(c, str(i + 1), x, 662, 64, "g", E.SOBRE, a)))
    E.relogio(c, t, b1, cx=1480, cy=500, r=200)
    E.frase(c, t, b1 + 1.2, ps("resolva", "i", 62) + [("antes", "g", 66, COR)] + ps("da resposta", "i", 62), 1480, 900, "center", 0.1)
    E.frase(c, t, lerp(b1, C["s01.end"], 0.55), ps("errar aqui", "i", 54, TINTA2) + [("não custa nada", "g", 58)], XE, 860, passo=0.08)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] + 0.15, 0.5, lambda a: E.escreve(c, "grupos", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s02.b", "as médias", "aritmética e com pesos"), ("s02.c", "a posição", "mediana, moda, quartis, boxplot"),
             ("s02.d", "a dispersão", "desvio padrão e coef. de variação"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 180 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 190, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 60, COR)], x + 40, y + 80, "left", 0.1)
        E.frase(c, t, C[k] + 0.5, ps(l2, "i", 50), x + 40, y + 155, "left", 0.06)
    alvo = [180 + i * 230 + 160 for i in range(3)]
    q1 = ease_io(prog(t, C["s02.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s02.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s02.b"], 0.4))
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("travou?", "i", 50, COR) + ps("procure a aula no canal", "i", 50), x, 960, "left", 0.1)


# ---------------- situação 1 ----------------
ITENS1 = [str(v) for v in TEMPOS]


def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    situacao(c, t, a3, 1)
    E.frase(c, t, b3, ps("tempo de 9 pessoas até o trabalho", "i", 56) + [("(min)", "g", 54)], XE, 260, passo=0.08)
    fichas_ac(c, t, b3 + 0.8, ITENS1, XE, 380, 1150, size=56, gap=26)
    E.frase(c, t, c3, ps("calcule:", "i", 58) + [("média, mediana e moda", "g", 62, COR)], XE, 620, passo=0.1)
    E.frase(c, t, d3, ps("qual representa melhor", "i", 56) + [("o tempo típico?", "g", 60, COR)], XE, 720, passo=0.1)
    relogio(c, t, C, "s04.a")


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    def ac(i):
        if t >= e5 and TEMPOS[i] == 15 and t < C["s06"]:
            return TINTA2
        if t >= d5 and i == 4:
            return E.COR
        if t >= b6 and i == 8:
            return ERRADO
        return None
    fichas_ac(c, t, C["s05"], ITENS1, XE, 170, 1700, size=50, gap=22, passo=0.02, acende=ac)

    def um():
        fcen(c, t, a5, "10 + 15 + 15 + 15 + 20 + 25 + 30 + 35 + 105 = 270", W / 2, 360, 54)
        fcen(c, t, b5, "270 ÷ 9 = 30", 560, 500, 72, COR)
        E.frase(c, t, b5 + 0.6, ps("média: 30 min", "i", 46, TINTA2), 560, 570, "center")
        fcen(c, t, c5, "(9 + 1) ÷ 2 = 5", 1360, 500, 72)
        E.frase(c, t, c5 + 0.6, ps("a mediana é o 5º valor", "i", 46, TINTA2), 1360, 570, "center")
        for i, (ti, rot, s) in enumerate(((b5 + 0.8, "média", "30"), (d5, "mediana", "20"), (e5, "moda", "15"))):
            x = 480 + 480 * i
            bola_txt(c, t, ti, s, x, 790, 100, 80, TINTA2 if i == 2 else None)
            E.frase(c, t, ti + 0.3, [(rot, "g", 50, COR)], x, 950, "center")
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t < C["s06"] - 0.1:
        return
    x0, x1, y = 200, 1380, 780
    vx = E.reta(c, t, C["s06"], x0, x1, y, 0, 110, [0, 20, 40, 60, 80, 100], size=40)
    pontos(c, t, C["s06"] + 0.2, vx, y, TEMPOS, r=20, passo=44, cores=lambda i: ERRADO if i == 8 and t >= b6 else None)
    media_fio(c, t, C["s06"] + 0.6, vx(30), 470, y, "média 30", COR, dx=60)
    media_fio(c, t, C["s06"] + 1.0, vx(20), 560, y, "mediana 20", TINTA2, dx=-90)
    E.frase(c, t, a6, ps("a média ficou", "i", 56) + [("bem acima", "g", 60, COR)] + ps("da mediana", "i", 56), W / 2, 330, "center", 0.08)
    E.foco(c, t, b6 + 0.3, 0.4, lambda a: centro(c, "105 puxa", vx(105), 660, 48, "g", ERRADO, a))
    pc = ep(t, c6, 0.5)
    if pc > 0:
        E.chave(c, vx(10) - 20, vx(30) + 20, 880, COR, pc, h=22)
    E.foco(c, t, c6 + 0.3, 0.4, lambda a: centro(c, "7 de 9: até 30 min", vx(20), 960, 46, "g", COR, a))
    bola_txt(c, t, d6, "20 min", 1640, 620, 130, 60)
    E.frase(c, t, d6 + 0.4, ps("tempo típico:", "i", 44, TINTA2), 1640, 820, "center", 0.08)
    E.frase(c, t, d6 + 0.8, [("a mediana", "g", 50, COR)], 1640, 885, "center", 0.08)


# ---------------- situação 2 ----------------
def tab_concurso(c, t, tb, tc, td, te, res=None, tr=None):
    cols = [("prova", 380, tb), ("peso", 200, tb), ("nota", 220, td)]
    nota_d = ("8,5", tr, COR) if res and t >= tr else ("?", te, COR)
    linhas = [[("objetiva", tb), ("3", tb + 0.3), ("6", td)], [("discursiva", tc), ("2", tc + 0.3), nota_d]]
    total = [("média", te), ("", te), ("7", te, COR)]
    quadro(c, t, 140, 380, cols, linhas, total, size=62)


def b_questao2(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    situacao(c, t, a7, 2)
    E.frase(c, t, a7 + 0.6, ps("concurso: nota final =", "i", 56) + [("média com pesos", "g", 60, COR)], XE, 260, passo=0.08)
    tab_concurso(c, t, b7, c7, d7, e7)
    E.frase(c, t, e7 + 0.4, ps("quanto precisa na discursiva", "i", 54) + [("para média 7?", "g", 58, COR)], XE, 820, passo=0.08)
    relogio(c, t, C, "s08.a")


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    tab_concurso(c, t, C["s09"], C["s09"], C["s09"], C["s09"], True, e9)
    X = 1420

    def um():
        E.frase(c, t, C["s09"] + 0.4, ps("total = média × soma dos pesos", "i", 54), X, 200, "center", 0.08)
        fcen(c, t, a9, "3 + 2 = 5", X, 330, 66)
        fcen(c, t, b9, "7 × 5 = 35", X, 450, 66)
        fcen(c, t, c9, "6 × 3 = 18", X, 570, 66)
        fcen(c, t, d9, "35 − 18 = 17", X, 690, 66)
        fcen(c, t, e9, "17 ÷ 2 = 8,5", X, 840, 80, COR)
    fase(c, t, C["s09"], C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.2, ps("pelo atalho das", "i", 54) + [("sobras e faltas", "g", 58, COR)], X, 200, "center", 0.08)
    fcen(c, t, a0, "6: 1 abaixo, peso 3", X, 320, 54)
    fcen(c, t, b0, "faltam 1 × 3 = 3", X, 420, 58, ERRADO)
    fcen(c, t, c0, "3 ÷ 2 = 1,5 acima", X, 520, 58)
    fcen(c, t, d0, "7 + 1,5 = 8,5", X, 640, 70, COR)
    E.foco(c, t, d0 + 0.8, 0.5, lambda a: E.selo(c, X + 290, 620, 38, True, a))
    vx = E.reta(c, t, C["s10"] + 0.3, 1040, 1780, 900, 5, 10, [5, 6, 7, 8, 9, 10], size=40)
    vx = lambda v: 1040 + (v - 5) * 740 / 5
    media_fio(c, t, C["s10"] + 0.5, vx(7), 760, 900, "média 7", TINTA2, 40)
    E.salto(c, t, a0, vx(7), vx(6), 900, 70, ERRADO, "−1 × 3", size=40)
    E.salto(c, t, c0, vx(7), vx(8.5), 900, 70, COR, "+1,5 × 2", size=40)


# ---------------- situação 3 ----------------
BX0, BX1, BY = 220, 1320, 560


def b_questao3(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    situacao(c, t, a1, 3)
    E.frase(c, t, b1, ps("bateria de um celular, em vários testes", "i", 54) + [("(horas)", "g", 52)], XE, 250, passo=0.08)
    boxplot(c, t, b1 + 0.6, BX0, BX1, BY, BOX, 6, 28)
    for i, (ti, s) in enumerate(((c1, "a amplitude?"), (d1, "a largura da caixa?"), (e1, "% dos testes com 12 h ou mais?"))):
        E.frase(c, t, ti, [(f"{i + 1})", "g", 56, COR)] + ps(s, "i", 56), XE, 760 + i * 95, passo=0.08)
    relogio(c, t, C, "s12.a")


def b_resposta3(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"], ps("bateria (h)", "i", 50, TINTA2), XE, 250)
    vx = boxplot(c, t, C["s13"], BX0, BX1, BY, BOX, 6, 28)
    pa = ep(t, a3, 0.5)
    if pa > 0 and t < b3:
        E.chave(c, vx(8), vx(26), BY + 110, ERRADO, pa, h=22)
    pb = ep(t, b3, 0.5)
    if pb > 0 and t < c3:
        E.chave(c, vx(12), vx(18), BY + 110, COR, pb, h=22)
    if t >= c3:
        quartos(c, t, c3 - 0.6, vx, BOX, 330, (1, 2, 3), c3)
    X = 1600
    fcen(c, t, a3, "26 − 8 = 18 h", X, 330, 64, ERRADO)
    E.frase(c, t, a3 + 0.6, ps("amplitude: um número só", "i", 42, TINTA2), X, 390, "center", 0.06)
    fcen(c, t, b3, "18 − 12 = 6 h", X, 530, 64, COR)
    E.frase(c, t, b3 + 0.6, ps("largura da caixa: Q3 − Q1", "i", 42, TINTA2), X, 590, "center", 0.06)
    E.frase(c, t, c3, ps("12 é o", "i", 54) + [("1º quartil:", "g", 58, COR)] + ps("acima dele, 3 pedaços", "i", 54), 760, 820, "center", 0.08)
    bola_txt(c, t, d3, "75%", 1600, 820, 120, 76)


# ---------------- situação 4 ----------------
LX, RX = 520, 1400


def b_questao4(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    situacao(c, t, a4, 4)
    E.frase(c, t, b4, ps("vendas por dia, em 4 dias", "i", 56), XE, 260, passo=0.08)
    for i, (nome, vals) in enumerate((("Carla", CARLA), ("Dora", DORA))):
        y = 390 + i * 140
        E.frase(c, t, b4 + 0.5 + i, [(nome, "g", 62, COR)], XE, y + 20)
        fichas_ac(c, t, b4 + 0.8 + i, [str(v) for v in vals], XE + 240, y, 700, size=58, gap=26)
    E.frase(c, t, c4, ps("calcule a", "i", 56) + [("média", "g", 60, COR)] + ps("e o", "i", 56) + [("desvio padrão", "g", 60, COR)] + ps("de cada uma", "i", 56),
            XE, 720, passo=0.08)
    E.frase(c, t, d4, [("quem é mais regular?", "g", 62, COR)], XE, 830, passo=0.08)
    relogio(c, t, C, "s15.a")


def b_resposta4(c, t, C, b):
    a6, b6, c6, d6, e6, f6 = (C[f"s16.{k}"] for k in "abcdef")
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    for x, nome, vals, ts in ((LX, "Carla", CARLA, a6), (RX, "Dora", DORA, b6)):
        E.frase(c, t, C["s16"], [(nome, "g", 72, COR)], x, 180, "center")
        fcen(c, t, C["s16"] + 0.3, " · ".join(str(v) for v in vals), x, 280, 60, TINTA2)
        fcen(c, t, ts, " + ".join(str(v) for v in vals) + " = 40", x, 390, 56)
    E.frase(c, t, c6, [("40 ÷ 4 = 10:", "g", 62, COR)] + ps("a mesma média", "i", 58), W / 2, 500, "center", 0.08)
    if t >= e7:
        E.foco(c, t, e7, 0.5, lambda a: E.selo(c, LX - 190, 160, 40, True, a))
        E.frase(c, t, e7 + 0.2, [("mais regular", "g", 48, CERTO)], LX + 130, 175, "left")

    def um():
        fcen(c, t, d6, "desvios: −2 · 0 · 0 · 2", LX, 630, 54)
        fcen(c, t, e6, "4 + 0 + 0 + 4 = 8", LX, 740, 58)
        fcen(c, t, f6, "8 ÷ 4 = 2", LX, 860, 66, COR)
        fcen(c, t, a7, "desvios: −6 · 0 · 0 · 6", RX, 630, 54)
        fcen(c, t, b7, "36 + 0 + 0 + 36 = 72", RX, 740, 58)
        fcen(c, t, c7, "72 ÷ 4 = 18", RX, 860, 66, COR)
        E.frase(c, t, f6 + 0.4, ps("variância", "i", 42, TINTA2), LX, 920, "center")
        E.frase(c, t, c7 + 0.4, ps("variância", "i", 42, TINTA2), RX, 920, "center")
        E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "mesma média: nem precisa tirar a raiz", W / 2, 1010, 48, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s16"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, ps("se pedir o desvio padrão,", "i", 54) + [("cerque", "g", 58, COR)], W / 2, 610, "center", 0.08)
    fcen(c, t, a8, "r{2} ≈ 1,4", LX, 750, 76, COR)
    fcen(c, t, b8, "r{18} ≈ 4,2", RX, 750, 76, COR)
    fcen(c, t, c8, "1,4^2 = 1,96", LX, 900, 62)
    fcen(c, t, d8, "4,2^2 = 17,64", RX, 900, 62)
    E.frase(c, t, d8 + 1.4, ps("bem perto", "i", 50, TINTA2), W / 2, 1000, "center")


# ---------------- situação 5 ----------------
def lojas(c, t, ta, tb, x1=140, x2=1020, w=760, y=230, h=260):
    cartao(c, t, ta, x1, y, w, h, "loja A", [(ps("média", "i", 52) + [("200", "g", 60, COR)], ta + 0.3), (ps("desvio padrão", "i", 52) + [("30", "g", 60, COR)], ta + 0.9)])
    cartao(c, t, tb, x2, y, w, h, "loja B", [(ps("média", "i", 52) + [("50", "g", 60, COR)], tb + 0.3), (ps("desvio padrão", "i", 52) + [("10", "g", 60, COR)], tb + 0.9)])


def b_questao5(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    situacao(c, t, a9, 5)
    E.frase(c, t, b9, ps("peças vendidas por dia", "i", 54), XE, 240, passo=0.08)
    lojas(c, t, b9, c9, 140, 740, 560, 300, 260)
    E.frase(c, t, d9, [("qual tem vendas mais regulares?", "g", 62, COR)], XE, 720, passo=0.08)
    relogio(c, t, C, "s20.a")


def b_resposta5(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    lojas(c, t, C["s21"], C["s21"])
    if t >= d1:
        p = ep(t, d1, 0.5)
        E.caixa_pontilhada(c, 126, 216, 788, 288, p, CERTO, prog_=p)
    E.foco(c, t, a1, 0.5, lambda a: E.pilula(c, "médias diferentes → coeficiente de variação", W / 2, 600, 52, "g", a=a, cor=E.SOBRE))
    fcen(c, t, b1, "30 ÷ 200 = 0,15 = 15%", 520, 760, 64, COR)
    fcen(c, t, c1, "10 ÷ 50 = 0,2 = 20%", 1400, 760, 64)
    E.foco(c, t, d1, 0.5, lambda a: E.selo(c, 240, 880, 40, True, a))
    E.frase(c, t, d1 + 0.1, [("loja A mais regular,", "g", 54, CERTO)] + ps("mesmo com DP maior", "i", 50), 300, 900, "left", 0.08)
    E.frase(c, t, e1, ps("comparar", "i", 52) + [("30 com 10", "g", 56, ERRADO)] + ps("= armadilha", "i", 52), 1400, 1000, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s22.a", ps("valor extremo:", "i", 58) + [("mediana", "g", 64, COR)]),
                 ("s22.b", ps("valor que falta:", "i", 58) + [("use o total", "g", 64, COR)]),
                 ("s22.c", ps("mesma média:", "i", 58) + [("desvio padrão", "g", 64, COR)]),
                 ("s22.d", ps("médias diferentes:", "i", 58) + [("coeficiente de variação", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 50, a=a), centro(c, str(i + 1), 200, y - 4, 58, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a0, b0, c0, d0, e0, f0 = (C[f"s23.{k}"] for k in "abcdef")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("desconfiar", "g", 100, COR)] + ps("de gráficos", "i", 80), XE, 410)
    for i, (ti, s) in enumerate(((b0, "eixo que não começa no zero"), (c0, "escala irregular"), (d0, "figura fora de proporção"))):
        E.frase(c, t, ti, [(f"{i + 1}.", "g", 52, COR)] + ps(s, "i", 52), XE, 540 + i * 90, passo=0.08)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, e0 + 0.2, 0.4))
    E.frase(c, t, f0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
