"""Visual — Estudativo · MAT-EST-003: gráficos de barras e de linhas.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): cada categoria com a sua cor de E._paleta (aqui o
transporte de MAT-EST-002: ônibus, carro, bicicleta, a pé, nas mesmas cores de lá), tabela que entra coluna a coluna, conta
da vez à direita, resposta na esfera.
Novo nesta aula (para copiar nas próximas):
- BARRAS = E.colunas com a cor da categoria em cada dado e a grade do eixo (eixo_y=True); a LEITURA do valor é uma guia
  tracejada na cor da matéria do topo da barra até o eixo do lado, com o número aceso no eixo (guia()).
- LINHA NO TEMPO = E.serie em tinta escura; cada SUBIDA vira uma pílula "+30" sobre o trecho (variacoes()), a queda em cinza
  "−10"; o trecho da vez (a maior alta) fica grosso na cor da matéria (trecho()). Ponto mais alto marcado com anel (anel()).
- Partes do gráfico (título, eixo de baixo, eixo do lado) apontadas com caixa pontilhada.
- No palco escuro, a linha é desenhada à mão em branco (linha_palco()), porque E.serie usa tinta escura.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-003_graficos_de_barras_e_de_linhas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barras", "linhas", "variacao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(4)    # ônibus, carro, bicicleta, a pé (as cores de MAT-EST-002)
TRANSP = [("ônibus", 8, CATS[0]), ("carro", 5, CATS[1]), ("bicicleta", 4, CATS[2]), ("a pé", 3, CATS[3])]
VENDAS = [("jan", 40), ("fev", 50), ("mar", 80), ("abr", 100), ("mai", 90)]
MUSEU = [("jun", 200), ("jul", 250), ("ago", 450), ("set", 360), ("out", 500)]
assert [VENDAS[i + 1][1] - VENDAS[i][1] for i in range(4)] == [10, 30, 20, -10] and 30 / 50 == 0.6 and 10 / 100 == 0.1
assert [MUSEU[i + 1][1] - MUSEU[i][1] for i in range(4)] == [50, 200, -90, 140] and 200 / 250 == 0.8 and 8 - 5 == 3 and 4 * 2 == 8


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³, − ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→−") else est, size * (0.92 if any(ch in w for ch in "%²³→−") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


# ================= peças dos gráficos (copiar nas próximas aulas) =================
class Graf:
    """a geometria de um E.colunas / E.serie: x, y, w, h e vmin..vmax; px(i) = centro da coluna ou do ponto i, py(v) = altura"""
    def __init__(self, x, y, w, h, n, vmax, vmin=0):
        self.x, self.y, self.w, self.h, self.n, self.vmax, self.vmin = x, y, w, h, n, vmax, vmin

    def px(self, i):
        return self.x + self.w * (i + 0.5) / self.n

    def py(self, v):
        return self.y + self.h - (v - self.vmin) / (self.vmax - self.vmin) * self.h

    def pt(self, i, v):
        return self.px(i), self.py(v)


def guia(c, t, t0, G, i, v, rotulo=None, cor=None, size=46):
    """a leitura: tracejado do topo da barra (ou do ponto) i até o eixo do lado, e o valor aceso no eixo"""
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0:
        return
    k = cor or E.COR
    xs, y = G.px(i), G.py(v)
    M.line(c, xs, y, lerp(xs, G.x, p), y, k, 1, 5, dash=E.TRACO)
    c.drawCircle(xs, y, 9, M.paint(k))
    s = rotulo if rotulo is not None else E._num(v)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.pilula(c, s, G.x - 20 - (E.larg(s, "g", size) + size * 1.1) / 2, y, size, "g", fundo=k, a=a))


def trecho(c, t, t0, G, dados, i, cor=None, largura=13):
    """o trecho do ponto i ao i+1 grosso, na cor da matéria"""
    p = ease_io(prog(t, t0, 0.6))
    if p > 0:
        P, Q = G.pt(i, dados[i][1]), G.pt(i + 1, dados[i + 1][1])
        M.line(c, *P, *Q, cor or E.COR, 1, largura, progress=p)


def variacoes(c, t, ts, G, dados, size=40, dy=-56):
    """a pílula "+30" (subida, cor da matéria) ou "−10" (queda, cinza) sobre cada trecho, no instante ts[i]"""
    for i, ti in enumerate(ts):
        if ti is None:
            continue
        d = dados[i + 1][1] - dados[i][1]
        P, Q = G.pt(i, dados[i][1]), G.pt(i + 1, dados[i + 1][1])
        s = ("+" if d > 0 else "−") + E._num(abs(d))
        mx = (P[0] + Q[0]) / 2
        if d > 0:   # acima e à esquerda do meio do trecho, longe dos valores que ficam sobre os pontos
            mx, my = mx - 50, (P[1] + Q[1]) / 2 + dy - 14
        else:       # abaixo e à esquerda do meio do trecho
            mx, my = mx - 60, (P[1] + Q[1]) / 2 + 74
        E.foco(c, t, ti, 0.4, lambda a, s=s, mx=mx, my=my, d=d: E.pilula(c, s, mx, my, size, "g", fundo=E.COR if d > 0 else TINTA2, a=a))


def anel(c, t, t0, P, r=30, cor=None):
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or ERRADO, 1, stroke=6))


def eixos_linha(c, t, t0, G, dados, marcas, unidade=None, size=40):
    """só os eixos de um gráfico de linha (antes dos pontos entrarem): a grade, os valores e os meses"""
    vy = E._eixo_dados(c, t, t0, G.x, G.y, G.w, G.h, G.vmin, G.vmax, marcas, E._num, size, TINTA)
    for i, (rot, _) in enumerate(dados):
        E.foco(c, t, t0 + 0.2 + 0.05 * i, 0.4, lambda a, i=i, rot=rot: centro(c, rot, G.px(i), G.y + G.h + 18 + size * 1.05, size, "b", TINTA, a))
    if unidade:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, unidade, G.x - 10, G.y - 46, 40, "i", TINTA2, a))
    return vy


def linha_palco(c, t, t0, pts, d=1.2, cor=BR, largura=7):
    """linha de pontos desenhada à mão (para o palco escuro)"""
    n = len(pts)
    q = ease_io(prog(t, t0, d)) * (n - 1)
    for i in range(n - 1):
        f = max(0.0, min(1.0, q - i))
        if f > 0:
            M.line(c, *pts[i], *pts[i + 1], cor, 1, largura, progress=f)
    for i, P in enumerate(pts):
        k = ease_back(prog(t, t0 + d * i / max(1, n - 1) - 0.05, 0.35))
        if k > 0:
            c.drawCircle(P[0], P[1], 12 * k, M.paint(cor))


# ---------------- os gráficos desta aula ----------------
GB = Graf(330, 300, 900, 540, 4, 10)            # barras do transporte
GL = Graf(220, 260, 1000, 580, 5, 120)          # vendas da loja
MARCAS_B = [0, 2, 4, 6, 8, 10]
MARCAS_L = [0, 20, 40, 60, 80, 100, 120]


def barras(c, t, t0, titulo_t=None, valores=False):
    E.colunas(c, t, t0, TRANSP, GB.x, GB.y, GB.w, GB.h, vmax=10, eixo_y=True, marcas=MARCAS_B, valores=valores, size=42)
    E.foco(c, t, titulo_t if titulo_t is not None else t0, 0.4,
           lambda a: E.escreve(c, "Como as 20 pessoas vão ao trabalho", GB.x - 60, GB.y - 120, 48, "b", TINTA, a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.escreve(c, "pessoas", GB.x - 100, GB.y - 46, 38, "i", TINTA2, a))


def vendas(c, t, t0, d=1.4, eixos=True, cor=TINTA, titulo=True):
    if eixos:
        eixos_linha(c, t, t0, GL, VENDAS, MARCAS_L, "unidades")
    E.serie(c, t, t0, VENDAS, GL.x, GL.y, GL.w, GL.h, vmin=0, vmax=120, marcas=MARCAS_L, cor=cor, d=d, eixos=False, size=40)
    if titulo:
        E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, "Vendas da loja, mês a mês", GL.x - 60, GL.y - 110, 48, "b", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        vendas(c, t, a1, 1.6)
        anel(c, t, c1, GL.pt(3, 100), 34)
        E.foco(c, t, c1 + 0.2, 0.4, lambda a: E.pilula(c, "abril?", GL.px(3), GL.py(100) - 140, 40, "g", fundo=ERRADO, a=a))
        trecho(c, t, d1, GL, VENDAS, 1)
        X = 1570
        E.frase(c, t, b1, ps("onde as vendas", "i", 62), X, 330, "center", 0.1)
        E.frase(c, t, b1 + 0.6, [("mais subiram?", "g", 70, COR)], X, 430, "center", 0.1)
        E.frase(c, t, c1 + 0.4, ps("o ponto mais alto?", "i", 56, ERRADO), X, 590, "center", 0.1)
        bola_txt(c, t, d1 + 0.3, "fev → mar", X, 800, 150, 54)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("gráficos de", "i", 88) + [("barras", "g", 100, COR)], XE, 420, passo=0.14)
        E.frase(c, t, ta + 2.0, ps("e de", "i", 88) + [("linhas", "g", 100, COR)], XE, 540, passo=0.14)
        E.frase(c, t, ta + 3.2, [("a maior alta", "g", 84)] + ps("e a variação em %", "i", 76), XE, 680, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a tabela de frequência", None), ("s03.c", "a variação percentual:", "f{diferença}{valor de antes}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 90, "left", 0.1)
        if l2:
            E.formula_em(c, t, C[k] + 0.6, l2, x + w - 60, y + 150, 56, "g", COR, "right")
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- barras ----------------
def b_barras(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    barras(c, t, a4, titulo_t=b5 if t < C["s05"] else a4)
    X = 1570

    def um():
        E.frase(c, t, a4, ps("cada resposta vira", "i", 58) + [("uma barra", "g", 62, COR)], X, 400, "center", 0.1)
        E.frase(c, t, b4, [("altura", "g", 66, COR)] + ps("= frequência", "i", 62), X, 560, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)

    def dois():
        E.frase(c, t, a5, ps("olhe", "i", 66) + [("3 coisas", "g", 70, COR)], X, 260, "center", 0.1)
        for k, (ti, txt, caixa) in enumerate(((b5, "o título", (GB.x - 80, GB.y - 180, 1000, 90)),
                                              (c5, "o eixo de baixo", (GB.x - 10, GB.y + GB.h + 10, GB.w + 20, 90)),
                                              (d5, "o eixo do lado e a unidade", (GB.x - 130, GB.y - 90, 120, GB.h + 120)))):
            p = ep(t, ti, 0.5) * (1 - ep(t, ti + 2.4, 0.4) if k < 2 else 1)
            if p > 0:
                E.caixa_pontilhada(c, *caixa, p, None, prog_=ep(t, ti, 0.5))
            E.foco(c, t, ti, 0.4, lambda a, k=k: (E.bola(c, X - 300, 420 + 150 * k, 40, a=a), centro(c, str(k + 1), X - 300, 437 + 150 * k, 48, "g", E.SOBRE, a)))
            E.frase(c, t, ti + 0.1, ps(txt, "i", 52), X - 240, 438 + 150 * k, "left", 0.08)
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, a6, ps("onde o topo encontra", "i", 54), X, 300, "center", 0.1)
    E.frase(c, t, a6 + 1.0, [("o eixo do lado", "g", 58, COR)], X, 380, "center", 0.1)
    guia(c, t, b6, GB, 0, 8)
    guia(c, t, c6, GB, 1, 5, cor=CATS[1])
    E.frase(c, t, b6 + 0.3, ps("ônibus:", "i", 56) + [("8", "g", 62, COR)], X - 150, 540, "center", 0.1)
    E.frase(c, t, c6 + 0.3, ps("carro:", "i", 56) + [("5", "g", 62)], X + 150, 540, "center", 0.1)
    fcen(c, t, d6, "8 − 5", X - 150, 760, 84)
    bola_txt(c, t, d6 + 0.6, "3", X + 170, 740, 100, 100)
    E.frase(c, t, d6 + 1.0, ps("pessoas a mais", "i", 48, TINTA2), X + 170, 910, "center", 0.1)


# ---------------- linhas ----------------
def b_linhas(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    eixos_linha(c, t, b7, GL, VENDAS, MARCAS_L, "unidades")
    E.foco(c, t, b7, 0.4, lambda a: E.escreve(c, "Vendas da loja, mês a mês", GL.x - 60, GL.y - 110, 48, "b", TINTA, a))
    if t >= C["s08"] - 0.6:
        E.serie(c, t, a8 - 0.5, VENDAS, GL.x, GL.y, GL.w, GL.h, vmin=0, vmax=120, marcas=MARCAS_L, cor=TINTA, d=max(0.5, e8 - a8), eixos=False, size=40)
    X = 1570

    def um():
        E.frase(c, t, a7, ps("o que", "i", 62) + [("muda com o tempo", "g", 64, COR)], X, 300, "center", 0.1)
        E.frase(c, t, b7, ps("meses no eixo de baixo", "i", 52), X, 460, "center", 0.1)
        E.frase(c, t, c7, ps("cada ponto = o valor do mês", "i", 52), X, 580, "center", 0.1)
        E.frase(c, t, d7, ps("a linha liga", "i", 52) + [("em ordem", "g", 56, COR)], X, 700, "center", 0.1)
        if t >= d7:
            p = ep(t, d7 + 0.4, 1.0)
            M.arrow(c, GL.px(0), GL.y + GL.h + 110, lerp(GL.px(0), GL.px(4), p), GL.y + GL.h + 110, E.COR, p, 5, 16, p)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t >= C["s08"]:
        for k, (ti, (m, v)) in enumerate(zip((a8, b8, c8, d8, e8), VENDAS)):
            E.frase(c, t, ti, ps(m + ":", "i", 54) + [(str(v), "g", 58, COR)], X, 300 + 110 * k, "center", 0.1)


# ---------------- a maior alta ----------------
def b_alta(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0 = C["s10.a"], C["s10.b"]
    vendas(c, t, -9)
    trecho(c, t, a0, GL, VENDAS, 1)
    variacoes(c, t, [b9, c9, d9, e9], GL, VENDAS)
    anel(c, t, b0, GL.pt(3, 100), 34, TINTA2)
    X = 1570
    E.frase(c, t, a9, ps("alta = a subida de um", "i", 52), X, 280, "center", 0.1)
    E.frase(c, t, a9 + 1.0, ps("ponto para o", "i", 52) + [("seguinte", "g", 56, COR)], X, 350, "center", 0.1)
    fcen(c, t, b9, "50 − 40 = 10", X, 490, 58)
    fcen(c, t, c9, "80 − 50 = 30", X, 590, 58, COR)
    fcen(c, t, d9, "100 − 80 = 20", X, 690, 58)
    fcen(c, t, e9, "abr → mai: desce 10", X, 790, 50, TINTA2)
    E.foco(c, t, a0, 0.5, lambda a: E.pilula(c, "maior alta: fev → mar", X, 920, 50, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, b0, ps("abril: maior valor, subiu menos", "i", 46, TINTA2), X, 1020, "center", 0.08)


# ---------------- variação em porcentagem ----------------
def b_variacao(c, t, C, b):
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    vendas(c, t, -9)
    variacoes(c, t, [-9, -9, -9, -9], GL, VENDAS)
    trecho(c, t, C["s11"], GL, VENDAS, 1)
    X = 1570

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("a alta em", "i", 60) + [("%", "g", 66, COR)], X, 260, "center", 0.1)
        fcen(c, t, a1, "f{diferença}{valor de antes}", X, 420, 60)
        fcen(c, t, b1, "30 ÷ 50 = 0,6", X, 620, 72)
        bola_txt(c, t, c1, "60%", X, 820, 120, 76)
        E.frase(c, t, c1 + 0.5, ps("de alta", "i", 50, TINTA2), X, 1010, "center", 0.1)
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    trecho(c, t, a2, GL, VENDAS, 3, TINTA2)
    E.frase(c, t, C["s12"] + 0.2, ps("na queda, a mesma conta", "i", 54), X, 260, "center", 0.1)
    fcen(c, t, a2, "100 → 90: caiu 10", X, 420, 60)
    fcen(c, t, b2, "10 ÷ 100 = 0,1", X, 600, 72)
    bola_txt(c, t, c2, "10%", X, 800, 120, 76, TINTA2)
    E.frase(c, t, c2 + 0.5, ps("de queda", "i", 50, TINTA2), X, 990, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    barras(c, t, C["s13"])
    X = 1570
    E.frase(c, t, C["s13"] + 0.2, [("erro comum:", "g", 62, ERRADO)], X, 260, "center", 0.1)
    E.frase(c, t, a3, ps("contar as linhas", "i", 54), X, 350, "center", 0.1)
    E.frase(c, t, a3 + 1.0, ps("sem ler o eixo", "i", 54), X, 420, "center", 0.1)
    if t >= b3:
        p = ep(t, b3, 0.5)
        E.caixa_pontilhada(c, GB.x - 130, GB.py(10) - 40, 120, GB.py(0) - GB.py(10) + 80, p, None, prog_=p)
    E.frase(c, t, b3 + 0.2, ps("cada linha vale", "i", 54) + [("2", "g", 60, COR)], X, 560, "center", 0.1)
    # as linhas contadas ao lado da barra do ônibus
    for k in range(1, 5):
        ti = lerp(c3 - 1.2, c3, k / 4)
        y = GB.py(2 * k)
        E.foco(c, t, ti, 0.3, lambda a, k=k, y=y: (M.line(c, GB.px(0) + 80, y, GB.px(0) + 150, y, ERRADO if t < e3 else CERTO, a, 5),
                                                  E.escreve(c, str(k), GB.px(0) + 165, y + 18, 50, "g", ERRADO if t < e3 else CERTO, a)))
    E.frase(c, t, c3, ps("quarta linha", "i", 54), X, 660, "center", 0.1)
    fcen(c, t, d3, "4 pessoas?", X, 780, 72, ERRADO)
    if t >= e3 - 0.3:
        E.risco(c, X - 200, 800, X + 200, 730, t, e3 - 0.3, largura=10)
    fcen(c, t, e3, "4 × 2 = 8", X, 930, 84, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    G = Graf(220, 360, 860, 520, 5, 120)
    pts = [G.pt(i, v) for i, (_, v) in enumerate(VENDAS)]

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a4, ps("procure o trecho", "i", 72, CLARO) + [("mais em pé", "g", 78, BR)], W / 2, 270, "center", 0.1)
        M.line(c, G.x, G.y + G.h, G.x + G.w, G.y + G.h, CLARO, ep(t, C["s14"], 0.5), 4)
        for i, (m, _) in enumerate(VENDAS):
            E.foco(c, t, C["s14"] + 0.1 * i, 0.4, lambda a, i=i, m=m: centro(c, m, G.px(i), G.y + G.h + 60, 40, "b", CLARO, a))
        linha_palco(c, t, C["s14"] + 0.2, pts, 1.2, CLARO, 6)
        p = ease_io(prog(t, c4, 0.6))
        if p > 0:
            M.line(c, *pts[1], *pts[2], BR, 1, 16, progress=p)
        E.frase(c, t, b4, ps("mais inclinada,", "i", 60, CLARO), 1500, 480, "center", 0.1)
        E.frase(c, t, b4 + 0.8, [("maior alta", "g", 66, BR)], 1500, 570, "center", 0.1)
        E.frase(c, t, c4, ps("fev → mar: quase dispara", "i", 52, CLARO), 1500, 700, "center", 0.1)
        E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "sem fazer conta", 1500, 850, 58, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("funciona porque os meses", "i", 62, CLARO), W / 2, 180, "center", 0.1)
    E.frase(c, t, a5, ps("estão", "i", 62, CLARO) + [("igualmente espaçados", "g", 66, BR)], W / 2, 270, "center", 0.1)
    y0 = 420
    for i in range(5):
        x = 360 + 300 * i
        E.foco(c, t, a5 + 0.15 * i, 0.4, lambda a, x=x: c.drawCircle(x, y0, 12, M.paint(BR, a)))
        if i < 4:
            E.foco(c, t, a5 + 0.15 * i + 0.1, 0.4, lambda a, x=x: (M.line(c, x + 20, y0, x + 280, y0, CLARO, a, 3),
                                                                  centro(c, "1 passo", x + 150, y0 - 24, 34, "i", CLARO, a)))
    E.frase(c, t, b5, ps("mesmo passo para o lado:", "i", 54, CLARO) + [("quem sobe mais fica mais em pé", "g", 56, BR)], W / 2, 540, "center", 0.08)
    E.foco(c, t, c5, 0.5, lambda a: E.selo(c, 330, 690, 44, False, a))
    E.frase(c, t, c5 + 0.1, ps("espaço muda: anos pulados", "i", 56, CLARO), 410, 712, "left", 0.1)
    for i, ano in enumerate(("2018", "2019", "2022")):
        x = 1250 + [0, 160, 560][i]
        E.foco(c, t, d5 + 0.15 * i, 0.4, lambda a, x=x, ano=ano: (c.drawCircle(x, 780, 10, M.paint(BR, a)), centro(c, ano, x, 840, 36, "b", CLARO, a)))
    E.foco(c, t, e5, 0.5, lambda a: E.pilula(c, "calcule as diferenças", W / 2, 960, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
GQ = Graf(1130, 330, 690, 500, 5, 600)
MARCAS_Q = [0, 100, 200, 300, 400, 500, 600]


def museu(c, t, t0, d, G=GQ, size=36):
    eixos_linha(c, t, t0, G, MUSEU, MARCAS_Q, "visitantes", size)
    E.serie(c, t, t0 + 0.3, MUSEU, G.x, G.y, G.w, G.h, vmin=0, vmax=600, marcas=MARCAS_Q, cor=TINTA, d=d, eixos=False, size=size)


def b_questao(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6, ps("visitantes de um", "i", 60) + [("museu", "g", 64, COR)], XE, 300, passo=0.1)
    E.frase(c, t, a6 + 1.2, ps("de junho a outubro", "i", 56, TINTA2), XE, 380, passo=0.1)
    E.frase(c, t, c6, [("1)", "g", 60, COR)] + ps("em que período a", "i", 58) + [("maior alta?", "g", 62, COR)], XE, 620, passo=0.1)
    E.frase(c, t, d6, [("2)", "g", 60, COR)] + ps("de quantos", "i", 58) + [("%?", "g", 62, COR)], XE, 740, passo=0.1)
    E.saida(c, t, C["s17.a"] - 0.1, lambda: museu(c, t, b6 - 0.3, max(1.0, (c6 - b6) * 0.9)))
    E.relogio(c, t, C["s17.a"], 1410, 560, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8, e8, f8 = (C[f"s18.{k}"] for k in "abcdef")
    a9, b9 = C["s19.a"], C["s19.b"]
    G = Graf(220, 260, 1000, 580, 5, 600)
    museu(c, t, -9, 1.0, G, 40)
    trecho(c, t, e8, G, MUSEU, 1)
    variacoes(c, t, [a8, b8, c8, d8], G, MUSEU)
    anel(c, t, f8, G.pt(4, 500), 34, TINTA2)
    X = 1570

    def um():
        fcen(c, t, a8, "250 − 200 = 50", X, 280, 54)
        fcen(c, t, b8, "450 − 250 = 200", X, 380, 54, COR)
        fcen(c, t, c8, "ago → set: desce", X, 480, 50, TINTA2)
        fcen(c, t, d8, "500 − 360 = 140", X, 580, 54)
        E.foco(c, t, e8, 0.5, lambda a: E.pilula(c, "maior alta: jul → ago", X, 720, 50, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, f8, ps("outubro: maior valor,", "i", 48, TINTA2), X, 850, "center", 0.08)
        E.frase(c, t, f8 + 0.9, ps("não a maior alta", "i", 48, TINTA2), X, 915, "center", 0.08)
    fase(c, t, C["s18"], C["s19"] - 0.1, um)
    if t < C["s19"] - 0.1:
        return
    E.frase(c, t, C["s19"] + 0.1, ps("em", "i", 60) + [("%:", "g", 66, COR)], X, 280, "center", 0.1)
    fcen(c, t, a9, "200 ÷ 250 = 0,8", X, 470, 70)
    bola_txt(c, t, b9, "80%", X, 700, 130, 80)
    E.frase(c, t, b9 + 0.5, ps("de alta", "i", 50, TINTA2), X, 900, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s20.a", ps("leia", "i", 64) + [("título, eixos e unidade", "g", 66, COR)] + ps("antes", "i", 64)),
                 ("s20.b", [("maior alta", "g", 66, COR)] + ps("= maior subida entre dois pontos seguidos", "i", 56)))
        for i, (k, partes) in enumerate(itens):
            y = 470 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
        E.frase(c, t, C["s20.b"] + 2.2, ps("não o ponto mais alto", "i", 52, TINTA2), 290, 760, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a1, ps("o gráfico de", "i", 84) + [("setores", "g", 110, COR)], XE, 410)
    E.pizza(c, t, a1 + 0.6, [("25%", 25), ("", 75)], 640, 690, 150, cores=[E.COR, E.mix(CINZA, PAPEL, 0.55)], pct=False, rotulos=False)
    fcen(c, t, b1, "25% → 90°", 1120, 720, 80, COR)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barras=b_barras, linhas=b_linhas, alta=b_alta, variacao=b_variacao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
