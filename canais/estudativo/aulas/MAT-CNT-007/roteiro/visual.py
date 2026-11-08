"""Visual — Estudativo · MAT-CNT-007: arranjo, quando a ordem importa.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 006): casinhas() com o número de opções dentro e a etapa embaixo,
"?" em cinza, × entre elas, igual_bola() com o resultado na esfera; regra() = pílula da restrição; ordem() = esfera com a ordem.
Peças vindas da MAT-CNT-005: pessoa() e bloco(). Da MAT-CNT-004: fracao_corte() (o corte de fatoriais).
Peças desta aula:
- podio(): três degraus (prata, ouro, bronze) com a medalha; quem(): corredores em cima, trocando de degrau em arco.
- corredores(): a fila dos oito, com quem fica fora do pódio esmaecendo.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-007_arranjo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("podio", "troca", "regra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F = math.factorial
assert F(8) == 40320 and 8 * 7 == 56 and 56 * 6 == 336 and F(8) // F(5) == 336 and F(8) // F(6) == 56 and F(0) == 1
assert 10 * 9 == 90 and 90 * 8 == 720 and F(10) // F(7) == 720 and 336 // F(3) == 56
from itertools import permutations
assert sum(1 for _ in permutations(range(8), 3)) == 336 and sum(1 for _ in permutations(range(10), 3)) == 720

GENTE = ["#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A", "#9C9CA3", "#3FA7A0", "#B58A2E"]
PESSOAS = {"Ana": GENTE[0], "Bia": GENTE[1], "Caio": GENTE[2]}
MEDALHA = {1: "#E2B33C", 2: "#A7ADB8", 3: "#C27A3E"}


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


# ---------------- peças desta aula ----------------
DEGRAU = {2: (-1, 0.62), 1: (0, 1.0), 3: (1, 0.42)}  # lugar: (coluna, altura relativa)


def podio(c, cx, base, w, h, a=1.0, nomes=True):
    """três degraus: prata à esquerda, ouro no meio (mais alto), bronze à direita. base = chão. Devolve {lugar: (x, topo)}"""
    topo = {}
    for lugar, (col, k) in DEGRAU.items():
        x = cx + col * w
        hh = h * k
        topo[lugar] = (x, base - hh)
        if a <= 0:
            continue
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2 + 4, base - hh, w - 8, hh), 14, 14)
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
        c.save(); c.translate(0, 8); c.drawRRect(r, sh); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(TINTA, a, stroke=5))
        rm = min(w * 0.2, hh * 0.32)
        my = base - hh + rm + 18
        c.drawCircle(x, my, rm, M.paint(MEDALHA[lugar], a))
        centro(c, str(lugar), x, my + rm * 0.42, rm * 1.15, "g", BR, a)
        if nomes and hh > rm * 2 + 90:
            centro(c, ("", "ouro", "prata", "bronze")[lugar], x, base - 26, max(40, w * 0.15), "i", TINTA2, a)
    return topo


def no_podio(c, t, topo, quem, trocas, h, a=1.0, nome_size=None):
    """corredores em cima dos degraus. quem = {lugar: nome}; trocas = [(t0, {lugar: nome})]: quem muda de degrau vai em arco"""
    ant, cur, q = quem, quem, 1.0
    for ti, nova in trocas:
        if t >= ti:
            ant, cur = cur, nova
            q = ease_io(prog(t, ti, 0.9))
    onde0 = {n: l for l, n in ant.items()}
    for lugar, nome in cur.items():
        x1, y1 = topo[lugar]
        x0, y0 = topo[onde0[nome]]
        x = lerp(x0, x1, q)
        y = lerp(y0, y1, q) - math.sin(math.pi * q) * h * 0.5 * (1 if lugar != onde0[nome] else 0)
        pessoa(c, x, y - h * 0.38, h, PESSOAS.get(nome, GENTE[5]), None, a)
        centro(c, nome, x, y - h * 1.02, nome_size or max(42, h * 0.3), "b", TINTA, a)


def corredores(c, t, t0, cx, y, passo, h, fora=None, tfora=None, nomes=False):
    """a fila dos oito; fora = índices que esmaecem a partir de tfora"""
    for i in range(8):
        x = cx + (i - 3.5) * passo
        k = 1.0
        if fora and i in fora and tfora is not None:
            k = 1 - 0.75 * ep(t, tfora, 0.6)
        E.foco(c, t, t0 + 0.07 * i, 0.4, lambda a, i=i, x=x, k=k: pessoa(c, x, y, h, GENTE[i], None, a * k))
        if nomes:
            E.foco(c, t, t0 + 0.07 * i + 0.2, 0.4, lambda a, i=i, x=x, k=k: centro(c, f"{i + 1}º", x, y + h * 0.38 + 60, 44, "b", TINTA2, a * k))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.frase(c, t, C["s01.a"], [("8", "g", 84, COR), ("corredores", "i", 84), ("na", "i", 84), ("final", "g", 84)], W / 2, 180, "center")
        corredores(c, t, C["s01.a"] + 0.3, W / 2, 330, 150, 130)
        pa = ep(t, C["s01.b"], 0.5)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: podio(c, 560, 860, 200, 300, a))
        E.frase(c, t, C["s01.b"] + 0.3, [("ouro,", "g", 60, MEDALHA[1]), ("prata", "g", 60, TINTA2), ("e", "i", 60), ("bronze", "g", 60, MEDALHA[3])],
                560, 960, "center")
        E.formula_em(c, t, C["s01.c"], "8! = 40.320", 1000, 600, 100, "g", ERRADO)
        if t >= C["s01.c"] + 0.8:
            E.risco(c, 980, 565, 1680, 565, t, C["s01.c"] + 0.8, largura=12)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "são", 1000, 840, 90, "i", TINTA, a))
        E.foco(c, t, C["s01.d"] + 0.2, 0.5, lambda a: (E.bola(c, 1330, 810, 120, a=a), centro(c, "336", 1330, 810 + 34, 92, "g", BR, a)))
        E.foco(c, t, C["s01.d"] + 0.5, 0.5, lambda a: E.escreve(c, "pódios", 1480, 840, 72, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("quando", "i", 120), ("a", "i", 120)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("ordem", "g", 132, COR), ("importa", "g", 132)], XE, 630)
        E.frase(c, t, C["s02.b"], [("o", "i", 84), ("teste", "i", 84), ("da", "i", 84), ("troca", "g", 90, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.a", 110, "casinhas"), ("s03.b", 680, "fatorial"), ("s03.c", 1250, "corte")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 560, 640, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 280, 390, "center")
    casinhas(c, t, 390, 600, [("", 3, C["s03.a"] + 0.3, C["s03.a"] + 0.6), ("", 4, C["s03.a"] + 0.4, C["s03.a"] + 0.7),
                              ("", 2, C["s03.a"] + 0.5, C["s03.a"] + 0.8)], s=110, gap=56)
    E.foco(c, t, C["s03.a"] + 1.0, 0.4, lambda a: E.centro(c, "uma por etapa", 390, 760, 46, "i", TINTA2, a))
    E.formula_em(c, t, C["s03.b"] + 0.3, "4! = 4 × 3 × 2 × 1", 960, 610, 58, "g", TINTA, "center")
    E.foco(c, t, C["s03.b"] + 0.7, 0.4, lambda a: E.centro(c, "desce até o 1", 960, 760, 46, "i", TINTA2, a))
    # 8!/6! = 8 × 7 × 6!/6! = 56
    tc = lerp(C["s03.c"], C["s03.end"], 0.45)
    fracao_corte(c, t, C["s03.c"] + 0.4, 1530, 560, 64, ["8", "×", "7", "×", "6!"], "6!", tc=tc, cortar=(4,))
    E.formula_em(c, t, tc + 0.6, "8 × 7 = 56", 1530, 790, 64, "g", COR, "center")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.82), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- pódio ----------------
NOMES3 = ("ouro", "prata", "bronze")
CXP, YP, SP, GP = 760, 560, 200, 150


def b_podio(c, t, C, b):
    def contas():
        E.frase(c, t, C["s04"] + 0.1, [("uma", "i", 80), ("casinha", "i", 80), ("por", "i", 80), ("lugar", "g", 84, COR)], W / 2, 180, "center")
        tv = (C["s04.b"], C["s04.c"], C["s04.d"])
        xs = casinhas(c, t, CXP, YP, [(n_, v, C["s04.a"] + 0.15 * i, tv[i]) for i, (n_, v) in enumerate(zip(NOMES3, (8, 7, 6)))], s=SP, gap=GP,
                      tx=[C["s05.a"], C["s05.b"]])
        for i in range(3):
            E.foco(c, t, C["s04.a"] + 0.15 * i + 0.2, 0.4, lambda a, i=i: (c.drawCircle(xs[i] - SP / 2 + 6, YP - SP / 2 + 6, 30, M.paint(MEDALHA[i + 1], a)),
                                                                     centro(c, str(i + 1), xs[i] - SP / 2 + 6, YP - SP / 2 + 19, 36, "g", BR, a)))
        ks = (("s04.b", "s04.c"), ("s04.c", "s04.d"), ("s04.d", "s05"))
        for i, (k0, k1) in enumerate(ks):
            marca(c, t, C[k0], xs[i], YP, SP, C[k1] - 0.2, COR)
        yr = YP - SP / 2 - 70
        regra(c, t, C["s04.b"] + 0.3, xs[0], yr, "qualquer um", size=34)
        regra(c, t, C["s04.c"] + 0.3, xs[1], yr, "sem o do ouro", size=34)
        regra(c, t, C["s04.d"] + 0.3, xs[2], yr, "sem os 2 de cima", size=34)
        E.formula_em(c, t, C["s05.a"], "8 × 7 = 56", 300, 930, 96, "g", TINTA)
        E.formula_em(c, t, C["s05.b"], "56 × 6", 900, 930, 96, "g", TINTA)
        bx = igual_bola(c, t, C["s05.b"] + 0.5, 1240, 896, "336", r=110)
        E.foco(c, t, C["s05.b"] + 0.9, 0.5, lambda a: E.escreve(c, "pódios", bx + 135, 918, 64, "g", COR, a))
    E.saida(c, t, C["s06"] - 0.1, contas)
    if t < C["s06"]:
        return
    # a mesma conta da fila, que para no meio
    E.frase(c, t, C["s06.a"], [("fila", "g", 72, COR), ("dos", "i", 72), ("8:", "i", 72), ("desce", "i", 72), ("até", "i", 72), ("o", "i", 72), ("1", "g", 72)],
            W / 2, 200, "center")
    s, g, y = 130, 56, 470
    xs = [W / 2 + (i - 3.5) * (s + g) for i in range(8)]
    casinhas(c, t, (xs[0] + xs[2]) / 2, y, [("", v, C["s06.a"] + 0.08 * i, C["s06.a"] + 0.3 + 0.08 * i) for i, v in enumerate((8, 7, 6))], s=s, gap=g)

    def resto():
        casinhas(c, t, (xs[3] + xs[7]) / 2, y, [("", v, C["s06.a"] + 0.08 * (i + 3), C["s06.a"] + 0.3 + 0.08 * (i + 3)) for i, v in enumerate((5, 4, 3, 2, 1))],
                 s=s, gap=g)
        E.sinal(c, t, C["s06.a"] + 0.3, "×", (xs[2] + xs[3]) / 2, y, s * 0.42)
    k = 1 - 0.78 * ep(t, C["s06.c"] + 0.4, 0.6)
    if k < 1:
        pt = skia.Paint(); pt.setAlphaf(k)
        c.saveLayer(None, pt); resto(); c.restore()
    else:
        resto()
    if t >= C["s06.b"]:
        xc = (xs[2] + xs[3]) / 2
        p = ease_io(prog(t, C["s06.b"], 0.5))
        pt = M.paint(COR, 1, stroke=7); pt.setPathEffect(skia.DashPathEffect.Make([20, 14], 0))
        c.drawLine(xc, y - 130, xc, y - 130 + 260 * p, pt)
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: E.pilula(c, "para no meio", xc, y - 175, 46, estilo="g", a=a))
    if t >= C["s06.c"]:
        E.chave(c, xs[0] - s / 2, xs[2] + s / 2, y + s / 2 + 30, COR, ep(t, C["s06.c"], 0.5))
        E.frase(c, t, C["s06.c"] + 0.3, [("pódio:", "g", 64, COR), ("só", "i", 64), ("3", "g", 64, COR), ("sobem", "i", 64)], (xs[0] + xs[2]) / 2, y + 200, "center")
    E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "só 3 casinhas", (xs[0] + xs[2]) / 2, 880, 64, estilo="g", a=a))


# ---------------- o teste da troca ----------------
def b_troca(c, t, C, b):
    BASE = 970
    ANTES = {1: "Ana", 2: "Bia", 3: "Caio"}
    DEPOIS = {1: "Bia", 2: "Ana", 3: "Caio"}

    def um_podio():
        E.frase(c, t, C["s07"] + 0.1, [("a", "i", 80), ("ordem", "g", 84, COR), ("importa?", "g", 84)], W / 2, 180, "center")
        E.foco(c, t, C["s07.a"], 0.5, lambda a: E.pilula(c, "o teste da troca", W / 2, 290, 56, estilo="g", a=a))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: podio(c, W / 2, BASE, 300, 330, a))
        topo = podio(c, W / 2, BASE, 300, 330, 0)
        E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: no_podio(c, t, topo, ANTES, [(C["s07.c"] + 0.2, DEPOIS)], 170, a))
        if t >= C["s07.c"]:
            E.foco(c, t, C["s07.c"], 0.4, lambda a: E.centro(c, "troque!", W / 2 - 520, 560, 72, "g", COR, a))
    E.saida(c, t, C["s08"] - 0.1, um_podio)
    if t < C["s08"]:
        return

    def dois():
        for i, (quem, x) in enumerate(((ANTES, 520), (DEPOIS, 1400))):
            E.foco(c, t, C["s08"] + 0.1 + 0.3 * i, 0.5, lambda a, quem=quem, x=x: (podio(c, x, 720, 190, 230, a, nomes=False),
                                                                             no_podio(c, t, podio(c, x, 720, 190, 230, 0), quem, [], 120, a, 44)))
        E.sinal(c, t, C["s08.a"], "≠", W / 2, 560, 150, ERRADO)
        E.foco(c, t, C["s08.a"] + 0.2, 0.5, lambda a: E.centro(c, "outro pódio", W / 2, 230, 84, "g", COR, a))
        E.frase(c, t, C["s08.b"], ps("trocar a ordem mudou o resultado", "i", 64), W / 2, 870, "center", passo=0.12)
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "a ordem importa", W / 2, 990, 64, estilo="g", fundo=CERTO, a=a))
    E.saida(c, t, C["s09"] - 0.1, dois)
    if t < C["s09"]:
        return
    # outra situação: os 3 primeiros ganham vaga
    E.frase(c, t, C["s09.a"], [("os", "i", 72), ("3", "g", 72, COR), ("primeiros", "i", 72), ("ganham", "i", 72), ("vaga", "g", 72)], W / 2, 190, "center")
    y = 500
    for j, (ordem_, x) in enumerate(((("Ana", "Bia", "Caio"), 520), (("Bia", "Ana", "Caio"), 1400))):
        t0 = C["s09.a"] + 1.2 + 0.8 * j
        for i, nome in enumerate(ordem_):
            E.foco(c, t, t0 + 0.12 * i, 0.4, lambda a, nome=nome, i=i, x=x: pessoa(c, x + (i - 1) * 170, y, 160, PESSOAS[nome], nome, a, TINTA))
        E.foco(c, t, t0 + 0.4, 0.5, lambda a, x=x: bloco(c, x - 250, x + 250, y + 40, 300, a))
    E.sinal(c, t, C["s09.b"], "=", W / 2, y + 30, 150, CERTO)
    E.foco(c, t, C["s09.b"] + 0.2, 0.5, lambda a: E.centro(c, "mesmo grupo", W / 2, 840, 76, "g", CERTO, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "a ordem não importa: outra conta", W / 2, 970, 54, estilo="g", fundo=TINTA2, a=a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def nome():
        E.frase(c, t, C["s10.a"], ps("só alguns, numa ordem que importa", "i", 68, TINTA2), W / 2, 220, "center", passo=0.12)
        E.frase(c, t, C["s10.b"], [("arranjo", "g", 170, COR)], W / 2, 450, "center")
        E.formula_em(c, t, C["s10.c"], "A(8, 3)", W / 2, 690, 130, "g", TINTA, "center")
        E.foco(c, t, C["s10.c"] + 0.6, 0.5, lambda a: E.centro(c, "8 elementos, 3 a 3", W / 2, 810, 60, "i", TINTA2, a))
    E.saida(c, t, C["s11"] - 0.1, nome)
    if C["s11"] <= t < C["s12"] + 0.5:
        def formula():
            E.formula_em(c, t, C["s11.a"], "A(n, p)", 560, 470, 130, "g", TINTA, "center")
            E.foco(c, t, C["s11.a"] + 0.2, 0.5, lambda a: E.pilula(c, "n = total", 460, 720, 56, estilo="b", fundo=TINTA2, a=a))
            E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "p = quantos escolhe", 610, 860, 56, estilo="b", fundo=TINTA2, a=a))
            E.formula_em(c, t, C["s11.c"], "= f{n!}{(n − p)!}", 830, 500, 130, "g", COR)
        E.saida(c, t, C["s12"] - 0.1, formula)
    if C["s12"] <= t < C["s13"] + 0.5:
        def origem():
            E.frase(c, t, C["s12"] + 0.1, ps("de onde vem isso?", "i", 72, TINTA2), W / 2, 170, "center")
            corredores(c, t, C["s12.a"], W / 2, 360, 170, 140, fora=range(3, 8), tfora=C["s12.b"])
            E.formula_em(c, t, C["s12.a"] + 0.4, "8!", 170, 380, 110, "g", TINTA)
            E.foco(c, t, C["s12.a"] + 0.8, 0.4, lambda a: E.centro(c, "fila dos 8", 230, 470, 44, "i", TINTA2, a) if t < C["s12.b"] else None)
            if t >= C["s12.b"]:
                x0, x1 = W / 2 - 0.5 * 170 - 60, W / 2 + 3.5 * 170 + 60
                E.chave(c, x0, x1, 500, TINTA2, ep(t, C["s12.b"], 0.5))
                E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.centro(c, "5 fora do pódio: ordem não interessa", (x0 + x1) / 2, 580, 46, "i", TINTA2, a))
            # 8!/5! cortando
            tc = C["s12.d"]
            fracao_corte(c, t, C["s12.c"], 720, 820, 96, ["8", "×", "7", "×", "6", "×", "5!"], "5!", tcima=[C["s12.c"]] * 6 + [C["s12.c"]],
                         tc=tc, cortar=(6,))
            E.formula_em(c, t, tc + 0.5, "= 8 × 7 × 6", 1080, 852, 84, "g", COR)
            igual_bola(c, t, tc + 1.4, 1530, 825, "336", r=95)
            E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "÷ 5!", 230, 820, 56, estilo="g", a=a))
        E.saida(c, t, C["s13"] - 0.1, origem)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("todos", "g", 84, COR), ("entram:", "i", 84), ("p", "g", 84), ("=", "g", 84), ("n", "g", 84)], W / 2, 220, "center")
    E.formula_em(c, t, C["s13.a"] + 0.6, "A(n, n) = f{n!}{(n − n)!}", 260, 480, 110, "g", TINTA)
    E.formula_em(c, t, C["s13.b"], "(n − n)! = 0! = 1", 260, 720, 96, "g", TINTA2)
    E.formula_em(c, t, C["s13.c"], "A(n, n) = n!", 260, 920, 110, "g", COR)
    E.foco(c, t, C["s13.c"] + 0.6, 0.5, lambda a: E.pilula(c, "permutação", 1300, 885, 64, estilo="g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s14.a"], ps("fatorial do total", "i", 64, TINTA2), W / 2, 270, "center")
    E.formula_em(c, t, C["s14.b"], "8!", 520, 470, 120, "g", ERRADO, "right")
    E.formula_em(c, t, C["s14.c"], "= 40.320", 545, 470, 120, "g", ERRADO)
    corredores(c, t, C["s14.d"], W / 2, 690, 190, 130, fora=range(3, 8), tfora=C["s14.e"], nomes=True)
    E.foco(c, t, C["s14.d"] + 0.6, 0.5, lambda a: E.centro(c, "a ordem dos 8, até o último", W / 2, 910, 56, "i", TINTA, a) if t < C["s14.e"] else None)
    if t >= C["s14.e"]:
        x0, x1 = W / 2 - 3.5 * 190 - 70, W / 2 - 1.5 * 190 + 70
        E.foco(c, t, C["s14.e"], 0.5, lambda a: bloco(c, x0 + 10, x1 - 10, 720, 240, a))
        E.foco(c, t, C["s14.e"] + 0.3, 0.5, lambda a: E.centro(c, "o pódio só olha os 3 primeiros", W / 2, 990, 64, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def desce():
        E.frase(c, t, C["s15.a"], ps("multiplique descendo do total", "i", 76, BR), W / 2, 200, "center", passo=0.14)
        E.frase(c, t, C["s15.b"], [("um", "g", 76, BR), ("número", "i", 76, CLARO), ("por", "i", 76, CLARO), ("lugar", "g", 76, BR)], W / 2, 310, "center")
        y1, y2 = 520, 830
        E.frase(c, t, C["s15.c"], [("3", "g", 60, BR), ("lugares", "i", 56, CLARO)], XE, y1 - 10)
        E.frase(c, t, C["s15.c"] + 0.2, [("entre", "i", 56, CLARO), ("8", "g", 60, BR)], XE, y1 + 55)
        xs = casinhas(c, t, 860, y1, [("", v, C["s15.c"] + 0.4 + 0.2 * i, C["s15.c"] + 0.5 + 0.2 * i) for i, v in enumerate((8, 7, 6))], s=150, escuro=True)
        igual_bola(c, t, C["s15.c"] + 1.3, xs[2] + 140, y1, "336", r=95, cor=E.COR, escuro=True)
        E.frase(c, t, C["s15.d"], [("2", "g", 60, BR), ("lugares", "i", 56, CLARO)], XE, y2 - 10)
        E.frase(c, t, C["s15.d"] + 0.2, [("entre", "i", 56, CLARO), ("10", "g", 60, BR)], XE, y2 + 55)
        xs = casinhas(c, t, 738.5, y2, [("", v, C["s15.d"] + 0.4 + 0.2 * i, C["s15.d"] + 0.5 + 0.2 * i)
                                                                         for i, v in enumerate((10, 9))], s=150, escuro=True)
        igual_bola(c, t, C["s15.d"] + 1.2, xs[1] + 140, y2, "90", r=95, cor=E.COR, escuro=True)
    E.saida(c, t, C["s16"] - 0.1, desce)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("cada lugar: uma opção a menos", "i", 72, BR), W / 2, 200, "center", passo=0.14)
    E.frase(c, t, C["s16.a"] + 1.4, ps("a fórmula corta o resto", "i", 60, CLARO), W / 2, 300, "center", passo=0.12)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "não compensa: regra no meio", W / 2, 440, 56, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s16.b"] + 0.6, ps("zero não vai na frente", "i", 60, CLARO), W / 2, 560, "center", passo=0.12)
    if t >= C["s16.c"]:
        xs = casinhas(c, t, 820, 780, [("centena", 9, C["s16.c"], C["s16.c"] + 0.4), ("dezena", "?", C["s16.c"] + 0.1, C["s16.c"] + 0.4),
                                       ("unidade", "?", C["s16.c"] + 0.2, C["s16.c"] + 0.4)], s=140, gap=80, tx=[None, None], escuro=True)
        marca(c, t, C["s16.c"] + 0.5, xs[0], 780, 140, None, CLARO)
        E.foco(c, t, C["s16.c"] + 0.7, 0.5, lambda a: E.escreve(c, "comece pela mais difícil", 1180, 800, 56, "g", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s17.a"], [("clube", "i", 80), ("com", "i", 80), ("10", "g", 88, COR), ("sócios", "i", 80)], XE, 360)
    E.frase(c, t, C["s17.b"], [("presidente,", "g", 72), ("vice", "g", 72)], XE, 490)
    E.frase(c, t, C["s17.b"] + 0.6, [("e", "i", 72), ("tesoureiro", "g", 72)], XE, 590)
    E.frase(c, t, C["s17.c"], [("quantas", "i", 84), ("chapas?", "g", 92, COR)], XE, 740)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "antes: o teste da troca", XE + 330, 870, 50, estilo="b", fundo=TINTA2, a=a))
    E.relogio(c, t, C["s18.a"], 1500, 560, 200)


# ---------------- resposta ----------------
def cargos(c, x, y, nomes, a=1.0):
    """chapa: presidente e vice, cada um com o nome"""
    for i, (cargo, nome) in enumerate(zip(("presidente", "vice"), nomes)):
        yy = y + i * 100
        E.escreve(c, cargo, x, yy, 50, "i", TINTA2, a)
        E.escreve(c, nome, x + 290, yy, 56, "g", PESSOAS[nome], a)


def b_resposta(c, t, C, b):
    def teste():
        E.foco(c, t, C["s19"] + 0.1, 0.5, lambda a: E.pilula(c, "o teste da troca", W / 2, 180, 52, estilo="g", a=a))
        E.foco(c, t, C["s19.a"], 0.5, lambda a: cargos(c, 300, 420, ("Ana", "Bia"), a))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: cargos(c, 1180, 420, ("Bia", "Ana"), a))
        E.sinal(c, t, C["s19.b"] + 0.4, "≠", 960, 450, 130, ERRADO)
        E.frase(c, t, C["s19.c"], ps("cargos diferentes:", "i", 68), W / 2, 760, "center")
        E.frase(c, t, C["s19.c"] + 0.6, [("a", "i", 76), ("ordem", "g", 80, COR), ("importa:", "g", 80), ("arranjo", "g", 80, COR)], W / 2, 880, "center")
    E.saida(c, t, C["s20"] - 0.1, teste)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, [("3", "g", 76, COR), ("cargos,", "i", 76), ("descendo", "i", 76), ("do", "i", 76), ("10", "g", 76, COR)], W / 2, 190, "center")
    xs = casinhas(c, t, 760, 500, [("presidente", 10, C["s20.a"], C["s20.a"] + 0.3), ("vice", 9, C["s20.a"] + 0.15, C["s20.a"] + 0.5),
                                   ("tesoureiro", 8, C["s20.a"] + 0.3, C["s20.a"] + 0.7)], s=190, gap=150, tx=[C["s20.b"], C["s20.c"]])
    E.formula_em(c, t, C["s20.b"], "10 × 9 = 90", 300, 900, 96, "g", TINTA)
    E.formula_em(c, t, C["s20.c"], "90 × 8", 900, 900, 96, "g", TINTA)
    bx = igual_bola(c, t, C["s20.c"] + 0.5, 1260, 866, "720", r=110, cor=CERTO)
    E.foco(c, t, C["s20.c"] + 0.9, 0.5, lambda a: E.escreve(c, "chapas", bx + 135, 888, 64, "g", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s21.a", "só alguns, e a troca muda o resultado?", "é arranjo"),
                                         ("s21.b", "multiplique descendo do total", "um número por lugar"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68), 400, y - 10, passo=0.1)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 96, COR)], 400, y + 95)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("a", "i", 84), ("ordem", "g", 88, COR), ("não", "g", 88, COR), ("importa", "g", 88, COR)], XE, 450)
    E.frase(c, t, C["s22.b"], [("comissão", "g", 84), ("de", "i", 80), ("3", "g", 84, COR), ("entre", "i", 80), ("8", "g", 84, COR)], XE, 600)
    E.formula_em(c, t, C["s22.c"], "f{A(8, 3)}{3!}", XE, 790, 96, "g", TINTA)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(720, 425, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, podio=b_podio, troca=b_troca, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
