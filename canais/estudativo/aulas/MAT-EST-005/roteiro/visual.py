"""Visual — Estudativo · MAT-EST-005: histograma.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): tabela (quadro()) que entra célula a célula no
marcador em que a fala diz o número, com a bolinha da cor da classe (CLS = E._paleta(5), as cores das classes de MAT-EST-002);
classes desenhadas com classe(20, 30) (MAT-EST-002); lista de idades em fichas (fichas()) que acendem na cor da classe;
leitura do valor com guia tracejada até o eixo do lado (guia(), MAT-EST-003); conta da vez à direita; resposta na esfera;
atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- HISTOGRAMA = E.histograma na primeira entrada; depois, eixos_h() + hist_cols() (as colunas com um instante por coluna e a
  cor de cada coluna calculada no tempo: a faixa da vez na cor da matéria, o resto em cinza claro). Hist guarda a geometria.
- FAIXA = chave embaixo do eixo de baixo, do limite inicial ao final, com a faixa escrita (faixa()).
- No palco escuro, o histograma é desenhado à mão em branco (hist_palco()), porque o E.histograma usa tinta escura.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-005_histograma.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tabela", "faixa", "diferenca", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
APAGADO = E.mix(CINZA, PAPEL, 0.55)
CLS = E._paleta(5)     # as classes 10 ⊢ 20 ... 50 ⊢ 60 (cores de MAT-EST-002)
CATS = E._paleta(4)    # ônibus, carro, bicicleta, a pé (cores de MAT-EST-002 e 003)
IDADES = [18, 23, 25, 31, 34, 19, 42, 27, 36, 30, 22, 45, 29, 38, 51, 26, 33, 40, 24, 37]
LIM = [10, 20, 30, 40, 50, 60]
FREQ = [2, 7, 7, 3, 1]
QLIM = [0, 15, 30, 45, 60]
QFREQ = [6, 14, 12, 8]
assert [sum(1 for v in IDADES if LIM[k] <= v < LIM[k + 1]) for k in range(5)] == FREQ and sum(FREQ) == 20 and IDADES.count(25) == 1
assert 7 + 7 == 14 and 2 + 7 == 9 and 20 - 9 == 11 == 7 + 3 + 1
assert sum(QFREQ) == 40 and 14 + 12 == 26 and 12 + 8 == 20 == 40 - 6 - 14 and 20 * 100 // 40 == 50


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ² ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def _cel(c, s, cx, y, size, estilo, cor, a):
    if callable(s):
        s(c, cx, y, size, cor, a)
    else:
        centro(c, s, cx, y, size, estilo, cor, a)


def classe(ini, fim):
    """rótulo de classe "20 ⊢ 30" (MAT-EST-002), desenhado: a fonte não tem o sinal"""
    def fn(c, cx, y, size, cor, a):
        s1, s2 = str(ini), str(fim)
        w1, w2 = E.larg(s1, "g", size), E.larg(s2, "g", size)
        gap = size * 1.05
        x0 = cx - (w1 + gap + w2) / 2
        E.escreve(c, s1, x0, y, size, "g", cor, a)
        sx, sy = x0 + w1 + size * 0.28, y - size * 0.36
        M.line(c, sx, sy - size * 0.32, sx, sy + size * 0.32, cor, a, max(3, size * 0.09))
        M.line(c, sx, sy, sx + gap - size * 0.56, sy, cor, a, max(3, size * 0.09))
        E.escreve(c, s2, x0 + w1 + gap, y, size, "g", cor, a)
    return fn


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados (MAT-EST-001/002): colunas = [(título, largura, t0)]; linhas = [[(texto ou classe(), t0[, cor]), ...]]"""
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
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: _cel(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
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
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else TINTA, a))
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
    """lista de dados em grade de fichas. itens = [(texto[, cor acesa, t_acende])]. Devolve os centros"""
    cx, cy, centros = x, y, []
    h = size * 1.55
    for i, it in enumerate(itens):
        s = it[0]
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px, py = cx + wi / 2, cy
        cor = it[1] if len(it) > 1 and t >= it[2] else None
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, py=py, cor=cor: ficha(c, s, px, py, size, a, cor), sobe=8)
        centros.append((px, py))
        cx += wi + gap
    return centros


def classe_de(v):
    return v // 10 - 1


