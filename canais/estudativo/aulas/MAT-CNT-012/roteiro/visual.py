"""Visual — Estudativo · MAT-CNT-012: probabilidade com contagem.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 011): casinhas() com o número de opções dentro, × entre elas,
igual_bola() com o resultado na esfera; casinha "fixo" (cheia) para quem já está decidido; pessoa() e bloco() da MAT-CNT-005;
dado() da MAT-CNT-011. Frações com E.fr, E.pontes e E.resultado do kit.
Peça desta aula:
- tabela66(): a tabela 6×6 dos dois dados (linhas = dado branco, colunas = dado vermelho), com as faces nos cabeçalhos;
  cada quadradinho pode acender numa cor, com um texto dentro, no instante da fala.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
from itertools import combinations
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-012_probabilidade_contagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dados", "sorteio", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERM = "#D94B3D"
PARES = [(b, v) for b in range(1, 7) for v in range(1, 7)]
SETE = [(b, v) for b, v in PARES if b + v == 7]
OITO = [(b, v) for b, v in PARES if b + v == 8]
assert len(PARES) == 36 and SETE == [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)] and Fr(6, 36) == Fr(1, 6)
assert Fr(1, 11) != Fr(1, 6) and sum(1 for b, v in PARES if b + v == 2) == 1
G = list(combinations(range(8), 3))
assert len(G) == 56 == 8 * 7 * 6 // 6 and sum(1 for g in G if 0 in g) == 21 == 7 * 6 // 2 and Fr(21, 56) == Fr(3, 8)
assert Fr(1, 8) * 100 == Fr(25, 2) and Fr(3, 8) * 100 == Fr(75, 2) and Fr(3, 36) == Fr(1, 12)
assert OITO == [(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)] and Fr(5, 36).denominator == 36
assert len(list(combinations(range(6), 2))) == 15 == 6 * 5 // 2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (iguais às da MAT-CNT-002) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def casinhas(c, t, cx, y, itens, s=180, gap=None, tx=None, escuro=False, size=None, tnomes=None):
    """as casinhas do princípio multiplicativo, centradas em cx; y = centro das caixas.
    itens = [(nome embaixo, valor, t_caixa, t_valor[, cor do valor])]; valor None = caixa vazia; "?" sai em cinza;
    cor "fixo" = algarismo já decidido: caixa cheia, valor em branco, sem × ao lado.
    tx = instante de cada × (None = sem ×; senão, junto com a caixa da direita); tnomes = instante de cada nome.
    Devolve o centro de cada caixa."""
    n = len(itens)
    gap = s * 0.62 if gap is None else gap
    if size is None:
        vals = [len(str(it[1])) for it in itens if it[1] is not None]
        maior = max(vals) if vals else 1
        size = s * (0.56 if maior <= 1 else 0.46 if maior == 2 else 0.36)
    x0 = cx - (n * s + (n - 1) * gap) / 2
    xs = [x0 + s / 2 + i * (s + gap) for i in range(n)]
    borda = BR if escuro else TINTA
    fixo = [len(it) > 4 and it[4] == "fixo" for it in itens]
    for i, it in enumerate(itens):
        nome, val, tb, tv = it[:4]
        cor_v = it[4] if len(it) > 4 else (BR if escuro else (CINZA if val == "?" else COR))
        x = xs[i]

        def caixa(a, x=x, cheia=fixo[i]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.12, s * 0.12)
            if escuro:
                c.drawRRect(r, M.paint(BR, (0.3 if cheia else 0.08) * a))
            else:
                sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
                sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
                c.save(); c.translate(0, 8); c.drawRRect(r, sh); c.restore()
                c.drawRRect(r, M.paint(TINTA if cheia else BR, a))
            c.drawRRect(r, M.paint(borda, a, stroke=5))
        E.foco(c, t, tb, 0.45, caixa)
        if nome:
            tn = tnomes[i] if tnomes else tb + 0.15
            E.foco(c, t, tn, 0.45, lambda a, x=x, nome=nome: centro(c, nome, x, y + s / 2 + max(52, s * 0.34), max(42, s * 0.27), "i",
                                                                  CLARO if escuro else TINTA2, a))
        if val is not None and tv is not None:
            cv = BR if cor_v == "fixo" else cor_v
            E.foco(c, t, tv, 0.45, lambda a, x=x, val=str(val), cv=cv: E.formula(c, val, x, y + size * 0.36, size, "g", cv, a, "center"))
        if i and not fixo[i] and not fixo[i - 1]:
            ti = tx[i - 1] if tx else tb
            if ti is not None:
                E.sinal(c, t, ti, "×", (xs[i - 1] + x) / 2, y, s * 0.42, BR if escuro else TINTA)
    return xs


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def marca(c, t, t0, x, y, s, t1=None, cor=None):
    """caixa pontilhada em volta da casinha da vez (some em t1)"""
    def f():
        p = ep(t, t0, 0.4)
        m = s * 0.16
        E.caixa_pontilhada(c, x - s / 2 - m, y - s / 2 - m, s + 2 * m, s + 2 * m, p, cor, p)
    if t >= t0:
        E.saida(c, t, t1, f) if t1 is not None else f()


def regra(c, t, t0, x, y, txt, fundo=None, size=40, t1=None):
    """pílula com a restrição, centrada em (x, y)"""
    f = lambda: E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x, y, size, estilo="b", fundo=fundo or TINTA2, a=a))
    E.saida(c, t, t1, f) if t1 is not None else f()


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


# ---------------- peças da MAT-CNT-005 e da MAT-CNT-004 ----------------
def pessoa(c, cx, cy, h, cor, nome=None, a=1.0, cor_nome=None, nome_y=None):
    """boneco simples: cabeça e tronco; (cx, cy) = centro do tronco. nome_y = linha de base do nome (senão, embaixo)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
    c.drawRRect(r, M.paint(cor, a))
    if nome:
        centro(c, nome, cx, nome_y if nome_y is not None else cy + h * 0.38 + 56, max(40, h * 0.24), "b", cor_nome or TINTA, a)


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


