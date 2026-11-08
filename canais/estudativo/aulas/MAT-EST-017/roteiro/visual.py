"""Visual — Estudativo · MAT-EST-017: interpretar a dispersão (regularidade e coeficiente de variação).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e da dispersão de MAT-EST-016: dados como bolinhas
empilhadas sobre a reta (pontos()), média como fio tracejado (media_fio()); tabela que entra coluna a coluna (quadro());
conta da vez embaixo ou à direita; resposta na esfera; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- CARTÃO DE GRUPO (cartao()): caixa pontilhada com o nome do grupo em cima e uma linha por medida (média, DP, CV), cada
  linha no marcador em que a fala diz o número.
- PESO DO DESVIO (peso()): barra cinza do tamanho da média com a parte do desvio padrão na cor da matéria: mostra quanto
  o desvio "pesa" na média, que é a ideia do coeficiente de variação.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-017_interpretar_a_dispersao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ler", "saltos", "cv", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
ANA, BIA = [5.8, 6.2, 6.2, 5.8], [5.3, 6.7, 5.9, 6.1]
_var = lambda v: sum((x - sum(v) / len(v)) ** 2 for x in v) / len(v)
assert abs(sum(ANA) / 4 - 6) < 1e-9 and abs(sum(BIA) / 4 - 6) < 1e-9 and abs(_var(ANA) - 0.04) < 1e-9 and abs(_var(BIA) - 0.25) < 1e-9
assert abs(0.6 / 12 - 0.05) < 1e-12 and abs(1 / 50 - 0.02) < 1e-12 and abs(2 / 40 - 0.05) < 1e-12 and abs(2.4 / 80 - 0.03) < 1e-12
assert abs(math.sqrt(0.64) - 0.8) < 1e-12 and abs(math.sqrt(0.25) - 0.5) < 1e-12


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




def pontos(c, t, ts, vx, y, vals, cor=None, r=24, passo=56):
    """os dados como bolinhas sobre a reta (y = a linha da reta); valor repetido empilha (de MAT-EST-016)"""
    ts = ts if isinstance(ts, (list, tuple)) else [ts + 0.12 * i for i in range(len(vals))]
    vistos = {}
    for i, v in enumerate(vals):
        k = vistos.get(v, 0)
        vistos[v] = k + 1
        q = ease_back(prog(t, ts[i], 0.45))
        if q > 0:
            c.drawCircle(vx(v), y - r - 8 - k * passo, r * q, M.paint(cor or E.COR))


def media_fio(c, t, t0, x, y0, y1, rotulo, cor=None, size=44):
    """a média: fio tracejado vertical de y0 (em cima) a y1, com o rótulo em cima (de MAT-EST-016)"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.line(c, x, y1, x, lerp(y1, y0, p), cor or TINTA, 1, 4, dash=E.TRACO)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, x, y0 - 14, size, "b", cor or TINTA, a), sobe=6)