# ================= peças do histograma (copiar nas próximas aulas) =================
class Hist:
    """geometria de um histograma: x, y, w, h, os limites das classes e vmax; vx(v) = x do limite v, vy(f) = altura"""
    def __init__(self, x, y, w, h, lims, vmax, marcas):
        self.x, self.y, self.w, self.h, self.lims, self.vmax, self.marcas = x, y, w, h, lims, vmax, marcas

    def vx(self, v):
        return self.x + (v - self.lims[0]) / (self.lims[-1] - self.lims[0]) * self.w

    def vy(self, f):
        return self.y + self.h - f / self.vmax * self.h

    def meio(self, i):
        return (self.vx(self.lims[i]) + self.vx(self.lims[i + 1])) / 2


def eixos_h(c, t, t0, G, size=40, unidade=None, eixo=None):
    """eixos do histograma (grade, valores do lado e os limites das classes embaixo)"""
    E._eixo_dados(c, t, t0, G.x, G.y, G.w, G.h, 0, G.vmax, G.marcas, E._num, size, TINTA)
    for i, v in enumerate(G.lims):
        E.foco(c, t, t0 + 0.2 + i * 0.04, 0.4, lambda a, v=v: (M.line(c, G.vx(v), G.y + G.h, G.vx(v), G.y + G.h + 14, TINTA, a, 4),
                                                               centro(c, E._num(v), G.vx(v), G.y + G.h + 24 + size, size, "b", TINTA, a)), sobe=6)
    if unidade:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, unidade, G.x - 10, G.y - 46, 38, "i", TINTA2, a))
    if eixo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, eixo, G.x + G.w - E.larg(eixo, "i", 36), G.y + G.h + 24 + size + 46, 36, "i", TINTA2, a))


def hist_cols(c, t, ts, G, freqs, cores=None, valores=True, size=40, d=0.5, cor_val=None):
    """as colunas, cada uma no seu instante ts[i], coladas; cores[i] = cor da coluna (None = cor da matéria)"""
    for i, f in enumerate(freqs):
        q = E.ease_out(prog(t, ts[i], d))
        if q <= 0:
            continue
        x0, x1 = G.vx(G.lims[i]), G.vx(G.lims[i + 1])
        cr = (cores[i] if cores else None) or E.COR
        topo = lerp(G.y + G.h, G.vy(f), q)
        c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint(cr))
        c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint(PAPEL, 1.0, stroke=4))
        if valores:
            cv = cor_val[i] if cor_val else (COR if cr == E.COR else TINTA2)
            E.foco(c, t, ts[i] + d * 0.8, 0.4, lambda a, f=f, x0=x0, x1=x1, cv=cv: centro(c, E._num(f), (x0 + x1) / 2, G.vy(f) - 22, size * 1.05, "g", cv, a), sobe=6)


