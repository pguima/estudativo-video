"""Visual — Estudativo · MAT-EST-020: números que enganam (amostra ruim, base pequena, correlação e causa).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): PESSOAS = BOLINHAS (pessoas()), a amostra é a
parte que fica forte com um anel e o resto desbota; cartão de grupo (cartao(), de MAT-EST-017); dados como bolinhas
sobre a reta com a média em fio tracejado (MAT-EST-016); linha no tempo = E.serie; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- MANCHETE (manchete()): cartão branco com a faixa preta em cima e a frase em grotesca: o número "de jornal".
- TERCEIRO FATOR (tres()): a causa em cima, as duas coisas que andam juntas embaixo, setas da causa para cada uma e a
  seta entre as duas riscada: correlação não é causa.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-020_numeros_que_enganam.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("amostra", "base", "correlacao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
APAGADO = E.mix(CINZA, PAPEL, 0.6)
assert (2 - 1) / 1 == 1 and (1100 - 1000) / 1000 == 0.1 and 2 - 1 == 1 and (6 - 2) == 4 and 4 / 2 == 2


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




def pessoas(c, t, t0, x, y, cols, lins, passo, r, estado=None, d=0.9):
    """a população em bolinhas (de MAT-EST-001). estado(i, j) -> (cor, anel)"""
    for j in range(lins):
        for i in range(cols):
            cx, cy = x + i * passo, y + j * passo
            k = ease_back(prog(t, t0 + d * (i / max(1, cols - 1)) * 0.8 + 0.02 * j, 0.35))
            cor, anel = (estado(i, j) if estado else (None, False))
            if k > 0:
                c.drawCircle(cx, cy, r * k, M.paint(cor or E.COR))
                if anel:
                    c.drawCircle(cx, cy, (r + 7) * k, M.paint(TINTA, 1, stroke=4))


def cartao(c, t, t0, x, y, w, h, titulo, linhas, cor=None):
    """um grupo: caixa pontilhada com o nome em cima e uma linha por medida (de MAT-EST-017)"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: centro(c, titulo, x + w / 2, y + 80, 60, "g", cor or COR, a))
    for i, (partes, ti) in enumerate(linhas):
        E.frase(c, t, ti, partes, x + w / 2, y + 170 + i * 84, "center", 0.08)


def manchete(c, t, t0, cx, cy, w, linhas, size=64, rot="MANCHETE"):
    """o número de jornal: cartão branco com faixa preta e a frase em grotesca"""
    def fn(a):
        h = 110 + len(linhas) * size * 1.25
        x, y = cx - w / 2, cy - h / 2
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setImageFilter(skia.ImageFilters.Blur(18, 18))
        c.drawRect(skia.Rect.MakeXYWH(x + 10, y + 16, w, h), sh)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR, a))
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, 56), M.paint(TINTA, a))
        E.escreve(c, rot, x + 30, y + 40, 32, "b", BR, a)
        for i, s in enumerate(linhas):
            centro(c, s, cx, y + 56 + size * 1.2 * (i + 1), size, "g", TINTA, a)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=3))
    E.foco(c, t, t0, 0.5, fn)


def no(c, s, cx, cy, size=52, cor=None, a=1.0):
    w = E.larg(s, "g", size) + size * 1.2
    E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, a=a)
    return w


def tres(c, t, tc, t1, t2, tx, causa, ef1, ef2, cx, cy, dx=420, dy=170, size=54):
    """o terceiro fator: causa em cima, efeitos embaixo; setas da causa (t1, t2) e a seta riscada entre os efeitos (tx)"""
    A, B1, B2 = (cx, cy - dy), (cx - dx, cy + dy), (cx + dx, cy + dy)
    for (P, ti) in ((B1, t1), (B2, t2)):
        p = ep(t, ti, 0.5)
        if p > 0:
            ux, uy = P[0] - A[0], P[1] - A[1]
            L = math.hypot(ux, uy)
            M.arrow(c, A[0] + ux / L * 70, A[1] + uy / L * 70, P[0] - ux / L * 70, P[1] - uy / L * 70, TINTA, 1, 6, 22, p)
    if tx is not None:
        p = ep(t, tx, 0.5)
        if p > 0:
            pt = M.paint(TINTA2, p, stroke=5)
            pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
            c.drawLine(B1[0] + 220, B1[1], B2[0] - 220, B2[1], pt)
            M.line(c, B2[0] - 240, B2[1] - 14, B2[0] - 220, B2[1], TINTA2, p, 5)
            M.line(c, B2[0] - 240, B2[1] + 14, B2[0] - 220, B2[1], TINTA2, p, 5)
            k = ep(t, tx + 0.4, 0.4)
            if k > 0:
                M.line(c, cx - 36 * k, B1[1] - 36 * k, cx + 36 * k, B1[1] + 36 * k, ERRADO, 1, 10)
                M.line(c, cx - 36 * k, B1[1] + 36 * k, cx + 36 * k, B1[1] - 36 * k, ERRADO, 1, 10)
    E.foco(c, t, tc, 0.5, lambda a: no(c, causa, *A, size, a=a))
    E.foco(c, t, min(t1, tx if tx is not None else t1), 0.5, lambda a: no(c, ef1, *B1, size, TINTA2, a))
    E.foco(c, t, min(t2, tx if tx is not None else t2), 0.5, lambda a: no(c, ef2, *B2, size, TINTA2, a))