def cartao(c, t, t0, x, y, w, h, titulo, linhas, cor=None, apaga=0.0):
    """um grupo: caixa pontilhada com o nome em cima e uma linha por medida. linhas = [(partes de E.frase, t)]"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    if apaga > 0:
        pa = skia.Paint(); pa.setAlphaf(1 - 0.65 * apaga); c.saveLayer(None, pa)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: centro(c, titulo, x + w / 2, y + 80, 62, "g", cor or COR, a))
    for i, (partes, ti) in enumerate(linhas):
        E.frase(c, t, ti, partes, x + w / 2, y + 160 + i * 74, "center", 0.08)
    if apaga > 0:
        c.restore()


def peso(c, t, t0, x, y, w, parte, total, rot, h=44):
    """quanto o desvio pesa na média: barra cinza = média, parte na cor da matéria = desvio padrão"""
    q = ease_io(prog(t, t0, 0.6))
    if q <= 0:
        return
    M.rrect(c, x, y, w * q, h, 10, E.mix(FIO, PAPEL, 0.3), 1.0)
    k = ease_io(prog(t, t0 + 0.5, 0.5))
    if k > 0:
        M.rrect(c, x, y, max(12, w * parte / total) * k, h, 10, E.COR, 1.0)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rot, x, y - 18, 44, "b", TINTA2, a))


def reta_saltos(c, t, t0, x0, x1, y, nome, vals, ts, tm):
    vx = E.reta(c, t, t0, x0, x1, y, 5, 7, [5, 5.5, 6, 6.5, 7], fmt=lambda v: E._num(v).replace(".", ","), size=36)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, nome, XE - 40, y - 10, 52, "g", COR, a))
    pontos(c, t, ts, vx, y, vals, r=20, passo=44)
    media_fio(c, t, tm, vx(6), y - 130, y, "")
    return vx


# ---------------- gancho ----------------
CX1, CX2, CY, CWW, CH = 140, 1020, 200, 760, 330    # os dois cartões dos corredores


def corredores(c, t, t0a, t0b, linhas_a, linhas_b, apaga_a=0.0, apaga_b=0.0, h=CH):
    cartao(c, t, t0a, CX1, CY, CWW, h, "corredor de 100 m", linhas_a, apaga=apaga_a)
    cartao(c, t, t0b, CX2, CY, CWW, h, "corredor de 400 m", linhas_b, apaga=apaga_b)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        corredores(c, t, a1, b1, [(ps("desvio padrão", "i", 54) + [("0,6 s", "g", 64, COR)], a1 + 0.6)],
                   [(ps("desvio padrão", "i", 54) + [("1 s", "g", 64, COR)], b1 + 0.6)], apaga_a=ep(t, d1, 0.5), h=250)
        E.frase(c, t, b1 + 2.4, ps("quem é", "i", 72) + [("mais regular?", "g", 78, COR)], W / 2, 640, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "quase todo mundo: 100 m", CX1 + CWW / 2, 800, 52, "g", fundo=ERRADO, a=a))
        E.foco(c, t, d1, 0.5, lambda a: E.selo(c, CX2 + CWW / 2 - 200, 790, 50, True, a))
        E.frase(c, t, d1 + 0.2, [("é o de 400 m", "g", 66, CERTO)], CX2 + CWW / 2 - 120, 815, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("ler o", "i", 80) + [("desvio padrão", "g", 90, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 3.0, ps("comparar", "i", 80) + [("médias diferentes", "g", 90, COR)], XE, 590, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "o desvio padrão, na unidade dos dados:", "r{variância}"), ("s03.c", "quantos por cento a parte é do total:", "parte ÷ total"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 74, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 40, y + 180, 64, "g", COR)
    alvo = [250 + i * 290 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 900, "left", 0.1)


# ---------------- ler o desvio padrão ----------------
def b_ler(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.2, ps("o que o", "i", 72) + [("desvio padrão", "g", 78, COR)] + ps("diz?", "i", 72), W / 2, 180, "center", 0.1)
    E.frase(c, t, a4, ps("o quanto os valores", "i", 56) + [("costumam se afastar", "g", 60, COR)] + ps("da média", "i", 56), W / 2, 290, "center", 0.08)
    for k, (t0, x0, vals, tit, l1, l2, cor) in enumerate(((b4, 140, [4, 4, 5, 5, 5, 6, 6], "pequeno", "valores perto da média", "homogêneo · regular", TINTA2),
                                                          (c4, 1020, [1, 2, 4, 5, 6, 8, 9], "grande", "valores espalhados", "heterogêneo · irregular", COR))):
        x1 = x0 + 760
        vx = E.reta(c, t, t0, x0 + 30, x1 - 30, 640, 0, 10, [], size=36)
        vx = lambda v, x0=x0, x1=x1: x0 + 30 + v * (x1 - x0 - 60) / 10
        pontos(c, t, t0 + 0.2, vx, 640, vals, r=20, passo=44)
        media_fio(c, t, t0 + 0.6, vx(5), 450, 640, "média")
        E.frase(c, t, t0, ps("desvio padrão", "i", 54) + [(tit, "g", 60, cor if cor != TINTA2 else TINTA)], (x0 + x1) / 2, 760, "center", 0.08)
        E.frase(c, t, t0 + 0.8, ps(l1, "i", 46, TINTA2), (x0 + x1) / 2, 840, "center", 0.06)
        E.foco(c, t, t0 + 1.4, 0.5, lambda a, l2=l2, x0=x0, x1=x1, cor=cor: E.pilula(c, l2, (x0 + x1) / 2, 940, 48, "g", fundo=cor, a=a))


# ---------------- Ana e Bia ----------------
def tab_saltos(c, t, ta, tb, tc, td, cor_dp=(TINTA, TINTA)):
    cols = [("atleta", 200, ta), ("saltos (m)", 700, ta), ("média", 220, tb), ("DP", 220, tc)]
    linhas = [[("Ana", ta + 0.3, COR), ("5,8 · 6,2 · 6,2 · 5,8", ta + 0.5), ("6 m", tb), ("0,2 m", tc, cor_dp[0])],
              [("Bia", ta + 1.0, COR), ("5,3 · 6,7 · 5,9 · 6,1", ta + 1.2), ("6 m", tb + 0.3), ("0,5 m", td, cor_dp[1])]]
    quadro(c, t, 260, 230, cols, linhas, size=56)


def b_saltos(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, C["s05"] + 0.2, ps("duas atletas de", "i", 60) + [("salto em distância", "g", 64, COR)], W / 2, 120, "center", 0.1)
    tab_saltos(c, t, a5, b5, c5, d5, (CERTO if t >= a6 else TINTA, TINTA))
    if t >= a6:   # o anel na linha da Ana
        p = ep(t, a6, 0.5)
        E.caixa_pontilhada(c, 240, 268, 1380, 82, p, CERTO, prog_=p)

    def retas():
        reta_saltos(c, t, a5 + 0.6, 380, 1500, 700, "Ana", ANA, a5 + 0.9, b5)
        reta_saltos(c, t, a5 + 1.4, 380, 1500, 930, "Bia", BIA, a5 + 1.7, b5)
    fase(c, t, C["s05"], a6 - 0.1, retas)
    if t < a6 - 0.1:
        return
    E.foco(c, t, a6, 0.5, lambda a: E.selo(c, 300, 600, 44, True, a))
    E.frase(c, t, a6 + 0.1, [("Ana é mais regular:", "g", 62, CERTO)] + ps("o desvio padrão dela é menor", "i", 56), 370, 622, "left", 0.08)
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "precisa de um salto seguro? leva a Ana", W / 2, 730, 50, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, c6, ps("mas", "i", 60) + [("regular ≠ melhor", "g", 66, ERRADO)], W / 2, 860, "center", 0.1)
    E.frase(c, t, c6 + 1.4, ps("salta mais longe →", "i", 52) + [("média", "g", 58, COR)], 540, 980, "center", 0.08)
    E.frase(c, t, d6, ps("regularidade →", "i", 52) + [("desvio padrão", "g", 58, COR)], 1380, 980, "center", 0.08)


# ---------------- coeficiente de variação ----------------
def b_cv(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    corredores(c, t, C["s07"], C["s07"] + 0.2,
               [(ps("média", "i", 52) + [("12 s", "g", 60, COR)], a7), (ps("desvio padrão", "i", 52) + [("0,6 s", "g", 60, COR)], a7 + 1.6),
                (ps("coef. de variação", "i", 52) + [("5%", "g", 60, COR)], c9 + 2.0)],
               [(ps("média", "i", 52) + [("50 s", "g", 60, COR)], b7), (ps("desvio padrão", "i", 52) + [("1 s", "g", 60, COR)], b7 + 1.6),
                (ps("coef. de variação", "i", 52) + [("2%", "g", 60, COR)], d9 + 2.0)], h=CH + 30)
    if t >= b0:   # o mais regular
        p = ep(t, b0, 0.5)
        E.caixa_pontilhada(c, CX2 - 14, CY - 14, CWW + 28, CH + 58, p, CERTO, prog_=p)
    tp = lerp(C["s08"], a8, 0.5)
    peso(c, t, tp, CX1 + 40, 650, CWW - 80, 0.6, 12, "0,6 s em 12 s")
    peso(c, t, C["s08"] + 0.3, CX2 + 40, 650, CWW - 80, 1, 50, "1 s em 50 s")

    def s8():
        E.foco(c, t, tp + 0.3, 0.4, lambda a: centro(c, "pesa mais", CX1 + CWW / 2, 760, 46, "i", TINTA2, a))
        E.foco(c, t, C["s08"] + 0.6, 0.4, lambda a: centro(c, "pesa pouco", CX2 + CWW / 2, 760, 46, "i", TINTA2, a))
        E.frase(c, t, a8, ps("o desvio padrão é", "i", 58) + [("quantos % da média?", "g", 64, COR)], W / 2, 880, "center", 0.08)
        E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "coeficiente de variação", W / 2, 990, 56, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s08"], C["s09"] - 0.1, s8)

    def s9():
        E.frase(c, t, a9, ps("parte ÷ total →", "i", 56), 560, 820, "center", 0.08)
        E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "CV = desvio padrão ÷ média", 1240, 800, 52, "g", a=a, cor=E.SOBRE))
        fcen(c, t, c9, "0,6 ÷ 12 = 0,05 = 5%", CX1 + CWW / 2, 960, 62, COR)
        fcen(c, t, d9, "1 ÷ 50 = 0,02 = 2%", CX2 + CWW / 2, 960, 62, COR)
    fase(c, t, C["s09"], C["s10"] - 0.1, s9)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, a0, [("menor CV", "g", 64, COR)] + ps("= mais regular", "i", 60), W / 2, 800, "center", 0.1)
    E.frase(c, t, b0 + 0.3, ps("o de 400 m varia só", "i", 50, TINTA2) + [("2%", "g", 54, CERTO)] + ps("do próprio tempo", "i", 50, TINTA2), W / 2, 880, "center", 0.06)
    E.frase(c, t, c0, ps("sem unidade:", "i", 52) + [("s ÷ s", "g", 56, COR)] + ps("se cancela", "i", 52), 560, 1000, "center", 0.08)
    E.frase(c, t, d0, ps("compara", "i", 52) + [("unidades diferentes", "g", 56, COR)], 1400, 1000, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s11"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    E.frase(c, t, a1, ps("comparar os desvios padrão com", "i", 56) + [("médias diferentes", "g", 60, ERRADO)], W / 2, 260, "center", 0.08)
    X = 520
    fcen(c, t, b1, "0,6 < 1", X, 440, 110, ERRADO)
    E.frase(c, t, b1 + 1.0, ps("→ escolhe o de", "i", 54) + [("100 m?", "g", 58, ERRADO)], X, 540, "center", 0.08)
    if t >= c1:
        E.risco(c, X - 260, 560, X + 260, 380, t, c1 + 1.0, largura=12)
    E.colunas(c, t, c1, [("100 m", 12, E.COR), ("400 m", 50, TINTA2)], 1180, 380, 560, 260, vmax=56, deitado=True,
              fmt=lambda v: f"{v} s", size=46)
    E.frase(c, t, c1 + 0.4, ps("quanto dura cada prova", "i", 46, TINTA2), 1340, 360, "center", 0.06)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "divida cada um pela sua média", W / 2, 780, 58, "g", a=a, cor=E.SOBRE))
    fcen(c, t, d1 + 0.8, "0,6 ÷ 12          1 ÷ 50", W / 2, 920, 70)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def um():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho:", "i", 60, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a2, ps("mesma média:", "i", 62, CLARO) + [("compare as variâncias", "g", 68, BR)], W / 2, 280, "center", 0.1)
        E.frase(c, t, a2 + 1.4, ps("sem tirar a raiz", "i", 54, CLARO), W / 2, 360, "center", 0.1)
        for i, (nome, v, ti) in enumerate((("Ana", "0,04", b2), ("Bia", "0,25", c2))):
            x = 640 + 640 * i
            E.foco(c, t, ti, 0.5, lambda a, nome=nome, x=x: centro(c, nome, x, 520, 60, "i", CLARO, a))
            fcen(c, t, ti + 0.1, v, x, 680, 130, BR)
        E.foco(c, t, d2, 0.5, lambda a: E.caixa_pontilhada(c, 640 - 230, 430, 460, 320, a, CLARO))
        E.frase(c, t, d2 + 0.3, ps("a menor →", "i", 60, CLARO) + [("mais regular", "g", 66, BR)], W / 2, 880, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, C["s13"] + 0.1, ps("funciona porque", "i", 60, CLARO), W / 2, 190, "center", 0.1)
    E.frase(c, t, a3, [("número maior", "g", 68, BR)] + ps("tem", "i", 62, CLARO) + [("raiz maior", "g", 68, BR)], W / 2, 300, "center", 0.1)
    fcen(c, t, a3 + 1.2, "r{0,04} = 0,2   <   r{0,25} = 0,5", W / 2, 450, 76, CLARO)
    E.foco(c, t, b3, 0.5, lambda a: E.selo(c, 470, 640, 44, False, a))
    E.frase(c, t, b3 + 0.1, ps("não compensa:", "i", 60, CLARO) + [("médias diferentes", "g", 64, BR)], 550, 662, "left", 0.1)
    E.frase(c, t, c3, ps("aí: desvio padrão", "i", 60, CLARO) + [("÷ média", "g", 70, BR)], W / 2, 830, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s14"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 160, passo=0.12)
    E.frase(c, t, a4, [("1)", "g", 56, COR)] + ps("2 arremessadores,", "i", 54) + [("mesma média", "g", 56)], XE, 270, passo=0.08)
    E.frase(c, t, b4, ps("variância: 1º", "i", 54) + [("0,64", "g", 58, COR)] + ps("· 2º", "i", 54) + [("0,25", "g", 58, COR)], XE + 60, 360, passo=0.08)
    E.frase(c, t, c4, ps("qual é mais regular?", "i", 54, TINTA2), XE + 60, 440, passo=0.08)
    E.frase(c, t, a5, [("2)", "g", 56, COR)] + ps("ciclista 1: média", "i", 54) + [("40 min,", "g", 56, COR)] + ps("DP", "i", 54) + [("2 min", "g", 56, COR)],
            XE, 580, passo=0.08)
    E.frase(c, t, b5, ps("ciclista 2: média", "i", 54) + [("80 min,", "g", 56, COR)] + ps("DP", "i", 54) + [("2,4 min", "g", 56, COR)], XE + 60, 670, passo=0.08)
    E.frase(c, t, c5, ps("qual é mais regular?", "i", 54, TINTA2), XE + 60, 750, passo=0.08)
    E.relogio(c, t, C["s16.a"], cx=1560, cy=480, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    X = 1440

    def um():
        E.frase(c, t, C["s17"] + 0.2, [("1)", "g", 64, COR)] + ps("médias iguais: compare as variâncias", "i", 60), XE, 200, passo=0.08)
        fcen(c, t, C["s17"] + 1.0, "0,64      0,25", 560, 420, 110)
        E.foco(c, t, a7, 0.5, lambda a: E.caixa_pontilhada(c, 595, 310, 290, 150, a, CERTO))
        E.frase(c, t, a7 + 0.3, ps("a menor", "i", 50, CERTO), 740, 520, "center")
        bola_txt(c, t, b7, "2º", X, 420, 120, 90)
        E.frase(c, t, b7 + 0.4, ps("arremessador", "i", 50) + [("mais regular", "g", 54, COR)], X, 610, "center", 0.08)
        E.frase(c, t, c7, ps("conferindo:", "i", 52, TINTA2), W / 2, 780, "center")
        fcen(c, t, c7 + 0.4, "r{0,64} = 0,8      r{0,25} = 0,5", W / 2, 900, 74)
    fase(c, t, C["s17"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, [("2)", "g", 64, COR)] + ps("médias diferentes →", "i", 60) + [("coeficiente de variação", "g", 64, COR)],
            XE, 200, passo=0.08)
    fcen(c, t, b8, "2 ÷ 40 = 0,05 = 5%", 560, 400, 72)
    fcen(c, t, c8, "2,4 ÷ 80 = 0,03 = 3%", 560, 560, 72, COR)
    bola_txt(c, t, d8, "2º", X, 440, 120, 90)
    E.frase(c, t, d8 + 0.4, ps("ciclista", "i", 50) + [("mais regular", "g", 54, COR)], X, 630, "center", 0.08)
    E.frase(c, t, d8 + 1.2, ps("mesmo com desvio padrão maior", "i", 50, TINTA2), W / 2, 820, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", ps("médias iguais:", "i", 60) + [("menor desvio padrão", "g", 66, COR)] + ps("= mais regular", "i", 60)),
                 ("s19.b", ps("médias diferentes:", "i", 60) + [("desvio padrão ÷ média", "g", 66, COR)] + ps("e compare", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0, f0 = (C[f"s20.{k}"] for k in "abcdef")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("praticar", "g", 100, COR)] + ps("tudo do módulo", "i", 80), XE, 410)
    for i, (ti, s) in enumerate(((b0, "calcular cada medida"), (c0, "escolher a mais adequada"), (d0, "comparar grupos pela regularidade"))):
        E.frase(c, t, ti, [(f"{i + 1}.", "g", 52, COR)] + ps(s, "i", 52), XE, 540 + i * 90, passo=0.08)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, e0 + 0.2, 0.4))
    E.frase(c, t, f0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ler=b_ler, saltos=b_saltos, cv=b_cv, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
