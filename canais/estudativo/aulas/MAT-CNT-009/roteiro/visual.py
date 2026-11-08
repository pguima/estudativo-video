"""Visual — Estudativo · MAT-CNT-009: combinações em problemas de escolha.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 008): casinhas() com o número de opções dentro e a etapa embaixo,
"?" em cinza, × entre elas, igual_bola() com o resultado na esfera; regra() = pílula da restrição.
Peças vindas da MAT-CNT-005: pessoa() e bloco(). 
Peças desta aula:
- caixa(): a caixa de um grupo (homens, mulheres), com o nome numa pílula em cima; cada caixa é uma etapa.
- grupo(): as pessoas de um grupo dentro da caixa.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from itertools import combinations
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-009_combinacoes_problemas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("etapas", "pelomenos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
C_ = lambda n, p: sum(1 for _ in combinations(range(n), p))
HOM, MUL = "#4F7FB0", "#C2577F"
POVO = ["H"] * 5 + ["M"] * 4
assert C_(5, 2) == 10 and C_(4, 2) == 6 and 10 * 6 == 60 and 10 + 6 == 16
assert C_(9, 3) == 84 == 9 * 8 * 7 // 6 and 9 * 8 * 7 == 504
assert sum(1 for g in combinations(range(9), 3) if any(POVO[i] == "M" for i in g)) == 74
assert 4 * C_(5, 2) == 40 and C_(4, 2) * 5 == 30 and C_(4, 3) == 4 and 40 + 30 + 4 == 74 and 84 - C_(5, 3) == 74
assert C_(8, 2) == 28 and 4 * 28 == 112
assert C_(4, 2) * C_(6, 2) == 90 and C_(10, 3) == 120 and C_(6, 3) == 20 and 120 - 20 == 100 and 10 * 9 * 8 == 720


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


# ---------------- peças desta aula ----------------
def caixa(c, x, y, w, h, titulo, a=1.0, cor=None, forte=0.0, escuro=False):
    """a caixa de um grupo, com o nome numa pílula em cima; forte (0..1) acende a borda na cor da matéria"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 34, 34)
    if escuro:
        c.drawRRect(r, M.paint(BR, 0.06 * a))
    else:
        c.drawRRect(r, M.paint(BR, 0.7 * a))
    borda = M.mix(BR if escuro else TINTA2, E.COR, forte)
    c.drawRRect(r, M.paint(borda, a, stroke=5 + 3 * forte))
    E.pilula(c, titulo, x + w / 2, y, 44, estilo="g", fundo=cor or TINTA2, a=a)


