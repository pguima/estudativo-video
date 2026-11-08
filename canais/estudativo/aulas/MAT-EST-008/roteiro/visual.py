"""Visual — Estudativo · MAT-EST-008: média aritmética (e o valor que falta). Primeira aula da parte de Médias.
Mesma linguagem da Estatística de MAT-EST-001 a 007: lista de dados em fichas/cartões, gráficos do kit (E.colunas) com a
cor da categoria, conta da vez à direita, resposta na esfera, atalho no palco escuro.
Novo nesta aula (para copiar nas próximas aulas de médias):
- MÉDIA = LINHA TRACEJADA na cor da matéria atravessando as colunas, com a pílula "média 7" na ponta (linha_media()).
- NIVELAR = as colunas sobem e descem até a altura da média (nivela()): o que sobra numa cobre o que falta na outra.
- SOBRAS E FALTAS = pílula "+1" na cor da matéria acima da coluna que passa da média e "−1" em cinza escuro na que fica
  abaixo, com o trecho entre o topo e a linha marcado (difs()). No palco escuro, as colunas são desenhadas à mão (barras()).
- PROVAS = cartões com o nome e a nota (prova()); a nota que falta chega com "?".
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-008_media_aritmetica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "total", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(4)
NOTAS = [6, 8, 5]
CAMINHADA = [5, 8, 7, 9]
VENDAS = [42, 55, 48, 51]
assert sum([6, 7, 8]) == 21 and 21 // 3 == 7 and sum(CAMINHADA) == 29 and 29 / 4 == 7.25
assert 7 * 4 == 28 and sum(NOTAS) == 19 and 28 - 19 == 9 and (19 + 8) / 4 == 6.75 and sum(n - 7 for n in NOTAS) == -2
assert 50 * 5 == 250 and sum(VENDAS) == 196 and 250 - 196 == 54 and sum(v - 50 for v in VENDAS) == -4


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


class Graf:
    """geometria de um E.colunas (MAT-EST-003): px(i) = centro da coluna i, py(v) = altura do valor v"""
    def __init__(self, x, y, w, h, n, vmax, vmin=0):
        self.x, self.y, self.w, self.h, self.n, self.vmax, self.vmin = x, y, w, h, n, vmax, vmin

    def px(self, i):
        return self.x + self.w * (i + 0.5) / self.n

    def py(self, v):
        return self.y + self.h - (v - self.vmin) / (self.vmax - self.vmin) * self.h

    def bw(self):
        return self.w / self.n * 0.62


# ================= peças das médias (copiar nas próximas aulas) =================
def linha_media(c, t, t0, G, v, rotulo=None, cor=None, size=40, x1=None):
    """a média: linha tracejada na altura v, de ponta a ponta do gráfico, com a pílula na direita"""
    p = ease_io(prog(t, t0, 0.7))
    if p <= 0:
        return
    k = cor or E.COR
    y = G.py(v)
    xe = x1 if x1 is not None else G.x + G.w + 20
    M.line(c, G.x - 10, y, lerp(G.x - 10, xe, p), y, k, 1, 6, dash=E.TRACO)
    s = rotulo or f"média {E._num(v)}"
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.pilula(c, s, xe + 20 + (E.larg(s, "g", size) + size * 1.1) / 2, y, size, "g", fundo=k, cor=M.on(k), a=a))


def barras(c, G, vals, cores, a=1.0, rotulos=None, valores=None, tinta=TINTA, size=42):
    """colunas desenhadas à mão (para nivelar e para o palco): vals podem mudar no tempo"""
    if a <= 0:
        return
    M.line(c, G.x - 10, G.y + G.h, G.x + G.w + 10, G.y + G.h, tinta, a, 5)
    for i, v in enumerate(vals):
        cx, bw = G.px(i), G.bw()
        top = G.py(v)
        M.rrect(c, cx - bw / 2, top, bw, G.y + G.h - top, 10, cores[i], a)
        c.drawRect(skia.Rect.MakeXYWH(cx - bw / 2, G.y + G.h - 12, bw, 12), M.paint(cores[i], a))
        if rotulos:
            centro(c, rotulos[i], cx, G.y + G.h + 18 + size, size, "b", tinta, a)
        if valores:
            centro(c, valores[i], cx, top - 22, size * 1.1, "g", tinta, a)


def nivela(G, vals, alvo, q):
    """as alturas no meio do caminho até a média (q = 0..1)"""
    return [lerp(v, alvo, q) for v in vals]


def difs(c, t, ts, G, vals, m, size=40, cor_mais=None, cor_menos=TINTA2, acima=0):
    """sobra (+) ou falta (−) de cada coluna em relação à média m: trecho marcado e pílula"""
    for i, ti in enumerate(ts):
        if ti is None:
            continue
        d = vals[i] - m
        if d == 0:
            continue
        p = ep(t, ti, 0.4)
        if p <= 0:
            continue
        cx, bw = G.px(i), G.bw()
        y0, y1 = G.py(vals[i]), G.py(m)
        k = (cor_mais or E.COR) if d > 0 else cor_menos
        M.line(c, cx + bw / 2 + 18, y0, cx + bw / 2 + 18, y1, k, p, 6)
        s = ("+" if d > 0 else "−") + E._num(abs(d))
        yy = min(y0, y1) - 46 - acima if d > 0 else max(y0, y1) + 46
        E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, k=k: E.pilula(c, s, cx, yy, size, "g", fundo=k, cor=M.on(k), a=a))


def prova(c, cx, cy, w, h, titulo, valor, a=1.0, cor=None, borda=None):
    """o cartão de uma prova: nome em cima, nota grande"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, BR, a)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22)
    c.drawRRect(rr, M.paint(borda or FIO, a, stroke=4 if borda is None else 7))
    centro(c, titulo, cx, cy - h / 2 + 52, 36, "i", TINTA2, a)
    centro(c, valor, cx, cy + h * 0.32, h * 0.45, "g", cor or TINTA, a)