def titulo(c, t, t0, n, s):
    E.frase(c, t, t0, [(n, "g", 66, COR)] + ps(s, "i", 62), W / 2, 160, "center", 0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        manchete(c, t, a1, W / 2, 330, 1300, ["Doença rara: casos sobem 100%", "na cidade"], 70)
        E.frase(c, t, b1 - 1.4, ps("o número que faltou:", "i", 52, TINTA2), W / 2, 600, "center", 0.08)
        E.foco(c, t, b1, 0.5, lambda a: (c.drawCircle(700, 730, 34, M.paint(ERRADO, a)), centro(c, "1 caso", 700, 830, 54, "g", TINTA, a)))
        E.foco(c, t, b1 + 0.4, 0.4, lambda a: M.arrow(c, 830, 730, 1010, 730, TINTA2, a, 6, 20))
        E.foco(c, t, b1 + 0.8, 0.5, lambda a: (c.drawCircle(1180, 730, 34, M.paint(ERRADO, a)), c.drawCircle(1270, 730, 34, M.paint(ERRADO, a)),
                                               centro(c, "2 casos", 1225, 830, 54, "g", TINTA, a)))
        E.foco(c, t, c1, 0.5, lambda a: E.selo(c, 560, 960, 40, True, a))
        E.frase(c, t, c1 + 0.1, ps("a conta está certa,", "i", 56) + ps("e mesmo assim", "i", 56) + [("engana", "g", 62, ERRADO)], 630, 980, "left", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("desconfiar de", "i", 80) + [("3 tipos", "g", 96, COR)], XE, 460, passo=0.12)
        E.frase(c, t, ta + 2.6, ps("de número", "i", 80), XE, 590, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "amostra:", "a parte que a pesquisa ouve"), ("s03.c", "valor extremo:", "puxa a média"),
             ("s03.d", "diferença de porcentagens:", "8% → 10% = 2 pontos percentuais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 180 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 190, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 48), x + 40, y + 70, "left", 0.08)
        E.formula_em(c, t, C[k] + 0.5, l2, x + 40, y + 150, 50, "g", COR)
    alvo = [180 + i * 230 + 160 for i in range(3)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 960, "left", 0.1)


# ---------------- amostra ruim ----------------
GX, GY, GC, GL, GP, GR = 160, 380, 12, 7, 66, 22     # a grade da população
NAO_USA = lambda i, j: (i * 7 + j * 5) % 9 == 0 or (i + 2 * j) % 11 == 0      # quem não usa internet
IRRITADO = lambda i, j: (i * 3 + j * 4) % 7 == 0                               # quem se irritou com o ônibus


def b_amostra(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    titulo(c, t, a4, "1º:", "a amostra ruim")
    X = 1480

    def um():
        def est(i, j):
            if t < c4:
                return None, False
            fora = NAO_USA(i, j)
            q = ep(t, c4, 0.5)
            return (E.mix(E.COR, APAGADO, q) if fora else E.COR), (not fora and q > 0.5)
        pessoas(c, t, C["s04"], GX, GY, GC, GL, GP, GR, est)
        E.frase(c, t, b4, ps("a colher só vale se", "i", 50) + [("a panela foi mexida", "g", 54, COR)], W / 2, 250, "center", 0.08)
        E.frase(c, t, c4, ps("pesquisa feita", "i", 52) + [("só pela internet", "g", 56, COR)], X, 420, "center", 0.08)
        E.frase(c, t, d4, ps("conclusão:", "i", 50), X, 540, "center", 0.08)
        E.frase(c, t, d4 + 0.6, [("quase todo mundo usa", "g", 52, ERRADO)], X, 610, "center", 0.08)
        E.frase(c, t, d4 + 1.2, [("internet todo dia", "g", 52, ERRADO)], X, 675, "center", 0.08)
        E.frase(c, t, e4, ps("as", "i", 50) + [("cinzas", "g", 54, TINTA2)] + ps("nem viram a pesquisa", "i", 50), X, 820, "center", 0.08)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)

    def dois():
        def est(i, j):
            irr = IRRITADO(i, j)
            if t < b5:
                return APAGADO, False
            q = ep(t, b5, 0.5)
            if irr:
                return E.mix(APAGADO, ERRADO, q), q > 0.5
            return APAGADO, False
        pessoas(c, t, C["s05"], GX, GY, GC, GL, GP, GR, est)
        E.frase(c, t, a5, ps("a enquete do ônibus:", "i", 52) + [("só responde quem quer", "g", 56, COR)], W / 2, 250, "center", 0.08)
        E.frase(c, t, b5, ps("irritado", "i", 52, ERRADO) + [("corre para votar", "g", 54, ERRADO)], X, 440, "center", 0.08)
        E.frase(c, t, c5, ps("satisfeito", "i", 52, TINTA2) + [("nem abre", "g", 54, TINTA2)], X, 540, "center", 0.08)
        E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "quem foi ouvido?", X, 700, 54, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, e5, 0.5, lambda a: E.pilula(c, "como foram escolhidos?", X, 820, 54, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, a6, ps("a", "i", 58) + [("renda média", "g", 62, COR)] + ps("do bairro subiu muito?", "i", 58), W / 2, 270, "center", 0.08)
    x0, x1, y = 200, 1700, 760
    vx = lambda v: x0 + v * (x1 - x0) / 60
    if t >= C["s06"]:
        M.arrow(c, x0 - 30, y, x1 + 50, y, TINTA, ep(t, C["s06"], 0.5), 5, 18, ep(t, C["s06"], 0.5))
        E.foco(c, t, C["s06"] + 0.3, 0.4, lambda a: E.escreve(c, "renda", x1 - 100, y + 70, 46, "i", TINTA2, a))
    vals = [10, 11, 12, 12, 13, 13, 14, 15, 15, 16]
    vistos = {}
    for i, v in enumerate(vals):
        k = vistos.get(v, 0); vistos[v] = k + 1
        q = ease_back(prog(t, C["s06"] + 0.3 + 0.08 * i, 0.4))
        if q > 0:
            c.drawCircle(vx(v), y - 22 - k * 30, 13 * q, M.paint(E.COR))
    qr = ease_back(prog(t, b6, 0.6))
    if qr > 0:
        c.drawCircle(vx(58), y - 46, 38 * qr, M.paint(ERRADO))
        E.foco(c, t, b6 + 0.3, 0.4, lambda a: centro(c, "muito rico", vx(58), y - 110, 46, "g", ERRADO, a))
    m0 = sum(vals) / len(vals)
    m1 = (sum(vals) + 58) / (len(vals) + 1)
    xm = vx(lerp(m0, m1, ease_io(prog(t, c6, 1.0))))
    if t >= C["s06"] + 1.2:
        p = ep(t, C["s06"] + 1.2, 0.5)
        M.line(c, xm, y, xm, lerp(y, 520, p), COR, 1, 5, dash=E.TRACO)
        E.foco(c, t, C["s06"] + 1.4, 0.4, lambda a: centro(c, "média", xm, 500, 48, "b", COR, a))
    pc = ep(t, c6 + 0.8, 0.5)
    if pc > 0:
        E.chave(c, vx(9.5), vx(16.5), y + 30, TINTA2, pc, h=22)
        E.foco(c, t, c6 + 1.0, 0.4, lambda a: centro(c, "a maioria continua igual", vx(13), y + 110, 44, "i", TINTA2, a))
    E.frase(c, t, c6, ps("o valor extremo", "i", 52) + [("puxa a média", "g", 56, ERRADO)], W / 2, 360, "center", 0.08)


# ---------------- base pequena ----------------
CX1, CX2, CY, CWW, CH = 140, 1020, 270, 760, 380


def b_base(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")

    def um():
        titulo(c, t, a7, "2º:", "a porcentagem sobre base pequena")
        cartao(c, t, a7 + 0.6, CX1, CY, CWW, CH, "cidade pequena",
               [([("1 → 2 casos", "g", 60)], a7 + 1.2), (ps("alta:", "i", 52) + [("+1 caso", "g", 58, COR)], b7),
                ([("1 ÷ 1 = 1 = 100%", "g", 60, ERRADO)], c7)])
        cartao(c, t, d7, CX2, CY, CWW, CH, "cidade grande",
               [([("1.000 → 1.100", "g", 60)], d7 + 0.3), (ps("alta:", "i", 52) + [("+100 casos", "g", 58, COR)], d7 + 1.0),
                ([("100 ÷ 1.000 = 0,1 = 10%", "g", 56, COR)], e7)])
        E.frase(c, t, C["s08"] + 0.2, ps("qual mudou mais?", "i", 60), W / 2, 760, "center", 0.08)
        E.frase(c, t, a8, ps("em %:", "i", 52) + [("a pequena", "g", 56, ERRADO)], CX1 + CWW / 2, 860, "center", 0.08)
        E.frase(c, t, b8, ps("em pessoas:", "i", 52) + [("a grande", "g", 56, COR)] + ps("(+100 contra +1)", "i", 48, TINTA2), CX2 + CWW / 2, 860, "center", 0.08)
        E.frase(c, t, c8, ps("base pequena: 1 caso vira", "i", 50) + [("% enorme", "g", 54, ERRADO)], W / 2, 960, "center", 0.08)
        E.foco(c, t, d8, 0.5, lambda a: E.pilula(c, "por cento de quanto?", W / 2, 1030, 54, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s07"], C["s09"] - 0.1, um)
    if t < C["s09"] - 0.1:
        return
    E.frase(c, t, C["s09"] + 0.2, ps("o mesmo vale para", "i", 62) + [("taxas", "g", 68, COR)], W / 2, 200, "center", 0.08)
    fcen(c, t, a9, "1% → 2%", W / 2, 400, 130)
    E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "+1 ponto percentual", 560, 580, 60, "g", fundo=TINTA2, a=a))
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "+100%", 1360, 580, 60, "g", fundo=ERRADO, a=a))
    E.frase(c, t, c9 + 1.0, ps("as duas frases são", "i", 52) + [("verdadeiras", "g", 56, CERTO)], W / 2, 710, "center", 0.08)
    manchete(c, t, d9, 1360, 900, 760, ["Taxa sobe 100%!"], 62)
    E.frase(c, t, d9 + 0.5, ps("a manchete escolhe", "i", 50) + [("a que assusta", "g", 54, ERRADO)], 560, 910, "center", 0.08)


# ---------------- correlação e causa ----------------
SORVETE = [90, 85, 70, 55, 40, 30, 28, 32, 45, 60, 75, 88]
AFOGA = [80, 78, 62, 50, 36, 28, 24, 30, 40, 54, 70, 82]
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def b_correlacao(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def um():
        titulo(c, t, a0, "3º:", "a correlação vendida como causa")
        E.frase(c, t, b0, [("correlação:", "g", 58, COR)] + ps("duas coisas que sobem e descem juntas", "i", 54), W / 2, 260, "center", 0.08)
        x, y, w, h = 220, 380, 1300, 460
        E.serie(c, t, c0, [(m, v) for m, v in zip(MESES, SORVETE)], x, y, w, h, vmin=0, vmax=100, marcas=[], valores=False, size=38)
        E.serie(c, t, d0, [(m, v) for m, v in zip(MESES, AFOGA)], x, y, w, h, vmin=0, vmax=100, marcas=[], valores=False, eixos=False,
                cor=TINTA2, size=38)
        E.foco(c, t, c0 + 1.8, 0.4, lambda a: E.escreve(c, "sorvete vendido", x + w + 20, y + h - 0.9 * h - 6, 44, "g", COR, a))
        E.foco(c, t, d0 + 1.8, 0.4, lambda a: E.escreve(c, "afogamentos", x + w + 20, y + h - 0.8 * h + 50, 44, "g", TINTA2, a))
    fase(c, t, C["s10"], C["s11"] - 0.1, um)

    def dois():
        E.frase(c, t, C["s11"] + 0.2, ps("sorvete causa afogamento?", "i", 62), W / 2, 190, "center", 0.08)
        E.frase(c, t, a1, [("não", "g", 90, ERRADO)], W / 2, 320, "center")
        tres(c, t, b1, c1, d1, a1 + 0.3, "calor", "mais sorvete", "mais gente nadando", W / 2, 650)
        E.frase(c, t, e1, ps("dependem do", "i", 54) + [("mesmo motivo,", "g", 58, COR)] + ps("não uma da outra", "i", 54), W / 2, 1010, "center", 0.08)
    fase(c, t, C["s11"], C["s12"] - 0.1, dois)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"] + 0.2, ps("antes de aceitar uma causa,", "i", 62) + [("pergunte:", "g", 66, COR)], W / 2, 200, "center", 0.08)
    for i, (ti, s) in enumerate(((a2, "existe um terceiro fator?"), (b2, "a causa pode ser ao contrário?"), (c2, "pode ser coincidência?"))):
        y = 370 + i * 150
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 22, 46, a=a), centro(c, str(i + 1), 420, y - 2, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, ps(s, "i", 62), 500, y, "left", 0.08)
    E.foco(c, t, d2, 0.5, lambda a: E.caixa_pontilhada(c, 300, 790, 1320, 200, a, TINTA2))
    E.frase(c, t, d2 + 0.1, ps("provar causa:", "i", 52, TINTA2) + [("experimentos com grupos comparáveis", "g", 54)], W / 2, 880, "center", 0.08)
    E.frase(c, t, d2 + 1.0, ps("assunto que vai além desta aula", "i", 44, TINTA2), W / 2, 950, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 160, "center", 0.1)
    E.frase(c, t, a3, ps("amostra", "i", 56) + [("grande", "g", 60)] + ps("conserta amostra", "i", 56) + [("mal escolhida?", "g", 60, ERRADO)], W / 2, 250, "center", 0.08)

    def est(i, j):
        canto = i <= 5 and j <= 3
        if t < d3:
            return (E.COR if canto else APAGADO) if t >= b3 else E.COR, canto and t >= b3
        return (ERRADO if canto else APAGADO), canto
    pessoas(c, t, C["s13"], 160, 380, 12, 7, 66, 22, est)
    if t >= d3:
        p = ep(t, d3, 0.5)
        E.caixa_pontilhada(c, 120, 340, 6 * 66 - 66 + 80, 4 * 66 - 66 + 80, p, ERRADO, prog_=p)
    X = 1460
    E.frase(c, t, b3, [("50.000 votos", "g", 72, COR)], X, 420, "center", 0.08)
    E.frase(c, t, b3 + 0.8, ps("no site de um time", "i", 52), X, 500, "center", 0.08)
    E.frase(c, t, c3, ps("→ o preferido", "i", 54) + [("do país?", "g", 58, ERRADO)], X, 620, "center", 0.08)
    E.frase(c, t, d3, ps("só votou quem", "i", 50) + [("visita o site", "g", 54, ERRADO)], X, 740, "center", 0.08)
    E.frase(c, t, e3, ps("colher maior, de um canto só,", "i", 50), W / 2, 930, "center", 0.08)
    E.frase(c, t, e3 + 1.2, [("continua de um canto só", "g", 58, ERRADO)], W / 2, 1010, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 60, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a4, [("3 perguntas", "g", 80, BR)] + ps("para qualquer número de manchete", "i", 60, CLARO), W / 2, 270, "center", 0.1)
        for i, (ti, s, tr) in enumerate(((b4, "quem foi ouvido?", "amostra"), (c4, "por cento de quanto?", "base pequena"), (d4, "o que mais mudou junto?", "correlação"))):
            y = 450 + i * 160
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 22, 46, a=a), centro(c, str(i + 1), 330, y - 2, 54, "g", E.SOBRE, a)))
            E.frase(c, t, ti + 0.1, [(s, "g", 70, BR)], 410, y, "left", 0.08)
            E.frase(c, t, ti + 0.6, [("→", "g", 48, CLARO), (tr, "i", 52, CLARO)], 1300, y, "left", 0.05)
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, a5, ps("a conta pode estar", "i", 60, CLARO) + [("certa", "g", 66, BR)] + ps("e a conclusão", "i", 60, CLARO) + [("errada", "g", 66, BR)],
            W / 2, 260, "center", 0.08)
    E.frase(c, t, b5, ps("as perguntas olham", "i", 56, CLARO) + [("de onde o número veio", "g", 62, BR)], W / 2, 380, "center", 0.08)
    E.foco(c, t, c5, 0.5, lambda a: E.selo(c, 300, 600, 44, False, a))
    E.frase(c, t, c5 + 0.1, ps("não compensa:", "i", 56, CLARO) + [("o enunciado garante a amostra e dá os números", "g", 52, BR)], 380, 620, "left", 0.06)
    E.frase(c, t, d5, ps("aí,", "i", 64, CLARO) + [("vá direto à conta", "g", 72, BR)], W / 2, 820, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6 = C["s16.a"], C["s16.b"]
    a7, b7 = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 150, passo=0.12)
    E.frase(c, t, C["s16"] + 1.2, ps("diga o problema de cada conclusão", "i", 52, TINTA2), XE, 230, passo=0.08)
    blocos = ((a6, "1)", ["pesquisa na porta de uma academia:", "70% da cidade faz exercício"]),
              (b6, "2)", ["furtos de bicicleta +200%:", "de 2 para 6. a conta está certa?"]),
              (a7, "3)", ["quem toma café da manhã tira nota maior:", "logo, o café faz a nota subir"]))
    for i, (ti, n, (l1, l2)) in enumerate(blocos):
        y = 360 + i * 230
        E.frase(c, t, ti, [(n, "g", 60, COR)] + ps(l1, "i", 52), XE, y, passo=0.06)
        t2 = b7 if i == 2 else ti + 1.2
        E.frase(c, t, t2, [(l2, "g", 54, TINTA)], XE + 70, y + 80, passo=0.06)
    E.relogio(c, t, C["s18.a"], cx=1620, cy=520, r=160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9 = C["s19.a"], C["s19.b"]
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")

    def um():
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "caso 1: amostra ruim", W / 2, 230, 64, "g", fundo=ERRADO, a=a))

        def est(i, j):
            canto = i >= 7 and j <= 2
            return (E.COR if canto else APAGADO) if t >= b9 else E.COR, canto and t >= b9
        pessoas(c, t, C["s19"], 160, 420, 12, 7, 66, 22, est)
        if t >= b9:
            p = ep(t, b9, 0.5)
            E.caixa_pontilhada(c, 160 + 7 * 66 - 40, 380, 5 * 66 + 14, 3 * 66 + 14, p, ERRADO, prog_=p)
        E.frase(c, t, b9, ps("na porta da academia,", "i", 52), 1440, 500, "center", 0.08)
        E.frase(c, t, b9 + 0.8, [("quase todos se exercitam", "g", 54, COR)], 1440, 580, "center", 0.08)
        E.frase(c, t, b9 + 2.0, ps("a colher veio de", "i", 50) + [("um canto só", "g", 54, ERRADO)], 1440, 720, "center", 0.08)
    fase(c, t, C["s19"], C["s20"] - 0.1, um)

    def dois():
        E.foco(c, t, a0, 0.5, lambda a: E.pilula(c, "caso 2: a conta está certa", W / 2, 230, 64, "g", fundo=CERTO, a=a))
        fcen(c, t, b0, "6 − 2 = 4", W / 2, 420, 90)
        fcen(c, t, c0, "4 ÷ 2 = 2 = 200%", W / 2, 570, 90, COR)
        E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "mas a base é pequena: só 4 furtos a mais", W / 2, 760, 56, "g", fundo=ERRADO, a=a))
        E.frase(c, t, d0 + 1.6, ps("olhe o número de casos, não só a porcentagem", "i", 50, TINTA2), W / 2, 890, "center", 0.06)
    fase(c, t, C["s20"], C["s21"] - 0.1, dois)
    if t < C["s21"] - 0.1:
        return
    E.foco(c, t, a1, 0.5, lambda a: E.pilula(c, "caso 3: correlação não prova causa", W / 2, 200, 60, "g", fundo=ERRADO, a=a))
    tres(c, t, b1, b1 + 1.0, c1, d1, "rotina organizada", "café da manhã", "estudo", W / 2, 560, dx=440)
    E.frase(c, t, d1 + 0.4, ps("andam juntas", "i", 54) + [("≠", "g", 60, ERRADO)] + ps("uma causa a outra", "i", 54), W / 2, 960, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", ps("confira", "i", 60) + [("quem foi ouvido", "g", 66, COR)]),
                 ("s22.b", ps("pergunte", "i", 60) + [("por cento de quanto", "g", 66, COR)]),
                 ("s22.c", ps("procure", "i", 60) + [("o terceiro fator", "g", 66, COR)] + ps("antes de aceitar uma causa", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a0, b0, c0, d0 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("praticar", "g", 100, COR)] + ps("gráficos e pesquisas", "i", 76), XE, 410)
    E.frase(c, t, b0, ps("a conclusão", "i", 58) + [("se sustenta nos dados?", "g", 62, COR)], XE, 560, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, amostra=b_amostra, base=b_base, correlacao=b_correlacao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