def grupo(c, t, t0, cx, y, n, cor, h=100, passo_=None, apaga=()):
    passo_ = passo_ or h * 1.15
    for i in range(n):
        x = cx + (i - (n - 1) / 2) * passo_
        E.foco(c, t, t0 + 0.08 * i, 0.4, lambda a, x=x, i=i: pessoa(c, x, y, h, cor, None, a * (0.3 if i in apaga else 1.0)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: caixa(c, 170, 230, 760, 420, "homens", a, HOM))
        grupo(c, t, C["s01.a"] + 0.2, 550, 400, 5, HOM, 110, 135)
        E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: E.centro(c, "2 entre 5", 550, 590, 60, "g", HOM, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: caixa(c, 990, 230, 760, 420, "mulheres", a, MUL))
        grupo(c, t, C["s01.b"] + 0.2, 1370, 400, 4, MUL, 110, 135)
        E.foco(c, t, C["s01.b"] + 0.8, 0.4, lambda a: E.centro(c, "2 entre 4", 1370, 590, 60, "g", MUL, a))
        E.formula_em(c, t, C["s01.c"], "10 + 6 = 16", 260, 870, 110, "g", ERRADO)
        if t >= C["s01.d"]:
            E.risco(c, 240, 830, 920, 830, t, C["s01.d"], largura=12)
        E.foco(c, t, C["s01.d"] + 0.2, 0.4, lambda a: E.escreve(c, "certo:", 1100, 900, 80, "i", TINTA, a))
        E.foco(c, t, C["s01.d"] + 0.4, 0.5, lambda a: (E.bola(c, 1450, 870, 120, a=a), centro(c, "60", 1450, 870 + 40, 110, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("comissões", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("com", "i", 110), ("regras", "g", 120)], XE, 620)
        E.frase(c, t, C["s02.b"], [("o", "i", 84), ("“pelo", "g", 90, COR), ("menos", "g", 90, COR), ("um”", "g", 90, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.a", 160, "combinação"), ("s03.b", 1000, "casinhas")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 760, 640, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 380, 390, "center")
    E.formula_em(c, t, C["s03.a"] + 0.4, "C = f{A(n, p)}{p!}", 540, 640, 96, "g", TINTA, "center")
    E.foco(c, t, C["s03.a"] + 1.2, 0.4, lambda a: E.centro(c, "arranjo ÷ fatorial dos escolhidos", 540, 830, 42, "i", TINTA2, a))
    for i, (k, sg, cor, l1) in enumerate((("s03.c", "×", COR, "etapas: faz todas"), ("s03.d", "+", CERTO, "casos: um ou outro"))):
        y = 560 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, y=y, sg=sg, cor=cor: (E.bola(c, 1120, y, 58, cor, a), centro(c, sg, 1120, y + 28, 80, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), 1210, y + 18, passo=0.1)
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.55), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- comissão em etapas ----------------
def b_etapas(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("comissão", "i", 76), ("em", "i", 76), ("etapas", "g", 80, COR)], W / 2, 150, "center")
    fh = ep(t, C["s04.b"], 0.4) * (1 - ep(t, C["s04.c"], 0.4))
    fm = ep(t, C["s04.c"], 0.4) * (1 - ep(t, C["s04.d"], 0.4))
    E.foco(c, t, C["s04"] + 0.3, 0.5, lambda a: caixa(c, 150, 240, 720, 510, "homens", a, HOM, fh))
    E.foco(c, t, C["s04"] + 0.5, 0.5, lambda a: caixa(c, 1050, 240, 720, 510, "mulheres", a, MUL, fm))
    grupo(c, t, C["s04"] + 0.5, 510, 370, 5, HOM, 90, 120)
    grupo(c, t, C["s04"] + 0.7, 1410, 370, 4, MUL, 90, 120)
    E.sinal(c, t, C["s04.d"], "×", 960, 490, 140, COR)
    # homens e mulheres: a mesma conta em cada caixa
    for cx, k, cor, txt, conta, f, r_ in ((510, "s05", HOM, "2 entre 5", "5 × 4 = 20", "f{20}{2!}", "10"),
                                          (1410, "s06", MUL, "2 entre 4", "4 × 3 = 12", "f{12}{2!}", "6")):
        E.foco(c, t, C[k + ".a"], 0.4, lambda a, cx=cx, cor=cor, txt=txt: E.centro(c, txt, cx, 500, 54, "g", cor, a))
        E.formula_em(c, t, C[k + ".b"], conta, cx, 595, 60, "g", TINTA, "center")
        E.formula_em(c, t, C[k + ".c"], f, cx - 80, 690, 62, "g", TINTA, "center")
        igual_bola(c, t, C[k + ".c"] + 0.4, cx - 10, 676, r_, r=48)
    # junta
    E.frase(c, t, C["s07.a"], ps("cada dupla de homens com cada dupla de mulheres", "i", 46, TINTA2), W / 2, 830, "center", passo=0.08)
    E.formula_em(c, t, C["s07.b"], "10 × 6", 330, 980, 96, "g", TINTA)
    bx = igual_bola(c, t, C["s07.b"] + 0.4, 680, 946, "60", r=80)
    E.foco(c, t, C["s07.b"] + 0.6, 0.5, lambda a: E.escreve(c, "comissões", bx + 105, 970, 52, "g", COR, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "10 + 6 = 16: só conta duplas", 1520, 950, 34, estilo="b", fundo=ERRADO, a=a))


# ---------------- pelo menos um ----------------
def b_pelomenos(c, t, C, b):
    def pergunta():
        E.frase(c, t, C["s08.a"], [("“pelo", "g", 84, COR), ("menos", "g", 84, COR), ("um”", "g", 84, COR)], W / 2, 170, "center")
        for i, g in enumerate(POVO):
            x = W / 2 + (i - 4) * 150 + (30 if g == "M" else -30)
            E.foco(c, t, C["s08.b"] + 0.07 * i, 0.4, lambda a, x=x, g=g: pessoa(c, x, 360, 120, HOM if g == "H" else MUL, None, a))
        E.foco(c, t, C["s08.b"] + 0.8, 0.4, lambda a: (E.centro(c, "5 homens", W / 2 - 330, 500, 48, "b", HOM, a),
                                                     E.centro(c, "4 mulheres", W / 2 + 450, 500, 48, "b", MUL, a)))
        E.frase(c, t, C["s08.c"], [("comissões", "i", 64), ("de", "i", 64), ("3", "g", 68, COR), ("com", "i", 64), ("pelo", "i", 64), ("menos", "i", 64),
                                   ("1", "g", 68, MUL), ("mulher?", "g", 68, MUL)], W / 2, 640, "center", passo=0.1)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "total: 3 entre 9", 260, 870, 60, "b", TINTA2, a))
        E.formula_em(c, t, C["s08.d"] + 0.8, "f{9 × 8 × 7}{3!} = f{504}{6}", 820, 880, 84, "g", TINTA)
        igual_bola(c, t, C["s08.e"], 1530, 850, "84", r=90)
    E.saida(c, t, C["s09"] - 0.1, pergunta)
    if t < C["s09"]:
        return
    # os três casos, um por linha
    E.foco(c, t, C["s09"] + 0.1, 0.5, lambda a: E.pilula(c, "pelo menos 1 mulher = 1, 2 ou 3 mulheres", W / 2, 150, 46, estilo="g", fundo=TINTA2, a=a)
           if t < C["s09.d"] else None)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "cada comissão cai em um caso só: some", W / 2, 150, 46, estilo="g", fundo=CERTO, a=a))
    ys = (330, 560, 790)
    rot = (("s09.a", "1 mulher"), ("s09.b", "2 mulheres"), ("s09.c", "3 mulheres"))
    for (k, txt), y in zip(rot, ys):
        E.foco(c, t, C[k], 0.4, lambda a, y=y, txt=txt: (E.bola(c, XE + 30, y, 30, MUL, a), E.escreve(c, txt, XE + 80, y + 20, 56, "g", MUL, a)))
    s = 130
    xs = casinhas(c, t, 900, ys[0], [("mulher", 4, C["s10.a"], C["s10.a"] + 0.2), ("2 homens", 10, C["s10.a"] + 0.6, C["s10.a"] + 1.2)], s=s, gap=90)
    igual_bola(c, t, C["s10.b"], xs[1] + 115, ys[0], "40", r=70)
    xs = casinhas(c, t, 900, ys[1], [("2 mulheres", 6, C["s10.c"], C["s10.c"] + 0.2), ("homem", 5, C["s10.c"] + 0.6, C["s10.c"] + 1.0)], s=s, gap=90)
    igual_bola(c, t, C["s10.d"], xs[1] + 115, ys[1], "30", r=70)
    xs = casinhas(c, t, 900 - (s + 90) / 2, ys[2], [("3 mulheres", 4, C["s10.e"], C["s10.e"] + 0.3)], s=s)
    E.foco(c, t, C["s10.e"] + 1.0, 0.4, lambda a: E.escreve(c, "= deixar 1 de fora", xs[0] + 110, ys[2] + 20, 50, "i", TINTA2, a))
    # a soma
    E.formula_em(c, t, C["s11.a"], "40 + 30 = 70", 1380, 470, 72, "g", TINTA)
    E.formula_em(c, t, C["s11.b"], "70 + 4", 1380, 640, 72, "g", TINTA)
    igual_bola(c, t, C["s11.b"] + 0.4, 1640, 616, "74", r=80, cor=CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s12.a"], ps("garantir uma mulher e completar com qualquer um", "i", 56, TINTA2), W / 2, 270, "center", passo=0.09)
    xs = casinhas(c, t, 560, 470, [("mulher garantida", 4, C["s12.b"], C["s12.b"] + 0.2), ("2 entre as 8", 28, C["s12.b"] + 0.8, C["s12.b"] + 2.6)],
                  s=150, gap=200)
    igual_bola(c, t, C["s12.c"], xs[1] + 125, 470, "112", r=95, cor=ERRADO)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "mais que o total: 84!", 1500, 470, 52, estilo="g", fundo=ERRADO, a=a))
    # Ana, Bia e Caio contada duas vezes
    for i, (garantida, resto) in enumerate((("Ana", ("Bia", "Caio")), ("Bia", ("Ana", "Caio")))):
        y = 760 + i * 150
        t0 = C["s12.e"] + 0.5 * i

        def linha(a, garantida=garantida, resto=resto, y=y):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(220, y - 55, 300, 100), 50, 50)
            c.drawRRect(r, M.paint(MUL, a))
            E.centro(c, garantida, 370, y + 17, 50, "g", BR, a)
            E.escreve(c, "garantida", 545, y + 15, 46, "i", TINTA2, a)
            E.escreve(c, "+  " + resto[0] + ", " + resto[1], 780, y + 17, 52, "g", TINTA, a)
        E.foco(c, t, t0, 0.5, linha)
    E.foco(c, t, C["s12.e"] + 1.4, 0.5, lambda a: E.escreve(c, "mesma comissão, 2 vezes", 1150, 855, 52, "g", ERRADO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def conta():
        E.frase(c, t, C["s13.a"], [("conte", "i", 80, CLARO), ("tudo", "g", 84, BR), ("e", "i", 80, CLARO), ("tire", "i", 80, CLARO), ("o", "i", 80, CLARO),
                                   ("que", "i", 80, CLARO), ("não", "g", 84, BR), ("serve", "g", 84, BR)], W / 2, 190, "center", passo=0.12)
        E.formula_em(c, t, C["s13.a"] + 1.6, "tudo: 84", 260, 400, 84, "g", BR)
        E.frase(c, t, C["s13.b"], [("não", "i", 64, CLARO), ("serve:", "i", 64, CLARO), ("nenhuma", "g", 70, BR), ("mulher", "g", 70, BR)], 260, 560, passo=0.12)
        E.foco(c, t, C["s13.b"] + 0.9, 0.4, lambda a: E.escreve(c, "(só homens)", 1120, 560, 56, "i", CLARO, a))
        E.formula_em(c, t, C["s13.c"], "3 homens entre 5:", 260, 730, 64, "g", BR)
        E.formula_em(c, t, C["s13.c"] + 1.2, "f{5 × 4}{2} = 10", 920, 740, 76, "g", BR)
        E.formula_em(c, t, C["s13.d"], "84 − 10", 260, 940, 100, "g", BR)
        igual_bola(c, t, C["s13.d"] + 0.4, 700, 905, "74", r=90, cor=E.COR, escuro=True)
        E.foco(c, t, C["s13.d"] + 1.2, 0.5, lambda a: E.escreve(c, "em uma linha", 1000, 930, 60, "i", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, conta)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("cada comissão ou tem mulher, ou não tem", "i", 68, BR), W / 2, 190, "center", passo=0.1)
    x, w, y, h = 260, 1400, 280, 110
    p = ep(t, C["s14.a"] + 0.6, 0.6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w * 74 / 84 * p, h), 18, 18), M.paint(E.COR))
    p2 = ep(t, C["s14.a"] + 1.0, 0.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w * 74 / 84 + 8, y, (w * 10 / 84 - 8) * p2, h), 18, 18), M.paint(CLARO, 0.5))
    E.foco(c, t, C["s14.a"] + 0.9, 0.4, lambda a: E.centro(c, "com mulher: 74", x + w * 37 / 84, y + 74, 54, "g", BR, a))
    E.foco(c, t, C["s14.a"] + 1.3, 0.4, lambda a: E.centro(c, "10", x + w * 79 / 84, y + 74, 54, "g", BR, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "compensa: “pelo menos um”", W / 2, 540, 54, estilo="g", fundo=CERTO, a=a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "não compensa: “exatamente uma”", W / 2, 700, 54, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s14.d"], [("conte", "i", 64, CLARO), ("direto:", "i", 64, CLARO)], 330, 880)
    xs = casinhas(c, t, 1000, 870, [("mulher", 4, C["s14.d"] + 0.3, C["s14.d"] + 0.5), ("2 homens", 10, C["s14.d"] + 0.4, C["s14.d"] + 0.7)],
                  s=120, gap=80, escuro=True)
    igual_bola(c, t, C["s14.d"] + 1.0, xs[1] + 105, 870, "40", r=75, cor=E.COR, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s15.a"], [("4", "g", 84, COR), ("professores", "i", 76), ("e", "i", 76), ("6", "g", 84, COR), ("alunos", "i", 76)], XE, 350)
    E.frase(c, t, C["s15.b"], [("comissões", "i", 64), ("de", "i", 64), ("2", "g", 70, COR), ("professores", "i", 64)], XE, 520)
    E.frase(c, t, C["s15.b"] + 0.9, [("e", "i", 64), ("2", "g", 70, COR), ("alunos?", "g", 70)], XE, 610)
    E.frase(c, t, C["s15.c"], [("comissões", "i", 64), ("de", "i", 64), ("3", "g", 70, COR), ("com", "i", 64)], XE, 780)
    E.frase(c, t, C["s15.c"] + 0.9, [("pelo", "g", 70), ("menos", "g", 70), ("1", "g", 70, COR), ("professor?", "g", 70)], XE, 870)
    E.relogio(c, t, C["s16.a"], 1500, 560, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def etapas():
        E.foco(c, t, C["s17"] + 0.1, 0.5, lambda a: caixa(c, 200, 280, 680, 420, "professores", a, TINTA2))
        E.foco(c, t, C["s17"] + 0.3, 0.5, lambda a: caixa(c, 1040, 280, 680, 420, "alunos", a, TINTA2))
        E.foco(c, t, C["s17.a"], 0.4, lambda a: E.centro(c, "2 entre 4", 540, 400, 56, "g", TINTA2, a))
        E.formula_em(c, t, C["s17.a"] + 0.3, "f{4 × 3}{2}", 420, 570, 90, "g", TINTA, "center")
        igual_bola(c, t, C["s17.a"] + 1.4, 550, 545, "6", r=70)
        E.foco(c, t, C["s17.b"], 0.4, lambda a: E.centro(c, "2 entre 6", 1380, 400, 56, "g", TINTA2, a))
        E.formula_em(c, t, C["s17.b"] + 0.3, "f{6 × 5}{2}", 1260, 570, 90, "g", TINTA, "center")
        igual_bola(c, t, C["s17.b"] + 1.4, 1390, 545, "15", r=70)
        E.sinal(c, t, C["s17.c"] - 0.4, "×", 960, 490, 120, COR)
        E.formula_em(c, t, C["s17.c"], "6 × 15", 560, 900, 100, "g", TINTA)
        bx = igual_bola(c, t, C["s17.c"] + 0.4, 900, 865, "90", r=90, cor=CERTO)
        E.foco(c, t, C["s17.c"] + 0.7, 0.5, lambda a: E.escreve(c, "comissões", bx + 110, 890, 60, "g", CERTO, a))
    E.saida(c, t, C["s18"] - 0.1, etapas)
    if t < C["s18"]:
        return
    E.foco(c, t, C["s18"] + 0.1, 0.5, lambda a: E.pilula(c, "pelo menos 1 professor", W / 2, 160, 50, estilo="g", a=a))
    E.formula_em(c, t, C["s18.a"], "tudo: 3 entre 10", 220, 360, 64, "g", TINTA)
    E.formula_em(c, t, C["s18.a"] + 1.4, "f{10 × 9 × 8}{3!} = f{720}{6}", 820, 370, 80, "g", TINTA)
    igual_bola(c, t, C["s18.b"], 1490, 345, "120", r=85)
    E.formula_em(c, t, C["s18.c"], "nenhum professor: 3 entre 6", 220, 600, 56, "g", ERRADO)
    E.formula_em(c, t, C["s18.d"], "f{6 × 5 × 4}{6}", 1100, 610, 80, "g", TINTA)
    igual_bola(c, t, C["s18.d"] + 1.6, 1490, 585, "20", r=85, cor=ERRADO)
    E.formula_em(c, t, C["s18.e"], "120 − 20", 480, 900, 104, "g", TINTA)
    bx = igual_bola(c, t, C["s18.e"] + 0.4, 990, 865, "100", r=95, cor=CERTO)
    E.foco(c, t, C["s18.e"] + 1.4, 0.5, lambda a: E.escreve(c, "menor que o total", bx + 120, 890, 52, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s19.a", "grupos diferentes são etapas:", "multiplique as combinações"),
                                         ("s19.b", "pelo menos um?", "tudo menos o nenhum"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68), 400, y - 10, passo=0.1)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 88, COR)], 400, y + 95)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20"] + 0.6, [("praticar", "g", 100, COR), ("contagem", "g", 100, COR)], XE, 450)
    E.frase(c, t, C["s20.a"], [("multiplica,", "g", 60), ("permuta,", "g", 60), ("arranja", "g", 60), ("ou", "i", 60), ("combina?", "g", 60, COR)],
            XE, 590, passo=0.15)
    E.frase(c, t, C["s20.b"], ps("com regras no meio", "i", 72), XE, 720)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(620, 325, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, etapas=b_etapas, pelomenos=b_pelomenos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