def fracao_corte(c, t, t0, cx, cy, size, cima, baixo, tcima=None, tc=None, cortar=(), cor=None, escuro=False):
    """fração de fatoriais: cima = lista de partes ("8", "×", "7", "×", "6!"), baixo = texto de baixo.
    tcima = instante de cada parte de cima (senão, junto); tc = instante do corte; cortar = índices de cima que somem com o de baixo."""
    tinta = cor or (BR if escuro else TINTA)
    esp = size * 0.22
    ws = [E.larg(p, "g", size) for p in cima]
    wc = sum(ws) + esp * (len(cima) - 1)
    wb = E.larg(baixo, "g", size)
    w = max(wc, wb) + size * 0.3
    y_cima, y_baixo = cy - size * 0.22, cy + size * 0.95
    E.foco(c, t, t0, 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.05, w, size * 0.09), 4, 4),
                                                 M.paint(tinta, a)))
    x = cx - wc / 2
    pos = []
    for i, (p, wp) in enumerate(zip(cima, ws)):
        ti = tcima[i] if tcima else t0
        E.foco(c, t, ti, 0.45, lambda a, p=p, x=x: E.escreve(c, p, x, y_cima, size, "g", tinta, a))
        pos.append((x, wp))
        x += wp + esp
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, baixo, cx - wb / 2, y_baixo, size, "g", tinta, a))
    if tc is not None and t >= tc:
        risca = E.COR if not escuro else CLARO
        for i in cortar:
            xx, wp = pos[i]
            E.risco(c, xx - 8, y_cima + 8, xx + wp + 8, y_cima - size * 0.78, t, tc, risca, size * 0.09)
        E.risco(c, cx - wb / 2 - 8, y_baixo + 8, cx + wb / 2 + 8, y_baixo - size * 0.78, t, tc + 0.2, risca, size * 0.09)
    return w



def fila(c, t, estados, cx, cy, passo, desenha, d=0.6, alto=None):
    """itens em fila que trocam de lugar. estados = [(instante, [ids na ordem])]; desenha(id, x, y).
    Quem muda de lugar desliza em arco (os que vão para a direita por cima, os outros por baixo). Devolve {id: x}"""
    cur, ant, q = estados[0][1], estados[0][1], 1.0
    for ti, ordem in estados:
        if t >= ti:
            ant, cur = cur, ordem
            q = ease_io(prog(t, ti, d))
    n = len(cur)
    alto = passo * 0.6 if alto is None else alto
    xs = {}
    for k in cur:
        i0, i1 = ant.index(k), cur.index(k)
        x = cx + (lerp(i0, i1, q) - (n - 1) / 2) * passo
        y = cy - math.sin(math.pi * q) * alto * (1 if i1 > i0 else -1 if i1 < i0 else 0)
        xs[k] = x
        desenha(k, x, y)
    return xs


