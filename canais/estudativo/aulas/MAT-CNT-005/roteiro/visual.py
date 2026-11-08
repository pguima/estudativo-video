"""Visual — Estudativo · MAT-CNT-005: permutação simples, filas e anagramas.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 004): casinhas() com o número de opções dentro, × entre elas,
igual_bola() com o resultado; casinha "fixo" (cheia) para o que já está decidido.
Peças desta aula:
- letra(): ficha de letra (anagramas). pessoa(): boneco com nome, para as filas.
- fila(): itens que trocam de lugar deslizando em arco, de um estado para outro (a permutação acontecendo na tela).
- bloco(): contorno arredondado na cor da matéria em volta de quem fica sempre junto.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-005_permutacao_simples.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("anagrama", "regra", "juntas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F = math.factorial
assert F(4) == 24 and F(3) == 6 and F(5) == 120 and F(4) * F(2) == 48 and 120 - 48 == 72 and F(6) == 720 and F(5) * 2 == 240
from itertools import permutations
assert sum(1 for p in permutations("ABCDE") if abs(p.index("A") - p.index("B")) == 1) == 48
assert sum(1 for p in permutations("BRASIL") if abs(p.index("A") - p.index("I")) == 1) == 240
assert sum(1 for p in permutations("AMOR") if p[0] == "A") == 6

PESSOAS = {"Ana": "#E08A3C", "Bia": "#8E5BD9", "p3": "#5B8DB8", "p4": "#55895A", "p5": "#9C9CA3"}


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


# ---------------- peças desta aula ----------------
def letra(c, cx, cy, s, ch, a=1.0, fundo=BR, tinta=TINTA, borda=TINTA):
    """ficha de letra, como as de jogo de palavras"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.16, s * 0.16)
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda, a, stroke=4))
    centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", tinta, a)


