"""Visual — Estudativo · MAT-CNT-001: princípio multiplicativo e árvore de possibilidades.
Linguagem visual da trilha Contagem e Probabilidade (as próximas aulas copiam daqui):
- casinhas(): uma caixa branca por etapa, com o número de opções DENTRO (grande, na cor da matéria), o nome da etapa embaixo
  em itálico e o × entre as caixas. "?" em cinza = casinha ainda sem conta. No palco escuro, escuro=True.
  Cor "fixo" = algarismo já decidido (caixa cheia). Peças de restrição (marca, regra, ordem, nota) em MAT-CNT-002.
- igual_bola(): "=" e o resultado na esfera, à direita da conta.
- E.arvore para a árvore; os números de cada ponta (1 a 12) são contados aqui, por grupo.
- camisa(), calca(), tenis(): ícones das peças de roupa, com a cor real da peça.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-001_principio_multiplicativo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("arvore", "casinhas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 * 4 == 12 and 12 * 2 == 24 and 3 * 4 * 2 == 24 and 10 ** 4 == 10000 and 10 ** 6 == 1000000
assert 3 * 5 == 15 and 15 * 2 == 30 and 3 + 5 + 2 == 10 and 10 ** 3 == 1000 and 3 + 4 == 7

CAMISAS = (("branca", "#FFFFFF"), ("azul", "#4F8FE0"), ("preta", "#26262B"))
CALCAS = (("jeans", "#3E5F93"), ("cinza", "#9C9CA3"), ("bege", "#D8C29C"), ("verde", "#55895A"))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
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


def _forma(c, pts, cx, cy, k, cor, a, fecha=True):
    p = skia.Path()
    p.moveTo(cx + pts[0][0] * k, cy + pts[0][1] * k)
    for x, y in pts[1:]:
        p.lineTo(cx + x * k, cy + y * k)
    if fecha:
        p.close()
    c.drawPath(p, M.paint(cor, a))
    pt = M.paint(TINTA, a, stroke=max(2.5, 3.2 * k))
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def camisa(c, cx, cy, tam, cor, a=1.0):
    """camiseta de frente; tam = altura em px"""
    if a <= 0:
        return
    k = tam / 100
    _forma(c, [(-17, -50), (-50, -38), (-68, -6), (-48, 4), (-36, -14), (-36, 50), (36, 50), (36, -14), (48, 4), (68, -6), (50, -38),
               (17, -50), (9, -40), (0, -37), (-9, -40)], cx, cy, k, cor, a)


def calca(c, cx, cy, tam, cor, a=1.0):
    """calça de frente; tam = altura em px"""
    if a <= 0:
        return
    k = tam / 100
    _forma(c, [(-33, -50), (33, -50), (40, 50), (9, 50), (0, -12), (-9, 50), (-40, 50)], cx, cy, k, cor, a)
    M.line(c, cx - 33 * k, cy - 38 * k, cx + 34 * k, cy - 38 * k, TINTA, a, max(2.5, 3.2 * k))


def tenis(c, cx, cy, tam, cor, a=1.0):
    """tênis de lado; tam = largura em px"""
    if a <= 0:
        return
    k = tam / 100
    _forma(c, [(-50, 18), (-50, -8), (-28, -10), (-12, -30), (12, -30), (16, -12), (40, -4), (50, 8), (50, 18)], cx, cy, k, cor, a)
    _forma(c, [(-52, 18), (52, 18), (52, 28), (-52, 28)], cx, cy, k, BR, a)


def roupa(c, cx, cy, tam, i, j, a=1.0):
    """uma roupa completa: camisa i em cima da calça j"""
    calca(c, cx, cy + tam * 0.42, tam * 0.9, CALCAS[j][1], a)
    camisa(c, cx, cy - tam * 0.38, tam * 0.8, CAMISAS[i][1], a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def armario():
        for i, (nome, cor) in enumerate(CAMISAS):
            E.foco(c, t, C["s01.a"] + 0.15 * i, 0.5, lambda a, i=i, cor=cor: camisa(c, 290 + i * 215, 330, 150, cor, a))
        for j, (nome, cor) in enumerate(CALCAS):
            E.foco(c, t, C["s01.b"] + 0.15 * j, 0.5, lambda a, j=j, cor=cor: calca(c, 220 + j * 180, 640, 170, cor, a))
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: E.escreve(c, "3 camisas", 880, 350, 64, "i", TINTA, a))
        E.foco(c, t, C["s01.b"] + 0.4, 0.5, lambda a: E.escreve(c, "4 calças", 900, 660, 64, "i", TINTA, a))
        E.frase(c, t, C["s01.b"] + 1.4, ps("quantas roupas?", "i", 92) [:1] + [("roupas?", "g", 84, COR)], 560, 960, "center")
        x = 1500
        E.formula_em(c, t, C["s01.c"], "3 + 4 = 7", x, 500, 110, "g", ERRADO, "center")
        if t >= C["s01.d"] - 0.3:
            E.risco(c, x - 220, 460, x + 220, 460, t, C["s01.d"] - 0.3, largura=14)
            E.formula_em(c, t, C["s01.d"], "3 × 4", x - 180, 740, 120, "g", TINTA, "center")
            igual_bola(c, t, C["s01.d"] + 0.3, x + 50, 697, "12", r=100)
        E.foco(c, t, C["s01.c"] + 0.4, 0.4, lambda a: E.centro(c, "você somou", x, 360, 56, "i", ERRADO, a) if t < C["s01.d"] else None)
    E.saida(c, t, C["s02"] - 0.1, armario)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("contar", "g", 132)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("sem", "i", 120), ("listar", "g", 132)], XE, 630)
        E.frase(c, t, C["s02.b"], [("a", "i", 104), ("árvore", "g", 110, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), W / 2, 230, "center")
    for k, x, titulo, conta in (("s03.a", 220, "tabuada", "3 × 4 = 12"), ("s03.b", 1000, "potência", "10^4 = 10 · 10 · 10 · 10")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 360, 700, 400, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 96, COR)], x + 350, 500, "center")
        E.formula_em(c, t, C[k] + 0.5, conta, x + 350, 660, 64 if k == "s03.b" else 80, "g", TINTA, "center")
    # o expoente diz quantas vezes a base aparece
    E.foco(c, t, C["s03.b"] + 1.6, 0.5, lambda a: E.centro(c, "4 vezes o 10", 1350, 850, 52, "i", TINTA2, a))
    E.cursor(c, 1146, 672, ep(t, C["s03.b"] + 1.6, 0.4))


# ---------------- a árvore ----------------
NX, NY, NW, NH = 700, 110, 900, 880


def arvore(c, t, t0, niveis, tn, destaque=()):
    return E.arvore(c, t, t0, niveis, NX, NY, NW, NH, tn=tn, destaque=destaque, size=46)


def b_arvore(c, t, C, b):
    # s04 e s05: o armário e a camisa branca com as quatro calças
    def armario():
        E.frase(c, t, C["s04"], ps("vamos montar as roupas", "i", 84), W / 2, 190, "center")
        for i, (nome, cor) in enumerate(CAMISAS):
            x = 560 + i * 400
            E.foco(c, t, C["s04.a"] + 0.4 * i, 0.5, lambda a, x=x, cor=cor, nome=nome: (camisa(c, x, 360, 140, cor, a),
                                                                                       centro(c, nome, x, 490, 48, "i", TINTA2, a)))
        for j, (nome, cor) in enumerate(CALCAS):
            x = 360 + j * 400
            E.foco(c, t, C["s04.b"] + 0.4 * j, 0.5, lambda a, x=x, cor=cor, nome=nome: (calca(c, x, 750, 160, cor, a),
                                                                                       centro(c, nome, x, 890, 48, "i", TINTA2, a)))
        if t >= C["s05.a"]:
            p = ep(t, C["s05.a"], 0.5)
            E.caixa_pontilhada(c, 560 - 120, 270, 240, 250, p, prog_=p)
            for j in range(4):
                q = ease_io(prog(t, C["s05.b"] + 0.25 * j, 0.5))
                if q > 0:
                    M.line(c, 560, 530, 360 + j * 400, 660, COR, 1.0, 6, progress=q)
            E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "4 roupas só com a branca", W / 2, 990, 50, estilo="b", a=a))
    if t < C["s06.a"] + 0.4:
        E.saida(c, t, C["s06.a"] - 0.1, armario)
    if t < C["s06"]:
        return

    camisas = [n for n, _ in CAMISAS]
    calcas = [n for n, _ in CALCAS]
    grupo = None
    if C["s07.a"] <= t < C["s07.d"]:
        grupo = camisas[0] if t < C["s07.b"] else camisas[1] if t < C["s07.c"] else camisas[2]
    dest = tuple((grupo, k) for k in calcas) if grupo else ((("branca", "jeans"),) if C["s06.d"] <= t < C["s07"] else ())

    def primeira():
        pos = arvore(c, t, C["s06.a"], [camisas, calcas], [C["s06.b"], C["s06.c"]], dest)
        # o número de cada ponta, grupo por grupo
        for gi, (cam, k) in enumerate((("branca", "s07.a"), ("azul", "s07.b"), ("preta", "s07.c"))):
            for j, cal in enumerate(calcas):
                px, py = pos[(cam, cal)]
                n = gi * 4 + j + 1
                E.foco(c, t, C[k] + 0.12 * j, 0.35, lambda a, px=px, py=py, n=n, cal=cal: E.escreve(
                    c, str(n), px + E.larg(cal, "g", 46) / 2 + 36, py + 17, 46, "b", COR, a))
        if C["s06.d"] <= t < C["s07"]:
            px, py = pos[("branca", "jeans")]
            E.cursor(c, px + 90, py + 10, ep(t, C["s06.d"], 0.4))
    E.saida(c, t, C["s08.a"] - 0.1, primeira)

    def textos06():
        E.frase(c, t, C["s06.a"], [("uma", "i", 92), ("árvore", "g", 92, COR)], XE, 260)
        E.frase(c, t, C["s06.b"], [("3", "g", 80, COR), ("galhos:", "i", 72)], XE, 430)
        E.frase(c, t, C["s06.b"] + 0.4, ps("as camisas", "i", 64, TINTA2), XE, 510)
        E.frase(c, t, C["s06.c"], [("4", "g", 80, COR), ("galhos", "i", 72)], XE, 650)
        E.frase(c, t, C["s06.c"] + 0.4, ps("em cada camisa", "i", 64, TINTA2), XE, 730)
        E.frase(c, t, C["s06.d"], [("ponta", "g", 64, COR), ("=", "g", 60), ("roupa", "i", 70)], XE, 890)
    E.saida(c, t, C["s07"] - 0.1, textos06)

    def textos07():
        for i, (k, cam) in enumerate((("s07.a", "branca"), ("s07.b", "azul"), ("s07.c", "preta"))):
            E.frase(c, t, C[k], [("4", "g", 84, COR), ("com", "i", 72), ("a", "i", 72), (cam, "i", 72)], XE, 300 + i * 120)
        if t >= C["s07.d"]:
            E.formula_em(c, t, C["s07.d"], "3 × 4", XE, 760, 110, "g", TINTA)
            igual_bola(c, t, C["s07.d"] + 0.5, XE + 360, 722, "12", r=95)
    E.saida(c, t, C["s08"] - 0.1, textos07)

    if t >= C["s08"]:
        E.frase(c, t, C["s08"] + 0.2, ps("a ordem não muda o total", "i", 60, TINTA2), XE, 200)
        if t >= C["s08.a"]:
            arvore(c, t, C["s08.a"], [calcas, camisas], [C["s08.a"] + 0.5, C["s08.a"] + 1.4])
            E.frase(c, t, C["s08.a"], ps("começando pela", "i", 72), XE, 400)
            E.frase(c, t, C["s08.a"] + 0.4, [("calça", "g", 92, COR)], XE, 500)
            E.formula_em(c, t, C["s08.b"], "4 × 3", XE, 720, 110, "g", TINTA)
            igual_bola(c, t, C["s08.b"] + 0.5, XE + 360, 682, "12", r=95)
            E.frase(c, t, C["s08.b"] + 1.8, ps("muda o desenho,", "i", 56, TINTA2), XE, 880)
            E.frase(c, t, C["s08.b"] + 2.4, ps("não a conta", "i", 56, TINTA2), XE, 950)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    def regra():
        E.frase(c, t, C["s09.a"], [("princípio", "g", 104, COR), ("multiplicativo", "g", 104, COR)], W / 2, 250, "center")
        E.frase(c, t, C["s09.a"] + 1.4, ps("ou princípio fundamental da contagem", "i", 56, TINTA2), W / 2, 345, "center", passo=0.12)
        E.passo(c, t, C["s09.b"], 1, "a escolha é feita", "em etapas", 520)
        E.passo(c, t, C["s09.c"], 2, "você faz", "todas as etapas", 700)
        E.passo(c, t, C["s09.d"], 3, "então", "multiplique as opções", 880)
        # ao lado: as etapas da roupa
        E.foco(c, t, C["s09.b"] + 0.4, 0.5, lambda a: (camisa(c, 1240, 560, 120, CAMISAS[1][1], a), calca(c, 1540, 560, 130, CALCAS[0][1], a)))
        E.sinal(c, t, C["s09.d"] + 0.2, "×", 1390, 560, 90)
        E.foco(c, t, C["s09.c"] + 0.3, 0.5, lambda a: E.centro(c, "camisa e calça", 1390, 720, 52, "i", TINTA2, a))
    E.saida(c, t, C["s10"] - 0.1, regra)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"] + 0.1, [("por", "i", 80), ("que", "i", 80), ("multiplicar?", "g", 76, COR)], W / 2, 190, "center")
    # cada camisa combina com todas as calças
    E.foco(c, t, C["s10.a"], 0.5, lambda a: camisa(c, 330, 560, 150, CAMISAS[0][1], a))
    for j in range(4):
        y = 330 + j * 155
        q = ease_io(prog(t, C["s10.a"] + 0.6 + 0.2 * j, 0.45))
        if q > 0:
            M.line(c, 420, 560, 600, y, TINTA2, 1.0, 5, progress=q)
        E.foco(c, t, C["s10.a"] + 0.9 + 0.2 * j, 0.4, lambda a, y=y, j=j: calca(c, 660, y, 115, CALCAS[j][1], a))
    E.foco(c, t, C["s10.a"] + 1.8, 0.5, lambda a: E.centro(c, "com todas", 480, 1000, 50, "i", TINTA2, a))
    # mais um andar: cada roupa vira duas
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (tenis(c, 1060, 330, 150, "#E8E8EA", a), tenis(c, 1260, 330, 150, "#C2463A", a)))
    E.foco(c, t, C["s10.b"] + 0.4, 0.5, lambda a: E.centro(c, "2 pares de tênis", 1160, 450, 50, "i", TINTA2, a))
    if t >= C["s10.c"]:
        E.foco(c, t, C["s10.c"], 0.5, lambda a: roupa(c, 1100, 680, 150, 0, 0, a))
        for k, (dy, cor) in enumerate(((-90, "#E8E8EA"), (90, "#C2463A"))):
            q = ease_io(prog(t, C["s10.c"] + 0.5 + 0.2 * k, 0.45))
            if q > 0:
                M.line(c, 1200, 680, 1380, 680 + dy, TINTA2, 1.0, 5, progress=q)
            E.foco(c, t, C["s10.c"] + 0.8 + 0.2 * k, 0.4, lambda a, dy=dy, cor=cor: tenis(c, 1480, 680 + dy, 150, cor, a))
        E.foco(c, t, C["s10.c"] + 1.3, 0.5, lambda a: E.centro(c, "cada roupa vira duas", 1290, 880, 50, "i", TINTA2, a))
    if t >= C["s10.d"]:
        E.formula_em(c, t, C["s10.d"], "12 × 2", 1290, 1010, 92, "g", TINTA, "right")
        E.sinal(c, t, C["s10.d"] + 0.3, "=", 1350, 978, 80)
        E.foco(c, t, C["s10.d"] + 0.5, 0.5, lambda a: E.escreve(c, "24", 1405, 1010, 92, "g", COR, a))


# ---------------- casinhas ----------------
def b_casinhas(c, t, C, b):
    E.frase(c, t, C["s11"] + 0.1, [("na", "i", 84), ("prova:", "i", 84), ("casinhas", "g", 84, COR)], W / 2, 200, "center")
    y = 560
    ta = C["s11.a"]
    xs = casinhas(c, t, 820, y, [("camisa", 3, ta, C["s11.c"]), ("calça", 4, ta + 0.25, C["s11.d"]), ("tênis", 2, ta + 0.5, C["s11.e"])], s=210,
                  tx=[C["s11.f"], C["s11.f"] + 0.3])
    # ícones em cima de cada casinha
    E.foco(c, t, ta + 0.2, 0.5, lambda a: camisa(c, xs[0], y - 200, 110, CAMISAS[1][1], a))
    E.foco(c, t, ta + 0.45, 0.5, lambda a: calca(c, xs[1], y - 200, 120, CALCAS[0][1], a))
    E.foco(c, t, ta + 0.7, 0.5, lambda a: tenis(c, xs[2], y - 200, 130, "#C2463A", a))
    # escreva dentro quantas opções
    p = ease_io(prog(t, C["s11.b"], 0.6))
    if C["s11.b"] <= t < C["s11.f"]:
        E.cursor(c, lerp(1500, xs[0] + 40, p), lerp(900, y + 30, p), ep(t, C["s11.b"], 0.4))
    E.foco(c, t, C["s11.b"] + 0.3, 0.5, lambda a: E.centro(c, "quantas opções?", 820, 920, 60, "i", TINTA2, a) if t < C["s11.f"] else None)
    igual_bola(c, t, C["s11.f"] + 0.7, xs[2] + 200, y, "24", r=120)


# ---------------- senha ----------------
def b_senha(c, t, C, b):
    def apresenta():
        E.frase(c, t, C["s12"] + 0.1, [("senha", "i", 84), ("de", "i", 84), ("4", "g", 84, COR), ("dígitos", "g", 84, COR)], W / 2, 200, "center")
        # visor da senha
        E.foco(c, t, C["s12.a"], 0.5, lambda a: M.rrect(c, 560, 290, 800, 190, 40, TINTA, a))
        for i in range(4):
            x = 680 + i * 186
            pin = "7737"[i]
            if t < C["s12.c"]:
                E.foco(c, t, C["s12.a"] + 0.3 + 0.15 * i, 0.3, lambda a, x=x: c.drawCircle(x, 385, 26, M.paint(BR, a)))
            else:
                E.foco(c, t, C["s12.c"] + 0.15 * i, 0.4, lambda a, x=x, pin=pin: centro(c, pin, x, 420, 110, "g", CLARO if pin == "7" else BR, a))
        # os dez algarismos
        for d in range(10):
            x = 330 + d * 140
            E.foco(c, t, C["s12.b"] + 0.08 * d, 0.4, lambda a, x=x, d=d: centro(c, str(d), x, 700, 96, "g", COR, a))
        if t >= C["s12.b"] + 0.9:
            E.chave(c, 290, 1630, 740, TINTA2, ep(t, C["s12.b"] + 0.9, 0.5))
        E.foco(c, t, C["s12.b"] + 1.2, 0.5, lambda a: E.pilula(c, "10 algarismos", 960, 850, 56, estilo="b", a=a))
        E.foco(c, t, C["s12.c"] + 0.6, 0.5, lambda a: E.pilula(c, "pode repetir", 1600, 300, 50, estilo="b", fundo=TINTA2, a=a))
    E.saida(c, t, C["s13"] - 0.1, apresenta)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"] + 0.1, [("4", "g", 84, COR), ("casinhas", "i", 84)], W / 2, 200, "center")
    tb = C["s13.a"]
    xs = casinhas(c, t, 760, 520, [(f"{i + 1}º dígito", 10, tb + 0.2 * i, C["s13.b"] + 0.25 * i) for i in range(4)], s=190,
                  tx=[C["s13.c"] + 0.4 * i for i in range(3)])
    E.foco(c, t, C["s13.b"] + 1.4, 0.5, lambda a: E.centro(c, "repete: nenhuma casinha perde opção", 760, 810, 52, "i", TINTA2, a))
    bx = igual_bola(c, t, C["s13.d"], xs[3] + 180, 520, "10.000", r=150, size=72)
    E.frase(c, t, C["s13.d"] + 0.4, [("senhas", "g", 72, COR)], bx, 760, "center")


# ---------------- erro ----------------
def mini_arvore(c, t, t0, x, y, w, h, n1, n2):
    """árvore sem rótulos: raiz, n1 galhos e n2 em cada um; as pontas acendem uma a uma"""
    rx, ry = x, y + h / 2
    folhas = n1 * n2
    for i in range(n1):
        my = y + h * (i * n2 + n2 / 2) / folhas
        q = ease_io(prog(t, t0 + 0.2, 0.5))
        if q > 0:
            M.line(c, rx, ry, x + w * 0.45, my, TINTA2, 1.0, 5, progress=q)
        for j in range(n2):
            k = i * n2 + j
            fy = y + h * (k + 0.5) / folhas
            q2 = ease_io(prog(t, t0 + 0.8, 0.5))
            if q2 > 0:
                M.line(c, x + w * 0.45, my, x + w * 0.9, fy, TINTA2, 1.0, 4, progress=q2)
            E.foco(c, t, t0 + 1.4 + 0.08 * k, 0.3, lambda a, fy=fy: c.drawCircle(x + w * 0.9 + 4, fy, 12, M.paint(COR, a)))
    k = ease_back(prog(t, t0, 0.35))
    if k > 0:
        c.drawCircle(rx, ry, 11 * k, M.paint(TINTA))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 180, "center")
    x = 560
    E.formula_em(c, t, C["s14.a"], "3 + 4 = 7", x, 380, 120, "g", ERRADO, "center")
    if t >= C["s14.d"] - 0.3:
        E.risco(c, x - 250, 330, x + 250, 330, t, C["s14.d"] - 0.3, largura=14)

    def pecas():
        for i in range(3):
            E.foco(c, t, C["s14.b"] + 0.1 * i, 0.4, lambda a, i=i: camisa(c, 180 + i * 150, 640, 110, CAMISAS[i][1], a))
        for j in range(4):
            E.foco(c, t, C["s14.b"] + 0.3 + 0.1 * j, 0.4, lambda a, j=j: calca(c, 640 + j * 130, 640, 120, CALCAS[j][1], a))
        E.foco(c, t, C["s14.b"] + 0.9, 0.5, lambda a: E.centro(c, "7 peças no armário", x, 830, 60, "i", TINTA, a))
    E.saida(c, t, C["s14.c"] - 0.1, pecas)
    if t >= C["s14.c"]:
        E.foco(c, t, C["s14.c"], 0.5, lambda a: roupa(c, x, 660, 200, 1, 2, a))
        E.foco(c, t, C["s14.c"] + 0.5, 0.5, lambda a: E.centro(c, "1 camisa e 1 calça juntas", x, 960, 56, "i", TINTA, a))
    if t >= C["s14.d"]:
        E.formula_em(c, t, C["s14.d"], "3 × 4 = 12", 1400, 380, 120, "g", CERTO, "center")
        mini_arvore(c, t, C["s14.d"] + 0.6, 1150, 470, 520, 500, 3, 4)
        E.foco(c, t, C["s14.d"] + 3.2, 0.5, lambda a: E.escreve(c, "12 pontas", 1530, 1040, 56, "b", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def potencia():
        E.frase(c, t, C["s15.a"], [("casinhas", "i", 92, CLARO), ("iguais", "g", 92, BR), ("viram", "i", 92, CLARO), ("potência", "g", 92, BR)],
                W / 2, 190, "center")
        y = 540
        xs = casinhas(c, t, 760, y, [("", 10, C["s15.a"] + 0.8 + 0.2 * i, C["s15.a"] + 1.0 + 0.2 * i) for i in range(4)], s=170, escuro=True)
        E.sinal(c, t, C["s15.b"] - 0.2, "=", 1430, y, 110, BR)
        fx, fy, fs = 1520, y + 54, 150
        E.formula_em(c, t, C["s15.b"], "10^4", fx, fy, fs, "g", BR)
        wb = E.formula(None, "10", 0, 0, fs, a=0)
        we = E.formula(None, "4", 0, 0, fs * 0.58, a=0)
        # base: o número de dentro de cada casinha
        if t >= C["s15.c"]:
            p = ep(t, C["s15.c"], 0.5)
            E.caixa_pontilhada(c, fx - 14, fy - fs * 0.78, wb + 22, fs * 0.92, p, CLARO, p)
            for x in xs:
                M.line(c, x - 50, y + 62, x + 50, y + 62, CLARO, p, 5)
            E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "base: opções em cada casinha", 760, 780, 48, estilo="b", fundo=E.COR, a=a))
        # expoente: quantas casinhas
        if t >= C["s15.d"]:
            p = ep(t, C["s15.d"], 0.5)
            E.chave(c, xs[0] - 85, xs[3] + 85, 425, CLARO, p, -22)
            E.caixa_pontilhada(c, fx + wb - 4, fy - fs * 0.42 - fs * 0.58 * 0.8, we + 18, fs * 0.58 * 0.95, p, CLARO, p)
            E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "expoente: quantas casinhas", 760, 330, 48, estilo="b", fundo=E.COR, a=a))
    E.saida(c, t, C["s16"] - 0.1, potencia)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("potência é multiplicação repetida", "i", 80, CLARO), W / 2, 200, "center", passo=0.15)

    def seis():
        E.frase(c, t, C["s16.a"] + 1.4, ps("senha de 6 dígitos", "i", 64, CLARO), W / 2, 360, "center")
        E.formula_em(c, t, C["s16.b"], "10^6 = 1.000.000", W / 2, 560, 150, "g", BR, "center")
    E.saida(c, t, C["s16.c"] - 0.1, seis)
    if t >= C["s16.c"]:
        E.frase(c, t, C["s16.c"], [("casinhas", "i", 72, CLARO), ("diferentes:", "g", 72, BR)], W / 2, 380, "center")
        xs = casinhas(c, t, 640, 640, [("camisa", 3, C["s16.c"] + 0.4, C["s16.c"] + 0.6), ("calça", 4, C["s16.c"] + 0.7, C["s16.c"] + 0.9)],
                      s=170, escuro=True, tx=[C["s16.d"]])
        E.foco(c, t, C["s16.c"] + 1.0, 0.5, lambda a: E.pilula(c, "sem potência", 1300, 520, 50, estilo="b", fundo=ERRADO, a=a))
        E.foco(c, t, C["s16.d"], 0.5, lambda a: E.escreve(c, "um por um", 1130, 700, 72, "i", CLARO, a))
        E.formula_em(c, t, C["s16.d"] + 0.4, "= 12", 1130, 820, 96, "g", BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    linhas = (("s17.a", "um", "pão", "3 tipos", 300), ("s17.b", "um", "recheio", "5", 400), ("s17.c", "uma", "bebida", "2", 500))
    E.foco(c, t, C["s17.a"] - 0.4, 0.5, lambda a: (E.bola(c, XE + 36, 300, 36, a=a), centro(c, "1", XE + 36, 316, 44, "g", BR, a)))
    for k, art, nome, op, y in linhas:
        E.frase(c, t, C[k], [(art, "i", 64), (nome, "g", 64)], XE + 100, y + 20)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, op=op, y=y: E.escreve(c, "entre " + op, XE + 520, y + 20, 60, "i", TINTA2, a))
    E.frase(c, t, C["s17.d"], [("quantos", "i", 70), ("combos?", "g", 70, COR)], XE + 100, 610)
    E.foco(c, t, C["s17.e"] - 0.3, 0.5, lambda a: (E.bola(c, XE + 36, 740, 36, a=a), centro(c, "2", XE + 36, 756, 44, "g", BR, a)))
    E.frase(c, t, C["s17.e"], [("cadeado:", "g", 64), ("3", "g", 64, COR), ("rodinhas,", "i", 64)], XE + 100, 760)
    E.frase(c, t, C["s17.e"] + 0.9, ps("cada uma de 0 a 9", "i", 60, TINTA2), XE + 100, 840)
    E.frase(c, t, C["s17.f"], [("quantos", "i", 70), ("códigos?", "g", 70, COR)], XE + 100, 940)
    # cadeado
    E.foco(c, t, C["s17.e"] + 0.4, 0.5, lambda a: cadeado(c, 1150, 760, a, "000"))
    E.relogio(c, t, C["s18.a"], 1530, 400, 190)


def cadeado(c, cx, cy, a, cod):
    """cadeado de rodinhas: corpo, alça e três janelas"""
    if a <= 0:
        return
    E.arco(c, cx, cy - 100, 90, 180, 180, TINTA2, 22, a)
    for x in (cx - 90, cx + 90):
        M.line(c, x, cy - 100, x, cy - 60, TINTA2, a, 22, cap_round=False)
    M.rrect(c, cx - 150, cy - 70, 300, 210, 30, TINTA, a)
    for i, ch in enumerate(cod):
        x = cx - 90 + i * 90
        M.rrect(c, x - 34, cy - 20, 68, 100, 12, BR, a)
        centro(c, ch, x, cy + 52, 64, "g", TINTA, a)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def combo():
        y = 400
        t0 = C["s19"] + 0.6
        xs = casinhas(c, t, 700, y, [("pão", 3, t0, t0 + 0.6), ("recheio", 5, t0 + 0.2, t0 + 0.8), ("bebida", 2, t0 + 0.4, t0 + 1.0)], s=180)
        E.formula_em(c, t, C["s19.a"], "3 × 5 = 15", 330, 760, 96, "g", TINTA)
        E.formula_em(c, t, C["s19.b"], "15 × 2", 330, 900, 96, "g", TINTA)
        igual_bola(c, t, C["s19.b"] + 0.4, 650, 868, "30", r=95)
        E.foco(c, t, C["s19.b"] + 0.8, 0.5, lambda a: E.escreve(c, "combos", 915, 895, 64, "i", COR, a))
        E.formula_em(c, t, C["s19.c"], "3 + 5 + 2 = 10", 1500, 400, 96, "g", ERRADO, "center")
        if t >= C["s19.c"] + 0.6:
            E.risco(c, 1180, 360, 1820, 360, t, C["s19.c"] + 0.6, largura=12)
        E.foco(c, t, C["s19.c"] + 1.0, 0.5, lambda a: E.centro(c, "só os itens do cardápio", 1500, 520, 54, "i", TINTA2, a))
    E.saida(c, t, C["s20"] - 0.1, combo)
    if t < C["s20"]:
        return
    y = 420
    ta = C["s20.a"]
    xs = casinhas(c, t, 720, y, [(f"rodinha {i + 1}", 10, ta + 0.2 * i, ta + 0.4 + 0.2 * i) for i in range(3)], s=180)
    E.sinal(c, t, C["s20.b"] - 0.2, "=", 1250, y, 110)
    E.formula_em(c, t, C["s20.b"], "10^3", 1330, y + 50, 140, "g", TINTA)
    E.foco(c, t, C["s20.b"] + 0.5, 0.5, lambda a: (E.bola(c, 1350, 770, 130, a=a), centro(c, "1.000", 1350, 795, 70, "g", BR, a)))
    E.foco(c, t, C["s20.b"] + 0.8, 0.5, lambda a: E.escreve(c, "códigos", 1510, 795, 64, "i", COR, a))
    cod = "000" if t < C["s20.c"] + 0.8 else "999"
    E.foco(c, t, C["s20.c"], 0.5, lambda a: cadeado(c, 560, 870, a, cod))
    E.foco(c, t, C["s20.c"] + 0.3, 0.5, lambda a: E.escreve(c, "000 até 999", 760, 910, 64, "b", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s21.a", "escolha em etapas, faz todas?", "multiplique"), ("s21.b", "casinhas iguais?", "potência"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72), 400, y - 10)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 100, COR)], 400, y + 95)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("casinhas", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s22.a"] + 0.3, [("com", "i", 130), ("regras", "g", 140, COR)], XE, 600)
    E.frase(c, t, C["s22.b"], [("por", "i", 72), ("qual", "i", 72), ("começar?", "g", 64)], XE, 730)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, arvore=b_arvore, regra=b_regra, casinhas=b_casinhas, senha=b_senha, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