# ---------------- peças da MAT-CNT-011 ----------------
PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, a=1.0, cor=None, fundo=BR, borda=None, sombra=True):
    """face de dado com as pintas; dado vermelho = fundo VERM, pintas brancas"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    if sombra:
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda or (TINTA if fundo == BR else M.mix(fundo, "#000000", 0.35)), a, stroke=max(3, s * 0.035)))
    k = s * 0.27
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.085, M.paint(cor or (TINTA if fundo == BR else BR), a))


def branco(c, cx, cy, s, n, a=1.0):
    dado(c, cx, cy, s, n, a)


def vermelho(c, cx, cy, s, n, a=1.0):
    dado(c, cx, cy, s, n, a, fundo=VERM)


# ---------------- peça desta aula: a tabela 6×6 ----------------
def tabela66(c, t, t0, x, y, cel, tl=None, tc=None, pinta=None, apaga=None, meio=None):
    """tabela dos dois dados: (x, y) = canto de cima à esquerda da grade; linhas = dado branco (1 a 6, de cima para baixo),
    colunas = dado vermelho. tl/tc = instante dos cabeçalhos; pinta = {(b, v): (t0, cor, texto)}; apaga = (t0, alfa) esmaece o resto.
    Devolve a função (b, v) → centro do quadradinho"""
    centro_ = lambda b, v: (x + (v - 0.5) * cel, y + (b - 0.5) * cel)
    k_ap = 1.0
    if apaga:
        k_ap = 1 - (1 - apaga[1]) * ep(t, apaga[0], 0.5)

    def grade(a):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 6 * cel), 16, 16), M.paint(BR, 0.85 * a))
        for i in range(7):
            M.line(c, x + i * cel, y, x + i * cel, y + 6 * cel, TINTA2, a * 0.5, 2.5)
            M.line(c, x, y + i * cel, x + 6 * cel, y + i * cel, TINTA2, a * 0.5, 2.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 6 * cel), 16, 16), M.paint(TINTA, a, stroke=4))
    E.foco(c, t, t0, 0.5, grade)
    for i in range(1, 7):
        E.foco(c, t, (tl if tl is not None else t0) + 0.08 * i, 0.4, lambda a, i=i: branco(c, x - cel * 0.62, y + (i - 0.5) * cel, cel * 0.72, i, a))
        E.foco(c, t, (tc if tc is not None else t0) + 0.08 * i, 0.4, lambda a, i=i: vermelho(c, x + (i - 0.5) * cel, y - cel * 0.62, cel * 0.72, i, a))
    if meio:
        meio(centro_)
    for (b, v), (tp, cor, txt) in (pinta or {}).items():
        cx, cy = centro_(b, v)

        def cheia(a, cx=cx, cy=cy, cor=cor, txt=txt):
            m = cel * 0.08
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - cel / 2 + m, cy - cel / 2 + m, cel - 2 * m, cel - 2 * m), 10, 10), M.paint(cor, a))
            if txt:
                centro(c, txt, cx, cy + cel * 0.13, cel * 0.36, "g", BR, a)
        E.foco(c, t, tp, 0.35, cheia, sobe=4)
    if apaga and k_ap < 1:
        # véu sobre os quadradinhos não pintados
        for b in range(1, 7):
            for v in range(1, 7):
                if (b, v) not in (pinta or {}):
                    cx, cy = centro_(b, v)
                    c.drawRect(skia.Rect.MakeXYWH(cx - cel / 2 + 2, cy - cel / 2 + 2, cel - 4, cel - 4), M.paint("#F4F3EF", 1 - k_ap))
    return centro_


def diagonal(c, t, t0, f, ini, fim, cor=None, largura=10):
    """linha que atravessa os quadradinhos de ini até fim"""
    if t < t0:
        return
    (x0, y0), (x1, y1) = f(*ini), f(*fim)
    M.line(c, x0, y0, x1, y1, cor or E.COR, 0.9, largura, progress=ease_io(prog(t, t0, 0.7)))


TX, TY, TC = 330, 250, 108  # a tabela grande, à esquerda


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: (branco(c, 330, 330, 190, 3, a), vermelho(c, 560, 330, 190, 4, a)))
        E.frase(c, t, C["s01.b"], [("chance", "i", 80), ("de", "i", 80), ("a", "i", 80), ("soma", "i", 80), ("dar", "i", 80), ("7?", "g", 96, COR)], 760, 360)
        E.frase(c, t, C["s01.b"] + 1.6, ps("somas de 2 a 12: são 11", "i", 60, TINTA2), XE + 60, 620, passo=0.12)
        E.fr(c, t, C["s01.c"], 1, 11, 400, 820, 120, ERRADO)
        if t >= C["s01.d"]:
            E.risco(c, 310, 900, 490, 740, t, C["s01.d"], largura=12)
            E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "errado", 540, 850, 72, "g", ERRADO, a))
        E.foco(c, t, C["s01.e"] - 0.2, 0.4, lambda a: E.escreve(c, "é", 1020, 850, 90, "i", TINTA, a))
        E.resultado(c, t, C["s01.e"], 1, 6, 1300, 800, 110, 150)
    E.saida(c, t, C["s02"] - 0.1, pergunta)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("probabilidade", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("com", "i", 110), ("contagem", "g", 120)], XE, 630)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 490, 84, "g", BR, a),
                                                      E.escreve(c, "de sorteio", 1270, 590, 80, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.a", 110, "probabilidade"), ("s03.b", 680, "casinhas"), ("s03.c", 1250, "combinação")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 560, 600, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 60, COR)], x + 280, 390, "center")
    E.fr(c, t, C["s03.a"] + 0.4, "favoráveis", "possíveis", 390, 600, 60)
    E.foco(c, t, C["s03.a"] + 1.4, 0.4, lambda a: E.centro(c, "mesma chance", 390, 790, 46, "i", TINTA2, a))
    casinhas(c, t, 960, 610, [("", 6, C["s03.b"] + 0.2, C["s03.b"] + 0.4), ("", 6, C["s03.b"] + 0.3, C["s03.b"] + 0.5)], s=130, gap=80)
    E.foco(c, t, C["s03.b"] + 0.8, 0.4, lambda a: E.centro(c, "etapas: multiplique", 960, 790, 46, "i", TINTA2, a))
    E.formula_em(c, t, C["s03.c"] + 0.3, "C = f{A(n, p)}{p!}", 1530, 640, 80, "g", TINTA, "center")
    E.foco(c, t, C["s03.c"] + 0.8, 0.4, lambda a: E.centro(c, "a ordem não importa", 1530, 790, 46, "i", TINTA2, a))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.55), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- dois dados ----------------
def b_dados(c, t, C, b):
    def casas():
        E.foco(c, t, C["s04.a"], 0.5, lambda a: (branco(c, 620, 380, 220, 5, a), vermelho(c, 1300, 380, 220, 2, a)))
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: (E.centro(c, "branco", 620, 560, 56, "i", TINTA2, a), E.centro(c, "vermelho", 1300, 560, 56, "i", VERM, a)))
        xs = casinhas(c, t, 820, 790, [("branco", 6, C["s04.b"], C["s04.b"] + 0.3), ("vermelho", 6, C["s04.c"], C["s04.c"] + 0.3)], s=170, gap=240,
                      tx=[C["s04.d"]])
        igual_bola(c, t, C["s04.d"] + 0.5, xs[1] + 150, 790, "36", r=110)
        E.foco(c, t, C["s04.d"] + 0.9, 0.5, lambda a: E.escreve(c, "possíveis", xs[1] + 150 + 52 + 230, 810, 56, "g", COR, a))
    E.saida(c, t, C["s05"] - 0.1, casas)
    if t < C["s05"]:
        return
    # a tabela fica na tela do s05 ao s08
    pinta = {}
    if t < C["s06"]:
        pinta[(3, 4)] = (C["s05.d"], E.COR, "")
    ks = ("s06.a", "s06.b", "s06.c", "s06.d", "s06.e", "s06.f")
    if t >= C["s06"]:
        for (bb, vv), k in zip(SETE, ks):
            pinta[(bb, vv)] = (C[k], E.COR, "7")
    if t >= C["s08.b"]:
        pinta[(1, 1)] = (C["s08.b"], ERRADO, "2")
    f = tabela66(c, t, C["s05.a"], TX, TY, TC, tl=C["s05.b"], tc=C["s05.c"], pinta=pinta,
                 meio=lambda f_: diagonal(c, t, C["s06.g"], f_, (1, 6), (6, 1), E.COR, 10))
    E.foco(c, t, C["s05.b"] + 0.2, 0.4, lambda a: E.escreve(c, "branco", TX - 160, TY + 6 * TC + 60, 40, "b", TINTA2, a))
    E.foco(c, t, C["s05.c"] + 0.2, 0.4, lambda a: E.escreve(c, "vermelho", TX + 6 * TC + 20, TY - TC * 0.62 + 14, 40, "b", VERM, a))
    RX = 1130

    def leitura():
        E.foco(c, t, C["s05.d"], 0.5, lambda a: (branco(c, RX + 60, 480, 110, 3, a), vermelho(c, RX + 200, 480, 110, 4, a)))
        E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: E.escreve(c, "1 quadradinho", RX, 620, 56, "g", COR, a))
        E.foco(c, t, C["s05.d"] + 0.6, 0.4, lambda a: E.escreve(c, "= 1 resultado", RX, 690, 52, "i", TINTA2, a))
        E.frase(c, t, C["s05.d"] + 2.4, ps("todos com a mesma chance", "i", 52, TINTA2), RX, 830, passo=0.1)
    E.saida(c, t, C["s06"] - 0.1, leitura)
    if C["s06"] <= t < C["s07"] + 0.4:
        def lista():
            E.frase(c, t, C["s06"] + 0.1, [("soma", "i", 64), ("7:", "g", 70, COR)], RX, 330)
            for i, ((bb, vv), k) in enumerate(zip(SETE, ks)):
                y = 430 + i * 85
                E.foco(c, t, C[k], 0.4, lambda a, bb=bb, vv=vv, y=y: (branco(c, RX + 30, y - 16, 62, bb, a), E.escreve(c, "+", RX + 80, y, 52, "g", TINTA, a),
                                                                   vermelho(c, RX + 160, y - 16, 62, vv, a)))
            E.foco(c, t, C["s06.g"] + 0.4, 0.5, lambda a: E.escreve(c, "6 quadradinhos", RX + 260, 650, 56, "g", COR, a))
        E.saida(c, t, C["s07"] - 0.1, lista)
    if C["s07"] <= t < C["s08"] + 0.4:
        def conta():
            E.fr(c, t, C["s07.a"], 6, 36, RX + 90, 560, 120, COR)
            E.pontes(c, t, RX + 190, RX + 400, 560, 120, "÷ 6", C["s07.a"] + 1.4, C["s07.a"] + 1.7, size=40)
            E.resultado(c, t, C["s07.b"], 1, 6, RX + 560, 560, 100, 130)
            E.foco(c, t, C["s07.a"] + 0.3, 0.4, lambda a: E.escreve(c, "favoráveis", RX, 400, 46, "b", CERTO, a))
            E.foco(c, t, C["s07.a"] + 0.6, 0.4, lambda a: E.escreve(c, "possíveis", RX, 760, 46, "b", TINTA2, a))
        E.saida(c, t, C["s08"] - 0.1, conta)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], ps("as somas não têm a mesma chance", "i", 56), RX - 40, 330, passo=0.1)
    E.foco(c, t, C["s08.b"], 0.45, lambda a: (E.escreve(c, "soma 2:", RX, 470, 60, "g", ERRADO, a), E.escreve(c, "1 jeito", RX + 260, 470, 60, "i", TINTA, a)))
    E.foco(c, t, C["s08.c"], 0.45, lambda a: (E.escreve(c, "soma 7:", RX, 580, 60, "g", COR, a), E.escreve(c, "6 jeitos", RX + 260, 580, 60, "i", TINTA, a)))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "conte resultados, não somas", RX + 310, 760, 46, estilo="g", a=a))


# ---------------- sorteio ----------------
NOMES8 = ["Ana", "", "", "", "", "", "", ""]
GENTE = ["#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A", "#9C9CA3", "#3FA7A0", "#B58A2E"]


def b_sorteio(c, t, C, b):
    def grupo():
        E.frase(c, t, C["s09.a"], [("8", "g", 84, COR), ("pessoas,", "i", 80), ("sorteio", "i", 80), ("de", "i", 80), ("3", "g", 84, COR)], W / 2, 190, "center")
        for i in range(8):
            x = W / 2 + (i - 3.5) * 190
            ana = i == 0 and t >= C["s09.c"]
            E.foco(c, t, C["s09.a"] + 0.3 + 0.07 * i, 0.4, lambda a, i=i, x=x, ana=ana: pessoa(c, x, 480, 170, GENTE[i], "Ana" if i == 0 else None, a,
                                                                                         COR if ana else TINTA))
        E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "comissão de 3", W / 2, 720, 54, estilo="g", fundo=TINTA2, a=a))
        if t >= C["s09.c"]:
            E.foco(c, t, C["s09.c"], 0.5, lambda a: E.caixa_pontilhada(c, W / 2 - 3.5 * 190 - 110, 330, 220, 330, a, E.COR, a))
        E.frase(c, t, C["s09.c"] + 0.2, [("chance", "i", 72), ("de", "i", 72), ("Ana", "g", 80, COR), ("estar", "i", 72), ("nela?", "g", 76)], W / 2, 890, "center")
    E.saida(c, t, C["s10"] - 0.1, grupo)
    if C["s10"] <= t < C["s12"] + 0.4:
        def contas():
            y1, y2 = 380, 760
            E.foco(c, t, C["s10.a"], 0.45, lambda a: E.escreve(c, "possíveis", XE, y1 - 60, 56, "g", TINTA2, a))
            E.foco(c, t, C["s10.a"] + 0.4, 0.45, lambda a: E.escreve(c, "3 entre 8", XE, y1 + 30, 64, "i", TINTA, a))
            E.formula_em(c, t, C["s10.b"], "f{8 × 7 × 6}{3!}", 650, y1 + 34, 100, "g", TINTA)
            igual_bola(c, t, C["s10.b"] + 2.4, 1080, y1, "56", r=95)
            E.foco(c, t, C["s11.a"], 0.45, lambda a: E.escreve(c, "favoráveis", XE, y2 - 60, 56, "g", CERTO, a))
            E.foco(c, t, C["s11.a"] + 0.4, 0.45, lambda a: E.escreve(c, "com Ana dentro", XE, y2 + 30, 60, "i", TINTA, a))
            xs = casinhas(c, t, 1590, y2 - 10, [("", "Ana", C["s11.a"] + 1.0, C["s11.a"] + 1.0, "fixo"), ("", "?", C["s11.b"], C["s11.b"] + 0.1),
                                                 ("", "?", C["s11.b"] + 0.1, C["s11.b"] + 0.2)], s=110, gap=40, size=34)
            E.foco(c, t, C["s11.b"] + 0.5, 0.4, lambda a: E.centro(c, "2 entre os 7 que sobram", 1590, y2 + 110, 42, "b", TINTA2, a))
            E.formula_em(c, t, C["s11.c"], "f{7 × 6}{2}", 650, y2 + 34, 100, "g", TINTA)
            igual_bola(c, t, C["s11.c"] + 1.6, 1000, y2, "21", r=95, cor=CERTO)
        E.saida(c, t, C["s12"] - 0.1, contas)
    if t < C["s12"]:
        return
    y = 420
    E.fr(c, t, C["s12.a"], 21, 56, 360, y, 120, TINTA)
    E.pontes(c, t, 470, 690, y, 120, "÷ 7", C["s12.a"] + 1.2, C["s12.a"] + 1.5, size=40)
    E.fr(c, t, C["s12.b"], 3, 8, 800, y, 120, COR)
    E.formula_em(c, t, C["s12.b"] + 1.2, "f{1}{8} = 12,5%", 1100, y + 40, 80, "g", TINTA2)
    E.formula_em(c, t, lerp(C["s12.b"], C["s12.c"], 0.4), "12,5 + 12,5 + 12,5", 300, 820, 84, "g", TINTA)
    igual_bola(c, t, C["s12.c"], 1100, 790, "37,5%", r=130, cor=CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], ps("tratar os dados como se fossem iguais", "i", 60, TINTA2), W / 2, 270, "center", passo=0.1)
    for i, txt in enumerate(("1 e 6", "2 e 5", "3 e 4")):
        E.foco(c, t, C["s13.b"] + 0.56 * i, 0.4, lambda a, i=i, txt=txt: E.escreve(c, txt, XE + 40, 440 + i * 110, 72, "g", ERRADO, a))
    E.foco(c, t, C["s13.b"] + 1.9, 0.4, lambda a: E.escreve(c, "e para aí", XE + 40, 760, 52, "i", TINTA2, a))
    E.fr(c, t, C["s13.c"], 3, 36, 640, 520, 100, ERRADO)
    E.sinal(c, t, C["s13.c"] + 1.0, "=", 760, 520, 80, ERRADO)
    E.fr(c, t, C["s13.c"] + 1.2, 1, 12, 870, 520, 100, ERRADO)
    if t >= C["s13.d"]:
        E.risco(c, 560, 610, 950, 420, t, C["s13.d"], largura=12)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (branco(c, 1170, 470, 130, 1, a), vermelho(c, 1320, 470, 130, 6, a)))
    E.sinal(c, t, C["s13.e"] - 0.2, "≠", 1245, 650, 100, ERRADO)
    E.foco(c, t, C["s13.e"], 0.5, lambda a: (branco(c, 1170, 820, 130, 6, a), vermelho(c, 1320, 820, 130, 1, a)))
    E.foco(c, t, C["s13.e"] + 1.0, 0.5, lambda a: E.centro(c, "quadradinhos diferentes", 1245, 990, 56, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def vagas():
        E.frase(c, t, C["s14.a"], ps("chance de 1 pessoa ser sorteada", "i", 72, CLARO), W / 2, 200, "center", passo=0.12)
        y = 520
        E.foco(c, t, C["s14.a"] + 1.6, 0.45, lambda a: E.escreve(c, "P =", 420, y + 40, 110, "g", BR, a))
        E.fr(c, t, C["s14.a"] + 2.0, "vagas", "pessoas", 860, y, 110, BR)
        E.fr(c, t, C["s14.b"], 3, 8, 860, 850, 130, BR)
        E.foco(c, t, C["s14.b"], 0.45, lambda a: E.escreve(c, "3 vagas, 8 pessoas:", 300, 880, 56, "i", CLARO, a))
        E.foco(c, t, C["s14.b"] + 1.6, 0.5, lambda a: E.pilula(c, "sem combinação nenhuma", 1400, 850, 50, estilo="g", fundo=E.COR, a=a))
    E.saida(c, t, C["s15"] - 0.1, vagas)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("sorteio justo: ninguém tem mais chance", "i", 68, BR), W / 2, 220, "center", passo=0.1)
    E.frase(c, t, C["s15.a"] + 2.4, ps("as vagas se dividem igualmente entre todos", "i", 56, CLARO), W / 2, 320, "center", passo=0.1)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "não compensa: mais de uma pessoa", W / 2, 520, 54, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s15.b"] + 2.2, [("Ana", "g", 72, BR), ("e", "i", 66, CLARO), ("Bia", "g", 72, BR), ("juntas", "i", 66, CLARO)], W / 2, 680, "center")
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "conte favoráveis e possíveis", W / 2, 850, 54, estilo="g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (branco(c, XE + 60, 350, 110, 2, a), vermelho(c, XE + 190, 350, 110, 6, a)))
    E.frase(c, t, C["s16.a"] + 0.3, [("chance", "i", 72), ("de", "i", 72), ("a", "i", 72), ("soma", "i", 72), ("dar", "i", 72), ("8?", "g", 84, COR)], XE + 290, 375)
    E.frase(c, t, C["s16.b"], [("6", "g", 80, COR), ("amigos,", "i", 72), ("2", "g", 80, COR), ("ingressos", "i", 72)], XE, 600)
    E.frase(c, t, C["s16.c"], [("chance", "i", 72), ("de", "i", 72), ("Ana", "g", 80, COR), ("e", "i", 72), ("Bia?", "g", 80, COR)], XE, 740)
    E.relogio(c, t, C["s17.a"], 1500, 600, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def dados():
        tp = [C["s18.a"] + 0.56 * i for i in range(5)]
        pinta = {(bb, vv): (tp[i], CERTO, "8") for i, (bb, vv) in enumerate(OITO)}
        f = tabela66(c, t, C["s18"] + 0.1, TX, TY, TC, pinta=pinta)
        RX = 1130
        E.frase(c, t, C["s18.b"], [("5", "g", 80, CERTO), ("favoráveis", "i", 64)], RX, 380)
        E.frase(c, t, C["s18.b"] + 0.9, [("36", "g", 80), ("possíveis", "i", 64)], RX, 480)
        E.fr(c, t, C["s18.c"], 5, 36, RX + 110, 680, 110, CERTO)
        E.foco(c, t, C["s18.c"] + 1.0, 0.4, lambda a: E.escreve(c, "não simplifica", RX + 260, 700, 50, "i", TINTA2, a))
        if t >= C["s18.d"]:
            x, y = f(4, 4)
            E.foco(c, t, C["s18.d"], 0.4, lambda a: E.caixa_pontilhada(c, x - TC * 0.62, y - TC * 0.62, TC * 1.24, TC * 1.24, a, E.COR, a))
            E.foco(c, t, C["s18.d"] + 0.2, 0.4, lambda a: E.escreve(c, "4 e 4: uma vez só", RX, 900, 56, "g", COR, a))
    E.saida(c, t, C["s19"] - 0.1, dados)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.1, [("ingressos", "g", 76), ("para", "i", 72), ("o", "i", 72), ("show", "i", 72)], W / 2, 180, "center")
    E.foco(c, t, C["s19.a"], 0.45, lambda a: E.escreve(c, "possíveis: duplas entre 6", XE, 330, 60, "b", TINTA2, a))
    E.formula_em(c, t, C["s19.b"], "f{6 × 5}{2}", XE, 500, 100, "g", TINTA)
    igual_bola(c, t, C["s19.b"] + 1.6, XE + 300, 466, "15", r=85)
    E.foco(c, t, C["s19.c"], 0.45, lambda a: E.escreve(c, "favoráveis: só 1 dupla", XE, 700, 60, "b", CERTO, a))
    for i, (nome, cor) in enumerate((("Ana", "#E08A3C"), ("Bia", "#8E5BD9"))):
        E.foco(c, t, C["s19.c"] + 0.5 + 0.2 * i, 0.4, lambda a, i=i, nome=nome, cor=cor: pessoa(c, XE + 130 + i * 150, 840, 120, cor, nome, a, TINTA))
    if t >= C["s19.c"] + 0.8:
        E.foco(c, t, C["s19.c"] + 0.8, 0.4, lambda a: bloco(c, XE + 60, XE + 350, 860, 170, a))
    E.resultado(c, t, C["s19.d"], 1, 15, 1300, 520, 110, 150, cor=CERTO)
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.pilula(c, "o atalho não serve: 2 pessoas", 1300, 850, 46, estilo="g", fundo=ERRADO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, txt) in enumerate((("s20.a", "conte os possíveis"), ("s20.b", "conte os favoráveis"), ("s20.c", "divida"))):
            y = 400 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y, 56, a=a), centro(c, str(i + 1), 420, y + 23, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(txt, "g", 80, COR if i == 2 else TINTA)], 520, y + 28)
        E.frase(c, t, C["s20.c"] + 1.0, ps("sempre com resultados de mesma chance", "i", 56, TINTA2), W / 2, 960, "center", passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("“pelo", "g", 100, COR), ("menos”", "g", 100, COR)], XE, 440)
    E.frase(c, t, C["s21.b"], [("1", "g", 70, COR), ("cara", "i", 64), ("em", "i", 64), ("3", "g", 70, COR), ("moedas", "i", 64)], XE, 580)
    E.frase(c, t, C["s21.c"], ps("olhe o que não pode acontecer", "i", 64, TINTA2), XE, 710, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(650, 355, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dados=b_dados, sorteio=b_sorteio, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