def pessoa(c, cx, cy, h, cor, nome=None, a=1.0, cor_nome=None):
    """boneco simples: cabeça e tronco; (cx, cy) = centro do tronco"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
    c.drawRRect(r, M.paint(cor, a))
    if nome:
        centro(c, nome, cx, cy + h * 0.38 + 56, 48, "b", cor_nome or TINTA, a)


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


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do bloco: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def palavras():
        est = [(C["s01.a"], list("AMOR")), (C["s01.b"], list("ROMA")), (C["s01.c"], list("RAMO")), (C["s01.d"], list("MORA"))]
        E.foco(c, t, C["s01.a"], 0.5, lambda a: fila(c, t, est, W / 2, 330, 190, lambda k, x, y: letra(c, x, y, 160, k, a)))
        E.frase(c, t, C["s01.d"] + 0.8, ps("mesmas letras, outra ordem", "i", 64, TINTA2), W / 2, 520, "center")
        t_cas = lerp(C["s01.d"], C["s01.e"], 0.75)
        xs = casinhas(c, t, 820, 750, [("", v, t_cas + 0.1 * i, t_cas + 0.2 + 0.15 * i) for i, v in enumerate((4, 3, 2, 1))], s=150, gap=80)
        igual_bola(c, t, C["s01.e"], xs[3] + 150, 750, "24", r=110)
    E.saida(c, t, C["s02"] - 0.1, palavras)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("filas", "g", 132), ("e", "i", 120)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("anagramas", "g", 132, COR)], XE, 630)
        E.frase(c, t, C["s02.b"], ps("com gente sempre junta", "i", 84), XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 210, "center")
    E.frase(c, t, C["s03.a"], [("duas", "g", 96, COR), ("coisas", "i", 96)], W / 2, 330, "center")
    for k, x, titulo in (("s03.b", 220, "casinha mais difícil"), ("s03.c", 1000, "fatorial")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 420, 700, 480, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 350, 520, "center")
    xs = casinhas(c, t, 570, 700, [("", 9, C["s03.b"] + 0.3, C["s03.b"] + 0.6), ("", "?", C["s03.b"] + 0.4, C["s03.b"] + 0.6),
                                   ("", "?", C["s03.b"] + 0.5, C["s03.b"] + 0.6)], s=120, gap=60, tx=[None, None])
    E.foco(c, t, C["s03.b"] + 0.8, 0.4, lambda a: E.caixa_pontilhada(c, xs[0] - 80, 620, 160, 160, a, E.COR, a))
    E.foco(c, t, C["s03.b"] + 0.9, 0.4, lambda a: E.centro(c, "comece por ela", 570, 850, 46, "i", TINTA2, a))
    E.formula_em(c, t, C["s03.c"] + 0.3, "4! = 4 × 3 × 2 × 1", 1350, 720, 76, "g", TINTA, "center")
    E.foco(c, t, C["s03.c"] + 0.8, 0.4, lambda a: E.centro(c, "todos os de baixo, até o 1", 1350, 830, 46, "i", TINTA2, a))


# ---------------- anagrama ----------------
def b_anagrama(c, t, C, b):
    def definicao():
        E.frase(c, t, C["s04.a"], [("anagrama", "g", 96, COR)], W / 2, 200, "center")
        E.frase(c, t, C["s04.a"] + 0.6, ps("cada ordem possível das letras", "i", 68), W / 2, 310, "center", passo=0.14)
        est = [(C["s04.a"] + 1.2, list("AMOR")), (C["s04.c"], list("RMOA"))]
        E.foco(c, t, C["s04.a"] + 1.2, 0.5, lambda a: fila(c, t, est, W / 2, 560, 190, lambda k, x, y: letra(c, x, y, 160, k, a)))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "com ou sem sentido", W / 2, 790, 54, estilo="b", fundo=TINTA2, a=a))
        E.foco(c, t, C["s04.c"] + 0.7, 0.5, lambda a: E.centro(c, "também conta", W / 2, 920, 64, "i", COR, a))
    E.saida(c, t, C["s05"] - 0.1, definicao)
    if t < C["s05"]:
        return

    def contar():
        E.frase(c, t, C["s05.a"], [("AMOR:", "g", 84), ("4", "g", 84, COR), ("letras", "i", 84), ("diferentes", "i", 84)], W / 2, 190, "center")
        for i, ch in enumerate("AMOR"):
            E.foco(c, t, C["s05.b"] + 0.3 * i, 0.4, lambda a, i=i, ch=ch: letra(c, W / 2 + (i - 1.5) * 130, 330, 100, ch, a))
        ks = ("s05.d", "s05.e", "s05.f", "s05.g")
        xs = casinhas(c, t, 640, 620, [(f"{i + 1}ª", 4 - i, C["s05.c"] + 0.15 * i, C[ks[i]]) for i in range(4)], s=170, gap=100,
                      tx=[C["s06.a"] + 0.2 * i for i in range(3)])
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "= 4!", xs[3] + 150, 620 + 40, 110, "g", TINTA, a))
        igual_bola(c, t, C["s06.c"], xs[3] + 420, 620, "24", r=110)
        E.foco(c, t, C["s06.c"] + 0.4, 0.5, lambda a: E.centro(c, "anagramas", xs[3] + 420 + 52 + 110, 830, 56, "g", COR, a))
    E.saida(c, t, C["s07"] - 0.1, contar)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("começando", "i", 84), ("com", "i", 84), ("A?", "g", 90, COR)], W / 2, 200, "center")
    xs = casinhas(c, t, 760, 520, [("1ª", "A", C["s07.b"] - 0.2, C["s07.b"], "fixo"), ("2ª", 3, C["s07.c"] - 0.6, C["s07.c"]),
                                   ("3ª", 2, C["s07.c"] - 0.5, C["s07.c"] + 0.2), ("4ª", 1, C["s07.c"] - 0.4, C["s07.c"] + 0.4)], s=170, gap=100,
                  tx=[None, C["s07.c"] + 0.5, C["s07.c"] + 0.6])
    E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: E.pilula(c, "1 opção", xs[0], 370, 44, estilo="b", fundo=TINTA2, a=a))
    if t >= C["s07.c"]:
        E.chave(c, xs[1] - 85, xs[3] + 85, 720, COR, ep(t, C["s07.c"] + 0.6, 0.5))
        E.formula_em(c, t, C["s07.c"] + 0.8, "3! = 6", (xs[1] + xs[3]) / 2, 840, 84, "g", COR, "center")
    igual_bola(c, t, C["s07.d"], xs[3] + 150, 520, "6", r=105)
    E.foco(c, t, C["s07.d"] + 0.3, 0.5, lambda a: E.centro(c, "começam com A", xs[3] + 150 + 58 + 105, 700, 50, "i", COR, a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def nome():
        E.frase(c, t, C["s08.a"] - 1.0, ps("trocar de lugar coisas todas diferentes", "i", 64, TINTA2), W / 2, 190, "center", passo=0.12)
        E.frase(c, t, C["s08.a"], [("permutação", "g", 150, COR)], W / 2, 380, "center")
        E.formula_em(c, t, C["s08.b"], "P = n!", W / 2, 590, 130, "g", TINTA, "center")
        E.foco(c, t, C["s08.b"] + 0.5, 0.5, lambda a: E.centro(c, "n = quantidade", W / 2, 690, 50, "i", TINTA2, a))
        E.frase(c, t, C["s08.b"] + 2.5, ps("cada casinha tem uma opção a menos:", "i", 56, TINTA2), W / 2, 850, "center", passo=0.1)
        E.frase(c, t, C["s08.b"] + 4.5, ps("quem já entrou não entra de novo", "i", 56, TINTA2), W / 2, 930, "center", passo=0.1)
    E.saida(c, t, C["s08.c"] - 0.1, nome)
    if t < C["s08.c"]:
        return
    E.frase(c, t, C["s08.c"], [("5", "g", 84, COR), ("pessoas", "i", 84), ("em", "i", 84), ("fila", "g", 84)], W / 2, 220, "center")
    for i, k in enumerate(("Ana", "Bia", "p3", "p4", "p5")):
        E.foco(c, t, C["s08.c"] + 0.4 + 0.15 * i, 0.4, lambda a, i=i, k=k: pessoa(c, 560 + i * 200, 520, 200, PESSOAS[k], None, a))
    E.formula_em(c, t, C["s08.d"], "5! = 5 × 4 × 3 × 2 × 1", 800, 840, 84, "g", TINTA, "center")
    igual_bola(c, t, C["s08.d"] + 0.6, 1300, 810, "120", r=105)
    E.foco(c, t, C["s08.d"] + 0.9, 0.5, lambda a: E.escreve(c, "filas", 1590, 830, 64, "g", COR, a))


# ---------------- juntas ----------------
NOMES = {"Ana": "Ana", "Bia": "Bia", "p3": None, "p4": None, "p5": None}


def b_juntas(c, t, C, b):
    y = 470

    def desenha(k, x, yy, a=1.0):
        pessoa(c, x, yy, 190, PESSOAS[k], NOMES[k], a, COR if k in ("Ana", "Bia") else None)

    # a fila: no começo, Ana e Bia separadas; no s10.a elas se colam; no s11 trocam dentro do bloco
    est = [(C["s09"], ["p3", "Ana", "p4", "Bia", "p5"]), (C["s10.a"], ["p3", "Ana", "Bia", "p4", "p5"])]
    if t >= C["s11.b"]:
        est.append((C["s11.b"], ["p3", "Ana", "Bia", "p4", "p5"]))
    if t >= C["s11.c"]:
        est.append((C["s11.c"], ["p3", "Bia", "Ana", "p4", "p5"]))
    passo_ = 230
    xs = fila(c, t, est, W / 2, y, passo_, lambda k, x, yy: E.foco(c, t, C["s09.a"] + 0.1 * list(PESSOAS).index(k), 0.4,
                                                                 lambda a: desenha(k, x, yy, a)), alto=150)
    E.saida(c, t, C["s11.a"] - 0.1, lambda: E.frase(c, t, C["s09.a"], [("5", "g", 80, COR), ("amigos", "i", 80), ("em", "i", 80), ("fila", "g", 80)],
                                                   W / 2, 170, "center"))
    E.frase(c, t, C["s11.a"], [("dentro", "i", 76), ("do", "i", 76), ("bloco,", "i", 76), ("elas", "i", 76), ("trocam", "g", 76, COR)], W / 2, 170, "center")
    if C["s09.b"] <= t < C["s10.a"] + 0.4:
        E.saida(c, t, C["s10.a"], lambda: E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "Ana e Bia sempre juntas", W / 2, 820, 54, estilo="b", a=a)))
    # o bloco
    if t >= C["s10.a"] + 0.5:
        x0, x1 = min(xs["Ana"], xs["Bia"]) - 95, max(xs["Ana"], xs["Bia"]) + 95
        E.foco(c, t, C["s10.a"] + 0.5, 0.5, lambda a: bloco(c, x0, x1, y + 40, 330, a))
        if t < C["s11.a"]:
            E.foco(c, t, C["s10.b"], 0.5, lambda a: E.pilula(c, "o bloco", (x0 + x1) / 2, y - 210, 46, estilo="g", a=a))
    if C["s10.c"] <= t < C["s10.d"] + 0.4:
        E.saida(c, t, C["s10.d"], lambda: E.foco(c, t, C["s10.c"], 0.5, lambda a: E.centro(c, "+ 3 amigos", W / 2, 840, 64, "i", TINTA2, a)))
    # a conta, embaixo
    yc = 960
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "4 peças", 330, yc - 30, 48, estilo="b", fundo=TINTA2, a=a))
    E.formula_em(c, t, C["s10.e"], "4! = 24", 520, yc, 90, "g", TINTA)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.centro(c, "Ana e Bia", W / 2, 840, 56, "b", COR, a) if t < C["s11.c"] else None)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.centro(c, "ou Bia e Ana", W / 2, 840, 56, "b", COR, a) if t < C["s11.d"] + 0.6 else None)
    E.formula_em(c, t, C["s11.d"], "× 2!", 920, yc, 90, "g", COR)
    E.foco(c, t, C["s11.d"] + 0.3, 0.5, lambda a: E.centro(c, "2 ordens", 990, yc + 70, 46, "i", COR, a))
    bx = igual_bola(c, t, C["s11.e"], 1200, yc - 32, "48", r=95)
    E.foco(c, t, C["s11.e"] + 0.3, 0.5, lambda a: E.escreve(c, "filas", bx + 120, yc - 10, 64, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s12.a"], ps("esqueceu a troca dentro do bloco", "i", 64, TINTA2), W / 2, 280, "center", passo=0.12)
    E.formula_em(c, t, C["s12.b"], "4! = 24", 300, 520, 110, "g", ERRADO)
    if t >= C["s12.b"] + 1.0:
        E.risco(c, 280, 480, 720, 480, t, C["s12.b"] + 1.0, largura=12)
    # as duas fotos
    for i, (ordem, x) in enumerate(((("Ana", "Bia"), 1020), (("Bia", "Ana"), 1580))):
        t0 = C["s12.c"] + 0.4 * i

        def foto(a, ordem=ordem, x=x):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 190, 360, 380, 380), 24, 24)
            c.drawRRect(r, M.paint(BR, a))
            c.drawRRect(r, M.paint(TINTA, a, stroke=4))
            for j, k in enumerate(ordem):
                pessoa(c, x - 85 + j * 170, 540, 170, PESSOAS[k], k, a, COR)
        E.foco(c, t, t0, 0.5, foto)
    E.sinal(c, t, C["s12.c"] + 0.6, "≠", 1300, 550, 120, ERRADO)
    E.foco(c, t, C["s12.c"] + 1.0, 0.5, lambda a: E.centro(c, "fotos diferentes", 1300, 830, 60, "i", TINTA, a))
    E.frase(c, t, C["s12.d"], [("bloco:", "g", 72, COR), ("multiplique", "i", 72), ("pelas", "i", 72), ("ordens", "g", 72), ("de", "i", 72),
                               ("dentro", "g", 72)], W / 2, 970, "center")
    E.formula_em(c, t, C["s12.d"] + 0.6, "24 × 2 = 48", 300, 680, 96, "g", CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def conta():
        E.frase(c, t, C["s13.a"], [("Ana", "g", 84, BR), ("e", "i", 84, CLARO), ("Bia", "g", 84, BR), ("separadas", "g", 84, CLARO)], W / 2, 200, "center")
        E.frase(c, t, C["s13.b"], [("conte", "i", 76, CLARO), ("todas", "g", 76, BR), ("e", "i", 76, CLARO), ("tire", "i", 76, CLARO),
                                   ("as", "i", 76, CLARO), ("juntas", "g", 76, BR)], W / 2, 330, "center")
        E.formula_em(c, t, C["s13.c"], "todas: 5! = 120", 420, 560, 90, "g", BR)
        E.formula_em(c, t, C["s13.c"] + 1.0, "juntas: 48", 420, 690, 90, "g", CLARO)
        E.formula_em(c, t, C["s13.d"], "120 − 48", 420, 880, 110, "g", BR)
        igual_bola(c, t, C["s13.d"] + 0.4, 920, 842, "72", r=105, cor=E.COR, escuro=True)
        E.foco(c, t, C["s13.d"] + 0.8, 0.5, lambda a: E.escreve(c, "separadas", 1215, 862, 64, "g", BR, a))
    E.saida(c, t, C["s14"] - 0.1, conta)
    if t < C["s14"]:
        return

    def grupos():
        E.frase(c, t, C["s14.a"], ps("cada fila cai em um grupo só", "i", 72, CLARO), W / 2, 200, "center")
        x, w, y, h = 260, 1400, 330, 120
        p = ep(t, C["s14.a"] + 0.6, 0.6)
        r1 = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w * 48 / 120 * p, h), 18, 18)
        c.drawRRect(r1, M.paint(E.COR))
        r2 = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w * 48 / 120, y, w * 72 / 120 * ep(t, C["s14.a"] + 1.0, 0.6), h), 18, 18)
        c.drawRRect(r2, M.paint(CLARO, 0.5))
        E.foco(c, t, C["s14.a"] + 0.8, 0.4, lambda a: E.centro(c, "juntas 48", x + w * 24 / 120, y + 80, 56, "g", BR, a))
        E.foco(c, t, C["s14.a"] + 1.2, 0.4, lambda a: E.centro(c, "separadas 72", x + w * 84 / 120, y + 80, 56, "g", BR, a))
    E.saida(c, t, C["s14.b"] - 0.1, grupos)
    if t < C["s14.b"]:
        return
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "não compensa: lugar fixo", W / 2, 240, 52, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s14.b"] + 0.5, ps("Ana na ponta esquerda", "i", 64, CLARO), W / 2, 380, "center")
    xs = casinhas(c, t, 740, 600, [("Ana", 1, C["s14.c"], C["s14.c"] + 0.3), ("", 4, C["s14.c"] + 0.5, C["s14.c"] + 0.7),
                                   ("", 3, C["s14.c"] + 0.6, C["s14.c"] + 0.8), ("", 2, C["s14.c"] + 0.7, C["s14.c"] + 0.9),
                                   ("", 1, C["s14.c"] + 0.8, C["s14.c"] + 1.0)], s=140, gap=70, escuro=True)
    E.foco(c, t, C["s14.c"] + 1.2, 0.5, lambda a: E.formula(c, "= 1 × 4! = 24", xs[4] + 110, 640, 76, "g", BR, a))
    E.foco(c, t, C["s14.c"] + 0.2, 0.5, lambda a: E.caixa_pontilhada(c, xs[0] - 90, 510, 180, 180, a, CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    for i, ch in enumerate("BRASIL"):
        forte = ch in "AI" and t >= C["s15.b"]
        E.foco(c, t, C["s15.a"] + 0.1 * i, 0.4, lambda a, i=i, ch=ch, forte=forte: letra(c, 260 + i * 150, 420, 130, ch, a,
                                                                                       E.COR if forte else BR, BR if forte else TINTA))
    E.frase(c, t, C["s15.a"] + 0.4, [("quantos", "i", 76), ("anagramas?", "g", 76, COR)], XE, 640)
    E.frase(c, t, C["s15.b"], [("e", "i", 76), ("com", "i", 76), ("as", "i", 76), ("vogais", "g", 76, COR), ("juntas?", "g", 76, COR)], XE, 780)
    E.relogio(c, t, C["s16.a"], 1520, 620, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def todas():
        E.frase(c, t, C["s17.a"], [("6", "g", 84, COR), ("letras", "i", 84), ("diferentes", "i", 84)], W / 2, 200, "center")
        for i, ch in enumerate("BRASIL"):
            E.foco(c, t, C["s17.b"] + 0.55 * i, 0.4, lambda a, i=i, ch=ch: letra(c, W / 2 + (i - 2.5) * 160, 420, 130, ch, a))
        E.formula_em(c, t, C["s17.c"], "6!", 700, 720, 130, "g", TINTA)
        igual_bola(c, t, C["s17.c"] + 0.4, 900, 680, "720", r=115)
        E.foco(c, t, C["s17.c"] + 0.7, 0.5, lambda a: E.escreve(c, "anagramas", 1215, 702, 64, "g", COR, a))
    E.saida(c, t, C["s18"] - 0.1, todas)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.1, [("vogais", "g", 80, COR), ("juntas", "g", 80, COR)], W / 2, 170, "center")
    y = 380
    est = [(C["s18"], ["B", "R", "A", "S", "I", "L"]), (C["s18.a"], ["A", "I", "B", "R", "S", "L"])]
    if t >= C["s18.d"]:
        est.append((C["s18.d"] + 0.3, ["I", "A", "B", "R", "S", "L"]))
    xs = fila(c, t, est, W / 2, y, 165, lambda k, x, yy: letra(c, x, yy, 130, k, 1.0, E.COR if k in "AI" else BR, BR if k in "AI" else TINTA), alto=120)
    if t >= C["s18.a"] + 0.5:
        x0, x1 = min(xs["A"], xs["I"]) - 65, max(xs["A"], xs["I"]) + 65
        E.foco(c, t, C["s18.a"] + 0.5, 0.5, lambda a: bloco(c, x0, x1, y, 130, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.centro(c, "bloco + 4 consoantes = 5 peças", W / 2, 640, 60, "i", TINTA, a))
    E.formula_em(c, t, C["s18.c"], "5! = 120", 330, 860, 96, "g", TINTA)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.escreve(c, "AI ou IA: 2", 330, 980, 56, "b", COR, a))
    E.formula_em(c, t, C["s18.e"], "120 × 2", 900, 860, 96, "g", TINTA)
    igual_bola(c, t, C["s18.e"] + 0.4, 1320, 826, "240", r=110, cor=CERTO)
    E.foco(c, t, C["s18.e"] + 1.6, 0.5, lambda a: E.escreve(c, "menos que 720", 1440, 990, 50, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s19.a", "tudo diferente, em fila?", "fatorial"), ("s19.b", "tem que ficar junto?", "bloco × trocas de dentro"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72), 400, y - 10)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 96, COR)], 400, y + 95)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20.a"], [("letras", "g", 120, COR), ("repetidas", "g", 120, COR)], XE, 450)
    for i, ch in enumerate("ARARA"):
        E.foco(c, t, C["s20.a"] + 0.6 + 0.1 * i, 0.4, lambda a, i=i, ch=ch: letra(c, XE + 50 + i * 115, 560, 95, ch, a))
    E.frase(c, t, C["s20.b"], [("e", "i", 84), ("mesa", "g", 90, COR), ("redonda", "g", 90, COR)], XE, 770)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, anagrama=b_anagrama, regra=b_regra, juntas=b_juntas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