def provas(c, t, ts, vals, x0=XE, cy=420, w=230, h=250, gap=40, cores=None, bordas=None):
    """a fila de cartões; ts[i] = instante de cada um"""
    for i, (ti, v) in enumerate(zip(ts, vals)):
        cx = x0 + w / 2 + i * (w + gap)
        cr = cores[i] if cores else None
        bd = bordas[i] if bordas else None
        E.foco(c, t, ti, 0.45, lambda a, cx=cx, v=v, i=i, cr=cr, bd=bd: prova(c, cx, cy, w, h, f"prova {i + 1}", v, a, cr, bd))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        quarta = "8" if c1 <= t < d1 + 0.8 else ("9" if t >= d1 + 0.8 else "?")
        cor4 = ERRADO if c1 <= t < d1 + 0.8 else (COR if t >= d1 + 0.8 else CINZA)
        provas(c, t, [a1, a1 + 1.4, a1 + 2.6, b1], ["6", "8", "5", quarta], 170, 400, cores=[None, None, None, cor4],
               bordas=[None, None, None, cor4 if t >= c1 else E.COR])
        E.frase(c, t, b1, ps("precisa de", "i", 58) + [("média 7", "g", 66, COR)] + ps("nas 4 provas", "i", 58), W / 2, 680, "center", 0.1)
        E.foco(c, t, c1 + 0.3, 0.5, lambda a: E.pilula(c, "um 8 resolve?", 1530, 400, 50, "g", fundo=ERRADO, a=a))
        E.foco(c, t, d1, 0.5, lambda a: E.selo(c, 1380, 860, 50, False, a))
        E.frase(c, t, d1 + 0.1, [("não resolve", "g", 62, ERRADO)], 1460, 884, "left", 0.1)
        bola_txt(c, t, d1 + 0.8, "9", 600, 880, 100, 110)
        E.frase(c, t, d1 + 1.0, ps("precisa de", "i", 54), 300, 900, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("calcular a", "i", 88) + [("média", "g", 100, COR)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 3.0, ps("e o", "i", 88) + [("valor que falta", "g", 100, COR)], XE, 580, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "montar a equação do problema", "x = o que falta"), ("s03.c", "dividir depois da vírgula", "7 ÷ 4 = 1,75"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 54), x + 44, y + 90, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.8, l2, x + w - 60, y + 175, 60, "g", COR, "right")
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- a ideia: dividir por igual ----------------
GA = Graf(220, 300, 820, 560, 3, 10)


def pessoa(c, cx, cy, s, cor, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.62, s * 0.3, M.paint(cor, a))
    M.rrect(c, cx - s * 0.42, cy - s * 0.25, s * 0.84, s * 0.95, s * 0.36, cor, a)