def faixa(c, t, t0, G, v0, v1, rotulo, cor=None, dy=110, size=44):
    """a faixa do eixo de baixo: chave de v0 a v1 abaixo dos números, com o texto embaixo"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    y = G.y + G.h + dy
    E.chave(c, G.vx(v0), G.vx(v1), y, cor or E.COR, p, 22, 6)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rotulo, (G.vx(v0) + G.vx(v1)) / 2, y + 30 + size, size, "g", cor or COR, a))


def guia(c, t, t0, G, x, f, cor=None, size=44):
    """a leitura da altura: tracejado do topo até o eixo do lado, com o valor aceso no eixo (MAT-EST-003)"""
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0:
        return
    k = cor or E.COR
    y = G.vy(f)
    M.line(c, x, y, lerp(x, G.x, p), y, k, 1, 5, dash=E.TRACO)
    c.drawCircle(x, y, 9, M.paint(k))
    s = E._num(f)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.pilula(c, s, G.x - 20 - (E.larg(s, "g", size) + size * 1.1) / 2, y, size, "g", fundo=k, a=a))


def hist_palco(c, t, t0, G, freqs, cores, size=40):
    """histograma à mão para o palco escuro: colunas nas cores dadas, limites em claro"""
    M.line(c, G.x - 10, G.y + G.h, G.x + G.w, G.y + G.h, CLARO, ep(t, t0, 0.5), 4)
    for i, v in enumerate(G.lims):
        E.foco(c, t, t0 + 0.05 * i, 0.4, lambda a, v=v: centro(c, E._num(v), G.vx(v), G.y + G.h + 24 + size, size, "b", CLARO, a))
    for i, f in enumerate(freqs):
        q = E.ease_out(prog(t, t0 + 0.2 + 0.1 * i, 0.5))
        if q > 0:
            x0, x1 = G.vx(G.lims[i]), G.vx(G.lims[i + 1])
            topo = lerp(G.y + G.h, G.vy(f), q)
            c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint(cores[i]))
            c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint("#07070F", 1, stroke=4))
            E.foco(c, t, t0 + 0.6 + 0.1 * i, 0.4, lambda a, f=f, x0=x0, x1=x1: centro(c, str(f), (x0 + x1) / 2, G.vy(f) - 20, size * 1.05, "g", BR, a))


def mistura(t, ti, de, para, d=0.4):
    """cor que passa de 'de' para 'para' a partir de ti"""
    return E.mix(de, para, ep(t, ti, d))


# ---------------- os histogramas desta aula ----------------
GH = Hist(230, 250, 1000, 580, LIM, 8, [0, 2, 4, 6, 8])          # idades, grande à esquerda
GQ = Hist(1060, 330, 760, 480, QLIM, 16, [0, 4, 8, 12, 16])      # minutos da questão


def idades(c, t, t0, G=GH, cores=None, ts=None, size=40, valores=True):
    if ts is None:   # já desenhado
        eixos_h(c, t, -9, G, size, "pessoas", "idade")
        hist_cols(c, t, [-9] * 5, G, FREQ, cores, valores, size)
    else:
        eixos_h(c, t, t0, G, size, "pessoas", "idade")
        hist_cols(c, t, ts, G, FREQ, cores, valores, size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.histograma(c, t, a1, LIM, FREQ, GH.x, GH.y, GH.w, GH.h, vmax=8, marcas=GH.marcas, valores=False)
        for k, v in enumerate((20, 30, 40, 50)):
            p = ep(t, b1 + 0.2 * k, 0.4)
            if p > 0:
                c.drawCircle(GH.vx(v), GH.vy(min(FREQ[k], FREQ[k + 1])) - 4, 14, M.paint(TINTA, p))
        p = ep(t, c1, 0.5)
        if p > 0:
            E.caixa_pontilhada(c, GH.x - 40, GH.y + GH.h + 14, GH.w + 80, 90, p, ERRADO, prog_=p)
        X = 1570
        E.frase(c, t, a1, ps("parece um gráfico", "i", 56), X, 260, "center", 0.1)
        E.frase(c, t, a1 + 0.9, ps("de", "i", 56) + [("barras?", "g", 62)], X, 340, "center", 0.1)
        E.frase(c, t, b1, [("colunas coladas", "g", 58, COR)], X, 480, "center", 0.1)
        E.frase(c, t, c1, ps("embaixo:", "i", 52) + [("só números", "g", 56, ERRADO)], X, 590, "center", 0.1)
        bola_txt(c, t, d1, "histograma", X, 790, 150, 46)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("ler um", "i", 88) + [("histograma", "g", 100, COR)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 3.0, ps("quantos numa", "i", 88) + [("faixa", "g", 100, COR)], XE, 580, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a tabela com classes"), ("s03.c", "ler um gráfico de barras:"))
    for i, (k, l1) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 90, "left", 0.1)
    E.foco(c, t, C["s03.b"] + 0.6, 0.5, lambda a: classe(10, 20)(c, x + w - 200, 240 + 170, 64, COR, a))
    E.frase(c, t, C["s03.c"] + 0.8, [("título, eixos, topo", "g", 52, COR)], x + w - 60, 520 + 170, "right", 0.1)
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- da tabela ao histograma ----------------
CX0, CY0 = 150, 330


def tabela_classes(c, t, tabs, t0, size=50, x=CX0, y=CY0):
    cols = [("classe (anos)", 340, t0), ("pessoas", 220, t0 + 0.2)]
    linhas = [[(classe(LIM[k], LIM[k + 1]), tabs[k]), (str(FREQ[k]), tabs[k] + 0.3, COR)] for k in range(5)]
    return quadro(c, t, x, y, cols, linhas, [("total", tabs[4] + 1.0), ("20", tabs[4] + 1.0)], size=size, cores=CLS)


def b_tabela(c, t, C, b):
    tabs = [C[f"s04.{k}"] for k in "abcde"]
    E.frase(c, t, C["s04"] + 0.2, ps("as idades das", "i", 60) + [("20 pessoas", "g", 64, COR)], 150, 200, "left", 0.1)
    tabela_classes(c, t, tabs, C["s04"] + 1.6)
    itens = [(str(v), CLS[classe_de(v)], tabs[classe_de(v)]) for v in IDADES]
    fichas(c, t, C["s04"] + 0.6, itens, 960, 360, 860, size=40, gap=18, passo=0.04)


# ---------------- o histograma ----------------
def b_histograma(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    E.histograma(c, t, a5 - 0.3, LIM, FREQ, GH.x, GH.y, GH.w, GH.h, vmax=8, marcas=GH.marcas, passo=0.25)
    E.foco(c, t, a5, 0.4, lambda a: (E.escreve(c, "pessoas", GH.x - 10, GH.y - 46, 38, "i", TINTA2, a),
                                     E.escreve(c, "idade", GH.x + GH.w - E.larg("idade", "i", 36), GH.y + GH.h + 110, 36, "i", TINTA2, a)))
    X = 1590

    def um():
        E.frase(c, t, C["s05"] + 0.1, ps("desenha a tabela", "i", 58), X, 260, "center", 0.1)
        E.frase(c, t, a5, ps("cada classe =", "i", 56) + [("1 coluna", "g", 60, COR)], X, 380, "center", 0.1)
        faixa(c, t, b5, GH, 20, 30, "10 anos")
        E.frase(c, t, b5, [("largura", "g", 60, COR)] + ps("= a faixa", "i", 56), X, 520, "center", 0.1)
        guia(c, t, c5, GH, GH.meio(1), 7)
        E.frase(c, t, c5, [("altura", "g", 60, COR)] + ps("= a frequência", "i", 56), X, 660, "center", 0.1)
        E.frase(c, t, c5 + 1.2, ps("quantas pessoas na faixa", "i", 46, TINTA2), X, 740, "center", 0.08)
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t < C["s06"] - 0.1:
        return
    p = ep(t, a6, 0.5)
    if p > 0:
        E.caixa_pontilhada(c, GH.x - 40, GH.y + GH.h + 14, GH.w + 80, 90, p, None, prog_=p)
    for k, v in enumerate((10, 20, 30)):
        E.foco(c, t, a6 + 0.8 + 0.6 * k, 0.3, lambda a, v=v: c.drawCircle(GH.vx(v), GH.y + GH.h, 12, M.paint(E.COR, a)))
    q = ep(t, b6, 0.6)
    if q > 0:
        M.line(c, GH.vx(30), GH.y + GH.h, GH.vx(30), lerp(GH.y + GH.h, GH.vy(7) - 30, q), TINTA, 1, 7)
    E.frase(c, t, a6, ps("eixo de baixo =", "i", 56), X, 260, "center", 0.1)
    E.frase(c, t, a6 + 0.6, [("reta numérica", "g", 62, COR)], X, 340, "center", 0.1)
    E.frase(c, t, a6 + 1.2, ps("as bordas das classes", "i", 48, TINTA2), X, 420, "center", 0.1)
    E.frase(c, t, b6, ps("uma termina,", "i", 56), X, 540, "center", 0.1)
    E.frase(c, t, b6 + 0.6, [("a próxima começa", "g", 60, COR)], X, 620, "center", 0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "colunas coladas", X, 790, 60, "g", a=a, cor=E.SOBRE))


# ---------------- ler uma faixa ----------------
def b_faixa(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8 = C["s08.a"], C["s08.b"]
    if t < d7:
        cores = [mistura(t, b7, E.COR, APAGADO) if i not in (1, 2) else None for i in range(5)]
    elif t < C["s08"]:
        cores = [None if i in (0, 1) else APAGADO for i in range(5)]
    else:
        cores = [None if i == 2 else APAGADO for i in range(5)]
    idades(c, t, 0, cores=cores)
    X = 1590
    E.saida(c, t, d7, lambda: faixa(c, t, a7, GH, 20, 40, "de 20 até menos de 40"))
    E.saida(c, t, C["s08"], lambda: faixa(c, t, d7, GH, 10, 30, "menos de 30"))

    def um():
        E.frase(c, t, a7, ps("de", "i", 56) + [("20", "g", 60, COR)] + ps("até menos de", "i", 56) + [("40?", "g", 60, COR)], X, 260, "center", 0.1)
        E.frase(c, t, b7, [("2 colunas", "g", 58)], X, 370, "center", 0.1)
        fcen(c, t, c7, "7 + 7", X - 110, 500, 76)
        bola_txt(c, t, c7 + 0.6, "14", X + 150, 480, 80, 70)
        E.frase(c, t, d7 - 1.6, ps("menos de", "i", 56) + [("30?", "g", 60, COR)], X, 680, "center", 0.1)
        fcen(c, t, d7, "2 + 7", X - 110, 810, 76)
        bola_txt(c, t, d7 + 0.6, "9", X + 150, 790, 80, 70)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, C["s08"] + 0.1, ps("na borda: a regra da tabela", "i", 52), X, 260, "center", 0.1)
    E.foco(c, t, a8, 0.5, lambda a: classe(30, 40)(c, X, 430, 110, COR, a))
    E.foco(c, t, a8 + 0.8, 0.4, lambda a: centro(c, "entra", X - 120, 520, 46, "g", CERTO, a))
    E.foco(c, t, a8 + 1.6, 0.4, lambda a: centro(c, "não entra", X + 130, 520, 46, "g", ERRADO, a))
    E.foco(c, t, b8, 0.5, lambda a: ficha(c, "30 anos", X, 700, 56, a, E.COR))
    E.frase(c, t, b8 + 0.6, ps("vai para a coluna de", "i", 50) + [("30 a 40", "g", 54, COR)], X, 830, "center", 0.1)
    p = ep(t, b8 + 0.4, 0.5)
    if p > 0:
        c.drawCircle(GH.vx(30), GH.y + GH.h, 16, M.paint(E.COR, p))
        M.arrow(c, GH.vx(30) + 10, GH.y + GH.h - 30, GH.meio(2), GH.vy(3), BR, p, 6, 20, ease_io(prog(t, b8 + 0.4, 0.6)))


# ---------------- barras x histograma ----------------
GB = (190, 400, 680, 400)       # barras do transporte (x, y, w, h)
GD = Hist(1100, 400, 680, 400, LIM, 8, [0, 4, 8])


def b_diferenca(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    x, y, w, h = GB
    TR = [("ônibus", 8, CATS[0]), ("carro", 5, CATS[1]), ("bicicleta", 4, CATS[2]), ("a pé", 3, CATS[3])]
    E.foco(c, t, C["s09"] + 0.2, 0.4, lambda a: centro(c, "barras", x + w / 2, 220, 70, "g", TINTA, a))
    E.colunas(c, t, a9, TR, x, y, w, h, vmax=10, size=36, passo=0.15)
    E.frase(c, t, a9 + 0.8, ps("cada barra =", "i", 48) + [("categoria", "g", 52, COR)], x + w / 2, 940, "center", 0.1)
    E.frase(c, t, a9 + 2.4, ps("qualitativa", "i", 46, TINTA2), x + w / 2, 1010, "center", 0.1)
    if t >= b9:   # trocar a ordem: seta dupla entre ônibus e carro
        sl = w / 4
        x1, x2 = x + sl * 0.5, x + sl * 1.5
        p = ep(t, b9 + 0.6, 0.5)
        pa = skia.Path()
        pa.moveTo(x1, y - 10); pa.quadTo((x1 + x2) / 2, y - 120, x2, y - 10)
        if p > 0:
            c.drawPath(pa, M.paint(TINTA, p, stroke=5))
            for xx, sx in ((x1, 1), (x2, -1)):
                M.line(c, xx, y - 10, xx + sx * 6, y - 40, TINTA, p, 5)
                M.line(c, xx, y - 10, xx + sx * 28, y - 22, TINTA, p, 5)
        E.foco(c, t, b9, 0.4, lambda a: E.pilula(c, "separadas: dá para trocar", x + w / 2, 275, 40, "g", fundo=TINTA, a=a))
    if t < C["s10"] - 0.1:
        return
    G = GD
    E.foco(c, t, C["s10"], 0.4, lambda a: centro(c, "histograma", G.x + G.w / 2, 220, 70, "g", COR, a))
    eixos_h(c, t, C["s10"], G, 36)
    hist_cols(c, t, [C["s10"] + 0.2 + 0.12 * i for i in range(5)], G, FREQ, valores=False, size=36)
    E.frase(c, t, a0, [("quantitativa", "g", 52, COR)] + ps("em classes", "i", 48), G.x + G.w / 2, 940, "center", 0.1)
    p = ep(t, b0, 0.8)
    if p > 0:
        M.arrow(c, G.x, G.y + G.h + 82, lerp(G.x, G.x + G.w, p), G.y + G.h + 82, E.COR, 1, 5, 18, p)
    E.frase(c, t, b0 + 0.3, ps("a ordem da reta: não muda", "i", 46, TINTA2), G.x + G.w / 2, 1010, "center", 0.08)
    E.foco(c, t, c0, 0.4, lambda a: E.pilula(c, "sem espaço: faixas se encostam", G.x + G.w / 2, 275, 40, "g", a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    cores = [mistura(t, c1, E.COR, APAGADO) if i != 1 else None for i in range(5)]
    idades(c, t, 0, cores=cores)
    p = ep(t, b1, 0.4)
    if p > 0:   # o alfinete no 25
        xx = GH.vx(25)
        M.line(c, xx, GH.y + GH.h + 8, xx, GH.y + GH.h + 60, ERRADO, p, 6)
        E.foco(c, t, b1, 0.4, lambda a: E.pilula(c, "25", xx, GH.y + GH.h + 110, 40, "g", fundo=ERRADO, a=a))
    if t < C["s12"]:
        contorno_t = ep(t, c1, 0.4)
        if contorno_t > 0:
            c.drawRect(skia.Rect.MakeLTRB(GH.vx(20), GH.vy(7), GH.vx(30), GH.y + GH.h), M.paint(ERRADO, contorno_t, stroke=8))
    X = 1590

    def um():
        E.frase(c, t, C["s11"] + 0.2, [("erro comum:", "g", 62, ERRADO)], X, 260, "center", 0.1)
        E.frase(c, t, a1, ps("a coluna como", "i", 54) + [("uma idade só", "g", 58)], X, 350, "center", 0.1)
        E.frase(c, t, b1, ps("quantos têm", "i", 56) + [("25 anos?", "g", 60, COR)], X, 520, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.selo(c, X - 120, 690, 50, False, a))
        E.foco(c, t, c1 + 0.2, 0.5, lambda a: E.escreve(c, "7?", X - 40, 730, 110, "g", ERRADO, a))
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    E.saida(c, t, c2, lambda: faixa(c, t, a2, GH, 20, 30, "de 20 até 29"))
    X = 1560
    E.frase(c, t, a2, [("7", "g", 64, COR)] + ps("= a faixa inteira", "i", 56), X, 240, "center", 0.1)
    vinte = sorted(v for v in IDADES if 20 <= v < 30)
    assert vinte == [22, 23, 24, 25, 26, 27, 29]
    for i, v in enumerate(vinte):
        cx = X - 276 + 92 * i
        E.foco(c, t, b2 - 0.8 + 0.08 * i, 0.4, lambda a, v=v, cx=cx: ficha(c, str(v), cx, 380, 36, a, E.COR if (v == 25 and t >= b2) else None,
                                                                         TINTA if v == 25 and t >= b2 else None), sobe=8)
    E.frase(c, t, b2 + 0.3, ps("só", "i", 54) + [("1 pessoa", "g", 58, COR)] + ps("tinha 25", "i", 54), X, 500, "center", 0.1)
    E.frase(c, t, c2, ps("mostra", "i", 56) + [("faixas,", "g", 60, COR)], X, 660, "center", 0.1)
    E.frase(c, t, c2 + 0.8, ps("não idades soltas", "i", 56), X, 740, "center", 0.1)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "só com ele: sem resposta", X + 30, 990, 46, "g", fundo=TINTA, a=a))


# ---------------- atalho (palco escuro) ----------------
GP = Hist(180, 380, 900, 440, LIM, 8, [0, 8])


def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4 = C["s14.a"], C["s14.b"]
    if t < C["s14"]:
        cores = [E.mix(E.mix(E.COR, BR, 0.25), BR, ep(t, b3, 0.4) * 0.6) if i < 2 else E.mix(E.mix(E.COR, BR, 0.25), "#3A3A55", ep(t, b3, 0.4)) for i in range(5)]
    else:
        cores = [E.mix(E.COR, BR, 0.25)] * 5
    hist_palco(c, t, C["s13"], GP, FREQ, cores)
    E.foco(c, t, C["s13"] + 0.2, 0.4, lambda a: E.escreve(c, "total: 20 pessoas", GP.x, GP.y - 160, 46, "i", CLARO, a))
    X = 1480

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 64, CLARO), X, 200, "center", 0.1)
        E.frase(c, t, a3, ps("conte o", "i", 60, CLARO) + [("lado menor", "g", 64, BR)], X, 300, "center", 0.1)
        E.frase(c, t, a3 + 1.2, ps("e tire do", "i", 60, CLARO) + [("total", "g", 64, BR)], X, 380, "center", 0.1)
        E.frase(c, t, lerp(a3, b3, 0.4), ps("30 anos ou mais?", "i", 56, CLARO), X, 520, "center", 0.1)
        fcen(c, t, b3, "2 + 7 = 9", X, 660, 80, BR)
        fcen(c, t, c3, "20 − 9 = 11", X - 120, 830, 80, BR)
        bola_txt(c, t, c3 + 0.6, "11", X + 260, 810, 90, 76)
        p = ep(t, c3 + 0.4, 0.5)
        if p > 0:
            E.chave(c, GP.vx(30), GP.vx(60), GP.y - 30, BR, p, -22, 6)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    p = ep(t, a4, 0.6)
    if p > 0:
        E.chave(c, GP.vx(10), GP.vx(60), GP.y - 30, BR, p, -22, 6)
    E.frase(c, t, a4, ps("todas as colunas", "i", 60, CLARO), X, 300, "center", 0.1)
    E.frase(c, t, a4 + 0.8, ps("somam o", "i", 60, CLARO) + [("total", "g", 64, BR)], X, 380, "center", 0.1)
    E.frase(c, t, a4 + 2.6, ps("o que não está de um lado", "i", 50, CLARO), X, 500, "center", 0.08)
    E.frase(c, t, a4 + 3.6, ps("está do outro", "i", 50, CLARO), X, 570, "center", 0.08)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, X - 260, 730, 44, False, a))
    E.frase(c, t, b4 + 0.1, ps("pediu o lado menor?", "i", 54, CLARO), X - 190, 752, "left", 0.1)
    E.foco(c, t, b4 + 1.4, 0.5, lambda a: E.pilula(c, "some direto", X, 880, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def minutos(c, t, ts, G=GQ, cores=None, size=36, t0=None):
    eixos_h(c, t, ts[0] - 0.6 if t0 is None else t0, G, size, "funcionários", "minutos")
    hist_cols(c, t, ts, G, QFREQ, cores, True, size)


def b_questao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, [("40", "g", 64, COR)] + ps("funcionários:", "i", 58), XE, 300, passo=0.1)
    E.frase(c, t, a5 + 1.0, ps("minutos até o trabalho", "i", 58), XE, 380, passo=0.1)
    E.frase(c, t, a6, [("1)", "g", 56, COR)] + ps("de 15 até menos de 45?", "i", 54), XE, 560, passo=0.1)
    E.frase(c, t, b6, [("2)", "g", 56, COR)] + ps("30 minutos ou mais:", "i", 54) + [("quantos %?", "g", 56)], XE, 680, passo=0.1)
    E.frase(c, t, c6, [("3)", "g", 56, COR)] + ps("exatamente 20 minutos?", "i", 54), XE, 800, passo=0.1)
    E.saida(c, t, C["s17.a"] - 0.1, lambda: minutos(c, t, [b5, c5, d5, e5], t0=a5))
    E.relogio(c, t, C["s17.a"], 1440, 540, 200)


# ---------------- resposta ----------------
GR = Hist(230, 300, 900, 520, QLIM, 16, [0, 4, 8, 12, 16])


def b_resposta(c, t, C, b):
    a8, b8 = C["s18.a"], C["s18.b"]
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    a0, b0 = C["s20.a"], C["s20.b"]
    if t < C["s19"]:
        cores = [mistura(t, a8, E.COR, APAGADO) if i in (0, 3) else None for i in range(4)]
    elif t < b9:
        cores = [None if i >= 2 else APAGADO for i in range(4)]
    elif t < C["s20"]:
        cores = [TINTA2 if i < 2 else None for i in range(4)]
    else:
        cores = [None if i == 1 else APAGADO for i in range(4)]
    minutos(c, t, [-9] * 4, GR, cores, 40)
    X = 1560

    def um():
        E.frase(c, t, C["s18"] + 0.1, [("1)", "g", 60, COR)] + ps("de 15 até menos de 45", "i", 54), X, 260, "center", 0.1)
        faixa(c, t, a8, GR, 15, 45, "2 colunas")
        fcen(c, t, b8, "14 + 12", X - 120, 520, 80)
        bola_txt(c, t, b8 + 0.6, "26", X + 170, 500, 90, 76)
        E.frase(c, t, b8 + 1.2, ps("funcionários", "i", 48, TINTA2), X + 170, 650, "center", 0.1)
    fase(c, t, C["s18"], C["s19"] - 0.1, um)

    def dois():
        E.frase(c, t, C["s19"] + 0.1, [("2)", "g", 60, COR)] + ps("30 minutos ou mais", "i", 54), X, 240, "center", 0.1)
        fcen(c, t, a9, "12 + 8 = 20", X, 380, 72)
        E.frase(c, t, b9 - 0.4, ps("pelo atalho:", "i", 50, TINTA2), X, 490, "center", 0.1)
        fcen(c, t, b9, "40 − 6 − 14 = 20", X, 590, 72)
        fcen(c, t, c9, "f{20}{40} = metade", X - 170, 790, 64)
        bola_txt(c, t, c9 + 0.8, "50%", X + 200, 770, 100, 64)
    fase(c, t, C["s19"], C["s20"] - 0.1, dois)
    if t < C["s20"] - 0.1:
        return
    E.frase(c, t, C["s20"] + 0.1, [("3)", "g", 60, COR)] + ps("exatamente 20 minutos?", "i", 54), X, 260, "center", 0.1)
    p = ep(t, a0, 0.4)
    if p > 0:
        xx = GR.vx(20)
        M.line(c, xx, GR.y + GR.h + 8, xx, GR.y + GR.h + 60, ERRADO, p, 6)
        E.pilula(c, "20", xx, GR.y + GR.h + 110, 40, "g", fundo=ERRADO, a=p)
    E.foco(c, t, a0, 0.5, lambda a: E.selo(c, X - 250, 440, 44, False, a))
    E.frase(c, t, a0 + 0.1, [("não dá para saber", "g", 50, ERRADO)], X - 185, 458, "left", 0.1)
    faixa(c, t, b0, GR, 15, 30, "15 a 30", dy=150)
    E.frase(c, t, b0, ps("só diz:", "i", 54) + [("14 na faixa", "g", 58, COR)], X, 640, "center", 0.1)
    E.foco(c, t, b0 + 0.6, 0.4, lambda a: classe(15, 30)(c, X, 760, 80, COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", ps("cada coluna é uma", "i", 64) + [("faixa", "g", 70, COR)]),
                 ("s21.b", [("altura", "g", 70, COR)] + ps("= quantos estão nela", "i", 64)),
                 ("s21.c", [("coladas:", "g", 70, COR)] + ps("as faixas se encostam", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2, e2 = (C[f"s22.{k}"] for k in "abcde")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a2, ps("cruzar", "i", 72) + [("linha e coluna", "g", 84, COR)], XE, 420, passo=0.12)
    E.frase(c, t, b2, ps("a", "i", 72) + [("legenda", "g", 84, COR)] + ps("de um mapa", "i", 72), XE, 560, passo=0.12)
    E.frase(c, t, c2, ps("o dado certo de um", "i", 72) + [("infográfico", "g", 84, COR)], XE, 700, passo=0.12)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 300, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(620, 325, p), ep(t, d2 + 0.2, 0.4))
    E.frase(c, t, e2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tabela=b_tabela, histograma=b_histograma, faixa=b_faixa, diferenca=b_diferenca,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