def amigos(c, t, t0, G, vals, a=1.0, rotulos=True):
    """os três amigos embaixo das colunas de dinheiro"""
    for i in range(3):
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda q, i=i: pessoa(c, G.px(i), G.y + G.h + 110, 90, CATS[i], q * a), sobe=10)
    if rotulos:
        for i, v in enumerate(vals):
            E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda q, i=i, v=v: centro(c, f"R$ {E._num(round(v, 2))}", G.px(i), G.py(v) - 24, 50, "g", TINTA, q * a))


def b_ideia(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    q = ease_io(prog(t, c4, 1.2))
    vals = nivela(GA, [6, 7, 8], 7, q)
    E.foco(c, t, a4, 0.5, lambda a: barras(c, GA, vals, CATS[:3], a), blur=0)
    amigos(c, t, a4, GA, [6, 7, 8] if q < 0.5 else [7, 7, 7])
    if 0 < q < 1:   # o real que passa do terceiro para o primeiro
        x = lerp(GA.px(2), GA.px(0), q)
        y = GA.py(8) - 60 - 120 * math.sin(math.pi * q)
        E.pilula(c, "R$ 1", x, y, 40, "g", fundo=CERTO)
    linha_media(c, t, d4, GA, 7, "média 7")
    X = 1500
    E.frase(c, t, C["s04"] + 0.2, ps("o que é a", "i", 60) + [("média?", "g", 66, COR)], X, 250, "center", 0.1)
    E.frase(c, t, a4, [("3 amigos:", "g", 58)] + ps("R$ 6, R$ 7, R$ 8", "i", 54), X, 380, "center", 0.1)
    fcen(c, t, b4, "6 + 7 + 8 = 21", X, 520, 66)
    E.frase(c, t, b4 + 1.0, ps("juntando tudo", "i", 46, TINTA2), X, 590, "center", 0.1)
    E.frase(c, t, c4, ps("dividindo por igual:", "i", 54) + [("7", "g", 62, COR)], X, 720, "center", 0.1)
    E.foco(c, t, d4 + 0.6, 0.5, lambda a: E.pilula(c, "o que cada um teria", X, 860, 50, "g", a=a, cor=E.SOBRE))


# ---------------- a regra ----------------
GC = Graf(180, 330, 760, 500, 4, 10)


def b_regra(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    s6 = C["s06"]

    def um():
        fcen(c, t, a5, "média = f{soma}{quantidade}", W / 2, 400, 110, COR)
        fcen(c, t, b5, "6 + 7 + 8 = 21", W / 2 - 330, 760, 80)
        E.frase(c, t, b5 + 1.2, ps("a soma", "i", 46, TINTA2), W / 2 - 330, 840, "center", 0.1)
        fcen(c, t, c5, "21 ÷ 3", W / 2 + 280, 760, 80)
        bola_txt(c, t, c5 + 0.6, "7", W / 2 + 560, 740, 90, 100)
        E.frase(c, t, c5 + 0.3, ps("3 valores", "i", 46, TINTA2), W / 2 + 280, 840, "center", 0.1)
    fase(c, t, C["s05"], s6 - 0.1, um)
    if t < s6 - 0.1:
        return
    dados = [(f"{i + 1}º dia", v, CATS[i]) for i, v in enumerate(CAMINHADA)]
    E.colunas(c, t, b6, dados, GC.x, GC.y, GC.w, GC.h, vmax=10, size=40)
    E.foco(c, t, b6 + 0.3, 0.4, lambda a: E.escreve(c, "km por dia", GC.x - 10, GC.y - 50, 40, "i", TINTA2, a))
    linha_media(c, t, d6 + 0.8, GC, 7.25, "média 7,25", x1=GC.x + GC.w + 10)
    X = 1500
    E.frase(c, t, a6, ps("pode dar um número", "i", 54), X, 260, "center", 0.1)
    E.frase(c, t, a6 + 1.0, [("que ninguém tem", "g", 60, COR)], X, 340, "center", 0.1)
    fcen(c, t, c6, "5 + 8 + 7 + 9 = 29", X + 40, 580, 60)
    fcen(c, t, d6, "29 ÷ 4 = 7,25", X + 40, 710, 72, COR)
    E.frase(c, t, d6 + 1.6, ps("km por dia", "i", 46, TINTA2), X + 40, 780, "center", 0.1)
    E.foco(c, t, e6, 0.5, lambda a: E.pilula(c, "nenhum dia teve: é a média", X + 40, 940, 44, "g", a=a, cor=E.SOBRE))


# ---------------- total = média × quantidade ----------------
def b_total(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    s8, s9 = C["s08"], C["s09"]
    G = Graf(200, 330, 700, 460, 3, 10)

    def um():
        E.foco(c, t, a7, 0.5, lambda a: barras(c, G, [7, 7, 7], CATS[:3], a), blur=0)
        amigos(c, t, a7, G, [7, 7, 7])
        X = 1440
        E.frase(c, t, C["s07"] + 0.2, ps("a regra ao", "i", 58) + [("contrário", "g", 62, COR)], X, 250, "center", 0.1)
        fcen(c, t, a7 + 0.8, "7 · 3 = 21", X, 400, 72)
        E.frase(c, t, a7 + 2.0, ps("o dinheiro todo", "i", 46, TINTA2), X, 470, "center", 0.1)
        E.frase(c, t, b7, ps("soma = média × quantidade", "i", 52), X, 600, "center", 0.1)
        p = ep(t, c7, 0.5)
        if p > 0:
            E.caixa_pontilhada(c, X - 430, 690, 860, 170, p, prog_=p)
        fcen(c, t, c7, "total = média · quantidade", X, 800, 58, COR)
    fase(c, t, C["s07"], s8 - 0.1, um)
    if t < s8 - 0.1:
        return
    vals = ["6", "8", "5", "9" if t >= d8 else ("x" if t >= a9 else "?")]
    provas(c, t, [s8] * 4, vals, 170, 330, 220, 230, 30, cores=[None, None, None, COR if t >= d8 or t >= a9 else CINZA],
           bordas=[None, None, None, E.COR])
    E.foco(c, t, s8, 0.4, lambda a: E.pilula(c, "média 7", 1330, 330, 50, "g", a=a, cor=E.SOBRE))
    X = 1440

    def dois():
        fcen(c, t, a8, "total: 7 · 4 = 28", 600, 600, 66)
        fcen(c, t, b8, "já tem: 6 + 8 + 5 = 19", 600, 720, 66)
        fcen(c, t, c8, "falta: 28 − 19 = 9", 600, 840, 66, COR)
        bola_txt(c, t, d8, "9", X, 720, 110, 120)
        E.frase(c, t, d8 + 0.5, ps("na última prova", "i", 48, TINTA2), X, 900, "center", 0.1)
    fase(c, t, s8, s9 - 0.1, dois)
    if t < s9 - 0.1:
        return
    E.frase(c, t, s9 + 0.1, ps("pela equação:", "i", 54, TINTA2), 600, 540, "center", 0.1)
    fcen(c, t, b9, "f{6 + 8 + 5 + x}{4} = 7", 600, 700, 72)
    fcen(c, t, c9, "19 + x = 28", 600, 900, 72)
    E.frase(c, t, c9 - 1.0, ps("× 4 dos dois lados", "i", 44, COR), 1100, 830, "left", 0.1)
    bola_txt(c, t, d9, "x = 9", X + 200, 860, 110, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    provas(c, t, [C["s10"]] * 4, ["6", "8", "5", "8"], 170, 330, 220, 230, 30, cores=[None, None, None, ERRADO],
           bordas=[None, None, None, ERRADO])
    X = 1450
    E.frase(c, t, C["s10"] + 0.2, [("erro comum:", "g", 62, ERRADO)], X, 260, "center", 0.1)
    E.frase(c, t, a0, ps("chutar uma nota", "i", 52), X, 360, "center", 0.1)
    E.frase(c, t, a0 + 1.0, ps("só um pouco acima da média", "i", 52), X, 430, "center", 0.1)
    fcen(c, t, b0, "19 + 8 = 27", 600, 640, 72)
    fcen(c, t, c0, "27 ÷ 4 = 6,75", 600, 790, 72, ERRADO)
    E.foco(c, t, d0, 0.5, lambda a: E.selo(c, X - 170, 640, 50, False, a))
    E.frase(c, t, d0 + 0.1, [("não chega a 7", "g", 60, ERRADO)], X - 100, 662, "left", 0.1)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "a última cobre o que faltou", X, 840, 48, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
GP = Graf(200, 300, 760, 520, 4, 10)


def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1, e1, f1 = (C[f"s11.{k}"] for k in "abcdef")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    s2 = C["s12"]
    claro = E.mix(E.COR, BR, 0.3)
    if t < s2:
        vals = [6, 8, 5, 7 if t >= f1 else 0.0001]
        cores = [claro, claro, claro, E.mix(E.COR, BR, 0.55)]
        rot = ["6", "8", "5", "9" if t >= f1 + 0.4 else "?"]
        E.foco(c, t, C["s11"], 0.5, lambda a: barras(c, GP, vals, cores, a, rot, None, BR, 56), blur=0)
        if t >= f1:   # a última sobe: o 7 mais os 2 que faltam
            hq = ease_io(prog(t, f1, 0.8))
            cx, bw = GP.px(3), GP.bw()
            top = GP.py(lerp(7, 9, hq))
            M.rrect(c, cx - bw / 2, top, bw, GP.py(7) - top + 6, 10, BR, 1)
        linha_media(c, t, a1, GP, 7, "média 7", BR, x1=GP.x + GP.w + 10)
        difs(c, t, [b1, c1, d1], GP, [6, 8, 5], 7, 38, BR, "#8C8CA8")
    else:
        vals = [6, 8]
        G2 = Graf(200, 300, 520, 520, 2, 10)
        E.foco(c, t, c2, 0.5, lambda a: barras(c, G2, vals, [claro, claro], a, ["R$ 6", "R$ 8"], None, BR, 40), blur=0)
        linha_media(c, t, c2 + 0.3, G2, 7, "média 7", BR, x1=G2.x + G2.w + 10)
        difs(c, t, [c2 + 0.8, c2 + 1.6], G2, vals, 7, 38, BR, "#8C8CA8")
    X = 1500

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("o atalho:", "i", 64, CLARO), X, 200, "center", 0.1)
        E.frase(c, t, a1, ps("compare cada valor", "i", 56, CLARO), X, 300, "center", 0.1)
        E.frase(c, t, a1 + 0.8, ps("com a", "i", 56, CLARO) + [("média 7", "g", 62, BR)], X, 380, "center", 0.1)
        fcen(c, t, d1 + 0.6, "−1 + 1 − 2 = −2", X, 560, 70, BR)
        E.frase(c, t, e1, ps("saldo:", "i", 60, CLARO) + [("faltam 2", "g", 66, BR)], X, 690, "center", 0.1)
        fcen(c, t, f1, "7 + 2 = 9", X - 120, 860, 80, BR)
        bola_txt(c, t, f1 + 0.6, "9", X + 220, 840, 90, 100)
    fase(c, t, C["s11"], s2 - 0.1, um)
    if t < s2 - 0.1:
        return
    E.frase(c, t, a2, ps("o que", "i", 56, CLARO) + [("sobra", "g", 60, BR)] + ps("numa", "i", 56, CLARO), X, 240, "center", 0.1)
    E.frase(c, t, a2 + 0.8, ps("cobre o que", "i", 56, CLARO) + [("falta", "g", 60, BR)] + ps("na outra", "i", 56, CLARO), X, 320, "center", 0.1)
    E.foco(c, t, b2, 0.5, lambda q: E.pilula(c, "sobras e faltas se anulam", X, 450, 48, "g", a=q, cor=E.SOBRE))
    E.frase(c, t, c2, ps("os amigos:", "i", 54, CLARO), X, 590, "center", 0.1)
    fcen(c, t, c2 + 1.8, "−1 + 1 = 0", X, 680, 66, BR)
    E.foco(c, t, d2, 0.5, lambda q: E.selo(c, X - 380, 860, 44, False, q))
    E.frase(c, t, d2 + 0.1, ps("muitos valores espalhados:", "i", 48, CLARO), X - 310, 850, "left", 0.08)
    E.frase(c, t, d2 + 1.2, [("some e divida", "g", 54, BR)], X - 310, 920, "left", 0.1)


# ---------------- questão ----------------
GQ = Graf(1060, 330, 780, 480, 5, 60)


def vendas(c, t, t0, G, size=38, valores=True):
    dados = [(f"{i + 1}ª", v, CATS[i]) for i, v in enumerate(VENDAS)] + [("5ª", 0.001, E.mix(FIO, PAPEL, 0.2))]
    E.colunas(c, t, t0, dados, G.x, G.y, G.w, G.h, vmax=60, size=size, valores=False)
    if valores:
        for i, v in enumerate(VENDAS):
            E.foco(c, t, t0 + 0.6 + 0.12 * i, 0.4, lambda a, i=i, v=v: centro(c, str(v), G.px(i), G.py(v) - 22, size * 1.1, "g", TINTA, a))
    E.foco(c, t, t0 + 1.0, 0.4, lambda a: centro(c, "?", G.px(4), G.y + G.h - 30, 90, "g", COR, a))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, "vendas por semana", G.x - 10, G.y - 120, 40, "i", TINTA2, a))


def b_questao(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a3, ps("vendedor: precisa de", "i", 56), XE, 320, passo=0.1)
    E.frase(c, t, a3 + 1.2, [("média 50", "g", 64, COR)] + ps("em 5 semanas", "i", 56), XE, 410, passo=0.1)
    E.frase(c, t, c3, ps("quantas vendas na", "i", 56), XE, 620, passo=0.1)
    E.frase(c, t, c3 + 1.0, [("5ª semana?", "g", 64, COR)], XE, 710, passo=0.1)

    def gr():
        vendas(c, t, b3, GQ)
        linha_media(c, t, b3 + 1.4, GQ, 50, "50", x1=GQ.x + GQ.w - 90, size=36)
    E.saida(c, t, C["s14.a"] - 0.1, gr)
    E.relogio(c, t, C["s14.a"], 1440, 540, 200)


# ---------------- resposta ----------------
GR = Graf(180, 330, 860, 520, 5, 60)


def b_resposta(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    s6 = C["s16"]
    vendas(c, t, -9, GR, 40)
    linha_media(c, t, -9, GR, 50, "50", x1=GR.x + GR.w - 10, size=36)
    q = ease_io(prog(t, c5 + 0.4, 0.8))
    if q > 0:   # a 5ª coluna sobe até 54
        cx, bw = GR.px(4), GR.bw()
        top = GR.py(54 * q)
        M.rrect(c, cx - bw / 2, top, bw, GR.y + GR.h - top, 10, E.COR, 1)
        E.foco(c, t, c5 + 1.0, 0.4, lambda a: centro(c, "54", cx, GR.py(54) - 22, 44, "g", COR, a))
    if t >= s6:
        ts = [a6, lerp(a6, b6, 0.3), lerp(a6, b6, 0.55), lerp(a6, b6, 0.8)]
        difs(c, t, ts, GR, VENDAS, 50, 34, acima=50)
    X = 1480

    def um():
        E.frase(c, t, C["s15"] + 0.1, ps("total = média · quantidade", "i", 50, TINTA2), X, 250, "center", 0.1)
        fcen(c, t, a5, "50 · 5 = 250", X, 380, 70)
        fcen(c, t, b5, "42 + 55 + 48 + 51 = 196", X, 530, 56)
        fcen(c, t, c5, "250 − 196 = 54", X, 680, 70, COR)
        bola_txt(c, t, c5 + 0.8, "54", X, 860, 100, 90)
    fase(c, t, C["s15"], s6 - 0.1, um)
    if t < s6 - 0.1:
        return
    E.frase(c, t, s6 + 0.1, ps("pelo atalho:", "i", 56, TINTA2), X, 260, "center", 0.1)
    fcen(c, t, a6 + 0.3, "−8 + 5 − 2 + 1 = −4", X, 420, 62)
    E.frase(c, t, b6, ps("saldo:", "i", 58) + [("faltam 4", "g", 64, COR)], X, 560, "center", 0.1)
    fcen(c, t, c6, "50 + 4 = 54", X, 700, 76, COR)
    E.foco(c, t, c6 + 1.4, 0.5, lambda a: E.selo(c, X - 120, 860, 46, True, a))
    E.frase(c, t, c6 + 1.5, [("bateu", "g", 62, CERTO)], X - 50, 884, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s17.a", [("média", "g", 70, COR)] + ps("= soma ÷ quantidade", "i", 64)),
                 ("s17.b", [("total", "g", 70, COR)] + ps("= média × quantidade", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
        E.frase(c, t, C["s17.b"] + 1.8, ps("é ele que acha o valor que falta", "i", 52, TINTA2), 290, 760, "left", 0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a8, ps("a", "i", 84) + [("média ponderada", "g", 104, COR)], XE, 410)
    E.frase(c, t, b8, ps("6 com peso 2, 8 com peso 3", "i", 60) + [("→ 7,2", "g", 66, COR)], XE, 560, passo=0.1)
    E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c8 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(960, 785, p), ep(t, c8 + 0.2, 0.4))
    E.frase(c, t, d8, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, regra=b_regra, total=b_total, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
